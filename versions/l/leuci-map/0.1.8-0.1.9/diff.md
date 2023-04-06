# Comparing `tmp/leuci-map-0.1.8.tar.gz` & `tmp/leuci-map-0.1.9.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "leuci-map-0.1.8.tar", last modified: Thu Mar 16 08:57:21 2023, max compression
+gzip compressed data, was "leuci-map-0.1.9.tar", last modified: Thu Mar 16 09:42:34 2023, max compression
```

## Comparing `leuci-map-0.1.8.tar` & `leuci-map-0.1.9.tar`

### file list

```diff
@@ -1,19 +1,19 @@
-drwxr-xr-x   0 rachel    (1000) rachel    (1000)        0 2023-03-16 08:57:21.386086 leuci-map-0.1.8/
--rw-r--r--   0 rachel    (1000) rachel    (1000)    35149 2023-02-26 19:14:49.000000 leuci-map-0.1.8/LICENSE
--rw-r--r--   0 rachel    (1000) rachel    (1000)      777 2023-03-16 08:57:21.386086 leuci-map-0.1.8/PKG-INFO
--rw-r--r--   0 rachel    (1000) rachel    (1000)      281 2023-02-27 09:58:46.000000 leuci-map-0.1.8/README.md
--rw-r--r--   0 rachel    (1000) rachel    (1000)      104 2023-02-09 09:20:26.000000 leuci-map-0.1.8/pyproject.toml
--rw-r--r--   0 rachel    (1000) rachel    (1000)      621 2023-03-16 08:57:21.396086 leuci-map-0.1.8/setup.cfg
-drwxr-xr-x   0 rachel    (1000) rachel    (1000)        0 2023-03-16 08:57:21.376086 leuci-map-0.1.8/src/
-drwxr-xr-x   0 rachel    (1000) rachel    (1000)        0 2023-03-16 08:57:21.376086 leuci-map-0.1.8/src/leuci_map/
--rw-r--r--   0 rachel    (1000) rachel    (1000)        0 2023-02-09 09:20:26.000000 leuci-map-0.1.8/src/leuci_map/__init__.py
--rw-r--r--   0 rachel    (1000) rachel    (1000)     1104 2023-02-09 09:20:26.000000 leuci-map-0.1.8/src/leuci_map/atom.py
--rw-r--r--   0 rachel    (1000) rachel    (1000)     3770 2023-03-15 10:08:46.000000 leuci-map-0.1.8/src/leuci_map/mapfunctions.py
--rw-r--r--   0 rachel    (1000) rachel    (1000)    14407 2023-03-15 23:22:07.000000 leuci-map-0.1.8/src/leuci_map/maploader.py
--rw-r--r--   0 rachel    (1000) rachel    (1000)     2463 2023-03-15 23:05:44.000000 leuci-map-0.1.8/src/leuci_map/mapobject.py
--rw-r--r--   0 rachel    (1000) rachel    (1000)     3903 2023-03-02 13:00:35.000000 leuci-map-0.1.8/src/leuci_map/pdbobject.py
-drwxr-xr-x   0 rachel    (1000) rachel    (1000)        0 2023-03-16 08:57:21.386086 leuci-map-0.1.8/src/leuci_map.egg-info/
--rw-r--r--   0 rachel    (1000) rachel    (1000)      777 2023-03-16 08:57:21.000000 leuci-map-0.1.8/src/leuci_map.egg-info/PKG-INFO
--rw-r--r--   0 rachel    (1000) rachel    (1000)      349 2023-03-16 08:57:21.000000 leuci-map-0.1.8/src/leuci_map.egg-info/SOURCES.txt
--rw-r--r--   0 rachel    (1000) rachel    (1000)        1 2023-03-16 08:57:21.000000 leuci-map-0.1.8/src/leuci_map.egg-info/dependency_links.txt
--rw-r--r--   0 rachel    (1000) rachel    (1000)       10 2023-03-16 08:57:21.000000 leuci-map-0.1.8/src/leuci_map.egg-info/top_level.txt
+drwxr-xr-x   0 rachel    (1000) rachel    (1000)        0 2023-03-16 09:42:34.575686 leuci-map-0.1.9/
+-rw-r--r--   0 rachel    (1000) rachel    (1000)    35149 2023-02-26 19:14:49.000000 leuci-map-0.1.9/LICENSE
+-rw-r--r--   0 rachel    (1000) rachel    (1000)      777 2023-03-16 09:42:34.575686 leuci-map-0.1.9/PKG-INFO
+-rw-r--r--   0 rachel    (1000) rachel    (1000)      281 2023-02-27 09:58:46.000000 leuci-map-0.1.9/README.md
+-rw-r--r--   0 rachel    (1000) rachel    (1000)      104 2023-02-09 09:20:26.000000 leuci-map-0.1.9/pyproject.toml
+-rw-r--r--   0 rachel    (1000) rachel    (1000)      621 2023-03-16 09:42:34.575686 leuci-map-0.1.9/setup.cfg
+drwxr-xr-x   0 rachel    (1000) rachel    (1000)        0 2023-03-16 09:42:34.565686 leuci-map-0.1.9/src/
+drwxr-xr-x   0 rachel    (1000) rachel    (1000)        0 2023-03-16 09:42:34.565686 leuci-map-0.1.9/src/leuci_map/
+-rw-r--r--   0 rachel    (1000) rachel    (1000)        0 2023-02-09 09:20:26.000000 leuci-map-0.1.9/src/leuci_map/__init__.py
+-rw-r--r--   0 rachel    (1000) rachel    (1000)     1104 2023-02-09 09:20:26.000000 leuci-map-0.1.9/src/leuci_map/atom.py
+-rw-r--r--   0 rachel    (1000) rachel    (1000)     4074 2023-03-16 09:38:58.000000 leuci-map-0.1.9/src/leuci_map/mapfunctions.py
+-rw-r--r--   0 rachel    (1000) rachel    (1000)    14407 2023-03-15 23:22:07.000000 leuci-map-0.1.9/src/leuci_map/maploader.py
+-rw-r--r--   0 rachel    (1000) rachel    (1000)     2463 2023-03-15 23:05:44.000000 leuci-map-0.1.9/src/leuci_map/mapobject.py
+-rw-r--r--   0 rachel    (1000) rachel    (1000)     3903 2023-03-02 13:00:35.000000 leuci-map-0.1.9/src/leuci_map/pdbobject.py
+drwxr-xr-x   0 rachel    (1000) rachel    (1000)        0 2023-03-16 09:42:34.565686 leuci-map-0.1.9/src/leuci_map.egg-info/
+-rw-r--r--   0 rachel    (1000) rachel    (1000)      777 2023-03-16 09:42:34.000000 leuci-map-0.1.9/src/leuci_map.egg-info/PKG-INFO
+-rw-r--r--   0 rachel    (1000) rachel    (1000)      349 2023-03-16 09:42:34.000000 leuci-map-0.1.9/src/leuci_map.egg-info/SOURCES.txt
+-rw-r--r--   0 rachel    (1000) rachel    (1000)        1 2023-03-16 09:42:34.000000 leuci-map-0.1.9/src/leuci_map.egg-info/dependency_links.txt
+-rw-r--r--   0 rachel    (1000) rachel    (1000)       10 2023-03-16 09:42:34.000000 leuci-map-0.1.9/src/leuci_map.egg-info/top_level.txt
```

### Comparing `leuci-map-0.1.8/LICENSE` & `leuci-map-0.1.9/LICENSE`

 * *Files identical despite different names*

### Comparing `leuci-map-0.1.8/PKG-INFO` & `leuci-map-0.1.9/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: leuci-map
-Version: 0.1.8
+Version: 0.1.9
 Summary: density maps library
 Home-page: https://github.com/pypa/sampleproject
 Author: Rachel Alcraft
 Author-email: rachelalcraft@gmail.com
 Project-URL: Bug Tracker, https://github.com/pypa/sampleproject/issues
 Classifier: Programming Language :: Python :: 3
 Classifier: License :: OSI Approved :: MIT License
