# Comparing `tmp/steam-pysigma-2023.3.4.tar.gz` & `tmp/steam-pysigma-2023.4.6.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "dist\steam-pysigma-2023.3.4.tar", last modified: Mon Apr  3 06:57:34 2023, max compression
+gzip compressed data, was "dist\steam-pysigma-2023.4.6.tar", last modified: Thu Apr  6 09:06:49 2023, max compression
```

## Comparing `steam-pysigma-2023.3.4.tar` & `steam-pysigma-2023.4.6.tar`

### file list

```diff
@@ -1,15 +1,15 @@
-drwxrwxrwx   0        0        0        0 2023-04-03 06:57:34.072499 steam-pysigma-2023.3.4/
--rw-rw-rw-   0        0        0     1030 2023-04-03 06:57:34.071499 steam-pysigma-2023.3.4/PKG-INFO
--rw-rw-rw-   0        0        0      616 2023-02-22 13:16:40.000000 steam-pysigma-2023.3.4/README.md
--rw-rw-rw-   0        0        0       42 2023-04-03 06:57:34.072499 steam-pysigma-2023.3.4/setup.cfg
--rw-rw-rw-   0        0        0      867 2023-04-03 06:56:43.000000 steam-pysigma-2023.3.4/setup.py
-drwxrwxrwx   0        0        0        0 2023-04-03 06:57:34.062498 steam-pysigma-2023.3.4/steam_pysigma/
--rw-rw-rw-   0        0        0        0 2023-02-02 13:16:25.000000 steam-pysigma-2023.3.4/steam_pysigma/__init__.py
--rw-rw-rw-   0        0        0    10769 2023-03-22 08:15:49.000000 steam-pysigma-2023.3.4/steam_pysigma/helpers.py
--rw-rw-rw-   0        0        0     8279 2023-03-15 16:25:27.000000 steam-pysigma-2023.3.4/steam_pysigma/pysigma.py
-drwxrwxrwx   0        0        0        0 2023-04-03 06:57:34.069499 steam-pysigma-2023.3.4/steam_pysigma.egg-info/
--rw-rw-rw-   0        0        0     1030 2023-04-03 06:57:30.000000 steam-pysigma-2023.3.4/steam_pysigma.egg-info/PKG-INFO
--rw-rw-rw-   0        0        0      278 2023-04-03 06:57:30.000000 steam-pysigma-2023.3.4/steam_pysigma.egg-info/SOURCES.txt
--rw-rw-rw-   0        0        0        1 2023-04-03 06:57:30.000000 steam-pysigma-2023.3.4/steam_pysigma.egg-info/dependency_links.txt
--rw-rw-rw-   0        0        0      237 2023-04-03 06:57:30.000000 steam-pysigma-2023.3.4/steam_pysigma.egg-info/requires.txt
--rw-rw-rw-   0        0        0       14 2023-04-03 06:57:30.000000 steam-pysigma-2023.3.4/steam_pysigma.egg-info/top_level.txt
+drwxrwxrwx   0        0        0        0 2023-04-06 09:06:49.882294 steam-pysigma-2023.4.6/
+-rw-rw-rw-   0        0        0     1030 2023-04-06 09:06:49.881294 steam-pysigma-2023.4.6/PKG-INFO
+-rw-rw-rw-   0        0        0      616 2023-02-22 13:16:40.000000 steam-pysigma-2023.4.6/README.md
+-rw-rw-rw-   0        0        0       42 2023-04-06 09:06:49.882294 steam-pysigma-2023.4.6/setup.cfg
+-rw-rw-rw-   0        0        0      867 2023-04-06 09:06:44.000000 steam-pysigma-2023.4.6/setup.py
+drwxrwxrwx   0        0        0        0 2023-04-06 09:06:49.872293 steam-pysigma-2023.4.6/steam_pysigma/
+-rw-rw-rw-   0        0        0        0 2023-02-02 13:16:25.000000 steam-pysigma-2023.4.6/steam_pysigma/__init__.py
+-rw-rw-rw-   0        0        0    10881 2023-04-05 08:23:05.000000 steam-pysigma-2023.4.6/steam_pysigma/helpers.py
+-rw-rw-rw-   0        0        0     8355 2023-04-05 08:56:51.000000 steam-pysigma-2023.4.6/steam_pysigma/pysigma.py
+drwxrwxrwx   0        0        0        0 2023-04-06 09:06:49.880293 steam-pysigma-2023.4.6/steam_pysigma.egg-info/
+-rw-rw-rw-   0        0        0     1030 2023-04-06 09:06:46.000000 steam-pysigma-2023.4.6/steam_pysigma.egg-info/PKG-INFO
+-rw-rw-rw-   0        0        0      278 2023-04-06 09:06:46.000000 steam-pysigma-2023.4.6/steam_pysigma.egg-info/SOURCES.txt
+-rw-rw-rw-   0        0        0        1 2023-04-06 09:06:46.000000 steam-pysigma-2023.4.6/steam_pysigma.egg-info/dependency_links.txt
+-rw-rw-rw-   0        0        0      237 2023-04-06 09:06:46.000000 steam-pysigma-2023.4.6/steam_pysigma.egg-info/requires.txt
+-rw-rw-rw-   0        0        0       14 2023-04-06 09:06:46.000000 steam-pysigma-2023.4.6/steam_pysigma.egg-info/top_level.txt
```

### Comparing `steam-pysigma-2023.3.4/PKG-INFO` & `steam-pysigma-2023.4.6/PKG-INFO`

 * *Files 7% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: steam-pysigma
-Version: 2023.3.4
+Version: 2023.4.6
 Summary: This is python wrapper of STEAM SIGMA code
 Home-page: https://gitlab.cern.ch/steam/steam_pysigma
 Author: STEAM Team
 Author-email: steam-team@cern.ch
 License: UNKNOWN
 Keywords: CERN,SIGMA,STEAM
 Platform: UNKNOWN
```

