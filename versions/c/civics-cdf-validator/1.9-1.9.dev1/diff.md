# Comparing `tmp/civics_cdf_validator-1.9.tar.gz` & `tmp/civics_cdf_validator-1.9.dev1.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "civics_cdf_validator-1.9.tar", last modified: Wed Jan 13 10:26:46 2021, max compression
+gzip compressed data, was "dist/civics_cdf_validator-1.9.dev1.tar", last modified: Wed Dec 16 16:01:00 2020, max compression
```

## Comparing `civics_cdf_validator-1.9.tar` & `civics_cdf_validator-1.9.dev1.tar`

### file list

```diff
@@ -1,24 +1,24 @@
-drwxr-xr-x   0 runner    (1001) docker     (116)        0 2021-01-13 10:26:46.930590 civics_cdf_validator-1.9/
--rw-r--r--   0 runner    (1001) docker     (116)     3720 2021-01-13 10:26:32.000000 civics_cdf_validator-1.9/CONTRIBUTING.md
--rw-r--r--   0 runner    (1001) docker     (116)    11358 2021-01-13 10:26:32.000000 civics_cdf_validator-1.9/LICENSE-2.0.txt
--rw-r--r--   0 runner    (1001) docker     (116)       96 2021-01-13 10:26:32.000000 civics_cdf_validator-1.9/MANIFEST.in
--rw-r--r--   0 runner    (1001) docker     (116)      560 2021-01-13 10:26:46.930590 civics_cdf_validator-1.9/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (116)     2247 2021-01-13 10:26:32.000000 civics_cdf_validator-1.9/README.md
--rw-r--r--   0 runner    (1001) docker     (116)        0 2021-01-13 10:26:32.000000 civics_cdf_validator-1.9/__init__.py
--rw-r--r--   0 runner    (1001) docker     (116)    12211 2021-01-13 10:26:32.000000 civics_cdf_validator-1.9/base.py
-drwxr-xr-x   0 runner    (1001) docker     (116)        0 2021-01-13 10:26:46.930590 civics_cdf_validator-1.9/civics_cdf_validator.egg-info/
--rw-r--r--   0 runner    (1001) docker     (116)      560 2021-01-13 10:26:46.000000 civics_cdf_validator-1.9/civics_cdf_validator.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (116)      443 2021-01-13 10:26:46.000000 civics_cdf_validator-1.9/civics_cdf_validator.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (116)        1 2021-01-13 10:26:46.000000 civics_cdf_validator-1.9/civics_cdf_validator.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (116)       78 2021-01-13 10:26:46.000000 civics_cdf_validator-1.9/civics_cdf_validator.egg-info/entry_points.txt
--rw-r--r--   0 runner    (1001) docker     (116)       78 2021-01-13 10:26:46.000000 civics_cdf_validator-1.9/civics_cdf_validator.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (116)       21 2021-01-13 10:26:46.000000 civics_cdf_validator-1.9/civics_cdf_validator.egg-info/top_level.txt
--rwxr-xr-x   0 runner    (1001) docker     (116)     6255 2021-01-13 10:26:32.000000 civics_cdf_validator-1.9/gpunit_rules.py
--rw-r--r--   0 runner    (1001) docker     (116)     6830 2021-01-13 10:26:32.000000 civics_cdf_validator-1.9/loggers.py
--rw-r--r--   0 runner    (1001) docker     (116)     2319 2021-01-13 10:26:32.000000 civics_cdf_validator-1.9/office_utils.py
--rwxr-xr-x   0 runner    (1001) docker     (116)    93100 2021-01-13 10:26:32.000000 civics_cdf_validator-1.9/rules.py
--rw-r--r--   0 runner    (1001) docker     (116)       63 2021-01-13 10:26:46.930590 civics_cdf_validator-1.9/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (116)     2251 2021-01-13 10:26:32.000000 civics_cdf_validator-1.9/setup.py
--rw-r--r--   0 runner    (1001) docker     (116)     3809 2021-01-13 10:26:32.000000 civics_cdf_validator-1.9/stats.py
--rwxr-xr-x   0 runner    (1001) docker     (116)    11294 2021-01-13 10:26:32.000000 civics_cdf_validator-1.9/validator.py
--rw-r--r--   0 runner    (1001) docker     (116)      182 2021-01-13 10:26:32.000000 civics_cdf_validator-1.9/version.py
+drwxr-xr-x   0 runner    (1001) docker     (116)        0 2020-12-16 16:01:00.188761 civics_cdf_validator-1.9.dev1/
+-rw-r--r--   0 runner    (1001) docker     (116)     3720 2020-12-16 16:00:50.000000 civics_cdf_validator-1.9.dev1/CONTRIBUTING.md
+-rw-r--r--   0 runner    (1001) docker     (116)    11358 2020-12-16 16:00:50.000000 civics_cdf_validator-1.9.dev1/LICENSE-2.0.txt
+-rw-r--r--   0 runner    (1001) docker     (116)       96 2020-12-16 16:00:50.000000 civics_cdf_validator-1.9.dev1/MANIFEST.in
+-rw-r--r--   0 runner    (1001) docker     (116)      565 2020-12-16 16:01:00.188761 civics_cdf_validator-1.9.dev1/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (116)     2247 2020-12-16 16:00:50.000000 civics_cdf_validator-1.9.dev1/README.md
+-rw-r--r--   0 runner    (1001) docker     (116)        0 2020-12-16 16:00:50.000000 civics_cdf_validator-1.9.dev1/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (116)    12211 2020-12-16 16:00:50.000000 civics_cdf_validator-1.9.dev1/base.py
+drwxr-xr-x   0 runner    (1001) docker     (116)        0 2020-12-16 16:01:00.188761 civics_cdf_validator-1.9.dev1/civics_cdf_validator.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (116)      565 2020-12-16 16:01:00.000000 civics_cdf_validator-1.9.dev1/civics_cdf_validator.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (116)      443 2020-12-16 16:01:00.000000 civics_cdf_validator-1.9.dev1/civics_cdf_validator.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (116)        1 2020-12-16 16:01:00.000000 civics_cdf_validator-1.9.dev1/civics_cdf_validator.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (116)       78 2020-12-16 16:01:00.000000 civics_cdf_validator-1.9.dev1/civics_cdf_validator.egg-info/entry_points.txt
+-rw-r--r--   0 runner    (1001) docker     (116)       78 2020-12-16 16:01:00.000000 civics_cdf_validator-1.9.dev1/civics_cdf_validator.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (116)       21 2020-12-16 16:01:00.000000 civics_cdf_validator-1.9.dev1/civics_cdf_validator.egg-info/top_level.txt
+-rwxr-xr-x   0 runner    (1001) docker     (116)     6255 2020-12-16 16:00:50.000000 civics_cdf_validator-1.9.dev1/gpunit_rules.py
+-rw-r--r--   0 runner    (1001) docker     (116)     6830 2020-12-16 16:00:50.000000 civics_cdf_validator-1.9.dev1/loggers.py
+-rw-r--r--   0 runner    (1001) docker     (116)     2319 2020-12-16 16:00:50.000000 civics_cdf_validator-1.9.dev1/office_utils.py
+-rwxr-xr-x   0 runner    (1001) docker     (116)    93100 2020-12-16 16:00:50.000000 civics_cdf_validator-1.9.dev1/rules.py
+-rw-r--r--   0 runner    (1001) docker     (116)       63 2020-12-16 16:01:00.188761 civics_cdf_validator-1.9.dev1/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (116)     2251 2020-12-16 16:00:50.000000 civics_cdf_validator-1.9.dev1/setup.py
+-rw-r--r--   0 runner    (1001) docker     (116)     3809 2020-12-16 16:00:50.000000 civics_cdf_validator-1.9.dev1/stats.py
+-rwxr-xr-x   0 runner    (1001) docker     (116)    11294 2020-12-16 16:00:50.000000 civics_cdf_validator-1.9.dev1/validator.py
+-rw-r--r--   0 runner    (1001) docker     (116)      187 2020-12-16 16:00:50.000000 civics_cdf_validator-1.9.dev1/version.py
```

### Comparing `civics_cdf_validator-1.9/CONTRIBUTING.md` & `civics_cdf_validator-1.9.dev1/CONTRIBUTING.md`

 * *Files identical despite different names*

### Comparing `civics_cdf_validator-1.9/LICENSE-2.0.txt` & `civics_cdf_validator-1.9.dev1/LICENSE-2.0.txt`

 * *Files identical despite different names*

### Comparing `civics_cdf_validator-1.9/PKG-INFO` & `civics_cdf_validator-1.9.dev1/PKG-INFO`

 * *Files 2% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 1.2
 Name: civics_cdf_validator
-Version: 1.9
+Version: 1.9.dev1
 Summary: Checks if an election feed follows best practices
 Home-page: https://github.com/google/civics_cdf_validator
 Author: Google Civics
 Author-email: election-results-xml-validator@google.com
 Maintainer: gVelocity Civics
 Maintainer-email: election-results-xml-validator@google.com
 License: Apache License
```

