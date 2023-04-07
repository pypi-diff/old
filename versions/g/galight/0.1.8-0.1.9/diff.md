# Comparing `tmp/galight-0.1.8.tar.gz` & `tmp/galight-0.1.9.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "galight-0.1.8.tar", last modified: Sat Jul 16 07:44:31 2022, max compression
+gzip compressed data, was "galight-0.1.9.tar", last modified: Mon Jul 18 03:57:15 2022, max compression
```

## Comparing `galight-0.1.8.tar` & `galight-0.1.9.tar`

### file list

```diff
@@ -1,60 +1,60 @@
-drwxr-xr-x   0 Dartoon    (501) staff       (20)        0 2022-07-16 07:44:31.921487 galight-0.1.8/
--rw-r--r--   0 Dartoon    (501) staff       (20)     1812 2022-01-05 06:46:18.000000 galight-0.1.8/.gitignore
--rw-r--r--   0 Dartoon    (501) staff       (20)      563 2021-04-15 09:22:25.000000 galight-0.1.8/.readthedocs.yaml
--rw-r--r--   0 Dartoon    (501) staff       (20)      216 2022-05-16 08:36:50.000000 galight-0.1.8/AUTHORS.rst
--rw-r--r--   0 Dartoon    (501) staff       (20)     2982 2021-05-25 12:34:49.000000 galight-0.1.8/CONTRIBUTING.rst
--rw-r--r--   0 Dartoon    (501) staff       (20)     1730 2022-07-16 07:43:27.000000 galight-0.1.8/HISTORY.rst
--rw-r--r--   0 Dartoon    (501) staff       (20)     1078 2020-09-04 06:37:59.000000 galight-0.1.8/LICENSE
--rw-r--r--   0 Dartoon    (501) staff       (20)      100 2020-09-04 06:37:59.000000 galight-0.1.8/MANIFEST.in
--rw-r--r--   0 Dartoon    (501) staff       (20)     1295 2021-05-25 12:34:50.000000 galight-0.1.8/Makefile
--rw-r--r--   0 Dartoon    (501) staff       (20)     3074 2022-07-16 07:44:31.921578 galight-0.1.8/PKG-INFO
--rw-r--r--   0 Dartoon    (501) staff       (20)     3209 2022-06-21 02:41:21.000000 galight-0.1.8/README.md
--rw-r--r--   0 Dartoon    (501) staff       (20)     2246 2021-06-07 15:14:51.000000 galight-0.1.8/README.rst
-drwxr-xr-x   0 Dartoon    (501) staff       (20)        0 2022-07-16 07:44:31.913695 galight-0.1.8/docs/
--rw-r--r--   0 Dartoon    (501) staff       (20)     6778 2020-09-04 06:37:59.000000 galight-0.1.8/docs/Makefile
--rw-r--r--   0 Dartoon    (501) staff       (20)       28 2020-09-04 06:37:59.000000 galight-0.1.8/docs/authors.rst
--rw-r--r--   0 Dartoon    (501) staff       (20)     8201 2021-05-25 12:34:55.000000 galight-0.1.8/docs/conf.py
--rw-r--r--   0 Dartoon    (501) staff       (20)       33 2020-09-04 06:37:59.000000 galight-0.1.8/docs/contributing.rst
--rw-r--r--   0 Dartoon    (501) staff       (20)      238 2021-05-25 12:34:55.000000 galight-0.1.8/docs/galight.data_process.rst
--rw-r--r--   0 Dartoon    (501) staff       (20)      247 2021-05-25 12:34:56.000000 galight-0.1.8/docs/galight.fitting_process.rst
--rw-r--r--   0 Dartoon    (501) staff       (20)      247 2021-05-25 12:34:57.000000 galight-0.1.8/docs/galight.fitting_specify.rst
--rw-r--r--   0 Dartoon    (501) staff       (20)      175 2021-05-25 12:34:57.000000 galight-0.1.8/docs/galight.rst
--rw-r--r--   0 Dartoon    (501) staff       (20)      873 2021-05-25 12:34:58.000000 galight-0.1.8/docs/galight.tools.rst
--rw-r--r--   0 Dartoon    (501) staff       (20)       28 2020-09-04 06:37:59.000000 galight-0.1.8/docs/history.rst
--rw-r--r--   0 Dartoon    (501) staff       (20)     1638 2022-06-21 02:41:21.000000 galight-0.1.8/docs/index.rst
--rw-r--r--   0 Dartoon    (501) staff       (20)      270 2021-05-25 12:34:59.000000 galight-0.1.8/docs/installation.rst
--rw-r--r--   0 Dartoon    (501) staff       (20)     6467 2020-09-04 06:37:59.000000 galight-0.1.8/docs/make.bat
--rw-r--r--   0 Dartoon    (501) staff       (20)      917 2021-05-25 12:34:59.000000 galight-0.1.8/docs/usage.rst
-drwxr-xr-x   0 Dartoon    (501) staff       (20)        0 2022-07-16 07:44:31.915795 galight-0.1.8/figs/
--rw-r--r--   0 Dartoon    (501) staff       (20)   162902 2021-05-17 12:57:12.000000 galight-0.1.8/figs/est_bkgstd.png
--rw-r--r--   0 Dartoon    (501) staff       (20)    86394 2021-05-17 12:52:01.000000 galight-0.1.8/figs/find_PSF.png
--rw-r--r--   0 Dartoon    (501) staff       (20)   249482 2021-11-15 01:26:25.000000 galight-0.1.8/figs/fitting_result.png
--rw-r--r--   0 Dartoon    (501) staff       (20)   382600 2021-05-17 13:03:39.000000 galight-0.1.8/figs/fitting_sets.png
-drwxr-xr-x   0 Dartoon    (501) staff       (20)        0 2022-07-16 07:44:31.917860 galight-0.1.8/galight/
--rw-r--r--   0 Dartoon    (501) staff       (20)      109 2022-06-24 02:54:05.000000 galight-0.1.8/galight/__init__.py
--rwxr-xr-x   0 Dartoon    (501) staff       (20)    23751 2022-07-15 07:21:30.000000 galight-0.1.8/galight/data_process.py
--rwxr-xr-x   0 Dartoon    (501) staff       (20)    29617 2022-06-25 15:03:21.000000 galight-0.1.8/galight/fitting_process.py
--rwxr-xr-x   0 Dartoon    (501) staff       (20)    22847 2022-05-30 05:55:57.000000 galight-0.1.8/galight/fitting_specify.py
-drwxr-xr-x   0 Dartoon    (501) staff       (20)        0 2022-07-16 07:44:31.919441 galight-0.1.8/galight/hsc_utils/
--rw-r--r--   0 Dartoon    (501) staff       (20)      126 2022-06-24 02:54:12.000000 galight-0.1.8/galight/hsc_utils/__init__.py
--rwxr-xr-x   0 Dartoon    (501) staff       (20)     4772 2021-11-30 00:10:53.000000 galight-0.1.8/galight/hsc_utils/hsc_image.py
--rwxr-xr-x   0 Dartoon    (501) staff       (20)     3910 2021-11-30 00:11:13.000000 galight-0.1.8/galight/hsc_utils/hsc_psf.py
-drwxr-xr-x   0 Dartoon    (501) staff       (20)        0 2022-07-16 07:44:31.921165 galight-0.1.8/galight/tools/
--rw-r--r--   0 Dartoon    (501) staff       (20)      109 2022-06-24 02:54:16.000000 galight-0.1.8/galight/tools/__init__.py
--rwxr-xr-x   0 Dartoon    (501) staff       (20)     4424 2022-06-29 09:18:12.000000 galight-0.1.8/galight/tools/astro_tools.py
--rw-r--r--   0 Dartoon    (501) staff       (20)    32127 2022-06-28 23:06:56.000000 galight-0.1.8/galight/tools/asymmetry_tools.py
--rwxr-xr-x   0 Dartoon    (501) staff       (20)     8690 2022-07-14 07:22:35.000000 galight-0.1.8/galight/tools/cutout_tools.py
--rwxr-xr-x   0 Dartoon    (501) staff       (20)    37416 2022-07-14 07:02:27.000000 galight-0.1.8/galight/tools/measure_tools.py
--rwxr-xr-x   0 Dartoon    (501) staff       (20)    16861 2022-05-19 06:55:18.000000 galight-0.1.8/galight/tools/plot_tools.py
-drwxr-xr-x   0 Dartoon    (501) staff       (20)        0 2022-07-16 07:44:31.918871 galight-0.1.8/galight.egg-info/
--rw-r--r--   0 Dartoon    (501) staff       (20)     3074 2022-07-16 07:44:31.000000 galight-0.1.8/galight.egg-info/PKG-INFO
--rw-r--r--   0 Dartoon    (501) staff       (20)     1077 2022-07-16 07:44:31.000000 galight-0.1.8/galight.egg-info/SOURCES.txt
--rw-r--r--   0 Dartoon    (501) staff       (20)        1 2022-07-16 07:44:31.000000 galight-0.1.8/galight.egg-info/dependency_links.txt
--rw-r--r--   0 Dartoon    (501) staff       (20)        1 2020-09-04 06:43:16.000000 galight-0.1.8/galight.egg-info/not-zip-safe
--rw-r--r--   0 Dartoon    (501) staff       (20)        8 2022-07-16 07:44:31.000000 galight-0.1.8/galight.egg-info/top_level.txt
--rw-r--r--   0 Dartoon    (501) staff       (20)      467 2022-05-16 09:04:43.000000 galight-0.1.8/requirements.txt
--rw-r--r--   0 Dartoon    (501) staff       (20)       61 2022-07-16 07:44:31.921867 galight-0.1.8/setup.cfg
--rw-r--r--   0 Dartoon    (501) staff       (20)     1498 2022-06-24 02:53:57.000000 galight-0.1.8/setup.py
-drwxr-xr-x   0 Dartoon    (501) staff       (20)        0 2022-07-16 07:44:31.921361 galight-0.1.8/test/
--rwxr-xr-x   0 Dartoon    (501) staff       (20)      268 2021-05-25 12:34:48.000000 galight-0.1.8/test/test_decomprofile.py
--rw-r--r--   0 Dartoon    (501) staff       (20)      499 2021-05-25 12:34:54.000000 galight-0.1.8/tox.ini
+drwxr-xr-x   0 Dartoon    (501) staff       (20)        0 2022-07-18 03:57:15.632192 galight-0.1.9/
+-rw-r--r--   0 Dartoon    (501) staff       (20)     1812 2022-01-05 06:46:18.000000 galight-0.1.9/.gitignore
+-rw-r--r--   0 Dartoon    (501) staff       (20)      563 2021-04-15 09:22:25.000000 galight-0.1.9/.readthedocs.yaml
+-rw-r--r--   0 Dartoon    (501) staff       (20)      216 2022-05-16 08:36:50.000000 galight-0.1.9/AUTHORS.rst
+-rw-r--r--   0 Dartoon    (501) staff       (20)     2982 2021-05-25 12:34:49.000000 galight-0.1.9/CONTRIBUTING.rst
+-rw-r--r--   0 Dartoon    (501) staff       (20)     1858 2022-07-18 03:55:34.000000 galight-0.1.9/HISTORY.rst
+-rw-r--r--   0 Dartoon    (501) staff       (20)     1078 2020-09-04 06:37:59.000000 galight-0.1.9/LICENSE
+-rw-r--r--   0 Dartoon    (501) staff       (20)      100 2020-09-04 06:37:59.000000 galight-0.1.9/MANIFEST.in
+-rw-r--r--   0 Dartoon    (501) staff       (20)     1295 2021-05-25 12:34:50.000000 galight-0.1.9/Makefile
+-rw-r--r--   0 Dartoon    (501) staff       (20)     3074 2022-07-18 03:57:15.632291 galight-0.1.9/PKG-INFO
+-rw-r--r--   0 Dartoon    (501) staff       (20)     3209 2022-06-21 02:41:21.000000 galight-0.1.9/README.md
+-rw-r--r--   0 Dartoon    (501) staff       (20)     2246 2021-06-07 15:14:51.000000 galight-0.1.9/README.rst
+drwxr-xr-x   0 Dartoon    (501) staff       (20)        0 2022-07-18 03:57:15.623862 galight-0.1.9/docs/
+-rw-r--r--   0 Dartoon    (501) staff       (20)     6778 2020-09-04 06:37:59.000000 galight-0.1.9/docs/Makefile
+-rw-r--r--   0 Dartoon    (501) staff       (20)       28 2020-09-04 06:37:59.000000 galight-0.1.9/docs/authors.rst
+-rw-r--r--   0 Dartoon    (501) staff       (20)     8201 2021-05-25 12:34:55.000000 galight-0.1.9/docs/conf.py
+-rw-r--r--   0 Dartoon    (501) staff       (20)       33 2020-09-04 06:37:59.000000 galight-0.1.9/docs/contributing.rst
+-rw-r--r--   0 Dartoon    (501) staff       (20)      238 2021-05-25 12:34:55.000000 galight-0.1.9/docs/galight.data_process.rst
+-rw-r--r--   0 Dartoon    (501) staff       (20)      247 2021-05-25 12:34:56.000000 galight-0.1.9/docs/galight.fitting_process.rst
+-rw-r--r--   0 Dartoon    (501) staff       (20)      247 2021-05-25 12:34:57.000000 galight-0.1.9/docs/galight.fitting_specify.rst
+-rw-r--r--   0 Dartoon    (501) staff       (20)      175 2021-05-25 12:34:57.000000 galight-0.1.9/docs/galight.rst
+-rw-r--r--   0 Dartoon    (501) staff       (20)      873 2021-05-25 12:34:58.000000 galight-0.1.9/docs/galight.tools.rst
+-rw-r--r--   0 Dartoon    (501) staff       (20)       28 2020-09-04 06:37:59.000000 galight-0.1.9/docs/history.rst
+-rw-r--r--   0 Dartoon    (501) staff       (20)     1638 2022-06-21 02:41:21.000000 galight-0.1.9/docs/index.rst
+-rw-r--r--   0 Dartoon    (501) staff       (20)      270 2021-05-25 12:34:59.000000 galight-0.1.9/docs/installation.rst
+-rw-r--r--   0 Dartoon    (501) staff       (20)     6467 2020-09-04 06:37:59.000000 galight-0.1.9/docs/make.bat
+-rw-r--r--   0 Dartoon    (501) staff       (20)      917 2021-05-25 12:34:59.000000 galight-0.1.9/docs/usage.rst
+drwxr-xr-x   0 Dartoon    (501) staff       (20)        0 2022-07-18 03:57:15.625912 galight-0.1.9/figs/
+-rw-r--r--   0 Dartoon    (501) staff       (20)   162902 2021-05-17 12:57:12.000000 galight-0.1.9/figs/est_bkgstd.png
+-rw-r--r--   0 Dartoon    (501) staff       (20)    86394 2021-05-17 12:52:01.000000 galight-0.1.9/figs/find_PSF.png
+-rw-r--r--   0 Dartoon    (501) staff       (20)   249482 2021-11-15 01:26:25.000000 galight-0.1.9/figs/fitting_result.png
+-rw-r--r--   0 Dartoon    (501) staff       (20)   382600 2021-05-17 13:03:39.000000 galight-0.1.9/figs/fitting_sets.png
+drwxr-xr-x   0 Dartoon    (501) staff       (20)        0 2022-07-18 03:57:15.628118 galight-0.1.9/galight/
+-rw-r--r--   0 Dartoon    (501) staff       (20)      109 2022-07-18 03:56:08.000000 galight-0.1.9/galight/__init__.py
+-rwxr-xr-x   0 Dartoon    (501) staff       (20)    25056 2022-07-17 08:26:53.000000 galight-0.1.9/galight/data_process.py
+-rwxr-xr-x   0 Dartoon    (501) staff       (20)    29617 2022-06-25 15:03:21.000000 galight-0.1.9/galight/fitting_process.py
+-rwxr-xr-x   0 Dartoon    (501) staff       (20)    22847 2022-05-30 05:55:57.000000 galight-0.1.9/galight/fitting_specify.py
+drwxr-xr-x   0 Dartoon    (501) staff       (20)        0 2022-07-18 03:57:15.629919 galight-0.1.9/galight/hsc_utils/
+-rw-r--r--   0 Dartoon    (501) staff       (20)      126 2022-07-18 03:56:13.000000 galight-0.1.9/galight/hsc_utils/__init__.py
+-rwxr-xr-x   0 Dartoon    (501) staff       (20)     4772 2021-11-30 00:10:53.000000 galight-0.1.9/galight/hsc_utils/hsc_image.py
+-rwxr-xr-x   0 Dartoon    (501) staff       (20)     3910 2021-11-30 00:11:13.000000 galight-0.1.9/galight/hsc_utils/hsc_psf.py
+drwxr-xr-x   0 Dartoon    (501) staff       (20)        0 2022-07-18 03:57:15.631769 galight-0.1.9/galight/tools/
+-rw-r--r--   0 Dartoon    (501) staff       (20)      109 2022-07-18 03:56:18.000000 galight-0.1.9/galight/tools/__init__.py
+-rwxr-xr-x   0 Dartoon    (501) staff       (20)     4700 2022-07-16 16:29:09.000000 galight-0.1.9/galight/tools/astro_tools.py
+-rw-r--r--   0 Dartoon    (501) staff       (20)    32414 2022-07-17 10:02:02.000000 galight-0.1.9/galight/tools/asymmetry_tools.py
+-rwxr-xr-x   0 Dartoon    (501) staff       (20)     8690 2022-07-14 07:22:35.000000 galight-0.1.9/galight/tools/cutout_tools.py
+-rwxr-xr-x   0 Dartoon    (501) staff       (20)    38227 2022-07-16 16:08:39.000000 galight-0.1.9/galight/tools/measure_tools.py
+-rwxr-xr-x   0 Dartoon    (501) staff       (20)    16861 2022-05-19 06:55:18.000000 galight-0.1.9/galight/tools/plot_tools.py
+drwxr-xr-x   0 Dartoon    (501) staff       (20)        0 2022-07-18 03:57:15.629311 galight-0.1.9/galight.egg-info/
+-rw-r--r--   0 Dartoon    (501) staff       (20)     3074 2022-07-18 03:57:15.000000 galight-0.1.9/galight.egg-info/PKG-INFO
+-rw-r--r--   0 Dartoon    (501) staff       (20)     1077 2022-07-18 03:57:15.000000 galight-0.1.9/galight.egg-info/SOURCES.txt
+-rw-r--r--   0 Dartoon    (501) staff       (20)        1 2022-07-18 03:57:15.000000 galight-0.1.9/galight.egg-info/dependency_links.txt
+-rw-r--r--   0 Dartoon    (501) staff       (20)        1 2020-09-04 06:43:16.000000 galight-0.1.9/galight.egg-info/not-zip-safe
+-rw-r--r--   0 Dartoon    (501) staff       (20)        8 2022-07-18 03:57:15.000000 galight-0.1.9/galight.egg-info/top_level.txt
+-rw-r--r--   0 Dartoon    (501) staff       (20)      467 2022-05-16 09:04:43.000000 galight-0.1.9/requirements.txt
+-rw-r--r--   0 Dartoon    (501) staff       (20)       61 2022-07-18 03:57:15.634439 galight-0.1.9/setup.cfg
+-rw-r--r--   0 Dartoon    (501) staff       (20)     1498 2022-07-18 03:56:00.000000 galight-0.1.9/setup.py
+drwxr-xr-x   0 Dartoon    (501) staff       (20)        0 2022-07-18 03:57:15.632063 galight-0.1.9/test/
+-rwxr-xr-x   0 Dartoon    (501) staff       (20)      268 2021-05-25 12:34:48.000000 galight-0.1.9/test/test_decomprofile.py
+-rw-r--r--   0 Dartoon    (501) staff       (20)      499 2021-05-25 12:34:54.000000 galight-0.1.9/tox.ini
```

### Comparing `galight-0.1.8/.gitignore` & `galight-0.1.9/.gitignore`

 * *Files identical despite different names*

### Comparing `galight-0.1.8/.readthedocs.yaml` & `galight-0.1.9/.readthedocs.yaml`

 * *Files identical despite different names*

### Comparing `galight-0.1.8/CONTRIBUTING.rst` & `galight-0.1.9/CONTRIBUTING.rst`

 * *Files identical despite different names*

### Comparing `galight-0.1.8/HISTORY.rst` & `galight-0.1.9/HISTORY.rst`

 * *Files 4% similar despite different names*

```diff
@@ -70,7 +70,13 @@
 
 * Improve reduced chisq calcualtions.
 * Improve stretch of showing image and use bbox_inches='tight'.
 * Debug for functions including cal_statmorph() and targets_subtraction().
 * Improve PSF selection function.
 * Update for lenstronomy > 1.10.3 and new photutils version 1.5.0
 
