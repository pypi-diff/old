# Comparing `tmp/jupyverse_api-0.0.50.tar.gz` & `tmp/jupyverse_api-0.1.2.tar.gz`

## Comparing `jupyverse_api-0.0.50.tar` & `jupyverse_api-0.1.2.tar`

### file list

```diff
@@ -1,25 +1,25 @@
--rw-r--r--   0        0        0      857 2020-02-02 00:00:00.000000 jupyverse_api-0.0.50/jupyverse_api/__init__.py
--rw-r--r--   0        0        0      348 2020-02-02 00:00:00.000000 jupyverse_api-0.0.50/jupyverse_api/exceptions.py
--rw-r--r--   0        0        0        0 2020-02-02 00:00:00.000000 jupyverse_api-0.0.50/jupyverse_api/py.typed
--rw-r--r--   0        0        0     1820 2020-02-02 00:00:00.000000 jupyverse_api-0.0.50/jupyverse_api/app/__init__.py
--rw-r--r--   0        0        0      612 2020-02-02 00:00:00.000000 jupyverse_api-0.0.50/jupyverse_api/auth/__init__.py
--rw-r--r--   0        0        0      308 2020-02-02 00:00:00.000000 jupyverse_api-0.0.50/jupyverse_api/auth/models.py
--rw-r--r--   0        0        0      854 2020-02-02 00:00:00.000000 jupyverse_api-0.0.50/jupyverse_api/contents/__init__.py
--rw-r--r--   0        0        0      474 2020-02-02 00:00:00.000000 jupyverse_api-0.0.50/jupyverse_api/contents/models.py
--rw-r--r--   0        0        0      121 2020-02-02 00:00:00.000000 jupyverse_api-0.0.50/jupyverse_api/frontend/__init__.py
--rw-r--r--   0        0        0      139 2020-02-02 00:00:00.000000 jupyverse_api-0.0.50/jupyverse_api/jupyterlab/__init__.py
--rw-r--r--   0        0        0      366 2020-02-02 00:00:00.000000 jupyverse_api-0.0.50/jupyverse_api/kernels/__init__.py
--rw-r--r--   0        0        0      622 2020-02-02 00:00:00.000000 jupyverse_api-0.0.50/jupyverse_api/kernels/models.py
--rw-r--r--   0        0        0      464 2020-02-02 00:00:00.000000 jupyverse_api-0.0.50/jupyverse_api/lab/__init__.py
--rw-r--r--   0        0        0       65 2020-02-02 00:00:00.000000 jupyverse_api-0.0.50/jupyverse_api/login/__init__.py
--rw-r--r--   0        0        0      506 2020-02-02 00:00:00.000000 jupyverse_api-0.0.50/jupyverse_api/main/__init__.py
--rw-r--r--   0        0        0       69 2020-02-02 00:00:00.000000 jupyverse_api-0.0.50/jupyverse_api/nbconvert/__init__.py
--rw-r--r--   0        0        0      270 2020-02-02 00:00:00.000000 jupyverse_api-0.0.50/jupyverse_api/resource_usage/__init__.py
--rw-r--r--   0        0        0       68 2020-02-02 00:00:00.000000 jupyverse_api-0.0.50/jupyverse_api/retrolab/__init__.py
--rw-r--r--   0        0        0      281 2020-02-02 00:00:00.000000 jupyverse_api-0.0.50/jupyverse_api/terminals/__init__.py
--rw-r--r--   0        0        0      110 2020-02-02 00:00:00.000000 jupyverse_api-0.0.50/jupyverse_api/yjs/__init__.py
--rw-r--r--   0        0        0     6359 2020-02-02 00:00:00.000000 jupyverse_api-0.0.50/.gitignore
--rw-r--r--   0        0        0     2833 2020-02-02 00:00:00.000000 jupyverse_api-0.0.50/COPYING.md
--rw-r--r--   0        0        0       47 2020-02-02 00:00:00.000000 jupyverse_api-0.0.50/README.md
--rw-r--r--   0        0        0     1104 2020-02-02 00:00:00.000000 jupyverse_api-0.0.50/pyproject.toml
--rw-r--r--   0        0        0      885 2020-02-02 00:00:00.000000 jupyverse_api-0.0.50/PKG-INFO
+-rw-r--r--   0        0        0      856 2020-02-02 00:00:00.000000 jupyverse_api-0.1.2/jupyverse_api/__init__.py
+-rw-r--r--   0        0        0      348 2020-02-02 00:00:00.000000 jupyverse_api-0.1.2/jupyverse_api/exceptions.py
+-rw-r--r--   0        0        0        0 2020-02-02 00:00:00.000000 jupyverse_api-0.1.2/jupyverse_api/py.typed
+-rw-r--r--   0        0        0     1820 2020-02-02 00:00:00.000000 jupyverse_api-0.1.2/jupyverse_api/app/__init__.py
+-rw-r--r--   0        0        0      612 2020-02-02 00:00:00.000000 jupyverse_api-0.1.2/jupyverse_api/auth/__init__.py
+-rw-r--r--   0        0        0      308 2020-02-02 00:00:00.000000 jupyverse_api-0.1.2/jupyverse_api/auth/models.py
+-rw-r--r--   0        0        0      854 2020-02-02 00:00:00.000000 jupyverse_api-0.1.2/jupyverse_api/contents/__init__.py
+-rw-r--r--   0        0        0      474 2020-02-02 00:00:00.000000 jupyverse_api-0.1.2/jupyverse_api/contents/models.py
+-rw-r--r--   0        0        0      121 2020-02-02 00:00:00.000000 jupyverse_api-0.1.2/jupyverse_api/frontend/__init__.py
+-rw-r--r--   0        0        0      139 2020-02-02 00:00:00.000000 jupyverse_api-0.1.2/jupyverse_api/jupyterlab/__init__.py
+-rw-r--r--   0        0        0      366 2020-02-02 00:00:00.000000 jupyverse_api-0.1.2/jupyverse_api/kernels/__init__.py
+-rw-r--r--   0        0        0      622 2020-02-02 00:00:00.000000 jupyverse_api-0.1.2/jupyverse_api/kernels/models.py
+-rw-r--r--   0        0        0      464 2020-02-02 00:00:00.000000 jupyverse_api-0.1.2/jupyverse_api/lab/__init__.py
+-rw-r--r--   0        0        0       65 2020-02-02 00:00:00.000000 jupyverse_api-0.1.2/jupyverse_api/login/__init__.py
+-rw-r--r--   0        0        0     2191 2020-02-02 00:00:00.000000 jupyverse_api-0.1.2/jupyverse_api/main/__init__.py
+-rw-r--r--   0        0        0       69 2020-02-02 00:00:00.000000 jupyverse_api-0.1.2/jupyverse_api/nbconvert/__init__.py
+-rw-r--r--   0        0        0      270 2020-02-02 00:00:00.000000 jupyverse_api-0.1.2/jupyverse_api/resource_usage/__init__.py
+-rw-r--r--   0        0        0       68 2020-02-02 00:00:00.000000 jupyverse_api-0.1.2/jupyverse_api/retrolab/__init__.py
+-rw-r--r--   0        0        0      281 2020-02-02 00:00:00.000000 jupyverse_api-0.1.2/jupyverse_api/terminals/__init__.py
+-rw-r--r--   0        0        0      110 2020-02-02 00:00:00.000000 jupyverse_api-0.1.2/jupyverse_api/yjs/__init__.py
+-rw-r--r--   0        0        0     6359 2020-02-02 00:00:00.000000 jupyverse_api-0.1.2/.gitignore
+-rw-r--r--   0        0        0     2833 2020-02-02 00:00:00.000000 jupyverse_api-0.1.2/COPYING.md
+-rw-r--r--   0        0        0       47 2020-02-02 00:00:00.000000 jupyverse_api-0.1.2/README.md
+-rw-r--r--   0        0        0     1191 2020-02-02 00:00:00.000000 jupyverse_api-0.1.2/pyproject.toml
+-rw-r--r--   0        0        0      884 2020-02-02 00:00:00.000000 jupyverse_api-0.1.2/PKG-INFO
```

