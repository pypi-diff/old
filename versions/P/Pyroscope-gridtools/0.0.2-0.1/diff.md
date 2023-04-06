# Comparing `tmp/Pyroscope-gridtools-0.0.2.tar.gz` & `tmp/Pyroscope-gridtools-0.1.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "dist/Pyroscope-gridtools-0.0.2.tar", last modified: Thu Apr  6 23:37:16 2023, max compression
+gzip compressed data, was "dist/Pyroscope-gridtools-0.1.tar", last modified: Thu Apr  6 23:23:40 2023, max compression
```

## Comparing `Pyroscope-gridtools-0.0.2.tar` & `Pyroscope-gridtools-0.1.tar`

### file list

```diff
@@ -1,22 +1,22 @@
-drwxrwxrwx   0 szhao007  (1000) szhao007  (1000)        0 2023-04-06 23:37:16.766804 Pyroscope-gridtools-0.0.2/
--rwxrwxrwx   0 szhao007  (1000) szhao007  (1000)      775 2023-04-06 23:37:16.759807 Pyroscope-gridtools-0.0.2/PKG-INFO
-drwxrwxrwx   0 szhao007  (1000) szhao007  (1000)        0 2023-04-06 23:37:16.528424 Pyroscope-gridtools-0.0.2/Pyroscope-gridtools/
--rwxrwxrwx   0 szhao007  (1000) szhao007  (1000)        0 2022-02-04 10:40:28.000000 Pyroscope-gridtools-0.0.2/Pyroscope-gridtools/__init__.py
--rwxrwxrwx   0 szhao007  (1000) szhao007  (1000)     2106 2023-04-06 22:27:16.000000 Pyroscope-gridtools-0.0.2/Pyroscope-gridtools/fileparser.py
--rwxrwxrwx   0 szhao007  (1000) szhao007  (1000)     6434 2023-04-06 22:28:48.000000 Pyroscope-gridtools-0.0.2/Pyroscope-gridtools/filter_data.py
--rwxrwxrwx   0 szhao007  (1000) szhao007  (1000)    28897 2023-04-06 22:47:52.000000 Pyroscope-gridtools-0.0.2/Pyroscope-gridtools/grid_ncf.py
--rwxrwxrwx   0 szhao007  (1000) szhao007  (1000)     6061 2023-04-06 23:34:18.000000 Pyroscope-gridtools-0.0.2/Pyroscope-gridtools/gridding.py
--rwxrwxrwx   0 szhao007  (1000) szhao007  (1000)    26095 2023-04-06 22:47:32.000000 Pyroscope-gridtools-0.0.2/Pyroscope-gridtools/gtools.py
--rwxrwxrwx   0 szhao007  (1000) szhao007  (1000)     8250 2023-04-06 22:40:51.000000 Pyroscope-gridtools-0.0.2/Pyroscope-gridtools/naming_conventions.py
--rwxrwxrwx   0 szhao007  (1000) szhao007  (1000)     8107 2023-04-06 23:14:16.000000 Pyroscope-gridtools-0.0.2/Pyroscope-gridtools/sat_data_input.py
--rwxrwxrwx   0 szhao007  (1000) szhao007  (1000)     7531 2023-04-06 23:14:29.000000 Pyroscope-gridtools-0.0.2/Pyroscope-gridtools/solar_zenith.py
--rwxrwxrwx   0 szhao007  (1000) szhao007  (1000)     3166 2023-04-06 22:45:00.000000 Pyroscope-gridtools-0.0.2/Pyroscope-gridtools/time_conv.py
-drwxrwxrwx   0 szhao007  (1000) szhao007  (1000)        0 2023-04-06 23:37:16.717874 Pyroscope-gridtools-0.0.2/Pyroscope_gridtools.egg-info/
--rwxrwxrwx   0 szhao007  (1000) szhao007  (1000)      775 2023-04-06 23:37:15.000000 Pyroscope-gridtools-0.0.2/Pyroscope_gridtools.egg-info/PKG-INFO
--rwxrwxrwx   0 szhao007  (1000) szhao007  (1000)      576 2023-04-06 23:37:15.000000 Pyroscope-gridtools-0.0.2/Pyroscope_gridtools.egg-info/SOURCES.txt
--rwxrwxrwx   0 szhao007  (1000) szhao007  (1000)        1 2023-04-06 23:37:15.000000 Pyroscope-gridtools-0.0.2/Pyroscope_gridtools.egg-info/dependency_links.txt
--rwxrwxrwx   0 szhao007  (1000) szhao007  (1000)       52 2023-04-06 23:37:15.000000 Pyroscope-gridtools-0.0.2/Pyroscope_gridtools.egg-info/requires.txt
--rwxrwxrwx   0 szhao007  (1000) szhao007  (1000)       20 2023-04-06 23:37:15.000000 Pyroscope-gridtools-0.0.2/Pyroscope_gridtools.egg-info/top_level.txt
--rwxrwxrwx   0 szhao007  (1000) szhao007  (1000)     9962 2023-04-06 22:20:54.000000 Pyroscope-gridtools-0.0.2/README.md
--rwxrwxrwx   0 szhao007  (1000) szhao007  (1000)       38 2023-04-06 23:37:16.768854 Pyroscope-gridtools-0.0.2/setup.cfg
--rwxrwxrwx   0 szhao007  (1000) szhao007  (1000)     1702 2023-04-06 23:37:12.000000 Pyroscope-gridtools-0.0.2/setup.py
+drwxrwxrwx   0 szhao007  (1000) szhao007  (1000)        0 2023-04-06 23:23:40.200537 Pyroscope-gridtools-0.1/
+-rwxrwxrwx   0 szhao007  (1000) szhao007  (1000)      773 2023-04-06 23:23:40.191071 Pyroscope-gridtools-0.1/PKG-INFO
+drwxrwxrwx   0 szhao007  (1000) szhao007  (1000)        0 2023-04-06 23:23:39.975088 Pyroscope-gridtools-0.1/Pyroscope-gridtools/
+-rwxrwxrwx   0 szhao007  (1000) szhao007  (1000)        0 2022-02-04 10:40:28.000000 Pyroscope-gridtools-0.1/Pyroscope-gridtools/__init__.py
+-rwxrwxrwx   0 szhao007  (1000) szhao007  (1000)     2106 2023-04-06 22:27:16.000000 Pyroscope-gridtools-0.1/Pyroscope-gridtools/fileparser.py
+-rwxrwxrwx   0 szhao007  (1000) szhao007  (1000)     6434 2023-04-06 22:28:48.000000 Pyroscope-gridtools-0.1/Pyroscope-gridtools/filter_data.py
+-rwxrwxrwx   0 szhao007  (1000) szhao007  (1000)    28897 2023-04-06 22:47:52.000000 Pyroscope-gridtools-0.1/Pyroscope-gridtools/grid_ncf.py
+-rwxrwxrwx   0 szhao007  (1000) szhao007  (1000)    10251 2023-04-06 23:12:45.000000 Pyroscope-gridtools-0.1/Pyroscope-gridtools/gridding.py
+-rwxrwxrwx   0 szhao007  (1000) szhao007  (1000)    26095 2023-04-06 22:47:32.000000 Pyroscope-gridtools-0.1/Pyroscope-gridtools/gtools.py
+-rwxrwxrwx   0 szhao007  (1000) szhao007  (1000)     8250 2023-04-06 22:40:51.000000 Pyroscope-gridtools-0.1/Pyroscope-gridtools/naming_conventions.py
+-rwxrwxrwx   0 szhao007  (1000) szhao007  (1000)     8107 2023-04-06 23:14:16.000000 Pyroscope-gridtools-0.1/Pyroscope-gridtools/sat_data_input.py
+-rwxrwxrwx   0 szhao007  (1000) szhao007  (1000)     7531 2023-04-06 23:14:29.000000 Pyroscope-gridtools-0.1/Pyroscope-gridtools/solar_zenith.py
+-rwxrwxrwx   0 szhao007  (1000) szhao007  (1000)     3166 2023-04-06 22:45:00.000000 Pyroscope-gridtools-0.1/Pyroscope-gridtools/time_conv.py
+drwxrwxrwx   0 szhao007  (1000) szhao007  (1000)        0 2023-04-06 23:23:40.155487 Pyroscope-gridtools-0.1/Pyroscope_gridtools.egg-info/
+-rwxrwxrwx   0 szhao007  (1000) szhao007  (1000)      773 2023-04-06 23:23:38.000000 Pyroscope-gridtools-0.1/Pyroscope_gridtools.egg-info/PKG-INFO
+-rwxrwxrwx   0 szhao007  (1000) szhao007  (1000)      576 2023-04-06 23:23:39.000000 Pyroscope-gridtools-0.1/Pyroscope_gridtools.egg-info/SOURCES.txt
+-rwxrwxrwx   0 szhao007  (1000) szhao007  (1000)        1 2023-04-06 23:23:38.000000 Pyroscope-gridtools-0.1/Pyroscope_gridtools.egg-info/dependency_links.txt
+-rwxrwxrwx   0 szhao007  (1000) szhao007  (1000)       57 2023-04-06 23:23:38.000000 Pyroscope-gridtools-0.1/Pyroscope_gridtools.egg-info/requires.txt
+-rwxrwxrwx   0 szhao007  (1000) szhao007  (1000)       20 2023-04-06 23:23:38.000000 Pyroscope-gridtools-0.1/Pyroscope_gridtools.egg-info/top_level.txt
+-rwxrwxrwx   0 szhao007  (1000) szhao007  (1000)     9962 2023-04-06 22:20:54.000000 Pyroscope-gridtools-0.1/README.md
+-rwxrwxrwx   0 szhao007  (1000) szhao007  (1000)       38 2023-04-06 23:23:40.203396 Pyroscope-gridtools-0.1/setup.cfg
+-rwxrwxrwx   0 szhao007  (1000) szhao007  (1000)     1614 2023-04-06 23:23:23.000000 Pyroscope-gridtools-0.1/setup.py
```

### Comparing `Pyroscope-gridtools-0.0.2/PKG-INFO` & `Pyroscope-gridtools-0.1/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 1.1
 Name: Pyroscope-gridtools