+
+0.1.9 (2022-07-18)
+++++++++++++++++++
+
+* Add PSF stacking function using photutils.EPSFBuilder 
+* Improve the CAS measurement
```

### Comparing `galight-0.1.8/LICENSE` & `galight-0.1.9/LICENSE`

 * *Files identical despite different names*

### Comparing `galight-0.1.8/Makefile` & `galight-0.1.9/Makefile`

 * *Files identical despite different names*

### Comparing `galight-0.1.8/PKG-INFO` & `galight-0.1.9/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: galight
-Version: 0.1.8
+Version: 0.1.9
 Summary: Galaxy light 2D modeling tool
 Home-page: https://github.com/dartoon/galight
 Author: Xuheng Ding
 Author-email: xuheng.ding@ipmu.jp
 License: MIT
 Keywords: galight
 Platform: UNKNOWN
```

### Comparing `galight-0.1.8/README.md` & `galight-0.1.9/README.md`

 * *Files identical despite different names*

### Comparing `galight-0.1.8/README.rst` & `galight-0.1.9/README.rst`

 * *Files identical despite different names*

### Comparing `galight-0.1.8/docs/Makefile` & `galight-0.1.9/docs/Makefile`

 * *Files identical despite different names*

### Comparing `galight-0.1.8/docs/conf.py` & `galight-0.1.9/docs/conf.py`

 * *Files identical despite different names*

### Comparing `galight-0.1.8/docs/galight.tools.rst` & `galight-0.1.9/docs/galight.tools.rst`

 * *Files identical despite different names*

### Comparing `galight-0.1.8/docs/index.rst` & `galight-0.1.9/docs/index.rst`

 * *Files identical despite different names*

### Comparing `galight-0.1.8/docs/make.bat` & `galight-0.1.9/docs/make.bat`

 * *Files identical despite different names*

### Comparing `galight-0.1.8/docs/usage.rst` & `galight-0.1.9/docs/usage.rst`

 * *Files identical despite different names*

### Comparing `galight-0.1.8/figs/est_bkgstd.png` & `galight-0.1.9/figs/est_bkgstd.png`

 * *Files identical despite different names*

### Comparing `galight-0.1.8/figs/find_PSF.png` & `galight-0.1.9/figs/find_PSF.png`

 * *Files identical despite different names*

### Comparing `galight-0.1.8/figs/fitting_result.png` & `galight-0.1.9/figs/fitting_result.png`

 * *Files identical despite different names*

### Comparing `galight-0.1.8/figs/fitting_sets.png` & `galight-0.1.9/figs/fitting_sets.png`

 * *Files identical despite different names*

### Comparing `galight-0.1.8/galight/data_process.py` & `galight-0.1.9/galight/data_process.py`

 * *Files 3% similar despite different names*

```diff
@@ -19,14 +19,15 @@
 from matplotlib.colors import LogNorm
 from galight.tools.astro_tools import plt_fits, read_pixel_scale
 import photutils
 import sys
 from packaging import version
 from galight.tools.measure_tools import search_local_max, measure_FWHM
 from galight.tools.measure_tools import detect_obj
