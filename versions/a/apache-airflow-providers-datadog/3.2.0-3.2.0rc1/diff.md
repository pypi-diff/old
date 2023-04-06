# Comparing `tmp/apache-airflow-providers-datadog-3.2.0.tar.gz` & `tmp/apache-airflow-providers-datadog-3.2.0rc1.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "dist/apache-airflow-providers-datadog-3.2.0.tar", last modified: Sun Apr  2 05:38:41 2023, max compression
+gzip compressed data, was "dist/apache-airflow-providers-datadog-3.2.0rc1.tar", last modified: Sun Apr  2 05:47:29 2023, max compression
```

## Comparing `apache-airflow-providers-datadog-3.2.0.tar` & `apache-airflow-providers-datadog-3.2.0rc1.tar`

### file list

```diff
@@ -1,28 +1,28 @@
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-02 05:38:41.000000 apache-airflow-providers-datadog-3.2.0/
--rw-r--r--   0 root         (0) root         (0)    10850 2023-02-24 18:43:54.000000 apache-airflow-providers-datadog-3.2.0/LICENSE
--rw-r--r--   0 root         (0) root         (0)     1122 2023-04-02 05:38:39.000000 apache-airflow-providers-datadog-3.2.0/MANIFEST.in
--rw-r--r--   0 root         (0) root         (0)      240 2023-02-24 18:43:54.000000 apache-airflow-providers-datadog-3.2.0/NOTICE
--rw-r--r--   0 root         (0) root         (0)     8899 2023-04-02 05:38:41.000000 apache-airflow-providers-datadog-3.2.0/PKG-INFO
--rw-r--r--   0 root         (0) root         (0)     7372 2023-04-02 05:38:39.000000 apache-airflow-providers-datadog-3.2.0/README.rst
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-02 05:38:41.000000 apache-airflow-providers-datadog-3.2.0/airflow/
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-02 05:38:41.000000 apache-airflow-providers-datadog-3.2.0/airflow/providers/
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-02 05:38:41.000000 apache-airflow-providers-datadog-3.2.0/airflow/providers/datadog/
--rw-r--r--   0 root         (0) root         (0)      787 2023-02-24 18:43:53.000000 apache-airflow-providers-datadog-3.2.0/airflow/providers/datadog/__init__.py
--rw-r--r--   0 root         (0) root         (0)     2300 2023-04-02 05:38:39.000000 apache-airflow-providers-datadog-3.2.0/airflow/providers/datadog/get_provider_info.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-02 05:38:41.000000 apache-airflow-providers-datadog-3.2.0/airflow/providers/datadog/hooks/
--rw-r--r--   0 root         (0) root         (0)      787 2023-02-24 18:43:53.000000 apache-airflow-providers-datadog-3.2.0/airflow/providers/datadog/hooks/__init__.py
--rw-r--r--   0 root         (0) root         (0)     7317 2023-03-16 20:46:35.000000 apache-airflow-providers-datadog-3.2.0/airflow/providers/datadog/hooks/datadog.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-02 05:38:41.000000 apache-airflow-providers-datadog-3.2.0/airflow/providers/datadog/sensors/
--rw-r--r--   0 root         (0) root         (0)      787 2023-02-24 18:43:53.000000 apache-airflow-providers-datadog-3.2.0/airflow/providers/datadog/sensors/__init__.py
--rw-r--r--   0 root         (0) root         (0)     4060 2023-02-24 18:43:53.000000 apache-airflow-providers-datadog-3.2.0/airflow/providers/datadog/sensors/datadog.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-02 05:38:41.000000 apache-airflow-providers-datadog-3.2.0/apache_airflow_providers_datadog.egg-info/
--rw-r--r--   0 root         (0) root         (0)     8899 2023-04-02 05:38:40.000000 apache-airflow-providers-datadog-3.2.0/apache_airflow_providers_datadog.egg-info/PKG-INFO
--rw-r--r--   0 root         (0) root         (0)      727 2023-04-02 05:38:41.000000 apache-airflow-providers-datadog-3.2.0/apache_airflow_providers_datadog.egg-info/SOURCES.txt
--rw-r--r--   0 root         (0) root         (0)        1 2023-04-02 05:38:40.000000 apache-airflow-providers-datadog-3.2.0/apache_airflow_providers_datadog.egg-info/dependency_links.txt
--rw-r--r--   0 root         (0) root         (0)      104 2023-04-02 05:38:40.000000 apache-airflow-providers-datadog-3.2.0/apache_airflow_providers_datadog.egg-info/entry_points.txt
--rw-r--r--   0 root         (0) root         (0)        1 2023-04-02 05:38:40.000000 apache-airflow-providers-datadog-3.2.0/apache_airflow_providers_datadog.egg-info/not-zip-safe
--rw-r--r--   0 root         (0) root         (0)       38 2023-04-02 05:38:40.000000 apache-airflow-providers-datadog-3.2.0/apache_airflow_providers_datadog.egg-info/requires.txt
--rw-r--r--   0 root         (0) root         (0)        8 2023-04-02 05:38:40.000000 apache-airflow-providers-datadog-3.2.0/apache_airflow_providers_datadog.egg-info/top_level.txt
--rw-r--r--   0 root         (0) root         (0)     5393 2023-04-01 16:40:04.000000 apache-airflow-providers-datadog-3.2.0/pyproject.toml
--rw-r--r--   0 root         (0) root         (0)     1843 2023-04-02 05:38:41.000000 apache-airflow-providers-datadog-3.2.0/setup.cfg
--rw-r--r--   0 root         (0) root         (0)     1490 2023-04-02 05:38:39.000000 apache-airflow-providers-datadog-3.2.0/setup.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-02 05:47:29.000000 apache-airflow-providers-datadog-3.2.0rc1/
+-rw-r--r--   0 root         (0) root         (0)    10850 2023-02-24 18:43:54.000000 apache-airflow-providers-datadog-3.2.0rc1/LICENSE
+-rw-r--r--   0 root         (0) root         (0)     1122 2023-04-02 05:47:27.000000 apache-airflow-providers-datadog-3.2.0rc1/MANIFEST.in
+-rw-r--r--   0 root         (0) root         (0)      240 2023-02-24 18:43:54.000000 apache-airflow-providers-datadog-3.2.0rc1/NOTICE
+-rw-r--r--   0 root         (0) root         (0)     8905 2023-04-02 05:47:29.000000 apache-airflow-providers-datadog-3.2.0rc1/PKG-INFO
+-rw-r--r--   0 root         (0) root         (0)     7375 2023-04-02 05:47:27.000000 apache-airflow-providers-datadog-3.2.0rc1/README.rst
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-02 05:47:29.000000 apache-airflow-providers-datadog-3.2.0rc1/airflow/
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-02 05:47:29.000000 apache-airflow-providers-datadog-3.2.0rc1/airflow/providers/
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-02 05:47:29.000000 apache-airflow-providers-datadog-3.2.0rc1/airflow/providers/datadog/
+-rw-r--r--   0 root         (0) root         (0)      787 2023-02-24 18:43:53.000000 apache-airflow-providers-datadog-3.2.0rc1/airflow/providers/datadog/__init__.py
+-rw-r--r--   0 root         (0) root         (0)     2300 2023-04-02 05:47:27.000000 apache-airflow-providers-datadog-3.2.0rc1/airflow/providers/datadog/get_provider_info.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-02 05:47:29.000000 apache-airflow-providers-datadog-3.2.0rc1/airflow/providers/datadog/hooks/
+-rw-r--r--   0 root         (0) root         (0)      787 2023-02-24 18:43:53.000000 apache-airflow-providers-datadog-3.2.0rc1/airflow/providers/datadog/hooks/__init__.py
+-rw-r--r--   0 root         (0) root         (0)     7317 2023-03-16 20:46:35.000000 apache-airflow-providers-datadog-3.2.0rc1/airflow/providers/datadog/hooks/datadog.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-02 05:47:29.000000 apache-airflow-providers-datadog-3.2.0rc1/airflow/providers/datadog/sensors/
+-rw-r--r--   0 root         (0) root         (0)      787 2023-02-24 18:43:53.000000 apache-airflow-providers-datadog-3.2.0rc1/airflow/providers/datadog/sensors/__init__.py
+-rw-r--r--   0 root         (0) root         (0)     4060 2023-02-24 18:43:53.000000 apache-airflow-providers-datadog-3.2.0rc1/airflow/providers/datadog/sensors/datadog.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-02 05:47:29.000000 apache-airflow-providers-datadog-3.2.0rc1/apache_airflow_providers_datadog.egg-info/
+-rw-r--r--   0 root         (0) root         (0)     8905 2023-04-02 05:47:28.000000 apache-airflow-providers-datadog-3.2.0rc1/apache_airflow_providers_datadog.egg-info/PKG-INFO
+-rw-r--r--   0 root         (0) root         (0)      727 2023-04-02 05:47:28.000000 apache-airflow-providers-datadog-3.2.0rc1/apache_airflow_providers_datadog.egg-info/SOURCES.txt
+-rw-r--r--   0 root         (0) root         (0)        1 2023-04-02 05:47:28.000000 apache-airflow-providers-datadog-3.2.0rc1/apache_airflow_providers_datadog.egg-info/dependency_links.txt
+-rw-r--r--   0 root         (0) root         (0)      104 2023-04-02 05:47:28.000000 apache-airflow-providers-datadog-3.2.0rc1/apache_airflow_providers_datadog.egg-info/entry_points.txt
+-rw-r--r--   0 root         (0) root         (0)        1 2023-04-02 05:47:28.000000 apache-airflow-providers-datadog-3.2.0rc1/apache_airflow_providers_datadog.egg-info/not-zip-safe
+-rw-r--r--   0 root         (0) root         (0)       43 2023-04-02 05:47:28.000000 apache-airflow-providers-datadog-3.2.0rc1/apache_airflow_providers_datadog.egg-info/requires.txt
+-rw-r--r--   0 root         (0) root         (0)        8 2023-04-02 05:47:28.000000 apache-airflow-providers-datadog-3.2.0rc1/apache_airflow_providers_datadog.egg-info/top_level.txt
+-rw-r--r--   0 root         (0) root         (0)     5393 2023-04-01 16:40:04.000000 apache-airflow-providers-datadog-3.2.0rc1/pyproject.toml
+-rw-r--r--   0 root         (0) root         (0)     1851 2023-04-02 05:47:29.000000 apache-airflow-providers-datadog-3.2.0rc1/setup.cfg
+-rw-r--r--   0 root         (0) root         (0)     1490 2023-04-02 05:47:27.000000 apache-airflow-providers-datadog-3.2.0rc1/setup.py
```

### Comparing `apache-airflow-providers-datadog-3.2.0/LICENSE` & `apache-airflow-providers-datadog-3.2.0rc1/LICENSE`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-datadog-3.2.0/MANIFEST.in` & `apache-airflow-providers-datadog-3.2.0rc1/MANIFEST.in`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-datadog-3.2.0/PKG-INFO` & `apache-airflow-providers-datadog-3.2.0rc1/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: apache-airflow-providers-datadog
-Version: 3.2.0
+Version: 3.2.0rc1
 Summary: Provider for Apache Airflow. Implements apache-airflow-providers-datadog package
 Home-page: https://airflow.apache.org/
 Download-URL: https://archive.apache.org/dist/airflow/providers
 Author: Apache Software Foundation
 Author-email: dev@airflow.apache.org
 License: Apache License 2.0
 Project-URL: Documentation, https://airflow.apache.org/docs/apache-airflow-providers-datadog/3.2.0/
