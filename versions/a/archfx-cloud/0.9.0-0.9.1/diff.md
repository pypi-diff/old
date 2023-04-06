# Comparing `tmp/archfx_cloud-0.9.0.tar.gz` & `tmp/archfx_cloud-0.9.1.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "dist/archfx_cloud-0.9.0.tar", last modified: Sat Apr  3 23:48:30 2021, max compression
+gzip compressed data, was "archfx_cloud-0.9.1.tar", last modified: Sun Apr  4 00:59:49 2021, max compression
```

## Comparing `archfx_cloud-0.9.0.tar` & `archfx_cloud-0.9.1.tar`

### file list

```diff
@@ -1,27 +1,27 @@
-drwxr-xr-x   0 david     (1000) david     (1000)        0 2021-04-03 23:48:30.120000 archfx_cloud-0.9.0/
--rw-r--r--   0 david     (1000) david     (1000)       19 2021-04-03 23:24:31.000000 archfx_cloud-0.9.0/MANIFEST.in
--rw-r--r--   0 david     (1000) david     (1000)    14151 2021-04-03 23:48:30.120000 archfx_cloud-0.9.0/PKG-INFO
--rw-r--r--   0 david     (1000) david     (1000)    10694 2021-04-03 22:23:06.000000 archfx_cloud-0.9.0/README.md
-drwxr-xr-x   0 david     (1000) david     (1000)        0 2021-04-03 23:48:30.120000 archfx_cloud-0.9.0/archfx_cloud/
--rw-r--r--   0 david     (1000) david     (1000)        0 2021-04-03 21:39:27.000000 archfx_cloud-0.9.0/archfx_cloud/__init__.py
-drwxr-xr-x   0 david     (1000) david     (1000)        0 2021-04-03 23:48:30.120000 archfx_cloud-0.9.0/archfx_cloud/api/
--rw-r--r--   0 david     (1000) david     (1000)        0 2021-04-03 21:39:27.000000 archfx_cloud-0.9.0/archfx_cloud/api/__init__.py
--rw-r--r--   0 david     (1000) david     (1000)    14196 2021-04-03 21:39:27.000000 archfx_cloud-0.9.0/archfx_cloud/api/connection.py
--rw-r--r--   0 david     (1000) david     (1000)     1481 2021-04-03 21:39:27.000000 archfx_cloud-0.9.0/archfx_cloud/api/exceptions.py
-drwxr-xr-x   0 david     (1000) david     (1000)        0 2021-04-03 23:48:30.120000 archfx_cloud-0.9.0/archfx_cloud/utils/
--rw-r--r--   0 david     (1000) david     (1000)        0 2021-04-03 21:39:27.000000 archfx_cloud-0.9.0/archfx_cloud/utils/__init__.py
--rw-r--r--   0 david     (1000) david     (1000)       70 2021-04-03 21:39:27.000000 archfx_cloud-0.9.0/archfx_cloud/utils/basic.py
--rw-r--r--   0 david     (1000) david     (1000)     3726 2021-04-03 22:16:23.000000 archfx_cloud-0.9.0/archfx_cloud/utils/convert.py
--rw-r--r--   0 david     (1000) david     (1000)     5088 2021-04-03 21:54:50.000000 archfx_cloud-0.9.0/archfx_cloud/utils/main.py
--rw-r--r--   0 david     (1000) david     (1000)    13383 2021-04-03 22:24:09.000000 archfx_cloud-0.9.0/archfx_cloud/utils/slugs.py
-drwxr-xr-x   0 david     (1000) david     (1000)        0 2021-04-03 23:48:30.120000 archfx_cloud-0.9.0/archfx_cloud.egg-info/
--rw-r--r--   0 david     (1000) david     (1000)    14151 2021-04-03 23:48:30.000000 archfx_cloud-0.9.0/archfx_cloud.egg-info/PKG-INFO
--rw-r--r--   0 david     (1000) david     (1000)      564 2021-04-03 23:48:30.000000 archfx_cloud-0.9.0/archfx_cloud.egg-info/SOURCES.txt
--rw-r--r--   0 david     (1000) david     (1000)        1 2021-04-03 23:48:30.000000 archfx_cloud-0.9.0/archfx_cloud.egg-info/dependency_links.txt
--rw-r--r--   0 david     (1000) david     (1000)       55 2021-04-03 23:48:30.000000 archfx_cloud-0.9.0/archfx_cloud.egg-info/entry_points.txt
--rw-r--r--   0 david     (1000) david     (1000)        1 2021-04-03 23:06:55.000000 archfx_cloud-0.9.0/archfx_cloud.egg-info/not-zip-safe
--rw-r--r--   0 david     (1000) david     (1000)       33 2021-04-03 23:48:30.000000 archfx_cloud-0.9.0/archfx_cloud.egg-info/requires.txt
--rw-r--r--   0 david     (1000) david     (1000)       13 2021-04-03 23:48:30.000000 archfx_cloud-0.9.0/archfx_cloud.egg-info/top_level.txt
--rw-r--r--   0 david     (1000) david     (1000)       79 2021-04-03 23:48:30.120000 archfx_cloud-0.9.0/setup.cfg
--rw-r--r--   0 david     (1000) david     (1000)     2608 2021-04-03 23:48:13.000000 archfx_cloud-0.9.0/setup.py
--rw-r--r--   0 david     (1000) david     (1000)       18 2021-04-03 21:47:24.000000 archfx_cloud-0.9.0/version.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-04-04 00:59:49.441718 archfx_cloud-0.9.1/
+-rw-r--r--   0 runner    (1001) docker     (121)       19 2021-04-04 00:59:35.000000 archfx_cloud-0.9.1/MANIFEST.in
+-rw-r--r--   0 runner    (1001) docker     (121)    14563 2021-04-04 00:59:49.441718 archfx_cloud-0.9.1/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (121)    10986 2021-04-04 00:59:35.000000 archfx_cloud-0.9.1/README.md
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-04-04 00:59:49.441718 archfx_cloud-0.9.1/archfx_cloud/
+-rw-r--r--   0 runner    (1001) docker     (121)        0 2021-04-04 00:59:35.000000 archfx_cloud-0.9.1/archfx_cloud/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-04-04 00:59:49.441718 archfx_cloud-0.9.1/archfx_cloud/api/
+-rw-r--r--   0 runner    (1001) docker     (121)        0 2021-04-04 00:59:35.000000 archfx_cloud-0.9.1/archfx_cloud/api/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    14196 2021-04-04 00:59:35.000000 archfx_cloud-0.9.1/archfx_cloud/api/connection.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1481 2021-04-04 00:59:35.000000 archfx_cloud-0.9.1/archfx_cloud/api/exceptions.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-04-04 00:59:49.441718 archfx_cloud-0.9.1/archfx_cloud/utils/
+-rw-r--r--   0 runner    (1001) docker     (121)        0 2021-04-04 00:59:35.000000 archfx_cloud-0.9.1/archfx_cloud/utils/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)       70 2021-04-04 00:59:35.000000 archfx_cloud-0.9.1/archfx_cloud/utils/basic.py
+-rw-r--r--   0 runner    (1001) docker     (121)     3726 2021-04-04 00:59:35.000000 archfx_cloud-0.9.1/archfx_cloud/utils/convert.py
+-rw-r--r--   0 runner    (1001) docker     (121)     5088 2021-04-04 00:59:35.000000 archfx_cloud-0.9.1/archfx_cloud/utils/main.py
+-rw-r--r--   0 runner    (1001) docker     (121)    13383 2021-04-04 00:59:35.000000 archfx_cloud-0.9.1/archfx_cloud/utils/slugs.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-04-04 00:59:49.441718 archfx_cloud-0.9.1/archfx_cloud.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (121)    14563 2021-04-04 00:59:49.000000 archfx_cloud-0.9.1/archfx_cloud.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (121)      564 2021-04-04 00:59:49.000000 archfx_cloud-0.9.1/archfx_cloud.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (121)        1 2021-04-04 00:59:49.000000 archfx_cloud-0.9.1/archfx_cloud.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (121)       55 2021-04-04 00:59:49.000000 archfx_cloud-0.9.1/archfx_cloud.egg-info/entry_points.txt
+-rw-r--r--   0 runner    (1001) docker     (121)        1 2021-04-04 00:59:48.000000 archfx_cloud-0.9.1/archfx_cloud.egg-info/not-zip-safe
+-rw-r--r--   0 runner    (1001) docker     (121)       33 2021-04-04 00:59:49.000000 archfx_cloud-0.9.1/archfx_cloud.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (121)       13 2021-04-04 00:59:49.000000 archfx_cloud-0.9.1/archfx_cloud.egg-info/top_level.txt
+-rw-r--r--   0 runner    (1001) docker     (121)       79 2021-04-04 00:59:49.441718 archfx_cloud-0.9.1/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (121)     1499 2021-04-04 00:59:35.000000 archfx_cloud-0.9.1/setup.py
+-rw-r--r--   0 runner    (1001) docker     (121)       18 2021-04-04 00:59:35.000000 archfx_cloud-0.9.1/version.py
```

### Comparing `archfx_cloud-0.9.0/PKG-INFO` & `archfx_cloud-0.9.1/PKG-INFO`

 * *Files 3% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: archfx_cloud
-Version: 0.9.0
+Version: 0.9.1
 Summary: Python client for https://archfx.io
 Home-page: https://github.com/iotile/python_archfx_cloud
 Author: Arch Systems Inc.
 Author-email: info@archsys.io
 License: MIT
 Description: # ArchFX Cloud Python API Package
         
@@ -217,15 +217,15 @@
         self.assertEqual(str(parts['parent']), str(parent))
         self.assertEqual(str(parts['device']), str(device))
         self.assertEqual(str(parts['variable']), '0000-5501')
         
         # Other forms of use
         device = ArchFxDeviceSlug('000a)
         assert(str(device) == 'd--0000-0000-0000-000a')
-        device = ArchFxDeviceSlug(d--000a)
+        device = ArchFxDeviceSlug('d--000a')
         assert(str(device) == 'd--0000-0000-0000-000a')
         device = ArchFxDeviceSlug(0xa)
         assert(str(device) == 'd--0000-0000-0000-000a')
         ```
         
         ### BaseMain Utility Class
         
