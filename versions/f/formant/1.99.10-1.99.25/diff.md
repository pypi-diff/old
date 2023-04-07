# Comparing `tmp/formant-1.99.10.tar.gz` & `tmp/formant-1.99.25.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "formant-1.99.10.tar", last modified: Fri Oct 28 01:56:00 2022, max compression
+gzip compressed data, was "formant-1.99.25.tar", last modified: Tue Nov  8 04:22:53 2022, max compression
```

## Comparing `formant-1.99.10.tar` & `formant-1.99.25.tar`

### file list

```diff
@@ -1,100 +1,100 @@
-drwxr-xr-x   0 runner    (1000) runner    (1000)        0 2022-10-28 01:56:00.670675 formant-1.99.10/
--rw-r--r--   0 runner    (1000) runner    (1000)      449 2022-10-28 01:56:00.670675 formant-1.99.10/PKG-INFO
--r-xr-xr-x   0 runner    (1000) runner    (1000)       23 2000-01-01 00:00:00.000000 formant-1.99.10/README.md
-drwxr-xr-x   0 runner    (1000) runner    (1000)        0 2022-10-28 01:56:00.666675 formant-1.99.10/formant/
--r-xr-xr-x   0 runner    (1000) runner    (1000)        0 2022-10-28 01:56:00.000000 formant-1.99.10/formant/__init__.py
-drwxr-xr-x   0 runner    (1000) runner    (1000)        0 2022-10-28 01:56:00.666675 formant-1.99.10/formant/protos/
--rwxr-xr-x   0 runner    (1000) runner    (1000)        0 2022-10-28 01:56:00.000000 formant-1.99.10/formant/protos/__init__.py
-drwxr-xr-x   0 runner    (1000) runner    (1000)        0 2022-10-28 01:56:00.666675 formant-1.99.10/formant/protos/agent/
--r-xr-xr-x   0 runner    (1000) runner    (1000)        0 2022-10-28 01:56:00.000000 formant-1.99.10/formant/protos/agent/__init__.py
-drwxr-xr-x   0 runner    (1000) runner    (1000)        0 2022-10-28 01:56:00.666675 formant-1.99.10/formant/protos/agent/v1/
--r-xr-xr-x   0 runner    (1000) runner    (1000)        0 2022-10-28 01:56:00.000000 formant-1.99.10/formant/protos/agent/v1/__init__.py
--r-xr-xr-x   0 runner    (1000) runner    (1000)    77876 2022-10-28 01:56:00.000000 formant-1.99.10/formant/protos/agent/v1/agent_pb2.py
--r-xr-xr-x   0 runner    (1000) runner    (1000)    45713 2022-10-28 01:56:00.000000 formant-1.99.10/formant/protos/agent/v1/agent_pb2_grpc.py
-drwxr-xr-x   0 runner    (1000) runner    (1000)        0 2022-10-28 01:56:00.666675 formant-1.99.10/formant/protos/api/
--rwxr-xr-x   0 runner    (1000) runner    (1000)        0 2022-10-28 01:56:00.000000 formant-1.99.10/formant/protos/api/__init__.py
-drwxr-xr-x   0 runner    (1000) runner    (1000)        0 2022-10-28 01:56:00.666675 formant-1.99.10/formant/protos/api/signaling/
--rwxr-xr-x   0 runner    (1000) runner    (1000)        0 2022-10-28 01:56:00.000000 formant-1.99.10/formant/protos/api/signaling/__init__.py
-drwxr-xr-x   0 runner    (1000) runner    (1000)        0 2022-10-28 01:56:00.666675 formant-1.99.10/formant/protos/model/
--rwxr-xr-x   0 runner    (1000) runner    (1000)        0 2022-10-28 01:56:00.000000 formant-1.99.10/formant/protos/model/__init__.py
-drwxr-xr-x   0 runner    (1000) runner    (1000)        0 2022-10-28 01:56:00.666675 formant-1.99.10/formant/protos/model/v1/
--r-xr-xr-x   0 runner    (1000) runner    (1000)        0 2022-10-28 01:56:00.000000 formant-1.99.10/formant/protos/model/v1/__init__.py
--r-xr-xr-x   0 runner    (1000) runner    (1000)    10369 2022-10-28 01:56:00.000000 formant-1.99.10/formant/protos/model/v1/commands_pb2.py
--r-xr-xr-x   0 runner    (1000) runner    (1000)      159 2022-10-28 01:56:00.000000 formant-1.99.10/formant/protos/model/v1/commands_pb2_grpc.py
--r-xr-xr-x   0 runner    (1000) runner    (1000)    91722 2022-10-28 01:56:00.000000 formant-1.99.10/formant/protos/model/v1/config_pb2.py
--r-xr-xr-x   0 runner    (1000) runner    (1000)      159 2022-10-28 01:56:00.000000 formant-1.99.10/formant/protos/model/v1/config_pb2_grpc.py
--r-xr-xr-x   0 runner    (1000) runner    (1000)    24653 2022-10-28 01:56:00.000000 formant-1.99.10/formant/protos/model/v1/datapoint_pb2.py
--r-xr-xr-x   0 runner    (1000) runner    (1000)      159 2022-10-28 01:56:00.000000 formant-1.99.10/formant/protos/model/v1/datapoint_pb2_grpc.py
--r-xr-xr-x   0 runner    (1000) runner    (1000)    28893 2022-10-28 01:56:00.000000 formant-1.99.10/formant/protos/model/v1/event_pb2.py
--r-xr-xr-x   0 runner    (1000) runner    (1000)      159 2022-10-28 01:56:00.000000 formant-1.99.10/formant/protos/model/v1/event_pb2_grpc.py
--r-xr-xr-x   0 runner    (1000) runner    (1000)     3613 2022-10-28 01:56:00.000000 formant-1.99.10/formant/protos/model/v1/file_pb2.py
--r-xr-xr-x   0 runner    (1000) runner    (1000)      159 2022-10-28 01:56:00.000000 formant-1.99.10/formant/protos/model/v1/file_pb2_grpc.py
--r-xr-xr-x   0 runner    (1000) runner    (1000)     7304 2022-10-28 01:56:00.000000 formant-1.99.10/formant/protos/model/v1/health_pb2.py
--r-xr-xr-x   0 runner    (1000) runner    (1000)      159 2022-10-28 01:56:00.000000 formant-1.99.10/formant/protos/model/v1/health_pb2_grpc.py
--r-xr-xr-x   0 runner    (1000) runner    (1000)    33872 2022-10-28 01:56:00.000000 formant-1.99.10/formant/protos/model/v1/intervention_pb2.py
--r-xr-xr-x   0 runner    (1000) runner    (1000)      159 2022-10-28 01:56:00.000000 formant-1.99.10/formant/protos/model/v1/intervention_pb2_grpc.py
--r-xr-xr-x   0 runner    (1000) runner    (1000)    21713 2022-10-28 01:56:00.000000 formant-1.99.10/formant/protos/model/v1/math_pb2.py
--r-xr-xr-x   0 runner    (1000) runner    (1000)      159 2022-10-28 01:56:00.000000 formant-1.99.10/formant/protos/model/v1/math_pb2_grpc.py
--r-xr-xr-x   0 runner    (1000) runner    (1000)    19190 2022-10-28 01:56:00.000000 formant-1.99.10/formant/protos/model/v1/media_pb2.py
--r-xr-xr-x   0 runner    (1000) runner    (1000)      159 2022-10-28 01:56:00.000000 formant-1.99.10/formant/protos/model/v1/media_pb2_grpc.py
--r-xr-xr-x   0 runner    (1000) runner    (1000)    42165 2022-10-28 01:56:00.000000 formant-1.99.10/formant/protos/model/v1/navigation_pb2.py
--r-xr-xr-x   0 runner    (1000) runner    (1000)      159 2022-10-28 01:56:00.000000 formant-1.99.10/formant/protos/model/v1/navigation_pb2_grpc.py
--r-xr-xr-x   0 runner    (1000) runner    (1000)    23518 2022-10-28 01:56:00.000000 formant-1.99.10/formant/protos/model/v1/ros_pb2.py
--r-xr-xr-x   0 runner    (1000) runner    (1000)      159 2022-10-28 01:56:00.000000 formant-1.99.10/formant/protos/model/v1/ros_pb2_grpc.py
--r-xr-xr-x   0 runner    (1000) runner    (1000)     3321 2022-10-28 01:56:00.000000 formant-1.99.10/formant/protos/model/v1/text_pb2.py
--r-xr-xr-x   0 runner    (1000) runner    (1000)      159 2022-10-28 01:56:00.000000 formant-1.99.10/formant/protos/model/v1/text_pb2_grpc.py
-drwxr-xr-x   0 runner    (1000) runner    (1000)        0 2022-10-28 01:56:00.666675 formant-1.99.10/formant/sdk/
--r-xr-xr-x   0 runner    (1000) runner    (1000)        0 2022-10-28 01:56:00.000000 formant-1.99.10/formant/sdk/__init__.py
-drwxr-xr-x   0 runner    (1000) runner    (1000)        0 2022-10-28 01:56:00.666675 formant-1.99.10/formant/sdk/agent/
--r-xr-xr-x   0 runner    (1000) runner    (1000)        0 2022-10-28 01:56:00.000000 formant-1.99.10/formant/sdk/agent/__init__.py
-drwxr-xr-x   0 runner    (1000) runner    (1000)        0 2022-10-28 01:56:00.666675 formant-1.99.10/formant/sdk/agent/adapter_utils/
--r-xr-xr-x   0 runner    (1000) runner    (1000)       71 2022-10-28 01:56:00.000000 formant-1.99.10/formant/sdk/agent/adapter_utils/__init__.py
--r-xr-xr-x   0 runner    (1000) runner    (1000)     3801 2022-10-28 01:56:00.000000 formant-1.99.10/formant/sdk/agent/adapter_utils/json_schema_validator.py
-drwxr-xr-x   0 runner    (1000) runner    (1000)        0 2022-10-28 01:56:00.670675 formant-1.99.10/formant/sdk/agent/v1/
--r-xr-xr-x   0 runner    (1000) runner    (1000)       43 2022-10-28 01:56:00.000000 formant-1.99.10/formant/sdk/agent/v1/__init__.py
--r-xr-xr-x   0 runner    (1000) runner    (1000)     1614 2022-10-28 01:56:00.000000 formant-1.99.10/formant/sdk/agent/v1/cancellable_stream_thread.py
--r-xr-xr-x   0 runner    (1000) runner    (1000)    52728 2022-10-28 01:56:00.000000 formant-1.99.10/formant/sdk/agent/v1/client.py
--r-xr-xr-x   0 runner    (1000) runner    (1000)     1878 2022-10-28 01:56:00.000000 formant-1.99.10/formant/sdk/agent/v1/exceptions.py
-drwxr-xr-x   0 runner    (1000) runner    (1000)        0 2022-10-28 01:56:00.670675 formant-1.99.10/formant/sdk/agent/v1/localization/
--r-xr-xr-x   0 runner    (1000) runner    (1000)        0 2022-10-28 01:56:00.000000 formant-1.99.10/formant/sdk/agent/v1/localization/__init__.py
--r-xr-xr-x   0 runner    (1000) runner    (1000)     4079 2022-10-28 01:56:00.000000 formant-1.99.10/formant/sdk/agent/v1/localization/localization_manager.py
-drwxr-xr-x   0 runner    (1000) runner    (1000)        0 2022-10-28 01:56:00.670675 formant-1.99.10/formant/sdk/agent/v1/localization/types/
--r-xr-xr-x   0 runner    (1000) runner    (1000)      271 2022-10-28 01:56:00.000000 formant-1.99.10/formant/sdk/agent/v1/localization/types/__init__.py
--r-xr-xr-x   0 runner    (1000) runner    (1000)      492 2022-10-28 01:56:00.000000 formant-1.99.10/formant/sdk/agent/v1/localization/types/goal.py
--r-xr-xr-x   0 runner    (1000) runner    (1000)     1779 2022-10-28 01:56:00.000000 formant-1.99.10/formant/sdk/agent/v1/localization/types/map.py
--r-xr-xr-x   0 runner    (1000) runner    (1000)     1260 2022-10-28 01:56:00.000000 formant-1.99.10/formant/sdk/agent/v1/localization/types/odometry.py
--r-xr-xr-x   0 runner    (1000) runner    (1000)      972 2022-10-28 01:56:00.000000 formant-1.99.10/formant/sdk/agent/v1/localization/types/path.py
-drwxr-xr-x   0 runner    (1000) runner    (1000)        0 2022-10-28 01:56:00.670675 formant-1.99.10/formant/sdk/agent/v1/localization/types/point_cloud/
--r-xr-xr-x   0 runner    (1000) runner    (1000)       48 2022-10-28 01:56:00.000000 formant-1.99.10/formant/sdk/agent/v1/localization/types/point_cloud/__init__.py
--r-xr-xr-x   0 runner    (1000) runner    (1000)     2569 2022-10-28 01:56:00.000000 formant-1.99.10/formant/sdk/agent/v1/localization/types/point_cloud/external.py
--r-xr-xr-x   0 runner    (1000) runner    (1000)     1437 2022-10-28 01:56:00.000000 formant-1.99.10/formant/sdk/agent/v1/localization/types/point_cloud/internal_types.py
--r-xr-xr-x   0 runner    (1000) runner    (1000)     1252 2022-10-28 01:56:00.000000 formant-1.99.10/formant/sdk/agent/v1/localization/types/point_cloud/laserscan.py
--r-xr-xr-x   0 runner    (1000) runner    (1000)     4713 2022-10-28 01:56:00.000000 formant-1.99.10/formant/sdk/agent/v1/localization/types/point_cloud/numpy_compat.py
--r-xr-xr-x   0 runner    (1000) runner    (1000)     8205 2022-10-28 01:56:00.000000 formant-1.99.10/formant/sdk/agent/v1/localization/types/point_cloud/point_cloud2.py
--r-xr-xr-x   0 runner    (1000) runner    (1000)     1223 2022-10-28 01:56:00.000000 formant-1.99.10/formant/sdk/agent/v1/localization/types/quaternion.py
--r-xr-xr-x   0 runner    (1000) runner    (1000)     2245 2022-10-28 01:56:00.000000 formant-1.99.10/formant/sdk/agent/v1/localization/types/transform.py
--r-xr-xr-x   0 runner    (1000) runner    (1000)     1007 2022-10-28 01:56:00.000000 formant-1.99.10/formant/sdk/agent/v1/localization/types/twist.py
--r-xr-xr-x   0 runner    (1000) runner    (1000)      999 2022-10-28 01:56:00.000000 formant-1.99.10/formant/sdk/agent/v1/localization/types/vector3.py
--r-xr-xr-x   0 runner    (1000) runner    (1000)     1815 2022-10-28 01:56:00.000000 formant-1.99.10/formant/sdk/agent/v1/localization/utils.py
-drwxr-xr-x   0 runner    (1000) runner    (1000)        0 2022-10-28 01:56:00.670675 formant-1.99.10/formant/sdk/cloud/
--r-xr-xr-x   0 runner    (1000) runner    (1000)        0 2022-10-28 01:56:00.000000 formant-1.99.10/formant/sdk/cloud/__init__.py
-drwxr-xr-x   0 runner    (1000) runner    (1000)        0 2022-10-28 01:56:00.670675 formant-1.99.10/formant/sdk/cloud/v1/
--r-xr-xr-x   0 runner    (1000) runner    (1000)       43 2022-10-28 01:56:00.000000 formant-1.99.10/formant/sdk/cloud/v1/__init__.py
--r-xr-xr-x   0 runner    (1000) runner    (1000)    19798 2022-10-28 01:56:00.000000 formant-1.99.10/formant/sdk/cloud/v1/client.py
-drwxr-xr-x   0 runner    (1000) runner    (1000)        0 2022-10-28 01:56:00.670675 formant-1.99.10/formant/sdk/cloud/v1/types/
--r-xr-xr-x   0 runner    (1000) runner    (1000)      223 2022-10-28 01:56:00.000000 formant-1.99.10/formant/sdk/cloud/v1/types/__init__.py
--r-xr-xr-x   0 runner    (1000) runner    (1000)     2604 2022-10-28 01:56:00.000000 formant-1.99.10/formant/sdk/cloud/v1/types/annotation.py
--r-xr-xr-x   0 runner    (1000) runner    (1000)      995 2022-10-28 01:56:00.000000 formant-1.99.10/formant/sdk/cloud/v1/types/annotation_field.py
--r-xr-xr-x   0 runner    (1000) runner    (1000)      849 2022-10-28 01:56:00.000000 formant-1.99.10/formant/sdk/cloud/v1/types/annotation_template.py
--r-xr-xr-x   0 runner    (1000) runner    (1000)      909 2022-10-28 01:56:00.000000 formant-1.99.10/formant/sdk/cloud/v1/types/annotation_template_list_result.py
-drwxr-xr-x   0 runner    (1000) runner    (1000)        0 2022-10-28 01:56:00.670675 formant-1.99.10/formant/sdk/utils/
--r-xr-xr-x   0 runner    (1000) runner    (1000)       59 2022-10-28 01:56:00.000000 formant-1.99.10/formant/sdk/utils/__init__.py
--r-xr-xr-x   0 runner    (1000) runner    (1000)     1938 2022-10-28 01:56:00.000000 formant-1.99.10/formant/sdk/utils/get_message_path_value.py
-drwxr-xr-x   0 runner    (1000) runner    (1000)        0 2022-10-28 01:56:00.666675 formant-1.99.10/formant.egg-info/
--rw-r--r--   0 runner    (1000) runner    (1000)      449 2022-10-28 01:56:00.000000 formant-1.99.10/formant.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1000) runner    (1000)     3199 2022-10-28 01:56:00.000000 formant-1.99.10/formant.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1000) runner    (1000)        1 2022-10-28 01:56:00.000000 formant-1.99.10/formant.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1000) runner    (1000)      143 2022-10-28 01:56:00.000000 formant-1.99.10/formant.egg-info/requires.txt
--rw-r--r--   0 runner    (1000) runner    (1000)        8 2022-10-28 01:56:00.000000 formant-1.99.10/formant.egg-info/top_level.txt
--rw-r--r--   0 runner    (1000) runner    (1000)       38 2022-10-28 01:56:00.670675 formant-1.99.10/setup.cfg
--r-xr-xr-x   0 runner    (1000) runner    (1000)      859 2022-10-28 01:56:00.000000 formant-1.99.10/setup.py
+drwxr-xr-x   0 runner    (1000) runner    (1000)        0 2022-11-08 04:22:53.837377 formant-1.99.25/
+-rw-r--r--   0 runner    (1000) runner    (1000)      449 2022-11-08 04:22:53.837377 formant-1.99.25/PKG-INFO
+-r-xr-xr-x   0 runner    (1000) runner    (1000)       23 2000-01-01 00:00:00.000000 formant-1.99.25/README.md
+drwxr-xr-x   0 runner    (1000) runner    (1000)        0 2022-11-08 04:22:53.829377 formant-1.99.25/formant/
+-r-xr-xr-x   0 runner    (1000) runner    (1000)        0 2022-11-08 04:22:53.000000 formant-1.99.25/formant/__init__.py
+drwxr-xr-x   0 runner    (1000) runner    (1000)        0 2022-11-08 04:22:53.833377 formant-1.99.25/formant/protos/
+-rwxr-xr-x   0 runner    (1000) runner    (1000)        0 2022-11-08 04:22:53.000000 formant-1.99.25/formant/protos/__init__.py
+drwxr-xr-x   0 runner    (1000) runner    (1000)        0 2022-11-08 04:22:53.833377 formant-1.99.25/formant/protos/agent/
+-r-xr-xr-x   0 runner    (1000) runner    (1000)        0 2022-11-08 04:22:53.000000 formant-1.99.25/formant/protos/agent/__init__.py
+drwxr-xr-x   0 runner    (1000) runner    (1000)        0 2022-11-08 04:22:53.833377 formant-1.99.25/formant/protos/agent/v1/
+-r-xr-xr-x   0 runner    (1000) runner    (1000)        0 2022-11-08 04:22:53.000000 formant-1.99.25/formant/protos/agent/v1/__init__.py
+-r-xr-xr-x   0 runner    (1000) runner    (1000)    77876 2022-11-08 04:22:53.000000 formant-1.99.25/formant/protos/agent/v1/agent_pb2.py
+-r-xr-xr-x   0 runner    (1000) runner    (1000)    45713 2022-11-08 04:22:53.000000 formant-1.99.25/formant/protos/agent/v1/agent_pb2_grpc.py
+drwxr-xr-x   0 runner    (1000) runner    (1000)        0 2022-11-08 04:22:53.833377 formant-1.99.25/formant/protos/api/
+-rwxr-xr-x   0 runner    (1000) runner    (1000)        0 2022-11-08 04:22:53.000000 formant-1.99.25/formant/protos/api/__init__.py
+drwxr-xr-x   0 runner    (1000) runner    (1000)        0 2022-11-08 04:22:53.833377 formant-1.99.25/formant/protos/api/signaling/
+-rwxr-xr-x   0 runner    (1000) runner    (1000)        0 2022-11-08 04:22:53.000000 formant-1.99.25/formant/protos/api/signaling/__init__.py
+drwxr-xr-x   0 runner    (1000) runner    (1000)        0 2022-11-08 04:22:53.833377 formant-1.99.25/formant/protos/model/
+-rwxr-xr-x   0 runner    (1000) runner    (1000)        0 2022-11-08 04:22:53.000000 formant-1.99.25/formant/protos/model/__init__.py
+drwxr-xr-x   0 runner    (1000) runner    (1000)        0 2022-11-08 04:22:53.833377 formant-1.99.25/formant/protos/model/v1/
+-r-xr-xr-x   0 runner    (1000) runner    (1000)        0 2022-11-08 04:22:53.000000 formant-1.99.25/formant/protos/model/v1/__init__.py
+-r-xr-xr-x   0 runner    (1000) runner    (1000)    10369 2022-11-08 04:22:53.000000 formant-1.99.25/formant/protos/model/v1/commands_pb2.py
+-r-xr-xr-x   0 runner    (1000) runner    (1000)      159 2022-11-08 04:22:53.000000 formant-1.99.25/formant/protos/model/v1/commands_pb2_grpc.py
+-r-xr-xr-x   0 runner    (1000) runner    (1000)    94200 2022-11-08 04:22:53.000000 formant-1.99.25/formant/protos/model/v1/config_pb2.py
+-r-xr-xr-x   0 runner    (1000) runner    (1000)      159 2022-11-08 04:22:53.000000 formant-1.99.25/formant/protos/model/v1/config_pb2_grpc.py
+-r-xr-xr-x   0 runner    (1000) runner    (1000)    24653 2022-11-08 04:22:53.000000 formant-1.99.25/formant/protos/model/v1/datapoint_pb2.py
+-r-xr-xr-x   0 runner    (1000) runner    (1000)      159 2022-11-08 04:22:53.000000 formant-1.99.25/formant/protos/model/v1/datapoint_pb2_grpc.py
+-r-xr-xr-x   0 runner    (1000) runner    (1000)    28893 2022-11-08 04:22:53.000000 formant-1.99.25/formant/protos/model/v1/event_pb2.py
+-r-xr-xr-x   0 runner    (1000) runner    (1000)      159 2022-11-08 04:22:53.000000 formant-1.99.25/formant/protos/model/v1/event_pb2_grpc.py
+-r-xr-xr-x   0 runner    (1000) runner    (1000)     3613 2022-11-08 04:22:53.000000 formant-1.99.25/formant/protos/model/v1/file_pb2.py
+-r-xr-xr-x   0 runner    (1000) runner    (1000)      159 2022-11-08 04:22:53.000000 formant-1.99.25/formant/protos/model/v1/file_pb2_grpc.py
+-r-xr-xr-x   0 runner    (1000) runner    (1000)     7304 2022-11-08 04:22:53.000000 formant-1.99.25/formant/protos/model/v1/health_pb2.py
+-r-xr-xr-x   0 runner    (1000) runner    (1000)      159 2022-11-08 04:22:53.000000 formant-1.99.25/formant/protos/model/v1/health_pb2_grpc.py
+-r-xr-xr-x   0 runner    (1000) runner    (1000)    33872 2022-11-08 04:22:53.000000 formant-1.99.25/formant/protos/model/v1/intervention_pb2.py
+-r-xr-xr-x   0 runner    (1000) runner    (1000)      159 2022-11-08 04:22:53.000000 formant-1.99.25/formant/protos/model/v1/intervention_pb2_grpc.py
+-r-xr-xr-x   0 runner    (1000) runner    (1000)    21713 2022-11-08 04:22:53.000000 formant-1.99.25/formant/protos/model/v1/math_pb2.py
+-r-xr-xr-x   0 runner    (1000) runner    (1000)      159 2022-11-08 04:22:53.000000 formant-1.99.25/formant/protos/model/v1/math_pb2_grpc.py
+-r-xr-xr-x   0 runner    (1000) runner    (1000)    19190 2022-11-08 04:22:53.000000 formant-1.99.25/formant/protos/model/v1/media_pb2.py
+-r-xr-xr-x   0 runner    (1000) runner    (1000)      159 2022-11-08 04:22:53.000000 formant-1.99.25/formant/protos/model/v1/media_pb2_grpc.py
+-r-xr-xr-x   0 runner    (1000) runner    (1000)    42165 2022-11-08 04:22:53.000000 formant-1.99.25/formant/protos/model/v1/navigation_pb2.py
+-r-xr-xr-x   0 runner    (1000) runner    (1000)      159 2022-11-08 04:22:53.000000 formant-1.99.25/formant/protos/model/v1/navigation_pb2_grpc.py
+-r-xr-xr-x   0 runner    (1000) runner    (1000)    23518 2022-11-08 04:22:53.000000 formant-1.99.25/formant/protos/model/v1/ros_pb2.py
+-r-xr-xr-x   0 runner    (1000) runner    (1000)      159 2022-11-08 04:22:53.000000 formant-1.99.25/formant/protos/model/v1/ros_pb2_grpc.py
+-r-xr-xr-x   0 runner    (1000) runner    (1000)     3321 2022-11-08 04:22:53.000000 formant-1.99.25/formant/protos/model/v1/text_pb2.py
+-r-xr-xr-x   0 runner    (1000) runner    (1000)      159 2022-11-08 04:22:53.000000 formant-1.99.25/formant/protos/model/v1/text_pb2_grpc.py
+drwxr-xr-x   0 runner    (1000) runner    (1000)        0 2022-11-08 04:22:53.833377 formant-1.99.25/formant/sdk/
+-r-xr-xr-x   0 runner    (1000) runner    (1000)        0 2022-11-08 04:22:53.000000 formant-1.99.25/formant/sdk/__init__.py
+drwxr-xr-x   0 runner    (1000) runner    (1000)        0 2022-11-08 04:22:53.833377 formant-1.99.25/formant/sdk/agent/
+-r-xr-xr-x   0 runner    (1000) runner    (1000)        0 2022-11-08 04:22:53.000000 formant-1.99.25/formant/sdk/agent/__init__.py
+drwxr-xr-x   0 runner    (1000) runner    (1000)        0 2022-11-08 04:22:53.833377 formant-1.99.25/formant/sdk/agent/adapter_utils/
+-r-xr-xr-x   0 runner    (1000) runner    (1000)       71 2022-11-08 04:22:53.000000 formant-1.99.25/formant/sdk/agent/adapter_utils/__init__.py
+-r-xr-xr-x   0 runner    (1000) runner    (1000)     3801 2022-11-08 04:22:53.000000 formant-1.99.25/formant/sdk/agent/adapter_utils/json_schema_validator.py
+drwxr-xr-x   0 runner    (1000) runner    (1000)        0 2022-11-08 04:22:53.833377 formant-1.99.25/formant/sdk/agent/v1/
+-r-xr-xr-x   0 runner    (1000) runner    (1000)       43 2022-11-08 04:22:53.000000 formant-1.99.25/formant/sdk/agent/v1/__init__.py
+-r-xr-xr-x   0 runner    (1000) runner    (1000)     1614 2022-11-08 04:22:53.000000 formant-1.99.25/formant/sdk/agent/v1/cancellable_stream_thread.py
+-r-xr-xr-x   0 runner    (1000) runner    (1000)    52728 2022-11-08 04:22:53.000000 formant-1.99.25/formant/sdk/agent/v1/client.py
+-r-xr-xr-x   0 runner    (1000) runner    (1000)     1878 2022-11-08 04:22:53.000000 formant-1.99.25/formant/sdk/agent/v1/exceptions.py
+drwxr-xr-x   0 runner    (1000) runner    (1000)        0 2022-11-08 04:22:53.833377 formant-1.99.25/formant/sdk/agent/v1/localization/
+-r-xr-xr-x   0 runner    (1000) runner    (1000)        0 2022-11-08 04:22:53.000000 formant-1.99.25/formant/sdk/agent/v1/localization/__init__.py
+-r-xr-xr-x   0 runner    (1000) runner    (1000)     4079 2022-11-08 04:22:53.000000 formant-1.99.25/formant/sdk/agent/v1/localization/localization_manager.py
+drwxr-xr-x   0 runner    (1000) runner    (1000)        0 2022-11-08 04:22:53.837377 formant-1.99.25/formant/sdk/agent/v1/localization/types/
+-r-xr-xr-x   0 runner    (1000) runner    (1000)      271 2022-11-08 04:22:53.000000 formant-1.99.25/formant/sdk/agent/v1/localization/types/__init__.py
+-r-xr-xr-x   0 runner    (1000) runner    (1000)      492 2022-11-08 04:22:53.000000 formant-1.99.25/formant/sdk/agent/v1/localization/types/goal.py
+-r-xr-xr-x   0 runner    (1000) runner    (1000)     1779 2022-11-08 04:22:53.000000 formant-1.99.25/formant/sdk/agent/v1/localization/types/map.py
+-r-xr-xr-x   0 runner    (1000) runner    (1000)     1260 2022-11-08 04:22:53.000000 formant-1.99.25/formant/sdk/agent/v1/localization/types/odometry.py
+-r-xr-xr-x   0 runner    (1000) runner    (1000)      972 2022-11-08 04:22:53.000000 formant-1.99.25/formant/sdk/agent/v1/localization/types/path.py
+drwxr-xr-x   0 runner    (1000) runner    (1000)        0 2022-11-08 04:22:53.837377 formant-1.99.25/formant/sdk/agent/v1/localization/types/point_cloud/
+-r-xr-xr-x   0 runner    (1000) runner    (1000)       48 2022-11-08 04:22:53.000000 formant-1.99.25/formant/sdk/agent/v1/localization/types/point_cloud/__init__.py
+-r-xr-xr-x   0 runner    (1000) runner    (1000)     2569 2022-11-08 04:22:53.000000 formant-1.99.25/formant/sdk/agent/v1/localization/types/point_cloud/external.py
+-r-xr-xr-x   0 runner    (1000) runner    (1000)     1437 2022-11-08 04:22:53.000000 formant-1.99.25/formant/sdk/agent/v1/localization/types/point_cloud/internal_types.py
+-r-xr-xr-x   0 runner    (1000) runner    (1000)     1252 2022-11-08 04:22:53.000000 formant-1.99.25/formant/sdk/agent/v1/localization/types/point_cloud/laserscan.py
+-r-xr-xr-x   0 runner    (1000) runner    (1000)     4713 2022-11-08 04:22:53.000000 formant-1.99.25/formant/sdk/agent/v1/localization/types/point_cloud/numpy_compat.py
+-r-xr-xr-x   0 runner    (1000) runner    (1000)     8205 2022-11-08 04:22:53.000000 formant-1.99.25/formant/sdk/agent/v1/localization/types/point_cloud/point_cloud2.py
+-r-xr-xr-x   0 runner    (1000) runner    (1000)     1223 2022-11-08 04:22:53.000000 formant-1.99.25/formant/sdk/agent/v1/localization/types/quaternion.py
+-r-xr-xr-x   0 runner    (1000) runner    (1000)     2245 2022-11-08 04:22:53.000000 formant-1.99.25/formant/sdk/agent/v1/localization/types/transform.py
+-r-xr-xr-x   0 runner    (1000) runner    (1000)     1007 2022-11-08 04:22:53.000000 formant-1.99.25/formant/sdk/agent/v1/localization/types/twist.py
+-r-xr-xr-x   0 runner    (1000) runner    (1000)      999 2022-11-08 04:22:53.000000 formant-1.99.25/formant/sdk/agent/v1/localization/types/vector3.py
+-r-xr-xr-x   0 runner    (1000) runner    (1000)     1815 2022-11-08 04:22:53.000000 formant-1.99.25/formant/sdk/agent/v1/localization/utils.py
+drwxr-xr-x   0 runner    (1000) runner    (1000)        0 2022-11-08 04:22:53.837377 formant-1.99.25/formant/sdk/cloud/
+-r-xr-xr-x   0 runner    (1000) runner    (1000)        0 2022-11-08 04:22:53.000000 formant-1.99.25/formant/sdk/cloud/__init__.py
+drwxr-xr-x   0 runner    (1000) runner    (1000)        0 2022-11-08 04:22:53.837377 formant-1.99.25/formant/sdk/cloud/v1/
+-r-xr-xr-x   0 runner    (1000) runner    (1000)       43 2022-11-08 04:22:53.000000 formant-1.99.25/formant/sdk/cloud/v1/__init__.py
+-r-xr-xr-x   0 runner    (1000) runner    (1000)    19798 2022-11-08 04:22:53.000000 formant-1.99.25/formant/sdk/cloud/v1/client.py
+drwxr-xr-x   0 runner    (1000) runner    (1000)        0 2022-11-08 04:22:53.837377 formant-1.99.25/formant/sdk/cloud/v1/types/
+-r-xr-xr-x   0 runner    (1000) runner    (1000)      223 2022-11-08 04:22:53.000000 formant-1.99.25/formant/sdk/cloud/v1/types/__init__.py
+-r-xr-xr-x   0 runner    (1000) runner    (1000)     2604 2022-11-08 04:22:53.000000 formant-1.99.25/formant/sdk/cloud/v1/types/annotation.py
+-r-xr-xr-x   0 runner    (1000) runner    (1000)      995 2022-11-08 04:22:53.000000 formant-1.99.25/formant/sdk/cloud/v1/types/annotation_field.py
+-r-xr-xr-x   0 runner    (1000) runner    (1000)      849 2022-11-08 04:22:53.000000 formant-1.99.25/formant/sdk/cloud/v1/types/annotation_template.py
+-r-xr-xr-x   0 runner    (1000) runner    (1000)      909 2022-11-08 04:22:53.000000 formant-1.99.25/formant/sdk/cloud/v1/types/annotation_template_list_result.py
+drwxr-xr-x   0 runner    (1000) runner    (1000)        0 2022-11-08 04:22:53.837377 formant-1.99.25/formant/sdk/utils/
+-r-xr-xr-x   0 runner    (1000) runner    (1000)       59 2022-11-08 04:22:53.000000 formant-1.99.25/formant/sdk/utils/__init__.py
+-r-xr-xr-x   0 runner    (1000) runner    (1000)     1938 2022-11-08 04:22:53.000000 formant-1.99.25/formant/sdk/utils/get_message_path_value.py
+drwxr-xr-x   0 runner    (1000) runner    (1000)        0 2022-11-08 04:22:53.833377 formant-1.99.25/formant.egg-info/
+-rw-r--r--   0 runner    (1000) runner    (1000)      449 2022-11-08 04:22:53.000000 formant-1.99.25/formant.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1000) runner    (1000)     3199 2022-11-08 04:22:53.000000 formant-1.99.25/formant.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1000) runner    (1000)        1 2022-11-08 04:22:53.000000 formant-1.99.25/formant.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1000) runner    (1000)      143 2022-11-08 04:22:53.000000 formant-1.99.25/formant.egg-info/requires.txt
+-rw-r--r--   0 runner    (1000) runner    (1000)        8 2022-11-08 04:22:53.000000 formant-1.99.25/formant.egg-info/top_level.txt
+-rw-r--r--   0 runner    (1000) runner    (1000)       38 2022-11-08 04:22:53.837377 formant-1.99.25/setup.cfg
+-r-xr-xr-x   0 runner    (1000) runner    (1000)      859 2022-11-08 04:22:53.000000 formant-1.99.25/setup.py
```

### Comparing `formant-1.99.10/formant/protos/agent/v1/agent_pb2.py` & `formant-1.99.25/formant/protos/agent/v1/agent_pb2.py`

 * *Files identical despite different names*

### Comparing `formant-1.99.10/formant/protos/agent/v1/agent_pb2_grpc.py` & `formant-1.99.25/formant/protos/agent/v1/agent_pb2_grpc.py`

 * *Files identical despite different names*

### Comparing `formant-1.99.10/formant/protos/model/v1/commands_pb2.py` & `formant-1.99.25/formant/protos/model/v1/commands_pb2.py`

 * *Files identical despite different names*

### Comparing `formant-1.99.10/formant/protos/model/v1/config_pb2.py` & `formant-1.99.25/formant/protos/model/v1/config_pb2.py`

 * *Files 1% similar despite different names*

```diff
@@ -18,15 +18,15 @@
 
 DESCRIPTOR = _descriptor.FileDescriptor(
   name='protos/model/v1/config.proto',
   package='v1.model',
   syntax='proto3',
   serialized_options=b'Z)github.com/FormantIO/genproto/go/v1/model',
   create_key=_descriptor._internal_create_key,
-  serialized_pb=b'\n\x1cprotos/model/v1/config.proto\x12\x08v1.model\x1a\x19protos/model/v1/ros.proto\x1a\x1egoogle/protobuf/wrappers.proto\"\xbe\x01\n\x17\x41gentConfigurationStore\x12#\n\ragent_version\x18\x01 \x01(\tR\x0c\x61gentVersion\x12\x42\n\rconfiguration\x18\x02 \x01(\x0b\x32\x1c.v1.model.AgentConfigurationR\rconfiguration\x12:\n\x0b\x66\x65\x61ture_set\x18\x03 \x01(\x0b\x32\x19.v1.model.AgentFeatureSetR\nfeatureSet\"\xa2\x03\n\x0f\x41gentFeatureSet\x12\x1c\n\ttelemetry\x18\x01 \x01(\x08R\ttelemetry\x12-\n\x12internal_telemetry\x18\x02 \x01(\x08R\x11internalTelemetry\x12\x16\n\x06teleop\x18\x03 \x01(\x08R\x06teleop\x12#\n\rcustom_events\x18\x04 \x01(\x08R\x0c\x63ustomEvents\x12)\n\x10triggered_events\x18\x05 \x01(\x08R\x0ftriggeredEvents\x12\x10\n\x03ssh\x18\x06 \x01(\x08R\x03ssh\x12\'\n\x0fport_forwarding\x18\x07 \x01(\x08R\x0eportForwarding\x12\x1a\n\x08\x63ommands\x18\x08 \x01(\x08R\x08\x63ommands\x12$\n\rinterventions\x18\t \x01(\x08R\rinterventions\x12\x1b\n\ton_demand\x18\n \x01(\x08R\x08onDemand\x12\x1d\n\napp_config\x18\x0b \x01(\x08R\tappConfig\x12!\n\x0c\x62lob_storage\x18\x0c \x01(\x08R\x0b\x62lobStorage\"z\n\x12\x41gentConfiguration\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12\x12\n\x04name\x18\x02 \x01(\tR\x04name\x12@\n\x08\x64ocument\x18\x03 \x01(\x0b\x32$.v1.model.AgentConfigurationDocumentR\x08\x64ocument\"\xeb\x05\n\x1a\x41gentConfigurationDocument\x12\x18\n\x07version\x18\x01 \x01(\x03R\x07version\x12\x42\n\x04tags\x18\x02 \x03(\x0b\x32..v1.model.AgentConfigurationDocument.TagsEntryR\x04tags\x12>\n\ttelemetry\x18\x03 \x01(\x0b\x32 .v1.model.TelemetryConfigurationR\ttelemetry\x12>\n\tresources\x18\x04 \x01(\x0b\x32 .v1.model.ResourcesConfigurationR\tresources\x12\x44\n\x0b\x61pplication\x18\x05 \x01(\x0b\x32\".v1.model.ApplicationConfigurationR\x0b\x61pplication\x12\x35\n\x06teleop\x18\x06 \x01(\x0b\x32\x1d.v1.model.TeleopConfigurationR\x06teleop\x12N\n\x0fport_forwarding\x18\x07 \x01(\x0b\x32%.v1.model.PortForwardingConfigurationR\x0eportForwarding\x12/\n\tblob_data\x18\x08 \x01(\x0b\x32\x12.v1.model.BlobDataR\x08\x62lobData\x12\x37\n\x0b\x64iagnostics\x18\t \x01(\x0b\x32\x15.v1.model.DiagnosticsR\x0b\x64iagnostics\x12\x43\n\x0fterminal_access\x18\n \x01(\x0b\x32\x1a.google.protobuf.BoolValueR\x0eterminalAccess\x12:\n\x08\x61\x64\x61pters\x18\x0b \x03(\x0b\x32\x1e.v1.model.AdapterConfigurationR\x08\x61\x64\x61pters\x1a\x37\n\tTagsEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value:\x02\x38\x01\"v\n\x14\x41\x64\x61pterConfiguration\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12\x12\n\x04name\x18\x02 \x01(\tR\x04name\x12\x17\n\x07\x66ile_id\x18\x03 \x01(\tR\x06\x66ileId\x12!\n\x0c\x65xec_command\x18\x04 \x01(\tR\x0b\x65xecCommand\"\x88\x02\n\x13TeleopConfiguration\x12G\n\x0bros_streams\x18\x01 \x03(\x0b\x32&.v1.model.TeleopRosStreamConfigurationR\nrosStreams\x12P\n\x0e\x63ustom_streams\x18\x02 \x03(\x0b\x32).v1.model.TeleopCustomStreamConfigurationR\rcustomStreams\x12V\n\x10hardware_streams\x18\x03 \x03(\x0b\x32+.v1.model.TeleopHardwareStreamConfigurationR\x0fhardwareStreams\"S\n\x1bPortForwardingConfiguration\x12\x34\n\x07\x65nabled\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.BoolValueR\x07\x65nabled\"\xcf\x02\n\x1cTeleopRosStreamConfiguration\x12\x1d\n\ntopic_name\x18\x01 \x01(\tR\ttopicName\x12\x35\n\ntopic_type\x18\x02 \x01(\x0e\x32\x16.v1.model.ROSTopicTypeR\ttopicType\x12(\n\x04mode\x18\x03 \x01(\x0e\x32\x14.v1.model.TeleopModeR\x04mode\x12!\n\x0c\x65ncode_video\x18\x04 \x01(\x08R\x0b\x65ncodeVideo\x12\x1f\n\x0b\x61udio_codec\x18\x05 \x01(\tR\naudioCodec\x12\x18\n\x07quality\x18\x06 \x01(\tR\x07quality\x12\x30\n\x14\x62\x61se_reference_frame\x18\x07 \x01(\tR\x12\x62\x61seReferenceFrame\x12\x1f\n\x0blocal_frame\x18\x08 \x01(\tR\nlocalFrame\"\x8a\x03\n!TeleopHardwareStreamConfiguration\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12&\n\x0frtc_stream_type\x18\x02 \x01(\tR\rrtcStreamType\x12(\n\x04mode\x18\x03 \x01(\x0e\x32\x14.v1.model.TeleopModeR\x04mode\x12#\n\rhw_descriptor\x18\x04 \x01(\tR\x0chwDescriptor\x12\x18\n\x07quality\x18\x05 \x01(\tR\x07quality\x12#\n\rhardware_type\x18\x06 \x01(\tR\x0chardwareType\x12\x30\n\x14rtsp_encoding_needed\x18\x07 \x01(\x08R\x12rtspEncodingNeeded\x12\x19\n\x08is_onvif\x18\x08 \x01(\x08R\x07isOnvif\x12&\n\x0fip_cam_username\x18\t \x01(\tR\ripCamUsername\x12&\n\x0fip_cam_password\x18\n \x01(\tR\ripCamPassword\"\xc4\x01\n\x1fTeleopCustomStreamConfiguration\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12&\n\x0frtc_stream_type\x18\x02 \x01(\tR\rrtcStreamType\x12(\n\x04mode\x18\x03 \x01(\x0e\x32\x14.v1.model.TeleopModeR\x04mode\x12!\n\x0c\x65ncode_video\x18\x04 \x01(\x08R\x0b\x65ncodeVideo\x12\x18\n\x07quality\x18\x05 \x01(\tR\x07quality\"\x7f\n\x16TelemetryConfiguration\x12\x37\n\x07streams\x18\x01 \x03(\x0b\x32\x1d.v1.model.StreamConfigurationR\x07streams\x12,\n\x03ros\x18\x02 \x01(\x0b\x32\x1a.v1.model.ROSConfigurationR\x03ros\"\xc6\x01\n\x18\x41pplicationConfiguration\x12\x65\n\x11\x63onfiguration_map\x18\x01 \x03(\x0b\x32\x38.v1.model.ApplicationConfiguration.ConfigurationMapEntryR\x10\x63onfigurationMap\x1a\x43\n\x15\x43onfigurationMapEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value:\x02\x38\x01\"\xc5\x01\n\x16ResourcesConfiguration\x12/\n\x04\x64isk\x18\x01 \x01(\x0b\x32\x1b.v1.model.DiskConfigurationR\x04\x64isk\x12J\n\x12stream_throttle_hz\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.DoubleValueR\x10streamThrottleHz\x12.\n\x13low_bandwidth_agent\x18\x03 \x01(\x08R\x11lowBandwidthAgent\"g\n\x11\x44iskConfiguration\x12\x1f\n\x0b\x62uffer_size\x18\x01 \x01(\x03R\nbufferSize\x12\x31\n\x15on_demand_buffer_size\x18\x02 \x01(\x03R\x12onDemandBufferSize\"K\n\x10ROSConfiguration\x12\x37\n\x18world_reference_frame_id\x18\x01 \x01(\tR\x15worldReferenceFrameId\"\xdd\x06\n\x13StreamConfiguration\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12;\n\x04tags\x18\x02 \x03(\x0b\x32\'.v1.model.StreamConfiguration.TagsEntryR\x04tags\x12\x31\n\tros_topic\x18\x03 \x01(\x0b\x32\x12.v1.model.ROSTopicH\x00R\x08rosTopic\x12\x46\n\x10ros_localization\x18\x04 \x01(\x0b\x32\x19.v1.model.ROSLocalizationH\x00R\x0frosLocalization\x12\x43\n\x0f\x64irectory_watch\x18\x05 \x01(\x0b\x32\x18.v1.model.DirectoryWatchH\x00R\x0e\x64irectoryWatch\x12\x31\n\tfile_tail\x18\x06 \x01(\x0b\x32\x12.v1.model.FileTailH\x00R\x08\x66ileTail\x12J\n\x12ros_transform_tree\x18\x07 \x01(\x0b\x32\x1a.v1.model.ROSTransformTreeH\x00R\x10rosTransformTree\x12*\n\x06\x63ustom\x18\t \x01(\x0b\x32\x10.v1.model.CustomH\x00R\x06\x63ustom\x12\x30\n\x08hardware\x18\n \x01(\x0b\x32\x12.v1.model.HardwareH\x00R\x08hardware\x12=\n\x0bthrottle_hz\x18\x08 \x01(\x0b\x32\x1c.google.protobuf.DoubleValueR\nthrottleHz\x12\x36\n\x08\x64isabled\x18\x13 \x01(\x0b\x32\x1a.google.protobuf.BoolValueR\x08\x64isabled\x12\x37\n\ton_demand\x18\x14 \x01(\x0b\x32\x1a.google.protobuf.BoolValueR\x08onDemand\x12\x44\n\ttransform\x18\x15 \x01(\x0b\x32&.v1.model.StreamTransformConfigurationR\ttransform\x12\x18\n\x07quality\x18\x16 \x01(\tR\x07quality\x1a\x37\n\tTagsEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value:\x02\x38\x01\x42\x0f\n\rconfiguration\"p\n\x1cStreamTransformConfiguration\x12P\n\x16video_encoding_enabled\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.BoolValueR\x14videoEncodingEnabled\"\x1e\n\x08\x42lobData\x12\x12\n\x04\x64\x61ta\x18\x01 \x01(\tR\x04\x64\x61ta\"\x8d\x01\n\x0b\x44iagnostics\x12;\n\x0breport_logs\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.BoolValueR\nreportLogs\x12\x41\n\x0ereport_metrics\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.BoolValueR\rreportMetrics\"\x08\n\x06\x43ustom\"\xa1\x02\n\x08Hardware\x12#\n\rhw_descriptor\x18\x01 \x01(\tR\x0chwDescriptor\x12.\n\x13\x61udio_hw_descriptor\x18\x03 \x01(\tR\x11\x61udioHwDescriptor\x12#\n\rhardware_type\x18\x04 \x01(\tR\x0chardwareType\x12\x30\n\x14rtsp_encoding_needed\x18\x05 \x01(\x08R\x12rtspEncodingNeeded\x12\x19\n\x08is_onvif\x18\x06 \x01(\x08R\x07isOnvif\x12&\n\x0fip_cam_username\x18\x07 \x01(\tR\ripCamUsername\x12&\n\x0fip_cam_password\x18\x08 \x01(\tR\ripCamPassword\"\xa0\x01\n\x0e\x44irectoryWatch\x12\x1c\n\tdirectory\x18\x01 \x01(\tR\tdirectory\x12\x1c\n\textension\x18\x02 \x01(\tR\textension\x12/\n\tfile_type\x18\x03 \x01(\x0e\x32\x12.v1.model.FileTypeR\x08\x66ileType\x12!\n\x0cremote_agent\x18\x04 \x01(\x08R\x0bremoteAgent\"\xaf\x01\n\x08\x46ileTail\x12\x1a\n\x08\x66ilename\x18\x01 \x01(\tR\x08\x66ilename\x12\x35\n\x0b\x66ile_format\x18\x02 \x01(\x0e\x32\x14.v1.model.FileFormatR\nfileFormat\x12\x19\n\x08time_key\x18\x03 \x01(\tR\x07timeKey\x12\x1f\n\x0btime_format\x18\x04 \x01(\tR\ntimeFormat\x12\x14\n\x05regex\x18\x05 \x01(\tR\x05regex*&\n\nTeleopMode\x12\x0b\n\x07\x43OMMAND\x10\x00\x12\x0b\n\x07OBSERVE\x10\x01*&\n\nFileFormat\x12\x0e\n\nPLAIN_TEXT\x10\x00\x12\x08\n\x04JSON\x10\x01*;\n\x08\x46ileType\x12\x08\n\x04\x46ILE\x10\x00\x12\t\n\x05IMAGE\x10\x01\x12\x0f\n\x0bPOINT_CLOUD\x10\x04\x12\t\n\x05VIDEO\x10\x05\x42+Z)github.com/FormantIO/genproto/go/v1/modelb\x06proto3'
+  serialized_pb=b'\n\x1cprotos/model/v1/config.proto\x12\x08v1.model\x1a\x19protos/model/v1/ros.proto\x1a\x1egoogle/protobuf/wrappers.proto\"\xbe\x01\n\x17\x41gentConfigurationStore\x12#\n\ragent_version\x18\x01 \x01(\tR\x0c\x61gentVersion\x12\x42\n\rconfiguration\x18\x02 \x01(\x0b\x32\x1c.v1.model.AgentConfigurationR\rconfiguration\x12:\n\x0b\x66\x65\x61ture_set\x18\x03 \x01(\x0b\x32\x19.v1.model.AgentFeatureSetR\nfeatureSet\"\xa2\x03\n\x0f\x41gentFeatureSet\x12\x1c\n\ttelemetry\x18\x01 \x01(\x08R\ttelemetry\x12-\n\x12internal_telemetry\x18\x02 \x01(\x08R\x11internalTelemetry\x12\x16\n\x06teleop\x18\x03 \x01(\x08R\x06teleop\x12#\n\rcustom_events\x18\x04 \x01(\x08R\x0c\x63ustomEvents\x12)\n\x10triggered_events\x18\x05 \x01(\x08R\x0ftriggeredEvents\x12\x10\n\x03ssh\x18\x06 \x01(\x08R\x03ssh\x12\'\n\x0fport_forwarding\x18\x07 \x01(\x08R\x0eportForwarding\x12\x1a\n\x08\x63ommands\x18\x08 \x01(\x08R\x08\x63ommands\x12$\n\rinterventions\x18\t \x01(\x08R\rinterventions\x12\x1b\n\ton_demand\x18\n \x01(\x08R\x08onDemand\x12\x1d\n\napp_config\x18\x0b \x01(\x08R\tappConfig\x12!\n\x0c\x62lob_storage\x18\x0c \x01(\x08R\x0b\x62lobStorage\"z\n\x12\x41gentConfiguration\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12\x12\n\x04name\x18\x02 \x01(\tR\x04name\x12@\n\x08\x64ocument\x18\x03 \x01(\x0b\x32$.v1.model.AgentConfigurationDocumentR\x08\x64ocument\"\x99\x06\n\x1a\x41gentConfigurationDocument\x12\x18\n\x07version\x18\x01 \x01(\x03R\x07version\x12\x42\n\x04tags\x18\x02 \x03(\x0b\x32..v1.model.AgentConfigurationDocument.TagsEntryR\x04tags\x12>\n\ttelemetry\x18\x03 \x01(\x0b\x32 .v1.model.TelemetryConfigurationR\ttelemetry\x12>\n\tresources\x18\x04 \x01(\x0b\x32 .v1.model.ResourcesConfigurationR\tresources\x12\x44\n\x0b\x61pplication\x18\x05 \x01(\x0b\x32\".v1.model.ApplicationConfigurationR\x0b\x61pplication\x12\x35\n\x06teleop\x18\x06 \x01(\x0b\x32\x1d.v1.model.TeleopConfigurationR\x06teleop\x12N\n\x0fport_forwarding\x18\x07 \x01(\x0b\x32%.v1.model.PortForwardingConfigurationR\x0eportForwarding\x12/\n\tblob_data\x18\x08 \x01(\x0b\x32\x12.v1.model.BlobDataR\x08\x62lobData\x12\x37\n\x0b\x64iagnostics\x18\t \x01(\x0b\x32\x15.v1.model.DiagnosticsR\x0b\x64iagnostics\x12\x43\n\x0fterminal_access\x18\n \x01(\x0b\x32\x1a.google.protobuf.BoolValueR\x0eterminalAccess\x12:\n\x08\x61\x64\x61pters\x18\x0b \x03(\x0b\x32\x1e.v1.model.AdapterConfigurationR\x08\x61\x64\x61pters\x12,\n\x08rtc_info\x18\x0c \x01(\x0b\x32\x11.v1.model.RtcInfoR\x07rtcInfo\x1a\x37\n\tTagsEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value:\x02\x38\x01\"v\n\x14\x41\x64\x61pterConfiguration\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12\x12\n\x04name\x18\x02 \x01(\tR\x04name\x12\x17\n\x07\x66ile_id\x18\x03 \x01(\tR\x06\x66ileId\x12!\n\x0c\x65xec_command\x18\x04 \x01(\tR\x0b\x65xecCommand\"\x88\x02\n\x13TeleopConfiguration\x12G\n\x0bros_streams\x18\x01 \x03(\x0b\x32&.v1.model.TeleopRosStreamConfigurationR\nrosStreams\x12P\n\x0e\x63ustom_streams\x18\x02 \x03(\x0b\x32).v1.model.TeleopCustomStreamConfigurationR\rcustomStreams\x12V\n\x10hardware_streams\x18\x03 \x03(\x0b\x32+.v1.model.TeleopHardwareStreamConfigurationR\x0fhardwareStreams\"S\n\x1bPortForwardingConfiguration\x12\x34\n\x07\x65nabled\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.BoolValueR\x07\x65nabled\"\xcf\x02\n\x1cTeleopRosStreamConfiguration\x12\x1d\n\ntopic_name\x18\x01 \x01(\tR\ttopicName\x12\x35\n\ntopic_type\x18\x02 \x01(\x0e\x32\x16.v1.model.ROSTopicTypeR\ttopicType\x12(\n\x04mode\x18\x03 \x01(\x0e\x32\x14.v1.model.TeleopModeR\x04mode\x12!\n\x0c\x65ncode_video\x18\x04 \x01(\x08R\x0b\x65ncodeVideo\x12\x1f\n\x0b\x61udio_codec\x18\x05 \x01(\tR\naudioCodec\x12\x18\n\x07quality\x18\x06 \x01(\tR\x07quality\x12\x30\n\x14\x62\x61se_reference_frame\x18\x07 \x01(\tR\x12\x62\x61seReferenceFrame\x12\x1f\n\x0blocal_frame\x18\x08 \x01(\tR\nlocalFrame\"\x8a\x03\n!TeleopHardwareStreamConfiguration\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12&\n\x0frtc_stream_type\x18\x02 \x01(\tR\rrtcStreamType\x12(\n\x04mode\x18\x03 \x01(\x0e\x32\x14.v1.model.TeleopModeR\x04mode\x12#\n\rhw_descriptor\x18\x04 \x01(\tR\x0chwDescriptor\x12\x18\n\x07quality\x18\x05 \x01(\tR\x07quality\x12#\n\rhardware_type\x18\x06 \x01(\tR\x0chardwareType\x12\x30\n\x14rtsp_encoding_needed\x18\x07 \x01(\x08R\x12rtspEncodingNeeded\x12\x19\n\x08is_onvif\x18\x08 \x01(\x08R\x07isOnvif\x12&\n\x0fip_cam_username\x18\t \x01(\tR\ripCamUsername\x12&\n\x0fip_cam_password\x18\n \x01(\tR\ripCamPassword\"\xc4\x01\n\x1fTeleopCustomStreamConfiguration\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12&\n\x0frtc_stream_type\x18\x02 \x01(\tR\rrtcStreamType\x12(\n\x04mode\x18\x03 \x01(\x0e\x32\x14.v1.model.TeleopModeR\x04mode\x12!\n\x0c\x65ncode_video\x18\x04 \x01(\x08R\x0b\x65ncodeVideo\x12\x18\n\x07quality\x18\x05 \x01(\tR\x07quality\"\x7f\n\x16TelemetryConfiguration\x12\x37\n\x07streams\x18\x01 \x03(\x0b\x32\x1d.v1.model.StreamConfigurationR\x07streams\x12,\n\x03ros\x18\x02 \x01(\x0b\x32\x1a.v1.model.ROSConfigurationR\x03ros\"\xc6\x01\n\x18\x41pplicationConfiguration\x12\x65\n\x11\x63onfiguration_map\x18\x01 \x03(\x0b\x32\x38.v1.model.ApplicationConfiguration.ConfigurationMapEntryR\x10\x63onfigurationMap\x1a\x43\n\x15\x43onfigurationMapEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value:\x02\x38\x01\"\xc5\x01\n\x16ResourcesConfiguration\x12/\n\x04\x64isk\x18\x01 \x01(\x0b\x32\x1b.v1.model.DiskConfigurationR\x04\x64isk\x12J\n\x12stream_throttle_hz\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.DoubleValueR\x10streamThrottleHz\x12.\n\x13low_bandwidth_agent\x18\x03 \x01(\x08R\x11lowBandwidthAgent\"g\n\x11\x44iskConfiguration\x12\x1f\n\x0b\x62uffer_size\x18\x01 \x01(\x03R\nbufferSize\x12\x31\n\x15on_demand_buffer_size\x18\x02 \x01(\x03R\x12onDemandBufferSize\"K\n\x10ROSConfiguration\x12\x37\n\x18world_reference_frame_id\x18\x01 \x01(\tR\x15worldReferenceFrameId\"\xdd\x06\n\x13StreamConfiguration\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12;\n\x04tags\x18\x02 \x03(\x0b\x32\'.v1.model.StreamConfiguration.TagsEntryR\x04tags\x12\x31\n\tros_topic\x18\x03 \x01(\x0b\x32\x12.v1.model.ROSTopicH\x00R\x08rosTopic\x12\x46\n\x10ros_localization\x18\x04 \x01(\x0b\x32\x19.v1.model.ROSLocalizationH\x00R\x0frosLocalization\x12\x43\n\x0f\x64irectory_watch\x18\x05 \x01(\x0b\x32\x18.v1.model.DirectoryWatchH\x00R\x0e\x64irectoryWatch\x12\x31\n\tfile_tail\x18\x06 \x01(\x0b\x32\x12.v1.model.FileTailH\x00R\x08\x66ileTail\x12J\n\x12ros_transform_tree\x18\x07 \x01(\x0b\x32\x1a.v1.model.ROSTransformTreeH\x00R\x10rosTransformTree\x12*\n\x06\x63ustom\x18\t \x01(\x0b\x32\x10.v1.model.CustomH\x00R\x06\x63ustom\x12\x30\n\x08hardware\x18\n \x01(\x0b\x32\x12.v1.model.HardwareH\x00R\x08hardware\x12=\n\x0bthrottle_hz\x18\x08 \x01(\x0b\x32\x1c.google.protobuf.DoubleValueR\nthrottleHz\x12\x36\n\x08\x64isabled\x18\x13 \x01(\x0b\x32\x1a.google.protobuf.BoolValueR\x08\x64isabled\x12\x37\n\ton_demand\x18\x14 \x01(\x0b\x32\x1a.google.protobuf.BoolValueR\x08onDemand\x12\x44\n\ttransform\x18\x15 \x01(\x0b\x32&.v1.model.StreamTransformConfigurationR\ttransform\x12\x18\n\x07quality\x18\x16 \x01(\tR\x07quality\x1a\x37\n\tTagsEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value:\x02\x38\x01\x42\x0f\n\rconfiguration\"p\n\x1cStreamTransformConfiguration\x12P\n\x16video_encoding_enabled\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.BoolValueR\x14videoEncodingEnabled\"\x1e\n\x08\x42lobData\x12\x12\n\x04\x64\x61ta\x18\x01 \x01(\tR\x04\x64\x61ta\"\x8d\x01\n\x0b\x44iagnostics\x12;\n\x0breport_logs\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.BoolValueR\nreportLogs\x12\x41\n\x0ereport_metrics\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.BoolValueR\rreportMetrics\"\x08\n\x06\x43ustom\"\xa1\x02\n\x08Hardware\x12#\n\rhw_descriptor\x18\x01 \x01(\tR\x0chwDescriptor\x12.\n\x13\x61udio_hw_descriptor\x18\x03 \x01(\tR\x11\x61udioHwDescriptor\x12#\n\rhardware_type\x18\x04 \x01(\tR\x0chardwareType\x12\x30\n\x14rtsp_encoding_needed\x18\x05 \x01(\x08R\x12rtspEncodingNeeded\x12\x19\n\x08is_onvif\x18\x06 \x01(\x08R\x07isOnvif\x12&\n\x0fip_cam_username\x18\x07 \x01(\tR\ripCamUsername\x12&\n\x0fip_cam_password\x18\x08 \x01(\tR\ripCamPassword\"\xa0\x01\n\x0e\x44irectoryWatch\x12\x1c\n\tdirectory\x18\x01 \x01(\tR\tdirectory\x12\x1c\n\textension\x18\x02 \x01(\tR\textension\x12/\n\tfile_type\x18\x03 \x01(\x0e\x32\x12.v1.model.FileTypeR\x08\x66ileType\x12!\n\x0cremote_agent\x18\x04 \x01(\x08R\x0bremoteAgent\"\xaf\x01\n\x08\x46ileTail\x12\x1a\n\x08\x66ilename\x18\x01 \x01(\tR\x08\x66ilename\x12\x35\n\x0b\x66ile_format\x18\x02 \x01(\x0e\x32\x14.v1.model.FileFormatR\nfileFormat\x12\x19\n\x08time_key\x18\x03 \x01(\tR\x07timeKey\x12\x1f\n\x0btime_format\x18\x04 \x01(\tR\ntimeFormat\x12\x14\n\x05regex\x18\x05 \x01(\tR\x05regex\"}\n\x07RtcInfo\x12;\n\x1artc_ice_transport_policies\x18\x01 \x03(\tR\x17rtcIceTransportPolicies\x12\x35\n\x17rtc_ice_server_protocol\x18\x02 \x01(\tR\x14rtcIceServerProtocol*&\n\nTeleopMode\x12\x0b\n\x07\x43OMMAND\x10\x00\x12\x0b\n\x07OBSERVE\x10\x01*&\n\nFileFormat\x12\x0e\n\nPLAIN_TEXT\x10\x00\x12\x08\n\x04JSON\x10\x01*;\n\x08\x46ileType\x12\x08\n\x04\x46ILE\x10\x00\x12\t\n\x05IMAGE\x10\x01\x12\x0f\n\x0bPOINT_CLOUD\x10\x04\x12\t\n\x05VIDEO\x10\x05\x42+Z)github.com/FormantIO/genproto/go/v1/modelb\x06proto3'
   ,
   dependencies=[protos_dot_model_dot_v1_dot_ros__pb2.DESCRIPTOR,google_dot_protobuf_dot_wrappers__pb2.DESCRIPTOR,])
 
 _TELEOPMODE = _descriptor.EnumDescriptor(
   name='TeleopMode',
   full_name='v1.model.TeleopMode',
   filename=None,
@@ -42,16 +42,16 @@
       name='OBSERVE', index=1, number=1,
       serialized_options=None,
       type=None,
       create_key=_descriptor._internal_create_key),
   ],
   containing_type=None,
   serialized_options=None,
