# Comparing `tmp/zephyr-python-api-0.0.2.tar.gz` & `tmp/zephyr-python-api-0.0.3.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "zephyr-python-api-0.0.2.tar", last modified: Tue Feb  7 13:58:35 2023, max compression
+gzip compressed data, was "zephyr-python-api-0.0.3.tar", last modified: Thu Apr  6 13:14:51 2023, max compression
```

## Comparing `zephyr-python-api-0.0.2.tar` & `zephyr-python-api-0.0.3.tar`

### file list

```diff
@@ -1,46 +1,46 @@
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-02-07 13:58:35.880159 zephyr-python-api-0.0.2/
--rw-r--r--   0 runner    (1001) docker     (122)    11345 2023-02-07 13:57:59.000000 zephyr-python-api-0.0.2/LICENSE
--rw-r--r--   0 runner    (1001) docker     (122)     2620 2023-02-07 13:58:35.880159 zephyr-python-api-0.0.2/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (122)     1859 2023-02-07 13:57:59.000000 zephyr-python-api-0.0.2/README.md
--rw-r--r--   0 runner    (1001) docker     (122)       84 2023-02-07 13:57:59.000000 zephyr-python-api-0.0.2/pyproject.toml
--rw-r--r--   0 runner    (1001) docker     (122)      856 2023-02-07 13:58:35.884159 zephyr-python-api-0.0.2/setup.cfg
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-02-07 13:58:35.872159 zephyr-python-api-0.0.2/zephyr/
--rw-r--r--   0 runner    (1001) docker     (122)      104 2023-02-07 13:57:59.000000 zephyr-python-api-0.0.2/zephyr/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-02-07 13:58:35.876159 zephyr-python-api-0.0.2/zephyr/scale/
--rw-r--r--   0 runner    (1001) docker     (122)       59 2023-02-07 13:57:59.000000 zephyr-python-api-0.0.2/zephyr/scale/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-02-07 13:58:35.876159 zephyr-python-api-0.0.2/zephyr/scale/cloud/
--rw-r--r--   0 runner    (1001) docker     (122)        0 2023-02-07 13:57:59.000000 zephyr-python-api-0.0.2/zephyr/scale/cloud/__init__.py
--rw-r--r--   0 runner    (1001) docker     (122)     2138 2023-02-07 13:57:59.000000 zephyr-python-api-0.0.2/zephyr/scale/cloud/cloud_api.py
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-02-07 13:58:35.880159 zephyr-python-api-0.0.2/zephyr/scale/cloud/endpoints/
--rw-r--r--   0 runner    (1001) docker     (122)      507 2023-02-07 13:57:59.000000 zephyr-python-api-0.0.2/zephyr/scale/cloud/endpoints/__init__.py
--rw-r--r--   0 runner    (1001) docker     (122)     1265 2023-02-07 13:57:59.000000 zephyr-python-api-0.0.2/zephyr/scale/cloud/endpoints/automations.py
--rw-r--r--   0 runner    (1001) docker     (122)      527 2023-02-07 13:57:59.000000 zephyr-python-api-0.0.2/zephyr/scale/cloud/endpoints/environments.py
--rw-r--r--   0 runner    (1001) docker     (122)      778 2023-02-07 13:57:59.000000 zephyr-python-api-0.0.2/zephyr/scale/cloud/endpoints/folders.py
--rw-r--r--   0 runner    (1001) docker     (122)      396 2023-02-07 13:57:59.000000 zephyr-python-api-0.0.2/zephyr/scale/cloud/endpoints/healthcheck.py
--rw-r--r--   0 runner    (1001) docker     (122)      469 2023-02-07 13:57:59.000000 zephyr-python-api-0.0.2/zephyr/scale/cloud/endpoints/links.py
--rw-r--r--   0 runner    (1001) docker     (122)      500 2023-02-07 13:57:59.000000 zephyr-python-api-0.0.2/zephyr/scale/cloud/endpoints/priorities.py
--rw-r--r--   0 runner    (1001) docker     (122)      482 2023-02-07 13:57:59.000000 zephyr-python-api-0.0.2/zephyr/scale/cloud/endpoints/projects.py
--rw-r--r--   0 runner    (1001) docker     (122)      480 2023-02-07 13:57:59.000000 zephyr-python-api-0.0.2/zephyr/scale/cloud/endpoints/statuses.py
--rw-r--r--   0 runner    (1001) docker     (122)     6182 2023-02-07 13:57:59.000000 zephyr-python-api-0.0.2/zephyr/scale/cloud/endpoints/test_cases.py
--rw-r--r--   0 runner    (1001) docker     (122)     2693 2023-02-07 13:57:59.000000 zephyr-python-api-0.0.2/zephyr/scale/cloud/endpoints/test_cycles.py
--rw-r--r--   0 runner    (1001) docker     (122)     1938 2023-02-07 13:57:59.000000 zephyr-python-api-0.0.2/zephyr/scale/cloud/endpoints/test_executions.py
--rw-r--r--   0 runner    (1001) docker     (122)      720 2023-02-07 13:57:59.000000 zephyr-python-api-0.0.2/zephyr/scale/cloud/endpoints/test_plans.py
--rw-r--r--   0 runner    (1001) docker     (122)     1345 2023-02-07 13:57:59.000000 zephyr-python-api-0.0.2/zephyr/scale/scale.py
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-02-07 13:58:35.880159 zephyr-python-api-0.0.2/zephyr/scale/server/
--rw-r--r--   0 runner    (1001) docker     (122)        0 2023-02-07 13:57:59.000000 zephyr-python-api-0.0.2/zephyr/scale/server/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-02-07 13:58:35.880159 zephyr-python-api-0.0.2/zephyr/scale/server/endpoints/
--rw-r--r--   0 runner    (1001) docker     (122)      532 2023-02-07 13:57:59.000000 zephyr-python-api-0.0.2/zephyr/scale/server/endpoints/__init__.py
--rw-r--r--   0 runner    (1001) docker     (122)    15428 2023-02-07 13:57:59.000000 zephyr-python-api-0.0.2/zephyr/scale/server/endpoints/endpoints.py
--rw-r--r--   0 runner    (1001) docker     (122)     1644 2023-02-07 13:57:59.000000 zephyr-python-api-0.0.2/zephyr/scale/server/endpoints/paths.py
--rw-r--r--   0 runner    (1001) docker     (122)     1550 2023-02-07 13:57:59.000000 zephyr-python-api-0.0.2/zephyr/scale/server/server_api.py
--rw-r--r--   0 runner    (1001) docker     (122)     1142 2023-02-07 13:57:59.000000 zephyr-python-api-0.0.2/zephyr/scale/server/server_defaults.py
--rw-r--r--   0 runner    (1001) docker     (122)     4126 2023-02-07 13:57:59.000000 zephyr-python-api-0.0.2/zephyr/scale/zephyr_session.py
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-02-07 13:58:35.880159 zephyr-python-api-0.0.2/zephyr/utils/
--rw-r--r--   0 runner    (1001) docker     (122)        0 2023-02-07 13:57:59.000000 zephyr-python-api-0.0.2/zephyr/utils/__init__.py
--rw-r--r--   0 runner    (1001) docker     (122)      524 2023-02-07 13:57:59.000000 zephyr-python-api-0.0.2/zephyr/utils/common.py
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-02-07 13:58:35.880159 zephyr-python-api-0.0.2/zephyr_python_api.egg-info/
--rw-r--r--   0 runner    (1001) docker     (122)     2620 2023-02-07 13:58:35.000000 zephyr-python-api-0.0.2/zephyr_python_api.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (122)     1238 2023-02-07 13:58:35.000000 zephyr-python-api-0.0.2/zephyr_python_api.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (122)        1 2023-02-07 13:58:35.000000 zephyr-python-api-0.0.2/zephyr_python_api.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (122)        9 2023-02-07 13:58:35.000000 zephyr-python-api-0.0.2/zephyr_python_api.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (122)        7 2023-02-07 13:58:35.000000 zephyr-python-api-0.0.2/zephyr_python_api.egg-info/top_level.txt
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 13:14:51.477127 zephyr-python-api-0.0.3/
+-rw-r--r--   0 runner    (1001) docker     (122)    11345 2023-04-06 13:14:04.000000 zephyr-python-api-0.0.3/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (122)     2707 2023-04-06 13:14:51.477127 zephyr-python-api-0.0.3/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (122)     1946 2023-04-06 13:14:04.000000 zephyr-python-api-0.0.3/README.md
+-rw-r--r--   0 runner    (1001) docker     (122)       84 2023-04-06 13:14:04.000000 zephyr-python-api-0.0.3/pyproject.toml
+-rw-r--r--   0 runner    (1001) docker     (122)      856 2023-04-06 13:14:51.477127 zephyr-python-api-0.0.3/setup.cfg
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 13:14:51.469127 zephyr-python-api-0.0.3/zephyr/
+-rw-r--r--   0 runner    (1001) docker     (122)      104 2023-04-06 13:14:04.000000 zephyr-python-api-0.0.3/zephyr/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 13:14:51.469127 zephyr-python-api-0.0.3/zephyr/scale/
+-rw-r--r--   0 runner    (1001) docker     (122)       59 2023-04-06 13:14:04.000000 zephyr-python-api-0.0.3/zephyr/scale/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 13:14:51.469127 zephyr-python-api-0.0.3/zephyr/scale/cloud/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2023-04-06 13:14:04.000000 zephyr-python-api-0.0.3/zephyr/scale/cloud/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)     2138 2023-04-06 13:14:04.000000 zephyr-python-api-0.0.3/zephyr/scale/cloud/cloud_api.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 13:14:51.473127 zephyr-python-api-0.0.3/zephyr/scale/cloud/endpoints/
+-rw-r--r--   0 runner    (1001) docker     (122)      507 2023-04-06 13:14:04.000000 zephyr-python-api-0.0.3/zephyr/scale/cloud/endpoints/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)     4685 2023-04-06 13:14:04.000000 zephyr-python-api-0.0.3/zephyr/scale/cloud/endpoints/automations.py
+-rw-r--r--   0 runner    (1001) docker     (122)      527 2023-04-06 13:14:04.000000 zephyr-python-api-0.0.3/zephyr/scale/cloud/endpoints/environments.py
+-rw-r--r--   0 runner    (1001) docker     (122)      778 2023-04-06 13:14:04.000000 zephyr-python-api-0.0.3/zephyr/scale/cloud/endpoints/folders.py
+-rw-r--r--   0 runner    (1001) docker     (122)      396 2023-04-06 13:14:04.000000 zephyr-python-api-0.0.3/zephyr/scale/cloud/endpoints/healthcheck.py
+-rw-r--r--   0 runner    (1001) docker     (122)      469 2023-04-06 13:14:04.000000 zephyr-python-api-0.0.3/zephyr/scale/cloud/endpoints/links.py
+-rw-r--r--   0 runner    (1001) docker     (122)      500 2023-04-06 13:14:04.000000 zephyr-python-api-0.0.3/zephyr/scale/cloud/endpoints/priorities.py
+-rw-r--r--   0 runner    (1001) docker     (122)      482 2023-04-06 13:14:04.000000 zephyr-python-api-0.0.3/zephyr/scale/cloud/endpoints/projects.py
+-rw-r--r--   0 runner    (1001) docker     (122)      480 2023-04-06 13:14:04.000000 zephyr-python-api-0.0.3/zephyr/scale/cloud/endpoints/statuses.py
+-rw-r--r--   0 runner    (1001) docker     (122)     6182 2023-04-06 13:14:04.000000 zephyr-python-api-0.0.3/zephyr/scale/cloud/endpoints/test_cases.py
+-rw-r--r--   0 runner    (1001) docker     (122)     2693 2023-04-06 13:14:04.000000 zephyr-python-api-0.0.3/zephyr/scale/cloud/endpoints/test_cycles.py
+-rw-r--r--   0 runner    (1001) docker     (122)     1938 2023-04-06 13:14:04.000000 zephyr-python-api-0.0.3/zephyr/scale/cloud/endpoints/test_executions.py
+-rw-r--r--   0 runner    (1001) docker     (122)      720 2023-04-06 13:14:04.000000 zephyr-python-api-0.0.3/zephyr/scale/cloud/endpoints/test_plans.py
+-rw-r--r--   0 runner    (1001) docker     (122)     1345 2023-04-06 13:14:04.000000 zephyr-python-api-0.0.3/zephyr/scale/scale.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 13:14:51.473127 zephyr-python-api-0.0.3/zephyr/scale/server/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2023-04-06 13:14:04.000000 zephyr-python-api-0.0.3/zephyr/scale/server/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 13:14:51.473127 zephyr-python-api-0.0.3/zephyr/scale/server/endpoints/
+-rw-r--r--   0 runner    (1001) docker     (122)      532 2023-04-06 13:14:04.000000 zephyr-python-api-0.0.3/zephyr/scale/server/endpoints/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)    15428 2023-04-06 13:14:04.000000 zephyr-python-api-0.0.3/zephyr/scale/server/endpoints/endpoints.py
+-rw-r--r--   0 runner    (1001) docker     (122)     1644 2023-04-06 13:14:04.000000 zephyr-python-api-0.0.3/zephyr/scale/server/endpoints/paths.py
+-rw-r--r--   0 runner    (1001) docker     (122)     1550 2023-04-06 13:14:04.000000 zephyr-python-api-0.0.3/zephyr/scale/server/server_api.py
+-rw-r--r--   0 runner    (1001) docker     (122)     1142 2023-04-06 13:14:04.000000 zephyr-python-api-0.0.3/zephyr/scale/server/server_defaults.py
+-rw-r--r--   0 runner    (1001) docker     (122)     4207 2023-04-06 13:14:04.000000 zephyr-python-api-0.0.3/zephyr/scale/zephyr_session.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 13:14:51.473127 zephyr-python-api-0.0.3/zephyr/utils/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2023-04-06 13:14:04.000000 zephyr-python-api-0.0.3/zephyr/utils/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)      524 2023-04-06 13:14:04.000000 zephyr-python-api-0.0.3/zephyr/utils/common.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 13:14:51.477127 zephyr-python-api-0.0.3/zephyr_python_api.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (122)     2707 2023-04-06 13:14:51.000000 zephyr-python-api-0.0.3/zephyr_python_api.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (122)     1238 2023-04-06 13:14:51.000000 zephyr-python-api-0.0.3/zephyr_python_api.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (122)        1 2023-04-06 13:14:51.000000 zephyr-python-api-0.0.3/zephyr_python_api.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (122)        9 2023-04-06 13:14:51.000000 zephyr-python-api-0.0.3/zephyr_python_api.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (122)        7 2023-04-06 13:14:51.000000 zephyr-python-api-0.0.3/zephyr_python_api.egg-info/top_level.txt
```

### Comparing `zephyr-python-api-0.0.2/LICENSE` & `zephyr-python-api-0.0.3/LICENSE`

 * *Files identical despite different names*

### Comparing `zephyr-python-api-0.0.2/PKG-INFO` & `zephyr-python-api-0.0.3/PKG-INFO`

 * *Files 13% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: zephyr-python-api
-Version: 0.0.2
+Version: 0.0.3
 Summary: Zephyr (TM4J) Python REST API wrapper
 Home-page: https://github.com/nassauwinter/zephyr-python-api
 Author: Petr Sharapenko
 Author-email: nassauwinter@gmail.com
 Project-URL: Bug Tracker, https://github.com/nassauwinter/zephyr-python-api/issues
 Classifier: Programming Language :: Python :: 3.6
 Classifier: Programming Language :: Python :: 3.7
@@ -73,14 +73,18 @@
 # Get a single test case by its id
 test_case = zapi.test_cases.get_test_case("<test_case_id>")
 
 # Create a test case
 creation_result = zapi.test_cases.create_test_case("<project_key>", "test_case_name")
 ```
 