```

### Comparing `leuci-map-0.1.8/setup.cfg` & `leuci-map-0.1.9/setup.cfg`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 [metadata]
 name = leuci-map
-version = 0.1.8
+version = 0.1.9
 author = Rachel Alcraft
 author_email = rachelalcraft@gmail.com
 description = density maps library
 long_description = file: README.md
 long_description_content_type = text/markdown
 url = https://github.com/pypa/sampleproject
 project_urls =
```

### Comparing `leuci-map-0.1.8/src/leuci_map/atom.py` & `leuci-map-0.1.9/src/leuci_map/atom.py`

 * *Files identical despite different names*

### Comparing `leuci-map-0.1.8/src/leuci_map/mapfunctions.py` & `leuci-map-0.1.9/src/leuci_map/mapfunctions.py`

 * *Files 6% similar despite different names*

```diff
@@ -30,26 +30,28 @@
         map2crs =  [int(self.mobj.map_header["17_MAPC"])-1,int(self.mobj.map_header["18_MAPR"])-1,int(self.mobj.map_header["19_MAPS"])-1]
         cell_dims = [float(self.mobj.map_header["11_X_length"]),float(self.mobj.map_header["12_Y_length"]),float(self.mobj.map_header["13_Z_length"])]
         angles =  [float(self.mobj.map_header["14_Alpha"]),float(self.mobj.map_header["15_Beta"]),float(self.mobj.map_header["16_Gamma"])]
         self.crs_spc = crs.CrsTransform(dim_order, crs_starts, axis_sampling, map2crs, cell_dims, angles)        
         
     def get_slice(self,central, linear, planar, width, samples, interp_method, deriv=0, fo=2,fc=-1,log_level=0):
         # change interpolator if necessary
-        if self.interp_method != interp_method or (self.fo != fo or self.fc != fc and self.mobj.diff_values != []):            
+        if self.interp_method != interp_method and self.mobj.diff_values == []:#then the method has changed but it is em with no diffs
+            self.interper = pol.create_interpolator(interp_method,self.main_interper_vals,self.mobj.F,self.mobj.M,self.mobj.S,log_level=log_level)
+        elif self.interp_method != interp_method or (self.fo != fo or self.fc != fc and self.mobj.diff_values != []):            
             if self.mobj.diff_values != []: #we can't change the fo and fc if thee is no diff
                 interper_vals = []
                 vs, ds = 0,0
                 vs, ds = fo, -1 * fo                
                 vs = vs + fc
                 ds = ds + (-2 * fc)
                 if log_level > 0:
                     print("New interper, Fos=",fo,"Fcs=",fc,"mains=",vs,"diffs=",ds)
                 for i in range(len(self.mobj.values)):
                     interper_vals.append(vs*self.mobj.values[i] + ds*self.mobj.diff_values[i])
-                self.interper = pol.create_interpolator(interp_method,interper_vals,self.mobj.F,self.mobj.M,self.mobj.S)
+                self.interper = pol.create_interpolator(interp_method,interper_vals,self.mobj.F,self.mobj.M,self.mobj.S,log_level=log_level)
                 self.interp_method = interp_method
                 self.fo = fo
                 self.fc = fc
         
         #############        
         # objects needed
         spc = space.SpaceTransform(central, linear, planar)
```

### Comparing `leuci-map-0.1.8/src/leuci_map/maploader.py` & `leuci-map-0.1.9/src/leuci_map/maploader.py`

 * *Files identical despite different names*

### Comparing `leuci-map-0.1.8/src/leuci_map/mapobject.py` & `leuci-map-0.1.9/src/leuci_map/mapobject.py`

 * *Files identical despite different names*

### Comparing `leuci-map-0.1.8/src/leuci_map/pdbobject.py` & `leuci-map-0.1.9/src/leuci_map/pdbobject.py`

 * *Files identical despite different names*

### Comparing `leuci-map-0.1.8/src/leuci_map.egg-info/PKG-INFO` & `leuci-map-0.1.9/src/leuci_map.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: leuci-map
-Version: 0.1.8
+Version: 0.1.9
 Summary: density maps library
 Home-page: https://github.com/pypa/sampleproject
 Author: Rachel Alcraft
 Author-email: rachelalcraft@gmail.com
 Project-URL: Bug Tracker, https://github.com/pypa/sampleproject/issues
 Classifier: Programming Language :: Python :: 3
 Classifier: License :: OSI Approved :: MIT License
```

