# Comparing `tmp/lumos-sat-1.0.0.tar.gz` & `tmp/lumos-sat-1.0.1.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "lumos-sat-1.0.0.tar", last modified: Thu Apr  6 20:12:40 2023, max compression
+gzip compressed data, was "lumos-sat-1.0.1.tar", last modified: Thu Apr  6 21:43:48 2023, max compression
```

## Comparing `lumos-sat-1.0.0.tar` & `lumos-sat-1.0.1.tar`

### file list

```diff
@@ -1,32 +1,35 @@
-drwxrwxrwx   0        0        0        0 2023-04-06 20:12:40.716459 lumos-sat-1.0.0/
--rw-rw-rw-   0        0        0     1096 2023-04-06 18:33:06.000000 lumos-sat-1.0.0/LICENSE
--rw-rw-rw-   0        0        0      834 2023-04-06 20:12:40.715463 lumos-sat-1.0.0/PKG-INFO
--rw-rw-rw-   0        0        0      577 2023-04-06 19:37:58.000000 lumos-sat-1.0.0/README.md
-drwxrwxrwx   0        0        0        0 2023-04-06 20:12:40.664598 lumos-sat-1.0.0/lumos/
--rw-rw-rw-   0        0        0        0 2023-04-06 18:42:57.000000 lumos-sat-1.0.0/lumos/__init__.py
-drwxrwxrwx   0        0        0        0 2023-04-06 20:12:40.672577 lumos-sat-1.0.0/lumos/brdf/
--rw-rw-rw-   0        0        0        0 2023-04-06 18:51:47.000000 lumos-sat-1.0.0/lumos/brdf/__init__.py
--rw-rw-rw-   0        0        0     2167 2023-04-06 19:00:07.000000 lumos-sat-1.0.0/lumos/brdf/fit_tools.py
--rw-rw-rw-   0        0        0     6493 2023-04-06 19:00:39.000000 lumos-sat-1.0.0/lumos/brdf/library.py
-drwxrwxrwx   0        0        0        0 2023-04-06 20:12:40.679558 lumos-sat-1.0.0/lumos/calculators/
--rw-rw-rw-   0        0        0        0 2023-04-06 18:51:54.000000 lumos-sat-1.0.0/lumos/calculators/__init__.py
--rw-rw-rw-   0        0        0     7743 2023-04-06 18:53:33.000000 lumos-sat-1.0.0/lumos/calculators/brightness_frame.py
--rw-rw-rw-   0        0        0     5378 2023-04-06 18:59:29.000000 lumos-sat-1.0.0/lumos/calculators/ground_frame.py
--rw-rw-rw-   0        0        0      207 2023-04-06 18:47:24.000000 lumos-sat-1.0.0/lumos/constants.py
--rw-rw-rw-   0        0        0     2320 2023-04-06 19:08:51.000000 lumos-sat-1.0.0/lumos/conversions.py
--rw-rw-rw-   0        0        0     2745 2023-04-06 18:49:01.000000 lumos-sat-1.0.0/lumos/functions.py
--rw-rw-rw-   0        0        0     3493 2023-04-06 18:49:21.000000 lumos-sat-1.0.0/lumos/geometry.py
-drwxrwxrwx   0        0        0        0 2023-04-06 20:12:40.690530 lumos-sat-1.0.0/lumos/plot/
--rw-rw-rw-   0        0        0        0 2023-03-10 18:54:08.000000 lumos-sat-1.0.0/lumos/plot/__init__.py
--rw-rw-rw-   0        0        0     1554 2023-04-06 19:19:50.000000 lumos-sat-1.0.0/lumos/plot/brdf.py
--rw-rw-rw-   0        0        0     3182 2023-03-14 05:45:11.000000 lumos-sat-1.0.0/lumos/plot/brightness_frame.py
--rw-rw-rw-   0        0        0     8227 2023-04-06 19:04:28.000000 lumos-sat-1.0.0/lumos/plot/ground_frame.py
--rw-rw-rw-   0        0        0      524 2023-04-06 19:30:32.000000 lumos-sat-1.0.0/lumos/video_tools.py
-drwxrwxrwx   0        0        0        0 2023-04-06 20:12:40.713468 lumos-sat-1.0.0/lumos_sat.egg-info/
--rw-rw-rw-   0        0        0      834 2023-04-06 20:12:40.000000 lumos-sat-1.0.0/lumos_sat.egg-info/PKG-INFO
--rw-rw-rw-   0        0        0      583 2023-04-06 20:12:40.000000 lumos-sat-1.0.0/lumos_sat.egg-info/SOURCES.txt
--rw-rw-rw-   0        0        0        1 2023-04-06 20:12:40.000000 lumos-sat-1.0.0/lumos_sat.egg-info/dependency_links.txt
--rw-rw-rw-   0        0        0      220 2023-04-06 20:12:40.000000 lumos-sat-1.0.0/lumos_sat.egg-info/requires.txt
--rw-rw-rw-   0        0        0        6 2023-04-06 20:12:40.000000 lumos-sat-1.0.0/lumos_sat.egg-info/top_level.txt
--rw-rw-rw-   0        0        0      588 2023-04-06 20:11:39.000000 lumos-sat-1.0.0/pyproject.toml
--rw-rw-rw-   0        0        0       42 2023-04-06 20:12:40.717457 lumos-sat-1.0.0/setup.cfg
+drwxrwxrwx   0        0        0        0 2023-04-06 21:43:48.525725 lumos-sat-1.0.1/
+-rw-rw-rw-   0        0        0     1096 2023-04-06 18:33:06.000000 lumos-sat-1.0.1/LICENSE
+-rw-rw-rw-   0        0        0       86 2023-04-06 21:38:28.000000 lumos-sat-1.0.1/MANIFEST.in
+-rw-rw-rw-   0        0        0      834 2023-04-06 21:43:48.522734 lumos-sat-1.0.1/PKG-INFO
+-rw-rw-rw-   0        0        0      577 2023-04-06 19:37:58.000000 lumos-sat-1.0.1/README.md
+drwxrwxrwx   0        0        0        0 2023-04-06 21:43:48.462893 lumos-sat-1.0.1/lumos/
+-rw-rw-rw-   0        0        0        0 2023-04-06 18:42:57.000000 lumos-sat-1.0.1/lumos/__init__.py
+drwxrwxrwx   0        0        0        0 2023-04-06 21:43:48.475861 lumos-sat-1.0.1/lumos/brdf/
+-rw-rw-rw-   0        0        0        0 2023-04-06 18:51:47.000000 lumos-sat-1.0.1/lumos/brdf/__init__.py
+-rw-rw-rw-   0        0        0     2167 2023-04-06 19:00:07.000000 lumos-sat-1.0.1/lumos/brdf/fit_tools.py
+-rw-rw-rw-   0        0        0     6493 2023-04-06 19:00:39.000000 lumos-sat-1.0.1/lumos/brdf/library.py
+drwxrwxrwx   0        0        0        0 2023-04-06 21:43:48.481842 lumos-sat-1.0.1/lumos/calculators/
+-rw-rw-rw-   0        0        0        0 2023-04-06 18:51:54.000000 lumos-sat-1.0.1/lumos/calculators/__init__.py
+-rw-rw-rw-   0        0        0     7743 2023-04-06 18:53:33.000000 lumos-sat-1.0.1/lumos/calculators/brightness_frame.py
+-rw-rw-rw-   0        0        0     5378 2023-04-06 18:59:29.000000 lumos-sat-1.0.1/lumos/calculators/ground_frame.py
+-rw-rw-rw-   0        0        0      207 2023-04-06 18:47:24.000000 lumos-sat-1.0.1/lumos/constants.py
+-rw-rw-rw-   0        0        0     2320 2023-04-06 19:08:51.000000 lumos-sat-1.0.1/lumos/conversions.py
+-rw-rw-rw-   0        0        0     2745 2023-04-06 18:49:01.000000 lumos-sat-1.0.1/lumos/functions.py
+-rw-rw-rw-   0        0        0     3493 2023-04-06 18:49:21.000000 lumos-sat-1.0.1/lumos/geometry.py
+drwxrwxrwx   0        0        0        0 2023-04-06 21:43:48.498796 lumos-sat-1.0.1/lumos/plot/
+-rw-rw-rw-   0        0        0        0 2023-03-10 18:54:08.000000 lumos-sat-1.0.1/lumos/plot/__init__.py
+-rw-rw-rw-   0        0        0     1554 2023-04-06 19:19:50.000000 lumos-sat-1.0.1/lumos/plot/brdf.py
+-rw-rw-rw-   0        0        0      213 2023-03-12 20:06:33.000000 lumos-sat-1.0.1/lumos/plot/brightness_frame.mplstyle
+-rw-rw-rw-   0        0        0     3182 2023-03-14 05:45:11.000000 lumos-sat-1.0.1/lumos/plot/brightness_frame.py
+-rw-rw-rw-   0        0        0      421 2023-03-14 05:45:11.000000 lumos-sat-1.0.1/lumos/plot/ground_frame.mplstyle
+-rw-rw-rw-   0        0        0     8227 2023-04-06 19:04:28.000000 lumos-sat-1.0.1/lumos/plot/ground_frame.py
+-rw-rw-rw-   0        0        0      524 2023-04-06 19:30:32.000000 lumos-sat-1.0.1/lumos/video_tools.py
+drwxrwxrwx   0        0        0        0 2023-04-06 21:43:48.518745 lumos-sat-1.0.1/lumos_sat.egg-info/
+-rw-rw-rw-   0        0        0      834 2023-04-06 21:43:48.000000 lumos-sat-1.0.1/lumos_sat.egg-info/PKG-INFO
+-rw-rw-rw-   0        0        0      665 2023-04-06 21:43:48.000000 lumos-sat-1.0.1/lumos_sat.egg-info/SOURCES.txt
+-rw-rw-rw-   0        0        0        1 2023-04-06 21:43:48.000000 lumos-sat-1.0.1/lumos_sat.egg-info/dependency_links.txt
+-rw-rw-rw-   0        0        0      220 2023-04-06 21:43:48.000000 lumos-sat-1.0.1/lumos_sat.egg-info/requires.txt
+-rw-rw-rw-   0        0        0        6 2023-04-06 21:43:48.000000 lumos-sat-1.0.1/lumos_sat.egg-info/top_level.txt
+-rw-rw-rw-   0        0        0      588 2023-04-06 21:43:19.000000 lumos-sat-1.0.1/pyproject.toml
+-rw-rw-rw-   0        0        0       42 2023-04-06 21:43:48.525725 lumos-sat-1.0.1/setup.cfg
```

### Comparing `lumos-sat-1.0.0/LICENSE` & `lumos-sat-1.0.1/LICENSE`

 * *Files identical despite different names*

### Comparing `lumos-sat-1.0.0/PKG-INFO` & `lumos-sat-1.0.1/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: lumos-sat
-Version: 1.0.0
+Version: 1.0.1
 Summary: Satellite Brightness Calculation Tools
 Author-email: Forrest Fankhauser <fafankhauser@ucdavis.edu>
 Requires-Python: >=3.10
 Description-Content-Type: text/markdown
 License-File: LICENSE
 
 # lumos-sat