### Comparing `steam-pysigma-2023.3.4/README.md` & `steam-pysigma-2023.4.6/README.md`

 * *Files identical despite different names*

### Comparing `steam-pysigma-2023.3.4/setup.py` & `steam-pysigma-2023.4.6/setup.py`

 * *Files 2% similar despite different names*

```diff
@@ -5,15 +5,15 @@
     long_description = fh.read()
 
 with open('requirements.txt') as f:
     required = f.read().splitlines()
 
 setup(
     name='steam-pysigma',
-    version="2023.3.4",
+    version="2023.4.6",
     author="STEAM Team",
     author_email="steam-team@cern.ch",
     description="This is python wrapper of STEAM SIGMA code",
     long_description=long_description,
     long_description_content_type='text/markdown',
     url="https://gitlab.cern.ch/steam/steam_pysigma",
     keywords={'STEAM', 'SIGMA', 'CERN'},
```

### Comparing `steam-pysigma-2023.3.4/steam_pysigma/helpers.py` & `steam-pysigma-2023.4.6/steam_pysigma/helpers.py`

 * *Files 2% similar despite different names*

```diff
@@ -122,14 +122,17 @@
     map.put(constants.LABEL_FLAG_ISCC_ADJN, FLAG_iscc_adjn)
     map.put(constants.LABEL_FLAG_MPERS, FLAG_M_pers)
     map.put(constants.LABEL_FLAG_QUENCH_ALL, FLAG_quench_all)
     map.put(constants.LABEL_FLAG_QUENCH_OFF, FLAG_quench_off)
     map.put(constants.LABEL_PARAM_QUENCH_TIME, PARAM_time_quench)
     map.put(constants.LABEL_MAGNETIC_LENGTH, magnetic_length)
     map.put(constants.LABEL_OPERATIONAL_TEMPERATUR, str(T_initial))
+    map.put(constants.LABEL_INIT_QUENCH_HEAT, str(50000))
+    map.put(constants.LABEL_QUENCH_TEMP, str(10))
+
 
     num_qh = model_data['Quench_Protection']['Quench_Heaters']['N_strips']
     ins_list = model_data['Quench_Protection']['Quench_Heaters']['s_ins']
     w_list = model_data['Quench_Protection']['Quench_Heaters']['w']
     qh_to_bath_list = model_data['Quench_Protection']['Quench_Heaters']['s_ins_He']
     qh_steel_strip = model_data['Quench_Protection']['Quench_Heaters']['h']
     tau = [round(a * b, 4) for a, b in zip(model_data['Quench_Protection']['Quench_Heaters']['R_warm'],
```

### Comparing `steam-pysigma-2023.3.4/steam_pysigma/pysigma.py` & `steam-pysigma-2023.4.6/steam_pysigma/pysigma.py`

 * *Files 1% similar despite different names*

```diff
@@ -44,14 +44,16 @@
         self.MagnetMPHBuilder = self.gateway.jvm.comsol.MagnetMPHBuilder
         self.QuenchHeaterMPHBuilder = self.gateway.jvm.comsol.QuenchHeaterMPHBuilder
         self.Cable = self.gateway.jvm.model.geometry.coil.Cable
         self.Winding = self.gateway.jvm.model.geometry.coil.Winding
         self.Pole = self.gateway.jvm.model.geometry.coil.Pole
         self.Coil = self.gateway.jvm.model.geometry.coil.Coil
         self.Magnet_T0_QH = self.gateway.jvm.input.OthersT0.Magnet_T0_QH
+        self.Magnet_T1_QH = self.gateway.jvm.input.OthersT0.Magnet_T1_QH
+
         self.StudyAPI = self.gateway.jvm.comsol.api.StudyAPI
         self.ResultsAPI = self.gateway.jvm.comsol.api.ResultsAPI
         self.constants = self.gateway.jvm.comsol.constants.MPHC
     # def __del__(self):
     #     self.gateway.shutdown()
 
 class ArraysSIGMA:
```

### Comparing `steam-pysigma-2023.3.4/steam_pysigma.egg-info/PKG-INFO` & `steam-pysigma-2023.4.6/steam_pysigma.egg-info/PKG-INFO`

 * *Files 7% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: steam-pysigma
-Version: 2023.3.4
+Version: 2023.4.6
 Summary: This is python wrapper of STEAM SIGMA code
 Home-page: https://gitlab.cern.ch/steam/steam_pysigma
 Author: STEAM Team
 Author-email: steam-team@cern.ch
 License: UNKNOWN
 Keywords: CERN,SIGMA,STEAM
 Platform: UNKNOWN
```

