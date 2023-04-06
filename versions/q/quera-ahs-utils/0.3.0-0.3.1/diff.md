# Comparing `tmp/quera-ahs-utils-0.3.0.tar.gz` & `tmp/quera-ahs-utils-0.3.1.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "quera-ahs-utils-0.3.0.tar", last modified: Wed Apr  5 11:38:15 2023, max compression
+gzip compressed data, was "quera-ahs-utils-0.3.1.tar", last modified: Thu Apr  6 11:49:47 2023, max compression
```

## Comparing `quera-ahs-utils-0.3.0.tar` & `quera-ahs-utils-0.3.1.tar`

### file list

```diff
@@ -1,32 +1,32 @@
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 11:38:15.620792 quera-ahs-utils-0.3.0/
--rw-r--r--   0 runner    (1001) docker     (123)    10624 2023-04-05 11:37:28.000000 quera-ahs-utils-0.3.0/LICENSE
--rw-r--r--   0 runner    (1001) docker     (123)     3141 2023-04-05 11:38:15.620792 quera-ahs-utils-0.3.0/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)     2389 2023-04-05 11:37:28.000000 quera-ahs-utils-0.3.0/README.md
--rw-r--r--   0 runner    (1001) docker     (123)      777 2023-04-05 11:37:28.000000 quera-ahs-utils-0.3.0/pyproject.toml
--rw-r--r--   0 runner    (1001) docker     (123)      571 2023-04-05 11:38:15.620792 quera-ahs-utils-0.3.0/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (123)      155 2023-04-05 11:37:28.000000 quera-ahs-utils-0.3.0/setup.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 11:38:15.616792 quera-ahs-utils-0.3.0/src/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 11:38:15.620792 quera-ahs-utils-0.3.0/src/quera_ahs_utils/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-05 11:37:28.000000 quera-ahs-utils-0.3.0/src/quera_ahs_utils/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)       22 2023-04-05 11:37:28.000000 quera-ahs-utils-0.3.0/src/quera_ahs_utils/_version.py
--rw-r--r--   0 runner    (1001) docker     (123)     1882 2023-04-05 11:37:28.000000 quera-ahs-utils-0.3.0/src/quera_ahs_utils/analysis.py
--rw-r--r--   0 runner    (1001) docker     (123)    13938 2023-04-05 11:37:28.000000 quera-ahs-utils-0.3.0/src/quera_ahs_utils/drive.py
--rw-r--r--   0 runner    (1001) docker     (123)     9226 2023-04-05 11:37:28.000000 quera-ahs-utils-0.3.0/src/quera_ahs_utils/ir.py
--rw-r--r--   0 runner    (1001) docker     (123)    11676 2023-04-05 11:37:28.000000 quera-ahs-utils-0.3.0/src/quera_ahs_utils/parallelize.py
--rw-r--r--   0 runner    (1001) docker     (123)     9131 2023-04-05 11:37:28.000000 quera-ahs-utils-0.3.0/src/quera_ahs_utils/plotting.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 11:38:15.620792 quera-ahs-utils-0.3.0/src/quera_ahs_utils/quera_ir/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-05 11:37:28.000000 quera-ahs-utils-0.3.0/src/quera_ahs_utils/quera_ir/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     1752 2023-04-05 11:37:28.000000 quera-ahs-utils-0.3.0/src/quera_ahs_utils/quera_ir/capabilities.py
--rw-r--r--   0 runner    (1001) docker     (123)      896 2023-04-05 11:37:28.000000 quera-ahs-utils-0.3.0/src/quera_ahs_utils/quera_ir/task_results.py
--rw-r--r--   0 runner    (1001) docker     (123)     5575 2023-04-05 11:37:28.000000 quera-ahs-utils-0.3.0/src/quera_ahs_utils/quera_ir/task_specification.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 11:38:15.620792 quera-ahs-utils-0.3.0/src/quera_ahs_utils.egg-info/
--rw-r--r--   0 runner    (1001) docker     (123)     3141 2023-04-05 11:38:15.000000 quera-ahs-utils-0.3.0/src/quera_ahs_utils.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)      747 2023-04-05 11:38:15.000000 quera-ahs-utils-0.3.0/src/quera_ahs_utils.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-05 11:38:15.000000 quera-ahs-utils-0.3.0/src/quera_ahs_utils.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (123)       50 2023-04-05 11:38:15.000000 quera-ahs-utils-0.3.0/src/quera_ahs_utils.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (123)       16 2023-04-05 11:38:15.000000 quera-ahs-utils-0.3.0/src/quera_ahs_utils.egg-info/top_level.txt
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 11:38:15.620792 quera-ahs-utils-0.3.0/test/
--rw-r--r--   0 runner    (1001) docker     (123)     4320 2023-04-05 11:37:28.000000 quera-ahs-utils-0.3.0/test/test_drive.py
--rw-r--r--   0 runner    (1001) docker     (123)     4086 2023-04-05 11:37:28.000000 quera-ahs-utils-0.3.0/test/test_ir.py
--rw-r--r--   0 runner    (1001) docker     (123)     2030 2023-04-05 11:37:28.000000 quera-ahs-utils-0.3.0/test/test_parallelize.py
--rw-r--r--   0 runner    (1001) docker     (123)     1537 2023-04-05 11:37:28.000000 quera-ahs-utils-0.3.0/test/test_plotting.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 11:49:47.028128 quera-ahs-utils-0.3.1/
+-rw-r--r--   0 runner    (1001) docker     (123)    10624 2023-04-06 11:48:51.000000 quera-ahs-utils-0.3.1/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (123)     3141 2023-04-06 11:49:47.028128 quera-ahs-utils-0.3.1/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     2389 2023-04-06 11:48:51.000000 quera-ahs-utils-0.3.1/README.md
+-rw-r--r--   0 runner    (1001) docker     (123)      777 2023-04-06 11:48:51.000000 quera-ahs-utils-0.3.1/pyproject.toml
+-rw-r--r--   0 runner    (1001) docker     (123)      571 2023-04-06 11:49:47.028128 quera-ahs-utils-0.3.1/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (123)      155 2023-04-06 11:48:51.000000 quera-ahs-utils-0.3.1/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 11:49:47.024128 quera-ahs-utils-0.3.1/src/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 11:49:47.028128 quera-ahs-utils-0.3.1/src/quera_ahs_utils/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 11:48:51.000000 quera-ahs-utils-0.3.1/src/quera_ahs_utils/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)       22 2023-04-06 11:48:51.000000 quera-ahs-utils-0.3.1/src/quera_ahs_utils/_version.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1882 2023-04-06 11:48:51.000000 quera-ahs-utils-0.3.1/src/quera_ahs_utils/analysis.py
+-rw-r--r--   0 runner    (1001) docker     (123)    13938 2023-04-06 11:48:51.000000 quera-ahs-utils-0.3.1/src/quera_ahs_utils/drive.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9226 2023-04-06 11:48:51.000000 quera-ahs-utils-0.3.1/src/quera_ahs_utils/ir.py
+-rw-r--r--   0 runner    (1001) docker     (123)    11676 2023-04-06 11:48:51.000000 quera-ahs-utils-0.3.1/src/quera_ahs_utils/parallelize.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9131 2023-04-06 11:48:51.000000 quera-ahs-utils-0.3.1/src/quera_ahs_utils/plotting.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 11:49:47.028128 quera-ahs-utils-0.3.1/src/quera_ahs_utils/quera_ir/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 11:48:51.000000 quera-ahs-utils-0.3.1/src/quera_ahs_utils/quera_ir/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1752 2023-04-06 11:48:51.000000 quera-ahs-utils-0.3.1/src/quera_ahs_utils/quera_ir/capabilities.py
+-rw-r--r--   0 runner    (1001) docker     (123)      896 2023-04-06 11:48:51.000000 quera-ahs-utils-0.3.1/src/quera_ahs_utils/quera_ir/task_results.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5688 2023-04-06 11:48:51.000000 quera-ahs-utils-0.3.1/src/quera_ahs_utils/quera_ir/task_specification.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 11:49:47.028128 quera-ahs-utils-0.3.1/src/quera_ahs_utils.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)     3141 2023-04-06 11:49:47.000000 quera-ahs-utils-0.3.1/src/quera_ahs_utils.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)      747 2023-04-06 11:49:47.000000 quera-ahs-utils-0.3.1/src/quera_ahs_utils.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-06 11:49:47.000000 quera-ahs-utils-0.3.1/src/quera_ahs_utils.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       50 2023-04-06 11:49:47.000000 quera-ahs-utils-0.3.1/src/quera_ahs_utils.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       16 2023-04-06 11:49:47.000000 quera-ahs-utils-0.3.1/src/quera_ahs_utils.egg-info/top_level.txt
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 11:49:47.028128 quera-ahs-utils-0.3.1/test/
+-rw-r--r--   0 runner    (1001) docker     (123)     4320 2023-04-06 11:48:51.000000 quera-ahs-utils-0.3.1/test/test_drive.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4086 2023-04-06 11:48:51.000000 quera-ahs-utils-0.3.1/test/test_ir.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2030 2023-04-06 11:48:51.000000 quera-ahs-utils-0.3.1/test/test_parallelize.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1537 2023-04-06 11:48:51.000000 quera-ahs-utils-0.3.1/test/test_plotting.py
```

### Comparing `quera-ahs-utils-0.3.0/LICENSE` & `quera-ahs-utils-0.3.1/LICENSE`

 * *Files identical despite different names*

### Comparing `quera-ahs-utils-0.3.0/PKG-INFO` & `quera-ahs-utils-0.3.1/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: quera-ahs-utils
-Version: 0.3.0
+Version: 0.3.1
 Summary: Various tools to interact with Braket Analog Hamiltonian Computing
 Home-page: https://github.com/QuEraComputing/quera-ahs-utils
 Author: QuEra Computing Inc. + Braket Science Team
 Author-email: Phillip Weinberg <pweinberg@quera.com>, John Long <jlong@quera.com>
 Maintainer-email: Phillip Weinberg <pweinberg@quera.com>, John Long <jlong@quera.com>
 Project-URL: Homepage, https://github.com/QuEraComputing/quera-ahs-utils
 Project-URL: Bug Tracker, https://github.com/QuEraComputing/quera-ahs-utils/issues
