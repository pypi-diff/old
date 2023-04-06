# Comparing `tmp/apache-airflow-providers-cncf-kubernetes-5.3.0.tar.gz` & `tmp/apache-airflow-providers-cncf-kubernetes-5.3.0rc1.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "dist/apache-airflow-providers-cncf-kubernetes-5.3.0.tar", last modified: Sun Apr  2 05:38:32 2023, max compression
+gzip compressed data, was "dist/apache-airflow-providers-cncf-kubernetes-5.3.0rc1.tar", last modified: Sun Apr  2 05:47:20 2023, max compression
```

## Comparing `apache-airflow-providers-cncf-kubernetes-5.3.0.tar` & `apache-airflow-providers-cncf-kubernetes-5.3.0rc1.tar`

### file list

```diff
@@ -1,50 +1,50 @@
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-02 05:38:32.000000 apache-airflow-providers-cncf-kubernetes-5.3.0/
--rw-r--r--   0 root         (0) root         (0)    10850 2023-02-24 18:43:54.000000 apache-airflow-providers-cncf-kubernetes-5.3.0/LICENSE
--rw-r--r--   0 root         (0) root         (0)     1174 2023-04-02 05:38:30.000000 apache-airflow-providers-cncf-kubernetes-5.3.0/MANIFEST.in
--rw-r--r--   0 root         (0) root         (0)      240 2023-02-24 18:43:54.000000 apache-airflow-providers-cncf-kubernetes-5.3.0/NOTICE
--rw-r--r--   0 root         (0) root         (0)    31892 2023-04-02 05:38:32.000000 apache-airflow-providers-cncf-kubernetes-5.3.0/PKG-INFO
--rw-r--r--   0 root         (0) root         (0)    30341 2023-04-02 05:38:30.000000 apache-airflow-providers-cncf-kubernetes-5.3.0/README.rst
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-02 05:38:32.000000 apache-airflow-providers-cncf-kubernetes-5.3.0/airflow/
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-02 05:38:32.000000 apache-airflow-providers-cncf-kubernetes-5.3.0/airflow/providers/
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-02 05:38:32.000000 apache-airflow-providers-cncf-kubernetes-5.3.0/airflow/providers/cncf/
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-02 05:38:32.000000 apache-airflow-providers-cncf-kubernetes-5.3.0/airflow/providers/cncf/kubernetes/
--rw-r--r--   0 root         (0) root         (0)      787 2023-02-24 18:43:53.000000 apache-airflow-providers-cncf-kubernetes-5.3.0/airflow/providers/cncf/kubernetes/__init__.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-02 05:38:32.000000 apache-airflow-providers-cncf-kubernetes-5.3.0/airflow/providers/cncf/kubernetes/backcompat/
--rw-r--r--   0 root         (0) root         (0)      785 2023-02-24 18:43:53.000000 apache-airflow-providers-cncf-kubernetes-5.3.0/airflow/providers/cncf/kubernetes/backcompat/__init__.py
--rw-r--r--   0 root         (0) root         (0)     4081 2023-02-24 18:43:53.000000 apache-airflow-providers-cncf-kubernetes-5.3.0/airflow/providers/cncf/kubernetes/backcompat/backwards_compat_converters.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-02 05:38:32.000000 apache-airflow-providers-cncf-kubernetes-5.3.0/airflow/providers/cncf/kubernetes/decorators/
--rw-r--r--   0 root         (0) root         (0)      787 2023-02-24 18:43:53.000000 apache-airflow-providers-cncf-kubernetes-5.3.0/airflow/providers/cncf/kubernetes/decorators/__init__.py
--rw-r--r--   0 root         (0) root         (0)     6151 2023-03-16 20:46:35.000000 apache-airflow-providers-cncf-kubernetes-5.3.0/airflow/providers/cncf/kubernetes/decorators/kubernetes.py
--rw-r--r--   0 root         (0) root         (0)     4274 2023-04-02 05:38:30.000000 apache-airflow-providers-cncf-kubernetes-5.3.0/airflow/providers/cncf/kubernetes/get_provider_info.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-02 05:38:32.000000 apache-airflow-providers-cncf-kubernetes-5.3.0/airflow/providers/cncf/kubernetes/hooks/
--rw-r--r--   0 root         (0) root         (0)      785 2023-02-24 18:43:53.000000 apache-airflow-providers-cncf-kubernetes-5.3.0/airflow/providers/cncf/kubernetes/hooks/__init__.py
--rw-r--r--   0 root         (0) root         (0)    23391 2023-03-15 08:58:48.000000 apache-airflow-providers-cncf-kubernetes-5.3.0/airflow/providers/cncf/kubernetes/hooks/kubernetes.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-02 05:38:32.000000 apache-airflow-providers-cncf-kubernetes-5.3.0/airflow/providers/cncf/kubernetes/operators/
--rw-r--r--   0 root         (0) root         (0)      787 2023-02-24 18:43:53.000000 apache-airflow-providers-cncf-kubernetes-5.3.0/airflow/providers/cncf/kubernetes/operators/__init__.py
--rw-r--r--   0 root         (0) root         (0)     1074 2023-03-06 20:52:28.000000 apache-airflow-providers-cncf-kubernetes-5.3.0/airflow/providers/cncf/kubernetes/operators/kubernetes_pod.py
--rw-r--r--   0 root         (0) root         (0)    37484 2023-03-12 11:08:42.000000 apache-airflow-providers-cncf-kubernetes-5.3.0/airflow/providers/cncf/kubernetes/operators/pod.py
--rw-r--r--   0 root         (0) root         (0)     4860 2023-03-15 08:58:48.000000 apache-airflow-providers-cncf-kubernetes-5.3.0/airflow/providers/cncf/kubernetes/operators/spark_kubernetes.py
--rw-r--r--   0 root         (0) root         (0)     1741 2023-02-24 18:43:53.000000 apache-airflow-providers-cncf-kubernetes-5.3.0/airflow/providers/cncf/kubernetes/python_kubernetes_script.jinja2
--rw-r--r--   0 root         (0) root         (0)     3343 2023-03-27 08:32:49.000000 apache-airflow-providers-cncf-kubernetes-5.3.0/airflow/providers/cncf/kubernetes/python_kubernetes_script.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-02 05:38:32.000000 apache-airflow-providers-cncf-kubernetes-5.3.0/airflow/providers/cncf/kubernetes/sensors/
--rw-r--r--   0 root         (0) root         (0)      785 2023-02-24 18:43:53.000000 apache-airflow-providers-cncf-kubernetes-5.3.0/airflow/providers/cncf/kubernetes/sensors/__init__.py
--rw-r--r--   0 root         (0) root         (0)     5226 2023-02-24 18:43:53.000000 apache-airflow-providers-cncf-kubernetes-5.3.0/airflow/providers/cncf/kubernetes/sensors/spark_kubernetes.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-02 05:38:32.000000 apache-airflow-providers-cncf-kubernetes-5.3.0/airflow/providers/cncf/kubernetes/triggers/
--rw-r--r--   0 root         (0) root         (0)      785 2023-02-24 18:43:53.000000 apache-airflow-providers-cncf-kubernetes-5.3.0/airflow/providers/cncf/kubernetes/triggers/__init__.py
--rw-r--r--   0 root         (0) root         (0)     1072 2023-03-06 20:52:28.000000 apache-airflow-providers-cncf-kubernetes-5.3.0/airflow/providers/cncf/kubernetes/triggers/kubernetes_pod.py
--rw-r--r--   0 root         (0) root         (0)    10454 2023-03-06 20:52:28.000000 apache-airflow-providers-cncf-kubernetes-5.3.0/airflow/providers/cncf/kubernetes/triggers/pod.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-02 05:38:32.000000 apache-airflow-providers-cncf-kubernetes-5.3.0/airflow/providers/cncf/kubernetes/utils/
--rw-r--r--   0 root         (0) root         (0)      863 2023-02-24 18:43:53.000000 apache-airflow-providers-cncf-kubernetes-5.3.0/airflow/providers/cncf/kubernetes/utils/__init__.py
--rw-r--r--   0 root         (0) root         (0)    22378 2023-03-10 19:31:58.000000 apache-airflow-providers-cncf-kubernetes-5.3.0/airflow/providers/cncf/kubernetes/utils/pod_manager.py
--rw-r--r--   0 root         (0) root         (0)     2404 2023-02-24 18:43:53.000000 apache-airflow-providers-cncf-kubernetes-5.3.0/airflow/providers/cncf/kubernetes/utils/xcom_sidecar.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-02 05:38:32.000000 apache-airflow-providers-cncf-kubernetes-5.3.0/apache_airflow_providers_cncf_kubernetes.egg-info/
--rw-r--r--   0 root         (0) root         (0)    31892 2023-04-02 05:38:31.000000 apache-airflow-providers-cncf-kubernetes-5.3.0/apache_airflow_providers_cncf_kubernetes.egg-info/PKG-INFO
--rw-r--r--   0 root         (0) root         (0)     1782 2023-04-02 05:38:31.000000 apache-airflow-providers-cncf-kubernetes-5.3.0/apache_airflow_providers_cncf_kubernetes.egg-info/SOURCES.txt
--rw-r--r--   0 root         (0) root         (0)        1 2023-04-02 05:38:31.000000 apache-airflow-providers-cncf-kubernetes-5.3.0/apache_airflow_providers_cncf_kubernetes.egg-info/dependency_links.txt
--rw-r--r--   0 root         (0) root         (0)      112 2023-04-02 05:38:31.000000 apache-airflow-providers-cncf-kubernetes-5.3.0/apache_airflow_providers_cncf_kubernetes.egg-info/entry_points.txt
--rw-r--r--   0 root         (0) root         (0)        1 2023-04-02 05:38:31.000000 apache-airflow-providers-cncf-kubernetes-5.3.0/apache_airflow_providers_cncf_kubernetes.egg-info/not-zip-safe
--rw-r--r--   0 root         (0) root         (0)      112 2023-04-02 05:38:31.000000 apache-airflow-providers-cncf-kubernetes-5.3.0/apache_airflow_providers_cncf_kubernetes.egg-info/requires.txt
--rw-r--r--   0 root         (0) root         (0)        8 2023-04-02 05:38:31.000000 apache-airflow-providers-cncf-kubernetes-5.3.0/apache_airflow_providers_cncf_kubernetes.egg-info/top_level.txt
--rw-r--r--   0 root         (0) root         (0)     5393 2023-04-01 16:40:04.000000 apache-airflow-providers-cncf-kubernetes-5.3.0/pyproject.toml
--rw-r--r--   0 root         (0) root         (0)     1968 2023-04-02 05:38:32.000000 apache-airflow-providers-cncf-kubernetes-5.3.0/setup.cfg
--rw-r--r--   0 root         (0) root         (0)     1522 2023-04-02 05:38:30.000000 apache-airflow-providers-cncf-kubernetes-5.3.0/setup.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-02 05:47:20.000000 apache-airflow-providers-cncf-kubernetes-5.3.0rc1/
+-rw-r--r--   0 root         (0) root         (0)    10850 2023-02-24 18:43:54.000000 apache-airflow-providers-cncf-kubernetes-5.3.0rc1/LICENSE
+-rw-r--r--   0 root         (0) root         (0)     1174 2023-04-02 05:47:18.000000 apache-airflow-providers-cncf-kubernetes-5.3.0rc1/MANIFEST.in
+-rw-r--r--   0 root         (0) root         (0)      240 2023-02-24 18:43:54.000000 apache-airflow-providers-cncf-kubernetes-5.3.0rc1/NOTICE
+-rw-r--r--   0 root         (0) root         (0)    31898 2023-04-02 05:47:20.000000 apache-airflow-providers-cncf-kubernetes-5.3.0rc1/PKG-INFO
+-rw-r--r--   0 root         (0) root         (0)    30344 2023-04-02 05:47:18.000000 apache-airflow-providers-cncf-kubernetes-5.3.0rc1/README.rst
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-02 05:47:20.000000 apache-airflow-providers-cncf-kubernetes-5.3.0rc1/airflow/
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-02 05:47:20.000000 apache-airflow-providers-cncf-kubernetes-5.3.0rc1/airflow/providers/
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-02 05:47:20.000000 apache-airflow-providers-cncf-kubernetes-5.3.0rc1/airflow/providers/cncf/
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-02 05:47:20.000000 apache-airflow-providers-cncf-kubernetes-5.3.0rc1/airflow/providers/cncf/kubernetes/
+-rw-r--r--   0 root         (0) root         (0)      787 2023-02-24 18:43:53.000000 apache-airflow-providers-cncf-kubernetes-5.3.0rc1/airflow/providers/cncf/kubernetes/__init__.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-02 05:47:20.000000 apache-airflow-providers-cncf-kubernetes-5.3.0rc1/airflow/providers/cncf/kubernetes/backcompat/
+-rw-r--r--   0 root         (0) root         (0)      785 2023-02-24 18:43:53.000000 apache-airflow-providers-cncf-kubernetes-5.3.0rc1/airflow/providers/cncf/kubernetes/backcompat/__init__.py
+-rw-r--r--   0 root         (0) root         (0)     4081 2023-02-24 18:43:53.000000 apache-airflow-providers-cncf-kubernetes-5.3.0rc1/airflow/providers/cncf/kubernetes/backcompat/backwards_compat_converters.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-02 05:47:20.000000 apache-airflow-providers-cncf-kubernetes-5.3.0rc1/airflow/providers/cncf/kubernetes/decorators/
+-rw-r--r--   0 root         (0) root         (0)      787 2023-02-24 18:43:53.000000 apache-airflow-providers-cncf-kubernetes-5.3.0rc1/airflow/providers/cncf/kubernetes/decorators/__init__.py
+-rw-r--r--   0 root         (0) root         (0)     6151 2023-03-16 20:46:35.000000 apache-airflow-providers-cncf-kubernetes-5.3.0rc1/airflow/providers/cncf/kubernetes/decorators/kubernetes.py
+-rw-r--r--   0 root         (0) root         (0)     4274 2023-04-02 05:47:18.000000 apache-airflow-providers-cncf-kubernetes-5.3.0rc1/airflow/providers/cncf/kubernetes/get_provider_info.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-02 05:47:20.000000 apache-airflow-providers-cncf-kubernetes-5.3.0rc1/airflow/providers/cncf/kubernetes/hooks/
+-rw-r--r--   0 root         (0) root         (0)      785 2023-02-24 18:43:53.000000 apache-airflow-providers-cncf-kubernetes-5.3.0rc1/airflow/providers/cncf/kubernetes/hooks/__init__.py
+-rw-r--r--   0 root         (0) root         (0)    23391 2023-03-15 08:58:48.000000 apache-airflow-providers-cncf-kubernetes-5.3.0rc1/airflow/providers/cncf/kubernetes/hooks/kubernetes.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-02 05:47:20.000000 apache-airflow-providers-cncf-kubernetes-5.3.0rc1/airflow/providers/cncf/kubernetes/operators/
+-rw-r--r--   0 root         (0) root         (0)      787 2023-02-24 18:43:53.000000 apache-airflow-providers-cncf-kubernetes-5.3.0rc1/airflow/providers/cncf/kubernetes/operators/__init__.py
+-rw-r--r--   0 root         (0) root         (0)     1074 2023-03-06 20:52:28.000000 apache-airflow-providers-cncf-kubernetes-5.3.0rc1/airflow/providers/cncf/kubernetes/operators/kubernetes_pod.py
+-rw-r--r--   0 root         (0) root         (0)    37484 2023-03-12 11:08:42.000000 apache-airflow-providers-cncf-kubernetes-5.3.0rc1/airflow/providers/cncf/kubernetes/operators/pod.py
+-rw-r--r--   0 root         (0) root         (0)     4860 2023-03-15 08:58:48.000000 apache-airflow-providers-cncf-kubernetes-5.3.0rc1/airflow/providers/cncf/kubernetes/operators/spark_kubernetes.py
+-rw-r--r--   0 root         (0) root         (0)     1741 2023-02-24 18:43:53.000000 apache-airflow-providers-cncf-kubernetes-5.3.0rc1/airflow/providers/cncf/kubernetes/python_kubernetes_script.jinja2
+-rw-r--r--   0 root         (0) root         (0)     3343 2023-03-27 08:32:49.000000 apache-airflow-providers-cncf-kubernetes-5.3.0rc1/airflow/providers/cncf/kubernetes/python_kubernetes_script.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-02 05:47:20.000000 apache-airflow-providers-cncf-kubernetes-5.3.0rc1/airflow/providers/cncf/kubernetes/sensors/
+-rw-r--r--   0 root         (0) root         (0)      785 2023-02-24 18:43:53.000000 apache-airflow-providers-cncf-kubernetes-5.3.0rc1/airflow/providers/cncf/kubernetes/sensors/__init__.py
+-rw-r--r--   0 root         (0) root         (0)     5226 2023-02-24 18:43:53.000000 apache-airflow-providers-cncf-kubernetes-5.3.0rc1/airflow/providers/cncf/kubernetes/sensors/spark_kubernetes.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-02 05:47:20.000000 apache-airflow-providers-cncf-kubernetes-5.3.0rc1/airflow/providers/cncf/kubernetes/triggers/
+-rw-r--r--   0 root         (0) root         (0)      785 2023-02-24 18:43:53.000000 apache-airflow-providers-cncf-kubernetes-5.3.0rc1/airflow/providers/cncf/kubernetes/triggers/__init__.py
+-rw-r--r--   0 root         (0) root         (0)     1072 2023-03-06 20:52:28.000000 apache-airflow-providers-cncf-kubernetes-5.3.0rc1/airflow/providers/cncf/kubernetes/triggers/kubernetes_pod.py
+-rw-r--r--   0 root         (0) root         (0)    10454 2023-03-06 20:52:28.000000 apache-airflow-providers-cncf-kubernetes-5.3.0rc1/airflow/providers/cncf/kubernetes/triggers/pod.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-02 05:47:20.000000 apache-airflow-providers-cncf-kubernetes-5.3.0rc1/airflow/providers/cncf/kubernetes/utils/
+-rw-r--r--   0 root         (0) root         (0)      863 2023-02-24 18:43:53.000000 apache-airflow-providers-cncf-kubernetes-5.3.0rc1/airflow/providers/cncf/kubernetes/utils/__init__.py
+-rw-r--r--   0 root         (0) root         (0)    22378 2023-03-10 19:31:58.000000 apache-airflow-providers-cncf-kubernetes-5.3.0rc1/airflow/providers/cncf/kubernetes/utils/pod_manager.py
+-rw-r--r--   0 root         (0) root         (0)     2404 2023-02-24 18:43:53.000000 apache-airflow-providers-cncf-kubernetes-5.3.0rc1/airflow/providers/cncf/kubernetes/utils/xcom_sidecar.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-02 05:47:20.000000 apache-airflow-providers-cncf-kubernetes-5.3.0rc1/apache_airflow_providers_cncf_kubernetes.egg-info/
+-rw-r--r--   0 root         (0) root         (0)    31898 2023-04-02 05:47:19.000000 apache-airflow-providers-cncf-kubernetes-5.3.0rc1/apache_airflow_providers_cncf_kubernetes.egg-info/PKG-INFO
+-rw-r--r--   0 root         (0) root         (0)     1782 2023-04-02 05:47:19.000000 apache-airflow-providers-cncf-kubernetes-5.3.0rc1/apache_airflow_providers_cncf_kubernetes.egg-info/SOURCES.txt
+-rw-r--r--   0 root         (0) root         (0)        1 2023-04-02 05:47:19.000000 apache-airflow-providers-cncf-kubernetes-5.3.0rc1/apache_airflow_providers_cncf_kubernetes.egg-info/dependency_links.txt
+-rw-r--r--   0 root         (0) root         (0)      112 2023-04-02 05:47:19.000000 apache-airflow-providers-cncf-kubernetes-5.3.0rc1/apache_airflow_providers_cncf_kubernetes.egg-info/entry_points.txt
+-rw-r--r--   0 root         (0) root         (0)        1 2023-04-02 05:47:19.000000 apache-airflow-providers-cncf-kubernetes-5.3.0rc1/apache_airflow_providers_cncf_kubernetes.egg-info/not-zip-safe
+-rw-r--r--   0 root         (0) root         (0)      117 2023-04-02 05:47:19.000000 apache-airflow-providers-cncf-kubernetes-5.3.0rc1/apache_airflow_providers_cncf_kubernetes.egg-info/requires.txt
+-rw-r--r--   0 root         (0) root         (0)        8 2023-04-02 05:47:19.000000 apache-airflow-providers-cncf-kubernetes-5.3.0rc1/apache_airflow_providers_cncf_kubernetes.egg-info/top_level.txt
+-rw-r--r--   0 root         (0) root         (0)     5393 2023-04-01 16:40:04.000000 apache-airflow-providers-cncf-kubernetes-5.3.0rc1/pyproject.toml
+-rw-r--r--   0 root         (0) root         (0)     1976 2023-04-02 05:47:20.000000 apache-airflow-providers-cncf-kubernetes-5.3.0rc1/setup.cfg
+-rw-r--r--   0 root         (0) root         (0)     1522 2023-04-02 05:47:18.000000 apache-airflow-providers-cncf-kubernetes-5.3.0rc1/setup.py
```

### Comparing `apache-airflow-providers-cncf-kubernetes-5.3.0/LICENSE` & `apache-airflow-providers-cncf-kubernetes-5.3.0rc1/LICENSE`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-cncf-kubernetes-5.3.0/MANIFEST.in` & `apache-airflow-providers-cncf-kubernetes-5.3.0rc1/MANIFEST.in`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-cncf-kubernetes-5.3.0/PKG-INFO` & `apache-airflow-providers-cncf-kubernetes-5.3.0rc1/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: apache-airflow-providers-cncf-kubernetes
-Version: 5.3.0
+Version: 5.3.0rc1
 Summary: Provider for Apache Airflow. Implements apache-airflow-providers-cncf-kubernetes package
 Home-page: https://airflow.apache.org/
 Download-URL: https://archive.apache.org/dist/airflow/providers
 Author: Apache Software Foundation
 Author-email: dev@airflow.apache.org
 License: Apache License 2.0
 Project-URL: Documentation, https://airflow.apache.org/docs/apache-airflow-providers-cncf-kubernetes/5.3.0/
