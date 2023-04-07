# Comparing `tmp/solcix-0.1.6.tar.gz` & `tmp/solcix-0.1.7.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "solcix-0.1.6.tar", max compression
+gzip compressed data, was "solcix-0.1.7.tar", max compression
```

## Comparing `solcix-0.1.6.tar` & `solcix-0.1.7.tar`

### file list

```diff
@@ -1,17 +1,17 @@
--rw-r--r--   0        0        0    34523 2023-04-07 01:15:56.610498 solcix-0.1.6/LICENSE
--rw-r--r--   0        0        0     8212 2023-04-07 01:15:56.610498 solcix-0.1.6/README.md
--rw-r--r--   0        0        0      871 2023-04-07 01:15:56.610498 solcix-0.1.6/pyproject.toml
--rw-r--r--   0        0        0     1109 2023-04-07 01:15:56.610498 solcix-0.1.6/solcix/__init__.py
--rw-r--r--   0        0        0     8987 2023-04-07 01:15:56.610498 solcix-0.1.6/solcix/__main__.py
--rw-r--r--   0        0        0      182 2023-04-07 01:15:56.610498 solcix-0.1.6/solcix/compile/__init__.py
--rw-r--r--   0        0        0    19156 2023-04-07 01:15:56.610498 solcix-0.1.6/solcix/compile/solc.py
--rw-r--r--   0        0        0      618 2023-04-07 01:15:56.610498 solcix-0.1.6/solcix/constant.py
--rw-r--r--   0        0        0      110 2023-04-07 01:15:56.610498 solcix-0.1.6/solcix/datatypes/__init__.py
--rw-r--r--   0        0        0     3949 2023-04-07 01:15:56.610498 solcix-0.1.6/solcix/datatypes/datatypes.py
--rw-r--r--   0        0        0     3407 2023-04-07 01:15:56.610498 solcix-0.1.6/solcix/errors.py
--rw-r--r--   0        0        0    21648 2023-04-07 01:15:56.610498 solcix-0.1.6/solcix/installer.py
--rw-r--r--   0        0        0      241 2023-04-07 01:15:56.610498 solcix-0.1.6/solcix/manage/__init__.py
--rw-r--r--   0        0        0     3773 2023-04-07 01:15:56.610498 solcix-0.1.6/solcix/manage/manage.py
--rw-r--r--   0        0        0    10656 2023-04-07 01:15:56.610498 solcix-0.1.6/solcix/resolver.py
--rw-r--r--   0        0        0      597 2023-04-07 01:15:56.610498 solcix-0.1.6/solcix/utils.py
--rw-r--r--   0        0        0     9373 1970-01-01 00:00:00.000000 solcix-0.1.6/PKG-INFO
+-rw-r--r--   0        0        0    34523 2023-04-07 11:28:07.282960 solcix-0.1.7/LICENSE
+-rw-r--r--   0        0        0     8208 2023-04-07 11:28:07.282960 solcix-0.1.7/README.md
+-rw-r--r--   0        0        0      871 2023-04-07 11:28:07.282960 solcix-0.1.7/pyproject.toml
+-rw-r--r--   0        0        0     1109 2023-04-07 11:28:07.282960 solcix-0.1.7/solcix/__init__.py
+-rw-r--r--   0        0        0     9081 2023-04-07 11:28:07.282960 solcix-0.1.7/solcix/__main__.py
+-rw-r--r--   0        0        0      182 2023-04-07 11:28:07.282960 solcix-0.1.7/solcix/compile/__init__.py
+-rw-r--r--   0        0        0    19156 2023-04-07 11:28:07.282960 solcix-0.1.7/solcix/compile/solc.py
+-rw-r--r--   0        0        0      618 2023-04-07 11:28:07.282960 solcix-0.1.7/solcix/constant.py
+-rw-r--r--   0        0        0      110 2023-04-07 11:28:07.282960 solcix-0.1.7/solcix/datatypes/__init__.py
+-rw-r--r--   0        0        0     3949 2023-04-07 11:28:07.282960 solcix-0.1.7/solcix/datatypes/datatypes.py
+-rw-r--r--   0        0        0     3407 2023-04-07 11:28:07.282960 solcix-0.1.7/solcix/errors.py
+-rw-r--r--   0        0        0    21648 2023-04-07 11:28:07.282960 solcix-0.1.7/solcix/installer.py
+-rw-r--r--   0        0        0      241 2023-04-07 11:28:07.282960 solcix-0.1.7/solcix/manage/__init__.py
+-rw-r--r--   0        0        0     3773 2023-04-07 11:28:07.282960 solcix-0.1.7/solcix/manage/manage.py
+-rw-r--r--   0        0        0    10656 2023-04-07 11:28:07.282960 solcix-0.1.7/solcix/resolver.py
+-rw-r--r--   0        0        0      597 2023-04-07 11:28:07.282960 solcix-0.1.7/solcix/utils.py
+-rw-r--r--   0        0        0     9369 1970-01-01 00:00:00.000000 solcix-0.1.7/PKG-INFO
```

### Comparing `solcix-0.1.6/LICENSE` & `solcix-0.1.7/LICENSE`

 * *Files identical despite different names*

### Comparing `solcix-0.1.6/README.md` & `solcix-0.1.7/README.md`

 * *Files 1% similar despite different names*

```diff
@@ -109,21 +109,20 @@
 ```bash
 solcix installed
 ```
 
 If global / local version is set, it will be displayed as below:
 
 ```bash
-0.8.19
-0.5.2
-0.5.1
 0.5.0
-0.8.0 <- current
 0.8.0
 0.8.16
+0.8.17
+0.8.18 <- current
+0.8.19
 ```
 
 ### Switching between Solidity compilers
 
 The `use` command can be used to switch between installed versions of the Solidity compiler, either globally or locally.
 
 - If the specified version is not installed, it will be installed automatically.