@@ -48,15 +48,15 @@
    KIND, either express or implied.  See the License for the
    specific language governing permissions and limitations
    under the License.
 
 
 Package ``apache-airflow-providers-datadog``
 
-Release: ``3.2.0``
+Release: ``3.2.0rc1``
 
 
 `Datadog <https://www.datadoghq.com/>`__
 
 
 Provider package
 ----------------
```

### Comparing `apache-airflow-providers-datadog-3.2.0/README.rst` & `apache-airflow-providers-datadog-3.2.0rc1/README.rst`

 * *Files 1% similar despite different names*

```diff
@@ -15,15 +15,15 @@
    KIND, either express or implied.  See the License for the
    specific language governing permissions and limitations
    under the License.
 
 
 Package ``apache-airflow-providers-datadog``
 
-Release: ``3.2.0``
+Release: ``3.2.0rc1``
 
 
 `Datadog <https://www.datadoghq.com/>`__
 
 
 Provider package
 ----------------
```

### Comparing `apache-airflow-providers-datadog-3.2.0/airflow/providers/datadog/__init__.py` & `apache-airflow-providers-datadog-3.2.0rc1/airflow/providers/datadog/__init__.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-datadog-3.2.0/airflow/providers/datadog/get_provider_info.py` & `apache-airflow-providers-datadog-3.2.0rc1/airflow/providers/datadog/get_provider_info.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-datadog-3.2.0/airflow/providers/datadog/hooks/__init__.py` & `apache-airflow-providers-datadog-3.2.0rc1/airflow/providers/datadog/hooks/__init__.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-datadog-3.2.0/airflow/providers/datadog/hooks/datadog.py` & `apache-airflow-providers-datadog-3.2.0rc1/airflow/providers/datadog/hooks/datadog.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-datadog-3.2.0/airflow/providers/datadog/sensors/__init__.py` & `apache-airflow-providers-datadog-3.2.0rc1/airflow/providers/datadog/sensors/__init__.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-datadog-3.2.0/airflow/providers/datadog/sensors/datadog.py` & `apache-airflow-providers-datadog-3.2.0rc1/airflow/providers/datadog/sensors/datadog.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-datadog-3.2.0/apache_airflow_providers_datadog.egg-info/PKG-INFO` & `apache-airflow-providers-datadog-3.2.0rc1/apache_airflow_providers_datadog.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: apache-airflow-providers-datadog
-Version: 3.2.0
+Version: 3.2.0rc1
 Summary: Provider for Apache Airflow. Implements apache-airflow-providers-datadog package
 Home-page: https://airflow.apache.org/
 Download-URL: https://archive.apache.org/dist/airflow/providers
 Author: Apache Software Foundation
 Author-email: dev@airflow.apache.org
 License: Apache License 2.0
 Project-URL: Documentation, https://airflow.apache.org/docs/apache-airflow-providers-datadog/3.2.0/
