# Comparing `tmp/flask_squeeze-3.0.2.tar.gz` & `tmp/flask_squeeze-3.0.3.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "flask_squeeze-3.0.2.tar", max compression
+gzip compressed data, was "flask_squeeze-3.0.3.tar", max compression
```

## Comparing `flask_squeeze-3.0.2.tar` & `flask_squeeze-3.0.3.tar`

### file list

```diff
@@ -1,11 +1,10 @@
--rw-r--r--   0        0        0     1061 2023-04-04 10:23:19.321417 flask_squeeze-3.0.2/LICENSE
--rw-r--r--   0        0        0     3535 2023-04-06 14:07:52.138505 flask_squeeze-3.0.2/README.md
--rw-r--r--   0        0        0       49 2023-04-04 12:50:40.490046 flask_squeeze-3.0.2/flask_squeeze/__init__.py
--rw-r--r--   0        0        0      963 2023-04-06 15:59:46.565069 flask_squeeze-3.0.2/flask_squeeze/cache.py
--rw-r--r--   0        0        0     1554 2023-04-04 12:57:27.961772 flask_squeeze-3.0.2/flask_squeeze/debug.py
--rw-r--r--   0        0        0     8267 2023-04-06 16:00:46.247713 flask_squeeze-3.0.2/flask_squeeze/flask_squeeze.py
--rw-r--r--   0        0        0     1760 2023-04-04 12:57:27.956281 flask_squeeze-3.0.2/flask_squeeze/log.py
--rw-r--r--   0        0        0     1482 2023-04-04 12:48:01.274755 flask_squeeze-3.0.2/flask_squeeze/minifiers.py
--rw-r--r--   0        0        0     1736 2023-04-06 16:03:45.531113 flask_squeeze-3.0.2/flask_squeeze/models.py
--rw-r--r--   0        0        0     1347 2023-04-06 16:04:00.992160 flask_squeeze-3.0.2/pyproject.toml
--rw-r--r--   0        0        0     4571 1970-01-01 00:00:00.000000 flask_squeeze-3.0.2/PKG-INFO
+-rw-r--r--   0        0        0     1061 2023-04-04 10:23:19.321417 flask_squeeze-3.0.3/LICENSE
+-rw-r--r--   0        0        0     3535 2023-04-06 14:07:52.138505 flask_squeeze-3.0.3/README.md
+-rw-r--r--   0        0        0       49 2023-04-04 12:50:40.490046 flask_squeeze-3.0.3/flask_squeeze/__init__.py
+-rw-r--r--   0        0        0     1554 2023-04-04 12:57:27.961772 flask_squeeze-3.0.3/flask_squeeze/debug.py
+-rw-r--r--   0        0        0     8143 2023-04-06 16:31:34.626198 flask_squeeze-3.0.3/flask_squeeze/flask_squeeze.py
+-rw-r--r--   0        0        0     1760 2023-04-04 12:57:27.956281 flask_squeeze-3.0.3/flask_squeeze/log.py
+-rw-r--r--   0        0        0     1482 2023-04-04 12:48:01.274755 flask_squeeze-3.0.3/flask_squeeze/minifiers.py
+-rw-r--r--   0        0        0     1736 2023-04-06 16:03:45.531113 flask_squeeze-3.0.3/flask_squeeze/models.py
+-rw-r--r--   0        0        0     1347 2023-04-06 16:32:15.265539 flask_squeeze-3.0.3/pyproject.toml
+-rw-r--r--   0        0        0     4571 1970-01-01 00:00:00.000000 flask_squeeze-3.0.3/PKG-INFO
```

### Comparing `flask_squeeze-3.0.2/LICENSE` & `flask_squeeze-3.0.3/LICENSE`

 * *Files identical despite different names*

### Comparing `flask_squeeze-3.0.2/README.md` & `flask_squeeze-3.0.3/README.md`

 * *Files identical despite different names*

### Comparing `flask_squeeze-3.0.2/flask_squeeze/debug.py` & `flask_squeeze-3.0.3/flask_squeeze/debug.py`

 * *Files identical despite different names*

### Comparing `flask_squeeze-3.0.2/flask_squeeze/flask_squeeze.py` & `flask_squeeze-3.0.3/flask_squeeze/flask_squeeze.py`

 * *Files 6% similar despite different names*

```diff
@@ -1,13 +1,13 @@
 import gzip
 import random
 import secrets
 import time
 import zlib