### Comparing `jupyverse_api-0.0.50/jupyverse_api/__init__.py` & `jupyverse_api-0.1.2/jupyverse_api/__init__.py`

 * *Files 14% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 from typing import Dict
 
 from pydantic import BaseModel, Extra
 
 from .app import App
 
 
-__version__ = "0.0.50"
+__version__ = "0.1.2"
 
 
 class Singleton(type):
     _instances: Dict = {}
 
     def __call__(cls, *args, **kwargs):
         if cls not in cls._instances:
```

### Comparing `jupyverse_api-0.0.50/jupyverse_api/app/__init__.py` & `jupyverse_api-0.1.2/jupyverse_api/app/__init__.py`

 * *Files identical despite different names*

### Comparing `jupyverse_api-0.0.50/jupyverse_api/auth/__init__.py` & `jupyverse_api-0.1.2/jupyverse_api/auth/__init__.py`

 * *Files identical despite different names*

### Comparing `jupyverse_api-0.0.50/jupyverse_api/contents/__init__.py` & `jupyverse_api-0.1.2/jupyverse_api/contents/__init__.py`

 * *Files identical despite different names*

### Comparing `jupyverse_api-0.0.50/jupyverse_api/kernels/models.py` & `jupyverse_api-0.1.2/jupyverse_api/kernels/models.py`

 * *Files identical despite different names*

### Comparing `jupyverse_api-0.0.50/.gitignore` & `jupyverse_api-0.1.2/.gitignore`

 * *Files identical despite different names*

### Comparing `jupyverse_api-0.0.50/COPYING.md` & `jupyverse_api-0.1.2/COPYING.md`

 * *Files identical despite different names*

### Comparing `jupyverse_api-0.0.50/pyproject.toml` & `jupyverse_api-0.1.2/pyproject.toml`

 * *Files 11% similar despite different names*

```diff
@@ -34,9 +34,12 @@
 [project.urls]
 Source = "https://github.com/jupyter-server/jupyverse/api"
 
 [project.entry-points."asphalt.components"]
 app = "jupyverse_api.main:AppComponent"
 jupyverse = "jupyverse_api.main:JupyverseComponent"
 
+[project.entry-points."jupyverse.components"]
+app = "jupyverse_api.main:AppComponent"
+
 [tool.hatch.version]
 path = "jupyverse_api/__init__.py"
```

### Comparing `jupyverse_api-0.0.50/PKG-INFO` & `jupyverse_api-0.1.2/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: jupyverse_api
-Version: 0.0.50
+Version: 0.1.2
 Summary: The public API for Jupyverse
 Project-URL: Source, https://github.com/jupyter-server/jupyverse/api
 Author-email: Jupyter Development Team <jupyter@googlegroups.com>
 License: BSD 3-Clause License
 License-File: COPYING.md
 Keywords: api,jupyverse
 Classifier: Development Status :: 4 - Beta
```

