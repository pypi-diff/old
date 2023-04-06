# Comparing `tmp/python_roborock-0.5.5.tar.gz` & `tmp/python_roborock-0.5.6.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "python_roborock-0.5.5.tar", max compression
+gzip compressed data, was "python_roborock-0.5.6.tar", max compression
```

## Comparing `python_roborock-0.5.5.tar` & `python_roborock-0.5.6.tar`

### file list

```diff
@@ -1,17 +1,17 @@
--rw-r--r--   0        0        0    35149 2023-04-06 03:25:06.692551 python_roborock-0.5.5/LICENSE
--rw-r--r--   0        0        0     2221 2023-04-06 03:25:06.692551 python_roborock-0.5.5/README.md
--rw-r--r--   0        0        0     1175 2023-04-06 03:25:07.568556 python_roborock-0.5.5/pyproject.toml
--rw-r--r--   0        0        0      300 2023-04-06 03:25:06.692551 python_roborock-0.5.5/roborock/__init__.py
--rw-r--r--   0        0        0    17099 2023-04-06 03:25:06.692551 python_roborock-0.5.5/roborock/api.py
--rw-r--r--   0        0        0     3957 2023-04-06 03:25:06.692551 python_roborock-0.5.5/roborock/cli.py
--rw-r--r--   0        0        0     8276 2023-04-06 03:25:06.692551 python_roborock-0.5.5/roborock/cloud_api.py
--rw-r--r--   0        0        0     3230 2023-04-06 03:25:06.692551 python_roborock-0.5.5/roborock/code_mappings.py
--rw-r--r--   0        0        0     8866 2023-04-06 03:25:06.692551 python_roborock-0.5.5/roborock/containers.py
--rw-r--r--   0        0        0     1022 2023-04-06 03:25:06.692551 python_roborock-0.5.5/roborock/exceptions.py
--rw-r--r--   0        0        0     7030 2023-04-06 03:25:06.692551 python_roborock-0.5.5/roborock/local_api.py
--rw-r--r--   0        0        0     1194 2023-04-06 03:25:06.692551 python_roborock-0.5.5/roborock/offline/offline.py
--rw-r--r--   0        0        0     6030 2023-04-06 03:25:06.692551 python_roborock-0.5.5/roborock/roborock_message.py
--rw-r--r--   0        0        0      644 2023-04-06 03:25:06.692551 python_roborock-0.5.5/roborock/roborock_queue.py
--rw-r--r--   0        0        0    12471 2023-04-06 03:25:06.692551 python_roborock-0.5.5/roborock/typing.py
--rw-r--r--   0        0        0      809 2023-04-06 03:25:06.692551 python_roborock-0.5.5/roborock/util.py
--rw-r--r--   0        0        0     3348 1970-01-01 00:00:00.000000 python_roborock-0.5.5/PKG-INFO
+-rw-r--r--   0        0        0    35149 2023-04-06 21:27:56.651006 python_roborock-0.5.6/LICENSE
+-rw-r--r--   0        0        0     2221 2023-04-06 21:27:56.651006 python_roborock-0.5.6/README.md
+-rw-r--r--   0        0        0     1175 2023-04-06 21:27:57.451013 python_roborock-0.5.6/pyproject.toml
+-rw-r--r--   0        0        0      300 2023-04-06 21:27:56.651006 python_roborock-0.5.6/roborock/__init__.py
+-rw-r--r--   0        0        0    17099 2023-04-06 21:27:56.651006 python_roborock-0.5.6/roborock/api.py
+-rw-r--r--   0        0        0     3957 2023-04-06 21:27:56.651006 python_roborock-0.5.6/roborock/cli.py
+-rw-r--r--   0        0        0     8276 2023-04-06 21:27:56.651006 python_roborock-0.5.6/roborock/cloud_api.py
+-rw-r--r--   0        0        0     3704 2023-04-06 21:27:56.651006 python_roborock-0.5.6/roborock/code_mappings.py
+-rw-r--r--   0        0        0     8866 2023-04-06 21:27:56.651006 python_roborock-0.5.6/roborock/containers.py
+-rw-r--r--   0        0        0     1022 2023-04-06 21:27:56.651006 python_roborock-0.5.6/roborock/exceptions.py
+-rw-r--r--   0        0        0     7030 2023-04-06 21:27:56.651006 python_roborock-0.5.6/roborock/local_api.py
+-rw-r--r--   0        0        0     1194 2023-04-06 21:27:56.651006 python_roborock-0.5.6/roborock/offline/offline.py
+-rw-r--r--   0        0        0     6030 2023-04-06 21:27:56.651006 python_roborock-0.5.6/roborock/roborock_message.py
+-rw-r--r--   0        0        0      644 2023-04-06 21:27:56.651006 python_roborock-0.5.6/roborock/roborock_queue.py
+-rw-r--r--   0        0        0    12471 2023-04-06 21:27:56.651006 python_roborock-0.5.6/roborock/typing.py
+-rw-r--r--   0        0        0      809 2023-04-06 21:27:56.651006 python_roborock-0.5.6/roborock/util.py
+-rw-r--r--   0        0        0     3348 1970-01-01 00:00:00.000000 python_roborock-0.5.6/PKG-INFO
```

### Comparing `python_roborock-0.5.5/LICENSE` & `python_roborock-0.5.6/LICENSE`

 * *Files identical despite different names*

### Comparing `python_roborock-0.5.5/README.md` & `python_roborock-0.5.6/README.md`

 * *Files identical despite different names*

### Comparing `python_roborock-0.5.5/pyproject.toml` & `python_roborock-0.5.6/pyproject.toml`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 [tool.poetry]
 name = "python-roborock"
-version = "0.5.5"
+version = "0.5.6"
 description = "A package to control Roborock vacuums."
 authors = ["humbertogontijo <humbertogontijo@users.noreply.github.com>"]
 license = "GPL-3.0-only"
 readme = "README.md"
 repository = "https://github.com/humbertogontijo/python-roborock"
 classifiers = [
     "Development Status :: 5 - Production/Stable",
```