```

### Comparing `lumos-sat-1.0.0/README.md` & `lumos-sat-1.0.1/README.md`

 * *Files identical despite different names*

### Comparing `lumos-sat-1.0.0/lumos/brdf/fit_tools.py` & `lumos-sat-1.0.1/lumos/brdf/fit_tools.py`

 * *Files identical despite different names*

### Comparing `lumos-sat-1.0.0/lumos/brdf/library.py` & `lumos-sat-1.0.1/lumos/brdf/library.py`

 * *Files identical despite different names*

### Comparing `lumos-sat-1.0.0/lumos/calculators/brightness_frame.py` & `lumos-sat-1.0.1/lumos/calculators/brightness_frame.py`

 * *Files identical despite different names*

### Comparing `lumos-sat-1.0.0/lumos/calculators/ground_frame.py` & `lumos-sat-1.0.1/lumos/calculators/ground_frame.py`

 * *Files identical despite different names*

### Comparing `lumos-sat-1.0.0/lumos/conversions.py` & `lumos-sat-1.0.1/lumos/conversions.py`

 * *Files identical despite different names*

### Comparing `lumos-sat-1.0.0/lumos/functions.py` & `lumos-sat-1.0.1/lumos/functions.py`

 * *Files identical despite different names*

### Comparing `lumos-sat-1.0.0/lumos/geometry.py` & `lumos-sat-1.0.1/lumos/geometry.py`

 * *Files identical despite different names*

### Comparing `lumos-sat-1.0.0/lumos/plot/brdf.py` & `lumos-sat-1.0.1/lumos/plot/brdf.py`

 * *Files identical despite different names*

### Comparing `lumos-sat-1.0.0/lumos/plot/brightness_frame.py` & `lumos-sat-1.0.1/lumos/plot/brightness_frame.py`

 * *Files identical despite different names*

### Comparing `lumos-sat-1.0.0/lumos/plot/ground_frame.py` & `lumos-sat-1.0.1/lumos/plot/ground_frame.py`

 * *Files identical despite different names*

### Comparing `lumos-sat-1.0.0/lumos/video_tools.py` & `lumos-sat-1.0.1/lumos/video_tools.py`

 * *Files identical despite different names*

### Comparing `lumos-sat-1.0.0/lumos_sat.egg-info/PKG-INFO` & `lumos-sat-1.0.1/lumos_sat.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: lumos-sat
-Version: 1.0.0
+Version: 1.0.1
 Summary: Satellite Brightness Calculation Tools
 Author-email: Forrest Fankhauser <fafankhauser@ucdavis.edu>
 Requires-Python: >=3.10
 Description-Content-Type: text/markdown
 License-File: LICENSE
 
 # lumos-sat
```

### Comparing `lumos-sat-1.0.0/pyproject.toml` & `lumos-sat-1.0.1/pyproject.toml`

 * *Files 2% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 [project]
 name = "lumos-sat"
-version = "1.0.0"
+version = "1.0.1"
 description = "Satellite Brightness Calculation Tools"
 authors = [
     {name = "Forrest Fankhauser", email = "fafankhauser@ucdavis.edu"},
 ]
 requires-python = ">=3.10"
 readme = "README.md"
```

