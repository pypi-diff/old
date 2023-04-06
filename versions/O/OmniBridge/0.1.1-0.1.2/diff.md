# Comparing `tmp/OmniBridge-0.1.1.tar.gz` & `tmp/OmniBridge-0.1.2.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "OmniBridge-0.1.1.tar", last modified: Thu Apr  6 14:49:53 2023, max compression
+gzip compressed data, was "OmniBridge-0.1.2.tar", last modified: Thu Apr  6 15:07:22 2023, max compression
```

## Comparing `OmniBridge-0.1.1.tar` & `OmniBridge-0.1.2.tar`

### file list

```diff
@@ -1,16 +1,16 @@
-drwxrwxrwx   0        0        0        0 2023-04-06 14:49:53.476498 OmniBridge-0.1.1/
--rw-rw-rw-   0        0        0    11558 2023-04-06 06:04:35.000000 OmniBridge-0.1.1/LICENSE
-drwxrwxrwx   0        0        0        0 2023-04-06 14:49:53.472498 OmniBridge-0.1.1/OmniBridge.egg-info/
--rw-rw-rw-   0        0        0      881 2023-04-06 14:49:53.000000 OmniBridge-0.1.1/OmniBridge.egg-info/PKG-INFO
--rw-rw-rw-   0        0        0      238 2023-04-06 14:49:53.000000 OmniBridge-0.1.1/OmniBridge.egg-info/SOURCES.txt
--rw-rw-rw-   0        0        0        1 2023-04-06 14:49:53.000000 OmniBridge-0.1.1/OmniBridge.egg-info/dependency_links.txt
--rw-rw-rw-   0        0        0       23 2023-04-06 14:49:53.000000 OmniBridge-0.1.1/OmniBridge.egg-info/requires.txt
--rw-rw-rw-   0        0        0        4 2023-04-06 14:49:53.000000 OmniBridge-0.1.1/OmniBridge.egg-info/top_level.txt
--rw-rw-rw-   0        0        0      881 2023-04-06 14:49:53.476498 OmniBridge-0.1.1/PKG-INFO
--rw-rw-rw-   0        0        0      659 2023-04-06 05:36:51.000000 OmniBridge-0.1.1/README.md
--rw-rw-rw-   0        0        0     1151 2023-04-05 09:41:50.000000 OmniBridge-0.1.1/pyproject.toml
--rw-rw-rw-   0        0        0       42 2023-04-06 14:49:53.476498 OmniBridge-0.1.1/setup.cfg
--rw-rw-rw-   0        0        0      629 2023-04-06 09:05:44.000000 OmniBridge-0.1.1/setup.py
-drwxrwxrwx   0        0        0        0 2023-04-06 14:49:53.475499 OmniBridge-0.1.1/src/
--rw-rw-rw-   0        0        0        0 2023-04-06 08:39:45.000000 OmniBridge-0.1.1/src/__init__.py
--rw-rw-rw-   0        0        0     1598 2023-04-06 08:26:29.000000 OmniBridge-0.1.1/src/main.py
+drwxrwxrwx   0        0        0        0 2023-04-06 15:07:22.246662 OmniBridge-0.1.2/
+-rw-rw-rw-   0        0        0    11558 2023-04-06 06:04:35.000000 OmniBridge-0.1.2/LICENSE
+drwxrwxrwx   0        0        0        0 2023-04-06 15:07:22.243152 OmniBridge-0.1.2/OmniBridge.egg-info/
+-rw-rw-rw-   0        0        0      951 2023-04-06 15:07:22.000000 OmniBridge-0.1.2/OmniBridge.egg-info/PKG-INFO
+-rw-rw-rw-   0        0        0      238 2023-04-06 15:07:22.000000 OmniBridge-0.1.2/OmniBridge.egg-info/SOURCES.txt
+-rw-rw-rw-   0        0        0        1 2023-04-06 15:07:22.000000 OmniBridge-0.1.2/OmniBridge.egg-info/dependency_links.txt
+-rw-rw-rw-   0        0        0       23 2023-04-06 15:07:22.000000 OmniBridge-0.1.2/OmniBridge.egg-info/requires.txt
+-rw-rw-rw-   0        0        0        4 2023-04-06 15:07:22.000000 OmniBridge-0.1.2/OmniBridge.egg-info/top_level.txt
+-rw-rw-rw-   0        0        0      951 2023-04-06 15:07:22.246662 OmniBridge-0.1.2/PKG-INFO
+-rw-rw-rw-   0        0        0      659 2023-04-06 05:36:51.000000 OmniBridge-0.1.2/README.md
+-rw-rw-rw-   0        0        0     1151 2023-04-05 09:41:50.000000 OmniBridge-0.1.2/pyproject.toml
+-rw-rw-rw-   0        0        0       42 2023-04-06 15:07:22.247662 OmniBridge-0.1.2/setup.cfg
+-rw-rw-rw-   0        0        0      716 2023-04-06 15:04:51.000000 OmniBridge-0.1.2/setup.py
+drwxrwxrwx   0        0        0        0 2023-04-06 15:07:22.245657 OmniBridge-0.1.2/src/
+-rw-rw-rw-   0        0        0        0 2023-04-06 08:39:45.000000 OmniBridge-0.1.2/src/__init__.py
+-rw-rw-rw-   0        0        0     1598 2023-04-06 08:26:29.000000 OmniBridge-0.1.2/src/main.py
```

### Comparing `OmniBridge-0.1.1/LICENSE` & `OmniBridge-0.1.2/LICENSE`

 * *Files identical despite different names*

### Comparing `OmniBridge-0.1.1/OmniBridge.egg-info/PKG-INFO` & `OmniBridge-0.1.2/README.md`

 * *Files 24% similar despite different names*

```diff
@@ -1,16 +1,7 @@
-Metadata-Version: 2.1
-Name: OmniBridge
-Version: 0.1.1
-Summary: Bridging AI models
-Home-page: https://github.com/tmpOrgName/OmniBridge
-Author: OmniSpective
-Author-email: eliran9692@gmail.com
-License-File: LICENSE
-
 # Install
 
 requirerments:
 * Python 3.11
 
 steps:
 1. git clone https://github.com/tmpOrgName/tmp.git