-Version: 0.0.2
+Version: 0.1
 Summary: Data fusion package for transforming L2 satellite to L3 spatial-temporal gridded data
 Home-page: https://github.com/jwei-openscapes/aerosol-data-fusion
 Author: Sally Zhao, Neil Gutkin
 Author-email: zhaosally0@gmail.com
 License: MIT
 Description: UNKNOWN
 Keywords: data fusion,satellite,L2,L3
```

### Comparing `Pyroscope-gridtools-0.0.2/Pyroscope-gridtools/fileparser.py` & `Pyroscope-gridtools-0.1/Pyroscope-gridtools/fileparser.py`

 * *Files identical despite different names*

### Comparing `Pyroscope-gridtools-0.0.2/Pyroscope-gridtools/filter_data.py` & `Pyroscope-gridtools-0.1/Pyroscope-gridtools/filter_data.py`

 * *Files identical despite different names*

### Comparing `Pyroscope-gridtools-0.0.2/Pyroscope-gridtools/grid_ncf.py` & `Pyroscope-gridtools-0.1/Pyroscope-gridtools/grid_ncf.py`

 * *Files identical despite different names*

### Comparing `Pyroscope-gridtools-0.0.2/Pyroscope-gridtools/gtools.py` & `Pyroscope-gridtools-0.1/Pyroscope-gridtools/gtools.py`

 * *Files identical despite different names*

### Comparing `Pyroscope-gridtools-0.0.2/Pyroscope-gridtools/naming_conventions.py` & `Pyroscope-gridtools-0.1/Pyroscope-gridtools/naming_conventions.py`

 * *Files identical despite different names*

### Comparing `Pyroscope-gridtools-0.0.2/Pyroscope-gridtools/sat_data_input.py` & `Pyroscope-gridtools-0.1/Pyroscope-gridtools/sat_data_input.py`

 * *Files identical despite different names*

### Comparing `Pyroscope-gridtools-0.0.2/Pyroscope-gridtools/solar_zenith.py` & `Pyroscope-gridtools-0.1/Pyroscope-gridtools/solar_zenith.py`

 * *Files identical despite different names*

### Comparing `Pyroscope-gridtools-0.0.2/Pyroscope-gridtools/time_conv.py` & `Pyroscope-gridtools-0.1/Pyroscope-gridtools/time_conv.py`

 * *Files identical despite different names*

### Comparing `Pyroscope-gridtools-0.0.2/Pyroscope_gridtools.egg-info/PKG-INFO` & `Pyroscope-gridtools-0.1/Pyroscope_gridtools.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 1.1
 Name: Pyroscope-gridtools
