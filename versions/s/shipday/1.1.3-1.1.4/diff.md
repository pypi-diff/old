# Comparing `tmp/shipday-1.1.3.tar.gz` & `tmp/shipday-1.1.4.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "shipday-1.1.3.tar", last modified: Sun Aug 28 16:19:00 2022, max compression
+gzip compressed data, was "shipday-1.1.4.tar", last modified: Thu Apr  6 10:40:31 2023, max compression
```

## Comparing `shipday-1.1.3.tar` & `shipday-1.1.4.tar`

### file list

```diff
@@ -1,43 +1,43 @@
-drwxr-xr-x   0 shahriartanvir   (501) staff       (20)        0 2022-08-28 16:19:00.402249 shipday-1.1.3/
--rw-r--r--   0 shahriartanvir   (501) staff       (20)     6087 2022-08-28 16:19:00.402111 shipday-1.1.3/PKG-INFO
--rw-r--r--   0 shahriartanvir   (501) staff       (20)     5027 2022-08-28 13:52:12.000000 shipday-1.1.3/README.md
--rw-r--r--   0 shahriartanvir   (501) staff       (20)       38 2022-08-28 16:19:00.402290 shipday-1.1.3/setup.cfg
--rw-r--r--   0 shahriartanvir   (501) staff       (20)     2199 2022-08-28 16:18:56.000000 shipday-1.1.3/setup.py
-drwxr-xr-x   0 shahriartanvir   (501) staff       (20)        0 2022-08-28 16:19:00.396741 shipday-1.1.3/shipday/
--rw-r--r--   0 shahriartanvir   (501) staff       (20)       43 2022-08-01 08:56:51.000000 shipday-1.1.3/shipday/__init__.py
-drwxr-xr-x   0 shahriartanvir   (501) staff       (20)        0 2022-08-28 16:19:00.397654 shipday-1.1.3/shipday/carrier/
--rw-r--r--   0 shahriartanvir   (501) staff       (20)       59 2022-08-01 11:43:29.000000 shipday-1.1.3/shipday/carrier/__init__.py
--rw-r--r--   0 shahriartanvir   (501) staff       (20)     1704 2022-08-08 11:43:06.000000 shipday-1.1.3/shipday/carrier/carrier_request.py
-drwxr-xr-x   0 shahriartanvir   (501) staff       (20)        0 2022-08-28 16:19:00.398121 shipday-1.1.3/shipday/exeptions/
--rw-r--r--   0 shahriartanvir   (501) staff       (20)       64 2022-08-02 14:22:05.000000 shipday-1.1.3/shipday/exeptions/__init__.py
--rw-r--r--   0 shahriartanvir   (501) staff       (20)      129 2022-08-02 14:28:09.000000 shipday-1.1.3/shipday/exeptions/shipday_exeption.py
-drwxr-xr-x   0 shahriartanvir   (501) staff       (20)        0 2022-08-28 16:19:00.398422 shipday-1.1.3/shipday/httpclient/
--rw-r--r--   0 shahriartanvir   (501) staff       (20)        0 2022-08-01 09:04:25.000000 shipday-1.1.3/shipday/httpclient/__init__.py
--rw-r--r--   0 shahriartanvir   (501) staff       (20)     1408 2022-08-18 16:20:10.000000 shipday-1.1.3/shipday/httpclient/shipdayclient.py
-drwxr-xr-x   0 shahriartanvir   (501) staff       (20)        0 2022-08-28 16:19:00.400686 shipday-1.1.3/shipday/order/
--rw-r--r--   0 shahriartanvir   (501) staff       (20)      363 2022-08-08 13:53:26.000000 shipday-1.1.3/shipday/order/__init__.py
--rw-r--r--   0 shahriartanvir   (501) staff       (20)     2811 2022-08-02 14:26:04.000000 shipday-1.1.3/shipday/order/address.py
--rw-r--r--   0 shahriartanvir   (501) staff       (20)      160 2022-08-02 04:19:29.000000 shipday-1.1.3/shipday/order/card_type.py
--rw-r--r--   0 shahriartanvir   (501) staff       (20)     2412 2022-08-09 11:08:05.000000 shipday-1.1.3/shipday/order/customer.py
--rw-r--r--   0 shahriartanvir   (501) staff       (20)     2346 2022-08-08 15:01:50.000000 shipday-1.1.3/shipday/order/order_cost.py
--rw-r--r--   0 shahriartanvir   (501) staff       (20)     5825 2022-08-09 11:36:35.000000 shipday-1.1.3/shipday/order/order_info.py
--rw-r--r--   0 shahriartanvir   (501) staff       (20)     2705 2022-08-08 14:39:16.000000 shipday-1.1.3/shipday/order/order_item.py
--rw-r--r--   0 shahriartanvir   (501) staff       (20)     4011 2022-08-09 12:06:24.000000 shipday-1.1.3/shipday/order/order_query.py
--rw-r--r--   0 shahriartanvir   (501) staff       (20)      608 2022-08-09 11:55:38.000000 shipday-1.1.3/shipday/order/order_status.py
--rw-r--r--   0 shahriartanvir   (501) staff       (20)     2106 2022-08-08 14:10:17.000000 shipday-1.1.3/shipday/order/pickup.py
-drwxr-xr-x   0 shahriartanvir   (501) staff       (20)        0 2022-08-28 16:19:00.401548 shipday-1.1.3/shipday/services/
--rw-r--r--   0 shahriartanvir   (501) staff       (20)      196 2022-08-18 08:55:56.000000 shipday-1.1.3/shipday/services/__init__.py
--rw-r--r--   0 shahriartanvir   (501) staff       (20)      915 2022-08-26 05:35:26.000000 shipday-1.1.3/shipday/services/carrier_service.py
--rw-r--r--   0 shahriartanvir   (501) staff       (20)     3303 2022-08-28 13:52:12.000000 shipday-1.1.3/shipday/services/on_demand_delivery_service.py
--rw-r--r--   0 shahriartanvir   (501) staff       (20)     2395 2022-08-03 14:35:20.000000 shipday-1.1.3/shipday/services/order_service.py
--rw-r--r--   0 shahriartanvir   (501) staff       (20)      618 2022-08-18 08:57:10.000000 shipday-1.1.3/shipday/shipday_object.py
-drwxr-xr-x   0 shahriartanvir   (501) staff       (20)        0 2022-08-28 16:19:00.401836 shipday-1.1.3/shipday/utils/
--rw-r--r--   0 shahriartanvir   (501) staff       (20)        0 2022-08-01 15:47:51.000000 shipday-1.1.3/shipday/utils/__init__.py
--rw-r--r--   0 shahriartanvir   (501) staff       (20)      907 2022-08-18 16:48:27.000000 shipday-1.1.3/shipday/utils/verifiers.py
--rw-r--r--   0 shahriartanvir   (501) staff       (20)       18 2022-08-28 13:52:36.000000 shipday-1.1.3/shipday/version.py
-drwxr-xr-x   0 shahriartanvir   (501) staff       (20)        0 2022-08-28 16:19:00.397287 shipday-1.1.3/shipday.egg-info/
--rw-r--r--   0 shahriartanvir   (501) staff       (20)     6087 2022-08-28 16:19:00.000000 shipday-1.1.3/shipday.egg-info/PKG-INFO
--rw-r--r--   0 shahriartanvir   (501) staff       (20)      905 2022-08-28 16:19:00.000000 shipday-1.1.3/shipday.egg-info/SOURCES.txt
--rw-r--r--   0 shahriartanvir   (501) staff       (20)        1 2022-08-28 16:19:00.000000 shipday-1.1.3/shipday.egg-info/dependency_links.txt
--rw-r--r--   0 shahriartanvir   (501) staff       (20)       43 2022-08-28 16:19:00.000000 shipday-1.1.3/shipday.egg-info/requires.txt
--rw-r--r--   0 shahriartanvir   (501) staff       (20)        8 2022-08-28 16:19:00.000000 shipday-1.1.3/shipday.egg-info/top_level.txt
+drwxr-xr-x   0 shahriartanvir   (501) staff       (20)        0 2023-04-06 10:40:31.139137 shipday-1.1.4/
+-rw-r--r--   0 shahriartanvir   (501) staff       (20)     6087 2023-04-06 10:40:31.138968 shipday-1.1.4/PKG-INFO
+-rw-r--r--   0 shahriartanvir   (501) staff       (20)     5027 2022-08-28 13:52:12.000000 shipday-1.1.4/README.md
+-rw-r--r--   0 shahriartanvir   (501) staff       (20)       38 2023-04-06 10:40:31.139195 shipday-1.1.4/setup.cfg
+-rw-r--r--   0 shahriartanvir   (501) staff       (20)     2199 2022-12-29 20:00:12.000000 shipday-1.1.4/setup.py
+drwxr-xr-x   0 shahriartanvir   (501) staff       (20)        0 2023-04-06 10:40:31.130250 shipday-1.1.4/shipday/
+-rw-r--r--   0 shahriartanvir   (501) staff       (20)       43 2022-08-01 08:56:51.000000 shipday-1.1.4/shipday/__init__.py
+drwxr-xr-x   0 shahriartanvir   (501) staff       (20)        0 2023-04-06 10:40:31.131724 shipday-1.1.4/shipday/carrier/
+-rw-r--r--   0 shahriartanvir   (501) staff       (20)       59 2022-08-01 11:43:29.000000 shipday-1.1.4/shipday/carrier/__init__.py
+-rw-r--r--   0 shahriartanvir   (501) staff       (20)     1704 2022-08-08 11:43:06.000000 shipday-1.1.4/shipday/carrier/carrier_request.py
+drwxr-xr-x   0 shahriartanvir   (501) staff       (20)        0 2023-04-06 10:40:31.132273 shipday-1.1.4/shipday/exeptions/
+-rw-r--r--   0 shahriartanvir   (501) staff       (20)       64 2022-08-02 14:22:05.000000 shipday-1.1.4/shipday/exeptions/__init__.py
+-rw-r--r--   0 shahriartanvir   (501) staff       (20)      129 2022-08-02 14:28:09.000000 shipday-1.1.4/shipday/exeptions/shipday_exeption.py
+drwxr-xr-x   0 shahriartanvir   (501) staff       (20)        0 2023-04-06 10:40:31.132674 shipday-1.1.4/shipday/httpclient/
+-rw-r--r--   0 shahriartanvir   (501) staff       (20)        0 2022-08-01 09:04:25.000000 shipday-1.1.4/shipday/httpclient/__init__.py
+-rw-r--r--   0 shahriartanvir   (501) staff       (20)     1408 2022-08-18 16:20:10.000000 shipday-1.1.4/shipday/httpclient/shipdayclient.py
+drwxr-xr-x   0 shahriartanvir   (501) staff       (20)        0 2023-04-06 10:40:31.136597 shipday-1.1.4/shipday/order/
+-rw-r--r--   0 shahriartanvir   (501) staff       (20)      363 2022-08-08 13:53:26.000000 shipday-1.1.4/shipday/order/__init__.py
+-rw-r--r--   0 shahriartanvir   (501) staff       (20)     2811 2022-12-29 19:56:44.000000 shipday-1.1.4/shipday/order/address.py
+-rw-r--r--   0 shahriartanvir   (501) staff       (20)      160 2022-08-02 04:19:29.000000 shipday-1.1.4/shipday/order/card_type.py
+-rw-r--r--   0 shahriartanvir   (501) staff       (20)     2412 2022-08-09 11:08:05.000000 shipday-1.1.4/shipday/order/customer.py
+-rw-r--r--   0 shahriartanvir   (501) staff       (20)     2346 2022-08-08 15:01:50.000000 shipday-1.1.4/shipday/order/order_cost.py
+-rw-r--r--   0 shahriartanvir   (501) staff       (20)     5825 2023-04-06 10:24:46.000000 shipday-1.1.4/shipday/order/order_info.py
+-rw-r--r--   0 shahriartanvir   (501) staff       (20)     2710 2023-04-06 10:24:46.000000 shipday-1.1.4/shipday/order/order_item.py
+-rw-r--r--   0 shahriartanvir   (501) staff       (20)     4011 2022-08-09 12:06:24.000000 shipday-1.1.4/shipday/order/order_query.py
+-rw-r--r--   0 shahriartanvir   (501) staff       (20)      608 2022-08-09 11:55:38.000000 shipday-1.1.4/shipday/order/order_status.py
+-rw-r--r--   0 shahriartanvir   (501) staff       (20)     2106 2022-08-08 14:10:17.000000 shipday-1.1.4/shipday/order/pickup.py
+drwxr-xr-x   0 shahriartanvir   (501) staff       (20)        0 2023-04-06 10:40:31.137942 shipday-1.1.4/shipday/services/
+-rw-r--r--   0 shahriartanvir   (501) staff       (20)      196 2022-08-18 08:55:56.000000 shipday-1.1.4/shipday/services/__init__.py
+-rw-r--r--   0 shahriartanvir   (501) staff       (20)      915 2022-08-26 05:35:26.000000 shipday-1.1.4/shipday/services/carrier_service.py
+-rw-r--r--   0 shahriartanvir   (501) staff       (20)     3303 2023-03-29 16:35:29.000000 shipday-1.1.4/shipday/services/on_demand_delivery_service.py
+-rw-r--r--   0 shahriartanvir   (501) staff       (20)     2395 2022-08-03 14:35:20.000000 shipday-1.1.4/shipday/services/order_service.py
+-rw-r--r--   0 shahriartanvir   (501) staff       (20)      618 2022-08-18 08:57:10.000000 shipday-1.1.4/shipday/shipday_object.py
+drwxr-xr-x   0 shahriartanvir   (501) staff       (20)        0 2023-04-06 10:40:31.138479 shipday-1.1.4/shipday/utils/
+-rw-r--r--   0 shahriartanvir   (501) staff       (20)        0 2022-08-01 15:47:51.000000 shipday-1.1.4/shipday/utils/__init__.py
+-rw-r--r--   0 shahriartanvir   (501) staff       (20)      907 2022-08-18 16:48:27.000000 shipday-1.1.4/shipday/utils/verifiers.py
+-rw-r--r--   0 shahriartanvir   (501) staff       (20)       18 2023-04-06 10:24:46.000000 shipday-1.1.4/shipday/version.py
+drwxr-xr-x   0 shahriartanvir   (501) staff       (20)        0 2023-04-06 10:40:31.131171 shipday-1.1.4/shipday.egg-info/
+-rw-r--r--   0 shahriartanvir   (501) staff       (20)     6087 2023-04-06 10:40:31.000000 shipday-1.1.4/shipday.egg-info/PKG-INFO
+-rw-r--r--   0 shahriartanvir   (501) staff       (20)      905 2023-04-06 10:40:31.000000 shipday-1.1.4/shipday.egg-info/SOURCES.txt
+-rw-r--r--   0 shahriartanvir   (501) staff       (20)        1 2023-04-06 10:40:31.000000 shipday-1.1.4/shipday.egg-info/dependency_links.txt
+-rw-r--r--   0 shahriartanvir   (501) staff       (20)       43 2023-04-06 10:40:31.000000 shipday-1.1.4/shipday.egg-info/requires.txt
+-rw-r--r--   0 shahriartanvir   (501) staff       (20)        8 2023-04-06 10:40:31.000000 shipday-1.1.4/shipday.egg-info/top_level.txt
```

### Comparing `shipday-1.1.3/PKG-INFO` & `shipday-1.1.4/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: shipday
-Version: 1.1.3
+Version: 1.1.4
 Summary: Python library for Shipday API
 Home-page: https://shipday.com/
 Author: Shipday
 Author-email: shahriar@shipday.com
 License: MIT
 Keywords: Shipday,DoorDash,Uber,Delivery API,Dispatch API,DoorDash API,Uber API,Dispatch App,Courier App,Delivery Dispatch,Delivery integration,Delivery Management,Dispatch Management,Delivery Service Integration,Local Delivery API
 Platform: UNKNOWN
