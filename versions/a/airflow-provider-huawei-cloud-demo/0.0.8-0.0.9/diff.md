# Comparing `tmp/airflow-provider-huawei-cloud-demo-0.0.8.tar.gz` & `tmp/airflow-provider-huawei-cloud-demo-0.0.9.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "/home/runner/work/airflow-provider-huawei-cloud/airflow-provider-huawei-cloud/dist/.tmp-mwgbce3h/airflow-provider-huawei-cloud-", last modified: Tue Apr  4 12:18:32 2023, max compression
+gzip compressed data, was "/home/runner/work/airflow-provider-huawei-cloud/airflow-provider-huawei-cloud/dist/.tmp-byd5if7a/airflow-provider-huawei-cloud-", last modified: Fri Apr  7 07:25:37 2023, max compression
```

## Comparing `airflow-provider-huawei-cloud-demo-0.0.8.tar` & `airflow-provider-huawei-cloud-demo-0.0.9.tar`

### file list

```diff
@@ -1,40 +1,43 @@
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-04 12:18:32.000000 airflow-provider-huawei-cloud-demo-0.0.8/
--rw-r--r--   0 runner    (1001) docker     (123)    11357 2023-04-04 12:17:28.000000 airflow-provider-huawei-cloud-demo-0.0.8/LICENSE
--rw-r--r--   0 runner    (1001) docker     (123)      549 2023-04-04 12:18:32.000000 airflow-provider-huawei-cloud-demo-0.0.8/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)       38 2023-04-04 12:17:28.000000 airflow-provider-huawei-cloud-demo-0.0.8/README.md
--rw-r--r--   0 runner    (1001) docker     (123)      162 2023-04-04 12:17:28.000000 airflow-provider-huawei-cloud-demo-0.0.8/pyproject.toml
--rw-r--r--   0 runner    (1001) docker     (123)     1040 2023-04-04 12:18:32.000000 airflow-provider-huawei-cloud-demo-0.0.8/setup.cfg
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-04 12:18:32.000000 airflow-provider-huawei-cloud-demo-0.0.8/src/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-04 12:18:32.000000 airflow-provider-huawei-cloud-demo-0.0.8/src/airflow_provider_huawei_cloud_demo.egg-info/
--rw-r--r--   0 runner    (1001) docker     (123)      549 2023-04-04 12:18:32.000000 airflow-provider-huawei-cloud-demo-0.0.8/src/airflow_provider_huawei_cloud_demo.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)     1382 2023-04-04 12:18:32.000000 airflow-provider-huawei-cloud-demo-0.0.8/src/airflow_provider_huawei_cloud_demo.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-04 12:18:32.000000 airflow-provider-huawei-cloud-demo-0.0.8/src/airflow_provider_huawei_cloud_demo.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (123)       91 2023-04-04 12:18:32.000000 airflow-provider-huawei-cloud-demo-0.0.8/src/airflow_provider_huawei_cloud_demo.egg-info/entry_points.txt
--rw-r--r--   0 runner    (1001) docker     (123)      229 2023-04-04 12:18:32.000000 airflow-provider-huawei-cloud-demo-0.0.8/src/airflow_provider_huawei_cloud_demo.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (123)       22 2023-04-04 12:18:32.000000 airflow-provider-huawei-cloud-demo-0.0.8/src/airflow_provider_huawei_cloud_demo.egg-info/top_level.txt
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-04 12:18:32.000000 airflow-provider-huawei-cloud-demo-0.0.8/src/huawei_cloud_provider/
--rw-r--r--   0 runner    (1001) docker     (123)      631 2023-04-04 12:17:28.000000 airflow-provider-huawei-cloud-demo-0.0.8/src/huawei_cloud_provider/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-04 12:18:32.000000 airflow-provider-huawei-cloud-demo-0.0.8/src/huawei_cloud_provider/hooks/
--rw-r--r--   0 runner    (1001) docker     (123)      787 2023-04-04 12:17:28.000000 airflow-provider-huawei-cloud-demo-0.0.8/src/huawei_cloud_provider/hooks/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     4488 2023-04-04 12:17:28.000000 airflow-provider-huawei-cloud-demo-0.0.8/src/huawei_cloud_provider/hooks/base_huawei_cloud.py
--rw-r--r--   0 runner    (1001) docker     (123)     6904 2023-04-04 12:17:28.000000 airflow-provider-huawei-cloud-demo-0.0.8/src/huawei_cloud_provider/hooks/cdm.py
--rw-r--r--   0 runner    (1001) docker     (123)     3519 2023-04-04 12:17:28.000000 airflow-provider-huawei-cloud-demo-0.0.8/src/huawei_cloud_provider/hooks/dataarts.py
--rw-r--r--   0 runner    (1001) docker     (123)    17462 2023-04-04 12:17:28.000000 airflow-provider-huawei-cloud-demo-0.0.8/src/huawei_cloud_provider/hooks/dli.py
--rw-r--r--   0 runner    (1001) docker     (123)    16549 2023-04-04 12:17:28.000000 airflow-provider-huawei-cloud-demo-0.0.8/src/huawei_cloud_provider/hooks/dws.py
--rw-r--r--   0 runner    (1001) docker     (123)    27384 2023-04-04 12:17:28.000000 airflow-provider-huawei-cloud-demo-0.0.8/src/huawei_cloud_provider/hooks/huawei_obs.py
--rw-r--r--   0 runner    (1001) docker     (123)     3603 2023-04-04 12:17:28.000000 airflow-provider-huawei-cloud-demo-0.0.8/src/huawei_cloud_provider/hooks/smn.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-04 12:18:32.000000 airflow-provider-huawei-cloud-demo-0.0.8/src/huawei_cloud_provider/operators/
--rw-r--r--   0 runner    (1001) docker     (123)      785 2023-04-04 12:17:28.000000 airflow-provider-huawei-cloud-demo-0.0.8/src/huawei_cloud_provider/operators/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     7424 2023-04-04 12:17:28.000000 airflow-provider-huawei-cloud-demo-0.0.8/src/huawei_cloud_provider/operators/cdm.py
--rw-r--r--   0 runner    (1001) docker     (123)     2601 2023-04-04 12:17:28.000000 airflow-provider-huawei-cloud-demo-0.0.8/src/huawei_cloud_provider/operators/dataarts.py
--rw-r--r--   0 runner    (1001) docker     (123)    26103 2023-04-04 12:17:28.000000 airflow-provider-huawei-cloud-demo-0.0.8/src/huawei_cloud_provider/operators/dli.py
--rw-r--r--   0 runner    (1001) docker     (123)    17443 2023-04-04 12:17:28.000000 airflow-provider-huawei-cloud-demo-0.0.8/src/huawei_cloud_provider/operators/dws.py
--rw-r--r--   0 runner    (1001) docker     (123)    29864 2023-04-04 12:17:28.000000 airflow-provider-huawei-cloud-demo-0.0.8/src/huawei_cloud_provider/operators/huawei_obs.py
--rw-r--r--   0 runner    (1001) docker     (123)     7085 2023-04-04 12:17:28.000000 airflow-provider-huawei-cloud-demo-0.0.8/src/huawei_cloud_provider/operators/smn.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-04 12:18:32.000000 airflow-provider-huawei-cloud-demo-0.0.8/src/huawei_cloud_provider/sensors/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-04 12:17:28.000000 airflow-provider-huawei-cloud-demo-0.0.8/src/huawei_cloud_provider/sensors/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     3158 2023-04-04 12:17:28.000000 airflow-provider-huawei-cloud-demo-0.0.8/src/huawei_cloud_provider/sensors/cdm.py
--rw-r--r--   0 runner    (1001) docker     (123)     3325 2023-04-04 12:17:28.000000 airflow-provider-huawei-cloud-demo-0.0.8/src/huawei_cloud_provider/sensors/dataarts.py
--rw-r--r--   0 runner    (1001) docker     (123)     3791 2023-04-04 12:17:28.000000 airflow-provider-huawei-cloud-demo-0.0.8/src/huawei_cloud_provider/sensors/dli.py
--rw-r--r--   0 runner    (1001) docker     (123)     4524 2023-04-04 12:17:28.000000 airflow-provider-huawei-cloud-demo-0.0.8/src/huawei_cloud_provider/sensors/dws.py
--rw-r--r--   0 runner    (1001) docker     (123)     3691 2023-04-04 12:17:28.000000 airflow-provider-huawei-cloud-demo-0.0.8/src/huawei_cloud_provider/sensors/huawei_obs_key.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:25:37.000000 airflow-provider-huawei-cloud-demo-0.0.9/
+-rw-r--r--   0 runner    (1001) docker     (123)    11357 2023-04-07 07:24:38.000000 airflow-provider-huawei-cloud-demo-0.0.9/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (123)      549 2023-04-07 07:25:37.000000 airflow-provider-huawei-cloud-demo-0.0.9/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)       38 2023-04-07 07:24:38.000000 airflow-provider-huawei-cloud-demo-0.0.9/README.md
+-rw-r--r--   0 runner    (1001) docker     (123)      162 2023-04-07 07:24:38.000000 airflow-provider-huawei-cloud-demo-0.0.9/pyproject.toml
+-rw-r--r--   0 runner    (1001) docker     (123)     1058 2023-04-07 07:25:37.000000 airflow-provider-huawei-cloud-demo-0.0.9/setup.cfg
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:25:37.000000 airflow-provider-huawei-cloud-demo-0.0.9/src/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:25:37.000000 airflow-provider-huawei-cloud-demo-0.0.9/src/airflow_provider_huawei_cloud_demo.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)      549 2023-04-07 07:25:37.000000 airflow-provider-huawei-cloud-demo-0.0.9/src/airflow_provider_huawei_cloud_demo.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     1523 2023-04-07 07:25:37.000000 airflow-provider-huawei-cloud-demo-0.0.9/src/airflow_provider_huawei_cloud_demo.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-07 07:25:37.000000 airflow-provider-huawei-cloud-demo-0.0.9/src/airflow_provider_huawei_cloud_demo.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       91 2023-04-07 07:25:37.000000 airflow-provider-huawei-cloud-demo-0.0.9/src/airflow_provider_huawei_cloud_demo.egg-info/entry_points.txt
+-rw-r--r--   0 runner    (1001) docker     (123)      246 2023-04-07 07:25:37.000000 airflow-provider-huawei-cloud-demo-0.0.9/src/airflow_provider_huawei_cloud_demo.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       22 2023-04-07 07:25:37.000000 airflow-provider-huawei-cloud-demo-0.0.9/src/airflow_provider_huawei_cloud_demo.egg-info/top_level.txt
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:25:37.000000 airflow-provider-huawei-cloud-demo-0.0.9/src/huawei_cloud_provider/
+-rw-r--r--   0 runner    (1001) docker     (123)      631 2023-04-07 07:24:38.000000 airflow-provider-huawei-cloud-demo-0.0.9/src/huawei_cloud_provider/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:25:37.000000 airflow-provider-huawei-cloud-demo-0.0.9/src/huawei_cloud_provider/hooks/
+-rw-r--r--   0 runner    (1001) docker     (123)      787 2023-04-07 07:24:38.000000 airflow-provider-huawei-cloud-demo-0.0.9/src/huawei_cloud_provider/hooks/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5320 2023-04-07 07:24:38.000000 airflow-provider-huawei-cloud-demo-0.0.9/src/huawei_cloud_provider/hooks/base_huawei_cloud.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6904 2023-04-07 07:24:38.000000 airflow-provider-huawei-cloud-demo-0.0.9/src/huawei_cloud_provider/hooks/cdm.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3519 2023-04-07 07:24:38.000000 airflow-provider-huawei-cloud-demo-0.0.9/src/huawei_cloud_provider/hooks/dataarts.py
+-rw-r--r--   0 runner    (1001) docker     (123)    17462 2023-04-07 07:24:38.000000 airflow-provider-huawei-cloud-demo-0.0.9/src/huawei_cloud_provider/hooks/dli.py
+-rw-r--r--   0 runner    (1001) docker     (123)    16549 2023-04-07 07:24:38.000000 airflow-provider-huawei-cloud-demo-0.0.9/src/huawei_cloud_provider/hooks/dws.py
+-rw-r--r--   0 runner    (1001) docker     (123)    27384 2023-04-07 07:24:38.000000 airflow-provider-huawei-cloud-demo-0.0.9/src/huawei_cloud_provider/hooks/huawei_obs.py
+-rw-r--r--   0 runner    (1001) docker     (123)    15407 2023-04-07 07:24:38.000000 airflow-provider-huawei-cloud-demo-0.0.9/src/huawei_cloud_provider/hooks/modelarts.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3603 2023-04-07 07:24:38.000000 airflow-provider-huawei-cloud-demo-0.0.9/src/huawei_cloud_provider/hooks/smn.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:25:37.000000 airflow-provider-huawei-cloud-demo-0.0.9/src/huawei_cloud_provider/operators/
+-rw-r--r--   0 runner    (1001) docker     (123)      785 2023-04-07 07:24:38.000000 airflow-provider-huawei-cloud-demo-0.0.9/src/huawei_cloud_provider/operators/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7424 2023-04-07 07:24:38.000000 airflow-provider-huawei-cloud-demo-0.0.9/src/huawei_cloud_provider/operators/cdm.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2601 2023-04-07 07:24:38.000000 airflow-provider-huawei-cloud-demo-0.0.9/src/huawei_cloud_provider/operators/dataarts.py
+-rw-r--r--   0 runner    (1001) docker     (123)    26103 2023-04-07 07:24:38.000000 airflow-provider-huawei-cloud-demo-0.0.9/src/huawei_cloud_provider/operators/dli.py
+-rw-r--r--   0 runner    (1001) docker     (123)    17443 2023-04-07 07:24:38.000000 airflow-provider-huawei-cloud-demo-0.0.9/src/huawei_cloud_provider/operators/dws.py
+-rw-r--r--   0 runner    (1001) docker     (123)    29864 2023-04-07 07:24:38.000000 airflow-provider-huawei-cloud-demo-0.0.9/src/huawei_cloud_provider/operators/huawei_obs.py
+-rw-r--r--   0 runner    (1001) docker     (123)    42253 2023-04-07 07:24:38.000000 airflow-provider-huawei-cloud-demo-0.0.9/src/huawei_cloud_provider/operators/modelarts.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7085 2023-04-07 07:24:38.000000 airflow-provider-huawei-cloud-demo-0.0.9/src/huawei_cloud_provider/operators/smn.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:25:37.000000 airflow-provider-huawei-cloud-demo-0.0.9/src/huawei_cloud_provider/sensors/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-07 07:24:38.000000 airflow-provider-huawei-cloud-demo-0.0.9/src/huawei_cloud_provider/sensors/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3158 2023-04-07 07:24:38.000000 airflow-provider-huawei-cloud-demo-0.0.9/src/huawei_cloud_provider/sensors/cdm.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3325 2023-04-07 07:24:38.000000 airflow-provider-huawei-cloud-demo-0.0.9/src/huawei_cloud_provider/sensors/dataarts.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3791 2023-04-07 07:24:38.000000 airflow-provider-huawei-cloud-demo-0.0.9/src/huawei_cloud_provider/sensors/dli.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4524 2023-04-07 07:24:38.000000 airflow-provider-huawei-cloud-demo-0.0.9/src/huawei_cloud_provider/sensors/dws.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3691 2023-04-07 07:24:38.000000 airflow-provider-huawei-cloud-demo-0.0.9/src/huawei_cloud_provider/sensors/huawei_obs_key.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4985 2023-04-07 07:24:38.000000 airflow-provider-huawei-cloud-demo-0.0.9/src/huawei_cloud_provider/sensors/modelarts.py
```

### Comparing `airflow-provider-huawei-cloud-demo-0.0.8/LICENSE` & `airflow-provider-huawei-cloud-demo-0.0.9/LICENSE`

 * *Files identical despite different names*

### Comparing `airflow-provider-huawei-cloud-demo-0.0.8/PKG-INFO` & `airflow-provider-huawei-cloud-demo-0.0.9/PKG-INFO`

 * *Files 26% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: airflow-provider-huawei-cloud-demo
-Version: 0.0.8
+Version: 0.0.9
 Summary: Huawei Cloud integration for Apoache Airflow
 Home-page: https://github.com/emincanozcan/airflow-provider-huawei-cloud
 Author: Emincan Ozcan
 Author-email: emincan@emincanozcan.com
 Classifier: Programming Language :: Python :: 3
 Classifier: License :: OSI Approved :: Apache Software License
 Classifier: Operating System :: OS Independent
```

