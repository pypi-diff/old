# Comparing `tmp/solcix-0.1.3.tar.gz` & `tmp/solcix-0.1.4.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "solcix-0.1.3.tar", max compression
+gzip compressed data, was "solcix-0.1.4.tar", max compression
```

## Comparing `solcix-0.1.3.tar` & `solcix-0.1.4.tar`

### file list

```diff
@@ -1,17 +1,16 @@
--rw-r--r--   0        0        0     5674 2023-04-06 13:35:08.183788 solcix-0.1.3/README.md
--rw-r--r--   0        0        0      935 2023-04-06 13:35:30.091923 solcix-0.1.3/pyproject.toml
--rw-r--r--   0        0        0     1103 2023-04-06 08:51:29.868152 solcix-0.1.3/solcix/__init__.py
--rw-r--r--   0        0        0     6993 2023-04-06 13:32:17.118795 solcix-0.1.3/solcix/__main__.py
--rw-r--r--   0        0        0       22 2023-04-06 13:35:25.067892 solcix-0.1.3/solcix/__version__.py
--rw-r--r--   0        0        0      182 2023-04-06 06:47:58.651981 solcix-0.1.3/solcix/compile/__init__.py
--rw-r--r--   0        0        0    19134 2023-04-06 09:25:41.021963 solcix-0.1.3/solcix/compile/solc.py
--rw-r--r--   0        0        0      618 2023-04-05 16:12:30.242253 solcix-0.1.3/solcix/constant.py
--rw-r--r--   0        0        0      110 2023-04-05 14:24:43.655338 solcix-0.1.3/solcix/datatypes/__init__.py
--rw-r--r--   0        0        0     3949 2023-04-06 08:39:27.233614 solcix-0.1.3/solcix/datatypes/datatypes.py
--rw-r--r--   0        0        0     3407 2023-04-06 08:32:26.769062 solcix-0.1.3/solcix/errors.py
--rw-r--r--   0        0        0    19449 2023-04-06 11:09:01.513052 solcix-0.1.3/solcix/installer.py
--rw-r--r--   0        0        0      247 2023-04-05 17:30:43.390279 solcix-0.1.3/solcix/manage/__init__.py
--rw-r--r--   0        0        0     4759 2023-04-06 13:22:11.056207 solcix-0.1.3/solcix/manage/manage.py
--rw-r--r--   0        0        0    10403 2023-04-05 18:06:59.201642 solcix-0.1.3/solcix/resolver.py
--rw-r--r--   0        0        0      597 2023-04-06 08:38:41.565504 solcix-0.1.3/solcix/utils.py
--rw-r--r--   0        0        0     6880 1970-01-01 00:00:00.000000 solcix-0.1.3/PKG-INFO
+-rw-r--r--   0        0        0     6356 2023-04-06 18:40:16.591860 solcix-0.1.4/README.md
+-rw-r--r--   0        0        0      935 2023-04-06 18:40:16.591860 solcix-0.1.4/pyproject.toml
+-rw-r--r--   0        0        0     1109 2023-04-06 18:40:16.591860 solcix-0.1.4/solcix/__init__.py
+-rw-r--r--   0        0        0     7884 2023-04-06 18:40:16.591860 solcix-0.1.4/solcix/__main__.py
+-rw-r--r--   0        0        0      182 2023-04-06 18:40:16.591860 solcix-0.1.4/solcix/compile/__init__.py
+-rw-r--r--   0        0        0    19181 2023-04-06 18:40:16.591860 solcix-0.1.4/solcix/compile/solc.py
+-rw-r--r--   0        0        0      618 2023-04-06 18:40:16.591860 solcix-0.1.4/solcix/constant.py
+-rw-r--r--   0        0        0      110 2023-04-06 18:40:16.591860 solcix-0.1.4/solcix/datatypes/__init__.py
+-rw-r--r--   0        0        0     3949 2023-04-06 18:40:16.591860 solcix-0.1.4/solcix/datatypes/datatypes.py
+-rw-r--r--   0        0        0     3407 2023-04-06 18:40:16.591860 solcix-0.1.4/solcix/errors.py
+-rw-r--r--   0        0        0    21421 2023-04-06 18:40:16.591860 solcix-0.1.4/solcix/installer.py
+-rw-r--r--   0        0        0      241 2023-04-06 18:40:16.591860 solcix-0.1.4/solcix/manage/__init__.py
+-rw-r--r--   0        0        0     3773 2023-04-06 18:40:16.591860 solcix-0.1.4/solcix/manage/manage.py
+-rw-r--r--   0        0        0    10656 2023-04-06 18:40:16.591860 solcix-0.1.4/solcix/resolver.py
+-rw-r--r--   0        0        0      597 2023-04-06 18:40:16.591860 solcix-0.1.4/solcix/utils.py
+-rw-r--r--   0        0        0     7562 1970-01-01 00:00:00.000000 solcix-0.1.4/PKG-INFO
```

### Comparing `solcix-0.1.3/README.md` & `solcix-0.1.4/README.md`

 * *Files 7% similar despite different names*

```diff
@@ -64,20 +64,20 @@
 
 ```bash
 solcix versions
 ```
 
 ### Listing installed Solidity compilers
 