```

### Comparing `shipday-1.1.3/README.md` & `shipday-1.1.4/README.md`

 * *Files identical despite different names*

### Comparing `shipday-1.1.3/setup.py` & `shipday-1.1.4/setup.py`

 * *Files identical despite different names*

### Comparing `shipday-1.1.3/shipday/carrier/carrier_request.py` & `shipday-1.1.4/shipday/carrier/carrier_request.py`

 * *Files identical despite different names*

### Comparing `shipday-1.1.3/shipday/httpclient/shipdayclient.py` & `shipday-1.1.4/shipday/httpclient/shipdayclient.py`

 * *Files identical despite different names*

### Comparing `shipday-1.1.3/shipday/order/address.py` & `shipday-1.1.4/shipday/order/address.py`

 * *Files identical despite different names*

### Comparing `shipday-1.1.3/shipday/order/customer.py` & `shipday-1.1.4/shipday/order/customer.py`

 * *Files identical despite different names*

### Comparing `shipday-1.1.3/shipday/order/order_cost.py` & `shipday-1.1.4/shipday/order/order_cost.py`

 * *Files identical despite different names*

### Comparing `shipday-1.1.3/shipday/order/order_info.py` & `shipday-1.1.4/shipday/order/order_info.py`

 * *Files identical despite different names*

### Comparing `shipday-1.1.3/shipday/order/order_item.py` & `shipday-1.1.4/shipday/order/order_item.py`

 * *Files 0% similar despite different names*

```diff
@@ -6,15 +6,15 @@
 
 
 class OrderItem:
     def __init__(self, name=None, unit_price=None, quantity=None, add_ons=None, detail=None,
                  **kwargs):
         kwargs = defaultdict(lambda: None, **kwargs)
         self._name = name