### Comparing `airflow-provider-huawei-cloud-demo-0.0.8/setup.cfg` & `airflow-provider-huawei-cloud-demo-0.0.9/setup.cfg`

 * *Files 12% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 [metadata]
 name = airflow-provider-huawei-cloud-demo
-version = 0.0.8
+version = 0.0.9
 author = Emincan Ozcan
 author_email = emincan@emincanozcan.com
 description = Huawei Cloud integration for Apoache Airflow
 long_description = file: README.md
 long_description_content_type = text/markdown
 url = https://github.com/emincanozcan/airflow-provider-huawei-cloud
 classifiers = 
@@ -26,14 +26,15 @@
 	esdk-obs-python==3.22.2
 	huaweicloudsdkdws==3.1.21
 	huaweicloudsdksmn==3.1.19
 	huaweicloudsdkdli==3.1.19
 	huaweicloudsdkcdm==3.1.19
 	huaweicloudsdkdlf==3.1.19
 	huaweicloudsdkiam==3.1.19
+	requests==2.28.2
 
 [options.packages.find]
 where = src
 
 [options.entry_points]
 apache_airflow_provider = 
 	provider_info=huawei_cloud_provider.__init__:get_provider_info
```

### Comparing `airflow-provider-huawei-cloud-demo-0.0.8/src/airflow_provider_huawei_cloud_demo.egg-info/PKG-INFO` & `airflow-provider-huawei-cloud-demo-0.0.9/src/airflow_provider_huawei_cloud_demo.egg-info/PKG-INFO`

 * *Files 26% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: airflow-provider-huawei-cloud-demo
-Version: 0.0.8
+Version: 0.0.9
 Summary: Huawei Cloud integration for Apoache Airflow
 Home-page: https://github.com/emincanozcan/airflow-provider-huawei-cloud
 Author: Emincan Ozcan
 Author-email: emincan@emincanozcan.com
 Classifier: Programming Language :: Python :: 3
 Classifier: License :: OSI Approved :: Apache Software License
 Classifier: Operating System :: OS Independent
```