-The `versions` command can be used to list all available versions of the Solidity compiler:
+The `ls` command can be used to list all available versions of the Solidity compiler:
 
 Example usage:
 
 ```bash
-solcix installed
+solcix ls
 ```
 
 If global / local version is set, it will be displayed as below:
 
 ```bash
 0.8.19
 0.5.2
@@ -126,15 +126,15 @@
 
 To uninstall all versions of Solidity compiler that have been installed using solcix, you can use the following command:
 
 ```bash
 solcix prune
 ```
 
-This will remove all versions of the Solidity compiler that have been installed by solcix.
+This will remove all versions of the Solidity compilers that have been installed by solcix, all cached files, and the solcix configuration file (local config takes precedence over global config).
 
 ### Verify Solidity compilers
 
 The `verify` command is used to verify the checksums of installed solc binaries and to reinstall any that are malformed.
 
 Example usage:
 
@@ -226,7 +226,15 @@
 
 ```bash
 pip3 install -U
 
 # Migrate to the new architecture and Reinstall all binaries
 solcix upgrade
 ```
+
+### Project Acknowledgements
+
+We would like to thank the original projects [solc-select](https://github.com/crytic/solc-select) and [py-solc-x](https://github.com/ApeWorX/py-solc-x) for providing excellent code base, upon which we have optimized and improved to make the project more robust and user-friendly.
+
+Our project is an improved and optimized version of solc-select and py-solc-x, with more features and excellent performance.
+
+If you enjoyed the original projects, we strongly recommend trying out our project to enjoy a better user experience and more efficient code execution.
```

### Comparing `solcix-0.1.3/pyproject.toml` & `solcix-0.1.4/pyproject.toml`

 * *Files 11% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 [tool.poetry]
 name = "solcix"
-version = "0.1.3"
+version = "0.1.4"
 description = "A Python wrapper for the Solidity compiler. Switch between versions, compile, and manage artifacts."
 authors = ["alan890104 <alan890104@gmail.com>"]
 readme = "README.md"
 
 [tool.poetry.dependencies]
 python = "^3.8"
 cfgv = "3.3.1"
```

### Comparing `solcix-0.1.3/solcix/__init__.py` & `solcix-0.1.4/solcix/__init__.py`

 * *Files 2% similar despite different names*

```diff
@@ -1,42 +1,42 @@
 import os
 from .constant import ARTIFACT_DIR
-from .__version__ import __version__
 from .installer import (
     get_available_versions,
     get_installable_versions,
     get_installed_versions,
     get_latest_version,
     get_executable,
     clear_cache,
     install_solc,
     uninstall_solc,
     verify_solc,
+    current_version,
 )
 from .resolver import (
     get_compatible_versions,
     get_recommended_version,
     install_solc_from_solidity,
     resolve_version_from_solidity,
 )
