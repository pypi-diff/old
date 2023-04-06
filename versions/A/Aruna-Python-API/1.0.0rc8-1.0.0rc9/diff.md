# Comparing `tmp/Aruna-Python-API-1.0.0rc8.tar.gz` & `tmp/Aruna-Python-API-1.0.0rc9.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "Aruna-Python-API-1.0.0rc8.tar", last modified: Thu Mar 16 10:12:11 2023, max compression
+gzip compressed data, was "Aruna-Python-API-1.0.0rc9.tar", last modified: Thu Mar 16 14:03:43 2023, max compression
```

## Comparing `Aruna-Python-API-1.0.0rc8.tar` & `Aruna-Python-API-1.0.0rc9.tar`

### file list

```diff
@@ -1,81 +1,81 @@
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-16 10:12:11.559564 Aruna-Python-API-1.0.0rc8/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-16 10:12:11.551564 Aruna-Python-API-1.0.0rc8/Aruna_Python_API.egg-info/
--rw-r--r--   0 runner    (1001) docker     (123)     2500 2023-03-16 10:12:11.000000 Aruna-Python-API-1.0.0rc8/Aruna_Python_API.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)     2949 2023-03-16 10:12:11.000000 Aruna-Python-API-1.0.0rc8/Aruna_Python_API.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-03-16 10:12:11.000000 Aruna-Python-API-1.0.0rc8/Aruna_Python_API.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (123)       83 2023-03-16 10:12:11.000000 Aruna-Python-API-1.0.0rc8/Aruna_Python_API.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (123)        6 2023-03-16 10:12:11.000000 Aruna-Python-API-1.0.0rc8/Aruna_Python_API.egg-info/top_level.txt
--rw-r--r--   0 runner    (1001) docker     (123)    11357 2023-03-16 10:11:42.000000 Aruna-Python-API-1.0.0rc8/LICENSE
--rw-r--r--   0 runner    (1001) docker     (123)     2500 2023-03-16 10:12:11.559564 Aruna-Python-API-1.0.0rc8/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)     2095 2023-03-16 10:11:42.000000 Aruna-Python-API-1.0.0rc8/README.md
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-16 10:12:11.551564 Aruna-Python-API-1.0.0rc8/aruna/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-16 10:11:42.000000 Aruna-Python-API-1.0.0rc8/aruna/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-16 10:12:11.551564 Aruna-Python-API-1.0.0rc8/aruna/api/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-16 10:11:42.000000 Aruna-Python-API-1.0.0rc8/aruna/api/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-16 10:12:11.551564 Aruna-Python-API-1.0.0rc8/aruna/api/internal/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-16 10:11:42.000000 Aruna-Python-API-1.0.0rc8/aruna/api/internal/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-16 10:12:11.551564 Aruna-Python-API-1.0.0rc8/aruna/api/internal/v1/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-16 10:11:42.000000 Aruna-Python-API-1.0.0rc8/aruna/api/internal/v1/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     3510 2023-03-16 10:11:58.000000 Aruna-Python-API-1.0.0rc8/aruna/api/internal/v1/authorize_pb2.py
--rw-r--r--   0 runner    (1001) docker     (123)     2584 2023-03-16 10:11:58.000000 Aruna-Python-API-1.0.0rc8/aruna/api/internal/v1/authorize_pb2.pyi
--rw-r--r--   0 runner    (1001) docker     (123)     4675 2023-03-16 10:11:58.000000 Aruna-Python-API-1.0.0rc8/aruna/api/internal/v1/authorize_pb2_grpc.py
--rw-r--r--   0 runner    (1001) docker     (123)     7652 2023-03-16 10:11:58.000000 Aruna-Python-API-1.0.0rc8/aruna/api/internal/v1/notification_pb2.py
--rw-r--r--   0 runner    (1001) docker     (123)     7448 2023-03-16 10:11:58.000000 Aruna-Python-API-1.0.0rc8/aruna/api/internal/v1/notification_pb2.pyi
--rw-r--r--   0 runner    (1001) docker     (123)    11854 2023-03-16 10:11:58.000000 Aruna-Python-API-1.0.0rc8/aruna/api/internal/v1/notification_pb2_grpc.py
--rw-r--r--   0 runner    (1001) docker     (123)     8578 2023-03-16 10:11:58.000000 Aruna-Python-API-1.0.0rc8/aruna/api/internal/v1/proxy_pb2.py
--rw-r--r--   0 runner    (1001) docker     (123)     7568 2023-03-16 10:11:58.000000 Aruna-Python-API-1.0.0rc8/aruna/api/internal/v1/proxy_pb2.pyi
--rw-r--r--   0 runner    (1001) docker     (123)    18735 2023-03-16 10:11:58.000000 Aruna-Python-API-1.0.0rc8/aruna/api/internal/v1/proxy_pb2_grpc.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-16 10:12:11.551564 Aruna-Python-API-1.0.0rc8/aruna/api/notification/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-16 10:11:42.000000 Aruna-Python-API-1.0.0rc8/aruna/api/notification/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-16 10:12:11.551564 Aruna-Python-API-1.0.0rc8/aruna/api/notification/services/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-16 10:11:42.000000 Aruna-Python-API-1.0.0rc8/aruna/api/notification/services/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-16 10:12:11.555564 Aruna-Python-API-1.0.0rc8/aruna/api/notification/services/v1/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-16 10:11:42.000000 Aruna-Python-API-1.0.0rc8/aruna/api/notification/services/v1/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     7956 2023-03-16 10:11:58.000000 Aruna-Python-API-1.0.0rc8/aruna/api/notification/services/v1/notification_service_pb2.py
--rw-r--r--   0 runner    (1001) docker     (123)     6624 2023-03-16 10:11:58.000000 Aruna-Python-API-1.0.0rc8/aruna/api/notification/services/v1/notification_service_pb2.pyi
--rw-r--r--   0 runner    (1001) docker     (123)    12858 2023-03-16 10:11:58.000000 Aruna-Python-API-1.0.0rc8/aruna/api/notification/services/v1/notification_service_pb2_grpc.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-16 10:12:11.555564 Aruna-Python-API-1.0.0rc8/aruna/api/storage/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-16 10:11:42.000000 Aruna-Python-API-1.0.0rc8/aruna/api/storage/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-16 10:12:11.555564 Aruna-Python-API-1.0.0rc8/aruna/api/storage/models/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-16 10:11:42.000000 Aruna-Python-API-1.0.0rc8/aruna/api/storage/models/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-16 10:12:11.555564 Aruna-Python-API-1.0.0rc8/aruna/api/storage/models/v1/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-16 10:11:42.000000 Aruna-Python-API-1.0.0rc8/aruna/api/storage/models/v1/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     4528 2023-03-16 10:11:58.000000 Aruna-Python-API-1.0.0rc8/aruna/api/storage/models/v1/auth_pb2.py
--rw-r--r--   0 runner    (1001) docker     (123)     5466 2023-03-16 10:11:58.000000 Aruna-Python-API-1.0.0rc8/aruna/api/storage/models/v1/auth_pb2.pyi
--rw-r--r--   0 runner    (1001) docker     (123)      159 2023-03-16 10:11:58.000000 Aruna-Python-API-1.0.0rc8/aruna/api/storage/models/v1/auth_pb2_grpc.py
--rw-r--r--   0 runner    (1001) docker     (123)    13949 2023-03-16 10:11:58.000000 Aruna-Python-API-1.0.0rc8/aruna/api/storage/models/v1/models_pb2.py
--rw-r--r--   0 runner    (1001) docker     (123)    19733 2023-03-16 10:11:58.000000 Aruna-Python-API-1.0.0rc8/aruna/api/storage/models/v1/models_pb2.pyi
--rw-r--r--   0 runner    (1001) docker     (123)      159 2023-03-16 10:11:58.000000 Aruna-Python-API-1.0.0rc8/aruna/api/storage/models/v1/models_pb2_grpc.py
--rw-r--r--   0 runner    (1001) docker     (123)     1966 2023-03-16 10:11:58.000000 Aruna-Python-API-1.0.0rc8/aruna/api/storage/models/v1/query_pb2.py
--rw-r--r--   0 runner    (1001) docker     (123)     1557 2023-03-16 10:11:58.000000 Aruna-Python-API-1.0.0rc8/aruna/api/storage/models/v1/query_pb2.pyi
--rw-r--r--   0 runner    (1001) docker     (123)      159 2023-03-16 10:11:58.000000 Aruna-Python-API-1.0.0rc8/aruna/api/storage/models/v1/query_pb2_grpc.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-16 10:12:11.555564 Aruna-Python-API-1.0.0rc8/aruna/api/storage/services/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-16 10:11:42.000000 Aruna-Python-API-1.0.0rc8/aruna/api/storage/services/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-16 10:12:11.559564 Aruna-Python-API-1.0.0rc8/aruna/api/storage/services/v1/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-16 10:11:42.000000 Aruna-Python-API-1.0.0rc8/aruna/api/storage/services/v1/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     8427 2023-03-16 10:11:58.000000 Aruna-Python-API-1.0.0rc8/aruna/api/storage/services/v1/collection_service_pb2.py
--rw-r--r--   0 runner    (1001) docker     (123)     6036 2023-03-16 10:11:58.000000 Aruna-Python-API-1.0.0rc8/aruna/api/storage/services/v1/collection_service_pb2.pyi
--rw-r--r--   0 runner    (1001) docker     (123)    14738 2023-03-16 10:11:58.000000 Aruna-Python-API-1.0.0rc8/aruna/api/storage/services/v1/collection_service_pb2_grpc.py
--rw-r--r--   0 runner    (1001) docker     (123)     6081 2023-03-16 10:11:58.000000 Aruna-Python-API-1.0.0rc8/aruna/api/storage/services/v1/endpoint_service_pb2.py
--rw-r--r--   0 runner    (1001) docker     (123)     3482 2023-03-16 10:11:58.000000 Aruna-Python-API-1.0.0rc8/aruna/api/storage/services/v1/endpoint_service_pb2.pyi
--rw-r--r--   0 runner    (1001) docker     (123)    11442 2023-03-16 10:11:58.000000 Aruna-Python-API-1.0.0rc8/aruna/api/storage/services/v1/endpoint_service_pb2_grpc.py
--rw-r--r--   0 runner    (1001) docker     (123)     6748 2023-03-16 10:11:58.000000 Aruna-Python-API-1.0.0rc8/aruna/api/storage/services/v1/info_service_pb2.py
--rw-r--r--   0 runner    (1001) docker     (123)     5186 2023-03-16 10:11:58.000000 Aruna-Python-API-1.0.0rc8/aruna/api/storage/services/v1/info_service_pb2.pyi
--rw-r--r--   0 runner    (1001) docker     (123)     9125 2023-03-16 10:11:58.000000 Aruna-Python-API-1.0.0rc8/aruna/api/storage/services/v1/info_service_pb2_grpc.py
--rw-r--r--   0 runner    (1001) docker     (123)    29817 2023-03-16 10:11:58.000000 Aruna-Python-API-1.0.0rc8/aruna/api/storage/services/v1/object_service_pb2.py
--rw-r--r--   0 runner    (1001) docker     (123)    23315 2023-03-16 10:11:58.000000 Aruna-Python-API-1.0.0rc8/aruna/api/storage/services/v1/object_service_pb2.pyi
--rw-r--r--   0 runner    (1001) docker     (123)    55158 2023-03-16 10:11:58.000000 Aruna-Python-API-1.0.0rc8/aruna/api/storage/services/v1/object_service_pb2_grpc.py
--rw-r--r--   0 runner    (1001) docker     (123)    12477 2023-03-16 10:11:58.000000 Aruna-Python-API-1.0.0rc8/aruna/api/storage/services/v1/objectgroup_service_pb2.py
--rw-r--r--   0 runner    (1001) docker     (123)     9532 2023-03-16 10:11:58.000000 Aruna-Python-API-1.0.0rc8/aruna/api/storage/services/v1/objectgroup_service_pb2.pyi
--rw-r--r--   0 runner    (1001) docker     (123)    21104 2023-03-16 10:11:58.000000 Aruna-Python-API-1.0.0rc8/aruna/api/storage/services/v1/objectgroup_service_pb2_grpc.py
--rw-r--r--   0 runner    (1001) docker     (123)    10158 2023-03-16 10:11:58.000000 Aruna-Python-API-1.0.0rc8/aruna/api/storage/services/v1/project_service_pb2.py
--rw-r--r--   0 runner    (1001) docker     (123)     5091 2023-03-16 10:11:58.000000 Aruna-Python-API-1.0.0rc8/aruna/api/storage/services/v1/project_service_pb2.pyi
--rw-r--r--   0 runner    (1001) docker     (123)    19904 2023-03-16 10:11:58.000000 Aruna-Python-API-1.0.0rc8/aruna/api/storage/services/v1/project_service_pb2_grpc.py
--rw-r--r--   0 runner    (1001) docker     (123)    11655 2023-03-16 10:11:58.000000 Aruna-Python-API-1.0.0rc8/aruna/api/storage/services/v1/service_account_service_pb2.py
--rw-r--r--   0 runner    (1001) docker     (123)     6593 2023-03-16 10:11:58.000000 Aruna-Python-API-1.0.0rc8/aruna/api/storage/services/v1/service_account_service_pb2.pyi
--rw-r--r--   0 runner    (1001) docker     (123)    22042 2023-03-16 10:11:58.000000 Aruna-Python-API-1.0.0rc8/aruna/api/storage/services/v1/service_account_service_pb2_grpc.py
--rw-r--r--   0 runner    (1001) docker     (123)    11124 2023-03-16 10:11:58.000000 Aruna-Python-API-1.0.0rc8/aruna/api/storage/services/v1/user_service_pb2.py
--rw-r--r--   0 runner    (1001) docker     (123)     6707 2023-03-16 10:11:58.000000 Aruna-Python-API-1.0.0rc8/aruna/api/storage/services/v1/user_service_pb2.pyi
--rw-r--r--   0 runner    (1001) docker     (123)    23300 2023-03-16 10:11:58.000000 Aruna-Python-API-1.0.0rc8/aruna/api/storage/services/v1/user_service_pb2_grpc.py
--rw-r--r--   0 runner    (1001) docker     (123)      103 2023-03-16 10:12:11.559564 Aruna-Python-API-1.0.0rc8/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (123)     1409 2023-03-16 10:11:58.000000 Aruna-Python-API-1.0.0rc8/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-16 14:03:43.702358 Aruna-Python-API-1.0.0rc9/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-16 14:03:43.694357 Aruna-Python-API-1.0.0rc9/Aruna_Python_API.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)     2500 2023-03-16 14:03:43.000000 Aruna-Python-API-1.0.0rc9/Aruna_Python_API.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     2949 2023-03-16 14:03:43.000000 Aruna-Python-API-1.0.0rc9/Aruna_Python_API.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-03-16 14:03:43.000000 Aruna-Python-API-1.0.0rc9/Aruna_Python_API.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       83 2023-03-16 14:03:43.000000 Aruna-Python-API-1.0.0rc9/Aruna_Python_API.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        6 2023-03-16 14:03:43.000000 Aruna-Python-API-1.0.0rc9/Aruna_Python_API.egg-info/top_level.txt
+-rw-r--r--   0 runner    (1001) docker     (123)    11357 2023-03-16 14:03:17.000000 Aruna-Python-API-1.0.0rc9/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (123)     2500 2023-03-16 14:03:43.702358 Aruna-Python-API-1.0.0rc9/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     2095 2023-03-16 14:03:17.000000 Aruna-Python-API-1.0.0rc9/README.md
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-16 14:03:43.694357 Aruna-Python-API-1.0.0rc9/aruna/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-16 14:03:17.000000 Aruna-Python-API-1.0.0rc9/aruna/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-16 14:03:43.694357 Aruna-Python-API-1.0.0rc9/aruna/api/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-16 14:03:17.000000 Aruna-Python-API-1.0.0rc9/aruna/api/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-16 14:03:43.694357 Aruna-Python-API-1.0.0rc9/aruna/api/internal/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-16 14:03:17.000000 Aruna-Python-API-1.0.0rc9/aruna/api/internal/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-16 14:03:43.698357 Aruna-Python-API-1.0.0rc9/aruna/api/internal/v1/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-16 14:03:17.000000 Aruna-Python-API-1.0.0rc9/aruna/api/internal/v1/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3510 2023-03-16 14:03:30.000000 Aruna-Python-API-1.0.0rc9/aruna/api/internal/v1/authorize_pb2.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2584 2023-03-16 14:03:30.000000 Aruna-Python-API-1.0.0rc9/aruna/api/internal/v1/authorize_pb2.pyi
+-rw-r--r--   0 runner    (1001) docker     (123)     4675 2023-03-16 14:03:30.000000 Aruna-Python-API-1.0.0rc9/aruna/api/internal/v1/authorize_pb2_grpc.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7652 2023-03-16 14:03:30.000000 Aruna-Python-API-1.0.0rc9/aruna/api/internal/v1/notification_pb2.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7448 2023-03-16 14:03:30.000000 Aruna-Python-API-1.0.0rc9/aruna/api/internal/v1/notification_pb2.pyi
+-rw-r--r--   0 runner    (1001) docker     (123)    11854 2023-03-16 14:03:30.000000 Aruna-Python-API-1.0.0rc9/aruna/api/internal/v1/notification_pb2_grpc.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8761 2023-03-16 14:03:30.000000 Aruna-Python-API-1.0.0rc9/aruna/api/internal/v1/proxy_pb2.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7919 2023-03-16 14:03:30.000000 Aruna-Python-API-1.0.0rc9/aruna/api/internal/v1/proxy_pb2.pyi
+-rw-r--r--   0 runner    (1001) docker     (123)    18735 2023-03-16 14:03:30.000000 Aruna-Python-API-1.0.0rc9/aruna/api/internal/v1/proxy_pb2_grpc.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-16 14:03:43.698357 Aruna-Python-API-1.0.0rc9/aruna/api/notification/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-16 14:03:17.000000 Aruna-Python-API-1.0.0rc9/aruna/api/notification/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-16 14:03:43.698357 Aruna-Python-API-1.0.0rc9/aruna/api/notification/services/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-16 14:03:17.000000 Aruna-Python-API-1.0.0rc9/aruna/api/notification/services/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-16 14:03:43.698357 Aruna-Python-API-1.0.0rc9/aruna/api/notification/services/v1/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-16 14:03:17.000000 Aruna-Python-API-1.0.0rc9/aruna/api/notification/services/v1/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7956 2023-03-16 14:03:30.000000 Aruna-Python-API-1.0.0rc9/aruna/api/notification/services/v1/notification_service_pb2.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6624 2023-03-16 14:03:30.000000 Aruna-Python-API-1.0.0rc9/aruna/api/notification/services/v1/notification_service_pb2.pyi
+-rw-r--r--   0 runner    (1001) docker     (123)    12858 2023-03-16 14:03:30.000000 Aruna-Python-API-1.0.0rc9/aruna/api/notification/services/v1/notification_service_pb2_grpc.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-16 14:03:43.698357 Aruna-Python-API-1.0.0rc9/aruna/api/storage/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-16 14:03:17.000000 Aruna-Python-API-1.0.0rc9/aruna/api/storage/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-16 14:03:43.698357 Aruna-Python-API-1.0.0rc9/aruna/api/storage/models/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-16 14:03:17.000000 Aruna-Python-API-1.0.0rc9/aruna/api/storage/models/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-16 14:03:43.698357 Aruna-Python-API-1.0.0rc9/aruna/api/storage/models/v1/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-16 14:03:17.000000 Aruna-Python-API-1.0.0rc9/aruna/api/storage/models/v1/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4528 2023-03-16 14:03:30.000000 Aruna-Python-API-1.0.0rc9/aruna/api/storage/models/v1/auth_pb2.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5466 2023-03-16 14:03:30.000000 Aruna-Python-API-1.0.0rc9/aruna/api/storage/models/v1/auth_pb2.pyi
+-rw-r--r--   0 runner    (1001) docker     (123)      159 2023-03-16 14:03:30.000000 Aruna-Python-API-1.0.0rc9/aruna/api/storage/models/v1/auth_pb2_grpc.py
+-rw-r--r--   0 runner    (1001) docker     (123)    13949 2023-03-16 14:03:30.000000 Aruna-Python-API-1.0.0rc9/aruna/api/storage/models/v1/models_pb2.py
+-rw-r--r--   0 runner    (1001) docker     (123)    19733 2023-03-16 14:03:30.000000 Aruna-Python-API-1.0.0rc9/aruna/api/storage/models/v1/models_pb2.pyi
+-rw-r--r--   0 runner    (1001) docker     (123)      159 2023-03-16 14:03:30.000000 Aruna-Python-API-1.0.0rc9/aruna/api/storage/models/v1/models_pb2_grpc.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1966 2023-03-16 14:03:30.000000 Aruna-Python-API-1.0.0rc9/aruna/api/storage/models/v1/query_pb2.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1557 2023-03-16 14:03:30.000000 Aruna-Python-API-1.0.0rc9/aruna/api/storage/models/v1/query_pb2.pyi
+-rw-r--r--   0 runner    (1001) docker     (123)      159 2023-03-16 14:03:30.000000 Aruna-Python-API-1.0.0rc9/aruna/api/storage/models/v1/query_pb2_grpc.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-16 14:03:43.698357 Aruna-Python-API-1.0.0rc9/aruna/api/storage/services/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-16 14:03:17.000000 Aruna-Python-API-1.0.0rc9/aruna/api/storage/services/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-16 14:03:43.702358 Aruna-Python-API-1.0.0rc9/aruna/api/storage/services/v1/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-16 14:03:17.000000 Aruna-Python-API-1.0.0rc9/aruna/api/storage/services/v1/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8427 2023-03-16 14:03:30.000000 Aruna-Python-API-1.0.0rc9/aruna/api/storage/services/v1/collection_service_pb2.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6036 2023-03-16 14:03:30.000000 Aruna-Python-API-1.0.0rc9/aruna/api/storage/services/v1/collection_service_pb2.pyi
+-rw-r--r--   0 runner    (1001) docker     (123)    14738 2023-03-16 14:03:30.000000 Aruna-Python-API-1.0.0rc9/aruna/api/storage/services/v1/collection_service_pb2_grpc.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6081 2023-03-16 14:03:30.000000 Aruna-Python-API-1.0.0rc9/aruna/api/storage/services/v1/endpoint_service_pb2.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3482 2023-03-16 14:03:30.000000 Aruna-Python-API-1.0.0rc9/aruna/api/storage/services/v1/endpoint_service_pb2.pyi
+-rw-r--r--   0 runner    (1001) docker     (123)    11442 2023-03-16 14:03:30.000000 Aruna-Python-API-1.0.0rc9/aruna/api/storage/services/v1/endpoint_service_pb2_grpc.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6748 2023-03-16 14:03:30.000000 Aruna-Python-API-1.0.0rc9/aruna/api/storage/services/v1/info_service_pb2.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5186 2023-03-16 14:03:30.000000 Aruna-Python-API-1.0.0rc9/aruna/api/storage/services/v1/info_service_pb2.pyi
+-rw-r--r--   0 runner    (1001) docker     (123)     9125 2023-03-16 14:03:30.000000 Aruna-Python-API-1.0.0rc9/aruna/api/storage/services/v1/info_service_pb2_grpc.py
+-rw-r--r--   0 runner    (1001) docker     (123)    29817 2023-03-16 14:03:30.000000 Aruna-Python-API-1.0.0rc9/aruna/api/storage/services/v1/object_service_pb2.py
+-rw-r--r--   0 runner    (1001) docker     (123)    23315 2023-03-16 14:03:30.000000 Aruna-Python-API-1.0.0rc9/aruna/api/storage/services/v1/object_service_pb2.pyi
+-rw-r--r--   0 runner    (1001) docker     (123)    55158 2023-03-16 14:03:30.000000 Aruna-Python-API-1.0.0rc9/aruna/api/storage/services/v1/object_service_pb2_grpc.py
+-rw-r--r--   0 runner    (1001) docker     (123)    12477 2023-03-16 14:03:30.000000 Aruna-Python-API-1.0.0rc9/aruna/api/storage/services/v1/objectgroup_service_pb2.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9532 2023-03-16 14:03:30.000000 Aruna-Python-API-1.0.0rc9/aruna/api/storage/services/v1/objectgroup_service_pb2.pyi
+-rw-r--r--   0 runner    (1001) docker     (123)    21104 2023-03-16 14:03:30.000000 Aruna-Python-API-1.0.0rc9/aruna/api/storage/services/v1/objectgroup_service_pb2_grpc.py
+-rw-r--r--   0 runner    (1001) docker     (123)    10158 2023-03-16 14:03:30.000000 Aruna-Python-API-1.0.0rc9/aruna/api/storage/services/v1/project_service_pb2.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5091 2023-03-16 14:03:30.000000 Aruna-Python-API-1.0.0rc9/aruna/api/storage/services/v1/project_service_pb2.pyi
+-rw-r--r--   0 runner    (1001) docker     (123)    19904 2023-03-16 14:03:30.000000 Aruna-Python-API-1.0.0rc9/aruna/api/storage/services/v1/project_service_pb2_grpc.py
+-rw-r--r--   0 runner    (1001) docker     (123)    11655 2023-03-16 14:03:30.000000 Aruna-Python-API-1.0.0rc9/aruna/api/storage/services/v1/service_account_service_pb2.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6593 2023-03-16 14:03:30.000000 Aruna-Python-API-1.0.0rc9/aruna/api/storage/services/v1/service_account_service_pb2.pyi
+-rw-r--r--   0 runner    (1001) docker     (123)    22042 2023-03-16 14:03:30.000000 Aruna-Python-API-1.0.0rc9/aruna/api/storage/services/v1/service_account_service_pb2_grpc.py
+-rw-r--r--   0 runner    (1001) docker     (123)    11124 2023-03-16 14:03:30.000000 Aruna-Python-API-1.0.0rc9/aruna/api/storage/services/v1/user_service_pb2.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6707 2023-03-16 14:03:30.000000 Aruna-Python-API-1.0.0rc9/aruna/api/storage/services/v1/user_service_pb2.pyi
+-rw-r--r--   0 runner    (1001) docker     (123)    23300 2023-03-16 14:03:30.000000 Aruna-Python-API-1.0.0rc9/aruna/api/storage/services/v1/user_service_pb2_grpc.py
+-rw-r--r--   0 runner    (1001) docker     (123)      103 2023-03-16 14:03:43.702358 Aruna-Python-API-1.0.0rc9/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (123)     1409 2023-03-16 14:03:30.000000 Aruna-Python-API-1.0.0rc9/setup.py
```

### Comparing `Aruna-Python-API-1.0.0rc8/Aruna_Python_API.egg-info/PKG-INFO` & `Aruna-Python-API-1.0.0rc9/Aruna_Python_API.egg-info/PKG-INFO`

 * *Files 8% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: Aruna-Python-API
-Version: 1.0.0rc8
+Version: 1.0.0rc9
 Summary: Aruna Object Storage Python API builds
 Home-page: https://github.com/ArunaStorage/python-api
 Author: Marius Dieckmann, Jannis Hochmuth
 Author-email: marius.dieckmann@computational.bio.uni-giessen.de, jannis.hochmuth@computational.bio.uni-giessen.de
 License: Apache 2.0
 Description-Content-Type: text/markdown
 License-File: LICENSE
```