@@ -48,15 +48,15 @@
    KIND, either express or implied.  See the License for the
    specific language governing permissions and limitations
    under the License.
 
 
 Package ``apache-airflow-providers-cncf-kubernetes``
 
-Release: ``5.3.0``
+Release: ``5.3.0rc1``
 
 
 `Kubernetes <https://kubernetes.io/>`__
 
 
 Provider package
 ----------------
```

### Comparing `apache-airflow-providers-cncf-kubernetes-5.3.0/README.rst` & `apache-airflow-providers-cncf-kubernetes-5.3.0rc1/README.rst`

 * *Files 0% similar despite different names*

```diff
@@ -15,15 +15,15 @@
    KIND, either express or implied.  See the License for the
    specific language governing permissions and limitations
    under the License.
 
 
 Package ``apache-airflow-providers-cncf-kubernetes``
 
-Release: ``5.3.0``
+Release: ``5.3.0rc1``
 
 
 `Kubernetes <https://kubernetes.io/>`__
 
 
 Provider package
 ----------------
```

### Comparing `apache-airflow-providers-cncf-kubernetes-5.3.0/airflow/providers/cncf/kubernetes/__init__.py` & `apache-airflow-providers-cncf-kubernetes-5.3.0rc1/airflow/providers/cncf/kubernetes/__init__.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-cncf-kubernetes-5.3.0/airflow/providers/cncf/kubernetes/backcompat/__init__.py` & `apache-airflow-providers-cncf-kubernetes-5.3.0rc1/airflow/providers/cncf/kubernetes/backcompat/__init__.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-cncf-kubernetes-5.3.0/airflow/providers/cncf/kubernetes/backcompat/backwards_compat_converters.py` & `apache-airflow-providers-cncf-kubernetes-5.3.0rc1/airflow/providers/cncf/kubernetes/backcompat/backwards_compat_converters.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-cncf-kubernetes-5.3.0/airflow/providers/cncf/kubernetes/decorators/__init__.py` & `apache-airflow-providers-cncf-kubernetes-5.3.0rc1/airflow/providers/cncf/kubernetes/decorators/__init__.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-cncf-kubernetes-5.3.0/airflow/providers/cncf/kubernetes/decorators/kubernetes.py` & `apache-airflow-providers-cncf-kubernetes-5.3.0rc1/airflow/providers/cncf/kubernetes/decorators/kubernetes.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-cncf-kubernetes-5.3.0/airflow/providers/cncf/kubernetes/get_provider_info.py` & `apache-airflow-providers-cncf-kubernetes-5.3.0rc1/airflow/providers/cncf/kubernetes/get_provider_info.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-cncf-kubernetes-5.3.0/airflow/providers/cncf/kubernetes/hooks/__init__.py` & `apache-airflow-providers-cncf-kubernetes-5.3.0rc1/airflow/providers/cncf/kubernetes/hooks/__init__.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-cncf-kubernetes-5.3.0/airflow/providers/cncf/kubernetes/hooks/kubernetes.py` & `apache-airflow-providers-cncf-kubernetes-5.3.0rc1/airflow/providers/cncf/kubernetes/hooks/kubernetes.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-cncf-kubernetes-5.3.0/airflow/providers/cncf/kubernetes/operators/__init__.py` & `apache-airflow-providers-cncf-kubernetes-5.3.0rc1/airflow/providers/cncf/kubernetes/operators/__init__.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-cncf-kubernetes-5.3.0/airflow/providers/cncf/kubernetes/operators/kubernetes_pod.py` & `apache-airflow-providers-cncf-kubernetes-5.3.0rc1/airflow/providers/cncf/kubernetes/operators/kubernetes_pod.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-cncf-kubernetes-5.3.0/airflow/providers/cncf/kubernetes/operators/pod.py` & `apache-airflow-providers-cncf-kubernetes-5.3.0rc1/airflow/providers/cncf/kubernetes/operators/pod.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-cncf-kubernetes-5.3.0/airflow/providers/cncf/kubernetes/operators/spark_kubernetes.py` & `apache-airflow-providers-cncf-kubernetes-5.3.0rc1/airflow/providers/cncf/kubernetes/operators/spark_kubernetes.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-cncf-kubernetes-5.3.0/airflow/providers/cncf/kubernetes/python_kubernetes_script.jinja2` & `apache-airflow-providers-cncf-kubernetes-5.3.0rc1/airflow/providers/cncf/kubernetes/python_kubernetes_script.jinja2`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-cncf-kubernetes-5.3.0/airflow/providers/cncf/kubernetes/python_kubernetes_script.py` & `apache-airflow-providers-cncf-kubernetes-5.3.0rc1/airflow/providers/cncf/kubernetes/python_kubernetes_script.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-cncf-kubernetes-5.3.0/airflow/providers/cncf/kubernetes/sensors/__init__.py` & `apache-airflow-providers-cncf-kubernetes-5.3.0rc1/airflow/providers/cncf/kubernetes/sensors/__init__.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-cncf-kubernetes-5.3.0/airflow/providers/cncf/kubernetes/sensors/spark_kubernetes.py` & `apache-airflow-providers-cncf-kubernetes-5.3.0rc1/airflow/providers/cncf/kubernetes/sensors/spark_kubernetes.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-cncf-kubernetes-5.3.0/airflow/providers/cncf/kubernetes/triggers/__init__.py` & `apache-airflow-providers-cncf-kubernetes-5.3.0rc1/airflow/providers/cncf/kubernetes/triggers/__init__.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-cncf-kubernetes-5.3.0/airflow/providers/cncf/kubernetes/triggers/kubernetes_pod.py` & `apache-airflow-providers-cncf-kubernetes-5.3.0rc1/airflow/providers/cncf/kubernetes/triggers/kubernetes_pod.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-cncf-kubernetes-5.3.0/airflow/providers/cncf/kubernetes/triggers/pod.py` & `apache-airflow-providers-cncf-kubernetes-5.3.0rc1/airflow/providers/cncf/kubernetes/triggers/pod.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-cncf-kubernetes-5.3.0/airflow/providers/cncf/kubernetes/utils/__init__.py` & `apache-airflow-providers-cncf-kubernetes-5.3.0rc1/airflow/providers/cncf/kubernetes/utils/__init__.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-cncf-kubernetes-5.3.0/airflow/providers/cncf/kubernetes/utils/pod_manager.py` & `apache-airflow-providers-cncf-kubernetes-5.3.0rc1/airflow/providers/cncf/kubernetes/utils/pod_manager.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-cncf-kubernetes-5.3.0/airflow/providers/cncf/kubernetes/utils/xcom_sidecar.py` & `apache-airflow-providers-cncf-kubernetes-5.3.0rc1/airflow/providers/cncf/kubernetes/utils/xcom_sidecar.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-cncf-kubernetes-5.3.0/apache_airflow_providers_cncf_kubernetes.egg-info/PKG-INFO` & `apache-airflow-providers-cncf-kubernetes-5.3.0rc1/apache_airflow_providers_cncf_kubernetes.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: apache-airflow-providers-cncf-kubernetes
-Version: 5.3.0
+Version: 5.3.0rc1
 Summary: Provider for Apache Airflow. Implements apache-airflow-providers-cncf-kubernetes package
 Home-page: https://airflow.apache.org/
 Download-URL: https://archive.apache.org/dist/airflow/providers
 Author: Apache Software Foundation
 Author-email: dev@airflow.apache.org
 License: Apache License 2.0
 Project-URL: Documentation, https://airflow.apache.org/docs/apache-airflow-providers-cncf-kubernetes/5.3.0/
@@ -48,15 +48,15 @@
    KIND, either express or implied.  See the License for the
    specific language governing permissions and limitations
    under the License.
 
 
 Package ``apache-airflow-providers-cncf-kubernetes``
 
-Release: ``5.3.0``
+Release: ``5.3.0rc1``
 
 
 `Kubernetes <https://kubernetes.io/>`__
 
 
 Provider package
 ----------------
