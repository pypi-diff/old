# Comparing `tmp/solcix-0.1.5.tar.gz` & `tmp/solcix-0.1.6.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "solcix-0.1.5.tar", max compression
+gzip compressed data, was "solcix-0.1.6.tar", max compression
```

## Comparing `solcix-0.1.5.tar` & `solcix-0.1.6.tar`

### file list

```diff
@@ -1,17 +1,17 @@
--rw-r--r--   0        0        0    34523 2023-04-07 00:17:24.679178 solcix-0.1.5/LICENSE
--rw-r--r--   0        0        0     7837 2023-04-07 00:17:24.679178 solcix-0.1.5/README.md
--rw-r--r--   0        0        0      893 2023-04-07 00:17:24.679178 solcix-0.1.5/pyproject.toml
--rw-r--r--   0        0        0     1109 2023-04-07 00:17:24.679178 solcix-0.1.5/solcix/__init__.py
--rw-r--r--   0        0        0     8884 2023-04-07 00:17:24.679178 solcix-0.1.5/solcix/__main__.py
--rw-r--r--   0        0        0      182 2023-04-07 00:17:24.679178 solcix-0.1.5/solcix/compile/__init__.py
--rw-r--r--   0        0        0    19156 2023-04-07 00:17:24.679178 solcix-0.1.5/solcix/compile/solc.py
--rw-r--r--   0        0        0      618 2023-04-07 00:17:24.679178 solcix-0.1.5/solcix/constant.py
--rw-r--r--   0        0        0      110 2023-04-07 00:17:24.679178 solcix-0.1.5/solcix/datatypes/__init__.py
--rw-r--r--   0        0        0     3949 2023-04-07 00:17:24.679178 solcix-0.1.5/solcix/datatypes/datatypes.py
--rw-r--r--   0        0        0     3407 2023-04-07 00:17:24.679178 solcix-0.1.5/solcix/errors.py
--rw-r--r--   0        0        0    21421 2023-04-07 00:17:24.679178 solcix-0.1.5/solcix/installer.py
--rw-r--r--   0        0        0      241 2023-04-07 00:17:24.679178 solcix-0.1.5/solcix/manage/__init__.py
--rw-r--r--   0        0        0     3773 2023-04-07 00:17:24.679178 solcix-0.1.5/solcix/manage/manage.py
--rw-r--r--   0        0        0    10656 2023-04-07 00:17:24.679178 solcix-0.1.5/solcix/resolver.py
--rw-r--r--   0        0        0      597 2023-04-07 00:17:24.679178 solcix-0.1.5/solcix/utils.py
--rw-r--r--   0        0        0     8998 1970-01-01 00:00:00.000000 solcix-0.1.5/PKG-INFO
+-rw-r--r--   0        0        0    34523 2023-04-07 01:15:56.610498 solcix-0.1.6/LICENSE
+-rw-r--r--   0        0        0     8212 2023-04-07 01:15:56.610498 solcix-0.1.6/README.md
+-rw-r--r--   0        0        0      871 2023-04-07 01:15:56.610498 solcix-0.1.6/pyproject.toml
+-rw-r--r--   0        0        0     1109 2023-04-07 01:15:56.610498 solcix-0.1.6/solcix/__init__.py
+-rw-r--r--   0        0        0     8987 2023-04-07 01:15:56.610498 solcix-0.1.6/solcix/__main__.py
+-rw-r--r--   0        0        0      182 2023-04-07 01:15:56.610498 solcix-0.1.6/solcix/compile/__init__.py
+-rw-r--r--   0        0        0    19156 2023-04-07 01:15:56.610498 solcix-0.1.6/solcix/compile/solc.py
+-rw-r--r--   0        0        0      618 2023-04-07 01:15:56.610498 solcix-0.1.6/solcix/constant.py
+-rw-r--r--   0        0        0      110 2023-04-07 01:15:56.610498 solcix-0.1.6/solcix/datatypes/__init__.py
+-rw-r--r--   0        0        0     3949 2023-04-07 01:15:56.610498 solcix-0.1.6/solcix/datatypes/datatypes.py
+-rw-r--r--   0        0        0     3407 2023-04-07 01:15:56.610498 solcix-0.1.6/solcix/errors.py
+-rw-r--r--   0        0        0    21648 2023-04-07 01:15:56.610498 solcix-0.1.6/solcix/installer.py
+-rw-r--r--   0        0        0      241 2023-04-07 01:15:56.610498 solcix-0.1.6/solcix/manage/__init__.py
+-rw-r--r--   0        0        0     3773 2023-04-07 01:15:56.610498 solcix-0.1.6/solcix/manage/manage.py
+-rw-r--r--   0        0        0    10656 2023-04-07 01:15:56.610498 solcix-0.1.6/solcix/resolver.py
+-rw-r--r--   0        0        0      597 2023-04-07 01:15:56.610498 solcix-0.1.6/solcix/utils.py
+-rw-r--r--   0        0        0     9373 1970-01-01 00:00:00.000000 solcix-0.1.6/PKG-INFO
```

### Comparing `solcix-0.1.5/LICENSE` & `solcix-0.1.6/LICENSE`

 * *Files identical despite different names*

### Comparing `solcix-0.1.5/README.md` & `solcix-0.1.6/README.md`

 * *Files 2% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 # Solcix
 
-[![Version](https://img.shields.io/pypi/v/solcix?color=brightgreen)](https://pypi.org/project/solcix?style=flat) [![Release](https://img.shields.io/github/v/release/Solratic/solcix?display_name=tag&include_prereleases?color=brightgreen)](https://github.com/Solratic/solcix)  [![Code Style](https://img.shields.io/badge/code%20style-black-black)](https://github.com/psf/black) [![Python Versions](https://img.shields.io/pypi/pyversions/solcix?style=flat)](https://pypi.org/project/solcix/) [![Activity](https://img.shields.io/github/commit-activity/w/Solratic/solcix?color=orange)](https://github.com/Solratic/solcix)
+[![Version](https://img.shields.io/pypi/v/solcix?color=green)](https://pypi.org/project/solcix?style=flat) [![Release](https://img.shields.io/github/v/release/Solratic/solcix?color=green)](https://github.com/Solratic/solcix) [![Python Versions](https://img.shields.io/pypi/pyversions/solcix?style=flat&color=306998)](https://pypi.org/project/solcix/) [![Code Style](https://img.shields.io/badge/code%20style-black-black)](https://github.com/psf/black) [![Activity](https://img.shields.io/github/commit-activity/w/Solratic/solcix?color=yellow)](https://github.com/Solratic/solcix) [![License](https://img.shields.io/github/license/Solratic/solcix?style=flat&color=orange)](https://github.com/Solratic/solcix/blob/main/LICENSE)
 
 Solcix is a Solidity version manager written in Python that allows for seamless switching between versions, easy compilation, and simple management of artifacts.
 
 ## Installation
 
 To install Solcix, you can use pip, the Python package manager:
 
@@ -40,14 +40,22 @@
 
 Uses the [pipenv](https://pipenv.pypa.io/en/latest/) package manager to install solcix in a project-specific virtual environment. pipenv also manages dependencies and isolates your project from the global environment, and use our wrapped solc api in your code. You can run the following command in your terminal to install:
 
 ```bash
 pipenv install solcix
 ```
 
+### With pip for main branch
+
+You can also install solcix from github main branch:
+
+```bash
+pip install git+https://github.com/Solratic/solcix.git@main
+```
+
 ## Enable Auto-Completion
 
 Enable auto-completion for `solcix` by running the following command:
 
 ### With Bash
 
 ```bash
