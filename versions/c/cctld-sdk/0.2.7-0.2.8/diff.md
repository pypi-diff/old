# Comparing `tmp/cctld-sdk-0.2.7.tar.gz` & `tmp/cctld-sdk-0.2.8.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "cctld-sdk-0.2.7.tar", last modified: Tue Mar 28 09:27:29 2023, max compression
+gzip compressed data, was "cctld-sdk-0.2.8.tar", last modified: Fri Apr  7 11:48:14 2023, max compression
```

## Comparing `cctld-sdk-0.2.7.tar` & `cctld-sdk-0.2.8.tar`

### file list

```diff
@@ -1,30 +1,30 @@
-drwxrwxrwx   0        0        0        0 2023-03-28 09:27:29.030347 cctld-sdk-0.2.7/
--rw-rw-rw-   0        0        0      144 2023-03-28 09:27:29.030347 cctld-sdk-0.2.7/PKG-INFO
--rw-rw-rw-   0        0        0        0 2022-06-03 13:18:40.000000 cctld-sdk-0.2.7/README.md
-drwxrwxrwx   0        0        0        0 2023-03-28 09:27:28.917796 cctld-sdk-0.2.7/cctld_sdk/
--rw-rw-rw-   0        0        0        0 2022-06-03 13:18:40.000000 cctld-sdk-0.2.7/cctld_sdk/__init__.py
-drwxrwxrwx   0        0        0        0 2023-03-28 09:27:29.002834 cctld-sdk-0.2.7/cctld_sdk/api/
--rw-rw-rw-   0        0        0      117 2022-07-19 06:16:07.000000 cctld-sdk-0.2.7/cctld_sdk/api/__init__.py
--rw-rw-rw-   0        0        0     2559 2022-12-21 09:31:33.000000 cctld-sdk-0.2.7/cctld_sdk/api/base_api.py
--rw-rw-rw-   0        0        0     1635 2022-08-17 09:20:39.000000 cctld-sdk-0.2.7/cctld_sdk/api/contact.py
--rw-rw-rw-   0        0        0      318 2022-08-17 09:20:39.000000 cctld-sdk-0.2.7/cctld_sdk/api/decorator.py
--rw-rw-rw-   0        0        0     2292 2022-08-17 09:20:39.000000 cctld-sdk-0.2.7/cctld_sdk/api/domain.py
--rw-rw-rw-   0        0        0     1141 2022-08-17 09:20:39.000000 cctld-sdk-0.2.7/cctld_sdk/api/ns.py
--rw-rw-rw-   0        0        0      809 2022-08-17 09:20:39.000000 cctld-sdk-0.2.7/cctld_sdk/api/registrar.py
--rw-rw-rw-   0        0        0      321 2022-08-17 07:17:45.000000 cctld-sdk-0.2.7/cctld_sdk/cctld.py
-drwxrwxrwx   0        0        0        0 2023-03-28 09:27:29.009991 cctld-sdk-0.2.7/cctld_sdk/common/
--rw-rw-rw-   0        0        0        0 2022-06-03 13:18:40.000000 cctld-sdk-0.2.7/cctld_sdk/common/__init__.py
--rw-rw-rw-   0        0        0      657 2022-08-17 09:20:39.000000 cctld-sdk-0.2.7/cctld_sdk/common/exceptions.py
--rw-rw-rw-   0        0        0     1719 2022-12-21 15:01:42.000000 cctld-sdk-0.2.7/cctld_sdk/common/types.py
-drwxrwxrwx   0        0        0        0 2023-03-28 09:27:29.030347 cctld-sdk-0.2.7/cctld_sdk/models/
--rw-rw-rw-   0        0        0       47 2022-06-03 13:18:40.000000 cctld-sdk-0.2.7/cctld_sdk/models/__init__.py
--rw-rw-rw-   0        0        0     2434 2023-03-28 09:19:22.000000 cctld-sdk-0.2.7/cctld_sdk/models/contact.py
--rw-rw-rw-   0        0        0      270 2022-08-02 06:47:14.000000 cctld-sdk-0.2.7/cctld_sdk/models/domain.py
-drwxrwxrwx   0        0        0        0 2023-03-28 09:27:28.977884 cctld-sdk-0.2.7/cctld_sdk.egg-info/
--rw-rw-rw-   0        0        0      144 2023-03-28 09:27:28.000000 cctld-sdk-0.2.7/cctld_sdk.egg-info/PKG-INFO
--rw-rw-rw-   0        0        0      568 2023-03-28 09:27:28.000000 cctld-sdk-0.2.7/cctld_sdk.egg-info/SOURCES.txt
--rw-rw-rw-   0        0        0        1 2023-03-28 09:27:28.000000 cctld-sdk-0.2.7/cctld_sdk.egg-info/dependency_links.txt
--rw-rw-rw-   0        0        0       29 2023-03-28 09:27:28.000000 cctld-sdk-0.2.7/cctld_sdk.egg-info/requires.txt
--rw-rw-rw-   0        0        0       10 2023-03-28 09:27:28.000000 cctld-sdk-0.2.7/cctld_sdk.egg-info/top_level.txt
--rw-rw-rw-   0        0        0       42 2023-03-28 09:27:29.030347 cctld-sdk-0.2.7/setup.cfg
--rw-rw-rw-   0        0        0      434 2023-03-28 09:19:44.000000 cctld-sdk-0.2.7/setup.py
+drwxrwxrwx   0        0        0        0 2023-04-07 11:48:14.176120 cctld-sdk-0.2.8/
+-rw-rw-rw-   0        0        0      144 2023-04-07 11:48:14.176120 cctld-sdk-0.2.8/PKG-INFO
+-rw-rw-rw-   0        0        0        0 2022-06-03 13:18:40.000000 cctld-sdk-0.2.8/README.md
+drwxrwxrwx   0        0        0        0 2023-04-07 11:48:14.102172 cctld-sdk-0.2.8/cctld_sdk/
+-rw-rw-rw-   0        0        0        0 2022-06-03 13:18:40.000000 cctld-sdk-0.2.8/cctld_sdk/__init__.py
+drwxrwxrwx   0        0        0        0 2023-04-07 11:48:14.166846 cctld-sdk-0.2.8/cctld_sdk/api/
+-rw-rw-rw-   0        0        0      117 2022-07-19 06:16:07.000000 cctld-sdk-0.2.8/cctld_sdk/api/__init__.py
+-rw-rw-rw-   0        0        0     2559 2022-12-21 09:31:33.000000 cctld-sdk-0.2.8/cctld_sdk/api/base_api.py
+-rw-rw-rw-   0        0        0     1635 2023-03-31 11:19:53.000000 cctld-sdk-0.2.8/cctld_sdk/api/contact.py
+-rw-rw-rw-   0        0        0      318 2022-08-17 09:20:39.000000 cctld-sdk-0.2.8/cctld_sdk/api/decorator.py
+-rw-rw-rw-   0        0        0     2804 2023-04-07 11:46:20.000000 cctld-sdk-0.2.8/cctld_sdk/api/domain.py
+-rw-rw-rw-   0        0        0     1141 2022-08-17 09:20:39.000000 cctld-sdk-0.2.8/cctld_sdk/api/ns.py
+-rw-rw-rw-   0        0        0      809 2022-08-17 09:20:39.000000 cctld-sdk-0.2.8/cctld_sdk/api/registrar.py
+-rw-rw-rw-   0        0        0      321 2022-08-17 07:17:45.000000 cctld-sdk-0.2.8/cctld_sdk/cctld.py
+drwxrwxrwx   0        0        0        0 2023-04-07 11:48:14.171304 cctld-sdk-0.2.8/cctld_sdk/common/
+-rw-rw-rw-   0        0        0        0 2022-06-03 13:18:40.000000 cctld-sdk-0.2.8/cctld_sdk/common/__init__.py
+-rw-rw-rw-   0        0        0      657 2022-08-17 09:20:39.000000 cctld-sdk-0.2.8/cctld_sdk/common/exceptions.py
+-rw-rw-rw-   0        0        0     1719 2022-12-21 15:01:42.000000 cctld-sdk-0.2.8/cctld_sdk/common/types.py
+drwxrwxrwx   0        0        0        0 2023-04-07 11:48:14.176120 cctld-sdk-0.2.8/cctld_sdk/models/
+-rw-rw-rw-   0        0        0       47 2022-06-03 13:18:40.000000 cctld-sdk-0.2.8/cctld_sdk/models/__init__.py
+-rw-rw-rw-   0        0        0     2434 2023-03-28 09:19:22.000000 cctld-sdk-0.2.8/cctld_sdk/models/contact.py
+-rw-rw-rw-   0        0        0      270 2023-04-07 11:23:35.000000 cctld-sdk-0.2.8/cctld_sdk/models/domain.py
+drwxrwxrwx   0        0        0        0 2023-04-07 11:48:14.150632 cctld-sdk-0.2.8/cctld_sdk.egg-info/
+-rw-rw-rw-   0        0        0      144 2023-04-07 11:48:14.000000 cctld-sdk-0.2.8/cctld_sdk.egg-info/PKG-INFO
+-rw-rw-rw-   0        0        0      568 2023-04-07 11:48:14.000000 cctld-sdk-0.2.8/cctld_sdk.egg-info/SOURCES.txt
+-rw-rw-rw-   0        0        0        1 2023-04-07 11:48:14.000000 cctld-sdk-0.2.8/cctld_sdk.egg-info/dependency_links.txt
+-rw-rw-rw-   0        0        0       29 2023-04-07 11:48:14.000000 cctld-sdk-0.2.8/cctld_sdk.egg-info/requires.txt
+-rw-rw-rw-   0        0        0       10 2023-04-07 11:48:14.000000 cctld-sdk-0.2.8/cctld_sdk.egg-info/top_level.txt
+-rw-rw-rw-   0        0        0       42 2023-04-07 11:48:14.176120 cctld-sdk-0.2.8/setup.cfg
+-rw-rw-rw-   0        0        0      434 2023-04-07 11:46:48.000000 cctld-sdk-0.2.8/setup.py
```

### Comparing `cctld-sdk-0.2.7/cctld_sdk/api/base_api.py` & `cctld-sdk-0.2.8/cctld_sdk/api/base_api.py`

 * *Files identical despite different names*

### Comparing `cctld-sdk-0.2.7/cctld_sdk/api/contact.py` & `cctld-sdk-0.2.8/cctld_sdk/api/contact.py`

 * *Files identical despite different names*

### Comparing `cctld-sdk-0.2.7/cctld_sdk/api/domain.py` & `cctld-sdk-0.2.8/cctld_sdk/api/domain.py`

 * *Files 22% similar despite different names*

```diff
@@ -23,18 +23,33 @@
             action=CCTLDActions.DOMAIN_DETAIL_BY_DOMAIN_NAME, data=data
         )
 
     def domain_add(self, domain_obj: Domain):
         data = domain_obj.__dict__
         return self.send_command(action=CCTLDActions.DOMAIN_ADD, data=data)
 
