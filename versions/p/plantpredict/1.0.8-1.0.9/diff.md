# Comparing `tmp/plantpredict-1.0.8.tar.gz` & `tmp/plantpredict-1.0.9.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "plantpredict-1.0.8.tar", last modified: Wed Oct 26 14:34:11 2022, max compression
+gzip compressed data, was "plantpredict-1.0.9.tar", last modified: Wed Apr  5 14:00:55 2023, max compression
```

## Comparing `plantpredict-1.0.8.tar` & `plantpredict-1.0.9.tar`

### file list

```diff
@@ -1,28 +1,42 @@
-drwxrwxrwx   0        0        0        0 2022-10-26 14:34:11.761694 plantpredict-1.0.8/
--rw-rw-rw-   0        0        0     1090 2021-10-26 12:39:42.000000 plantpredict-1.0.8/LICENSE
--rw-rw-rw-   0        0        0      808 2022-10-26 14:34:11.760696 plantpredict-1.0.8/PKG-INFO
--rw-rw-rw-   0        0        0      413 2022-10-26 14:19:49.000000 plantpredict-1.0.8/README.md
-drwxrwxrwx   0        0        0        0 2022-10-26 14:34:11.755709 plantpredict-1.0.8/plantpredict/
--rw-rw-rw-   0        0        0       84 2021-10-26 12:39:42.000000 plantpredict-1.0.8/plantpredict/__init__.py
--rw-rw-rw-   0        0        0     2218 2022-10-24 17:39:50.000000 plantpredict-1.0.8/plantpredict/api.py
--rw-rw-rw-   0        0        0     2590 2022-09-14 14:05:12.000000 plantpredict-1.0.8/plantpredict/ashrae.py
--rw-rw-rw-   0        0        0     6536 2021-10-26 12:39:42.000000 plantpredict-1.0.8/plantpredict/enumerations.py
--rw-rw-rw-   0        0        0     2530 2022-09-14 14:05:12.000000 plantpredict-1.0.8/plantpredict/error_handlers.py
--rw-rw-rw-   0        0        0     9994 2022-09-14 14:05:12.000000 plantpredict-1.0.8/plantpredict/geo.py
--rw-rw-rw-   0        0        0     2568 2021-10-26 12:39:42.000000 plantpredict-1.0.8/plantpredict/helpers.py
--rw-rw-rw-   0        0        0     2935 2021-10-26 12:39:42.000000 plantpredict-1.0.8/plantpredict/inverter.py
--rw-rw-rw-   0        0        0    64106 2022-09-14 14:05:12.000000 plantpredict-1.0.8/plantpredict/module.py
--rw-rw-rw-   0        0        0     2293 2022-09-14 14:05:12.000000 plantpredict-1.0.8/plantpredict/plant_predict_entity.py
--rw-rw-rw-   0        0        0   101649 2021-10-26 12:39:42.000000 plantpredict-1.0.8/plantpredict/powerplant.py
--rw-rw-rw-   0        0        0    13139 2021-10-26 12:39:42.000000 plantpredict-1.0.8/plantpredict/prediction.py
--rw-rw-rw-   0        0        0     6977 2022-09-14 14:05:12.000000 plantpredict-1.0.8/plantpredict/project.py
--rw-rw-rw-   0        0        0     5279 2021-10-26 12:39:42.000000 plantpredict-1.0.8/plantpredict/utilities.py
--rw-rw-rw-   0        0        0     9766 2022-10-24 17:39:55.000000 plantpredict-1.0.8/plantpredict/weather.py
-drwxrwxrwx   0        0        0        0 2022-10-26 14:34:11.759698 plantpredict-1.0.8/plantpredict.egg-info/
--rw-rw-rw-   0        0        0      808 2022-10-26 14:34:11.000000 plantpredict-1.0.8/plantpredict.egg-info/PKG-INFO
--rw-rw-rw-   0        0        0      590 2022-10-26 14:34:11.000000 plantpredict-1.0.8/plantpredict.egg-info/SOURCES.txt
--rw-rw-rw-   0        0        0        1 2022-10-26 14:34:11.000000 plantpredict-1.0.8/plantpredict.egg-info/dependency_links.txt
--rw-rw-rw-   0        0        0       39 2022-10-26 14:34:11.000000 plantpredict-1.0.8/plantpredict.egg-info/requires.txt
--rw-rw-rw-   0        0        0       13 2022-10-26 14:34:11.000000 plantpredict-1.0.8/plantpredict.egg-info/top_level.txt
--rw-rw-rw-   0        0        0       42 2022-10-26 14:34:11.761694 plantpredict-1.0.8/setup.cfg
--rw-rw-rw-   0        0        0      749 2022-10-26 14:19:55.000000 plantpredict-1.0.8/setup.py
+drwxrwxrwx   0        0        0        0 2023-04-05 14:00:55.218663 plantpredict-1.0.9/
+-rw-rw-rw-   0        0        0     1090 2023-03-28 13:53:34.000000 plantpredict-1.0.9/LICENSE
+-rw-rw-rw-   0        0        0      808 2023-04-05 14:00:55.217664 plantpredict-1.0.9/PKG-INFO
+-rw-rw-rw-   0        0        0      413 2023-04-05 13:52:23.000000 plantpredict-1.0.9/README.md
+drwxrwxrwx   0        0        0        0 2023-04-05 14:00:55.194554 plantpredict-1.0.9/plantpredict/
+-rw-rw-rw-   0        0        0       84 2023-03-28 13:53:34.000000 plantpredict-1.0.9/plantpredict/__init__.py
+-rw-rw-rw-   0        0        0     2218 2023-03-28 13:53:34.000000 plantpredict-1.0.9/plantpredict/api.py
+-rw-rw-rw-   0        0        0     2590 2023-03-28 13:53:34.000000 plantpredict-1.0.9/plantpredict/ashrae.py
+-rw-rw-rw-   0        0        0     6536 2023-03-28 13:53:34.000000 plantpredict-1.0.9/plantpredict/enumerations.py
+-rw-rw-rw-   0        0        0     2530 2023-03-28 13:53:34.000000 plantpredict-1.0.9/plantpredict/error_handlers.py
+-rw-rw-rw-   0        0        0     9994 2023-03-28 13:53:34.000000 plantpredict-1.0.9/plantpredict/geo.py
+-rw-rw-rw-   0        0        0     2568 2023-03-28 13:53:34.000000 plantpredict-1.0.9/plantpredict/helpers.py
+-rw-rw-rw-   0        0        0     2935 2023-03-28 13:53:34.000000 plantpredict-1.0.9/plantpredict/inverter.py
+-rw-rw-rw-   0        0        0    64106 2023-03-28 13:53:34.000000 plantpredict-1.0.9/plantpredict/module.py
+-rw-rw-rw-   0        0        0     2293 2023-03-28 13:53:34.000000 plantpredict-1.0.9/plantpredict/plant_predict_entity.py
+-rw-rw-rw-   0        0        0   101653 2023-04-05 13:45:54.000000 plantpredict-1.0.9/plantpredict/powerplant.py
+-rw-rw-rw-   0        0        0    13139 2023-03-28 13:53:34.000000 plantpredict-1.0.9/plantpredict/prediction.py
+-rw-rw-rw-   0        0        0     6977 2023-03-28 13:53:34.000000 plantpredict-1.0.9/plantpredict/project.py
+-rw-rw-rw-   0        0        0     5042 2023-04-05 13:43:25.000000 plantpredict-1.0.9/plantpredict/utilities.py
+-rw-rw-rw-   0        0        0     9766 2023-03-28 13:53:34.000000 plantpredict-1.0.9/plantpredict/weather.py
+drwxrwxrwx   0        0        0        0 2023-04-05 14:00:55.201319 plantpredict-1.0.9/plantpredict.egg-info/
+-rw-rw-rw-   0        0        0      808 2023-04-05 14:00:55.000000 plantpredict-1.0.9/plantpredict.egg-info/PKG-INFO
+-rw-rw-rw-   0        0        0      895 2023-04-05 14:00:55.000000 plantpredict-1.0.9/plantpredict.egg-info/SOURCES.txt
+-rw-rw-rw-   0        0        0        1 2023-04-05 14:00:55.000000 plantpredict-1.0.9/plantpredict.egg-info/dependency_links.txt
+-rw-rw-rw-   0        0        0       39 2023-04-05 14:00:55.000000 plantpredict-1.0.9/plantpredict.egg-info/requires.txt
+-rw-rw-rw-   0        0        0       13 2023-04-05 14:00:55.000000 plantpredict-1.0.9/plantpredict.egg-info/top_level.txt
+-rw-rw-rw-   0        0        0       42 2023-04-05 14:00:55.218663 plantpredict-1.0.9/setup.cfg
+-rw-rw-rw-   0        0        0      749 2023-04-05 13:52:27.000000 plantpredict-1.0.9/setup.py
+drwxrwxrwx   0        0        0        0 2023-04-05 14:00:55.216667 plantpredict-1.0.9/tests/
+-rw-rw-rw-   0        0        0     1821 2023-03-28 13:53:34.000000 plantpredict-1.0.9/tests/test_api.py
+-rw-rw-rw-   0        0        0     1649 2023-03-28 13:53:34.000000 plantpredict-1.0.9/tests/test_ashrae.py
+-rw-rw-rw-   0        0        0      187 2023-03-28 13:53:34.000000 plantpredict-1.0.9/tests/test_error_handlers.py
+-rw-rw-rw-   0        0        0     2598 2023-03-28 13:53:34.000000 plantpredict-1.0.9/tests/test_geo.py
+-rw-rw-rw-   0        0        0     2357 2023-03-28 13:53:34.000000 plantpredict-1.0.9/tests/test_helpers.py
+-rw-rw-rw-   0        0        0     2070 2023-03-28 13:53:34.000000 plantpredict-1.0.9/tests/test_inverter.py
+-rw-rw-rw-   0        0        0    18338 2023-03-28 13:53:34.000000 plantpredict-1.0.9/tests/test_module.py
+-rw-rw-rw-   0        0        0     2791 2023-03-28 13:53:34.000000 plantpredict-1.0.9/tests/test_plant_predict_entity.py
+-rw-rw-rw-   0        0        0    52406 2023-03-28 13:53:34.000000 plantpredict-1.0.9/tests/test_powerplant.py
+-rw-rw-rw-   0        0        0     6795 2023-03-28 13:53:34.000000 plantpredict-1.0.9/tests/test_prediction.py
+-rw-rw-rw-   0        0        0     4838 2023-03-28 13:53:34.000000 plantpredict-1.0.9/tests/test_project.py
+-rw-rw-rw-   0        0        0     2992 2023-03-28 13:53:34.000000 plantpredict-1.0.9/tests/test_utilities.py
+-rw-rw-rw-   0        0        0     2915 2023-03-28 13:53:34.000000 plantpredict-1.0.9/tests/test_weather.py
```

### Comparing `plantpredict-1.0.8/LICENSE` & `plantpredict-1.0.9/LICENSE`

 * *Files identical despite different names*

### Comparing `plantpredict-1.0.8/PKG-INFO` & `plantpredict-1.0.9/PKG-INFO`

 * *Files 2% similar despite different names*

```diff
@@ -1,23 +1,23 @@
 Metadata-Version: 2.1
 Name: plantpredict