### Comparing `python_roborock-0.5.5/roborock/api.py` & `python_roborock-0.5.6/roborock/api.py`

 * *Files identical despite different names*

### Comparing `python_roborock-0.5.5/roborock/cli.py` & `python_roborock-0.5.6/roborock/cli.py`

 * *Files identical despite different names*

### Comparing `python_roborock-0.5.5/roborock/cloud_api.py` & `python_roborock-0.5.6/roborock/cloud_api.py`

 * *Files identical despite different names*

### Comparing `python_roborock-0.5.5/roborock/code_mappings.py` & `python_roborock-0.5.6/roborock/code_mappings.py`

 * *Files 18% similar despite different names*

```diff
@@ -1,14 +1,13 @@
 from __future__ import annotations
 
 from enum import Enum
 
 
 class RoborockEnum(str, Enum):
-
     def __str__(self):
         return str(self.value)
 
     @classmethod
     def _missing_(cls, code: int):
         return cls._member_map_.get(str(code))
 
@@ -25,117 +24,142 @@
         return list(cls.as_dict().keys())
 
     @classmethod
     def items(cls):
         return cls.as_dict().items()
 
 
-class RoborockCode:
-
-    def __new__(cls, name: str, data: dict):
-        return RoborockEnum(name, {str(key): value for key, value in data.items()})
+def create_code_enum(name: str, data: dict) -> RoborockEnum:
+    return RoborockEnum(name, {str(key): value for key, value in data.items()})
 
 
-RoborockStateCode = RoborockCode("RoborockStateCode", {
-    1: "starting",
-    2: "charger_disconnected",
-    3: "idle",
-    4: "remote_control_active",
-    5: "cleaning",
-    6: "returning_home",
-    7: "manual_mode",
-    8: "charging",
-    9: "charging_problem",
-    10: "paused",
-    11: "spot_cleaning",
-    12: "error",
-    13: "shutting_down",
-    14: "updating",
-    15: "docking",
-    16: "going_to_target",
-    17: "zoned_cleaning",
-    18: "segment_cleaning",
-    22: "emptying_the_bin",  # on s7+, see #1189
-    23: "washing_the_mop",  # on a46, #1435
-    26: "going_to_wash_the_mop",  # on a46, #1435
-    100: "charging_complete",
-    101: "device_offline",
-})
-
-RoborockErrorCode = RoborockCode("RoborockErrorCode", {
-    0: "none",
-    1: "lidar_blocked",
-    2: "bumper_stuck",
-    3: "wheels_suspended",
-    4: "cliff_sensor_error",
-    5: "main_brush_jammed",
-    6: "side_brush_jammed",
-    7: "wheels_jammed",
-    8: "robot_trapped",
-    9: "no_dustbin",
-    12: "low_battery",
-    13: "charging_error",
-    14: "battery_error",
-    15: "wall_sensor_dirty",
-    16: "robot_tilted",
-    17: "side_brush_error",
-    18: "fan_error",
-    21: "vertical_bumper_pressed",
-    22: "dock_locator_error",
-    23: "return_to_dock_fail",
-    24: "no-go_zone_detected",
-    27: "vibrarise_jammed",
-    28: "robot_on_carpet",
-    29: "filter_blocked",
-    30: "invisible_wall_detected",
-    31: "cannot_cross_carpet",
-    32: "internal_error"
-})
-
-RoborockFanPowerCode = RoborockCode("RoborockFanPowerCode", {
-    105: "off",
-    101: "silent",
-    102: "balanced",
-    103: "turbo",
-    104: "max",
-    108: "max_plus",
-    106: "custom",
-})
-
-RoborockMopModeCode = RoborockCode("RoborockMopModeCode", {
-    300: "standard",
-    301: "deep",
-    303: "deep_plus",
-    302: "custom",
-})
-
-RoborockMopIntensityCode = RoborockCode("RoborockMopIntensityCode", {
-    200: "off",
-    201: "mild",
-    202: "moderate",
-    203: "intense",
-    204: "custom",
-})
-
-RoborockDockErrorCode = RoborockCode("RoborockDockErrorCode", {
-    0: "ok",
-    38: 'water empty',
-    39: 'waste water tank full',
-})
-
-RoborockDockTypeCode = RoborockCode("RoborockDockTypeCode", {
-    0: "no_dock",
-    3: "empty_wash_fill_dock",
-})
-
-RoborockDockDustCollectionModeCode = RoborockCode("RoborockDockDustCollectionModeCode", {
-    0: "smart",
-    1: "light",
-    2: "balanced",
-    4: "max",
-})
-
-RoborockDockWashTowelModeCode = RoborockCode("RoborockDockWashTowelModeCode", {
-    0: "light",
-    1: "balanced",
-    2: "deep",
-})
+RoborockStateCode = create_code_enum(
+    "RoborockStateCode",
+    {
+        1: "starting",
+        2: "charger_disconnected",
+        3: "idle",
+        4: "remote_control_active",
+        5: "cleaning",
+        6: "returning_home",
+        7: "manual_mode",
+        8: "charging",
+        9: "charging_problem",
+        10: "paused",
+        11: "spot_cleaning",
+        12: "error",
+        13: "shutting_down",
+        14: "updating",
+        15: "docking",
+        16: "going_to_target",
+        17: "zoned_cleaning",
+        18: "segment_cleaning",
+        22: "emptying_the_bin",  # on s7+, see #1189
+        23: "washing_the_mop",  # on a46, #1435
+        26: "going_to_wash_the_mop",  # on a46, #1435
+        100: "charging_complete",
+        101: "device_offline",
+    },
+)
+
+RoborockErrorCode = create_code_enum(
+    "RoborockErrorCode",
+    {
+        0: "none",
+        1: "lidar_blocked",
+        2: "bumper_stuck",
+        3: "wheels_suspended",
+        4: "cliff_sensor_error",
+        5: "main_brush_jammed",
+        6: "side_brush_jammed",
+        7: "wheels_jammed",
+        8: "robot_trapped",
+        9: "no_dustbin",
+        12: "low_battery",
+        13: "charging_error",
+        14: "battery_error",
+        15: "wall_sensor_dirty",
+        16: "robot_tilted",
+        17: "side_brush_error",
+        18: "fan_error",
+        21: "vertical_bumper_pressed",
+        22: "dock_locator_error",
+        23: "return_to_dock_fail",
+        24: "no-go_zone_detected",
+        27: "vibrarise_jammed",
+        28: "robot_on_carpet",
+        29: "filter_blocked",
+        30: "invisible_wall_detected",
+        31: "cannot_cross_carpet",
+        32: "internal_error",
+    },
+)
+
+RoborockFanPowerCode = create_code_enum(
+    "RoborockFanPowerCode",
+    {
+        105: "off",
+        101: "silent",
+        102: "balanced",
+        103: "turbo",
+        104: "max",
+        108: "max_plus",
+        106: "custom",
+    },
+)
+
+RoborockMopModeCode = create_code_enum(
+    "RoborockMopModeCode",
+    {
+        300: "standard",
+        301: "deep",
+        303: "deep_plus",
+        302: "custom",
+    },
+)
+
+RoborockMopIntensityCode = create_code_enum(
+    "RoborockMopIntensityCode",
+    {
+        200: "off",
+        201: "mild",
+        202: "moderate",
+        203: "intense",
+        204: "custom",
+    },
+)
+
+RoborockDockErrorCode = create_code_enum(
+    "RoborockDockErrorCode",
+    {
+        0: "ok",
+        38: "water empty",
+        39: "waste water tank full",
+    },
+)
+
+RoborockDockTypeCode = create_code_enum(
+    "RoborockDockTypeCode",
+    {
+        0: "no_dock",
+        3: "empty_wash_fill_dock",
+    },
+)
+
+RoborockDockDustCollectionModeCode = create_code_enum(
+    "RoborockDockDustCollectionModeCode",
+    {
+        0: "smart",
+        1: "light",
+        2: "balanced",
+        4: "max",
+    },
+)
+
+RoborockDockWashTowelModeCode = create_code_enum(
+    "RoborockDockWashTowelModeCode",
+    {
+        0: "light",
+        1: "balanced",
+        2: "deep",
+    },
+)
```