@@ -85,15 +93,15 @@
 ### Installing Solidity compilers
 
 The `install` command can be used to install one or more versions of the Solidity compiler:
 
 Example usage:
 
 ```bash
-solcix install 0.8.4 0.7.6
+solcix install 0.8.4 0.7.6 latest
 ```
 
 ### Listing installed Solidity compilers
 
 The `installed` command can be used to list all available versions of the Solidity compiler:
 
 Example usage:
@@ -130,14 +138,19 @@
 ```
 
 ```bash
 # Setting local version to 0.8.16, it will create a .solcix file in the current directory
 solcix use local 0.8.16
 ```
 
+```bash
+# You can also use the alias `latest` to use the latest version
+solcix use global latest
+```
+
 Simply run the command will see the changes:
 
 ```bash
 solc --version
 ```
 
 ### Show current Solidity compiler version
```

### Comparing `solcix-0.1.5/pyproject.toml` & `solcix-0.1.6/pyproject.toml`

 * *Files 16% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 [tool.poetry]
 name = "solcix"
-version = "0.1.5"
+version = "0.1.6"
 description = "A Python wrapper for the Solidity compiler. Switch between versions, compile, and manage artifacts."
 authors = ["alan890104 <alan890104@gmail.com>"]
 readme = "README.md"
 
 [tool.poetry.dependencies]
 python = "^3.8"
 cfgv = "3.3.1"
@@ -25,15 +25,14 @@
 virtualenv = "20.21.0"
 colorama = "^0.4.6"
 pyfiglet = "^0.8.post1"
 
 [tool.poetry.group.dev.dependencies]
 black = "23.3.0"
 pre-commit = "^3.2.2"
-pytest-cov = "^4.0.0"
 
 [tool.poetry.scripts]
 solcix = "solcix.__main__:cli"
 solc = "solcix.__main__:solc"
 
 [build-system]
 requires = ["poetry-core"]
