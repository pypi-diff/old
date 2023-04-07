# Comparing `tmp/smops-0.1.6.tar.gz` & `tmp/smops-0.1.7.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "smops-0.1.6.tar", last modified: Fri Dec 16 10:16:04 2022, max compression
+gzip compressed data, was "smops-0.1.7.tar", last modified: Fri Apr  7 13:57:45 2023, max compression
```

## Comparing `smops-0.1.6.tar` & `smops-0.1.7.tar`

### file list

```diff
@@ -1,23 +1,23 @@
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2022-12-16 10:16:04.814224 smops-0.1.6/
--rw-r--r--   0 runner    (1001) docker     (123)      150 2022-12-16 10:15:53.000000 smops-0.1.6/AUTHORS.rst
--rw-r--r--   0 runner    (1001) docker     (123)     3484 2022-12-16 10:15:53.000000 smops-0.1.6/CONTRIBUTING.rst
--rw-r--r--   0 runner    (1001) docker     (123)      585 2022-12-16 10:15:53.000000 smops-0.1.6/HISTORY.rst
--rw-r--r--   0 runner    (1001) docker     (123)     1067 2022-12-16 10:15:53.000000 smops-0.1.6/LICENSE
--rw-r--r--   0 runner    (1001) docker     (123)      262 2022-12-16 10:15:53.000000 smops-0.1.6/MANIFEST.in
--rw-r--r--   0 runner    (1001) docker     (123)     3067 2022-12-16 10:16:04.814224 smops-0.1.6/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)     2384 2022-12-16 10:15:53.000000 smops-0.1.6/README.rst
--rw-r--r--   0 runner    (1001) docker     (123)     1093 2022-12-16 10:16:04.818224 smops-0.1.6/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (123)      266 2022-12-16 10:15:53.000000 smops-0.1.6/setup.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2022-12-16 10:16:04.814224 smops-0.1.6/smops/
--rw-r--r--   0 runner    (1001) docker     (123)      144 2022-12-16 10:15:53.000000 smops-0.1.6/smops/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     1360 2022-12-16 10:15:53.000000 smops-0.1.6/smops/cmdline.py
--rw-r--r--   0 runner    (1001) docker     (123)     1464 2022-12-16 10:15:53.000000 smops-0.1.6/smops/schema.yml
--rw-r--r--   0 runner    (1001) docker     (123)    13044 2022-12-16 10:15:53.000000 smops-0.1.6/smops/smooth.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2022-12-16 10:16:04.814224 smops-0.1.6/smops.egg-info/
--rw-r--r--   0 runner    (1001) docker     (123)     3067 2022-12-16 10:16:04.000000 smops-0.1.6/smops.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)      362 2022-12-16 10:16:04.000000 smops-0.1.6/smops.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2022-12-16 10:16:04.000000 smops-0.1.6/smops.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (123)       44 2022-12-16 10:16:04.000000 smops-0.1.6/smops.egg-info/entry_points.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2022-12-16 10:16:04.000000 smops-0.1.6/smops.egg-info/not-zip-safe
--rw-r--r--   0 runner    (1001) docker     (123)       49 2022-12-16 10:16:04.000000 smops-0.1.6/smops.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (123)        6 2022-12-16 10:16:04.000000 smops-0.1.6/smops.egg-info/top_level.txt
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 13:57:45.191517 smops-0.1.7/
+-rw-r--r--   0 runner    (1001) docker     (123)      150 2023-04-07 13:57:31.000000 smops-0.1.7/AUTHORS.rst
+-rw-r--r--   0 runner    (1001) docker     (123)     3484 2023-04-07 13:57:31.000000 smops-0.1.7/CONTRIBUTING.rst
+-rw-r--r--   0 runner    (1001) docker     (123)      720 2023-04-07 13:57:31.000000 smops-0.1.7/HISTORY.rst
+-rw-r--r--   0 runner    (1001) docker     (123)     1067 2023-04-07 13:57:31.000000 smops-0.1.7/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (123)      262 2023-04-07 13:57:31.000000 smops-0.1.7/MANIFEST.in
+-rw-r--r--   0 runner    (1001) docker     (123)     3067 2023-04-07 13:57:45.191517 smops-0.1.7/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     2384 2023-04-07 13:57:31.000000 smops-0.1.7/README.rst
+-rw-r--r--   0 runner    (1001) docker     (123)     1102 2023-04-07 13:57:45.191517 smops-0.1.7/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (123)      266 2023-04-07 13:57:31.000000 smops-0.1.7/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 13:57:45.187517 smops-0.1.7/smops/
+-rw-r--r--   0 runner    (1001) docker     (123)      144 2023-04-07 13:57:31.000000 smops-0.1.7/smops/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1360 2023-04-07 13:57:31.000000 smops-0.1.7/smops/cmdline.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1464 2023-04-07 13:57:31.000000 smops-0.1.7/smops/schema.yml
+-rw-r--r--   0 runner    (1001) docker     (123)    13108 2023-04-07 13:57:31.000000 smops-0.1.7/smops/smooth.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 13:57:45.191517 smops-0.1.7/smops.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)     3067 2023-04-07 13:57:45.000000 smops-0.1.7/smops.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)      362 2023-04-07 13:57:45.000000 smops-0.1.7/smops.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-07 13:57:45.000000 smops-0.1.7/smops.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       44 2023-04-07 13:57:45.000000 smops-0.1.7/smops.egg-info/entry_points.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-07 13:57:45.000000 smops-0.1.7/smops.egg-info/not-zip-safe
+-rw-r--r--   0 runner    (1001) docker     (123)       58 2023-04-07 13:57:45.000000 smops-0.1.7/smops.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        6 2023-04-07 13:57:45.000000 smops-0.1.7/smops.egg-info/top_level.txt
```

### Comparing `smops-0.1.6/CONTRIBUTING.rst` & `smops-0.1.7/CONTRIBUTING.rst`

 * *Files identical despite different names*

### Comparing `smops-0.1.6/HISTORY.rst` & `smops-0.1.7/HISTORY.rst`

 * *Files 12% similar despite different names*

```diff
@@ -1,10 +1,15 @@
 =======
 History
 =======