-  serialized_start=5504,
-  serialized_end=5542,
+  serialized_start=5677,
+  serialized_end=5715,
 )
 _sym_db.RegisterEnumDescriptor(_TELEOPMODE)
 
 TeleopMode = enum_type_wrapper.EnumTypeWrapper(_TELEOPMODE)
 _FILEFORMAT = _descriptor.EnumDescriptor(
   name='FileFormat',
   full_name='v1.model.FileFormat',
@@ -68,16 +68,16 @@
       name='JSON', index=1, number=1,
       serialized_options=None,
       type=None,
       create_key=_descriptor._internal_create_key),
   ],
   containing_type=None,
   serialized_options=None,
-  serialized_start=5544,
-  serialized_end=5582,
+  serialized_start=5717,
+  serialized_end=5755,
 )
 _sym_db.RegisterEnumDescriptor(_FILEFORMAT)
 
 FileFormat = enum_type_wrapper.EnumTypeWrapper(_FILEFORMAT)
 _FILETYPE = _descriptor.EnumDescriptor(
   name='FileType',
   full_name='v1.model.FileType',
@@ -104,16 +104,16 @@
       name='VIDEO', index=3, number=5,
       serialized_options=None,
       type=None,
       create_key=_descriptor._internal_create_key),
   ],
   containing_type=None,
   serialized_options=None,
