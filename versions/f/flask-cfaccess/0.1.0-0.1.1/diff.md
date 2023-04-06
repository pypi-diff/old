# Comparing `tmp/flask-cfaccess-0.1.0.tar.gz` & `tmp/flask-cfaccess-0.1.1.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "flask-cfaccess-0.1.0.tar", last modified: Thu Apr  6 15:10:14 2023, max compression
+gzip compressed data, was "flask-cfaccess-0.1.1.tar", last modified: Thu Apr  6 15:45:36 2023, max compression
```

## Comparing `flask-cfaccess-0.1.0.tar` & `flask-cfaccess-0.1.1.tar`

### file list

```diff
@@ -1,39 +1,41 @@
-drwxr-xr-x   0 michael   (1000) michael   (1000)        0 2023-04-06 15:10:14.569065 flask-cfaccess-0.1.0/
--rw-r--r--   0 michael   (1000) michael   (1000)     2794 2023-04-06 14:53:29.000000 flask-cfaccess-0.1.0/.gitignore
--rw-r--r--   0 michael   (1000) michael   (1000)      299 2023-04-06 14:54:01.000000 flask-cfaccess-0.1.0/.readthedocs.yml
--rw-r--r--   0 michael   (1000) michael   (1000)       69 2023-04-06 15:01:48.000000 flask-cfaccess-0.1.0/CHANGES.md
--rw-r--r--   0 michael   (1000) michael   (1000)     1077 2023-04-06 09:18:30.000000 flask-cfaccess-0.1.0/LICENSE
--rw-r--r--   0 michael   (1000) michael   (1000)      118 2023-04-06 14:52:50.000000 flask-cfaccess-0.1.0/MANIFEST.in
--rw-r--r--   0 michael   (1000) michael   (1000)     1469 2023-04-06 15:10:14.569065 flask-cfaccess-0.1.0/PKG-INFO
--rw-r--r--   0 michael   (1000) michael   (1000)      408 2023-04-06 09:33:45.000000 flask-cfaccess-0.1.0/README.md
--rw-r--r--   0 michael   (1000) michael   (1000)      160 2023-04-06 15:10:14.000000 flask-cfaccess-0.1.0/_version.py
-drwxr-xr-x   0 michael   (1000) michael   (1000)        0 2023-04-06 15:10:14.566065 flask-cfaccess-0.1.0/docs/
--rw-r--r--   0 michael   (1000) michael   (1000)      634 2023-04-06 08:55:24.000000 flask-cfaccess-0.1.0/docs/Makefile
--rw-r--r--   0 michael   (1000) michael   (1000)       74 2023-04-06 10:11:04.000000 flask-cfaccess-0.1.0/docs/api.rst
--rw-r--r--   0 michael   (1000) michael   (1000)       29 2023-04-06 09:29:40.000000 flask-cfaccess-0.1.0/docs/changes.rst
--rw-r--r--   0 michael   (1000) michael   (1000)     3457 2023-04-06 11:10:58.000000 flask-cfaccess-0.1.0/docs/conf.py
--rw-r--r--   0 michael   (1000) michael   (1000)      755 2023-04-06 09:45:47.000000 flask-cfaccess-0.1.0/docs/flask-login.rst
--rw-r--r--   0 michael   (1000) michael   (1000)     3012 2023-04-06 09:57:08.000000 flask-cfaccess-0.1.0/docs/getting-started.rst
--rw-r--r--   0 michael   (1000) michael   (1000)      458 2023-04-06 11:15:31.000000 flask-cfaccess-0.1.0/docs/index.rst
--rw-r--r--   0 michael   (1000) michael   (1000)      608 2023-04-06 09:26:30.000000 flask-cfaccess-0.1.0/docs/installation.rst
--rw-r--r--   0 michael   (1000) michael   (1000)      128 2023-04-06 09:18:57.000000 flask-cfaccess-0.1.0/docs/license.rst
--rw-r--r--   0 michael   (1000) michael   (1000)      800 2023-04-06 08:55:24.000000 flask-cfaccess-0.1.0/docs/make.bat
--rw-r--r--   0 michael   (1000) michael   (1000)       90 2023-04-06 14:57:04.000000 flask-cfaccess-0.1.0/docs/requirements.txt
-drwxr-xr-x   0 michael   (1000) michael   (1000)        0 2023-04-06 15:10:14.567065 flask-cfaccess-0.1.0/flask_cfaccess.egg-info/
--rw-r--r--   0 michael   (1000) michael   (1000)     1469 2023-04-06 15:10:14.000000 flask-cfaccess-0.1.0/flask_cfaccess.egg-info/PKG-INFO
--rw-r--r--   0 michael   (1000) michael   (1000)      648 2023-04-06 15:10:14.000000 flask-cfaccess-0.1.0/flask_cfaccess.egg-info/SOURCES.txt
--rw-r--r--   0 michael   (1000) michael   (1000)        1 2023-04-06 15:10:14.000000 flask-cfaccess-0.1.0/flask_cfaccess.egg-info/dependency_links.txt
--rw-r--r--   0 michael   (1000) michael   (1000)      310 2023-04-06 15:10:14.000000 flask-cfaccess-0.1.0/flask_cfaccess.egg-info/requires.txt
--rw-r--r--   0 michael   (1000) michael   (1000)       15 2023-04-06 15:10:14.000000 flask-cfaccess-0.1.0/flask_cfaccess.egg-info/top_level.txt
--rw-r--r--   0 michael   (1000) michael   (1000)     4907 2023-04-06 15:02:36.000000 flask-cfaccess-0.1.0/flask_cfaccess.py
--rw-r--r--   0 michael   (1000) michael   (1000)        0 2023-04-06 12:10:05.000000 flask-cfaccess-0.1.0/py.typed
--rw-r--r--   0 michael   (1000) michael   (1000)     2830 2023-04-06 15:00:11.000000 flask-cfaccess-0.1.0/pyproject.toml
--rw-r--r--   0 michael   (1000) michael   (1000)       43 2023-04-06 15:01:37.000000 flask-cfaccess-0.1.0/requirements.txt
--rw-r--r--   0 michael   (1000) michael   (1000)       38 2023-04-06 15:10:14.569065 flask-cfaccess-0.1.0/setup.cfg
-drwxr-xr-x   0 michael   (1000) michael   (1000)        0 2023-04-06 15:10:14.568066 flask-cfaccess-0.1.0/tests/
--rw-r--r--   0 michael   (1000) michael   (1000)     2873 2023-04-06 14:45:25.000000 flask-cfaccess-0.1.0/tests/conftest.py
-drwxr-xr-x   0 michael   (1000) michael   (1000)        0 2023-04-06 15:10:14.569065 flask-cfaccess-0.1.0/tests/keys/
--rw-r--r--   0 michael   (1000) michael   (1000)     1734 2023-04-06 14:23:11.000000 flask-cfaccess-0.1.0/tests/keys/rsa_private_key.json
--rw-r--r--   0 michael   (1000) michael   (1000)      456 2023-04-06 14:23:03.000000 flask-cfaccess-0.1.0/tests/keys/rsa_public_key.json
--rw-r--r--   0 michael   (1000) michael   (1000)      113 2023-04-06 13:32:30.000000 flask-cfaccess-0.1.0/tests/requirements.txt
--rw-r--r--   0 michael   (1000) michael   (1000)     6629 2023-04-06 14:50:04.000000 flask-cfaccess-0.1.0/tests/test_cfaccess.py
+drwxr-xr-x   0 michael   (1000) michael   (1000)        0 2023-04-06 15:45:36.117090 flask-cfaccess-0.1.1/
+drwxr-xr-x   0 michael   (1000) michael   (1000)        0 2023-04-06 15:45:36.113090 flask-cfaccess-0.1.1/.github/
+-rw-r--r--   0 michael   (1000) michael   (1000)       15 2023-04-06 15:42:44.000000 flask-cfaccess-0.1.1/.github/FUNDING.yml
+-rw-r--r--   0 michael   (1000) michael   (1000)     2794 2023-04-06 14:53:29.000000 flask-cfaccess-0.1.1/.gitignore
+-rw-r--r--   0 michael   (1000) michael   (1000)      353 2023-04-06 15:42:44.000000 flask-cfaccess-0.1.1/.readthedocs.yml
+-rw-r--r--   0 michael   (1000) michael   (1000)      164 2023-04-06 15:42:44.000000 flask-cfaccess-0.1.1/CHANGES.md
+-rw-r--r--   0 michael   (1000) michael   (1000)     1077 2023-04-06 09:18:30.000000 flask-cfaccess-0.1.1/LICENSE
+-rw-r--r--   0 michael   (1000) michael   (1000)      118 2023-04-06 14:52:50.000000 flask-cfaccess-0.1.1/MANIFEST.in
+-rw-r--r--   0 michael   (1000) michael   (1000)     1469 2023-04-06 15:45:36.117090 flask-cfaccess-0.1.1/PKG-INFO
+-rw-r--r--   0 michael   (1000) michael   (1000)      408 2023-04-06 09:33:45.000000 flask-cfaccess-0.1.1/README.md
+-rw-r--r--   0 michael   (1000) michael   (1000)      160 2023-04-06 15:45:35.000000 flask-cfaccess-0.1.1/_version.py
+drwxr-xr-x   0 michael   (1000) michael   (1000)        0 2023-04-06 15:45:36.114090 flask-cfaccess-0.1.1/docs/
+-rw-r--r--   0 michael   (1000) michael   (1000)      634 2023-04-06 08:55:24.000000 flask-cfaccess-0.1.1/docs/Makefile
+-rw-r--r--   0 michael   (1000) michael   (1000)       74 2023-04-06 10:11:04.000000 flask-cfaccess-0.1.1/docs/api.rst
+-rw-r--r--   0 michael   (1000) michael   (1000)       29 2023-04-06 09:29:40.000000 flask-cfaccess-0.1.1/docs/changes.rst
+-rw-r--r--   0 michael   (1000) michael   (1000)     3492 2023-04-06 15:42:44.000000 flask-cfaccess-0.1.1/docs/conf.py
+-rw-r--r--   0 michael   (1000) michael   (1000)      755 2023-04-06 09:45:47.000000 flask-cfaccess-0.1.1/docs/flask-login.rst
+-rw-r--r--   0 michael   (1000) michael   (1000)     3012 2023-04-06 09:57:08.000000 flask-cfaccess-0.1.1/docs/getting-started.rst
+-rw-r--r--   0 michael   (1000) michael   (1000)      458 2023-04-06 15:30:32.000000 flask-cfaccess-0.1.1/docs/index.rst
+-rw-r--r--   0 michael   (1000) michael   (1000)      608 2023-04-06 09:26:30.000000 flask-cfaccess-0.1.1/docs/installation.rst
+-rw-r--r--   0 michael   (1000) michael   (1000)      128 2023-04-06 09:18:57.000000 flask-cfaccess-0.1.1/docs/license.rst
+-rw-r--r--   0 michael   (1000) michael   (1000)      800 2023-04-06 08:55:24.000000 flask-cfaccess-0.1.1/docs/make.bat
+-rw-r--r--   0 michael   (1000) michael   (1000)       90 2023-04-06 14:57:04.000000 flask-cfaccess-0.1.1/docs/requirements.txt
+drwxr-xr-x   0 michael   (1000) michael   (1000)        0 2023-04-06 15:45:36.115090 flask-cfaccess-0.1.1/flask_cfaccess.egg-info/
+-rw-r--r--   0 michael   (1000) michael   (1000)     1469 2023-04-06 15:45:36.000000 flask-cfaccess-0.1.1/flask_cfaccess.egg-info/PKG-INFO
+-rw-r--r--   0 michael   (1000) michael   (1000)      668 2023-04-06 15:45:36.000000 flask-cfaccess-0.1.1/flask_cfaccess.egg-info/SOURCES.txt
+-rw-r--r--   0 michael   (1000) michael   (1000)        1 2023-04-06 15:45:36.000000 flask-cfaccess-0.1.1/flask_cfaccess.egg-info/dependency_links.txt
+-rw-r--r--   0 michael   (1000) michael   (1000)      340 2023-04-06 15:45:36.000000 flask-cfaccess-0.1.1/flask_cfaccess.egg-info/requires.txt
+-rw-r--r--   0 michael   (1000) michael   (1000)       15 2023-04-06 15:45:36.000000 flask-cfaccess-0.1.1/flask_cfaccess.egg-info/top_level.txt
+-rw-r--r--   0 michael   (1000) michael   (1000)     4907 2023-04-06 15:02:36.000000 flask-cfaccess-0.1.1/flask_cfaccess.py
+-rw-r--r--   0 michael   (1000) michael   (1000)        0 2023-04-06 12:10:05.000000 flask-cfaccess-0.1.1/py.typed
+-rw-r--r--   0 michael   (1000) michael   (1000)     2878 2023-04-06 15:42:44.000000 flask-cfaccess-0.1.1/pyproject.toml
+-rw-r--r--   0 michael   (1000) michael   (1000)       43 2023-04-06 15:01:37.000000 flask-cfaccess-0.1.1/requirements.txt
+-rw-r--r--   0 michael   (1000) michael   (1000)       38 2023-04-06 15:45:36.117090 flask-cfaccess-0.1.1/setup.cfg
+drwxr-xr-x   0 michael   (1000) michael   (1000)        0 2023-04-06 15:45:36.116090 flask-cfaccess-0.1.1/tests/
+-rw-r--r--   0 michael   (1000) michael   (1000)     2873 2023-04-06 14:45:25.000000 flask-cfaccess-0.1.1/tests/conftest.py
+drwxr-xr-x   0 michael   (1000) michael   (1000)        0 2023-04-06 15:45:36.116090 flask-cfaccess-0.1.1/tests/keys/
+-rw-r--r--   0 michael   (1000) michael   (1000)     1734 2023-04-06 14:23:11.000000 flask-cfaccess-0.1.1/tests/keys/rsa_private_key.json
+-rw-r--r--   0 michael   (1000) michael   (1000)      456 2023-04-06 14:23:03.000000 flask-cfaccess-0.1.1/tests/keys/rsa_public_key.json
+-rw-r--r--   0 michael   (1000) michael   (1000)      113 2023-04-06 13:32:30.000000 flask-cfaccess-0.1.1/tests/requirements.txt
+-rw-r--r--   0 michael   (1000) michael   (1000)     6629 2023-04-06 14:50:04.000000 flask-cfaccess-0.1.1/tests/test_cfaccess.py
```

### Comparing `flask-cfaccess-0.1.0/.gitignore` & `flask-cfaccess-0.1.1/.gitignore`

 * *Files identical despite different names*

### Comparing `flask-cfaccess-0.1.0/LICENSE` & `flask-cfaccess-0.1.1/LICENSE`

 * *Files identical despite different names*

### Comparing `flask-cfaccess-0.1.0/PKG-INFO` & `flask-cfaccess-0.1.1/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: flask-cfaccess
-Version: 0.1.0
+Version: 0.1.1
 Summary: Zero Trust Access with Cloudflare Access for Flask applications.
 Author-email: Michael de Villiers <michael@devilears.co.za>
 Maintainer-email: Michael de Villiers <michael@devilears.co.za>
 License: MIT
 Project-URL: Documentation, https://flask-cfaccess.readthedocs.io/
 Project-URL: Changes, https://flask-cfaccess.readthedocs.io/changes/
 Project-URL: Source Code, https://github.com/COUR4G3/flask-cfaccess/
