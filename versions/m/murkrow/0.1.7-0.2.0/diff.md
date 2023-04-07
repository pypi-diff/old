# Comparing `tmp/murkrow-0.1.7.tar.gz` & `tmp/murkrow-0.2.0.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "murkrow-0.1.7.tar", max compression
+gzip compressed data, was "murkrow-0.2.0.tar", max compression
```

## Comparing `murkrow-0.1.7.tar` & `murkrow-0.2.0.tar`

### file list

```diff
@@ -1,10 +1,10 @@
--rw-r--r--   0        0        0     1504 2023-04-06 23:40:21.685931 murkrow-0.1.7/LICENSE
--rw-r--r--   0        0        0     1536 2023-04-06 23:55:12.092008 murkrow-0.1.7/README.md
--rw-r--r--   0        0        0      334 2023-04-07 00:09:21.522802 murkrow-0.1.7/murkrow/__init__.py
--rw-r--r--   0        0        0     2783 2023-04-06 23:40:21.688098 murkrow-0.1.7/murkrow/display.py
--rw-r--r--   0        0        0      469 2023-04-07 00:08:22.034218 murkrow-0.1.7/murkrow/messaging.py
--rw-r--r--   0        0        0       19 2023-04-06 23:40:21.688250 murkrow-0.1.7/murkrow/murkrow.py
--rw-r--r--   0        0        0     2799 2023-04-07 00:09:21.522606 murkrow-0.1.7/pyproject.toml
--rw-r--r--   0        0        0       37 2023-04-06 23:40:21.688686 murkrow-0.1.7/tests/__init__.py
--rw-r--r--   0        0        0      624 2023-04-07 00:08:40.215618 murkrow-0.1.7/tests/test_murkrow.py
--rw-r--r--   0        0        0     3685 1970-01-01 00:00:00.000000 murkrow-0.1.7/PKG-INFO
+-rw-r--r--   0        0        0     1504 2023-04-06 23:40:21.685931 murkrow-0.2.0/LICENSE
+-rw-r--r--   0        0        0     1536 2023-04-06 23:55:12.092008 murkrow-0.2.0/README.md
+-rw-r--r--   0        0        0      374 2023-04-07 00:30:55.625174 murkrow-0.2.0/murkrow/__init__.py
+-rw-r--r--   0        0        0     2783 2023-04-06 23:40:21.688098 murkrow-0.2.0/murkrow/display.py
+-rw-r--r--   0        0        0     1587 2023-04-07 00:18:50.562830 murkrow-0.2.0/murkrow/messaging.py
+-rw-r--r--   0        0        0      981 2023-04-07 00:29:36.934709 murkrow-0.2.0/murkrow/murkrow.py
+-rw-r--r--   0        0        0     2818 2023-04-07 00:30:55.624980 murkrow-0.2.0/pyproject.toml
+-rw-r--r--   0        0        0       37 2023-04-06 23:40:21.688686 murkrow-0.2.0/tests/__init__.py
+-rw-r--r--   0        0        0      624 2023-04-07 00:08:40.215618 murkrow-0.2.0/tests/test_murkrow.py
+-rw-r--r--   0        0        0     3726 1970-01-01 00:00:00.000000 murkrow-0.2.0/PKG-INFO
```

### Comparing `murkrow-0.1.7/LICENSE` & `murkrow-0.2.0/LICENSE`

 * *Files identical despite different names*

### Comparing `murkrow-0.1.7/README.md` & `murkrow-0.2.0/README.md`

 * *Files identical despite different names*

### Comparing `murkrow-0.1.7/murkrow/display.py` & `murkrow-0.2.0/murkrow/display.py`

 * *Files identical despite different names*

### Comparing `murkrow-0.1.7/pyproject.toml` & `murkrow-0.2.0/pyproject.toml`

 * *Files 2% similar despite different names*

```diff
@@ -1,11 +1,11 @@
 [tool]
 [tool.poetry]
 name = "murkrow"
-version = "0.1.7"
+version = "0.2.0"
 homepage = "https://github.com/rgbkrk/murkrow"
 description = "Markdown for LLMs."
 authors = ["Kyle Kelley <rgbkrk@gmail.com>"]
 readme = "README.md"
 license =  "BSD-3-Clause"
 classifiers=[
     'Development Status :: 2 - Pre-Alpha',
@@ -41,14 +41,15 @@
 mkdocs-material-extensions  = { version = "^1.0.1", optional = true}
 twine  = { version = "^3.3.0", optional = true}
 mkdocs-autorefs = {version = "^0.2.1", optional = true}
 pre-commit = {version = "^2.12.0", optional = true}
 toml = {version = "^0.10.2", optional = true}
 bump2version = {version = "^1.0.1", optional = true}
 ipython = ">=7, <9"
+openai = "^0.27.4"
 
 [tool.poetry.extras]
 test = [
     "pytest",
     "black",
     "isort",
     "mypy",
```

### Comparing `murkrow-0.1.7/tests/test_murkrow.py` & `murkrow-0.2.0/tests/test_murkrow.py`

 * *Files identical despite different names*

### Comparing `murkrow-0.1.7/PKG-INFO` & `murkrow-0.2.0/PKG-INFO`

 * *Files 2% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: murkrow
-Version: 0.1.7
+Version: 0.2.0
 Summary: Markdown for LLMs.
 Home-page: https://github.com/rgbkrk/murkrow
 License: BSD-3-Clause
 Author: Kyle Kelley
 Author-email: rgbkrk@gmail.com
 Requires-Python: >=3.8,<4.0
 Classifier: Development Status :: 2 - Pre-Alpha
@@ -31,14 +31,15 @@
 Requires-Dist: mkdocs (>=1.1.2,<2.0.0) ; extra == "doc"
 Requires-Dist: mkdocs-autorefs (>=0.2.1,<0.3.0) ; extra == "doc"
 Requires-Dist: mkdocs-include-markdown-plugin (>=1.0.0,<2.0.0) ; extra == "doc"
 Requires-Dist: mkdocs-material (>=6.1.7,<7.0.0) ; extra == "doc"
 Requires-Dist: mkdocs-material-extensions (>=1.0.1,<2.0.0)
 Requires-Dist: mkdocstrings (>=0.15.2,<0.16.0) ; extra == "doc"
 Requires-Dist: mypy (>=0.900,<0.901) ; extra == "test"
+Requires-Dist: openai (>=0.27.4,<0.28.0)
 Requires-Dist: pip (>=20.3.1,<21.0.0) ; extra == "dev"
 Requires-Dist: pre-commit (>=2.12.0,<3.0.0) ; extra == "dev"
 Requires-Dist: pytest (>=6.2.4,<7.0.0) ; extra == "test"
 Requires-Dist: pytest-cov (>=2.12.0,<3.0.0) ; extra == "test"
 Requires-Dist: toml (>=0.10.2,<0.11.0) ; extra == "dev"
 Requires-Dist: tox (>=3.20.1,<4.0.0) ; extra == "dev"
 Requires-Dist: twine (>=3.3.0,<4.0.0) ; extra == "dev"
```

