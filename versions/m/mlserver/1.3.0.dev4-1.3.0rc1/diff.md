# Comparing `tmp/mlserver-1.3.0.dev4.tar.gz` & `tmp/mlserver-1.3.0rc1.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "mlserver-1.3.0.dev4.tar", last modified: Wed Mar 22 09:50:33 2023, max compression
+gzip compressed data, was "mlserver-1.3.0rc1.tar", last modified: Thu Apr  6 13:37:59 2023, max compression
```

## Comparing `mlserver-1.3.0.dev4.tar` & `mlserver-1.3.0rc1.tar`

### file list

```diff
@@ -1,116 +1,122 @@
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-22 09:50:33.190762 mlserver-1.3.0.dev4/
--rw-r--r--   0 runner    (1001) docker     (123)    11354 2023-03-22 09:49:54.000000 mlserver-1.3.0.dev4/LICENSE
--rw-r--r--   0 runner    (1001) docker     (123)     6561 2023-03-22 09:50:33.190762 mlserver-1.3.0.dev4/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)     5366 2023-03-22 09:49:54.000000 mlserver-1.3.0.dev4/README.md
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-22 09:50:33.182762 mlserver-1.3.0.dev4/mlserver/
--rw-r--r--   0 runner    (1001) docker     (123)      299 2023-03-22 09:49:54.000000 mlserver-1.3.0.dev4/mlserver/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    16113 2023-03-22 09:49:54.000000 mlserver-1.3.0.dev4/mlserver/batch_processing.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-22 09:50:33.182762 mlserver-1.3.0.dev4/mlserver/batching/
--rw-r--r--   0 runner    (1001) docker     (123)      176 2023-03-22 09:49:54.000000 mlserver-1.3.0.dev4/mlserver/batching/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     5529 2023-03-22 09:49:54.000000 mlserver-1.3.0.dev4/mlserver/batching/adaptive.py
--rw-r--r--   0 runner    (1001) docker     (123)     1856 2023-03-22 09:49:54.000000 mlserver-1.3.0.dev4/mlserver/batching/hooks.py
--rw-r--r--   0 runner    (1001) docker     (123)    10847 2023-03-22 09:49:54.000000 mlserver-1.3.0.dev4/mlserver/batching/requests.py
--rw-r--r--   0 runner    (1001) docker     (123)      911 2023-03-22 09:49:54.000000 mlserver-1.3.0.dev4/mlserver/batching/shape.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-22 09:50:33.186761 mlserver-1.3.0.dev4/mlserver/cli/
--rw-r--r--   0 runner    (1001) docker     (123)       43 2023-03-22 09:49:54.000000 mlserver-1.3.0.dev4/mlserver/cli/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     1883 2023-03-22 09:49:54.000000 mlserver-1.3.0.dev4/mlserver/cli/build.py
--rw-r--r--   0 runner    (1001) docker     (123)     2371 2023-03-22 09:49:54.000000 mlserver-1.3.0.dev4/mlserver/cli/constants.py
--rw-r--r--   0 runner    (1001) docker     (123)      427 2023-03-22 09:49:54.000000 mlserver-1.3.0.dev4/mlserver/cli/init_project.py
--rw-r--r--   0 runner    (1001) docker     (123)     6813 2023-03-22 09:49:54.000000 mlserver-1.3.0.dev4/mlserver/cli/main.py
--rw-r--r--   0 runner    (1001) docker     (123)     1318 2023-03-22 09:49:54.000000 mlserver-1.3.0.dev4/mlserver/cli/serve.py
--rw-r--r--   0 runner    (1001) docker     (123)     3323 2023-03-22 09:49:54.000000 mlserver-1.3.0.dev4/mlserver/cloudevents.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-22 09:50:33.186761 mlserver-1.3.0.dev4/mlserver/codecs/
--rw-r--r--   0 runner    (1001) docker     (123)     1177 2023-03-22 09:49:54.000000 mlserver-1.3.0.dev4/mlserver/codecs/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     9601 2023-03-22 09:49:54.000000 mlserver-1.3.0.dev4/mlserver/codecs/base.py
--rw-r--r--   0 runner    (1001) docker     (123)     2575 2023-03-22 09:49:54.000000 mlserver-1.3.0.dev4/mlserver/codecs/base64.py
--rw-r--r--   0 runner    (1001) docker     (123)     2455 2023-03-22 09:49:54.000000 mlserver-1.3.0.dev4/mlserver/codecs/datetime.py
--rw-r--r--   0 runner    (1001) docker     (123)     7198 2023-03-22 09:49:54.000000 mlserver-1.3.0.dev4/mlserver/codecs/decorator.py
--rw-r--r--   0 runner    (1001) docker     (123)     2056 2023-03-22 09:49:54.000000 mlserver-1.3.0.dev4/mlserver/codecs/errors.py
--rw-r--r--   0 runner    (1001) docker     (123)      749 2023-03-22 09:49:54.000000 mlserver-1.3.0.dev4/mlserver/codecs/lists.py
--rw-r--r--   0 runner    (1001) docker     (123)     4955 2023-03-22 09:49:54.000000 mlserver-1.3.0.dev4/mlserver/codecs/numpy.py
--rw-r--r--   0 runner    (1001) docker     (123)     3674 2023-03-22 09:49:54.000000 mlserver-1.3.0.dev4/mlserver/codecs/pandas.py
--rw-r--r--   0 runner    (1001) docker     (123)     2825 2023-03-22 09:49:54.000000 mlserver-1.3.0.dev4/mlserver/codecs/string.py
--rw-r--r--   0 runner    (1001) docker     (123)     7557 2023-03-22 09:49:54.000000 mlserver-1.3.0.dev4/mlserver/codecs/utils.py
--rw-r--r--   0 runner    (1001) docker     (123)     2750 2023-03-22 09:49:54.000000 mlserver-1.3.0.dev4/mlserver/env.py
--rw-r--r--   0 runner    (1001) docker     (123)     1175 2023-03-22 09:49:54.000000 mlserver-1.3.0.dev4/mlserver/errors.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-22 09:50:33.186761 mlserver-1.3.0.dev4/mlserver/grpc/
--rw-r--r--   0 runner    (1001) docker     (123)       57 2023-03-22 09:49:54.000000 mlserver-1.3.0.dev4/mlserver/grpc/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    16463 2023-03-22 09:49:54.000000 mlserver-1.3.0.dev4/mlserver/grpc/converters.py
--rw-r--r--   0 runner    (1001) docker     (123)    31033 2023-03-22 09:49:54.000000 mlserver-1.3.0.dev4/mlserver/grpc/dataplane_pb2.py
--rw-r--r--   0 runner    (1001) docker     (123)    15571 2023-03-22 09:49:54.000000 mlserver-1.3.0.dev4/mlserver/grpc/dataplane_pb2_grpc.py
--rw-r--r--   0 runner    (1001) docker     (123)     8624 2023-03-22 09:49:54.000000 mlserver-1.3.0.dev4/mlserver/grpc/interceptors.py
--rw-r--r--   0 runner    (1001) docker     (123)       92 2023-03-22 09:49:54.000000 mlserver-1.3.0.dev4/mlserver/grpc/logging.py
--rw-r--r--   0 runner    (1001) docker     (123)     2021 2023-03-22 09:49:54.000000 mlserver-1.3.0.dev4/mlserver/grpc/model_repository.py
--rw-r--r--   0 runner    (1001) docker     (123)     6507 2023-03-22 09:49:54.000000 mlserver-1.3.0.dev4/mlserver/grpc/model_repository_pb2.py
--rw-r--r--   0 runner    (1001) docker     (123)     6338 2023-03-22 09:49:54.000000 mlserver-1.3.0.dev4/mlserver/grpc/model_repository_pb2_grpc.py
--rw-r--r--   0 runner    (1001) docker     (123)     3398 2023-03-22 09:49:54.000000 mlserver-1.3.0.dev4/mlserver/grpc/server.py
--rw-r--r--   0 runner    (1001) docker     (123)     4044 2023-03-22 09:49:54.000000 mlserver-1.3.0.dev4/mlserver/grpc/servicers.py
--rw-r--r--   0 runner    (1001) docker     (123)     1679 2023-03-22 09:49:54.000000 mlserver-1.3.0.dev4/mlserver/grpc/utils.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-22 09:50:33.186761 mlserver-1.3.0.dev4/mlserver/handlers/
--rw-r--r--   0 runner    (1001) docker     (123)      255 2023-03-22 09:49:54.000000 mlserver-1.3.0.dev4/mlserver/handlers/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     1038 2023-03-22 09:49:54.000000 mlserver-1.3.0.dev4/mlserver/handlers/custom.py
--rw-r--r--   0 runner    (1001) docker     (123)     3497 2023-03-22 09:49:54.000000 mlserver-1.3.0.dev4/mlserver/handlers/dataplane.py
--rw-r--r--   0 runner    (1001) docker     (123)     2906 2023-03-22 09:49:54.000000 mlserver-1.3.0.dev4/mlserver/handlers/model_repository.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-22 09:50:33.186761 mlserver-1.3.0.dev4/mlserver/kafka/
--rw-r--r--   0 runner    (1001) docker     (123)       59 2023-03-22 09:49:54.000000 mlserver-1.3.0.dev4/mlserver/kafka/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      358 2023-03-22 09:49:54.000000 mlserver-1.3.0.dev4/mlserver/kafka/errors.py
--rw-r--r--   0 runner    (1001) docker     (123)     1624 2023-03-22 09:49:54.000000 mlserver-1.3.0.dev4/mlserver/kafka/handlers.py
--rw-r--r--   0 runner    (1001) docker     (123)       85 2023-03-22 09:49:54.000000 mlserver-1.3.0.dev4/mlserver/kafka/logging.py
--rw-r--r--   0 runner    (1001) docker     (123)     1694 2023-03-22 09:49:54.000000 mlserver-1.3.0.dev4/mlserver/kafka/message.py
--rw-r--r--   0 runner    (1001) docker     (123)     3547 2023-03-22 09:49:54.000000 mlserver-1.3.0.dev4/mlserver/kafka/server.py
--rw-r--r--   0 runner    (1001) docker     (123)     1589 2023-03-22 09:49:54.000000 mlserver-1.3.0.dev4/mlserver/logging.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-22 09:50:33.190762 mlserver-1.3.0.dev4/mlserver/metrics/
--rw-r--r--   0 runner    (1001) docker     (123)      212 2023-03-22 09:49:54.000000 mlserver-1.3.0.dev4/mlserver/metrics/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     2244 2023-03-22 09:49:54.000000 mlserver-1.3.0.dev4/mlserver/metrics/context.py
--rw-r--r--   0 runner    (1001) docker     (123)     1030 2023-03-22 09:49:54.000000 mlserver-1.3.0.dev4/mlserver/metrics/errors.py
--rw-r--r--   0 runner    (1001) docker     (123)       87 2023-03-22 09:49:54.000000 mlserver-1.3.0.dev4/mlserver/metrics/logging.py
--rw-r--r--   0 runner    (1001) docker     (123)     1908 2023-03-22 09:49:54.000000 mlserver-1.3.0.dev4/mlserver/metrics/prometheus.py
--rw-r--r--   0 runner    (1001) docker     (123)      975 2023-03-22 09:49:54.000000 mlserver-1.3.0.dev4/mlserver/metrics/registry.py
--rw-r--r--   0 runner    (1001) docker     (123)     2453 2023-03-22 09:49:54.000000 mlserver-1.3.0.dev4/mlserver/metrics/server.py
--rw-r--r--   0 runner    (1001) docker     (123)     1478 2023-03-22 09:49:54.000000 mlserver-1.3.0.dev4/mlserver/middleware.py
--rw-r--r--   0 runner    (1001) docker     (123)     7781 2023-03-22 09:49:54.000000 mlserver-1.3.0.dev4/mlserver/model.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-22 09:50:33.190762 mlserver-1.3.0.dev4/mlserver/parallel/
--rw-r--r--   0 runner    (1001) docker     (123)      170 2023-03-22 09:49:54.000000 mlserver-1.3.0.dev4/mlserver/parallel/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     5330 2023-03-22 09:49:54.000000 mlserver-1.3.0.dev4/mlserver/parallel/dispatcher.py
--rw-r--r--   0 runner    (1001) docker     (123)      811 2023-03-22 09:49:54.000000 mlserver-1.3.0.dev4/mlserver/parallel/errors.py
--rw-r--r--   0 runner    (1001) docker     (123)       96 2023-03-22 09:49:54.000000 mlserver-1.3.0.dev4/mlserver/parallel/logging.py
--rw-r--r--   0 runner    (1001) docker     (123)     1647 2023-03-22 09:49:54.000000 mlserver-1.3.0.dev4/mlserver/parallel/messages.py
--rw-r--r--   0 runner    (1001) docker     (123)     2607 2023-03-22 09:49:54.000000 mlserver-1.3.0.dev4/mlserver/parallel/model.py
--rw-r--r--   0 runner    (1001) docker     (123)     5111 2023-03-22 09:49:54.000000 mlserver-1.3.0.dev4/mlserver/parallel/pool.py
--rw-r--r--   0 runner    (1001) docker     (123)     1113 2023-03-22 09:49:54.000000 mlserver-1.3.0.dev4/mlserver/parallel/utils.py
--rw-r--r--   0 runner    (1001) docker     (123)     6868 2023-03-22 09:49:54.000000 mlserver-1.3.0.dev4/mlserver/parallel/worker.py
--rw-r--r--   0 runner    (1001) docker     (123)     3146 2023-03-22 09:49:54.000000 mlserver-1.3.0.dev4/mlserver/raw.py
--rw-r--r--   0 runner    (1001) docker     (123)    10404 2023-03-22 09:49:54.000000 mlserver-1.3.0.dev4/mlserver/registry.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-22 09:50:33.190762 mlserver-1.3.0.dev4/mlserver/repository/
--rw-r--r--   0 runner    (1001) docker     (123)      302 2023-03-22 09:49:54.000000 mlserver-1.3.0.dev4/mlserver/repository/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      697 2023-03-22 09:49:54.000000 mlserver-1.3.0.dev4/mlserver/repository/factory.py
--rw-r--r--   0 runner    (1001) docker     (123)     1587 2023-03-22 09:49:54.000000 mlserver-1.3.0.dev4/mlserver/repository/load.py
--rw-r--r--   0 runner    (1001) docker     (123)     2560 2023-03-22 09:49:54.000000 mlserver-1.3.0.dev4/mlserver/repository/repository.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-22 09:50:33.190762 mlserver-1.3.0.dev4/mlserver/rest/
--rw-r--r--   0 runner    (1001) docker     (123)       57 2023-03-22 09:49:54.000000 mlserver-1.3.0.dev4/mlserver/rest/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     4484 2023-03-22 09:49:54.000000 mlserver-1.3.0.dev4/mlserver/rest/app.py
--rw-r--r--   0 runner    (1001) docker     (123)     2844 2023-03-22 09:49:54.000000 mlserver-1.3.0.dev4/mlserver/rest/endpoints.py
--rw-r--r--   0 runner    (1001) docker     (123)      492 2023-03-22 09:49:54.000000 mlserver-1.3.0.dev4/mlserver/rest/errors.py
--rw-r--r--   0 runner    (1001) docker     (123)      876 2023-03-22 09:49:54.000000 mlserver-1.3.0.dev4/mlserver/rest/logging.py
--rw-r--r--   0 runner    (1001) docker     (123)      882 2023-03-22 09:49:54.000000 mlserver-1.3.0.dev4/mlserver/rest/requests.py
--rw-r--r--   0 runner    (1001) docker     (123)     1958 2023-03-22 09:49:54.000000 mlserver-1.3.0.dev4/mlserver/rest/responses.py
--rw-r--r--   0 runner    (1001) docker     (123)     3212 2023-03-22 09:49:54.000000 mlserver-1.3.0.dev4/mlserver/rest/server.py
--rw-r--r--   0 runner    (1001) docker     (123)      890 2023-03-22 09:49:54.000000 mlserver-1.3.0.dev4/mlserver/rest/utils.py
--rw-r--r--   0 runner    (1001) docker     (123)     6170 2023-03-22 09:49:54.000000 mlserver-1.3.0.dev4/mlserver/server.py
--rw-r--r--   0 runner    (1001) docker     (123)     9047 2023-03-22 09:49:54.000000 mlserver-1.3.0.dev4/mlserver/settings.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-22 09:50:33.190762 mlserver-1.3.0.dev4/mlserver/types/
--rw-r--r--   0 runner    (1001) docker     (123)     1096 2023-03-22 09:49:54.000000 mlserver-1.3.0.dev4/mlserver/types/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      655 2023-03-22 09:49:54.000000 mlserver-1.3.0.dev4/mlserver/types/base.py
--rw-r--r--   0 runner    (1001) docker     (123)     2115 2023-03-22 09:49:54.000000 mlserver-1.3.0.dev4/mlserver/types/dataplane.py
--rw-r--r--   0 runner    (1001) docker     (123)     1042 2023-03-22 09:49:54.000000 mlserver-1.3.0.dev4/mlserver/types/model_repository.py
--rw-r--r--   0 runner    (1001) docker     (123)     3998 2023-03-22 09:49:54.000000 mlserver-1.3.0.dev4/mlserver/utils.py
--rw-r--r--   0 runner    (1001) docker     (123)       27 2023-03-22 09:49:54.000000 mlserver-1.3.0.dev4/mlserver/version.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-22 09:50:33.182762 mlserver-1.3.0.dev4/mlserver.egg-info/
--rw-r--r--   0 runner    (1001) docker     (123)     6561 2023-03-22 09:50:33.000000 mlserver-1.3.0.dev4/mlserver.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)     2657 2023-03-22 09:50:33.000000 mlserver-1.3.0.dev4/mlserver.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-03-22 09:50:33.000000 mlserver-1.3.0.dev4/mlserver.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (123)       48 2023-03-22 09:50:33.000000 mlserver-1.3.0.dev4/mlserver.egg-info/entry_points.txt
--rw-r--r--   0 runner    (1001) docker     (123)      344 2023-03-22 09:50:33.000000 mlserver-1.3.0.dev4/mlserver.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (123)        9 2023-03-22 09:50:33.000000 mlserver-1.3.0.dev4/mlserver.egg-info/top_level.txt
--rw-r--r--   0 runner    (1001) docker     (123)     3964 2023-03-22 09:50:33.190762 mlserver-1.3.0.dev4/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (123)     1864 2023-03-22 09:49:54.000000 mlserver-1.3.0.dev4/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 13:37:59.370681 mlserver-1.3.0rc1/
+-rw-r--r--   0 runner    (1001) docker     (123)    11354 2023-04-06 13:37:15.000000 mlserver-1.3.0rc1/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (123)       23 2023-04-06 13:37:15.000000 mlserver-1.3.0rc1/MANIFEST.in
+-rw-r--r--   0 runner    (1001) docker     (123)     6559 2023-04-06 13:37:59.370681 mlserver-1.3.0rc1/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     5366 2023-04-06 13:37:15.000000 mlserver-1.3.0rc1/README.md
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 13:37:59.354681 mlserver-1.3.0rc1/mlserver/
+-rw-r--r--   0 runner    (1001) docker     (123)      299 2023-04-06 13:37:15.000000 mlserver-1.3.0rc1/mlserver/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    16113 2023-04-06 13:37:15.000000 mlserver-1.3.0rc1/mlserver/batch_processing.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 13:37:59.354681 mlserver-1.3.0rc1/mlserver/batching/
+-rw-r--r--   0 runner    (1001) docker     (123)      176 2023-04-06 13:37:15.000000 mlserver-1.3.0rc1/mlserver/batching/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5529 2023-04-06 13:37:15.000000 mlserver-1.3.0rc1/mlserver/batching/adaptive.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1856 2023-04-06 13:37:15.000000 mlserver-1.3.0rc1/mlserver/batching/hooks.py
+-rw-r--r--   0 runner    (1001) docker     (123)    10847 2023-04-06 13:37:15.000000 mlserver-1.3.0rc1/mlserver/batching/requests.py
+-rw-r--r--   0 runner    (1001) docker     (123)      911 2023-04-06 13:37:15.000000 mlserver-1.3.0rc1/mlserver/batching/shape.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 13:37:59.354681 mlserver-1.3.0rc1/mlserver/cli/
+-rw-r--r--   0 runner    (1001) docker     (123)       43 2023-04-06 13:37:15.000000 mlserver-1.3.0rc1/mlserver/cli/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1883 2023-04-06 13:37:15.000000 mlserver-1.3.0rc1/mlserver/cli/build.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2371 2023-04-06 13:37:15.000000 mlserver-1.3.0rc1/mlserver/cli/constants.py
+-rw-r--r--   0 runner    (1001) docker     (123)      427 2023-04-06 13:37:15.000000 mlserver-1.3.0rc1/mlserver/cli/init_project.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6813 2023-04-06 13:37:15.000000 mlserver-1.3.0rc1/mlserver/cli/main.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1318 2023-04-06 13:37:15.000000 mlserver-1.3.0rc1/mlserver/cli/serve.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3323 2023-04-06 13:37:15.000000 mlserver-1.3.0rc1/mlserver/cloudevents.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 13:37:59.358681 mlserver-1.3.0rc1/mlserver/codecs/
+-rw-r--r--   0 runner    (1001) docker     (123)     1177 2023-04-06 13:37:15.000000 mlserver-1.3.0rc1/mlserver/codecs/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9601 2023-04-06 13:37:15.000000 mlserver-1.3.0rc1/mlserver/codecs/base.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2575 2023-04-06 13:37:15.000000 mlserver-1.3.0rc1/mlserver/codecs/base64.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2455 2023-04-06 13:37:15.000000 mlserver-1.3.0rc1/mlserver/codecs/datetime.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7306 2023-04-06 13:37:15.000000 mlserver-1.3.0rc1/mlserver/codecs/decorator.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2056 2023-04-06 13:37:15.000000 mlserver-1.3.0rc1/mlserver/codecs/errors.py
+-rw-r--r--   0 runner    (1001) docker     (123)      749 2023-04-06 13:37:15.000000 mlserver-1.3.0rc1/mlserver/codecs/lists.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4955 2023-04-06 13:37:15.000000 mlserver-1.3.0rc1/mlserver/codecs/numpy.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3674 2023-04-06 13:37:15.000000 mlserver-1.3.0rc1/mlserver/codecs/pandas.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2825 2023-04-06 13:37:15.000000 mlserver-1.3.0rc1/mlserver/codecs/string.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7557 2023-04-06 13:37:15.000000 mlserver-1.3.0rc1/mlserver/codecs/utils.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3814 2023-04-06 13:37:15.000000 mlserver-1.3.0rc1/mlserver/env.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1494 2023-04-06 13:37:15.000000 mlserver-1.3.0rc1/mlserver/errors.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 13:37:59.358681 mlserver-1.3.0rc1/mlserver/grpc/
+-rw-r--r--   0 runner    (1001) docker     (123)       57 2023-04-06 13:37:15.000000 mlserver-1.3.0rc1/mlserver/grpc/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    16463 2023-04-06 13:37:15.000000 mlserver-1.3.0rc1/mlserver/grpc/converters.py
+-rw-r--r--   0 runner    (1001) docker     (123)    31033 2023-04-06 13:37:15.000000 mlserver-1.3.0rc1/mlserver/grpc/dataplane_pb2.py
+-rw-r--r--   0 runner    (1001) docker     (123)    15571 2023-04-06 13:37:15.000000 mlserver-1.3.0rc1/mlserver/grpc/dataplane_pb2_grpc.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8624 2023-04-06 13:37:15.000000 mlserver-1.3.0rc1/mlserver/grpc/interceptors.py
+-rw-r--r--   0 runner    (1001) docker     (123)       92 2023-04-06 13:37:15.000000 mlserver-1.3.0rc1/mlserver/grpc/logging.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2021 2023-04-06 13:37:15.000000 mlserver-1.3.0rc1/mlserver/grpc/model_repository.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6507 2023-04-06 13:37:15.000000 mlserver-1.3.0rc1/mlserver/grpc/model_repository_pb2.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6338 2023-04-06 13:37:15.000000 mlserver-1.3.0rc1/mlserver/grpc/model_repository_pb2_grpc.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3398 2023-04-06 13:37:15.000000 mlserver-1.3.0rc1/mlserver/grpc/server.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4044 2023-04-06 13:37:15.000000 mlserver-1.3.0rc1/mlserver/grpc/servicers.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1679 2023-04-06 13:37:15.000000 mlserver-1.3.0rc1/mlserver/grpc/utils.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 13:37:59.362681 mlserver-1.3.0rc1/mlserver/handlers/
+-rw-r--r--   0 runner    (1001) docker     (123)      255 2023-04-06 13:37:15.000000 mlserver-1.3.0rc1/mlserver/handlers/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1038 2023-04-06 13:37:15.000000 mlserver-1.3.0rc1/mlserver/handlers/custom.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3615 2023-04-06 13:37:15.000000 mlserver-1.3.0rc1/mlserver/handlers/dataplane.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2906 2023-04-06 13:37:15.000000 mlserver-1.3.0rc1/mlserver/handlers/model_repository.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 13:37:59.362681 mlserver-1.3.0rc1/mlserver/kafka/
+-rw-r--r--   0 runner    (1001) docker     (123)       59 2023-04-06 13:37:15.000000 mlserver-1.3.0rc1/mlserver/kafka/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      358 2023-04-06 13:37:15.000000 mlserver-1.3.0rc1/mlserver/kafka/errors.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1624 2023-04-06 13:37:15.000000 mlserver-1.3.0rc1/mlserver/kafka/handlers.py
+-rw-r--r--   0 runner    (1001) docker     (123)       85 2023-04-06 13:37:15.000000 mlserver-1.3.0rc1/mlserver/kafka/logging.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1694 2023-04-06 13:37:15.000000 mlserver-1.3.0rc1/mlserver/kafka/message.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3547 2023-04-06 13:37:15.000000 mlserver-1.3.0rc1/mlserver/kafka/server.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1589 2023-04-06 13:37:15.000000 mlserver-1.3.0rc1/mlserver/logging.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 13:37:59.362681 mlserver-1.3.0rc1/mlserver/metrics/
+-rw-r--r--   0 runner    (1001) docker     (123)      282 2023-04-06 13:37:15.000000 mlserver-1.3.0rc1/mlserver/metrics/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2244 2023-04-06 13:37:15.000000 mlserver-1.3.0rc1/mlserver/metrics/context.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1030 2023-04-06 13:37:15.000000 mlserver-1.3.0rc1/mlserver/metrics/errors.py
+-rw-r--r--   0 runner    (1001) docker     (123)       87 2023-04-06 13:37:15.000000 mlserver-1.3.0rc1/mlserver/metrics/logging.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1961 2023-04-06 13:37:15.000000 mlserver-1.3.0rc1/mlserver/metrics/prometheus.py
+-rw-r--r--   0 runner    (1001) docker     (123)      975 2023-04-06 13:37:15.000000 mlserver-1.3.0rc1/mlserver/metrics/registry.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2453 2023-04-06 13:37:15.000000 mlserver-1.3.0rc1/mlserver/metrics/server.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1478 2023-04-06 13:37:15.000000 mlserver-1.3.0rc1/mlserver/middleware.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7749 2023-04-06 13:37:15.000000 mlserver-1.3.0rc1/mlserver/model.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 13:37:59.366681 mlserver-1.3.0rc1/mlserver/parallel/
+-rw-r--r--   0 runner    (1001) docker     (123)      190 2023-04-06 13:37:15.000000 mlserver-1.3.0rc1/mlserver/parallel/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5632 2023-04-06 13:37:15.000000 mlserver-1.3.0rc1/mlserver/parallel/dispatcher.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1234 2023-04-06 13:37:15.000000 mlserver-1.3.0rc1/mlserver/parallel/errors.py
+-rw-r--r--   0 runner    (1001) docker     (123)       96 2023-04-06 13:37:15.000000 mlserver-1.3.0rc1/mlserver/parallel/logging.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1506 2023-04-06 13:37:15.000000 mlserver-1.3.0rc1/mlserver/parallel/messages.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2607 2023-04-06 13:37:15.000000 mlserver-1.3.0rc1/mlserver/parallel/model.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3838 2023-04-06 13:37:15.000000 mlserver-1.3.0rc1/mlserver/parallel/pool.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7325 2023-04-06 13:37:15.000000 mlserver-1.3.0rc1/mlserver/parallel/registry.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1113 2023-04-06 13:37:15.000000 mlserver-1.3.0rc1/mlserver/parallel/utils.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6868 2023-04-06 13:37:15.000000 mlserver-1.3.0rc1/mlserver/parallel/worker.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3146 2023-04-06 13:37:15.000000 mlserver-1.3.0rc1/mlserver/raw.py
+-rw-r--r--   0 runner    (1001) docker     (123)    10897 2023-04-06 13:37:15.000000 mlserver-1.3.0rc1/mlserver/registry.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 13:37:59.366681 mlserver-1.3.0rc1/mlserver/repository/
+-rw-r--r--   0 runner    (1001) docker     (123)      302 2023-04-06 13:37:15.000000 mlserver-1.3.0rc1/mlserver/repository/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      697 2023-04-06 13:37:15.000000 mlserver-1.3.0rc1/mlserver/repository/factory.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1587 2023-04-06 13:37:15.000000 mlserver-1.3.0rc1/mlserver/repository/load.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2560 2023-04-06 13:37:15.000000 mlserver-1.3.0rc1/mlserver/repository/repository.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 13:37:59.370681 mlserver-1.3.0rc1/mlserver/rest/
+-rw-r--r--   0 runner    (1001) docker     (123)       57 2023-04-06 13:37:15.000000 mlserver-1.3.0rc1/mlserver/rest/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5268 2023-04-06 13:37:15.000000 mlserver-1.3.0rc1/mlserver/rest/app.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4450 2023-04-06 13:37:15.000000 mlserver-1.3.0rc1/mlserver/rest/endpoints.py
+-rw-r--r--   0 runner    (1001) docker     (123)      492 2023-04-06 13:37:15.000000 mlserver-1.3.0rc1/mlserver/rest/errors.py
+-rw-r--r--   0 runner    (1001) docker     (123)      876 2023-04-06 13:37:15.000000 mlserver-1.3.0rc1/mlserver/rest/logging.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3383 2023-04-06 13:37:15.000000 mlserver-1.3.0rc1/mlserver/rest/openapi.py
+-rw-r--r--   0 runner    (1001) docker     (123)      882 2023-04-06 13:37:15.000000 mlserver-1.3.0rc1/mlserver/rest/requests.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1958 2023-04-06 13:37:15.000000 mlserver-1.3.0rc1/mlserver/rest/responses.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3212 2023-04-06 13:37:15.000000 mlserver-1.3.0rc1/mlserver/rest/server.py
+-rw-r--r--   0 runner    (1001) docker     (123)      890 2023-04-06 13:37:15.000000 mlserver-1.3.0rc1/mlserver/rest/utils.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6534 2023-04-06 13:37:15.000000 mlserver-1.3.0rc1/mlserver/server.py
+-rw-r--r--   0 runner    (1001) docker     (123)    12403 2023-04-06 13:37:15.000000 mlserver-1.3.0rc1/mlserver/settings.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 13:37:59.370681 mlserver-1.3.0rc1/mlserver/types/
+-rw-r--r--   0 runner    (1001) docker     (123)     1096 2023-04-06 13:37:15.000000 mlserver-1.3.0rc1/mlserver/types/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      655 2023-04-06 13:37:15.000000 mlserver-1.3.0rc1/mlserver/types/base.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2115 2023-04-06 13:37:15.000000 mlserver-1.3.0rc1/mlserver/types/dataplane.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1042 2023-04-06 13:37:15.000000 mlserver-1.3.0rc1/mlserver/types/model_repository.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3922 2023-04-06 13:37:15.000000 mlserver-1.3.0rc1/mlserver/utils.py
+-rw-r--r--   0 runner    (1001) docker     (123)       26 2023-04-06 13:37:15.000000 mlserver-1.3.0rc1/mlserver/version.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 13:37:59.354681 mlserver-1.3.0rc1/mlserver.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)     6559 2023-04-06 13:37:59.000000 mlserver-1.3.0rc1/mlserver.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     2777 2023-04-06 13:37:59.000000 mlserver-1.3.0rc1/mlserver.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-06 13:37:59.000000 mlserver-1.3.0rc1/mlserver.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       48 2023-04-06 13:37:59.000000 mlserver-1.3.0rc1/mlserver.egg-info/entry_points.txt
+-rw-r--r--   0 runner    (1001) docker     (123)      318 2023-04-06 13:37:59.000000 mlserver-1.3.0rc1/mlserver.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        9 2023-04-06 13:37:59.000000 mlserver-1.3.0rc1/mlserver.egg-info/top_level.txt
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 13:37:59.370681 mlserver-1.3.0rc1/openapi/
+-rw-r--r--   0 runner    (1001) docker     (123)    19065 2023-04-06 13:37:15.000000 mlserver-1.3.0rc1/openapi/dataplane.json
+-rw-r--r--   0 runner    (1001) docker     (123)     5385 2023-04-06 13:37:15.000000 mlserver-1.3.0rc1/openapi/model_repository.json
+-rw-r--r--   0 runner    (1001) docker     (123)     4005 2023-04-06 13:37:59.370681 mlserver-1.3.0rc1/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (123)     2091 2023-04-06 13:37:15.000000 mlserver-1.3.0rc1/setup.py
```

### Comparing `mlserver-1.3.0.dev4/LICENSE` & `mlserver-1.3.0rc1/LICENSE`

 * *Files identical despite different names*

### Comparing `mlserver-1.3.0.dev4/PKG-INFO` & `mlserver-1.3.0rc1/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: mlserver
-Version: 1.3.0.dev4
+Version: 1.3.0rc1
 Summary: ML server
 Home-page: https://github.com/SeldonIO/MLServer.git
 Author: Seldon Technologies Ltd.
 Author-email: hello@seldon.io
 License: Apache 2.0
 Description: # MLServer
