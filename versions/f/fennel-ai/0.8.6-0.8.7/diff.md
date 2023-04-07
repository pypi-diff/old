# Comparing `tmp/fennel_ai-0.8.6.tar.gz` & `tmp/fennel_ai-0.8.7.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "fennel_ai-0.8.6.tar", max compression
+gzip compressed data, was "fennel_ai-0.8.7.tar", max compression
```

## Comparing `fennel_ai-0.8.6.tar` & `fennel_ai-0.8.7.tar`

### file list

```diff
@@ -1,111 +1,111 @@
--rw-r--r--   0        0        0     2491 2023-01-18 00:37:07.677469 fennel_ai-0.8.6/README.md
--rw-r--r--   0        0        0       57 2022-12-23 11:34:46.808938 fennel_ai-0.8.6/fennel/.gitignore
--rw-r--r--   0        0        0     2466 2023-03-23 19:15:08.151636 fennel_ai-0.8.6/fennel/CHANGELOG.md
--rw-r--r--   0        0        0      337 2022-11-24 00:08:26.704177 fennel_ai-0.8.6/fennel/__init__.py
--rw-r--r--   0        0        0       48 2023-03-23 00:26:22.396530 fennel_ai-0.8.6/fennel/client/__init__.py
--rw-r--r--   0        0        0    11825 2023-03-23 18:24:25.756906 fennel_ai-0.8.6/fennel/client/client.py
--rw-r--r--   0        0        0        0 2022-11-18 15:56:16.259075 fennel_ai-0.8.6/fennel/client_tests/__init__.py
--rw-r--r--   0        0        0   389178 2023-03-22 22:12:03.387749 fennel_ai-0.8.6/fennel/client_tests/data/post_data.csv
--rw-r--r--   0        0        0    65661 2023-03-22 22:12:03.388224 fennel_ai-0.8.6/fennel/client_tests/data/user_data.csv
--rw-r--r--   0        0        0    55865 2023-03-22 22:12:03.388611 fennel_ai-0.8.6/fennel/client_tests/data/view_data_sampled.csv
--rw-r--r--   0        0        0     4623 2023-03-22 22:12:03.388978 fennel_ai-0.8.6/fennel/client_tests/test_additional_schemas.py
--rw-r--r--   0        0        0     4255 2023-03-13 21:55:38.562681 fennel_ai-0.8.6/fennel/client_tests/test_data_integration.py
--rw-r--r--   0        0        0    45385 2023-03-23 19:15:08.152241 fennel_ai-0.8.6/fennel/client_tests/test_dataset.py
--rw-r--r--   0        0        0    16401 2023-03-22 22:11:57.293483 fennel_ai-0.8.6/fennel/client_tests/test_featureset.py
--rw-r--r--   0        0        0     8643 2023-03-23 19:15:08.152568 fennel_ai-0.8.6/fennel/client_tests/test_invalid.py
--rw-r--r--   0        0        0    18511 2023-03-13 15:12:57.725657 fennel_ai-0.8.6/fennel/client_tests/test_search.py
--rw-r--r--   0        0        0     6305 2023-03-22 22:12:03.389978 fennel_ai-0.8.6/fennel/client_tests/test_social_network.py
--rw-r--r--   0        0        0      236 2023-01-15 19:54:21.648934 fennel_ai-0.8.6/fennel/datasets/__init__.py
--rw-r--r--   0        0        0    43066 2023-03-23 19:15:08.153081 fennel_ai-0.8.6/fennel/datasets/datasets.py
--rw-r--r--   0        0        0    32633 2023-03-23 19:15:08.153540 fennel_ai-0.8.6/fennel/datasets/test_dataset.py
--rw-r--r--   0        0        0     4221 2023-03-13 21:55:38.565096 fennel_ai-0.8.6/fennel/datasets/test_dataset_lookup.py
--rw-r--r--   0        0        0     4753 2023-03-22 22:12:03.390967 fennel_ai-0.8.6/fennel/datasets/test_invalid_dataset.py
--rw-r--r--   0        0        0    10067 2023-03-22 22:12:03.391381 fennel_ai-0.8.6/fennel/datasets/test_schema_validator.py
--rw-r--r--   0        0        0      200 2023-01-10 06:36:00.253930 fennel_ai-0.8.6/fennel/featuresets/__init__.py
--rw-r--r--   0        0        0    16790 2023-03-22 22:12:03.391820 fennel_ai-0.8.6/fennel/featuresets/featureset.py
--rw-r--r--   0        0        0    10429 2023-03-13 21:55:38.565640 fennel_ai-0.8.6/fennel/featuresets/test_featureset.py
--rw-r--r--   0        0        0     6919 2023-03-22 22:12:03.392143 fennel_ai-0.8.6/fennel/featuresets/test_invalid_featureset.py
--rw-r--r--   0        0        0    10244 2022-11-18 15:56:16.261069 fennel_ai-0.8.6/fennel/gen/.DS_Store
--rw-r--r--   0        0        0        0 2023-03-20 21:41:09.633386 fennel_ai-0.8.6/fennel/gen/__init__.py
--rw-r--r--   0        0        0     6547 2023-03-20 21:41:09.633777 fennel_ai-0.8.6/fennel/gen/connector_pb2.py
--rw-r--r--   0        0        0    19866 2023-03-20 21:41:09.612102 fennel_ai-0.8.6/fennel/gen/connector_pb2.pyi
--rw-r--r--   0        0        0      159 2023-03-20 21:41:09.634107 fennel_ai-0.8.6/fennel/gen/connector_pb2_grpc.py
--rw-r--r--   0        0        0     5548 2023-03-20 21:41:09.634374 fennel_ai-0.8.6/fennel/gen/dataset_pb2.py
--rw-r--r--   0        0        0    16076 2023-03-20 21:41:09.612868 fennel_ai-0.8.6/fennel/gen/dataset_pb2.pyi
--rw-r--r--   0        0        0      159 2023-03-20 21:41:09.634651 fennel_ai-0.8.6/fennel/gen/dataset_pb2_grpc.py
--rw-r--r--   0        0        0     1797 2023-03-20 21:41:09.634835 fennel_ai-0.8.6/fennel/gen/expectations_pb2.py
--rw-r--r--   0        0        0     3355 2023-03-20 21:41:09.613550 fennel_ai-0.8.6/fennel/gen/expectations_pb2.pyi
--rw-r--r--   0        0        0      159 2023-03-20 21:41:09.634997 fennel_ai-0.8.6/fennel/gen/expectations_pb2_grpc.py
--rw-r--r--   0        0        0     2888 2023-03-20 21:41:09.635173 fennel_ai-0.8.6/fennel/gen/featureset_pb2.py
--rw-r--r--   0        0        0     6756 2023-03-20 21:41:09.613748 fennel_ai-0.8.6/fennel/gen/featureset_pb2.pyi
--rw-r--r--   0        0        0      159 2023-03-20 21:41:09.635340 fennel_ai-0.8.6/fennel/gen/featureset_pb2_grpc.py
--rw-r--r--   0        0        0     1134 2023-03-20 21:41:09.635498 fennel_ai-0.8.6/fennel/gen/metadata_pb2.py
--rw-r--r--   0        0        0     1463 2023-03-20 21:41:09.614005 fennel_ai-0.8.6/fennel/gen/metadata_pb2.pyi
--rw-r--r--   0        0        0      159 2023-03-20 21:41:09.635667 fennel_ai-0.8.6/fennel/gen/metadata_pb2_grpc.py
--rw-r--r--   0        0        0     1000 2023-03-20 21:41:09.635850 fennel_ai-0.8.6/fennel/gen/pycode_pb2.py
--rw-r--r--   0        0        0      896 2023-03-20 21:41:09.614308 fennel_ai-0.8.6/fennel/gen/pycode_pb2.pyi
--rw-r--r--   0        0        0      159 2023-03-20 21:41:09.636068 fennel_ai-0.8.6/fennel/gen/pycode_pb2_grpc.py
--rw-r--r--   0        0        0     6142 2023-03-20 21:41:09.636299 fennel_ai-0.8.6/fennel/gen/schema_pb2.py
--rw-r--r--   0        0        0    17262 2023-03-20 21:41:09.614597 fennel_ai-0.8.6/fennel/gen/schema_pb2.pyi
--rw-r--r--   0        0        0      159 2023-03-20 21:41:09.636566 fennel_ai-0.8.6/fennel/gen/schema_pb2_grpc.py
--rw-r--r--   0        0        0     2389 2023-03-20 21:41:09.636777 fennel_ai-0.8.6/fennel/gen/services_pb2.py
--rw-r--r--   0        0        0     4157 2023-03-20 21:41:09.614899 fennel_ai-0.8.6/fennel/gen/services_pb2.pyi
--rw-r--r--   0        0        0     2596 2023-03-20 21:41:09.636973 fennel_ai-0.8.6/fennel/gen/services_pb2_grpc.py
--rw-r--r--   0        0        0     1871 2023-03-20 21:41:09.637160 fennel_ai-0.8.6/fennel/gen/spec_pb2.py
--rw-r--r--   0        0        0     3805 2023-03-20 21:41:09.615210 fennel_ai-0.8.6/fennel/gen/spec_pb2.pyi
--rw-r--r--   0        0        0      159 2023-03-20 21:41:09.637334 fennel_ai-0.8.6/fennel/gen/spec_pb2_grpc.py
--rw-r--r--   0        0        0     1463 2023-03-20 21:41:09.637510 fennel_ai-0.8.6/fennel/gen/status_pb2.py
--rw-r--r--   0        0        0     2739 2023-03-20 21:41:09.615641 fennel_ai-0.8.6/fennel/gen/status_pb2.pyi
--rw-r--r--   0        0        0      159 2023-03-20 21:41:09.637911 fennel_ai-0.8.6/fennel/gen/status_pb2_grpc.py
--rw-r--r--   0        0        0     1451 2023-03-20 21:41:09.638145 fennel_ai-0.8.6/fennel/gen/window_pb2.py
--rw-r--r--   0        0        0     2158 2023-03-20 21:41:09.615851 fennel_ai-0.8.6/fennel/gen/window_pb2.pyi
--rw-r--r--   0        0        0      159 2023-03-20 21:41:09.638323 fennel_ai-0.8.6/fennel/gen/window_pb2_grpc.py
--rw-r--r--   0        0        0        0 2022-11-09 19:46:02.908591 fennel_ai-0.8.6/fennel/lib/__init__.py
--rw-r--r--   0        0        0      135 2022-11-11 19:32:36.803532 fennel_ai-0.8.6/fennel/lib/aggregate/__init__.py
--rw-r--r--   0        0        0     2436 2023-03-13 21:55:38.571879 fennel_ai-0.8.6/fennel/lib/aggregate/aggregate.py
--rw-r--r--   0        0        0       61 2022-11-29 23:09:55.918142 fennel_ai-0.8.6/fennel/lib/ascii_visualizer/__init__.py
--rw-r--r--   0        0        0     8988 2022-11-29 23:09:55.918358 fennel_ai-0.8.6/fennel/lib/ascii_visualizer/dag_ascii.py
--rw-r--r--   0        0        0      224 2023-02-01 17:00:28.098529 fennel_ai-0.8.6/fennel/lib/ascii_visualizer/test_dag_ascii.py
--rw-r--r--   0        0        0      158 2023-03-22 22:12:03.392415 fennel_ai-0.8.6/fennel/lib/duration/__init__.py
--rw-r--r--   0        0        0     2622 2023-03-22 22:12:03.392714 fennel_ai-0.8.6/fennel/lib/duration/duration.py
--rw-r--r--   0        0        0      676 2023-02-01 17:00:28.098805 fennel_ai-0.8.6/fennel/lib/duration/test_duration.py
--rw-r--r--   0        0        0      196 2023-02-22 16:02:41.305630 fennel_ai-0.8.6/fennel/lib/expectations/__init__.py
--rw-r--r--   0        0        0     1369 2023-02-22 16:02:41.305950 fennel_ai-0.8.6/fennel/lib/expectations/great_expectations.py
--rw-r--r--   0        0        0    48532 2023-03-17 00:48:03.288481 fennel_ai-0.8.6/fennel/lib/expectations/supported_expectations.py
--rw-r--r--   0        0        0     8785 2023-03-17 00:48:03.288739 fennel_ai-0.8.6/fennel/lib/expectations/test_great_expectations.py
--rw-r--r--   0        0        0      176 2022-11-20 00:53:58.700243 fennel_ai-0.8.6/fennel/lib/graph_algorithms/__init__.py
--rw-r--r--   0        0        0     1498 2022-11-23 18:44:04.928854 fennel_ai-0.8.6/fennel/lib/graph_algorithms/cycle_detection.py
--rw-r--r--   0        0        0     6603 2023-03-22 22:12:03.393103 fennel_ai-0.8.6/fennel/lib/graph_algorithms/extractor_order.py
--rw-r--r--   0        0        0      885 2023-02-01 17:00:28.099073 fennel_ai-0.8.6/fennel/lib/graph_algorithms/test_cycle_detection.py
--rw-r--r--   0        0        0     5187 2023-03-13 21:55:38.572834 fennel_ai-0.8.6/fennel/lib/graph_algorithms/test_extractor_order.py
--rw-r--r--   0        0        0     1889 2023-03-13 21:55:38.573053 fennel_ai-0.8.6/fennel/lib/graph_algorithms/utils.py
--rw-r--r--   0        0        0      131 2022-11-12 22:18:19.614314 fennel_ai-0.8.6/fennel/lib/metadata/__init__.py
--rw-r--r--   0        0        0     2941 2023-03-13 21:55:38.573364 fennel_ai-0.8.6/fennel/lib/metadata/metadata.py
--rw-r--r--   0        0        0      834 2023-02-01 17:00:28.099569 fennel_ai-0.8.6/fennel/lib/metadata/test_invalid_metadata.py
--rw-r--r--   0        0        0    15054 2023-03-17 00:48:03.289127 fennel_ai-0.8.6/fennel/lib/metadata/test_metadata.py
--rw-r--r--   0        0        0      195 2023-03-20 20:31:36.582302 fennel_ai-0.8.6/fennel/lib/schema/__init__.py
--rw-r--r--   0        0        0    17676 2023-03-22 22:12:03.393457 fennel_ai-0.8.6/fennel/lib/schema/schema.py
--rw-r--r--   0        0        0    16782 2023-03-13 21:55:38.574337 fennel_ai-0.8.6/fennel/lib/schema/test_schema.py
--rw-r--r--   0        0        0      309 2023-03-13 21:55:38.574590 fennel_ai-0.8.6/fennel/lib/to_proto/__init__.py
--rw-r--r--   0        0        0     4659 2023-03-13 21:55:38.574873 fennel_ai-0.8.6/fennel/lib/to_proto/serializer.py
--rw-r--r--   0        0        0    23166 2023-03-17 20:25:30.263250 fennel_ai-0.8.6/fennel/lib/to_proto/to_proto.py
--rw-r--r--   0        0        0       44 2022-11-04 18:55:54.267426 fennel_ai-0.8.6/fennel/lib/window/__init__.py
--rw-r--r--   0        0        0     1813 2023-03-22 22:12:03.393851 fennel_ai-0.8.6/fennel/lib/window/window.py
--rw-r--r--   0        0        0        0 2022-11-09 19:46:02.910770 fennel_ai-0.8.6/fennel/py.typed
--rw-r--r--   0        0        0      260 2023-03-17 20:25:30.263512 fennel_ai-0.8.6/fennel/sources/__init__.py
--rw-r--r--   0        0        0    11451 2023-03-21 15:47:19.336492 fennel_ai-0.8.6/fennel/sources/sources.py
--rw-r--r--   0        0        0     3182 2023-03-13 21:55:38.576421 fennel_ai-0.8.6/fennel/sources/test_invalid_sources.py
--rw-r--r--   0        0        0    19557 2023-03-17 20:25:30.264122 fennel_ai-0.8.6/fennel/sources/test_sources.py
--rw-r--r--   0        0        0      471 2023-03-23 00:26:22.397142 fennel_ai-0.8.6/fennel/test_lib/__init__.py
--rw-r--r--   0        0        0    12798 2023-03-23 19:15:08.153907 fennel_ai-0.8.6/fennel/test_lib/executor.py
--rw-r--r--   0        0        0      649 2022-11-18 15:56:16.264922 fennel_ai-0.8.6/fennel/test_lib/grpc_mock.py
--rw-r--r--   0        0        0     5296 2023-03-13 21:55:38.577416 fennel_ai-0.8.6/fennel/test_lib/integration_client.py
--rw-r--r--   0        0        0     2194 2023-03-23 18:24:28.837994 fennel_ai-0.8.6/fennel/test_lib/local_client.py
--rw-r--r--   0        0        0    21239 2023-03-22 22:12:03.394232 fennel_ai-0.8.6/fennel/test_lib/mock_client.py
--rw-r--r--   0        0        0      217 2023-01-18 23:54:57.910585 fennel_ai-0.8.6/fennel/test_lib/test_client.py
--rw-r--r--   0        0        0     2085 2023-03-13 22:56:22.944013 fennel_ai-0.8.6/fennel/test_lib/test_utils.py
--rw-r--r--   0        0        0      629 2022-11-10 17:22:18.645670 fennel_ai-0.8.6/fennel/test_utils.py
--rw-r--r--   0        0        0     4647 2023-02-15 06:18:04.217476 fennel_ai-0.8.6/fennel/utils.py
--rw-r--r--   0        0        0     2114 2023-03-23 19:15:08.154285 fennel_ai-0.8.6/pyproject.toml
--rw-r--r--   0        0        0     3912 1970-01-01 00:00:00.000000 fennel_ai-0.8.6/setup.py
--rw-r--r--   0        0        0     3520 1970-01-01 00:00:00.000000 fennel_ai-0.8.6/PKG-INFO
+-rw-r--r--   0        0        0     2491 2023-01-18 00:37:07.677469 fennel_ai-0.8.7/README.md
+-rw-r--r--   0        0        0       57 2022-12-23 11:34:46.808938 fennel_ai-0.8.7/fennel/.gitignore
+-rw-r--r--   0        0        0     2590 2023-03-30 15:23:38.265173 fennel_ai-0.8.7/fennel/CHANGELOG.md
+-rw-r--r--   0        0        0      325 2023-03-30 15:23:38.265413 fennel_ai-0.8.7/fennel/__init__.py
+-rw-r--r--   0        0        0       48 2023-03-23 00:26:22.396530 fennel_ai-0.8.7/fennel/client/__init__.py
+-rw-r--r--   0        0        0    11825 2023-03-27 05:25:11.193711 fennel_ai-0.8.7/fennel/client/client.py
+-rw-r--r--   0        0        0        0 2022-11-18 15:56:16.259075 fennel_ai-0.8.7/fennel/client_tests/__init__.py
+-rw-r--r--   0        0        0   389178 2023-04-03 18:15:25.548333 fennel_ai-0.8.7/fennel/client_tests/data/post_data.csv
+-rw-r--r--   0        0        0    65661 2023-04-03 18:15:25.548891 fennel_ai-0.8.7/fennel/client_tests/data/user_data.csv
+-rw-r--r--   0        0        0    55865 2023-04-03 18:15:25.549501 fennel_ai-0.8.7/fennel/client_tests/data/view_data_sampled.csv
+-rw-r--r--   0        0        0     4623 2023-03-22 22:12:03.388978 fennel_ai-0.8.7/fennel/client_tests/test_additional_schemas.py
+-rw-r--r--   0        0        0     4255 2023-03-13 21:55:38.562681 fennel_ai-0.8.7/fennel/client_tests/test_data_integration.py
+-rw-r--r--   0        0        0    45478 2023-04-03 18:15:25.550037 fennel_ai-0.8.7/fennel/client_tests/test_dataset.py
+-rw-r--r--   0        0        0    16292 2023-04-03 18:15:25.550446 fennel_ai-0.8.7/fennel/client_tests/test_featureset.py
+-rw-r--r--   0        0        0     8730 2023-04-03 18:15:25.550770 fennel_ai-0.8.7/fennel/client_tests/test_invalid.py
+-rw-r--r--   0        0        0    18563 2023-04-03 18:15:25.551195 fennel_ai-0.8.7/fennel/client_tests/test_search.py
+-rw-r--r--   0        0        0     6251 2023-04-03 18:15:25.551555 fennel_ai-0.8.7/fennel/client_tests/test_social_network.py
+-rw-r--r--   0        0        0      236 2023-03-31 01:28:14.503503 fennel_ai-0.8.7/fennel/datasets/__init__.py
+-rw-r--r--   0        0        0    43409 2023-04-03 18:15:25.552234 fennel_ai-0.8.7/fennel/datasets/datasets.py
+-rw-r--r--   0        0        0    32648 2023-04-03 18:15:25.552871 fennel_ai-0.8.7/fennel/datasets/test_dataset.py
+-rw-r--r--   0        0        0     4197 2023-04-03 18:15:25.553115 fennel_ai-0.8.7/fennel/datasets/test_dataset_lookup.py
+-rw-r--r--   0        0        0     4833 2023-03-30 15:23:38.268353 fennel_ai-0.8.7/fennel/datasets/test_invalid_dataset.py
+-rw-r--r--   0        0        0    10208 2023-03-30 15:23:38.268570 fennel_ai-0.8.7/fennel/datasets/test_schema_validator.py
+-rw-r--r--   0        0        0      184 2023-03-30 15:23:38.268779 fennel_ai-0.8.7/fennel/featuresets/__init__.py
+-rw-r--r--   0        0        0    16985 2023-04-03 18:15:25.553533 fennel_ai-0.8.7/fennel/featuresets/featureset.py
+-rw-r--r--   0        0        0    10384 2023-04-03 18:15:25.553776 fennel_ai-0.8.7/fennel/featuresets/test_featureset.py
+-rw-r--r--   0        0        0     6818 2023-03-30 15:23:38.269527 fennel_ai-0.8.7/fennel/featuresets/test_invalid_featureset.py
+-rw-r--r--   0        0        0    10244 2022-11-18 15:56:16.261069 fennel_ai-0.8.7/fennel/gen/.DS_Store
+-rw-r--r--   0        0        0        0 2023-03-30 20:44:20.504882 fennel_ai-0.8.7/fennel/gen/__init__.py
+-rw-r--r--   0        0        0     6547 2023-03-30 20:44:20.505226 fennel_ai-0.8.7/fennel/gen/connector_pb2.py
+-rw-r--r--   0        0        0    19866 2023-03-30 20:44:20.487174 fennel_ai-0.8.7/fennel/gen/connector_pb2.pyi
+-rw-r--r--   0        0        0      159 2023-03-30 20:44:20.505443 fennel_ai-0.8.7/fennel/gen/connector_pb2_grpc.py
+-rw-r--r--   0        0        0     5548 2023-04-03 18:15:25.554142 fennel_ai-0.8.7/fennel/gen/dataset_pb2.py
+-rw-r--r--   0        0        0    16076 2023-04-03 18:15:25.554450 fennel_ai-0.8.7/fennel/gen/dataset_pb2.pyi
+-rw-r--r--   0        0        0      159 2023-03-30 20:44:20.505896 fennel_ai-0.8.7/fennel/gen/dataset_pb2_grpc.py
+-rw-r--r--   0        0        0     1797 2023-03-30 20:44:20.506072 fennel_ai-0.8.7/fennel/gen/expectations_pb2.py
+-rw-r--r--   0        0        0     3355 2023-03-30 20:44:20.487719 fennel_ai-0.8.7/fennel/gen/expectations_pb2.pyi
+-rw-r--r--   0        0        0      159 2023-03-30 20:44:20.506234 fennel_ai-0.8.7/fennel/gen/expectations_pb2_grpc.py
+-rw-r--r--   0        0        0     2888 2023-04-03 18:15:25.554732 fennel_ai-0.8.7/fennel/gen/featureset_pb2.py
+-rw-r--r--   0        0        0     6756 2023-04-03 18:15:25.555214 fennel_ai-0.8.7/fennel/gen/featureset_pb2.pyi
+-rw-r--r--   0        0        0      159 2023-03-30 20:44:20.506602 fennel_ai-0.8.7/fennel/gen/featureset_pb2_grpc.py
+-rw-r--r--   0        0        0     1134 2023-03-30 20:44:20.506783 fennel_ai-0.8.7/fennel/gen/metadata_pb2.py
+-rw-r--r--   0        0        0     1463 2023-03-30 20:44:20.488314 fennel_ai-0.8.7/fennel/gen/metadata_pb2.pyi
+-rw-r--r--   0        0        0      159 2023-03-30 20:44:20.507139 fennel_ai-0.8.7/fennel/gen/metadata_pb2_grpc.py
+-rw-r--r--   0        0        0     1000 2023-04-03 18:15:25.555620 fennel_ai-0.8.7/fennel/gen/pycode_pb2.py
+-rw-r--r--   0        0        0      896 2023-04-03 18:15:25.555844 fennel_ai-0.8.7/fennel/gen/pycode_pb2.pyi
+-rw-r--r--   0        0        0      159 2023-03-30 20:44:20.507541 fennel_ai-0.8.7/fennel/gen/pycode_pb2_grpc.py
+-rw-r--r--   0        0        0     6142 2023-03-30 20:44:20.507742 fennel_ai-0.8.7/fennel/gen/schema_pb2.py
+-rw-r--r--   0        0        0    17262 2023-03-30 20:44:20.488722 fennel_ai-0.8.7/fennel/gen/schema_pb2.pyi
+-rw-r--r--   0        0        0      159 2023-03-30 20:44:20.507930 fennel_ai-0.8.7/fennel/gen/schema_pb2_grpc.py
+-rw-r--r--   0        0        0     2389 2023-03-30 20:44:20.508121 fennel_ai-0.8.7/fennel/gen/services_pb2.py
+-rw-r--r--   0        0        0     4157 2023-03-30 20:44:20.488933 fennel_ai-0.8.7/fennel/gen/services_pb2.pyi
+-rw-r--r--   0        0        0     2596 2023-03-30 20:44:20.508349 fennel_ai-0.8.7/fennel/gen/services_pb2_grpc.py
+-rw-r--r--   0        0        0     1871 2023-03-30 20:44:20.508569 fennel_ai-0.8.7/fennel/gen/spec_pb2.py
+-rw-r--r--   0        0        0     3805 2023-03-30 20:44:20.489178 fennel_ai-0.8.7/fennel/gen/spec_pb2.pyi
+-rw-r--r--   0        0        0      159 2023-03-30 20:44:20.508751 fennel_ai-0.8.7/fennel/gen/spec_pb2_grpc.py
+-rw-r--r--   0        0        0     1463 2023-03-30 20:44:20.508915 fennel_ai-0.8.7/fennel/gen/status_pb2.py
+-rw-r--r--   0        0        0     2739 2023-03-30 20:44:20.489355 fennel_ai-0.8.7/fennel/gen/status_pb2.pyi
+-rw-r--r--   0        0        0      159 2023-03-30 20:44:20.509087 fennel_ai-0.8.7/fennel/gen/status_pb2_grpc.py
+-rw-r--r--   0        0        0     1451 2023-03-30 20:44:20.509273 fennel_ai-0.8.7/fennel/gen/window_pb2.py
+-rw-r--r--   0        0        0     2158 2023-03-30 20:44:20.489543 fennel_ai-0.8.7/fennel/gen/window_pb2.pyi
+-rw-r--r--   0        0        0      159 2023-03-30 20:44:20.509493 fennel_ai-0.8.7/fennel/gen/window_pb2_grpc.py
+-rw-r--r--   0        0        0        0 2023-03-30 15:07:05.962017 fennel_ai-0.8.7/fennel/lib/__init__.py
+-rw-r--r--   0        0        0      135 2022-11-11 19:32:36.803532 fennel_ai-0.8.7/fennel/lib/aggregate/__init__.py
+-rw-r--r--   0        0        0     2436 2023-03-13 21:55:38.571879 fennel_ai-0.8.7/fennel/lib/aggregate/aggregate.py
+-rw-r--r--   0        0        0       61 2022-11-29 23:09:55.918142 fennel_ai-0.8.7/fennel/lib/ascii_visualizer/__init__.py
+-rw-r--r--   0        0        0     8988 2023-03-27 17:57:59.513593 fennel_ai-0.8.7/fennel/lib/ascii_visualizer/dag_ascii.py
+-rw-r--r--   0        0        0      224 2023-02-01 17:00:28.098529 fennel_ai-0.8.7/fennel/lib/ascii_visualizer/test_dag_ascii.py
+-rw-r--r--   0        0        0      158 2023-03-22 22:12:03.392415 fennel_ai-0.8.7/fennel/lib/duration/__init__.py
+-rw-r--r--   0        0        0     2622 2023-03-22 22:12:03.392714 fennel_ai-0.8.7/fennel/lib/duration/duration.py
+-rw-r--r--   0        0        0      676 2023-02-01 17:00:28.098805 fennel_ai-0.8.7/fennel/lib/duration/test_duration.py
+-rw-r--r--   0        0        0      196 2023-02-22 16:02:41.305630 fennel_ai-0.8.7/fennel/lib/expectations/__init__.py
+-rw-r--r--   0        0        0     1369 2023-02-22 16:02:41.305950 fennel_ai-0.8.7/fennel/lib/expectations/great_expectations.py
+-rw-r--r--   0        0        0    48532 2023-03-17 00:48:03.288481 fennel_ai-0.8.7/fennel/lib/expectations/supported_expectations.py
+-rw-r--r--   0        0        0     8785 2023-04-03 18:15:25.556179 fennel_ai-0.8.7/fennel/lib/expectations/test_great_expectations.py
+-rw-r--r--   0        0        0      176 2022-11-20 00:53:58.700243 fennel_ai-0.8.7/fennel/lib/graph_algorithms/__init__.py
+-rw-r--r--   0        0        0     1498 2023-03-30 05:20:46.621863 fennel_ai-0.8.7/fennel/lib/graph_algorithms/cycle_detection.py
+-rw-r--r--   0        0        0     6530 2023-04-03 18:15:25.556564 fennel_ai-0.8.7/fennel/lib/graph_algorithms/extractor_order.py
+-rw-r--r--   0        0        0      891 2023-03-30 15:23:38.271768 fennel_ai-0.8.7/fennel/lib/graph_algorithms/test_cycle_detection.py
+-rw-r--r--   0        0        0     4923 2023-03-30 15:23:38.271965 fennel_ai-0.8.7/fennel/lib/graph_algorithms/test_extractor_order.py
+-rw-r--r--   0        0        0     1889 2023-03-13 21:55:38.573053 fennel_ai-0.8.7/fennel/lib/graph_algorithms/utils.py
+-rw-r--r--   0        0        0      131 2022-11-12 22:18:19.614314 fennel_ai-0.8.7/fennel/lib/metadata/__init__.py
+-rw-r--r--   0        0        0     2941 2023-04-03 18:15:25.556955 fennel_ai-0.8.7/fennel/lib/metadata/metadata.py
+-rw-r--r--   0        0        0      834 2023-02-01 17:00:28.099569 fennel_ai-0.8.7/fennel/lib/metadata/test_invalid_metadata.py
+-rw-r--r--   0        0        0    15024 2023-04-03 18:15:25.557248 fennel_ai-0.8.7/fennel/lib/metadata/test_metadata.py
+-rw-r--r--   0        0        0      232 2023-03-30 15:23:38.272415 fennel_ai-0.8.7/fennel/lib/schema/__init__.py
+-rw-r--r--   0        0        0    17894 2023-04-03 18:15:25.557606 fennel_ai-0.8.7/fennel/lib/schema/schema.py
+-rw-r--r--   0        0        0    16782 2023-03-13 21:55:38.574337 fennel_ai-0.8.7/fennel/lib/schema/test_schema.py
+-rw-r--r--   0        0        0      309 2023-03-13 21:55:38.574590 fennel_ai-0.8.7/fennel/lib/to_proto/__init__.py
+-rw-r--r--   0        0        0     4659 2023-04-03 18:15:25.557939 fennel_ai-0.8.7/fennel/lib/to_proto/serializer.py
+-rw-r--r--   0        0        0    23166 2023-04-03 18:15:25.558429 fennel_ai-0.8.7/fennel/lib/to_proto/to_proto.py
+-rw-r--r--   0        0        0       44 2022-11-04 18:55:54.267426 fennel_ai-0.8.7/fennel/lib/window/__init__.py
+-rw-r--r--   0        0        0     1813 2023-03-22 22:12:03.393851 fennel_ai-0.8.7/fennel/lib/window/window.py
+-rw-r--r--   0        0        0        0 2022-11-09 19:46:02.910770 fennel_ai-0.8.7/fennel/py.typed
+-rw-r--r--   0        0        0      260 2023-03-17 20:25:30.263512 fennel_ai-0.8.7/fennel/sources/__init__.py
+-rw-r--r--   0        0        0    11451 2023-03-21 15:47:19.336492 fennel_ai-0.8.7/fennel/sources/sources.py
+-rw-r--r--   0        0        0     3182 2023-04-03 18:15:25.558759 fennel_ai-0.8.7/fennel/sources/test_invalid_sources.py
+-rw-r--r--   0        0        0    19557 2023-04-03 18:15:25.559104 fennel_ai-0.8.7/fennel/sources/test_sources.py
+-rw-r--r--   0        0        0      471 2023-04-03 18:15:25.559496 fennel_ai-0.8.7/fennel/test_lib/__init__.py
+-rw-r--r--   0        0        0    12798 2023-04-03 18:15:25.559800 fennel_ai-0.8.7/fennel/test_lib/executor.py
+-rw-r--r--   0        0        0      649 2022-11-18 15:56:16.264922 fennel_ai-0.8.7/fennel/test_lib/grpc_mock.py
+-rw-r--r--   0        0        0     5074 2023-03-29 03:08:48.126158 fennel_ai-0.8.7/fennel/test_lib/integration_client.py
+-rw-r--r--   0        0        0     2194 2023-03-27 05:25:11.198551 fennel_ai-0.8.7/fennel/test_lib/local_client.py
+-rw-r--r--   0        0        0    20741 2023-04-03 18:15:25.560193 fennel_ai-0.8.7/fennel/test_lib/mock_client.py
+-rw-r--r--   0        0        0      217 2023-01-18 23:54:57.910585 fennel_ai-0.8.7/fennel/test_lib/test_client.py
+-rw-r--r--   0        0        0     2085 2023-04-03 18:15:25.560398 fennel_ai-0.8.7/fennel/test_lib/test_utils.py
+-rw-r--r--   0        0        0      629 2022-11-10 17:22:18.645670 fennel_ai-0.8.7/fennel/test_utils.py
+-rw-r--r--   0        0        0     4647 2023-04-03 18:15:25.560613 fennel_ai-0.8.7/fennel/utils.py
+-rw-r--r--   0        0        0     2114 2023-04-03 18:15:25.561037 fennel_ai-0.8.7/pyproject.toml
+-rw-r--r--   0        0        0     3912 1970-01-01 00:00:00.000000 fennel_ai-0.8.7/setup.py
+-rw-r--r--   0        0        0     3520 1970-01-01 00:00:00.000000 fennel_ai-0.8.7/PKG-INFO
```

### Comparing `fennel_ai-0.8.6/README.md` & `fennel_ai-0.8.7/README.md`

 * *Files identical despite different names*

### Comparing `fennel_ai-0.8.6/fennel/CHANGELOG.md` & `fennel_ai-0.8.7/fennel/CHANGELOG.md`

 * *Files 11% similar despite different names*

```diff
@@ -1,9 +1,12 @@
 # Changelog
 
