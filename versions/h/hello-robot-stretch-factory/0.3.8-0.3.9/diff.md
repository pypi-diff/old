# Comparing `tmp/hello_robot_stretch_factory-0.3.8.tar.gz` & `tmp/hello_robot_stretch_factory-0.3.9.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "hello_robot_stretch_factory-0.3.8.tar", last modified: Wed Sep 14 17:04:28 2022, max compression
+gzip compressed data, was "hello_robot_stretch_factory-0.3.9.tar", last modified: Mon Sep 26 23:26:26 2022, max compression
```

## Comparing `hello_robot_stretch_factory-0.3.8.tar` & `hello_robot_stretch_factory-0.3.9.tar`

### file list

```diff
@@ -1,49 +1,49 @@
-drwxrwxr-x   0 hello-robot  (1000) hello-robot  (1000)        0 2022-09-14 17:04:28.537069 hello_robot_stretch_factory-0.3.8/
--rw-rw-r--   0 hello-robot  (1000) hello-robot  (1000)      929 2022-09-14 17:03:07.000000 hello_robot_stretch_factory-0.3.8/LICENSE.md
--rw-rw-r--   0 hello-robot  (1000) hello-robot  (1000)      816 2022-09-14 17:04:28.529069 hello_robot_stretch_factory-0.3.8/PKG-INFO
--rw-rw-r--   0 hello-robot  (1000) hello-robot  (1000)      355 2022-09-14 17:03:07.000000 hello_robot_stretch_factory-0.3.8/README.md
-drwxrwxr-x   0 hello-robot  (1000) hello-robot  (1000)        0 2022-09-14 17:04:28.529069 hello_robot_stretch_factory-0.3.8/hello_robot_stretch_factory.egg-info/
--rw-rw-r--   0 hello-robot  (1000) hello-robot  (1000)      816 2022-09-14 17:04:28.000000 hello_robot_stretch_factory-0.3.8/hello_robot_stretch_factory.egg-info/PKG-INFO
--rw-rw-r--   0 hello-robot  (1000) hello-robot  (1000)     1447 2022-09-14 17:04:28.000000 hello_robot_stretch_factory-0.3.8/hello_robot_stretch_factory.egg-info/SOURCES.txt
--rw-rw-r--   0 hello-robot  (1000) hello-robot  (1000)        1 2022-09-14 17:04:28.000000 hello_robot_stretch_factory-0.3.8/hello_robot_stretch_factory.egg-info/dependency_links.txt
--rw-rw-r--   0 hello-robot  (1000) hello-robot  (1000)       73 2022-09-14 17:04:28.000000 hello_robot_stretch_factory-0.3.8/hello_robot_stretch_factory.egg-info/requires.txt
--rw-rw-r--   0 hello-robot  (1000) hello-robot  (1000)       16 2022-09-14 17:04:28.000000 hello_robot_stretch_factory-0.3.8/hello_robot_stretch_factory.egg-info/top_level.txt
--rw-rw-r--   0 hello-robot  (1000) hello-robot  (1000)       38 2022-09-14 17:04:28.537069 hello_robot_stretch_factory-0.3.8/setup.cfg
--rw-rw-r--   0 hello-robot  (1000) hello-robot  (1000)      935 2022-09-14 17:04:26.000000 hello_robot_stretch_factory-0.3.8/setup.py
-drwxrwxr-x   0 hello-robot  (1000) hello-robot  (1000)        0 2022-09-14 17:04:28.529069 hello_robot_stretch_factory-0.3.8/stretch_factory/
--rw-rw-r--   0 hello-robot  (1000) hello-robot  (1000)        0 2022-09-14 17:03:07.000000 hello_robot_stretch_factory-0.3.8/stretch_factory/__init__.py
--rw-rw-r--   0 hello-robot  (1000) hello-robot  (1000)     5706 2022-09-14 17:03:07.000000 hello_robot_stretch_factory-0.3.8/stretch_factory/device_mgmt.py
--rw-rw-r--   0 hello-robot  (1000) hello-robot  (1000)    38097 2022-09-14 17:03:07.000000 hello_robot_stretch_factory-0.3.8/stretch_factory/firmware_updater.py
--rw-rw-r--   0 hello-robot  (1000) hello-robot  (1000)    15885 2022-09-14 17:03:07.000000 hello_robot_stretch_factory-0.3.8/stretch_factory/hello_device_utils.py
--rw-rw-r--   0 hello-robot  (1000) hello-robot  (1000)    12828 2022-09-14 17:03:07.000000 hello_robot_stretch_factory-0.3.8/stretch_factory/param_mgmt.py
-drwxrwxr-x   0 hello-robot  (1000) hello-robot  (1000)        0 2022-09-14 17:04:28.529069 hello_robot_stretch_factory-0.3.8/test/
--rw-rw-r--   0 hello-robot  (1000) hello-robot  (1000)      685 2022-09-14 17:03:07.000000 hello_robot_stretch_factory-0.3.8/test/test_firmware_updater.py
--rw-rw-r--   0 hello-robot  (1000) hello-robot  (1000)      668 2022-09-14 17:03:07.000000 hello_robot_stretch_factory-0.3.8/test/test_usb_reset.py
-drwxrwxr-x   0 hello-robot  (1000) hello-robot  (1000)        0 2022-09-14 17:04:28.529069 hello_robot_stretch_factory-0.3.8/tools/
--rwxrwxr-x   0 hello-robot  (1000) hello-robot  (1000)     2456 2022-09-14 17:03:07.000000 hello_robot_stretch_factory-0.3.8/tools/RE1_migrate_contacts.py
--rwxrwxr-x   0 hello-robot  (1000) hello-robot  (1000)     6621 2022-09-14 17:03:07.000000 hello_robot_stretch_factory-0.3.8/tools/RE1_migrate_params.py
--rwxrwxr-x   0 hello-robot  (1000) hello-robot  (1000)    21784 2022-09-14 17:03:07.000000 hello_robot_stretch_factory-0.3.8/tools/REx_D435i_check.py
--rwxrwxr-x   0 hello-robot  (1000) hello-robot  (1000)     5418 2022-09-14 17:03:07.000000 hello_robot_stretch_factory-0.3.8/tools/REx_base_calibrate_imu_collect.py
--rwxrwxr-x   0 hello-robot  (1000) hello-robot  (1000)    32027 2022-09-14 17:03:07.000000 hello_robot_stretch_factory-0.3.8/tools/REx_base_calibrate_imu_process.py
--rwxrwxr-x   0 hello-robot  (1000) hello-robot  (1000)     5950 2022-09-14 17:03:07.000000 hello_robot_stretch_factory-0.3.8/tools/REx_base_calibrate_wheel_separation.py
--rwxrwxr-x   0 hello-robot  (1000) hello-robot  (1000)     7224 2022-09-14 17:03:07.000000 hello_robot_stretch_factory-0.3.8/tools/REx_calibrate_guarded_contact.py
--rwxrwxr-x   0 hello-robot  (1000) hello-robot  (1000)     3578 2022-09-14 17:03:07.000000 hello_robot_stretch_factory-0.3.8/tools/REx_calibrate_range.py
--rwxrwxr-x   0 hello-robot  (1000) hello-robot  (1000)     1728 2022-09-14 17:03:07.000000 hello_robot_stretch_factory-0.3.8/tools/REx_cliff_sensor_calibrate.py
--rwxrwxr-x   0 hello-robot  (1000) hello-robot  (1000)     1442 2022-09-14 17:03:07.000000 hello_robot_stretch_factory-0.3.8/tools/REx_dynamixel_id_change.py
--rwxrwxr-x   0 hello-robot  (1000) hello-robot  (1000)     1354 2022-09-14 17:03:07.000000 hello_robot_stretch_factory-0.3.8/tools/REx_dynamixel_id_scan.py
--rwxrwxr-x   0 hello-robot  (1000) hello-robot  (1000)     5045 2022-09-14 17:03:07.000000 hello_robot_stretch_factory-0.3.8/tools/REx_dynamixel_jog.py
--rwxrwxr-x   0 hello-robot  (1000) hello-robot  (1000)     1374 2022-09-14 17:03:07.000000 hello_robot_stretch_factory-0.3.8/tools/REx_dynamixel_reboot.py
--rwxrwxr-x   0 hello-robot  (1000) hello-robot  (1000)     1188 2022-09-14 17:03:07.000000 hello_robot_stretch_factory-0.3.8/tools/REx_dynamixel_set_baud.py
--rwxrwxr-x   0 hello-robot  (1000) hello-robot  (1000)     5331 2022-09-14 17:03:07.000000 hello_robot_stretch_factory-0.3.8/tools/REx_firmware_updater.py
--rwxrwxr-x   0 hello-robot  (1000) hello-robot  (1000)     1583 2022-09-14 17:03:07.000000 hello_robot_stretch_factory-0.3.8/tools/REx_gamepad_configure.py
--rwxrwxr-x   0 hello-robot  (1000) hello-robot  (1000)     2338 2022-09-14 17:03:07.000000 hello_robot_stretch_factory-0.3.8/tools/REx_gripper_calibrate.py
--rwxrwxr-x   0 hello-robot  (1000) hello-robot  (1000)     1947 2022-09-14 17:03:07.000000 hello_robot_stretch_factory-0.3.8/tools/REx_hello_dynamixel_jog.py
--rwxrwxr-x   0 hello-robot  (1000) hello-robot  (1000)      870 2022-09-14 17:03:07.000000 hello_robot_stretch_factory-0.3.8/tools/REx_stepper_calibration_YAML_to_flash.py
--rwxrwxr-x   0 hello-robot  (1000) hello-robot  (1000)      685 2022-09-14 17:03:07.000000 hello_robot_stretch_factory-0.3.8/tools/REx_stepper_calibration_flash_to_YAML.py
--rwxrwxr-x   0 hello-robot  (1000) hello-robot  (1000)     1168 2022-09-14 17:03:07.000000 hello_robot_stretch_factory-0.3.8/tools/REx_stepper_calibration_run.py
--rwxrwxr-x   0 hello-robot  (1000) hello-robot  (1000)    18644 2022-09-14 17:03:07.000000 hello_robot_stretch_factory-0.3.8/tools/REx_stepper_ctrl_tuning.py
--rwxrwxr-x   0 hello-robot  (1000) hello-robot  (1000)     1163 2022-09-14 17:03:07.000000 hello_robot_stretch_factory-0.3.8/tools/REx_stepper_gains.py
--rwxrwxr-x   0 hello-robot  (1000) hello-robot  (1000)     4064 2022-09-14 17:03:07.000000 hello_robot_stretch_factory-0.3.8/tools/REx_stepper_jog.py
--rwxrwxr-x   0 hello-robot  (1000) hello-robot  (1000)      852 2022-09-14 17:03:07.000000 hello_robot_stretch_factory-0.3.8/tools/REx_stepper_mechaduino_menu.py
--rwxrwxr-x   0 hello-robot  (1000) hello-robot  (1000)     2347 2022-09-14 17:03:07.000000 hello_robot_stretch_factory-0.3.8/tools/REx_usb_reset.py
--rwxrwxr-x   0 hello-robot  (1000) hello-robot  (1000)     1379 2022-09-14 17:03:07.000000 hello_robot_stretch_factory-0.3.8/tools/REx_wacc_calibrate.py
+drwxrwxr-x   0 hello-robot  (1000) hello-robot  (1000)        0 2022-09-26 23:26:26.513807 hello_robot_stretch_factory-0.3.9/
+-rw-rw-r--   0 hello-robot  (1000) hello-robot  (1000)      929 2022-09-26 19:48:43.000000 hello_robot_stretch_factory-0.3.9/LICENSE.md
+-rw-rw-r--   0 hello-robot  (1000) hello-robot  (1000)      816 2022-09-26 23:26:26.513807 hello_robot_stretch_factory-0.3.9/PKG-INFO
+-rw-rw-r--   0 hello-robot  (1000) hello-robot  (1000)      355 2022-09-26 19:48:43.000000 hello_robot_stretch_factory-0.3.9/README.md
+drwxrwxr-x   0 hello-robot  (1000) hello-robot  (1000)        0 2022-09-26 23:26:26.513807 hello_robot_stretch_factory-0.3.9/hello_robot_stretch_factory.egg-info/
+-rw-rw-r--   0 hello-robot  (1000) hello-robot  (1000)      816 2022-09-26 23:26:26.000000 hello_robot_stretch_factory-0.3.9/hello_robot_stretch_factory.egg-info/PKG-INFO
+-rw-rw-r--   0 hello-robot  (1000) hello-robot  (1000)     1447 2022-09-26 23:26:26.000000 hello_robot_stretch_factory-0.3.9/hello_robot_stretch_factory.egg-info/SOURCES.txt
+-rw-rw-r--   0 hello-robot  (1000) hello-robot  (1000)        1 2022-09-26 23:26:26.000000 hello_robot_stretch_factory-0.3.9/hello_robot_stretch_factory.egg-info/dependency_links.txt
+-rw-rw-r--   0 hello-robot  (1000) hello-robot  (1000)       73 2022-09-26 23:26:26.000000 hello_robot_stretch_factory-0.3.9/hello_robot_stretch_factory.egg-info/requires.txt
+-rw-rw-r--   0 hello-robot  (1000) hello-robot  (1000)       16 2022-09-26 23:26:26.000000 hello_robot_stretch_factory-0.3.9/hello_robot_stretch_factory.egg-info/top_level.txt
+-rw-rw-r--   0 hello-robot  (1000) hello-robot  (1000)       38 2022-09-26 23:26:26.513807 hello_robot_stretch_factory-0.3.9/setup.cfg
+-rw-rw-r--   0 hello-robot  (1000) hello-robot  (1000)      992 2022-09-26 23:24:38.000000 hello_robot_stretch_factory-0.3.9/setup.py
+drwxrwxr-x   0 hello-robot  (1000) hello-robot  (1000)        0 2022-09-26 23:26:26.513807 hello_robot_stretch_factory-0.3.9/stretch_factory/
+-rw-rw-r--   0 hello-robot  (1000) hello-robot  (1000)        0 2022-09-26 19:48:43.000000 hello_robot_stretch_factory-0.3.9/stretch_factory/__init__.py
+-rw-rw-r--   0 hello-robot  (1000) hello-robot  (1000)     6326 2022-09-26 22:58:30.000000 hello_robot_stretch_factory-0.3.9/stretch_factory/device_mgmt.py
+-rw-rw-r--   0 hello-robot  (1000) hello-robot  (1000)    40406 2022-09-26 23:19:44.000000 hello_robot_stretch_factory-0.3.9/stretch_factory/firmware_updater.py
+-rw-rw-r--   0 hello-robot  (1000) hello-robot  (1000)    15885 2022-09-26 19:48:43.000000 hello_robot_stretch_factory-0.3.9/stretch_factory/hello_device_utils.py
+-rw-rw-r--   0 hello-robot  (1000) hello-robot  (1000)    12828 2022-09-26 19:48:43.000000 hello_robot_stretch_factory-0.3.9/stretch_factory/param_mgmt.py
+drwxrwxr-x   0 hello-robot  (1000) hello-robot  (1000)        0 2022-09-26 23:26:26.513807 hello_robot_stretch_factory-0.3.9/test/
+-rw-rw-r--   0 hello-robot  (1000) hello-robot  (1000)      685 2022-09-26 19:48:43.000000 hello_robot_stretch_factory-0.3.9/test/test_firmware_updater.py
+-rw-rw-r--   0 hello-robot  (1000) hello-robot  (1000)      668 2022-09-26 19:48:43.000000 hello_robot_stretch_factory-0.3.9/test/test_usb_reset.py
+drwxrwxr-x   0 hello-robot  (1000) hello-robot  (1000)        0 2022-09-26 23:26:26.513807 hello_robot_stretch_factory-0.3.9/tools/
+-rwxrwxr-x   0 hello-robot  (1000) hello-robot  (1000)     2456 2022-09-26 19:48:43.000000 hello_robot_stretch_factory-0.3.9/tools/RE1_migrate_contacts.py
+-rwxrwxr-x   0 hello-robot  (1000) hello-robot  (1000)     6621 2022-09-26 19:48:43.000000 hello_robot_stretch_factory-0.3.9/tools/RE1_migrate_params.py
+-rwxrwxr-x   0 hello-robot  (1000) hello-robot  (1000)    21784 2022-09-26 19:48:43.000000 hello_robot_stretch_factory-0.3.9/tools/REx_D435i_check.py
+-rwxrwxr-x   0 hello-robot  (1000) hello-robot  (1000)     5418 2022-09-26 19:48:43.000000 hello_robot_stretch_factory-0.3.9/tools/REx_base_calibrate_imu_collect.py
+-rwxrwxr-x   0 hello-robot  (1000) hello-robot  (1000)    32027 2022-09-26 19:48:43.000000 hello_robot_stretch_factory-0.3.9/tools/REx_base_calibrate_imu_process.py
+-rwxrwxr-x   0 hello-robot  (1000) hello-robot  (1000)     5950 2022-09-26 19:48:43.000000 hello_robot_stretch_factory-0.3.9/tools/REx_base_calibrate_wheel_separation.py
+-rwxrwxr-x   0 hello-robot  (1000) hello-robot  (1000)     7224 2022-09-26 20:01:43.000000 hello_robot_stretch_factory-0.3.9/tools/REx_calibrate_guarded_contact.py
+-rwxrwxr-x   0 hello-robot  (1000) hello-robot  (1000)     3578 2022-09-26 19:48:43.000000 hello_robot_stretch_factory-0.3.9/tools/REx_calibrate_range.py
+-rwxrwxr-x   0 hello-robot  (1000) hello-robot  (1000)     1728 2022-09-26 19:48:43.000000 hello_robot_stretch_factory-0.3.9/tools/REx_cliff_sensor_calibrate.py
+-rwxrwxr-x   0 hello-robot  (1000) hello-robot  (1000)     1442 2022-09-26 19:48:43.000000 hello_robot_stretch_factory-0.3.9/tools/REx_dynamixel_id_change.py
+-rwxrwxr-x   0 hello-robot  (1000) hello-robot  (1000)     1354 2022-09-26 19:48:43.000000 hello_robot_stretch_factory-0.3.9/tools/REx_dynamixel_id_scan.py
+-rwxrwxr-x   0 hello-robot  (1000) hello-robot  (1000)     5045 2022-09-26 19:48:43.000000 hello_robot_stretch_factory-0.3.9/tools/REx_dynamixel_jog.py
+-rwxrwxr-x   0 hello-robot  (1000) hello-robot  (1000)     1374 2022-09-26 19:48:43.000000 hello_robot_stretch_factory-0.3.9/tools/REx_dynamixel_reboot.py
+-rwxrwxr-x   0 hello-robot  (1000) hello-robot  (1000)     1188 2022-09-26 19:48:43.000000 hello_robot_stretch_factory-0.3.9/tools/REx_dynamixel_set_baud.py
+-rwxrwxr-x   0 hello-robot  (1000) hello-robot  (1000)     5361 2022-09-26 21:04:56.000000 hello_robot_stretch_factory-0.3.9/tools/REx_firmware_updater.py
+-rwxrwxr-x   0 hello-robot  (1000) hello-robot  (1000)     1583 2022-09-26 19:48:43.000000 hello_robot_stretch_factory-0.3.9/tools/REx_gamepad_configure.py
+-rwxrwxr-x   0 hello-robot  (1000) hello-robot  (1000)     2338 2022-09-26 19:48:43.000000 hello_robot_stretch_factory-0.3.9/tools/REx_gripper_calibrate.py
+-rwxrwxr-x   0 hello-robot  (1000) hello-robot  (1000)     1947 2022-09-26 19:48:43.000000 hello_robot_stretch_factory-0.3.9/tools/REx_hello_dynamixel_jog.py
+-rwxrwxr-x   0 hello-robot  (1000) hello-robot  (1000)      870 2022-09-26 19:48:43.000000 hello_robot_stretch_factory-0.3.9/tools/REx_stepper_calibration_YAML_to_flash.py
+-rwxrwxr-x   0 hello-robot  (1000) hello-robot  (1000)      685 2022-09-26 19:48:43.000000 hello_robot_stretch_factory-0.3.9/tools/REx_stepper_calibration_flash_to_YAML.py
+-rwxrwxr-x   0 hello-robot  (1000) hello-robot  (1000)     1168 2022-09-26 19:48:43.000000 hello_robot_stretch_factory-0.3.9/tools/REx_stepper_calibration_run.py
+-rwxrwxr-x   0 hello-robot  (1000) hello-robot  (1000)    18644 2022-09-26 19:48:43.000000 hello_robot_stretch_factory-0.3.9/tools/REx_stepper_ctrl_tuning.py
+-rwxrwxr-x   0 hello-robot  (1000) hello-robot  (1000)     1163 2022-09-26 19:48:43.000000 hello_robot_stretch_factory-0.3.9/tools/REx_stepper_gains.py
+-rwxrwxr-x   0 hello-robot  (1000) hello-robot  (1000)     4064 2022-09-26 19:48:43.000000 hello_robot_stretch_factory-0.3.9/tools/REx_stepper_jog.py
+-rwxrwxr-x   0 hello-robot  (1000) hello-robot  (1000)      852 2022-09-26 19:48:43.000000 hello_robot_stretch_factory-0.3.9/tools/REx_stepper_mechaduino_menu.py
+-rwxrwxr-x   0 hello-robot  (1000) hello-robot  (1000)     2347 2022-09-26 19:48:43.000000 hello_robot_stretch_factory-0.3.9/tools/REx_usb_reset.py
+-rwxrwxr-x   0 hello-robot  (1000) hello-robot  (1000)     1379 2022-09-26 19:48:43.000000 hello_robot_stretch_factory-0.3.9/tools/REx_wacc_calibrate.py
```

### Comparing `hello_robot_stretch_factory-0.3.8/LICENSE.md` & `hello_robot_stretch_factory-0.3.9/LICENSE.md`

 * *Files identical despite different names*

### Comparing `hello_robot_stretch_factory-0.3.8/PKG-INFO` & `hello_robot_stretch_factory-0.3.9/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: hello_robot_stretch_factory
-Version: 0.3.8
+Version: 0.3.9
 Summary: Stretch Factory Tools
 Home-page: https://github.com/hello-robot/stretch_factory
 Author: Hello Robot Inc.
 Author-email: support@hello-robot.com
 Classifier: Programming Language :: Python :: 3
 Classifier: Operating System :: OS Independent
 Classifier: License :: OSI Approved :: GNU General Public License v3 (GPLv3)
