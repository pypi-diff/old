# Comparing `tmp/syncqb-1.0.0.tar.gz` & `tmp/syncqb-1.0.1.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "syncqb-1.0.0.tar", last modified: Thu Apr  6 18:49:10 2023, max compression
+gzip compressed data, was "syncqb-1.0.1.tar", last modified: Thu Apr  6 20:54:20 2023, max compression
```

## Comparing `syncqb-1.0.0.tar` & `syncqb-1.0.1.tar`

### file list

```diff
@@ -1,22 +1,29 @@
-drwxr-xr-x   0 jacob     (1000) jacob     (1000)        0 2023-04-06 18:49:10.688285 syncqb-1.0.0/
--rw-r--r--   0 jacob     (1000) jacob     (1000)     1073 2022-09-12 17:13:14.000000 syncqb-1.0.0/LICENSE
--rw-r--r--   0 jacob     (1000) jacob     (1000)    10313 2023-04-06 18:49:10.688285 syncqb-1.0.0/PKG-INFO
--rw-r--r--   0 jacob     (1000) jacob     (1000)     8642 2023-04-05 20:53:17.000000 syncqb-1.0.0/README.md
--rw-r--r--   0 jacob     (1000) jacob     (1000)      643 2023-04-05 20:31:06.000000 syncqb-1.0.0/pyproject.toml
--rw-r--r--   0 jacob     (1000) jacob     (1000)       38 2023-04-06 18:49:10.688285 syncqb-1.0.0/setup.cfg
-drwxr-xr-x   0 jacob     (1000) jacob     (1000)        0 2023-04-06 18:49:10.688285 syncqb-1.0.0/src/
-drwxr-xr-x   0 jacob     (1000) jacob     (1000)        0 2023-04-06 18:49:10.688285 syncqb-1.0.0/src/syncqb/
--rw-r--r--   0 jacob     (1000) jacob     (1000)        0 2022-09-12 14:58:01.000000 syncqb-1.0.0/src/syncqb/__init__.py
--rw-r--r--   0 jacob     (1000) jacob     (1000)    17570 2023-04-06 18:45:06.000000 syncqb-1.0.0/src/syncqb/json_quickbase.py
--rw-r--r--   0 jacob     (1000) jacob     (1000)     1928 2023-04-06 18:38:17.000000 syncqb-1.0.0/src/syncqb/qb_client.py
--rw-r--r--   0 jacob     (1000) jacob     (1000)     1310 2023-04-03 20:33:16.000000 syncqb-1.0.0/src/syncqb/qb_errors.py
--rw-r--r--   0 jacob     (1000) jacob     (1000)      618 2023-04-06 18:45:19.000000 syncqb-1.0.0/src/syncqb/quickbase.py
--rw-r--r--   0 jacob     (1000) jacob     (1000)    26602 2023-04-06 18:45:28.000000 syncqb-1.0.0/src/syncqb/xml_quickbase.py
-drwxr-xr-x   0 jacob     (1000) jacob     (1000)        0 2023-04-06 18:49:10.688285 syncqb-1.0.0/src/syncqb.egg-info/
--rw-r--r--   0 jacob     (1000) jacob     (1000)    10313 2023-04-06 18:49:10.000000 syncqb-1.0.0/src/syncqb.egg-info/PKG-INFO
--rw-r--r--   0 jacob     (1000) jacob     (1000)      371 2023-04-06 18:49:10.000000 syncqb-1.0.0/src/syncqb.egg-info/SOURCES.txt
--rw-r--r--   0 jacob     (1000) jacob     (1000)        1 2023-04-06 18:49:10.000000 syncqb-1.0.0/src/syncqb.egg-info/dependency_links.txt
--rw-r--r--   0 jacob     (1000) jacob     (1000)       59 2023-04-06 18:49:10.000000 syncqb-1.0.0/src/syncqb.egg-info/entry_points.txt
--rw-r--r--   0 jacob     (1000) jacob     (1000)        7 2023-04-06 18:49:10.000000 syncqb-1.0.0/src/syncqb.egg-info/top_level.txt
-drwxr-xr-x   0 jacob     (1000) jacob     (1000)        0 2023-04-06 18:49:10.688285 syncqb-1.0.0/tests/
--rw-r--r--   0 jacob     (1000) jacob     (1000)     1443 2023-04-06 15:05:02.000000 syncqb-1.0.0/tests/test.py
+drwxr-xr-x   0 jacob     (1000) jacob     (1000)        0 2023-04-06 20:54:20.535325 syncqb-1.0.1/
+-rw-r--r--   0 jacob     (1000) jacob     (1000)     1073 2022-09-12 17:13:14.000000 syncqb-1.0.1/LICENSE
+-rw-r--r--   0 jacob     (1000) jacob     (1000)    10313 2023-04-06 20:54:20.525324 syncqb-1.0.1/PKG-INFO
+-rw-r--r--   0 jacob     (1000) jacob     (1000)     8642 2023-04-05 20:53:17.000000 syncqb-1.0.1/README.md
+-rw-r--r--   0 jacob     (1000) jacob     (1000)      643 2023-04-06 20:47:25.000000 syncqb-1.0.1/pyproject.toml
+-rw-r--r--   0 jacob     (1000) jacob     (1000)       38 2023-04-06 20:54:20.535325 syncqb-1.0.1/setup.cfg
+-rw-r--r--   0 jacob     (1000) jacob     (1000)       82 2023-04-06 20:44:31.000000 syncqb-1.0.1/setup.py
+drwxr-xr-x   0 jacob     (1000) jacob     (1000)        0 2023-04-06 20:54:20.525324 syncqb-1.0.1/src/
+drwxr-xr-x   0 jacob     (1000) jacob     (1000)        0 2023-04-06 20:54:20.525324 syncqb-1.0.1/src/syncqb/
+-rw-r--r--   0 jacob     (1000) jacob     (1000)        0 2022-09-12 14:58:01.000000 syncqb-1.0.1/src/syncqb/__init__.py
+-rw-r--r--   0 jacob     (1000) jacob     (1000)        0 2023-03-29 20:36:22.000000 syncqb-1.0.1/src/syncqb/__init__.pyi
+-rw-r--r--   0 jacob     (1000) jacob     (1000)    17643 2023-04-06 20:19:05.000000 syncqb-1.0.1/src/syncqb/json_quickbase.py
+-rw-r--r--   0 jacob     (1000) jacob     (1000)    10545 2023-04-05 20:37:35.000000 syncqb-1.0.1/src/syncqb/json_quickbase.pyi
+-rw-r--r--   0 jacob     (1000) jacob     (1000)     1928 2023-04-06 18:38:17.000000 syncqb-1.0.1/src/syncqb/qb_client.py
+-rw-r--r--   0 jacob     (1000) jacob     (1000)     1387 2023-04-03 17:21:25.000000 syncqb-1.0.1/src/syncqb/qb_client.pyi
+-rw-r--r--   0 jacob     (1000) jacob     (1000)     1310 2023-04-03 20:33:16.000000 syncqb-1.0.1/src/syncqb/qb_errors.py
+-rw-r--r--   0 jacob     (1000) jacob     (1000)     1076 2023-04-03 17:24:36.000000 syncqb-1.0.1/src/syncqb/qb_errors.pyi
+-rw-r--r--   0 jacob     (1000) jacob     (1000)      618 2023-04-06 18:45:19.000000 syncqb-1.0.1/src/syncqb/quickbase.py
+-rw-r--r--   0 jacob     (1000) jacob     (1000)      588 2023-04-03 17:21:59.000000 syncqb-1.0.1/src/syncqb/quickbase.pyi
+-rw-r--r--   0 jacob     (1000) jacob     (1000)    26718 2023-04-06 20:21:34.000000 syncqb-1.0.1/src/syncqb/xml_quickbase.py
+-rw-r--r--   0 jacob     (1000) jacob     (1000)     8781 2023-04-05 20:37:23.000000 syncqb-1.0.1/src/syncqb/xml_quickbase.pyi
+drwxr-xr-x   0 jacob     (1000) jacob     (1000)        0 2023-04-06 20:54:20.525324 syncqb-1.0.1/src/syncqb.egg-info/
+-rw-r--r--   0 jacob     (1000) jacob     (1000)    10313 2023-04-06 20:54:20.000000 syncqb-1.0.1/src/syncqb.egg-info/PKG-INFO
+-rw-r--r--   0 jacob     (1000) jacob     (1000)      538 2023-04-06 20:54:20.000000 syncqb-1.0.1/src/syncqb.egg-info/SOURCES.txt
+-rw-r--r--   0 jacob     (1000) jacob     (1000)        1 2023-04-06 20:54:20.000000 syncqb-1.0.1/src/syncqb.egg-info/dependency_links.txt
+-rw-r--r--   0 jacob     (1000) jacob     (1000)       59 2023-04-06 20:54:20.000000 syncqb-1.0.1/src/syncqb.egg-info/entry_points.txt
+-rw-r--r--   0 jacob     (1000) jacob     (1000)        7 2023-04-06 20:54:20.000000 syncqb-1.0.1/src/syncqb.egg-info/top_level.txt
+drwxr-xr-x   0 jacob     (1000) jacob     (1000)        0 2023-04-06 20:54:20.525324 syncqb-1.0.1/tests/
+-rw-r--r--   0 jacob     (1000) jacob     (1000)     1443 2023-04-06 15:05:02.000000 syncqb-1.0.1/tests/test.py
```

### Comparing `syncqb-1.0.0/LICENSE` & `syncqb-1.0.1/LICENSE`

 * *Files identical despite different names*

### Comparing `syncqb-1.0.0/PKG-INFO` & `syncqb-1.0.1/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: syncqb
-Version: 1.0.0
+Version: 1.0.1
 Summary: A Python SDK for quickbase
 Author-email: Jacob Gearhardt <jacob@synctivate.com>
 License: Copyright (c) 2018 The Python Packaging Authority
         
         Permission is hereby granted, free of charge, to any person obtaining a copy
         of this software and associated documentation files (the "Software"), to deal
         in the Software without restriction, including without limitation the rights