@@ -307,24 +307,39 @@
         ```
         
         ## Deployment
         
         To deploy to pypi:
         
         1. Update `version.py` with new version number
-        1. Update `CHANGELOG.md` with description of new release
+        1. Update `RELEASE.md` with description of new release
         1. Run `python setup.py test` to ensure everything is ok
         1. Commit all changes to master (PR is needed)
         1. Once everythin commited, create a new version Tag. Deployment is triggered from that:
         
         ```bash
         git tag -a v0.9.13 -m "v0.9.13"
         git push origin v0.9.13
         ```
         
+        ### Manual Release
+        
+        All deployments should be done using the Ci/CD process (github actions)
+        but just for copleteness, this is how a manual deployments is done
+        
+        ```bash
+        # Test
+        python setup.py test
+        # Build
+        python setup.py sdist bdist_wheel
+        twine check dist/*
+        # Publish
+        twine upload dist/*
+        ```
+        
 Keywords: iotile,archfx,arch,iiot,automation
 Platform: UNKNOWN
 Classifier: Programming Language :: Python
 Classifier: Programming Language :: Python :: 3
 Classifier: Programming Language :: Python :: 3.7
 Classifier: Programming Language :: Python :: 3.8
 Classifier: Programming Language :: Python :: 3.9
```

### Comparing `archfx_cloud-0.9.0/README.md` & `archfx_cloud-0.9.1/README.md`

 * *Files 2% similar despite different names*

```diff
@@ -209,15 +209,15 @@
 self.assertEqual(str(parts['parent']), str(parent))
 self.assertEqual(str(parts['device']), str(device))
 self.assertEqual(str(parts['variable']), '0000-5501')
 
 # Other forms of use
 device = ArchFxDeviceSlug('000a)
 assert(str(device) == 'd--0000-0000-0000-000a')
-device = ArchFxDeviceSlug(d--000a)
+device = ArchFxDeviceSlug('d--000a')
 assert(str(device) == 'd--0000-0000-0000-000a')
 device = ArchFxDeviceSlug(0xa)
 assert(str(device) == 'd--0000-0000-0000-000a')
 ```
 
 ### BaseMain Utility Class
 
@@ -299,16 +299,31 @@
 ```
 
 ## Deployment
 
 To deploy to pypi:
 
 1. Update `version.py` with new version number
-1. Update `CHANGELOG.md` with description of new release
+1. Update `RELEASE.md` with description of new release
 1. Run `python setup.py test` to ensure everything is ok
 1. Commit all changes to master (PR is needed)
 1. Once everythin commited, create a new version Tag. Deployment is triggered from that:
 
 ```bash
 git tag -a v0.9.13 -m "v0.9.13"
 git push origin v0.9.13
 ```
+
+### Manual Release
+
+All deployments should be done using the Ci/CD process (github actions)
+but just for copleteness, this is how a manual deployments is done
+
+```bash
+# Test
+python setup.py test
+# Build
+python setup.py sdist bdist_wheel
+twine check dist/*
+# Publish
+twine upload dist/*
+```
```

### Comparing `archfx_cloud-0.9.0/archfx_cloud/api/connection.py` & `archfx_cloud-0.9.1/archfx_cloud/api/connection.py`

 * *Files identical despite different names*

### Comparing `archfx_cloud-0.9.0/archfx_cloud/api/exceptions.py` & `archfx_cloud-0.9.1/archfx_cloud/api/exceptions.py`

 * *Files identical despite different names*

### Comparing `archfx_cloud-0.9.0/archfx_cloud/utils/convert.py` & `archfx_cloud-0.9.1/archfx_cloud/utils/convert.py`

 * *Files identical despite different names*

### Comparing `archfx_cloud-0.9.0/archfx_cloud/utils/main.py` & `archfx_cloud-0.9.1/archfx_cloud/utils/main.py`

 * *Files identical despite different names*

### Comparing `archfx_cloud-0.9.0/archfx_cloud/utils/slugs.py` & `archfx_cloud-0.9.1/archfx_cloud/utils/slugs.py`

 * *Files identical despite different names*

### Comparing `archfx_cloud-0.9.0/archfx_cloud.egg-info/PKG-INFO` & `archfx_cloud-0.9.1/archfx_cloud.egg-info/PKG-INFO`

 * *Files 3% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: archfx-cloud
-Version: 0.9.0
+Version: 0.9.1
 Summary: Python client for https://archfx.io
 Home-page: https://github.com/iotile/python_archfx_cloud
 Author: Arch Systems Inc.
 Author-email: info@archsys.io
 License: MIT
 Description: # ArchFX Cloud Python API Package
         
@@ -217,15 +217,15 @@
         self.assertEqual(str(parts['parent']), str(parent))
         self.assertEqual(str(parts['device']), str(device))
         self.assertEqual(str(parts['variable']), '0000-5501')
         
         # Other forms of use
         device = ArchFxDeviceSlug('000a)
         assert(str(device) == 'd--0000-0000-0000-000a')
-        device = ArchFxDeviceSlug(d--000a)
+        device = ArchFxDeviceSlug('d--000a')
         assert(str(device) == 'd--0000-0000-0000-000a')
         device = ArchFxDeviceSlug(0xa)
         assert(str(device) == 'd--0000-0000-0000-000a')
         ```
         
         ### BaseMain Utility Class
         
@@ -307,24 +307,39 @@
         ```
         
         ## Deployment
         
         To deploy to pypi:
         
         1. Update `version.py` with new version number
-        1. Update `CHANGELOG.md` with description of new release
+        1. Update `RELEASE.md` with description of new release
         1. Run `python setup.py test` to ensure everything is ok
         1. Commit all changes to master (PR is needed)
         1. Once everythin commited, create a new version Tag. Deployment is triggered from that:
         
         ```bash
         git tag -a v0.9.13 -m "v0.9.13"
         git push origin v0.9.13
         ```
         
+        ### Manual Release
+        
+        All deployments should be done using the Ci/CD process (github actions)
+        but just for copleteness, this is how a manual deployments is done
+        
+        ```bash
+        # Test
+        python setup.py test
+        # Build
+        python setup.py sdist bdist_wheel
+        twine check dist/*
+        # Publish
+        twine upload dist/*
+        ```
+        
 Keywords: iotile,archfx,arch,iiot,automation
 Platform: UNKNOWN
 Classifier: Programming Language :: Python
 Classifier: Programming Language :: Python :: 3
 Classifier: Programming Language :: Python :: 3.7
 Classifier: Programming Language :: Python :: 3.8
 Classifier: Programming Language :: Python :: 3.9
```

### Comparing `archfx_cloud-0.9.0/archfx_cloud.egg-info/SOURCES.txt` & `archfx_cloud-0.9.1/archfx_cloud.egg-info/SOURCES.txt`

 * *Files identical despite different names*

