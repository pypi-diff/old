# Comparing `tmp/apache-airflow-providers-airbyte-3.2.1.tar.gz` & `tmp/apache-airflow-providers-airbyte-3.2.1rc1.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "dist/apache-airflow-providers-airbyte-3.2.1.tar", last modified: Sun Apr  2 05:37:53 2023, max compression
+gzip compressed data, was "dist/apache-airflow-providers-airbyte-3.2.1rc1.tar", last modified: Sun Apr  2 05:46:42 2023, max compression
```

## Comparing `apache-airflow-providers-airbyte-3.2.1.tar` & `apache-airflow-providers-airbyte-3.2.1rc1.tar`

### file list

```diff
@@ -1,31 +1,31 @@
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-02 05:37:53.000000 apache-airflow-providers-airbyte-3.2.1/
--rw-r--r--   0 root         (0) root         (0)    10850 2023-02-24 18:43:54.000000 apache-airflow-providers-airbyte-3.2.1/LICENSE
--rw-r--r--   0 root         (0) root         (0)     1122 2023-04-02 05:37:51.000000 apache-airflow-providers-airbyte-3.2.1/MANIFEST.in
--rw-r--r--   0 root         (0) root         (0)      240 2023-02-24 18:43:54.000000 apache-airflow-providers-airbyte-3.2.1/NOTICE
--rw-r--r--   0 root         (0) root         (0)    10601 2023-04-02 05:37:53.000000 apache-airflow-providers-airbyte-3.2.1/PKG-INFO
--rw-r--r--   0 root         (0) root         (0)     9053 2023-04-02 05:37:51.000000 apache-airflow-providers-airbyte-3.2.1/README.rst
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-02 05:37:53.000000 apache-airflow-providers-airbyte-3.2.1/airflow/
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-02 05:37:53.000000 apache-airflow-providers-airbyte-3.2.1/airflow/providers/
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-02 05:37:53.000000 apache-airflow-providers-airbyte-3.2.1/airflow/providers/airbyte/
--rw-r--r--   0 root         (0) root         (0)      787 2023-02-24 18:43:53.000000 apache-airflow-providers-airbyte-3.2.1/airflow/providers/airbyte/__init__.py
--rw-r--r--   0 root         (0) root         (0)     2568 2023-04-02 05:37:51.000000 apache-airflow-providers-airbyte-3.2.1/airflow/providers/airbyte/get_provider_info.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-02 05:37:53.000000 apache-airflow-providers-airbyte-3.2.1/airflow/providers/airbyte/hooks/
--rw-r--r--   0 root         (0) root         (0)      787 2023-02-24 18:43:53.000000 apache-airflow-providers-airbyte-3.2.1/airflow/providers/airbyte/hooks/__init__.py
--rw-r--r--   0 root         (0) root         (0)     5059 2023-03-11 12:12:47.000000 apache-airflow-providers-airbyte-3.2.1/airflow/providers/airbyte/hooks/airbyte.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-02 05:37:53.000000 apache-airflow-providers-airbyte-3.2.1/airflow/providers/airbyte/operators/
--rw-r--r--   0 root         (0) root         (0)      787 2023-02-24 18:43:53.000000 apache-airflow-providers-airbyte-3.2.1/airflow/providers/airbyte/operators/__init__.py
--rw-r--r--   0 root         (0) root         (0)     3869 2023-03-11 12:12:47.000000 apache-airflow-providers-airbyte-3.2.1/airflow/providers/airbyte/operators/airbyte.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-02 05:37:53.000000 apache-airflow-providers-airbyte-3.2.1/airflow/providers/airbyte/sensors/
--rw-r--r--   0 root         (0) root         (0)      785 2023-02-24 18:43:53.000000 apache-airflow-providers-airbyte-3.2.1/airflow/providers/airbyte/sensors/__init__.py
--rw-r--r--   0 root         (0) root         (0)     2793 2023-03-11 12:12:47.000000 apache-airflow-providers-airbyte-3.2.1/airflow/providers/airbyte/sensors/airbyte.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-02 05:37:53.000000 apache-airflow-providers-airbyte-3.2.1/apache_airflow_providers_airbyte.egg-info/
--rw-r--r--   0 root         (0) root         (0)    10601 2023-04-02 05:37:52.000000 apache-airflow-providers-airbyte-3.2.1/apache_airflow_providers_airbyte.egg-info/PKG-INFO
--rw-r--r--   0 root         (0) root         (0)      822 2023-04-02 05:37:53.000000 apache-airflow-providers-airbyte-3.2.1/apache_airflow_providers_airbyte.egg-info/SOURCES.txt
--rw-r--r--   0 root         (0) root         (0)        1 2023-04-02 05:37:52.000000 apache-airflow-providers-airbyte-3.2.1/apache_airflow_providers_airbyte.egg-info/dependency_links.txt
--rw-r--r--   0 root         (0) root         (0)      104 2023-04-02 05:37:52.000000 apache-airflow-providers-airbyte-3.2.1/apache_airflow_providers_airbyte.egg-info/entry_points.txt
--rw-r--r--   0 root         (0) root         (0)        1 2023-04-02 05:37:52.000000 apache-airflow-providers-airbyte-3.2.1/apache_airflow_providers_airbyte.egg-info/not-zip-safe
--rw-r--r--   0 root         (0) root         (0)       90 2023-04-02 05:37:52.000000 apache-airflow-providers-airbyte-3.2.1/apache_airflow_providers_airbyte.egg-info/requires.txt
--rw-r--r--   0 root         (0) root         (0)        8 2023-04-02 05:37:52.000000 apache-airflow-providers-airbyte-3.2.1/apache_airflow_providers_airbyte.egg-info/top_level.txt
--rw-r--r--   0 root         (0) root         (0)     5393 2023-04-01 16:40:04.000000 apache-airflow-providers-airbyte-3.2.1/pyproject.toml
--rw-r--r--   0 root         (0) root         (0)     1857 2023-04-02 05:37:53.000000 apache-airflow-providers-airbyte-3.2.1/setup.cfg
--rw-r--r--   0 root         (0) root         (0)     1531 2023-04-02 05:37:51.000000 apache-airflow-providers-airbyte-3.2.1/setup.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-02 05:46:42.000000 apache-airflow-providers-airbyte-3.2.1rc1/
+-rw-r--r--   0 root         (0) root         (0)    10850 2023-02-24 18:43:54.000000 apache-airflow-providers-airbyte-3.2.1rc1/LICENSE
+-rw-r--r--   0 root         (0) root         (0)     1122 2023-04-02 05:46:40.000000 apache-airflow-providers-airbyte-3.2.1rc1/MANIFEST.in
+-rw-r--r--   0 root         (0) root         (0)      240 2023-02-24 18:43:54.000000 apache-airflow-providers-airbyte-3.2.1rc1/NOTICE
+-rw-r--r--   0 root         (0) root         (0)    10607 2023-04-02 05:46:42.000000 apache-airflow-providers-airbyte-3.2.1rc1/PKG-INFO
+-rw-r--r--   0 root         (0) root         (0)     9056 2023-04-02 05:46:40.000000 apache-airflow-providers-airbyte-3.2.1rc1/README.rst
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-02 05:46:42.000000 apache-airflow-providers-airbyte-3.2.1rc1/airflow/
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-02 05:46:42.000000 apache-airflow-providers-airbyte-3.2.1rc1/airflow/providers/
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-02 05:46:42.000000 apache-airflow-providers-airbyte-3.2.1rc1/airflow/providers/airbyte/
+-rw-r--r--   0 root         (0) root         (0)      787 2023-02-24 18:43:53.000000 apache-airflow-providers-airbyte-3.2.1rc1/airflow/providers/airbyte/__init__.py
+-rw-r--r--   0 root         (0) root         (0)     2568 2023-04-02 05:46:40.000000 apache-airflow-providers-airbyte-3.2.1rc1/airflow/providers/airbyte/get_provider_info.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-02 05:46:42.000000 apache-airflow-providers-airbyte-3.2.1rc1/airflow/providers/airbyte/hooks/
+-rw-r--r--   0 root         (0) root         (0)      787 2023-02-24 18:43:53.000000 apache-airflow-providers-airbyte-3.2.1rc1/airflow/providers/airbyte/hooks/__init__.py
+-rw-r--r--   0 root         (0) root         (0)     5059 2023-03-11 12:12:47.000000 apache-airflow-providers-airbyte-3.2.1rc1/airflow/providers/airbyte/hooks/airbyte.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-02 05:46:42.000000 apache-airflow-providers-airbyte-3.2.1rc1/airflow/providers/airbyte/operators/
+-rw-r--r--   0 root         (0) root         (0)      787 2023-02-24 18:43:53.000000 apache-airflow-providers-airbyte-3.2.1rc1/airflow/providers/airbyte/operators/__init__.py
+-rw-r--r--   0 root         (0) root         (0)     3869 2023-03-11 12:12:47.000000 apache-airflow-providers-airbyte-3.2.1rc1/airflow/providers/airbyte/operators/airbyte.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-02 05:46:42.000000 apache-airflow-providers-airbyte-3.2.1rc1/airflow/providers/airbyte/sensors/
+-rw-r--r--   0 root         (0) root         (0)      785 2023-02-24 18:43:53.000000 apache-airflow-providers-airbyte-3.2.1rc1/airflow/providers/airbyte/sensors/__init__.py
+-rw-r--r--   0 root         (0) root         (0)     2793 2023-03-11 12:12:47.000000 apache-airflow-providers-airbyte-3.2.1rc1/airflow/providers/airbyte/sensors/airbyte.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-02 05:46:42.000000 apache-airflow-providers-airbyte-3.2.1rc1/apache_airflow_providers_airbyte.egg-info/
+-rw-r--r--   0 root         (0) root         (0)    10607 2023-04-02 05:46:41.000000 apache-airflow-providers-airbyte-3.2.1rc1/apache_airflow_providers_airbyte.egg-info/PKG-INFO
+-rw-r--r--   0 root         (0) root         (0)      822 2023-04-02 05:46:41.000000 apache-airflow-providers-airbyte-3.2.1rc1/apache_airflow_providers_airbyte.egg-info/SOURCES.txt
+-rw-r--r--   0 root         (0) root         (0)        1 2023-04-02 05:46:41.000000 apache-airflow-providers-airbyte-3.2.1rc1/apache_airflow_providers_airbyte.egg-info/dependency_links.txt
+-rw-r--r--   0 root         (0) root         (0)      104 2023-04-02 05:46:41.000000 apache-airflow-providers-airbyte-3.2.1rc1/apache_airflow_providers_airbyte.egg-info/entry_points.txt
+-rw-r--r--   0 root         (0) root         (0)        1 2023-04-02 05:46:41.000000 apache-airflow-providers-airbyte-3.2.1rc1/apache_airflow_providers_airbyte.egg-info/not-zip-safe
+-rw-r--r--   0 root         (0) root         (0)       95 2023-04-02 05:46:41.000000 apache-airflow-providers-airbyte-3.2.1rc1/apache_airflow_providers_airbyte.egg-info/requires.txt
+-rw-r--r--   0 root         (0) root         (0)        8 2023-04-02 05:46:41.000000 apache-airflow-providers-airbyte-3.2.1rc1/apache_airflow_providers_airbyte.egg-info/top_level.txt
+-rw-r--r--   0 root         (0) root         (0)     5393 2023-04-01 16:40:04.000000 apache-airflow-providers-airbyte-3.2.1rc1/pyproject.toml
+-rw-r--r--   0 root         (0) root         (0)     1865 2023-04-02 05:46:42.000000 apache-airflow-providers-airbyte-3.2.1rc1/setup.cfg
+-rw-r--r--   0 root         (0) root         (0)     1531 2023-04-02 05:46:40.000000 apache-airflow-providers-airbyte-3.2.1rc1/setup.py
```

### Comparing `apache-airflow-providers-airbyte-3.2.1/LICENSE` & `apache-airflow-providers-airbyte-3.2.1rc1/LICENSE`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-airbyte-3.2.1/MANIFEST.in` & `apache-airflow-providers-airbyte-3.2.1rc1/MANIFEST.in`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-airbyte-3.2.1/PKG-INFO` & `apache-airflow-providers-airbyte-3.2.1rc1/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: apache-airflow-providers-airbyte
-Version: 3.2.1
+Version: 3.2.1rc1
 Summary: Provider for Apache Airflow. Implements apache-airflow-providers-airbyte package
 Home-page: https://airflow.apache.org/
 Download-URL: https://archive.apache.org/dist/airflow/providers
 Author: Apache Software Foundation
 Author-email: dev@airflow.apache.org
 License: Apache License 2.0
 Project-URL: Documentation, https://airflow.apache.org/docs/apache-airflow-providers-airbyte/3.2.1/
