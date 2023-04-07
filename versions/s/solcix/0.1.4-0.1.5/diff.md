# Comparing `tmp/solcix-0.1.4.tar.gz` & `tmp/solcix-0.1.5.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "solcix-0.1.4.tar", max compression
+gzip compressed data, was "solcix-0.1.5.tar", max compression
```

## Comparing `solcix-0.1.4.tar` & `solcix-0.1.5.tar`

### file list

```diff
@@ -1,16 +1,17 @@
--rw-r--r--   0        0        0     6356 2023-04-06 18:40:16.591860 solcix-0.1.4/README.md
--rw-r--r--   0        0        0      935 2023-04-06 18:40:16.591860 solcix-0.1.4/pyproject.toml
--rw-r--r--   0        0        0     1109 2023-04-06 18:40:16.591860 solcix-0.1.4/solcix/__init__.py
--rw-r--r--   0        0        0     7884 2023-04-06 18:40:16.591860 solcix-0.1.4/solcix/__main__.py
--rw-r--r--   0        0        0      182 2023-04-06 18:40:16.591860 solcix-0.1.4/solcix/compile/__init__.py
--rw-r--r--   0        0        0    19181 2023-04-06 18:40:16.591860 solcix-0.1.4/solcix/compile/solc.py
--rw-r--r--   0        0        0      618 2023-04-06 18:40:16.591860 solcix-0.1.4/solcix/constant.py
--rw-r--r--   0        0        0      110 2023-04-06 18:40:16.591860 solcix-0.1.4/solcix/datatypes/__init__.py
--rw-r--r--   0        0        0     3949 2023-04-06 18:40:16.591860 solcix-0.1.4/solcix/datatypes/datatypes.py
--rw-r--r--   0        0        0     3407 2023-04-06 18:40:16.591860 solcix-0.1.4/solcix/errors.py
--rw-r--r--   0        0        0    21421 2023-04-06 18:40:16.591860 solcix-0.1.4/solcix/installer.py
--rw-r--r--   0        0        0      241 2023-04-06 18:40:16.591860 solcix-0.1.4/solcix/manage/__init__.py
--rw-r--r--   0        0        0     3773 2023-04-06 18:40:16.591860 solcix-0.1.4/solcix/manage/manage.py
--rw-r--r--   0        0        0    10656 2023-04-06 18:40:16.591860 solcix-0.1.4/solcix/resolver.py
--rw-r--r--   0        0        0      597 2023-04-06 18:40:16.591860 solcix-0.1.4/solcix/utils.py
--rw-r--r--   0        0        0     7562 1970-01-01 00:00:00.000000 solcix-0.1.4/PKG-INFO
+-rw-r--r--   0        0        0    34523 2023-04-07 00:17:24.679178 solcix-0.1.5/LICENSE
+-rw-r--r--   0        0        0     7837 2023-04-07 00:17:24.679178 solcix-0.1.5/README.md
+-rw-r--r--   0        0        0      893 2023-04-07 00:17:24.679178 solcix-0.1.5/pyproject.toml
+-rw-r--r--   0        0        0     1109 2023-04-07 00:17:24.679178 solcix-0.1.5/solcix/__init__.py
+-rw-r--r--   0        0        0     8884 2023-04-07 00:17:24.679178 solcix-0.1.5/solcix/__main__.py
+-rw-r--r--   0        0        0      182 2023-04-07 00:17:24.679178 solcix-0.1.5/solcix/compile/__init__.py
+-rw-r--r--   0        0        0    19156 2023-04-07 00:17:24.679178 solcix-0.1.5/solcix/compile/solc.py
+-rw-r--r--   0        0        0      618 2023-04-07 00:17:24.679178 solcix-0.1.5/solcix/constant.py
+-rw-r--r--   0        0        0      110 2023-04-07 00:17:24.679178 solcix-0.1.5/solcix/datatypes/__init__.py
+-rw-r--r--   0        0        0     3949 2023-04-07 00:17:24.679178 solcix-0.1.5/solcix/datatypes/datatypes.py
+-rw-r--r--   0        0        0     3407 2023-04-07 00:17:24.679178 solcix-0.1.5/solcix/errors.py
+-rw-r--r--   0        0        0    21421 2023-04-07 00:17:24.679178 solcix-0.1.5/solcix/installer.py
+-rw-r--r--   0        0        0      241 2023-04-07 00:17:24.679178 solcix-0.1.5/solcix/manage/__init__.py
+-rw-r--r--   0        0        0     3773 2023-04-07 00:17:24.679178 solcix-0.1.5/solcix/manage/manage.py
+-rw-r--r--   0        0        0    10656 2023-04-07 00:17:24.679178 solcix-0.1.5/solcix/resolver.py
+-rw-r--r--   0        0        0      597 2023-04-07 00:17:24.679178 solcix-0.1.5/solcix/utils.py
+-rw-r--r--   0        0        0     8998 1970-01-01 00:00:00.000000 solcix-0.1.5/PKG-INFO
```

### Comparing `solcix-0.1.4/README.md` & `solcix-0.1.5/README.md`

 * *Files 13% similar despite different names*

```diff
@@ -1,10 +1,12 @@
 # Solcix
 