```

### Comparing `hello_robot_stretch_factory-0.3.8/hello_robot_stretch_factory.egg-info/PKG-INFO` & `hello_robot_stretch_factory-0.3.9/hello_robot_stretch_factory.egg-info/PKG-INFO`

 * *Files 17% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: hello-robot-stretch-factory
-Version: 0.3.8
+Version: 0.3.9
 Summary: Stretch Factory Tools
 Home-page: https://github.com/hello-robot/stretch_factory
 Author: Hello Robot Inc.
 Author-email: support@hello-robot.com
 Classifier: Programming Language :: Python :: 3
 Classifier: Operating System :: OS Independent
 Classifier: License :: OSI Approved :: GNU General Public License v3 (GPLv3)
```

### Comparing `hello_robot_stretch_factory-0.3.8/hello_robot_stretch_factory.egg-info/SOURCES.txt` & `hello_robot_stretch_factory-0.3.9/hello_robot_stretch_factory.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `hello_robot_stretch_factory-0.3.8/setup.py` & `hello_robot_stretch_factory-0.3.9/setup.py`

 * *Files 16% similar despite different names*

```diff
@@ -2,27 +2,28 @@
 from os.path import isfile
 import glob
 
 with open("README.md", "r") as fh:
     long_description = fh.read()
 
 script_path='./tools'
-stretch_scripts=[f for f in glob.glob(script_path+'/*.py') if isfile(f)]
+ex_scripts = glob.glob(script_path+'/*.py') + glob.glob(script_path+'/*.sh')
+stretch_scripts=[f for f in ex_scripts if isfile(f)]
 
 setuptools.setup(
     name="hello_robot_stretch_factory",
-    version="0.3.8",
+    version="0.3.9",
     author="Hello Robot Inc.",
     author_email="support@hello-robot.com",
     description="Stretch Factory Tools",
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://github.com/hello-robot/stretch_factory",
     scripts = stretch_scripts,
     packages=['stretch_factory'],
     classifiers=[
         "Programming Language :: Python :: 3",
         "Operating System :: OS Independent",
         "License :: OSI Approved :: GNU General Public License v3 (GPLv3)"
     ],
-    install_requires=['future', 'pyserial','pyusb','gitpython','hello-robot-stretch-body>=0.4.0','tabulate']
+    install_requires=['future', 'pyserial','pyusb','gitpython','hello-robot-stretch-body>=0.4.8','tabulate']
 )
```

