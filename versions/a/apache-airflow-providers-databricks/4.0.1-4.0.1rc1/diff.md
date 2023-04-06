# Comparing `tmp/apache-airflow-providers-databricks-4.0.1.tar.gz` & `tmp/apache-airflow-providers-databricks-4.0.1rc1.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "dist/apache-airflow-providers-databricks-4.0.1.tar", last modified: Sun Apr  2 05:38:38 2023, max compression
+gzip compressed data, was "dist/apache-airflow-providers-databricks-4.0.1rc1.tar", last modified: Sun Apr  2 05:47:26 2023, max compression
```

## Comparing `apache-airflow-providers-databricks-4.0.1.tar` & `apache-airflow-providers-databricks-4.0.1rc1.tar`

### file list

```diff
@@ -1,38 +1,38 @@
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-02 05:38:38.000000 apache-airflow-providers-databricks-4.0.1/
--rw-r--r--   0 root         (0) root         (0)    10850 2023-02-24 18:43:54.000000 apache-airflow-providers-databricks-4.0.1/LICENSE
--rw-r--r--   0 root         (0) root         (0)     1122 2023-04-02 05:38:36.000000 apache-airflow-providers-databricks-4.0.1/MANIFEST.in
--rw-r--r--   0 root         (0) root         (0)      240 2023-02-24 18:43:54.000000 apache-airflow-providers-databricks-4.0.1/NOTICE
--rw-r--r--   0 root         (0) root         (0)    18449 2023-04-02 05:38:38.000000 apache-airflow-providers-databricks-4.0.1/PKG-INFO
--rw-r--r--   0 root         (0) root         (0)    16886 2023-04-02 05:38:36.000000 apache-airflow-providers-databricks-4.0.1/README.rst
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-02 05:38:38.000000 apache-airflow-providers-databricks-4.0.1/airflow/
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-02 05:38:38.000000 apache-airflow-providers-databricks-4.0.1/airflow/providers/
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-02 05:38:38.000000 apache-airflow-providers-databricks-4.0.1/airflow/providers/databricks/
--rw-r--r--   0 root         (0) root         (0)      787 2023-02-24 18:43:53.000000 apache-airflow-providers-databricks-4.0.1/airflow/providers/databricks/__init__.py
--rw-r--r--   0 root         (0) root         (0)     5094 2023-04-02 05:38:36.000000 apache-airflow-providers-databricks-4.0.1/airflow/providers/databricks/get_provider_info.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-02 05:38:38.000000 apache-airflow-providers-databricks-4.0.1/airflow/providers/databricks/hooks/
--rw-r--r--   0 root         (0) root         (0)      787 2023-02-24 18:43:53.000000 apache-airflow-providers-databricks-4.0.1/airflow/providers/databricks/hooks/__init__.py
--rw-r--r--   0 root         (0) root         (0)    15815 2023-02-24 18:43:53.000000 apache-airflow-providers-databricks-4.0.1/airflow/providers/databricks/hooks/databricks.py
--rw-r--r--   0 root         (0) root         (0)    26704 2023-02-24 18:43:53.000000 apache-airflow-providers-databricks-4.0.1/airflow/providers/databricks/hooks/databricks_base.py
--rw-r--r--   0 root         (0) root         (0)     9278 2023-02-24 18:43:53.000000 apache-airflow-providers-databricks-4.0.1/airflow/providers/databricks/hooks/databricks_sql.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-02 05:38:38.000000 apache-airflow-providers-databricks-4.0.1/airflow/providers/databricks/operators/
--rw-r--r--   0 root         (0) root         (0)      787 2023-02-24 18:43:53.000000 apache-airflow-providers-databricks-4.0.1/airflow/providers/databricks/operators/__init__.py
--rw-r--r--   0 root         (0) root         (0)    31391 2023-03-10 19:31:58.000000 apache-airflow-providers-databricks-4.0.1/airflow/providers/databricks/operators/databricks.py
--rw-r--r--   0 root         (0) root         (0)    13226 2023-02-24 18:43:53.000000 apache-airflow-providers-databricks-4.0.1/airflow/providers/databricks/operators/databricks_repos.py
--rw-r--r--   0 root         (0) root         (0)    16679 2023-02-24 18:43:53.000000 apache-airflow-providers-databricks-4.0.1/airflow/providers/databricks/operators/databricks_sql.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-02 05:38:38.000000 apache-airflow-providers-databricks-4.0.1/airflow/providers/databricks/triggers/
--rw-r--r--   0 root         (0) root         (0)      787 2023-02-24 18:43:53.000000 apache-airflow-providers-databricks-4.0.1/airflow/providers/databricks/triggers/__init__.py
--rw-r--r--   0 root         (0) root         (0)     2811 2023-02-24 18:43:53.000000 apache-airflow-providers-databricks-4.0.1/airflow/providers/databricks/triggers/databricks.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-02 05:38:38.000000 apache-airflow-providers-databricks-4.0.1/airflow/providers/databricks/utils/
--rw-r--r--   0 root         (0) root         (0)      785 2023-02-24 18:43:53.000000 apache-airflow-providers-databricks-4.0.1/airflow/providers/databricks/utils/__init__.py
--rw-r--r--   0 root         (0) root         (0)     2909 2023-02-24 18:43:53.000000 apache-airflow-providers-databricks-4.0.1/airflow/providers/databricks/utils/databricks.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-02 05:38:38.000000 apache-airflow-providers-databricks-4.0.1/apache_airflow_providers_databricks.egg-info/
--rw-r--r--   0 root         (0) root         (0)    18449 2023-04-02 05:38:38.000000 apache-airflow-providers-databricks-4.0.1/apache_airflow_providers_databricks.egg-info/PKG-INFO
--rw-r--r--   0 root         (0) root         (0)     1197 2023-04-02 05:38:38.000000 apache-airflow-providers-databricks-4.0.1/apache_airflow_providers_databricks.egg-info/SOURCES.txt
--rw-r--r--   0 root         (0) root         (0)        1 2023-04-02 05:38:38.000000 apache-airflow-providers-databricks-4.0.1/apache_airflow_providers_databricks.egg-info/dependency_links.txt
--rw-r--r--   0 root         (0) root         (0)      107 2023-04-02 05:38:38.000000 apache-airflow-providers-databricks-4.0.1/apache_airflow_providers_databricks.egg-info/entry_points.txt
--rw-r--r--   0 root         (0) root         (0)        1 2023-04-02 05:38:38.000000 apache-airflow-providers-databricks-4.0.1/apache_airflow_providers_databricks.egg-info/not-zip-safe
--rw-r--r--   0 root         (0) root         (0)      190 2023-04-02 05:38:38.000000 apache-airflow-providers-databricks-4.0.1/apache_airflow_providers_databricks.egg-info/requires.txt
--rw-r--r--   0 root         (0) root         (0)        8 2023-04-02 05:38:38.000000 apache-airflow-providers-databricks-4.0.1/apache_airflow_providers_databricks.egg-info/top_level.txt
--rw-r--r--   0 root         (0) root         (0)     5393 2023-04-01 16:40:04.000000 apache-airflow-providers-databricks-4.0.1/pyproject.toml
--rw-r--r--   0 root         (0) root         (0)     1968 2023-04-02 05:38:38.000000 apache-airflow-providers-databricks-4.0.1/setup.cfg
--rw-r--r--   0 root         (0) root         (0)     1555 2023-04-02 05:38:36.000000 apache-airflow-providers-databricks-4.0.1/setup.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-02 05:47:26.000000 apache-airflow-providers-databricks-4.0.1rc1/
+-rw-r--r--   0 root         (0) root         (0)    10850 2023-02-24 18:43:54.000000 apache-airflow-providers-databricks-4.0.1rc1/LICENSE
+-rw-r--r--   0 root         (0) root         (0)     1122 2023-04-02 05:47:24.000000 apache-airflow-providers-databricks-4.0.1rc1/MANIFEST.in
+-rw-r--r--   0 root         (0) root         (0)      240 2023-02-24 18:43:54.000000 apache-airflow-providers-databricks-4.0.1rc1/NOTICE
+-rw-r--r--   0 root         (0) root         (0)    18455 2023-04-02 05:47:26.000000 apache-airflow-providers-databricks-4.0.1rc1/PKG-INFO
+-rw-r--r--   0 root         (0) root         (0)    16889 2023-04-02 05:47:24.000000 apache-airflow-providers-databricks-4.0.1rc1/README.rst
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-02 05:47:26.000000 apache-airflow-providers-databricks-4.0.1rc1/airflow/
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-02 05:47:26.000000 apache-airflow-providers-databricks-4.0.1rc1/airflow/providers/
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-02 05:47:26.000000 apache-airflow-providers-databricks-4.0.1rc1/airflow/providers/databricks/
+-rw-r--r--   0 root         (0) root         (0)      787 2023-02-24 18:43:53.000000 apache-airflow-providers-databricks-4.0.1rc1/airflow/providers/databricks/__init__.py
+-rw-r--r--   0 root         (0) root         (0)     5094 2023-04-02 05:47:24.000000 apache-airflow-providers-databricks-4.0.1rc1/airflow/providers/databricks/get_provider_info.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-02 05:47:26.000000 apache-airflow-providers-databricks-4.0.1rc1/airflow/providers/databricks/hooks/
+-rw-r--r--   0 root         (0) root         (0)      787 2023-02-24 18:43:53.000000 apache-airflow-providers-databricks-4.0.1rc1/airflow/providers/databricks/hooks/__init__.py
+-rw-r--r--   0 root         (0) root         (0)    15815 2023-02-24 18:43:53.000000 apache-airflow-providers-databricks-4.0.1rc1/airflow/providers/databricks/hooks/databricks.py
+-rw-r--r--   0 root         (0) root         (0)    26704 2023-02-24 18:43:53.000000 apache-airflow-providers-databricks-4.0.1rc1/airflow/providers/databricks/hooks/databricks_base.py
+-rw-r--r--   0 root         (0) root         (0)     9278 2023-02-24 18:43:53.000000 apache-airflow-providers-databricks-4.0.1rc1/airflow/providers/databricks/hooks/databricks_sql.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-02 05:47:26.000000 apache-airflow-providers-databricks-4.0.1rc1/airflow/providers/databricks/operators/
+-rw-r--r--   0 root         (0) root         (0)      787 2023-02-24 18:43:53.000000 apache-airflow-providers-databricks-4.0.1rc1/airflow/providers/databricks/operators/__init__.py
+-rw-r--r--   0 root         (0) root         (0)    31391 2023-03-10 19:31:58.000000 apache-airflow-providers-databricks-4.0.1rc1/airflow/providers/databricks/operators/databricks.py
+-rw-r--r--   0 root         (0) root         (0)    13226 2023-02-24 18:43:53.000000 apache-airflow-providers-databricks-4.0.1rc1/airflow/providers/databricks/operators/databricks_repos.py
+-rw-r--r--   0 root         (0) root         (0)    16679 2023-02-24 18:43:53.000000 apache-airflow-providers-databricks-4.0.1rc1/airflow/providers/databricks/operators/databricks_sql.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-02 05:47:26.000000 apache-airflow-providers-databricks-4.0.1rc1/airflow/providers/databricks/triggers/
+-rw-r--r--   0 root         (0) root         (0)      787 2023-02-24 18:43:53.000000 apache-airflow-providers-databricks-4.0.1rc1/airflow/providers/databricks/triggers/__init__.py
+-rw-r--r--   0 root         (0) root         (0)     2811 2023-02-24 18:43:53.000000 apache-airflow-providers-databricks-4.0.1rc1/airflow/providers/databricks/triggers/databricks.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-02 05:47:26.000000 apache-airflow-providers-databricks-4.0.1rc1/airflow/providers/databricks/utils/
+-rw-r--r--   0 root         (0) root         (0)      785 2023-02-24 18:43:53.000000 apache-airflow-providers-databricks-4.0.1rc1/airflow/providers/databricks/utils/__init__.py
+-rw-r--r--   0 root         (0) root         (0)     2909 2023-02-24 18:43:53.000000 apache-airflow-providers-databricks-4.0.1rc1/airflow/providers/databricks/utils/databricks.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-02 05:47:26.000000 apache-airflow-providers-databricks-4.0.1rc1/apache_airflow_providers_databricks.egg-info/
+-rw-r--r--   0 root         (0) root         (0)    18455 2023-04-02 05:47:25.000000 apache-airflow-providers-databricks-4.0.1rc1/apache_airflow_providers_databricks.egg-info/PKG-INFO
+-rw-r--r--   0 root         (0) root         (0)     1197 2023-04-02 05:47:26.000000 apache-airflow-providers-databricks-4.0.1rc1/apache_airflow_providers_databricks.egg-info/SOURCES.txt
+-rw-r--r--   0 root         (0) root         (0)        1 2023-04-02 05:47:25.000000 apache-airflow-providers-databricks-4.0.1rc1/apache_airflow_providers_databricks.egg-info/dependency_links.txt
+-rw-r--r--   0 root         (0) root         (0)      107 2023-04-02 05:47:26.000000 apache-airflow-providers-databricks-4.0.1rc1/apache_airflow_providers_databricks.egg-info/entry_points.txt
+-rw-r--r--   0 root         (0) root         (0)        1 2023-04-02 05:47:25.000000 apache-airflow-providers-databricks-4.0.1rc1/apache_airflow_providers_databricks.egg-info/not-zip-safe
+-rw-r--r--   0 root         (0) root         (0)      200 2023-04-02 05:47:26.000000 apache-airflow-providers-databricks-4.0.1rc1/apache_airflow_providers_databricks.egg-info/requires.txt
+-rw-r--r--   0 root         (0) root         (0)        8 2023-04-02 05:47:26.000000 apache-airflow-providers-databricks-4.0.1rc1/apache_airflow_providers_databricks.egg-info/top_level.txt
+-rw-r--r--   0 root         (0) root         (0)     5393 2023-04-01 16:40:04.000000 apache-airflow-providers-databricks-4.0.1rc1/pyproject.toml
+-rw-r--r--   0 root         (0) root         (0)     1981 2023-04-02 05:47:26.000000 apache-airflow-providers-databricks-4.0.1rc1/setup.cfg
+-rw-r--r--   0 root         (0) root         (0)     1555 2023-04-02 05:47:24.000000 apache-airflow-providers-databricks-4.0.1rc1/setup.py
```

### Comparing `apache-airflow-providers-databricks-4.0.1/LICENSE` & `apache-airflow-providers-databricks-4.0.1rc1/LICENSE`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-databricks-4.0.1/MANIFEST.in` & `apache-airflow-providers-databricks-4.0.1rc1/MANIFEST.in`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-databricks-4.0.1/PKG-INFO` & `apache-airflow-providers-databricks-4.0.1rc1/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: apache-airflow-providers-databricks
-Version: 4.0.1
+Version: 4.0.1rc1
 Summary: Provider for Apache Airflow. Implements apache-airflow-providers-databricks package
 Home-page: https://airflow.apache.org/
 Download-URL: https://archive.apache.org/dist/airflow/providers
 Author: Apache Software Foundation
 Author-email: dev@airflow.apache.org
 License: Apache License 2.0
 Project-URL: Documentation, https://airflow.apache.org/docs/apache-airflow-providers-databricks/4.0.1/