```

### Comparing `mlserver-1.3.0.dev4/README.md` & `mlserver-1.3.0rc1/README.md`

 * *Files identical despite different names*

### Comparing `mlserver-1.3.0.dev4/mlserver/batch_processing.py` & `mlserver-1.3.0rc1/mlserver/batch_processing.py`

 * *Files identical despite different names*

### Comparing `mlserver-1.3.0.dev4/mlserver/batching/adaptive.py` & `mlserver-1.3.0rc1/mlserver/batching/adaptive.py`

 * *Files identical despite different names*

### Comparing `mlserver-1.3.0.dev4/mlserver/batching/hooks.py` & `mlserver-1.3.0rc1/mlserver/batching/hooks.py`

 * *Files identical despite different names*

### Comparing `mlserver-1.3.0.dev4/mlserver/batching/requests.py` & `mlserver-1.3.0rc1/mlserver/batching/requests.py`

 * *Files identical despite different names*

### Comparing `mlserver-1.3.0.dev4/mlserver/batching/shape.py` & `mlserver-1.3.0rc1/mlserver/batching/shape.py`

 * *Files identical despite different names*

### Comparing `mlserver-1.3.0.dev4/mlserver/cli/build.py` & `mlserver-1.3.0rc1/mlserver/cli/build.py`

 * *Files identical despite different names*

### Comparing `mlserver-1.3.0.dev4/mlserver/cli/constants.py` & `mlserver-1.3.0rc1/mlserver/cli/constants.py`

 * *Files identical despite different names*

### Comparing `mlserver-1.3.0.dev4/mlserver/cli/main.py` & `mlserver-1.3.0rc1/mlserver/cli/main.py`

 * *Files identical despite different names*

### Comparing `mlserver-1.3.0.dev4/mlserver/cli/serve.py` & `mlserver-1.3.0rc1/mlserver/cli/serve.py`

 * *Files identical despite different names*

### Comparing `mlserver-1.3.0.dev4/mlserver/cloudevents.py` & `mlserver-1.3.0rc1/mlserver/cloudevents.py`

 * *Files identical despite different names*

### Comparing `mlserver-1.3.0.dev4/mlserver/codecs/__init__.py` & `mlserver-1.3.0rc1/mlserver/codecs/__init__.py`

 * *Files identical despite different names*

### Comparing `mlserver-1.3.0.dev4/mlserver/codecs/base.py` & `mlserver-1.3.0rc1/mlserver/codecs/base.py`

 * *Files identical despite different names*

### Comparing `mlserver-1.3.0.dev4/mlserver/codecs/base64.py` & `mlserver-1.3.0rc1/mlserver/codecs/base64.py`

 * *Files identical despite different names*

### Comparing `mlserver-1.3.0.dev4/mlserver/codecs/datetime.py` & `mlserver-1.3.0rc1/mlserver/codecs/datetime.py`

 * *Files identical despite different names*

### Comparing `mlserver-1.3.0.dev4/mlserver/codecs/decorator.py` & `mlserver-1.3.0rc1/mlserver/codecs/decorator.py`

 * *Files 2% similar despite different names*

```diff
@@ -34,14 +34,18 @@
     if a is None:
         return []
 
     if isinstance(a, tuple):
         # Split into components
         return list(a)
 