### Comparing `airflow-provider-huawei-cloud-demo-0.0.8/src/airflow_provider_huawei_cloud_demo.egg-info/SOURCES.txt` & `airflow-provider-huawei-cloud-demo-0.0.9/src/airflow_provider_huawei_cloud_demo.egg-info/SOURCES.txt`

 * *Files 18% similar despite different names*

```diff
@@ -12,21 +12,24 @@
 src/huawei_cloud_provider/hooks/__init__.py
 src/huawei_cloud_provider/hooks/base_huawei_cloud.py
 src/huawei_cloud_provider/hooks/cdm.py
 src/huawei_cloud_provider/hooks/dataarts.py
 src/huawei_cloud_provider/hooks/dli.py
 src/huawei_cloud_provider/hooks/dws.py
 src/huawei_cloud_provider/hooks/huawei_obs.py
+src/huawei_cloud_provider/hooks/modelarts.py
 src/huawei_cloud_provider/hooks/smn.py
 src/huawei_cloud_provider/operators/__init__.py
 src/huawei_cloud_provider/operators/cdm.py
 src/huawei_cloud_provider/operators/dataarts.py
 src/huawei_cloud_provider/operators/dli.py
 src/huawei_cloud_provider/operators/dws.py
 src/huawei_cloud_provider/operators/huawei_obs.py
+src/huawei_cloud_provider/operators/modelarts.py
 src/huawei_cloud_provider/operators/smn.py
 src/huawei_cloud_provider/sensors/__init__.py
 src/huawei_cloud_provider/sensors/cdm.py
 src/huawei_cloud_provider/sensors/dataarts.py
 src/huawei_cloud_provider/sensors/dli.py
 src/huawei_cloud_provider/sensors/dws.py
-src/huawei_cloud_provider/sensors/huawei_obs_key.py
+src/huawei_cloud_provider/sensors/huawei_obs_key.py
+src/huawei_cloud_provider/sensors/modelarts.py
```

