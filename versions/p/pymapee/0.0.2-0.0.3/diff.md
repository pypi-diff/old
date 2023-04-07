# Comparing `tmp/pymapee-0.0.2.tar.gz` & `tmp/pymapee-0.0.3.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "pymapee-0.0.2.tar", last modified: Mon Apr  3 20:18:38 2023, max compression
+gzip compressed data, was "pymapee-0.0.3.tar", last modified: Fri Apr  7 10:12:17 2023, max compression
```

## Comparing `pymapee-0.0.2.tar` & `pymapee-0.0.3.tar`

### file list

```diff
@@ -1,48 +1,49 @@
-drwxrwxrwx   0        0        0        0 2023-04-03 20:18:38.077297 pymapee-0.0.2/
--rw-rw-rw-   0        0        0      313 2023-04-01 08:23:17.000000 pymapee-0.0.2/.editorconfig
-drwxrwxrwx   0        0        0        0 2023-04-03 20:18:38.017275 pymapee-0.0.2/.github/
-drwxrwxrwx   0        0        0        0 2023-04-03 20:18:38.030370 pymapee-0.0.2/.github/ISSUE_TEMPLATE/
--rw-rw-rw-   0        0        0      532 2023-04-01 08:23:17.000000 pymapee-0.0.2/.github/ISSUE_TEMPLATE/bug_report.md
--rw-rw-rw-   0        0        0      510 2023-04-01 08:23:17.000000 pymapee-0.0.2/.github/ISSUE_TEMPLATE/config.yml
--rw-rw-rw-   0        0        0      459 2023-04-01 08:23:17.000000 pymapee-0.0.2/.github/ISSUE_TEMPLATE/feature_request.md
-drwxrwxrwx   0        0        0        0 2023-04-03 20:18:38.030370 pymapee-0.0.2/.github/workflows/
--rw-rw-rw-   0        0        0     1439 2023-04-01 08:23:17.000000 pymapee-0.0.2/.github/workflows/build.yml
--rw-rw-rw-   0        0        0      872 2023-04-01 08:23:17.000000 pymapee-0.0.2/.github/workflows/docs.yml
--rw-rw-rw-   0        0        0     1032 2023-04-01 08:23:17.000000 pymapee-0.0.2/.github/workflows/pypi.yml
--rw-rw-rw-   0        0        0     1345 2023-04-03 20:02:52.000000 pymapee-0.0.2/.gitignore
--rw-rw-rw-   0        0        0      168 2023-04-01 08:23:17.000000 pymapee-0.0.2/AUTHORS.rst
--rw-rw-rw-   0        0        0     1089 2023-04-01 08:23:17.000000 pymapee-0.0.2/LICENSE
--rw-rw-rw-   0        0        0      129 2023-04-01 08:23:17.000000 pymapee-0.0.2/MANIFEST.in
--rw-rw-rw-   0        0        0     2886 2023-04-03 20:18:38.077297 pymapee-0.0.2/PKG-INFO
--rw-rw-rw-   0        0        0     1756 2023-04-03 20:01:14.000000 pymapee-0.0.2/README.md
-drwxrwxrwx   0        0        0        0 2023-04-03 20:18:38.046069 pymapee-0.0.2/docs/
--rw-rw-rw-   0        0        0       29 2023-04-01 08:23:17.000000 pymapee-0.0.2/docs/authors.rst
--rw-rw-rw-   0        0        0       96 2023-04-01 08:23:17.000000 pymapee-0.0.2/docs/changelog.md
--rw-rw-rw-   0        0        0     3242 2023-04-01 08:23:17.000000 pymapee-0.0.2/docs/contributing.md
--rw-rw-rw-   0        0        0        7 2023-04-01 08:23:17.000000 pymapee-0.0.2/docs/faq.md
--rw-rw-rw-   0        0        0      653 2023-04-01 08:23:17.000000 pymapee-0.0.2/docs/index.md
--rw-rw-rw-   0        0        0      613 2023-04-01 08:23:17.000000 pymapee-0.0.2/docs/installation.md
-drwxrwxrwx   0        0        0        0 2023-04-03 20:18:38.046069 pymapee-0.0.2/docs/overrides/
--rw-rw-rw-   0        0        0      285 2023-04-01 08:23:17.000000 pymapee-0.0.2/docs/overrides/main.html
--rw-rw-rw-   0        0        0       42 2023-04-01 08:23:17.000000 pymapee-0.0.2/docs/pymapee.md
--rw-rw-rw-   0        0        0       69 2023-04-01 08:23:17.000000 pymapee-0.0.2/docs/usage.md
-drwxrwxrwx   0        0        0        0 2023-04-03 20:18:38.046069 pymapee-0.0.2/examples/
--rw-rw-rw-   0        0        0    15528 2023-04-03 17:59:09.000000 pymapee-0.0.2/examples/Notebook 01. Cloud masking and vegetation indices.ipynb
--rw-rw-rw-   0        0        0     1211 2023-04-01 08:23:17.000000 pymapee-0.0.2/mkdocs.yml
-drwxrwxrwx   0        0        0        0 2023-04-03 20:18:38.061673 pymapee-0.0.2/pymapee/
--rw-rw-rw-   0        0        0      189 2023-04-03 20:06:51.000000 pymapee-0.0.2/pymapee/__init__.py
--rw-rw-rw-   0        0        0     9180 2023-04-03 19:16:19.000000 pymapee-0.0.2/pymapee/pymapee.py
--rw-rw-rw-   0        0        0     5936 2023-04-03 12:33:55.000000 pymapee-0.0.2/pymapee/utils.py
-drwxrwxrwx   0        0        0        0 2023-04-03 20:18:38.077297 pymapee-0.0.2/pymapee.egg-info/
--rw-rw-rw-   0        0        0     2886 2023-04-03 20:18:37.000000 pymapee-0.0.2/pymapee.egg-info/PKG-INFO
--rw-rw-rw-   0        0        0      802 2023-04-03 20:18:37.000000 pymapee-0.0.2/pymapee.egg-info/SOURCES.txt
--rw-rw-rw-   0        0        0        1 2023-04-03 20:18:37.000000 pymapee-0.0.2/pymapee.egg-info/dependency_links.txt
--rw-rw-rw-   0        0        0        2 2023-04-02 19:42:09.000000 pymapee-0.0.2/pymapee.egg-info/not-zip-safe
--rw-rw-rw-   0        0        0        8 2023-04-03 20:18:37.000000 pymapee-0.0.2/pymapee.egg-info/top_level.txt
--rw-rw-rw-   0        0        0        0 2023-04-01 08:23:17.000000 pymapee-0.0.2/requirements.txt
--rw-rw-rw-   0        0        0      103 2023-04-01 08:23:17.000000 pymapee-0.0.2/requirements_dev.txt
--rw-rw-rw-   0        0        0      478 2023-04-03 20:18:38.077297 pymapee-0.0.2/setup.cfg
--rw-rw-rw-   0        0        0     1867 2023-04-03 20:18:24.000000 pymapee-0.0.2/setup.py
-drwxrwxrwx   0        0        0        0 2023-04-03 20:18:38.077297 pymapee-0.0.2/tests/
--rw-rw-rw-   0        0        0       38 2023-04-01 08:23:17.000000 pymapee-0.0.2/tests/__init__.py
--rw-rw-rw-   0        0        0      577 2023-04-01 08:23:17.000000 pymapee-0.0.2/tests/test_pymapee.py
+drwxrwxrwx   0        0        0        0 2023-04-07 10:12:17.073967 pymapee-0.0.3/
+-rw-rw-rw-   0        0        0      313 2023-04-01 08:23:17.000000 pymapee-0.0.3/.editorconfig
+drwxrwxrwx   0        0        0        0 2023-04-07 10:12:16.554181 pymapee-0.0.3/.github/
+drwxrwxrwx   0        0        0        0 2023-04-07 10:12:16.697521 pymapee-0.0.3/.github/ISSUE_TEMPLATE/
+-rw-rw-rw-   0        0        0      532 2023-04-01 08:23:17.000000 pymapee-0.0.3/.github/ISSUE_TEMPLATE/bug_report.md
+-rw-rw-rw-   0        0        0      510 2023-04-01 08:23:17.000000 pymapee-0.0.3/.github/ISSUE_TEMPLATE/config.yml
+-rw-rw-rw-   0        0        0      459 2023-04-01 08:23:17.000000 pymapee-0.0.3/.github/ISSUE_TEMPLATE/feature_request.md
+drwxrwxrwx   0        0        0        0 2023-04-07 10:12:16.809593 pymapee-0.0.3/.github/workflows/
+-rw-rw-rw-   0        0        0     1439 2023-04-01 08:23:17.000000 pymapee-0.0.3/.github/workflows/build.yml
+-rw-rw-rw-   0        0        0      872 2023-04-01 08:23:17.000000 pymapee-0.0.3/.github/workflows/docs.yml
+-rw-rw-rw-   0        0        0     1032 2023-04-01 08:23:17.000000 pymapee-0.0.3/.github/workflows/pypi.yml
+-rw-rw-rw-   0        0        0     1345 2023-04-03 20:02:52.000000 pymapee-0.0.3/.gitignore
+-rw-rw-rw-   0        0        0      168 2023-04-01 08:23:17.000000 pymapee-0.0.3/AUTHORS.rst
+-rw-rw-rw-   0        0        0     1089 2023-04-01 08:23:17.000000 pymapee-0.0.3/LICENSE
+-rw-rw-rw-   0        0        0      129 2023-04-01 08:23:17.000000 pymapee-0.0.3/MANIFEST.in
+-rw-rw-rw-   0        0        0     3248 2023-04-07 10:12:17.074997 pymapee-0.0.3/PKG-INFO
+-rw-rw-rw-   0        0        0     2102 2023-04-07 09:30:29.000000 pymapee-0.0.3/README.md
+drwxrwxrwx   0        0        0        0 2023-04-07 10:12:16.976147 pymapee-0.0.3/docs/
+-rw-rw-rw-   0        0        0       29 2023-04-01 08:23:17.000000 pymapee-0.0.3/docs/authors.rst
+-rw-rw-rw-   0        0        0       96 2023-04-01 08:23:17.000000 pymapee-0.0.3/docs/changelog.md
+-rw-rw-rw-   0        0        0     3242 2023-04-01 08:23:17.000000 pymapee-0.0.3/docs/contributing.md
+-rw-rw-rw-   0        0        0        7 2023-04-01 08:23:17.000000 pymapee-0.0.3/docs/faq.md
+-rw-rw-rw-   0        0        0      653 2023-04-01 08:23:17.000000 pymapee-0.0.3/docs/index.md
+-rw-rw-rw-   0        0        0      613 2023-04-01 08:23:17.000000 pymapee-0.0.3/docs/installation.md
+drwxrwxrwx   0        0        0        0 2023-04-07 10:12:16.988955 pymapee-0.0.3/docs/overrides/
+-rw-rw-rw-   0        0        0      285 2023-04-01 08:23:17.000000 pymapee-0.0.3/docs/overrides/main.html
+-rw-rw-rw-   0        0        0       42 2023-04-01 08:23:17.000000 pymapee-0.0.3/docs/pymapee.md
+-rw-rw-rw-   0        0        0       69 2023-04-01 08:23:17.000000 pymapee-0.0.3/docs/usage.md
+drwxrwxrwx   0        0        0        0 2023-04-07 10:12:17.019386 pymapee-0.0.3/examples/
+-rw-rw-rw-   0        0        0    15528 2023-04-03 17:59:09.000000 pymapee-0.0.3/examples/Notebook 01. Cloud masking and vegetation indices.ipynb
+-rw-rw-rw-   0        0        0     1211 2023-04-01 08:23:17.000000 pymapee-0.0.3/mkdocs.yml
+drwxrwxrwx   0        0        0        0 2023-04-07 10:12:17.028392 pymapee-0.0.3/pymapee/
+-rw-rw-rw-   0        0        0      189 2023-04-07 10:03:26.000000 pymapee-0.0.3/pymapee/__init__.py
+-rw-rw-rw-   0        0        0    12099 2023-04-04 21:05:55.000000 pymapee-0.0.3/pymapee/pymapee.py
+-rw-rw-rw-   0        0        0     6880 2023-04-04 21:05:15.000000 pymapee-0.0.3/pymapee/utils.py
+drwxrwxrwx   0        0        0        0 2023-04-07 10:12:17.068715 pymapee-0.0.3/pymapee.egg-info/
+-rw-rw-rw-   0        0        0     3248 2023-04-07 10:12:16.000000 pymapee-0.0.3/pymapee.egg-info/PKG-INFO
+-rw-rw-rw-   0        0        0      832 2023-04-07 10:12:16.000000 pymapee-0.0.3/pymapee.egg-info/SOURCES.txt
+-rw-rw-rw-   0        0        0       27 2023-04-07 10:12:16.000000 pymapee-0.0.3/pymapee.egg-info/dependency_links.txt
+-rw-rw-rw-   0        0        0        2 2023-04-02 19:42:09.000000 pymapee-0.0.3/pymapee.egg-info/not-zip-safe
+-rw-rw-rw-   0        0        0       25 2023-04-07 10:12:16.000000 pymapee-0.0.3/pymapee.egg-info/requires.txt
+-rw-rw-rw-   0        0        0        8 2023-04-07 10:12:16.000000 pymapee-0.0.3/pymapee.egg-info/top_level.txt
+-rw-rw-rw-   0        0        0       26 2023-04-07 10:12:06.000000 pymapee-0.0.3/requirements.txt
+-rw-rw-rw-   0        0        0      103 2023-04-01 08:23:17.000000 pymapee-0.0.3/requirements_dev.txt
+-rw-rw-rw-   0        0        0      478 2023-04-07 10:12:17.076965 pymapee-0.0.3/setup.cfg
+-rw-rw-rw-   0        0        0     1867 2023-04-07 10:03:31.000000 pymapee-0.0.3/setup.py
+drwxrwxrwx   0        0        0        0 2023-04-07 10:12:17.072958 pymapee-0.0.3/tests/
+-rw-rw-rw-   0        0        0       38 2023-04-01 08:23:17.000000 pymapee-0.0.3/tests/__init__.py
+-rw-rw-rw-   0        0        0      577 2023-04-01 08:23:17.000000 pymapee-0.0.3/tests/test_pymapee.py
```

### Comparing `pymapee-0.0.2/.github/ISSUE_TEMPLATE/bug_report.md` & `pymapee-0.0.3/.github/ISSUE_TEMPLATE/bug_report.md`

 * *Files identical despite different names*

### Comparing `pymapee-0.0.2/.github/workflows/build.yml` & `pymapee-0.0.3/.github/workflows/build.yml`

 * *Files identical despite different names*

### Comparing `pymapee-0.0.2/.github/workflows/docs.yml` & `pymapee-0.0.3/.github/workflows/docs.yml`

 * *Files identical despite different names*

### Comparing `pymapee-0.0.2/.github/workflows/pypi.yml` & `pymapee-0.0.3/.github/workflows/pypi.yml`

 * *Files identical despite different names*

### Comparing `pymapee-0.0.2/.gitignore` & `pymapee-0.0.3/.gitignore`

 * *Files identical despite different names*

### Comparing `pymapee-0.0.2/LICENSE` & `pymapee-0.0.3/LICENSE`

 * *Files identical despite different names*

### Comparing `pymapee-0.0.2/PKG-INFO` & `pymapee-0.0.3/PKG-INFO`

 * *Files 21% similar despite different names*

```diff
@@ -1,25 +1,26 @@
 Metadata-Version: 2.1
 Name: pymapee
