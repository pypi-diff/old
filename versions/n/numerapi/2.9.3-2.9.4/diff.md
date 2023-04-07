# Comparing `tmp/numerapi-2.9.3.tar.gz` & `tmp/numerapi-2.9.4.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "numerapi-2.9.3.tar", last modified: Fri Nov 12 21:30:01 2021, max compression
+gzip compressed data, was "numerapi-2.9.4.tar", last modified: Sun Nov 14 12:24:00 2021, max compression
```

## Comparing `numerapi-2.9.3.tar` & `numerapi-2.9.4.tar`

### file list

```diff
@@ -1,20 +1,20 @@
-drwxr-xr-x   0 runner    (1001) docker     (116)        0 2021-11-12 21:30:01.266423 numerapi-2.9.3/
--rw-r--r--   0 runner    (1001) docker     (116)     1056 2021-11-12 21:29:57.000000 numerapi-2.9.3/LICENSE
--rw-r--r--   0 runner    (1001) docker     (116)     8160 2021-11-12 21:30:01.266423 numerapi-2.9.3/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (116)     6225 2021-11-12 21:29:57.000000 numerapi-2.9.3/README.md
-drwxr-xr-x   0 runner    (1001) docker     (116)        0 2021-11-12 21:30:01.262422 numerapi-2.9.3/numerapi/
--rw-r--r--   0 runner    (1001) docker     (116)      355 2021-11-12 21:29:57.000000 numerapi-2.9.3/numerapi/__init__.py
--rw-r--r--   0 runner    (1001) docker     (116)    24980 2021-11-12 21:29:57.000000 numerapi-2.9.3/numerapi/base_api.py
--rw-r--r--   0 runner    (1001) docker     (116)     7564 2021-11-12 21:29:57.000000 numerapi-2.9.3/numerapi/cli.py
--rw-r--r--   0 runner    (1001) docker     (116)    42148 2021-11-12 21:29:57.000000 numerapi-2.9.3/numerapi/numerapi.py
--rw-r--r--   0 runner    (1001) docker     (116)    16583 2021-11-12 21:29:57.000000 numerapi-2.9.3/numerapi/signalsapi.py
--rw-r--r--   0 runner    (1001) docker     (116)     3633 2021-11-12 21:29:57.000000 numerapi-2.9.3/numerapi/utils.py
-drwxr-xr-x   0 runner    (1001) docker     (116)        0 2021-11-12 21:30:01.266423 numerapi-2.9.3/numerapi.egg-info/
--rw-r--r--   0 runner    (1001) docker     (116)     8160 2021-11-12 21:30:01.000000 numerapi-2.9.3/numerapi.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (116)      340 2021-11-12 21:30:01.000000 numerapi-2.9.3/numerapi.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (116)        1 2021-11-12 21:30:01.000000 numerapi-2.9.3/numerapi.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (116)       47 2021-11-12 21:30:01.000000 numerapi-2.9.3/numerapi.egg-info/entry_points.txt
--rw-r--r--   0 runner    (1001) docker     (116)       68 2021-11-12 21:30:01.000000 numerapi-2.9.3/numerapi.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (116)        9 2021-11-12 21:30:01.000000 numerapi-2.9.3/numerapi.egg-info/top_level.txt
--rw-r--r--   0 runner    (1001) docker     (116)       38 2021-11-12 21:30:01.266423 numerapi-2.9.3/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (116)     1411 2021-11-12 21:29:57.000000 numerapi-2.9.3/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (116)        0 2021-11-14 12:24:00.020230 numerapi-2.9.4/
+-rw-r--r--   0 runner    (1001) docker     (116)     1056 2021-11-14 12:23:55.000000 numerapi-2.9.4/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (116)     8160 2021-11-14 12:24:00.020230 numerapi-2.9.4/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (116)     6225 2021-11-14 12:23:55.000000 numerapi-2.9.4/README.md
+drwxr-xr-x   0 runner    (1001) docker     (116)        0 2021-11-14 12:24:00.020230 numerapi-2.9.4/numerapi/
+-rw-r--r--   0 runner    (1001) docker     (116)      355 2021-11-14 12:23:55.000000 numerapi-2.9.4/numerapi/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (116)    24980 2021-11-14 12:23:55.000000 numerapi-2.9.4/numerapi/base_api.py
+-rw-r--r--   0 runner    (1001) docker     (116)     7572 2021-11-14 12:23:55.000000 numerapi-2.9.4/numerapi/cli.py
+-rw-r--r--   0 runner    (1001) docker     (116)    42148 2021-11-14 12:23:55.000000 numerapi-2.9.4/numerapi/numerapi.py
+-rw-r--r--   0 runner    (1001) docker     (116)    16583 2021-11-14 12:23:55.000000 numerapi-2.9.4/numerapi/signalsapi.py
+-rw-r--r--   0 runner    (1001) docker     (116)     3633 2021-11-14 12:23:55.000000 numerapi-2.9.4/numerapi/utils.py
+drwxr-xr-x   0 runner    (1001) docker     (116)        0 2021-11-14 12:24:00.020230 numerapi-2.9.4/numerapi.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (116)     8160 2021-11-14 12:23:59.000000 numerapi-2.9.4/numerapi.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (116)      340 2021-11-14 12:24:00.000000 numerapi-2.9.4/numerapi.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (116)        1 2021-11-14 12:23:59.000000 numerapi-2.9.4/numerapi.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (116)       47 2021-11-14 12:23:59.000000 numerapi-2.9.4/numerapi.egg-info/entry_points.txt
+-rw-r--r--   0 runner    (1001) docker     (116)       68 2021-11-14 12:23:59.000000 numerapi-2.9.4/numerapi.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (116)        9 2021-11-14 12:23:59.000000 numerapi-2.9.4/numerapi.egg-info/top_level.txt
+-rw-r--r--   0 runner    (1001) docker     (116)       38 2021-11-14 12:24:00.020230 numerapi-2.9.4/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (116)     1411 2021-11-14 12:23:55.000000 numerapi-2.9.4/setup.py
```

### Comparing `numerapi-2.9.3/LICENSE` & `numerapi-2.9.4/LICENSE`

 * *Files identical despite different names*

### Comparing `numerapi-2.9.3/PKG-INFO` & `numerapi-2.9.4/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: numerapi
-Version: 2.9.3
+Version: 2.9.4
 Summary: Automatically download and upload data for the Numerai machine learning competition
 Home-page: https://github.com/uuazed/numerapi
 Maintainer: uuazed
 Maintainer-email: uuazed@gmail.com
 License: MIT License
 Description: [![Build Status](https://app.travis-ci.com/uuazed/numerapi.svg)](https://app.travis-ci.com/uuazed/numerapi)
         [![codecov](https://codecov.io/gh/uuazed/numerapi/branch/master/graph/badge.svg)](https://codecov.io/gh/uuazed/numerapi)
```

### Comparing `numerapi-2.9.3/README.md` & `numerapi-2.9.4/README.md`

 * *Files identical despite different names*

### Comparing `numerapi-2.9.3/numerapi/base_api.py` & `numerapi-2.9.4/numerapi/base_api.py`

 * *Files identical despite different names*

### Comparing `numerapi-2.9.3/numerapi/cli.py` & `numerapi-2.9.4/numerapi/cli.py`

 * *Files 0% similar despite different names*

```diff
@@ -197,15 +197,15 @@
     '--new_data', is_flag=True, default=False,
     help="set this flag if you are using the new data")
 @click.argument('path', type=click.Path(exists=True))
 def submit(path, tournament, model_id, new_data):
     """Upload predictions from file."""
     data_version = 2 if new_data else 1
     click.echo(napi.upload_predictions(
-        path, tournament, model_id, data_version))
+        path, tournament, model_id, version=data_version))
 
 
 @cli.command()
 @click.argument("username")
 def stake_get(username):
     """Get stake value of a user."""
     click.echo(napi.stake_get(username))
```

### Comparing `numerapi-2.9.3/numerapi/numerapi.py` & `numerapi-2.9.4/numerapi/numerapi.py`

 * *Files identical despite different names*

### Comparing `numerapi-2.9.3/numerapi/signalsapi.py` & `numerapi-2.9.4/numerapi/signalsapi.py`

 * *Files identical despite different names*

### Comparing `numerapi-2.9.3/numerapi/utils.py` & `numerapi-2.9.4/numerapi/utils.py`

 * *Files identical despite different names*

### Comparing `numerapi-2.9.3/numerapi.egg-info/PKG-INFO` & `numerapi-2.9.4/numerapi.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: numerapi
-Version: 2.9.3
+Version: 2.9.4
 Summary: Automatically download and upload data for the Numerai machine learning competition
 Home-page: https://github.com/uuazed/numerapi
 Maintainer: uuazed
 Maintainer-email: uuazed@gmail.com
 License: MIT License
 Description: [![Build Status](https://app.travis-ci.com/uuazed/numerapi.svg)](https://app.travis-ci.com/uuazed/numerapi)
         [![codecov](https://codecov.io/gh/uuazed/numerapi/branch/master/graph/badge.svg)](https://codecov.io/gh/uuazed/numerapi)
```

### Comparing `numerapi-2.9.3/setup.py` & `numerapi-2.9.4/setup.py`

 * *Files 0% similar despite different names*

```diff
@@ -2,15 +2,15 @@
 from setuptools import find_packages
 
 
 def load(path):
     return open(path, 'r').read()
 
 
-numerapi_version = '2.9.3'
+numerapi_version = '2.9.4'
 
 
 classifiers = [
     "Development Status :: 5 - Production/Stable",
     "Environment :: Console",
     "Intended Audience :: Science/Research",
     "License :: OSI Approved :: MIT License",
```

