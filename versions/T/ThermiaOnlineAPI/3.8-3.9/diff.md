# Comparing `tmp/ThermiaOnlineAPI-3.8.tar.gz` & `tmp/ThermiaOnlineAPI-3.9.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "ThermiaOnlineAPI-3.8.tar", last modified: Wed Jan  4 16:32:22 2023, max compression
+gzip compressed data, was "ThermiaOnlineAPI-3.9.tar", last modified: Wed Jan  4 22:44:51 2023, max compression
```

## Comparing `ThermiaOnlineAPI-3.8.tar` & `ThermiaOnlineAPI-3.9.tar`

### file list

```diff
@@ -1,27 +1,27 @@
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-04 16:32:22.147998 ThermiaOnlineAPI-3.8/
--rw-r--r--   0 runner    (1001) docker     (123)    35149 2023-01-04 16:32:13.000000 ThermiaOnlineAPI-3.8/LICENSE
--rw-r--r--   0 runner    (1001) docker     (123)     8715 2023-01-04 16:32:22.147998 ThermiaOnlineAPI-3.8/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)     8269 2023-01-04 16:32:13.000000 ThermiaOnlineAPI-3.8/README.md
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-04 16:32:22.147998 ThermiaOnlineAPI-3.8/ThermiaOnlineAPI/
--rw-r--r--   0 runner    (1001) docker     (123)     1007 2023-01-04 16:32:13.000000 ThermiaOnlineAPI-3.8/ThermiaOnlineAPI/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-04 16:32:22.147998 ThermiaOnlineAPI-3.8/ThermiaOnlineAPI/api/
--rw-r--r--   0 runner    (1001) docker     (123)    22493 2023-01-04 16:32:13.000000 ThermiaOnlineAPI-3.8/ThermiaOnlineAPI/api/ThermiaAPI.py
--rw-r--r--   0 runner    (1001) docker     (123)       18 2023-01-04 16:32:13.000000 ThermiaOnlineAPI-3.8/ThermiaOnlineAPI/api/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     4849 2023-01-04 16:32:13.000000 ThermiaOnlineAPI-3.8/ThermiaOnlineAPI/const.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-04 16:32:22.147998 ThermiaOnlineAPI-3.8/ThermiaOnlineAPI/exceptions/
--rw-r--r--   0 runner    (1001) docker     (123)      222 2023-01-04 16:32:13.000000 ThermiaOnlineAPI-3.8/ThermiaOnlineAPI/exceptions/AuthenticationException.py
--rw-r--r--   0 runner    (1001) docker     (123)      208 2023-01-04 16:32:13.000000 ThermiaOnlineAPI-3.8/ThermiaOnlineAPI/exceptions/NetworkException.py
--rw-r--r--   0 runner    (1001) docker     (123)       29 2023-01-04 16:32:13.000000 ThermiaOnlineAPI-3.8/ThermiaOnlineAPI/exceptions/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-04 16:32:22.147998 ThermiaOnlineAPI-3.8/ThermiaOnlineAPI/model/
--rw-r--r--   0 runner    (1001) docker     (123)    28640 2023-01-04 16:32:13.000000 ThermiaOnlineAPI-3.8/ThermiaOnlineAPI/model/HeatPump.py
--rw-r--r--   0 runner    (1001) docker     (123)       22 2023-01-04 16:32:13.000000 ThermiaOnlineAPI-3.8/ThermiaOnlineAPI/model/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-04 16:32:22.147998 ThermiaOnlineAPI-3.8/ThermiaOnlineAPI/utils/
--rw-r--r--   0 runner    (1001) docker     (123)       11 2023-01-04 16:32:13.000000 ThermiaOnlineAPI-3.8/ThermiaOnlineAPI/utils/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     1100 2023-01-04 16:32:13.000000 ThermiaOnlineAPI-3.8/ThermiaOnlineAPI/utils/utils.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-04 16:32:22.147998 ThermiaOnlineAPI-3.8/ThermiaOnlineAPI.egg-info/
--rw-r--r--   0 runner    (1001) docker     (123)     8715 2023-01-04 16:32:22.000000 ThermiaOnlineAPI-3.8/ThermiaOnlineAPI.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)      599 2023-01-04 16:32:22.000000 ThermiaOnlineAPI-3.8/ThermiaOnlineAPI.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-01-04 16:32:22.000000 ThermiaOnlineAPI-3.8/ThermiaOnlineAPI.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (123)       17 2023-01-04 16:32:22.000000 ThermiaOnlineAPI-3.8/ThermiaOnlineAPI.egg-info/top_level.txt
--rw-r--r--   0 runner    (1001) docker     (123)       79 2023-01-04 16:32:22.147998 ThermiaOnlineAPI-3.8/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (123)     1110 2023-01-04 16:32:13.000000 ThermiaOnlineAPI-3.8/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-04 22:44:51.106414 ThermiaOnlineAPI-3.9/
+-rw-r--r--   0 runner    (1001) docker     (123)    35149 2023-01-04 22:44:41.000000 ThermiaOnlineAPI-3.9/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (123)     8715 2023-01-04 22:44:51.106414 ThermiaOnlineAPI-3.9/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     8269 2023-01-04 22:44:41.000000 ThermiaOnlineAPI-3.9/README.md
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-04 22:44:51.102414 ThermiaOnlineAPI-3.9/ThermiaOnlineAPI/
+-rw-r--r--   0 runner    (1001) docker     (123)     1007 2023-01-04 22:44:41.000000 ThermiaOnlineAPI-3.9/ThermiaOnlineAPI/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-04 22:44:51.106414 ThermiaOnlineAPI-3.9/ThermiaOnlineAPI/api/
+-rw-r--r--   0 runner    (1001) docker     (123)    22493 2023-01-04 22:44:41.000000 ThermiaOnlineAPI-3.9/ThermiaOnlineAPI/api/ThermiaAPI.py
+-rw-r--r--   0 runner    (1001) docker     (123)       18 2023-01-04 22:44:41.000000 ThermiaOnlineAPI-3.9/ThermiaOnlineAPI/api/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4849 2023-01-04 22:44:41.000000 ThermiaOnlineAPI-3.9/ThermiaOnlineAPI/const.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-04 22:44:51.106414 ThermiaOnlineAPI-3.9/ThermiaOnlineAPI/exceptions/
+-rw-r--r--   0 runner    (1001) docker     (123)      222 2023-01-04 22:44:41.000000 ThermiaOnlineAPI-3.9/ThermiaOnlineAPI/exceptions/AuthenticationException.py
+-rw-r--r--   0 runner    (1001) docker     (123)      208 2023-01-04 22:44:41.000000 ThermiaOnlineAPI-3.9/ThermiaOnlineAPI/exceptions/NetworkException.py
+-rw-r--r--   0 runner    (1001) docker     (123)       29 2023-01-04 22:44:41.000000 ThermiaOnlineAPI-3.9/ThermiaOnlineAPI/exceptions/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-04 22:44:51.106414 ThermiaOnlineAPI-3.9/ThermiaOnlineAPI/model/
+-rw-r--r--   0 runner    (1001) docker     (123)    29416 2023-01-04 22:44:41.000000 ThermiaOnlineAPI-3.9/ThermiaOnlineAPI/model/HeatPump.py
+-rw-r--r--   0 runner    (1001) docker     (123)       22 2023-01-04 22:44:41.000000 ThermiaOnlineAPI-3.9/ThermiaOnlineAPI/model/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-04 22:44:51.106414 ThermiaOnlineAPI-3.9/ThermiaOnlineAPI/utils/
+-rw-r--r--   0 runner    (1001) docker     (123)       11 2023-01-04 22:44:41.000000 ThermiaOnlineAPI-3.9/ThermiaOnlineAPI/utils/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1100 2023-01-04 22:44:41.000000 ThermiaOnlineAPI-3.9/ThermiaOnlineAPI/utils/utils.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-04 22:44:51.102414 ThermiaOnlineAPI-3.9/ThermiaOnlineAPI.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)     8715 2023-01-04 22:44:51.000000 ThermiaOnlineAPI-3.9/ThermiaOnlineAPI.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)      599 2023-01-04 22:44:51.000000 ThermiaOnlineAPI-3.9/ThermiaOnlineAPI.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-01-04 22:44:51.000000 ThermiaOnlineAPI-3.9/ThermiaOnlineAPI.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       17 2023-01-04 22:44:51.000000 ThermiaOnlineAPI-3.9/ThermiaOnlineAPI.egg-info/top_level.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       79 2023-01-04 22:44:51.106414 ThermiaOnlineAPI-3.9/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (123)     1110 2023-01-04 22:44:41.000000 ThermiaOnlineAPI-3.9/setup.py
```

### Comparing `ThermiaOnlineAPI-3.8/LICENSE` & `ThermiaOnlineAPI-3.9/LICENSE`

 * *Files identical despite different names*

### Comparing `ThermiaOnlineAPI-3.8/PKG-INFO` & `ThermiaOnlineAPI-3.9/PKG-INFO`

 * *Files 2% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: ThermiaOnlineAPI
-Version: 3.8
+Version: 3.9
 Summary: A Python API for Thermia heat pumps using https://online.thermia.se
 Home-page: https://github.com/klejejs/python-thermia-online-api
 Download-URL: https://github.com/klejejs/python-thermia-online-api/releases
 Author: Krisjanis Lejejs
 Author-email: krisjanis.lejejs@gmail.com
 License: GPL-3.0
 Keywords: Thermia,Online
```

