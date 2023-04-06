# Comparing `tmp/mlserver-huggingface-1.3.0rc1.tar.gz` & `tmp/mlserver-huggingface-1.3.0rc2.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "mlserver-huggingface-1.3.0rc1.tar", last modified: Thu Apr  6 13:36:32 2023, max compression
+gzip compressed data, was "mlserver-huggingface-1.3.0rc2.tar", last modified: Thu Apr  6 15:39:25 2023, max compression
```

## Comparing `mlserver-huggingface-1.3.0rc1.tar` & `mlserver-huggingface-1.3.0rc2.tar`

### file list

```diff
@@ -1,30 +1,30 @@
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 13:36:32.842879 mlserver-huggingface-1.3.0rc1/
--rw-r--r--   0 runner    (1001) docker     (123)    11354 2023-04-06 13:35:49.000000 mlserver-huggingface-1.3.0rc1/LICENSE
--rw-r--r--   0 runner    (1001) docker     (123)     2093 2023-04-06 13:36:32.842879 mlserver-huggingface-1.3.0rc1/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)     1329 2023-04-06 13:35:49.000000 mlserver-huggingface-1.3.0rc1/README.md
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 13:36:32.838879 mlserver-huggingface-1.3.0rc1/mlserver_huggingface/
--rw-r--r--   0 runner    (1001) docker     (123)       74 2023-04-06 13:35:49.000000 mlserver-huggingface-1.3.0rc1/mlserver_huggingface/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 13:36:32.842879 mlserver-huggingface-1.3.0rc1/mlserver_huggingface/codecs/
--rw-r--r--   0 runner    (1001) docker     (123)      593 2023-04-06 13:35:49.000000 mlserver-huggingface-1.3.0rc1/mlserver_huggingface/codecs/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     6724 2023-04-06 13:35:49.000000 mlserver-huggingface-1.3.0rc1/mlserver_huggingface/codecs/base.py
--rw-r--r--   0 runner    (1001) docker     (123)     1976 2023-04-06 13:35:49.000000 mlserver-huggingface-1.3.0rc1/mlserver_huggingface/codecs/conversation.py
--rw-r--r--   0 runner    (1001) docker     (123)     2464 2023-04-06 13:35:49.000000 mlserver-huggingface-1.3.0rc1/mlserver_huggingface/codecs/image.py
--rw-r--r--   0 runner    (1001) docker     (123)     1745 2023-04-06 13:35:49.000000 mlserver-huggingface-1.3.0rc1/mlserver_huggingface/codecs/json.py
--rw-r--r--   0 runner    (1001) docker     (123)     1938 2023-04-06 13:35:49.000000 mlserver-huggingface-1.3.0rc1/mlserver_huggingface/codecs/jsonlist.py
--rw-r--r--   0 runner    (1001) docker     (123)     2154 2023-04-06 13:35:49.000000 mlserver-huggingface-1.3.0rc1/mlserver_huggingface/codecs/numpylist.py
--rw-r--r--   0 runner    (1001) docker     (123)     1560 2023-04-06 13:35:49.000000 mlserver-huggingface-1.3.0rc1/mlserver_huggingface/codecs/raw.py
--rw-r--r--   0 runner    (1001) docker     (123)     5541 2023-04-06 13:35:49.000000 mlserver-huggingface-1.3.0rc1/mlserver_huggingface/codecs/utils.py
--rw-r--r--   0 runner    (1001) docker     (123)     1824 2023-04-06 13:35:49.000000 mlserver-huggingface-1.3.0rc1/mlserver_huggingface/common.py
--rw-r--r--   0 runner    (1001) docker     (123)     1291 2023-04-06 13:35:49.000000 mlserver-huggingface-1.3.0rc1/mlserver_huggingface/errors.py
--rw-r--r--   0 runner    (1001) docker     (123)     9842 2023-04-06 13:35:49.000000 mlserver-huggingface-1.3.0rc1/mlserver_huggingface/metadata.py
--rw-r--r--   0 runner    (1001) docker     (123)     1970 2023-04-06 13:35:49.000000 mlserver-huggingface-1.3.0rc1/mlserver_huggingface/runtime.py
--rw-r--r--   0 runner    (1001) docker     (123)     4588 2023-04-06 13:35:49.000000 mlserver-huggingface-1.3.0rc1/mlserver_huggingface/settings.py
--rw-r--r--   0 runner    (1001) docker     (123)       26 2023-04-06 13:35:49.000000 mlserver-huggingface-1.3.0rc1/mlserver_huggingface/version.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 13:36:32.838879 mlserver-huggingface-1.3.0rc1/mlserver_huggingface.egg-info/
--rw-r--r--   0 runner    (1001) docker     (123)     2093 2023-04-06 13:36:32.000000 mlserver-huggingface-1.3.0rc1/mlserver_huggingface.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)      816 2023-04-06 13:36:32.000000 mlserver-huggingface-1.3.0rc1/mlserver_huggingface.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-06 13:36:32.000000 mlserver-huggingface-1.3.0rc1/mlserver_huggingface.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (123)       51 2023-04-06 13:36:32.000000 mlserver-huggingface-1.3.0rc1/mlserver_huggingface.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (123)       21 2023-04-06 13:36:32.000000 mlserver-huggingface-1.3.0rc1/mlserver_huggingface.egg-info/top_level.txt
--rw-r--r--   0 runner    (1001) docker     (123)       38 2023-04-06 13:36:32.842879 mlserver-huggingface-1.3.0rc1/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (123)     1183 2023-04-06 13:35:49.000000 mlserver-huggingface-1.3.0rc1/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 15:39:25.148881 mlserver-huggingface-1.3.0rc2/
+-rw-r--r--   0 runner    (1001) docker     (123)    11354 2023-04-06 15:38:51.000000 mlserver-huggingface-1.3.0rc2/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (123)     2093 2023-04-06 15:39:25.148881 mlserver-huggingface-1.3.0rc2/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     1329 2023-04-06 15:38:51.000000 mlserver-huggingface-1.3.0rc2/README.md
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 15:39:25.148881 mlserver-huggingface-1.3.0rc2/mlserver_huggingface/
+-rw-r--r--   0 runner    (1001) docker     (123)       74 2023-04-06 15:38:51.000000 mlserver-huggingface-1.3.0rc2/mlserver_huggingface/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 15:39:25.148881 mlserver-huggingface-1.3.0rc2/mlserver_huggingface/codecs/
+-rw-r--r--   0 runner    (1001) docker     (123)      593 2023-04-06 15:38:51.000000 mlserver-huggingface-1.3.0rc2/mlserver_huggingface/codecs/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6724 2023-04-06 15:38:51.000000 mlserver-huggingface-1.3.0rc2/mlserver_huggingface/codecs/base.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1976 2023-04-06 15:38:51.000000 mlserver-huggingface-1.3.0rc2/mlserver_huggingface/codecs/conversation.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2464 2023-04-06 15:38:51.000000 mlserver-huggingface-1.3.0rc2/mlserver_huggingface/codecs/image.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1745 2023-04-06 15:38:51.000000 mlserver-huggingface-1.3.0rc2/mlserver_huggingface/codecs/json.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1938 2023-04-06 15:38:51.000000 mlserver-huggingface-1.3.0rc2/mlserver_huggingface/codecs/jsonlist.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2154 2023-04-06 15:38:51.000000 mlserver-huggingface-1.3.0rc2/mlserver_huggingface/codecs/numpylist.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1560 2023-04-06 15:38:51.000000 mlserver-huggingface-1.3.0rc2/mlserver_huggingface/codecs/raw.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5541 2023-04-06 15:38:51.000000 mlserver-huggingface-1.3.0rc2/mlserver_huggingface/codecs/utils.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1824 2023-04-06 15:38:51.000000 mlserver-huggingface-1.3.0rc2/mlserver_huggingface/common.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1291 2023-04-06 15:38:51.000000 mlserver-huggingface-1.3.0rc2/mlserver_huggingface/errors.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9842 2023-04-06 15:38:51.000000 mlserver-huggingface-1.3.0rc2/mlserver_huggingface/metadata.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1970 2023-04-06 15:38:51.000000 mlserver-huggingface-1.3.0rc2/mlserver_huggingface/runtime.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4588 2023-04-06 15:38:51.000000 mlserver-huggingface-1.3.0rc2/mlserver_huggingface/settings.py
+-rw-r--r--   0 runner    (1001) docker     (123)       26 2023-04-06 15:38:51.000000 mlserver-huggingface-1.3.0rc2/mlserver_huggingface/version.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 15:39:25.148881 mlserver-huggingface-1.3.0rc2/mlserver_huggingface.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)     2093 2023-04-06 15:39:25.000000 mlserver-huggingface-1.3.0rc2/mlserver_huggingface.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)      816 2023-04-06 15:39:25.000000 mlserver-huggingface-1.3.0rc2/mlserver_huggingface.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-06 15:39:25.000000 mlserver-huggingface-1.3.0rc2/mlserver_huggingface.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       51 2023-04-06 15:39:25.000000 mlserver-huggingface-1.3.0rc2/mlserver_huggingface.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       21 2023-04-06 15:39:25.000000 mlserver-huggingface-1.3.0rc2/mlserver_huggingface.egg-info/top_level.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       38 2023-04-06 15:39:25.148881 mlserver-huggingface-1.3.0rc2/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (123)     1183 2023-04-06 15:38:51.000000 mlserver-huggingface-1.3.0rc2/setup.py
```

### Comparing `mlserver-huggingface-1.3.0rc1/LICENSE` & `mlserver-huggingface-1.3.0rc2/LICENSE`

 * *Files identical despite different names*

### Comparing `mlserver-huggingface-1.3.0rc1/PKG-INFO` & `mlserver-huggingface-1.3.0rc2/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: mlserver-huggingface
-Version: 1.3.0rc1
+Version: 1.3.0rc2
 Summary: HuggingFace runtime for MLServer
 Home-page: https://github.com/SeldonIO/MLServer.git
 Author: Seldon Technologies Ltd.
 Author-email: hello@seldon.io
 License: Apache 2.0
 Description: # HuggingFace runtime for MLServer