+### Troubleshooting
+
+For troubleshooting see [TROUBLESHOOTING.md](TROUBLESHOOTING.md)
+
 
 ### License
 
 This library is licensed under the Apache 2.0 License.
 
 ### Links
```

### Comparing `zephyr-python-api-0.0.2/README.md` & `zephyr-python-api-0.0.3/README.md`

 * *Files 7% similar despite different names*

```diff
@@ -54,14 +54,18 @@
 # Get a single test case by its id
 test_case = zapi.test_cases.get_test_case("<test_case_id>")
 
 # Create a test case
 creation_result = zapi.test_cases.create_test_case("<project_key>", "test_case_name")
 ```
 
+### Troubleshooting
+
+For troubleshooting see [TROUBLESHOOTING.md](TROUBLESHOOTING.md)
+
 
 ### License
 
 This library is licensed under the Apache 2.0 License.
 
 ### Links
```

### Comparing `zephyr-python-api-0.0.2/setup.cfg` & `zephyr-python-api-0.0.3/setup.cfg`

 * *Files 11% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 [metadata]
 name = zephyr-python-api
-version = 0.0.2
+version = 0.0.3
 author = Petr Sharapenko
 author_email = nassauwinter@gmail.com
 description = Zephyr (TM4J) Python REST API wrapper
 long_description = file: README.md
 long_description_content_type = text/markdown
 url = https://github.com/nassauwinter/zephyr-python-api
 project_urls =