### Comparing `hello_robot_stretch_factory-0.3.8/stretch_factory/device_mgmt.py` & `hello_robot_stretch_factory-0.3.9/stretch_factory/device_mgmt.py`

 * *Files 6% similar despite different names*

```diff
@@ -11,14 +11,28 @@
     Therefore, you may need to add the fallowing to a udev rule if it is not already there (eg in a file
     /etc/udev/rules.d/94-hello-usb.rules :
 
     SUBSYSTEM=="usb", ENV{DEVTYPE}=="usb_device", MODE="0664", GROUP="plugdev"
 
     Also see: https://stackoverflow.com/questions/31992058/how-can-i-comunicate-with-this-device-using-pyusb/31994168#31994168
     """
+
+    @staticmethod
+    def reset_all_arduino():
+        devs = []
+        all = usb.core.find(find_all=True)
+        for dev in all:
+            if dev.idVendor == 0x2341:# and dev.idProduct == 0x804d:
+                devs.append(dev)
+        for d in devs:
+            try:
+                d.reset()
+            except:
+                pass
+
     def __init__(self,device_names=None):
         self.comports= serial.tools.list_ports.comports()
         if device_names==None:
             self.device_names = ['hello-motor-arm',
                                  'hello-motor-lift',
                                  'hello-motor-right-wheel',
                                  'hello-motor-left-wheel',
@@ -30,31 +44,36 @@
             self.device_names=device_names
         self.device_info={}
         for d in self.device_names:
             self.device_info[d]={'device':None,'info':None, 'core':None}
 
         self.valid=True
 
-        #Build mapping between symlink and device name
+        #Build mapping between symlink (hello-motor-arm) and device name (ttyACM0)
         n_match=0
         lsdev=Popen("ls -ltr /dev/hello*", shell=True, bufsize=64, stdin=PIPE, stdout=PIPE, close_fds=True).stdout.read().split(b'\n')
         for name in self.device_info.keys():
             for line in lsdev:
                 if line.find(name.encode())>=0:
                     map=line[line.find(name.encode()):] #eg: hello-motor-arm -> ttyACM4
                     device=map[map.find(b'->')+3:] #eg ttyACM
-                    self.device_info[name]['device']=device
+                    self.device_info[name]['device']=device #Now self.device_info['hello-pimu']['device']='ttyACM0' for example
                     n_match=n_match+1
         if not n_match==len(self.device_info.keys()):
-            print('ls parse: Failed to match all devices for StretchSerialInfo')
-            print(self.device_info)
+            print('ls parse: Failed to match all device symlinks to /dev/ttyACMx for StretchSerialInfo')
+
+
+        #Now for each device mapped above find the associated comport under usb.core
         for c in self.comports:
             for name in self.device_info.keys():
-                if c.device[5:].encode()==self.device_info[name]['device']:
+                ttyACMx = c.device[5:].encode()
+                if ttyACMx==self.device_info[name]['device']:
                     self.device_info[name]['info']=c
+
+        #Now build a list of usb.core devices with Arduino vendor info
         devs = []
         if self.check_udev_rules():
             all = usb.core.find(find_all=True)
             for dev in all:
                 if dev.idVendor == 0x2341 and dev.idProduct == 0x804d:
                     devs.append(dev)
                 if dev.idVendor == 0x0403 and dev.idProduct == 0x6001:
```

