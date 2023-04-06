# Comparing `tmp/element-interface-0.5.0.tar.gz` & `tmp/element-interface-0.5.1.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "element-interface-0.5.0.tar", last modified: Thu Jan 12 19:44:17 2023, max compression
+gzip compressed data, was "element-interface-0.5.1.tar", last modified: Thu Apr  6 22:04:21 2023, max compression
```

## Comparing `element-interface-0.5.0.tar` & `element-interface-0.5.1.tar`

### file list

```diff
@@ -1,25 +1,25 @@
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-12 19:44:17.417340 element-interface-0.5.0/
--rw-r--r--   0 runner    (1001) docker     (123)     1072 2023-01-12 19:44:12.000000 element-interface-0.5.0/LICENSE
--rw-r--r--   0 runner    (1001) docker     (123)     1025 2023-01-12 19:44:17.417340 element-interface-0.5.0/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)      630 2023-01-12 19:44:12.000000 element-interface-0.5.0/README.md
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-12 19:44:17.413340 element-interface-0.5.0/element_interface/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-12 19:44:12.000000 element-interface-0.5.0/element_interface/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    12565 2023-01-12 19:44:12.000000 element-interface-0.5.0/element_interface/caiman_loader.py
--rw-r--r--   0 runner    (1001) docker     (123)     2043 2023-01-12 19:44:12.000000 element-interface-0.5.0/element_interface/dandi.py
--rw-r--r--   0 runner    (1001) docker     (123)     1945 2023-01-12 19:44:12.000000 element-interface-0.5.0/element_interface/extract_loader.py
--rw-r--r--   0 runner    (1001) docker     (123)     2596 2023-01-12 19:44:12.000000 element-interface-0.5.0/element_interface/extract_trigger.py
--rw-r--r--   0 runner    (1001) docker     (123)     5803 2023-01-12 19:44:12.000000 element-interface-0.5.0/element_interface/prairieviewreader.py
--rw-r--r--   0 runner    (1001) docker     (123)     1492 2023-01-12 19:44:12.000000 element-interface-0.5.0/element_interface/run_caiman.py
--rw-r--r--   0 runner    (1001) docker     (123)     1310 2023-01-12 19:44:12.000000 element-interface-0.5.0/element_interface/scanimage_utils.py
--rw-r--r--   0 runner    (1001) docker     (123)     8646 2023-01-12 19:44:12.000000 element-interface-0.5.0/element_interface/suite2p_loader.py
--rw-r--r--   0 runner    (1001) docker     (123)     8626 2023-01-12 19:44:12.000000 element-interface-0.5.0/element_interface/suite2p_trigger.py
--rw-r--r--   0 runner    (1001) docker     (123)     5985 2023-01-12 19:44:12.000000 element-interface-0.5.0/element_interface/utils.py
--rw-r--r--   0 runner    (1001) docker     (123)       46 2023-01-12 19:44:12.000000 element-interface-0.5.0/element_interface/version.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-12 19:44:17.417340 element-interface-0.5.0/element_interface.egg-info/
--rw-r--r--   0 runner    (1001) docker     (123)     1025 2023-01-12 19:44:17.000000 element-interface-0.5.0/element_interface.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)      632 2023-01-12 19:44:17.000000 element-interface-0.5.0/element_interface.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-01-12 19:44:17.000000 element-interface-0.5.0/element_interface.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (123)       12 2023-01-12 19:44:17.000000 element-interface-0.5.0/element_interface.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (123)       18 2023-01-12 19:44:17.000000 element-interface-0.5.0/element_interface.egg-info/top_level.txt
--rw-r--r--   0 runner    (1001) docker     (123)       38 2023-01-12 19:44:17.417340 element-interface-0.5.0/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (123)     1060 2023-01-12 19:44:12.000000 element-interface-0.5.0/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 22:04:21.054083 element-interface-0.5.1/
+-rw-r--r--   0 runner    (1001) docker     (123)     1072 2023-04-06 22:04:18.000000 element-interface-0.5.1/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (123)     1025 2023-04-06 22:04:21.054083 element-interface-0.5.1/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)      630 2023-04-06 22:04:18.000000 element-interface-0.5.1/README.md
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 22:04:21.054083 element-interface-0.5.1/element_interface/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 22:04:18.000000 element-interface-0.5.1/element_interface/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    12565 2023-04-06 22:04:18.000000 element-interface-0.5.1/element_interface/caiman_loader.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2043 2023-04-06 22:04:18.000000 element-interface-0.5.1/element_interface/dandi.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1945 2023-04-06 22:04:18.000000 element-interface-0.5.1/element_interface/extract_loader.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2596 2023-04-06 22:04:18.000000 element-interface-0.5.1/element_interface/extract_trigger.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6741 2023-04-06 22:04:18.000000 element-interface-0.5.1/element_interface/prairieviewreader.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1492 2023-04-06 22:04:18.000000 element-interface-0.5.1/element_interface/run_caiman.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1310 2023-04-06 22:04:18.000000 element-interface-0.5.1/element_interface/scanimage_utils.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8646 2023-04-06 22:04:18.000000 element-interface-0.5.1/element_interface/suite2p_loader.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8626 2023-04-06 22:04:18.000000 element-interface-0.5.1/element_interface/suite2p_trigger.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5985 2023-04-06 22:04:18.000000 element-interface-0.5.1/element_interface/utils.py
+-rw-r--r--   0 runner    (1001) docker     (123)       46 2023-04-06 22:04:18.000000 element-interface-0.5.1/element_interface/version.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 22:04:21.054083 element-interface-0.5.1/element_interface.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)     1025 2023-04-06 22:04:20.000000 element-interface-0.5.1/element_interface.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)      632 2023-04-06 22:04:20.000000 element-interface-0.5.1/element_interface.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-06 22:04:20.000000 element-interface-0.5.1/element_interface.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       12 2023-04-06 22:04:20.000000 element-interface-0.5.1/element_interface.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       18 2023-04-06 22:04:20.000000 element-interface-0.5.1/element_interface.egg-info/top_level.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       38 2023-04-06 22:04:21.054083 element-interface-0.5.1/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (123)     1060 2023-04-06 22:04:18.000000 element-interface-0.5.1/setup.py
```

### Comparing `element-interface-0.5.0/LICENSE` & `element-interface-0.5.1/LICENSE`

 * *Files identical despite different names*

### Comparing `element-interface-0.5.0/PKG-INFO` & `element-interface-0.5.1/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: element-interface
-Version: 0.5.0
+Version: 0.5.1
 Summary: Loaders of neurophysiological data into the DataJoint Elements
 Home-page: https://github.com/datajoint/element-interface
 Author: DataJoint
 Author-email: info@datajoint.com
 License: MIT
 Keywords: neuroscience calcium-imaging science datajoint
 Platform: UNKNOWN
