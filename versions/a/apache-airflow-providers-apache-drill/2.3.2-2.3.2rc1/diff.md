# Comparing `tmp/apache-airflow-providers-apache-drill-2.3.2.tar.gz` & `tmp/apache-airflow-providers-apache-drill-2.3.2rc1.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "dist/apache-airflow-providers-apache-drill-2.3.2.tar", last modified: Sun Apr  2 05:38:09 2023, max compression
+gzip compressed data, was "dist/apache-airflow-providers-apache-drill-2.3.2rc1.tar", last modified: Sun Apr  2 05:46:57 2023, max compression
```

## Comparing `apache-airflow-providers-apache-drill-2.3.2.tar` & `apache-airflow-providers-apache-drill-2.3.2rc1.tar`

### file list

```diff
@@ -1,29 +1,29 @@
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-02 05:38:09.000000 apache-airflow-providers-apache-drill-2.3.2/
--rw-r--r--   0 root         (0) root         (0)    10850 2023-02-24 18:43:54.000000 apache-airflow-providers-apache-drill-2.3.2/LICENSE
--rw-r--r--   0 root         (0) root         (0)     1122 2023-04-02 05:38:07.000000 apache-airflow-providers-apache-drill-2.3.2/MANIFEST.in
--rw-r--r--   0 root         (0) root         (0)      240 2023-02-24 18:43:54.000000 apache-airflow-providers-apache-drill-2.3.2/NOTICE
--rw-r--r--   0 root         (0) root         (0)    10080 2023-04-02 05:38:09.000000 apache-airflow-providers-apache-drill-2.3.2/PKG-INFO
--rw-r--r--   0 root         (0) root         (0)     8511 2023-04-02 05:38:07.000000 apache-airflow-providers-apache-drill-2.3.2/README.rst
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-02 05:38:09.000000 apache-airflow-providers-apache-drill-2.3.2/airflow/
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-02 05:38:09.000000 apache-airflow-providers-apache-drill-2.3.2/airflow/providers/
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-02 05:38:09.000000 apache-airflow-providers-apache-drill-2.3.2/airflow/providers/apache/
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-02 05:38:09.000000 apache-airflow-providers-apache-drill-2.3.2/airflow/providers/apache/drill/
--rw-r--r--   0 root         (0) root         (0)      787 2023-02-24 18:43:53.000000 apache-airflow-providers-apache-drill-2.3.2/airflow/providers/apache/drill/__init__.py
--rw-r--r--   0 root         (0) root         (0)     2666 2023-04-02 05:38:07.000000 apache-airflow-providers-apache-drill-2.3.2/airflow/providers/apache/drill/get_provider_info.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-02 05:38:09.000000 apache-airflow-providers-apache-drill-2.3.2/airflow/providers/apache/drill/hooks/
--rw-r--r--   0 root         (0) root         (0)      787 2023-02-24 18:43:53.000000 apache-airflow-providers-apache-drill-2.3.2/airflow/providers/apache/drill/hooks/__init__.py
--rw-r--r--   0 root         (0) root         (0)     3659 2023-03-27 08:32:48.000000 apache-airflow-providers-apache-drill-2.3.2/airflow/providers/apache/drill/hooks/drill.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-02 05:38:09.000000 apache-airflow-providers-apache-drill-2.3.2/airflow/providers/apache/drill/operators/
--rw-r--r--   0 root         (0) root         (0)      787 2023-02-24 18:43:53.000000 apache-airflow-providers-apache-drill-2.3.2/airflow/providers/apache/drill/operators/__init__.py
--rw-r--r--   0 root         (0) root         (0)     2142 2023-02-24 18:43:53.000000 apache-airflow-providers-apache-drill-2.3.2/airflow/providers/apache/drill/operators/drill.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-02 05:38:09.000000 apache-airflow-providers-apache-drill-2.3.2/apache_airflow_providers_apache_drill.egg-info/
--rw-r--r--   0 root         (0) root         (0)    10080 2023-04-02 05:38:09.000000 apache-airflow-providers-apache-drill-2.3.2/apache_airflow_providers_apache_drill.egg-info/PKG-INFO
--rw-r--r--   0 root         (0) root         (0)      792 2023-04-02 05:38:09.000000 apache-airflow-providers-apache-drill-2.3.2/apache_airflow_providers_apache_drill.egg-info/SOURCES.txt
--rw-r--r--   0 root         (0) root         (0)        1 2023-04-02 05:38:09.000000 apache-airflow-providers-apache-drill-2.3.2/apache_airflow_providers_apache_drill.egg-info/dependency_links.txt
--rw-r--r--   0 root         (0) root         (0)      109 2023-04-02 05:38:09.000000 apache-airflow-providers-apache-drill-2.3.2/apache_airflow_providers_apache_drill.egg-info/entry_points.txt
--rw-r--r--   0 root         (0) root         (0)        1 2023-04-02 05:38:09.000000 apache-airflow-providers-apache-drill-2.3.2/apache_airflow_providers_apache_drill.egg-info/not-zip-safe
--rw-r--r--   0 root         (0) root         (0)      139 2023-04-02 05:38:09.000000 apache-airflow-providers-apache-drill-2.3.2/apache_airflow_providers_apache_drill.egg-info/requires.txt
--rw-r--r--   0 root         (0) root         (0)        8 2023-04-02 05:38:09.000000 apache-airflow-providers-apache-drill-2.3.2/apache_airflow_providers_apache_drill.egg-info/top_level.txt
--rw-r--r--   0 root         (0) root         (0)     5393 2023-04-01 16:40:04.000000 apache-airflow-providers-apache-drill-2.3.2/pyproject.toml
--rw-r--r--   0 root         (0) root         (0)     1925 2023-04-02 05:38:09.000000 apache-airflow-providers-apache-drill-2.3.2/setup.cfg
--rw-r--r--   0 root         (0) root         (0)     1563 2023-04-02 05:38:07.000000 apache-airflow-providers-apache-drill-2.3.2/setup.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-02 05:46:57.000000 apache-airflow-providers-apache-drill-2.3.2rc1/
+-rw-r--r--   0 root         (0) root         (0)    10850 2023-02-24 18:43:54.000000 apache-airflow-providers-apache-drill-2.3.2rc1/LICENSE
+-rw-r--r--   0 root         (0) root         (0)     1122 2023-04-02 05:46:55.000000 apache-airflow-providers-apache-drill-2.3.2rc1/MANIFEST.in
+-rw-r--r--   0 root         (0) root         (0)      240 2023-02-24 18:43:54.000000 apache-airflow-providers-apache-drill-2.3.2rc1/NOTICE
+-rw-r--r--   0 root         (0) root         (0)    10086 2023-04-02 05:46:57.000000 apache-airflow-providers-apache-drill-2.3.2rc1/PKG-INFO
+-rw-r--r--   0 root         (0) root         (0)     8514 2023-04-02 05:46:55.000000 apache-airflow-providers-apache-drill-2.3.2rc1/README.rst
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-02 05:46:57.000000 apache-airflow-providers-apache-drill-2.3.2rc1/airflow/
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-02 05:46:57.000000 apache-airflow-providers-apache-drill-2.3.2rc1/airflow/providers/
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-02 05:46:57.000000 apache-airflow-providers-apache-drill-2.3.2rc1/airflow/providers/apache/
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-02 05:46:57.000000 apache-airflow-providers-apache-drill-2.3.2rc1/airflow/providers/apache/drill/
+-rw-r--r--   0 root         (0) root         (0)      787 2023-02-24 18:43:53.000000 apache-airflow-providers-apache-drill-2.3.2rc1/airflow/providers/apache/drill/__init__.py
+-rw-r--r--   0 root         (0) root         (0)     2666 2023-04-02 05:46:55.000000 apache-airflow-providers-apache-drill-2.3.2rc1/airflow/providers/apache/drill/get_provider_info.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-02 05:46:57.000000 apache-airflow-providers-apache-drill-2.3.2rc1/airflow/providers/apache/drill/hooks/
+-rw-r--r--   0 root         (0) root         (0)      787 2023-02-24 18:43:53.000000 apache-airflow-providers-apache-drill-2.3.2rc1/airflow/providers/apache/drill/hooks/__init__.py
+-rw-r--r--   0 root         (0) root         (0)     3659 2023-03-27 08:32:48.000000 apache-airflow-providers-apache-drill-2.3.2rc1/airflow/providers/apache/drill/hooks/drill.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-02 05:46:57.000000 apache-airflow-providers-apache-drill-2.3.2rc1/airflow/providers/apache/drill/operators/
+-rw-r--r--   0 root         (0) root         (0)      787 2023-02-24 18:43:53.000000 apache-airflow-providers-apache-drill-2.3.2rc1/airflow/providers/apache/drill/operators/__init__.py
+-rw-r--r--   0 root         (0) root         (0)     2142 2023-02-24 18:43:53.000000 apache-airflow-providers-apache-drill-2.3.2rc1/airflow/providers/apache/drill/operators/drill.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-02 05:46:57.000000 apache-airflow-providers-apache-drill-2.3.2rc1/apache_airflow_providers_apache_drill.egg-info/
+-rw-r--r--   0 root         (0) root         (0)    10086 2023-04-02 05:46:56.000000 apache-airflow-providers-apache-drill-2.3.2rc1/apache_airflow_providers_apache_drill.egg-info/PKG-INFO
+-rw-r--r--   0 root         (0) root         (0)      792 2023-04-02 05:46:57.000000 apache-airflow-providers-apache-drill-2.3.2rc1/apache_airflow_providers_apache_drill.egg-info/SOURCES.txt
+-rw-r--r--   0 root         (0) root         (0)        1 2023-04-02 05:46:57.000000 apache-airflow-providers-apache-drill-2.3.2rc1/apache_airflow_providers_apache_drill.egg-info/dependency_links.txt
+-rw-r--r--   0 root         (0) root         (0)      109 2023-04-02 05:46:57.000000 apache-airflow-providers-apache-drill-2.3.2rc1/apache_airflow_providers_apache_drill.egg-info/entry_points.txt
+-rw-r--r--   0 root         (0) root         (0)        1 2023-04-02 05:46:56.000000 apache-airflow-providers-apache-drill-2.3.2rc1/apache_airflow_providers_apache_drill.egg-info/not-zip-safe
+-rw-r--r--   0 root         (0) root         (0)      149 2023-04-02 05:46:57.000000 apache-airflow-providers-apache-drill-2.3.2rc1/apache_airflow_providers_apache_drill.egg-info/requires.txt
+-rw-r--r--   0 root         (0) root         (0)        8 2023-04-02 05:46:57.000000 apache-airflow-providers-apache-drill-2.3.2rc1/apache_airflow_providers_apache_drill.egg-info/top_level.txt
+-rw-r--r--   0 root         (0) root         (0)     5393 2023-04-01 16:40:04.000000 apache-airflow-providers-apache-drill-2.3.2rc1/pyproject.toml
+-rw-r--r--   0 root         (0) root         (0)     1938 2023-04-02 05:46:57.000000 apache-airflow-providers-apache-drill-2.3.2rc1/setup.cfg
+-rw-r--r--   0 root         (0) root         (0)     1563 2023-04-02 05:46:55.000000 apache-airflow-providers-apache-drill-2.3.2rc1/setup.py
```

### Comparing `apache-airflow-providers-apache-drill-2.3.2/LICENSE` & `apache-airflow-providers-apache-drill-2.3.2rc1/LICENSE`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-apache-drill-2.3.2/MANIFEST.in` & `apache-airflow-providers-apache-drill-2.3.2rc1/MANIFEST.in`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-apache-drill-2.3.2/PKG-INFO` & `apache-airflow-providers-apache-drill-2.3.2rc1/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: apache-airflow-providers-apache-drill
-Version: 2.3.2
+Version: 2.3.2rc1
 Summary: Provider for Apache Airflow. Implements apache-airflow-providers-apache-drill package
 Home-page: https://airflow.apache.org/
 Download-URL: https://archive.apache.org/dist/airflow/providers
 Author: Apache Software Foundation
 Author-email: dev@airflow.apache.org
 License: Apache License 2.0
 Project-URL: Documentation, https://airflow.apache.org/docs/apache-airflow-providers-apache-drill/2.3.2/
