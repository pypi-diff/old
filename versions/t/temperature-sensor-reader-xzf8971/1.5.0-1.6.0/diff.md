# Comparing `tmp/temperature_sensor_reader_xzf8971-1.5.0.tar.gz` & `tmp/temperature_sensor_reader_xzf8971-1.6.0.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "temperature_sensor_reader_xzf8971-1.5.0.tar", last modified: Fri Apr  7 03:40:10 2023, max compression
+gzip compressed data, was "temperature_sensor_reader_xzf8971-1.6.0.tar", last modified: Fri Apr  7 03:43:40 2023, max compression
```

## Comparing `temperature_sensor_reader_xzf8971-1.5.0.tar` & `temperature_sensor_reader_xzf8971-1.6.0.tar`

### file list

```diff
@@ -1,37 +1,37 @@
-drwxrwxr-x   0 user      (1000) user      (1000)        0 2023-04-07 03:40:10.755582 temperature_sensor_reader_xzf8971-1.5.0/
--rw-rw-r--   0 user      (1000) user      (1000)     1805 2022-12-02 08:19:39.000000 temperature_sensor_reader_xzf8971-1.5.0/.gitignore
--rw-rw-r--   0 user      (1000) user      (1000)      102 2022-11-11 06:17:47.000000 temperature_sensor_reader_xzf8971-1.5.0/.gitmodules
--rw-rw-r--   0 user      (1000) user      (1000)     1067 2022-10-31 02:56:10.000000 temperature_sensor_reader_xzf8971-1.5.0/LICENSE
--rw-rw-r--   0 user      (1000) user      (1000)     3138 2023-04-07 03:40:10.754582 temperature_sensor_reader_xzf8971-1.5.0/PKG-INFO
--rw-rw-r--   0 user      (1000) user      (1000)     2540 2022-11-17 06:34:54.000000 temperature_sensor_reader_xzf8971-1.5.0/README.md
--rw-rw-r--   0 user      (1000) user      (1000)      106 2022-12-02 08:19:39.000000 temperature_sensor_reader_xzf8971-1.5.0/__init__.py
--rw-rw-r--   0 user      (1000) user      (1000)       64 2022-11-14 03:16:03.000000 temperature_sensor_reader_xzf8971-1.5.0/build_and_install_locally.sh
--rw-rw-r--   0 user      (1000) user      (1000)      121 2022-11-14 03:13:15.000000 temperature_sensor_reader_xzf8971-1.5.0/build_and_upload.sh
-drwxrwxr-x   0 user      (1000) user      (1000)        0 2023-04-07 03:40:10.745582 temperature_sensor_reader_xzf8971-1.5.0/examples/
--rw-rw-r--   0 user      (1000) user      (1000)      552 2022-12-02 08:19:39.000000 temperature_sensor_reader_xzf8971-1.5.0/examples/JDRK_data_analysis.py
--rw-rw-r--   0 user      (1000) user      (1000)     2139 2022-11-11 06:37:07.000000 temperature_sensor_reader_xzf8971-1.5.0/examples/JDRK_sensor.py
-drwxrwxr-x   0 user      (1000) user      (1000)        0 2023-04-07 03:40:10.747582 temperature_sensor_reader_xzf8971-1.5.0/graphtec_reader/
--rw-rw-r--   0 user      (1000) user      (1000)       30 2022-11-11 06:17:47.000000 temperature_sensor_reader_xzf8971-1.5.0/graphtec_reader/__init__.py
--rw-rw-r--   0 user      (1000) user      (1000)      939 2022-11-11 06:17:47.000000 temperature_sensor_reader_xzf8971-1.5.0/graphtec_reader/__main__.py
--rw-rw-r--   0 user      (1000) user      (1000)     6451 2023-04-07 03:30:03.000000 temperature_sensor_reader_xzf8971-1.5.0/graphtec_reader/helper_function.py
-drwxrwxr-x   0 user      (1000) user      (1000)        0 2023-04-07 03:40:10.751582 temperature_sensor_reader_xzf8971-1.5.0/modbus_configuretools/
--rw-rw-r--   0 user      (1000) user      (1000)      132 2022-10-31 02:56:10.000000 temperature_sensor_reader_xzf8971-1.5.0/modbus_configuretools/__init__.py
--rw-rw-r--   0 user      (1000) user      (1000)     2438 2022-11-14 03:35:17.000000 temperature_sensor_reader_xzf8971-1.5.0/modbus_configuretools/derived_modbus_wrapper.py
--rw-rw-r--   0 user      (1000) user      (1000)     3547 2022-11-14 03:28:25.000000 temperature_sensor_reader_xzf8971-1.5.0/modbus_configuretools/helper_function.py
--rw-rw-r--   0 user      (1000) user      (1000)     1279 2022-10-31 02:56:10.000000 temperature_sensor_reader_xzf8971-1.5.0/modbus_configuretools/modbus_wrapper.py
--rw-rw-r--   0 user      (1000) user      (1000)     7852 2022-11-14 03:44:06.000000 temperature_sensor_reader_xzf8971-1.5.0/modbus_configuretools/temperature_sensor.py
--rw-rw-r--   0 user      (1000) user      (1000)      820 2023-04-07 03:39:34.000000 temperature_sensor_reader_xzf8971-1.5.0/pyproject.toml
--rw-rw-r--   0 user      (1000) user      (1000)       38 2023-04-07 03:40:10.755582 temperature_sensor_reader_xzf8971-1.5.0/setup.cfg
--rw-rw-r--   0 user      (1000) user      (1000)      128 2022-11-11 06:28:45.000000 temperature_sensor_reader_xzf8971-1.5.0/setup.py
-drwxrwxr-x   0 user      (1000) user      (1000)        0 2023-04-07 03:40:10.752582 temperature_sensor_reader_xzf8971-1.5.0/temperature_data_analysis/
--rw-rw-r--   0 user      (1000) user      (1000)       83 2022-12-02 08:19:39.000000 temperature_sensor_reader_xzf8971-1.5.0/temperature_data_analysis/__init__.py
--rw-rw-r--   0 user      (1000) user      (1000)     3448 2022-12-02 08:19:39.000000 temperature_sensor_reader_xzf8971-1.5.0/temperature_data_analysis/data_wrapper.py
--rw-rw-r--   0 user      (1000) user      (1000)        0 2022-12-02 08:19:39.000000 temperature_sensor_reader_xzf8971-1.5.0/temperature_data_analysis/helper_function.py
--rw-rw-r--   0 user      (1000) user      (1000)     1813 2023-04-07 03:30:03.000000 temperature_sensor_reader_xzf8971-1.5.0/temperature_data_analysis/plot_wrapper.py
-drwxrwxr-x   0 user      (1000) user      (1000)        0 2023-04-07 03:40:10.754582 temperature_sensor_reader_xzf8971-1.5.0/temperature_sensor_reader_xzf8971.egg-info/
--rw-rw-r--   0 user      (1000) user      (1000)     3138 2023-04-07 03:40:10.000000 temperature_sensor_reader_xzf8971-1.5.0/temperature_sensor_reader_xzf8971.egg-info/PKG-INFO
--rw-rw-r--   0 user      (1000) user      (1000)      985 2023-04-07 03:40:10.000000 temperature_sensor_reader_xzf8971-1.5.0/temperature_sensor_reader_xzf8971.egg-info/SOURCES.txt
--rw-rw-r--   0 user      (1000) user      (1000)        1 2023-04-07 03:40:10.000000 temperature_sensor_reader_xzf8971-1.5.0/temperature_sensor_reader_xzf8971.egg-info/dependency_links.txt
--rw-rw-r--   0 user      (1000) user      (1000)        1 2022-11-17 06:29:21.000000 temperature_sensor_reader_xzf8971-1.5.0/temperature_sensor_reader_xzf8971.egg-info/not-zip-safe
--rw-rw-r--   0 user      (1000) user      (1000)       74 2023-04-07 03:40:10.000000 temperature_sensor_reader_xzf8971-1.5.0/temperature_sensor_reader_xzf8971.egg-info/requires.txt
--rw-rw-r--   0 user      (1000) user      (1000)       64 2023-04-07 03:40:10.000000 temperature_sensor_reader_xzf8971-1.5.0/temperature_sensor_reader_xzf8971.egg-info/top_level.txt
+drwxrwxr-x   0 user      (1000) user      (1000)        0 2023-04-07 03:43:40.687587 temperature_sensor_reader_xzf8971-1.6.0/
+-rw-rw-r--   0 user      (1000) user      (1000)     1805 2022-12-02 08:19:39.000000 temperature_sensor_reader_xzf8971-1.6.0/.gitignore
+-rw-rw-r--   0 user      (1000) user      (1000)      102 2022-11-11 06:17:47.000000 temperature_sensor_reader_xzf8971-1.6.0/.gitmodules
+-rw-rw-r--   0 user      (1000) user      (1000)     1067 2022-10-31 02:56:10.000000 temperature_sensor_reader_xzf8971-1.6.0/LICENSE
+-rw-rw-r--   0 user      (1000) user      (1000)     3138 2023-04-07 03:43:40.687587 temperature_sensor_reader_xzf8971-1.6.0/PKG-INFO
+-rw-rw-r--   0 user      (1000) user      (1000)     2540 2022-11-17 06:34:54.000000 temperature_sensor_reader_xzf8971-1.6.0/README.md
+-rw-rw-r--   0 user      (1000) user      (1000)      106 2022-12-02 08:19:39.000000 temperature_sensor_reader_xzf8971-1.6.0/__init__.py
+-rw-rw-r--   0 user      (1000) user      (1000)       64 2022-11-14 03:16:03.000000 temperature_sensor_reader_xzf8971-1.6.0/build_and_install_locally.sh
+-rw-rw-r--   0 user      (1000) user      (1000)      121 2022-11-14 03:13:15.000000 temperature_sensor_reader_xzf8971-1.6.0/build_and_upload.sh
+drwxrwxr-x   0 user      (1000) user      (1000)        0 2023-04-07 03:43:40.678587 temperature_sensor_reader_xzf8971-1.6.0/examples/
+-rw-rw-r--   0 user      (1000) user      (1000)      552 2022-12-02 08:19:39.000000 temperature_sensor_reader_xzf8971-1.6.0/examples/JDRK_data_analysis.py
+-rw-rw-r--   0 user      (1000) user      (1000)     2139 2022-11-11 06:37:07.000000 temperature_sensor_reader_xzf8971-1.6.0/examples/JDRK_sensor.py
+drwxrwxr-x   0 user      (1000) user      (1000)        0 2023-04-07 03:43:40.679587 temperature_sensor_reader_xzf8971-1.6.0/graphtec_reader/
+-rw-rw-r--   0 user      (1000) user      (1000)       30 2022-11-11 06:17:47.000000 temperature_sensor_reader_xzf8971-1.6.0/graphtec_reader/__init__.py
+-rw-rw-r--   0 user      (1000) user      (1000)      939 2022-11-11 06:17:47.000000 temperature_sensor_reader_xzf8971-1.6.0/graphtec_reader/__main__.py
+-rw-rw-r--   0 user      (1000) user      (1000)     6451 2023-04-07 03:30:03.000000 temperature_sensor_reader_xzf8971-1.6.0/graphtec_reader/helper_function.py
+drwxrwxr-x   0 user      (1000) user      (1000)        0 2023-04-07 03:43:40.681587 temperature_sensor_reader_xzf8971-1.6.0/modbus_configuretools/
+-rw-rw-r--   0 user      (1000) user      (1000)      132 2022-10-31 02:56:10.000000 temperature_sensor_reader_xzf8971-1.6.0/modbus_configuretools/__init__.py
+-rw-rw-r--   0 user      (1000) user      (1000)     2438 2022-11-14 03:35:17.000000 temperature_sensor_reader_xzf8971-1.6.0/modbus_configuretools/derived_modbus_wrapper.py
+-rw-rw-r--   0 user      (1000) user      (1000)     3547 2022-11-14 03:28:25.000000 temperature_sensor_reader_xzf8971-1.6.0/modbus_configuretools/helper_function.py
+-rw-rw-r--   0 user      (1000) user      (1000)     1279 2022-10-31 02:56:10.000000 temperature_sensor_reader_xzf8971-1.6.0/modbus_configuretools/modbus_wrapper.py
+-rw-rw-r--   0 user      (1000) user      (1000)     7852 2022-11-14 03:44:06.000000 temperature_sensor_reader_xzf8971-1.6.0/modbus_configuretools/temperature_sensor.py
+-rw-rw-r--   0 user      (1000) user      (1000)      820 2023-04-07 03:43:02.000000 temperature_sensor_reader_xzf8971-1.6.0/pyproject.toml
+-rw-rw-r--   0 user      (1000) user      (1000)       38 2023-04-07 03:43:40.687587 temperature_sensor_reader_xzf8971-1.6.0/setup.cfg
+-rw-rw-r--   0 user      (1000) user      (1000)      128 2022-11-11 06:28:45.000000 temperature_sensor_reader_xzf8971-1.6.0/setup.py
+drwxrwxr-x   0 user      (1000) user      (1000)        0 2023-04-07 03:43:40.684587 temperature_sensor_reader_xzf8971-1.6.0/temperature_data_analysis/
+-rw-rw-r--   0 user      (1000) user      (1000)       83 2022-12-02 08:19:39.000000 temperature_sensor_reader_xzf8971-1.6.0/temperature_data_analysis/__init__.py
+-rw-rw-r--   0 user      (1000) user      (1000)     3448 2022-12-02 08:19:39.000000 temperature_sensor_reader_xzf8971-1.6.0/temperature_data_analysis/data_wrapper.py
+-rw-rw-r--   0 user      (1000) user      (1000)        0 2022-12-02 08:19:39.000000 temperature_sensor_reader_xzf8971-1.6.0/temperature_data_analysis/helper_function.py
+-rw-rw-r--   0 user      (1000) user      (1000)     1813 2023-04-07 03:30:03.000000 temperature_sensor_reader_xzf8971-1.6.0/temperature_data_analysis/plot_wrapper.py
+drwxrwxr-x   0 user      (1000) user      (1000)        0 2023-04-07 03:43:40.686587 temperature_sensor_reader_xzf8971-1.6.0/temperature_sensor_reader_xzf8971.egg-info/
+-rw-rw-r--   0 user      (1000) user      (1000)     3138 2023-04-07 03:43:40.000000 temperature_sensor_reader_xzf8971-1.6.0/temperature_sensor_reader_xzf8971.egg-info/PKG-INFO
+-rw-rw-r--   0 user      (1000) user      (1000)      985 2023-04-07 03:43:40.000000 temperature_sensor_reader_xzf8971-1.6.0/temperature_sensor_reader_xzf8971.egg-info/SOURCES.txt
+-rw-rw-r--   0 user      (1000) user      (1000)        1 2023-04-07 03:43:40.000000 temperature_sensor_reader_xzf8971-1.6.0/temperature_sensor_reader_xzf8971.egg-info/dependency_links.txt
+-rw-rw-r--   0 user      (1000) user      (1000)        1 2022-11-17 06:29:21.000000 temperature_sensor_reader_xzf8971-1.6.0/temperature_sensor_reader_xzf8971.egg-info/not-zip-safe
+-rw-rw-r--   0 user      (1000) user      (1000)       74 2023-04-07 03:43:40.000000 temperature_sensor_reader_xzf8971-1.6.0/temperature_sensor_reader_xzf8971.egg-info/requires.txt
+-rw-rw-r--   0 user      (1000) user      (1000)       64 2023-04-07 03:43:40.000000 temperature_sensor_reader_xzf8971-1.6.0/temperature_sensor_reader_xzf8971.egg-info/top_level.txt
```

### Comparing `temperature_sensor_reader_xzf8971-1.5.0/.gitignore` & `temperature_sensor_reader_xzf8971-1.6.0/.gitignore`

 * *Files identical despite different names*

### Comparing `temperature_sensor_reader_xzf8971-1.5.0/LICENSE` & `temperature_sensor_reader_xzf8971-1.6.0/LICENSE`

 * *Files identical despite different names*

### Comparing `temperature_sensor_reader_xzf8971-1.5.0/PKG-INFO` & `temperature_sensor_reader_xzf8971-1.6.0/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: temperature_sensor_reader_xzf8971
-Version: 1.5.0
+Version: 1.6.0
 Summary: A package to read/write registers on a temperature sensor with python.
 Author-email: Zifeng <zifeng.xu@foxmail.com>
 Project-URL: Homepage, https://github.com/xzf89718/temperature_sensor_reader
 Project-URL: Bug Tracker, https://github.com/xzf89718/temperature_sensor_reader/issues
 Classifier: Programming Language :: Python :: 3
 Classifier: License :: OSI Approved :: MIT License
 Classifier: Operating System :: OS Independent
