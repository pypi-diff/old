# Comparing `tmp/apache-airflow-providers-ssh-3.6.0.tar.gz` & `tmp/apache-airflow-providers-ssh-3.6.0rc1.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "dist/apache-airflow-providers-ssh-3.6.0.tar", last modified: Sun Apr  2 05:40:32 2023, max compression
+gzip compressed data, was "dist/apache-airflow-providers-ssh-3.6.0rc1.tar", last modified: Sun Apr  2 05:49:20 2023, max compression
```

## Comparing `apache-airflow-providers-ssh-3.6.0.tar` & `apache-airflow-providers-ssh-3.6.0rc1.tar`

### file list

```diff
@@ -1,28 +1,28 @@
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-02 05:40:31.000000 apache-airflow-providers-ssh-3.6.0/
--rw-r--r--   0 root         (0) root         (0)    10850 2023-02-24 18:43:54.000000 apache-airflow-providers-ssh-3.6.0/LICENSE
--rw-r--r--   0 root         (0) root         (0)     1122 2023-04-02 05:40:30.000000 apache-airflow-providers-ssh-3.6.0/MANIFEST.in
--rw-r--r--   0 root         (0) root         (0)      240 2023-02-24 18:43:54.000000 apache-airflow-providers-ssh-3.6.0/NOTICE
--rw-r--r--   0 root         (0) root         (0)    12611 2023-04-02 05:40:31.000000 apache-airflow-providers-ssh-3.6.0/PKG-INFO
--rw-r--r--   0 root         (0) root         (0)    11096 2023-04-02 05:40:30.000000 apache-airflow-providers-ssh-3.6.0/README.rst
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-02 05:40:31.000000 apache-airflow-providers-ssh-3.6.0/airflow/
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-02 05:40:31.000000 apache-airflow-providers-ssh-3.6.0/airflow/providers/
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-02 05:40:31.000000 apache-airflow-providers-ssh-3.6.0/airflow/providers/ssh/
--rw-r--r--   0 root         (0) root         (0)      787 2023-02-24 18:43:53.000000 apache-airflow-providers-ssh-3.6.0/airflow/providers/ssh/__init__.py
--rw-r--r--   0 root         (0) root         (0)     2570 2023-04-02 05:40:30.000000 apache-airflow-providers-ssh-3.6.0/airflow/providers/ssh/get_provider_info.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-02 05:40:31.000000 apache-airflow-providers-ssh-3.6.0/airflow/providers/ssh/hooks/
--rw-r--r--   0 root         (0) root         (0)      787 2023-02-24 18:43:53.000000 apache-airflow-providers-ssh-3.6.0/airflow/providers/ssh/hooks/__init__.py
--rw-r--r--   0 root         (0) root         (0)    22439 2023-03-27 08:32:49.000000 apache-airflow-providers-ssh-3.6.0/airflow/providers/ssh/hooks/ssh.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-02 05:40:31.000000 apache-airflow-providers-ssh-3.6.0/airflow/providers/ssh/operators/
--rw-r--r--   0 root         (0) root         (0)      787 2023-02-24 18:43:53.000000 apache-airflow-providers-ssh-3.6.0/airflow/providers/ssh/operators/__init__.py
--rw-r--r--   0 root         (0) root         (0)     7667 2023-03-27 08:32:49.000000 apache-airflow-providers-ssh-3.6.0/airflow/providers/ssh/operators/ssh.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-02 05:40:31.000000 apache-airflow-providers-ssh-3.6.0/apache_airflow_providers_ssh.egg-info/
--rw-r--r--   0 root         (0) root         (0)    12611 2023-04-02 05:40:31.000000 apache-airflow-providers-ssh-3.6.0/apache_airflow_providers_ssh.egg-info/PKG-INFO
--rw-r--r--   0 root         (0) root         (0)      671 2023-04-02 05:40:31.000000 apache-airflow-providers-ssh-3.6.0/apache_airflow_providers_ssh.egg-info/SOURCES.txt
--rw-r--r--   0 root         (0) root         (0)        1 2023-04-02 05:40:31.000000 apache-airflow-providers-ssh-3.6.0/apache_airflow_providers_ssh.egg-info/dependency_links.txt
--rw-r--r--   0 root         (0) root         (0)      100 2023-04-02 05:40:31.000000 apache-airflow-providers-ssh-3.6.0/apache_airflow_providers_ssh.egg-info/entry_points.txt
--rw-r--r--   0 root         (0) root         (0)        1 2023-04-02 05:40:31.000000 apache-airflow-providers-ssh-3.6.0/apache_airflow_providers_ssh.egg-info/not-zip-safe
--rw-r--r--   0 root         (0) root         (0)       55 2023-04-02 05:40:31.000000 apache-airflow-providers-ssh-3.6.0/apache_airflow_providers_ssh.egg-info/requires.txt
--rw-r--r--   0 root         (0) root         (0)        8 2023-04-02 05:40:31.000000 apache-airflow-providers-ssh-3.6.0/apache_airflow_providers_ssh.egg-info/top_level.txt
--rw-r--r--   0 root         (0) root         (0)     5393 2023-04-01 16:40:04.000000 apache-airflow-providers-ssh-3.6.0/pyproject.toml
--rw-r--r--   0 root         (0) root         (0)     1837 2023-04-02 05:40:32.000000 apache-airflow-providers-ssh-3.6.0/setup.cfg
--rw-r--r--   0 root         (0) root         (0)     1452 2023-04-02 05:40:30.000000 apache-airflow-providers-ssh-3.6.0/setup.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-02 05:49:20.000000 apache-airflow-providers-ssh-3.6.0rc1/
+-rw-r--r--   0 root         (0) root         (0)    10850 2023-02-24 18:43:54.000000 apache-airflow-providers-ssh-3.6.0rc1/LICENSE
+-rw-r--r--   0 root         (0) root         (0)     1122 2023-04-02 05:49:18.000000 apache-airflow-providers-ssh-3.6.0rc1/MANIFEST.in
+-rw-r--r--   0 root         (0) root         (0)      240 2023-02-24 18:43:54.000000 apache-airflow-providers-ssh-3.6.0rc1/NOTICE
+-rw-r--r--   0 root         (0) root         (0)    12617 2023-04-02 05:49:20.000000 apache-airflow-providers-ssh-3.6.0rc1/PKG-INFO
+-rw-r--r--   0 root         (0) root         (0)    11099 2023-04-02 05:49:18.000000 apache-airflow-providers-ssh-3.6.0rc1/README.rst
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-02 05:49:20.000000 apache-airflow-providers-ssh-3.6.0rc1/airflow/
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-02 05:49:20.000000 apache-airflow-providers-ssh-3.6.0rc1/airflow/providers/
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-02 05:49:20.000000 apache-airflow-providers-ssh-3.6.0rc1/airflow/providers/ssh/
+-rw-r--r--   0 root         (0) root         (0)      787 2023-02-24 18:43:53.000000 apache-airflow-providers-ssh-3.6.0rc1/airflow/providers/ssh/__init__.py
+-rw-r--r--   0 root         (0) root         (0)     2570 2023-04-02 05:49:18.000000 apache-airflow-providers-ssh-3.6.0rc1/airflow/providers/ssh/get_provider_info.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-02 05:49:20.000000 apache-airflow-providers-ssh-3.6.0rc1/airflow/providers/ssh/hooks/
+-rw-r--r--   0 root         (0) root         (0)      787 2023-02-24 18:43:53.000000 apache-airflow-providers-ssh-3.6.0rc1/airflow/providers/ssh/hooks/__init__.py
+-rw-r--r--   0 root         (0) root         (0)    22439 2023-03-27 08:32:49.000000 apache-airflow-providers-ssh-3.6.0rc1/airflow/providers/ssh/hooks/ssh.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-02 05:49:20.000000 apache-airflow-providers-ssh-3.6.0rc1/airflow/providers/ssh/operators/
+-rw-r--r--   0 root         (0) root         (0)      787 2023-02-24 18:43:53.000000 apache-airflow-providers-ssh-3.6.0rc1/airflow/providers/ssh/operators/__init__.py
+-rw-r--r--   0 root         (0) root         (0)     7667 2023-03-27 08:32:49.000000 apache-airflow-providers-ssh-3.6.0rc1/airflow/providers/ssh/operators/ssh.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-02 05:49:20.000000 apache-airflow-providers-ssh-3.6.0rc1/apache_airflow_providers_ssh.egg-info/
+-rw-r--r--   0 root         (0) root         (0)    12617 2023-04-02 05:49:19.000000 apache-airflow-providers-ssh-3.6.0rc1/apache_airflow_providers_ssh.egg-info/PKG-INFO
+-rw-r--r--   0 root         (0) root         (0)      671 2023-04-02 05:49:19.000000 apache-airflow-providers-ssh-3.6.0rc1/apache_airflow_providers_ssh.egg-info/SOURCES.txt
+-rw-r--r--   0 root         (0) root         (0)        1 2023-04-02 05:49:19.000000 apache-airflow-providers-ssh-3.6.0rc1/apache_airflow_providers_ssh.egg-info/dependency_links.txt
+-rw-r--r--   0 root         (0) root         (0)      100 2023-04-02 05:49:19.000000 apache-airflow-providers-ssh-3.6.0rc1/apache_airflow_providers_ssh.egg-info/entry_points.txt
+-rw-r--r--   0 root         (0) root         (0)        1 2023-04-02 05:49:19.000000 apache-airflow-providers-ssh-3.6.0rc1/apache_airflow_providers_ssh.egg-info/not-zip-safe
+-rw-r--r--   0 root         (0) root         (0)       60 2023-04-02 05:49:19.000000 apache-airflow-providers-ssh-3.6.0rc1/apache_airflow_providers_ssh.egg-info/requires.txt
+-rw-r--r--   0 root         (0) root         (0)        8 2023-04-02 05:49:19.000000 apache-airflow-providers-ssh-3.6.0rc1/apache_airflow_providers_ssh.egg-info/top_level.txt
+-rw-r--r--   0 root         (0) root         (0)     5393 2023-04-01 16:40:04.000000 apache-airflow-providers-ssh-3.6.0rc1/pyproject.toml
+-rw-r--r--   0 root         (0) root         (0)     1845 2023-04-02 05:49:20.000000 apache-airflow-providers-ssh-3.6.0rc1/setup.cfg
+-rw-r--r--   0 root         (0) root         (0)     1452 2023-04-02 05:49:18.000000 apache-airflow-providers-ssh-3.6.0rc1/setup.py
```

### Comparing `apache-airflow-providers-ssh-3.6.0/LICENSE` & `apache-airflow-providers-ssh-3.6.0rc1/LICENSE`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-ssh-3.6.0/MANIFEST.in` & `apache-airflow-providers-ssh-3.6.0rc1/MANIFEST.in`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-ssh-3.6.0/PKG-INFO` & `apache-airflow-providers-ssh-3.6.0rc1/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: apache-airflow-providers-ssh
-Version: 3.6.0
+Version: 3.6.0rc1
 Summary: Provider for Apache Airflow. Implements apache-airflow-providers-ssh package
 Home-page: https://airflow.apache.org/
 Download-URL: https://archive.apache.org/dist/airflow/providers
 Author: Apache Software Foundation
 Author-email: dev@airflow.apache.org
 License: Apache License 2.0
 Project-URL: Documentation, https://airflow.apache.org/docs/apache-airflow-providers-ssh/3.6.0/