+    if get_origin(a) is tuple:
+        # Convert type arguments into list
+        return list(get_args(a))
+
     # Otherwise, assume it's a single element
     return [a]
 
 
 def _is_codec_type(c: Codec, t: Type) -> bool:
     if issubclass(c, t):  # type: ignore
         return True
```

### Comparing `mlserver-1.3.0.dev4/mlserver/codecs/errors.py` & `mlserver-1.3.0rc1/mlserver/codecs/errors.py`

 * *Files identical despite different names*

### Comparing `mlserver-1.3.0.dev4/mlserver/codecs/lists.py` & `mlserver-1.3.0rc1/mlserver/codecs/lists.py`

 * *Files identical despite different names*

### Comparing `mlserver-1.3.0.dev4/mlserver/codecs/numpy.py` & `mlserver-1.3.0rc1/mlserver/codecs/numpy.py`

 * *Files identical despite different names*

### Comparing `mlserver-1.3.0.dev4/mlserver/codecs/pandas.py` & `mlserver-1.3.0rc1/mlserver/codecs/pandas.py`

 * *Files identical despite different names*

### Comparing `mlserver-1.3.0.dev4/mlserver/codecs/string.py` & `mlserver-1.3.0rc1/mlserver/codecs/string.py`

 * *Files identical despite different names*

### Comparing `mlserver-1.3.0.dev4/mlserver/codecs/utils.py` & `mlserver-1.3.0rc1/mlserver/codecs/utils.py`

 * *Files identical despite different names*

### Comparing `mlserver-1.3.0.dev4/mlserver/env.py` & `mlserver-1.3.0rc1/mlserver/env.py`

 * *Files 24% similar despite different names*

```diff
@@ -1,44 +1,78 @@
 import asyncio
 import os
 import sys
 import tarfile
 import glob