-
 from . import datatypes, compile, manage
 
 
 __all__ = [
     # Installer
     "get_available_versions",
     "get_installable_versions",
     "get_installed_versions",
     "get_latest_version",
     "get_executable",
     "clear_cache",
     "install_solc",
     "uninstall_solc",
     "verify_solc",
+    "current_version",
     # Resolver
     "get_compatible_versions",
     "get_recommended_version",
     "install_solc_from_solidity",
     "resolve_version_from_solidity",
     # Compile
     "compile",
```

### Comparing `solcix-0.1.3/solcix/__main__.py` & `solcix-0.1.4/solcix/__main__.py`

 * *Files 6% similar despite different names*

```diff
@@ -1,21 +1,19 @@
-import os
 import sys
 import json
 import textwrap
 from typing import List, Union
 import pyfiglet
 import subprocess
 
 import click
 from colorama import Fore, Style
 
 import solcix.installer
 import solcix.resolver
-from solcix.__version__ import __version__
 from solcix.datatypes import Version
 from solcix.errors import NotInstalledError
 from .constant import ARTIFACT_DIR
 
 CONTEXT_SETTINGS = dict(
     help_option_names=["-h", "--help"],
 )
@@ -23,15 +21,15 @@
 WELCOME_MESSAGE = (
     f"{Fore.YELLOW}{pyfiglet.figlet_format('welcome to solcix')}{Style.RESET_ALL}"
 )
 VERSION_INFO = f"version  |  %(version)s \n"
 
 # fmt: off
 @click.group(context_settings=CONTEXT_SETTINGS, invoke_without_command=True, no_args_is_help=True,)
-@click.version_option(version=__version__, prog_name="solcix", message=f"{Fore.YELLOW}{pyfiglet.figlet_format('welcome to solcix')}{Style.RESET_ALL} {VERSION_INFO}")
+@click.version_option(package_name="solcix", message=f"{Fore.YELLOW}{pyfiglet.figlet_format('welcome to solcix')}{Style.RESET_ALL} {VERSION_INFO}")
 def cli():
     pass
 
 
 @cli.command(help="Install solc binaries.")
 @click.argument("version", nargs=-1, required=True, type=click.STRING)
 @click.option("--use-cache/--no-use-cache", default=True, is_flag=True)
@@ -39,36 +37,44 @@
     success, skipped, error = solcix.installer.install_solc(version, use_cache)
     print(Fore.GREEN + f"success: {', '.join(success)}" + Style.RESET_ALL)
     print(Fore.YELLOW + f"skipped: {', '.join(skipped)}" + Style.RESET_ALL)
     print(Fore.RED + f"error  : {', '.join(error)}" + Style.RESET_ALL)
 
 
 @cli.command(help="List available solc versions.")
-def versions():
+def ls():
     releases, latest = solcix.get_available_versions()
     for release, artifact in releases.items():
         print(f"release: {release:6s} | artifact: {artifact}")
     print(Fore.GREEN + f"latest: {latest}" + Style.RESET_ALL)
 
 
 @cli.command(help="List all installed solc versions.")
 def installed():
     installed = solcix.get_installed_versions()
     installed = sorted(installed, key=Version)
     try:
-        current, _ = solcix.manage.current_version()
+        current, _ = solcix.current_version()
         for version in installed:
             if current == version:
                 print(Fore.GREEN + f"{version} <- current" + Style.RESET_ALL)
             print(version)
     except NotInstalledError as e:
         print(Fore.YELLOW + f"{e}" + Style.RESET_ALL)
         for version in installed:
             print(version)
 
+@cli.command(help="Show current solc version.")
+def current():
+    try:
+        current, _ = solcix.current_version()
+        print(f"{Fore.GREEN}solc-{current}{Style.RESET_ALL} is currently used.")
+    except NotInstalledError as e:
+        print(Fore.YELLOW + f"{e}" + Style.RESET_ALL)
+
 
 @cli.command(help="Switch between solc versions. If the version is not installed, it will be installed.")
 @click.argument("scope", nargs=1, required=True, type=click.Choice(["global", "local"]))
 @click.argument("version", nargs=1, required=True, type=click.STRING)
 def use(scope: str, version: str):
     if scope == "global":
         solcix.manage.switch_global_version(version, True)
@@ -82,54 +88,71 @@
     success, skipped, error = solcix.uninstall_solc(version)
     print(Fore.GREEN + f"success: {', '.join(success)}" + Style.RESET_ALL)
     print(Fore.YELLOW + f"skipped: {', '.join(skipped)}" + Style.RESET_ALL)
     print(Fore.RED + f"error  : {', '.join(error)}" + Style.RESET_ALL)
 
 @cli.command(help="Uninstall all solc binaries.")
 def prune():
+    opt = click.confirm(default=False, text="Are you sure to uninstall all solc binaries, caches, and config files?")
+    if opt is False:
+        print(f"{Fore.YELLOW}You have canceled the operation. Indeed, a wise choice!{Style.RESET_ALL}")
+        return
+    # Delete all cached versions
+    solcix.clear_cache()
+    # Delete all config files
+    solcix.manage.clear_config()
+    # Delete all installed versions
     versions = solcix.get_installed_versions()
     success, skipped, error = solcix.uninstall_solc(versions)
     print(Fore.GREEN + f"success: {', '.join(success)}" + Style.RESET_ALL)
     print(Fore.YELLOW + f"skipped: {', '.join(skipped)}" + Style.RESET_ALL)
     print(Fore.RED + f"error  : {', '.join(error)}" + Style.RESET_ALL)
 
+
 @cli.command(help="Verify checksums of installed solc binaries, and reinstall malformed ones.")
 @click.argument("version", nargs=-1, required=True, type=click.STRING)
 def verify(version: Union[List[str], str]):
     solcix.verify_solc(version)
 
 @cli.command(help="Remove all cached files.")
 def clear():
     solcix.clear_cache()
 
 
-@cli.command(context_settings=dict(ignore_unknown_options=True), help="Compile Solidity files and print the result, if the output is a TTY, the result will be formatted. Otherwise the result will be printed as a JSON string.")
+@cli.command(context_settings=dict(ignore_unknown_options=True, allow_extra_args=True), help="Compile Solidity files and print the result, if the output is a TTY, the result will be formatted. Otherwise the result will be printed as a JSON string. If you want to show the help message of solc, please use `solc --help`.")
 @click.argument("file", nargs=1, required=True, type=click.Path(exists=True))
 @click.option("-o", "--output", default=None, type=click.Path(), help="Output directory, will be create if not exists.")
-@click.argument("kwargs", nargs=-1, type=click.UNPROCESSED)
-def compile(file: str, output: str, **kwargs):
+@click.pass_context
+def compile(ctx: click.Context, file: str, output: str):
+    params = dict([item.strip('--').split('=') for item in ctx.args])
+    params["source_files"] = file
     if output is not None:
-        os.makedirs(output, exist_ok=True)
-        kwargs["output_dir"] = output
-    compile_result = solcix.compile.compile_files(file, **kwargs)
+        params["output_dir"] = output
+    try:
+        version = solcix.install_solc_from_solidity(source=file)
+        params["solc_version"] = version
+    except Exception as e:
+        print(e)
+        sys.exit(1)
+    compile_result = solcix.compile.compile_files(**params)
     if output is not None:
         print(f"Compilation result is saved in the output directory {output}.")
     else:
         if sys.stdout.isatty():
             width = 70
             wrapper = textwrap.TextWrapper(width=width, initial_indent="    ", subsequent_indent="    ")
             for contract, result in compile_result.items():
                 print(Fore.GREEN +  f"Contract: {contract}" )
                 for field, value in result.items():
                         print(Fore.BLUE + f"  {field}"+ Style.RESET_ALL)
                         shortend_str = textwrap.shorten(f"    {value}", width=width*5, placeholder="...")
                         padded_str = wrapper.fill(shortend_str)
                         print(padded_str)
             print(Fore.CYAN + "* Output to directory by", Fore.YELLOW + "`solcix compile <FILE> -o <output dir>`" + Style.RESET_ALL)
-            print(Fore.CYAN + "* Print to a single json file by", Fore.YELLOW + "`solcix compile <FILE> <filename>.json`" + Style.RESET_ALL, "to view whole result.")
+            print(Fore.CYAN + "* Print to a single json file by", Fore.YELLOW + "`solcix compile <FILE> <output file>.json`" + Style.RESET_ALL, "to view whole result.")
         else:
             print(json.dumps(compile_result, indent=4, sort_keys=True))
 
 
 @cli.command()
 @click.argument("file", nargs=1, required=True, type=click.Path(exists=True, dir_okay=False, readable=True))
 @click.option("--recommand/--no-recommand", default=True, is_flag=True)
@@ -148,16 +171,15 @@
 @cli.command()
 def upgrade():
     solcix.manage.upgrade_architecture()
 
 
 def solc() -> None:
     try:
-        current = solcix.manage.current_version()
-        version, _ = current
+        version, _  = solcix.current_version()
         path = ARTIFACT_DIR.joinpath(f"solc-{version}", f"solc-{version}")
         subprocess.run([str(path), *sys.argv[1:]], check=True)
     except NotInstalledError as e:
         print(Fore.RED + str(e) + Style.RESET_ALL)
         sys.exit(1)
     except subprocess.CalledProcessError as e:
         sys.exit(e.returncode)
```

### Comparing `solcix-0.1.3/solcix/compile/solc.py` & `solcix-0.1.4/solcix/compile/solc.py`

 * *Files 2% similar despite different names*

```diff
@@ -22,15 +22,15 @@
 ) -> Tuple[str, str, List[str], subprocess.Popen]:
     """
     This is an `low level function` which execute the solc binary with given arguments and return stdout, stderr, command and Popen object.
 
     Parameters
     ----------
         - solc_path: Optional path to solc binary.
-            - default to `solc` if not provided.
+            - default to local or global `solc` if not provided.
         - stdin: Optional string to pass as standard input to the solc process.
         - source_files: Optional list of source files to compile.
         - import_remappings: Optional import remappings as either dict, list or string.
         - **kwargs: Optional solc options and values.
 
     Returns
     -------
@@ -127,17 +127,15 @@
     evm_version: Optional[str] = None,
     revert_strings: Optional[Union[List[str], str]] = None,
     metadata_hash: Optional[str] = None,
     metadata_literal: bool = False,
     optimize: bool = False,
     optimize_runs: Optional[int] = None,
     optimize_yul: bool = False,
-    no_optimize_yul: bool = True,
     yul_optimizations: Optional[int] = None,
-    **kwargs: Any,
 ):
     """
     Compile Solidity source code into EVM bytecode.
 
     Parameters:
     -----------
     - source : str