```

### Comparing `quera-ahs-utils-0.3.0/README.md` & `quera-ahs-utils-0.3.1/README.md`

 * *Files identical despite different names*

### Comparing `quera-ahs-utils-0.3.0/pyproject.toml` & `quera-ahs-utils-0.3.1/pyproject.toml`

 * *Files 1% similar despite different names*

```diff
@@ -1,14 +1,14 @@
 [build-system]
 requires = ["setuptools>=61.0"]
 build-backend = "setuptools.build_meta"
 
 [project]
 name = "quera-ahs-utils"
-version = "0.3.0"
+version = "0.3.1"
 authors = [
   { name="Phillip Weinberg", email="pweinberg@quera.com" },
   { name="John Long", email="jlong@quera.com" }
 ]
 maintainers = [
   { name="Phillip Weinberg", email="pweinberg@quera.com" },
   { name="John Long", email="jlong@quera.com" }
```

### Comparing `quera-ahs-utils-0.3.0/setup.cfg` & `quera-ahs-utils-0.3.1/setup.cfg`

 * *Files identical despite different names*

### Comparing `quera-ahs-utils-0.3.0/src/quera_ahs_utils/analysis.py` & `quera-ahs-utils-0.3.1/src/quera_ahs_utils/analysis.py`

 * *Files identical despite different names*

### Comparing `quera-ahs-utils-0.3.0/src/quera_ahs_utils/drive.py` & `quera-ahs-utils-0.3.1/src/quera_ahs_utils/drive.py`

 * *Files identical despite different names*

### Comparing `quera-ahs-utils-0.3.0/src/quera_ahs_utils/ir.py` & `quera-ahs-utils-0.3.1/src/quera_ahs_utils/ir.py`

 * *Files identical despite different names*

### Comparing `quera-ahs-utils-0.3.0/src/quera_ahs_utils/parallelize.py` & `quera-ahs-utils-0.3.1/src/quera_ahs_utils/parallelize.py`

 * *Files identical despite different names*

### Comparing `quera-ahs-utils-0.3.0/src/quera_ahs_utils/plotting.py` & `quera-ahs-utils-0.3.1/src/quera_ahs_utils/plotting.py`

 * *Files identical despite different names*

### Comparing `quera-ahs-utils-0.3.0/src/quera_ahs_utils/quera_ir/capabilities.py` & `quera-ahs-utils-0.3.1/src/quera_ahs_utils/quera_ir/capabilities.py`

 * *Files identical despite different names*

### Comparing `quera-ahs-utils-0.3.0/src/quera_ahs_utils/quera_ir/task_results.py` & `quera-ahs-utils-0.3.1/src/quera_ahs_utils/quera_ir/task_results.py`

 * *Files identical despite different names*

### Comparing `quera-ahs-utils-0.3.0/src/quera_ahs_utils/quera_ir/task_specification.py` & `quera-ahs-utils-0.3.1/src/quera_ahs_utils/quera_ir/task_specification.py`

 * *Files 4% similar despite different names*

```diff
@@ -38,15 +38,15 @@
             'global_': 'global'
         }
     
     def __hash__(self):
         return hash((RabiFrequencyAmplitude, self.global_))
     
     def discretize(self, task_capabilities: QuEraCapabilities):
