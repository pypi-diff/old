# Comparing `tmp/posym-0.5.0.tar.gz` & `tmp/posym-0.5.1.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "posym-0.5.0.tar", last modified: Thu Apr  6 10:47:14 2023, max compression
+gzip compressed data, was "posym-0.5.1.tar", last modified: Thu Apr  6 15:56:37 2023, max compression
```

## Comparing `posym-0.5.0.tar` & `posym-0.5.1.tar`

### file list

```diff
@@ -1,30 +1,30 @@
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 10:47:14.377541 posym-0.5.0/
--rw-r--r--   0 runner    (1001) docker     (123)     1070 2023-04-06 10:47:03.000000 posym-0.5.0/LICENSE
--rw-r--r--   0 runner    (1001) docker     (123)    13717 2023-04-06 10:47:14.377541 posym-0.5.0/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)    13452 2023-04-06 10:47:03.000000 posym-0.5.0/README.md
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 10:47:14.377541 posym-0.5.0/c/
--rw-r--r--   0 runner    (1001) docker     (123)    12679 2023-04-06 10:47:03.000000 posym-0.5.0/c/integrals.c
--rw-r--r--   0 runner    (1001) docker     (123)     7282 2023-04-06 10:47:03.000000 posym-0.5.0/c/permutations.c
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 10:47:14.377541 posym-0.5.0/posym/
--rw-r--r--   0 runner    (1001) docker     (123)    27131 2023-04-06 10:47:03.000000 posym-0.5.0/posym/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      972 2023-04-06 10:47:03.000000 posym-0.5.0/posym/algebra.py
--rw-r--r--   0 runner    (1001) docker     (123)    30004 2023-04-06 10:47:03.000000 posym-0.5.0/posym/basis.py
--rw-r--r--   0 runner    (1001) docker     (123)    28249 2023-04-06 10:47:03.000000 posym-0.5.0/posym/generate_tables.py
--rw-r--r--   0 runner    (1001) docker     (123)    12339 2023-04-06 10:47:03.000000 posym-0.5.0/posym/ir_tables.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 10:47:14.377541 posym-0.5.0/posym/operations/
--rw-r--r--   0 runner    (1001) docker     (123)     4537 2023-04-06 10:47:03.000000 posym-0.5.0/posym/operations/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     1346 2023-04-06 10:47:03.000000 posym-0.5.0/posym/operations/identity.py
--rw-r--r--   0 runner    (1001) docker     (123)     2810 2023-04-06 10:47:03.000000 posym-0.5.0/posym/operations/inversion.py
--rw-r--r--   0 runner    (1001) docker     (123)     6006 2023-04-06 10:47:03.000000 posym-0.5.0/posym/operations/irotation.py
--rw-r--r--   0 runner    (1001) docker     (123)     3693 2023-04-06 10:47:03.000000 posym-0.5.0/posym/operations/reflection.py
--rw-r--r--   0 runner    (1001) docker     (123)     5386 2023-04-06 10:47:03.000000 posym-0.5.0/posym/operations/rotation.py
--rw-r--r--   0 runner    (1001) docker     (123)     3001 2023-04-06 10:47:03.000000 posym-0.5.0/posym/pointgroup.py
--rw-r--r--   0 runner    (1001) docker     (123)     6114 2023-04-06 10:47:03.000000 posym-0.5.0/posym/tools.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 10:47:14.377541 posym-0.5.0/posym.egg-info/
--rw-r--r--   0 runner    (1001) docker     (123)    13717 2023-04-06 10:47:14.000000 posym-0.5.0/posym.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)      508 2023-04-06 10:47:14.000000 posym-0.5.0/posym.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-06 10:47:14.000000 posym-0.5.0/posym.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (123)       26 2023-04-06 10:47:14.000000 posym-0.5.0/posym.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (123)        6 2023-04-06 10:47:14.000000 posym-0.5.0/posym.egg-info/top_level.txt
--rw-r--r--   0 runner    (1001) docker     (123)       38 2023-04-06 10:47:14.377541 posym-0.5.0/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (123)     1846 2023-04-06 10:47:03.000000 posym-0.5.0/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 15:56:37.560892 posym-0.5.1/
+-rw-r--r--   0 runner    (1001) docker     (123)     1070 2023-04-06 15:56:28.000000 posym-0.5.1/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (123)    13717 2023-04-06 15:56:37.560892 posym-0.5.1/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)    13452 2023-04-06 15:56:28.000000 posym-0.5.1/README.md
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 15:56:37.560892 posym-0.5.1/c/
+-rw-r--r--   0 runner    (1001) docker     (123)    12679 2023-04-06 15:56:28.000000 posym-0.5.1/c/integrals.c
+-rw-r--r--   0 runner    (1001) docker     (123)     7282 2023-04-06 15:56:28.000000 posym-0.5.1/c/permutations.c
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 15:56:37.560892 posym-0.5.1/posym/
+-rw-r--r--   0 runner    (1001) docker     (123)    27405 2023-04-06 15:56:28.000000 posym-0.5.1/posym/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      972 2023-04-06 15:56:28.000000 posym-0.5.1/posym/algebra.py
+-rw-r--r--   0 runner    (1001) docker     (123)    30004 2023-04-06 15:56:28.000000 posym-0.5.1/posym/basis.py
+-rw-r--r--   0 runner    (1001) docker     (123)    28249 2023-04-06 15:56:28.000000 posym-0.5.1/posym/generate_tables.py
+-rw-r--r--   0 runner    (1001) docker     (123)    12339 2023-04-06 15:56:28.000000 posym-0.5.1/posym/ir_tables.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 15:56:37.560892 posym-0.5.1/posym/operations/
+-rw-r--r--   0 runner    (1001) docker     (123)     4537 2023-04-06 15:56:28.000000 posym-0.5.1/posym/operations/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1346 2023-04-06 15:56:28.000000 posym-0.5.1/posym/operations/identity.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2810 2023-04-06 15:56:28.000000 posym-0.5.1/posym/operations/inversion.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6006 2023-04-06 15:56:28.000000 posym-0.5.1/posym/operations/irotation.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3693 2023-04-06 15:56:28.000000 posym-0.5.1/posym/operations/reflection.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5386 2023-04-06 15:56:28.000000 posym-0.5.1/posym/operations/rotation.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3001 2023-04-06 15:56:28.000000 posym-0.5.1/posym/pointgroup.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6114 2023-04-06 15:56:28.000000 posym-0.5.1/posym/tools.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 15:56:37.560892 posym-0.5.1/posym.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)    13717 2023-04-06 15:56:37.000000 posym-0.5.1/posym.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)      508 2023-04-06 15:56:37.000000 posym-0.5.1/posym.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-06 15:56:37.000000 posym-0.5.1/posym.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       26 2023-04-06 15:56:37.000000 posym-0.5.1/posym.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        6 2023-04-06 15:56:37.000000 posym-0.5.1/posym.egg-info/top_level.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       38 2023-04-06 15:56:37.560892 posym-0.5.1/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (123)     1846 2023-04-06 15:56:28.000000 posym-0.5.1/setup.py
```

### Comparing `posym-0.5.0/LICENSE` & `posym-0.5.1/LICENSE`

 * *Files identical despite different names*

### Comparing `posym-0.5.0/PKG-INFO` & `posym-0.5.1/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: posym
-Version: 0.5.0
+Version: 0.5.1
 Summary: posym module
 Home-page: https://github.com/abelcarreras/posym
 Author: Abel Carreras
 Author-email: abelcarreras83@gmail.com
 License: MIT License
 Description-Content-Type: text/markdown
 License-File: LICENSE
