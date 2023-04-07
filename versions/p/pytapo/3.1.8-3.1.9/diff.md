# Comparing `tmp/pytapo-3.1.8.tar.gz` & `tmp/pytapo-3.1.9.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "pytapo-3.1.8.tar", last modified: Mon Apr  3 11:23:12 2023, max compression
+gzip compressed data, was "pytapo-3.1.9.tar", last modified: Mon Apr  3 12:42:38 2023, max compression
```

## Comparing `pytapo-3.1.8.tar` & `pytapo-3.1.9.tar`

### file list

```diff
@@ -1,27 +1,27 @@
-drwxr-xr-x   0 jurajnyiri   (501) staff       (20)        0 2023-04-03 11:23:12.209255 pytapo-3.1.8/
--rw-r--r--   0 jurajnyiri   (501) staff       (20)     1069 2020-10-01 16:27:56.000000 pytapo-3.1.8/LICENSE
--rw-r--r--   0 jurajnyiri   (501) staff       (20)       16 2020-10-05 17:18:33.000000 pytapo-3.1.8/MANIFEST.in
--rw-r--r--   0 jurajnyiri   (501) staff       (20)     5513 2023-04-03 11:23:12.208841 pytapo-3.1.8/PKG-INFO
--rw-r--r--   0 jurajnyiri   (501) staff       (20)     5076 2023-02-19 14:19:57.000000 pytapo-3.1.8/README.md
-drwxr-xr-x   0 jurajnyiri   (501) staff       (20)        0 2023-04-03 11:23:12.197639 pytapo-3.1.8/pytapo/
--rw-r--r--   0 jurajnyiri   (501) staff       (20)    39011 2023-04-03 11:11:18.000000 pytapo-3.1.8/pytapo/__init__.py
--rw-r--r--   0 jurajnyiri   (501) staff       (20)      523 2023-04-03 10:49:34.000000 pytapo-3.1.8/pytapo/const.py
-drwxr-xr-x   0 jurajnyiri   (501) staff       (20)        0 2023-04-03 11:23:12.207764 pytapo-3.1.8/pytapo/media_stream/
--rw-r--r--   0 jurajnyiri   (501) staff       (20)        0 2022-11-24 13:18:53.000000 pytapo-3.1.8/pytapo/media_stream/__init__.py
--rw-r--r--   0 jurajnyiri   (501) staff       (20)     1977 2023-02-18 20:12:52.000000 pytapo-3.1.8/pytapo/media_stream/_utils.py
--rw-r--r--   0 jurajnyiri   (501) staff       (20)     4295 2023-02-19 16:33:44.000000 pytapo-3.1.8/pytapo/media_stream/convert.py
--rw-r--r--   0 jurajnyiri   (501) staff       (20)     2626 2023-02-17 23:16:54.000000 pytapo-3.1.8/pytapo/media_stream/crypto.py
--rw-r--r--   0 jurajnyiri   (501) staff       (20)     8385 2023-02-24 11:56:12.000000 pytapo-3.1.8/pytapo/media_stream/downloader.py
--rw-r--r--   0 jurajnyiri   (501) staff       (20)      607 2022-11-24 13:18:53.000000 pytapo-3.1.8/pytapo/media_stream/error.py
--rw-r--r--   0 jurajnyiri   (501) staff       (20)     3241 2023-02-18 20:28:53.000000 pytapo-3.1.8/pytapo/media_stream/pes.py
--rw-r--r--   0 jurajnyiri   (501) staff       (20)      659 2023-02-18 20:21:47.000000 pytapo-3.1.8/pytapo/media_stream/response.py
--rw-r--r--   0 jurajnyiri   (501) staff       (20)    19229 2023-02-18 22:06:34.000000 pytapo-3.1.8/pytapo/media_stream/session.py
--rw-r--r--   0 jurajnyiri   (501) staff       (20)     5222 2023-02-18 20:30:07.000000 pytapo-3.1.8/pytapo/media_stream/tsReader.py
-drwxr-xr-x   0 jurajnyiri   (501) staff       (20)        0 2023-04-03 11:23:12.200375 pytapo-3.1.8/pytapo.egg-info/
--rw-r--r--   0 jurajnyiri   (501) staff       (20)     5513 2023-04-03 11:23:12.000000 pytapo-3.1.8/pytapo.egg-info/PKG-INFO
--rw-r--r--   0 jurajnyiri   (501) staff       (20)      530 2023-04-03 11:23:12.000000 pytapo-3.1.8/pytapo.egg-info/SOURCES.txt
--rw-r--r--   0 jurajnyiri   (501) staff       (20)        1 2023-04-03 11:23:12.000000 pytapo-3.1.8/pytapo.egg-info/dependency_links.txt
--rw-r--r--   0 jurajnyiri   (501) staff       (20)       34 2023-04-03 11:23:12.000000 pytapo-3.1.8/pytapo.egg-info/requires.txt
--rw-r--r--   0 jurajnyiri   (501) staff       (20)        7 2023-04-03 11:23:12.000000 pytapo-3.1.8/pytapo.egg-info/top_level.txt
--rw-r--r--   0 jurajnyiri   (501) staff       (20)       38 2023-04-03 11:23:12.209382 pytapo-3.1.8/setup.cfg
--rw-r--r--   0 jurajnyiri   (501) staff       (20)      778 2023-04-03 11:22:13.000000 pytapo-3.1.8/setup.py
+drwxr-xr-x   0 jurajnyiri   (501) staff       (20)        0 2023-04-03 12:42:38.733887 pytapo-3.1.9/
+-rw-r--r--   0 jurajnyiri   (501) staff       (20)     1069 2020-10-01 16:27:56.000000 pytapo-3.1.9/LICENSE
+-rw-r--r--   0 jurajnyiri   (501) staff       (20)       16 2020-10-05 17:18:33.000000 pytapo-3.1.9/MANIFEST.in
+-rw-r--r--   0 jurajnyiri   (501) staff       (20)     5513 2023-04-03 12:42:38.733345 pytapo-3.1.9/PKG-INFO
+-rw-r--r--   0 jurajnyiri   (501) staff       (20)     5076 2023-02-19 14:19:57.000000 pytapo-3.1.9/README.md
+drwxr-xr-x   0 jurajnyiri   (501) staff       (20)        0 2023-04-03 12:42:38.719347 pytapo-3.1.9/pytapo/
+-rw-r--r--   0 jurajnyiri   (501) staff       (20)    39055 2023-04-03 12:41:17.000000 pytapo-3.1.9/pytapo/__init__.py
+-rw-r--r--   0 jurajnyiri   (501) staff       (20)      523 2023-04-03 10:49:34.000000 pytapo-3.1.9/pytapo/const.py
+drwxr-xr-x   0 jurajnyiri   (501) staff       (20)        0 2023-04-03 12:42:38.732028 pytapo-3.1.9/pytapo/media_stream/
+-rw-r--r--   0 jurajnyiri   (501) staff       (20)        0 2022-11-24 13:18:53.000000 pytapo-3.1.9/pytapo/media_stream/__init__.py
+-rw-r--r--   0 jurajnyiri   (501) staff       (20)     1977 2023-02-18 20:12:52.000000 pytapo-3.1.9/pytapo/media_stream/_utils.py
+-rw-r--r--   0 jurajnyiri   (501) staff       (20)     4295 2023-02-19 16:33:44.000000 pytapo-3.1.9/pytapo/media_stream/convert.py
+-rw-r--r--   0 jurajnyiri   (501) staff       (20)     2626 2023-02-17 23:16:54.000000 pytapo-3.1.9/pytapo/media_stream/crypto.py
+-rw-r--r--   0 jurajnyiri   (501) staff       (20)     8385 2023-02-24 11:56:12.000000 pytapo-3.1.9/pytapo/media_stream/downloader.py
+-rw-r--r--   0 jurajnyiri   (501) staff       (20)      607 2022-11-24 13:18:53.000000 pytapo-3.1.9/pytapo/media_stream/error.py
+-rw-r--r--   0 jurajnyiri   (501) staff       (20)     3241 2023-02-18 20:28:53.000000 pytapo-3.1.9/pytapo/media_stream/pes.py
+-rw-r--r--   0 jurajnyiri   (501) staff       (20)      659 2023-02-18 20:21:47.000000 pytapo-3.1.9/pytapo/media_stream/response.py
+-rw-r--r--   0 jurajnyiri   (501) staff       (20)    19229 2023-02-18 22:06:34.000000 pytapo-3.1.9/pytapo/media_stream/session.py
+-rw-r--r--   0 jurajnyiri   (501) staff       (20)     5222 2023-02-18 20:30:07.000000 pytapo-3.1.9/pytapo/media_stream/tsReader.py
+drwxr-xr-x   0 jurajnyiri   (501) staff       (20)        0 2023-04-03 12:42:38.722253 pytapo-3.1.9/pytapo.egg-info/
+-rw-r--r--   0 jurajnyiri   (501) staff       (20)     5513 2023-04-03 12:42:38.000000 pytapo-3.1.9/pytapo.egg-info/PKG-INFO
+-rw-r--r--   0 jurajnyiri   (501) staff       (20)      530 2023-04-03 12:42:38.000000 pytapo-3.1.9/pytapo.egg-info/SOURCES.txt
+-rw-r--r--   0 jurajnyiri   (501) staff       (20)        1 2023-04-03 12:42:38.000000 pytapo-3.1.9/pytapo.egg-info/dependency_links.txt
+-rw-r--r--   0 jurajnyiri   (501) staff       (20)       34 2023-04-03 12:42:38.000000 pytapo-3.1.9/pytapo.egg-info/requires.txt
+-rw-r--r--   0 jurajnyiri   (501) staff       (20)        7 2023-04-03 12:42:38.000000 pytapo-3.1.9/pytapo.egg-info/top_level.txt
+-rw-r--r--   0 jurajnyiri   (501) staff       (20)       38 2023-04-03 12:42:38.734037 pytapo-3.1.9/setup.cfg
+-rw-r--r--   0 jurajnyiri   (501) staff       (20)      778 2023-04-03 12:40:50.000000 pytapo-3.1.9/setup.py
```

### Comparing `pytapo-3.1.8/LICENSE` & `pytapo-3.1.9/LICENSE`

 * *Files identical despite different names*

### Comparing `pytapo-3.1.8/PKG-INFO` & `pytapo-3.1.9/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: pytapo
-Version: 3.1.8
+Version: 3.1.9
 Summary: Python library for communication with Tapo Cameras
 Home-page: https://github.com/JurajNyiri/pytapo
 Author: Juraj Nyíri
 Author-email: juraj.nyiri@gmail.com
 License: MIT
 Classifier: Programming Language :: Python :: 3
 Classifier: License :: OSI Approved :: MIT License