@@ -49,15 +49,15 @@
    KIND, either express or implied.  See the License for the
    specific language governing permissions and limitations
    under the License.
 
 
 Package ``apache-airflow-providers-apache-drill``
 
-Release: ``2.3.2``
+Release: ``2.3.2rc1``
 
 
 `Apache Drill <https://drill.apache.org/>`__.
 
 
 Provider package
 ----------------
```

### Comparing `apache-airflow-providers-apache-drill-2.3.2/README.rst` & `apache-airflow-providers-apache-drill-2.3.2rc1/README.rst`

 * *Files 1% similar despite different names*

```diff
@@ -15,15 +15,15 @@
    KIND, either express or implied.  See the License for the
    specific language governing permissions and limitations
    under the License.
 
 
 Package ``apache-airflow-providers-apache-drill``
 
-Release: ``2.3.2``
+Release: ``2.3.2rc1``
 
 
 `Apache Drill <https://drill.apache.org/>`__.
 
 
 Provider package
 ----------------
```

### Comparing `apache-airflow-providers-apache-drill-2.3.2/airflow/providers/apache/drill/__init__.py` & `apache-airflow-providers-apache-drill-2.3.2rc1/airflow/providers/apache/drill/__init__.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-apache-drill-2.3.2/airflow/providers/apache/drill/get_provider_info.py` & `apache-airflow-providers-apache-drill-2.3.2rc1/airflow/providers/apache/drill/get_provider_info.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-apache-drill-2.3.2/airflow/providers/apache/drill/hooks/__init__.py` & `apache-airflow-providers-apache-drill-2.3.2rc1/airflow/providers/apache/drill/hooks/__init__.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-apache-drill-2.3.2/airflow/providers/apache/drill/hooks/drill.py` & `apache-airflow-providers-apache-drill-2.3.2rc1/airflow/providers/apache/drill/hooks/drill.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-apache-drill-2.3.2/airflow/providers/apache/drill/operators/__init__.py` & `apache-airflow-providers-apache-drill-2.3.2rc1/airflow/providers/apache/drill/operators/__init__.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-apache-drill-2.3.2/airflow/providers/apache/drill/operators/drill.py` & `apache-airflow-providers-apache-drill-2.3.2rc1/airflow/providers/apache/drill/operators/drill.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-apache-drill-2.3.2/apache_airflow_providers_apache_drill.egg-info/PKG-INFO` & `apache-airflow-providers-apache-drill-2.3.2rc1/apache_airflow_providers_apache_drill.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: apache-airflow-providers-apache-drill
-Version: 2.3.2
+Version: 2.3.2rc1
 Summary: Provider for Apache Airflow. Implements apache-airflow-providers-apache-drill package
 Home-page: https://airflow.apache.org/
 Download-URL: https://archive.apache.org/dist/airflow/providers
 Author: Apache Software Foundation
 Author-email: dev@airflow.apache.org
 License: Apache License 2.0
 Project-URL: Documentation, https://airflow.apache.org/docs/apache-airflow-providers-apache-drill/2.3.2/
