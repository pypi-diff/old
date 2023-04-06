# Comparing `tmp/rw_noise-0.1.1.tar.gz` & `tmp/rw_noise-0.1.2.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "rw_noise-0.1.1.tar", last modified: Thu Aug 18 15:54:56 2022, max compression
+gzip compressed data, was "rw_noise-0.1.2.tar", last modified: Thu Apr  6 15:29:25 2023, max compression
```

## Comparing `rw_noise-0.1.1.tar` & `rw_noise-0.1.2.tar`

### file list

```diff
@@ -1,49 +1,49 @@
-drwxr-xr-x   0 dominik   (1000) dominik   (1000)        0 2022-08-18 15:54:56.593504 rw_noise-0.1.1/
--rw-r--r--   0 dominik   (1000) dominik   (1000)       96 2022-08-18 13:28:05.000000 rw_noise-0.1.1/.gitignore
--rw-r--r--   0 dominik   (1000) dominik   (1000)     2213 2022-08-18 14:56:52.000000 rw_noise-0.1.1/CMakeLists.txt
--rw-r--r--   0 dominik   (1000) dominik   (1000)     1070 2022-08-18 13:57:56.000000 rw_noise-0.1.1/LICENSE
--rw-r--r--   0 dominik   (1000) dominik   (1000)     4272 2022-08-18 15:54:56.593504 rw_noise-0.1.1/PKG-INFO
--rw-r--r--   0 dominik   (1000) dominik   (1000)     3569 2022-08-18 15:53:10.000000 rw_noise-0.1.1/Readme.md
--rw-r--r--   0 dominik   (1000) dominik   (1000)     1279 2022-08-18 12:34:43.000000 rw_noise-0.1.1/__init__.py
-drwxr-xr-x   0 dominik   (1000) dominik   (1000)        0 2022-08-18 15:54:56.590170 rw_noise-0.1.1/evaluation/
--rw-r--r--   0 dominik   (1000) dominik   (1000)     3833 2022-08-18 12:54:46.000000 rw_noise-0.1.1/evaluation/Readme.md
-drwxr-xr-x   0 dominik   (1000) dominik   (1000)        0 2022-08-18 15:54:56.590170 rw_noise-0.1.1/evaluation/artificial/
--rwxr-xr-x   0 dominik   (1000) dominik   (1000)     1213 2022-08-18 13:35:16.000000 rw_noise-0.1.1/evaluation/artificial/interactive_segmentation.py
-drwxr-xr-x   0 dominik   (1000) dominik   (1000)        0 2022-08-18 15:54:56.590170 rw_noise-0.1.1/evaluation/conversion_scripts/
--rw-r--r--   0 dominik   (1000) dominik   (1000)      746 2022-03-14 10:54:49.000000 rw_noise-0.1.1/evaluation/conversion_scripts/crop_FastMRI.py
--rw-r--r--   0 dominik   (1000) dominik   (1000)      391 2022-03-14 10:54:49.000000 rw_noise-0.1.1/evaluation/conversion_scripts/crop_Larvae.py
--rwxr-xr-x   0 dominik   (1000) dominik   (1000)     2038 2022-02-26 08:35:41.000000 rw_noise-0.1.1/evaluation/conversion_scripts/makemask_fim.py
--rwxr-xr-x   0 dominik   (1000) dominik   (1000)     1660 2022-03-07 10:39:48.000000 rw_noise-0.1.1/evaluation/conversion_scripts/makemask_mri.py
--rw-r--r--   0 dominik   (1000) dominik   (1000)     1005 2022-02-21 10:37:03.000000 rw_noise-0.1.1/evaluation/conversion_scripts/npy_to_png_slice.py
--rw-r--r--   0 dominik   (1000) dominik   (1000)     1117 2022-02-21 10:37:03.000000 rw_noise-0.1.1/evaluation/conversion_scripts/save_h5_npy_png.py
-drwxr-xr-x   0 dominik   (1000) dominik   (1000)        0 2022-08-18 15:54:56.590170 rw_noise-0.1.1/evaluation/fastmri/
--rw-r--r--   0 dominik   (1000) dominik   (1000)     2969 2022-03-09 11:16:00.000000 rw_noise-0.1.1/evaluation/fastmri/data.py
--rwxr-xr-x   0 dominik   (1000) dominik   (1000)     2316 2022-03-07 10:39:48.000000 rw_noise-0.1.1/evaluation/fastmri/illustration.py
--rwxr-xr-x   0 dominik   (1000) dominik   (1000)      806 2022-03-09 12:53:00.000000 rw_noise-0.1.1/evaluation/fastmri/interactive_segmentation.py
--rwxr-xr-x   0 dominik   (1000) dominik   (1000)     2466 2022-03-04 10:50:46.000000 rw_noise-0.1.1/evaluation/fastmri/run_evaluation.py
-drwxr-xr-x   0 dominik   (1000) dominik   (1000)        0 2022-08-18 15:54:56.590170 rw_noise-0.1.1/evaluation/fim/
--rw-r--r--   0 dominik   (1000) dominik   (1000)      995 2022-03-09 11:21:44.000000 rw_noise-0.1.1/evaluation/fim/data.py
--rwxr-xr-x   0 dominik   (1000) dominik   (1000)     1767 2022-08-17 13:15:45.000000 rw_noise-0.1.1/evaluation/fim/illustration.py
--rwxr-xr-x   0 dominik   (1000) dominik   (1000)     1913 2022-03-09 11:21:12.000000 rw_noise-0.1.1/evaluation/fim/run_evaluation.py
--rwxr-xr-x   0 dominik   (1000) dominik   (1000)    19583 2022-08-10 13:44:15.000000 rw_noise-0.1.1/evaluation/plot_results.py
-drwxr-xr-x   0 dominik   (1000) dominik   (1000)        0 2022-08-18 15:54:56.590170 rw_noise-0.1.1/evaluation/spiral/
--rw-r--r--   0 dominik   (1000) dominik   (1000)     1713 2022-03-02 17:21:21.000000 rw_noise-0.1.1/evaluation/spiral/data.py
--rwxr--r--   0 dominik   (1000) dominik   (1000)     2598 2022-03-03 11:03:57.000000 rw_noise-0.1.1/evaluation/spiral/illustration.py
--rwxr-xr-x   0 dominik   (1000) dominik   (1000)     4292 2022-03-02 17:21:10.000000 rw_noise-0.1.1/evaluation/spiral/run_evaluation.py
--rw-r--r--   0 dominik   (1000) dominik   (1000)    17702 2022-08-18 12:45:30.000000 rw_noise-0.1.1/evaluation/util.py
--rw-r--r--   0 dominik   (1000) dominik   (1000)      201 2022-08-18 14:23:29.000000 rw_noise-0.1.1/pyproject.toml
-drwxr-xr-x   0 dominik   (1000) dominik   (1000)        0 2022-08-18 15:54:56.593504 rw_noise-0.1.1/rw_noise.egg-info/
--rw-r--r--   0 dominik   (1000) dominik   (1000)     4272 2022-08-18 15:54:56.000000 rw_noise-0.1.1/rw_noise.egg-info/PKG-INFO
--rw-r--r--   0 dominik   (1000) dominik   (1000)     1031 2022-08-18 15:54:56.000000 rw_noise-0.1.1/rw_noise.egg-info/SOURCES.txt
--rw-r--r--   0 dominik   (1000) dominik   (1000)        1 2022-08-18 15:54:56.000000 rw_noise-0.1.1/rw_noise.egg-info/dependency_links.txt
--rw-r--r--   0 dominik   (1000) dominik   (1000)        9 2022-08-18 15:54:56.000000 rw_noise-0.1.1/rw_noise.egg-info/top_level.txt
--rw-r--r--   0 dominik   (1000) dominik   (1000)      706 2022-08-18 15:54:56.593504 rw_noise-0.1.1/setup.cfg
--rw-r--r--   0 dominik   (1000) dominik   (1000)      590 2022-08-18 15:21:15.000000 rw_noise-0.1.1/setup.py
-drwxr-xr-x   0 dominik   (1000) dominik   (1000)        0 2022-08-18 15:54:56.593504 rw_noise-0.1.1/src/
--rw-r--r--   0 dominik   (1000) dominik   (1000)     2455 2022-02-02 13:49:53.000000 rw_noise-0.1.1/src/imgs.cpp
--rw-r--r--   0 dominik   (1000) dominik   (1000)     4101 2022-08-10 13:42:42.000000 rw_noise-0.1.1/src/imgs.h
--rw-r--r--   0 dominik   (1000) dominik   (1000)     9871 2022-08-18 12:28:50.000000 rw_noise-0.1.1/src/lib.cpp
--rw-r--r--   0 dominik   (1000) dominik   (1000)    10135 2022-08-18 15:14:32.000000 rw_noise-0.1.1/src/rw.cpp
--rw-r--r--   0 dominik   (1000) dominik   (1000)      257 2022-02-26 08:35:41.000000 rw_noise-0.1.1/src/rw.h
--rw-r--r--   0 dominik   (1000) dominik   (1000)    10354 2022-03-08 15:02:00.000000 rw_noise-0.1.1/src/weights.cpp
--rw-r--r--   0 dominik   (1000) dominik   (1000)    14622 2022-03-08 15:01:35.000000 rw_noise-0.1.1/src/weights.h
+drwxr-xr-x   0 dominik   (1000) dominik   (1000)        0 2023-04-06 15:29:25.686570 rw_noise-0.1.2/
+-rw-r--r--   0 dominik   (1000) dominik   (1000)       96 2023-04-04 09:39:39.000000 rw_noise-0.1.2/.gitignore
+-rw-r--r--   0 dominik   (1000) dominik   (1000)     2213 2023-04-04 09:39:39.000000 rw_noise-0.1.2/CMakeLists.txt
+-rw-r--r--   0 dominik   (1000) dominik   (1000)     1070 2023-04-04 09:39:39.000000 rw_noise-0.1.2/LICENSE
+-rw-r--r--   0 dominik   (1000) dominik   (1000)     4273 2023-04-06 15:29:25.686570 rw_noise-0.1.2/PKG-INFO
+-rw-r--r--   0 dominik   (1000) dominik   (1000)     3570 2023-04-04 09:39:39.000000 rw_noise-0.1.2/Readme.md
+-rw-r--r--   0 dominik   (1000) dominik   (1000)     1502 2023-04-04 09:39:39.000000 rw_noise-0.1.2/__init__.py
+drwxr-xr-x   0 dominik   (1000) dominik   (1000)        0 2023-04-06 15:29:25.669903 rw_noise-0.1.2/evaluation/
+-rw-r--r--   0 dominik   (1000) dominik   (1000)     4089 2023-04-06 15:22:38.000000 rw_noise-0.1.2/evaluation/Readme.md
+drwxr-xr-x   0 dominik   (1000) dominik   (1000)        0 2023-04-06 15:29:25.669903 rw_noise-0.1.2/evaluation/artificial/
+-rwxr-xr-x   0 dominik   (1000) dominik   (1000)     1213 2023-04-04 09:39:39.000000 rw_noise-0.1.2/evaluation/artificial/interactive_segmentation.py
+drwxr-xr-x   0 dominik   (1000) dominik   (1000)        0 2023-04-06 15:29:25.669903 rw_noise-0.1.2/evaluation/conversion_scripts/
+-rw-r--r--   0 dominik   (1000) dominik   (1000)      746 2023-04-04 09:39:39.000000 rw_noise-0.1.2/evaluation/conversion_scripts/crop_FastMRI.py
+-rw-r--r--   0 dominik   (1000) dominik   (1000)      391 2023-04-04 09:39:39.000000 rw_noise-0.1.2/evaluation/conversion_scripts/crop_Larvae.py
+-rwxr-xr-x   0 dominik   (1000) dominik   (1000)     2038 2023-04-04 09:39:39.000000 rw_noise-0.1.2/evaluation/conversion_scripts/makemask_fim.py
+-rwxr-xr-x   0 dominik   (1000) dominik   (1000)     1660 2023-04-04 09:39:39.000000 rw_noise-0.1.2/evaluation/conversion_scripts/makemask_mri.py
+-rw-r--r--   0 dominik   (1000) dominik   (1000)     1005 2023-04-04 09:39:39.000000 rw_noise-0.1.2/evaluation/conversion_scripts/npy_to_png_slice.py
+-rw-r--r--   0 dominik   (1000) dominik   (1000)     1117 2023-04-04 09:39:39.000000 rw_noise-0.1.2/evaluation/conversion_scripts/save_h5_npy_png.py
+drwxr-xr-x   0 dominik   (1000) dominik   (1000)        0 2023-04-06 15:29:25.669903 rw_noise-0.1.2/evaluation/fastmri/
+-rw-r--r--   0 dominik   (1000) dominik   (1000)     2969 2023-04-04 09:39:39.000000 rw_noise-0.1.2/evaluation/fastmri/data.py
+-rwxr-xr-x   0 dominik   (1000) dominik   (1000)     2316 2023-04-04 09:39:39.000000 rw_noise-0.1.2/evaluation/fastmri/illustration.py
+-rwxr-xr-x   0 dominik   (1000) dominik   (1000)      806 2023-04-04 09:39:39.000000 rw_noise-0.1.2/evaluation/fastmri/interactive_segmentation.py
+-rwxr-xr-x   0 dominik   (1000) dominik   (1000)     2466 2023-04-04 09:39:39.000000 rw_noise-0.1.2/evaluation/fastmri/run_evaluation.py
+drwxr-xr-x   0 dominik   (1000) dominik   (1000)        0 2023-04-06 15:29:25.673236 rw_noise-0.1.2/evaluation/fim/
+-rw-r--r--   0 dominik   (1000) dominik   (1000)      995 2023-04-04 09:39:39.000000 rw_noise-0.1.2/evaluation/fim/data.py
+-rwxr-xr-x   0 dominik   (1000) dominik   (1000)     1767 2023-04-06 15:28:54.000000 rw_noise-0.1.2/evaluation/fim/illustration.py
+-rwxr-xr-x   0 dominik   (1000) dominik   (1000)     1913 2023-04-04 09:39:39.000000 rw_noise-0.1.2/evaluation/fim/run_evaluation.py
+-rwxr-xr-x   0 dominik   (1000) dominik   (1000)    19641 2023-04-06 15:28:54.000000 rw_noise-0.1.2/evaluation/plot_results.py
+drwxr-xr-x   0 dominik   (1000) dominik   (1000)        0 2023-04-06 15:29:25.683236 rw_noise-0.1.2/evaluation/spiral/
+-rw-r--r--   0 dominik   (1000) dominik   (1000)     1713 2023-04-04 09:39:39.000000 rw_noise-0.1.2/evaluation/spiral/data.py
+-rwxr-xr-x   0 dominik   (1000) dominik   (1000)     2598 2023-04-04 09:39:39.000000 rw_noise-0.1.2/evaluation/spiral/illustration.py
+-rwxr-xr-x   0 dominik   (1000) dominik   (1000)     4377 2023-04-04 09:39:39.000000 rw_noise-0.1.2/evaluation/spiral/run_evaluation.py
+-rw-r--r--   0 dominik   (1000) dominik   (1000)    18063 2023-04-06 15:28:54.000000 rw_noise-0.1.2/evaluation/util.py
+-rw-r--r--   0 dominik   (1000) dominik   (1000)      201 2023-04-04 09:39:39.000000 rw_noise-0.1.2/pyproject.toml
+drwxr-xr-x   0 dominik   (1000) dominik   (1000)        0 2023-04-06 15:29:25.683236 rw_noise-0.1.2/rw_noise.egg-info/
+-rw-r--r--   0 dominik   (1000) dominik   (1000)     4273 2023-04-06 15:29:25.000000 rw_noise-0.1.2/rw_noise.egg-info/PKG-INFO
+-rw-r--r--   0 dominik   (1000) dominik   (1000)     1031 2023-04-06 15:29:25.000000 rw_noise-0.1.2/rw_noise.egg-info/SOURCES.txt
+-rw-r--r--   0 dominik   (1000) dominik   (1000)        1 2023-04-06 15:29:25.000000 rw_noise-0.1.2/rw_noise.egg-info/dependency_links.txt
+-rw-r--r--   0 dominik   (1000) dominik   (1000)        9 2023-04-06 15:29:25.000000 rw_noise-0.1.2/rw_noise.egg-info/top_level.txt
+-rw-r--r--   0 dominik   (1000) dominik   (1000)      706 2023-04-06 15:29:25.686570 rw_noise-0.1.2/setup.cfg
+-rw-r--r--   0 dominik   (1000) dominik   (1000)      590 2023-04-04 09:39:39.000000 rw_noise-0.1.2/setup.py
+drwxr-xr-x   0 dominik   (1000) dominik   (1000)        0 2023-04-06 15:29:25.686570 rw_noise-0.1.2/src/
+-rw-r--r--   0 dominik   (1000) dominik   (1000)     2494 2023-04-06 15:16:32.000000 rw_noise-0.1.2/src/imgs.cpp
+-rw-r--r--   0 dominik   (1000) dominik   (1000)     4101 2023-04-04 09:39:39.000000 rw_noise-0.1.2/src/imgs.h
+-rw-r--r--   0 dominik   (1000) dominik   (1000)     9998 2023-04-04 09:39:39.000000 rw_noise-0.1.2/src/lib.cpp
+-rw-r--r--   0 dominik   (1000) dominik   (1000)    10135 2023-04-04 09:39:39.000000 rw_noise-0.1.2/src/rw.cpp
+-rw-r--r--   0 dominik   (1000) dominik   (1000)      257 2023-04-04 09:39:39.000000 rw_noise-0.1.2/src/rw.h
+-rw-r--r--   0 dominik   (1000) dominik   (1000)    15551 2023-04-06 15:15:52.000000 rw_noise-0.1.2/src/weights.cpp
+-rw-r--r--   0 dominik   (1000) dominik   (1000)    14956 2023-04-06 15:15:52.000000 rw_noise-0.1.2/src/weights.h
```

### Comparing `rw_noise-0.1.1/CMakeLists.txt` & `rw_noise-0.1.2/CMakeLists.txt`

 * *Files identical despite different names*

### Comparing `rw_noise-0.1.1/LICENSE` & `rw_noise-0.1.2/LICENSE`

 * *Files identical despite different names*

### Comparing `rw_noise-0.1.1/PKG-INFO` & `rw_noise-0.1.2/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: rw_noise
-Version: 0.1.1
+Version: 0.1.2
 Summary: A library for random walker image segmentation under known noise models
 Home-page: https://zivgitlab.uni-muenster.de/ag-pria/rw-noise-model
 Author: Dominik Drees
 Author-email: dominik.drees@uni-muenster.de
 License: MIT
 Keywords: random-walker image-segmentation noise-model
 Platform: any
