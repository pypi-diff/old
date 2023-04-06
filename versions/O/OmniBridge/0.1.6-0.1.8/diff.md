# Comparing `tmp/OmniBridge-0.1.6.tar.gz` & `tmp/OmniBridge-0.1.8.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "OmniBridge-0.1.6.tar", last modified: Thu Apr  6 15:36:45 2023, max compression
+gzip compressed data, was "OmniBridge-0.1.8.tar", last modified: Thu Apr  6 15:44:17 2023, max compression
```

## Comparing `OmniBridge-0.1.6.tar` & `OmniBridge-0.1.8.tar`

### file list

```diff
@@ -1,17 +1,17 @@
-drwxrwxrwx   0        0        0        0 2023-04-06 15:36:45.025893 OmniBridge-0.1.6/
--rw-rw-rw-   0        0        0    11558 2023-04-06 06:04:35.000000 OmniBridge-0.1.6/LICENSE
-drwxrwxrwx   0        0        0        0 2023-04-06 15:36:45.020892 OmniBridge-0.1.6/OmniBridge.egg-info/
--rw-rw-rw-   0        0        0      951 2023-04-06 15:36:44.000000 OmniBridge-0.1.6/OmniBridge.egg-info/PKG-INFO
--rw-rw-rw-   0        0        0      253 2023-04-06 15:36:44.000000 OmniBridge-0.1.6/OmniBridge.egg-info/SOURCES.txt
--rw-rw-rw-   0        0        0        1 2023-04-06 15:36:44.000000 OmniBridge-0.1.6/OmniBridge.egg-info/dependency_links.txt
--rw-rw-rw-   0        0        0       23 2023-04-06 15:36:44.000000 OmniBridge-0.1.6/OmniBridge.egg-info/requires.txt
--rw-rw-rw-   0        0        0        4 2023-04-06 15:36:44.000000 OmniBridge-0.1.6/OmniBridge.egg-info/top_level.txt
--rw-rw-rw-   0        0        0      951 2023-04-06 15:36:45.025893 OmniBridge-0.1.6/PKG-INFO
--rw-rw-rw-   0        0        0      659 2023-04-06 05:36:51.000000 OmniBridge-0.1.6/README.md
--rw-rw-rw-   0        0        0     1151 2023-04-05 09:41:50.000000 OmniBridge-0.1.6/pyproject.toml
--rw-rw-rw-   0        0        0       42 2023-04-06 15:36:45.026892 OmniBridge-0.1.6/setup.cfg
--rw-rw-rw-   0        0        0      903 2023-04-06 15:36:27.000000 OmniBridge-0.1.6/setup.py
-drwxrwxrwx   0        0        0        0 2023-04-06 15:36:45.024892 OmniBridge-0.1.6/src/
--rw-rw-rw-   0        0        0        0 2023-04-06 08:39:45.000000 OmniBridge-0.1.6/src/__init__.py
--rw-rw-rw-   0        0        0     1598 2023-04-06 08:26:29.000000 OmniBridge-0.1.6/src/main.py
--rw-rw-rw-   0        0        0       17 2023-04-06 15:25:16.000000 OmniBridge-0.1.6/src/version.py
+drwxrwxrwx   0        0        0        0 2023-04-06 15:44:17.919069 OmniBridge-0.1.8/
+-rw-rw-rw-   0        0        0    11558 2023-04-06 06:04:35.000000 OmniBridge-0.1.8/LICENSE
+drwxrwxrwx   0        0        0        0 2023-04-06 15:44:17.914040 OmniBridge-0.1.8/OmniBridge.egg-info/
+-rw-rw-rw-   0        0        0      951 2023-04-06 15:44:17.000000 OmniBridge-0.1.8/OmniBridge.egg-info/PKG-INFO
+-rw-rw-rw-   0        0        0      274 2023-04-06 15:44:17.000000 OmniBridge-0.1.8/OmniBridge.egg-info/SOURCES.txt
+-rw-rw-rw-   0        0        0        1 2023-04-06 15:44:17.000000 OmniBridge-0.1.8/OmniBridge.egg-info/dependency_links.txt
+-rw-rw-rw-   0        0        0       23 2023-04-06 15:44:17.000000 OmniBridge-0.1.8/OmniBridge.egg-info/requires.txt
+-rw-rw-rw-   0        0        0       11 2023-04-06 15:44:17.000000 OmniBridge-0.1.8/OmniBridge.egg-info/top_level.txt
+-rw-rw-rw-   0        0        0      951 2023-04-06 15:44:17.918069 OmniBridge-0.1.8/PKG-INFO
+-rw-rw-rw-   0        0        0      659 2023-04-06 05:36:51.000000 OmniBridge-0.1.8/README.md
+drwxrwxrwx   0        0        0        0 2023-04-06 15:44:17.917040 OmniBridge-0.1.8/omnibridge/
+-rw-rw-rw-   0        0        0        0 2023-04-06 08:39:45.000000 OmniBridge-0.1.8/omnibridge/__init__.py
+-rw-rw-rw-   0        0        0     1598 2023-04-06 08:26:29.000000 OmniBridge-0.1.8/omnibridge/main.py
+-rw-rw-rw-   0        0        0       17 2023-04-06 15:25:16.000000 OmniBridge-0.1.8/omnibridge/version.py
+-rw-rw-rw-   0        0        0     1151 2023-04-05 09:41:50.000000 OmniBridge-0.1.8/pyproject.toml
+-rw-rw-rw-   0        0        0       42 2023-04-06 15:44:17.919069 OmniBridge-0.1.8/setup.cfg
+-rw-rw-rw-   0        0        0      924 2023-04-06 15:42:54.000000 OmniBridge-0.1.8/setup.py
```

### Comparing `OmniBridge-0.1.6/LICENSE` & `OmniBridge-0.1.8/LICENSE`

 * *Files identical despite different names*

### Comparing `OmniBridge-0.1.6/OmniBridge.egg-info/PKG-INFO` & `OmniBridge-0.1.8/OmniBridge.egg-info/PKG-INFO`

 * *Files 24% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: OmniBridge
-Version: 0.1.6
+Version: 0.1.8
 Summary: Bridging AI models
 Home-page: https://github.com/tmpOrgName/OmniBridge
 Author: OmniSpective
 Author-email: eliran9692@gmail.com
 License: Apache License 2.0
 Description-Content-Type: text/markdown
 License-File: LICENSE
```

