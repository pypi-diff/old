# Comparing `tmp/pylzy-1.8.7.tar.gz` & `tmp/pylzy-1.8.8.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "pylzy-1.8.7.tar", last modified: Wed Apr  5 15:27:49 2023, max compression
+gzip compressed data, was "pylzy-1.8.8.tar", last modified: Thu Apr  6 10:38:36 2023, max compression
```

## Comparing `pylzy-1.8.7.tar` & `pylzy-1.8.8.tar`

### file list

```diff
@@ -1,159 +1,159 @@
-drwxrwxr-x   0 ubuntu    (1000) ubuntu    (1001)        0 2023-04-05 15:27:49.697297 pylzy-1.8.7/
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)      578 2023-04-05 15:27:31.000000 pylzy-1.8.7/LICENSE
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)       58 2023-04-05 14:45:02.000000 pylzy-1.8.7/MANIFEST.in
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)     2910 2023-04-05 15:27:49.697297 pylzy-1.8.7/PKG-INFO
-drwxrwxr-x   0 ubuntu    (1000) ubuntu    (1001)        0 2023-04-05 15:27:49.665296 pylzy-1.8.7/ai/
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)        0 2023-04-05 15:27:47.000000 pylzy-1.8.7/ai/__init__.py
-drwxrwxr-x   0 ubuntu    (1000) ubuntu    (1001)        0 2023-04-05 15:27:49.665296 pylzy-1.8.7/ai/lzy/
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)        0 2023-04-05 15:27:47.000000 pylzy-1.8.7/ai/lzy/__init__.py
-drwxrwxr-x   0 ubuntu    (1000) ubuntu    (1001)        0 2023-04-05 15:27:49.665296 pylzy-1.8.7/ai/lzy/v1/
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)        0 2023-04-05 15:27:47.000000 pylzy-1.8.7/ai/lzy/v1/__init__.py
-drwxrwxr-x   0 ubuntu    (1000) ubuntu    (1001)        0 2023-04-05 15:27:49.673296 pylzy-1.8.7/ai/lzy/v1/common/
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)        0 2023-04-05 15:27:47.000000 pylzy-1.8.7/ai/lzy/v1/common/__init__.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)     5714 2023-04-05 15:27:46.000000 pylzy-1.8.7/ai/lzy/v1/common/data_scheme_pb2.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)     1909 2023-04-05 15:27:46.000000 pylzy-1.8.7/ai/lzy/v1/common/data_scheme_pb2.pyi
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)      159 2023-04-05 15:27:46.000000 pylzy-1.8.7/ai/lzy/v1/common/data_scheme_pb2_grpc.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)    18939 2023-04-05 15:27:46.000000 pylzy-1.8.7/ai/lzy/v1/common/env_pb2.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)     7171 2023-04-05 15:27:46.000000 pylzy-1.8.7/ai/lzy/v1/common/env_pb2.pyi
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)      159 2023-04-05 15:27:46.000000 pylzy-1.8.7/ai/lzy/v1/common/env_pb2_grpc.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)    13859 2023-04-05 15:27:46.000000 pylzy-1.8.7/ai/lzy/v1/common/operation_pb2.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)     4971 2023-04-05 15:27:46.000000 pylzy-1.8.7/ai/lzy/v1/common/operation_pb2.pyi
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)      159 2023-04-05 15:27:46.000000 pylzy-1.8.7/ai/lzy/v1/common/operation_pb2_grpc.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)    14306 2023-04-05 15:27:46.000000 pylzy-1.8.7/ai/lzy/v1/common/slot_pb2.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)     6471 2023-04-05 15:27:46.000000 pylzy-1.8.7/ai/lzy/v1/common/slot_pb2.pyi
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)      159 2023-04-05 15:27:46.000000 pylzy-1.8.7/ai/lzy/v1/common/slot_pb2_grpc.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)     8161 2023-04-05 15:27:46.000000 pylzy-1.8.7/ai/lzy/v1/common/storage_pb2.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)     2622 2023-04-05 15:27:46.000000 pylzy-1.8.7/ai/lzy/v1/common/storage_pb2.pyi
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)      159 2023-04-05 15:27:46.000000 pylzy-1.8.7/ai/lzy/v1/common/storage_pb2_grpc.py
-drwxrwxr-x   0 ubuntu    (1000) ubuntu    (1001)        0 2023-04-05 15:27:49.689297 pylzy-1.8.7/ai/lzy/v1/long_running/
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)        0 2023-04-05 15:27:47.000000 pylzy-1.8.7/ai/lzy/v1/long_running/__init__.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)    17745 2023-04-05 15:27:46.000000 pylzy-1.8.7/ai/lzy/v1/long_running/operation_pb2.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)     5386 2023-04-05 15:27:46.000000 pylzy-1.8.7/ai/lzy/v1/long_running/operation_pb2.pyi
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)     6359 2023-04-05 15:27:46.000000 pylzy-1.8.7/ai/lzy/v1/long_running/operation_pb2_grpc.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)     3623 2023-04-05 15:27:46.000000 pylzy-1.8.7/ai/lzy/v1/long_running/option_pb2.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)     1670 2023-04-05 15:27:46.000000 pylzy-1.8.7/ai/lzy/v1/long_running/option_pb2.pyi
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)      159 2023-04-05 15:27:46.000000 pylzy-1.8.7/ai/lzy/v1/long_running/option_pb2_grpc.py
-drwxrwxr-x   0 ubuntu    (1000) ubuntu    (1001)        0 2023-04-05 15:27:49.689297 pylzy-1.8.7/ai/lzy/v1/validation/
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)        0 2023-04-05 15:27:47.000000 pylzy-1.8.7/ai/lzy/v1/validation/__init__.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)     1827 2023-04-05 15:27:46.000000 pylzy-1.8.7/ai/lzy/v1/validation/validation_pb2.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)      774 2023-04-05 15:27:46.000000 pylzy-1.8.7/ai/lzy/v1/validation/validation_pb2.pyi
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)      159 2023-04-05 15:27:46.000000 pylzy-1.8.7/ai/lzy/v1/validation/validation_pb2_grpc.py
-drwxrwxr-x   0 ubuntu    (1000) ubuntu    (1001)        0 2023-04-05 15:27:49.689297 pylzy-1.8.7/ai/lzy/v1/whiteboard/
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)        0 2023-04-05 15:27:47.000000 pylzy-1.8.7/ai/lzy/v1/whiteboard/__init__.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)    13566 2023-04-05 15:27:47.000000 pylzy-1.8.7/ai/lzy/v1/whiteboard/whiteboard_pb2.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)     5339 2023-04-05 15:27:47.000000 pylzy-1.8.7/ai/lzy/v1/whiteboard/whiteboard_pb2.pyi
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)      159 2023-04-05 15:27:47.000000 pylzy-1.8.7/ai/lzy/v1/whiteboard/whiteboard_pb2_grpc.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)    15568 2023-04-05 15:27:47.000000 pylzy-1.8.7/ai/lzy/v1/whiteboard/whiteboard_service_pb2.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)     5226 2023-04-05 15:27:47.000000 pylzy-1.8.7/ai/lzy/v1/whiteboard/whiteboard_service_pb2.pyi
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)     8512 2023-04-05 15:27:47.000000 pylzy-1.8.7/ai/lzy/v1/whiteboard/whiteboard_service_pb2_grpc.py
-drwxrwxr-x   0 ubuntu    (1000) ubuntu    (1001)        0 2023-04-05 15:27:49.693297 pylzy-1.8.7/ai/lzy/v1/workflow/
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)        0 2023-04-05 15:27:47.000000 pylzy-1.8.7/ai/lzy/v1/workflow/__init__.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)    33793 2023-04-05 15:27:47.000000 pylzy-1.8.7/ai/lzy/v1/workflow/workflow_pb2.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)    13601 2023-04-05 15:27:47.000000 pylzy-1.8.7/ai/lzy/v1/workflow/workflow_pb2.pyi
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)      159 2023-04-05 15:27:47.000000 pylzy-1.8.7/ai/lzy/v1/workflow/workflow_pb2_grpc.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)     7758 2023-04-05 15:27:47.000000 pylzy-1.8.7/ai/lzy/v1/workflow/workflow_private_service_pb2.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)     1826 2023-04-05 15:27:47.000000 pylzy-1.8.7/ai/lzy/v1/workflow/workflow_private_service_pb2.pyi
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)     4993 2023-04-05 15:27:47.000000 pylzy-1.8.7/ai/lzy/v1/workflow/workflow_private_service_pb2_grpc.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)    48368 2023-04-05 15:27:47.000000 pylzy-1.8.7/ai/lzy/v1/workflow/workflow_service_pb2.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)    14903 2023-04-05 15:27:47.000000 pylzy-1.8.7/ai/lzy/v1/workflow/workflow_service_pb2.pyi
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)    18006 2023-04-05 15:27:47.000000 pylzy-1.8.7/ai/lzy/v1/workflow/workflow_service_pb2_grpc.py
-drwxrwxr-x   0 ubuntu    (1000) ubuntu    (1001)        0 2023-04-05 15:27:49.649296 pylzy-1.8.7/google/
-drwxrwxr-x   0 ubuntu    (1000) ubuntu    (1001)        0 2023-04-05 15:27:49.693297 pylzy-1.8.7/google/protobuf/
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)     2765 2023-04-05 15:27:46.000000 pylzy-1.8.7/google/protobuf/any_pb2.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)      159 2023-04-05 15:27:46.000000 pylzy-1.8.7/google/protobuf/any_pb2_grpc.py
-drwxrwxr-x   0 ubuntu    (1000) ubuntu    (1001)        0 2023-04-05 15:27:49.693297 pylzy-1.8.7/google/rpc/
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)     3456 2023-04-05 15:27:46.000000 pylzy-1.8.7/google/rpc/status_pb2.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)      159 2023-04-05 15:27:46.000000 pylzy-1.8.7/google/rpc/status_pb2_grpc.py
-drwxrwxr-x   0 ubuntu    (1000) ubuntu    (1001)        0 2023-04-05 15:27:49.693297 pylzy-1.8.7/lzy/
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)       33 2023-04-05 14:45:02.000000 pylzy-1.8.7/lzy/__init__.py
-drwxrwxr-x   0 ubuntu    (1000) ubuntu    (1001)        0 2023-04-05 15:27:49.693297 pylzy-1.8.7/lzy/api/
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)        0 2023-04-05 14:45:02.000000 pylzy-1.8.7/lzy/api/__init__.py
-drwxrwxr-x   0 ubuntu    (1000) ubuntu    (1001)        0 2023-04-05 15:27:49.693297 pylzy-1.8.7/lzy/api/v1/
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)    12906 2023-04-05 14:45:02.000000 pylzy-1.8.7/lzy/api/v1/__init__.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)     9929 2023-04-05 14:45:02.000000 pylzy-1.8.7/lzy/api/v1/call.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)      746 2023-04-05 14:45:02.000000 pylzy-1.8.7/lzy/api/v1/entry_index.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)     2624 2023-04-05 14:45:02.000000 pylzy-1.8.7/lzy/api/v1/env.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)      287 2023-04-05 14:45:02.000000 pylzy-1.8.7/lzy/api/v1/exceptions.py
-drwxrwxr-x   0 ubuntu    (1000) ubuntu    (1001)        0 2023-04-05 15:27:49.693297 pylzy-1.8.7/lzy/api/v1/local/
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)        0 2023-04-05 14:45:02.000000 pylzy-1.8.7/lzy/api/v1/local/__init__.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)     6570 2023-04-05 14:45:02.000000 pylzy-1.8.7/lzy/api/v1/local/runtime.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)     1945 2023-04-05 14:45:02.000000 pylzy-1.8.7/lzy/api/v1/provisioning.py
-drwxrwxr-x   0 ubuntu    (1000) ubuntu    (1001)        0 2023-04-05 15:27:49.693297 pylzy-1.8.7/lzy/api/v1/remote/
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)        0 2023-04-05 14:45:02.000000 pylzy-1.8.7/lzy/api/v1/remote/__init__.py
-drwxrwxr-x   0 ubuntu    (1000) ubuntu    (1001)        0 2023-04-05 15:27:49.693297 pylzy-1.8.7/lzy/api/v1/remote/model/
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)        0 2023-04-05 14:45:02.000000 pylzy-1.8.7/lzy/api/v1/remote/model/__init__.py
-drwxrwxr-x   0 ubuntu    (1000) ubuntu    (1001)        0 2023-04-05 15:27:49.693297 pylzy-1.8.7/lzy/api/v1/remote/model/converter/
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)       55 2023-04-05 14:45:02.000000 pylzy-1.8.7/lzy/api/v1/remote/model/converter/__init__.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)     2079 2023-04-05 14:45:02.000000 pylzy-1.8.7/lzy/api/v1/remote/model/converter/storage_creds.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)    16650 2023-04-05 14:45:02.000000 pylzy-1.8.7/lzy/api/v1/remote/runtime.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)     8888 2023-04-05 14:45:02.000000 pylzy-1.8.7/lzy/api/v1/remote/workflow_service_client.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)      879 2023-04-05 14:45:02.000000 pylzy-1.8.7/lzy/api/v1/runtime.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)     1001 2023-04-05 14:45:02.000000 pylzy-1.8.7/lzy/api/v1/signatures.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)     6832 2023-04-05 14:45:02.000000 pylzy-1.8.7/lzy/api/v1/snapshot.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)     6337 2023-04-05 14:45:02.000000 pylzy-1.8.7/lzy/api/v1/startup.py
-drwxrwxr-x   0 ubuntu    (1000) ubuntu    (1001)        0 2023-04-05 15:27:49.697297 pylzy-1.8.7/lzy/api/v1/utils/
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)        0 2023-04-05 14:45:02.000000 pylzy-1.8.7/lzy/api/v1/utils/__init__.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)     1042 2023-04-05 14:45:02.000000 pylzy-1.8.7/lzy/api/v1/utils/conda.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)     1054 2023-04-05 14:45:02.000000 pylzy-1.8.7/lzy/api/v1/utils/files.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)     1252 2023-04-05 14:45:02.000000 pylzy-1.8.7/lzy/api/v1/utils/hashing.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)      566 2023-04-05 14:45:02.000000 pylzy-1.8.7/lzy/api/v1/utils/packages.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)      271 2023-04-05 14:45:02.000000 pylzy-1.8.7/lzy/api/v1/utils/pickle.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)     2272 2023-04-05 14:45:02.000000 pylzy-1.8.7/lzy/api/v1/utils/proxy_adapter.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)     2388 2023-04-05 14:45:02.000000 pylzy-1.8.7/lzy/api/v1/utils/types.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)      156 2023-04-05 14:45:02.000000 pylzy-1.8.7/lzy/api/v1/utils/validation.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)     8195 2023-04-05 14:45:02.000000 pylzy-1.8.7/lzy/api/v1/whiteboards.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)     9046 2023-04-05 14:45:02.000000 pylzy-1.8.7/lzy/api/v1/workflow.py
-drwxrwxr-x   0 ubuntu    (1000) ubuntu    (1001)        0 2023-04-05 15:27:49.697297 pylzy-1.8.7/lzy/injections/
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)        0 2023-04-05 14:45:02.000000 pylzy-1.8.7/lzy/injections/__init__.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)     2365 2023-04-05 14:45:02.000000 pylzy-1.8.7/lzy/injections/catboost.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)      362 2023-04-05 14:45:02.000000 pylzy-1.8.7/lzy/injections/extensions.py
-drwxrwxr-x   0 ubuntu    (1000) ubuntu    (1001)        0 2023-04-05 15:27:49.697297 pylzy-1.8.7/lzy/logs/
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)        0 2023-04-05 14:45:02.000000 pylzy-1.8.7/lzy/logs/__init__.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)     2251 2023-04-05 14:45:02.000000 pylzy-1.8.7/lzy/logs/config.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)      632 2023-04-05 14:45:02.000000 pylzy-1.8.7/lzy/logs/logging.yml
-drwxrwxr-x   0 ubuntu    (1000) ubuntu    (1001)        0 2023-04-05 15:27:49.697297 pylzy-1.8.7/lzy/proxy/
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)       50 2023-04-05 14:45:02.000000 pylzy-1.8.7/lzy/proxy/__init__.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)     6609 2023-04-05 14:45:02.000000 pylzy-1.8.7/lzy/proxy/automagic.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)      489 2023-04-05 14:45:02.000000 pylzy-1.8.7/lzy/proxy/result.py
-drwxrwxr-x   0 ubuntu    (1000) ubuntu    (1001)        0 2023-04-05 15:27:49.697297 pylzy-1.8.7/lzy/py_env/
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)        0 2023-04-05 14:45:02.000000 pylzy-1.8.7/lzy/py_env/__init__.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)      366 2023-04-05 14:45:02.000000 pylzy-1.8.7/lzy/py_env/api.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)     8117 2023-04-05 14:45:02.000000 pylzy-1.8.7/lzy/py_env/py_env_provider.py
-drwxrwxr-x   0 ubuntu    (1000) ubuntu    (1001)        0 2023-04-05 15:27:49.697297 pylzy-1.8.7/lzy/serialization/
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)        0 2023-04-05 14:45:02.000000 pylzy-1.8.7/lzy/serialization/__init__.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)     3075 2023-04-05 14:45:02.000000 pylzy-1.8.7/lzy/serialization/file.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)     3120 2023-04-05 14:45:02.000000 pylzy-1.8.7/lzy/serialization/registry.py
-drwxrwxr-x   0 ubuntu    (1000) ubuntu    (1001)        0 2023-04-05 15:27:49.697297 pylzy-1.8.7/lzy/storage/
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)        0 2023-04-05 14:45:02.000000 pylzy-1.8.7/lzy/storage/__init__.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)     2846 2023-04-05 14:45:02.000000 pylzy-1.8.7/lzy/storage/api.py
-drwxrwxr-x   0 ubuntu    (1000) ubuntu    (1001)        0 2023-04-05 15:27:49.697297 pylzy-1.8.7/lzy/storage/async_/
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)     1572 2023-04-05 14:45:02.000000 pylzy-1.8.7/lzy/storage/async_/__init__.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)     4227 2023-04-05 14:45:02.000000 pylzy-1.8.7/lzy/storage/async_/azure.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)     1896 2023-04-05 14:45:02.000000 pylzy-1.8.7/lzy/storage/async_/fs.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)     2978 2023-04-05 14:45:02.000000 pylzy-1.8.7/lzy/storage/async_/s3.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)     2206 2023-04-05 14:45:02.000000 pylzy-1.8.7/lzy/storage/registry.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)      653 2023-04-05 14:45:02.000000 pylzy-1.8.7/lzy/storage/url.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)      128 2023-04-05 14:45:02.000000 pylzy-1.8.7/lzy/types.py
-drwxrwxr-x   0 ubuntu    (1000) ubuntu    (1001)        0 2023-04-05 15:27:49.697297 pylzy-1.8.7/lzy/utils/
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)        0 2023-04-05 14:45:02.000000 pylzy-1.8.7/lzy/utils/__init__.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)     1227 2023-04-05 14:45:02.000000 pylzy-1.8.7/lzy/utils/event_loop.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)     8406 2023-04-05 14:45:02.000000 pylzy-1.8.7/lzy/utils/grpc.py
-drwxrwxr-x   0 ubuntu    (1000) ubuntu    (1001)        0 2023-04-05 15:27:49.697297 pylzy-1.8.7/lzy/version/
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)        6 2023-04-05 14:45:02.000000 pylzy-1.8.7/lzy/version/version
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)      129 2023-04-05 14:45:02.000000 pylzy-1.8.7/lzy/version.py
-drwxrwxr-x   0 ubuntu    (1000) ubuntu    (1001)        0 2023-04-05 15:27:49.697297 pylzy-1.8.7/lzy/whiteboards/
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)        0 2023-04-05 14:45:02.000000 pylzy-1.8.7/lzy/whiteboards/__init__.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)     1892 2023-04-05 14:45:02.000000 pylzy-1.8.7/lzy/whiteboards/api.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)    10064 2023-04-05 14:45:02.000000 pylzy-1.8.7/lzy/whiteboards/index.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)     4477 2023-04-05 14:45:02.000000 pylzy-1.8.7/lzy/whiteboards/wrapper.py
-drwxrwxr-x   0 ubuntu    (1000) ubuntu    (1001)        0 2023-04-05 15:27:49.697297 pylzy-1.8.7/pylzy.egg-info/
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)     2910 2023-04-05 15:27:48.000000 pylzy-1.8.7/pylzy.egg-info/PKG-INFO
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)     3744 2023-04-05 15:27:49.000000 pylzy-1.8.7/pylzy.egg-info/SOURCES.txt
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)        1 2023-04-05 15:27:48.000000 pylzy-1.8.7/pylzy.egg-info/dependency_links.txt
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)      433 2023-04-05 15:27:49.000000 pylzy-1.8.7/pylzy.egg-info/requires.txt
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)      402 2023-04-05 15:27:49.000000 pylzy-1.8.7/pylzy.egg-info/top_level.txt
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)      497 2023-04-05 14:45:02.000000 pylzy-1.8.7/pyproject.toml
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)     2496 2023-04-05 15:27:31.000000 pylzy-1.8.7/readme.md
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)      433 2023-04-05 14:45:02.000000 pylzy-1.8.7/requirements.txt
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)       67 2023-04-05 15:27:49.701297 pylzy-1.8.7/setup.cfg
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)     1870 2023-04-05 14:45:02.000000 pylzy-1.8.7/setup.py
+drwxrwxr-x   0 ubuntu    (1000) ubuntu    (1001)        0 2023-04-06 10:38:36.337395 pylzy-1.8.8/
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)      578 2023-04-06 10:38:19.000000 pylzy-1.8.8/LICENSE
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)       58 2023-04-06 10:13:20.000000 pylzy-1.8.8/MANIFEST.in
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)     2910 2023-04-06 10:38:36.337395 pylzy-1.8.8/PKG-INFO
+drwxrwxr-x   0 ubuntu    (1000) ubuntu    (1001)        0 2023-04-06 10:38:36.309394 pylzy-1.8.8/ai/
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)        0 2023-04-06 10:38:34.000000 pylzy-1.8.8/ai/__init__.py
+drwxrwxr-x   0 ubuntu    (1000) ubuntu    (1001)        0 2023-04-06 10:38:36.309394 pylzy-1.8.8/ai/lzy/
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)        0 2023-04-06 10:38:34.000000 pylzy-1.8.8/ai/lzy/__init__.py
+drwxrwxr-x   0 ubuntu    (1000) ubuntu    (1001)        0 2023-04-06 10:38:36.309394 pylzy-1.8.8/ai/lzy/v1/
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)        0 2023-04-06 10:38:34.000000 pylzy-1.8.8/ai/lzy/v1/__init__.py
+drwxrwxr-x   0 ubuntu    (1000) ubuntu    (1001)        0 2023-04-06 10:38:36.317395 pylzy-1.8.8/ai/lzy/v1/common/
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)        0 2023-04-06 10:38:34.000000 pylzy-1.8.8/ai/lzy/v1/common/__init__.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)     5714 2023-04-06 10:38:33.000000 pylzy-1.8.8/ai/lzy/v1/common/data_scheme_pb2.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)     1909 2023-04-06 10:38:33.000000 pylzy-1.8.8/ai/lzy/v1/common/data_scheme_pb2.pyi
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)      159 2023-04-06 10:38:33.000000 pylzy-1.8.8/ai/lzy/v1/common/data_scheme_pb2_grpc.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)    18939 2023-04-06 10:38:33.000000 pylzy-1.8.8/ai/lzy/v1/common/env_pb2.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)     7171 2023-04-06 10:38:33.000000 pylzy-1.8.8/ai/lzy/v1/common/env_pb2.pyi
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)      159 2023-04-06 10:38:33.000000 pylzy-1.8.8/ai/lzy/v1/common/env_pb2_grpc.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)    13859 2023-04-06 10:38:33.000000 pylzy-1.8.8/ai/lzy/v1/common/operation_pb2.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)     4971 2023-04-06 10:38:33.000000 pylzy-1.8.8/ai/lzy/v1/common/operation_pb2.pyi
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)      159 2023-04-06 10:38:33.000000 pylzy-1.8.8/ai/lzy/v1/common/operation_pb2_grpc.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)    14306 2023-04-06 10:38:33.000000 pylzy-1.8.8/ai/lzy/v1/common/slot_pb2.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)     6471 2023-04-06 10:38:33.000000 pylzy-1.8.8/ai/lzy/v1/common/slot_pb2.pyi
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)      159 2023-04-06 10:38:33.000000 pylzy-1.8.8/ai/lzy/v1/common/slot_pb2_grpc.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)     8161 2023-04-06 10:38:33.000000 pylzy-1.8.8/ai/lzy/v1/common/storage_pb2.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)     2622 2023-04-06 10:38:33.000000 pylzy-1.8.8/ai/lzy/v1/common/storage_pb2.pyi
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)      159 2023-04-06 10:38:33.000000 pylzy-1.8.8/ai/lzy/v1/common/storage_pb2_grpc.py
+drwxrwxr-x   0 ubuntu    (1000) ubuntu    (1001)        0 2023-04-06 10:38:36.329395 pylzy-1.8.8/ai/lzy/v1/long_running/
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)        0 2023-04-06 10:38:34.000000 pylzy-1.8.8/ai/lzy/v1/long_running/__init__.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)    17745 2023-04-06 10:38:33.000000 pylzy-1.8.8/ai/lzy/v1/long_running/operation_pb2.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)     5386 2023-04-06 10:38:33.000000 pylzy-1.8.8/ai/lzy/v1/long_running/operation_pb2.pyi
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)     6359 2023-04-06 10:38:33.000000 pylzy-1.8.8/ai/lzy/v1/long_running/operation_pb2_grpc.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)     3623 2023-04-06 10:38:33.000000 pylzy-1.8.8/ai/lzy/v1/long_running/option_pb2.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)     1670 2023-04-06 10:38:33.000000 pylzy-1.8.8/ai/lzy/v1/long_running/option_pb2.pyi
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)      159 2023-04-06 10:38:33.000000 pylzy-1.8.8/ai/lzy/v1/long_running/option_pb2_grpc.py
+drwxrwxr-x   0 ubuntu    (1000) ubuntu    (1001)        0 2023-04-06 10:38:36.329395 pylzy-1.8.8/ai/lzy/v1/validation/
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)        0 2023-04-06 10:38:34.000000 pylzy-1.8.8/ai/lzy/v1/validation/__init__.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)     1827 2023-04-06 10:38:33.000000 pylzy-1.8.8/ai/lzy/v1/validation/validation_pb2.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)      774 2023-04-06 10:38:33.000000 pylzy-1.8.8/ai/lzy/v1/validation/validation_pb2.pyi
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)      159 2023-04-06 10:38:33.000000 pylzy-1.8.8/ai/lzy/v1/validation/validation_pb2_grpc.py
+drwxrwxr-x   0 ubuntu    (1000) ubuntu    (1001)        0 2023-04-06 10:38:36.329395 pylzy-1.8.8/ai/lzy/v1/whiteboard/
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)        0 2023-04-06 10:38:34.000000 pylzy-1.8.8/ai/lzy/v1/whiteboard/__init__.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)    13566 2023-04-06 10:38:34.000000 pylzy-1.8.8/ai/lzy/v1/whiteboard/whiteboard_pb2.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)     5339 2023-04-06 10:38:34.000000 pylzy-1.8.8/ai/lzy/v1/whiteboard/whiteboard_pb2.pyi
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)      159 2023-04-06 10:38:34.000000 pylzy-1.8.8/ai/lzy/v1/whiteboard/whiteboard_pb2_grpc.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)    15568 2023-04-06 10:38:34.000000 pylzy-1.8.8/ai/lzy/v1/whiteboard/whiteboard_service_pb2.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)     5226 2023-04-06 10:38:34.000000 pylzy-1.8.8/ai/lzy/v1/whiteboard/whiteboard_service_pb2.pyi
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)     8512 2023-04-06 10:38:34.000000 pylzy-1.8.8/ai/lzy/v1/whiteboard/whiteboard_service_pb2_grpc.py
+drwxrwxr-x   0 ubuntu    (1000) ubuntu    (1001)        0 2023-04-06 10:38:36.333395 pylzy-1.8.8/ai/lzy/v1/workflow/
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)        0 2023-04-06 10:38:34.000000 pylzy-1.8.8/ai/lzy/v1/workflow/__init__.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)    33793 2023-04-06 10:38:34.000000 pylzy-1.8.8/ai/lzy/v1/workflow/workflow_pb2.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)    13601 2023-04-06 10:38:34.000000 pylzy-1.8.8/ai/lzy/v1/workflow/workflow_pb2.pyi
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)      159 2023-04-06 10:38:34.000000 pylzy-1.8.8/ai/lzy/v1/workflow/workflow_pb2_grpc.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)     7758 2023-04-06 10:38:34.000000 pylzy-1.8.8/ai/lzy/v1/workflow/workflow_private_service_pb2.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)     1826 2023-04-06 10:38:34.000000 pylzy-1.8.8/ai/lzy/v1/workflow/workflow_private_service_pb2.pyi
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)     4993 2023-04-06 10:38:34.000000 pylzy-1.8.8/ai/lzy/v1/workflow/workflow_private_service_pb2_grpc.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)    48368 2023-04-06 10:38:34.000000 pylzy-1.8.8/ai/lzy/v1/workflow/workflow_service_pb2.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)    14903 2023-04-06 10:38:34.000000 pylzy-1.8.8/ai/lzy/v1/workflow/workflow_service_pb2.pyi
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)    18006 2023-04-06 10:38:34.000000 pylzy-1.8.8/ai/lzy/v1/workflow/workflow_service_pb2_grpc.py
+drwxrwxr-x   0 ubuntu    (1000) ubuntu    (1001)        0 2023-04-06 10:38:36.305395 pylzy-1.8.8/google/
+drwxrwxr-x   0 ubuntu    (1000) ubuntu    (1001)        0 2023-04-06 10:38:36.333395 pylzy-1.8.8/google/protobuf/
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)     2765 2023-04-06 10:38:33.000000 pylzy-1.8.8/google/protobuf/any_pb2.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)      159 2023-04-06 10:38:33.000000 pylzy-1.8.8/google/protobuf/any_pb2_grpc.py
+drwxrwxr-x   0 ubuntu    (1000) ubuntu    (1001)        0 2023-04-06 10:38:36.333395 pylzy-1.8.8/google/rpc/
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)     3456 2023-04-06 10:38:33.000000 pylzy-1.8.8/google/rpc/status_pb2.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)      159 2023-04-06 10:38:33.000000 pylzy-1.8.8/google/rpc/status_pb2_grpc.py
+drwxrwxr-x   0 ubuntu    (1000) ubuntu    (1001)        0 2023-04-06 10:38:36.333395 pylzy-1.8.8/lzy/
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)       33 2023-04-06 10:13:20.000000 pylzy-1.8.8/lzy/__init__.py
+drwxrwxr-x   0 ubuntu    (1000) ubuntu    (1001)        0 2023-04-06 10:38:36.333395 pylzy-1.8.8/lzy/api/
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)        0 2023-04-06 10:13:20.000000 pylzy-1.8.8/lzy/api/__init__.py
+drwxrwxr-x   0 ubuntu    (1000) ubuntu    (1001)        0 2023-04-06 10:38:36.333395 pylzy-1.8.8/lzy/api/v1/
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)    12950 2023-04-06 10:13:20.000000 pylzy-1.8.8/lzy/api/v1/__init__.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)     9929 2023-04-06 10:13:20.000000 pylzy-1.8.8/lzy/api/v1/call.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)      746 2023-04-06 10:13:20.000000 pylzy-1.8.8/lzy/api/v1/entry_index.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)     2624 2023-04-06 10:13:20.000000 pylzy-1.8.8/lzy/api/v1/env.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)      287 2023-04-06 10:13:20.000000 pylzy-1.8.8/lzy/api/v1/exceptions.py
+drwxrwxr-x   0 ubuntu    (1000) ubuntu    (1001)        0 2023-04-06 10:38:36.333395 pylzy-1.8.8/lzy/api/v1/local/
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)        0 2023-04-06 10:13:20.000000 pylzy-1.8.8/lzy/api/v1/local/__init__.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)     6570 2023-04-06 10:13:20.000000 pylzy-1.8.8/lzy/api/v1/local/runtime.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)     1945 2023-04-06 10:13:20.000000 pylzy-1.8.8/lzy/api/v1/provisioning.py
+drwxrwxr-x   0 ubuntu    (1000) ubuntu    (1001)        0 2023-04-06 10:38:36.333395 pylzy-1.8.8/lzy/api/v1/remote/
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)        0 2023-04-06 10:13:20.000000 pylzy-1.8.8/lzy/api/v1/remote/__init__.py
+drwxrwxr-x   0 ubuntu    (1000) ubuntu    (1001)        0 2023-04-06 10:38:36.333395 pylzy-1.8.8/lzy/api/v1/remote/model/
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)        0 2023-04-06 10:13:20.000000 pylzy-1.8.8/lzy/api/v1/remote/model/__init__.py
+drwxrwxr-x   0 ubuntu    (1000) ubuntu    (1001)        0 2023-04-06 10:38:36.333395 pylzy-1.8.8/lzy/api/v1/remote/model/converter/
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)       55 2023-04-06 10:13:20.000000 pylzy-1.8.8/lzy/api/v1/remote/model/converter/__init__.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)     2079 2023-04-06 10:13:20.000000 pylzy-1.8.8/lzy/api/v1/remote/model/converter/storage_creds.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)    16650 2023-04-06 10:13:20.000000 pylzy-1.8.8/lzy/api/v1/remote/runtime.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)     8888 2023-04-06 10:13:20.000000 pylzy-1.8.8/lzy/api/v1/remote/workflow_service_client.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)      879 2023-04-06 10:13:20.000000 pylzy-1.8.8/lzy/api/v1/runtime.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)     1001 2023-04-06 10:13:20.000000 pylzy-1.8.8/lzy/api/v1/signatures.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)     6832 2023-04-06 10:13:20.000000 pylzy-1.8.8/lzy/api/v1/snapshot.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)     6337 2023-04-06 10:13:20.000000 pylzy-1.8.8/lzy/api/v1/startup.py
+drwxrwxr-x   0 ubuntu    (1000) ubuntu    (1001)        0 2023-04-06 10:38:36.333395 pylzy-1.8.8/lzy/api/v1/utils/
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)        0 2023-04-06 10:13:20.000000 pylzy-1.8.8/lzy/api/v1/utils/__init__.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)     1042 2023-04-06 10:13:20.000000 pylzy-1.8.8/lzy/api/v1/utils/conda.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)     1054 2023-04-06 10:13:20.000000 pylzy-1.8.8/lzy/api/v1/utils/files.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)     1252 2023-04-06 10:13:20.000000 pylzy-1.8.8/lzy/api/v1/utils/hashing.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)      566 2023-04-06 10:13:20.000000 pylzy-1.8.8/lzy/api/v1/utils/packages.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)      271 2023-04-06 10:13:20.000000 pylzy-1.8.8/lzy/api/v1/utils/pickle.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)     2272 2023-04-06 10:13:20.000000 pylzy-1.8.8/lzy/api/v1/utils/proxy_adapter.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)     2388 2023-04-06 10:13:20.000000 pylzy-1.8.8/lzy/api/v1/utils/types.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)      156 2023-04-06 10:13:20.000000 pylzy-1.8.8/lzy/api/v1/utils/validation.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)     8195 2023-04-06 10:13:20.000000 pylzy-1.8.8/lzy/api/v1/whiteboards.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)     9046 2023-04-06 10:13:20.000000 pylzy-1.8.8/lzy/api/v1/workflow.py
+drwxrwxr-x   0 ubuntu    (1000) ubuntu    (1001)        0 2023-04-06 10:38:36.337395 pylzy-1.8.8/lzy/injections/
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)        0 2023-04-06 10:13:20.000000 pylzy-1.8.8/lzy/injections/__init__.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)     2365 2023-04-06 10:13:20.000000 pylzy-1.8.8/lzy/injections/catboost.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)      362 2023-04-06 10:13:20.000000 pylzy-1.8.8/lzy/injections/extensions.py
+drwxrwxr-x   0 ubuntu    (1000) ubuntu    (1001)        0 2023-04-06 10:38:36.337395 pylzy-1.8.8/lzy/logs/
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)        0 2023-04-06 10:13:20.000000 pylzy-1.8.8/lzy/logs/__init__.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)     2251 2023-04-06 10:13:20.000000 pylzy-1.8.8/lzy/logs/config.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)      632 2023-04-06 10:13:20.000000 pylzy-1.8.8/lzy/logs/logging.yml
+drwxrwxr-x   0 ubuntu    (1000) ubuntu    (1001)        0 2023-04-06 10:38:36.337395 pylzy-1.8.8/lzy/proxy/
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)       50 2023-04-06 10:13:20.000000 pylzy-1.8.8/lzy/proxy/__init__.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)     6609 2023-04-06 10:13:20.000000 pylzy-1.8.8/lzy/proxy/automagic.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)      489 2023-04-06 10:13:20.000000 pylzy-1.8.8/lzy/proxy/result.py
+drwxrwxr-x   0 ubuntu    (1000) ubuntu    (1001)        0 2023-04-06 10:38:36.337395 pylzy-1.8.8/lzy/py_env/
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)        0 2023-04-06 10:13:20.000000 pylzy-1.8.8/lzy/py_env/__init__.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)      366 2023-04-06 10:13:20.000000 pylzy-1.8.8/lzy/py_env/api.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)     8117 2023-04-06 10:13:20.000000 pylzy-1.8.8/lzy/py_env/py_env_provider.py
+drwxrwxr-x   0 ubuntu    (1000) ubuntu    (1001)        0 2023-04-06 10:38:36.337395 pylzy-1.8.8/lzy/serialization/
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)        0 2023-04-06 10:13:20.000000 pylzy-1.8.8/lzy/serialization/__init__.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)     3075 2023-04-06 10:13:20.000000 pylzy-1.8.8/lzy/serialization/file.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)     3120 2023-04-06 10:13:20.000000 pylzy-1.8.8/lzy/serialization/registry.py
+drwxrwxr-x   0 ubuntu    (1000) ubuntu    (1001)        0 2023-04-06 10:38:36.337395 pylzy-1.8.8/lzy/storage/
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)        0 2023-04-06 10:13:20.000000 pylzy-1.8.8/lzy/storage/__init__.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)     2846 2023-04-06 10:13:20.000000 pylzy-1.8.8/lzy/storage/api.py
+drwxrwxr-x   0 ubuntu    (1000) ubuntu    (1001)        0 2023-04-06 10:38:36.337395 pylzy-1.8.8/lzy/storage/async_/
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)     1572 2023-04-06 10:13:20.000000 pylzy-1.8.8/lzy/storage/async_/__init__.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)     4227 2023-04-06 10:13:20.000000 pylzy-1.8.8/lzy/storage/async_/azure.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)     1896 2023-04-06 10:13:20.000000 pylzy-1.8.8/lzy/storage/async_/fs.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)     2978 2023-04-06 10:13:20.000000 pylzy-1.8.8/lzy/storage/async_/s3.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)     2206 2023-04-06 10:13:20.000000 pylzy-1.8.8/lzy/storage/registry.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)      653 2023-04-06 10:13:20.000000 pylzy-1.8.8/lzy/storage/url.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)      128 2023-04-06 10:13:20.000000 pylzy-1.8.8/lzy/types.py
+drwxrwxr-x   0 ubuntu    (1000) ubuntu    (1001)        0 2023-04-06 10:38:36.337395 pylzy-1.8.8/lzy/utils/
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)        0 2023-04-06 10:13:20.000000 pylzy-1.8.8/lzy/utils/__init__.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)     1227 2023-04-06 10:13:20.000000 pylzy-1.8.8/lzy/utils/event_loop.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)     8406 2023-04-06 10:13:20.000000 pylzy-1.8.8/lzy/utils/grpc.py
+drwxrwxr-x   0 ubuntu    (1000) ubuntu    (1001)        0 2023-04-06 10:38:36.337395 pylzy-1.8.8/lzy/version/
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)        6 2023-04-06 10:13:20.000000 pylzy-1.8.8/lzy/version/version
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)      129 2023-04-06 10:13:20.000000 pylzy-1.8.8/lzy/version.py
+drwxrwxr-x   0 ubuntu    (1000) ubuntu    (1001)        0 2023-04-06 10:38:36.337395 pylzy-1.8.8/lzy/whiteboards/
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)        0 2023-04-06 10:13:20.000000 pylzy-1.8.8/lzy/whiteboards/__init__.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)     1892 2023-04-06 10:13:20.000000 pylzy-1.8.8/lzy/whiteboards/api.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)    10064 2023-04-06 10:13:20.000000 pylzy-1.8.8/lzy/whiteboards/index.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)     4477 2023-04-06 10:13:20.000000 pylzy-1.8.8/lzy/whiteboards/wrapper.py
+drwxrwxr-x   0 ubuntu    (1000) ubuntu    (1001)        0 2023-04-06 10:38:36.337395 pylzy-1.8.8/pylzy.egg-info/
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)     2910 2023-04-06 10:38:35.000000 pylzy-1.8.8/pylzy.egg-info/PKG-INFO
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)     3744 2023-04-06 10:38:36.000000 pylzy-1.8.8/pylzy.egg-info/SOURCES.txt
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)        1 2023-04-06 10:38:35.000000 pylzy-1.8.8/pylzy.egg-info/dependency_links.txt
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)      433 2023-04-06 10:38:36.000000 pylzy-1.8.8/pylzy.egg-info/requires.txt
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)      402 2023-04-06 10:38:36.000000 pylzy-1.8.8/pylzy.egg-info/top_level.txt
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)      497 2023-04-06 10:13:20.000000 pylzy-1.8.8/pyproject.toml
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)     2496 2023-04-06 10:38:19.000000 pylzy-1.8.8/readme.md
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)      433 2023-04-06 10:13:20.000000 pylzy-1.8.8/requirements.txt
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)       67 2023-04-06 10:38:36.337395 pylzy-1.8.8/setup.cfg
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1001)     1870 2023-04-06 10:13:20.000000 pylzy-1.8.8/setup.py
```

### Comparing `pylzy-1.8.7/LICENSE` & `pylzy-1.8.8/LICENSE`

 * *Files identical despite different names*

### Comparing `pylzy-1.8.7/PKG-INFO` & `pylzy-1.8.8/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: pylzy
-Version: 1.8.7
+Version: 1.8.8
 Summary: UNKNOWN
 Author: ʎzy developers
 License: LICENSE
 Platform: UNKNOWN
 Classifier: Programming Language :: Python :: 3.7
 Classifier: Programming Language :: Python :: 3.8
 Classifier: Programming Language :: Python :: 3.9
