# Comparing `tmp/fps_login-0.1.2.tar.gz` & `tmp/fps_login-0.1.3.tar.gz`

## Comparing `fps_login-0.1.2.tar` & `fps_login-0.1.3.tar`

### file list

```diff
@@ -1,20 +1,20 @@
--rw-r--r--   0        0        0       43 2020-02-02 00:00:00.000000 fps_login-0.1.2/MANIFEST.in
--rw-r--r--   0        0        0       22 2020-02-02 00:00:00.000000 fps_login-0.1.2/fps_login/__init__.py
--rw-r--r--   0        0        0      487 2020-02-02 00:00:00.000000 fps_login-0.1.2/fps_login/main.py
--rw-r--r--   0        0        0     1072 2020-02-02 00:00:00.000000 fps_login-0.1.2/fps_login/routes.py
--rw-r--r--   0        0        0     3104 2020-02-02 00:00:00.000000 fps_login-0.1.2/fps_login/static/index.html
--rw-r--r--   0        0        0     1150 2020-02-02 00:00:00.000000 fps_login-0.1.2/fps_login/static/favicons/favicon-busy-1.ico
--rw-r--r--   0        0        0     1150 2020-02-02 00:00:00.000000 fps_login-0.1.2/fps_login/static/favicons/favicon-busy-2.ico
--rw-r--r--   0        0        0     1150 2020-02-02 00:00:00.000000 fps_login-0.1.2/fps_login/static/favicons/favicon-busy-3.ico
--rw-r--r--   0        0        0     1150 2020-02-02 00:00:00.000000 fps_login-0.1.2/fps_login/static/favicons/favicon-file.ico
--rw-r--r--   0        0        0     1150 2020-02-02 00:00:00.000000 fps_login-0.1.2/fps_login/static/favicons/favicon-notebook.ico
--rw-r--r--   0        0        0     1150 2020-02-02 00:00:00.000000 fps_login-0.1.2/fps_login/static/favicons/favicon-terminal.ico
--rw-r--r--   0        0        0    32038 2020-02-02 00:00:00.000000 fps_login-0.1.2/fps_login/static/favicons/favicon.ico
--rw-r--r--   0        0        0     2798 2020-02-02 00:00:00.000000 fps_login-0.1.2/fps_login/static/logo/github.svg
--rw-r--r--   0        0        0     5922 2020-02-02 00:00:00.000000 fps_login-0.1.2/fps_login/static/logo/logo.png
--rw-r--r--   0        0        0     1408 2020-02-02 00:00:00.000000 fps_login-0.1.2/fps_login/static/style/index.css
--rw-r--r--   0        0        0     6359 2020-02-02 00:00:00.000000 fps_login-0.1.2/.gitignore
--rw-r--r--   0        0        0     2833 2020-02-02 00:00:00.000000 fps_login-0.1.2/COPYING.md
--rw-r--r--   0        0        0       46 2020-02-02 00:00:00.000000 fps_login-0.1.2/README.md
--rw-r--r--   0        0        0      854 2020-02-02 00:00:00.000000 fps_login-0.1.2/pyproject.toml
--rw-r--r--   0        0        0      438 2020-02-02 00:00:00.000000 fps_login-0.1.2/PKG-INFO
+-rw-r--r--   0        0        0       43 2020-02-02 00:00:00.000000 fps_login-0.1.3/MANIFEST.in
+-rw-r--r--   0        0        0       22 2020-02-02 00:00:00.000000 fps_login-0.1.3/fps_login/__init__.py
+-rw-r--r--   0        0        0      487 2020-02-02 00:00:00.000000 fps_login-0.1.3/fps_login/main.py
+-rw-r--r--   0        0        0     1072 2020-02-02 00:00:00.000000 fps_login-0.1.3/fps_login/routes.py
+-rw-r--r--   0        0        0     3104 2020-02-02 00:00:00.000000 fps_login-0.1.3/fps_login/static/index.html
+-rw-r--r--   0        0        0     1150 2020-02-02 00:00:00.000000 fps_login-0.1.3/fps_login/static/favicons/favicon-busy-1.ico
+-rw-r--r--   0        0        0     1150 2020-02-02 00:00:00.000000 fps_login-0.1.3/fps_login/static/favicons/favicon-busy-2.ico
+-rw-r--r--   0        0        0     1150 2020-02-02 00:00:00.000000 fps_login-0.1.3/fps_login/static/favicons/favicon-busy-3.ico
+-rw-r--r--   0        0        0     1150 2020-02-02 00:00:00.000000 fps_login-0.1.3/fps_login/static/favicons/favicon-file.ico
+-rw-r--r--   0        0        0     1150 2020-02-02 00:00:00.000000 fps_login-0.1.3/fps_login/static/favicons/favicon-notebook.ico
+-rw-r--r--   0        0        0     1150 2020-02-02 00:00:00.000000 fps_login-0.1.3/fps_login/static/favicons/favicon-terminal.ico
+-rw-r--r--   0        0        0    32038 2020-02-02 00:00:00.000000 fps_login-0.1.3/fps_login/static/favicons/favicon.ico
+-rw-r--r--   0        0        0     2798 2020-02-02 00:00:00.000000 fps_login-0.1.3/fps_login/static/logo/github.svg
+-rw-r--r--   0        0        0     5922 2020-02-02 00:00:00.000000 fps_login-0.1.3/fps_login/static/logo/logo.png
+-rw-r--r--   0        0        0     1408 2020-02-02 00:00:00.000000 fps_login-0.1.3/fps_login/static/style/index.css
+-rw-r--r--   0        0        0     6359 2020-02-02 00:00:00.000000 fps_login-0.1.3/.gitignore
+-rw-r--r--   0        0        0     2833 2020-02-02 00:00:00.000000 fps_login-0.1.3/COPYING.md
+-rw-r--r--   0        0        0       46 2020-02-02 00:00:00.000000 fps_login-0.1.3/README.md
+-rw-r--r--   0        0        0      865 2020-02-02 00:00:00.000000 fps_login-0.1.3/pyproject.toml
+-rw-r--r--   0        0        0      448 2020-02-02 00:00:00.000000 fps_login-0.1.3/PKG-INFO
```

