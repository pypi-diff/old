# Comparing `tmp/fps_login-0.0.50.tar.gz` & `tmp/fps_login-0.1.2.tar.gz`

## Comparing `fps_login-0.0.50.tar` & `fps_login-0.1.2.tar`

### file list

```diff
@@ -1,19 +1,20 @@
--rw-r--r--   0        0        0       43 2020-02-02 00:00:00.000000 fps_login-0.0.50/MANIFEST.in
--rw-r--r--   0        0        0       23 2020-02-02 00:00:00.000000 fps_login-0.0.50/fps_login/__init__.py
--rw-r--r--   0        0        0      727 2020-02-02 00:00:00.000000 fps_login-0.0.50/fps_login/routes.py
--rw-r--r--   0        0        0     3104 2020-02-02 00:00:00.000000 fps_login-0.0.50/fps_login/static/index.html
--rw-r--r--   0        0        0     1150 2020-02-02 00:00:00.000000 fps_login-0.0.50/fps_login/static/favicons/favicon-busy-1.ico
--rw-r--r--   0        0        0     1150 2020-02-02 00:00:00.000000 fps_login-0.0.50/fps_login/static/favicons/favicon-busy-2.ico
--rw-r--r--   0        0        0     1150 2020-02-02 00:00:00.000000 fps_login-0.0.50/fps_login/static/favicons/favicon-busy-3.ico
--rw-r--r--   0        0        0     1150 2020-02-02 00:00:00.000000 fps_login-0.0.50/fps_login/static/favicons/favicon-file.ico
--rw-r--r--   0        0        0     1150 2020-02-02 00:00:00.000000 fps_login-0.0.50/fps_login/static/favicons/favicon-notebook.ico
--rw-r--r--   0        0        0     1150 2020-02-02 00:00:00.000000 fps_login-0.0.50/fps_login/static/favicons/favicon-terminal.ico
--rw-r--r--   0        0        0    32038 2020-02-02 00:00:00.000000 fps_login-0.0.50/fps_login/static/favicons/favicon.ico
--rw-r--r--   0        0        0     2798 2020-02-02 00:00:00.000000 fps_login-0.0.50/fps_login/static/logo/github.svg
--rw-r--r--   0        0        0     5922 2020-02-02 00:00:00.000000 fps_login-0.0.50/fps_login/static/logo/logo.png
--rw-r--r--   0        0        0     1408 2020-02-02 00:00:00.000000 fps_login-0.0.50/fps_login/static/style/index.css
--rw-r--r--   0        0        0     6359 2020-02-02 00:00:00.000000 fps_login-0.0.50/.gitignore
--rw-r--r--   0        0        0     2833 2020-02-02 00:00:00.000000 fps_login-0.0.50/COPYING.md
--rw-r--r--   0        0        0       46 2020-02-02 00:00:00.000000 fps_login-0.0.50/README.md
--rw-r--r--   0        0        0      769 2020-02-02 00:00:00.000000 fps_login-0.0.50/pyproject.toml
--rw-r--r--   0        0        0      443 2020-02-02 00:00:00.000000 fps_login-0.0.50/PKG-INFO
+-rw-r--r--   0        0        0       43 2020-02-02 00:00:00.000000 fps_login-0.1.2/MANIFEST.in
+-rw-r--r--   0        0        0       22 2020-02-02 00:00:00.000000 fps_login-0.1.2/fps_login/__init__.py
+-rw-r--r--   0        0        0      487 2020-02-02 00:00:00.000000 fps_login-0.1.2/fps_login/main.py
+-rw-r--r--   0        0        0     1072 2020-02-02 00:00:00.000000 fps_login-0.1.2/fps_login/routes.py
+-rw-r--r--   0        0        0     3104 2020-02-02 00:00:00.000000 fps_login-0.1.2/fps_login/static/index.html
+-rw-r--r--   0        0        0     1150 2020-02-02 00:00:00.000000 fps_login-0.1.2/fps_login/static/favicons/favicon-busy-1.ico
+-rw-r--r--   0        0        0     1150 2020-02-02 00:00:00.000000 fps_login-0.1.2/fps_login/static/favicons/favicon-busy-2.ico
+-rw-r--r--   0        0        0     1150 2020-02-02 00:00:00.000000 fps_login-0.1.2/fps_login/static/favicons/favicon-busy-3.ico
+-rw-r--r--   0        0        0     1150 2020-02-02 00:00:00.000000 fps_login-0.1.2/fps_login/static/favicons/favicon-file.ico
+-rw-r--r--   0        0        0     1150 2020-02-02 00:00:00.000000 fps_login-0.1.2/fps_login/static/favicons/favicon-notebook.ico
+-rw-r--r--   0        0        0     1150 2020-02-02 00:00:00.000000 fps_login-0.1.2/fps_login/static/favicons/favicon-terminal.ico
+-rw-r--r--   0        0        0    32038 2020-02-02 00:00:00.000000 fps_login-0.1.2/fps_login/static/favicons/favicon.ico
+-rw-r--r--   0        0        0     2798 2020-02-02 00:00:00.000000 fps_login-0.1.2/fps_login/static/logo/github.svg
+-rw-r--r--   0        0        0     5922 2020-02-02 00:00:00.000000 fps_login-0.1.2/fps_login/static/logo/logo.png
+-rw-r--r--   0        0        0     1408 2020-02-02 00:00:00.000000 fps_login-0.1.2/fps_login/static/style/index.css
+-rw-r--r--   0        0        0     6359 2020-02-02 00:00:00.000000 fps_login-0.1.2/.gitignore
+-rw-r--r--   0        0        0     2833 2020-02-02 00:00:00.000000 fps_login-0.1.2/COPYING.md
+-rw-r--r--   0        0        0       46 2020-02-02 00:00:00.000000 fps_login-0.1.2/README.md
+-rw-r--r--   0        0        0      854 2020-02-02 00:00:00.000000 fps_login-0.1.2/pyproject.toml
+-rw-r--r--   0        0        0      438 2020-02-02 00:00:00.000000 fps_login-0.1.2/PKG-INFO
```