@@ -48,15 +48,15 @@
    KIND, either express or implied.  See the License for the
    specific language governing permissions and limitations
    under the License.
 
 
 Package ``apache-airflow-providers-ssh``
 
-Release: ``3.6.0``
+Release: ``3.6.0rc1``
 
 
 `Secure Shell (SSH) <https://tools.ietf.org/html/rfc4251>`__
 
 
 Provider package
 ----------------
```

### Comparing `apache-airflow-providers-ssh-3.6.0/README.rst` & `apache-airflow-providers-ssh-3.6.0rc1/README.rst`

 * *Files 0% similar despite different names*

```diff
@@ -15,15 +15,15 @@
    KIND, either express or implied.  See the License for the
    specific language governing permissions and limitations
    under the License.
 
 
 Package ``apache-airflow-providers-ssh``
 
-Release: ``3.6.0``
+Release: ``3.6.0rc1``
 
 
 `Secure Shell (SSH) <https://tools.ietf.org/html/rfc4251>`__
 
 
 Provider package
 ----------------
```

### Comparing `apache-airflow-providers-ssh-3.6.0/airflow/providers/ssh/__init__.py` & `apache-airflow-providers-ssh-3.6.0rc1/airflow/providers/ssh/__init__.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-ssh-3.6.0/airflow/providers/ssh/get_provider_info.py` & `apache-airflow-providers-ssh-3.6.0rc1/airflow/providers/ssh/get_provider_info.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-ssh-3.6.0/airflow/providers/ssh/hooks/__init__.py` & `apache-airflow-providers-ssh-3.6.0rc1/airflow/providers/ssh/hooks/__init__.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-ssh-3.6.0/airflow/providers/ssh/hooks/ssh.py` & `apache-airflow-providers-ssh-3.6.0rc1/airflow/providers/ssh/hooks/ssh.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-ssh-3.6.0/airflow/providers/ssh/operators/__init__.py` & `apache-airflow-providers-ssh-3.6.0rc1/airflow/providers/ssh/operators/__init__.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-ssh-3.6.0/airflow/providers/ssh/operators/ssh.py` & `apache-airflow-providers-ssh-3.6.0rc1/airflow/providers/ssh/operators/ssh.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-ssh-3.6.0/apache_airflow_providers_ssh.egg-info/PKG-INFO` & `apache-airflow-providers-ssh-3.6.0rc1/apache_airflow_providers_ssh.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: apache-airflow-providers-ssh
-Version: 3.6.0
+Version: 3.6.0rc1
 Summary: Provider for Apache Airflow. Implements apache-airflow-providers-ssh package
 Home-page: https://airflow.apache.org/
 Download-URL: https://archive.apache.org/dist/airflow/providers
 Author: Apache Software Foundation
 Author-email: dev@airflow.apache.org
 License: Apache License 2.0
 Project-URL: Documentation, https://airflow.apache.org/docs/apache-airflow-providers-ssh/3.6.0/
