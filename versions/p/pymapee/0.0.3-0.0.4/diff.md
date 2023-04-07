# Comparing `tmp/pymapee-0.0.3.tar.gz` & `tmp/pymapee-0.0.4.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "pymapee-0.0.3.tar", last modified: Fri Apr  7 10:12:17 2023, max compression
+gzip compressed data, was "pymapee-0.0.4.tar", last modified: Fri Apr  7 14:42:29 2023, max compression
```

## Comparing `pymapee-0.0.3.tar` & `pymapee-0.0.4.tar`

### file list

```diff
@@ -1,49 +1,49 @@
-drwxrwxrwx   0        0        0        0 2023-04-07 10:12:17.073967 pymapee-0.0.3/
--rw-rw-rw-   0        0        0      313 2023-04-01 08:23:17.000000 pymapee-0.0.3/.editorconfig
-drwxrwxrwx   0        0        0        0 2023-04-07 10:12:16.554181 pymapee-0.0.3/.github/
-drwxrwxrwx   0        0        0        0 2023-04-07 10:12:16.697521 pymapee-0.0.3/.github/ISSUE_TEMPLATE/
--rw-rw-rw-   0        0        0      532 2023-04-01 08:23:17.000000 pymapee-0.0.3/.github/ISSUE_TEMPLATE/bug_report.md
--rw-rw-rw-   0        0        0      510 2023-04-01 08:23:17.000000 pymapee-0.0.3/.github/ISSUE_TEMPLATE/config.yml
--rw-rw-rw-   0        0        0      459 2023-04-01 08:23:17.000000 pymapee-0.0.3/.github/ISSUE_TEMPLATE/feature_request.md
-drwxrwxrwx   0        0        0        0 2023-04-07 10:12:16.809593 pymapee-0.0.3/.github/workflows/
--rw-rw-rw-   0        0        0     1439 2023-04-01 08:23:17.000000 pymapee-0.0.3/.github/workflows/build.yml
--rw-rw-rw-   0        0        0      872 2023-04-01 08:23:17.000000 pymapee-0.0.3/.github/workflows/docs.yml
--rw-rw-rw-   0        0        0     1032 2023-04-01 08:23:17.000000 pymapee-0.0.3/.github/workflows/pypi.yml
--rw-rw-rw-   0        0        0     1345 2023-04-03 20:02:52.000000 pymapee-0.0.3/.gitignore
--rw-rw-rw-   0        0        0      168 2023-04-01 08:23:17.000000 pymapee-0.0.3/AUTHORS.rst
--rw-rw-rw-   0        0        0     1089 2023-04-01 08:23:17.000000 pymapee-0.0.3/LICENSE
--rw-rw-rw-   0        0        0      129 2023-04-01 08:23:17.000000 pymapee-0.0.3/MANIFEST.in
--rw-rw-rw-   0        0        0     3248 2023-04-07 10:12:17.074997 pymapee-0.0.3/PKG-INFO
--rw-rw-rw-   0        0        0     2102 2023-04-07 09:30:29.000000 pymapee-0.0.3/README.md
-drwxrwxrwx   0        0        0        0 2023-04-07 10:12:16.976147 pymapee-0.0.3/docs/
--rw-rw-rw-   0        0        0       29 2023-04-01 08:23:17.000000 pymapee-0.0.3/docs/authors.rst
--rw-rw-rw-   0        0        0       96 2023-04-01 08:23:17.000000 pymapee-0.0.3/docs/changelog.md
--rw-rw-rw-   0        0        0     3242 2023-04-01 08:23:17.000000 pymapee-0.0.3/docs/contributing.md
--rw-rw-rw-   0        0        0        7 2023-04-01 08:23:17.000000 pymapee-0.0.3/docs/faq.md
--rw-rw-rw-   0        0        0      653 2023-04-01 08:23:17.000000 pymapee-0.0.3/docs/index.md
--rw-rw-rw-   0        0        0      613 2023-04-01 08:23:17.000000 pymapee-0.0.3/docs/installation.md
-drwxrwxrwx   0        0        0        0 2023-04-07 10:12:16.988955 pymapee-0.0.3/docs/overrides/
--rw-rw-rw-   0        0        0      285 2023-04-01 08:23:17.000000 pymapee-0.0.3/docs/overrides/main.html
--rw-rw-rw-   0        0        0       42 2023-04-01 08:23:17.000000 pymapee-0.0.3/docs/pymapee.md
--rw-rw-rw-   0        0        0       69 2023-04-01 08:23:17.000000 pymapee-0.0.3/docs/usage.md
-drwxrwxrwx   0        0        0        0 2023-04-07 10:12:17.019386 pymapee-0.0.3/examples/
--rw-rw-rw-   0        0        0    15528 2023-04-03 17:59:09.000000 pymapee-0.0.3/examples/Notebook 01. Cloud masking and vegetation indices.ipynb
--rw-rw-rw-   0        0        0     1211 2023-04-01 08:23:17.000000 pymapee-0.0.3/mkdocs.yml
-drwxrwxrwx   0        0        0        0 2023-04-07 10:12:17.028392 pymapee-0.0.3/pymapee/
--rw-rw-rw-   0        0        0      189 2023-04-07 10:03:26.000000 pymapee-0.0.3/pymapee/__init__.py
--rw-rw-rw-   0        0        0    12099 2023-04-04 21:05:55.000000 pymapee-0.0.3/pymapee/pymapee.py
--rw-rw-rw-   0        0        0     6880 2023-04-04 21:05:15.000000 pymapee-0.0.3/pymapee/utils.py
-drwxrwxrwx   0        0        0        0 2023-04-07 10:12:17.068715 pymapee-0.0.3/pymapee.egg-info/
--rw-rw-rw-   0        0        0     3248 2023-04-07 10:12:16.000000 pymapee-0.0.3/pymapee.egg-info/PKG-INFO
--rw-rw-rw-   0        0        0      832 2023-04-07 10:12:16.000000 pymapee-0.0.3/pymapee.egg-info/SOURCES.txt
--rw-rw-rw-   0        0        0       27 2023-04-07 10:12:16.000000 pymapee-0.0.3/pymapee.egg-info/dependency_links.txt
--rw-rw-rw-   0        0        0        2 2023-04-02 19:42:09.000000 pymapee-0.0.3/pymapee.egg-info/not-zip-safe
--rw-rw-rw-   0        0        0       25 2023-04-07 10:12:16.000000 pymapee-0.0.3/pymapee.egg-info/requires.txt
--rw-rw-rw-   0        0        0        8 2023-04-07 10:12:16.000000 pymapee-0.0.3/pymapee.egg-info/top_level.txt
--rw-rw-rw-   0        0        0       26 2023-04-07 10:12:06.000000 pymapee-0.0.3/requirements.txt
--rw-rw-rw-   0        0        0      103 2023-04-01 08:23:17.000000 pymapee-0.0.3/requirements_dev.txt
--rw-rw-rw-   0        0        0      478 2023-04-07 10:12:17.076965 pymapee-0.0.3/setup.cfg
--rw-rw-rw-   0        0        0     1867 2023-04-07 10:03:31.000000 pymapee-0.0.3/setup.py
-drwxrwxrwx   0        0        0        0 2023-04-07 10:12:17.072958 pymapee-0.0.3/tests/
--rw-rw-rw-   0        0        0       38 2023-04-01 08:23:17.000000 pymapee-0.0.3/tests/__init__.py
--rw-rw-rw-   0        0        0      577 2023-04-01 08:23:17.000000 pymapee-0.0.3/tests/test_pymapee.py
+drwxrwxrwx   0        0        0        0 2023-04-07 14:42:29.534594 pymapee-0.0.4/
+-rw-rw-rw-   0        0        0      313 2023-04-01 08:23:17.000000 pymapee-0.0.4/.editorconfig
+drwxrwxrwx   0        0        0        0 2023-04-07 14:42:29.455717 pymapee-0.0.4/.github/
+drwxrwxrwx   0        0        0        0 2023-04-07 14:42:29.480949 pymapee-0.0.4/.github/ISSUE_TEMPLATE/
+-rw-rw-rw-   0        0        0      532 2023-04-01 08:23:17.000000 pymapee-0.0.4/.github/ISSUE_TEMPLATE/bug_report.md
+-rw-rw-rw-   0        0        0      510 2023-04-01 08:23:17.000000 pymapee-0.0.4/.github/ISSUE_TEMPLATE/config.yml
+-rw-rw-rw-   0        0        0      459 2023-04-01 08:23:17.000000 pymapee-0.0.4/.github/ISSUE_TEMPLATE/feature_request.md
+drwxrwxrwx   0        0        0        0 2023-04-07 14:42:29.485979 pymapee-0.0.4/.github/workflows/
+-rw-rw-rw-   0        0        0     1439 2023-04-01 08:23:17.000000 pymapee-0.0.4/.github/workflows/build.yml
+-rw-rw-rw-   0        0        0      872 2023-04-01 08:23:17.000000 pymapee-0.0.4/.github/workflows/docs.yml
+-rw-rw-rw-   0        0        0     1032 2023-04-01 08:23:17.000000 pymapee-0.0.4/.github/workflows/pypi.yml
+-rw-rw-rw-   0        0        0     1345 2023-04-03 20:02:52.000000 pymapee-0.0.4/.gitignore
+-rw-rw-rw-   0        0        0      168 2023-04-01 08:23:17.000000 pymapee-0.0.4/AUTHORS.rst
+-rw-rw-rw-   0        0        0     1089 2023-04-01 08:23:17.000000 pymapee-0.0.4/LICENSE
+-rw-rw-rw-   0        0        0      129 2023-04-01 08:23:17.000000 pymapee-0.0.4/MANIFEST.in
+-rw-rw-rw-   0        0        0     3399 2023-04-07 14:42:29.534594 pymapee-0.0.4/PKG-INFO
+-rw-rw-rw-   0        0        0     2229 2023-04-07 11:55:25.000000 pymapee-0.0.4/README.md
+drwxrwxrwx   0        0        0        0 2023-04-07 14:42:29.496107 pymapee-0.0.4/docs/
+-rw-rw-rw-   0        0        0       29 2023-04-01 08:23:17.000000 pymapee-0.0.4/docs/authors.rst
+-rw-rw-rw-   0        0        0       96 2023-04-01 08:23:17.000000 pymapee-0.0.4/docs/changelog.md
+-rw-rw-rw-   0        0        0     3242 2023-04-01 08:23:17.000000 pymapee-0.0.4/docs/contributing.md
+-rw-rw-rw-   0        0        0        7 2023-04-01 08:23:17.000000 pymapee-0.0.4/docs/faq.md
+-rw-rw-rw-   0        0        0      653 2023-04-01 08:23:17.000000 pymapee-0.0.4/docs/index.md
+-rw-rw-rw-   0        0        0      613 2023-04-01 08:23:17.000000 pymapee-0.0.4/docs/installation.md
+drwxrwxrwx   0        0        0        0 2023-04-07 14:42:29.497109 pymapee-0.0.4/docs/overrides/
+-rw-rw-rw-   0        0        0      285 2023-04-01 08:23:17.000000 pymapee-0.0.4/docs/overrides/main.html
+-rw-rw-rw-   0        0        0       42 2023-04-01 08:23:17.000000 pymapee-0.0.4/docs/pymapee.md
+-rw-rw-rw-   0        0        0       69 2023-04-01 08:23:17.000000 pymapee-0.0.4/docs/usage.md
+drwxrwxrwx   0        0        0        0 2023-04-07 14:42:29.498107 pymapee-0.0.4/examples/
+-rw-rw-rw-   0        0        0    14840 2023-04-07 14:17:05.000000 pymapee-0.0.4/examples/Notebook 01. Cloud masking and vegetation indices.ipynb
+-rw-rw-rw-   0        0        0     1211 2023-04-01 08:23:17.000000 pymapee-0.0.4/mkdocs.yml
+drwxrwxrwx   0        0        0        0 2023-04-07 14:42:29.502659 pymapee-0.0.4/pymapee/
+-rw-rw-rw-   0        0        0      189 2023-04-07 14:41:51.000000 pymapee-0.0.4/pymapee/__init__.py
+-rw-rw-rw-   0        0        0    13283 2023-04-07 14:36:06.000000 pymapee-0.0.4/pymapee/pymapee.py
+-rw-rw-rw-   0        0        0     8460 2023-04-07 14:33:48.000000 pymapee-0.0.4/pymapee/utils.py
+drwxrwxrwx   0        0        0        0 2023-04-07 14:42:29.529603 pymapee-0.0.4/pymapee.egg-info/
+-rw-rw-rw-   0        0        0     3399 2023-04-07 14:42:29.000000 pymapee-0.0.4/pymapee.egg-info/PKG-INFO
+-rw-rw-rw-   0        0        0      832 2023-04-07 14:42:29.000000 pymapee-0.0.4/pymapee.egg-info/SOURCES.txt
+-rw-rw-rw-   0        0        0       27 2023-04-07 14:42:29.000000 pymapee-0.0.4/pymapee.egg-info/dependency_links.txt
+-rw-rw-rw-   0        0        0        2 2023-04-02 19:42:09.000000 pymapee-0.0.4/pymapee.egg-info/not-zip-safe
+-rw-rw-rw-   0        0        0       25 2023-04-07 14:42:29.000000 pymapee-0.0.4/pymapee.egg-info/requires.txt
+-rw-rw-rw-   0        0        0        8 2023-04-07 14:42:29.000000 pymapee-0.0.4/pymapee.egg-info/top_level.txt
+-rw-rw-rw-   0        0        0       26 2023-04-07 10:12:06.000000 pymapee-0.0.4/requirements.txt
+-rw-rw-rw-   0        0        0      103 2023-04-01 08:23:17.000000 pymapee-0.0.4/requirements_dev.txt
+-rw-rw-rw-   0        0        0      478 2023-04-07 14:42:29.537489 pymapee-0.0.4/setup.cfg
+-rw-rw-rw-   0        0        0     1867 2023-04-07 14:41:58.000000 pymapee-0.0.4/setup.py
+drwxrwxrwx   0        0        0        0 2023-04-07 14:42:29.532599 pymapee-0.0.4/tests/
+-rw-rw-rw-   0        0        0       38 2023-04-01 08:23:17.000000 pymapee-0.0.4/tests/__init__.py
+-rw-rw-rw-   0        0        0      577 2023-04-01 08:23:17.000000 pymapee-0.0.4/tests/test_pymapee.py
```

### Comparing `pymapee-0.0.3/.github/ISSUE_TEMPLATE/bug_report.md` & `pymapee-0.0.4/.github/ISSUE_TEMPLATE/bug_report.md`

 * *Files identical despite different names*

### Comparing `pymapee-0.0.3/.github/workflows/build.yml` & `pymapee-0.0.4/.github/workflows/build.yml`

 * *Files identical despite different names*

### Comparing `pymapee-0.0.3/.github/workflows/docs.yml` & `pymapee-0.0.4/.github/workflows/docs.yml`

 * *Files identical despite different names*

### Comparing `pymapee-0.0.3/.github/workflows/pypi.yml` & `pymapee-0.0.4/.github/workflows/pypi.yml`

 * *Files identical despite different names*

### Comparing `pymapee-0.0.3/.gitignore` & `pymapee-0.0.4/.gitignore`

 * *Files identical despite different names*

### Comparing `pymapee-0.0.3/LICENSE` & `pymapee-0.0.4/LICENSE`

 * *Files identical despite different names*

### Comparing `pymapee-0.0.3/PKG-INFO` & `pymapee-0.0.4/PKG-INFO`

 * *Files 6% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: pymapee
-Version: 0.0.3
+Version: 0.0.4
 Summary: A Simple Python package to pre-processing satellite data using Google Earth Engine.
 Home-page: https://github.com/tuyenhavan/pymapee
 Author: Tuyen Ha
 Author-email: tuyenmassey@gmail.com
 License: MIT license
 Description: # Welcome to pymapee
         
@@ -26,14 +26,17 @@
         ## Features
         
         -   Masking cloud-related pixels (e.g., MODIS, Landsat, and Sentinel-2)
         -   Making monthly composite
         -   Calculating monthly vegetation anomaly index (VAI) and vegetation condition index (VCI).
         -   Scaling data
         -   Downloading an image or image collection (e.g., time-series NDVI)
+        
+        Examples are provided [here](https://github.com/tuyenhavan/pymapee/tree/main/examples), and it will be regularly updated.
+        
         ---
         ## Installation
         Install `pymapee` using pip 
         
         `pip install pymapee`
         
         or install from Github to get the latest update.
```

