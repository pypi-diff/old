# Comparing `tmp/vidis_algorithms_api-0.2.0.tar.gz` & `tmp/vidis_algorithms_api-0.3.0.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "vidis_algorithms_api-0.2.0.tar", last modified: Tue Nov 15 09:19:37 2022, max compression
+gzip compressed data, was "vidis_algorithms_api-0.3.0.tar", last modified: Fri Apr  7 06:18:36 2023, max compression
```

## Comparing `vidis_algorithms_api-0.2.0.tar` & `vidis_algorithms_api-0.3.0.tar`

### file list

```diff
@@ -1,46 +1,26 @@
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-11-15 09:19:37.430530 vidis_algorithms_api-0.2.0/
--rw-r--r--   0 root         (0) root         (0)      383 2022-11-15 09:19:37.430530 vidis_algorithms_api-0.2.0/PKG-INFO
--rw-rw-rw-   0 root         (0) root         (0)       29 2022-11-02 10:16:57.000000 vidis_algorithms_api-0.2.0/README.md
--rw-rw-rw-   0 root         (0) root         (0)      471 2022-11-15 09:13:09.000000 vidis_algorithms_api-0.2.0/pyproject.toml
--rw-r--r--   0 root         (0) root         (0)       38 2022-11-15 09:19:37.430530 vidis_algorithms_api-0.2.0/setup.cfg
--rw-rw-rw-   0 root         (0) root         (0)      747 2022-11-15 09:13:09.000000 vidis_algorithms_api-0.2.0/setup.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-11-15 09:19:37.426530 vidis_algorithms_api-0.2.0/test/
--rw-rw-rw-   0 root         (0) root         (0)      546 2022-11-15 09:13:09.000000 vidis_algorithms_api-0.2.0/test/algorithm.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-11-15 09:19:37.430530 vidis_algorithms_api-0.2.0/vidis_algorithms_api/
--rw-rw-rw-   0 root         (0) root         (0)     1933 2022-11-13 14:38:53.000000 vidis_algorithms_api-0.2.0/vidis_algorithms_api/MQConsumer.py
--rw-rw-rw-   0 root         (0) root         (0)      368 2022-11-13 14:38:53.000000 vidis_algorithms_api-0.2.0/vidis_algorithms_api/Main.py
--rw-rw-rw-   0 root         (0) root         (0)     2748 2022-11-15 09:13:09.000000 vidis_algorithms_api-0.2.0/vidis_algorithms_api/Task.py
--rw-rw-rw-   0 root         (0) root         (0)       56 2022-11-02 10:16:57.000000 vidis_algorithms_api-0.2.0/vidis_algorithms_api/__init__.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-11-15 09:19:37.430530 vidis_algorithms_api-0.2.0/vidis_algorithms_api/algorithm/
--rw-rw-rw-   0 root         (0) root         (0)        0 2022-11-02 10:16:57.000000 vidis_algorithms_api-0.2.0/vidis_algorithms_api/algorithm/__init__.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-11-15 09:19:37.430530 vidis_algorithms_api-0.2.0/vidis_algorithms_api/core/
--rw-rw-rw-   0 root         (0) root         (0)      531 2022-11-15 09:13:09.000000 vidis_algorithms_api-0.2.0/vidis_algorithms_api/core/Settings.py
--rw-rw-rw-   0 root         (0) root         (0)       54 2022-11-02 10:16:57.000000 vidis_algorithms_api-0.2.0/vidis_algorithms_api/core/__init__.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-11-15 09:19:37.430530 vidis_algorithms_api-0.2.0/vidis_algorithms_api/dao/
--rw-rw-rw-   0 root         (0) root         (0)      794 2022-11-02 10:16:57.000000 vidis_algorithms_api-0.2.0/vidis_algorithms_api/dao/AsyncTaskDao.py
--rw-rw-rw-   0 root         (0) root         (0)      506 2022-11-15 09:13:09.000000 vidis_algorithms_api-0.2.0/vidis_algorithms_api/dao/CustomLayerDao.py
--rw-rw-rw-   0 root         (0) root         (0)       82 2022-11-02 10:16:57.000000 vidis_algorithms_api-0.2.0/vidis_algorithms_api/dao/__init__.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-11-15 09:19:37.430530 vidis_algorithms_api-0.2.0/vidis_algorithms_api/dao/base/
--rw-rw-rw-   0 root         (0) root         (0)     1286 2022-11-02 10:16:57.000000 vidis_algorithms_api-0.2.0/vidis_algorithms_api/dao/base/MariaDataSource.py
--rw-rw-rw-   0 root         (0) root         (0)      470 2022-11-02 10:16:57.000000 vidis_algorithms_api-0.2.0/vidis_algorithms_api/dao/base/SQLDataSource.py
--rw-rw-rw-   0 root         (0) root         (0)       45 2022-11-02 10:16:57.000000 vidis_algorithms_api-0.2.0/vidis_algorithms_api/dao/base/__init__.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-11-15 09:19:37.430530 vidis_algorithms_api-0.2.0/vidis_algorithms_api/dao/datasources/
--rw-rw-rw-   0 root         (0) root         (0)     1159 2022-11-02 10:16:57.000000 vidis_algorithms_api-0.2.0/vidis_algorithms_api/dao/datasources/AsyncTaskDataSource.py
--rw-rw-rw-   0 root         (0) root         (0)      382 2022-11-15 09:13:09.000000 vidis_algorithms_api-0.2.0/vidis_algorithms_api/dao/datasources/CustomLayerDataSource.py
--rw-rw-rw-   0 root         (0) root         (0)      110 2022-11-02 10:16:57.000000 vidis_algorithms_api-0.2.0/vidis_algorithms_api/dao/datasources/__init__.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-11-15 09:19:37.430530 vidis_algorithms_api-0.2.0/vidis_algorithms_api/models/
--rw-rw-rw-   0 root         (0) root         (0)     1391 2022-11-02 10:16:57.000000 vidis_algorithms_api-0.2.0/vidis_algorithms_api/models/AsyncTasks.py
--rw-rw-rw-   0 root         (0) root         (0)       71 2022-11-02 10:16:57.000000 vidis_algorithms_api-0.2.0/vidis_algorithms_api/models/Base.py
--rw-rw-rw-   0 root         (0) root         (0)      952 2022-11-13 16:42:11.000000 vidis_algorithms_api-0.2.0/vidis_algorithms_api/models/CustomLayer.py
--rw-rw-rw-   0 root         (0) root         (0)      211 2022-11-02 10:16:57.000000 vidis_algorithms_api-0.2.0/vidis_algorithms_api/models/Hyperspecter.py
--rw-rw-rw-   0 root         (0) root         (0)      199 2022-11-15 09:13:09.000000 vidis_algorithms_api-0.2.0/vidis_algorithms_api/models/QueuePayload.py
--rw-rw-rw-   0 root         (0) root         (0)      167 2022-11-02 10:16:57.000000 vidis_algorithms_api-0.2.0/vidis_algorithms_api/models/__init__.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-11-15 09:19:37.430530 vidis_algorithms_api-0.2.0/vidis_algorithms_api/utils/
--rw-rw-rw-   0 root         (0) root         (0)      981 2022-11-15 09:13:09.000000 vidis_algorithms_api-0.2.0/vidis_algorithms_api/utils/DataProvider.py
--rw-rw-rw-   0 root         (0) root         (0)       39 2022-11-02 10:16:57.000000 vidis_algorithms_api-0.2.0/vidis_algorithms_api/utils/__init__.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-11-15 09:19:37.430530 vidis_algorithms_api-0.2.0/vidis_algorithms_api.egg-info/
--rw-r--r--   0 root         (0) root         (0)      383 2022-11-15 09:19:37.000000 vidis_algorithms_api-0.2.0/vidis_algorithms_api.egg-info/PKG-INFO
--rw-r--r--   0 root         (0) root         (0)     1276 2022-11-15 09:19:37.000000 vidis_algorithms_api-0.2.0/vidis_algorithms_api.egg-info/SOURCES.txt
--rw-r--r--   0 root         (0) root         (0)        1 2022-11-15 09:19:37.000000 vidis_algorithms_api-0.2.0/vidis_algorithms_api.egg-info/dependency_links.txt
--rw-r--r--   0 root         (0) root         (0)      124 2022-11-15 09:19:37.000000 vidis_algorithms_api-0.2.0/vidis_algorithms_api.egg-info/requires.txt
--rw-r--r--   0 root         (0) root         (0)       31 2022-11-15 09:19:37.000000 vidis_algorithms_api-0.2.0/vidis_algorithms_api.egg-info/top_level.txt
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 06:18:36.696200 vidis_algorithms_api-0.3.0/
+-rw-r--r--   0 root         (0) root         (0)      383 2023-04-07 06:18:36.696200 vidis_algorithms_api-0.3.0/PKG-INFO
+-rw-rw-rw-   0 root         (0) root         (0)     1370 2023-04-06 10:48:38.000000 vidis_algorithms_api-0.3.0/README.md
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 06:18:36.692200 vidis_algorithms_api-0.3.0/examples/
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 06:18:36.692200 vidis_algorithms_api-0.3.0/examples/dummy_example/
+-rw-rw-rw-   0 root         (0) root         (0)      528 2023-04-06 10:48:38.000000 vidis_algorithms_api-0.3.0/examples/dummy_example/algorithm.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 06:18:36.692200 vidis_algorithms_api-0.3.0/examples/neural_network/
+-rw-rw-rw-   0 root         (0) root         (0)     3626 2023-04-06 10:48:38.000000 vidis_algorithms_api-0.3.0/examples/neural_network/algorithm.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 06:18:36.692200 vidis_algorithms_api-0.3.0/examples/neural_network/model/
+-rw-rw-rw-   0 root         (0) root         (0)     3737 2023-04-06 10:48:38.000000 vidis_algorithms_api-0.3.0/examples/neural_network/model/model.py
+-rw-rw-rw-   0 root         (0) root         (0)      471 2023-04-06 10:48:38.000000 vidis_algorithms_api-0.3.0/pyproject.toml
+-rw-r--r--   0 root         (0) root         (0)       38 2023-04-07 06:18:36.696200 vidis_algorithms_api-0.3.0/setup.cfg
+-rw-rw-rw-   0 root         (0) root         (0)      654 2023-04-06 10:48:38.000000 vidis_algorithms_api-0.3.0/setup.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 06:18:36.692200 vidis_algorithms_api-0.3.0/vidis_algorithms_api/
+-rw-rw-rw-   0 root         (0) root         (0)      568 2023-04-06 10:48:38.000000 vidis_algorithms_api-0.3.0/vidis_algorithms_api/Main.py
+-rw-rw-rw-   0 root         (0) root         (0)     1091 2023-04-06 10:48:38.000000 vidis_algorithms_api-0.3.0/vidis_algorithms_api/Task.py
+-rw-rw-rw-   0 root         (0) root         (0)       56 2023-04-06 10:48:38.000000 vidis_algorithms_api-0.3.0/vidis_algorithms_api/__init__.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 06:18:36.696200 vidis_algorithms_api-0.3.0/vidis_algorithms_api/core/
+-rw-rw-rw-   0 root         (0) root         (0)      217 2023-04-06 10:48:38.000000 vidis_algorithms_api-0.3.0/vidis_algorithms_api/core/Settings.py
+-rw-rw-rw-   0 root         (0) root         (0)       54 2023-04-06 10:48:38.000000 vidis_algorithms_api-0.3.0/vidis_algorithms_api/core/__init__.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 06:18:36.696200 vidis_algorithms_api-0.3.0/vidis_algorithms_api.egg-info/
+-rw-r--r--   0 root         (0) root         (0)      383 2023-04-07 06:18:36.000000 vidis_algorithms_api-0.3.0/vidis_algorithms_api.egg-info/PKG-INFO
+-rw-r--r--   0 root         (0) root         (0)      531 2023-04-07 06:18:36.000000 vidis_algorithms_api-0.3.0/vidis_algorithms_api.egg-info/SOURCES.txt
+-rw-r--r--   0 root         (0) root         (0)        1 2023-04-07 06:18:36.000000 vidis_algorithms_api-0.3.0/vidis_algorithms_api.egg-info/dependency_links.txt
+-rw-r--r--   0 root         (0) root         (0)       59 2023-04-07 06:18:36.000000 vidis_algorithms_api-0.3.0/vidis_algorithms_api.egg-info/requires.txt
+-rw-r--r--   0 root         (0) root         (0)       42 2023-04-07 06:18:36.000000 vidis_algorithms_api-0.3.0/vidis_algorithms_api.egg-info/top_level.txt
```

### Comparing `vidis_algorithms_api-0.2.0/setup.py` & `vidis_algorithms_api-0.3.0/setup.py`

 * *Files 13% similar despite different names*

```diff
@@ -1,26 +1,22 @@
 from setuptools import setup, find_packages
 
 requirements = [
-    'pika==1.3.1',
-    'mariadb==1.0.7',
-    'mysqlclient==2.0.3',
     'pydantic==1.10.2',
     'loguru==0.6.0',
-    'sqlalchemy==1.4.42',
-    'loguru==0.6.0',
-    'numpy==1.23.4',
+    'numpy==1.24.1',
+    'celery==5.2.7',
 ]
 
 with open('README.md', 'r') as f:
     description = f.read()
 
 
 def setup_package():
-    __version__ = '0.2.0'
+    __version__ = '0.3.0'
     url = 'https://github.com/Banayaki'
 
     setup(name='vidis_algorithms_api',
           description=description,
           version=__version__,
           url=url,
           license='MIT',
```

