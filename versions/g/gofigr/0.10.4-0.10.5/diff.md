# Comparing `tmp/gofigr-0.10.4.tar.gz` & `tmp/gofigr-0.10.5.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "gofigr-0.10.4.tar", last modified: Mon Apr  3 19:13:07 2023, max compression
+gzip compressed data, was "gofigr-0.10.5.tar", last modified: Thu Apr  6 16:46:32 2023, max compression
```

## Comparing `gofigr-0.10.4.tar` & `gofigr-0.10.5.tar`

### file list

```diff
@@ -1,27 +1,27 @@
-drwxrwxr-x   0 ubuntu    (1000) ubuntu    (1000)        0 2023-04-03 19:13:07.350076 gofigr-0.10.4/
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     1078 2023-04-03 19:12:00.000000 gofigr-0.10.4/LICENSE
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)       80 2023-04-03 19:12:00.000000 gofigr-0.10.4/MANIFEST.in
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     7833 2023-04-03 19:13:07.350076 gofigr-0.10.4/PKG-INFO
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     6023 2023-04-03 19:12:00.000000 gofigr-0.10.4/README.rst
-drwxrwxr-x   0 ubuntu    (1000) ubuntu    (1000)        0 2023-04-03 19:13:07.338076 gofigr-0.10.4/gofigr/
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)    12625 2023-04-03 19:12:00.000000 gofigr-0.10.4/gofigr/__init__.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     4991 2023-04-03 19:12:00.000000 gofigr-0.10.4/gofigr/gfconfig.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)    17462 2023-04-03 19:12:00.000000 gofigr-0.10.4/gofigr/jupyter.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)    41221 2023-04-03 19:12:00.000000 gofigr-0.10.4/gofigr/models.py
-drwxrwxr-x   0 ubuntu    (1000) ubuntu    (1000)        0 2023-04-03 19:13:07.346076 gofigr-0.10.4/gofigr/resources/
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)   584424 2023-04-03 19:12:00.000000 gofigr-0.10.4/gofigr/resources/FreeMono.ttf
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)       76 2023-04-03 19:12:00.000000 gofigr-0.10.4/gofigr/resources/__init__.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     3097 2023-04-03 19:12:00.000000 gofigr-0.10.4/gofigr/watermarks.py
-drwxrwxr-x   0 ubuntu    (1000) ubuntu    (1000)        0 2023-04-03 19:13:07.342076 gofigr-0.10.4/gofigr.egg-info/
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     7833 2023-04-03 19:13:07.000000 gofigr-0.10.4/gofigr.egg-info/PKG-INFO
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)      447 2023-04-03 19:13:07.000000 gofigr-0.10.4/gofigr.egg-info/SOURCES.txt
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)        1 2023-04-03 19:13:07.000000 gofigr-0.10.4/gofigr.egg-info/dependency_links.txt
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)       50 2023-04-03 19:13:07.000000 gofigr-0.10.4/gofigr.egg-info/entry_points.txt
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)      164 2023-04-03 19:13:07.000000 gofigr-0.10.4/gofigr.egg-info/requires.txt
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)        7 2023-04-03 19:13:07.000000 gofigr-0.10.4/gofigr.egg-info/top_level.txt
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     1478 2023-04-03 19:12:00.000000 gofigr-0.10.4/pyproject.toml
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)       38 2023-04-03 19:13:07.350076 gofigr-0.10.4/setup.cfg
-drwxrwxr-x   0 ubuntu    (1000) ubuntu    (1000)        0 2023-04-03 19:13:07.350076 gofigr-0.10.4/tests/
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)    40678 2023-04-03 19:12:00.000000 gofigr-0.10.4/tests/test_client.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     2698 2023-04-03 19:12:00.000000 gofigr-0.10.4/tests/test_models.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     1007 2023-04-03 19:12:00.000000 gofigr-0.10.4/tests/test_watermarks.py
+drwxrwxr-x   0 ubuntu    (1000) ubuntu    (1000)        0 2023-04-06 16:46:32.178324 gofigr-0.10.5/
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     1078 2023-04-06 16:28:46.000000 gofigr-0.10.5/LICENSE
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)       80 2023-04-06 16:28:46.000000 gofigr-0.10.5/MANIFEST.in
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     7833 2023-04-06 16:46:32.178324 gofigr-0.10.5/PKG-INFO
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     6023 2023-04-06 16:28:46.000000 gofigr-0.10.5/README.rst
+drwxrwxr-x   0 ubuntu    (1000) ubuntu    (1000)        0 2023-04-06 16:46:32.170324 gofigr-0.10.5/gofigr/
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)    12625 2023-04-06 16:28:46.000000 gofigr-0.10.5/gofigr/__init__.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     4991 2023-04-06 16:28:46.000000 gofigr-0.10.5/gofigr/gfconfig.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)    17897 2023-04-06 16:28:46.000000 gofigr-0.10.5/gofigr/jupyter.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)    41221 2023-04-06 16:28:46.000000 gofigr-0.10.5/gofigr/models.py
+drwxrwxr-x   0 ubuntu    (1000) ubuntu    (1000)        0 2023-04-06 16:46:32.174324 gofigr-0.10.5/gofigr/resources/
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)   584424 2023-04-06 16:28:46.000000 gofigr-0.10.5/gofigr/resources/FreeMono.ttf
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)       76 2023-04-06 16:28:46.000000 gofigr-0.10.5/gofigr/resources/__init__.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     3097 2023-04-06 16:28:46.000000 gofigr-0.10.5/gofigr/watermarks.py
+drwxrwxr-x   0 ubuntu    (1000) ubuntu    (1000)        0 2023-04-06 16:46:32.174324 gofigr-0.10.5/gofigr.egg-info/
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     7833 2023-04-06 16:46:32.000000 gofigr-0.10.5/gofigr.egg-info/PKG-INFO
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)      447 2023-04-06 16:46:32.000000 gofigr-0.10.5/gofigr.egg-info/SOURCES.txt
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)        1 2023-04-06 16:46:32.000000 gofigr-0.10.5/gofigr.egg-info/dependency_links.txt
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)       50 2023-04-06 16:46:32.000000 gofigr-0.10.5/gofigr.egg-info/entry_points.txt
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)      174 2023-04-06 16:46:32.000000 gofigr-0.10.5/gofigr.egg-info/requires.txt
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)        7 2023-04-06 16:46:32.000000 gofigr-0.10.5/gofigr.egg-info/top_level.txt
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     1522 2023-04-06 16:28:46.000000 gofigr-0.10.5/pyproject.toml
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)       38 2023-04-06 16:46:32.178324 gofigr-0.10.5/setup.cfg
+drwxrwxr-x   0 ubuntu    (1000) ubuntu    (1000)        0 2023-04-06 16:46:32.178324 gofigr-0.10.5/tests/
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)    40678 2023-04-06 16:28:46.000000 gofigr-0.10.5/tests/test_client.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     2698 2023-04-06 16:28:46.000000 gofigr-0.10.5/tests/test_models.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     1007 2023-04-06 16:28:46.000000 gofigr-0.10.5/tests/test_watermarks.py
```

### Comparing `gofigr-0.10.4/LICENSE` & `gofigr-0.10.5/LICENSE`

 * *Files identical despite different names*

### Comparing `gofigr-0.10.4/PKG-INFO` & `gofigr-0.10.5/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: gofigr
-Version: 0.10.4
+Version: 0.10.5
 Summary: GoFigr client library
 Author-email: Maciej Pacula <maciej@gofigr.io>
 License: Copyright 2022-2023 Flagstaff Solutions, LLC
         
         Permission is hereby granted, free of charge, to any person obtaining a copy of
         this software and associated documentation files (the “Software”), to deal in
         the Software without restriction, including without limitation the rights to