```

### Comparing `mlserver-huggingface-1.3.0rc1/README.md` & `mlserver-huggingface-1.3.0rc2/README.md`

 * *Files identical despite different names*

### Comparing `mlserver-huggingface-1.3.0rc1/mlserver_huggingface/codecs/__init__.py` & `mlserver-huggingface-1.3.0rc2/mlserver_huggingface/codecs/__init__.py`

 * *Files identical despite different names*

### Comparing `mlserver-huggingface-1.3.0rc1/mlserver_huggingface/codecs/base.py` & `mlserver-huggingface-1.3.0rc2/mlserver_huggingface/codecs/base.py`

 * *Files identical despite different names*

### Comparing `mlserver-huggingface-1.3.0rc1/mlserver_huggingface/codecs/conversation.py` & `mlserver-huggingface-1.3.0rc2/mlserver_huggingface/codecs/conversation.py`

 * *Files identical despite different names*

### Comparing `mlserver-huggingface-1.3.0rc1/mlserver_huggingface/codecs/image.py` & `mlserver-huggingface-1.3.0rc2/mlserver_huggingface/codecs/image.py`

 * *Files identical despite different names*

### Comparing `mlserver-huggingface-1.3.0rc1/mlserver_huggingface/codecs/json.py` & `mlserver-huggingface-1.3.0rc2/mlserver_huggingface/codecs/json.py`

 * *Files identical despite different names*

### Comparing `mlserver-huggingface-1.3.0rc1/mlserver_huggingface/codecs/jsonlist.py` & `mlserver-huggingface-1.3.0rc2/mlserver_huggingface/codecs/jsonlist.py`

 * *Files identical despite different names*

### Comparing `mlserver-huggingface-1.3.0rc1/mlserver_huggingface/codecs/numpylist.py` & `mlserver-huggingface-1.3.0rc2/mlserver_huggingface/codecs/numpylist.py`

 * *Files identical despite different names*

### Comparing `mlserver-huggingface-1.3.0rc1/mlserver_huggingface/codecs/raw.py` & `mlserver-huggingface-1.3.0rc2/mlserver_huggingface/codecs/raw.py`

 * *Files identical despite different names*

### Comparing `mlserver-huggingface-1.3.0rc1/mlserver_huggingface/codecs/utils.py` & `mlserver-huggingface-1.3.0rc2/mlserver_huggingface/codecs/utils.py`

 * *Files identical despite different names*

### Comparing `mlserver-huggingface-1.3.0rc1/mlserver_huggingface/common.py` & `mlserver-huggingface-1.3.0rc2/mlserver_huggingface/common.py`

 * *Files identical despite different names*

### Comparing `mlserver-huggingface-1.3.0rc1/mlserver_huggingface/errors.py` & `mlserver-huggingface-1.3.0rc2/mlserver_huggingface/errors.py`

 * *Files identical despite different names*

### Comparing `mlserver-huggingface-1.3.0rc1/mlserver_huggingface/metadata.py` & `mlserver-huggingface-1.3.0rc2/mlserver_huggingface/metadata.py`

 * *Files identical despite different names*

### Comparing `mlserver-huggingface-1.3.0rc1/mlserver_huggingface/runtime.py` & `mlserver-huggingface-1.3.0rc2/mlserver_huggingface/runtime.py`

 * *Files identical despite different names*

### Comparing `mlserver-huggingface-1.3.0rc1/mlserver_huggingface/settings.py` & `mlserver-huggingface-1.3.0rc2/mlserver_huggingface/settings.py`

 * *Files identical despite different names*

### Comparing `mlserver-huggingface-1.3.0rc1/mlserver_huggingface.egg-info/PKG-INFO` & `mlserver-huggingface-1.3.0rc2/mlserver_huggingface.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: mlserver-huggingface
-Version: 1.3.0rc1
+Version: 1.3.0rc2
 Summary: HuggingFace runtime for MLServer
 Home-page: https://github.com/SeldonIO/MLServer.git
 Author: Seldon Technologies Ltd.
 Author-email: hello@seldon.io
 License: Apache 2.0
 Description: # HuggingFace runtime for MLServer
```

### Comparing `mlserver-huggingface-1.3.0rc1/mlserver_huggingface.egg-info/SOURCES.txt` & `mlserver-huggingface-1.3.0rc2/mlserver_huggingface.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `mlserver-huggingface-1.3.0rc1/setup.py` & `mlserver-huggingface-1.3.0rc2/setup.py`

 * *Files identical despite different names*

