processes the pypi
[changelog](https://warehouse.pypa.io/api-reference/xml-rpc.html) and if a new release for
a package is published, attempts to create diffs between old and new version
using diffoscope, output formats:

 * html
 * text
 * markdown

Projects with artifacts > 10 MB are ignored and some "special cases" are not
handled yet: no guarantee that all packages are tracked.

Changes are pushed to this repository until it reaches some magic limits.

Requirements: podman

```
usage: fetch.py [-h] [-w WORKER] [-p PACKAGES] [-t TMPDIR]
                [-o OUTPUT] [-l SIZELIMIT] [-s]

pypi-diff bot

optional arguments:
  -h, --help            show this help message and exit
  -w WORKER, --worker WORKER
                        Amount of workers to use
  -p PACKAGES, --packages PACKAGES
                        Process only specific packages, seperated
                        by ','
  -t TMPDIR, --tmpdir TMPDIR
                        Default directory for storing temporary
                        artifacts.
  -o OUTPUT, --output OUTPUT
                        Default output directory.
  -l SIZELIMIT, --sizelimit SIZELIMIT
                        Skip if download packages exceed limit
  -s, --silent          Dont log to stderr
```