```

### Comparing `element-interface-0.5.0/README.md` & `element-interface-0.5.1/README.md`

 * *Files identical despite different names*

### Comparing `element-interface-0.5.0/element_interface/caiman_loader.py` & `element-interface-0.5.1/element_interface/caiman_loader.py`

 * *Files identical despite different names*

### Comparing `element-interface-0.5.0/element_interface/dandi.py` & `element-interface-0.5.1/element_interface/dandi.py`

 * *Files identical despite different names*

### Comparing `element-interface-0.5.0/element_interface/extract_loader.py` & `element-interface-0.5.1/element_interface/extract_loader.py`

 * *Files identical despite different names*

### Comparing `element-interface-0.5.0/element_interface/extract_trigger.py` & `element-interface-0.5.1/element_interface/extract_trigger.py`

 * *Files identical despite different names*

### Comparing `element-interface-0.5.0/element_interface/prairieviewreader.py` & `element-interface-0.5.1/element_interface/prairieviewreader.py`

 * *Files 17% similar despite different names*

```diff
@@ -38,15 +38,15 @@
             break
     else:
         raise FileNotFoundError(
             f"No PrarieView metadata XML file found at {pvtiffile.parent}"
         )
 
     bidirectional_scan = False  # Does not support bidirectional
-    roi = 1
+    roi = 0
     n_fields = 1  # Always contains 1 field
     record_start_time = root.find(".//Sequence/[@cycle='1']").attrib.get("time")
 
     # Get all channels and find unique values
     channel_list = [
         int(channel.attrib.get("channel"))
         for channel in root.iterfind(".//Sequence/Frame/File/[@channel]")
@@ -111,39 +111,60 @@
         )
         n_depths = 1
         assert z_fields.size == n_depths
         bidirection_z = False
 
     else:
 
-        bidirection_z = bool(root.find(".//Sequence").attrib.get("bidirectionalZ"))
+        bidirection_z = root.find(".//Sequence").attrib.get("bidirectionalZ") == "True"
 
         # One "Frame" per depth. Gets number of frames in first sequence
         planes = [
             int(plane.attrib.get("index"))
             for plane in root.findall(".//Sequence/[@cycle='1']/Frame")
         ]
         n_depths = len(set(planes))