-Version: 0.0.2
+Version: 0.0.3
 Summary: A Simple Python package to pre-processing satellite data using Google Earth Engine.
 Home-page: https://github.com/tuyenhavan/pymapee
 Author: Tuyen Ha
 Author-email: tuyenmassey@gmail.com
 License: MIT license
-Description: # pymapee
-        
+Description: # Welcome to pymapee
         
         [![image](https://img.shields.io/pypi/v/pymapee.svg)](https://pypi.python.org/pypi/pymapee)
         [![image](https://img.shields.io/conda/vn/conda-forge/pymapee.svg)](https://anaconda.org/conda-forge/pymapee)
-        
-        [![image](https://pyup.io/repos/github/tuyenhavan/pymapee/shield.svg)](https://pyup.io/repos/github/tuyenhavan/pymapee)
+        [![image](https://pepy.tech/badge/pymapee)](https://pepy.tech/project/pymapee)
+        [![image](https://github.com/tuyenhavan/pymapee/workflows/docs/badge.svg)](https://pymapee.org)
+        [![image](https://github.com/tuyenhavan/pymapee/workflows/build/badge.svg)](https://github.com/tuyenhavan/pymapee/actions?query=workflow%3Abuild)
+        [![image](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
         
         
-        **A Simple Python package to pre-processing satellite data using Google Earth Engine.**
+        **A Simple Python package to pre-processing satellite-based data using Google Earth Engine.**
         
         `pymapee` is a simple Python package that aims to provide common functionalities to pre-process or calculate vegetation drought indices using Google Earth Engine. Currently, this package supports cloud masking (MODIS, Landsat, Sentinel-2), composite (monthly), and calculation of vegetation anomaly index (VAI) and vegetation condition index (VCI). It also supports to download an image collection (e.g., time-series NDVI or LST) or an image. This package is under active development, and changes are expected over time.
         
         -  GitHub repo: [https://github.com/tuyenhavan/pymapee](https://github.com/tuyenhavan/pymapee)
         -   Free software: MIT license
         ---
         ## Features
@@ -31,23 +32,24 @@
         -   Downloading an image or image collection (e.g., time-series NDVI)
         ---
         ## Installation
         Install `pymapee` using pip 
         
         `pip install pymapee`
         
-        or install from Github
+        or install from Github to get the latest update.
         
         `pip install git+https://github.com/tuyenhavan/pymapee.git`
         
         ---
         ## Credits
         
         This package was created with [Cookiecutter](https://github.com/cookiecutter/cookiecutter) and the [giswqs/pypackage](https://github.com/giswqs/pypackage) project template.
         
+        
 Keywords: pymapee
 Platform: UNKNOWN
 Classifier: Development Status :: 2 - Pre-Alpha
 Classifier: Intended Audience :: Developers
 Classifier: License :: OSI Approved :: MIT License
 Classifier: Natural Language :: English
 Classifier: Programming Language :: Python :: 3
```

### Comparing `pymapee-0.0.2/README.md` & `pymapee-0.0.3/README.md`

 * *Files 16% similar despite different names*

```diff
@@ -1,17 +1,18 @@
-# pymapee
-
+# Welcome to pymapee
 
 [![image](https://img.shields.io/pypi/v/pymapee.svg)](https://pypi.python.org/pypi/pymapee)
 [![image](https://img.shields.io/conda/vn/conda-forge/pymapee.svg)](https://anaconda.org/conda-forge/pymapee)
-
-[![image](https://pyup.io/repos/github/tuyenhavan/pymapee/shield.svg)](https://pyup.io/repos/github/tuyenhavan/pymapee)
+[![image](https://pepy.tech/badge/pymapee)](https://pepy.tech/project/pymapee)
+[![image](https://github.com/tuyenhavan/pymapee/workflows/docs/badge.svg)](https://pymapee.org)
+[![image](https://github.com/tuyenhavan/pymapee/workflows/build/badge.svg)](https://github.com/tuyenhavan/pymapee/actions?query=workflow%3Abuild)
+[![image](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
 
 
-**A Simple Python package to pre-processing satellite data using Google Earth Engine.**
+**A Simple Python package to pre-processing satellite-based data using Google Earth Engine.**
 
 `pymapee` is a simple Python package that aims to provide common functionalities to pre-process or calculate vegetation drought indices using Google Earth Engine. Currently, this package supports cloud masking (MODIS, Landsat, Sentinel-2), composite (monthly), and calculation of vegetation anomaly index (VAI) and vegetation condition index (VCI). It also supports to download an image collection (e.g., time-series NDVI or LST) or an image. This package is under active development, and changes are expected over time.
 
 -  GitHub repo: [https://github.com/tuyenhavan/pymapee](https://github.com/tuyenhavan/pymapee)
 -   Free software: MIT license
 ---
 ## Features
@@ -23,15 +24,16 @@
 -   Downloading an image or image collection (e.g., time-series NDVI)
 ---
 ## Installation
 Install `pymapee` using pip 
 
 `pip install pymapee`
 
-or install from Github
+or install from Github to get the latest update.
 
 `pip install git+https://github.com/tuyenhavan/pymapee.git`
 
 ---
 ## Credits
 
 This package was created with [Cookiecutter](https://github.com/cookiecutter/cookiecutter) and the [giswqs/pypackage](https://github.com/giswqs/pypackage) project template.
+
```

### Comparing `pymapee-0.0.2/docs/contributing.md` & `pymapee-0.0.3/docs/contributing.md`

 * *Files identical despite different names*

### Comparing `pymapee-0.0.2/docs/index.md` & `pymapee-0.0.3/docs/index.md`

 * *Files identical despite different names*

### Comparing `pymapee-0.0.2/docs/installation.md` & `pymapee-0.0.3/docs/installation.md`

 * *Files identical despite different names*

### Comparing `pymapee-0.0.2/examples/Notebook 01. Cloud masking and vegetation indices.ipynb` & `pymapee-0.0.3/examples/Notebook 01. Cloud masking and vegetation indices.ipynb`

 * *Files identical despite different names*

### Comparing `pymapee-0.0.2/mkdocs.yml` & `pymapee-0.0.3/mkdocs.yml`

 * *Files identical despite different names*

### Comparing `pymapee-0.0.2/pymapee/pymapee.py` & `pymapee-0.0.3/pymapee/pymapee.py`

 * *Files 18% similar despite different names*

```diff
@@ -1,11 +1,11 @@
 """Main module."""
 import ee
 from .utils import (date_range_col, monthly_datetime_list,
-                    cloud_mask, scaling_data)
+                    cloud_mask, scaling_data, data_format)
 
 def initialize_ee():
     ee.Initialize()
 
 def authenticate_ee():
     ee.Authenticate()
 
@@ -163,14 +163,75 @@
         max_value=col_month.max()
         vci_img=subcol.max().subtract(min_value).divide(max_value.subtract(min_value)).multiply(100)
         vci_img=vci_img.set({"system:time_start":start_time.millis()}).rename("VCI")
         return ee.Algorithms.If(size.gt(0), vci_img)
     vci_col=ee.ImageCollection.fromImages(monthly_list.map(vci))
     return vci_col
 
+def col_resample(col, resample_method=None, scale=None, crs=None):
+    """ Return a collection of resampled images. Resampling methods include max, min,
+        bilinear, bicubic, average, mode, and median.
+
+        Args:
+            col (ee.ImageCollection|ee.Image): The input image collection.
+            resample_method (str|optional): The resampling method. Default to bilinear.
+            crs (str|optional): The coordinate referenced system (reprojection) EPSG code. Default to None.
+            scale (int|float|optional): The spatial resolution in meters. Default to None.
+
+        Returns:
+            ee.ImageCollection: The output of resampled collection.
+    """
+    if resample_method is None:
+        resample_method="bilinear"
+    if crs is None:
+        if isinstance(col, ee.Image):
+            crs=col.select(0).projection().getInfo()["crs"]
+        elif isinstance(col, ee.ImageCollection):
+            crs=col.first().select(0).projection().getInfo()["crs"]
+    if scale is None:
+        scale =1000
+    if not (isinstance(resample_method, str) and isinstance(crs, str) and isinstance(scale, (int, float))):
+        raise TypeError ("Unsupported data type!")
+    if isinstance(col, ee.Image):
+        data=ee.Image(col).resample(resample_method).reproject(crs=crs, scale=scale)
+    if isinstance(col, ee.ImageCollection):
+        data=col.map(lambda img: img.resample(resample_method).reproject(crs=crs, scale=scale))
+    else:
+        raise TypeError("Unsupported data type!")
+    return data
+
+def value_from_image(img, polygon, method=None, scale=None, keep_geometry=False):
+    """ Extract values from an multi-band image using polygon (e.g., point, polygon).
+
+        Args:
+            img (ee.Image): The image that is used to extract values from.
+            polygon (ee.FeatureCollection): The shapefile feature collection.
+            method (str|optional): The method for extracting values using shapefile feature. Default to None.
+            scale (int|float|optional): The scale value in meters.
+            keep_geometry (bol|optional): If True, then keep the coordinate values. Default to False.
+
+        Returns:
+            pandas.DataFrame: The extracted dataframe.
+    """
+    if not isinstance(img, ee.Image):
+        raise TypeError("Unsupported data type!")
+    if not isinstance(polygon, ee.FeatureCollection):
+        raise TypeError("Unsupported data type!")
+    if method is None:
+        method="median"
+    if scale is None:
+        scale =1000
+    if not (isinstance(method, str) and isinstance(scale, (int, float))):
+        raise TypeError("Unsupported data type!")
+    value=img.reduceRegions(collection=polygon, reducer=method, scale=scale)
+    dict_value=value.select(trend_band.bandNames().getInfo(), retainGeometry=keep_geometry).getInfo()
+    df=data_format(dict_value)
+    return df
+
+
 def download_ee(ds,aoi,folder_name="GEE_Data",res=1000):
     """ Export an image from GEE with a given scale and area of interest
     to the Google Drive. If input data is an ImageCollection, it will convert it
     into an image and then export. The collection should contains only single data,
     for example NDVI bands or precipitation bands or LST bands.
 
         Args:
```

### Comparing `pymapee-0.0.2/pymapee/utils.py` & `pymapee-0.0.3/pymapee/utils.py`

 * *Files 21% similar despite different names*

```diff
@@ -100,14 +100,28 @@
     monthly_list=month_list.map(month_step)
     return monthly_list
 
 ##############################################################################
 #                                 Other Untilities                           #
 ##############################################################################
 
+def is_package_install(pkg_name):
+    """ Return True if the package is installed and False otherwise."""
+    try:
+        __import__(pkg_name)
+        return True
+    except:
+        return False
+
+def package_install(pkg_name):
+    """ Install the package."""
+    import subprocess
+    if isinstance(pkg_name, str):
+        pkg_name=pkg_name.strip()
+    subprocess.check_call(["python","-m", "pip","install", pkg_name])
 
 def scaling_data(col, scale_factor=None):
     """ Scale value of an image or collection
 
         Args:
             col (ee.ImageCollection|ee.Image): The input image or collection.
             scale_factor (int|float|optional): The scale given by scale information in image band. Default to None.
@@ -135,14 +149,31 @@
     """
     if isinstance(col, ee.Image):
         out_data=ee.Image(col.subtract(273.15).copyProperties(col, col.propertyNames()))
     if isinstance (col, ee.ImageCollection):
         out_data=col.map(lambda img: img.subtract(273.15).copyProperties(img, img.propertyNames()))
     return out_data
 
+def data_format(input_data):
+    """ Format data returned by reduceRegions"""
+    if not is_package_install("pandas"):
+        package_install("pandas")
+    try:
+        import pandas as pd
+    except:
+        print("Please install pandas. Here is the link https://pandas.pydata.org/docs/getting_started/install.html")
+
+    data=input_data["features"]
+    slist=[]
+    for i in data:
+        thuoctinh=i["properties"]
+        slist.append(thuoctinh)
+    df=pd.DataFrame(slist)
+    return df
+
 def col_timestamp_band(col):
     """ return a collection with a new band added called timestamp"""
     def time_band(img):
         _time_band=img.metadata("system:time_start").rename("timestamp")
         time_band_mask=_time_band.updateMask(img.mask().select(0))
         return img.addBands(time_band_mask)
     return col.map(time_band)
```

### Comparing `pymapee-0.0.2/pymapee.egg-info/PKG-INFO` & `pymapee-0.0.3/pymapee.egg-info/PKG-INFO`

 * *Files 21% similar despite different names*

```diff
@@ -1,25 +1,26 @@
 Metadata-Version: 2.1
 Name: pymapee
-Version: 0.0.2
+Version: 0.0.3
 Summary: A Simple Python package to pre-processing satellite data using Google Earth Engine.
 Home-page: https://github.com/tuyenhavan/pymapee
 Author: Tuyen Ha
 Author-email: tuyenmassey@gmail.com
 License: MIT license
-Description: # pymapee
-        
+Description: # Welcome to pymapee
         
         [![image](https://img.shields.io/pypi/v/pymapee.svg)](https://pypi.python.org/pypi/pymapee)
         [![image](https://img.shields.io/conda/vn/conda-forge/pymapee.svg)](https://anaconda.org/conda-forge/pymapee)
-        
-        [![image](https://pyup.io/repos/github/tuyenhavan/pymapee/shield.svg)](https://pyup.io/repos/github/tuyenhavan/pymapee)
+        [![image](https://pepy.tech/badge/pymapee)](https://pepy.tech/project/pymapee)
+        [![image](https://github.com/tuyenhavan/pymapee/workflows/docs/badge.svg)](https://pymapee.org)
+        [![image](https://github.com/tuyenhavan/pymapee/workflows/build/badge.svg)](https://github.com/tuyenhavan/pymapee/actions?query=workflow%3Abuild)
+        [![image](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
         
         
-        **A Simple Python package to pre-processing satellite data using Google Earth Engine.**
+        **A Simple Python package to pre-processing satellite-based data using Google Earth Engine.**
         
         `pymapee` is a simple Python package that aims to provide common functionalities to pre-process or calculate vegetation drought indices using Google Earth Engine. Currently, this package supports cloud masking (MODIS, Landsat, Sentinel-2), composite (monthly), and calculation of vegetation anomaly index (VAI) and vegetation condition index (VCI). It also supports to download an image collection (e.g., time-series NDVI or LST) or an image. This package is under active development, and changes are expected over time.
         
         -  GitHub repo: [https://github.com/tuyenhavan/pymapee](https://github.com/tuyenhavan/pymapee)
         -   Free software: MIT license
         ---
         ## Features
@@ -31,23 +32,24 @@
         -   Downloading an image or image collection (e.g., time-series NDVI)
         ---
         ## Installation
         Install `pymapee` using pip 
         
         `pip install pymapee`
         
-        or install from Github
+        or install from Github to get the latest update.
         
         `pip install git+https://github.com/tuyenhavan/pymapee.git`
         
         ---
         ## Credits
         
         This package was created with [Cookiecutter](https://github.com/cookiecutter/cookiecutter) and the [giswqs/pypackage](https://github.com/giswqs/pypackage) project template.
         
+        
 Keywords: pymapee
 Platform: UNKNOWN
 Classifier: Development Status :: 2 - Pre-Alpha
 Classifier: Intended Audience :: Developers
 Classifier: License :: OSI Approved :: MIT License
 Classifier: Natural Language :: English
 Classifier: Programming Language :: Python :: 3
```

### Comparing `pymapee-0.0.2/pymapee.egg-info/SOURCES.txt` & `pymapee-0.0.3/pymapee.egg-info/SOURCES.txt`

 * *Files 12% similar despite different names*

```diff
@@ -28,10 +28,11 @@
 pymapee/__init__.py
 pymapee/pymapee.py
 pymapee/utils.py
 pymapee.egg-info/PKG-INFO
 pymapee.egg-info/SOURCES.txt
 pymapee.egg-info/dependency_links.txt
 pymapee.egg-info/not-zip-safe
+pymapee.egg-info/requires.txt
 pymapee.egg-info/top_level.txt
 tests/__init__.py
 tests/test_pymapee.py
```

### Comparing `pymapee-0.0.2/setup.py` & `pymapee-0.0.3/setup.py`

 * *Files 5% similar despite different names*

```diff
@@ -49,10 +49,10 @@
     keywords='pymapee',
     name='pymapee',
     packages=find_packages(include=['pymapee', 'pymapee.*']),
     setup_requires=setup_requirements,
     test_suite='tests',
     tests_require=test_requirements,
     url='https://github.com/tuyenhavan/pymapee',
-    version='0.0.2',
+    version='0.0.3',
     zip_safe=False,
 )
```

### Comparing `pymapee-0.0.2/tests/test_pymapee.py` & `pymapee-0.0.3/tests/test_pymapee.py`

 * *Files identical despite different names*