-    def domain_edit(self, domain_id: int, domain_obj: Domain):
+    def domain_edit(self, domain_id: int, attrs_dict: dict):
+        """
+        attrs_dict should be :
+        {
+            "sCustID":int[required],
+            "sAdminID":int[required],
+            "sTechID": int[required],
+            "sBillID":int[required],
+            "pnsID":int[optional],
+            "snsID":int[optional],
+            "tnsID":int[optional],
+            "qnsID":int[optional],
+            "sDesc":str[optional],
+            "lWhois":int[optional]
+        }
+        note that include only required fields and fields you want to change in attrs_dict
+        """
         # sourcery skip: dict-assign-update-to-union
-        data = {"id": domain_id}
-        data.update(domain_obj.__dict__)
+        data = {"id": domain_id, **attrs_dict}
         return self.send_command(action=CCTLDActions.DOMAIN_EDIT, data=data)
 
     def domain_deleg_list(self, start_at: int = 0, count: int = 100):
         data = {"id": start_at, "count": count}
         return self.send_command(action=CCTLDActions.DOMAIN_DELEG_LIST, data=data)
 
     def domain_deleg(self, domain_id: int, year: int):
```

### Comparing `cctld-sdk-0.2.7/cctld_sdk/api/ns.py` & `cctld-sdk-0.2.8/cctld_sdk/api/ns.py`

 * *Files identical despite different names*

### Comparing `cctld-sdk-0.2.7/cctld_sdk/api/registrar.py` & `cctld-sdk-0.2.8/cctld_sdk/api/registrar.py`

 * *Files identical despite different names*

### Comparing `cctld-sdk-0.2.7/cctld_sdk/common/exceptions.py` & `cctld-sdk-0.2.8/cctld_sdk/common/exceptions.py`

 * *Files identical despite different names*

### Comparing `cctld-sdk-0.2.7/cctld_sdk/common/types.py` & `cctld-sdk-0.2.8/cctld_sdk/common/types.py`

 * *Files identical despite different names*

### Comparing `cctld-sdk-0.2.7/cctld_sdk/models/contact.py` & `cctld-sdk-0.2.8/cctld_sdk/models/contact.py`

 * *Files identical despite different names*

### Comparing `cctld-sdk-0.2.7/cctld_sdk.egg-info/SOURCES.txt` & `cctld-sdk-0.2.8/cctld_sdk.egg-info/SOURCES.txt`

 * *Files identical despite different names*