@@ -49,15 +49,15 @@
    KIND, either express or implied.  See the License for the
    specific language governing permissions and limitations
    under the License.
 
 
 Package ``apache-airflow-providers-databricks``
 
-Release: ``4.0.1``
+Release: ``4.0.1rc1``
 
 
 `Databricks <https://databricks.com/>`__
 
 
 Provider package
 ----------------
```

### Comparing `apache-airflow-providers-databricks-4.0.1/README.rst` & `apache-airflow-providers-databricks-4.0.1rc1/README.rst`

 * *Files 0% similar despite different names*

```diff
@@ -15,15 +15,15 @@
    KIND, either express or implied.  See the License for the
    specific language governing permissions and limitations
    under the License.
 
 
 Package ``apache-airflow-providers-databricks``
 
-Release: ``4.0.1``
+Release: ``4.0.1rc1``
 
 
 `Databricks <https://databricks.com/>`__
 
 
 Provider package
 ----------------
```

### Comparing `apache-airflow-providers-databricks-4.0.1/airflow/providers/databricks/__init__.py` & `apache-airflow-providers-databricks-4.0.1rc1/airflow/providers/databricks/__init__.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-databricks-4.0.1/airflow/providers/databricks/get_provider_info.py` & `apache-airflow-providers-databricks-4.0.1rc1/airflow/providers/databricks/get_provider_info.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-databricks-4.0.1/airflow/providers/databricks/hooks/__init__.py` & `apache-airflow-providers-databricks-4.0.1rc1/airflow/providers/databricks/hooks/__init__.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-databricks-4.0.1/airflow/providers/databricks/hooks/databricks.py` & `apache-airflow-providers-databricks-4.0.1rc1/airflow/providers/databricks/hooks/databricks.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-databricks-4.0.1/airflow/providers/databricks/hooks/databricks_base.py` & `apache-airflow-providers-databricks-4.0.1rc1/airflow/providers/databricks/hooks/databricks_base.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-databricks-4.0.1/airflow/providers/databricks/hooks/databricks_sql.py` & `apache-airflow-providers-databricks-4.0.1rc1/airflow/providers/databricks/hooks/databricks_sql.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-databricks-4.0.1/airflow/providers/databricks/operators/__init__.py` & `apache-airflow-providers-databricks-4.0.1rc1/airflow/providers/databricks/operators/__init__.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-databricks-4.0.1/airflow/providers/databricks/operators/databricks.py` & `apache-airflow-providers-databricks-4.0.1rc1/airflow/providers/databricks/operators/databricks.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-databricks-4.0.1/airflow/providers/databricks/operators/databricks_repos.py` & `apache-airflow-providers-databricks-4.0.1rc1/airflow/providers/databricks/operators/databricks_repos.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-databricks-4.0.1/airflow/providers/databricks/operators/databricks_sql.py` & `apache-airflow-providers-databricks-4.0.1rc1/airflow/providers/databricks/operators/databricks_sql.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-databricks-4.0.1/airflow/providers/databricks/triggers/__init__.py` & `apache-airflow-providers-databricks-4.0.1rc1/airflow/providers/databricks/triggers/__init__.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-databricks-4.0.1/airflow/providers/databricks/triggers/databricks.py` & `apache-airflow-providers-databricks-4.0.1rc1/airflow/providers/databricks/triggers/databricks.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-databricks-4.0.1/airflow/providers/databricks/utils/__init__.py` & `apache-airflow-providers-databricks-4.0.1rc1/airflow/providers/databricks/utils/__init__.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-databricks-4.0.1/airflow/providers/databricks/utils/databricks.py` & `apache-airflow-providers-databricks-4.0.1rc1/airflow/providers/databricks/utils/databricks.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-databricks-4.0.1/apache_airflow_providers_databricks.egg-info/PKG-INFO` & `apache-airflow-providers-databricks-4.0.1rc1/apache_airflow_providers_databricks.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: apache-airflow-providers-databricks
-Version: 4.0.1
+Version: 4.0.1rc1
 Summary: Provider for Apache Airflow. Implements apache-airflow-providers-databricks package
 Home-page: https://airflow.apache.org/
 Download-URL: https://archive.apache.org/dist/airflow/providers
 Author: Apache Software Foundation
 Author-email: dev@airflow.apache.org
 License: Apache License 2.0
 Project-URL: Documentation, https://airflow.apache.org/docs/apache-airflow-providers-databricks/4.0.1/