@@ -48,14 +48,15 @@
 For weight definition, a method has to be supplied which can be constructed via the following functions:
  * `fixed` (Grady [1]) 
  * `global_gaussian_bian` (Bian et al. [2])
  * `ttest` (Bian et al. [3])
  * `poisson` (Drees et al. [4]),
  * `variable_gaussian` (Drees et al. [4]),
  * `global_gaussian` (Drees et al. [4]),
+
 Of those, only `fixed` and `global_gaussian` are suitable for non-scalar pixel data.
 
 A minimal example program using the library could look like the following:
 ```python
 import rw_noise as rw
 import numpy as np
 import matplotlib.pyplot as plt
```

### Comparing `rw_noise-0.1.1/Readme.md` & `rw_noise-0.1.2/Readme.md`

 * *Files 2% similar despite different names*

```diff
@@ -29,14 +29,15 @@
 For weight definition, a method has to be supplied which can be constructed via the following functions:
  * `fixed` (Grady [1]) 
  * `global_gaussian_bian` (Bian et al. [2])
  * `ttest` (Bian et al. [3])
  * `poisson` (Drees et al. [4]),
  * `variable_gaussian` (Drees et al. [4]),
  * `global_gaussian` (Drees et al. [4]),
+
 Of those, only `fixed` and `global_gaussian` are suitable for non-scalar pixel data.
 
 A minimal example program using the library could look like the following:
 ```python
 import rw_noise as rw
 import numpy as np
 import matplotlib.pyplot as plt