@@ -49,15 +49,15 @@
    KIND, either express or implied.  See the License for the
    specific language governing permissions and limitations
    under the License.
 
 
 Package ``apache-airflow-providers-airbyte``
 
-Release: ``3.2.1``
+Release: ``3.2.1rc1``
 
 
 `Airbyte <https://airbyte.io/>`__
 
 
 Provider package
 ----------------
```

### Comparing `apache-airflow-providers-airbyte-3.2.1/README.rst` & `apache-airflow-providers-airbyte-3.2.1rc1/README.rst`

 * *Files 0% similar despite different names*

```diff
@@ -15,15 +15,15 @@
    KIND, either express or implied.  See the License for the
    specific language governing permissions and limitations
    under the License.
 
 
 Package ``apache-airflow-providers-airbyte``
 
-Release: ``3.2.1``
+Release: ``3.2.1rc1``
 
 
 `Airbyte <https://airbyte.io/>`__
 
 
 Provider package
 ----------------
```

### Comparing `apache-airflow-providers-airbyte-3.2.1/airflow/providers/airbyte/__init__.py` & `apache-airflow-providers-airbyte-3.2.1rc1/airflow/providers/airbyte/__init__.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-airbyte-3.2.1/airflow/providers/airbyte/get_provider_info.py` & `apache-airflow-providers-airbyte-3.2.1rc1/airflow/providers/airbyte/get_provider_info.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-airbyte-3.2.1/airflow/providers/airbyte/hooks/__init__.py` & `apache-airflow-providers-airbyte-3.2.1rc1/airflow/providers/airbyte/hooks/__init__.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-airbyte-3.2.1/airflow/providers/airbyte/hooks/airbyte.py` & `apache-airflow-providers-airbyte-3.2.1rc1/airflow/providers/airbyte/hooks/airbyte.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-airbyte-3.2.1/airflow/providers/airbyte/operators/__init__.py` & `apache-airflow-providers-airbyte-3.2.1rc1/airflow/providers/airbyte/operators/__init__.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-airbyte-3.2.1/airflow/providers/airbyte/operators/airbyte.py` & `apache-airflow-providers-airbyte-3.2.1rc1/airflow/providers/airbyte/operators/airbyte.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-airbyte-3.2.1/airflow/providers/airbyte/sensors/__init__.py` & `apache-airflow-providers-airbyte-3.2.1rc1/airflow/providers/airbyte/sensors/__init__.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-airbyte-3.2.1/airflow/providers/airbyte/sensors/airbyte.py` & `apache-airflow-providers-airbyte-3.2.1rc1/airflow/providers/airbyte/sensors/airbyte.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-airbyte-3.2.1/apache_airflow_providers_airbyte.egg-info/PKG-INFO` & `apache-airflow-providers-airbyte-3.2.1rc1/apache_airflow_providers_airbyte.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: apache-airflow-providers-airbyte
-Version: 3.2.1
+Version: 3.2.1rc1
 Summary: Provider for Apache Airflow. Implements apache-airflow-providers-airbyte package
 Home-page: https://airflow.apache.org/
 Download-URL: https://archive.apache.org/dist/airflow/providers
 Author: Apache Software Foundation
 Author-email: dev@airflow.apache.org
 License: Apache License 2.0
 Project-URL: Documentation, https://airflow.apache.org/docs/apache-airflow-providers-airbyte/3.2.1/