### Comparing `hello_robot_stretch_factory-0.3.8/stretch_factory/firmware_updater.py` & `hello_robot_stretch_factory-0.3.9/stretch_factory/firmware_updater.py`

 * *Files 2% similar despite different names*

```diff
@@ -3,20 +3,21 @@
 import click
 import os
 from subprocess import Popen, PIPE
 import git
 import stretch_body.stepper
 import stretch_body.pimu
 import stretch_body.wacc
+import stretch_body.device
 import yaml
 import time
 import sys
 import stretch_body.device
 from stretch_factory.device_mgmt import StretchDeviceMgmt
-
+import stretch_body.hello_utils
 
 # #####################################################################################################
 class FirmwareVersion():
     """
     Manage comparision of firmware versions
     """
     def __init__(self,version_str):
@@ -286,14 +287,15 @@
                     self.recommended[device_name]=None
 
     def pretty_print(self):
         click.secho(' Recommended Firmware Updates '.center(110,'#'), fg="cyan",bold=True)
         print('\n')
         click.secho('%s | %s | %s | %s ' % ('DEVICE'.ljust(25), 'INSTALLED'.ljust(25), 'RECOMMENDED'.ljust(25), 'ACTION'.ljust(25)), fg="cyan", bold=True)
         click.secho('-'*110,fg="cyan", bold=True)
+
         for device_name in self.recommended.keys():
             dev_out=device_name.upper().ljust(25)
             installed_out=''.ljust(25)
             rec_out = ''.ljust(25)
             action_out = ''.ljust(25)
             if not self.fw_installed.is_device_valid(device_name):
                 installed_out='No device available'.ljust(25)
@@ -307,14 +309,32 @@
                     if self.recommended[device_name] > version:
                         action_out='Upgrade recommended'.ljust(25)
                     elif self.recommended[device_name] < version:
                         action_out='Downgrade recommended'.ljust(25)
                     else:
                         action_out = 'At most recent version'.ljust(25)
             print('%s | %s | %s | %s ' %(dev_out,installed_out,rec_out,action_out))
+
+
+    def print_recommended_args(self):
+        dev_arg_map={'hello-pimu':' --pimu','hello-wacc':' --wacc','hello-motor-right-wheel':' --right_wheel',
+                     'hello-motor-left-wheel':' --left_wheel','hello-motor-lift':' --lift',
+                     'hello-motor-arm':' --arm'}
+        rec_args=''
+        for device_name in self.recommended.keys():
+            if self.fw_installed.is_device_valid(device_name):
+                version = self.fw_installed.get_version(device_name)
+                if self.recommended[device_name]!=None:
+                    if self.recommended[device_name] > version:
+                        rec_args=rec_args+dev_arg_map[device_name]
+        if len(rec_args):
+            click.secho('\nRun recommended command: \nREx_firmware_updater.py --install %s'%rec_args,fg="green", bold=True)
+        else:
+            click.secho('\nFirmware upgrade not necessary',fg="green", bold=True)
+
 # #####################################################################################################
 
 log_device=stretch_body.device.Device(req_params=False)
 
 def user_msg_log(msg,user_display=True,fg=None,bg=None,bold=False):
     if user_display:
         click.secho(str(msg),fg=fg, bg=bg,bold=bold)
@@ -534,19 +554,23 @@
                     return False
         return self.do_update(verbose=verbose,no_prompts=no_prompts)
 
 
     def flash_stepper_calibration(self,device_name):
         if device_name == 'hello-motor-arm' or device_name == 'hello-motor-lift' or device_name == 'hello-motor-right-wheel' or device_name == 'hello-motor-left-wheel':
                 click.secho(' Flashing Stepper Calibration: %s '.center(110,'#') % device_name, fg="cyan",bold=True)
+                if not self.wait_on_device(device_name):
+                    click.secho('Device %s failed to return to bus' % device_name, fg="red",bold=True)
+                    return False
                 time.sleep(1.0)
                 motor = stretch_body.stepper.Stepper('/dev/' + device_name)
                 motor.startup()
                 if not motor.hw_valid:
                     click.secho('Failed to startup stepper %s' % device_name, fg="red", bold=True)
+                    return False
                 else:
                     print('Writing gains to flash...')
                     motor.write_gains_to_flash()
                     motor.push_command()
                     print('Gains written to flash')
                     print('')
                     print('Reading calibration data from YAML...')
@@ -557,29 +581,37 @@
                     self.wait_on_device(device_name)
                     motor.board_reset()
                     motor.push_command()
                     motor.transport.ser.close()
                     time.sleep(2.0)
                     self.wait_on_device(device_name)
                     print('Successful return of device to bus.')
+        return True
 
 
 
 
     def post_firmware_update(self):
         #Return True if no errors
+        click.secho(' Performing Post Firmware Updates '.center(110, '#'), fg="cyan", bold=True)
+        StretchDeviceMgmt.reset_all_arduino()
+        s = StretchDeviceMgmt()
+        s.reset_all()
+        time.sleep(2.0)
+        flash_stepper_calibration_success={}
         for device_name in self.target.keys():
             if self.fw_updated[device_name]:
-                self.flash_stepper_calibration(device_name)
+                flash_stepper_calibration_success[device_name]=self.flash_stepper_calibration(device_name)
                 time.sleep(2.0)  # Give time to get back on bus
-                s = StretchDeviceMgmt([device_name])
-                s.reset_all()
-                if not self.wait_on_device(device_name):
-                    print('Failed to return to bus')
-                    return False
+                #s = StretchDeviceMgmt([device_name])
+                #s.reset_all()
+                # StretchDeviceMgmt.reset_all_arduino()
+                # if not self.wait_on_device(device_name):
+                #     print('Failed to return to bus')
+                #     return False
         print('')
         click.secho(' Confirming Firmware Updates '.center(110,'#'), fg="cyan", bold=True)
         self.fw_installed = InstalledFirmware(self.use_device) #Pull the currently installed system from fw
         n_failure=0
         for device_name in self.target.keys():
             if self.use_device[device_name]:
                 if not self.fw_installed.is_device_valid(device_name): #Device may not have come back on bus
@@ -588,14 +620,19 @@
                 else:
                     v_curr =self.fw_installed.get_version(device_name)  # Version that is now on the board
                     if v_curr ==  self.target[device_name]:
                         click.secho('%s | %s ' % (device_name.upper().ljust(25), 'Installed firmware matches target'.ljust(40)),fg="green")
                     else:
                         click.secho('%s | %s ' % (device_name.upper().ljust(25), 'Firmware update failure!!'.ljust(40)),fg="red", bold=True)
                         n_failure=n_failure+1
+                    if not flash_stepper_calibration_success[device_name]:
+                        n_failure = n_failure + 1
+                        click.secho('%s | %s ' % (device_name.upper().ljust(25), 'Stepper calibration flash failure!!'.ljust(40)),fg="red", bold=True)
+                        click.secho('To manually restore stepper calibration, after power-cycling robot run ', fg="red",bold=True)
+                        click.secho('REx_stepper_calibration_YAML_to_flash.py %s' % device_name)
         if n_failure !=0:
             click.secho('#'*110,fg="red", bold=True)
             click.secho('Firmware update reported %d failures.\nTo remedy failures power down and the power up the robot and try again.'%n_failure,fg="red", bold=True)
             return False
         return True
 
     def get_firmware_version_from_path(self,sketch_name,path):
@@ -684,16 +721,19 @@
             if not type(port_name)==str:
                 port_name=port_name.decode('utf-8')
             return port_name
         except IndexError:
             return None
 
     def does_stepper_have_encoder_calibration_YAML(self,device_name):
-        dd = stretch_body.stepper.Stepper('/dev/' + device_name)
-        return len(dd.read_encoder_calibration_from_YAML())!=0
+        d=stretch_body.device.Device(req_params=False)
+        sn = d.robot_params[device_name]['serial_no']
+        fn = 'calibration_steppers/' + device_name + '_' + sn + '.yaml'
+        enc_data = stretch_body.hello_utils.read_fleet_yaml(fn)
+        return len(enc_data)!=0
 
     def flash_firmware_update(self,device_name, tag,repo_path=None,verbose=False):
         click.secho('-------- FIRMWARE FLASH %s | %s ------------'%(device_name,tag), fg="cyan", bold=True)
         config_file = self.fw_available.repo_path + '/arduino-cli.yaml'
 
         user_msg_log('Config: '+str(config_file), user_display=verbose)
         user_msg_log('Repo: '+str(repo_path), user_display=verbose)
@@ -705,19 +745,17 @@
             sketch_name = 'hello_wacc'
         if device_name == 'hello-pimu':
             sketch_name = 'hello_pimu'
 
         if sketch_name=='hello_stepper' and not self.does_stepper_have_encoder_calibration_YAML(device_name):
             print('Encoder data has not been stored for %s and may be lost. Aborting firmware flash.'%device_name)
             return False
-
-        s = StretchDeviceMgmt([device_name])
-        if not s.reset(device_name):
-            return False
-
+        #s = StretchDeviceMgmt([device_name])
+        #if not s.reset(device_name):
+        #    return False
         print('Looking for device %s on bus' % device_name)
         if not self.wait_on_device(device_name, timeout=5.0):
             print('Failure: Device not on bus.')
             return False
         port_name = self.get_port_name(device_name)
         if port_name is not None and sketch_name is not None:
 
@@ -760,19 +798,21 @@
                     else:
                         for m in k:
                             print(m.decode('utf-8'))
 
             success = uu[-1] == b'CPU reset.'
             if not success:
                 print('Firmware flash. Failed to upload to %s' % (port_name))
+                return False
             else:
                 print('Success in firmware flash.')
-                time.sleep(2.0) #Give time to get back on bus
-                s = StretchDeviceMgmt([device_name])
-                s.reset_all()
-                if self.wait_on_device(device_name):
-                    return True
-            print('Failure for device %s to return to USB bus after upload'%device_name)
-            return False
+                #Give time to get back on bus
+                time.sleep(3.0)
+                s = StretchDeviceMgmt.reset_all_arduino()
+
+                if not self.wait_on_device(device_name):
+                    click.secho('Device %s failed to return to bus' % device_name, fg="red",bold=True)
+                    return False
+                return True
         else:
             print('Firmware update %s. Failed to find device %s'%(tag,device_name))
             return False
```