### Comparing `pymapee-0.0.3/README.md` & `pymapee-0.0.4/README.md`

 * *Files 4% similar despite different names*

```diff
@@ -18,14 +18,17 @@
 ## Features
 
 -   Masking cloud-related pixels (e.g., MODIS, Landsat, and Sentinel-2)
 -   Making monthly composite
 -   Calculating monthly vegetation anomaly index (VAI) and vegetation condition index (VCI).
 -   Scaling data
 -   Downloading an image or image collection (e.g., time-series NDVI)
+
+Examples are provided [here](https://github.com/tuyenhavan/pymapee/tree/main/examples), and it will be regularly updated.
+
 ---
 ## Installation
 Install `pymapee` using pip 
 
 `pip install pymapee`
 
 or install from Github to get the latest update.
```

### Comparing `pymapee-0.0.3/docs/contributing.md` & `pymapee-0.0.4/docs/contributing.md`

 * *Files identical despite different names*

### Comparing `pymapee-0.0.3/docs/index.md` & `pymapee-0.0.4/docs/index.md`

 * *Files identical despite different names*

### Comparing `pymapee-0.0.3/docs/installation.md` & `pymapee-0.0.4/docs/installation.md`

 * *Files identical despite different names*

### Comparing `pymapee-0.0.3/mkdocs.yml` & `pymapee-0.0.4/mkdocs.yml`

 * *Files identical despite different names*