@@ -168,16 +166,14 @@
         - Whether to use the metadata string as a literal or as a path to a file.
     - optimize : bool
         - Whether to enable bytecode optimization.
     - optimize_runs : Optional[int]
         - The number of optimization runs to perform.
     - optimize_yul : bool
         - Whether to optimize Yul code.
-    - no_optimize_yul : bool
-        - Whether to disable Yul optimization.
     - yul_optimizations : Optional[int]
         - The level of Yul optimizations to perform.
 
     Returns:
     --------
     A dictionary containing the compiled contract artifacts.
     """
@@ -194,15 +190,14 @@
         evm_version=evm_version,
         revert_strings=revert_strings,
         metadata_hash=metadata_hash,
         metadata_literal=metadata_literal,
         optimize=optimize,
         optimize_runs=optimize_runs,
         optimize_yul=optimize_yul,
-        no_optimize_yul=no_optimize_yul,
         yul_optimizations=yul_optimizations,
     )
 
 
 def compile_files(
     source_files: Union[List[Union[str, Path]], str, Path],
     solc_path: Optional[Union[str, Path]] = None,
@@ -216,17 +211,15 @@
     evm_version: Optional[str] = None,
     revert_strings: Optional[Union[List[str], str]] = None,
     metadata_hash: Optional[str] = None,
     metadata_literal: bool = False,
     optimize: bool = False,
     optimize_runs: Optional[int] = None,
     optimize_yul: bool = False,
-    no_optimize_yul: bool = True,
     yul_optimizations: Optional[int] = None,
-    **kwargs: Any,
 ):
     """
         Compile Solidity source code files into EVM bytecode.
 
     Parameters:
     -----------
     - source_files : Union[List[Union[str, Path]], str, Path]