### Comparing `civics_cdf_validator-1.9/README.md` & `civics_cdf_validator-1.9.dev1/README.md`

 * *Files identical despite different names*

### Comparing `civics_cdf_validator-1.9/base.py` & `civics_cdf_validator-1.9.dev1/base.py`

 * *Files identical despite different names*

### Comparing `civics_cdf_validator-1.9/civics_cdf_validator.egg-info/PKG-INFO` & `civics_cdf_validator-1.9.dev1/civics_cdf_validator.egg-info/PKG-INFO`

 * *Files 2% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 1.2
 Name: civics-cdf-validator
-Version: 1.9
+Version: 1.9.dev1
 Summary: Checks if an election feed follows best practices
 Home-page: https://github.com/google/civics_cdf_validator
 Author: Google Civics
 Author-email: election-results-xml-validator@google.com
 Maintainer: gVelocity Civics
 Maintainer-email: election-results-xml-validator@google.com
 License: Apache License
```

### Comparing `civics_cdf_validator-1.9/gpunit_rules.py` & `civics_cdf_validator-1.9.dev1/gpunit_rules.py`

 * *Files identical despite different names*

### Comparing `civics_cdf_validator-1.9/loggers.py` & `civics_cdf_validator-1.9.dev1/loggers.py`

 * *Files identical despite different names*

### Comparing `civics_cdf_validator-1.9/office_utils.py` & `civics_cdf_validator-1.9.dev1/office_utils.py`

 * *Files identical despite different names*

### Comparing `civics_cdf_validator-1.9/rules.py` & `civics_cdf_validator-1.9.dev1/rules.py`

 * *Files identical despite different names*

### Comparing `civics_cdf_validator-1.9/setup.py` & `civics_cdf_validator-1.9.dev1/setup.py`

 * *Files identical despite different names*

### Comparing `civics_cdf_validator-1.9/stats.py` & `civics_cdf_validator-1.9.dev1/stats.py`

 * *Files identical despite different names*

### Comparing `civics_cdf_validator-1.9/validator.py` & `civics_cdf_validator-1.9.dev1/validator.py`

 * *Files identical despite different names*

