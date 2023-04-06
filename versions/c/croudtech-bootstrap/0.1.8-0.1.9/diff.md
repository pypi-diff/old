# Comparing `tmp/croudtech-bootstrap-0.1.8.tar.gz` & `tmp/croudtech-bootstrap-0.1.9.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "croudtech-bootstrap-0.1.8.tar", last modified: Tue Jun 21 16:21:16 2022, max compression
+gzip compressed data, was "croudtech-bootstrap-0.1.9.tar", last modified: Tue Jun 21 16:27:04 2022, max compression
```

## Comparing `croudtech-bootstrap-0.1.8.tar` & `croudtech-bootstrap-0.1.9.tar`

### file list

```diff
@@ -1,28 +1,28 @@
-drwxr-xr-x   0 vsts      (1001) docker     (121)        0 2022-06-21 16:21:16.654228 croudtech-bootstrap-0.1.8/
--rw-r--r--   0 vsts      (1001) docker     (121)       24 2022-06-21 16:20:44.000000 croudtech-bootstrap-0.1.8/MANIFEST.in
--rw-r--r--   0 vsts      (1001) docker     (121)      477 2022-06-21 16:21:16.654228 croudtech-bootstrap-0.1.8/PKG-INFO
--rw-r--r--   0 vsts      (1001) docker     (121)        0 2022-06-21 16:20:44.000000 croudtech-bootstrap-0.1.8/README.md
-drwxr-xr-x   0 vsts      (1001) docker     (121)        0 2022-06-21 16:21:16.654228 croudtech-bootstrap-0.1.8/croudtech_bootstrap.egg-info/
--rw-r--r--   0 vsts      (1001) docker     (121)      477 2022-06-21 16:21:16.000000 croudtech-bootstrap-0.1.8/croudtech_bootstrap.egg-info/PKG-INFO
--rw-r--r--   0 vsts      (1001) docker     (121)      795 2022-06-21 16:21:16.000000 croudtech-bootstrap-0.1.8/croudtech_bootstrap.egg-info/SOURCES.txt
--rw-r--r--   0 vsts      (1001) docker     (121)        1 2022-06-21 16:21:16.000000 croudtech-bootstrap-0.1.8/croudtech_bootstrap.egg-info/dependency_links.txt
--rw-r--r--   0 vsts      (1001) docker     (121)       72 2022-06-21 16:21:16.000000 croudtech-bootstrap-0.1.8/croudtech_bootstrap.egg-info/entry_points.txt
--rw-r--r--   0 vsts      (1001) docker     (121)        1 2022-06-21 16:21:14.000000 croudtech-bootstrap-0.1.8/croudtech_bootstrap.egg-info/not-zip-safe
--rw-r--r--   0 vsts      (1001) docker     (121)      735 2022-06-21 16:21:16.000000 croudtech-bootstrap-0.1.8/croudtech_bootstrap.egg-info/requires.txt
--rw-r--r--   0 vsts      (1001) docker     (121)       24 2022-06-21 16:21:16.000000 croudtech-bootstrap-0.1.8/croudtech_bootstrap.egg-info/top_level.txt
-drwxr-xr-x   0 vsts      (1001) docker     (121)        0 2022-06-21 16:21:16.654228 croudtech-bootstrap-0.1.8/croudtech_bootstrap_app/
--rw-r--r--   0 vsts      (1001) docker     (121)        0 2022-06-21 16:20:44.000000 croudtech-bootstrap-0.1.8/croudtech_bootstrap_app/__init__.py
--rw-r--r--   0 vsts      (1001) docker     (121)        0 2022-06-21 16:20:44.000000 croudtech-bootstrap-0.1.8/croudtech_bootstrap_app/__main__.py
--rw-r--r--   0 vsts      (1001) docker     (121)    18056 2022-06-21 16:20:44.000000 croudtech-bootstrap-0.1.8/croudtech_bootstrap_app/bootstrap.py
--rw-r--r--   0 vsts      (1001) docker     (121)     9676 2022-06-21 16:20:44.000000 croudtech-bootstrap-0.1.8/croudtech_bootstrap_app/cli.py
--rw-r--r--   0 vsts      (1001) docker     (121)      206 2022-06-21 16:20:44.000000 croudtech-bootstrap-0.1.8/croudtech_bootstrap_app/croudtech-bootstrap.py
--rw-r--r--   0 vsts      (1001) docker     (121)      654 2022-06-21 16:20:44.000000 croudtech-bootstrap-0.1.8/croudtech_bootstrap_app/logging.py
--rw-r--r--   0 vsts      (1001) docker     (121)      804 2022-06-21 16:20:44.000000 croudtech-bootstrap-0.1.8/croudtech_bootstrap_app/metrics.py
--rw-r--r--   0 vsts      (1001) docker     (121)     3382 2022-06-21 16:20:44.000000 croudtech-bootstrap-0.1.8/croudtech_bootstrap_app/redis_config.py
-drwxr-xr-x   0 vsts      (1001) docker     (121)        0 2022-06-21 16:21:16.654228 croudtech-bootstrap-0.1.8/croudtech_bootstrap_app/tests/
--rw-r--r--   0 vsts      (1001) docker     (121)        0 2022-06-21 16:20:44.000000 croudtech-bootstrap-0.1.8/croudtech_bootstrap_app/tests/__init__.py
--rw-r--r--   0 vsts      (1001) docker     (121)     1787 2022-06-21 16:20:44.000000 croudtech-bootstrap-0.1.8/croudtech_bootstrap_app/tests/bootstrap_test.py
--rw-r--r--   0 vsts      (1001) docker     (121)      106 2022-06-21 16:20:44.000000 croudtech-bootstrap-0.1.8/pyproject.toml
--rw-r--r--   0 vsts      (1001) docker     (121)      986 2022-06-21 16:20:44.000000 croudtech-bootstrap-0.1.8/requirements.txt
--rw-r--r--   0 vsts      (1001) docker     (121)     1255 2022-06-21 16:21:16.654228 croudtech-bootstrap-0.1.8/setup.cfg
--rw-r--r--   0 vsts      (1001) docker     (121)      283 2022-06-21 16:20:44.000000 croudtech-bootstrap-0.1.8/setup.py
+drwxr-xr-x   0 vsts      (1001) docker     (121)        0 2022-06-21 16:27:04.870117 croudtech-bootstrap-0.1.9/
+-rw-r--r--   0 vsts      (1001) docker     (121)       24 2022-06-21 16:26:31.000000 croudtech-bootstrap-0.1.9/MANIFEST.in
+-rw-r--r--   0 vsts      (1001) docker     (121)      477 2022-06-21 16:27:04.870117 croudtech-bootstrap-0.1.9/PKG-INFO
+-rw-r--r--   0 vsts      (1001) docker     (121)        0 2022-06-21 16:26:31.000000 croudtech-bootstrap-0.1.9/README.md
+drwxr-xr-x   0 vsts      (1001) docker     (121)        0 2022-06-21 16:27:04.870117 croudtech-bootstrap-0.1.9/croudtech_bootstrap.egg-info/
+-rw-r--r--   0 vsts      (1001) docker     (121)      477 2022-06-21 16:27:04.000000 croudtech-bootstrap-0.1.9/croudtech_bootstrap.egg-info/PKG-INFO
+-rw-r--r--   0 vsts      (1001) docker     (121)      795 2022-06-21 16:27:04.000000 croudtech-bootstrap-0.1.9/croudtech_bootstrap.egg-info/SOURCES.txt
+-rw-r--r--   0 vsts      (1001) docker     (121)        1 2022-06-21 16:27:04.000000 croudtech-bootstrap-0.1.9/croudtech_bootstrap.egg-info/dependency_links.txt
+-rw-r--r--   0 vsts      (1001) docker     (121)       72 2022-06-21 16:27:04.000000 croudtech-bootstrap-0.1.9/croudtech_bootstrap.egg-info/entry_points.txt
+-rw-r--r--   0 vsts      (1001) docker     (121)        1 2022-06-21 16:27:02.000000 croudtech-bootstrap-0.1.9/croudtech_bootstrap.egg-info/not-zip-safe
+-rw-r--r--   0 vsts      (1001) docker     (121)      735 2022-06-21 16:27:04.000000 croudtech-bootstrap-0.1.9/croudtech_bootstrap.egg-info/requires.txt
+-rw-r--r--   0 vsts      (1001) docker     (121)       24 2022-06-21 16:27:04.000000 croudtech-bootstrap-0.1.9/croudtech_bootstrap.egg-info/top_level.txt
+drwxr-xr-x   0 vsts      (1001) docker     (121)        0 2022-06-21 16:27:04.870117 croudtech-bootstrap-0.1.9/croudtech_bootstrap_app/
+-rw-r--r--   0 vsts      (1001) docker     (121)        0 2022-06-21 16:26:31.000000 croudtech-bootstrap-0.1.9/croudtech_bootstrap_app/__init__.py
+-rw-r--r--   0 vsts      (1001) docker     (121)        0 2022-06-21 16:26:31.000000 croudtech-bootstrap-0.1.9/croudtech_bootstrap_app/__main__.py
+-rw-r--r--   0 vsts      (1001) docker     (121)    18056 2022-06-21 16:26:31.000000 croudtech-bootstrap-0.1.9/croudtech_bootstrap_app/bootstrap.py
+-rw-r--r--   0 vsts      (1001) docker     (121)     9676 2022-06-21 16:26:31.000000 croudtech-bootstrap-0.1.9/croudtech_bootstrap_app/cli.py
+-rw-r--r--   0 vsts      (1001) docker     (121)      206 2022-06-21 16:26:31.000000 croudtech-bootstrap-0.1.9/croudtech_bootstrap_app/croudtech-bootstrap.py
+-rw-r--r--   0 vsts      (1001) docker     (121)      654 2022-06-21 16:26:31.000000 croudtech-bootstrap-0.1.9/croudtech_bootstrap_app/logging.py
+-rw-r--r--   0 vsts      (1001) docker     (121)      804 2022-06-21 16:26:31.000000 croudtech-bootstrap-0.1.9/croudtech_bootstrap_app/metrics.py
+-rw-r--r--   0 vsts      (1001) docker     (121)     3382 2022-06-21 16:26:31.000000 croudtech-bootstrap-0.1.9/croudtech_bootstrap_app/redis_config.py
+drwxr-xr-x   0 vsts      (1001) docker     (121)        0 2022-06-21 16:27:04.870117 croudtech-bootstrap-0.1.9/croudtech_bootstrap_app/tests/
+-rw-r--r--   0 vsts      (1001) docker     (121)        0 2022-06-21 16:26:31.000000 croudtech-bootstrap-0.1.9/croudtech_bootstrap_app/tests/__init__.py
+-rw-r--r--   0 vsts      (1001) docker     (121)     1787 2022-06-21 16:26:31.000000 croudtech-bootstrap-0.1.9/croudtech_bootstrap_app/tests/bootstrap_test.py
+-rw-r--r--   0 vsts      (1001) docker     (121)      106 2022-06-21 16:26:31.000000 croudtech-bootstrap-0.1.9/pyproject.toml
+-rw-r--r--   0 vsts      (1001) docker     (121)      986 2022-06-21 16:26:31.000000 croudtech-bootstrap-0.1.9/requirements.txt
+-rw-r--r--   0 vsts      (1001) docker     (121)     1255 2022-06-21 16:27:04.870117 croudtech-bootstrap-0.1.9/setup.cfg
+-rw-r--r--   0 vsts      (1001) docker     (121)      283 2022-06-21 16:26:31.000000 croudtech-bootstrap-0.1.9/setup.py
```

### Comparing `croudtech-bootstrap-0.1.8/croudtech_bootstrap.egg-info/SOURCES.txt` & `croudtech-bootstrap-0.1.9/croudtech_bootstrap.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `croudtech-bootstrap-0.1.8/croudtech_bootstrap.egg-info/requires.txt` & `croudtech-bootstrap-0.1.9/croudtech_bootstrap.egg-info/requires.txt`

 * *Files identical despite different names*

