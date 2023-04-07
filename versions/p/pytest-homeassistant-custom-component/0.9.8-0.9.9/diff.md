# Comparing `tmp/pytest-homeassistant-custom-component-0.9.8.tar.gz` & `tmp/pytest-homeassistant-custom-component-0.9.9.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "pytest-homeassistant-custom-component-0.9.8.tar", last modified: Tue May 31 05:18:36 2022, max compression
+gzip compressed data, was "pytest-homeassistant-custom-component-0.9.9.tar", last modified: Wed Jun  1 05:43:30 2022, max compression
```

## Comparing `pytest-homeassistant-custom-component-0.9.8.tar` & `pytest-homeassistant-custom-component-0.9.9.tar`

### file list

```diff
@@ -1,47 +1,47 @@
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-05-31 05:18:36.067147 pytest-homeassistant-custom-component-0.9.8/
--rw-r--r--   0 runner    (1001) docker     (121)     1070 2022-05-31 05:18:22.000000 pytest-homeassistant-custom-component-0.9.8/LICENSE
--rw-r--r--   0 runner    (1001) docker     (121)    11357 2022-05-31 05:18:22.000000 pytest-homeassistant-custom-component-0.9.8/LICENSE_HA_CORE.md
--rw-r--r--   0 runner    (1001) docker     (121)      771 2022-05-31 05:18:36.067147 pytest-homeassistant-custom-component-0.9.8/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (121)     2995 2022-05-31 05:18:22.000000 pytest-homeassistant-custom-component-0.9.8/README.md
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-05-31 05:18:36.063147 pytest-homeassistant-custom-component-0.9.8/custom_components/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-05-31 05:18:23.000000 pytest-homeassistant-custom-component-0.9.8/custom_components/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-05-31 05:18:36.063147 pytest-homeassistant-custom-component-0.9.8/custom_components/simple_integration/
--rw-r--r--   0 runner    (1001) docker     (121)     1069 2022-05-31 05:18:23.000000 pytest-homeassistant-custom-component-0.9.8/custom_components/simple_integration/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     1024 2022-05-31 05:18:23.000000 pytest-homeassistant-custom-component-0.9.8/custom_components/simple_integration/config_flow.py
--rw-r--r--   0 runner    (1001) docker     (121)       87 2022-05-31 05:18:23.000000 pytest-homeassistant-custom-component-0.9.8/custom_components/simple_integration/const.py
--rw-r--r--   0 runner    (1001) docker     (121)      873 2022-05-31 05:18:23.000000 pytest-homeassistant-custom-component-0.9.8/custom_components/simple_integration/sensor.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-05-31 05:18:36.063147 pytest-homeassistant-custom-component-0.9.8/generate_phacc/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-05-31 05:18:23.000000 pytest-homeassistant-custom-component-0.9.8/generate_phacc/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)      760 2022-05-31 05:18:23.000000 pytest-homeassistant-custom-component-0.9.8/generate_phacc/const.py
--rwxr-xr-x   0 runner    (1001) docker     (121)     7339 2022-05-31 05:18:23.000000 pytest-homeassistant-custom-component-0.9.8/generate_phacc/generate_phacc.py
--rw-r--r--   0 runner    (1001) docker     (121)     2249 2022-05-31 05:18:23.000000 pytest-homeassistant-custom-component-0.9.8/generate_phacc/ha.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-05-31 05:18:36.063147 pytest-homeassistant-custom-component-0.9.8/pytest_homeassistant_custom_component/
--rw-r--r--   0 runner    (1001) docker     (121)      138 2022-05-31 05:18:23.000000 pytest-homeassistant-custom-component-0.9.8/pytest_homeassistant_custom_component/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    38761 2022-05-31 05:18:23.000000 pytest-homeassistant-custom-component-0.9.8/pytest_homeassistant_custom_component/common.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-05-31 05:18:36.063147 pytest-homeassistant-custom-component-0.9.8/pytest_homeassistant_custom_component/components/
--rw-r--r--   0 runner    (1001) docker     (121)      138 2022-05-31 05:18:23.000000 pytest-homeassistant-custom-component-0.9.8/pytest_homeassistant_custom_component/components/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-05-31 05:18:36.067147 pytest-homeassistant-custom-component-0.9.8/pytest_homeassistant_custom_component/components/recorder/
--rw-r--r--   0 runner    (1001) docker     (121)      142 2022-05-31 05:18:23.000000 pytest-homeassistant-custom-component-0.9.8/pytest_homeassistant_custom_component/components/recorder/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     4803 2022-05-31 05:18:23.000000 pytest-homeassistant-custom-component-0.9.8/pytest_homeassistant_custom_component/components/recorder/common.py
--rw-r--r--   0 runner    (1001) docker     (121)     5567 2022-05-31 05:18:23.000000 pytest-homeassistant-custom-component-0.9.8/pytest_homeassistant_custom_component/components/recorder/models_schema_0.py
--rw-r--r--   0 runner    (1001) docker     (121)      551 2022-05-31 05:18:23.000000 pytest-homeassistant-custom-component-0.9.8/pytest_homeassistant_custom_component/const.py
--rw-r--r--   0 runner    (1001) docker     (121)     1013 2022-05-31 05:18:23.000000 pytest-homeassistant-custom-component-0.9.8/pytest_homeassistant_custom_component/ignore_uncaught_exceptions.py
--rw-r--r--   0 runner    (1001) docker     (121)    23886 2022-05-31 05:18:23.000000 pytest-homeassistant-custom-component-0.9.8/pytest_homeassistant_custom_component/plugins.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-05-31 05:18:36.067147 pytest-homeassistant-custom-component-0.9.8/pytest_homeassistant_custom_component/test_util/
--rw-r--r--   0 runner    (1001) docker     (121)      142 2022-05-31 05:18:23.000000 pytest-homeassistant-custom-component-0.9.8/pytest_homeassistant_custom_component/test_util/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     9447 2022-05-31 05:18:23.000000 pytest-homeassistant-custom-component-0.9.8/pytest_homeassistant_custom_component/test_util/aiohttp.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-05-31 05:18:36.063147 pytest-homeassistant-custom-component-0.9.8/pytest_homeassistant_custom_component.egg-info/
--rw-r--r--   0 runner    (1001) docker     (121)      771 2022-05-31 05:18:36.000000 pytest-homeassistant-custom-component-0.9.8/pytest_homeassistant_custom_component.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (121)     1503 2022-05-31 05:18:36.000000 pytest-homeassistant-custom-component-0.9.8/pytest_homeassistant_custom_component.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (121)        1 2022-05-31 05:18:36.000000 pytest-homeassistant-custom-component-0.9.8/pytest_homeassistant_custom_component.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (121)       74 2022-05-31 05:18:36.000000 pytest-homeassistant-custom-component-0.9.8/pytest_homeassistant_custom_component.egg-info/entry_points.txt
--rw-r--r--   0 runner    (1001) docker     (121)      457 2022-05-31 05:18:36.000000 pytest-homeassistant-custom-component-0.9.8/pytest_homeassistant_custom_component.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (121)       77 2022-05-31 05:18:36.000000 pytest-homeassistant-custom-component-0.9.8/pytest_homeassistant_custom_component.egg-info/top_level.txt
--rw-r--r--   0 runner    (1001) docker     (121)       38 2022-05-31 05:18:36.067147 pytest-homeassistant-custom-component-0.9.8/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (121)     1233 2022-05-31 05:18:23.000000 pytest-homeassistant-custom-component-0.9.8/setup.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-05-31 05:18:36.067147 pytest-homeassistant-custom-component-0.9.8/tests/
--rw-r--r--   0 runner    (1001) docker     (121)       52 2022-05-31 05:18:23.000000 pytest-homeassistant-custom-component-0.9.8/tests/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)      154 2022-05-31 05:18:23.000000 pytest-homeassistant-custom-component-0.9.8/tests/conftest.py
--rw-r--r--   0 runner    (1001) docker     (121)      248 2022-05-31 05:18:23.000000 pytest-homeassistant-custom-component-0.9.8/tests/test_common.py
--rw-r--r--   0 runner    (1001) docker     (121)     1247 2022-05-31 05:18:23.000000 pytest-homeassistant-custom-component-0.9.8/tests/test_config_flow.py
--rw-r--r--   0 runner    (1001) docker     (121)      541 2022-05-31 05:18:23.000000 pytest-homeassistant-custom-component-0.9.8/tests/test_sensor.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-01 05:43:30.179567 pytest-homeassistant-custom-component-0.9.9/
+-rw-r--r--   0 runner    (1001) docker     (121)     1070 2022-06-01 05:43:18.000000 pytest-homeassistant-custom-component-0.9.9/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (121)    11357 2022-06-01 05:43:18.000000 pytest-homeassistant-custom-component-0.9.9/LICENSE_HA_CORE.md
+-rw-r--r--   0 runner    (1001) docker     (121)      771 2022-06-01 05:43:30.179567 pytest-homeassistant-custom-component-0.9.9/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (121)     2995 2022-06-01 05:43:18.000000 pytest-homeassistant-custom-component-0.9.9/README.md
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-01 05:43:30.175567 pytest-homeassistant-custom-component-0.9.9/custom_components/
+-rw-r--r--   0 runner    (1001) docker     (121)        0 2022-06-01 05:43:18.000000 pytest-homeassistant-custom-component-0.9.9/custom_components/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-01 05:43:30.179567 pytest-homeassistant-custom-component-0.9.9/custom_components/simple_integration/
+-rw-r--r--   0 runner    (1001) docker     (121)     1069 2022-06-01 05:43:18.000000 pytest-homeassistant-custom-component-0.9.9/custom_components/simple_integration/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1024 2022-06-01 05:43:18.000000 pytest-homeassistant-custom-component-0.9.9/custom_components/simple_integration/config_flow.py
+-rw-r--r--   0 runner    (1001) docker     (121)       87 2022-06-01 05:43:18.000000 pytest-homeassistant-custom-component-0.9.9/custom_components/simple_integration/const.py
+-rw-r--r--   0 runner    (1001) docker     (121)      873 2022-06-01 05:43:18.000000 pytest-homeassistant-custom-component-0.9.9/custom_components/simple_integration/sensor.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-01 05:43:30.179567 pytest-homeassistant-custom-component-0.9.9/generate_phacc/
+-rw-r--r--   0 runner    (1001) docker     (121)        0 2022-06-01 05:43:18.000000 pytest-homeassistant-custom-component-0.9.9/generate_phacc/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)      760 2022-06-01 05:43:18.000000 pytest-homeassistant-custom-component-0.9.9/generate_phacc/const.py
+-rwxr-xr-x   0 runner    (1001) docker     (121)     7339 2022-06-01 05:43:18.000000 pytest-homeassistant-custom-component-0.9.9/generate_phacc/generate_phacc.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2249 2022-06-01 05:43:18.000000 pytest-homeassistant-custom-component-0.9.9/generate_phacc/ha.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-01 05:43:30.179567 pytest-homeassistant-custom-component-0.9.9/pytest_homeassistant_custom_component/
+-rw-r--r--   0 runner    (1001) docker     (121)      138 2022-06-01 05:43:18.000000 pytest-homeassistant-custom-component-0.9.9/pytest_homeassistant_custom_component/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    38761 2022-06-01 05:43:18.000000 pytest-homeassistant-custom-component-0.9.9/pytest_homeassistant_custom_component/common.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-01 05:43:30.179567 pytest-homeassistant-custom-component-0.9.9/pytest_homeassistant_custom_component/components/
+-rw-r--r--   0 runner    (1001) docker     (121)      138 2022-06-01 05:43:18.000000 pytest-homeassistant-custom-component-0.9.9/pytest_homeassistant_custom_component/components/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-01 05:43:30.179567 pytest-homeassistant-custom-component-0.9.9/pytest_homeassistant_custom_component/components/recorder/
+-rw-r--r--   0 runner    (1001) docker     (121)      142 2022-06-01 05:43:18.000000 pytest-homeassistant-custom-component-0.9.9/pytest_homeassistant_custom_component/components/recorder/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     4803 2022-06-01 05:43:18.000000 pytest-homeassistant-custom-component-0.9.9/pytest_homeassistant_custom_component/components/recorder/common.py
+-rw-r--r--   0 runner    (1001) docker     (121)     5567 2022-06-01 05:43:18.000000 pytest-homeassistant-custom-component-0.9.9/pytest_homeassistant_custom_component/components/recorder/models_schema_0.py
+-rw-r--r--   0 runner    (1001) docker     (121)      551 2022-06-01 05:43:18.000000 pytest-homeassistant-custom-component-0.9.9/pytest_homeassistant_custom_component/const.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1013 2022-06-01 05:43:18.000000 pytest-homeassistant-custom-component-0.9.9/pytest_homeassistant_custom_component/ignore_uncaught_exceptions.py
+-rw-r--r--   0 runner    (1001) docker     (121)    23886 2022-06-01 05:43:18.000000 pytest-homeassistant-custom-component-0.9.9/pytest_homeassistant_custom_component/plugins.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-01 05:43:30.179567 pytest-homeassistant-custom-component-0.9.9/pytest_homeassistant_custom_component/test_util/
+-rw-r--r--   0 runner    (1001) docker     (121)      142 2022-06-01 05:43:18.000000 pytest-homeassistant-custom-component-0.9.9/pytest_homeassistant_custom_component/test_util/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     9447 2022-06-01 05:43:18.000000 pytest-homeassistant-custom-component-0.9.9/pytest_homeassistant_custom_component/test_util/aiohttp.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-01 05:43:30.179567 pytest-homeassistant-custom-component-0.9.9/pytest_homeassistant_custom_component.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (121)      771 2022-06-01 05:43:30.000000 pytest-homeassistant-custom-component-0.9.9/pytest_homeassistant_custom_component.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (121)     1503 2022-06-01 05:43:30.000000 pytest-homeassistant-custom-component-0.9.9/pytest_homeassistant_custom_component.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (121)        1 2022-06-01 05:43:30.000000 pytest-homeassistant-custom-component-0.9.9/pytest_homeassistant_custom_component.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (121)       74 2022-06-01 05:43:30.000000 pytest-homeassistant-custom-component-0.9.9/pytest_homeassistant_custom_component.egg-info/entry_points.txt
+-rw-r--r--   0 runner    (1001) docker     (121)      457 2022-06-01 05:43:30.000000 pytest-homeassistant-custom-component-0.9.9/pytest_homeassistant_custom_component.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (121)       77 2022-06-01 05:43:30.000000 pytest-homeassistant-custom-component-0.9.9/pytest_homeassistant_custom_component.egg-info/top_level.txt
+-rw-r--r--   0 runner    (1001) docker     (121)       38 2022-06-01 05:43:30.179567 pytest-homeassistant-custom-component-0.9.9/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (121)     1233 2022-06-01 05:43:18.000000 pytest-homeassistant-custom-component-0.9.9/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-01 05:43:30.179567 pytest-homeassistant-custom-component-0.9.9/tests/
+-rw-r--r--   0 runner    (1001) docker     (121)       52 2022-06-01 05:43:19.000000 pytest-homeassistant-custom-component-0.9.9/tests/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)      154 2022-06-01 05:43:19.000000 pytest-homeassistant-custom-component-0.9.9/tests/conftest.py
+-rw-r--r--   0 runner    (1001) docker     (121)      248 2022-06-01 05:43:19.000000 pytest-homeassistant-custom-component-0.9.9/tests/test_common.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1247 2022-06-01 05:43:19.000000 pytest-homeassistant-custom-component-0.9.9/tests/test_config_flow.py
+-rw-r--r--   0 runner    (1001) docker     (121)      541 2022-06-01 05:43:19.000000 pytest-homeassistant-custom-component-0.9.9/tests/test_sensor.py
```

### Comparing `pytest-homeassistant-custom-component-0.9.8/LICENSE` & `pytest-homeassistant-custom-component-0.9.9/LICENSE`

 * *Files identical despite different names*

### Comparing `pytest-homeassistant-custom-component-0.9.8/LICENSE_HA_CORE.md` & `pytest-homeassistant-custom-component-0.9.9/LICENSE_HA_CORE.md`

 * *Files identical despite different names*

### Comparing `pytest-homeassistant-custom-component-0.9.8/PKG-INFO` & `pytest-homeassistant-custom-component-0.9.9/PKG-INFO`

 * *Files 16% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: pytest-homeassistant-custom-component
-Version: 0.9.8
+Version: 0.9.9
 Summary: Experimental package to automatically extract test plugins for Home Assistant custom components
 Home-page: https://github.com/MatthewFlamm/pytest-homeassistant-custom-component
 Author: Matthew Flamm
 Author-email: matthewflamm0@gmail.com
 License: MIT license
 Platform: UNKNOWN
 Classifier: Development Status :: 3 - Alpha
```