### Comparing `OmniBridge-0.1.6/PKG-INFO` & `OmniBridge-0.1.8/PKG-INFO`

 * *Files 24% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: OmniBridge
-Version: 0.1.6
+Version: 0.1.8
 Summary: Bridging AI models
 Home-page: https://github.com/tmpOrgName/OmniBridge
 Author: OmniSpective
 Author-email: eliran9692@gmail.com
 License: Apache License 2.0
 Description-Content-Type: text/markdown
 License-File: LICENSE
```

### Comparing `OmniBridge-0.1.6/README.md` & `OmniBridge-0.1.8/README.md`

 * *Files identical despite different names*

### Comparing `OmniBridge-0.1.6/pyproject.toml` & `OmniBridge-0.1.8/pyproject.toml`

 * *Files identical despite different names*

### Comparing `OmniBridge-0.1.6/setup.py` & `OmniBridge-0.1.8/setup.py`

 * *Files 21% similar despite different names*

```diff
@@ -4,31 +4,31 @@
 import os
 
 this_directory = path.abspath(path.dirname(__file__))
 with open(path.join(this_directory, "README.md"), encoding="utf-8") as f:
     long_description = f.read()
 
 spec = util.spec_from_file_location(
-    "src.version", os.path.join("src", "version.py")
+    "omnibridge.version", os.path.join("omnibridge", "version.py")
 )
 mod = util.module_from_spec(spec)
 spec.loader.exec_module(mod)
 version = mod.version
 
 
 setup(
     name='OmniBridge',
     license="Apache License 2.0",
-    version="0.1.6",
+    version="0.1.8",
     author='OmniSpective',
     author_email='eliran9692@gmail.com',
     description='Bridging AI models',
     long_description=long_description,
     long_description_content_type="text/markdown",
     url='https://github.com/tmpOrgName/OmniBridge',
-    packages=['src'],
+    packages=['omnibridge'],
     install_requires=[
         'requests',
         'ruff',
         'argparse'
     ],
 )
```

### Comparing `OmniBridge-0.1.6/src/main.py` & `OmniBridge-0.1.8/omnibridge/main.py`

 * *Files identical despite different names*

