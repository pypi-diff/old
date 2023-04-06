# Comparing `tmp/geofred-0.1.1.tar.gz` & `tmp/geofred-0.1.2.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "geofred-0.1.1.tar", last modified: Fri Mar  3 17:07:33 2023, max compression
+gzip compressed data, was "geofred-0.1.2.tar", last modified: Thu Apr  6 19:10:32 2023, max compression
```

## Comparing `geofred-0.1.1.tar` & `geofred-0.1.2.tar`

### file list

```diff
@@ -1,22 +1,22 @@
-drwxr-xr-x   0 stevelee   (501) staff       (20)        0 2023-03-03 17:07:33.118977 geofred-0.1.1/
--rw-r--r--   0 stevelee   (501) staff       (20)     1073 2022-04-11 15:53:18.000000 geofred-0.1.1/LICENSE
--rw-r--r--   0 stevelee   (501) staff       (20)      413 2023-03-03 17:07:33.118427 geofred-0.1.1/PKG-INFO
--rwxr-xr-x   0 stevelee   (501) staff       (20)     2931 2022-08-04 16:10:01.000000 geofred-0.1.1/README.md
-drwxr-xr-x   0 stevelee   (501) staff       (20)        0 2023-03-03 17:07:33.094587 geofred-0.1.1/geofred/
--rwxr-xr-x   0 stevelee   (501) staff       (20)      101 2023-03-03 17:06:39.000000 geofred-0.1.1/geofred/__init__.py
--rwxrwxrwx   0 stevelee   (501) staff       (20)     2361 2023-03-03 17:03:52.000000 geofred-0.1.1/geofred/geofred.py
-drwxr-xr-x   0 stevelee   (501) staff       (20)        0 2023-03-03 17:07:33.117326 geofred-0.1.1/geofred/storage/
--rw-r--r--   0 stevelee   (501) staff       (20)        0 2022-04-11 21:21:36.000000 geofred-0.1.1/geofred/storage/__init__.py
--rwxrwxrwx   0 stevelee   (501) staff       (20)  6622736 2021-10-22 19:12:06.000000 geofred-0.1.1/geofred/storage/location_lookup.csv
--rwxr-xr-x   0 stevelee   (501) staff       (20)      602 2022-04-11 21:21:36.000000 geofred-0.1.1/geofred/storage/location_lookup.py
--rwxrwxrwx   0 stevelee   (501) staff       (20)      687 2023-03-03 16:50:02.000000 geofred-0.1.1/geofred/storage/state.csv
--rwxr-xr-x   0 stevelee   (501) staff       (20)      459 2023-03-03 17:00:33.000000 geofred-0.1.1/geofred/storage/state.py
--rwxr-xr-x   0 stevelee   (501) staff       (20)     7886 2023-03-03 17:00:19.000000 geofred-0.1.1/geofred/utils.py
-drwxr-xr-x   0 stevelee   (501) staff       (20)        0 2023-03-03 17:07:33.097293 geofred-0.1.1/geofred.egg-info/
--rw-r--r--   0 stevelee   (501) staff       (20)      413 2023-03-03 17:07:33.000000 geofred-0.1.1/geofred.egg-info/PKG-INFO
--rw-r--r--   0 stevelee   (501) staff       (20)      386 2023-03-03 17:07:33.000000 geofred-0.1.1/geofred.egg-info/SOURCES.txt
--rw-r--r--   0 stevelee   (501) staff       (20)        1 2023-03-03 17:07:33.000000 geofred-0.1.1/geofred.egg-info/dependency_links.txt
--rw-r--r--   0 stevelee   (501) staff       (20)       18 2023-03-03 17:07:33.000000 geofred-0.1.1/geofred.egg-info/requires.txt
--rw-r--r--   0 stevelee   (501) staff       (20)        8 2023-03-03 17:07:33.000000 geofred-0.1.1/geofred.egg-info/top_level.txt
--rw-r--r--   0 stevelee   (501) staff       (20)       38 2023-03-03 17:07:33.119123 geofred-0.1.1/setup.cfg
--rw-r--r--   0 stevelee   (501) staff       (20)      707 2023-03-03 17:06:02.000000 geofred-0.1.1/setup.py
+drwxr-xr-x   0 stevelee   (501) staff       (20)        0 2023-04-06 19:10:32.820245 geofred-0.1.2/
+-rw-r--r--   0 stevelee   (501) staff       (20)     1073 2022-04-11 15:53:18.000000 geofred-0.1.2/LICENSE
+-rw-r--r--   0 stevelee   (501) staff       (20)      413 2023-04-06 19:10:32.819745 geofred-0.1.2/PKG-INFO
+-rwxr-xr-x   0 stevelee   (501) staff       (20)     2931 2022-08-04 16:10:01.000000 geofred-0.1.2/README.md
+drwxr-xr-x   0 stevelee   (501) staff       (20)        0 2023-04-06 19:10:32.799984 geofred-0.1.2/geofred/
+-rwxr-xr-x   0 stevelee   (501) staff       (20)      101 2023-04-06 19:09:05.000000 geofred-0.1.2/geofred/__init__.py
+-rwxrwxrwx   0 stevelee   (501) staff       (20)     2361 2023-03-03 17:03:52.000000 geofred-0.1.2/geofred/geofred.py
+drwxr-xr-x   0 stevelee   (501) staff       (20)        0 2023-04-06 19:10:32.818672 geofred-0.1.2/geofred/storage/
+-rw-r--r--   0 stevelee   (501) staff       (20)        0 2022-04-11 21:21:36.000000 geofred-0.1.2/geofred/storage/__init__.py
+-rwxrwxrwx   0 stevelee   (501) staff       (20)  6622736 2021-10-22 19:12:06.000000 geofred-0.1.2/geofred/storage/location_lookup.csv
+-rwxr-xr-x   0 stevelee   (501) staff       (20)      602 2022-04-11 21:21:36.000000 geofred-0.1.2/geofred/storage/location_lookup.py
+-rwxrwxrwx   0 stevelee   (501) staff       (20)      687 2023-03-03 16:50:02.000000 geofred-0.1.2/geofred/storage/state.csv
+-rwxr-xr-x   0 stevelee   (501) staff       (20)      459 2023-03-03 17:00:33.000000 geofred-0.1.2/geofred/storage/state.py
+-rwxr-xr-x   0 stevelee   (501) staff       (20)     7886 2023-04-06 19:07:19.000000 geofred-0.1.2/geofred/utils.py
+drwxr-xr-x   0 stevelee   (501) staff       (20)        0 2023-04-06 19:10:32.804270 geofred-0.1.2/geofred.egg-info/
+-rw-r--r--   0 stevelee   (501) staff       (20)      413 2023-04-06 19:10:32.000000 geofred-0.1.2/geofred.egg-info/PKG-INFO
+-rw-r--r--   0 stevelee   (501) staff       (20)      386 2023-04-06 19:10:32.000000 geofred-0.1.2/geofred.egg-info/SOURCES.txt
+-rw-r--r--   0 stevelee   (501) staff       (20)        1 2023-04-06 19:10:32.000000 geofred-0.1.2/geofred.egg-info/dependency_links.txt
+-rw-r--r--   0 stevelee   (501) staff       (20)       18 2023-04-06 19:10:32.000000 geofred-0.1.2/geofred.egg-info/requires.txt
+-rw-r--r--   0 stevelee   (501) staff       (20)        8 2023-04-06 19:10:32.000000 geofred-0.1.2/geofred.egg-info/top_level.txt
+-rw-r--r--   0 stevelee   (501) staff       (20)       38 2023-04-06 19:10:32.820368 geofred-0.1.2/setup.cfg
+-rw-r--r--   0 stevelee   (501) staff       (20)      707 2023-04-06 19:09:15.000000 geofred-0.1.2/setup.py
```

### Comparing `geofred-0.1.1/LICENSE` & `geofred-0.1.2/LICENSE`

 * *Files identical despite different names*

### Comparing `geofred-0.1.1/README.md` & `geofred-0.1.2/README.md`

 * *Files identical despite different names*

### Comparing `geofred-0.1.1/geofred/geofred.py` & `geofred-0.1.2/geofred/geofred.py`

 * *Files identical despite different names*

### Comparing `geofred-0.1.1/geofred/storage/location_lookup.csv` & `geofred-0.1.2/geofred/storage/location_lookup.csv`

 * *Files identical despite different names*

### Comparing `geofred-0.1.1/geofred/storage/location_lookup.py` & `geofred-0.1.2/geofred/storage/location_lookup.py`

 * *Files identical despite different names*

### Comparing `geofred-0.1.1/geofred/storage/state.csv` & `geofred-0.1.2/geofred/storage/state.csv`

 * *Files identical despite different names*

### Comparing `geofred-0.1.1/geofred/utils.py` & `geofred-0.1.2/geofred/utils.py`

 * *Files 0% similar despite different names*

```diff
@@ -213,15 +213,15 @@
         result_dict[k] = v
     return result_dict
 
 
 def get_locations_df():
     from geofred.storage.location_lookup import DF_LOCATIONS
 
-    DF_LOCATIONS["zip"] = DF_LOCATIONS["zip"].apply(make_valid_zip)
+    DF_LOCATIONS["zip"] = DF_LOCATIONS["zip"].apply(make_valid_key)
     return DF_LOCATIONS
 
 
 def get_search_terms(series_name):
     terms = []
     for s in series_name:
         phrase = ""
```

### Comparing `geofred-0.1.1/setup.py` & `geofred-0.1.2/setup.py`

 * *Files 2% similar despite different names*

```diff
@@ -1,12 +1,12 @@
 from setuptools import setup, find_packages
 
 setup(
     name="geofred",
-    version="0.1.1",
+    version="0.1.2",
     description='A wrapper around "zachwill/fred" FRED API that provides easier handling of locations and aggregation types.',
     url="https://github.com/slee981/geofred",
     author="Stephen Lee",
     author_email="smlee.981@gmail.com",
     license="BSD 2-clause",
     packages=find_packages(include=["geofred", "geofred.storage"]),
     package_data={"geofred.storage": ["*.csv"]},
```