-from typing import Union
+from typing import Union, Dict
 
 import brotli
 from flask import Flask, Response, request
 
 from .cache import MemoryCache
 from .debug import add_debug_header, ctx_add_debug_header
 from .log import d_log, log
@@ -19,24 +19,24 @@
 	choose_minification_from_mimetype_and_config,
 )
 
 
 class Squeeze:
 
 	__slots__ = "cache", "app", "encode_choice", "minify_choice", "resource_type"
-	cache: MemoryCache
+	cache: Dict[str, bytes]
 	app: Flask
 	encode_choice: Union[Encoding, None]
 	minify_choice: Union[Minifcation, None]
 	resource_type: Union[str, None]
 
 
 	def __init__(self, app: Flask = None) -> None:
 		""" Initialize Flask-Squeeze with or without app. """
-		self.cache = MemoryCache()
+		self.cache = {}
 		self.app = app
 		if app is not None:
 			self.init_app(app)
 
 
 	def init_app(self, app: Flask) -> None:
 		""" Initialize Flask-Squeeze with app """
@@ -164,35 +164,34 @@
 		self,
 		response: Response,
 	) -> None:
 		"""
 			Compress a static resource.
 		"""
 
-		path = request.path
-		from_cache = self.cache.get(path, self.encode_choice, self.minify_choice)
+
+		# Serve from cache if possible
+		from_cache = self.cache.get(request.path, None)
 		if from_cache is not None:
 			log(2, "Found in cache. RETURN")
 			response.direct_passthrough = False
 			response.set_data(from_cache)
 			response.headers["X-Flask-Squeeze-Cache"] = "HIT"
 			return
 
 		# Assert: not in cache
 
 		if self.minify_choice is not None:
 			self.execute_minify(response)
 		if self.encode_choice is not None:
 			self.execute_compress(response)
 
-		# If compression or minification was done, insert into cache
-		if self.encode_choice or self.minify_choice:
-			response.headers["X-Flask-Squeeze-Cache"] = "MISS"
-			data = response.get_data(as_text=False)
-			self.cache.insert(path, self.encode_choice, self.minify_choice, data)
+		# Assert: At least one of minify or compress was run
+		response.headers["X-Flask-Squeeze-Cache"] = "MISS"
+		self.cache[request.path] = response.get_data(as_text=False)
 
 
 
 	@d_log(level=1, with_args=[1, 2])
 	def recompute_headers(
 		self,
 		response: Response,
```

### Comparing `flask_squeeze-3.0.2/flask_squeeze/log.py` & `flask_squeeze-3.0.3/flask_squeeze/log.py`

 * *Files identical despite different names*

### Comparing `flask_squeeze-3.0.2/flask_squeeze/minifiers.py` & `flask_squeeze-3.0.3/flask_squeeze/minifiers.py`

 * *Files identical despite different names*

### Comparing `flask_squeeze-3.0.2/flask_squeeze/models.py` & `flask_squeeze-3.0.3/flask_squeeze/models.py`

 * *Files identical despite different names*

### Comparing `flask_squeeze-3.0.2/pyproject.toml` & `flask_squeeze-3.0.3/pyproject.toml`

 * *Files 8% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 [tool.poetry]
 name = "flask-squeeze"
-version = "3.0.2"
+version = "3.0.3"
 repository = "https://github.com/mkrd/Flask-Squeeze"
 description = "Compress and minify Flask responses!"
 readme = "README.md"
 authors = ["Marcel Kröker <kroeker.marcel@gmail.com>"]
 license = "MIT"
 classifiers=[
 	"Programming Language :: Python :: 3",
```

### Comparing `flask_squeeze-3.0.2/PKG-INFO` & `flask_squeeze-3.0.3/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: flask-squeeze
-Version: 3.0.2
+Version: 3.0.3
 Summary: Compress and minify Flask responses!
 Home-page: https://github.com/mkrd/Flask-Squeeze
 License: MIT
 Author: Marcel Kröker
 Author-email: kroeker.marcel@gmail.com
 Requires-Python: >=3.8,<4.0
 Classifier: Intended Audience :: Developers
```

