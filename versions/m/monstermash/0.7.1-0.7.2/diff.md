# Comparing `tmp/monstermash-0.7.1.tar.gz` & `tmp/monstermash-0.7.2.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "monstermash-0.7.1.tar", max compression
+gzip compressed data, was "monstermash-0.7.2.tar", max compression
```

## Comparing `monstermash-0.7.1.tar` & `monstermash-0.7.2.tar`

### file list

```diff
@@ -1,6 +1,6 @@
--rw-r--r--   0        0        0     1366 2023-03-30 09:25:51.419567 monstermash-0.7.1/README.md
--rw-r--r--   0        0        0     1041 2023-03-30 09:25:51.423567 monstermash-0.7.1/pyproject.toml
--rw-r--r--   0        0        0       86 2023-03-30 09:25:51.423567 monstermash-0.7.1/src/monstermash/__init__.py
--rw-r--r--   0        0        0     1968 2023-03-30 09:25:51.423567 monstermash-0.7.1/src/monstermash/__main__.py
--rw-r--r--   0        0        0     1530 2023-03-30 09:25:51.423567 monstermash-0.7.1/src/monstermash/crypt.py
--rw-r--r--   0        0        0     1926 1970-01-01 00:00:00.000000 monstermash-0.7.1/PKG-INFO
+-rw-r--r--   0        0        0     1366 2023-04-06 10:44:23.532484 monstermash-0.7.2/README.md
+-rw-r--r--   0        0        0     1046 2023-04-06 10:44:23.532484 monstermash-0.7.2/pyproject.toml
+-rw-r--r--   0        0        0       86 2023-04-06 10:44:23.532484 monstermash-0.7.2/src/monstermash/__init__.py
+-rw-r--r--   0        0        0     1968 2023-04-06 10:44:23.532484 monstermash-0.7.2/src/monstermash/__main__.py
+-rw-r--r--   0        0        0     1530 2023-04-06 10:44:23.536484 monstermash-0.7.2/src/monstermash/crypt.py
+-rw-r--r--   0        0        0     1926 1970-01-01 00:00:00.000000 monstermash-0.7.2/PKG-INFO
```

### Comparing `monstermash-0.7.1/README.md` & `monstermash-0.7.2/README.md`

 * *Files 6% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 ##  🧟 Monstermash
 
-> 1️⃣ version: 0.7.1
+> 1️⃣ version: 0.7.2
 
 > ✍️ author: Mitchell Lisle
 
 ## Install
 Install from PyPi
 
 ```shell
```

### Comparing `monstermash-0.7.1/pyproject.toml` & `monstermash-0.7.2/pyproject.toml`

 * *Files 11% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 [tool.poetry]
 name = "monstermash"
-version = "0.7.1"
+version = "0.7.2"
 description = ""
 authors = ["Mitchell Lisle <m.lisle90@gmail.com>"]
 readme = "README.md"
 packages = [{include = "monstermash", from = "src"}]
 
 [tool.poetry.dependencies]
 python = "^3.8.1"
@@ -27,15 +27,15 @@
 
 
 [tool.poetry.group.docs.dependencies]
 mkdocs = "^1.4.2"
 mkdocs-material = "^9.1.4"
 mkdocs-gen-files = "^0.4.0"
 mkdocs-literate-nav = "^0.6.0"
-mkdocstrings = {extras = ["python"], version = "^0.20.0"}
+mkdocstrings = {extras = ["python"], version = ">=0.20,<0.22"}
 mkautodoc = "^0.2.0"
 
 
 [tool.poetry.group.test.dependencies]
 pytest = "^7.2.2"
 pytest-dotenv = "^0.5.2"
 pytest-cov = "^4.0.0"
```

### Comparing `monstermash-0.7.1/src/monstermash/__main__.py` & `monstermash-0.7.2/src/monstermash/__main__.py`

 * *Files identical despite different names*

### Comparing `monstermash-0.7.1/src/monstermash/crypt.py` & `monstermash-0.7.2/src/monstermash/crypt.py`

 * *Files identical despite different names*

### Comparing `monstermash-0.7.1/PKG-INFO` & `monstermash-0.7.2/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: monstermash
-Version: 0.7.1
+Version: 0.7.2
 Summary: 
 Author: Mitchell Lisle
 Author-email: m.lisle90@gmail.com
 Requires-Python: >=3.8.1,<4.0.0
 Classifier: Programming Language :: Python :: 3
 Classifier: Programming Language :: Python :: 3.9
 Classifier: Programming Language :: Python :: 3.10
@@ -13,15 +13,15 @@
 Requires-Dist: pydantic (>=1.10.7,<2.0.0)
 Requires-Dist: pynacl (>=1.5.0,<2.0.0)
 Requires-Dist: questionary (>=1.10.0,<2.0.0)
 Description-Content-Type: text/markdown
 
 ##  🧟 Monstermash
 
-> 1️⃣ version: 0.7.1
+> 1️⃣ version: 0.7.2
 
 > ✍️ author: Mitchell Lisle
 
 ## Install
 Install from PyPi
 
 ```shell
```