@@ -284,28 +277,26 @@
         evm_version=evm_version,
         revert_strings=revert_strings,
         metadata_hash=metadata_hash,
         metadata_literal=metadata_literal,
         optimize=optimize,
         optimize_runs=optimize_runs,
         optimize_yul=optimize_yul,
-        no_optimize_yul=no_optimize_yul,
         yul_optimizations=yul_optimizations,
     )
 
 
 def compile_standard(
     input_data: Dict[str, Any],
     solc_path: Optional[Union[str, Path]] = None,
     solc_version: Optional[str] = None,
     base_path: Optional[str] = None,
     allow_paths: Optional[Union[List[Union[str, Path]], str, Path]] = None,
     output_dir: Optional[Union[str, Path]] = None,
     overwrite: bool = False,
-    **kwargs: Any,
 ) -> Dict[str, Any]:
     """
     Compile Solidity contracts from standard JSON input.
 
     Parameters:
     - input_data (Dict[str, Any]): The standard JSON input containing the Solidity contract(s) to compile.
     - solc_path (Optional[Union[str, Path]]): The path to the solc binary to use. If not specified, the latest version of solc available on the system will be used.
@@ -391,15 +382,26 @@
     >>> _get_combined_json_outputs('/usr/local/bin/solc')
     'bin,abi,interface,metadata,ir,ast'
 
     """
     if solc_path is None:
         solc_path = get_executable()
 
-    help_str = solc_execute(solc_path=solc_path, help=True)[0].split("\n")
+    # help_str = solc_execute(solc_path=solc_path, help=True)[0].split("\n")
+
+    # Execute solc with the `--help` flag to get the combined JSON output options.
+    cmd = [str(solc_path), "--help"]
+    output = subprocess.run(
+        cmd,
+        check=False,
+        stdout=subprocess.PIPE,
+        stderr=subprocess.PIPE,
+    )
+    help_str = output.stdout.decode("utf-8").split("\n")
+
     combined_json_args = next(i for i in help_str if i.startswith("  --combined-json"))
     return combined_json_args.split(" ")[-1]
 
 
 def _parse_compiler_output(stdout: str) -> Dict[str, Any]:
     """
     Parses the compiler output from JSON to a dictionary.
```

### Comparing `solcix-0.1.3/solcix/constant.py` & `solcix-0.1.4/solcix/constant.py`

 * *Files identical despite different names*

### Comparing `solcix-0.1.3/solcix/datatypes/datatypes.py` & `solcix-0.1.4/solcix/datatypes/datatypes.py`

 * *Files identical despite different names*

### Comparing `solcix-0.1.3/solcix/errors.py` & `solcix-0.1.4/solcix/errors.py`

 * *Files identical despite different names*

### Comparing `solcix-0.1.3/solcix/installer.py` & `solcix-0.1.4/solcix/installer.py`

 * *Files 3% similar despite different names*

```diff
@@ -3,40 +3,40 @@
 import os
 import shutil
 import sys
 from collections import defaultdict
 from glob import glob
 from os import access, makedirs
 from pathlib import Path
-from typing import Iterable, List, Tuple, Union
+from typing import Iterable, List, Tuple, Union, Optional, Set, Dict, Any
 from urllib.request import urlopen, urlretrieve
 from zipfile import ZipFile
 
 from Crypto.Hash import keccak
 from joblib import Memory
 
-from solcix.__version__ import __version__
 from solcix.constant import (
     ARTIFACT_DIR,
+    SOLCIX_DIR,
     CRYTIC_SOLC_ARTIFACTS,
     CRYTIC_SOLC_JSON,
     EarliestRelease,
     Platform,
 )
 from solcix.datatypes import ProgressBar, Version
 from solcix.errors import (
     ChecksumMismatchError,
     ChecksumMissingError,
     NoSolcVersionInstalledError,
     UnsupportedPlatformError,
+    NotInstalledError,
 )
 
-from .utils import is_valid_version
-
-cachedir = ARTIFACT_DIR.joinpath(".solcix", "cache", __version__)
+cachedir = ARTIFACT_DIR.joinpath(".solcix", "cache")
+os.makedirs(cachedir, exist_ok=True)
 memory = Memory(cachedir, verbose=0)
 
 
 def clear_cache() -> None:
     """
     Clears the cache directory used by `solc_execute` and `solcx.compile_*` functions.
 