```

### Comparing `flask-cfaccess-0.1.0/docs/Makefile` & `flask-cfaccess-0.1.1/docs/Makefile`

 * *Files identical despite different names*

### Comparing `flask-cfaccess-0.1.0/docs/conf.py` & `flask-cfaccess-0.1.1/docs/conf.py`

 * *Files 6% similar despite different names*

```diff
@@ -12,27 +12,26 @@
 #
 # import os
 import importlib
 import inspect
 import os
 import sys
 
-sys.path.insert(0, os.path.abspath(".."))
-
+from importlib.metadata import version as get_version
 
-from flask_cfaccess import __version__
+sys.path.insert(0, os.path.abspath(".."))
 
 # -- Project information -----------------------------------------------------
 
 project = "flask-cfaccess"
 copyright = "2023, Michael de Villiers"
 author = "Michael de Villiers"
 
 # The full version, including alpha/beta/rc tags
-release = "0.1-dev0"
+release = get_version("flask_cfaccess")
 
 
 # -- General configuration ---------------------------------------------------
 
 # Add any Sphinx extension module names here, as strings. They can be
 # extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
 # ones.
@@ -61,15 +60,15 @@
 # a list of builtin themes.
 #
 html_theme = "alabaster"
 
 # Add any paths that contain custom static files (such as style sheets) here,
 # relative to this directory. They are copied after the builtin static files,
 # so a file named "default.css" will overwrite the builtin "default.css".
