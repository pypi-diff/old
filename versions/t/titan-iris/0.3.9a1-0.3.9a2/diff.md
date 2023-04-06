# Comparing `tmp/titan-iris-0.3.9a1.tar.gz` & `tmp/titan-iris-0.3.9a2.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "titan-iris-0.3.9a1.tar", last modified: Mon Apr  3 21:24:02 2023, max compression
+gzip compressed data, was "titan-iris-0.3.9a2.tar", last modified: Tue Apr  4 06:56:06 2023, max compression
```

## Comparing `titan-iris-0.3.9a1.tar` & `titan-iris-0.3.9a2.tar`

### file list

```diff
@@ -1,33 +1,33 @@
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-03 21:24:02.331125 titan-iris-0.3.9a1/
--rw-r--r--   0 runner    (1001) docker     (123)     2240 2023-04-03 21:23:49.000000 titan-iris-0.3.9a1/.gitignore
--rw-r--r--   0 runner    (1001) docker     (123)      699 2023-04-03 21:23:49.000000 titan-iris-0.3.9a1/Dockerfile
--rw-r--r--   0 runner    (1001) docker     (123)       15 2023-04-03 21:23:49.000000 titan-iris-0.3.9a1/MANIFEST.in
--rw-r--r--   0 runner    (1001) docker     (123)     2130 2023-04-03 21:24:02.331125 titan-iris-0.3.9a1/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)     2033 2023-04-03 21:23:49.000000 titan-iris-0.3.9a1/README.md
--rw-r--r--   0 runner    (1001) docker     (123)       30 2023-04-03 21:23:49.000000 titan-iris-0.3.9a1/pytest.ini
--rw-r--r--   0 runner    (1001) docker     (123)      217 2023-04-03 21:23:49.000000 titan-iris-0.3.9a1/requirements.txt
--rw-r--r--   0 runner    (1001) docker     (123)       15 2023-04-03 21:23:49.000000 titan-iris-0.3.9a1/requirements_dev.txt
--rw-r--r--   0 runner    (1001) docker     (123)      160 2023-04-03 21:24:02.331125 titan-iris-0.3.9a1/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (123)      698 2023-04-03 21:23:49.000000 titan-iris-0.3.9a1/setup.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-03 21:24:02.331125 titan-iris-0.3.9a1/src/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-03 21:24:02.331125 titan-iris-0.3.9a1/src/iris/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-03 21:23:49.000000 titan-iris-0.3.9a1/src/iris/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      649 2023-04-03 21:23:49.000000 titan-iris-0.3.9a1/src/iris/config.yaml
--rw-r--r--   0 runner    (1001) docker     (123)    18057 2023-04-03 21:23:49.000000 titan-iris-0.3.9a1/src/iris/main.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-03 21:24:02.331125 titan-iris-0.3.9a1/src/iris/sdk/
--rw-r--r--   0 runner    (1001) docker     (123)       24 2023-04-03 21:23:49.000000 titan-iris-0.3.9a1/src/iris/sdk/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    10740 2023-04-03 21:23:49.000000 titan-iris-0.3.9a1/src/iris/sdk/auth_utils.py
--rw-r--r--   0 runner    (1001) docker     (123)     4812 2023-04-03 21:23:49.000000 titan-iris-0.3.9a1/src/iris/sdk/conf_manager.py
--rw-r--r--   0 runner    (1001) docker     (123)     6123 2023-04-03 21:23:49.000000 titan-iris-0.3.9a1/src/iris/sdk/exception.py
--rw-r--r--   0 runner    (1001) docker     (123)    23192 2023-04-03 21:23:49.000000 titan-iris-0.3.9a1/src/iris/sdk/iris_sdk.py
--rw-r--r--   0 runner    (1001) docker     (123)     4099 2023-04-03 21:23:49.000000 titan-iris-0.3.9a1/src/iris/sdk/safe_convert.py
--rw-r--r--   0 runner    (1001) docker     (123)     7377 2023-04-03 21:23:49.000000 titan-iris-0.3.9a1/src/iris/sdk/utils.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-03 21:24:02.331125 titan-iris-0.3.9a1/src/titan_iris.egg-info/
--rw-r--r--   0 runner    (1001) docker     (123)     2130 2023-04-03 21:24:01.000000 titan-iris-0.3.9a1/src/titan_iris.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)      601 2023-04-03 21:24:02.000000 titan-iris-0.3.9a1/src/titan_iris.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-03 21:24:01.000000 titan-iris-0.3.9a1/src/titan_iris.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (123)       40 2023-04-03 21:24:01.000000 titan-iris-0.3.9a1/src/titan_iris.egg-info/entry_points.txt
--rw-r--r--   0 runner    (1001) docker     (123)      195 2023-04-03 21:24:01.000000 titan-iris-0.3.9a1/src/titan_iris.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (123)        5 2023-04-03 21:24:01.000000 titan-iris-0.3.9a1/src/titan_iris.egg-info/top_level.txt
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-03 21:24:02.331125 titan-iris-0.3.9a1/tests/
--rw-r--r--   0 runner    (1001) docker     (123)     3040 2023-04-03 21:23:49.000000 titan-iris-0.3.9a1/tests/test_cli.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-04 06:56:06.914348 titan-iris-0.3.9a2/
+-rw-r--r--   0 runner    (1001) docker     (123)     2240 2023-04-04 06:55:49.000000 titan-iris-0.3.9a2/.gitignore
+-rw-r--r--   0 runner    (1001) docker     (123)      699 2023-04-04 06:55:49.000000 titan-iris-0.3.9a2/Dockerfile
+-rw-r--r--   0 runner    (1001) docker     (123)       15 2023-04-04 06:55:49.000000 titan-iris-0.3.9a2/MANIFEST.in
+-rw-r--r--   0 runner    (1001) docker     (123)     2130 2023-04-04 06:56:06.914348 titan-iris-0.3.9a2/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     2033 2023-04-04 06:55:49.000000 titan-iris-0.3.9a2/README.md
+-rw-r--r--   0 runner    (1001) docker     (123)       30 2023-04-04 06:55:49.000000 titan-iris-0.3.9a2/pytest.ini
+-rw-r--r--   0 runner    (1001) docker     (123)      217 2023-04-04 06:55:49.000000 titan-iris-0.3.9a2/requirements.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       15 2023-04-04 06:55:49.000000 titan-iris-0.3.9a2/requirements_dev.txt
+-rw-r--r--   0 runner    (1001) docker     (123)      160 2023-04-04 06:56:06.918348 titan-iris-0.3.9a2/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (123)      698 2023-04-04 06:55:49.000000 titan-iris-0.3.9a2/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-04 06:56:06.902348 titan-iris-0.3.9a2/src/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-04 06:56:06.910348 titan-iris-0.3.9a2/src/iris/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-04 06:55:49.000000 titan-iris-0.3.9a2/src/iris/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      649 2023-04-04 06:55:49.000000 titan-iris-0.3.9a2/src/iris/config.yaml
+-rw-r--r--   0 runner    (1001) docker     (123)    18057 2023-04-04 06:55:49.000000 titan-iris-0.3.9a2/src/iris/main.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-04 06:56:06.910348 titan-iris-0.3.9a2/src/iris/sdk/
+-rw-r--r--   0 runner    (1001) docker     (123)       24 2023-04-04 06:55:49.000000 titan-iris-0.3.9a2/src/iris/sdk/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    10740 2023-04-04 06:55:49.000000 titan-iris-0.3.9a2/src/iris/sdk/auth_utils.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4812 2023-04-04 06:55:49.000000 titan-iris-0.3.9a2/src/iris/sdk/conf_manager.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6123 2023-04-04 06:55:49.000000 titan-iris-0.3.9a2/src/iris/sdk/exception.py
+-rw-r--r--   0 runner    (1001) docker     (123)    23192 2023-04-04 06:55:49.000000 titan-iris-0.3.9a2/src/iris/sdk/iris_sdk.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4099 2023-04-04 06:55:49.000000 titan-iris-0.3.9a2/src/iris/sdk/safe_convert.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7377 2023-04-04 06:55:49.000000 titan-iris-0.3.9a2/src/iris/sdk/utils.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-04 06:56:06.914348 titan-iris-0.3.9a2/src/titan_iris.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)     2130 2023-04-04 06:56:06.000000 titan-iris-0.3.9a2/src/titan_iris.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)      601 2023-04-04 06:56:06.000000 titan-iris-0.3.9a2/src/titan_iris.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-04 06:56:06.000000 titan-iris-0.3.9a2/src/titan_iris.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       40 2023-04-04 06:56:06.000000 titan-iris-0.3.9a2/src/titan_iris.egg-info/entry_points.txt
+-rw-r--r--   0 runner    (1001) docker     (123)      195 2023-04-04 06:56:06.000000 titan-iris-0.3.9a2/src/titan_iris.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        5 2023-04-04 06:56:06.000000 titan-iris-0.3.9a2/src/titan_iris.egg-info/top_level.txt
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-04 06:56:06.914348 titan-iris-0.3.9a2/tests/
+-rw-r--r--   0 runner    (1001) docker     (123)     3040 2023-04-04 06:55:49.000000 titan-iris-0.3.9a2/tests/test_cli.py
```

### Comparing `titan-iris-0.3.9a1/.gitignore` & `titan-iris-0.3.9a2/.gitignore`

 * *Files identical despite different names*

### Comparing `titan-iris-0.3.9a1/Dockerfile` & `titan-iris-0.3.9a2/Dockerfile`

 * *Files identical despite different names*

### Comparing `titan-iris-0.3.9a1/PKG-INFO` & `titan-iris-0.3.9a2/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: titan-iris
-Version: 0.3.9a1
+Version: 0.3.9a2
 Description-Content-Type: text/markdown
 
 # IRIS CLI Package
 
 Simple overview of use/purpose.
 
 ## Description