```

### Comparing `pytapo-3.1.8/README.md` & `pytapo-3.1.9/README.md`

 * *Files identical despite different names*

### Comparing `pytapo-3.1.8/pytapo/__init__.py` & `pytapo-3.1.9/pytapo/__init__.py`

 * *Files 0% similar despite different names*

```diff
@@ -677,19 +677,20 @@
             "getTamperDetectionConfig", {"tamper_detection": {"name": "tamper_det"}},
         )["tamper_detection"]["tamper_det"]
 
     def setTamperDetection(self, enabled, sensitivity=False):
         data = {
             "tamper_detection": {"tamper_det": {"enabled": "on" if enabled else "off"}}
         }
-        if sensitivity not in ["high", "normal", "low"]:
-            raise Exception("Invalid sensitivity, can be low, normal or high")
-        if sensitivity == "normal":
-            sensitivity = "medium"
-        data["tamper_detection"]["tamper_det"]["sensitivity"] = sensitivity
+        if sensitivity:
+            if sensitivity not in ["high", "normal", "low"]:
+                raise Exception("Invalid sensitivity, can be low, normal or high")
+            if sensitivity == "normal":
+                sensitivity = "medium"
+            data["tamper_detection"]["tamper_det"]["sensitivity"] = sensitivity
 
         return self.executeFunction("setTamperDetectionConfig", data)
 
     def getBabyCryDetection(self):
         return self.executeFunction(
             "getBCDConfig", {"sound_detection": {"name": ["bcd"]}},
         )["sound_detection"]["bcd"]