+import hashlib
 
-from typing import List
+from typing import List, Optional
 from functools import cached_property
 
 from .logging import logger
 
 
 def _extract_env(tarball_path: str, env_path: str) -> None:
     logger.info(f"Extracting environment tarball from {tarball_path}...")
     with tarfile.open(tarball_path, "r") as tarball:
         tarball.extractall(path=env_path)
 
 
+def _compute_hash(tarball_path: str) -> str:
+    """
+    From Python 3.11's implementation of `hashlib.file_digest()`:
+    https://github.com/python/cpython/blob/3.11/Lib/hashlib.py#L257
+    """
+    h = hashlib.sha256()
+    buffer_size = 2**18
+
+    # Disable IO buffering since it's handled explicitly below
+    with open(tarball_path, "rb", buffering=0) as env_file:
+        buffer = bytearray(buffer_size)
+        view = memoryview(buffer)
+        while True:
+            size = env_file.readinto(buffer)
+            if size == 0:
+                break
+            h.update(view[:size])
+
+    return h.hexdigest()
+
+
+async def compute_hash(tarball_path: str) -> str:
+    loop = asyncio.get_running_loop()
+    return await loop.run_in_executor(None, _compute_hash, tarball_path)
+
+
 class Environment:
     """
     Custom Python environment.
     The class can be used as a context manager to enable / disable the custom
     environment.
     """
 
