# Comparing `tmp/venra-0.1.3.tar.gz` & `tmp/venra-0.1.4.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "venra-0.1.3.tar", last modified: Thu Oct 13 13:57:14 2022, max compression
+gzip compressed data, was "venra-0.1.4.tar", last modified: Thu Apr  6 14:50:58 2023, max compression
```

## Comparing `venra-0.1.3.tar` & `venra-0.1.4.tar`

### file list

```diff
@@ -1,22 +1,22 @@
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-10-13 13:57:14.088052 venra-0.1.3/
--rw-r--r--   0 runner    (1001) docker     (121)     1079 2022-10-13 13:57:02.000000 venra-0.1.3/LICENSE
--rw-r--r--   0 runner    (1001) docker     (121)     3385 2022-10-13 13:57:14.088052 venra-0.1.3/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (121)     2533 2022-10-13 13:57:02.000000 venra-0.1.3/README.md
--rw-r--r--   0 runner    (1001) docker     (121)       38 2022-10-13 13:57:14.088052 venra-0.1.3/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (121)     1200 2022-10-13 13:57:02.000000 venra-0.1.3/setup.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-10-13 13:57:14.088052 venra-0.1.3/venra/
--rw-r--r--   0 runner    (1001) docker     (121)      983 2022-10-13 13:57:02.000000 venra-0.1.3/venra/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)       22 2022-10-13 13:57:02.000000 venra-0.1.3/venra/__version__.py
--rw-r--r--   0 runner    (1001) docker     (121)     2486 2022-10-13 13:57:02.000000 venra-0.1.3/venra/client.py
--rw-r--r--   0 runner    (1001) docker     (121)     1233 2022-10-13 13:57:02.000000 venra-0.1.3/venra/config.py
--rw-r--r--   0 runner    (1001) docker     (121)     3817 2022-10-13 13:57:02.000000 venra-0.1.3/venra/document.py
--rw-r--r--   0 runner    (1001) docker     (121)      556 2022-10-13 13:57:02.000000 venra-0.1.3/venra/exceptions.py
--rw-r--r--   0 runner    (1001) docker     (121)     6113 2022-10-13 13:57:02.000000 venra-0.1.3/venra/query.py
--rw-r--r--   0 runner    (1001) docker     (121)     1935 2022-10-13 13:57:02.000000 venra-0.1.3/venra/system.py
--rw-r--r--   0 runner    (1001) docker     (121)     1753 2022-10-13 13:57:02.000000 venra-0.1.3/venra/visit.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-10-13 13:57:14.088052 venra-0.1.3/venra.egg-info/
--rw-r--r--   0 runner    (1001) docker     (121)     3385 2022-10-13 13:57:14.000000 venra-0.1.3/venra.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (121)      325 2022-10-13 13:57:14.000000 venra-0.1.3/venra.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (121)        1 2022-10-13 13:57:14.000000 venra-0.1.3/venra.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (121)       19 2022-10-13 13:57:14.000000 venra-0.1.3/venra.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (121)        6 2022-10-13 13:57:14.000000 venra-0.1.3/venra.egg-info/top_level.txt
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 14:50:57.997521 venra-0.1.4/
+-rw-r--r--   0 runner    (1001) docker     (123)     1079 2023-04-06 14:50:48.000000 venra-0.1.4/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (123)     3385 2023-04-06 14:50:57.997521 venra-0.1.4/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     2533 2023-04-06 14:50:48.000000 venra-0.1.4/README.md
+-rw-r--r--   0 runner    (1001) docker     (123)       38 2023-04-06 14:50:57.997521 venra-0.1.4/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (123)     1200 2023-04-06 14:50:48.000000 venra-0.1.4/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 14:50:57.997521 venra-0.1.4/venra/
+-rw-r--r--   0 runner    (1001) docker     (123)      983 2023-04-06 14:50:48.000000 venra-0.1.4/venra/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)       22 2023-04-06 14:50:48.000000 venra-0.1.4/venra/__version__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2486 2023-04-06 14:50:48.000000 venra-0.1.4/venra/client.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1233 2023-04-06 14:50:48.000000 venra-0.1.4/venra/config.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3817 2023-04-06 14:50:48.000000 venra-0.1.4/venra/document.py
+-rw-r--r--   0 runner    (1001) docker     (123)      556 2023-04-06 14:50:48.000000 venra-0.1.4/venra/exceptions.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6113 2023-04-06 14:50:48.000000 venra-0.1.4/venra/query.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1935 2023-04-06 14:50:48.000000 venra-0.1.4/venra/system.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1957 2023-04-06 14:50:48.000000 venra-0.1.4/venra/visit.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 14:50:57.997521 venra-0.1.4/venra.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)     3385 2023-04-06 14:50:57.000000 venra-0.1.4/venra.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)      325 2023-04-06 14:50:57.000000 venra-0.1.4/venra.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-06 14:50:57.000000 venra-0.1.4/venra.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       19 2023-04-06 14:50:57.000000 venra-0.1.4/venra.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        6 2023-04-06 14:50:57.000000 venra-0.1.4/venra.egg-info/top_level.txt
```

### Comparing `venra-0.1.3/LICENSE` & `venra-0.1.4/LICENSE`

 * *Files identical despite different names*

### Comparing `venra-0.1.3/PKG-INFO` & `venra-0.1.4/PKG-INFO`

 * *Files 3% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: venra
-Version: 0.1.3
+Version: 0.1.4
 Summary: Venra provides a simple, high-level api for vespa.ai.
 Home-page: https://github.com/codycollier/venra
 Author: Cody Collier
 Author-email: cody@telnet.org
 License: MIT
 Keywords: artificial intelligence,information retrieval,machine learning,search
 Classifier: Development Status :: 4 - Beta
```

