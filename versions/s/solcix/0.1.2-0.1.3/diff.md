# Comparing `tmp/solcix-0.1.2.tar.gz` & `tmp/solcix-0.1.3.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "solcix-0.1.2.tar", max compression
+gzip compressed data, was "solcix-0.1.3.tar", max compression
```

## Comparing `solcix-0.1.2.tar` & `solcix-0.1.3.tar`

### file list

```diff
@@ -1,17 +1,17 @@
--rw-r--r--   0        0        0     5104 2023-04-06 11:59:09.004164 solcix-0.1.2/README.md
--rw-r--r--   0        0        0      935 2023-04-06 13:08:08.136419 solcix-0.1.2/pyproject.toml
--rw-r--r--   0        0        0     1103 2023-04-06 08:51:29.868152 solcix-0.1.2/solcix/__init__.py
--rw-r--r--   0        0        0     6469 2023-04-06 12:57:41.589225 solcix-0.1.2/solcix/__main__.py
--rw-r--r--   0        0        0       22 2023-04-06 13:06:39.195988 solcix-0.1.2/solcix/__version__.py
--rw-r--r--   0        0        0      182 2023-04-06 06:47:58.651981 solcix-0.1.2/solcix/compile/__init__.py
--rw-r--r--   0        0        0    19134 2023-04-06 09:25:41.021963 solcix-0.1.2/solcix/compile/solc.py
--rw-r--r--   0        0        0      618 2023-04-05 16:12:30.242253 solcix-0.1.2/solcix/constant.py
--rw-r--r--   0        0        0      110 2023-04-05 14:24:43.655338 solcix-0.1.2/solcix/datatypes/__init__.py
--rw-r--r--   0        0        0     3949 2023-04-06 08:39:27.233614 solcix-0.1.2/solcix/datatypes/datatypes.py
--rw-r--r--   0        0        0     3407 2023-04-06 08:32:26.769062 solcix-0.1.2/solcix/errors.py
--rw-r--r--   0        0        0    19449 2023-04-06 11:09:01.513052 solcix-0.1.2/solcix/installer.py
--rw-r--r--   0        0        0      247 2023-04-05 17:30:43.390279 solcix-0.1.2/solcix/manage/__init__.py
--rw-r--r--   0        0        0     4799 2023-04-06 13:03:26.451012 solcix-0.1.2/solcix/manage/manage.py
--rw-r--r--   0        0        0    10403 2023-04-05 18:06:59.201642 solcix-0.1.2/solcix/resolver.py
--rw-r--r--   0        0        0      597 2023-04-06 08:38:41.565504 solcix-0.1.2/solcix/utils.py
--rw-r--r--   0        0        0     6310 1970-01-01 00:00:00.000000 solcix-0.1.2/PKG-INFO
+-rw-r--r--   0        0        0     5674 2023-04-06 13:35:08.183788 solcix-0.1.3/README.md
+-rw-r--r--   0        0        0      935 2023-04-06 13:35:30.091923 solcix-0.1.3/pyproject.toml
+-rw-r--r--   0        0        0     1103 2023-04-06 08:51:29.868152 solcix-0.1.3/solcix/__init__.py
+-rw-r--r--   0        0        0     6993 2023-04-06 13:32:17.118795 solcix-0.1.3/solcix/__main__.py
+-rw-r--r--   0        0        0       22 2023-04-06 13:35:25.067892 solcix-0.1.3/solcix/__version__.py
+-rw-r--r--   0        0        0      182 2023-04-06 06:47:58.651981 solcix-0.1.3/solcix/compile/__init__.py
+-rw-r--r--   0        0        0    19134 2023-04-06 09:25:41.021963 solcix-0.1.3/solcix/compile/solc.py
+-rw-r--r--   0        0        0      618 2023-04-05 16:12:30.242253 solcix-0.1.3/solcix/constant.py
+-rw-r--r--   0        0        0      110 2023-04-05 14:24:43.655338 solcix-0.1.3/solcix/datatypes/__init__.py
+-rw-r--r--   0        0        0     3949 2023-04-06 08:39:27.233614 solcix-0.1.3/solcix/datatypes/datatypes.py
+-rw-r--r--   0        0        0     3407 2023-04-06 08:32:26.769062 solcix-0.1.3/solcix/errors.py
+-rw-r--r--   0        0        0    19449 2023-04-06 11:09:01.513052 solcix-0.1.3/solcix/installer.py
+-rw-r--r--   0        0        0      247 2023-04-05 17:30:43.390279 solcix-0.1.3/solcix/manage/__init__.py
+-rw-r--r--   0        0        0     4759 2023-04-06 13:22:11.056207 solcix-0.1.3/solcix/manage/manage.py
+-rw-r--r--   0        0        0    10403 2023-04-05 18:06:59.201642 solcix-0.1.3/solcix/resolver.py
+-rw-r--r--   0        0        0      597 2023-04-06 08:38:41.565504 solcix-0.1.3/solcix/utils.py
+-rw-r--r--   0        0        0     6880 1970-01-01 00:00:00.000000 solcix-0.1.3/PKG-INFO
```

### Comparing `solcix-0.1.2/README.md` & `solcix-0.1.3/README.md`

 * *Files 5% similar despite different names*

```diff
@@ -118,14 +118,24 @@
 
 The `uninstall` command can be used to uninstall one or more versions of the Solidity compiler:
 
 ```bash
 solcix uninstall 0.8.4 0.7.6
 ```
 
