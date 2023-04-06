# Comparing `tmp/fps_resource_usage-0.1.2.tar.gz` & `tmp/fps_resource_usage-0.1.3.tar.gz`

## Comparing `fps_resource_usage-0.1.2.tar` & `fps_resource_usage-0.1.3.tar`

### file list

```diff
@@ -1,8 +1,8 @@
--rw-r--r--   0        0        0       22 2020-02-02 00:00:00.000000 fps_resource_usage-0.1.2/fps_resource_usage/__init__.py
--rw-r--r--   0        0        0      695 2020-02-02 00:00:00.000000 fps_resource_usage-0.1.2/fps_resource_usage/main.py
--rw-r--r--   0        0        0     2620 2020-02-02 00:00:00.000000 fps_resource_usage-0.1.2/fps_resource_usage/routes.py
--rw-r--r--   0        0        0     6359 2020-02-02 00:00:00.000000 fps_resource_usage-0.1.2/.gitignore
--rw-r--r--   0        0        0     2833 2020-02-02 00:00:00.000000 fps_resource_usage-0.1.2/COPYING.md
--rw-r--r--   0        0        0       64 2020-02-02 00:00:00.000000 fps_resource_usage-0.1.2/README.md
--rw-r--r--   0        0        0      998 2020-02-02 00:00:00.000000 fps_resource_usage-0.1.2/pyproject.toml
--rw-r--r--   0        0        0      559 2020-02-02 00:00:00.000000 fps_resource_usage-0.1.2/PKG-INFO
+-rw-r--r--   0        0        0       22 2020-02-02 00:00:00.000000 fps_resource_usage-0.1.3/fps_resource_usage/__init__.py
+-rw-r--r--   0        0        0      695 2020-02-02 00:00:00.000000 fps_resource_usage-0.1.3/fps_resource_usage/main.py
+-rw-r--r--   0        0        0     2620 2020-02-02 00:00:00.000000 fps_resource_usage-0.1.3/fps_resource_usage/routes.py
+-rw-r--r--   0        0        0     6359 2020-02-02 00:00:00.000000 fps_resource_usage-0.1.3/.gitignore
+-rw-r--r--   0        0        0     2833 2020-02-02 00:00:00.000000 fps_resource_usage-0.1.3/COPYING.md
+-rw-r--r--   0        0        0       64 2020-02-02 00:00:00.000000 fps_resource_usage-0.1.3/README.md
+-rw-r--r--   0        0        0     1009 2020-02-02 00:00:00.000000 fps_resource_usage-0.1.3/pyproject.toml
+-rw-r--r--   0        0        0      569 2020-02-02 00:00:00.000000 fps_resource_usage-0.1.3/PKG-INFO
```

### Comparing `fps_resource_usage-0.1.2/fps_resource_usage/main.py` & `fps_resource_usage-0.1.3/fps_resource_usage/main.py`

 * *Files identical despite different names*

### Comparing `fps_resource_usage-0.1.2/fps_resource_usage/routes.py` & `fps_resource_usage-0.1.3/fps_resource_usage/routes.py`

 * *Files identical despite different names*

### Comparing `fps_resource_usage-0.1.2/.gitignore` & `fps_resource_usage-0.1.3/.gitignore`

 * *Files identical despite different names*

### Comparing `fps_resource_usage-0.1.2/COPYING.md` & `fps_resource_usage-0.1.3/COPYING.md`

 * *Files identical despite different names*

### Comparing `fps_resource_usage-0.1.2/pyproject.toml` & `fps_resource_usage-0.1.3/pyproject.toml`

 * *Files 12% similar despite different names*

```diff
@@ -7,15 +7,15 @@
 description = "An FPS plugin for the resource usage API"
 keywords = ["jupyter", "server", "fastapi", "plugins"]
 requires-python = ">=3.8"
 dependencies = [
     "psutil >=5.9.4",
     "types-psutil",
     "anyio >=3.6.2",
-    "jupyverse-api",
+    "jupyverse-api >=0.1.2,<1",
 ]
 dynamic = [ "version",]
 [[project.authors]]
 name = "Jupyter Development Team"
 email = "jupyter@googlegroups.com"
 
 [project.readme]
```

### Comparing `fps_resource_usage-0.1.2/PKG-INFO` & `fps_resource_usage-0.1.3/PKG-INFO`

 * *Files 3% similar despite different names*

```diff
@@ -1,19 +1,19 @@
 Metadata-Version: 2.1
 Name: fps_resource_usage
-Version: 0.1.2
+Version: 0.1.3
 Summary: An FPS plugin for the resource usage API
 Project-URL: Homepage, https://jupyter.org
 Author-email: Jupyter Development Team <jupyter@googlegroups.com>
 License: BSD 3-Clause License
 License-File: COPYING.md
 Keywords: fastapi,jupyter,plugins,server
 Requires-Python: >=3.8
 Requires-Dist: anyio>=3.6.2
-Requires-Dist: jupyverse-api
+Requires-Dist: jupyverse-api<1,>=0.1.2
 Requires-Dist: psutil>=5.9.4
 Requires-Dist: types-psutil
 Description-Content-Type: text/markdown
 
 # fps-resource-usage
 
 An FPS plugin for the resource usage API.
```