### Comparing `venra-0.1.3/README.md` & `venra-0.1.4/README.md`

 * *Files identical despite different names*

### Comparing `venra-0.1.3/setup.py` & `venra-0.1.4/setup.py`

 * *Files identical despite different names*

### Comparing `venra-0.1.3/venra/__init__.py` & `venra-0.1.4/venra/__init__.py`

 * *Files identical despite different names*

### Comparing `venra-0.1.3/venra/client.py` & `venra-0.1.4/venra/client.py`

 * *Files identical despite different names*

### Comparing `venra-0.1.3/venra/config.py` & `venra-0.1.4/venra/config.py`

 * *Files identical despite different names*

### Comparing `venra-0.1.3/venra/document.py` & `venra-0.1.4/venra/document.py`

 * *Files identical despite different names*

### Comparing `venra-0.1.3/venra/exceptions.py` & `venra-0.1.4/venra/exceptions.py`

 * *Files identical despite different names*

### Comparing `venra-0.1.3/venra/query.py` & `venra-0.1.4/venra/query.py`

 * *Files identical despite different names*

### Comparing `venra-0.1.3/venra/system.py` & `venra-0.1.4/venra/system.py`

 * *Files identical despite different names*

### Comparing `venra-0.1.3/venra/visit.py` & `venra-0.1.4/venra/visit.py`

 * *Files 12% similar despite different names*

```diff
@@ -26,21 +26,26 @@
 
 def _vespa_get(namespace, doctype, selection=None, continuation=None):
     """Internal wrapper for visit api http call handling"""
     base_uri = f"{config.vespa_host_app}/document/v1/{namespace}/{doctype}/docid"
 
     vc = client.get_vespa_client()
 
-    if selection:
-        vr = vc.get(f"{base_uri}?selection={selection}")
-    elif continuation:
-        vr = vc.get(f"{base_uri}?continuation={continuation}")
-    else:
+    if not selection and not continuation:
         vr = vc.get(f"{base_uri}")
 
+    elif not selection and continuation:
+        vr = vc.get(f"{base_uri}?continuation={continuation}")
+
+    elif selection and not continuation:
+        vr = vc.get(f"{base_uri}?selection={selection}")
+
+    elif selection and continuation:
+        vr = vc.get(f"{base_uri}?selection={selection}&continuation={continuation}")
+
     _api_err_check(vr) 
     vr = vr.json()
 
     return vr
 
 
 def feed(namespace, doctype, selection=None, fields_only=True):
@@ -62,11 +67,11 @@
 
         # check for continuation / more results
         continuation = vr.get("continuation", False)
         if not continuation:
             break
 
         # retrieve the next set of results
-        vr = _vespa_get(namespace, doctype, None, continuation)
+        vr = _vespa_get(namespace, doctype, selection, continuation)
 
     return
```

### Comparing `venra-0.1.3/venra.egg-info/PKG-INFO` & `venra-0.1.4/venra.egg-info/PKG-INFO`

 * *Files 3% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: venra
-Version: 0.1.3
+Version: 0.1.4
 Summary: Venra provides a simple, high-level api for vespa.ai.
 Home-page: https://github.com/codycollier/venra
 Author: Cody Collier
 Author-email: cody@telnet.org
 License: MIT
 Keywords: artificial intelligence,information retrieval,machine learning,search
 Classifier: Development Status :: 4 - Beta
```

