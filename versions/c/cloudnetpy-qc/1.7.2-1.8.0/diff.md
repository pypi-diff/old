# Comparing `tmp/cloudnetpy_qc-1.7.2.tar.gz` & `tmp/cloudnetpy_qc-1.8.0.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "cloudnetpy_qc-1.7.2.tar", last modified: Fri Mar 10 10:07:20 2023, max compression
+gzip compressed data, was "cloudnetpy_qc-1.8.0.tar", last modified: Thu Apr  6 11:00:58 2023, max compression
```

## Comparing `cloudnetpy_qc-1.7.2.tar` & `cloudnetpy_qc-1.8.0.tar`

### file list

```diff
@@ -1,26 +1,26 @@
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-10 10:07:20.915552 cloudnetpy_qc-1.7.2/
--rw-r--r--   0 runner    (1001) docker     (123)     1094 2023-03-10 10:07:12.000000 cloudnetpy_qc-1.7.2/LICENSE
--rw-r--r--   0 runner    (1001) docker     (123)       56 2023-03-10 10:07:12.000000 cloudnetpy_qc-1.7.2/MANIFEST.in
--rw-r--r--   0 runner    (1001) docker     (123)     2044 2023-03-10 10:07:20.915552 cloudnetpy_qc-1.7.2/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)     1368 2023-03-10 10:07:12.000000 cloudnetpy_qc-1.7.2/README.md
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-10 10:07:20.911552 cloudnetpy_qc-1.7.2/cloudnetpy_qc/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-10 10:07:12.000000 cloudnetpy_qc-1.7.2/cloudnetpy_qc/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-10 10:07:20.915552 cloudnetpy_qc-1.7.2/cloudnetpy_qc/data/
--rw-r--r--   0 runner    (1001) docker     (123)    14435 2023-03-10 10:07:12.000000 cloudnetpy_qc-1.7.2/cloudnetpy_qc/data/area-type-table.xml
--rw-r--r--   0 runner    (1001) docker     (123)  4094783 2023-03-10 10:07:12.000000 cloudnetpy_qc-1.7.2/cloudnetpy_qc/data/cf-standard-name-table.xml
--rw-r--r--   0 runner    (1001) docker     (123)     1118 2023-03-10 10:07:12.000000 cloudnetpy_qc-1.7.2/cloudnetpy_qc/data/data_quality_config.ini
--rw-r--r--   0 runner    (1001) docker     (123)      169 2023-03-10 10:07:12.000000 cloudnetpy_qc-1.7.2/cloudnetpy_qc/data/metadata_config.ini
--rw-r--r--   0 runner    (1001) docker     (123)     6274 2023-03-10 10:07:12.000000 cloudnetpy_qc-1.7.2/cloudnetpy_qc/data/standardized-region-list.xml
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-10 10:07:12.000000 cloudnetpy_qc-1.7.2/cloudnetpy_qc/py.typed
--rw-r--r--   0 runner    (1001) docker     (123)    15883 2023-03-10 10:07:12.000000 cloudnetpy_qc-1.7.2/cloudnetpy_qc/quality.py
--rw-r--r--   0 runner    (1001) docker     (123)     1195 2023-03-10 10:07:12.000000 cloudnetpy_qc-1.7.2/cloudnetpy_qc/utils.py
--rw-r--r--   0 runner    (1001) docker     (123)    29881 2023-03-10 10:07:12.000000 cloudnetpy_qc-1.7.2/cloudnetpy_qc/variables.py
--rw-r--r--   0 runner    (1001) docker     (123)      100 2023-03-10 10:07:12.000000 cloudnetpy_qc-1.7.2/cloudnetpy_qc/version.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-10 10:07:20.911552 cloudnetpy_qc-1.7.2/cloudnetpy_qc.egg-info/
--rw-r--r--   0 runner    (1001) docker     (123)     2044 2023-03-10 10:07:20.000000 cloudnetpy_qc-1.7.2/cloudnetpy_qc.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)      586 2023-03-10 10:07:20.000000 cloudnetpy_qc-1.7.2/cloudnetpy_qc.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-03-10 10:07:20.000000 cloudnetpy_qc-1.7.2/cloudnetpy_qc.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (123)       63 2023-03-10 10:07:20.000000 cloudnetpy_qc-1.7.2/cloudnetpy_qc.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (123)       14 2023-03-10 10:07:20.000000 cloudnetpy_qc-1.7.2/cloudnetpy_qc.egg-info/top_level.txt
--rw-r--r--   0 runner    (1001) docker     (123)       38 2023-03-10 10:07:20.915552 cloudnetpy_qc-1.7.2/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (123)     1338 2023-03-10 10:07:12.000000 cloudnetpy_qc-1.7.2/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 11:00:58.369038 cloudnetpy_qc-1.8.0/
+-rw-r--r--   0 runner    (1001) docker     (123)     1094 2023-04-06 11:00:50.000000 cloudnetpy_qc-1.8.0/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (123)       56 2023-04-06 11:00:50.000000 cloudnetpy_qc-1.8.0/MANIFEST.in
+-rw-r--r--   0 runner    (1001) docker     (123)     2044 2023-04-06 11:00:58.369038 cloudnetpy_qc-1.8.0/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     1368 2023-04-06 11:00:50.000000 cloudnetpy_qc-1.8.0/README.md
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 11:00:58.361038 cloudnetpy_qc-1.8.0/cloudnetpy_qc/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 11:00:50.000000 cloudnetpy_qc-1.8.0/cloudnetpy_qc/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 11:00:58.369038 cloudnetpy_qc-1.8.0/cloudnetpy_qc/data/
+-rw-r--r--   0 runner    (1001) docker     (123)    14435 2023-04-06 11:00:50.000000 cloudnetpy_qc-1.8.0/cloudnetpy_qc/data/area-type-table.xml
+-rw-r--r--   0 runner    (1001) docker     (123)  4094783 2023-04-06 11:00:50.000000 cloudnetpy_qc-1.8.0/cloudnetpy_qc/data/cf-standard-name-table.xml
+-rw-r--r--   0 runner    (1001) docker     (123)     1118 2023-04-06 11:00:50.000000 cloudnetpy_qc-1.8.0/cloudnetpy_qc/data/data_quality_config.ini
+-rw-r--r--   0 runner    (1001) docker     (123)      169 2023-04-06 11:00:50.000000 cloudnetpy_qc-1.8.0/cloudnetpy_qc/data/metadata_config.ini
+-rw-r--r--   0 runner    (1001) docker     (123)     6274 2023-04-06 11:00:50.000000 cloudnetpy_qc-1.8.0/cloudnetpy_qc/data/standardized-region-list.xml
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 11:00:50.000000 cloudnetpy_qc-1.8.0/cloudnetpy_qc/py.typed
+-rw-r--r--   0 runner    (1001) docker     (123)    15826 2023-04-06 11:00:50.000000 cloudnetpy_qc-1.8.0/cloudnetpy_qc/quality.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1195 2023-04-06 11:00:50.000000 cloudnetpy_qc-1.8.0/cloudnetpy_qc/utils.py
+-rw-r--r--   0 runner    (1001) docker     (123)    29881 2023-04-06 11:00:50.000000 cloudnetpy_qc-1.8.0/cloudnetpy_qc/variables.py
+-rw-r--r--   0 runner    (1001) docker     (123)      100 2023-04-06 11:00:50.000000 cloudnetpy_qc-1.8.0/cloudnetpy_qc/version.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 11:00:58.365038 cloudnetpy_qc-1.8.0/cloudnetpy_qc.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)     2044 2023-04-06 11:00:58.000000 cloudnetpy_qc-1.8.0/cloudnetpy_qc.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)      586 2023-04-06 11:00:58.000000 cloudnetpy_qc-1.8.0/cloudnetpy_qc.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-06 11:00:58.000000 cloudnetpy_qc-1.8.0/cloudnetpy_qc.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       69 2023-04-06 11:00:58.000000 cloudnetpy_qc-1.8.0/cloudnetpy_qc.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       14 2023-04-06 11:00:58.000000 cloudnetpy_qc-1.8.0/cloudnetpy_qc.egg-info/top_level.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       38 2023-04-06 11:00:58.369038 cloudnetpy_qc-1.8.0/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (123)     1347 2023-04-06 11:00:50.000000 cloudnetpy_qc-1.8.0/setup.py
```

### Comparing `cloudnetpy_qc-1.7.2/LICENSE` & `cloudnetpy_qc-1.8.0/LICENSE`

 * *Files identical despite different names*

### Comparing `cloudnetpy_qc-1.7.2/PKG-INFO` & `cloudnetpy_qc-1.8.0/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: cloudnetpy_qc
-Version: 1.7.2
+Version: 1.8.0
 Summary: Quality control routines for CloudnetPy products
 Home-page: https://github.com/actris-cloudnet/cloudnetpy-qc
 Author: Finnish Meteorological Institute
 Author-email: actris-cloudnet@fmi.fi
 License: MIT License
 Classifier: Programming Language :: Python :: 3.10
 Classifier: Programming Language :: Python :: 3.11