```

### Comparing `rw_noise-0.1.1/__init__.py` & `rw_noise-0.1.2/__init__.py`

 * *Files 2% similar despite different names*

```diff
@@ -13,14 +13,21 @@
 def poisson(filter_extent, search_extent=None):
     if search_extent is None:
         search_extent = filter_extent
     return {"name": "poisson",
             "search_extent": search_extent, "filter_extent": filter_extent}
 
 
+def loupas(filter_extent, search_extent=None):
+    if search_extent is None:
+        search_extent = filter_extent
+    return {"name": "loupas",
+            "search_extent": search_extent, "filter_extent": filter_extent}
+
+
 def ttest(filter_extent, search_extent=None):
     if search_extent is None:
         search_extent = filter_extent
     return {"name": "ttest",
             "search_extent": search_extent, "filter_extent": filter_extent}
```

### Comparing `rw_noise-0.1.1/evaluation/Readme.md` & `rw_noise-0.1.2/evaluation/Readme.md`

 * *Files 10% similar despite different names*

```diff
@@ -51,7 +51,11 @@
 
 # Plotting Quantitative Results
 
 You can use the script `plot_results.py` to generate the plots of quantitative results also shown in the paper.
 The script assumes that the respective `result.csv` reside in the folders `spiral`, `fim` and `fastmri`.
 This happens automatically if you execute the `run_evaluation.py` scripts within those directories.
 You can then just execute the script `plot_results.py` and optionally add a path to a folder as an argument to export the figures to files.