+from galight.tools.astro_tools import plt_many_fits
 class DataProcess(object):
     """
     A class to Process the data, including the following feature:
         - automaticlly estimate and remove background light.
         - cutout the target photo stamp.
         - search all the avaiable PSF in the field.
         - creat mask for the objects.
@@ -164,17 +165,17 @@
                     except:
                         gauss_mean, gauss_1sig = np.mean(edge_data), np.std(edge_data)
                     up_limit = gauss_mean + 2 * gauss_1sig
                     percent = np.sum(edge_data>up_limit)/float(len(edge_data))
                     if percent<0.03:
                         break
                 radius = rad
-            if if_plot == True:
-                print("Plot target cut out zoom in:")
             if cut_kernel is not None:
+                if if_plot == True:
+                    print("Plot target cut out zoom in:")
                 target_stamp, self.target_pos = cut_center_auto(image=self.fov_image, center= self.target_pos, 
                                                   kernel = cut_kernel, radius=radius,
                                                   return_center=True, if_plot=if_plot)
             else:
                 target_stamp = cutout(image = self.fov_image, center = self.target_pos, radius=radius)
         self.radius = int(len(target_stamp)/2)
         
@@ -302,15 +303,15 @@
         cl_list = list(dict.fromkeys(cl_list)) 
         cl_list.reverse()
         for i in cl_list:
             self.segm_deblend[self.segm_deblend>i]  = self.segm_deblend[self.segm_deblend>i] - 1
             self.tbl.remove_row(i)
             
     def find_PSF(self, radius = 50, PSF_pos_list = None, pos_type = 'pixel', psf_edge=120, FWHM_sort=False,
-                 if_filter=False, FWHM_filer = None, user_option= False, select_all=True,
+                 if_filter=False, FWHM_filer = None, user_option= False, select_all=False,
                  nearyby_obj_filter = False , **kwargs):
         """
         Find all the available PSF candidates in the field of view.
         
         Parameter
         --------
             radius: int/float.
