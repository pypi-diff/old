import os
import sys
import xmlrpc.client
import logging
import subprocess
import shutil
import pprint
import argparse
import time
from datetime import datetime
from dataclasses import dataclass
from threading import current_thread
from concurrent.futures import ThreadPoolExecutor, as_completed
from pypi_json import PyPIJSON
import serial
import packaging
import requests

jclient = PyPIJSON()

logFormat = (
    "%(asctime)s %(levelname)s %(name)s %(module)s - %(funcName)s"
    " [%(threadName)s]: %(message)s"
)
logDateFormat = "[%Y-%m-%d %H:%M:%S]"
logfile = datetime.now().strftime("%Y%d%m")
handler = [
    logging.FileHandler(logfile + ".log"),
]
logging.basicConfig(
    level=logging.INFO,
    format=logFormat,
    datefmt=logDateFormat,
    handlers=handler,
)

log = logging.getLogger()


@dataclass
class pkgInfo:
    name: str
    version: str


def main():
    parser = argparse.ArgumentParser(
        description="pypi-diff bot",
    )

    parser.add_argument(
        "-w",
        "--worker",
        default=5,
        required=False,
        help="Amount of workers to use",
    )
    parser.add_argument(
        "-p",
        "--packages",
        default="all",
        required=False,
        help="Process only specific packages, seperated by ','",
    )
    parser.add_argument(
        "-t",
        "--tmpdir",
        default="tmp",
        required=False,
        help="Default directory for storing temporary artifacts.",
    )
    parser.add_argument(
        "-o",
        "--output",
        default="versions",
        required=False,
        help="Default output directory.",
    )
    parser.add_argument(
        "-l",
        "--sizelimit",
        default=10485760,
        required=False,
        help="Skip if download packages exceed limit",
    )
    parser.add_argument(
        "-s",
        "--silent",
        default=False,
        action="store_true",
        required=False,
        help="Dont log to stderr",
    )

    args = parser.parse_args()

    if args.silent is False:
        log.handlers.append(logging.StreamHandler(stream=sys.stderr))

    client = xmlrpc.client.ServerProxy("https://pypi.org/pypi")

    serialLast = serial.read()
    if serialLast == "":
        log.info("No serial file found, fetching last serial via API")
        serialLast = client.changelog_last_serial()

    log.info("Get Changelog since Serial: [%s]", serialLast)

    # API Limit may reset in 1 seconds
    time.sleep(2)
    serialCur = client.changelog_last_serial()
    time.sleep(2)
    changelog = client.changelog_since_serial(int(serialLast))
    changedPackages = []

    for pkg in changelog:
        if pkg[3] == "new release":
            if args.packages != "all":
                if not pkg[0] in args.packages.split(","):
                    log.info("Ignoring package [%s], not in package list.", pkg[0])
                    continue
            changedPackages.append(pkgInfo(pkg[0], pkg[1]))

    if len(changedPackages) == 0:
        log.info("No changed packages found")
        serial.write(serialCur)
        sys.exit(1)

    log.info("Found %s changed packages", len(changedPackages))

    for path in [args.output, args.tmpdir]:
        if not os.path.exists(path):
            os.makedirs(path, exist_ok=True)

    with ThreadPoolExecutor(max_workers=args.worker) as executor:
        futures = {
            executor.submit(processPackages, args, jclient, p): p
            for p in changedPackages
        }
        for future in as_completed(futures):
            if future.result() is True:
                log.info("success")
            else:
                log.info("error")

    serial.write(serialCur)


def processPackages(args, jclient, p):
    current_thread().name = p.name
    try:
        releaseInfo = jclient.get_metadata(p.name)
    except packaging.requirements.InvalidRequirement as e:
        log.error("Unable to get metadata: %s", e)
        return False
    try:
        old = list(releaseInfo.releases.keys())[-2]
    except IndexError:
        log.warning("Skipping, unable to determine old version")
        return False
    new = list(releaseInfo.releases.keys())[-1]
    log.info("New version: [%s] Old Version: [%s]", new, old)

    if new == old:
        log.warning("Versions are the same, skipping..")
        return False

    diffPath = f"{args.output}/{p.name[0]}/{p.name}/{old}-{new}"
    repPath = f"{diffPath}/index.html"
    if os.path.exists(repPath):
        log.info("report already exists")
        return True

    diffOn = []
    for P in [old, new]:
        # TODO: figure out whats going on in these cases....
        try:
            url = jclient.get_metadata(p.name, P).urls[-1]["url"]
            filename = jclient.get_metadata(p.name, P).urls[-1]["filename"]
        except IndexError:
            log.warning("fallback to get urls: [%s]", P)
            log.warning(pprint.pprint(jclient.get_metadata(p.name, P).urls))
            log.warning(pprint.pprint(jclient.get_metadata(p.name, P)))
            try:
                url = jclient.get_metadata(p.name, P).urls[0]["url"]
                filename = jclient.get_metadata(p.name, P).urls[0]["filename"]
            except IndexError:
                log.warning("unable to get url for both version [%s]", P)
                log.warning(pprint.pprint(jclient.get_metadata(p.name, P).urls))
                return False
        except packaging.requirements.InvalidRequirement as err:
            logging.error("Unable to fetch info: %s", err)
            return False

        if filename.endswith(".whl"):
            filename = f"{filename}.zip"
        tf = f"{args.tmpdir}/{filename}"
        diffOn.append(tf)
        if not os.path.exists(tf):
            log.info("Downloading %s", url)
            pkgHeader = requests.head(url)
            if int(pkgHeader.headers["Content-length"]) >= args.sizelimit:
                log.warning(
                    "Skipping package: exceeds size limit %s>=%s",
                    pkgHeader.headers["Content-length"],
                    args.sizelimit,
                )
                return False
            pkgData = requests.get(url, allow_redirects=True)
            with open(tf, "wb") as fhf:
                fhf.write(pkgData.content)

    if not os.path.exists(diffPath):
        os.makedirs(diffPath, exist_ok=True)

    log.info("executing diffoscope")
    pwd = os.path.abspath(os.curdir)
    try:
        cmd = [
            "podman",
            "run",
            "--user",
            "0:0",
            "--rm",
            "-w",
            pwd,
            "-v",
            f"{pwd}/tmp:{pwd}/tmp:ro",
            "-v",
            f"{pwd}/versions:{pwd}/versions:rw",
            "registry.salsa.debian.org/reproducible-builds/diffoscope",
            "--no-progress",
            diffOn[0],
            diffOn[1],
            "--html",
            f"{diffPath}/index.html",
            "--text",
            f"{diffPath}/diff.txt",
            "--markdown",
            f"{diffPath}/diff.md",
        ]
        log.info(" ".join(cmd))
        exe = subprocess.run(
            cmd,
            check=False,
            timeout=180,  # 2 minutes timeout
            capture_output=True,
        )
    except subprocess.TimeoutExpired:
        log.error("Timeout during execution of pkgdiff")
        try:
            shutil.rmtree(diffPath)
        except:
            pass
        return False

    if exe.returncode >= 2:
        log.error("Diffoscope failed: %s", exe.stderr.decode())
        return False

    return True


if __name__ == "__main__":
    main()
