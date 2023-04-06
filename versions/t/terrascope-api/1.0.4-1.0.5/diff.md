# Comparing `tmp/terrascope-api-1.0.4.tar.gz` & `tmp/terrascope-api-1.0.5.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "terrascope-api-1.0.4.tar", last modified: Thu Dec  1 19:44:41 2022, max compression
+gzip compressed data, was "terrascope-api-1.0.5.tar", last modified: Mon Dec 19 20:09:27 2022, max compression
```

## Comparing `terrascope-api-1.0.4.tar` & `terrascope-api-1.0.5.tar`

### file list

```diff
@@ -1,73 +1,75 @@
-drwxr-xr-x   0 sjawahar   (501) staff       (20)        0 2022-12-01 19:44:41.851241 terrascope-api-1.0.4/
--rw-r--r--   0 sjawahar   (501) staff       (20)     1061 2022-12-01 17:01:43.000000 terrascope-api-1.0.4/LICENSE
--rw-r--r--   0 sjawahar   (501) staff       (20)      164 2022-12-01 19:44:41.850045 terrascope-api-1.0.4/PKG-INFO
--rw-r--r--   0 sjawahar   (501) staff       (20)      579 2022-09-14 22:43:22.000000 terrascope-api-1.0.4/README.md
--rw-r--r--   0 sjawahar   (501) staff       (20)       38 2022-12-01 19:44:41.851610 terrascope-api-1.0.4/setup.cfg
--rw-r--r--   0 sjawahar   (501) staff       (20)     1150 2022-12-01 19:43:30.000000 terrascope-api-1.0.4/setup.py
-drwxr-xr-x   0 sjawahar   (501) staff       (20)        0 2022-12-01 19:44:41.764006 terrascope-api-1.0.4/src/
-drwxr-xr-x   0 sjawahar   (501) staff       (20)        0 2022-12-01 19:44:41.764424 terrascope-api-1.0.4/src/py/
-drwxr-xr-x   0 sjawahar   (501) staff       (20)        0 2022-12-01 19:44:41.771295 terrascope-api-1.0.4/src/py/terrascope_api/
--rw-r--r--   0 sjawahar   (501) staff       (20)      384 2022-12-01 17:01:43.000000 terrascope-api-1.0.4/src/py/terrascope_api/__init__.py
--rw-r--r--   0 sjawahar   (501) staff       (20)     5934 2022-12-01 19:28:06.000000 terrascope-api-1.0.4/src/py/terrascope_api/async_client.py
--rw-r--r--   0 sjawahar   (501) staff       (20)     3615 2022-12-01 17:01:43.000000 terrascope-api-1.0.4/src/py/terrascope_api/async_interceptors.py
-drwxr-xr-x   0 sjawahar   (501) staff       (20)        0 2022-12-01 19:44:41.807730 terrascope-api-1.0.4/src/py/terrascope_api/models/
--rw-r--r--   0 sjawahar   (501) staff       (20)     1143 2022-12-01 19:29:06.000000 terrascope-api-1.0.4/src/py/terrascope_api/models/__init__.py
--rw-r--r--   0 sjawahar   (501) staff       (20)     5481 2022-12-01 19:28:55.000000 terrascope-api-1.0.4/src/py/terrascope_api/models/algorithm_computation_pb2.py
--rw-r--r--   0 sjawahar   (501) staff       (20)     7454 2022-12-01 19:28:56.000000 terrascope-api-1.0.4/src/py/terrascope_api/models/algorithm_config_pb2.py
--rw-r--r--   0 sjawahar   (501) staff       (20)     1869 2022-12-01 19:28:56.000000 terrascope-api-1.0.4/src/py/terrascope_api/models/algorithm_manifest_pb2.py
--rw-r--r--   0 sjawahar   (501) staff       (20)     3947 2022-12-01 19:28:56.000000 terrascope-api-1.0.4/src/py/terrascope_api/models/algorithm_pb2.py
--rw-r--r--   0 sjawahar   (501) staff       (20)     8661 2022-12-01 19:28:56.000000 terrascope-api-1.0.4/src/py/terrascope_api/models/algorithm_version_pb2.py
--rw-r--r--   0 sjawahar   (501) staff       (20)     5698 2022-12-01 19:28:56.000000 terrascope-api-1.0.4/src/py/terrascope_api/models/analysis_computation_pb2.py
--rw-r--r--   0 sjawahar   (501) staff       (20)     7294 2022-12-01 19:28:57.000000 terrascope-api-1.0.4/src/py/terrascope_api/models/analysis_config_pb2.py
--rw-r--r--   0 sjawahar   (501) staff       (20)     3860 2022-12-01 19:28:57.000000 terrascope-api-1.0.4/src/py/terrascope_api/models/analysis_pb2.py
--rw-r--r--   0 sjawahar   (501) staff       (20)     5681 2022-12-01 19:28:57.000000 terrascope-api-1.0.4/src/py/terrascope_api/models/analysis_version_pb2.py
--rw-r--r--   0 sjawahar   (501) staff       (20)     5461 2022-12-01 19:28:57.000000 terrascope-api-1.0.4/src/py/terrascope_api/models/aoi_collection_pb2.py
--rw-r--r--   0 sjawahar   (501) staff       (20)     5938 2022-12-01 19:28:57.000000 terrascope-api-1.0.4/src/py/terrascope_api/models/aoi_pb2.py
--rw-r--r--   0 sjawahar   (501) staff       (20)     2568 2022-12-01 19:28:57.000000 terrascope-api-1.0.4/src/py/terrascope_api/models/aoi_transaction_pb2.py
--rw-r--r--   0 sjawahar   (501) staff       (20)     4446 2022-12-01 19:28:57.000000 terrascope-api-1.0.4/src/py/terrascope_api/models/aoi_version_pb2.py
--rw-r--r--   0 sjawahar   (501) staff       (20)     1054 2022-12-01 19:28:57.000000 terrascope-api-1.0.4/src/py/terrascope_api/models/common_models_pb2.py
--rw-r--r--   0 sjawahar   (501) staff       (20)     7251 2022-12-01 19:28:58.000000 terrascope-api-1.0.4/src/py/terrascope_api/models/credit_pb2.py
--rw-r--r--   0 sjawahar   (501) staff       (20)     2507 2022-12-01 19:28:58.000000 terrascope-api-1.0.4/src/py/terrascope_api/models/data_source_pb2.py
--rw-r--r--   0 sjawahar   (501) staff       (20)     2800 2022-12-01 19:28:58.000000 terrascope-api-1.0.4/src/py/terrascope_api/models/data_type_pb2.py
--rw-r--r--   0 sjawahar   (501) staff       (20)     3423 2022-12-01 19:28:58.000000 terrascope-api-1.0.4/src/py/terrascope_api/models/permission_pb2.py
--rw-r--r--   0 sjawahar   (501) staff       (20)     6104 2022-12-01 19:28:58.000000 terrascope-api-1.0.4/src/py/terrascope_api/models/result_pb2.py
--rw-r--r--   0 sjawahar   (501) staff       (20)     1555 2022-12-01 19:28:58.000000 terrascope-api-1.0.4/src/py/terrascope_api/models/system_pb2.py
--rw-r--r--   0 sjawahar   (501) staff       (20)     4604 2022-12-01 19:28:58.000000 terrascope-api-1.0.4/src/py/terrascope_api/models/toi_pb2.py
--rw-r--r--   0 sjawahar   (501) staff       (20)     1565 2022-12-01 19:28:58.000000 terrascope-api-1.0.4/src/py/terrascope_api/models/token_pb2.py
--rw-r--r--   0 sjawahar   (501) staff       (20)     3285 2022-12-01 19:28:58.000000 terrascope-api-1.0.4/src/py/terrascope_api/models/user_collection_pb2.py
--rw-r--r--   0 sjawahar   (501) staff       (20)     3029 2022-12-01 19:28:59.000000 terrascope-api-1.0.4/src/py/terrascope_api/models/user_pb2.py
--rw-r--r--   0 sjawahar   (501) staff       (20)     3306 2022-12-01 19:28:59.000000 terrascope-api-1.0.4/src/py/terrascope_api/models/visualization_pb2.py
-drwxr-xr-x   0 sjawahar   (501) staff       (20)        0 2022-12-01 19:44:41.848840 terrascope-api-1.0.4/src/py/terrascope_api/stubs/
--rw-r--r--   0 sjawahar   (501) staff       (20)     1268 2022-12-01 19:29:07.000000 terrascope-api-1.0.4/src/py/terrascope_api/stubs/__init__.py
--rw-r--r--   0 sjawahar   (501) staff       (20)     8881 2022-12-01 19:28:59.000000 terrascope-api-1.0.4/src/py/terrascope_api/stubs/algorithm_computation_pb2_grpc.py
--rw-r--r--   0 sjawahar   (501) staff       (20)    13880 2022-12-01 19:29:00.000000 terrascope-api-1.0.4/src/py/terrascope_api/stubs/algorithm_config_pb2_grpc.py
--rw-r--r--   0 sjawahar   (501) staff       (20)     2724 2022-12-01 19:29:00.000000 terrascope-api-1.0.4/src/py/terrascope_api/stubs/algorithm_manifest_pb2_grpc.py
--rw-r--r--   0 sjawahar   (501) staff       (20)     7648 2022-12-01 19:29:00.000000 terrascope-api-1.0.4/src/py/terrascope_api/stubs/algorithm_pb2_grpc.py
--rw-r--r--   0 sjawahar   (501) staff       (20)    13032 2022-12-01 19:29:01.000000 terrascope-api-1.0.4/src/py/terrascope_api/stubs/algorithm_version_pb2_grpc.py
--rw-r--r--   0 sjawahar   (501) staff       (20)     8616 2022-12-01 19:29:01.000000 terrascope-api-1.0.4/src/py/terrascope_api/stubs/analysis_computation_pb2_grpc.py
--rw-r--r--   0 sjawahar   (501) staff       (20)     6229 2022-12-01 19:29:01.000000 terrascope-api-1.0.4/src/py/terrascope_api/stubs/analysis_config_pb2_grpc.py
--rw-r--r--   0 sjawahar   (501) staff       (20)     5885 2022-12-01 19:29:02.000000 terrascope-api-1.0.4/src/py/terrascope_api/stubs/analysis_pb2_grpc.py
--rw-r--r--   0 sjawahar   (501) staff       (20)     7036 2022-12-01 19:29:02.000000 terrascope-api-1.0.4/src/py/terrascope_api/stubs/analysis_version_pb2_grpc.py
--rw-r--r--   0 sjawahar   (501) staff       (20)    11230 2022-12-01 19:29:02.000000 terrascope-api-1.0.4/src/py/terrascope_api/stubs/aoi_collection_pb2_grpc.py
--rw-r--r--   0 sjawahar   (501) staff       (20)     7568 2022-12-01 19:29:03.000000 terrascope-api-1.0.4/src/py/terrascope_api/stubs/aoi_pb2_grpc.py
--rw-r--r--   0 sjawahar   (501) staff       (20)     4489 2022-12-01 19:29:03.000000 terrascope-api-1.0.4/src/py/terrascope_api/stubs/aoi_transaction_pb2_grpc.py
--rw-r--r--   0 sjawahar   (501) staff       (20)     6123 2022-12-01 19:29:03.000000 terrascope-api-1.0.4/src/py/terrascope_api/stubs/aoi_version_pb2_grpc.py
--rw-r--r--   0 sjawahar   (501) staff       (20)      159 2022-12-01 19:29:03.000000 terrascope-api-1.0.4/src/py/terrascope_api/stubs/common_models_pb2_grpc.py
--rw-r--r--   0 sjawahar   (501) staff       (20)    14248 2022-12-01 19:29:04.000000 terrascope-api-1.0.4/src/py/terrascope_api/stubs/credit_pb2_grpc.py
--rw-r--r--   0 sjawahar   (501) staff       (20)     4073 2022-12-01 19:29:04.000000 terrascope-api-1.0.4/src/py/terrascope_api/stubs/data_source_pb2_grpc.py
--rw-r--r--   0 sjawahar   (501) staff       (20)     5475 2022-12-01 19:29:04.000000 terrascope-api-1.0.4/src/py/terrascope_api/stubs/data_type_pb2_grpc.py
--rw-r--r--   0 sjawahar   (501) staff       (20)     4476 2022-12-01 19:29:05.000000 terrascope-api-1.0.4/src/py/terrascope_api/stubs/permission_pb2_grpc.py
--rw-r--r--   0 sjawahar   (501) staff       (20)     4258 2022-12-01 19:29:05.000000 terrascope-api-1.0.4/src/py/terrascope_api/stubs/result_pb2_grpc.py
--rw-r--r--   0 sjawahar   (501) staff       (20)     2452 2022-12-01 19:29:05.000000 terrascope-api-1.0.4/src/py/terrascope_api/stubs/system_pb2_grpc.py
--rw-r--r--   0 sjawahar   (501) staff       (20)     7122 2022-12-01 19:29:05.000000 terrascope-api-1.0.4/src/py/terrascope_api/stubs/toi_pb2_grpc.py
--rw-r--r--   0 sjawahar   (501) staff       (20)     2588 2022-12-01 19:29:05.000000 terrascope-api-1.0.4/src/py/terrascope_api/stubs/token_pb2_grpc.py
--rw-r--r--   0 sjawahar   (501) staff       (20)     6023 2022-12-01 19:29:05.000000 terrascope-api-1.0.4/src/py/terrascope_api/stubs/user_collection_pb2_grpc.py
--rw-r--r--   0 sjawahar   (501) staff       (20)     7298 2022-12-01 19:29:06.000000 terrascope-api-1.0.4/src/py/terrascope_api/stubs/user_pb2_grpc.py
--rw-r--r--   0 sjawahar   (501) staff       (20)     2674 2022-12-01 19:29:06.000000 terrascope-api-1.0.4/src/py/terrascope_api/stubs/visualization_pb2_grpc.py
--rw-r--r--   0 sjawahar   (501) staff       (20)     5301 2022-12-01 17:01:43.000000 terrascope-api-1.0.4/src/py/terrascope_api/sync_client.py
-drwxr-xr-x   0 sjawahar   (501) staff       (20)        0 2022-12-01 19:44:41.775145 terrascope-api-1.0.4/src/py/terrascope_api.egg-info/
--rw-r--r--   0 sjawahar   (501) staff       (20)      164 2022-12-01 19:44:41.000000 terrascope-api-1.0.4/src/py/terrascope_api.egg-info/PKG-INFO
--rw-r--r--   0 sjawahar   (501) staff       (20)     3002 2022-12-01 19:44:41.000000 terrascope-api-1.0.4/src/py/terrascope_api.egg-info/SOURCES.txt
--rw-r--r--   0 sjawahar   (501) staff       (20)        1 2022-12-01 19:44:41.000000 terrascope-api-1.0.4/src/py/terrascope_api.egg-info/dependency_links.txt
--rw-r--r--   0 sjawahar   (501) staff       (20)       30 2022-12-01 19:44:41.000000 terrascope-api-1.0.4/src/py/terrascope_api.egg-info/requires.txt
--rw-r--r--   0 sjawahar   (501) staff       (20)       15 2022-12-01 19:44:41.000000 terrascope-api-1.0.4/src/py/terrascope_api.egg-info/top_level.txt
+drwxr-xr-x   0 sjawahar   (501) staff       (20)        0 2022-12-19 20:09:27.822223 terrascope-api-1.0.5/
+-rw-r--r--   0 sjawahar   (501) staff       (20)     1061 2022-12-12 15:59:49.000000 terrascope-api-1.0.5/LICENSE
+-rw-r--r--   0 sjawahar   (501) staff       (20)      164 2022-12-19 20:09:27.820129 terrascope-api-1.0.5/PKG-INFO
+-rw-r--r--   0 sjawahar   (501) staff       (20)      579 2022-09-14 22:43:22.000000 terrascope-api-1.0.5/README.md
+-rw-r--r--   0 sjawahar   (501) staff       (20)       38 2022-12-19 20:09:27.822517 terrascope-api-1.0.5/setup.cfg
+-rw-r--r--   0 sjawahar   (501) staff       (20)     1150 2022-12-19 20:07:44.000000 terrascope-api-1.0.5/setup.py
+drwxr-xr-x   0 sjawahar   (501) staff       (20)        0 2022-12-19 20:09:27.759745 terrascope-api-1.0.5/src/
+drwxr-xr-x   0 sjawahar   (501) staff       (20)        0 2022-12-19 20:09:27.760124 terrascope-api-1.0.5/src/py/
+drwxr-xr-x   0 sjawahar   (501) staff       (20)        0 2022-12-19 20:09:27.765404 terrascope-api-1.0.5/src/py/terrascope_api/
+-rw-r--r--   0 sjawahar   (501) staff       (20)      384 2022-12-12 15:59:49.000000 terrascope-api-1.0.5/src/py/terrascope_api/__init__.py
+-rw-r--r--   0 sjawahar   (501) staff       (20)     6051 2022-12-19 20:00:29.000000 terrascope-api-1.0.5/src/py/terrascope_api/async_client.py
+-rw-r--r--   0 sjawahar   (501) staff       (20)     3615 2022-12-12 15:59:49.000000 terrascope-api-1.0.5/src/py/terrascope_api/async_interceptors.py
+drwxr-xr-x   0 sjawahar   (501) staff       (20)        0 2022-12-19 20:09:27.792665 terrascope-api-1.0.5/src/py/terrascope_api/models/
+-rw-r--r--   0 sjawahar   (501) staff       (20)     1174 2022-12-19 20:02:45.000000 terrascope-api-1.0.5/src/py/terrascope_api/models/__init__.py
+-rw-r--r--   0 sjawahar   (501) staff       (20)     5481 2022-12-19 20:02:37.000000 terrascope-api-1.0.5/src/py/terrascope_api/models/algorithm_computation_pb2.py
+-rw-r--r--   0 sjawahar   (501) staff       (20)     7454 2022-12-19 20:02:37.000000 terrascope-api-1.0.5/src/py/terrascope_api/models/algorithm_config_pb2.py
+-rw-r--r--   0 sjawahar   (501) staff       (20)     1869 2022-12-19 20:02:38.000000 terrascope-api-1.0.5/src/py/terrascope_api/models/algorithm_manifest_pb2.py
+-rw-r--r--   0 sjawahar   (501) staff       (20)     3947 2022-12-19 20:02:38.000000 terrascope-api-1.0.5/src/py/terrascope_api/models/algorithm_pb2.py
+-rw-r--r--   0 sjawahar   (501) staff       (20)     8661 2022-12-19 20:02:38.000000 terrascope-api-1.0.5/src/py/terrascope_api/models/algorithm_version_pb2.py
+-rw-r--r--   0 sjawahar   (501) staff       (20)     5698 2022-12-19 20:02:38.000000 terrascope-api-1.0.5/src/py/terrascope_api/models/analysis_computation_pb2.py
+-rw-r--r--   0 sjawahar   (501) staff       (20)     7294 2022-12-19 20:02:38.000000 terrascope-api-1.0.5/src/py/terrascope_api/models/analysis_config_pb2.py
+-rw-r--r--   0 sjawahar   (501) staff       (20)     3860 2022-12-19 20:02:38.000000 terrascope-api-1.0.5/src/py/terrascope_api/models/analysis_pb2.py
+-rw-r--r--   0 sjawahar   (501) staff       (20)     5681 2022-12-19 20:02:38.000000 terrascope-api-1.0.5/src/py/terrascope_api/models/analysis_version_pb2.py
+-rw-r--r--   0 sjawahar   (501) staff       (20)     5461 2022-12-19 20:02:38.000000 terrascope-api-1.0.5/src/py/terrascope_api/models/aoi_collection_pb2.py
+-rw-r--r--   0 sjawahar   (501) staff       (20)     5938 2022-12-19 20:02:38.000000 terrascope-api-1.0.5/src/py/terrascope_api/models/aoi_pb2.py
+-rw-r--r--   0 sjawahar   (501) staff       (20)     2568 2022-12-19 20:02:38.000000 terrascope-api-1.0.5/src/py/terrascope_api/models/aoi_transaction_pb2.py
+-rw-r--r--   0 sjawahar   (501) staff       (20)     4446 2022-12-19 20:02:38.000000 terrascope-api-1.0.5/src/py/terrascope_api/models/aoi_version_pb2.py
+-rw-r--r--   0 sjawahar   (501) staff       (20)     1054 2022-12-19 20:02:39.000000 terrascope-api-1.0.5/src/py/terrascope_api/models/common_models_pb2.py
+-rw-r--r--   0 sjawahar   (501) staff       (20)     7251 2022-12-19 20:02:39.000000 terrascope-api-1.0.5/src/py/terrascope_api/models/credit_pb2.py
+-rw-r--r--   0 sjawahar   (501) staff       (20)     2507 2022-12-19 20:02:39.000000 terrascope-api-1.0.5/src/py/terrascope_api/models/data_source_pb2.py
+-rw-r--r--   0 sjawahar   (501) staff       (20)     2800 2022-12-19 20:02:39.000000 terrascope-api-1.0.5/src/py/terrascope_api/models/data_type_pb2.py
+-rw-r--r--   0 sjawahar   (501) staff       (20)     3423 2022-12-19 20:02:39.000000 terrascope-api-1.0.5/src/py/terrascope_api/models/permission_pb2.py
+-rw-r--r--   0 sjawahar   (501) staff       (20)     6104 2022-12-19 20:02:39.000000 terrascope-api-1.0.5/src/py/terrascope_api/models/result_pb2.py
+-rw-r--r--   0 sjawahar   (501) staff       (20)     1555 2022-12-19 20:02:39.000000 terrascope-api-1.0.5/src/py/terrascope_api/models/system_pb2.py
+-rw-r--r--   0 sjawahar   (501) staff       (20)     2586 2022-12-19 20:02:39.000000 terrascope-api-1.0.5/src/py/terrascope_api/models/tile_pb2.py
+-rw-r--r--   0 sjawahar   (501) staff       (20)     4604 2022-12-19 20:02:39.000000 terrascope-api-1.0.5/src/py/terrascope_api/models/toi_pb2.py
+-rw-r--r--   0 sjawahar   (501) staff       (20)     1565 2022-12-19 20:02:39.000000 terrascope-api-1.0.5/src/py/terrascope_api/models/token_pb2.py
+-rw-r--r--   0 sjawahar   (501) staff       (20)     3285 2022-12-19 20:02:39.000000 terrascope-api-1.0.5/src/py/terrascope_api/models/user_collection_pb2.py
+-rw-r--r--   0 sjawahar   (501) staff       (20)     3029 2022-12-19 20:02:39.000000 terrascope-api-1.0.5/src/py/terrascope_api/models/user_pb2.py
+-rw-r--r--   0 sjawahar   (501) staff       (20)     5071 2022-12-19 20:02:39.000000 terrascope-api-1.0.5/src/py/terrascope_api/models/visualization_pb2.py
+drwxr-xr-x   0 sjawahar   (501) staff       (20)        0 2022-12-19 20:09:27.817769 terrascope-api-1.0.5/src/py/terrascope_api/stubs/
+-rw-r--r--   0 sjawahar   (501) staff       (20)     1304 2022-12-19 20:02:45.000000 terrascope-api-1.0.5/src/py/terrascope_api/stubs/__init__.py
+-rw-r--r--   0 sjawahar   (501) staff       (20)     8881 2022-12-19 20:02:40.000000 terrascope-api-1.0.5/src/py/terrascope_api/stubs/algorithm_computation_pb2_grpc.py
+-rw-r--r--   0 sjawahar   (501) staff       (20)    13880 2022-12-19 20:02:40.000000 terrascope-api-1.0.5/src/py/terrascope_api/stubs/algorithm_config_pb2_grpc.py
+-rw-r--r--   0 sjawahar   (501) staff       (20)     2724 2022-12-19 20:02:40.000000 terrascope-api-1.0.5/src/py/terrascope_api/stubs/algorithm_manifest_pb2_grpc.py
+-rw-r--r--   0 sjawahar   (501) staff       (20)     7648 2022-12-19 20:02:40.000000 terrascope-api-1.0.5/src/py/terrascope_api/stubs/algorithm_pb2_grpc.py
+-rw-r--r--   0 sjawahar   (501) staff       (20)    13032 2022-12-19 20:02:41.000000 terrascope-api-1.0.5/src/py/terrascope_api/stubs/algorithm_version_pb2_grpc.py
+-rw-r--r--   0 sjawahar   (501) staff       (20)     8616 2022-12-19 20:02:41.000000 terrascope-api-1.0.5/src/py/terrascope_api/stubs/analysis_computation_pb2_grpc.py
+-rw-r--r--   0 sjawahar   (501) staff       (20)     6229 2022-12-19 20:02:41.000000 terrascope-api-1.0.5/src/py/terrascope_api/stubs/analysis_config_pb2_grpc.py
+-rw-r--r--   0 sjawahar   (501) staff       (20)     5885 2022-12-19 20:02:41.000000 terrascope-api-1.0.5/src/py/terrascope_api/stubs/analysis_pb2_grpc.py
+-rw-r--r--   0 sjawahar   (501) staff       (20)     7036 2022-12-19 20:02:41.000000 terrascope-api-1.0.5/src/py/terrascope_api/stubs/analysis_version_pb2_grpc.py
+-rw-r--r--   0 sjawahar   (501) staff       (20)    11230 2022-12-19 20:02:42.000000 terrascope-api-1.0.5/src/py/terrascope_api/stubs/aoi_collection_pb2_grpc.py
+-rw-r--r--   0 sjawahar   (501) staff       (20)     7568 2022-12-19 20:02:42.000000 terrascope-api-1.0.5/src/py/terrascope_api/stubs/aoi_pb2_grpc.py
+-rw-r--r--   0 sjawahar   (501) staff       (20)     4489 2022-12-19 20:02:42.000000 terrascope-api-1.0.5/src/py/terrascope_api/stubs/aoi_transaction_pb2_grpc.py
+-rw-r--r--   0 sjawahar   (501) staff       (20)     6123 2022-12-19 20:02:42.000000 terrascope-api-1.0.5/src/py/terrascope_api/stubs/aoi_version_pb2_grpc.py
+-rw-r--r--   0 sjawahar   (501) staff       (20)      159 2022-12-19 20:02:42.000000 terrascope-api-1.0.5/src/py/terrascope_api/stubs/common_models_pb2_grpc.py
+-rw-r--r--   0 sjawahar   (501) staff       (20)    14248 2022-12-19 20:02:43.000000 terrascope-api-1.0.5/src/py/terrascope_api/stubs/credit_pb2_grpc.py
+-rw-r--r--   0 sjawahar   (501) staff       (20)     4073 2022-12-19 20:02:43.000000 terrascope-api-1.0.5/src/py/terrascope_api/stubs/data_source_pb2_grpc.py
+-rw-r--r--   0 sjawahar   (501) staff       (20)     5475 2022-12-19 20:02:43.000000 terrascope-api-1.0.5/src/py/terrascope_api/stubs/data_type_pb2_grpc.py
+-rw-r--r--   0 sjawahar   (501) staff       (20)     4476 2022-12-19 20:02:43.000000 terrascope-api-1.0.5/src/py/terrascope_api/stubs/permission_pb2_grpc.py
+-rw-r--r--   0 sjawahar   (501) staff       (20)     4258 2022-12-19 20:02:43.000000 terrascope-api-1.0.5/src/py/terrascope_api/stubs/result_pb2_grpc.py
+-rw-r--r--   0 sjawahar   (501) staff       (20)     2452 2022-12-19 20:02:43.000000 terrascope-api-1.0.5/src/py/terrascope_api/stubs/system_pb2_grpc.py
+-rw-r--r--   0 sjawahar   (501) staff       (20)     2379 2022-12-19 20:02:44.000000 terrascope-api-1.0.5/src/py/terrascope_api/stubs/tile_pb2_grpc.py
+-rw-r--r--   0 sjawahar   (501) staff       (20)     7122 2022-12-19 20:02:44.000000 terrascope-api-1.0.5/src/py/terrascope_api/stubs/toi_pb2_grpc.py
+-rw-r--r--   0 sjawahar   (501) staff       (20)     2588 2022-12-19 20:02:44.000000 terrascope-api-1.0.5/src/py/terrascope_api/stubs/token_pb2_grpc.py
+-rw-r--r--   0 sjawahar   (501) staff       (20)     6023 2022-12-19 20:02:44.000000 terrascope-api-1.0.5/src/py/terrascope_api/stubs/user_collection_pb2_grpc.py
+-rw-r--r--   0 sjawahar   (501) staff       (20)     7298 2022-12-19 20:02:44.000000 terrascope-api-1.0.5/src/py/terrascope_api/stubs/user_pb2_grpc.py
+-rw-r--r--   0 sjawahar   (501) staff       (20)     4439 2022-12-19 20:02:44.000000 terrascope-api-1.0.5/src/py/terrascope_api/stubs/visualization_pb2_grpc.py
+-rw-r--r--   0 sjawahar   (501) staff       (20)     5507 2022-12-19 20:00:29.000000 terrascope-api-1.0.5/src/py/terrascope_api/sync_client.py
+drwxr-xr-x   0 sjawahar   (501) staff       (20)        0 2022-12-19 20:09:27.768244 terrascope-api-1.0.5/src/py/terrascope_api.egg-info/
+-rw-r--r--   0 sjawahar   (501) staff       (20)      164 2022-12-19 20:09:27.000000 terrascope-api-1.0.5/src/py/terrascope_api.egg-info/PKG-INFO
+-rw-r--r--   0 sjawahar   (501) staff       (20)     3088 2022-12-19 20:09:27.000000 terrascope-api-1.0.5/src/py/terrascope_api.egg-info/SOURCES.txt
+-rw-r--r--   0 sjawahar   (501) staff       (20)        1 2022-12-19 20:09:27.000000 terrascope-api-1.0.5/src/py/terrascope_api.egg-info/dependency_links.txt
+-rw-r--r--   0 sjawahar   (501) staff       (20)       30 2022-12-19 20:09:27.000000 terrascope-api-1.0.5/src/py/terrascope_api.egg-info/requires.txt
+-rw-r--r--   0 sjawahar   (501) staff       (20)       15 2022-12-19 20:09:27.000000 terrascope-api-1.0.5/src/py/terrascope_api.egg-info/top_level.txt
```

### Comparing `terrascope-api-1.0.4/LICENSE` & `terrascope-api-1.0.5/LICENSE`

 * *Files identical despite different names*

### Comparing `terrascope-api-1.0.4/README.md` & `terrascope-api-1.0.5/README.md`

 * *Files identical despite different names*

### Comparing `terrascope-api-1.0.4/setup.py` & `terrascope-api-1.0.5/setup.py`

 * *Files 1% similar despite different names*

```diff
@@ -32,15 +32,15 @@
 
 inject_custom_repository('orbital')
 
 EXCLUDE_FILES = []
 
 setuptools.setup(
     name='terrascope-api',
-    version='1.0.4',
+    version='1.0.5',
     description='Terrascope API Client',
     url='https://github.com/orbitalinsight/oi_papi',
     package_dir={'': 'src/py'},
     packages=setuptools.find_packages('src/py', exclude=[
         'mocked_services',
         'oi_papi',
         'oi_papi.*'
```

### Comparing `terrascope-api-1.0.4/src/py/terrascope_api/async_client.py` & `terrascope-api-1.0.5/src/py/terrascope_api/async_client.py`

 * *Files 0% similar despite different names*

```diff
@@ -47,15 +47,16 @@
             #  makes sense since it would be easy to hijack
         self.context_injecting_interceptors = [
             # materialize distributed context from request headers
             ContextInjectorUnaryUnary(), ContextInjectorUnaryStream(),
             ContextInjectorStreamUnary(), ContextInjectorStreamStream()
         ]
         self.options = [('grpc.max_send_message_length', -1),
-                        ('grpc.max_receive_message_length', -1)]
+                        ('grpc.max_receive_message_length', -1),
+                        ('grpc.max_metadata_size', 16000)]
         service_config_json = json.dumps({
             "methodConfig": [{
                 "name": [{}],  # Apply retry to all methods by using [{}]
                 "retryPolicy": {
                     "maxAttempts": 5,
                     "initialBackoff": "1.0s",
                     "maxBackoff": "60s",
@@ -83,14 +84,15 @@
         self.system = stubs.system.SystemApiStub(self._channel)
         self.toi = stubs.toi.TOIApiStub(self._channel)
         self.permission = stubs.permission.PermissionApiStub(self._channel)
         self.user = stubs.user.UserApiStub(self._channel)
         self.user_collection = stubs.user_collection.UserCollectionApiStub(self._channel)
         self.token = stubs.token.TokenApiStub(self._channel)
         self.visualization = stubs.visualization.VisualizationApiStub(self._channel)
+        self.tile = stubs.tile.TileApiStub(self._channel)
 
         self.data_source = stubs.data_source.DataSourceAPIStub(self._channel)
         self.data_type = stubs.data_type.DataTypeAPIStub(self._channel)
 
     def _get_insecure_channel(self):
         return grpc.aio.insecure_channel(f"{self._oi_papi_url}:{self._port}",
                                          options=self.options,
```

### Comparing `terrascope-api-1.0.4/src/py/terrascope_api/async_interceptors.py` & `terrascope-api-1.0.5/src/py/terrascope_api/async_interceptors.py`

 * *Files identical despite different names*

### Comparing `terrascope-api-1.0.4/src/py/terrascope_api/models/__init__.py` & `terrascope-api-1.0.5/src/py/terrascope_api/models/__init__.py`

 * *Files 2% similar despite different names*

```diff
@@ -14,12 +14,13 @@
 from . import common_models_pb2 as common_models
 from . import credit_pb2 as credit
 from . import data_source_pb2 as data_source
 from . import data_type_pb2 as data_type
 from . import permission_pb2 as permission
 from . import result_pb2 as result
 from . import system_pb2 as system
+from . import tile_pb2 as tile
 from . import toi_pb2 as toi
 from . import token_pb2 as token
 from . import user_collection_pb2 as user_collection
 from . import user_pb2 as user
 from . import visualization_pb2 as visualization
```

### Comparing `terrascope-api-1.0.4/src/py/terrascope_api/models/algorithm_computation_pb2.py` & `terrascope-api-1.0.5/src/py/terrascope_api/models/algorithm_computation_pb2.py`

 * *Files identical despite different names*

### Comparing `terrascope-api-1.0.4/src/py/terrascope_api/models/algorithm_config_pb2.py` & `terrascope-api-1.0.5/src/py/terrascope_api/models/algorithm_config_pb2.py`

 * *Files identical despite different names*

### Comparing `terrascope-api-1.0.4/src/py/terrascope_api/models/algorithm_manifest_pb2.py` & `terrascope-api-1.0.5/src/py/terrascope_api/models/algorithm_manifest_pb2.py`

 * *Files identical despite different names*

### Comparing `terrascope-api-1.0.4/src/py/terrascope_api/models/algorithm_pb2.py` & `terrascope-api-1.0.5/src/py/terrascope_api/models/algorithm_pb2.py`

 * *Files identical despite different names*

### Comparing `terrascope-api-1.0.4/src/py/terrascope_api/models/algorithm_version_pb2.py` & `terrascope-api-1.0.5/src/py/terrascope_api/models/algorithm_version_pb2.py`

 * *Files identical despite different names*

### Comparing `terrascope-api-1.0.4/src/py/terrascope_api/models/analysis_computation_pb2.py` & `terrascope-api-1.0.5/src/py/terrascope_api/models/analysis_computation_pb2.py`

 * *Files identical despite different names*

### Comparing `terrascope-api-1.0.4/src/py/terrascope_api/models/analysis_config_pb2.py` & `terrascope-api-1.0.5/src/py/terrascope_api/models/analysis_config_pb2.py`

 * *Files identical despite different names*

### Comparing `terrascope-api-1.0.4/src/py/terrascope_api/models/analysis_pb2.py` & `terrascope-api-1.0.5/src/py/terrascope_api/models/analysis_pb2.py`

 * *Files identical despite different names*

### Comparing `terrascope-api-1.0.4/src/py/terrascope_api/models/analysis_version_pb2.py` & `terrascope-api-1.0.5/src/py/terrascope_api/models/analysis_version_pb2.py`

 * *Files identical despite different names*

### Comparing `terrascope-api-1.0.4/src/py/terrascope_api/models/aoi_collection_pb2.py` & `terrascope-api-1.0.5/src/py/terrascope_api/models/aoi_collection_pb2.py`

 * *Files identical despite different names*

### Comparing `terrascope-api-1.0.4/src/py/terrascope_api/models/aoi_pb2.py` & `terrascope-api-1.0.5/src/py/terrascope_api/models/aoi_pb2.py`

 * *Files identical despite different names*

### Comparing `terrascope-api-1.0.4/src/py/terrascope_api/models/aoi_transaction_pb2.py` & `terrascope-api-1.0.5/src/py/terrascope_api/models/aoi_transaction_pb2.py`

 * *Files identical despite different names*

### Comparing `terrascope-api-1.0.4/src/py/terrascope_api/models/aoi_version_pb2.py` & `terrascope-api-1.0.5/src/py/terrascope_api/models/aoi_version_pb2.py`

 * *Files identical despite different names*

### Comparing `terrascope-api-1.0.4/src/py/terrascope_api/models/common_models_pb2.py` & `terrascope-api-1.0.5/src/py/terrascope_api/models/common_models_pb2.py`

 * *Files identical despite different names*

### Comparing `terrascope-api-1.0.4/src/py/terrascope_api/models/credit_pb2.py` & `terrascope-api-1.0.5/src/py/terrascope_api/models/credit_pb2.py`

 * *Files identical despite different names*

### Comparing `terrascope-api-1.0.4/src/py/terrascope_api/models/data_source_pb2.py` & `terrascope-api-1.0.5/src/py/terrascope_api/models/data_source_pb2.py`

 * *Files identical despite different names*

### Comparing `terrascope-api-1.0.4/src/py/terrascope_api/models/data_type_pb2.py` & `terrascope-api-1.0.5/src/py/terrascope_api/models/data_type_pb2.py`

 * *Files identical despite different names*

### Comparing `terrascope-api-1.0.4/src/py/terrascope_api/models/permission_pb2.py` & `terrascope-api-1.0.5/src/py/terrascope_api/models/permission_pb2.py`

 * *Files identical despite different names*

### Comparing `terrascope-api-1.0.4/src/py/terrascope_api/models/result_pb2.py` & `terrascope-api-1.0.5/src/py/terrascope_api/models/result_pb2.py`

 * *Files identical despite different names*

### Comparing `terrascope-api-1.0.4/src/py/terrascope_api/models/system_pb2.py` & `terrascope-api-1.0.5/src/py/terrascope_api/models/system_pb2.py`

 * *Files identical despite different names*

### Comparing `terrascope-api-1.0.4/src/py/terrascope_api/models/toi_pb2.py` & `terrascope-api-1.0.5/src/py/terrascope_api/models/toi_pb2.py`

 * *Files identical despite different names*

### Comparing `terrascope-api-1.0.4/src/py/terrascope_api/models/token_pb2.py` & `terrascope-api-1.0.5/src/py/terrascope_api/models/token_pb2.py`

 * *Files identical despite different names*

### Comparing `terrascope-api-1.0.4/src/py/terrascope_api/models/user_collection_pb2.py` & `terrascope-api-1.0.5/src/py/terrascope_api/models/user_collection_pb2.py`

 * *Files identical despite different names*

### Comparing `terrascope-api-1.0.4/src/py/terrascope_api/models/user_pb2.py` & `terrascope-api-1.0.5/src/py/terrascope_api/models/user_pb2.py`

 * *Files identical despite different names*

### Comparing `terrascope-api-1.0.4/src/py/terrascope_api/models/visualization_pb2.py` & `terrascope-api-1.0.5/src/py/terrascope_api/models/visualization_pb2.py`

 * *Files 23% similar despite different names*

```diff
@@ -11,15 +11,15 @@
 _sym_db = _symbol_database.Default()
 
 
 from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
 from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
 
 
-DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x13visualization.proto\x12\x15oi.papi.visualization\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\xad\x05\n\rVisualization\x12\n\n\x02id\x18\x01 \x01(\t\x12\x16\n\x0e\x63omputation_id\x18\x02 \x01(\t\x12\x1d\n\x15result_observation_id\x18\x03 \x01(\t\x12\x37\n\x04type\x18\x04 \x01(\x0e\x32).oi.papi.visualization.Visualization.Type\x12\x39\n\x05state\x18\x05 \x01(\x0e\x32*.oi.papi.visualization.Visualization.State\x12)\n\x08metadata\x18\x06 \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x44\n\x0b\x61\x63\x63\x65ss_info\x18\x07 \x01(\x0b\x32/.oi.papi.visualization.Visualization.AccessInfo\x12.\n\ncreated_on\x18\x08 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12.\n\nupdated_on\x18\t \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x1aP\n\nAccessInfo\x12\x14\n\x0curl_template\x18\x01 \x01(\t\x12,\n\x0b\x63redentials\x18\x02 \x01(\x0b\x32\x17.google.protobuf.Struct\"A\n\x04Type\x12\x10\n\x0cUNKNOWN_TYPE\x10\x00\x12\x0c\n\x08STANDARD\x10\x01\x12\x0b\n\x07SPATIAL\x10\x02\x12\x0c\n\x08TEMPORAL\x10\x03\"\x7f\n\x05State\x12\x11\n\rUNKNOWN_STATE\x10\x00\x12\x07\n\x03NEW\x10\x01\x12\n\n\x06QUEUED\x10\x02\x12\x0e\n\nVALIDATING\x10\x03\x12\t\n\x05\x45MPTY\x10\x04\x12\x0c\n\x08UPLOADED\x10\x05\x12\n\n\x06\x46\x41ILED\x10\x06\x12\x0c\n\x08\x44\x45LETING\x10\x07\x12\x0b\n\x07\x44\x45LETED\x10\x08\"9\n\x17VisualizationGetRequest\x12\x1e\n\x16result_observation_ids\x18\x01 \x03(\t\"m\n\x18VisualizationGetResponse\x12\x13\n\x0bstatus_code\x18\x01 \x01(\r\x12<\n\x0evisualizations\x18\x02 \x03(\x0b\x32$.oi.papi.visualization.Visualization2z\n\x10VisualizationApi\x12\x66\n\x03get\x12..oi.papi.visualization.VisualizationGetRequest\x1a/.oi.papi.visualization.VisualizationGetResponseb\x06proto3')
+DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x13visualization.proto\x12\x15oi.papi.visualization\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\xad\x05\n\rVisualization\x12\n\n\x02id\x18\x01 \x01(\t\x12\x16\n\x0e\x63omputation_id\x18\x02 \x01(\t\x12\x1d\n\x15result_observation_id\x18\x03 \x01(\t\x12\x37\n\x04type\x18\x04 \x01(\x0e\x32).oi.papi.visualization.Visualization.Type\x12\x39\n\x05state\x18\x05 \x01(\x0e\x32*.oi.papi.visualization.Visualization.State\x12)\n\x08metadata\x18\x06 \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x44\n\x0b\x61\x63\x63\x65ss_info\x18\x07 \x01(\x0b\x32/.oi.papi.visualization.Visualization.AccessInfo\x12.\n\ncreated_on\x18\x08 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12.\n\nupdated_on\x18\t \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x1aP\n\nAccessInfo\x12\x14\n\x0curl_template\x18\x01 \x01(\t\x12,\n\x0b\x63redentials\x18\x02 \x01(\x0b\x32\x17.google.protobuf.Struct\"A\n\x04Type\x12\x10\n\x0cUNKNOWN_TYPE\x10\x00\x12\x0c\n\x08STANDARD\x10\x01\x12\x0b\n\x07SPATIAL\x10\x02\x12\x0c\n\x08TEMPORAL\x10\x03\"\x7f\n\x05State\x12\x11\n\rUNKNOWN_STATE\x10\x00\x12\x07\n\x03NEW\x10\x01\x12\n\n\x06QUEUED\x10\x02\x12\x0e\n\nVALIDATING\x10\x03\x12\t\n\x05\x45MPTY\x10\x04\x12\x0c\n\x08UPLOADED\x10\x05\x12\n\n\x06\x46\x41ILED\x10\x06\x12\x0c\n\x08\x44\x45LETING\x10\x07\x12\x0b\n\x07\x44\x45LETED\x10\x08\"9\n\x17VisualizationGetRequest\x12\x1e\n\x16result_observation_ids\x18\x01 \x03(\t\"m\n\x18VisualizationGetResponse\x12\x13\n\x0bstatus_code\x18\x01 \x01(\r\x12<\n\x0evisualizations\x18\x02 \x03(\x0b\x32$.oi.papi.visualization.Visualization\"\xdd\x01\n\nVisualizer\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12I\n\x0fvisualizer_type\x18\x03 \x01(\x0e\x32\x30.oi.papi.visualization.Visualizer.VisualizerType\x12\x11\n\tdata_type\x18\x04 \x01(\t\"W\n\x0eVisualizerType\x12\x1b\n\x17UNKNOWN_VISUALIZER_TYPE\x10\x00\x12\n\n\x06KEPLER\x10\x01\x12\x1c\n\x18OI_VISUALIZATION_SERVICE\x10\x02\"~\n\x10VisualizerConfig\x12\n\n\x02id\x18\x01 \x01(\t\x12\'\n\x06\x63onfig\x18\x02 \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x35\n\nvisualizer\x18\x03 \x01(\x0b\x32!.oi.papi.visualization.Visualizer\"y\n\x14VisualizerConfigAlgo\x12\x1c\n\x14\x61lgorithm_version_id\x18\x01 \x01(\t\x12\x43\n\x12visualizer_configs\x18\x02 \x03(\x0b\x32\'.oi.papi.visualization.VisualizerConfig\"?\n\x1eVisualizerConfigAlgoGetRequest\x12\x1d\n\x15\x61lgorithm_version_ids\x18\x01 \x03(\t\"\x84\x01\n\x1fVisualizerConfigAlgoGetResponse\x12\x13\n\x0bstatus_code\x18\x01 \x01(\r\x12L\n\x17visualizer_config_algos\x18\x02 \x03(\x0b\x32+.oi.papi.visualization.VisualizerConfigAlgo2\xfd\x01\n\x10VisualizationApi\x12\x66\n\x03get\x12..oi.papi.visualization.VisualizationGetRequest\x1a/.oi.papi.visualization.VisualizationGetResponse\x12\x80\x01\n\x0fget_config_algo\x12\x35.oi.papi.visualization.VisualizerConfigAlgoGetRequest\x1a\x36.oi.papi.visualization.VisualizerConfigAlgoGetResponseb\x06proto3')
 
 _builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
 _builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'visualization_pb2', globals())
 if _descriptor._USE_C_DESCRIPTORS == False:
 
   DESCRIPTOR._options = None
   _VISUALIZATION._serialized_start=110
@@ -30,10 +30,22 @@
   _VISUALIZATION_TYPE._serialized_end=666
   _VISUALIZATION_STATE._serialized_start=668
   _VISUALIZATION_STATE._serialized_end=795
   _VISUALIZATIONGETREQUEST._serialized_start=797
   _VISUALIZATIONGETREQUEST._serialized_end=854
   _VISUALIZATIONGETRESPONSE._serialized_start=856
   _VISUALIZATIONGETRESPONSE._serialized_end=965
-  _VISUALIZATIONAPI._serialized_start=967
-  _VISUALIZATIONAPI._serialized_end=1089
+  _VISUALIZER._serialized_start=968
+  _VISUALIZER._serialized_end=1189
+  _VISUALIZER_VISUALIZERTYPE._serialized_start=1102
+  _VISUALIZER_VISUALIZERTYPE._serialized_end=1189
+  _VISUALIZERCONFIG._serialized_start=1191
+  _VISUALIZERCONFIG._serialized_end=1317
+  _VISUALIZERCONFIGALGO._serialized_start=1319
+  _VISUALIZERCONFIGALGO._serialized_end=1440
+  _VISUALIZERCONFIGALGOGETREQUEST._serialized_start=1442
+  _VISUALIZERCONFIGALGOGETREQUEST._serialized_end=1505
+  _VISUALIZERCONFIGALGOGETRESPONSE._serialized_start=1508
+  _VISUALIZERCONFIGALGOGETRESPONSE._serialized_end=1640
+  _VISUALIZATIONAPI._serialized_start=1643
+  _VISUALIZATIONAPI._serialized_end=1896
 # @@protoc_insertion_point(module_scope)
```

### Comparing `terrascope-api-1.0.4/src/py/terrascope_api/stubs/__init__.py` & `terrascope-api-1.0.5/src/py/terrascope_api/stubs/__init__.py`

 * *Files 2% similar despite different names*

```diff
@@ -14,12 +14,13 @@
 from . import common_models_pb2_grpc as common_models
 from . import credit_pb2_grpc as credit
 from . import data_source_pb2_grpc as data_source
 from . import data_type_pb2_grpc as data_type
 from . import permission_pb2_grpc as permission
 from . import result_pb2_grpc as result
 from . import system_pb2_grpc as system
+from . import tile_pb2_grpc as tile
 from . import toi_pb2_grpc as toi
 from . import token_pb2_grpc as token
 from . import user_collection_pb2_grpc as user_collection
 from . import user_pb2_grpc as user
 from . import visualization_pb2_grpc as visualization
```

### Comparing `terrascope-api-1.0.4/src/py/terrascope_api/stubs/algorithm_computation_pb2_grpc.py` & `terrascope-api-1.0.5/src/py/terrascope_api/stubs/algorithm_computation_pb2_grpc.py`

 * *Files identical despite different names*

### Comparing `terrascope-api-1.0.4/src/py/terrascope_api/stubs/algorithm_config_pb2_grpc.py` & `terrascope-api-1.0.5/src/py/terrascope_api/stubs/algorithm_config_pb2_grpc.py`

 * *Files identical despite different names*

### Comparing `terrascope-api-1.0.4/src/py/terrascope_api/stubs/algorithm_manifest_pb2_grpc.py` & `terrascope-api-1.0.5/src/py/terrascope_api/stubs/algorithm_manifest_pb2_grpc.py`

 * *Files identical despite different names*

### Comparing `terrascope-api-1.0.4/src/py/terrascope_api/stubs/algorithm_pb2_grpc.py` & `terrascope-api-1.0.5/src/py/terrascope_api/stubs/algorithm_pb2_grpc.py`

 * *Files identical despite different names*

### Comparing `terrascope-api-1.0.4/src/py/terrascope_api/stubs/algorithm_version_pb2_grpc.py` & `terrascope-api-1.0.5/src/py/terrascope_api/stubs/algorithm_version_pb2_grpc.py`

 * *Files identical despite different names*

### Comparing `terrascope-api-1.0.4/src/py/terrascope_api/stubs/analysis_computation_pb2_grpc.py` & `terrascope-api-1.0.5/src/py/terrascope_api/stubs/analysis_computation_pb2_grpc.py`

 * *Files identical despite different names*

### Comparing `terrascope-api-1.0.4/src/py/terrascope_api/stubs/analysis_config_pb2_grpc.py` & `terrascope-api-1.0.5/src/py/terrascope_api/stubs/analysis_config_pb2_grpc.py`

 * *Files identical despite different names*

### Comparing `terrascope-api-1.0.4/src/py/terrascope_api/stubs/analysis_pb2_grpc.py` & `terrascope-api-1.0.5/src/py/terrascope_api/stubs/analysis_pb2_grpc.py`

 * *Files identical despite different names*

### Comparing `terrascope-api-1.0.4/src/py/terrascope_api/stubs/analysis_version_pb2_grpc.py` & `terrascope-api-1.0.5/src/py/terrascope_api/stubs/analysis_version_pb2_grpc.py`

 * *Files identical despite different names*

### Comparing `terrascope-api-1.0.4/src/py/terrascope_api/stubs/aoi_collection_pb2_grpc.py` & `terrascope-api-1.0.5/src/py/terrascope_api/stubs/aoi_collection_pb2_grpc.py`

 * *Files identical despite different names*

### Comparing `terrascope-api-1.0.4/src/py/terrascope_api/stubs/aoi_pb2_grpc.py` & `terrascope-api-1.0.5/src/py/terrascope_api/stubs/aoi_pb2_grpc.py`

 * *Files identical despite different names*

### Comparing `terrascope-api-1.0.4/src/py/terrascope_api/stubs/aoi_transaction_pb2_grpc.py` & `terrascope-api-1.0.5/src/py/terrascope_api/stubs/aoi_transaction_pb2_grpc.py`

 * *Files identical despite different names*

### Comparing `terrascope-api-1.0.4/src/py/terrascope_api/stubs/aoi_version_pb2_grpc.py` & `terrascope-api-1.0.5/src/py/terrascope_api/stubs/aoi_version_pb2_grpc.py`

 * *Files identical despite different names*

### Comparing `terrascope-api-1.0.4/src/py/terrascope_api/stubs/credit_pb2_grpc.py` & `terrascope-api-1.0.5/src/py/terrascope_api/stubs/credit_pb2_grpc.py`

 * *Files identical despite different names*

### Comparing `terrascope-api-1.0.4/src/py/terrascope_api/stubs/data_source_pb2_grpc.py` & `terrascope-api-1.0.5/src/py/terrascope_api/stubs/data_source_pb2_grpc.py`

 * *Files identical despite different names*

### Comparing `terrascope-api-1.0.4/src/py/terrascope_api/stubs/data_type_pb2_grpc.py` & `terrascope-api-1.0.5/src/py/terrascope_api/stubs/data_type_pb2_grpc.py`

 * *Files identical despite different names*

### Comparing `terrascope-api-1.0.4/src/py/terrascope_api/stubs/permission_pb2_grpc.py` & `terrascope-api-1.0.5/src/py/terrascope_api/stubs/permission_pb2_grpc.py`

 * *Files identical despite different names*

### Comparing `terrascope-api-1.0.4/src/py/terrascope_api/stubs/result_pb2_grpc.py` & `terrascope-api-1.0.5/src/py/terrascope_api/stubs/result_pb2_grpc.py`

 * *Files identical despite different names*

### Comparing `terrascope-api-1.0.4/src/py/terrascope_api/stubs/system_pb2_grpc.py` & `terrascope-api-1.0.5/src/py/terrascope_api/stubs/system_pb2_grpc.py`

 * *Files identical despite different names*

### Comparing `terrascope-api-1.0.4/src/py/terrascope_api/stubs/toi_pb2_grpc.py` & `terrascope-api-1.0.5/src/py/terrascope_api/stubs/toi_pb2_grpc.py`

 * *Files identical despite different names*

### Comparing `terrascope-api-1.0.4/src/py/terrascope_api/stubs/token_pb2_grpc.py` & `terrascope-api-1.0.5/src/py/terrascope_api/stubs/token_pb2_grpc.py`

 * *Files identical despite different names*

### Comparing `terrascope-api-1.0.4/src/py/terrascope_api/stubs/user_collection_pb2_grpc.py` & `terrascope-api-1.0.5/src/py/terrascope_api/stubs/user_collection_pb2_grpc.py`

 * *Files identical despite different names*

### Comparing `terrascope-api-1.0.4/src/py/terrascope_api/stubs/user_pb2_grpc.py` & `terrascope-api-1.0.5/src/py/terrascope_api/stubs/user_pb2_grpc.py`

 * *Files identical despite different names*

### Comparing `terrascope-api-1.0.4/src/py/terrascope_api/sync_client.py` & `terrascope-api-1.0.5/src/py/terrascope_api/sync_client.py`

 * *Files 1% similar despite different names*

```diff
@@ -15,14 +15,15 @@
 from terrascope_api.stubs import system_pb2_grpc as system_pb2_grpc
 from terrascope_api.stubs import aoi_pb2_grpc as aoi_pb2_grpc
 from terrascope_api.stubs import aoi_collection_pb2_grpc as aoi_collection_pb2_grpc
 from terrascope_api.stubs import aoi_version_pb2_grpc as aoi_version_pb2_grpc
 from terrascope_api.stubs import aoi_transaction_pb2_grpc as aoi_transaction_pb2_grpc
 from terrascope_api.stubs import algorithm_computation_pb2_grpc as algorithm_computation_pb2_grpc
 from terrascope_api.stubs import visualization_pb2_grpc as visualization_pb2_grpc
+from terrascope_api.stubs import tile_pb2_grpc as tile_pb2_grpc
 from terrascope_api.stubs import user_pb2_grpc as user_pb2_grpc
 from terrascope_api.stubs import user_collection_pb2_grpc as user_collection_pb2_grpc
 from terrascope_api.stubs import token_pb2_grpc as token_pb2_grpc
 from terrascope_api.stubs import permission_pb2_grpc as permission_pb2_grpc
 from terrascope_api.stubs import algorithm_pb2_grpc as algorithm_pb2_grpc
 from terrascope_api.stubs import algorithm_version_pb2_grpc as algorithm_version_pb2_grpc
 from terrascope_api.stubs import algorithm_config_pb2_grpc as algorithm_config_pb2_grpc
@@ -53,14 +54,15 @@
         self.system = system_pb2_grpc.SystemApiStub(self._channel)
         self.aoi = aoi_pb2_grpc.AOIApiStub(self._channel)
         self.aoi_collection = aoi_collection_pb2_grpc.AOICollectionApiStub(self._channel)
         self.aoi_version = aoi_version_pb2_grpc.AOIVersionApiStub(self._channel)
         self.aoi_transaction = aoi_transaction_pb2_grpc.AOITransactionApiStub(self._channel)
         self.computation = algorithm_computation_pb2_grpc.AlgorithmComputationApiStub(self._channel)
         self.visualization = visualization_pb2_grpc.VisualizationApiStub(self._channel)
+        self.tile = tile_pb2_grpc.TileApiStub(self._channel)
         self.permission = permission_pb2_grpc.PermissionApiStub(self._channel)
         self.user = user_pb2_grpc.UserApiStub(self._channel)
         self.user_collection = user_collection_pb2_grpc.UserCollectionApiStub(self._channel)
         self.token = token_pb2_grpc.TokenApiStub(self._channel)
         self.algorithm = algorithm_pb2_grpc.AlgorithmApiStub(self._channel)
         self.algorithm_version = algorithm_version_pb2_grpc.AlgorithmVersionApiStub(self._channel)
         self.algorithm_config = algorithm_config_pb2_grpc.AlgorithmConfigApiStub(self._channel)
@@ -73,15 +75,16 @@
         self.analysis_computation = analysis_computation_pb2_grpc.AnalysisComputationApiStub(self._channel)
         self.data_source = data_source_pb2_grpc.DataSourceAPIStub(self._channel)
         self.data_type = data_type_pb2_grpc.DataTypeAPIStub(self._channel)
 
     def _get_insecure_channel(self):
         return grpc.insecure_channel(f"{self._oi_papi_url}:{self._port}",
                                      options=[('grpc.max_send_message_length', -1),
-                                              ('grpc.max_receive_message_length', -1)]
+                                              ('grpc.max_receive_message_length', -1),
+                                              ('grpc.max_metadata_size', 16000)]
                                      )
 
     def _get_secure_channel(self):
         creds = grpc.ssl_channel_credentials(root_certificates=None, private_key=None, certificate_chain=None)
         return grpc.secure_channel(f"{self._oi_papi_url}:{self._port}", creds, compression=None,
                                    options=[('grpc.max_send_message_length', -1),
                                             ('grpc.max_receive_message_length', -1)])
```

### Comparing `terrascope-api-1.0.4/src/py/terrascope_api.egg-info/SOURCES.txt` & `terrascope-api-1.0.5/src/py/terrascope_api.egg-info/SOURCES.txt`

 * *Files 2% similar despite different names*

```diff
@@ -27,14 +27,15 @@
 src/py/terrascope_api/models/common_models_pb2.py
 src/py/terrascope_api/models/credit_pb2.py
 src/py/terrascope_api/models/data_source_pb2.py
 src/py/terrascope_api/models/data_type_pb2.py
 src/py/terrascope_api/models/permission_pb2.py
 src/py/terrascope_api/models/result_pb2.py
 src/py/terrascope_api/models/system_pb2.py
+src/py/terrascope_api/models/tile_pb2.py
 src/py/terrascope_api/models/toi_pb2.py
 src/py/terrascope_api/models/token_pb2.py
 src/py/terrascope_api/models/user_collection_pb2.py
 src/py/terrascope_api/models/user_pb2.py
 src/py/terrascope_api/models/visualization_pb2.py
 src/py/terrascope_api/stubs/__init__.py
 src/py/terrascope_api/stubs/algorithm_computation_pb2_grpc.py
@@ -53,12 +54,13 @@
 src/py/terrascope_api/stubs/common_models_pb2_grpc.py
 src/py/terrascope_api/stubs/credit_pb2_grpc.py
 src/py/terrascope_api/stubs/data_source_pb2_grpc.py
 src/py/terrascope_api/stubs/data_type_pb2_grpc.py
 src/py/terrascope_api/stubs/permission_pb2_grpc.py
 src/py/terrascope_api/stubs/result_pb2_grpc.py
 src/py/terrascope_api/stubs/system_pb2_grpc.py
+src/py/terrascope_api/stubs/tile_pb2_grpc.py
 src/py/terrascope_api/stubs/toi_pb2_grpc.py
 src/py/terrascope_api/stubs/token_pb2_grpc.py
 src/py/terrascope_api/stubs/user_collection_pb2_grpc.py
 src/py/terrascope_api/stubs/user_pb2_grpc.py
 src/py/terrascope_api/stubs/visualization_pb2_grpc.py
```