```

### Comparing `solcix-0.1.5/solcix/__init__.py` & `solcix-0.1.6/solcix/__init__.py`

 * *Files identical despite different names*

### Comparing `solcix-0.1.5/solcix/__main__.py` & `solcix-0.1.6/solcix/__main__.py`

 * *Files 1% similar despite different names*

```diff
@@ -58,15 +58,16 @@
         print(Fore.YELLOW + "No solc binary is installed. Please use `solcix install` or `solc use` to install solc." + Style.RESET_ALL)
         return
     try:
         current, _ = solcix.current_version()
         for version in installed:
             if current == version:
                 print(Fore.GREEN + f"{version} <- current" + Style.RESET_ALL)
-            print(version)
+            else:
+                print(version)
     except NotInstalledError as e:
         print(Fore.YELLOW + f"{e}" + Style.RESET_ALL)
         for version in installed:
             print(version)
 
 @cli.command(help="Show current solc version.")
 def current():
@@ -77,14 +78,16 @@
         print(Fore.YELLOW + f"{e}" + Style.RESET_ALL)
 
 
 @cli.command(help="Switch between solc versions. If the version is not installed, it will be installed.")
 @click.argument("scope", nargs=1, required=True, type=click.Choice(["global", "local"]))
 @click.argument("version", nargs=1, required=True, type=click.STRING)
 def use(scope: str, version: str):
+    if version == "latest":
+        _, version = solcix.get_available_versions()
     if scope == "global":
         solcix.manage.switch_global_version(version, True)
     elif scope == "local":
         solcix.manage.switch_local_version(version, True)
 
 
 @cli.command(help="Uninstall solc binaries.")
```

### Comparing `solcix-0.1.5/solcix/compile/solc.py` & `solcix-0.1.6/solcix/compile/solc.py`

 * *Files identical despite different names*

### Comparing `solcix-0.1.5/solcix/constant.py` & `solcix-0.1.6/solcix/constant.py`

 * *Files identical despite different names*

### Comparing `solcix-0.1.5/solcix/datatypes/datatypes.py` & `solcix-0.1.6/solcix/datatypes/datatypes.py`

 * *Files identical despite different names*

### Comparing `solcix-0.1.5/solcix/errors.py` & `solcix-0.1.6/solcix/errors.py`

 * *Files identical despite different names*

### Comparing `solcix-0.1.5/solcix/installer.py` & `solcix-0.1.6/solcix/installer.py`

 * *Files 2% similar despite different names*

```diff
@@ -3,38 +3,40 @@
 import os
 import shutil
 import sys
 from collections import defaultdict
 from glob import glob
 from os import access, makedirs
 from pathlib import Path
-from typing import Iterable, List, Tuple, Union, Optional, Set, Dict, Any
+from typing import Any, Dict, Iterable, List, Optional, Set, Tuple, Union
 from urllib.request import urlopen, urlretrieve
 from zipfile import ZipFile
 
 from Crypto.Hash import keccak
 from joblib import Memory
 
 from solcix.constant import (
     ARTIFACT_DIR,
-    SOLCIX_DIR,
     CRYTIC_SOLC_ARTIFACTS,
     CRYTIC_SOLC_JSON,
+    SOLCIX_DIR,
     EarliestRelease,
     Platform,
 )
 from solcix.datatypes import ProgressBar, Version
 from solcix.errors import (
     ChecksumMismatchError,
     ChecksumMissingError,
     NoSolcVersionInstalledError,
-    UnsupportedPlatformError,
     NotInstalledError,
+    UnsupportedPlatformError,
 )
 
+from .utils import is_valid_version
+
 cachedir = ARTIFACT_DIR.joinpath(".solcix", "cache")
 os.makedirs(cachedir, exist_ok=True)
 memory = Memory(cachedir, verbose=0)
 
 
 def clear_cache() -> None:
     """
@@ -349,24 +351,27 @@
     Raises
     ------
         ValueError
             If the specified version or platform is not installed, or if the checksums do not match.
     """
     if isinstance(version, str):
         version = [version]
+    _, latest = get_available_versions()
+    version = [latest if v == "latest" else v for v in version]
     fixs = []
     for v in version:
         try:
-            v = Version(v)
-            _verify_checksum(v)
-        except AssertionError:
-            if verbose:
-                print(
-                    f"Since solc-{v} is not a valid version, checksum verification is skipped."
-                )
+            if is_valid_version(v):
+                _verify_checksum(v)
+                print(f"Checksum verification passed for solc-{v}.")
+            else:
+                if verbose:
+                    print(
+                        f"Since solc-{v} is not a valid version, checksum verification is skipped."
+                    )
         except ChecksumMismatchError:
             if reinstall:
                 fixs.append(v)
         except FileNotFoundError:
             if verbose:
                 print(
                     f"Since solc-{v} is not installed, checksum verification is skipped."
```

### Comparing `solcix-0.1.5/solcix/manage/manage.py` & `solcix-0.1.6/solcix/manage/manage.py`

 * *Files identical despite different names*

### Comparing `solcix-0.1.5/solcix/resolver.py` & `solcix-0.1.6/solcix/resolver.py`

 * *Files identical despite different names*

### Comparing `solcix-0.1.5/solcix/utils.py` & `solcix-0.1.6/solcix/utils.py`

 * *Files identical despite different names*

### Comparing `solcix-0.1.5/PKG-INFO` & `solcix-0.1.6/PKG-INFO`

 * *Files 7% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: solcix
-Version: 0.1.5
+Version: 0.1.6
 Summary: A Python wrapper for the Solidity compiler. Switch between versions, compile, and manage artifacts.
 Author: alan890104
 Author-email: alan890104@gmail.com
 Requires-Python: >=3.8,<4.0
 Classifier: Programming Language :: Python :: 3
 Classifier: Programming Language :: Python :: 3.8
 Classifier: Programming Language :: Python :: 3.9
@@ -28,15 +28,15 @@
 Requires-Dist: tomli (==2.0.1)
 Requires-Dist: tqdm (==4.65.0)
 Requires-Dist: virtualenv (==20.21.0)
 Description-Content-Type: text/markdown
 
 # Solcix
 
-[![Version](https://img.shields.io/pypi/v/solcix?color=brightgreen)](https://pypi.org/project/solcix?style=flat) [![Release](https://img.shields.io/github/v/release/Solratic/solcix?display_name=tag&include_prereleases?color=brightgreen)](https://github.com/Solratic/solcix)  [![Code Style](https://img.shields.io/badge/code%20style-black-black)](https://github.com/psf/black) [![Python Versions](https://img.shields.io/pypi/pyversions/solcix?style=flat)](https://pypi.org/project/solcix/) [![Activity](https://img.shields.io/github/commit-activity/w/Solratic/solcix?color=orange)](https://github.com/Solratic/solcix)
+[![Version](https://img.shields.io/pypi/v/solcix?color=green)](https://pypi.org/project/solcix?style=flat) [![Release](https://img.shields.io/github/v/release/Solratic/solcix?color=green)](https://github.com/Solratic/solcix) [![Python Versions](https://img.shields.io/pypi/pyversions/solcix?style=flat&color=306998)](https://pypi.org/project/solcix/) [![Code Style](https://img.shields.io/badge/code%20style-black-black)](https://github.com/psf/black) [![Activity](https://img.shields.io/github/commit-activity/w/Solratic/solcix?color=yellow)](https://github.com/Solratic/solcix) [![License](https://img.shields.io/github/license/Solratic/solcix?style=flat&color=orange)](https://github.com/Solratic/solcix/blob/main/LICENSE)
 
 Solcix is a Solidity version manager written in Python that allows for seamless switching between versions, easy compilation, and simple management of artifacts.
 
 ## Installation
 
 To install Solcix, you can use pip, the Python package manager:
 
@@ -72,14 +72,22 @@
 
 Uses the [pipenv](https://pipenv.pypa.io/en/latest/) package manager to install solcix in a project-specific virtual environment. pipenv also manages dependencies and isolates your project from the global environment, and use our wrapped solc api in your code. You can run the following command in your terminal to install:
 
 ```bash
 pipenv install solcix
 ```
 
+### With pip for main branch
+
+You can also install solcix from github main branch:
+
+```bash
+pip install git+https://github.com/Solratic/solcix.git@main
+```
+
 ## Enable Auto-Completion
 
 Enable auto-completion for `solcix` by running the following command:
 
 ### With Bash
 
 ```bash
@@ -117,15 +125,15 @@
 ### Installing Solidity compilers
 
 The `install` command can be used to install one or more versions of the Solidity compiler:
 
 Example usage:
 
 ```bash
-solcix install 0.8.4 0.7.6
+solcix install 0.8.4 0.7.6 latest
 ```
 
 ### Listing installed Solidity compilers
 
 The `installed` command can be used to list all available versions of the Solidity compiler:
 
 Example usage:
@@ -162,14 +170,19 @@
 ```
 
 ```bash
 # Setting local version to 0.8.16, it will create a .solcix file in the current directory
 solcix use local 0.8.16
 ```
 
+```bash
+# You can also use the alias `latest` to use the latest version
+solcix use global latest
+```
+
 Simply run the command will see the changes:
 
 ```bash
 solc --version
 ```
 
 ### Show current Solidity compiler version
```

