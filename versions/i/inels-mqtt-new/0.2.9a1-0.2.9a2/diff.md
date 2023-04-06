# Comparing `tmp/inels-mqtt-new-0.2.9a1.tar.gz` & `tmp/inels-mqtt-new-0.2.9a2.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "inels-mqtt-new-0.2.9a1.tar", last modified: Fri Mar 17 16:09:15 2023, max compression
+gzip compressed data, was "inels-mqtt-new-0.2.9a2.tar", last modified: Fri Mar 17 17:19:47 2023, max compression
```

## Comparing `inels-mqtt-new-0.2.9a1.tar` & `inels-mqtt-new-0.2.9a2.tar`

### file list

```diff
@@ -1,34 +1,34 @@
-drwxrwxr-x   0 zed4805   (1000) zed4805   (1000)        0 2023-03-17 16:09:15.644439 inels-mqtt-new-0.2.9a1/
--rw-rw-r--   0 zed4805   (1000) zed4805   (1000)     1098 2022-12-09 11:04:29.000000 inels-mqtt-new-0.2.9a1/LICENSE
--rw-rw-r--   0 zed4805   (1000) zed4805   (1000)       60 2022-12-09 11:04:29.000000 inels-mqtt-new-0.2.9a1/MANIFEST.in
--rw-rw-r--   0 zed4805   (1000) zed4805   (1000)     1971 2023-03-17 16:09:15.644439 inels-mqtt-new-0.2.9a1/PKG-INFO
--rw-rw-r--   0 zed4805   (1000) zed4805   (1000)     1565 2023-03-13 13:15:33.000000 inels-mqtt-new-0.2.9a1/README.md
-drwxrwxr-x   0 zed4805   (1000) zed4805   (1000)        0 2023-03-17 16:09:15.639439 inels-mqtt-new-0.2.9a1/inels_mqtt_new.egg-info/
--rw-rw-r--   0 zed4805   (1000) zed4805   (1000)     1971 2023-03-17 16:09:15.000000 inels-mqtt-new-0.2.9a1/inels_mqtt_new.egg-info/PKG-INFO
--rw-rw-r--   0 zed4805   (1000) zed4805   (1000)      612 2023-03-17 16:09:15.000000 inels-mqtt-new-0.2.9a1/inels_mqtt_new.egg-info/SOURCES.txt
--rw-rw-r--   0 zed4805   (1000) zed4805   (1000)        1 2023-03-17 16:09:15.000000 inels-mqtt-new-0.2.9a1/inels_mqtt_new.egg-info/dependency_links.txt
--rw-rw-r--   0 zed4805   (1000) zed4805   (1000)        1 2022-12-14 11:42:43.000000 inels-mqtt-new-0.2.9a1/inels_mqtt_new.egg-info/not-zip-safe
--rw-rw-r--   0 zed4805   (1000) zed4805   (1000)       16 2023-03-17 16:09:15.000000 inels-mqtt-new-0.2.9a1/inels_mqtt_new.egg-info/top_level.txt
-drwxrwxr-x   0 zed4805   (1000) zed4805   (1000)        0 2023-03-17 16:09:15.641439 inels-mqtt-new-0.2.9a1/inelsmqtt/
--rw-rw-r--   0 zed4805   (1000) zed4805   (1000)    17216 2023-03-13 18:18:53.000000 inels-mqtt-new-0.2.9a1/inelsmqtt/__init__.py
--rw-rw-r--   0 zed4805   (1000) zed4805   (1000)     3642 2022-10-27 02:45:24.000000 inels-mqtt-new-0.2.9a1/inelsmqtt/config.py
--rw-rw-r--   0 zed4805   (1000) zed4805   (1000)    21271 2023-03-13 16:18:45.000000 inels-mqtt-new-0.2.9a1/inelsmqtt/const.py
-drwxrwxr-x   0 zed4805   (1000) zed4805   (1000)        0 2023-03-17 16:09:15.641439 inels-mqtt-new-0.2.9a1/inelsmqtt/devices/
--rw-rw-r--   0 zed4805   (1000) zed4805   (1000)    10132 2023-02-27 18:01:48.000000 inels-mqtt-new-0.2.9a1/inelsmqtt/devices/__init__.py
--rw-rw-r--   0 zed4805   (1000) zed4805   (1000)     2045 2022-12-20 18:05:57.000000 inels-mqtt-new-0.2.9a1/inelsmqtt/devices/switch.py
--rw-rw-r--   0 zed4805   (1000) zed4805   (1000)     2786 2023-02-24 14:51:44.000000 inels-mqtt-new-0.2.9a1/inelsmqtt/discovery.py
--rw-rw-r--   0 zed4805   (1000) zed4805   (1000)     3022 2022-11-23 14:11:40.000000 inels-mqtt-new-0.2.9a1/inelsmqtt/mqtt_client.py
--rw-rw-r--   0 zed4805   (1000) zed4805   (1000)    88025 2023-03-17 16:08:33.000000 inels-mqtt-new-0.2.9a1/inelsmqtt/util.py
--rw-rw-r--   0 zed4805   (1000) zed4805   (1000)      132 2022-12-09 11:04:29.000000 inels-mqtt-new-0.2.9a1/pyproject.toml
--rw-rw-r--   0 zed4805   (1000) zed4805   (1000)       30 2022-12-09 11:04:29.000000 inels-mqtt-new-0.2.9a1/requirements.txt
--rw-rw-r--   0 zed4805   (1000) zed4805   (1000)      198 2023-03-17 16:09:15.644439 inels-mqtt-new-0.2.9a1/setup.cfg
--rw-rw-r--   0 zed4805   (1000) zed4805   (1000)      820 2023-03-17 16:08:53.000000 inels-mqtt-new-0.2.9a1/setup.py
-drwxrwxr-x   0 zed4805   (1000) zed4805   (1000)        0 2023-03-17 16:09:15.643439 inels-mqtt-new-0.2.9a1/tests/
--rw-rw-r--   0 zed4805   (1000) zed4805   (1000)       36 2022-12-09 11:04:29.000000 inels-mqtt-new-0.2.9a1/tests/__init__.py
--rw-rw-r--   0 zed4805   (1000) zed4805   (1000)     4792 2022-12-09 11:04:29.000000 inels-mqtt-new-0.2.9a1/tests/const.py
-drwxrwxr-x   0 zed4805   (1000) zed4805   (1000)        0 2023-03-17 16:09:15.643439 inels-mqtt-new-0.2.9a1/tests/devices/
--rw-rw-r--   0 zed4805   (1000) zed4805   (1000)       32 2022-12-09 11:04:29.000000 inels-mqtt-new-0.2.9a1/tests/devices/__init__.py
--rw-rw-r--   0 zed4805   (1000) zed4805   (1000)    16688 2022-12-14 11:39:38.000000 inels-mqtt-new-0.2.9a1/tests/devices/device_test.py
--rw-rw-r--   0 zed4805   (1000) zed4805   (1000)     2639 2022-12-14 11:39:31.000000 inels-mqtt-new-0.2.9a1/tests/discovery_test.py
--rw-rw-r--   0 zed4805   (1000) zed4805   (1000)     6597 2022-12-14 11:39:37.000000 inels-mqtt-new-0.2.9a1/tests/inels_mqtt_test.py
--rw-rw-r--   0 zed4805   (1000) zed4805   (1000)     1032 2022-12-09 11:04:29.000000 inels-mqtt-new-0.2.9a1/tests/online_test.py
+drwxrwxr-x   0 zed4805   (1000) zed4805   (1000)        0 2023-03-17 17:19:47.747532 inels-mqtt-new-0.2.9a2/
+-rw-rw-r--   0 zed4805   (1000) zed4805   (1000)     1098 2022-12-09 11:04:29.000000 inels-mqtt-new-0.2.9a2/LICENSE
+-rw-rw-r--   0 zed4805   (1000) zed4805   (1000)       60 2022-12-09 11:04:29.000000 inels-mqtt-new-0.2.9a2/MANIFEST.in
+-rw-rw-r--   0 zed4805   (1000) zed4805   (1000)     1971 2023-03-17 17:19:47.747532 inels-mqtt-new-0.2.9a2/PKG-INFO
+-rw-rw-r--   0 zed4805   (1000) zed4805   (1000)     1565 2023-03-13 13:15:33.000000 inels-mqtt-new-0.2.9a2/README.md
+drwxrwxr-x   0 zed4805   (1000) zed4805   (1000)        0 2023-03-17 17:19:47.743533 inels-mqtt-new-0.2.9a2/inels_mqtt_new.egg-info/
+-rw-rw-r--   0 zed4805   (1000) zed4805   (1000)     1971 2023-03-17 17:19:47.000000 inels-mqtt-new-0.2.9a2/inels_mqtt_new.egg-info/PKG-INFO
+-rw-rw-r--   0 zed4805   (1000) zed4805   (1000)      612 2023-03-17 17:19:47.000000 inels-mqtt-new-0.2.9a2/inels_mqtt_new.egg-info/SOURCES.txt
+-rw-rw-r--   0 zed4805   (1000) zed4805   (1000)        1 2023-03-17 17:19:47.000000 inels-mqtt-new-0.2.9a2/inels_mqtt_new.egg-info/dependency_links.txt
+-rw-rw-r--   0 zed4805   (1000) zed4805   (1000)        1 2022-12-14 11:42:43.000000 inels-mqtt-new-0.2.9a2/inels_mqtt_new.egg-info/not-zip-safe
+-rw-rw-r--   0 zed4805   (1000) zed4805   (1000)       16 2023-03-17 17:19:47.000000 inels-mqtt-new-0.2.9a2/inels_mqtt_new.egg-info/top_level.txt
+drwxrwxr-x   0 zed4805   (1000) zed4805   (1000)        0 2023-03-17 17:19:47.745532 inels-mqtt-new-0.2.9a2/inelsmqtt/
+-rw-rw-r--   0 zed4805   (1000) zed4805   (1000)    17216 2023-03-13 18:18:53.000000 inels-mqtt-new-0.2.9a2/inelsmqtt/__init__.py
+-rw-rw-r--   0 zed4805   (1000) zed4805   (1000)     3642 2022-10-27 02:45:24.000000 inels-mqtt-new-0.2.9a2/inelsmqtt/config.py
+-rw-rw-r--   0 zed4805   (1000) zed4805   (1000)    21271 2023-03-13 16:18:45.000000 inels-mqtt-new-0.2.9a2/inelsmqtt/const.py
+drwxrwxr-x   0 zed4805   (1000) zed4805   (1000)        0 2023-03-17 17:19:47.745532 inels-mqtt-new-0.2.9a2/inelsmqtt/devices/
+-rw-rw-r--   0 zed4805   (1000) zed4805   (1000)    10257 2023-03-17 17:16:16.000000 inels-mqtt-new-0.2.9a2/inelsmqtt/devices/__init__.py
+-rw-rw-r--   0 zed4805   (1000) zed4805   (1000)     2045 2022-12-20 18:05:57.000000 inels-mqtt-new-0.2.9a2/inelsmqtt/devices/switch.py
+-rw-rw-r--   0 zed4805   (1000) zed4805   (1000)     2786 2023-02-24 14:51:44.000000 inels-mqtt-new-0.2.9a2/inelsmqtt/discovery.py
+-rw-rw-r--   0 zed4805   (1000) zed4805   (1000)     3022 2022-11-23 14:11:40.000000 inels-mqtt-new-0.2.9a2/inelsmqtt/mqtt_client.py
+-rw-rw-r--   0 zed4805   (1000) zed4805   (1000)    88025 2023-03-17 16:08:33.000000 inels-mqtt-new-0.2.9a2/inelsmqtt/util.py
+-rw-rw-r--   0 zed4805   (1000) zed4805   (1000)      132 2022-12-09 11:04:29.000000 inels-mqtt-new-0.2.9a2/pyproject.toml
+-rw-rw-r--   0 zed4805   (1000) zed4805   (1000)       30 2022-12-09 11:04:29.000000 inels-mqtt-new-0.2.9a2/requirements.txt
+-rw-rw-r--   0 zed4805   (1000) zed4805   (1000)      198 2023-03-17 17:19:47.748532 inels-mqtt-new-0.2.9a2/setup.cfg
+-rw-rw-r--   0 zed4805   (1000) zed4805   (1000)      820 2023-03-17 17:16:01.000000 inels-mqtt-new-0.2.9a2/setup.py
+drwxrwxr-x   0 zed4805   (1000) zed4805   (1000)        0 2023-03-17 17:19:47.747532 inels-mqtt-new-0.2.9a2/tests/
+-rw-rw-r--   0 zed4805   (1000) zed4805   (1000)       36 2022-12-09 11:04:29.000000 inels-mqtt-new-0.2.9a2/tests/__init__.py
+-rw-rw-r--   0 zed4805   (1000) zed4805   (1000)     4792 2022-12-09 11:04:29.000000 inels-mqtt-new-0.2.9a2/tests/const.py
+drwxrwxr-x   0 zed4805   (1000) zed4805   (1000)        0 2023-03-17 17:19:47.747532 inels-mqtt-new-0.2.9a2/tests/devices/
+-rw-rw-r--   0 zed4805   (1000) zed4805   (1000)       32 2022-12-09 11:04:29.000000 inels-mqtt-new-0.2.9a2/tests/devices/__init__.py
+-rw-rw-r--   0 zed4805   (1000) zed4805   (1000)    16688 2022-12-14 11:39:38.000000 inels-mqtt-new-0.2.9a2/tests/devices/device_test.py
+-rw-rw-r--   0 zed4805   (1000) zed4805   (1000)     2639 2022-12-14 11:39:31.000000 inels-mqtt-new-0.2.9a2/tests/discovery_test.py
+-rw-rw-r--   0 zed4805   (1000) zed4805   (1000)     6597 2022-12-14 11:39:37.000000 inels-mqtt-new-0.2.9a2/tests/inels_mqtt_test.py
+-rw-rw-r--   0 zed4805   (1000) zed4805   (1000)     1032 2022-12-09 11:04:29.000000 inels-mqtt-new-0.2.9a2/tests/online_test.py
```

### Comparing `inels-mqtt-new-0.2.9a1/LICENSE` & `inels-mqtt-new-0.2.9a2/LICENSE`

 * *Files identical despite different names*

### Comparing `inels-mqtt-new-0.2.9a1/PKG-INFO` & `inels-mqtt-new-0.2.9a2/PKG-INFO`

 * *Files 4% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: inels-mqtt-new
-Version: 0.2.9a1
+Version: 0.2.9a2
 Summary: Python library for iNels mqtt protocol
 Home-page: https://github.com/zed4805/inels-mqtt-new
 Author: Elko EP s.r.o.
 Author-email: zed4805@gmail.com
 License: MIT
 Keywords: iNels,Elko EP,Home assistant integration
 Classifier: License :: OSI Approved :: MIT License
```