### Comparing `python_roborock-0.5.5/roborock/containers.py` & `python_roborock-0.5.6/roborock/containers.py`

 * *Files identical despite different names*

### Comparing `python_roborock-0.5.5/roborock/exceptions.py` & `python_roborock-0.5.6/roborock/exceptions.py`

 * *Files identical despite different names*

### Comparing `python_roborock-0.5.5/roborock/local_api.py` & `python_roborock-0.5.6/roborock/local_api.py`

 * *Files identical despite different names*

### Comparing `python_roborock-0.5.5/roborock/offline/offline.py` & `python_roborock-0.5.6/roborock/offline/offline.py`

 * *Files identical despite different names*

### Comparing `python_roborock-0.5.5/roborock/roborock_message.py` & `python_roborock-0.5.6/roborock/roborock_message.py`

 * *Files identical despite different names*

### Comparing `python_roborock-0.5.5/roborock/roborock_queue.py` & `python_roborock-0.5.6/roborock/roborock_queue.py`

 * *Files identical despite different names*

### Comparing `python_roborock-0.5.5/roborock/typing.py` & `python_roborock-0.5.6/roborock/typing.py`

 * *Files identical despite different names*

### Comparing `python_roborock-0.5.5/roborock/util.py` & `python_roborock-0.5.6/roborock/util.py`

 * *Files identical despite different names*