-        z_min = float(
-            root.findall(
-                ".//Sequence/[@cycle='1']/Frame/PVStateShard/PVStateValue/[@key='positionCurrent']/SubindexedValues/SubindexedValue/[@subindex='0']"
-            )[0].attrib.get("value")
-        )
-        z_max = float(
-            root.findall(
-                ".//Sequence/[@cycle='1']/Frame/PVStateShard/PVStateValue/[@key='positionCurrent']/SubindexedValues/SubindexedValue/[@subindex='0']"
-            )[-1].attrib.get("value")
-        )
-        z_step = float(
-            root.find(
-                ".//PVStateShard/PVStateValue/[@key='micronsPerPixel']/IndexedValue/[@index='ZAxis']"
-            ).attrib.get("value")
+
+        z_controllers = root.findall(
+            ".//Sequence/[@cycle='1']/Frame/[@index='1']/PVStateShard/PVStateValue/[@key='positionCurrent']/SubindexedValues/[@index='ZAxis']/SubindexedValue"
         )
-        z_fields = np.arange(z_min, z_max + 1, z_step)
-        assert z_fields.size == n_depths
+        if len(z_controllers) > 1:
+
+            z_repeats = []
+            for controller in root.findall(
+                ".//Sequence/[@cycle='1']/Frame/[@index='1']/PVStateShard/PVStateValue/[@key='positionCurrent']/SubindexedValues/[@index='ZAxis']/"):
+                z_repeats.append(
+                    [
+                        float(z.attrib.get("value"))
+                        for z in root.findall(
+                            ".//Sequence/[@cycle='1']/Frame/PVStateShard/PVStateValue/[@key='positionCurrent']/SubindexedValues/[@index='ZAxis']/SubindexedValue/[@subindex='{0}']".format(
+                                controller.attrib.get("subindex")
+                            )
+                        )
+                    ]
+                )
+    
+
+            controller_assert = [not all(z == z_controller[0] for z in z_controller) for z_controller in z_repeats]
+
+            assert sum(controller_assert)==1, "Multiple controllers changing z depth is not supported"
+
+            z_fields = z_repeats[controller_assert.index(True)]
+            
+        else:
+            z_fields = [
+                z.attrib.get("value")
+                for z in root.findall(
+                    ".//Sequence/[@cycle='1']/Frame/PVStateShard/PVStateValue/[@key='positionCurrent']/SubindexedValues/[@index='ZAxis']/SubindexedValue/[@subindex='0']"
+                )
+            ]
+
+        assert (
+            len(z_fields) == n_depths
+        ), "Number of z fields does not match number of depths."
 
     metainfo = dict(
         num_fields=n_fields,
         num_channels=n_channels,
         num_planes=n_depths,
         num_frames=n_frames,
         num_rois=roi,
```

### Comparing `element-interface-0.5.0/element_interface/run_caiman.py` & `element-interface-0.5.1/element_interface/run_caiman.py`

 * *Files identical despite different names*

### Comparing `element-interface-0.5.0/element_interface/scanimage_utils.py` & `element-interface-0.5.1/element_interface/scanimage_utils.py`

 * *Files identical despite different names*

### Comparing `element-interface-0.5.0/element_interface/suite2p_loader.py` & `element-interface-0.5.1/element_interface/suite2p_loader.py`

 * *Files identical despite different names*

### Comparing `element-interface-0.5.0/element_interface/suite2p_trigger.py` & `element-interface-0.5.1/element_interface/suite2p_trigger.py`

 * *Files identical despite different names*

### Comparing `element-interface-0.5.0/element_interface/utils.py` & `element-interface-0.5.1/element_interface/utils.py`

 * *Files identical despite different names*

### Comparing `element-interface-0.5.0/element_interface.egg-info/PKG-INFO` & `element-interface-0.5.1/element_interface.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: element-interface
-Version: 0.5.0
+Version: 0.5.1
 Summary: Loaders of neurophysiological data into the DataJoint Elements
 Home-page: https://github.com/datajoint/element-interface
 Author: DataJoint
 Author-email: info@datajoint.com
 License: MIT
 Keywords: neuroscience calcium-imaging science datajoint
 Platform: UNKNOWN
```

### Comparing `element-interface-0.5.0/element_interface.egg-info/SOURCES.txt` & `element-interface-0.5.1/element_interface.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `element-interface-0.5.0/setup.py` & `element-interface-0.5.1/setup.py`

 * *Files identical despite different names*