### Comparing `hello_robot_stretch_factory-0.3.8/stretch_factory/hello_device_utils.py` & `hello_robot_stretch_factory-0.3.9/stretch_factory/hello_device_utils.py`

 * *Files identical despite different names*

### Comparing `hello_robot_stretch_factory-0.3.8/stretch_factory/param_mgmt.py` & `hello_robot_stretch_factory-0.3.9/stretch_factory/param_mgmt.py`

 * *Files identical despite different names*

### Comparing `hello_robot_stretch_factory-0.3.8/test/test_firmware_updater.py` & `hello_robot_stretch_factory-0.3.9/test/test_firmware_updater.py`

 * *Files identical despite different names*

### Comparing `hello_robot_stretch_factory-0.3.8/test/test_usb_reset.py` & `hello_robot_stretch_factory-0.3.9/test/test_usb_reset.py`

 * *Files identical despite different names*

### Comparing `hello_robot_stretch_factory-0.3.8/tools/RE1_migrate_contacts.py` & `hello_robot_stretch_factory-0.3.9/tools/RE1_migrate_contacts.py`

 * *Files identical despite different names*

### Comparing `hello_robot_stretch_factory-0.3.8/tools/RE1_migrate_params.py` & `hello_robot_stretch_factory-0.3.9/tools/RE1_migrate_params.py`

 * *Files identical despite different names*