@@ -90,15 +90,15 @@
     return (
         f"https://binaries.soliditylang.org/{platform.value}/{artifact}",
         f"https://binaries.soliditylang.org/{platform.value}/list.json",
     )
 
 
 @memory.cache
-def get_available_versions() -> Tuple[dict[str, str], str]:
+def get_available_versions() -> Tuple[Dict[str, str], str]:
     """
     Returns a tuple containing a dictionary of available Solidity compiler versions and the latest version.
 
     Returns
     -------
         tuple[dict[str], str]: A tuple containing a sorted dictionary of available Solidity compiler versions and the latest version.
 
@@ -126,35 +126,82 @@
             releases.update(extra)
 
     # Return the available versions and latest version as a tuple
     releases = {k: v for k, v in sorted(releases.items(), key=lambda x: Version(x[0]))}
     return releases, latest
 
 
-def get_installed_versions() -> set[str]:
+def get_installed_versions() -> Set[str]:
     """Returns a set of installed versions."""
     return {f.removeprefix("solc-") for f in glob("solc-*", root_dir=ARTIFACT_DIR)}
 
 
-def get_installable_versions() -> list[str]:
+def get_installable_versions() -> List[str]:
     """Returns a list of installable versions ordered by version."""
     releases, _ = get_available_versions()
     installable = list(set(releases.keys()) - get_installed_versions())
     installable.sort(key=Version)
     return installable
 
 
 def get_latest_version() -> str:
     """Returns the latest version of Solidity."""
     _, latest = get_available_versions()
     return latest
 
 
+def current_version() -> Tuple[str, str]:
+    """
+    Get the current version of the Solidity compiler.
+    Local version takes precedence over global version.
+
+    Raises
+    ------
+    NotInstalledError
+        If no version is set.
+
+    Returns:
+    --------
+    A tuple containing the current version and the path of the version information.
+    """
+    if os.path.isfile(".solcix"):
+        with open(".solcix", "r", encoding="utf-8") as f:
+            version = f.read()
+            source = ".solcix"
+    else:
+        source: str = "SOLC_VERSION"
+        version: Any = os.environ.get(source)
+
+    if not version:
+        source_path = SOLCIX_DIR.joinpath("global-version")
+        source = source_path.as_posix()
+
+        if source_path.is_file():
+            with open(source_path, encoding="utf-8") as f:
+                version = f.read()
+        else:
+            raise NotInstalledError(
+                "💫 No solc version set. Run `solcix use global VERSION`, `solcix use local Version` or set SOLC_VERSION environment variable. 💫"
+            )
+
+    versions: List[str] = get_installed_versions()
+
+    if version not in versions:
+        raise NotInstalledError(
+            f"\n😱 Version '{version}' not installed (set by {source}). 😱"
+            f"\nRun `solcix install {version}`."
+            f"\nOr use one of the following versions:\n"
+            f"{', '.join(versions)}"
+        )
+
+    return version, source
+
+
 @memory.cache
-def _get_version_dict(releases: dict[str, str]) -> dict[int, dict[int, dict[int, str]]]:
+def _get_version_dict(releases: Dict[str, str]) -> Dict[int, Dict[int, Dict[int, str]]]:
     """
     Returns a nested dictionary of Solidity compiler releases, organized by major, minor, and patch version numbers.
 
     Parameters
     ----------
         releases (dict[str, str]): A sorted dictionary of Solidity compiler releases, where the keys are version numbers and the values are artifact names.
 
