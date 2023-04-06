# Comparing `tmp/apache-airflow-providers-http-4.3.0.tar.gz` & `tmp/apache-airflow-providers-http-4.3.0rc1.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "dist/apache-airflow-providers-http-4.3.0.tar", last modified: Sun Apr  2 05:40:03 2023, max compression
+gzip compressed data, was "dist/apache-airflow-providers-http-4.3.0rc1.tar", last modified: Sun Apr  2 05:48:49 2023, max compression
```

## Comparing `apache-airflow-providers-http-4.3.0.tar` & `apache-airflow-providers-http-4.3.0rc1.tar`

### file list

```diff
@@ -1,31 +1,31 @@
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-02 05:40:03.000000 apache-airflow-providers-http-4.3.0/
--rw-r--r--   0 root         (0) root         (0)    10850 2023-02-24 18:43:54.000000 apache-airflow-providers-http-4.3.0/LICENSE
--rw-r--r--   0 root         (0) root         (0)     1122 2023-04-02 05:40:01.000000 apache-airflow-providers-http-4.3.0/MANIFEST.in
--rw-r--r--   0 root         (0) root         (0)      240 2023-02-24 18:43:54.000000 apache-airflow-providers-http-4.3.0/NOTICE
--rw-r--r--   0 root         (0) root         (0)    11487 2023-04-02 05:40:03.000000 apache-airflow-providers-http-4.3.0/PKG-INFO
--rw-r--r--   0 root         (0) root         (0)     9969 2023-04-02 05:40:01.000000 apache-airflow-providers-http-4.3.0/README.rst
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-02 05:40:03.000000 apache-airflow-providers-http-4.3.0/airflow/
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-02 05:40:03.000000 apache-airflow-providers-http-4.3.0/airflow/providers/
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-02 05:40:03.000000 apache-airflow-providers-http-4.3.0/airflow/providers/http/
--rw-r--r--   0 root         (0) root         (0)      787 2023-02-24 18:43:53.000000 apache-airflow-providers-http-4.3.0/airflow/providers/http/__init__.py
--rw-r--r--   0 root         (0) root         (0)     2901 2023-04-02 05:40:01.000000 apache-airflow-providers-http-4.3.0/airflow/providers/http/get_provider_info.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-02 05:40:03.000000 apache-airflow-providers-http-4.3.0/airflow/providers/http/hooks/
--rw-r--r--   0 root         (0) root         (0)      787 2023-02-24 18:43:53.000000 apache-airflow-providers-http-4.3.0/airflow/providers/http/hooks/__init__.py
--rw-r--r--   0 root         (0) root         (0)    16289 2023-03-27 08:32:49.000000 apache-airflow-providers-http-4.3.0/airflow/providers/http/hooks/http.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-02 05:40:03.000000 apache-airflow-providers-http-4.3.0/airflow/providers/http/operators/
--rw-r--r--   0 root         (0) root         (0)      787 2023-02-24 18:43:53.000000 apache-airflow-providers-http-4.3.0/airflow/providers/http/operators/__init__.py
--rw-r--r--   0 root         (0) root         (0)     5828 2023-03-27 08:32:49.000000 apache-airflow-providers-http-4.3.0/airflow/providers/http/operators/http.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-02 05:40:03.000000 apache-airflow-providers-http-4.3.0/airflow/providers/http/sensors/
--rw-r--r--   0 root         (0) root         (0)      787 2023-02-24 18:43:53.000000 apache-airflow-providers-http-4.3.0/airflow/providers/http/sensors/__init__.py
--rw-r--r--   0 root         (0) root         (0)     5885 2023-02-24 18:43:53.000000 apache-airflow-providers-http-4.3.0/airflow/providers/http/sensors/http.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-02 05:40:03.000000 apache-airflow-providers-http-4.3.0/apache_airflow_providers_http.egg-info/
--rw-r--r--   0 root         (0) root         (0)    11487 2023-04-02 05:40:03.000000 apache-airflow-providers-http-4.3.0/apache_airflow_providers_http.egg-info/PKG-INFO
--rw-r--r--   0 root         (0) root         (0)      768 2023-04-02 05:40:03.000000 apache-airflow-providers-http-4.3.0/apache_airflow_providers_http.egg-info/SOURCES.txt
--rw-r--r--   0 root         (0) root         (0)        1 2023-04-02 05:40:03.000000 apache-airflow-providers-http-4.3.0/apache_airflow_providers_http.egg-info/dependency_links.txt
--rw-r--r--   0 root         (0) root         (0)      101 2023-04-02 05:40:03.000000 apache-airflow-providers-http-4.3.0/apache_airflow_providers_http.egg-info/entry_points.txt
--rw-r--r--   0 root         (0) root         (0)        1 2023-04-02 05:40:03.000000 apache-airflow-providers-http-4.3.0/apache_airflow_providers_http.egg-info/not-zip-safe
--rw-r--r--   0 root         (0) root         (0)       51 2023-04-02 05:40:03.000000 apache-airflow-providers-http-4.3.0/apache_airflow_providers_http.egg-info/requires.txt
--rw-r--r--   0 root         (0) root         (0)        8 2023-04-02 05:40:03.000000 apache-airflow-providers-http-4.3.0/apache_airflow_providers_http.egg-info/top_level.txt
--rw-r--r--   0 root         (0) root         (0)     5393 2023-04-01 16:40:04.000000 apache-airflow-providers-http-4.3.0/pyproject.toml
--rw-r--r--   0 root         (0) root         (0)     1840 2023-04-02 05:40:03.000000 apache-airflow-providers-http-4.3.0/setup.cfg
--rw-r--r--   0 root         (0) root         (0)     1456 2023-04-02 05:40:01.000000 apache-airflow-providers-http-4.3.0/setup.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-02 05:48:49.000000 apache-airflow-providers-http-4.3.0rc1/
+-rw-r--r--   0 root         (0) root         (0)    10850 2023-02-24 18:43:54.000000 apache-airflow-providers-http-4.3.0rc1/LICENSE
+-rw-r--r--   0 root         (0) root         (0)     1122 2023-04-02 05:48:48.000000 apache-airflow-providers-http-4.3.0rc1/MANIFEST.in
+-rw-r--r--   0 root         (0) root         (0)      240 2023-02-24 18:43:54.000000 apache-airflow-providers-http-4.3.0rc1/NOTICE
+-rw-r--r--   0 root         (0) root         (0)    11493 2023-04-02 05:48:49.000000 apache-airflow-providers-http-4.3.0rc1/PKG-INFO
+-rw-r--r--   0 root         (0) root         (0)     9972 2023-04-02 05:48:48.000000 apache-airflow-providers-http-4.3.0rc1/README.rst
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-02 05:48:49.000000 apache-airflow-providers-http-4.3.0rc1/airflow/
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-02 05:48:49.000000 apache-airflow-providers-http-4.3.0rc1/airflow/providers/
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-02 05:48:49.000000 apache-airflow-providers-http-4.3.0rc1/airflow/providers/http/
+-rw-r--r--   0 root         (0) root         (0)      787 2023-02-24 18:43:53.000000 apache-airflow-providers-http-4.3.0rc1/airflow/providers/http/__init__.py
+-rw-r--r--   0 root         (0) root         (0)     2901 2023-04-02 05:48:48.000000 apache-airflow-providers-http-4.3.0rc1/airflow/providers/http/get_provider_info.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-02 05:48:49.000000 apache-airflow-providers-http-4.3.0rc1/airflow/providers/http/hooks/
+-rw-r--r--   0 root         (0) root         (0)      787 2023-02-24 18:43:53.000000 apache-airflow-providers-http-4.3.0rc1/airflow/providers/http/hooks/__init__.py
+-rw-r--r--   0 root         (0) root         (0)    16289 2023-03-27 08:32:49.000000 apache-airflow-providers-http-4.3.0rc1/airflow/providers/http/hooks/http.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-02 05:48:49.000000 apache-airflow-providers-http-4.3.0rc1/airflow/providers/http/operators/
+-rw-r--r--   0 root         (0) root         (0)      787 2023-02-24 18:43:53.000000 apache-airflow-providers-http-4.3.0rc1/airflow/providers/http/operators/__init__.py
+-rw-r--r--   0 root         (0) root         (0)     5828 2023-03-27 08:32:49.000000 apache-airflow-providers-http-4.3.0rc1/airflow/providers/http/operators/http.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-02 05:48:49.000000 apache-airflow-providers-http-4.3.0rc1/airflow/providers/http/sensors/
+-rw-r--r--   0 root         (0) root         (0)      787 2023-02-24 18:43:53.000000 apache-airflow-providers-http-4.3.0rc1/airflow/providers/http/sensors/__init__.py
+-rw-r--r--   0 root         (0) root         (0)     5885 2023-02-24 18:43:53.000000 apache-airflow-providers-http-4.3.0rc1/airflow/providers/http/sensors/http.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-02 05:48:49.000000 apache-airflow-providers-http-4.3.0rc1/apache_airflow_providers_http.egg-info/
+-rw-r--r--   0 root         (0) root         (0)    11493 2023-04-02 05:48:49.000000 apache-airflow-providers-http-4.3.0rc1/apache_airflow_providers_http.egg-info/PKG-INFO
+-rw-r--r--   0 root         (0) root         (0)      768 2023-04-02 05:48:49.000000 apache-airflow-providers-http-4.3.0rc1/apache_airflow_providers_http.egg-info/SOURCES.txt
+-rw-r--r--   0 root         (0) root         (0)        1 2023-04-02 05:48:49.000000 apache-airflow-providers-http-4.3.0rc1/apache_airflow_providers_http.egg-info/dependency_links.txt
+-rw-r--r--   0 root         (0) root         (0)      101 2023-04-02 05:48:49.000000 apache-airflow-providers-http-4.3.0rc1/apache_airflow_providers_http.egg-info/entry_points.txt
+-rw-r--r--   0 root         (0) root         (0)        1 2023-04-02 05:48:49.000000 apache-airflow-providers-http-4.3.0rc1/apache_airflow_providers_http.egg-info/not-zip-safe
+-rw-r--r--   0 root         (0) root         (0)       51 2023-04-02 05:48:49.000000 apache-airflow-providers-http-4.3.0rc1/apache_airflow_providers_http.egg-info/requires.txt
+-rw-r--r--   0 root         (0) root         (0)        8 2023-04-02 05:48:49.000000 apache-airflow-providers-http-4.3.0rc1/apache_airflow_providers_http.egg-info/top_level.txt
+-rw-r--r--   0 root         (0) root         (0)     5393 2023-04-01 16:40:04.000000 apache-airflow-providers-http-4.3.0rc1/pyproject.toml
+-rw-r--r--   0 root         (0) root         (0)     1843 2023-04-02 05:48:49.000000 apache-airflow-providers-http-4.3.0rc1/setup.cfg
+-rw-r--r--   0 root         (0) root         (0)     1456 2023-04-02 05:48:48.000000 apache-airflow-providers-http-4.3.0rc1/setup.py
```

### Comparing `apache-airflow-providers-http-4.3.0/LICENSE` & `apache-airflow-providers-http-4.3.0rc1/LICENSE`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-http-4.3.0/MANIFEST.in` & `apache-airflow-providers-http-4.3.0rc1/MANIFEST.in`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-http-4.3.0/PKG-INFO` & `apache-airflow-providers-http-4.3.0rc1/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: apache-airflow-providers-http
-Version: 4.3.0
+Version: 4.3.0rc1
 Summary: Provider for Apache Airflow. Implements apache-airflow-providers-http package
 Home-page: https://airflow.apache.org/
 Download-URL: https://archive.apache.org/dist/airflow/providers
 Author: Apache Software Foundation
 Author-email: dev@airflow.apache.org
 License: Apache License 2.0
 Project-URL: Documentation, https://airflow.apache.org/docs/apache-airflow-providers-http/4.3.0/