-    def __init__(self, env_path: str):
+    def __init__(self, env_path: str, env_hash: str):
         self._env_path = env_path
+        self.env_hash = env_hash
 
     @classmethod
-    async def from_tarball(cls, tarball_path: str, env_path: str) -> "Environment":
+    async def from_tarball(
+        cls, tarball_path: str, env_path: str, env_hash: Optional[str] = None
+    ) -> "Environment":
         """
         Instantiate an Environment object from an environment tarball.
+        If the env hash is not provided, it will be computed on-the-fly.
         """
         loop = asyncio.get_running_loop()
         await loop.run_in_executor(None, _extract_env, tarball_path, env_path)
 
-        return cls(env_path)
+        if not env_hash:
+            env_hash = await compute_hash(tarball_path)
+
+        return cls(env_path, env_hash)
 
     @cached_property
     def _sys_path(self) -> List[str]:
         """
         Extra paths that will be added to `sys.path` (i.e. `PYTHONPATH`) to
         expose the custom environment.
         These paths are mainly used on the `__enter__` method of the context
```

### Comparing `mlserver-1.3.0.dev4/mlserver/errors.py` & `mlserver-1.3.0rc1/mlserver/errors.py`

 * *Files 16% similar despite different names*

```diff
@@ -22,14 +22,23 @@
         msg = f"Model {name} not found"
         if version is not None:
             msg = f"Model {name} with version {version} not found"
 
         super().__init__(msg, status.HTTP_404_NOT_FOUND)
 
 
+class ModelNotReady(MLServerError):
+    def __init__(self, name: str, version: Optional[str] = None):
+        msg = f"Model {name} is not ready yet."
+        if version is not None:
+            msg = f"Model {name} with version {version} is not ready yet."
+
+        super().__init__(msg, status.HTTP_400_BAD_REQUEST)
+
+
 class InferenceError(MLServerError):
     def __init__(self, msg: str):
         super().__init__(msg, status.HTTP_400_BAD_REQUEST)
 
 
 class ModelParametersMissing(MLServerError):
     def __init__(self, model_name: str):
```

### Comparing `mlserver-1.3.0.dev4/mlserver/grpc/converters.py` & `mlserver-1.3.0rc1/mlserver/grpc/converters.py`

 * *Files identical despite different names*

### Comparing `mlserver-1.3.0.dev4/mlserver/grpc/dataplane_pb2.py` & `mlserver-1.3.0rc1/mlserver/grpc/dataplane_pb2.py`

 * *Files identical despite different names*

### Comparing `mlserver-1.3.0.dev4/mlserver/grpc/dataplane_pb2_grpc.py` & `mlserver-1.3.0rc1/mlserver/grpc/dataplane_pb2_grpc.py`

 * *Files identical despite different names*

### Comparing `mlserver-1.3.0.dev4/mlserver/grpc/interceptors.py` & `mlserver-1.3.0rc1/mlserver/grpc/interceptors.py`

 * *Files identical despite different names*

### Comparing `mlserver-1.3.0.dev4/mlserver/grpc/model_repository.py` & `mlserver-1.3.0rc1/mlserver/grpc/model_repository.py`

 * *Files identical despite different names*

### Comparing `mlserver-1.3.0.dev4/mlserver/grpc/model_repository_pb2.py` & `mlserver-1.3.0rc1/mlserver/grpc/model_repository_pb2.py`

 * *Files identical despite different names*

### Comparing `mlserver-1.3.0.dev4/mlserver/grpc/model_repository_pb2_grpc.py` & `mlserver-1.3.0rc1/mlserver/grpc/model_repository_pb2_grpc.py`

 * *Files identical despite different names*

### Comparing `mlserver-1.3.0.dev4/mlserver/grpc/server.py` & `mlserver-1.3.0rc1/mlserver/grpc/server.py`

 * *Files identical despite different names*

### Comparing `mlserver-1.3.0.dev4/mlserver/grpc/servicers.py` & `mlserver-1.3.0rc1/mlserver/grpc/servicers.py`

 * *Files identical despite different names*

### Comparing `mlserver-1.3.0.dev4/mlserver/grpc/utils.py` & `mlserver-1.3.0rc1/mlserver/grpc/utils.py`

 * *Files identical despite different names*

### Comparing `mlserver-1.3.0.dev4/mlserver/handlers/custom.py` & `mlserver-1.3.0rc1/mlserver/handlers/custom.py`

 * *Files identical despite different names*

### Comparing `mlserver-1.3.0.dev4/mlserver/handlers/dataplane.py` & `mlserver-1.3.0rc1/mlserver/handlers/dataplane.py`

 * *Files 10% similar despite different names*

```diff
@@ -1,13 +1,14 @@
 from prometheus_client import (
     Counter,
     Summary,
 )
 from typing import Optional
 
+from ..errors import ModelNotReady
 from ..metrics import model_context
 from ..settings import Settings
 from ..registry import MultiModelRegistry
 from ..types import (
     MetadataModelResponse,
     MetadataServerResponse,
     InferenceRequest,
@@ -88,14 +89,16 @@
         ).count_exceptions()
 
         with infer_duration, infer_errors:
             if payload.id is None:
                 payload.id = generate_uuid()
 
             model = await self._model_registry.get_model(name, version)
+            if not model.ready:
+                raise ModelNotReady(name, version)
 
             self._inference_middleware.request_middleware(payload, model.settings)
 
             # TODO: Make await optional for sync methods
             with model_context(model.settings):
                 prediction = await model.predict(payload)
```

### Comparing `mlserver-1.3.0.dev4/mlserver/handlers/model_repository.py` & `mlserver-1.3.0rc1/mlserver/handlers/model_repository.py`

 * *Files identical despite different names*

### Comparing `mlserver-1.3.0.dev4/mlserver/kafka/handlers.py` & `mlserver-1.3.0rc1/mlserver/kafka/handlers.py`

 * *Files identical despite different names*

### Comparing `mlserver-1.3.0.dev4/mlserver/kafka/message.py` & `mlserver-1.3.0rc1/mlserver/kafka/message.py`

 * *Files identical despite different names*

### Comparing `mlserver-1.3.0.dev4/mlserver/kafka/server.py` & `mlserver-1.3.0rc1/mlserver/kafka/server.py`

 * *Files identical despite different names*

### Comparing `mlserver-1.3.0.dev4/mlserver/logging.py` & `mlserver-1.3.0rc1/mlserver/logging.py`

 * *Files identical despite different names*

### Comparing `mlserver-1.3.0.dev4/mlserver/metrics/context.py` & `mlserver-1.3.0rc1/mlserver/metrics/context.py`

 * *Files identical despite different names*

### Comparing `mlserver-1.3.0.dev4/mlserver/metrics/errors.py` & `mlserver-1.3.0rc1/mlserver/metrics/errors.py`

 * *Files identical despite different names*

### Comparing `mlserver-1.3.0.dev4/mlserver/metrics/prometheus.py` & `mlserver-1.3.0rc1/mlserver/metrics/prometheus.py`

 * *Files 2% similar despite different names*

```diff
@@ -22,14 +22,15 @@
     if not settings.parallel_workers:
         return
 
     # Re-set Prometheus' Value class to use the multiproc version.
     # Note that this workaround depends on initialising all metrics in a
     # lazy manner (i.e. not as global values)
     # https://github.com/prometheus/client_python/blob/781e3e1851d80a53732bb8102d5754cf9d68b3c1/prometheus_client/values.py#L126-L134
+    os.makedirs(settings.metrics_dir, exist_ok=True)
     os.environ[PROMETHEUS_MULTIPROC_DIR] = settings.metrics_dir
     values.ValueClass = values.get_value_class()
 
 
 async def stop_metrics(settings: Settings, pid: int):
     if not settings.parallel_workers:
         return
```

### Comparing `mlserver-1.3.0.dev4/mlserver/metrics/registry.py` & `mlserver-1.3.0rc1/mlserver/metrics/registry.py`

 * *Files identical despite different names*

### Comparing `mlserver-1.3.0.dev4/mlserver/metrics/server.py` & `mlserver-1.3.0rc1/mlserver/metrics/server.py`

 * *Files identical despite different names*

### Comparing `mlserver-1.3.0.dev4/mlserver/middleware.py` & `mlserver-1.3.0rc1/mlserver/middleware.py`

 * *Files identical despite different names*

### Comparing `mlserver-1.3.0.dev4/mlserver/model.py` & `mlserver-1.3.0rc1/mlserver/model.py`

 * *Files 1% similar despite different names*

```diff
@@ -63,16 +63,15 @@
         enabled).
         Its return value will represent the model's readiness status.
         A return value of ``True`` will mean the model is ready.
 
         **This method should be overriden to implement your custom load
         logic.**
         """