-Version: 1.0.8
+Version: 1.0.9
 Summary: Python SDK for PlantPredict (https://ui.plantpredict.terabase.energy).
 Home-page: https://github.com/plantpredict/python-sdk
 Author: Stephen Kaplan, Performance & Prediction Engineer at First Solar, Inc.
 Author-email: stephen.kaplan@firstsolar.com
 License: LICENSE.txt
 Requires-Python: >=3.5, <4
 License-File: LICENSE
 
 <img src="docs/_images/FS_PlantPredict_Logo_Horz_RGB-01.png" width="50%" height="50%">
 
 # plantpredict-python
 
-Install **latest stable version** (1.0.8) via: `pip install plantpredict`.
+Install **latest stable version** (1.0.9) via: `pip install plantpredict`.
 
 Install **development version** via Github master branch.
 
 ---
 
 Documentation can be found at https://plantpredict-python.readthedocs.io
```

### Comparing `plantpredict-1.0.8/plantpredict/api.py` & `plantpredict-1.0.9/plantpredict/api.py`

 * *Files identical despite different names*

### Comparing `plantpredict-1.0.8/plantpredict/ashrae.py` & `plantpredict-1.0.9/plantpredict/ashrae.py`

 * *Files identical despite different names*

### Comparing `plantpredict-1.0.8/plantpredict/enumerations.py` & `plantpredict-1.0.9/plantpredict/enumerations.py`

 * *Files identical despite different names*

### Comparing `plantpredict-1.0.8/plantpredict/error_handlers.py` & `plantpredict-1.0.9/plantpredict/error_handlers.py`

 * *Files identical despite different names*

### Comparing `plantpredict-1.0.8/plantpredict/geo.py` & `plantpredict-1.0.9/plantpredict/geo.py`

 * *Files identical despite different names*

### Comparing `plantpredict-1.0.8/plantpredict/helpers.py` & `plantpredict-1.0.9/plantpredict/helpers.py`

 * *Files identical despite different names*

### Comparing `plantpredict-1.0.8/plantpredict/inverter.py` & `plantpredict-1.0.9/plantpredict/inverter.py`

 * *Files identical despite different names*

### Comparing `plantpredict-1.0.8/plantpredict/module.py` & `plantpredict-1.0.9/plantpredict/module.py`

 * *Files identical despite different names*

### Comparing `plantpredict-1.0.8/plantpredict/plant_predict_entity.py` & `plantpredict-1.0.9/plantpredict/plant_predict_entity.py`

 * *Files identical despite different names*

### Comparing `plantpredict-1.0.8/plantpredict/powerplant.py` & `plantpredict-1.0.9/plantpredict/powerplant.py`

 * *Files 0% similar despite different names*

```diff
@@ -126,15 +126,15 @@
 
             .. code-block:: python
 
                 powerplant.transmission_lines = [{
                     "id": 48373,
                     "length": 2.0,                             # units [km]
                     "resistance": 0.5,                         # units [Ohms/300 m]
-                    "number_of_conducters_per_phase": 3,
+                    "number_of_conductors_per_phase": 3,
                     "ordinal": 1
                 }]
 
     .. container:: toggle
 
         .. container:: header
 
@@ -370,15 +370,15 @@
                         energy meter (1-indexed).
         """
         transmission_line = {
             "length": length,
             "resistance": resistance,
             "number_of_conductors_per_phase": number_of_conductors_per_phase,
             "ordinal": ordinal
-        }
+            }
         # append new transmission line, or if list doesn't yet exist, create it
         try:
             self.transmission_lines.append(transmission_line)
         except AttributeError:
             self.transmission_lines = [transmission_line]
 
     def _validate_block_name(self, block_name):
```

### Comparing `plantpredict-1.0.8/plantpredict/prediction.py` & `plantpredict-1.0.9/plantpredict/prediction.py`

 * *Files identical despite different names*

### Comparing `plantpredict-1.0.8/plantpredict/project.py` & `plantpredict-1.0.9/plantpredict/project.py`

 * *Files identical despite different names*

### Comparing `plantpredict-1.0.8/plantpredict/utilities.py` & `plantpredict-1.0.9/plantpredict/utilities.py`

 * *Files 4% similar despite different names*

```diff
@@ -60,28 +60,26 @@
         "light_generatedcurrent": "light_generated_current",
         "bo_s": "bos",
         "sandiaconductive": "sandia_conductive",
         "sandiaconvective": "sandia_convective",
         "l_i_d": "lid",
         "at25": "at_25",
         "l_g_i_a": "lgia",
-        "number_of_conducters_per_phase": "number_of_conductors_per_phase",      # misspelled in PlantPredict backend
         "cool996": "cool_996",
         "heat996": "heat_996",
         "max50_year": "max_50_year",
         "min50_year": "min_50_year",
         "p_q": "pq",
         "kvacurves": "kva_curves",
-        "k_va": "kva"
+        "k_va": "kva",
     },
     "snake_to_camel": {
         "powerplant": "powerPlant",
         "backtracking": "backTracking",
-        "backsideMismatch": "backSideMismatch",
-        "numberOfConductorsPerPhase": "numberOfConductersPerPhase"              # misspelled in PlantPredict backend
+        "backsideMismatch": "backSideMismatch"
     }
 }
 
 
 def convert_json(d, convert_function):
     """
     Convert a nested dictionary from one convention to another. Prepares payload for http request.
```

### Comparing `plantpredict-1.0.8/plantpredict/weather.py` & `plantpredict-1.0.9/plantpredict/weather.py`

 * *Files identical despite different names*

### Comparing `plantpredict-1.0.8/plantpredict.egg-info/PKG-INFO` & `plantpredict-1.0.9/plantpredict.egg-info/PKG-INFO`

 * *Files 2% similar despite different names*

```diff
@@ -1,23 +1,23 @@
 Metadata-Version: 2.1
 Name: plantpredict
-Version: 1.0.8
+Version: 1.0.9
 Summary: Python SDK for PlantPredict (https://ui.plantpredict.terabase.energy).
 Home-page: https://github.com/plantpredict/python-sdk
 Author: Stephen Kaplan, Performance & Prediction Engineer at First Solar, Inc.
 Author-email: stephen.kaplan@firstsolar.com
 License: LICENSE.txt
 Requires-Python: >=3.5, <4
 License-File: LICENSE
 
 <img src="docs/_images/FS_PlantPredict_Logo_Horz_RGB-01.png" width="50%" height="50%">
 
 # plantpredict-python
 
-Install **latest stable version** (1.0.8) via: `pip install plantpredict`.
+Install **latest stable version** (1.0.9) via: `pip install plantpredict`.
 
 Install **development version** via Github master branch.
 
 ---
 
 Documentation can be found at https://plantpredict-python.readthedocs.io
```

### Comparing `plantpredict-1.0.8/setup.py` & `plantpredict-1.0.9/setup.py`

 * *Files 2% similar despite different names*

```diff
@@ -2,15 +2,15 @@
 from setuptools import setup
 
 __currdir__ = os.getcwd()
 __readme__ = os.path.join(__currdir__, 'README.md')
 
 setup(
     name='plantpredict',
-    version='1.0.8',
+    version='1.0.9',
     description='Python SDK for PlantPredict (https://ui.plantpredict.terabase.energy).',
     url='https://github.com/plantpredict/python-sdk',
     author='Stephen Kaplan, Performance & Prediction Engineer at First Solar, Inc.',
     author_email='stephen.kaplan@firstsolar.com',
     license='LICENSE.txt',
     long_description=open(__readme__).read(),
     packages=['plantpredict'],
```