@@ -48,15 +48,15 @@
    KIND, either express or implied.  See the License for the
    specific language governing permissions and limitations
    under the License.
 
 
 Package ``apache-airflow-providers-http``
 
-Release: ``4.3.0``
+Release: ``4.3.0rc1``
 
 
 `Hypertext Transfer Protocol (HTTP) <https://www.w3.org/Protocols/>`__
 
 
 Provider package
 ----------------
```

### Comparing `apache-airflow-providers-http-4.3.0/README.rst` & `apache-airflow-providers-http-4.3.0rc1/README.rst`

 * *Files 0% similar despite different names*

```diff
@@ -15,15 +15,15 @@
    KIND, either express or implied.  See the License for the
    specific language governing permissions and limitations
    under the License.
 
 
 Package ``apache-airflow-providers-http``
 
-Release: ``4.3.0``
+Release: ``4.3.0rc1``
 
 
 `Hypertext Transfer Protocol (HTTP) <https://www.w3.org/Protocols/>`__
 
 
 Provider package
 ----------------
```

### Comparing `apache-airflow-providers-http-4.3.0/airflow/providers/http/__init__.py` & `apache-airflow-providers-http-4.3.0rc1/airflow/providers/http/__init__.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-http-4.3.0/airflow/providers/http/get_provider_info.py` & `apache-airflow-providers-http-4.3.0rc1/airflow/providers/http/get_provider_info.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-http-4.3.0/airflow/providers/http/hooks/__init__.py` & `apache-airflow-providers-http-4.3.0rc1/airflow/providers/http/hooks/__init__.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-http-4.3.0/airflow/providers/http/hooks/http.py` & `apache-airflow-providers-http-4.3.0rc1/airflow/providers/http/hooks/http.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-http-4.3.0/airflow/providers/http/operators/__init__.py` & `apache-airflow-providers-http-4.3.0rc1/airflow/providers/http/operators/__init__.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-http-4.3.0/airflow/providers/http/operators/http.py` & `apache-airflow-providers-http-4.3.0rc1/airflow/providers/http/operators/http.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-http-4.3.0/airflow/providers/http/sensors/__init__.py` & `apache-airflow-providers-http-4.3.0rc1/airflow/providers/http/sensors/__init__.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-http-4.3.0/airflow/providers/http/sensors/http.py` & `apache-airflow-providers-http-4.3.0rc1/airflow/providers/http/sensors/http.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-http-4.3.0/apache_airflow_providers_http.egg-info/PKG-INFO` & `apache-airflow-providers-http-4.3.0rc1/apache_airflow_providers_http.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: apache-airflow-providers-http
-Version: 4.3.0
+Version: 4.3.0rc1
 Summary: Provider for Apache Airflow. Implements apache-airflow-providers-http package
 Home-page: https://airflow.apache.org/
 Download-URL: https://archive.apache.org/dist/airflow/providers
 Author: Apache Software Foundation
 Author-email: dev@airflow.apache.org
 License: Apache License 2.0
 Project-URL: Documentation, https://airflow.apache.org/docs/apache-airflow-providers-http/4.3.0/