-        self.ready = True
-        return self.ready
+        return True
 
     async def predict(self, payload: InferenceRequest) -> InferenceResponse:
         """
         Method responsible for running inference on the model.
 
 
         **This method should be overriden to implement your custom inference
```

### Comparing `mlserver-1.3.0.dev4/mlserver/parallel/dispatcher.py` & `mlserver-1.3.0rc1/mlserver/parallel/dispatcher.py`

 * *Files 4% similar despite different names*

```diff
@@ -3,40 +3,50 @@
 from typing import Dict, List, Tuple
 from itertools import cycle
 from multiprocessing import Queue
 from concurrent.futures import ThreadPoolExecutor
 from asyncio import Future
 
 from ..utils import schedule_with_callback, generate_uuid
+from ..metrics import REGISTRY
 
 from .worker import Worker
 from .logging import logger
 from .utils import END_OF_QUEUE, cancel_task
 from .messages import (
     Message,
     ModelUpdateMessage,
     ModelRequestMessage,
     ModelResponseMessage,
 )
 from prometheus_client import Histogram
 
+QUEUE_METRIC_NAME = "parallel_request_queue"
+
 
 class Dispatcher:
     def __init__(self, workers: Dict[int, Worker], responses: Queue):
         self._responses = responses
         self._workers = workers
         self._workers_round_robin = cycle(self._workers.keys())
         self._active = False
         self._process_responses_task = None
         self._executor = ThreadPoolExecutor()
         self._async_responses: Dict[str, Future[ModelResponseMessage]] = {}
-        self.parallel_request_queue_size = Histogram(
-            "parallel_request_queue",
+        self.parallel_request_queue_size = self._get_or_create_metric()
+
+    def _get_or_create_metric(self) -> Histogram:
+        if QUEUE_METRIC_NAME in REGISTRY:
+            return REGISTRY[QUEUE_METRIC_NAME]  # type: ignore
+
+        return Histogram(
+            QUEUE_METRIC_NAME,
             "counter of request queue size for workers",
             ["workerpid"],
+            registry=REGISTRY,
         )
 
     def start(self):
         self._active = True
         self._process_responses_task = schedule_with_callback(
             self._process_responses(), self._process_responses_cb
         )
```

### Comparing `mlserver-1.3.0.dev4/mlserver/parallel/messages.py` & `mlserver-1.3.0rc1/mlserver/parallel/messages.py`

 * *Files 13% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 import json
 
 from asyncio import CancelledError
 from enum import IntEnum
 from pydantic import BaseModel, Field
 from typing import Any, Dict, List, Optional, Union
 
-from ..utils import get_import_path, generate_uuid
+from ..utils import generate_uuid
 from ..settings import ModelSettings
 
 
 class ModelUpdateType(IntEnum):
     Load = 1
     Unload = 2
 
@@ -43,15 +43,14 @@
         model_settings = kwargs.pop("model_settings", None)
         if model_settings:
             as_dict = model_settings.dict()
             # Ensure the private `_source` attr also gets serialised
             if model_settings._source:
                 as_dict["_source"] = model_settings._source
 
-            import_path = get_import_path(model_settings.implementation)
-            as_dict["implementation"] = import_path
             kwargs["serialised_model_settings"] = json.dumps(as_dict)
+
         return super().__init__(*args, **kwargs)
 
     @property
     def model_settings(self) -> ModelSettings:
         return ModelSettings.parse_raw(self.serialised_model_settings)
```

### Comparing `mlserver-1.3.0.dev4/mlserver/parallel/model.py` & `mlserver-1.3.0rc1/mlserver/parallel/model.py`

 * *Files identical despite different names*

### Comparing `mlserver-1.3.0.dev4/mlserver/parallel/utils.py` & `mlserver-1.3.0rc1/mlserver/parallel/utils.py`

 * *Files identical despite different names*

### Comparing `mlserver-1.3.0.dev4/mlserver/parallel/worker.py` & `mlserver-1.3.0rc1/mlserver/parallel/worker.py`

 * *Files identical despite different names*

### Comparing `mlserver-1.3.0.dev4/mlserver/raw.py` & `mlserver-1.3.0rc1/mlserver/raw.py`

 * *Files identical despite different names*

### Comparing `mlserver-1.3.0.dev4/mlserver/registry.py` & `mlserver-1.3.0rc1/mlserver/registry.py`

 * *Files 6% similar despite different names*

```diff
@@ -5,14 +5,15 @@
 from functools import cmp_to_key
 
 from .model import MLModel
 from .errors import ModelNotFound
 from .logging import logger
 from .settings import ModelSettings
 
+ModelInitialiser = Callable[[ModelSettings], MLModel]
 ModelRegistryHook = Callable[[MLModel], Awaitable[MLModel]]
 ModelReloadHook = Callable[[MLModel, MLModel], Awaitable[MLModel]]
 
 
 def _get_version(model_settings: ModelSettings) -> Optional[str]:
     if model_settings.parameters:
         return model_settings.parameters.version
@@ -42,33 +43,40 @@
             return 1
         elif a.version < b.version:
             return -1
         else:
             return 0
 
 
+def model_initialiser(model_settings: ModelSettings) -> MLModel:
+    model_class = model_settings.implementation
+    return model_class(model_settings)  # type: ignore
+
+
 class SingleModelRegistry:
     """
     Registry for a single model with multiple versions.
     """
 
     def __init__(
         self,
         model_settings: ModelSettings,
         on_model_load: List[ModelRegistryHook] = [],
         on_model_reload: List[ModelReloadHook] = [],
         on_model_unload: List[ModelRegistryHook] = [],
+        model_initialiser: ModelInitialiser = model_initialiser,
     ):
         self._versions: Dict[str, MLModel] = {}
         self._default: Optional[MLModel] = None
 
         self._name = model_settings.name
         self._on_model_load = on_model_load
         self._on_model_reload = on_model_reload
         self._on_model_unload = on_model_unload
+        self._model_initialiser = model_initialiser
 
     @property
     def default(self) -> Optional[MLModel]:
         if self._default is None:
             self._default = self._find_default()
 
         return self._default
@@ -128,16 +136,15 @@
 
     async def load(self, model_settings: ModelSettings) -> MLModel:
         # If there's a previously loaded model, we'll need to unload it at the
         # end
         previous_version = _get_version(model_settings)
         previous_loaded_model = self._find_model(previous_version)
 
-        model_class = model_settings.implementation
-        new_model = model_class(model_settings)  # type: ignore
+        new_model = self._model_initialiser(model_settings)
 
         if previous_loaded_model:
             await self._reload_model(previous_loaded_model, new_model)
         else:
             await self._load_model(new_model)
 
         return new_model
@@ -151,15 +158,15 @@
             for callback in self._on_model_load:
                 # NOTE: Callbacks need to be executed sequentially to ensure that
                 # they go in the right order
                 model = await callback(model)
 
             # Register model again to ensure we save version modified by hooks
             self._register(model)
-            await model.load()
+            model.ready = await model.load()
 
             logger.info(f"Loaded model '{model.name}' succesfully.")
         except Exception:
             logger.info(
                 f"Couldn't load model '{model.name}'. "
                 "Model will be removed from registry."
             )
@@ -169,15 +176,15 @@
     async def _reload_model(self, old_model: MLModel, new_model: MLModel):
         for callback in self._on_model_reload:
             new_model = await callback(old_model, new_model)
 
         # Loading the model before unloading the old one - this will ensure
         # that at least one is available (sort of mimicking a rolling
         # deployment)
-        await new_model.load()
+        new_model.ready = await new_model.load()
         self._register(new_model)
 
         if old_model == self.default:
             self._clear_default()
 
         logger.info(f"Reloaded model '{new_model.name}' succesfully.")
 
@@ -261,27 +268,30 @@
     """
 
     def __init__(
         self,
         on_model_load: List[ModelRegistryHook] = [],
         on_model_reload: List[ModelReloadHook] = [],
         on_model_unload: List[ModelRegistryHook] = [],
+        model_initialiser: ModelInitialiser = model_initialiser,
     ):
         self._models: Dict[str, SingleModelRegistry] = {}
         self._on_model_load = on_model_load
         self._on_model_reload = on_model_reload
         self._on_model_unload = on_model_unload