```

### Comparing `syncqb-1.0.0/README.md` & `syncqb-1.0.1/README.md`

 * *Files identical despite different names*

### Comparing `syncqb-1.0.0/pyproject.toml` & `syncqb-1.0.1/pyproject.toml`

 * *Files 2% similar despite different names*

```diff
@@ -1,14 +1,14 @@
 [build-system]
 requires = ["setuptools>=61.0",'requests','lxml','chardet']
 build-backend = "setuptools.build_meta"
 
 [project]
 name = "syncqb"
-version = "1.0.0"
+version = "1.0.1"
 authors = [
   { name="Jacob Gearhardt", email="jacob@synctivate.com" },
 ]
 description = "A Python SDK for quickbase"
 readme = "README.md"
 license = { file="LICENSE" }
 requires-python = ">=3.6"
```

### Comparing `syncqb-1.0.0/src/syncqb/json_quickbase.py` & `syncqb-1.0.1/src/syncqb/json_quickbase.py`

 * *Files 1% similar despite different names*

```diff
@@ -25,18 +25,19 @@
     # ---------------------------------------- core request functions ----------------------------------------
     def _attempt_request(self, url, action, params=None, body=None, json=True):
         tries = 0
 
         while tries < 10:
             try:
                 return self._request(url, action, params=params, body=body, json=json)
