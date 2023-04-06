# Comparing `tmp/apache-airflow-providers-hashicorp-3.3.1.tar.gz` & `tmp/apache-airflow-providers-hashicorp-3.3.1rc1.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "dist/apache-airflow-providers-hashicorp-3.3.1.tar", last modified: Sun Apr  2 05:40:00 2023, max compression
+gzip compressed data, was "dist/apache-airflow-providers-hashicorp-3.3.1rc1.tar", last modified: Sun Apr  2 05:48:46 2023, max compression
```

## Comparing `apache-airflow-providers-hashicorp-3.3.1.tar` & `apache-airflow-providers-hashicorp-3.3.1rc1.tar`

### file list

```diff
@@ -1,31 +1,31 @@
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-02 05:40:00.000000 apache-airflow-providers-hashicorp-3.3.1/
--rw-r--r--   0 root         (0) root         (0)    10850 2023-02-24 18:43:54.000000 apache-airflow-providers-hashicorp-3.3.1/LICENSE
--rw-r--r--   0 root         (0) root         (0)     1122 2023-04-02 05:39:56.000000 apache-airflow-providers-hashicorp-3.3.1/MANIFEST.in
--rw-r--r--   0 root         (0) root         (0)      240 2023-02-24 18:43:54.000000 apache-airflow-providers-hashicorp-3.3.1/NOTICE
--rw-r--r--   0 root         (0) root         (0)    11708 2023-04-02 05:40:00.000000 apache-airflow-providers-hashicorp-3.3.1/PKG-INFO
--rw-r--r--   0 root         (0) root         (0)    10152 2023-04-02 05:39:56.000000 apache-airflow-providers-hashicorp-3.3.1/README.rst
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-02 05:40:00.000000 apache-airflow-providers-hashicorp-3.3.1/airflow/
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-02 05:40:00.000000 apache-airflow-providers-hashicorp-3.3.1/airflow/providers/
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-02 05:40:00.000000 apache-airflow-providers-hashicorp-3.3.1/airflow/providers/hashicorp/
--rw-r--r--   0 root         (0) root         (0)      785 2023-02-24 18:43:53.000000 apache-airflow-providers-hashicorp-3.3.1/airflow/providers/hashicorp/__init__.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-02 05:40:00.000000 apache-airflow-providers-hashicorp-3.3.1/airflow/providers/hashicorp/_internal_client/
--rw-r--r--   0 root         (0) root         (0)      785 2023-02-24 18:43:53.000000 apache-airflow-providers-hashicorp-3.3.1/airflow/providers/hashicorp/_internal_client/__init__.py
--rw-r--r--   0 root         (0) root         (0)    20535 2023-02-24 18:43:53.000000 apache-airflow-providers-hashicorp-3.3.1/airflow/providers/hashicorp/_internal_client/vault_client.py
--rw-r--r--   0 root         (0) root         (0)     2474 2023-04-02 05:39:56.000000 apache-airflow-providers-hashicorp-3.3.1/airflow/providers/hashicorp/get_provider_info.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-02 05:40:00.000000 apache-airflow-providers-hashicorp-3.3.1/airflow/providers/hashicorp/hooks/
--rw-r--r--   0 root         (0) root         (0)      785 2023-02-24 18:43:53.000000 apache-airflow-providers-hashicorp-3.3.1/airflow/providers/hashicorp/hooks/__init__.py
--rw-r--r--   0 root         (0) root         (0)    18653 2023-03-16 20:46:35.000000 apache-airflow-providers-hashicorp-3.3.1/airflow/providers/hashicorp/hooks/vault.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-02 05:40:00.000000 apache-airflow-providers-hashicorp-3.3.1/airflow/providers/hashicorp/secrets/
--rw-r--r--   0 root         (0) root         (0)      785 2023-02-24 18:43:53.000000 apache-airflow-providers-hashicorp-3.3.1/airflow/providers/hashicorp/secrets/__init__.py
--rw-r--r--   0 root         (0) root         (0)    11906 2023-03-06 20:52:28.000000 apache-airflow-providers-hashicorp-3.3.1/airflow/providers/hashicorp/secrets/vault.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-02 05:40:00.000000 apache-airflow-providers-hashicorp-3.3.1/apache_airflow_providers_hashicorp.egg-info/
--rw-r--r--   0 root         (0) root         (0)    11708 2023-04-02 05:40:00.000000 apache-airflow-providers-hashicorp-3.3.1/apache_airflow_providers_hashicorp.egg-info/PKG-INFO
--rw-r--r--   0 root         (0) root         (0)      867 2023-04-02 05:40:00.000000 apache-airflow-providers-hashicorp-3.3.1/apache_airflow_providers_hashicorp.egg-info/SOURCES.txt
--rw-r--r--   0 root         (0) root         (0)        1 2023-04-02 05:40:00.000000 apache-airflow-providers-hashicorp-3.3.1/apache_airflow_providers_hashicorp.egg-info/dependency_links.txt
--rw-r--r--   0 root         (0) root         (0)      106 2023-04-02 05:40:00.000000 apache-airflow-providers-hashicorp-3.3.1/apache_airflow_providers_hashicorp.egg-info/entry_points.txt
--rw-r--r--   0 root         (0) root         (0)        1 2023-04-02 05:40:00.000000 apache-airflow-providers-hashicorp-3.3.1/apache_airflow_providers_hashicorp.egg-info/not-zip-safe
--rw-r--r--   0 root         (0) root         (0)       75 2023-04-02 05:40:00.000000 apache-airflow-providers-hashicorp-3.3.1/apache_airflow_providers_hashicorp.egg-info/requires.txt
--rw-r--r--   0 root         (0) root         (0)        8 2023-04-02 05:40:00.000000 apache-airflow-providers-hashicorp-3.3.1/apache_airflow_providers_hashicorp.egg-info/top_level.txt
--rw-r--r--   0 root         (0) root         (0)     5393 2023-04-01 16:40:04.000000 apache-airflow-providers-hashicorp-3.3.1/pyproject.toml
--rw-r--r--   0 root         (0) root         (0)     1850 2023-04-02 05:40:00.000000 apache-airflow-providers-hashicorp-3.3.1/setup.cfg
--rw-r--r--   0 root         (0) root         (0)     1543 2023-04-02 05:39:56.000000 apache-airflow-providers-hashicorp-3.3.1/setup.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-02 05:48:46.000000 apache-airflow-providers-hashicorp-3.3.1rc1/
+-rw-r--r--   0 root         (0) root         (0)    10850 2023-02-24 18:43:54.000000 apache-airflow-providers-hashicorp-3.3.1rc1/LICENSE
+-rw-r--r--   0 root         (0) root         (0)     1122 2023-04-02 05:48:42.000000 apache-airflow-providers-hashicorp-3.3.1rc1/MANIFEST.in
+-rw-r--r--   0 root         (0) root         (0)      240 2023-02-24 18:43:54.000000 apache-airflow-providers-hashicorp-3.3.1rc1/NOTICE
+-rw-r--r--   0 root         (0) root         (0)    11714 2023-04-02 05:48:46.000000 apache-airflow-providers-hashicorp-3.3.1rc1/PKG-INFO
+-rw-r--r--   0 root         (0) root         (0)    10155 2023-04-02 05:48:42.000000 apache-airflow-providers-hashicorp-3.3.1rc1/README.rst
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-02 05:48:46.000000 apache-airflow-providers-hashicorp-3.3.1rc1/airflow/
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-02 05:48:46.000000 apache-airflow-providers-hashicorp-3.3.1rc1/airflow/providers/
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-02 05:48:46.000000 apache-airflow-providers-hashicorp-3.3.1rc1/airflow/providers/hashicorp/
+-rw-r--r--   0 root         (0) root         (0)      785 2023-02-24 18:43:53.000000 apache-airflow-providers-hashicorp-3.3.1rc1/airflow/providers/hashicorp/__init__.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-02 05:48:46.000000 apache-airflow-providers-hashicorp-3.3.1rc1/airflow/providers/hashicorp/_internal_client/
+-rw-r--r--   0 root         (0) root         (0)      785 2023-02-24 18:43:53.000000 apache-airflow-providers-hashicorp-3.3.1rc1/airflow/providers/hashicorp/_internal_client/__init__.py
+-rw-r--r--   0 root         (0) root         (0)    20535 2023-02-24 18:43:53.000000 apache-airflow-providers-hashicorp-3.3.1rc1/airflow/providers/hashicorp/_internal_client/vault_client.py
+-rw-r--r--   0 root         (0) root         (0)     2474 2023-04-02 05:48:42.000000 apache-airflow-providers-hashicorp-3.3.1rc1/airflow/providers/hashicorp/get_provider_info.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-02 05:48:46.000000 apache-airflow-providers-hashicorp-3.3.1rc1/airflow/providers/hashicorp/hooks/
+-rw-r--r--   0 root         (0) root         (0)      785 2023-02-24 18:43:53.000000 apache-airflow-providers-hashicorp-3.3.1rc1/airflow/providers/hashicorp/hooks/__init__.py
+-rw-r--r--   0 root         (0) root         (0)    18653 2023-03-16 20:46:35.000000 apache-airflow-providers-hashicorp-3.3.1rc1/airflow/providers/hashicorp/hooks/vault.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-02 05:48:46.000000 apache-airflow-providers-hashicorp-3.3.1rc1/airflow/providers/hashicorp/secrets/
+-rw-r--r--   0 root         (0) root         (0)      785 2023-02-24 18:43:53.000000 apache-airflow-providers-hashicorp-3.3.1rc1/airflow/providers/hashicorp/secrets/__init__.py
+-rw-r--r--   0 root         (0) root         (0)    11906 2023-03-06 20:52:28.000000 apache-airflow-providers-hashicorp-3.3.1rc1/airflow/providers/hashicorp/secrets/vault.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-02 05:48:46.000000 apache-airflow-providers-hashicorp-3.3.1rc1/apache_airflow_providers_hashicorp.egg-info/
+-rw-r--r--   0 root         (0) root         (0)    11714 2023-04-02 05:48:46.000000 apache-airflow-providers-hashicorp-3.3.1rc1/apache_airflow_providers_hashicorp.egg-info/PKG-INFO
+-rw-r--r--   0 root         (0) root         (0)      867 2023-04-02 05:48:46.000000 apache-airflow-providers-hashicorp-3.3.1rc1/apache_airflow_providers_hashicorp.egg-info/SOURCES.txt
+-rw-r--r--   0 root         (0) root         (0)        1 2023-04-02 05:48:46.000000 apache-airflow-providers-hashicorp-3.3.1rc1/apache_airflow_providers_hashicorp.egg-info/dependency_links.txt
+-rw-r--r--   0 root         (0) root         (0)      106 2023-04-02 05:48:46.000000 apache-airflow-providers-hashicorp-3.3.1rc1/apache_airflow_providers_hashicorp.egg-info/entry_points.txt
+-rw-r--r--   0 root         (0) root         (0)        1 2023-04-02 05:48:46.000000 apache-airflow-providers-hashicorp-3.3.1rc1/apache_airflow_providers_hashicorp.egg-info/not-zip-safe
+-rw-r--r--   0 root         (0) root         (0)       80 2023-04-02 05:48:46.000000 apache-airflow-providers-hashicorp-3.3.1rc1/apache_airflow_providers_hashicorp.egg-info/requires.txt
+-rw-r--r--   0 root         (0) root         (0)        8 2023-04-02 05:48:46.000000 apache-airflow-providers-hashicorp-3.3.1rc1/apache_airflow_providers_hashicorp.egg-info/top_level.txt
+-rw-r--r--   0 root         (0) root         (0)     5393 2023-04-01 16:40:04.000000 apache-airflow-providers-hashicorp-3.3.1rc1/pyproject.toml
+-rw-r--r--   0 root         (0) root         (0)     1858 2023-04-02 05:48:46.000000 apache-airflow-providers-hashicorp-3.3.1rc1/setup.cfg
+-rw-r--r--   0 root         (0) root         (0)     1543 2023-04-02 05:48:42.000000 apache-airflow-providers-hashicorp-3.3.1rc1/setup.py
```

### Comparing `apache-airflow-providers-hashicorp-3.3.1/LICENSE` & `apache-airflow-providers-hashicorp-3.3.1rc1/LICENSE`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-hashicorp-3.3.1/MANIFEST.in` & `apache-airflow-providers-hashicorp-3.3.1rc1/MANIFEST.in`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-hashicorp-3.3.1/PKG-INFO` & `apache-airflow-providers-hashicorp-3.3.1rc1/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: apache-airflow-providers-hashicorp
-Version: 3.3.1
+Version: 3.3.1rc1
 Summary: Provider for Apache Airflow. Implements apache-airflow-providers-hashicorp package
 Home-page: https://airflow.apache.org/
 Download-URL: https://archive.apache.org/dist/airflow/providers
 Author: Apache Software Foundation
 Author-email: dev@airflow.apache.org
 License: Apache License 2.0
 Project-URL: Documentation, https://airflow.apache.org/docs/apache-airflow-providers-hashicorp/3.3.1/