@@ -49,15 +49,15 @@
    KIND, either express or implied.  See the License for the
    specific language governing permissions and limitations
    under the License.
 
 
 Package ``apache-airflow-providers-apache-drill``
 
-Release: ``2.3.2``
+Release: ``2.3.2rc1``
 
 
 `Apache Drill <https://drill.apache.org/>`__.
 
 
 Provider package
 ----------------
```

### Comparing `apache-airflow-providers-apache-drill-2.3.2/apache_airflow_providers_apache_drill.egg-info/SOURCES.txt` & `apache-airflow-providers-apache-drill-2.3.2rc1/apache_airflow_providers_apache_drill.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-apache-drill-2.3.2/pyproject.toml` & `apache-airflow-providers-apache-drill-2.3.2rc1/pyproject.toml`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-apache-drill-2.3.2/setup.cfg` & `apache-airflow-providers-apache-drill-2.3.2rc1/setup.cfg`

 * *Files 10% similar despite different names*

```diff
@@ -42,22 +42,22 @@
 include_package_data = True
 python_requires = ~=3.7
 packages = find:
 setup_requires = 
 	setuptools
 	wheel
 install_requires = 
-	apache-airflow-providers-common-sql>=1.3.1
-	apache-airflow>=2.3.0
+	apache-airflow-providers-common-sql>=1.3.1.dev0
+	apache-airflow>=2.3.0.dev0
 	sqlalchemy-drill>=1.1.0
 
 [options.entry_points]
 apache_airflow_provider = 
 	provider_info=airflow.providers.apache.drill.get_provider_info:get_provider_info
 
 [files]
 packages = airflow.providers.apache.drill
 
 [egg_info]
-tag_build = 
+tag_build = rc1
 tag_date = 0
```

### Comparing `apache-airflow-providers-apache-drill-2.3.2/setup.py` & `apache-airflow-providers-apache-drill-2.3.2rc1/setup.py`

 * *Files identical despite different names*

