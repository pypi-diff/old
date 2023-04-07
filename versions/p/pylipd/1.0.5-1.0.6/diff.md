# Comparing `tmp/pylipd-1.0.5.tar.gz` & `tmp/pylipd-1.0.6.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "pylipd-1.0.5.tar", last modified: Fri Apr  7 06:01:32 2023, max compression
+gzip compressed data, was "pylipd-1.0.6.tar", last modified: Fri Apr  7 06:13:27 2023, max compression
```

## Comparing `pylipd-1.0.5.tar` & `pylipd-1.0.6.tar`

### file list

```diff
@@ -1,32 +1,32 @@
-drwxr-xr-x   0 varun      (502) staff       (20)        0 2023-04-07 06:01:32.010823 pylipd-1.0.5/
--rw-r--r--   0 varun      (502) staff       (20)    11357 2022-09-22 13:14:27.000000 pylipd-1.0.5/LICENSE
--rw-r--r--   0 varun      (502) staff       (20)     1282 2023-04-07 06:01:32.010873 pylipd-1.0.5/PKG-INFO
--rw-r--r--   0 varun      (502) staff       (20)      630 2023-03-22 12:37:06.000000 pylipd-1.0.5/README.md
-drwxr-xr-x   0 varun      (502) staff       (20)        0 2023-04-07 06:01:32.009281 pylipd-1.0.5/pylipd/
--rw-r--r--   0 varun      (502) staff       (20)       22 2023-04-07 06:00:00.000000 pylipd-1.0.5/pylipd/__init__.py
-drwxr-xr-x   0 varun      (502) staff       (20)        0 2023-04-07 06:01:32.009755 pylipd-1.0.5/pylipd/globals/
--rw-r--r--   0 varun      (502) staff       (20)        0 2023-01-10 17:13:18.000000 pylipd-1.0.5/pylipd/globals/__init__.py
--rw-r--r--   0 varun      (502) staff       (20)      383 2022-11-15 21:36:42.000000 pylipd-1.0.5/pylipd/globals/blacklist.py
--rw-r--r--   0 varun      (502) staff       (20)    14564 2023-03-06 15:30:09.000000 pylipd-1.0.5/pylipd/globals/schema.py
--rw-r--r--   0 varun      (502) staff       (20)      197 2022-11-14 07:40:00.000000 pylipd-1.0.5/pylipd/globals/urls.py
--rw-r--r--   0 varun      (502) staff       (20)    15815 2023-02-10 12:09:50.000000 pylipd-1.0.5/pylipd/legacy_utils.py
--rw-r--r--   0 varun      (502) staff       (20)    28677 2023-04-07 04:11:12.000000 pylipd-1.0.5/pylipd/lipd.py
--rw-r--r--   0 varun      (502) staff       (20)    42808 2023-03-31 15:11:12.000000 pylipd-1.0.5/pylipd/lipd_to_rdf.py
--rw-r--r--   0 varun      (502) staff       (20)     1742 2023-04-07 05:39:21.000000 pylipd-1.0.5/pylipd/multi_processing.py
--rw-r--r--   0 varun      (502) staff       (20)    17140 2023-02-23 13:16:36.000000 pylipd-1.0.5/pylipd/rdf_to_lipd.py
-drwxr-xr-x   0 varun      (502) staff       (20)        0 2023-04-07 06:01:32.009953 pylipd-1.0.5/pylipd/series/
--rw-r--r--   0 varun      (502) staff       (20)        0 2023-01-10 17:13:31.000000 pylipd-1.0.5/pylipd/series/__init__.py
--rw-r--r--   0 varun      (502) staff       (20)     3223 2022-11-15 20:06:27.000000 pylipd-1.0.5/pylipd/series/regexes.py
--rw-r--r--   0 varun      (502) staff       (20)     2270 2023-03-22 17:52:14.000000 pylipd-1.0.5/pylipd/test.py
--rw-r--r--   0 varun      (502) staff       (20)     4141 2023-04-07 05:57:19.000000 pylipd-1.0.5/pylipd/usage.py
--rw-r--r--   0 varun      (502) staff       (20)     2602 2023-02-23 10:01:04.000000 pylipd-1.0.5/pylipd/utils.py
-drwxr-xr-x   0 varun      (502) staff       (20)        0 2023-04-07 06:01:32.010727 pylipd-1.0.5/pylipd.egg-info/
--rw-r--r--   0 varun      (502) staff       (20)     1282 2023-04-07 06:01:32.000000 pylipd-1.0.5/pylipd.egg-info/PKG-INFO
--rw-r--r--   0 varun      (502) staff       (20)      588 2023-04-07 06:01:32.000000 pylipd-1.0.5/pylipd.egg-info/SOURCES.txt
--rw-r--r--   0 varun      (502) staff       (20)        1 2023-04-07 06:01:32.000000 pylipd-1.0.5/pylipd.egg-info/dependency_links.txt
--rw-r--r--   0 varun      (502) staff       (20)        1 2023-02-24 09:46:52.000000 pylipd-1.0.5/pylipd.egg-info/not-zip-safe
--rw-r--r--   0 varun      (502) staff       (20)       29 2023-04-07 06:01:32.000000 pylipd-1.0.5/pylipd.egg-info/requires.txt
--rw-r--r--   0 varun      (502) staff       (20)        7 2023-04-07 06:01:32.000000 pylipd-1.0.5/pylipd.egg-info/top_level.txt
--rw-r--r--   0 varun      (502) staff       (20)      104 2023-02-10 17:39:16.000000 pylipd-1.0.5/pyproject.toml
--rw-r--r--   0 varun      (502) staff       (20)      686 2023-04-07 06:01:32.011122 pylipd-1.0.5/setup.cfg
--rw-r--r--   0 varun      (502) staff       (20)      956 2023-04-07 05:59:53.000000 pylipd-1.0.5/setup.py
+drwxr-xr-x   0 varun      (502) staff       (20)        0 2023-04-07 06:13:27.903817 pylipd-1.0.6/
+-rw-r--r--   0 varun      (502) staff       (20)    11357 2022-09-22 13:14:27.000000 pylipd-1.0.6/LICENSE
+-rw-r--r--   0 varun      (502) staff       (20)     1282 2023-04-07 06:13:27.903864 pylipd-1.0.6/PKG-INFO
+-rw-r--r--   0 varun      (502) staff       (20)      630 2023-03-22 12:37:06.000000 pylipd-1.0.6/README.md
+drwxr-xr-x   0 varun      (502) staff       (20)        0 2023-04-07 06:13:27.902426 pylipd-1.0.6/pylipd/
+-rw-r--r--   0 varun      (502) staff       (20)       22 2023-04-07 06:13:24.000000 pylipd-1.0.6/pylipd/__init__.py
+drwxr-xr-x   0 varun      (502) staff       (20)        0 2023-04-07 06:13:27.902854 pylipd-1.0.6/pylipd/globals/
+-rw-r--r--   0 varun      (502) staff       (20)        0 2023-01-10 17:13:18.000000 pylipd-1.0.6/pylipd/globals/__init__.py
+-rw-r--r--   0 varun      (502) staff       (20)      383 2022-11-15 21:36:42.000000 pylipd-1.0.6/pylipd/globals/blacklist.py
+-rw-r--r--   0 varun      (502) staff       (20)    14564 2023-03-06 15:30:09.000000 pylipd-1.0.6/pylipd/globals/schema.py
+-rw-r--r--   0 varun      (502) staff       (20)      197 2022-11-14 07:40:00.000000 pylipd-1.0.6/pylipd/globals/urls.py
+-rw-r--r--   0 varun      (502) staff       (20)    15901 2023-04-07 06:12:11.000000 pylipd-1.0.6/pylipd/legacy_utils.py
+-rw-r--r--   0 varun      (502) staff       (20)    28677 2023-04-07 04:11:12.000000 pylipd-1.0.6/pylipd/lipd.py
+-rw-r--r--   0 varun      (502) staff       (20)    42808 2023-03-31 15:11:12.000000 pylipd-1.0.6/pylipd/lipd_to_rdf.py
+-rw-r--r--   0 varun      (502) staff       (20)     1742 2023-04-07 05:39:21.000000 pylipd-1.0.6/pylipd/multi_processing.py
+-rw-r--r--   0 varun      (502) staff       (20)    17140 2023-02-23 13:16:36.000000 pylipd-1.0.6/pylipd/rdf_to_lipd.py
+drwxr-xr-x   0 varun      (502) staff       (20)        0 2023-04-07 06:13:27.903050 pylipd-1.0.6/pylipd/series/
+-rw-r--r--   0 varun      (502) staff       (20)        0 2023-01-10 17:13:31.000000 pylipd-1.0.6/pylipd/series/__init__.py
+-rw-r--r--   0 varun      (502) staff       (20)     3223 2022-11-15 20:06:27.000000 pylipd-1.0.6/pylipd/series/regexes.py
+-rw-r--r--   0 varun      (502) staff       (20)     2270 2023-03-22 17:52:14.000000 pylipd-1.0.6/pylipd/test.py
+-rw-r--r--   0 varun      (502) staff       (20)     4141 2023-04-07 05:57:19.000000 pylipd-1.0.6/pylipd/usage.py
+-rw-r--r--   0 varun      (502) staff       (20)     2602 2023-02-23 10:01:04.000000 pylipd-1.0.6/pylipd/utils.py
+drwxr-xr-x   0 varun      (502) staff       (20)        0 2023-04-07 06:13:27.903707 pylipd-1.0.6/pylipd.egg-info/
+-rw-r--r--   0 varun      (502) staff       (20)     1282 2023-04-07 06:13:27.000000 pylipd-1.0.6/pylipd.egg-info/PKG-INFO
+-rw-r--r--   0 varun      (502) staff       (20)      588 2023-04-07 06:13:27.000000 pylipd-1.0.6/pylipd.egg-info/SOURCES.txt
+-rw-r--r--   0 varun      (502) staff       (20)        1 2023-04-07 06:13:27.000000 pylipd-1.0.6/pylipd.egg-info/dependency_links.txt
+-rw-r--r--   0 varun      (502) staff       (20)        1 2023-02-24 09:46:52.000000 pylipd-1.0.6/pylipd.egg-info/not-zip-safe
+-rw-r--r--   0 varun      (502) staff       (20)       29 2023-04-07 06:13:27.000000 pylipd-1.0.6/pylipd.egg-info/requires.txt
+-rw-r--r--   0 varun      (502) staff       (20)        7 2023-04-07 06:13:27.000000 pylipd-1.0.6/pylipd.egg-info/top_level.txt
+-rw-r--r--   0 varun      (502) staff       (20)      104 2023-02-10 17:39:16.000000 pylipd-1.0.6/pyproject.toml
+-rw-r--r--   0 varun      (502) staff       (20)      686 2023-04-07 06:13:27.904103 pylipd-1.0.6/setup.cfg
+-rw-r--r--   0 varun      (502) staff       (20)      956 2023-04-07 06:13:22.000000 pylipd-1.0.6/setup.py
```

### Comparing `pylipd-1.0.5/LICENSE` & `pylipd-1.0.6/LICENSE`

 * *Files identical despite different names*

### Comparing `pylipd-1.0.5/PKG-INFO` & `pylipd-1.0.6/PKG-INFO`

 * *Files 8% similar despite different names*

```diff
@@ -1,13 +1,13 @@
 Metadata-Version: 2.1
 Name: pylipd