+
+# Note! Updates since the publication of the original paper
+
+Since the publication, an error in the calculation of region variances has been noticed and fixed. The results produced with versions `>= 0.1.2` will thus not reflect the paper results exactly.
```

### Comparing `rw_noise-0.1.1/evaluation/artificial/interactive_segmentation.py` & `rw_noise-0.1.2/evaluation/artificial/interactive_segmentation.py`

 * *Files identical despite different names*

### Comparing `rw_noise-0.1.1/evaluation/conversion_scripts/crop_FastMRI.py` & `rw_noise-0.1.2/evaluation/conversion_scripts/crop_FastMRI.py`

 * *Files identical despite different names*

### Comparing `rw_noise-0.1.1/evaluation/conversion_scripts/makemask_fim.py` & `rw_noise-0.1.2/evaluation/conversion_scripts/makemask_fim.py`

 * *Files identical despite different names*

### Comparing `rw_noise-0.1.1/evaluation/conversion_scripts/makemask_mri.py` & `rw_noise-0.1.2/evaluation/conversion_scripts/makemask_mri.py`

 * *Files identical despite different names*

### Comparing `rw_noise-0.1.1/evaluation/conversion_scripts/npy_to_png_slice.py` & `rw_noise-0.1.2/evaluation/conversion_scripts/npy_to_png_slice.py`

 * *Files identical despite different names*

### Comparing `rw_noise-0.1.1/evaluation/conversion_scripts/save_h5_npy_png.py` & `rw_noise-0.1.2/evaluation/conversion_scripts/save_h5_npy_png.py`

 * *Files identical despite different names*

### Comparing `rw_noise-0.1.1/evaluation/fastmri/data.py` & `rw_noise-0.1.2/evaluation/fastmri/data.py`

 * *Files identical despite different names*

### Comparing `rw_noise-0.1.1/evaluation/fastmri/illustration.py` & `rw_noise-0.1.2/evaluation/fastmri/illustration.py`

 * *Files identical despite different names*

### Comparing `rw_noise-0.1.1/evaluation/fastmri/interactive_segmentation.py` & `rw_noise-0.1.2/evaluation/fastmri/interactive_segmentation.py`

 * *Files identical despite different names*

### Comparing `rw_noise-0.1.1/evaluation/fastmri/run_evaluation.py` & `rw_noise-0.1.2/evaluation/fastmri/run_evaluation.py`

 * *Files identical despite different names*

### Comparing `rw_noise-0.1.1/evaluation/fim/data.py` & `rw_noise-0.1.2/evaluation/fim/data.py`

 * *Files identical despite different names*

### Comparing `rw_noise-0.1.1/evaluation/fim/illustration.py` & `rw_noise-0.1.2/evaluation/fim/illustration.py`

 * *Files identical despite different names*

### Comparing `rw_noise-0.1.1/evaluation/fim/run_evaluation.py` & `rw_noise-0.1.2/evaluation/fim/run_evaluation.py`

 * *Files identical despite different names*

### Comparing `rw_noise-0.1.1/evaluation/plot_results.py` & `rw_noise-0.1.2/evaluation/plot_results.py`

 * *Files 1% similar despite different names*

```diff
@@ -107,14 +107,16 @@
     elif "global_gaussian" in name:
         if "bian" in name or "ang" in name:
             base = "Bian [4] (Gaussian, const. $\\sigma$)"
         else:
             base = "Ours (Gaussian, const. $\\sigma$)"
     elif "poisson" in name:
         base = "Ours (Poisson)"
