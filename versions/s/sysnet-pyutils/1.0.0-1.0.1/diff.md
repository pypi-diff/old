# Comparing `tmp/sysnet-pyutils-1.0.0.tar.gz` & `tmp/sysnet-pyutils-1.0.1.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "sysnet-pyutils-1.0.0.tar", last modified: Thu Apr  6 10:29:43 2023, max compression
+gzip compressed data, was "sysnet-pyutils-1.0.1.tar", last modified: Thu Apr  6 10:53:22 2023, max compression
```

## Comparing `sysnet-pyutils-1.0.0.tar` & `sysnet-pyutils-1.0.1.tar`

### file list

```diff
@@ -1,18 +1,18 @@
-drwxrwxrwx   0        0        0        0 2023-04-06 10:29:43.799494 sysnet-pyutils-1.0.0/
--rw-rw-rw-   0        0        0    35184 2023-03-27 14:59:40.000000 sysnet-pyutils-1.0.0/LICENSE
--rw-rw-rw-   0        0        0     5807 2023-04-06 10:29:43.799494 sysnet-pyutils-1.0.0/PKG-INFO
--rw-rw-rw-   0        0        0     5185 2023-04-06 10:22:58.000000 sysnet-pyutils-1.0.0/README.md
--rw-rw-rw-   0        0        0      862 2023-04-06 10:26:51.000000 sysnet-pyutils-1.0.0/pyproject.toml
--rw-rw-rw-   0        0        0       47 2023-03-27 16:22:12.000000 sysnet-pyutils-1.0.0/requirements.txt
--rw-rw-rw-   0        0        0       42 2023-04-06 10:29:43.799494 sysnet-pyutils-1.0.0/setup.cfg
-drwxrwxrwx   0        0        0        0 2023-04-06 10:29:43.790486 sysnet-pyutils-1.0.0/sysnet_pyutils/
--rw-rw-rw-   0        0        0        0 2023-03-27 15:02:04.000000 sysnet-pyutils-1.0.0/sysnet_pyutils/__init__.py
--rw-rw-rw-   0        0        0     2622 2023-04-06 08:45:17.000000 sysnet-pyutils-1.0.0/sysnet_pyutils/barcode.py
--rw-rw-rw-   0        0        0     2737 2023-04-06 08:45:17.000000 sysnet-pyutils-1.0.0/sysnet_pyutils/ident.py
--rw-rw-rw-   0        0        0     8632 2023-04-06 10:28:59.000000 sysnet-pyutils-1.0.0/sysnet_pyutils/utils.py
-drwxrwxrwx   0        0        0        0 2023-04-06 10:29:43.799494 sysnet-pyutils-1.0.0/sysnet_pyutils.egg-info/
--rw-rw-rw-   0        0        0     5807 2023-04-06 10:29:43.000000 sysnet-pyutils-1.0.0/sysnet_pyutils.egg-info/PKG-INFO
--rw-rw-rw-   0        0        0      339 2023-04-06 10:29:43.000000 sysnet-pyutils-1.0.0/sysnet_pyutils.egg-info/SOURCES.txt
--rw-rw-rw-   0        0        0        1 2023-04-06 10:29:43.000000 sysnet-pyutils-1.0.0/sysnet_pyutils.egg-info/dependency_links.txt
--rw-rw-rw-   0        0        0       48 2023-04-06 10:29:43.000000 sysnet-pyutils-1.0.0/sysnet_pyutils.egg-info/requires.txt
--rw-rw-rw-   0        0        0       15 2023-04-06 10:29:43.000000 sysnet-pyutils-1.0.0/sysnet_pyutils.egg-info/top_level.txt
+drwxrwxrwx   0        0        0        0 2023-04-06 10:53:22.880650 sysnet-pyutils-1.0.1/
+-rw-rw-rw-   0        0        0    35184 2023-03-27 14:59:40.000000 sysnet-pyutils-1.0.1/LICENSE
+-rw-rw-rw-   0        0        0     5807 2023-04-06 10:53:22.879649 sysnet-pyutils-1.0.1/PKG-INFO
+-rw-rw-rw-   0        0        0     5185 2023-04-06 10:22:58.000000 sysnet-pyutils-1.0.1/README.md
+-rw-rw-rw-   0        0        0      862 2023-04-06 10:52:47.000000 sysnet-pyutils-1.0.1/pyproject.toml
+-rw-rw-rw-   0        0        0       47 2023-03-27 16:22:12.000000 sysnet-pyutils-1.0.1/requirements.txt
+-rw-rw-rw-   0        0        0       42 2023-04-06 10:53:22.880650 sysnet-pyutils-1.0.1/setup.cfg
+drwxrwxrwx   0        0        0        0 2023-04-06 10:53:22.869652 sysnet-pyutils-1.0.1/sysnet_pyutils/
+-rw-rw-rw-   0        0        0        0 2023-03-27 15:02:04.000000 sysnet-pyutils-1.0.1/sysnet_pyutils/__init__.py
+-rw-rw-rw-   0        0        0     2622 2023-04-06 08:45:17.000000 sysnet-pyutils-1.0.1/sysnet_pyutils/barcode.py
+-rw-rw-rw-   0        0        0     2763 2023-04-06 10:52:47.000000 sysnet-pyutils-1.0.1/sysnet_pyutils/ident.py
+-rw-rw-rw-   0        0        0     8620 2023-04-06 10:52:47.000000 sysnet-pyutils-1.0.1/sysnet_pyutils/utils.py
+drwxrwxrwx   0        0        0        0 2023-04-06 10:53:22.878651 sysnet-pyutils-1.0.1/sysnet_pyutils.egg-info/
+-rw-rw-rw-   0        0        0     5807 2023-04-06 10:53:22.000000 sysnet-pyutils-1.0.1/sysnet_pyutils.egg-info/PKG-INFO
+-rw-rw-rw-   0        0        0      339 2023-04-06 10:53:22.000000 sysnet-pyutils-1.0.1/sysnet_pyutils.egg-info/SOURCES.txt
+-rw-rw-rw-   0        0        0        1 2023-04-06 10:53:22.000000 sysnet-pyutils-1.0.1/sysnet_pyutils.egg-info/dependency_links.txt
+-rw-rw-rw-   0        0        0       48 2023-04-06 10:53:22.000000 sysnet-pyutils-1.0.1/sysnet_pyutils.egg-info/requires.txt
+-rw-rw-rw-   0        0        0       15 2023-04-06 10:53:22.000000 sysnet-pyutils-1.0.1/sysnet_pyutils.egg-info/top_level.txt
```

### Comparing `sysnet-pyutils-1.0.0/LICENSE` & `sysnet-pyutils-1.0.1/LICENSE`

 * *Files identical despite different names*

### Comparing `sysnet-pyutils-1.0.0/PKG-INFO` & `sysnet-pyutils-1.0.1/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: sysnet-pyutils
-Version: 1.0.0
+Version: 1.0.1
 Summary: Python Utilities
 Author-email: Data Developer <info@sysnet.cz>
 Project-URL: Homepage, https://github.com/SYSNET-CZ/pyutils
 Classifier: Development Status :: 5 - Production/Stable
 Classifier: Programming Language :: Python :: 3
 Classifier: Intended Audience :: Developers
 Classifier: License :: Free For Home Use
