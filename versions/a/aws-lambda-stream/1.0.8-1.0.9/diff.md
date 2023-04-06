# Comparing `tmp/aws_lambda_stream-1.0.8.tar.gz` & `tmp/aws_lambda_stream-1.0.9.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "aws_lambda_stream-1.0.8.tar", max compression
+gzip compressed data, was "aws_lambda_stream-1.0.9.tar", max compression
```

## Comparing `aws_lambda_stream-1.0.8.tar` & `aws_lambda_stream-1.0.9.tar`

### file list

```diff
@@ -1,58 +1,58 @@
--rw-r--r--   0        0        0     1076 2023-02-08 05:37:14.950615 aws_lambda_stream-1.0.8/LICENSE
--rw-r--r--   0        0        0      478 2023-02-08 06:37:38.252467 aws_lambda_stream-1.0.8/README.md
--rw-r--r--   0        0        0      747 2023-02-03 18:24:04.273418 aws_lambda_stream-1.0.8/aws_lambda_stream/__init__.py
--rw-r--r--   0        0        0      352 2023-03-01 04:00:26.276550 aws_lambda_stream-1.0.8/aws_lambda_stream/connectors/__init__.py
--rw-r--r--   0        0        0     1602 2023-02-03 19:26:10.049622 aws_lambda_stream-1.0.8/aws_lambda_stream/connectors/dynamodb.py
--rw-r--r--   0        0        0     3509 2022-11-10 14:59:59.886154 aws_lambda_stream-1.0.8/aws_lambda_stream/connectors/elasticsearch.py
--rw-r--r--   0        0        0      221 2022-10-05 04:58:41.716315 aws_lambda_stream-1.0.8/aws_lambda_stream/connectors/eventbridge.py
--rw-r--r--   0        0        0      186 2023-03-01 03:52:09.979571 aws_lambda_stream-1.0.8/aws_lambda_stream/connectors/lambda_.py
--rw-r--r--   0        0        0      908 2022-10-12 14:15:26.216275 aws_lambda_stream-1.0.8/aws_lambda_stream/connectors/s3.py
--rw-r--r--   0        0        0      678 2023-02-14 05:33:36.467074 aws_lambda_stream-1.0.8/aws_lambda_stream/connectors/sns.py
--rw-r--r--   0        0        0      563 2023-02-14 05:28:39.331132 aws_lambda_stream-1.0.8/aws_lambda_stream/connectors/sqs.py
--rw-r--r--   0        0        0       70 2022-09-07 12:25:07.481058 aws_lambda_stream-1.0.8/aws_lambda_stream/events/__init__.py
--rw-r--r--   0        0        0     4650 2023-02-16 05:15:17.334571 aws_lambda_stream-1.0.8/aws_lambda_stream/events/dynamodb.py
--rw-r--r--   0        0        0     1016 2023-02-08 23:12:04.697392 aws_lambda_stream-1.0.8/aws_lambda_stream/events/kinesis.py
--rw-r--r--   0        0        0     2301 2023-02-03 18:24:04.276261 aws_lambda_stream-1.0.8/aws_lambda_stream/events/s3.py
--rw-r--r--   0        0        0     2073 2023-02-03 18:24:04.276592 aws_lambda_stream-1.0.8/aws_lambda_stream/events/sns.py
--rw-r--r--   0        0        0     1470 2023-02-03 18:24:04.277239 aws_lambda_stream-1.0.8/aws_lambda_stream/events/sqs.py
--rw-r--r--   0        0        0      172 2023-02-03 18:24:04.278143 aws_lambda_stream-1.0.8/aws_lambda_stream/filters/__init__.py
--rw-r--r--   0        0        0      204 2023-02-03 18:24:04.278452 aws_lambda_stream-1.0.8/aws_lambda_stream/filters/content.py
--rw-r--r--   0        0        0      639 2022-11-15 14:34:45.024830 aws_lambda_stream-1.0.8/aws_lambda_stream/filters/event_type.py
--rw-r--r--   0        0        0      754 2023-02-08 03:34:42.274970 aws_lambda_stream-1.0.8/aws_lambda_stream/filters/latch.py
--rw-r--r--   0        0        0      504 2023-02-03 18:24:04.278934 aws_lambda_stream-1.0.8/aws_lambda_stream/filters/skip.py
--rw-r--r--   0        0        0        0 2022-10-05 03:29:29.473147 aws_lambda_stream-1.0.8/aws_lambda_stream/flavors/__init__.py
--rw-r--r--   0        0        0     1041 2023-02-07 23:38:45.570357 aws_lambda_stream-1.0.8/aws_lambda_stream/flavors/cdc.py
--rw-r--r--   0        0        0     2487 2023-02-03 18:24:04.279800 aws_lambda_stream-1.0.8/aws_lambda_stream/flavors/collect.py
--rw-r--r--   0        0        0     2820 2023-02-03 18:24:04.280222 aws_lambda_stream-1.0.8/aws_lambda_stream/flavors/correlate.py
--rw-r--r--   0        0        0     1071 2023-02-03 18:24:04.281121 aws_lambda_stream-1.0.8/aws_lambda_stream/flavors/elasticsearch.py
--rw-r--r--   0        0        0     7191 2023-02-22 21:55:44.377898 aws_lambda_stream-1.0.8/aws_lambda_stream/flavors/evaluate.py
--rw-r--r--   0        0        0     1124 2023-02-08 03:37:45.548460 aws_lambda_stream-1.0.8/aws_lambda_stream/flavors/materialize.py
--rw-r--r--   0        0        0      992 2023-02-08 04:33:57.896213 aws_lambda_stream-1.0.8/aws_lambda_stream/flavors/s3.py
--rw-r--r--   0        0        0      896 2023-02-03 18:24:04.282923 aws_lambda_stream-1.0.8/aws_lambda_stream/flavors/sns.py
--rw-r--r--   0        0        0     2813 2023-03-01 04:42:58.732633 aws_lambda_stream-1.0.8/aws_lambda_stream/flavors/task.py
--rw-r--r--   0        0        0     2892 2023-02-16 05:07:21.062429 aws_lambda_stream-1.0.8/aws_lambda_stream/pipelines/__init__.py
--rw-r--r--   0        0        0     3570 2023-02-16 05:06:42.204097 aws_lambda_stream-1.0.8/aws_lambda_stream/repositories/__init__.py
--rw-r--r--   0        0        0      436 2022-10-05 03:50:07.747050 aws_lambda_stream-1.0.8/aws_lambda_stream/utils/__init__.py
--rw-r--r--   0        0        0      140 2023-02-14 05:32:21.038521 aws_lambda_stream-1.0.8/aws_lambda_stream/utils/aws.py
--rw-r--r--   0        0        0      153 2022-10-05 04:49:33.238263 aws_lambda_stream-1.0.8/aws_lambda_stream/utils/batch.py
--rw-r--r--   0        0        0      244 2022-10-05 04:49:17.299087 aws_lambda_stream-1.0.8/aws_lambda_stream/utils/concurrency.py
--rw-r--r--   0        0        0      163 2022-10-05 04:43:54.856386 aws_lambda_stream-1.0.8/aws_lambda_stream/utils/decorators.py
--rw-r--r--   0        0        0     4794 2023-02-08 23:10:24.837093 aws_lambda_stream-1.0.8/aws_lambda_stream/utils/dynamodb.py
--rw-r--r--   0        0        0     1889 2023-02-14 06:26:12.182019 aws_lambda_stream-1.0.8/aws_lambda_stream/utils/elasticsearch.py
--rw-r--r--   0        0        0     2256 2023-02-09 19:29:00.766950 aws_lambda_stream-1.0.8/aws_lambda_stream/utils/eventbridge.py
--rw-r--r--   0        0        0     2750 2023-02-03 18:24:04.286064 aws_lambda_stream-1.0.8/aws_lambda_stream/utils/faults.py
--rw-r--r--   0        0        0      413 2023-02-03 18:24:04.286668 aws_lambda_stream-1.0.8/aws_lambda_stream/utils/filters.py
--rw-r--r--   0        0        0      333 2023-02-03 18:24:04.287082 aws_lambda_stream-1.0.8/aws_lambda_stream/utils/json_encoder.py
--rw-r--r--   0        0        0      558 2023-03-01 04:10:54.251855 aws_lambda_stream-1.0.8/aws_lambda_stream/utils/lambda_.py
--rw-r--r--   0        0        0      618 2022-09-20 05:37:59.968618 aws_lambda_stream-1.0.8/aws_lambda_stream/utils/logger.py
--rw-r--r--   0        0        0     1982 2023-02-03 18:24:04.287769 aws_lambda_stream-1.0.8/aws_lambda_stream/utils/operators.py
--rw-r--r--   0        0        0      268 2022-10-05 03:53:16.892335 aws_lambda_stream-1.0.8/aws_lambda_stream/utils/opt.py
--rw-r--r--   0        0        0      345 2022-11-15 05:45:17.281224 aws_lambda_stream-1.0.8/aws_lambda_stream/utils/pluralize.py
--rw-r--r--   0        0        0      440 2022-10-12 16:28:48.582840 aws_lambda_stream-1.0.8/aws_lambda_stream/utils/s3.py
--rw-r--r--   0        0        0      908 2022-11-15 05:25:05.442119 aws_lambda_stream-1.0.8/aws_lambda_stream/utils/sns.py
--rw-r--r--   0        0        0      964 2023-02-09 19:19:31.634487 aws_lambda_stream-1.0.8/aws_lambda_stream/utils/split.py
--rw-r--r--   0        0        0      994 2023-02-03 18:24:04.288012 aws_lambda_stream-1.0.8/aws_lambda_stream/utils/tags.py
--rw-r--r--   0        0        0      370 2023-02-03 18:24:04.288204 aws_lambda_stream-1.0.8/aws_lambda_stream/utils/time.py
--rw-r--r--   0        0        0      609 2023-03-01 04:48:24.020896 aws_lambda_stream-1.0.8/pyproject.toml
--rw-r--r--   0        0        0     1550 2023-03-01 04:49:05.691562 aws_lambda_stream-1.0.8/setup.py
--rw-r--r--   0        0        0     1287 2023-03-01 04:49:05.691700 aws_lambda_stream-1.0.8/PKG-INFO
+-rw-r--r--   0        0        0     1076 2023-02-08 05:37:14.950615 aws_lambda_stream-1.0.9/LICENSE
+-rw-r--r--   0        0        0      478 2023-02-08 06:37:38.252467 aws_lambda_stream-1.0.9/README.md
+-rw-r--r--   0        0        0      747 2023-02-03 18:24:04.273418 aws_lambda_stream-1.0.9/aws_lambda_stream/__init__.py
+-rw-r--r--   0        0        0      352 2023-03-01 04:00:26.276550 aws_lambda_stream-1.0.9/aws_lambda_stream/connectors/__init__.py
+-rw-r--r--   0        0        0     1602 2023-02-03 19:26:10.049622 aws_lambda_stream-1.0.9/aws_lambda_stream/connectors/dynamodb.py
+-rw-r--r--   0        0        0     3509 2022-11-10 14:59:59.886154 aws_lambda_stream-1.0.9/aws_lambda_stream/connectors/elasticsearch.py
+-rw-r--r--   0        0        0      221 2022-10-05 04:58:41.716315 aws_lambda_stream-1.0.9/aws_lambda_stream/connectors/eventbridge.py
+-rw-r--r--   0        0        0      186 2023-03-01 03:52:09.979571 aws_lambda_stream-1.0.9/aws_lambda_stream/connectors/lambda_.py
+-rw-r--r--   0        0        0      908 2022-10-12 14:15:26.216275 aws_lambda_stream-1.0.9/aws_lambda_stream/connectors/s3.py
+-rw-r--r--   0        0        0      678 2023-02-14 05:33:36.467074 aws_lambda_stream-1.0.9/aws_lambda_stream/connectors/sns.py
+-rw-r--r--   0        0        0      563 2023-02-14 05:28:39.331132 aws_lambda_stream-1.0.9/aws_lambda_stream/connectors/sqs.py
+-rw-r--r--   0        0        0       70 2022-09-07 12:25:07.481058 aws_lambda_stream-1.0.9/aws_lambda_stream/events/__init__.py
+-rw-r--r--   0        0        0     4650 2023-02-16 05:15:17.334571 aws_lambda_stream-1.0.9/aws_lambda_stream/events/dynamodb.py
+-rw-r--r--   0        0        0     1016 2023-02-08 23:12:04.697392 aws_lambda_stream-1.0.9/aws_lambda_stream/events/kinesis.py
+-rw-r--r--   0        0        0     2301 2023-02-03 18:24:04.276261 aws_lambda_stream-1.0.9/aws_lambda_stream/events/s3.py
+-rw-r--r--   0        0        0     2073 2023-02-03 18:24:04.276592 aws_lambda_stream-1.0.9/aws_lambda_stream/events/sns.py
+-rw-r--r--   0        0        0     1470 2023-02-03 18:24:04.277239 aws_lambda_stream-1.0.9/aws_lambda_stream/events/sqs.py
+-rw-r--r--   0        0        0      172 2023-02-03 18:24:04.278143 aws_lambda_stream-1.0.9/aws_lambda_stream/filters/__init__.py
+-rw-r--r--   0        0        0      204 2023-02-03 18:24:04.278452 aws_lambda_stream-1.0.9/aws_lambda_stream/filters/content.py
+-rw-r--r--   0        0        0      639 2022-11-15 14:34:45.024830 aws_lambda_stream-1.0.9/aws_lambda_stream/filters/event_type.py
+-rw-r--r--   0        0        0      754 2023-02-08 03:34:42.274970 aws_lambda_stream-1.0.9/aws_lambda_stream/filters/latch.py
+-rw-r--r--   0        0        0      504 2023-02-03 18:24:04.278934 aws_lambda_stream-1.0.9/aws_lambda_stream/filters/skip.py
+-rw-r--r--   0        0        0        0 2022-10-05 03:29:29.473147 aws_lambda_stream-1.0.9/aws_lambda_stream/flavors/__init__.py
+-rw-r--r--   0        0        0     1041 2023-02-07 23:38:45.570357 aws_lambda_stream-1.0.9/aws_lambda_stream/flavors/cdc.py
+-rw-r--r--   0        0        0     2487 2023-02-03 18:24:04.279800 aws_lambda_stream-1.0.9/aws_lambda_stream/flavors/collect.py
+-rw-r--r--   0        0        0     2820 2023-02-03 18:24:04.280222 aws_lambda_stream-1.0.9/aws_lambda_stream/flavors/correlate.py
+-rw-r--r--   0        0        0     1071 2023-02-03 18:24:04.281121 aws_lambda_stream-1.0.9/aws_lambda_stream/flavors/elasticsearch.py
+-rw-r--r--   0        0        0     7191 2023-02-22 21:55:44.377898 aws_lambda_stream-1.0.9/aws_lambda_stream/flavors/evaluate.py
+-rw-r--r--   0        0        0     1124 2023-02-08 03:37:45.548460 aws_lambda_stream-1.0.9/aws_lambda_stream/flavors/materialize.py
+-rw-r--r--   0        0        0      992 2023-02-08 04:33:57.896213 aws_lambda_stream-1.0.9/aws_lambda_stream/flavors/s3.py
+-rw-r--r--   0        0        0      896 2023-02-03 18:24:04.282923 aws_lambda_stream-1.0.9/aws_lambda_stream/flavors/sns.py
+-rw-r--r--   0        0        0     2813 2023-03-01 04:42:58.732633 aws_lambda_stream-1.0.9/aws_lambda_stream/flavors/task.py
+-rw-r--r--   0        0        0     2892 2023-02-16 05:07:21.062429 aws_lambda_stream-1.0.9/aws_lambda_stream/pipelines/__init__.py
+-rw-r--r--   0        0        0     3570 2023-02-16 05:06:42.204097 aws_lambda_stream-1.0.9/aws_lambda_stream/repositories/__init__.py
+-rw-r--r--   0        0        0      436 2022-10-05 03:50:07.747050 aws_lambda_stream-1.0.9/aws_lambda_stream/utils/__init__.py
+-rw-r--r--   0        0        0      140 2023-02-14 05:32:21.038521 aws_lambda_stream-1.0.9/aws_lambda_stream/utils/aws.py
+-rw-r--r--   0        0        0      153 2022-10-05 04:49:33.238263 aws_lambda_stream-1.0.9/aws_lambda_stream/utils/batch.py
+-rw-r--r--   0        0        0      244 2022-10-05 04:49:17.299087 aws_lambda_stream-1.0.9/aws_lambda_stream/utils/concurrency.py
+-rw-r--r--   0        0        0      163 2022-10-05 04:43:54.856386 aws_lambda_stream-1.0.9/aws_lambda_stream/utils/decorators.py
+-rw-r--r--   0        0        0     4794 2023-02-08 23:10:24.837093 aws_lambda_stream-1.0.9/aws_lambda_stream/utils/dynamodb.py
+-rw-r--r--   0        0        0     1889 2023-02-14 06:26:12.182019 aws_lambda_stream-1.0.9/aws_lambda_stream/utils/elasticsearch.py
+-rw-r--r--   0        0        0     2256 2023-02-09 19:29:00.766950 aws_lambda_stream-1.0.9/aws_lambda_stream/utils/eventbridge.py
+-rw-r--r--   0        0        0     2750 2023-02-03 18:24:04.286064 aws_lambda_stream-1.0.9/aws_lambda_stream/utils/faults.py
+-rw-r--r--   0        0        0      413 2023-02-03 18:24:04.286668 aws_lambda_stream-1.0.9/aws_lambda_stream/utils/filters.py
+-rw-r--r--   0        0        0      333 2023-02-03 18:24:04.287082 aws_lambda_stream-1.0.9/aws_lambda_stream/utils/json_encoder.py
+-rw-r--r--   0        0        0      558 2023-03-01 04:10:54.251855 aws_lambda_stream-1.0.9/aws_lambda_stream/utils/lambda_.py
+-rw-r--r--   0        0        0      618 2022-09-20 05:37:59.968618 aws_lambda_stream-1.0.9/aws_lambda_stream/utils/logger.py
+-rw-r--r--   0        0        0     1982 2023-02-03 18:24:04.287769 aws_lambda_stream-1.0.9/aws_lambda_stream/utils/operators.py
+-rw-r--r--   0        0        0      268 2022-10-05 03:53:16.892335 aws_lambda_stream-1.0.9/aws_lambda_stream/utils/opt.py
+-rw-r--r--   0        0        0      345 2022-11-15 05:45:17.281224 aws_lambda_stream-1.0.9/aws_lambda_stream/utils/pluralize.py
+-rw-r--r--   0        0        0      440 2022-10-12 16:28:48.582840 aws_lambda_stream-1.0.9/aws_lambda_stream/utils/s3.py
+-rw-r--r--   0        0        0      908 2022-11-15 05:25:05.442119 aws_lambda_stream-1.0.9/aws_lambda_stream/utils/sns.py
+-rw-r--r--   0        0        0      964 2023-02-09 19:19:31.634487 aws_lambda_stream-1.0.9/aws_lambda_stream/utils/split.py
+-rw-r--r--   0        0        0      994 2023-02-03 18:24:04.288012 aws_lambda_stream-1.0.9/aws_lambda_stream/utils/tags.py
+-rw-r--r--   0        0        0      370 2023-02-03 18:24:04.288204 aws_lambda_stream-1.0.9/aws_lambda_stream/utils/time.py
+-rw-r--r--   0        0        0      609 2023-03-01 05:04:42.270007 aws_lambda_stream-1.0.9/pyproject.toml
+-rw-r--r--   0        0        0     1550 2023-03-01 05:05:26.601549 aws_lambda_stream-1.0.9/setup.py
+-rw-r--r--   0        0        0     1287 2023-03-01 05:05:26.601696 aws_lambda_stream-1.0.9/PKG-INFO
```

### Comparing `aws_lambda_stream-1.0.8/LICENSE` & `aws_lambda_stream-1.0.9/LICENSE`

 * *Files identical despite different names*

### Comparing `aws_lambda_stream-1.0.8/aws_lambda_stream/__init__.py` & `aws_lambda_stream-1.0.9/aws_lambda_stream/__init__.py`

 * *Files identical despite different names*

### Comparing `aws_lambda_stream-1.0.8/aws_lambda_stream/connectors/dynamodb.py` & `aws_lambda_stream-1.0.9/aws_lambda_stream/connectors/dynamodb.py`

 * *Files identical despite different names*

### Comparing `aws_lambda_stream-1.0.8/aws_lambda_stream/connectors/elasticsearch.py` & `aws_lambda_stream-1.0.9/aws_lambda_stream/connectors/elasticsearch.py`

 * *Files identical despite different names*

### Comparing `aws_lambda_stream-1.0.8/aws_lambda_stream/connectors/s3.py` & `aws_lambda_stream-1.0.9/aws_lambda_stream/connectors/s3.py`

 * *Files identical despite different names*

### Comparing `aws_lambda_stream-1.0.8/aws_lambda_stream/connectors/sns.py` & `aws_lambda_stream-1.0.9/aws_lambda_stream/connectors/sns.py`

 * *Files identical despite different names*

### Comparing `aws_lambda_stream-1.0.8/aws_lambda_stream/connectors/sqs.py` & `aws_lambda_stream-1.0.9/aws_lambda_stream/connectors/sqs.py`

 * *Files identical despite different names*

### Comparing `aws_lambda_stream-1.0.8/aws_lambda_stream/events/dynamodb.py` & `aws_lambda_stream-1.0.9/aws_lambda_stream/events/dynamodb.py`

 * *Files identical despite different names*

### Comparing `aws_lambda_stream-1.0.8/aws_lambda_stream/events/kinesis.py` & `aws_lambda_stream-1.0.9/aws_lambda_stream/events/kinesis.py`

 * *Files identical despite different names*

### Comparing `aws_lambda_stream-1.0.8/aws_lambda_stream/events/s3.py` & `aws_lambda_stream-1.0.9/aws_lambda_stream/events/s3.py`

 * *Files identical despite different names*

### Comparing `aws_lambda_stream-1.0.8/aws_lambda_stream/events/sns.py` & `aws_lambda_stream-1.0.9/aws_lambda_stream/events/sns.py`

 * *Files identical despite different names*

### Comparing `aws_lambda_stream-1.0.8/aws_lambda_stream/events/sqs.py` & `aws_lambda_stream-1.0.9/aws_lambda_stream/events/sqs.py`

 * *Files identical despite different names*

### Comparing `aws_lambda_stream-1.0.8/aws_lambda_stream/filters/event_type.py` & `aws_lambda_stream-1.0.9/aws_lambda_stream/filters/event_type.py`

 * *Files identical despite different names*

### Comparing `aws_lambda_stream-1.0.8/aws_lambda_stream/filters/latch.py` & `aws_lambda_stream-1.0.9/aws_lambda_stream/filters/latch.py`

 * *Files identical despite different names*

### Comparing `aws_lambda_stream-1.0.8/aws_lambda_stream/flavors/cdc.py` & `aws_lambda_stream-1.0.9/aws_lambda_stream/flavors/cdc.py`

 * *Files identical despite different names*

### Comparing `aws_lambda_stream-1.0.8/aws_lambda_stream/flavors/collect.py` & `aws_lambda_stream-1.0.9/aws_lambda_stream/flavors/collect.py`

 * *Files identical despite different names*

### Comparing `aws_lambda_stream-1.0.8/aws_lambda_stream/flavors/correlate.py` & `aws_lambda_stream-1.0.9/aws_lambda_stream/flavors/correlate.py`

 * *Files identical despite different names*

### Comparing `aws_lambda_stream-1.0.8/aws_lambda_stream/flavors/elasticsearch.py` & `aws_lambda_stream-1.0.9/aws_lambda_stream/flavors/elasticsearch.py`

 * *Files identical despite different names*

### Comparing `aws_lambda_stream-1.0.8/aws_lambda_stream/flavors/evaluate.py` & `aws_lambda_stream-1.0.9/aws_lambda_stream/flavors/evaluate.py`

 * *Files identical despite different names*

### Comparing `aws_lambda_stream-1.0.8/aws_lambda_stream/flavors/materialize.py` & `aws_lambda_stream-1.0.9/aws_lambda_stream/flavors/materialize.py`

 * *Files identical despite different names*

### Comparing `aws_lambda_stream-1.0.8/aws_lambda_stream/flavors/s3.py` & `aws_lambda_stream-1.0.9/aws_lambda_stream/flavors/s3.py`

 * *Files identical despite different names*

### Comparing `aws_lambda_stream-1.0.8/aws_lambda_stream/flavors/sns.py` & `aws_lambda_stream-1.0.9/aws_lambda_stream/flavors/sns.py`

 * *Files identical despite different names*

### Comparing `aws_lambda_stream-1.0.8/aws_lambda_stream/flavors/task.py` & `aws_lambda_stream-1.0.9/aws_lambda_stream/flavors/task.py`

 * *Files identical despite different names*

### Comparing `aws_lambda_stream-1.0.8/aws_lambda_stream/pipelines/__init__.py` & `aws_lambda_stream-1.0.9/aws_lambda_stream/pipelines/__init__.py`

 * *Files identical despite different names*

### Comparing `aws_lambda_stream-1.0.8/aws_lambda_stream/repositories/__init__.py` & `aws_lambda_stream-1.0.9/aws_lambda_stream/repositories/__init__.py`

 * *Files identical despite different names*

### Comparing `aws_lambda_stream-1.0.8/aws_lambda_stream/utils/dynamodb.py` & `aws_lambda_stream-1.0.9/aws_lambda_stream/utils/dynamodb.py`

 * *Files identical despite different names*

### Comparing `aws_lambda_stream-1.0.8/aws_lambda_stream/utils/elasticsearch.py` & `aws_lambda_stream-1.0.9/aws_lambda_stream/utils/elasticsearch.py`

 * *Files identical despite different names*

### Comparing `aws_lambda_stream-1.0.8/aws_lambda_stream/utils/eventbridge.py` & `aws_lambda_stream-1.0.9/aws_lambda_stream/utils/eventbridge.py`

 * *Files identical despite different names*

### Comparing `aws_lambda_stream-1.0.8/aws_lambda_stream/utils/faults.py` & `aws_lambda_stream-1.0.9/aws_lambda_stream/utils/faults.py`

 * *Files identical despite different names*

### Comparing `aws_lambda_stream-1.0.8/aws_lambda_stream/utils/lambda_.py` & `aws_lambda_stream-1.0.9/aws_lambda_stream/utils/lambda_.py`

 * *Files identical despite different names*

### Comparing `aws_lambda_stream-1.0.8/aws_lambda_stream/utils/logger.py` & `aws_lambda_stream-1.0.9/aws_lambda_stream/utils/logger.py`

 * *Files identical despite different names*

### Comparing `aws_lambda_stream-1.0.8/aws_lambda_stream/utils/operators.py` & `aws_lambda_stream-1.0.9/aws_lambda_stream/utils/operators.py`

 * *Files identical despite different names*

### Comparing `aws_lambda_stream-1.0.8/aws_lambda_stream/utils/sns.py` & `aws_lambda_stream-1.0.9/aws_lambda_stream/utils/sns.py`

 * *Files identical despite different names*

### Comparing `aws_lambda_stream-1.0.8/aws_lambda_stream/utils/split.py` & `aws_lambda_stream-1.0.9/aws_lambda_stream/utils/split.py`

 * *Files identical despite different names*

### Comparing `aws_lambda_stream-1.0.8/aws_lambda_stream/utils/tags.py` & `aws_lambda_stream-1.0.9/aws_lambda_stream/utils/tags.py`

 * *Files identical despite different names*

### Comparing `aws_lambda_stream-1.0.8/pyproject.toml` & `aws_lambda_stream-1.0.9/pyproject.toml`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 [tool.poetry]
 name = "aws_lambda_stream"
-version = "1.0.8"
+version = "1.0.9"
 description = "Create stream processors with AWS Lambda functions"
 authors = ["Alejandro Hernández <clandro89@gmail.com>"]
 repository="https://github.com/clandro89/aws-lambda-stream"
 readme = "README.md"
 
 [tool.poetry.dependencies]
 python = "^3.8"
```