+    elif "loupas" in name:
+        base = "Ours (Loupas)"
     elif "ttest" in name:
         base = "Bian [5] (Gaussian, var. $\\sigma$)"
 
     if "scalar" in name:
         base += " $||\cdot||_2$"
     return base
```

### Comparing `rw_noise-0.1.1/evaluation/spiral/data.py` & `rw_noise-0.1.2/evaluation/spiral/data.py`

 * *Files identical despite different names*

### Comparing `rw_noise-0.1.1/evaluation/spiral/illustration.py` & `rw_noise-0.1.2/evaluation/spiral/illustration.py`

 * *Files identical despite different names*

### Comparing `rw_noise-0.1.1/evaluation/spiral/run_evaluation.py` & `rw_noise-0.1.2/evaluation/spiral/run_evaluation.py`

 * *Files 3% similar despite different names*

```diff
@@ -28,14 +28,15 @@
 
 num_tries = 100
 for i in range(num_tries):
     random_seed = i
 
     methods_poisson = [
             util.poisson(2),
+            util.loupas(2),
             util.ttest(2),
             util.global_gaussian(2),
             util.global_gaussian_bian(2),
             util.variable_gaussian(2),
             ]
     for beta in util.gen_betas(-3, 5, 5):
         methods_poisson.append(util.fixed(beta))