### Comparing `pytest-homeassistant-custom-component-0.9.8/README.md` & `pytest-homeassistant-custom-component-0.9.9/README.md`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 # pytest-homeassistant-custom-component
 
-![HA core version](https://img.shields.io/static/v1?label=HA+core+version&message=2022.6.0b4&labelColor=blue)
+![HA core version](https://img.shields.io/static/v1?label=HA+core+version&message=2022.6.0b7&labelColor=blue)
 
 Package to automatically extract testing plugins from Home Assistant for custom component testing.
 The goal is to provide the same functionality as the tests in home-assistant/core.
 pytest-homeassistant-custom-component is updated daily according to the latest homeassistant release including beta.
 
 ## Usage:
 * All pytest fixtures can be used as normal, like `hass`
```

### Comparing `pytest-homeassistant-custom-component-0.9.8/custom_components/simple_integration/__init__.py` & `pytest-homeassistant-custom-component-0.9.9/custom_components/simple_integration/__init__.py`

 * *Files identical despite different names*

### Comparing `pytest-homeassistant-custom-component-0.9.8/custom_components/simple_integration/config_flow.py` & `pytest-homeassistant-custom-component-0.9.9/custom_components/simple_integration/config_flow.py`

 * *Files identical despite different names*

### Comparing `pytest-homeassistant-custom-component-0.9.8/custom_components/simple_integration/sensor.py` & `pytest-homeassistant-custom-component-0.9.9/custom_components/simple_integration/sensor.py`

 * *Files identical despite different names*

### Comparing `pytest-homeassistant-custom-component-0.9.8/generate_phacc/const.py` & `pytest-homeassistant-custom-component-0.9.9/generate_phacc/const.py`

 * *Files identical despite different names*

### Comparing `pytest-homeassistant-custom-component-0.9.8/generate_phacc/generate_phacc.py` & `pytest-homeassistant-custom-component-0.9.9/generate_phacc/generate_phacc.py`

 * *Files identical despite different names*

### Comparing `pytest-homeassistant-custom-component-0.9.8/generate_phacc/ha.py` & `pytest-homeassistant-custom-component-0.9.9/generate_phacc/ha.py`

 * *Files identical despite different names*

### Comparing `pytest-homeassistant-custom-component-0.9.8/pytest_homeassistant_custom_component/common.py` & `pytest-homeassistant-custom-component-0.9.9/pytest_homeassistant_custom_component/common.py`

 * *Files identical despite different names*

### Comparing `pytest-homeassistant-custom-component-0.9.8/pytest_homeassistant_custom_component/components/recorder/common.py` & `pytest-homeassistant-custom-component-0.9.9/pytest_homeassistant_custom_component/components/recorder/common.py`

 * *Files identical despite different names*

### Comparing `pytest-homeassistant-custom-component-0.9.8/pytest_homeassistant_custom_component/components/recorder/models_schema_0.py` & `pytest-homeassistant-custom-component-0.9.9/pytest_homeassistant_custom_component/components/recorder/models_schema_0.py`

 * *Files identical despite different names*

### Comparing `pytest-homeassistant-custom-component-0.9.8/pytest_homeassistant_custom_component/const.py` & `pytest-homeassistant-custom-component-0.9.9/pytest_homeassistant_custom_component/const.py`

 * *Files 1% similar despite different names*

```diff
@@ -6,12 +6,12 @@
 from __future__ import annotations
 
 from typing import Final
 
 
 MAJOR_VERSION: Final = 2022
 MINOR_VERSION: Final = 6
-PATCH_VERSION: Final = "0b4"
+PATCH_VERSION: Final = "0b7"
 __short_version__: Final = f"{MAJOR_VERSION}.{MINOR_VERSION}"
 __version__: Final = f"{__short_version__}.{PATCH_VERSION}"
 REQUIRED_PYTHON_VER: Final[tuple[int, int, int]] = (3, 9, 0)
 REQUIRED_NEXT_PYTHON_VER: Final[tuple[int, int, int]] = (3, 9, 0)
```

### Comparing `pytest-homeassistant-custom-component-0.9.8/pytest_homeassistant_custom_component/ignore_uncaught_exceptions.py` & `pytest-homeassistant-custom-component-0.9.9/pytest_homeassistant_custom_component/ignore_uncaught_exceptions.py`

 * *Files identical despite different names*

### Comparing `pytest-homeassistant-custom-component-0.9.8/pytest_homeassistant_custom_component/plugins.py` & `pytest-homeassistant-custom-component-0.9.9/pytest_homeassistant_custom_component/plugins.py`

 * *Files identical despite different names*

### Comparing `pytest-homeassistant-custom-component-0.9.8/pytest_homeassistant_custom_component/test_util/aiohttp.py` & `pytest-homeassistant-custom-component-0.9.9/pytest_homeassistant_custom_component/test_util/aiohttp.py`

 * *Files identical despite different names*

### Comparing `pytest-homeassistant-custom-component-0.9.8/pytest_homeassistant_custom_component.egg-info/PKG-INFO` & `pytest-homeassistant-custom-component-0.9.9/pytest_homeassistant_custom_component.egg-info/PKG-INFO`

 * *Files 16% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: pytest-homeassistant-custom-component
-Version: 0.9.8
+Version: 0.9.9
 Summary: Experimental package to automatically extract test plugins for Home Assistant custom components
 Home-page: https://github.com/MatthewFlamm/pytest-homeassistant-custom-component
 Author: Matthew Flamm
 Author-email: matthewflamm0@gmail.com
 License: MIT license
 Platform: UNKNOWN
 Classifier: Development Status :: 3 - Alpha
```

### Comparing `pytest-homeassistant-custom-component-0.9.8/pytest_homeassistant_custom_component.egg-info/SOURCES.txt` & `pytest-homeassistant-custom-component-0.9.9/pytest_homeassistant_custom_component.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `pytest-homeassistant-custom-component-0.9.8/setup.py` & `pytest-homeassistant-custom-component-0.9.9/setup.py`

 * *Files identical despite different names*

### Comparing `pytest-homeassistant-custom-component-0.9.8/tests/test_config_flow.py` & `pytest-homeassistant-custom-component-0.9.9/tests/test_config_flow.py`

 * *Files identical despite different names*

### Comparing `pytest-homeassistant-custom-component-0.9.8/tests/test_sensor.py` & `pytest-homeassistant-custom-component-0.9.9/tests/test_sensor.py`

 * *Files identical despite different names*