+## [0.8.7] - 2023-03-29
+- Change from type to decorator based input and output specification for pipelines and extractors 
+
 ## [0.8.6] - 2023-03-21
 - Add rename and drop operators to the client. 
 
 ## [0.8.5] - 2023-03-21
 - Improve client error reporting.
 
 ## [0.8.4] - 2023-03-20
```

### Comparing `fennel_ai-0.8.6/fennel/client/client.py` & `fennel_ai-0.8.7/fennel/client/client.py`

 * *Files identical despite different names*

### Comparing `fennel_ai-0.8.6/fennel/client_tests/data/post_data.csv` & `fennel_ai-0.8.7/fennel/client_tests/data/post_data.csv`

 * *Files identical despite different names*

### Comparing `fennel_ai-0.8.6/fennel/client_tests/data/user_data.csv` & `fennel_ai-0.8.7/fennel/client_tests/data/user_data.csv`

 * *Files identical despite different names*

### Comparing `fennel_ai-0.8.6/fennel/client_tests/data/view_data_sampled.csv` & `fennel_ai-0.8.7/fennel/client_tests/data/view_data_sampled.csv`

 * *Files identical despite different names*

### Comparing `fennel_ai-0.8.6/fennel/client_tests/test_additional_schemas.py` & `fennel_ai-0.8.7/fennel/client_tests/test_additional_schemas.py`

 * *Files identical despite different names*

### Comparing `fennel_ai-0.8.6/fennel/client_tests/test_data_integration.py` & `fennel_ai-0.8.7/fennel/client_tests/test_data_integration.py`

 * *Files identical despite different names*

### Comparing `fennel_ai-0.8.6/fennel/client_tests/test_dataset.py` & `fennel_ai-0.8.7/fennel/client_tests/test_dataset.py`

 * *Files 1% similar despite different names*

```diff
@@ -8,15 +8,15 @@
 import pandas as pd
 import pytest
 import requests
 
 from fennel.datasets import dataset, field, pipeline, Dataset, on_demand
 from fennel.lib.aggregate import Count, Sum, Average
 from fennel.lib.metadata import meta
