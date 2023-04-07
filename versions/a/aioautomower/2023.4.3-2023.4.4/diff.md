# Comparing `tmp/aioautomower-2023.4.3.tar.gz` & `tmp/aioautomower-2023.4.4.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "aioautomower-2023.4.3.tar", last modified: Thu Apr  6 15:36:53 2023, max compression
+gzip compressed data, was "aioautomower-2023.4.4.tar", last modified: Fri Apr  7 12:08:44 2023, max compression
```

## Comparing `aioautomower-2023.4.3.tar` & `aioautomower-2023.4.4.tar`

### file list

```diff
@@ -1,19 +1,19 @@
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 15:36:53.851419 aioautomower-2023.4.3/
--rw-r--r--   0 runner    (1001) docker     (123)      555 2023-04-06 15:36:43.000000 aioautomower-2023.4.3/LICENSE
--rw-r--r--   0 runner    (1001) docker     (123)     5287 2023-04-06 15:36:53.851419 aioautomower-2023.4.3/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)     4802 2023-04-06 15:36:43.000000 aioautomower-2023.4.3/README.md
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 15:36:53.851419 aioautomower-2023.4.3/aioautomower/
--rw-r--r--   0 runner    (1001) docker     (123)       97 2023-04-06 15:36:43.000000 aioautomower-2023.4.3/aioautomower/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     2173 2023-04-06 15:36:43.000000 aioautomower-2023.4.3/aioautomower/cli.py
--rw-r--r--   0 runner    (1001) docker     (123)      969 2023-04-06 15:36:43.000000 aioautomower-2023.4.3/aioautomower/const.py
--rw-r--r--   0 runner    (1001) docker     (123)     8413 2023-04-06 15:36:43.000000 aioautomower-2023.4.3/aioautomower/rest.py
--rw-r--r--   0 runner    (1001) docker     (123)    16067 2023-04-06 15:36:43.000000 aioautomower-2023.4.3/aioautomower/session.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 15:36:53.851419 aioautomower-2023.4.3/aioautomower.egg-info/
--rw-r--r--   0 runner    (1001) docker     (123)     5287 2023-04-06 15:36:53.000000 aioautomower-2023.4.3/aioautomower.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)      356 2023-04-06 15:36:53.000000 aioautomower-2023.4.3/aioautomower.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-06 15:36:53.000000 aioautomower-2023.4.3/aioautomower.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (123)       52 2023-04-06 15:36:53.000000 aioautomower-2023.4.3/aioautomower.egg-info/entry_points.txt
--rw-r--r--   0 runner    (1001) docker     (123)        8 2023-04-06 15:36:53.000000 aioautomower-2023.4.3/aioautomower.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (123)       13 2023-04-06 15:36:53.000000 aioautomower-2023.4.3/aioautomower.egg-info/top_level.txt
--rw-r--r--   0 runner    (1001) docker     (123)       38 2023-04-06 15:36:53.851419 aioautomower-2023.4.3/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (123)      867 2023-04-06 15:36:43.000000 aioautomower-2023.4.3/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 12:08:44.226260 aioautomower-2023.4.4/
+-rw-r--r--   0 runner    (1001) docker     (123)      555 2023-04-07 12:08:31.000000 aioautomower-2023.4.4/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (123)     5287 2023-04-07 12:08:44.222260 aioautomower-2023.4.4/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     4802 2023-04-07 12:08:31.000000 aioautomower-2023.4.4/README.md
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 12:08:44.222260 aioautomower-2023.4.4/aioautomower/
+-rw-r--r--   0 runner    (1001) docker     (123)       97 2023-04-07 12:08:31.000000 aioautomower-2023.4.4/aioautomower/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2173 2023-04-07 12:08:31.000000 aioautomower-2023.4.4/aioautomower/cli.py
+-rw-r--r--   0 runner    (1001) docker     (123)      969 2023-04-07 12:08:31.000000 aioautomower-2023.4.4/aioautomower/const.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8413 2023-04-07 12:08:31.000000 aioautomower-2023.4.4/aioautomower/rest.py
+-rw-r--r--   0 runner    (1001) docker     (123)    16029 2023-04-07 12:08:31.000000 aioautomower-2023.4.4/aioautomower/session.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 12:08:44.222260 aioautomower-2023.4.4/aioautomower.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)     5287 2023-04-07 12:08:44.000000 aioautomower-2023.4.4/aioautomower.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)      356 2023-04-07 12:08:44.000000 aioautomower-2023.4.4/aioautomower.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-07 12:08:44.000000 aioautomower-2023.4.4/aioautomower.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       52 2023-04-07 12:08:44.000000 aioautomower-2023.4.4/aioautomower.egg-info/entry_points.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        8 2023-04-07 12:08:44.000000 aioautomower-2023.4.4/aioautomower.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       13 2023-04-07 12:08:44.000000 aioautomower-2023.4.4/aioautomower.egg-info/top_level.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       38 2023-04-07 12:08:44.226260 aioautomower-2023.4.4/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (123)      867 2023-04-07 12:08:31.000000 aioautomower-2023.4.4/setup.py
```

### Comparing `aioautomower-2023.4.3/LICENSE` & `aioautomower-2023.4.4/LICENSE`

 * *Files identical despite different names*

### Comparing `aioautomower-2023.4.3/PKG-INFO` & `aioautomower-2023.4.4/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: aioautomower
-Version: 2023.4.3
+Version: 2023.4.4
 Summary: module to communicate to Husqvarna Automower API
 Home-page: https://github.com/Thomas55555/aioautomower
 Author: Thomas Protzner
 Author-email: thomas.protzner@gmail.com
 License: Apache License 2.0
 Classifier: Programming Language :: Python :: 3
 Classifier: License :: OSI Approved :: Apache Software License