### Comparing `hello_robot_stretch_factory-0.3.8/tools/REx_D435i_check.py` & `hello_robot_stretch_factory-0.3.9/tools/REx_D435i_check.py`

 * *Files identical despite different names*

### Comparing `hello_robot_stretch_factory-0.3.8/tools/REx_base_calibrate_imu_collect.py` & `hello_robot_stretch_factory-0.3.9/tools/REx_base_calibrate_imu_collect.py`

 * *Files identical despite different names*

### Comparing `hello_robot_stretch_factory-0.3.8/tools/REx_base_calibrate_imu_process.py` & `hello_robot_stretch_factory-0.3.9/tools/REx_base_calibrate_imu_process.py`

 * *Files identical despite different names*

### Comparing `hello_robot_stretch_factory-0.3.8/tools/REx_base_calibrate_wheel_separation.py` & `hello_robot_stretch_factory-0.3.9/tools/REx_base_calibrate_wheel_separation.py`

 * *Files identical despite different names*

### Comparing `hello_robot_stretch_factory-0.3.8/tools/REx_calibrate_guarded_contact.py` & `hello_robot_stretch_factory-0.3.9/tools/REx_calibrate_guarded_contact.py`

 * *Files identical despite different names*

### Comparing `hello_robot_stretch_factory-0.3.8/tools/REx_calibrate_range.py` & `hello_robot_stretch_factory-0.3.9/tools/REx_calibrate_range.py`

 * *Files identical despite different names*