-from fennel.lib.schema import Embedding, oneof, Series
+from fennel.lib.schema import Embedding, oneof, inputs
 from fennel.lib.window import Window
 from fennel.test_lib import mock_client
 
 
 ################################################################################
 #                           Dataset Unit Tests
 ################################################################################
@@ -37,15 +37,16 @@
 class UserInfoDatasetDerived:
     user_id: int = field(key=True).meta(description="User ID")  # type: ignore
     name: str = field().meta(description="User name")  # type: ignore
     country_name: Optional[str]
     ts: datetime = field(timestamp=True)
 
     @pipeline(id=1)
-    def get_info(cls, info: Dataset[UserInfoDataset]):
+    @inputs(UserInfoDataset)
+    def get_info(cls, info: Dataset):
         x = info.rename({"country": "country_name", "timestamp": "ts"})
         return x.drop(columns=["age"])
 
 
 class TestDataset(unittest.TestCase):
     @pytest.mark.integration
     @mock_client
@@ -260,15 +261,16 @@
             doc_id: int = field(key=True)
             bert_embedding: Embedding[4]
             fast_text_embedding: Embedding[3]
             num_words: int
             timestamp: datetime = field(timestamp=True)
 
             @on_demand(expires_after="3d")
-            def get_embedding(cls, ts: Series[datetime], doc_ids: Series[int]):
+            @inputs(datetime, int)
+            def get_embedding(cls, ts: pd.Series, doc_ids: pd.Series):
                 data = []
                 doc_ids = doc_ids.tolist()
                 for i in range(len(ts)):
                     data.append(
                         [
                             doc_ids[i],
                             [0.1, 0.2, 0.3, 0.4],
@@ -341,15 +343,16 @@
     movie: str = field(key=True)
     rating: float
     num_ratings: int
     sum_ratings: float
     t: datetime
 
     @pipeline(id=1)
-    def pipeline_aggregate(cls, activity: Dataset[RatingActivity]):
+    @inputs(RatingActivity)
+    def pipeline_aggregate(cls, activity: Dataset):
         return activity.groupby("movie").aggregate(
             [
                 Count(
                     window=Window("forever"), into_field=str(cls.num_ratings)
                 ),
                 Sum(
                     window=Window("forever"),
@@ -371,15 +374,16 @@
     movie: str = field(key=True)
     rating_sq: float
     rating_cube: float
     rating_into_5: float
     t: datetime
 
     @pipeline(id=1)
-    def pipeline_transform(cls, m: Dataset[MovieRating]):
+    @inputs(MovieRating)
+    def pipeline_transform(cls, m: Dataset):
         def t(df: pd.DataFrame) -> pd.DataFrame:
             df["rating_sq"] = df["rating"] * df["rating"]
             df["rating_cube"] = df["rating_sq"] * df["rating"]
             df["rating_into_5"] = df["rating"] * 5
             return df[
                 ["movie", "t", "rating_sq", "rating_cube", "rating_into_5"]
             ]
@@ -463,17 +467,16 @@
         key=True
     )
     rating: float
     revenue_in_millions: float
     t: datetime
 
     @pipeline(id=1)
-    def pipeline_join(
-        cls, rating: Dataset[MovieRating], revenue: Dataset[MovieRevenue]
-    ):
+    @inputs(MovieRating, MovieRevenue)
+    def pipeline_join(cls, rating: Dataset, revenue: Dataset):
         def to_millions(df: pd.DataFrame) -> pd.DataFrame:
             df[str(cls.revenue_in_millions)] = df["revenue"] / 1000000
             df[str(cls.revenue_in_millions)].fillna(-1, inplace=True)
             return df[
                 [
                     str(cls.movie),
                     str(cls.t),
@@ -608,15 +611,16 @@
     num_ratings_3d: int
     sum_ratings_7d: float
     avg_rating_6h: float
     total_ratings: int
     t: datetime
 
     @pipeline(id=1)
-    def pipeline_aggregate(cls, activity: Dataset[RatingActivity]):
+    @inputs(RatingActivity)
+    def pipeline_aggregate(cls, activity: Dataset):
         return activity.groupby("movie").aggregate(
             [
                 Count(window=Window("3d"), into_field=str(cls.num_ratings_3d)),
                 Sum(
                     window=Window("7d"),
                     of="rating",
                     into_field=str(cls.sum_ratings_7d),
@@ -763,15 +767,16 @@
 @dataset
 class PositiveRatingActivity:
     cnt_rating: int
     movie: str = field(key=True)
     t: datetime
 
     @pipeline(id=1)
-    def filter_positive_ratings(cls, rating: Dataset[RatingActivity]):
+    @inputs(RatingActivity)
+    def filter_positive_ratings(cls, rating: Dataset):
         filtered_ds = rating.filter(lambda df: df["rating"] >= 3.5)
         return filtered_ds.groupby("movie").aggregate(
             [Count(window=Window("forever"), into_field=str(cls.cnt_rating))],
         )
 
 
 class TestBasicFilter(unittest.TestCase):
@@ -863,17 +868,16 @@
     # transaction_amount: float
 
     num_categ_fraudulent_transactions: int
     num_categ_fraudulent_transactions_7d: int
     sum_categ_fraudulent_transactions_7d: float
 
     @pipeline(id=1)
-    def create_fraud_dataset(
-        cls, activity: Dataset[Activity], merchant_info: Dataset[MerchantInfo]
-    ):
+    @inputs(Activity, MerchantInfo)
+    def create_fraud_dataset(cls, activity: Dataset, merchant_info: Dataset):
         def extract_info(df: pd.DataFrame) -> pd.DataFrame:
             df_json = df["metadata"].apply(json.loads).apply(pd.Series)
             df_timestamp = pd.concat([df_json, df["timestamp"]], axis=1)
             return df_timestamp
 
         def fillna(df: pd.DataFrame) -> pd.DataFrame:
             df["category"].fillna("unknown", inplace=True)
@@ -1044,27 +1048,29 @@
 @dataset
 class UserAgeAggregated:
     city: str = field(key=True)
     timestamp: datetime
     sum_age: int
 
     @pipeline(id=1)
-    def create_user_age_aggregated(cls, user_age: Dataset[UserAge]):
+    @inputs(UserAge)
+    def create_user_age_aggregated(cls, user_age: Dataset):
         return user_age.groupby("city").aggregate(
             [
                 Sum(
                     window=Window("1w"),
                     of="age",
                     into_field="sum_age",
                 )
             ]
         )
 
     @pipeline(id=2)
-    def create_user_age_aggregated2(cls, user_age: Dataset[UserAgeNonTable]):
+    @inputs(UserAgeNonTable)
+    def create_user_age_aggregated2(cls, user_age: Dataset):
         return user_age.groupby("city").aggregate(
             [
                 Sum(
                     window=Window("1w"),
                     of="age",
                     into_field="sum_age",
                 )
@@ -1183,19 +1189,17 @@
     height: float = field().meta(description="in cm")  # type: ignore
     weight: float = field().meta(description="in kg")  # type: ignore
     club: str
     salary: Optional[int]
     wag: Optional[str]
 
     @pipeline(id=1)
+    @inputs(PlayerInfo, ClubSalary, WAG)
     def create_player_detailed_info(
-        cls,
-        player_info: Dataset[PlayerInfo],
-        club_salary: Dataset[ClubSalary],
-        wag: Dataset[WAG],
+        cls, player_info: Dataset, club_salary: Dataset, wag: Dataset
     ):
         def convert_to_metric_stats(df: pd.DataFrame) -> pd.DataFrame:
             df["height"] = df["height"] * 2.54
             df["weight"] = df["weight"] * 0.453592
             return df
 
         metric_stats = player_info.transform(
```

### Comparing `fennel_ai-0.8.6/fennel/client_tests/test_featureset.py` & `fennel_ai-0.8.7/fennel/client_tests/test_featureset.py`

 * *Files 6% similar despite different names*

```diff
@@ -5,17 +5,17 @@
 
 import numpy as np
 import pandas as pd
 import pytest
 import requests
 
 from fennel.datasets import dataset, field
-from fennel.featuresets import featureset, extractor, depends_on, feature
+from fennel.featuresets import featureset, extractor, feature
 from fennel.lib.metadata import meta
-from fennel.lib.schema import Series, DataFrame, Embedding
+from fennel.lib.schema import Embedding, inputs, outputs
 from fennel.test_lib import mock_client
 
 
 ################################################################################
 #                           Feature Single Extractor Unit Tests
 ################################################################################
 
@@ -35,19 +35,18 @@
 class UserInfoSingleExtractor:
     userid: int = feature(id=1)
     age: int = feature(id=4).meta(owner="aditya@fennel.ai")  # type: ignore
     age_squared: int = feature(id=5)
     age_cubed: int = feature(id=6)
     is_name_common: bool = feature(id=7)
 
-    @extractor
-    @depends_on(UserInfoDataset)
-    def get_user_info(
-        cls, ts: Series[datetime], user_id: Series[userid]
-    ) -> DataFrame[age, age_squared, age_cubed, is_name_common]:
+    @extractor(depends_on=[UserInfoDataset])
+    @inputs(userid)
+    @outputs(age, age_squared, age_cubed, is_name_common)
+    def get_user_info(cls, ts: pd.Series, user_id: pd.Series):
         df, _ = UserInfoDataset.lookup(ts, user_id=user_id)  # type: ignore
         df[str(cls.userid)] = user_id
         df[str(cls.age_squared)] = df["age"] ** 2
         df[str(cls.age_cubed)] = df["age"] ** 3
         df[str(cls.is_name_common)] = df["name"].isin(["John", "Mary", "Bob"])
         return df[
             [
@@ -76,46 +75,46 @@
     country_geoid: int = feature(id=3)
     age: int = feature(id=4).meta(owner="aditya@fennel.ai")  # type: ignore
     age_squared: int = feature(id=5)
     age_cubed: int = feature(id=6)
     is_name_common: bool = feature(id=7)
     age_reciprocal: float = feature(id=8)
 
-    @extractor
-    @depends_on(UserInfoDataset)
-    def get_user_age_and_name(
-        cls, ts: Series[datetime], user_id: Series[userid]
-    ) -> DataFrame[age, name]:
+    @extractor(depends_on=[UserInfoDataset])
+    @inputs(userid)
+    @outputs(age, name)
+    def get_user_age_and_name(cls, ts: pd.Series, user_id: pd.Series):
         df, _ = UserInfoDataset.lookup(ts, user_id=user_id)  # type: ignore
         return df[[str(cls.age), str(cls.name)]]
 
     @extractor
+    @inputs(age, name)
+    @outputs(age_squared, age_cubed, is_name_common)
     def get_age_and_name_features(
-        cls, ts: Series[datetime], user_age: Series[age], name: Series[name]
-    ) -> DataFrame[age_squared, age_cubed, is_name_common]:
+        cls, ts: pd.Series, user_age: pd.Series, name: pd.Series
+    ):
         is_name_common = name.isin(["John", "Mary", "Bob"])
         df = pd.concat([user_age**2, user_age**3, is_name_common], axis=1)
         df.columns = [
             str(cls.age_squared),
             str(cls.age_cubed),
             str(cls.is_name_common),
         ]
         return df
 
     @extractor
-    def get_age_reciprocal(
-        cls, ts: Series[datetime], age: Series[age]
-    ) -> Series[age_reciprocal]:
+    @inputs(age)
+    @outputs(age_reciprocal)
+    def get_age_reciprocal(cls, ts: pd.Series, age: pd.Series):
         return age.apply(lambda x: 1 / (x / (3600.0 * 24)) + 0.01)
 
-    @extractor(version=2)
-    @depends_on(UserInfoDataset)
-    def get_country_geoid(
-        cls, ts: Series[datetime], user_id: Series[userid]
-    ) -> Series[country_geoid]:
+    @extractor(depends_on=[UserInfoDataset], version=2)
+    @inputs(userid)
+    @outputs(country_geoid)
+    def get_country_geoid(cls, ts: pd.Series, user_id: pd.Series):
         df, _ = UserInfoDataset.lookup(ts, user_id=user_id)  # type: ignore
         return df["country"].apply(get_country_geoid)
 
 
 class TestSimpleExtractor(unittest.TestCase):
     @pytest.mark.integration
     def test_get_age_and_name_features(self):
@@ -239,20 +238,25 @@
 @featureset
 class UserInfoTransformedFeatures:
     age_power_four: int = feature(id=1)
     is_name_common: bool = feature(id=2)
     country_geoid_square: int = feature(id=3)
 
     @extractor
+    @inputs(
+        UserInfoMultipleExtractor.age,
+        UserInfoMultipleExtractor.is_name_common,
+        UserInfoMultipleExtractor.country_geoid,
+    )
     def get_user_transformed_features(
         cls,
-        ts: Series[datetime],
-        user_age: Series[UserInfoMultipleExtractor.age],
-        is_name_common: Series[UserInfoMultipleExtractor.is_name_common],
-        country_geoid: Series[UserInfoMultipleExtractor.country_geoid],
+        ts: pd.Series,
+        user_age: pd.Series,
+        is_name_common: pd.Series,
+        country_geoid: pd.Series,
     ):
         age_power_four = user_age**4
         country_geoid = country_geoid**2
         return pd.DataFrame(
             {
                 str(cls.age_power_four): age_power_four,
                 str(cls.is_name_common): is_name_common,
@@ -284,19 +288,17 @@
         response = client.log("UserInfoDataset", df)
         assert response.status_code == requests.codes.OK, response.json()
         if client.is_integration_client():
             time.sleep(1)
 
         feature_df = client.extract_features(
             output_feature_list=[
-                DataFrame[
-                    UserInfoTransformedFeatures.age_power_four,
-                    UserInfoTransformedFeatures.is_name_common,
-                    UserInfoTransformedFeatures.country_geoid_square,
-                ]
+                UserInfoTransformedFeatures.age_power_four,
+                UserInfoTransformedFeatures.is_name_common,
+                UserInfoTransformedFeatures.country_geoid_square,
             ],
             input_feature_list=[UserInfoMultipleExtractor.userid],
             input_dataframe=pd.DataFrame(
                 {"UserInfoMultipleExtractor.userid": [18232, 18234]}
             ),
         )
         self.assertEqual(feature_df.shape, (2, 3))
@@ -317,19 +319,17 @@
         )
 
         if client.is_integration_client():
             return
 
         feature_df = client.extract_historical_features(
             output_feature_list=[
-                DataFrame[
-                    UserInfoTransformedFeatures.age_power_four,
-                    UserInfoTransformedFeatures.is_name_common,
-                    UserInfoTransformedFeatures.country_geoid_square,
-                ],
+                UserInfoTransformedFeatures.age_power_four,
+                UserInfoTransformedFeatures.is_name_common,
+                UserInfoTransformedFeatures.country_geoid_square,
             ],
             input_feature_list=[UserInfoMultipleExtractor.userid],
             input_dataframe=pd.DataFrame(
                 {"UserInfoMultipleExtractor.userid": [18232, 18234]}
             ),
             timestamps=pd.Series([now, now]),
         )
@@ -368,19 +368,18 @@
 @featureset
 class DocumentFeatures:
     doc_id: int = feature(id=1)
     bert_embedding: Embedding[4] = feature(id=2)
     fast_text_embedding: Embedding[3] = feature(id=3)
     num_words: int = feature(id=4)
 
-    @extractor
-    @depends_on(DocumentContentDataset)
-    def get_doc_features(
-        cls, ts: Series[datetime], doc_id: Series[doc_id]
-    ) -> DataFrame[num_words, bert_embedding, fast_text_embedding]:
+    @extractor(depends_on=[DocumentContentDataset])
+    @inputs(doc_id)
+    @outputs(num_words, bert_embedding, fast_text_embedding)
+    def get_doc_features(cls, ts: pd.Series, doc_id: pd.Series):
         df, _ = DocumentContentDataset.lookup(ts, doc_id=doc_id)  # type: ignore
 
         df[str(cls.bert_embedding)] = df[str(cls.bert_embedding)].apply(
             lambda x: x if x is not None else [0, 0, 0, 0]
         )
         df[str(cls.fast_text_embedding)] = df[
             str(cls.fast_text_embedding)
```

### Comparing `fennel_ai-0.8.6/fennel/client_tests/test_invalid.py` & `fennel_ai-0.8.7/fennel/client_tests/test_invalid.py`

 * *Files 4% similar despite different names*

```diff
@@ -1,20 +1,21 @@
 import unittest
 from datetime import datetime
 
 import pandas as pd
 import pytest
 
 from fennel.datasets import dataset, pipeline, field, Dataset
-from fennel.featuresets import featureset, extractor, feature, depends_on
+from fennel.featuresets import featureset, extractor, feature
 from fennel.lib.metadata import meta
-from fennel.lib.schema import Series, DataFrame
+from fennel.lib.schema import inputs, outputs
+from fennel.test_lib import *
+
 
 # noinspection PyUnresolvedReferences
-from fennel.test_lib import *
 
 
 @featureset
 class Query:
     shortcut_id: int = feature(id=1)
     member_id: int = feature(id=2)
     domain: int = feature(id=3)
@@ -53,29 +54,29 @@
     url: str
     uid: str
     transitionType: str
     hasShortcut: bool
     country: str
 
     @pipeline(id=1)
-    def copy(cls, ds: Dataset[MemberActivityDataset]):
+    @inputs(MemberActivityDataset)
+    def copy(cls, ds: Dataset):
         return ds
 
 
 @meta(owner="test@fennel.ai")
 @featureset
 class DomainFeatures:
     domain: str = feature(id=1)
     DOMAIN_USED_COUNT: int = feature(id=2)
 
-    @extractor
-    @depends_on(MemberActivityDatasetCopy)
-    def get_domain_feature(
-        cls, ts: Series[datetime], domain: Series[Query.domain]
-    ) -> DataFrame[domain, DOMAIN_USED_COUNT]:
+    @extractor(depends_on=[MemberActivityDatasetCopy])
+    @inputs(Query.domain)
+    @outputs(domain, DOMAIN_USED_COUNT)
+    def get_domain_feature(cls, ts: pd.Series, domain: pd.Series):
         df, found = MemberActivityDatasetCopy.lookup(  # type: ignore
             ts, domain=domain
         )
         return df
 
 
 class TestInvalidSync(unittest.TestCase):
@@ -99,23 +100,22 @@
 
 @meta(owner="test@fennel.ai")
 @featureset
 class DomainFeatures2:
     domain: str = feature(id=1)
     DOMAIN_USED_COUNT: int = feature(id=2)
 
-    @extractor
-    @depends_on(MemberDataset)
-    def get_domain_feature(
-        cls, ts: Series[datetime], domain: Series[Query.domain]
-    ) -> DataFrame[domain, DOMAIN_USED_COUNT]:
+    @extractor()
+    @inputs(Query.domain)
+    @outputs(domain, DOMAIN_USED_COUNT)
+    def get_domain_feature(cls, ts: pd.Series, domain: pd.Series):
         df, found = MemberActivityDatasetCopy.lookup(  # type: ignore
             ts, domain=domain
         )
-        return df
+        return df[[str(cls.domain), str(cls.DOMAIN_USED_COUNT)]]
 
 
 class TestInvalidExtractorDependsOn(unittest.TestCase):
     @pytest.mark.integration
     @mock_client
     def test_missing_features(self, client):
         @meta(owner="test@fennel.ai")
@@ -149,48 +149,52 @@
             url: str
             uid: str
             transitionType: str
             hasShortcut: bool
             country: str
 
             @pipeline(id=1)
-            def copy(cls, ds: Dataset[MemberActivityDataset]):
+            @inputs(MemberActivityDataset)
+            def copy(cls, ds: Dataset):
                 return ds
 
         @meta(owner="test@fennel.ai")
         @featureset
         class DomainFeatures:
             domain: str = feature(id=1)
             DOMAIN_USED_COUNT: int = feature(id=2)
 
-            @extractor
-            @depends_on(MemberActivityDatasetCopy)
-            def get_domain_feature(
-                cls, ts: Series[datetime], domain: Series[Query.domain]
-            ) -> DataFrame[domain, DOMAIN_USED_COUNT]:
+            @extractor(depends_on=[MemberActivityDatasetCopy])
+            @inputs(Query.domain)
+            @outputs(domain, DOMAIN_USED_COUNT)
+            def get_domain_feature(cls, ts: pd.Series, domain: pd.Series):
                 df, found = MemberActivityDatasetCopy.lookup(  # type: ignore
                     ts, domain=domain
                 )
                 return df
 
         with pytest.raises(Exception) as e:
-            client.sync(datasets=[MemberDataset], featuresets=[DomainFeatures2])
+            client.sync(
+                datasets=[
+                    MemberActivityDatasetCopy,
+                ],
+                featuresets=[DomainFeatures],
+            )
             client.extract_features(
                 output_feature_list=[DomainFeatures2],
                 input_feature_list=[Query],
                 input_dataframe=pd.DataFrame(
                     {
                         "Query.domain": [
                             "www.google.com",
                             "www.google.com",
                         ],
                     }
                 ),
             )
-
         if client.is_integration_client():
             assert (
                 'Failed to sync: error: can not add edge: from vertex (Feature, "Query.domain") not in graph'
                 in str(e.value)
             )
         else:
             assert (
@@ -243,26 +247,23 @@
                         "Query.domain": [
                             "www.google.com",
                             "www.google.com",
                         ],
                     }
                 ),
             )
-
         if client.is_integration_client():
             assert (
                 'Failed to sync: error: can not add edge: from vertex (Dataset, "MemberActivityDataset") not in graph'
                 == str(e.value)
             )
         else:
             assert (
-                "Extractor `get_domain_feature` is not allowed to access "
-                "dataset `MemberActivityDatasetCopy`, enabled datasets are ["
-                "'MemberDataset']. Use `@depends_on` to specify dataset "
-                "dependencies." == str(e.value)
+                "Extractor `get_domain_feature` is not allowed to access dataset `MemberActivityDatasetCopy`, enabled datasets are []. Use `depends_on` param in @extractor to specify dataset dependencies."
+                == str(e.value)
             )
 
     @mock_client
     def test_drop_timestamp_col(self, client):
         with pytest.raises(Exception) as e:
 
             @meta(owner="test@fennel.ai")
@@ -272,13 +273,14 @@
                 sk: str
                 uid: str = field(key=True)
                 email: str
                 displayName: str
                 createdAt: datetime = field(timestamp=True)
 
                 @pipeline(id=1)
-                def del_timestamp(cls, d: Dataset[MemberDataset]):
+                @inputs(MemberDataset)
+                def del_timestamp(cls, d: Dataset):
                     return d.drop(columns=["createdAt"])
 
         assert (
             "cannot drop timestamp field createdAt from '[Pipeline:del_timestamp]->drop node'"
         ) == str(e.value)
```

### Comparing `fennel_ai-0.8.6/fennel/client_tests/test_search.py` & `fennel_ai-0.8.7/fennel/client_tests/test_search.py`

 * *Files 3% similar despite different names*

```diff
@@ -7,19 +7,19 @@
 import numpy as np
 import pandas as pd
 import pytest
 import requests
 
 from fennel import sources
 from fennel.datasets import dataset, Dataset, pipeline, field
-from fennel.featuresets import featureset, feature, extractor, depends_on
+from fennel.featuresets import featureset, feature, extractor
 from fennel.lib.aggregate import Count, Sum
 from fennel.lib.metadata import meta
 from fennel.lib.schema import Embedding
-from fennel.lib.schema import Series
+from fennel.lib.schema import inputs
 from fennel.lib.window import Window
 from fennel.sources import source
 from fennel.test_lib import mock_client
 
 biq_query = sources.BigQuery(
     name="bg_source",
     project_id="my-project-356105",
@@ -86,43 +86,46 @@
     body: str
     title: str
     owner: str
     origin: str
     creation_timestamp: datetime
 
     @pipeline(id=1)
-    def notion_pipe(cls, ds: Dataset[NotionDocs]):
+    @inputs(NotionDocs)
+    def notion_pipe(cls, ds: Dataset):
         return ds.transform(
             lambda df: doc_pipeline_helper(df, "Notion"),
             schema={
                 "doc_id": int,
                 "body": str,
                 "title": str,
                 "owner": str,
                 "creation_timestamp": datetime,
                 "origin": str,
             },
         )
 
     @pipeline(id=2)
-    def coda_pipe(cls, ds: Dataset[CodaDocs]):
+    @inputs(CodaDocs)
+    def coda_pipe(cls, ds: Dataset):
         return ds.transform(
             lambda df: doc_pipeline_helper(df, "Coda"),
             schema={
                 "doc_id": int,
                 "body": str,
                 "title": str,
                 "owner": str,
                 "creation_timestamp": datetime,
                 "origin": str,
             },
         )
 
     @pipeline(id=3)
-    def google_docs_pipe(cls, ds: Dataset[GoogleDocs]):
+    @inputs(GoogleDocs)
+    def google_docs_pipe(cls, ds: Dataset):
         return ds.transform(
             lambda df: doc_pipeline_helper(df, "GoogleDocs"),
             schema={
                 "doc_id": int,
                 "body": str,
                 "title": str,
                 "owner": str,
@@ -186,18 +189,16 @@
     fast_text_embedding: Embedding[256]
     num_words: int
     num_stop_words: int
     top_10_unique_words: List[str]
     creation_timestamp: datetime
 
     @pipeline(id=1)
-    def content_features(
-        cls,
-        ds: Dataset[Document],
-    ):
+    @inputs(Document)
+    def content_features(cls, ds: Dataset):
         return ds.transform(
             get_content_features,
             schema={
                 "doc_id": int,
                 "bert_embedding": Embedding[128],
                 "fast_text_embedding": Embedding[256],
                 "num_words": int,
@@ -225,15 +226,16 @@
     user_id: int = field(key=True)
     num_views: int
     num_short_views_7d: int
     num_long_views: int
     timestamp: datetime
 
     @pipeline(id=1)
-    def user_engagement_pipeline(cls, ds: Dataset[UserActivity]):
+    @inputs(UserActivity)
+    def user_engagement_pipeline(cls, ds: Dataset):
         def create_short_click(df: pd.DataFrame) -> pd.DataFrame:
             df["is_short_click"] = df[str(UserActivity.view_time)] < 5
             df["is_long_click"] = df[str(UserActivity.view_time)] >= 5
             df["is_short_click"].astype(int)
             df["is_long_click"].astype(int)
             return df
 
@@ -273,15 +275,16 @@
     num_views: int
     num_views_7d: int
     num_views_28d: int
     total_timespent: float
     timestamp: datetime
 
     @pipeline(id=1)
-    def doc_engagement_pipeline(cls, ds: Dataset[UserActivity]):
+    @inputs(UserActivity)
+    def doc_engagement_pipeline(cls, ds: Dataset):
         return ds.groupby("doc_id").aggregate(
             [
                 Count(window=Window("forever"), into_field=str(cls.num_views)),
                 Count(window=Window("7d"), into_field=str(cls.num_views_7d)),
                 Count(window=Window("28d"), into_field=str(cls.num_views_28d)),
                 Sum(
                     window=Window("forever"),
@@ -310,17 +313,17 @@
     user_id: int = feature(id=1)
     num_views: int = feature(id=2).meta(  # type: ignore
         owner="aditya@fennel.ai"
     )
     num_short_views_7d: int = feature(id=3)
     num_long_views: int = feature(id=4)
 
-    @extractor
-    @depends_on(UserEngagementDataset)
-    def get_features(cls, ts: Series[datetime], user_id: Series[Query.user_id]):
+    @extractor(depends_on=[UserEngagementDataset])
+    @inputs(Query.user_id)
+    def get_features(cls, ts: pd.Series, user_id: pd.Series):
         df, found = UserEngagementDataset.lookup(  # type: ignore
             ts, user_id=user_id  # type: ignore
         )
         df.drop("timestamp", axis=1, inplace=True)
         return df
 
 
@@ -329,17 +332,17 @@
 class DocumentFeatures:
     doc_id: int = feature(id=1)
     num_views: int = feature(id=2)
     num_views_7d: int = feature(id=3)
     total_timespent_minutes: float = feature(id=4)
     num_views_28d: int = feature(id=5)
 
-    @extractor
-    @depends_on(DocumentEngagementDataset)
-    def get_features(cls, ts: Series[datetime], doc_id: Series[Query.doc_id]):
+    @extractor(depends_on=[DocumentEngagementDataset])
+    @inputs(Query.doc_id)
+    def get_features(cls, ts: pd.Series, doc_id: pd.Series):
         df, found = DocumentEngagementDataset.lookup(  # type: ignore
             ts, doc_id=doc_id  # type: ignore
         )
         df[str(cls.total_timespent_minutes)] = df["total_timespent"] / 60
         df.drop("total_timespent", axis=1, inplace=True)
         df.drop("timestamp", axis=1, inplace=True)
         return df
@@ -351,17 +354,17 @@
     doc_id: int = feature(id=1)
     bert_embedding: Embedding[128] = feature(id=2)
     fast_text_embedding: Embedding[256] = feature(id=3)
     num_words: int = feature(id=4)
     num_stop_words: int = feature(id=5)
     top_10_unique_words: List[str] = feature(id=6)
 
-    @extractor
-    @depends_on(DocumentContentDataset)
-    def get_features(cls, ts: Series[datetime], doc_id: Series[Query.doc_id]):
+    @extractor(depends_on=[DocumentContentDataset])
+    @inputs(Query.doc_id)
+    def get_features(cls, ts: pd.Series, doc_id: pd.Series):
         df, found = DocumentContentDataset.lookup(  # type: ignore
             ts, doc_id=doc_id  # type: ignore
         )
         df.drop("creation_timestamp", axis=1, inplace=True)
         return df
```

### Comparing `fennel_ai-0.8.6/fennel/client_tests/test_social_network.py` & `fennel_ai-0.8.7/fennel/client_tests/test_social_network.py`

 * *Files 8% similar despite different names*

```diff
@@ -1,18 +1,17 @@
 from datetime import datetime
 
 import pandas as pd
 import requests
 
 from fennel.datasets import dataset, field, Dataset, pipeline
-from fennel.featuresets import depends_on
 from fennel.featuresets import featureset, feature, extractor
 from fennel.lib.aggregate import Count
 from fennel.lib.metadata import meta
-from fennel.lib.schema import Series
+from fennel.lib.schema import inputs, outputs
 from fennel.lib.schema import regex, oneof
 from fennel.lib.window import Window
 from fennel.test_lib import mock_client
 
 
 @meta(owner="data-eng@myspace.com")
 @dataset
@@ -48,50 +47,48 @@
 @dataset
 class CityInfo:
     city: str = field(key=True)
     gender: str = field(key=True)
     count: int
     timestamp: datetime
 
-    @classmethod
-    @pipeline(1)
-    def count_city_gender(cls, user_info: Dataset[UserInfo]):
+    @pipeline(id=1)
+    @inputs(UserInfo)
+    def count_city_gender(cls, user_info: Dataset):
         return user_info.groupby(["city", "gender"]).aggregate(
             [Count(window=Window("1y 5s"), into_field="count")]
         )
 
 
 @dataset
 @meta(owner="ml-eng@myspace.com")
 class UserViewsDataset:
     user_id: str = field(key=True)
     num_views: int
     time_stamp: datetime
 
-    @classmethod
     @pipeline(1)
-    def count_user_views(cls, view_data: Dataset[ViewData]):
+    @inputs(ViewData)
+    def count_user_views(cls, view_data: Dataset):
         return view_data.groupby("user_id").aggregate(
             [Count(window=Window("3y 8s"), into_field="num_views")]
         )
 
 
 @dataset
 @meta(owner="ml-eng@myspace.com")
 class UserCategoryDataset:
     user_id: str = field(key=True)
     category: str = field(key=True)
     num_views: int
     time_stamp: datetime
 
-    @classmethod
     @pipeline(1)
-    def count_user_views(
-        cls, view_data: Dataset[ViewData], post_info: Dataset[PostInfo]
-    ):
+    @inputs(ViewData, PostInfo)
+    def count_user_views(cls, view_data: Dataset, post_info: Dataset):
         post_info_enriched = view_data.left_join(post_info, on=["post_id"])
         post_info_enriched_t = post_info_enriched.transform(
             lambda df: df.fillna("unknown"),
             schema={"user_id": str, "category": str, "time_stamp": datetime},
         )
         return post_info_enriched_t.groupby("user_id", "category").aggregate(
             [Count(window=Window("3y 8s"), into_field="num_views")]
@@ -111,32 +108,32 @@
 @meta(owner="feature-team@myspace.com")
 @featureset
 class UserFeatures:
     num_views: int = feature(id=2)
     num_category_views: int = feature(id=3)
     category_view_ratio: float = feature(id=4)
 
-    @depends_on(UserViewsDataset)
-    @extractor
-    def extract_user_views(
-        cls, ts: Series[datetime], user_ids: Series[Request.user_id]
-    ) -> Series[num_views]:
+    @extractor(depends_on=[UserViewsDataset])
+    @inputs(Request.user_id)
+    @outputs(num_views)
+    def extract_user_views(cls, ts: pd.Series, user_ids: pd.Series):
         views, _ = UserViewsDataset.lookup(ts, user_id=user_ids)  # type: ignore
         views = views.fillna(0)
 
         return views["num_views"]
 
-    @depends_on(UserCategoryDataset, UserViewsDataset)
-    @extractor
+    @extractor(depends_on=[UserCategoryDataset, UserViewsDataset])
+    @inputs(Request.user_id, Request.category)
+    @outputs(category_view_ratio, num_category_views)
     def extractor_category_view(
         cls,
-        ts: Series[datetime],
-        user_ids: Series[Request.user_id],
-        categories: Series[Request.category],
-    ) -> Series[category_view_ratio, num_category_views]:
+        ts: pd.Series,
+        user_ids: pd.Series,
+        categories: pd.Series,
+    ):
         category_views, _ = UserCategoryDataset.lookup(  # type: ignore
             ts, user_id=user_ids, category=categories
         )
         views, _ = UserViewsDataset.lookup(ts, user_id=user_ids)  # type: ignore
         category_views = category_views.fillna(0)
         views = views.fillna(0.001)
         category_views["num_views"] = category_views["num_views"].astype(int)
```

### Comparing `fennel_ai-0.8.6/fennel/datasets/datasets.py` & `fennel_ai-0.8.7/fennel/datasets/datasets.py`

 * *Files 2% similar despite different names*

```diff
@@ -31,15 +31,15 @@
 )
 from fennel.lib.expectations import Expectations, GE_ATTR_FUNC
 from fennel.lib.metadata import (
     meta,
     get_meta_attr,
     set_meta_attr,
 )
-from fennel.lib.schema import dtype_to_string, get_dtype
+from fennel.lib.schema import dtype_to_string, get_dtype, FENNEL_INPUTS
 from fennel.utils import (
     fhash,
     parse_annotation_comments,
     propogate_fennel_attributes,
 )
 
 Tags = Union[List[str], Tuple[str, ...], str]
@@ -527,28 +527,38 @@
         params = []
         for name, param in sig.parameters.items():
             if not cls_param and param.name != "cls":
                 raise TypeError(
                     f"pipeline functions are classmethods and must have cls "
                     f"as the first parameter, found `{name}` for pipeline `{pipeline_name}`."
                 )
-            elif not cls_param:
-                cls_param = True
-                continue
-
-            if not isinstance(param.annotation, Dataset):
-                if issubclass(param.annotation, Dataset):
+            break
+        if not hasattr(pipeline_func, FENNEL_INPUTS):
+            raise TypeError(
+                f"pipeline `{pipeline_name}` must have "
+                f"Datasets as @input parameters."
+            )
+        inputs = getattr(pipeline_func, FENNEL_INPUTS)
+        for inp in inputs:
+            if not isinstance(inp, Dataset):
+                if issubclass(inp, Dataset):
                     raise TypeError(
                         f"pipeline `{pipeline_name}` must have "
                         f"Dataset[<Dataset Name>] as parameters."
                     )
+                if hasattr(inp, "_name"):
+                    name = inp._name
+                elif hasattr(inp, "__name__"):
+                    name = inp.__name__
+                else:
+                    name = str(inp)
                 raise TypeError(
                     f"Parameter {name} is not a Dataset in {pipeline_name}"
                 )
-            params.append(param.annotation)
+            params.append(inp)
 
         setattr(
             pipeline_func,
             PIPELINE_ATTR,
             Pipeline(inputs=list(params), func=pipeline_func, id=id),
         )
         return pipeline_func
@@ -797,33 +807,32 @@
             key_index = 0
             for name, param in sig.parameters.items():
                 if not cls_param and param.name != "cls":
                     raise TypeError(
                         f"on_demand functions are classmethods and must have "
                         f"cls as the first parameter, found {name}."
                     )
-                elif not cls_param:
-                    cls_param = True
-                    continue
-
+                break
+            inputs = getattr(on_demand.func, FENNEL_INPUTS)
+            for inp in inputs:
                 if not check_timestamp:
-                    if param.annotation == datetime.datetime:
+                    if inp == datetime.datetime:
                         check_timestamp = True
                         continue
                     raise ValueError(
                         f"on_demand method {on_demand.func.__name__} must take "
                         f"timestamp as first parameter with type Series[datetime]."
                     )
-                if param.annotation != key_fields[key_index].dtype:
+                if inp != key_fields[key_index].dtype:
                     raise ValueError(
                         f"on_demand method {on_demand.func.__name__} must take "
                         f"key fields in the same order as defined in the "
                         f"dataset with the same type, parameter "
                         f"{key_fields[key_index].name} has type"
-                        f" {param.annotation} but expected "
+                        f" {inp} but expected "
                         f" {key_fields[key_index].dtype} "
                     )
                 key_index += 1
             on_demand.bound_func = functools.partial(on_demand.func, self)
             cloudpickle.register_pickle_by_value(
                 inspect.getmodule(on_demand.func)
             )
@@ -1255,15 +1264,14 @@
         schema.name = f"'[Pipeline:{self.pipeline_name}]->union node'"
         return schema
 
     def visitRename(self, obj) -> DSSchema:
         input_schema = copy.deepcopy(self.visit(obj.node))
         input_schema.name = f"'[Pipeline:{self.pipeline_name}]->rename node'"
         for old, new in obj.column_mapping.items():
-            print(input_schema.fields())
             if old not in input_schema.fields():
                 raise ValueError(
                     f"Field {old} does not exist in schema of "
                     f"rename node {input_schema.name}."
                 )
             if new in input_schema.fields():
                 raise ValueError(
```

### Comparing `fennel_ai-0.8.6/fennel/datasets/test_dataset.py` & `fennel_ai-0.8.7/fennel/datasets/test_dataset.py`

 * *Files 1% similar despite different names*

```diff
@@ -7,15 +7,15 @@
 from google.protobuf.json_format import ParseDict  # type: ignore
 
 import fennel.gen.dataset_pb2 as ds_proto
 from fennel.datasets import dataset, pipeline, field, Dataset
 from fennel.gen.services_pb2 import SyncRequest
 from fennel.lib.aggregate import Count
 from fennel.lib.metadata import meta
-from fennel.lib.schema import Embedding
+from fennel.lib.schema import Embedding, inputs
 from fennel.lib.window import Window
 from fennel.test_lib import *
 
 
 @meta(owner="test@test.com")
 @dataset
 class UserInfoDataset:
@@ -168,15 +168,15 @@
 #         user_id: int = field(key=True)
 #         name: str = field(key=True)
 #         credit_score: float
 #         timestamp: datetime
 
 #         @on_demand(expires_after="7d")
 #         def pull_from_api(
-#             cls, ts: Series[datetime], user_id: Series[int], names: Series[str]
+#             cls, ts: pd.Series[datetime], user_id: pd.Series[int], names: pd.Series[str]
 #         ) -> pd.DataFrame:
 #             user_list = user_id.tolist()
 #             names = names.tolist()
 #             resp = requests.get(
 #                 API_ENDPOINT_URL, json={"users": user_list, "names": names}
 #             )
 #             df = pd.DataFrame(columns=["user_id", "credit_score", "timestamp"])
@@ -277,15 +277,16 @@
     @meta(owner="aditya@fennel.ai")
     @dataset
     class ABCDataset:
         a1: int = field(key=True)
         t: datetime
 
         @pipeline(id=1)
-        def pipeline1(cls, a: Dataset[A], b: Dataset[B]):
+        @inputs(A, B)
+        def pipeline1(cls, a: Dataset, b: Dataset):
             return a.left_join(b, left_on=["a1"], right_on=["b1"])
 
     view = InternalTestClient(grpc_stub)
     view.add(ABCDataset)
     sync_request = view._get_sync_request_proto()
     assert len(sync_request.datasets) == 1
     d = {
@@ -378,19 +379,16 @@
     class FraudReportAggregatedDataset:
         merchant_id: int = field(key=True)
         timestamp: datetime
         num_merchant_fraudulent_transactions: int
         num_merchant_fraudulent_transactions_7d: int
 
         @pipeline(id=1)
-        def create_fraud_dataset(
-            cls,
-            activity: Dataset[Activity],
-            user_info: Dataset[UserInfoDataset],
-        ):
+        @inputs(Activity, UserInfoDataset)
+        def create_fraud_dataset(cls, activity: Dataset, user_info: Dataset):
             def extract_info(df: pd.DataFrame) -> pd.DataFrame:
                 df["metadata_dict"] = (
                     df["metadata"].apply(json.loads).apply(pd.Series)
                 )
                 df["transaction_amount"] = df["metadata_dict"].apply(
                     lambda x: x["transaction_amt"]
                 )
@@ -631,15 +629,16 @@
 
     @dataset
     class B:
         b1: int = field(key=True)
         t: datetime
 
         @pipeline(id=1)
-        def from_a(cls, a: Dataset[A]):
+        @inputs(A)
+        def from_a(cls, a: Dataset):
             x = a.rename({"a1": "b1"})
             return x.drop(["a2", "a3"])
 
 
 def test_union_datasets(grpc_stub):
     @dataset
     class A:
@@ -654,15 +653,16 @@
     @meta(owner="test@test.com")
     @dataset
     class ABCDataset:
         a1: int = field(key=True)
         t: datetime
 
         @pipeline(id=1)
-        def pipeline2_diamond(cls, a: Dataset[A]):
+        @inputs(A)
+        def pipeline2_diamond(cls, a: Dataset):
             b = a.transform(lambda df: df)
             c = a.transform(lambda df: df * 2)
             d = b + c
             e = d.transform(lambda df: df * 3)
             f = d.transform(lambda df: df * 4)
             return e + f
 
@@ -850,18 +850,16 @@
         fast_text_embedding: Embedding[256]
         num_words: int
         num_stop_words: int
         top_10_unique_words: List[str]
         creation_timestamp: datetime
 
         @pipeline(id=1)
-        def content_features(
-            cls,
-            ds: Dataset[Document],
-        ):
+        @inputs(Document)
+        def content_features(cls, ds: Dataset):
             return ds.transform(
                 get_content_features,
                 schema={
                     "doc_id": int,
                     "bert_embedding": Embedding[128],
                     "fast_text_embedding": Embedding[256],
                     "num_words": int,
```

### Comparing `fennel_ai-0.8.6/fennel/datasets/test_dataset_lookup.py` & `fennel_ai-0.8.7/fennel/datasets/test_dataset_lookup.py`

 * *Files 7% similar despite different names*

```diff
@@ -1,17 +1,17 @@
 import pickle
 import typing
 from datetime import datetime
 
 import pandas as pd
 
 import fennel.utils
-from fennel.featuresets import featureset, feature, extractor, depends_on
+from fennel.featuresets import featureset, feature, extractor
 from fennel.lib.metadata import meta
-from fennel.lib.schema import DataFrame, Series
+from fennel.lib.schema import inputs, outputs
 from fennel.test_lib import *
 
 
 @meta(owner="test@test.com")
 @fennel.dataset
 class UserInfoDataset:
     user_id: int = fennel.field(key=True)
@@ -54,42 +54,41 @@
         userid: int = feature(id=1)
         name: str = feature(id=2)
         # The users gender among male/female/non-binary
         age_sq: int = feature(id=3).meta(owner="aditya@fennel.ai")
         age_cube: int = feature(id=4).meta(owner="mohit@fennel.ai")
         gender: str = feature(id=5)
 
-        @extractor
-        @depends_on(UserInfoDataset)
+        @extractor(depends_on=[UserInfoDataset])
+        @inputs(userid, name)
+        @outputs(age_sq, gender)
         @typing.no_type_check
         def user_age_sq(
-            cls,
-            ts: Series[datetime],
-            user_id: Series[userid],
-            names: Series[name],
-        ) -> DataFrame[age_sq, gender]:
+            cls, ts: pd.Series, user_id: pd.Series, names: pd.Series
+        ):
             user_id_plus_one = user_id * 5
             df, _ = UserInfoDataset.lookup(
                 ts,
                 user_id=user_id_plus_one,
                 name=names,
                 fields=["age", "gender"],
             )
             df["age_sq"] = df["age"] * df["age"]
             return df[["age_sq", "gender"]]
 
-        @extractor
-        @depends_on(UserInfoDataset)
+        @extractor(depends_on=[UserInfoDataset])
+        @inputs(userid, name)
+        @outputs(age_cube)
         @typing.no_type_check
         def user_age_cube(
             cls,
-            ts: Series[datetime],
-            user_id: Series[userid],
-            names: Series[name],
-        ) -> Series[age_cube]:
+            ts: pd.Series,
+            user_id: pd.Series,
+            names: pd.Series,
+        ):
             user_id_into_three = user_id * 3
             df, _ = UserInfoDataset.lookup(
                 ts,
                 user_id=user_id_into_three,
                 name=names,
             )
             df["age_cube"] = df["age"] * df["age"] * df["age"]
```

### Comparing `fennel_ai-0.8.6/fennel/datasets/test_invalid_dataset.py` & `fennel_ai-0.8.7/fennel/datasets/test_invalid_dataset.py`

 * *Files 6% similar despite different names*

```diff
@@ -1,13 +1,14 @@
 from datetime import datetime
 from typing import Optional, List
 
 import pytest
 
 from fennel.datasets import dataset, pipeline, field, Dataset
+from fennel.lib.schema import inputs
 from fennel.test_lib import *
 
 
 def test_multiple_date_time(grpc_stub):
     with pytest.raises(ValueError) as e:
 
         @dataset
@@ -95,28 +96,30 @@
 
             @pipeline(id=1)
             def create_pipeline(cls, a: Dataset):
                 return a
 
     assert (
         str(e.value)
-        == "pipeline `create_pipeline` must have Dataset[<Dataset Name>] as parameters."
+        == "pipeline `create_pipeline` must have Datasets as @input "
+        "parameters."
     )
 
     with pytest.raises(TypeError) as e:
 
         @dataset
         class ABCDataset3:
             a: int = field(key=True)
             b: int = field(key=True)
             c: int
             d: datetime
 
             @pipeline(id=1)  # type: ignore
-            def create_pipeline(a: Dataset[XYZ]):  # type: ignore
+            @inputs(XYZ)
+            def create_pipeline(a: Dataset):  # type: ignore
                 return a
 
     assert (
         str(e.value)
         == "pipeline functions are classmethods and must have cls as the "
         "first parameter, found `a` for pipeline `create_pipeline`."
     )
@@ -135,15 +138,16 @@
         class ABCDataset:
             a: int = field(key=True)
             b: int = field(key=True)
             c: int
             d: datetime
 
             @pipeline(id=1)
-            def create_pipeline(cls, a: Dataset[XYZ]):
+            @inputs(XYZ)
+            def create_pipeline(cls, a: Dataset):
                 b = a.transform(lambda x: x)
                 return a.left_join(b, on=["user_id"])  # type: ignore
 
     assert str(e.value) == "Cannot join with an intermediate dataset"
 
 
 def test_dataset_optional_key(grpc_stub):
```

### Comparing `fennel_ai-0.8.6/fennel/datasets/test_schema_validator.py` & `fennel_ai-0.8.7/fennel/datasets/test_schema_validator.py`

 * *Files 5% similar despite different names*

```diff
@@ -4,14 +4,15 @@
 
 import pandas as pd
 import pytest
 
 from fennel.datasets import dataset, field, pipeline, Dataset
 from fennel.lib.aggregate import Sum
 from fennel.lib.metadata import meta
+from fennel.lib.schema import inputs
 from fennel.lib.window import Window
 
 
 @meta(owner="test@test.com")
 @dataset
 class MovieRating:
     movie: str = field(key=True)
@@ -35,19 +36,16 @@
         class MovieStats:
             movie: str = field(key=True)
             rating: float
             revenue: int
             t: datetime
 
             @pipeline(id=1)
-            def pipeline_join(
-                cls,
-                rating: Dataset[MovieRating],
-                revenue: Dataset[MovieRevenue],
-            ):
+            @inputs(MovieRating, MovieRevenue)
+            def pipeline_join(cls, rating: Dataset, revenue: Dataset):
                 return rating.left_join(revenue, on=[str(cls.movie)])
 
     assert (
         str(e.value)
         == """[TypeError('Field `revenue` has type `Optional[int]` in `pipeline pipeline_join output value` schema but type `int` in `MovieStats value` schema.')]"""
     )
 
@@ -69,15 +67,16 @@
         class PositiveRatingActivity:
             userid: int
             rating: float
             movie: str = field(key=True)
             t: datetime
 
             @pipeline(id=1)
-            def filter_positive_ratings(cls, rating: Dataset[RatingActivity]):
+            @inputs(RatingActivity)
+            def filter_positive_ratings(cls, rating: Dataset):
                 return rating.filter(lambda df: df[df["rating"] >= 3.5])
 
     assert (
         str(e.value)
         == """[TypeError('Field `movie` is present in `PositiveRatingActivity` `key` schema but not present in `pipeline filter_positive_ratings output key` schema.'), TypeError('Field `movie` is present in `pipeline filter_positive_ratings output` `value` schema but not present in `PositiveRatingActivity value` schema.')]"""
     )
 
@@ -108,18 +107,17 @@
         @dataset
         class FraudReportAggregatedDataset:
             category: str = field(key=True)
             timestamp: datetime
             sum_categ_fraudulent_transactions_7d: int
 
             @pipeline(id=1)
+            @inputs(Activity, MerchantInfo)
             def create_fraud_dataset(
-                cls,
-                activity: Dataset[Activity],
-                merchant_info: Dataset[MerchantInfo],
+                cls, activity: Dataset, merchant_info: Dataset
             ):
                 def extract_info(df: pd.DataFrame) -> pd.DataFrame:
                     df_json = df["metadata"].apply(json.loads).apply(pd.Series)
                     df_timestamp = pd.concat([df_json, df["timestamp"]], axis=1)
                     return df_timestamp
 
                 def fillna(df: pd.DataFrame) -> pd.DataFrame:
@@ -184,15 +182,16 @@
         @dataset
         class A1:
             a1: str = field(key=True)
             b1: float
             t: datetime
 
             @pipeline(id=1)
-            def transform(cls, a: Dataset[A]):
+            @inputs(A)
+            def transform(cls, a: Dataset):
                 return a.transform(
                     lambda df: df,
                     schema={
                         "a1": int,
                         "b1": float,
                         "t": datetime,
                     },
@@ -209,15 +208,16 @@
         @dataset
         class A2:
             a1: str = field(key=True)
             b1: float
             t: datetime
 
             @pipeline(id=1)
-            def transform(cls, a: Dataset[A]):
+            @inputs(A)
+            def transform(cls, a: Dataset):
                 return a.transform(
                     lambda df: df,
                     schema={
                         "a1": str,
                         "b1": int,
                         "t": datetime,
                     },
@@ -234,15 +234,16 @@
         @dataset
         class A3:
             a1: str = field(key=True)
             b1: int
             t: datetime
 
             @pipeline(id=1)
-            def transform(cls, a: Dataset[A]):
+            @inputs(A)
+            def transform(cls, a: Dataset):
                 return a.transform(
                     lambda df: df,
                     schema={
                         "a2": str,
                         "b1": int,
                         "t": datetime,
                     },
@@ -259,15 +260,16 @@
         @dataset
         class A4:
             a1: str = field(key=True)
             b1: int
             t: datetime
 
             @pipeline(id=1)
-            def transform(cls, a: Dataset[A]):
+            @inputs(A)
+            def transform(cls, a: Dataset):
                 return a.transform(
                     lambda df: df,
                     schema={
                         "a1": str,
                         "b1": int,
                         "d": datetime,
                     },
@@ -295,15 +297,16 @@
         class C:
             movie: str = field(key=True)
             rating: float
             revenue: int
             t: datetime
 
             @pipeline(id=1)
-            def pipeline_join(cls, a: Dataset[A], b: Dataset[B]):
+            @inputs(A, B)
+            def pipeline_join(cls, a: Dataset, b: Dataset):
                 return a.left_join(b, left_on=["a1"], right_on=["b1", "b2"])
 
     assert (
         str(e.value)
         == """right_on field ['b1', 'b2'] are not the key fields of the right dataset B."""
     )
 
@@ -335,15 +338,16 @@
             a1: str = field(key=True)
             b1: float
             b2: Optional[int]
             b3: Optional[str]
             t: datetime
 
             @pipeline(id=1)
-            def pipeline_join(cls, a: Dataset[A], c: Dataset[C]):
+            @inputs(A, C)
+            def pipeline_join(cls, a: Dataset, c: Dataset):
                 return a.left_join(c, left_on=["a1"], right_on=["b1"])
 
     assert (
         str(e.value)
         == """Key field a1 has type str in left schema but, key field b1 has type int in right schema."""
     )
 
@@ -355,14 +359,15 @@
             a1: str = field(key=True)
             b1: float
             b2: Optional[int]
             b3: Optional[str]
             t: datetime
 
             @pipeline(id=1)
-            def pipeline_join(cls, a: Dataset[A], e: Dataset[E]):
+            @inputs(A, E)
+            def pipeline_join(cls, a: Dataset, e: Dataset):
                 return a.left_join(e, on=["a1"])
 
     assert (
         str(e.value)
         == """Key field a1 has type str in left schema but type int in right schema."""
     )
```

### Comparing `fennel_ai-0.8.6/fennel/featuresets/featureset.py` & `fennel_ai-0.8.7/fennel/featuresets/featureset.py`

 * *Files 6% similar despite different names*

```diff
@@ -1,13 +1,12 @@
 from __future__ import annotations
 
 import functools
 import inspect
 from dataclasses import dataclass
-from datetime import datetime
 from typing import (
     Any,
     cast,
     Callable,
     Dict,
     Type,
     TypeVar,
@@ -24,14 +23,15 @@
 from fennel.datasets import Dataset
 from fennel.lib.expectations import Expectations, GE_ATTR_FUNC
 from fennel.lib.metadata import (
     meta,
     get_meta_attr,
     set_meta_attr,
 )
+from fennel.lib.schema import FENNEL_INPUTS, FENNEL_OUTPUTS
 from fennel.utils import (
     parse_annotation_comments,
     propogate_fennel_attributes,
 )
 
 T = TypeVar("T")
 EXTRACTOR_ATTR = "__fennel_extractor__"
@@ -123,63 +123,89 @@
 ):
     ...
 
 
 @overload
 def extractor(
     *,
+    depends_on: List[T],
     version: int,
 ):
     ...
 
 
-def extractor(func: Optional[Callable] = None, version: int = 0):
+@overload
+def extractor(
+    *,
+    depends_on: List[T],
+):
+    ...
+
+
+@overload
+def extractor():
+    ...
+
+
+def extractor(
+    func: Optional[Callable] = None, depends_on: List = [], version: int = 0
+):
     """
     extractor is a decorator for a function that extracts a feature from a
     featureset.
     """
 
     def _create_extractor(extractor_func: Callable, version: int):
         if not callable(extractor_func):
             raise TypeError("extractor can only be applied to functions")
         sig = inspect.signature(extractor_func)
         extractor_name = extractor_func.__name__
         params = []
-        check_timestamp = False
         class_method = False
+        setattr(extractor_func, DEPENDS_ON_DATASETS_ATTR, list(depends_on))
+        if not hasattr(extractor_func, FENNEL_INPUTS):
+            raise TypeError(
+                f"extractor `{extractor_name}` must have a `fennel_inputs` "
+                f"attribute"
+            )
+        inputs = getattr(extractor_func, FENNEL_INPUTS)
         for name, param in sig.parameters.items():
             if not class_method and param.name != "cls":
                 raise TypeError(
                     f"extractor `{extractor_name}` should have cls as the "
                     f"first parameter since they are class methods"
                 )
-            elif not class_method:
+            else:
                 class_method = True
                 continue
-
-            if not check_timestamp:
-                if param.annotation == datetime:
-                    check_timestamp = True
-                    continue
+            if param.name != "ts":
                 raise TypeError(
-                    f"extractor `{extractor_name}` functions must have timestamp ( of type "
-                    f"Series[datetime] ) as the second parameter, found "
-                    f"`{param.annotation}` instead."
+                    f"extractor `{extractor_name}` should have ts as the "
+                    f"second parameter"
                 )
-            if (
-                not isinstance(param.annotation, Feature)
-                and not type(param.annotation) is tuple
-            ):
+            break
+
+        for inp in inputs:
+            if not isinstance(inp, Feature):
+                if hasattr(inp, "_name"):
+                    name = inp._name
+                elif hasattr(inp, "__name__"):
+                    name = inp.__name__
+                else:
+                    name = str(inp)
                 raise TypeError(
-                    f"Parameter `{name}` is not a feature or a DataFrame of "
-                    f"features but a `{type(param.annotation)}`. Please note "
+                    f"Parameter `{name}` is not a feature of but a "
+                    f"`{type(inp)}`. Please note "
                     f"that Featuresets are mutable and hence not supported."
                 )
-            params.append(param.annotation)
-        return_annotation = extractor_func.__annotations__.get("return", None)
+            params.append(inp)
+        if hasattr(extractor_func, FENNEL_OUTPUTS):
+            return_annotation = getattr(extractor_func, FENNEL_OUTPUTS)
+        else:
+            return_annotation = None
         outputs = []
         if return_annotation is not None:
             if isinstance(return_annotation, Feature):
                 # If feature name is set, it means that the feature is from another
                 # featureset.
                 if (
                     "." in str(return_annotation.fqn())
@@ -195,20 +221,19 @@
             elif isinstance(return_annotation, str):
                 raise TypeError(
                     "str datatype not supported, please ensure "
                     "from __future__ import annotations is disabled"
                 )
             elif isinstance(return_annotation, tuple):
                 for f in return_annotation:
-                    if not isinstance(f, Feature) and not isinstance(
-                        f, Featureset
-                    ):
+                    if not isinstance(f, Feature):
                         raise TypeError(
-                            "Extractors can only return a Series[feature] or a "
-                            "DataFrame[featureset]."
+                            f"Extractor `{extractor_name}` can only return a "
+                            f"set of features, but found type {type(f)} in "
+                            f"output annotation."
                         )
                     f = cast(Feature, f)
                     if "." in f.fqn() and len(f.fqn()) > 0:
                         raise TypeError(
                             "Extractors can only extract a feature defined "
                             f"in the same featureset, found "
                             f"{str(return_annotation)}."
@@ -243,25 +268,14 @@
         return wrap
 
     func = cast(Callable, func)
     # @extractor decorator was used without arguments
     return wrap(func)
 
 
-def depends_on(*datasets: Any):
-    if len(datasets) == 0:
-        raise TypeError("depends_on must have at least one dataset")
-
-    def decorator(func):
-        setattr(func, DEPENDS_ON_DATASETS_ATTR, list(datasets))
-        return func
-
-    return decorator
-
-
 # ---------------------------------------------------------------------
 # Featureset & Extractor
 # ---------------------------------------------------------------------
 
 
 @dataclass
 class Feature:
```

### Comparing `fennel_ai-0.8.6/fennel/featuresets/test_featureset.py` & `fennel_ai-0.8.7/fennel/featuresets/test_featureset.py`

 * *Files 4% similar despite different names*

```diff
@@ -1,17 +1,18 @@
 from datetime import datetime
 from typing import Optional
 
+import pandas as pd
 from google.protobuf.json_format import ParseDict  # type: ignore
 
 import fennel.gen.featureset_pb2 as fs_proto
 from fennel.datasets import dataset, field
-from fennel.featuresets import featureset, extractor, depends_on, feature
+from fennel.featuresets import featureset, extractor, feature
 from fennel.lib.metadata import meta
-from fennel.lib.schema import Series, DataFrame
+from fennel.lib.schema import inputs, outputs
 from fennel.test_lib import *
 
 
 @meta(owner="test@test.com")
 @dataset
 class UserInfoDataset:
     user_id: int = field(key=True)
@@ -39,21 +40,18 @@
         userid: int = feature(id=1)
         home_geoid: int = feature(id=2)
         # The users gender among male/female/non-binary
         gender: str = feature(id=3)
         age: int = feature(id=4).meta(owner="aditya@fennel.ai")
         income: int = feature(id=5).meta(deprecated=True)
 
-        @extractor(version=2)
-        @depends_on(UserInfoDataset)
+        @extractor(depends_on=[UserInfoDataset], version=2)
+        @inputs(User.id, User.age)
         def get_user_info(
-            cls,
-            ts: Series[datetime],
-            user_id: Series[User.id],
-            user_age: Series[User.age],
+            cls, ts: pd.Series, user_id: pd.Series, user_age: pd.Series
         ):
             return UserInfoDataset.lookup(ts, user_id=user_id)  # type: ignore
 
     view = InternalTestClient(grpc_stub)
     view.add(UserInfoDataset)
     view.add(UserInfo)
     sync_request = view._get_sync_request_proto()
@@ -171,32 +169,30 @@
         userid: int = feature(id=1)
         home_geoid: int = feature(id=2)
         # The users gender among male/female/non-binary
         gender: str = feature(id=3)
         age: int = feature(id=4).meta(owner="aditya@fennel.ai")
         income: int = feature(id=5)
 
-        @extractor
-        @depends_on(UserInfoDataset)
-        def get_user_info1(
-            cls, ts: Series[datetime], user_id: Series[User.id]
-        ) -> DataFrame[userid, home_geoid]:
+        @extractor(depends_on=[UserInfoDataset])
+        @inputs(User.id)
+        @outputs(userid, home_geoid)
+        def get_user_info1(cls, ts: pd.Series, user_id: pd.Series):
             pass
 
-        @extractor
-        @depends_on(UserInfoDataset)
-        def get_user_info2(
-            cls, ts: Series[datetime], user_id: Series[User.id]
-        ) -> DataFrame[gender, age]:
+        @extractor(depends_on=[UserInfoDataset])
+        @inputs(User.id)
+        @outputs(gender, age)
+        def get_user_info2(cls, ts: pd.Series, user_id: pd.Series):
             pass
 
         @extractor
-        def get_user_info3(
-            cls, ts: Series[datetime], user_id: Series[User.id]
-        ) -> DataFrame[income]:
+        @inputs(User.id)
+        @outputs(income)
+        def get_user_info3(cls, ts: pd.Series, user_id: pd.Series) -> income:
             pass
 
     view = InternalTestClient(grpc_stub)
     view.add(UserInfoDataset)
     view.add(UserInfo)
     sync_request = view._get_sync_request_proto()
     assert len(sync_request.feature_sets) == 1
```

### Comparing `fennel_ai-0.8.6/fennel/featuresets/test_invalid_featureset.py` & `fennel_ai-0.8.7/fennel/featuresets/test_invalid_featureset.py`

 * *Files 17% similar despite different names*

```diff
@@ -1,15 +1,16 @@
 from datetime import datetime
 from typing import Optional, List
 
+import pandas as pd
 import pytest
 
 from fennel.datasets import dataset, field
-from fennel.featuresets import featureset, extractor, depends_on, feature
-from fennel.lib.schema import Series, DataFrame
+from fennel.featuresets import featureset, extractor, feature
+from fennel.lib.schema import inputs, outputs
 
 # noinspection PyUnresolvedReferences
 from fennel.test_lib import *
 
 
 @dataset
 class UserInfoDataset:
@@ -34,25 +35,23 @@
     with pytest.raises(TypeError) as e:
 
         @featureset
         class UserInfoInvalid:
             userid: int = feature(id=1)
             home_geoid: int = feature(id=2)
 
-            @extractor
-            @depends_on(UserInfoDataset)
-            def get_user_info1(
-                cls, ts: Series[datetime], user_features: DataFrame[User]
-            ) -> DataFrame[userid, home_geoid]:
+            @extractor(depends_on=[UserInfoDataset])
+            @inputs(User)
+            @outputs(userid, home_geoid)
+            def get_user_info1(cls, ts: pd.Series, user: pd.Series):
                 pass
 
     assert (
         str(e.value)
-        == "Parameter `user_features` is not a feature or a DataFrame "
-        "of features but a `<class 'fennel.featuresets.featureset.Featureset'>`. Please note that Featuresets are mutable and hence not supported."
+        == "Parameter `User` is not a feature of but a `<class 'fennel.featuresets.featureset.Featureset'>`. Please note that Featuresets are mutable and hence not supported."
     )
 
 
 def test_complex_featureset(grpc_stub):
     with pytest.raises(TypeError) as e:
 
         @featureset
@@ -60,32 +59,30 @@
             userid: int = feature(id=1)
             home_geoid: int = feature(id=2)
             # The users gender among male/female/non-binary
             gender: str = feature(id=3)
             age: int = feature(id=4).meta(owner="aditya@fennel.ai")
             income: int = feature(id=5)
 
-            @extractor
-            @depends_on(UserInfoDataset)
-            def get_user_info1(
-                cls, ts: Series[datetime], user_id: Series[User.id]
-            ) -> DataFrame[userid, home_geoid]:
+            @extractor(depends_on=[UserInfoDataset])
+            @inputs(User.id)
+            @outputs(userid, home_geoid)
+            def get_user_info1(cls, ts: pd.Series, user_id: pd.Series):
                 pass
 
-            @extractor
-            @depends_on(UserInfoDataset)
-            def get_user_info2(
-                cls, ts: Series[datetime], user_id: Series[User.id]
-            ) -> DataFrame[gender, age]:
+            @extractor(depends_on=[UserInfoDataset])
+            @inputs(User.id)
+            @outputs(gender, age)
+            def get_user_info2(cls, ts: pd.Series, user_id: pd.Series):
                 pass
 
             @extractor
-            def get_user_info3(
-                cls, ts: Series[datetime], user_id: Series[User.id]
-            ) -> Series[gender]:
+            @inputs(User.id)
+            @outputs(gender)
+            def get_user_info3(cls, ts: pd.Series, user_id: pd.Series):
                 pass
 
     assert (
         str(e.value) == "Feature `gender` is extracted by multiple extractors."
     )
 
 
@@ -98,62 +95,61 @@
             home_geoid: int = feature(id=2)
             # The users gender among male/female/non-binary
             gender: str = feature(id=3)
             age: int = feature(id=4).meta(owner="aditya@fennel.ai")
             income: int = feature(id=5)
 
             @extractor
-            def get_user_info3(
-                cls, ts: Series[datetime], user_id: Series[User.id]
-            ) -> Series[User.age]:
+            @inputs(User.id)
+            @outputs(User.age)
+            def get_user_info3(cls, ts: pd.Series, user_id: pd.Series):
                 pass
 
     assert (
         str(e.value) == "Extractors can only extract a feature defined in "
-        "the same featureset, found User.age"
+        "the same featureset, found (User.age,)."
     )
 
     with pytest.raises(TypeError) as e:
 
         @featureset
         class UserInfo2:
             userid: int = feature(id=1)
             home_geoid: int = feature(id=2)
             # The users gender among male/female/non-binary
             gender: str = feature(id=3)
             age: int = feature(id=4).meta(owner="aditya@fennel.ai")
             income: int = feature(id=5)
 
             @extractor
-            def get_user_info3(
-                cls, ts: Series[datetime], user_id: Series[User.id]
-            ) -> DataFrame[User]:
+            @inputs(User.id)
+            @outputs(User)
+            def get_user_info3(cls, ts: pd.Series, user_id: pd.Series):
                 pass
 
     assert (
-        str(e.value) == "Extractors can only return a Series[feature] or "
-        "a DataFrame[<list of features defined in this "
-        "Featureset>]."
+        str(e.value)
+        == "Extractor `get_user_info3` can only return a set of features, but found type <class 'fennel.featuresets.featureset.Featureset'> in output annotation."
     )
 
     with pytest.raises(TypeError) as e:
 
         @featureset
         class UserInfo3:
             userid: int = feature(id=1)
             home_geoid: int = feature(id=2)
             # The users gender among male/female/non-binary
             gender: str = feature(id=3)
             age: int = feature(id=4).meta(owner="aditya@fennel.ai")
             income: int = feature(id=5)
 
             @extractor
-            def get_user_info3(
-                cls, ts: Series[datetime], user_id: Series[User.id]
-            ) -> DataFrame[User.age, User.id]:
+            @inputs(User.id)
+            @outputs(User.age, User.id)
+            def get_user_info3(cls, ts: pd.Series, user_id: pd.Series):
                 pass
 
     assert (
         str(e.value) == "Extractors can only extract a feature defined in "
         "the same featureset, found (User.age, User.id)."
     )
 
@@ -165,17 +161,16 @@
             home_geoid: int = feature(id=2)
             # The users gender among male/female/non-binary
             gender: str = feature(id=3)
             age: int = feature(id=4).meta(owner="aditya@fennel.ai")
             income: int = feature(id=5)
 
             @extractor(version="2")
-            def get_user_info3(
-                cls, ts: Series[datetime], user_id: Series[User.id]
-            ):
+            @inputs(User.id)
+            def get_user_info3(cls, ts: pd.Series, user_id: pd.Series):
                 pass
 
     assert str(e.value) == "version for extractor must be an int."
 
 
 def test_missing_id(grpc_stub):
     with pytest.raises(TypeError) as e:
```

### Comparing `fennel_ai-0.8.6/fennel/gen/.DS_Store` & `fennel_ai-0.8.7/fennel/gen/.DS_Store`

 * *Files identical despite different names*

### Comparing `fennel_ai-0.8.6/fennel/gen/connector_pb2.py` & `fennel_ai-0.8.7/fennel/gen/connector_pb2.py`

 * *Files identical despite different names*

### Comparing `fennel_ai-0.8.6/fennel/gen/connector_pb2.pyi` & `fennel_ai-0.8.7/fennel/gen/connector_pb2.pyi`

 * *Files identical despite different names*

### Comparing `fennel_ai-0.8.6/fennel/gen/dataset_pb2.py` & `fennel_ai-0.8.7/fennel/gen/dataset_pb2.py`

 * *Files identical despite different names*

### Comparing `fennel_ai-0.8.6/fennel/gen/dataset_pb2.pyi` & `fennel_ai-0.8.7/fennel/gen/dataset_pb2.pyi`

 * *Files identical despite different names*

### Comparing `fennel_ai-0.8.6/fennel/gen/expectations_pb2.py` & `fennel_ai-0.8.7/fennel/gen/expectations_pb2.py`

 * *Files identical despite different names*

### Comparing `fennel_ai-0.8.6/fennel/gen/expectations_pb2.pyi` & `fennel_ai-0.8.7/fennel/gen/expectations_pb2.pyi`

 * *Files identical despite different names*

### Comparing `fennel_ai-0.8.6/fennel/gen/featureset_pb2.py` & `fennel_ai-0.8.7/fennel/gen/featureset_pb2.py`

 * *Files identical despite different names*

### Comparing `fennel_ai-0.8.6/fennel/gen/featureset_pb2.pyi` & `fennel_ai-0.8.7/fennel/gen/featureset_pb2.pyi`

 * *Files identical despite different names*

### Comparing `fennel_ai-0.8.6/fennel/gen/metadata_pb2.py` & `fennel_ai-0.8.7/fennel/gen/metadata_pb2.py`

 * *Files identical despite different names*

### Comparing `fennel_ai-0.8.6/fennel/gen/metadata_pb2.pyi` & `fennel_ai-0.8.7/fennel/gen/metadata_pb2.pyi`

 * *Files identical despite different names*

### Comparing `fennel_ai-0.8.6/fennel/gen/pycode_pb2.py` & `fennel_ai-0.8.7/fennel/gen/pycode_pb2.py`

 * *Files identical despite different names*

### Comparing `fennel_ai-0.8.6/fennel/gen/pycode_pb2.pyi` & `fennel_ai-0.8.7/fennel/gen/pycode_pb2.pyi`

 * *Files identical despite different names*

### Comparing `fennel_ai-0.8.6/fennel/gen/schema_pb2.py` & `fennel_ai-0.8.7/fennel/gen/schema_pb2.py`

 * *Files identical despite different names*

### Comparing `fennel_ai-0.8.6/fennel/gen/schema_pb2.pyi` & `fennel_ai-0.8.7/fennel/gen/schema_pb2.pyi`

 * *Files identical despite different names*

### Comparing `fennel_ai-0.8.6/fennel/gen/services_pb2.py` & `fennel_ai-0.8.7/fennel/gen/services_pb2.py`

 * *Files identical despite different names*

### Comparing `fennel_ai-0.8.6/fennel/gen/services_pb2.pyi` & `fennel_ai-0.8.7/fennel/gen/services_pb2.pyi`

 * *Files identical despite different names*

### Comparing `fennel_ai-0.8.6/fennel/gen/services_pb2_grpc.py` & `fennel_ai-0.8.7/fennel/gen/services_pb2_grpc.py`

 * *Files identical despite different names*

### Comparing `fennel_ai-0.8.6/fennel/gen/spec_pb2.py` & `fennel_ai-0.8.7/fennel/gen/spec_pb2.py`

 * *Files identical despite different names*

### Comparing `fennel_ai-0.8.6/fennel/gen/spec_pb2.pyi` & `fennel_ai-0.8.7/fennel/gen/spec_pb2.pyi`

 * *Files identical despite different names*

### Comparing `fennel_ai-0.8.6/fennel/gen/status_pb2.py` & `fennel_ai-0.8.7/fennel/gen/status_pb2.py`

 * *Files identical despite different names*

### Comparing `fennel_ai-0.8.6/fennel/gen/status_pb2.pyi` & `fennel_ai-0.8.7/fennel/gen/status_pb2.pyi`

 * *Files identical despite different names*

### Comparing `fennel_ai-0.8.6/fennel/gen/window_pb2.py` & `fennel_ai-0.8.7/fennel/gen/window_pb2.py`

 * *Files identical despite different names*

### Comparing `fennel_ai-0.8.6/fennel/gen/window_pb2.pyi` & `fennel_ai-0.8.7/fennel/gen/window_pb2.pyi`

 * *Files identical despite different names*

### Comparing `fennel_ai-0.8.6/fennel/lib/aggregate/aggregate.py` & `fennel_ai-0.8.7/fennel/lib/aggregate/aggregate.py`

 * *Files identical despite different names*

### Comparing `fennel_ai-0.8.6/fennel/lib/ascii_visualizer/dag_ascii.py` & `fennel_ai-0.8.7/fennel/lib/ascii_visualizer/dag_ascii.py`

 * *Files identical despite different names*

### Comparing `fennel_ai-0.8.6/fennel/lib/duration/duration.py` & `fennel_ai-0.8.7/fennel/lib/duration/duration.py`

 * *Files identical despite different names*

### Comparing `fennel_ai-0.8.6/fennel/lib/duration/test_duration.py` & `fennel_ai-0.8.7/fennel/lib/duration/test_duration.py`

 * *Files identical despite different names*

### Comparing `fennel_ai-0.8.6/fennel/lib/expectations/great_expectations.py` & `fennel_ai-0.8.7/fennel/lib/expectations/great_expectations.py`

 * *Files identical despite different names*

### Comparing `fennel_ai-0.8.6/fennel/lib/expectations/supported_expectations.py` & `fennel_ai-0.8.7/fennel/lib/expectations/supported_expectations.py`

 * *Files identical despite different names*

### Comparing `fennel_ai-0.8.6/fennel/lib/expectations/test_great_expectations.py` & `fennel_ai-0.8.7/fennel/lib/expectations/test_great_expectations.py`

 * *Files identical despite different names*

### Comparing `fennel_ai-0.8.6/fennel/lib/graph_algorithms/cycle_detection.py` & `fennel_ai-0.8.7/fennel/lib/graph_algorithms/cycle_detection.py`

 * *Files identical despite different names*

### Comparing `fennel_ai-0.8.6/fennel/lib/graph_algorithms/extractor_order.py` & `fennel_ai-0.8.7/fennel/lib/graph_algorithms/extractor_order.py`

 * *Files 2% similar despite different names*

```diff
@@ -1,17 +1,16 @@
 from collections import defaultdict
 from typing import cast, List, Union, Dict, Set, Tuple
 
 from fennel.featuresets import Extractor, Featureset, Feature
 from fennel.lib.ascii_visualizer import draw_graph
 from fennel.lib.graph_algorithms.utils import extractor_graph
-from fennel.lib.schema import DataFrame
 
 
-def _get_features(feature: Union[Feature, Featureset, DataFrame]) -> set:
+def _get_features(feature: Union[Feature, Featureset]) -> set:
     if isinstance(feature, Feature):
         return {feature.fqn()}
     elif isinstance(feature, Featureset):
         return {f.fqn() for f in feature.features}
     elif type(feature) is tuple:
         return {f.fqn() for f in feature}
     else:
@@ -104,16 +103,16 @@
             edges.add(
                 (get_feature_vertex(output), get_extractor_vertex(extractor))
             )
     return vertices, edges
 
 
 def get_extractor_order(
-    input_features: List[Union[Feature, DataFrame, Featureset]],
-    output_features: List[Union[Feature, DataFrame, Featureset]],
+    input_features: List[Union[Feature, Featureset]],
+    output_features: List[Union[Feature, Featureset]],
     extractors: List[Extractor],
 ) -> List[Extractor]:
     """
     Given a list of input features and output features find the most optimal
     order to run the extractors.
     :param input_features: List of features provided by user
     :param output_features: List of features that need to be extracted
```

### Comparing `fennel_ai-0.8.6/fennel/lib/graph_algorithms/test_extractor_order.py` & `fennel_ai-0.8.7/fennel/lib/graph_algorithms/test_extractor_order.py`

 * *Files 14% similar despite different names*

```diff
@@ -1,38 +1,34 @@
-from datetime import datetime
-
 import pandas as pd
 
 from fennel.featuresets import featureset, extractor, feature
 from fennel.lib.graph_algorithms import get_extractor_order
-from fennel.lib.schema import Series, DataFrame
+from fennel.lib.schema import inputs, outputs
 
 
 @featureset
 class A:
     a1: int = feature(id=1)
     a2: int = feature(id=2)
     root: int = feature(id=3)
 
     @extractor
-    def a1_a2(
-        cls, ts: Series[datetime], root: Series[root]
-    ) -> DataFrame[a1, a2]:
+    @inputs(root)
+    def a1_a2(cls, ts: pd.Series, root: pd.Series):
         pass
 
 
 @featureset
 class B:
     b1: int = feature(id=1)
     b2: int = feature(id=2)
 
     @extractor
-    def b1_b2(
-        cls, ts: Series[datetime], a1: Series[A.a1], a2: Series[A.a2]
-    ) -> DataFrame[b1, b2]:
+    @inputs(A.a1, A.a2)
+    def b1_b2(cls, ts: pd.Series, a1: pd.Series, a2: pd.Series):
         pass
 
 
 def test_simple_extractor_path():
     extractors = A.extractors + B.extractors
     extractors = get_extractor_order([A.root], [B.b1, B.b2], extractors)
     extractors_to_run = [e.name for e in extractors]
@@ -57,74 +53,76 @@
 class C:
     c1: int = feature(id=1)
     c2: int = feature(id=2)
     c3: int = feature(id=3)
     c4: int = feature(id=4)
 
     @extractor
-    def c1_from_root(
-        cls, ts: Series[datetime], a1: Series[A.root]
-    ) -> Series[c1]:
+    @inputs(A.root)
+    @outputs(c1)
+    def c1_from_root(cls, ts: pd.Series, a1: pd.Series):
         pass
 
     @extractor
-    def from_c1(
-        cls, ts: Series[datetime], c1: Series[c1]
-    ) -> DataFrame[c2, c3, c4]:
+    @inputs(c1)
+    @outputs(c2, c3, c4)
+    def from_c1(cls, ts: pd.Series, c1: pd.Series):
         pass
 
 
 def test_complex_extractor_path():
     extractors = A.extractors + B.extractors + C.extractors
     extractors = get_extractor_order([A.root], [B.b1, B.b2, C.c2], extractors)
     extractors_to_run = [e.name for e in extractors]
     assert len(extractors_to_run) == 4
     assert extractors_to_run == [
+        "a1_a2",
         "c1_from_root",
         "from_c1",
-        "a1_a2",
         "b1_b2",
     ]
 
     extractors = A.extractors + B.extractors + C.extractors
     extractors = get_extractor_order(
         [A.root, C.c1], [B.b1, B.b2, C.c2], extractors
     )
     extractors_to_run = [e.name for e in extractors]
     assert len(extractors_to_run) == 3
-    assert extractors_to_run == ["from_c1", "a1_a2", "b1_b2"]
+    assert extractors_to_run == ["a1_a2", "from_c1", "b1_b2"]
 
 
 @featureset
 class UserInfo:
     userid: int = feature(id=1)
     name: str = feature(id=2)
     country_geoid: int = feature(id=3)
     # The users gender among male/female/non-binary
     age: int = feature(id=4).meta(owner="aditya@fennel.ai")  # type: ignore
     age_squared: int = feature(id=5)
     age_cubed: int = feature(id=6)
     is_name_common: bool = feature(id=7)
 
     @extractor
-    def get_user_age_and_name(
-        cls, ts: Series[datetime], user_id: Series[userid]
-    ) -> DataFrame[age, name]:
+    @inputs(userid)
+    @outputs(age, name)
+    def get_user_age_and_name(cls, ts: pd.Series, user_id: pd.Series):
         pass
 
     @extractor
+    @inputs(age, name)
+    @outputs(age_squared, age_cubed, is_name_common)
     def get_age_and_name_features(
-        cls, ts: Series[datetime], user_age: Series[age], name: Series[name]
-    ) -> DataFrame[age_squared, age_cubed, is_name_common]:
+        cls, ts: pd.Series, user_age: pd.Series, name: pd.Series
+    ):
         pass
 
     @extractor
-    def get_country_geoid(
-        cls, ts: Series[datetime], user_id: Series[userid]
-    ) -> Series[country_geoid]:
+    @inputs(userid)
+    @outputs(country_geoid)
+    def get_country_geoid(cls, ts: pd.Series, user_id: pd.Series):
         pass
 
 
 def test_age_feature_extraction():
     extractors = get_extractor_order(
         [UserInfo.userid], [UserInfo], UserInfo.extractors
     )
@@ -138,39 +136,33 @@
 
 @featureset
 class UserInfoTransformedFeatures:
     age_power_four: int = feature(id=1)
     is_name_common: bool = feature(id=2)
 
     @extractor
-    @extractor
+    @inputs(UserInfo.age, UserInfo.is_name_common)
     def get_user_transformed_features(
-        cls,
-        ts: Series[datetime],
-        user_features: DataFrame[UserInfo.age, UserInfo.is_name_common],
+        cls, ts: pd.Series, age: pd.Series, is_name_common: pd.Series
     ):
-        age = user_features[repr(UserInfo.age)]
-        is_name_common = user_features[repr(UserInfo.is_name_common)]
         age_power_four = age**4
         return pd.DataFrame(
             {
                 "age_power_four": age_power_four,
                 "is_name_common": is_name_common,
             }
         )
 
 
 def test_age_feature_extraction_complex():
     extractors = get_extractor_order(
         [UserInfo.userid],
         [
-            DataFrame[
-                UserInfoTransformedFeatures.age_power_four,
-                UserInfoTransformedFeatures.is_name_common,
-            ]
+            UserInfoTransformedFeatures.age_power_four,
+            UserInfoTransformedFeatures.is_name_common,
         ],
         UserInfo.extractors + UserInfoTransformedFeatures.extractors,
     )
     extractors_to_run = [e.name for e in extractors]
     assert len(extractors_to_run) == 3
     assert extractors_to_run[0] == "get_user_age_and_name"
     assert extractors_to_run[1] == "get_age_and_name_features"
```

### Comparing `fennel_ai-0.8.6/fennel/lib/graph_algorithms/utils.py` & `fennel_ai-0.8.7/fennel/lib/graph_algorithms/utils.py`

 * *Files identical despite different names*

### Comparing `fennel_ai-0.8.6/fennel/lib/metadata/metadata.py` & `fennel_ai-0.8.7/fennel/lib/metadata/metadata.py`

 * *Files identical despite different names*

### Comparing `fennel_ai-0.8.6/fennel/lib/metadata/test_invalid_metadata.py` & `fennel_ai-0.8.7/fennel/lib/metadata/test_invalid_metadata.py`

 * *Files identical despite different names*

### Comparing `fennel_ai-0.8.6/fennel/lib/metadata/test_metadata.py` & `fennel_ai-0.8.7/fennel/lib/metadata/test_metadata.py`

 * *Files 2% similar despite different names*

```diff
@@ -1,19 +1,20 @@
 from datetime import datetime
 from datetime import timedelta
 from typing import Optional, Dict, List
 
+import pandas as pd
 from google.protobuf.json_format import ParseDict  # type: ignore
 
 import fennel.gen.featureset_pb2 as fs_proto
 from fennel.datasets import dataset, field
-from fennel.featuresets import featureset, extractor, depends_on, feature
+from fennel.featuresets import featureset, extractor, feature
 from fennel.gen.services_pb2 import SyncRequest
 from fennel.lib.metadata import meta
-from fennel.lib.schema import DataFrame, Series
+from fennel.lib.schema import inputs, outputs
 from fennel.test_lib import *
 
 
 @meta(
     owner="aditya@fennel.ai",
     description="test",
     tags=["test"],
@@ -310,35 +311,32 @@
         home_geoid: int = feature(id=2)
         # The users gender among male/female
         gender: str = feature(id=3)
         age: int = feature(id=4).meta(owner="aditya@fennel.ai")
         income: int = feature(id=5)
 
         @meta(owner="a@xyz.com", description="top_meta")
-        @extractor
-        @depends_on(UserInfoDataset)
-        def get_user_info1(
-            cls, ts: Series[datetime], user_id: Series[User.id]
-        ) -> DataFrame[userid, home_geoid]:
+        @extractor(depends_on=[UserInfoDataset])
+        @inputs(User.id)
+        @outputs(userid, home_geoid)
+        def get_user_info1(cls, ts: pd.Series, user_id: pd.Series):
             pass
 
-        @extractor
+        @extractor(depends_on=[UserInfoDataset])
+        @inputs(User.id)
+        @outputs(gender, age)
         @meta(owner="b@xyz.com", description="middle_meta")
-        @depends_on(UserInfoDataset)
-        def get_user_info2(
-            cls, ts: Series[datetime], user_id: Series[User.id]
-        ) -> DataFrame[gender, age]:
+        def get_user_info2(cls, ts: pd.Series, user_id: pd.Series):
             pass
 
-        @extractor
-        @depends_on(UserInfoDataset)
+        @extractor(depends_on=[UserInfoDataset])
+        @inputs(User.id)
+        @outputs(income)
         @meta(owner="c@xyz.com", description="bottom_meta")
-        def get_user_info3(
-            cls, ts: Series[datetime], user_id: Series[User.id]
-        ) -> Series[income]:
+        def get_user_info3(cls, ts: pd.Series, user_id: pd.Series):
             pass
 
     view = InternalTestClient(grpc_stub)
     view.add(UserInfoDataset)
     view.add(UserInfo)
     sync_request = view._get_sync_request_proto()
     assert len(sync_request.datasets) == 1
```

### Comparing `fennel_ai-0.8.6/fennel/lib/schema/schema.py` & `fennel_ai-0.8.7/fennel/lib/schema/schema.py`

 * *Files 2% similar despite different names*

```diff
@@ -6,30 +6,16 @@
 from typing import Union, Any, List, TYPE_CHECKING
 
 import numpy as np
 import pandas as pd
 
 import fennel.gen.schema_pb2 as schema_proto
 
-if TYPE_CHECKING:
-    Series = pd.Series
-else:
-
-    class Series:
-        def __class_getitem__(cls, item):
-            return item
-
-
-if TYPE_CHECKING:
-    DataFrame = pd.DataFrame
-else:
-
-    class DataFrame:
-        def __class_getitem__(cls, item):
-            return item
+FENNEL_INPUTS = "__fennel_inputs__"
+FENNEL_OUTPUTS = "__fennel_outputs__"
 
 
 def _get_args(type_: Any) -> Any:
     """Get the type arguments of a type."""
     return getattr(type_, "__args__", None)
 
 
@@ -493,7 +479,29 @@
         try:
             _validate_field_in_df(field, df)
         except ValueError as e:
             exceptions.append(e)
         except Exception as e:
             raise e
     return exceptions
+
+
+def inputs(*inps: Any):
+    if len(inps) == 0:
+        raise ValueError("No inputs specified")
+
+    def decorator(func):
+        setattr(func, FENNEL_INPUTS, inps)
+        return func
+
+    return decorator
+
+
+def outputs(*outs: Any):
+    if len(outs) == 0:
+        raise ValueError("No outputs specified")
+
+    def decorator(func):
+        setattr(func, FENNEL_OUTPUTS, outs)
+        return func
+
+    return decorator
```

### Comparing `fennel_ai-0.8.6/fennel/lib/schema/test_schema.py` & `fennel_ai-0.8.7/fennel/lib/schema/test_schema.py`

 * *Files identical despite different names*

### Comparing `fennel_ai-0.8.6/fennel/lib/to_proto/serializer.py` & `fennel_ai-0.8.7/fennel/lib/to_proto/serializer.py`

 * *Files identical despite different names*

### Comparing `fennel_ai-0.8.6/fennel/lib/to_proto/to_proto.py` & `fennel_ai-0.8.7/fennel/lib/to_proto/to_proto.py`

 * *Files identical despite different names*

### Comparing `fennel_ai-0.8.6/fennel/lib/window/window.py` & `fennel_ai-0.8.7/fennel/lib/window/window.py`

 * *Files identical despite different names*

### Comparing `fennel_ai-0.8.6/fennel/sources/sources.py` & `fennel_ai-0.8.7/fennel/sources/sources.py`

 * *Files identical despite different names*

### Comparing `fennel_ai-0.8.6/fennel/sources/test_invalid_sources.py` & `fennel_ai-0.8.7/fennel/sources/test_invalid_sources.py`

 * *Files identical despite different names*

### Comparing `fennel_ai-0.8.6/fennel/sources/test_sources.py` & `fennel_ai-0.8.7/fennel/sources/test_sources.py`

 * *Files identical despite different names*

### Comparing `fennel_ai-0.8.6/fennel/test_lib/executor.py` & `fennel_ai-0.8.7/fennel/test_lib/executor.py`

 * *Files identical despite different names*

### Comparing `fennel_ai-0.8.6/fennel/test_lib/grpc_mock.py` & `fennel_ai-0.8.7/fennel/test_lib/grpc_mock.py`

 * *Files identical despite different names*

### Comparing `fennel_ai-0.8.6/fennel/test_lib/integration_client.py` & `fennel_ai-0.8.7/fennel/test_lib/integration_client.py`

 * *Files 4% similar despite different names*

```diff
@@ -42,20 +42,16 @@
     ret_pa, found_pa = lookup(ds_name, ts_pa, fields, keys_pa)
 
     # convert back to pandas
     return ret_pa.to_pandas(), found_pa.to_pandas()
 
 
 class IntegrationClient:
-    def __init__(self, tier_id, reset_db, is_data_integration_test):
-        self._client = RustClient(
-            tier_id=tier_id,
-            reset_db=reset_db,
-            data_integration=is_data_integration_test,
-        )
+    def __init__(self):
+        self._client = RustClient()
         self.to_register: Set[str] = set()
         self.to_register_objects: List[Union[Dataset, Featureset]] = []
         fennel.datasets.datasets.dataset_lookup = lookup_wrapper
 
     def is_integration_client(self):
         return True
 
@@ -75,17 +71,14 @@
         for featureset in featuresets:
             self.add(featureset)
         sync_request = self._get_sync_request_proto()
         self._client.sync(sync_request.SerializeToString())
         time.sleep(1.1)
         return FakeResponse(200, "OK")
 
-    def __del__(self):
-        self._client.close()
-
     def extract_features(
         self,
         input_feature_list: List[Union[Feature, Featureset]],
         output_feature_list: List[Union[Feature, Featureset]],
         input_dataframe: pd.DataFrame,
         log: bool = False,
         workflow: str = "default",
```

### Comparing `fennel_ai-0.8.6/fennel/test_lib/local_client.py` & `fennel_ai-0.8.7/fennel/test_lib/local_client.py`

 * *Files identical despite different names*

### Comparing `fennel_ai-0.8.6/fennel/test_lib/mock_client.py` & `fennel_ai-0.8.7/fennel/test_lib/mock_client.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,9 @@
 from __future__ import annotations
 
-import hashlib
 import json
 import os
 from collections import defaultdict
 from dataclasses import dataclass
 from datetime import datetime
 from functools import partial
 from typing import Dict, List, Tuple, Union, Optional
@@ -68,15 +67,16 @@
         raise ValueError(
             f"Dataset {cls_name} not found, please ensure it is synced."
         )
     if allowed_datasets is not None and cls_name not in allowed_datasets:
         raise ValueError(
             f"Extractor `{extractor_name}` is not allowed to access dataset "
             f"`{cls_name}`, enabled datasets are {allowed_datasets}. "
-            f"Use `@depends_on` to specify dataset dependencies."
+            f"Use `depends_on` param in @extractor to specify dataset "
+            f"dependencies."
         )
     right_key_fields = datasets[cls_name].key_fields
     if len(right_key_fields) == 0:
         raise ValueError(
             f"Dataset {cls_name} does not have any key fields. "
             f"Cannot perform lookup operation on it."
         )
@@ -349,15 +349,15 @@
         args = []
         for input in extractor.inputs:
             if isinstance(input, Feature):
                 if input.fqn_ in intermediate_data:
                     args.append(intermediate_data[input.fqn_])
                 else:
                     raise Exception(
-                        f"Feature {input} could not be "
+                        f"Feature `{input}` could not be "
                         f"calculated by any extractor."
                     )
             elif isinstance(input, Featureset):
                 raise Exception(
                     "Featureset is not supported as input to an "
                     "extractor since they are mutable."
                 )
@@ -511,27 +511,12 @@
             client = MockClient()
             f = test_func(*args, **kwargs, client=client)
         if (
             "USE_INT_CLIENT" in os.environ
             and int(os.environ.get("USE_INT_CLIENT")) == 1
         ):
             print("Running rust client tests")
-            # Tier ID is hash of the test name
-            tier_id = (
-                int(
-                    hashlib.sha256(
-                        (test_func.__name__).encode("utf-8")
-                    ).hexdigest(),
-                    16,
-                )
-                % 10**9
-            )
-            is_data_integration_test = "data_integration" in test_func.__name__
-            client = IntegrationClient(
-                tier_id,
-                reset_db=True,
-                is_data_integration_test=is_data_integration_test,
-            )
+            client = IntegrationClient()
             f = test_func(*args, **kwargs, client=client)
         return f
 
     return wrapper
```

### Comparing `fennel_ai-0.8.6/fennel/test_lib/test_utils.py` & `fennel_ai-0.8.7/fennel/test_lib/test_utils.py`

 * *Files identical despite different names*

### Comparing `fennel_ai-0.8.6/fennel/test_utils.py` & `fennel_ai-0.8.7/fennel/test_utils.py`

 * *Files identical despite different names*

### Comparing `fennel_ai-0.8.6/fennel/utils.py` & `fennel_ai-0.8.7/fennel/utils.py`

 * *Files identical despite different names*

### Comparing `fennel_ai-0.8.6/pyproject.toml` & `fennel_ai-0.8.7/pyproject.toml`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 [tool.poetry]
 name = "fennel-ai"
-version = "0.8.6"
+version = "0.8.7"
 description = "The modern realtime feature engineering platform"
 authors = ["Fennel AI <developers@fennel.ai>"]
 packages = [
     { include = "fennel" }
 ]
 readme = "README.md"
```

### Comparing `fennel_ai-0.8.6/setup.py` & `fennel_ai-0.8.7/setup.py`

 * *Files 0% similar despite different names*

```diff
@@ -37,15 +37,15 @@
  'pytest-mock>=3.9.0,<4.0.0',
  'pytest>=7.1.3,<8.0.0',
  'requests>=2.28.1,<3.0.0',
  'types-requests>=2.28.11,<3.0.0']
 
 setup_kwargs = {
     'name': 'fennel-ai',
-    'version': '0.8.6',
+    'version': '0.8.7',
     'description': 'The modern realtime feature engineering platform',
     'long_description': "# Welcome to Fennel\n\n## The modern realtime feature engineering platform\n\n---\n\nFennel is a modern realtime feature engineering platform and has been architected from the ground up in service of three design goals.\n\n## Fennel's Three Design Goals\n1. Easy to install, learn & use - using familiar Python instead of special DSLs, simple but powerful abstractions, zero dependency installation, fully managed with zero ops, same code working for both realtime and non-realtime cases and more to make using Fennel as easy as possible\n2. Reduce cloud costs - being significantly lower on cloud costs compared to other alternatives by squeezing as much out of cloud hardware as possible [See  for how Fennel does this]\n3. Encourage best practices - native support for testing, CI/CD, versioned & immutable features, lineage tracking, enforcement of code ownership, data expectations, read/write compute separation and more to help you bring best engineering practices to feature engineering too\n\nAs a result of the architectural philosophy, Fennel ends up unlocking the following benefits:\n\n## Benefits of Fennel\n\n1. Higher development velocity: more iterations can be done in the same time leading to higher business value\n2. Lower total costs of ownership: Fennel saves costs across the board - cloud spend, bandwidth of engineers that would have gone in ops, and bandwidth of data scientists by making them more productive\n3. Higher business value via realtime features: unlocking realtime and other sophisticated features leads to better models with higher business gains\n4. Healthier codebase & more reliable features: engineering best practices like testing, immutability, code ownership etc improve code maintainability leading to more reliable data & feature\n\n## Getting Started With Fennel\n\n[Start](https://docs.fennel.ai/getting-started/quickstart) here if you want to directly dive deep into an end-to-end example.\n\nOr if you are not in a hurry, read about the main [concepts](https://docs.fennel.ai/overview/concepts) first followed by some more details about the [datasets](https://docs.fennel.ai/datasets/overview)  and [featuresets](https://docs.fennel.ai/featuresets/overview-wip) . And if you run into any issues or have any questions/feedback, you're welcome to jump into our slack channel to directly chat with the engineers building it.\nWe, the team behind Fennel, have thoroughly enjoyed building Fennel and hope learning and using Fennel brings as much delight to you as well!",
     'author': 'Fennel AI',
     'author_email': 'developers@fennel.ai',
     'maintainer': 'None',
     'maintainer_email': 'None',
     'url': 'None',
```

### Comparing `fennel_ai-0.8.6/PKG-INFO` & `fennel_ai-0.8.7/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: fennel-ai
-Version: 0.8.6
+Version: 0.8.7
 Summary: The modern realtime feature engineering platform
 Author: Fennel AI
 Author-email: developers@fennel.ai
 Requires-Python: >=3.8,<4.0
 Classifier: Programming Language :: Python :: 3
 Classifier: Programming Language :: Python :: 3.8
 Classifier: Programming Language :: Python :: 3.9
```

