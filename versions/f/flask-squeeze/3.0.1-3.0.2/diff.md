# Comparing `tmp/flask_squeeze-3.0.1.tar.gz` & `tmp/flask_squeeze-3.0.2.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "flask_squeeze-3.0.1.tar", max compression
+gzip compressed data, was "flask_squeeze-3.0.2.tar", max compression
```

## Comparing `flask_squeeze-3.0.1.tar` & `flask_squeeze-3.0.2.tar`

### file list

```diff
@@ -1,11 +1,11 @@
--rw-r--r--   0        0        0     1061 2023-04-04 10:23:19.321417 flask_squeeze-3.0.1/LICENSE
--rw-r--r--   0        0        0     3535 2023-04-06 14:07:52.138505 flask_squeeze-3.0.1/README.md
--rw-r--r--   0        0        0       49 2023-04-04 12:50:40.490046 flask_squeeze-3.0.1/flask_squeeze/__init__.py
--rw-r--r--   0        0        0      879 2023-04-06 14:07:52.143754 flask_squeeze-3.0.1/flask_squeeze/cache.py
--rw-r--r--   0        0        0     1554 2023-04-04 12:57:27.961772 flask_squeeze-3.0.1/flask_squeeze/debug.py
--rw-r--r--   0        0        0     8267 2023-04-06 14:31:05.060736 flask_squeeze-3.0.1/flask_squeeze/flask_squeeze.py
--rw-r--r--   0        0        0     1760 2023-04-04 12:57:27.956281 flask_squeeze-3.0.1/flask_squeeze/log.py
--rw-r--r--   0        0        0     1482 2023-04-04 12:48:01.274755 flask_squeeze-3.0.1/flask_squeeze/minifiers.py
--rw-r--r--   0        0        0     1652 2023-04-06 14:27:12.250458 flask_squeeze-3.0.1/flask_squeeze/models.py
--rw-r--r--   0        0        0     1347 2023-04-06 14:32:31.191824 flask_squeeze-3.0.1/pyproject.toml
--rw-r--r--   0        0        0     4571 1970-01-01 00:00:00.000000 flask_squeeze-3.0.1/PKG-INFO
+-rw-r--r--   0        0        0     1061 2023-04-04 10:23:19.321417 flask_squeeze-3.0.2/LICENSE
+-rw-r--r--   0        0        0     3535 2023-04-06 14:07:52.138505 flask_squeeze-3.0.2/README.md
+-rw-r--r--   0        0        0       49 2023-04-04 12:50:40.490046 flask_squeeze-3.0.2/flask_squeeze/__init__.py
+-rw-r--r--   0        0        0      963 2023-04-06 15:59:46.565069 flask_squeeze-3.0.2/flask_squeeze/cache.py
+-rw-r--r--   0        0        0     1554 2023-04-04 12:57:27.961772 flask_squeeze-3.0.2/flask_squeeze/debug.py
+-rw-r--r--   0        0        0     8267 2023-04-06 16:00:46.247713 flask_squeeze-3.0.2/flask_squeeze/flask_squeeze.py
+-rw-r--r--   0        0        0     1760 2023-04-04 12:57:27.956281 flask_squeeze-3.0.2/flask_squeeze/log.py
+-rw-r--r--   0        0        0     1482 2023-04-04 12:48:01.274755 flask_squeeze-3.0.2/flask_squeeze/minifiers.py
+-rw-r--r--   0        0        0     1736 2023-04-06 16:03:45.531113 flask_squeeze-3.0.2/flask_squeeze/models.py
+-rw-r--r--   0        0        0     1347 2023-04-06 16:04:00.992160 flask_squeeze-3.0.2/pyproject.toml
+-rw-r--r--   0        0        0     4571 1970-01-01 00:00:00.000000 flask_squeeze-3.0.2/PKG-INFO
```

### Comparing `flask_squeeze-3.0.1/LICENSE` & `flask_squeeze-3.0.2/LICENSE`

 * *Files identical despite different names*

### Comparing `flask_squeeze-3.0.1/README.md` & `flask_squeeze-3.0.2/README.md`

 * *Files identical despite different names*

### Comparing `flask_squeeze-3.0.1/flask_squeeze/debug.py` & `flask_squeeze-3.0.2/flask_squeeze/debug.py`

 * *Files identical despite different names*

### Comparing `flask_squeeze-3.0.1/flask_squeeze/flask_squeeze.py` & `flask_squeeze-3.0.2/flask_squeeze/flask_squeeze.py`

 * *Files identical despite different names*

### Comparing `flask_squeeze-3.0.1/flask_squeeze/log.py` & `flask_squeeze-3.0.2/flask_squeeze/log.py`

 * *Files identical despite different names*

### Comparing `flask_squeeze-3.0.1/flask_squeeze/minifiers.py` & `flask_squeeze-3.0.2/flask_squeeze/minifiers.py`

 * *Files identical despite different names*

### Comparing `flask_squeeze-3.0.1/flask_squeeze/models.py` & `flask_squeeze-3.0.2/flask_squeeze/models.py`

 * *Files 13% similar despite different names*

```diff
@@ -19,15 +19,15 @@
 	config: Config,
 ) -> Union[Encoding, None]:
 	"""
 		If the client supports brotli, gzip, or deflate, return the best encoding.
 		If the client does not accept any of these encodings, or if the config
 		variable SQUEEZE_COMPRESS is False, return None.
 	"""