```

### Comparing `cloudnetpy_qc-1.7.2/README.md` & `cloudnetpy_qc-1.8.0/README.md`

 * *Files identical despite different names*

### Comparing `cloudnetpy_qc-1.7.2/cloudnetpy_qc/data/area-type-table.xml` & `cloudnetpy_qc-1.8.0/cloudnetpy_qc/data/area-type-table.xml`

 * *Files identical despite different names*

### Comparing `cloudnetpy_qc-1.7.2/cloudnetpy_qc/data/cf-standard-name-table.xml` & `cloudnetpy_qc-1.8.0/cloudnetpy_qc/data/cf-standard-name-table.xml`

 * *Files identical despite different names*

### Comparing `cloudnetpy_qc-1.7.2/cloudnetpy_qc/data/data_quality_config.ini` & `cloudnetpy_qc-1.8.0/cloudnetpy_qc/data/data_quality_config.ini`

 * *Files identical despite different names*

### Comparing `cloudnetpy_qc-1.7.2/cloudnetpy_qc/data/standardized-region-list.xml` & `cloudnetpy_qc-1.8.0/cloudnetpy_qc/data/standardized-region-list.xml`

 * *Files identical despite different names*

### Comparing `cloudnetpy_qc-1.7.2/cloudnetpy_qc/quality.py` & `cloudnetpy_qc-1.8.0/cloudnetpy_qc/quality.py`

 * *Files 3% similar despite different names*

```diff
@@ -5,14 +5,15 @@
 import os
 from dataclasses import dataclass
 from enum import Enum
 from pathlib import Path
 
 import netCDF4
 import numpy as np