-  serialized_start=5584,
-  serialized_end=5643,
+  serialized_start=5757,
+  serialized_end=5816,
 )
 _sym_db.RegisterEnumDescriptor(_FILETYPE)
 
 FileType = enum_type_wrapper.EnumTypeWrapper(_FILETYPE)
 COMMAND = 0
 OBSERVE = 1
 PLAIN_TEXT = 0
@@ -356,16 +356,16 @@
   ],
   serialized_options=b'8\001',
   is_extendable=False,
   syntax='proto3',
   extension_ranges=[],
   oneofs=[
   ],
-  serialized_start=1532,
-  serialized_end=1587,
+  serialized_start=1578,
+  serialized_end=1633,
 )
 
 _AGENTCONFIGURATIONDOCUMENT = _descriptor.Descriptor(
   name='AgentConfigurationDocument',
   full_name='v1.model.AgentConfigurationDocument',
   filename=None,
   file=DESCRIPTOR,
@@ -445,28 +445,35 @@
     _descriptor.FieldDescriptor(
       name='adapters', full_name='v1.model.AgentConfigurationDocument.adapters', index=10,
       number=11, type=11, cpp_type=10, label=3,
       has_default_value=False, default_value=[],
       message_type=None, enum_type=None, containing_type=None,
       is_extension=False, extension_scope=None,
       serialized_options=None, json_name='adapters', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
+    _descriptor.FieldDescriptor(
+      name='rtc_info', full_name='v1.model.AgentConfigurationDocument.rtc_info', index=11,
+      number=12, type=11, cpp_type=10, label=1,
+      has_default_value=False, default_value=None,
+      message_type=None, enum_type=None, containing_type=None,
+      is_extension=False, extension_scope=None,
+      serialized_options=None, json_name='rtcInfo', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
   ],
   extensions=[
   ],
   nested_types=[_AGENTCONFIGURATIONDOCUMENT_TAGSENTRY, ],
   enum_types=[
   ],
   serialized_options=None,
   is_extendable=False,
   syntax='proto3',
   extension_ranges=[],
   oneofs=[
   ],
   serialized_start=840,
-  serialized_end=1587,
+  serialized_end=1633,
 )
 
 
 _ADAPTERCONFIGURATION = _descriptor.Descriptor(
   name='AdapterConfiguration',
   full_name='v1.model.AdapterConfiguration',
   filename=None,
@@ -510,16 +517,16 @@
   ],
   serialized_options=None,
   is_extendable=False,
   syntax='proto3',
   extension_ranges=[],
   oneofs=[
   ],
-  serialized_start=1589,
-  serialized_end=1707,
+  serialized_start=1635,
+  serialized_end=1753,
 )
 
 
 _TELEOPCONFIGURATION = _descriptor.Descriptor(
   name='TeleopConfiguration',
   full_name='v1.model.TeleopConfiguration',
   filename=None,
@@ -556,16 +563,16 @@
   ],
   serialized_options=None,
   is_extendable=False,
   syntax='proto3',
   extension_ranges=[],
   oneofs=[
   ],