### Comparing `inels-mqtt-new-0.2.9a1/README.md` & `inels-mqtt-new-0.2.9a2/README.md`

 * *Files identical despite different names*

### Comparing `inels-mqtt-new-0.2.9a1/inels_mqtt_new.egg-info/PKG-INFO` & `inels-mqtt-new-0.2.9a2/inels_mqtt_new.egg-info/PKG-INFO`

 * *Files 4% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: inels-mqtt-new
-Version: 0.2.9a1
+Version: 0.2.9a2
 Summary: Python library for iNels mqtt protocol
 Home-page: https://github.com/zed4805/inels-mqtt-new
 Author: Elko EP s.r.o.
 Author-email: zed4805@gmail.com
 License: MIT
 Keywords: iNels,Elko EP,Home assistant integration
 Classifier: License :: OSI Approved :: MIT License
```

### Comparing `inels-mqtt-new-0.2.9a1/inels_mqtt_new.egg-info/SOURCES.txt` & `inels-mqtt-new-0.2.9a2/inels_mqtt_new.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `inels-mqtt-new-0.2.9a1/inelsmqtt/__init__.py` & `inels-mqtt-new-0.2.9a2/inelsmqtt/__init__.py`

 * *Files identical despite different names*

### Comparing `inels-mqtt-new-0.2.9a1/inelsmqtt/config.py` & `inels-mqtt-new-0.2.9a2/inelsmqtt/config.py`

 * *Files identical despite different names*