### Comparing `fps_login-0.0.50/fps_login/static/index.html` & `fps_login-0.1.2/fps_login/static/index.html`

 * *Files identical despite different names*

### Comparing `fps_login-0.0.50/fps_login/static/favicons/favicon-busy-1.ico` & `fps_login-0.1.2/fps_login/static/favicons/favicon-busy-1.ico`

 * *Files identical despite different names*

### Comparing `fps_login-0.0.50/fps_login/static/favicons/favicon-busy-2.ico` & `fps_login-0.1.2/fps_login/static/favicons/favicon-busy-2.ico`

 * *Files identical despite different names*

### Comparing `fps_login-0.0.50/fps_login/static/favicons/favicon-busy-3.ico` & `fps_login-0.1.2/fps_login/static/favicons/favicon-busy-3.ico`

 * *Files identical despite different names*

### Comparing `fps_login-0.0.50/fps_login/static/favicons/favicon-file.ico` & `fps_login-0.1.2/fps_login/static/favicons/favicon-file.ico`

 * *Files identical despite different names*

### Comparing `fps_login-0.0.50/fps_login/static/favicons/favicon-notebook.ico` & `fps_login-0.1.2/fps_login/static/favicons/favicon-notebook.ico`

 * *Files identical despite different names*

### Comparing `fps_login-0.0.50/fps_login/static/favicons/favicon-terminal.ico` & `fps_login-0.1.2/fps_login/static/favicons/favicon-terminal.ico`

 * *Files identical despite different names*

### Comparing `fps_login-0.0.50/fps_login/static/favicons/favicon.ico` & `fps_login-0.1.2/fps_login/static/favicons/favicon.ico`

 * *Files identical despite different names*

### Comparing `fps_login-0.0.50/fps_login/static/logo/github.svg` & `fps_login-0.1.2/fps_login/static/logo/github.svg`

 * *Files identical despite different names*

### Comparing `fps_login-0.0.50/fps_login/static/logo/logo.png` & `fps_login-0.1.2/fps_login/static/logo/logo.png`

 * *Files identical despite different names*

### Comparing `fps_login-0.0.50/fps_login/static/style/index.css` & `fps_login-0.1.2/fps_login/static/style/index.css`

 * *Files identical despite different names*

### Comparing `fps_login-0.0.50/.gitignore` & `fps_login-0.1.2/.gitignore`

 * *Files identical despite different names*

### Comparing `fps_login-0.0.50/COPYING.md` & `fps_login-0.1.2/COPYING.md`

 * *Files identical despite different names*

### Comparing `fps_login-0.0.50/pyproject.toml` & `fps_login-0.1.2/pyproject.toml`

 * *Files 22% similar despite different names*

```diff
@@ -1,17 +1,19 @@
 [build-system]
 requires = [ "hatchling",]
 build-backend = "hatchling.build"
 
 [project]
 name = "fps_login"
 description = "An FPS plugin for the login API"
-keywords = [ "jupyter", "server", "fastapi", "pluggy", "plugins",]
+keywords = ["jupyter", "server", "fastapi", "plugins"]
 requires-python = ">=3.8"
-dependencies = [ "fps >=0.0.8",]
+dependencies = [
+  "jupyverse-api",
+]
 dynamic = [ "version",]
 [[project.authors]]
 name = "Jupyter Development Team"
 email = "jupyter@googlegroups.com"
 
 [project.readme]
 file = "README.md"
@@ -25,12 +27,13 @@
 
 [tool.check-manifest]
 ignore = [ ".*",]
 
 [tool.jupyter-releaser]
 skip = [ "check-links",]
 
-[project.entry-points.fps_router]
-fps-login = "fps_login.routes"
+[project.entry-points]
+"asphalt.components"   = {login = "fps_login.main:LoginComponent"}
+"jupyverse.components" = {login = "fps_login.main:LoginComponent"}
 
 [tool.hatch.version]
 path = "fps_login/__init__.py"
```