-  serialized_start=1710,
-  serialized_end=1974,
+  serialized_start=1756,
+  serialized_end=2020,
 )
 
 
 _PORTFORWARDINGCONFIGURATION = _descriptor.Descriptor(
   name='PortForwardingConfiguration',
   full_name='v1.model.PortForwardingConfiguration',
   filename=None,
@@ -588,16 +595,16 @@
   ],
   serialized_options=None,
   is_extendable=False,
   syntax='proto3',
   extension_ranges=[],
   oneofs=[
   ],
-  serialized_start=1976,
-  serialized_end=2059,
+  serialized_start=2022,
+  serialized_end=2105,
 )
 
 
 _TELEOPROSSTREAMCONFIGURATION = _descriptor.Descriptor(
   name='TeleopRosStreamConfiguration',
   full_name='v1.model.TeleopRosStreamConfiguration',
   filename=None,
@@ -669,16 +676,16 @@
   ],
   serialized_options=None,
   is_extendable=False,
   syntax='proto3',
   extension_ranges=[],
   oneofs=[
   ],
-  serialized_start=2062,
-  serialized_end=2397,
+  serialized_start=2108,
+  serialized_end=2443,
 )
 
 
 _TELEOPHARDWARESTREAMCONFIGURATION = _descriptor.Descriptor(
   name='TeleopHardwareStreamConfiguration',
   full_name='v1.model.TeleopHardwareStreamConfiguration',
   filename=None,
@@ -764,16 +771,16 @@
   ],
   serialized_options=None,
   is_extendable=False,
   syntax='proto3',
   extension_ranges=[],
   oneofs=[
   ],