### Comparing `fps_login-0.1.2/fps_login/routes.py` & `fps_login-0.1.3/fps_login/routes.py`

 * *Files identical despite different names*

### Comparing `fps_login-0.1.2/fps_login/static/index.html` & `fps_login-0.1.3/fps_login/static/index.html`

 * *Files identical despite different names*

### Comparing `fps_login-0.1.2/fps_login/static/favicons/favicon-busy-1.ico` & `fps_login-0.1.3/fps_login/static/favicons/favicon-busy-1.ico`

 * *Files identical despite different names*

### Comparing `fps_login-0.1.2/fps_login/static/favicons/favicon-busy-2.ico` & `fps_login-0.1.3/fps_login/static/favicons/favicon-busy-2.ico`

 * *Files identical despite different names*

### Comparing `fps_login-0.1.2/fps_login/static/favicons/favicon-busy-3.ico` & `fps_login-0.1.3/fps_login/static/favicons/favicon-busy-3.ico`

 * *Files identical despite different names*

### Comparing `fps_login-0.1.2/fps_login/static/favicons/favicon-file.ico` & `fps_login-0.1.3/fps_login/static/favicons/favicon-file.ico`

 * *Files identical despite different names*

### Comparing `fps_login-0.1.2/fps_login/static/favicons/favicon-notebook.ico` & `fps_login-0.1.3/fps_login/static/favicons/favicon-notebook.ico`

 * *Files identical despite different names*

### Comparing `fps_login-0.1.2/fps_login/static/favicons/favicon-terminal.ico` & `fps_login-0.1.3/fps_login/static/favicons/favicon-terminal.ico`

 * *Files identical despite different names*

### Comparing `fps_login-0.1.2/fps_login/static/favicons/favicon.ico` & `fps_login-0.1.3/fps_login/static/favicons/favicon.ico`

 * *Files identical despite different names*

### Comparing `fps_login-0.1.2/fps_login/static/logo/github.svg` & `fps_login-0.1.3/fps_login/static/logo/github.svg`

 * *Files identical despite different names*

### Comparing `fps_login-0.1.2/fps_login/static/logo/logo.png` & `fps_login-0.1.3/fps_login/static/logo/logo.png`

 * *Files identical despite different names*

### Comparing `fps_login-0.1.2/fps_login/static/style/index.css` & `fps_login-0.1.3/fps_login/static/style/index.css`

 * *Files identical despite different names*

### Comparing `fps_login-0.1.2/.gitignore` & `fps_login-0.1.3/.gitignore`

 * *Files identical despite different names*

### Comparing `fps_login-0.1.2/COPYING.md` & `fps_login-0.1.3/COPYING.md`

 * *Files identical despite different names*

### Comparing `fps_login-0.1.2/pyproject.toml` & `fps_login-0.1.3/pyproject.toml`

 * *Files 22% similar despite different names*

```diff
@@ -4,15 +4,15 @@
 
 [project]
 name = "fps_login"
 description = "An FPS plugin for the login API"
 keywords = ["jupyter", "server", "fastapi", "plugins"]
 requires-python = ">=3.8"
 dependencies = [
-  "jupyverse-api",
+  "jupyverse-api >=0.1.2,<1",
 ]
 dynamic = [ "version",]
 [[project.authors]]
 name = "Jupyter Development Team"
 email = "jupyter@googlegroups.com"
 
 [project.readme]
```