### Comparing `croudtech-bootstrap-0.1.8/croudtech_bootstrap_app/bootstrap.py` & `croudtech-bootstrap-0.1.9/croudtech_bootstrap_app/bootstrap.py`

 * *Files identical despite different names*

### Comparing `croudtech-bootstrap-0.1.8/croudtech_bootstrap_app/cli.py` & `croudtech-bootstrap-0.1.9/croudtech_bootstrap_app/cli.py`

 * *Files identical despite different names*

### Comparing `croudtech-bootstrap-0.1.8/croudtech_bootstrap_app/logging.py` & `croudtech-bootstrap-0.1.9/croudtech_bootstrap_app/logging.py`

 * *Files identical despite different names*

### Comparing `croudtech-bootstrap-0.1.8/croudtech_bootstrap_app/metrics.py` & `croudtech-bootstrap-0.1.9/croudtech_bootstrap_app/metrics.py`

 * *Files identical despite different names*

### Comparing `croudtech-bootstrap-0.1.8/croudtech_bootstrap_app/redis_config.py` & `croudtech-bootstrap-0.1.9/croudtech_bootstrap_app/redis_config.py`

 * *Files identical despite different names*

### Comparing `croudtech-bootstrap-0.1.8/croudtech_bootstrap_app/tests/bootstrap_test.py` & `croudtech-bootstrap-0.1.9/croudtech_bootstrap_app/tests/bootstrap_test.py`

 * *Files identical despite different names*

### Comparing `croudtech-bootstrap-0.1.8/requirements.txt` & `croudtech-bootstrap-0.1.9/requirements.txt`

 * *Files identical despite different names*

### Comparing `croudtech-bootstrap-0.1.8/setup.cfg` & `croudtech-bootstrap-0.1.9/setup.cfg`

 * *Files identical despite different names*