@@ -51,14 +52,16 @@
             img = np.random.poisson(img)
             return img.astype(np.float32)
 
         for method in methods_poisson:
             configurations.append(("poisson", noise_param, method, data_fn, random_seed))
 
     methods_loupas = [
+            util.loupas(2),
+            util.poisson(2),
             util.ttest(2),
             util.global_gaussian(2),
             util.global_gaussian_bian(2),
             util.variable_gaussian(2),
             ]
     for beta in util.gen_betas(-3, 5, 5):
         methods_loupas.append(util.fixed(beta))
```

### Comparing `rw_noise-0.1.1/evaluation/util.py` & `rw_noise-0.1.2/evaluation/util.py`

 * *Files 2% similar despite different names*

```diff
@@ -2,17 +2,27 @@
 import pygame
 import time
 import math
 import scipy.ndimage
 import scipy.spatial
 import sklearn.metrics
 import matplotlib.pyplot as plt
+
 # Note: you first have to build and install the package in the repository root!
+
+# If you do not want to install, or for local development uncomment the
+# following lines to directly use the files in the repository. The shared
+# library has to be located in a subfolder "lib".
+
+#import sys
+#from os import path
+#project_folder_path = path.join(path.dirname(path.abspath(__file__)), "..", "..")
+#sys.path.append(project_folder_path)
 import rw_noise
-from rw_noise import fixed, poisson, ttest, global_gaussian_bian, global_gaussian, variable_gaussian
+from rw_noise import fixed, poisson, ttest, global_gaussian_bian, global_gaussian, variable_gaussian, loupas
 
 run_rw_with_weights = rw_noise.solve
 rw_weights = rw_noise.weights
 run_rw = rw_noise.run
 
 show_nd_as_color = False
```

### Comparing `rw_noise-0.1.1/rw_noise.egg-info/PKG-INFO` & `rw_noise-0.1.2/rw_noise.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: rw-noise
-Version: 0.1.1
+Version: 0.1.2
 Summary: A library for random walker image segmentation under known noise models
 Home-page: https://zivgitlab.uni-muenster.de/ag-pria/rw-noise-model
 Author: Dominik Drees
 Author-email: dominik.drees@uni-muenster.de
 License: MIT
 Keywords: random-walker image-segmentation noise-model
 Platform: any
@@ -48,14 +48,15 @@
 For weight definition, a method has to be supplied which can be constructed via the following functions:
  * `fixed` (Grady [1]) 
  * `global_gaussian_bian` (Bian et al. [2])
  * `ttest` (Bian et al. [3])
  * `poisson` (Drees et al. [4]),
  * `variable_gaussian` (Drees et al. [4]),
  * `global_gaussian` (Drees et al. [4]),
+
 Of those, only `fixed` and `global_gaussian` are suitable for non-scalar pixel data.
 
 A minimal example program using the library could look like the following:
 ```python
 import rw_noise as rw
 import numpy as np
 import matplotlib.pyplot as plt
```

### Comparing `rw_noise-0.1.1/rw_noise.egg-info/SOURCES.txt` & `rw_noise-0.1.2/rw_noise.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `rw_noise-0.1.1/setup.cfg` & `rw_noise-0.1.2/setup.cfg`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 [metadata]
 name = rw_noise
-version = 0.1.1
+version = 0.1.2
 description = A library for random walker image segmentation under known noise models
 long_description = file: Readme.md
 long_description_content_type = text/markdown
 author = Dominik Drees
 author_email = dominik.drees@uni-muenster.de
 license = MIT
 platforms = any
```

### Comparing `rw_noise-0.1.1/setup.py` & `rw_noise-0.1.2/setup.py`

 * *Files identical despite different names*

### Comparing `rw_noise-0.1.1/src/imgs.cpp` & `rw_noise-0.1.2/src/imgs.cpp`

 * *Files 2% similar despite different names*

```diff
@@ -59,17 +59,18 @@
             int xbegin = std::max(0, xbase - wExtent);
             int ybegin = std::max(0, ybase - hExtent);
 
             int xend = std::min(static_cast<int>(cols), xbase+1 + wExtent);
             int yend = std::min(static_cast<int>(rows), ybase+1 + hExtent);
 
             float sum = 0.0f;
+            float mean = means(ybase,xbase)[0];
             for(int y = ybegin; y < yend; ++y) {
                 for(int x = xbegin; x < xend; ++x) {
-                    float diff = means(y,x)[0] - img(y,x)[0];
+                    float diff = mean - img(y,x)[0];
                     sum += diff*diff;
                 }
             }
             float num = (xend-xbegin)*(yend-ybegin);
             var(ybase,xbase) = Pixel<float, 1>{sum/(num-1)};
         }
     }