@@ -49,15 +49,15 @@
    KIND, either express or implied.  See the License for the
    specific language governing permissions and limitations
    under the License.
 
 
 Package ``apache-airflow-providers-databricks``
 
-Release: ``4.0.1``
+Release: ``4.0.1rc1``
 
 
 `Databricks <https://databricks.com/>`__
 
 
 Provider package
 ----------------
```

### Comparing `apache-airflow-providers-databricks-4.0.1/apache_airflow_providers_databricks.egg-info/SOURCES.txt` & `apache-airflow-providers-databricks-4.0.1rc1/apache_airflow_providers_databricks.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-databricks-4.0.1/pyproject.toml` & `apache-airflow-providers-databricks-4.0.1rc1/pyproject.toml`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-databricks-4.0.1/setup.cfg` & `apache-airflow-providers-databricks-4.0.1rc1/setup.cfg`

 * *Files 5% similar despite different names*

```diff
@@ -43,23 +43,23 @@
 python_requires = ~=3.7
 packages = find:
 setup_requires = 
 	setuptools
 	wheel
 install_requires = 
 	aiohttp>=3.6.3, <4
-	apache-airflow-providers-common-sql>=1.3.1
-	apache-airflow>=2.3.0
+	apache-airflow-providers-common-sql>=1.3.1.dev0
+	apache-airflow>=2.3.0.dev0
 	databricks-sql-connector>=2.0.0, <3.0.0
 	requests>=2.27,<3
 
 [options.entry_points]
 apache_airflow_provider = 
 	provider_info=airflow.providers.databricks.get_provider_info:get_provider_info
 
 [files]
 packages = airflow.providers.databricks
 
 [egg_info]
-tag_build = 
+tag_build = rc1
 tag_date = 0
```

### Comparing `apache-airflow-providers-databricks-4.0.1/setup.py` & `apache-airflow-providers-databricks-4.0.1rc1/setup.py`

 * *Files identical despite different names*