-Version: 1.0.5
+Version: 1.0.6
 Summary: Python utilities for handling LiPD data
 Home-page: https://github.com/linkedearth/pylipd
-Download-URL: https://github.com/linkedearth/pylipd/tarball/1.0.5
+Download-URL: https://github.com/linkedearth/pylipd/tarball/1.0.6
 Author: Varun Ratnakar
 Author-email: varunratnakar@gmail.com
 License: Apache 2-0 License
 Project-URL: Bug Tracker, https://github.com/linkedearth/pylipd/issues
 Keywords: Paleoclimate, Data Analysis, LiPD
 Classifier: Programming Language :: Python :: 3
 Classifier: License :: OSI Approved :: MIT License
```

### Comparing `pylipd-1.0.5/README.md` & `pylipd-1.0.6/README.md`

 * *Files identical despite different names*

### Comparing `pylipd-1.0.5/pylipd/globals/schema.py` & `pylipd-1.0.6/pylipd/globals/schema.py`

 * *Files identical despite different names*

### Comparing `pylipd-1.0.5/pylipd/legacy_utils.py` & `pylipd-1.0.6/pylipd/legacy_utils.py`

 * *Files 1% similar despite different names*

```diff
@@ -255,14 +255,17 @@
                 if "variableName" not in v:
                     continue
                 
                 s = ""
                 k = v["variableName"]
 
                 # special case for year bp, or any variation of it. Translate key to "age""
