# Comparing `tmp/sciencebasepy-2.0.8.tar.gz` & `tmp/sciencebasepy-2.0.9.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "sciencebasepy-2.0.8.tar", last modified: Thu Oct 20 21:38:24 2022, max compression
+gzip compressed data, was "sciencebasepy-2.0.9.tar", last modified: Wed Dec  7 19:50:54 2022, max compression
```

## Comparing `sciencebasepy-2.0.8.tar` & `sciencebasepy-2.0.9.tar`

### file list

```diff
@@ -1,25 +1,25 @@
-drwxr-xr-x   0 jsheflin (1824439838) GS\Domain Users (346589396)        0 2022-10-20 21:38:24.602429 sciencebasepy-2.0.8/
--rw-r--r--   0 jsheflin (1824439838) GS\Domain Users (346589396)      569 2022-10-11 20:36:33.000000 sciencebasepy-2.0.8/LICENSE
--rw-r--r--   0 jsheflin (1824439838) GS\Domain Users (346589396)    17754 2022-10-20 21:38:24.601563 sciencebasepy-2.0.8/PKG-INFO
--rw-r--r--   0 jsheflin (1824439838) GS\Domain Users (346589396)    16793 2022-10-13 15:52:50.000000 sciencebasepy-2.0.8/README.md
-drwxr-xr-x   0 jsheflin (1824439838) GS\Domain Users (346589396)        0 2022-10-20 21:38:24.554583 sciencebasepy-2.0.8/sb3/
--rw-r--r--   0 jsheflin (1824439838) GS\Domain Users (346589396)     6387 2022-10-11 23:23:29.000000 sciencebasepy-2.0.8/sb3/SbSessionEx.py
--rw-r--r--   0 jsheflin (1824439838) GS\Domain Users (346589396)        0 2022-10-11 20:36:33.000000 sciencebasepy-2.0.8/sb3/__init__.py
--rw-r--r--   0 jsheflin (1824439838) GS\Domain Users (346589396)     3752 2022-10-11 20:36:33.000000 sciencebasepy-2.0.8/sb3/auth.py
--rw-r--r--   0 jsheflin (1824439838) GS\Domain Users (346589396)     7384 2022-10-11 23:23:29.000000 sciencebasepy-2.0.8/sb3/client.py
--rw-r--r--   0 jsheflin (1824439838) GS\Domain Users (346589396)     1136 2022-10-11 20:36:33.000000 sciencebasepy-2.0.8/sb3/querys.py
-drwxr-xr-x   0 jsheflin (1824439838) GS\Domain Users (346589396)        0 2022-10-20 21:38:24.575987 sciencebasepy-2.0.8/sciencebasepy/
--rw-r--r--   0 jsheflin (1824439838) GS\Domain Users (346589396)    71177 2022-10-20 20:03:35.000000 sciencebasepy-2.0.8/sciencebasepy/SbSession.py
--rw-r--r--   0 jsheflin (1824439838) GS\Domain Users (346589396)      281 2022-10-11 20:36:33.000000 sciencebasepy-2.0.8/sciencebasepy/__init__.py
-drwxr-xr-x   0 jsheflin (1824439838) GS\Domain Users (346589396)        0 2022-10-20 21:38:24.582213 sciencebasepy-2.0.8/sciencebasepy.egg-info/
--rw-r--r--   0 jsheflin (1824439838) GS\Domain Users (346589396)    17754 2022-10-20 21:38:24.000000 sciencebasepy-2.0.8/sciencebasepy.egg-info/PKG-INFO
--rw-r--r--   0 jsheflin (1824439838) GS\Domain Users (346589396)      397 2022-10-20 21:38:24.000000 sciencebasepy-2.0.8/sciencebasepy.egg-info/SOURCES.txt
--rw-r--r--   0 jsheflin (1824439838) GS\Domain Users (346589396)        1 2022-10-20 21:38:24.000000 sciencebasepy-2.0.8/sciencebasepy.egg-info/dependency_links.txt
--rw-r--r--   0 jsheflin (1824439838) GS\Domain Users (346589396)       18 2022-10-20 21:38:24.000000 sciencebasepy-2.0.8/sciencebasepy.egg-info/requires.txt
--rw-r--r--   0 jsheflin (1824439838) GS\Domain Users (346589396)       24 2022-10-20 21:38:24.000000 sciencebasepy-2.0.8/sciencebasepy.egg-info/top_level.txt
--rw-r--r--   0 jsheflin (1824439838) GS\Domain Users (346589396)       38 2022-10-20 21:38:24.602616 sciencebasepy-2.0.8/setup.cfg
--rw-r--r--   0 jsheflin (1824439838) GS\Domain Users (346589396)     1227 2022-10-20 20:07:39.000000 sciencebasepy-2.0.8/setup.py
-drwxr-xr-x   0 jsheflin (1824439838) GS\Domain Users (346589396)        0 2022-10-20 21:38:24.600059 sciencebasepy-2.0.8/tests/
--rw-r--r--   0 jsheflin (1824439838) GS\Domain Users (346589396)        0 2022-10-11 20:36:33.000000 sciencebasepy-2.0.8/tests/__init__.py
--rw-r--r--   0 jsheflin (1824439838) GS\Domain Users (346589396)     1435 2022-10-11 20:36:33.000000 sciencebasepy-2.0.8/tests/test_login.py
--rw-r--r--   0 jsheflin (1824439838) GS\Domain Users (346589396)     3729 2022-10-11 20:36:33.000000 sciencebasepy-2.0.8/tests/test_upload.py
+drwxr-xr-x   0 jsheflin (1824439838) GS\Domain Users (346589396)        0 2022-12-07 19:50:54.940765 sciencebasepy-2.0.9/
+-rw-r--r--   0 jsheflin (1824439838) GS\Domain Users (346589396)      569 2022-10-11 20:36:33.000000 sciencebasepy-2.0.9/LICENSE
+-rw-r--r--   0 jsheflin (1824439838) GS\Domain Users (346589396)    17754 2022-12-07 19:50:54.940200 sciencebasepy-2.0.9/PKG-INFO
+-rw-r--r--   0 jsheflin (1824439838) GS\Domain Users (346589396)    16793 2022-10-13 15:52:50.000000 sciencebasepy-2.0.9/README.md
+drwxr-xr-x   0 jsheflin (1824439838) GS\Domain Users (346589396)        0 2022-12-07 19:50:54.911065 sciencebasepy-2.0.9/sb3/
+-rw-r--r--   0 jsheflin (1824439838) GS\Domain Users (346589396)     6387 2022-10-11 23:23:29.000000 sciencebasepy-2.0.9/sb3/SbSessionEx.py
+-rw-r--r--   0 jsheflin (1824439838) GS\Domain Users (346589396)        0 2022-10-11 20:36:33.000000 sciencebasepy-2.0.9/sb3/__init__.py
+-rw-r--r--   0 jsheflin (1824439838) GS\Domain Users (346589396)     3752 2022-10-11 20:36:33.000000 sciencebasepy-2.0.9/sb3/auth.py
+-rw-r--r--   0 jsheflin (1824439838) GS\Domain Users (346589396)     7384 2022-10-11 23:23:29.000000 sciencebasepy-2.0.9/sb3/client.py
+-rw-r--r--   0 jsheflin (1824439838) GS\Domain Users (346589396)     1136 2022-10-11 20:36:33.000000 sciencebasepy-2.0.9/sb3/querys.py
+drwxr-xr-x   0 jsheflin (1824439838) GS\Domain Users (346589396)        0 2022-12-07 19:50:54.916826 sciencebasepy-2.0.9/sciencebasepy/
+-rw-r--r--   0 jsheflin (1824439838) GS\Domain Users (346589396)    71215 2022-12-06 22:19:43.000000 sciencebasepy-2.0.9/sciencebasepy/SbSession.py
+-rw-r--r--   0 jsheflin (1824439838) GS\Domain Users (346589396)      281 2022-10-11 20:36:33.000000 sciencebasepy-2.0.9/sciencebasepy/__init__.py
+drwxr-xr-x   0 jsheflin (1824439838) GS\Domain Users (346589396)        0 2022-12-07 19:50:54.920873 sciencebasepy-2.0.9/sciencebasepy.egg-info/
+-rw-r--r--   0 jsheflin (1824439838) GS\Domain Users (346589396)    17754 2022-12-07 19:50:54.000000 sciencebasepy-2.0.9/sciencebasepy.egg-info/PKG-INFO
+-rw-r--r--   0 jsheflin (1824439838) GS\Domain Users (346589396)      397 2022-12-07 19:50:54.000000 sciencebasepy-2.0.9/sciencebasepy.egg-info/SOURCES.txt
+-rw-r--r--   0 jsheflin (1824439838) GS\Domain Users (346589396)        1 2022-12-07 19:50:54.000000 sciencebasepy-2.0.9/sciencebasepy.egg-info/dependency_links.txt
+-rw-r--r--   0 jsheflin (1824439838) GS\Domain Users (346589396)       18 2022-12-07 19:50:54.000000 sciencebasepy-2.0.9/sciencebasepy.egg-info/requires.txt
+-rw-r--r--   0 jsheflin (1824439838) GS\Domain Users (346589396)       24 2022-12-07 19:50:54.000000 sciencebasepy-2.0.9/sciencebasepy.egg-info/top_level.txt
+-rw-r--r--   0 jsheflin (1824439838) GS\Domain Users (346589396)       38 2022-12-07 19:50:54.940922 sciencebasepy-2.0.9/setup.cfg
+-rw-r--r--   0 jsheflin (1824439838) GS\Domain Users (346589396)     1227 2022-12-07 19:48:07.000000 sciencebasepy-2.0.9/setup.py
+drwxr-xr-x   0 jsheflin (1824439838) GS\Domain Users (346589396)        0 2022-12-07 19:50:54.939315 sciencebasepy-2.0.9/tests/
+-rw-r--r--   0 jsheflin (1824439838) GS\Domain Users (346589396)        0 2022-10-11 20:36:33.000000 sciencebasepy-2.0.9/tests/__init__.py
+-rw-r--r--   0 jsheflin (1824439838) GS\Domain Users (346589396)     1435 2022-10-11 20:36:33.000000 sciencebasepy-2.0.9/tests/test_login.py
+-rw-r--r--   0 jsheflin (1824439838) GS\Domain Users (346589396)     3729 2022-10-11 20:36:33.000000 sciencebasepy-2.0.9/tests/test_upload.py
```

### Comparing `sciencebasepy-2.0.8/LICENSE` & `sciencebasepy-2.0.9/LICENSE`

 * *Files identical despite different names*

### Comparing `sciencebasepy-2.0.8/PKG-INFO` & `sciencebasepy-2.0.9/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: sciencebasepy
-Version: 2.0.8
+Version: 2.0.9
 Summary: Python ScienceBase Utilities
 Home-page: https://github.com/usgs/sciencebasepy
 Author: USGS ScienceBase Development Team
 Author-email: sciencebase@usgs.gov
 Classifier: License :: Public Domain
 Classifier: Operating System :: OS Independent
 Classifier: Programming Language :: Python