@@ -387,15 +388,14 @@
                 fluxs = fluxs[select_bool]
                 PSF_cutouts = PSF_cutouts[select_bool]
             else:
                 PSF_locs = init_PSF_locs
             if user_option == False:
                 select_idx = [np.where(FWHMs == FWHMs.min())[0][0]]
             else:
-                from galight.tools.astro_tools import plt_many_fits
                 plt_many_fits(PSF_cutouts, FWHMs, 'FWHM')
                 if select_all is not True:
                     if sys.version_info[0] == 2:
                         select_idx = raw_input('Input directly the PSF inital id to select, use space between each id:\n (press Enter to selet all)\n')
                     elif sys.version_info[0] == 3:
                         select_idx = input('Input directly the PSF inital id to select, use space between each id:\n (press Enter to selet all)\n')
                 else:
@@ -422,14 +422,38 @@
 
     def profiles_compare(self, **kargs):
         """
         Use galight.tools.measure_tools.profiles_compare to plot the profiles of data and PSFs (when prepared).
         """    
         from galight.tools.measure_tools import profiles_compare    
         profiles_compare([self.target_stamp] + self.PSF_list, **kargs)
+
+
+    def stack_PSF(self,  oversampling=1, maxiters=10, tool = 'photutils',if_plot=False):
+        if hasattr(self, 'stack_PSF_done'):
+            print("WARNING: PSF has stacked already! Let's just show the plot.")
+        else:
+            from galight.tools.measure_tools import stack_PSF
+            stack_PSF = stack_PSF(self.fov_image, self.PSF_pos_list, psf_size=len(self.PSF_list[0]),
+                             oversampling=oversampling, maxiters=maxiters, tool = tool)
+            self.PSF_list.append(stack_PSF)
+            self.PSF_FWHM_list.append(np.mean(measure_FWHM(stack_PSF)))
+            self.psf_id_for_fitting = -1
+        # print('The stack PSF in the last:')
+        labels = ['PSF{0}'.format(i) for i in range(len(self.PSF_list))]
+        labels[-1] = 'stacked PSF'
+        plt_many_fits(self.PSF_list[:-1]+[self.PSF_list[-1]*np.sum(self.PSF_list[0])], self.PSF_FWHM_list, 'FWHM', labels = labels)
+        print('Plot residual:')
+        labels = ['stacked - PSF{0}'.format(i) for i in range(len(self.PSF_list))]
+        plt_many_fits([(self.PSF_list[-1]/np.sum(self.PSF_list[-1]) - 
+                        self.PSF_list[i]/np.sum(self.PSF_list[i]) ) for i in range(len(self.PSF_list)-1)], 
+                      labels = labels[:-1], norm = None)
+        self.stack_PSF_done = True
+
+
         
     def plot_overview(self, **kargs):
         """
         Use galight.tools.cutout_tools.plot_overview to plot image overview.
         """
         from galight.tools.cutout_tools import plot_overview
         if hasattr(self, 'PSF_pos_list'):
