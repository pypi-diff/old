# Comparing `tmp/h2o-featurestore-0.9.1.tar.gz` & `tmp/h2o-featurestore-0.9.2.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "dist/h2o-featurestore-0.9.1.tar", last modified: Wed Oct  5 13:33:55 2022, max compression
+gzip compressed data, was "dist/h2o-featurestore-0.9.2.tar", last modified: Thu Oct  6 10:18:11 2022, max compression
```

## Comparing `h2o-featurestore-0.9.1.tar` & `h2o-featurestore-0.9.2.tar`

### file list

```diff
@@ -1,97 +1,97 @@
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-10-05 13:33:55.960181 h2o-featurestore-0.9.1/
--rw-r--r--   0 root         (0) root         (0)      151 2022-10-05 08:57:48.000000 h2o-featurestore-0.9.1/MANIFEST.in
--rw-r--r--   0 root         (0) root         (0)     1297 2022-10-05 13:33:55.960181 h2o-featurestore-0.9.1/PKG-INFO
--rw-r--r--   0 root         (0) root         (0)      546 2022-10-05 08:57:48.000000 h2o-featurestore-0.9.1/README.md
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-10-05 13:33:55.952181 h2o-featurestore-0.9.1/ai/
--rw-r--r--   0 root         (0) root         (0)        0 2022-10-05 08:57:48.000000 h2o-featurestore-0.9.1/ai/__init__.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-10-05 13:33:55.952181 h2o-featurestore-0.9.1/ai/h2o/
--rw-r--r--   0 root         (0) root         (0)        0 2022-10-05 08:57:48.000000 h2o-featurestore-0.9.1/ai/h2o/__init__.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-10-05 13:33:55.952181 h2o-featurestore-0.9.1/ai/h2o/featurestore/
--rw-r--r--   0 root         (0) root         (0)        0 2022-10-05 08:57:48.000000 h2o-featurestore-0.9.1/ai/h2o/featurestore/__init__.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-10-05 13:33:55.952181 h2o-featurestore-0.9.1/ai/h2o/featurestore/api/
--rw-r--r--   0 root         (0) root         (0)        0 2022-10-05 08:57:48.000000 h2o-featurestore-0.9.1/ai/h2o/featurestore/api/__init__.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-10-05 13:33:55.956181 h2o-featurestore-0.9.1/ai/h2o/featurestore/api/v1/
--rw-r--r--   0 root         (0) root         (0)   538747 2022-10-05 08:57:48.000000 h2o-featurestore-0.9.1/ai/h2o/featurestore/api/v1/CoreService_pb2.py
--rw-r--r--   0 root         (0) root         (0)   228828 2022-10-05 08:57:48.000000 h2o-featurestore-0.9.1/ai/h2o/featurestore/api/v1/CoreService_pb2_grpc.py
--rw-r--r--   0 root         (0) root         (0)     3422 2022-10-05 08:57:48.000000 h2o-featurestore-0.9.1/ai/h2o/featurestore/api/v1/DashboardApi_pb2.py
--rw-r--r--   0 root         (0) root         (0)      159 2022-10-05 08:57:48.000000 h2o-featurestore-0.9.1/ai/h2o/featurestore/api/v1/DashboardApi_pb2_grpc.py
--rw-r--r--   0 root         (0) root         (0)     4510 2022-10-05 08:57:48.000000 h2o-featurestore-0.9.1/ai/h2o/featurestore/api/v1/Events_pb2.py
--rw-r--r--   0 root         (0) root         (0)      159 2022-10-05 08:57:48.000000 h2o-featurestore-0.9.1/ai/h2o/featurestore/api/v1/Events_pb2_grpc.py
--rw-r--r--   0 root         (0) root         (0)     8950 2022-10-05 08:57:48.000000 h2o-featurestore-0.9.1/ai/h2o/featurestore/api/v1/FeatureSetProtoApi_pb2.py
--rw-r--r--   0 root         (0) root         (0)      159 2022-10-05 08:57:48.000000 h2o-featurestore-0.9.1/ai/h2o/featurestore/api/v1/FeatureSetProtoApi_pb2_grpc.py
--rw-r--r--   0 root         (0) root         (0)    18321 2022-10-05 08:57:48.000000 h2o-featurestore-0.9.1/ai/h2o/featurestore/api/v1/FeatureSetSearch_pb2.py
--rw-r--r--   0 root         (0) root         (0)      159 2022-10-05 08:57:48.000000 h2o-featurestore-0.9.1/ai/h2o/featurestore/api/v1/FeatureSetSearch_pb2_grpc.py
--rw-r--r--   0 root         (0) root         (0)     6869 2022-10-05 08:57:48.000000 h2o-featurestore-0.9.1/ai/h2o/featurestore/api/v1/OnlineApi_pb2.py
--rw-r--r--   0 root         (0) root         (0)      159 2022-10-05 08:57:48.000000 h2o-featurestore-0.9.1/ai/h2o/featurestore/api/v1/OnlineApi_pb2_grpc.py
--rw-r--r--   0 root         (0) root         (0)    18695 2022-10-05 08:57:48.000000 h2o-featurestore-0.9.1/ai/h2o/featurestore/api/v1/RecommendationProtoApi_pb2.py
--rw-r--r--   0 root         (0) root         (0)      159 2022-10-05 08:57:48.000000 h2o-featurestore-0.9.1/ai/h2o/featurestore/api/v1/RecommendationProtoApi_pb2_grpc.py
--rw-r--r--   0 root         (0) root         (0)     8357 2022-10-05 08:57:48.000000 h2o-featurestore-0.9.1/ai/h2o/featurestore/api/v1/TimeToLiveApi_pb2.py
--rw-r--r--   0 root         (0) root         (0)      159 2022-10-05 08:57:48.000000 h2o-featurestore-0.9.1/ai/h2o/featurestore/api/v1/TimeToLiveApi_pb2_grpc.py
--rw-r--r--   0 root         (0) root         (0)        0 2022-10-05 08:57:48.000000 h2o-featurestore-0.9.1/ai/h2o/featurestore/api/v1/__init__.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-10-05 13:33:55.956181 h2o-featurestore-0.9.1/featurestore/
--rw-r--r--   0 root         (0) root         (0)     1874 2022-10-05 08:57:48.000000 h2o-featurestore-0.9.1/featurestore/__init__.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-10-05 13:33:55.956181 h2o-featurestore-0.9.1/featurestore/_credentials/
--rw-r--r--   0 root         (0) root         (0)   264440 2022-10-05 08:57:48.000000 h2o-featurestore-0.9.1/featurestore/_credentials/roots.pem
--rw-r--r--   0 root         (0) root         (0)     7647 2022-10-05 08:57:48.000000 h2o-featurestore-0.9.1/featurestore/client.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-10-05 13:33:55.956181 h2o-featurestore-0.9.1/featurestore/core/
--rw-r--r--   0 root         (0) root         (0)       55 2022-10-05 08:57:48.000000 h2o-featurestore-0.9.1/featurestore/core/__init__.py
--rw-r--r--   0 root         (0) root         (0)     4946 2022-10-05 08:57:48.000000 h2o-featurestore-0.9.1/featurestore/core/auth.py
--rw-r--r--   0 root         (0) root         (0)      175 2022-10-05 08:57:48.000000 h2o-featurestore-0.9.1/featurestore/core/client_config.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-10-05 13:33:55.956181 h2o-featurestore-0.9.1/featurestore/core/collections/
--rw-r--r--   0 root         (0) root         (0)        0 2022-10-05 08:57:48.000000 h2o-featurestore-0.9.1/featurestore/core/collections/__init__.py
--rw-r--r--   0 root         (0) root         (0)     4946 2022-10-05 08:57:48.000000 h2o-featurestore-0.9.1/featurestore/core/collections/classifiers.py
--rw-r--r--   0 root         (0) root         (0)     4386 2022-10-05 08:57:48.000000 h2o-featurestore-0.9.1/featurestore/core/collections/feature_sets.py
--rw-r--r--   0 root         (0) root         (0)     1600 2022-10-05 08:57:48.000000 h2o-featurestore-0.9.1/featurestore/core/collections/ingest_history.py
--rw-r--r--   0 root         (0) root         (0)     2123 2022-10-05 08:57:48.000000 h2o-featurestore-0.9.1/featurestore/core/collections/jobs.py
--rw-r--r--   0 root         (0) root         (0)     1973 2022-10-05 08:57:48.000000 h2o-featurestore-0.9.1/featurestore/core/collections/pats.py
--rw-r--r--   0 root         (0) root         (0)     2733 2022-10-05 08:57:48.000000 h2o-featurestore-0.9.1/featurestore/core/collections/projects.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-10-05 13:33:55.956181 h2o-featurestore-0.9.1/featurestore/core/commons/
--rw-r--r--   0 root         (0) root         (0)        0 2022-10-05 08:57:48.000000 h2o-featurestore-0.9.1/featurestore/core/commons/__init__.py
--rw-r--r--   0 root         (0) root         (0)      917 2022-10-05 08:57:48.000000 h2o-featurestore-0.9.1/featurestore/core/commons/spark_utils.py
--rw-r--r--   0 root         (0) root         (0)     1880 2022-10-05 08:57:48.000000 h2o-featurestore-0.9.1/featurestore/core/config.py
--rw-r--r--   0 root         (0) root         (0)     9802 2022-10-05 08:57:48.000000 h2o-featurestore-0.9.1/featurestore/core/credentials.py
--rw-r--r--   0 root         (0) root         (0)    11562 2022-10-05 08:57:48.000000 h2o-featurestore-0.9.1/featurestore/core/data_source_wrappers.py
--rw-r--r--   0 root         (0) root         (0)      807 2022-10-05 08:57:48.000000 h2o-featurestore-0.9.1/featurestore/core/data_types.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-10-05 13:33:55.960181 h2o-featurestore-0.9.1/featurestore/core/entities/
--rw-r--r--   0 root         (0) root         (0)        0 2022-10-05 08:57:48.000000 h2o-featurestore-0.9.1/featurestore/core/entities/__init__.py
--rw-r--r--   0 root         (0) root         (0)     1842 2022-10-05 08:57:48.000000 h2o-featurestore-0.9.1/featurestore/core/entities/base_job.py
--rw-r--r--   0 root         (0) root         (0)      196 2022-10-05 08:57:48.000000 h2o-featurestore-0.9.1/featurestore/core/entities/compute_recommendation_classifiers_job.py
--rw-r--r--   0 root         (0) root         (0)      166 2022-10-05 08:57:48.000000 h2o-featurestore-0.9.1/featurestore/core/entities/compute_statistics_job.py
--rw-r--r--   0 root         (0) root         (0)     1220 2022-10-05 08:57:48.000000 h2o-featurestore-0.9.1/featurestore/core/entities/extract_schema_job.py
--rw-r--r--   0 root         (0) root         (0)     9920 2022-10-05 08:57:48.000000 h2o-featurestore-0.9.1/featurestore/core/entities/feature.py
--rw-r--r--   0 root         (0) root         (0)    25612 2022-10-05 08:57:48.000000 h2o-featurestore-0.9.1/featurestore/core/entities/feature_set.py
--rw-r--r--   0 root         (0) root         (0)     2300 2022-10-05 08:57:48.000000 h2o-featurestore-0.9.1/featurestore/core/entities/feature_set_schema.py
--rw-r--r--   0 root         (0) root         (0)     1221 2022-10-05 08:57:48.000000 h2o-featurestore-0.9.1/featurestore/core/entities/ingest.py
--rw-r--r--   0 root         (0) root         (0)      500 2022-10-05 08:57:48.000000 h2o-featurestore-0.9.1/featurestore/core/entities/ingest_job.py
--rw-r--r--   0 root         (0) root         (0)      722 2022-10-05 08:57:48.000000 h2o-featurestore-0.9.1/featurestore/core/entities/materialization_online_job.py
--rw-r--r--   0 root         (0) root         (0)      935 2022-10-05 08:57:48.000000 h2o-featurestore-0.9.1/featurestore/core/entities/pat.py
--rw-r--r--   0 root         (0) root         (0)     4634 2022-10-05 08:57:48.000000 h2o-featurestore-0.9.1/featurestore/core/entities/project.py
--rw-r--r--   0 root         (0) root         (0)      842 2022-10-05 08:57:48.000000 h2o-featurestore-0.9.1/featurestore/core/entities/recommendation.py
--rw-r--r--   0 root         (0) root         (0)      655 2022-10-05 08:57:48.000000 h2o-featurestore-0.9.1/featurestore/core/entities/retrieve_job.py
--rw-r--r--   0 root         (0) root         (0)      156 2022-10-05 08:57:48.000000 h2o-featurestore-0.9.1/featurestore/core/entities/revert_ingest_job.py
--rw-r--r--   0 root         (0) root         (0)      369 2022-10-05 08:57:48.000000 h2o-featurestore-0.9.1/featurestore/core/entities/user.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-10-05 13:33:55.960181 h2o-featurestore-0.9.1/featurestore/core/filter/
--rw-r--r--   0 root         (0) root         (0)       67 2022-10-05 08:57:48.000000 h2o-featurestore-0.9.1/featurestore/core/filter/__init__.py
--rw-r--r--   0 root         (0) root         (0)     5156 2022-10-05 08:57:48.000000 h2o-featurestore-0.9.1/featurestore/core/filter/base.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-10-05 13:33:55.960181 h2o-featurestore-0.9.1/featurestore/core/filter/collections/
--rw-r--r--   0 root         (0) root         (0)       65 2022-10-05 08:57:48.000000 h2o-featurestore-0.9.1/featurestore/core/filter/collections/__init__.py
--rw-r--r--   0 root         (0) root         (0)      412 2022-10-05 08:57:48.000000 h2o-featurestore-0.9.1/featurestore/core/filter/collections/feature.py
--rw-r--r--   0 root         (0) root         (0)      523 2022-10-05 08:57:48.000000 h2o-featurestore-0.9.1/featurestore/core/filter/collections/feature_set.py
--rw-r--r--   0 root         (0) root         (0)      698 2022-10-05 08:57:48.000000 h2o-featurestore-0.9.1/featurestore/core/interactive_console.py
--rw-r--r--   0 root         (0) root         (0)     4543 2022-10-05 08:57:48.000000 h2o-featurestore-0.9.1/featurestore/core/interceptors.py
--rw-r--r--   0 root         (0) root         (0)     1395 2022-10-05 08:57:48.000000 h2o-featurestore-0.9.1/featurestore/core/job_info.py
--rw-r--r--   0 root         (0) root         (0)      385 2022-10-05 08:57:48.000000 h2o-featurestore-0.9.1/featurestore/core/job_types.py
--rw-r--r--   0 root         (0) root         (0)     7340 2022-10-05 08:57:48.000000 h2o-featurestore-0.9.1/featurestore/core/retrieve_holder.py
--rw-r--r--   0 root         (0) root         (0)    13371 2022-10-05 08:57:48.000000 h2o-featurestore-0.9.1/featurestore/core/schema.py
--rw-r--r--   0 root         (0) root         (0)     5469 2022-10-05 08:57:48.000000 h2o-featurestore-0.9.1/featurestore/core/transformations.py
--rw-r--r--   0 root         (0) root         (0)     1238 2022-10-05 08:57:48.000000 h2o-featurestore-0.9.1/featurestore/core/user_credentials.py
--rw-r--r--   0 root         (0) root         (0)     1112 2022-10-05 08:57:48.000000 h2o-featurestore-0.9.1/featurestore/core/utils.py
--rw-r--r--   0 root         (0) root         (0)        5 2022-10-05 08:57:48.000000 h2o-featurestore-0.9.1/featurestore/version.txt
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-10-05 13:33:55.960181 h2o-featurestore-0.9.1/h2o_featurestore.egg-info/
--rw-r--r--   0 root         (0) root         (0)     1297 2022-10-05 13:33:55.000000 h2o-featurestore-0.9.1/h2o_featurestore.egg-info/PKG-INFO
--rw-r--r--   0 root         (0) root         (0)     3185 2022-10-05 13:33:55.000000 h2o-featurestore-0.9.1/h2o_featurestore.egg-info/SOURCES.txt
--rw-r--r--   0 root         (0) root         (0)        1 2022-10-05 13:33:55.000000 h2o-featurestore-0.9.1/h2o_featurestore.egg-info/dependency_links.txt
--rw-r--r--   0 root         (0) root         (0)      148 2022-10-05 13:33:55.000000 h2o-featurestore-0.9.1/h2o_featurestore.egg-info/requires.txt
--rw-r--r--   0 root         (0) root         (0)       16 2022-10-05 13:33:55.000000 h2o-featurestore-0.9.1/h2o_featurestore.egg-info/top_level.txt
--rw-r--r--   0 root         (0) root         (0)       67 2022-10-05 13:33:55.964181 h2o-featurestore-0.9.1/setup.cfg
--rw-r--r--   0 root         (0) root         (0)     1638 2022-10-05 08:57:48.000000 h2o-featurestore-0.9.1/setup.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2022-10-06 10:18:11.491231 h2o-featurestore-0.9.2/
+-rw-r--r--   0 root         (0) root         (0)      151 2022-10-06 09:31:00.000000 h2o-featurestore-0.9.2/MANIFEST.in
+-rw-r--r--   0 root         (0) root         (0)     1297 2022-10-06 10:18:11.491231 h2o-featurestore-0.9.2/PKG-INFO
+-rw-r--r--   0 root         (0) root         (0)      546 2022-10-06 09:31:00.000000 h2o-featurestore-0.9.2/README.md
+drwxr-xr-x   0 root         (0) root         (0)        0 2022-10-06 10:18:11.479231 h2o-featurestore-0.9.2/ai/
+-rw-r--r--   0 root         (0) root         (0)        0 2022-10-06 09:31:00.000000 h2o-featurestore-0.9.2/ai/__init__.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2022-10-06 10:18:11.483231 h2o-featurestore-0.9.2/ai/h2o/
+-rw-r--r--   0 root         (0) root         (0)        0 2022-10-06 09:31:00.000000 h2o-featurestore-0.9.2/ai/h2o/__init__.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2022-10-06 10:18:11.483231 h2o-featurestore-0.9.2/ai/h2o/featurestore/
+-rw-r--r--   0 root         (0) root         (0)        0 2022-10-06 09:31:00.000000 h2o-featurestore-0.9.2/ai/h2o/featurestore/__init__.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2022-10-06 10:18:11.483231 h2o-featurestore-0.9.2/ai/h2o/featurestore/api/
+-rw-r--r--   0 root         (0) root         (0)        0 2022-10-06 09:31:00.000000 h2o-featurestore-0.9.2/ai/h2o/featurestore/api/__init__.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2022-10-06 10:18:11.483231 h2o-featurestore-0.9.2/ai/h2o/featurestore/api/v1/
+-rw-r--r--   0 root         (0) root         (0)   538747 2022-10-06 09:31:00.000000 h2o-featurestore-0.9.2/ai/h2o/featurestore/api/v1/CoreService_pb2.py
+-rw-r--r--   0 root         (0) root         (0)   228828 2022-10-06 09:31:00.000000 h2o-featurestore-0.9.2/ai/h2o/featurestore/api/v1/CoreService_pb2_grpc.py
+-rw-r--r--   0 root         (0) root         (0)     3422 2022-10-06 09:31:00.000000 h2o-featurestore-0.9.2/ai/h2o/featurestore/api/v1/DashboardApi_pb2.py
+-rw-r--r--   0 root         (0) root         (0)      159 2022-10-06 09:31:00.000000 h2o-featurestore-0.9.2/ai/h2o/featurestore/api/v1/DashboardApi_pb2_grpc.py
+-rw-r--r--   0 root         (0) root         (0)     4510 2022-10-06 09:31:00.000000 h2o-featurestore-0.9.2/ai/h2o/featurestore/api/v1/Events_pb2.py
+-rw-r--r--   0 root         (0) root         (0)      159 2022-10-06 09:31:00.000000 h2o-featurestore-0.9.2/ai/h2o/featurestore/api/v1/Events_pb2_grpc.py
+-rw-r--r--   0 root         (0) root         (0)     8950 2022-10-06 09:31:00.000000 h2o-featurestore-0.9.2/ai/h2o/featurestore/api/v1/FeatureSetProtoApi_pb2.py
+-rw-r--r--   0 root         (0) root         (0)      159 2022-10-06 09:31:00.000000 h2o-featurestore-0.9.2/ai/h2o/featurestore/api/v1/FeatureSetProtoApi_pb2_grpc.py
+-rw-r--r--   0 root         (0) root         (0)    18321 2022-10-06 09:31:00.000000 h2o-featurestore-0.9.2/ai/h2o/featurestore/api/v1/FeatureSetSearch_pb2.py
+-rw-r--r--   0 root         (0) root         (0)      159 2022-10-06 09:31:00.000000 h2o-featurestore-0.9.2/ai/h2o/featurestore/api/v1/FeatureSetSearch_pb2_grpc.py
+-rw-r--r--   0 root         (0) root         (0)     6869 2022-10-06 09:31:00.000000 h2o-featurestore-0.9.2/ai/h2o/featurestore/api/v1/OnlineApi_pb2.py
+-rw-r--r--   0 root         (0) root         (0)      159 2022-10-06 09:31:00.000000 h2o-featurestore-0.9.2/ai/h2o/featurestore/api/v1/OnlineApi_pb2_grpc.py
+-rw-r--r--   0 root         (0) root         (0)    18695 2022-10-06 09:31:00.000000 h2o-featurestore-0.9.2/ai/h2o/featurestore/api/v1/RecommendationProtoApi_pb2.py
+-rw-r--r--   0 root         (0) root         (0)      159 2022-10-06 09:31:00.000000 h2o-featurestore-0.9.2/ai/h2o/featurestore/api/v1/RecommendationProtoApi_pb2_grpc.py
+-rw-r--r--   0 root         (0) root         (0)     8357 2022-10-06 09:31:00.000000 h2o-featurestore-0.9.2/ai/h2o/featurestore/api/v1/TimeToLiveApi_pb2.py
+-rw-r--r--   0 root         (0) root         (0)      159 2022-10-06 09:31:00.000000 h2o-featurestore-0.9.2/ai/h2o/featurestore/api/v1/TimeToLiveApi_pb2_grpc.py
+-rw-r--r--   0 root         (0) root         (0)        0 2022-10-06 09:31:00.000000 h2o-featurestore-0.9.2/ai/h2o/featurestore/api/v1/__init__.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2022-10-06 10:18:11.483231 h2o-featurestore-0.9.2/featurestore/
+-rw-r--r--   0 root         (0) root         (0)     1874 2022-10-06 09:31:00.000000 h2o-featurestore-0.9.2/featurestore/__init__.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2022-10-06 10:18:11.483231 h2o-featurestore-0.9.2/featurestore/_credentials/
+-rw-r--r--   0 root         (0) root         (0)   264440 2022-10-06 09:31:00.000000 h2o-featurestore-0.9.2/featurestore/_credentials/roots.pem
+-rw-r--r--   0 root         (0) root         (0)     7647 2022-10-06 09:31:00.000000 h2o-featurestore-0.9.2/featurestore/client.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2022-10-06 10:18:11.487231 h2o-featurestore-0.9.2/featurestore/core/
+-rw-r--r--   0 root         (0) root         (0)       55 2022-10-06 09:31:00.000000 h2o-featurestore-0.9.2/featurestore/core/__init__.py
+-rw-r--r--   0 root         (0) root         (0)     4946 2022-10-06 09:31:00.000000 h2o-featurestore-0.9.2/featurestore/core/auth.py
+-rw-r--r--   0 root         (0) root         (0)      175 2022-10-06 09:31:00.000000 h2o-featurestore-0.9.2/featurestore/core/client_config.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2022-10-06 10:18:11.487231 h2o-featurestore-0.9.2/featurestore/core/collections/
+-rw-r--r--   0 root         (0) root         (0)        0 2022-10-06 09:31:00.000000 h2o-featurestore-0.9.2/featurestore/core/collections/__init__.py
+-rw-r--r--   0 root         (0) root         (0)     4946 2022-10-06 09:31:00.000000 h2o-featurestore-0.9.2/featurestore/core/collections/classifiers.py
+-rw-r--r--   0 root         (0) root         (0)     4386 2022-10-06 09:31:00.000000 h2o-featurestore-0.9.2/featurestore/core/collections/feature_sets.py
+-rw-r--r--   0 root         (0) root         (0)     1600 2022-10-06 09:31:00.000000 h2o-featurestore-0.9.2/featurestore/core/collections/ingest_history.py
+-rw-r--r--   0 root         (0) root         (0)     2123 2022-10-06 09:31:00.000000 h2o-featurestore-0.9.2/featurestore/core/collections/jobs.py
+-rw-r--r--   0 root         (0) root         (0)     1973 2022-10-06 09:31:00.000000 h2o-featurestore-0.9.2/featurestore/core/collections/pats.py
+-rw-r--r--   0 root         (0) root         (0)     2733 2022-10-06 09:31:00.000000 h2o-featurestore-0.9.2/featurestore/core/collections/projects.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2022-10-06 10:18:11.487231 h2o-featurestore-0.9.2/featurestore/core/commons/
+-rw-r--r--   0 root         (0) root         (0)        0 2022-10-06 09:31:00.000000 h2o-featurestore-0.9.2/featurestore/core/commons/__init__.py
+-rw-r--r--   0 root         (0) root         (0)      917 2022-10-06 09:31:00.000000 h2o-featurestore-0.9.2/featurestore/core/commons/spark_utils.py
+-rw-r--r--   0 root         (0) root         (0)     1880 2022-10-06 09:31:00.000000 h2o-featurestore-0.9.2/featurestore/core/config.py
+-rw-r--r--   0 root         (0) root         (0)     9802 2022-10-06 09:31:00.000000 h2o-featurestore-0.9.2/featurestore/core/credentials.py
+-rw-r--r--   0 root         (0) root         (0)    11562 2022-10-06 09:31:00.000000 h2o-featurestore-0.9.2/featurestore/core/data_source_wrappers.py
+-rw-r--r--   0 root         (0) root         (0)      807 2022-10-06 09:31:00.000000 h2o-featurestore-0.9.2/featurestore/core/data_types.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2022-10-06 10:18:11.487231 h2o-featurestore-0.9.2/featurestore/core/entities/
+-rw-r--r--   0 root         (0) root         (0)        0 2022-10-06 09:31:00.000000 h2o-featurestore-0.9.2/featurestore/core/entities/__init__.py
+-rw-r--r--   0 root         (0) root         (0)     1842 2022-10-06 09:31:00.000000 h2o-featurestore-0.9.2/featurestore/core/entities/base_job.py
+-rw-r--r--   0 root         (0) root         (0)      196 2022-10-06 09:31:00.000000 h2o-featurestore-0.9.2/featurestore/core/entities/compute_recommendation_classifiers_job.py
+-rw-r--r--   0 root         (0) root         (0)      166 2022-10-06 09:31:00.000000 h2o-featurestore-0.9.2/featurestore/core/entities/compute_statistics_job.py
+-rw-r--r--   0 root         (0) root         (0)     1220 2022-10-06 09:31:00.000000 h2o-featurestore-0.9.2/featurestore/core/entities/extract_schema_job.py
+-rw-r--r--   0 root         (0) root         (0)     9920 2022-10-06 09:31:00.000000 h2o-featurestore-0.9.2/featurestore/core/entities/feature.py
+-rw-r--r--   0 root         (0) root         (0)    25612 2022-10-06 09:31:00.000000 h2o-featurestore-0.9.2/featurestore/core/entities/feature_set.py
+-rw-r--r--   0 root         (0) root         (0)     2300 2022-10-06 09:31:00.000000 h2o-featurestore-0.9.2/featurestore/core/entities/feature_set_schema.py
+-rw-r--r--   0 root         (0) root         (0)     1221 2022-10-06 09:31:00.000000 h2o-featurestore-0.9.2/featurestore/core/entities/ingest.py
+-rw-r--r--   0 root         (0) root         (0)      500 2022-10-06 09:31:00.000000 h2o-featurestore-0.9.2/featurestore/core/entities/ingest_job.py
+-rw-r--r--   0 root         (0) root         (0)      722 2022-10-06 09:31:00.000000 h2o-featurestore-0.9.2/featurestore/core/entities/materialization_online_job.py
+-rw-r--r--   0 root         (0) root         (0)      935 2022-10-06 09:31:00.000000 h2o-featurestore-0.9.2/featurestore/core/entities/pat.py
+-rw-r--r--   0 root         (0) root         (0)     4634 2022-10-06 09:31:00.000000 h2o-featurestore-0.9.2/featurestore/core/entities/project.py
+-rw-r--r--   0 root         (0) root         (0)      842 2022-10-06 09:31:00.000000 h2o-featurestore-0.9.2/featurestore/core/entities/recommendation.py
+-rw-r--r--   0 root         (0) root         (0)      655 2022-10-06 09:31:00.000000 h2o-featurestore-0.9.2/featurestore/core/entities/retrieve_job.py
+-rw-r--r--   0 root         (0) root         (0)      156 2022-10-06 09:31:00.000000 h2o-featurestore-0.9.2/featurestore/core/entities/revert_ingest_job.py
+-rw-r--r--   0 root         (0) root         (0)      369 2022-10-06 09:31:00.000000 h2o-featurestore-0.9.2/featurestore/core/entities/user.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2022-10-06 10:18:11.491231 h2o-featurestore-0.9.2/featurestore/core/filter/
+-rw-r--r--   0 root         (0) root         (0)       67 2022-10-06 09:31:00.000000 h2o-featurestore-0.9.2/featurestore/core/filter/__init__.py
+-rw-r--r--   0 root         (0) root         (0)     5156 2022-10-06 09:31:00.000000 h2o-featurestore-0.9.2/featurestore/core/filter/base.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2022-10-06 10:18:11.491231 h2o-featurestore-0.9.2/featurestore/core/filter/collections/
+-rw-r--r--   0 root         (0) root         (0)       65 2022-10-06 09:31:00.000000 h2o-featurestore-0.9.2/featurestore/core/filter/collections/__init__.py
+-rw-r--r--   0 root         (0) root         (0)      412 2022-10-06 09:31:00.000000 h2o-featurestore-0.9.2/featurestore/core/filter/collections/feature.py
+-rw-r--r--   0 root         (0) root         (0)      523 2022-10-06 09:31:00.000000 h2o-featurestore-0.9.2/featurestore/core/filter/collections/feature_set.py
+-rw-r--r--   0 root         (0) root         (0)      698 2022-10-06 09:31:00.000000 h2o-featurestore-0.9.2/featurestore/core/interactive_console.py
+-rw-r--r--   0 root         (0) root         (0)     4543 2022-10-06 09:31:00.000000 h2o-featurestore-0.9.2/featurestore/core/interceptors.py
+-rw-r--r--   0 root         (0) root         (0)     1395 2022-10-06 09:31:00.000000 h2o-featurestore-0.9.2/featurestore/core/job_info.py
+-rw-r--r--   0 root         (0) root         (0)      385 2022-10-06 09:31:00.000000 h2o-featurestore-0.9.2/featurestore/core/job_types.py
+-rw-r--r--   0 root         (0) root         (0)     7340 2022-10-06 09:31:00.000000 h2o-featurestore-0.9.2/featurestore/core/retrieve_holder.py
+-rw-r--r--   0 root         (0) root         (0)    13371 2022-10-06 09:31:00.000000 h2o-featurestore-0.9.2/featurestore/core/schema.py
+-rw-r--r--   0 root         (0) root         (0)     5469 2022-10-06 09:31:00.000000 h2o-featurestore-0.9.2/featurestore/core/transformations.py
+-rw-r--r--   0 root         (0) root         (0)     1238 2022-10-06 09:31:00.000000 h2o-featurestore-0.9.2/featurestore/core/user_credentials.py
+-rw-r--r--   0 root         (0) root         (0)     1112 2022-10-06 09:31:00.000000 h2o-featurestore-0.9.2/featurestore/core/utils.py
+-rw-r--r--   0 root         (0) root         (0)        5 2022-10-06 09:31:00.000000 h2o-featurestore-0.9.2/featurestore/version.txt
+drwxr-xr-x   0 root         (0) root         (0)        0 2022-10-06 10:18:11.491231 h2o-featurestore-0.9.2/h2o_featurestore.egg-info/
+-rw-r--r--   0 root         (0) root         (0)     1297 2022-10-06 10:18:11.000000 h2o-featurestore-0.9.2/h2o_featurestore.egg-info/PKG-INFO
+-rw-r--r--   0 root         (0) root         (0)     3185 2022-10-06 10:18:11.000000 h2o-featurestore-0.9.2/h2o_featurestore.egg-info/SOURCES.txt
+-rw-r--r--   0 root         (0) root         (0)        1 2022-10-06 10:18:11.000000 h2o-featurestore-0.9.2/h2o_featurestore.egg-info/dependency_links.txt
+-rw-r--r--   0 root         (0) root         (0)      148 2022-10-06 10:18:11.000000 h2o-featurestore-0.9.2/h2o_featurestore.egg-info/requires.txt
+-rw-r--r--   0 root         (0) root         (0)       16 2022-10-06 10:18:11.000000 h2o-featurestore-0.9.2/h2o_featurestore.egg-info/top_level.txt
+-rw-r--r--   0 root         (0) root         (0)       67 2022-10-06 10:18:11.491231 h2o-featurestore-0.9.2/setup.cfg
+-rw-r--r--   0 root         (0) root         (0)     1638 2022-10-06 09:31:00.000000 h2o-featurestore-0.9.2/setup.py
```

### Comparing `h2o-featurestore-0.9.1/PKG-INFO` & `h2o-featurestore-0.9.2/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: h2o-featurestore
-Version: 0.9.1
+Version: 0.9.2
 Summary: Feature Store Client for Python
 Home-page: https://docs.h2o.ai/feature-store/latest-stable/docs/index.html
 Author: H2O.ai
 Author-email: support@h2o.ai
 License: Apache v2
 Download-URL: https://docs.h2o.ai/feature-store/latest-stable/docs/download.html
 Description: Feature Store Client
