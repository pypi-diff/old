# Comparing `tmp/ydb-3.2.1.tar.gz` & `tmp/ydb-3.2.2.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "ydb-3.2.1.tar", last modified: Mon Apr  3 15:07:04 2023, max compression
+gzip compressed data, was "ydb-3.2.2.tar", last modified: Thu Apr  6 11:52:04 2023, max compression
```

## Comparing `ydb-3.2.1.tar` & `ydb-3.2.2.tar`

### file list

```diff
@@ -1,257 +1,248 @@
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-03 15:07:04.728172 ydb-3.2.1/
--rw-r--r--   0 runner    (1001) docker     (123)      220 2023-04-03 15:06:55.000000 ydb-3.2.1/AUTHORS
--rw-r--r--   0 runner    (1001) docker     (123)    11361 2023-04-03 15:06:55.000000 ydb-3.2.1/LICENSE
--rw-r--r--   0 runner    (1001) docker     (123)       25 2023-04-03 15:06:55.000000 ydb-3.2.1/MANIFEST.in
--rw-r--r--   0 runner    (1001) docker     (123)     1669 2023-04-03 15:07:04.728172 ydb-3.2.1/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)     1126 2023-04-03 15:06:55.000000 ydb-3.2.1/README.md
--rw-r--r--   0 runner    (1001) docker     (123)       31 2023-04-03 15:06:55.000000 ydb-3.2.1/pyproject.toml
--rw-r--r--   0 runner    (1001) docker     (123)       64 2023-04-03 15:06:55.000000 ydb-3.2.1/requirements.txt
--rw-r--r--   0 runner    (1001) docker     (123)       38 2023-04-03 15:07:04.728172 ydb-3.2.1/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (123)     1127 2023-04-03 15:06:57.000000 ydb-3.2.1/setup.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-03 15:07:04.724172 ydb-3.2.1/tests/
--rw-r--r--   0 runner    (1001) docker     (123)      531 2023-04-03 15:06:55.000000 ydb-3.2.1/tests/test_errors.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-03 15:07:04.696172 ydb-3.2.1/ydb/
--rw-r--r--   0 runner    (1001) docker     (123)      582 2023-04-03 15:06:55.000000 ydb-3.2.1/ydb/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     3032 2023-04-03 15:06:55.000000 ydb-3.2.1/ydb/_apis.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-03 15:07:04.696172 ydb-3.2.1/ydb/_dbapi/
--rw-r--r--   0 runner    (1001) docker     (123)      573 2023-04-03 15:06:55.000000 ydb-3.2.1/ydb/_dbapi/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     2233 2023-04-03 15:06:55.000000 ydb-3.2.1/ydb/_dbapi/connection.py
--rw-r--r--   0 runner    (1001) docker     (123)     5341 2023-04-03 15:06:55.000000 ydb-3.2.1/ydb/_dbapi/cursor.py
--rw-r--r--   0 runner    (1001) docker     (123)     1970 2023-04-03 15:06:55.000000 ydb-3.2.1/ydb/_dbapi/errors.py
--rw-r--r--   0 runner    (1001) docker     (123)     2077 2023-04-03 15:06:55.000000 ydb-3.2.1/ydb/_dbapi/test_cursor.py
--rw-r--r--   0 runner    (1001) docker     (123)     1659 2023-04-03 15:06:55.000000 ydb-3.2.1/ydb/_errors.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-03 15:07:04.696172 ydb-3.2.1/ydb/_grpc/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-03 15:06:55.000000 ydb-3.2.1/ydb/_grpc/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-03 15:07:04.696172 ydb-3.2.1/ydb/_grpc/common/
--rw-r--r--   0 runner    (1001) docker     (123)     1253 2023-04-03 15:06:55.000000 ydb-3.2.1/ydb/_grpc/common/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-03 15:07:04.700172 ydb-3.2.1/ydb/_grpc/grpcwrapper/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-03 15:06:55.000000 ydb-3.2.1/ydb/_grpc/grpcwrapper/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     8273 2023-04-03 15:06:55.000000 ydb-3.2.1/ydb/_grpc/grpcwrapper/common_utils.py
--rw-r--r--   0 runner    (1001) docker     (123)      719 2023-04-03 15:06:55.000000 ydb-3.2.1/ydb/_grpc/grpcwrapper/ydb_scheme.py
--rw-r--r--   0 runner    (1001) docker     (123)    42335 2023-04-03 15:06:55.000000 ydb-3.2.1/ydb/_grpc/grpcwrapper/ydb_topic.py
--rw-r--r--   0 runner    (1001) docker     (123)     5865 2023-04-03 15:06:55.000000 ydb-3.2.1/ydb/_grpc/grpcwrapper/ydb_topic_public_types.py
--rw-r--r--   0 runner    (1001) docker     (123)      726 2023-04-03 15:06:55.000000 ydb-3.2.1/ydb/_grpc/grpcwrapper/ydb_topic_test.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-03 15:07:04.700172 ydb-3.2.1/ydb/_grpc/v3/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-03 15:06:55.000000 ydb-3.2.1/ydb/_grpc/v3/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-03 15:07:04.708172 ydb-3.2.1/ydb/_grpc/v3/protos/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-03 15:06:55.000000 ydb-3.2.1/ydb/_grpc/v3/protos/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-03 15:07:04.708172 ydb-3.2.1/ydb/_grpc/v3/protos/annotations/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-03 15:06:55.000000 ydb-3.2.1/ydb/_grpc/v3/protos/annotations/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    12213 2023-04-03 15:06:55.000000 ydb-3.2.1/ydb/_grpc/v3/protos/annotations/validation_pb2.py
--rw-r--r--   0 runner    (1001) docker     (123)      159 2023-04-03 15:06:55.000000 ydb-3.2.1/ydb/_grpc/v3/protos/annotations/validation_pb2_grpc.py
--rw-r--r--   0 runner    (1001) docker     (123)     6184 2023-04-03 15:06:55.000000 ydb-3.2.1/ydb/_grpc/v3/protos/ydb_auth_pb2.py
--rw-r--r--   0 runner    (1001) docker     (123)      159 2023-04-03 15:06:55.000000 ydb-3.2.1/ydb/_grpc/v3/protos/ydb_auth_pb2_grpc.py
--rw-r--r--   0 runner    (1001) docker     (123)    83179 2023-04-03 15:06:55.000000 ydb-3.2.1/ydb/_grpc/v3/protos/ydb_cms_pb2.py
--rw-r--r--   0 runner    (1001) docker     (123)      159 2023-04-03 15:06:55.000000 ydb-3.2.1/ydb/_grpc/v3/protos/ydb_cms_pb2_grpc.py
--rw-r--r--   0 runner    (1001) docker     (123)     7124 2023-04-03 15:06:55.000000 ydb-3.2.1/ydb/_grpc/v3/protos/ydb_common_pb2.py
--rw-r--r--   0 runner    (1001) docker     (123)      159 2023-04-03 15:06:55.000000 ydb-3.2.1/ydb/_grpc/v3/protos/ydb_common_pb2_grpc.py
--rw-r--r--   0 runner    (1001) docker     (123)   121326 2023-04-03 15:06:55.000000 ydb-3.2.1/ydb/_grpc/v3/protos/ydb_coordination_pb2.py
--rw-r--r--   0 runner    (1001) docker     (123)      159 2023-04-03 15:06:55.000000 ydb-3.2.1/ydb/_grpc/v3/protos/ydb_coordination_pb2_grpc.py
--rw-r--r--   0 runner    (1001) docker     (123)    16470 2023-04-03 15:06:55.000000 ydb-3.2.1/ydb/_grpc/v3/protos/ydb_discovery_pb2.py
--rw-r--r--   0 runner    (1001) docker     (123)      159 2023-04-03 15:06:55.000000 ydb-3.2.1/ydb/_grpc/v3/protos/ydb_discovery_pb2_grpc.py
--rw-r--r--   0 runner    (1001) docker     (123)    41176 2023-04-03 15:06:55.000000 ydb-3.2.1/ydb/_grpc/v3/protos/ydb_export_pb2.py
--rw-r--r--   0 runner    (1001) docker     (123)      159 2023-04-03 15:06:55.000000 ydb-3.2.1/ydb/_grpc/v3/protos/ydb_export_pb2_grpc.py
--rw-r--r--   0 runner    (1001) docker     (123)     4995 2023-04-03 15:06:55.000000 ydb-3.2.1/ydb/_grpc/v3/protos/ydb_formats_pb2.py
--rw-r--r--   0 runner    (1001) docker     (123)      159 2023-04-03 15:06:55.000000 ydb-3.2.1/ydb/_grpc/v3/protos/ydb_formats_pb2_grpc.py
--rw-r--r--   0 runner    (1001) docker     (123)    30782 2023-04-03 15:06:55.000000 ydb-3.2.1/ydb/_grpc/v3/protos/ydb_import_pb2.py
--rw-r--r--   0 runner    (1001) docker     (123)      159 2023-04-03 15:06:55.000000 ydb-3.2.1/ydb/_grpc/v3/protos/ydb_import_pb2_grpc.py
--rw-r--r--   0 runner    (1001) docker     (123)     7161 2023-04-03 15:06:55.000000 ydb-3.2.1/ydb/_grpc/v3/protos/ydb_issue_message_pb2.py
--rw-r--r--   0 runner    (1001) docker     (123)      159 2023-04-03 15:06:55.000000 ydb-3.2.1/ydb/_grpc/v3/protos/ydb_issue_message_pb2_grpc.py
--rw-r--r--   0 runner    (1001) docker     (123)    72285 2023-04-03 15:06:55.000000 ydb-3.2.1/ydb/_grpc/v3/protos/ydb_monitoring_pb2.py
--rw-r--r--   0 runner    (1001) docker     (123)      159 2023-04-03 15:06:55.000000 ydb-3.2.1/ydb/_grpc/v3/protos/ydb_monitoring_pb2_grpc.py
--rw-r--r--   0 runner    (1001) docker     (123)    29771 2023-04-03 15:06:55.000000 ydb-3.2.1/ydb/_grpc/v3/protos/ydb_operation_pb2.py
--rw-r--r--   0 runner    (1001) docker     (123)      159 2023-04-03 15:06:55.000000 ydb-3.2.1/ydb/_grpc/v3/protos/ydb_operation_pb2_grpc.py
--rw-r--r--   0 runner    (1001) docker     (123)    16311 2023-04-03 15:06:55.000000 ydb-3.2.1/ydb/_grpc/v3/protos/ydb_query_stats_pb2.py
--rw-r--r--   0 runner    (1001) docker     (123)      159 2023-04-03 15:06:55.000000 ydb-3.2.1/ydb/_grpc/v3/protos/ydb_query_stats_pb2_grpc.py
--rw-r--r--   0 runner    (1001) docker     (123)    40278 2023-04-03 15:06:55.000000 ydb-3.2.1/ydb/_grpc/v3/protos/ydb_rate_limiter_pb2.py
--rw-r--r--   0 runner    (1001) docker     (123)      159 2023-04-03 15:06:55.000000 ydb-3.2.1/ydb/_grpc/v3/protos/ydb_rate_limiter_pb2_grpc.py
--rw-r--r--   0 runner    (1001) docker     (123)    38051 2023-04-03 15:06:55.000000 ydb-3.2.1/ydb/_grpc/v3/protos/ydb_scheme_pb2.py
--rw-r--r--   0 runner    (1001) docker     (123)      159 2023-04-03 15:06:55.000000 ydb-3.2.1/ydb/_grpc/v3/protos/ydb_scheme_pb2_grpc.py
--rw-r--r--   0 runner    (1001) docker     (123)    25816 2023-04-03 15:06:55.000000 ydb-3.2.1/ydb/_grpc/v3/protos/ydb_scripting_pb2.py
--rw-r--r--   0 runner    (1001) docker     (123)      159 2023-04-03 15:06:55.000000 ydb-3.2.1/ydb/_grpc/v3/protos/ydb_scripting_pb2_grpc.py
--rw-r--r--   0 runner    (1001) docker     (123)     6884 2023-04-03 15:06:55.000000 ydb-3.2.1/ydb/_grpc/v3/protos/ydb_status_codes_pb2.py
--rw-r--r--   0 runner    (1001) docker     (123)      159 2023-04-03 15:06:55.000000 ydb-3.2.1/ydb/_grpc/v3/protos/ydb_status_codes_pb2_grpc.py
--rw-r--r--   0 runner    (1001) docker     (123)   332647 2023-04-03 15:06:55.000000 ydb-3.2.1/ydb/_grpc/v3/protos/ydb_table_pb2.py
--rw-r--r--   0 runner    (1001) docker     (123)      159 2023-04-03 15:06:55.000000 ydb-3.2.1/ydb/_grpc/v3/protos/ydb_table_pb2_grpc.py
--rw-r--r--   0 runner    (1001) docker     (123)   234296 2023-04-03 15:06:55.000000 ydb-3.2.1/ydb/_grpc/v3/protos/ydb_topic_pb2.py
--rw-r--r--   0 runner    (1001) docker     (123)      159 2023-04-03 15:06:55.000000 ydb-3.2.1/ydb/_grpc/v3/protos/ydb_topic_pb2_grpc.py
--rw-r--r--   0 runner    (1001) docker     (123)    52587 2023-04-03 15:06:55.000000 ydb-3.2.1/ydb/_grpc/v3/protos/ydb_value_pb2.py
--rw-r--r--   0 runner    (1001) docker     (123)      159 2023-04-03 15:06:55.000000 ydb-3.2.1/ydb/_grpc/v3/protos/ydb_value_pb2_grpc.py
--rw-r--r--   0 runner    (1001) docker     (123)     1970 2023-04-03 15:06:55.000000 ydb-3.2.1/ydb/_grpc/v3/ydb_auth_v1_pb2.py
--rw-r--r--   0 runner    (1001) docker     (123)     2503 2023-04-03 15:06:55.000000 ydb-3.2.1/ydb/_grpc/v3/ydb_auth_v1_pb2_grpc.py
--rw-r--r--   0 runner    (1001) docker     (123)     4418 2023-04-03 15:06:55.000000 ydb-3.2.1/ydb/_grpc/v3/ydb_cms_v1_pb2.py
--rw-r--r--   0 runner    (1001) docker     (123)    11170 2023-04-03 15:06:55.000000 ydb-3.2.1/ydb/_grpc/v3/ydb_cms_v1_pb2_grpc.py
--rw-r--r--   0 runner    (1001) docker     (123)     4226 2023-04-03 15:06:55.000000 ydb-3.2.1/ydb/_grpc/v3/ydb_coordination_v1_pb2.py
--rw-r--r--   0 runner    (1001) docker     (123)     9797 2023-04-03 15:06:55.000000 ydb-3.2.1/ydb/_grpc/v3/ydb_coordination_v1_pb2_grpc.py
--rw-r--r--   0 runner    (1001) docker     (123)     2610 2023-04-03 15:06:55.000000 ydb-3.2.1/ydb/_grpc/v3/ydb_discovery_v1_pb2.py
--rw-r--r--   0 runner    (1001) docker     (123)     4307 2023-04-03 15:06:55.000000 ydb-3.2.1/ydb/_grpc/v3/ydb_discovery_v1_pb2_grpc.py
--rw-r--r--   0 runner    (1001) docker     (123)     2512 2023-04-03 15:06:55.000000 ydb-3.2.1/ydb/_grpc/v3/ydb_export_v1_pb2.py
--rw-r--r--   0 runner    (1001) docker     (123)     4370 2023-04-03 15:06:55.000000 ydb-3.2.1/ydb/_grpc/v3/ydb_export_v1_pb2_grpc.py
--rw-r--r--   0 runner    (1001) docker     (123)     2527 2023-04-03 15:06:55.000000 ydb-3.2.1/ydb/_grpc/v3/ydb_import_v1_pb2.py
--rw-r--r--   0 runner    (1001) docker     (123)     4404 2023-04-03 15:06:55.000000 ydb-3.2.1/ydb/_grpc/v3/ydb_import_v1_pb2_grpc.py
--rw-r--r--   0 runner    (1001) docker     (123)     2622 2023-04-03 15:06:55.000000 ydb-3.2.1/ydb/_grpc/v3/ydb_monitoring_v1_pb2.py
--rw-r--r--   0 runner    (1001) docker     (123)     4293 2023-04-03 15:06:55.000000 ydb-3.2.1/ydb/_grpc/v3/ydb_monitoring_v1_pb2_grpc.py
--rw-r--r--   0 runner    (1001) docker     (123)     3688 2023-04-03 15:06:55.000000 ydb-3.2.1/ydb/_grpc/v3/ydb_operation_v1_pb2.py
--rw-r--r--   0 runner    (1001) docker     (123)    10345 2023-04-03 15:06:55.000000 ydb-3.2.1/ydb/_grpc/v3/ydb_operation_v1_pb2_grpc.py
--rw-r--r--   0 runner    (1001) docker     (123)     4877 2023-04-03 15:06:55.000000 ydb-3.2.1/ydb/_grpc/v3/ydb_rate_limiter_v1_pb2.py
--rw-r--r--   0 runner    (1001) docker     (123)    11754 2023-04-03 15:06:55.000000 ydb-3.2.1/ydb/_grpc/v3/ydb_rate_limiter_v1_pb2_grpc.py
--rw-r--r--   0 runner    (1001) docker     (123)     4012 2023-04-03 15:06:55.000000 ydb-3.2.1/ydb/_grpc/v3/ydb_scheme_v1_pb2.py
--rw-r--r--   0 runner    (1001) docker     (123)    10044 2023-04-03 15:06:55.000000 ydb-3.2.1/ydb/_grpc/v3/ydb_scheme_v1_pb2_grpc.py
--rw-r--r--   0 runner    (1001) docker     (123)     3112 2023-04-03 15:06:55.000000 ydb-3.2.1/ydb/_grpc/v3/ydb_scripting_v1_pb2.py
--rw-r--r--   0 runner    (1001) docker     (123)     6037 2023-04-03 15:06:55.000000 ydb-3.2.1/ydb/_grpc/v3/ydb_scripting_v1_pb2_grpc.py
--rw-r--r--   0 runner    (1001) docker     (123)    11659 2023-04-03 15:06:55.000000 ydb-3.2.1/ydb/_grpc/v3/ydb_table_v1_pb2.py
--rw-r--r--   0 runner    (1001) docker     (123)    36535 2023-04-03 15:06:55.000000 ydb-3.2.1/ydb/_grpc/v3/ydb_table_v1_pb2_grpc.py
--rw-r--r--   0 runner    (1001) docker     (123)     4956 2023-04-03 15:06:55.000000 ydb-3.2.1/ydb/_grpc/v3/ydb_topic_v1_pb2.py
--rw-r--r--   0 runner    (1001) docker     (123)    14404 2023-04-03 15:06:55.000000 ydb-3.2.1/ydb/_grpc/v3/ydb_topic_v1_pb2_grpc.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-03 15:07:04.712172 ydb-3.2.1/ydb/_grpc/v4/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-03 15:06:55.000000 ydb-3.2.1/ydb/_grpc/v4/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-03 15:07:04.716172 ydb-3.2.1/ydb/_grpc/v4/protos/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-03 15:06:55.000000 ydb-3.2.1/ydb/_grpc/v4/protos/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-03 15:07:04.716172 ydb-3.2.1/ydb/_grpc/v4/protos/annotations/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-03 15:06:55.000000 ydb-3.2.1/ydb/_grpc/v4/protos/annotations/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     2727 2023-04-03 15:06:55.000000 ydb-3.2.1/ydb/_grpc/v4/protos/annotations/validation_pb2.py
--rw-r--r--   0 runner    (1001) docker     (123)      159 2023-04-03 15:06:55.000000 ydb-3.2.1/ydb/_grpc/v4/protos/annotations/validation_pb2_grpc.py
--rw-r--r--   0 runner    (1001) docker     (123)     1747 2023-04-03 15:06:55.000000 ydb-3.2.1/ydb/_grpc/v4/protos/ydb_auth_pb2.py
--rw-r--r--   0 runner    (1001) docker     (123)      159 2023-04-03 15:06:55.000000 ydb-3.2.1/ydb/_grpc/v4/protos/ydb_auth_pb2_grpc.py
--rw-r--r--   0 runner    (1001) docker     (123)    12062 2023-04-03 15:06:55.000000 ydb-3.2.1/ydb/_grpc/v4/protos/ydb_cms_pb2.py
--rw-r--r--   0 runner    (1001) docker     (123)      159 2023-04-03 15:06:55.000000 ydb-3.2.1/ydb/_grpc/v4/protos/ydb_cms_pb2_grpc.py
--rw-r--r--   0 runner    (1001) docker     (123)     1882 2023-04-03 15:06:55.000000 ydb-3.2.1/ydb/_grpc/v4/protos/ydb_common_pb2.py
--rw-r--r--   0 runner    (1001) docker     (123)      159 2023-04-03 15:06:55.000000 ydb-3.2.1/ydb/_grpc/v4/protos/ydb_common_pb2_grpc.py
--rw-r--r--   0 runner    (1001) docker     (123)    15716 2023-04-03 15:06:55.000000 ydb-3.2.1/ydb/_grpc/v4/protos/ydb_coordination_pb2.py
--rw-r--r--   0 runner    (1001) docker     (123)      159 2023-04-03 15:06:55.000000 ydb-3.2.1/ydb/_grpc/v4/protos/ydb_coordination_pb2_grpc.py
--rw-r--r--   0 runner    (1001) docker     (123)     2871 2023-04-03 15:06:55.000000 ydb-3.2.1/ydb/_grpc/v4/protos/ydb_discovery_pb2.py
--rw-r--r--   0 runner    (1001) docker     (123)      159 2023-04-03 15:06:55.000000 ydb-3.2.1/ydb/_grpc/v4/protos/ydb_discovery_pb2_grpc.py
--rw-r--r--   0 runner    (1001) docker     (123)     9313 2023-04-03 15:06:55.000000 ydb-3.2.1/ydb/_grpc/v4/protos/ydb_export_pb2.py
--rw-r--r--   0 runner    (1001) docker     (123)      159 2023-04-03 15:06:55.000000 ydb-3.2.1/ydb/_grpc/v4/protos/ydb_export_pb2_grpc.py
--rw-r--r--   0 runner    (1001) docker     (123)     1514 2023-04-03 15:06:55.000000 ydb-3.2.1/ydb/_grpc/v4/protos/ydb_formats_pb2.py
--rw-r--r--   0 runner    (1001) docker     (123)      159 2023-04-03 15:06:55.000000 ydb-3.2.1/ydb/_grpc/v4/protos/ydb_formats_pb2_grpc.py
--rw-r--r--   0 runner    (1001) docker     (123)     6939 2023-04-03 15:06:55.000000 ydb-3.2.1/ydb/_grpc/v4/protos/ydb_import_pb2.py
--rw-r--r--   0 runner    (1001) docker     (123)      159 2023-04-03 15:06:55.000000 ydb-3.2.1/ydb/_grpc/v4/protos/ydb_import_pb2_grpc.py
--rw-r--r--   0 runner    (1001) docker     (123)     1770 2023-04-03 15:06:55.000000 ydb-3.2.1/ydb/_grpc/v4/protos/ydb_issue_message_pb2.py
--rw-r--r--   0 runner    (1001) docker     (123)      159 2023-04-03 15:06:55.000000 ydb-3.2.1/ydb/_grpc/v4/protos/ydb_issue_message_pb2_grpc.py
--rw-r--r--   0 runner    (1001) docker     (123)     9769 2023-04-03 15:06:55.000000 ydb-3.2.1/ydb/_grpc/v4/protos/ydb_monitoring_pb2.py
--rw-r--r--   0 runner    (1001) docker     (123)      159 2023-04-03 15:06:55.000000 ydb-3.2.1/ydb/_grpc/v4/protos/ydb_monitoring_pb2_grpc.py
--rw-r--r--   0 runner    (1001) docker     (123)     6165 2023-04-03 15:06:55.000000 ydb-3.2.1/ydb/_grpc/v4/protos/ydb_operation_pb2.py
--rw-r--r--   0 runner    (1001) docker     (123)      159 2023-04-03 15:06:55.000000 ydb-3.2.1/ydb/_grpc/v4/protos/ydb_operation_pb2_grpc.py
--rw-r--r--   0 runner    (1001) docker     (123)     2849 2023-04-03 15:06:55.000000 ydb-3.2.1/ydb/_grpc/v4/protos/ydb_query_stats_pb2.py
--rw-r--r--   0 runner    (1001) docker     (123)      159 2023-04-03 15:06:55.000000 ydb-3.2.1/ydb/_grpc/v4/protos/ydb_query_stats_pb2_grpc.py
--rw-r--r--   0 runner    (1001) docker     (123)     6057 2023-04-03 15:06:55.000000 ydb-3.2.1/ydb/_grpc/v4/protos/ydb_rate_limiter_pb2.py
--rw-r--r--   0 runner    (1001) docker     (123)      159 2023-04-03 15:06:55.000000 ydb-3.2.1/ydb/_grpc/v4/protos/ydb_rate_limiter_pb2_grpc.py
--rw-r--r--   0 runner    (1001) docker     (123)     5830 2023-04-03 15:06:55.000000 ydb-3.2.1/ydb/_grpc/v4/protos/ydb_scheme_pb2.py
--rw-r--r--   0 runner    (1001) docker     (123)      159 2023-04-03 15:06:55.000000 ydb-3.2.1/ydb/_grpc/v4/protos/ydb_scheme_pb2_grpc.py
--rw-r--r--   0 runner    (1001) docker     (123)     5143 2023-04-03 15:06:55.000000 ydb-3.2.1/ydb/_grpc/v4/protos/ydb_scripting_pb2.py
--rw-r--r--   0 runner    (1001) docker     (123)      159 2023-04-03 15:06:55.000000 ydb-3.2.1/ydb/_grpc/v4/protos/ydb_scripting_pb2_grpc.py
--rw-r--r--   0 runner    (1001) docker     (123)     2153 2023-04-03 15:06:55.000000 ydb-3.2.1/ydb/_grpc/v4/protos/ydb_status_codes_pb2.py
--rw-r--r--   0 runner    (1001) docker     (123)      159 2023-04-03 15:06:55.000000 ydb-3.2.1/ydb/_grpc/v4/protos/ydb_status_codes_pb2_grpc.py
--rw-r--r--   0 runner    (1001) docker     (123)    46408 2023-04-03 15:06:55.000000 ydb-3.2.1/ydb/_grpc/v4/protos/ydb_table_pb2.py
--rw-r--r--   0 runner    (1001) docker     (123)      159 2023-04-03 15:06:55.000000 ydb-3.2.1/ydb/_grpc/v4/protos/ydb_table_pb2_grpc.py
--rw-r--r--   0 runner    (1001) docker     (123)    34953 2023-04-03 15:06:55.000000 ydb-3.2.1/ydb/_grpc/v4/protos/ydb_topic_pb2.py
--rw-r--r--   0 runner    (1001) docker     (123)      159 2023-04-03 15:06:55.000000 ydb-3.2.1/ydb/_grpc/v4/protos/ydb_topic_pb2_grpc.py
--rw-r--r--   0 runner    (1001) docker     (123)     6618 2023-04-03 15:06:55.000000 ydb-3.2.1/ydb/_grpc/v4/protos/ydb_value_pb2.py
--rw-r--r--   0 runner    (1001) docker     (123)      159 2023-04-03 15:06:55.000000 ydb-3.2.1/ydb/_grpc/v4/protos/ydb_value_pb2_grpc.py
--rw-r--r--   0 runner    (1001) docker     (123)     1325 2023-04-03 15:06:55.000000 ydb-3.2.1/ydb/_grpc/v4/ydb_auth_v1_pb2.py
--rw-r--r--   0 runner    (1001) docker     (123)     2503 2023-04-03 15:06:55.000000 ydb-3.2.1/ydb/_grpc/v4/ydb_auth_v1_pb2_grpc.py
--rw-r--r--   0 runner    (1001) docker     (123)     1868 2023-04-03 15:06:55.000000 ydb-3.2.1/ydb/_grpc/v4/ydb_cms_v1_pb2.py
--rw-r--r--   0 runner    (1001) docker     (123)    11170 2023-04-03 15:06:55.000000 ydb-3.2.1/ydb/_grpc/v4/ydb_cms_v1_pb2_grpc.py
--rw-r--r--   0 runner    (1001) docker     (123)     1937 2023-04-03 15:06:55.000000 ydb-3.2.1/ydb/_grpc/v4/ydb_coordination_v1_pb2.py
--rw-r--r--   0 runner    (1001) docker     (123)     9797 2023-04-03 15:06:55.000000 ydb-3.2.1/ydb/_grpc/v4/ydb_coordination_v1_pb2_grpc.py
--rw-r--r--   0 runner    (1001) docker     (123)     1518 2023-04-03 15:06:55.000000 ydb-3.2.1/ydb/_grpc/v4/ydb_discovery_v1_pb2.py
--rw-r--r--   0 runner    (1001) docker     (123)     4307 2023-04-03 15:06:55.000000 ydb-3.2.1/ydb/_grpc/v4/ydb_discovery_v1_pb2_grpc.py
--rw-r--r--   0 runner    (1001) docker     (123)     1461 2023-04-03 15:06:55.000000 ydb-3.2.1/ydb/_grpc/v4/ydb_export_v1_pb2.py
--rw-r--r--   0 runner    (1001) docker     (123)     4370 2023-04-03 15:06:55.000000 ydb-3.2.1/ydb/_grpc/v4/ydb_export_v1_pb2_grpc.py
--rw-r--r--   0 runner    (1001) docker     (123)     1468 2023-04-03 15:06:55.000000 ydb-3.2.1/ydb/_grpc/v4/ydb_import_v1_pb2.py
--rw-r--r--   0 runner    (1001) docker     (123)     4404 2023-04-03 15:06:55.000000 ydb-3.2.1/ydb/_grpc/v4/ydb_import_v1_pb2_grpc.py
--rw-r--r--   0 runner    (1001) docker     (123)     1519 2023-04-03 15:06:55.000000 ydb-3.2.1/ydb/_grpc/v4/ydb_monitoring_v1_pb2.py
--rw-r--r--   0 runner    (1001) docker     (123)     4293 2023-04-03 15:06:55.000000 ydb-3.2.1/ydb/_grpc/v4/ydb_monitoring_v1_pb2_grpc.py
--rw-r--r--   0 runner    (1001) docker     (123)     1776 2023-04-03 15:06:55.000000 ydb-3.2.1/ydb/_grpc/v4/ydb_operation_v1_pb2.py
--rw-r--r--   0 runner    (1001) docker     (123)    10345 2023-04-03 15:06:55.000000 ydb-3.2.1/ydb/_grpc/v4/ydb_operation_v1_pb2_grpc.py
--rw-r--r--   0 runner    (1001) docker     (123)     2097 2023-04-03 15:06:55.000000 ydb-3.2.1/ydb/_grpc/v4/ydb_rate_limiter_v1_pb2.py
--rw-r--r--   0 runner    (1001) docker     (123)    11754 2023-04-03 15:06:55.000000 ydb-3.2.1/ydb/_grpc/v4/ydb_rate_limiter_v1_pb2_grpc.py
--rw-r--r--   0 runner    (1001) docker     (123)     1789 2023-04-03 15:06:55.000000 ydb-3.2.1/ydb/_grpc/v4/ydb_scheme_v1_pb2.py
--rw-r--r--   0 runner    (1001) docker     (123)    10044 2023-04-03 15:06:55.000000 ydb-3.2.1/ydb/_grpc/v4/ydb_scheme_v1_pb2_grpc.py
--rw-r--r--   0 runner    (1001) docker     (123)     1621 2023-04-03 15:06:55.000000 ydb-3.2.1/ydb/_grpc/v4/ydb_scripting_v1_pb2.py
--rw-r--r--   0 runner    (1001) docker     (123)     6037 2023-04-03 15:06:55.000000 ydb-3.2.1/ydb/_grpc/v4/ydb_scripting_v1_pb2_grpc.py
--rw-r--r--   0 runner    (1001) docker     (123)     3453 2023-04-03 15:06:55.000000 ydb-3.2.1/ydb/_grpc/v4/ydb_table_v1_pb2.py
--rw-r--r--   0 runner    (1001) docker     (123)    36535 2023-04-03 15:06:55.000000 ydb-3.2.1/ydb/_grpc/v4/ydb_table_v1_pb2_grpc.py
--rw-r--r--   0 runner    (1001) docker     (123)     2038 2023-04-03 15:06:55.000000 ydb-3.2.1/ydb/_grpc/v4/ydb_topic_v1_pb2.py
--rw-r--r--   0 runner    (1001) docker     (123)    14404 2023-04-03 15:06:55.000000 ydb-3.2.1/ydb/_grpc/v4/ydb_topic_v1_pb2_grpc.py
--rw-r--r--   0 runner    (1001) docker     (123)    16278 2023-04-03 15:06:55.000000 ydb-3.2.1/ydb/_session_impl.py
--rw-r--r--   0 runner    (1001) docker     (123)    14424 2023-04-03 15:06:55.000000 ydb-3.2.1/ydb/_sp_impl.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-03 15:07:04.720172 ydb-3.2.1/ydb/_sqlalchemy/
--rw-r--r--   0 runner    (1001) docker     (123)     9770 2023-04-03 15:06:55.000000 ydb-3.2.1/ydb/_sqlalchemy/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      573 2023-04-03 15:06:55.000000 ydb-3.2.1/ydb/_sqlalchemy/types.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-03 15:07:04.720172 ydb-3.2.1/ydb/_topic_common/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-03 15:06:55.000000 ydb-3.2.1/ydb/_topic_common/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     4659 2023-04-03 15:06:55.000000 ydb-3.2.1/ydb/_topic_common/common.py
--rw-r--r--   0 runner    (1001) docker     (123)     7957 2023-04-03 15:06:55.000000 ydb-3.2.1/ydb/_topic_common/common_test.py
--rw-r--r--   0 runner    (1001) docker     (123)     1966 2023-04-03 15:06:55.000000 ydb-3.2.1/ydb/_topic_common/test_helpers.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-03 15:07:04.724172 ydb-3.2.1/ydb/_topic_reader/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-03 15:06:55.000000 ydb-3.2.1/ydb/_topic_reader/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     5528 2023-04-03 15:06:55.000000 ydb-3.2.1/ydb/_topic_reader/datatypes.py
--rw-r--r--   0 runner    (1001) docker     (123)     7350 2023-04-03 15:06:55.000000 ydb-3.2.1/ydb/_topic_reader/datatypes_test.py
--rw-r--r--   0 runner    (1001) docker     (123)     2529 2023-04-03 15:06:55.000000 ydb-3.2.1/ydb/_topic_reader/topic_reader.py
--rw-r--r--   0 runner    (1001) docker     (123)    22781 2023-04-03 15:06:55.000000 ydb-3.2.1/ydb/_topic_reader/topic_reader_asyncio.py
--rw-r--r--   0 runner    (1001) docker     (123)    46742 2023-04-03 15:06:55.000000 ydb-3.2.1/ydb/_topic_reader/topic_reader_asyncio_test.py
--rw-r--r--   0 runner    (1001) docker     (123)     5469 2023-04-03 15:06:55.000000 ydb-3.2.1/ydb/_topic_reader/topic_reader_sync.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-03 15:07:04.724172 ydb-3.2.1/ydb/_topic_writer/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-03 15:06:55.000000 ydb-3.2.1/ydb/_topic_writer/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     8093 2023-04-03 15:06:55.000000 ydb-3.2.1/ydb/_topic_writer/topic_writer.py
--rw-r--r--   0 runner    (1001) docker     (123)    23229 2023-04-03 15:06:55.000000 ydb-3.2.1/ydb/_topic_writer/topic_writer_asyncio.py
--rw-r--r--   0 runner    (1001) docker     (123)    24156 2023-04-03 15:06:55.000000 ydb-3.2.1/ydb/_topic_writer/topic_writer_asyncio_test.py
--rw-r--r--   0 runner    (1001) docker     (123)     3376 2023-04-03 15:06:55.000000 ydb-3.2.1/ydb/_topic_writer/topic_writer_sync.py
--rw-r--r--   0 runner    (1001) docker     (123)      951 2023-04-03 15:06:55.000000 ydb-3.2.1/ydb/_topic_writer/topic_writer_test.py
--rw-r--r--   0 runner    (1001) docker     (123)     5679 2023-04-03 15:06:55.000000 ydb-3.2.1/ydb/_tx_ctx_impl.py
--rw-r--r--   0 runner    (1001) docker     (123)     4130 2023-04-03 15:06:55.000000 ydb-3.2.1/ydb/_utilities.py
--rw-r--r--   0 runner    (1001) docker     (123)      281 2023-04-03 15:06:55.000000 ydb-3.2.1/ydb/_utilities_test.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-03 15:07:04.724172 ydb-3.2.1/ydb/aio/
--rw-r--r--   0 runner    (1001) docker     (123)       91 2023-04-03 15:06:55.000000 ydb-3.2.1/ydb/aio/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      462 2023-04-03 15:06:55.000000 ydb-3.2.1/ydb/aio/_utilities.py
--rw-r--r--   0 runner    (1001) docker     (123)     8402 2023-04-03 15:06:55.000000 ydb-3.2.1/ydb/aio/connection.py
--rw-r--r--   0 runner    (1001) docker     (123)     3402 2023-04-03 15:06:55.000000 ydb-3.2.1/ydb/aio/credentials.py
--rw-r--r--   0 runner    (1001) docker     (123)     1877 2023-04-03 15:06:55.000000 ydb-3.2.1/ydb/aio/driver.py
--rw-r--r--   0 runner    (1001) docker     (123)     4831 2023-04-03 15:06:55.000000 ydb-3.2.1/ydb/aio/iam.py
--rw-r--r--   0 runner    (1001) docker     (123)     8745 2023-04-03 15:06:55.000000 ydb-3.2.1/ydb/aio/pool.py
--rw-r--r--   0 runner    (1001) docker     (123)     2128 2023-04-03 15:06:55.000000 ydb-3.2.1/ydb/aio/resolver.py
--rw-r--r--   0 runner    (1001) docker     (123)      838 2023-04-03 15:06:55.000000 ydb-3.2.1/ydb/aio/scheme.py
--rw-r--r--   0 runner    (1001) docker     (123)    18011 2023-04-03 15:06:55.000000 ydb-3.2.1/ydb/aio/table.py
--rw-r--r--   0 runner    (1001) docker     (123)      304 2023-04-03 15:06:55.000000 ydb-3.2.1/ydb/auth_helpers.py
--rw-r--r--   0 runner    (1001) docker     (123)    18813 2023-04-03 15:06:55.000000 ydb-3.2.1/ydb/connection.py
--rw-r--r--   0 runner    (1001) docker     (123)    15107 2023-04-03 15:06:55.000000 ydb-3.2.1/ydb/convert.py
--rw-r--r--   0 runner    (1001) docker     (123)     7135 2023-04-03 15:06:55.000000 ydb-3.2.1/ydb/credentials.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-03 15:07:04.724172 ydb-3.2.1/ydb/dbapi/
--rw-r--r--   0 runner    (1001) docker     (123)      711 2023-04-03 15:06:55.000000 ydb-3.2.1/ydb/dbapi/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     2569 2023-04-03 15:06:55.000000 ydb-3.2.1/ydb/dbapi/connection.py
--rw-r--r--   0 runner    (1001) docker     (123)     5002 2023-04-03 15:06:55.000000 ydb-3.2.1/ydb/dbapi/cursor.py
--rw-r--r--   0 runner    (1001) docker     (123)     2174 2023-04-03 15:06:55.000000 ydb-3.2.1/ydb/dbapi/errors.py
--rw-r--r--   0 runner    (1001) docker     (123)   285865 2023-04-03 15:06:55.000000 ydb-3.2.1/ydb/default_pem.py
--rw-r--r--   0 runner    (1001) docker     (123)     9311 2023-04-03 15:06:55.000000 ydb-3.2.1/ydb/driver.py
--rw-r--r--   0 runner    (1001) docker     (123)     7769 2023-04-03 15:06:55.000000 ydb-3.2.1/ydb/export.py
--rw-r--r--   0 runner    (1001) docker     (123)      625 2023-04-03 15:06:55.000000 ydb-3.2.1/ydb/global_settings.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-03 15:07:04.724172 ydb-3.2.1/ydb/iam/
--rw-r--r--   0 runner    (1001) docker     (123)      125 2023-04-03 15:06:55.000000 ydb-3.2.1/ydb/iam/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     6296 2023-04-03 15:06:55.000000 ydb-3.2.1/ydb/iam/auth.py
--rw-r--r--   0 runner    (1001) docker     (123)     4376 2023-04-03 15:06:55.000000 ydb-3.2.1/ydb/import_client.py
--rw-r--r--   0 runner    (1001) docker     (123)     2336 2023-04-03 15:06:55.000000 ydb-3.2.1/ydb/interceptor.py
--rw-r--r--   0 runner    (1001) docker     (123)     4950 2023-04-03 15:06:55.000000 ydb-3.2.1/ydb/issues.py
--rw-r--r--   0 runner    (1001) docker     (123)     2973 2023-04-03 15:06:55.000000 ydb-3.2.1/ydb/operation.py
--rw-r--r--   0 runner    (1001) docker     (123)    16567 2023-04-03 15:06:55.000000 ydb-3.2.1/ydb/pool.py
--rw-r--r--   0 runner    (1001) docker     (123)     6878 2023-04-03 15:06:55.000000 ydb-3.2.1/ydb/resolver.py
--rw-r--r--   0 runner    (1001) docker     (123)    14271 2023-04-03 15:06:55.000000 ydb-3.2.1/ydb/scheme.py
--rw-r--r--   0 runner    (1001) docker     (123)      810 2023-04-03 15:06:55.000000 ydb-3.2.1/ydb/scheme_test.py
--rw-r--r--   0 runner    (1001) docker     (123)     3384 2023-04-03 15:06:55.000000 ydb-3.2.1/ydb/scripting.py
--rw-r--r--   0 runner    (1001) docker     (123)     3937 2023-04-03 15:06:55.000000 ydb-3.2.1/ydb/settings.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-03 15:07:04.724172 ydb-3.2.1/ydb/sqlalchemy/
--rw-r--r--   0 runner    (1001) docker     (123)     9869 2023-04-03 15:06:55.000000 ydb-3.2.1/ydb/sqlalchemy/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      662 2023-04-03 15:06:55.000000 ydb-3.2.1/ydb/sqlalchemy/types.py
--rw-r--r--   0 runner    (1001) docker     (123)    82321 2023-04-03 15:06:55.000000 ydb-3.2.1/ydb/table.py
--rw-r--r--   0 runner    (1001) docker     (123)     4895 2023-04-03 15:06:55.000000 ydb-3.2.1/ydb/table_test.py
--rw-r--r--   0 runner    (1001) docker     (123)    13062 2023-04-03 15:06:55.000000 ydb-3.2.1/ydb/topic.py
--rw-r--r--   0 runner    (1001) docker     (123)     4768 2023-04-03 15:06:55.000000 ydb-3.2.1/ydb/tracing.py
--rw-r--r--   0 runner    (1001) docker     (123)    11729 2023-04-03 15:06:55.000000 ydb-3.2.1/ydb/types.py
--rw-r--r--   0 runner    (1001) docker     (123)       18 2023-04-03 15:06:57.000000 ydb-3.2.1/ydb/ydb_version.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-03 15:07:04.724172 ydb-3.2.1/ydb.egg-info/
--rw-r--r--   0 runner    (1001) docker     (123)     1669 2023-04-03 15:07:04.000000 ydb-3.2.1/ydb.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)     8247 2023-04-03 15:07:04.000000 ydb-3.2.1/ydb.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-03 15:07:04.000000 ydb-3.2.1/ydb.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (123)       82 2023-04-03 15:07:04.000000 ydb-3.2.1/ydb.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (123)        4 2023-04-03 15:07:04.000000 ydb-3.2.1/ydb.egg-info/top_level.txt
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 11:52:04.444212 ydb-3.2.2/
+-rw-r--r--   0 runner    (1001) docker     (123)      220 2023-04-06 11:51:54.000000 ydb-3.2.2/AUTHORS
+-rw-r--r--   0 runner    (1001) docker     (123)    11361 2023-04-06 11:51:54.000000 ydb-3.2.2/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (123)       25 2023-04-06 11:51:54.000000 ydb-3.2.2/MANIFEST.in
+-rw-r--r--   0 runner    (1001) docker     (123)     1669 2023-04-06 11:52:04.444212 ydb-3.2.2/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     1126 2023-04-06 11:51:54.000000 ydb-3.2.2/README.md
+-rw-r--r--   0 runner    (1001) docker     (123)       31 2023-04-06 11:51:54.000000 ydb-3.2.2/pyproject.toml
+-rw-r--r--   0 runner    (1001) docker     (123)       64 2023-04-06 11:51:54.000000 ydb-3.2.2/requirements.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       38 2023-04-06 11:52:04.444212 ydb-3.2.2/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (123)     1127 2023-04-06 11:51:57.000000 ydb-3.2.2/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 11:52:04.444212 ydb-3.2.2/tests/
+-rw-r--r--   0 runner    (1001) docker     (123)      531 2023-04-06 11:51:54.000000 ydb-3.2.2/tests/test_errors.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 11:52:04.420212 ydb-3.2.2/ydb/
+-rw-r--r--   0 runner    (1001) docker     (123)      582 2023-04-06 11:51:54.000000 ydb-3.2.2/ydb/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3032 2023-04-06 11:51:54.000000 ydb-3.2.2/ydb/_apis.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1659 2023-04-06 11:51:54.000000 ydb-3.2.2/ydb/_errors.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 11:52:04.420212 ydb-3.2.2/ydb/_grpc/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 11:51:54.000000 ydb-3.2.2/ydb/_grpc/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 11:52:04.420212 ydb-3.2.2/ydb/_grpc/common/
+-rw-r--r--   0 runner    (1001) docker     (123)     1253 2023-04-06 11:51:54.000000 ydb-3.2.2/ydb/_grpc/common/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 11:52:04.420212 ydb-3.2.2/ydb/_grpc/grpcwrapper/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 11:51:54.000000 ydb-3.2.2/ydb/_grpc/grpcwrapper/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8273 2023-04-06 11:51:54.000000 ydb-3.2.2/ydb/_grpc/grpcwrapper/common_utils.py
+-rw-r--r--   0 runner    (1001) docker     (123)      719 2023-04-06 11:51:54.000000 ydb-3.2.2/ydb/_grpc/grpcwrapper/ydb_scheme.py
+-rw-r--r--   0 runner    (1001) docker     (123)    42335 2023-04-06 11:51:54.000000 ydb-3.2.2/ydb/_grpc/grpcwrapper/ydb_topic.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5865 2023-04-06 11:51:54.000000 ydb-3.2.2/ydb/_grpc/grpcwrapper/ydb_topic_public_types.py
+-rw-r--r--   0 runner    (1001) docker     (123)      726 2023-04-06 11:51:54.000000 ydb-3.2.2/ydb/_grpc/grpcwrapper/ydb_topic_test.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 11:52:04.424212 ydb-3.2.2/ydb/_grpc/v3/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 11:51:54.000000 ydb-3.2.2/ydb/_grpc/v3/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 11:52:04.428212 ydb-3.2.2/ydb/_grpc/v3/protos/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 11:51:54.000000 ydb-3.2.2/ydb/_grpc/v3/protos/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 11:52:04.428212 ydb-3.2.2/ydb/_grpc/v3/protos/annotations/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 11:51:54.000000 ydb-3.2.2/ydb/_grpc/v3/protos/annotations/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    12213 2023-04-06 11:51:54.000000 ydb-3.2.2/ydb/_grpc/v3/protos/annotations/validation_pb2.py
+-rw-r--r--   0 runner    (1001) docker     (123)      159 2023-04-06 11:51:54.000000 ydb-3.2.2/ydb/_grpc/v3/protos/annotations/validation_pb2_grpc.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6184 2023-04-06 11:51:54.000000 ydb-3.2.2/ydb/_grpc/v3/protos/ydb_auth_pb2.py
+-rw-r--r--   0 runner    (1001) docker     (123)      159 2023-04-06 11:51:54.000000 ydb-3.2.2/ydb/_grpc/v3/protos/ydb_auth_pb2_grpc.py
+-rw-r--r--   0 runner    (1001) docker     (123)    83179 2023-04-06 11:51:54.000000 ydb-3.2.2/ydb/_grpc/v3/protos/ydb_cms_pb2.py
+-rw-r--r--   0 runner    (1001) docker     (123)      159 2023-04-06 11:51:54.000000 ydb-3.2.2/ydb/_grpc/v3/protos/ydb_cms_pb2_grpc.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7124 2023-04-06 11:51:54.000000 ydb-3.2.2/ydb/_grpc/v3/protos/ydb_common_pb2.py
+-rw-r--r--   0 runner    (1001) docker     (123)      159 2023-04-06 11:51:54.000000 ydb-3.2.2/ydb/_grpc/v3/protos/ydb_common_pb2_grpc.py
+-rw-r--r--   0 runner    (1001) docker     (123)   121326 2023-04-06 11:51:54.000000 ydb-3.2.2/ydb/_grpc/v3/protos/ydb_coordination_pb2.py
+-rw-r--r--   0 runner    (1001) docker     (123)      159 2023-04-06 11:51:54.000000 ydb-3.2.2/ydb/_grpc/v3/protos/ydb_coordination_pb2_grpc.py
+-rw-r--r--   0 runner    (1001) docker     (123)    16470 2023-04-06 11:51:54.000000 ydb-3.2.2/ydb/_grpc/v3/protos/ydb_discovery_pb2.py
+-rw-r--r--   0 runner    (1001) docker     (123)      159 2023-04-06 11:51:54.000000 ydb-3.2.2/ydb/_grpc/v3/protos/ydb_discovery_pb2_grpc.py
+-rw-r--r--   0 runner    (1001) docker     (123)    41176 2023-04-06 11:51:54.000000 ydb-3.2.2/ydb/_grpc/v3/protos/ydb_export_pb2.py
+-rw-r--r--   0 runner    (1001) docker     (123)      159 2023-04-06 11:51:54.000000 ydb-3.2.2/ydb/_grpc/v3/protos/ydb_export_pb2_grpc.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4995 2023-04-06 11:51:54.000000 ydb-3.2.2/ydb/_grpc/v3/protos/ydb_formats_pb2.py
+-rw-r--r--   0 runner    (1001) docker     (123)      159 2023-04-06 11:51:54.000000 ydb-3.2.2/ydb/_grpc/v3/protos/ydb_formats_pb2_grpc.py
+-rw-r--r--   0 runner    (1001) docker     (123)    30782 2023-04-06 11:51:54.000000 ydb-3.2.2/ydb/_grpc/v3/protos/ydb_import_pb2.py
+-rw-r--r--   0 runner    (1001) docker     (123)      159 2023-04-06 11:51:54.000000 ydb-3.2.2/ydb/_grpc/v3/protos/ydb_import_pb2_grpc.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7161 2023-04-06 11:51:54.000000 ydb-3.2.2/ydb/_grpc/v3/protos/ydb_issue_message_pb2.py
+-rw-r--r--   0 runner    (1001) docker     (123)      159 2023-04-06 11:51:54.000000 ydb-3.2.2/ydb/_grpc/v3/protos/ydb_issue_message_pb2_grpc.py
+-rw-r--r--   0 runner    (1001) docker     (123)    72285 2023-04-06 11:51:54.000000 ydb-3.2.2/ydb/_grpc/v3/protos/ydb_monitoring_pb2.py
+-rw-r--r--   0 runner    (1001) docker     (123)      159 2023-04-06 11:51:54.000000 ydb-3.2.2/ydb/_grpc/v3/protos/ydb_monitoring_pb2_grpc.py
+-rw-r--r--   0 runner    (1001) docker     (123)    29771 2023-04-06 11:51:54.000000 ydb-3.2.2/ydb/_grpc/v3/protos/ydb_operation_pb2.py
+-rw-r--r--   0 runner    (1001) docker     (123)      159 2023-04-06 11:51:54.000000 ydb-3.2.2/ydb/_grpc/v3/protos/ydb_operation_pb2_grpc.py
+-rw-r--r--   0 runner    (1001) docker     (123)    16311 2023-04-06 11:51:54.000000 ydb-3.2.2/ydb/_grpc/v3/protos/ydb_query_stats_pb2.py
+-rw-r--r--   0 runner    (1001) docker     (123)      159 2023-04-06 11:51:54.000000 ydb-3.2.2/ydb/_grpc/v3/protos/ydb_query_stats_pb2_grpc.py
+-rw-r--r--   0 runner    (1001) docker     (123)    40278 2023-04-06 11:51:54.000000 ydb-3.2.2/ydb/_grpc/v3/protos/ydb_rate_limiter_pb2.py
+-rw-r--r--   0 runner    (1001) docker     (123)      159 2023-04-06 11:51:54.000000 ydb-3.2.2/ydb/_grpc/v3/protos/ydb_rate_limiter_pb2_grpc.py
+-rw-r--r--   0 runner    (1001) docker     (123)    38051 2023-04-06 11:51:54.000000 ydb-3.2.2/ydb/_grpc/v3/protos/ydb_scheme_pb2.py
+-rw-r--r--   0 runner    (1001) docker     (123)      159 2023-04-06 11:51:54.000000 ydb-3.2.2/ydb/_grpc/v3/protos/ydb_scheme_pb2_grpc.py
+-rw-r--r--   0 runner    (1001) docker     (123)    25816 2023-04-06 11:51:54.000000 ydb-3.2.2/ydb/_grpc/v3/protos/ydb_scripting_pb2.py
+-rw-r--r--   0 runner    (1001) docker     (123)      159 2023-04-06 11:51:54.000000 ydb-3.2.2/ydb/_grpc/v3/protos/ydb_scripting_pb2_grpc.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6884 2023-04-06 11:51:54.000000 ydb-3.2.2/ydb/_grpc/v3/protos/ydb_status_codes_pb2.py
+-rw-r--r--   0 runner    (1001) docker     (123)      159 2023-04-06 11:51:54.000000 ydb-3.2.2/ydb/_grpc/v3/protos/ydb_status_codes_pb2_grpc.py
+-rw-r--r--   0 runner    (1001) docker     (123)   332647 2023-04-06 11:51:54.000000 ydb-3.2.2/ydb/_grpc/v3/protos/ydb_table_pb2.py
+-rw-r--r--   0 runner    (1001) docker     (123)      159 2023-04-06 11:51:54.000000 ydb-3.2.2/ydb/_grpc/v3/protos/ydb_table_pb2_grpc.py
+-rw-r--r--   0 runner    (1001) docker     (123)   234296 2023-04-06 11:51:54.000000 ydb-3.2.2/ydb/_grpc/v3/protos/ydb_topic_pb2.py
+-rw-r--r--   0 runner    (1001) docker     (123)      159 2023-04-06 11:51:54.000000 ydb-3.2.2/ydb/_grpc/v3/protos/ydb_topic_pb2_grpc.py
+-rw-r--r--   0 runner    (1001) docker     (123)    52587 2023-04-06 11:51:54.000000 ydb-3.2.2/ydb/_grpc/v3/protos/ydb_value_pb2.py
+-rw-r--r--   0 runner    (1001) docker     (123)      159 2023-04-06 11:51:54.000000 ydb-3.2.2/ydb/_grpc/v3/protos/ydb_value_pb2_grpc.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1970 2023-04-06 11:51:54.000000 ydb-3.2.2/ydb/_grpc/v3/ydb_auth_v1_pb2.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2503 2023-04-06 11:51:54.000000 ydb-3.2.2/ydb/_grpc/v3/ydb_auth_v1_pb2_grpc.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4418 2023-04-06 11:51:54.000000 ydb-3.2.2/ydb/_grpc/v3/ydb_cms_v1_pb2.py
+-rw-r--r--   0 runner    (1001) docker     (123)    11170 2023-04-06 11:51:54.000000 ydb-3.2.2/ydb/_grpc/v3/ydb_cms_v1_pb2_grpc.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4226 2023-04-06 11:51:54.000000 ydb-3.2.2/ydb/_grpc/v3/ydb_coordination_v1_pb2.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9797 2023-04-06 11:51:54.000000 ydb-3.2.2/ydb/_grpc/v3/ydb_coordination_v1_pb2_grpc.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2610 2023-04-06 11:51:54.000000 ydb-3.2.2/ydb/_grpc/v3/ydb_discovery_v1_pb2.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4307 2023-04-06 11:51:54.000000 ydb-3.2.2/ydb/_grpc/v3/ydb_discovery_v1_pb2_grpc.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2512 2023-04-06 11:51:54.000000 ydb-3.2.2/ydb/_grpc/v3/ydb_export_v1_pb2.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4370 2023-04-06 11:51:54.000000 ydb-3.2.2/ydb/_grpc/v3/ydb_export_v1_pb2_grpc.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2527 2023-04-06 11:51:54.000000 ydb-3.2.2/ydb/_grpc/v3/ydb_import_v1_pb2.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4404 2023-04-06 11:51:54.000000 ydb-3.2.2/ydb/_grpc/v3/ydb_import_v1_pb2_grpc.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2622 2023-04-06 11:51:54.000000 ydb-3.2.2/ydb/_grpc/v3/ydb_monitoring_v1_pb2.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4293 2023-04-06 11:51:54.000000 ydb-3.2.2/ydb/_grpc/v3/ydb_monitoring_v1_pb2_grpc.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3688 2023-04-06 11:51:54.000000 ydb-3.2.2/ydb/_grpc/v3/ydb_operation_v1_pb2.py
+-rw-r--r--   0 runner    (1001) docker     (123)    10345 2023-04-06 11:51:54.000000 ydb-3.2.2/ydb/_grpc/v3/ydb_operation_v1_pb2_grpc.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4877 2023-04-06 11:51:54.000000 ydb-3.2.2/ydb/_grpc/v3/ydb_rate_limiter_v1_pb2.py
+-rw-r--r--   0 runner    (1001) docker     (123)    11754 2023-04-06 11:51:54.000000 ydb-3.2.2/ydb/_grpc/v3/ydb_rate_limiter_v1_pb2_grpc.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4012 2023-04-06 11:51:54.000000 ydb-3.2.2/ydb/_grpc/v3/ydb_scheme_v1_pb2.py
+-rw-r--r--   0 runner    (1001) docker     (123)    10044 2023-04-06 11:51:54.000000 ydb-3.2.2/ydb/_grpc/v3/ydb_scheme_v1_pb2_grpc.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3112 2023-04-06 11:51:55.000000 ydb-3.2.2/ydb/_grpc/v3/ydb_scripting_v1_pb2.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6037 2023-04-06 11:51:55.000000 ydb-3.2.2/ydb/_grpc/v3/ydb_scripting_v1_pb2_grpc.py
+-rw-r--r--   0 runner    (1001) docker     (123)    11659 2023-04-06 11:51:55.000000 ydb-3.2.2/ydb/_grpc/v3/ydb_table_v1_pb2.py
+-rw-r--r--   0 runner    (1001) docker     (123)    36535 2023-04-06 11:51:55.000000 ydb-3.2.2/ydb/_grpc/v3/ydb_table_v1_pb2_grpc.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4956 2023-04-06 11:51:55.000000 ydb-3.2.2/ydb/_grpc/v3/ydb_topic_v1_pb2.py
+-rw-r--r--   0 runner    (1001) docker     (123)    14404 2023-04-06 11:51:55.000000 ydb-3.2.2/ydb/_grpc/v3/ydb_topic_v1_pb2_grpc.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 11:52:04.432212 ydb-3.2.2/ydb/_grpc/v4/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 11:51:55.000000 ydb-3.2.2/ydb/_grpc/v4/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 11:52:04.436212 ydb-3.2.2/ydb/_grpc/v4/protos/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 11:51:55.000000 ydb-3.2.2/ydb/_grpc/v4/protos/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 11:52:04.436212 ydb-3.2.2/ydb/_grpc/v4/protos/annotations/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 11:51:55.000000 ydb-3.2.2/ydb/_grpc/v4/protos/annotations/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2727 2023-04-06 11:51:55.000000 ydb-3.2.2/ydb/_grpc/v4/protos/annotations/validation_pb2.py
+-rw-r--r--   0 runner    (1001) docker     (123)      159 2023-04-06 11:51:55.000000 ydb-3.2.2/ydb/_grpc/v4/protos/annotations/validation_pb2_grpc.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1747 2023-04-06 11:51:55.000000 ydb-3.2.2/ydb/_grpc/v4/protos/ydb_auth_pb2.py
+-rw-r--r--   0 runner    (1001) docker     (123)      159 2023-04-06 11:51:55.000000 ydb-3.2.2/ydb/_grpc/v4/protos/ydb_auth_pb2_grpc.py
+-rw-r--r--   0 runner    (1001) docker     (123)    12062 2023-04-06 11:51:55.000000 ydb-3.2.2/ydb/_grpc/v4/protos/ydb_cms_pb2.py
+-rw-r--r--   0 runner    (1001) docker     (123)      159 2023-04-06 11:51:55.000000 ydb-3.2.2/ydb/_grpc/v4/protos/ydb_cms_pb2_grpc.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1882 2023-04-06 11:51:55.000000 ydb-3.2.2/ydb/_grpc/v4/protos/ydb_common_pb2.py
+-rw-r--r--   0 runner    (1001) docker     (123)      159 2023-04-06 11:51:55.000000 ydb-3.2.2/ydb/_grpc/v4/protos/ydb_common_pb2_grpc.py
+-rw-r--r--   0 runner    (1001) docker     (123)    15716 2023-04-06 11:51:55.000000 ydb-3.2.2/ydb/_grpc/v4/protos/ydb_coordination_pb2.py
+-rw-r--r--   0 runner    (1001) docker     (123)      159 2023-04-06 11:51:55.000000 ydb-3.2.2/ydb/_grpc/v4/protos/ydb_coordination_pb2_grpc.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2871 2023-04-06 11:51:55.000000 ydb-3.2.2/ydb/_grpc/v4/protos/ydb_discovery_pb2.py
+-rw-r--r--   0 runner    (1001) docker     (123)      159 2023-04-06 11:51:55.000000 ydb-3.2.2/ydb/_grpc/v4/protos/ydb_discovery_pb2_grpc.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9313 2023-04-06 11:51:55.000000 ydb-3.2.2/ydb/_grpc/v4/protos/ydb_export_pb2.py
+-rw-r--r--   0 runner    (1001) docker     (123)      159 2023-04-06 11:51:55.000000 ydb-3.2.2/ydb/_grpc/v4/protos/ydb_export_pb2_grpc.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1514 2023-04-06 11:51:55.000000 ydb-3.2.2/ydb/_grpc/v4/protos/ydb_formats_pb2.py
+-rw-r--r--   0 runner    (1001) docker     (123)      159 2023-04-06 11:51:55.000000 ydb-3.2.2/ydb/_grpc/v4/protos/ydb_formats_pb2_grpc.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6939 2023-04-06 11:51:55.000000 ydb-3.2.2/ydb/_grpc/v4/protos/ydb_import_pb2.py
+-rw-r--r--   0 runner    (1001) docker     (123)      159 2023-04-06 11:51:55.000000 ydb-3.2.2/ydb/_grpc/v4/protos/ydb_import_pb2_grpc.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1770 2023-04-06 11:51:55.000000 ydb-3.2.2/ydb/_grpc/v4/protos/ydb_issue_message_pb2.py
+-rw-r--r--   0 runner    (1001) docker     (123)      159 2023-04-06 11:51:55.000000 ydb-3.2.2/ydb/_grpc/v4/protos/ydb_issue_message_pb2_grpc.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9769 2023-04-06 11:51:55.000000 ydb-3.2.2/ydb/_grpc/v4/protos/ydb_monitoring_pb2.py
+-rw-r--r--   0 runner    (1001) docker     (123)      159 2023-04-06 11:51:55.000000 ydb-3.2.2/ydb/_grpc/v4/protos/ydb_monitoring_pb2_grpc.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6165 2023-04-06 11:51:55.000000 ydb-3.2.2/ydb/_grpc/v4/protos/ydb_operation_pb2.py
+-rw-r--r--   0 runner    (1001) docker     (123)      159 2023-04-06 11:51:55.000000 ydb-3.2.2/ydb/_grpc/v4/protos/ydb_operation_pb2_grpc.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2849 2023-04-06 11:51:55.000000 ydb-3.2.2/ydb/_grpc/v4/protos/ydb_query_stats_pb2.py
+-rw-r--r--   0 runner    (1001) docker     (123)      159 2023-04-06 11:51:55.000000 ydb-3.2.2/ydb/_grpc/v4/protos/ydb_query_stats_pb2_grpc.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6057 2023-04-06 11:51:55.000000 ydb-3.2.2/ydb/_grpc/v4/protos/ydb_rate_limiter_pb2.py
+-rw-r--r--   0 runner    (1001) docker     (123)      159 2023-04-06 11:51:55.000000 ydb-3.2.2/ydb/_grpc/v4/protos/ydb_rate_limiter_pb2_grpc.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5830 2023-04-06 11:51:55.000000 ydb-3.2.2/ydb/_grpc/v4/protos/ydb_scheme_pb2.py
+-rw-r--r--   0 runner    (1001) docker     (123)      159 2023-04-06 11:51:55.000000 ydb-3.2.2/ydb/_grpc/v4/protos/ydb_scheme_pb2_grpc.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5143 2023-04-06 11:51:55.000000 ydb-3.2.2/ydb/_grpc/v4/protos/ydb_scripting_pb2.py
+-rw-r--r--   0 runner    (1001) docker     (123)      159 2023-04-06 11:51:55.000000 ydb-3.2.2/ydb/_grpc/v4/protos/ydb_scripting_pb2_grpc.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2153 2023-04-06 11:51:55.000000 ydb-3.2.2/ydb/_grpc/v4/protos/ydb_status_codes_pb2.py
+-rw-r--r--   0 runner    (1001) docker     (123)      159 2023-04-06 11:51:55.000000 ydb-3.2.2/ydb/_grpc/v4/protos/ydb_status_codes_pb2_grpc.py
+-rw-r--r--   0 runner    (1001) docker     (123)    46408 2023-04-06 11:51:55.000000 ydb-3.2.2/ydb/_grpc/v4/protos/ydb_table_pb2.py
+-rw-r--r--   0 runner    (1001) docker     (123)      159 2023-04-06 11:51:55.000000 ydb-3.2.2/ydb/_grpc/v4/protos/ydb_table_pb2_grpc.py
+-rw-r--r--   0 runner    (1001) docker     (123)    34953 2023-04-06 11:51:55.000000 ydb-3.2.2/ydb/_grpc/v4/protos/ydb_topic_pb2.py
+-rw-r--r--   0 runner    (1001) docker     (123)      159 2023-04-06 11:51:55.000000 ydb-3.2.2/ydb/_grpc/v4/protos/ydb_topic_pb2_grpc.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6618 2023-04-06 11:51:55.000000 ydb-3.2.2/ydb/_grpc/v4/protos/ydb_value_pb2.py
+-rw-r--r--   0 runner    (1001) docker     (123)      159 2023-04-06 11:51:55.000000 ydb-3.2.2/ydb/_grpc/v4/protos/ydb_value_pb2_grpc.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1325 2023-04-06 11:51:55.000000 ydb-3.2.2/ydb/_grpc/v4/ydb_auth_v1_pb2.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2503 2023-04-06 11:51:55.000000 ydb-3.2.2/ydb/_grpc/v4/ydb_auth_v1_pb2_grpc.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1868 2023-04-06 11:51:55.000000 ydb-3.2.2/ydb/_grpc/v4/ydb_cms_v1_pb2.py
+-rw-r--r--   0 runner    (1001) docker     (123)    11170 2023-04-06 11:51:55.000000 ydb-3.2.2/ydb/_grpc/v4/ydb_cms_v1_pb2_grpc.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1937 2023-04-06 11:51:55.000000 ydb-3.2.2/ydb/_grpc/v4/ydb_coordination_v1_pb2.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9797 2023-04-06 11:51:55.000000 ydb-3.2.2/ydb/_grpc/v4/ydb_coordination_v1_pb2_grpc.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1518 2023-04-06 11:51:55.000000 ydb-3.2.2/ydb/_grpc/v4/ydb_discovery_v1_pb2.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4307 2023-04-06 11:51:55.000000 ydb-3.2.2/ydb/_grpc/v4/ydb_discovery_v1_pb2_grpc.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1461 2023-04-06 11:51:55.000000 ydb-3.2.2/ydb/_grpc/v4/ydb_export_v1_pb2.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4370 2023-04-06 11:51:55.000000 ydb-3.2.2/ydb/_grpc/v4/ydb_export_v1_pb2_grpc.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1468 2023-04-06 11:51:55.000000 ydb-3.2.2/ydb/_grpc/v4/ydb_import_v1_pb2.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4404 2023-04-06 11:51:55.000000 ydb-3.2.2/ydb/_grpc/v4/ydb_import_v1_pb2_grpc.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1519 2023-04-06 11:51:55.000000 ydb-3.2.2/ydb/_grpc/v4/ydb_monitoring_v1_pb2.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4293 2023-04-06 11:51:55.000000 ydb-3.2.2/ydb/_grpc/v4/ydb_monitoring_v1_pb2_grpc.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1776 2023-04-06 11:51:55.000000 ydb-3.2.2/ydb/_grpc/v4/ydb_operation_v1_pb2.py
+-rw-r--r--   0 runner    (1001) docker     (123)    10345 2023-04-06 11:51:55.000000 ydb-3.2.2/ydb/_grpc/v4/ydb_operation_v1_pb2_grpc.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2097 2023-04-06 11:51:55.000000 ydb-3.2.2/ydb/_grpc/v4/ydb_rate_limiter_v1_pb2.py
+-rw-r--r--   0 runner    (1001) docker     (123)    11754 2023-04-06 11:51:55.000000 ydb-3.2.2/ydb/_grpc/v4/ydb_rate_limiter_v1_pb2_grpc.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1789 2023-04-06 11:51:55.000000 ydb-3.2.2/ydb/_grpc/v4/ydb_scheme_v1_pb2.py
+-rw-r--r--   0 runner    (1001) docker     (123)    10044 2023-04-06 11:51:55.000000 ydb-3.2.2/ydb/_grpc/v4/ydb_scheme_v1_pb2_grpc.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1621 2023-04-06 11:51:55.000000 ydb-3.2.2/ydb/_grpc/v4/ydb_scripting_v1_pb2.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6037 2023-04-06 11:51:55.000000 ydb-3.2.2/ydb/_grpc/v4/ydb_scripting_v1_pb2_grpc.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3453 2023-04-06 11:51:55.000000 ydb-3.2.2/ydb/_grpc/v4/ydb_table_v1_pb2.py
+-rw-r--r--   0 runner    (1001) docker     (123)    36535 2023-04-06 11:51:55.000000 ydb-3.2.2/ydb/_grpc/v4/ydb_table_v1_pb2_grpc.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2038 2023-04-06 11:51:55.000000 ydb-3.2.2/ydb/_grpc/v4/ydb_topic_v1_pb2.py
+-rw-r--r--   0 runner    (1001) docker     (123)    14404 2023-04-06 11:51:55.000000 ydb-3.2.2/ydb/_grpc/v4/ydb_topic_v1_pb2_grpc.py
+-rw-r--r--   0 runner    (1001) docker     (123)    16278 2023-04-06 11:51:55.000000 ydb-3.2.2/ydb/_session_impl.py
+-rw-r--r--   0 runner    (1001) docker     (123)    14424 2023-04-06 11:51:55.000000 ydb-3.2.2/ydb/_sp_impl.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 11:52:04.436212 ydb-3.2.2/ydb/_topic_common/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 11:51:55.000000 ydb-3.2.2/ydb/_topic_common/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4659 2023-04-06 11:51:55.000000 ydb-3.2.2/ydb/_topic_common/common.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7957 2023-04-06 11:51:55.000000 ydb-3.2.2/ydb/_topic_common/common_test.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1966 2023-04-06 11:51:55.000000 ydb-3.2.2/ydb/_topic_common/test_helpers.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 11:52:04.440212 ydb-3.2.2/ydb/_topic_reader/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 11:51:55.000000 ydb-3.2.2/ydb/_topic_reader/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5528 2023-04-06 11:51:55.000000 ydb-3.2.2/ydb/_topic_reader/datatypes.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7350 2023-04-06 11:51:55.000000 ydb-3.2.2/ydb/_topic_reader/datatypes_test.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2529 2023-04-06 11:51:55.000000 ydb-3.2.2/ydb/_topic_reader/topic_reader.py
+-rw-r--r--   0 runner    (1001) docker     (123)    22781 2023-04-06 11:51:55.000000 ydb-3.2.2/ydb/_topic_reader/topic_reader_asyncio.py
+-rw-r--r--   0 runner    (1001) docker     (123)    46742 2023-04-06 11:51:55.000000 ydb-3.2.2/ydb/_topic_reader/topic_reader_asyncio_test.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5469 2023-04-06 11:51:55.000000 ydb-3.2.2/ydb/_topic_reader/topic_reader_sync.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 11:52:04.440212 ydb-3.2.2/ydb/_topic_writer/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 11:51:55.000000 ydb-3.2.2/ydb/_topic_writer/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8093 2023-04-06 11:51:55.000000 ydb-3.2.2/ydb/_topic_writer/topic_writer.py
+-rw-r--r--   0 runner    (1001) docker     (123)    23229 2023-04-06 11:51:55.000000 ydb-3.2.2/ydb/_topic_writer/topic_writer_asyncio.py
+-rw-r--r--   0 runner    (1001) docker     (123)    24156 2023-04-06 11:51:55.000000 ydb-3.2.2/ydb/_topic_writer/topic_writer_asyncio_test.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3376 2023-04-06 11:51:55.000000 ydb-3.2.2/ydb/_topic_writer/topic_writer_sync.py
+-rw-r--r--   0 runner    (1001) docker     (123)      951 2023-04-06 11:51:55.000000 ydb-3.2.2/ydb/_topic_writer/topic_writer_test.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5653 2023-04-06 11:51:55.000000 ydb-3.2.2/ydb/_tx_ctx_impl.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4130 2023-04-06 11:51:55.000000 ydb-3.2.2/ydb/_utilities.py
+-rw-r--r--   0 runner    (1001) docker     (123)      281 2023-04-06 11:51:55.000000 ydb-3.2.2/ydb/_utilities_test.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 11:52:04.440212 ydb-3.2.2/ydb/aio/
+-rw-r--r--   0 runner    (1001) docker     (123)       91 2023-04-06 11:51:55.000000 ydb-3.2.2/ydb/aio/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      462 2023-04-06 11:51:55.000000 ydb-3.2.2/ydb/aio/_utilities.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8402 2023-04-06 11:51:55.000000 ydb-3.2.2/ydb/aio/connection.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3402 2023-04-06 11:51:55.000000 ydb-3.2.2/ydb/aio/credentials.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1877 2023-04-06 11:51:55.000000 ydb-3.2.2/ydb/aio/driver.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4831 2023-04-06 11:51:55.000000 ydb-3.2.2/ydb/aio/iam.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8745 2023-04-06 11:51:55.000000 ydb-3.2.2/ydb/aio/pool.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2128 2023-04-06 11:51:55.000000 ydb-3.2.2/ydb/aio/resolver.py
+-rw-r--r--   0 runner    (1001) docker     (123)      838 2023-04-06 11:51:55.000000 ydb-3.2.2/ydb/aio/scheme.py
+-rw-r--r--   0 runner    (1001) docker     (123)    18011 2023-04-06 11:51:55.000000 ydb-3.2.2/ydb/aio/table.py
+-rw-r--r--   0 runner    (1001) docker     (123)      304 2023-04-06 11:51:55.000000 ydb-3.2.2/ydb/auth_helpers.py
+-rw-r--r--   0 runner    (1001) docker     (123)    18813 2023-04-06 11:51:55.000000 ydb-3.2.2/ydb/connection.py
+-rw-r--r--   0 runner    (1001) docker     (123)    15107 2023-04-06 11:51:55.000000 ydb-3.2.2/ydb/convert.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7135 2023-04-06 11:51:55.000000 ydb-3.2.2/ydb/credentials.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 11:52:04.444212 ydb-3.2.2/ydb/dbapi/
+-rw-r--r--   0 runner    (1001) docker     (123)      711 2023-04-06 11:51:55.000000 ydb-3.2.2/ydb/dbapi/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2569 2023-04-06 11:51:55.000000 ydb-3.2.2/ydb/dbapi/connection.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5002 2023-04-06 11:51:55.000000 ydb-3.2.2/ydb/dbapi/cursor.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2174 2023-04-06 11:51:55.000000 ydb-3.2.2/ydb/dbapi/errors.py
+-rw-r--r--   0 runner    (1001) docker     (123)   285865 2023-04-06 11:51:55.000000 ydb-3.2.2/ydb/default_pem.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9311 2023-04-06 11:51:55.000000 ydb-3.2.2/ydb/driver.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7769 2023-04-06 11:51:55.000000 ydb-3.2.2/ydb/export.py
+-rw-r--r--   0 runner    (1001) docker     (123)      625 2023-04-06 11:51:55.000000 ydb-3.2.2/ydb/global_settings.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 11:52:04.444212 ydb-3.2.2/ydb/iam/
+-rw-r--r--   0 runner    (1001) docker     (123)      125 2023-04-06 11:51:55.000000 ydb-3.2.2/ydb/iam/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6296 2023-04-06 11:51:55.000000 ydb-3.2.2/ydb/iam/auth.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4376 2023-04-06 11:51:55.000000 ydb-3.2.2/ydb/import_client.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2336 2023-04-06 11:51:55.000000 ydb-3.2.2/ydb/interceptor.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4950 2023-04-06 11:51:55.000000 ydb-3.2.2/ydb/issues.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2973 2023-04-06 11:51:55.000000 ydb-3.2.2/ydb/operation.py
+-rw-r--r--   0 runner    (1001) docker     (123)    16567 2023-04-06 11:51:55.000000 ydb-3.2.2/ydb/pool.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6878 2023-04-06 11:51:55.000000 ydb-3.2.2/ydb/resolver.py
+-rw-r--r--   0 runner    (1001) docker     (123)    14271 2023-04-06 11:51:55.000000 ydb-3.2.2/ydb/scheme.py
+-rw-r--r--   0 runner    (1001) docker     (123)      810 2023-04-06 11:51:55.000000 ydb-3.2.2/ydb/scheme_test.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3384 2023-04-06 11:51:55.000000 ydb-3.2.2/ydb/scripting.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3937 2023-04-06 11:51:55.000000 ydb-3.2.2/ydb/settings.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 11:52:04.444212 ydb-3.2.2/ydb/sqlalchemy/
+-rw-r--r--   0 runner    (1001) docker     (123)     9869 2023-04-06 11:51:55.000000 ydb-3.2.2/ydb/sqlalchemy/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      662 2023-04-06 11:51:55.000000 ydb-3.2.2/ydb/sqlalchemy/types.py
+-rw-r--r--   0 runner    (1001) docker     (123)    82321 2023-04-06 11:51:55.000000 ydb-3.2.2/ydb/table.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4895 2023-04-06 11:51:55.000000 ydb-3.2.2/ydb/table_test.py
+-rw-r--r--   0 runner    (1001) docker     (123)    13062 2023-04-06 11:51:55.000000 ydb-3.2.2/ydb/topic.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4768 2023-04-06 11:51:55.000000 ydb-3.2.2/ydb/tracing.py
+-rw-r--r--   0 runner    (1001) docker     (123)    11729 2023-04-06 11:51:55.000000 ydb-3.2.2/ydb/types.py
+-rw-r--r--   0 runner    (1001) docker     (123)       18 2023-04-06 11:51:57.000000 ydb-3.2.2/ydb/ydb_version.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 11:52:04.444212 ydb-3.2.2/ydb.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)     1669 2023-04-06 11:52:04.000000 ydb-3.2.2/ydb.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     8064 2023-04-06 11:52:04.000000 ydb-3.2.2/ydb.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-06 11:52:04.000000 ydb-3.2.2/ydb.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       82 2023-04-06 11:52:04.000000 ydb-3.2.2/ydb.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        4 2023-04-06 11:52:04.000000 ydb-3.2.2/ydb.egg-info/top_level.txt
```

### Comparing `ydb-3.2.1/LICENSE` & `ydb-3.2.2/LICENSE`

 * *Files identical despite different names*

### Comparing `ydb-3.2.1/PKG-INFO` & `ydb-3.2.2/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: ydb
-Version: 3.2.1
+Version: 3.2.2
 Summary: YDB Python SDK
 Home-page: http://github.com/ydb-platform/ydb-python-sdk
 Author: Yandex LLC
 Author-email: ydb@yandex-team.ru
 License: Apache 2.0
 Classifier: Programming Language :: Python
 Classifier: Programming Language :: Python :: 2