+                if type(k) is list:
+                    k = k[0]
+                    
                 if "bp" in k.lower():
                     s = "age"
 
                 # all other normal cases. clean key and set key.
                 elif any(x in k.lower() for x in ('age', 'depth', 'year', "yr", "distance_from_top", "distance")):
                     # Some keys have units hanging on them (i.e. 'year_ad', 'depth_cm'). We don't want units on the keys
                     if re_pandas_x_und.match(k):
```

### Comparing `pylipd-1.0.5/pylipd/lipd.py` & `pylipd-1.0.6/pylipd/lipd.py`

 * *Files identical despite different names*

### Comparing `pylipd-1.0.5/pylipd/lipd_to_rdf.py` & `pylipd-1.0.6/pylipd/lipd_to_rdf.py`

 * *Files identical despite different names*

### Comparing `pylipd-1.0.5/pylipd/multi_processing.py` & `pylipd-1.0.6/pylipd/multi_processing.py`

 * *Files identical despite different names*

### Comparing `pylipd-1.0.5/pylipd/rdf_to_lipd.py` & `pylipd-1.0.6/pylipd/rdf_to_lipd.py`

 * *Files identical despite different names*

### Comparing `pylipd-1.0.5/pylipd/series/regexes.py` & `pylipd-1.0.6/pylipd/series/regexes.py`

 * *Files identical despite different names*

### Comparing `pylipd-1.0.5/pylipd/test.py` & `pylipd-1.0.6/pylipd/test.py`

 * *Files identical despite different names*

### Comparing `pylipd-1.0.5/pylipd/usage.py` & `pylipd-1.0.6/pylipd/usage.py`

 * *Files identical despite different names*

### Comparing `pylipd-1.0.5/pylipd/utils.py` & `pylipd-1.0.6/pylipd/utils.py`

 * *Files identical despite different names*

### Comparing `pylipd-1.0.5/pylipd.egg-info/PKG-INFO` & `pylipd-1.0.6/pylipd.egg-info/PKG-INFO`

 * *Files 8% similar despite different names*

```diff
@@ -1,13 +1,13 @@
 Metadata-Version: 2.1
 Name: pylipd