+        self._model_initialiser = model_initialiser
 
     async def load(self, model_settings: ModelSettings) -> MLModel:
         if model_settings.name not in self._models:
             self._models[model_settings.name] = SingleModelRegistry(
                 model_settings,
                 on_model_load=self._on_model_load,
                 on_model_reload=self._on_model_reload,
                 on_model_unload=self._on_model_unload,
+                model_initialiser=self._model_initialiser,
             )
 
         return await self._models[model_settings.name].load(model_settings)
 
     async def unload(self, name: str):
         model_registry = self._get_model_registry(name)
         await model_registry.unload()
```

### Comparing `mlserver-1.3.0.dev4/mlserver/repository/factory.py` & `mlserver-1.3.0rc1/mlserver/repository/factory.py`

 * *Files identical despite different names*

### Comparing `mlserver-1.3.0.dev4/mlserver/repository/load.py` & `mlserver-1.3.0rc1/mlserver/repository/load.py`

 * *Files identical despite different names*

### Comparing `mlserver-1.3.0.dev4/mlserver/repository/repository.py` & `mlserver-1.3.0rc1/mlserver/repository/repository.py`

 * *Files identical despite different names*

### Comparing `mlserver-1.3.0.dev4/mlserver/rest/logging.py` & `mlserver-1.3.0rc1/mlserver/rest/logging.py`

 * *Files identical despite different names*

### Comparing `mlserver-1.3.0.dev4/mlserver/rest/requests.py` & `mlserver-1.3.0rc1/mlserver/rest/requests.py`

 * *Files identical despite different names*

### Comparing `mlserver-1.3.0.dev4/mlserver/rest/responses.py` & `mlserver-1.3.0rc1/mlserver/rest/responses.py`

 * *Files identical despite different names*

### Comparing `mlserver-1.3.0.dev4/mlserver/rest/server.py` & `mlserver-1.3.0rc1/mlserver/rest/server.py`

 * *Files identical despite different names*

### Comparing `mlserver-1.3.0.dev4/mlserver/rest/utils.py` & `mlserver-1.3.0rc1/mlserver/rest/utils.py`

 * *Files identical despite different names*

### Comparing `mlserver-1.3.0.dev4/mlserver/server.py` & `mlserver-1.3.0rc1/mlserver/server.py`

 * *Files 4% similar despite different names*

```diff
@@ -7,15 +7,15 @@
 from mlserver.repository.factory import ModelRepositoryFactory
 
 from .model import MLModel
 from .settings import Settings, ModelSettings
 from .logging import configure_logger
 from .registry import MultiModelRegistry
 from .handlers import DataPlane, ModelRepositoryHandlers
-from .parallel import InferencePool
+from .parallel import InferencePoolRegistry
 from .batching import load_batching
 from .rest import RESTServer
 from .grpc import GRPCServer
 from .metrics import MetricsServer
 from .kafka import KafkaServer
 from .utils import logger
 
@@ -27,22 +27,22 @@
         self._settings = settings
         self._add_signal_handlers()
 
         self._metrics_server = None
         if self._settings.metrics_endpoint:
             self._metrics_server = MetricsServer(self._settings)
 
-        self._inference_pool = None
+        self._inference_pool_registry = None
         if self._settings.parallel_workers:
             # Only load inference pool if parallel inference has been enabled
             on_worker_stop = []
             if self._metrics_server:
                 on_worker_stop = [self._metrics_server.on_worker_stop]
 