### Comparing `hello_robot_stretch_factory-0.3.8/tools/REx_cliff_sensor_calibrate.py` & `hello_robot_stretch_factory-0.3.9/tools/REx_cliff_sensor_calibrate.py`

 * *Files identical despite different names*

### Comparing `hello_robot_stretch_factory-0.3.8/tools/REx_dynamixel_id_change.py` & `hello_robot_stretch_factory-0.3.9/tools/REx_dynamixel_id_change.py`

 * *Files identical despite different names*

### Comparing `hello_robot_stretch_factory-0.3.8/tools/REx_dynamixel_id_scan.py` & `hello_robot_stretch_factory-0.3.9/tools/REx_dynamixel_id_scan.py`

 * *Files identical despite different names*

### Comparing `hello_robot_stretch_factory-0.3.8/tools/REx_dynamixel_jog.py` & `hello_robot_stretch_factory-0.3.9/tools/REx_dynamixel_jog.py`

 * *Files identical despite different names*

### Comparing `hello_robot_stretch_factory-0.3.8/tools/REx_dynamixel_reboot.py` & `hello_robot_stretch_factory-0.3.9/tools/REx_dynamixel_reboot.py`

 * *Files identical despite different names*

### Comparing `hello_robot_stretch_factory-0.3.8/tools/REx_dynamixel_set_baud.py` & `hello_robot_stretch_factory-0.3.9/tools/REx_dynamixel_set_baud.py`

 * *Files identical despite different names*

