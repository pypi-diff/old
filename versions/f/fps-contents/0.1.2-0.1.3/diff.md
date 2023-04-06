# Comparing `tmp/fps_contents-0.1.2.tar.gz` & `tmp/fps_contents-0.1.3.tar.gz`

## Comparing `fps_contents-0.1.2.tar` & `fps_contents-0.1.3.tar`

### file list

```diff
@@ -1,12 +1,12 @@
--rw-r--r--   0        0        0       13 2020-02-02 00:00:00.000000 fps_contents-0.1.2/MANIFEST.in
--rw-r--r--   0        0        0       22 2020-02-02 00:00:00.000000 fps_contents-0.1.2/fps_contents/__init__.py
--rw-r--r--   0        0        0     8386 2020-02-02 00:00:00.000000 fps_contents-0.1.2/fps_contents/fileid.py
--rw-r--r--   0        0        0      501 2020-02-02 00:00:00.000000 fps_contents-0.1.2/fps_contents/main.py
--rw-r--r--   0        0        0      259 2020-02-02 00:00:00.000000 fps_contents-0.1.2/fps_contents/models.py
--rw-r--r--   0        0        0        0 2020-02-02 00:00:00.000000 fps_contents-0.1.2/fps_contents/py.typed
--rw-r--r--   0        0        0    10716 2020-02-02 00:00:00.000000 fps_contents-0.1.2/fps_contents/routes.py
--rw-r--r--   0        0        0     6359 2020-02-02 00:00:00.000000 fps_contents-0.1.2/.gitignore
--rw-r--r--   0        0        0     2833 2020-02-02 00:00:00.000000 fps_contents-0.1.2/COPYING.md
--rw-r--r--   0        0        0       52 2020-02-02 00:00:00.000000 fps_contents-0.1.2/README.md
--rw-r--r--   0        0        0      965 2020-02-02 00:00:00.000000 fps_contents-0.1.2/pyproject.toml
--rw-r--r--   0        0        0      554 2020-02-02 00:00:00.000000 fps_contents-0.1.2/PKG-INFO
+-rw-r--r--   0        0        0       13 2020-02-02 00:00:00.000000 fps_contents-0.1.3/MANIFEST.in
+-rw-r--r--   0        0        0       22 2020-02-02 00:00:00.000000 fps_contents-0.1.3/fps_contents/__init__.py
+-rw-r--r--   0        0        0     8386 2020-02-02 00:00:00.000000 fps_contents-0.1.3/fps_contents/fileid.py
+-rw-r--r--   0        0        0      501 2020-02-02 00:00:00.000000 fps_contents-0.1.3/fps_contents/main.py
+-rw-r--r--   0        0        0      259 2020-02-02 00:00:00.000000 fps_contents-0.1.3/fps_contents/models.py
+-rw-r--r--   0        0        0        0 2020-02-02 00:00:00.000000 fps_contents-0.1.3/fps_contents/py.typed
+-rw-r--r--   0        0        0    10716 2020-02-02 00:00:00.000000 fps_contents-0.1.3/fps_contents/routes.py
+-rw-r--r--   0        0        0     6359 2020-02-02 00:00:00.000000 fps_contents-0.1.3/.gitignore
+-rw-r--r--   0        0        0     2833 2020-02-02 00:00:00.000000 fps_contents-0.1.3/COPYING.md
+-rw-r--r--   0        0        0       52 2020-02-02 00:00:00.000000 fps_contents-0.1.3/README.md
+-rw-r--r--   0        0        0      976 2020-02-02 00:00:00.000000 fps_contents-0.1.3/pyproject.toml
+-rw-r--r--   0        0        0      564 2020-02-02 00:00:00.000000 fps_contents-0.1.3/PKG-INFO
```

### Comparing `fps_contents-0.1.2/fps_contents/fileid.py` & `fps_contents-0.1.3/fps_contents/fileid.py`

 * *Files identical despite different names*

### Comparing `fps_contents-0.1.2/fps_contents/routes.py` & `fps_contents-0.1.3/fps_contents/routes.py`

 * *Files identical despite different names*

### Comparing `fps_contents-0.1.2/.gitignore` & `fps_contents-0.1.3/.gitignore`

 * *Files identical despite different names*

### Comparing `fps_contents-0.1.2/COPYING.md` & `fps_contents-0.1.3/COPYING.md`

 * *Files identical despite different names*

### Comparing `fps_contents-0.1.2/pyproject.toml` & `fps_contents-0.1.3/pyproject.toml`

 * *Files 2% similar despite different names*

```diff
@@ -7,15 +7,15 @@
 description = "An FPS plugin for the contents API"
 keywords = ["jupyter", "server", "fastapi", "plugins"]
 requires-python = ">=3.8"
 dependencies = [
     "watchfiles >=0.18.1,<1",
     "aiosqlite >=0.17.0,<1",
     "anyio>=3.6.2,<4",
-    "jupyverse-api",
+    "jupyverse-api >=0.1.2,<1",
 ]
 dynamic = [ "version",]
 [[project.authors]]
 name = "Jupyter Development Team"
 email = "jupyter@googlegroups.com"
 
 [project.readme]
```

### Comparing `fps_contents-0.1.2/PKG-INFO` & `fps_contents-0.1.3/PKG-INFO`

 * *Files 14% similar despite different names*

```diff
@@ -1,19 +1,19 @@
 Metadata-Version: 2.1
 Name: fps_contents
-Version: 0.1.2
+Version: 0.1.3
 Summary: An FPS plugin for the contents API
 Project-URL: Homepage, https://jupyter.org
 Author-email: Jupyter Development Team <jupyter@googlegroups.com>
 License: BSD 3-Clause License
 License-File: COPYING.md
 Keywords: fastapi,jupyter,plugins,server
 Requires-Python: >=3.8
 Requires-Dist: aiosqlite<1,>=0.17.0
 Requires-Dist: anyio<4,>=3.6.2
-Requires-Dist: jupyverse-api
+Requires-Dist: jupyverse-api<1,>=0.1.2
 Requires-Dist: watchfiles<1,>=0.18.1
 Description-Content-Type: text/markdown
 
 # fps-contents
 
 An FPS plugin for the contents API.
```