@@ -48,15 +48,15 @@
    KIND, either express or implied.  See the License for the
    specific language governing permissions and limitations
    under the License.
 
 
 Package ``apache-airflow-providers-http``
 
-Release: ``4.3.0``
+Release: ``4.3.0rc1``
 
 
 `Hypertext Transfer Protocol (HTTP) <https://www.w3.org/Protocols/>`__
 
 
 Provider package
 ----------------
```

### Comparing `apache-airflow-providers-http-4.3.0/apache_airflow_providers_http.egg-info/SOURCES.txt` & `apache-airflow-providers-http-4.3.0rc1/apache_airflow_providers_http.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-http-4.3.0/pyproject.toml` & `apache-airflow-providers-http-4.3.0rc1/pyproject.toml`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-http-4.3.0/setup.cfg` & `apache-airflow-providers-http-4.3.0rc1/setup.cfg`

 * *Files 1% similar despite different names*

```diff
@@ -55,10 +55,10 @@
 apache_airflow_provider = 
 	provider_info=airflow.providers.http.get_provider_info:get_provider_info
 
 [files]
 packages = airflow.providers.http
 
 [egg_info]
-tag_build = 
+tag_build = rc1
 tag_date = 0
```

### Comparing `apache-airflow-providers-http-4.3.0/setup.py` & `apache-airflow-providers-http-4.3.0rc1/setup.py`

 * *Files identical despite different names*