-        self._unit_price = unit_price or kwargs['unitPrice']
+        self._unit_price = unit_price or kwargs['unitPrice'] or 0
         self._quantity = quantity
         self._add_ons = add_ons or kwargs['addOns']
         self._detail = detail
 
     @property
     def name(self):
         return self._name
```

### Comparing `shipday-1.1.3/shipday/order/order_query.py` & `shipday-1.1.4/shipday/order/order_query.py`

 * *Files identical despite different names*

### Comparing `shipday-1.1.3/shipday/order/order_status.py` & `shipday-1.1.4/shipday/order/order_status.py`

 * *Files identical despite different names*

### Comparing `shipday-1.1.3/shipday/order/pickup.py` & `shipday-1.1.4/shipday/order/pickup.py`

 * *Files identical despite different names*

### Comparing `shipday-1.1.3/shipday/services/carrier_service.py` & `shipday-1.1.4/shipday/services/carrier_service.py`

 * *Files identical despite different names*

### Comparing `shipday-1.1.3/shipday/services/on_demand_delivery_service.py` & `shipday-1.1.4/shipday/services/on_demand_delivery_service.py`

 * *Files identical despite different names*

### Comparing `shipday-1.1.3/shipday/services/order_service.py` & `shipday-1.1.4/shipday/services/order_service.py`

 * *Files identical despite different names*

### Comparing `shipday-1.1.3/shipday/shipday_object.py` & `shipday-1.1.4/shipday/shipday_object.py`

 * *Files identical despite different names*

### Comparing `shipday-1.1.3/shipday/utils/verifiers.py` & `shipday-1.1.4/shipday/utils/verifiers.py`

 * *Files identical despite different names*

### Comparing `shipday-1.1.3/shipday.egg-info/PKG-INFO` & `shipday-1.1.4/shipday.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: shipday
-Version: 1.1.3
+Version: 1.1.4
 Summary: Python library for Shipday API
 Home-page: https://shipday.com/
 Author: Shipday
 Author-email: shahriar@shipday.com
 License: MIT
 Keywords: Shipday,DoorDash,Uber,Delivery API,Dispatch API,DoorDash API,Uber API,Dispatch App,Courier App,Delivery Dispatch,Delivery integration,Delivery Management,Dispatch Management,Delivery Service Integration,Local Delivery API
 Platform: UNKNOWN
```

### Comparing `shipday-1.1.3/shipday.egg-info/SOURCES.txt` & `shipday-1.1.4/shipday.egg-info/SOURCES.txt`

 * *Files identical despite different names*