-        global_time_resolution = task_capabilities.capabilities.rydberg.global_.time_delta_min
+        global_time_resolution = task_capabilities.capabilities.rydberg.global_.time_resolution
         global_value_resolution =  task_capabilities.capabilities.rydberg.global_.rabi_frequency_resolution
         
         return RabiFrequencyAmplitude(**{"global":GlobalField(
                 times = discretize_list(self.global_.times, global_time_resolution),
                 values = discretize_list(self.global_.values, global_value_resolution))} 
             )
 
@@ -58,16 +58,16 @@
             'global_': 'global'
         }
         
     def __hash__(self):
         return hash((RabiFrequencyPhase, self.global_))
     
     def discretize(self, task_capabilities: QuEraCapabilities):
-        global_time_resolution = task_capabilities.capabilities.rydberg.global_.time_delta_min
-        global_value_resolution =  task_capabilities.capabilities.rydberg.global_.rabi_frequency_resolution
+        global_time_resolution = task_capabilities.capabilities.rydberg.global_.time_resolution
+        global_value_resolution =  task_capabilities.capabilities.rydberg.global_.phase_resolution
         
         return RabiFrequencyPhase(**{"global":GlobalField(
                 times = discretize_list(self.global_.times, global_time_resolution),
                 values = discretize_list(self.global_.values, global_value_resolution))}               
             )
     
 class Detuning(BaseModel):
