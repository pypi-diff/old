# Comparing `tmp/rubrical-0.1.1.tar.gz` & `tmp/rubrical-0.1.2.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "rubrical-0.1.1.tar", max compression
+gzip compressed data, was "rubrical-0.1.2.tar", max compression
```

## Comparing `rubrical-0.1.1.tar` & `rubrical-0.1.2.tar`

### file list

```diff
@@ -1,23 +1,23 @@
--rw-r--r--   0        0        0    15976 2023-04-01 07:44:34.225221 rubrical-0.1.1/LICENSE
--rw-r--r--   0        0        0     2543 2023-04-01 07:44:34.225221 rubrical-0.1.1/README.md
--rw-r--r--   0        0        0     1866 2023-04-01 07:44:59.169138 rubrical-0.1.1/pyproject.toml
--rw-r--r--   0        0        0        0 2023-04-01 07:44:34.225221 rubrical-0.1.1/rubrical/__init__.py
--rw-r--r--   0        0        0      784 2023-04-01 07:44:34.225221 rubrical-0.1.1/rubrical/comparisons/__init__.py
--rw-r--r--   0        0        0     1799 2023-04-01 07:44:34.225221 rubrical-0.1.1/rubrical/comparisons/semversion.py
--rw-r--r--   0        0        0      519 2023-04-01 07:44:34.225221 rubrical-0.1.1/rubrical/comparisons/string.py
--rw-r--r--   0        0        0      295 2023-04-01 07:44:34.225221 rubrical-0.1.1/rubrical/comparisons/utils.py
--rw-r--r--   0        0        0      504 2023-04-01 07:44:34.225221 rubrical-0.1.1/rubrical/enum.py
--rw-r--r--   0        0        0     2583 2023-04-01 07:44:34.225221 rubrical-0.1.1/rubrical/main.py
--rw-r--r--   0        0        0        0 2023-04-01 07:44:34.225221 rubrical-0.1.1/rubrical/package_managers/__init__.py
--rw-r--r--   0        0        0     1670 2023-04-01 07:44:34.225221 rubrical-0.1.1/rubrical/package_managers/base_package_manager.py
--rw-r--r--   0        0        0     1476 2023-04-01 07:44:34.225221 rubrical-0.1.1/rubrical/package_managers/jsonnet.py
--rw-r--r--   0        0        0     1931 2023-04-01 07:44:34.225221 rubrical-0.1.1/rubrical/package_managers/python.py
--rw-r--r--   0        0        0      271 2023-04-01 07:44:34.225221 rubrical-0.1.1/rubrical/package_managers/utilities/git.py
--rw-r--r--   0        0        0     2352 2023-04-01 07:44:34.225221 rubrical-0.1.1/rubrical/reporters/gh.py
--rw-r--r--   0        0        0     1476 2023-04-01 07:44:34.225221 rubrical-0.1.1/rubrical/reporters/terminal.py
--rw-r--r--   0        0        0     4057 2023-04-01 07:44:34.225221 rubrical-0.1.1/rubrical/rubrical.py
--rw-r--r--   0        0        0      467 2023-04-01 07:44:34.229221 rubrical-0.1.1/rubrical/schemas/configuration.py
--rw-r--r--   0        0        0      251 2023-04-01 07:44:34.229221 rubrical-0.1.1/rubrical/schemas/package.py
--rw-r--r--   0        0        0      235 2023-04-01 07:44:34.229221 rubrical-0.1.1/rubrical/schemas/results.py
--rw-r--r--   0        0        0      633 2023-04-01 07:44:34.229221 rubrical-0.1.1/rubrical/utilities/console.py
--rw-r--r--   0        0        0     3514 1970-01-01 00:00:00.000000 rubrical-0.1.1/PKG-INFO
+-rw-r--r--   0        0        0    15976 2023-04-06 09:35:32.148463 rubrical-0.1.2/LICENSE
+-rw-r--r--   0        0        0     2543 2023-04-06 09:35:32.148463 rubrical-0.1.2/README.md
+-rw-r--r--   0        0        0     1866 2023-04-06 09:35:58.760751 rubrical-0.1.2/pyproject.toml
+-rw-r--r--   0        0        0        0 2023-04-06 09:35:32.148463 rubrical-0.1.2/rubrical/__init__.py
+-rw-r--r--   0        0        0      784 2023-04-06 09:35:32.148463 rubrical-0.1.2/rubrical/comparisons/__init__.py
+-rw-r--r--   0        0        0     1799 2023-04-06 09:35:32.148463 rubrical-0.1.2/rubrical/comparisons/semversion.py
+-rw-r--r--   0        0        0      519 2023-04-06 09:35:32.148463 rubrical-0.1.2/rubrical/comparisons/string.py
+-rw-r--r--   0        0        0      295 2023-04-06 09:35:32.148463 rubrical-0.1.2/rubrical/comparisons/utils.py
+-rw-r--r--   0        0        0      504 2023-04-06 09:35:32.148463 rubrical-0.1.2/rubrical/enum.py
+-rw-r--r--   0        0        0     2623 2023-04-06 09:35:32.148463 rubrical-0.1.2/rubrical/main.py
+-rw-r--r--   0        0        0        0 2023-04-06 09:35:32.148463 rubrical-0.1.2/rubrical/package_managers/__init__.py
+-rw-r--r--   0        0        0     1670 2023-04-06 09:35:32.148463 rubrical-0.1.2/rubrical/package_managers/base_package_manager.py
+-rw-r--r--   0        0        0     1476 2023-04-06 09:35:32.148463 rubrical-0.1.2/rubrical/package_managers/jsonnet.py
+-rw-r--r--   0        0        0     1931 2023-04-06 09:35:32.148463 rubrical-0.1.2/rubrical/package_managers/python.py
+-rw-r--r--   0        0        0      271 2023-04-06 09:35:32.148463 rubrical-0.1.2/rubrical/package_managers/utilities/git.py
+-rw-r--r--   0        0        0     2352 2023-04-06 09:35:32.148463 rubrical-0.1.2/rubrical/reporters/gh.py
+-rw-r--r--   0        0        0     1476 2023-04-06 09:35:32.148463 rubrical-0.1.2/rubrical/reporters/terminal.py
+-rw-r--r--   0        0        0     4057 2023-04-06 09:35:32.148463 rubrical-0.1.2/rubrical/rubrical.py
+-rw-r--r--   0        0        0      467 2023-04-06 09:35:32.148463 rubrical-0.1.2/rubrical/schemas/configuration.py
+-rw-r--r--   0        0        0      251 2023-04-06 09:35:32.148463 rubrical-0.1.2/rubrical/schemas/package.py
+-rw-r--r--   0        0        0      235 2023-04-06 09:35:32.148463 rubrical-0.1.2/rubrical/schemas/results.py
+-rw-r--r--   0        0        0      633 2023-04-06 09:35:32.148463 rubrical-0.1.2/rubrical/utilities/console.py
+-rw-r--r--   0        0        0     3514 1970-01-01 00:00:00.000000 rubrical-0.1.2/PKG-INFO
```

### Comparing `rubrical-0.1.1/LICENSE` & `rubrical-0.1.2/LICENSE`

 * *Files identical despite different names*

### Comparing `rubrical-0.1.1/README.md` & `rubrical-0.1.2/README.md`

 * *Files identical despite different names*

### Comparing `rubrical-0.1.1/pyproject.toml` & `rubrical-0.1.2/pyproject.toml`

 * *Files 1% similar despite different names*

```diff
@@ -25,15 +25,15 @@
 [tool.isort]
 profile = "black"
 
 [tool.setuptools_scm]
 
 [tool.poetry]
 name = "rubrical"
