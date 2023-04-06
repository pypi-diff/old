# Comparing `tmp/sag-py-logging-0.1.0.tar.gz` & `tmp/sag-py-logging-0.2.0.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "sag-py-logging-0.1.0.tar", last modified: Mon Apr  3 09:33:56 2023, max compression
+gzip compressed data, was "sag-py-logging-0.2.0.tar", last modified: Thu Apr  6 12:01:24 2023, max compression
```

## Comparing `sag-py-logging-0.1.0.tar` & `sag-py-logging-0.2.0.tar`

### file list

```diff
@@ -1,22 +1,22 @@
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-03 09:33:56.648773 sag-py-logging-0.1.0/
--rw-r--r--   0 runner    (1001) docker     (123)     1069 2023-04-03 09:33:45.000000 sag-py-logging-0.1.0/LICENSE.txt
--rw-r--r--   0 runner    (1001) docker     (123)     4029 2023-04-03 09:33:56.648773 sag-py-logging-0.1.0/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)     3114 2023-04-03 09:33:45.000000 sag-py-logging-0.1.0/README.md
--rw-r--r--   0 runner    (1001) docker     (123)       86 2023-04-03 09:33:45.000000 sag-py-logging-0.1.0/pyproject.toml
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-03 09:33:56.648773 sag-py-logging-0.1.0/sag_py_logging/
--rw-r--r--   0 runner    (1001) docker     (123)      189 2023-04-03 09:33:45.000000 sag-py-logging-0.1.0/sag_py_logging/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     1575 2023-04-03 09:33:45.000000 sag-py-logging-0.1.0/sag_py_logging/console_extra_field_filter.py
--rw-r--r--   0 runner    (1001) docker     (123)      894 2023-04-03 09:33:45.000000 sag-py-logging-0.1.0/sag_py_logging/log_config_initializer.py
--rw-r--r--   0 runner    (1001) docker     (123)       98 2023-04-03 09:33:45.000000 sag-py-logging-0.1.0/sag_py_logging/models.py
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-03 09:33:45.000000 sag-py-logging-0.1.0/sag_py_logging/py.typed
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-03 09:33:56.648773 sag-py-logging-0.1.0/sag_py_logging.egg-info/
--rw-r--r--   0 runner    (1001) docker     (123)     4029 2023-04-03 09:33:56.000000 sag-py-logging-0.1.0/sag_py_logging.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)      484 2023-04-03 09:33:56.000000 sag-py-logging-0.1.0/sag_py_logging.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-03 09:33:56.000000 sag-py-logging-0.1.0/sag_py_logging.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (123)       14 2023-04-03 09:33:56.000000 sag-py-logging-0.1.0/sag_py_logging.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (123)       15 2023-04-03 09:33:56.000000 sag-py-logging-0.1.0/sag_py_logging.egg-info/top_level.txt
--rw-r--r--   0 runner    (1001) docker     (123)       78 2023-04-03 09:33:56.648773 sag-py-logging-0.1.0/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (123)     1358 2023-04-03 09:33:45.000000 sag-py-logging-0.1.0/setup.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-03 09:33:56.648773 sag-py-logging-0.1.0/tests/
--rw-r--r--   0 runner    (1001) docker     (123)     1059 2023-04-03 09:33:45.000000 sag-py-logging-0.1.0/tests/test_console_extra_field_filter.py
--rw-r--r--   0 runner    (1001) docker     (123)     1387 2023-04-03 09:33:45.000000 sag-py-logging-0.1.0/tests/test_log_config_initializer.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 12:01:24.171465 sag-py-logging-0.2.0/
+-rw-r--r--   0 runner    (1001) docker     (123)     1069 2023-04-06 12:01:13.000000 sag-py-logging-0.2.0/LICENSE.txt
+-rw-r--r--   0 runner    (1001) docker     (123)     4121 2023-04-06 12:01:24.171465 sag-py-logging-0.2.0/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     3206 2023-04-06 12:01:13.000000 sag-py-logging-0.2.0/README.md
+-rw-r--r--   0 runner    (1001) docker     (123)       86 2023-04-06 12:01:13.000000 sag-py-logging-0.2.0/pyproject.toml
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 12:01:24.171465 sag-py-logging-0.2.0/sag_py_logging/
+-rw-r--r--   0 runner    (1001) docker     (123)      189 2023-04-06 12:01:13.000000 sag-py-logging-0.2.0/sag_py_logging/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1575 2023-04-06 12:01:13.000000 sag-py-logging-0.2.0/sag_py_logging/console_extra_field_filter.py
+-rw-r--r--   0 runner    (1001) docker     (123)      941 2023-04-06 12:01:13.000000 sag-py-logging-0.2.0/sag_py_logging/log_config_initializer.py
+-rw-r--r--   0 runner    (1001) docker     (123)       98 2023-04-06 12:01:13.000000 sag-py-logging-0.2.0/sag_py_logging/models.py
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 12:01:13.000000 sag-py-logging-0.2.0/sag_py_logging/py.typed
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 12:01:24.171465 sag-py-logging-0.2.0/sag_py_logging.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)     4121 2023-04-06 12:01:24.000000 sag-py-logging-0.2.0/sag_py_logging.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)      484 2023-04-06 12:01:24.000000 sag-py-logging-0.2.0/sag_py_logging.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-06 12:01:24.000000 sag-py-logging-0.2.0/sag_py_logging.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       14 2023-04-06 12:01:24.000000 sag-py-logging-0.2.0/sag_py_logging.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       15 2023-04-06 12:01:24.000000 sag-py-logging-0.2.0/sag_py_logging.egg-info/top_level.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       78 2023-04-06 12:01:24.171465 sag-py-logging-0.2.0/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (123)     1358 2023-04-06 12:01:13.000000 sag-py-logging-0.2.0/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 12:01:24.171465 sag-py-logging-0.2.0/tests/
+-rw-r--r--   0 runner    (1001) docker     (123)     1059 2023-04-06 12:01:13.000000 sag-py-logging-0.2.0/tests/test_console_extra_field_filter.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1387 2023-04-06 12:01:13.000000 sag-py-logging-0.2.0/tests/test_log_config_initializer.py
```

### Comparing `sag-py-logging-0.1.0/LICENSE.txt` & `sag-py-logging-0.2.0/LICENSE.txt`

 * *Files identical despite different names*

### Comparing `sag-py-logging-0.1.0/PKG-INFO` & `sag-py-logging-0.2.0/PKG-INFO`

 * *Files 3% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: sag-py-logging
-Version: 0.1.0
+Version: 0.2.0
 Summary: Initialize logging from a configuration json
 Home-page: https://github.com/SamhammerAG/sag_py_logging
 Author: Samhammer AG
 Author-email: support@samhammer.de
 License: MIT
 Project-URL: Documentation, https://github.com/SamhammerAG/sag_py_logging
 Project-URL: Bug Reports, https://github.com/SamhammerAG/sag_py_logging/issues
@@ -40,28 +40,30 @@
 * Placeholder support for the config json
 * A log filter to log extra fields
 
 ## How to use
 
 ### Installation
 
-pip install sag_py_logging
+pip install sag-py-logging
 
 ### Initialize logging from json
 
 Add the following as early as possible to your application code:
 
 ```python
 from sag_py_logging.log_config_initializer import init_logging
 
 placeholder_container = { "host": "myhost.com", ...}
 
 init_logging("./log_config.json", config.logging_config)
 ```
 
+Init logging returns the log configuration as dictionary if needed for further processing.
+
 ### The json configuration
 
 ```json
 {
     "version": 1,
     "disable_existing_loggers": "true",
     "root": {
```

### Comparing `sag-py-logging-0.1.0/README.md` & `sag-py-logging-0.2.0/README.md`

 * *Files 4% similar despite different names*

```diff
@@ -17,28 +17,30 @@
 * Placeholder support for the config json
 * A log filter to log extra fields
 
 ## How to use
 
 ### Installation
 
-pip install sag_py_logging
+pip install sag-py-logging
 
 ### Initialize logging from json
 
 Add the following as early as possible to your application code:
 
 ```python
 from sag_py_logging.log_config_initializer import init_logging
 
 placeholder_container = { "host": "myhost.com", ...}
 
 init_logging("./log_config.json", config.logging_config)
 ```
 
+Init logging returns the log configuration as dictionary if needed for further processing.
+
 ### The json configuration
 
 ```json
 {
     "version": 1,
     "disable_existing_loggers": "true",
     "root": {
```

### Comparing `sag-py-logging-0.1.0/sag_py_logging/console_extra_field_filter.py` & `sag-py-logging-0.2.0/sag_py_logging/console_extra_field_filter.py`

 * *Files identical despite different names*

### Comparing `sag-py-logging-0.1.0/sag_py_logging/log_config_initializer.py` & `sag-py-logging-0.2.0/sag_py_logging/log_config_initializer.py`

 * *Files 16% similar despite different names*

```diff
@@ -1,19 +1,22 @@
 import json
 import logging
 import logging.config
 from string import Template
 from typing import Any, Dict, Mapping
 
 
-def init_logging(config_file: str, placeholder_container: Mapping[str, object], encoding: str = "UTF-8") -> None:
+def init_logging(
+    config_file: str, placeholder_container: Mapping[str, object], encoding: str = "UTF-8"
+) -> Dict[str, Any]:
     with open(config_file, "r", encoding=encoding) as log_config_reader:
         log_template: str = log_config_reader.read()
         log_config_dict: Dict[str, Any] = _template_to_parsed_json(log_template, placeholder_container)
         _init_python_logging(log_config_dict)
+        return log_config_dict
 
 
 def _template_to_parsed_json(log_template: str, placeholder_container: Mapping[str, object]) -> Dict[str, Any]:
     parsed_log_templage: str = Template(log_template).substitute(placeholder_container)
     return json.loads(parsed_log_templage)
```

### Comparing `sag-py-logging-0.1.0/sag_py_logging.egg-info/PKG-INFO` & `sag-py-logging-0.2.0/sag_py_logging.egg-info/PKG-INFO`

 * *Files 3% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: sag-py-logging
-Version: 0.1.0
+Version: 0.2.0
 Summary: Initialize logging from a configuration json
 Home-page: https://github.com/SamhammerAG/sag_py_logging
 Author: Samhammer AG
 Author-email: support@samhammer.de
 License: MIT
 Project-URL: Documentation, https://github.com/SamhammerAG/sag_py_logging
 Project-URL: Bug Reports, https://github.com/SamhammerAG/sag_py_logging/issues
@@ -40,28 +40,30 @@
 * Placeholder support for the config json
 * A log filter to log extra fields
 
 ## How to use
 
 ### Installation
 
-pip install sag_py_logging
+pip install sag-py-logging
 
 ### Initialize logging from json
 
 Add the following as early as possible to your application code:
 
 ```python
 from sag_py_logging.log_config_initializer import init_logging
 
 placeholder_container = { "host": "myhost.com", ...}
 
 init_logging("./log_config.json", config.logging_config)
 ```
 
+Init logging returns the log configuration as dictionary if needed for further processing.
+
 ### The json configuration
 
 ```json
 {
     "version": 1,
     "disable_existing_loggers": "true",
     "root": {
```

### Comparing `sag-py-logging-0.1.0/setup.py` & `sag-py-logging-0.2.0/setup.py`

 * *Files 1% similar despite different names*

```diff
@@ -4,15 +4,15 @@
     LONG_DESCRIPTION = fh.read()
 
 with open("requirements.txt", "r") as fin:
     REQS = fin.read().splitlines()
 
 setuptools.setup(
     name="sag-py-logging",
-    version="0.1.0",
+    version="0.2.0",
     description="Initialize logging from a configuration json",
     long_description=LONG_DESCRIPTION,
     long_description_content_type="text/markdown",
     url="https://github.com/SamhammerAG/sag_py_logging",
     author="Samhammer AG",
     author_email="support@samhammer.de",
     license="MIT",
```

### Comparing `sag-py-logging-0.1.0/tests/test_console_extra_field_filter.py` & `sag-py-logging-0.2.0/tests/test_console_extra_field_filter.py`

 * *Files identical despite different names*

### Comparing `sag-py-logging-0.1.0/tests/test_log_config_initializer.py` & `sag-py-logging-0.2.0/tests/test_log_config_initializer.py`

 * *Files identical despite different names*