```

### Comparing `zephyr-python-api-0.0.2/zephyr/scale/cloud/cloud_api.py` & `zephyr-python-api-0.0.3/zephyr/scale/cloud/cloud_api.py`

 * *Files identical despite different names*

### Comparing `zephyr-python-api-0.0.2/zephyr/scale/cloud/endpoints/environments.py` & `zephyr-python-api-0.0.3/zephyr/scale/cloud/endpoints/environments.py`

 * *Files identical despite different names*

### Comparing `zephyr-python-api-0.0.2/zephyr/scale/cloud/endpoints/folders.py` & `zephyr-python-api-0.0.3/zephyr/scale/cloud/endpoints/folders.py`

 * *Files identical despite different names*

### Comparing `zephyr-python-api-0.0.2/zephyr/scale/cloud/endpoints/test_cases.py` & `zephyr-python-api-0.0.3/zephyr/scale/cloud/endpoints/test_cases.py`

 * *Files identical despite different names*

### Comparing `zephyr-python-api-0.0.2/zephyr/scale/cloud/endpoints/test_cycles.py` & `zephyr-python-api-0.0.3/zephyr/scale/cloud/endpoints/test_cycles.py`

 * *Files identical despite different names*

### Comparing `zephyr-python-api-0.0.2/zephyr/scale/cloud/endpoints/test_executions.py` & `zephyr-python-api-0.0.3/zephyr/scale/cloud/endpoints/test_executions.py`

 * *Files identical despite different names*

### Comparing `zephyr-python-api-0.0.2/zephyr/scale/cloud/endpoints/test_plans.py` & `zephyr-python-api-0.0.3/zephyr/scale/cloud/endpoints/test_plans.py`

 * *Files identical despite different names*

### Comparing `zephyr-python-api-0.0.2/zephyr/scale/scale.py` & `zephyr-python-api-0.0.3/zephyr/scale/scale.py`

 * *Files identical despite different names*

### Comparing `zephyr-python-api-0.0.2/zephyr/scale/server/endpoints/__init__.py` & `zephyr-python-api-0.0.3/zephyr/scale/server/endpoints/__init__.py`

 * *Files identical despite different names*

### Comparing `zephyr-python-api-0.0.2/zephyr/scale/server/endpoints/endpoints.py` & `zephyr-python-api-0.0.3/zephyr/scale/server/endpoints/endpoints.py`

 * *Files identical despite different names*

### Comparing `zephyr-python-api-0.0.2/zephyr/scale/server/endpoints/paths.py` & `zephyr-python-api-0.0.3/zephyr/scale/server/endpoints/paths.py`

 * *Files identical despite different names*

### Comparing `zephyr-python-api-0.0.2/zephyr/scale/server/server_api.py` & `zephyr-python-api-0.0.3/zephyr/scale/server/server_api.py`

 * *Files identical despite different names*

### Comparing `zephyr-python-api-0.0.2/zephyr/scale/server/server_defaults.py` & `zephyr-python-api-0.0.3/zephyr/scale/server/server_defaults.py`

 * *Files identical despite different names*

### Comparing `zephyr-python-api-0.0.2/zephyr/scale/zephyr_session.py` & `zephyr-python-api-0.0.3/zephyr/scale/zephyr_session.py`

 * *Files 6% similar despite different names*

```diff
@@ -97,15 +97,19 @@
                 yield value
             if response.get("isLast") is True:
                 break
             params_str = urlparse(response.get("next")).query
             params.update(parse_qs(params_str))
         return
 