```

### Comparing `posym-0.5.0/README.md` & `posym-0.5.1/README.md`

 * *Files identical despite different names*

### Comparing `posym-0.5.0/c/integrals.c` & `posym-0.5.1/c/integrals.c`

 * *Files identical despite different names*

### Comparing `posym-0.5.0/c/permutations.c` & `posym-0.5.1/c/permutations.c`

 * *Files identical despite different names*

### Comparing `posym-0.5.0/posym/__init__.py` & `posym-0.5.1/posym/__init__.py`

 * *Files 2% similar despite different names*

```diff
@@ -1,9 +1,9 @@
 __author__ = 'Abel Carreras'
-__version__ = '0.5.0'
+__version__ = '0.5.1'
 
 from posym.tools import list_round
 from posym.pointgroup import PointGroup
 from posym.basis import BasisFunction
 from scipy.spatial.transform import Rotation as R
 from scipy.optimize import minimize, basinhopping
 import numpy as np
@@ -206,15 +206,15 @@
             # definition group measure
             return -np.sum(coor_measures)
 
         optimization_function = optimization_function_simple if fast_optimization else optimization_function_full
 
         # preliminary scan
         guess_angles = ref_value = None
-        for angles in itertools.product(np.arange(0, 180, 10), np.arange(0, 180, 10), np.arange(0, 180, 10)):
+        for angles in itertools.product(np.arange(-90, 100, 10), np.arange(-90, 100, 10), np.arange(-90, 100, 10)):
             value = optimization_function(angles)
             if ref_value is None or value < ref_value:
                 ref_value = value
                 guess_angles = angles
 
         result = minimize(optimization_function, guess_angles, method='CG',)
 