### Comparing `Aruna-Python-API-1.0.0rc8/Aruna_Python_API.egg-info/SOURCES.txt` & `Aruna-Python-API-1.0.0rc9/Aruna_Python_API.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `Aruna-Python-API-1.0.0rc8/LICENSE` & `Aruna-Python-API-1.0.0rc9/LICENSE`

 * *Files identical despite different names*

### Comparing `Aruna-Python-API-1.0.0rc8/PKG-INFO` & `Aruna-Python-API-1.0.0rc9/PKG-INFO`

 * *Files 8% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: Aruna-Python-API
-Version: 1.0.0rc8
+Version: 1.0.0rc9
 Summary: Aruna Object Storage Python API builds
 Home-page: https://github.com/ArunaStorage/python-api
 Author: Marius Dieckmann, Jannis Hochmuth
 Author-email: marius.dieckmann@computational.bio.uni-giessen.de, jannis.hochmuth@computational.bio.uni-giessen.de
 License: Apache 2.0
 Description-Content-Type: text/markdown
 License-File: LICENSE
```

### Comparing `Aruna-Python-API-1.0.0rc8/README.md` & `Aruna-Python-API-1.0.0rc9/README.md`

 * *Files identical despite different names*

### Comparing `Aruna-Python-API-1.0.0rc8/aruna/api/internal/v1/authorize_pb2.py` & `Aruna-Python-API-1.0.0rc9/aruna/api/internal/v1/authorize_pb2.py`

 * *Files identical despite different names*

### Comparing `Aruna-Python-API-1.0.0rc8/aruna/api/internal/v1/authorize_pb2.pyi` & `Aruna-Python-API-1.0.0rc9/aruna/api/internal/v1/authorize_pb2.pyi`

 * *Files identical despite different names*

### Comparing `Aruna-Python-API-1.0.0rc8/aruna/api/internal/v1/authorize_pb2_grpc.py` & `Aruna-Python-API-1.0.0rc9/aruna/api/internal/v1/authorize_pb2_grpc.py`

 * *Files identical despite different names*

### Comparing `Aruna-Python-API-1.0.0rc8/aruna/api/internal/v1/notification_pb2.py` & `Aruna-Python-API-1.0.0rc9/aruna/api/internal/v1/notification_pb2.py`

 * *Files identical despite different names*

### Comparing `Aruna-Python-API-1.0.0rc8/aruna/api/internal/v1/notification_pb2.pyi` & `Aruna-Python-API-1.0.0rc9/aruna/api/internal/v1/notification_pb2.pyi`

 * *Files identical despite different names*

### Comparing `Aruna-Python-API-1.0.0rc8/aruna/api/internal/v1/notification_pb2_grpc.py` & `Aruna-Python-API-1.0.0rc9/aruna/api/internal/v1/notification_pb2_grpc.py`

 * *Files identical despite different names*

### Comparing `Aruna-Python-API-1.0.0rc8/aruna/api/internal/v1/proxy_pb2.py` & `Aruna-Python-API-1.0.0rc9/aruna/api/internal/v1/proxy_pb2.py`

 * *Files 6% similar despite different names*

```diff
@@ -12,28 +12,28 @@
 
 
 from aruna.api.storage.models.v1 import models_pb2 as aruna_dot_api_dot_storage_dot_models_dot_v1_dot_models__pb2
 from aruna.api.storage.services.v1 import object_service_pb2 as aruna_dot_api_dot_storage_dot_services_dot_v1_dot_object__service__pb2
 from google.api import visibility_pb2 as google_dot_api_dot_visibility__pb2
 
 
-DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!aruna/api/internal/v1/proxy.proto\x12\x15\x61runa.api.internal.v1\x1a(aruna/api/storage/models/v1/models.proto\x1a\x32\x61runa/api/storage/services/v1/object_service.proto\x1a\x1bgoogle/api/visibility.proto\"\xff\x01\n\x08Location\x12\x37\n\x04type\x18\x01 \x01(\x0e\x32#.aruna.api.internal.v1.LocationTypeR\x04type\x12\x16\n\x06\x62ucket\x18\x02 \x01(\tR\x06\x62ucket\x12\x12\n\x04path\x18\x03 \x01(\tR\x04path\x12\x1f\n\x0b\x65ndpoint_id\x18\x04 \x01(\tR\nendpointId\x12#\n\ris_compressed\x18\x05 \x01(\x08R\x0cisCompressed\x12!\n\x0cis_encrypted\x18\x06 \x01(\x08R\x0bisEncrypted\x12%\n\x0e\x65ncryption_key\x18\x07 \x01(\tR\rencryptionKey\"?\n\x08PartETag\x12\x1f\n\x0bpart_number\x18\x01 \x01(\x03R\npartNumber\x12\x12\n\x04\x65tag\x18\x02 \x01(\tR\x04\x65tag\"0\n\x1aInitMultipartUploadRequest\x12\x12\n\x04path\x18\x01 \x01(\tR\x04path\":\n\x1bInitMultipartUploadResponse\x12\x1b\n\tupload_id\x18\x01 \x01(\tR\x08uploadId\"\x8f\x01\n\x1c\x46inishMultipartUploadRequest\x12\x1b\n\tupload_id\x18\x01 \x01(\tR\x08uploadId\x12\x12\n\x04path\x18\x02 \x01(\tR\x04path\x12>\n\npart_etags\x18\x03 \x03(\x0b\x32\x1f.aruna.api.internal.v1.PartETagR\tpartEtags\"\x1f\n\x1d\x46inishMultipartUploadResponse\"R\n\x13\x44\x65leteObjectRequest\x12;\n\x08location\x18\x01 \x01(\x0b\x32\x1f.aruna.api.internal.v1.LocationR\x08location\"\x16\n\x14\x44\x65leteObjectResponse\"\xd1\x01\n\x15\x46inalizeObjectRequest\x12\x1b\n\tobject_id\x18\x01 \x01(\tR\x08objectId\x12#\n\rcollection_id\x18\x02 \x01(\tR\x0c\x63ollectionId\x12;\n\x08location\x18\x03 \x01(\x0b\x32\x1f.aruna.api.internal.v1.LocationR\x08location\x12\x39\n\x06hashes\x18\x04 \x03(\x0b\x32!.aruna.api.storage.models.v1.HashR\x06hashes\"\x18\n\x16\x46inalizeObjectResponse\"j\n\x1fGetOrCreateEncryptionKeyRequest\x12\x12\n\x04path\x18\x01 \x01(\tR\x04path\x12\x12\n\x04hash\x18\x02 \x01(\tR\x04hash\x12\x1f\n\x0b\x65ndpoint_id\x18\x03 \x01(\tR\nendpointId\"c\n GetOrCreateEncryptionKeyResponse\x12%\n\x0e\x65ncryption_key\x18\x01 \x01(\tR\rencryptionKey\x12\x18\n\x07\x63reated\x18\x02 \x01(\x08R\x07\x63reated\"\x97\x01\n\x1eGetOrCreateObjectByPathRequest\x12\x12\n\x04path\x18\x01 \x01(\tR\x04path\x12\x1d\n\naccess_key\x18\x02 \x01(\tR\taccessKey\x12\x42\n\x06object\x18\x03 \x01(\x0b\x32*.aruna.api.storage.services.v1.StageObjectR\x06object\"\xe4\x01\n\x1fGetOrCreateObjectByPathResponse\x12\x1b\n\tobject_id\x18\x01 \x01(\tR\x08objectId\x12#\n\rcollection_id\x18\x02 \x01(\tR\x0c\x63ollectionId\x12\x44\n\tdataclass\x18\x03 \x01(\x0e\x32&.aruna.api.storage.models.v1.DataClassR\tdataclass\x12\x39\n\x06hashes\x18\x04 \x03(\x0b\x32!.aruna.api.storage.models.v1.HashR\x06hashes\"\x8f\x01\n\x18GetObjectLocationRequest\x12\x12\n\x04path\x18\x01 \x01(\tR\x04path\x12\x1f\n\x0brevision_id\x18\x02 \x01(\tR\nrevisionId\x12\x1d\n\naccess_key\x18\x03 \x01(\tR\taccessKey\x12\x1f\n\x0b\x65ndpoint_id\x18\x04 \x01(\tR\nendpointId\"\x95\x01\n\x19GetObjectLocationResponse\x12;\n\x06object\x18\x01 \x01(\x0b\x32#.aruna.api.storage.models.v1.ObjectR\x06object\x12;\n\x08location\x18\x02 \x01(\x0b\x32\x1f.aruna.api.internal.v1.LocationR\x08location\"U\n\x1cGetCollectionByBucketRequest\x12\x16\n\x06\x62ucket\x18\x01 \x01(\tR\x06\x62ucket\x12\x1d\n\naccess_key\x18\x02 \x01(\tR\taccessKey\"c\n\x1dGetCollectionByBucketResponse\x12\x1d\n\nproject_id\x18\x01 \x01(\tR\tprojectId\x12#\n\rcollection_id\x18\x02 \x01(\tR\x0c\x63ollectionId*[\n\x0cLocationType\x12\x1d\n\x19LOCATION_TYPE_UNSPECIFIED\x10\x00\x12\x14\n\x10LOCATION_TYPE_S3\x10\x01\x12\x16\n\x12LOCATION_TYPE_FILE\x10\x02\x32\x9a\x03\n\x14InternalProxyService\x12~\n\x13InitMultipartUpload\x12\x31.aruna.api.internal.v1.InitMultipartUploadRequest\x1a\x32.aruna.api.internal.v1.InitMultipartUploadResponse\"\x00\x12\x84\x01\n\x15\x46inishMultipartUpload\x12\x33.aruna.api.internal.v1.FinishMultipartUploadRequest\x1a\x34.aruna.api.internal.v1.FinishMultipartUploadResponse\"\x00\x12i\n\x0c\x44\x65leteObject\x12*.aruna.api.internal.v1.DeleteObjectRequest\x1a+.aruna.api.internal.v1.DeleteObjectResponse\"\x00\x1a\x10\xfa\xd2\xe4\x93\x02\n\x12\x08INTERNAL2\xbf\x05\n\x1cInternalProxyNotifierService\x12\x8a\x01\n\x17GetOrCreateObjectByPath\x12\x35.aruna.api.internal.v1.GetOrCreateObjectByPathRequest\x1a\x36.aruna.api.internal.v1.GetOrCreateObjectByPathResponse\"\x00\x12o\n\x0e\x46inalizeObject\x12,.aruna.api.internal.v1.FinalizeObjectRequest\x1a-.aruna.api.internal.v1.FinalizeObjectResponse\"\x00\x12\x8d\x01\n\x18GetOrCreateEncryptionKey\x12\x36.aruna.api.internal.v1.GetOrCreateEncryptionKeyRequest\x1a\x37.aruna.api.internal.v1.GetOrCreateEncryptionKeyResponse\"\x00\x12x\n\x11GetObjectLocation\x12/.aruna.api.internal.v1.GetObjectLocationRequest\x1a\x30.aruna.api.internal.v1.GetObjectLocationResponse\"\x00\x12\x84\x01\n\x15GetCollectionByBucket\x12\x33.aruna.api.internal.v1.GetCollectionByBucketRequest\x1a\x34.aruna.api.internal.v1.GetCollectionByBucketResponse\"\x00\x1a\x10\xfa\xd2\xe4\x93\x02\n\x12\x08INTERNALB6Z4github.com/ArunaStorage/go-api/aruna/api/internal/v1b\x06proto3')
+DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!aruna/api/internal/v1/proxy.proto\x12\x15\x61runa.api.internal.v1\x1a(aruna/api/storage/models/v1/models.proto\x1a\x32\x61runa/api/storage/services/v1/object_service.proto\x1a\x1bgoogle/api/visibility.proto\"\xff\x01\n\x08Location\x12\x37\n\x04type\x18\x01 \x01(\x0e\x32#.aruna.api.internal.v1.LocationTypeR\x04type\x12\x16\n\x06\x62ucket\x18\x02 \x01(\tR\x06\x62ucket\x12\x12\n\x04path\x18\x03 \x01(\tR\x04path\x12\x1f\n\x0b\x65ndpoint_id\x18\x04 \x01(\tR\nendpointId\x12#\n\ris_compressed\x18\x05 \x01(\x08R\x0cisCompressed\x12!\n\x0cis_encrypted\x18\x06 \x01(\x08R\x0bisEncrypted\x12%\n\x0e\x65ncryption_key\x18\x07 \x01(\tR\rencryptionKey\"?\n\x08PartETag\x12\x1f\n\x0bpart_number\x18\x01 \x01(\x03R\npartNumber\x12\x12\n\x04\x65tag\x18\x02 \x01(\tR\x04\x65tag\"0\n\x1aInitMultipartUploadRequest\x12\x12\n\x04path\x18\x01 \x01(\tR\x04path\":\n\x1bInitMultipartUploadResponse\x12\x1b\n\tupload_id\x18\x01 \x01(\tR\x08uploadId\"\x8f\x01\n\x1c\x46inishMultipartUploadRequest\x12\x1b\n\tupload_id\x18\x01 \x01(\tR\x08uploadId\x12\x12\n\x04path\x18\x02 \x01(\tR\x04path\x12>\n\npart_etags\x18\x03 \x03(\x0b\x32\x1f.aruna.api.internal.v1.PartETagR\tpartEtags\"\x1f\n\x1d\x46inishMultipartUploadResponse\"R\n\x13\x44\x65leteObjectRequest\x12;\n\x08location\x18\x01 \x01(\x0b\x32\x1f.aruna.api.internal.v1.LocationR\x08location\"\x16\n\x14\x44\x65leteObjectResponse\"\xf8\x01\n\x15\x46inalizeObjectRequest\x12\x1b\n\tobject_id\x18\x01 \x01(\tR\x08objectId\x12#\n\rcollection_id\x18\x02 \x01(\tR\x0c\x63ollectionId\x12;\n\x08location\x18\x03 \x01(\x0b\x32\x1f.aruna.api.internal.v1.LocationR\x08location\x12\x39\n\x06hashes\x18\x04 \x03(\x0b\x32!.aruna.api.storage.models.v1.HashR\x06hashes\x12%\n\x0e\x63ontent_length\x18\x05 \x01(\x03R\rcontentLength\"\x18\n\x16\x46inalizeObjectResponse\"j\n\x1fGetOrCreateEncryptionKeyRequest\x12\x12\n\x04path\x18\x01 \x01(\tR\x04path\x12\x12\n\x04hash\x18\x02 \x01(\tR\x04hash\x12\x1f\n\x0b\x65ndpoint_id\x18\x03 \x01(\tR\nendpointId\"c\n GetOrCreateEncryptionKeyResponse\x12%\n\x0e\x65ncryption_key\x18\x01 \x01(\tR\rencryptionKey\x12\x18\n\x07\x63reated\x18\x02 \x01(\x08R\x07\x63reated\"\x97\x01\n\x1eGetOrCreateObjectByPathRequest\x12\x12\n\x04path\x18\x01 \x01(\tR\x04path\x12\x1d\n\naccess_key\x18\x02 \x01(\tR\taccessKey\x12\x42\n\x06object\x18\x03 \x01(\x0b\x32*.aruna.api.storage.services.v1.StageObjectR\x06object\"\xa7\x02\n\x1fGetOrCreateObjectByPathResponse\x12\x1b\n\tobject_id\x18\x01 \x01(\tR\x08objectId\x12#\n\rcollection_id\x18\x02 \x01(\tR\x0c\x63ollectionId\x12\x44\n\tdataclass\x18\x03 \x01(\x0e\x32&.aruna.api.storage.models.v1.DataClassR\tdataclass\x12\x39\n\x06hashes\x18\x04 \x03(\x0b\x32!.aruna.api.storage.models.v1.HashR\x06hashes\x12\'\n\x0frevision_number\x18\x05 \x01(\x03R\x0erevisionNumber\x12\x18\n\x07\x63reated\x18\x06 \x01(\x08R\x07\x63reated\"\x8f\x01\n\x18GetObjectLocationRequest\x12\x12\n\x04path\x18\x01 \x01(\tR\x04path\x12\x1f\n\x0brevision_id\x18\x02 \x01(\tR\nrevisionId\x12\x1d\n\naccess_key\x18\x03 \x01(\tR\taccessKey\x12\x1f\n\x0b\x65ndpoint_id\x18\x04 \x01(\tR\nendpointId\"\x95\x01\n\x19GetObjectLocationResponse\x12;\n\x06object\x18\x01 \x01(\x0b\x32#.aruna.api.storage.models.v1.ObjectR\x06object\x12;\n\x08location\x18\x02 \x01(\x0b\x32\x1f.aruna.api.internal.v1.LocationR\x08location\"U\n\x1cGetCollectionByBucketRequest\x12\x16\n\x06\x62ucket\x18\x01 \x01(\tR\x06\x62ucket\x12\x1d\n\naccess_key\x18\x02 \x01(\tR\taccessKey\"c\n\x1dGetCollectionByBucketResponse\x12\x1d\n\nproject_id\x18\x01 \x01(\tR\tprojectId\x12#\n\rcollection_id\x18\x02 \x01(\tR\x0c\x63ollectionId*[\n\x0cLocationType\x12\x1d\n\x19LOCATION_TYPE_UNSPECIFIED\x10\x00\x12\x14\n\x10LOCATION_TYPE_S3\x10\x01\x12\x16\n\x12LOCATION_TYPE_FILE\x10\x02\x32\x9a\x03\n\x14InternalProxyService\x12~\n\x13InitMultipartUpload\x12\x31.aruna.api.internal.v1.InitMultipartUploadRequest\x1a\x32.aruna.api.internal.v1.InitMultipartUploadResponse\"\x00\x12\x84\x01\n\x15\x46inishMultipartUpload\x12\x33.aruna.api.internal.v1.FinishMultipartUploadRequest\x1a\x34.aruna.api.internal.v1.FinishMultipartUploadResponse\"\x00\x12i\n\x0c\x44\x65leteObject\x12*.aruna.api.internal.v1.DeleteObjectRequest\x1a+.aruna.api.internal.v1.DeleteObjectResponse\"\x00\x1a\x10\xfa\xd2\xe4\x93\x02\n\x12\x08INTERNAL2\xbf\x05\n\x1cInternalProxyNotifierService\x12\x8a\x01\n\x17GetOrCreateObjectByPath\x12\x35.aruna.api.internal.v1.GetOrCreateObjectByPathRequest\x1a\x36.aruna.api.internal.v1.GetOrCreateObjectByPathResponse\"\x00\x12o\n\x0e\x46inalizeObject\x12,.aruna.api.internal.v1.FinalizeObjectRequest\x1a-.aruna.api.internal.v1.FinalizeObjectResponse\"\x00\x12\x8d\x01\n\x18GetOrCreateEncryptionKey\x12\x36.aruna.api.internal.v1.GetOrCreateEncryptionKeyRequest\x1a\x37.aruna.api.internal.v1.GetOrCreateEncryptionKeyResponse\"\x00\x12x\n\x11GetObjectLocation\x12/.aruna.api.internal.v1.GetObjectLocationRequest\x1a\x30.aruna.api.internal.v1.GetObjectLocationResponse\"\x00\x12\x84\x01\n\x15GetCollectionByBucket\x12\x33.aruna.api.internal.v1.GetCollectionByBucketRequest\x1a\x34.aruna.api.internal.v1.GetCollectionByBucketResponse\"\x00\x1a\x10\xfa\xd2\xe4\x93\x02\n\x12\x08INTERNALB6Z4github.com/ArunaStorage/go-api/aruna/api/internal/v1b\x06proto3')
 
 _builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
 _builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'aruna.api.internal.v1.proxy_pb2', globals())
 if _descriptor._USE_C_DESCRIPTORS == False:
 
   DESCRIPTOR._options = None
   DESCRIPTOR._serialized_options = b'Z4github.com/ArunaStorage/go-api/aruna/api/internal/v1'
   _INTERNALPROXYSERVICE._options = None
   _INTERNALPROXYSERVICE._serialized_options = b'\372\322\344\223\002\n\022\010INTERNAL'
   _INTERNALPROXYNOTIFIERSERVICE._options = None
   _INTERNALPROXYNOTIFIERSERVICE._serialized_options = b'\372\322\344\223\002\n\022\010INTERNAL'
-  _LOCATIONTYPE._serialized_start=2221
-  _LOCATIONTYPE._serialized_end=2312
+  _LOCATIONTYPE._serialized_start=2327
+  _LOCATIONTYPE._serialized_end=2418
   _LOCATION._serialized_start=184
   _LOCATION._serialized_end=439
   _PARTETAG._serialized_start=441
   _PARTETAG._serialized_end=504
   _INITMULTIPARTUPLOADREQUEST._serialized_start=506
   _INITMULTIPARTUPLOADREQUEST._serialized_end=554
   _INITMULTIPARTUPLOADRESPONSE._serialized_start=556
@@ -43,31 +43,31 @@
   _FINISHMULTIPARTUPLOADRESPONSE._serialized_start=762
   _FINISHMULTIPARTUPLOADRESPONSE._serialized_end=793
   _DELETEOBJECTREQUEST._serialized_start=795
   _DELETEOBJECTREQUEST._serialized_end=877
   _DELETEOBJECTRESPONSE._serialized_start=879
   _DELETEOBJECTRESPONSE._serialized_end=901
   _FINALIZEOBJECTREQUEST._serialized_start=904
-  _FINALIZEOBJECTREQUEST._serialized_end=1113
-  _FINALIZEOBJECTRESPONSE._serialized_start=1115
-  _FINALIZEOBJECTRESPONSE._serialized_end=1139
-  _GETORCREATEENCRYPTIONKEYREQUEST._serialized_start=1141
-  _GETORCREATEENCRYPTIONKEYREQUEST._serialized_end=1247
-  _GETORCREATEENCRYPTIONKEYRESPONSE._serialized_start=1249
-  _GETORCREATEENCRYPTIONKEYRESPONSE._serialized_end=1348
-  _GETORCREATEOBJECTBYPATHREQUEST._serialized_start=1351
-  _GETORCREATEOBJECTBYPATHREQUEST._serialized_end=1502
-  _GETORCREATEOBJECTBYPATHRESPONSE._serialized_start=1505
-  _GETORCREATEOBJECTBYPATHRESPONSE._serialized_end=1733
-  _GETOBJECTLOCATIONREQUEST._serialized_start=1736
-  _GETOBJECTLOCATIONREQUEST._serialized_end=1879
-  _GETOBJECTLOCATIONRESPONSE._serialized_start=1882
-  _GETOBJECTLOCATIONRESPONSE._serialized_end=2031
-  _GETCOLLECTIONBYBUCKETREQUEST._serialized_start=2033
-  _GETCOLLECTIONBYBUCKETREQUEST._serialized_end=2118
-  _GETCOLLECTIONBYBUCKETRESPONSE._serialized_start=2120
-  _GETCOLLECTIONBYBUCKETRESPONSE._serialized_end=2219
-  _INTERNALPROXYSERVICE._serialized_start=2315
-  _INTERNALPROXYSERVICE._serialized_end=2725
-  _INTERNALPROXYNOTIFIERSERVICE._serialized_start=2728
-  _INTERNALPROXYNOTIFIERSERVICE._serialized_end=3431
+  _FINALIZEOBJECTREQUEST._serialized_end=1152
+  _FINALIZEOBJECTRESPONSE._serialized_start=1154
+  _FINALIZEOBJECTRESPONSE._serialized_end=1178
+  _GETORCREATEENCRYPTIONKEYREQUEST._serialized_start=1180
+  _GETORCREATEENCRYPTIONKEYREQUEST._serialized_end=1286
+  _GETORCREATEENCRYPTIONKEYRESPONSE._serialized_start=1288
+  _GETORCREATEENCRYPTIONKEYRESPONSE._serialized_end=1387
+  _GETORCREATEOBJECTBYPATHREQUEST._serialized_start=1390
+  _GETORCREATEOBJECTBYPATHREQUEST._serialized_end=1541
+  _GETORCREATEOBJECTBYPATHRESPONSE._serialized_start=1544
+  _GETORCREATEOBJECTBYPATHRESPONSE._serialized_end=1839
+  _GETOBJECTLOCATIONREQUEST._serialized_start=1842
+  _GETOBJECTLOCATIONREQUEST._serialized_end=1985
+  _GETOBJECTLOCATIONRESPONSE._serialized_start=1988
+  _GETOBJECTLOCATIONRESPONSE._serialized_end=2137
+  _GETCOLLECTIONBYBUCKETREQUEST._serialized_start=2139
+  _GETCOLLECTIONBYBUCKETREQUEST._serialized_end=2224
+  _GETCOLLECTIONBYBUCKETRESPONSE._serialized_start=2226
+  _GETCOLLECTIONBYBUCKETRESPONSE._serialized_end=2325
+  _INTERNALPROXYSERVICE._serialized_start=2421
+  _INTERNALPROXYSERVICE._serialized_end=2831
+  _INTERNALPROXYNOTIFIERSERVICE._serialized_start=2834
+  _INTERNALPROXYNOTIFIERSERVICE._serialized_end=3537
 # @@protoc_insertion_point(module_scope)
```

### Comparing `Aruna-Python-API-1.0.0rc8/aruna/api/internal/v1/proxy_pb2.pyi` & `Aruna-Python-API-1.0.0rc9/aruna/api/internal/v1/proxy_pb2.pyi`

 * *Files 2% similar despite different names*

```diff
@@ -19,24 +19,26 @@
     def __init__(self, location: _Optional[_Union[Location, _Mapping]] = ...) -> None: ...
 
 class DeleteObjectResponse(_message.Message):
     __slots__ = []
     def __init__(self) -> None: ...
 
 class FinalizeObjectRequest(_message.Message):
-    __slots__ = ["collection_id", "hashes", "location", "object_id"]
+    __slots__ = ["collection_id", "content_length", "hashes", "location", "object_id"]
     COLLECTION_ID_FIELD_NUMBER: _ClassVar[int]
+    CONTENT_LENGTH_FIELD_NUMBER: _ClassVar[int]
     HASHES_FIELD_NUMBER: _ClassVar[int]
     LOCATION_FIELD_NUMBER: _ClassVar[int]
     OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
     collection_id: str
+    content_length: int
     hashes: _containers.RepeatedCompositeFieldContainer[_models_pb2.Hash]
     location: Location
     object_id: str
-    def __init__(self, object_id: _Optional[str] = ..., collection_id: _Optional[str] = ..., location: _Optional[_Union[Location, _Mapping]] = ..., hashes: _Optional[_Iterable[_Union[_models_pb2.Hash, _Mapping]]] = ...) -> None: ...
+    def __init__(self, object_id: _Optional[str] = ..., collection_id: _Optional[str] = ..., location: _Optional[_Union[Location, _Mapping]] = ..., hashes: _Optional[_Iterable[_Union[_models_pb2.Hash, _Mapping]]] = ..., content_length: _Optional[int] = ...) -> None: ...
 
 class FinalizeObjectResponse(_message.Message):
     __slots__ = []
     def __init__(self) -> None: ...
 
 class FinishMultipartUploadRequest(_message.Message):
     __slots__ = ["part_etags", "path", "upload_id"]
@@ -113,24 +115,28 @@
     PATH_FIELD_NUMBER: _ClassVar[int]
     access_key: str
     object: _object_service_pb2.StageObject
     path: str
     def __init__(self, path: _Optional[str] = ..., access_key: _Optional[str] = ..., object: _Optional[_Union[_object_service_pb2.StageObject, _Mapping]] = ...) -> None: ...
 
 class GetOrCreateObjectByPathResponse(_message.Message):
-    __slots__ = ["collection_id", "dataclass", "hashes", "object_id"]
+    __slots__ = ["collection_id", "created", "dataclass", "hashes", "object_id", "revision_number"]
     COLLECTION_ID_FIELD_NUMBER: _ClassVar[int]
+    CREATED_FIELD_NUMBER: _ClassVar[int]
     DATACLASS_FIELD_NUMBER: _ClassVar[int]
     HASHES_FIELD_NUMBER: _ClassVar[int]
     OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
+    REVISION_NUMBER_FIELD_NUMBER: _ClassVar[int]
     collection_id: str
+    created: bool
     dataclass: _models_pb2.DataClass
     hashes: _containers.RepeatedCompositeFieldContainer[_models_pb2.Hash]
     object_id: str
-    def __init__(self, object_id: _Optional[str] = ..., collection_id: _Optional[str] = ..., dataclass: _Optional[_Union[_models_pb2.DataClass, str]] = ..., hashes: _Optional[_Iterable[_Union[_models_pb2.Hash, _Mapping]]] = ...) -> None: ...
+    revision_number: int
+    def __init__(self, object_id: _Optional[str] = ..., collection_id: _Optional[str] = ..., dataclass: _Optional[_Union[_models_pb2.DataClass, str]] = ..., hashes: _Optional[_Iterable[_Union[_models_pb2.Hash, _Mapping]]] = ..., revision_number: _Optional[int] = ..., created: bool = ...) -> None: ...
 
 class InitMultipartUploadRequest(_message.Message):
     __slots__ = ["path"]
     PATH_FIELD_NUMBER: _ClassVar[int]
     path: str
     def __init__(self, path: _Optional[str] = ...) -> None: ...
```

### Comparing `Aruna-Python-API-1.0.0rc8/aruna/api/internal/v1/proxy_pb2_grpc.py` & `Aruna-Python-API-1.0.0rc9/aruna/api/internal/v1/proxy_pb2_grpc.py`

 * *Files identical despite different names*

### Comparing `Aruna-Python-API-1.0.0rc8/aruna/api/notification/services/v1/notification_service_pb2.py` & `Aruna-Python-API-1.0.0rc9/aruna/api/notification/services/v1/notification_service_pb2.py`

 * *Files identical despite different names*

### Comparing `Aruna-Python-API-1.0.0rc8/aruna/api/notification/services/v1/notification_service_pb2.pyi` & `Aruna-Python-API-1.0.0rc9/aruna/api/notification/services/v1/notification_service_pb2.pyi`

 * *Files identical despite different names*

### Comparing `Aruna-Python-API-1.0.0rc8/aruna/api/notification/services/v1/notification_service_pb2_grpc.py` & `Aruna-Python-API-1.0.0rc9/aruna/api/notification/services/v1/notification_service_pb2_grpc.py`

 * *Files identical despite different names*

### Comparing `Aruna-Python-API-1.0.0rc8/aruna/api/storage/models/v1/auth_pb2.py` & `Aruna-Python-API-1.0.0rc9/aruna/api/storage/models/v1/auth_pb2.py`

 * *Files identical despite different names*

### Comparing `Aruna-Python-API-1.0.0rc8/aruna/api/storage/models/v1/auth_pb2.pyi` & `Aruna-Python-API-1.0.0rc9/aruna/api/storage/models/v1/auth_pb2.pyi`

 * *Files identical despite different names*

### Comparing `Aruna-Python-API-1.0.0rc8/aruna/api/storage/models/v1/models_pb2.py` & `Aruna-Python-API-1.0.0rc9/aruna/api/storage/models/v1/models_pb2.py`

 * *Files identical despite different names*

### Comparing `Aruna-Python-API-1.0.0rc8/aruna/api/storage/models/v1/models_pb2.pyi` & `Aruna-Python-API-1.0.0rc9/aruna/api/storage/models/v1/models_pb2.pyi`

 * *Files identical despite different names*

### Comparing `Aruna-Python-API-1.0.0rc8/aruna/api/storage/models/v1/query_pb2.py` & `Aruna-Python-API-1.0.0rc9/aruna/api/storage/models/v1/query_pb2.py`

 * *Files identical despite different names*

### Comparing `Aruna-Python-API-1.0.0rc8/aruna/api/storage/models/v1/query_pb2.pyi` & `Aruna-Python-API-1.0.0rc9/aruna/api/storage/models/v1/query_pb2.pyi`

 * *Files identical despite different names*

### Comparing `Aruna-Python-API-1.0.0rc8/aruna/api/storage/services/v1/collection_service_pb2.py` & `Aruna-Python-API-1.0.0rc9/aruna/api/storage/services/v1/collection_service_pb2.py`

 * *Files identical despite different names*

### Comparing `Aruna-Python-API-1.0.0rc8/aruna/api/storage/services/v1/collection_service_pb2.pyi` & `Aruna-Python-API-1.0.0rc9/aruna/api/storage/services/v1/collection_service_pb2.pyi`

 * *Files identical despite different names*

### Comparing `Aruna-Python-API-1.0.0rc8/aruna/api/storage/services/v1/collection_service_pb2_grpc.py` & `Aruna-Python-API-1.0.0rc9/aruna/api/storage/services/v1/collection_service_pb2_grpc.py`

 * *Files identical despite different names*

### Comparing `Aruna-Python-API-1.0.0rc8/aruna/api/storage/services/v1/endpoint_service_pb2.py` & `Aruna-Python-API-1.0.0rc9/aruna/api/storage/services/v1/endpoint_service_pb2.py`

 * *Files identical despite different names*

### Comparing `Aruna-Python-API-1.0.0rc8/aruna/api/storage/services/v1/endpoint_service_pb2.pyi` & `Aruna-Python-API-1.0.0rc9/aruna/api/storage/services/v1/endpoint_service_pb2.pyi`

 * *Files identical despite different names*

### Comparing `Aruna-Python-API-1.0.0rc8/aruna/api/storage/services/v1/endpoint_service_pb2_grpc.py` & `Aruna-Python-API-1.0.0rc9/aruna/api/storage/services/v1/endpoint_service_pb2_grpc.py`

 * *Files identical despite different names*

### Comparing `Aruna-Python-API-1.0.0rc8/aruna/api/storage/services/v1/info_service_pb2.py` & `Aruna-Python-API-1.0.0rc9/aruna/api/storage/services/v1/info_service_pb2.py`

 * *Files identical despite different names*

### Comparing `Aruna-Python-API-1.0.0rc8/aruna/api/storage/services/v1/info_service_pb2.pyi` & `Aruna-Python-API-1.0.0rc9/aruna/api/storage/services/v1/info_service_pb2.pyi`

 * *Files identical despite different names*

### Comparing `Aruna-Python-API-1.0.0rc8/aruna/api/storage/services/v1/info_service_pb2_grpc.py` & `Aruna-Python-API-1.0.0rc9/aruna/api/storage/services/v1/info_service_pb2_grpc.py`

 * *Files identical despite different names*

### Comparing `Aruna-Python-API-1.0.0rc8/aruna/api/storage/services/v1/object_service_pb2.py` & `Aruna-Python-API-1.0.0rc9/aruna/api/storage/services/v1/object_service_pb2.py`

 * *Files identical despite different names*

### Comparing `Aruna-Python-API-1.0.0rc8/aruna/api/storage/services/v1/object_service_pb2.pyi` & `Aruna-Python-API-1.0.0rc9/aruna/api/storage/services/v1/object_service_pb2.pyi`

 * *Files identical despite different names*

### Comparing `Aruna-Python-API-1.0.0rc8/aruna/api/storage/services/v1/object_service_pb2_grpc.py` & `Aruna-Python-API-1.0.0rc9/aruna/api/storage/services/v1/object_service_pb2_grpc.py`

 * *Files identical despite different names*

### Comparing `Aruna-Python-API-1.0.0rc8/aruna/api/storage/services/v1/objectgroup_service_pb2.py` & `Aruna-Python-API-1.0.0rc9/aruna/api/storage/services/v1/objectgroup_service_pb2.py`

 * *Files identical despite different names*

### Comparing `Aruna-Python-API-1.0.0rc8/aruna/api/storage/services/v1/objectgroup_service_pb2.pyi` & `Aruna-Python-API-1.0.0rc9/aruna/api/storage/services/v1/objectgroup_service_pb2.pyi`

 * *Files identical despite different names*

### Comparing `Aruna-Python-API-1.0.0rc8/aruna/api/storage/services/v1/objectgroup_service_pb2_grpc.py` & `Aruna-Python-API-1.0.0rc9/aruna/api/storage/services/v1/objectgroup_service_pb2_grpc.py`

 * *Files identical despite different names*

### Comparing `Aruna-Python-API-1.0.0rc8/aruna/api/storage/services/v1/project_service_pb2.py` & `Aruna-Python-API-1.0.0rc9/aruna/api/storage/services/v1/project_service_pb2.py`

 * *Files 0% similar despite different names*

```diff
@@ -12,22 +12,22 @@
 
 
 from aruna.api.storage.models.v1 import auth_pb2 as aruna_dot_api_dot_storage_dot_models_dot_v1_dot_auth__pb2
 from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
 from protoc_gen_openapiv2.options import annotations_pb2 as protoc__gen__openapiv2_dot_options_dot_annotations__pb2
 
 
-DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n3aruna/api/storage/services/v1/project_service.proto\x12\x1d\x61runa.api.storage.services.v1\x1a&aruna/api/storage/models/v1/auth.proto\x1a\x1cgoogle/api/annotations.proto\x1a.protoc-gen-openapiv2/options/annotations.proto\"L\n\x14\x43reateProjectRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12 \n\x0b\x64\x65scription\x18\x02 \x01(\tR\x0b\x64\x65scription\"6\n\x15\x43reateProjectResponse\x12\x1d\n\nproject_id\x18\x01 \x01(\tR\tprojectId\"\x91\x01\n\x17\x41\x64\x64UserToProjectRequest\x12\x1d\n\nproject_id\x18\x01 \x01(\tR\tprojectId\x12W\n\x0fuser_permission\x18\x03 \x01(\x0b\x32..aruna.api.storage.models.v1.ProjectPermissionR\x0euserPermission\"\x1a\n\x18\x41\x64\x64UserToProjectResponse\"2\n\x11GetProjectRequest\x12\x1d\n\nproject_id\x18\x01 \x01(\tR\tprojectId\"\\\n\x12GetProjectResponse\x12\x46\n\x07project\x18\x01 \x01(\x0b\x32,.aruna.api.storage.models.v1.ProjectOverviewR\x07project\"\x14\n\x12GetProjectsRequest\"_\n\x13GetProjectsResponse\x12H\n\x08projects\x18\x01 \x03(\x0b\x32,.aruna.api.storage.models.v1.ProjectOverviewR\x08projects\"6\n\x15\x44\x65stroyProjectRequest\x12\x1d\n\nproject_id\x18\x01 \x01(\tR\tprojectId\"\x18\n\x16\x44\x65stroyProjectResponse\"k\n\x14UpdateProjectRequest\x12\x1d\n\nproject_id\x18\x01 \x01(\tR\tprojectId\x12\x12\n\x04name\x18\x02 \x01(\tR\x04name\x12 \n\x0b\x64\x65scription\x18\x03 \x01(\tR\x0b\x64\x65scription\"_\n\x15UpdateProjectResponse\x12\x46\n\x07project\x18\x01 \x01(\x0b\x32,.aruna.api.storage.models.v1.ProjectOverviewR\x07project\"V\n\x1cRemoveUserFromProjectRequest\x12\x1d\n\nproject_id\x18\x01 \x01(\tR\tprojectId\x12\x17\n\x07user_id\x18\x02 \x01(\tR\x06userId\"\x1f\n\x1dRemoveUserFromProjectResponse\"]\n#GetUserPermissionsForProjectRequest\x12\x1d\n\nproject_id\x18\x01 \x01(\tR\tprojectId\x12\x17\n\x07user_id\x18\x02 \x01(\tR\x06userId\"\x8a\x01\n$GetUserPermissionsForProjectResponse\x12\x62\n\x0fuser_permission\x18\x01 \x01(\x0b\x32\x39.aruna.api.storage.models.v1.ProjectPermissionDisplayNameR\x0euserPermission\"\x9e\x01\n$EditUserPermissionsForProjectRequest\x12\x1d\n\nproject_id\x18\x01 \x01(\tR\tprojectId\x12W\n\x0fuser_permission\x18\x02 \x01(\x0b\x32..aruna.api.storage.models.v1.ProjectPermissionR\x0euserPermission\"\'\n%EditUserPermissionsForProjectResponse2\xb1\x0c\n\x0eProjectService\x12\x92\x01\n\rCreateProject\x12\x33.aruna.api.storage.services.v1.CreateProjectRequest\x1a\x34.aruna.api.storage.services.v1.CreateProjectResponse\"\x16\x82\xd3\xe4\x93\x02\x10:\x01*\"\x0b/v1/project\x12\xb1\x01\n\x10\x41\x64\x64UserToProject\x12\x36.aruna.api.storage.services.v1.AddUserToProjectRequest\x1a\x37.aruna.api.storage.services.v1.AddUserToProjectResponse\",\x82\xd3\xe4\x93\x02&:\x01*\"!/v1/project/{project_id}/add_user\x12\x93\x01\n\nGetProject\x12\x30.aruna.api.storage.services.v1.GetProjectRequest\x1a\x31.aruna.api.storage.services.v1.GetProjectResponse\" \x82\xd3\xe4\x93\x02\x1a\x12\x18/v1/project/{project_id}\x12\x8a\x01\n\x0bGetProjects\x12\x31.aruna.api.storage.services.v1.GetProjectsRequest\x1a\x32.aruna.api.storage.services.v1.GetProjectsResponse\"\x14\x82\xd3\xe4\x93\x02\x0e\x12\x0c/v1/projects\x12\x9f\x01\n\x0e\x44\x65stroyProject\x12\x34.aruna.api.storage.services.v1.DestroyProjectRequest\x1a\x35.aruna.api.storage.services.v1.DestroyProjectResponse\" \x82\xd3\xe4\x93\x02\x1a*\x18/v1/project/{project_id}\x12\x9c\x01\n\rUpdateProject\x12\x33.aruna.api.storage.services.v1.UpdateProjectRequest\x1a\x34.aruna.api.storage.services.v1.UpdateProjectResponse\" \x82\xd3\xe4\x93\x02\x1a\x1a\x18/v1/project/{project_id}\x12\xc0\x01\n\x15RemoveUserFromProject\x12;.aruna.api.storage.services.v1.RemoveUserFromProjectRequest\x1a<.aruna.api.storage.services.v1.RemoveUserFromProjectResponse\",\x82\xd3\xe4\x93\x02&*$/v1/project/{project_id}/remove_user\x12\xd2\x01\n\x1cGetUserPermissionsForProject\x12\x42.aruna.api.storage.services.v1.GetUserPermissionsForProjectRequest\x1a\x43.aruna.api.storage.services.v1.GetUserPermissionsForProjectResponse\")\x82\xd3\xe4\x93\x02#\x12!/v1/project/{project_id}/get_user\x12\xd9\x01\n\x1d\x45\x64itUserPermissionsForProject\x12\x43.aruna.api.storage.services.v1.EditUserPermissionsForProjectRequest\x1a\x44.aruna.api.storage.services.v1.EditUserPermissionsForProjectResponse\"-\x82\xd3\xe4\x93\x02\':\x01*2\"/v1/project/{project_id}/edit_userB\xe5\x02\n>com.github.ArunaStorage.java_api.aruna.api.storage.services.v1B\x0eProjectServiceP\x01Z<github.com/ArunaStorage/go-api/aruna/api/storage/services/v1\x92\x41\xd1\x01\x12\x31\n#Aruna Object Storage (AOS) REST API2\n1.0.0-rc.8*\x01\x02\x32\x10\x61pplication/json:\x10\x61pplication/jsonZ`\n^\n\rAccessKeyAuth\x12M\x08\x02\x12\x38\x41uthentication token, prefixed by Bearer: Bearer <token>\x1a\rAuthorization \x02\x62\x13\n\x11\n\rAccessKeyAuth\x12\x00\x62\x06proto3')
+DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n3aruna/api/storage/services/v1/project_service.proto\x12\x1d\x61runa.api.storage.services.v1\x1a&aruna/api/storage/models/v1/auth.proto\x1a\x1cgoogle/api/annotations.proto\x1a.protoc-gen-openapiv2/options/annotations.proto\"L\n\x14\x43reateProjectRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12 \n\x0b\x64\x65scription\x18\x02 \x01(\tR\x0b\x64\x65scription\"6\n\x15\x43reateProjectResponse\x12\x1d\n\nproject_id\x18\x01 \x01(\tR\tprojectId\"\x91\x01\n\x17\x41\x64\x64UserToProjectRequest\x12\x1d\n\nproject_id\x18\x01 \x01(\tR\tprojectId\x12W\n\x0fuser_permission\x18\x03 \x01(\x0b\x32..aruna.api.storage.models.v1.ProjectPermissionR\x0euserPermission\"\x1a\n\x18\x41\x64\x64UserToProjectResponse\"2\n\x11GetProjectRequest\x12\x1d\n\nproject_id\x18\x01 \x01(\tR\tprojectId\"\\\n\x12GetProjectResponse\x12\x46\n\x07project\x18\x01 \x01(\x0b\x32,.aruna.api.storage.models.v1.ProjectOverviewR\x07project\"\x14\n\x12GetProjectsRequest\"_\n\x13GetProjectsResponse\x12H\n\x08projects\x18\x01 \x03(\x0b\x32,.aruna.api.storage.models.v1.ProjectOverviewR\x08projects\"6\n\x15\x44\x65stroyProjectRequest\x12\x1d\n\nproject_id\x18\x01 \x01(\tR\tprojectId\"\x18\n\x16\x44\x65stroyProjectResponse\"k\n\x14UpdateProjectRequest\x12\x1d\n\nproject_id\x18\x01 \x01(\tR\tprojectId\x12\x12\n\x04name\x18\x02 \x01(\tR\x04name\x12 \n\x0b\x64\x65scription\x18\x03 \x01(\tR\x0b\x64\x65scription\"_\n\x15UpdateProjectResponse\x12\x46\n\x07project\x18\x01 \x01(\x0b\x32,.aruna.api.storage.models.v1.ProjectOverviewR\x07project\"V\n\x1cRemoveUserFromProjectRequest\x12\x1d\n\nproject_id\x18\x01 \x01(\tR\tprojectId\x12\x17\n\x07user_id\x18\x02 \x01(\tR\x06userId\"\x1f\n\x1dRemoveUserFromProjectResponse\"]\n#GetUserPermissionsForProjectRequest\x12\x1d\n\nproject_id\x18\x01 \x01(\tR\tprojectId\x12\x17\n\x07user_id\x18\x02 \x01(\tR\x06userId\"\x8a\x01\n$GetUserPermissionsForProjectResponse\x12\x62\n\x0fuser_permission\x18\x01 \x01(\x0b\x32\x39.aruna.api.storage.models.v1.ProjectPermissionDisplayNameR\x0euserPermission\"\x9e\x01\n$EditUserPermissionsForProjectRequest\x12\x1d\n\nproject_id\x18\x01 \x01(\tR\tprojectId\x12W\n\x0fuser_permission\x18\x02 \x01(\x0b\x32..aruna.api.storage.models.v1.ProjectPermissionR\x0euserPermission\"\'\n%EditUserPermissionsForProjectResponse2\xb1\x0c\n\x0eProjectService\x12\x92\x01\n\rCreateProject\x12\x33.aruna.api.storage.services.v1.CreateProjectRequest\x1a\x34.aruna.api.storage.services.v1.CreateProjectResponse\"\x16\x82\xd3\xe4\x93\x02\x10:\x01*\"\x0b/v1/project\x12\xb1\x01\n\x10\x41\x64\x64UserToProject\x12\x36.aruna.api.storage.services.v1.AddUserToProjectRequest\x1a\x37.aruna.api.storage.services.v1.AddUserToProjectResponse\",\x82\xd3\xe4\x93\x02&:\x01*\"!/v1/project/{project_id}/add_user\x12\x93\x01\n\nGetProject\x12\x30.aruna.api.storage.services.v1.GetProjectRequest\x1a\x31.aruna.api.storage.services.v1.GetProjectResponse\" \x82\xd3\xe4\x93\x02\x1a\x12\x18/v1/project/{project_id}\x12\x8a\x01\n\x0bGetProjects\x12\x31.aruna.api.storage.services.v1.GetProjectsRequest\x1a\x32.aruna.api.storage.services.v1.GetProjectsResponse\"\x14\x82\xd3\xe4\x93\x02\x0e\x12\x0c/v1/projects\x12\x9f\x01\n\x0e\x44\x65stroyProject\x12\x34.aruna.api.storage.services.v1.DestroyProjectRequest\x1a\x35.aruna.api.storage.services.v1.DestroyProjectResponse\" \x82\xd3\xe4\x93\x02\x1a*\x18/v1/project/{project_id}\x12\x9c\x01\n\rUpdateProject\x12\x33.aruna.api.storage.services.v1.UpdateProjectRequest\x1a\x34.aruna.api.storage.services.v1.UpdateProjectResponse\" \x82\xd3\xe4\x93\x02\x1a\x1a\x18/v1/project/{project_id}\x12\xc0\x01\n\x15RemoveUserFromProject\x12;.aruna.api.storage.services.v1.RemoveUserFromProjectRequest\x1a<.aruna.api.storage.services.v1.RemoveUserFromProjectResponse\",\x82\xd3\xe4\x93\x02&*$/v1/project/{project_id}/remove_user\x12\xd2\x01\n\x1cGetUserPermissionsForProject\x12\x42.aruna.api.storage.services.v1.GetUserPermissionsForProjectRequest\x1a\x43.aruna.api.storage.services.v1.GetUserPermissionsForProjectResponse\")\x82\xd3\xe4\x93\x02#\x12!/v1/project/{project_id}/get_user\x12\xd9\x01\n\x1d\x45\x64itUserPermissionsForProject\x12\x43.aruna.api.storage.services.v1.EditUserPermissionsForProjectRequest\x1a\x44.aruna.api.storage.services.v1.EditUserPermissionsForProjectResponse\"-\x82\xd3\xe4\x93\x02\':\x01*2\"/v1/project/{project_id}/edit_userB\xe5\x02\n>com.github.ArunaStorage.java_api.aruna.api.storage.services.v1B\x0eProjectServiceP\x01Z<github.com/ArunaStorage/go-api/aruna/api/storage/services/v1\x92\x41\xd1\x01\x12\x31\n#Aruna Object Storage (AOS) REST API2\n1.0.0-rc.9*\x01\x02\x32\x10\x61pplication/json:\x10\x61pplication/jsonZ`\n^\n\rAccessKeyAuth\x12M\x08\x02\x12\x38\x41uthentication token, prefixed by Bearer: Bearer <token>\x1a\rAuthorization \x02\x62\x13\n\x11\n\rAccessKeyAuth\x12\x00\x62\x06proto3')
 
 _builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
 _builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'aruna.api.storage.services.v1.project_service_pb2', globals())
 if _descriptor._USE_C_DESCRIPTORS == False:
 
   DESCRIPTOR._options = None