@@ -49,15 +49,15 @@
    KIND, either express or implied.  See the License for the
    specific language governing permissions and limitations
    under the License.
 
 
 Package ``apache-airflow-providers-hashicorp``
 
-Release: ``3.3.1``
+Release: ``3.3.1rc1``
 
 
 Hashicorp including `Hashicorp Vault <https://www.vaultproject.io/>`__
 
 
 Provider package
 ----------------
```

### Comparing `apache-airflow-providers-hashicorp-3.3.1/README.rst` & `apache-airflow-providers-hashicorp-3.3.1rc1/README.rst`

 * *Files 0% similar despite different names*

```diff
@@ -15,15 +15,15 @@
    KIND, either express or implied.  See the License for the
    specific language governing permissions and limitations
    under the License.
 
 
 Package ``apache-airflow-providers-hashicorp``
 
-Release: ``3.3.1``
+Release: ``3.3.1rc1``
 
 
 Hashicorp including `Hashicorp Vault <https://www.vaultproject.io/>`__
 
 
 Provider package
 ----------------
```

### Comparing `apache-airflow-providers-hashicorp-3.3.1/airflow/providers/hashicorp/__init__.py` & `apache-airflow-providers-hashicorp-3.3.1rc1/airflow/providers/hashicorp/__init__.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-hashicorp-3.3.1/airflow/providers/hashicorp/_internal_client/__init__.py` & `apache-airflow-providers-hashicorp-3.3.1rc1/airflow/providers/hashicorp/_internal_client/__init__.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-hashicorp-3.3.1/airflow/providers/hashicorp/_internal_client/vault_client.py` & `apache-airflow-providers-hashicorp-3.3.1rc1/airflow/providers/hashicorp/_internal_client/vault_client.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-hashicorp-3.3.1/airflow/providers/hashicorp/get_provider_info.py` & `apache-airflow-providers-hashicorp-3.3.1rc1/airflow/providers/hashicorp/get_provider_info.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-hashicorp-3.3.1/airflow/providers/hashicorp/hooks/__init__.py` & `apache-airflow-providers-hashicorp-3.3.1rc1/airflow/providers/hashicorp/hooks/__init__.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-hashicorp-3.3.1/airflow/providers/hashicorp/hooks/vault.py` & `apache-airflow-providers-hashicorp-3.3.1rc1/airflow/providers/hashicorp/hooks/vault.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-hashicorp-3.3.1/airflow/providers/hashicorp/secrets/__init__.py` & `apache-airflow-providers-hashicorp-3.3.1rc1/airflow/providers/hashicorp/secrets/__init__.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-hashicorp-3.3.1/airflow/providers/hashicorp/secrets/vault.py` & `apache-airflow-providers-hashicorp-3.3.1rc1/airflow/providers/hashicorp/secrets/vault.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-hashicorp-3.3.1/apache_airflow_providers_hashicorp.egg-info/PKG-INFO` & `apache-airflow-providers-hashicorp-3.3.1rc1/apache_airflow_providers_hashicorp.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: apache-airflow-providers-hashicorp
-Version: 3.3.1
+Version: 3.3.1rc1
 Summary: Provider for Apache Airflow. Implements apache-airflow-providers-hashicorp package
 Home-page: https://airflow.apache.org/
 Download-URL: https://archive.apache.org/dist/airflow/providers
 Author: Apache Software Foundation
 Author-email: dev@airflow.apache.org
 License: Apache License 2.0
 Project-URL: Documentation, https://airflow.apache.org/docs/apache-airflow-providers-hashicorp/3.3.1/