```

### Comparing `sciencebasepy-2.0.8/README.md` & `sciencebasepy-2.0.9/README.md`

 * *Files identical despite different names*

### Comparing `sciencebasepy-2.0.8/sb3/SbSessionEx.py` & `sciencebasepy-2.0.9/sb3/SbSessionEx.py`

 * *Files identical despite different names*

### Comparing `sciencebasepy-2.0.8/sb3/auth.py` & `sciencebasepy-2.0.9/sb3/auth.py`

 * *Files identical despite different names*

### Comparing `sciencebasepy-2.0.8/sb3/client.py` & `sciencebasepy-2.0.9/sb3/client.py`

 * *Files identical despite different names*

### Comparing `sciencebasepy-2.0.8/sb3/querys.py` & `sciencebasepy-2.0.9/sb3/querys.py`

 * *Files identical despite different names*

### Comparing `sciencebasepy-2.0.8/sciencebasepy/SbSession.py` & `sciencebasepy-2.0.9/sciencebasepy/SbSession.py`

 * *Files 0% similar despite different names*

```diff
@@ -1413,15 +1413,16 @@
                 return False
 
             else:
                 params = {
                     "filename": filename,
                     "item_id": item_id,
                     "queue_name": "publish_sd_to_agol",
-                    "email": self._username
+                    "email": self._username,
+                    "type": "single"
                 }
 
                 start_spatial_service_url = "https://rwxatj0usl.execute-api.us-west-2.amazonaws.com/prod/startSpatialService"
 
                 self._session.post(start_spatial_service_url, json=params)
 
                 print("Triggered spatial service creation in ArcGIS Online.")