### Comparing `pymapee-0.0.3/pymapee/pymapee.py` & `pymapee-0.0.4/pymapee/pymapee.py`

 * *Files 4% similar despite different names*

```diff
@@ -1,17 +1,40 @@
 """Main module."""
 import ee
 from .utils import (date_range_col, monthly_datetime_list,
-                    cloud_mask, scaling_data, data_format)
+                    cloud_mask, scaling_data, data_format,
+                    gee_service_account, non_service_account)
 
-def initialize_ee():
-    ee.Initialize()
-
-def authenticate_ee():
-    ee.Authenticate()
+def initialize_ee(token_name="EARTHENGINE_TOKEN", autho_mode="notebook", service_account=False):
+    """ Authenticate and initialize the Google Earth Engine (GEE).
+    
+        Args:
+            token_name (str|optional): The token name of GEE. Defaults to EARTHENGINE_TOKEN.
+            autho_mode (str|optional): The authentication mode. Defaults to notebook.
+            service_account (bool, optional): If True, use GEE service account and False otherwise. Defaults to False.
+        
+        Credit: This function is mainly taken from https://github.com/gee-community/geemap
+    """
+    import httplib2
+    import os
+    if ee.data._credentials is None:
+        ee_token=os.environ.get(token_name)
+        if service_account:
+            try:
+                gee_service_account()
+            except:
+                print("Failed to initialize Google Earth Engine.")
+        else:
+            try:
+                if ee_token is not None:
+                    non_service_account()
+                ee.Initialize(http_transport=httplib2.Http())
+            except:
+                ee.Authenticate(auth_mode=autho_mode)
+                ee.Initialize(http_transport=httplib2.Http())
 
 def modis_cloud_mask(col, from_bit, to_bit, QA_band="DetailedQA", threshold=1):
     """ Return a collection of MODIS cloud-free images
 
         Args:
             col (ee.ImageCollection): The input image collection.
             from_bit (int): The start bit to extract.
```