### Comparing `aws_lambda_stream-1.0.8/setup.py` & `aws_lambda_stream-1.0.9/setup.py`

 * *Files 0% similar despite different names*

```diff
@@ -19,15 +19,15 @@
  'boto3>=1.24.66,<2.0.0',
  'pydash>=5.1.1,<6.0.0',
  'reactivex>=4.0.4,<5.0.0',
  'requests-aws4auth>=1.1.2,<2.0.0']
 
 setup_kwargs = {
     'name': 'aws-lambda-stream',
-    'version': '1.0.8',
+    'version': '1.0.9',
     'description': 'Create stream processors with AWS Lambda functions',
     'long_description': '# aws-lambda-stream\n\nThis a python version of [aws-lambda-stream](https://github.com/jgilbert01/aws-lambda-stream) using [ReactiveX](https://github.com/ReactiveX/RxPY)\n\n\n## Installation\nWith `pip` installed, run:\n\n````\npip install aws-lambda-stream\n````\n\nWith `poetry`, run:\n````\npoetry add aws-lambda-stream\n````\n\n## Credits\n- [aws-lambda-stream](https://github.com/jgilbert01/aws-lambda-stream)\n\n## License\nThis library is licensed under the MIT License. See the LICENSE file.',
     'author': 'Alejandro Hernández',
     'author_email': 'clandro89@gmail.com',
     'maintainer': None,
     'maintainer_email': None,
     'url': 'https://github.com/clandro89/aws-lambda-stream',
```

### Comparing `aws_lambda_stream-1.0.8/PKG-INFO` & `aws_lambda_stream-1.0.9/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: aws-lambda-stream
-Version: 1.0.8
+Version: 1.0.9
 Summary: Create stream processors with AWS Lambda functions
 Home-page: https://github.com/clandro89/aws-lambda-stream
 Author: Alejandro Hernández
 Author-email: clandro89@gmail.com
 Requires-Python: >=3.8,<4.0
 Classifier: Programming Language :: Python :: 3
 Classifier: Programming Language :: Python :: 3.10
```