```

### Comparing `pylzy-1.8.7/ai/lzy/v1/common/data_scheme_pb2.py` & `pylzy-1.8.8/ai/lzy/v1/common/data_scheme_pb2.py`

 * *Files identical despite different names*

### Comparing `pylzy-1.8.7/ai/lzy/v1/common/data_scheme_pb2.pyi` & `pylzy-1.8.8/ai/lzy/v1/common/data_scheme_pb2.pyi`

 * *Files identical despite different names*

### Comparing `pylzy-1.8.7/ai/lzy/v1/common/env_pb2.py` & `pylzy-1.8.8/ai/lzy/v1/common/env_pb2.py`

 * *Files identical despite different names*

### Comparing `pylzy-1.8.7/ai/lzy/v1/common/env_pb2.pyi` & `pylzy-1.8.8/ai/lzy/v1/common/env_pb2.pyi`

 * *Files identical despite different names*

### Comparing `pylzy-1.8.7/ai/lzy/v1/common/operation_pb2.py` & `pylzy-1.8.8/ai/lzy/v1/common/operation_pb2.py`

 * *Files identical despite different names*

### Comparing `pylzy-1.8.7/ai/lzy/v1/common/operation_pb2.pyi` & `pylzy-1.8.8/ai/lzy/v1/common/operation_pb2.pyi`

 * *Files identical despite different names*

### Comparing `pylzy-1.8.7/ai/lzy/v1/common/slot_pb2.py` & `pylzy-1.8.8/ai/lzy/v1/common/slot_pb2.py`

 * *Files identical despite different names*

### Comparing `pylzy-1.8.7/ai/lzy/v1/common/slot_pb2.pyi` & `pylzy-1.8.8/ai/lzy/v1/common/slot_pb2.pyi`

 * *Files identical despite different names*

### Comparing `pylzy-1.8.7/ai/lzy/v1/common/storage_pb2.py` & `pylzy-1.8.8/ai/lzy/v1/common/storage_pb2.py`

 * *Files identical despite different names*

### Comparing `pylzy-1.8.7/ai/lzy/v1/common/storage_pb2.pyi` & `pylzy-1.8.8/ai/lzy/v1/common/storage_pb2.pyi`

 * *Files identical despite different names*

### Comparing `pylzy-1.8.7/ai/lzy/v1/long_running/operation_pb2.py` & `pylzy-1.8.8/ai/lzy/v1/long_running/operation_pb2.py`

 * *Files identical despite different names*

### Comparing `pylzy-1.8.7/ai/lzy/v1/long_running/operation_pb2.pyi` & `pylzy-1.8.8/ai/lzy/v1/long_running/operation_pb2.pyi`

 * *Files identical despite different names*

### Comparing `pylzy-1.8.7/ai/lzy/v1/long_running/operation_pb2_grpc.py` & `pylzy-1.8.8/ai/lzy/v1/long_running/operation_pb2_grpc.py`

 * *Files identical despite different names*

### Comparing `pylzy-1.8.7/ai/lzy/v1/long_running/option_pb2.py` & `pylzy-1.8.8/ai/lzy/v1/long_running/option_pb2.py`

 * *Files identical despite different names*

### Comparing `pylzy-1.8.7/ai/lzy/v1/long_running/option_pb2.pyi` & `pylzy-1.8.8/ai/lzy/v1/long_running/option_pb2.pyi`

 * *Files identical despite different names*

### Comparing `pylzy-1.8.7/ai/lzy/v1/validation/validation_pb2.py` & `pylzy-1.8.8/ai/lzy/v1/validation/validation_pb2.py`

 * *Files identical despite different names*

### Comparing `pylzy-1.8.7/ai/lzy/v1/validation/validation_pb2.pyi` & `pylzy-1.8.8/ai/lzy/v1/validation/validation_pb2.pyi`

 * *Files identical despite different names*

### Comparing `pylzy-1.8.7/ai/lzy/v1/whiteboard/whiteboard_pb2.py` & `pylzy-1.8.8/ai/lzy/v1/whiteboard/whiteboard_pb2.py`

 * *Files identical despite different names*

### Comparing `pylzy-1.8.7/ai/lzy/v1/whiteboard/whiteboard_pb2.pyi` & `pylzy-1.8.8/ai/lzy/v1/whiteboard/whiteboard_pb2.pyi`

 * *Files identical despite different names*

### Comparing `pylzy-1.8.7/ai/lzy/v1/whiteboard/whiteboard_service_pb2.py` & `pylzy-1.8.8/ai/lzy/v1/whiteboard/whiteboard_service_pb2.py`

 * *Files identical despite different names*

### Comparing `pylzy-1.8.7/ai/lzy/v1/whiteboard/whiteboard_service_pb2.pyi` & `pylzy-1.8.8/ai/lzy/v1/whiteboard/whiteboard_service_pb2.pyi`

 * *Files identical despite different names*

### Comparing `pylzy-1.8.7/ai/lzy/v1/whiteboard/whiteboard_service_pb2_grpc.py` & `pylzy-1.8.8/ai/lzy/v1/whiteboard/whiteboard_service_pb2_grpc.py`

 * *Files identical despite different names*

### Comparing `pylzy-1.8.7/ai/lzy/v1/workflow/workflow_pb2.py` & `pylzy-1.8.8/ai/lzy/v1/workflow/workflow_pb2.py`

 * *Files identical despite different names*

### Comparing `pylzy-1.8.7/ai/lzy/v1/workflow/workflow_pb2.pyi` & `pylzy-1.8.8/ai/lzy/v1/workflow/workflow_pb2.pyi`

 * *Files identical despite different names*

### Comparing `pylzy-1.8.7/ai/lzy/v1/workflow/workflow_private_service_pb2.py` & `pylzy-1.8.8/ai/lzy/v1/workflow/workflow_private_service_pb2.py`

 * *Files identical despite different names*

### Comparing `pylzy-1.8.7/ai/lzy/v1/workflow/workflow_private_service_pb2.pyi` & `pylzy-1.8.8/ai/lzy/v1/workflow/workflow_private_service_pb2.pyi`

 * *Files identical despite different names*

### Comparing `pylzy-1.8.7/ai/lzy/v1/workflow/workflow_private_service_pb2_grpc.py` & `pylzy-1.8.8/ai/lzy/v1/workflow/workflow_private_service_pb2_grpc.py`

 * *Files identical despite different names*

### Comparing `pylzy-1.8.7/ai/lzy/v1/workflow/workflow_service_pb2.py` & `pylzy-1.8.8/ai/lzy/v1/workflow/workflow_service_pb2.py`

 * *Files identical despite different names*

### Comparing `pylzy-1.8.7/ai/lzy/v1/workflow/workflow_service_pb2.pyi` & `pylzy-1.8.8/ai/lzy/v1/workflow/workflow_service_pb2.pyi`

 * *Files identical despite different names*

### Comparing `pylzy-1.8.7/ai/lzy/v1/workflow/workflow_service_pb2_grpc.py` & `pylzy-1.8.8/ai/lzy/v1/workflow/workflow_service_pb2_grpc.py`

 * *Files identical despite different names*

### Comparing `pylzy-1.8.7/google/protobuf/any_pb2.py` & `pylzy-1.8.8/google/protobuf/any_pb2.py`

 * *Files identical despite different names*

### Comparing `pylzy-1.8.7/google/rpc/status_pb2.py` & `pylzy-1.8.8/google/rpc/status_pb2.py`

 * *Files identical despite different names*

### Comparing `pylzy-1.8.7/lzy/api/v1/__init__.py` & `pylzy-1.8.8/lzy/api/v1/__init__.py`

 * *Files 1% similar despite different names*

```diff
@@ -262,15 +262,16 @@
         if docker_only and docker_image is None:
             raise ValueError("docker_only is set, but docker image is not set")
 
         provisioning = provisioning.override(Provisioning(cpu_type, cpu_count, gpu_type, gpu_count, ram_size_gb))
         provisioning.validate()
 
         # it is important to detect py env before registering lazy calls to avoid materialization of them