### Comparing `pymapee-0.0.3/pymapee/utils.py` & `pymapee-0.0.4/pymapee/utils.py`

 * *Files 17% similar despite different names*

```diff
@@ -1,10 +1,12 @@
 """ A helper module to support pymapee module"""
 import datetime
 import ee
+import os
+import json
 
 ##############################################################################
 #                                 Cloud Mask                                 #
 ##############################################################################
 
 def bitwise_extract(img, from_bit, to_bit):
     """ Extract cloud-related bits
@@ -97,14 +99,47 @@
         first_month=ee.Date.fromYMD(y,m,1)
         next_month=first_month.advance(month,"month")
         return next_month.millis()
     monthly_list=month_list.map(month_step)
     return monthly_list
 
 ##############################################################################
+#                         Initialization and Authentication                  #
+##############################################################################
+
+def gee_service_account():
+    credential_file=os.path.expanduser("~/.config/earthengine/private-key.json")
+    if os.path.exists(credential_file):
+        with open(credential_file) as file:
+            token_dict=json.load(file)
+    else:
+        token_name = "EARTHENGINE_TOKEN"
+        ee_token = os.environ.get(token_name)
+        if ee_token:
+            token_dict = json.loads(ee_token, strict=False)
+            service_account = token_dict["client_email"]
+            private_key = token_dict["private_key"]
+            credentials = ee.ServiceAccountCredentials(service_account, key_data=private_key)
+            ee.Initialize(credentials)
+
+def non_service_account():
+    credential_file=os.path.expanduser("~/.config/earthengine/credentials")
+    if not os.path.exists(credential_file):
+        folder=os.path.dirname(credential_file)
+        os.makedirs(folder, exist_okay=True)
+        if ee_token.startswith("{") and ee_token.endswith(""):
+            token_dict=json.loads(ee_token)
+            with open(credential_file,"w") as new_file:
+                new_file.write(json.dumps(token_dict))
+        else:
+            credential=('{"refresh_token":"%s"}' % ee_token)
+            with open(credential_file,"w") as new_file:
+                new_file.write(credential)
+
+##############################################################################
 #                                 Other Untilities                           #
 ##############################################################################
 
 def is_package_install(pkg_name):
     """ Return True if the package is installed and False otherwise."""
     try:
         __import__(pkg_name)
```