```

### Comparing `h2o-featurestore-0.9.1/README.md` & `h2o-featurestore-0.9.2/README.md`

 * *Files identical despite different names*

### Comparing `h2o-featurestore-0.9.1/ai/h2o/featurestore/api/v1/CoreService_pb2.py` & `h2o-featurestore-0.9.2/ai/h2o/featurestore/api/v1/CoreService_pb2.py`

 * *Files identical despite different names*

### Comparing `h2o-featurestore-0.9.1/ai/h2o/featurestore/api/v1/CoreService_pb2_grpc.py` & `h2o-featurestore-0.9.2/ai/h2o/featurestore/api/v1/CoreService_pb2_grpc.py`

 * *Files identical despite different names*

### Comparing `h2o-featurestore-0.9.1/ai/h2o/featurestore/api/v1/DashboardApi_pb2.py` & `h2o-featurestore-0.9.2/ai/h2o/featurestore/api/v1/DashboardApi_pb2.py`

 * *Files identical despite different names*

### Comparing `h2o-featurestore-0.9.1/ai/h2o/featurestore/api/v1/Events_pb2.py` & `h2o-featurestore-0.9.2/ai/h2o/featurestore/api/v1/Events_pb2.py`

 * *Files identical despite different names*

### Comparing `h2o-featurestore-0.9.1/ai/h2o/featurestore/api/v1/FeatureSetProtoApi_pb2.py` & `h2o-featurestore-0.9.2/ai/h2o/featurestore/api/v1/FeatureSetProtoApi_pb2.py`

 * *Files identical despite different names*

### Comparing `h2o-featurestore-0.9.1/ai/h2o/featurestore/api/v1/FeatureSetSearch_pb2.py` & `h2o-featurestore-0.9.2/ai/h2o/featurestore/api/v1/FeatureSetSearch_pb2.py`

 * *Files identical despite different names*

### Comparing `h2o-featurestore-0.9.1/ai/h2o/featurestore/api/v1/OnlineApi_pb2.py` & `h2o-featurestore-0.9.2/ai/h2o/featurestore/api/v1/OnlineApi_pb2.py`

 * *Files identical despite different names*

### Comparing `h2o-featurestore-0.9.1/ai/h2o/featurestore/api/v1/RecommendationProtoApi_pb2.py` & `h2o-featurestore-0.9.2/ai/h2o/featurestore/api/v1/RecommendationProtoApi_pb2.py`

 * *Files identical despite different names*

### Comparing `h2o-featurestore-0.9.1/ai/h2o/featurestore/api/v1/TimeToLiveApi_pb2.py` & `h2o-featurestore-0.9.2/ai/h2o/featurestore/api/v1/TimeToLiveApi_pb2.py`

 * *Files identical despite different names*

### Comparing `h2o-featurestore-0.9.1/featurestore/__init__.py` & `h2o-featurestore-0.9.2/featurestore/__init__.py`

 * *Files identical despite different names*

### Comparing `h2o-featurestore-0.9.1/featurestore/_credentials/roots.pem` & `h2o-featurestore-0.9.2/featurestore/_credentials/roots.pem`

 * *Files identical despite different names*

### Comparing `h2o-featurestore-0.9.1/featurestore/client.py` & `h2o-featurestore-0.9.2/featurestore/client.py`

 * *Files identical despite different names*

### Comparing `h2o-featurestore-0.9.1/featurestore/core/auth.py` & `h2o-featurestore-0.9.2/featurestore/core/auth.py`

 * *Files identical despite different names*

### Comparing `h2o-featurestore-0.9.1/featurestore/core/collections/classifiers.py` & `h2o-featurestore-0.9.2/featurestore/core/collections/classifiers.py`

 * *Files identical despite different names*

### Comparing `h2o-featurestore-0.9.1/featurestore/core/collections/feature_sets.py` & `h2o-featurestore-0.9.2/featurestore/core/collections/feature_sets.py`

 * *Files identical despite different names*

### Comparing `h2o-featurestore-0.9.1/featurestore/core/collections/ingest_history.py` & `h2o-featurestore-0.9.2/featurestore/core/collections/ingest_history.py`

 * *Files identical despite different names*

### Comparing `h2o-featurestore-0.9.1/featurestore/core/collections/jobs.py` & `h2o-featurestore-0.9.2/featurestore/core/collections/jobs.py`

 * *Files identical despite different names*

### Comparing `h2o-featurestore-0.9.1/featurestore/core/collections/pats.py` & `h2o-featurestore-0.9.2/featurestore/core/collections/pats.py`

 * *Files identical despite different names*

### Comparing `h2o-featurestore-0.9.1/featurestore/core/collections/projects.py` & `h2o-featurestore-0.9.2/featurestore/core/collections/projects.py`

 * *Files identical despite different names*

### Comparing `h2o-featurestore-0.9.1/featurestore/core/commons/spark_utils.py` & `h2o-featurestore-0.9.2/featurestore/core/commons/spark_utils.py`

 * *Files identical despite different names*

### Comparing `h2o-featurestore-0.9.1/featurestore/core/config.py` & `h2o-featurestore-0.9.2/featurestore/core/config.py`

 * *Files identical despite different names*

### Comparing `h2o-featurestore-0.9.1/featurestore/core/credentials.py` & `h2o-featurestore-0.9.2/featurestore/core/credentials.py`

 * *Files identical despite different names*

### Comparing `h2o-featurestore-0.9.1/featurestore/core/data_source_wrappers.py` & `h2o-featurestore-0.9.2/featurestore/core/data_source_wrappers.py`

 * *Files identical despite different names*

### Comparing `h2o-featurestore-0.9.1/featurestore/core/data_types.py` & `h2o-featurestore-0.9.2/featurestore/core/data_types.py`

 * *Files identical despite different names*

### Comparing `h2o-featurestore-0.9.1/featurestore/core/entities/base_job.py` & `h2o-featurestore-0.9.2/featurestore/core/entities/base_job.py`

 * *Files identical despite different names*

### Comparing `h2o-featurestore-0.9.1/featurestore/core/entities/extract_schema_job.py` & `h2o-featurestore-0.9.2/featurestore/core/entities/extract_schema_job.py`

 * *Files identical despite different names*

### Comparing `h2o-featurestore-0.9.1/featurestore/core/entities/feature.py` & `h2o-featurestore-0.9.2/featurestore/core/entities/feature.py`

 * *Files identical despite different names*

### Comparing `h2o-featurestore-0.9.1/featurestore/core/entities/feature_set.py` & `h2o-featurestore-0.9.2/featurestore/core/entities/feature_set.py`

 * *Files identical despite different names*

### Comparing `h2o-featurestore-0.9.1/featurestore/core/entities/feature_set_schema.py` & `h2o-featurestore-0.9.2/featurestore/core/entities/feature_set_schema.py`

 * *Files identical despite different names*

### Comparing `h2o-featurestore-0.9.1/featurestore/core/entities/ingest.py` & `h2o-featurestore-0.9.2/featurestore/core/entities/ingest.py`

 * *Files identical despite different names*

### Comparing `h2o-featurestore-0.9.1/featurestore/core/entities/materialization_online_job.py` & `h2o-featurestore-0.9.2/featurestore/core/entities/materialization_online_job.py`

 * *Files identical despite different names*

### Comparing `h2o-featurestore-0.9.1/featurestore/core/entities/pat.py` & `h2o-featurestore-0.9.2/featurestore/core/entities/pat.py`

 * *Files identical despite different names*

### Comparing `h2o-featurestore-0.9.1/featurestore/core/entities/project.py` & `h2o-featurestore-0.9.2/featurestore/core/entities/project.py`

 * *Files identical despite different names*

### Comparing `h2o-featurestore-0.9.1/featurestore/core/entities/recommendation.py` & `h2o-featurestore-0.9.2/featurestore/core/entities/recommendation.py`

 * *Files identical despite different names*

### Comparing `h2o-featurestore-0.9.1/featurestore/core/entities/retrieve_job.py` & `h2o-featurestore-0.9.2/featurestore/core/entities/retrieve_job.py`

 * *Files identical despite different names*

### Comparing `h2o-featurestore-0.9.1/featurestore/core/filter/base.py` & `h2o-featurestore-0.9.2/featurestore/core/filter/base.py`

 * *Files identical despite different names*

### Comparing `h2o-featurestore-0.9.1/featurestore/core/filter/collections/feature_set.py` & `h2o-featurestore-0.9.2/featurestore/core/filter/collections/feature_set.py`

 * *Files identical despite different names*

### Comparing `h2o-featurestore-0.9.1/featurestore/core/interactive_console.py` & `h2o-featurestore-0.9.2/featurestore/core/interactive_console.py`

 * *Files identical despite different names*

### Comparing `h2o-featurestore-0.9.1/featurestore/core/interceptors.py` & `h2o-featurestore-0.9.2/featurestore/core/interceptors.py`

 * *Files identical despite different names*

### Comparing `h2o-featurestore-0.9.1/featurestore/core/job_info.py` & `h2o-featurestore-0.9.2/featurestore/core/job_info.py`

 * *Files identical despite different names*

### Comparing `h2o-featurestore-0.9.1/featurestore/core/retrieve_holder.py` & `h2o-featurestore-0.9.2/featurestore/core/retrieve_holder.py`

 * *Files identical despite different names*

### Comparing `h2o-featurestore-0.9.1/featurestore/core/schema.py` & `h2o-featurestore-0.9.2/featurestore/core/schema.py`

 * *Files identical despite different names*

### Comparing `h2o-featurestore-0.9.1/featurestore/core/transformations.py` & `h2o-featurestore-0.9.2/featurestore/core/transformations.py`

 * *Files identical despite different names*

### Comparing `h2o-featurestore-0.9.1/featurestore/core/user_credentials.py` & `h2o-featurestore-0.9.2/featurestore/core/user_credentials.py`

 * *Files identical despite different names*

### Comparing `h2o-featurestore-0.9.1/featurestore/core/utils.py` & `h2o-featurestore-0.9.2/featurestore/core/utils.py`

 * *Files identical despite different names*

### Comparing `h2o-featurestore-0.9.1/h2o_featurestore.egg-info/PKG-INFO` & `h2o-featurestore-0.9.2/h2o_featurestore.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: h2o-featurestore
-Version: 0.9.1
+Version: 0.9.2
 Summary: Feature Store Client for Python
 Home-page: https://docs.h2o.ai/feature-store/latest-stable/docs/index.html
 Author: H2O.ai
 Author-email: support@h2o.ai
 License: Apache v2
 Download-URL: https://docs.h2o.ai/feature-store/latest-stable/docs/download.html
 Description: Feature Store Client
```

### Comparing `h2o-featurestore-0.9.1/h2o_featurestore.egg-info/SOURCES.txt` & `h2o-featurestore-0.9.2/h2o_featurestore.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `h2o-featurestore-0.9.1/setup.py` & `h2o-featurestore-0.9.2/setup.py`

 * *Files 1% similar despite different names*

```diff
@@ -7,15 +7,15 @@
 
 setup(
     name='h2o-featurestore',
 
     # Versions should comply with PEP440.  For a discussion on single-sourcing
     # the version across setup.py and the project code, see
     # https://packaging.python.org/en/latest/single_source_version.html
-    version="0.9.1",
+    version="0.9.2",
     description='Feature Store Client for Python',
     long_description=long_description,
     long_description_content_type='text/markdown',
     url='https://docs.h2o.ai/feature-store/latest-stable/docs/index.html',
     download_url='https://docs.h2o.ai/feature-store/latest-stable/docs/download.html',
     author='H2O.ai',
     author_email='support@h2o.ai',
```

