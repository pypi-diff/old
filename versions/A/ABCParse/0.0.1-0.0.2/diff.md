# Comparing `tmp/ABCParse-0.0.1.tar.gz` & `tmp/ABCParse-0.0.2.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "ABCParse-0.0.1.tar", last modified: Fri Apr  7 03:21:10 2023, max compression
+gzip compressed data, was "ABCParse-0.0.2.tar", last modified: Fri Apr  7 03:23:59 2023, max compression
```

## Comparing `ABCParse-0.0.1.tar` & `ABCParse-0.0.2.tar`

### file list

```diff
@@ -1,14 +1,14 @@
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 03:21:10.382958 ABCParse-0.0.1/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 03:21:10.382958 ABCParse-0.0.1/ABCParse/
--rw-r--r--   0 runner    (1001) docker     (123)       47 2023-04-07 03:20:57.000000 ABCParse-0.0.1/ABCParse/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     2988 2023-04-07 03:20:57.000000 ABCParse-0.0.1/ABCParse/_abc_parse.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 03:21:10.382958 ABCParse-0.0.1/ABCParse.egg-info/
--rw-r--r--   0 runner    (1001) docker     (123)      904 2023-04-07 03:21:10.000000 ABCParse-0.0.1/ABCParse.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)      198 2023-04-07 03:21:10.000000 ABCParse-0.0.1/ABCParse.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-07 03:21:10.000000 ABCParse-0.0.1/ABCParse.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (123)        9 2023-04-07 03:21:10.000000 ABCParse-0.0.1/ABCParse.egg-info/top_level.txt
--rw-r--r--   0 runner    (1001) docker     (123)    34523 2023-04-07 03:20:57.000000 ABCParse-0.0.1/LICENSE
--rw-r--r--   0 runner    (1001) docker     (123)      904 2023-04-07 03:21:10.382958 ABCParse-0.0.1/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)      408 2023-04-07 03:20:57.000000 ABCParse-0.0.1/README.md
--rw-r--r--   0 runner    (1001) docker     (123)       38 2023-04-07 03:21:10.382958 ABCParse-0.0.1/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (123)      746 2023-04-07 03:20:57.000000 ABCParse-0.0.1/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 03:23:59.615117 ABCParse-0.0.2/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 03:23:59.615117 ABCParse-0.0.2/ABCParse/
+-rw-r--r--   0 runner    (1001) docker     (123)       47 2023-04-07 03:23:48.000000 ABCParse-0.0.2/ABCParse/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2988 2023-04-07 03:23:48.000000 ABCParse-0.0.2/ABCParse/_abc_parse.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 03:23:59.615117 ABCParse-0.0.2/ABCParse.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)     1221 2023-04-07 03:23:59.000000 ABCParse-0.0.2/ABCParse.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)      198 2023-04-07 03:23:59.000000 ABCParse-0.0.2/ABCParse.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-07 03:23:59.000000 ABCParse-0.0.2/ABCParse.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        9 2023-04-07 03:23:59.000000 ABCParse-0.0.2/ABCParse.egg-info/top_level.txt
+-rw-r--r--   0 runner    (1001) docker     (123)    34523 2023-04-07 03:23:48.000000 ABCParse-0.0.2/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (123)     1221 2023-04-07 03:23:59.615117 ABCParse-0.0.2/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)      725 2023-04-07 03:23:48.000000 ABCParse-0.0.2/README.md
+-rw-r--r--   0 runner    (1001) docker     (123)       38 2023-04-07 03:23:59.615117 ABCParse-0.0.2/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (123)      746 2023-04-07 03:23:48.000000 ABCParse-0.0.2/setup.py
```

### Comparing `ABCParse-0.0.1/ABCParse/_abc_parse.py` & `ABCParse-0.0.2/ABCParse/_abc_parse.py`

 * *Files identical despite different names*

### Comparing `ABCParse-0.0.1/ABCParse.egg-info/PKG-INFO` & `ABCParse-0.0.2/ABCParse.egg-info/PKG-INFO`

 * *Files 20% similar despite different names*

```diff
@@ -1,25 +1,28 @@
 Metadata-Version: 2.1
 Name: ABCParse
-Version: 0.0.1
+Version: 0.0.2
 Summary: A better base class to automatically parse local args.
 Author: Michael E. Vinyard
 Author-email: mvinyard@broadinstitute.org
 License: MIT
 Classifier: Development Status :: 2 - Pre-Alpha
 Classifier: Programming Language :: Python :: 3.7
 Classifier: Intended Audience :: Science/Research
 Classifier: Topic :: Scientific/Engineering :: Bio-Informatics
 Requires-Python: >3.7.0
 Description-Content-Type: text/markdown
 License-File: LICENSE
 
 # ABCParse
 
-![Python Tests](https://github.com/mvinyard/AutoParser/actions/workflows/python-tests.yml/badge.svg)
+![Python Tests](https://github.com/mvinyard/ABCParse/actions/workflows/python-tests.yml/badge.svg)
+[![PyPI pyversions](https://img.shields.io/pypi/pyversions/ABCParse.svg)](https://pypi.python.org/pypi/ABCParse/)
+[![PyPI version](https://badge.fury.io/py/ABCParse.svg)](https://badge.fury.io/py/ABCParse)
+[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
 
 A better base class that handles parsing local arguments.
 
 ```bash
 pip install ABCParse
 ```
```

### Comparing `ABCParse-0.0.1/LICENSE` & `ABCParse-0.0.2/LICENSE`

 * *Files identical despite different names*

### Comparing `ABCParse-0.0.1/PKG-INFO` & `ABCParse-0.0.2/PKG-INFO`

 * *Files 20% similar despite different names*

```diff
@@ -1,25 +1,28 @@
 Metadata-Version: 2.1
 Name: ABCParse
-Version: 0.0.1
+Version: 0.0.2
 Summary: A better base class to automatically parse local args.
 Author: Michael E. Vinyard
 Author-email: mvinyard@broadinstitute.org
 License: MIT
 Classifier: Development Status :: 2 - Pre-Alpha
 Classifier: Programming Language :: Python :: 3.7
 Classifier: Intended Audience :: Science/Research
 Classifier: Topic :: Scientific/Engineering :: Bio-Informatics
 Requires-Python: >3.7.0
 Description-Content-Type: text/markdown
 License-File: LICENSE
 
 # ABCParse
 
-![Python Tests](https://github.com/mvinyard/AutoParser/actions/workflows/python-tests.yml/badge.svg)
+![Python Tests](https://github.com/mvinyard/ABCParse/actions/workflows/python-tests.yml/badge.svg)
+[![PyPI pyversions](https://img.shields.io/pypi/pyversions/ABCParse.svg)](https://pypi.python.org/pypi/ABCParse/)
+[![PyPI version](https://badge.fury.io/py/ABCParse.svg)](https://badge.fury.io/py/ABCParse)
+[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
 
 A better base class that handles parsing local arguments.
 
 ```bash
 pip install ABCParse
 ```
```

### Comparing `ABCParse-0.0.1/setup.py` & `ABCParse-0.0.2/setup.py`

 * *Files 1% similar despite different names*

```diff
@@ -3,15 +3,15 @@
 import re
 import os
 import sys
 
 
 setuptools.setup(
     name="ABCParse",
-    version="0.0.1",
+    version="0.0.2",
     python_requires=">3.7.0",
     author="Michael E. Vinyard",
     author_email="mvinyard@broadinstitute.org",
     url=None,
     long_description=open("README.md", encoding="utf-8").read(),
     long_description_content_type="text/markdown",
     description="A better base class to automatically parse local args.",
```