### Comparing `inels-mqtt-new-0.2.9a1/inelsmqtt/const.py` & `inels-mqtt-new-0.2.9a2/inelsmqtt/const.py`

 * *Files identical despite different names*

### Comparing `inels-mqtt-new-0.2.9a1/inelsmqtt/devices/__init__.py` & `inels-mqtt-new-0.2.9a2/inelsmqtt/devices/__init__.py`

 * *Files 1% similar despite different names*

```diff
@@ -52,16 +52,17 @@
         self.__mqtt = mqtt
         self.__device_type = DEVICE_TYPE_DICT[
             fragments[TOPIC_FRAGMENTS[FRAGMENT_DEVICE_TYPE]]
         ]
         self.__inels_type = INELS_DEVICE_TYPE_DICT[
             fragments[TOPIC_FRAGMENTS[FRAGMENT_DEVICE_TYPE]]
         ]
-        self.__unique_id = fragments[TOPIC_FRAGMENTS[FRAGMENT_UNIQUE_ID]]
-        self.__parent_id = fragments[TOPIC_FRAGMENTS[FRAGMENT_SERIAL_NUMBER]]
+
+        self.__unique_id = f"{fragments[TOPIC_FRAGMENTS[FRAGMENT_SERIAL_NUMBER]]}_{fragments[TOPIC_FRAGMENTS[FRAGMENT_UNIQUE_ID]]}" #fragments[TOPIC_FRAGMENTS[FRAGMENT_UNIQUE_ID]]
+        self.__parent_id = self.__unique_id#fragments[TOPIC_FRAGMENTS[FRAGMENT_SERIAL_NUMBER]]
         self.__state_topic = state_topic
         self.__set_topic = None
 
         if self.__device_type is not SENSOR and self.__device_type is not BUTTON:
             self.__set_topic = f"{fragments[TOPIC_FRAGMENTS[FRAGMENT_DOMAIN]]}/set/{fragments[TOPIC_FRAGMENTS[FRAGMENT_SERIAL_NUMBER]]}/{fragments[TOPIC_FRAGMENTS[FRAGMENT_DEVICE_TYPE]]}/{fragments[TOPIC_FRAGMENTS[FRAGMENT_UNIQUE_ID]]}"  # noqa: E501
 
         self.__connected_topic = f"{fragments[TOPIC_FRAGMENTS[FRAGMENT_DOMAIN]]}/connected/{fragments[TOPIC_FRAGMENTS[FRAGMENT_SERIAL_NUMBER]]}/{fragments[TOPIC_FRAGMENTS[FRAGMENT_DEVICE_TYPE]]}/{fragments[TOPIC_FRAGMENTS[FRAGMENT_UNIQUE_ID]]}"  # noqa: E501
```