```

### Comparing `rw_noise-0.1.1/src/imgs.h` & `rw_noise-0.1.2/src/imgs.h`

 * *Files identical despite different names*

### Comparing `rw_noise-0.1.1/src/lib.cpp` & `rw_noise-0.1.2/src/lib.cpp`

 * *Files 2% similar despite different names*

```diff
@@ -145,14 +145,16 @@
             return std::make_unique<TTestParameter>(img, search_extent, filter_extent);
         } else if(name == "global_gaussian") {
             return std::make_unique<GlobalGaussianParameterGeneric<1>>(img, search_extent, filter_extent);
         } else if(name == "variable_gaussian") {
             return std::make_unique<VariableGaussianParameter>(img, search_extent, filter_extent);
         } else if(name == "poisson") {
             return std::make_unique<PoissonParameter>(img, search_extent, filter_extent);
+        } else if(name == "loupas") {
+            return std::make_unique<LoupasParameter>(img, search_extent, filter_extent);
         }
     }
     std::stringstream s;
     s << "Unknown method name '";
     s << name;
     s << "'";
     throw RWException(s.str());
```

### Comparing `rw_noise-0.1.1/src/rw.cpp` & `rw_noise-0.1.2/src/rw.cpp`

 * *Files identical despite different names*

### Comparing `rw_noise-0.1.1/src/weights.cpp` & `rw_noise-0.1.2/src/weights.cpp`

 * *Files 26% similar despite different names*

```diff
@@ -1,14 +1,17 @@
 #include "weights.h"
 
 #include <random>
 #include <algorithm>
 #include <cmath>
 #include <numeric>
 
+#include <boost/math/quadrature/tanh_sinh.hpp>
+#include <boost/math/special_functions/pow.hpp>
+
 template<int N>
 static std::pair<Pixel<float, N>,Pixel<float, N>> sample_aggregate_neighborhood(const Image<float, N>& aggregateHorizontal, const Image<float, N>& aggregateVertical, Eigen::Vector2i p1, Eigen::Vector2i p2, int filter_size_parallel, int filter_size_orthogonal) {
     Eigen::Vector2i p1sum;
     Eigen::Vector2i p2sum;
     const Image<float,N>* sum;
     if(p1[0] == p2[0]) {
         // horizontal case, i.e.:
@@ -158,14 +161,149 @@
         float exponent = -lambda[0] + std::log(lambda[0]) * sample[0] - std::lgamma(sample[0] + 1);
         return std::exp(exponent);
     };
 
     return dynamic_neighborhood_similarity(poissonSimilarity, probForParamsGivenSample, img, estimatedParams, search_extent, filter_extent, p1, p2);
 }
 