+### Uninstall all Solidity compilers
+
+To uninstall all versions of Solidity compiler that have been installed using solcix, you can use the following command:
+
+```bash
+solcix prune
+```
+
+This will remove all versions of the Solidity compiler that have been installed by solcix.
+
 ### Verify Solidity compilers
 
 The `verify` command is used to verify the checksums of installed solc binaries and to reinstall any that are malformed.
 
 Example usage:
 
 ```bash
@@ -203,7 +213,20 @@
 
 ```bash
 These versions are compatible with the pragma.
 0.8.5
 0.8.6
 0.8.7
 ```
+
+### Upgrade Solcix
+
+The `upgrade` command is used to upgrade the architecture of the installed solc binaries, it will remove all old binaries and download the new ones.
+
+Example usage:
+
+```bash
+pip3 install -U
+
+# Migrate to the new architecture and Reinstall all binaries
+solcix upgrade
+```
```

### Comparing `solcix-0.1.2/pyproject.toml` & `solcix-0.1.3/pyproject.toml`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 [tool.poetry]
 name = "solcix"
-version = "0.1.2"
+version = "0.1.3"
 description = "A Python wrapper for the Solidity compiler. Switch between versions, compile, and manage artifacts."
 authors = ["alan890104 <alan890104@gmail.com>"]
 readme = "README.md"
 
 [tool.poetry.dependencies]
 python = "^3.8"
 cfgv = "3.3.1"
```

### Comparing `solcix-0.1.2/solcix/__init__.py` & `solcix-0.1.3/solcix/__init__.py`

 * *Files identical despite different names*

### Comparing `solcix-0.1.2/solcix/__main__.py` & `solcix-0.1.3/solcix/__main__.py`

 * *Files 4% similar despite different names*

```diff
@@ -49,23 +49,24 @@
         print(f"release: {release:6s} | artifact: {artifact}")
     print(Fore.GREEN + f"latest: {latest}" + Style.RESET_ALL)
 
 
 @cli.command(help="List all installed solc versions.")
 def installed():
     installed = solcix.get_installed_versions()
+    installed = sorted(installed, key=Version)
     try:
         current, _ = solcix.manage.current_version()
         for version in installed:
             if current == version:
                 print(Fore.GREEN + f"{version} <- current" + Style.RESET_ALL)
             print(version)
     except NotInstalledError as e:
         print(Fore.YELLOW + f"{e}" + Style.RESET_ALL)
-        for version in sorted(installed, key=Version):
+        for version in installed:
             print(version)
 
 
 @cli.command(help="Switch between solc versions. If the version is not installed, it will be installed.")
 @click.argument("scope", nargs=1, required=True, type=click.Choice(["global", "local"]))
 @click.argument("version", nargs=1, required=True, type=click.STRING)
 def use(scope: str, version: str):
@@ -79,23 +80,27 @@
 @click.argument("version", nargs=-1, required=True, type=click.STRING)
 def uninstall(version: Union[List[str], str]):
     success, skipped, error = solcix.uninstall_solc(version)
     print(Fore.GREEN + f"success: {', '.join(success)}" + Style.RESET_ALL)
     print(Fore.YELLOW + f"skipped: {', '.join(skipped)}" + Style.RESET_ALL)
     print(Fore.RED + f"error  : {', '.join(error)}" + Style.RESET_ALL)
 
+@cli.command(help="Uninstall all solc binaries.")
+def prune():
+    versions = solcix.get_installed_versions()
+    success, skipped, error = solcix.uninstall_solc(versions)
+    print(Fore.GREEN + f"success: {', '.join(success)}" + Style.RESET_ALL)
+    print(Fore.YELLOW + f"skipped: {', '.join(skipped)}" + Style.RESET_ALL)
+    print(Fore.RED + f"error  : {', '.join(error)}" + Style.RESET_ALL)
 
-@cli.command(
-    help="Verify checksums of installed solc binaries, and reinstall malformed ones."
-)
+@cli.command(help="Verify checksums of installed solc binaries, and reinstall malformed ones.")
 @click.argument("version", nargs=-1, required=True, type=click.STRING)
 def verify(version: Union[List[str], str]):
     solcix.verify_solc(version)
 