-  DESCRIPTOR._serialized_options = b'\n>com.github.ArunaStorage.java_api.aruna.api.storage.services.v1B\016ProjectServiceP\001Z<github.com/ArunaStorage/go-api/aruna/api/storage/services/v1\222A\321\001\0221\n#Aruna Object Storage (AOS) REST API2\n1.0.0-rc.8*\001\0022\020application/json:\020application/jsonZ`\n^\n\rAccessKeyAuth\022M\010\002\0228Authentication token, prefixed by Bearer: Bearer <token>\032\rAuthorization \002b\023\n\021\n\rAccessKeyAuth\022\000'
+  DESCRIPTOR._serialized_options = b'\n>com.github.ArunaStorage.java_api.aruna.api.storage.services.v1B\016ProjectServiceP\001Z<github.com/ArunaStorage/go-api/aruna/api/storage/services/v1\222A\321\001\0221\n#Aruna Object Storage (AOS) REST API2\n1.0.0-rc.9*\001\0022\020application/json:\020application/jsonZ`\n^\n\rAccessKeyAuth\022M\010\002\0228Authentication token, prefixed by Bearer: Bearer <token>\032\rAuthorization \002b\023\n\021\n\rAccessKeyAuth\022\000'
   _PROJECTSERVICE.methods_by_name['CreateProject']._options = None
   _PROJECTSERVICE.methods_by_name['CreateProject']._serialized_options = b'\202\323\344\223\002\020:\001*\"\013/v1/project'
   _PROJECTSERVICE.methods_by_name['AddUserToProject']._options = None
   _PROJECTSERVICE.methods_by_name['AddUserToProject']._serialized_options = b'\202\323\344\223\002&:\001*\"!/v1/project/{project_id}/add_user'
   _PROJECTSERVICE.methods_by_name['GetProject']._options = None
   _PROJECTSERVICE.methods_by_name['GetProject']._serialized_options = b'\202\323\344\223\002\032\022\030/v1/project/{project_id}'
   _PROJECTSERVICE.methods_by_name['GetProjects']._options = None
