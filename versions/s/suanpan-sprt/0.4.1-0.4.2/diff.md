# Comparing `tmp/suanpan-sprt-0.4.1.tar.gz` & `tmp/suanpan-sprt-0.4.2.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "dist/suanpan-sprt-0.4.1.tar", last modified: Thu Apr  6 01:54:57 2023, max compression
+gzip compressed data, was "dist/suanpan-sprt-0.4.2.tar", last modified: Fri Apr  7 07:10:38 2023, max compression
```

## Comparing `suanpan-sprt-0.4.1.tar` & `suanpan-sprt-0.4.2.tar`

### file list

```diff
@@ -1,26 +1,26 @@
-drwxrwxr-x   0 gitlab-runner  (1003) gitlab-runner  (1003)        0 2023-04-06 01:54:57.000000 suanpan-sprt-0.4.1/
--rw-rw-r--   0 gitlab-runner  (1003) gitlab-runner  (1003)      437 2023-04-06 01:54:57.000000 suanpan-sprt-0.4.1/PKG-INFO
--rw-rw-r--   0 gitlab-runner  (1003) gitlab-runner  (1003)       84 2023-03-13 09:36:01.000000 suanpan-sprt-0.4.1/README.md
--rw-rw-r--   0 gitlab-runner  (1003) gitlab-runner  (1003)       38 2023-04-06 01:54:57.000000 suanpan-sprt-0.4.1/setup.cfg
--rw-rw-r--   0 gitlab-runner  (1003) gitlab-runner  (1003)     1038 2023-03-13 09:36:01.000000 suanpan-sprt-0.4.1/setup.py
-drwxrwxr-x   0 gitlab-runner  (1003) gitlab-runner  (1003)        0 2023-04-06 01:54:57.000000 suanpan-sprt-0.4.1/sprt/
--rw-rw-r--   0 gitlab-runner  (1003) gitlab-runner  (1003)      100 2023-03-13 09:36:01.000000 suanpan-sprt-0.4.1/sprt/__init__.py
--rw-rw-r--   0 gitlab-runner  (1003) gitlab-runner  (1003)     3136 2023-03-23 04:28:38.000000 suanpan-sprt-0.4.1/sprt/__main__.py
--rw-rw-r--   0 gitlab-runner  (1003) gitlab-runner  (1003)     8450 2023-04-06 01:54:57.000000 suanpan-sprt-0.4.1/sprt/arguments.py
--rw-rw-r--   0 gitlab-runner  (1003) gitlab-runner  (1003)     1280 2023-04-04 09:18:04.000000 suanpan-sprt-0.4.1/sprt/envs.py
--rw-rw-r--   0 gitlab-runner  (1003) gitlab-runner  (1003)      190 2023-03-13 09:36:01.000000 suanpan-sprt-0.4.1/sprt/exceptions.py
--rw-rw-r--   0 gitlab-runner  (1003) gitlab-runner  (1003)     3603 2023-04-04 09:18:04.000000 suanpan-sprt-0.4.1/sprt/loader.py
--rw-rw-r--   0 gitlab-runner  (1003) gitlab-runner  (1003)     2069 2023-04-04 09:18:04.000000 suanpan-sprt-0.4.1/sprt/log.py
--rw-rw-r--   0 gitlab-runner  (1003) gitlab-runner  (1003)      880 2023-04-04 09:18:04.000000 suanpan-sprt-0.4.1/sprt/master.py
--rw-rw-r--   0 gitlab-runner  (1003) gitlab-runner  (1003)     3365 2023-04-04 09:18:04.000000 suanpan-sprt-0.4.1/sprt/server.py
--rw-rw-r--   0 gitlab-runner  (1003) gitlab-runner  (1003)     6456 2023-04-04 09:18:04.000000 suanpan-sprt-0.4.1/sprt/storage.py
--rw-rw-r--   0 gitlab-runner  (1003) gitlab-runner  (1003)     3448 2023-04-04 09:18:04.000000 suanpan-sprt-0.4.1/sprt/testing.py
--rw-rw-r--   0 gitlab-runner  (1003) gitlab-runner  (1003)      605 2023-04-04 09:18:04.000000 suanpan-sprt-0.4.1/sprt/utils.py
--rw-rw-r--   0 gitlab-runner  (1003) gitlab-runner  (1003)       22 2023-04-06 01:54:57.000000 suanpan-sprt-0.4.1/sprt/version.py
-drwxrwxr-x   0 gitlab-runner  (1003) gitlab-runner  (1003)        0 2023-04-06 01:54:57.000000 suanpan-sprt-0.4.1/suanpan_sprt.egg-info/
--rw-rw-r--   0 gitlab-runner  (1003) gitlab-runner  (1003)      437 2023-04-06 01:54:57.000000 suanpan-sprt-0.4.1/suanpan_sprt.egg-info/PKG-INFO
--rw-rw-r--   0 gitlab-runner  (1003) gitlab-runner  (1003)      439 2023-04-06 01:54:57.000000 suanpan-sprt-0.4.1/suanpan_sprt.egg-info/SOURCES.txt
--rw-rw-r--   0 gitlab-runner  (1003) gitlab-runner  (1003)        1 2023-04-06 01:54:57.000000 suanpan-sprt-0.4.1/suanpan_sprt.egg-info/dependency_links.txt
--rw-rw-r--   0 gitlab-runner  (1003) gitlab-runner  (1003)       44 2023-04-06 01:54:57.000000 suanpan-sprt-0.4.1/suanpan_sprt.egg-info/entry_points.txt
--rw-rw-r--   0 gitlab-runner  (1003) gitlab-runner  (1003)      158 2023-04-06 01:54:57.000000 suanpan-sprt-0.4.1/suanpan_sprt.egg-info/requires.txt
--rw-rw-r--   0 gitlab-runner  (1003) gitlab-runner  (1003)        5 2023-04-06 01:54:57.000000 suanpan-sprt-0.4.1/suanpan_sprt.egg-info/top_level.txt
+drwxrwxr-x   0 gitlab-runner  (1003) gitlab-runner  (1003)        0 2023-04-07 07:10:38.000000 suanpan-sprt-0.4.2/
+-rw-rw-r--   0 gitlab-runner  (1003) gitlab-runner  (1003)      437 2023-04-07 07:10:38.000000 suanpan-sprt-0.4.2/PKG-INFO
+-rw-rw-r--   0 gitlab-runner  (1003) gitlab-runner  (1003)       84 2023-03-13 09:36:01.000000 suanpan-sprt-0.4.2/README.md
+-rw-rw-r--   0 gitlab-runner  (1003) gitlab-runner  (1003)       38 2023-04-07 07:10:38.000000 suanpan-sprt-0.4.2/setup.cfg
+-rw-rw-r--   0 gitlab-runner  (1003) gitlab-runner  (1003)     1038 2023-03-13 09:36:01.000000 suanpan-sprt-0.4.2/setup.py
+drwxrwxr-x   0 gitlab-runner  (1003) gitlab-runner  (1003)        0 2023-04-07 07:10:38.000000 suanpan-sprt-0.4.2/sprt/
+-rw-rw-r--   0 gitlab-runner  (1003) gitlab-runner  (1003)      100 2023-03-13 09:36:01.000000 suanpan-sprt-0.4.2/sprt/__init__.py
+-rw-rw-r--   0 gitlab-runner  (1003) gitlab-runner  (1003)     3136 2023-03-23 04:28:38.000000 suanpan-sprt-0.4.2/sprt/__main__.py
+-rw-rw-r--   0 gitlab-runner  (1003) gitlab-runner  (1003)     8450 2023-04-06 01:54:57.000000 suanpan-sprt-0.4.2/sprt/arguments.py
+-rw-rw-r--   0 gitlab-runner  (1003) gitlab-runner  (1003)     1280 2023-04-04 09:18:04.000000 suanpan-sprt-0.4.2/sprt/envs.py
+-rw-rw-r--   0 gitlab-runner  (1003) gitlab-runner  (1003)      190 2023-03-13 09:36:01.000000 suanpan-sprt-0.4.2/sprt/exceptions.py
+-rw-rw-r--   0 gitlab-runner  (1003) gitlab-runner  (1003)     3700 2023-04-07 07:10:37.000000 suanpan-sprt-0.4.2/sprt/loader.py
+-rw-rw-r--   0 gitlab-runner  (1003) gitlab-runner  (1003)     2069 2023-04-04 09:18:04.000000 suanpan-sprt-0.4.2/sprt/log.py
+-rw-rw-r--   0 gitlab-runner  (1003) gitlab-runner  (1003)      880 2023-04-04 09:18:04.000000 suanpan-sprt-0.4.2/sprt/master.py
+-rw-rw-r--   0 gitlab-runner  (1003) gitlab-runner  (1003)     3365 2023-04-04 09:18:04.000000 suanpan-sprt-0.4.2/sprt/server.py
+-rw-rw-r--   0 gitlab-runner  (1003) gitlab-runner  (1003)     6456 2023-04-04 09:18:04.000000 suanpan-sprt-0.4.2/sprt/storage.py
+-rw-rw-r--   0 gitlab-runner  (1003) gitlab-runner  (1003)     3448 2023-04-04 09:18:04.000000 suanpan-sprt-0.4.2/sprt/testing.py
+-rw-rw-r--   0 gitlab-runner  (1003) gitlab-runner  (1003)      605 2023-04-04 09:18:04.000000 suanpan-sprt-0.4.2/sprt/utils.py
+-rw-rw-r--   0 gitlab-runner  (1003) gitlab-runner  (1003)       22 2023-04-07 07:10:37.000000 suanpan-sprt-0.4.2/sprt/version.py
+drwxrwxr-x   0 gitlab-runner  (1003) gitlab-runner  (1003)        0 2023-04-07 07:10:38.000000 suanpan-sprt-0.4.2/suanpan_sprt.egg-info/
+-rw-rw-r--   0 gitlab-runner  (1003) gitlab-runner  (1003)      437 2023-04-07 07:10:37.000000 suanpan-sprt-0.4.2/suanpan_sprt.egg-info/PKG-INFO
+-rw-rw-r--   0 gitlab-runner  (1003) gitlab-runner  (1003)      439 2023-04-07 07:10:38.000000 suanpan-sprt-0.4.2/suanpan_sprt.egg-info/SOURCES.txt
+-rw-rw-r--   0 gitlab-runner  (1003) gitlab-runner  (1003)        1 2023-04-07 07:10:37.000000 suanpan-sprt-0.4.2/suanpan_sprt.egg-info/dependency_links.txt
+-rw-rw-r--   0 gitlab-runner  (1003) gitlab-runner  (1003)       44 2023-04-07 07:10:37.000000 suanpan-sprt-0.4.2/suanpan_sprt.egg-info/entry_points.txt
+-rw-rw-r--   0 gitlab-runner  (1003) gitlab-runner  (1003)      158 2023-04-07 07:10:37.000000 suanpan-sprt-0.4.2/suanpan_sprt.egg-info/requires.txt
+-rw-rw-r--   0 gitlab-runner  (1003) gitlab-runner  (1003)        5 2023-04-07 07:10:37.000000 suanpan-sprt-0.4.2/suanpan_sprt.egg-info/top_level.txt
```

### Comparing `suanpan-sprt-0.4.1/setup.py` & `suanpan-sprt-0.4.2/setup.py`

 * *Files identical despite different names*

### Comparing `suanpan-sprt-0.4.1/sprt/__main__.py` & `suanpan-sprt-0.4.2/sprt/__main__.py`

 * *Files identical despite different names*

### Comparing `suanpan-sprt-0.4.1/sprt/arguments.py` & `suanpan-sprt-0.4.2/sprt/arguments.py`

 * *Files identical despite different names*

### Comparing `suanpan-sprt-0.4.1/sprt/envs.py` & `suanpan-sprt-0.4.2/sprt/envs.py`

 * *Files identical despite different names*

### Comparing `suanpan-sprt-0.4.1/sprt/loader.py` & `suanpan-sprt-0.4.2/sprt/loader.py`

 * *Files 5% similar despite different names*

```diff
@@ -20,14 +20,16 @@
         self.context = RuntimeContext(envs.userId, envs.appId, node_id)
 
     def load_module(self):
         if not self.location.is_file():
             raise Exception(f'invalid component file: {self.location}')
 
         spec = importlib.util.spec_from_file_location(self.name, self.location)