### Comparing `hello_robot_stretch_factory-0.3.8/tools/REx_firmware_updater.py` & `hello_robot_stretch_factory-0.3.9/tools/REx_firmware_updater.py`

 * *Files 1% similar despite different names*

```diff
@@ -82,28 +82,29 @@
 The user may update Stetch Body version from time to time. After installing
 a new version of Stretch Body, this firmware updater tools should be run. 
 """
 
 if args.arm or args.lift or args.wacc or args.pimu or args.left_wheel or args.right_wheel:
     use_device={'hello-motor-lift':args.lift,'hello-motor-arm':args.arm, 'hello-motor-right-wheel':args.right_wheel, 'hello-motor-left-wheel':args.left_wheel,'hello-pimu':args.pimu,'hello-wacc':args.wacc}
 else:
-    use_device = {'hello-motor-lift': True, 'hello-motor-arm': True, 'hello-motor-right-wheel': True, 'hello-motor-left-wheel': True, 'hello-pimu': True, 'hello-wacc': True}
+    use_device = {'hello-motor-arm': True, 'hello-motor-right-wheel': True, 'hello-motor-left-wheel': True, 'hello-pimu': True, 'hello-wacc': True,'hello-motor-lift': True}
 
 if args.mgmt:
     print(mgmt)
     exit()
 
 if args.current:
     c = InstalledFirmware(use_device)
     c.pretty_print()
     exit()
 
 if args.recommended:
     r = RecommendedFirmware(use_device)
     r.pretty_print()
+    r.print_recommended_args()
     exit()
 
 if args.available:
     a = AvailableFirmware(use_device)
     a.pretty_print()
     exit()
```

### Comparing `hello_robot_stretch_factory-0.3.8/tools/REx_gamepad_configure.py` & `hello_robot_stretch_factory-0.3.9/tools/REx_gamepad_configure.py`

 * *Files identical despite different names*

### Comparing `hello_robot_stretch_factory-0.3.8/tools/REx_gripper_calibrate.py` & `hello_robot_stretch_factory-0.3.9/tools/REx_gripper_calibrate.py`

 * *Files identical despite different names*

### Comparing `hello_robot_stretch_factory-0.3.8/tools/REx_hello_dynamixel_jog.py` & `hello_robot_stretch_factory-0.3.9/tools/REx_hello_dynamixel_jog.py`

 * *Files identical despite different names*

### Comparing `hello_robot_stretch_factory-0.3.8/tools/REx_stepper_calibration_YAML_to_flash.py` & `hello_robot_stretch_factory-0.3.9/tools/REx_stepper_calibration_YAML_to_flash.py`

 * *Files identical despite different names*

### Comparing `hello_robot_stretch_factory-0.3.8/tools/REx_stepper_calibration_flash_to_YAML.py` & `hello_robot_stretch_factory-0.3.9/tools/REx_stepper_calibration_flash_to_YAML.py`

 * *Files identical despite different names*

### Comparing `hello_robot_stretch_factory-0.3.8/tools/REx_stepper_calibration_run.py` & `hello_robot_stretch_factory-0.3.9/tools/REx_stepper_calibration_run.py`

 * *Files identical despite different names*

### Comparing `hello_robot_stretch_factory-0.3.8/tools/REx_stepper_ctrl_tuning.py` & `hello_robot_stretch_factory-0.3.9/tools/REx_stepper_ctrl_tuning.py`

 * *Files identical despite different names*

### Comparing `hello_robot_stretch_factory-0.3.8/tools/REx_stepper_gains.py` & `hello_robot_stretch_factory-0.3.9/tools/REx_stepper_gains.py`

 * *Files identical despite different names*

### Comparing `hello_robot_stretch_factory-0.3.8/tools/REx_stepper_jog.py` & `hello_robot_stretch_factory-0.3.9/tools/REx_stepper_jog.py`

 * *Files identical despite different names*

### Comparing `hello_robot_stretch_factory-0.3.8/tools/REx_stepper_mechaduino_menu.py` & `hello_robot_stretch_factory-0.3.9/tools/REx_stepper_mechaduino_menu.py`

 * *Files identical despite different names*

### Comparing `hello_robot_stretch_factory-0.3.8/tools/REx_usb_reset.py` & `hello_robot_stretch_factory-0.3.9/tools/REx_usb_reset.py`

 * *Files identical despite different names*

### Comparing `hello_robot_stretch_factory-0.3.8/tools/REx_wacc_calibrate.py` & `hello_robot_stretch_factory-0.3.9/tools/REx_wacc_calibrate.py`

 * *Files identical despite different names*