-html_static_path = ["_static"]
+# html_static_path = ["_static"]
 
 
 autodoc_typehints = "description"
 
 
 intersphinx_mapping = {
     "python": ("https://docs.python.org/3/", None),
```

### Comparing `flask-cfaccess-0.1.0/docs/flask-login.rst` & `flask-cfaccess-0.1.1/docs/flask-login.rst`

 * *Files identical despite different names*

### Comparing `flask-cfaccess-0.1.0/docs/getting-started.rst` & `flask-cfaccess-0.1.1/docs/getting-started.rst`

 * *Files identical despite different names*

### Comparing `flask-cfaccess-0.1.0/docs/installation.rst` & `flask-cfaccess-0.1.1/docs/installation.rst`

 * *Files identical despite different names*

### Comparing `flask-cfaccess-0.1.0/docs/make.bat` & `flask-cfaccess-0.1.1/docs/make.bat`

 * *Files identical despite different names*

### Comparing `flask-cfaccess-0.1.0/flask_cfaccess.egg-info/PKG-INFO` & `flask-cfaccess-0.1.1/flask_cfaccess.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: flask-cfaccess
-Version: 0.1.0
+Version: 0.1.1
 Summary: Zero Trust Access with Cloudflare Access for Flask applications.
 Author-email: Michael de Villiers <michael@devilears.co.za>
 Maintainer-email: Michael de Villiers <michael@devilears.co.za>
 License: MIT
 Project-URL: Documentation, https://flask-cfaccess.readthedocs.io/
 Project-URL: Changes, https://flask-cfaccess.readthedocs.io/changes/
 Project-URL: Source Code, https://github.com/COUR4G3/flask-cfaccess/
```

### Comparing `flask-cfaccess-0.1.0/flask_cfaccess.egg-info/SOURCES.txt` & `flask-cfaccess-0.1.1/flask_cfaccess.egg-info/SOURCES.txt`

 * *Files 16% similar despite different names*

```diff
@@ -5,14 +5,15 @@
 MANIFEST.in
 README.md
 _version.py
 flask_cfaccess.py
 py.typed
 pyproject.toml
 requirements.txt
+.github/FUNDING.yml
 docs/Makefile
 docs/api.rst
 docs/changes.rst
 docs/conf.py
 docs/flask-login.rst
 docs/getting-started.rst
 docs/index.rst
```

### Comparing `flask-cfaccess-0.1.0/flask_cfaccess.py` & `flask-cfaccess-0.1.1/flask_cfaccess.py`

 * *Files identical despite different names*

### Comparing `flask-cfaccess-0.1.0/pyproject.toml` & `flask-cfaccess-0.1.1/pyproject.toml`

 * *Files 5% similar despite different names*

```diff
@@ -14,14 +14,16 @@
     "Programming Language :: Python",
     "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
 ]
 dynamic = ["version"]
 requires-python = ">= 3.8"
 dependencies = [
     "flask ~= 2.2.3",
+    "pyjwt ~= 2.6.0",
+    "requests ~= 2.28.2",
 ]
 
 [project.urls]
 Documentation = "https://flask-cfaccess.readthedocs.io/"
 Changes = "https://flask-cfaccess.readthedocs.io/changes/"
 "Source Code" = "https://github.com/COUR4G3/flask-cfaccess/"
 "Issue Tracker" = "https://github.com/COUR4G3/hacksaw/flask-cfaccess/"
```

### Comparing `flask-cfaccess-0.1.0/tests/conftest.py` & `flask-cfaccess-0.1.1/tests/conftest.py`

 * *Files identical despite different names*

### Comparing `flask-cfaccess-0.1.0/tests/keys/rsa_private_key.json` & `flask-cfaccess-0.1.1/tests/keys/rsa_private_key.json`

 * *Files identical despite different names*

### Comparing `flask-cfaccess-0.1.0/tests/test_cfaccess.py` & `flask-cfaccess-0.1.1/tests/test_cfaccess.py`

 * *Files identical despite different names*