@@ -185,15 +232,15 @@
     for version, artifact in releases.items():
         major, minor, patch = map(int, version.split("."))
         version_dict[major][minor][patch] = artifact
     return version_dict
 
 
 @memory.cache
-def get_version_objects(releases: dict[str, str]) -> list[Version]:
+def get_version_objects(releases: Dict[str, str]) -> List[Version]:
     """
     Retrieve a list of Version objects from a dictionary of release versions.
 
     Parameters
     ----------
         releases: A dictionary of release versions, where the keys are version
             strings and the values are release dates.
@@ -347,36 +394,46 @@
         return EarliestRelease.LINUX.value
     elif _get_platform() == Platform.MACOS:
         return EarliestRelease.MACOS.value
     elif _get_platform() == Platform.WINDOWS:
         return EarliestRelease.WINDOWS.value
 
 
-def _get_default_solc_path(program: Union[str, Path]) -> Union[Path, None]:
-    def is_executable(path: Path) -> bool:
-        return path.is_file() and access(path, os.X_OK)
-
-    fpath, _ = os.path.split(program)
-    if fpath:
-        if is_executable(fpath):
-            return program
-    else:
-        for path in os.environ["PATH"].split(os.pathsep):
-            path = path.strip('"')
-            exe_file = Path(path).joinpath(program)
-            if is_executable(exe_file):
-                return exe_file
+def _get_default_solc_path() -> Optional[Path]:
+    """
+    Returns the default path to the solc binary.
+
+    The function tries to determine the current version of solc and returns the path to the solc binary
+    for that version. If the binary is not found or is not executable, None is returned.
+
+    Returns:
+        Path or None: The path to the solc binary for the current version of solc, or None if the binary
+        cannot be found or is not executable.
+    """
+    try:
+        version = None
+        _, path = current_version()
+        with open(path, "r") as f:
+            version = f.read().strip()
+        executable = ARTIFACT_DIR.joinpath(f"solc-{version}", f"solc-{version}")
+        executable = executable.as_posix()
+        # If the binary exists and is executable, return its path
+        if os.path.isfile(executable) and access(executable, os.X_OK):
+            return executable
+    except Exception as e:
+        print(e)
+    # If the binary cannot be found or is not executable, return None
     return None
 
 
 def install_solc(
-    versions: str | Iterable[str],
+    versions: Union[str, Iterable[str]],
     use_cache: bool = True,
     verbose: bool = True,
-) -> tuple[list[str], list[str], list[str]]:
+) -> Tuple[List[str], List[str], List[str]]:
     """
     Downloads and installs Solidity compiler versions specified in the `versions` parameter.
 
     Parameters
     ----------
     - versions : str | Iterable[str]
         The version(s) of the Solidity compiler to download and install. If a string is provided,
@@ -483,20 +540,20 @@
     return success, skipped, errors
 
 
 def get_executable(
     version: Union[str, Version] = None, solc_path: Union[Path, str] = None
 ) -> Union[Path, None]:
     """
-    Get the path of the installed solc binary.
+    Get the path of the installed solc binary. Default is the local or global installed solc binary.
 
     Parameters
     ----------
     version: str or Version, optional
-        The version of solc to look for. If None, returns the default installed solc binary.
+        The version of solc to look for. If None, returns local or global installed solc binary.
     solc_path: Path or str, optional
         The path to a solc binary. If provided, ignores version param and returns the path to the binary if it exists.
 
     Returns
     -------
     Path or None
         Returns the path of the installed solc binary if it exists, otherwise returns None.
@@ -511,30 +568,29 @@
         if executable_path.exists():
             return executable_path
         raise NoSolcVersionInstalledError(
             f"solc binary not found at path: {executable_path}"
         )
 
     if version is None:
-        default_executable_path = _get_default_solc_path("solc")
+        default_executable_path = _get_default_solc_path()
         if default_executable_path is None:
             raise NoSolcVersionInstalledError("No default solc binary found")
         return default_executable_path
 
-    artifact_parent = Path(ARTIFACT_DIR.joinpath(f"solc-{version}"))
-    artifact_path = Path(artifact_parent.joinpath(f"solc-{version}"))
+    artifact_path = Path(ARTIFACT_DIR.joinpath(f"solc-{version}"), f"solc-{version}")
 
     if not artifact_path.exists():
         raise NoSolcVersionInstalledError(f"solc version {version} is not installed")
 
     return artifact_path
 
 
 def uninstall_solc(
-    versions: str | Iterable[str],
+    versions: Union[str, Iterable[str]],
     verbose: bool = True,
 ) -> Tuple[List[str], List[str], List[str]]:
     """
         Uninstall solc version(s) by deleting their artifacts from disk.
 
     Parameters
     ----------
