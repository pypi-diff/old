# Comparing `tmp/fps_kernels-0.1.2.tar.gz` & `tmp/fps_kernels-0.1.3.tar.gz`

## Comparing `fps_kernels-0.1.2.tar` & `fps_kernels-0.1.3.tar`

### file list

```diff
@@ -1,18 +1,18 @@
--rw-r--r--   0        0        0       13 2020-02-02 00:00:00.000000 fps_kernels-0.1.2/MANIFEST.in
--rw-r--r--   0        0        0       22 2020-02-02 00:00:00.000000 fps_kernels-0.1.2/fps_kernels/__init__.py
--rw-r--r--   0        0        0     1582 2020-02-02 00:00:00.000000 fps_kernels-0.1.2/fps_kernels/main.py
--rw-r--r--   0        0        0    15262 2020-02-02 00:00:00.000000 fps_kernels-0.1.2/fps_kernels/routes.py
--rw-r--r--   0        0        0        0 2020-02-02 00:00:00.000000 fps_kernels-0.1.2/fps_kernels/kernel_driver/__init__.py
--rw-r--r--   0        0        0     2987 2020-02-02 00:00:00.000000 fps_kernels-0.1.2/fps_kernels/kernel_driver/connect.py
--rw-r--r--   0        0        0     8632 2020-02-02 00:00:00.000000 fps_kernels-0.1.2/fps_kernels/kernel_driver/driver.py
--rw-r--r--   0        0        0     1900 2020-02-02 00:00:00.000000 fps_kernels-0.1.2/fps_kernels/kernel_driver/kernelspec.py
--rw-r--r--   0        0        0     4078 2020-02-02 00:00:00.000000 fps_kernels-0.1.2/fps_kernels/kernel_driver/message.py
--rw-r--r--   0        0        0     2916 2020-02-02 00:00:00.000000 fps_kernels-0.1.2/fps_kernels/kernel_driver/paths.py
--rw-r--r--   0        0        0        0 2020-02-02 00:00:00.000000 fps_kernels-0.1.2/fps_kernels/kernel_server/__init__.py
--rw-r--r--   0        0        0     2731 2020-02-02 00:00:00.000000 fps_kernels-0.1.2/fps_kernels/kernel_server/message.py
--rw-r--r--   0        0        0    11591 2020-02-02 00:00:00.000000 fps_kernels-0.1.2/fps_kernels/kernel_server/server.py
--rw-r--r--   0        0        0     6359 2020-02-02 00:00:00.000000 fps_kernels-0.1.2/.gitignore
--rw-r--r--   0        0        0     2833 2020-02-02 00:00:00.000000 fps_kernels-0.1.2/COPYING.md
--rw-r--r--   0        0        0       50 2020-02-02 00:00:00.000000 fps_kernels-0.1.2/README.md
--rw-r--r--   0        0        0      987 2020-02-02 00:00:00.000000 fps_kernels-0.1.2/pyproject.toml
--rw-r--r--   0        0        0      598 2020-02-02 00:00:00.000000 fps_kernels-0.1.2/PKG-INFO
+-rw-r--r--   0        0        0       13 2020-02-02 00:00:00.000000 fps_kernels-0.1.3/MANIFEST.in
+-rw-r--r--   0        0        0       22 2020-02-02 00:00:00.000000 fps_kernels-0.1.3/fps_kernels/__init__.py
+-rw-r--r--   0        0        0     1582 2020-02-02 00:00:00.000000 fps_kernels-0.1.3/fps_kernels/main.py
+-rw-r--r--   0        0        0    15262 2020-02-02 00:00:00.000000 fps_kernels-0.1.3/fps_kernels/routes.py
+-rw-r--r--   0        0        0        0 2020-02-02 00:00:00.000000 fps_kernels-0.1.3/fps_kernels/kernel_driver/__init__.py
+-rw-r--r--   0        0        0     2987 2020-02-02 00:00:00.000000 fps_kernels-0.1.3/fps_kernels/kernel_driver/connect.py
+-rw-r--r--   0        0        0     8632 2020-02-02 00:00:00.000000 fps_kernels-0.1.3/fps_kernels/kernel_driver/driver.py
+-rw-r--r--   0        0        0     1900 2020-02-02 00:00:00.000000 fps_kernels-0.1.3/fps_kernels/kernel_driver/kernelspec.py
+-rw-r--r--   0        0        0     4078 2020-02-02 00:00:00.000000 fps_kernels-0.1.3/fps_kernels/kernel_driver/message.py
+-rw-r--r--   0        0        0     2916 2020-02-02 00:00:00.000000 fps_kernels-0.1.3/fps_kernels/kernel_driver/paths.py
+-rw-r--r--   0        0        0        0 2020-02-02 00:00:00.000000 fps_kernels-0.1.3/fps_kernels/kernel_server/__init__.py
+-rw-r--r--   0        0        0     2731 2020-02-02 00:00:00.000000 fps_kernels-0.1.3/fps_kernels/kernel_server/message.py
+-rw-r--r--   0        0        0    11591 2020-02-02 00:00:00.000000 fps_kernels-0.1.3/fps_kernels/kernel_server/server.py
+-rw-r--r--   0        0        0     6359 2020-02-02 00:00:00.000000 fps_kernels-0.1.3/.gitignore
+-rw-r--r--   0        0        0     2833 2020-02-02 00:00:00.000000 fps_kernels-0.1.3/COPYING.md
+-rw-r--r--   0        0        0       50 2020-02-02 00:00:00.000000 fps_kernels-0.1.3/README.md
+-rw-r--r--   0        0        0      998 2020-02-02 00:00:00.000000 fps_kernels-0.1.3/pyproject.toml
+-rw-r--r--   0        0        0      608 2020-02-02 00:00:00.000000 fps_kernels-0.1.3/PKG-INFO
```