```

### Comparing `titan-iris-0.3.9a1/README.md` & `titan-iris-0.3.9a2/README.md`

 * *Files identical despite different names*

### Comparing `titan-iris-0.3.9a1/setup.py` & `titan-iris-0.3.9a2/setup.py`

 * *Files identical despite different names*

### Comparing `titan-iris-0.3.9a1/src/iris/config.yaml` & `titan-iris-0.3.9a2/src/iris/config.yaml`

 * *Files identical despite different names*

### Comparing `titan-iris-0.3.9a1/src/iris/main.py` & `titan-iris-0.3.9a2/src/iris/main.py`

 * *Files identical despite different names*

### Comparing `titan-iris-0.3.9a1/src/iris/sdk/auth_utils.py` & `titan-iris-0.3.9a2/src/iris/sdk/auth_utils.py`

 * *Files identical despite different names*

### Comparing `titan-iris-0.3.9a1/src/iris/sdk/conf_manager.py` & `titan-iris-0.3.9a2/src/iris/sdk/conf_manager.py`

 * *Files identical despite different names*

### Comparing `titan-iris-0.3.9a1/src/iris/sdk/exception.py` & `titan-iris-0.3.9a2/src/iris/sdk/exception.py`

 * *Files identical despite different names*

### Comparing `titan-iris-0.3.9a1/src/iris/sdk/iris_sdk.py` & `titan-iris-0.3.9a2/src/iris/sdk/iris_sdk.py`

 * *Files identical despite different names*

### Comparing `titan-iris-0.3.9a1/src/iris/sdk/safe_convert.py` & `titan-iris-0.3.9a2/src/iris/sdk/safe_convert.py`

 * *Files identical despite different names*

### Comparing `titan-iris-0.3.9a1/src/iris/sdk/utils.py` & `titan-iris-0.3.9a2/src/iris/sdk/utils.py`

 * *Files identical despite different names*

### Comparing `titan-iris-0.3.9a1/src/titan_iris.egg-info/PKG-INFO` & `titan-iris-0.3.9a2/src/titan_iris.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: titan-iris
-Version: 0.3.9a1
+Version: 0.3.9a2
 Description-Content-Type: text/markdown
 
 # IRIS CLI Package
 
 Simple overview of use/purpose.
 
 ## Description
```

### Comparing `titan-iris-0.3.9a1/src/titan_iris.egg-info/SOURCES.txt` & `titan-iris-0.3.9a2/src/titan_iris.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `titan-iris-0.3.9a1/tests/test_cli.py` & `titan-iris-0.3.9a2/tests/test_cli.py`

 * *Files identical despite different names*

