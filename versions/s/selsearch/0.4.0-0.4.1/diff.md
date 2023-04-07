# Comparing `tmp/selsearch-0.4.0.tar.gz` & `tmp/selsearch-0.4.1.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "selsearch-0.4.0.tar", max compression
+gzip compressed data, was "selsearch-0.4.1.tar", max compression
```

## Comparing `selsearch-0.4.0.tar` & `selsearch-0.4.1.tar`

### file list

```diff
@@ -1,11 +1,11 @@
--rw-r--r--   0        0        0     1067 2023-04-03 11:08:43.746305 selsearch-0.4.0/LICENSE.md
--rw-r--r--   0        0        0     3771 2023-04-03 11:08:43.746305 selsearch-0.4.0/README.md
--rw-r--r--   0        0        0      993 2023-04-03 11:08:43.746305 selsearch-0.4.0/pyproject.toml
--rw-r--r--   0        0        0       22 2023-04-03 11:08:43.746305 selsearch-0.4.0/selsearch/__init__.py
--rw-r--r--   0        0        0     1435 2023-04-03 11:08:43.746305 selsearch-0.4.0/selsearch/__main__.py
--rw-r--r--   0        0        0     3370 2023-04-03 11:08:43.746305 selsearch-0.4.0/selsearch/config.py
--rw-r--r--   0        0        0     1125 2023-04-03 11:08:43.746305 selsearch-0.4.0/selsearch/keys.py
--rw-r--r--   0        0        0     1305 2023-04-03 11:08:43.746305 selsearch-0.4.0/selsearch/run.py
--rw-r--r--   0        0        0      400 2023-04-03 11:08:43.746305 selsearch-0.4.0/selsearch/search.py
--rw-r--r--   0        0        0     1196 2023-04-03 11:08:43.746305 selsearch-0.4.0/selsearch/selection.py
--rw-r--r--   0        0        0     4708 1970-01-01 00:00:00.000000 selsearch-0.4.0/PKG-INFO
+-rw-r--r--   0        0        0     1067 2023-04-07 09:38:40.524398 selsearch-0.4.1/LICENSE.md
+-rw-r--r--   0        0        0     3771 2023-04-07 09:38:40.524398 selsearch-0.4.1/README.md
+-rw-r--r--   0        0        0      993 2023-04-07 09:38:40.524398 selsearch-0.4.1/pyproject.toml
+-rw-r--r--   0        0        0       22 2023-04-07 09:38:40.524398 selsearch-0.4.1/selsearch/__init__.py
+-rw-r--r--   0        0        0     1435 2023-04-07 09:38:40.524398 selsearch-0.4.1/selsearch/__main__.py
+-rw-r--r--   0        0        0     3370 2023-04-07 09:38:40.524398 selsearch-0.4.1/selsearch/config.py
+-rw-r--r--   0        0        0     1125 2023-04-07 09:38:40.524398 selsearch-0.4.1/selsearch/keys.py
+-rw-r--r--   0        0        0     1305 2023-04-07 09:38:40.524398 selsearch-0.4.1/selsearch/run.py
+-rw-r--r--   0        0        0      400 2023-04-07 09:38:40.524398 selsearch-0.4.1/selsearch/search.py
+-rw-r--r--   0        0        0     1196 2023-04-07 09:38:40.524398 selsearch-0.4.1/selsearch/selection.py
+-rw-r--r--   0        0        0     4708 1970-01-01 00:00:00.000000 selsearch-0.4.1/PKG-INFO
```

### Comparing `selsearch-0.4.0/LICENSE.md` & `selsearch-0.4.1/LICENSE.md`

 * *Files identical despite different names*

### Comparing `selsearch-0.4.0/README.md` & `selsearch-0.4.1/README.md`

 * *Files identical despite different names*

### Comparing `selsearch-0.4.0/pyproject.toml` & `selsearch-0.4.1/pyproject.toml`

 * *Files 1% similar despite different names*

```diff
@@ -23,15 +23,15 @@
 license = "MIT"
 name = "selsearch"
 packages = [
   {include = "selsearch"}
 ]
 readme = "README.md"
 repository = "https://github.com/jeertmans/selsearch"
-version = "0.4.0"
+version = "0.4.1"
 
 [tool.poetry.dependencies]
 appdirs = "^1.4.4"
 click = "^8.1.3"
 pydantic = "^1.10.7"
 pynput = "^1.7.6"
 pyperclip = "^1.8.2"
```

### Comparing `selsearch-0.4.0/selsearch/__main__.py` & `selsearch-0.4.1/selsearch/__main__.py`

 * *Files identical despite different names*

### Comparing `selsearch-0.4.0/selsearch/config.py` & `selsearch-0.4.1/selsearch/config.py`

 * *Files identical despite different names*

### Comparing `selsearch-0.4.0/selsearch/keys.py` & `selsearch-0.4.1/selsearch/keys.py`

 * *Files identical despite different names*

### Comparing `selsearch-0.4.0/selsearch/run.py` & `selsearch-0.4.1/selsearch/run.py`

 * *Files identical despite different names*

### Comparing `selsearch-0.4.0/selsearch/selection.py` & `selsearch-0.4.1/selsearch/selection.py`

 * *Files identical despite different names*

### Comparing `selsearch-0.4.0/PKG-INFO` & `selsearch-0.4.1/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: selsearch
-Version: 0.4.0
+Version: 0.4.1
 Summary: Internet search based on selected text
 Home-page: https://github.com/jeertmans/selsearch
 License: MIT
 Keywords: manim,slides,plugin,manimgl
 Author: Jérome Eertmans
 Author-email: jeertmans@icloud.com
 Requires-Python: >=3.8,<4.0
```