```

### Comparing `sysnet-pyutils-1.0.0/README.md` & `sysnet-pyutils-1.0.1/README.md`

 * *Files identical despite different names*

### Comparing `sysnet-pyutils-1.0.0/pyproject.toml` & `sysnet-pyutils-1.0.1/pyproject.toml`

 * *Files 0% similar despite different names*

```diff
@@ -1,14 +1,14 @@
 [build-system]
 requires = ["setuptools>=61.0"]
 build-backend = "setuptools.build_meta"
 
 [project]
 name = "sysnet-pyutils"
-version = "1.0.0"
+version = "1.0.1"
 authors = [
   { name="Data Developer", email="info@sysnet.cz" },
 ]
 description = "Python Utilities"
 readme = "README.md"
 license = { file="LICENSE.md" }
 requires-python = ">=3.9"
```

### Comparing `sysnet-pyutils-1.0.0/sysnet_pyutils/barcode.py` & `sysnet-pyutils-1.0.1/sysnet_pyutils/barcode.py`

 * *Files identical despite different names*

### Comparing `sysnet-pyutils-1.0.0/sysnet_pyutils/ident.py` & `sysnet-pyutils-1.0.1/sysnet_pyutils/ident.py`

 * *Files 0% similar despite different names*

```diff
@@ -6,15 +6,15 @@
 # Author:       Radim Jager
 # Copyright:    (c) SYSNET s.r.o. 2019
 # License:      CC BY-SA 4.0
 # -------------------------------------------------------------------------------
 import os
 import uuid
 
-import barcode
+import sysnet_pyutils.barcode as barcode
 
 PID_PREFIX = os.getenv('PID_PREFIX', 'SNT')
 ID_LENGTH = 12
 
 DIGITS36 = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
             'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
             'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
```

### Comparing `sysnet-pyutils-1.0.0/sysnet_pyutils/utils.py` & `sysnet-pyutils-1.0.1/sysnet_pyutils/utils.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,22 +1,21 @@
 import logging
 import os
 import secrets
 import sys
 import traceback
 import uuid
 from datetime import datetime, timedelta
-# from pathlib import Path
 from urllib.parse import quote
 
 import dateutil.parser
 import pytz
 import yaml
 
-from ident import generate_pid, check_pid, correct_pid, generate_id12
+from sysnet_pyutils.ident import generate_pid, check_pid, correct_pid, generate_id12
 
 TZ = os.getenv('TZ', 'Europe/Prague')
 DEBUG = os.getenv("DEBUG", 'True').lower() in ('true', '1', 't')
 LOG_FORMAT = os.getenv('LOG_FORMAT', '%(asctime)s - %(levelname)s in %(module)s: %(message)s')
 LOG_DATE_FORMAT = os.getenv('LOG_DATE_FORMAT', '%d.%m.%Y %H:%M:%S')
```

### Comparing `sysnet-pyutils-1.0.0/sysnet_pyutils.egg-info/PKG-INFO` & `sysnet-pyutils-1.0.1/sysnet_pyutils.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: sysnet-pyutils
-Version: 1.0.0
+Version: 1.0.1
 Summary: Python Utilities
 Author-email: Data Developer <info@sysnet.cz>
 Project-URL: Homepage, https://github.com/SYSNET-CZ/pyutils
 Classifier: Development Status :: 5 - Production/Stable
 Classifier: Programming Language :: Python :: 3
 Classifier: Intended Audience :: Developers
 Classifier: License :: Free For Home Use
```

