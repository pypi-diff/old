# Comparing `tmp/flask_squeeze-3.0.4.tar.gz` & `tmp/flask_squeeze-3.0.5.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "flask_squeeze-3.0.4.tar", max compression
+gzip compressed data, was "flask_squeeze-3.0.5.tar", max compression
```

## Comparing `flask_squeeze-3.0.4.tar` & `flask_squeeze-3.0.5.tar`

### file list

```diff
@@ -1,10 +1,10 @@
--rw-r--r--   0        0        0     1061 2023-04-04 10:23:19.321417 flask_squeeze-3.0.4/LICENSE
--rw-r--r--   0        0        0     3535 2023-04-06 14:07:52.138505 flask_squeeze-3.0.4/README.md
--rw-r--r--   0        0        0       49 2023-04-04 12:50:40.490046 flask_squeeze-3.0.4/flask_squeeze/__init__.py
--rw-r--r--   0        0        0     1554 2023-04-04 12:57:27.961772 flask_squeeze-3.0.4/flask_squeeze/debug.py
--rw-r--r--   0        0        0     8443 2023-04-06 16:34:06.675548 flask_squeeze-3.0.4/flask_squeeze/flask_squeeze.py
--rw-r--r--   0        0        0     1760 2023-04-04 12:57:27.956281 flask_squeeze-3.0.4/flask_squeeze/log.py
--rw-r--r--   0        0        0     1482 2023-04-04 12:48:01.274755 flask_squeeze-3.0.4/flask_squeeze/minifiers.py
--rw-r--r--   0        0        0     1736 2023-04-06 16:03:45.531113 flask_squeeze-3.0.4/flask_squeeze/models.py
--rw-r--r--   0        0        0     1347 2023-04-06 16:34:46.201583 flask_squeeze-3.0.4/pyproject.toml
--rw-r--r--   0        0        0     4571 1970-01-01 00:00:00.000000 flask_squeeze-3.0.4/PKG-INFO
+-rw-r--r--   0        0        0     1061 2023-04-04 10:23:19.321417 flask_squeeze-3.0.5/LICENSE
+-rw-r--r--   0        0        0     3535 2023-04-06 14:07:52.138505 flask_squeeze-3.0.5/README.md
+-rw-r--r--   0        0        0       49 2023-04-04 12:50:40.490046 flask_squeeze-3.0.5/flask_squeeze/__init__.py
+-rw-r--r--   0        0        0     1554 2023-04-04 12:57:27.961772 flask_squeeze-3.0.5/flask_squeeze/debug.py
+-rw-r--r--   0        0        0     8412 2023-04-06 16:38:06.035825 flask_squeeze-3.0.5/flask_squeeze/flask_squeeze.py
+-rw-r--r--   0        0        0     1760 2023-04-04 12:57:27.956281 flask_squeeze-3.0.5/flask_squeeze/log.py
+-rw-r--r--   0        0        0     1482 2023-04-04 12:48:01.274755 flask_squeeze-3.0.5/flask_squeeze/minifiers.py
+-rw-r--r--   0        0        0     1736 2023-04-06 16:03:45.531113 flask_squeeze-3.0.5/flask_squeeze/models.py
+-rw-r--r--   0        0        0     1347 2023-04-06 16:38:25.677623 flask_squeeze-3.0.5/pyproject.toml
+-rw-r--r--   0        0        0     4571 1970-01-01 00:00:00.000000 flask_squeeze-3.0.5/PKG-INFO
```

### Comparing `flask_squeeze-3.0.4/LICENSE` & `flask_squeeze-3.0.5/LICENSE`

 * *Files identical despite different names*

### Comparing `flask_squeeze-3.0.4/README.md` & `flask_squeeze-3.0.5/README.md`

 * *Files identical despite different names*

### Comparing `flask_squeeze-3.0.4/flask_squeeze/debug.py` & `flask_squeeze-3.0.5/flask_squeeze/debug.py`

 * *Files identical despite different names*

### Comparing `flask_squeeze-3.0.4/flask_squeeze/flask_squeeze.py` & `flask_squeeze-3.0.5/flask_squeeze/flask_squeeze.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,18 +1,17 @@
 import gzip
 import random
 import secrets
 import time
 import zlib
-from typing import Union, Dict
+from typing import Dict, Union
 
 import brotli
 from flask import Flask, Response, request
 
-from .cache import MemoryCache
 from .debug import add_debug_header, ctx_add_debug_header
 from .log import d_log, log
 from .minifiers import minify_css, minify_html, minify_js
 from .models import (
 	Encoding,
 	Minifcation,
 	choose_encoding_from_headers_and_config,
```

### Comparing `flask_squeeze-3.0.4/flask_squeeze/log.py` & `flask_squeeze-3.0.5/flask_squeeze/log.py`

 * *Files identical despite different names*

### Comparing `flask_squeeze-3.0.4/flask_squeeze/minifiers.py` & `flask_squeeze-3.0.5/flask_squeeze/minifiers.py`

 * *Files identical despite different names*

### Comparing `flask_squeeze-3.0.4/flask_squeeze/models.py` & `flask_squeeze-3.0.5/flask_squeeze/models.py`

 * *Files identical despite different names*

### Comparing `flask_squeeze-3.0.4/pyproject.toml` & `flask_squeeze-3.0.5/pyproject.toml`

 * *Files 7% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 [tool.poetry]
 name = "flask-squeeze"
-version = "3.0.4"
+version = "3.0.5"
 repository = "https://github.com/mkrd/Flask-Squeeze"
 description = "Compress and minify Flask responses!"
 readme = "README.md"
 authors = ["Marcel Kröker <kroeker.marcel@gmail.com>"]
 license = "MIT"
 classifiers=[
 	"Programming Language :: Python :: 3",
```

### Comparing `flask_squeeze-3.0.4/PKG-INFO` & `flask_squeeze-3.0.5/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: flask-squeeze
-Version: 3.0.4
+Version: 3.0.5
 Summary: Compress and minify Flask responses!
 Home-page: https://github.com/mkrd/Flask-Squeeze
 License: MIT
 Author: Marcel Kröker
 Author-email: kroeker.marcel@gmail.com
 Requires-Python: >=3.8,<4.0
 Classifier: Intended Audience :: Developers
```