@@ -48,15 +48,15 @@
    KIND, either express or implied.  See the License for the
    specific language governing permissions and limitations
    under the License.
 
 
 Package ``apache-airflow-providers-datadog``
 
-Release: ``3.2.0``
+Release: ``3.2.0rc1``
 
 
 `Datadog <https://www.datadoghq.com/>`__
 
 
 Provider package
 ----------------
```

### Comparing `apache-airflow-providers-datadog-3.2.0/apache_airflow_providers_datadog.egg-info/SOURCES.txt` & `apache-airflow-providers-datadog-3.2.0rc1/apache_airflow_providers_datadog.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-datadog-3.2.0/pyproject.toml` & `apache-airflow-providers-datadog-3.2.0rc1/pyproject.toml`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-datadog-3.2.0/setup.cfg` & `apache-airflow-providers-datadog-3.2.0rc1/setup.cfg`

 * *Files 8% similar despite different names*

```diff
@@ -42,21 +42,21 @@
 include_package_data = True
 python_requires = ~=3.7
 packages = find:
 setup_requires = 
 	setuptools
 	wheel
 install_requires = 
-	apache-airflow>=2.3.0
+	apache-airflow>=2.3.0.dev0
 	datadog>=0.14.0
 
 [options.entry_points]
 apache_airflow_provider = 
 	provider_info=airflow.providers.datadog.get_provider_info:get_provider_info
 
 [files]
 packages = airflow.providers.datadog
 
 [egg_info]
-tag_build = 
+tag_build = rc1
 tag_date = 0
```

### Comparing `apache-airflow-providers-datadog-3.2.0/setup.py` & `apache-airflow-providers-datadog-3.2.0rc1/setup.py`

 * *Files identical despite different names*