-Version: 1.0.5
+Version: 1.0.6
 Summary: Python utilities for handling LiPD data
 Home-page: https://github.com/linkedearth/pylipd
-Download-URL: https://github.com/linkedearth/pylipd/tarball/1.0.5
+Download-URL: https://github.com/linkedearth/pylipd/tarball/1.0.6
 Author: Varun Ratnakar
 Author-email: varunratnakar@gmail.com
 License: Apache 2-0 License
 Project-URL: Bug Tracker, https://github.com/linkedearth/pylipd/issues
 Keywords: Paleoclimate, Data Analysis, LiPD
 Classifier: Programming Language :: Python :: 3
 Classifier: License :: OSI Approved :: MIT License
```

### Comparing `pylipd-1.0.5/pylipd.egg-info/SOURCES.txt` & `pylipd-1.0.6/pylipd.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `pylipd-1.0.5/setup.cfg` & `pylipd-1.0.6/setup.cfg`

 * *Files 23% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 [metadata]
 name = pylipd
-version = 1.0.5
+version = 1.0.6
 author = Varun Ratnakar
 author_email = varunratnakar@gmail.com
 description = Python utilities for handling LiPD data
 long_description = file: README.md
 long_description_content_type = text/markdown
 url = https://github.com/linkedearth/pylipd
 project_urls =
```

### Comparing `pylipd-1.0.5/setup.py` & `pylipd-1.0.6/setup.py`

 * *Files 17% similar despite different names*

```diff
@@ -1,13 +1,13 @@
 import os
 
 from setuptools import setup, find_packages
 
 
-version = '1.0.5'
+version = '1.0.6'
 
 # Read the readme file contents into variable
 def read(fname):
     return open(os.path.join(os.path.dirname(__file__), fname)).read()
 
 setup(
     name='pylipd',
```