```

### Comparing `temperature_sensor_reader_xzf8971-1.5.0/README.md` & `temperature_sensor_reader_xzf8971-1.6.0/README.md`

 * *Files identical despite different names*

### Comparing `temperature_sensor_reader_xzf8971-1.5.0/examples/JDRK_data_analysis.py` & `temperature_sensor_reader_xzf8971-1.6.0/examples/JDRK_data_analysis.py`

 * *Files identical despite different names*

### Comparing `temperature_sensor_reader_xzf8971-1.5.0/examples/JDRK_sensor.py` & `temperature_sensor_reader_xzf8971-1.6.0/examples/JDRK_sensor.py`

 * *Files identical despite different names*

### Comparing `temperature_sensor_reader_xzf8971-1.5.0/graphtec_reader/__main__.py` & `temperature_sensor_reader_xzf8971-1.6.0/graphtec_reader/__main__.py`

 * *Files identical despite different names*

### Comparing `temperature_sensor_reader_xzf8971-1.5.0/graphtec_reader/helper_function.py` & `temperature_sensor_reader_xzf8971-1.6.0/graphtec_reader/helper_function.py`

 * *Files identical despite different names*

### Comparing `temperature_sensor_reader_xzf8971-1.5.0/modbus_configuretools/derived_modbus_wrapper.py` & `temperature_sensor_reader_xzf8971-1.6.0/modbus_configuretools/derived_modbus_wrapper.py`

 * *Files identical despite different names*

### Comparing `temperature_sensor_reader_xzf8971-1.5.0/modbus_configuretools/helper_function.py` & `temperature_sensor_reader_xzf8971-1.6.0/modbus_configuretools/helper_function.py`

 * *Files identical despite different names*

### Comparing `temperature_sensor_reader_xzf8971-1.5.0/modbus_configuretools/modbus_wrapper.py` & `temperature_sensor_reader_xzf8971-1.6.0/modbus_configuretools/modbus_wrapper.py`

 * *Files identical despite different names*

### Comparing `temperature_sensor_reader_xzf8971-1.5.0/modbus_configuretools/temperature_sensor.py` & `temperature_sensor_reader_xzf8971-1.6.0/modbus_configuretools/temperature_sensor.py`

 * *Files identical despite different names*

### Comparing `temperature_sensor_reader_xzf8971-1.5.0/pyproject.toml` & `temperature_sensor_reader_xzf8971-1.6.0/pyproject.toml`

 * *Files 2% similar despite different names*

```diff
@@ -1,14 +1,14 @@
 [build-system]
 requires = ["setuptools>=61.0", "setuptools-scm", "cython ~= 0.29.0"]
 build-backend = "setuptools.build_meta"
 
 [project]
 name = "temperature_sensor_reader_xzf8971"