### Comparing `ThermiaOnlineAPI-3.8/README.md` & `ThermiaOnlineAPI-3.9/README.md`

 * *Files identical despite different names*

### Comparing `ThermiaOnlineAPI-3.8/ThermiaOnlineAPI/__init__.py` & `ThermiaOnlineAPI-3.9/ThermiaOnlineAPI/__init__.py`

 * *Files identical despite different names*

### Comparing `ThermiaOnlineAPI-3.8/ThermiaOnlineAPI/api/ThermiaAPI.py` & `ThermiaOnlineAPI-3.9/ThermiaOnlineAPI/api/ThermiaAPI.py`

 * *Files identical despite different names*

### Comparing `ThermiaOnlineAPI-3.8/ThermiaOnlineAPI/const.py` & `ThermiaOnlineAPI-3.9/ThermiaOnlineAPI/const.py`

 * *Files identical despite different names*

### Comparing `ThermiaOnlineAPI-3.8/ThermiaOnlineAPI/model/HeatPump.py` & `ThermiaOnlineAPI-3.9/ThermiaOnlineAPI/model/HeatPump.py`

 * *Files 2% similar despite different names*

```diff
@@ -55,14 +55,15 @@
         self.__info = None
         self.__status = None
         self.__device_data = None
 
         # GROUPS
         self.__group_temperatures = None
         self.__group_operational_status = None
+        self.__operational_status_register = None
         self.__group_operational_time = None
         self.__group_operational_operation = None
         self.__group_hot_water: Dict[str, Optional[int]] = {
             "hot_water_switch": None,
             "hot_water_boost_switch": None,
         }
 
@@ -340,35 +341,43 @@
 
         if value.get("visible"):
             return value.get("value")
 
         return None
 
     def __get_operational_statuses_from_operational_status(self) -> Optional[Dict]:
+        if self.__operational_status_register is not None:
+            return self.__get_register_from_operational_status(
+                self.__operational_status_register
+            )
+
         # Try to get the data from the REG_OPERATIONAL_STATUS_PRIO1 register
         data = self.__get_register_from_operational_status(REG_OPERATIONAL_STATUS_PRIO1)
         if data is not None:
+            self.__operational_status_register = REG_OPERATIONAL_STATUS_PRIO1
             return {
                 "registerValues": data.get("valueNames", []),
                 "valueNamePrefix": "REG_VALUE_STATUS_",
             }
 
         # Try to get the data from the COMP_STATUS_ITEC register
         data = self.__get_register_from_operational_status(COMP_STATUS_ITEC)
         if data is not None:
+            self.__operational_status_register = COMP_STATUS_ITEC
             return {
                 "registerValues": data.get("valueNames", []),
                 "valueNamePrefix": "COMP_VALUE_",
             }
 
         # Try to get the data from the REG_OPERATIONAL_STATUS_PRIORITY_BITMASK register
         data = self.__get_register_from_operational_status(
             REG_OPERATIONAL_STATUS_PRIORITY_BITMASK
         )
         if data is not None:
+            self.__operational_status_register = REG_OPERATIONAL_STATUS_PRIORITY_BITMASK
             return {
                 "registerValues": data.get("valueNames", []),
                 "valueNamePrefix": "REG_VALUE_STATUS_",
             }
 
         return None
 
@@ -542,15 +551,23 @@
 
     ###########################################################################
     # Operational status (REG_GROUP_OPERATIONAL_STATUS)
     ###########################################################################
 
     @property
     def operational_status(self):
-        data = self.__get_register_from_operational_status(REG_OPERATIONAL_STATUS_PRIO1)
+        if self.__operational_status_register is None:
+            # Attempt to get the register from the status data
+            self.__get_operational_statuses_from_operational_status()
+            if self.__operational_status_register is None:
+                return None
+
+        data = self.__get_register_from_operational_status(
+            self.__operational_status_register
+        )
 
         if data is None:
             return None
 
         current_register_value = get_dict_value_or_none(data, "registerValue")
 
         data = self.__get_all_operational_statuses_from_operational_status()
```