-            except ConnectionError or QBResponseError:
+            except requests.exceptions.Timeout or QBResponseError:
                 tries += 1
                 time.sleep(1)
                 pass
+        raise QBConnectionError('Connection Error: Timeout')
 
     def _request(self, url, action, params=None, body=None, json=True):
         kwargs = {
             'headers': self.headers,
             'timeout': self.timeout,
         }
         if params:
```

### Comparing `syncqb-1.0.0/src/syncqb/qb_client.py` & `syncqb-1.0.1/src/syncqb/qb_client.py`

 * *Files identical despite different names*

### Comparing `syncqb-1.0.0/src/syncqb/qb_errors.py` & `syncqb-1.0.1/src/syncqb/qb_errors.py`

 * *Files identical despite different names*

### Comparing `syncqb-1.0.0/src/syncqb/quickbase.py` & `syncqb-1.0.1/src/syncqb/quickbase.py`

 * *Files identical despite different names*

### Comparing `syncqb-1.0.0/src/syncqb/xml_quickbase.py` & `syncqb-1.0.1/src/syncqb/xml_quickbase.py`

 * *Files 0% similar despite different names*

```diff
@@ -32,41 +32,43 @@
         if action == 'files':
             headers = {'cookie': f'ticket={self.ticket}'}
         else:
             headers = {
                 'content-type': 'application/xml',
                 'QUICKBASE-ACTION': f'API_{action}',
             }
-        while True:
+        tries = 0
+        while tries < 10:
             try:
-                response = self._make_request(url, data, headers, type)
-                break
-            except requests.exceptions.Timeout:
+                return self._make_request(url, data, headers, type)
+            except requests.exceptions.Timeout or QBConnectionError:
                 print('Timeout error, retrying...')
+                tries += 1
                 time.sleep(1)
+        raise QBConnectionError('Connection Error: Timeout')
+
+    def _make_request(self, url, data, headers, type):
+        if type == 'POST':
+            response =  requests.post(url, data=data, headers=headers, timeout=self.timeout)
+        elif type == 'GET':
+            response = requests.get(url, headers=headers, timeout=self.timeout)
 
         if response.status_code == 401 or response.status_code == 403:
             raise QBAuthError('Invalid credentials')
         elif response.status_code == 404:
             raise QBConnectionError('Connection Error: Invalid URL')
         elif response.status_code == 400:
             raise QBResponseError('Response Error: Invalid request', response)
         elif response.status_code == 429:
             raise QBResponseError('Response Error: Too many requests', response)
         elif response.status_code == 500:
             raise QBResponseError('Response Error: Internal Quickbase Server Error', response)
         
         return response.content
 
-    def _make_request(self, url, data, headers, type):
-        if type == 'POST':
-            return requests.post(url, data=data, headers=headers, timeout=self.timeout)
-        elif type == 'GET':
-            return requests.get(url, headers=headers, timeout=self.timeout)
-
     def _build_xml(self, data):
         if self.ticket:
             data['ticket'] = self.ticket
         if self.apptoken:
             data['apptoken'] = self.apptoken
 
         request = etree.Element('qdbapi')
```

### Comparing `syncqb-1.0.0/src/syncqb.egg-info/PKG-INFO` & `syncqb-1.0.1/src/syncqb.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: syncqb
-Version: 1.0.0
+Version: 1.0.1
 Summary: A Python SDK for quickbase
 Author-email: Jacob Gearhardt <jacob@synctivate.com>
 License: Copyright (c) 2018 The Python Packaging Authority
         
         Permission is hereby granted, free of charge, to any person obtaining a copy
         of this software and associated documentation files (the "Software"), to deal
         in the Software without restriction, including without limitation the rights
```

### Comparing `syncqb-1.0.0/tests/test.py` & `syncqb-1.0.1/tests/test.py`

 * *Files identical despite different names*