### Comparing `airflow-provider-huawei-cloud-demo-0.0.8/src/huawei_cloud_provider/__init__.py` & `airflow-provider-huawei-cloud-demo-0.0.9/src/huawei_cloud_provider/__init__.py`

 * *Files identical despite different names*

### Comparing `airflow-provider-huawei-cloud-demo-0.0.8/src/huawei_cloud_provider/hooks/__init__.py` & `airflow-provider-huawei-cloud-demo-0.0.9/src/huawei_cloud_provider/hooks/__init__.py`

 * *Files identical despite different names*

### Comparing `airflow-provider-huawei-cloud-demo-0.0.8/src/huawei_cloud_provider/hooks/base_huawei_cloud.py` & `airflow-provider-huawei-cloud-demo-0.0.9/src/huawei_cloud_provider/hooks/base_huawei_cloud.py`

 * *Files 18% similar despite different names*

```diff
@@ -19,15 +19,15 @@
 
 import json
 from typing import Any
 
 from huaweicloudsdkcore.auth.credentials import GlobalCredentials
 from huaweicloudsdkcore.exceptions import exceptions
 from huaweicloudsdkiam.v3 import IamClient, KeystoneListAuthDomainsRequest
-
+from . utils.signer import send_signed_request
 from airflow.hooks.base import BaseHook
 
 
 class HuaweiBaseHook(BaseHook):
     """Base class for Huawei Cloud hooks."""
 
     conn_name_attr = "huaweicloud_conn_id"
@@ -109,7 +109,31 @@
             )
 
             request = KeystoneListAuthDomainsRequest()
             client.keystone_list_auth_domains(request)
             return True, "Connection test succeeded!"
         except exceptions.ClientRequestException as e:
             return False, f"{e.error_code} {e.error_msg}"
+
+    def send_request(self, method: str, url: str, body: dict = {}):
+        body = {k: v for k, v in body.items() if v is not None}
+        return send_signed_request(
+            ak=self.conn.login,
+            sk=self.conn.password,
+            project_id=self.get_project_id(),
+            region=self.get_region(),
+            method=method,
+            url=url,
+            body=body
+        )
+
+    def get_request(self, url: str):
+        return self.send_request("GET", url)
+
+    def post_request(self, url: str, body: dict = {}):
+        return self.send_request("POST", url, body)
+
+    def put_request(self, url: str, body: dict = {}):
+        return self.send_request("PUT", url, body)
+
+    def delete_request(self, url: str):
+        return self.send_request("DELETE", url)
```