```

### Comparing `sciencebasepy-2.0.8/sciencebasepy.egg-info/PKG-INFO` & `sciencebasepy-2.0.9/sciencebasepy.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: sciencebasepy
-Version: 2.0.8
+Version: 2.0.9
 Summary: Python ScienceBase Utilities
 Home-page: https://github.com/usgs/sciencebasepy
 Author: USGS ScienceBase Development Team
 Author-email: sciencebase@usgs.gov
 Classifier: License :: Public Domain
 Classifier: Operating System :: OS Independent
 Classifier: Programming Language :: Python
```

### Comparing `sciencebasepy-2.0.8/setup.py` & `sciencebasepy-2.0.9/setup.py`

 * *Files 4% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 import setuptools
 
 with open("README.md", "r") as fh:
     long_description = fh.read()
 
 setuptools.setup(
     name='sciencebasepy',
-    version='2.0.8',
+    version='2.0.9',
     author="USGS ScienceBase Development Team",
     author_email="sciencebase@usgs.gov",
     description="Python ScienceBase Utilities",
     long_description=long_description,
     long_description_content_type="text/markdown",
     url='https://github.com/usgs/sciencebasepy',
     packages=setuptools.find_packages(),
```

### Comparing `sciencebasepy-2.0.8/tests/test_login.py` & `sciencebasepy-2.0.9/tests/test_login.py`

 * *Files identical despite different names*

### Comparing `sciencebasepy-2.0.8/tests/test_upload.py` & `sciencebasepy-2.0.9/tests/test_upload.py`

 * *Files identical despite different names*