@@ -231,25 +231,33 @@
                 sub_operation = copy.deepcopy(sub_operation)
                 sub_operation.apply_rotation(rotmol)
                 operations_list.append(sub_operation)
 
         return operations_list
 
     @property
+    def measure(self):
+        return 100*(1-self.get_ir_representation().values[0])
+
+    @property
     def measure_pos(self):
 
         rotmol = R.from_euler('zyx', self._angles, degrees=True)
 
-        coor_measures = []
+        operator_measures = []
         for operation in self._pg.operations:
-            for sub_operation in self._pg.get_sub_operations(operation.label):
-                coor_m = sub_operation.get_measure_pos(self._coordinates, self._symbols, orientation=rotmol)
-                coor_measures.append(coor_m)
+            sub_operator_measures = []
+            for op in self._pg.get_sub_operations(operation.label):
+                overlap = op.get_measure_pos(self._coordinates, self._symbols, orientation=rotmol)
+                sub_operator_measures.append(overlap)
+            operator_measures.append(np.average(sub_operator_measures))
+
+        ir_rep = np.dot(self._pg.trans_matrix_inv, operator_measures)
 
-        return 1-np.average(coor_measures)
+        return 100 * (1 - ir_rep[0])
 
     @property
     def opt_coordinates(self):
         rotmol = R.from_euler('zyx', self._angles, degrees=True)
         return rotmol.apply(self._coordinates)
 
     @property
```

### Comparing `posym-0.5.0/posym/algebra.py` & `posym-0.5.1/posym/algebra.py`

 * *Files identical despite different names*

### Comparing `posym-0.5.0/posym/basis.py` & `posym-0.5.1/posym/basis.py`

 * *Files identical despite different names*

### Comparing `posym-0.5.0/posym/generate_tables.py` & `posym-0.5.1/posym/generate_tables.py`

 * *Files identical despite different names*

### Comparing `posym-0.5.0/posym/ir_tables.py` & `posym-0.5.1/posym/ir_tables.py`

 * *Files identical despite different names*

### Comparing `posym-0.5.0/posym/operations/__init__.py` & `posym-0.5.1/posym/operations/__init__.py`

 * *Files identical despite different names*

### Comparing `posym-0.5.0/posym/operations/identity.py` & `posym-0.5.1/posym/operations/identity.py`

 * *Files identical despite different names*

### Comparing `posym-0.5.0/posym/operations/inversion.py` & `posym-0.5.1/posym/operations/inversion.py`

 * *Files identical despite different names*

### Comparing `posym-0.5.0/posym/operations/irotation.py` & `posym-0.5.1/posym/operations/irotation.py`

 * *Files identical despite different names*

### Comparing `posym-0.5.0/posym/operations/reflection.py` & `posym-0.5.1/posym/operations/reflection.py`

 * *Files identical despite different names*

### Comparing `posym-0.5.0/posym/operations/rotation.py` & `posym-0.5.1/posym/operations/rotation.py`

 * *Files identical despite different names*

### Comparing `posym-0.5.0/posym/pointgroup.py` & `posym-0.5.1/posym/pointgroup.py`

 * *Files identical despite different names*

### Comparing `posym-0.5.0/posym/tools.py` & `posym-0.5.1/posym/tools.py`

 * *Files identical despite different names*

### Comparing `posym-0.5.0/posym.egg-info/PKG-INFO` & `posym-0.5.1/posym.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: posym
-Version: 0.5.0
+Version: 0.5.1
 Summary: posym module
 Home-page: https://github.com/abelcarreras/posym
 Author: Abel Carreras
 Author-email: abelcarreras83@gmail.com
 License: MIT License
 Description-Content-Type: text/markdown
 License-File: LICENSE
```

### Comparing `posym-0.5.0/setup.py` & `posym-0.5.1/setup.py`

 * *Files identical despite different names*