+LoupasParameter::LoupasParameter(const Image<float, 1>& img, int search_extent, int filter_extent)
+    : img(img)
+    , estimatedParams()
+    , filter_extent(filter_extent)
+    , search_extent(search_extent)
+    , sigma2()
+{
+    Image<float, 1> mean = meanFilterClamped(img, filter_extent, filter_extent);
+    Image<float, 1> variance = variances(img, mean, filter_extent, filter_extent);
+
+    //Eigen::Matrix<float, Eigen::Dynamic, Eigen::Dynamic> sigma2s = variance.binaryExpr(mean, [](Pixel<float,1> v, Pixel<float,1> m){ return v[0]/m[0]; });
+    //sigma2 = sigma2s.mean();
+
+    int rows = img.rows();
+    int cols = img.cols();
+    std::vector<float> vals;
+    for(int y = 0; y < rows; ++y) {
+        for(int x = 0; x < cols; ++x) {
+            vals.push_back(variance(y,x)[0] / mean(y,x)[0]);
+        }
+    }
+    size_t mid = vals.size()/2;
+    std::nth_element(vals.begin(), vals.begin()+mid, vals.end());
+    float median = vals[mid];
+    //TODO: good results seem to be REALLY dependent on good parameter estimation... is there a better way?
+    sigma2 = median;
+
+    // TODO maybe a median filter would also make sense here?
+    // it seems to produce really bad results, though...
+    estimatedParams = mean;
+}
+
+// The integral-part of the expression for the modified bessel function of 2nd order (K_v(x))
+// References:
+// https://math.stackexchange.com/questions/1960778/approximating-the-log-of-the-modified-bessel-function-of-the-second-kind
+// https://onlinelibrary.wiley.com/templates/jsp/_ux3/_acropolis/_pericles/pdf-viewer/web/viewer.html?file=/doi/pdfdirect/10.1002/cnm.972
+static double bessel_K_integral_log(double v, double x) {
+    // double seems to be fine here, float does not have enough exponent bits.
+    // long double also works, but requires considerably more computation time
+    typedef double Float;
+    if (v==0.5f) {
+        return 0.0f;
+    }
+    v = std::abs(v);
+    assert(v < 50); //Loupas method becomes numerically unstable for too large neighborhood sizes. :(
+    constexpr size_t n = 8;
+    Float beta = (2*n) / (2.0f * v + 1.0f);
+
+    Float v_minus_05 = v-0.5;
+    Float v_exp_2 = -2.0 * v -1.0;
+
+    Float error;
+    Float L1;
+    size_t levels;
+    //Float termination = 0.01;
+    Float termination = std::sqrt(std::numeric_limits<Float>::epsilon());
+
+    boost::math::quadrature::tanh_sinh<Float> integrator;
+    Float res = integrator.integrate([&](const Float u) {
+        auto u_power_beta = std::pow(u, beta);
+        auto first = beta * std::exp(-u_power_beta) * std::pow(2.0 * x + u_power_beta, v_minus_05) * boost::math::pow<n-1>(u);
+        auto second = std::exp(-1.0 / u);
+        if (second > 0) {
+            second *= std::pow(u, v_exp_2) * std::pow(2 * x * u + 1, v_minus_05);
+        }
+        return first + second;
+    }, 0.0, 1.0, termination, &error, &L1, &levels);
+
+    return std::log(res);
+}
+
+
+float LoupasParameter::weight(Eigen::Vector2i p1, Eigen::Vector2i p2) const {
+    auto similarity = [this] (const Image<float, 1>& img, std::vector<Eigen::Vector2i> neighborhood1, std::vector<Eigen::Vector2i> neighborhood2) {
+        if(neighborhood1.size() > neighborhood2.size()) {
+            neighborhood1.resize(neighborhood2.size());
+        } else if(neighborhood1.size() < neighborhood2.size()) {
+            neighborhood2.resize(neighborhood1.size());
+        }
+        assert(neighborhood1.size() == neighborhood2.size());
+
+        auto sum_sq = [&] (const std::vector<Eigen::Vector2i>& vals) -> float {
+            float sum = 0.0f;
+            for(const auto& p : vals) {
+                float s = sample<float, 1>(img, p)[0];
+                sum += s*s;
+            }
+            return sum;
+        };
+        float n = neighborhood1.size();
+        float v = (-n*0.5+1);
+
+        float Ex2 = sum_sq(neighborhood1)/n;
+        float Ey2 = sum_sq(neighborhood2)/n;
+        float Ez2 = (Ex2 + Ey2)*0.5f;
+
+        float nfactor = n/(2.0f*sigma2);
+        float expf1 = nfactor * ((std::sqrt(Ex2) + std::sqrt(Ey2))*0.5f - std::sqrt(Ez2));
+
+        float dx = std::sqrt(Ex2) * nfactor;
+        float dy = std::sqrt(Ey2) * nfactor;
+        float dz = std::sqrt(Ez2) * nfactor;
+
+        double intx_log = bessel_K_integral_log(v, dx);
+        double inty_log = bessel_K_integral_log(v, dy);
+        double intz_log = bessel_K_integral_log(v, dz);
+
+        double expf2 = intz_log - (intx_log + inty_log)*0.5f;
+
+        double w = std::exp(expf1 + expf2);
+
+        //w = std::min(w, 1.0f);
+        assert(!std::isnan(w) && std::isfinite(w) && 0 <= w && w <= 1.1);
+
+        return w;
+    };
+
+    auto probForParamsGivenSample = [this] (Pixel<float, 1> mu_p, Pixel<float, 1> sample_p) -> float {
+        float mu = mu_p[0];
+        float sample = sample_p[0];
+        auto diff = mu-sample;
+        auto diffSq = diff*diff;
+
+        float e = std::exp(-diffSq/(2*mu*sigma2));
+        float f = 1/std::sqrt(2.0f * M_PI * mu * sigma2);
+
+        float w = f*e;
+
+        return w;
+    };
+
+    return dynamic_neighborhood_similarity(similarity, probForParamsGivenSample, img, estimatedParams, search_extent, filter_extent, p1, p2);
+}
+
+
 TTestParameter::TTestParameter(const Image<float, 1>& img, int search_extent, int filter_extent)
     : img(img)
     , estimatedParams(img.rows(), img.cols())
     , search_extent(search_extent)
     , filter_extent(filter_extent)
 {
     Image<float, 1> mean = meanFilterClamped(img, filter_extent, filter_extent);
```

### Comparing `rw_noise-0.1.1/src/weights.h` & `rw_noise-0.1.2/src/weights.h`

 * *Files 1% similar despite different names*

```diff
@@ -71,14 +71,25 @@
     int filter_extent;
     int search_extent;
 
     PoissonParameter(const Image<float, 1>& img, int search_extent, int filter_extent);
     float weight(Eigen::Vector2i p1, Eigen::Vector2i p2) const;
 };
 
+struct LoupasParameter : public Parameters {
+    const Image<float, 1>& img;
+    Image<float, 1> estimatedParams;
+    int filter_extent;
+    int search_extent;
+    float sigma2;
+
+    LoupasParameter(const Image<float, 1>& img, int search_extent, int filter_extent);
+    float weight(Eigen::Vector2i p1, Eigen::Vector2i p2) const;
+};
+
 /// ----------------------------------------------------------------------------
 /// Implementation -------------------------------------------------------------
 /// ----------------------------------------------------------------------------
 
 inline long linear_order(const Eigen::Vector2i& p) {
     return long(p(1)) + (long(p(0)) << 32);
 }
```