-Solcix is a Solidity compiler manager for Python. You can switch between versions, compile, and manage artifacts easily.
+[![Version](https://img.shields.io/pypi/v/solcix?color=brightgreen)](https://pypi.org/project/solcix?style=flat) [![Release](https://img.shields.io/github/v/release/Solratic/solcix?display_name=tag&include_prereleases?color=brightgreen)](https://github.com/Solratic/solcix)  [![Code Style](https://img.shields.io/badge/code%20style-black-black)](https://github.com/psf/black) [![Python Versions](https://img.shields.io/pypi/pyversions/solcix?style=flat)](https://pypi.org/project/solcix/) [![Activity](https://img.shields.io/github/commit-activity/w/Solratic/solcix?color=orange)](https://github.com/Solratic/solcix)
+
+Solcix is a Solidity version manager written in Python that allows for seamless switching between versions, easy compilation, and simple management of artifacts.
 
 ## Installation
 
 To install Solcix, you can use pip, the Python package manager:
 
 ### With pip For Windows
 
@@ -38,46 +40,70 @@
 
 Uses the [pipenv](https://pipenv.pypa.io/en/latest/) package manager to install solcix in a project-specific virtual environment. pipenv also manages dependencies and isolates your project from the global environment, and use our wrapped solc api in your code. You can run the following command in your terminal to install:
 
 ```bash
 pipenv install solcix
 ```
 
+## Enable Auto-Completion
+
+Enable auto-completion for `solcix` by running the following command:
+
+### With Bash
+
+```bash
+_SOLCIX_COMPLETE=bash_source solcix > ~/.solcix-complete.bash
+source ~/.solcix-complete.bash
+```
+
+### With Zsh
+
+```zsh
+_SOLCIX_COMPLETE=zsh_source solcix > ~/.solcix-complete.zsh
+source ~/.solcix-complete.zsh
+```
+
+### With Fish
+
+```fish
+_SOLCIX_COMPLETE=fish_source solcix > ~/.config/fish/completions/solcix.fish
+```
+
 ## Usage - CLI
 
 Solcix can be used as a library or as a command line tool. Here are the available commands:
 
-### Installing Solidity compilers
+### Listing available Solidity compilers
 
-The `install` command can be used to install one or more versions of the Solidity compiler:
+The `ls` command can be used to list all available versions of the Solidity compiler:
 
 Example usage:
 
 ```bash
-solcix install 0.8.4 0.7.6
+solcix ls
 ```
 
-### Listing available Solidity compilers
+### Installing Solidity compilers
 
-The `versions` command can be used to list all available versions of the Solidity compiler:
+The `install` command can be used to install one or more versions of the Solidity compiler:
 
 Example usage:
 
 ```bash
-solcix versions
+solcix install 0.8.4 0.7.6
 ```
 
 ### Listing installed Solidity compilers
 
-The `ls` command can be used to list all available versions of the Solidity compiler:
+The `installed` command can be used to list all available versions of the Solidity compiler:
 
 Example usage:
 
 ```bash
-solcix ls
+solcix installed
 ```
 
 If global / local version is set, it will be displayed as below:
 
 ```bash
 0.8.19
 0.5.2
@@ -110,14 +136,24 @@
 
 Simply run the command will see the changes:
 
 ```bash
 solc --version
 ```
 
+### Show current Solidity compiler version
+
+The `current` command can be used to show the current version of the Solidity compiler (local version takes precedence over global version):
+
+Example usage:
+
+```bash
+solcix current
+```
+
 ### Uninstalling Solidity compilers
 
 The `uninstall` command can be used to uninstall one or more versions of the Solidity compiler:
 
 ```bash
 solcix uninstall 0.8.4 0.7.6
 ```
@@ -171,15 +207,21 @@
 ```
 
 Additional optional arguments can be passed to the command using the kwargs argument, it will be taken by the [solc command](https://docs.soliditylang.org/en/v0.8.19/using-the-compiler.html#basic-usage).
 
 Example usage:
 
 ```bash
-solcix compile <file.sol> --optimize
+solcix compile <file.sol> --optimize=True --optimize-runs=200 --overwrite=True
+```
+
+Or you can redirect the output to a single json file:
+
+```bash
+solcix compile <file.sol> > output.json
 ```
 
 ### Resolve compatible versions from solidity file
 
 The `resolve` command is used to determine the recommended solc version for a Solidity file based on its pragma statement. It can also be used to list all versions that are compatible with the Solidity file.
 
 Example usage:
```

### Comparing `solcix-0.1.4/pyproject.toml` & `solcix-0.1.5/pyproject.toml`

 * *Files 9% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 [tool.poetry]
 name = "solcix"
-version = "0.1.4"
+version = "0.1.5"
 description = "A Python wrapper for the Solidity compiler. Switch between versions, compile, and manage artifacts."
 authors = ["alan890104 <alan890104@gmail.com>"]
 readme = "README.md"
 
 [tool.poetry.dependencies]
 python = "^3.8"
 cfgv = "3.3.1"
@@ -19,23 +19,21 @@
 pathspec = "0.11.1"
 platformdirs = "3.2.0"
 pycryptodome = "3.17"
 pyyaml = "6.0"
 tomli = "2.0.1"
 tqdm = "4.65.0"
 virtualenv = "20.21.0"
-pytest-mock = "^3.10.0"
 colorama = "^0.4.6"
 pyfiglet = "^0.8.post1"
 
 [tool.poetry.group.dev.dependencies]
 black = "23.3.0"
 pre-commit = "^3.2.2"
 pytest-cov = "^4.0.0"
-pytest = "^7.2.2"
 
 [tool.poetry.scripts]
 solcix = "solcix.__main__:cli"
 solc = "solcix.__main__:solc"
 
 [build-system]
 requires = ["poetry-core"]
```

### Comparing `solcix-0.1.4/solcix/__init__.py` & `solcix-0.1.5/solcix/__init__.py`

 * *Files identical despite different names*

### Comparing `solcix-0.1.4/solcix/__main__.py` & `solcix-0.1.5/solcix/__main__.py`

 * *Files 2% similar despite different names*

```diff
@@ -1,7 +1,9 @@
+import os
+import ast
 import sys
 import json
 import textwrap
 from typing import List, Union
 import pyfiglet
 import subprocess
 
@@ -48,14 +50,17 @@
     print(Fore.GREEN + f"latest: {latest}" + Style.RESET_ALL)
 
 
 @cli.command(help="List all installed solc versions.")
 def installed():
     installed = solcix.get_installed_versions()
     installed = sorted(installed, key=Version)
+    if len(installed) == 0:
+        print(Fore.YELLOW + "No solc binary is installed. Please use `solcix install` or `solc use` to install solc." + Style.RESET_ALL)
+        return
     try:
         current, _ = solcix.current_version()
         for version in installed:
             if current == version:
                 print(Fore.GREEN + f"{version} <- current" + Style.RESET_ALL)
             print(version)
     except NotInstalledError as e:
@@ -90,15 +95,15 @@
     print(Fore.YELLOW + f"skipped: {', '.join(skipped)}" + Style.RESET_ALL)
     print(Fore.RED + f"error  : {', '.join(error)}" + Style.RESET_ALL)
 
 @cli.command(help="Uninstall all solc binaries.")
 def prune():
     opt = click.confirm(default=False, text="Are you sure to uninstall all solc binaries, caches, and config files?")
     if opt is False:
-        print(f"{Fore.YELLOW}You have canceled the operation. Indeed, a wise choice!{Style.RESET_ALL}")
+        print(f"👀{Fore.YELLOW} You have canceled the operation. Indeed, a wise choice!{Style.RESET_ALL} 👀")
         return
     # Delete all cached versions
     solcix.clear_cache()
     # Delete all config files
     solcix.manage.clear_config()
     # Delete all installed versions
     versions = solcix.get_installed_versions()
@@ -119,24 +124,38 @@
 
 
 @cli.command(context_settings=dict(ignore_unknown_options=True, allow_extra_args=True), help="Compile Solidity files and print the result, if the output is a TTY, the result will be formatted. Otherwise the result will be printed as a JSON string. If you want to show the help message of solc, please use `solc --help`.")
 @click.argument("file", nargs=1, required=True, type=click.Path(exists=True))
 @click.option("-o", "--output", default=None, type=click.Path(), help="Output directory, will be create if not exists.")
 @click.pass_context
 def compile(ctx: click.Context, file: str, output: str):
-    params = dict([item.strip('--').split('=') for item in ctx.args])
-    params["source_files"] = file
+    # Parse arguments
+    params = dict()
+    for segment in ctx.args:
+        if segment.startswith("--") and segment.find("=") != 1:
+            key, value = segment.strip("--").split("=")
+            params[key.replace("-","_")] = ast.literal_eval(value)
+
+    # check output directory
     if output is not None:
         params["output_dir"] = output
+        if os.path.exists(output) and "overwrite" not in params:
+            click.confirm(f"Output path `{output}` already exists, do you want to overwrite it?", default=False, abort=True)
+            params["overwrite"] = True
+
+    # check solc version is installed
     try:
         version = solcix.install_solc_from_solidity(source=file)
         params["solc_version"] = version
+        params["source_files"] = file
     except Exception as e:
         print(e)
         sys.exit(1)
+
+    # compile
     compile_result = solcix.compile.compile_files(**params)
     if output is not None:
         print(f"Compilation result is saved in the output directory {output}.")
     else:
         if sys.stdout.isatty():
             width = 70
             wrapper = textwrap.TextWrapper(width=width, initial_indent="    ", subsequent_indent="    ")
@@ -149,30 +168,30 @@
                         print(padded_str)
             print(Fore.CYAN + "* Output to directory by", Fore.YELLOW + "`solcix compile <FILE> -o <output dir>`" + Style.RESET_ALL)
             print(Fore.CYAN + "* Print to a single json file by", Fore.YELLOW + "`solcix compile <FILE> <output file>.json`" + Style.RESET_ALL, "to view whole result.")
         else:
             print(json.dumps(compile_result, indent=4, sort_keys=True))
 
 
-@cli.command()
+@cli.command(help="Resolve the version of solc from the pragma in the Solidity file, and print the recommended version. If you want to see all compatible versions, use `solcix resolve --no-recommand`.")
 @click.argument("file", nargs=1, required=True, type=click.Path(exists=True, dir_okay=False, readable=True))
 @click.option("--recommand/--no-recommand", default=True, is_flag=True)
 def resolve(file: str, recommand: bool):
     pragma = solcix.resolve_version_from_solidity(file)
     if recommand:
         version = solcix.get_recommended_version(pragma)
-        print(f"The recommended version is {version}, use `solcix resolve --no-recommand` to see all compatible versions.")
+        print(f"The recommended version is {Fore.YELLOW}{version}.{Style.RESET_ALL}\nUse {Fore.YELLOW}`solcix resolve --no-recommand`{Style.RESET_ALL} to see all compatible versions.")
     else:
         versions = solcix.get_compatible_versions(pragma)
         print("These versions are compatible with the pragma.")
         for version in versions:
             print(version)
 
 
-@cli.command()
+@cli.command(help="Reinstall all solc binaries.")
 def upgrade():
     solcix.manage.upgrade_architecture()
 
 
 def solc() -> None:
     try:
         version, _  = solcix.current_version()
```

#### encoding

```diff
@@ -1 +1 @@
-us-ascii
+utf-8
```

### Comparing `solcix-0.1.4/solcix/compile/solc.py` & `solcix-0.1.5/solcix/compile/solc.py`

 * *Files 1% similar despite different names*

```diff
@@ -413,15 +413,15 @@
 
     Returns
     -------
     - Dict[str, Any]
         - A dictionary of the compiled contracts and their details.
 
     """
-    output = json.loads(stdout)
+    output: dict = json.loads(stdout)
 
     contracts = output.get("contracts", {})
     sources = output.get("sources", {})
 
     for path_str, data in contracts.items():
         if "abi" in data and isinstance(data["abi"], str):
             data["abi"] = json.loads(data["abi"])
@@ -492,15 +492,14 @@
             raise FileExistsError(
                 f"Target output file {target_path} already exists - use overwrite=True to overwrite"
             )
 
     stdoutdata, stderrdata, command, proc = solc_execute(
         solc_path=solc_path,
         combined_json=combined_json,
-        output_dir=output_dir,
         overwrite=overwrite,
         **kwargs,
     )
 
     if output_dir:
         output_path = Path(output_dir).joinpath("combined.json")
         if stdoutdata:
```

### Comparing `solcix-0.1.4/solcix/constant.py` & `solcix-0.1.5/solcix/constant.py`

 * *Files identical despite different names*

### Comparing `solcix-0.1.4/solcix/datatypes/datatypes.py` & `solcix-0.1.5/solcix/datatypes/datatypes.py`

 * *Files identical despite different names*

### Comparing `solcix-0.1.4/solcix/errors.py` & `solcix-0.1.5/solcix/errors.py`

 * *Files identical despite different names*

### Comparing `solcix-0.1.4/solcix/installer.py` & `solcix-0.1.5/solcix/installer.py`

 * *Files identical despite different names*

### Comparing `solcix-0.1.4/solcix/manage/manage.py` & `solcix-0.1.5/solcix/manage/manage.py`

 * *Files identical despite different names*

### Comparing `solcix-0.1.4/solcix/resolver.py` & `solcix-0.1.5/solcix/resolver.py`

 * *Files identical despite different names*

### Comparing `solcix-0.1.4/solcix/utils.py` & `solcix-0.1.5/solcix/utils.py`

 * *Files identical despite different names*

### Comparing `solcix-0.1.4/PKG-INFO` & `solcix-0.1.5/PKG-INFO`

 * *Files 18% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: solcix
-Version: 0.1.4
+Version: 0.1.5
 Summary: A Python wrapper for the Solidity compiler. Switch between versions, compile, and manage artifacts.
 Author: alan890104
 Author-email: alan890104@gmail.com
 Requires-Python: >=3.8,<4.0
 Classifier: Programming Language :: Python :: 3
 Classifier: Programming Language :: Python :: 3.8
 Classifier: Programming Language :: Python :: 3.9
@@ -20,24 +20,25 @@
 Requires-Dist: mypy-extensions (==1.0.0)
 Requires-Dist: nodeenv (==1.7.0)
 Requires-Dist: packaging (==23.0)
 Requires-Dist: pathspec (==0.11.1)
 Requires-Dist: platformdirs (==3.2.0)
 Requires-Dist: pycryptodome (==3.17)
 Requires-Dist: pyfiglet (>=0.8.post1,<0.9)
-Requires-Dist: pytest-mock (>=3.10.0,<4.0.0)
 Requires-Dist: pyyaml (==6.0)
 Requires-Dist: tomli (==2.0.1)
 Requires-Dist: tqdm (==4.65.0)
 Requires-Dist: virtualenv (==20.21.0)
 Description-Content-Type: text/markdown
 
 # Solcix
 
-Solcix is a Solidity compiler manager for Python. You can switch between versions, compile, and manage artifacts easily.
+[![Version](https://img.shields.io/pypi/v/solcix?color=brightgreen)](https://pypi.org/project/solcix?style=flat) [![Release](https://img.shields.io/github/v/release/Solratic/solcix?display_name=tag&include_prereleases?color=brightgreen)](https://github.com/Solratic/solcix)  [![Code Style](https://img.shields.io/badge/code%20style-black-black)](https://github.com/psf/black) [![Python Versions](https://img.shields.io/pypi/pyversions/solcix?style=flat)](https://pypi.org/project/solcix/) [![Activity](https://img.shields.io/github/commit-activity/w/Solratic/solcix?color=orange)](https://github.com/Solratic/solcix)
+
+Solcix is a Solidity version manager written in Python that allows for seamless switching between versions, easy compilation, and simple management of artifacts.
 
 ## Installation
 
 To install Solcix, you can use pip, the Python package manager:
 
 ### With pip For Windows
 
@@ -71,46 +72,70 @@
 
 Uses the [pipenv](https://pipenv.pypa.io/en/latest/) package manager to install solcix in a project-specific virtual environment. pipenv also manages dependencies and isolates your project from the global environment, and use our wrapped solc api in your code. You can run the following command in your terminal to install:
 
 ```bash
 pipenv install solcix
 ```
 
+## Enable Auto-Completion
+
+Enable auto-completion for `solcix` by running the following command:
+
+### With Bash
+
+```bash
+_SOLCIX_COMPLETE=bash_source solcix > ~/.solcix-complete.bash
+source ~/.solcix-complete.bash
+```
+
+### With Zsh
+
+```zsh
+_SOLCIX_COMPLETE=zsh_source solcix > ~/.solcix-complete.zsh
+source ~/.solcix-complete.zsh
+```
+
+### With Fish
+
+```fish
+_SOLCIX_COMPLETE=fish_source solcix > ~/.config/fish/completions/solcix.fish
+```
+
 ## Usage - CLI
 
 Solcix can be used as a library or as a command line tool. Here are the available commands:
 
-### Installing Solidity compilers
+### Listing available Solidity compilers
 
-The `install` command can be used to install one or more versions of the Solidity compiler:
+The `ls` command can be used to list all available versions of the Solidity compiler:
 
 Example usage:
 
 ```bash
-solcix install 0.8.4 0.7.6
+solcix ls
 ```
 
-### Listing available Solidity compilers
+### Installing Solidity compilers
 
-The `versions` command can be used to list all available versions of the Solidity compiler:
+The `install` command can be used to install one or more versions of the Solidity compiler:
 
 Example usage:
 
 ```bash
-solcix versions
+solcix install 0.8.4 0.7.6
 ```
 
 ### Listing installed Solidity compilers
 
-The `ls` command can be used to list all available versions of the Solidity compiler:
+The `installed` command can be used to list all available versions of the Solidity compiler:
 
 Example usage:
 
 ```bash
-solcix ls
+solcix installed
 ```
 
 If global / local version is set, it will be displayed as below:
 
 ```bash
 0.8.19
 0.5.2
@@ -143,14 +168,24 @@
 
 Simply run the command will see the changes:
 
 ```bash
 solc --version
 ```
 
+### Show current Solidity compiler version
+
+The `current` command can be used to show the current version of the Solidity compiler (local version takes precedence over global version):
+
+Example usage:
+
+```bash
+solcix current
+```
+
 ### Uninstalling Solidity compilers
 
 The `uninstall` command can be used to uninstall one or more versions of the Solidity compiler:
 
 ```bash
 solcix uninstall 0.8.4 0.7.6
 ```
@@ -204,15 +239,21 @@
 ```
 
 Additional optional arguments can be passed to the command using the kwargs argument, it will be taken by the [solc command](https://docs.soliditylang.org/en/v0.8.19/using-the-compiler.html#basic-usage).
 
 Example usage:
 
 ```bash
-solcix compile <file.sol> --optimize
+solcix compile <file.sol> --optimize=True --optimize-runs=200 --overwrite=True
+```
+
+Or you can redirect the output to a single json file:
+
+```bash
+solcix compile <file.sol> > output.json
 ```
 
 ### Resolve compatible versions from solidity file
 
 The `resolve` command is used to determine the recommended solc version for a Solidity file based on its pragma statement. It can also be used to list all versions that are compatible with the Solidity file.
 
 Example usage:
```

