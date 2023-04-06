# Comparing `tmp/filenamemanager-0.2.0.tar.gz` & `tmp/filenamemanager-0.3.0.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "filenamemanager-0.2.0.tar", max compression
+gzip compressed data, was "filenamemanager-0.3.0.tar", max compression
```

## Comparing `filenamemanager-0.2.0.tar` & `filenamemanager-0.3.0.tar`

### file list

```diff
@@ -1,11 +1,10 @@
--rw-r--r--   0        0        0     1507 2022-10-11 14:27:51.037508 filenamemanager-0.2.0/LICENSE
--rw-r--r--   0        0        0     2805 2022-10-11 14:27:51.037508 filenamemanager-0.2.0/README.md
--rw-r--r--   0        0        0      211 2022-10-11 14:27:51.037508 filenamemanager-0.2.0/filename_manager/__init__.py
--rw-r--r--   0        0        0     3105 2022-10-11 14:27:51.037508 filenamemanager-0.2.0/filename_manager/filename_manager.py
--rw-r--r--   0        0        0     3356 2022-10-11 14:27:51.037508 filenamemanager-0.2.0/filename_manager/parameter.py
--rw-r--r--   0        0        0     2936 2022-10-11 14:27:51.037508 filenamemanager-0.2.0/pyproject.toml
--rw-r--r--   0        0        0       45 2022-10-11 14:27:51.037508 filenamemanager-0.2.0/tests/__init__.py
--rw-r--r--   0        0        0     1927 2022-10-11 14:27:51.037508 filenamemanager-0.2.0/tests/test_filename_manager.py
--rw-r--r--   0        0        0     2319 2022-10-11 14:27:51.041508 filenamemanager-0.2.0/tests/test_parameter.py
--rw-r--r--   0        0        0     4284 1970-01-01 00:00:00.000000 filenamemanager-0.2.0/setup.py
--rw-r--r--   0        0        0     5143 1970-01-01 00:00:00.000000 filenamemanager-0.2.0/PKG-INFO
+-rw-r--r--   0        0        0     1507 2023-04-06 14:32:09.934713 filenamemanager-0.3.0/LICENSE
+-rw-r--r--   0        0        0     2805 2023-04-06 14:32:09.934713 filenamemanager-0.3.0/README.md
+-rw-r--r--   0        0        0      211 2023-04-06 14:32:09.934713 filenamemanager-0.3.0/filename_manager/__init__.py
+-rw-r--r--   0        0        0     3105 2023-04-06 14:32:09.934713 filenamemanager-0.3.0/filename_manager/filename_manager.py
+-rw-r--r--   0        0        0     3356 2023-04-06 14:32:09.934713 filenamemanager-0.3.0/filename_manager/parameter.py
+-rw-r--r--   0        0        0     2922 2023-04-06 14:32:09.934713 filenamemanager-0.3.0/pyproject.toml
+-rw-r--r--   0        0        0       45 2023-04-06 14:32:09.934713 filenamemanager-0.3.0/tests/__init__.py
+-rw-r--r--   0        0        0     1927 2023-04-06 14:32:09.934713 filenamemanager-0.3.0/tests/test_filename_manager.py
+-rw-r--r--   0        0        0     2319 2023-04-06 14:32:09.934713 filenamemanager-0.3.0/tests/test_parameter.py
+-rw-r--r--   0        0        0     5133 1970-01-01 00:00:00.000000 filenamemanager-0.3.0/PKG-INFO
```

### Comparing `filenamemanager-0.2.0/LICENSE` & `filenamemanager-0.3.0/LICENSE`

 * *Files identical despite different names*

### Comparing `filenamemanager-0.2.0/README.md` & `filenamemanager-0.3.0/README.md`

 * *Files identical despite different names*

### Comparing `filenamemanager-0.2.0/filename_manager/filename_manager.py` & `filenamemanager-0.3.0/filename_manager/filename_manager.py`

 * *Files identical despite different names*

### Comparing `filenamemanager-0.2.0/filename_manager/parameter.py` & `filenamemanager-0.3.0/filename_manager/parameter.py`

 * *Files identical despite different names*

### Comparing `filenamemanager-0.2.0/pyproject.toml` & `filenamemanager-0.3.0/pyproject.toml`

 * *Files 8% similar despite different names*

```diff
@@ -1,11 +1,11 @@
 [tool]
 [tool.poetry]
 name = "FilenameManager"
-version = "0.2.0"
+version = "0.3.0"
 homepage = "https://github.com/cemde/FilenameManager"
 description = "A simple library to handle filenames automatically for artifacts.."
 authors = ["Cornelius Emde <c.emde@me.com>"]
 readme = "README.md"
 license =  "BSD-3-Clause"
 classifiers=[
     'Development Status :: 2 - Pre-Alpha',
@@ -23,15 +23,14 @@
     { include = "tests", format = "sdist" },
 ]
 
 [tool.poetry.dependencies]
 python = ">=3.6.2,<4.0"
 
 black  = { version = "^22.6", optional = true}
-jinja2  = { version = "<3.0", optional = true}
 isort  = { version = "^5.8.0", optional = true}
 flake8  = { version = "^3.9.2", optional = true}
 flake8-docstrings = { version = "^1.6.0", optional = true }
 mypy = {version = "^0.900", optional = true}
 pytest  = { version = "^6.2.4", optional = true}
 pytest-cov  = { version = "^2.12.0", optional = true}
 tox  = { version = "^3.20.1", optional = true}
