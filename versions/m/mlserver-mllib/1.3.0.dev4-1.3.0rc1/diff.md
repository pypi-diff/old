# Comparing `tmp/mlserver-mllib-1.3.0.dev4.tar.gz` & `tmp/mlserver-mllib-1.3.0rc1.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "mlserver-mllib-1.3.0.dev4.tar", last modified: Wed Mar 22 09:49:17 2023, max compression
+gzip compressed data, was "mlserver-mllib-1.3.0rc1.tar", last modified: Thu Apr  6 13:37:42 2023, max compression
```

## Comparing `mlserver-mllib-1.3.0.dev4.tar` & `mlserver-mllib-1.3.0rc1.tar`

### file list

```diff
@@ -1,18 +1,18 @@
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-22 09:49:17.369693 mlserver-mllib-1.3.0.dev4/
--rw-r--r--   0 runner    (1001) docker     (123)    11354 2023-03-22 09:48:44.000000 mlserver-mllib-1.3.0.dev4/LICENSE
--rw-r--r--   0 runner    (1001) docker     (123)      794 2023-03-22 09:49:17.369693 mlserver-mllib-1.3.0.dev4/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)      370 2023-03-22 09:48:44.000000 mlserver-mllib-1.3.0.dev4/README.md
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-22 09:49:17.369693 mlserver-mllib-1.3.0.dev4/mlserver_mllib/
--rw-r--r--   0 runner    (1001) docker     (123)       56 2023-03-22 09:48:44.000000 mlserver-mllib-1.3.0.dev4/mlserver_mllib/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      326 2023-03-22 09:48:44.000000 mlserver-mllib-1.3.0.dev4/mlserver_mllib/errors.py
--rw-r--r--   0 runner    (1001) docker     (123)     1596 2023-03-22 09:48:44.000000 mlserver-mllib-1.3.0.dev4/mlserver_mllib/mllib.py
--rw-r--r--   0 runner    (1001) docker     (123)     1370 2023-03-22 09:48:44.000000 mlserver-mllib-1.3.0.dev4/mlserver_mllib/utils.py
--rw-r--r--   0 runner    (1001) docker     (123)       27 2023-03-22 09:48:44.000000 mlserver-mllib-1.3.0.dev4/mlserver_mllib/version.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-22 09:49:17.369693 mlserver-mllib-1.3.0.dev4/mlserver_mllib.egg-info/
--rw-r--r--   0 runner    (1001) docker     (123)      794 2023-03-22 09:49:17.000000 mlserver-mllib-1.3.0.dev4/mlserver_mllib.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)      341 2023-03-22 09:49:17.000000 mlserver-mllib-1.3.0.dev4/mlserver_mllib.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-03-22 09:49:17.000000 mlserver-mllib-1.3.0.dev4/mlserver_mllib.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (123)       17 2023-03-22 09:49:17.000000 mlserver-mllib-1.3.0.dev4/mlserver_mllib.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (123)       15 2023-03-22 09:49:17.000000 mlserver-mllib-1.3.0.dev4/mlserver_mllib.egg-info/top_level.txt
--rw-r--r--   0 runner    (1001) docker     (123)       38 2023-03-22 09:49:17.369693 mlserver-mllib-1.3.0.dev4/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (123)     1131 2023-03-22 09:48:44.000000 mlserver-mllib-1.3.0.dev4/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 13:37:42.054215 mlserver-mllib-1.3.0rc1/
+-rw-r--r--   0 runner    (1001) docker     (123)    11354 2023-04-06 13:37:07.000000 mlserver-mllib-1.3.0rc1/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (123)      792 2023-04-06 13:37:42.054215 mlserver-mllib-1.3.0rc1/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)      370 2023-04-06 13:37:07.000000 mlserver-mllib-1.3.0rc1/README.md
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 13:37:42.050214 mlserver-mllib-1.3.0rc1/mlserver_mllib/
+-rw-r--r--   0 runner    (1001) docker     (123)       56 2023-04-06 13:37:07.000000 mlserver-mllib-1.3.0rc1/mlserver_mllib/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      326 2023-04-06 13:37:07.000000 mlserver-mllib-1.3.0rc1/mlserver_mllib/errors.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1564 2023-04-06 13:37:07.000000 mlserver-mllib-1.3.0rc1/mlserver_mllib/mllib.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1370 2023-04-06 13:37:07.000000 mlserver-mllib-1.3.0rc1/mlserver_mllib/utils.py
+-rw-r--r--   0 runner    (1001) docker     (123)       26 2023-04-06 13:37:07.000000 mlserver-mllib-1.3.0rc1/mlserver_mllib/version.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 13:37:42.054215 mlserver-mllib-1.3.0rc1/mlserver_mllib.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)      792 2023-04-06 13:37:41.000000 mlserver-mllib-1.3.0rc1/mlserver_mllib.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)      341 2023-04-06 13:37:42.000000 mlserver-mllib-1.3.0rc1/mlserver_mllib.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-06 13:37:41.000000 mlserver-mllib-1.3.0rc1/mlserver_mllib.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       17 2023-04-06 13:37:41.000000 mlserver-mllib-1.3.0rc1/mlserver_mllib.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       15 2023-04-06 13:37:41.000000 mlserver-mllib-1.3.0rc1/mlserver_mllib.egg-info/top_level.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       38 2023-04-06 13:37:42.054215 mlserver-mllib-1.3.0rc1/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (123)     1131 2023-04-06 13:37:07.000000 mlserver-mllib-1.3.0rc1/setup.py
```

### Comparing `mlserver-mllib-1.3.0.dev4/LICENSE` & `mlserver-mllib-1.3.0rc1/LICENSE`

 * *Files identical despite different names*

### Comparing `mlserver-mllib-1.3.0.dev4/mlserver_mllib/mllib.py` & `mlserver-mllib-1.3.0rc1/mlserver_mllib/mllib.py`

 * *Files 6% similar despite different names*

```diff
@@ -14,16 +14,15 @@
         sc = SparkContext(appName="MLlibModel", conf=conf)
 
         model_uri = await get_model_uri(self._settings)
         model_load = await get_mllib_load(self._settings)
 
         self._model = model_load(sc, model_uri)
 
-        self.ready = True
-        return self.ready
+        return True
 
     async def predict(self, payload: types.InferenceRequest) -> types.InferenceResponse:
         payload = self._check_request(payload)
         prediction = self._model.predict(payload.inputs[0].data)
 
         return types.InferenceResponse(
             model_name=self.name,
```

### Comparing `mlserver-mllib-1.3.0.dev4/mlserver_mllib/utils.py` & `mlserver-mllib-1.3.0rc1/mlserver_mllib/utils.py`

 * *Files identical despite different names*

### Comparing `mlserver-mllib-1.3.0.dev4/setup.py` & `mlserver-mllib-1.3.0rc1/setup.py`

 * *Files identical despite different names*