@@ -49,15 +49,15 @@
    KIND, either express or implied.  See the License for the
    specific language governing permissions and limitations
    under the License.
 
 
 Package ``apache-airflow-providers-airbyte``
 
-Release: ``3.2.1``
+Release: ``3.2.1rc1``
 
 
 `Airbyte <https://airbyte.io/>`__
 
 
 Provider package
 ----------------
```

### Comparing `apache-airflow-providers-airbyte-3.2.1/apache_airflow_providers_airbyte.egg-info/SOURCES.txt` & `apache-airflow-providers-airbyte-3.2.1rc1/apache_airflow_providers_airbyte.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-airbyte-3.2.1/pyproject.toml` & `apache-airflow-providers-airbyte-3.2.1rc1/pyproject.toml`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-airbyte-3.2.1/setup.cfg` & `apache-airflow-providers-airbyte-3.2.1rc1/setup.cfg`

 * *Files 2% similar despite different names*

```diff
@@ -43,20 +43,20 @@
 python_requires = ~=3.7
 packages = find:
 setup_requires = 
 	setuptools
 	wheel
 install_requires = 
 	apache-airflow-providers-http
-	apache-airflow>=2.3.0
+	apache-airflow>=2.3.0.dev0
 
 [options.entry_points]
 apache_airflow_provider = 
 	provider_info=airflow.providers.airbyte.get_provider_info:get_provider_info
 
 [files]
 packages = airflow.providers.airbyte
 
 [egg_info]
-tag_build = 
+tag_build = rc1
 tag_date = 0
```

### Comparing `apache-airflow-providers-airbyte-3.2.1/setup.py` & `apache-airflow-providers-airbyte-3.2.1rc1/setup.py`

 * *Files identical despite different names*