+import scipy.stats
 from numpy import ma
 
 from . import utils
 from .variables import VARIABLES, Product
 from .version import __version__
 
 DATA_PATH = os.path.join(os.path.dirname(__file__), "data")
@@ -361,26 +362,24 @@
                 self._add_message("LDR exists but all the values are invalid.")
 
 
 @test("Range correction", "Test that beta is range corrected.", products=[Product.LIDAR])
 class TestIfRangeCorrected(Test):
     def run(self):
         try:
-            data = self.nc["beta_raw"][:]
-        except IndexError:
+            range_var = self.nc["range"]
+            beta_raw = self.nc["beta_raw"]
+        except KeyError:
             return
-        noise_threshold = 2e-6
-        std_threshold = 1e-6
-        noise_ind = np.where(data < noise_threshold)
-        noise_std = float(np.std(data[noise_ind]))
-        if noise_std < std_threshold:
-            self._add_message(
-                f"Suspiciously low noise std ({utils.format_value(noise_std)}). "
-                f"Data might not be range-corrected."
-            )
+        n_top_ranges = 200
+        x = range_var[-n_top_ranges:] ** 2
+        y = np.std(beta_raw[:, -n_top_ranges:], axis=0)
+        res = scipy.stats.pearsonr(x, y)
+        if res.statistic < 0.5:
+            self._add_message("Data might not be range corrected.")
 
 
 @test(
     "Instrument PID",
     "Test that valid instrument PID exists.",
     ErrorLevel.WARNING,
     [Product.MWR, Product.LIDAR, Product.RADAR, Product.DISDROMETER],
```

### Comparing `cloudnetpy_qc-1.7.2/cloudnetpy_qc/utils.py` & `cloudnetpy_qc-1.8.0/cloudnetpy_qc/utils.py`

 * *Files identical despite different names*

### Comparing `cloudnetpy_qc-1.7.2/cloudnetpy_qc/variables.py` & `cloudnetpy_qc-1.8.0/cloudnetpy_qc/variables.py`

 * *Files identical despite different names*

### Comparing `cloudnetpy_qc-1.7.2/cloudnetpy_qc.egg-info/PKG-INFO` & `cloudnetpy_qc-1.8.0/cloudnetpy_qc.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: cloudnetpy-qc
-Version: 1.7.2
+Version: 1.8.0
 Summary: Quality control routines for CloudnetPy products
 Home-page: https://github.com/actris-cloudnet/cloudnetpy-qc
 Author: Finnish Meteorological Institute
 Author-email: actris-cloudnet@fmi.fi
 License: MIT License
 Classifier: Programming Language :: Python :: 3.10
 Classifier: Programming Language :: Python :: 3.11
```

### Comparing `cloudnetpy_qc-1.7.2/cloudnetpy_qc.egg-info/SOURCES.txt` & `cloudnetpy_qc-1.8.0/cloudnetpy_qc.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `cloudnetpy_qc-1.7.2/setup.py` & `cloudnetpy_qc-1.8.0/setup.py`

 * *Files 6% similar despite different names*

```diff
@@ -20,15 +20,15 @@
     author_email="actris-cloudnet@fmi.fi",
     url="https://github.com/actris-cloudnet/cloudnetpy-qc",
     license="MIT License",
     packages=find_packages(),
     include_package_data=True,
     setup_requires=["wheel"],
     python_requires=">=3.10",
-    install_requires=["numpy", "netCDF4", "cfchecker"],
+    install_requires=["numpy", "scipy", "netCDF4", "cfchecker"],
     extras_require={
         "test": [
             "pytest-flakefinder",
             "pylint",
             "mypy",
         ],
     },
```

