# Comparing `tmp/calixa-proto-py-2.0.8.tar.gz` & `tmp/calixa-proto-py-2.0.9.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "calixa-proto-py-2.0.8.tar", max compression
+gzip compressed data, was "calixa-proto-py-2.0.9.tar", max compression
```

## Comparing `calixa-proto-py-2.0.8.tar` & `calixa-proto-py-2.0.9.tar`

### file list

```diff
@@ -1,176 +1,188 @@
--rw-r--r--   0        0        0       22 2022-05-13 13:48:35.269385 calixa-proto-py-2.0.8/calixa_proto_py/__init__.py
--rw-r--r--   0        0        0     5936 2022-05-13 13:50:52.719848 calixa-proto-py-2.0.8/calixa_proto_py/account.proto
--rw-r--r--   0        0        0    14327 2022-05-13 13:50:55.311895 calixa-proto-py-2.0.8/calixa_proto_py/account_pb2.py
--rw-r--r--   0        0        0    19310 2022-05-13 13:50:55.311895 calixa-proto-py-2.0.8/calixa_proto_py/account_pb2.pyi
--rw-r--r--   0        0        0      159 2022-05-13 13:50:55.311895 calixa-proto-py-2.0.8/calixa_proto_py/account_pb2_grpc.py
--rw-r--r--   0        0        0     1297 2022-05-13 13:50:52.727849 calixa-proto-py-2.0.8/calixa_proto_py/account_service.proto
--rw-r--r--   0        0        0     5328 2022-05-13 13:50:54.439879 calixa-proto-py-2.0.8/calixa_proto_py/account_service_pb2.py
--rw-r--r--   0        0        0     3886 2022-05-13 13:50:54.439879 calixa-proto-py-2.0.8/calixa_proto_py/account_service_pb2.pyi
--rw-r--r--   0        0        0     6121 2022-05-13 13:50:54.439879 calixa-proto-py-2.0.8/calixa_proto_py/account_service_pb2_grpc.py
--rw-r--r--   0        0        0    10835 2022-05-13 13:50:52.731849 calixa-proto-py-2.0.8/calixa_proto_py/action.proto
--rw-r--r--   0        0        0    22341 2022-05-13 13:50:54.815886 calixa-proto-py-2.0.8/calixa_proto_py/action_pb2.py
--rw-r--r--   0        0        0    31167 2022-05-13 13:50:54.815886 calixa-proto-py-2.0.8/calixa_proto_py/action_pb2.pyi
--rw-r--r--   0        0        0      159 2022-05-13 13:50:54.815886 calixa-proto-py-2.0.8/calixa_proto_py/action_pb2_grpc.py
--rw-r--r--   0        0        0     2140 2022-05-13 13:50:52.735849 calixa-proto-py-2.0.8/calixa_proto_py/action_service.proto
--rw-r--r--   0        0        0     7396 2022-05-13 13:50:55.955906 calixa-proto-py-2.0.8/calixa_proto_py/action_service_pb2.py
--rw-r--r--   0        0        0     6951 2022-05-13 13:50:55.955906 calixa-proto-py-2.0.8/calixa_proto_py/action_service_pb2.pyi
--rw-r--r--   0        0        0     7800 2022-05-13 13:50:55.955906 calixa-proto-py-2.0.8/calixa_proto_py/action_service_pb2_grpc.py
--rw-r--r--   0        0        0     1198 2022-05-13 13:50:52.739849 calixa-proto-py-2.0.8/calixa_proto_py/authentication.proto
--rw-r--r--   0        0        0     5260 2022-05-13 13:50:56.219911 calixa-proto-py-2.0.8/calixa_proto_py/authentication_pb2.py
--rw-r--r--   0        0        0     5616 2022-05-13 13:50:56.219911 calixa-proto-py-2.0.8/calixa_proto_py/authentication_pb2.pyi
--rw-r--r--   0        0        0     4368 2022-05-13 13:50:56.219911 calixa-proto-py-2.0.8/calixa_proto_py/authentication_pb2_grpc.py
--rw-r--r--   0        0        0     2696 2022-05-13 13:50:52.743849 calixa-proto-py-2.0.8/calixa_proto_py/automation.proto
--rw-r--r--   0        0        0      786 2022-05-13 13:50:52.747849 calixa-proto-py-2.0.8/calixa_proto_py/automation_log.proto
--rw-r--r--   0        0        0     2726 2022-05-13 13:50:53.955871 calixa-proto-py-2.0.8/calixa_proto_py/automation_log_pb2.py
--rw-r--r--   0        0        0     3902 2022-05-13 13:50:53.955871 calixa-proto-py-2.0.8/calixa_proto_py/automation_log_pb2.pyi
--rw-r--r--   0        0        0      159 2022-05-13 13:50:53.955871 calixa-proto-py-2.0.8/calixa_proto_py/automation_log_pb2_grpc.py
--rw-r--r--   0        0        0     9806 2022-05-13 13:50:55.611900 calixa-proto-py-2.0.8/calixa_proto_py/automation_pb2.py
--rw-r--r--   0        0        0    12962 2022-05-13 13:50:55.611900 calixa-proto-py-2.0.8/calixa_proto_py/automation_pb2.pyi
--rw-r--r--   0        0        0      159 2022-05-13 13:50:55.611900 calixa-proto-py-2.0.8/calixa_proto_py/automation_pb2_grpc.py
--rw-r--r--   0        0        0     1176 2022-05-13 13:50:52.751849 calixa-proto-py-2.0.8/calixa_proto_py/automation_service.proto
--rw-r--r--   0        0        0     4832 2022-05-13 13:50:55.111891 calixa-proto-py-2.0.8/calixa_proto_py/automation_service_pb2.py
--rw-r--r--   0        0        0     2809 2022-05-13 13:50:55.111891 calixa-proto-py-2.0.8/calixa_proto_py/automation_service_pb2.pyi
--rw-r--r--   0        0        0     7520 2022-05-13 13:50:55.111891 calixa-proto-py-2.0.8/calixa_proto_py/automation_service_pb2_grpc.py
--rw-r--r--   0        0        0     6303 2022-05-13 13:50:52.755849 calixa-proto-py-2.0.8/calixa_proto_py/billing.proto
--rw-r--r--   0        0        0    21739 2022-05-13 13:50:54.707884 calixa-proto-py-2.0.8/calixa_proto_py/billing_pb2.py
--rw-r--r--   0        0        0    29816 2022-05-13 13:50:54.707884 calixa-proto-py-2.0.8/calixa_proto_py/billing_pb2.pyi
--rw-r--r--   0        0        0      159 2022-05-13 13:50:54.707884 calixa-proto-py-2.0.8/calixa_proto_py/billing_pb2_grpc.py
--rw-r--r--   0        0        0     2498 2022-05-13 13:50:52.759849 calixa-proto-py-2.0.8/calixa_proto_py/collaboration.proto
--rw-r--r--   0        0        0     1856 2022-05-13 13:50:52.763849 calixa-proto-py-2.0.8/calixa_proto_py/collaboration_entity.proto
--rw-r--r--   0        0        0     5325 2022-05-13 13:50:53.763867 calixa-proto-py-2.0.8/calixa_proto_py/collaboration_entity_pb2.py
--rw-r--r--   0        0        0     7293 2022-05-13 13:50:53.763867 calixa-proto-py-2.0.8/calixa_proto_py/collaboration_entity_pb2.pyi
--rw-r--r--   0        0        0      159 2022-05-13 13:50:53.763867 calixa-proto-py-2.0.8/calixa_proto_py/collaboration_entity_pb2_grpc.py
--rw-r--r--   0        0        0    10111 2022-05-13 13:50:55.403897 calixa-proto-py-2.0.8/calixa_proto_py/collaboration_pb2.py
--rw-r--r--   0        0        0     8110 2022-05-13 13:50:55.403897 calixa-proto-py-2.0.8/calixa_proto_py/collaboration_pb2.pyi
--rw-r--r--   0        0        0    16114 2022-05-13 13:50:55.403897 calixa-proto-py-2.0.8/calixa_proto_py/collaboration_pb2_grpc.py
--rw-r--r--   0        0        0     7113 2022-05-13 13:50:52.767849 calixa-proto-py-2.0.8/calixa_proto_py/common.proto
--rw-r--r--   0        0        0    12308 2022-05-13 13:50:54.303877 calixa-proto-py-2.0.8/calixa_proto_py/common_pb2.py
--rw-r--r--   0        0        0    16924 2022-05-13 13:50:54.303877 calixa-proto-py-2.0.8/calixa_proto_py/common_pb2.pyi
--rw-r--r--   0        0        0     2525 2022-05-13 13:50:54.303877 calixa-proto-py-2.0.8/calixa_proto_py/common_pb2_grpc.py
--rw-r--r--   0        0        0     6302 2022-05-13 13:50:52.771849 calixa-proto-py-2.0.8/calixa_proto_py/condition.proto
--rw-r--r--   0        0        0    16550 2022-05-13 13:50:54.499880 calixa-proto-py-2.0.8/calixa_proto_py/condition_pb2.py
--rw-r--r--   0        0        0    24865 2022-05-13 13:50:54.499880 calixa-proto-py-2.0.8/calixa_proto_py/condition_pb2.pyi
--rw-r--r--   0        0        0      159 2022-05-13 13:50:54.499880 calixa-proto-py-2.0.8/calixa_proto_py/condition_pb2_grpc.py
--rw-r--r--   0        0        0      892 2022-05-13 13:50:52.775849 calixa-proto-py-2.0.8/calixa_proto_py/console_string.proto
--rw-r--r--   0        0        0     3236 2022-05-13 13:50:54.007871 calixa-proto-py-2.0.8/calixa_proto_py/console_string_pb2.py
--rw-r--r--   0        0        0     3168 2022-05-13 13:50:54.007871 calixa-proto-py-2.0.8/calixa_proto_py/console_string_pb2.pyi
--rw-r--r--   0        0        0      159 2022-05-13 13:50:54.007871 calixa-proto-py-2.0.8/calixa_proto_py/console_string_pb2_grpc.py
--rw-r--r--   0        0        0     4664 2022-05-13 13:50:52.779850 calixa-proto-py-2.0.8/calixa_proto_py/conversation.proto
--rw-r--r--   0        0        0     7548 2022-05-13 13:50:54.759885 calixa-proto-py-2.0.8/calixa_proto_py/conversation_pb2.py
--rw-r--r--   0        0        0     9988 2022-05-13 13:50:54.759885 calixa-proto-py-2.0.8/calixa_proto_py/conversation_pb2.pyi
--rw-r--r--   0        0        0      159 2022-05-13 13:50:54.759885 calixa-proto-py-2.0.8/calixa_proto_py/conversation_pb2_grpc.py
--rw-r--r--   0        0        0     1065 2022-05-13 13:50:52.783850 calixa-proto-py-2.0.8/calixa_proto_py/counter.proto
--rw-r--r--   0        0        0     4512 2022-05-13 13:50:54.151874 calixa-proto-py-2.0.8/calixa_proto_py/counter_pb2.py
--rw-r--r--   0        0        0     6143 2022-05-13 13:50:54.151874 calixa-proto-py-2.0.8/calixa_proto_py/counter_pb2.pyi
--rw-r--r--   0        0        0      159 2022-05-13 13:50:54.151874 calixa-proto-py-2.0.8/calixa_proto_py/counter_pb2_grpc.py
--rw-r--r--   0        0        0     1319 2022-05-13 13:50:52.787850 calixa-proto-py-2.0.8/calixa_proto_py/custom_entity.proto
--rw-r--r--   0        0        0     6136 2022-05-13 13:50:56.063908 calixa-proto-py-2.0.8/calixa_proto_py/custom_entity_pb2.py
--rw-r--r--   0        0        0     8513 2022-05-13 13:50:56.063908 calixa-proto-py-2.0.8/calixa_proto_py/custom_entity_pb2.pyi
--rw-r--r--   0        0        0      159 2022-05-13 13:50:56.063908 calixa-proto-py-2.0.8/calixa_proto_py/custom_entity_pb2_grpc.py
--rw-r--r--   0        0        0     4824 2022-05-13 13:50:52.791850 calixa-proto-py-2.0.8/calixa_proto_py/datawarehouse.proto
--rw-r--r--   0        0        0    23901 2022-05-13 13:50:56.163910 calixa-proto-py-2.0.8/calixa_proto_py/datawarehouse_pb2.py
--rw-r--r--   0        0        0    25857 2022-05-13 13:50:56.163910 calixa-proto-py-2.0.8/calixa_proto_py/datawarehouse_pb2.pyi
--rw-r--r--   0        0        0    20543 2022-05-13 13:50:56.163910 calixa-proto-py-2.0.8/calixa_proto_py/datawarehouse_pb2_grpc.py
--rw-r--r--   0        0        0     1410 2022-05-13 13:50:52.795850 calixa-proto-py-2.0.8/calixa_proto_py/domaindata.proto
--rw-r--r--   0        0        0     4425 2022-05-13 13:50:55.195893 calixa-proto-py-2.0.8/calixa_proto_py/domaindata_pb2.py
--rw-r--r--   0        0        0     3725 2022-05-13 13:50:55.195893 calixa-proto-py-2.0.8/calixa_proto_py/domaindata_pb2.pyi
--rw-r--r--   0        0        0      159 2022-05-13 13:50:55.195893 calixa-proto-py-2.0.8/calixa_proto_py/domaindata_pb2_grpc.py
--rw-r--r--   0        0        0    21669 2022-05-13 13:50:52.803850 calixa-proto-py-2.0.8/calixa_proto_py/entity.proto
--rw-r--r--   0        0        0    52588 2022-05-13 13:50:55.863905 calixa-proto-py-2.0.8/calixa_proto_py/entity_pb2.py
--rw-r--r--   0        0        0    76997 2022-05-13 13:50:55.863905 calixa-proto-py-2.0.8/calixa_proto_py/entity_pb2.pyi
--rw-r--r--   0        0        0    36359 2022-05-13 13:50:55.863905 calixa-proto-py-2.0.8/calixa_proto_py/entity_pb2_grpc.py
--rw-r--r--   0        0        0      551 2022-05-13 13:50:52.807850 calixa-proto-py-2.0.8/calixa_proto_py/entity_reference.proto
--rw-r--r--   0        0        0     1716 2022-05-13 13:50:53.595864 calixa-proto-py-2.0.8/calixa_proto_py/entity_reference_pb2.py
--rw-r--r--   0        0        0     2034 2022-05-13 13:50:53.595864 calixa-proto-py-2.0.8/calixa_proto_py/entity_reference_pb2.pyi
--rw-r--r--   0        0        0      159 2022-05-13 13:50:53.595864 calixa-proto-py-2.0.8/calixa_proto_py/entity_reference_pb2_grpc.py
--rw-r--r--   0        0        0     1699 2022-05-13 13:50:52.811850 calixa-proto-py-2.0.8/calixa_proto_py/event_label.proto
--rw-r--r--   0        0        0     4139 2022-05-13 13:50:56.011907 calixa-proto-py-2.0.8/calixa_proto_py/event_label_pb2.py
--rw-r--r--   0        0        0     5735 2022-05-13 13:50:56.011907 calixa-proto-py-2.0.8/calixa_proto_py/event_label_pb2.pyi
--rw-r--r--   0        0        0      159 2022-05-13 13:50:56.011907 calixa-proto-py-2.0.8/calixa_proto_py/event_label_pb2_grpc.py
--rw-r--r--   0        0        0    28733 2022-05-13 13:50:52.815850 calixa-proto-py-2.0.8/calixa_proto_py/external_domain_model.proto
--rw-r--r--   0        0        0    57727 2022-05-13 13:50:56.307913 calixa-proto-py-2.0.8/calixa_proto_py/external_domain_model_pb2.py
--rw-r--r--   0        0        0   122930 2022-05-13 13:50:56.307913 calixa-proto-py-2.0.8/calixa_proto_py/external_domain_model_pb2.pyi
--rw-r--r--   0        0        0      159 2022-05-13 13:50:56.307913 calixa-proto-py-2.0.8/calixa_proto_py/external_domain_model_pb2_grpc.py
--rw-r--r--   0        0        0     1078 2022-05-13 13:50:52.819850 calixa-proto-py-2.0.8/calixa_proto_py/external_entities_relinking.proto
--rw-r--r--   0        0        0     2832 2022-05-13 13:50:54.095873 calixa-proto-py-2.0.8/calixa_proto_py/external_entities_relinking_pb2.py
--rw-r--r--   0        0        0     2848 2022-05-13 13:50:54.095873 calixa-proto-py-2.0.8/calixa_proto_py/external_entities_relinking_pb2.pyi
--rw-r--r--   0        0        0      159 2022-05-13 13:50:54.095873 calixa-proto-py-2.0.8/calixa_proto_py/external_entities_relinking_pb2_grpc.py
--rw-r--r--   0        0        0     1313 2022-05-13 13:50:52.823850 calixa-proto-py-2.0.8/calixa_proto_py/import_log.proto
--rw-r--r--   0        0        0     5390 2022-05-13 13:50:54.967889 calixa-proto-py-2.0.8/calixa_proto_py/import_log_pb2.py
--rw-r--r--   0        0        0     6307 2022-05-13 13:50:54.967889 calixa-proto-py-2.0.8/calixa_proto_py/import_log_pb2.pyi
--rw-r--r--   0        0        0     4213 2022-05-13 13:50:54.967889 calixa-proto-py-2.0.8/calixa_proto_py/import_log_pb2_grpc.py
--rw-r--r--   0        0        0    17240 2022-05-13 13:50:52.827850 calixa-proto-py-2.0.8/calixa_proto_py/integration.proto
--rw-r--r--   0        0        0      385 2022-05-13 13:50:52.831850 calixa-proto-py-2.0.8/calixa_proto_py/integration_datawarehouse.proto
--rw-r--r--   0        0        0     1438 2022-05-13 13:50:54.591882 calixa-proto-py-2.0.8/calixa_proto_py/integration_datawarehouse_pb2.py
--rw-r--r--   0        0        0      353 2022-05-13 13:50:54.591882 calixa-proto-py-2.0.8/calixa_proto_py/integration_datawarehouse_pb2.pyi
--rw-r--r--   0        0        0      159 2022-05-13 13:50:54.591882 calixa-proto-py-2.0.8/calixa_proto_py/integration_datawarehouse_pb2_grpc.py
--rw-r--r--   0        0        0     2412 2022-05-13 13:50:52.835851 calixa-proto-py-2.0.8/calixa_proto_py/integration_elt.proto
--rw-r--r--   0        0        0     4094 2022-05-13 13:50:56.443915 calixa-proto-py-2.0.8/calixa_proto_py/integration_elt_pb2.py
--rw-r--r--   0        0        0     6184 2022-05-13 13:50:56.443915 calixa-proto-py-2.0.8/calixa_proto_py/integration_elt_pb2.pyi
--rw-r--r--   0        0        0      159 2022-05-13 13:50:56.443915 calixa-proto-py-2.0.8/calixa_proto_py/integration_elt_pb2_grpc.py
--rw-r--r--   0        0        0    10607 2022-05-13 13:50:52.839851 calixa-proto-py-2.0.8/calixa_proto_py/integration_manager.proto
--rw-r--r--   0        0        0    31880 2022-05-13 13:50:53.863869 calixa-proto-py-2.0.8/calixa_proto_py/integration_manager_pb2.py
--rw-r--r--   0        0        0    27595 2022-05-13 13:50:53.863869 calixa-proto-py-2.0.8/calixa_proto_py/integration_manager_pb2.pyi
--rw-r--r--   0        0        0    46507 2022-05-13 13:50:53.863869 calixa-proto-py-2.0.8/calixa_proto_py/integration_manager_pb2_grpc.py
--rw-r--r--   0        0        0    43957 2022-05-13 13:50:55.763903 calixa-proto-py-2.0.8/calixa_proto_py/integration_pb2.py
--rw-r--r--   0        0        0    51474 2022-05-13 13:50:55.763903 calixa-proto-py-2.0.8/calixa_proto_py/integration_pb2.pyi
--rw-r--r--   0        0        0    25970 2022-05-13 13:50:55.763903 calixa-proto-py-2.0.8/calixa_proto_py/integration_pb2_grpc.py
--rw-r--r--   0        0        0     2607 2022-05-13 13:50:52.843851 calixa-proto-py-2.0.8/calixa_proto_py/integration_source.proto
--rw-r--r--   0        0        0     4732 2022-05-13 13:50:56.355914 calixa-proto-py-2.0.8/calixa_proto_py/integration_source_pb2.py
--rw-r--r--   0        0        0     6607 2022-05-13 13:50:56.355914 calixa-proto-py-2.0.8/calixa_proto_py/integration_source_pb2.pyi
--rw-r--r--   0        0        0      159 2022-05-13 13:50:56.355914 calixa-proto-py-2.0.8/calixa_proto_py/integration_source_pb2_grpc.py
--rw-r--r--   0        0        0     5106 2022-05-13 13:50:52.851851 calixa-proto-py-2.0.8/calixa_proto_py/learning.proto
--rw-r--r--   0        0        0    11405 2022-05-13 13:50:53.715866 calixa-proto-py-2.0.8/calixa_proto_py/learning_pb2.py
--rw-r--r--   0        0        0    15794 2022-05-13 13:50:53.715866 calixa-proto-py-2.0.8/calixa_proto_py/learning_pb2.pyi
--rw-r--r--   0        0        0      159 2022-05-13 13:50:53.715866 calixa-proto-py-2.0.8/calixa_proto_py/learning_pb2_grpc.py
--rw-r--r--   0        0        0     2180 2022-05-13 13:50:52.855851 calixa-proto-py-2.0.8/calixa_proto_py/log.proto
--rw-r--r--   0        0        0     9933 2022-05-13 13:50:54.647883 calixa-proto-py-2.0.8/calixa_proto_py/log_pb2.py
--rw-r--r--   0        0        0    10581 2022-05-13 13:50:54.647883 calixa-proto-py-2.0.8/calixa_proto_py/log_pb2.pyi
--rw-r--r--   0        0        0     5649 2022-05-13 13:50:54.647883 calixa-proto-py-2.0.8/calixa_proto_py/log_pb2_grpc.py
--rw-r--r--   0        0        0     8083 2022-05-13 13:50:52.859851 calixa-proto-py-2.0.8/calixa_proto_py/metric.proto
--rw-r--r--   0        0        0    22904 2022-05-13 13:50:54.875887 calixa-proto-py-2.0.8/calixa_proto_py/metric_pb2.py
--rw-r--r--   0        0        0    30592 2022-05-13 13:50:54.875887 calixa-proto-py-2.0.8/calixa_proto_py/metric_pb2.pyi
--rw-r--r--   0        0        0    15947 2022-05-13 13:50:54.875887 calixa-proto-py-2.0.8/calixa_proto_py/metric_pb2_grpc.py
--rw-r--r--   0        0        0      915 2022-05-13 13:50:52.863851 calixa-proto-py-2.0.8/calixa_proto_py/notification_test_service.proto
--rw-r--r--   0        0        0     5080 2022-05-13 13:50:54.203875 calixa-proto-py-2.0.8/calixa_proto_py/notification_test_service_pb2.py
--rw-r--r--   0        0        0     5421 2022-05-13 13:50:54.203875 calixa-proto-py-2.0.8/calixa_proto_py/notification_test_service_pb2.pyi
--rw-r--r--   0        0        0     2823 2022-05-13 13:50:54.203875 calixa-proto-py-2.0.8/calixa_proto_py/notification_test_service_pb2_grpc.py
--rw-r--r--   0        0        0     9448 2022-05-13 13:50:52.867851 calixa-proto-py-2.0.8/calixa_proto_py/organization.proto
--rw-r--r--   0        0        0    25717 2022-05-13 13:50:53.659865 calixa-proto-py-2.0.8/calixa_proto_py/organization_pb2.py
--rw-r--r--   0        0        0    32417 2022-05-13 13:50:53.659865 calixa-proto-py-2.0.8/calixa_proto_py/organization_pb2.pyi
--rw-r--r--   0        0        0    21390 2022-05-13 13:50:53.659865 calixa-proto-py-2.0.8/calixa_proto_py/organization_pb2_grpc.py
--rw-r--r--   0        0        0      564 2022-05-13 13:50:52.871851 calixa-proto-py-2.0.8/calixa_proto_py/owner.proto
--rw-r--r--   0        0        0     1926 2022-05-13 13:50:54.251876 calixa-proto-py-2.0.8/calixa_proto_py/owner_pb2.py
--rw-r--r--   0        0        0     2313 2022-05-13 13:50:54.251876 calixa-proto-py-2.0.8/calixa_proto_py/owner_pb2.pyi
--rw-r--r--   0        0        0      159 2022-05-13 13:50:54.251876 calixa-proto-py-2.0.8/calixa_proto_py/owner_pb2_grpc.py
--rw-r--r--   0        0        0      338 2022-05-13 13:50:52.875851 calixa-proto-py-2.0.8/calixa_proto_py/pubsub.proto
--rw-r--r--   0        0        0     1701 2022-05-13 13:50:55.459898 calixa-proto-py-2.0.8/calixa_proto_py/pubsub_pb2.py
--rw-r--r--   0        0        0     1663 2022-05-13 13:50:55.459898 calixa-proto-py-2.0.8/calixa_proto_py/pubsub_pb2.pyi
--rw-r--r--   0        0        0      159 2022-05-13 13:50:55.459898 calixa-proto-py-2.0.8/calixa_proto_py/pubsub_pb2_grpc.py
--rw-r--r--   0        0        0     1965 2022-05-13 13:50:52.879851 calixa-proto-py-2.0.8/calixa_proto_py/push_notification.proto
--rw-r--r--   0        0        0     6095 2022-05-13 13:50:55.667901 calixa-proto-py-2.0.8/calixa_proto_py/push_notification_pb2.py
--rw-r--r--   0        0        0     9159 2022-05-13 13:50:55.667901 calixa-proto-py-2.0.8/calixa_proto_py/push_notification_pb2.pyi
--rw-r--r--   0        0        0      159 2022-05-13 13:50:55.667901 calixa-proto-py-2.0.8/calixa_proto_py/push_notification_pb2_grpc.py
--rw-r--r--   0        0        0     2794 2022-05-13 13:50:52.883851 calixa-proto-py-2.0.8/calixa_proto_py/related_data.proto
--rw-r--r--   0        0        0     5962 2022-05-13 13:50:54.351878 calixa-proto-py-2.0.8/calixa_proto_py/related_data_pb2.py
--rw-r--r--   0        0        0     8615 2022-05-13 13:50:54.351878 calixa-proto-py-2.0.8/calixa_proto_py/related_data_pb2.pyi
--rw-r--r--   0        0        0      159 2022-05-13 13:50:54.351878 calixa-proto-py-2.0.8/calixa_proto_py/related_data_pb2_grpc.py
--rw-r--r--   0        0        0     5534 2022-05-13 13:50:52.887852 calixa-proto-py-2.0.8/calixa_proto_py/search.proto
--rw-r--r--   0        0        0    13251 2022-05-13 13:50:55.551899 calixa-proto-py-2.0.8/calixa_proto_py/search_pb2.py
--rw-r--r--   0        0        0    17706 2022-05-13 13:50:55.551899 calixa-proto-py-2.0.8/calixa_proto_py/search_pb2.pyi
--rw-r--r--   0        0        0     7443 2022-05-13 13:50:55.551899 calixa-proto-py-2.0.8/calixa_proto_py/search_pb2_grpc.py
--rw-r--r--   0        0        0      750 2022-05-13 13:50:52.895852 calixa-proto-py-2.0.8/calixa_proto_py/segment.proto
--rw-r--r--   0        0        0     1886 2022-05-13 13:50:55.247894 calixa-proto-py-2.0.8/calixa_proto_py/segment_pb2.py
--rw-r--r--   0        0        0     2487 2022-05-13 13:50:55.247894 calixa-proto-py-2.0.8/calixa_proto_py/segment_pb2.pyi
--rw-r--r--   0        0        0      159 2022-05-13 13:50:55.247894 calixa-proto-py-2.0.8/calixa_proto_py/segment_pb2_grpc.py
--rw-r--r--   0        0        0      586 2022-05-13 13:50:52.899852 calixa-proto-py-2.0.8/calixa_proto_py/sidedata/annotation.proto
--rw-r--r--   0        0        0     2505 2022-05-13 13:50:56.499916 calixa-proto-py-2.0.8/calixa_proto_py/sidedata/annotation_pb2.py
--rw-r--r--   0        0        0     3148 2022-05-13 13:50:56.499916 calixa-proto-py-2.0.8/calixa_proto_py/sidedata/annotation_pb2.pyi
--rw-r--r--   0        0        0      159 2022-05-13 13:50:56.499916 calixa-proto-py-2.0.8/calixa_proto_py/sidedata/annotation_pb2_grpc.py
--rw-r--r--   0        0        0      293 2022-05-13 13:50:52.903852 calixa-proto-py-2.0.8/calixa_proto_py/tag.proto
--rw-r--r--   0        0        0     1408 2022-05-13 13:50:55.023890 calixa-proto-py-2.0.8/calixa_proto_py/tag_pb2.py
--rw-r--r--   0        0        0     1410 2022-05-13 13:50:55.023890 calixa-proto-py-2.0.8/calixa_proto_py/tag_pb2.pyi
--rw-r--r--   0        0        0      159 2022-05-13 13:50:55.023890 calixa-proto-py-2.0.8/calixa_proto_py/tag_pb2_grpc.py
--rw-r--r--   0        0        0      462 2022-05-13 13:48:35.269385 calixa-proto-py-2.0.8/pyproject.toml
--rw-r--r--   0        0        0      835 2022-05-13 13:50:57.135398 calixa-proto-py-2.0.8/setup.py
--rw-r--r--   0        0        0      568 2022-05-13 13:50:57.135717 calixa-proto-py-2.0.8/PKG-INFO
+-rw-r--r--   0        0        0       22 2022-06-28 20:32:02.206637 calixa-proto-py-2.0.9/calixa_proto_py/__init__.py
+-rw-r--r--   0        0        0     6129 2022-06-28 20:34:16.416920 calixa-proto-py-2.0.9/calixa_proto_py/account.proto
+-rw-r--r--   0        0        0    53320 2022-06-28 20:34:18.620956 calixa-proto-py-2.0.9/calixa_proto_py/account_pb2.py
+-rw-r--r--   0        0        0    20164 2022-06-28 20:34:18.620956 calixa-proto-py-2.0.9/calixa_proto_py/account_pb2.pyi
+-rw-r--r--   0        0        0      159 2022-06-28 20:34:18.620956 calixa-proto-py-2.0.9/calixa_proto_py/account_pb2_grpc.py
+-rw-r--r--   0        0        0     1297 2022-06-28 20:34:16.420920 calixa-proto-py-2.0.9/calixa_proto_py/account_service.proto
+-rw-r--r--   0        0        0    10556 2022-06-28 20:34:20.056983 calixa-proto-py-2.0.9/calixa_proto_py/account_service_pb2.py
+-rw-r--r--   0        0        0     3881 2022-06-28 20:34:20.056983 calixa-proto-py-2.0.9/calixa_proto_py/account_service_pb2.pyi
+-rw-r--r--   0        0        0     6121 2022-06-28 20:34:20.056983 calixa-proto-py-2.0.9/calixa_proto_py/account_service_pb2_grpc.py
+-rw-r--r--   0        0        0    11815 2022-06-28 20:34:16.424920 calixa-proto-py-2.0.9/calixa_proto_py/action.proto
+-rw-r--r--   0        0        0    89039 2022-06-28 20:34:18.560955 calixa-proto-py-2.0.9/calixa_proto_py/action_pb2.py
+-rw-r--r--   0        0        0    33824 2022-06-28 20:34:18.560955 calixa-proto-py-2.0.9/calixa_proto_py/action_pb2.pyi
+-rw-r--r--   0        0        0      159 2022-06-28 20:34:18.560955 calixa-proto-py-2.0.9/calixa_proto_py/action_pb2_grpc.py
+-rw-r--r--   0        0        0     2501 2022-06-28 20:34:16.428920 calixa-proto-py-2.0.9/calixa_proto_py/action_service.proto
+-rw-r--r--   0        0        0    21658 2022-06-28 20:34:18.096948 calixa-proto-py-2.0.9/calixa_proto_py/action_service_pb2.py
+-rw-r--r--   0        0        0     8421 2022-06-28 20:34:18.096948 calixa-proto-py-2.0.9/calixa_proto_py/action_service_pb2.pyi
+-rw-r--r--   0        0        0     7800 2022-06-28 20:34:18.096948 calixa-proto-py-2.0.9/calixa_proto_py/action_service_pb2_grpc.py
+-rw-r--r--   0        0        0     1198 2022-06-28 20:34:16.432920 calixa-proto-py-2.0.9/calixa_proto_py/authentication.proto
+-rw-r--r--   0        0        0    15991 2022-06-28 20:34:18.500954 calixa-proto-py-2.0.9/calixa_proto_py/authentication_pb2.py
+-rw-r--r--   0        0        0     5654 2022-06-28 20:34:18.500954 calixa-proto-py-2.0.9/calixa_proto_py/authentication_pb2.pyi
+-rw-r--r--   0        0        0     4368 2022-06-28 20:34:18.500954 calixa-proto-py-2.0.9/calixa_proto_py/authentication_pb2_grpc.py
+-rw-r--r--   0        0        0     3121 2022-06-28 20:34:16.436920 calixa-proto-py-2.0.9/calixa_proto_py/automation.proto
+-rw-r--r--   0        0        0      823 2022-06-28 20:34:16.440920 calixa-proto-py-2.0.9/calixa_proto_py/automation_log.proto
+-rw-r--r--   0        0        0     8544 2022-06-28 20:34:20.140984 calixa-proto-py-2.0.9/calixa_proto_py/automation_log_pb2.py
+-rw-r--r--   0        0        0     4084 2022-06-28 20:34:20.140984 calixa-proto-py-2.0.9/calixa_proto_py/automation_log_pb2.pyi
+-rw-r--r--   0        0        0      159 2022-06-28 20:34:20.140984 calixa-proto-py-2.0.9/calixa_proto_py/automation_log_pb2_grpc.py
+-rw-r--r--   0        0        0    35451 2022-06-28 20:34:20.304988 calixa-proto-py-2.0.9/calixa_proto_py/automation_pb2.py
+-rw-r--r--   0        0        0    14629 2022-06-28 20:34:20.304988 calixa-proto-py-2.0.9/calixa_proto_py/automation_pb2.pyi
+-rw-r--r--   0        0        0      159 2022-06-28 20:34:20.304988 calixa-proto-py-2.0.9/calixa_proto_py/automation_pb2_grpc.py
+-rw-r--r--   0        0        0     1176 2022-06-28 20:34:16.444920 calixa-proto-py-2.0.9/calixa_proto_py/automation_service.proto
+-rw-r--r--   0        0        0    10817 2022-06-28 20:34:18.948961 calixa-proto-py-2.0.9/calixa_proto_py/automation_service_pb2.py
+-rw-r--r--   0        0        0     2804 2022-06-28 20:34:18.948961 calixa-proto-py-2.0.9/calixa_proto_py/automation_service_pb2.pyi
+-rw-r--r--   0        0        0     7520 2022-06-28 20:34:18.948961 calixa-proto-py-2.0.9/calixa_proto_py/automation_service_pb2_grpc.py
+-rw-r--r--   0        0        0     6303 2022-06-28 20:34:16.448920 calixa-proto-py-2.0.9/calixa_proto_py/billing.proto
+-rw-r--r--   0        0        0    75500 2022-06-28 20:34:18.676957 calixa-proto-py-2.0.9/calixa_proto_py/billing_pb2.py
+-rw-r--r--   0        0        0    30213 2022-06-28 20:34:18.676957 calixa-proto-py-2.0.9/calixa_proto_py/billing_pb2.pyi
+-rw-r--r--   0        0        0      159 2022-06-28 20:34:18.676957 calixa-proto-py-2.0.9/calixa_proto_py/billing_pb2_grpc.py
+-rw-r--r--   0        0        0     2498 2022-06-28 20:34:16.452920 calixa-proto-py-2.0.9/calixa_proto_py/collaboration.proto
+-rw-r--r--   0        0        0     1856 2022-06-28 20:34:16.456920 calixa-proto-py-2.0.9/calixa_proto_py/collaboration_entity.proto
+-rw-r--r--   0        0        0    18734 2022-06-28 20:34:17.484937 calixa-proto-py-2.0.9/calixa_proto_py/collaboration_entity_pb2.py
+-rw-r--r--   0        0        0     7387 2022-06-28 20:34:17.484937 calixa-proto-py-2.0.9/calixa_proto_py/collaboration_entity_pb2.pyi
+-rw-r--r--   0        0        0      159 2022-06-28 20:34:17.484937 calixa-proto-py-2.0.9/calixa_proto_py/collaboration_entity_pb2_grpc.py
+-rw-r--r--   0        0        0    29657 2022-06-28 20:34:19.656975 calixa-proto-py-2.0.9/calixa_proto_py/collaboration_pb2.py
+-rw-r--r--   0        0        0     8105 2022-06-28 20:34:19.656975 calixa-proto-py-2.0.9/calixa_proto_py/collaboration_pb2.pyi
+-rw-r--r--   0        0        0    16114 2022-06-28 20:34:19.656975 calixa-proto-py-2.0.9/calixa_proto_py/collaboration_pb2_grpc.py
+-rw-r--r--   0        0        0     7113 2022-06-28 20:34:16.460920 calixa-proto-py-2.0.9/calixa_proto_py/common.proto
+-rw-r--r--   0        0        0    43285 2022-06-28 20:34:19.712976 calixa-proto-py-2.0.9/calixa_proto_py/common_pb2.py
+-rw-r--r--   0        0        0    17057 2022-06-28 20:34:19.712976 calixa-proto-py-2.0.9/calixa_proto_py/common_pb2.pyi
+-rw-r--r--   0        0        0     2525 2022-06-28 20:34:19.712976 calixa-proto-py-2.0.9/calixa_proto_py/common_pb2_grpc.py
+-rw-r--r--   0        0        0     6519 2022-06-28 20:34:16.464921 calixa-proto-py-2.0.9/calixa_proto_py/condition.proto
+-rw-r--r--   0        0        0    67176 2022-06-28 20:34:19.968981 calixa-proto-py-2.0.9/calixa_proto_py/condition_pb2.py
+-rw-r--r--   0        0        0    26810 2022-06-28 20:34:19.968981 calixa-proto-py-2.0.9/calixa_proto_py/condition_pb2.pyi
+-rw-r--r--   0        0        0      159 2022-06-28 20:34:19.968981 calixa-proto-py-2.0.9/calixa_proto_py/condition_pb2_grpc.py
+-rw-r--r--   0        0        0      892 2022-06-28 20:34:16.468921 calixa-proto-py-2.0.9/calixa_proto_py/console_string.proto
+-rw-r--r--   0        0        0     6989 2022-06-28 20:34:19.912980 calixa-proto-py-2.0.9/calixa_proto_py/console_string_pb2.py
+-rw-r--r--   0        0        0     3098 2022-06-28 20:34:19.912980 calixa-proto-py-2.0.9/calixa_proto_py/console_string_pb2.pyi
+-rw-r--r--   0        0        0      159 2022-06-28 20:34:19.912980 calixa-proto-py-2.0.9/calixa_proto_py/console_string_pb2_grpc.py
+-rw-r--r--   0        0        0     4664 2022-06-28 20:34:16.472921 calixa-proto-py-2.0.9/calixa_proto_py/conversation.proto
+-rw-r--r--   0        0        0    25509 2022-06-28 20:34:19.196966 calixa-proto-py-2.0.9/calixa_proto_py/conversation_pb2.py
+-rw-r--r--   0        0        0    10141 2022-06-28 20:34:19.196966 calixa-proto-py-2.0.9/calixa_proto_py/conversation_pb2.pyi
+-rw-r--r--   0        0        0      159 2022-06-28 20:34:19.196966 calixa-proto-py-2.0.9/calixa_proto_py/conversation_pb2_grpc.py
+-rw-r--r--   0        0        0     1065 2022-06-28 20:34:16.476921 calixa-proto-py-2.0.9/calixa_proto_py/counter.proto
+-rw-r--r--   0        0        0    14007 2022-06-28 20:34:18.152948 calixa-proto-py-2.0.9/calixa_proto_py/counter_pb2.py
+-rw-r--r--   0        0        0     6243 2022-06-28 20:34:18.152948 calixa-proto-py-2.0.9/calixa_proto_py/counter_pb2.pyi
+-rw-r--r--   0        0        0      159 2022-06-28 20:34:18.152948 calixa-proto-py-2.0.9/calixa_proto_py/counter_pb2_grpc.py
+-rw-r--r--   0        0        0     1319 2022-06-28 20:34:16.480921 calixa-proto-py-2.0.9/calixa_proto_py/custom_entity.proto
+-rw-r--r--   0        0        0    20590 2022-06-28 20:34:17.624940 calixa-proto-py-2.0.9/calixa_proto_py/custom_entity_pb2.py
+-rw-r--r--   0        0        0     8523 2022-06-28 20:34:17.624940 calixa-proto-py-2.0.9/calixa_proto_py/custom_entity_pb2.pyi
+-rw-r--r--   0        0        0      159 2022-06-28 20:34:17.624940 calixa-proto-py-2.0.9/calixa_proto_py/custom_entity_pb2_grpc.py
+-rw-r--r--   0        0        0     4824 2022-06-28 20:34:16.484921 calixa-proto-py-2.0.9/calixa_proto_py/datawarehouse.proto
+-rw-r--r--   0        0        0    72685 2022-06-28 20:34:18.344951 calixa-proto-py-2.0.9/calixa_proto_py/datawarehouse_pb2.py
+-rw-r--r--   0        0        0    25692 2022-06-28 20:34:18.344951 calixa-proto-py-2.0.9/calixa_proto_py/datawarehouse_pb2.pyi
+-rw-r--r--   0        0        0    20543 2022-06-28 20:34:18.344951 calixa-proto-py-2.0.9/calixa_proto_py/datawarehouse_pb2_grpc.py
+-rw-r--r--   0        0        0     1410 2022-06-28 20:34:16.488921 calixa-proto-py-2.0.9/calixa_proto_py/domaindata.proto
+-rw-r--r--   0        0        0     9326 2022-06-28 20:34:19.464971 calixa-proto-py-2.0.9/calixa_proto_py/domaindata_pb2.py
+-rw-r--r--   0        0        0     3759 2022-06-28 20:34:19.464971 calixa-proto-py-2.0.9/calixa_proto_py/domaindata_pb2.pyi
+-rw-r--r--   0        0        0      159 2022-06-28 20:34:19.464971 calixa-proto-py-2.0.9/calixa_proto_py/domaindata_pb2_grpc.py
+-rw-r--r--   0        0        0    23174 2022-06-28 20:34:16.492921 calixa-proto-py-2.0.9/calixa_proto_py/entity.proto
+-rw-r--r--   0        0        0   232374 2022-06-28 20:34:18.444953 calixa-proto-py-2.0.9/calixa_proto_py/entity_pb2.py
+-rw-r--r--   0        0        0    85585 2022-06-28 20:34:18.444953 calixa-proto-py-2.0.9/calixa_proto_py/entity_pb2.pyi
+-rw-r--r--   0        0        0    36359 2022-06-28 20:34:18.444953 calixa-proto-py-2.0.9/calixa_proto_py/entity_pb2_grpc.py
+-rw-r--r--   0        0        0      553 2022-06-28 20:34:16.496921 calixa-proto-py-2.0.9/calixa_proto_py/entity_reference.proto
+-rw-r--r--   0        0        0     4761 2022-06-28 20:34:17.764942 calixa-proto-py-2.0.9/calixa_proto_py/entity_reference_pb2.py
+-rw-r--r--   0        0        0     2036 2022-06-28 20:34:17.764942 calixa-proto-py-2.0.9/calixa_proto_py/entity_reference_pb2.pyi
+-rw-r--r--   0        0        0      159 2022-06-28 20:34:17.764942 calixa-proto-py-2.0.9/calixa_proto_py/entity_reference_pb2_grpc.py
+-rw-r--r--   0        0        0     1779 2022-06-28 20:34:16.500921 calixa-proto-py-2.0.9/calixa_proto_py/event_label.proto
+-rw-r--r--   0        0        0    11772 2022-06-28 20:34:19.296968 calixa-proto-py-2.0.9/calixa_proto_py/event_label_pb2.py
+-rw-r--r--   0        0        0     5761 2022-06-28 20:34:19.296968 calixa-proto-py-2.0.9/calixa_proto_py/event_label_pb2.pyi
+-rw-r--r--   0        0        0      159 2022-06-28 20:34:19.296968 calixa-proto-py-2.0.9/calixa_proto_py/event_label_pb2_grpc.py
+-rw-r--r--   0        0        0    28733 2022-06-28 20:34:16.504921 calixa-proto-py-2.0.9/calixa_proto_py/external_domain_model.proto
+-rw-r--r--   0        0        0   380457 2022-06-28 20:34:17.956945 calixa-proto-py-2.0.9/calixa_proto_py/external_domain_model_pb2.py
+-rw-r--r--   0        0        0   123109 2022-06-28 20:34:17.956945 calixa-proto-py-2.0.9/calixa_proto_py/external_domain_model_pb2.pyi
+-rw-r--r--   0        0        0      159 2022-06-28 20:34:17.956945 calixa-proto-py-2.0.9/calixa_proto_py/external_domain_model_pb2_grpc.py
+-rw-r--r--   0        0        0     1078 2022-06-28 20:34:16.508921 calixa-proto-py-2.0.9/calixa_proto_py/external_entities_relinking.proto
+-rw-r--r--   0        0        0     6576 2022-06-28 20:34:19.856979 calixa-proto-py-2.0.9/calixa_proto_py/external_entities_relinking_pb2.py
+-rw-r--r--   0        0        0     2843 2022-06-28 20:34:19.856979 calixa-proto-py-2.0.9/calixa_proto_py/external_entities_relinking_pb2.pyi
+-rw-r--r--   0        0        0      159 2022-06-28 20:34:19.856979 calixa-proto-py-2.0.9/calixa_proto_py/external_entities_relinking_pb2_grpc.py
+-rw-r--r--   0        0        0     1313 2022-06-28 20:34:16.512921 calixa-proto-py-2.0.9/calixa_proto_py/import_log.proto
+-rw-r--r--   0        0        0    16820 2022-06-28 20:34:18.768958 calixa-proto-py-2.0.9/calixa_proto_py/import_log_pb2.py
+-rw-r--r--   0        0        0     6288 2022-06-28 20:34:18.768958 calixa-proto-py-2.0.9/calixa_proto_py/import_log_pb2.pyi
+-rw-r--r--   0        0        0     4213 2022-06-28 20:34:18.768958 calixa-proto-py-2.0.9/calixa_proto_py/import_log_pb2_grpc.py
+-rw-r--r--   0        0        0     3412 2022-06-28 20:34:16.516921 calixa-proto-py-2.0.9/calixa_proto_py/inbox.proto
+-rw-r--r--   0        0        0    32467 2022-06-28 20:34:19.380970 calixa-proto-py-2.0.9/calixa_proto_py/inbox_pb2.py
+-rw-r--r--   0        0        0    11723 2022-06-28 20:34:19.380970 calixa-proto-py-2.0.9/calixa_proto_py/inbox_pb2.pyi
+-rw-r--r--   0        0        0     7238 2022-06-28 20:34:19.380970 calixa-proto-py-2.0.9/calixa_proto_py/inbox_pb2_grpc.py
+-rw-r--r--   0        0        0    17240 2022-06-28 20:34:16.520922 calixa-proto-py-2.0.9/calixa_proto_py/integration.proto
+-rw-r--r--   0        0        0      385 2022-06-28 20:34:16.524922 calixa-proto-py-2.0.9/calixa_proto_py/integration_datawarehouse.proto
+-rw-r--r--   0        0        0     1743 2022-06-28 20:34:18.856960 calixa-proto-py-2.0.9/calixa_proto_py/integration_datawarehouse_pb2.py
+-rw-r--r--   0        0        0      348 2022-06-28 20:34:18.856960 calixa-proto-py-2.0.9/calixa_proto_py/integration_datawarehouse_pb2.pyi
+-rw-r--r--   0        0        0      159 2022-06-28 20:34:18.856960 calixa-proto-py-2.0.9/calixa_proto_py/integration_datawarehouse_pb2_grpc.py
+-rw-r--r--   0        0        0     2412 2022-06-28 20:34:16.528922 calixa-proto-py-2.0.9/calixa_proto_py/integration_elt.proto
+-rw-r--r--   0        0        0    14204 2022-06-28 20:34:19.140965 calixa-proto-py-2.0.9/calixa_proto_py/integration_elt_pb2.py
+-rw-r--r--   0        0        0     6222 2022-06-28 20:34:19.140965 calixa-proto-py-2.0.9/calixa_proto_py/integration_elt_pb2.pyi
+-rw-r--r--   0        0        0      159 2022-06-28 20:34:19.140965 calixa-proto-py-2.0.9/calixa_proto_py/integration_elt_pb2_grpc.py
+-rw-r--r--   0        0        0    10607 2022-06-28 20:34:16.532922 calixa-proto-py-2.0.9/calixa_proto_py/integration_manager.proto
+-rw-r--r--   0        0        0    93423 2022-06-28 20:34:20.240986 calixa-proto-py-2.0.9/calixa_proto_py/integration_manager_pb2.py
+-rw-r--r--   0        0        0    27771 2022-06-28 20:34:20.240986 calixa-proto-py-2.0.9/calixa_proto_py/integration_manager_pb2.pyi
+-rw-r--r--   0        0        0    46507 2022-06-28 20:34:20.240986 calixa-proto-py-2.0.9/calixa_proto_py/integration_manager_pb2_grpc.py
+-rw-r--r--   0        0        0   144319 2022-06-28 20:34:17.864944 calixa-proto-py-2.0.9/calixa_proto_py/integration_pb2.py
+-rw-r--r--   0        0        0    51749 2022-06-28 20:34:17.864944 calixa-proto-py-2.0.9/calixa_proto_py/integration_pb2.pyi
+-rw-r--r--   0        0        0    25970 2022-06-28 20:34:17.864944 calixa-proto-py-2.0.9/calixa_proto_py/integration_pb2_grpc.py
+-rw-r--r--   0        0        0     2643 2022-06-28 20:34:16.536922 calixa-proto-py-2.0.9/calixa_proto_py/integration_source.proto
+-rw-r--r--   0        0        0    12306 2022-06-28 20:34:17.672940 calixa-proto-py-2.0.9/calixa_proto_py/integration_source_pb2.py
+-rw-r--r--   0        0        0     6885 2022-06-28 20:34:17.672940 calixa-proto-py-2.0.9/calixa_proto_py/integration_source_pb2.pyi
+-rw-r--r--   0        0        0      159 2022-06-28 20:34:17.672940 calixa-proto-py-2.0.9/calixa_proto_py/integration_source_pb2_grpc.py
+-rw-r--r--   0        0        0     5281 2022-06-28 20:34:16.540922 calixa-proto-py-2.0.9/calixa_proto_py/learning.proto
+-rw-r--r--   0        0        0    41759 2022-06-28 20:34:19.056963 calixa-proto-py-2.0.9/calixa_proto_py/learning_pb2.py
+-rw-r--r--   0        0        0    17224 2022-06-28 20:34:19.056963 calixa-proto-py-2.0.9/calixa_proto_py/learning_pb2.pyi
+-rw-r--r--   0        0        0      159 2022-06-28 20:34:19.056963 calixa-proto-py-2.0.9/calixa_proto_py/learning_pb2_grpc.py
+-rw-r--r--   0        0        0     2180 2022-06-28 20:34:16.544922 calixa-proto-py-2.0.9/calixa_proto_py/log.proto
+-rw-r--r--   0        0        0    30545 2022-06-28 20:34:19.568973 calixa-proto-py-2.0.9/calixa_proto_py/log_pb2.py
+-rw-r--r--   0        0        0    10437 2022-06-28 20:34:19.568973 calixa-proto-py-2.0.9/calixa_proto_py/log_pb2.pyi
+-rw-r--r--   0        0        0     5649 2022-06-28 20:34:19.568973 calixa-proto-py-2.0.9/calixa_proto_py/log_pb2_grpc.py
+-rw-r--r--   0        0        0     8085 2022-06-28 20:34:16.552922 calixa-proto-py-2.0.9/calixa_proto_py/metric.proto
+-rw-r--r--   0        0        0    82737 2022-06-28 20:34:19.776977 calixa-proto-py-2.0.9/calixa_proto_py/metric_pb2.py
+-rw-r--r--   0        0        0    30930 2022-06-28 20:34:19.776977 calixa-proto-py-2.0.9/calixa_proto_py/metric_pb2.pyi
+-rw-r--r--   0        0        0    15947 2022-06-28 20:34:19.776977 calixa-proto-py-2.0.9/calixa_proto_py/metric_pb2_grpc.py
+-rw-r--r--   0        0        0      915 2022-06-28 20:34:16.556922 calixa-proto-py-2.0.9/calixa_proto_py/notification_test_service.proto
+-rw-r--r--   0        0        0    15897 2022-06-28 20:34:18.248950 calixa-proto-py-2.0.9/calixa_proto_py/notification_test_service_pb2.py
+-rw-r--r--   0        0        0     5308 2022-06-28 20:34:18.248950 calixa-proto-py-2.0.9/calixa_proto_py/notification_test_service_pb2.pyi
+-rw-r--r--   0        0        0     2823 2022-06-28 20:34:18.248950 calixa-proto-py-2.0.9/calixa_proto_py/notification_test_service_pb2_grpc.py
+-rw-r--r--   0        0        0     7001 2022-06-28 20:34:16.560922 calixa-proto-py-2.0.9/calixa_proto_py/organization.proto
+-rw-r--r--   0        0        0    58731 2022-06-28 20:34:17.332935 calixa-proto-py-2.0.9/calixa_proto_py/organization_pb2.py
+-rw-r--r--   0        0        0    22196 2022-06-28 20:34:17.332935 calixa-proto-py-2.0.9/calixa_proto_py/organization_pb2.pyi
+-rw-r--r--   0        0        0     8876 2022-06-28 20:34:17.332935 calixa-proto-py-2.0.9/calixa_proto_py/organization_pb2_grpc.py
+-rw-r--r--   0        0        0     3494 2022-06-28 20:34:16.564922 calixa-proto-py-2.0.9/calixa_proto_py/organization_service.proto
+-rw-r--r--   0        0        0    41598 2022-06-28 20:34:17.568939 calixa-proto-py-2.0.9/calixa_proto_py/organization_service_pb2.py
+-rw-r--r--   0        0        0    13133 2022-06-28 20:34:17.568939 calixa-proto-py-2.0.9/calixa_proto_py/organization_service_pb2.pyi
+-rw-r--r--   0        0        0    23241 2022-06-28 20:34:17.568939 calixa-proto-py-2.0.9/calixa_proto_py/organization_service_pb2_grpc.py
+-rw-r--r--   0        0        0      564 2022-06-28 20:34:16.568922 calixa-proto-py-2.0.9/calixa_proto_py/owner.proto
+-rw-r--r--   0        0        0     4284 2022-06-28 20:34:17.716941 calixa-proto-py-2.0.9/calixa_proto_py/owner_pb2.py
+-rw-r--r--   0        0        0     2345 2022-06-28 20:34:17.716941 calixa-proto-py-2.0.9/calixa_proto_py/owner_pb2.pyi
+-rw-r--r--   0        0        0      159 2022-06-28 20:34:17.716941 calixa-proto-py-2.0.9/calixa_proto_py/owner_pb2_grpc.py
+-rw-r--r--   0        0        0     1754 2022-06-28 20:34:16.572922 calixa-proto-py-2.0.9/calixa_proto_py/playbook.proto
+-rw-r--r--   0        0        0    13886 2022-06-28 20:34:19.004962 calixa-proto-py-2.0.9/calixa_proto_py/playbook_pb2.py
+-rw-r--r--   0        0        0     4622 2022-06-28 20:34:19.004962 calixa-proto-py-2.0.9/calixa_proto_py/playbook_pb2.pyi
+-rw-r--r--   0        0        0     7306 2022-06-28 20:34:19.004962 calixa-proto-py-2.0.9/calixa_proto_py/playbook_pb2_grpc.py
+-rw-r--r--   0        0        0      338 2022-06-28 20:34:16.572922 calixa-proto-py-2.0.9/calixa_proto_py/pubsub.proto
+-rw-r--r--   0        0        0     3297 2022-06-28 20:34:17.276934 calixa-proto-py-2.0.9/calixa_proto_py/pubsub_pb2.py
+-rw-r--r--   0        0        0     1658 2022-06-28 20:34:17.276934 calixa-proto-py-2.0.9/calixa_proto_py/pubsub_pb2.pyi
+-rw-r--r--   0        0        0      159 2022-06-28 20:34:17.276934 calixa-proto-py-2.0.9/calixa_proto_py/pubsub_pb2_grpc.py
+-rw-r--r--   0        0        0     1965 2022-06-28 20:34:16.576923 calixa-proto-py-2.0.9/calixa_proto_py/push_notification.proto
+-rw-r--r--   0        0        0    24702 2022-06-28 20:34:19.248967 calixa-proto-py-2.0.9/calixa_proto_py/push_notification_pb2.py
+-rw-r--r--   0        0        0     9234 2022-06-28 20:34:19.248967 calixa-proto-py-2.0.9/calixa_proto_py/push_notification_pb2.pyi
+-rw-r--r--   0        0        0      159 2022-06-28 20:34:19.248967 calixa-proto-py-2.0.9/calixa_proto_py/push_notification_pb2_grpc.py
+-rw-r--r--   0        0        0     2859 2022-06-28 20:34:16.580922 calixa-proto-py-2.0.9/calixa_proto_py/related_data.proto
+-rw-r--r--   0        0        0    19075 2022-06-28 20:34:18.200949 calixa-proto-py-2.0.9/calixa_proto_py/related_data_pb2.py
+-rw-r--r--   0        0        0     8792 2022-06-28 20:34:18.200949 calixa-proto-py-2.0.9/calixa_proto_py/related_data_pb2.pyi
+-rw-r--r--   0        0        0      159 2022-06-28 20:34:18.200949 calixa-proto-py-2.0.9/calixa_proto_py/related_data_pb2_grpc.py
+-rw-r--r--   0        0        0     6636 2022-06-28 20:34:16.588923 calixa-proto-py-2.0.9/calixa_proto_py/search.proto
+-rw-r--r--   0        0        0    67350 2022-06-28 20:34:17.424936 calixa-proto-py-2.0.9/calixa_proto_py/search_pb2.py
+-rw-r--r--   0        0        0    23564 2022-06-28 20:34:17.424936 calixa-proto-py-2.0.9/calixa_proto_py/search_pb2.pyi
+-rw-r--r--   0        0        0     7443 2022-06-28 20:34:17.424936 calixa-proto-py-2.0.9/calixa_proto_py/search_pb2_grpc.py
+-rw-r--r--   0        0        0      889 2022-06-28 20:34:16.592923 calixa-proto-py-2.0.9/calixa_proto_py/segment.proto
+-rw-r--r--   0        0        0     6934 2022-06-28 20:34:19.516972 calixa-proto-py-2.0.9/calixa_proto_py/segment_pb2.py
+-rw-r--r--   0        0        0     2482 2022-06-28 20:34:19.516972 calixa-proto-py-2.0.9/calixa_proto_py/segment_pb2.pyi
+-rw-r--r--   0        0        0      159 2022-06-28 20:34:19.516972 calixa-proto-py-2.0.9/calixa_proto_py/segment_pb2_grpc.py
+-rw-r--r--   0        0        0      586 2022-06-28 20:34:16.596923 calixa-proto-py-2.0.9/calixa_proto_py/sidedata/annotation.proto
+-rw-r--r--   0        0        0     6309 2022-06-28 20:34:20.356989 calixa-proto-py-2.0.9/calixa_proto_py/sidedata/annotation_pb2.py
+-rw-r--r--   0        0        0     3193 2022-06-28 20:34:20.356989 calixa-proto-py-2.0.9/calixa_proto_py/sidedata/annotation_pb2.pyi
+-rw-r--r--   0        0        0      159 2022-06-28 20:34:20.356989 calixa-proto-py-2.0.9/calixa_proto_py/sidedata/annotation_pb2_grpc.py
+-rw-r--r--   0        0        0      293 2022-06-28 20:34:16.600923 calixa-proto-py-2.0.9/calixa_proto_py/tag.proto
+-rw-r--r--   0        0        0     3188 2022-06-28 20:34:18.008946 calixa-proto-py-2.0.9/calixa_proto_py/tag_pb2.py
+-rw-r--r--   0        0        0     1405 2022-06-28 20:34:18.008946 calixa-proto-py-2.0.9/calixa_proto_py/tag_pb2.pyi
+-rw-r--r--   0        0        0      159 2022-06-28 20:34:18.008946 calixa-proto-py-2.0.9/calixa_proto_py/tag_pb2_grpc.py
+-rw-r--r--   0        0        0      462 2022-06-28 20:32:02.206637 calixa-proto-py-2.0.9/pyproject.toml
+-rw-r--r--   0        0        0      835 2022-06-28 20:34:21.015948 calixa-proto-py-2.0.9/setup.py
+-rw-r--r--   0        0        0      568 2022-06-28 20:34:21.016233 calixa-proto-py-2.0.9/PKG-INFO
```

### Comparing `calixa-proto-py-2.0.8/calixa_proto_py/account.proto` & `calixa-proto-py-2.0.9/calixa_proto_py/account.proto`

 * *Files 2% similar despite different names*

```diff
@@ -85,20 +85,23 @@
   JourneyValue journey = 20 [(calixa.sidedata.def) = {
     data_type: HIGH_CARDINALITY,
     qualifier: 'j',
   }];
 
   repeated calixa.domain.entity.EntityReference enriched_with = 21;
 
-  repeated calixa.domain.learning.TaskModelPrediction predictions = 22 [(calixa.sidedata.def) = {
+  reserved 22;
+
+  int64 users_count = 23;
+
+  repeated PredictionValue predictions = 24 [(calixa.sidedata.def) = {
     data_type: HIGH_CARDINALITY,
-    qualifier: 'p',
+    qualifier: 'pv',
   }];
 
-  int64 users_count = 23;
 }
 
 enum AccountUserStatus {
   ACCOUNT_USER_STATUS_UNSPECIFIED = 0;
   ACCOUNT_USER_ACTIVE = 1;
   ACCOUNT_USER_SUSPENDED = 2;
   ACCOUNT_USER_DELETED = 3;
@@ -209,7 +212,14 @@
 
 // side-data encapsulating journey data:
 // 1) journey id 2) journey milestone id
 message JourneyValue {
   string journey_id = 1;
   string milestone_id = 2; // this can be "" in case of no milestone
 }
+
+// side-data encapsulating prediction data:
+// 1) prediction id 2) prediction value
+message PredictionValue {
+  string prediction_id = 1;
+  calixa.domain.learning.TaskModelPrediction prediction = 2;
+}
```

### Comparing `calixa-proto-py-2.0.8/calixa_proto_py/account_pb2.pyi` & `calixa-proto-py-2.0.9/calixa_proto_py/account_pb2.pyi`

 * *Files 10% similar despite different names*

```diff
@@ -1,11 +1,9 @@
-"""
-@generated by mypy-protobuf.  Do not edit manually!
-isort:skip_file
-"""
+# @generated by generate_proto_mypy_stubs.py.  Do not edit!
+import sys
 from common_pb2 import (
     Address as common_pb2___Address,
     Amount as common_pb2___Amount,
 )
 
 from entity_reference_pb2 import (
     EntityReference as entity_reference_pb2___EntityReference,
@@ -75,14 +73,15 @@
     ACCOUNT_ACTIVE = typing___cast(AccountStatusValue, 1)
     ACCOUNT_SUSPENDED = typing___cast(AccountStatusValue, 2)
     ACCOUNT_DELETED = typing___cast(AccountStatusValue, 3)
 ACCOUNT_STATUS_UNSPECIFIED = typing___cast(AccountStatusValue, 0)
 ACCOUNT_ACTIVE = typing___cast(AccountStatusValue, 1)
 ACCOUNT_SUSPENDED = typing___cast(AccountStatusValue, 2)
 ACCOUNT_DELETED = typing___cast(AccountStatusValue, 3)
+type___AccountStatus = AccountStatus
 
 OpportunityStatusValue = typing___NewType('OpportunityStatusValue', builtin___int)
 type___OpportunityStatusValue = OpportunityStatusValue
 OpportunityStatus: _OpportunityStatus
 class _OpportunityStatus(google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper[OpportunityStatusValue]):
     DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
     OPPORTUNITY_STATUS_UNSPECIFIED = typing___cast(OpportunityStatusValue, 0)
@@ -93,14 +92,15 @@
     OPPORTUNITY_STATUS_CLOSED_WON = typing___cast(OpportunityStatusValue, 5)
 OPPORTUNITY_STATUS_UNSPECIFIED = typing___cast(OpportunityStatusValue, 0)
 OPPORTUNITY_STATUS_OPEN = typing___cast(OpportunityStatusValue, 1)
 OPPORTUNITY_STATUS_CLOSED = typing___cast(OpportunityStatusValue, 2)
 OPPORTUNITY_STATUS_WON = typing___cast(OpportunityStatusValue, 3)
 OPPORTUNITY_STATUS_LOST = typing___cast(OpportunityStatusValue, 4)
 OPPORTUNITY_STATUS_CLOSED_WON = typing___cast(OpportunityStatusValue, 5)
+type___OpportunityStatus = OpportunityStatus
 
 AccountUserStatusValue = typing___NewType('AccountUserStatusValue', builtin___int)
 type___AccountUserStatusValue = AccountUserStatusValue
 AccountUserStatus: _AccountUserStatus
 class _AccountUserStatus(google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper[AccountUserStatusValue]):
     DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
     ACCOUNT_USER_STATUS_UNSPECIFIED = typing___cast(AccountUserStatusValue, 0)
@@ -109,14 +109,15 @@
     ACCOUNT_USER_DELETED = typing___cast(AccountUserStatusValue, 3)
     ACCOUNT_USER_INVITED = typing___cast(AccountUserStatusValue, 4)
 ACCOUNT_USER_STATUS_UNSPECIFIED = typing___cast(AccountUserStatusValue, 0)
 ACCOUNT_USER_ACTIVE = typing___cast(AccountUserStatusValue, 1)
 ACCOUNT_USER_SUSPENDED = typing___cast(AccountUserStatusValue, 2)
 ACCOUNT_USER_DELETED = typing___cast(AccountUserStatusValue, 3)
 ACCOUNT_USER_INVITED = typing___cast(AccountUserStatusValue, 4)
+type___AccountUserStatus = AccountUserStatus
 
 class Opportunity(google___protobuf___message___Message):
     DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
     name: typing___Text = ...
     description: typing___Text = ...
     stage: typing___Text = ...
     type: typing___Text = ...
@@ -190,15 +191,15 @@
     @property
     def journey(self) -> type___JourneyValue: ...
 
     @property
     def enriched_with(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[entity_reference_pb2___EntityReference]: ...
 
     @property
-    def predictions(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[learning_pb2___TaskModelPrediction]: ...
+    def predictions(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[type___PredictionValue]: ...
 
     def __init__(self,
         *,
         name : typing___Optional[typing___Text] = None,
         status : typing___Optional[type___AccountStatusValue] = None,
         domain_name : typing___Optional[typing___Text] = None,
         created_by_user_id : typing___Optional[typing___Text] = None,
@@ -207,16 +208,16 @@
         signed_up_at : typing___Optional[google___protobuf___timestamp_pb2___Timestamp] = None,
         first_seen_at : typing___Optional[google___protobuf___timestamp_pb2___Timestamp] = None,
         last_seen_at : typing___Optional[google___protobuf___timestamp_pb2___Timestamp] = None,
         owner : typing___Optional[owner_pb2___Owner] = None,
         score_value : typing___Optional[typing___Iterable[type___ScoreValue]] = None,
         journey : typing___Optional[type___JourneyValue] = None,
         enriched_with : typing___Optional[typing___Iterable[entity_reference_pb2___EntityReference]] = None,
-        predictions : typing___Optional[typing___Iterable[learning_pb2___TaskModelPrediction]] = None,
         users_count : typing___Optional[builtin___int] = None,
+        predictions : typing___Optional[typing___Iterable[type___PredictionValue]] = None,
         ) -> None: ...
     def HasField(self, field_name: typing_extensions___Literal[u"address",b"address",u"first_seen_at",b"first_seen_at",u"journey",b"journey",u"last_seen_at",b"last_seen_at",u"owner",b"owner",u"properties",b"properties",u"signed_up_at",b"signed_up_at"]) -> builtin___bool: ...
     def ClearField(self, field_name: typing_extensions___Literal[u"address",b"address",u"created_by_user_id",b"created_by_user_id",u"domain_name",b"domain_name",u"enriched_with",b"enriched_with",u"first_seen_at",b"first_seen_at",u"journey",b"journey",u"last_seen_at",b"last_seen_at",u"name",b"name",u"owner",b"owner",u"predictions",b"predictions",u"properties",b"properties",u"score_value",b"score_value",u"signed_up_at",b"signed_up_at",u"status",b"status",u"users_count",b"users_count"]) -> None: ...
 type___Account = Account
 
 class AccountAssociation(google___protobuf___message___Message):
     DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
@@ -375,7 +376,23 @@
     def __init__(self,
         *,
         journey_id : typing___Optional[typing___Text] = None,
         milestone_id : typing___Optional[typing___Text] = None,
         ) -> None: ...
     def ClearField(self, field_name: typing_extensions___Literal[u"journey_id",b"journey_id",u"milestone_id",b"milestone_id"]) -> None: ...
 type___JourneyValue = JourneyValue
+
+class PredictionValue(google___protobuf___message___Message):
+    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
+    prediction_id: typing___Text = ...
+
+    @property
+    def prediction(self) -> learning_pb2___TaskModelPrediction: ...
+
+    def __init__(self,
+        *,
+        prediction_id : typing___Optional[typing___Text] = None,
+        prediction : typing___Optional[learning_pb2___TaskModelPrediction] = None,
+        ) -> None: ...
+    def HasField(self, field_name: typing_extensions___Literal[u"prediction",b"prediction"]) -> builtin___bool: ...
+    def ClearField(self, field_name: typing_extensions___Literal[u"prediction",b"prediction",u"prediction_id",b"prediction_id"]) -> None: ...
+type___PredictionValue = PredictionValue
```

### Comparing `calixa-proto-py-2.0.8/calixa_proto_py/account_service.proto` & `calixa-proto-py-2.0.9/calixa_proto_py/account_service.proto`

 * *Files identical despite different names*

### Comparing `calixa-proto-py-2.0.8/calixa_proto_py/account_service_pb2.pyi` & `calixa-proto-py-2.0.9/calixa_proto_py/account_service_pb2.pyi`

 * *Files 2% similar despite different names*

```diff
@@ -1,11 +1,9 @@
-"""
-@generated by mypy-protobuf.  Do not edit manually!
-isort:skip_file
-"""
+# @generated by generate_proto_mypy_stubs.py.  Do not edit!
+import sys
 from common_pb2 import (
     ExternalId as common_pb2___ExternalId,
 )
 
 from entity_pb2 import (
     Entity as entity_pb2___Entity,
 )
```

### Comparing `calixa-proto-py-2.0.8/calixa_proto_py/account_service_pb2_grpc.py` & `calixa-proto-py-2.0.9/calixa_proto_py/account_service_pb2_grpc.py`

 * *Files identical despite different names*

### Comparing `calixa-proto-py-2.0.8/calixa_proto_py/action.proto` & `calixa-proto-py-2.0.9/calixa_proto_py/action.proto`

 * *Files 8% similar despite different names*

```diff
@@ -70,14 +70,16 @@
   google.protobuf.Timestamp timestamp = 2;
   string body = 3;
   string title = 4;
   string status = 5;
   string priority = 6;
   string account_id = 7; // This is the external Account ID in SF/HS
   string contact_id = 8; // This is the external Contact ID in SF/HS
+  reserved 9; // int64 relative_date_millis = 9
+  int32 relative_days = 10; // number of days to add to invocation dates when triggered from automation
 }
 
 message OwnershipUpdateParams {
   // HubSpot/Salesforce internal ID, coming from either:
   // - SALESFORCE_USER entity
   // - HUBSPOT_OWNER entity
   string owner_id = 1;
@@ -115,14 +117,19 @@
   google.protobuf.Struct payload = 2;
 }
 
 message RedirectParams {
   string url = 1;
 }
 
+message GetContactListParams {
+  string list_id = 1;
+  string name = 2;
+}
+
 message RequestConfig {
   string url = 1;
   string httpMethod = 2;
   repeated string headers = 3;
   // This is a payload that of static values that is configured into the Action.
   // When custom action is invoked, this payload and the payload created at
   // invocation time are merged together and sent to the the external APi
@@ -165,14 +172,16 @@
     TaskCreateParams task_create_params = 400;
     CadenceAddPersonParams cadence_add_person_params = 500;
     SequenceAddProspectParams sequence_add_prospect_params = 600;
     OwnershipUpdateParams ownership_update_params = 700;
 
     CustomParams custom_params = 10000;
     RedirectParams redirect_params = 10001;
+
+    GetContactListParams contact_list_params = 800;
   }
 
   reserved 536870911; // previously bool force
 }
 
 message ThirdPartyActionInvocationResponse {
   map<string, string> headers = 1;
@@ -204,14 +213,16 @@
   // Array with information about _how_ to render this action in the UI
   // For standard actions, this is statically defined (see DefaultActionConfigUtils.java)
   // For custom actions, this is going to be user defined through the action builder UI
   repeated DisplayField display_fields = 1000;
   // Array with information about _where_ to render this action in the UI
   // NOTE: Do not confuse with field #3 above, which is used as a constraint/validation helper
   repeated calixa.domain.common.EntityType display_on_entity_types = 1001;
+  
+  bool installed_by_parent_integration = 1002; // whenever an action is installed from the parent integration, this must be true
 }
 
 
 /**
   Example of Standard Actions mapped in the from end
   - https://github.com/calixa-io/console/blob/master/src/js/constants/action_constants.js#L27-L38:
 
@@ -269,24 +280,30 @@
           "entity" = {...} TODO Data of the affected entity –– Which subset of data to send?
        }
 
  */
 message DisplayField {
   string key = 1;
   string display = 2;
+
   DisplayFieldType field_type = 3;
   string placeholder = 4;
   bool required = 5;
 
   // For searchable entities the values below should be populated
   calixa.domain.common.EntityType supplied_by_entity_type = 6; // The entity type to be searched for
   repeated string supplied_by_id_name = 7; // List of possible paths in the object, used for display in the UI
+  string supplied_by_id_secondary_name = 10; // Secondary path to show fallback information in the UI
+
   string supplied_by_id_value = 8; // Path to the value to be used in the final action invocation call
   string supplied_by_entity_filter = 9; // optional entity filter console appends with AND on action search typings
 
+  DisplayFieldContext context = 11; // defines which context this can be used, automations or actions or both
+  string secondary_display = 12; // some new fields have information before (field display) and after (this field) the input
+
   repeated Value options = 100;
   map<string, string> initial_value = 101;
   map<string, string> render_when = 102;
   google.protobuf.Struct properties = 103;
 
   // Used to sort multiple display fields in one configuration. Use 0 to indicate a value was not appropriately set
   int32 order = 10000;
@@ -309,7 +326,16 @@
   DISPLAY_FIELD_TYPE_MICROS = 7;
   DISPLAY_FIELD_TYPE_NUMBER = 8;
   DISPLAY_FIELD_TYPE_PERCENTAGE = 9;
   DISPLAY_FIELD_TYPE_STRING = 10;
   DISPLAY_FIELD_TYPE_RENDERABLE = 11;
   DISPLAY_FIELD_TYPE_HIDDEN = 12;
 }
+
+/**
+ * This defines which context the display field will be rendered or used
+ */
+enum DisplayFieldContext {
+  DISPLAY_FIELD_CONTEXT_UNSPECIFIED = 0;
+  DISPLAY_FIELD_CONTEXT_ACTION = 1;
+  DISPLAY_FIELD_CONTEXT_AUTOMATION = 2;
+}
```

### Comparing `calixa-proto-py-2.0.8/calixa_proto_py/action_pb2.pyi` & `calixa-proto-py-2.0.9/calixa_proto_py/action_pb2.pyi`

 * *Files 2% similar despite different names*

```diff
@@ -1,26 +1,23 @@
-"""
-@generated by mypy-protobuf.  Do not edit manually!
-isort:skip_file
-"""
+# @generated by generate_proto_mypy_stubs.py.  Do not edit!
+import sys
 from common_pb2 import (
     Amount as common_pb2___Amount,
     EntityTypeValue as common_pb2___EntityTypeValue,
 )
 
 from google.protobuf.descriptor import (
     Descriptor as google___protobuf___descriptor___Descriptor,
     EnumDescriptor as google___protobuf___descriptor___EnumDescriptor,
     FileDescriptor as google___protobuf___descriptor___FileDescriptor,
 )
 
 from google.protobuf.internal.containers import (
     RepeatedCompositeFieldContainer as google___protobuf___internal___containers___RepeatedCompositeFieldContainer,
     RepeatedScalarFieldContainer as google___protobuf___internal___containers___RepeatedScalarFieldContainer,
-    ScalarMap as google___protobuf___internal___containers___ScalarMap,
 )
 
 from google.protobuf.internal.enum_type_wrapper import (
     _EnumTypeWrapper as google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper,
 )
 
 from google.protobuf.message import (
@@ -38,14 +35,15 @@
 from integration_source_pb2 import (
     IntegrationSourceValue as integration_source_pb2___IntegrationSourceValue,
 )
 
 from typing import (
     Iterable as typing___Iterable,
     Mapping as typing___Mapping,
+    MutableMapping as typing___MutableMapping,
     NewType as typing___NewType,
     Optional as typing___Optional,
     Text as typing___Text,
     cast as typing___cast,
 )
 
 from typing_extensions import (
@@ -68,26 +66,28 @@
     DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
     ACTION_STATE_UNSPECIFIED = typing___cast(ActionStateValue, 0)
     ACTION_STATE_ENABLED = typing___cast(ActionStateValue, 1)
     ACTION_STATE_DISABLED = typing___cast(ActionStateValue, 2)
 ACTION_STATE_UNSPECIFIED = typing___cast(ActionStateValue, 0)
 ACTION_STATE_ENABLED = typing___cast(ActionStateValue, 1)
 ACTION_STATE_DISABLED = typing___cast(ActionStateValue, 2)
+type___ActionState = ActionState
 
 ActionInvocationStatusValue = typing___NewType('ActionInvocationStatusValue', builtin___int)
 type___ActionInvocationStatusValue = ActionInvocationStatusValue
 ActionInvocationStatus: _ActionInvocationStatus
 class _ActionInvocationStatus(google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper[ActionInvocationStatusValue]):
     DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
     ACTION_INVOCATION_STATUS_UNSPECIFIED = typing___cast(ActionInvocationStatusValue, 0)
     ACTION_INVOCATION_STATUS_SUCCESS = typing___cast(ActionInvocationStatusValue, 1)
     ACTION_INVOCATION_STATUS_FAILED = typing___cast(ActionInvocationStatusValue, 2)
 ACTION_INVOCATION_STATUS_UNSPECIFIED = typing___cast(ActionInvocationStatusValue, 0)
 ACTION_INVOCATION_STATUS_SUCCESS = typing___cast(ActionInvocationStatusValue, 1)
 ACTION_INVOCATION_STATUS_FAILED = typing___cast(ActionInvocationStatusValue, 2)
+type___ActionInvocationStatus = ActionInvocationStatus
 
 AutomationActionFrequencyValue = typing___NewType('AutomationActionFrequencyValue', builtin___int)
 type___AutomationActionFrequencyValue = AutomationActionFrequencyValue
 AutomationActionFrequency: _AutomationActionFrequency
 class _AutomationActionFrequency(google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper[AutomationActionFrequencyValue]):
     DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
     AUTOMATION_FREQUENCY_UNSPECIFIED = typing___cast(AutomationActionFrequencyValue, 0)
@@ -102,14 +102,15 @@
 AUTOMATION_FREQUENCY_HOURLY = typing___cast(AutomationActionFrequencyValue, 1)
 AUTOMATION_FREQUENCY_DAILY = typing___cast(AutomationActionFrequencyValue, 2)
 AUTOMATION_FREQUENCY_WEEKLY = typing___cast(AutomationActionFrequencyValue, 3)
 AUTOMATION_FREQUENCY_MONTHLY = typing___cast(AutomationActionFrequencyValue, 4)
 AUTOMATION_FREQUENCY_QUARTERLY = typing___cast(AutomationActionFrequencyValue, 5)
 AUTOMATION_FREQUENCY_YEARLY = typing___cast(AutomationActionFrequencyValue, 6)
 AUTOMATION_FREQUENCY_ALL_TIME = typing___cast(AutomationActionFrequencyValue, 1000)
+type___AutomationActionFrequency = AutomationActionFrequency
 
 ActionTypeValue = typing___NewType('ActionTypeValue', builtin___int)
 type___ActionTypeValue = ActionTypeValue
 ActionType: _ActionType
 class _ActionType(google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper[ActionTypeValue]):
     DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
     ACTION_TYPE_UNSPECIFIED = typing___cast(ActionTypeValue, 0)
@@ -132,14 +133,15 @@
 ACTION_TYPE_OPPORTUNITY_CREATE_USER = typing___cast(ActionTypeValue, 301)
 ACTION_TYPE_TASK_CREATE = typing___cast(ActionTypeValue, 400)
 ACTION_TYPE_TASK_CREATE_USER = typing___cast(ActionTypeValue, 401)
 ACTION_TYPE_CADENCE_ADD_PERSON = typing___cast(ActionTypeValue, 500)
 ACTION_TYPE_SEQUENCE_ADD_PROSPECT = typing___cast(ActionTypeValue, 600)
 ACTION_TYPE_CUSTOM = typing___cast(ActionTypeValue, 10000)
 ACTION_TYPE_REDIRECT = typing___cast(ActionTypeValue, 10001)
+type___ActionType = ActionType
 
 DisplayFieldTypeValue = typing___NewType('DisplayFieldTypeValue', builtin___int)
 type___DisplayFieldTypeValue = DisplayFieldTypeValue
 DisplayFieldType: _DisplayFieldType
 class _DisplayFieldType(google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper[DisplayFieldTypeValue]):
     DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
     DISPLAY_FIELD_TYPE_UNSPECIFIED = typing___cast(DisplayFieldTypeValue, 0)
@@ -164,14 +166,28 @@
 DISPLAY_FIELD_TYPE_ENUM = typing___cast(DisplayFieldTypeValue, 6)
 DISPLAY_FIELD_TYPE_MICROS = typing___cast(DisplayFieldTypeValue, 7)
 DISPLAY_FIELD_TYPE_NUMBER = typing___cast(DisplayFieldTypeValue, 8)
 DISPLAY_FIELD_TYPE_PERCENTAGE = typing___cast(DisplayFieldTypeValue, 9)
 DISPLAY_FIELD_TYPE_STRING = typing___cast(DisplayFieldTypeValue, 10)
 DISPLAY_FIELD_TYPE_RENDERABLE = typing___cast(DisplayFieldTypeValue, 11)
 DISPLAY_FIELD_TYPE_HIDDEN = typing___cast(DisplayFieldTypeValue, 12)
+type___DisplayFieldType = DisplayFieldType
+
+DisplayFieldContextValue = typing___NewType('DisplayFieldContextValue', builtin___int)
+type___DisplayFieldContextValue = DisplayFieldContextValue
+DisplayFieldContext: _DisplayFieldContext
+class _DisplayFieldContext(google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper[DisplayFieldContextValue]):
+    DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
+    DISPLAY_FIELD_CONTEXT_UNSPECIFIED = typing___cast(DisplayFieldContextValue, 0)
+    DISPLAY_FIELD_CONTEXT_ACTION = typing___cast(DisplayFieldContextValue, 1)
+    DISPLAY_FIELD_CONTEXT_AUTOMATION = typing___cast(DisplayFieldContextValue, 2)
+DISPLAY_FIELD_CONTEXT_UNSPECIFIED = typing___cast(DisplayFieldContextValue, 0)
+DISPLAY_FIELD_CONTEXT_ACTION = typing___cast(DisplayFieldContextValue, 1)
+DISPLAY_FIELD_CONTEXT_AUTOMATION = typing___cast(DisplayFieldContextValue, 2)
+type___DisplayFieldContext = DisplayFieldContext
 
 class ChargeRefundParams(google___protobuf___message___Message):
     DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
     reason: typing___Text = ...
 
     @property
     def amount(self) -> common_pb2___Amount: ...
@@ -245,31 +261,33 @@
     owner_id: typing___Text = ...
     body: typing___Text = ...
     title: typing___Text = ...
     status: typing___Text = ...
     priority: typing___Text = ...
     account_id: typing___Text = ...
     contact_id: typing___Text = ...
+    relative_days: builtin___int = ...
 
     @property
     def timestamp(self) -> google___protobuf___timestamp_pb2___Timestamp: ...
 
     def __init__(self,
         *,
         owner_id : typing___Optional[typing___Text] = None,
         timestamp : typing___Optional[google___protobuf___timestamp_pb2___Timestamp] = None,
         body : typing___Optional[typing___Text] = None,
         title : typing___Optional[typing___Text] = None,
         status : typing___Optional[typing___Text] = None,
         priority : typing___Optional[typing___Text] = None,
         account_id : typing___Optional[typing___Text] = None,
         contact_id : typing___Optional[typing___Text] = None,
+        relative_days : typing___Optional[builtin___int] = None,
         ) -> None: ...
     def HasField(self, field_name: typing_extensions___Literal[u"timestamp",b"timestamp"]) -> builtin___bool: ...
-    def ClearField(self, field_name: typing_extensions___Literal[u"account_id",b"account_id",u"body",b"body",u"contact_id",b"contact_id",u"owner_id",b"owner_id",u"priority",b"priority",u"status",b"status",u"timestamp",b"timestamp",u"title",b"title"]) -> None: ...
+    def ClearField(self, field_name: typing_extensions___Literal[u"account_id",b"account_id",u"body",b"body",u"contact_id",b"contact_id",u"owner_id",b"owner_id",u"priority",b"priority",u"relative_days",b"relative_days",u"status",b"status",u"timestamp",b"timestamp",u"title",b"title"]) -> None: ...
 type___TaskCreateParams = TaskCreateParams
 
 class OwnershipUpdateParams(google___protobuf___message___Message):
     DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
     owner_id: typing___Text = ...
     owned_object_id: typing___Text = ...
     owned_object_type: common_pb2___EntityTypeValue = ...
@@ -334,14 +352,27 @@
     def __init__(self,
         *,
         url : typing___Optional[typing___Text] = None,
         ) -> None: ...
     def ClearField(self, field_name: typing_extensions___Literal[u"url",b"url"]) -> None: ...
 type___RedirectParams = RedirectParams
 
+class GetContactListParams(google___protobuf___message___Message):
+    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
+    list_id: typing___Text = ...
+    name: typing___Text = ...
+
+    def __init__(self,
+        *,
+        list_id : typing___Optional[typing___Text] = None,
+        name : typing___Optional[typing___Text] = None,
+        ) -> None: ...
+    def ClearField(self, field_name: typing_extensions___Literal[u"list_id",b"list_id",u"name",b"name"]) -> None: ...
+type___GetContactListParams = GetContactListParams
+
 class RequestConfig(google___protobuf___message___Message):
     DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
     url: typing___Text = ...
     httpMethod: typing___Text = ...
     headers: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text] = ...
 
     @property
@@ -387,30 +418,34 @@
 
     @property
     def custom_params(self) -> type___CustomParams: ...
 
     @property
     def redirect_params(self) -> type___RedirectParams: ...
 
+    @property
+    def contact_list_params(self) -> type___GetContactListParams: ...
+
     def __init__(self,
         *,
         charge_refund_params : typing___Optional[type___ChargeRefundParams] = None,
         subscription_trial_update_params : typing___Optional[type___SubscriptionTrialUpdateParams] = None,
         coupon_apply_params : typing___Optional[type___CouponApplyParams] = None,
         opportunity_create_params : typing___Optional[type___OpportunityCreateParams] = None,
         task_create_params : typing___Optional[type___TaskCreateParams] = None,
         cadence_add_person_params : typing___Optional[type___CadenceAddPersonParams] = None,
         sequence_add_prospect_params : typing___Optional[type___SequenceAddProspectParams] = None,
         ownership_update_params : typing___Optional[type___OwnershipUpdateParams] = None,
         custom_params : typing___Optional[type___CustomParams] = None,
         redirect_params : typing___Optional[type___RedirectParams] = None,
+        contact_list_params : typing___Optional[type___GetContactListParams] = None,
         ) -> None: ...
-    def HasField(self, field_name: typing_extensions___Literal[u"cadence_add_person_params",b"cadence_add_person_params",u"charge_refund_params",b"charge_refund_params",u"coupon_apply_params",b"coupon_apply_params",u"custom_params",b"custom_params",u"opportunity_create_params",b"opportunity_create_params",u"ownership_update_params",b"ownership_update_params",u"params",b"params",u"redirect_params",b"redirect_params",u"sequence_add_prospect_params",b"sequence_add_prospect_params",u"subscription_trial_update_params",b"subscription_trial_update_params",u"task_create_params",b"task_create_params"]) -> builtin___bool: ...
-    def ClearField(self, field_name: typing_extensions___Literal[u"cadence_add_person_params",b"cadence_add_person_params",u"charge_refund_params",b"charge_refund_params",u"coupon_apply_params",b"coupon_apply_params",u"custom_params",b"custom_params",u"opportunity_create_params",b"opportunity_create_params",u"ownership_update_params",b"ownership_update_params",u"params",b"params",u"redirect_params",b"redirect_params",u"sequence_add_prospect_params",b"sequence_add_prospect_params",u"subscription_trial_update_params",b"subscription_trial_update_params",u"task_create_params",b"task_create_params"]) -> None: ...
-    def WhichOneof(self, oneof_group: typing_extensions___Literal[u"params",b"params"]) -> typing_extensions___Literal["charge_refund_params","subscription_trial_update_params","coupon_apply_params","opportunity_create_params","task_create_params","cadence_add_person_params","sequence_add_prospect_params","ownership_update_params","custom_params","redirect_params"]: ...
+    def HasField(self, field_name: typing_extensions___Literal[u"cadence_add_person_params",b"cadence_add_person_params",u"charge_refund_params",b"charge_refund_params",u"contact_list_params",b"contact_list_params",u"coupon_apply_params",b"coupon_apply_params",u"custom_params",b"custom_params",u"opportunity_create_params",b"opportunity_create_params",u"ownership_update_params",b"ownership_update_params",u"params",b"params",u"redirect_params",b"redirect_params",u"sequence_add_prospect_params",b"sequence_add_prospect_params",u"subscription_trial_update_params",b"subscription_trial_update_params",u"task_create_params",b"task_create_params"]) -> builtin___bool: ...
+    def ClearField(self, field_name: typing_extensions___Literal[u"cadence_add_person_params",b"cadence_add_person_params",u"charge_refund_params",b"charge_refund_params",u"contact_list_params",b"contact_list_params",u"coupon_apply_params",b"coupon_apply_params",u"custom_params",b"custom_params",u"opportunity_create_params",b"opportunity_create_params",u"ownership_update_params",b"ownership_update_params",u"params",b"params",u"redirect_params",b"redirect_params",u"sequence_add_prospect_params",b"sequence_add_prospect_params",u"subscription_trial_update_params",b"subscription_trial_update_params",u"task_create_params",b"task_create_params"]) -> None: ...
+    def WhichOneof(self, oneof_group: typing_extensions___Literal[u"params",b"params"]) -> typing_extensions___Literal["charge_refund_params","subscription_trial_update_params","coupon_apply_params","opportunity_create_params","task_create_params","cadence_add_person_params","sequence_add_prospect_params","ownership_update_params","custom_params","redirect_params","contact_list_params"]: ...
 type___ActionParams = ActionParams
 
 class ThirdPartyActionInvocationResponse(google___protobuf___message___Message):
     DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
     class HeadersEntry(google___protobuf___message___Message):
         DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
         key: typing___Text = ...
@@ -437,18 +472,18 @@
         def ClearField(self, field_name: typing_extensions___Literal[u"key",b"key",u"value",b"value"]) -> None: ...
     type___MetaEntry = MetaEntry
 
     body: typing___Text = ...
     status_code: builtin___int = ...
 
     @property
-    def headers(self) -> google___protobuf___internal___containers___ScalarMap[typing___Text, typing___Text]: ...
+    def headers(self) -> typing___MutableMapping[typing___Text, typing___Text]: ...
 
     @property
-    def meta(self) -> google___protobuf___internal___containers___ScalarMap[typing___Text, typing___Text]: ...
+    def meta(self) -> typing___MutableMapping[typing___Text, typing___Text]: ...
 
     def __init__(self,
         *,
         headers : typing___Optional[typing___Mapping[typing___Text, typing___Text]] = None,
         meta : typing___Optional[typing___Mapping[typing___Text, typing___Text]] = None,
         body : typing___Optional[typing___Text] = None,
         status_code : typing___Optional[builtin___int] = None,
@@ -462,14 +497,15 @@
     source: integration_source_pb2___IntegrationSourceValue = ...
     entity_type: common_pb2___EntityTypeValue = ...
     created_by_organization_user: typing___Text = ...
     action_state: type___ActionStateValue = ...
     action_type: type___ActionTypeValue = ...
     description: typing___Text = ...
     display_on_entity_types: google___protobuf___internal___containers___RepeatedScalarFieldContainer[common_pb2___EntityTypeValue] = ...
+    installed_by_parent_integration: builtin___bool = ...
 
     @property
     def default_action_params(self) -> type___ActionParams: ...
 
     @property
     def request_config(self) -> type___RequestConfig: ...
 
@@ -485,17 +521,18 @@
         default_action_params : typing___Optional[type___ActionParams] = None,
         action_state : typing___Optional[type___ActionStateValue] = None,
         action_type : typing___Optional[type___ActionTypeValue] = None,
         description : typing___Optional[typing___Text] = None,
         request_config : typing___Optional[type___RequestConfig] = None,
         display_fields : typing___Optional[typing___Iterable[type___DisplayField]] = None,
         display_on_entity_types : typing___Optional[typing___Iterable[common_pb2___EntityTypeValue]] = None,
+        installed_by_parent_integration : typing___Optional[builtin___bool] = None,
         ) -> None: ...
     def HasField(self, field_name: typing_extensions___Literal[u"default_action_params",b"default_action_params",u"request_config",b"request_config"]) -> builtin___bool: ...
-    def ClearField(self, field_name: typing_extensions___Literal[u"action_state",b"action_state",u"action_type",b"action_type",u"created_by_organization_user",b"created_by_organization_user",u"default_action_params",b"default_action_params",u"description",b"description",u"display_fields",b"display_fields",u"display_on_entity_types",b"display_on_entity_types",u"entity_type",b"entity_type",u"request_config",b"request_config",u"source",b"source",u"title",b"title"]) -> None: ...
+    def ClearField(self, field_name: typing_extensions___Literal[u"action_state",b"action_state",u"action_type",b"action_type",u"created_by_organization_user",b"created_by_organization_user",u"default_action_params",b"default_action_params",u"description",b"description",u"display_fields",b"display_fields",u"display_on_entity_types",b"display_on_entity_types",u"entity_type",b"entity_type",u"installed_by_parent_integration",b"installed_by_parent_integration",u"request_config",b"request_config",u"source",b"source",u"title",b"title"]) -> None: ...
 type___ActionConfig = ActionConfig
 
 class DisplayField(google___protobuf___message___Message):
     DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
     class InitialValueEntry(google___protobuf___message___Message):
         DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
         key: typing___Text = ...
@@ -525,49 +562,55 @@
     key: typing___Text = ...
     display: typing___Text = ...
     field_type: type___DisplayFieldTypeValue = ...
     placeholder: typing___Text = ...
     required: builtin___bool = ...
     supplied_by_entity_type: common_pb2___EntityTypeValue = ...
     supplied_by_id_name: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text] = ...
+    supplied_by_id_secondary_name: typing___Text = ...
     supplied_by_id_value: typing___Text = ...
     supplied_by_entity_filter: typing___Text = ...
+    context: type___DisplayFieldContextValue = ...
+    secondary_display: typing___Text = ...
     order: builtin___int = ...
 
     @property
     def options(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[type___Value]: ...
 
     @property
-    def initial_value(self) -> google___protobuf___internal___containers___ScalarMap[typing___Text, typing___Text]: ...
+    def initial_value(self) -> typing___MutableMapping[typing___Text, typing___Text]: ...
 
     @property
-    def render_when(self) -> google___protobuf___internal___containers___ScalarMap[typing___Text, typing___Text]: ...
+    def render_when(self) -> typing___MutableMapping[typing___Text, typing___Text]: ...
 
     @property
     def properties(self) -> google___protobuf___struct_pb2___Struct: ...
 
     def __init__(self,
         *,
         key : typing___Optional[typing___Text] = None,
         display : typing___Optional[typing___Text] = None,
         field_type : typing___Optional[type___DisplayFieldTypeValue] = None,
         placeholder : typing___Optional[typing___Text] = None,
         required : typing___Optional[builtin___bool] = None,
         supplied_by_entity_type : typing___Optional[common_pb2___EntityTypeValue] = None,
         supplied_by_id_name : typing___Optional[typing___Iterable[typing___Text]] = None,
+        supplied_by_id_secondary_name : typing___Optional[typing___Text] = None,
         supplied_by_id_value : typing___Optional[typing___Text] = None,
         supplied_by_entity_filter : typing___Optional[typing___Text] = None,
+        context : typing___Optional[type___DisplayFieldContextValue] = None,
+        secondary_display : typing___Optional[typing___Text] = None,
         options : typing___Optional[typing___Iterable[type___Value]] = None,
         initial_value : typing___Optional[typing___Mapping[typing___Text, typing___Text]] = None,
         render_when : typing___Optional[typing___Mapping[typing___Text, typing___Text]] = None,
         properties : typing___Optional[google___protobuf___struct_pb2___Struct] = None,
         order : typing___Optional[builtin___int] = None,
         ) -> None: ...
     def HasField(self, field_name: typing_extensions___Literal[u"properties",b"properties"]) -> builtin___bool: ...
-    def ClearField(self, field_name: typing_extensions___Literal[u"display",b"display",u"field_type",b"field_type",u"initial_value",b"initial_value",u"key",b"key",u"options",b"options",u"order",b"order",u"placeholder",b"placeholder",u"properties",b"properties",u"render_when",b"render_when",u"required",b"required",u"supplied_by_entity_filter",b"supplied_by_entity_filter",u"supplied_by_entity_type",b"supplied_by_entity_type",u"supplied_by_id_name",b"supplied_by_id_name",u"supplied_by_id_value",b"supplied_by_id_value"]) -> None: ...
+    def ClearField(self, field_name: typing_extensions___Literal[u"context",b"context",u"display",b"display",u"field_type",b"field_type",u"initial_value",b"initial_value",u"key",b"key",u"options",b"options",u"order",b"order",u"placeholder",b"placeholder",u"properties",b"properties",u"render_when",b"render_when",u"required",b"required",u"secondary_display",b"secondary_display",u"supplied_by_entity_filter",b"supplied_by_entity_filter",u"supplied_by_entity_type",b"supplied_by_entity_type",u"supplied_by_id_name",b"supplied_by_id_name",u"supplied_by_id_secondary_name",b"supplied_by_id_secondary_name",u"supplied_by_id_value",b"supplied_by_id_value"]) -> None: ...
 type___DisplayField = DisplayField
 
 class Value(google___protobuf___message___Message):
     DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
     key: typing___Text = ...
     display: typing___Text = ...
```

### Comparing `calixa-proto-py-2.0.8/calixa_proto_py/action_service.proto` & `calixa-proto-py-2.0.9/calixa_proto_py/action_service.proto`

 * *Files 10% similar despite different names*

```diff
@@ -15,22 +15,30 @@
 
 enum CleanupStatus {
   CLEANUP_STATUS_UNSPECIFIED = 0;
   CLEANUP_STATUS_SUCCESS = 1;
   CLEANUP_STATUS_FAILURE = 2;
 }
 
-message GetActionsRequest {
+enum ActionOrigin {
+  ACTION_ORIGIN_UNSPECIFIED = 0;
+  ACTION_ORIGIN_USER = 1; // Console UI manual user action invocation
+  ACTION_ORIGIN_AUTOMATION = 2; // Automation Actions 
+  ACTION_ORIGIN_INTERNAL = 3; // Ownership Actions that are called internally
+}
 
+message GetActionsRequest {
+  ActionOrigin action_origin = 1;
 }
 
 message InvokeActionRequest {
   string action_canonical_id = 1;
   string entity_canonical_id = 2;
   calixa.domain.action.ActionParams override_action_params = 3;
+  ActionOrigin action_origin = 4;
 }
 
 message InvokeActionResponse {
   ActionInvocationStatus action_invocation_status = 1;
   calixa.domain.action.ThirdPartyActionInvocationResponse raw_response_payload = 2;
 }
 
@@ -51,20 +59,21 @@
  * NOTE: The effective integration details based on the 'source' field is going to be
  * determined in a best-effort kind of way until 'EntityOrigin' is properly backfilled
  * for all entities in the graph
  */
 message GetRelatedDataRequest {
   calixa.domain.relateddata.RelatedDataType related_data_type = 1;
   calixa.domain.integration.IntegrationSource source = 2;
+  ActionOrigin action_origin = 3;
 }
 
 message GetRelatedDataResponse {
   repeated calixa.domain.relateddata.RelatedData related_data = 1;
 }
 
 message IntegrationRemovalCleanupRequest {
   calixa.domain.integration.IntegrationSource source = 1;
 }
 
 message IntegrationRemovalCleanupResponse {
   CleanupStatus status = 1;
-}
+}
```

### Comparing `calixa-proto-py-2.0.8/calixa_proto_py/action_service_pb2.pyi` & `calixa-proto-py-2.0.9/calixa_proto_py/action_service_pb2.pyi`

 * *Files 15% similar despite different names*

```diff
@@ -1,11 +1,9 @@
-"""
-@generated by mypy-protobuf.  Do not edit manually!
-isort:skip_file
-"""
+# @generated by generate_proto_mypy_stubs.py.  Do not edit!
+import sys
 from action_pb2 import (
     ActionInvocationStatusValue as action_pb2___ActionInvocationStatusValue,
     ActionParams as action_pb2___ActionParams,
     ThirdPartyActionInvocationResponse as action_pb2___ThirdPartyActionInvocationResponse,
 )
 
 from google.protobuf.descriptor import (
@@ -63,38 +61,60 @@
     DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
     CLEANUP_STATUS_UNSPECIFIED = typing___cast(CleanupStatusValue, 0)
     CLEANUP_STATUS_SUCCESS = typing___cast(CleanupStatusValue, 1)
     CLEANUP_STATUS_FAILURE = typing___cast(CleanupStatusValue, 2)
 CLEANUP_STATUS_UNSPECIFIED = typing___cast(CleanupStatusValue, 0)
 CLEANUP_STATUS_SUCCESS = typing___cast(CleanupStatusValue, 1)
 CLEANUP_STATUS_FAILURE = typing___cast(CleanupStatusValue, 2)
+type___CleanupStatus = CleanupStatus
+
+ActionOriginValue = typing___NewType('ActionOriginValue', builtin___int)
+type___ActionOriginValue = ActionOriginValue
+ActionOrigin: _ActionOrigin
+class _ActionOrigin(google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper[ActionOriginValue]):
+    DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
+    ACTION_ORIGIN_UNSPECIFIED = typing___cast(ActionOriginValue, 0)
+    ACTION_ORIGIN_USER = typing___cast(ActionOriginValue, 1)
+    ACTION_ORIGIN_AUTOMATION = typing___cast(ActionOriginValue, 2)
+    ACTION_ORIGIN_INTERNAL = typing___cast(ActionOriginValue, 3)
+ACTION_ORIGIN_UNSPECIFIED = typing___cast(ActionOriginValue, 0)
+ACTION_ORIGIN_USER = typing___cast(ActionOriginValue, 1)
+ACTION_ORIGIN_AUTOMATION = typing___cast(ActionOriginValue, 2)
+ACTION_ORIGIN_INTERNAL = typing___cast(ActionOriginValue, 3)
+type___ActionOrigin = ActionOrigin
 
 class GetActionsRequest(google___protobuf___message___Message):
     DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
+    action_origin: type___ActionOriginValue = ...
 
     def __init__(self,
+        *,
+        action_origin : typing___Optional[type___ActionOriginValue] = None,
         ) -> None: ...
+    def ClearField(self, field_name: typing_extensions___Literal[u"action_origin",b"action_origin"]) -> None: ...
 type___GetActionsRequest = GetActionsRequest
 
 class InvokeActionRequest(google___protobuf___message___Message):
     DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
     action_canonical_id: typing___Text = ...
     entity_canonical_id: typing___Text = ...
+    action_origin: type___ActionOriginValue = ...
 
     @property
     def override_action_params(self) -> action_pb2___ActionParams: ...
 
     def __init__(self,
         *,
         action_canonical_id : typing___Optional[typing___Text] = None,
         entity_canonical_id : typing___Optional[typing___Text] = None,
         override_action_params : typing___Optional[action_pb2___ActionParams] = None,
+        action_origin : typing___Optional[type___ActionOriginValue] = None,
         ) -> None: ...
     def HasField(self, field_name: typing_extensions___Literal[u"override_action_params",b"override_action_params"]) -> builtin___bool: ...
-    def ClearField(self, field_name: typing_extensions___Literal[u"action_canonical_id",b"action_canonical_id",u"entity_canonical_id",b"entity_canonical_id",u"override_action_params",b"override_action_params"]) -> None: ...
+    def ClearField(self, field_name: typing_extensions___Literal[u"action_canonical_id",b"action_canonical_id",u"action_origin",b"action_origin",u"entity_canonical_id",b"entity_canonical_id",u"override_action_params",b"override_action_params"]) -> None: ...
 type___InvokeActionRequest = InvokeActionRequest
 
 class InvokeActionResponse(google___protobuf___message___Message):
     DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
     action_invocation_status: action_pb2___ActionInvocationStatusValue = ...
 
     @property
@@ -109,21 +129,23 @@
     def ClearField(self, field_name: typing_extensions___Literal[u"action_invocation_status",b"action_invocation_status",u"raw_response_payload",b"raw_response_payload"]) -> None: ...
 type___InvokeActionResponse = InvokeActionResponse
 
 class GetRelatedDataRequest(google___protobuf___message___Message):
     DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
     related_data_type: related_data_pb2___RelatedDataTypeValue = ...
     source: integration_source_pb2___IntegrationSourceValue = ...
+    action_origin: type___ActionOriginValue = ...
 
     def __init__(self,
         *,
         related_data_type : typing___Optional[related_data_pb2___RelatedDataTypeValue] = None,
         source : typing___Optional[integration_source_pb2___IntegrationSourceValue] = None,
+        action_origin : typing___Optional[type___ActionOriginValue] = None,
         ) -> None: ...
-    def ClearField(self, field_name: typing_extensions___Literal[u"related_data_type",b"related_data_type",u"source",b"source"]) -> None: ...
+    def ClearField(self, field_name: typing_extensions___Literal[u"action_origin",b"action_origin",u"related_data_type",b"related_data_type",u"source",b"source"]) -> None: ...
 type___GetRelatedDataRequest = GetRelatedDataRequest
 
 class GetRelatedDataResponse(google___protobuf___message___Message):
     DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
 
     @property
     def related_data(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[related_data_pb2___RelatedData]: ...
```

### Comparing `calixa-proto-py-2.0.8/calixa_proto_py/action_service_pb2_grpc.py` & `calixa-proto-py-2.0.9/calixa_proto_py/action_service_pb2_grpc.py`

 * *Files identical despite different names*

### Comparing `calixa-proto-py-2.0.8/calixa_proto_py/authentication.proto` & `calixa-proto-py-2.0.9/calixa_proto_py/authentication.proto`

 * *Files identical despite different names*

### Comparing `calixa-proto-py-2.0.8/calixa_proto_py/authentication_pb2.pyi` & `calixa-proto-py-2.0.9/calixa_proto_py/authentication_pb2.pyi`

 * *Files 8% similar despite different names*

```diff
@@ -1,11 +1,9 @@
-"""
-@generated by mypy-protobuf.  Do not edit manually!
-isort:skip_file
-"""
+# @generated by generate_proto_mypy_stubs.py.  Do not edit!
+import sys
 from google.protobuf.descriptor import (
     Descriptor as google___protobuf___descriptor___Descriptor,
     EnumDescriptor as google___protobuf___descriptor___EnumDescriptor,
     FileDescriptor as google___protobuf___descriptor___FileDescriptor,
 )
 
 from google.protobuf.internal.enum_type_wrapper import (
@@ -49,14 +47,15 @@
     IDENTITY_PROVIDER_PASSWORD = typing___cast(IdentityProviderValue, 1)
     IDENTITY_PROVIDER_GOOGLE = typing___cast(IdentityProviderValue, 2)
     IDENTITY_PROVIDER_GITHUB = typing___cast(IdentityProviderValue, 3)
 IDENTITY_PROVIDER_UNSPECIFIED = typing___cast(IdentityProviderValue, 0)
 IDENTITY_PROVIDER_PASSWORD = typing___cast(IdentityProviderValue, 1)
 IDENTITY_PROVIDER_GOOGLE = typing___cast(IdentityProviderValue, 2)
 IDENTITY_PROVIDER_GITHUB = typing___cast(IdentityProviderValue, 3)
+type___IdentityProvider = IdentityProvider
 
 class FirebaseUser(google___protobuf___message___Message):
     DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
     user_id: typing___Text = ...
     email: typing___Text = ...
     email_verified: builtin___bool = ...
     name: typing___Text = ...
```

### Comparing `calixa-proto-py-2.0.8/calixa_proto_py/authentication_pb2_grpc.py` & `calixa-proto-py-2.0.9/calixa_proto_py/authentication_pb2_grpc.py`

 * *Files identical despite different names*

### Comparing `calixa-proto-py-2.0.8/calixa_proto_py/automation.proto` & `calixa-proto-py-2.0.9/calixa_proto_py/automation.proto`

 * *Files 15% similar despite different names*

```diff
@@ -6,14 +6,15 @@
 import "google/protobuf/empty.proto";
 
 import "common.proto";
 import "event_label.proto";
 import "push_notification.proto";
 import "condition.proto";
 import "action.proto";
+import "entity_reference.proto";
 
 option java_package = "io.calixa.domain.automation";
 option java_multiple_files = true;
 option optimize_for = SPEED;
 
 package calixa.domain.automation;
 
@@ -56,42 +57,55 @@
 }
 
 message AutomationActionConfig {
   calixa.domain.action.ActionParams action_params = 1;
   string action_id = 2;
 }
 
+message SendToInboxAction {
+  entity.EntityReference entity_reference = 1;
+
+  string playbook_id = 2;
+
+  // this owner_id follow the same logic as Actions, if current_owner
+  // then get it from Ownership, otherwise set the value specified by UI
+  string owner_id = 3;
+}
+
 message AutomationAction {
   oneof automationAction {
     calixa.domain.notification.Notification notification = 1;
     AutomationActionConfig action = 3; // represents Standard and Custom Actions
+    SendToInboxAction send_to_inbox = 6;
   }
   reserved 2; // UpdateEntityAction update_entity = 2;
   reserved 5; // string task_owner = 5;
 
   AutomationActionSuppressionPeriod suppression_period = 4; // field used for automations
 
   string time_zone = 52;
 }
 
 message AutomationActionResult {
   oneof automationAction_Result {
     bool sent = 1;
-    HttpResponses httpResponses = 2;
+    HttpResponses http_responses = 2;
 
     string error = 1000;
     bool suppressed = 1001;
+    bool rate_limited = 1002;
   }
 }
 
 // Responses related to an Entity (canonical ID) from AutomationAction invoked through automations
 message HttpResponses {
-  map<string, action.ThirdPartyActionInvocationResponse> httpResponse = 1;
+  map<string, action.ThirdPartyActionInvocationResponse> http_response = 1;
 }
 
 message Automation {
   string title = 1;
   AutomationStatus status = 2;
   Trigger trigger = 3;
-  AutomationAction automationAction = 4;
+  AutomationAction automation_action = 4;
   common.EntityType entity_type = 5;
+  string created_by_organization_user_id = 6;
 }
```

### Comparing `calixa-proto-py-2.0.8/calixa_proto_py/automation_log.proto` & `calixa-proto-py-2.0.9/calixa_proto_py/automation_log.proto`

 * *Files 19% similar despite different names*

```diff
@@ -10,14 +10,15 @@
 option java_multiple_files = true;
 option optimize_for = SPEED;
 
 enum ExecutionStatus {
   EXECUTION_STATUS_UNSPECIFIED = 0;
   EXECUTION_STATUS_SUCCESS = 1;
   EXECUTION_STATUS_ERROR = 2;
+  EXECUTION_STATUS_RATE_LIMITED = 3;
 }
 
 message AutomationLog {
 
   string id = 1;
   google.protobuf.Timestamp started_at = 2;
   google.protobuf.Timestamp finished_at = 3;
```

### Comparing `calixa-proto-py-2.0.8/calixa_proto_py/automation_log_pb2.pyi` & `calixa-proto-py-2.0.9/calixa_proto_py/automation_log_pb2.pyi`

 * *Files 4% similar despite different names*

```diff
@@ -1,11 +1,9 @@
-"""
-@generated by mypy-protobuf.  Do not edit manually!
-isort:skip_file
-"""
+# @generated by generate_proto_mypy_stubs.py.  Do not edit!
+import sys
 from action_pb2 import (
     ThirdPartyActionInvocationResponse as action_pb2___ThirdPartyActionInvocationResponse,
 )
 
 from entity_pb2 import (
     Entity as entity_pb2___Entity,
 )
@@ -52,17 +50,20 @@
 type___ExecutionStatusValue = ExecutionStatusValue
 ExecutionStatus: _ExecutionStatus
 class _ExecutionStatus(google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper[ExecutionStatusValue]):
     DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
     EXECUTION_STATUS_UNSPECIFIED = typing___cast(ExecutionStatusValue, 0)
     EXECUTION_STATUS_SUCCESS = typing___cast(ExecutionStatusValue, 1)
     EXECUTION_STATUS_ERROR = typing___cast(ExecutionStatusValue, 2)
+    EXECUTION_STATUS_RATE_LIMITED = typing___cast(ExecutionStatusValue, 3)
 EXECUTION_STATUS_UNSPECIFIED = typing___cast(ExecutionStatusValue, 0)
 EXECUTION_STATUS_SUCCESS = typing___cast(ExecutionStatusValue, 1)
 EXECUTION_STATUS_ERROR = typing___cast(ExecutionStatusValue, 2)
+EXECUTION_STATUS_RATE_LIMITED = typing___cast(ExecutionStatusValue, 3)
+type___ExecutionStatus = ExecutionStatus
 
 class AutomationLog(google___protobuf___message___Message):
     DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
     id: typing___Text = ...
     status: type___ExecutionStatusValue = ...
     error: typing___Text = ...
```

### Comparing `calixa-proto-py-2.0.8/calixa_proto_py/automation_pb2.pyi` & `calixa-proto-py-2.0.9/calixa_proto_py/automation_pb2.pyi`

 * *Files 12% similar despite different names*

```diff
@@ -1,52 +1,51 @@
-"""
-@generated by mypy-protobuf.  Do not edit manually!
-isort:skip_file
-"""
+# @generated by generate_proto_mypy_stubs.py.  Do not edit!
+import sys
 from action_pb2 import (
     ActionParams as action_pb2___ActionParams,
     ThirdPartyActionInvocationResponse as action_pb2___ThirdPartyActionInvocationResponse,
 )
 
 from common_pb2 import (
     EntityTypeValue as common_pb2___EntityTypeValue,
 )
 
 from condition_pb2 import (
     ConditionGroup as condition_pb2___ConditionGroup,
 )
 
+from entity_reference_pb2 import (
+    EntityReference as entity_reference_pb2___EntityReference,
+)
+
 from event_label_pb2 import (
     EventLabelValue as event_label_pb2___EventLabelValue,
 )
 
 from google.protobuf.descriptor import (
     Descriptor as google___protobuf___descriptor___Descriptor,
     EnumDescriptor as google___protobuf___descriptor___EnumDescriptor,
     FileDescriptor as google___protobuf___descriptor___FileDescriptor,
 )
 
-from google.protobuf.internal.containers import (
-    MessageMap as google___protobuf___internal___containers___MessageMap,
-)
-
 from google.protobuf.internal.enum_type_wrapper import (
     _EnumTypeWrapper as google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper,
 )
 
 from google.protobuf.message import (
     Message as google___protobuf___message___Message,
 )
 
 from push_notification_pb2 import (
     Notification as push_notification_pb2___Notification,
 )
 
 from typing import (
     Mapping as typing___Mapping,
+    MutableMapping as typing___MutableMapping,
     NewType as typing___NewType,
     Optional as typing___Optional,
     Text as typing___Text,
     cast as typing___cast,
 )
 
 from typing_extensions import (
@@ -69,14 +68,15 @@
     DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
     AUTOMATION_STATUS_UNSPECIFIED = typing___cast(AutomationStatusValue, 0)
     AUTOMATION_STATUS_ENABLED = typing___cast(AutomationStatusValue, 1)
     AUTOMATION_STATUS_PAUSED = typing___cast(AutomationStatusValue, 2)
 AUTOMATION_STATUS_UNSPECIFIED = typing___cast(AutomationStatusValue, 0)
 AUTOMATION_STATUS_ENABLED = typing___cast(AutomationStatusValue, 1)
 AUTOMATION_STATUS_PAUSED = typing___cast(AutomationStatusValue, 2)
+type___AutomationStatus = AutomationStatus
 
 AutomationActionSuppressionPeriodValue = typing___NewType('AutomationActionSuppressionPeriodValue', builtin___int)
 type___AutomationActionSuppressionPeriodValue = AutomationActionSuppressionPeriodValue
 AutomationActionSuppressionPeriod: _AutomationActionSuppressionPeriod
 class _AutomationActionSuppressionPeriod(google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper[AutomationActionSuppressionPeriodValue]):
     DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
     AUTOMATION_SUPPRESSION_PERIOD_UNSPECIFIED = typing___cast(AutomationActionSuppressionPeriodValue, 0)
@@ -91,14 +91,15 @@
 AUTOMATION_SUPPRESSION_PERIOD_HOURLY = typing___cast(AutomationActionSuppressionPeriodValue, 1)
 AUTOMATION_SUPPRESSION_PERIOD_DAILY = typing___cast(AutomationActionSuppressionPeriodValue, 2)
 AUTOMATION_SUPPRESSION_PERIOD_WEEKLY = typing___cast(AutomationActionSuppressionPeriodValue, 3)
 AUTOMATION_SUPPRESSION_PERIOD_MONTHLY = typing___cast(AutomationActionSuppressionPeriodValue, 4)
 AUTOMATION_SUPPRESSION_PERIOD_QUARTERLY = typing___cast(AutomationActionSuppressionPeriodValue, 5)
 AUTOMATION_SUPPRESSION_PERIOD_YEARLY = typing___cast(AutomationActionSuppressionPeriodValue, 6)
 AUTOMATION_SUPPRESSION_PERIOD_ALL_TIME = typing___cast(AutomationActionSuppressionPeriodValue, 1000)
+type___AutomationActionSuppressionPeriod = AutomationActionSuppressionPeriod
 
 class EventTrigger(google___protobuf___message___Message):
     DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
     event_label: event_label_pb2___EventLabelValue = ...
 
     @property
     def trigger(self) -> condition_pb2___ConditionGroup: ...
@@ -157,56 +158,80 @@
         action_params : typing___Optional[action_pb2___ActionParams] = None,
         action_id : typing___Optional[typing___Text] = None,
         ) -> None: ...
     def HasField(self, field_name: typing_extensions___Literal[u"action_params",b"action_params"]) -> builtin___bool: ...
     def ClearField(self, field_name: typing_extensions___Literal[u"action_id",b"action_id",u"action_params",b"action_params"]) -> None: ...
 type___AutomationActionConfig = AutomationActionConfig
 
+class SendToInboxAction(google___protobuf___message___Message):
+    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
+    playbook_id: typing___Text = ...
+    owner_id: typing___Text = ...
+
+    @property
+    def entity_reference(self) -> entity_reference_pb2___EntityReference: ...
+
+    def __init__(self,
+        *,
+        entity_reference : typing___Optional[entity_reference_pb2___EntityReference] = None,
+        playbook_id : typing___Optional[typing___Text] = None,
+        owner_id : typing___Optional[typing___Text] = None,
+        ) -> None: ...
+    def HasField(self, field_name: typing_extensions___Literal[u"entity_reference",b"entity_reference"]) -> builtin___bool: ...
+    def ClearField(self, field_name: typing_extensions___Literal[u"entity_reference",b"entity_reference",u"owner_id",b"owner_id",u"playbook_id",b"playbook_id"]) -> None: ...
+type___SendToInboxAction = SendToInboxAction
+
 class AutomationAction(google___protobuf___message___Message):
     DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
     suppression_period: type___AutomationActionSuppressionPeriodValue = ...
     time_zone: typing___Text = ...
 
     @property
     def notification(self) -> push_notification_pb2___Notification: ...
 
     @property
     def action(self) -> type___AutomationActionConfig: ...
 
+    @property
+    def send_to_inbox(self) -> type___SendToInboxAction: ...
+
     def __init__(self,
         *,
         notification : typing___Optional[push_notification_pb2___Notification] = None,
         action : typing___Optional[type___AutomationActionConfig] = None,
+        send_to_inbox : typing___Optional[type___SendToInboxAction] = None,
         suppression_period : typing___Optional[type___AutomationActionSuppressionPeriodValue] = None,
         time_zone : typing___Optional[typing___Text] = None,
         ) -> None: ...
-    def HasField(self, field_name: typing_extensions___Literal[u"action",b"action",u"automationAction",b"automationAction",u"notification",b"notification"]) -> builtin___bool: ...
-    def ClearField(self, field_name: typing_extensions___Literal[u"action",b"action",u"automationAction",b"automationAction",u"notification",b"notification",u"suppression_period",b"suppression_period",u"time_zone",b"time_zone"]) -> None: ...
-    def WhichOneof(self, oneof_group: typing_extensions___Literal[u"automationAction",b"automationAction"]) -> typing_extensions___Literal["notification","action"]: ...
+    def HasField(self, field_name: typing_extensions___Literal[u"action",b"action",u"automationAction",b"automationAction",u"notification",b"notification",u"send_to_inbox",b"send_to_inbox"]) -> builtin___bool: ...
+    def ClearField(self, field_name: typing_extensions___Literal[u"action",b"action",u"automationAction",b"automationAction",u"notification",b"notification",u"send_to_inbox",b"send_to_inbox",u"suppression_period",b"suppression_period",u"time_zone",b"time_zone"]) -> None: ...
+    def WhichOneof(self, oneof_group: typing_extensions___Literal[u"automationAction",b"automationAction"]) -> typing_extensions___Literal["notification","action","send_to_inbox"]: ...
 type___AutomationAction = AutomationAction
 
 class AutomationActionResult(google___protobuf___message___Message):
     DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
     sent: builtin___bool = ...
     error: typing___Text = ...
     suppressed: builtin___bool = ...
+    rate_limited: builtin___bool = ...
 
     @property
-    def httpResponses(self) -> type___HttpResponses: ...
+    def http_responses(self) -> type___HttpResponses: ...
 
     def __init__(self,
         *,
         sent : typing___Optional[builtin___bool] = None,
-        httpResponses : typing___Optional[type___HttpResponses] = None,
+        http_responses : typing___Optional[type___HttpResponses] = None,
         error : typing___Optional[typing___Text] = None,
         suppressed : typing___Optional[builtin___bool] = None,
+        rate_limited : typing___Optional[builtin___bool] = None,
         ) -> None: ...
-    def HasField(self, field_name: typing_extensions___Literal[u"automationAction_Result",b"automationAction_Result",u"error",b"error",u"httpResponses",b"httpResponses",u"sent",b"sent",u"suppressed",b"suppressed"]) -> builtin___bool: ...
-    def ClearField(self, field_name: typing_extensions___Literal[u"automationAction_Result",b"automationAction_Result",u"error",b"error",u"httpResponses",b"httpResponses",u"sent",b"sent",u"suppressed",b"suppressed"]) -> None: ...
-    def WhichOneof(self, oneof_group: typing_extensions___Literal[u"automationAction_Result",b"automationAction_Result"]) -> typing_extensions___Literal["sent","httpResponses","error","suppressed"]: ...
+    def HasField(self, field_name: typing_extensions___Literal[u"automationAction_Result",b"automationAction_Result",u"error",b"error",u"http_responses",b"http_responses",u"rate_limited",b"rate_limited",u"sent",b"sent",u"suppressed",b"suppressed"]) -> builtin___bool: ...
+    def ClearField(self, field_name: typing_extensions___Literal[u"automationAction_Result",b"automationAction_Result",u"error",b"error",u"http_responses",b"http_responses",u"rate_limited",b"rate_limited",u"sent",b"sent",u"suppressed",b"suppressed"]) -> None: ...
+    def WhichOneof(self, oneof_group: typing_extensions___Literal[u"automationAction_Result",b"automationAction_Result"]) -> typing_extensions___Literal["sent","http_responses","error","suppressed","rate_limited"]: ...
 type___AutomationActionResult = AutomationActionResult
 
 class HttpResponses(google___protobuf___message___Message):
     DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
     class HttpResponseEntry(google___protobuf___message___Message):
         DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
         key: typing___Text = ...
@@ -221,39 +246,41 @@
             ) -> None: ...
         def HasField(self, field_name: typing_extensions___Literal[u"value",b"value"]) -> builtin___bool: ...
         def ClearField(self, field_name: typing_extensions___Literal[u"key",b"key",u"value",b"value"]) -> None: ...
     type___HttpResponseEntry = HttpResponseEntry
 
 
     @property
-    def httpResponse(self) -> google___protobuf___internal___containers___MessageMap[typing___Text, action_pb2___ThirdPartyActionInvocationResponse]: ...
+    def http_response(self) -> typing___MutableMapping[typing___Text, action_pb2___ThirdPartyActionInvocationResponse]: ...
 
     def __init__(self,
         *,
-        httpResponse : typing___Optional[typing___Mapping[typing___Text, action_pb2___ThirdPartyActionInvocationResponse]] = None,
+        http_response : typing___Optional[typing___Mapping[typing___Text, action_pb2___ThirdPartyActionInvocationResponse]] = None,
         ) -> None: ...
-    def ClearField(self, field_name: typing_extensions___Literal[u"httpResponse",b"httpResponse"]) -> None: ...
+    def ClearField(self, field_name: typing_extensions___Literal[u"http_response",b"http_response"]) -> None: ...
 type___HttpResponses = HttpResponses
 
 class Automation(google___protobuf___message___Message):
     DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
     title: typing___Text = ...
     status: type___AutomationStatusValue = ...
     entity_type: common_pb2___EntityTypeValue = ...
+    created_by_organization_user_id: typing___Text = ...
 
     @property
     def trigger(self) -> type___Trigger: ...
 
     @property
-    def automationAction(self) -> type___AutomationAction: ...
+    def automation_action(self) -> type___AutomationAction: ...
 
     def __init__(self,
         *,
         title : typing___Optional[typing___Text] = None,
         status : typing___Optional[type___AutomationStatusValue] = None,
         trigger : typing___Optional[type___Trigger] = None,
-        automationAction : typing___Optional[type___AutomationAction] = None,
+        automation_action : typing___Optional[type___AutomationAction] = None,
         entity_type : typing___Optional[common_pb2___EntityTypeValue] = None,
+        created_by_organization_user_id : typing___Optional[typing___Text] = None,
         ) -> None: ...
-    def HasField(self, field_name: typing_extensions___Literal[u"automationAction",b"automationAction",u"trigger",b"trigger"]) -> builtin___bool: ...
-    def ClearField(self, field_name: typing_extensions___Literal[u"automationAction",b"automationAction",u"entity_type",b"entity_type",u"status",b"status",u"title",b"title",u"trigger",b"trigger"]) -> None: ...
+    def HasField(self, field_name: typing_extensions___Literal[u"automation_action",b"automation_action",u"trigger",b"trigger"]) -> builtin___bool: ...
+    def ClearField(self, field_name: typing_extensions___Literal[u"automation_action",b"automation_action",u"created_by_organization_user_id",b"created_by_organization_user_id",u"entity_type",b"entity_type",u"status",b"status",u"title",b"title",u"trigger",b"trigger"]) -> None: ...
 type___Automation = Automation
```

### Comparing `calixa-proto-py-2.0.8/calixa_proto_py/automation_service.proto` & `calixa-proto-py-2.0.9/calixa_proto_py/automation_service.proto`

 * *Files identical despite different names*

### Comparing `calixa-proto-py-2.0.8/calixa_proto_py/automation_service_pb2.pyi` & `calixa-proto-py-2.0.9/calixa_proto_py/automation_service_pb2.pyi`

 * *Files 8% similar despite different names*

```diff
@@ -1,11 +1,9 @@
-"""
-@generated by mypy-protobuf.  Do not edit manually!
-isort:skip_file
-"""
+# @generated by generate_proto_mypy_stubs.py.  Do not edit!
+import sys
 from entity_pb2 import (
     Entity as entity_pb2___Entity,
 )
 
 from google.protobuf.descriptor import (
     Descriptor as google___protobuf___descriptor___Descriptor,
     FileDescriptor as google___protobuf___descriptor___FileDescriptor,
```

### Comparing `calixa-proto-py-2.0.8/calixa_proto_py/automation_service_pb2_grpc.py` & `calixa-proto-py-2.0.9/calixa_proto_py/automation_service_pb2_grpc.py`

 * *Files identical despite different names*

### Comparing `calixa-proto-py-2.0.8/calixa_proto_py/billing.proto` & `calixa-proto-py-2.0.9/calixa_proto_py/billing.proto`

 * *Files identical despite different names*

### Comparing `calixa-proto-py-2.0.8/calixa_proto_py/billing_pb2.pyi` & `calixa-proto-py-2.0.9/calixa_proto_py/billing_pb2.pyi`

 * *Files 1% similar despite different names*

```diff
@@ -1,11 +1,9 @@
-"""
-@generated by mypy-protobuf.  Do not edit manually!
-isort:skip_file
-"""
+# @generated by generate_proto_mypy_stubs.py.  Do not edit!
+import sys
 from common_pb2 import (
     Address as common_pb2___Address,
     Amount as common_pb2___Amount,
     ExternalId as common_pb2___ExternalId,
 )
 
 from google.protobuf.descriptor import (
@@ -71,40 +69,43 @@
 INCOMPLETE = typing___cast(SubscriptionStatusValue, 1)
 INCOMPLETE_EXPIRED = typing___cast(SubscriptionStatusValue, 2)
 TRIALING = typing___cast(SubscriptionStatusValue, 3)
 ACTIVE = typing___cast(SubscriptionStatusValue, 4)
 PAST_DUE = typing___cast(SubscriptionStatusValue, 5)
 CANCELED = typing___cast(SubscriptionStatusValue, 6)
 UNPAID = typing___cast(SubscriptionStatusValue, 7)
+type___SubscriptionStatus = SubscriptionStatus
 
 SubscriptionCollectionMethodValue = typing___NewType('SubscriptionCollectionMethodValue', builtin___int)
 type___SubscriptionCollectionMethodValue = SubscriptionCollectionMethodValue
 SubscriptionCollectionMethod: _SubscriptionCollectionMethod
 class _SubscriptionCollectionMethod(google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper[SubscriptionCollectionMethodValue]):
     DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
     SUBSCRIPTION_COLLECTION_METHOD_UNSPECIFIED = typing___cast(SubscriptionCollectionMethodValue, 0)
     SUBSCRIPTION_COLLECTION_METHOD_CHARGE_AUTOMATICALLY = typing___cast(SubscriptionCollectionMethodValue, 1)
     SUBSCRIPTION_COLLECTION_METHOD_SEND_INVOICE = typing___cast(SubscriptionCollectionMethodValue, 2)
 SUBSCRIPTION_COLLECTION_METHOD_UNSPECIFIED = typing___cast(SubscriptionCollectionMethodValue, 0)
 SUBSCRIPTION_COLLECTION_METHOD_CHARGE_AUTOMATICALLY = typing___cast(SubscriptionCollectionMethodValue, 1)
 SUBSCRIPTION_COLLECTION_METHOD_SEND_INVOICE = typing___cast(SubscriptionCollectionMethodValue, 2)
+type___SubscriptionCollectionMethod = SubscriptionCollectionMethod
 
 SubscriptionPauseCollectionBehaviorValue = typing___NewType('SubscriptionPauseCollectionBehaviorValue', builtin___int)
 type___SubscriptionPauseCollectionBehaviorValue = SubscriptionPauseCollectionBehaviorValue
 SubscriptionPauseCollectionBehavior: _SubscriptionPauseCollectionBehavior
 class _SubscriptionPauseCollectionBehavior(google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper[SubscriptionPauseCollectionBehaviorValue]):
     DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
     SUBSCRIPTION_PAUSE_COLLECTION_BEHAVIOR_UNSPECIFIED = typing___cast(SubscriptionPauseCollectionBehaviorValue, 0)
     SUBSCRIPTION_PAUSE_COLLECTION_BEHAVIOR_KEEP_AS_DRAFT = typing___cast(SubscriptionPauseCollectionBehaviorValue, 1)
     SUBSCRIPTION_PAUSE_COLLECTION_BEHAVIOR_MARK_UNCOLLECTIBLE = typing___cast(SubscriptionPauseCollectionBehaviorValue, 2)
     SUBSCRIPTION_PAUSE_COLLECTION_BEHAVIOR_BEHAVIOR_VOID = typing___cast(SubscriptionPauseCollectionBehaviorValue, 3)
 SUBSCRIPTION_PAUSE_COLLECTION_BEHAVIOR_UNSPECIFIED = typing___cast(SubscriptionPauseCollectionBehaviorValue, 0)
 SUBSCRIPTION_PAUSE_COLLECTION_BEHAVIOR_KEEP_AS_DRAFT = typing___cast(SubscriptionPauseCollectionBehaviorValue, 1)
 SUBSCRIPTION_PAUSE_COLLECTION_BEHAVIOR_MARK_UNCOLLECTIBLE = typing___cast(SubscriptionPauseCollectionBehaviorValue, 2)
 SUBSCRIPTION_PAUSE_COLLECTION_BEHAVIOR_BEHAVIOR_VOID = typing___cast(SubscriptionPauseCollectionBehaviorValue, 3)
+type___SubscriptionPauseCollectionBehavior = SubscriptionPauseCollectionBehavior
 
 InvoiceStatusValue = typing___NewType('InvoiceStatusValue', builtin___int)
 type___InvoiceStatusValue = InvoiceStatusValue
 InvoiceStatus: _InvoiceStatus
 class _InvoiceStatus(google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper[InvoiceStatusValue]):
     DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
     INVOICE_STATUS_UNSPECIFIED = typing___cast(InvoiceStatusValue, 0)
@@ -117,14 +118,15 @@
 INVOICE_STATUS_UNSPECIFIED = typing___cast(InvoiceStatusValue, 0)
 DRAFT = typing___cast(InvoiceStatusValue, 1)
 DELETED = typing___cast(InvoiceStatusValue, 2)
 OPEN = typing___cast(InvoiceStatusValue, 3)
 PAID = typing___cast(InvoiceStatusValue, 4)
 UNCOLLECTIBLE = typing___cast(InvoiceStatusValue, 5)
 VOID = typing___cast(InvoiceStatusValue, 6)
+type___InvoiceStatus = InvoiceStatus
 
 InvoiceFrequencyValue = typing___NewType('InvoiceFrequencyValue', builtin___int)
 type___InvoiceFrequencyValue = InvoiceFrequencyValue
 InvoiceFrequency: _InvoiceFrequency
 class _InvoiceFrequency(google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper[InvoiceFrequencyValue]):
     DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
     INVOICE_FREQUENCY_UNSPECIFIED = typing___cast(InvoiceFrequencyValue, 0)
@@ -133,24 +135,26 @@
     INVOICE_FREQUENCY_MONTH = typing___cast(InvoiceFrequencyValue, 3)
     INVOICE_FREQUENCY_YEAR = typing___cast(InvoiceFrequencyValue, 4)
 INVOICE_FREQUENCY_UNSPECIFIED = typing___cast(InvoiceFrequencyValue, 0)
 INVOICE_FREQUENCY_DAY = typing___cast(InvoiceFrequencyValue, 1)
 INVOICE_FREQUENCY_WEEK = typing___cast(InvoiceFrequencyValue, 2)
 INVOICE_FREQUENCY_MONTH = typing___cast(InvoiceFrequencyValue, 3)
 INVOICE_FREQUENCY_YEAR = typing___cast(InvoiceFrequencyValue, 4)
+type___InvoiceFrequency = InvoiceFrequency
 
 PaymentMethodTypeValue = typing___NewType('PaymentMethodTypeValue', builtin___int)
 type___PaymentMethodTypeValue = PaymentMethodTypeValue
 PaymentMethodType: _PaymentMethodType
 class _PaymentMethodType(google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper[PaymentMethodTypeValue]):
     DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
     PAYMENT_METHOD_TYPE_UNSPECIFIED = typing___cast(PaymentMethodTypeValue, 0)
     PAYMENT_METHOD_TYPE_CARD = typing___cast(PaymentMethodTypeValue, 1)
 PAYMENT_METHOD_TYPE_UNSPECIFIED = typing___cast(PaymentMethodTypeValue, 0)
 PAYMENT_METHOD_TYPE_CARD = typing___cast(PaymentMethodTypeValue, 1)
+type___PaymentMethodType = PaymentMethodType
 
 ChargeStatusValue = typing___NewType('ChargeStatusValue', builtin___int)
 type___ChargeStatusValue = ChargeStatusValue
 ChargeStatus: _ChargeStatus
 class _ChargeStatus(google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper[ChargeStatusValue]):
     DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
     CHARGE_STATUS_UNSPECIFIED = typing___cast(ChargeStatusValue, 0)
@@ -165,28 +169,30 @@
 CHARGE_STATUS_CREATED = typing___cast(ChargeStatusValue, 1)
 CHARGE_STATUS_EXPIRED = typing___cast(ChargeStatusValue, 2)
 CHARGE_STATUS_FAILED = typing___cast(ChargeStatusValue, 3)
 CHARGE_STATUS_PENDING = typing___cast(ChargeStatusValue, 4)
 CHARGE_STATUS_REFUNDED = typing___cast(ChargeStatusValue, 5)
 CHARGE_STATUS_PARTIALLY_REFUNDED = typing___cast(ChargeStatusValue, 6)
 CHARGE_STATUS_SUCCEEDED = typing___cast(ChargeStatusValue, 7)
+type___ChargeStatus = ChargeStatus
 
 ChargeRefundStatusValue = typing___NewType('ChargeRefundStatusValue', builtin___int)
 type___ChargeRefundStatusValue = ChargeRefundStatusValue
 ChargeRefundStatus: _ChargeRefundStatus
 class _ChargeRefundStatus(google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper[ChargeRefundStatusValue]):
     DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
     CHARGE_REFUND_STATUS_UNSPECIFIED = typing___cast(ChargeRefundStatusValue, 0)
     CHARGE_REFUND_STATUS_SUCCEEDED = typing___cast(ChargeRefundStatusValue, 1)
     CHARGE_REFUND_STATUS_FAILED = typing___cast(ChargeRefundStatusValue, 2)
     CHARGE_REFUND_STATUS_PENDING = typing___cast(ChargeRefundStatusValue, 3)
 CHARGE_REFUND_STATUS_UNSPECIFIED = typing___cast(ChargeRefundStatusValue, 0)
 CHARGE_REFUND_STATUS_SUCCEEDED = typing___cast(ChargeRefundStatusValue, 1)
 CHARGE_REFUND_STATUS_FAILED = typing___cast(ChargeRefundStatusValue, 2)
 CHARGE_REFUND_STATUS_PENDING = typing___cast(ChargeRefundStatusValue, 3)
+type___ChargeRefundStatus = ChargeRefundStatus
 
 class Product(google___protobuf___message___Message):
     DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
     active: builtin___bool = ...
     name: typing___Text = ...
     description: typing___Text = ...
     type: typing___Text = ...
```

### Comparing `calixa-proto-py-2.0.8/calixa_proto_py/collaboration.proto` & `calixa-proto-py-2.0.9/calixa_proto_py/collaboration.proto`

 * *Files identical despite different names*

### Comparing `calixa-proto-py-2.0.8/calixa_proto_py/collaboration_entity.proto` & `calixa-proto-py-2.0.9/calixa_proto_py/collaboration_entity.proto`

 * *Files identical despite different names*

### Comparing `calixa-proto-py-2.0.8/calixa_proto_py/collaboration_entity_pb2.pyi` & `calixa-proto-py-2.0.9/calixa_proto_py/collaboration_entity_pb2.pyi`

 * *Files 4% similar despite different names*

```diff
@@ -1,11 +1,9 @@
-"""
-@generated by mypy-protobuf.  Do not edit manually!
-isort:skip_file
-"""
+# @generated by generate_proto_mypy_stubs.py.  Do not edit!
+import sys
 from common_pb2 import (
     EntityTypeValue as common_pb2___EntityTypeValue,
 )
 
 from google.protobuf.descriptor import (
     Descriptor as google___protobuf___descriptor___Descriptor,
     EnumDescriptor as google___protobuf___descriptor___EnumDescriptor,
@@ -56,38 +54,41 @@
     DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
     PINNED_STATE_UNSPECIFIED = typing___cast(PinnedStateValue, 0)
     PINNED = typing___cast(PinnedStateValue, 1)
     UNPINNED = typing___cast(PinnedStateValue, 2)
 PINNED_STATE_UNSPECIFIED = typing___cast(PinnedStateValue, 0)
 PINNED = typing___cast(PinnedStateValue, 1)
 UNPINNED = typing___cast(PinnedStateValue, 2)
+type___PinnedState = PinnedState
 
 ResolvedStateValue = typing___NewType('ResolvedStateValue', builtin___int)
 type___ResolvedStateValue = ResolvedStateValue
 ResolvedState: _ResolvedState
 class _ResolvedState(google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper[ResolvedStateValue]):
     DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
     RESOLVED_STATE_UNSPECIFIED = typing___cast(ResolvedStateValue, 0)
     RESOLVED = typing___cast(ResolvedStateValue, 1)
     UNRESOLVED = typing___cast(ResolvedStateValue, 2)
 RESOLVED_STATE_UNSPECIFIED = typing___cast(ResolvedStateValue, 0)
 RESOLVED = typing___cast(ResolvedStateValue, 1)
 UNRESOLVED = typing___cast(ResolvedStateValue, 2)
+type___ResolvedState = ResolvedState
 
 ReadStateValue = typing___NewType('ReadStateValue', builtin___int)
 type___ReadStateValue = ReadStateValue
 ReadState: _ReadState
 class _ReadState(google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper[ReadStateValue]):
     DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
     READ_STATE_UNSPECIFIED = typing___cast(ReadStateValue, 0)
     READ = typing___cast(ReadStateValue, 1)
     UNREAD = typing___cast(ReadStateValue, 2)
 READ_STATE_UNSPECIFIED = typing___cast(ReadStateValue, 0)
 READ = typing___cast(ReadStateValue, 1)
 UNREAD = typing___cast(ReadStateValue, 2)
+type___ReadState = ReadState
 
 class Message(google___protobuf___message___Message):
     DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
     message_id: typing___Text = ...
     thread_id: typing___Text = ...
     body: typing___Text = ...
     author_id: typing___Text = ...
```

### Comparing `calixa-proto-py-2.0.8/calixa_proto_py/collaboration_pb2.pyi` & `calixa-proto-py-2.0.9/calixa_proto_py/collaboration_pb2.pyi`

 * *Files 2% similar despite different names*

```diff
@@ -1,11 +1,9 @@
-"""
-@generated by mypy-protobuf.  Do not edit manually!
-isort:skip_file
-"""
+# @generated by generate_proto_mypy_stubs.py.  Do not edit!
+import sys
 from common_pb2 import (
     EntityTypeValue as common_pb2___EntityTypeValue,
 )
 
 from entity_pb2 import (
     Entity as entity_pb2___Entity,
 )
```

### Comparing `calixa-proto-py-2.0.8/calixa_proto_py/collaboration_pb2_grpc.py` & `calixa-proto-py-2.0.9/calixa_proto_py/collaboration_pb2_grpc.py`

 * *Files identical despite different names*

### Comparing `calixa-proto-py-2.0.8/calixa_proto_py/common.proto` & `calixa-proto-py-2.0.9/calixa_proto_py/common.proto`

 * *Files identical despite different names*

### Comparing `calixa-proto-py-2.0.8/calixa_proto_py/common_pb2.pyi` & `calixa-proto-py-2.0.9/calixa_proto_py/common_pb2.pyi`

 * *Files 1% similar despite different names*

```diff
@@ -1,11 +1,9 @@
-"""
-@generated by mypy-protobuf.  Do not edit manually!
-isort:skip_file
-"""
+# @generated by generate_proto_mypy_stubs.py.  Do not edit!
+import sys
 from google.protobuf.descriptor import (
     Descriptor as google___protobuf___descriptor___Descriptor,
     EnumDescriptor as google___protobuf___descriptor___EnumDescriptor,
     FileDescriptor as google___protobuf___descriptor___FileDescriptor,
 )
 
 from google.protobuf.internal.enum_type_wrapper import (
@@ -55,14 +53,15 @@
     EXTERNAL_ID_TYPE_PRIMARY = typing___cast(ExternalIdTypeValue, 1)
     EXTERNAL_ID_TYPE_RELATIONSHIP = typing___cast(ExternalIdTypeValue, 2)
     EXTERNAL_ID_TYPE_EMAIL = typing___cast(ExternalIdTypeValue, 3)
 EXTERNAL_ID_TYPE_UNSPECIFIED = typing___cast(ExternalIdTypeValue, 0)
 EXTERNAL_ID_TYPE_PRIMARY = typing___cast(ExternalIdTypeValue, 1)
 EXTERNAL_ID_TYPE_RELATIONSHIP = typing___cast(ExternalIdTypeValue, 2)
 EXTERNAL_ID_TYPE_EMAIL = typing___cast(ExternalIdTypeValue, 3)
+type___ExternalIdType = ExternalIdType
 
 EntityTypeValue = typing___NewType('EntityTypeValue', builtin___int)
 type___EntityTypeValue = EntityTypeValue
 EntityType: _EntityType
 class _EntityType(google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper[EntityTypeValue]):
     DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
     ENTITY_TYPE_UNSPECIFIED = typing___cast(EntityTypeValue, 0)
@@ -175,28 +174,30 @@
 OUTREACH_SEQUENCE = typing___cast(EntityTypeValue, 2024)
 OUTREACH_SEQUENCE_STATE = typing___cast(EntityTypeValue, 2025)
 CLEARBIT_PERSON = typing___cast(EntityTypeValue, 2026)
 CLEARBIT_COMPANY = typing___cast(EntityTypeValue, 2027)
 SALESFORCE_CUSTOM_PROPERTY = typing___cast(EntityTypeValue, 2028)
 SALESFORCE_CUSTOM_PROPERTY_DEFINITION = typing___cast(EntityTypeValue, 2029)
 DATA_WAREHOUSE_SYNC = typing___cast(EntityTypeValue, 3000)
+type___EntityType = EntityType
 
 ServingStatusValue = typing___NewType('ServingStatusValue', builtin___int)
 type___ServingStatusValue = ServingStatusValue
 ServingStatus: _ServingStatus
 class _ServingStatus(google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper[ServingStatusValue]):
     DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
     UNKNOWN = typing___cast(ServingStatusValue, 0)
     SERVING = typing___cast(ServingStatusValue, 1)
     NOT_SERVING = typing___cast(ServingStatusValue, 2)
     SERVICE_UNKNOWN = typing___cast(ServingStatusValue, 3)
 UNKNOWN = typing___cast(ServingStatusValue, 0)
 SERVING = typing___cast(ServingStatusValue, 1)
 NOT_SERVING = typing___cast(ServingStatusValue, 2)
 SERVICE_UNKNOWN = typing___cast(ServingStatusValue, 3)
+type___ServingStatus = ServingStatus
 
 TaskStatusValue = typing___NewType('TaskStatusValue', builtin___int)
 type___TaskStatusValue = TaskStatusValue
 TaskStatus: _TaskStatus
 class _TaskStatus(google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper[TaskStatusValue]):
     DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
     TASK_STATUS_UNDEFINED = typing___cast(TaskStatusValue, 0)
@@ -207,14 +208,15 @@
     TASK_STATUS_TIMED_OUT = typing___cast(TaskStatusValue, 5)
 TASK_STATUS_UNDEFINED = typing___cast(TaskStatusValue, 0)
 TASK_STATUS_PENDING = typing___cast(TaskStatusValue, 1)
 TASK_STATUS_STARTED = typing___cast(TaskStatusValue, 2)
 TASK_STATUS_DONE = typing___cast(TaskStatusValue, 3)
 TASK_STATUS_ERROR = typing___cast(TaskStatusValue, 4)
 TASK_STATUS_TIMED_OUT = typing___cast(TaskStatusValue, 5)
+type___TaskStatus = TaskStatus
 
 class Amount(google___protobuf___message___Message):
     DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
     micros: builtin___int = ...
     currency: typing___Text = ...
 
     def __init__(self,
```

### Comparing `calixa-proto-py-2.0.8/calixa_proto_py/common_pb2_grpc.py` & `calixa-proto-py-2.0.9/calixa_proto_py/common_pb2_grpc.py`

 * *Files identical despite different names*

### Comparing `calixa-proto-py-2.0.8/calixa_proto_py/condition.proto` & `calixa-proto-py-2.0.9/calixa_proto_py/condition.proto`

 * *Files 13% similar despite different names*

```diff
@@ -2,14 +2,15 @@
 
 import "google/protobuf/timestamp.proto";
 import "google/protobuf/struct.proto";
 import "google/protobuf/field_mask.proto";
 import "google/protobuf/empty.proto";
 
 import "common.proto";
+import "learning.proto";
 
 option java_package = "io.calixa.domain.condition";
 option java_multiple_files = true;
 option optimize_for = SPEED;
 
 package calixa.domain.condition;
 
@@ -84,15 +85,15 @@
   // To mirror what is surfaced through the ConditionJson endpoint, the front-end
   // now sends the specific type on which the field is set. This is somewhat
   // redundant as "field = account.domain_name" and "entity_type = 'account'",
   // but we're fine with this.
   calixa.domain.common.EntityType entity_type = 10;
 }
 
-message MetricThresholdCondition {
+message MetricCondition {
   // this is counter key, metric id
   string metric_descriptor_id = 1;
   // only few operators are supported for metric conditions
   FieldOperatorType operator = 2;
   repeated ConditionValue values = 3 ;
 
   oneof metric_range {
@@ -101,43 +102,36 @@
   }
 
   // TODO(freds): Add validations to these once we update TrendSearch to also
   // use the following fields.
   string time_zone = 10;
   calixa.domain.common.EntityType entity_type = 11;
 
-  string type = 12; // The type of field for the Condition used to set
-                    // the condition value. Only used by Console; GrossHack
+  string type = 12 [deprecated = true]; // The type of field for the Condition used to set
+  // the condition value. Only used by Console; GrossHack
 
   // used to express filters on metrics' properties: https://www.notion.so/Metric-Subproperties-API-72e68e9d5d7d496891f32b339a497518#16e7491a04e142e885ce26541e0a0b29
   ConditionOrGroup conditions = 13;
+  MetricConditionType metric_condition_type = 14;
+}
+
+enum MetricConditionType {
+  METRIC_CONDITION_TYPE_UNSPECIFIED = 0;
+  METRIC_CONDITION_TYPE_THRESHOLD = 1;
+  METRIC_CONDITION_TYPE_PERCENTAGE_CHANGE = 2;
 }
 
 enum ComparedToRangeType {
   COMPARE_TO_RANGE_TYPE_NOT_SPECIFIED = 0;
   COMPARE_TO_RANGE_TYPE_PREVIOUS_PERIOD = 1;
   COMPARE_TO_RANGE_TYPE_PREVIOUS_MONTH = 2;
   COMPARE_TO_RANGE_TYPE_PREVIOUS_QUARTER = 3;
   COMPARE_TO_RANGE_TYPE_PREVIOUS_YEAR = 4;
 }
 
-message MetricChangeCondition {
-  // this is counter key, metric id
-  string metric_descriptor_id = 1;
-  // only few operators are supported for metric conditions
-  FieldOperatorType operator = 2;
-  double change_percentage = 3;
-
-  RelativeTimeRange current_time_range = 4;
-  ComparedToRangeType compared_to_range_type = 5;
-
-  string time_zone = 10;
-  calixa.domain.common.EntityType entity_type = 11;
-}
-
 message Journey {
   string id = 1;
   string name = 2;
   common.EntityType entity_type = 3;
   // the index into the array determines the priority of the milestone
   repeated JourneyMilestone milestones = 4;
   google.protobuf.Timestamp definition_updated_at = 5;
@@ -184,22 +178,37 @@
   FieldOperatorType operator = 2;
 
   // These values will correspond to the jm_ ids or "None"
   // journey milestones are disjuncted (ORed together)
   repeated string values = 3;
 }
 
+message PredictionTaskCondition {
+  string prediction_id = 100;
+  calixa.domain.learning.PredictionTask prediction_task = 1;
+  FieldOperatorType operator = 2; //;
+
+  repeated ConditionValue values = 3;
+}
+
+// Used for querying a detailed account rollup view:
+message AccountsRollupCondition {
+  string field = 1;
+  repeated ConditionValue values = 2;
+}
+
 message ConditionOrGroup {
   oneof conditionOrGroup {
     Condition condition = 1;
     ConditionGroup group = 2;
-    MetricThresholdCondition metric_threshold_condition = 3;
-    MetricChangeCondition metric_change_condition = 4;
+    MetricCondition metric_condition = 3;
+    AccountsRollupCondition accounts_rollup_condition = 4;
     ScoringFunctionCondition scoring_function_condition = 5;
     JourneyMilestoneCondition journey_milestone_condition = 6;
+    PredictionTaskCondition prediction_task_condition = 7;
   }
 }
 
 enum LogicOperatorType {
   LOGIC_OPERATOR_TYPE_UNSPECIFIED = 0;
   LOGIC_OPERATOR_TYPE_AND = 1;
   LOGIC_OPERATOR_TYPE_OR = 2;
```

### Comparing `calixa-proto-py-2.0.8/calixa_proto_py/condition_pb2.pyi` & `calixa-proto-py-2.0.9/calixa_proto_py/condition_pb2.pyi`

 * *Files 4% similar despite different names*

```diff
@@ -1,11 +1,9 @@
-"""
-@generated by mypy-protobuf.  Do not edit manually!
-isort:skip_file
-"""
+# @generated by generate_proto_mypy_stubs.py.  Do not edit!
+import sys
 from common_pb2 import (
     EntityTypeValue as common_pb2___EntityTypeValue,
 )
 
 from google.protobuf.descriptor import (
     Descriptor as google___protobuf___descriptor___Descriptor,
     EnumDescriptor as google___protobuf___descriptor___EnumDescriptor,
@@ -25,14 +23,18 @@
     Message as google___protobuf___message___Message,
 )
 
 from google.protobuf.timestamp_pb2 import (
     Timestamp as google___protobuf___timestamp_pb2___Timestamp,
 )
 
+from learning_pb2 import (
+    PredictionTaskValue as learning_pb2___PredictionTaskValue,
+)
+
 from typing import (
     Iterable as typing___Iterable,
     NewType as typing___NewType,
     Optional as typing___Optional,
     Text as typing___Text,
     cast as typing___cast,
 )
@@ -61,14 +63,15 @@
     CONDITION_FIELD_TYPE_MONEY = typing___cast(ConditionFieldTypeValue, 3)
     CONDITION_FIELD_TYPE_ENUM = typing___cast(ConditionFieldTypeValue, 4)
 CONDITION_FIELD_TYPE_UNSPECIFIED = typing___cast(ConditionFieldTypeValue, 0)
 CONDITION_FIELD_TYPE_STRING = typing___cast(ConditionFieldTypeValue, 1)
 CONDITION_FIELD_TYPE_INTEGER = typing___cast(ConditionFieldTypeValue, 2)
 CONDITION_FIELD_TYPE_MONEY = typing___cast(ConditionFieldTypeValue, 3)
 CONDITION_FIELD_TYPE_ENUM = typing___cast(ConditionFieldTypeValue, 4)
+type___ConditionFieldType = ConditionFieldType
 
 RelativeTimeRangeValue = typing___NewType('RelativeTimeRangeValue', builtin___int)
 type___RelativeTimeRangeValue = RelativeTimeRangeValue
 RelativeTimeRange: _RelativeTimeRange
 class _RelativeTimeRange(google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper[RelativeTimeRangeValue]):
     DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
     RELATIVE_TIME_RANGE_UNSPECIFIED = typing___cast(RelativeTimeRangeValue, 0)
@@ -85,14 +88,15 @@
 RELATIVE_TIME_RANGE_YESTERDAY = typing___cast(RelativeTimeRangeValue, 2)
 RELATIVE_TIME_RANGE_LAST_7_DAYS = typing___cast(RelativeTimeRangeValue, 3)
 RELATIVE_TIME_RANGE_LAST_30_DAYS = typing___cast(RelativeTimeRangeValue, 4)
 RELATIVE_TIME_RANGE_LAST_90_DAYS = typing___cast(RelativeTimeRangeValue, 5)
 RELATIVE_TIME_RANGE_LAST_365_DAYS = typing___cast(RelativeTimeRangeValue, 6)
 RELATIVE_TIME_RANGE_ALL_TIME = typing___cast(RelativeTimeRangeValue, 7)
 RELATIVE_TIME_RANGE_LAST_180_DAYS = typing___cast(RelativeTimeRangeValue, 8)
+type___RelativeTimeRange = RelativeTimeRange
 
 FieldOperatorTypeValue = typing___NewType('FieldOperatorTypeValue', builtin___int)
 type___FieldOperatorTypeValue = FieldOperatorTypeValue
 FieldOperatorType: _FieldOperatorType
 class _FieldOperatorType(google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper[FieldOperatorTypeValue]):
     DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
     FIELD_OPERATOR_TYPE_UNSPECIFIED = typing___cast(FieldOperatorTypeValue, 0)
@@ -125,14 +129,28 @@
 FIELD_OPERATOR_TYPE_CONTAINS = typing___cast(FieldOperatorTypeValue, 10)
 FIELD_OPERATOR_TYPE_ISNOT = typing___cast(FieldOperatorTypeValue, 11)
 FIELD_OPERATOR_TYPE_NOTCONTAIN = typing___cast(FieldOperatorTypeValue, 12)
 FIELD_OPERATOR_TYPE_BEFORE = typing___cast(FieldOperatorTypeValue, 13)
 FIELD_OPERATOR_TYPE_IS_SET = typing___cast(FieldOperatorTypeValue, 14)
 FIELD_OPERATOR_TYPE_IS_NOT_SET = typing___cast(FieldOperatorTypeValue, 15)
 FIELD_OPERATOR_TYPE_BIDIRECTIONAL_WITHIN = typing___cast(FieldOperatorTypeValue, 16)
+type___FieldOperatorType = FieldOperatorType
+
+MetricConditionTypeValue = typing___NewType('MetricConditionTypeValue', builtin___int)
+type___MetricConditionTypeValue = MetricConditionTypeValue
+MetricConditionType: _MetricConditionType
+class _MetricConditionType(google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper[MetricConditionTypeValue]):
+    DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
+    METRIC_CONDITION_TYPE_UNSPECIFIED = typing___cast(MetricConditionTypeValue, 0)
+    METRIC_CONDITION_TYPE_THRESHOLD = typing___cast(MetricConditionTypeValue, 1)
+    METRIC_CONDITION_TYPE_PERCENTAGE_CHANGE = typing___cast(MetricConditionTypeValue, 2)
+METRIC_CONDITION_TYPE_UNSPECIFIED = typing___cast(MetricConditionTypeValue, 0)
+METRIC_CONDITION_TYPE_THRESHOLD = typing___cast(MetricConditionTypeValue, 1)
+METRIC_CONDITION_TYPE_PERCENTAGE_CHANGE = typing___cast(MetricConditionTypeValue, 2)
+type___MetricConditionType = MetricConditionType
 
 ComparedToRangeTypeValue = typing___NewType('ComparedToRangeTypeValue', builtin___int)
 type___ComparedToRangeTypeValue = ComparedToRangeTypeValue
 ComparedToRangeType: _ComparedToRangeType
 class _ComparedToRangeType(google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper[ComparedToRangeTypeValue]):
     DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
     COMPARE_TO_RANGE_TYPE_NOT_SPECIFIED = typing___cast(ComparedToRangeTypeValue, 0)
@@ -141,26 +159,28 @@
     COMPARE_TO_RANGE_TYPE_PREVIOUS_QUARTER = typing___cast(ComparedToRangeTypeValue, 3)
     COMPARE_TO_RANGE_TYPE_PREVIOUS_YEAR = typing___cast(ComparedToRangeTypeValue, 4)
 COMPARE_TO_RANGE_TYPE_NOT_SPECIFIED = typing___cast(ComparedToRangeTypeValue, 0)
 COMPARE_TO_RANGE_TYPE_PREVIOUS_PERIOD = typing___cast(ComparedToRangeTypeValue, 1)
 COMPARE_TO_RANGE_TYPE_PREVIOUS_MONTH = typing___cast(ComparedToRangeTypeValue, 2)
 COMPARE_TO_RANGE_TYPE_PREVIOUS_QUARTER = typing___cast(ComparedToRangeTypeValue, 3)
 COMPARE_TO_RANGE_TYPE_PREVIOUS_YEAR = typing___cast(ComparedToRangeTypeValue, 4)
+type___ComparedToRangeType = ComparedToRangeType
 
 LogicOperatorTypeValue = typing___NewType('LogicOperatorTypeValue', builtin___int)
 type___LogicOperatorTypeValue = LogicOperatorTypeValue
 LogicOperatorType: _LogicOperatorType
 class _LogicOperatorType(google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper[LogicOperatorTypeValue]):
     DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
     LOGIC_OPERATOR_TYPE_UNSPECIFIED = typing___cast(LogicOperatorTypeValue, 0)
     LOGIC_OPERATOR_TYPE_AND = typing___cast(LogicOperatorTypeValue, 1)
     LOGIC_OPERATOR_TYPE_OR = typing___cast(LogicOperatorTypeValue, 2)
 LOGIC_OPERATOR_TYPE_UNSPECIFIED = typing___cast(LogicOperatorTypeValue, 0)
 LOGIC_OPERATOR_TYPE_AND = typing___cast(LogicOperatorTypeValue, 1)
 LOGIC_OPERATOR_TYPE_OR = typing___cast(LogicOperatorTypeValue, 2)
+type___LogicOperatorType = LogicOperatorType
 
 class AbsoluteTimeRange(google___protobuf___message___Message):
     DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
 
     @property
     def to(self) -> google___protobuf___timestamp_pb2___Timestamp: ...
 
@@ -208,22 +228,23 @@
         operator : typing___Optional[type___FieldOperatorTypeValue] = None,
         values : typing___Optional[typing___Iterable[type___ConditionValue]] = None,
         entity_type : typing___Optional[common_pb2___EntityTypeValue] = None,
         ) -> None: ...
     def ClearField(self, field_name: typing_extensions___Literal[u"entity_type",b"entity_type",u"field",b"field",u"operator",b"operator",u"type",b"type",u"values",b"values"]) -> None: ...
 type___Condition = Condition
 
-class MetricThresholdCondition(google___protobuf___message___Message):
+class MetricCondition(google___protobuf___message___Message):
     DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
     metric_descriptor_id: typing___Text = ...
     operator: type___FieldOperatorTypeValue = ...
     relative_time_range: type___RelativeTimeRangeValue = ...
     time_zone: typing___Text = ...
     entity_type: common_pb2___EntityTypeValue = ...
     type: typing___Text = ...
+    metric_condition_type: type___MetricConditionTypeValue = ...
 
     @property
     def values(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[type___ConditionValue]: ...
 
     @property
     def absolute_time_range(self) -> type___AbsoluteTimeRange: ...
 
@@ -237,42 +258,20 @@
         values : typing___Optional[typing___Iterable[type___ConditionValue]] = None,
         relative_time_range : typing___Optional[type___RelativeTimeRangeValue] = None,
         absolute_time_range : typing___Optional[type___AbsoluteTimeRange] = None,
         time_zone : typing___Optional[typing___Text] = None,
         entity_type : typing___Optional[common_pb2___EntityTypeValue] = None,
         type : typing___Optional[typing___Text] = None,
         conditions : typing___Optional[type___ConditionOrGroup] = None,
+        metric_condition_type : typing___Optional[type___MetricConditionTypeValue] = None,
         ) -> None: ...
     def HasField(self, field_name: typing_extensions___Literal[u"absolute_time_range",b"absolute_time_range",u"conditions",b"conditions",u"metric_range",b"metric_range",u"relative_time_range",b"relative_time_range"]) -> builtin___bool: ...
-    def ClearField(self, field_name: typing_extensions___Literal[u"absolute_time_range",b"absolute_time_range",u"conditions",b"conditions",u"entity_type",b"entity_type",u"metric_descriptor_id",b"metric_descriptor_id",u"metric_range",b"metric_range",u"operator",b"operator",u"relative_time_range",b"relative_time_range",u"time_zone",b"time_zone",u"type",b"type",u"values",b"values"]) -> None: ...
+    def ClearField(self, field_name: typing_extensions___Literal[u"absolute_time_range",b"absolute_time_range",u"conditions",b"conditions",u"entity_type",b"entity_type",u"metric_condition_type",b"metric_condition_type",u"metric_descriptor_id",b"metric_descriptor_id",u"metric_range",b"metric_range",u"operator",b"operator",u"relative_time_range",b"relative_time_range",u"time_zone",b"time_zone",u"type",b"type",u"values",b"values"]) -> None: ...
     def WhichOneof(self, oneof_group: typing_extensions___Literal[u"metric_range",b"metric_range"]) -> typing_extensions___Literal["relative_time_range","absolute_time_range"]: ...
-type___MetricThresholdCondition = MetricThresholdCondition
-
-class MetricChangeCondition(google___protobuf___message___Message):
-    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
-    metric_descriptor_id: typing___Text = ...
-    operator: type___FieldOperatorTypeValue = ...
-    change_percentage: builtin___float = ...
-    current_time_range: type___RelativeTimeRangeValue = ...
-    compared_to_range_type: type___ComparedToRangeTypeValue = ...
-    time_zone: typing___Text = ...
-    entity_type: common_pb2___EntityTypeValue = ...
-
-    def __init__(self,
-        *,
-        metric_descriptor_id : typing___Optional[typing___Text] = None,
-        operator : typing___Optional[type___FieldOperatorTypeValue] = None,
-        change_percentage : typing___Optional[builtin___float] = None,
-        current_time_range : typing___Optional[type___RelativeTimeRangeValue] = None,
-        compared_to_range_type : typing___Optional[type___ComparedToRangeTypeValue] = None,
-        time_zone : typing___Optional[typing___Text] = None,
-        entity_type : typing___Optional[common_pb2___EntityTypeValue] = None,
-        ) -> None: ...
-    def ClearField(self, field_name: typing_extensions___Literal[u"change_percentage",b"change_percentage",u"compared_to_range_type",b"compared_to_range_type",u"current_time_range",b"current_time_range",u"entity_type",b"entity_type",u"metric_descriptor_id",b"metric_descriptor_id",u"operator",b"operator",u"time_zone",b"time_zone"]) -> None: ...
-type___MetricChangeCondition = MetricChangeCondition
+type___MetricCondition = MetricCondition
 
 class Journey(google___protobuf___message___Message):
     DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
     id: typing___Text = ...
     name: typing___Text = ...
     entity_type: common_pb2___EntityTypeValue = ...
 
@@ -386,47 +385,85 @@
         journey_id : typing___Optional[typing___Text] = None,
         operator : typing___Optional[type___FieldOperatorTypeValue] = None,
         values : typing___Optional[typing___Iterable[typing___Text]] = None,
         ) -> None: ...
     def ClearField(self, field_name: typing_extensions___Literal[u"journey_id",b"journey_id",u"operator",b"operator",u"values",b"values"]) -> None: ...
 type___JourneyMilestoneCondition = JourneyMilestoneCondition
 
+class PredictionTaskCondition(google___protobuf___message___Message):
+    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
+    prediction_id: typing___Text = ...
+    prediction_task: learning_pb2___PredictionTaskValue = ...
+    operator: type___FieldOperatorTypeValue = ...
+
+    @property
+    def values(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[type___ConditionValue]: ...
+
+    def __init__(self,
+        *,
+        prediction_id : typing___Optional[typing___Text] = None,
+        prediction_task : typing___Optional[learning_pb2___PredictionTaskValue] = None,
+        operator : typing___Optional[type___FieldOperatorTypeValue] = None,
+        values : typing___Optional[typing___Iterable[type___ConditionValue]] = None,
+        ) -> None: ...
+    def ClearField(self, field_name: typing_extensions___Literal[u"operator",b"operator",u"prediction_id",b"prediction_id",u"prediction_task",b"prediction_task",u"values",b"values"]) -> None: ...
+type___PredictionTaskCondition = PredictionTaskCondition
+
+class AccountsRollupCondition(google___protobuf___message___Message):
+    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
+    field: typing___Text = ...
+
+    @property
+    def values(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[type___ConditionValue]: ...
+
+    def __init__(self,
+        *,
+        field : typing___Optional[typing___Text] = None,
+        values : typing___Optional[typing___Iterable[type___ConditionValue]] = None,
+        ) -> None: ...
+    def ClearField(self, field_name: typing_extensions___Literal[u"field",b"field",u"values",b"values"]) -> None: ...
+type___AccountsRollupCondition = AccountsRollupCondition
+
 class ConditionOrGroup(google___protobuf___message___Message):
     DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
 
     @property
     def condition(self) -> type___Condition: ...
 
     @property
     def group(self) -> type___ConditionGroup: ...
 
     @property
-    def metric_threshold_condition(self) -> type___MetricThresholdCondition: ...
+    def metric_condition(self) -> type___MetricCondition: ...
 
     @property
-    def metric_change_condition(self) -> type___MetricChangeCondition: ...
+    def accounts_rollup_condition(self) -> type___AccountsRollupCondition: ...
 
     @property
     def scoring_function_condition(self) -> type___ScoringFunctionCondition: ...
 
     @property
     def journey_milestone_condition(self) -> type___JourneyMilestoneCondition: ...
 
+    @property
+    def prediction_task_condition(self) -> type___PredictionTaskCondition: ...
+
     def __init__(self,
         *,
         condition : typing___Optional[type___Condition] = None,
         group : typing___Optional[type___ConditionGroup] = None,
-        metric_threshold_condition : typing___Optional[type___MetricThresholdCondition] = None,
-        metric_change_condition : typing___Optional[type___MetricChangeCondition] = None,
+        metric_condition : typing___Optional[type___MetricCondition] = None,
+        accounts_rollup_condition : typing___Optional[type___AccountsRollupCondition] = None,
         scoring_function_condition : typing___Optional[type___ScoringFunctionCondition] = None,
         journey_milestone_condition : typing___Optional[type___JourneyMilestoneCondition] = None,
+        prediction_task_condition : typing___Optional[type___PredictionTaskCondition] = None,
         ) -> None: ...
-    def HasField(self, field_name: typing_extensions___Literal[u"condition",b"condition",u"conditionOrGroup",b"conditionOrGroup",u"group",b"group",u"journey_milestone_condition",b"journey_milestone_condition",u"metric_change_condition",b"metric_change_condition",u"metric_threshold_condition",b"metric_threshold_condition",u"scoring_function_condition",b"scoring_function_condition"]) -> builtin___bool: ...
-    def ClearField(self, field_name: typing_extensions___Literal[u"condition",b"condition",u"conditionOrGroup",b"conditionOrGroup",u"group",b"group",u"journey_milestone_condition",b"journey_milestone_condition",u"metric_change_condition",b"metric_change_condition",u"metric_threshold_condition",b"metric_threshold_condition",u"scoring_function_condition",b"scoring_function_condition"]) -> None: ...
-    def WhichOneof(self, oneof_group: typing_extensions___Literal[u"conditionOrGroup",b"conditionOrGroup"]) -> typing_extensions___Literal["condition","group","metric_threshold_condition","metric_change_condition","scoring_function_condition","journey_milestone_condition"]: ...
+    def HasField(self, field_name: typing_extensions___Literal[u"accounts_rollup_condition",b"accounts_rollup_condition",u"condition",b"condition",u"conditionOrGroup",b"conditionOrGroup",u"group",b"group",u"journey_milestone_condition",b"journey_milestone_condition",u"metric_condition",b"metric_condition",u"prediction_task_condition",b"prediction_task_condition",u"scoring_function_condition",b"scoring_function_condition"]) -> builtin___bool: ...
+    def ClearField(self, field_name: typing_extensions___Literal[u"accounts_rollup_condition",b"accounts_rollup_condition",u"condition",b"condition",u"conditionOrGroup",b"conditionOrGroup",u"group",b"group",u"journey_milestone_condition",b"journey_milestone_condition",u"metric_condition",b"metric_condition",u"prediction_task_condition",b"prediction_task_condition",u"scoring_function_condition",b"scoring_function_condition"]) -> None: ...
+    def WhichOneof(self, oneof_group: typing_extensions___Literal[u"conditionOrGroup",b"conditionOrGroup"]) -> typing_extensions___Literal["condition","group","metric_condition","accounts_rollup_condition","scoring_function_condition","journey_milestone_condition","prediction_task_condition"]: ...
 type___ConditionOrGroup = ConditionOrGroup
 
 class ConditionGroup(google___protobuf___message___Message):
     DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
     logic_operator: type___LogicOperatorTypeValue = ...
 
     @property
```

### Comparing `calixa-proto-py-2.0.8/calixa_proto_py/console_string.proto` & `calixa-proto-py-2.0.9/calixa_proto_py/console_string.proto`

 * *Files identical despite different names*

### Comparing `calixa-proto-py-2.0.8/calixa_proto_py/console_string_pb2.pyi` & `calixa-proto-py-2.0.9/calixa_proto_py/console_string_pb2.pyi`

 * *Files 16% similar despite different names*

```diff
@@ -1,31 +1,26 @@
-"""
-@generated by mypy-protobuf.  Do not edit manually!
-isort:skip_file
-"""
+# @generated by generate_proto_mypy_stubs.py.  Do not edit!
+import sys
 from google.protobuf.descriptor import (
     Descriptor as google___protobuf___descriptor___Descriptor,
     EnumDescriptor as google___protobuf___descriptor___EnumDescriptor,
     FileDescriptor as google___protobuf___descriptor___FileDescriptor,
 )
 
-from google.protobuf.internal.containers import (
-    ScalarMap as google___protobuf___internal___containers___ScalarMap,
-)
-
 from google.protobuf.internal.enum_type_wrapper import (
     _EnumTypeWrapper as google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper,
 )
 
 from google.protobuf.message import (
     Message as google___protobuf___message___Message,
 )
 
 from typing import (
     Mapping as typing___Mapping,
+    MutableMapping as typing___MutableMapping,
     NewType as typing___NewType,
     Optional as typing___Optional,
     Text as typing___Text,
     cast as typing___cast,
 )
 
 from typing_extensions import (
@@ -48,14 +43,15 @@
     DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
     CONSOLE_STRING_KEY_UNSPECIFIED = typing___cast(ConsoleStringKeyValue, 0)
     CONSOLE_STRING_KEY_INVALID_CURSOR_FIELD = typing___cast(ConsoleStringKeyValue, 1000)
     CONSOLE_STRING_KEY_MISSING_ROWS = typing___cast(ConsoleStringKeyValue, 1001)
 CONSOLE_STRING_KEY_UNSPECIFIED = typing___cast(ConsoleStringKeyValue, 0)
 CONSOLE_STRING_KEY_INVALID_CURSOR_FIELD = typing___cast(ConsoleStringKeyValue, 1000)
 CONSOLE_STRING_KEY_MISSING_ROWS = typing___cast(ConsoleStringKeyValue, 1001)
+type___ConsoleStringKey = ConsoleStringKey
 
 class ConsoleString(google___protobuf___message___Message):
     DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
     class ValuesEntry(google___protobuf___message___Message):
         DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
         key: typing___Text = ...
         value: typing___Text = ...
@@ -67,15 +63,15 @@
             ) -> None: ...
         def ClearField(self, field_name: typing_extensions___Literal[u"key",b"key",u"value",b"value"]) -> None: ...
     type___ValuesEntry = ValuesEntry
 
     key: type___ConsoleStringKeyValue = ...
 
     @property
-    def values(self) -> google___protobuf___internal___containers___ScalarMap[typing___Text, typing___Text]: ...
+    def values(self) -> typing___MutableMapping[typing___Text, typing___Text]: ...
 
     def __init__(self,
         *,
         key : typing___Optional[type___ConsoleStringKeyValue] = None,
         values : typing___Optional[typing___Mapping[typing___Text, typing___Text]] = None,
         ) -> None: ...
     def ClearField(self, field_name: typing_extensions___Literal[u"key",b"key",u"values",b"values"]) -> None: ...
```

### Comparing `calixa-proto-py-2.0.8/calixa_proto_py/conversation.proto` & `calixa-proto-py-2.0.9/calixa_proto_py/conversation.proto`

 * *Files identical despite different names*

### Comparing `calixa-proto-py-2.0.8/calixa_proto_py/conversation_pb2.pyi` & `calixa-proto-py-2.0.9/calixa_proto_py/conversation_pb2.pyi`

 * *Files 2% similar despite different names*

```diff
@@ -1,11 +1,9 @@
-"""
-@generated by mypy-protobuf.  Do not edit manually!
-isort:skip_file
-"""
+# @generated by generate_proto_mypy_stubs.py.  Do not edit!
+import sys
 from google.protobuf.descriptor import (
     Descriptor as google___protobuf___descriptor___Descriptor,
     EnumDescriptor as google___protobuf___descriptor___EnumDescriptor,
     FileDescriptor as google___protobuf___descriptor___FileDescriptor,
 )
 
 from google.protobuf.internal.containers import (
@@ -52,38 +50,41 @@
     MESSAGE_SOURCE_EMAIL = typing___cast(MessageSourceValue, 3)
     MESSAGE_SOURCE_SMS = typing___cast(MessageSourceValue, 4)
 MESSAGE_SOURCE_UNSPECIFIED = typing___cast(MessageSourceValue, 0)
 MESSAGE_SOURCE_WEBFORM = typing___cast(MessageSourceValue, 1)
 MESSAGE_SOURCE_WEBCHAT = typing___cast(MessageSourceValue, 2)
 MESSAGE_SOURCE_EMAIL = typing___cast(MessageSourceValue, 3)
 MESSAGE_SOURCE_SMS = typing___cast(MessageSourceValue, 4)
+type___MessageSource = MessageSource
 
 MessageVisibilityValue = typing___NewType('MessageVisibilityValue', builtin___int)
 type___MessageVisibilityValue = MessageVisibilityValue
 MessageVisibility: _MessageVisibility
 class _MessageVisibility(google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper[MessageVisibilityValue]):
     DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
     MESSAGE_VISIBILITY_UNSPECIFIED = typing___cast(MessageVisibilityValue, 0)
     MESSAGE_VISIBILITY_PUBLIC = typing___cast(MessageVisibilityValue, 1)
     MESSAGE_VISIBILITY_INTERNAL = typing___cast(MessageVisibilityValue, 2)
 MESSAGE_VISIBILITY_UNSPECIFIED = typing___cast(MessageVisibilityValue, 0)
 MESSAGE_VISIBILITY_PUBLIC = typing___cast(MessageVisibilityValue, 1)
 MESSAGE_VISIBILITY_INTERNAL = typing___cast(MessageVisibilityValue, 2)
+type___MessageVisibility = MessageVisibility
 
 MessageDirectionValue = typing___NewType('MessageDirectionValue', builtin___int)
 type___MessageDirectionValue = MessageDirectionValue
 MessageDirection: _MessageDirection
 class _MessageDirection(google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper[MessageDirectionValue]):
     DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
     MESSAGE_DIRECTION_UNSPECIFIED = typing___cast(MessageDirectionValue, 0)
     MESSAGE_DIRECTION_INBOUND = typing___cast(MessageDirectionValue, 1)
     MESSAGE_DIRECTION_OUTBOUND = typing___cast(MessageDirectionValue, 2)
 MESSAGE_DIRECTION_UNSPECIFIED = typing___cast(MessageDirectionValue, 0)
 MESSAGE_DIRECTION_INBOUND = typing___cast(MessageDirectionValue, 1)
 MESSAGE_DIRECTION_OUTBOUND = typing___cast(MessageDirectionValue, 2)
+type___MessageDirection = MessageDirection
 
 MessageTypeValue = typing___NewType('MessageTypeValue', builtin___int)
 type___MessageTypeValue = MessageTypeValue
 MessageType: _MessageType
 class _MessageType(google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper[MessageTypeValue]):
     DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
     MESSAGE_TYPE_UNSPECIFIED = typing___cast(MessageTypeValue, 0)
@@ -106,14 +107,15 @@
 MESSAGE_TYPE_INTERCOM = typing___cast(MessageTypeValue, 5)
 MESSAGE_TYPE_SMOOCH = typing___cast(MessageTypeValue, 6)
 MESSAGE_TYPE_SMS = typing___cast(MessageTypeValue, 7)
 MESSAGE_TYPE_TWEET = typing___cast(MessageTypeValue, 8)
 MESSAGE_TYPE_TWEET_DM = typing___cast(MessageTypeValue, 9)
 MESSAGE_TYPE_WHATSAPP = typing___cast(MessageTypeValue, 10)
 MESSAGE_TYPE_ZENDESK = typing___cast(MessageTypeValue, 11)
+type___MessageType = MessageType
 
 class UserLite(google___protobuf___message___Message):
     DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
     external_user_id: typing___Text = ...
     name: typing___Text = ...
     email: typing___Text = ...
```

### Comparing `calixa-proto-py-2.0.8/calixa_proto_py/counter.proto` & `calixa-proto-py-2.0.9/calixa_proto_py/counter.proto`

 * *Files identical despite different names*

### Comparing `calixa-proto-py-2.0.8/calixa_proto_py/counter_pb2.pyi` & `calixa-proto-py-2.0.9/calixa_proto_py/counter_pb2.pyi`

 * *Files 3% similar despite different names*

```diff
@@ -1,11 +1,9 @@
-"""
-@generated by mypy-protobuf.  Do not edit manually!
-isort:skip_file
-"""
+# @generated by generate_proto_mypy_stubs.py.  Do not edit!
+import sys
 from google.protobuf.descriptor import (
     Descriptor as google___protobuf___descriptor___Descriptor,
     EnumDescriptor as google___protobuf___descriptor___EnumDescriptor,
     FileDescriptor as google___protobuf___descriptor___FileDescriptor,
 )
 
 from google.protobuf.internal.enum_type_wrapper import (
@@ -45,14 +43,15 @@
 CounterType: _CounterType
 class _CounterType(google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper[CounterTypeValue]):
     DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
     COUNTER_TYPE_UNSPECIFIED = typing___cast(CounterTypeValue, 0)
     COUNTER_TYPE_METRIC = typing___cast(CounterTypeValue, 1)
 COUNTER_TYPE_UNSPECIFIED = typing___cast(CounterTypeValue, 0)
 COUNTER_TYPE_METRIC = typing___cast(CounterTypeValue, 1)
+type___CounterType = CounterType
 
 GroupByValue = typing___NewType('GroupByValue', builtin___int)
 type___GroupByValue = GroupByValue
 GroupBy: _GroupBy
 class _GroupBy(google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper[GroupByValue]):
     DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
     GROUP_BY_UNSPECIFIED = typing___cast(GroupByValue, 0)
@@ -63,28 +62,30 @@
     GROUP_BY_YEAR = typing___cast(GroupByValue, 5)
 GROUP_BY_UNSPECIFIED = typing___cast(GroupByValue, 0)
 GROUP_BY_HOUR = typing___cast(GroupByValue, 1)
 GROUP_BY_DAY = typing___cast(GroupByValue, 2)
 GROUP_BY_WEEK = typing___cast(GroupByValue, 3)
 GROUP_BY_MONTH = typing___cast(GroupByValue, 4)
 GROUP_BY_YEAR = typing___cast(GroupByValue, 5)
+type___GroupBy = GroupBy
 
 AggregateOperationValue = typing___NewType('AggregateOperationValue', builtin___int)
 type___AggregateOperationValue = AggregateOperationValue
 AggregateOperation: _AggregateOperation
 class _AggregateOperation(google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper[AggregateOperationValue]):
     DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
     AGGREGATE_OPERATION_UNSPECIFIED = typing___cast(AggregateOperationValue, 0)
     AGGREGATE_OPERATION_SUM = typing___cast(AggregateOperationValue, 1)
     AGGREGATE_OPERATION_AVG = typing___cast(AggregateOperationValue, 2)
     AGGREGATE_OPERATION_COUNT = typing___cast(AggregateOperationValue, 3)
 AGGREGATE_OPERATION_UNSPECIFIED = typing___cast(AggregateOperationValue, 0)
 AGGREGATE_OPERATION_SUM = typing___cast(AggregateOperationValue, 1)
 AGGREGATE_OPERATION_AVG = typing___cast(AggregateOperationValue, 2)
 AGGREGATE_OPERATION_COUNT = typing___cast(AggregateOperationValue, 3)
+type___AggregateOperation = AggregateOperation
 
 class CounterKey(google___protobuf___message___Message):
     DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
     organization_id: typing___Text = ...
     key: typing___Text = ...
     counter_type: type___CounterTypeValue = ...
     param: typing___Text = ...
```

### Comparing `calixa-proto-py-2.0.8/calixa_proto_py/custom_entity.proto` & `calixa-proto-py-2.0.9/calixa_proto_py/custom_entity.proto`

 * *Files identical despite different names*

### Comparing `calixa-proto-py-2.0.8/calixa_proto_py/custom_entity_pb2.pyi` & `calixa-proto-py-2.0.9/calixa_proto_py/custom_entity_pb2.pyi`

 * *Files 6% similar despite different names*

```diff
@@ -1,19 +1,16 @@
-"""
-@generated by mypy-protobuf.  Do not edit manually!
-isort:skip_file
-"""
+# @generated by generate_proto_mypy_stubs.py.  Do not edit!
+import sys
 from google.protobuf.descriptor import (
     Descriptor as google___protobuf___descriptor___Descriptor,
     EnumDescriptor as google___protobuf___descriptor___EnumDescriptor,
     FileDescriptor as google___protobuf___descriptor___FileDescriptor,
 )
 
 from google.protobuf.internal.containers import (
-    MessageMap as google___protobuf___internal___containers___MessageMap,
     RepeatedCompositeFieldContainer as google___protobuf___internal___containers___RepeatedCompositeFieldContainer,
     RepeatedScalarFieldContainer as google___protobuf___internal___containers___RepeatedScalarFieldContainer,
 )
 
 from google.protobuf.internal.enum_type_wrapper import (
     _EnumTypeWrapper as google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper,
 )
@@ -25,14 +22,15 @@
 from google.protobuf.timestamp_pb2 import (
     Timestamp as google___protobuf___timestamp_pb2___Timestamp,
 )
 
 from typing import (
     Iterable as typing___Iterable,
     Mapping as typing___Mapping,
+    MutableMapping as typing___MutableMapping,
     NewType as typing___NewType,
     Optional as typing___Optional,
     Text as typing___Text,
     cast as typing___cast,
 )
 
 from typing_extensions import (
@@ -61,14 +59,15 @@
     CUSTOM_ENTITY_DEFINITION_FIELD_TYPE_TIMESTAMP = typing___cast(CustomEntityDefinitionFieldTypeValue, 5)
 CUSTOM_ENTITY_DEFINITION_FIELD_TYPE_UNSPECIFIED = typing___cast(CustomEntityDefinitionFieldTypeValue, 0)
 CUSTOM_ENTITY_DEFINITION_FIELD_TYPE_STRING = typing___cast(CustomEntityDefinitionFieldTypeValue, 1)
 CUSTOM_ENTITY_DEFINITION_FIELD_TYPE_LONG = typing___cast(CustomEntityDefinitionFieldTypeValue, 2)
 CUSTOM_ENTITY_DEFINITION_FIELD_TYPE_DOUBLE = typing___cast(CustomEntityDefinitionFieldTypeValue, 3)
 CUSTOM_ENTITY_DEFINITION_FIELD_TYPE_BOOLEAN = typing___cast(CustomEntityDefinitionFieldTypeValue, 4)
 CUSTOM_ENTITY_DEFINITION_FIELD_TYPE_TIMESTAMP = typing___cast(CustomEntityDefinitionFieldTypeValue, 5)
+type___CustomEntityDefinitionFieldType = CustomEntityDefinitionFieldType
 
 class CustomEntity(google___protobuf___message___Message):
     DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
     class ValuesEntry(google___protobuf___message___Message):
         DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
         key: typing___Text = ...
 
@@ -86,15 +85,15 @@
 
     custom_entity_definition_id: typing___Text = ...
     external_id: typing___Text = ...
     api_account_ids: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text] = ...
     api_user_ids: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text] = ...
 
     @property
-    def values(self) -> google___protobuf___internal___containers___MessageMap[typing___Text, type___CustomEntityFieldValue]: ...
+    def values(self) -> typing___MutableMapping[typing___Text, type___CustomEntityFieldValue]: ...
 
     def __init__(self,
         *,
         custom_entity_definition_id : typing___Optional[typing___Text] = None,
         external_id : typing___Optional[typing___Text] = None,
         api_account_ids : typing___Optional[typing___Iterable[typing___Text]] = None,
         api_user_ids : typing___Optional[typing___Iterable[typing___Text]] = None,
```

### Comparing `calixa-proto-py-2.0.8/calixa_proto_py/datawarehouse.proto` & `calixa-proto-py-2.0.9/calixa_proto_py/datawarehouse.proto`

 * *Files identical despite different names*

### Comparing `calixa-proto-py-2.0.8/calixa_proto_py/datawarehouse_pb2.pyi` & `calixa-proto-py-2.0.9/calixa_proto_py/datawarehouse_pb2.pyi`

 * *Files 3% similar despite different names*

```diff
@@ -1,11 +1,9 @@
-"""
-@generated by mypy-protobuf.  Do not edit manually!
-isort:skip_file
-"""
+# @generated by generate_proto_mypy_stubs.py.  Do not edit!
+import sys
 from common_pb2 import (
     EntityTypeValue as common_pb2___EntityTypeValue,
 )
 
 from console_string_pb2 import (
     ConsoleString as console_string_pb2___ConsoleString,
 )
@@ -20,18 +18,16 @@
 
 from google.protobuf.descriptor import (
     Descriptor as google___protobuf___descriptor___Descriptor,
     FileDescriptor as google___protobuf___descriptor___FileDescriptor,
 )
 
 from google.protobuf.internal.containers import (
-    MessageMap as google___protobuf___internal___containers___MessageMap,
     RepeatedCompositeFieldContainer as google___protobuf___internal___containers___RepeatedCompositeFieldContainer,
     RepeatedScalarFieldContainer as google___protobuf___internal___containers___RepeatedScalarFieldContainer,
-    ScalarMap as google___protobuf___internal___containers___ScalarMap,
 )
 
 from google.protobuf.message import (
     Message as google___protobuf___message___Message,
 )
 
 from google.protobuf.timestamp_pb2 import (
@@ -54,14 +50,15 @@
     MetricValue as metric_pb2___MetricValue,
     MetricValueTypeValue as metric_pb2___MetricValueTypeValue,
 )
 
 from typing import (
     Iterable as typing___Iterable,
     Mapping as typing___Mapping,
+    MutableMapping as typing___MutableMapping,
     Optional as typing___Optional,
     Text as typing___Text,
 )
 
 from typing_extensions import (
     Literal as typing_extensions___Literal,
 )
@@ -473,21 +470,21 @@
     @property
     def entities(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[entity_pb2___EntityWithRelationships]: ...
 
     @property
     def table(self) -> type___DataWarehouseTable: ...
 
     @property
-    def errors(self) -> google___protobuf___internal___containers___ScalarMap[typing___Text, typing___Text]: ...
+    def errors(self) -> typing___MutableMapping[typing___Text, typing___Text]: ...
 
     @property
     def observations(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[type___MetricPreview]: ...
 
     @property
-    def warnings(self) -> google___protobuf___internal___containers___MessageMap[typing___Text, console_string_pb2___ConsoleString]: ...
+    def warnings(self) -> typing___MutableMapping[typing___Text, console_string_pb2___ConsoleString]: ...
 
     def __init__(self,
         *,
         entities : typing___Optional[typing___Iterable[entity_pb2___EntityWithRelationships]] = None,
         table : typing___Optional[type___DataWarehouseTable] = None,
         errors : typing___Optional[typing___Mapping[typing___Text, typing___Text]] = None,
         observations : typing___Optional[typing___Iterable[type___MetricPreview]] = None,
```

### Comparing `calixa-proto-py-2.0.8/calixa_proto_py/datawarehouse_pb2_grpc.py` & `calixa-proto-py-2.0.9/calixa_proto_py/datawarehouse_pb2_grpc.py`

 * *Files identical despite different names*

### Comparing `calixa-proto-py-2.0.8/calixa_proto_py/domaindata.proto` & `calixa-proto-py-2.0.9/calixa_proto_py/domaindata.proto`

 * *Files identical despite different names*

### Comparing `calixa-proto-py-2.0.8/calixa_proto_py/domaindata_pb2.pyi` & `calixa-proto-py-2.0.9/calixa_proto_py/domaindata_pb2.pyi`

 * *Files 5% similar despite different names*

```diff
@@ -1,11 +1,9 @@
-"""
-@generated by mypy-protobuf.  Do not edit manually!
-isort:skip_file
-"""
+# @generated by generate_proto_mypy_stubs.py.  Do not edit!
+import sys
 from google.protobuf.descriptor import (
     Descriptor as google___protobuf___descriptor___Descriptor,
     EnumDescriptor as google___protobuf___descriptor___EnumDescriptor,
     FileDescriptor as google___protobuf___descriptor___FileDescriptor,
 )
 
 from google.protobuf.internal.enum_type_wrapper import (
@@ -57,14 +55,15 @@
 DOMAIN_DATA_TYPE_ACCOUNT_METRIC_DESCRIPTOR_ID = typing___cast(DomainDataTypeValue, 3)
 DOMAIN_DATA_TYPE_ACCOUNT_USER_METRIC_DESCRIPTOR_ID = typing___cast(DomainDataTypeValue, 4)
 DOMAIN_DATA_TYPE_ACCOUNT_TAG = typing___cast(DomainDataTypeValue, 5)
 DOMAIN_DATA_TYPE_ACCOUNT_USER_TAG = typing___cast(DomainDataTypeValue, 6)
 DOMAIN_DATA_TYPE_ACCOUNT_AND_ACCOUNT_USER_SALESFORCE_OWNERS = typing___cast(DomainDataTypeValue, 7)
 DOMAIN_DATA_TYPE_ACCOUNT_AND_ACCOUNT_USER_HUBSPOT_OWNERS = typing___cast(DomainDataTypeValue, 8)
 DOMAIN_DATA_TYPE_ACCOUNT_AND_ACCOUNT_USER_ORGANIZATION_USERS_OWNERS = typing___cast(DomainDataTypeValue, 9)
+type___DomainDataType = DomainDataType
 
 class DomainValue(google___protobuf___message___Message):
     DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
     organization_id: typing___Text = ...
     type: type___DomainDataTypeValue = ...
     domain_value: typing___Text = ...
```

### Comparing `calixa-proto-py-2.0.8/calixa_proto_py/entity.proto` & `calixa-proto-py-2.0.9/calixa_proto_py/entity.proto`

 * *Files 2% similar despite different names*

```diff
@@ -26,14 +26,66 @@
 
 option java_package = "io.calixa.domain.entity";
 option java_multiple_files = true;
 option optimize_for = SPEED;
 
 package calixa.domain.entity;
 
+enum EntityObserverNotificationPolicy {
+  ENTITY_OBSERVER_NOTIFICATION_POLICY_UNDEFINED = 0;
+  ENTITY_OBSERVER_NOTIFICATION_POLICY_ONCE = 1;
+  ENTITY_OBSERVER_NOTIFICATION_POLICY_ALWAYS = 2;
+}
+
+message ActionEvinceUpdate {
+  google.protobuf.FieldMask field_mask = 1;
+}
+
+message ActionAddUserToAccount {
+  common.ExternalId api_user_id = 1;
+}
+
+message EntityObserverAction {
+  oneof action {
+    ActionEvinceUpdate evince_update = 1;
+    ActionAddUserToAccount add_user_to_account = 2;
+  }
+}
+
+message MutationObserver {
+  string organization_id = 1;
+
+  oneof observer {
+    EntityObserver entity_observer = 2;
+    RelationshipObserver relationship_observer = 3;
+  }
+
+  EntityObserverNotificationPolicy notification_policy = 11;
+  EntityObserverAction action = 12;
+}
+
+message RelationshipObserver {
+  common.ExternalId observed = 1;           // The entity being observed
+  common.ExternalId observer = 2;           // The entity observing
+
+  repeated entity.MutationType mutation_types = 3;
+  RelationshipType relationship_type = 4;
+  common.EntityType from_entity_type = 5;
+}
+
+message EntityObserver {
+  common.ExternalId observed = 1; // The entity being observed
+  common.ExternalId observer = 2; // The entity observing
+
+  // When mutation_types includes UPDATED, the FieldMask that must be set in
+  // order to invoke action
+  repeated entity.MutationType mutation_types = 3;
+  google.protobuf.FieldMask update_mask = 4;
+}
+
 message Entity {
   reserved 303, 304, 2007, 2008;
   reserved 3; // PushNotificationConfig push_notification_config in entity
   reserved 9000; // previously calixa.domain.notification.PushNotificationLog
   reserved 102; // calixa.domain.account.AccountUserRole account_user_role = 102;
   reserved 2009;  //calixa.domain.external.CognitoUser cognito_user = 2009;
 
@@ -643,9 +695,10 @@
 enum EntityState {
   ENTITY_STATE_ACTIVE = 0;
   ENTITY_STATE_DELETED = 1; // entity was deleted in external CRM, we mark it as deleted
 }
 
 message AutomationEvent {
   Entity automation = 1;
-  Entity event = 2;
+  EntityWithRelationships entity_with_relationships = 2;
+  EntityReference entity_reference = 3;
 }
```

### Comparing `calixa-proto-py-2.0.8/calixa_proto_py/entity_pb2.pyi` & `calixa-proto-py-2.0.9/calixa_proto_py/entity_pb2.pyi`

 * *Files 4% similar despite different names*

```diff
@@ -1,11 +1,9 @@
-"""
-@generated by mypy-protobuf.  Do not edit manually!
-isort:skip_file
-"""
+# @generated by generate_proto_mypy_stubs.py.  Do not edit!
+import sys
 from account_pb2 import (
     Account as account_pb2___Account,
     AccountUser as account_pb2___AccountUser,
     Opportunity as account_pb2___Opportunity,
     Teammate as account_pb2___Teammate,
 )
 
@@ -155,14 +153,27 @@
 builtin___bytes = bytes
 builtin___float = float
 builtin___int = int
 
 
 DESCRIPTOR: google___protobuf___descriptor___FileDescriptor = ...
 
+EntityObserverNotificationPolicyValue = typing___NewType('EntityObserverNotificationPolicyValue', builtin___int)
+type___EntityObserverNotificationPolicyValue = EntityObserverNotificationPolicyValue
+EntityObserverNotificationPolicy: _EntityObserverNotificationPolicy
+class _EntityObserverNotificationPolicy(google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper[EntityObserverNotificationPolicyValue]):
+    DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
+    ENTITY_OBSERVER_NOTIFICATION_POLICY_UNDEFINED = typing___cast(EntityObserverNotificationPolicyValue, 0)
+    ENTITY_OBSERVER_NOTIFICATION_POLICY_ONCE = typing___cast(EntityObserverNotificationPolicyValue, 1)
+    ENTITY_OBSERVER_NOTIFICATION_POLICY_ALWAYS = typing___cast(EntityObserverNotificationPolicyValue, 2)
+ENTITY_OBSERVER_NOTIFICATION_POLICY_UNDEFINED = typing___cast(EntityObserverNotificationPolicyValue, 0)
+ENTITY_OBSERVER_NOTIFICATION_POLICY_ONCE = typing___cast(EntityObserverNotificationPolicyValue, 1)
+ENTITY_OBSERVER_NOTIFICATION_POLICY_ALWAYS = typing___cast(EntityObserverNotificationPolicyValue, 2)
+type___EntityObserverNotificationPolicy = EntityObserverNotificationPolicy
+
 RelationshipTypeValue = typing___NewType('RelationshipTypeValue', builtin___int)
 type___RelationshipTypeValue = RelationshipTypeValue
 RelationshipType: _RelationshipType
 class _RelationshipType(google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper[RelationshipTypeValue]):
     DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
     GRAPH_EDGE_TYPE_UNSPECIFIED = typing___cast(RelationshipTypeValue, 0)
     GRAPH_EDGE_TYPE_BELONGS_TO = typing___cast(RelationshipTypeValue, 1)
@@ -182,42 +193,45 @@
 GRAPH_EDGE_TYPE_EVENT_BELONGS_TO = typing___cast(RelationshipTypeValue, 4)
 GRAPH_EDGE_TYPE_TAGGED_WITH = typing___cast(RelationshipTypeValue, 5)
 GRAPH_EDGE_TYPE_HOUSEKEEPING = typing___cast(RelationshipTypeValue, 6)
 GRAPH_EDGE_TYPE_OWNED_BY = typing___cast(RelationshipTypeValue, 7)
 GRAPH_EDGE_EXTERNAL_USER_BELONGS_TO_EXTERNAL_ACCOUNT = typing___cast(RelationshipTypeValue, 8)
 GRAPH_EDGE_TYPE_ACCOUNT_OR_ACCOUNT_USER_OWNED_BY = typing___cast(RelationshipTypeValue, 9)
 GRAPH_EDGE_TYPE_ENRICHED_WITH = typing___cast(RelationshipTypeValue, 10)
+type___RelationshipType = RelationshipType
 
 EdgeDirectionValue = typing___NewType('EdgeDirectionValue', builtin___int)
 type___EdgeDirectionValue = EdgeDirectionValue
 EdgeDirection: _EdgeDirection
 class _EdgeDirection(google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper[EdgeDirectionValue]):
     DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
     GRAPH_EDGE_DIRECTION_UNSPECIFIED = typing___cast(EdgeDirectionValue, 0)
     GRAPH_EDGE_DIRECTION_INCOMING = typing___cast(EdgeDirectionValue, 1)
     GRAPH_EDGE_DIRECTION_OUTGOING = typing___cast(EdgeDirectionValue, 2)
     GRAPH_EDGE_DIRECTION_BOTH = typing___cast(EdgeDirectionValue, 3)
 GRAPH_EDGE_DIRECTION_UNSPECIFIED = typing___cast(EdgeDirectionValue, 0)
 GRAPH_EDGE_DIRECTION_INCOMING = typing___cast(EdgeDirectionValue, 1)
 GRAPH_EDGE_DIRECTION_OUTGOING = typing___cast(EdgeDirectionValue, 2)
 GRAPH_EDGE_DIRECTION_BOTH = typing___cast(EdgeDirectionValue, 3)
+type___EdgeDirection = EdgeDirection
 
 MutationTypeValue = typing___NewType('MutationTypeValue', builtin___int)
 type___MutationTypeValue = MutationTypeValue
 MutationType: _MutationType
 class _MutationType(google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper[MutationTypeValue]):
     DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
     MUTATION_TYPE_UNSPECIFIED = typing___cast(MutationTypeValue, 0)
     MUTATION_TYPE_CREATED = typing___cast(MutationTypeValue, 1)
     MUTATION_TYPE_UPDATED = typing___cast(MutationTypeValue, 2)
     MUTATION_TYPE_DELETED = typing___cast(MutationTypeValue, 3)
 MUTATION_TYPE_UNSPECIFIED = typing___cast(MutationTypeValue, 0)
 MUTATION_TYPE_CREATED = typing___cast(MutationTypeValue, 1)
 MUTATION_TYPE_UPDATED = typing___cast(MutationTypeValue, 2)
 MUTATION_TYPE_DELETED = typing___cast(MutationTypeValue, 3)
+type___MutationType = MutationType
 
 SaveEntityMutationTypeValue = typing___NewType('SaveEntityMutationTypeValue', builtin___int)
 type___SaveEntityMutationTypeValue = SaveEntityMutationTypeValue
 SaveEntityMutationType: _SaveEntityMutationType
 class _SaveEntityMutationType(google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper[SaveEntityMutationTypeValue]):
     DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
     SAVE_ENTITY_MUTATION_TYPE_UNSPECIFIED = typing___cast(SaveEntityMutationTypeValue, 0)
@@ -228,14 +242,15 @@
     SAVE_ENTITY_MUTATION_TYPE_STALE_UPDATE = typing___cast(SaveEntityMutationTypeValue, 5)
 SAVE_ENTITY_MUTATION_TYPE_UNSPECIFIED = typing___cast(SaveEntityMutationTypeValue, 0)
 SAVE_ENTITY_MUTATION_TYPE_CREATED = typing___cast(SaveEntityMutationTypeValue, 1)
 SAVE_ENTITY_MUTATION_TYPE_UPDATED = typing___cast(SaveEntityMutationTypeValue, 2)
 SAVE_ENTITY_MUTATION_TYPE_DELETED = typing___cast(SaveEntityMutationTypeValue, 3)
 SAVE_ENTITY_MUTATION_TYPE_NOOP = typing___cast(SaveEntityMutationTypeValue, 4)
 SAVE_ENTITY_MUTATION_TYPE_STALE_UPDATE = typing___cast(SaveEntityMutationTypeValue, 5)
+type___SaveEntityMutationType = SaveEntityMutationType
 
 DataWarehouseFieldTypeValue = typing___NewType('DataWarehouseFieldTypeValue', builtin___int)
 type___DataWarehouseFieldTypeValue = DataWarehouseFieldTypeValue
 DataWarehouseFieldType: _DataWarehouseFieldType
 class _DataWarehouseFieldType(google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper[DataWarehouseFieldTypeValue]):
     DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
     DATA_WAREHOUSE_FIELD_TYPE_UNSPECIFIED = typing___cast(DataWarehouseFieldTypeValue, 0)
@@ -252,24 +267,148 @@
 DATA_WAREHOUSE_FIELD_TYPE_STRING = typing___cast(DataWarehouseFieldTypeValue, 2)
 DATA_WAREHOUSE_FIELD_TYPE_ENUM = typing___cast(DataWarehouseFieldTypeValue, 3)
 DATA_WAREHOUSE_FIELD_TYPE_BOOLEAN = typing___cast(DataWarehouseFieldTypeValue, 4)
 DATA_WAREHOUSE_FIELD_TYPE_TIMESTAMP = typing___cast(DataWarehouseFieldTypeValue, 5)
 DATA_WAREHOUSE_FIELD_TYPE_DECIMAL = typing___cast(DataWarehouseFieldTypeValue, 6)
 DATA_WAREHOUSE_FIELD_TYPE_PRIMARY_EXTERNAL_ID = typing___cast(DataWarehouseFieldTypeValue, 1000)
 DATA_WAREHOUSE_FIELD_TYPE_EMAIL_EXTERNAL_ID = typing___cast(DataWarehouseFieldTypeValue, 1001)
+type___DataWarehouseFieldType = DataWarehouseFieldType
 
 EntityStateValue = typing___NewType('EntityStateValue', builtin___int)
 type___EntityStateValue = EntityStateValue
 EntityState: _EntityState
 class _EntityState(google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper[EntityStateValue]):
     DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
     ENTITY_STATE_ACTIVE = typing___cast(EntityStateValue, 0)
     ENTITY_STATE_DELETED = typing___cast(EntityStateValue, 1)
 ENTITY_STATE_ACTIVE = typing___cast(EntityStateValue, 0)
 ENTITY_STATE_DELETED = typing___cast(EntityStateValue, 1)
+type___EntityState = EntityState
+
+class ActionEvinceUpdate(google___protobuf___message___Message):
+    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
+
+    @property
+    def field_mask(self) -> google___protobuf___field_mask_pb2___FieldMask: ...
+
+    def __init__(self,
+        *,
+        field_mask : typing___Optional[google___protobuf___field_mask_pb2___FieldMask] = None,
+        ) -> None: ...
+    def HasField(self, field_name: typing_extensions___Literal[u"field_mask",b"field_mask"]) -> builtin___bool: ...
+    def ClearField(self, field_name: typing_extensions___Literal[u"field_mask",b"field_mask"]) -> None: ...
+type___ActionEvinceUpdate = ActionEvinceUpdate
+
+class ActionAddUserToAccount(google___protobuf___message___Message):
+    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
+
+    @property
+    def api_user_id(self) -> common_pb2___ExternalId: ...
+
+    def __init__(self,
+        *,
+        api_user_id : typing___Optional[common_pb2___ExternalId] = None,
+        ) -> None: ...
+    def HasField(self, field_name: typing_extensions___Literal[u"api_user_id",b"api_user_id"]) -> builtin___bool: ...
+    def ClearField(self, field_name: typing_extensions___Literal[u"api_user_id",b"api_user_id"]) -> None: ...
+type___ActionAddUserToAccount = ActionAddUserToAccount
+
+class EntityObserverAction(google___protobuf___message___Message):
+    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
+
+    @property
+    def evince_update(self) -> type___ActionEvinceUpdate: ...
+
+    @property
+    def add_user_to_account(self) -> type___ActionAddUserToAccount: ...
+
+    def __init__(self,
+        *,
+        evince_update : typing___Optional[type___ActionEvinceUpdate] = None,
+        add_user_to_account : typing___Optional[type___ActionAddUserToAccount] = None,
+        ) -> None: ...
+    def HasField(self, field_name: typing_extensions___Literal[u"action",b"action",u"add_user_to_account",b"add_user_to_account",u"evince_update",b"evince_update"]) -> builtin___bool: ...
+    def ClearField(self, field_name: typing_extensions___Literal[u"action",b"action",u"add_user_to_account",b"add_user_to_account",u"evince_update",b"evince_update"]) -> None: ...
+    def WhichOneof(self, oneof_group: typing_extensions___Literal[u"action",b"action"]) -> typing_extensions___Literal["evince_update","add_user_to_account"]: ...
+type___EntityObserverAction = EntityObserverAction
+
+class MutationObserver(google___protobuf___message___Message):
+    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
+    organization_id: typing___Text = ...
+    notification_policy: type___EntityObserverNotificationPolicyValue = ...
+
+    @property
+    def entity_observer(self) -> type___EntityObserver: ...
+
+    @property
+    def relationship_observer(self) -> type___RelationshipObserver: ...
+
+    @property
+    def action(self) -> type___EntityObserverAction: ...
+
+    def __init__(self,
+        *,
+        organization_id : typing___Optional[typing___Text] = None,
+        entity_observer : typing___Optional[type___EntityObserver] = None,
+        relationship_observer : typing___Optional[type___RelationshipObserver] = None,
+        notification_policy : typing___Optional[type___EntityObserverNotificationPolicyValue] = None,
+        action : typing___Optional[type___EntityObserverAction] = None,
+        ) -> None: ...
+    def HasField(self, field_name: typing_extensions___Literal[u"action",b"action",u"entity_observer",b"entity_observer",u"observer",b"observer",u"relationship_observer",b"relationship_observer"]) -> builtin___bool: ...
+    def ClearField(self, field_name: typing_extensions___Literal[u"action",b"action",u"entity_observer",b"entity_observer",u"notification_policy",b"notification_policy",u"observer",b"observer",u"organization_id",b"organization_id",u"relationship_observer",b"relationship_observer"]) -> None: ...
+    def WhichOneof(self, oneof_group: typing_extensions___Literal[u"observer",b"observer"]) -> typing_extensions___Literal["entity_observer","relationship_observer"]: ...
+type___MutationObserver = MutationObserver
+
+class RelationshipObserver(google___protobuf___message___Message):
+    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
+    mutation_types: google___protobuf___internal___containers___RepeatedScalarFieldContainer[type___MutationTypeValue] = ...
+    relationship_type: type___RelationshipTypeValue = ...
+    from_entity_type: common_pb2___EntityTypeValue = ...
+
+    @property
+    def observed(self) -> common_pb2___ExternalId: ...
+
+    @property
+    def observer(self) -> common_pb2___ExternalId: ...
+
+    def __init__(self,
+        *,
+        observed : typing___Optional[common_pb2___ExternalId] = None,
+        observer : typing___Optional[common_pb2___ExternalId] = None,
+        mutation_types : typing___Optional[typing___Iterable[type___MutationTypeValue]] = None,
+        relationship_type : typing___Optional[type___RelationshipTypeValue] = None,
+        from_entity_type : typing___Optional[common_pb2___EntityTypeValue] = None,
+        ) -> None: ...
+    def HasField(self, field_name: typing_extensions___Literal[u"observed",b"observed",u"observer",b"observer"]) -> builtin___bool: ...
+    def ClearField(self, field_name: typing_extensions___Literal[u"from_entity_type",b"from_entity_type",u"mutation_types",b"mutation_types",u"observed",b"observed",u"observer",b"observer",u"relationship_type",b"relationship_type"]) -> None: ...
+type___RelationshipObserver = RelationshipObserver
+
+class EntityObserver(google___protobuf___message___Message):
+    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
+    mutation_types: google___protobuf___internal___containers___RepeatedScalarFieldContainer[type___MutationTypeValue] = ...
+
+    @property
+    def observed(self) -> common_pb2___ExternalId: ...
+
+    @property
+    def observer(self) -> common_pb2___ExternalId: ...
+
+    @property
+    def update_mask(self) -> google___protobuf___field_mask_pb2___FieldMask: ...
+
+    def __init__(self,
+        *,
+        observed : typing___Optional[common_pb2___ExternalId] = None,
+        observer : typing___Optional[common_pb2___ExternalId] = None,
+        mutation_types : typing___Optional[typing___Iterable[type___MutationTypeValue]] = None,
+        update_mask : typing___Optional[google___protobuf___field_mask_pb2___FieldMask] = None,
+        ) -> None: ...
+    def HasField(self, field_name: typing_extensions___Literal[u"observed",b"observed",u"observer",b"observer",u"update_mask",b"update_mask"]) -> builtin___bool: ...
+    def ClearField(self, field_name: typing_extensions___Literal[u"mutation_types",b"mutation_types",u"observed",b"observed",u"observer",b"observer",u"update_mask",b"update_mask"]) -> None: ...
+type___EntityObserver = EntityObserver
 
 class Entity(google___protobuf___message___Message):
     DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
     organization_id: typing___Text = ...
     canonical_id: typing___Text = ...
     entity_state: type___EntityStateValue = ...
 
@@ -1371,17 +1510,21 @@
 class AutomationEvent(google___protobuf___message___Message):
     DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
 
     @property
     def automation(self) -> type___Entity: ...
 
     @property
-    def event(self) -> type___Entity: ...
+    def entity_with_relationships(self) -> type___EntityWithRelationships: ...
+
+    @property
+    def entity_reference(self) -> entity_reference_pb2___EntityReference: ...
 
     def __init__(self,
         *,
         automation : typing___Optional[type___Entity] = None,
-        event : typing___Optional[type___Entity] = None,
+        entity_with_relationships : typing___Optional[type___EntityWithRelationships] = None,
+        entity_reference : typing___Optional[entity_reference_pb2___EntityReference] = None,
         ) -> None: ...
-    def HasField(self, field_name: typing_extensions___Literal[u"automation",b"automation",u"event",b"event"]) -> builtin___bool: ...
-    def ClearField(self, field_name: typing_extensions___Literal[u"automation",b"automation",u"event",b"event"]) -> None: ...
+    def HasField(self, field_name: typing_extensions___Literal[u"automation",b"automation",u"entity_reference",b"entity_reference",u"entity_with_relationships",b"entity_with_relationships"]) -> builtin___bool: ...
+    def ClearField(self, field_name: typing_extensions___Literal[u"automation",b"automation",u"entity_reference",b"entity_reference",u"entity_with_relationships",b"entity_with_relationships"]) -> None: ...
 type___AutomationEvent = AutomationEvent
```

### Comparing `calixa-proto-py-2.0.8/calixa_proto_py/entity_pb2_grpc.py` & `calixa-proto-py-2.0.9/calixa_proto_py/entity_pb2_grpc.py`

 * *Files identical despite different names*

### Comparing `calixa-proto-py-2.0.8/calixa_proto_py/entity_reference.proto` & `calixa-proto-py-2.0.9/calixa_proto_py/entity_reference.proto`

 * *Files 20% similar despite different names*

```diff
@@ -9,12 +9,12 @@
 package calixa.domain.entity;
 
 // Defines a reference (unique locatable instance) to an Entity within the
 // graph. This can be either a canonical ID (internally known) or an ExternalId.
 message EntityReference {
   string organization_id = 1;
   oneof id {
-    calixa.domain.common.ExternalId externalId = 2;
+    calixa.domain.common.ExternalId external_id = 2;
     string canonical_id = 3;
   }
   calixa.domain.common.EntityType entity_type = 4;
-}
+}
```

### Comparing `calixa-proto-py-2.0.8/calixa_proto_py/entity_reference_pb2.pyi` & `calixa-proto-py-2.0.9/calixa_proto_py/entity_reference_pb2.pyi`

 * *Files 16% similar despite different names*

```diff
@@ -1,11 +1,9 @@
-"""
-@generated by mypy-protobuf.  Do not edit manually!
-isort:skip_file
-"""
+# @generated by generate_proto_mypy_stubs.py.  Do not edit!
+import sys
 from common_pb2 import (
     EntityTypeValue as common_pb2___EntityTypeValue,
     ExternalId as common_pb2___ExternalId,
 )
 
 from google.protobuf.descriptor import (
     Descriptor as google___protobuf___descriptor___Descriptor,
@@ -37,20 +35,20 @@
 class EntityReference(google___protobuf___message___Message):
     DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
     organization_id: typing___Text = ...
     canonical_id: typing___Text = ...
     entity_type: common_pb2___EntityTypeValue = ...
 
     @property
-    def externalId(self) -> common_pb2___ExternalId: ...
+    def external_id(self) -> common_pb2___ExternalId: ...
 
     def __init__(self,
         *,
         organization_id : typing___Optional[typing___Text] = None,
-        externalId : typing___Optional[common_pb2___ExternalId] = None,
+        external_id : typing___Optional[common_pb2___ExternalId] = None,
         canonical_id : typing___Optional[typing___Text] = None,
         entity_type : typing___Optional[common_pb2___EntityTypeValue] = None,
         ) -> None: ...
-    def HasField(self, field_name: typing_extensions___Literal[u"canonical_id",b"canonical_id",u"externalId",b"externalId",u"id",b"id"]) -> builtin___bool: ...
-    def ClearField(self, field_name: typing_extensions___Literal[u"canonical_id",b"canonical_id",u"entity_type",b"entity_type",u"externalId",b"externalId",u"id",b"id",u"organization_id",b"organization_id"]) -> None: ...
-    def WhichOneof(self, oneof_group: typing_extensions___Literal[u"id",b"id"]) -> typing_extensions___Literal["externalId","canonical_id"]: ...
+    def HasField(self, field_name: typing_extensions___Literal[u"canonical_id",b"canonical_id",u"external_id",b"external_id",u"id",b"id"]) -> builtin___bool: ...
+    def ClearField(self, field_name: typing_extensions___Literal[u"canonical_id",b"canonical_id",u"entity_type",b"entity_type",u"external_id",b"external_id",u"id",b"id",u"organization_id",b"organization_id"]) -> None: ...
+    def WhichOneof(self, oneof_group: typing_extensions___Literal[u"id",b"id"]) -> typing_extensions___Literal["external_id","canonical_id"]: ...
 type___EntityReference = EntityReference
```

### Comparing `calixa-proto-py-2.0.8/calixa_proto_py/event_label.proto` & `calixa-proto-py-2.0.9/calixa_proto_py/event_label.proto`

 * *Files 18% similar despite different names*

```diff
@@ -39,18 +39,18 @@
   EVENT_LABEL_CONVERSATION_CREATED = 500;
   EVENT_LABEL_MESSAGE_CREATED = 501;
 
   EVENT_LABEL_OPPORTUNITY_CREATED = 600;
   EVENT_LABEL_OPPORTUNITY_UPDATED = 601;
 
   // External Entity Updates
-  EVENT_LABEL_EXTERNAL_USER_UPDATED = 700;
-  EVENT_LABEL_EXTERNAL_ACCOUNT_UPDATED = 701;
-  EVENT_LABEL_EXTERNAL_USER_CREATED = 702;
-  EVENT_LABEL_EXTERNAL_ACCOUNT_CREATED = 703;
+  EVENT_LABEL_EXTERNAL_USER_UPDATED = 700 [deprecated = true];
+  EVENT_LABEL_EXTERNAL_ACCOUNT_UPDATED = 701 [deprecated = true];
+  EVENT_LABEL_EXTERNAL_USER_CREATED = 702 [deprecated = true];
+  EVENT_LABEL_EXTERNAL_ACCOUNT_CREATED = 703 [deprecated = true];
 
   // Tagged entities - Currently only for AC/ACU
   EVENT_LABEL_TAG_ADDED = 800;
   EVENT_LABEL_TAG_REMOVED = 801;
 
   // Actions
   EVENT_LABEL_ACTION_INVOKED = 900;
```

### Comparing `calixa-proto-py-2.0.8/calixa_proto_py/event_label_pb2.pyi` & `calixa-proto-py-2.0.9/calixa_proto_py/event_label_pb2.pyi`

 * *Files 4% similar despite different names*

```diff
@@ -1,11 +1,9 @@
-"""
-@generated by mypy-protobuf.  Do not edit manually!
-isort:skip_file
-"""
+# @generated by generate_proto_mypy_stubs.py.  Do not edit!
+import sys
 from google.protobuf.descriptor import (
     EnumDescriptor as google___protobuf___descriptor___EnumDescriptor,
     FileDescriptor as google___protobuf___descriptor___FileDescriptor,
 )
 
 from google.protobuf.internal.enum_type_wrapper import (
     _EnumTypeWrapper as google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper,
@@ -95,7 +93,8 @@
 EVENT_LABEL_EXTERNAL_USER_CREATED = typing___cast(EventLabelValue, 702)
 EVENT_LABEL_EXTERNAL_ACCOUNT_CREATED = typing___cast(EventLabelValue, 703)
 EVENT_LABEL_TAG_ADDED = typing___cast(EventLabelValue, 800)
 EVENT_LABEL_TAG_REMOVED = typing___cast(EventLabelValue, 801)
 EVENT_LABEL_ACTION_INVOKED = typing___cast(EventLabelValue, 900)
 EVENT_LABEL_CUSTOM_ENTITY_CREATED = typing___cast(EventLabelValue, 1001)
 EVENT_LABEL_CUSTOM_ENTITY_UPDATED = typing___cast(EventLabelValue, 1002)
+type___EventLabel = EventLabel
```

### Comparing `calixa-proto-py-2.0.8/calixa_proto_py/external_domain_model.proto` & `calixa-proto-py-2.0.9/calixa_proto_py/external_domain_model.proto`

 * *Files identical despite different names*

### Comparing `calixa-proto-py-2.0.8/calixa_proto_py/external_domain_model_pb2.pyi` & `calixa-proto-py-2.0.9/calixa_proto_py/external_domain_model_pb2.pyi`

 * *Files 0% similar despite different names*

```diff
@@ -1,11 +1,9 @@
-"""
-@generated by mypy-protobuf.  Do not edit manually!
-isort:skip_file
-"""
+# @generated by generate_proto_mypy_stubs.py.  Do not edit!
+import sys
 from account_pb2 import (
     AccountStatusValue as account_pb2___AccountStatusValue,
     AccountUserStatusValue as account_pb2___AccountUserStatusValue,
 )
 
 from common_pb2 import (
     Amount as common_pb2___Amount,
@@ -15,15 +13,14 @@
 from google.protobuf.descriptor import (
     Descriptor as google___protobuf___descriptor___Descriptor,
     EnumDescriptor as google___protobuf___descriptor___EnumDescriptor,
     FileDescriptor as google___protobuf___descriptor___FileDescriptor,
 )
 
 from google.protobuf.internal.containers import (
-    MessageMap as google___protobuf___internal___containers___MessageMap,
     RepeatedCompositeFieldContainer as google___protobuf___internal___containers___RepeatedCompositeFieldContainer,
     RepeatedScalarFieldContainer as google___protobuf___internal___containers___RepeatedScalarFieldContainer,
 )
 
 from google.protobuf.internal.enum_type_wrapper import (
     _EnumTypeWrapper as google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper,
 )
@@ -41,14 +38,15 @@
 from google.protobuf.timestamp_pb2 import (
     Timestamp as google___protobuf___timestamp_pb2___Timestamp,
 )
 
 from typing import (
     Iterable as typing___Iterable,
     Mapping as typing___Mapping,
+    MutableMapping as typing___MutableMapping,
     NewType as typing___NewType,
     Optional as typing___Optional,
     Text as typing___Text,
     cast as typing___cast,
 )
 
 from typing_extensions import (
@@ -71,14 +69,15 @@
     DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
     CUSTOM_PROPERTY_TYPE_UNSPECIFIED = typing___cast(CustomPropertyTypeValue, 0)
     CUSTOM_PROPERTY_TYPE_SCALAR = typing___cast(CustomPropertyTypeValue, 1)
     CUSTOM_PROPERTY_TYPE_RELATIONSHIP = typing___cast(CustomPropertyTypeValue, 2)
 CUSTOM_PROPERTY_TYPE_UNSPECIFIED = typing___cast(CustomPropertyTypeValue, 0)
 CUSTOM_PROPERTY_TYPE_SCALAR = typing___cast(CustomPropertyTypeValue, 1)
 CUSTOM_PROPERTY_TYPE_RELATIONSHIP = typing___cast(CustomPropertyTypeValue, 2)
+type___CustomPropertyType = CustomPropertyType
 
 SalesforceCustomPropertyTypeValue = typing___NewType('SalesforceCustomPropertyTypeValue', builtin___int)
 type___SalesforceCustomPropertyTypeValue = SalesforceCustomPropertyTypeValue
 SalesforceCustomPropertyType: _SalesforceCustomPropertyType
 class _SalesforceCustomPropertyType(google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper[SalesforceCustomPropertyTypeValue]):
     DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
     SALESFORCE_CUSTOM_PROPERTY_UNSPECIFIED = typing___cast(SalesforceCustomPropertyTypeValue, 0)
@@ -119,14 +118,15 @@
 SALESFORCE_CUSTOM_PROPERTY_URL = typing___cast(SalesforceCustomPropertyTypeValue, 14)
 SALESFORCE_CUSTOM_PROPERTY_EMAIL = typing___cast(SalesforceCustomPropertyTypeValue, 15)
 SALESFORCE_CUSTOM_PROPERTY_COMBOBOX = typing___cast(SalesforceCustomPropertyTypeValue, 16)
 SALESFORCE_CUSTOM_PROPERTY_PICKLIST = typing___cast(SalesforceCustomPropertyTypeValue, 17)
 SALESFORCE_CUSTOM_PROPERTY_MULTI_PICKLIST = typing___cast(SalesforceCustomPropertyTypeValue, 18)
 SALESFORCE_CUSTOM_PROPERTY_ANY_TYPE = typing___cast(SalesforceCustomPropertyTypeValue, 19)
 SALESFORCE_CUSTOM_PROPERTY_LOCATION = typing___cast(SalesforceCustomPropertyTypeValue, 20)
+type___SalesforceCustomPropertyType = SalesforceCustomPropertyType
 
 HubSpotCompanyTypeValue = typing___NewType('HubSpotCompanyTypeValue', builtin___int)
 type___HubSpotCompanyTypeValue = HubSpotCompanyTypeValue
 HubSpotCompanyType: _HubSpotCompanyType
 class _HubSpotCompanyType(google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper[HubSpotCompanyTypeValue]):
     DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
     HUBSPOT_COMPANY_TYPE_UNSPECIFIED = typing___cast(HubSpotCompanyTypeValue, 0)
@@ -137,14 +137,15 @@
     HUBSPOT_COMPANY_TYPE_OTHER = typing___cast(HubSpotCompanyTypeValue, 5)
 HUBSPOT_COMPANY_TYPE_UNSPECIFIED = typing___cast(HubSpotCompanyTypeValue, 0)
 HUBSPOT_COMPANY_TYPE_PROSPECT = typing___cast(HubSpotCompanyTypeValue, 1)
 HUBSPOT_COMPANY_TYPE_PARTNER = typing___cast(HubSpotCompanyTypeValue, 2)
 HUBSPOT_COMPANY_TYPE_RESELLER = typing___cast(HubSpotCompanyTypeValue, 3)
 HUBSPOT_COMPANY_TYPE_VENDOR = typing___cast(HubSpotCompanyTypeValue, 4)
 HUBSPOT_COMPANY_TYPE_OTHER = typing___cast(HubSpotCompanyTypeValue, 5)
+type___HubSpotCompanyType = HubSpotCompanyType
 
 SalesloftCurrentStateValue = typing___NewType('SalesloftCurrentStateValue', builtin___int)
 type___SalesloftCurrentStateValue = SalesloftCurrentStateValue
 SalesloftCurrentState: _SalesloftCurrentState
 class _SalesloftCurrentState(google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper[SalesloftCurrentStateValue]):
     DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
     SALESLOFT_CURRENT_STATE_UNSPECIFIED = typing___cast(SalesloftCurrentStateValue, 0)
@@ -161,26 +162,28 @@
 SALESLOFT_CURRENT_STATE_STAGED = typing___cast(SalesloftCurrentStateValue, 2)
 SALESLOFT_CURRENT_STATE_ACTIVE = typing___cast(SalesloftCurrentStateValue, 3)
 SALESLOFT_CURRENT_STATE_SCHEDULED = typing___cast(SalesloftCurrentStateValue, 4)
 SALESLOFT_CURRENT_STATE_COMPLETED = typing___cast(SalesloftCurrentStateValue, 5)
 SALESLOFT_CURRENT_STATE_REMOVED = typing___cast(SalesloftCurrentStateValue, 6)
 SALESLOFT_CURRENT_STATE_REMOVED_NO_ACTION = typing___cast(SalesloftCurrentStateValue, 7)
 SALESLOFT_CURRENT_STATE_REASSIGNED = typing___cast(SalesloftCurrentStateValue, 8)
+type___SalesloftCurrentState = SalesloftCurrentState
 
 OutreachRelationshipTypeValue = typing___NewType('OutreachRelationshipTypeValue', builtin___int)
 type___OutreachRelationshipTypeValue = OutreachRelationshipTypeValue
 OutreachRelationshipType: _OutreachRelationshipType
 class _OutreachRelationshipType(google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper[OutreachRelationshipTypeValue]):
     DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
     OUTREACH_RELATIONSHIP_TYPE_UNSPECIFIED = typing___cast(OutreachRelationshipTypeValue, 0)
     OUTREACH_RELATIONSHIP_TYPE_PROSPECT = typing___cast(OutreachRelationshipTypeValue, 1)
     OUTREACH_RELATIONSHIP_TYPE_SEQUENCE = typing___cast(OutreachRelationshipTypeValue, 2)
 OUTREACH_RELATIONSHIP_TYPE_UNSPECIFIED = typing___cast(OutreachRelationshipTypeValue, 0)
 OUTREACH_RELATIONSHIP_TYPE_PROSPECT = typing___cast(OutreachRelationshipTypeValue, 1)
 OUTREACH_RELATIONSHIP_TYPE_SEQUENCE = typing___cast(OutreachRelationshipTypeValue, 2)
+type___OutreachRelationshipType = OutreachRelationshipType
 
 class CustomProperty(google___protobuf___message___Message):
     DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
     class FieldsEntry(google___protobuf___message___Message):
         DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
         key: typing___Text = ...
 
@@ -194,15 +197,15 @@
             ) -> None: ...
         def HasField(self, field_name: typing_extensions___Literal[u"value",b"value"]) -> builtin___bool: ...
         def ClearField(self, field_name: typing_extensions___Literal[u"key",b"key",u"value",b"value"]) -> None: ...
     type___FieldsEntry = FieldsEntry
 
 
     @property
-    def fields(self) -> google___protobuf___internal___containers___MessageMap[typing___Text, type___CustomPropertyValue]: ...
+    def fields(self) -> typing___MutableMapping[typing___Text, type___CustomPropertyValue]: ...
 
     def __init__(self,
         *,
         fields : typing___Optional[typing___Mapping[typing___Text, type___CustomPropertyValue]] = None,
         ) -> None: ...
     def ClearField(self, field_name: typing_extensions___Literal[u"fields",b"fields"]) -> None: ...
 type___CustomProperty = CustomProperty
@@ -660,15 +663,15 @@
         def HasField(self, field_name: typing_extensions___Literal[u"value",b"value"]) -> builtin___bool: ...
         def ClearField(self, field_name: typing_extensions___Literal[u"key",b"key",u"value",b"value"]) -> None: ...
     type___CustomPropertiesEntry = CustomPropertiesEntry
 
     salesforce_entity_type: typing___Text = ...
 
     @property
-    def custom_properties(self) -> google___protobuf___internal___containers___MessageMap[typing___Text, type___SalesforceCustomProperty]: ...
+    def custom_properties(self) -> typing___MutableMapping[typing___Text, type___SalesforceCustomProperty]: ...
 
     def __init__(self,
         *,
         salesforce_entity_type : typing___Optional[typing___Text] = None,
         custom_properties : typing___Optional[typing___Mapping[typing___Text, type___SalesforceCustomProperty]] = None,
         ) -> None: ...
     def ClearField(self, field_name: typing_extensions___Literal[u"custom_properties",b"custom_properties",u"salesforce_entity_type",b"salesforce_entity_type"]) -> None: ...
```

### Comparing `calixa-proto-py-2.0.8/calixa_proto_py/external_entities_relinking.proto` & `calixa-proto-py-2.0.9/calixa_proto_py/external_entities_relinking.proto`

 * *Files identical despite different names*

### Comparing `calixa-proto-py-2.0.8/calixa_proto_py/external_entities_relinking_pb2.pyi` & `calixa-proto-py-2.0.9/calixa_proto_py/external_entities_relinking_pb2.pyi`

 * *Files 3% similar despite different names*

```diff
@@ -1,11 +1,9 @@
-"""
-@generated by mypy-protobuf.  Do not edit manually!
-isort:skip_file
-"""
+# @generated by generate_proto_mypy_stubs.py.  Do not edit!
+import sys
 from common_pb2 import (
     EntityTypeValue as common_pb2___EntityTypeValue,
 )
 
 from entity_reference_pb2 import (
     EntityReference as entity_reference_pb2___EntityReference,
 )
```

### Comparing `calixa-proto-py-2.0.8/calixa_proto_py/import_log.proto` & `calixa-proto-py-2.0.9/calixa_proto_py/import_log.proto`

 * *Files identical despite different names*

### Comparing `calixa-proto-py-2.0.8/calixa_proto_py/import_log_pb2.pyi` & `calixa-proto-py-2.0.9/calixa_proto_py/import_log_pb2.pyi`

 * *Files 3% similar despite different names*

```diff
@@ -1,20 +1,17 @@
-"""
-@generated by mypy-protobuf.  Do not edit manually!
-isort:skip_file
-"""
+# @generated by generate_proto_mypy_stubs.py.  Do not edit!
+import sys
 from google.protobuf.descriptor import (
     Descriptor as google___protobuf___descriptor___Descriptor,
     EnumDescriptor as google___protobuf___descriptor___EnumDescriptor,
     FileDescriptor as google___protobuf___descriptor___FileDescriptor,
 )
 
 from google.protobuf.internal.containers import (
     RepeatedCompositeFieldContainer as google___protobuf___internal___containers___RepeatedCompositeFieldContainer,
-    ScalarMap as google___protobuf___internal___containers___ScalarMap,
 )
 
 from google.protobuf.internal.enum_type_wrapper import (
     _EnumTypeWrapper as google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper,
 )
 
 from google.protobuf.message import (
@@ -28,14 +25,15 @@
 from integration_pb2 import (
     Integration as integration_pb2___Integration,
 )
 
 from typing import (
     Iterable as typing___Iterable,
     Mapping as typing___Mapping,
+    MutableMapping as typing___MutableMapping,
     NewType as typing___NewType,
     Optional as typing___Optional,
     Text as typing___Text,
     cast as typing___cast,
 )
 
 from typing_extensions import (
@@ -58,14 +56,15 @@
     DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
     IMPORT_LOG_STATUS_UNSPECIFIED = typing___cast(ImportLogStatusValue, 0)
     IMPORT_LOG_STATUS_SUCCESS = typing___cast(ImportLogStatusValue, 1)
     IMPORT_LOG_STATUS_FAILURE_GENERIC = typing___cast(ImportLogStatusValue, 2)
 IMPORT_LOG_STATUS_UNSPECIFIED = typing___cast(ImportLogStatusValue, 0)
 IMPORT_LOG_STATUS_SUCCESS = typing___cast(ImportLogStatusValue, 1)
 IMPORT_LOG_STATUS_FAILURE_GENERIC = typing___cast(ImportLogStatusValue, 2)
+type___ImportLogStatus = ImportLogStatus
 
 class ImportLog(google___protobuf___message___Message):
     DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
     class AdditionalInformationEntry(google___protobuf___message___Message):
         DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
         key: typing___Text = ...
         value: typing___Text = ...
@@ -85,15 +84,15 @@
     @property
     def import_started_at(self) -> google___protobuf___timestamp_pb2___Timestamp: ...
 
     @property
     def integration(self) -> integration_pb2___Integration: ...
 
     @property
-    def additional_information(self) -> google___protobuf___internal___containers___ScalarMap[typing___Text, typing___Text]: ...
+    def additional_information(self) -> typing___MutableMapping[typing___Text, typing___Text]: ...
 
     def __init__(self,
         *,
         status : typing___Optional[type___ImportLogStatusValue] = None,
         status_message : typing___Optional[typing___Text] = None,
         import_started_at : typing___Optional[google___protobuf___timestamp_pb2___Timestamp] = None,
         duration_seconds : typing___Optional[builtin___int] = None,
```

### Comparing `calixa-proto-py-2.0.8/calixa_proto_py/import_log_pb2_grpc.py` & `calixa-proto-py-2.0.9/calixa_proto_py/import_log_pb2_grpc.py`

 * *Files identical despite different names*

### Comparing `calixa-proto-py-2.0.8/calixa_proto_py/integration.proto` & `calixa-proto-py-2.0.9/calixa_proto_py/integration.proto`

 * *Files identical despite different names*

### Comparing `calixa-proto-py-2.0.8/calixa_proto_py/integration_datawarehouse_pb2.py` & `calixa-proto-py-2.0.9/calixa_proto_py/integration_datawarehouse_pb2.py`

 * *Files 22% similar despite different names*

```diff
@@ -1,13 +1,12 @@
 # -*- coding: utf-8 -*-
 # Generated by the protocol buffer compiler.  DO NOT EDIT!
 # source: integration_datawarehouse.proto
 """Generated protocol buffer code."""
 from google.protobuf import descriptor as _descriptor
-from google.protobuf import descriptor_pool as _descriptor_pool
 from google.protobuf import message as _message
 from google.protobuf import reflection as _reflection
 from google.protobuf import symbol_database as _symbol_database
 # @@protoc_insertion_point(imports)
 
 _sym_db = _symbol_database.Default()
 
@@ -16,16 +15,24 @@
 from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
 import integration_source_pb2 as integration__source__pb2
 import integration_pb2 as integration__pb2
 import common_pb2 as common__pb2
 import entity_pb2 as entity__pb2
 
 
-DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1fintegration_datawarehouse.proto\x12#calixa.domain.integration.warehouse\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x18integration_source.proto\x1a\x11integration.proto\x1a\x0c\x63ommon.proto\x1a\x0c\x65ntity.protoB)\n#io.calixa.integration.datawarehouseH\x01P\x01\x62\x06proto3')
+DESCRIPTOR = _descriptor.FileDescriptor(
+  name='integration_datawarehouse.proto',
+  package='calixa.domain.integration.warehouse',
+  syntax='proto3',
+  serialized_options=b'\n#io.calixa.integration.datawarehouseH\001P\001',
+  create_key=_descriptor._internal_create_key,
+  serialized_pb=b'\n\x1fintegration_datawarehouse.proto\x12#calixa.domain.integration.warehouse\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x18integration_source.proto\x1a\x11integration.proto\x1a\x0c\x63ommon.proto\x1a\x0c\x65ntity.protoB)\n#io.calixa.integration.datawarehouseH\x01P\x01\x62\x06proto3'
+  ,
+  dependencies=[google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,integration__source__pb2.DESCRIPTOR,integration__pb2.DESCRIPTOR,common__pb2.DESCRIPTOR,entity__pb2.DESCRIPTOR,])
 
 
 
-if _descriptor._USE_C_DESCRIPTORS == False:
+_sym_db.RegisterFileDescriptor(DESCRIPTOR)
 
-  DESCRIPTOR._options = None
-  DESCRIPTOR._serialized_options = b'\n#io.calixa.integration.datawarehouseH\001P\001'
+
+DESCRIPTOR._options = None
 # @@protoc_insertion_point(module_scope)
```

### Comparing `calixa-proto-py-2.0.8/calixa_proto_py/integration_elt.proto` & `calixa-proto-py-2.0.9/calixa_proto_py/integration_elt.proto`

 * *Files identical despite different names*

### Comparing `calixa-proto-py-2.0.8/calixa_proto_py/integration_elt_pb2.pyi` & `calixa-proto-py-2.0.9/calixa_proto_py/integration_elt_pb2.pyi`

 * *Files 1% similar despite different names*

```diff
@@ -1,11 +1,9 @@
-"""
-@generated by mypy-protobuf.  Do not edit manually!
-isort:skip_file
-"""
+# @generated by generate_proto_mypy_stubs.py.  Do not edit!
+import sys
 from common_pb2 import (
     ExternalId as common_pb2___ExternalId,
     RequestContext as common_pb2___RequestContext,
 )
 
 from entity_pb2 import (
     Entity as entity_pb2___Entity,
@@ -66,14 +64,15 @@
     LOAD_MUTATION_TYPE_PUT_ENTITY = typing___cast(LoadMutationTypeValue, 1)
     LOAD_MUTATION_TYPE_PATCH_ENTITY = typing___cast(LoadMutationTypeValue, 2)
     LOAD_MUTATION_TYPE_EVINCE_EVENT = typing___cast(LoadMutationTypeValue, 3)
 LOAD_MUTATION_TYPE_UNSPECIFIED = typing___cast(LoadMutationTypeValue, 0)
 LOAD_MUTATION_TYPE_PUT_ENTITY = typing___cast(LoadMutationTypeValue, 1)
 LOAD_MUTATION_TYPE_PATCH_ENTITY = typing___cast(LoadMutationTypeValue, 2)
 LOAD_MUTATION_TYPE_EVINCE_EVENT = typing___cast(LoadMutationTypeValue, 3)
+type___LoadMutationType = LoadMutationType
 
 class ExtractedEntity(google___protobuf___message___Message):
     DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
     organization_id: typing___Text = ...
     instance_id: typing___Text = ...
     data_warehouse_sync_id: typing___Text = ...
     source: integration_source_pb2___IntegrationSourceValue = ...
```

### Comparing `calixa-proto-py-2.0.8/calixa_proto_py/integration_manager.proto` & `calixa-proto-py-2.0.9/calixa_proto_py/integration_manager.proto`

 * *Files identical despite different names*

### Comparing `calixa-proto-py-2.0.8/calixa_proto_py/integration_manager_pb2.pyi` & `calixa-proto-py-2.0.9/calixa_proto_py/integration_manager_pb2.pyi`

 * *Files 1% similar despite different names*

```diff
@@ -1,11 +1,9 @@
-"""
-@generated by mypy-protobuf.  Do not edit manually!
-isort:skip_file
-"""
+# @generated by generate_proto_mypy_stubs.py.  Do not edit!
+import sys
 from common_pb2 import (
     EntityTypeValue as common_pb2___EntityTypeValue,
 )
 
 from google.protobuf.descriptor import (
     Descriptor as google___protobuf___descriptor___Descriptor,
     EnumDescriptor as google___protobuf___descriptor___EnumDescriptor,
@@ -72,38 +70,41 @@
     DELETE_INTEGRATION_STATUS_SUCCESS = typing___cast(DeleteIntegrationStatusValue, 1)
     DELETE_INTEGRATION_STATUS_FAILURE = typing___cast(DeleteIntegrationStatusValue, 2)
     DELETE_INTEGRATION_STATUS_CONFLICT = typing___cast(DeleteIntegrationStatusValue, 3)
 DELETE_INTEGRATION_STATUS_UNSPECIFIED = typing___cast(DeleteIntegrationStatusValue, 0)
 DELETE_INTEGRATION_STATUS_SUCCESS = typing___cast(DeleteIntegrationStatusValue, 1)
 DELETE_INTEGRATION_STATUS_FAILURE = typing___cast(DeleteIntegrationStatusValue, 2)
 DELETE_INTEGRATION_STATUS_CONFLICT = typing___cast(DeleteIntegrationStatusValue, 3)
+type___DeleteIntegrationStatus = DeleteIntegrationStatus
 
 PublishBackfillTaskStatusValue = typing___NewType('PublishBackfillTaskStatusValue', builtin___int)
 type___PublishBackfillTaskStatusValue = PublishBackfillTaskStatusValue
 PublishBackfillTaskStatus: _PublishBackfillTaskStatus
 class _PublishBackfillTaskStatus(google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper[PublishBackfillTaskStatusValue]):
     DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
     PUBLISH_BACKFILL_TASK_STATUS_UNSPECIFIED = typing___cast(PublishBackfillTaskStatusValue, 0)
     PUBLISH_BACKFILL_TASK_STATUS_SUCCESS = typing___cast(PublishBackfillTaskStatusValue, 1)
     PUBLISH_BACKFILL_TASK_STATUS_FAILURE = typing___cast(PublishBackfillTaskStatusValue, 2)
 PUBLISH_BACKFILL_TASK_STATUS_UNSPECIFIED = typing___cast(PublishBackfillTaskStatusValue, 0)
 PUBLISH_BACKFILL_TASK_STATUS_SUCCESS = typing___cast(PublishBackfillTaskStatusValue, 1)
 PUBLISH_BACKFILL_TASK_STATUS_FAILURE = typing___cast(PublishBackfillTaskStatusValue, 2)
+type___PublishBackfillTaskStatus = PublishBackfillTaskStatus
 
 IntegrationConfigValueTypeValue = typing___NewType('IntegrationConfigValueTypeValue', builtin___int)
 type___IntegrationConfigValueTypeValue = IntegrationConfigValueTypeValue
 IntegrationConfigValueType: _IntegrationConfigValueType
 class _IntegrationConfigValueType(google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper[IntegrationConfigValueTypeValue]):
     DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
     INTEGRATION_CONFIG_VALUE_TYPE_UNSPECIFIED = typing___cast(IntegrationConfigValueTypeValue, 0)
     INTEGRATION_CONFIG_VALUE_TYPE_STRING = typing___cast(IntegrationConfigValueTypeValue, 1)
     INTEGRATION_CONFIG_VALUE_TYPE_LONG = typing___cast(IntegrationConfigValueTypeValue, 2)
 INTEGRATION_CONFIG_VALUE_TYPE_UNSPECIFIED = typing___cast(IntegrationConfigValueTypeValue, 0)
 INTEGRATION_CONFIG_VALUE_TYPE_STRING = typing___cast(IntegrationConfigValueTypeValue, 1)
 INTEGRATION_CONFIG_VALUE_TYPE_LONG = typing___cast(IntegrationConfigValueTypeValue, 2)
+type___IntegrationConfigValueType = IntegrationConfigValueType
 
 class PublishBackfillTasksRequest(google___protobuf___message___Message):
     DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
     source: integration_source_pb2___IntegrationSourceValue = ...
     entity_types_to_backfill: google___protobuf___internal___containers___RepeatedScalarFieldContainer[common_pb2___EntityTypeValue] = ...
     integration_selection_window_in_minutes: builtin___int = ...
```

### Comparing `calixa-proto-py-2.0.8/calixa_proto_py/integration_manager_pb2_grpc.py` & `calixa-proto-py-2.0.9/calixa_proto_py/integration_manager_pb2_grpc.py`

 * *Files identical despite different names*

### Comparing `calixa-proto-py-2.0.8/calixa_proto_py/integration_pb2.pyi` & `calixa-proto-py-2.0.9/calixa_proto_py/integration_pb2.pyi`

 * *Files 1% similar despite different names*

```diff
@@ -1,11 +1,9 @@
-"""
-@generated by mypy-protobuf.  Do not edit manually!
-isort:skip_file
-"""
+# @generated by generate_proto_mypy_stubs.py.  Do not edit!
+import sys
 from action_pb2 import (
     ActionInvocationStatusValue as action_pb2___ActionInvocationStatusValue,
     ActionParams as action_pb2___ActionParams,
     ThirdPartyActionInvocationResponse as action_pb2___ThirdPartyActionInvocationResponse,
 )
 
 from common_pb2 import (
@@ -21,15 +19,14 @@
     EnumDescriptor as google___protobuf___descriptor___EnumDescriptor,
     FileDescriptor as google___protobuf___descriptor___FileDescriptor,
 )
 
 from google.protobuf.internal.containers import (
     RepeatedCompositeFieldContainer as google___protobuf___internal___containers___RepeatedCompositeFieldContainer,
     RepeatedScalarFieldContainer as google___protobuf___internal___containers___RepeatedScalarFieldContainer,
-    ScalarMap as google___protobuf___internal___containers___ScalarMap,
 )
 
 from google.protobuf.internal.enum_type_wrapper import (
     _EnumTypeWrapper as google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper,
 )
 
 from google.protobuf.message import (
@@ -55,14 +52,15 @@
     RelatedData as related_data_pb2___RelatedData,
     RelatedDataTypeValue as related_data_pb2___RelatedDataTypeValue,
 )
 
 from typing import (
     Iterable as typing___Iterable,
     Mapping as typing___Mapping,
+    MutableMapping as typing___MutableMapping,
     NewType as typing___NewType,
     Optional as typing___Optional,
     Text as typing___Text,
     cast as typing___cast,
 )
 
 from typing_extensions import (
@@ -87,78 +85,84 @@
     INTEGRATION_STATUS_ENABLED = typing___cast(IntegrationStatusValue, 1)
     INTEGRATION_STATUS_PAUSED = typing___cast(IntegrationStatusValue, 3)
     INTEGRATION_STATUS_FAILED = typing___cast(IntegrationStatusValue, 4)
 INTEGRATION_STATUS_UNSPECIFIED = typing___cast(IntegrationStatusValue, 0)
 INTEGRATION_STATUS_ENABLED = typing___cast(IntegrationStatusValue, 1)
 INTEGRATION_STATUS_PAUSED = typing___cast(IntegrationStatusValue, 3)
 INTEGRATION_STATUS_FAILED = typing___cast(IntegrationStatusValue, 4)
+type___IntegrationStatus = IntegrationStatus
 
 OAuthFinalizedStatusValue = typing___NewType('OAuthFinalizedStatusValue', builtin___int)
 type___OAuthFinalizedStatusValue = OAuthFinalizedStatusValue
 OAuthFinalizedStatus: _OAuthFinalizedStatus
 class _OAuthFinalizedStatus(google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper[OAuthFinalizedStatusValue]):
     DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
     OAUTH_FINALIZED_STATUS_UNSPECIFIED = typing___cast(OAuthFinalizedStatusValue, 0)
     OAUTH_FINALIZED_STATUS_SUCCESS = typing___cast(OAuthFinalizedStatusValue, 1)
     OAUTH_FINALIZED_STATUS_ACCESS_DENIED = typing___cast(OAuthFinalizedStatusValue, 2)
 OAUTH_FINALIZED_STATUS_UNSPECIFIED = typing___cast(OAuthFinalizedStatusValue, 0)
 OAUTH_FINALIZED_STATUS_SUCCESS = typing___cast(OAuthFinalizedStatusValue, 1)
 OAUTH_FINALIZED_STATUS_ACCESS_DENIED = typing___cast(OAuthFinalizedStatusValue, 2)
+type___OAuthFinalizedStatus = OAuthFinalizedStatus
 
 HealthCheckStatusValue = typing___NewType('HealthCheckStatusValue', builtin___int)
 type___HealthCheckStatusValue = HealthCheckStatusValue
 HealthCheckStatus: _HealthCheckStatus
 class _HealthCheckStatus(google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper[HealthCheckStatusValue]):
     DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
     HEALTH_CHECK_STATE_UNSPECIFIED = typing___cast(HealthCheckStatusValue, 0)
     HEALTH_CHECK_STATE_OK = typing___cast(HealthCheckStatusValue, 1)
     HEALTH_CHECK_STATE_UNHEALTHY = typing___cast(HealthCheckStatusValue, 2)
 HEALTH_CHECK_STATE_UNSPECIFIED = typing___cast(HealthCheckStatusValue, 0)
 HEALTH_CHECK_STATE_OK = typing___cast(HealthCheckStatusValue, 1)
 HEALTH_CHECK_STATE_UNHEALTHY = typing___cast(HealthCheckStatusValue, 2)
+type___HealthCheckStatus = HealthCheckStatus
 
 CredentialsStatusValue = typing___NewType('CredentialsStatusValue', builtin___int)
 type___CredentialsStatusValue = CredentialsStatusValue
 CredentialsStatus: _CredentialsStatus
 class _CredentialsStatus(google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper[CredentialsStatusValue]):
     DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
     CREDENTIALS_STATUS_UNSPECIFIED = typing___cast(CredentialsStatusValue, 0)
     CREDENTIALS_STATUS_OK = typing___cast(CredentialsStatusValue, 1)
     CREDENTIALS_STATUS_REJECTED = typing___cast(CredentialsStatusValue, 2)
 CREDENTIALS_STATUS_UNSPECIFIED = typing___cast(CredentialsStatusValue, 0)
 CREDENTIALS_STATUS_OK = typing___cast(CredentialsStatusValue, 1)
 CREDENTIALS_STATUS_REJECTED = typing___cast(CredentialsStatusValue, 2)
+type___CredentialsStatus = CredentialsStatus
 
 InstallStatusValue = typing___NewType('InstallStatusValue', builtin___int)
 type___InstallStatusValue = InstallStatusValue
 InstallStatus: _InstallStatus
 class _InstallStatus(google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper[InstallStatusValue]):
     DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
     INSTALL_STATUS_UNSPECIFIED = typing___cast(InstallStatusValue, 0)
     INSTALL_STATUS_OK = typing___cast(InstallStatusValue, 1)
     INSTALL_STATUS_FAILED = typing___cast(InstallStatusValue, 2)
     INSTALL_STATUS_DUPLICATE = typing___cast(InstallStatusValue, 3)
 INSTALL_STATUS_UNSPECIFIED = typing___cast(InstallStatusValue, 0)
 INSTALL_STATUS_OK = typing___cast(InstallStatusValue, 1)
 INSTALL_STATUS_FAILED = typing___cast(InstallStatusValue, 2)
 INSTALL_STATUS_DUPLICATE = typing___cast(InstallStatusValue, 3)
+type___InstallStatus = InstallStatus
 
 UninstallStatusValue = typing___NewType('UninstallStatusValue', builtin___int)
 type___UninstallStatusValue = UninstallStatusValue
 UninstallStatus: _UninstallStatus
 class _UninstallStatus(google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper[UninstallStatusValue]):
     DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
     UNINSTALL_STATUS_UNSPECIFIED = typing___cast(UninstallStatusValue, 0)
     UNINSTALL_STATUS_SUCCESS = typing___cast(UninstallStatusValue, 1)
     UNINSTALL_STATUS_FAILURE = typing___cast(UninstallStatusValue, 2)
     UNINSTALL_STATUS_NOOP = typing___cast(UninstallStatusValue, 3)
 UNINSTALL_STATUS_UNSPECIFIED = typing___cast(UninstallStatusValue, 0)
 UNINSTALL_STATUS_SUCCESS = typing___cast(UninstallStatusValue, 1)
 UNINSTALL_STATUS_FAILURE = typing___cast(UninstallStatusValue, 2)
 UNINSTALL_STATUS_NOOP = typing___cast(UninstallStatusValue, 3)
+type___UninstallStatus = UninstallStatus
 
 BackfillTaskStatusValue = typing___NewType('BackfillTaskStatusValue', builtin___int)
 type___BackfillTaskStatusValue = BackfillTaskStatusValue
 BackfillTaskStatus: _BackfillTaskStatus
 class _BackfillTaskStatus(google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper[BackfillTaskStatusValue]):
     DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
     BACKFILL_TASK_STATUS_UNSPECIFIED = typing___cast(BackfillTaskStatusValue, 0)
@@ -177,42 +181,45 @@
 BACKFILL_TASK_STATUS_SUCCESS = typing___cast(BackfillTaskStatusValue, 3)
 BACKFILL_TASK_STATUS_ERROR_UNSUPPORTED = typing___cast(BackfillTaskStatusValue, 4)
 BACKFILL_TASK_STATUS_ERROR_UNKNOWN = typing___cast(BackfillTaskStatusValue, 5)
 BACKFILL_TASK_STATUS_ERROR_PLATFORM = typing___cast(BackfillTaskStatusValue, 6)
 BACKFILL_TASK_STATUS_ERROR_THIRD_PARTY_API = typing___cast(BackfillTaskStatusValue, 7)
 BACKFILL_TASK_STATUS_ERROR_INVALID_CREDENTIALS = typing___cast(BackfillTaskStatusValue, 8)
 BACKFILL_TASK_STATUS_ERROR_THROTTLED = typing___cast(BackfillTaskStatusValue, 9)
+type___BackfillTaskStatus = BackfillTaskStatus
 
 CursorStatusValue = typing___NewType('CursorStatusValue', builtin___int)
 type___CursorStatusValue = CursorStatusValue
 CursorStatus: _CursorStatus
 class _CursorStatus(google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper[CursorStatusValue]):
     DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
     CURSOR_STATUS_UNSPECIFIED = typing___cast(CursorStatusValue, 0)
     CURSOR_STATUS_PROCESSED = typing___cast(CursorStatusValue, 1)
     CURSOR_STATUS_ERROR = typing___cast(CursorStatusValue, 2)
     CURSOR_STATUS_PENDING = typing___cast(CursorStatusValue, 3)
 CURSOR_STATUS_UNSPECIFIED = typing___cast(CursorStatusValue, 0)
 CURSOR_STATUS_PROCESSED = typing___cast(CursorStatusValue, 1)
 CURSOR_STATUS_ERROR = typing___cast(CursorStatusValue, 2)
 CURSOR_STATUS_PENDING = typing___cast(CursorStatusValue, 3)
+type___CursorStatus = CursorStatus
 
 RefreshTokensStatusValue = typing___NewType('RefreshTokensStatusValue', builtin___int)
 type___RefreshTokensStatusValue = RefreshTokensStatusValue
 RefreshTokensStatus: _RefreshTokensStatus
 class _RefreshTokensStatus(google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper[RefreshTokensStatusValue]):
     DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
     REFRESH_TOKENS_STATUS_UNSPECIFIED = typing___cast(RefreshTokensStatusValue, 0)
     REFRESH_TOKENS_STATUS_SUCCESS = typing___cast(RefreshTokensStatusValue, 1)
     REFRESH_TOKENS_ACCESS_DENIED = typing___cast(RefreshTokensStatusValue, 2)
     REFRESH_TOKENS_FAILED = typing___cast(RefreshTokensStatusValue, 3)
 REFRESH_TOKENS_STATUS_UNSPECIFIED = typing___cast(RefreshTokensStatusValue, 0)
 REFRESH_TOKENS_STATUS_SUCCESS = typing___cast(RefreshTokensStatusValue, 1)
 REFRESH_TOKENS_ACCESS_DENIED = typing___cast(RefreshTokensStatusValue, 2)
 REFRESH_TOKENS_FAILED = typing___cast(RefreshTokensStatusValue, 3)
+type___RefreshTokensStatus = RefreshTokensStatus
 
 class BigQueryCredentials(google___protobuf___message___Message):
     DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
     project_id: typing___Text = ...
 
     def __init__(self,
         *,
@@ -326,15 +333,15 @@
     channel: integration_source_pb2___IntegrationChannelValue = ...
     store: integration_source_pb2___IntegrationStoreValue = ...
 
     @property
     def credentials(self) -> type___Credentials: ...
 
     @property
-    def properties(self) -> google___protobuf___internal___containers___ScalarMap[typing___Text, typing___Text]: ...
+    def properties(self) -> typing___MutableMapping[typing___Text, typing___Text]: ...
 
     @property
     def installed_at(self) -> google___protobuf___timestamp_pb2___Timestamp: ...
 
     @property
     def created_at(self) -> google___protobuf___timestamp_pb2___Timestamp: ...
 
@@ -456,15 +463,15 @@
         def ClearField(self, field_name: typing_extensions___Literal[u"key",b"key",u"value",b"value"]) -> None: ...
     type___QueryParametersEntry = QueryParametersEntry
 
     json_encoded_post_params: typing___Text = ...
     redirect_uri: typing___Text = ...
 
     @property
-    def query_parameters(self) -> google___protobuf___internal___containers___ScalarMap[typing___Text, typing___Text]: ...
+    def query_parameters(self) -> typing___MutableMapping[typing___Text, typing___Text]: ...
 
     @property
     def integration(self) -> type___Integration: ...
 
     def __init__(self,
         *,
         query_parameters : typing___Optional[typing___Mapping[typing___Text, typing___Text]] = None,
@@ -553,15 +560,15 @@
     type___ConnectionIdsEntry = ConnectionIdsEntry
 
     workspace_id: typing___Text = ...
     source_id: typing___Text = ...
     sync_frequency_millis: builtin___int = ...
 
     @property
-    def connection_ids(self) -> google___protobuf___internal___containers___ScalarMap[typing___Text, typing___Text]: ...
+    def connection_ids(self) -> typing___MutableMapping[typing___Text, typing___Text]: ...
 
     def __init__(self,
         *,
         workspace_id : typing___Optional[typing___Text] = None,
         source_id : typing___Optional[typing___Text] = None,
         connection_ids : typing___Optional[typing___Mapping[typing___Text, typing___Text]] = None,
         sync_frequency_millis : typing___Optional[builtin___int] = None,
```

### Comparing `calixa-proto-py-2.0.8/calixa_proto_py/integration_pb2_grpc.py` & `calixa-proto-py-2.0.9/calixa_proto_py/integration_pb2_grpc.py`

 * *Files identical despite different names*

### Comparing `calixa-proto-py-2.0.8/calixa_proto_py/integration_source.proto` & `calixa-proto-py-2.0.9/calixa_proto_py/integration_source.proto`

 * *Files 4% similar despite different names*

```diff
@@ -23,14 +23,15 @@
   INTEGRATION_SOURCE_HUBSPOT = 12;
   INTEGRATION_SOURCE_GOOGLE_FIREBASE = 13;
   INTEGRATION_SOURCE_SLACK = 14;
   INTEGRATION_SOURCE_SALESLOFT = 15;
   INTEGRATION_SOURCE_OUTREACH = 16;
   INTEGRATION_SOURCE_CLEARBIT = 17;
   INTEGRATION_SOURCE_AMPLITUDE = 18;
+  INTEGRATION_SOURCE_MIXPANEL = 19;
 
   INTEGRATION_SOURCE_AUTO_METRICS = 536870907;
 
   INTEGRATION_SOURCE_ORGANIZATION = 536870908 [deprecated = true];
 
   // Special case: This represents an email address -- this is UNIVERSAL
   INTEGRATION_SOURCE_UNIVERSAL_EMAIL = 536870909;
```

### Comparing `calixa-proto-py-2.0.8/calixa_proto_py/integration_source_pb2.pyi` & `calixa-proto-py-2.0.9/calixa_proto_py/integration_source_pb2.pyi`

 * *Files 4% similar despite different names*

```diff
@@ -1,11 +1,9 @@
-"""
-@generated by mypy-protobuf.  Do not edit manually!
-isort:skip_file
-"""
+# @generated by generate_proto_mypy_stubs.py.  Do not edit!
+import sys
 from google.protobuf.descriptor import (
     EnumDescriptor as google___protobuf___descriptor___EnumDescriptor,
     FileDescriptor as google___protobuf___descriptor___FileDescriptor,
 )
 
 from google.protobuf.internal.enum_type_wrapper import (
     _EnumTypeWrapper as google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper,
@@ -45,14 +43,15 @@
     INTEGRATION_SOURCE_HUBSPOT = typing___cast(IntegrationSourceValue, 12)
     INTEGRATION_SOURCE_GOOGLE_FIREBASE = typing___cast(IntegrationSourceValue, 13)
     INTEGRATION_SOURCE_SLACK = typing___cast(IntegrationSourceValue, 14)
     INTEGRATION_SOURCE_SALESLOFT = typing___cast(IntegrationSourceValue, 15)
     INTEGRATION_SOURCE_OUTREACH = typing___cast(IntegrationSourceValue, 16)
     INTEGRATION_SOURCE_CLEARBIT = typing___cast(IntegrationSourceValue, 17)
     INTEGRATION_SOURCE_AMPLITUDE = typing___cast(IntegrationSourceValue, 18)
+    INTEGRATION_SOURCE_MIXPANEL = typing___cast(IntegrationSourceValue, 19)
     INTEGRATION_SOURCE_AUTO_METRICS = typing___cast(IntegrationSourceValue, 536870907)
     INTEGRATION_SOURCE_ORGANIZATION = typing___cast(IntegrationSourceValue, 536870908)
     INTEGRATION_SOURCE_UNIVERSAL_EMAIL = typing___cast(IntegrationSourceValue, 536870909)
     INTEGRATION_SOURCE_CALIXA_CONSOLE = typing___cast(IntegrationSourceValue, 536870910)
     INTEGRATION_SOURCE_CALIXA_API = typing___cast(IntegrationSourceValue, 536870911)
 INTEGRATION_SOURCE_UNSPECIFIED = typing___cast(IntegrationSourceValue, 0)
 INTEGRATION_SOURCE_STRIPE = typing___cast(IntegrationSourceValue, 1)
@@ -68,33 +67,36 @@
 INTEGRATION_SOURCE_HUBSPOT = typing___cast(IntegrationSourceValue, 12)
 INTEGRATION_SOURCE_GOOGLE_FIREBASE = typing___cast(IntegrationSourceValue, 13)
 INTEGRATION_SOURCE_SLACK = typing___cast(IntegrationSourceValue, 14)
 INTEGRATION_SOURCE_SALESLOFT = typing___cast(IntegrationSourceValue, 15)
 INTEGRATION_SOURCE_OUTREACH = typing___cast(IntegrationSourceValue, 16)
 INTEGRATION_SOURCE_CLEARBIT = typing___cast(IntegrationSourceValue, 17)
 INTEGRATION_SOURCE_AMPLITUDE = typing___cast(IntegrationSourceValue, 18)
+INTEGRATION_SOURCE_MIXPANEL = typing___cast(IntegrationSourceValue, 19)
 INTEGRATION_SOURCE_AUTO_METRICS = typing___cast(IntegrationSourceValue, 536870907)
 INTEGRATION_SOURCE_ORGANIZATION = typing___cast(IntegrationSourceValue, 536870908)
 INTEGRATION_SOURCE_UNIVERSAL_EMAIL = typing___cast(IntegrationSourceValue, 536870909)
 INTEGRATION_SOURCE_CALIXA_CONSOLE = typing___cast(IntegrationSourceValue, 536870910)
 INTEGRATION_SOURCE_CALIXA_API = typing___cast(IntegrationSourceValue, 536870911)
+type___IntegrationSource = IntegrationSource
 
 IntegrationStoreValue = typing___NewType('IntegrationStoreValue', builtin___int)
 type___IntegrationStoreValue = IntegrationStoreValue
 IntegrationStore: _IntegrationStore
 class _IntegrationStore(google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper[IntegrationStoreValue]):
     DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
     INTEGRATION_STORE_UNSPECIFIED = typing___cast(IntegrationStoreValue, 0)
     INTEGRATION_STORE_BIGQUERY = typing___cast(IntegrationStoreValue, 1)
     INTEGRATION_STORE_SNOWFLAKE = typing___cast(IntegrationStoreValue, 2)
     INTEGRATION_STORE_REDSHIFT = typing___cast(IntegrationStoreValue, 3)
 INTEGRATION_STORE_UNSPECIFIED = typing___cast(IntegrationStoreValue, 0)
 INTEGRATION_STORE_BIGQUERY = typing___cast(IntegrationStoreValue, 1)
 INTEGRATION_STORE_SNOWFLAKE = typing___cast(IntegrationStoreValue, 2)
 INTEGRATION_STORE_REDSHIFT = typing___cast(IntegrationStoreValue, 3)
+type___IntegrationStore = IntegrationStore
 
 IntegrationChannelValue = typing___NewType('IntegrationChannelValue', builtin___int)
 type___IntegrationChannelValue = IntegrationChannelValue
 IntegrationChannel: _IntegrationChannel
 class _IntegrationChannel(google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper[IntegrationChannelValue]):
     DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
     INTEGRATION_CHANNEL_UNSPECIFIED = typing___cast(IntegrationChannelValue, 0)
@@ -103,7 +105,8 @@
     INTEGRATION_CHANNEL_CENSUS = typing___cast(IntegrationChannelValue, 4)
     INTEGRATION_CHANNEL_INTERNAL = typing___cast(IntegrationChannelValue, 5)
 INTEGRATION_CHANNEL_UNSPECIFIED = typing___cast(IntegrationChannelValue, 0)
 INTEGRATION_CHANNEL_DIRECT = typing___cast(IntegrationChannelValue, 1)
 INTEGRATION_CHANNEL_AIRBYTE = typing___cast(IntegrationChannelValue, 3)
 INTEGRATION_CHANNEL_CENSUS = typing___cast(IntegrationChannelValue, 4)
 INTEGRATION_CHANNEL_INTERNAL = typing___cast(IntegrationChannelValue, 5)
+type___IntegrationChannel = IntegrationChannel
```

### Comparing `calixa-proto-py-2.0.8/calixa_proto_py/learning.proto` & `calixa-proto-py-2.0.9/calixa_proto_py/learning.proto`

 * *Files 13% similar despite different names*

```diff
@@ -33,16 +33,14 @@
   // unique identifier of a feature, should also be descriptive
   string id = 1;
   // longer description, explanation
   string description = 2;
   // Can the model "learn" on this feature? By default, no
   bool learnable = 3;
   FeatureValueType type = 4;
-  // which entity type this feature is describing
-  calixa.domain.common.EntityType entity_type = 5;
 }
 
 // TODO(freds): Add validations
 message FeatureValue {
   // having a ref as opposed to FeatureDef might be more efficient if we use this in the BEAM job
   // FeatureDef def = 1;
   string feature_id = 1;
@@ -63,18 +61,22 @@
 
 /**
  * Defines a PredictionTask: which models and which features for each models.
  * A collection of these messages represent the 'prediction_task_definitions' for a given organization_id
  * and it is stored in organization.proto:Settings
  */
 message PredictionTaskDefinition {
+  string prediction_id = 100;
   PredictionTask prediction_task = 1;
   repeated ModelDefinition model_definitions = 2;
+  // which entity type this task for?
+  calixa.domain.common.EntityType entity_type = 3;
   // here we can define also how to combine 'model_definitions'
   // e.g. "combine 0-2 with Combiner x, 3-4 with Combiner Y"
+  // TODO(glg): define possible outputs. E.g. type: boolean, or enumeration: ["dog", "cat"]
 }
 
 /**
  * Captures the required 'features' for each 'model_type'.
  * We could also add BQ model's options here.
  */
 message ModelDefinition {
@@ -113,46 +115,55 @@
   PredictionTask prediction_task = 1;
   TaskLabelSource label_source = 2;
   google.protobuf.Value label = 3;
   google.protobuf.Timestamp created_at = 4;
 }
 
 /**
- * Models the 'predicted_label' (string/number/list) for a given PredictionTask.
- * A 'predicted_label' is computed by combining 1 or more TaskModelPrediction(s) ('model_predictions').
- */
-message PredictionTaskResult {
-  PredictionTask prediction_task = 1;
-  // This is computed by combining the corresponding 'model_predictions'
-  google.protobuf.Value predicted_label = 2;
-  google.protobuf.Timestamp created_at = 3;
-  repeated TaskModelPrediction model_predictions = 4;
-}
-
-/**
- * The output of a specific 'model_id's prediction.
+ * The output of a specific  PredictionTask.
  * This data is also stored in BigQuery as the output of a specific model.
  */
 message TaskModelPrediction {
-  string model_id = 1;
-  google.protobuf.Value label = 2;
-  google.protobuf.Value predicted_label = 3;
-  float probability = 4;
-  map<string, float> top_feature_attributions = 5;
-}
-
-/**
- * Top-level message representing all available TaskResult(s) for a given 'entity_reference'.
- * This data is also stored in BigQuery as the output of a specific prediction task.
- */
-message Prediction {
-  entity.EntityReference entity_reference = 1;
-  repeated PredictionTaskResult predictions = 2;
+  PredictionTask prediction_task = 1;
+  ModelType model_type = 2;
+  google.protobuf.Value label = 3;
+  google.protobuf.Value predicted_label = 4;
+  float probability = 5;
+  map<string, float> top_feature_attributions = 6;
 }
-
 // TODO(glg): feature_vectors BT table
 message FeatureVector {
   entity.EntityReference entity_reference = 1;
   google.protobuf.Timestamp created_at = 2;
   TaskLabel task_label = 3;
   repeated FeatureValue feature_values = 4;
 }
+
+// Prediction workflow
+// see io.calixa.learning.LearningWorkflowReceiver
+
+enum WorkflowStage {
+  WORKFLOW_STAGE_UNKNOWN = 0;
+  WORKFLOW_STAGE_START = 1;
+  // extract Entity's feature vectors and labels
+  WORKFLOW_STAGE_FEATURES = 2;
+  // train Model with feature vectors and labels (for supervised learning)
+  WORKFLOW_STAGE_MODEL_TRAINING = 3;
+  // run Entity's feature vectors through the Model to obtain predictions
+  WORKFLOW_STAGE_PREDICTION = 4;
+}
+
+message PredictionWorkflow {
+  WorkflowStage stage = 1;
+  string organization_id = 2;
+  google.protobuf.Timestamp started_at = 3;
+  repeated PredictionJobId jobs = 4;
+  bool force_model_update = 5;
+}
+
+message PredictionJobId {
+  string job_id = 1;
+  ModelType model_type = 2;
+  PredictionTask prediction_task = 3;
+  string location = 4;
+  string project = 5;
+}
```

### Comparing `calixa-proto-py-2.0.8/calixa_proto_py/learning_pb2.pyi` & `calixa-proto-py-2.0.9/calixa_proto_py/learning_pb2.pyi`

 * *Files 15% similar despite different names*

```diff
@@ -1,11 +1,9 @@
-"""
-@generated by mypy-protobuf.  Do not edit manually!
-isort:skip_file
-"""
+# @generated by generate_proto_mypy_stubs.py.  Do not edit!
+import sys
 from common_pb2 import (
     EntityTypeValue as common_pb2___EntityTypeValue,
 )
 
 from entity_reference_pb2 import (
     EntityReference as entity_reference_pb2___EntityReference,
 )
@@ -18,15 +16,14 @@
 
 from google.protobuf.duration_pb2 import (
     Duration as google___protobuf___duration_pb2___Duration,
 )
 
 from google.protobuf.internal.containers import (
     RepeatedCompositeFieldContainer as google___protobuf___internal___containers___RepeatedCompositeFieldContainer,
-    ScalarMap as google___protobuf___internal___containers___ScalarMap,
 )
 
 from google.protobuf.internal.enum_type_wrapper import (
     _EnumTypeWrapper as google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper,
 )
 
 from google.protobuf.message import (
@@ -40,14 +37,15 @@
 from google.protobuf.timestamp_pb2 import (
     Timestamp as google___protobuf___timestamp_pb2___Timestamp,
 )
 
 from typing import (
     Iterable as typing___Iterable,
     Mapping as typing___Mapping,
+    MutableMapping as typing___MutableMapping,
     NewType as typing___NewType,
     Optional as typing___Optional,
     Text as typing___Text,
     cast as typing___cast,
 )
 
 from typing_extensions import (
@@ -76,68 +74,87 @@
     FEATURE_VALUE_TYPE_BOOLEAN = typing___cast(FeatureValueTypeValue, 5)
 FEATURE_VALUE_TYPE_UNSPECIFIED = typing___cast(FeatureValueTypeValue, 0)
 FEATURE_VALUE_TYPE_INT64 = typing___cast(FeatureValueTypeValue, 1)
 FEATURE_VALUE_TYPE_DOUBLE = typing___cast(FeatureValueTypeValue, 2)
 FEATURE_VALUE_TYPE_STRING = typing___cast(FeatureValueTypeValue, 3)
 FEATURE_VALUE_TYPE_TIMESTAMP = typing___cast(FeatureValueTypeValue, 4)
 FEATURE_VALUE_TYPE_BOOLEAN = typing___cast(FeatureValueTypeValue, 5)
+type___FeatureValueType = FeatureValueType
 
 PredictionTaskValue = typing___NewType('PredictionTaskValue', builtin___int)
 type___PredictionTaskValue = PredictionTaskValue
 PredictionTask: _PredictionTask
 class _PredictionTask(google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper[PredictionTaskValue]):
     DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
     PREDICTION_TASK_UNSPECIFIED = typing___cast(PredictionTaskValue, 0)
     PREDICTION_TASK_BIG_FISH = typing___cast(PredictionTaskValue, 1)
     PREDICTION_TASK_SAME_FISH = typing___cast(PredictionTaskValue, 2)
 PREDICTION_TASK_UNSPECIFIED = typing___cast(PredictionTaskValue, 0)
 PREDICTION_TASK_BIG_FISH = typing___cast(PredictionTaskValue, 1)
 PREDICTION_TASK_SAME_FISH = typing___cast(PredictionTaskValue, 2)
+type___PredictionTask = PredictionTask
 
 ModelTypeValue = typing___NewType('ModelTypeValue', builtin___int)
 type___ModelTypeValue = ModelTypeValue
 ModelType: _ModelType
 class _ModelType(google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper[ModelTypeValue]):
     DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
     MODEL_TYPE_UNSPECIFIED = typing___cast(ModelTypeValue, 0)
     MODEL_TYPE_LOGISTIC_REG = typing___cast(ModelTypeValue, 1)
     MODEL_TYPE_KMEANS = typing___cast(ModelTypeValue, 2)
 MODEL_TYPE_UNSPECIFIED = typing___cast(ModelTypeValue, 0)
 MODEL_TYPE_LOGISTIC_REG = typing___cast(ModelTypeValue, 1)
 MODEL_TYPE_KMEANS = typing___cast(ModelTypeValue, 2)
+type___ModelType = ModelType
 
 TaskLabelSourceValue = typing___NewType('TaskLabelSourceValue', builtin___int)
 type___TaskLabelSourceValue = TaskLabelSourceValue
 TaskLabelSource: _TaskLabelSource
 class _TaskLabelSource(google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper[TaskLabelSourceValue]):
     DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
     TASK_LABEL_SOURCE_UNSPECIFIED = typing___cast(TaskLabelSourceValue, 0)
     TASK_LABEL_SOURCE_AUTOMATIC = typing___cast(TaskLabelSourceValue, 1)
     TASK_LABEL_SOURCE_USER = typing___cast(TaskLabelSourceValue, 2)
 TASK_LABEL_SOURCE_UNSPECIFIED = typing___cast(TaskLabelSourceValue, 0)
 TASK_LABEL_SOURCE_AUTOMATIC = typing___cast(TaskLabelSourceValue, 1)
 TASK_LABEL_SOURCE_USER = typing___cast(TaskLabelSourceValue, 2)
+type___TaskLabelSource = TaskLabelSource
+
+WorkflowStageValue = typing___NewType('WorkflowStageValue', builtin___int)
+type___WorkflowStageValue = WorkflowStageValue
+WorkflowStage: _WorkflowStage
+class _WorkflowStage(google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper[WorkflowStageValue]):
+    DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
+    WORKFLOW_STAGE_UNKNOWN = typing___cast(WorkflowStageValue, 0)
+    WORKFLOW_STAGE_START = typing___cast(WorkflowStageValue, 1)
+    WORKFLOW_STAGE_FEATURES = typing___cast(WorkflowStageValue, 2)
+    WORKFLOW_STAGE_MODEL_TRAINING = typing___cast(WorkflowStageValue, 3)
+    WORKFLOW_STAGE_PREDICTION = typing___cast(WorkflowStageValue, 4)
+WORKFLOW_STAGE_UNKNOWN = typing___cast(WorkflowStageValue, 0)
+WORKFLOW_STAGE_START = typing___cast(WorkflowStageValue, 1)
+WORKFLOW_STAGE_FEATURES = typing___cast(WorkflowStageValue, 2)
+WORKFLOW_STAGE_MODEL_TRAINING = typing___cast(WorkflowStageValue, 3)
+WORKFLOW_STAGE_PREDICTION = typing___cast(WorkflowStageValue, 4)
+type___WorkflowStage = WorkflowStage
 
 class FeatureDefinition(google___protobuf___message___Message):
     DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
     id: typing___Text = ...
     description: typing___Text = ...
     learnable: builtin___bool = ...
     type: type___FeatureValueTypeValue = ...
-    entity_type: common_pb2___EntityTypeValue = ...
 
     def __init__(self,
         *,
         id : typing___Optional[typing___Text] = None,
         description : typing___Optional[typing___Text] = None,
         learnable : typing___Optional[builtin___bool] = None,
         type : typing___Optional[type___FeatureValueTypeValue] = None,
-        entity_type : typing___Optional[common_pb2___EntityTypeValue] = None,
         ) -> None: ...
-    def ClearField(self, field_name: typing_extensions___Literal[u"description",b"description",u"entity_type",b"entity_type",u"id",b"id",u"learnable",b"learnable",u"type",b"type"]) -> None: ...
+    def ClearField(self, field_name: typing_extensions___Literal[u"description",b"description",u"id",b"id",u"learnable",b"learnable",u"type",b"type"]) -> None: ...
 type___FeatureDefinition = FeatureDefinition
 
 class FeatureValue(google___protobuf___message___Message):
     DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
     feature_id: typing___Text = ...
 
     @property
@@ -154,25 +171,29 @@
         ) -> None: ...
     def HasField(self, field_name: typing_extensions___Literal[u"created_at",b"created_at",u"value",b"value"]) -> builtin___bool: ...
     def ClearField(self, field_name: typing_extensions___Literal[u"created_at",b"created_at",u"feature_id",b"feature_id",u"value",b"value"]) -> None: ...
 type___FeatureValue = FeatureValue
 
 class PredictionTaskDefinition(google___protobuf___message___Message):
     DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
+    prediction_id: typing___Text = ...
     prediction_task: type___PredictionTaskValue = ...
+    entity_type: common_pb2___EntityTypeValue = ...
 
     @property
     def model_definitions(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[type___ModelDefinition]: ...
 
     def __init__(self,
         *,
+        prediction_id : typing___Optional[typing___Text] = None,
         prediction_task : typing___Optional[type___PredictionTaskValue] = None,
         model_definitions : typing___Optional[typing___Iterable[type___ModelDefinition]] = None,
+        entity_type : typing___Optional[common_pb2___EntityTypeValue] = None,
         ) -> None: ...
-    def ClearField(self, field_name: typing_extensions___Literal[u"model_definitions",b"model_definitions",u"prediction_task",b"prediction_task"]) -> None: ...
+    def ClearField(self, field_name: typing_extensions___Literal[u"entity_type",b"entity_type",u"model_definitions",b"model_definitions",u"prediction_id",b"prediction_id",u"prediction_task",b"prediction_task"]) -> None: ...
 type___PredictionTaskDefinition = PredictionTaskDefinition
 
 class ModelDefinition(google___protobuf___message___Message):
     DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
     model_type: type___ModelTypeValue = ...
 
     @property
@@ -209,38 +230,14 @@
         label : typing___Optional[google___protobuf___struct_pb2___Value] = None,
         created_at : typing___Optional[google___protobuf___timestamp_pb2___Timestamp] = None,
         ) -> None: ...
     def HasField(self, field_name: typing_extensions___Literal[u"created_at",b"created_at",u"label",b"label"]) -> builtin___bool: ...
     def ClearField(self, field_name: typing_extensions___Literal[u"created_at",b"created_at",u"label",b"label",u"label_source",b"label_source",u"prediction_task",b"prediction_task"]) -> None: ...
 type___TaskLabel = TaskLabel
 
-class PredictionTaskResult(google___protobuf___message___Message):
-    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
-    prediction_task: type___PredictionTaskValue = ...
-
-    @property
-    def predicted_label(self) -> google___protobuf___struct_pb2___Value: ...
-
-    @property
-    def created_at(self) -> google___protobuf___timestamp_pb2___Timestamp: ...
-
-    @property
-    def model_predictions(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[type___TaskModelPrediction]: ...
-
-    def __init__(self,
-        *,
-        prediction_task : typing___Optional[type___PredictionTaskValue] = None,
-        predicted_label : typing___Optional[google___protobuf___struct_pb2___Value] = None,
-        created_at : typing___Optional[google___protobuf___timestamp_pb2___Timestamp] = None,
-        model_predictions : typing___Optional[typing___Iterable[type___TaskModelPrediction]] = None,
-        ) -> None: ...
-    def HasField(self, field_name: typing_extensions___Literal[u"created_at",b"created_at",u"predicted_label",b"predicted_label"]) -> builtin___bool: ...
-    def ClearField(self, field_name: typing_extensions___Literal[u"created_at",b"created_at",u"model_predictions",b"model_predictions",u"predicted_label",b"predicted_label",u"prediction_task",b"prediction_task"]) -> None: ...
-type___PredictionTaskResult = PredictionTaskResult
-
 class TaskModelPrediction(google___protobuf___message___Message):
     DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
     class TopFeatureAttributionsEntry(google___protobuf___message___Message):
         DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
         key: typing___Text = ...
         value: builtin___float = ...
 
@@ -248,56 +245,40 @@
             *,
             key : typing___Optional[typing___Text] = None,
             value : typing___Optional[builtin___float] = None,
             ) -> None: ...
         def ClearField(self, field_name: typing_extensions___Literal[u"key",b"key",u"value",b"value"]) -> None: ...
     type___TopFeatureAttributionsEntry = TopFeatureAttributionsEntry
 
-    model_id: typing___Text = ...
+    prediction_task: type___PredictionTaskValue = ...
+    model_type: type___ModelTypeValue = ...
     probability: builtin___float = ...
 
     @property
     def label(self) -> google___protobuf___struct_pb2___Value: ...
 
     @property
     def predicted_label(self) -> google___protobuf___struct_pb2___Value: ...
 
     @property
-    def top_feature_attributions(self) -> google___protobuf___internal___containers___ScalarMap[typing___Text, builtin___float]: ...
+    def top_feature_attributions(self) -> typing___MutableMapping[typing___Text, builtin___float]: ...
 
     def __init__(self,
         *,
-        model_id : typing___Optional[typing___Text] = None,
+        prediction_task : typing___Optional[type___PredictionTaskValue] = None,
+        model_type : typing___Optional[type___ModelTypeValue] = None,
         label : typing___Optional[google___protobuf___struct_pb2___Value] = None,
         predicted_label : typing___Optional[google___protobuf___struct_pb2___Value] = None,
         probability : typing___Optional[builtin___float] = None,
         top_feature_attributions : typing___Optional[typing___Mapping[typing___Text, builtin___float]] = None,
         ) -> None: ...
     def HasField(self, field_name: typing_extensions___Literal[u"label",b"label",u"predicted_label",b"predicted_label"]) -> builtin___bool: ...
-    def ClearField(self, field_name: typing_extensions___Literal[u"label",b"label",u"model_id",b"model_id",u"predicted_label",b"predicted_label",u"probability",b"probability",u"top_feature_attributions",b"top_feature_attributions"]) -> None: ...
+    def ClearField(self, field_name: typing_extensions___Literal[u"label",b"label",u"model_type",b"model_type",u"predicted_label",b"predicted_label",u"prediction_task",b"prediction_task",u"probability",b"probability",u"top_feature_attributions",b"top_feature_attributions"]) -> None: ...
 type___TaskModelPrediction = TaskModelPrediction
 
-class Prediction(google___protobuf___message___Message):
-    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
-
-    @property
-    def entity_reference(self) -> entity_reference_pb2___EntityReference: ...
-
-    @property
-    def predictions(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[type___PredictionTaskResult]: ...
-
-    def __init__(self,
-        *,
-        entity_reference : typing___Optional[entity_reference_pb2___EntityReference] = None,
-        predictions : typing___Optional[typing___Iterable[type___PredictionTaskResult]] = None,
-        ) -> None: ...
-    def HasField(self, field_name: typing_extensions___Literal[u"entity_reference",b"entity_reference"]) -> builtin___bool: ...
-    def ClearField(self, field_name: typing_extensions___Literal[u"entity_reference",b"entity_reference",u"predictions",b"predictions"]) -> None: ...
-type___Prediction = Prediction
-
 class FeatureVector(google___protobuf___message___Message):
     DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
 
     @property
     def entity_reference(self) -> entity_reference_pb2___EntityReference: ...
 
     @property
@@ -315,7 +296,50 @@
         created_at : typing___Optional[google___protobuf___timestamp_pb2___Timestamp] = None,
         task_label : typing___Optional[type___TaskLabel] = None,
         feature_values : typing___Optional[typing___Iterable[type___FeatureValue]] = None,
         ) -> None: ...
     def HasField(self, field_name: typing_extensions___Literal[u"created_at",b"created_at",u"entity_reference",b"entity_reference",u"task_label",b"task_label"]) -> builtin___bool: ...
     def ClearField(self, field_name: typing_extensions___Literal[u"created_at",b"created_at",u"entity_reference",b"entity_reference",u"feature_values",b"feature_values",u"task_label",b"task_label"]) -> None: ...
 type___FeatureVector = FeatureVector
+
+class PredictionWorkflow(google___protobuf___message___Message):
+    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
+    stage: type___WorkflowStageValue = ...
+    organization_id: typing___Text = ...
+    force_model_update: builtin___bool = ...
+
+    @property
+    def started_at(self) -> google___protobuf___timestamp_pb2___Timestamp: ...
+
+    @property
+    def jobs(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[type___PredictionJobId]: ...
+
+    def __init__(self,
+        *,
+        stage : typing___Optional[type___WorkflowStageValue] = None,
+        organization_id : typing___Optional[typing___Text] = None,
+        started_at : typing___Optional[google___protobuf___timestamp_pb2___Timestamp] = None,
+        jobs : typing___Optional[typing___Iterable[type___PredictionJobId]] = None,
+        force_model_update : typing___Optional[builtin___bool] = None,
+        ) -> None: ...
+    def HasField(self, field_name: typing_extensions___Literal[u"started_at",b"started_at"]) -> builtin___bool: ...
+    def ClearField(self, field_name: typing_extensions___Literal[u"force_model_update",b"force_model_update",u"jobs",b"jobs",u"organization_id",b"organization_id",u"stage",b"stage",u"started_at",b"started_at"]) -> None: ...
+type___PredictionWorkflow = PredictionWorkflow
+
+class PredictionJobId(google___protobuf___message___Message):
+    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
+    job_id: typing___Text = ...
+    model_type: type___ModelTypeValue = ...
+    prediction_task: type___PredictionTaskValue = ...
+    location: typing___Text = ...
+    project: typing___Text = ...
+
+    def __init__(self,
+        *,
+        job_id : typing___Optional[typing___Text] = None,
+        model_type : typing___Optional[type___ModelTypeValue] = None,
+        prediction_task : typing___Optional[type___PredictionTaskValue] = None,
+        location : typing___Optional[typing___Text] = None,
+        project : typing___Optional[typing___Text] = None,
+        ) -> None: ...
+    def ClearField(self, field_name: typing_extensions___Literal[u"job_id",b"job_id",u"location",b"location",u"model_type",b"model_type",u"prediction_task",b"prediction_task",u"project",b"project"]) -> None: ...
+type___PredictionJobId = PredictionJobId
```

### Comparing `calixa-proto-py-2.0.8/calixa_proto_py/log.proto` & `calixa-proto-py-2.0.9/calixa_proto_py/log.proto`

 * *Files identical despite different names*

### Comparing `calixa-proto-py-2.0.8/calixa_proto_py/log_pb2.pyi` & `calixa-proto-py-2.0.9/calixa_proto_py/log_pb2.pyi`

 * *Files 3% similar despite different names*

```diff
@@ -1,25 +1,19 @@
-"""
-@generated by mypy-protobuf.  Do not edit manually!
-isort:skip_file
-"""
+# @generated by generate_proto_mypy_stubs.py.  Do not edit!
+import sys
 from common_pb2 import (
     RequestContext as common_pb2___RequestContext,
 )
 
 from google.protobuf.descriptor import (
     Descriptor as google___protobuf___descriptor___Descriptor,
     EnumDescriptor as google___protobuf___descriptor___EnumDescriptor,
     FileDescriptor as google___protobuf___descriptor___FileDescriptor,
 )
 
-from google.protobuf.internal.containers import (
-    ScalarMap as google___protobuf___internal___containers___ScalarMap,
-)
-
 from google.protobuf.internal.enum_type_wrapper import (
     _EnumTypeWrapper as google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper,
 )
 
 from google.protobuf.message import (
     Message as google___protobuf___message___Message,
 )
@@ -30,14 +24,15 @@
 
 from integration_source_pb2 import (
     IntegrationSourceValue as integration_source_pb2___IntegrationSourceValue,
 )
 
 from typing import (
     Mapping as typing___Mapping,
+    MutableMapping as typing___MutableMapping,
     NewType as typing___NewType,
     Optional as typing___Optional,
     Text as typing___Text,
     cast as typing___cast,
 )
 
 from typing_extensions import (
@@ -62,14 +57,15 @@
     LOG_STATUS_PROCESSED = typing___cast(LogStatusValue, 1)
     LOG_STATUS_FAILED = typing___cast(LogStatusValue, 2)
     LOG_STATUS_PENDING = typing___cast(LogStatusValue, 3)
 LOG_STATUS_UNSPECIFIED = typing___cast(LogStatusValue, 0)
 LOG_STATUS_PROCESSED = typing___cast(LogStatusValue, 1)
 LOG_STATUS_FAILED = typing___cast(LogStatusValue, 2)
 LOG_STATUS_PENDING = typing___cast(LogStatusValue, 3)
+type___LogStatus = LogStatus
 
 class ThirdPartyLogEntry(google___protobuf___message___Message):
     DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
     class HeadersEntry(google___protobuf___message___Message):
         DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
         key: typing___Text = ...
         value: typing___Text = ...
@@ -94,18 +90,18 @@
             ) -> None: ...
         def ClearField(self, field_name: typing_extensions___Literal[u"key",b"key",u"value",b"value"]) -> None: ...
     type___MetaEntry = MetaEntry
 
     body: typing___Text = ...
 
     @property
-    def headers(self) -> google___protobuf___internal___containers___ScalarMap[typing___Text, typing___Text]: ...
+    def headers(self) -> typing___MutableMapping[typing___Text, typing___Text]: ...
 
     @property
-    def meta(self) -> google___protobuf___internal___containers___ScalarMap[typing___Text, typing___Text]: ...
+    def meta(self) -> typing___MutableMapping[typing___Text, typing___Text]: ...
 
     def __init__(self,
         *,
         headers : typing___Optional[typing___Mapping[typing___Text, typing___Text]] = None,
         meta : typing___Optional[typing___Mapping[typing___Text, typing___Text]] = None,
         body : typing___Optional[typing___Text] = None,
         ) -> None: ...
@@ -126,15 +122,15 @@
             ) -> None: ...
         def ClearField(self, field_name: typing_extensions___Literal[u"key",b"key",u"value",b"value"]) -> None: ...
     type___HeadersEntry = HeadersEntry
 
     body: typing___Text = ...
 
     @property
-    def headers(self) -> google___protobuf___internal___containers___ScalarMap[typing___Text, typing___Text]: ...
+    def headers(self) -> typing___MutableMapping[typing___Text, typing___Text]: ...
 
     @property
     def request_context(self) -> common_pb2___RequestContext: ...
 
     def __init__(self,
         *,
         headers : typing___Optional[typing___Mapping[typing___Text, typing___Text]] = None,
```

### Comparing `calixa-proto-py-2.0.8/calixa_proto_py/log_pb2_grpc.py` & `calixa-proto-py-2.0.9/calixa_proto_py/log_pb2_grpc.py`

 * *Files identical despite different names*

### Comparing `calixa-proto-py-2.0.8/calixa_proto_py/metric.proto` & `calixa-proto-py-2.0.9/calixa_proto_py/metric.proto`

 * *Files 2% similar despite different names*

```diff
@@ -269,15 +269,15 @@
   google.protobuf.Timestamp from = 3;
   google.protobuf.Timestamp to = 4;
   MetricAggregateOperation aggregate_operation = 5;
   repeated string metric_descriptor_ids = 6;
 }
 
 message AggregatedMetric {
-  int64 current = 1;
-  int64 previous = 2;
+  double current = 1;
+  double previous = 2;
   double delta = 3;
 }
 
 message MetricSummaryResponse {
   map<string, AggregatedMetric> metric_summaries = 1;
 }
```

### Comparing `calixa-proto-py-2.0.8/calixa_proto_py/metric_pb2.pyi` & `calixa-proto-py-2.0.9/calixa_proto_py/metric_pb2.pyi`

 * *Files 2% similar despite different names*

```diff
@@ -1,11 +1,9 @@
-"""
-@generated by mypy-protobuf.  Do not edit manually!
-isort:skip_file
-"""
+# @generated by generate_proto_mypy_stubs.py.  Do not edit!
+import sys
 from common_pb2 import (
     EntityTypeValue as common_pb2___EntityTypeValue,
     RequestContext as common_pb2___RequestContext,
 )
 
 from condition_pb2 import (
     ConditionGroup as condition_pb2___ConditionGroup,
@@ -22,15 +20,14 @@
 )
 
 from google.protobuf.field_mask_pb2 import (
     FieldMask as google___protobuf___field_mask_pb2___FieldMask,
 )
 
 from google.protobuf.internal.containers import (
-    MessageMap as google___protobuf___internal___containers___MessageMap,
     RepeatedScalarFieldContainer as google___protobuf___internal___containers___RepeatedScalarFieldContainer,
 )
 
 from google.protobuf.internal.enum_type_wrapper import (
     _EnumTypeWrapper as google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper,
 )
 
@@ -49,14 +46,15 @@
 from integration_source_pb2 import (
     IntegrationSourceValue as integration_source_pb2___IntegrationSourceValue,
 )
 
 from typing import (
     Iterable as typing___Iterable,
     Mapping as typing___Mapping,
+    MutableMapping as typing___MutableMapping,
     NewType as typing___NewType,
     Optional as typing___Optional,
     Text as typing___Text,
     cast as typing___cast,
 )
 
 from typing_extensions import (
@@ -79,68 +77,73 @@
     DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
     METRIC_STATUS_UNSPECIFIED = typing___cast(MetricStatusValue, 0)
     ACTIVE = typing___cast(MetricStatusValue, 1)
     DELETED = typing___cast(MetricStatusValue, 2)
 METRIC_STATUS_UNSPECIFIED = typing___cast(MetricStatusValue, 0)
 ACTIVE = typing___cast(MetricStatusValue, 1)
 DELETED = typing___cast(MetricStatusValue, 2)
+type___MetricStatus = MetricStatus
 
 MetricTypeValue = typing___NewType('MetricTypeValue', builtin___int)
 type___MetricTypeValue = MetricTypeValue
 MetricType: _MetricType
 class _MetricType(google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper[MetricTypeValue]):
     DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
     METRIC_TYPE_UNSPECIFIED = typing___cast(MetricTypeValue, 0)
     CUMULATIVE = typing___cast(MetricTypeValue, 1)
     GAUGE = typing___cast(MetricTypeValue, 2)
     DERIVED = typing___cast(MetricTypeValue, 3)
 METRIC_TYPE_UNSPECIFIED = typing___cast(MetricTypeValue, 0)
 CUMULATIVE = typing___cast(MetricTypeValue, 1)
 GAUGE = typing___cast(MetricTypeValue, 2)
 DERIVED = typing___cast(MetricTypeValue, 3)
+type___MetricType = MetricType
 
 MetricValueTypeValue = typing___NewType('MetricValueTypeValue', builtin___int)
 type___MetricValueTypeValue = MetricValueTypeValue
 MetricValueType: _MetricValueType
 class _MetricValueType(google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper[MetricValueTypeValue]):
     DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
     METRIC_VALUE_TYPE_UNSPECIFIED = typing___cast(MetricValueTypeValue, 0)
     INT64 = typing___cast(MetricValueTypeValue, 1)
     DOUBLE = typing___cast(MetricValueTypeValue, 2)
     MONEY = typing___cast(MetricValueTypeValue, 3)
 METRIC_VALUE_TYPE_UNSPECIFIED = typing___cast(MetricValueTypeValue, 0)
 INT64 = typing___cast(MetricValueTypeValue, 1)
 DOUBLE = typing___cast(MetricValueTypeValue, 2)
 MONEY = typing___cast(MetricValueTypeValue, 3)
+type___MetricValueType = MetricValueType
 
 MetricExternalEntityTypeValue = typing___NewType('MetricExternalEntityTypeValue', builtin___int)
 type___MetricExternalEntityTypeValue = MetricExternalEntityTypeValue
 MetricExternalEntityType: _MetricExternalEntityType
 class _MetricExternalEntityType(google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper[MetricExternalEntityTypeValue]):
     DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
     METRIC_EXTERNAL_ENTITY_UNSPECIFIED = typing___cast(MetricExternalEntityTypeValue, 0)
     ORGANIZATION = typing___cast(MetricExternalEntityTypeValue, 1)
     ACCOUNT = typing___cast(MetricExternalEntityTypeValue, 2)
     ACCOUNT_USER = typing___cast(MetricExternalEntityTypeValue, 3)
 METRIC_EXTERNAL_ENTITY_UNSPECIFIED = typing___cast(MetricExternalEntityTypeValue, 0)
 ORGANIZATION = typing___cast(MetricExternalEntityTypeValue, 1)
 ACCOUNT = typing___cast(MetricExternalEntityTypeValue, 2)
 ACCOUNT_USER = typing___cast(MetricExternalEntityTypeValue, 3)
+type___MetricExternalEntityType = MetricExternalEntityType
 
 MetricOriginValue = typing___NewType('MetricOriginValue', builtin___int)
 type___MetricOriginValue = MetricOriginValue
 MetricOrigin: _MetricOrigin
 class _MetricOrigin(google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper[MetricOriginValue]):
     DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
     METRIC_ORIGIN_UNSPECIFIED = typing___cast(MetricOriginValue, 0)
     METRIC_ORIGIN_API = typing___cast(MetricOriginValue, 1)
     METRIC_ORIGIN_AUTOMATIC = typing___cast(MetricOriginValue, 2)
 METRIC_ORIGIN_UNSPECIFIED = typing___cast(MetricOriginValue, 0)
 METRIC_ORIGIN_API = typing___cast(MetricOriginValue, 1)
 METRIC_ORIGIN_AUTOMATIC = typing___cast(MetricOriginValue, 2)
+type___MetricOrigin = MetricOrigin
 
 MetricGroupByValue = typing___NewType('MetricGroupByValue', builtin___int)
 type___MetricGroupByValue = MetricGroupByValue
 MetricGroupBy: _MetricGroupBy
 class _MetricGroupBy(google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper[MetricGroupByValue]):
     DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
     METRIC_GROUP_BY_UNSPECIFIED = typing___cast(MetricGroupByValue, 0)
@@ -151,54 +154,58 @@
     METRIC_GROUP_BY_YEAR = typing___cast(MetricGroupByValue, 5)
 METRIC_GROUP_BY_UNSPECIFIED = typing___cast(MetricGroupByValue, 0)
 METRIC_GROUP_BY_HOUR = typing___cast(MetricGroupByValue, 1)
 METRIC_GROUP_BY_DAY = typing___cast(MetricGroupByValue, 2)
 METRIC_GROUP_BY_WEEK = typing___cast(MetricGroupByValue, 3)
 METRIC_GROUP_BY_MONTH = typing___cast(MetricGroupByValue, 4)
 METRIC_GROUP_BY_YEAR = typing___cast(MetricGroupByValue, 5)
+type___MetricGroupBy = MetricGroupBy
 
 MetricAggregateOperationValue = typing___NewType('MetricAggregateOperationValue', builtin___int)
 type___MetricAggregateOperationValue = MetricAggregateOperationValue
 MetricAggregateOperation: _MetricAggregateOperation
 class _MetricAggregateOperation(google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper[MetricAggregateOperationValue]):
     DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
     METRIC_AGGREGATE_OPERATION_UNSPECIFIED = typing___cast(MetricAggregateOperationValue, 0)
     METRIC_AGGREGATE_OPERATION_SUM = typing___cast(MetricAggregateOperationValue, 1)
     METRIC_AGGREGATE_OPERATION_AVG = typing___cast(MetricAggregateOperationValue, 2)
     METRIC_AGGREGATE_OPERATION_COUNT = typing___cast(MetricAggregateOperationValue, 3)
 METRIC_AGGREGATE_OPERATION_UNSPECIFIED = typing___cast(MetricAggregateOperationValue, 0)
 METRIC_AGGREGATE_OPERATION_SUM = typing___cast(MetricAggregateOperationValue, 1)
 METRIC_AGGREGATE_OPERATION_AVG = typing___cast(MetricAggregateOperationValue, 2)
 METRIC_AGGREGATE_OPERATION_COUNT = typing___cast(MetricAggregateOperationValue, 3)
+type___MetricAggregateOperation = MetricAggregateOperation
 
 DerivedMetricValue = typing___NewType('DerivedMetricValue', builtin___int)
 type___DerivedMetricValue = DerivedMetricValue
 DerivedMetric: _DerivedMetric
 class _DerivedMetric(google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper[DerivedMetricValue]):
     DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
     DERIVED_METRIC_UNSPECIFIED = typing___cast(DerivedMetricValue, 0)
     DERIVED_METRIC_DAYS_ACTIVE = typing___cast(DerivedMetricValue, 1)
     DERIVED_METRIC_USERS_ACTIVE = typing___cast(DerivedMetricValue, 2)
     DERIVED_METRIC_ACCOUNTS_ACTIVE = typing___cast(DerivedMetricValue, 3)
 DERIVED_METRIC_UNSPECIFIED = typing___cast(DerivedMetricValue, 0)
 DERIVED_METRIC_DAYS_ACTIVE = typing___cast(DerivedMetricValue, 1)
 DERIVED_METRIC_USERS_ACTIVE = typing___cast(DerivedMetricValue, 2)
 DERIVED_METRIC_ACCOUNTS_ACTIVE = typing___cast(DerivedMetricValue, 3)
+type___DerivedMetric = DerivedMetric
 
 MetricObservationFeatureValue = typing___NewType('MetricObservationFeatureValue', builtin___int)
 type___MetricObservationFeatureValue = MetricObservationFeatureValue
 MetricObservationFeature: _MetricObservationFeature
 class _MetricObservationFeature(google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper[MetricObservationFeatureValue]):
     DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
     METRIC_OBSERVATION_FEATURE_UNSPECIFIED = typing___cast(MetricObservationFeatureValue, 0)
     METRIC_OBSERVATION_FEATURE_IS_AUTO_METRIC = typing___cast(MetricObservationFeatureValue, 1)
     METRIC_OBSERVATION_FEATURE_IS_TRACK_METRIC = typing___cast(MetricObservationFeatureValue, 2)
 METRIC_OBSERVATION_FEATURE_UNSPECIFIED = typing___cast(MetricObservationFeatureValue, 0)
 METRIC_OBSERVATION_FEATURE_IS_AUTO_METRIC = typing___cast(MetricObservationFeatureValue, 1)
 METRIC_OBSERVATION_FEATURE_IS_TRACK_METRIC = typing___cast(MetricObservationFeatureValue, 2)
+type___MetricObservationFeature = MetricObservationFeature
 
 class MetricDescriptor(google___protobuf___message___Message):
     DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
     metric_descriptor_id: typing___Text = ...
     organization_id: typing___Text = ...
     status: type___MetricStatusValue = ...
     metric_type: type___MetricTypeValue = ...
@@ -503,22 +510,22 @@
         ) -> None: ...
     def HasField(self, field_name: typing_extensions___Literal[u"from",b"from",u"to",b"to"]) -> builtin___bool: ...
     def ClearField(self, field_name: typing_extensions___Literal[u"aggregate_operation",b"aggregate_operation",u"canonical_entity_id",b"canonical_entity_id",u"from",b"from",u"metric_descriptor_ids",b"metric_descriptor_ids",u"organization_id",b"organization_id",u"to",b"to"]) -> None: ...
 type___MetricSummaryRequest = MetricSummaryRequest
 
 class AggregatedMetric(google___protobuf___message___Message):
     DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
-    current: builtin___int = ...
-    previous: builtin___int = ...
+    current: builtin___float = ...
+    previous: builtin___float = ...
     delta: builtin___float = ...
 
     def __init__(self,
         *,
-        current : typing___Optional[builtin___int] = None,
-        previous : typing___Optional[builtin___int] = None,
+        current : typing___Optional[builtin___float] = None,
+        previous : typing___Optional[builtin___float] = None,
         delta : typing___Optional[builtin___float] = None,
         ) -> None: ...
     def ClearField(self, field_name: typing_extensions___Literal[u"current",b"current",u"delta",b"delta",u"previous",b"previous"]) -> None: ...
 type___AggregatedMetric = AggregatedMetric
 
 class MetricSummaryResponse(google___protobuf___message___Message):
     DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
@@ -536,15 +543,15 @@
             ) -> None: ...
         def HasField(self, field_name: typing_extensions___Literal[u"value",b"value"]) -> builtin___bool: ...
         def ClearField(self, field_name: typing_extensions___Literal[u"key",b"key",u"value",b"value"]) -> None: ...
     type___MetricSummariesEntry = MetricSummariesEntry
 
 
     @property
-    def metric_summaries(self) -> google___protobuf___internal___containers___MessageMap[typing___Text, type___AggregatedMetric]: ...
+    def metric_summaries(self) -> typing___MutableMapping[typing___Text, type___AggregatedMetric]: ...
 
     def __init__(self,
         *,
         metric_summaries : typing___Optional[typing___Mapping[typing___Text, type___AggregatedMetric]] = None,
         ) -> None: ...
     def ClearField(self, field_name: typing_extensions___Literal[u"metric_summaries",b"metric_summaries"]) -> None: ...
 type___MetricSummaryResponse = MetricSummaryResponse
```

### Comparing `calixa-proto-py-2.0.8/calixa_proto_py/metric_pb2_grpc.py` & `calixa-proto-py-2.0.9/calixa_proto_py/metric_pb2_grpc.py`

 * *Files identical despite different names*

### Comparing `calixa-proto-py-2.0.8/calixa_proto_py/notification_test_service.proto` & `calixa-proto-py-2.0.9/calixa_proto_py/notification_test_service.proto`

 * *Files identical despite different names*

### Comparing `calixa-proto-py-2.0.8/calixa_proto_py/notification_test_service_pb2.pyi` & `calixa-proto-py-2.0.9/calixa_proto_py/notification_test_service_pb2.pyi`

 * *Files 15% similar despite different names*

```diff
@@ -1,34 +1,29 @@
-"""
-@generated by mypy-protobuf.  Do not edit manually!
-isort:skip_file
-"""
+# @generated by generate_proto_mypy_stubs.py.  Do not edit!
+import sys
 from common_pb2 import (
     EntityTypeValue as common_pb2___EntityTypeValue,
 )
 
 from google.protobuf.descriptor import (
     Descriptor as google___protobuf___descriptor___Descriptor,
     FileDescriptor as google___protobuf___descriptor___FileDescriptor,
 )
 
-from google.protobuf.internal.containers import (
-    ScalarMap as google___protobuf___internal___containers___ScalarMap,
-)
-
 from google.protobuf.message import (
     Message as google___protobuf___message___Message,
 )
 
 from google.protobuf.struct_pb2 import (
     Struct as google___protobuf___struct_pb2___Struct,
 )
 
 from typing import (
     Mapping as typing___Mapping,
+    MutableMapping as typing___MutableMapping,
     Optional as typing___Optional,
     Text as typing___Text,
 )
 
 from typing_extensions import (
     Literal as typing_extensions___Literal,
 )
@@ -80,15 +75,15 @@
         def ClearField(self, field_name: typing_extensions___Literal[u"key",b"key",u"value",b"value"]) -> None: ...
     type___HeadersEntry = HeadersEntry
 
     url: typing___Text = ...
     httpMethod: typing___Text = ...
 
     @property
-    def headers(self) -> google___protobuf___internal___containers___ScalarMap[typing___Text, typing___Text]: ...
+    def headers(self) -> typing___MutableMapping[typing___Text, typing___Text]: ...
 
     def __init__(self,
         *,
         url : typing___Optional[typing___Text] = None,
         httpMethod : typing___Optional[typing___Text] = None,
         headers : typing___Optional[typing___Mapping[typing___Text, typing___Text]] = None,
         ) -> None: ...
```

### Comparing `calixa-proto-py-2.0.8/calixa_proto_py/notification_test_service_pb2_grpc.py` & `calixa-proto-py-2.0.9/calixa_proto_py/notification_test_service_pb2_grpc.py`

 * *Files identical despite different names*

### Comparing `calixa-proto-py-2.0.8/calixa_proto_py/organization_pb2.pyi` & `calixa-proto-py-2.0.9/calixa_proto_py/organization_pb2.pyi`

 * *Files 20% similar despite different names*

```diff
@@ -1,11 +1,9 @@
-"""
-@generated by mypy-protobuf.  Do not edit manually!
-isort:skip_file
-"""
+# @generated by generate_proto_mypy_stubs.py.  Do not edit!
+import sys
 from common_pb2 import (
     EntityTypeValue as common_pb2___EntityTypeValue,
 )
 
 from condition_pb2 import (
     Journey as condition_pb2___Journey,
     ScoringFunction as condition_pb2___ScoringFunction,
@@ -13,18 +11,14 @@
 
 from google.protobuf.descriptor import (
     Descriptor as google___protobuf___descriptor___Descriptor,
     EnumDescriptor as google___protobuf___descriptor___EnumDescriptor,
     FileDescriptor as google___protobuf___descriptor___FileDescriptor,
 )
 
-from google.protobuf.field_mask_pb2 import (
-    FieldMask as google___protobuf___field_mask_pb2___FieldMask,
-)
-
 from google.protobuf.internal.containers import (
     RepeatedCompositeFieldContainer as google___protobuf___internal___containers___RepeatedCompositeFieldContainer,
     RepeatedScalarFieldContainer as google___protobuf___internal___containers___RepeatedScalarFieldContainer,
 )
 
 from google.protobuf.internal.enum_type_wrapper import (
     _EnumTypeWrapper as google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper,
@@ -74,14 +68,15 @@
     DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
     ACCESS_KEY_STATUS_UNSPECIFIED = typing___cast(AccessKeyStatusValue, 0)
     ACCESS_KEY_ACTIVE = typing___cast(AccessKeyStatusValue, 1)
     ACCESS_KEY_INACTIVE = typing___cast(AccessKeyStatusValue, 2)
 ACCESS_KEY_STATUS_UNSPECIFIED = typing___cast(AccessKeyStatusValue, 0)
 ACCESS_KEY_ACTIVE = typing___cast(AccessKeyStatusValue, 1)
 ACCESS_KEY_INACTIVE = typing___cast(AccessKeyStatusValue, 2)
+type___AccessKeyStatus = AccessKeyStatus
 
 OrganizationUserStatusValue = typing___NewType('OrganizationUserStatusValue', builtin___int)
 type___OrganizationUserStatusValue = OrganizationUserStatusValue
 OrganizationUserStatus: _OrganizationUserStatus
 class _OrganizationUserStatus(google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper[OrganizationUserStatusValue]):
     DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
     ORGANIZATION_USER_STATUS_UNSPECIFIED = typing___cast(OrganizationUserStatusValue, 0)
@@ -90,14 +85,15 @@
     ORGANIZATION_USER_DELETED = typing___cast(OrganizationUserStatusValue, 3)
     ORGANIZATION_USER_INVITED = typing___cast(OrganizationUserStatusValue, 4)
 ORGANIZATION_USER_STATUS_UNSPECIFIED = typing___cast(OrganizationUserStatusValue, 0)
 ORGANIZATION_USER_ACTIVE = typing___cast(OrganizationUserStatusValue, 1)
 ORGANIZATION_USER_SUSPENDED = typing___cast(OrganizationUserStatusValue, 2)
 ORGANIZATION_USER_DELETED = typing___cast(OrganizationUserStatusValue, 3)
 ORGANIZATION_USER_INVITED = typing___cast(OrganizationUserStatusValue, 4)
+type___OrganizationUserStatus = OrganizationUserStatus
 
 PropertyFieldTypeValue = typing___NewType('PropertyFieldTypeValue', builtin___int)
 type___PropertyFieldTypeValue = PropertyFieldTypeValue
 PropertyFieldType: _PropertyFieldType
 class _PropertyFieldType(google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper[PropertyFieldTypeValue]):
     DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
     PROPERTY_FIELD_TYPE_UNSPECIFIED = typing___cast(PropertyFieldTypeValue, 0)
@@ -108,14 +104,15 @@
     PROPERTY_FIELD_TYPE_TIMESTAMP = typing___cast(PropertyFieldTypeValue, 5)
 PROPERTY_FIELD_TYPE_UNSPECIFIED = typing___cast(PropertyFieldTypeValue, 0)
 PROPERTY_FIELD_TYPE_INTEGER = typing___cast(PropertyFieldTypeValue, 1)
 PROPERTY_FIELD_TYPE_DECIMAL = typing___cast(PropertyFieldTypeValue, 2)
 PROPERTY_FIELD_TYPE_STRING = typing___cast(PropertyFieldTypeValue, 3)
 PROPERTY_FIELD_TYPE_BOOLEAN = typing___cast(PropertyFieldTypeValue, 4)
 PROPERTY_FIELD_TYPE_TIMESTAMP = typing___cast(PropertyFieldTypeValue, 5)
+type___PropertyFieldType = PropertyFieldType
 
 class AccessKey(google___protobuf___message___Message):
     DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
     organization_id: typing___Text = ...
     access_key_id: typing___Text = ...
     secret_access_key: typing___Text = ...
     status: type___AccessKeyStatusValue = ...
@@ -316,223 +313,14 @@
         is_public : typing___Optional[builtin___bool] = None,
         created_by_organization_user_id : typing___Optional[typing___Text] = None,
         folder_id : typing___Optional[typing___Text] = None,
         ) -> None: ...
     def ClearField(self, field_name: typing_extensions___Literal[u"columns",b"columns",u"created_by_organization_user_id",b"created_by_organization_user_id",u"entity_type",b"entity_type",u"filters",b"filters",u"folder_id",b"folder_id",u"is_public",b"is_public",u"name",b"name",u"rank_metrics",b"rank_metrics",u"sort_field",b"sort_field",u"sort_order",b"sort_order"]) -> None: ...
 type___TrendSearch = TrendSearch
 
-class CreateKeyRequest(google___protobuf___message___Message):
-    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
-    organization_id: typing___Text = ...
-    created_by_id: typing___Text = ...
-
-    def __init__(self,
-        *,
-        organization_id : typing___Optional[typing___Text] = None,
-        created_by_id : typing___Optional[typing___Text] = None,
-        ) -> None: ...
-    def ClearField(self, field_name: typing_extensions___Literal[u"created_by_id",b"created_by_id",u"organization_id",b"organization_id"]) -> None: ...
-type___CreateKeyRequest = CreateKeyRequest
-
-class CreateOrganizationRequest(google___protobuf___message___Message):
-    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
-
-    @property
-    def organization(self) -> type___Organization: ...
-
-    def __init__(self,
-        *,
-        organization : typing___Optional[type___Organization] = None,
-        ) -> None: ...
-    def HasField(self, field_name: typing_extensions___Literal[u"organization",b"organization"]) -> builtin___bool: ...
-    def ClearField(self, field_name: typing_extensions___Literal[u"organization",b"organization"]) -> None: ...
-type___CreateOrganizationRequest = CreateOrganizationRequest
-
-class CreateOrganizationUserRequest(google___protobuf___message___Message):
-    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
-
-    @property
-    def organizationUser(self) -> type___OrganizationUser: ...
-
-    def __init__(self,
-        *,
-        organizationUser : typing___Optional[type___OrganizationUser] = None,
-        ) -> None: ...
-    def HasField(self, field_name: typing_extensions___Literal[u"organizationUser",b"organizationUser"]) -> builtin___bool: ...
-    def ClearField(self, field_name: typing_extensions___Literal[u"organizationUser",b"organizationUser"]) -> None: ...
-type___CreateOrganizationUserRequest = CreateOrganizationUserRequest
-
-class UpdateOrganizationRequest(google___protobuf___message___Message):
-    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
-
-    @property
-    def organization(self) -> type___Organization: ...
-
-    @property
-    def update_mask(self) -> google___protobuf___field_mask_pb2___FieldMask: ...
-
-    def __init__(self,
-        *,
-        organization : typing___Optional[type___Organization] = None,
-        update_mask : typing___Optional[google___protobuf___field_mask_pb2___FieldMask] = None,
-        ) -> None: ...
-    def HasField(self, field_name: typing_extensions___Literal[u"organization",b"organization",u"update_mask",b"update_mask"]) -> builtin___bool: ...
-    def ClearField(self, field_name: typing_extensions___Literal[u"organization",b"organization",u"update_mask",b"update_mask"]) -> None: ...
-type___UpdateOrganizationRequest = UpdateOrganizationRequest
-
-class UpdateOrganizationUserRequest(google___protobuf___message___Message):
-    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
-
-    @property
-    def organization_user(self) -> type___OrganizationUser: ...
-
-    @property
-    def update_mask(self) -> google___protobuf___field_mask_pb2___FieldMask: ...
-
-    def __init__(self,
-        *,
-        organization_user : typing___Optional[type___OrganizationUser] = None,
-        update_mask : typing___Optional[google___protobuf___field_mask_pb2___FieldMask] = None,
-        ) -> None: ...
-    def HasField(self, field_name: typing_extensions___Literal[u"organization_user",b"organization_user",u"update_mask",b"update_mask"]) -> builtin___bool: ...
-    def ClearField(self, field_name: typing_extensions___Literal[u"organization_user",b"organization_user",u"update_mask",b"update_mask"]) -> None: ...
-type___UpdateOrganizationUserRequest = UpdateOrganizationUserRequest
-
-class AccessAndSecretKeys(google___protobuf___message___Message):
-    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
-    access_key_id: typing___Text = ...
-    secret_access_key: typing___Text = ...
-
-    def __init__(self,
-        *,
-        access_key_id : typing___Optional[typing___Text] = None,
-        secret_access_key : typing___Optional[typing___Text] = None,
-        ) -> None: ...
-    def ClearField(self, field_name: typing_extensions___Literal[u"access_key_id",b"access_key_id",u"secret_access_key",b"secret_access_key"]) -> None: ...
-type___AccessAndSecretKeys = AccessAndSecretKeys
-
-class GetOrganizationRequest(google___protobuf___message___Message):
-    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
-    organization_id: typing___Text = ...
-
-    @property
-    def access_and_secret_keys(self) -> type___AccessAndSecretKeys: ...
-
-    def __init__(self,
-        *,
-        organization_id : typing___Optional[typing___Text] = None,
-        access_and_secret_keys : typing___Optional[type___AccessAndSecretKeys] = None,
-        ) -> None: ...
-    def HasField(self, field_name: typing_extensions___Literal[u"access_and_secret_keys",b"access_and_secret_keys",u"organization_id",b"organization_id",u"possible_keys",b"possible_keys"]) -> builtin___bool: ...
-    def ClearField(self, field_name: typing_extensions___Literal[u"access_and_secret_keys",b"access_and_secret_keys",u"organization_id",b"organization_id",u"possible_keys",b"possible_keys"]) -> None: ...
-    def WhichOneof(self, oneof_group: typing_extensions___Literal[u"possible_keys",b"possible_keys"]) -> typing_extensions___Literal["organization_id","access_and_secret_keys"]: ...
-type___GetOrganizationRequest = GetOrganizationRequest
-
-class GetOrganizationUserRequest(google___protobuf___message___Message):
-    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
-    organization_id: typing___Text = ...
-    organization_user_id: typing___Text = ...
-    email: typing___Text = ...
-    invite_email: typing___Text = ...
-    firebase_user_id: typing___Text = ...
-
-    def __init__(self,
-        *,
-        organization_id : typing___Optional[typing___Text] = None,
-        organization_user_id : typing___Optional[typing___Text] = None,
-        email : typing___Optional[typing___Text] = None,
-        invite_email : typing___Optional[typing___Text] = None,
-        firebase_user_id : typing___Optional[typing___Text] = None,
-        ) -> None: ...
-    def HasField(self, field_name: typing_extensions___Literal[u"email",b"email",u"firebase_user_id",b"firebase_user_id",u"invite_email",b"invite_email",u"organization_user_id",b"organization_user_id",u"possible_keys",b"possible_keys"]) -> builtin___bool: ...
-    def ClearField(self, field_name: typing_extensions___Literal[u"email",b"email",u"firebase_user_id",b"firebase_user_id",u"invite_email",b"invite_email",u"organization_id",b"organization_id",u"organization_user_id",b"organization_user_id",u"possible_keys",b"possible_keys"]) -> None: ...
-    def WhichOneof(self, oneof_group: typing_extensions___Literal[u"possible_keys",b"possible_keys"]) -> typing_extensions___Literal["organization_user_id","email","invite_email","firebase_user_id"]: ...
-type___GetOrganizationUserRequest = GetOrganizationUserRequest
-
-class ListOrganizationUsersRequest(google___protobuf___message___Message):
-    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
-    organization_id: typing___Text = ...
-    invite_email: typing___Text = ...
-    firebase_user_id: typing___Text = ...
-
-    def __init__(self,
-        *,
-        organization_id : typing___Optional[typing___Text] = None,
-        invite_email : typing___Optional[typing___Text] = None,
-        firebase_user_id : typing___Optional[typing___Text] = None,
-        ) -> None: ...
-    def HasField(self, field_name: typing_extensions___Literal[u"firebase_user_id",b"firebase_user_id",u"invite_email",b"invite_email",u"organization_id",b"organization_id",u"possible_keys",b"possible_keys"]) -> builtin___bool: ...
-    def ClearField(self, field_name: typing_extensions___Literal[u"firebase_user_id",b"firebase_user_id",u"invite_email",b"invite_email",u"organization_id",b"organization_id",u"possible_keys",b"possible_keys"]) -> None: ...
-    def WhichOneof(self, oneof_group: typing_extensions___Literal[u"possible_keys",b"possible_keys"]) -> typing_extensions___Literal["organization_id","invite_email","firebase_user_id"]: ...
-type___ListOrganizationUsersRequest = ListOrganizationUsersRequest
-
-class SendOrganizationUserInvitesRequest(google___protobuf___message___Message):
-    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
-
-    @property
-    def inviter(self) -> type___OrganizationUser: ...
-
-    @property
-    def invitees(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[type___OrganizationUser]: ...
-
-    def __init__(self,
-        *,
-        inviter : typing___Optional[type___OrganizationUser] = None,
-        invitees : typing___Optional[typing___Iterable[type___OrganizationUser]] = None,
-        ) -> None: ...
-    def HasField(self, field_name: typing_extensions___Literal[u"inviter",b"inviter"]) -> builtin___bool: ...
-    def ClearField(self, field_name: typing_extensions___Literal[u"invitees",b"invitees",u"inviter",b"inviter"]) -> None: ...
-type___SendOrganizationUserInvitesRequest = SendOrganizationUserInvitesRequest
-
-class SendOrganizationUserInvitesResponse(google___protobuf___message___Message):
-    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
-    email_results: google___protobuf___internal___containers___RepeatedScalarFieldContainer[builtin___bool] = ...
-
-    @property
-    def invitees(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[type___OrganizationUser]: ...
-
-    def __init__(self,
-        *,
-        invitees : typing___Optional[typing___Iterable[type___OrganizationUser]] = None,
-        email_results : typing___Optional[typing___Iterable[builtin___bool]] = None,
-        ) -> None: ...
-    def ClearField(self, field_name: typing_extensions___Literal[u"email_results",b"email_results",u"invitees",b"invitees"]) -> None: ...
-type___SendOrganizationUserInvitesResponse = SendOrganizationUserInvitesResponse
-
-class AcceptOrganizationUserInviteRequest(google___protobuf___message___Message):
-    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
-    firebase_user_id: typing___Text = ...
-    invite_token: typing___Text = ...
-
-    def __init__(self,
-        *,
-        firebase_user_id : typing___Optional[typing___Text] = None,
-        invite_token : typing___Optional[typing___Text] = None,
-        ) -> None: ...
-    def ClearField(self, field_name: typing_extensions___Literal[u"firebase_user_id",b"firebase_user_id",u"invite_token",b"invite_token"]) -> None: ...
-type___AcceptOrganizationUserInviteRequest = AcceptOrganizationUserInviteRequest
-
-class AcceptOrganizationUserInviteResponse(google___protobuf___message___Message):
-    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
-
-    @property
-    def organization_user(self) -> type___OrganizationUser: ...
-
-    @property
-    def implicit_organization_users(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[type___OrganizationUser]: ...
-
-    def __init__(self,
-        *,
-        organization_user : typing___Optional[type___OrganizationUser] = None,
-        implicit_organization_users : typing___Optional[typing___Iterable[type___OrganizationUser]] = None,
-        ) -> None: ...
-    def HasField(self, field_name: typing_extensions___Literal[u"organization_user",b"organization_user"]) -> builtin___bool: ...
-    def ClearField(self, field_name: typing_extensions___Literal[u"implicit_organization_users",b"implicit_organization_users",u"organization_user",b"organization_user"]) -> None: ...
-type___AcceptOrganizationUserInviteResponse = AcceptOrganizationUserInviteResponse
-
 class CrmLinkingDefinition(google___protobuf___message___Message):
     DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
     source: integration_source_pb2___IntegrationSourceValue = ...
     linking_field: typing___Text = ...
 
     @property
     def updated_at(self) -> google___protobuf___timestamp_pb2___Timestamp: ...
@@ -574,7 +362,43 @@
         updated_at : typing___Optional[google___protobuf___timestamp_pb2___Timestamp] = None,
         created_by_organization_user_id : typing___Optional[typing___Text] = None,
         deleted_at : typing___Optional[google___protobuf___timestamp_pb2___Timestamp] = None,
         ) -> None: ...
     def HasField(self, field_name: typing_extensions___Literal[u"created_at",b"created_at",u"deleted_at",b"deleted_at",u"updated_at",b"updated_at"]) -> builtin___bool: ...
     def ClearField(self, field_name: typing_extensions___Literal[u"created_at",b"created_at",u"created_by_organization_user_id",b"created_by_organization_user_id",u"deleted_at",b"deleted_at",u"description",b"description",u"folder_id",b"folder_id",u"is_public",b"is_public",u"name",b"name",u"updated_at",b"updated_at"]) -> None: ...
 type___Folder = Folder
+
+class GetFolderRequest(google___protobuf___message___Message):
+    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
+    folder_id: typing___Text = ...
+
+    def __init__(self,
+        *,
+        folder_id : typing___Optional[typing___Text] = None,
+        ) -> None: ...
+    def ClearField(self, field_name: typing_extensions___Literal[u"folder_id",b"folder_id"]) -> None: ...
+type___GetFolderRequest = GetFolderRequest
+
+class PutFolderRequest(google___protobuf___message___Message):
+    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
+
+    @property
+    def folder(self) -> type___Folder: ...
+
+    def __init__(self,
+        *,
+        folder : typing___Optional[type___Folder] = None,
+        ) -> None: ...
+    def HasField(self, field_name: typing_extensions___Literal[u"folder",b"folder"]) -> builtin___bool: ...
+    def ClearField(self, field_name: typing_extensions___Literal[u"folder",b"folder"]) -> None: ...
+type___PutFolderRequest = PutFolderRequest
+
+class DeleteFolderRequest(google___protobuf___message___Message):
+    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
+    folder_id: typing___Text = ...
+
+    def __init__(self,
+        *,
+        folder_id : typing___Optional[typing___Text] = None,
+        ) -> None: ...
+    def ClearField(self, field_name: typing_extensions___Literal[u"folder_id",b"folder_id"]) -> None: ...
+type___DeleteFolderRequest = DeleteFolderRequest
```

### Comparing `calixa-proto-py-2.0.8/calixa_proto_py/organization_pb2_grpc.py` & `calixa-proto-py-2.0.9/calixa_proto_py/organization_service_pb2_grpc.py`

 * *Files 4% similar despite different names*

```diff
@@ -1,83 +1,90 @@
 # Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
 """Client and server classes corresponding to protobuf-defined services."""
 import grpc
 
+import entity_pb2 as entity__pb2
 from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
 import organization_pb2 as organization__pb2
+import organization_service_pb2 as organization__service__pb2
 
 
 class OrganizationServiceStub(object):
     """Missing associated documentation comment in .proto file."""
 
     def __init__(self, channel):
         """Constructor.
 
         Args:
             channel: A grpc.Channel.
         """
         self.CreateOrganization = channel.unary_unary(
                 '/calixa.domain.organization.OrganizationService/CreateOrganization',
-                request_serializer=organization__pb2.CreateOrganizationRequest.SerializeToString,
+                request_serializer=organization__service__pb2.CreateOrganizationRequest.SerializeToString,
                 response_deserializer=organization__pb2.Organization.FromString,
                 )
         self.UpdateOrganization = channel.unary_unary(
                 '/calixa.domain.organization.OrganizationService/UpdateOrganization',
-                request_serializer=organization__pb2.UpdateOrganizationRequest.SerializeToString,
+                request_serializer=organization__service__pb2.UpdateOrganizationRequest.SerializeToString,
                 response_deserializer=organization__pb2.Organization.FromString,
                 )
         self.GetOrganization = channel.unary_unary(
                 '/calixa.domain.organization.OrganizationService/GetOrganization',
-                request_serializer=organization__pb2.GetOrganizationRequest.SerializeToString,
+                request_serializer=organization__service__pb2.GetOrganizationRequest.SerializeToString,
                 response_deserializer=organization__pb2.Organization.FromString,
                 )
         self.GetOrganizations = channel.unary_stream(
                 '/calixa.domain.organization.OrganizationService/GetOrganizations',
                 request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                 response_deserializer=organization__pb2.Organization.FromString,
                 )
         self.CreateOrganizationUser = channel.unary_unary(
                 '/calixa.domain.organization.OrganizationService/CreateOrganizationUser',
-                request_serializer=organization__pb2.CreateOrganizationUserRequest.SerializeToString,
-                response_deserializer=organization__pb2.OrganizationUser.FromString,
+                request_serializer=organization__service__pb2.CreateOrganizationUserRequest.SerializeToString,
+                response_deserializer=entity__pb2.Entity.FromString,
                 )
         self.UpdateOrganizationUser = channel.unary_unary(
                 '/calixa.domain.organization.OrganizationService/UpdateOrganizationUser',
-                request_serializer=organization__pb2.UpdateOrganizationUserRequest.SerializeToString,
-                response_deserializer=organization__pb2.OrganizationUser.FromString,
+                request_serializer=organization__service__pb2.UpdateOrganizationUserRequest.SerializeToString,
+                response_deserializer=entity__pb2.Entity.FromString,
+                )
+        self.PutOrganizationUser = channel.unary_unary(
+                '/calixa.domain.organization.OrganizationService/PutOrganizationUser',
+                request_serializer=entity__pb2.Entity.SerializeToString,
+                response_deserializer=entity__pb2.SaveEntityResponse.FromString,
                 )
         self.GetOrganizationUser = channel.unary_unary(
                 '/calixa.domain.organization.OrganizationService/GetOrganizationUser',
-                request_serializer=organization__pb2.GetOrganizationUserRequest.SerializeToString,
-                response_deserializer=organization__pb2.OrganizationUser.FromString,
+                request_serializer=organization__service__pb2.GetOrganizationUserRequest.SerializeToString,
+                response_deserializer=entity__pb2.Entity.FromString,
                 )
         self.ListOrganizationUsers = channel.unary_stream(
                 '/calixa.domain.organization.OrganizationService/ListOrganizationUsers',
-                request_serializer=organization__pb2.ListOrganizationUsersRequest.SerializeToString,
-                response_deserializer=organization__pb2.OrganizationUser.FromString,
+                request_serializer=organization__service__pb2.ListOrganizationUsersRequest.SerializeToString,
+                response_deserializer=entity__pb2.Entity.FromString,
                 )
         self.CreateAccessKey = channel.unary_unary(
                 '/calixa.domain.organization.OrganizationService/CreateAccessKey',
-                request_serializer=organization__pb2.CreateKeyRequest.SerializeToString,
+                request_serializer=organization__service__pb2.CreateKeyRequest.SerializeToString,
                 response_deserializer=organization__pb2.AccessKey.FromString,
                 )
         self.GetAccessKeys = channel.unary_stream(
                 '/calixa.domain.organization.OrganizationService/GetAccessKeys',
-                request_serializer=organization__pb2.GetOrganizationRequest.SerializeToString,
+                request_serializer=organization__service__pb2.GetOrganizationRequest.SerializeToString,
                 response_deserializer=organization__pb2.AccessKey.FromString,
                 )
         self.SendOrganizationUserInvite = channel.unary_unary(
                 '/calixa.domain.organization.OrganizationService/SendOrganizationUserInvite',
-                request_serializer=organization__pb2.SendOrganizationUserInvitesRequest.SerializeToString,
-                response_deserializer=organization__pb2.SendOrganizationUserInvitesResponse.FromString,
+                request_serializer=organization__service__pb2.SendOrganizationUserInvitesRequest.SerializeToString,
+                response_deserializer=organization__service__pb2.SendOrganizationUserInvitesResponse.FromString,
                 )
         self.AcceptOrganizationUserInvite = channel.unary_unary(
                 '/calixa.domain.organization.OrganizationService/AcceptOrganizationUserInvite',
-                request_serializer=organization__pb2.AcceptOrganizationUserInviteRequest.SerializeToString,
-                response_deserializer=organization__pb2.AcceptOrganizationUserInviteResponse.FromString,
+                request_serializer=organization__service__pb2.AcceptOrganizationUserInviteRequest.SerializeToString,
+                response_deserializer=organization__service__pb2.AcceptOrganizationUserInviteResponse.FromString,
                 )
 
 
 class OrganizationServiceServicer(object):
     """Missing associated documentation comment in .proto file."""
 
     def CreateOrganization(self, request, context):
@@ -112,14 +119,20 @@
 
     def UpdateOrganizationUser(self, request, context):
         """Missing associated documentation comment in .proto file."""
         context.set_code(grpc.StatusCode.UNIMPLEMENTED)
         context.set_details('Method not implemented!')
         raise NotImplementedError('Method not implemented!')
 
+    def PutOrganizationUser(self, request, context):
+        """Missing associated documentation comment in .proto file."""
+        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
+        context.set_details('Method not implemented!')
+        raise NotImplementedError('Method not implemented!')
+
     def GetOrganizationUser(self, request, context):
         """Missing associated documentation comment in .proto file."""
         context.set_code(grpc.StatusCode.UNIMPLEMENTED)
         context.set_details('Method not implemented!')
         raise NotImplementedError('Method not implemented!')
 
     def ListOrganizationUsers(self, request, context):
@@ -153,71 +166,76 @@
         raise NotImplementedError('Method not implemented!')
 
 
 def add_OrganizationServiceServicer_to_server(servicer, server):
     rpc_method_handlers = {
             'CreateOrganization': grpc.unary_unary_rpc_method_handler(
                     servicer.CreateOrganization,
-                    request_deserializer=organization__pb2.CreateOrganizationRequest.FromString,
+                    request_deserializer=organization__service__pb2.CreateOrganizationRequest.FromString,
                     response_serializer=organization__pb2.Organization.SerializeToString,
             ),
             'UpdateOrganization': grpc.unary_unary_rpc_method_handler(
                     servicer.UpdateOrganization,
-                    request_deserializer=organization__pb2.UpdateOrganizationRequest.FromString,
+                    request_deserializer=organization__service__pb2.UpdateOrganizationRequest.FromString,
                     response_serializer=organization__pb2.Organization.SerializeToString,
             ),
             'GetOrganization': grpc.unary_unary_rpc_method_handler(
                     servicer.GetOrganization,
-                    request_deserializer=organization__pb2.GetOrganizationRequest.FromString,
+                    request_deserializer=organization__service__pb2.GetOrganizationRequest.FromString,
                     response_serializer=organization__pb2.Organization.SerializeToString,
             ),
             'GetOrganizations': grpc.unary_stream_rpc_method_handler(
                     servicer.GetOrganizations,
                     request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                     response_serializer=organization__pb2.Organization.SerializeToString,
             ),
             'CreateOrganizationUser': grpc.unary_unary_rpc_method_handler(
                     servicer.CreateOrganizationUser,
-                    request_deserializer=organization__pb2.CreateOrganizationUserRequest.FromString,
-                    response_serializer=organization__pb2.OrganizationUser.SerializeToString,
+                    request_deserializer=organization__service__pb2.CreateOrganizationUserRequest.FromString,
+                    response_serializer=entity__pb2.Entity.SerializeToString,
             ),
             'UpdateOrganizationUser': grpc.unary_unary_rpc_method_handler(
                     servicer.UpdateOrganizationUser,
-                    request_deserializer=organization__pb2.UpdateOrganizationUserRequest.FromString,
-                    response_serializer=organization__pb2.OrganizationUser.SerializeToString,
+                    request_deserializer=organization__service__pb2.UpdateOrganizationUserRequest.FromString,
+                    response_serializer=entity__pb2.Entity.SerializeToString,
+            ),
+            'PutOrganizationUser': grpc.unary_unary_rpc_method_handler(
+                    servicer.PutOrganizationUser,
+                    request_deserializer=entity__pb2.Entity.FromString,
+                    response_serializer=entity__pb2.SaveEntityResponse.SerializeToString,
             ),
             'GetOrganizationUser': grpc.unary_unary_rpc_method_handler(
                     servicer.GetOrganizationUser,
-                    request_deserializer=organization__pb2.GetOrganizationUserRequest.FromString,
-                    response_serializer=organization__pb2.OrganizationUser.SerializeToString,
+                    request_deserializer=organization__service__pb2.GetOrganizationUserRequest.FromString,
+                    response_serializer=entity__pb2.Entity.SerializeToString,
             ),
             'ListOrganizationUsers': grpc.unary_stream_rpc_method_handler(
                     servicer.ListOrganizationUsers,
-                    request_deserializer=organization__pb2.ListOrganizationUsersRequest.FromString,
-                    response_serializer=organization__pb2.OrganizationUser.SerializeToString,
+                    request_deserializer=organization__service__pb2.ListOrganizationUsersRequest.FromString,
+                    response_serializer=entity__pb2.Entity.SerializeToString,
             ),
             'CreateAccessKey': grpc.unary_unary_rpc_method_handler(
                     servicer.CreateAccessKey,
-                    request_deserializer=organization__pb2.CreateKeyRequest.FromString,
+                    request_deserializer=organization__service__pb2.CreateKeyRequest.FromString,
                     response_serializer=organization__pb2.AccessKey.SerializeToString,
             ),
             'GetAccessKeys': grpc.unary_stream_rpc_method_handler(
                     servicer.GetAccessKeys,
-                    request_deserializer=organization__pb2.GetOrganizationRequest.FromString,
+                    request_deserializer=organization__service__pb2.GetOrganizationRequest.FromString,
                     response_serializer=organization__pb2.AccessKey.SerializeToString,
             ),
             'SendOrganizationUserInvite': grpc.unary_unary_rpc_method_handler(
                     servicer.SendOrganizationUserInvite,
-                    request_deserializer=organization__pb2.SendOrganizationUserInvitesRequest.FromString,
-                    response_serializer=organization__pb2.SendOrganizationUserInvitesResponse.SerializeToString,
+                    request_deserializer=organization__service__pb2.SendOrganizationUserInvitesRequest.FromString,
+                    response_serializer=organization__service__pb2.SendOrganizationUserInvitesResponse.SerializeToString,
             ),
             'AcceptOrganizationUserInvite': grpc.unary_unary_rpc_method_handler(
                     servicer.AcceptOrganizationUserInvite,
-                    request_deserializer=organization__pb2.AcceptOrganizationUserInviteRequest.FromString,
-                    response_serializer=organization__pb2.AcceptOrganizationUserInviteResponse.SerializeToString,
+                    request_deserializer=organization__service__pb2.AcceptOrganizationUserInviteRequest.FromString,
+                    response_serializer=organization__service__pb2.AcceptOrganizationUserInviteResponse.SerializeToString,
             ),
     }
     generic_handler = grpc.method_handlers_generic_handler(
             'calixa.domain.organization.OrganizationService', rpc_method_handlers)
     server.add_generic_rpc_handlers((generic_handler,))
 
 
@@ -233,15 +251,15 @@
             call_credentials=None,
             insecure=False,
             compression=None,
             wait_for_ready=None,
             timeout=None,
             metadata=None):
         return grpc.experimental.unary_unary(request, target, '/calixa.domain.organization.OrganizationService/CreateOrganization',
-            organization__pb2.CreateOrganizationRequest.SerializeToString,
+            organization__service__pb2.CreateOrganizationRequest.SerializeToString,
             organization__pb2.Organization.FromString,
             options, channel_credentials,
             insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
 
     @staticmethod
     def UpdateOrganization(request,
             target,
@@ -250,15 +268,15 @@
             call_credentials=None,
             insecure=False,
             compression=None,
             wait_for_ready=None,
             timeout=None,
             metadata=None):
         return grpc.experimental.unary_unary(request, target, '/calixa.domain.organization.OrganizationService/UpdateOrganization',
-            organization__pb2.UpdateOrganizationRequest.SerializeToString,
+            organization__service__pb2.UpdateOrganizationRequest.SerializeToString,
             organization__pb2.Organization.FromString,
             options, channel_credentials,
             insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
 
     @staticmethod
     def GetOrganization(request,
             target,
@@ -267,15 +285,15 @@
             call_credentials=None,
             insecure=False,
             compression=None,
             wait_for_ready=None,
             timeout=None,
             metadata=None):
         return grpc.experimental.unary_unary(request, target, '/calixa.domain.organization.OrganizationService/GetOrganization',
-            organization__pb2.GetOrganizationRequest.SerializeToString,
+            organization__service__pb2.GetOrganizationRequest.SerializeToString,
             organization__pb2.Organization.FromString,
             options, channel_credentials,
             insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
 
     @staticmethod
     def GetOrganizations(request,
             target,
@@ -301,16 +319,16 @@
             call_credentials=None,
             insecure=False,
             compression=None,
             wait_for_ready=None,
             timeout=None,
             metadata=None):
         return grpc.experimental.unary_unary(request, target, '/calixa.domain.organization.OrganizationService/CreateOrganizationUser',
-            organization__pb2.CreateOrganizationUserRequest.SerializeToString,
-            organization__pb2.OrganizationUser.FromString,
+            organization__service__pb2.CreateOrganizationUserRequest.SerializeToString,
+            entity__pb2.Entity.FromString,
             options, channel_credentials,
             insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
 
     @staticmethod
     def UpdateOrganizationUser(request,
             target,
             options=(),
@@ -318,16 +336,33 @@
             call_credentials=None,
             insecure=False,
             compression=None,
             wait_for_ready=None,
             timeout=None,
             metadata=None):
         return grpc.experimental.unary_unary(request, target, '/calixa.domain.organization.OrganizationService/UpdateOrganizationUser',
-            organization__pb2.UpdateOrganizationUserRequest.SerializeToString,
-            organization__pb2.OrganizationUser.FromString,
+            organization__service__pb2.UpdateOrganizationUserRequest.SerializeToString,
+            entity__pb2.Entity.FromString,
+            options, channel_credentials,
+            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
+
+    @staticmethod
+    def PutOrganizationUser(request,
+            target,
+            options=(),
+            channel_credentials=None,
+            call_credentials=None,
+            insecure=False,
+            compression=None,
+            wait_for_ready=None,
+            timeout=None,
+            metadata=None):
+        return grpc.experimental.unary_unary(request, target, '/calixa.domain.organization.OrganizationService/PutOrganizationUser',
+            entity__pb2.Entity.SerializeToString,
+            entity__pb2.SaveEntityResponse.FromString,
             options, channel_credentials,
             insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
 
     @staticmethod
     def GetOrganizationUser(request,
             target,
             options=(),
@@ -335,16 +370,16 @@
             call_credentials=None,
             insecure=False,
             compression=None,
             wait_for_ready=None,
             timeout=None,
             metadata=None):
         return grpc.experimental.unary_unary(request, target, '/calixa.domain.organization.OrganizationService/GetOrganizationUser',
-            organization__pb2.GetOrganizationUserRequest.SerializeToString,
-            organization__pb2.OrganizationUser.FromString,
+            organization__service__pb2.GetOrganizationUserRequest.SerializeToString,
+            entity__pb2.Entity.FromString,
             options, channel_credentials,
             insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
 
     @staticmethod
     def ListOrganizationUsers(request,
             target,
             options=(),
@@ -352,16 +387,16 @@
             call_credentials=None,
             insecure=False,
             compression=None,
             wait_for_ready=None,
             timeout=None,
             metadata=None):
         return grpc.experimental.unary_stream(request, target, '/calixa.domain.organization.OrganizationService/ListOrganizationUsers',
-            organization__pb2.ListOrganizationUsersRequest.SerializeToString,
-            organization__pb2.OrganizationUser.FromString,
+            organization__service__pb2.ListOrganizationUsersRequest.SerializeToString,
+            entity__pb2.Entity.FromString,
             options, channel_credentials,
             insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
 
     @staticmethod
     def CreateAccessKey(request,
             target,
             options=(),
@@ -369,15 +404,15 @@
             call_credentials=None,
             insecure=False,
             compression=None,
             wait_for_ready=None,
             timeout=None,
             metadata=None):
         return grpc.experimental.unary_unary(request, target, '/calixa.domain.organization.OrganizationService/CreateAccessKey',
-            organization__pb2.CreateKeyRequest.SerializeToString,
+            organization__service__pb2.CreateKeyRequest.SerializeToString,
             organization__pb2.AccessKey.FromString,
             options, channel_credentials,
             insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
 
     @staticmethod
     def GetAccessKeys(request,
             target,
@@ -386,15 +421,15 @@
             call_credentials=None,
             insecure=False,
             compression=None,
             wait_for_ready=None,
             timeout=None,
             metadata=None):
         return grpc.experimental.unary_stream(request, target, '/calixa.domain.organization.OrganizationService/GetAccessKeys',
-            organization__pb2.GetOrganizationRequest.SerializeToString,
+            organization__service__pb2.GetOrganizationRequest.SerializeToString,
             organization__pb2.AccessKey.FromString,
             options, channel_credentials,
             insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
 
     @staticmethod
     def SendOrganizationUserInvite(request,
             target,
@@ -403,16 +438,16 @@
             call_credentials=None,
             insecure=False,
             compression=None,
             wait_for_ready=None,
             timeout=None,
             metadata=None):
         return grpc.experimental.unary_unary(request, target, '/calixa.domain.organization.OrganizationService/SendOrganizationUserInvite',
-            organization__pb2.SendOrganizationUserInvitesRequest.SerializeToString,
-            organization__pb2.SendOrganizationUserInvitesResponse.FromString,
+            organization__service__pb2.SendOrganizationUserInvitesRequest.SerializeToString,
+            organization__service__pb2.SendOrganizationUserInvitesResponse.FromString,
             options, channel_credentials,
             insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
 
     @staticmethod
     def AcceptOrganizationUserInvite(request,
             target,
             options=(),
@@ -420,11 +455,11 @@
             call_credentials=None,
             insecure=False,
             compression=None,
             wait_for_ready=None,
             timeout=None,
             metadata=None):
         return grpc.experimental.unary_unary(request, target, '/calixa.domain.organization.OrganizationService/AcceptOrganizationUserInvite',
-            organization__pb2.AcceptOrganizationUserInviteRequest.SerializeToString,
-            organization__pb2.AcceptOrganizationUserInviteResponse.FromString,
+            organization__service__pb2.AcceptOrganizationUserInviteRequest.SerializeToString,
+            organization__service__pb2.AcceptOrganizationUserInviteResponse.FromString,
             options, channel_credentials,
             insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
```

### Comparing `calixa-proto-py-2.0.8/calixa_proto_py/owner.proto` & `calixa-proto-py-2.0.9/calixa_proto_py/owner.proto`

 * *Files identical despite different names*

### Comparing `calixa-proto-py-2.0.8/calixa_proto_py/owner_pb2.pyi` & `calixa-proto-py-2.0.9/calixa_proto_py/owner_pb2.pyi`

 * *Files 5% similar despite different names*

```diff
@@ -1,11 +1,9 @@
-"""
-@generated by mypy-protobuf.  Do not edit manually!
-isort:skip_file
-"""
+# @generated by generate_proto_mypy_stubs.py.  Do not edit!
+import sys
 from google.protobuf.descriptor import (
     Descriptor as google___protobuf___descriptor___Descriptor,
     EnumDescriptor as google___protobuf___descriptor___EnumDescriptor,
     FileDescriptor as google___protobuf___descriptor___FileDescriptor,
 )
 
 from google.protobuf.internal.enum_type_wrapper import (
@@ -45,14 +43,15 @@
     OWNERSHIP_TYPE_CALIXA = typing___cast(OwnershipTypeValue, 1)
     OWNERSHIP_TYPE_HUBSPOT = typing___cast(OwnershipTypeValue, 2)
     OWNERSHIP_TYPE_SALESFORCE = typing___cast(OwnershipTypeValue, 3)
 OWNERSHIP_TYPE_UNSPECIFIED = typing___cast(OwnershipTypeValue, 0)
 OWNERSHIP_TYPE_CALIXA = typing___cast(OwnershipTypeValue, 1)
 OWNERSHIP_TYPE_HUBSPOT = typing___cast(OwnershipTypeValue, 2)
 OWNERSHIP_TYPE_SALESFORCE = typing___cast(OwnershipTypeValue, 3)
+type___OwnershipType = OwnershipType
 
 class Owner(google___protobuf___message___Message):
     DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
     id: typing___Text = ...
     type: type___OwnershipTypeValue = ...
 
     def __init__(self,
```

### Comparing `calixa-proto-py-2.0.8/calixa_proto_py/pubsub_pb2.pyi` & `calixa-proto-py-2.0.9/calixa_proto_py/pubsub_pb2.pyi`

 * *Files 6% similar despite different names*

```diff
@@ -1,11 +1,9 @@
-"""
-@generated by mypy-protobuf.  Do not edit manually!
-isort:skip_file
-"""
+# @generated by generate_proto_mypy_stubs.py.  Do not edit!
+import sys
 from common_pb2 import (
     RequestContext as common_pb2___RequestContext,
 )
 
 from google.protobuf.any_pb2 import (
     Any as google___protobuf___any_pb2___Any,
 )
```

### Comparing `calixa-proto-py-2.0.8/calixa_proto_py/push_notification.proto` & `calixa-proto-py-2.0.9/calixa_proto_py/push_notification.proto`

 * *Files identical despite different names*

### Comparing `calixa-proto-py-2.0.8/calixa_proto_py/push_notification_pb2.pyi` & `calixa-proto-py-2.0.9/calixa_proto_py/push_notification_pb2.pyi`

 * *Files 1% similar despite different names*

```diff
@@ -1,11 +1,9 @@
-"""
-@generated by mypy-protobuf.  Do not edit manually!
-isort:skip_file
-"""
+# @generated by generate_proto_mypy_stubs.py.  Do not edit!
+import sys
 from action_pb2 import (
     RequestConfig as action_pb2___RequestConfig,
 )
 
 from google.protobuf.descriptor import (
     Descriptor as google___protobuf___descriptor___Descriptor,
     EnumDescriptor as google___protobuf___descriptor___EnumDescriptor,
@@ -61,14 +59,15 @@
 WEBHOOK = typing___cast(TemplateValue, 3)
 SLACK = typing___cast(TemplateValue, 4)
 TRACK_EVENT_AUTOMATION_EMAIL = typing___cast(TemplateValue, 5)
 TRACK_EVENT_AUTOMATION_SLACK = typing___cast(TemplateValue, 6)
 EMAIL_AUTOMATION_METRICS = typing___cast(TemplateValue, 7)
 SLACK_AUTOMATION_METRICS = typing___cast(TemplateValue, 8)
 EMAIL_INVITE = typing___cast(TemplateValue, 9)
+type___Template = Template
 
 NotificationFrequencyValue = typing___NewType('NotificationFrequencyValue', builtin___int)
 type___NotificationFrequencyValue = NotificationFrequencyValue
 NotificationFrequency: _NotificationFrequency
 class _NotificationFrequency(google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper[NotificationFrequencyValue]):
     DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
     NOTIFICATION_FREQUENCY_UNSPECIFIED = typing___cast(NotificationFrequencyValue, 0)
@@ -83,14 +82,15 @@
 NOTIFICATION_FREQUENCY_HOURLY = typing___cast(NotificationFrequencyValue, 1)
 NOTIFICATION_FREQUENCY_DAILY = typing___cast(NotificationFrequencyValue, 2)
 NOTIFICATION_FREQUENCY_WEEKLY = typing___cast(NotificationFrequencyValue, 3)
 NOTIFICATION_FREQUENCY_MONTHLY = typing___cast(NotificationFrequencyValue, 4)
 NOTIFICATION_FREQUENCY_QUARTERLY = typing___cast(NotificationFrequencyValue, 5)
 NOTIFICATION_FREQUENCY_YEARLY = typing___cast(NotificationFrequencyValue, 6)
 NOTIFICATION_FREQUENCY_ALL_TIME = typing___cast(NotificationFrequencyValue, 1000)
+type___NotificationFrequency = NotificationFrequency
 
 class Notification(google___protobuf___message___Message):
     DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
     organization_id: typing___Text = ...
     template: type___TemplateValue = ...
     notification_frequency: type___NotificationFrequencyValue = ...
     time_zone: typing___Text = ...
```

### Comparing `calixa-proto-py-2.0.8/calixa_proto_py/related_data.proto` & `calixa-proto-py-2.0.9/calixa_proto_py/related_data.proto`

 * *Files 2% similar despite different names*

```diff
@@ -14,14 +14,15 @@
   RELATED_DATA_TYPE_SUBSCRIPTION = 2; // Retrieve Subscription IDs (internally)
   RELATED_DATA_TYPE_OPPORTUNITY = 3;  // Retrieve Opportunity Stage Name + Owner ID
   RELATED_DATA_TYPE_TASK = 4;         // Retrieve Task Owner ID
   RELATED_DATA_TYPE_CADENCE = 5;      // Retrieve Available Cadence
   RELATED_DATA_TYPE_SEQUENCE = 6;     // Retrieve Available Sequences + Mailboxes
 
   RELATED_DATA_TYPE_SLACK_CHANNEL = 10000;  // EXPERIMENTAL: Retrieve channel Slack channel names
+  RELATED_DATA_TYPE_CONTACT_LIST = 7; // Retrieve contact lists 
 }
 
 /*
  * Types of fields supported by Related Data API
  */
 enum RelatedDataFieldType {
   RELATED_DATA_FIELD_TYPE_UNSPECIFIED = 0;
```

### Comparing `calixa-proto-py-2.0.8/calixa_proto_py/related_data_pb2.pyi` & `calixa-proto-py-2.0.9/calixa_proto_py/related_data_pb2.pyi`

 * *Files 8% similar despite different names*

```diff
@@ -1,33 +1,31 @@
-"""
-@generated by mypy-protobuf.  Do not edit manually!
-isort:skip_file
-"""
+# @generated by generate_proto_mypy_stubs.py.  Do not edit!
+import sys
 from google.protobuf.descriptor import (
     Descriptor as google___protobuf___descriptor___Descriptor,
     EnumDescriptor as google___protobuf___descriptor___EnumDescriptor,
     FileDescriptor as google___protobuf___descriptor___FileDescriptor,
 )
 
 from google.protobuf.internal.containers import (
-    MessageMap as google___protobuf___internal___containers___MessageMap,
     RepeatedCompositeFieldContainer as google___protobuf___internal___containers___RepeatedCompositeFieldContainer,
 )
 
 from google.protobuf.internal.enum_type_wrapper import (
     _EnumTypeWrapper as google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper,
 )
 
 from google.protobuf.message import (
     Message as google___protobuf___message___Message,
 )
 
 from typing import (
     Iterable as typing___Iterable,
     Mapping as typing___Mapping,
+    MutableMapping as typing___MutableMapping,
     NewType as typing___NewType,
     Optional as typing___Optional,
     Text as typing___Text,
     cast as typing___cast,
 )
 
 from typing_extensions import (
@@ -52,22 +50,25 @@
     RELATED_DATA_TYPE_COUPON = typing___cast(RelatedDataTypeValue, 1)
     RELATED_DATA_TYPE_SUBSCRIPTION = typing___cast(RelatedDataTypeValue, 2)
     RELATED_DATA_TYPE_OPPORTUNITY = typing___cast(RelatedDataTypeValue, 3)
     RELATED_DATA_TYPE_TASK = typing___cast(RelatedDataTypeValue, 4)
     RELATED_DATA_TYPE_CADENCE = typing___cast(RelatedDataTypeValue, 5)
     RELATED_DATA_TYPE_SEQUENCE = typing___cast(RelatedDataTypeValue, 6)
     RELATED_DATA_TYPE_SLACK_CHANNEL = typing___cast(RelatedDataTypeValue, 10000)
+    RELATED_DATA_TYPE_CONTACT_LIST = typing___cast(RelatedDataTypeValue, 7)
 RELATED_DATA_TYPE_UNSPECIFIED = typing___cast(RelatedDataTypeValue, 0)
 RELATED_DATA_TYPE_COUPON = typing___cast(RelatedDataTypeValue, 1)
 RELATED_DATA_TYPE_SUBSCRIPTION = typing___cast(RelatedDataTypeValue, 2)
 RELATED_DATA_TYPE_OPPORTUNITY = typing___cast(RelatedDataTypeValue, 3)
 RELATED_DATA_TYPE_TASK = typing___cast(RelatedDataTypeValue, 4)
 RELATED_DATA_TYPE_CADENCE = typing___cast(RelatedDataTypeValue, 5)
 RELATED_DATA_TYPE_SEQUENCE = typing___cast(RelatedDataTypeValue, 6)
 RELATED_DATA_TYPE_SLACK_CHANNEL = typing___cast(RelatedDataTypeValue, 10000)
+RELATED_DATA_TYPE_CONTACT_LIST = typing___cast(RelatedDataTypeValue, 7)
+type___RelatedDataType = RelatedDataType
 
 RelatedDataFieldTypeValue = typing___NewType('RelatedDataFieldTypeValue', builtin___int)
 type___RelatedDataFieldTypeValue = RelatedDataFieldTypeValue
 RelatedDataFieldType: _RelatedDataFieldType
 class _RelatedDataFieldType(google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper[RelatedDataFieldTypeValue]):
     DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
     RELATED_DATA_FIELD_TYPE_UNSPECIFIED = typing___cast(RelatedDataFieldTypeValue, 0)
@@ -92,14 +93,15 @@
 RELATED_DATA_FIELD_TYPE_ENUM = typing___cast(RelatedDataFieldTypeValue, 6)
 RELATED_DATA_FIELD_TYPE_MICROS = typing___cast(RelatedDataFieldTypeValue, 7)
 RELATED_DATA_FIELD_TYPE_NUMBER = typing___cast(RelatedDataFieldTypeValue, 8)
 RELATED_DATA_FIELD_TYPE_PERCENTAGE = typing___cast(RelatedDataFieldTypeValue, 9)
 RELATED_DATA_FIELD_TYPE_STRING = typing___cast(RelatedDataFieldTypeValue, 10)
 RELATED_DATA_FIELD_TYPE_RENDERABLE = typing___cast(RelatedDataFieldTypeValue, 11)
 RELATED_DATA_FIELD_TYPE_HIDDEN = typing___cast(RelatedDataFieldTypeValue, 12)
+type___RelatedDataFieldType = RelatedDataFieldType
 
 class RelatedData(google___protobuf___message___Message):
     DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
     class PropertiesEntry(google___protobuf___message___Message):
         DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
         key: typing___Text = ...
 
@@ -121,15 +123,15 @@
     has_other: builtin___bool = ...
     associated_with: typing___Text = ...
 
     @property
     def values(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[type___Value]: ...
 
     @property
-    def properties(self) -> google___protobuf___internal___containers___MessageMap[typing___Text, type___Property]: ...
+    def properties(self) -> typing___MutableMapping[typing___Text, type___Property]: ...
 
     def __init__(self,
         *,
         field : typing___Optional[typing___Text] = None,
         display : typing___Optional[typing___Text] = None,
         field_type : typing___Optional[type___RelatedDataFieldTypeValue] = None,
         has_other : typing___Optional[builtin___bool] = None,
```

### Comparing `calixa-proto-py-2.0.8/calixa_proto_py/search.proto` & `calixa-proto-py-2.0.9/calixa_proto_py/search.proto`

 * *Files 17% similar despite different names*

```diff
@@ -9,14 +9,15 @@
 import "collaboration_entity.proto";
 import "entity.proto";
 import "common.proto";
 import "counter.proto";
 import "automation_log.proto";
 import "condition.proto";
 import "automation.proto";
+import "metric.proto";
 
 option java_package = "io.calixa.domain.search";
 option java_multiple_files = true;
 option optimize_for = SPEED;
 
 package calixa.domain.search;
 
@@ -153,23 +154,59 @@
 enum SortType {
   SORT_TYPE_UNSPECIFIED = 0;
   SORT_TYPE_PROPERTY = 1; // limited capability
   SORT_TYPE_METRIC = 2;
   SORT_TYPE_DELTA = 3;
   SORT_TYPE_SCORING_FUNCTION = 4;
   SORT_TYPE_JOURNEY = 5;
+  SORT_TYPE_PREDICTION = 6;
 }
 
 message TrendSearchRequest {
   string organization_id = 1;
   calixa.domain.common.EntityType entity_type = 2;
   calixa.domain.condition.ConditionGroup condition = 3;
   repeated MetricWithTimeRange rank_metrics = 4;
   int32 page = 5;
   int32 hits_per_page = 6;
   SortType sort_type = 7;
   string sort_field_type = 10;
-  // property key or metric id
+  // property key or metric id or prediction id
   string sort_field = 8;
   bool sort_asc = 9;
   repeated calixa.domain.condition.ConditionOrGroup columns = 11;
 }
+
+enum RollupType {
+  ROLLUP_TYPE_UNSPECIFIED = 0;
+  ROLLUP_TYPE_EMAIL_DOMAIN = 1;
+}
+
+message TrendSearchRollupRequest {
+  string organization_id = 1;
+  calixa.domain.common.EntityType entity_type = 2;
+  calixa.domain.condition.ConditionGroup condition = 3; // filters
+  repeated MetricWithTimeRange rank_metrics = 4;
+  RollupType rollup_type = 5;
+
+  int32 page = 6;
+  int32 hits_per_page = 7;
+  SortType sort_type = 8;
+  string sort_field_type = 9;
+  // property key or metric id
+  string sort_field = 10;
+  bool sort_asc = 11;
+  repeated calixa.domain.condition.ConditionOrGroup columns = 12;
+}
+
+message TrendSearchRollupResponse {
+  string organization_id = 1;
+  repeated TrendSearchRollupRow rows = 2;
+}
+
+message TrendSearchRollupRow {
+  string predicate = 1; // this is domain name for now, let's see what the future holds...
+  int64 accounts_count = 2;
+  int64 users_count = 3;
+  repeated string owners = 4; // list of owner canonical ids
+  map<string, calixa.domain.metric.AggregatedMetric> aggregated_metrics = 5; // metrics
+}
```

### Comparing `calixa-proto-py-2.0.8/calixa_proto_py/search_pb2.pyi` & `calixa-proto-py-2.0.9/calixa_proto_py/search_pb2.pyi`

 * *Files 13% similar despite different names*

```diff
@@ -1,11 +1,9 @@
-"""
-@generated by mypy-protobuf.  Do not edit manually!
-isort:skip_file
-"""
+# @generated by generate_proto_mypy_stubs.py.  Do not edit!
+import sys
 from automation_log_pb2 import (
     AutomationLog as automation_log_pb2___AutomationLog,
 )
 
 from common_pb2 import (
     EntityTypeValue as common_pb2___EntityTypeValue,
 )
@@ -28,32 +26,36 @@
     EnumDescriptor as google___protobuf___descriptor___EnumDescriptor,
     FileDescriptor as google___protobuf___descriptor___FileDescriptor,
 )
 
 from google.protobuf.internal.containers import (
     RepeatedCompositeFieldContainer as google___protobuf___internal___containers___RepeatedCompositeFieldContainer,
     RepeatedScalarFieldContainer as google___protobuf___internal___containers___RepeatedScalarFieldContainer,
-    ScalarMap as google___protobuf___internal___containers___ScalarMap,
 )
 
 from google.protobuf.internal.enum_type_wrapper import (
     _EnumTypeWrapper as google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper,
 )
 
 from google.protobuf.message import (
     Message as google___protobuf___message___Message,
 )
 
 from google.protobuf.timestamp_pb2 import (
     Timestamp as google___protobuf___timestamp_pb2___Timestamp,
 )
 
+from metric_pb2 import (
+    AggregatedMetric as metric_pb2___AggregatedMetric,
+)
+
 from typing import (
     Iterable as typing___Iterable,
     Mapping as typing___Mapping,
+    MutableMapping as typing___MutableMapping,
     NewType as typing___NewType,
     Optional as typing___Optional,
     Text as typing___Text,
     cast as typing___cast,
 )
 
 from typing_extensions import (
@@ -76,20 +78,34 @@
     DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
     SORT_TYPE_UNSPECIFIED = typing___cast(SortTypeValue, 0)
     SORT_TYPE_PROPERTY = typing___cast(SortTypeValue, 1)
     SORT_TYPE_METRIC = typing___cast(SortTypeValue, 2)
     SORT_TYPE_DELTA = typing___cast(SortTypeValue, 3)
     SORT_TYPE_SCORING_FUNCTION = typing___cast(SortTypeValue, 4)
     SORT_TYPE_JOURNEY = typing___cast(SortTypeValue, 5)
+    SORT_TYPE_PREDICTION = typing___cast(SortTypeValue, 6)
 SORT_TYPE_UNSPECIFIED = typing___cast(SortTypeValue, 0)
 SORT_TYPE_PROPERTY = typing___cast(SortTypeValue, 1)
 SORT_TYPE_METRIC = typing___cast(SortTypeValue, 2)
 SORT_TYPE_DELTA = typing___cast(SortTypeValue, 3)
 SORT_TYPE_SCORING_FUNCTION = typing___cast(SortTypeValue, 4)
 SORT_TYPE_JOURNEY = typing___cast(SortTypeValue, 5)
+SORT_TYPE_PREDICTION = typing___cast(SortTypeValue, 6)
+type___SortType = SortType
+
+RollupTypeValue = typing___NewType('RollupTypeValue', builtin___int)
+type___RollupTypeValue = RollupTypeValue
+RollupType: _RollupType
+class _RollupType(google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper[RollupTypeValue]):
+    DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
+    ROLLUP_TYPE_UNSPECIFIED = typing___cast(RollupTypeValue, 0)
+    ROLLUP_TYPE_EMAIL_DOMAIN = typing___cast(RollupTypeValue, 1)
+ROLLUP_TYPE_UNSPECIFIED = typing___cast(RollupTypeValue, 0)
+ROLLUP_TYPE_EMAIL_DOMAIN = typing___cast(RollupTypeValue, 1)
+type___RollupType = RollupType
 
 class SearchParameters(google___protobuf___message___Message):
     DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
     entity: common_pb2___EntityTypeValue = ...
     automation_log: builtin___bool = ...
     action_invocation_log: builtin___bool = ...
     filters: typing___Text = ...
@@ -184,15 +200,15 @@
             ) -> None: ...
         def ClearField(self, field_name: typing_extensions___Literal[u"key",b"key",u"value",b"value"]) -> None: ...
     type___ValuesEntry = ValuesEntry
 
     facet_name: typing___Text = ...
 
     @property
-    def values(self) -> google___protobuf___internal___containers___ScalarMap[typing___Text, builtin___int]: ...
+    def values(self) -> typing___MutableMapping[typing___Text, builtin___int]: ...
 
     def __init__(self,
         *,
         facet_name : typing___Optional[typing___Text] = None,
         values : typing___Optional[typing___Mapping[typing___Text, builtin___int]] = None,
         ) -> None: ...
     def ClearField(self, field_name: typing_extensions___Literal[u"facet_name",b"facet_name",u"values",b"values"]) -> None: ...
@@ -346,7 +362,99 @@
         sort_field : typing___Optional[typing___Text] = None,
         sort_asc : typing___Optional[builtin___bool] = None,
         columns : typing___Optional[typing___Iterable[condition_pb2___ConditionOrGroup]] = None,
         ) -> None: ...
     def HasField(self, field_name: typing_extensions___Literal[u"condition",b"condition"]) -> builtin___bool: ...
     def ClearField(self, field_name: typing_extensions___Literal[u"columns",b"columns",u"condition",b"condition",u"entity_type",b"entity_type",u"hits_per_page",b"hits_per_page",u"organization_id",b"organization_id",u"page",b"page",u"rank_metrics",b"rank_metrics",u"sort_asc",b"sort_asc",u"sort_field",b"sort_field",u"sort_field_type",b"sort_field_type",u"sort_type",b"sort_type"]) -> None: ...
 type___TrendSearchRequest = TrendSearchRequest
+
+class TrendSearchRollupRequest(google___protobuf___message___Message):
+    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
+    organization_id: typing___Text = ...
+    entity_type: common_pb2___EntityTypeValue = ...
+    rollup_type: type___RollupTypeValue = ...
+    page: builtin___int = ...
+    hits_per_page: builtin___int = ...
+    sort_type: type___SortTypeValue = ...
+    sort_field_type: typing___Text = ...
+    sort_field: typing___Text = ...
+    sort_asc: builtin___bool = ...
+
+    @property
+    def condition(self) -> condition_pb2___ConditionGroup: ...
+
+    @property
+    def rank_metrics(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[type___MetricWithTimeRange]: ...
+
+    @property
+    def columns(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[condition_pb2___ConditionOrGroup]: ...
+
+    def __init__(self,
+        *,
+        organization_id : typing___Optional[typing___Text] = None,
+        entity_type : typing___Optional[common_pb2___EntityTypeValue] = None,
+        condition : typing___Optional[condition_pb2___ConditionGroup] = None,
+        rank_metrics : typing___Optional[typing___Iterable[type___MetricWithTimeRange]] = None,
+        rollup_type : typing___Optional[type___RollupTypeValue] = None,
+        page : typing___Optional[builtin___int] = None,
+        hits_per_page : typing___Optional[builtin___int] = None,
+        sort_type : typing___Optional[type___SortTypeValue] = None,
+        sort_field_type : typing___Optional[typing___Text] = None,
+        sort_field : typing___Optional[typing___Text] = None,
+        sort_asc : typing___Optional[builtin___bool] = None,
+        columns : typing___Optional[typing___Iterable[condition_pb2___ConditionOrGroup]] = None,
+        ) -> None: ...
+    def HasField(self, field_name: typing_extensions___Literal[u"condition",b"condition"]) -> builtin___bool: ...
+    def ClearField(self, field_name: typing_extensions___Literal[u"columns",b"columns",u"condition",b"condition",u"entity_type",b"entity_type",u"hits_per_page",b"hits_per_page",u"organization_id",b"organization_id",u"page",b"page",u"rank_metrics",b"rank_metrics",u"rollup_type",b"rollup_type",u"sort_asc",b"sort_asc",u"sort_field",b"sort_field",u"sort_field_type",b"sort_field_type",u"sort_type",b"sort_type"]) -> None: ...
+type___TrendSearchRollupRequest = TrendSearchRollupRequest
+
+class TrendSearchRollupResponse(google___protobuf___message___Message):
+    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
+    organization_id: typing___Text = ...
+
+    @property
+    def rows(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[type___TrendSearchRollupRow]: ...
+
+    def __init__(self,
+        *,
+        organization_id : typing___Optional[typing___Text] = None,
+        rows : typing___Optional[typing___Iterable[type___TrendSearchRollupRow]] = None,
+        ) -> None: ...
+    def ClearField(self, field_name: typing_extensions___Literal[u"organization_id",b"organization_id",u"rows",b"rows"]) -> None: ...
+type___TrendSearchRollupResponse = TrendSearchRollupResponse
+
+class TrendSearchRollupRow(google___protobuf___message___Message):
+    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
+    class AggregatedMetricsEntry(google___protobuf___message___Message):
+        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
+        key: typing___Text = ...
+
+        @property
+        def value(self) -> metric_pb2___AggregatedMetric: ...
+
+        def __init__(self,
+            *,
+            key : typing___Optional[typing___Text] = None,
+            value : typing___Optional[metric_pb2___AggregatedMetric] = None,
+            ) -> None: ...
+        def HasField(self, field_name: typing_extensions___Literal[u"value",b"value"]) -> builtin___bool: ...
+        def ClearField(self, field_name: typing_extensions___Literal[u"key",b"key",u"value",b"value"]) -> None: ...
+    type___AggregatedMetricsEntry = AggregatedMetricsEntry
+
+    predicate: typing___Text = ...
+    accounts_count: builtin___int = ...
+    users_count: builtin___int = ...
+    owners: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text] = ...
+
+    @property
+    def aggregated_metrics(self) -> typing___MutableMapping[typing___Text, metric_pb2___AggregatedMetric]: ...
+
+    def __init__(self,
+        *,
+        predicate : typing___Optional[typing___Text] = None,
+        accounts_count : typing___Optional[builtin___int] = None,
+        users_count : typing___Optional[builtin___int] = None,
+        owners : typing___Optional[typing___Iterable[typing___Text]] = None,
+        aggregated_metrics : typing___Optional[typing___Mapping[typing___Text, metric_pb2___AggregatedMetric]] = None,
+        ) -> None: ...
+    def ClearField(self, field_name: typing_extensions___Literal[u"accounts_count",b"accounts_count",u"aggregated_metrics",b"aggregated_metrics",u"owners",b"owners",u"predicate",b"predicate",u"users_count",b"users_count"]) -> None: ...
+type___TrendSearchRollupRow = TrendSearchRollupRow
```

### Comparing `calixa-proto-py-2.0.8/calixa_proto_py/search_pb2_grpc.py` & `calixa-proto-py-2.0.9/calixa_proto_py/search_pb2_grpc.py`

 * *Files identical despite different names*

### Comparing `calixa-proto-py-2.0.8/calixa_proto_py/segment.proto` & `calixa-proto-py-2.0.9/calixa_proto_py/segment.proto`

 * *Files 22% similar despite different names*

```diff
@@ -4,17 +4,21 @@
 
 option java_package = "io.calixa.domain.segment";
 option java_multiple_files = true;
 option optimize_for = SPEED;
 
 package calixa.domain.segment;
 
-// TODO(freds): This domain object is to be deleted once EventService is complete.
+// TODO(freds): Delete this proto when Segment is migrated from Python to Java
+// using LoadedEntity.
+// See https://linear.app/calixa/issue/CAL-1051/migrate-segment-to-use-loadedentryreceiver
 message SegmentEvent {
 
+  option deprecated = true;
+
   string id = 1;
   string organizationId = 2;
   string instance_id = 300;
   string accountId = 3;
   string accountUserId = 4;
   string raw = 5;
```

### Comparing `calixa-proto-py-2.0.8/calixa_proto_py/segment_pb2.pyi` & `calixa-proto-py-2.0.9/calixa_proto_py/segment_pb2.pyi`

 * *Files 8% similar despite different names*

```diff
@@ -1,11 +1,9 @@
-"""
-@generated by mypy-protobuf.  Do not edit manually!
-isort:skip_file
-"""
+# @generated by generate_proto_mypy_stubs.py.  Do not edit!
+import sys
 from google.protobuf.descriptor import (
     Descriptor as google___protobuf___descriptor___Descriptor,
     FileDescriptor as google___protobuf___descriptor___FileDescriptor,
 )
 
 from google.protobuf.message import (
     Message as google___protobuf___message___Message,
```

### Comparing `calixa-proto-py-2.0.8/calixa_proto_py/sidedata/annotation.proto` & `calixa-proto-py-2.0.9/calixa_proto_py/sidedata/annotation.proto`

 * *Files identical despite different names*

### Comparing `calixa-proto-py-2.0.8/calixa_proto_py/sidedata/annotation_pb2.pyi` & `calixa-proto-py-2.0.9/calixa_proto_py/sidedata/annotation_pb2.pyi`

 * *Files 2% similar despite different names*

```diff
@@ -1,11 +1,9 @@
-"""
-@generated by mypy-protobuf.  Do not edit manually!
-isort:skip_file
-"""
+# @generated by generate_proto_mypy_stubs.py.  Do not edit!
+import sys
 from google.protobuf.descriptor import (
     Descriptor as google___protobuf___descriptor___Descriptor,
     EnumDescriptor as google___protobuf___descriptor___EnumDescriptor,
     FieldDescriptor as google___protobuf___descriptor___FieldDescriptor,
     FileDescriptor as google___protobuf___descriptor___FileDescriptor,
 )
 
@@ -49,24 +47,26 @@
     DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
     UNSPECIFIED = typing___cast(DataTypeValue, 0)
     HIGH_VELOCITY = typing___cast(DataTypeValue, 1)
     HIGH_CARDINALITY = typing___cast(DataTypeValue, 2)
 UNSPECIFIED = typing___cast(DataTypeValue, 0)
 HIGH_VELOCITY = typing___cast(DataTypeValue, 1)
 HIGH_CARDINALITY = typing___cast(DataTypeValue, 2)
+type___DataType = DataType
 
 OptionValue = typing___NewType('OptionValue', builtin___int)
 type___OptionValue = OptionValue
 Option: _Option
 class _Option(google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper[OptionValue]):
     DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
     OPTION_UNSPECIFIED = typing___cast(OptionValue, 0)
     OPTION_KEEP_HIGHEST = typing___cast(OptionValue, 1)
 OPTION_UNSPECIFIED = typing___cast(OptionValue, 0)
 OPTION_KEEP_HIGHEST = typing___cast(OptionValue, 1)
+type___Option = Option
 
 class SideDataDef(google___protobuf___message___Message):
     DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
     data_type: type___DataTypeValue = ...
     qualifier: typing___Text = ...
     options: google___protobuf___internal___containers___RepeatedScalarFieldContainer[type___OptionValue] = ...
```

### Comparing `calixa-proto-py-2.0.8/calixa_proto_py/tag_pb2.pyi` & `calixa-proto-py-2.0.9/calixa_proto_py/tag_pb2.pyi`

 * *Files 4% similar despite different names*

```diff
@@ -1,11 +1,9 @@
-"""
-@generated by mypy-protobuf.  Do not edit manually!
-isort:skip_file
-"""
+# @generated by generate_proto_mypy_stubs.py.  Do not edit!
+import sys
 from common_pb2 import (
     EntityTypeValue as common_pb2___EntityTypeValue,
 )
 
 from google.protobuf.descriptor import (
     Descriptor as google___protobuf___descriptor___Descriptor,
     FileDescriptor as google___protobuf___descriptor___FileDescriptor,
```

### Comparing `calixa-proto-py-2.0.8/PKG-INFO` & `calixa-proto-py-2.0.9/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: calixa-proto-py
-Version: 2.0.8
+Version: 2.0.9
 Summary: Calixa proto py
 Author: Calixa Platform Developers
 Author-email: everyone@calixa.io
 Requires-Python: >=3.7,<4.0
 Classifier: Programming Language :: Python :: 3
 Classifier: Programming Language :: Python :: 3.10
 Classifier: Programming Language :: Python :: 3.7
```