```

### Comparing `galight-0.1.8/galight/fitting_process.py` & `galight-0.1.9/galight/fitting_process.py`

 * *Files identical despite different names*

### Comparing `galight-0.1.8/galight/fitting_specify.py` & `galight-0.1.9/galight/fitting_specify.py`

 * *Files identical despite different names*

### Comparing `galight-0.1.8/galight/hsc_utils/hsc_image.py` & `galight-0.1.9/galight/hsc_utils/hsc_image.py`

 * *Files identical despite different names*

### Comparing `galight-0.1.8/galight/hsc_utils/hsc_psf.py` & `galight-0.1.9/galight/hsc_utils/hsc_psf.py`

 * *Files identical despite different names*

### Comparing `galight-0.1.8/galight/tools/astro_tools.py` & `galight-0.1.9/galight/tools/astro_tools.py`

 * *Files 10% similar despite different names*

```diff
@@ -28,15 +28,15 @@
     """
     wcs = WCS(header)
     # diff_RA_DEC = wcs.all_pix2world([0,0],[0,100],1)
     # diff_scale = np.sqrt((diff_RA_DEC[0][1]-diff_RA_DEC[0][0])**2 + (diff_RA_DEC[1][1]-diff_RA_DEC[1][0])**2)
     # pix_scale = diff_scale * 3600 / 100
     from astropy.wcs.utils import proj_plane_pixel_scales
     scales = proj_plane_pixel_scales(wcs) * 3600  #From degree to arcsec
-    if scales[0] != scales[1]:
+    if abs(scales[0]-scales[1])/scales[0]>1.e-5:
         print('Warning: Pixel scale is not the same along x and y!!!')
     pix_scale = scales[0] 
     return pix_scale
 
 def read_fits_exp(header):
     """
     Readout the header information from a pyfits file.