### Comparing `fps_kernels-0.1.2/fps_kernels/main.py` & `fps_kernels-0.1.3/fps_kernels/main.py`

 * *Files identical despite different names*

### Comparing `fps_kernels-0.1.2/fps_kernels/routes.py` & `fps_kernels-0.1.3/fps_kernels/routes.py`

 * *Files identical despite different names*

### Comparing `fps_kernels-0.1.2/fps_kernels/kernel_driver/connect.py` & `fps_kernels-0.1.3/fps_kernels/kernel_driver/connect.py`

 * *Files identical despite different names*

### Comparing `fps_kernels-0.1.2/fps_kernels/kernel_driver/driver.py` & `fps_kernels-0.1.3/fps_kernels/kernel_driver/driver.py`

 * *Files identical despite different names*

### Comparing `fps_kernels-0.1.2/fps_kernels/kernel_driver/kernelspec.py` & `fps_kernels-0.1.3/fps_kernels/kernel_driver/kernelspec.py`

 * *Files identical despite different names*

### Comparing `fps_kernels-0.1.2/fps_kernels/kernel_driver/message.py` & `fps_kernels-0.1.3/fps_kernels/kernel_driver/message.py`

 * *Files identical despite different names*

### Comparing `fps_kernels-0.1.2/fps_kernels/kernel_driver/paths.py` & `fps_kernels-0.1.3/fps_kernels/kernel_driver/paths.py`

 * *Files identical despite different names*

### Comparing `fps_kernels-0.1.2/fps_kernels/kernel_server/message.py` & `fps_kernels-0.1.3/fps_kernels/kernel_server/message.py`

 * *Files identical despite different names*

### Comparing `fps_kernels-0.1.2/fps_kernels/kernel_server/server.py` & `fps_kernels-0.1.3/fps_kernels/kernel_server/server.py`

 * *Files identical despite different names*

### Comparing `fps_kernels-0.1.2/.gitignore` & `fps_kernels-0.1.3/.gitignore`

 * *Files identical despite different names*

### Comparing `fps_kernels-0.1.2/COPYING.md` & `fps_kernels-0.1.3/COPYING.md`

 * *Files identical despite different names*

### Comparing `fps_kernels-0.1.2/pyproject.toml` & `fps_kernels-0.1.3/pyproject.toml`

 * *Files 8% similar despite different names*

```diff
@@ -9,15 +9,15 @@
 requires-python = ">=3.8"
 dependencies = [
     "pyzmq",
     "websockets",
     "python-dateutil",
     "types-python-dateutil",
     "watchfiles >=0.16.1,<1",
-    "jupyverse-api",
+    "jupyverse-api >=0.1.2,<1",
 ]
 dynamic = [ "version",]
 [[project.authors]]
 name = "Jupyter Development Team"
 email = "jupyter@googlegroups.com"
 
 [project.readme]
```

### Comparing `fps_kernels-0.1.2/PKG-INFO` & `fps_kernels-0.1.3/PKG-INFO`

 * *Files 2% similar despite different names*

```diff
@@ -1,18 +1,18 @@
 Metadata-Version: 2.1
 Name: fps_kernels
-Version: 0.1.2
+Version: 0.1.3
 Summary: An FPS plugin for the kernels API
 Project-URL: Homepage, https://jupyter.org
 Author-email: Jupyter Development Team <jupyter@googlegroups.com>
 License: BSD 3-Clause License
 License-File: COPYING.md
 Keywords: fastapi,jupyter,plugins,server
 Requires-Python: >=3.8
-Requires-Dist: jupyverse-api
+Requires-Dist: jupyverse-api<1,>=0.1.2
 Requires-Dist: python-dateutil
 Requires-Dist: pyzmq
 Requires-Dist: types-python-dateutil
 Requires-Dist: watchfiles<1,>=0.16.1
 Requires-Dist: websockets
 Description-Content-Type: text/markdown
```