```

### Comparing `ydb-3.2.1/README.md` & `ydb-3.2.2/README.md`

 * *Files identical despite different names*

### Comparing `ydb-3.2.1/setup.py` & `ydb-3.2.2/setup.py`

 * *Files 8% similar despite different names*

```diff
@@ -9,15 +9,15 @@
     for line in r.readlines():
         line = line.strip()
         if line != "":
             requirements.append(line)
 
 setuptools.setup(
     name="ydb",
-    version="3.2.1",  # AUTOVERSION
+    version="3.2.2",  # AUTOVERSION
     description="YDB Python SDK",
     author="Yandex LLC",
     author_email="ydb@yandex-team.ru",
     url="http://github.com/ydb-platform/ydb-python-sdk",
     license="Apache 2.0",
     package_dir={"": "."},
     long_description=long_description,
```

### Comparing `ydb-3.2.1/tests/test_errors.py` & `ydb-3.2.2/tests/test_errors.py`

 * *Files identical despite different names*

### Comparing `ydb-3.2.1/ydb/__init__.py` & `ydb-3.2.2/ydb/__init__.py`

 * *Files identical despite different names*

### Comparing `ydb-3.2.1/ydb/_apis.py` & `ydb-3.2.2/ydb/_apis.py`

 * *Files identical despite different names*

### Comparing `ydb-3.2.1/ydb/_dbapi/connection.py` & `ydb-3.2.2/ydb/dbapi/connection.py`

 * *Files 13% similar despite different names*

```diff
@@ -1,33 +1,48 @@
+from __future__ import absolute_import, unicode_literals
+
 import posixpath
 
 import ydb
 from .cursor import Cursor
 from .errors import DatabaseError
 
 
-class Connection:
+class Connection(object):
+
+    deiver = None
+    pool = None
+
     def __init__(self, endpoint, database=None, **conn_kwargs):
         self.endpoint = endpoint
         self.database = database
-        self.driver = self._create_driver(self.endpoint, self.database, **conn_kwargs)
-        self.pool = ydb.SessionPool(self.driver)
+        self._conn_kwargs = conn_kwargs
+        driver, pool = self._create_driver(self.endpoint, self.database, **conn_kwargs)
+        self.driver = driver
+        self.pool = pool
 
     def cursor(self):
         return Cursor(self)
 
+    def execute(self, sql, parameters=None):
+        return self.cursor().execute(sql, parameters)
+
+    def executemany(self, sql, parameters):
+        return self.cursor().executemany(sql, parameters)
+
     def describe(self, table_path):
         full_path = posixpath.join(self.database, table_path)
         try:
             res = self.pool.retry_operation_sync(lambda cli: cli.describe_table(full_path))
             return res.columns
         except ydb.Error as e:
             raise DatabaseError(e.message, e.issues, e.status)
+
         except Exception:
-            raise DatabaseError(f"Failed to describe table {table_path}")
+            raise DatabaseError("Failed to describe table %r" % (table_path,))
 
     def check_exists(self, table_path):
         try:
             self.driver.scheme_client.describe_path(table_path)
             return True
         except ydb.SchemeError:
             return False
@@ -35,35 +50,38 @@
     def commit(self):
         pass
 
     def rollback(self):
         pass
 
     def close(self):
-        if self.pool:
+        if self.pool is not None:
             self.pool.stop()
-        if self.driver:
+        if self.driver is not None:
             self.driver.stop()
 
     @staticmethod
+    def _create_endpoint(host, port):
+        return "%s:%d" % (host, port)
+
+    @staticmethod
     def _create_driver(endpoint, database, **conn_kwargs):
-        # TODO: add cache for initialized drivers/pools?
         driver_config = ydb.DriverConfig(
             endpoint,
             database=database,
             table_client_settings=ydb.TableClientSettings()
             .with_native_date_in_result_sets(True)
             .with_native_datetime_in_result_sets(True)
-            .with_native_timestamp_in_result_sets(True)
-            .with_native_interval_in_result_sets(True)
             .with_native_json_in_result_sets(True),
-            **conn_kwargs,
+            **conn_kwargs
         )
         driver = ydb.Driver(driver_config)
         try:
             driver.wait(timeout=5, fail_fast=True)
         except ydb.Error as e:
             raise DatabaseError(e.message, e.issues, e.status)
+
         except Exception:
             driver.stop()
-            raise DatabaseError(f"Failed to connect to YDB, details {driver.discovery_debug_details()}")
-        return driver
+            raise DatabaseError("Failed to connect to YDB, details %s" % driver.discovery_debug_details())
+
+        return driver, ydb.SessionPool(driver)
```

### Comparing `ydb-3.2.1/ydb/_dbapi/cursor.py` & `ydb-3.2.2/ydb/dbapi/cursor.py`

 * *Files 12% similar despite different names*

```diff
@@ -1,140 +1,133 @@
+from __future__ import absolute_import, unicode_literals
+
+import collections
 import datetime
 import itertools
 import logging
-import uuid
-import decimal
-import string
 
 import ydb
-from .errors import DatabaseError, ProgrammingError
+from .errors import DatabaseError
 
 
-logger = logging.getLogger(__name__)
+LOGGER = logging.getLogger(__name__)
 
 
-identifier_starts = {x for x in itertools.chain(string.ascii_letters, "_")}
-valid_identifier_chars = {x for x in itertools.chain(identifier_starts, string.digits)}
+STR_QUOTE_MAP = (
+    ("\\", "\\\\"),
+    ("'", r"\'"),
+    ("\0", r"\x00"),
+    # To re-check: \b \f \r \n \t
+)
 
 
-def check_identifier_valid(idt: str):
-    valid = idt and idt[0] in identifier_starts and all(c in valid_identifier_chars for c in idt)
-    if not valid:
-        raise ProgrammingError(f"Invalid identifier {idt}")
-    return valid
+def render_str(value):
+    for r_from, r_to in STR_QUOTE_MAP:
+        value = value.replace(r_from, r_to)
+    return "'" + value + "'"
 
 
-def get_column_type(type_obj):
-    return str(ydb.convert.type_to_native(type_obj))
+def render_date(value):
+    return "Date({})".format(render_str(value.isoformat()))
 
 
-def _generate_type_str(value):
-    tvalue = type(value)
+def render_datetime(value):
+    # TODO: is there a better solution for this?
+    return "DateTime::MakeDatetime(DateTime::ParseIso8601({}))".format(render_str(value.isoformat()))
 
-    stype = {
-        bool: "Bool",
-        bytes: "String",
-        str: "Utf8",
-        int: "Int64",
-        float: "Double",
-        decimal.Decimal: "Decimal(22, 9)",
-        datetime.date: "Date",
-        datetime.datetime: "Timestamp",
-        datetime.timedelta: "Interval",
-        uuid.UUID: "Uuid",
-    }.get(tvalue)
 
-    if tvalue == dict:
-        types_lst = ", ".join(f"{k}: {_generate_type_str(v)}" for k, v in value.items())
-        stype = f"Struct<{types_lst}>"
+def render(value):
+    if value is None:
+        return "NULL"
+    if isinstance(value, str):
+        return render_str(value)
+    if isinstance(value, datetime.datetime):
+        return render_datetime(value)
+    if isinstance(value, datetime.date):
+        return render_date(value)
+    return repr(value)
 
-    elif tvalue == tuple:
-        types_lst = ", ".join(_generate_type_str(x) for x in value)
-        stype = f"Tuple<{types_lst}>"
 
-    elif tvalue == list:
-        nested_type = _generate_type_str(value[0])
-        stype = f"List<{nested_type}>"
+def render_sql(sql, parameters):
+    if not parameters:
+        return sql
 
-    elif tvalue == set:
-        nested_type = _generate_type_str(next(iter(value)))
-        stype = f"Set<{nested_type}>"
+    assert sql.count("?") == len(parameters), "num of placeholders != num of params"
 
-    if stype is None:
-        raise ProgrammingError(f"Cannot translate value {value} (type {tvalue}) to ydb type.")
+    quoted_params = [render(param) for param in parameters]
+    quoted_params += [""]
+    sql_pieces = sql.split("?")
+    assert len(sql_pieces) == len(quoted_params)
+    return "".join(piece for pair in zip(sql_pieces, quoted_params) for piece in pair if piece)
 
-    return stype
 
+def named_result_for(column_names):
+    # TODO fix: this doesn't allow columns names starting with underscore, e.g. `select 1 as _a`.
+    return collections.namedtuple("NamedResult", column_names)
 
-def _generate_declare_stms(params: dict) -> str:
-    return "".join(f"DECLARE {k} AS {_generate_type_str(t)}; " for k, t in params.items())
+
+def _get_column_type(type_obj):
+    return str(type_obj)
+
+
+def get_column_type(type_obj):
+    return _get_column_type(ydb.convert.type_to_native(type_obj))
 
 
 class Cursor(object):
     def __init__(self, connection):
         self.connection = connection
-        self.description = None
+        self.description = []
         self.arraysize = 1
+        self.logger = LOGGER
         self.rows = None
         self._rows_prefetched = None
 
-    def execute(self, sql, parameters=None, context=None):
-        self.description = None
-        sql_params = None
-
-        if parameters:
-            for name in parameters.keys():
-                check_identifier_valid(name)
-            sql = sql % {k: f"${k}" for k, v in parameters.items()}
-            sql_params = {f"${k}": v for k, v in parameters.items()}
-            declare_stms = _generate_declare_stms(sql_params)
-            sql = f"{declare_stms}{sql}"
-
-        logger.info("execute sql: %s, params: %s", sql, sql_params)
-
-        def _execute_in_pool(cli):
-            try:
-                if context and context.get("isddl"):
-                    return cli.execute_scheme(sql)
-                else:
-                    prepared_query = cli.prepare(sql)
-                    return cli.transaction().execute(prepared_query, sql_params, commit_tx=True)
-            except ydb.Error as e:
-                raise DatabaseError(e.message, e.issues, e.status)
+    def execute(self, sql, parameters=None):
+        fsql = render_sql(sql, parameters)
+        self.logger.debug("execute sql: %s", fsql)
+        try:
+            chunks = self.connection.driver.table_client.scan_query(fsql)
+        except ydb.Error as e:
+            raise DatabaseError(e.message, e.issues, e.status)
+
+        self.description = []
 
-        chunks = self.connection.pool.retry_operation_sync(_execute_in_pool)
         rows = self._rows_iterable(chunks)
         # Prefetch the description:
         try:
             first_row = next(rows)
         except StopIteration:
             pass
         else:
             rows = itertools.chain((first_row,), rows)
         if self.rows is not None:
             rows = itertools.chain(self.rows, rows)
 
         self.rows = rows
 
     def _rows_iterable(self, chunks_iterable):
+        description = None
         try:
             for chunk in chunks_iterable:
-                self.description = [
-                    (
-                        col.name,
-                        get_column_type(col.type),
-                        None,
-                        None,
-                        None,
-                        None,
-                        None,
-                    )
-                    for col in chunk.columns
-                ]
-                for row in chunk.rows:
+                if description is None and len(chunk.result_set.rows) > 0:
+                    description = [
+                        (
+                            col.name,
+                            get_column_type(col.type),
+                            None,
+                            None,
+                            None,
+                            None,
+                            None,
+                        )
+                        for col in chunk.result_set.columns
+                    ]
+                    self.description = description
+                for row in chunk.result_set.rows:
                     # returns tuple to be compatible with SqlAlchemy and because
                     #  of this PEP to return a sequence: https://www.python.org/dev/peps/pep-0249/#fetchmany
                     yield row[::]
         except ydb.Error as e:
             raise DatabaseError(e.message, e.issues, e.status)
 
     def _ensure_prefetched(self):
@@ -147,18 +140,26 @@
         for parameters in seq_of_parameters:
             self.execute(sql, parameters)
 
     def executescript(self, script):
         return self.execute(script)
 
     def fetchone(self):
-        return next(self.rows or [], None)
+        if self.rows is None:
+            return None
+        try:
+            return next(self.rows)
+        except StopIteration:
+            return None
 
     def fetchmany(self, size=None):
-        return list(itertools.islice(self.rows, size or self.arraysize))
+        if size is None:
+            size = self.arraysize
+
+        return list(itertools.islice(self.rows, size))
 
     def fetchall(self):
         return list(self.rows)
 
     def nextset(self):
         self.fetchall()
```

### Comparing `ydb-3.2.1/ydb/_dbapi/errors.py` & `ydb-3.2.2/ydb/dbapi/errors.py`

 * *Files 13% similar despite different names*

```diff
@@ -1,18 +1,20 @@
 class Warning(Exception):
     pass
 
 
 class Error(Exception):
     def __init__(self, message, issues=None, status=None):
-        super(Error, self).__init__(message)
 
         pretty_issues = _pretty_issues(issues)
+        message = message if pretty_issues is None else pretty_issues
+
+        super(Error, self).__init__(message)
         self.issues = issues
-        self.message = pretty_issues or message
+        self.message = message
         self.status = status
 
 
 class InterfaceError(Error):
     pass
 
 
@@ -55,37 +57,46 @@
 
     return "\n" + "\n".join(children_messages)
 
 
 def _get_messages(issue, max_depth=100, indent=2, depth=0, root=False):
     if depth >= max_depth:
         return None
-
     margin_str = " " * depth * indent
     pre_message = ""
     children = ""
-
     if issue.issues:
         collapsed_messages = []
         while not root and len(issue.issues) == 1:
             collapsed_messages.append(issue.message)
             issue = issue.issues[0]
-
         if collapsed_messages:
-            pre_message = f"{margin_str}{', '.join(collapsed_messages)}\n"
+            pre_message = margin_str + ", ".join(collapsed_messages) + "\n"
             depth += 1
             margin_str = " " * depth * indent
+        else:
+            pre_message = ""
 
         children_messages = [
             _get_messages(iss, max_depth=max_depth, indent=indent, depth=depth + 1) for iss in issue.issues
         ]
 
         if None in children_messages:
             return None
 
         children = "\n".join(children_messages)
 
     return (
-        f"{pre_message}{margin_str}{issue.message}\n{margin_str}"
-        f"severity level: {issue.severity}\n{margin_str}"
-        f"issue code: {issue.issue_code}\n{children}"
+        pre_message
+        + margin_str
+        + issue.message
+        + "\n"
+        + margin_str
+        + "severity level: "
+        + str(issue.severity)
+        + "\n"
+        + margin_str
+        + "issue code: "
+        + str(issue.issue_code)
+        + "\n"
+        + children
     )
```

### Comparing `ydb-3.2.1/ydb/_errors.py` & `ydb-3.2.2/ydb/_errors.py`

 * *Files identical despite different names*

### Comparing `ydb-3.2.1/ydb/_grpc/common/__init__.py` & `ydb-3.2.2/ydb/_grpc/common/__init__.py`

 * *Files identical despite different names*

### Comparing `ydb-3.2.1/ydb/_grpc/grpcwrapper/common_utils.py` & `ydb-3.2.2/ydb/_grpc/grpcwrapper/common_utils.py`

 * *Files identical despite different names*

### Comparing `ydb-3.2.1/ydb/_grpc/grpcwrapper/ydb_scheme.py` & `ydb-3.2.2/ydb/_grpc/grpcwrapper/ydb_scheme.py`

 * *Files identical despite different names*

### Comparing `ydb-3.2.1/ydb/_grpc/grpcwrapper/ydb_topic.py` & `ydb-3.2.2/ydb/_grpc/grpcwrapper/ydb_topic.py`

 * *Files identical despite different names*

### Comparing `ydb-3.2.1/ydb/_grpc/grpcwrapper/ydb_topic_public_types.py` & `ydb-3.2.2/ydb/_grpc/grpcwrapper/ydb_topic_public_types.py`

 * *Files identical despite different names*

### Comparing `ydb-3.2.1/ydb/_grpc/grpcwrapper/ydb_topic_test.py` & `ydb-3.2.2/ydb/_grpc/grpcwrapper/ydb_topic_test.py`

 * *Files identical despite different names*

### Comparing `ydb-3.2.1/ydb/_grpc/v3/protos/annotations/validation_pb2.py` & `ydb-3.2.2/ydb/_grpc/v3/protos/annotations/validation_pb2.py`

 * *Files identical despite different names*

### Comparing `ydb-3.2.1/ydb/_grpc/v3/protos/ydb_auth_pb2.py` & `ydb-3.2.2/ydb/_grpc/v3/protos/ydb_auth_pb2.py`

 * *Files identical despite different names*

### Comparing `ydb-3.2.1/ydb/_grpc/v3/protos/ydb_cms_pb2.py` & `ydb-3.2.2/ydb/_grpc/v3/protos/ydb_cms_pb2.py`

 * *Files identical despite different names*

### Comparing `ydb-3.2.1/ydb/_grpc/v3/protos/ydb_common_pb2.py` & `ydb-3.2.2/ydb/_grpc/v3/protos/ydb_common_pb2.py`

 * *Files identical despite different names*

### Comparing `ydb-3.2.1/ydb/_grpc/v3/protos/ydb_coordination_pb2.py` & `ydb-3.2.2/ydb/_grpc/v3/protos/ydb_coordination_pb2.py`

 * *Files identical despite different names*

### Comparing `ydb-3.2.1/ydb/_grpc/v3/protos/ydb_discovery_pb2.py` & `ydb-3.2.2/ydb/_grpc/v3/protos/ydb_discovery_pb2.py`

 * *Files identical despite different names*

### Comparing `ydb-3.2.1/ydb/_grpc/v3/protos/ydb_export_pb2.py` & `ydb-3.2.2/ydb/_grpc/v3/protos/ydb_export_pb2.py`

 * *Files identical despite different names*

### Comparing `ydb-3.2.1/ydb/_grpc/v3/protos/ydb_formats_pb2.py` & `ydb-3.2.2/ydb/_grpc/v3/protos/ydb_formats_pb2.py`

 * *Files identical despite different names*

### Comparing `ydb-3.2.1/ydb/_grpc/v3/protos/ydb_import_pb2.py` & `ydb-3.2.2/ydb/_grpc/v3/protos/ydb_import_pb2.py`

 * *Files identical despite different names*

### Comparing `ydb-3.2.1/ydb/_grpc/v3/protos/ydb_issue_message_pb2.py` & `ydb-3.2.2/ydb/_grpc/v3/protos/ydb_issue_message_pb2.py`

 * *Files identical despite different names*

### Comparing `ydb-3.2.1/ydb/_grpc/v3/protos/ydb_monitoring_pb2.py` & `ydb-3.2.2/ydb/_grpc/v3/protos/ydb_monitoring_pb2.py`

 * *Files identical despite different names*

### Comparing `ydb-3.2.1/ydb/_grpc/v3/protos/ydb_operation_pb2.py` & `ydb-3.2.2/ydb/_grpc/v3/protos/ydb_operation_pb2.py`

 * *Files identical despite different names*

### Comparing `ydb-3.2.1/ydb/_grpc/v3/protos/ydb_query_stats_pb2.py` & `ydb-3.2.2/ydb/_grpc/v3/protos/ydb_query_stats_pb2.py`

 * *Files identical despite different names*

### Comparing `ydb-3.2.1/ydb/_grpc/v3/protos/ydb_rate_limiter_pb2.py` & `ydb-3.2.2/ydb/_grpc/v3/protos/ydb_rate_limiter_pb2.py`

 * *Files identical despite different names*

### Comparing `ydb-3.2.1/ydb/_grpc/v3/protos/ydb_scheme_pb2.py` & `ydb-3.2.2/ydb/_grpc/v3/protos/ydb_scheme_pb2.py`

 * *Files identical despite different names*

### Comparing `ydb-3.2.1/ydb/_grpc/v3/protos/ydb_scripting_pb2.py` & `ydb-3.2.2/ydb/_grpc/v3/protos/ydb_scripting_pb2.py`

 * *Files identical despite different names*

### Comparing `ydb-3.2.1/ydb/_grpc/v3/protos/ydb_status_codes_pb2.py` & `ydb-3.2.2/ydb/_grpc/v3/protos/ydb_status_codes_pb2.py`

 * *Files identical despite different names*

### Comparing `ydb-3.2.1/ydb/_grpc/v3/protos/ydb_table_pb2.py` & `ydb-3.2.2/ydb/_grpc/v3/protos/ydb_table_pb2.py`

 * *Files identical despite different names*

### Comparing `ydb-3.2.1/ydb/_grpc/v3/protos/ydb_topic_pb2.py` & `ydb-3.2.2/ydb/_grpc/v3/protos/ydb_topic_pb2.py`

 * *Files identical despite different names*

### Comparing `ydb-3.2.1/ydb/_grpc/v3/protos/ydb_value_pb2.py` & `ydb-3.2.2/ydb/_grpc/v3/protos/ydb_value_pb2.py`

 * *Files identical despite different names*

### Comparing `ydb-3.2.1/ydb/_grpc/v3/ydb_auth_v1_pb2.py` & `ydb-3.2.2/ydb/_grpc/v3/ydb_auth_v1_pb2.py`

 * *Files identical despite different names*

### Comparing `ydb-3.2.1/ydb/_grpc/v3/ydb_auth_v1_pb2_grpc.py` & `ydb-3.2.2/ydb/_grpc/v3/ydb_auth_v1_pb2_grpc.py`

 * *Files identical despite different names*

### Comparing `ydb-3.2.1/ydb/_grpc/v3/ydb_cms_v1_pb2.py` & `ydb-3.2.2/ydb/_grpc/v3/ydb_cms_v1_pb2.py`

 * *Files identical despite different names*

### Comparing `ydb-3.2.1/ydb/_grpc/v3/ydb_cms_v1_pb2_grpc.py` & `ydb-3.2.2/ydb/_grpc/v3/ydb_cms_v1_pb2_grpc.py`

 * *Files identical despite different names*

### Comparing `ydb-3.2.1/ydb/_grpc/v3/ydb_coordination_v1_pb2.py` & `ydb-3.2.2/ydb/_grpc/v3/ydb_coordination_v1_pb2.py`

 * *Files identical despite different names*

### Comparing `ydb-3.2.1/ydb/_grpc/v3/ydb_coordination_v1_pb2_grpc.py` & `ydb-3.2.2/ydb/_grpc/v3/ydb_coordination_v1_pb2_grpc.py`

 * *Files identical despite different names*

### Comparing `ydb-3.2.1/ydb/_grpc/v3/ydb_discovery_v1_pb2.py` & `ydb-3.2.2/ydb/_grpc/v3/ydb_discovery_v1_pb2.py`

 * *Files identical despite different names*

### Comparing `ydb-3.2.1/ydb/_grpc/v3/ydb_discovery_v1_pb2_grpc.py` & `ydb-3.2.2/ydb/_grpc/v3/ydb_discovery_v1_pb2_grpc.py`

 * *Files identical despite different names*

### Comparing `ydb-3.2.1/ydb/_grpc/v3/ydb_export_v1_pb2.py` & `ydb-3.2.2/ydb/_grpc/v3/ydb_export_v1_pb2.py`

 * *Files identical despite different names*

### Comparing `ydb-3.2.1/ydb/_grpc/v3/ydb_export_v1_pb2_grpc.py` & `ydb-3.2.2/ydb/_grpc/v3/ydb_export_v1_pb2_grpc.py`

 * *Files identical despite different names*

### Comparing `ydb-3.2.1/ydb/_grpc/v3/ydb_import_v1_pb2.py` & `ydb-3.2.2/ydb/_grpc/v3/ydb_import_v1_pb2.py`

 * *Files identical despite different names*

### Comparing `ydb-3.2.1/ydb/_grpc/v3/ydb_import_v1_pb2_grpc.py` & `ydb-3.2.2/ydb/_grpc/v3/ydb_import_v1_pb2_grpc.py`

 * *Files identical despite different names*

### Comparing `ydb-3.2.1/ydb/_grpc/v3/ydb_monitoring_v1_pb2.py` & `ydb-3.2.2/ydb/_grpc/v3/ydb_monitoring_v1_pb2.py`

 * *Files identical despite different names*

### Comparing `ydb-3.2.1/ydb/_grpc/v3/ydb_monitoring_v1_pb2_grpc.py` & `ydb-3.2.2/ydb/_grpc/v3/ydb_monitoring_v1_pb2_grpc.py`

 * *Files identical despite different names*

### Comparing `ydb-3.2.1/ydb/_grpc/v3/ydb_operation_v1_pb2.py` & `ydb-3.2.2/ydb/_grpc/v3/ydb_operation_v1_pb2.py`

 * *Files identical despite different names*

### Comparing `ydb-3.2.1/ydb/_grpc/v3/ydb_operation_v1_pb2_grpc.py` & `ydb-3.2.2/ydb/_grpc/v3/ydb_operation_v1_pb2_grpc.py`

 * *Files identical despite different names*

### Comparing `ydb-3.2.1/ydb/_grpc/v3/ydb_rate_limiter_v1_pb2.py` & `ydb-3.2.2/ydb/_grpc/v3/ydb_rate_limiter_v1_pb2.py`

 * *Files identical despite different names*

### Comparing `ydb-3.2.1/ydb/_grpc/v3/ydb_rate_limiter_v1_pb2_grpc.py` & `ydb-3.2.2/ydb/_grpc/v3/ydb_rate_limiter_v1_pb2_grpc.py`

 * *Files identical despite different names*

### Comparing `ydb-3.2.1/ydb/_grpc/v3/ydb_scheme_v1_pb2.py` & `ydb-3.2.2/ydb/_grpc/v3/ydb_scheme_v1_pb2.py`

 * *Files identical despite different names*

### Comparing `ydb-3.2.1/ydb/_grpc/v3/ydb_scheme_v1_pb2_grpc.py` & `ydb-3.2.2/ydb/_grpc/v3/ydb_scheme_v1_pb2_grpc.py`

 * *Files identical despite different names*

### Comparing `ydb-3.2.1/ydb/_grpc/v3/ydb_scripting_v1_pb2.py` & `ydb-3.2.2/ydb/_grpc/v3/ydb_scripting_v1_pb2.py`

 * *Files identical despite different names*

### Comparing `ydb-3.2.1/ydb/_grpc/v3/ydb_scripting_v1_pb2_grpc.py` & `ydb-3.2.2/ydb/_grpc/v3/ydb_scripting_v1_pb2_grpc.py`

 * *Files identical despite different names*

### Comparing `ydb-3.2.1/ydb/_grpc/v3/ydb_table_v1_pb2.py` & `ydb-3.2.2/ydb/_grpc/v3/ydb_table_v1_pb2.py`

 * *Files identical despite different names*

### Comparing `ydb-3.2.1/ydb/_grpc/v3/ydb_table_v1_pb2_grpc.py` & `ydb-3.2.2/ydb/_grpc/v3/ydb_table_v1_pb2_grpc.py`

 * *Files identical despite different names*

### Comparing `ydb-3.2.1/ydb/_grpc/v3/ydb_topic_v1_pb2.py` & `ydb-3.2.2/ydb/_grpc/v3/ydb_topic_v1_pb2.py`

 * *Files identical despite different names*

### Comparing `ydb-3.2.1/ydb/_grpc/v3/ydb_topic_v1_pb2_grpc.py` & `ydb-3.2.2/ydb/_grpc/v3/ydb_topic_v1_pb2_grpc.py`

 * *Files identical despite different names*

### Comparing `ydb-3.2.1/ydb/_grpc/v4/protos/annotations/validation_pb2.py` & `ydb-3.2.2/ydb/_grpc/v4/protos/annotations/validation_pb2.py`

 * *Files identical despite different names*

### Comparing `ydb-3.2.1/ydb/_grpc/v4/protos/ydb_auth_pb2.py` & `ydb-3.2.2/ydb/_grpc/v4/protos/ydb_auth_pb2.py`

 * *Files identical despite different names*

### Comparing `ydb-3.2.1/ydb/_grpc/v4/protos/ydb_cms_pb2.py` & `ydb-3.2.2/ydb/_grpc/v4/protos/ydb_cms_pb2.py`

 * *Files identical despite different names*

### Comparing `ydb-3.2.1/ydb/_grpc/v4/protos/ydb_common_pb2.py` & `ydb-3.2.2/ydb/_grpc/v4/protos/ydb_common_pb2.py`

 * *Files identical despite different names*

### Comparing `ydb-3.2.1/ydb/_grpc/v4/protos/ydb_coordination_pb2.py` & `ydb-3.2.2/ydb/_grpc/v4/protos/ydb_coordination_pb2.py`

 * *Files identical despite different names*

### Comparing `ydb-3.2.1/ydb/_grpc/v4/protos/ydb_discovery_pb2.py` & `ydb-3.2.2/ydb/_grpc/v4/protos/ydb_discovery_pb2.py`

 * *Files identical despite different names*

### Comparing `ydb-3.2.1/ydb/_grpc/v4/protos/ydb_export_pb2.py` & `ydb-3.2.2/ydb/_grpc/v4/protos/ydb_export_pb2.py`

 * *Files identical despite different names*

### Comparing `ydb-3.2.1/ydb/_grpc/v4/protos/ydb_formats_pb2.py` & `ydb-3.2.2/ydb/_grpc/v4/protos/ydb_formats_pb2.py`

 * *Files identical despite different names*

### Comparing `ydb-3.2.1/ydb/_grpc/v4/protos/ydb_import_pb2.py` & `ydb-3.2.2/ydb/_grpc/v4/protos/ydb_import_pb2.py`

 * *Files identical despite different names*

### Comparing `ydb-3.2.1/ydb/_grpc/v4/protos/ydb_issue_message_pb2.py` & `ydb-3.2.2/ydb/_grpc/v4/protos/ydb_issue_message_pb2.py`

 * *Files identical despite different names*

### Comparing `ydb-3.2.1/ydb/_grpc/v4/protos/ydb_monitoring_pb2.py` & `ydb-3.2.2/ydb/_grpc/v4/protos/ydb_monitoring_pb2.py`

 * *Files identical despite different names*

### Comparing `ydb-3.2.1/ydb/_grpc/v4/protos/ydb_operation_pb2.py` & `ydb-3.2.2/ydb/_grpc/v4/protos/ydb_operation_pb2.py`

 * *Files identical despite different names*

### Comparing `ydb-3.2.1/ydb/_grpc/v4/protos/ydb_query_stats_pb2.py` & `ydb-3.2.2/ydb/_grpc/v4/protos/ydb_query_stats_pb2.py`

 * *Files identical despite different names*

### Comparing `ydb-3.2.1/ydb/_grpc/v4/protos/ydb_rate_limiter_pb2.py` & `ydb-3.2.2/ydb/_grpc/v4/protos/ydb_rate_limiter_pb2.py`

 * *Files identical despite different names*

### Comparing `ydb-3.2.1/ydb/_grpc/v4/protos/ydb_scheme_pb2.py` & `ydb-3.2.2/ydb/_grpc/v4/protos/ydb_scheme_pb2.py`

 * *Files identical despite different names*

### Comparing `ydb-3.2.1/ydb/_grpc/v4/protos/ydb_scripting_pb2.py` & `ydb-3.2.2/ydb/_grpc/v4/protos/ydb_scripting_pb2.py`

 * *Files identical despite different names*

### Comparing `ydb-3.2.1/ydb/_grpc/v4/protos/ydb_status_codes_pb2.py` & `ydb-3.2.2/ydb/_grpc/v4/protos/ydb_status_codes_pb2.py`

 * *Files identical despite different names*

### Comparing `ydb-3.2.1/ydb/_grpc/v4/protos/ydb_table_pb2.py` & `ydb-3.2.2/ydb/_grpc/v4/protos/ydb_table_pb2.py`

 * *Files identical despite different names*

### Comparing `ydb-3.2.1/ydb/_grpc/v4/protos/ydb_topic_pb2.py` & `ydb-3.2.2/ydb/_grpc/v4/protos/ydb_topic_pb2.py`

 * *Files identical despite different names*

### Comparing `ydb-3.2.1/ydb/_grpc/v4/protos/ydb_value_pb2.py` & `ydb-3.2.2/ydb/_grpc/v4/protos/ydb_value_pb2.py`

 * *Files identical despite different names*

### Comparing `ydb-3.2.1/ydb/_grpc/v4/ydb_auth_v1_pb2.py` & `ydb-3.2.2/ydb/_grpc/v4/ydb_auth_v1_pb2.py`

 * *Files identical despite different names*

### Comparing `ydb-3.2.1/ydb/_grpc/v4/ydb_auth_v1_pb2_grpc.py` & `ydb-3.2.2/ydb/_grpc/v4/ydb_auth_v1_pb2_grpc.py`

 * *Files identical despite different names*

### Comparing `ydb-3.2.1/ydb/_grpc/v4/ydb_cms_v1_pb2.py` & `ydb-3.2.2/ydb/_grpc/v4/ydb_cms_v1_pb2.py`

 * *Files identical despite different names*

### Comparing `ydb-3.2.1/ydb/_grpc/v4/ydb_cms_v1_pb2_grpc.py` & `ydb-3.2.2/ydb/_grpc/v4/ydb_cms_v1_pb2_grpc.py`

 * *Files identical despite different names*

### Comparing `ydb-3.2.1/ydb/_grpc/v4/ydb_coordination_v1_pb2.py` & `ydb-3.2.2/ydb/_grpc/v4/ydb_coordination_v1_pb2.py`

 * *Files identical despite different names*

### Comparing `ydb-3.2.1/ydb/_grpc/v4/ydb_coordination_v1_pb2_grpc.py` & `ydb-3.2.2/ydb/_grpc/v4/ydb_coordination_v1_pb2_grpc.py`

 * *Files identical despite different names*

### Comparing `ydb-3.2.1/ydb/_grpc/v4/ydb_discovery_v1_pb2.py` & `ydb-3.2.2/ydb/_grpc/v4/ydb_discovery_v1_pb2.py`

 * *Files identical despite different names*

### Comparing `ydb-3.2.1/ydb/_grpc/v4/ydb_discovery_v1_pb2_grpc.py` & `ydb-3.2.2/ydb/_grpc/v4/ydb_discovery_v1_pb2_grpc.py`

 * *Files identical despite different names*

### Comparing `ydb-3.2.1/ydb/_grpc/v4/ydb_export_v1_pb2.py` & `ydb-3.2.2/ydb/_grpc/v4/ydb_export_v1_pb2.py`

 * *Files identical despite different names*

### Comparing `ydb-3.2.1/ydb/_grpc/v4/ydb_export_v1_pb2_grpc.py` & `ydb-3.2.2/ydb/_grpc/v4/ydb_export_v1_pb2_grpc.py`

 * *Files identical despite different names*

### Comparing `ydb-3.2.1/ydb/_grpc/v4/ydb_import_v1_pb2.py` & `ydb-3.2.2/ydb/_grpc/v4/ydb_import_v1_pb2.py`

 * *Files identical despite different names*

### Comparing `ydb-3.2.1/ydb/_grpc/v4/ydb_import_v1_pb2_grpc.py` & `ydb-3.2.2/ydb/_grpc/v4/ydb_import_v1_pb2_grpc.py`

 * *Files identical despite different names*

### Comparing `ydb-3.2.1/ydb/_grpc/v4/ydb_monitoring_v1_pb2.py` & `ydb-3.2.2/ydb/_grpc/v4/ydb_monitoring_v1_pb2.py`

 * *Files identical despite different names*

### Comparing `ydb-3.2.1/ydb/_grpc/v4/ydb_monitoring_v1_pb2_grpc.py` & `ydb-3.2.2/ydb/_grpc/v4/ydb_monitoring_v1_pb2_grpc.py`

 * *Files identical despite different names*

### Comparing `ydb-3.2.1/ydb/_grpc/v4/ydb_operation_v1_pb2.py` & `ydb-3.2.2/ydb/_grpc/v4/ydb_operation_v1_pb2.py`

 * *Files identical despite different names*

### Comparing `ydb-3.2.1/ydb/_grpc/v4/ydb_operation_v1_pb2_grpc.py` & `ydb-3.2.2/ydb/_grpc/v4/ydb_operation_v1_pb2_grpc.py`

 * *Files identical despite different names*

### Comparing `ydb-3.2.1/ydb/_grpc/v4/ydb_rate_limiter_v1_pb2.py` & `ydb-3.2.2/ydb/_grpc/v4/ydb_rate_limiter_v1_pb2.py`

 * *Files identical despite different names*

### Comparing `ydb-3.2.1/ydb/_grpc/v4/ydb_rate_limiter_v1_pb2_grpc.py` & `ydb-3.2.2/ydb/_grpc/v4/ydb_rate_limiter_v1_pb2_grpc.py`

 * *Files identical despite different names*

### Comparing `ydb-3.2.1/ydb/_grpc/v4/ydb_scheme_v1_pb2.py` & `ydb-3.2.2/ydb/_grpc/v4/ydb_scheme_v1_pb2.py`

 * *Files identical despite different names*

### Comparing `ydb-3.2.1/ydb/_grpc/v4/ydb_scheme_v1_pb2_grpc.py` & `ydb-3.2.2/ydb/_grpc/v4/ydb_scheme_v1_pb2_grpc.py`

 * *Files identical despite different names*

### Comparing `ydb-3.2.1/ydb/_grpc/v4/ydb_scripting_v1_pb2.py` & `ydb-3.2.2/ydb/_grpc/v4/ydb_scripting_v1_pb2.py`

 * *Files identical despite different names*

### Comparing `ydb-3.2.1/ydb/_grpc/v4/ydb_scripting_v1_pb2_grpc.py` & `ydb-3.2.2/ydb/_grpc/v4/ydb_scripting_v1_pb2_grpc.py`

 * *Files identical despite different names*

### Comparing `ydb-3.2.1/ydb/_grpc/v4/ydb_table_v1_pb2.py` & `ydb-3.2.2/ydb/_grpc/v4/ydb_table_v1_pb2.py`

 * *Files identical despite different names*

### Comparing `ydb-3.2.1/ydb/_grpc/v4/ydb_table_v1_pb2_grpc.py` & `ydb-3.2.2/ydb/_grpc/v4/ydb_table_v1_pb2_grpc.py`

 * *Files identical despite different names*

### Comparing `ydb-3.2.1/ydb/_grpc/v4/ydb_topic_v1_pb2.py` & `ydb-3.2.2/ydb/_grpc/v4/ydb_topic_v1_pb2.py`

 * *Files identical despite different names*

### Comparing `ydb-3.2.1/ydb/_grpc/v4/ydb_topic_v1_pb2_grpc.py` & `ydb-3.2.2/ydb/_grpc/v4/ydb_topic_v1_pb2_grpc.py`

 * *Files identical despite different names*

### Comparing `ydb-3.2.1/ydb/_session_impl.py` & `ydb-3.2.2/ydb/_session_impl.py`

 * *Files identical despite different names*

### Comparing `ydb-3.2.1/ydb/_sp_impl.py` & `ydb-3.2.2/ydb/_sp_impl.py`

 * *Files identical despite different names*

### Comparing `ydb-3.2.1/ydb/_sqlalchemy/__init__.py` & `ydb-3.2.2/ydb/sqlalchemy/__init__.py`

 * *Files 11% similar despite different names*

```diff
@@ -1,322 +1,293 @@
 """
 Experimental
 Work in progress, breaking changes are possible.
 """
-import ydb
-import ydb._dbapi as dbapi
 
-import sqlalchemy as sa
-from sqlalchemy import dialects
-from sqlalchemy import Table
-from sqlalchemy.exc import CompileError
-from sqlalchemy.sql import functions, literal_column
-from sqlalchemy.sql.compiler import (
-    IdentifierPreparer,
-    GenericTypeCompiler,
-    SQLCompiler,
-    DDLCompiler,
-)
-from sqlalchemy.sql.elements import ClauseList
-from sqlalchemy.engine.default import DefaultDialect
-from sqlalchemy.util.compat import inspect_getfullargspec
+from __future__ import absolute_import, unicode_literals
 
-from ydb._sqlalchemy.types import UInt32, UInt64
 
+try:
+    import ydb
+    from ydb.dbapi.errors import NotSupportedError
+    from ydb.sqlalchemy.types import UInt32, UInt64
+
+    from sqlalchemy.engine.default import DefaultDialect
+    from sqlalchemy.sql.compiler import (
+        IdentifierPreparer,
+        GenericTypeCompiler,
+        SQLCompiler,
+    )
+    from sqlalchemy import Table
+    from sqlalchemy.sql.elements import ClauseList
+    from sqlalchemy.sql import functions
+    import sqlalchemy as sa
+    from sqlalchemy import exc
+    from sqlalchemy.util.compat import inspect_getfullargspec
+    from sqlalchemy.sql import literal_column
+
+    SQLALCHEMY_VERSION = tuple(sa.__version__.split("."))
+    SA_14 = SQLALCHEMY_VERSION >= ("1", "4")
+
+    class YqlIdentifierPreparer(IdentifierPreparer):
+        def __init__(self, dialect):
+            super(YqlIdentifierPreparer, self).__init__(
+                dialect,
+                initial_quote="`",
+                final_quote="`",
+            )
 
-SQLALCHEMY_VERSION = tuple(sa.__version__.split("."))
-SA_14 = SQLALCHEMY_VERSION >= ("1", "4")
-
-
-class YqlIdentifierPreparer(IdentifierPreparer):
-    def __init__(self, dialect):
-        super(YqlIdentifierPreparer, self).__init__(
-            dialect,
-            initial_quote="`",
-            final_quote="`",
-        )
-
-    def _requires_quotes(self, value):
-        # Force all identifiers to get quoted unless already quoted.
-        return not (value.startswith(self.initial_quote) and value.endswith(self.final_quote))
-
-
-class YqlTypeCompiler(GenericTypeCompiler):
-    def visit_VARCHAR(self, type_, **kw):
-        return "STRING"
-
-    def visit_unicode(self, type_, **kw):
-        return "UTF8"
-
-    def visit_NVARCHAR(self, type_, **kw):
-        return "UTF8"
-
-    def visit_TEXT(self, type_, **kw):
-        return "UTF8"
-
-    def visit_FLOAT(self, type_, **kw):
-        return "DOUBLE"
-
-    def visit_BOOLEAN(self, type_, **kw):
-        return "BOOL"
+        def _requires_quotes(self, value):
+            # Force all identifiers to get quoted unless already quoted.
+            return not (value.startswith(self.initial_quote) and value.endswith(self.final_quote))
 
-    def visit_uint32(self, type_, **kw):
-        return "UInt32"
+    class YqlTypeCompiler(GenericTypeCompiler):
+        def visit_VARCHAR(self, type_, **kw):
+            return "STRING"
 
-    def visit_uint64(self, type_, **kw):
-        return "UInt64"
+        def visit_unicode(self, type_, **kw):
+            return "UTF8"
 
-    def visit_uint8(self, type_, **kw):
-        return "UInt8"
+        def visit_NVARCHAR(self, type_, **kw):
+            return "UTF8"
 
-    def visit_INTEGER(self, type_, **kw):
-        return "Int64"
+        def visit_TEXT(self, type_, **kw):
+            return "UTF8"
 
-    def visit_NUMERIC(self, type_, **kw):
-        return "Int64"
+        def visit_FLOAT(self, type_, **kw):
+            return "DOUBLE"
 
+        def visit_BOOLEAN(self, type_, **kw):
+            return "BOOL"
 
-class ParametrizedFunction(functions.Function):
-    __visit_name__ = "parametrized_function"
+        def visit_uint32(self, type_, **kw):
+            return "UInt32"
 
-    def __init__(self, name, params, *args, **kwargs):
-        super(ParametrizedFunction, self).__init__(name, *args, **kwargs)
-        self._func_name = name
-        self._func_params = params
-        self.params_expr = ClauseList(operator=functions.operators.comma_op, group_contents=True, *params).self_group()
+        def visit_uint64(self, type_, **kw):
+            return "UInt64"
 
+        def visit_uint8(self, type_, **kw):
+            return "UInt8"
 
-class YqlCompiler(SQLCompiler):
-    def group_by_clause(self, select, **kw):
-        # Hack to ensure it is possible to define labels in groupby.
-        kw.update(within_columns_clause=True)
-        return super(YqlCompiler, self).group_by_clause(select, **kw)
+    class ParametrizedFunction(functions.Function):
+        __visit_name__ = "parametrized_function"
 
-    def visit_lambda(self, lambda_, **kw):
-        func = lambda_.func
-        spec = inspect_getfullargspec(func)
+        def __init__(self, name, params, *args, **kwargs):
+            super(ParametrizedFunction, self).__init__(name, *args, **kwargs)
+            self._func_name = name
+            self._func_params = params
+            self.params_expr = ClauseList(
+                operator=functions.operators.comma_op, group_contents=True, *params
+            ).self_group()
 
-        if spec.varargs:
-            raise CompileError("Lambdas with *args are not supported")
+    class YqlCompiler(SQLCompiler):
+        def group_by_clause(self, select, **kw):
+            # Hack to ensure it is possible to define labels in groupby.
+            kw.update(within_columns_clause=True)
+            return super(YqlCompiler, self).group_by_clause(select, **kw)
 
-        try:
-            keywords = spec.keywords
-        except AttributeError:
-            keywords = spec.varkw
+        def visit_lambda(self, lambda_, **kw):
+            func = lambda_.func
+            spec = inspect_getfullargspec(func)
 
-        if keywords:
-            raise CompileError("Lambdas with **kwargs are not supported")
+            if spec.varargs:
+                raise exc.CompileError("Lambdas with *args are not supported")
 
-        text = "(" + ", ".join("$" + arg for arg in spec.args) + ")" + " -> "
+            try:
+                keywords = spec.keywords
+            except AttributeError:
+                keywords = spec.varkw
 
-        args = [literal_column("$" + arg) for arg in spec.args]
-        text += "{ RETURN " + self.process(func(*args), **kw) + " ;}"
+            if keywords:
+                raise exc.CompileError("Lambdas with **kwargs are not supported")
 
-        return text
+            text = "(" + ", ".join("$" + arg for arg in spec.args) + ")" + " -> "
 
-    def visit_parametrized_function(self, func, **kwargs):
-        name = func.name
-        name_parts = []
-        for name in name.split("::"):
-            fname = (
-                self.preparer.quote(name)
-                if self.preparer._requires_quotes_illegal_chars(name) or isinstance(name, sa.sql.elements.quoted_name)
-                else name
-            )
+            args = [literal_column("$" + arg) for arg in spec.args]
+            text += "{ RETURN " + self.process(func(*args), **kw) + " ;}"
 
-            name_parts.append(fname)
+            return text
 
-        name = "::".join(name_parts)
-        params = func.params_expr._compiler_dispatch(self, **kwargs)
-        args = self.function_argspec(func, **kwargs)
-        return "%(name)s%(params)s%(args)s" % dict(name=name, params=params, args=args)
-
-    def visit_function(self, func, add_to_result_map=None, **kwargs):
-        # Copypaste of `sa.sql.compiler.SQLCompiler.visit_function` with
-        # `::` as namespace separator instead of `.`
-        if add_to_result_map is not None:
-            add_to_result_map(func.name, func.name, (), func.type)
-
-        disp = getattr(self, "visit_%s_func" % func.name.lower(), None)
-        if disp:
-            return disp(func, **kwargs)
-        else:
-            name = sa.sql.compiler.FUNCTIONS.get(func.__class__, None)
-            if name:
-                if func._has_args:
-                    name += "%(expr)s"
-            else:
-                name = func.name
-                name = (
+        def visit_parametrized_function(self, func, **kwargs):
+            name = func.name
+            name_parts = []
+            for name in name.split("::"):
+                fname = (
                     self.preparer.quote(name)
                     if self.preparer._requires_quotes_illegal_chars(name)
                     or isinstance(name, sa.sql.elements.quoted_name)
                     else name
                 )
-                name = name + "%(expr)s"
-            return "::".join(
-                [
-                    (
-                        self.preparer.quote(tok)
-                        if self.preparer._requires_quotes_illegal_chars(tok)
+
+                name_parts.append(fname)
+
+            name = "::".join(name_parts)
+            params = func.params_expr._compiler_dispatch(self, **kwargs)
+            args = self.function_argspec(func, **kwargs)
+            return "%(name)s%(params)s%(args)s" % dict(name=name, params=params, args=args)
+
+        def visit_function(self, func, add_to_result_map=None, **kwargs):
+            # Copypaste of `sa.sql.compiler.SQLCompiler.visit_function` with
+            # `::` as namespace separator instead of `.`
+            if add_to_result_map is not None:
+                add_to_result_map(func.name, func.name, (), func.type)
+
+            disp = getattr(self, "visit_%s_func" % func.name.lower(), None)
+            if disp:
+                return disp(func, **kwargs)
+            else:
+                name = sa.sql.compiler.FUNCTIONS.get(func.__class__, None)
+                if name:
+                    if func._has_args:
+                        name += "%(expr)s"
+                else:
+                    name = func.name
+                    name = (
+                        self.preparer.quote(name)
+                        if self.preparer._requires_quotes_illegal_chars(name)
                         or isinstance(name, sa.sql.elements.quoted_name)
-                        else tok
+                        else name
                     )
-                    for tok in func.packagenames
-                ]
-                + [name]
-            ) % {"expr": self.function_argspec(func, **kwargs)}
-
-
-class YqlDdlCompiler(DDLCompiler):
-    pass
-
-
-def upsert(table):
-    return sa.sql.Insert(table)
-
-
-COLUMN_TYPES = {
-    ydb.PrimitiveType.Int8: sa.INTEGER,
-    ydb.PrimitiveType.Int16: sa.INTEGER,
-    ydb.PrimitiveType.Int32: sa.INTEGER,
-    ydb.PrimitiveType.Int64: sa.INTEGER,
-    ydb.PrimitiveType.Uint8: sa.INTEGER,
-    ydb.PrimitiveType.Uint16: sa.INTEGER,
-    ydb.PrimitiveType.Uint32: UInt32,
-    ydb.PrimitiveType.Uint64: UInt64,
-    ydb.PrimitiveType.Float: sa.FLOAT,
-    ydb.PrimitiveType.Double: sa.FLOAT,
-    ydb.PrimitiveType.String: sa.TEXT,
-    ydb.PrimitiveType.Utf8: sa.TEXT,
-    ydb.PrimitiveType.Json: sa.JSON,
-    ydb.PrimitiveType.JsonDocument: sa.JSON,
-    ydb.DecimalType: sa.DECIMAL,
-    ydb.PrimitiveType.Yson: sa.TEXT,
-    ydb.PrimitiveType.Date: sa.DATE,
-    ydb.PrimitiveType.Datetime: sa.DATETIME,
-    ydb.PrimitiveType.Timestamp: sa.DATETIME,
-    ydb.PrimitiveType.Interval: sa.INTEGER,
-    ydb.PrimitiveType.Bool: sa.BOOLEAN,
-    ydb.PrimitiveType.DyNumber: sa.TEXT,
-}
-
-
-def _get_column_info(t):
-    nullable = False
-    if isinstance(t, ydb.OptionalType):
-        nullable = True
-        t = t.item
-
-    if isinstance(t, ydb.DecimalType):
-        return sa.DECIMAL(precision=t.precision, scale=t.scale), nullable
-
-    return COLUMN_TYPES[t], nullable
-
-
-class YqlDialect(DefaultDialect):
-    name = "yql"
-    supports_alter = False
-    max_identifier_length = 63
-    supports_sane_rowcount = False
-    supports_statement_cache = False
-
-    supports_native_enum = False
-    supports_native_boolean = True
-    supports_smallserial = False
-
-    supports_sequences = False
-    sequences_optional = True
-    preexecute_autoincrement_sequences = True
-    postfetch_lastrowid = False
-
-    supports_default_values = False
-    supports_empty_insert = False
-    supports_multivalues_insert = True
-    default_paramstyle = "qmark"
-
-    isolation_level = None
-
-    preparer = YqlIdentifierPreparer
-    statement_compiler = YqlCompiler
-    ddl_compiler = YqlDdlCompiler
-    type_compiler = YqlTypeCompiler
-
-    driver = ydb.Driver
-
-    @staticmethod
-    def dbapi():
-        return dbapi
-
-    def _check_unicode_returns(self, *args, **kwargs):
-        # Normally, this would do 2 SQL queries, which isn't quite necessary.
-        return "conditional"
-
-    def get_columns(self, connection, table_name, schema=None, **kw):
-        if schema is not None:
-            raise dbapi.errors.NotSupportedError("unsupported on non empty schema")
-
-        qt = table_name.name if isinstance(table_name, Table) else table_name
-
-        if SA_14:
-            raw_conn = connection.connection
-        else:
-            raw_conn = connection.raw_connection()
-
-        columns = raw_conn.describe(qt)
-        as_compatible = []
-        for column in columns:
-            col_type, nullable = _get_column_info(column.type)
-            as_compatible.append(
-                {
-                    "name": column.name,
-                    "type": col_type,
-                    "nullable": nullable,
-                }
-            )
+                    name = name + "%(expr)s"
+                return "::".join(
+                    [
+                        (
+                            self.preparer.quote(tok)
+                            if self.preparer._requires_quotes_illegal_chars(tok)
+                            or isinstance(name, sa.sql.elements.quoted_name)
+                            else tok
+                        )
+                        for tok in func.packagenames
+                    ]
+                    + [name]
+                ) % {"expr": self.function_argspec(func, **kwargs)}
+
+    COLUMN_TYPES = {
+        ydb.PrimitiveType.Int8: sa.INTEGER,
+        ydb.PrimitiveType.Int16: sa.INTEGER,
+        ydb.PrimitiveType.Int32: sa.INTEGER,
+        ydb.PrimitiveType.Int64: sa.INTEGER,
+        ydb.PrimitiveType.Uint8: sa.INTEGER,
+        ydb.PrimitiveType.Uint16: sa.INTEGER,
+        ydb.PrimitiveType.Uint32: UInt32,
+        ydb.PrimitiveType.Uint64: UInt64,
+        ydb.PrimitiveType.Float: sa.FLOAT,
+        ydb.PrimitiveType.Double: sa.FLOAT,
+        ydb.PrimitiveType.String: sa.TEXT,
+        ydb.PrimitiveType.Utf8: sa.TEXT,
+        ydb.PrimitiveType.Json: sa.JSON,
+        ydb.PrimitiveType.JsonDocument: sa.JSON,
+        ydb.DecimalType: sa.DECIMAL,
+        ydb.PrimitiveType.Yson: sa.TEXT,
+        ydb.PrimitiveType.Date: sa.DATE,
+        ydb.PrimitiveType.Datetime: sa.DATETIME,
+        ydb.PrimitiveType.Timestamp: sa.DATETIME,
+        ydb.PrimitiveType.Interval: sa.INTEGER,
+        ydb.PrimitiveType.Bool: sa.BOOLEAN,
+        ydb.PrimitiveType.DyNumber: sa.TEXT,
+    }
+
+    def _get_column_info(t):
+        nullable = False
+        if isinstance(t, ydb.OptionalType):
+            nullable = True
+            t = t.item
+
+        if isinstance(t, ydb.DecimalType):
+            return sa.DECIMAL(precision=t.precision, scale=t.scale), nullable
+
+        return COLUMN_TYPES[t], nullable
+
+    class YqlDialect(DefaultDialect):
+        name = "yql"
+        supports_alter = False
+        max_identifier_length = 63
+        supports_sane_rowcount = False
+        supports_statement_cache = False
+
+        supports_native_enum = False
+        supports_native_boolean = True
+        supports_smallserial = False
+
+        supports_sequences = False
+        sequences_optional = True
+        preexecute_autoincrement_sequences = True
+        postfetch_lastrowid = False
+
+        supports_default_values = False
+        supports_empty_insert = False
+        supports_multivalues_insert = True
+        default_paramstyle = "qmark"
+
+        isolation_level = None
+
+        preparer = YqlIdentifierPreparer
+        statement_compiler = YqlCompiler
+        type_compiler = YqlTypeCompiler
+
+        @staticmethod
+        def dbapi():
+            import ydb.dbapi
+
+            return ydb.dbapi
+
+        def _check_unicode_returns(self, *args, **kwargs):
+            # Normally, this would do 2 SQL queries, which isn't quite necessary.
+            return "conditional"
+
+        def get_columns(self, connection, table_name, schema=None, **kw):
+            if schema is not None:
+                raise NotSupportedError
 
-        return as_compatible
+            if isinstance(table_name, Table):
+                qt = table_name.name
+            else:
+                qt = table_name
 
-    def has_table(self, connection, table_name, schema=None, **kwargs):
-        if schema is not None:
-            raise dbapi.errors.NotSupportedError("unsupported on non empty schema")
-
-        quote = self.identifier_preparer.quote_identifier
-        qtable = quote(table_name)
-
-        # TODO: use `get_columns` instead.
-        statement = "SELECT * FROM " + qtable
-        try:
-            connection.execute(statement)
-            return True
-        except Exception:
-            return False
-
-    def get_pk_constraint(self, connection, table_name, schema=None, **kwargs):
-        # TODO: implement me
-        return []
-
-    def get_foreign_keys(self, connection, table_name, schema=None, **kwargs):
-        # foreign keys unsupported
-        return []
-
-    def get_indexes(self, connection, table_name, schema=None, **kwargs):
-        # TODO: implement me
-        return []
-
-    def do_commit(self, dbapi_connection) -> None:
-        # TODO: needs to implement?
-        pass
-
-    def do_execute(self, cursor, statement, parameters, context=None) -> None:
-        c = None
-        if context is not None and context.isddl:
-            c = {"isddl": True}
-        cursor.execute(statement, parameters, c)
+            if SA_14:
+                raw_conn = connection.connection
+            else:
+                raw_conn = connection.raw_connection()
+            columns = raw_conn.describe(qt)
+            as_compatible = []
+            for column in columns:
+                col_type, nullable = _get_column_info(column.type)
+                as_compatible.append(
+                    {
+                        "name": column.name,
+                        "type": col_type,
+                        "nullable": nullable,
+                    }
+                )
+
+            return as_compatible
+
+        def has_table(self, connection, table_name, schema=None):
+            if schema is not None:
+                raise NotSupportedError
+
+            quote = self.identifier_preparer.quote_identifier
+            qtable = quote(table_name)
+
+            # TODO: use `get_columns` instead.
+            statement = "SELECT * FROM " + qtable
+            try:
+                connection.execute(statement)
+                return True
+            except Exception:
+                return False
+
+except ImportError:
+
+    class YqlDialect(object):
+        def __init__(self):
+            raise RuntimeError("could not import sqlalchemy")
 
 
 def register_dialect(
     name="yql",
     module=__name__,
     cls="YqlDialect",
 ):
-    return dialects.registry.register(name, module, cls)
+    import sqlalchemy as sa
+
+    return sa.dialects.registry.register(name, module, cls)
```

### Comparing `ydb-3.2.1/ydb/_sqlalchemy/types.py` & `ydb-3.2.2/ydb/sqlalchemy/types.py`

 * *Files 20% similar despite different names*

```diff
@@ -1,11 +1,15 @@
-from sqlalchemy.types import Integer
-from sqlalchemy.sql import type_api
-from sqlalchemy.sql.elements import ColumnElement
-from sqlalchemy import util, exc
+try:
+    from sqlalchemy.types import Integer
+    from sqlalchemy.sql import type_api
+    from sqlalchemy.sql.elements import ColumnElement
+    from sqlalchemy import util, exc
+except ImportError:
+    Integer = object
+    ColumnElement = object
 
 
 class UInt32(Integer):
     __visit_name__ = "uint32"
 
 
 class UInt64(Integer):
```

### Comparing `ydb-3.2.1/ydb/_topic_common/common.py` & `ydb-3.2.2/ydb/_topic_common/common.py`

 * *Files identical despite different names*

### Comparing `ydb-3.2.1/ydb/_topic_common/common_test.py` & `ydb-3.2.2/ydb/_topic_common/common_test.py`

 * *Files identical despite different names*

### Comparing `ydb-3.2.1/ydb/_topic_common/test_helpers.py` & `ydb-3.2.2/ydb/_topic_common/test_helpers.py`

 * *Files identical despite different names*

### Comparing `ydb-3.2.1/ydb/_topic_reader/datatypes.py` & `ydb-3.2.2/ydb/_topic_reader/datatypes.py`

 * *Files identical despite different names*

### Comparing `ydb-3.2.1/ydb/_topic_reader/datatypes_test.py` & `ydb-3.2.2/ydb/_topic_reader/datatypes_test.py`

 * *Files identical despite different names*

### Comparing `ydb-3.2.1/ydb/_topic_reader/topic_reader.py` & `ydb-3.2.2/ydb/_topic_reader/topic_reader.py`

 * *Files identical despite different names*

### Comparing `ydb-3.2.1/ydb/_topic_reader/topic_reader_asyncio.py` & `ydb-3.2.2/ydb/_topic_reader/topic_reader_asyncio.py`

 * *Files identical despite different names*

### Comparing `ydb-3.2.1/ydb/_topic_reader/topic_reader_asyncio_test.py` & `ydb-3.2.2/ydb/_topic_reader/topic_reader_asyncio_test.py`

 * *Files identical despite different names*

### Comparing `ydb-3.2.1/ydb/_topic_reader/topic_reader_sync.py` & `ydb-3.2.2/ydb/_topic_reader/topic_reader_sync.py`

 * *Files identical despite different names*

### Comparing `ydb-3.2.1/ydb/_topic_writer/topic_writer.py` & `ydb-3.2.2/ydb/_topic_writer/topic_writer.py`

 * *Files identical despite different names*

### Comparing `ydb-3.2.1/ydb/_topic_writer/topic_writer_asyncio.py` & `ydb-3.2.2/ydb/_topic_writer/topic_writer_asyncio.py`

 * *Files identical despite different names*

### Comparing `ydb-3.2.1/ydb/_topic_writer/topic_writer_asyncio_test.py` & `ydb-3.2.2/ydb/_topic_writer/topic_writer_asyncio_test.py`

 * *Files identical despite different names*

### Comparing `ydb-3.2.1/ydb/_topic_writer/topic_writer_sync.py` & `ydb-3.2.2/ydb/_topic_writer/topic_writer_sync.py`

 * *Files identical despite different names*

### Comparing `ydb-3.2.1/ydb/_topic_writer/topic_writer_test.py` & `ydb-3.2.2/ydb/_topic_writer/topic_writer_test.py`

 * *Files identical despite different names*

### Comparing `ydb-3.2.1/ydb/_tx_ctx_impl.py` & `ydb-3.2.2/ydb/_tx_ctx_impl.py`

 * *Files 3% similar despite different names*

```diff
@@ -105,38 +105,44 @@
     return tx_settings
 
 
 @wrap_tx_factory_handler
 def execute_request_factory(session_state, tx_state, query, parameters, commit_tx, settings):
     data_query, query_id = session_state.lookup(query)
     parameters_types = {}
-    keep_in_cache = False
+
     if query_id is not None:
         query_pb = _apis.ydb_table.Query(id=query_id)
         parameters_types = data_query.parameters_types
     else:
         if data_query is not None:
             # client cache disabled for send query text every time
             yql_text = data_query.yql_text
             parameters_types = data_query.parameters_types
         elif isinstance(query, types.DataQuery):
-            if settings is not None and hasattr(settings, "keep_in_cache"):
-                keep_in_cache = settings.keep_in_cache
-            else:
-                # that is an instance of a data query and we don't know query id for id.
-                # so let's prepare it to keep in cache
-                keep_in_cache = True
             yql_text = query.yql_text
             parameters_types = query.parameters_types
         else:
             yql_text = query
         query_pb = _apis.ydb_table.Query(yql_text=yql_text)
     request = _apis.ydb_table.ExecuteDataQueryRequest(parameters=convert.parameters_to_pb(parameters_types, parameters))
+
+    if query_id is not None:
+        # SDK not send query text and nothing save to cache
+        keep_in_cache = False
+    elif settings is not None and hasattr(settings, "keep_in_cache"):
+        keep_in_cache = settings.keep_in_cache
+    elif parameters:
+        keep_in_cache = True
+    else:
+        keep_in_cache = False
+
     if keep_in_cache:
         request.query_cache_policy.keep_in_cache = True
+
     request.query.MergeFrom(query_pb)
     tx_control = _apis.ydb_table.TransactionControl()
     tx_control.commit_tx = commit_tx
     if tx_state.tx_id is not None:
         tx_control.tx_id = tx_state.tx_id
     else:
         tx_control.begin_tx.MergeFrom(_construct_tx_settings(tx_state))
```

### Comparing `ydb-3.2.1/ydb/_utilities.py` & `ydb-3.2.2/ydb/_utilities.py`

 * *Files identical despite different names*

### Comparing `ydb-3.2.1/ydb/aio/connection.py` & `ydb-3.2.2/ydb/aio/connection.py`

 * *Files identical despite different names*

### Comparing `ydb-3.2.1/ydb/aio/credentials.py` & `ydb-3.2.2/ydb/aio/credentials.py`

 * *Files identical despite different names*

### Comparing `ydb-3.2.1/ydb/aio/driver.py` & `ydb-3.2.2/ydb/aio/driver.py`

 * *Files identical despite different names*

### Comparing `ydb-3.2.1/ydb/aio/iam.py` & `ydb-3.2.2/ydb/aio/iam.py`

 * *Files identical despite different names*

### Comparing `ydb-3.2.1/ydb/aio/pool.py` & `ydb-3.2.2/ydb/aio/pool.py`

 * *Files identical despite different names*

### Comparing `ydb-3.2.1/ydb/aio/resolver.py` & `ydb-3.2.2/ydb/aio/resolver.py`

 * *Files identical despite different names*

### Comparing `ydb-3.2.1/ydb/aio/scheme.py` & `ydb-3.2.2/ydb/aio/scheme.py`

 * *Files identical despite different names*

### Comparing `ydb-3.2.1/ydb/aio/table.py` & `ydb-3.2.2/ydb/aio/table.py`

 * *Files identical despite different names*

### Comparing `ydb-3.2.1/ydb/connection.py` & `ydb-3.2.2/ydb/connection.py`

 * *Files identical despite different names*

### Comparing `ydb-3.2.1/ydb/convert.py` & `ydb-3.2.2/ydb/convert.py`

 * *Files identical despite different names*

### Comparing `ydb-3.2.1/ydb/credentials.py` & `ydb-3.2.2/ydb/credentials.py`

 * *Files identical despite different names*

### Comparing `ydb-3.2.1/ydb/dbapi/__init__.py` & `ydb-3.2.2/ydb/dbapi/__init__.py`

 * *Files identical despite different names*

### Comparing `ydb-3.2.1/ydb/default_pem.py` & `ydb-3.2.2/ydb/default_pem.py`

 * *Files identical despite different names*

### Comparing `ydb-3.2.1/ydb/driver.py` & `ydb-3.2.2/ydb/driver.py`

 * *Files identical despite different names*

### Comparing `ydb-3.2.1/ydb/export.py` & `ydb-3.2.2/ydb/export.py`

 * *Files identical despite different names*

### Comparing `ydb-3.2.1/ydb/global_settings.py` & `ydb-3.2.2/ydb/global_settings.py`

 * *Files identical despite different names*

### Comparing `ydb-3.2.1/ydb/iam/auth.py` & `ydb-3.2.2/ydb/iam/auth.py`

 * *Files identical despite different names*

### Comparing `ydb-3.2.1/ydb/import_client.py` & `ydb-3.2.2/ydb/import_client.py`

 * *Files identical despite different names*

### Comparing `ydb-3.2.1/ydb/interceptor.py` & `ydb-3.2.2/ydb/interceptor.py`

 * *Files identical despite different names*

### Comparing `ydb-3.2.1/ydb/issues.py` & `ydb-3.2.2/ydb/issues.py`

 * *Files identical despite different names*

### Comparing `ydb-3.2.1/ydb/operation.py` & `ydb-3.2.2/ydb/operation.py`

 * *Files identical despite different names*

### Comparing `ydb-3.2.1/ydb/pool.py` & `ydb-3.2.2/ydb/pool.py`

 * *Files identical despite different names*

### Comparing `ydb-3.2.1/ydb/resolver.py` & `ydb-3.2.2/ydb/resolver.py`

 * *Files identical despite different names*

### Comparing `ydb-3.2.1/ydb/scheme.py` & `ydb-3.2.2/ydb/scheme.py`

 * *Files identical despite different names*

### Comparing `ydb-3.2.1/ydb/scheme_test.py` & `ydb-3.2.2/ydb/scheme_test.py`

 * *Files identical despite different names*

### Comparing `ydb-3.2.1/ydb/scripting.py` & `ydb-3.2.2/ydb/scripting.py`

 * *Files identical despite different names*

### Comparing `ydb-3.2.1/ydb/settings.py` & `ydb-3.2.2/ydb/settings.py`

 * *Files identical despite different names*

### Comparing `ydb-3.2.1/ydb/table.py` & `ydb-3.2.2/ydb/table.py`

 * *Files identical despite different names*

### Comparing `ydb-3.2.1/ydb/table_test.py` & `ydb-3.2.2/ydb/table_test.py`

 * *Files identical despite different names*

### Comparing `ydb-3.2.1/ydb/topic.py` & `ydb-3.2.2/ydb/topic.py`

 * *Files identical despite different names*

### Comparing `ydb-3.2.1/ydb/tracing.py` & `ydb-3.2.2/ydb/tracing.py`

 * *Files identical despite different names*

### Comparing `ydb-3.2.1/ydb/types.py` & `ydb-3.2.2/ydb/types.py`

 * *Files identical despite different names*

### Comparing `ydb-3.2.1/ydb.egg-info/PKG-INFO` & `ydb-3.2.2/ydb.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: ydb
-Version: 3.2.1
+Version: 3.2.2
 Summary: YDB Python SDK
 Home-page: http://github.com/ydb-platform/ydb-python-sdk
 Author: Yandex LLC
 Author-email: ydb@yandex-team.ru
 License: Apache 2.0
 Classifier: Programming Language :: Python
 Classifier: Programming Language :: Python :: 2
```

### Comparing `ydb-3.2.1/ydb.egg-info/SOURCES.txt` & `ydb-3.2.2/ydb.egg-info/SOURCES.txt`

 * *Files 2% similar despite different names*

```diff
@@ -33,19 +33,14 @@
 ./ydb/settings.py
 ./ydb/table.py
 ./ydb/table_test.py
 ./ydb/topic.py
 ./ydb/tracing.py
 ./ydb/types.py
 ./ydb/ydb_version.py
-./ydb/_dbapi/__init__.py
-./ydb/_dbapi/connection.py
-./ydb/_dbapi/cursor.py
-./ydb/_dbapi/errors.py
-./ydb/_dbapi/test_cursor.py
 ./ydb/_grpc/__init__.py
 ./ydb/_grpc/common/__init__.py
 ./ydb/_grpc/grpcwrapper/__init__.py
 ./ydb/_grpc/grpcwrapper/common_utils.py
 ./ydb/_grpc/grpcwrapper/ydb_scheme.py
 ./ydb/_grpc/grpcwrapper/ydb_topic.py
 ./ydb/_grpc/grpcwrapper/ydb_topic_public_types.py
@@ -184,16 +179,14 @@
 ./ydb/_grpc/v4/protos/ydb_topic_pb2.py
 ./ydb/_grpc/v4/protos/ydb_topic_pb2_grpc.py
 ./ydb/_grpc/v4/protos/ydb_value_pb2.py
 ./ydb/_grpc/v4/protos/ydb_value_pb2_grpc.py
 ./ydb/_grpc/v4/protos/annotations/__init__.py
 ./ydb/_grpc/v4/protos/annotations/validation_pb2.py
 ./ydb/_grpc/v4/protos/annotations/validation_pb2_grpc.py
-./ydb/_sqlalchemy/__init__.py
-./ydb/_sqlalchemy/types.py
 ./ydb/_topic_common/__init__.py
 ./ydb/_topic_common/common.py
 ./ydb/_topic_common/common_test.py
 ./ydb/_topic_common/test_helpers.py
 ./ydb/_topic_reader/__init__.py
 ./ydb/_topic_reader/datatypes.py
 ./ydb/_topic_reader/datatypes_test.py
```