@@ -79,22 +79,23 @@
             'global_': 'global'
         }
 
     def __hash__(self):
         return hash((Detuning, self.global_, self.local))
     
     def discretize(self, task_capabilities: QuEraCapabilities):
-        global_time_resolution = task_capabilities.capabilities.rydberg.global_.time_delta_min
-        global_value_resolution =  task_capabilities.capabilities.rydberg.global_.rabi_frequency_resolution
-        
+        global_time_resolution = task_capabilities.capabilities.rydberg.global_.time_resolution
+        global_value_resolution =  task_capabilities.capabilities.rydberg.global_.detuning_resolution
+        local_time_resolution = task_capabilities.capabilities.rydberg.local.time_resolution
+
         return Detuning(**{"global":GlobalField(
                 times = discretize_list(self.global_.times, global_time_resolution),
                 values = discretize_list(self.global_.values, global_value_resolution)
             ),"local": LocalField(
-                    times = self.local.times, values = self.local.values,
+                    times = discretize_list(self.local.times, local_time_resolution), values = self.local.values,
                     lattice_site_coefficients=self.local.lattice_site_coefficients
                 )
             }
         )
     
 class RydbergHamiltonian(BaseModel):
     rabi_frequency_amplitude: RabiFrequencyAmplitude
```

### Comparing `quera-ahs-utils-0.3.0/src/quera_ahs_utils.egg-info/PKG-INFO` & `quera-ahs-utils-0.3.1/src/quera_ahs_utils.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: quera-ahs-utils
-Version: 0.3.0
+Version: 0.3.1
 Summary: Various tools to interact with Braket Analog Hamiltonian Computing
 Home-page: https://github.com/QuEraComputing/quera-ahs-utils
 Author: QuEra Computing Inc. + Braket Science Team
 Author-email: Phillip Weinberg <pweinberg@quera.com>, John Long <jlong@quera.com>
 Maintainer-email: Phillip Weinberg <pweinberg@quera.com>, John Long <jlong@quera.com>
 Project-URL: Homepage, https://github.com/QuEraComputing/quera-ahs-utils
 Project-URL: Bug Tracker, https://github.com/QuEraComputing/quera-ahs-utils/issues
```

### Comparing `quera-ahs-utils-0.3.0/src/quera_ahs_utils.egg-info/SOURCES.txt` & `quera-ahs-utils-0.3.1/src/quera_ahs_utils.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `quera-ahs-utils-0.3.0/test/test_drive.py` & `quera-ahs-utils-0.3.1/test/test_drive.py`

 * *Files identical despite different names*

### Comparing `quera-ahs-utils-0.3.0/test/test_ir.py` & `quera-ahs-utils-0.3.1/test/test_ir.py`

 * *Files identical despite different names*

### Comparing `quera-ahs-utils-0.3.0/test/test_parallelize.py` & `quera-ahs-utils-0.3.1/test/test_parallelize.py`

 * *Files identical despite different names*

### Comparing `quera-ahs-utils-0.3.0/test/test_plotting.py` & `quera-ahs-utils-0.3.1/test/test_plotting.py`

 * *Files identical despite different names*