```

### Comparing `aioautomower-2023.4.3/README.md` & `aioautomower-2023.4.4/README.md`

 * *Files identical despite different names*

### Comparing `aioautomower-2023.4.3/aioautomower/cli.py` & `aioautomower-2023.4.4/aioautomower/cli.py`

 * *Files identical despite different names*

### Comparing `aioautomower-2023.4.3/aioautomower/const.py` & `aioautomower-2023.4.4/aioautomower/const.py`

 * *Files identical despite different names*

### Comparing `aioautomower-2023.4.3/aioautomower/rest.py` & `aioautomower-2023.4.4/aioautomower/rest.py`

 * *Files identical despite different names*

### Comparing `aioautomower-2023.4.3/aioautomower/session.py` & `aioautomower-2023.4.4/aioautomower/session.py`

 * *Files 1% similar despite different names*

```diff
@@ -134,15 +134,14 @@
         else:
             self.ws_task = self.loop.create_task(self._ws_task())
         self.rest_task = self.loop.create_task(self._rest_task())
         self.token_task = self.loop.create_task(self._token_monitor_task())
 
     async def close(self):
         """Close the session."""
-        await self.invalidate_token()
         for task in [
             self.ws_task,
             self.token_task,
             self.websocket_monitor_task,
             self.rest_task,
         ]:
             tasks = []
```

### Comparing `aioautomower-2023.4.3/aioautomower.egg-info/PKG-INFO` & `aioautomower-2023.4.4/aioautomower.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: aioautomower
-Version: 2023.4.3
+Version: 2023.4.4
 Summary: module to communicate to Husqvarna Automower API
 Home-page: https://github.com/Thomas55555/aioautomower
 Author: Thomas Protzner
 Author-email: thomas.protzner@gmail.com
 License: Apache License 2.0
 Classifier: Programming Language :: Python :: 3
 Classifier: License :: OSI Approved :: Apache Software License
```

### Comparing `aioautomower-2023.4.3/setup.py` & `aioautomower-2023.4.4/setup.py`

 * *Files 1% similar despite different names*

```diff
@@ -15,12 +15,12 @@
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: Apache Software License",
         "Operating System :: OS Independent",
     ],
     install_requires=list(val.strip() for val in open("requirements.txt")),
-    version="2023.4.3",
+    version="2023.4.4",
     entry_points={
         "console_scripts": ["automower=aioautomower.cli:main"],
     },
 )
```