```

### Comparing `OmniBridge-0.1.1/PKG-INFO` & `OmniBridge-0.1.2/OmniBridge.egg-info/PKG-INFO`

 * *Files 27% similar despite different names*

```diff
@@ -1,14 +1,16 @@
 Metadata-Version: 2.1
 Name: OmniBridge
-Version: 0.1.1
+Version: 0.1.2
 Summary: Bridging AI models
 Home-page: https://github.com/tmpOrgName/OmniBridge
 Author: OmniSpective
 Author-email: eliran9692@gmail.com
+License: Apache License 2.0
+Description-Content-Type: text/markdown
 License-File: LICENSE
 
 # Install
 
 requirerments:
 * Python 3.11
```

### Comparing `OmniBridge-0.1.1/pyproject.toml` & `OmniBridge-0.1.2/pyproject.toml`

 * *Files identical despite different names*

### Comparing `OmniBridge-0.1.1/setup.py` & `OmniBridge-0.1.2/setup.py`

 * *Files 13% similar despite different names*

```diff
@@ -5,19 +5,21 @@
 this_directory = path.abspath(path.dirname(__file__))
 with open(path.join(this_directory, "README.md"), encoding="utf-8") as f:
     long_description = f.read()
 
 
 setup(
     name='OmniBridge',
+    license="Apache License 2.0",
     version=version,
     author='OmniSpective',
     author_email='eliran9692@gmail.com',
     description='Bridging AI models',
     long_description=long_description,
+    long_description_content_type="text/markdown",
     url='https://github.com/tmpOrgName/OmniBridge',
     packages=['src'],
     install_requires=[
         'requests',
         'ruff',
         'argparse'
     ],
```

### Comparing `OmniBridge-0.1.1/src/main.py` & `OmniBridge-0.1.2/src/main.py`

 * *Files identical despite different names*

