# Comparing `tmp/fps_auth-0.1.2.tar.gz` & `tmp/fps_auth-0.1.3.tar.gz`

## Comparing `fps_auth-0.1.2.tar` & `fps_auth-0.1.3.tar`

### file list

```diff
@@ -1,14 +1,14 @@
--rw-r--r--   0        0        0       13 2020-02-02 00:00:00.000000 fps_auth-0.1.2/MANIFEST.in
--rw-r--r--   0        0        0       22 2020-02-02 00:00:00.000000 fps_auth-0.1.2/fps_auth/__init__.py
--rw-r--r--   0        0        0    10954 2020-02-02 00:00:00.000000 fps_auth-0.1.2/fps_auth/backends.py
--rw-r--r--   0        0        0      542 2020-02-02 00:00:00.000000 fps_auth-0.1.2/fps_auth/config.py
--rw-r--r--   0        0        0     3281 2020-02-02 00:00:00.000000 fps_auth-0.1.2/fps_auth/db.py
--rw-r--r--   0        0        0     2229 2020-02-02 00:00:00.000000 fps_auth-0.1.2/fps_auth/main.py
--rw-r--r--   0        0        0      406 2020-02-02 00:00:00.000000 fps_auth-0.1.2/fps_auth/models.py
--rw-r--r--   0        0        0        0 2020-02-02 00:00:00.000000 fps_auth-0.1.2/fps_auth/py.typed
--rw-r--r--   0        0        0     5837 2020-02-02 00:00:00.000000 fps_auth-0.1.2/fps_auth/routes.py
--rw-r--r--   0        0        0     6359 2020-02-02 00:00:00.000000 fps_auth-0.1.2/.gitignore
--rw-r--r--   0        0        0     2833 2020-02-02 00:00:00.000000 fps_auth-0.1.2/COPYING.md
--rw-r--r--   0        0        0       54 2020-02-02 00:00:00.000000 fps_auth-0.1.2/README.md
--rw-r--r--   0        0        0      950 2020-02-02 00:00:00.000000 fps_auth-0.1.2/pyproject.toml
--rw-r--r--   0        0        0      570 2020-02-02 00:00:00.000000 fps_auth-0.1.2/PKG-INFO
+-rw-r--r--   0        0        0       13 2020-02-02 00:00:00.000000 fps_auth-0.1.3/MANIFEST.in
+-rw-r--r--   0        0        0       22 2020-02-02 00:00:00.000000 fps_auth-0.1.3/fps_auth/__init__.py
+-rw-r--r--   0        0        0    10954 2020-02-02 00:00:00.000000 fps_auth-0.1.3/fps_auth/backends.py
+-rw-r--r--   0        0        0      542 2020-02-02 00:00:00.000000 fps_auth-0.1.3/fps_auth/config.py
+-rw-r--r--   0        0        0     3281 2020-02-02 00:00:00.000000 fps_auth-0.1.3/fps_auth/db.py
+-rw-r--r--   0        0        0     2229 2020-02-02 00:00:00.000000 fps_auth-0.1.3/fps_auth/main.py
+-rw-r--r--   0        0        0      406 2020-02-02 00:00:00.000000 fps_auth-0.1.3/fps_auth/models.py
+-rw-r--r--   0        0        0        0 2020-02-02 00:00:00.000000 fps_auth-0.1.3/fps_auth/py.typed
+-rw-r--r--   0        0        0     5837 2020-02-02 00:00:00.000000 fps_auth-0.1.3/fps_auth/routes.py
+-rw-r--r--   0        0        0     6359 2020-02-02 00:00:00.000000 fps_auth-0.1.3/.gitignore
+-rw-r--r--   0        0        0     2833 2020-02-02 00:00:00.000000 fps_auth-0.1.3/COPYING.md
+-rw-r--r--   0        0        0       54 2020-02-02 00:00:00.000000 fps_auth-0.1.3/README.md
+-rw-r--r--   0        0        0      961 2020-02-02 00:00:00.000000 fps_auth-0.1.3/pyproject.toml
+-rw-r--r--   0        0        0      580 2020-02-02 00:00:00.000000 fps_auth-0.1.3/PKG-INFO
```

### Comparing `fps_auth-0.1.2/fps_auth/backends.py` & `fps_auth-0.1.3/fps_auth/backends.py`

 * *Files identical despite different names*

### Comparing `fps_auth-0.1.2/fps_auth/config.py` & `fps_auth-0.1.3/fps_auth/config.py`

 * *Files identical despite different names*

### Comparing `fps_auth-0.1.2/fps_auth/db.py` & `fps_auth-0.1.3/fps_auth/db.py`

 * *Files identical despite different names*

### Comparing `fps_auth-0.1.2/fps_auth/main.py` & `fps_auth-0.1.3/fps_auth/main.py`

 * *Files identical despite different names*

### Comparing `fps_auth-0.1.2/fps_auth/routes.py` & `fps_auth-0.1.3/fps_auth/routes.py`

 * *Files identical despite different names*

### Comparing `fps_auth-0.1.2/.gitignore` & `fps_auth-0.1.3/.gitignore`

 * *Files identical despite different names*

### Comparing `fps_auth-0.1.2/COPYING.md` & `fps_auth-0.1.3/COPYING.md`

 * *Files identical despite different names*

### Comparing `fps_auth-0.1.2/pyproject.toml` & `fps_auth-0.1.3/pyproject.toml`

 * *Files 8% similar despite different names*

```diff
@@ -8,15 +8,15 @@
 keywords = ["jupyter", "server", "fastapi", "plugins"]
 dynamic = ["version"]
 requires-python = ">=3.8"
 dependencies = [
     "aiosqlite",
     "fastapi-users[sqlalchemy,oauth] >=10.1.4,<11",
     "sqlalchemy >=1,<2",
-    "jupyverse-api",
+    "jupyverse-api >=0.1.2,<1",
 ]
 
 [[project.authors]]
 name = "Jupyter Development Team"
 email = "jupyter@googlegroups.com"
 
 [project.readme]
```

### Comparing `fps_auth-0.1.2/PKG-INFO` & `fps_auth-0.1.3/PKG-INFO`

 * *Files 19% similar despite different names*

```diff
@@ -1,19 +1,19 @@
 Metadata-Version: 2.1
 Name: fps_auth
-Version: 0.1.2
+Version: 0.1.3
 Summary: An FPS plugin for the authentication API
 Project-URL: Homepage, https://jupyter.org
 Author-email: Jupyter Development Team <jupyter@googlegroups.com>
 License: BSD 3-Clause License
 License-File: COPYING.md
 Keywords: fastapi,jupyter,plugins,server
 Requires-Python: >=3.8
 Requires-Dist: aiosqlite
 Requires-Dist: fastapi-users[oauth,sqlalchemy]<11,>=10.1.4
-Requires-Dist: jupyverse-api
+Requires-Dist: jupyverse-api<1,>=0.1.2
 Requires-Dist: sqlalchemy<2,>=1
 Description-Content-Type: text/markdown
 
 # fps-auth
 
 An FPS plugin for the authentication API.
```