### Comparing `ThermiaOnlineAPI-3.8/ThermiaOnlineAPI/utils/utils.py` & `ThermiaOnlineAPI-3.9/ThermiaOnlineAPI/utils/utils.py`

 * *Files identical despite different names*

### Comparing `ThermiaOnlineAPI-3.8/ThermiaOnlineAPI.egg-info/PKG-INFO` & `ThermiaOnlineAPI-3.9/ThermiaOnlineAPI.egg-info/PKG-INFO`

 * *Files 2% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: ThermiaOnlineAPI
-Version: 3.8
+Version: 3.9
 Summary: A Python API for Thermia heat pumps using https://online.thermia.se
 Home-page: https://github.com/klejejs/python-thermia-online-api
 Download-URL: https://github.com/klejejs/python-thermia-online-api/releases
 Author: Krisjanis Lejejs
 Author-email: krisjanis.lejejs@gmail.com
 License: GPL-3.0
 Keywords: Thermia,Online
```

### Comparing `ThermiaOnlineAPI-3.8/ThermiaOnlineAPI.egg-info/SOURCES.txt` & `ThermiaOnlineAPI-3.9/ThermiaOnlineAPI.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `ThermiaOnlineAPI-3.8/setup.py` & `ThermiaOnlineAPI-3.9/setup.py`

 * *Files identical despite different names*