-  serialized_start=2400,
-  serialized_end=2794,
+  serialized_start=2446,
+  serialized_end=2840,
 )
 
 
 _TELEOPCUSTOMSTREAMCONFIGURATION = _descriptor.Descriptor(
   name='TeleopCustomStreamConfiguration',
   full_name='v1.model.TeleopCustomStreamConfiguration',
   filename=None,
@@ -824,16 +831,16 @@
   ],
   serialized_options=None,
   is_extendable=False,
   syntax='proto3',
   extension_ranges=[],
   oneofs=[
   ],
-  serialized_start=2797,
-  serialized_end=2993,
+  serialized_start=2843,
+  serialized_end=3039,
 )
 
 
 _TELEMETRYCONFIGURATION = _descriptor.Descriptor(
   name='TelemetryConfiguration',
   full_name='v1.model.TelemetryConfiguration',
   filename=None,
@@ -863,16 +870,16 @@
   ],
   serialized_options=None,
   is_extendable=False,
   syntax='proto3',
   extension_ranges=[],
   oneofs=[
   ],
-  serialized_start=2995,
-  serialized_end=3122,
+  serialized_start=3041,
+  serialized_end=3168,
 )
 
 
 _APPLICATIONCONFIGURATION_CONFIGURATIONMAPENTRY = _descriptor.Descriptor(
   name='ConfigurationMapEntry',
   full_name='v1.model.ApplicationConfiguration.ConfigurationMapEntry',
   filename=None,
@@ -902,16 +909,16 @@
   ],
   serialized_options=b'8\001',
   is_extendable=False,
   syntax='proto3',
   extension_ranges=[],
   oneofs=[
   ],
