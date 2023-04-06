# Comparing `tmp/fps_retrolab-0.1.2.tar.gz` & `tmp/fps_retrolab-0.1.3.tar.gz`

## Comparing `fps_retrolab-0.1.2.tar` & `fps_retrolab-0.1.3.tar`

### file list

```diff
@@ -1,9 +1,9 @@
--rw-r--r--   0        0        0       13 2020-02-02 00:00:00.000000 fps_retrolab-0.1.2/MANIFEST.in
--rw-r--r--   0        0        0       22 2020-02-02 00:00:00.000000 fps_retrolab-0.1.2/fps_retrolab/__init__.py
--rw-r--r--   0        0        0      738 2020-02-02 00:00:00.000000 fps_retrolab-0.1.2/fps_retrolab/main.py
--rw-r--r--   0        0        0     6717 2020-02-02 00:00:00.000000 fps_retrolab-0.1.2/fps_retrolab/routes.py
--rw-r--r--   0        0        0     6359 2020-02-02 00:00:00.000000 fps_retrolab-0.1.2/.gitignore
--rw-r--r--   0        0        0     2833 2020-02-02 00:00:00.000000 fps_retrolab-0.1.2/COPYING.md
--rw-r--r--   0        0        0       52 2020-02-02 00:00:00.000000 fps_retrolab-0.1.2/README.md
--rw-r--r--   0        0        0      899 2020-02-02 00:00:00.000000 fps_retrolab-0.1.2/pyproject.toml
--rw-r--r--   0        0        0      474 2020-02-02 00:00:00.000000 fps_retrolab-0.1.2/PKG-INFO
+-rw-r--r--   0        0        0       13 2020-02-02 00:00:00.000000 fps_retrolab-0.1.3/MANIFEST.in
+-rw-r--r--   0        0        0       22 2020-02-02 00:00:00.000000 fps_retrolab-0.1.3/fps_retrolab/__init__.py
+-rw-r--r--   0        0        0      738 2020-02-02 00:00:00.000000 fps_retrolab-0.1.3/fps_retrolab/main.py
+-rw-r--r--   0        0        0     6717 2020-02-02 00:00:00.000000 fps_retrolab-0.1.3/fps_retrolab/routes.py
+-rw-r--r--   0        0        0     6359 2020-02-02 00:00:00.000000 fps_retrolab-0.1.3/.gitignore
+-rw-r--r--   0        0        0     2833 2020-02-02 00:00:00.000000 fps_retrolab-0.1.3/COPYING.md
+-rw-r--r--   0        0        0       52 2020-02-02 00:00:00.000000 fps_retrolab-0.1.3/README.md
+-rw-r--r--   0        0        0      910 2020-02-02 00:00:00.000000 fps_retrolab-0.1.3/pyproject.toml
+-rw-r--r--   0        0        0      484 2020-02-02 00:00:00.000000 fps_retrolab-0.1.3/PKG-INFO
```

### Comparing `fps_retrolab-0.1.2/fps_retrolab/main.py` & `fps_retrolab-0.1.3/fps_retrolab/main.py`

 * *Files identical despite different names*

### Comparing `fps_retrolab-0.1.2/fps_retrolab/routes.py` & `fps_retrolab-0.1.3/fps_retrolab/routes.py`

 * *Files identical despite different names*

### Comparing `fps_retrolab-0.1.2/.gitignore` & `fps_retrolab-0.1.3/.gitignore`

 * *Files identical despite different names*

### Comparing `fps_retrolab-0.1.2/COPYING.md` & `fps_retrolab-0.1.3/COPYING.md`

 * *Files identical despite different names*

### Comparing `fps_retrolab-0.1.2/pyproject.toml` & `fps_retrolab-0.1.3/pyproject.toml`

 * *Files 1% similar despite different names*

```diff
@@ -5,15 +5,15 @@
 [project]
 name = "fps_retrolab"
 description = "An FPS plugin for the RetroLab API"
 keywords = ["jupyter", "server", "fastapi", "plugins"]
 requires-python = ">=3.8"
 dependencies = [
     "retrolab",
-    "jupyverse-api",
+    "jupyverse-api >=0.1.2,<1",
 ]
 dynamic = [ "version",]
 [[project.authors]]
 name = "Jupyter Development Team"
 email = "jupyter@googlegroups.com"
 
 [project.readme]
```

