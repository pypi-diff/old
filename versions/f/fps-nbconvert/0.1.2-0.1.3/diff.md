# Comparing `tmp/fps_nbconvert-0.1.2.tar.gz` & `tmp/fps_nbconvert-0.1.3.tar.gz`

## Comparing `fps_nbconvert-0.1.2.tar` & `fps_nbconvert-0.1.3.tar`

### file list

```diff
@@ -1,9 +1,9 @@
--rw-r--r--   0        0        0       13 2020-02-02 00:00:00.000000 fps_nbconvert-0.1.2/MANIFEST.in
--rw-r--r--   0        0        0       22 2020-02-02 00:00:00.000000 fps_nbconvert-0.1.2/fps_nbconvert/__init__.py
--rw-r--r--   0        0        0      509 2020-02-02 00:00:00.000000 fps_nbconvert-0.1.2/fps_nbconvert/main.py
--rw-r--r--   0        0        0     1563 2020-02-02 00:00:00.000000 fps_nbconvert-0.1.2/fps_nbconvert/routes.py
--rw-r--r--   0        0        0     6359 2020-02-02 00:00:00.000000 fps_nbconvert-0.1.2/.gitignore
--rw-r--r--   0        0        0     2833 2020-02-02 00:00:00.000000 fps_nbconvert-0.1.2/COPYING.md
--rw-r--r--   0        0        0       54 2020-02-02 00:00:00.000000 fps_nbconvert-0.1.2/README.md
--rw-r--r--   0        0        0      909 2020-02-02 00:00:00.000000 fps_nbconvert-0.1.2/pyproject.toml
--rw-r--r--   0        0        0      479 2020-02-02 00:00:00.000000 fps_nbconvert-0.1.2/PKG-INFO
+-rw-r--r--   0        0        0       13 2020-02-02 00:00:00.000000 fps_nbconvert-0.1.3/MANIFEST.in
+-rw-r--r--   0        0        0       22 2020-02-02 00:00:00.000000 fps_nbconvert-0.1.3/fps_nbconvert/__init__.py
+-rw-r--r--   0        0        0      509 2020-02-02 00:00:00.000000 fps_nbconvert-0.1.3/fps_nbconvert/main.py
+-rw-r--r--   0        0        0     1563 2020-02-02 00:00:00.000000 fps_nbconvert-0.1.3/fps_nbconvert/routes.py
+-rw-r--r--   0        0        0     6359 2020-02-02 00:00:00.000000 fps_nbconvert-0.1.3/.gitignore
+-rw-r--r--   0        0        0     2833 2020-02-02 00:00:00.000000 fps_nbconvert-0.1.3/COPYING.md
+-rw-r--r--   0        0        0       54 2020-02-02 00:00:00.000000 fps_nbconvert-0.1.3/README.md
+-rw-r--r--   0        0        0      920 2020-02-02 00:00:00.000000 fps_nbconvert-0.1.3/pyproject.toml
+-rw-r--r--   0        0        0      489 2020-02-02 00:00:00.000000 fps_nbconvert-0.1.3/PKG-INFO
```

### Comparing `fps_nbconvert-0.1.2/fps_nbconvert/routes.py` & `fps_nbconvert-0.1.3/fps_nbconvert/routes.py`

 * *Files identical despite different names*

### Comparing `fps_nbconvert-0.1.2/.gitignore` & `fps_nbconvert-0.1.3/.gitignore`

 * *Files identical despite different names*

### Comparing `fps_nbconvert-0.1.2/COPYING.md` & `fps_nbconvert-0.1.3/COPYING.md`

 * *Files identical despite different names*

### Comparing `fps_nbconvert-0.1.2/pyproject.toml` & `fps_nbconvert-0.1.3/pyproject.toml`

 * *Files 11% similar despite different names*

```diff
@@ -5,15 +5,15 @@
 [project]
 name = "fps_nbconvert"
 description = "An FPS plugin for the nbconvert API"
 keywords = ["jupyter", "server", "fastapi", "plugins"]
 requires-python = ">=3.8"
 dependencies = [
     "nbconvert",
-    "jupyverse-api",
+    "jupyverse-api >=0.1.2,<1",
 ]
 dynamic = [ "version",]
 [[project.authors]]
 name = "Jupyter Development Team"
 email = "jupyter@googlegroups.com"
 
 [project.readme]
```