@@ -86,14 +85,19 @@
   | _build
   | buck-out
   | build
   | dist
 )/
 '''
 
+
+[tool.ruff]
+line-length = 120
+
+
 [tool.isort]
 multi_line_output = 3
 include_trailing_comma = true
 force_grid_wrap = 0
 use_parentheses = true
 ensure_newline_before_comments = true
 line_length = 120
```

### Comparing `filenamemanager-0.2.0/tests/test_filename_manager.py` & `filenamemanager-0.3.0/tests/test_filename_manager.py`

 * *Files identical despite different names*

### Comparing `filenamemanager-0.2.0/tests/test_parameter.py` & `filenamemanager-0.3.0/tests/test_parameter.py`

 * *Files identical despite different names*

### Comparing `filenamemanager-0.2.0/PKG-INFO` & `filenamemanager-0.3.0/PKG-INFO`

 * *Files 6% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: filenamemanager
-Version: 0.2.0
+Version: 0.3.0
 Summary: A simple library to handle filenames automatically for artifacts..
 Home-page: https://github.com/cemde/FilenameManager
 License: BSD-3-Clause
 Author: Cornelius Emde
 Author-email: c.emde@me.com
 Requires-Python: >=3.6.2,<4.0
 Classifier: Development Status :: 2 - Pre-Alpha
@@ -21,35 +21,34 @@
 Classifier: Programming Language :: Python :: 3.10
 Classifier: Programming Language :: Python :: 3.7
 Classifier: Programming Language :: Python :: 3.8
 Classifier: Programming Language :: Python :: 3.9
 Provides-Extra: dev
 Provides-Extra: doc
 Provides-Extra: test
-Requires-Dist: black (>=22.6,<23.0); extra == "test"
-Requires-Dist: bump2version (>=1.0.1,<2.0.0); extra == "dev"
-Requires-Dist: flake8 (>=3.9.2,<4.0.0); extra == "test"
-Requires-Dist: flake8-docstrings (>=1.6.0,<2.0.0); extra == "test"
-Requires-Dist: isort (>=5.8.0,<6.0.0); extra == "test"
-Requires-Dist: jinja2 (<3.0)
-Requires-Dist: mkdocs (>=1.1.2,<2.0.0); extra == "doc"
-Requires-Dist: mkdocs-autorefs (>=0.2.1,<0.3.0); extra == "doc"
-Requires-Dist: mkdocs-include-markdown-plugin (>=1.0.0,<2.0.0); extra == "doc"
-Requires-Dist: mkdocs-material (>=6.1.7,<7.0.0); extra == "doc"
+Requires-Dist: black (>=22.6,<23.0) ; extra == "test"
+Requires-Dist: bump2version (>=1.0.1,<2.0.0) ; extra == "dev"
+Requires-Dist: flake8 (>=3.9.2,<4.0.0) ; extra == "test"
+Requires-Dist: flake8-docstrings (>=1.6.0,<2.0.0) ; extra == "test"
+Requires-Dist: isort (>=5.8.0,<6.0.0) ; extra == "test"
+Requires-Dist: mkdocs (>=1.1.2,<2.0.0) ; extra == "doc"
+Requires-Dist: mkdocs-autorefs (>=0.2.1,<0.3.0) ; extra == "doc"
+Requires-Dist: mkdocs-include-markdown-plugin (>=1.0.0,<2.0.0) ; extra == "doc"
+Requires-Dist: mkdocs-material (>=6.1.7,<7.0.0) ; extra == "doc"
 Requires-Dist: mkdocs-material-extensions (>=1.0.1,<2.0.0)
-Requires-Dist: mkdocstrings (>=0.15.2,<0.16.0); extra == "doc"
-Requires-Dist: mypy (>=0.900,<0.901); extra == "test"
-Requires-Dist: pip (>=20.3.1,<21.0.0); extra == "dev"
-Requires-Dist: pre-commit (>=2.12.0,<3.0.0); extra == "dev"
-Requires-Dist: pytest (>=6.2.4,<7.0.0); extra == "test"
-Requires-Dist: pytest-cov (>=2.12.0,<3.0.0); extra == "test"
-Requires-Dist: toml (>=0.10.2,<0.11.0); extra == "dev"
-Requires-Dist: tox (>=3.20.1,<4.0.0); extra == "dev"
-Requires-Dist: twine (>=3.3.0,<4.0.0); extra == "dev"
-Requires-Dist: virtualenv (>=20.2.2,<21.0.0); extra == "dev"
+Requires-Dist: mkdocstrings (>=0.15.2,<0.16.0) ; extra == "doc"
+Requires-Dist: mypy (>=0.900,<0.901) ; extra == "test"
+Requires-Dist: pip (>=20.3.1,<21.0.0) ; extra == "dev"
+Requires-Dist: pre-commit (>=2.12.0,<3.0.0) ; extra == "dev"
+Requires-Dist: pytest (>=6.2.4,<7.0.0) ; extra == "test"
+Requires-Dist: pytest-cov (>=2.12.0,<3.0.0) ; extra == "test"
+Requires-Dist: toml (>=0.10.2,<0.11.0) ; extra == "dev"
+Requires-Dist: tox (>=3.20.1,<4.0.0) ; extra == "dev"
+Requires-Dist: twine (>=3.3.0,<4.0.0) ; extra == "dev"
+Requires-Dist: virtualenv (>=20.2.2,<21.0.0) ; extra == "dev"
 Description-Content-Type: text/markdown
 
 # Filename-Manager
 
 
 [![pypi](https://img.shields.io/pypi/v/FilenameManager.svg)](https://pypi.org/project/FilenameManager/)
 [![python](https://img.shields.io/pypi/pyversions/FilenameManager.svg)](https://pypi.org/project/FilenameManager/)
```