```

### Comparing `Aruna-Python-API-1.0.0rc8/aruna/api/storage/services/v1/project_service_pb2.pyi` & `Aruna-Python-API-1.0.0rc9/aruna/api/storage/services/v1/project_service_pb2.pyi`

 * *Files identical despite different names*

### Comparing `Aruna-Python-API-1.0.0rc8/aruna/api/storage/services/v1/project_service_pb2_grpc.py` & `Aruna-Python-API-1.0.0rc9/aruna/api/storage/services/v1/project_service_pb2_grpc.py`

 * *Files identical despite different names*

### Comparing `Aruna-Python-API-1.0.0rc8/aruna/api/storage/services/v1/service_account_service_pb2.py` & `Aruna-Python-API-1.0.0rc9/aruna/api/storage/services/v1/service_account_service_pb2.py`

 * *Files identical despite different names*

### Comparing `Aruna-Python-API-1.0.0rc8/aruna/api/storage/services/v1/service_account_service_pb2.pyi` & `Aruna-Python-API-1.0.0rc9/aruna/api/storage/services/v1/service_account_service_pb2.pyi`

 * *Files identical despite different names*

### Comparing `Aruna-Python-API-1.0.0rc8/aruna/api/storage/services/v1/service_account_service_pb2_grpc.py` & `Aruna-Python-API-1.0.0rc9/aruna/api/storage/services/v1/service_account_service_pb2_grpc.py`

 * *Files identical despite different names*

### Comparing `Aruna-Python-API-1.0.0rc8/aruna/api/storage/services/v1/user_service_pb2.py` & `Aruna-Python-API-1.0.0rc9/aruna/api/storage/services/v1/user_service_pb2.py`

 * *Files identical despite different names*

### Comparing `Aruna-Python-API-1.0.0rc8/aruna/api/storage/services/v1/user_service_pb2.pyi` & `Aruna-Python-API-1.0.0rc9/aruna/api/storage/services/v1/user_service_pb2.pyi`

 * *Files identical despite different names*

### Comparing `Aruna-Python-API-1.0.0rc8/aruna/api/storage/services/v1/user_service_pb2_grpc.py` & `Aruna-Python-API-1.0.0rc9/aruna/api/storage/services/v1/user_service_pb2_grpc.py`

 * *Files identical despite different names*

### Comparing `Aruna-Python-API-1.0.0rc8/setup.py` & `Aruna-Python-API-1.0.0rc9/setup.py`

 * *Files 4% similar despite different names*

```diff
@@ -1,14 +1,14 @@
 #!/usr/bin/env python
 
 from setuptools import setup, find_packages
 
 setup(
     name='Aruna-Python-API',
-    version="1.0.0-rc.8",
+    version="1.0.0-rc.9",
     description='Aruna Object Storage Python API builds',
     long_description=open('README.md', 'r').read(),
     long_description_content_type='text/markdown',
     url='https://github.com/ArunaStorage/python-api',
     license='Apache 2.0',
     author='Marius Dieckmann, Jannis Hochmuth',
     author_email='marius.dieckmann@computational.bio.uni-giessen.de, '
```