### Comparing `airflow-provider-huawei-cloud-demo-0.0.8/src/huawei_cloud_provider/hooks/cdm.py` & `airflow-provider-huawei-cloud-demo-0.0.9/src/huawei_cloud_provider/hooks/cdm.py`

 * *Files identical despite different names*

### Comparing `airflow-provider-huawei-cloud-demo-0.0.8/src/huawei_cloud_provider/hooks/dataarts.py` & `airflow-provider-huawei-cloud-demo-0.0.9/src/huawei_cloud_provider/hooks/dataarts.py`

 * *Files identical despite different names*

### Comparing `airflow-provider-huawei-cloud-demo-0.0.8/src/huawei_cloud_provider/hooks/dli.py` & `airflow-provider-huawei-cloud-demo-0.0.9/src/huawei_cloud_provider/hooks/dli.py`

 * *Files identical despite different names*

### Comparing `airflow-provider-huawei-cloud-demo-0.0.8/src/huawei_cloud_provider/hooks/dws.py` & `airflow-provider-huawei-cloud-demo-0.0.9/src/huawei_cloud_provider/hooks/dws.py`

 * *Files identical despite different names*

### Comparing `airflow-provider-huawei-cloud-demo-0.0.8/src/huawei_cloud_provider/hooks/huawei_obs.py` & `airflow-provider-huawei-cloud-demo-0.0.9/src/huawei_cloud_provider/hooks/huawei_obs.py`

 * *Files identical despite different names*