```

#### encoding

```diff
@@ -1 +1 @@
-us-ascii
+utf-8
```

### Comparing `solcix-0.1.3/solcix/resolver.py` & `solcix-0.1.4/solcix/resolver.py`

 * *Files 2% similar despite different names*

```diff
@@ -4,14 +4,15 @@
 import os
 from solcix.errors import NoCompatibleVersionError
 from solcix.installer import (
     get_earliest_release,
     _get_version_dict,
     get_version_objects,
     get_available_versions,
+    get_installed_versions,
     install_solc,
 )
 from solcix.datatypes import PRAGMA_TYPE, Version
 
 
 def resolve_version_from_solidity(
     source: Union[str, Path],
@@ -213,28 +214,33 @@
     return None
 
 
 def install_solc_from_solidity(
     source: Union[str, Path],
     version_resolver: Callable[[PRAGMA_TYPE], str] = None,
     verbose: bool = True,
-):
+) -> str:
     """
     Install the solc version specified in the given source code.
 
     Parameters
     ----------
     - source : str | Path
         - The source code or file path to parse for the solc version.
     - version_resolver : Callable[[PRAGMA_TYPE], str], optional
         - A function that takes a PRAGMA_TYPE and returns a recommended version, by default None
         If not provided, `get_recommended_version` is used as default resolver.
     - verbose : bool, optional
         - Whether to print the installation progress, by default True
 
+    Returns
+    -------
+    str
+        The version extracted by version resolver solc version.
+
     Raises
     ------
     ValueError
         If the solc version cannot be resolved from the source code.
 
     Notes
     -----
@@ -254,8 +260,11 @@
     smaller than the given version, or the maximum version of the previous minor
     release if no such version exists.
     """
     version = resolve_version_from_solidity(source)
     if version_resolver is None:
         version_resolver = get_recommended_version
     recommended_version = version_resolver(version)
-    install_solc(recommended_version, verbose=verbose)
+    installed = get_installed_versions()
+    if recommended_version not in installed:
+        install_solc(recommended_version, verbose=verbose)
+    return recommended_version
```

### Comparing `solcix-0.1.3/solcix/utils.py` & `solcix-0.1.4/solcix/utils.py`

 * *Files identical despite different names*

### Comparing `solcix-0.1.3/PKG-INFO` & `solcix-0.1.4/PKG-INFO`

 * *Files 6% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: solcix
-Version: 0.1.3
+Version: 0.1.4
 Summary: A Python wrapper for the Solidity compiler. Switch between versions, compile, and manage artifacts.
 Author: alan890104
 Author-email: alan890104@gmail.com
 Requires-Python: >=3.8,<4.0
 Classifier: Programming Language :: Python :: 3
 Classifier: Programming Language :: Python :: 3.8
 Classifier: Programming Language :: Python :: 3.9
@@ -97,20 +97,20 @@
 
 ```bash
 solcix versions
 ```
 
 ### Listing installed Solidity compilers
 
-The `versions` command can be used to list all available versions of the Solidity compiler:
+The `ls` command can be used to list all available versions of the Solidity compiler:
 
 Example usage:
 
 ```bash
-solcix installed
+solcix ls
 ```
 
 If global / local version is set, it will be displayed as below:
 
 ```bash
 0.8.19
 0.5.2
@@ -159,15 +159,15 @@
 
 To uninstall all versions of Solidity compiler that have been installed using solcix, you can use the following command:
 
 ```bash
 solcix prune
 ```
 
-This will remove all versions of the Solidity compiler that have been installed by solcix.
+This will remove all versions of the Solidity compilers that have been installed by solcix, all cached files, and the solcix configuration file (local config takes precedence over global config).
 
 ### Verify Solidity compilers
 
 The `verify` command is used to verify the checksums of installed solc binaries and to reinstall any that are malformed.
 
 Example usage:
 
@@ -260,7 +260,15 @@
 ```bash
 pip3 install -U
 
 # Migrate to the new architecture and Reinstall all binaries
 solcix upgrade
 ```
 
+### Project Acknowledgements
+
+We would like to thank the original projects [solc-select](https://github.com/crytic/solc-select) and [py-solc-x](https://github.com/ApeWorX/py-solc-x) for providing excellent code base, upon which we have optimized and improved to make the project more robust and user-friendly.
+
+Our project is an improved and optimized version of solc-select and py-solc-x, with more features and excellent performance.
+
+If you enjoyed the original projects, we strongly recommend trying out our project to enjoy a better user experience and more efficient code execution.
+
```