-
 @cli.command(help="Remove all cached files.")
 def clear():
     solcix.clear_cache()
 
 
 @cli.command(context_settings=dict(ignore_unknown_options=True), help="Compile Solidity files and print the result, if the output is a TTY, the result will be formatted. Otherwise the result will be printed as a JSON string.")
 @click.argument("file", nargs=1, required=True, type=click.Path(exists=True))
@@ -136,18 +141,26 @@
     else:
         versions = solcix.get_compatible_versions(pragma)
         print("These versions are compatible with the pragma.")
         for version in versions:
             print(version)
 
 
+@cli.command()
+def upgrade():
+    solcix.manage.upgrade_architecture()
+
+
 def solc() -> None:
     try:
         current = solcix.manage.current_version()
         version, _ = current
         path = ARTIFACT_DIR.joinpath(f"solc-{version}", f"solc-{version}")
         subprocess.run([str(path), *sys.argv[1:]], check=True)
     except NotInstalledError as e:
         print(Fore.RED + str(e) + Style.RESET_ALL)
         sys.exit(1)
     except subprocess.CalledProcessError as e:
         sys.exit(e.returncode)
+
+if __name__ == "__main__":
+    cli()
```

### Comparing `solcix-0.1.2/solcix/compile/solc.py` & `solcix-0.1.3/solcix/compile/solc.py`

 * *Files identical despite different names*

### Comparing `solcix-0.1.2/solcix/constant.py` & `solcix-0.1.3/solcix/constant.py`

 * *Files identical despite different names*

### Comparing `solcix-0.1.2/solcix/datatypes/datatypes.py` & `solcix-0.1.3/solcix/datatypes/datatypes.py`

 * *Files identical despite different names*

### Comparing `solcix-0.1.2/solcix/errors.py` & `solcix-0.1.3/solcix/errors.py`

 * *Files identical despite different names*

### Comparing `solcix-0.1.2/solcix/installer.py` & `solcix-0.1.3/solcix/installer.py`

 * *Files identical despite different names*

### Comparing `solcix-0.1.2/solcix/manage/manage.py` & `solcix-0.1.3/solcix/manage/manage.py`

 * *Files 4% similar despite different names*

```diff
@@ -135,21 +135,19 @@
     Upgrade the architecture.
 
     If there are installed versions of solc, remove the current ARTIFACT_DIR directory and install the latest
     version of solc.
 
     Raises:
     -------
-    argparse.ArgumentTypeError
+    NotInstalledError
         If there are no installed versions of solc.
 
     """
     currently_installed = get_installed_versions()
     if len(currently_installed) > 0:
         shutil.rmtree(ARTIFACT_DIR)
         os.makedirs(ARTIFACT_DIR, exist_ok=True)
         install_solc(currently_installed)
         print("🔥 solcix is now up to date! 🔥")
     else:
-        raise argparse.ArgumentTypeError(
-            "Run `solcix install --help` for more information"
-        )
+        raise NotInstalledError("Run `solcix install --help` for more information")
```

### Comparing `solcix-0.1.2/solcix/resolver.py` & `solcix-0.1.3/solcix/resolver.py`

 * *Files identical despite different names*

### Comparing `solcix-0.1.2/solcix/utils.py` & `solcix-0.1.3/solcix/utils.py`

 * *Files identical despite different names*

### Comparing `solcix-0.1.2/PKG-INFO` & `solcix-0.1.3/PKG-INFO`

 * *Files 3% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: solcix
-Version: 0.1.2
+Version: 0.1.3
 Summary: A Python wrapper for the Solidity compiler. Switch between versions, compile, and manage artifacts.
 Author: alan890104
 Author-email: alan890104@gmail.com
 Requires-Python: >=3.8,<4.0
 Classifier: Programming Language :: Python :: 3
 Classifier: Programming Language :: Python :: 3.8
 Classifier: Programming Language :: Python :: 3.9
@@ -151,14 +151,24 @@
 
 The `uninstall` command can be used to uninstall one or more versions of the Solidity compiler:
 
 ```bash
 solcix uninstall 0.8.4 0.7.6
 ```
 
+### Uninstall all Solidity compilers
+
+To uninstall all versions of Solidity compiler that have been installed using solcix, you can use the following command:
+
+```bash
+solcix prune
+```
+
+This will remove all versions of the Solidity compiler that have been installed by solcix.
+
 ### Verify Solidity compilers
 
 The `verify` command is used to verify the checksums of installed solc binaries and to reinstall any that are malformed.
 
 Example usage:
 
 ```bash
@@ -237,7 +247,20 @@
 ```bash
 These versions are compatible with the pragma.
 0.8.5
 0.8.6
 0.8.7
 ```
 
+### Upgrade Solcix
+
+The `upgrade` command is used to upgrade the architecture of the installed solc binaries, it will remove all old binaries and download the new ones.
+
+Example usage:
+
+```bash
+pip3 install -U
+
+# Migrate to the new architecture and Reinstall all binaries
+solcix upgrade
+```
+
```