@@ -172,15 +171,15 @@
 ```
 
 ### Uninstall all Solidity compilers
 
 To uninstall all versions of Solidity compiler that have been installed using solcix, you can use the following command:
 
 ```bash
-solcix prune
+solcix purge
 ```
 
 This will remove all versions of the Solidity compilers that have been installed by solcix, all cached files, and the solcix configuration file (local config takes precedence over global config).
 
 ### Verify Solidity compilers
 
 The `verify` command is used to verify the checksums of installed solc binaries and to reinstall any that are malformed.
```

### Comparing `solcix-0.1.6/pyproject.toml` & `solcix-0.1.7/pyproject.toml`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 [tool.poetry]
 name = "solcix"
-version = "0.1.6"
+version = "0.1.7"
 description = "A Python wrapper for the Solidity compiler. Switch between versions, compile, and manage artifacts."
 authors = ["alan890104 <alan890104@gmail.com>"]
 readme = "README.md"
 
 [tool.poetry.dependencies]
 python = "^3.8"
 cfgv = "3.3.1"
```

### Comparing `solcix-0.1.6/solcix/__init__.py` & `solcix-0.1.7/solcix/__init__.py`

 * *Files identical despite different names*

### Comparing `solcix-0.1.6/solcix/__main__.py` & `solcix-0.1.7/solcix/__main__.py`

 * *Files 1% similar despite different names*

```diff
@@ -95,15 +95,15 @@
 def uninstall(version: Union[List[str], str]):
     success, skipped, error = solcix.uninstall_solc(version)
     print(Fore.GREEN + f"success: {', '.join(success)}" + Style.RESET_ALL)
     print(Fore.YELLOW + f"skipped: {', '.join(skipped)}" + Style.RESET_ALL)
     print(Fore.RED + f"error  : {', '.join(error)}" + Style.RESET_ALL)
 
 @cli.command(help="Uninstall all solc binaries.")