-version = "1.5.0"
+version = "1.6.0"
 authors = [
   { name="Zifeng", email="zifeng.xu@foxmail.com" },
 ]
 description = "A package to read/write registers on a temperature sensor with python."
 readme = "README.md"
 requires-python = ">=3.7"
 classifiers = [
```

### Comparing `temperature_sensor_reader_xzf8971-1.5.0/temperature_data_analysis/data_wrapper.py` & `temperature_sensor_reader_xzf8971-1.6.0/temperature_data_analysis/data_wrapper.py`

 * *Files identical despite different names*

### Comparing `temperature_sensor_reader_xzf8971-1.5.0/temperature_data_analysis/plot_wrapper.py` & `temperature_sensor_reader_xzf8971-1.6.0/temperature_data_analysis/plot_wrapper.py`

 * *Files identical despite different names*

### Comparing `temperature_sensor_reader_xzf8971-1.5.0/temperature_sensor_reader_xzf8971.egg-info/PKG-INFO` & `temperature_sensor_reader_xzf8971-1.6.0/temperature_sensor_reader_xzf8971.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: temperature-sensor-reader-xzf8971
-Version: 1.5.0
+Version: 1.6.0
 Summary: A package to read/write registers on a temperature sensor with python.
 Author-email: Zifeng <zifeng.xu@foxmail.com>
 Project-URL: Homepage, https://github.com/xzf89718/temperature_sensor_reader
 Project-URL: Bug Tracker, https://github.com/xzf89718/temperature_sensor_reader/issues
 Classifier: Programming Language :: Python :: 3
 Classifier: License :: OSI Approved :: MIT License
 Classifier: Operating System :: OS Independent
```

### Comparing `temperature_sensor_reader_xzf8971-1.5.0/temperature_sensor_reader_xzf8971.egg-info/SOURCES.txt` & `temperature_sensor_reader_xzf8971-1.6.0/temperature_sensor_reader_xzf8971.egg-info/SOURCES.txt`

 * *Files identical despite different names*