@@ -49,15 +49,15 @@
    KIND, either express or implied.  See the License for the
    specific language governing permissions and limitations
    under the License.
 
 
 Package ``apache-airflow-providers-hashicorp``
 
-Release: ``3.3.1``
+Release: ``3.3.1rc1``
 
 
 Hashicorp including `Hashicorp Vault <https://www.vaultproject.io/>`__
 
 
 Provider package
 ----------------
```

### Comparing `apache-airflow-providers-hashicorp-3.3.1/apache_airflow_providers_hashicorp.egg-info/SOURCES.txt` & `apache-airflow-providers-hashicorp-3.3.1rc1/apache_airflow_providers_hashicorp.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-hashicorp-3.3.1/pyproject.toml` & `apache-airflow-providers-hashicorp-3.3.1rc1/pyproject.toml`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-hashicorp-3.3.1/setup.cfg` & `apache-airflow-providers-hashicorp-3.3.1rc1/setup.cfg`

 * *Files 2% similar despite different names*

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
 	hvac>=0.10
 
 [options.entry_points]
 apache_airflow_provider = 
 	provider_info=airflow.providers.hashicorp.get_provider_info:get_provider_info
 
 [files]
 packages = airflow.providers.hashicorp
 
 [egg_info]
-tag_build = 
+tag_build = rc1
 tag_date = 0
```

### Comparing `apache-airflow-providers-hashicorp-3.3.1/setup.py` & `apache-airflow-providers-hashicorp-3.3.1rc1/setup.py`

 * *Files identical despite different names*