@@ -48,24 +48,31 @@
         
     Return
     --------
         The pixel scale in arcsec scale.
     """    
     return header['EXPTIME']
 
-def plt_fits(img, norm = None, figsize = None, colorbar = False, savename = None, vmin= None, vmax=None, hold = False):
+def plt_fits(img, norm = 'log', figsize = None, colorbar = False, savename = None, 
+             vmin= None, vmax=None, cmap = 'gist_heat', hold = False):
     """
     Directly plot a 2D image using imshow.
     """
+    import copy, matplotlib
+    if cmap == 'gist_heat':
+        my_cmap = copy.copy(matplotlib.cm.get_cmap('gist_heat')) # copy the default cmap
+        my_cmap.set_bad('black')
+    else:
+        my_cmap = None
     fig, ax = plt.subplots(figsize=figsize)
-    if norm is None or norm == 'log':
+    if norm == 'log':
         norm = LogNorm(vmin=vmin, vmax=vmax)#np.max(img[~np.isnan(img)]))
     else:
-        norm = None
-    plt.imshow(img, norm=norm, origin='lower') 
+        norm = norm
+    plt.imshow(img, norm=norm, origin='lower',cmap = my_cmap) 
     if colorbar == True:
         plt.colorbar()
     if savename is not None:
         plt.savefig(savename,bbox_inches='tight')
     if hold == False:
         plt.show()     
     # plt.imshow(img, norm=LogNorm(), cmap = 'gist_heat', origin='low')   
@@ -77,15 +84,15 @@
     rgb_default = make_lupton_rgb(imgs[0], imgs[1], imgs[2], **args)
     plt.imshow(rgb_default, origin='lower')
     if savename is not None:
         plt.savefig(savename,bbox_inches='tight')
     plt.show()
 
 def plt_many_fits(imgs, texts = None, prop = None, savename = None, labels = None, hide_axes = False,
-                  if_plot=True, cmap=None, label_size = 17):
+                  if_plot=True, cmap=None, label_size = 17, norm = LogNorm()):
     """
     Plot many fits in a row
     
     Parameter
     --------
         imgs: Input of a list of images to show
         texts: measured properties
@@ -100,15 +107,15 @@
         _row=2
     fig, (axs) = plt.subplots(_row, 5, figsize=(15, 3 + 3 * (_row-1)))
     import matplotlib as mat
     mat.rcParams['font.family'] = 'STIXGeneral'
     for i in range(len(imgs)):
         _i = int(i / 5)
         _j = int(i % 5)
-        axs[_i][_j].imshow(imgs[i], origin='lower', norm=LogNorm(), cmap=cmap)
+        axs[_i][_j].imshow(imgs[i], origin='lower', norm=norm, cmap=cmap)
         frame_size = len(imgs[i])
         if labels is None:
             label = "ini_ID = {0}".format(i)
         else:
             label = labels[i]
         plttext = axs[_i][_j].text(frame_size*0.05, frame_size*0.87, label,
                  fontsize=label_size, weight='bold', color='black')