### Comparing `airflow-provider-huawei-cloud-demo-0.0.8/src/huawei_cloud_provider/hooks/smn.py` & `airflow-provider-huawei-cloud-demo-0.0.9/src/huawei_cloud_provider/hooks/smn.py`

 * *Files identical despite different names*

### Comparing `airflow-provider-huawei-cloud-demo-0.0.8/src/huawei_cloud_provider/operators/__init__.py` & `airflow-provider-huawei-cloud-demo-0.0.9/src/huawei_cloud_provider/operators/__init__.py`

 * *Files identical despite different names*

### Comparing `airflow-provider-huawei-cloud-demo-0.0.8/src/huawei_cloud_provider/operators/cdm.py` & `airflow-provider-huawei-cloud-demo-0.0.9/src/huawei_cloud_provider/operators/cdm.py`

 * *Files identical despite different names*

### Comparing `airflow-provider-huawei-cloud-demo-0.0.8/src/huawei_cloud_provider/operators/dataarts.py` & `airflow-provider-huawei-cloud-demo-0.0.9/src/huawei_cloud_provider/operators/dataarts.py`

 * *Files identical despite different names*

### Comparing `airflow-provider-huawei-cloud-demo-0.0.8/src/huawei_cloud_provider/operators/dli.py` & `airflow-provider-huawei-cloud-demo-0.0.9/src/huawei_cloud_provider/operators/dli.py`

 * *Files identical despite different names*

