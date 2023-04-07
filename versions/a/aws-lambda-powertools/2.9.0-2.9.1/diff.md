# Comparing `tmp/aws_lambda_powertools-2.9.0.tar.gz` & `tmp/aws_lambda_powertools-2.9.1.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "aws_lambda_powertools-2.9.0.tar", max compression
+gzip compressed data, was "aws_lambda_powertools-2.9.1.tar", max compression
```

## Comparing `aws_lambda_powertools-2.9.0.tar` & `aws_lambda_powertools-2.9.1.tar`

### file list

```diff
@@ -1,159 +1,158 @@
--rw-r--r--   0        0        0      951 2023-02-21 11:01:40.237963 aws_lambda_powertools-2.9.0/LICENSE
--rw-r--r--   0        0        0     6118 2023-02-21 11:01:40.237963 aws_lambda_powertools-2.9.0/README.md
--rw-r--r--   0        0        0    10200 2023-02-21 11:01:40.237963 aws_lambda_powertools-2.9.0/THIRD-PARTY-LICENSES
--rw-r--r--   0        0        0      447 2023-02-21 11:01:40.237963 aws_lambda_powertools-2.9.0/aws_lambda_powertools/__init__.py
--rw-r--r--   0        0        0      521 2023-02-21 11:01:40.237963 aws_lambda_powertools-2.9.0/aws_lambda_powertools/event_handler/__init__.py
--rw-r--r--   0        0        0    32035 2023-02-21 11:01:40.237963 aws_lambda_powertools-2.9.0/aws_lambda_powertools/event_handler/api_gateway.py
--rw-r--r--   0        0        0     6745 2023-02-21 11:01:40.237963 aws_lambda_powertools-2.9.0/aws_lambda_powertools/event_handler/appsync.py
--rw-r--r--   0        0        0      163 2023-02-21 11:01:40.237963 aws_lambda_powertools-2.9.0/aws_lambda_powertools/event_handler/content_types.py
--rw-r--r--   0        0        0     1160 2023-02-21 11:01:40.237963 aws_lambda_powertools-2.9.0/aws_lambda_powertools/event_handler/exceptions.py
--rw-r--r--   0        0        0     1686 2023-02-21 11:01:40.241963 aws_lambda_powertools-2.9.0/aws_lambda_powertools/event_handler/lambda_function_url.py
--rw-r--r--   0        0        0      867 2023-02-21 11:01:40.241963 aws_lambda_powertools-2.9.0/aws_lambda_powertools/event_handler/router.py
--rw-r--r--   0        0        0      163 2023-02-21 11:01:40.241963 aws_lambda_powertools-2.9.0/aws_lambda_powertools/exceptions/__init__.py
--rw-r--r--   0        0        0       72 2023-02-21 11:01:40.241963 aws_lambda_powertools-2.9.0/aws_lambda_powertools/logging/__init__.py
--rw-r--r--   0        0        0      369 2023-02-21 11:01:40.241963 aws_lambda_powertools-2.9.0/aws_lambda_powertools/logging/correlation_paths.py
--rw-r--r--   0        0        0       58 2023-02-21 11:01:40.241963 aws_lambda_powertools-2.9.0/aws_lambda_powertools/logging/exceptions.py
--rw-r--r--   0        0        0      491 2023-02-21 11:01:40.241963 aws_lambda_powertools-2.9.0/aws_lambda_powertools/logging/filters.py
--rw-r--r--   0        0        0    12654 2023-02-21 11:01:40.241963 aws_lambda_powertools-2.9.0/aws_lambda_powertools/logging/formatter.py
--rw-r--r--   0        0        0     1736 2023-02-21 11:01:40.241963 aws_lambda_powertools-2.9.0/aws_lambda_powertools/logging/lambda_context.py
--rw-r--r--   0        0        0    28767 2023-02-21 11:01:40.241963 aws_lambda_powertools-2.9.0/aws_lambda_powertools/logging/logger.py
--rw-r--r--   0        0        0     3543 2023-02-21 11:01:40.241963 aws_lambda_powertools-2.9.0/aws_lambda_powertools/logging/utils.py
--rw-r--r--   0        0        0      524 2023-02-21 11:01:40.241963 aws_lambda_powertools-2.9.0/aws_lambda_powertools/metrics/__init__.py
--rw-r--r--   0        0        0    22062 2023-02-21 11:01:40.241963 aws_lambda_powertools-2.9.0/aws_lambda_powertools/metrics/base.py
--rw-r--r--   0        0        0      418 2023-02-21 11:01:40.241963 aws_lambda_powertools-2.9.0/aws_lambda_powertools/metrics/exceptions.py
--rw-r--r--   0        0        0      136 2023-02-21 11:01:40.241963 aws_lambda_powertools-2.9.0/aws_lambda_powertools/metrics/metric.py
--rw-r--r--   0        0        0     4693 2023-02-21 11:01:40.241963 aws_lambda_powertools-2.9.0/aws_lambda_powertools/metrics/metrics.py
--rw-r--r--   0        0        0      166 2023-02-21 11:01:40.241963 aws_lambda_powertools-2.9.0/aws_lambda_powertools/metrics/types.py
--rw-r--r--   0        0        0      127 2023-02-21 11:01:40.241963 aws_lambda_powertools-2.9.0/aws_lambda_powertools/middleware_factory/__init__.py
--rw-r--r--   0        0        0      106 2023-02-21 11:01:40.241963 aws_lambda_powertools-2.9.0/aws_lambda_powertools/middleware_factory/exceptions.py
--rw-r--r--   0        0        0     5112 2023-02-21 11:01:40.241963 aws_lambda_powertools-2.9.0/aws_lambda_powertools/middleware_factory/factory.py
--rw-r--r--   0        0        0      750 2023-02-21 11:01:40.241963 aws_lambda_powertools-2.9.0/aws_lambda_powertools/package_logger.py
--rw-r--r--   0        0        0        0 2023-02-21 11:01:40.241963 aws_lambda_powertools-2.9.0/aws_lambda_powertools/py.typed
--rw-r--r--   0        0        0        0 2023-02-21 11:01:40.241963 aws_lambda_powertools-2.9.0/aws_lambda_powertools/shared/__init__.py
--rw-r--r--   0        0        0      929 2023-02-21 11:01:40.241963 aws_lambda_powertools-2.9.0/aws_lambda_powertools/shared/cache_dict.py
--rw-r--r--   0        0        0     1209 2023-02-21 11:01:40.241963 aws_lambda_powertools-2.9.0/aws_lambda_powertools/shared/constants.py
--rw-r--r--   0        0        0     3832 2023-02-21 11:01:40.241963 aws_lambda_powertools-2.9.0/aws_lambda_powertools/shared/cookies.py
--rw-r--r--   0        0        0     4703 2023-02-21 11:01:40.241963 aws_lambda_powertools-2.9.0/aws_lambda_powertools/shared/functions.py
--rw-r--r--   0        0        0     5372 2023-02-21 11:01:40.241963 aws_lambda_powertools-2.9.0/aws_lambda_powertools/shared/headers_serializer.py
--rw-r--r--   0        0        0      406 2023-02-21 11:01:40.241963 aws_lambda_powertools-2.9.0/aws_lambda_powertools/shared/json_encoder.py
--rw-r--r--   0        0        0     2035 2023-02-21 11:01:40.241963 aws_lambda_powertools-2.9.0/aws_lambda_powertools/shared/lazy_import.py
--rw-r--r--   0        0        0      275 2023-02-21 11:01:40.241963 aws_lambda_powertools-2.9.0/aws_lambda_powertools/shared/types.py
--rw-r--r--   0        0        0      143 2023-02-21 11:01:40.241963 aws_lambda_powertools-2.9.0/aws_lambda_powertools/tracing/__init__.py
--rw-r--r--   0        0        0     4424 2023-02-21 11:01:40.241963 aws_lambda_powertools-2.9.0/aws_lambda_powertools/tracing/base.py
--rw-r--r--   0        0        0      492 2023-02-21 11:01:40.241963 aws_lambda_powertools-2.9.0/aws_lambda_powertools/tracing/extensions.py
--rw-r--r--   0        0        0    30676 2023-02-21 11:01:40.241963 aws_lambda_powertools-2.9.0/aws_lambda_powertools/tracing/tracer.py
--rw-r--r--   0        0        0       64 2023-02-21 11:01:40.241963 aws_lambda_powertools-2.9.0/aws_lambda_powertools/utilities/__init__.py
--rw-r--r--   0        0        0      897 2023-02-21 11:01:40.241963 aws_lambda_powertools-2.9.0/aws_lambda_powertools/utilities/batch/__init__.py
--rw-r--r--   0        0        0    23738 2023-02-21 11:01:40.241963 aws_lambda_powertools-2.9.0/aws_lambda_powertools/utilities/batch/base.py
--rw-r--r--   0        0        0     1240 2023-02-21 11:01:40.241963 aws_lambda_powertools-2.9.0/aws_lambda_powertools/utilities/batch/exceptions.py
--rw-r--r--   0        0        0     3194 2023-02-21 11:01:40.241963 aws_lambda_powertools-2.9.0/aws_lambda_powertools/utilities/batch/sqs_fifo_partial_processor.py
--rw-r--r--   0        0        0      947 2023-02-21 11:01:40.241963 aws_lambda_powertools-2.9.0/aws_lambda_powertools/utilities/batch/types.py
--rw-r--r--   0        0        0     1490 2023-02-21 11:01:40.241963 aws_lambda_powertools-2.9.0/aws_lambda_powertools/utilities/data_classes/__init__.py
--rw-r--r--   0        0        0     3721 2023-02-21 11:01:40.241963 aws_lambda_powertools-2.9.0/aws_lambda_powertools/utilities/data_classes/active_mq_event.py
--rw-r--r--   0        0        0     1632 2023-02-21 11:01:40.241963 aws_lambda_powertools-2.9.0/aws_lambda_powertools/utilities/data_classes/alb_event.py
--rw-r--r--   0        0        0    18824 2023-02-21 11:01:40.241963 aws_lambda_powertools-2.9.0/aws_lambda_powertools/utilities/data_classes/api_gateway_authorizer_event.py
--rw-r--r--   0        0        0     8783 2023-02-21 11:01:40.241963 aws_lambda_powertools-2.9.0/aws_lambda_powertools/utilities/data_classes/api_gateway_proxy_event.py
--rw-r--r--   0        0        0        0 2023-02-21 11:01:40.241963 aws_lambda_powertools-2.9.0/aws_lambda_powertools/utilities/data_classes/appsync/__init__.py
--rw-r--r--   0        0        0     2662 2023-02-21 11:01:40.241963 aws_lambda_powertools-2.9.0/aws_lambda_powertools/utilities/data_classes/appsync/scalar_types_utils.py
--rw-r--r--   0        0        0     3927 2023-02-21 11:01:40.241963 aws_lambda_powertools-2.9.0/aws_lambda_powertools/utilities/data_classes/appsync_authorizer_event.py
--rw-r--r--   0        0        0     7838 2023-02-21 11:01:40.241963 aws_lambda_powertools-2.9.0/aws_lambda_powertools/utilities/data_classes/appsync_resolver_event.py
--rw-r--r--   0        0        0     4207 2023-02-21 11:01:40.241963 aws_lambda_powertools-2.9.0/aws_lambda_powertools/utilities/data_classes/cloud_watch_custom_widget_event.py
--rw-r--r--   0        0        0     3322 2023-02-21 11:01:40.241963 aws_lambda_powertools-2.9.0/aws_lambda_powertools/utilities/data_classes/cloud_watch_logs_event.py
--rw-r--r--   0        0        0     7206 2023-02-21 11:01:40.241963 aws_lambda_powertools-2.9.0/aws_lambda_powertools/utilities/data_classes/code_pipeline_job_event.py
--rw-r--r--   0        0        0    32633 2023-02-21 11:01:40.241963 aws_lambda_powertools-2.9.0/aws_lambda_powertools/utilities/data_classes/cognito_user_pool_event.py
--rw-r--r--   0        0        0    13637 2023-02-21 11:01:40.241963 aws_lambda_powertools-2.9.0/aws_lambda_powertools/utilities/data_classes/common.py
--rw-r--r--   0        0        0     5484 2023-02-21 11:01:40.241963 aws_lambda_powertools-2.9.0/aws_lambda_powertools/utilities/data_classes/connect_contact_flow_event.py
--rw-r--r--   0        0        0     9418 2023-02-21 11:01:40.241963 aws_lambda_powertools-2.9.0/aws_lambda_powertools/utilities/data_classes/dynamo_db_stream_event.py
--rw-r--r--   0        0        0     2423 2023-02-21 11:01:40.241963 aws_lambda_powertools-2.9.0/aws_lambda_powertools/utilities/data_classes/event_bridge_event.py
--rw-r--r--   0        0        0     1094 2023-02-21 11:01:40.241963 aws_lambda_powertools-2.9.0/aws_lambda_powertools/utilities/data_classes/event_source.py
--rw-r--r--   0        0        0     3847 2023-02-21 11:01:40.241963 aws_lambda_powertools-2.9.0/aws_lambda_powertools/utilities/data_classes/kafka_event.py
--rw-r--r--   0        0        0     3847 2023-02-21 11:01:40.241963 aws_lambda_powertools-2.9.0/aws_lambda_powertools/utilities/data_classes/kinesis_firehose_event.py
--rw-r--r--   0        0        0     3913 2023-02-21 11:01:40.241963 aws_lambda_powertools-2.9.0/aws_lambda_powertools/utilities/data_classes/kinesis_stream_event.py
--rw-r--r--   0        0        0      633 2023-02-21 11:01:40.241963 aws_lambda_powertools-2.9.0/aws_lambda_powertools/utilities/data_classes/lambda_function_url_event.py
--rw-r--r--   0        0        0     3005 2023-02-21 11:01:40.241963 aws_lambda_powertools-2.9.0/aws_lambda_powertools/utilities/data_classes/rabbit_mq_event.py
--rw-r--r--   0        0        0     5942 2023-02-21 11:01:40.241963 aws_lambda_powertools-2.9.0/aws_lambda_powertools/utilities/data_classes/s3_event.py
--rw-r--r--   0        0        0    12949 2023-02-21 11:01:40.241963 aws_lambda_powertools-2.9.0/aws_lambda_powertools/utilities/data_classes/s3_object_event.py
--rw-r--r--   0        0        0     8846 2023-02-21 11:01:40.241963 aws_lambda_powertools-2.9.0/aws_lambda_powertools/utilities/data_classes/ses_event.py
--rw-r--r--   0        0        0     3893 2023-02-21 11:01:40.241963 aws_lambda_powertools-2.9.0/aws_lambda_powertools/utilities/data_classes/sns_event.py
--rw-r--r--   0        0        0     5257 2023-02-21 11:01:40.241963 aws_lambda_powertools-2.9.0/aws_lambda_powertools/utilities/data_classes/sqs_event.py
--rw-r--r--   0        0        0      393 2023-02-21 11:01:40.241963 aws_lambda_powertools-2.9.0/aws_lambda_powertools/utilities/feature_flags/__init__.py
--rw-r--r--   0        0        0     4032 2023-02-21 11:01:40.241963 aws_lambda_powertools-2.9.0/aws_lambda_powertools/utilities/feature_flags/appconfig.py
--rw-r--r--   0        0        0     1745 2023-02-21 11:01:40.241963 aws_lambda_powertools-2.9.0/aws_lambda_powertools/utilities/feature_flags/base.py
--rw-r--r--   0        0        0      447 2023-02-21 11:01:40.241963 aws_lambda_powertools-2.9.0/aws_lambda_powertools/utilities/feature_flags/exceptions.py
--rw-r--r--   0        0        0    13570 2023-02-21 11:01:40.241963 aws_lambda_powertools-2.9.0/aws_lambda_powertools/utilities/feature_flags/feature_flags.py
--rw-r--r--   0        0        0    18840 2023-02-21 11:01:40.245963 aws_lambda_powertools-2.9.0/aws_lambda_powertools/utilities/feature_flags/schema.py
--rw-r--r--   0        0        0     4081 2023-02-21 11:01:40.245963 aws_lambda_powertools-2.9.0/aws_lambda_powertools/utilities/feature_flags/time_conditions.py
--rw-r--r--   0        0        0      473 2023-02-21 11:01:40.245963 aws_lambda_powertools-2.9.0/aws_lambda_powertools/utilities/idempotency/__init__.py
--rw-r--r--   0        0        0     8808 2023-02-21 11:01:40.245963 aws_lambda_powertools-2.9.0/aws_lambda_powertools/utilities/idempotency/base.py
--rw-r--r--   0        0        0     2440 2023-02-21 11:01:40.245963 aws_lambda_powertools-2.9.0/aws_lambda_powertools/utilities/idempotency/config.py
--rw-r--r--   0        0        0     1683 2023-02-21 11:01:40.245963 aws_lambda_powertools-2.9.0/aws_lambda_powertools/utilities/idempotency/exceptions.py
--rw-r--r--   0        0        0     4930 2023-02-21 11:01:40.245963 aws_lambda_powertools-2.9.0/aws_lambda_powertools/utilities/idempotency/idempotency.py
--rw-r--r--   0        0        0        0 2023-02-21 11:01:40.245963 aws_lambda_powertools-2.9.0/aws_lambda_powertools/utilities/idempotency/persistence/__init__.py
--rw-r--r--   0        0        0    16325 2023-02-21 11:01:40.245963 aws_lambda_powertools-2.9.0/aws_lambda_powertools/utilities/idempotency/persistence/base.py
--rw-r--r--   0        0        0    10506 2023-02-21 11:01:40.245963 aws_lambda_powertools-2.9.0/aws_lambda_powertools/utilities/idempotency/persistence/dynamodb.py
--rw-r--r--   0        0        0     2682 2023-02-21 11:01:40.245963 aws_lambda_powertools-2.9.0/aws_lambda_powertools/utilities/jmespath_utils/__init__.py
--rw-r--r--   0        0        0      412 2023-02-21 11:01:40.245963 aws_lambda_powertools-2.9.0/aws_lambda_powertools/utilities/jmespath_utils/envelopes.py
--rw-r--r--   0        0        0      730 2023-02-21 11:01:40.245963 aws_lambda_powertools-2.9.0/aws_lambda_powertools/utilities/parameters/__init__.py
--rw-r--r--   0        0        0     6872 2023-02-21 11:01:40.245963 aws_lambda_powertools-2.9.0/aws_lambda_powertools/utilities/parameters/appconfig.py
--rw-r--r--   0        0        0    14331 2023-02-21 11:01:40.245963 aws_lambda_powertools-2.9.0/aws_lambda_powertools/utilities/parameters/base.py
--rw-r--r--   0        0        0     8256 2023-02-21 11:01:40.245963 aws_lambda_powertools-2.9.0/aws_lambda_powertools/utilities/parameters/dynamodb.py
--rw-r--r--   0        0        0      253 2023-02-21 11:01:40.245963 aws_lambda_powertools-2.9.0/aws_lambda_powertools/utilities/parameters/exceptions.py
--rw-r--r--   0        0        0     5432 2023-02-21 11:01:40.245963 aws_lambda_powertools-2.9.0/aws_lambda_powertools/utilities/parameters/secrets.py
--rw-r--r--   0        0        0    28878 2023-02-21 11:01:40.245963 aws_lambda_powertools-2.9.0/aws_lambda_powertools/utilities/parameters/ssm.py
--rw-r--r--   0        0        0       98 2023-02-21 11:01:40.245963 aws_lambda_powertools-2.9.0/aws_lambda_powertools/utilities/parameters/types.py
--rw-r--r--   0        0        0      397 2023-02-21 11:01:40.245963 aws_lambda_powertools-2.9.0/aws_lambda_powertools/utilities/parser/__init__.py
--rw-r--r--   0        0        0      870 2023-02-21 11:01:40.245963 aws_lambda_powertools-2.9.0/aws_lambda_powertools/utilities/parser/envelopes/__init__.py
--rw-r--r--   0        0        0     1115 2023-02-21 11:01:40.245963 aws_lambda_powertools-2.9.0/aws_lambda_powertools/utilities/parser/envelopes/apigw.py
--rw-r--r--   0        0        0     1131 2023-02-21 11:01:40.245963 aws_lambda_powertools-2.9.0/aws_lambda_powertools/utilities/parser/envelopes/apigwv2.py
--rw-r--r--   0        0        0     1966 2023-02-21 11:01:40.245963 aws_lambda_powertools-2.9.0/aws_lambda_powertools/utilities/parser/envelopes/base.py
--rw-r--r--   0        0        0     1444 2023-02-21 11:01:40.245963 aws_lambda_powertools-2.9.0/aws_lambda_powertools/utilities/parser/envelopes/cloudwatch.py
--rw-r--r--   0        0        0     1577 2023-02-21 11:01:40.245963 aws_lambda_powertools-2.9.0/aws_lambda_powertools/utilities/parser/envelopes/dynamodb.py
--rw-r--r--   0        0        0     1084 2023-02-21 11:01:40.245963 aws_lambda_powertools-2.9.0/aws_lambda_powertools/utilities/parser/envelopes/event_bridge.py
--rw-r--r--   0        0        0     1722 2023-02-21 11:01:40.245963 aws_lambda_powertools-2.9.0/aws_lambda_powertools/utilities/parser/envelopes/kafka.py
--rw-r--r--   0        0        0     1740 2023-02-21 11:01:40.245963 aws_lambda_powertools-2.9.0/aws_lambda_powertools/utilities/parser/envelopes/kinesis.py
--rw-r--r--   0        0        0     1817 2023-02-21 11:01:40.245963 aws_lambda_powertools-2.9.0/aws_lambda_powertools/utilities/parser/envelopes/kinesis_firehose.py
--rw-r--r--   0        0        0     1126 2023-02-21 11:01:40.245963 aws_lambda_powertools-2.9.0/aws_lambda_powertools/utilities/parser/envelopes/lambda_function_url.py
--rw-r--r--   0        0        0     2830 2023-02-21 11:01:40.245963 aws_lambda_powertools-2.9.0/aws_lambda_powertools/utilities/parser/envelopes/sns.py
--rw-r--r--   0        0        0     1366 2023-02-21 11:01:40.245963 aws_lambda_powertools-2.9.0/aws_lambda_powertools/utilities/parser/envelopes/sqs.py
--rw-r--r--   0        0        0      207 2023-02-21 11:01:40.245963 aws_lambda_powertools-2.9.0/aws_lambda_powertools/utilities/parser/exceptions.py
--rw-r--r--   0        0        0     3479 2023-02-21 11:01:40.245963 aws_lambda_powertools-2.9.0/aws_lambda_powertools/utilities/parser/models/__init__.py
--rw-r--r--   0        0        0      439 2023-02-21 11:01:40.245963 aws_lambda_powertools-2.9.0/aws_lambda_powertools/utilities/parser/models/alb.py
--rw-r--r--   0        0        0     2871 2023-02-21 11:01:40.245963 aws_lambda_powertools-2.9.0/aws_lambda_powertools/utilities/parser/models/apigw.py
--rw-r--r--   0        0        0     1890 2023-02-21 11:01:40.245963 aws_lambda_powertools-2.9.0/aws_lambda_powertools/utilities/parser/models/apigwv2.py
--rw-r--r--   0        0        0     1245 2023-02-21 11:01:40.245963 aws_lambda_powertools-2.9.0/aws_lambda_powertools/utilities/parser/models/cloudwatch.py
--rw-r--r--   0        0        0     1855 2023-02-21 11:01:40.245963 aws_lambda_powertools-2.9.0/aws_lambda_powertools/utilities/parser/models/dynamodb.py
--rw-r--r--   0        0        0      480 2023-02-21 11:01:40.245963 aws_lambda_powertools-2.9.0/aws_lambda_powertools/utilities/parser/models/event_bridge.py
--rw-r--r--   0        0        0     1839 2023-02-21 11:01:40.245963 aws_lambda_powertools-2.9.0/aws_lambda_powertools/utilities/parser/models/kafka.py
--rw-r--r--   0        0        0     1836 2023-02-21 11:01:40.245963 aws_lambda_powertools-2.9.0/aws_lambda_powertools/utilities/parser/models/kinesis.py
--rw-r--r--   0        0        0      926 2023-02-21 11:01:40.245963 aws_lambda_powertools-2.9.0/aws_lambda_powertools/utilities/parser/models/kinesis_firehose.py
--rw-r--r--   0        0        0      611 2023-02-21 11:01:40.245963 aws_lambda_powertools-2.9.0/aws_lambda_powertools/utilities/parser/models/lambda_function_url.py
--rw-r--r--   0        0        0     2078 2023-02-21 11:01:40.245963 aws_lambda_powertools-2.9.0/aws_lambda_powertools/utilities/parser/models/s3.py
--rw-r--r--   0        0        0     1256 2023-02-21 11:01:40.245963 aws_lambda_powertools-2.9.0/aws_lambda_powertools/utilities/parser/models/s3_object_event.py
--rw-r--r--   0        0        0     1573 2023-02-21 11:01:40.245963 aws_lambda_powertools-2.9.0/aws_lambda_powertools/utilities/parser/models/ses.py
--rw-r--r--   0        0        0     1663 2023-02-21 11:01:40.245963 aws_lambda_powertools-2.9.0/aws_lambda_powertools/utilities/parser/models/sns.py
--rw-r--r--   0        0        0     2627 2023-02-21 11:01:40.245963 aws_lambda_powertools-2.9.0/aws_lambda_powertools/utilities/parser/models/sqs.py
--rw-r--r--   0        0        0     5317 2023-02-21 11:01:40.245963 aws_lambda_powertools-2.9.0/aws_lambda_powertools/utilities/parser/parser.py
--rw-r--r--   0        0        0      530 2023-02-21 11:01:40.245963 aws_lambda_powertools-2.9.0/aws_lambda_powertools/utilities/parser/pydantic.py
--rw-r--r--   0        0        0      466 2023-02-21 11:01:40.245963 aws_lambda_powertools-2.9.0/aws_lambda_powertools/utilities/parser/types.py
--rw-r--r--   0        0        0       97 2023-02-21 11:01:40.245963 aws_lambda_powertools-2.9.0/aws_lambda_powertools/utilities/streaming/__init__.py
--rw-r--r--   0        0        0     6028 2023-02-21 11:01:40.245963 aws_lambda_powertools-2.9.0/aws_lambda_powertools/utilities/streaming/_s3_seekable_io.py
--rw-r--r--   0        0        0     8150 2023-02-21 11:01:40.245963 aws_lambda_powertools-2.9.0/aws_lambda_powertools/utilities/streaming/compat.py
--rw-r--r--   0        0        0     9386 2023-02-21 11:01:40.245963 aws_lambda_powertools-2.9.0/aws_lambda_powertools/utilities/streaming/s3_object.py
--rw-r--r--   0        0        0      430 2023-02-21 11:01:40.245963 aws_lambda_powertools-2.9.0/aws_lambda_powertools/utilities/streaming/transformations/__init__.py
--rw-r--r--   0        0        0      846 2023-02-21 11:01:40.245963 aws_lambda_powertools-2.9.0/aws_lambda_powertools/utilities/streaming/transformations/base.py
--rw-r--r--   0        0        0     2312 2023-02-21 11:01:40.245963 aws_lambda_powertools-2.9.0/aws_lambda_powertools/utilities/streaming/transformations/csv.py
--rw-r--r--   0        0        0      886 2023-02-21 11:01:40.245963 aws_lambda_powertools-2.9.0/aws_lambda_powertools/utilities/streaming/transformations/gzip.py
--rw-r--r--   0        0        0     2217 2023-02-21 11:01:40.245963 aws_lambda_powertools-2.9.0/aws_lambda_powertools/utilities/streaming/transformations/zip.py
--rw-r--r--   0        0        0      142 2023-02-21 11:01:40.245963 aws_lambda_powertools-2.9.0/aws_lambda_powertools/utilities/typing/__init__.py
--rw-r--r--   0        0        0      808 2023-02-21 11:01:40.245963 aws_lambda_powertools-2.9.0/aws_lambda_powertools/utilities/typing/lambda_client_context.py
--rw-r--r--   0        0        0      730 2023-02-21 11:01:40.245963 aws_lambda_powertools-2.9.0/aws_lambda_powertools/utilities/typing/lambda_client_context_mobile_client.py
--rw-r--r--   0        0        0      556 2023-02-21 11:01:40.245963 aws_lambda_powertools-2.9.0/aws_lambda_powertools/utilities/typing/lambda_cognito_identity.py
--rw-r--r--   0        0        0     2682 2023-02-21 11:01:40.245963 aws_lambda_powertools-2.9.0/aws_lambda_powertools/utilities/typing/lambda_context.py
--rw-r--r--   0        0        0      398 2023-02-21 11:01:40.245963 aws_lambda_powertools-2.9.0/aws_lambda_powertools/utilities/validation/__init__.py
--rw-r--r--   0        0        0     1608 2023-02-21 11:01:40.245963 aws_lambda_powertools-2.9.0/aws_lambda_powertools/utilities/validation/base.py
--rw-r--r--   0        0        0      438 2023-02-21 11:01:40.245963 aws_lambda_powertools-2.9.0/aws_lambda_powertools/utilities/validation/envelopes.py
--rw-r--r--   0        0        0     2004 2023-02-21 11:01:40.245963 aws_lambda_powertools-2.9.0/aws_lambda_powertools/utilities/validation/exceptions.py
--rw-r--r--   0        0        0     8162 2023-02-21 11:01:40.245963 aws_lambda_powertools-2.9.0/aws_lambda_powertools/utilities/validation/validator.py
--rw-r--r--   0        0        0     5390 2023-02-21 11:04:12.801394 aws_lambda_powertools-2.9.0/pyproject.toml
--rw-r--r--   0        0        0     8420 1970-01-01 00:00:00.000000 aws_lambda_powertools-2.9.0/setup.py
--rw-r--r--   0        0        0     8149 1970-01-01 00:00:00.000000 aws_lambda_powertools-2.9.0/PKG-INFO
+-rw-r--r--   0        0        0      951 2023-03-01 21:07:13.448219 aws_lambda_powertools-2.9.1/LICENSE
+-rw-r--r--   0        0        0     6118 2023-03-01 21:07:13.448219 aws_lambda_powertools-2.9.1/README.md
+-rw-r--r--   0        0        0    10200 2023-03-01 21:07:13.448219 aws_lambda_powertools-2.9.1/THIRD-PARTY-LICENSES
+-rw-r--r--   0        0        0      447 2023-03-01 21:07:13.448219 aws_lambda_powertools-2.9.1/aws_lambda_powertools/__init__.py
+-rw-r--r--   0        0        0      521 2023-03-01 21:07:13.448219 aws_lambda_powertools-2.9.1/aws_lambda_powertools/event_handler/__init__.py
+-rw-r--r--   0        0        0    32035 2023-03-01 21:07:13.448219 aws_lambda_powertools-2.9.1/aws_lambda_powertools/event_handler/api_gateway.py
+-rw-r--r--   0        0        0     6745 2023-03-01 21:07:13.448219 aws_lambda_powertools-2.9.1/aws_lambda_powertools/event_handler/appsync.py
+-rw-r--r--   0        0        0      163 2023-03-01 21:07:13.448219 aws_lambda_powertools-2.9.1/aws_lambda_powertools/event_handler/content_types.py
+-rw-r--r--   0        0        0     1160 2023-03-01 21:07:13.448219 aws_lambda_powertools-2.9.1/aws_lambda_powertools/event_handler/exceptions.py
+-rw-r--r--   0        0        0     1686 2023-03-01 21:07:13.448219 aws_lambda_powertools-2.9.1/aws_lambda_powertools/event_handler/lambda_function_url.py
+-rw-r--r--   0        0        0      867 2023-03-01 21:07:13.448219 aws_lambda_powertools-2.9.1/aws_lambda_powertools/event_handler/router.py
+-rw-r--r--   0        0        0      163 2023-03-01 21:07:13.448219 aws_lambda_powertools-2.9.1/aws_lambda_powertools/exceptions/__init__.py
+-rw-r--r--   0        0        0       72 2023-03-01 21:07:13.448219 aws_lambda_powertools-2.9.1/aws_lambda_powertools/logging/__init__.py
+-rw-r--r--   0        0        0      369 2023-03-01 21:07:13.448219 aws_lambda_powertools-2.9.1/aws_lambda_powertools/logging/correlation_paths.py
+-rw-r--r--   0        0        0       58 2023-03-01 21:07:13.448219 aws_lambda_powertools-2.9.1/aws_lambda_powertools/logging/exceptions.py
+-rw-r--r--   0        0        0      491 2023-03-01 21:07:13.448219 aws_lambda_powertools-2.9.1/aws_lambda_powertools/logging/filters.py
+-rw-r--r--   0        0        0    12654 2023-03-01 21:07:13.448219 aws_lambda_powertools-2.9.1/aws_lambda_powertools/logging/formatter.py
+-rw-r--r--   0        0        0     1736 2023-03-01 21:07:13.448219 aws_lambda_powertools-2.9.1/aws_lambda_powertools/logging/lambda_context.py
+-rw-r--r--   0        0        0    28767 2023-03-01 21:07:13.448219 aws_lambda_powertools-2.9.1/aws_lambda_powertools/logging/logger.py
+-rw-r--r--   0        0        0     3543 2023-03-01 21:07:13.448219 aws_lambda_powertools-2.9.1/aws_lambda_powertools/logging/utils.py
+-rw-r--r--   0        0        0      524 2023-03-01 21:07:13.448219 aws_lambda_powertools-2.9.1/aws_lambda_powertools/metrics/__init__.py
+-rw-r--r--   0        0        0    22062 2023-03-01 21:07:13.448219 aws_lambda_powertools-2.9.1/aws_lambda_powertools/metrics/base.py
+-rw-r--r--   0        0        0      418 2023-03-01 21:07:13.448219 aws_lambda_powertools-2.9.1/aws_lambda_powertools/metrics/exceptions.py
+-rw-r--r--   0        0        0      136 2023-03-01 21:07:13.448219 aws_lambda_powertools-2.9.1/aws_lambda_powertools/metrics/metric.py
+-rw-r--r--   0        0        0     4693 2023-03-01 21:07:13.448219 aws_lambda_powertools-2.9.1/aws_lambda_powertools/metrics/metrics.py
+-rw-r--r--   0        0        0      166 2023-03-01 21:07:13.448219 aws_lambda_powertools-2.9.1/aws_lambda_powertools/metrics/types.py
+-rw-r--r--   0        0        0      127 2023-03-01 21:07:13.448219 aws_lambda_powertools-2.9.1/aws_lambda_powertools/middleware_factory/__init__.py
+-rw-r--r--   0        0        0      106 2023-03-01 21:07:13.448219 aws_lambda_powertools-2.9.1/aws_lambda_powertools/middleware_factory/exceptions.py
+-rw-r--r--   0        0        0     5112 2023-03-01 21:07:13.448219 aws_lambda_powertools-2.9.1/aws_lambda_powertools/middleware_factory/factory.py
+-rw-r--r--   0        0        0      750 2023-03-01 21:07:13.448219 aws_lambda_powertools-2.9.1/aws_lambda_powertools/package_logger.py
+-rw-r--r--   0        0        0        0 2023-03-01 21:07:13.448219 aws_lambda_powertools-2.9.1/aws_lambda_powertools/py.typed
+-rw-r--r--   0        0        0        0 2023-03-01 21:07:13.448219 aws_lambda_powertools-2.9.1/aws_lambda_powertools/shared/__init__.py
+-rw-r--r--   0        0        0      929 2023-03-01 21:07:13.448219 aws_lambda_powertools-2.9.1/aws_lambda_powertools/shared/cache_dict.py
+-rw-r--r--   0        0        0     1209 2023-03-01 21:07:13.448219 aws_lambda_powertools-2.9.1/aws_lambda_powertools/shared/constants.py
+-rw-r--r--   0        0        0     3832 2023-03-01 21:07:13.448219 aws_lambda_powertools-2.9.1/aws_lambda_powertools/shared/cookies.py
+-rw-r--r--   0        0        0     4703 2023-03-01 21:07:13.448219 aws_lambda_powertools-2.9.1/aws_lambda_powertools/shared/functions.py
+-rw-r--r--   0        0        0     5372 2023-03-01 21:07:13.448219 aws_lambda_powertools-2.9.1/aws_lambda_powertools/shared/headers_serializer.py
+-rw-r--r--   0        0        0      406 2023-03-01 21:07:13.448219 aws_lambda_powertools-2.9.1/aws_lambda_powertools/shared/json_encoder.py
+-rw-r--r--   0        0        0     2035 2023-03-01 21:07:13.448219 aws_lambda_powertools-2.9.1/aws_lambda_powertools/shared/lazy_import.py
+-rw-r--r--   0        0        0      275 2023-03-01 21:07:13.448219 aws_lambda_powertools-2.9.1/aws_lambda_powertools/shared/types.py
+-rw-r--r--   0        0        0      143 2023-03-01 21:07:13.448219 aws_lambda_powertools-2.9.1/aws_lambda_powertools/tracing/__init__.py
+-rw-r--r--   0        0        0     4424 2023-03-01 21:07:13.448219 aws_lambda_powertools-2.9.1/aws_lambda_powertools/tracing/base.py
+-rw-r--r--   0        0        0      492 2023-03-01 21:07:13.448219 aws_lambda_powertools-2.9.1/aws_lambda_powertools/tracing/extensions.py
+-rw-r--r--   0        0        0    30676 2023-03-01 21:07:13.452219 aws_lambda_powertools-2.9.1/aws_lambda_powertools/tracing/tracer.py
+-rw-r--r--   0        0        0       64 2023-03-01 21:07:13.452219 aws_lambda_powertools-2.9.1/aws_lambda_powertools/utilities/__init__.py
+-rw-r--r--   0        0        0      897 2023-03-01 21:07:13.452219 aws_lambda_powertools-2.9.1/aws_lambda_powertools/utilities/batch/__init__.py
+-rw-r--r--   0        0        0    23738 2023-03-01 21:07:13.452219 aws_lambda_powertools-2.9.1/aws_lambda_powertools/utilities/batch/base.py
+-rw-r--r--   0        0        0     1240 2023-03-01 21:07:13.452219 aws_lambda_powertools-2.9.1/aws_lambda_powertools/utilities/batch/exceptions.py
+-rw-r--r--   0        0        0     3194 2023-03-01 21:07:13.452219 aws_lambda_powertools-2.9.1/aws_lambda_powertools/utilities/batch/sqs_fifo_partial_processor.py
+-rw-r--r--   0        0        0      947 2023-03-01 21:07:13.452219 aws_lambda_powertools-2.9.1/aws_lambda_powertools/utilities/batch/types.py
+-rw-r--r--   0        0        0     1490 2023-03-01 21:07:13.452219 aws_lambda_powertools-2.9.1/aws_lambda_powertools/utilities/data_classes/__init__.py
+-rw-r--r--   0        0        0     3721 2023-03-01 21:07:13.452219 aws_lambda_powertools-2.9.1/aws_lambda_powertools/utilities/data_classes/active_mq_event.py
+-rw-r--r--   0        0        0     1632 2023-03-01 21:07:13.452219 aws_lambda_powertools-2.9.1/aws_lambda_powertools/utilities/data_classes/alb_event.py
+-rw-r--r--   0        0        0    18824 2023-03-01 21:07:13.452219 aws_lambda_powertools-2.9.1/aws_lambda_powertools/utilities/data_classes/api_gateway_authorizer_event.py
+-rw-r--r--   0        0        0     8783 2023-03-01 21:07:13.452219 aws_lambda_powertools-2.9.1/aws_lambda_powertools/utilities/data_classes/api_gateway_proxy_event.py
+-rw-r--r--   0        0        0        0 2023-03-01 21:07:13.452219 aws_lambda_powertools-2.9.1/aws_lambda_powertools/utilities/data_classes/appsync/__init__.py
+-rw-r--r--   0        0        0     2662 2023-03-01 21:07:13.452219 aws_lambda_powertools-2.9.1/aws_lambda_powertools/utilities/data_classes/appsync/scalar_types_utils.py
+-rw-r--r--   0        0        0     3927 2023-03-01 21:07:13.452219 aws_lambda_powertools-2.9.1/aws_lambda_powertools/utilities/data_classes/appsync_authorizer_event.py
+-rw-r--r--   0        0        0     7838 2023-03-01 21:07:13.452219 aws_lambda_powertools-2.9.1/aws_lambda_powertools/utilities/data_classes/appsync_resolver_event.py
+-rw-r--r--   0        0        0     4207 2023-03-01 21:07:13.452219 aws_lambda_powertools-2.9.1/aws_lambda_powertools/utilities/data_classes/cloud_watch_custom_widget_event.py
+-rw-r--r--   0        0        0     3322 2023-03-01 21:07:13.452219 aws_lambda_powertools-2.9.1/aws_lambda_powertools/utilities/data_classes/cloud_watch_logs_event.py
+-rw-r--r--   0        0        0     7206 2023-03-01 21:07:13.452219 aws_lambda_powertools-2.9.1/aws_lambda_powertools/utilities/data_classes/code_pipeline_job_event.py
+-rw-r--r--   0        0        0    32633 2023-03-01 21:07:13.452219 aws_lambda_powertools-2.9.1/aws_lambda_powertools/utilities/data_classes/cognito_user_pool_event.py
+-rw-r--r--   0        0        0    13637 2023-03-01 21:07:13.452219 aws_lambda_powertools-2.9.1/aws_lambda_powertools/utilities/data_classes/common.py
+-rw-r--r--   0        0        0     5484 2023-03-01 21:07:13.452219 aws_lambda_powertools-2.9.1/aws_lambda_powertools/utilities/data_classes/connect_contact_flow_event.py
+-rw-r--r--   0        0        0     9418 2023-03-01 21:07:13.452219 aws_lambda_powertools-2.9.1/aws_lambda_powertools/utilities/data_classes/dynamo_db_stream_event.py
+-rw-r--r--   0        0        0     2423 2023-03-01 21:07:13.452219 aws_lambda_powertools-2.9.1/aws_lambda_powertools/utilities/data_classes/event_bridge_event.py
+-rw-r--r--   0        0        0     1094 2023-03-01 21:07:13.452219 aws_lambda_powertools-2.9.1/aws_lambda_powertools/utilities/data_classes/event_source.py
+-rw-r--r--   0        0        0     3847 2023-03-01 21:07:13.452219 aws_lambda_powertools-2.9.1/aws_lambda_powertools/utilities/data_classes/kafka_event.py
+-rw-r--r--   0        0        0     3847 2023-03-01 21:07:13.452219 aws_lambda_powertools-2.9.1/aws_lambda_powertools/utilities/data_classes/kinesis_firehose_event.py
+-rw-r--r--   0        0        0     3913 2023-03-01 21:07:13.452219 aws_lambda_powertools-2.9.1/aws_lambda_powertools/utilities/data_classes/kinesis_stream_event.py
+-rw-r--r--   0        0        0      633 2023-03-01 21:07:13.452219 aws_lambda_powertools-2.9.1/aws_lambda_powertools/utilities/data_classes/lambda_function_url_event.py
+-rw-r--r--   0        0        0     3005 2023-03-01 21:07:13.452219 aws_lambda_powertools-2.9.1/aws_lambda_powertools/utilities/data_classes/rabbit_mq_event.py
+-rw-r--r--   0        0        0     5942 2023-03-01 21:07:13.452219 aws_lambda_powertools-2.9.1/aws_lambda_powertools/utilities/data_classes/s3_event.py
+-rw-r--r--   0        0        0    12949 2023-03-01 21:07:13.452219 aws_lambda_powertools-2.9.1/aws_lambda_powertools/utilities/data_classes/s3_object_event.py
+-rw-r--r--   0        0        0     8846 2023-03-01 21:07:13.452219 aws_lambda_powertools-2.9.1/aws_lambda_powertools/utilities/data_classes/ses_event.py
+-rw-r--r--   0        0        0     3893 2023-03-01 21:07:13.452219 aws_lambda_powertools-2.9.1/aws_lambda_powertools/utilities/data_classes/sns_event.py
+-rw-r--r--   0        0        0     5257 2023-03-01 21:07:13.452219 aws_lambda_powertools-2.9.1/aws_lambda_powertools/utilities/data_classes/sqs_event.py
+-rw-r--r--   0        0        0      393 2023-03-01 21:07:13.452219 aws_lambda_powertools-2.9.1/aws_lambda_powertools/utilities/feature_flags/__init__.py
+-rw-r--r--   0        0        0     4032 2023-03-01 21:07:13.452219 aws_lambda_powertools-2.9.1/aws_lambda_powertools/utilities/feature_flags/appconfig.py
+-rw-r--r--   0        0        0     1745 2023-03-01 21:07:13.452219 aws_lambda_powertools-2.9.1/aws_lambda_powertools/utilities/feature_flags/base.py
+-rw-r--r--   0        0        0      447 2023-03-01 21:07:13.452219 aws_lambda_powertools-2.9.1/aws_lambda_powertools/utilities/feature_flags/exceptions.py
+-rw-r--r--   0        0        0    13570 2023-03-01 21:07:13.452219 aws_lambda_powertools-2.9.1/aws_lambda_powertools/utilities/feature_flags/feature_flags.py
+-rw-r--r--   0        0        0    18840 2023-03-01 21:07:13.452219 aws_lambda_powertools-2.9.1/aws_lambda_powertools/utilities/feature_flags/schema.py
+-rw-r--r--   0        0        0     4081 2023-03-01 21:07:13.452219 aws_lambda_powertools-2.9.1/aws_lambda_powertools/utilities/feature_flags/time_conditions.py
+-rw-r--r--   0        0        0      473 2023-03-01 21:07:13.452219 aws_lambda_powertools-2.9.1/aws_lambda_powertools/utilities/idempotency/__init__.py
+-rw-r--r--   0        0        0     8808 2023-03-01 21:07:13.452219 aws_lambda_powertools-2.9.1/aws_lambda_powertools/utilities/idempotency/base.py
+-rw-r--r--   0        0        0     2440 2023-03-01 21:07:13.452219 aws_lambda_powertools-2.9.1/aws_lambda_powertools/utilities/idempotency/config.py
+-rw-r--r--   0        0        0     1683 2023-03-01 21:07:13.452219 aws_lambda_powertools-2.9.1/aws_lambda_powertools/utilities/idempotency/exceptions.py
+-rw-r--r--   0        0        0     4930 2023-03-01 21:07:13.452219 aws_lambda_powertools-2.9.1/aws_lambda_powertools/utilities/idempotency/idempotency.py
+-rw-r--r--   0        0        0        0 2023-03-01 21:07:13.452219 aws_lambda_powertools-2.9.1/aws_lambda_powertools/utilities/idempotency/persistence/__init__.py
+-rw-r--r--   0        0        0    16325 2023-03-01 21:07:13.452219 aws_lambda_powertools-2.9.1/aws_lambda_powertools/utilities/idempotency/persistence/base.py
+-rw-r--r--   0        0        0    10956 2023-03-01 21:07:13.452219 aws_lambda_powertools-2.9.1/aws_lambda_powertools/utilities/idempotency/persistence/dynamodb.py
+-rw-r--r--   0        0        0     2682 2023-03-01 21:07:13.452219 aws_lambda_powertools-2.9.1/aws_lambda_powertools/utilities/jmespath_utils/__init__.py
+-rw-r--r--   0        0        0      412 2023-03-01 21:07:13.452219 aws_lambda_powertools-2.9.1/aws_lambda_powertools/utilities/jmespath_utils/envelopes.py
+-rw-r--r--   0        0        0      730 2023-03-01 21:07:13.452219 aws_lambda_powertools-2.9.1/aws_lambda_powertools/utilities/parameters/__init__.py
+-rw-r--r--   0        0        0     6872 2023-03-01 21:07:13.452219 aws_lambda_powertools-2.9.1/aws_lambda_powertools/utilities/parameters/appconfig.py
+-rw-r--r--   0        0        0    14331 2023-03-01 21:07:13.452219 aws_lambda_powertools-2.9.1/aws_lambda_powertools/utilities/parameters/base.py
+-rw-r--r--   0        0        0     8256 2023-03-01 21:07:13.452219 aws_lambda_powertools-2.9.1/aws_lambda_powertools/utilities/parameters/dynamodb.py
+-rw-r--r--   0        0        0      253 2023-03-01 21:07:13.452219 aws_lambda_powertools-2.9.1/aws_lambda_powertools/utilities/parameters/exceptions.py
+-rw-r--r--   0        0        0     5432 2023-03-01 21:07:13.452219 aws_lambda_powertools-2.9.1/aws_lambda_powertools/utilities/parameters/secrets.py
+-rw-r--r--   0        0        0    28878 2023-03-01 21:07:13.452219 aws_lambda_powertools-2.9.1/aws_lambda_powertools/utilities/parameters/ssm.py
+-rw-r--r--   0        0        0       98 2023-03-01 21:07:13.452219 aws_lambda_powertools-2.9.1/aws_lambda_powertools/utilities/parameters/types.py
+-rw-r--r--   0        0        0      397 2023-03-01 21:07:13.452219 aws_lambda_powertools-2.9.1/aws_lambda_powertools/utilities/parser/__init__.py
+-rw-r--r--   0        0        0      870 2023-03-01 21:07:13.452219 aws_lambda_powertools-2.9.1/aws_lambda_powertools/utilities/parser/envelopes/__init__.py
+-rw-r--r--   0        0        0     1115 2023-03-01 21:07:13.452219 aws_lambda_powertools-2.9.1/aws_lambda_powertools/utilities/parser/envelopes/apigw.py
+-rw-r--r--   0        0        0     1131 2023-03-01 21:07:13.452219 aws_lambda_powertools-2.9.1/aws_lambda_powertools/utilities/parser/envelopes/apigwv2.py
+-rw-r--r--   0        0        0     1966 2023-03-01 21:07:13.452219 aws_lambda_powertools-2.9.1/aws_lambda_powertools/utilities/parser/envelopes/base.py
+-rw-r--r--   0        0        0     1444 2023-03-01 21:07:13.452219 aws_lambda_powertools-2.9.1/aws_lambda_powertools/utilities/parser/envelopes/cloudwatch.py
+-rw-r--r--   0        0        0     1577 2023-03-01 21:07:13.452219 aws_lambda_powertools-2.9.1/aws_lambda_powertools/utilities/parser/envelopes/dynamodb.py
+-rw-r--r--   0        0        0     1084 2023-03-01 21:07:13.452219 aws_lambda_powertools-2.9.1/aws_lambda_powertools/utilities/parser/envelopes/event_bridge.py
+-rw-r--r--   0        0        0     1722 2023-03-01 21:07:13.452219 aws_lambda_powertools-2.9.1/aws_lambda_powertools/utilities/parser/envelopes/kafka.py
+-rw-r--r--   0        0        0     1740 2023-03-01 21:07:13.452219 aws_lambda_powertools-2.9.1/aws_lambda_powertools/utilities/parser/envelopes/kinesis.py
+-rw-r--r--   0        0        0     1817 2023-03-01 21:07:13.452219 aws_lambda_powertools-2.9.1/aws_lambda_powertools/utilities/parser/envelopes/kinesis_firehose.py
+-rw-r--r--   0        0        0     1126 2023-03-01 21:07:13.452219 aws_lambda_powertools-2.9.1/aws_lambda_powertools/utilities/parser/envelopes/lambda_function_url.py
+-rw-r--r--   0        0        0     2830 2023-03-01 21:07:13.452219 aws_lambda_powertools-2.9.1/aws_lambda_powertools/utilities/parser/envelopes/sns.py
+-rw-r--r--   0        0        0     1366 2023-03-01 21:07:13.456220 aws_lambda_powertools-2.9.1/aws_lambda_powertools/utilities/parser/envelopes/sqs.py
+-rw-r--r--   0        0        0      207 2023-03-01 21:07:13.456220 aws_lambda_powertools-2.9.1/aws_lambda_powertools/utilities/parser/exceptions.py
+-rw-r--r--   0        0        0     3479 2023-03-01 21:07:13.456220 aws_lambda_powertools-2.9.1/aws_lambda_powertools/utilities/parser/models/__init__.py
+-rw-r--r--   0        0        0      439 2023-03-01 21:07:13.456220 aws_lambda_powertools-2.9.1/aws_lambda_powertools/utilities/parser/models/alb.py
+-rw-r--r--   0        0        0     3064 2023-03-01 21:07:13.456220 aws_lambda_powertools-2.9.1/aws_lambda_powertools/utilities/parser/models/apigw.py
+-rw-r--r--   0        0        0     1890 2023-03-01 21:07:13.456220 aws_lambda_powertools-2.9.1/aws_lambda_powertools/utilities/parser/models/apigwv2.py
+-rw-r--r--   0        0        0     1245 2023-03-01 21:07:13.456220 aws_lambda_powertools-2.9.1/aws_lambda_powertools/utilities/parser/models/cloudwatch.py
+-rw-r--r--   0        0        0     1855 2023-03-01 21:07:13.456220 aws_lambda_powertools-2.9.1/aws_lambda_powertools/utilities/parser/models/dynamodb.py
+-rw-r--r--   0        0        0      480 2023-03-01 21:07:13.456220 aws_lambda_powertools-2.9.1/aws_lambda_powertools/utilities/parser/models/event_bridge.py
+-rw-r--r--   0        0        0     1839 2023-03-01 21:07:13.456220 aws_lambda_powertools-2.9.1/aws_lambda_powertools/utilities/parser/models/kafka.py
+-rw-r--r--   0        0        0     1836 2023-03-01 21:07:13.456220 aws_lambda_powertools-2.9.1/aws_lambda_powertools/utilities/parser/models/kinesis.py
+-rw-r--r--   0        0        0      926 2023-03-01 21:07:13.456220 aws_lambda_powertools-2.9.1/aws_lambda_powertools/utilities/parser/models/kinesis_firehose.py
+-rw-r--r--   0        0        0      611 2023-03-01 21:07:13.456220 aws_lambda_powertools-2.9.1/aws_lambda_powertools/utilities/parser/models/lambda_function_url.py
+-rw-r--r--   0        0        0     2078 2023-03-01 21:07:13.456220 aws_lambda_powertools-2.9.1/aws_lambda_powertools/utilities/parser/models/s3.py
+-rw-r--r--   0        0        0     1256 2023-03-01 21:07:13.456220 aws_lambda_powertools-2.9.1/aws_lambda_powertools/utilities/parser/models/s3_object_event.py
+-rw-r--r--   0        0        0     1573 2023-03-01 21:07:13.456220 aws_lambda_powertools-2.9.1/aws_lambda_powertools/utilities/parser/models/ses.py
+-rw-r--r--   0        0        0     1663 2023-03-01 21:07:13.456220 aws_lambda_powertools-2.9.1/aws_lambda_powertools/utilities/parser/models/sns.py
+-rw-r--r--   0        0        0     2627 2023-03-01 21:07:13.456220 aws_lambda_powertools-2.9.1/aws_lambda_powertools/utilities/parser/models/sqs.py
+-rw-r--r--   0        0        0     5317 2023-03-01 21:07:13.456220 aws_lambda_powertools-2.9.1/aws_lambda_powertools/utilities/parser/parser.py
+-rw-r--r--   0        0        0      530 2023-03-01 21:07:13.456220 aws_lambda_powertools-2.9.1/aws_lambda_powertools/utilities/parser/pydantic.py
+-rw-r--r--   0        0        0      466 2023-03-01 21:07:13.456220 aws_lambda_powertools-2.9.1/aws_lambda_powertools/utilities/parser/types.py
+-rw-r--r--   0        0        0       97 2023-03-01 21:07:13.456220 aws_lambda_powertools-2.9.1/aws_lambda_powertools/utilities/streaming/__init__.py
+-rw-r--r--   0        0        0     6028 2023-03-01 21:07:13.456220 aws_lambda_powertools-2.9.1/aws_lambda_powertools/utilities/streaming/_s3_seekable_io.py
+-rw-r--r--   0        0        0     8150 2023-03-01 21:07:13.456220 aws_lambda_powertools-2.9.1/aws_lambda_powertools/utilities/streaming/compat.py
+-rw-r--r--   0        0        0     9386 2023-03-01 21:07:13.456220 aws_lambda_powertools-2.9.1/aws_lambda_powertools/utilities/streaming/s3_object.py
+-rw-r--r--   0        0        0      430 2023-03-01 21:07:13.456220 aws_lambda_powertools-2.9.1/aws_lambda_powertools/utilities/streaming/transformations/__init__.py
+-rw-r--r--   0        0        0      846 2023-03-01 21:07:13.456220 aws_lambda_powertools-2.9.1/aws_lambda_powertools/utilities/streaming/transformations/base.py
+-rw-r--r--   0        0        0     2312 2023-03-01 21:07:13.456220 aws_lambda_powertools-2.9.1/aws_lambda_powertools/utilities/streaming/transformations/csv.py
+-rw-r--r--   0        0        0      886 2023-03-01 21:07:13.456220 aws_lambda_powertools-2.9.1/aws_lambda_powertools/utilities/streaming/transformations/gzip.py
+-rw-r--r--   0        0        0     2217 2023-03-01 21:07:13.456220 aws_lambda_powertools-2.9.1/aws_lambda_powertools/utilities/streaming/transformations/zip.py
+-rw-r--r--   0        0        0      142 2023-03-01 21:07:13.456220 aws_lambda_powertools-2.9.1/aws_lambda_powertools/utilities/typing/__init__.py
+-rw-r--r--   0        0        0      808 2023-03-01 21:07:13.456220 aws_lambda_powertools-2.9.1/aws_lambda_powertools/utilities/typing/lambda_client_context.py
+-rw-r--r--   0        0        0      730 2023-03-01 21:07:13.456220 aws_lambda_powertools-2.9.1/aws_lambda_powertools/utilities/typing/lambda_client_context_mobile_client.py
+-rw-r--r--   0        0        0      556 2023-03-01 21:07:13.456220 aws_lambda_powertools-2.9.1/aws_lambda_powertools/utilities/typing/lambda_cognito_identity.py
+-rw-r--r--   0        0        0     2682 2023-03-01 21:07:13.456220 aws_lambda_powertools-2.9.1/aws_lambda_powertools/utilities/typing/lambda_context.py
+-rw-r--r--   0        0        0      398 2023-03-01 21:07:13.456220 aws_lambda_powertools-2.9.1/aws_lambda_powertools/utilities/validation/__init__.py
+-rw-r--r--   0        0        0     1608 2023-03-01 21:07:13.456220 aws_lambda_powertools-2.9.1/aws_lambda_powertools/utilities/validation/base.py
+-rw-r--r--   0        0        0      438 2023-03-01 21:07:13.456220 aws_lambda_powertools-2.9.1/aws_lambda_powertools/utilities/validation/envelopes.py
+-rw-r--r--   0        0        0     2004 2023-03-01 21:07:13.456220 aws_lambda_powertools-2.9.1/aws_lambda_powertools/utilities/validation/exceptions.py
+-rw-r--r--   0        0        0     8162 2023-03-01 21:07:13.456220 aws_lambda_powertools-2.9.1/aws_lambda_powertools/utilities/validation/validator.py
+-rw-r--r--   0        0        0     5328 2023-03-01 21:10:05.571417 aws_lambda_powertools-2.9.1/pyproject.toml
+-rw-r--r--   0        0        0     8087 1970-01-01 00:00:00.000000 aws_lambda_powertools-2.9.1/PKG-INFO
```

### Comparing `aws_lambda_powertools-2.9.0/LICENSE` & `aws_lambda_powertools-2.9.1/LICENSE`

 * *Files identical despite different names*

### Comparing `aws_lambda_powertools-2.9.0/README.md` & `aws_lambda_powertools-2.9.1/README.md`

 * *Files identical despite different names*

### Comparing `aws_lambda_powertools-2.9.0/THIRD-PARTY-LICENSES` & `aws_lambda_powertools-2.9.1/THIRD-PARTY-LICENSES`

 * *Files identical despite different names*

### Comparing `aws_lambda_powertools-2.9.0/aws_lambda_powertools/event_handler/__init__.py` & `aws_lambda_powertools-2.9.1/aws_lambda_powertools/event_handler/__init__.py`

 * *Files identical despite different names*

### Comparing `aws_lambda_powertools-2.9.0/aws_lambda_powertools/event_handler/api_gateway.py` & `aws_lambda_powertools-2.9.1/aws_lambda_powertools/event_handler/api_gateway.py`

 * *Files identical despite different names*

### Comparing `aws_lambda_powertools-2.9.0/aws_lambda_powertools/event_handler/appsync.py` & `aws_lambda_powertools-2.9.1/aws_lambda_powertools/event_handler/appsync.py`

 * *Files identical despite different names*

### Comparing `aws_lambda_powertools-2.9.0/aws_lambda_powertools/event_handler/exceptions.py` & `aws_lambda_powertools-2.9.1/aws_lambda_powertools/event_handler/exceptions.py`

 * *Files identical despite different names*

### Comparing `aws_lambda_powertools-2.9.0/aws_lambda_powertools/event_handler/lambda_function_url.py` & `aws_lambda_powertools-2.9.1/aws_lambda_powertools/event_handler/lambda_function_url.py`

 * *Files identical despite different names*

### Comparing `aws_lambda_powertools-2.9.0/aws_lambda_powertools/event_handler/router.py` & `aws_lambda_powertools-2.9.1/aws_lambda_powertools/event_handler/router.py`

 * *Files identical despite different names*

### Comparing `aws_lambda_powertools-2.9.0/aws_lambda_powertools/logging/formatter.py` & `aws_lambda_powertools-2.9.1/aws_lambda_powertools/logging/formatter.py`

 * *Files identical despite different names*

### Comparing `aws_lambda_powertools-2.9.0/aws_lambda_powertools/logging/lambda_context.py` & `aws_lambda_powertools-2.9.1/aws_lambda_powertools/logging/lambda_context.py`

 * *Files identical despite different names*

### Comparing `aws_lambda_powertools-2.9.0/aws_lambda_powertools/logging/logger.py` & `aws_lambda_powertools-2.9.1/aws_lambda_powertools/logging/logger.py`

 * *Files identical despite different names*

### Comparing `aws_lambda_powertools-2.9.0/aws_lambda_powertools/logging/utils.py` & `aws_lambda_powertools-2.9.1/aws_lambda_powertools/logging/utils.py`

 * *Files identical despite different names*

### Comparing `aws_lambda_powertools-2.9.0/aws_lambda_powertools/metrics/__init__.py` & `aws_lambda_powertools-2.9.1/aws_lambda_powertools/metrics/__init__.py`

 * *Files identical despite different names*

### Comparing `aws_lambda_powertools-2.9.0/aws_lambda_powertools/metrics/base.py` & `aws_lambda_powertools-2.9.1/aws_lambda_powertools/metrics/base.py`

 * *Files identical despite different names*

### Comparing `aws_lambda_powertools-2.9.0/aws_lambda_powertools/metrics/metrics.py` & `aws_lambda_powertools-2.9.1/aws_lambda_powertools/metrics/metrics.py`

 * *Files identical despite different names*

### Comparing `aws_lambda_powertools-2.9.0/aws_lambda_powertools/middleware_factory/factory.py` & `aws_lambda_powertools-2.9.1/aws_lambda_powertools/middleware_factory/factory.py`

 * *Files identical despite different names*

### Comparing `aws_lambda_powertools-2.9.0/aws_lambda_powertools/package_logger.py` & `aws_lambda_powertools-2.9.1/aws_lambda_powertools/package_logger.py`

 * *Files identical despite different names*

### Comparing `aws_lambda_powertools-2.9.0/aws_lambda_powertools/shared/cache_dict.py` & `aws_lambda_powertools-2.9.1/aws_lambda_powertools/shared/cache_dict.py`

 * *Files identical despite different names*

### Comparing `aws_lambda_powertools-2.9.0/aws_lambda_powertools/shared/constants.py` & `aws_lambda_powertools-2.9.1/aws_lambda_powertools/shared/constants.py`

 * *Files identical despite different names*

### Comparing `aws_lambda_powertools-2.9.0/aws_lambda_powertools/shared/cookies.py` & `aws_lambda_powertools-2.9.1/aws_lambda_powertools/shared/cookies.py`

 * *Files identical despite different names*

### Comparing `aws_lambda_powertools-2.9.0/aws_lambda_powertools/shared/functions.py` & `aws_lambda_powertools-2.9.1/aws_lambda_powertools/shared/functions.py`

 * *Files identical despite different names*

### Comparing `aws_lambda_powertools-2.9.0/aws_lambda_powertools/shared/headers_serializer.py` & `aws_lambda_powertools-2.9.1/aws_lambda_powertools/shared/headers_serializer.py`

 * *Files identical despite different names*

### Comparing `aws_lambda_powertools-2.9.0/aws_lambda_powertools/shared/lazy_import.py` & `aws_lambda_powertools-2.9.1/aws_lambda_powertools/shared/lazy_import.py`

 * *Files identical despite different names*

### Comparing `aws_lambda_powertools-2.9.0/aws_lambda_powertools/tracing/base.py` & `aws_lambda_powertools-2.9.1/aws_lambda_powertools/tracing/base.py`

 * *Files identical despite different names*

### Comparing `aws_lambda_powertools-2.9.0/aws_lambda_powertools/tracing/tracer.py` & `aws_lambda_powertools-2.9.1/aws_lambda_powertools/tracing/tracer.py`

 * *Files identical despite different names*

### Comparing `aws_lambda_powertools-2.9.0/aws_lambda_powertools/utilities/batch/__init__.py` & `aws_lambda_powertools-2.9.1/aws_lambda_powertools/utilities/batch/__init__.py`

 * *Files identical despite different names*

### Comparing `aws_lambda_powertools-2.9.0/aws_lambda_powertools/utilities/batch/base.py` & `aws_lambda_powertools-2.9.1/aws_lambda_powertools/utilities/batch/base.py`

 * *Files identical despite different names*

### Comparing `aws_lambda_powertools-2.9.0/aws_lambda_powertools/utilities/batch/exceptions.py` & `aws_lambda_powertools-2.9.1/aws_lambda_powertools/utilities/batch/exceptions.py`

 * *Files identical despite different names*

### Comparing `aws_lambda_powertools-2.9.0/aws_lambda_powertools/utilities/batch/sqs_fifo_partial_processor.py` & `aws_lambda_powertools-2.9.1/aws_lambda_powertools/utilities/batch/sqs_fifo_partial_processor.py`

 * *Files identical despite different names*

### Comparing `aws_lambda_powertools-2.9.0/aws_lambda_powertools/utilities/batch/types.py` & `aws_lambda_powertools-2.9.1/aws_lambda_powertools/utilities/batch/types.py`

 * *Files identical despite different names*

### Comparing `aws_lambda_powertools-2.9.0/aws_lambda_powertools/utilities/data_classes/__init__.py` & `aws_lambda_powertools-2.9.1/aws_lambda_powertools/utilities/data_classes/__init__.py`

 * *Files identical despite different names*

### Comparing `aws_lambda_powertools-2.9.0/aws_lambda_powertools/utilities/data_classes/active_mq_event.py` & `aws_lambda_powertools-2.9.1/aws_lambda_powertools/utilities/data_classes/active_mq_event.py`

 * *Files identical despite different names*

### Comparing `aws_lambda_powertools-2.9.0/aws_lambda_powertools/utilities/data_classes/alb_event.py` & `aws_lambda_powertools-2.9.1/aws_lambda_powertools/utilities/data_classes/alb_event.py`

 * *Files identical despite different names*

### Comparing `aws_lambda_powertools-2.9.0/aws_lambda_powertools/utilities/data_classes/api_gateway_authorizer_event.py` & `aws_lambda_powertools-2.9.1/aws_lambda_powertools/utilities/data_classes/api_gateway_authorizer_event.py`

 * *Files identical despite different names*

### Comparing `aws_lambda_powertools-2.9.0/aws_lambda_powertools/utilities/data_classes/api_gateway_proxy_event.py` & `aws_lambda_powertools-2.9.1/aws_lambda_powertools/utilities/data_classes/api_gateway_proxy_event.py`

 * *Files identical despite different names*

### Comparing `aws_lambda_powertools-2.9.0/aws_lambda_powertools/utilities/data_classes/appsync/scalar_types_utils.py` & `aws_lambda_powertools-2.9.1/aws_lambda_powertools/utilities/data_classes/appsync/scalar_types_utils.py`

 * *Files identical despite different names*

### Comparing `aws_lambda_powertools-2.9.0/aws_lambda_powertools/utilities/data_classes/appsync_authorizer_event.py` & `aws_lambda_powertools-2.9.1/aws_lambda_powertools/utilities/data_classes/appsync_authorizer_event.py`

 * *Files identical despite different names*

### Comparing `aws_lambda_powertools-2.9.0/aws_lambda_powertools/utilities/data_classes/appsync_resolver_event.py` & `aws_lambda_powertools-2.9.1/aws_lambda_powertools/utilities/data_classes/appsync_resolver_event.py`

 * *Files identical despite different names*

### Comparing `aws_lambda_powertools-2.9.0/aws_lambda_powertools/utilities/data_classes/cloud_watch_custom_widget_event.py` & `aws_lambda_powertools-2.9.1/aws_lambda_powertools/utilities/data_classes/cloud_watch_custom_widget_event.py`

 * *Files identical despite different names*

### Comparing `aws_lambda_powertools-2.9.0/aws_lambda_powertools/utilities/data_classes/cloud_watch_logs_event.py` & `aws_lambda_powertools-2.9.1/aws_lambda_powertools/utilities/data_classes/cloud_watch_logs_event.py`

 * *Files identical despite different names*

### Comparing `aws_lambda_powertools-2.9.0/aws_lambda_powertools/utilities/data_classes/code_pipeline_job_event.py` & `aws_lambda_powertools-2.9.1/aws_lambda_powertools/utilities/data_classes/code_pipeline_job_event.py`

 * *Files identical despite different names*

### Comparing `aws_lambda_powertools-2.9.0/aws_lambda_powertools/utilities/data_classes/cognito_user_pool_event.py` & `aws_lambda_powertools-2.9.1/aws_lambda_powertools/utilities/data_classes/cognito_user_pool_event.py`

 * *Files identical despite different names*

### Comparing `aws_lambda_powertools-2.9.0/aws_lambda_powertools/utilities/data_classes/common.py` & `aws_lambda_powertools-2.9.1/aws_lambda_powertools/utilities/data_classes/common.py`

 * *Files identical despite different names*

### Comparing `aws_lambda_powertools-2.9.0/aws_lambda_powertools/utilities/data_classes/connect_contact_flow_event.py` & `aws_lambda_powertools-2.9.1/aws_lambda_powertools/utilities/data_classes/connect_contact_flow_event.py`

 * *Files identical despite different names*

### Comparing `aws_lambda_powertools-2.9.0/aws_lambda_powertools/utilities/data_classes/dynamo_db_stream_event.py` & `aws_lambda_powertools-2.9.1/aws_lambda_powertools/utilities/data_classes/dynamo_db_stream_event.py`

 * *Files identical despite different names*

### Comparing `aws_lambda_powertools-2.9.0/aws_lambda_powertools/utilities/data_classes/event_bridge_event.py` & `aws_lambda_powertools-2.9.1/aws_lambda_powertools/utilities/data_classes/event_bridge_event.py`

 * *Files identical despite different names*

### Comparing `aws_lambda_powertools-2.9.0/aws_lambda_powertools/utilities/data_classes/event_source.py` & `aws_lambda_powertools-2.9.1/aws_lambda_powertools/utilities/data_classes/event_source.py`

 * *Files identical despite different names*

### Comparing `aws_lambda_powertools-2.9.0/aws_lambda_powertools/utilities/data_classes/kafka_event.py` & `aws_lambda_powertools-2.9.1/aws_lambda_powertools/utilities/data_classes/kafka_event.py`

 * *Files identical despite different names*

### Comparing `aws_lambda_powertools-2.9.0/aws_lambda_powertools/utilities/data_classes/kinesis_firehose_event.py` & `aws_lambda_powertools-2.9.1/aws_lambda_powertools/utilities/data_classes/kinesis_firehose_event.py`

 * *Files identical despite different names*

### Comparing `aws_lambda_powertools-2.9.0/aws_lambda_powertools/utilities/data_classes/kinesis_stream_event.py` & `aws_lambda_powertools-2.9.1/aws_lambda_powertools/utilities/data_classes/kinesis_stream_event.py`

 * *Files identical despite different names*

### Comparing `aws_lambda_powertools-2.9.0/aws_lambda_powertools/utilities/data_classes/lambda_function_url_event.py` & `aws_lambda_powertools-2.9.1/aws_lambda_powertools/utilities/data_classes/lambda_function_url_event.py`

 * *Files identical despite different names*

### Comparing `aws_lambda_powertools-2.9.0/aws_lambda_powertools/utilities/data_classes/rabbit_mq_event.py` & `aws_lambda_powertools-2.9.1/aws_lambda_powertools/utilities/data_classes/rabbit_mq_event.py`

 * *Files identical despite different names*

### Comparing `aws_lambda_powertools-2.9.0/aws_lambda_powertools/utilities/data_classes/s3_event.py` & `aws_lambda_powertools-2.9.1/aws_lambda_powertools/utilities/data_classes/s3_event.py`

 * *Files identical despite different names*

### Comparing `aws_lambda_powertools-2.9.0/aws_lambda_powertools/utilities/data_classes/s3_object_event.py` & `aws_lambda_powertools-2.9.1/aws_lambda_powertools/utilities/data_classes/s3_object_event.py`

 * *Files identical despite different names*

### Comparing `aws_lambda_powertools-2.9.0/aws_lambda_powertools/utilities/data_classes/ses_event.py` & `aws_lambda_powertools-2.9.1/aws_lambda_powertools/utilities/data_classes/ses_event.py`

 * *Files identical despite different names*

### Comparing `aws_lambda_powertools-2.9.0/aws_lambda_powertools/utilities/data_classes/sns_event.py` & `aws_lambda_powertools-2.9.1/aws_lambda_powertools/utilities/data_classes/sns_event.py`

 * *Files identical despite different names*

### Comparing `aws_lambda_powertools-2.9.0/aws_lambda_powertools/utilities/data_classes/sqs_event.py` & `aws_lambda_powertools-2.9.1/aws_lambda_powertools/utilities/data_classes/sqs_event.py`

 * *Files identical despite different names*

### Comparing `aws_lambda_powertools-2.9.0/aws_lambda_powertools/utilities/feature_flags/appconfig.py` & `aws_lambda_powertools-2.9.1/aws_lambda_powertools/utilities/feature_flags/appconfig.py`

 * *Files identical despite different names*

### Comparing `aws_lambda_powertools-2.9.0/aws_lambda_powertools/utilities/feature_flags/base.py` & `aws_lambda_powertools-2.9.1/aws_lambda_powertools/utilities/feature_flags/base.py`

 * *Files identical despite different names*

### Comparing `aws_lambda_powertools-2.9.0/aws_lambda_powertools/utilities/feature_flags/feature_flags.py` & `aws_lambda_powertools-2.9.1/aws_lambda_powertools/utilities/feature_flags/feature_flags.py`

 * *Files identical despite different names*

### Comparing `aws_lambda_powertools-2.9.0/aws_lambda_powertools/utilities/feature_flags/schema.py` & `aws_lambda_powertools-2.9.1/aws_lambda_powertools/utilities/feature_flags/schema.py`

 * *Files identical despite different names*

### Comparing `aws_lambda_powertools-2.9.0/aws_lambda_powertools/utilities/feature_flags/time_conditions.py` & `aws_lambda_powertools-2.9.1/aws_lambda_powertools/utilities/feature_flags/time_conditions.py`

 * *Files identical despite different names*

### Comparing `aws_lambda_powertools-2.9.0/aws_lambda_powertools/utilities/idempotency/base.py` & `aws_lambda_powertools-2.9.1/aws_lambda_powertools/utilities/idempotency/base.py`

 * *Files identical despite different names*

### Comparing `aws_lambda_powertools-2.9.0/aws_lambda_powertools/utilities/idempotency/config.py` & `aws_lambda_powertools-2.9.1/aws_lambda_powertools/utilities/idempotency/config.py`

 * *Files identical despite different names*

### Comparing `aws_lambda_powertools-2.9.0/aws_lambda_powertools/utilities/idempotency/exceptions.py` & `aws_lambda_powertools-2.9.1/aws_lambda_powertools/utilities/idempotency/exceptions.py`

 * *Files identical despite different names*

### Comparing `aws_lambda_powertools-2.9.0/aws_lambda_powertools/utilities/idempotency/idempotency.py` & `aws_lambda_powertools-2.9.1/aws_lambda_powertools/utilities/idempotency/idempotency.py`

 * *Files identical despite different names*

### Comparing `aws_lambda_powertools-2.9.0/aws_lambda_powertools/utilities/idempotency/persistence/base.py` & `aws_lambda_powertools-2.9.1/aws_lambda_powertools/utilities/idempotency/persistence/base.py`

 * *Files identical despite different names*

### Comparing `aws_lambda_powertools-2.9.0/aws_lambda_powertools/utilities/idempotency/persistence/dynamodb.py` & `aws_lambda_powertools-2.9.1/aws_lambda_powertools/utilities/idempotency/persistence/dynamodb.py`

 * *Files 2% similar despite different names*

```diff
@@ -100,14 +100,29 @@
         self.validation_key_attr = validation_key_attr
 
         self._deserializer = TypeDeserializer()
 
         super(DynamoDBPersistenceLayer, self).__init__()
 
     def _get_key(self, idempotency_key: str) -> dict:
+        """Build primary key attribute simple or composite based on params.
+
+        When sort_key_attr is set, we must return a composite key with static_pk_value,
+        otherwise we use the idempotency key given.
+
+        Parameters
+        ----------
+        idempotency_key : str
+            idempotency key to use for simple primary key
+
+        Returns
+        -------
+        dict
+            simple or composite key for DynamoDB primary key
+        """
         if self.sort_key_attr:
             return {self.key_attr: {"S": self.static_pk_value}, self.sort_key_attr: {"S": idempotency_key}}
         return {self.key_attr: {"S": idempotency_key}}
 
     def _item_to_data_record(self, item: Dict[str, Any]) -> DataRecord:
         """
         Translate raw item records from DynamoDB to DataRecord
@@ -141,16 +156,16 @@
             item = response["Item"]
         except KeyError as exc:
             raise IdempotencyItemNotFoundError from exc
         return self._item_to_data_record(item)
 
     def _put_record(self, data_record: DataRecord) -> None:
         item = {
+            # get simple or composite primary key
             **self._get_key(data_record.idempotency_key),
-            self.key_attr: {"S": data_record.idempotency_key},
             self.expiry_attr: {"N": str(data_record.expiry_timestamp)},
             self.status_attr: {"S": data_record.status},
         }
 
         if data_record.in_progress_expiry_timestamp is not None:
             item[self.in_progress_expiry_attr] = {"N": str(data_record.in_progress_expiry_timestamp)}
```

### Comparing `aws_lambda_powertools-2.9.0/aws_lambda_powertools/utilities/jmespath_utils/__init__.py` & `aws_lambda_powertools-2.9.1/aws_lambda_powertools/utilities/jmespath_utils/__init__.py`

 * *Files identical despite different names*

### Comparing `aws_lambda_powertools-2.9.0/aws_lambda_powertools/utilities/parameters/__init__.py` & `aws_lambda_powertools-2.9.1/aws_lambda_powertools/utilities/parameters/__init__.py`

 * *Files identical despite different names*

### Comparing `aws_lambda_powertools-2.9.0/aws_lambda_powertools/utilities/parameters/appconfig.py` & `aws_lambda_powertools-2.9.1/aws_lambda_powertools/utilities/parameters/appconfig.py`

 * *Files identical despite different names*

### Comparing `aws_lambda_powertools-2.9.0/aws_lambda_powertools/utilities/parameters/base.py` & `aws_lambda_powertools-2.9.1/aws_lambda_powertools/utilities/parameters/base.py`

 * *Files identical despite different names*

### Comparing `aws_lambda_powertools-2.9.0/aws_lambda_powertools/utilities/parameters/dynamodb.py` & `aws_lambda_powertools-2.9.1/aws_lambda_powertools/utilities/parameters/dynamodb.py`

 * *Files identical despite different names*

### Comparing `aws_lambda_powertools-2.9.0/aws_lambda_powertools/utilities/parameters/secrets.py` & `aws_lambda_powertools-2.9.1/aws_lambda_powertools/utilities/parameters/secrets.py`

 * *Files identical despite different names*

### Comparing `aws_lambda_powertools-2.9.0/aws_lambda_powertools/utilities/parameters/ssm.py` & `aws_lambda_powertools-2.9.1/aws_lambda_powertools/utilities/parameters/ssm.py`

 * *Files identical despite different names*

### Comparing `aws_lambda_powertools-2.9.0/aws_lambda_powertools/utilities/parser/envelopes/__init__.py` & `aws_lambda_powertools-2.9.1/aws_lambda_powertools/utilities/parser/envelopes/__init__.py`

 * *Files identical despite different names*

### Comparing `aws_lambda_powertools-2.9.0/aws_lambda_powertools/utilities/parser/envelopes/apigw.py` & `aws_lambda_powertools-2.9.1/aws_lambda_powertools/utilities/parser/envelopes/apigw.py`

 * *Files identical despite different names*

### Comparing `aws_lambda_powertools-2.9.0/aws_lambda_powertools/utilities/parser/envelopes/apigwv2.py` & `aws_lambda_powertools-2.9.1/aws_lambda_powertools/utilities/parser/envelopes/apigwv2.py`

 * *Files identical despite different names*

### Comparing `aws_lambda_powertools-2.9.0/aws_lambda_powertools/utilities/parser/envelopes/base.py` & `aws_lambda_powertools-2.9.1/aws_lambda_powertools/utilities/parser/envelopes/base.py`

 * *Files identical despite different names*

### Comparing `aws_lambda_powertools-2.9.0/aws_lambda_powertools/utilities/parser/envelopes/cloudwatch.py` & `aws_lambda_powertools-2.9.1/aws_lambda_powertools/utilities/parser/envelopes/cloudwatch.py`

 * *Files identical despite different names*

### Comparing `aws_lambda_powertools-2.9.0/aws_lambda_powertools/utilities/parser/envelopes/dynamodb.py` & `aws_lambda_powertools-2.9.1/aws_lambda_powertools/utilities/parser/envelopes/dynamodb.py`

 * *Files identical despite different names*

### Comparing `aws_lambda_powertools-2.9.0/aws_lambda_powertools/utilities/parser/envelopes/event_bridge.py` & `aws_lambda_powertools-2.9.1/aws_lambda_powertools/utilities/parser/envelopes/event_bridge.py`

 * *Files identical despite different names*

### Comparing `aws_lambda_powertools-2.9.0/aws_lambda_powertools/utilities/parser/envelopes/kafka.py` & `aws_lambda_powertools-2.9.1/aws_lambda_powertools/utilities/parser/envelopes/kafka.py`

 * *Files identical despite different names*

### Comparing `aws_lambda_powertools-2.9.0/aws_lambda_powertools/utilities/parser/envelopes/kinesis.py` & `aws_lambda_powertools-2.9.1/aws_lambda_powertools/utilities/parser/envelopes/kinesis.py`

 * *Files identical despite different names*

### Comparing `aws_lambda_powertools-2.9.0/aws_lambda_powertools/utilities/parser/envelopes/kinesis_firehose.py` & `aws_lambda_powertools-2.9.1/aws_lambda_powertools/utilities/parser/envelopes/kinesis_firehose.py`

 * *Files identical despite different names*

### Comparing `aws_lambda_powertools-2.9.0/aws_lambda_powertools/utilities/parser/envelopes/lambda_function_url.py` & `aws_lambda_powertools-2.9.1/aws_lambda_powertools/utilities/parser/envelopes/lambda_function_url.py`

 * *Files identical despite different names*

### Comparing `aws_lambda_powertools-2.9.0/aws_lambda_powertools/utilities/parser/envelopes/sns.py` & `aws_lambda_powertools-2.9.1/aws_lambda_powertools/utilities/parser/envelopes/sns.py`

 * *Files identical despite different names*

### Comparing `aws_lambda_powertools-2.9.0/aws_lambda_powertools/utilities/parser/envelopes/sqs.py` & `aws_lambda_powertools-2.9.1/aws_lambda_powertools/utilities/parser/envelopes/sqs.py`

 * *Files identical despite different names*

### Comparing `aws_lambda_powertools-2.9.0/aws_lambda_powertools/utilities/parser/models/__init__.py` & `aws_lambda_powertools-2.9.1/aws_lambda_powertools/utilities/parser/models/__init__.py`

 * *Files identical despite different names*

### Comparing `aws_lambda_powertools-2.9.0/aws_lambda_powertools/utilities/parser/models/apigw.py` & `aws_lambda_powertools-2.9.1/aws_lambda_powertools/utilities/parser/models/apigw.py`

 * *Files 22% similar despite different names*

```diff
@@ -27,15 +27,17 @@
     apiKeyId: Optional[str]
     caller: Optional[str]
     cognitoAuthenticationProvider: Optional[str]
     cognitoAuthenticationType: Optional[str]
     cognitoIdentityId: Optional[str]
     cognitoIdentityPoolId: Optional[str]
     principalOrgId: Optional[str]
-    sourceIp: IPvAnyNetwork
+    # see #1562, temp workaround until API Gateway fixes it the Test button payload
+    # removing it will not be considered a regression in the future
+    sourceIp: Union[IPvAnyNetwork, Literal["test-invoke-source-ip"]]
     user: Optional[str]
     userAgent: Optional[str]
     userArn: Optional[str]
     clientCert: Optional[ApiGatewayUserCert]
 
 
 class APIGatewayEventAuthorizer(BaseModel):
```

### Comparing `aws_lambda_powertools-2.9.0/aws_lambda_powertools/utilities/parser/models/apigwv2.py` & `aws_lambda_powertools-2.9.1/aws_lambda_powertools/utilities/parser/models/apigwv2.py`

 * *Files identical despite different names*

### Comparing `aws_lambda_powertools-2.9.0/aws_lambda_powertools/utilities/parser/models/cloudwatch.py` & `aws_lambda_powertools-2.9.1/aws_lambda_powertools/utilities/parser/models/cloudwatch.py`

 * *Files identical despite different names*

### Comparing `aws_lambda_powertools-2.9.0/aws_lambda_powertools/utilities/parser/models/dynamodb.py` & `aws_lambda_powertools-2.9.1/aws_lambda_powertools/utilities/parser/models/dynamodb.py`

 * *Files identical despite different names*

### Comparing `aws_lambda_powertools-2.9.0/aws_lambda_powertools/utilities/parser/models/kafka.py` & `aws_lambda_powertools-2.9.1/aws_lambda_powertools/utilities/parser/models/kafka.py`

 * *Files identical despite different names*

### Comparing `aws_lambda_powertools-2.9.0/aws_lambda_powertools/utilities/parser/models/kinesis.py` & `aws_lambda_powertools-2.9.1/aws_lambda_powertools/utilities/parser/models/kinesis.py`

 * *Files identical despite different names*

### Comparing `aws_lambda_powertools-2.9.0/aws_lambda_powertools/utilities/parser/models/kinesis_firehose.py` & `aws_lambda_powertools-2.9.1/aws_lambda_powertools/utilities/parser/models/kinesis_firehose.py`

 * *Files identical despite different names*

### Comparing `aws_lambda_powertools-2.9.0/aws_lambda_powertools/utilities/parser/models/lambda_function_url.py` & `aws_lambda_powertools-2.9.1/aws_lambda_powertools/utilities/parser/models/lambda_function_url.py`

 * *Files identical despite different names*

### Comparing `aws_lambda_powertools-2.9.0/aws_lambda_powertools/utilities/parser/models/s3.py` & `aws_lambda_powertools-2.9.1/aws_lambda_powertools/utilities/parser/models/s3.py`

 * *Files identical despite different names*

### Comparing `aws_lambda_powertools-2.9.0/aws_lambda_powertools/utilities/parser/models/s3_object_event.py` & `aws_lambda_powertools-2.9.1/aws_lambda_powertools/utilities/parser/models/s3_object_event.py`

 * *Files identical despite different names*

### Comparing `aws_lambda_powertools-2.9.0/aws_lambda_powertools/utilities/parser/models/ses.py` & `aws_lambda_powertools-2.9.1/aws_lambda_powertools/utilities/parser/models/ses.py`

 * *Files identical despite different names*

### Comparing `aws_lambda_powertools-2.9.0/aws_lambda_powertools/utilities/parser/models/sns.py` & `aws_lambda_powertools-2.9.1/aws_lambda_powertools/utilities/parser/models/sns.py`

 * *Files identical despite different names*

### Comparing `aws_lambda_powertools-2.9.0/aws_lambda_powertools/utilities/parser/models/sqs.py` & `aws_lambda_powertools-2.9.1/aws_lambda_powertools/utilities/parser/models/sqs.py`

 * *Files identical despite different names*

### Comparing `aws_lambda_powertools-2.9.0/aws_lambda_powertools/utilities/parser/parser.py` & `aws_lambda_powertools-2.9.1/aws_lambda_powertools/utilities/parser/parser.py`

 * *Files identical despite different names*

### Comparing `aws_lambda_powertools-2.9.0/aws_lambda_powertools/utilities/parser/pydantic.py` & `aws_lambda_powertools-2.9.1/aws_lambda_powertools/utilities/parser/pydantic.py`

 * *Files identical despite different names*

### Comparing `aws_lambda_powertools-2.9.0/aws_lambda_powertools/utilities/streaming/_s3_seekable_io.py` & `aws_lambda_powertools-2.9.1/aws_lambda_powertools/utilities/streaming/_s3_seekable_io.py`

 * *Files identical despite different names*

### Comparing `aws_lambda_powertools-2.9.0/aws_lambda_powertools/utilities/streaming/compat.py` & `aws_lambda_powertools-2.9.1/aws_lambda_powertools/utilities/streaming/compat.py`

 * *Files identical despite different names*

### Comparing `aws_lambda_powertools-2.9.0/aws_lambda_powertools/utilities/streaming/s3_object.py` & `aws_lambda_powertools-2.9.1/aws_lambda_powertools/utilities/streaming/s3_object.py`

 * *Files identical despite different names*

### Comparing `aws_lambda_powertools-2.9.0/aws_lambda_powertools/utilities/streaming/transformations/base.py` & `aws_lambda_powertools-2.9.1/aws_lambda_powertools/utilities/streaming/transformations/base.py`

 * *Files identical despite different names*

### Comparing `aws_lambda_powertools-2.9.0/aws_lambda_powertools/utilities/streaming/transformations/csv.py` & `aws_lambda_powertools-2.9.1/aws_lambda_powertools/utilities/streaming/transformations/csv.py`

 * *Files identical despite different names*

### Comparing `aws_lambda_powertools-2.9.0/aws_lambda_powertools/utilities/streaming/transformations/gzip.py` & `aws_lambda_powertools-2.9.1/aws_lambda_powertools/utilities/streaming/transformations/gzip.py`

 * *Files identical despite different names*

### Comparing `aws_lambda_powertools-2.9.0/aws_lambda_powertools/utilities/streaming/transformations/zip.py` & `aws_lambda_powertools-2.9.1/aws_lambda_powertools/utilities/streaming/transformations/zip.py`

 * *Files identical despite different names*

### Comparing `aws_lambda_powertools-2.9.0/aws_lambda_powertools/utilities/typing/lambda_client_context.py` & `aws_lambda_powertools-2.9.1/aws_lambda_powertools/utilities/typing/lambda_client_context.py`

 * *Files identical despite different names*

### Comparing `aws_lambda_powertools-2.9.0/aws_lambda_powertools/utilities/typing/lambda_client_context_mobile_client.py` & `aws_lambda_powertools-2.9.1/aws_lambda_powertools/utilities/typing/lambda_client_context_mobile_client.py`

 * *Files identical despite different names*

### Comparing `aws_lambda_powertools-2.9.0/aws_lambda_powertools/utilities/typing/lambda_cognito_identity.py` & `aws_lambda_powertools-2.9.1/aws_lambda_powertools/utilities/typing/lambda_cognito_identity.py`

 * *Files identical despite different names*

### Comparing `aws_lambda_powertools-2.9.0/aws_lambda_powertools/utilities/typing/lambda_context.py` & `aws_lambda_powertools-2.9.1/aws_lambda_powertools/utilities/typing/lambda_context.py`

 * *Files identical despite different names*

### Comparing `aws_lambda_powertools-2.9.0/aws_lambda_powertools/utilities/validation/base.py` & `aws_lambda_powertools-2.9.1/aws_lambda_powertools/utilities/validation/base.py`

 * *Files identical despite different names*

### Comparing `aws_lambda_powertools-2.9.0/aws_lambda_powertools/utilities/validation/exceptions.py` & `aws_lambda_powertools-2.9.1/aws_lambda_powertools/utilities/validation/exceptions.py`

 * *Files identical despite different names*

### Comparing `aws_lambda_powertools-2.9.0/aws_lambda_powertools/utilities/validation/validator.py` & `aws_lambda_powertools-2.9.1/aws_lambda_powertools/utilities/validation/validator.py`

 * *Files identical despite different names*

### Comparing `aws_lambda_powertools-2.9.0/pyproject.toml` & `aws_lambda_powertools-2.9.1/pyproject.toml`

 * *Files 4% similar despite different names*

```diff
@@ -1,11 +1,11 @@
 [tool.poetry]
 name = "aws_lambda_powertools"
-version = "2.9.0"
-description = "A suite of utilities for AWS Lambda functions to ease adopting best practices such as tracing, structured logging, custom metrics, batching, idempotency, feature flags, and more."
+version = "2.9.1"
+description = "AWS Lambda Powertools is a developer toolkit to implement Serverless best practices and increase developer velocity."
 authors = ["Amazon Web Services"]
 include = ["aws_lambda_powertools/py.typed", "THIRD-PARTY-LICENSES"]
 classifiers=[
     "Development Status :: 5 - Production/Stable",
     "Intended Audience :: Developers",
     "License :: OSI Approved :: MIT No Attribution License (MIT-0)",
     "Natural Language :: English",
@@ -30,15 +30,15 @@
 aws-xray-sdk = { version = "^2.8.0", optional = true }
 fastjsonschema = { version = "^2.14.5", optional = true }
 pydantic = { version = "^1.8.2", optional = true }
 boto3 = { version = "^1.20.32", optional = true }
 typing-extensions = "^4.4.0"
 
 [tool.poetry.dev-dependencies]
-coverage = {extras = ["toml"], version = "^7.1"}
+coverage = {extras = ["toml"], version = "^7.2"}
 pytest = "^7.2.1"
 black = "^23.1"
 boto3 = "^1.18"
 flake8 = [
   # https://github.com/python/importlib_metadata/issues/406
   { version = "*", python="^3.7" },
   { version = ">=5", python= ">=3.8"},
@@ -59,33 +59,33 @@
 xenon = "^0.9.0"
 flake8-eradicate = "^1.2.1"
 flake8-bugbear = "^23.2.13"
 mkdocs-git-revision-date-plugin = "^0.3.2"
 mike = "^1.1.2"
 retry = "^0.9.2"
 pytest-xdist = "^3.2.0"
-aws-cdk-lib = "^2.65.0"
+aws-cdk-lib = "^2.66.1"
 "aws-cdk.aws-apigatewayv2-alpha" = "^2.38.1-alpha.0"
 "aws-cdk.aws-apigatewayv2-integrations-alpha" = "^2.38.1-alpha.0"
 "aws-cdk.aws-apigatewayv2-authorizers-alpha" = "^2.38.1-alpha.0"
 pytest-benchmark = "^4.0.0"
 python-snappy = "^0.6.1"
 mypy-boto3-appconfig = "^1.26.71"
 mypy-boto3-cloudformation = "^1.26.57"
 mypy-boto3-cloudwatch = "^1.26.52"
 mypy-boto3-dynamodb = "^1.26.24"
-mypy-boto3-lambda = "^1.26.55"
+mypy-boto3-lambda = "^1.26.80"
 mypy-boto3-logs = "^1.26.53"
 mypy-boto3-secretsmanager = "^1.26.49"
-mypy-boto3-ssm = "^1.26.43"
+mypy-boto3-ssm = "^1.26.77"
 mypy-boto3-s3 = "^1.26.62"
 mypy-boto3-xray = "^1.26.11"
 types-requests = "^2.28.11"
 typing-extensions = "^4.4.0"
-mkdocs-material = "^9.0.13"
+mkdocs-material = "^9.0.15"
 filelock = "^3.9.0"
 checksumdir = "^1.2.0"
 mypy-boto3-appconfigdata = "^1.26.70"
 importlib-metadata = "^6.0"
 ijson = "^3.2.0"
 typed-ast = { version = "^1.5.4", python = "< 3.8"}
 hvac = "^1.0.2"
```

### Comparing `aws_lambda_powertools-2.9.0/setup.py` & `aws_lambda_powertools-2.9.1/PKG-INFO`

 * *Files 24% similar despite different names*

```diff
@@ -1,63 +1,103 @@
-# -*- coding: utf-8 -*-
-from setuptools import setup
+Metadata-Version: 2.1
+Name: aws-lambda-powertools
+Version: 2.9.1
+Summary: AWS Lambda Powertools is a developer toolkit to implement Serverless best practices and increase developer velocity.
+Home-page: https://github.com/awslabs/aws-lambda-powertools-python
+License: MIT
+Keywords: aws_lambda_powertools,aws,tracing,logging,lambda,powertools,feature_flags,idempotency,middleware
+Author: Amazon Web Services
+Requires-Python: >=3.7.4,<4.0.0
+Classifier: Development Status :: 5 - Production/Stable
+Classifier: Intended Audience :: Developers
+Classifier: License :: OSI Approved :: MIT License
+Classifier: License :: OSI Approved :: MIT No Attribution License (MIT-0)
+Classifier: Natural Language :: English
+Classifier: Programming Language :: Python :: 3
+Classifier: Programming Language :: Python :: 3.8
+Classifier: Programming Language :: Python :: 3.9
+Classifier: Programming Language :: Python :: 3.10
+Classifier: Programming Language :: Python :: 3.11
+Classifier: Programming Language :: Python :: 3.7
+Classifier: Programming Language :: Python :: 3.8
+Classifier: Programming Language :: Python :: 3.9
+Provides-Extra: all
+Provides-Extra: aws-sdk
+Provides-Extra: parser
+Provides-Extra: tracer
+Provides-Extra: validation
+Requires-Dist: aws-xray-sdk (>=2.8.0,<3.0.0) ; extra == "tracer" or extra == "all"
+Requires-Dist: boto3 (>=1.20.32,<2.0.0) ; extra == "aws-sdk"
+Requires-Dist: fastjsonschema (>=2.14.5,<3.0.0) ; extra == "validation" or extra == "all"
+Requires-Dist: pydantic (>=1.8.2,<2.0.0) ; extra == "parser" or extra == "all"
+Requires-Dist: typing-extensions (>=4.4.0,<5.0.0)
+Project-URL: Documentation, https://awslabs.github.io/aws-lambda-powertools-python/
+Project-URL: Issue tracker, https://github.com/awslabs/aws-lambda-powertools-python/issues
+Project-URL: Repository, https://github.com/awslabs/aws-lambda-powertools-python
+Project-URL: Releases, https://github.com/awslabs/aws-lambda-powertools-python/releases
+Description-Content-Type: text/markdown
+
+<!-- markdownlint-disable MD013 MD041 MD043  -->
+# AWS Lambda Powertools for Python
+
+[![Build](https://github.com/awslabs/aws-lambda-powertools-python/actions/workflows/python_build.yml/badge.svg)](https://github.com/awslabs/aws-lambda-powertools-python/actions/workflows/python_build.yml)
+[![codecov.io](https://codecov.io/github/awslabs/aws-lambda-powertools-python/branch/develop/graphs/badge.svg)](https://app.codecov.io/gh/awslabs/aws-lambda-powertools-python)
+![PythonSupport](https://img.shields.io/static/v1?label=python&message=%203.7|%203.8|%203.9&color=blue?style=flat-square&logo=python) ![PyPI version](https://badge.fury.io/py/aws-lambda-powertools.svg) ![PyPi monthly downloads](https://img.shields.io/pypi/dm/aws-lambda-powertools) [![Join our Discord](https://dcbadge.vercel.app/api/server/B8zZKbbyET)](https://discord.gg/B8zZKbbyET)
+
+Powertools is a developer toolkit to implement Serverless [best practices and increase developer velocity](https://awslabs.github.io/aws-lambda-powertools-python/latest/#features).
+
+> Also available in [Java](https://github.com/awslabs/aws-lambda-powertools-java), [Typescript](https://github.com/awslabs/aws-lambda-powertools-typescript), and [.NET](https://awslabs.github.io/aws-lambda-powertools-dotnet/).
+
+**[📜Documentation](https://awslabs.github.io/aws-lambda-powertools-python/)** | **[🐍PyPi](https://pypi.org/project/aws-lambda-powertools/)** | **[Roadmap](https://awslabs.github.io/aws-lambda-powertools-python/latest/roadmap/)** | **[Detailed blog post](https://aws.amazon.com/blogs/opensource/simplifying-serverless-best-practices-with-lambda-powertools/)**
+
+> **An AWS Developer Acceleration (DevAx) initiative by Specialist Solution Architects | aws-devax-open-source@amazon.com**
+
+![hero-image](https://user-images.githubusercontent.com/3340292/198254617-d0fdb672-86a6-4988-8a40-adf437135e0a.png)
+
+## Features
+
+* **[Tracing](https://awslabs.github.io/aws-lambda-powertools-python/latest/core/tracer/)** - Decorators and utilities to trace Lambda function handlers, and both synchronous and asynchronous functions
+* **[Logging](https://awslabs.github.io/aws-lambda-powertools-python/latest/core/logger/)** - Structured logging made easier, and decorator to enrich structured logging with key Lambda context details
+* **[Metrics](https://awslabs.github.io/aws-lambda-powertools-python/latest/core/metrics/)** - Custom Metrics created asynchronously via CloudWatch Embedded Metric Format (EMF)
+* **[Event handler: AppSync](https://awslabs.github.io/aws-lambda-powertools-python/latest/core/event_handler/appsync/)** - AWS AppSync event handler for Lambda Direct Resolver and Amplify GraphQL Transformer function
+* **[Event handler: API Gateway and ALB](https://awslabs.github.io/aws-lambda-powertools-python/latest/core/event_handler/api_gateway/)** - Amazon API Gateway REST/HTTP API and ALB event handler for Lambda functions invoked using Proxy integration
+* **[Bring your own middleware](https://awslabs.github.io/aws-lambda-powertools-python/latest/utilities/middleware_factory/)** - Decorator factory to create your own middleware to run logic before, and after each Lambda invocation
+* **[Parameters utility](https://awslabs.github.io/aws-lambda-powertools-python/latest/utilities/parameters/)** - Retrieve and cache parameter values from Parameter Store, Secrets Manager, or DynamoDB
+* **[Batch processing](https://awslabs.github.io/aws-lambda-powertools-python/latest/utilities/batch/)** - Handle partial failures for AWS SQS batch processing
+* **[Typing](https://awslabs.github.io/aws-lambda-powertools-python/latest/utilities/typing/)** - Static typing classes to speedup development in your IDE
+* **[Validation](https://awslabs.github.io/aws-lambda-powertools-python/latest/utilities/validation/)** - JSON Schema validator for inbound events and responses
+* **[Event source data classes](https://awslabs.github.io/aws-lambda-powertools-python/latest/utilities/data_classes/)** - Data classes describing the schema of common Lambda event triggers
+* **[Parser](https://awslabs.github.io/aws-lambda-powertools-python/latest/utilities/parser/)** - Data parsing and deep validation using Pydantic
+* **[Idempotency](https://awslabs.github.io/aws-lambda-powertools-python/latest/utilities/idempotency/)** - Convert your Lambda functions into idempotent operations which are safe to retry
+* **[Feature Flags](https://awslabs.github.io/aws-lambda-powertools-python/latest/utilities/feature_flags/)** - A simple rule engine to evaluate when one or multiple features should be enabled depending on the input
+* **[Streaming](https://awslabs.github.io/aws-lambda-powertools-python/latest/utilities/streaming/)** - Streams datasets larger than the available memory as streaming data.
+
+### Installation
+
+With [pip](https://pip.pypa.io/en/latest/index.html) installed, run: ``pip install aws-lambda-powertools``
+
+## Tutorial and Examples
+
+* [Tutorial](https://awslabs.github.io/aws-lambda-powertools-python/latest/tutorial)
+* [Serverless Shopping cart](https://github.com/aws-samples/aws-serverless-shopping-cart)
+* [Serverless Airline](https://github.com/aws-samples/aws-serverless-airline-booking)
+* [Serverless E-commerce platform](https://github.com/aws-samples/aws-serverless-ecommerce-platform)
+* [Serverless GraphQL Nanny Booking Api](https://github.com/trey-rosius/babysitter_api)
+
+## Credits
+
+* Structured logging initial implementation from [aws-lambda-logging](https://gitlab.com/hadrien/aws_lambda_logging)
+* Powertools idea [DAZN Powertools](https://github.com/getndazn/dazn-lambda-powertools/)
+
+## Connect
+
+* **AWS Lambda Powertools on Discord**: `#python` - **[Invite link](https://discord.gg/B8zZKbbyET)**
+* **Email**: aws-lambda-powertools-feedback@amazon.com
 
-packages = \
-['aws_lambda_powertools',
- 'aws_lambda_powertools.event_handler',
- 'aws_lambda_powertools.exceptions',
- 'aws_lambda_powertools.logging',
- 'aws_lambda_powertools.metrics',
- 'aws_lambda_powertools.middleware_factory',
- 'aws_lambda_powertools.shared',
- 'aws_lambda_powertools.tracing',
- 'aws_lambda_powertools.utilities',
- 'aws_lambda_powertools.utilities.batch',
- 'aws_lambda_powertools.utilities.data_classes',
- 'aws_lambda_powertools.utilities.data_classes.appsync',
- 'aws_lambda_powertools.utilities.feature_flags',
- 'aws_lambda_powertools.utilities.idempotency',
- 'aws_lambda_powertools.utilities.idempotency.persistence',
- 'aws_lambda_powertools.utilities.jmespath_utils',
- 'aws_lambda_powertools.utilities.parameters',
- 'aws_lambda_powertools.utilities.parser',
- 'aws_lambda_powertools.utilities.parser.envelopes',
- 'aws_lambda_powertools.utilities.parser.models',
- 'aws_lambda_powertools.utilities.streaming',
- 'aws_lambda_powertools.utilities.streaming.transformations',
- 'aws_lambda_powertools.utilities.typing',
- 'aws_lambda_powertools.utilities.validation']
-
-package_data = \
-{'': ['*']}
-
-install_requires = \
-['typing-extensions>=4.4.0,<5.0.0']
-
-extras_require = \
-{'all': ['aws-xray-sdk>=2.8.0,<3.0.0',
-         'fastjsonschema>=2.14.5,<3.0.0',
-         'pydantic>=1.8.2,<2.0.0'],
- 'aws-sdk': ['boto3>=1.20.32,<2.0.0'],
- 'parser': ['pydantic>=1.8.2,<2.0.0'],
- 'tracer': ['aws-xray-sdk>=2.8.0,<3.0.0'],
- 'validation': ['fastjsonschema>=2.14.5,<3.0.0']}
-
-setup_kwargs = {
-    'name': 'aws-lambda-powertools',
-    'version': '2.9.0',
-    'description': 'A suite of utilities for AWS Lambda functions to ease adopting best practices such as tracing, structured logging, custom metrics, batching, idempotency, feature flags, and more.',
-    'long_description': '<!-- markdownlint-disable MD013 MD041 MD043  -->\n# AWS Lambda Powertools for Python\n\n[![Build](https://github.com/awslabs/aws-lambda-powertools-python/actions/workflows/python_build.yml/badge.svg)](https://github.com/awslabs/aws-lambda-powertools-python/actions/workflows/python_build.yml)\n[![codecov.io](https://codecov.io/github/awslabs/aws-lambda-powertools-python/branch/develop/graphs/badge.svg)](https://app.codecov.io/gh/awslabs/aws-lambda-powertools-python)\n![PythonSupport](https://img.shields.io/static/v1?label=python&message=%203.7|%203.8|%203.9&color=blue?style=flat-square&logo=python) ![PyPI version](https://badge.fury.io/py/aws-lambda-powertools.svg) ![PyPi monthly downloads](https://img.shields.io/pypi/dm/aws-lambda-powertools) [![Join our Discord](https://dcbadge.vercel.app/api/server/B8zZKbbyET)](https://discord.gg/B8zZKbbyET)\n\nPowertools is a developer toolkit to implement Serverless [best practices and increase developer velocity](https://awslabs.github.io/aws-lambda-powertools-python/latest/#features).\n\n> Also available in [Java](https://github.com/awslabs/aws-lambda-powertools-java), [Typescript](https://github.com/awslabs/aws-lambda-powertools-typescript), and [.NET](https://awslabs.github.io/aws-lambda-powertools-dotnet/).\n\n**[📜Documentation](https://awslabs.github.io/aws-lambda-powertools-python/)** | **[🐍PyPi](https://pypi.org/project/aws-lambda-powertools/)** | **[Roadmap](https://awslabs.github.io/aws-lambda-powertools-python/latest/roadmap/)** | **[Detailed blog post](https://aws.amazon.com/blogs/opensource/simplifying-serverless-best-practices-with-lambda-powertools/)**\n\n> **An AWS Developer Acceleration (DevAx) initiative by Specialist Solution Architects | aws-devax-open-source@amazon.com**\n\n![hero-image](https://user-images.githubusercontent.com/3340292/198254617-d0fdb672-86a6-4988-8a40-adf437135e0a.png)\n\n## Features\n\n* **[Tracing](https://awslabs.github.io/aws-lambda-powertools-python/latest/core/tracer/)** - Decorators and utilities to trace Lambda function handlers, and both synchronous and asynchronous functions\n* **[Logging](https://awslabs.github.io/aws-lambda-powertools-python/latest/core/logger/)** - Structured logging made easier, and decorator to enrich structured logging with key Lambda context details\n* **[Metrics](https://awslabs.github.io/aws-lambda-powertools-python/latest/core/metrics/)** - Custom Metrics created asynchronously via CloudWatch Embedded Metric Format (EMF)\n* **[Event handler: AppSync](https://awslabs.github.io/aws-lambda-powertools-python/latest/core/event_handler/appsync/)** - AWS AppSync event handler for Lambda Direct Resolver and Amplify GraphQL Transformer function\n* **[Event handler: API Gateway and ALB](https://awslabs.github.io/aws-lambda-powertools-python/latest/core/event_handler/api_gateway/)** - Amazon API Gateway REST/HTTP API and ALB event handler for Lambda functions invoked using Proxy integration\n* **[Bring your own middleware](https://awslabs.github.io/aws-lambda-powertools-python/latest/utilities/middleware_factory/)** - Decorator factory to create your own middleware to run logic before, and after each Lambda invocation\n* **[Parameters utility](https://awslabs.github.io/aws-lambda-powertools-python/latest/utilities/parameters/)** - Retrieve and cache parameter values from Parameter Store, Secrets Manager, or DynamoDB\n* **[Batch processing](https://awslabs.github.io/aws-lambda-powertools-python/latest/utilities/batch/)** - Handle partial failures for AWS SQS batch processing\n* **[Typing](https://awslabs.github.io/aws-lambda-powertools-python/latest/utilities/typing/)** - Static typing classes to speedup development in your IDE\n* **[Validation](https://awslabs.github.io/aws-lambda-powertools-python/latest/utilities/validation/)** - JSON Schema validator for inbound events and responses\n* **[Event source data classes](https://awslabs.github.io/aws-lambda-powertools-python/latest/utilities/data_classes/)** - Data classes describing the schema of common Lambda event triggers\n* **[Parser](https://awslabs.github.io/aws-lambda-powertools-python/latest/utilities/parser/)** - Data parsing and deep validation using Pydantic\n* **[Idempotency](https://awslabs.github.io/aws-lambda-powertools-python/latest/utilities/idempotency/)** - Convert your Lambda functions into idempotent operations which are safe to retry\n* **[Feature Flags](https://awslabs.github.io/aws-lambda-powertools-python/latest/utilities/feature_flags/)** - A simple rule engine to evaluate when one or multiple features should be enabled depending on the input\n* **[Streaming](https://awslabs.github.io/aws-lambda-powertools-python/latest/utilities/streaming/)** - Streams datasets larger than the available memory as streaming data.\n\n### Installation\n\nWith [pip](https://pip.pypa.io/en/latest/index.html) installed, run: ``pip install aws-lambda-powertools``\n\n## Tutorial and Examples\n\n* [Tutorial](https://awslabs.github.io/aws-lambda-powertools-python/latest/tutorial)\n* [Serverless Shopping cart](https://github.com/aws-samples/aws-serverless-shopping-cart)\n* [Serverless Airline](https://github.com/aws-samples/aws-serverless-airline-booking)\n* [Serverless E-commerce platform](https://github.com/aws-samples/aws-serverless-ecommerce-platform)\n* [Serverless GraphQL Nanny Booking Api](https://github.com/trey-rosius/babysitter_api)\n\n## Credits\n\n* Structured logging initial implementation from [aws-lambda-logging](https://gitlab.com/hadrien/aws_lambda_logging)\n* Powertools idea [DAZN Powertools](https://github.com/getndazn/dazn-lambda-powertools/)\n\n## Connect\n\n* **AWS Lambda Powertools on Discord**: `#python` - **[Invite link](https://discord.gg/B8zZKbbyET)**\n* **Email**: aws-lambda-powertools-feedback@amazon.com\n\n## Security disclosures\n\nIf you think you’ve found a potential security issue, please do not post it in the Issues.  Instead, please follow the instructions [here](https://aws.amazon.com/security/vulnerability-reporting/) or [email AWS security directly](mailto:aws-security@amazon.com).\n\n## License\n\nThis library is licensed under the MIT-0 License. See the LICENSE file.\n',
-    'author': 'Amazon Web Services',
-    'author_email': 'None',
-    'maintainer': 'None',
-    'maintainer_email': 'None',
-    'url': 'https://github.com/awslabs/aws-lambda-powertools-python',
-    'packages': packages,
-    'package_data': package_data,
-    'install_requires': install_requires,
-    'extras_require': extras_require,
-    'python_requires': '>=3.7.4,<4.0.0',
-}
+## Security disclosures
 
+If you think you’ve found a potential security issue, please do not post it in the Issues.  Instead, please follow the instructions [here](https://aws.amazon.com/security/vulnerability-reporting/) or [email AWS security directly](mailto:aws-security@amazon.com).
+
+## License
+
+This library is licensed under the MIT-0 License. See the LICENSE file.
 
-setup(**setup_kwargs)
```