-            self._inference_pool = InferencePool(
+            self._inference_pool_registry = InferencePoolRegistry(
                 self._settings, on_worker_stop=on_worker_stop  # type: ignore
             )
 
         self._model_registry = self._create_model_registry()
         self._model_repository = ModelRepositoryFactory.resolve_model_repository(
             self._settings
         )
@@ -60,33 +60,40 @@
         on_model_load = [
             self.add_custom_handlers,
             load_batching,
         ]
         on_model_reload = [self.reload_custom_handlers]
         on_model_unload = [self.remove_custom_handlers]
 
-        if self._inference_pool:
-            on_model_load = [
-                self._inference_pool.load_model,
-                self.add_custom_handlers,
-                load_batching,
-            ]
-            on_model_reload = [
-                self._inference_pool.reload_model,  # type: ignore
-                self.reload_custom_handlers,
-            ]
-            on_model_unload = [
-                self._inference_pool.unload_model,  # type: ignore
-                self.remove_custom_handlers,
-            ]
+        if not self._inference_pool_registry:
+            return MultiModelRegistry(
+                on_model_load=on_model_load,  # type: ignore
+                on_model_reload=on_model_reload,  # type: ignore
+                on_model_unload=on_model_unload,  # type: ignore
+            )
+
+        on_model_load = [
+            self._inference_pool_registry.load_model,
+            self.add_custom_handlers,
+            load_batching,
+        ]
+        on_model_reload = [
+            self._inference_pool_registry.reload_model,  # type: ignore
+            self.reload_custom_handlers,
+        ]
+        on_model_unload = [
+            self._inference_pool_registry.unload_model,  # type: ignore
+            self.remove_custom_handlers,
+        ]
 
         return MultiModelRegistry(
             on_model_load=on_model_load,  # type: ignore
             on_model_reload=on_model_reload,  # type: ignore
             on_model_unload=on_model_unload,  # type: ignore
+            model_initialiser=self._inference_pool_registry.model_initialiser,
         )
 
     def _configure_logger(self):
         logger.setLevel(logging.INFO)
         if self._settings.debug:
             logger.setLevel(logging.DEBUG)
 
@@ -163,16 +170,16 @@
 
         for sig in HANDLED_SIGNALS:
             loop.add_signal_handler(
                 sig, lambda s=sig: asyncio.create_task(self.stop(sig=s))
             )
 
     async def stop(self, sig: Optional[int] = None):
-        if self._inference_pool:
-            await self._inference_pool.close()
+        if self._inference_pool_registry:
+            await self._inference_pool_registry.close()
 
         if self._kafka_server:
             await self._kafka_server.stop()
 
         if self._grpc_server:
             await self._grpc_server.stop(sig)
```

### Comparing `mlserver-1.3.0.dev4/mlserver/types/__init__.py` & `mlserver-1.3.0rc1/mlserver/types/__init__.py`

 * *Files identical despite different names*

### Comparing `mlserver-1.3.0.dev4/mlserver/types/base.py` & `mlserver-1.3.0rc1/mlserver/types/base.py`

 * *Files identical despite different names*

### Comparing `mlserver-1.3.0.dev4/mlserver/types/dataplane.py` & `mlserver-1.3.0rc1/mlserver/types/dataplane.py`

 * *Files identical despite different names*

### Comparing `mlserver-1.3.0.dev4/mlserver/types/model_repository.py` & `mlserver-1.3.0rc1/mlserver/types/model_repository.py`

 * *Files identical despite different names*

### Comparing `mlserver-1.3.0.dev4/mlserver/utils.py` & `mlserver-1.3.0rc1/mlserver/utils.py`

 * *Files 4% similar despite different names*

```diff
@@ -1,14 +1,14 @@
 import os
 import uuid
 import asyncio
 import urllib.parse
 
 from asyncio import Task
-from typing import Callable, Dict, Optional, List, Type
+from typing import Callable, Dict, Optional, List
 
 from .logging import logger
 from .types import InferenceRequest, InferenceResponse, Parameters
 from .settings import ModelSettings
 from .errors import InvalidModelURI
 
 
@@ -22,15 +22,15 @@
     if not model_uri:
         raise InvalidModelURI(settings.name)
 
     model_uri_components = urllib.parse.urlparse(model_uri, scheme="file")
     if model_uri_components.scheme != "file":
         return model_uri
 
-    full_model_path = _to_absolute_path(settings._source, model_uri_components.path)
+    full_model_path = to_absolute_path(settings, model_uri_components.path)
     if os.path.isfile(full_model_path):
         return full_model_path
 
     if os.path.isdir(full_model_path):
         # If full_model_path is a folder, search for a well-known model filename
         for fname in wellknown_filenames:
             model_path = os.path.join(full_model_path, fname)
@@ -40,22 +40,23 @@
         # If none, return the folder
         return full_model_path
 
     # Otherwise, the uri is neither a file nor a folder
     raise InvalidModelURI(settings.name, full_model_path)
 
 
-def _to_absolute_path(source: Optional[str], model_uri: str) -> str:
+def to_absolute_path(model_settings: ModelSettings, uri: str) -> str:
+    source = model_settings._source
     if source is None:
         # Treat path as either absolute or relative to the working directory of
         # the MLServer instance
-        return model_uri
+        return uri
 
     parent_folder = os.path.dirname(source)
-    unnormalised = os.path.join(parent_folder, model_uri)
+    unnormalised = os.path.join(parent_folder, uri)
     return os.path.normpath(unnormalised)
 
 
 def get_wrapped_method(f: Callable) -> Callable:
     while hasattr(f, "__wrapped__"):
         f = f.__wrapped__  # type: ignore
 
@@ -129,11 +130,7 @@
     logger.debug(f"Using asyncio event-loop policy: {policy}")
 
 
 def schedule_with_callback(coro, cb) -> Task:
     task = asyncio.create_task(coro)
     task.add_done_callback(cb)
     return task
-
-
-def get_import_path(klass: Type):
-    return f"{klass.__module__}.{klass.__name__}"
```

### Comparing `mlserver-1.3.0.dev4/mlserver.egg-info/PKG-INFO` & `mlserver-1.3.0rc1/mlserver.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: mlserver
-Version: 1.3.0.dev4
+Version: 1.3.0rc1
 Summary: ML server
 Home-page: https://github.com/SeldonIO/MLServer.git
 Author: Seldon Technologies Ltd.
 Author-email: hello@seldon.io
 License: Apache 2.0
 Description: # MLServer
```

### Comparing `mlserver-1.3.0.dev4/mlserver.egg-info/SOURCES.txt` & `mlserver-1.3.0rc1/mlserver.egg-info/SOURCES.txt`

 * *Files 7% similar despite different names*

```diff
@@ -1,8 +1,9 @@
 LICENSE
+MANIFEST.in
 README.md
 setup.cfg
 setup.py
 mlserver/__init__.py
 mlserver/batch_processing.py
 mlserver/cloudevents.py
 mlserver/env.py
@@ -76,26 +77,30 @@
 mlserver/parallel/__init__.py
 mlserver/parallel/dispatcher.py
 mlserver/parallel/errors.py
 mlserver/parallel/logging.py
 mlserver/parallel/messages.py
 mlserver/parallel/model.py
 mlserver/parallel/pool.py
+mlserver/parallel/registry.py
 mlserver/parallel/utils.py
 mlserver/parallel/worker.py
 mlserver/repository/__init__.py
 mlserver/repository/factory.py
 mlserver/repository/load.py
 mlserver/repository/repository.py
 mlserver/rest/__init__.py
 mlserver/rest/app.py
 mlserver/rest/endpoints.py
 mlserver/rest/errors.py
 mlserver/rest/logging.py
+mlserver/rest/openapi.py
 mlserver/rest/requests.py
 mlserver/rest/responses.py
 mlserver/rest/server.py
 mlserver/rest/utils.py
 mlserver/types/__init__.py
 mlserver/types/base.py
 mlserver/types/dataplane.py
-mlserver/types/model_repository.py
+mlserver/types/model_repository.py
+openapi/dataplane.json
+openapi/model_repository.json
```

### Comparing `mlserver-1.3.0.dev4/setup.cfg` & `mlserver-1.3.0rc1/setup.cfg`

 * *Files 5% similar despite different names*

```diff
@@ -116,23 +116,24 @@
 	-e{toxinidir}/runtimes/mllib
 	-e{toxinidir}/runtimes/lightgbm
 	-e{toxinidir}/runtimes/mlflow
 	-e{toxinidir}/runtimes/huggingface
 	-r{toxinidir}/requirements/dev.txt
 commands = 
 	pip install \
-	-e{toxinidir} \
 	-r{toxinidir}/runtimes/mlflow/requirements/dev.txt \
-	-r{toxinidir}/runtimes/alibi-explain/requirements/dev.txt
+	-r{toxinidir}/runtimes/alibi-explain/requirements/dev.txt \
+	-r{toxinidir}/runtimes/alibi-detect/requirements/dev.txt
+	pip install \
+	-e{toxinidir}
 	python -m pytest {posargs} \
 	{toxinidir}/tests \
 	{toxinidir}/runtimes/alibi-explain \
 	{toxinidir}/runtimes/alibi-detect \
 	{toxinidir}/runtimes/sklearn \
-	{toxinidir}/runtimes/sklearn \
 	{toxinidir}/runtimes/xgboost \
 	{toxinidir}/runtimes/mllib \
 	{toxinidir}/runtimes/lightgbm \
 	{toxinidir}/runtimes/mlflow \
 	{toxinidir}/runtimes/huggingface
 
 [testenv:licenses]
```

### Comparing `mlserver-1.3.0.dev4/setup.py` & `mlserver-1.3.0rc1/setup.py`

 * *Files 20% similar despite different names*

```diff
@@ -34,22 +34,26 @@
 setup(
     name=PKG_NAME,
     version=_load_version(),
     url="https://github.com/SeldonIO/MLServer.git",
     author="Seldon Technologies Ltd.",
     author_email="hello@seldon.io",
     description="ML server",
+    include_package_data=True,
     packages=find_packages(exclude=["tests", "tests.*"]),
     install_requires=[
         "click",
         # 0.89.0: https://github.com/tiangolo/fastapi/issues/5861
         "fastapi >=0.88.0, <=0.89.1, !=0.89.0",
         "python-dotenv",
         "grpcio",
-        "importlib-metadata;python_version<'3.8'",
+        # The importlib-resources backport is required to use some
+        # functionality added in Python 3.10
+        # https://setuptools.pypa.io/en/latest/userguide/datafiles.html#accessing-data-files-at-runtime
+        "importlib-resources",
         "numpy",
         "pandas",
         # Force patch for CVE-2022-1941
         # https://github.com/huggingface/optimum/issues/733
         "protobuf == 3.20.3",
         "uvicorn",
         "starlette_exporter",
```