-  serialized_start=3256,
-  serialized_end=3323,
+  serialized_start=3302,
+  serialized_end=3369,
 )
 
 _APPLICATIONCONFIGURATION = _descriptor.Descriptor(
   name='ApplicationConfiguration',
   full_name='v1.model.ApplicationConfiguration',
   filename=None,
   file=DESCRIPTOR,
@@ -933,16 +940,16 @@
   ],
   serialized_options=None,
   is_extendable=False,
   syntax='proto3',
   extension_ranges=[],
   oneofs=[
   ],
-  serialized_start=3125,
-  serialized_end=3323,
+  serialized_start=3171,
+  serialized_end=3369,
 )
 
 
 _RESOURCESCONFIGURATION = _descriptor.Descriptor(
   name='ResourcesConfiguration',
   full_name='v1.model.ResourcesConfiguration',
   filename=None,
@@ -979,16 +986,16 @@
   ],
   serialized_options=None,
   is_extendable=False,
   syntax='proto3',
   extension_ranges=[],
   oneofs=[
   ],
-  serialized_start=3326,
-  serialized_end=3523,
+  serialized_start=3372,
+  serialized_end=3569,
 )
 
 
 _DISKCONFIGURATION = _descriptor.Descriptor(
   name='DiskConfiguration',
   full_name='v1.model.DiskConfiguration',
   filename=None,
@@ -1018,16 +1025,16 @@
   ],
   serialized_options=None,
   is_extendable=False,
   syntax='proto3',
   extension_ranges=[],
   oneofs=[
   ],