-Version: 0.0.2
+Version: 0.1
 Summary: Data fusion package for transforming L2 satellite to L3 spatial-temporal gridded data
 Home-page: https://github.com/jwei-openscapes/aerosol-data-fusion
 Author: Sally Zhao, Neil Gutkin
 Author-email: zhaosally0@gmail.com
 License: MIT
 Description: UNKNOWN
 Keywords: data fusion,satellite,L2,L3
```

### Comparing `Pyroscope-gridtools-0.0.2/Pyroscope_gridtools.egg-info/SOURCES.txt` & `Pyroscope-gridtools-0.1/Pyroscope_gridtools.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `Pyroscope-gridtools-0.0.2/README.md` & `Pyroscope-gridtools-0.1/README.md`

 * *Files identical despite different names*

### Comparing `Pyroscope-gridtools-0.0.2/setup.py` & `Pyroscope-gridtools-0.1/setup.py`

 * *Files 9% similar despite different names*

```diff
@@ -1,30 +1,30 @@
 from setuptools import setup, find_packages
 import codecs
 import os
 
-VERSION = '0.0.2'
+VERSION = '0.0.1'
 DESCRIPTION = 'Data fusion package for satellite data transformation.'
-LONG_DESCRIPTION = 'Data fusion package for transforming L2 satellite to L3 spatial-temporal gridded data'
-#LONG_DESCRIPTION = 'Data fusion package for transforming L2 satellite to L3 spatial-temporal gridded data.'
+LONG_DESCRIPTION = 'Data fusion package for transforming L2 satellite to L3 spatial-temporal gridded data.'
 
 # Setting up
 setup(
     name = 'Pyroscope-gridtools',         # Package name
     packages = ['Pyroscope-gridtools'],   
-    version = '0.0.2',      # Initial version
+    version = '0.1',      # Initial version
     license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
-    description = 'Data fusion package for transforming L2 satellite to L3 spatial-temporal gridded data',
+    description = 'Data fusion package for transforming L2 satellite to L3 spatial-temporal gridded data',  
     author = 'Sally Zhao, Neil Gutkin',                 
     author_email = 'zhaosally0@gmail.com',     
     url = 'https://github.com/jwei-openscapes/aerosol-data-fusion',   # github repository  
     keywords = ['data fusion', 'satellite', 'L2', 'L3'],   # Keywords
     install_requires=[            
             'numpy',
             'joblib',
+            'cuda',
             'netCDF4',
             'pyhdf',
             'pyyaml',
             'numba',
             'os', 
             'argparse'
         ],
```