@@ -48,15 +48,15 @@
    KIND, either express or implied.  See the License for the
    specific language governing permissions and limitations
    under the License.
 
 
 Package ``apache-airflow-providers-ssh``
 
-Release: ``3.6.0``
+Release: ``3.6.0rc1``
 
 
 `Secure Shell (SSH) <https://tools.ietf.org/html/rfc4251>`__
 
 
 Provider package
 ----------------
```

### Comparing `apache-airflow-providers-ssh-3.6.0/apache_airflow_providers_ssh.egg-info/SOURCES.txt` & `apache-airflow-providers-ssh-3.6.0rc1/apache_airflow_providers_ssh.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-ssh-3.6.0/pyproject.toml` & `apache-airflow-providers-ssh-3.6.0rc1/pyproject.toml`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-ssh-3.6.0/setup.cfg` & `apache-airflow-providers-ssh-3.6.0rc1/setup.cfg`

 * *Files 7% similar despite different names*

```diff
@@ -42,22 +42,22 @@
 include_package_data = True
 python_requires = ~=3.7
 packages = find:
 setup_requires = 
 	setuptools
 	wheel
 install_requires = 
-	apache-airflow>=2.3.0
+	apache-airflow>=2.3.0.dev0
 	paramiko>=2.6.0
 	sshtunnel>=0.3.2
 
 [options.entry_points]
 apache_airflow_provider = 
 	provider_info=airflow.providers.ssh.get_provider_info:get_provider_info
 
 [files]
 packages = airflow.providers.ssh
 
 [egg_info]
-tag_build = 
+tag_build = rc1
 tag_date = 0
```

### Comparing `apache-airflow-providers-ssh-3.6.0/setup.py` & `apache-airflow-providers-ssh-3.6.0rc1/setup.py`

 * *Files identical despite different names*