```

### Comparing `galight-0.1.8/galight/tools/asymmetry_tools.py` & `galight-0.1.9/galight/tools/asymmetry_tools.py`

 * *Files 1% similar despite different names*

```diff
@@ -79,14 +79,15 @@
         r_SB_p = r_SB_list[0]
     except:
         r_p = r_grids[-1]
         r_SB_p = r_SB[-1]
         warnings.warn("Couldn't find the SB_annu/SB_rad below eta, and use the last annu instead...",
                       AstropyUserWarning)
     if if_plot == True:
+        print("Plot the measure of petrosian radius:")
         minorLocator = AutoMinorLocator()
         fig, ax = plt.subplots()
         plt.plot(r_grids, r_SB, 'x-', label = 'Ave SB in radius')
         plt.plot(r_grids, r_SB_annu, 'x--', label = 'SB in annuli')
         plt.scatter(r_p, r_SB_p*eta,s=100,c = 'r', marker='o',
                     label='Ave SB times eta ({0})'.format(eta))
         ax.xaxis.set_minor_locator(minorLocator)
@@ -148,25 +149,27 @@
             if True, use the pertrosian radius aperture as target segm map.
         
         rm_ps: bool.
             if True, the point source(s) in the image will be removed. 
         
     """
     def __init__(self, fitting_process_class, obj_id=0, interp_order=3, seg_cal_reg = 'or', 
-                 consider_petrosian=False, eta = 0.2, rm_ps = False, rm_model=False):
+                 consider_petrosian=False, eta = 0.2, rm_ps = False, rm_model=False, rm_obj=False):
         self.fitting_process_class = fitting_process_class
         self.interp_order = interp_order
         self.seg_cal_reg = seg_cal_reg
         self.obj_id = obj_id
         self.interp_order = interp_order
         self.img = copy.deepcopy(self.fitting_process_class.fitting_specify_class.kwargs_data['image_data'])
         if rm_ps == True:
             self.img -= np.sum(self.fitting_process_class.image_ps_list, axis = 0)
         elif rm_model == True:
             self.img = self.img - np.sum(self.fitting_process_class.image_ps_list, axis = 0) - np.sum(self.fitting_process_class.image_host_list, axis = 0)
+        if rm_obj == True:
+            self.img = self.img - np.sum(self.fitting_process_class.image_host_list[:obj_id] + self.fitting_process_class.image_host_list[obj_id+1:], axis = 0)
         self.consider_petrosian = consider_petrosian
         self.eta = eta
     def asy_segm(self, segm = None, mask_type = 'segm', extend=1.):
         """
         To produce the segmentation map and get the segm_id of the object for the measurement.
        
         Parameter
@@ -316,15 +319,15 @@
             bkg_asy = np.sum(bkg_asy_2d)
             self.bkg_asy_dens = bkg_asy/np.sum(self.light_masks) #The density of the background asymmetry.
         else:
             assert 0 < bkg_asy_dens < 1.0
             self.bkg_asy_dens = bkg_asy_dens
         if if_plot_bkg == True:
             print("Plot the region to estiamte the background asymmetry:")