-def prune():
+def purge():
     opt = click.confirm(default=False, text="Are you sure to uninstall all solc binaries, caches, and config files?")
     if opt is False:
         print(f"👀{Fore.YELLOW} You have canceled the operation. Indeed, a wise choice!{Style.RESET_ALL} 👀")
         return
     # Delete all cached versions
     solcix.clear_cache()
     # Delete all config files
@@ -132,15 +132,18 @@
 @click.pass_context
 def compile(ctx: click.Context, file: str, output: str):
     # Parse arguments
     params = dict()
     for segment in ctx.args:
         if segment.startswith("--") and segment.find("=") != 1:
             key, value = segment.strip("--").split("=")
-            params[key.replace("-","_")] = ast.literal_eval(value)
+            try:
+                params[key.replace("-","_")] = ast.literal_eval(value)
+            except:
+                params[key.replace("-","_")] = value
 
     # check output directory
     if output is not None:
         params["output_dir"] = output
         if os.path.exists(output) and "overwrite" not in params:
             click.confirm(f"Output path `{output}` already exists, do you want to overwrite it?", default=False, abort=True)
             params["overwrite"] = True
```

### Comparing `solcix-0.1.6/solcix/compile/solc.py` & `solcix-0.1.7/solcix/compile/solc.py`

 * *Files identical despite different names*

### Comparing `solcix-0.1.6/solcix/constant.py` & `solcix-0.1.7/solcix/constant.py`

 * *Files identical despite different names*

### Comparing `solcix-0.1.6/solcix/datatypes/datatypes.py` & `solcix-0.1.7/solcix/datatypes/datatypes.py`

 * *Files identical despite different names*

### Comparing `solcix-0.1.6/solcix/errors.py` & `solcix-0.1.7/solcix/errors.py`

 * *Files identical despite different names*

### Comparing `solcix-0.1.6/solcix/installer.py` & `solcix-0.1.7/solcix/installer.py`

 * *Files identical despite different names*

### Comparing `solcix-0.1.6/solcix/manage/manage.py` & `solcix-0.1.7/solcix/manage/manage.py`

 * *Files identical despite different names*

### Comparing `solcix-0.1.6/solcix/resolver.py` & `solcix-0.1.7/solcix/resolver.py`

 * *Files identical despite different names*

### Comparing `solcix-0.1.6/solcix/utils.py` & `solcix-0.1.7/solcix/utils.py`

 * *Files identical despite different names*

### Comparing `solcix-0.1.6/PKG-INFO` & `solcix-0.1.7/PKG-INFO`

 * *Files 2% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: solcix
-Version: 0.1.6
+Version: 0.1.7
 Summary: A Python wrapper for the Solidity compiler. Switch between versions, compile, and manage artifacts.
 Author: alan890104
 Author-email: alan890104@gmail.com
 Requires-Python: >=3.8,<4.0
 Classifier: Programming Language :: Python :: 3
 Classifier: Programming Language :: Python :: 3.8
 Classifier: Programming Language :: Python :: 3.9
@@ -141,21 +141,20 @@
 ```bash
 solcix installed
 ```
 
 If global / local version is set, it will be displayed as below:
 
 ```bash
-0.8.19
-0.5.2
-0.5.1
 0.5.0
-0.8.0 <- current
 0.8.0
 0.8.16
+0.8.17
+0.8.18 <- current
+0.8.19
 ```
 
 ### Switching between Solidity compilers
 
 The `use` command can be used to switch between installed versions of the Solidity compiler, either globally or locally.
 
 - If the specified version is not installed, it will be installed automatically.
@@ -204,15 +203,15 @@
 ```
 
 ### Uninstall all Solidity compilers
 
 To uninstall all versions of Solidity compiler that have been installed using solcix, you can use the following command:
 
 ```bash
-solcix prune
+solcix purge
 ```
 
 This will remove all versions of the Solidity compilers that have been installed by solcix, all cached files, and the solcix configuration file (local config takes precedence over global config).
 
 ### Verify Solidity compilers
 
 The `verify` command is used to verify the checksums of installed solc binaries and to reinstall any that are malformed.
```