### Comparing `python_roborock-0.5.5/PKG-INFO` & `python_roborock-0.5.6/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: python-roborock
-Version: 0.5.5
+Version: 0.5.6
 Summary: A package to control Roborock vacuums.
 Home-page: https://github.com/humbertogontijo/python-roborock
 License: GPL-3.0-only
 Author: humbertogontijo
 Author-email: humbertogontijo@users.noreply.github.com
 Requires-Python: >=3.9,<4.0
 Classifier: Development Status :: 5 - Production/Stable
```

#### html2text {}

```diff
@@ -1,8 +1,8 @@
-Metadata-Version: 2.1 Name: python-roborock Version: 0.5.5 Summary: A package
+Metadata-Version: 2.1 Name: python-roborock Version: 0.5.6 Summary: A package
 to control Roborock vacuums. Home-page: https://github.com/humbertogontijo/
 python-roborock License: GPL-3.0-only Author: humbertogontijo Author-email:
 humbertogontijo@users.noreply.github.com Requires-Python: >=3.9,<4.0
 Classifier: Development Status :: 5 - Production/Stable Classifier: Intended
 Audience :: Developers Classifier: License :: OSI Approved :: GNU General
 Public License v3 (GPLv3) Classifier: Natural Language :: English Classifier:
 Operating System :: OS Independent Classifier: Programming Language :: Python
```