-            plt_fits(bkg_asy_2d,norm='linear')
+            plt_fits(bkg_asy_2d,norm=None)
         return self.bkg_asy_dens
 
     def cal_asymmetry(self, rotate_pix, obj_flux = None, if_plot = True, bkg_asy_dens=None, if_plot_bkg = False):
         '''
         Parameters
         ----------
         rotate_pix : array
@@ -436,25 +439,26 @@
     """
     Inherit Measure_asy and calculate the other CAS parameters including smoothness, concentration and gini.
     """
     def __init__(self, fitting_process_class, **kwargs):
         Measure_asy.__init__(self, fitting_process_class=fitting_process_class, **kwargs)
 
     def cal_CAS(self, mask_type='segm', if_remeasure_bkg = False, bkg_asy_dens=None, skysmooth=None, extend=1, 
-                if_plot = False, if_plot_bkg=False, segm = None, if_residual=False, image_org=None):
+                if_plot = False, if_plot_bkg=False, segm = None, if_residual=False, image_org=None, radius=None):
         self.asy_segm(mask_type=mask_type, segm=segm, extend=extend)
         self.find_pos_res = self.find_pos()
         self.make_bkg(rotate_pix = self.find_pos_res["x"], if_remeasure_bkg=if_remeasure_bkg)
         obj_flux = None
         if if_residual == True and image_org is not None:
             obj_flux = np.sum(image_org[self.cal_areas == True])
         self.asy = self.cal_asymmetry(rotate_pix = self.find_pos_res["x"], bkg_asy_dens=bkg_asy_dens,
                                       if_plot=if_plot, if_plot_bkg=if_plot_bkg, obj_flux = obj_flux)
         segm_id = self.segm_id
-        radius = len(self.img)/2*0.95
+        if radius == None:
+            radius = len(self.img)/2*0.95
         center =  np.array([len(self.img)/2]*2) + self.find_pos_res["x"]
         self._mask = (self.segm == segm_id) +  (self.segm == 0)  #A mask for the object.
         
         try:
             q = self.fitting_process_class.final_result_galaxy[self.obj_id]['q']
             theta = - self.fitting_process_class.final_result_galaxy[self.obj_id]['phi_G']  #Galight and apr's theta is reversed.
             xc, yc = np.array(self.fitting_process_class.final_result_galaxy[self.obj_id]['position_xy']) + int(len(self.img)/2)
@@ -463,34 +467,34 @@
             q = apr.b/apr.a
             theta = apr.theta
             xc, yc = apr.positions
         if if_residual == False:
             self.r_p_c = cal_r_petrosian(self.img, center=center, eta=self.eta, mask= self._mask ,
                                     radius=radius, if_plot=if_plot)
             self.r_p_e = cal_r_petrosian(self.img, center=center, eta=self.eta, mask= self._mask,
-                                    radius=radius, q=q, theta = theta, if_plot=if_plot)
+                                    radius=radius, q=q, theta = theta, if_plot=False)
         if if_residual == True:
             if image_org is None:
                 image_org = copy.deepcopy(self.fitting_process_class.fitting_specify_class.kwargs_data['image_data'])
             self.image_org = image_org
             self.r_p_c = cal_r_petrosian(image_org, center=center, eta=self.eta, mask= self._mask ,
                                          radius=radius, if_plot=if_plot) 
             
             self.r_p_e = cal_r_petrosian(image_org, center=center, eta=self.eta, mask= self._mask,
-                                    radius=radius, q=q, theta = theta, if_plot=if_plot)
+                                    radius=radius, q=q, theta = theta, if_plot=False)
         
         
         skysmooth = self._skysmoothness(bkg=self.img_bkg,r_p_c=self.r_p_c,skysmooth=skysmooth)
         self.smoothness, self.S_flag = self.cal_smoothness(image= self.img,
                                     center=center, r_p_c=self.r_p_c,skysmooth=skysmooth, image_org= image_org,
                                     if_residual=if_residual)
 
         self.concentration = self.cal_concentration(image = self.img ,
                                                 mask = self._mask,
-                                                center=center, radius = radius,if_plot=if_plot)
+                                                center=center, radius = radius, if_plot=if_plot)
         self.gini = self.cal_gini(self.img * self.cal_areas, self.r_p_e, theta, q, xc, yc)
         return self.asy, self.smoothness, self.concentration, self.gini
 
 
     def cal_concentration(self, image, mask, center, radius, tot_flux=None, if_plot = False):
         from galight.tools.measure_tools import flux_profile
         seeding_num = np.min([int(radius*2), 100])
@@ -510,15 +514,15 @@
             plt.scatter(r_20, r_flux[r_grids==r_20],s=50,c = 'b', marker='o',
                         label='r20')
             ax.xaxis.set_minor_locator(minorLocator)
             plt.tick_params(which='both', width=2)
             plt.tick_params(which='major', length=7)
             plt.tick_params(which='minor', length=4, color='r')
             plt.grid()
-            ax.set_ylabel("Surface Brightness")
+            ax.set_ylabel("Fluxs inside")
             ax.set_xlabel("Pixels")
             plt.grid(which="minor")
             plt.legend()
             plt.show()
         C = 5.0 * np.log10(r_80/r_20)
         return C
```

### Comparing `galight-0.1.8/galight/tools/cutout_tools.py` & `galight-0.1.9/galight/tools/cutout_tools.py`

 * *Files identical despite different names*

### Comparing `galight-0.1.8/galight/tools/measure_tools.py` & `galight-0.1.9/galight/tools/measure_tools.py`

 * *Files 0% similar despite different names*

```diff
@@ -948,7 +948,25 @@
     plt.legend()
     if ifplot == True:
         plt.show()
     else:
         plt.close()
     return peak_loc, popt[2]
 
+
+def stack_PSF(data, psf_POS_list, psf_size = 71,  oversampling=1, maxiters=10, tool = 'photutils'):
+    if tool == 'photutils':
+        from astropy.table import Table
+        from astropy.nddata import NDData
+        from photutils.psf import extract_stars
+        from photutils import EPSFBuilder 
+        stars_tbl = Table()
+        stars_tbl['x'] = np.array(psf_POS_list)[:,0]
+        stars_tbl['y'] = np.array(psf_POS_list)[:,1]
+        nddata = NDData(data=data) 
+        #nddata = NDData(data=self.fov_image) 
+        stars = extract_stars(nddata, stars_tbl, size=psf_size)  
+        epsf_builder=EPSFBuilder(oversampling=oversampling, maxiters=maxiters,progress_bar=True,shape=psf_size)
+        epsf,fitted_stars=epsf_builder(stars)        
+        stack_psf = epsf.data
+        return stack_psf
+
```

### Comparing `galight-0.1.8/galight/tools/plot_tools.py` & `galight-0.1.9/galight/tools/plot_tools.py`

 * *Files identical despite different names*

### Comparing `galight-0.1.8/galight.egg-info/PKG-INFO` & `galight-0.1.9/galight.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: galight
-Version: 0.1.8
+Version: 0.1.9
 Summary: Galaxy light 2D modeling tool
 Home-page: https://github.com/dartoon/galight
 Author: Xuheng Ding
 Author-email: xuheng.ding@ipmu.jp
 License: MIT
 Keywords: galight
 Platform: UNKNOWN
```

### Comparing `galight-0.1.8/galight.egg-info/SOURCES.txt` & `galight-0.1.9/galight.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `galight-0.1.8/setup.py` & `galight-0.1.9/setup.py`

 * *Files 1% similar despite different names*

```diff
@@ -20,15 +20,15 @@
 -------------
 
 The full documentation is at http://galight.rtfd.org."""
 history = open('HISTORY.rst').read().replace('.. :changelog:', '')
 
 setup(
     name='galight',
-    version='0.1.8',
+    version='0.1.9',
     description='Galaxy light 2D modeling tool',
     long_description=readme,
     long_description_content_type='text/markdown',
     author='Xuheng Ding',
     author_email='xuheng.ding@ipmu.jp',
     url='https://github.com/dartoon/galight',
     packages=[
```