@@ -20,28 +20,28 @@
         FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
         AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
         LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
         OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
         THE SOFTWARE.
         
 Project-URL: Homepage, https://www.gofigr.io
-Project-URL: Documentation, https://gofigr.io/docs/gofigr-python/latest/
+Project-URL: Documentation, https://gofigr.io/docs/gofigr-python/10.0.4/
 Keywords: science,visualization,version control,plotting,data,reproducibility
 Classifier: License :: OSI Approved :: MIT License
 Classifier: Programming Language :: Python
 Classifier: Programming Language :: Python :: 3
 Requires-Python: >=3.9
 Description-Content-Type: text/x-rst
 Provides-Extra: dev
 License-File: LICENSE
 
 .. figure:: docs/source/images/logo_wide_light.png
   :alt: GoFigr.io logo
 
-GoFigr - Python Client (0.10.4)
+GoFigr - Python Client (0.10.5)
 ====================================
 GoFigr (https://www.gofigr.io) is a service which provides sophisticated version control for figures.
 
 This repository contains the Python client for GoFigr.
 
 Account registration
 ********************
```

### Comparing `gofigr-0.10.4/README.rst` & `gofigr-0.10.5/README.rst`

 * *Files 0% similar despite different names*

```diff
@@ -1,11 +1,11 @@
 .. figure:: docs/source/images/logo_wide_light.png
   :alt: GoFigr.io logo
 
-GoFigr - Python Client (0.10.4)
+GoFigr - Python Client (0.10.5)
 ====================================
 GoFigr (https://www.gofigr.io) is a service which provides sophisticated version control for figures.
 
 This repository contains the Python client for GoFigr.
 
 Account registration
 ********************
```

### Comparing `gofigr-0.10.4/gofigr/__init__.py` & `gofigr-0.10.5/gofigr/__init__.py`

 * *Files identical despite different names*

### Comparing `gofigr-0.10.4/gofigr/gfconfig.py` & `gofigr-0.10.5/gofigr/gfconfig.py`

 * *Files identical despite different names*

### Comparing `gofigr-0.10.4/gofigr/jupyter.py` & `gofigr-0.10.5/gofigr/jupyter.py`

 * *Files 2% similar despite different names*

```diff
@@ -12,14 +12,15 @@
 import os
 import subprocess
 from collections import namedtuple
 from functools import wraps
 from uuid import UUID
 
 import PIL
+import ipynbname
 import matplotlib.pyplot as plt
 import six
 from IPython.core.display_functions import display
 
 from gofigr import GoFigr, CodeLanguage, API_URL, APP_URL
 from gofigr.watermarks import DefaultWatermark
 
@@ -195,14 +196,25 @@
         :param revision: FigureRevision
         :return: annotated FigureRevision
 
         """
         return revision
 
 
+class NotebookNameAnnotator(Annotator):
+    """"Annotates revisions with the name & path of the current notebook"""
+    def annotate(self, revision):
+        if revision.metadata is None:
+            revision.metadata = {}
+
+        revision.metadata['notebook_name'] = ipynbname.name()
+        revision.metadata['notebook_path'] = str(ipynbname.path())
+        return revision
+
+
 class CellCodeAnnotator(Annotator):
     """"Annotates revisions with cell contents"""
     def annotate(self, revision):
         revision.data.append(_GF_EXTENSION.gf.CodeData(name="Jupyter Cell",
                                                        language=CodeLanguage.PYTHON,
                                                        contents=_GF_EXTENSION.cell.raw_cell))
         return revision
@@ -228,15 +240,15 @@
         except subprocess.CalledProcessError as e:
             output = e.output
 
         revision.data.append(_GF_EXTENSION.gf.TextData(name="System Info", contents=output))
         return revision
 
 
-DEFAULT_ANNOTATORS = (CellCodeAnnotator(), SystemAnnotator(), PipFreezeAnnotator())
+DEFAULT_ANNOTATORS = (NotebookNameAnnotator(), CellCodeAnnotator(), SystemAnnotator(), PipFreezeAnnotator())
 
 
 def figure_to_bytes(fig, fmt):
     """\
     Converts a matplotlib figure to raw bytes
 
     :param fig: matplotlib figure
@@ -449,15 +461,15 @@
     else:
         return matches[0]
 
 
 @from_config_or_env("GF_", os.path.join(os.environ['HOME'], '.gofigr'))
 def configure(username, password, workspace=None, analysis=None, url=API_URL,
               default_metadata=None, auto_publish=True,
-              watermark=None, annotators=None):
+              watermark=None, annotators=DEFAULT_ANNOTATORS):
     """\
     Configures the Jupyter plugin for use.
 
     :param username: GoFigr username
     :param password: GoFigr password
     :param url: API URL
     :param workspace: one of: API ID (string), ApiId instance, or FindByName instance
```

### Comparing `gofigr-0.10.4/gofigr/models.py` & `gofigr-0.10.5/gofigr/models.py`

 * *Files identical despite different names*

### Comparing `gofigr-0.10.4/gofigr/resources/FreeMono.ttf` & `gofigr-0.10.5/gofigr/resources/FreeMono.ttf`

 * *Files identical despite different names*

### Comparing `gofigr-0.10.4/gofigr/watermarks.py` & `gofigr-0.10.5/gofigr/watermarks.py`

 * *Files identical despite different names*

### Comparing `gofigr-0.10.4/gofigr.egg-info/PKG-INFO` & `gofigr-0.10.5/gofigr.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: gofigr
-Version: 0.10.4
+Version: 0.10.5
 Summary: GoFigr client library
 Author-email: Maciej Pacula <maciej@gofigr.io>
 License: Copyright 2022-2023 Flagstaff Solutions, LLC
         
         Permission is hereby granted, free of charge, to any person obtaining a copy of
         this software and associated documentation files (the “Software”), to deal in
         the Software without restriction, including without limitation the rights to
@@ -20,28 +20,28 @@
         FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
         AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
         LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
         OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
         THE SOFTWARE.
         
 Project-URL: Homepage, https://www.gofigr.io
-Project-URL: Documentation, https://gofigr.io/docs/gofigr-python/latest/
+Project-URL: Documentation, https://gofigr.io/docs/gofigr-python/10.0.4/
 Keywords: science,visualization,version control,plotting,data,reproducibility
 Classifier: License :: OSI Approved :: MIT License
 Classifier: Programming Language :: Python
 Classifier: Programming Language :: Python :: 3
 Requires-Python: >=3.9
 Description-Content-Type: text/x-rst
 Provides-Extra: dev
 License-File: LICENSE
 
 .. figure:: docs/source/images/logo_wide_light.png
   :alt: GoFigr.io logo
 
-GoFigr - Python Client (0.10.4)
+GoFigr - Python Client (0.10.5)
 ====================================
 GoFigr (https://www.gofigr.io) is a service which provides sophisticated version control for figures.
 
 This repository contains the Python client for GoFigr.
 
 Account registration
 ********************
```

### Comparing `gofigr-0.10.4/pyproject.toml` & `gofigr-0.10.5/pyproject.toml`

 * *Files 12% similar despite different names*

```diff
@@ -2,52 +2,53 @@
 
 [build-system]
 requires      = ["setuptools>=61.0.0", "wheel"]
 build-backend = "setuptools.build_meta"
 
 [project]
 name = "gofigr"
-version = "0.10.4"
+version = "0.10.5"
 description = "GoFigr client library"
 readme = "README.rst"
 authors = [{ name = "Maciej Pacula", email = "maciej@gofigr.io" }]
 license = { file = "LICENSE" }
 classifiers = [
     "License :: OSI Approved :: MIT License",
     "Programming Language :: Python",
     "Programming Language :: Python :: 3",
 ]
 keywords = ["science", "visualization", "version control", "plotting", "data", "reproducibility"]
 dependencies = [
     "numpy", "pandas", "pyqrcode", "pillow", "matplotlib", "dateutils",
-    "python-dateutil", "ipython", "requests", "pypng"
+    "python-dateutil", "ipython", "requests", "pypng", "ipynbname"
 ]
 requires-python = ">=3.9"
 
 [project.optional-dependencies]
 dev = ["pip-tools", "bumpver", "build", "twine", "pylint", "flake8", "sphinx", "sphinx_rtd_theme"]
 
 [project.urls]
 Homepage = "https://www.gofigr.io"
-Documentation = "https://gofigr.io/docs/gofigr-python/latest/"
+Documentation = "https://gofigr.io/docs/gofigr-python/10.0.4/"
 
 [project.scripts]
 gfconfig = "gofigr.gfconfig:main"
 
 [tool.bumpver]
-current_version = "0.10.4"
+current_version = "0.10.5"
 version_pattern = "MAJOR.MINOR.PATCH"
 commit_message = "Bump version {old_version} -> {new_version}"
 commit = true
 tag = true
 push = false
 
 [tool.bumpver.file_patterns]
 "pyproject.toml" = [
     'version = "{version}"',
+    'gofigr-python/{version}/'
 ]
 
 "version.txt" = [
     '{version}'
 ]
 
 "docs/source/conf.py" = [
```

### Comparing `gofigr-0.10.4/tests/test_client.py` & `gofigr-0.10.5/tests/test_client.py`

 * *Files identical despite different names*

### Comparing `gofigr-0.10.4/tests/test_models.py` & `gofigr-0.10.5/tests/test_models.py`

 * *Files identical despite different names*

### Comparing `gofigr-0.10.4/tests/test_watermarks.py` & `gofigr-0.10.5/tests/test_watermarks.py`

 * *Files identical despite different names*