```

### Comparing `pytapo-3.1.8/pytapo/const.py` & `pytapo-3.1.9/pytapo/const.py`

 * *Files identical despite different names*

### Comparing `pytapo-3.1.8/pytapo/media_stream/_utils.py` & `pytapo-3.1.9/pytapo/media_stream/_utils.py`

 * *Files identical despite different names*

### Comparing `pytapo-3.1.8/pytapo/media_stream/convert.py` & `pytapo-3.1.9/pytapo/media_stream/convert.py`

 * *Files identical despite different names*

### Comparing `pytapo-3.1.8/pytapo/media_stream/crypto.py` & `pytapo-3.1.9/pytapo/media_stream/crypto.py`

 * *Files identical despite different names*

### Comparing `pytapo-3.1.8/pytapo/media_stream/downloader.py` & `pytapo-3.1.9/pytapo/media_stream/downloader.py`

 * *Files identical despite different names*

### Comparing `pytapo-3.1.8/pytapo/media_stream/error.py` & `pytapo-3.1.9/pytapo/media_stream/error.py`

 * *Files identical despite different names*

### Comparing `pytapo-3.1.8/pytapo/media_stream/pes.py` & `pytapo-3.1.9/pytapo/media_stream/pes.py`

 * *Files identical despite different names*

### Comparing `pytapo-3.1.8/pytapo/media_stream/response.py` & `pytapo-3.1.9/pytapo/media_stream/response.py`

 * *Files identical despite different names*

### Comparing `pytapo-3.1.8/pytapo/media_stream/session.py` & `pytapo-3.1.9/pytapo/media_stream/session.py`

 * *Files identical despite different names*

### Comparing `pytapo-3.1.8/pytapo/media_stream/tsReader.py` & `pytapo-3.1.9/pytapo/media_stream/tsReader.py`

 * *Files identical despite different names*

### Comparing `pytapo-3.1.8/pytapo.egg-info/PKG-INFO` & `pytapo-3.1.9/pytapo.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: pytapo
-Version: 3.1.8
+Version: 3.1.9
 Summary: Python library for communication with Tapo Cameras
 Home-page: https://github.com/JurajNyiri/pytapo
 Author: Juraj Nyíri
 Author-email: juraj.nyiri@gmail.com
 License: MIT
 Classifier: Programming Language :: Python :: 3
 Classifier: License :: OSI Approved :: MIT License
```

### Comparing `pytapo-3.1.8/pytapo.egg-info/SOURCES.txt` & `pytapo-3.1.9/pytapo.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `pytapo-3.1.8/setup.py` & `pytapo-3.1.9/setup.py`

 * *Files 2% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 import setuptools
 
 with open("README.md", "r") as fh:
     long_description = fh.read()
 
 setuptools.setup(
     name="pytapo",
-    version="3.1.8",
+    version="3.1.9",
     author="Juraj Nyíri",
     author_email="juraj.nyiri@gmail.com",
     description="Python library for communication with Tapo Cameras",
     license="MIT",
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://github.com/JurajNyiri/pytapo",
```