+0.1.7 (2023-04-07)
+------------------
+* Return stimela as a dependency
+* Allow NaN values while dealing with interpolations, issue #5
+
 
 0.1.6 (2022-12-16)
 ------------------
 * Removed stimela2 as a dependency
 
 
 0.1.5 (2022-12-7)
```

### Comparing `smops-0.1.6/LICENSE` & `smops-0.1.7/LICENSE`

 * *Files identical despite different names*

### Comparing `smops-0.1.6/PKG-INFO` & `smops-0.1.7/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: smops
-Version: 0.1.6
+Version: 0.1.7
 Summary: Python script for interpolating FITS model images over frequency
 Home-page: https://github.com/mulan-94/smops
 Author: L. Andati
 License: MIT license
 Keywords: smops,model frequency interpolation,FITS images
 Classifier: Development Status :: 4 - Beta
 Classifier: Intended Audience :: Developers
```

### Comparing `smops-0.1.6/README.rst` & `smops-0.1.7/README.rst`

 * *Files identical despite different names*

### Comparing `smops-0.1.6/setup.cfg` & `smops-0.1.7/setup.cfg`

 * *Files 7% similar despite different names*

```diff
@@ -28,15 +28,15 @@
 zip_safe = False
 install_requires = 
 	astropy
 	dask
 	python-casacore
 	psutil
 	numpy
-	scabha
+	stimela==2.0rc4
 
 [options.package_data]
 * = *.yml
 
 [bdist_wheel]
 universal = 1
```

### Comparing `smops-0.1.6/smops/cmdline.py` & `smops-0.1.7/smops/cmdline.py`

 * *Files identical despite different names*

### Comparing `smops-0.1.6/smops/schema.yml` & `smops-0.1.7/smops/schema.yml`

 * *Files identical despite different names*

### Comparing `smops-0.1.6/smops/smooth.py` & `smops-0.1.7/smops/smooth.py`

 * *Files 1% similar despite different names*

```diff
@@ -186,15 +186,16 @@
 
     result = {"xdims": nx, "ydims": ny}
 
     # components excluding zeros
     mask = np.any(model, axis=0)
     beta = model*mask
     beta = beta.reshape(nband, -1)
-    
+    beta = np.ma.masked_invalid(beta)
+    beta.fill_value = np.nan
    
     if spectral_poly_order > infreqs.size:
         raise ValueError(f"spectral-poly-order can't be larger than nband ({nband})")
 
     # we are given frequencies at bin centers, convert to bin edges
     #delta_freq is the same as CDELt value in the image header
     delta_freq = infreqs[1] - infreqs[0] 
@@ -206,16 +207,15 @@
     # set design matrix for each component
     # look at Offringa and Smirnov 1706.06786
     xfit = np.zeros([nband, spectral_poly_order])
     for i in range(1, spectral_poly_order+1):
         xfit[:, i-1] = (whigh**i - wlow**i)/(i*wdiff)
 
 
-
-    dirty_comps = np.dot(xfit.T, wsums*beta)
+    dirty_comps = np.ma.dot(xfit.T, wsums*beta)
     hess_comps = xfit.T.dot(wsums*xfit)
 
     comps = da.from_array(
         np.linalg.solve(hess_comps, dirty_comps),
         chunks="auto")
 
     w = outfreqs/ref_freq
```

### Comparing `smops-0.1.6/smops.egg-info/PKG-INFO` & `smops-0.1.7/smops.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: smops
-Version: 0.1.6
+Version: 0.1.7
 Summary: Python script for interpolating FITS model images over frequency
 Home-page: https://github.com/mulan-94/smops
 Author: L. Andati
 License: MIT license
 Keywords: smops,model frequency interpolation,FITS images
 Classifier: Development Status :: 4 - Beta
 Classifier: Intended Audience :: Developers
```