-	if not config["SQUEEZE_COMPRESS"]:
+	if not config.get("SQUEEZE_COMPRESS") or headers is None:
 		return None
 	encoding = headers.get("Accept-Encoding", "").lower()
 	if "br" in encoding:
 		return Encoding.br
 	if "deflate" in encoding:
 		return Encoding.deflate
 	if "gzip" in encoding:
@@ -38,25 +38,27 @@
 class Minifcation(Enum):
 	js = "js"
 	css = "css"
 	html = "html"
 
 
 def choose_minification_from_mimetype_and_config(
-	mimetype: str,
+	mimetype: Union[str, None],
 	config: Config,
 ) -> Union[Minifcation, None]:
 	"""
 		Based on the response mimetype:
 		- `js` or `json`, and `SQUEEZE_MINIFY_JS=True`: return `Minifcation.js`
 		- `css` and `SQUEEZE_MINIFY_CSS=True`: return `Minifcation.css`
 		-  `html` and `SQUEEZE_MINIFY_HTML=True`: return `Minifcation.html`
 		- Otherwise, return `None`
 	"""
+	if mimetype is None:
+		return None
 	is_js_or_json = mimetype.endswith("javascript") or mimetype.endswith("json")
-	if is_js_or_json and config["SQUEEZE_MINIFY_JS"]:
+	if is_js_or_json and config.get("SQUEEZE_MINIFY_JS"):
 		return Minifcation.js
-	if mimetype.endswith("css") and config["SQUEEZE_MINIFY_CSS"]:
+	if mimetype.endswith("css") and config.get("SQUEEZE_MINIFY_CSS"):
 		return Minifcation.css
-	if mimetype.endswith("html") and config["SQUEEZE_MINIFY_HTML"]:
+	if mimetype.endswith("html") and config.get("SQUEEZE_MINIFY_HTML"):
 		return Minifcation.html
 	return None
```

### Comparing `flask_squeeze-3.0.1/pyproject.toml` & `flask_squeeze-3.0.2/pyproject.toml`

 * *Files 8% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 [tool.poetry]
 name = "flask-squeeze"
-version = "3.0.1"
+version = "3.0.2"
 repository = "https://github.com/mkrd/Flask-Squeeze"
 description = "Compress and minify Flask responses!"
 readme = "README.md"
 authors = ["Marcel Kröker <kroeker.marcel@gmail.com>"]
 license = "MIT"
 classifiers=[
 	"Programming Language :: Python :: 3",
```

### Comparing `flask_squeeze-3.0.1/PKG-INFO` & `flask_squeeze-3.0.2/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: flask-squeeze
-Version: 3.0.1
+Version: 3.0.2
 Summary: Compress and minify Flask responses!
 Home-page: https://github.com/mkrd/Flask-Squeeze
 License: MIT
 Author: Marcel Kröker
 Author-email: kroeker.marcel@gmail.com
 Requires-Python: >=3.8,<4.0
 Classifier: Intended Audience :: Developers
```