```

### Comparing `apache-airflow-providers-cncf-kubernetes-5.3.0/apache_airflow_providers_cncf_kubernetes.egg-info/SOURCES.txt` & `apache-airflow-providers-cncf-kubernetes-5.3.0rc1/apache_airflow_providers_cncf_kubernetes.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-cncf-kubernetes-5.3.0/pyproject.toml` & `apache-airflow-providers-cncf-kubernetes-5.3.0rc1/pyproject.toml`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-cncf-kubernetes-5.3.0/setup.cfg` & `apache-airflow-providers-cncf-kubernetes-5.3.0rc1/setup.cfg`

 * *Files 2% similar despite different names*

```diff
@@ -42,24 +42,24 @@
 include_package_data = True
 python_requires = ~=3.7
 packages = find:
 setup_requires = 
 	setuptools
 	wheel
 install_requires = 
-	apache-airflow>=2.3.0
+	apache-airflow>=2.3.0.dev0
 	asgiref>=3.5.2
 	cryptography>=2.0.0
 	kubernetes>=21.7.0,<24
 	kubernetes_asyncio>=18.20.1,<25
 
 [options.entry_points]
 apache_airflow_provider = 
 	provider_info=airflow.providers.cncf.kubernetes.get_provider_info:get_provider_info
 
 [files]
 packages = airflow.providers.cncf.kubernetes
 
 [egg_info]
-tag_build = 
+tag_build = rc1
 tag_date = 0
```

### Comparing `apache-airflow-providers-cncf-kubernetes-5.3.0/setup.py` & `apache-airflow-providers-cncf-kubernetes-5.3.0rc1/setup.py`

 * *Files identical despite different names*