### Comparing `pymapee-0.0.3/pymapee.egg-info/PKG-INFO` & `pymapee-0.0.4/pymapee.egg-info/PKG-INFO`

 * *Files 6% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: pymapee
-Version: 0.0.3
+Version: 0.0.4
 Summary: A Simple Python package to pre-processing satellite data using Google Earth Engine.
 Home-page: https://github.com/tuyenhavan/pymapee
 Author: Tuyen Ha
 Author-email: tuyenmassey@gmail.com
 License: MIT license
 Description: # Welcome to pymapee
         
@@ -26,14 +26,17 @@
         ## Features
         
         -   Masking cloud-related pixels (e.g., MODIS, Landsat, and Sentinel-2)
         -   Making monthly composite
         -   Calculating monthly vegetation anomaly index (VAI) and vegetation condition index (VCI).
         -   Scaling data
         -   Downloading an image or image collection (e.g., time-series NDVI)
+        
+        Examples are provided [here](https://github.com/tuyenhavan/pymapee/tree/main/examples), and it will be regularly updated.
+        
         ---
         ## Installation
         Install `pymapee` using pip 
         
         `pip install pymapee`
         
         or install from Github to get the latest update.
```

### Comparing `pymapee-0.0.3/pymapee.egg-info/SOURCES.txt` & `pymapee-0.0.4/pymapee.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `pymapee-0.0.3/setup.py` & `pymapee-0.0.4/setup.py`

 * *Files 6% similar despite different names*

```diff
@@ -49,10 +49,10 @@
     keywords='pymapee',
     name='pymapee',
     packages=find_packages(include=['pymapee', 'pymapee.*']),
     setup_requires=setup_requirements,
     test_suite='tests',
     tests_require=test_requirements,
     url='https://github.com/tuyenhavan/pymapee',
-    version='0.0.3',
+    version='0.0.4',
     zip_safe=False,
 )
```

### Comparing `pymapee-0.0.3/tests/test_pymapee.py` & `pymapee-0.0.4/tests/test_pymapee.py`

 * *Files identical despite different names*