+        if spec is None:
+            raise Exception(f'invalid component spec: {self.location}')
         module = importlib.util.module_from_spec(spec)
         spec.loader.exec_module(module)
         return module
 
     async def call_func(self, request_id, args, params):
         in_slot = []
         has_context = False
```

### Comparing `suanpan-sprt-0.4.1/sprt/log.py` & `suanpan-sprt-0.4.2/sprt/log.py`

 * *Files identical despite different names*

### Comparing `suanpan-sprt-0.4.1/sprt/master.py` & `suanpan-sprt-0.4.2/sprt/master.py`

 * *Files identical despite different names*

### Comparing `suanpan-sprt-0.4.1/sprt/server.py` & `suanpan-sprt-0.4.2/sprt/server.py`

 * *Files identical despite different names*

### Comparing `suanpan-sprt-0.4.1/sprt/storage.py` & `suanpan-sprt-0.4.2/sprt/storage.py`

 * *Files identical despite different names*

### Comparing `suanpan-sprt-0.4.1/sprt/testing.py` & `suanpan-sprt-0.4.2/sprt/testing.py`

 * *Files identical despite different names*

### Comparing `suanpan-sprt-0.4.1/sprt/utils.py` & `suanpan-sprt-0.4.2/sprt/utils.py`

 * *Files identical despite different names*