### Comparing `inels-mqtt-new-0.2.9a1/inelsmqtt/devices/switch.py` & `inels-mqtt-new-0.2.9a2/inelsmqtt/devices/switch.py`

 * *Files identical despite different names*

### Comparing `inels-mqtt-new-0.2.9a1/inelsmqtt/discovery.py` & `inels-mqtt-new-0.2.9a2/inelsmqtt/discovery.py`

 * *Files identical despite different names*

### Comparing `inels-mqtt-new-0.2.9a1/inelsmqtt/mqtt_client.py` & `inels-mqtt-new-0.2.9a2/inelsmqtt/mqtt_client.py`

 * *Files identical despite different names*

### Comparing `inels-mqtt-new-0.2.9a1/inelsmqtt/util.py` & `inels-mqtt-new-0.2.9a2/inelsmqtt/util.py`

 * *Files identical despite different names*

### Comparing `inels-mqtt-new-0.2.9a1/setup.py` & `inels-mqtt-new-0.2.9a2/setup.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,13 +1,13 @@
 """Setup script for inels-mqtt package."""
 from setuptools import setup, find_packages
 
 setup(
     name="inels-mqtt-new",
-    version="0.2.9a1",
+    version="0.2.9a2",
     url="https://github.com/zed4805/inels-mqtt-new",
     license="MIT",
     author="Elko EP s.r.o.",
     author_email="zed4805@gmail.com",
     description="Python library for iNels mqtt protocol",
     keywords=["iNels", "Elko EP", "Home assistant integration"],
     long_description_content_type="text/markdown",
```

### Comparing `inels-mqtt-new-0.2.9a1/tests/const.py` & `inels-mqtt-new-0.2.9a2/tests/const.py`

 * *Files identical despite different names*

### Comparing `inels-mqtt-new-0.2.9a1/tests/devices/device_test.py` & `inels-mqtt-new-0.2.9a2/tests/devices/device_test.py`

 * *Files identical despite different names*

### Comparing `inels-mqtt-new-0.2.9a1/tests/discovery_test.py` & `inels-mqtt-new-0.2.9a2/tests/discovery_test.py`

 * *Files identical despite different names*

### Comparing `inels-mqtt-new-0.2.9a1/tests/inels_mqtt_test.py` & `inels-mqtt-new-0.2.9a2/tests/inels_mqtt_test.py`

 * *Files identical despite different names*

### Comparing `inels-mqtt-new-0.2.9a1/tests/online_test.py` & `inels-mqtt-new-0.2.9a2/tests/online_test.py`

 * *Files identical despite different names*