-        namespace = inspect.stack()[1].frame.f_globals
+        frame = inspect.stack()[1].frame
+        namespace = {**frame.f_globals, **frame.f_locals}
         auto_py_env: PyEnv = self.__env_provider.provide(namespace)
 
         libraries = {} if not libraries else libraries
         local_modules_path = auto_py_env.local_modules_path if not local_modules_path else local_modules_path
         env = env.override(
             Env(python_version, libraries, conda_yaml_path, docker_image, docker_pull_policy, local_modules_path,
                 docker_only=docker_only, env_variables=env_variables, docker_credentials=docker_credentials)
```

### Comparing `pylzy-1.8.7/lzy/api/v1/call.py` & `pylzy-1.8.8/lzy/api/v1/call.py`

 * *Files identical despite different names*

### Comparing `pylzy-1.8.7/lzy/api/v1/entry_index.py` & `pylzy-1.8.8/lzy/api/v1/entry_index.py`

 * *Files identical despite different names*

### Comparing `pylzy-1.8.7/lzy/api/v1/env.py` & `pylzy-1.8.8/lzy/api/v1/env.py`

 * *Files identical despite different names*

### Comparing `pylzy-1.8.7/lzy/api/v1/local/runtime.py` & `pylzy-1.8.8/lzy/api/v1/local/runtime.py`

 * *Files identical despite different names*

### Comparing `pylzy-1.8.7/lzy/api/v1/provisioning.py` & `pylzy-1.8.8/lzy/api/v1/provisioning.py`

 * *Files identical despite different names*

### Comparing `pylzy-1.8.7/lzy/api/v1/remote/model/converter/storage_creds.py` & `pylzy-1.8.8/lzy/api/v1/remote/model/converter/storage_creds.py`

 * *Files identical despite different names*

### Comparing `pylzy-1.8.7/lzy/api/v1/remote/runtime.py` & `pylzy-1.8.8/lzy/api/v1/remote/runtime.py`

 * *Files identical despite different names*

### Comparing `pylzy-1.8.7/lzy/api/v1/remote/workflow_service_client.py` & `pylzy-1.8.8/lzy/api/v1/remote/workflow_service_client.py`

 * *Files identical despite different names*

### Comparing `pylzy-1.8.7/lzy/api/v1/runtime.py` & `pylzy-1.8.8/lzy/api/v1/runtime.py`

 * *Files identical despite different names*

### Comparing `pylzy-1.8.7/lzy/api/v1/signatures.py` & `pylzy-1.8.8/lzy/api/v1/signatures.py`

 * *Files identical despite different names*

### Comparing `pylzy-1.8.7/lzy/api/v1/snapshot.py` & `pylzy-1.8.8/lzy/api/v1/snapshot.py`

 * *Files identical despite different names*

### Comparing `pylzy-1.8.7/lzy/api/v1/startup.py` & `pylzy-1.8.8/lzy/api/v1/startup.py`

 * *Files identical despite different names*

### Comparing `pylzy-1.8.7/lzy/api/v1/utils/conda.py` & `pylzy-1.8.8/lzy/api/v1/utils/conda.py`

 * *Files identical despite different names*

### Comparing `pylzy-1.8.7/lzy/api/v1/utils/files.py` & `pylzy-1.8.8/lzy/api/v1/utils/files.py`

 * *Files identical despite different names*

### Comparing `pylzy-1.8.7/lzy/api/v1/utils/hashing.py` & `pylzy-1.8.8/lzy/api/v1/utils/hashing.py`

 * *Files identical despite different names*

### Comparing `pylzy-1.8.7/lzy/api/v1/utils/packages.py` & `pylzy-1.8.8/lzy/api/v1/utils/packages.py`

 * *Files identical despite different names*

### Comparing `pylzy-1.8.7/lzy/api/v1/utils/proxy_adapter.py` & `pylzy-1.8.8/lzy/api/v1/utils/proxy_adapter.py`

 * *Files identical despite different names*

### Comparing `pylzy-1.8.7/lzy/api/v1/utils/types.py` & `pylzy-1.8.8/lzy/api/v1/utils/types.py`

 * *Files identical despite different names*

### Comparing `pylzy-1.8.7/lzy/api/v1/whiteboards.py` & `pylzy-1.8.8/lzy/api/v1/whiteboards.py`

 * *Files identical despite different names*

### Comparing `pylzy-1.8.7/lzy/api/v1/workflow.py` & `pylzy-1.8.8/lzy/api/v1/workflow.py`

 * *Files identical despite different names*

### Comparing `pylzy-1.8.7/lzy/injections/catboost.py` & `pylzy-1.8.8/lzy/injections/catboost.py`

 * *Files identical despite different names*

### Comparing `pylzy-1.8.7/lzy/logs/config.py` & `pylzy-1.8.8/lzy/logs/config.py`

 * *Files identical despite different names*

### Comparing `pylzy-1.8.7/lzy/logs/logging.yml` & `pylzy-1.8.8/lzy/logs/logging.yml`

 * *Files identical despite different names*

### Comparing `pylzy-1.8.7/lzy/proxy/automagic.py` & `pylzy-1.8.8/lzy/proxy/automagic.py`

 * *Files identical despite different names*

### Comparing `pylzy-1.8.7/lzy/py_env/py_env_provider.py` & `pylzy-1.8.8/lzy/py_env/py_env_provider.py`

 * *Files identical despite different names*

### Comparing `pylzy-1.8.7/lzy/serialization/file.py` & `pylzy-1.8.8/lzy/serialization/file.py`

 * *Files identical despite different names*

### Comparing `pylzy-1.8.7/lzy/serialization/registry.py` & `pylzy-1.8.8/lzy/serialization/registry.py`

 * *Files identical despite different names*

### Comparing `pylzy-1.8.7/lzy/storage/api.py` & `pylzy-1.8.8/lzy/storage/api.py`

 * *Files identical despite different names*

### Comparing `pylzy-1.8.7/lzy/storage/async_/__init__.py` & `pylzy-1.8.8/lzy/storage/async_/__init__.py`

 * *Files identical despite different names*

### Comparing `pylzy-1.8.7/lzy/storage/async_/azure.py` & `pylzy-1.8.8/lzy/storage/async_/azure.py`

 * *Files identical despite different names*

### Comparing `pylzy-1.8.7/lzy/storage/async_/fs.py` & `pylzy-1.8.8/lzy/storage/async_/fs.py`

 * *Files identical despite different names*

### Comparing `pylzy-1.8.7/lzy/storage/async_/s3.py` & `pylzy-1.8.8/lzy/storage/async_/s3.py`

 * *Files identical despite different names*

### Comparing `pylzy-1.8.7/lzy/storage/registry.py` & `pylzy-1.8.8/lzy/storage/registry.py`

 * *Files identical despite different names*

### Comparing `pylzy-1.8.7/lzy/storage/url.py` & `pylzy-1.8.8/lzy/storage/url.py`

 * *Files identical despite different names*

### Comparing `pylzy-1.8.7/lzy/utils/event_loop.py` & `pylzy-1.8.8/lzy/utils/event_loop.py`

 * *Files identical despite different names*

### Comparing `pylzy-1.8.7/lzy/utils/grpc.py` & `pylzy-1.8.8/lzy/utils/grpc.py`

 * *Files identical despite different names*

### Comparing `pylzy-1.8.7/lzy/whiteboards/api.py` & `pylzy-1.8.8/lzy/whiteboards/api.py`

 * *Files identical despite different names*

### Comparing `pylzy-1.8.7/lzy/whiteboards/index.py` & `pylzy-1.8.8/lzy/whiteboards/index.py`

 * *Files identical despite different names*

### Comparing `pylzy-1.8.7/lzy/whiteboards/wrapper.py` & `pylzy-1.8.8/lzy/whiteboards/wrapper.py`

 * *Files identical despite different names*

### Comparing `pylzy-1.8.7/pylzy.egg-info/PKG-INFO` & `pylzy-1.8.8/pylzy.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: pylzy
-Version: 1.8.7
+Version: 1.8.8
 Summary: UNKNOWN
 Author: ʎzy developers
 License: LICENSE
 Platform: UNKNOWN
 Classifier: Programming Language :: Python :: 3.7
 Classifier: Programming Language :: Python :: 3.8
 Classifier: Programming Language :: Python :: 3.9
```

### Comparing `pylzy-1.8.7/pylzy.egg-info/SOURCES.txt` & `pylzy-1.8.8/pylzy.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `pylzy-1.8.7/readme.md` & `pylzy-1.8.8/readme.md`

 * *Files identical despite different names*

### Comparing `pylzy-1.8.7/setup.py` & `pylzy-1.8.8/setup.py`

 * *Files identical despite different names*