-    def post_file(self, endpoint: str, file_path: str, **kwargs):
+    def post_file(self, endpoint: str, file_path: str, to_files=None, **kwargs):
         """
         Post wrapper to send a file. Handles single file opening,
         sending its content and closing
         """
         with open(file_path, "rb") as file:
             files = {"file": file}
+
+            if to_files:
+                files.update(to_files)
+
             return self._request("post", endpoint, files=files, **kwargs)
```

### Comparing `zephyr-python-api-0.0.2/zephyr/utils/common.py` & `zephyr-python-api-0.0.3/zephyr/utils/common.py`

 * *Files identical despite different names*

### Comparing `zephyr-python-api-0.0.2/zephyr_python_api.egg-info/PKG-INFO` & `zephyr-python-api-0.0.3/zephyr_python_api.egg-info/PKG-INFO`

 * *Files 13% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: zephyr-python-api
-Version: 0.0.2
+Version: 0.0.3
 Summary: Zephyr (TM4J) Python REST API wrapper
 Home-page: https://github.com/nassauwinter/zephyr-python-api
 Author: Petr Sharapenko
 Author-email: nassauwinter@gmail.com
 Project-URL: Bug Tracker, https://github.com/nassauwinter/zephyr-python-api/issues
 Classifier: Programming Language :: Python :: 3.6
 Classifier: Programming Language :: Python :: 3.7
@@ -73,14 +73,18 @@
 # Get a single test case by its id
 test_case = zapi.test_cases.get_test_case("<test_case_id>")
 
 # Create a test case
 creation_result = zapi.test_cases.create_test_case("<project_key>", "test_case_name")
 ```
 
+### Troubleshooting
+
+For troubleshooting see [TROUBLESHOOTING.md](TROUBLESHOOTING.md)
+
 
 ### License
 
 This library is licensed under the Apache 2.0 License.
 
 ### Links
```

### Comparing `zephyr-python-api-0.0.2/zephyr_python_api.egg-info/SOURCES.txt` & `zephyr-python-api-0.0.3/zephyr_python_api.egg-info/SOURCES.txt`

 * *Files identical despite different names*