-version = "0.1.1"
+version = "0.1.2"
 description = "A CLI to encourage (😅) people to update their dependencies!"
 authors = ["Ivan Lee <ivanklee86@gmail.com>"]
 license = "MPL-2.0"
 homepage = "https://github.com/ivanklee86/rubrical"
 repository = "https://github.com/ivanklee86/rubrical"
 readme = "README.md"
 classifiers=[
```

### Comparing `rubrical-0.1.1/rubrical/comparisons/__init__.py` & `rubrical-0.1.2/rubrical/comparisons/__init__.py`

 * *Files identical despite different names*

### Comparing `rubrical-0.1.1/rubrical/comparisons/semversion.py` & `rubrical-0.1.2/rubrical/comparisons/semversion.py`

 * *Files identical despite different names*

### Comparing `rubrical-0.1.1/rubrical/comparisons/string.py` & `rubrical-0.1.2/rubrical/comparisons/string.py`

 * *Files identical despite different names*

### Comparing `rubrical-0.1.1/rubrical/main.py` & `rubrical-0.1.2/rubrical/main.py`

 * *Files 5% similar despite different names*

```diff
@@ -28,15 +28,17 @@
         help="Github access token for reporting.  Presence will enable Github reporting.",
     ),
     gh_custom_url: str = typer.Option(
         "",
         envvar="RUBRICAL_GH_CUSTOM_URL",
         help="Github Enterprise custom url. e.g. https://github.custom.dev",
     ),
-    debug: bool = typer.Option(False, help="Enable debug messages"),
+    debug: bool = typer.Option(
+        False, envvar="RUBGRICAL_DEBUG", help="Enable debug messages"
+    ),
 ):
     """
     A CLI to encourage (😅) people to update their dependencies!
     """
 
     console.print_header("Rubrical starting!", "⚙️ ")
```

### Comparing `rubrical-0.1.1/rubrical/package_managers/base_package_manager.py` & `rubrical-0.1.2/rubrical/package_managers/base_package_manager.py`

 * *Files identical despite different names*

### Comparing `rubrical-0.1.1/rubrical/package_managers/jsonnet.py` & `rubrical-0.1.2/rubrical/package_managers/jsonnet.py`

 * *Files identical despite different names*

### Comparing `rubrical-0.1.1/rubrical/package_managers/python.py` & `rubrical-0.1.2/rubrical/package_managers/python.py`

 * *Files identical despite different names*

### Comparing `rubrical-0.1.1/rubrical/reporters/gh.py` & `rubrical-0.1.2/rubrical/reporters/gh.py`

 * *Files identical despite different names*

### Comparing `rubrical-0.1.1/rubrical/reporters/terminal.py` & `rubrical-0.1.2/rubrical/reporters/terminal.py`

 * *Files identical despite different names*

### Comparing `rubrical-0.1.1/rubrical/rubrical.py` & `rubrical-0.1.2/rubrical/rubrical.py`

 * *Files identical despite different names*

### Comparing `rubrical-0.1.1/rubrical/utilities/console.py` & `rubrical-0.1.2/rubrical/utilities/console.py`

 * *Files identical despite different names*

### Comparing `rubrical-0.1.1/PKG-INFO` & `rubrical-0.1.2/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: rubrical
-Version: 0.1.1
+Version: 0.1.2
 Summary: A CLI to encourage (😅) people to update their dependencies!
 Home-page: https://github.com/ivanklee86/rubrical
 License: MPL-2.0
 Author: Ivan Lee
 Author-email: ivanklee86@gmail.com
 Requires-Python: >=3.11,<4.0
 Classifier: Development Status :: 2 - Pre-Alpha
```