### Comparing `airflow-provider-huawei-cloud-demo-0.0.8/src/huawei_cloud_provider/operators/dws.py` & `airflow-provider-huawei-cloud-demo-0.0.9/src/huawei_cloud_provider/operators/dws.py`

 * *Files identical despite different names*

### Comparing `airflow-provider-huawei-cloud-demo-0.0.8/src/huawei_cloud_provider/operators/huawei_obs.py` & `airflow-provider-huawei-cloud-demo-0.0.9/src/huawei_cloud_provider/operators/huawei_obs.py`

 * *Files identical despite different names*

### Comparing `airflow-provider-huawei-cloud-demo-0.0.8/src/huawei_cloud_provider/operators/smn.py` & `airflow-provider-huawei-cloud-demo-0.0.9/src/huawei_cloud_provider/operators/smn.py`

 * *Files identical despite different names*

### Comparing `airflow-provider-huawei-cloud-demo-0.0.8/src/huawei_cloud_provider/sensors/cdm.py` & `airflow-provider-huawei-cloud-demo-0.0.9/src/huawei_cloud_provider/sensors/cdm.py`

 * *Files identical despite different names*

### Comparing `airflow-provider-huawei-cloud-demo-0.0.8/src/huawei_cloud_provider/sensors/dataarts.py` & `airflow-provider-huawei-cloud-demo-0.0.9/src/huawei_cloud_provider/sensors/dataarts.py`

 * *Files identical despite different names*

### Comparing `airflow-provider-huawei-cloud-demo-0.0.8/src/huawei_cloud_provider/sensors/dli.py` & `airflow-provider-huawei-cloud-demo-0.0.9/src/huawei_cloud_provider/sensors/dli.py`

 * *Files identical despite different names*

### Comparing `airflow-provider-huawei-cloud-demo-0.0.8/src/huawei_cloud_provider/sensors/dws.py` & `airflow-provider-huawei-cloud-demo-0.0.9/src/huawei_cloud_provider/sensors/dws.py`

 * *Files identical despite different names*

### Comparing `airflow-provider-huawei-cloud-demo-0.0.8/src/huawei_cloud_provider/sensors/huawei_obs_key.py` & `airflow-provider-huawei-cloud-demo-0.0.9/src/huawei_cloud_provider/sensors/huawei_obs_key.py`

 * *Files identical despite different names*