-  serialized_start=3525,
-  serialized_end=3628,
+  serialized_start=3571,
+  serialized_end=3674,
 )
 
 
 _ROSCONFIGURATION = _descriptor.Descriptor(
   name='ROSConfiguration',
   full_name='v1.model.ROSConfiguration',
   filename=None,
@@ -1050,16 +1057,16 @@
   ],
   serialized_options=None,
   is_extendable=False,
   syntax='proto3',
   extension_ranges=[],
   oneofs=[
   ],
-  serialized_start=3630,
-  serialized_end=3705,
+  serialized_start=3676,
+  serialized_end=3751,
 )
 
 
 _STREAMCONFIGURATION_TAGSENTRY = _descriptor.Descriptor(
   name='TagsEntry',
   full_name='v1.model.StreamConfiguration.TagsEntry',
   filename=None,
@@ -1089,16 +1096,16 @@
   ],
   serialized_options=b'8\001',
   is_extendable=False,
   syntax='proto3',
   extension_ranges=[],
   oneofs=[
   ],
-  serialized_start=1532,
-  serialized_end=1587,
+  serialized_start=1578,
+  serialized_end=1633,
 )
 
 _STREAMCONFIGURATION = _descriptor.Descriptor(
   name='StreamConfiguration',
   full_name='v1.model.StreamConfiguration',
   filename=None,
   file=DESCRIPTOR,
@@ -1216,16 +1223,16 @@
   oneofs=[
     _descriptor.OneofDescriptor(
       name='configuration', full_name='v1.model.StreamConfiguration.configuration',
       index=0, containing_type=None,
       create_key=_descriptor._internal_create_key,
     fields=[]),
   ],
-  serialized_start=3708,
-  serialized_end=4569,
+  serialized_start=3754,
+  serialized_end=4615,
 )
 
 
 _STREAMTRANSFORMCONFIGURATION = _descriptor.Descriptor(
   name='StreamTransformConfiguration',
   full_name='v1.model.StreamTransformConfiguration',
   filename=None,
@@ -1248,16 +1255,16 @@
   ],
   serialized_options=None,
   is_extendable=False,
   syntax='proto3',
   extension_ranges=[],
   oneofs=[
   ],
-  serialized_start=4571,
-  serialized_end=4683,
+  serialized_start=4617,
+  serialized_end=4729,
 )
 
 
 _BLOBDATA = _descriptor.Descriptor(
   name='BlobData',
   full_name='v1.model.BlobData',
   filename=None,
@@ -1280,16 +1287,16 @@
   ],
   serialized_options=None,
   is_extendable=False,
   syntax='proto3',
   extension_ranges=[],
   oneofs=[
   ],
-  serialized_start=4685,
-  serialized_end=4715,
+  serialized_start=4731,
+  serialized_end=4761,
 )
 
 
 _DIAGNOSTICS = _descriptor.Descriptor(
   name='Diagnostics',
   full_name='v1.model.Diagnostics',
   filename=None,
@@ -1319,16 +1326,16 @@
   ],
   serialized_options=None,
   is_extendable=False,
   syntax='proto3',
   extension_ranges=[],
   oneofs=[
   ],
-  serialized_start=4718,
-  serialized_end=4859,
+  serialized_start=4764,
+  serialized_end=4905,
 )
 
 
 _CUSTOM = _descriptor.Descriptor(
   name='Custom',
   full_name='v1.model.Custom',
   filename=None,
@@ -1344,16 +1351,16 @@
   ],
   serialized_options=None,
   is_extendable=False,
   syntax='proto3',
   extension_ranges=[],
   oneofs=[
   ],
-  serialized_start=4861,
-  serialized_end=4869,
+  serialized_start=4907,
+  serialized_end=4915,
 )
 
 
 _HARDWARE = _descriptor.Descriptor(
   name='Hardware',
   full_name='v1.model.Hardware',
   filename=None,
@@ -1418,16 +1425,16 @@
   ],
   serialized_options=None,
   is_extendable=False,
   syntax='proto3',
   extension_ranges=[],
   oneofs=[
   ],
-  serialized_start=4872,
-  serialized_end=5161,
+  serialized_start=4918,
+  serialized_end=5207,
 )
 
 
 _DIRECTORYWATCH = _descriptor.Descriptor(
   name='DirectoryWatch',
   full_name='v1.model.DirectoryWatch',
   filename=None,
@@ -1471,16 +1478,16 @@
   ],
   serialized_options=None,
   is_extendable=False,
   syntax='proto3',
   extension_ranges=[],
   oneofs=[
   ],
-  serialized_start=5164,
-  serialized_end=5324,
+  serialized_start=5210,
+  serialized_end=5370,
 )
 
 
 _FILETAIL = _descriptor.Descriptor(
   name='FileTail',
   full_name='v1.model.FileTail',
   filename=None,
@@ -1531,16 +1538,55 @@
   ],
   serialized_options=None,
   is_extendable=False,
   syntax='proto3',
   extension_ranges=[],
   oneofs=[
   ],
-  serialized_start=5327,
-  serialized_end=5502,
+  serialized_start=5373,
+  serialized_end=5548,
+)
+
+
+_RTCINFO = _descriptor.Descriptor(
+  name='RtcInfo',
+  full_name='v1.model.RtcInfo',
+  filename=None,
+  file=DESCRIPTOR,
+  containing_type=None,
+  create_key=_descriptor._internal_create_key,
+  fields=[
+    _descriptor.FieldDescriptor(
+      name='rtc_ice_transport_policies', full_name='v1.model.RtcInfo.rtc_ice_transport_policies', index=0,
+      number=1, type=9, cpp_type=9, label=3,
+      has_default_value=False, default_value=[],
+      message_type=None, enum_type=None, containing_type=None,
+      is_extension=False, extension_scope=None,
+      serialized_options=None, json_name='rtcIceTransportPolicies', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
+    _descriptor.FieldDescriptor(
+      name='rtc_ice_server_protocol', full_name='v1.model.RtcInfo.rtc_ice_server_protocol', index=1,
+      number=2, type=9, cpp_type=9, label=1,
+      has_default_value=False, default_value=b"".decode('utf-8'),
+      message_type=None, enum_type=None, containing_type=None,
+      is_extension=False, extension_scope=None,
+      serialized_options=None, json_name='rtcIceServerProtocol', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
+  ],
+  extensions=[
+  ],
+  nested_types=[],
+  enum_types=[
+  ],
+  serialized_options=None,
+  is_extendable=False,
+  syntax='proto3',
+  extension_ranges=[],
+  oneofs=[
+  ],
+  serialized_start=5550,
+  serialized_end=5675,
 )
 
 _AGENTCONFIGURATIONSTORE.fields_by_name['configuration'].message_type = _AGENTCONFIGURATION
 _AGENTCONFIGURATIONSTORE.fields_by_name['feature_set'].message_type = _AGENTFEATURESET
 _AGENTCONFIGURATION.fields_by_name['document'].message_type = _AGENTCONFIGURATIONDOCUMENT
 _AGENTCONFIGURATIONDOCUMENT_TAGSENTRY.containing_type = _AGENTCONFIGURATIONDOCUMENT
 _AGENTCONFIGURATIONDOCUMENT.fields_by_name['tags'].message_type = _AGENTCONFIGURATIONDOCUMENT_TAGSENTRY
@@ -1549,14 +1595,15 @@
 _AGENTCONFIGURATIONDOCUMENT.fields_by_name['application'].message_type = _APPLICATIONCONFIGURATION
 _AGENTCONFIGURATIONDOCUMENT.fields_by_name['teleop'].message_type = _TELEOPCONFIGURATION
 _AGENTCONFIGURATIONDOCUMENT.fields_by_name['port_forwarding'].message_type = _PORTFORWARDINGCONFIGURATION
 _AGENTCONFIGURATIONDOCUMENT.fields_by_name['blob_data'].message_type = _BLOBDATA
 _AGENTCONFIGURATIONDOCUMENT.fields_by_name['diagnostics'].message_type = _DIAGNOSTICS
 _AGENTCONFIGURATIONDOCUMENT.fields_by_name['terminal_access'].message_type = google_dot_protobuf_dot_wrappers__pb2._BOOLVALUE
 _AGENTCONFIGURATIONDOCUMENT.fields_by_name['adapters'].message_type = _ADAPTERCONFIGURATION
+_AGENTCONFIGURATIONDOCUMENT.fields_by_name['rtc_info'].message_type = _RTCINFO
 _TELEOPCONFIGURATION.fields_by_name['ros_streams'].message_type = _TELEOPROSSTREAMCONFIGURATION
 _TELEOPCONFIGURATION.fields_by_name['custom_streams'].message_type = _TELEOPCUSTOMSTREAMCONFIGURATION
 _TELEOPCONFIGURATION.fields_by_name['hardware_streams'].message_type = _TELEOPHARDWARESTREAMCONFIGURATION
 _PORTFORWARDINGCONFIGURATION.fields_by_name['enabled'].message_type = google_dot_protobuf_dot_wrappers__pb2._BOOLVALUE
 _TELEOPROSSTREAMCONFIGURATION.fields_by_name['topic_type'].enum_type = protos_dot_model_dot_v1_dot_ros__pb2._ROSTOPICTYPE
 _TELEOPROSSTREAMCONFIGURATION.fields_by_name['mode'].enum_type = _TELEOPMODE
 _TELEOPHARDWARESTREAMCONFIGURATION.fields_by_name['mode'].enum_type = _TELEOPMODE
@@ -1625,14 +1672,15 @@
 DESCRIPTOR.message_types_by_name['StreamTransformConfiguration'] = _STREAMTRANSFORMCONFIGURATION
 DESCRIPTOR.message_types_by_name['BlobData'] = _BLOBDATA
 DESCRIPTOR.message_types_by_name['Diagnostics'] = _DIAGNOSTICS
 DESCRIPTOR.message_types_by_name['Custom'] = _CUSTOM
 DESCRIPTOR.message_types_by_name['Hardware'] = _HARDWARE
 DESCRIPTOR.message_types_by_name['DirectoryWatch'] = _DIRECTORYWATCH
 DESCRIPTOR.message_types_by_name['FileTail'] = _FILETAIL
+DESCRIPTOR.message_types_by_name['RtcInfo'] = _RTCINFO
 DESCRIPTOR.enum_types_by_name['TeleopMode'] = _TELEOPMODE
 DESCRIPTOR.enum_types_by_name['FileFormat'] = _FILEFORMAT
 DESCRIPTOR.enum_types_by_name['FileType'] = _FILETYPE
 _sym_db.RegisterFileDescriptor(DESCRIPTOR)
 
 AgentConfigurationStore = _reflection.GeneratedProtocolMessageType('AgentConfigurationStore', (_message.Message,), {
   'DESCRIPTOR' : _AGENTCONFIGURATIONSTORE,
@@ -1815,13 +1863,20 @@
 FileTail = _reflection.GeneratedProtocolMessageType('FileTail', (_message.Message,), {
   'DESCRIPTOR' : _FILETAIL,
   '__module__' : 'protos.model.v1.config_pb2'
   # @@protoc_insertion_point(class_scope:v1.model.FileTail)
   })
 _sym_db.RegisterMessage(FileTail)
 
+RtcInfo = _reflection.GeneratedProtocolMessageType('RtcInfo', (_message.Message,), {
+  'DESCRIPTOR' : _RTCINFO,
+  '__module__' : 'protos.model.v1.config_pb2'
+  # @@protoc_insertion_point(class_scope:v1.model.RtcInfo)
+  })
+_sym_db.RegisterMessage(RtcInfo)
+
 
 DESCRIPTOR._options = None
 _AGENTCONFIGURATIONDOCUMENT_TAGSENTRY._options = None
 _APPLICATIONCONFIGURATION_CONFIGURATIONMAPENTRY._options = None
 _STREAMCONFIGURATION_TAGSENTRY._options = None
 # @@protoc_insertion_point(module_scope)
```

### Comparing `formant-1.99.10/formant/protos/model/v1/datapoint_pb2.py` & `formant-1.99.25/formant/protos/model/v1/datapoint_pb2.py`

 * *Files identical despite different names*

### Comparing `formant-1.99.10/formant/protos/model/v1/event_pb2.py` & `formant-1.99.25/formant/protos/model/v1/event_pb2.py`

 * *Files identical despite different names*

### Comparing `formant-1.99.10/formant/protos/model/v1/file_pb2.py` & `formant-1.99.25/formant/protos/model/v1/file_pb2.py`

 * *Files identical despite different names*

### Comparing `formant-1.99.10/formant/protos/model/v1/health_pb2.py` & `formant-1.99.25/formant/protos/model/v1/health_pb2.py`

 * *Files identical despite different names*

### Comparing `formant-1.99.10/formant/protos/model/v1/intervention_pb2.py` & `formant-1.99.25/formant/protos/model/v1/intervention_pb2.py`

 * *Files identical despite different names*

### Comparing `formant-1.99.10/formant/protos/model/v1/math_pb2.py` & `formant-1.99.25/formant/protos/model/v1/math_pb2.py`

 * *Files identical despite different names*

### Comparing `formant-1.99.10/formant/protos/model/v1/media_pb2.py` & `formant-1.99.25/formant/protos/model/v1/media_pb2.py`

 * *Files identical despite different names*

### Comparing `formant-1.99.10/formant/protos/model/v1/navigation_pb2.py` & `formant-1.99.25/formant/protos/model/v1/navigation_pb2.py`

 * *Files identical despite different names*

### Comparing `formant-1.99.10/formant/protos/model/v1/ros_pb2.py` & `formant-1.99.25/formant/protos/model/v1/ros_pb2.py`

 * *Files identical despite different names*

### Comparing `formant-1.99.10/formant/protos/model/v1/text_pb2.py` & `formant-1.99.25/formant/protos/model/v1/text_pb2.py`

 * *Files identical despite different names*

### Comparing `formant-1.99.10/formant/sdk/agent/adapter_utils/json_schema_validator.py` & `formant-1.99.25/formant/sdk/agent/adapter_utils/json_schema_validator.py`

 * *Files identical despite different names*

### Comparing `formant-1.99.10/formant/sdk/agent/v1/cancellable_stream_thread.py` & `formant-1.99.25/formant/sdk/agent/v1/cancellable_stream_thread.py`

 * *Files identical despite different names*

### Comparing `formant-1.99.10/formant/sdk/agent/v1/client.py` & `formant-1.99.25/formant/sdk/agent/v1/client.py`

 * *Files identical despite different names*

### Comparing `formant-1.99.10/formant/sdk/agent/v1/exceptions.py` & `formant-1.99.25/formant/sdk/agent/v1/exceptions.py`

 * *Files identical despite different names*

### Comparing `formant-1.99.10/formant/sdk/agent/v1/localization/localization_manager.py` & `formant-1.99.25/formant/sdk/agent/v1/localization/localization_manager.py`

 * *Files identical despite different names*

### Comparing `formant-1.99.10/formant/sdk/agent/v1/localization/types/map.py` & `formant-1.99.25/formant/sdk/agent/v1/localization/types/map.py`

 * *Files identical despite different names*

### Comparing `formant-1.99.10/formant/sdk/agent/v1/localization/types/odometry.py` & `formant-1.99.25/formant/sdk/agent/v1/localization/types/odometry.py`

 * *Files identical despite different names*

### Comparing `formant-1.99.10/formant/sdk/agent/v1/localization/types/path.py` & `formant-1.99.25/formant/sdk/agent/v1/localization/types/path.py`

 * *Files identical despite different names*

### Comparing `formant-1.99.10/formant/sdk/agent/v1/localization/types/point_cloud/external.py` & `formant-1.99.25/formant/sdk/agent/v1/localization/types/point_cloud/external.py`

 * *Files identical despite different names*

### Comparing `formant-1.99.10/formant/sdk/agent/v1/localization/types/point_cloud/internal_types.py` & `formant-1.99.25/formant/sdk/agent/v1/localization/types/point_cloud/internal_types.py`

 * *Files identical despite different names*

### Comparing `formant-1.99.10/formant/sdk/agent/v1/localization/types/point_cloud/laserscan.py` & `formant-1.99.25/formant/sdk/agent/v1/localization/types/point_cloud/laserscan.py`

 * *Files identical despite different names*

### Comparing `formant-1.99.10/formant/sdk/agent/v1/localization/types/point_cloud/numpy_compat.py` & `formant-1.99.25/formant/sdk/agent/v1/localization/types/point_cloud/numpy_compat.py`

 * *Files identical despite different names*

### Comparing `formant-1.99.10/formant/sdk/agent/v1/localization/types/point_cloud/point_cloud2.py` & `formant-1.99.25/formant/sdk/agent/v1/localization/types/point_cloud/point_cloud2.py`

 * *Files identical despite different names*

### Comparing `formant-1.99.10/formant/sdk/agent/v1/localization/types/quaternion.py` & `formant-1.99.25/formant/sdk/agent/v1/localization/types/quaternion.py`

 * *Files identical despite different names*

### Comparing `formant-1.99.10/formant/sdk/agent/v1/localization/types/transform.py` & `formant-1.99.25/formant/sdk/agent/v1/localization/types/transform.py`

 * *Files identical despite different names*

### Comparing `formant-1.99.10/formant/sdk/agent/v1/localization/types/twist.py` & `formant-1.99.25/formant/sdk/agent/v1/localization/types/twist.py`

 * *Files identical despite different names*

### Comparing `formant-1.99.10/formant/sdk/agent/v1/localization/types/vector3.py` & `formant-1.99.25/formant/sdk/agent/v1/localization/types/vector3.py`

 * *Files identical despite different names*

### Comparing `formant-1.99.10/formant/sdk/agent/v1/localization/utils.py` & `formant-1.99.25/formant/sdk/agent/v1/localization/utils.py`

 * *Files identical despite different names*

### Comparing `formant-1.99.10/formant/sdk/cloud/v1/client.py` & `formant-1.99.25/formant/sdk/cloud/v1/client.py`

 * *Files identical despite different names*

### Comparing `formant-1.99.10/formant/sdk/cloud/v1/types/annotation.py` & `formant-1.99.25/formant/sdk/cloud/v1/types/annotation.py`

 * *Files identical despite different names*

### Comparing `formant-1.99.10/formant/sdk/cloud/v1/types/annotation_field.py` & `formant-1.99.25/formant/sdk/cloud/v1/types/annotation_field.py`

 * *Files identical despite different names*

### Comparing `formant-1.99.10/formant/sdk/cloud/v1/types/annotation_template.py` & `formant-1.99.25/formant/sdk/cloud/v1/types/annotation_template.py`

 * *Files identical despite different names*

### Comparing `formant-1.99.10/formant/sdk/cloud/v1/types/annotation_template_list_result.py` & `formant-1.99.25/formant/sdk/cloud/v1/types/annotation_template_list_result.py`

 * *Files identical despite different names*

### Comparing `formant-1.99.10/formant/sdk/utils/get_message_path_value.py` & `formant-1.99.25/formant/sdk/utils/get_message_path_value.py`

 * *Files identical despite different names*

### Comparing `formant-1.99.10/formant.egg-info/SOURCES.txt` & `formant-1.99.25/formant.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `formant-1.99.10/setup.py` & `formant-1.99.25/setup.py`

 * *Files 2% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 import setuptools
 
 with open("README.md", "r") as fh:
     long_description = fh.read()
 
 setuptools.setup(
     name="formant",
-    version="1.99.10",
+    version="1.99.25",
     author="Formant",
     author_email="eng@formant.io",
     description="Formant python package",
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://formant.io",
     packages=setuptools.find_packages(),
```

