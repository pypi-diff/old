# Comparing `tmp/moto-4.1.7.dev8.tar.gz` & `tmp/moto-4.1.7.dev9.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "moto-4.1.7.dev8.tar", last modified: Tue Mar 28 19:17:53 2023, max compression
+gzip compressed data, was "moto-4.1.7.dev9.tar", last modified: Tue Mar 28 19:15:35 2023, max compression
```

## Comparing `moto-4.1.7.dev8.tar` & `moto-4.1.7.dev9.tar`

### file list

```diff
@@ -1,2042 +1,2042 @@
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:53.197519 moto-4.1.7.dev8/
--rw-r--r--   0 runner    (1001) docker     (123)     2976 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/AUTHORS.md
--rw-r--r--   0 runner    (1001) docker     (123)    10834 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/LICENSE
--rw-r--r--   0 runner    (1001) docker     (123)      919 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/MANIFEST.in
--rw-r--r--   0 runner    (1001) docker     (123)     6287 2023-03-28 19:17:53.197519 moto-4.1.7.dev8/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)     2512 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/README.md
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:52.745515 moto-4.1.7.dev8/moto/
--rw-r--r--   0 runner    (1001) docker     (123)     8775 2023-03-28 19:17:45.000000 moto-4.1.7.dev8/moto/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:52.749515 moto-4.1.7.dev8/moto/acm/
--rw-r--r--   0 runner    (1001) docker     (123)      155 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/acm/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      511 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/acm/exceptions.py
--rw-r--r--   0 runner    (1001) docker     (123)    21261 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/acm/models.py
--rw-r--r--   0 runner    (1001) docker     (123)     8771 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/acm/responses.py
--rw-r--r--   0 runner    (1001) docker     (123)      169 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/acm/urls.py
--rw-r--r--   0 runner    (1001) docker     (123)      313 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/acm/utils.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:52.749515 moto-4.1.7.dev8/moto/acmpca/
--rw-r--r--   0 runner    (1001) docker     (123)      191 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/acmpca/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      261 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/acmpca/exceptions.py
--rw-r--r--   0 runner    (1001) docker     (123)    12457 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/acmpca/models.py
--rw-r--r--   0 runner    (1001) docker     (123)     6712 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/acmpca/responses.py
--rw-r--r--   0 runner    (1001) docker     (123)      190 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/acmpca/urls.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:52.753515 moto-4.1.7.dev8/moto/amp/
--rw-r--r--   0 runner    (1001) docker     (123)      179 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/amp/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     1054 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/amp/exceptions.py
--rw-r--r--   0 runner    (1001) docker     (123)     7938 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/amp/models.py
--rw-r--r--   0 runner    (1001) docker     (123)     6717 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/amp/responses.py
--rw-r--r--   0 runner    (1001) docker     (123)      876 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/amp/urls.py
--rw-r--r--   0 runner    (1001) docker     (123)      476 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/amp/utils.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:52.753515 moto-4.1.7.dev8/moto/apigateway/
--rw-r--r--   0 runner    (1001) docker     (123)      190 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/apigateway/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     7520 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/apigateway/exceptions.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:52.753515 moto-4.1.7.dev8/moto/apigateway/integration_parsers/
--rw-r--r--   0 runner    (1001) docker     (123)      305 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/apigateway/integration_parsers/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     1371 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/apigateway/integration_parsers/aws_parser.py
--rw-r--r--   0 runner    (1001) docker     (123)      600 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/apigateway/integration_parsers/http_parser.py
--rw-r--r--   0 runner    (1001) docker     (123)      511 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/apigateway/integration_parsers/unknown_parser.py
--rw-r--r--   0 runner    (1001) docker     (123)    91746 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/apigateway/models.py
--rw-r--r--   0 runner    (1001) docker     (123)    40056 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/apigateway/responses.py
--rw-r--r--   0 runner    (1001) docker     (123)     3687 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/apigateway/urls.py
--rw-r--r--   0 runner    (1001) docker     (123)      607 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/apigateway/utils.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:52.753515 moto-4.1.7.dev8/moto/apigatewayv2/
--rw-r--r--   0 runner    (1001) docker     (123)      215 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/apigatewayv2/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     3040 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/apigatewayv2/exceptions.py
--rw-r--r--   0 runner    (1001) docker     (123)    64715 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/apigatewayv2/models.py
--rw-r--r--   0 runner    (1001) docker     (123)    36307 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/apigatewayv2/responses.py
--rw-r--r--   0 runner    (1001) docker     (123)     2415 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/apigatewayv2/urls.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:52.757515 moto-4.1.7.dev8/moto/applicationautoscaling/
--rw-r--r--   0 runner    (1001) docker     (123)      172 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/applicationautoscaling/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      197 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/applicationautoscaling/exceptions.py
--rw-r--r--   0 runner    (1001) docker     (123)    19977 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/applicationautoscaling/models.py
--rw-r--r--   0 runner    (1001) docker     (123)     9948 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/applicationautoscaling/responses.py
--rw-r--r--   0 runner    (1001) docker     (123)      197 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/applicationautoscaling/urls.py
--rw-r--r--   0 runner    (1001) docker     (123)      227 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/applicationautoscaling/utils.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:52.757515 moto-4.1.7.dev8/moto/appsync/
--rw-r--r--   0 runner    (1001) docker     (123)      195 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/appsync/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      357 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/appsync/exceptions.py
--rw-r--r--   0 runner    (1001) docker     (123)    11432 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/appsync/models.py
--rw-r--r--   0 runner    (1001) docker     (123)     9910 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/appsync/responses.py
--rw-r--r--   0 runner    (1001) docker     (123)      750 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/appsync/urls.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:52.757515 moto-4.1.7.dev8/moto/athena/
--rw-r--r--   0 runner    (1001) docker     (123)      170 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/athena/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      551 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/athena/exceptions.py
--rw-r--r--   0 runner    (1001) docker     (123)    12434 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/athena/models.py
--rw-r--r--   0 runner    (1001) docker     (123)     8425 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/athena/responses.py
--rw-r--r--   0 runner    (1001) docker     (123)      142 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/athena/urls.py
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/athena/utils.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:52.757515 moto-4.1.7.dev8/moto/autoscaling/
--rw-r--r--   0 runner    (1001) docker     (123)      195 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/autoscaling/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      718 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/autoscaling/exceptions.py
--rw-r--r--   0 runner    (1001) docker     (123)    61357 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/autoscaling/models.py
--rw-r--r--   0 runner    (1001) docker     (123)    65472 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/autoscaling/responses.py
--rw-r--r--   0 runner    (1001) docker     (123)      157 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/autoscaling/urls.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:52.761515 moto-4.1.7.dev8/moto/awslambda/
--rw-r--r--   0 runner    (1001) docker     (123)      170 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/awslambda/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     2126 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/awslambda/exceptions.py
--rw-r--r--   0 runner    (1001) docker     (123)    75083 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/awslambda/models.py
--rw-r--r--   0 runner    (1001) docker     (123)     6258 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/awslambda/policy.py
--rw-r--r--   0 runner    (1001) docker     (123)    23480 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/awslambda/responses.py
--rw-r--r--   0 runner    (1001) docker     (123)     2646 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/awslambda/urls.py
--rw-r--r--   0 runner    (1001) docker     (123)     1146 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/awslambda/utils.py
--rw-r--r--   0 runner    (1001) docker     (123)     9961 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/backend_index.py
--rw-r--r--   0 runner    (1001) docker     (123)     1805 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/backends.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:52.761515 moto-4.1.7.dev8/moto/batch/
--rw-r--r--   0 runner    (1001) docker     (123)      165 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/batch/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      433 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/batch/exceptions.py
--rw-r--r--   0 runner    (1001) docker     (123)    69404 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/batch/models.py
--rw-r--r--   0 runner    (1001) docker     (123)    10487 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/batch/responses.py
--rw-r--r--   0 runner    (1001) docker     (123)     1468 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/batch/urls.py
--rw-r--r--   0 runner    (1001) docker     (123)     1276 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/batch/utils.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:52.761515 moto-4.1.7.dev8/moto/batch_simple/
--rw-r--r--   0 runner    (1001) docker     (123)      193 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/batch_simple/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     2828 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/batch_simple/models.py
--rw-r--r--   0 runner    (1001) docker     (123)      377 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/batch_simple/responses.py
--rw-r--r--   0 runner    (1001) docker     (123)      258 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/batch_simple/urls.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:52.761515 moto-4.1.7.dev8/moto/budgets/
--rw-r--r--   0 runner    (1001) docker     (123)      127 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/budgets/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      901 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/budgets/exceptions.py
--rw-r--r--   0 runner    (1001) docker     (123)     5665 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/budgets/models.py
--rw-r--r--   0 runner    (1001) docker     (123)     2737 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/budgets/responses.py
--rw-r--r--   0 runner    (1001) docker     (123)      154 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/budgets/urls.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:52.765515 moto-4.1.7.dev8/moto/ce/
--rw-r--r--   0 runner    (1001) docker     (123)      175 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ce/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      294 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ce/exceptions.py
--rw-r--r--   0 runner    (1001) docker     (123)     5275 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ce/models.py
--rw-r--r--   0 runner    (1001) docker     (123)     3907 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ce/responses.py
--rw-r--r--   0 runner    (1001) docker     (123)      193 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ce/urls.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:52.765515 moto-4.1.7.dev8/moto/cloudformation/
--rw-r--r--   0 runner    (1001) docker     (123)      210 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/cloudformation/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     3450 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/cloudformation/custom_model.py
--rw-r--r--   0 runner    (1001) docker     (123)     2857 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/cloudformation/exceptions.py
--rw-r--r--   0 runner    (1001) docker     (123)    45880 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/cloudformation/models.py
--rw-r--r--   0 runner    (1001) docker     (123)    37479 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/cloudformation/parsing.py
--rw-r--r--   0 runner    (1001) docker     (123)    53038 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/cloudformation/responses.py
--rw-r--r--   0 runner    (1001) docker     (123)      266 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/cloudformation/urls.py
--rw-r--r--   0 runner    (1001) docker     (123)     3751 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/cloudformation/utils.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:52.765515 moto-4.1.7.dev8/moto/cloudfront/
--rw-r--r--   0 runner    (1001) docker     (123)      136 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/cloudfront/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     2202 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/cloudfront/exceptions.py
--rw-r--r--   0 runner    (1001) docker     (123)    14571 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/cloudfront/models.py
--rw-r--r--   0 runner    (1001) docker     (123)    30155 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/cloudfront/responses.py
--rw-r--r--   0 runner    (1001) docker     (123)      590 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/cloudfront/urls.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:52.765515 moto-4.1.7.dev8/moto/cloudtrail/
--rw-r--r--   0 runner    (1001) docker     (123)      207 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/cloudtrail/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     2203 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/cloudtrail/exceptions.py
--rw-r--r--   0 runner    (1001) docker     (123)    15598 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/cloudtrail/models.py
--rw-r--r--   0 runner    (1001) docker     (123)     7759 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/cloudtrail/responses.py
--rw-r--r--   0 runner    (1001) docker     (123)      221 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/cloudtrail/urls.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:52.769515 moto-4.1.7.dev8/moto/cloudwatch/
--rw-r--r--   0 runner    (1001) docker     (123)      136 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/cloudwatch/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      989 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/cloudwatch/exceptions.py
--rw-r--r--   0 runner    (1001) docker     (123)    33739 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/cloudwatch/models.py
--rw-r--r--   0 runner    (1001) docker     (123)    30696 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/cloudwatch/responses.py
--rw-r--r--   0 runner    (1001) docker     (123)      153 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/cloudwatch/urls.py
--rw-r--r--   0 runner    (1001) docker     (123)      280 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/cloudwatch/utils.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:52.769515 moto-4.1.7.dev8/moto/codebuild/
--rw-r--r--   0 runner    (1001) docker     (123)      133 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/codebuild/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      606 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/codebuild/exceptions.py
--rw-r--r--   0 runner    (1001) docker     (123)    10568 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/codebuild/models.py
--rw-r--r--   0 runner    (1001) docker     (123)     6835 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/codebuild/responses.py
--rw-r--r--   0 runner    (1001) docker     (123)      151 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/codebuild/urls.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:52.769515 moto-4.1.7.dev8/moto/codecommit/
--rw-r--r--   0 runner    (1001) docker     (123)      136 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/codecommit/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     1075 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/codecommit/exceptions.py
--rw-r--r--   0 runner    (1001) docker     (123)     3105 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/codecommit/models.py
--rw-r--r--   0 runner    (1001) docker     (123)     1933 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/codecommit/responses.py
--rw-r--r--   0 runner    (1001) docker     (123)      154 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/codecommit/urls.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:52.769515 moto-4.1.7.dev8/moto/codepipeline/
--rw-r--r--   0 runner    (1001) docker     (123)      142 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/codepipeline/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      916 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/codepipeline/exceptions.py
--rw-r--r--   0 runner    (1001) docker     (123)     7694 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/codepipeline/models.py
--rw-r--r--   0 runner    (1001) docker     (123)     1933 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/codepipeline/responses.py
--rw-r--r--   0 runner    (1001) docker     (123)      160 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/codepipeline/urls.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:52.773515 moto-4.1.7.dev8/moto/cognitoidentity/
--rw-r--r--   0 runner    (1001) docker     (123)      151 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/cognitoidentity/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      595 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/cognitoidentity/exceptions.py
--rw-r--r--   0 runner    (1001) docker     (123)     6990 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/cognitoidentity/models.py
--rw-r--r--   0 runner    (1001) docker     (123)     3684 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/cognitoidentity/responses.py
--rw-r--r--   0 runner    (1001) docker     (123)      169 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/cognitoidentity/urls.py
--rw-r--r--   0 runner    (1001) docker     (123)      143 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/cognitoidentity/utils.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:52.773515 moto-4.1.7.dev8/moto/cognitoidp/
--rw-r--r--   0 runner    (1001) docker     (123)      136 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/cognitoidp/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     1959 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/cognitoidp/exceptions.py
--rw-r--r--   0 runner    (1001) docker     (123)    83773 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/cognitoidp/models.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:52.773515 moto-4.1.7.dev8/moto/cognitoidp/resources/
--rw-r--r--   0 runner    (1001) docker     (123)      792 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/cognitoidp/resources/jwks-private.json
--rw-r--r--   0 runner    (1001) docker     (123)      491 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/cognitoidp/resources/jwks-public.json
--rw-r--r--   0 runner    (1001) docker     (123)    24950 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/cognitoidp/responses.py
--rw-r--r--   0 runner    (1001) docker     (123)      300 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/cognitoidp/urls.py
--rw-r--r--   0 runner    (1001) docker     (123)     2940 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/cognitoidp/utils.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:52.773515 moto-4.1.7.dev8/moto/comprehend/
--rw-r--r--   0 runner    (1001) docker     (123)      207 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/comprehend/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      318 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/comprehend/exceptions.py
--rw-r--r--   0 runner    (1001) docker     (123)     4985 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/comprehend/models.py
--rw-r--r--   0 runner    (1001) docker     (123)     3930 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/comprehend/responses.py
--rw-r--r--   0 runner    (1001) docker     (123)      205 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/comprehend/urls.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:52.777515 moto-4.1.7.dev8/moto/config/
--rw-r--r--   0 runner    (1001) docker     (123)      124 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/config/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    11897 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/config/exceptions.py
--rw-r--r--   0 runner    (1001) docker     (123)    77608 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/config/models.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:52.777515 moto-4.1.7.dev8/moto/config/resources/
--rw-r--r--   0 runner    (1001) docker     (123)   117575 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/config/resources/aws_managed_rules.json
--rw-r--r--   0 runner    (1001) docker     (123)     8828 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/config/responses.py
--rw-r--r--   0 runner    (1001) docker     (123)      142 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/config/urls.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:52.777515 moto-4.1.7.dev8/moto/core/
--rw-r--r--   0 runner    (1001) docker     (123)      439 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/core/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    11074 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/core/base_backend.py
--rw-r--r--   0 runner    (1001) docker     (123)     2455 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/core/botocore_stubber.py
--rw-r--r--   0 runner    (1001) docker     (123)     9179 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/core/common_models.py
--rw-r--r--   0 runner    (1001) docker     (123)      155 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/core/common_types.py
--rw-r--r--   0 runner    (1001) docker     (123)     6436 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/core/custom_responses_mock.py
--rw-r--r--   0 runner    (1001) docker     (123)     5438 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/core/exceptions.py
--rw-r--r--   0 runner    (1001) docker     (123)      482 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/core/model_instances.py
--rw-r--r--   0 runner    (1001) docker     (123)    15270 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/core/models.py
--rw-r--r--   0 runner    (1001) docker     (123)    40468 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/core/responses.py
--rw-r--r--   0 runner    (1001) docker     (123)     1705 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/core/responses_custom_registry.py
--rw-r--r--   0 runner    (1001) docker     (123)    10961 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/core/utils.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:52.777515 moto-4.1.7.dev8/moto/databrew/
--rw-r--r--   0 runner    (1001) docker     (123)      130 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/databrew/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     1398 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/databrew/exceptions.py
--rw-r--r--   0 runner    (1001) docker     (123)    25372 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/databrew/models.py
--rw-r--r--   0 runner    (1001) docker     (123)    19227 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/databrew/responses.py
--rw-r--r--   0 runner    (1001) docker     (123)     1170 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/databrew/urls.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:52.781515 moto-4.1.7.dev8/moto/datapipeline/
--rw-r--r--   0 runner    (1001) docker     (123)      142 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/datapipeline/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     5687 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/datapipeline/models.py
--rw-r--r--   0 runner    (1001) docker     (123)     3659 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/datapipeline/responses.py
--rw-r--r--   0 runner    (1001) docker     (123)      160 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/datapipeline/urls.py
--rw-r--r--   0 runner    (1001) docker     (123)      878 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/datapipeline/utils.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:52.781515 moto-4.1.7.dev8/moto/datasync/
--rw-r--r--   0 runner    (1001) docker     (123)      180 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/datasync/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      351 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/datasync/exceptions.py
--rw-r--r--   0 runner    (1001) docker     (123)     8414 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/datasync/models.py
--rw-r--r--   0 runner    (1001) docker     (123)     6465 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/datasync/responses.py
--rw-r--r--   0 runner    (1001) docker     (123)      156 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/datasync/urls.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:52.781515 moto-4.1.7.dev8/moto/dax/
--rw-r--r--   0 runner    (1001) docker     (123)      179 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/dax/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      552 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/dax/exceptions.py
--rw-r--r--   0 runner    (1001) docker     (123)    10023 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/dax/models.py
--rw-r--r--   0 runner    (1001) docker     (123)     4729 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/dax/responses.py
--rw-r--r--   0 runner    (1001) docker     (123)      177 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/dax/urls.py
--rw-r--r--   0 runner    (1001) docker     (123)      195 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/dax/utils.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:52.781515 moto-4.1.7.dev8/moto/dms/
--rw-r--r--   0 runner    (1001) docker     (123)      155 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/dms/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      551 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/dms/exceptions.py
--rw-r--r--   0 runner    (1001) docker     (123)     7041 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/dms/models.py
--rw-r--r--   0 runner    (1001) docker     (123)     2859 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/dms/responses.py
--rw-r--r--   0 runner    (1001) docker     (123)      183 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/dms/urls.py
--rw-r--r--   0 runner    (1001) docker     (123)     1574 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/dms/utils.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:52.785515 moto-4.1.7.dev8/moto/ds/
--rw-r--r--   0 runner    (1001) docker     (123)      175 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ds/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     2998 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ds/exceptions.py
--rw-r--r--   0 runner    (1001) docker     (123)    21712 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ds/models.py
--rw-r--r--   0 runner    (1001) docker     (123)     6531 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ds/responses.py
--rw-r--r--   0 runner    (1001) docker     (123)      201 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ds/urls.py
--rw-r--r--   0 runner    (1001) docker     (123)      475 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ds/utils.py
--rw-r--r--   0 runner    (1001) docker     (123)     5236 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ds/validations.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:52.785515 moto-4.1.7.dev8/moto/dynamodb/
--rw-r--r--   0 runner    (1001) docker     (123)      193 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/dynamodb/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    42639 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/dynamodb/comparisons.py
--rw-r--r--   0 runner    (1001) docker     (123)    12266 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/dynamodb/exceptions.py
--rw-r--r--   0 runner    (1001) docker     (123)      192 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/dynamodb/limits.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:52.785515 moto-4.1.7.dev8/moto/dynamodb/models/
--rw-r--r--   0 runner    (1001) docker     (123)    29890 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/dynamodb/models/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    16297 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/dynamodb/models/dynamo_type.py
--rw-r--r--   0 runner    (1001) docker     (123)    39690 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/dynamodb/models/table.py
--rw-r--r--   0 runner    (1001) docker     (123)      363 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/dynamodb/models/utilities.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:52.789515 moto-4.1.7.dev8/moto/dynamodb/parsing/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/dynamodb/parsing/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    14200 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/dynamodb/parsing/ast_nodes.py
--rw-r--r--   0 runner    (1001) docker     (123)    12062 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/dynamodb/parsing/executors.py
--rw-r--r--   0 runner    (1001) docker     (123)    34656 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/dynamodb/parsing/expressions.py
--rw-r--r--   0 runner    (1001) docker     (123)     9356 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/dynamodb/parsing/key_condition_expression.py
--rw-r--r--   0 runner    (1001) docker     (123)      893 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/dynamodb/parsing/reserved_keywords.py
--rw-r--r--   0 runner    (1001) docker     (123)     4136 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/dynamodb/parsing/reserved_keywords.txt
--rw-r--r--   0 runner    (1001) docker     (123)     8340 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/dynamodb/parsing/tokens.py
--rw-r--r--   0 runner    (1001) docker     (123)    18402 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/dynamodb/parsing/validators.py
--rw-r--r--   0 runner    (1001) docker     (123)    44274 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/dynamodb/responses.py
--rw-r--r--   0 runner    (1001) docker     (123)      141 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/dynamodb/urls.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:52.789515 moto-4.1.7.dev8/moto/dynamodb_v20111205/
--rw-r--r--   0 runner    (1001) docker     (123)      267 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/dynamodb_v20111205/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     1193 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/dynamodb_v20111205/comparisons.py
--rw-r--r--   0 runner    (1001) docker     (123)    13284 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/dynamodb_v20111205/models.py
--rw-r--r--   0 runner    (1001) docker     (123)    11594 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/dynamodb_v20111205/responses.py
--rw-r--r--   0 runner    (1001) docker     (123)      141 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/dynamodb_v20111205/urls.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:52.789515 moto-4.1.7.dev8/moto/dynamodbstreams/
--rw-r--r--   0 runner    (1001) docker     (123)      215 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/dynamodbstreams/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     5453 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/dynamodbstreams/models.py
--rw-r--r--   0 runner    (1001) docker     (123)     1439 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/dynamodbstreams/responses.py
--rw-r--r--   0 runner    (1001) docker     (123)      168 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/dynamodbstreams/urls.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:52.789515 moto-4.1.7.dev8/moto/ebs/
--rw-r--r--   0 runner    (1001) docker     (123)      179 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ebs/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     4892 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ebs/models.py
--rw-r--r--   0 runner    (1001) docker     (123)     5872 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ebs/responses.py
--rw-r--r--   0 runner    (1001) docker     (123)      557 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ebs/urls.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:52.789515 moto-4.1.7.dev8/moto/ec2/
--rw-r--r--   0 runner    (1001) docker     (123)      115 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ec2/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    24247 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ec2/exceptions.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:52.797515 moto-4.1.7.dev8/moto/ec2/models/
--rw-r--r--   0 runner    (1001) docker     (123)    10045 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ec2/models/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    13217 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ec2/models/amis.py
--rw-r--r--   0 runner    (1001) docker     (123)    12295 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ec2/models/availability_zones_and_regions.py
--rw-r--r--   0 runner    (1001) docker     (123)     2333 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ec2/models/carrier_gateways.py
--rw-r--r--   0 runner    (1001) docker     (123)     1513 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ec2/models/core.py
--rw-r--r--   0 runner    (1001) docker     (123)     3612 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ec2/models/customer_gateways.py
--rw-r--r--   0 runner    (1001) docker     (123)     4823 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ec2/models/dhcp_options.py
--rw-r--r--   0 runner    (1001) docker     (123)    19544 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ec2/models/elastic_block_store.py
--rw-r--r--   0 runner    (1001) docker     (123)     9062 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ec2/models/elastic_ip_addresses.py
--rw-r--r--   0 runner    (1001) docker     (123)    16013 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ec2/models/elastic_network_interfaces.py
--rw-r--r--   0 runner    (1001) docker     (123)    12318 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ec2/models/fleets.py
--rw-r--r--   0 runner    (1001) docker     (123)    11151 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ec2/models/flow_logs.py
--rw-r--r--   0 runner    (1001) docker     (123)     3271 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ec2/models/hosts.py
--rw-r--r--   0 runner    (1001) docker     (123)     5723 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ec2/models/iam_instance_profile.py
--rw-r--r--   0 runner    (1001) docker     (123)     8212 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ec2/models/instance_types.py
--rw-r--r--   0 runner    (1001) docker     (123)    36950 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ec2/models/instances.py
--rw-r--r--   0 runner    (1001) docker     (123)     6237 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ec2/models/internet_gateways.py
--rw-r--r--   0 runner    (1001) docker     (123)     2583 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ec2/models/key_pairs.py
--rw-r--r--   0 runner    (1001) docker     (123)     8321 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ec2/models/launch_templates.py
--rw-r--r--   0 runner    (1001) docker     (123)     6670 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ec2/models/managed_prefixes.py
--rw-r--r--   0 runner    (1001) docker     (123)     5145 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ec2/models/nat_gateways.py
--rw-r--r--   0 runner    (1001) docker     (123)     9951 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ec2/models/network_acls.py
--rw-r--r--   0 runner    (1001) docker     (123)    20808 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ec2/models/route_tables.py
--rw-r--r--   0 runner    (1001) docker     (123)    47173 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ec2/models/security_groups.py
--rw-r--r--   0 runner    (1001) docker     (123)    20404 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ec2/models/spot_requests.py
--rw-r--r--   0 runner    (1001) docker     (123)    17073 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ec2/models/subnets.py
--rw-r--r--   0 runner    (1001) docker     (123)     5290 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ec2/models/tags.py
--rw-r--r--   0 runner    (1001) docker     (123)     4619 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ec2/models/transit_gateway.py
--rw-r--r--   0 runner    (1001) docker     (123)    12869 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ec2/models/transit_gateway_attachments.py
--rw-r--r--   0 runner    (1001) docker     (123)    14765 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ec2/models/transit_gateway_route_tables.py
--rw-r--r--   0 runner    (1001) docker     (123)     7076 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ec2/models/vpc_peering_connections.py
--rw-r--r--   0 runner    (1001) docker     (123)     5614 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ec2/models/vpc_service_configuration.py
--rw-r--r--   0 runner    (1001) docker     (123)    33929 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ec2/models/vpcs.py
--rw-r--r--   0 runner    (1001) docker     (123)     3356 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ec2/models/vpn_connections.py
--rw-r--r--   0 runner    (1001) docker     (123)     6508 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ec2/models/vpn_gateway.py
--rw-r--r--   0 runner    (1001) docker     (123)      381 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ec2/models/windows.py
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ec2/regions.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:52.797515 moto-4.1.7.dev8/moto/ec2/resources/
--rw-r--r--   0 runner    (1001) docker     (123)    24777 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ec2/resources/amis.json
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:52.705514 moto-4.1.7.dev8/moto/ec2/resources/ecs/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:52.813515 moto-4.1.7.dev8/moto/ec2/resources/ecs/optimized_amis/
--rw-r--r--   0 runner    (1001) docker     (123)   110385 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ec2/resources/ecs/optimized_amis/af-south-1.json
--rw-r--r--   0 runner    (1001) docker     (123)   184754 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ec2/resources/ecs/optimized_amis/ap-east-1.json
--rw-r--r--   0 runner    (1001) docker     (123)   237334 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ec2/resources/ecs/optimized_amis/ap-northeast-1.json
--rw-r--r--   0 runner    (1001) docker     (123)   205924 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ec2/resources/ecs/optimized_amis/ap-northeast-2.json
--rw-r--r--   0 runner    (1001) docker     (123)    76970 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ec2/resources/ecs/optimized_amis/ap-northeast-3.json
--rw-r--r--   0 runner    (1001) docker     (123)   233439 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ec2/resources/ecs/optimized_amis/ap-south-1.json
--rw-r--r--   0 runner    (1001) docker     (123)    13740 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ec2/resources/ecs/optimized_amis/ap-south-2.json
--rw-r--r--   0 runner    (1001) docker     (123)   224300 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ec2/resources/ecs/optimized_amis/ap-southeast-1.json
--rw-r--r--   0 runner    (1001) docker     (123)   237334 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ec2/resources/ecs/optimized_amis/ap-southeast-2.json
--rw-r--r--   0 runner    (1001) docker     (123)    41214 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ec2/resources/ecs/optimized_amis/ap-southeast-3.json
--rw-r--r--   0 runner    (1001) docker     (123)   204442 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ec2/resources/ecs/optimized_amis/ca-central-1.json
--rw-r--r--   0 runner    (1001) docker     (123)   236846 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ec2/resources/ecs/optimized_amis/eu-central-1.json
--rw-r--r--   0 runner    (1001) docker     (123)    13740 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ec2/resources/ecs/optimized_amis/eu-central-2.json
--rw-r--r--   0 runner    (1001) docker     (123)   196475 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ec2/resources/ecs/optimized_amis/eu-north-1.json
--rw-r--r--   0 runner    (1001) docker     (123)   151250 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ec2/resources/ecs/optimized_amis/eu-south-1.json
--rw-r--r--   0 runner    (1001) docker     (123)    16169 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ec2/resources/ecs/optimized_amis/eu-south-2.json
--rw-r--r--   0 runner    (1001) docker     (123)   241191 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ec2/resources/ecs/optimized_amis/eu-west-1.json
--rw-r--r--   0 runner    (1001) docker     (123)   205418 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ec2/resources/ecs/optimized_amis/eu-west-2.json
--rw-r--r--   0 runner    (1001) docker     (123)   205543 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ec2/resources/ecs/optimized_amis/eu-west-3.json
--rw-r--r--   0 runner    (1001) docker     (123)    27007 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ec2/resources/ecs/optimized_amis/me-central-1.json
--rw-r--r--   0 runner    (1001) docker     (123)   170773 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ec2/resources/ecs/optimized_amis/me-south-1.json
--rw-r--r--   0 runner    (1001) docker     (123)   216660 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ec2/resources/ecs/optimized_amis/sa-east-1.json
--rw-r--r--   0 runner    (1001) docker     (123)   244124 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ec2/resources/ecs/optimized_amis/us-east-1.json
--rw-r--r--   0 runner    (1001) docker     (123)   241191 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ec2/resources/ecs/optimized_amis/us-east-2.json
--rw-r--r--   0 runner    (1001) docker     (123)   219056 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ec2/resources/ecs/optimized_amis/us-west-1.json
--rw-r--r--   0 runner    (1001) docker     (123)   243613 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ec2/resources/ecs/optimized_amis/us-west-2.json
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:52.705514 moto-4.1.7.dev8/moto/ec2/resources/instance_type_offerings/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:52.821515 moto-4.1.7.dev8/moto/ec2/resources/instance_type_offerings/availability-zone/
--rw-r--r--   0 runner    (1001) docker     (123)    34118 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ec2/resources/instance_type_offerings/availability-zone/af-south-1.json
--rw-r--r--   0 runner    (1001) docker     (123)    38329 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ec2/resources/instance_type_offerings/availability-zone/ap-east-1.json
--rw-r--r--   0 runner    (1001) docker     (123)   112314 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ec2/resources/instance_type_offerings/availability-zone/ap-northeast-1.json
--rw-r--r--   0 runner    (1001) docker     (123)    77322 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ec2/resources/instance_type_offerings/availability-zone/ap-northeast-2.json
--rw-r--r--   0 runner    (1001) docker     (123)    39526 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ec2/resources/instance_type_offerings/availability-zone/ap-northeast-3.json
--rw-r--r--   0 runner    (1001) docker     (123)    70185 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ec2/resources/instance_type_offerings/availability-zone/ap-south-1.json
--rw-r--r--   0 runner    (1001) docker     (123)    23840 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ec2/resources/instance_type_offerings/availability-zone/ap-south-2.json
--rw-r--r--   0 runner    (1001) docker     (123)   100189 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ec2/resources/instance_type_offerings/availability-zone/ap-southeast-1.json
--rw-r--r--   0 runner    (1001) docker     (123)    98303 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ec2/resources/instance_type_offerings/availability-zone/ap-southeast-2.json
--rw-r--r--   0 runner    (1001) docker     (123)    29228 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ec2/resources/instance_type_offerings/availability-zone/ap-southeast-3.json
--rw-r--r--   0 runner    (1001) docker     (123)    63506 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ec2/resources/instance_type_offerings/availability-zone/ca-central-1.json
--rw-r--r--   0 runner    (1001) docker     (123)   102387 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ec2/resources/instance_type_offerings/availability-zone/eu-central-1.json
--rw-r--r--   0 runner    (1001) docker     (123)    23689 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ec2/resources/instance_type_offerings/availability-zone/eu-central-2.json
--rw-r--r--   0 runner    (1001) docker     (123)    47988 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ec2/resources/instance_type_offerings/availability-zone/eu-north-1.json
--rw-r--r--   0 runner    (1001) docker     (123)    48293 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ec2/resources/instance_type_offerings/availability-zone/eu-south-1.json
--rw-r--r--   0 runner    (1001) docker     (123)    23840 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ec2/resources/instance_type_offerings/availability-zone/eu-south-2.json
--rw-r--r--   0 runner    (1001) docker     (123)   121525 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ec2/resources/instance_type_offerings/availability-zone/eu-west-1.json
--rw-r--r--   0 runner    (1001) docker     (123)    71490 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ec2/resources/instance_type_offerings/availability-zone/eu-west-2.json
--rw-r--r--   0 runner    (1001) docker     (123)    58608 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ec2/resources/instance_type_offerings/availability-zone/eu-west-3.json
--rw-r--r--   0 runner    (1001) docker     (123)    24548 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ec2/resources/instance_type_offerings/availability-zone/me-central-1.json
--rw-r--r--   0 runner    (1001) docker     (123)    33135 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ec2/resources/instance_type_offerings/availability-zone/me-south-1.json
--rw-r--r--   0 runner    (1001) docker     (123)    64179 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ec2/resources/instance_type_offerings/availability-zone/sa-east-1.json
--rw-r--r--   0 runner    (1001) docker     (123)   199785 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ec2/resources/instance_type_offerings/availability-zone/us-east-1.json
--rw-r--r--   0 runner    (1001) docker     (123)   111712 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ec2/resources/instance_type_offerings/availability-zone/us-east-2.json
--rw-r--r--   0 runner    (1001) docker     (123)    48786 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ec2/resources/instance_type_offerings/availability-zone/us-west-1.json
--rw-r--r--   0 runner    (1001) docker     (123)   147856 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ec2/resources/instance_type_offerings/availability-zone/us-west-2.json
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:52.829516 moto-4.1.7.dev8/moto/ec2/resources/instance_type_offerings/availability-zone-id/
--rw-r--r--   0 runner    (1001) docker     (123)    32606 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ec2/resources/instance_type_offerings/availability-zone-id/af-south-1.json
--rw-r--r--   0 runner    (1001) docker     (123)    37177 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ec2/resources/instance_type_offerings/availability-zone-id/ap-east-1.json
--rw-r--r--   0 runner    (1001) docker     (123)   102960 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ec2/resources/instance_type_offerings/availability-zone-id/ap-northeast-1.json
--rw-r--r--   0 runner    (1001) docker     (123)    70854 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ec2/resources/instance_type_offerings/availability-zone-id/ap-northeast-2.json
--rw-r--r--   0 runner    (1001) docker     (123)    36220 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ec2/resources/instance_type_offerings/availability-zone-id/ap-northeast-3.json
--rw-r--r--   0 runner    (1001) docker     (123)    67077 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ec2/resources/instance_type_offerings/availability-zone-id/ap-south-1.json
--rw-r--r--   0 runner    (1001) docker     (123)    22778 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ec2/resources/instance_type_offerings/availability-zone-id/ap-south-2.json
--rw-r--r--   0 runner    (1001) docker     (123)    91831 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ec2/resources/instance_type_offerings/availability-zone-id/ap-southeast-1.json
--rw-r--r--   0 runner    (1001) docker     (123)    90095 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ec2/resources/instance_type_offerings/availability-zone-id/ap-southeast-2.json
--rw-r--r--   0 runner    (1001) docker     (123)    26780 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ec2/resources/instance_type_offerings/availability-zone-id/ap-southeast-3.json
--rw-r--r--   0 runner    (1001) docker     (123)    58961 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ec2/resources/instance_type_offerings/availability-zone-id/ca-central-1.json
--rw-r--r--   0 runner    (1001) docker     (123)    95067 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ec2/resources/instance_type_offerings/availability-zone-id/eu-central-1.json
--rw-r--r--   0 runner    (1001) docker     (123)    21984 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ec2/resources/instance_type_offerings/availability-zone-id/eu-central-2.json
--rw-r--r--   0 runner    (1001) docker     (123)    45867 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ec2/resources/instance_type_offerings/availability-zone-id/eu-north-1.json
--rw-r--r--   0 runner    (1001) docker     (123)    46157 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ec2/resources/instance_type_offerings/availability-zone-id/eu-south-1.json
--rw-r--r--   0 runner    (1001) docker     (123)    22778 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ec2/resources/instance_type_offerings/availability-zone-id/eu-south-2.json
--rw-r--r--   0 runner    (1001) docker     (123)   117899 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ec2/resources/instance_type_offerings/availability-zone-id/eu-west-1.json
--rw-r--r--   0 runner    (1001) docker     (123)    69350 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ec2/resources/instance_type_offerings/availability-zone-id/eu-west-2.json
--rw-r--r--   0 runner    (1001) docker     (123)    56856 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ec2/resources/instance_type_offerings/availability-zone-id/eu-west-3.json
--rw-r--r--   0 runner    (1001) docker     (123)    22778 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ec2/resources/instance_type_offerings/availability-zone-id/me-central-1.json
--rw-r--r--   0 runner    (1001) docker     (123)    31665 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ec2/resources/instance_type_offerings/availability-zone-id/me-south-1.json
--rw-r--r--   0 runner    (1001) docker     (123)    62257 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ec2/resources/instance_type_offerings/availability-zone-id/sa-east-1.json
--rw-r--r--   0 runner    (1001) docker     (123)   193821 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ec2/resources/instance_type_offerings/availability-zone-id/us-east-1.json
--rw-r--r--   0 runner    (1001) docker     (123)   108380 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ec2/resources/instance_type_offerings/availability-zone-id/us-east-2.json
--rw-r--r--   0 runner    (1001) docker     (123)    47322 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ec2/resources/instance_type_offerings/availability-zone-id/us-west-1.json
--rw-r--r--   0 runner    (1001) docker     (123)   143444 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ec2/resources/instance_type_offerings/availability-zone-id/us-west-2.json
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:52.837516 moto-4.1.7.dev8/moto/ec2/resources/instance_type_offerings/region/
--rw-r--r--   0 runner    (1001) docker     (123)    11746 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ec2/resources/instance_type_offerings/region/af-south-1.json
--rw-r--r--   0 runner    (1001) docker     (123)    12719 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ec2/resources/instance_type_offerings/region/ap-east-1.json
--rw-r--r--   0 runner    (1001) docker     (123)    40058 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ec2/resources/instance_type_offerings/region/ap-northeast-1.json
--rw-r--r--   0 runner    (1001) docker     (123)    25337 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ec2/resources/instance_type_offerings/region/ap-northeast-2.json
--rw-r--r--   0 runner    (1001) docker     (123)    15559 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ec2/resources/instance_type_offerings/region/ap-northeast-3.json
--rw-r--r--   0 runner    (1001) docker     (123)    24687 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ec2/resources/instance_type_offerings/region/ap-south-1.json
--rw-r--r--   0 runner    (1001) docker     (123)     7830 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ec2/resources/instance_type_offerings/region/ap-south-2.json
--rw-r--r--   0 runner    (1001) docker     (123)    36117 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ec2/resources/instance_type_offerings/region/ap-southeast-1.json
--rw-r--r--   0 runner    (1001) docker     (123)    33577 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ec2/resources/instance_type_offerings/region/ap-southeast-2.json
--rw-r--r--   0 runner    (1001) docker     (123)     9903 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ec2/resources/instance_type_offerings/region/ap-southeast-3.json
--rw-r--r--   0 runner    (1001) docker     (123)    23616 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ec2/resources/instance_type_offerings/region/ca-central-1.json
--rw-r--r--   0 runner    (1001) docker     (123)    35491 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ec2/resources/instance_type_offerings/region/eu-central-1.json
--rw-r--r--   0 runner    (1001) docker     (123)     7879 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ec2/resources/instance_type_offerings/region/eu-central-2.json
--rw-r--r--   0 runner    (1001) docker     (123)    16599 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ec2/resources/instance_type_offerings/region/eu-north-1.json
--rw-r--r--   0 runner    (1001) docker     (123)    16182 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ec2/resources/instance_type_offerings/region/eu-south-1.json
--rw-r--r--   0 runner    (1001) docker     (123)     7830 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ec2/resources/instance_type_offerings/region/eu-south-2.json
--rw-r--r--   0 runner    (1001) docker     (123)    40817 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ec2/resources/instance_type_offerings/region/eu-west-1.json
--rw-r--r--   0 runner    (1001) docker     (123)    24748 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ec2/resources/instance_type_offerings/region/eu-west-2.json
--rw-r--r--   0 runner    (1001) docker     (123)    19711 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ec2/resources/instance_type_offerings/region/eu-west-3.json
--rw-r--r--   0 runner    (1001) docker     (123)     8066 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ec2/resources/instance_type_offerings/region/me-central-1.json
--rw-r--r--   0 runner    (1001) docker     (123)    11132 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ec2/resources/instance_type_offerings/region/me-south-1.json
--rw-r--r--   0 runner    (1001) docker     (123)    24067 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ec2/resources/instance_type_offerings/region/sa-east-1.json
--rw-r--r--   0 runner    (1001) docker     (123)    41549 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ec2/resources/instance_type_offerings/region/us-east-1.json
--rw-r--r--   0 runner    (1001) docker     (123)    37729 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ec2/resources/instance_type_offerings/region/us-east-2.json
--rw-r--r--   0 runner    (1001) docker     (123)    24028 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ec2/resources/instance_type_offerings/region/us-west-1.json
--rw-r--r--   0 runner    (1001) docker     (123)    41477 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ec2/resources/instance_type_offerings/region/us-west-2.json
--rw-r--r--   0 runner    (1001) docker     (123)  1293813 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ec2/resources/instance_types.json
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:52.849516 moto-4.1.7.dev8/moto/ec2/resources/latest_amis/
--rw-r--r--   0 runner    (1001) docker     (123)     9548 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ec2/resources/latest_amis/af-south-1.json
--rw-r--r--   0 runner    (1001) docker     (123)     9548 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ec2/resources/latest_amis/ap-east-1.json
--rw-r--r--   0 runner    (1001) docker     (123)    10558 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ec2/resources/latest_amis/ap-northeast-1.json
--rw-r--r--   0 runner    (1001) docker     (123)     9548 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ec2/resources/latest_amis/ap-northeast-2.json
--rw-r--r--   0 runner    (1001) docker     (123)     9548 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ec2/resources/latest_amis/ap-northeast-3.json
--rw-r--r--   0 runner    (1001) docker     (123)     9548 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ec2/resources/latest_amis/ap-south-1.json
--rw-r--r--   0 runner    (1001) docker     (123)     7506 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ec2/resources/latest_amis/ap-south-2.json
--rw-r--r--   0 runner    (1001) docker     (123)    10558 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ec2/resources/latest_amis/ap-southeast-1.json
--rw-r--r--   0 runner    (1001) docker     (123)    10558 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ec2/resources/latest_amis/ap-southeast-2.json
--rw-r--r--   0 runner    (1001) docker     (123)     9548 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ec2/resources/latest_amis/ap-southeast-3.json
--rw-r--r--   0 runner    (1001) docker     (123)     9548 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ec2/resources/latest_amis/ca-central-1.json
--rw-r--r--   0 runner    (1001) docker     (123)    10558 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ec2/resources/latest_amis/eu-central-1.json
--rw-r--r--   0 runner    (1001) docker     (123)     7506 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ec2/resources/latest_amis/eu-central-2.json
--rw-r--r--   0 runner    (1001) docker     (123)     9548 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ec2/resources/latest_amis/eu-north-1.json
--rw-r--r--   0 runner    (1001) docker     (123)     9548 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ec2/resources/latest_amis/eu-south-1.json
--rw-r--r--   0 runner    (1001) docker     (123)     7506 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ec2/resources/latest_amis/eu-south-2.json
--rw-r--r--   0 runner    (1001) docker     (123)    10558 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ec2/resources/latest_amis/eu-west-1.json
--rw-r--r--   0 runner    (1001) docker     (123)     9548 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ec2/resources/latest_amis/eu-west-2.json
--rw-r--r--   0 runner    (1001) docker     (123)     9548 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ec2/resources/latest_amis/eu-west-3.json
--rw-r--r--   0 runner    (1001) docker     (123)     9548 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ec2/resources/latest_amis/me-central-1.json
--rw-r--r--   0 runner    (1001) docker     (123)     9548 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ec2/resources/latest_amis/me-south-1.json
--rw-r--r--   0 runner    (1001) docker     (123)    10558 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ec2/resources/latest_amis/sa-east-1.json
--rw-r--r--   0 runner    (1001) docker     (123)    10558 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ec2/resources/latest_amis/us-east-1.json
--rw-r--r--   0 runner    (1001) docker     (123)     9548 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ec2/resources/latest_amis/us-east-2.json
--rw-r--r--   0 runner    (1001) docker     (123)    10558 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ec2/resources/latest_amis/us-west-1.json
--rw-r--r--   0 runner    (1001) docker     (123)    10558 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ec2/resources/latest_amis/us-west-2.json
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:52.861516 moto-4.1.7.dev8/moto/ec2/responses/
--rw-r--r--   0 runner    (1001) docker     (123)     2781 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ec2/responses/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     1247 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ec2/responses/_base_response.py
--rw-r--r--   0 runner    (1001) docker     (123)     1864 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ec2/responses/account_attributes.py
--rw-r--r--   0 runner    (1001) docker     (123)     8121 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ec2/responses/amis.py
--rw-r--r--   0 runner    (1001) docker     (123)     1850 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ec2/responses/availability_zones_and_regions.py
--rw-r--r--   0 runner    (1001) docker     (123)     3694 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ec2/responses/carrier_gateways.py
--rw-r--r--   0 runner    (1001) docker     (123)     3372 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ec2/responses/customer_gateways.py
--rw-r--r--   0 runner    (1001) docker     (123)     4986 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ec2/responses/dhcp_options.py
--rw-r--r--   0 runner    (1001) docker     (123)     3494 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ec2/responses/egress_only_internet_gateways.py
--rw-r--r--   0 runner    (1001) docker     (123)    19278 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ec2/responses/elastic_block_store.py
--rw-r--r--   0 runner    (1001) docker     (123)     7313 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ec2/responses/elastic_ip_addresses.py
--rw-r--r--   0 runner    (1001) docker     (123)    18139 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ec2/responses/elastic_network_interfaces.py
--rw-r--r--   0 runner    (1001) docker     (123)    24972 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ec2/responses/fleets.py
--rw-r--r--   0 runner    (1001) docker     (123)     4840 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ec2/responses/flow_logs.py
--rw-r--r--   0 runner    (1001) docker     (123)     1490 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ec2/responses/general.py
--rw-r--r--   0 runner    (1001) docker     (123)     4593 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ec2/responses/hosts.py
--rw-r--r--   0 runner    (1001) docker     (123)     4394 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ec2/responses/iam_instance_profiles.py
--rw-r--r--   0 runner    (1001) docker     (123)    40932 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ec2/responses/instances.py
--rw-r--r--   0 runner    (1001) docker     (123)     4373 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ec2/responses/internet_gateways.py
--rw-r--r--   0 runner    (1001) docker     (123)      493 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ec2/responses/ip_addresses.py
--rw-r--r--   0 runner    (1001) docker     (123)     2646 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ec2/responses/key_pairs.py
--rw-r--r--   0 runner    (1001) docker     (123)     9129 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ec2/responses/launch_templates.py
--rw-r--r--   0 runner    (1001) docker     (123)      428 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ec2/responses/monitoring.py
--rw-r--r--   0 runner    (1001) docker     (123)     5213 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ec2/responses/nat_gateways.py
--rw-r--r--   0 runner    (1001) docker     (123)     7903 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ec2/responses/network_acls.py
--rw-r--r--   0 runner    (1001) docker     (123)     1341 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ec2/responses/reserved_instances.py
--rw-r--r--   0 runner    (1001) docker     (123)    14035 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ec2/responses/route_tables.py
--rw-r--r--   0 runner    (1001) docker     (123)    26457 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ec2/responses/security_groups.py
--rw-r--r--   0 runner    (1001) docker     (123)     2106 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ec2/responses/settings.py
--rw-r--r--   0 runner    (1001) docker     (123)     8310 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ec2/responses/spot_fleets.py
--rw-r--r--   0 runner    (1001) docker     (123)    11251 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ec2/responses/spot_instances.py
--rw-r--r--   0 runner    (1001) docker     (123)     9288 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ec2/responses/subnets.py
--rw-r--r--   0 runner    (1001) docker     (123)     2065 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ec2/responses/tags.py
--rw-r--r--   0 runner    (1001) docker     (123)    24840 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ec2/responses/transit_gateway_attachments.py
--rw-r--r--   0 runner    (1001) docker     (123)    13988 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ec2/responses/transit_gateway_route_tables.py
--rw-r--r--   0 runner    (1001) docker     (123)     9214 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ec2/responses/transit_gateways.py
--rw-r--r--   0 runner    (1001) docker     (123)     4910 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ec2/responses/virtual_private_gateways.py
--rw-r--r--   0 runner    (1001) docker     (123)    11252 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ec2/responses/vpc_peering_connections.py
--rw-r--r--   0 runner    (1001) docker     (123)     8827 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ec2/responses/vpc_service_configuration.py
--rw-r--r--   0 runner    (1001) docker     (123)    39221 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ec2/responses/vpcs.py
--rw-r--r--   0 runner    (1001) docker     (123)    10018 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ec2/responses/vpn_connections.py
--rw-r--r--   0 runner    (1001) docker     (123)     1308 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ec2/responses/windows.py
--rw-r--r--   0 runner    (1001) docker     (123)      140 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ec2/urls.py
--rw-r--r--   0 runner    (1001) docker     (123)    28837 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ec2/utils.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:52.865516 moto-4.1.7.dev8/moto/ec2instanceconnect/
--rw-r--r--   0 runner    (1001) docker     (123)      160 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ec2instanceconnect/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      346 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ec2instanceconnect/models.py
--rw-r--r--   0 runner    (1001) docker     (123)      539 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ec2instanceconnect/responses.py
--rw-r--r--   0 runner    (1001) docker     (123)      180 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ec2instanceconnect/urls.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:52.865516 moto-4.1.7.dev8/moto/ecr/
--rw-r--r--   0 runner    (1001) docker     (123)      155 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ecr/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     4096 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ecr/exceptions.py
--rw-r--r--   0 runner    (1001) docker     (123)    39758 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ecr/models.py
--rw-r--r--   0 runner    (1001) docker     (123)     8913 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ecr/policy_validation.py
--rw-r--r--   0 runner    (1001) docker     (123)    11127 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ecr/responses.py
--rw-r--r--   0 runner    (1001) docker     (123)      188 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ecr/urls.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:52.865516 moto-4.1.7.dev8/moto/ecs/
--rw-r--r--   0 runner    (1001) docker     (123)      155 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ecs/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     1814 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ecs/exceptions.py
--rw-r--r--   0 runner    (1001) docker     (123)    86426 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ecs/models.py
--rw-r--r--   0 runner    (1001) docker     (123)    22481 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ecs/responses.py
--rw-r--r--   0 runner    (1001) docker     (123)      165 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ecs/urls.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:52.869516 moto-4.1.7.dev8/moto/efs/
--rw-r--r--   0 runner    (1001) docker     (123)      155 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/efs/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     2180 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/efs/exceptions.py
--rw-r--r--   0 runner    (1001) docker     (123)    26760 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/efs/models.py
--rw-r--r--   0 runner    (1001) docker     (123)     8303 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/efs/responses.py
--rw-r--r--   0 runner    (1001) docker     (123)      927 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/efs/urls.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:52.869516 moto-4.1.7.dev8/moto/eks/
--rw-r--r--   0 runner    (1001) docker     (123)      171 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/eks/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      942 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/eks/exceptions.py
--rw-r--r--   0 runner    (1001) docker     (123)    30391 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/eks/models.py
--rw-r--r--   0 runner    (1001) docker     (123)     8680 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/eks/responses.py
--rw-r--r--   0 runner    (1001) docker     (123)      624 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/eks/urls.py
--rw-r--r--   0 runner    (1001) docker     (123)     1582 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/eks/utils.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:52.873516 moto-4.1.7.dev8/moto/elasticache/
--rw-r--r--   0 runner    (1001) docker     (123)      139 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/elasticache/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     1592 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/elasticache/exceptions.py
--rw-r--r--   0 runner    (1001) docker     (123)     2935 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/elasticache/models.py
--rw-r--r--   0 runner    (1001) docker     (123)     4087 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/elasticache/responses.py
--rw-r--r--   0 runner    (1001) docker     (123)      209 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/elasticache/urls.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:52.873516 moto-4.1.7.dev8/moto/elasticbeanstalk/
--rw-r--r--   0 runner    (1001) docker     (123)      129 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/elasticbeanstalk/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      334 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/elasticbeanstalk/exceptions.py
--rw-r--r--   0 runner    (1001) docker     (123)     5079 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/elasticbeanstalk/models.py
--rw-r--r--   0 runner    (1001) docker     (123)    57275 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/elasticbeanstalk/responses.py
--rw-r--r--   0 runner    (1001) docker     (123)      180 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/elasticbeanstalk/urls.py
--rw-r--r--   0 runner    (1001) docker     (123)      393 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/elasticbeanstalk/utils.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:52.873516 moto-4.1.7.dev8/moto/elastictranscoder/
--rw-r--r--   0 runner    (1001) docker     (123)      157 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/elastictranscoder/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     3919 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/elastictranscoder/models.py
--rw-r--r--   0 runner    (1001) docker     (123)     5079 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/elastictranscoder/responses.py
--rw-r--r--   0 runner    (1001) docker     (123)      350 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/elastictranscoder/urls.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:52.877516 moto-4.1.7.dev8/moto/elb/
--rw-r--r--   0 runner    (1001) docker     (123)      155 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/elb/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     2703 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/elb/exceptions.py
--rw-r--r--   0 runner    (1001) docker     (123)    25335 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/elb/models.py
--rw-r--r--   0 runner    (1001) docker     (123)     1008 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/elb/policies.py
--rw-r--r--   0 runner    (1001) docker     (123)    37722 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/elb/responses.py
--rw-r--r--   0 runner    (1001) docker     (123)     1336 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/elb/urls.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:52.881516 moto-4.1.7.dev8/moto/elbv2/
--rw-r--r--   0 runner    (1001) docker     (123)      163 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/elbv2/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     5578 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/elbv2/exceptions.py
--rw-r--r--   0 runner    (1001) docker     (123)    69704 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/elbv2/models.py
--rw-r--r--   0 runner    (1001) docker     (123)    68565 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/elbv2/responses.py
--rw-r--r--   0 runner    (1001) docker     (123)      164 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/elbv2/urls.py
--rw-r--r--   0 runner    (1001) docker     (123)      388 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/elbv2/utils.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:52.881516 moto-4.1.7.dev8/moto/emr/
--rw-r--r--   0 runner    (1001) docker     (123)      155 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/emr/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      484 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/emr/exceptions.py
--rw-r--r--   0 runner    (1001) docker     (123)    28079 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/emr/models.py
--rw-r--r--   0 runner    (1001) docker     (123)    65244 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/emr/responses.py
--rw-r--r--   0 runner    (1001) docker     (123)      233 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/emr/urls.py
--rw-r--r--   0 runner    (1001) docker     (123)    16001 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/emr/utils.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:52.881516 moto-4.1.7.dev8/moto/emrcontainers/
--rw-r--r--   0 runner    (1001) docker     (123)      240 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/emrcontainers/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      270 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/emrcontainers/exceptions.py
--rw-r--r--   0 runner    (1001) docker     (123)    13384 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/emrcontainers/models.py
--rw-r--r--   0 runner    (1001) docker     (123)     5584 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/emrcontainers/responses.py
--rw-r--r--   0 runner    (1001) docker     (123)      533 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/emrcontainers/urls.py
--rw-r--r--   0 runner    (1001) docker     (123)     1651 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/emrcontainers/utils.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:52.885516 moto-4.1.7.dev8/moto/emrserverless/
--rw-r--r--   0 runner    (1001) docker     (123)      268 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/emrserverless/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      479 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/emrserverless/exceptions.py
--rw-r--r--   0 runner    (1001) docker     (123)    10304 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/emrserverless/models.py
--rw-r--r--   0 runner    (1001) docker     (123)     4886 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/emrserverless/responses.py
--rw-r--r--   0 runner    (1001) docker     (123)      687 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/emrserverless/urls.py
--rw-r--r--   0 runner    (1001) docker     (123)      600 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/emrserverless/utils.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:52.885516 moto-4.1.7.dev8/moto/es/
--rw-r--r--   0 runner    (1001) docker     (123)      175 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/es/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      858 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/es/exceptions.py
--rw-r--r--   0 runner    (1001) docker     (123)     5931 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/es/models.py
--rw-r--r--   0 runner    (1001) docker     (123)     4601 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/es/responses.py
--rw-r--r--   0 runner    (1001) docker     (123)      931 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/es/urls.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:52.889516 moto-4.1.7.dev8/moto/events/
--rw-r--r--   0 runner    (1001) docker     (123)      170 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/events/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     1024 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/events/exceptions.py
--rw-r--r--   0 runner    (1001) docker     (123)    66807 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/events/models.py
--rw-r--r--   0 runner    (1001) docker     (123)     2247 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/events/notifications.py
--rw-r--r--   0 runner    (1001) docker     (123)    18552 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/events/responses.py
--rw-r--r--   0 runner    (1001) docker     (123)      139 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/events/urls.py
--rw-r--r--   0 runner    (1001) docker     (123)      434 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/events/utils.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:52.889516 moto-4.1.7.dev8/moto/firehose/
--rw-r--r--   0 runner    (1001) docker     (123)      199 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/firehose/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     1486 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/firehose/exceptions.py
--rw-r--r--   0 runner    (1001) docker     (123)    29565 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/firehose/models.py
--rw-r--r--   0 runner    (1001) docker     (123)     5319 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/firehose/responses.py
--rw-r--r--   0 runner    (1001) docker     (123)      182 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/firehose/urls.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:52.889516 moto-4.1.7.dev8/moto/forecast/
--rw-r--r--   0 runner    (1001) docker     (123)      180 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/forecast/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      524 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/forecast/exceptions.py
--rw-r--r--   0 runner    (1001) docker     (123)     5915 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/forecast/models.py
--rw-r--r--   0 runner    (1001) docker     (123)     2987 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/forecast/responses.py
--rw-r--r--   0 runner    (1001) docker     (123)      148 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/forecast/urls.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:52.893516 moto-4.1.7.dev8/moto/glacier/
--rw-r--r--   0 runner    (1001) docker     (123)      175 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/glacier/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     8181 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/glacier/models.py
--rw-r--r--   0 runner    (1001) docker     (123)     7306 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/glacier/responses.py
--rw-r--r--   0 runner    (1001) docker     (123)      885 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/glacier/urls.py
--rw-r--r--   0 runner    (1001) docker     (123)      293 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/glacier/utils.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:52.893516 moto-4.1.7.dev8/moto/glue/
--rw-r--r--   0 runner    (1001) docker     (123)      118 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/glue/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     9638 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/glue/exceptions.py
--rw-r--r--   0 runner    (1001) docker     (123)     1439 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/glue/glue_schema_registry_constants.py
--rw-r--r--   0 runner    (1001) docker     (123)    15009 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/glue/glue_schema_registry_utils.py
--rw-r--r--   0 runner    (1001) docker     (123)    52028 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/glue/models.py
--rw-r--r--   0 runner    (1001) docker     (123)    21842 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/glue/responses.py
--rw-r--r--   0 runner    (1001) docker     (123)      136 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/glue/urls.py
--rw-r--r--   0 runner    (1001) docker     (123)    12557 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/glue/utils.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:52.893516 moto-4.1.7.dev8/moto/greengrass/
--rw-r--r--   0 runner    (1001) docker     (123)      136 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/greengrass/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     1146 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/greengrass/exceptions.py
--rw-r--r--   0 runner    (1001) docker     (123)    54499 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/greengrass/models.py
--rw-r--r--   0 runner    (1001) docker     (123)    30895 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/greengrass/responses.py
--rw-r--r--   0 runner    (1001) docker     (123)     3051 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/greengrass/urls.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:52.897516 moto-4.1.7.dev8/moto/guardduty/
--rw-r--r--   0 runner    (1001) docker     (123)      185 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/guardduty/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     1039 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/guardduty/exceptions.py
--rw-r--r--   0 runner    (1001) docker     (123)     7861 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/guardduty/models.py
--rw-r--r--   0 runner    (1001) docker     (123)     5980 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/guardduty/responses.py
--rw-r--r--   0 runner    (1001) docker     (123)      553 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/guardduty/urls.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:52.901516 moto-4.1.7.dev8/moto/iam/
--rw-r--r--   0 runner    (1001) docker     (123)      115 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/iam/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    16725 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/iam/access_control.py
--rw-r--r--   0 runner    (1001) docker     (123)  1599363 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/iam/aws_managed_policies.py
--rw-r--r--   0 runner    (1001) docker     (123)    14247 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/iam/config.py
--rw-r--r--   0 runner    (1001) docker     (123)     3532 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/iam/exceptions.py
--rw-r--r--   0 runner    (1001) docker     (123)   118562 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/iam/models.py
--rw-r--r--   0 runner    (1001) docker     (123)    22588 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/iam/policy_validation.py
--rw-r--r--   0 runner    (1001) docker     (123)   107097 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/iam/responses.py
--rw-r--r--   0 runner    (1001) docker     (123)      134 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/iam/urls.py
--rw-r--r--   0 runner    (1001) docker     (123)     2250 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/iam/utils.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:52.901516 moto-4.1.7.dev8/moto/identitystore/
--rw-r--r--   0 runner    (1001) docker     (123)      219 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/identitystore/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)       54 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/identitystore/exceptions.py
--rw-r--r--   0 runner    (1001) docker     (123)      908 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/identitystore/models.py
--rw-r--r--   0 runner    (1001) docker     (123)     1117 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/identitystore/responses.py
--rw-r--r--   0 runner    (1001) docker     (123)      216 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/identitystore/urls.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:52.905516 moto-4.1.7.dev8/moto/instance_metadata/
--rw-r--r--   0 runner    (1001) docker     (123)       55 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/instance_metadata/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      266 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/instance_metadata/models.py
--rw-r--r--   0 runner    (1001) docker     (123)     1767 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/instance_metadata/responses.py
--rw-r--r--   0 runner    (1001) docker     (123)      207 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/instance_metadata/urls.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:52.905516 moto-4.1.7.dev8/moto/iot/
--rw-r--r--   0 runner    (1001) docker     (123)      115 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/iot/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     2545 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/iot/exceptions.py
--rw-r--r--   0 runner    (1001) docker     (123)    70619 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/iot/models.py
--rw-r--r--   0 runner    (1001) docker     (123)    32365 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/iot/responses.py
--rw-r--r--   0 runner    (1001) docker     (123)      742 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/iot/urls.py
--rw-r--r--   0 runner    (1001) docker     (123)      208 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/iot/utils.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:52.905516 moto-4.1.7.dev8/moto/iotdata/
--rw-r--r--   0 runner    (1001) docker     (123)      127 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/iotdata/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      693 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/iotdata/exceptions.py
--rw-r--r--   0 runner    (1001) docker     (123)     7563 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/iotdata/models.py
--rw-r--r--   0 runner    (1001) docker     (123)     1797 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/iotdata/responses.py
--rw-r--r--   0 runner    (1001) docker     (123)      373 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/iotdata/urls.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:52.909516 moto-4.1.7.dev8/moto/kinesis/
--rw-r--r--   0 runner    (1001) docker     (123)      175 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/kinesis/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     3818 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/kinesis/exceptions.py
--rw-r--r--   0 runner    (1001) docker     (123)    35988 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/kinesis/models.py
--rw-r--r--   0 runner    (1001) docker     (123)    12283 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/kinesis/responses.py
--rw-r--r--   0 runner    (1001) docker     (123)      566 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/kinesis/urls.py
--rw-r--r--   0 runner    (1001) docker     (123)     1922 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/kinesis/utils.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:52.909516 moto-4.1.7.dev8/moto/kinesisvideo/
--rw-r--r--   0 runner    (1001) docker     (123)      200 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/kinesisvideo/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      538 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/kinesisvideo/exceptions.py
--rw-r--r--   0 runner    (1001) docker     (123)     4313 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/kinesisvideo/models.py
--rw-r--r--   0 runner    (1001) docker     (123)     2221 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/kinesisvideo/responses.py
--rw-r--r--   0 runner    (1001) docker     (123)      390 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/kinesisvideo/urls.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:52.913516 moto-4.1.7.dev8/moto/kinesisvideoarchivedmedia/
--rw-r--r--   0 runner    (1001) docker     (123)      265 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/kinesisvideoarchivedmedia/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)       37 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/kinesisvideoarchivedmedia/exceptions.py
--rw-r--r--   0 runner    (1001) docker     (123)     2018 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/kinesisvideoarchivedmedia/models.py
--rw-r--r--   0 runner    (1001) docker     (123)     1812 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/kinesisvideoarchivedmedia/responses.py
--rw-r--r--   0 runner    (1001) docker     (123)      230 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/kinesisvideoarchivedmedia/urls.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:52.913516 moto-4.1.7.dev8/moto/kms/
--rw-r--r--   0 runner    (1001) docker     (123)      155 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/kms/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     1182 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/kms/exceptions.py
--rw-r--r--   0 runner    (1001) docker     (123)    24509 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/kms/models.py
--rw-r--r--   0 runner    (1001) docker     (123)     1735 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/kms/policy_validator.py
--rw-r--r--   0 runner    (1001) docker     (123)    25988 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/kms/responses.py
--rw-r--r--   0 runner    (1001) docker     (123)      133 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/kms/urls.py
--rw-r--r--   0 runner    (1001) docker     (123)     7658 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/kms/utils.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:52.913516 moto-4.1.7.dev8/moto/logs/
--rw-r--r--   0 runner    (1001) docker     (123)      118 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/logs/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     1340 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/logs/exceptions.py
--rw-r--r--   0 runner    (1001) docker     (123)     2742 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/logs/metric_filters.py
--rw-r--r--   0 runner    (1001) docker     (123)    36704 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/logs/models.py
--rw-r--r--   0 runner    (1001) docker     (123)    14217 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/logs/responses.py
--rw-r--r--   0 runner    (1001) docker     (123)      136 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/logs/urls.py
--rw-r--r--   0 runner    (1001) docker     (123)     1899 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/logs/utils.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:52.917516 moto-4.1.7.dev8/moto/managedblockchain/
--rw-r--r--   0 runner    (1001) docker     (123)      225 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/managedblockchain/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     3110 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/managedblockchain/exceptions.py
--rw-r--r--   0 runner    (1001) docker     (123)    37565 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/managedblockchain/models.py
--rw-r--r--   0 runner    (1001) docker     (123)    16840 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/managedblockchain/responses.py
--rw-r--r--   0 runner    (1001) docker     (123)     1732 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/managedblockchain/urls.py
--rw-r--r--   0 runner    (1001) docker     (123)     4185 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/managedblockchain/utils.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:52.917516 moto-4.1.7.dev8/moto/mediaconnect/
--rw-r--r--   0 runner    (1001) docker     (123)      200 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/mediaconnect/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      193 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/mediaconnect/exceptions.py
--rw-r--r--   0 runner    (1001) docker     (123)    15029 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/mediaconnect/models.py
--rw-r--r--   0 runner    (1001) docker     (123)    10367 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/mediaconnect/responses.py
--rw-r--r--   0 runner    (1001) docker     (123)     1121 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/mediaconnect/urls.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:52.917516 moto-4.1.7.dev8/moto/medialive/
--rw-r--r--   0 runner    (1001) docker     (123)      133 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/medialive/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/medialive/exceptions.py
--rw-r--r--   0 runner    (1001) docker     (123)     9868 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/medialive/models.py
--rw-r--r--   0 runner    (1001) docker     (123)     6064 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/medialive/responses.py
--rw-r--r--   0 runner    (1001) docker     (123)      520 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/medialive/urls.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:52.921517 moto-4.1.7.dev8/moto/mediapackage/
--rw-r--r--   0 runner    (1001) docker     (123)      200 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/mediapackage/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      325 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/mediapackage/exceptions.py
--rw-r--r--   0 runner    (1001) docker     (123)     7327 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/mediapackage/models.py
--rw-r--r--   0 runner    (1001) docker     (123)     4680 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/mediapackage/responses.py
--rw-r--r--   0 runner    (1001) docker     (123)      379 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/mediapackage/urls.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:52.921517 moto-4.1.7.dev8/moto/mediastore/
--rw-r--r--   0 runner    (1001) docker     (123)      190 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/mediastore/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      872 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/mediastore/exceptions.py
--rw-r--r--   0 runner    (1001) docker     (123)     4267 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/mediastore/models.py
--rw-r--r--   0 runner    (1001) docker     (123)     3214 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/mediastore/responses.py
--rw-r--r--   0 runner    (1001) docker     (123)      221 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/mediastore/urls.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:52.921517 moto-4.1.7.dev8/moto/mediastoredata/
--rw-r--r--   0 runner    (1001) docker     (123)      210 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/mediastoredata/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      329 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/mediastoredata/exceptions.py
--rw-r--r--   0 runner    (1001) docker     (123)     2265 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/mediastoredata/models.py
--rw-r--r--   0 runner    (1001) docker     (123)     1118 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/mediastoredata/responses.py
--rw-r--r--   0 runner    (1001) docker     (123)      241 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/mediastoredata/urls.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:52.921517 moto-4.1.7.dev8/moto/meteringmarketplace/
--rw-r--r--   0 runner    (1001) docker     (123)      235 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/meteringmarketplace/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     1250 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/meteringmarketplace/exceptions.py
--rw-r--r--   0 runner    (1001) docker     (123)     4374 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/meteringmarketplace/models.py
--rw-r--r--   0 runner    (1001) docker     (123)      661 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/meteringmarketplace/responses.py
--rw-r--r--   0 runner    (1001) docker     (123)      236 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/meteringmarketplace/urls.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:52.921517 moto-4.1.7.dev8/moto/moto_api/
--rw-r--r--   0 runner    (1001) docker     (123)      367 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/moto_api/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:52.921517 moto-4.1.7.dev8/moto/moto_api/_internal/
--rw-r--r--   0 runner    (1001) docker     (123)      339 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/moto_api/_internal/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     2590 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/moto_api/_internal/managed_state_model.py
--rw-r--r--   0 runner    (1001) docker     (123)     1660 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/moto_api/_internal/models.py
--rw-r--r--   0 runner    (1001) docker     (123)     1032 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/moto_api/_internal/moto_random.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:52.925516 moto-4.1.7.dev8/moto/moto_api/_internal/recorder/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/moto_api/_internal/recorder/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     4950 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/moto_api/_internal/recorder/models.py
--rw-r--r--   0 runner    (1001) docker     (123)     1606 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/moto_api/_internal/recorder/responses.py
--rw-r--r--   0 runner    (1001) docker     (123)     5960 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/moto_api/_internal/responses.py
--rw-r--r--   0 runner    (1001) docker     (123)     2046 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/moto_api/_internal/state_manager.py
--rw-r--r--   0 runner    (1001) docker     (123)     1347 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/moto_api/_internal/urls.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:52.925516 moto-4.1.7.dev8/moto/moto_server/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:52.925516 moto-4.1.7.dev8/moto/moto_server/templates/
--rw-r--r--   0 runner    (1001) docker     (123)     5985 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/moto_server/templates/dashboard.html
--rw-r--r--   0 runner    (1001) docker     (123)     1188 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/moto_server/threaded_moto_server.py
--rw-r--r--   0 runner    (1001) docker     (123)     1071 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/moto_server/utilities.py
--rw-r--r--   0 runner    (1001) docker     (123)    11718 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/moto_server/werkzeug_app.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:52.925516 moto-4.1.7.dev8/moto/mq/
--rw-r--r--   0 runner    (1001) docker     (123)      175 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/mq/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     8368 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/mq/configuration.py
--rw-r--r--   0 runner    (1001) docker     (123)     2410 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/mq/exceptions.py
--rw-r--r--   0 runner    (1001) docker     (123)    17887 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/mq/models.py
--rw-r--r--   0 runner    (1001) docker     (123)    10554 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/mq/responses.py
--rw-r--r--   0 runner    (1001) docker     (123)      793 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/mq/urls.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:52.925516 moto-4.1.7.dev8/moto/neptune/
--rw-r--r--   0 runner    (1001) docker     (123)      493 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/neptune/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      848 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/neptune/exceptions.py
--rw-r--r--   0 runner    (1001) docker     (123)    16523 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/neptune/models.py
--rw-r--r--   0 runner    (1001) docker     (123)     7895 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/neptune/responses.py
--rw-r--r--   0 runner    (1001) docker     (123)      151 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/neptune/urls.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:52.925516 moto-4.1.7.dev8/moto/opensearch/
--rw-r--r--   0 runner    (1001) docker     (123)      207 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/opensearch/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     4473 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/opensearch/data.py
--rw-r--r--   0 runner    (1001) docker     (123)      266 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/opensearch/exceptions.py
--rw-r--r--   0 runner    (1001) docker     (123)    13390 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/opensearch/models.py
--rw-r--r--   0 runner    (1001) docker     (123)     6592 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/opensearch/responses.py
--rw-r--r--   0 runner    (1001) docker     (123)      223 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/opensearch/urls.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:52.929517 moto-4.1.7.dev8/moto/opsworks/
--rw-r--r--   0 runner    (1001) docker     (123)      180 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/opsworks/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      371 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/opsworks/exceptions.py
--rw-r--r--   0 runner    (1001) docker     (123)    24826 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/opsworks/models.py
--rw-r--r--   0 runner    (1001) docker     (123)     6762 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/opsworks/responses.py
--rw-r--r--   0 runner    (1001) docker     (123)      259 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/opsworks/urls.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:52.929517 moto-4.1.7.dev8/moto/organizations/
--rw-r--r--   0 runner    (1001) docker     (123)      145 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/organizations/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     2748 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/organizations/exceptions.py
--rw-r--r--   0 runner    (1001) docker     (123)    34112 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/organizations/models.py
--rw-r--r--   0 runner    (1001) docker     (123)     8160 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/organizations/responses.py
--rw-r--r--   0 runner    (1001) docker     (123)      163 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/organizations/urls.py
--rw-r--r--   0 runner    (1001) docker     (123)     4009 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/organizations/utils.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:52.929517 moto-4.1.7.dev8/moto/packages/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/packages/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:52.929517 moto-4.1.7.dev8/moto/packages/boto/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/packages/boto/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:52.929517 moto-4.1.7.dev8/moto/packages/boto/ec2/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/packages/boto/ec2/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     3336 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/packages/boto/ec2/blockdevicemapping.py
--rw-r--r--   0 runner    (1001) docker     (123)     1932 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/packages/boto/ec2/ec2object.py
--rw-r--r--   0 runner    (1001) docker     (123)     1187 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/packages/boto/ec2/image.py
--rw-r--r--   0 runner    (1001) docker     (123)     7305 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/packages/boto/ec2/instance.py
--rw-r--r--   0 runner    (1001) docker     (123)     1941 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/packages/boto/ec2/instancetype.py
--rw-r--r--   0 runner    (1001) docker     (123)     1605 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/packages/boto/ec2/tag.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:52.929517 moto-4.1.7.dev8/moto/packages/cfnresponse/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/packages/cfnresponse/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     1506 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/packages/cfnresponse/cfnresponse.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:52.933517 moto-4.1.7.dev8/moto/personalize/
--rw-r--r--   0 runner    (1001) docker     (123)      211 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/personalize/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      354 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/personalize/exceptions.py
--rw-r--r--   0 runner    (1001) docker     (123)     1951 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/personalize/models.py
--rw-r--r--   0 runner    (1001) docker     (123)     1600 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/personalize/responses.py
--rw-r--r--   0 runner    (1001) docker     (123)      209 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/personalize/urls.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:52.933517 moto-4.1.7.dev8/moto/pinpoint/
--rw-r--r--   0 runner    (1001) docker     (123)      199 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/pinpoint/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      465 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/pinpoint/exceptions.py
--rw-r--r--   0 runner    (1001) docker     (123)     4727 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/pinpoint/models.py
--rw-r--r--   0 runner    (1001) docker     (123)     5580 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/pinpoint/responses.py
--rw-r--r--   0 runner    (1001) docker     (123)      554 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/pinpoint/urls.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:52.933517 moto-4.1.7.dev8/moto/polly/
--rw-r--r--   0 runner    (1001) docker     (123)      165 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/polly/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     3282 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/polly/models.py
--rw-r--r--   0 runner    (1001) docker     (123)    16652 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/polly/resources.py
--rw-r--r--   0 runner    (1001) docker     (123)     6956 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/polly/responses.py
--rw-r--r--   0 runner    (1001) docker     (123)      311 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/polly/urls.py
--rw-r--r--   0 runner    (1001) docker     (123)      127 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/polly/utils.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:52.933517 moto-4.1.7.dev8/moto/quicksight/
--rw-r--r--   0 runner    (1001) docker     (123)      207 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/quicksight/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      236 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/quicksight/exceptions.py
--rw-r--r--   0 runner    (1001) docker     (123)     7745 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/quicksight/models.py
--rw-r--r--   0 runner    (1001) docker     (123)     7829 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/quicksight/responses.py
--rw-r--r--   0 runner    (1001) docker     (123)     1186 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/quicksight/urls.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:52.933517 moto-4.1.7.dev8/moto/ram/
--rw-r--r--   0 runner    (1001) docker     (123)      155 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ram/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      933 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ram/exceptions.py
--rw-r--r--   0 runner    (1001) docker     (123)     8007 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ram/models.py
--rw-r--r--   0 runner    (1001) docker     (123)     1210 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ram/responses.py
--rw-r--r--   0 runner    (1001) docker     (123)      495 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ram/urls.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:52.937517 moto-4.1.7.dev8/moto/rds/
--rw-r--r--   0 runner    (1001) docker     (123)      155 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/rds/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     5788 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/rds/exceptions.py
--rw-r--r--   0 runner    (1001) docker     (123)   161415 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/rds/models.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:52.713514 moto-4.1.7.dev8/moto/rds/resources/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:52.937517 moto-4.1.7.dev8/moto/rds/resources/cluster_options/
--rw-r--r--   0 runner    (1001) docker     (123)   133645 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/rds/resources/cluster_options/neptune.json
--rw-r--r--   0 runner    (1001) docker     (123)    57063 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/rds/responses.py
--rw-r--r--   0 runner    (1001) docker     (123)      166 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/rds/urls.py
--rw-r--r--   0 runner    (1001) docker     (123)    11479 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/rds/utils.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:52.937517 moto-4.1.7.dev8/moto/redshift/
--rw-r--r--   0 runner    (1001) docker     (123)      130 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/redshift/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     5210 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/redshift/exceptions.py
--rw-r--r--   0 runner    (1001) docker     (123)    39885 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/redshift/models.py
--rw-r--r--   0 runner    (1001) docker     (123)    29120 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/redshift/responses.py
--rw-r--r--   0 runner    (1001) docker     (123)      148 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/redshift/urls.py
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/redshift/utils.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:52.937517 moto-4.1.7.dev8/moto/redshiftdata/
--rw-r--r--   0 runner    (1001) docker     (123)      142 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/redshiftdata/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      334 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/redshiftdata/exceptions.py
--rw-r--r--   0 runner    (1001) docker     (123)     7211 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/redshiftdata/models.py
--rw-r--r--   0 runner    (1001) docker     (123)     2150 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/redshiftdata/responses.py
--rw-r--r--   0 runner    (1001) docker     (123)      196 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/redshiftdata/urls.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:52.941517 moto-4.1.7.dev8/moto/rekognition/
--rw-r--r--   0 runner    (1001) docker     (123)      211 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/rekognition/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)       52 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/rekognition/exceptions.py
--rw-r--r--   0 runner    (1001) docker     (123)    13288 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/rekognition/models.py
--rw-r--r--   0 runner    (1001) docker     (123)     2281 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/rekognition/responses.py
--rw-r--r--   0 runner    (1001) docker     (123)      208 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/rekognition/urls.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:52.941517 moto-4.1.7.dev8/moto/resourcegroups/
--rw-r--r--   0 runner    (1001) docker     (123)      210 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/resourcegroups/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      226 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/resourcegroups/exceptions.py
--rw-r--r--   0 runner    (1001) docker     (123)    13344 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/resourcegroups/models.py
--rw-r--r--   0 runner    (1001) docker     (123)     6386 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/resourcegroups/responses.py
--rw-r--r--   0 runner    (1001) docker     (123)      934 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/resourcegroups/urls.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:52.941517 moto-4.1.7.dev8/moto/resourcegroupstaggingapi/
--rw-r--r--   0 runner    (1001) docker     (123)      260 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/resourcegroupstaggingapi/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    27328 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/resourcegroupstaggingapi/models.py
--rw-r--r--   0 runner    (1001) docker     (123)     3483 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/resourcegroupstaggingapi/responses.py
--rw-r--r--   0 runner    (1001) docker     (123)      178 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/resourcegroupstaggingapi/urls.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:52.941517 moto-4.1.7.dev8/moto/route53/
--rw-r--r--   0 runner    (1001) docker     (123)      127 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/route53/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     5404 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/route53/exceptions.py
--rw-r--r--   0 runner    (1001) docker     (123)    34262 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/route53/models.py
--rw-r--r--   0 runner    (1001) docker     (123)    34372 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/route53/responses.py
--rw-r--r--   0 runner    (1001) docker     (123)     2533 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/route53/urls.py
--rw-r--r--   0 runner    (1001) docker     (123)      364 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/route53/utils.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:52.941517 moto-4.1.7.dev8/moto/route53resolver/
--rw-r--r--   0 runner    (1001) docker     (123)      227 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/route53resolver/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     2793 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/route53resolver/exceptions.py
--rw-r--r--   0 runner    (1001) docker     (123)    35274 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/route53resolver/models.py
--rw-r--r--   0 runner    (1001) docker     (123)    11715 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/route53resolver/responses.py
--rw-r--r--   0 runner    (1001) docker     (123)      225 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/route53resolver/urls.py
--rw-r--r--   0 runner    (1001) docker     (123)     1150 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/route53resolver/utils.py
--rw-r--r--   0 runner    (1001) docker     (123)     4911 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/route53resolver/validations.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:52.945517 moto-4.1.7.dev8/moto/s3/
--rw-r--r--   0 runner    (1001) docker     (123)      112 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/s3/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     1259 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/s3/cloud_formation.py
--rw-r--r--   0 runner    (1001) docker     (123)     4469 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/s3/config.py
--rw-r--r--   0 runner    (1001) docker     (123)    16719 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/s3/exceptions.py
--rw-r--r--   0 runner    (1001) docker     (123)    82916 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/s3/models.py
--rw-r--r--   0 runner    (1001) docker     (123)     3767 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/s3/notifications.py
--rw-r--r--   0 runner    (1001) docker     (123)   115846 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/s3/responses.py
--rw-r--r--   0 runner    (1001) docker     (123)     1871 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/s3/select_object_content.py
--rw-r--r--   0 runner    (1001) docker     (123)      871 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/s3/urls.py
--rw-r--r--   0 runner    (1001) docker     (123)     6538 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/s3/utils.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:52.945517 moto-4.1.7.dev8/moto/s3bucket_path/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/s3bucket_path/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      301 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/s3bucket_path/utils.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:52.949517 moto-4.1.7.dev8/moto/s3control/
--rw-r--r--   0 runner    (1001) docker     (123)      203 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/s3control/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     4922 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/s3control/config.py
--rw-r--r--   0 runner    (1001) docker     (123)     1376 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/s3control/exceptions.py
--rw-r--r--   0 runner    (1001) docker     (123)     4813 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/s3control/models.py
--rw-r--r--   0 runner    (1001) docker     (123)     9040 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/s3control/responses.py
--rw-r--r--   0 runner    (1001) docker     (123)      607 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/s3control/urls.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:52.949517 moto-4.1.7.dev8/moto/sagemaker/
--rw-r--r--   0 runner    (1001) docker     (123)      185 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/sagemaker/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     1209 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/sagemaker/exceptions.py
--rw-r--r--   0 runner    (1001) docker     (123)    91754 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/sagemaker/models.py
--rw-r--r--   0 runner    (1001) docker     (123)    28604 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/sagemaker/responses.py
--rw-r--r--   0 runner    (1001) docker     (123)      169 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/sagemaker/urls.py
--rw-r--r--   0 runner    (1001) docker     (123)     1493 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/sagemaker/utils.py
--rw-r--r--   0 runner    (1001) docker     (123)      538 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/sagemaker/validators.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:52.949517 moto-4.1.7.dev8/moto/sdb/
--rw-r--r--   0 runner    (1001) docker     (123)      179 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/sdb/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     1247 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/sdb/exceptions.py
--rw-r--r--   0 runner    (1001) docker     (123)     3310 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/sdb/models.py
--rw-r--r--   0 runner    (1001) docker     (123)     3383 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/sdb/responses.py
--rw-r--r--   0 runner    (1001) docker     (123)      150 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/sdb/urls.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:52.953517 moto-4.1.7.dev8/moto/secretsmanager/
--rw-r--r--   0 runner    (1001) docker     (123)      210 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/secretsmanager/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     1929 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/secretsmanager/exceptions.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:52.953517 moto-4.1.7.dev8/moto/secretsmanager/list_secrets/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/secretsmanager/list_secrets/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     1169 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/secretsmanager/list_secrets/filters.py
--rw-r--r--   0 runner    (1001) docker     (123)    30397 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/secretsmanager/models.py
--rw-r--r--   0 runner    (1001) docker     (123)     8758 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/secretsmanager/responses.py
--rw-r--r--   0 runner    (1001) docker     (123)      166 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/secretsmanager/urls.py
--rw-r--r--   0 runner    (1001) docker     (123)     3483 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/secretsmanager/utils.py
--rw-r--r--   0 runner    (1001) docker     (123)     2749 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/server.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:52.953517 moto-4.1.7.dev8/moto/servicediscovery/
--rw-r--r--   0 runner    (1001) docker     (123)      231 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/servicediscovery/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      623 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/servicediscovery/exceptions.py
--rw-r--r--   0 runner    (1001) docker     (123)    10956 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/servicediscovery/models.py
--rw-r--r--   0 runner    (1001) docker     (123)     6515 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/servicediscovery/responses.py
--rw-r--r--   0 runner    (1001) docker     (123)      229 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/servicediscovery/urls.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:52.953517 moto-4.1.7.dev8/moto/servicequotas/
--rw-r--r--   0 runner    (1001) docker     (123)      219 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/servicequotas/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      365 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/servicequotas/exceptions.py
--rw-r--r--   0 runner    (1001) docker     (123)     1149 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/servicequotas/models.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:52.953517 moto-4.1.7.dev8/moto/servicequotas/resources/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/servicequotas/resources/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:52.953517 moto-4.1.7.dev8/moto/servicequotas/resources/default_quotas/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/servicequotas/resources/default_quotas/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     9458 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/servicequotas/resources/default_quotas/vpc.py
--rw-r--r--   0 runner    (1001) docker     (123)     1231 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/servicequotas/responses.py
--rw-r--r--   0 runner    (1001) docker     (123)      217 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/servicequotas/urls.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:52.953517 moto-4.1.7.dev8/moto/ses/
--rw-r--r--   0 runner    (1001) docker     (123)      115 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ses/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     2283 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ses/exceptions.py
--rw-r--r--   0 runner    (1001) docker     (123)     2424 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ses/feedback.py
--rw-r--r--   0 runner    (1001) docker     (123)    21690 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ses/models.py
--rw-r--r--   0 runner    (1001) docker     (123)    31667 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ses/responses.py
--rw-r--r--   0 runner    (1001) docker     (123)     1743 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ses/template.py
--rw-r--r--   0 runner    (1001) docker     (123)      189 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ses/urls.py
--rw-r--r--   0 runner    (1001) docker     (123)      573 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ses/utils.py
--rw-r--r--   0 runner    (1001) docker     (123)     4587 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/settings.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:52.957517 moto-4.1.7.dev8/moto/signer/
--rw-r--r--   0 runner    (1001) docker     (123)      191 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/signer/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)       47 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/signer/exceptions.py
--rw-r--r--   0 runner    (1001) docker     (123)     6690 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/signer/models.py
--rw-r--r--   0 runner    (1001) docker     (123)     1609 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/signer/responses.py
--rw-r--r--   0 runner    (1001) docker     (123)      302 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/signer/urls.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:52.957517 moto-4.1.7.dev8/moto/sns/
--rw-r--r--   0 runner    (1001) docker     (123)      115 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/sns/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     2096 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/sns/exceptions.py
--rw-r--r--   0 runner    (1001) docker     (123)    38878 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/sns/models.py
--rw-r--r--   0 runner    (1001) docker     (123)    46551 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/sns/responses.py
--rw-r--r--   0 runner    (1001) docker     (123)      133 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/sns/urls.py
--rw-r--r--   0 runner    (1001) docker     (123)      424 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/sns/utils.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:52.957517 moto-4.1.7.dev8/moto/sqs/
--rw-r--r--   0 runner    (1001) docker     (123)      115 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/sqs/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     3058 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/sqs/exceptions.py
--rw-r--r--   0 runner    (1001) docker     (123)    38213 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/sqs/models.py
--rw-r--r--   0 runner    (1001) docker     (123)    30771 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/sqs/responses.py
--rw-r--r--   0 runner    (1001) docker     (123)      255 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/sqs/urls.py
--rw-r--r--   0 runner    (1001) docker     (123)     2558 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/sqs/utils.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:52.957517 moto-4.1.7.dev8/moto/ssm/
--rw-r--r--   0 runner    (1001) docker     (123)      115 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ssm/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     3171 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ssm/exceptions.py
--rw-r--r--   0 runner    (1001) docker     (123)    75789 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ssm/models.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:52.961517 moto-4.1.7.dev8/moto/ssm/resources/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:52.969517 moto-4.1.7.dev8/moto/ssm/resources/ami-amazon-linux-latest/
--rw-r--r--   0 runner    (1001) docker     (123)    10194 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ssm/resources/ami-amazon-linux-latest/af-south-1.json
--rw-r--r--   0 runner    (1001) docker     (123)    10164 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ssm/resources/ami-amazon-linux-latest/ap-east-1.json
--rw-r--r--   0 runner    (1001) docker     (123)    11683 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ssm/resources/ami-amazon-linux-latest/ap-northeast-1.json
--rw-r--r--   0 runner    (1001) docker     (123)    10307 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ssm/resources/ami-amazon-linux-latest/ap-northeast-2.json
--rw-r--r--   0 runner    (1001) docker     (123)    10310 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ssm/resources/ami-amazon-linux-latest/ap-northeast-3.json
--rw-r--r--   0 runner    (1001) docker     (123)    10192 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ssm/resources/ami-amazon-linux-latest/ap-south-1.json
--rw-r--r--   0 runner    (1001) docker     (123)     6642 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ssm/resources/ami-amazon-linux-latest/ap-south-2.json
--rw-r--r--   0 runner    (1001) docker     (123)    11685 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ssm/resources/ami-amazon-linux-latest/ap-southeast-1.json
--rw-r--r--   0 runner    (1001) docker     (123)    11683 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ssm/resources/ami-amazon-linux-latest/ap-southeast-2.json
--rw-r--r--   0 runner    (1001) docker     (123)     9614 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ssm/resources/ami-amazon-linux-latest/ap-southeast-3.json
--rw-r--r--   0 runner    (1001) docker     (123)    10251 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ssm/resources/ami-amazon-linux-latest/ca-central-1.json
--rw-r--r--   0 runner    (1001) docker     (123)    11616 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ssm/resources/ami-amazon-linux-latest/eu-central-1.json
--rw-r--r--   0 runner    (1001) docker     (123)     6682 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ssm/resources/ami-amazon-linux-latest/eu-central-2.json
--rw-r--r--   0 runner    (1001) docker     (123)    10193 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ssm/resources/ami-amazon-linux-latest/eu-north-1.json
--rw-r--r--   0 runner    (1001) docker     (123)    10191 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ssm/resources/ami-amazon-linux-latest/eu-south-1.json
--rw-r--r--   0 runner    (1001) docker     (123)     6645 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ssm/resources/ami-amazon-linux-latest/eu-south-2.json
--rw-r--r--   0 runner    (1001) docker     (123)    11520 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ssm/resources/ami-amazon-linux-latest/eu-west-1.json
--rw-r--r--   0 runner    (1001) docker     (123)    10161 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ssm/resources/ami-amazon-linux-latest/eu-west-2.json
--rw-r--r--   0 runner    (1001) docker     (123)    10160 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ssm/resources/ami-amazon-linux-latest/eu-west-3.json
--rw-r--r--   0 runner    (1001) docker     (123)     9562 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ssm/resources/ami-amazon-linux-latest/me-central-1.json
--rw-r--r--   0 runner    (1001) docker     (123)    10193 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ssm/resources/ami-amazon-linux-latest/me-south-1.json
--rw-r--r--   0 runner    (1001) docker     (123)    11520 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ssm/resources/ami-amazon-linux-latest/sa-east-1.json
--rw-r--r--   0 runner    (1001) docker     (123)    11520 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ssm/resources/ami-amazon-linux-latest/us-east-1.json
--rw-r--r--   0 runner    (1001) docker     (123)    10165 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ssm/resources/ami-amazon-linux-latest/us-east-2.json
--rw-r--r--   0 runner    (1001) docker     (123)    11516 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ssm/resources/ami-amazon-linux-latest/us-west-1.json
--rw-r--r--   0 runner    (1001) docker     (123)    11520 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ssm/resources/ami-amazon-linux-latest/us-west-2.json
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:52.713514 moto-4.1.7.dev8/moto/ssm/resources/ecs/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:52.997517 moto-4.1.7.dev8/moto/ssm/resources/ecs/optimized_amis/
--rw-r--r--   0 runner    (1001) docker     (123)   416937 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ssm/resources/ecs/optimized_amis/af-south-1.json
--rw-r--r--   0 runner    (1001) docker     (123)   688021 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ssm/resources/ecs/optimized_amis/ap-east-1.json
--rw-r--r--   0 runner    (1001) docker     (123)   807102 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ssm/resources/ecs/optimized_amis/ap-northeast-1.json
--rw-r--r--   0 runner    (1001) docker     (123)   738181 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ssm/resources/ecs/optimized_amis/ap-northeast-2.json
--rw-r--r--   0 runner    (1001) docker     (123)   360357 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ssm/resources/ecs/optimized_amis/ap-northeast-3.json
--rw-r--r--   0 runner    (1001) docker     (123)   798560 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ssm/resources/ecs/optimized_amis/ap-south-1.json
--rw-r--r--   0 runner    (1001) docker     (123)    85325 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ssm/resources/ecs/optimized_amis/ap-south-2.json
--rw-r--r--   0 runner    (1001) docker     (123)   778515 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ssm/resources/ecs/optimized_amis/ap-southeast-1.json
--rw-r--r--   0 runner    (1001) docker     (123)   807102 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ssm/resources/ecs/optimized_amis/ap-southeast-2.json
--rw-r--r--   0 runner    (1001) docker     (123)   239300 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ssm/resources/ecs/optimized_amis/ap-southeast-3.json
--rw-r--r--   0 runner    (1001) docker     (123)   734929 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ssm/resources/ecs/optimized_amis/ca-central-1.json
--rw-r--r--   0 runner    (1001) docker     (123)   806032 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ssm/resources/ecs/optimized_amis/eu-central-1.json
--rw-r--r--   0 runner    (1001) docker     (123)    84904 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ssm/resources/ecs/optimized_amis/eu-central-2.json
--rw-r--r--   0 runner    (1001) docker     (123)   717425 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ssm/resources/ecs/optimized_amis/eu-north-1.json
--rw-r--r--   0 runner    (1001) docker     (123)   618637 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ssm/resources/ecs/optimized_amis/eu-south-1.json
--rw-r--r--   0 runner    (1001) docker     (123)    99223 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ssm/resources/ecs/optimized_amis/eu-south-2.json
--rw-r--r--   0 runner    (1001) docker     (123)   815560 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ssm/resources/ecs/optimized_amis/eu-west-1.json
--rw-r--r--   0 runner    (1001) docker     (123)   737073 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ssm/resources/ecs/optimized_amis/eu-west-2.json
--rw-r--r--   0 runner    (1001) docker     (123)   737391 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ssm/resources/ecs/optimized_amis/eu-west-3.json
--rw-r--r--   0 runner    (1001) docker     (123)   164329 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ssm/resources/ecs/optimized_amis/me-central-1.json
--rw-r--r--   0 runner    (1001) docker     (123)   659463 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ssm/resources/ecs/optimized_amis/me-south-1.json
--rw-r--r--   0 runner    (1001) docker     (123)   761741 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ssm/resources/ecs/optimized_amis/sa-east-1.json
--rw-r--r--   0 runner    (1001) docker     (123)   823629 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ssm/resources/ecs/optimized_amis/us-east-1.json
--rw-r--r--   0 runner    (1001) docker     (123)   815560 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ssm/resources/ecs/optimized_amis/us-east-2.json
--rw-r--r--   0 runner    (1001) docker     (123)   767008 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ssm/resources/ecs/optimized_amis/us-west-1.json
--rw-r--r--   0 runner    (1001) docker     (123)   820874 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ssm/resources/ecs/optimized_amis/us-west-2.json
--rw-r--r--   0 runner    (1001) docker     (123)  1695456 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ssm/resources/regions.json
--rw-r--r--   0 runner    (1001) docker     (123)  1773533 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ssm/resources/services.json
--rw-r--r--   0 runner    (1001) docker     (123)    15018 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ssm/responses.py
--rw-r--r--   0 runner    (1001) docker     (123)      219 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ssm/urls.py
--rw-r--r--   0 runner    (1001) docker     (123)     1224 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ssm/utils.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:52.997517 moto-4.1.7.dev8/moto/ssoadmin/
--rw-r--r--   0 runner    (1001) docker     (123)      199 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ssoadmin/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      227 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ssoadmin/exceptions.py
--rw-r--r--   0 runner    (1001) docker     (123)     8104 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ssoadmin/models.py
--rw-r--r--   0 runner    (1001) docker     (123)     5455 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ssoadmin/responses.py
--rw-r--r--   0 runner    (1001) docker     (123)      192 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ssoadmin/urls.py
--rw-r--r--   0 runner    (1001) docker     (123)      253 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/ssoadmin/utils.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:53.001517 moto-4.1.7.dev8/moto/stepfunctions/
--rw-r--r--   0 runner    (1001) docker     (123)      143 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/stepfunctions/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      915 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/stepfunctions/exceptions.py
--rw-r--r--   0 runner    (1001) docker     (123)    21074 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/stepfunctions/models.py
--rw-r--r--   0 runner    (1001) docker     (123)     6755 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/stepfunctions/responses.py
--rw-r--r--   0 runner    (1001) docker     (123)      153 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/stepfunctions/urls.py
--rw-r--r--   0 runner    (1001) docker     (123)      691 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/stepfunctions/utils.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:53.001517 moto-4.1.7.dev8/moto/sts/
--rw-r--r--   0 runner    (1001) docker     (123)      115 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/sts/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      239 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/sts/exceptions.py
--rw-r--r--   0 runner    (1001) docker     (123)     6610 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/sts/models.py
--rw-r--r--   0 runner    (1001) docker     (123)     8761 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/sts/responses.py
--rw-r--r--   0 runner    (1001) docker     (123)      138 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/sts/urls.py
--rw-r--r--   0 runner    (1001) docker     (123)      759 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/sts/utils.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:53.001517 moto-4.1.7.dev8/moto/support/
--rw-r--r--   0 runner    (1001) docker     (123)      127 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/support/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/support/exceptions.py
--rw-r--r--   0 runner    (1001) docker     (123)     7989 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/support/models.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:53.001517 moto-4.1.7.dev8/moto/support/resources/
--rw-r--r--   0 runner    (1001) docker     (123)   172189 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/support/resources/describe_trusted_advisor_checks.json
--rw-r--r--   0 runner    (1001) docker     (123)     2461 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/support/responses.py
--rw-r--r--   0 runner    (1001) docker     (123)      153 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/support/urls.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:53.005517 moto-4.1.7.dev8/moto/swf/
--rw-r--r--   0 runner    (1001) docker     (123)      115 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/swf/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     4265 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/swf/constants.py
--rw-r--r--   0 runner    (1001) docker     (123)     3795 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/swf/exceptions.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:53.005517 moto-4.1.7.dev8/moto/swf/models/
--rw-r--r--   0 runner    (1001) docker     (123)    18122 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/swf/models/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     2909 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/swf/models/activity_task.py
--rw-r--r--   0 runner    (1001) docker     (123)      397 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/swf/models/activity_type.py
--rw-r--r--   0 runner    (1001) docker     (123)     2904 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/swf/models/decision_task.py
--rw-r--r--   0 runner    (1001) docker     (123)     4456 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/swf/models/domain.py
--rw-r--r--   0 runner    (1001) docker     (123)     1982 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/swf/models/generic_type.py
--rw-r--r--   0 runner    (1001) docker     (123)     2434 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/swf/models/history_event.py
--rw-r--r--   0 runner    (1001) docker     (123)      310 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/swf/models/timeout.py
--rw-r--r--   0 runner    (1001) docker     (123)      425 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/swf/models/timer.py
--rw-r--r--   0 runner    (1001) docker     (123)    30491 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/swf/models/workflow_execution.py
--rw-r--r--   0 runner    (1001) docker     (123)      409 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/swf/models/workflow_type.py
--rw-r--r--   0 runner    (1001) docker     (123)    21829 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/swf/responses.py
--rw-r--r--   0 runner    (1001) docker     (123)      133 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/swf/urls.py
--rw-r--r--   0 runner    (1001) docker     (123)       59 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/swf/utils.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:53.009517 moto-4.1.7.dev8/moto/textract/
--rw-r--r--   0 runner    (1001) docker     (123)      199 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/textract/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      981 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/textract/exceptions.py
--rw-r--r--   0 runner    (1001) docker     (123)     1937 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/textract/models.py
--rw-r--r--   0 runner    (1001) docker     (123)     1081 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/textract/responses.py
--rw-r--r--   0 runner    (1001) docker     (123)      196 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/textract/urls.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:53.009517 moto-4.1.7.dev8/moto/timestreamwrite/
--rw-r--r--   0 runner    (1001) docker     (123)      151 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/timestreamwrite/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      313 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/timestreamwrite/exceptions.py
--rw-r--r--   0 runner    (1001) docker     (123)     8111 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/timestreamwrite/models.py
--rw-r--r--   0 runner    (1001) docker     (123)     4991 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/timestreamwrite/responses.py
--rw-r--r--   0 runner    (1001) docker     (123)      463 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/timestreamwrite/urls.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:53.009517 moto-4.1.7.dev8/moto/transcribe/
--rw-r--r--   0 runner    (1001) docker     (123)      190 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/transcribe/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      351 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/transcribe/exceptions.py
--rw-r--r--   0 runner    (1001) docker     (123)    31162 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/transcribe/models.py
--rw-r--r--   0 runner    (1001) docker     (123)     8194 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/transcribe/responses.py
--rw-r--r--   0 runner    (1001) docker     (123)      154 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/transcribe/urls.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:53.009517 moto-4.1.7.dev8/moto/utilities/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/utilities/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     2341 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/utilities/aws_headers.py
--rw-r--r--   0 runner    (1001) docker     (123)     9139 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/utilities/distutils_version.py
--rw-r--r--   0 runner    (1001) docker     (123)     2318 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/utilities/docker_utilities.py
--rw-r--r--   0 runner    (1001) docker     (123)     7404 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/utilities/paginator.py
--rw-r--r--   0 runner    (1001) docker     (123)     7572 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/utilities/tagging_service.py
--rw-r--r--   0 runner    (1001) docker     (123)     2059 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/utilities/tokenizer.py
--rw-r--r--   0 runner    (1001) docker     (123)     2784 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/utilities/utils.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:53.013517 moto-4.1.7.dev8/moto/wafv2/
--rw-r--r--   0 runner    (1001) docker     (123)      165 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/wafv2/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      633 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/wafv2/exceptions.py
--rw-r--r--   0 runner    (1001) docker     (123)     6397 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/wafv2/models.py
--rw-r--r--   0 runner    (1001) docker     (123)     6140 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/wafv2/responses.py
--rw-r--r--   0 runner    (1001) docker     (123)      151 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/wafv2/urls.py
--rw-r--r--   0 runner    (1001) docker     (123)      401 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/wafv2/utils.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:53.013517 moto-4.1.7.dev8/moto/xray/
--rw-r--r--   0 runner    (1001) docker     (123)      257 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/xray/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      568 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/xray/exceptions.py
--rw-r--r--   0 runner    (1001) docker     (123)     3548 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/xray/mock_client.py
--rw-r--r--   0 runner    (1001) docker     (123)    10130 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/xray/models.py
--rw-r--r--   0 runner    (1001) docker     (123)     5909 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/xray/responses.py
--rw-r--r--   0 runner    (1001) docker     (123)      393 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/moto/xray/urls.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:52.745515 moto-4.1.7.dev8/moto.egg-info/
--rw-r--r--   0 runner    (1001) docker     (123)     6287 2023-03-28 19:17:52.000000 moto-4.1.7.dev8/moto.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)    65063 2023-03-28 19:17:52.000000 moto-4.1.7.dev8/moto.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-03-28 19:17:52.000000 moto-4.1.7.dev8/moto.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (123)       49 2023-03-28 19:17:52.000000 moto-4.1.7.dev8/moto.egg-info/entry_points.txt
--rw-r--r--   0 runner    (1001) docker     (123)     2839 2023-03-28 19:17:52.000000 moto-4.1.7.dev8/moto.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (123)        5 2023-03-28 19:17:52.000000 moto-4.1.7.dev8/moto.egg-info/top_level.txt
--rw-r--r--   0 runner    (1001) docker     (123)       91 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/pyproject.toml
--rw-r--r--   0 runner    (1001) docker     (123)      162 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/requirements-dev.txt
--rw-r--r--   0 runner    (1001) docker     (123)       49 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/requirements.txt
--rw-r--r--   0 runner    (1001) docker     (123)     5500 2023-03-28 19:17:53.197519 moto-4.1.7.dev8/setup.cfg
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:53.013517 moto-4.1.7.dev8/tests/
--rw-r--r--   0 runner    (1001) docker     (123)      517 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     1310 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/helpers.py
--rw-r--r--   0 runner    (1001) docker     (123)      196 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/markers.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:53.013517 moto-4.1.7.dev8/tests/test_acm/
--rw-r--r--   0 runner    (1001) docker     (123)       41 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_acm/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:53.017517 moto-4.1.7.dev8/tests/test_acm/resources/
--rw-r--r--   0 runner    (1001) docker     (123)     1945 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_acm/resources/README.md
--rw-r--r--   0 runner    (1001) docker     (123)       41 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_acm/resources/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     3243 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_acm/resources/ca.key
--rw-r--r--   0 runner    (1001) docker     (123)     3502 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_acm/resources/ca.pem
--rw-r--r--   0 runner    (1001) docker     (123)       17 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_acm/resources/ca.srl
--rw-r--r--   0 runner    (1001) docker     (123)     1589 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_acm/resources/star_moto_com-bad.pem
--rw-r--r--   0 runner    (1001) docker     (123)     1017 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_acm/resources/star_moto_com.csr
--rw-r--r--   0 runner    (1001) docker     (123)     1675 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_acm/resources/star_moto_com.key
--rw-r--r--   0 runner    (1001) docker     (123)     1558 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_acm/resources/star_moto_com.pem
--rw-r--r--   0 runner    (1001) docker     (123)    25475 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_acm/test_acm.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:53.017517 moto-4.1.7.dev8/tests/test_acmpca/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_acmpca/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    12974 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_acmpca/test_acmpca.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:53.017517 moto-4.1.7.dev8/tests/test_amp/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_amp/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     2167 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_amp/test_amp_logging_config.py
--rw-r--r--   0 runner    (1001) docker     (123)     6058 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_amp/test_amp_rulegroupnamespaces.py
--rw-r--r--   0 runner    (1001) docker     (123)     5042 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_amp/test_amp_workspaces.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:53.021518 moto-4.1.7.dev8/tests/test_apigateway/
--rw-r--r--   0 runner    (1001) docker     (123)       41 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_apigateway/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:53.025518 moto-4.1.7.dev8/tests/test_apigateway/resources/
--rw-r--r--   0 runner    (1001) docker     (123)    21989 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_apigateway/resources/petstore-swagger-v3.yaml
--rw-r--r--   0 runner    (1001) docker     (123)     1656 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_apigateway/resources/test_api.json
--rw-r--r--   0 runner    (1001) docker     (123)     1294 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_apigateway/resources/test_api.yaml
--rw-r--r--   0 runner    (1001) docker     (123)     1642 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_apigateway/resources/test_api_invalid.json
--rw-r--r--   0 runner    (1001) docker     (123)     1641 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_apigateway/resources/test_api_invalid_version.json
--rw-r--r--   0 runner    (1001) docker     (123)     1062 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_apigateway/resources/test_deep_api.yaml
--rw-r--r--   0 runner    (1001) docker     (123)    91555 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_apigateway/test_apigateway.py
--rw-r--r--   0 runner    (1001) docker     (123)    10430 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_apigateway/test_apigateway_cloudformation.py
--rw-r--r--   0 runner    (1001) docker     (123)     7799 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_apigateway/test_apigateway_deployments.py
--rw-r--r--   0 runner    (1001) docker     (123)     3117 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_apigateway/test_apigateway_export.py
--rw-r--r--   0 runner    (1001) docker     (123)     5216 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_apigateway/test_apigateway_gatewayresponses.py
--rw-r--r--   0 runner    (1001) docker     (123)     3228 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_apigateway/test_apigateway_importrestapi.py
--rw-r--r--   0 runner    (1001) docker     (123)     7942 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_apigateway/test_apigateway_integration.py
--rw-r--r--   0 runner    (1001) docker     (123)     7637 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_apigateway/test_apigateway_putrestapi.py
--rw-r--r--   0 runner    (1001) docker     (123)    18926 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_apigateway/test_apigateway_stage.py
--rw-r--r--   0 runner    (1001) docker     (123)     4856 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_apigateway/test_apigateway_validators.py
--rw-r--r--   0 runner    (1001) docker     (123)     3144 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_apigateway/test_apigateway_vpclink.py
--rw-r--r--   0 runner    (1001) docker     (123)     5294 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_apigateway/test_server.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:53.025518 moto-4.1.7.dev8/tests/test_apigatewayv2/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_apigatewayv2/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    11724 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_apigatewayv2/test_apigatewayv2.py
--rw-r--r--   0 runner    (1001) docker     (123)     7989 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_apigatewayv2/test_apigatewayv2_authorizers.py
--rw-r--r--   0 runner    (1001) docker     (123)     3242 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_apigatewayv2/test_apigatewayv2_domains.py
--rw-r--r--   0 runner    (1001) docker     (123)     6738 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_apigatewayv2/test_apigatewayv2_integrationresponses.py
--rw-r--r--   0 runner    (1001) docker     (123)    12319 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_apigatewayv2/test_apigatewayv2_integrations.py
--rw-r--r--   0 runner    (1001) docker     (123)     6837 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_apigatewayv2/test_apigatewayv2_mappings.py
--rw-r--r--   0 runner    (1001) docker     (123)     3858 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_apigatewayv2/test_apigatewayv2_models.py
--rw-r--r--   0 runner    (1001) docker     (123)     5621 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_apigatewayv2/test_apigatewayv2_reimport.py
--rw-r--r--   0 runner    (1001) docker     (123)    11181 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_apigatewayv2/test_apigatewayv2_routes.py
--rw-r--r--   0 runner    (1001) docker     (123)     1965 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_apigatewayv2/test_apigatewayv2_tags.py
--rw-r--r--   0 runner    (1001) docker     (123)     5184 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_apigatewayv2/test_apigatewayv2_vpclinks.py
--rw-r--r--   0 runner    (1001) docker     (123)      360 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_apigatewayv2/test_server.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:53.025518 moto-4.1.7.dev8/tests/test_applicationautoscaling/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_applicationautoscaling/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    25197 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_applicationautoscaling/test_applicationautoscaling.py
--rw-r--r--   0 runner    (1001) docker     (123)     4077 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_applicationautoscaling/test_validation.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:53.029518 moto-4.1.7.dev8/tests/test_appsync/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_appsync/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     5489 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_appsync/test_appsync.py
--rw-r--r--   0 runner    (1001) docker     (123)     3519 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_appsync/test_appsync_apikeys.py
--rw-r--r--   0 runner    (1001) docker     (123)     2646 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_appsync/test_appsync_schema.py
--rw-r--r--   0 runner    (1001) docker     (123)     2857 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_appsync/test_appsync_tags.py
--rw-r--r--   0 runner    (1001) docker     (123)      490 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_appsync/test_server.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:53.029518 moto-4.1.7.dev8/tests/test_athena/
--rw-r--r--   0 runner    (1001) docker     (123)       41 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_athena/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    14774 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_athena/test_athena.py
--rw-r--r--   0 runner    (1001) docker     (123)     5393 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_athena/test_athena_server_api.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:53.033518 moto-4.1.7.dev8/tests/test_autoscaling/
--rw-r--r--   0 runner    (1001) docker     (123)       41 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_autoscaling/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    48170 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_autoscaling/test_autoscaling.py
--rw-r--r--   0 runner    (1001) docker     (123)    17392 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_autoscaling/test_autoscaling_cloudformation.py
--rw-r--r--   0 runner    (1001) docker     (123)     9658 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_autoscaling/test_autoscaling_groups.py
--rw-r--r--   0 runner    (1001) docker     (123)     1494 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_autoscaling/test_autoscaling_metrics.py
--rw-r--r--   0 runner    (1001) docker     (123)     3150 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_autoscaling/test_autoscaling_scheduledactions.py
--rw-r--r--   0 runner    (1001) docker     (123)     8692 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_autoscaling/test_autoscaling_tags.py
--rw-r--r--   0 runner    (1001) docker     (123)    40671 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_autoscaling/test_elb.py
--rw-r--r--   0 runner    (1001) docker     (123)     4184 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_autoscaling/test_elbv2.py
--rw-r--r--   0 runner    (1001) docker     (123)    12469 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_autoscaling/test_launch_configurations.py
--rw-r--r--   0 runner    (1001) docker     (123)     5331 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_autoscaling/test_policies.py
--rw-r--r--   0 runner    (1001) docker     (123)      458 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_autoscaling/test_server.py
--rw-r--r--   0 runner    (1001) docker     (123)      933 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_autoscaling/utils.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:53.033518 moto-4.1.7.dev8/tests/test_awslambda/
--rw-r--r--   0 runner    (1001) docker     (123)       41 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_awslambda/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    11564 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_awslambda/test_awslambda_cloudformation.py
--rw-r--r--   0 runner    (1001) docker     (123)    46812 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_awslambda/test_lambda.py
--rw-r--r--   0 runner    (1001) docker     (123)    10044 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_awslambda/test_lambda_alias.py
--rw-r--r--   0 runner    (1001) docker     (123)     2799 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_awslambda/test_lambda_concurrency.py
--rw-r--r--   0 runner    (1001) docker     (123)    15860 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_awslambda/test_lambda_eventsourcemapping.py
--rw-r--r--   0 runner    (1001) docker     (123)     4021 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_awslambda/test_lambda_function_urls.py
--rw-r--r--   0 runner    (1001) docker     (123)    12979 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_awslambda/test_lambda_invoke.py
--rw-r--r--   0 runner    (1001) docker     (123)     9713 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_awslambda/test_lambda_layers.py
--rw-r--r--   0 runner    (1001) docker     (123)     9427 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_awslambda/test_lambda_policy.py
--rw-r--r--   0 runner    (1001) docker     (123)     4087 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_awslambda/test_lambda_tags.py
--rw-r--r--   0 runner    (1001) docker     (123)     1380 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_awslambda/test_policy.py
--rw-r--r--   0 runner    (1001) docker     (123)     5610 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_awslambda/utilities.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:53.037518 moto-4.1.7.dev8/tests/test_batch/
--rw-r--r--   0 runner    (1001) docker     (123)     1387 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_batch/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      333 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_batch/test_batch.py
--rw-r--r--   0 runner    (1001) docker     (123)     9596 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_batch/test_batch_cloudformation.py
--rw-r--r--   0 runner    (1001) docker     (123)    13474 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_batch/test_batch_compute_envs.py
--rw-r--r--   0 runner    (1001) docker     (123)     6948 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_batch/test_batch_job_queue.py
--rw-r--r--   0 runner    (1001) docker     (123)    34446 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_batch/test_batch_jobs.py
--rw-r--r--   0 runner    (1001) docker     (123)     2989 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_batch/test_batch_scheduling_policy.py
--rw-r--r--   0 runner    (1001) docker     (123)     2021 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_batch/test_batch_tags_job_definition.py
--rw-r--r--   0 runner    (1001) docker     (123)     4137 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_batch/test_batch_tags_job_queue.py
--rw-r--r--   0 runner    (1001) docker     (123)      368 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_batch/test_batch_tags_scheduling_policy.py
--rw-r--r--   0 runner    (1001) docker     (123)    11540 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_batch/test_batch_task_definition.py
--rw-r--r--   0 runner    (1001) docker     (123)      381 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_batch/test_server.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:53.037518 moto-4.1.7.dev8/tests/test_batch_simple/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_batch_simple/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     9807 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_batch_simple/test_batch_cloudformation.py
--rw-r--r--   0 runner    (1001) docker     (123)     3473 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_batch_simple/test_batch_compute_envs.py
--rw-r--r--   0 runner    (1001) docker     (123)     3374 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_batch_simple/test_batch_jobs.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:53.041518 moto-4.1.7.dev8/tests/test_budgets/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_budgets/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     6679 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_budgets/test_budgets.py
--rw-r--r--   0 runner    (1001) docker     (123)     6974 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_budgets/test_notifications.py
--rw-r--r--   0 runner    (1001) docker     (123)      516 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_budgets/test_server.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:53.041518 moto-4.1.7.dev8/tests/test_ce/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_ce/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     4466 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_ce/test_ce.py
--rw-r--r--   0 runner    (1001) docker     (123)     1998 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_ce/test_ce_tags.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:53.045518 moto-4.1.7.dev8/tests/test_cloudformation/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_cloudformation/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:53.049518 moto-4.1.7.dev8/tests/test_cloudformation/fixtures/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_cloudformation/fixtures/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     3233 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_cloudformation/fixtures/custom_lambda.py
--rw-r--r--   0 runner    (1001) docker     (123)       64 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_cloudformation/fixtures/ec2_classic_eip.py
--rw-r--r--   0 runner    (1001) docker     (123)      243 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_cloudformation/fixtures/fn_join.py
--rw-r--r--   0 runner    (1001) docker     (123)     1604 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_cloudformation/fixtures/kms_key.py
--rw-r--r--   0 runner    (1001) docker     (123)     8837 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_cloudformation/fixtures/rds_mysql_with_db_parameter_group.py
--rw-r--r--   0 runner    (1001) docker     (123)     8550 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_cloudformation/fixtures/rds_mysql_with_read_replica.py
--rw-r--r--   0 runner    (1001) docker     (123)     7040 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_cloudformation/fixtures/redshift.py
--rw-r--r--   0 runner    (1001) docker     (123)     1277 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_cloudformation/fixtures/route53_ec2_instance_with_public_ip.py
--rw-r--r--   0 runner    (1001) docker     (123)     1052 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_cloudformation/fixtures/route53_health_check.py
--rw-r--r--   0 runner    (1001) docker     (123)     3189 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_cloudformation/fixtures/route53_roundrobin.py
--rw-r--r--   0 runner    (1001) docker     (123)    10926 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_cloudformation/fixtures/single_instance_with_ebs_volume.py
--rw-r--r--   0 runner    (1001) docker     (123)      106 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_cloudformation/fixtures/vpc_eip.py
--rw-r--r--   0 runner    (1001) docker     (123)      939 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_cloudformation/fixtures/vpc_eni.py
--rw-r--r--   0 runner    (1001) docker     (123)    12162 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_cloudformation/fixtures/vpc_single_instance_in_subnet.py
--rw-r--r--   0 runner    (1001) docker     (123)     8625 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_cloudformation/test_cloudformation_custom_resources.py
--rw-r--r--   0 runner    (1001) docker     (123)     5440 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_cloudformation/test_cloudformation_depends_on.py
--rw-r--r--   0 runner    (1001) docker     (123)    12559 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_cloudformation/test_cloudformation_multi_accounts.py
--rw-r--r--   0 runner    (1001) docker     (123)     6373 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_cloudformation/test_cloudformation_nested_stacks.py
--rw-r--r--   0 runner    (1001) docker     (123)    85564 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_cloudformation/test_cloudformation_stack_crud_boto3.py
--rw-r--r--   0 runner    (1001) docker     (123)    69300 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_cloudformation/test_cloudformation_stack_integration.py
--rw-r--r--   0 runner    (1001) docker     (123)     4223 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_cloudformation/test_cloudformation_stack_policies.py
--rw-r--r--   0 runner    (1001) docker     (123)     2949 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_cloudformation/test_import_value.py
--rw-r--r--   0 runner    (1001) docker     (123)     1051 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_cloudformation/test_server.py
--rw-r--r--   0 runner    (1001) docker     (123)    20743 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_cloudformation/test_stack_parsing.py
--rw-r--r--   0 runner    (1001) docker     (123)     4442 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_cloudformation/test_validate.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:53.049518 moto-4.1.7.dev8/tests/test_cloudfront/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_cloudfront/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     2446 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_cloudfront/cloudfront_test_scaffolding.py
--rw-r--r--   0 runner    (1001) docker     (123)    10114 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_cloudfront/test_cloudfront.py
--rw-r--r--   0 runner    (1001) docker     (123)     1582 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_cloudfront/test_cloudfront_dist_tags.py
--rw-r--r--   0 runner    (1001) docker     (123)    28631 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_cloudfront/test_cloudfront_distributions.py
--rw-r--r--   0 runner    (1001) docker     (123)     2938 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_cloudfront/test_cloudfront_invalidation.py
--rw-r--r--   0 runner    (1001) docker     (123)      489 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_cloudfront/test_server.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:53.049518 moto-4.1.7.dev8/tests/test_cloudtrail/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_cloudtrail/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    21003 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_cloudtrail/test_cloudtrail.py
--rw-r--r--   0 runner    (1001) docker     (123)     6377 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_cloudtrail/test_cloudtrail_eventselectors.py
--rw-r--r--   0 runner    (1001) docker     (123)     2539 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_cloudtrail/test_cloudtrail_tags.py
--rw-r--r--   0 runner    (1001) docker     (123)      541 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_cloudtrail/test_server.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:53.053518 moto-4.1.7.dev8/tests/test_cloudwatch/
--rw-r--r--   0 runner    (1001) docker     (123)       41 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_cloudwatch/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     8634 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_cloudwatch/test_cloudwatch_alarms.py
--rw-r--r--   0 runner    (1001) docker     (123)    54006 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_cloudwatch/test_cloudwatch_boto3.py
--rw-r--r--   0 runner    (1001) docker     (123)     3368 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_cloudwatch/test_cloudwatch_dashboards.py
--rw-r--r--   0 runner    (1001) docker     (123)     6388 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_cloudwatch/test_cloudwatch_tags.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:53.053518 moto-4.1.7.dev8/tests/test_codebuild/
--rw-r--r--   0 runner    (1001) docker     (123)    19951 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_codebuild/test_codebuild.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:53.053518 moto-4.1.7.dev8/tests/test_codecommit/
--rw-r--r--   0 runner    (1001) docker     (123)     8512 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_codecommit/test_codecommit.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:53.053518 moto-4.1.7.dev8/tests/test_codepipeline/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_codepipeline/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    25530 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_codepipeline/test_codepipeline.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:53.057518 moto-4.1.7.dev8/tests/test_cognitoidentity/
--rw-r--r--   0 runner    (1001) docker     (123)       41 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_cognitoidentity/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     8947 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_cognitoidentity/test_cognitoidentity.py
--rw-r--r--   0 runner    (1001) docker     (123)     3130 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_cognitoidentity/test_server.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:53.057518 moto-4.1.7.dev8/tests/test_cognitoidp/
--rw-r--r--   0 runner    (1001) docker     (123)       41 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_cognitoidp/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)   161791 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_cognitoidp/test_cognitoidp.py
--rw-r--r--   0 runner    (1001) docker     (123)     3560 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_cognitoidp/test_cognitoidp_exceptions.py
--rw-r--r--   0 runner    (1001) docker     (123)     3858 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_cognitoidp/test_cognitoidp_replay.py
--rw-r--r--   0 runner    (1001) docker     (123)     6356 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_cognitoidp/test_server.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:53.061518 moto-4.1.7.dev8/tests/test_comprehend/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_comprehend/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     7440 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_comprehend/test_comprehend.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:53.061518 moto-4.1.7.dev8/tests/test_config/
--rw-r--r--   0 runner    (1001) docker     (123)       41 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_config/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    78639 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_config/test_config.py
--rw-r--r--   0 runner    (1001) docker     (123)    18070 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_config/test_config_rules.py
--rw-r--r--   0 runner    (1001) docker     (123)    11670 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_config/test_config_rules_integration.py
--rw-r--r--   0 runner    (1001) docker     (123)    11741 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_config/test_config_tags.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:53.073518 moto-4.1.7.dev8/tests/test_core/
--rw-r--r--   0 runner    (1001) docker     (123)       41 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_core/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     2580 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_core/test_account_id_resolution.py
--rw-r--r--   0 runner    (1001) docker     (123)    26898 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_core/test_auth.py
--rw-r--r--   0 runner    (1001) docker     (123)     9624 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_core/test_backenddict.py
--rw-r--r--   0 runner    (1001) docker     (123)      501 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_core/test_context_manager.py
--rw-r--r--   0 runner    (1001) docker     (123)     9923 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_core/test_decorator_calls.py
--rw-r--r--   0 runner    (1001) docker     (123)      929 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_core/test_docker.py
--rw-r--r--   0 runner    (1001) docker     (123)     1074 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_core/test_environ_patching.py
--rw-r--r--   0 runner    (1001) docker     (123)     3261 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_core/test_importorder.py
--rw-r--r--   0 runner    (1001) docker     (123)     1297 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_core/test_instance_metadata.py
--rw-r--r--   0 runner    (1001) docker     (123)      959 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_core/test_mock_all.py
--rw-r--r--   0 runner    (1001) docker     (123)     2232 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_core/test_mock_regions.py
--rw-r--r--   0 runner    (1001) docker     (123)     4951 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_core/test_moto_api.py
--rw-r--r--   0 runner    (1001) docker     (123)      736 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_core/test_nested.py
--rw-r--r--   0 runner    (1001) docker     (123)     1493 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_core/test_request_mocking.py
--rw-r--r--   0 runner    (1001) docker     (123)     8330 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_core/test_responses.py
--rw-r--r--   0 runner    (1001) docker     (123)     2012 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_core/test_responses_module.py
--rw-r--r--   0 runner    (1001) docker     (123)     1543 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_core/test_server.py
--rw-r--r--   0 runner    (1001) docker     (123)      758 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_core/test_settings.py
--rw-r--r--   0 runner    (1001) docker     (123)      326 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_core/test_socket.py
--rw-r--r--   0 runner    (1001) docker     (123)      920 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_core/test_url_base_regex.py
--rw-r--r--   0 runner    (1001) docker     (123)      733 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_core/test_url_mapping.py
--rw-r--r--   0 runner    (1001) docker     (123)     1455 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_core/test_utils.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:53.077518 moto-4.1.7.dev8/tests/test_databrew/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_databrew/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     8669 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_databrew/test_databrew_datasets.py
--rw-r--r--   0 runner    (1001) docker     (123)    13383 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_databrew/test_databrew_jobs.py
--rw-r--r--   0 runner    (1001) docker     (123)    19199 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_databrew/test_databrew_recipes.py
--rw-r--r--   0 runner    (1001) docker     (123)     5426 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_databrew/test_databrew_rulesets.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:53.077518 moto-4.1.7.dev8/tests/test_datapipeline/
--rw-r--r--   0 runner    (1001) docker     (123)       41 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_datapipeline/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     6242 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_datapipeline/test_datapipeline.py
--rw-r--r--   0 runner    (1001) docker     (123)     2736 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_datapipeline/test_datapipeline_cloudformation.py
--rw-r--r--   0 runner    (1001) docker     (123)      586 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_datapipeline/test_server.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:53.077518 moto-4.1.7.dev8/tests/test_datasync/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_datasync/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    14878 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_datasync/test_datasync.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:53.081518 moto-4.1.7.dev8/tests/test_dax/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_dax/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    16182 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_dax/test_dax.py
--rw-r--r--   0 runner    (1001) docker     (123)      376 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_dax/test_server.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:53.081518 moto-4.1.7.dev8/tests/test_dms/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_dms/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     7191 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_dms/test_dms.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:53.085518 moto-4.1.7.dev8/tests/test_ds/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_ds/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    13394 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_ds/test_ds.py
--rw-r--r--   0 runner    (1001) docker     (123)    11204 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_ds/test_ds_ad_connect.py
--rw-r--r--   0 runner    (1001) docker     (123)     8960 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_ds/test_ds_microsoft_ad.py
--rw-r--r--   0 runner    (1001) docker     (123)     9095 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_ds/test_ds_simple_ad_directory.py
--rw-r--r--   0 runner    (1001) docker     (123)     4751 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_ds/test_ds_tags.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:53.093518 moto-4.1.7.dev8/tests/test_dynamodb/
--rw-r--r--   0 runner    (1001) docker     (123)       41 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_dynamodb/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      545 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_dynamodb/conftest.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:53.093518 moto-4.1.7.dev8/tests/test_dynamodb/exceptions/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_dynamodb/exceptions/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    39637 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_dynamodb/exceptions/test_dynamodb_exceptions.py
--rw-r--r--   0 runner    (1001) docker     (123)    12004 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_dynamodb/exceptions/test_key_length_exceptions.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:53.093518 moto-4.1.7.dev8/tests/test_dynamodb/models/
--rw-r--r--   0 runner    (1001) docker     (123)     7419 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_dynamodb/models/test_key_condition_expression_parser.py
--rw-r--r--   0 runner    (1001) docker     (123)   204428 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_dynamodb/test_dynamodb.py
--rw-r--r--   0 runner    (1001) docker     (123)     8093 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_dynamodb/test_dynamodb_batch_get_item.py
--rw-r--r--   0 runner    (1001) docker     (123)     1619 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_dynamodb/test_dynamodb_cloudformation.py
--rw-r--r--   0 runner    (1001) docker     (123)    15796 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_dynamodb/test_dynamodb_condition_expressions.py
--rw-r--r--   0 runner    (1001) docker     (123)     5383 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_dynamodb/test_dynamodb_consumedcapacity.py
--rw-r--r--   0 runner    (1001) docker     (123)    16456 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_dynamodb/test_dynamodb_create_table.py
--rw-r--r--   0 runner    (1001) docker     (123)    17832 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_dynamodb/test_dynamodb_executor.py
--rw-r--r--   0 runner    (1001) docker     (123)     9879 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_dynamodb/test_dynamodb_expression_tokenizer.py
--rw-r--r--   0 runner    (1001) docker     (123)    14053 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_dynamodb/test_dynamodb_expressions.py
--rw-r--r--   0 runner    (1001) docker     (123)    39804 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_dynamodb/test_dynamodb_table_with_range_key.py
--rw-r--r--   0 runner    (1001) docker     (123)    20261 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_dynamodb/test_dynamodb_table_without_range_key.py
--rw-r--r--   0 runner    (1001) docker     (123)     1062 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_dynamodb/test_dynamodb_update_expressions.py
--rw-r--r--   0 runner    (1001) docker     (123)     2832 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_dynamodb/test_dynamodb_update_table.py
--rw-r--r--   0 runner    (1001) docker     (123)    16779 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_dynamodb/test_dynamodb_validation.py
--rw-r--r--   0 runner    (1001) docker     (123)     1095 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_dynamodb/test_server.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:53.093518 moto-4.1.7.dev8/tests/test_dynamodb_v20111205/
--rw-r--r--   0 runner    (1001) docker     (123)       41 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_dynamodb_v20111205/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    43145 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_dynamodb_v20111205/test_server.py
--rw-r--r--   0 runner    (1001) docker     (123)     2391 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_dynamodb_v20111205/test_servermode.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:53.097518 moto-4.1.7.dev8/tests/test_dynamodbstreams/
--rw-r--r--   0 runner    (1001) docker     (123)       41 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_dynamodbstreams/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    10314 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_dynamodbstreams/test_dynamodbstreams.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:53.097518 moto-4.1.7.dev8/tests/test_ebs/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_ebs/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     5997 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_ebs/test_ebs.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:53.121518 moto-4.1.7.dev8/tests/test_ec2/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_ec2/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      496 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_ec2/helpers.py
--rw-r--r--   0 runner    (1001) docker     (123)     1218 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_ec2/test_account_attributes.py
--rw-r--r--   0 runner    (1001) docker     (123)      135 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_ec2/test_amazon_dev_pay.py
--rw-r--r--   0 runner    (1001) docker     (123)    44698 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_ec2/test_amis.py
--rw-r--r--   0 runner    (1001) docker     (123)     2456 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_ec2/test_availability_zones_and_regions.py
--rw-r--r--   0 runner    (1001) docker     (123)     3832 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_ec2/test_carrier_gateways.py
--rw-r--r--   0 runner    (1001) docker     (123)     4131 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_ec2/test_customer_gateways.py
--rw-r--r--   0 runner    (1001) docker     (123)    17165 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_ec2/test_dhcp_options.py
--rw-r--r--   0 runner    (1001) docker     (123)    35904 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_ec2/test_ec2_cloudformation.py
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_ec2/test_ec2_core.py
--rw-r--r--   0 runner    (1001) docker     (123)     1521 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_ec2/test_ec2_integration.py
--rw-r--r--   0 runner    (1001) docker     (123)     3410 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_ec2/test_egress_only_igw.py
--rw-r--r--   0 runner    (1001) docker     (123)    42808 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_ec2/test_elastic_block_store.py
--rw-r--r--   0 runner    (1001) docker     (123)    26968 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_ec2/test_elastic_ip_addresses.py
--rw-r--r--   0 runner    (1001) docker     (123)    40929 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_ec2/test_elastic_network_interfaces.py
--rw-r--r--   0 runner    (1001) docker     (123)    22223 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_ec2/test_fleets.py
--rw-r--r--   0 runner    (1001) docker     (123)    24744 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_ec2/test_flow_logs.py
--rw-r--r--   0 runner    (1001) docker     (123)     3659 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_ec2/test_flow_logs_cloudformation.py
--rw-r--r--   0 runner    (1001) docker     (123)      888 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_ec2/test_general.py
--rw-r--r--   0 runner    (1001) docker     (123)     5099 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_ec2/test_hosts.py
--rw-r--r--   0 runner    (1001) docker     (123)    10287 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_ec2/test_iam_integration.py
--rw-r--r--   0 runner    (1001) docker     (123)     3205 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_ec2/test_instance_type_offerings.py
--rw-r--r--   0 runner    (1001) docker     (123)     6937 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_ec2/test_instance_types.py
--rw-r--r--   0 runner    (1001) docker     (123)    98932 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_ec2/test_instances.py
--rw-r--r--   0 runner    (1001) docker     (123)    12355 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_ec2/test_internet_gateways.py
--rw-r--r--   0 runner    (1001) docker     (123)      133 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_ec2/test_ip_addresses.py
--rw-r--r--   0 runner    (1001) docker     (123)     9667 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_ec2/test_key_pairs.py
--rw-r--r--   0 runner    (1001) docker     (123)    22901 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_ec2/test_launch_templates.py
--rw-r--r--   0 runner    (1001) docker     (123)      131 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_ec2/test_monitoring.py
--rw-r--r--   0 runner    (1001) docker     (123)    10435 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_ec2/test_nat_gateway.py
--rw-r--r--   0 runner    (1001) docker     (123)    15234 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_ec2/test_network_acls.py
--rw-r--r--   0 runner    (1001) docker     (123)      137 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_ec2/test_placement_groups.py
--rw-r--r--   0 runner    (1001) docker     (123)    11252 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_ec2/test_prefix_lists.py
--rw-r--r--   0 runner    (1001) docker     (123)     6112 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_ec2/test_regions.py
--rw-r--r--   0 runner    (1001) docker     (123)      139 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_ec2/test_reserved_instances.py
--rw-r--r--   0 runner    (1001) docker     (123)    40234 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_ec2/test_route_tables.py
--rw-r--r--   0 runner    (1001) docker     (123)    64524 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_ec2/test_security_groups.py
--rw-r--r--   0 runner    (1001) docker     (123)     9376 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_ec2/test_security_groups_cloudformation.py
--rw-r--r--   0 runner    (1001) docker     (123)     2458 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_ec2/test_server.py
--rw-r--r--   0 runner    (1001) docker     (123)     1584 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_ec2/test_settings.py
--rw-r--r--   0 runner    (1001) docker     (123)    20068 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_ec2/test_spot_fleet.py
--rw-r--r--   0 runner    (1001) docker     (123)    15364 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_ec2/test_spot_instances.py
--rw-r--r--   0 runner    (1001) docker     (123)    31381 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_ec2/test_subnets.py
--rw-r--r--   0 runner    (1001) docker     (123)    18120 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_ec2/test_tags.py
--rw-r--r--   0 runner    (1001) docker     (123)    33200 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_ec2/test_transit_gateway.py
--rw-r--r--   0 runner    (1001) docker     (123)     3556 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_ec2/test_transit_gateway_cloudformation.py
--rw-r--r--   0 runner    (1001) docker     (123)     8110 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_ec2/test_transit_gateway_peering_attachments.py
--rw-r--r--   0 runner    (1001) docker     (123)     2022 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_ec2/test_utils.py
--rw-r--r--   0 runner    (1001) docker     (123)    10382 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_ec2/test_virtual_private_gateways.py
--rw-r--r--   0 runner    (1001) docker     (123)      130 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_ec2/test_vm_export.py
--rw-r--r--   0 runner    (1001) docker     (123)      130 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_ec2/test_vm_import.py
--rw-r--r--   0 runner    (1001) docker     (123)    11771 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_ec2/test_vpc_endpoint_services_integration.py
--rw-r--r--   0 runner    (1001) docker     (123)    19510 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_ec2/test_vpc_peering.py
--rw-r--r--   0 runner    (1001) docker     (123)    13918 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_ec2/test_vpc_service_configuration.py
--rw-r--r--   0 runner    (1001) docker     (123)    45725 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_ec2/test_vpcs.py
--rw-r--r--   0 runner    (1001) docker     (123)     4926 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_ec2/test_vpn_connections.py
--rw-r--r--   0 runner    (1001) docker     (123)      938 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_ec2/test_windows.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:53.121518 moto-4.1.7.dev8/tests/test_ec2instanceconnect/
--rw-r--r--   0 runner    (1001) docker     (123)      898 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_ec2instanceconnect/test_ec2instanceconnect_boto3.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:53.121518 moto-4.1.7.dev8/tests/test_ecr/
--rw-r--r--   0 runner    (1001) docker     (123)       41 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_ecr/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    90248 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_ecr/test_ecr_boto3.py
--rw-r--r--   0 runner    (1001) docker     (123)     3133 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_ecr/test_ecr_cloudformation.py
--rw-r--r--   0 runner    (1001) docker     (123)     2383 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_ecr/test_ecr_helpers.py
--rw-r--r--   0 runner    (1001) docker     (123)    11690 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_ecr/test_ecr_policy_validation.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:53.125519 moto-4.1.7.dev8/tests/test_ecs/
--rw-r--r--   0 runner    (1001) docker     (123)       41 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_ecs/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     8223 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_ecs/test_ecs_account_settings.py
--rw-r--r--   0 runner    (1001) docker     (123)   124666 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_ecs/test_ecs_boto3.py
--rw-r--r--   0 runner    (1001) docker     (123)     7707 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_ecs/test_ecs_capacity_provider.py
--rw-r--r--   0 runner    (1001) docker     (123)    14232 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_ecs/test_ecs_cloudformation.py
--rw-r--r--   0 runner    (1001) docker     (123)     1192 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_ecs/test_ecs_efs.py
--rw-r--r--   0 runner    (1001) docker     (123)     1499 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_ecs/test_ecs_task_def_tags.py
--rw-r--r--   0 runner    (1001) docker     (123)    13616 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_ecs/test_ecs_tasksets.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:53.125519 moto-4.1.7.dev8/tests/test_efs/
--rw-r--r--   0 runner    (1001) docker     (123)      358 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_efs/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      103 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_efs/junk_drawer.py
--rw-r--r--   0 runner    (1001) docker     (123)     2318 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_efs/test_access_point_tagging.py
--rw-r--r--   0 runner    (1001) docker     (123)     4445 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_efs/test_access_points.py
--rw-r--r--   0 runner    (1001) docker     (123)    13043 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_efs/test_file_system.py
--rw-r--r--   0 runner    (1001) docker     (123)     1906 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_efs/test_filesystem_tagging.py
--rw-r--r--   0 runner    (1001) docker     (123)     1554 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_efs/test_lifecycle_config.py
--rw-r--r--   0 runner    (1001) docker     (123)    13392 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_efs/test_mount_target.py
--rw-r--r--   0 runner    (1001) docker     (123)     3709 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_efs/test_mount_target_security_groups.py
--rw-r--r--   0 runner    (1001) docker     (123)     3115 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_efs/test_server.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:53.125519 moto-4.1.7.dev8/tests/test_eks/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_eks/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    52255 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_eks/test_eks.py
--rw-r--r--   0 runner    (1001) docker     (123)     7616 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_eks/test_eks_constants.py
--rw-r--r--   0 runner    (1001) docker     (123)     2240 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_eks/test_eks_ec2.py
--rw-r--r--   0 runner    (1001) docker     (123)     4344 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_eks/test_eks_utils.py
--rw-r--r--   0 runner    (1001) docker     (123)    17353 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_eks/test_server.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:53.129519 moto-4.1.7.dev8/tests/test_elasticache/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_elasticache/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     7236 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_elasticache/test_elasticache.py
--rw-r--r--   0 runner    (1001) docker     (123)      477 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_elasticache/test_server.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:53.129519 moto-4.1.7.dev8/tests/test_elasticbeanstalk/
--rw-r--r--   0 runner    (1001) docker     (123)     4486 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_elasticbeanstalk/test_eb.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:53.129519 moto-4.1.7.dev8/tests/test_elastictranscoder/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_elastictranscoder/__init__
--rw-r--r--   0 runner    (1001) docker     (123)    14785 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_elastictranscoder/test_elastictranscoder.py
--rw-r--r--   0 runner    (1001) docker     (123)      423 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_elastictranscoder/test_server.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:53.129519 moto-4.1.7.dev8/tests/test_elb/
--rw-r--r--   0 runner    (1001) docker     (123)       41 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_elb/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    41073 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_elb/test_elb.py
--rw-r--r--   0 runner    (1001) docker     (123)     1982 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_elb/test_elb_availabilityzones.py
--rw-r--r--   0 runner    (1001) docker     (123)     5096 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_elb/test_elb_cloudformation.py
--rw-r--r--   0 runner    (1001) docker     (123)    10157 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_elb/test_elb_policies.py
--rw-r--r--   0 runner    (1001) docker     (123)     1951 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_elb/test_elb_subnets.py
--rw-r--r--   0 runner    (1001) docker     (123)      394 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_elb/test_server.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:53.129519 moto-4.1.7.dev8/tests/test_elbv2/
--rw-r--r--   0 runner    (1001) docker     (123)       41 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_elbv2/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    65284 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_elbv2/test_elbv2.py
--rw-r--r--   0 runner    (1001) docker     (123)    12345 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_elbv2/test_elbv2_cloudformation.py
--rw-r--r--   0 runner    (1001) docker     (123)     2419 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_elbv2/test_elbv2_integration.py
--rw-r--r--   0 runner    (1001) docker     (123)     2777 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_elbv2/test_elbv2_listener_rule_tags.py
--rw-r--r--   0 runner    (1001) docker     (123)    16854 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_elbv2/test_elbv2_listener_rules.py
--rw-r--r--   0 runner    (1001) docker     (123)     2365 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_elbv2/test_elbv2_listener_tags.py
--rw-r--r--   0 runner    (1001) docker     (123)     2738 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_elbv2/test_elbv2_set_subnets.py
--rw-r--r--   0 runner    (1001) docker     (123)    25515 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_elbv2/test_elbv2_target_groups.py
--rw-r--r--   0 runner    (1001) docker     (123)      403 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_elbv2/test_server.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:53.133519 moto-4.1.7.dev8/tests/test_emr/
--rw-r--r--   0 runner    (1001) docker     (123)       41 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_emr/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    45802 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_emr/test_emr_boto3.py
--rw-r--r--   0 runner    (1001) docker     (123)     7968 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_emr/test_emr_integration.py
--rw-r--r--   0 runner    (1001) docker     (123)      403 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_emr/test_server.py
--rw-r--r--   0 runner    (1001) docker     (123)     1484 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_emr/test_utils.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:53.133519 moto-4.1.7.dev8/tests/test_emrcontainers/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_emrcontainers/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    20727 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_emrcontainers/test_emrcontainers.py
--rw-r--r--   0 runner    (1001) docker     (123)      380 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_emrcontainers/test_server.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:53.133519 moto-4.1.7.dev8/tests/test_emrserverless/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_emrserverless/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    19180 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_emrserverless/test_emrserverless.py
--rw-r--r--   0 runner    (1001) docker     (123)      386 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_emrserverless/test_server.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:53.133519 moto-4.1.7.dev8/tests/test_es/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_es/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     9146 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_es/test_es.py
--rw-r--r--   0 runner    (1001) docker     (123)      352 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_es/test_server.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:53.133519 moto-4.1.7.dev8/tests/test_events/
--rw-r--r--   0 runner    (1001) docker     (123)       41 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_events/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     4186 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_events/test_event_pattern.py
--rw-r--r--   0 runner    (1001) docker     (123)    81682 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_events/test_events.py
--rw-r--r--   0 runner    (1001) docker     (123)     5843 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_events/test_events_cloudformation.py
--rw-r--r--   0 runner    (1001) docker     (123)    13082 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_events/test_events_integration.py
--rw-r--r--   0 runner    (1001) docker     (123)     9161 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_events/test_events_lambdatriggers_integration.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:53.137519 moto-4.1.7.dev8/tests/test_firehose/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_firehose/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    20103 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_firehose/test_firehose.py
--rw-r--r--   0 runner    (1001) docker     (123)    13553 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_firehose/test_firehose_destination_types.py
--rw-r--r--   0 runner    (1001) docker     (123)     2967 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_firehose/test_firehose_encryption.py
--rw-r--r--   0 runner    (1001) docker     (123)     5439 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_firehose/test_firehose_put.py
--rw-r--r--   0 runner    (1001) docker     (123)     5953 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_firehose/test_firehose_tags.py
--rw-r--r--   0 runner    (1001) docker     (123)     3336 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_firehose/test_http_destinations.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:53.137519 moto-4.1.7.dev8/tests/test_forecast/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_forecast/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     7786 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_forecast/test_forecast.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:53.137519 moto-4.1.7.dev8/tests/test_glacier/
--rw-r--r--   0 runner    (1001) docker     (123)       41 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_glacier/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)       38 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_glacier/test.gz
--rw-r--r--   0 runner    (1001) docker     (123)     1988 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_glacier/test_glacier_archives.py
--rw-r--r--   0 runner    (1001) docker     (123)     4811 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_glacier/test_glacier_jobs.py
--rw-r--r--   0 runner    (1001) docker     (123)     2989 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_glacier/test_glacier_vaults.py
--rw-r--r--   0 runner    (1001) docker     (123)      436 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_glacier/test_server.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:53.137519 moto-4.1.7.dev8/tests/test_glue/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_glue/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:53.137519 moto-4.1.7.dev8/tests/test_glue/fixtures/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_glue/fixtures/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     2153 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_glue/fixtures/datacatalog.py
--rw-r--r--   0 runner    (1001) docker     (123)     5015 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_glue/fixtures/schema_registry.py
--rw-r--r--   0 runner    (1001) docker     (123)     6423 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_glue/helpers.py
--rw-r--r--   0 runner    (1001) docker     (123)    48038 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_glue/test_datacatalog.py
--rw-r--r--   0 runner    (1001) docker     (123)    14293 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_glue/test_glue.py
--rw-r--r--   0 runner    (1001) docker     (123)     4899 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_glue/test_glue_job_runs.py
--rw-r--r--   0 runner    (1001) docker     (123)    14929 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_glue/test_partition_filter.py
--rw-r--r--   0 runner    (1001) docker     (123)    47112 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_glue/test_schema_registry.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:53.141519 moto-4.1.7.dev8/tests/test_greengrass/
--rw-r--r--   0 runner    (1001) docker     (123)       41 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_greengrass/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    13441 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_greengrass/test_greengrass_core.py
--rw-r--r--   0 runner    (1001) docker     (123)    18455 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_greengrass/test_greengrass_deployment.py
--rw-r--r--   0 runner    (1001) docker     (123)    15306 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_greengrass/test_greengrass_device.py
--rw-r--r--   0 runner    (1001) docker     (123)    16217 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_greengrass/test_greengrass_functions.py
--rw-r--r--   0 runner    (1001) docker     (123)    19915 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_greengrass/test_greengrass_groups.py
--rw-r--r--   0 runner    (1001) docker     (123)    21905 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_greengrass/test_greengrass_resource.py
--rw-r--r--   0 runner    (1001) docker     (123)    20373 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_greengrass/test_greengrass_subscriptions.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:53.141519 moto-4.1.7.dev8/tests/test_guardduty/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_guardduty/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     5080 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_guardduty/test_guardduty.py
--rw-r--r--   0 runner    (1001) docker     (123)     3179 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_guardduty/test_guardduty_filters.py
--rw-r--r--   0 runner    (1001) docker     (123)      844 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_guardduty/test_guardduty_organization.py
--rw-r--r--   0 runner    (1001) docker     (123)      432 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_guardduty/test_server.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:53.141519 moto-4.1.7.dev8/tests/test_iam/
--rw-r--r--   0 runner    (1001) docker     (123)       41 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_iam/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)   167646 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_iam/test_iam.py
--rw-r--r--   0 runner    (1001) docker     (123)      822 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_iam/test_iam_access_integration.py
--rw-r--r--   0 runner    (1001) docker     (123)      672 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_iam/test_iam_account_aliases.py
--rw-r--r--   0 runner    (1001) docker     (123)    51772 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_iam/test_iam_cloudformation.py
--rw-r--r--   0 runner    (1001) docker     (123)    11597 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_iam/test_iam_groups.py
--rw-r--r--   0 runner    (1001) docker     (123)    13090 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_iam/test_iam_oidc.py
--rw-r--r--   0 runner    (1001) docker     (123)     1264 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_iam/test_iam_password_last_used.py
--rw-r--r--   0 runner    (1001) docker     (123)    51265 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_iam/test_iam_policies.py
--rw-r--r--   0 runner    (1001) docker     (123)     3196 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_iam/test_iam_server_certificates.py
--rw-r--r--   0 runner    (1001) docker     (123)      594 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_iam/test_server.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:53.141519 moto-4.1.7.dev8/tests/test_identitystore/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_identitystore/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      761 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_identitystore/test_identitystore.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:53.145519 moto-4.1.7.dev8/tests/test_iot/
--rw-r--r--   0 runner    (1001) docker     (123)       41 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_iot/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     6115 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_iot/test_iot.py
--rw-r--r--   0 runner    (1001) docker     (123)     6208 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_iot/test_iot_ca_certificates.py
--rw-r--r--   0 runner    (1001) docker     (123)    13028 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_iot/test_iot_certificates.py
--rw-r--r--   0 runner    (1001) docker     (123)     2700 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_iot/test_iot_deprecate_thing_type.py
--rw-r--r--   0 runner    (1001) docker     (123)     8519 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_iot/test_iot_domain_configuration.py
--rw-r--r--   0 runner    (1001) docker     (123)     9937 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_iot/test_iot_job_executions.py
--rw-r--r--   0 runner    (1001) docker     (123)    11995 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_iot/test_iot_jobs.py
--rw-r--r--   0 runner    (1001) docker     (123)    17661 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_iot/test_iot_policies.py
--rw-r--r--   0 runner    (1001) docker     (123)     1621 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_iot/test_iot_search.py
--rw-r--r--   0 runner    (1001) docker     (123)    28056 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_iot/test_iot_thing_groups.py
--rw-r--r--   0 runner    (1001) docker     (123)     3398 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_iot/test_iot_thing_types.py
--rw-r--r--   0 runner    (1001) docker     (123)     9267 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_iot/test_iot_things.py
--rw-r--r--   0 runner    (1001) docker     (123)     5634 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_iot/test_iot_topic_rules.py
--rw-r--r--   0 runner    (1001) docker     (123)     1467 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_iot/test_server.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:53.145519 moto-4.1.7.dev8/tests/test_iotdata/
--rw-r--r--   0 runner    (1001) docker     (123)       41 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_iotdata/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     6399 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_iotdata/test_iotdata.py
--rw-r--r--   0 runner    (1001) docker     (123)     1044 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_iotdata/test_server.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:53.149519 moto-4.1.7.dev8/tests/test_kinesis/
--rw-r--r--   0 runner    (1001) docker     (123)       41 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_kinesis/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    31019 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_kinesis/test_kinesis.py
--rw-r--r--   0 runner    (1001) docker     (123)    13043 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_kinesis/test_kinesis_boto3.py
--rw-r--r--   0 runner    (1001) docker     (123)     5287 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_kinesis/test_kinesis_cloudformation.py
--rw-r--r--   0 runner    (1001) docker     (123)     2319 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_kinesis/test_kinesis_encryption.py
--rw-r--r--   0 runner    (1001) docker     (123)     5415 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_kinesis/test_kinesis_monitoring.py
--rw-r--r--   0 runner    (1001) docker     (123)     5195 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_kinesis/test_kinesis_stream_consumers.py
--rw-r--r--   0 runner    (1001) docker     (123)     1967 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_kinesis/test_kinesis_stream_limits.py
--rw-r--r--   0 runner    (1001) docker     (123)      434 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_kinesis/test_server.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:53.149519 moto-4.1.7.dev8/tests/test_kinesisvideo/
--rw-r--r--   0 runner    (1001) docker     (123)       41 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_kinesisvideo/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     4857 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_kinesisvideo/test_kinesisvideo.py
--rw-r--r--   0 runner    (1001) docker     (123)      398 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_kinesisvideo/test_server.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:53.149519 moto-4.1.7.dev8/tests/test_kinesisvideoarchivedmedia/
--rw-r--r--   0 runner    (1001) docker     (123)       41 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_kinesisvideoarchivedmedia/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     2962 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_kinesisvideoarchivedmedia/test_kinesisvideoarchivedmedia.py
--rw-r--r--   0 runner    (1001) docker     (123)      500 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_kinesisvideoarchivedmedia/test_server.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:53.149519 moto-4.1.7.dev8/tests/test_kms/
--rw-r--r--   0 runner    (1001) docker     (123)       41 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_kms/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    45373 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_kms/test_kms_boto3.py
--rw-r--r--   0 runner    (1001) docker     (123)     6967 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_kms/test_kms_encrypt.py
--rw-r--r--   0 runner    (1001) docker     (123)     5945 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_kms/test_kms_grants.py
--rw-r--r--   0 runner    (1001) docker     (123)     4823 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_kms/test_kms_policy_enforcement.py
--rw-r--r--   0 runner    (1001) docker     (123)     1183 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_kms/test_model.py
--rw-r--r--   0 runner    (1001) docker     (123)      457 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_kms/test_server.py
--rw-r--r--   0 runner    (1001) docker     (123)     5468 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_kms/test_utils.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:53.149519 moto-4.1.7.dev8/tests/test_logs/
--rw-r--r--   0 runner    (1001) docker     (123)       41 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_logs/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    19409 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_logs/test_integration.py
--rw-r--r--   0 runner    (1001) docker     (123)    47011 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_logs/test_logs.py
--rw-r--r--   0 runner    (1001) docker     (123)     7020 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_logs/test_logs_filter.py
--rw-r--r--   0 runner    (1001) docker     (123)      772 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_logs/test_models.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:53.153519 moto-4.1.7.dev8/tests/test_managedblockchain/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_managedblockchain/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     2411 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_managedblockchain/helpers.py
--rw-r--r--   0 runner    (1001) docker     (123)     4768 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_managedblockchain/test_managedblockchain_invitations.py
--rw-r--r--   0 runner    (1001) docker     (123)    25157 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_managedblockchain/test_managedblockchain_members.py
--rw-r--r--   0 runner    (1001) docker     (123)     4854 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_managedblockchain/test_managedblockchain_networks.py
--rw-r--r--   0 runner    (1001) docker     (123)    19320 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_managedblockchain/test_managedblockchain_nodes.py
--rw-r--r--   0 runner    (1001) docker     (123)     7924 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_managedblockchain/test_managedblockchain_proposals.py
--rw-r--r--   0 runner    (1001) docker     (123)    22370 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_managedblockchain/test_managedblockchain_proposalvotes.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:53.153519 moto-4.1.7.dev8/tests/test_mediaconnect/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_mediaconnect/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    25048 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_mediaconnect/test_mediaconnect.py
--rw-r--r--   0 runner    (1001) docker     (123)      435 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_mediaconnect/test_server.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:53.153519 moto-4.1.7.dev8/tests/test_medialive/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_medialive/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    12296 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_medialive/test_medialive.py
--rw-r--r--   0 runner    (1001) docker     (123)      702 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_medialive/test_server.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:53.153519 moto-4.1.7.dev8/tests/test_mediapackage/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_mediapackage/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    10907 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_mediapackage/test_mediapackage.py
--rw-r--r--   0 runner    (1001) docker     (123)      741 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_mediapackage/test_server.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:53.153519 moto-4.1.7.dev8/tests/test_mediastore/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_mediastore/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    10137 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_mediastore/test_mediastore.py
--rw-r--r--   0 runner    (1001) docker     (123)      508 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_mediastore/test_server.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:53.153519 moto-4.1.7.dev8/tests/test_mediastoredata/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_mediastoredata/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     2442 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_mediastoredata/test_mediastoredata.py
--rw-r--r--   0 runner    (1001) docker     (123)      411 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_mediastoredata/test_server.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:53.153519 moto-4.1.7.dev8/tests/test_meteringmarketplace/
--rw-r--r--   0 runner    (1001) docker     (123)     2822 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_meteringmarketplace/test_meteringmarketplace.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:53.153519 moto-4.1.7.dev8/tests/test_moto_api/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_moto_api/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:53.153519 moto-4.1.7.dev8/tests/test_moto_api/mock_random/
--rw-r--r--   0 runner    (1001) docker     (123)     1251 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_moto_api/mock_random/test_mock_random.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:53.157519 moto-4.1.7.dev8/tests/test_moto_api/recorder/
--rw-r--r--   0 runner    (1001) docker     (123)    10193 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_moto_api/recorder/test_recorder.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:53.157519 moto-4.1.7.dev8/tests/test_moto_api/state_manager/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_moto_api/state_manager/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:53.157519 moto-4.1.7.dev8/tests/test_moto_api/state_manager/servermode/
--rw-r--r--   0 runner    (1001) docker     (123)     1990 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_moto_api/state_manager/servermode/test_inmemory_server.py
--rw-r--r--   0 runner    (1001) docker     (123)     1992 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_moto_api/state_manager/servermode/test_state_manager.py
--rw-r--r--   0 runner    (1001) docker     (123)     1755 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_moto_api/state_manager/test_batch_integration.py
--rw-r--r--   0 runner    (1001) docker     (123)     4137 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_moto_api/state_manager/test_managed_state_model.py
--rw-r--r--   0 runner    (1001) docker     (123)     2067 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_moto_api/state_manager/test_state_manager.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:53.157519 moto-4.1.7.dev8/tests/test_mq/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_mq/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    14031 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_mq/test_mq.py
--rw-r--r--   0 runner    (1001) docker     (123)     7095 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_mq/test_mq_configuration.py
--rw-r--r--   0 runner    (1001) docker     (123)     3255 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_mq/test_mq_tags.py
--rw-r--r--   0 runner    (1001) docker     (123)     5234 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_mq/test_mq_users.py
--rw-r--r--   0 runner    (1001) docker     (123)      382 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_mq/test_server.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:53.157519 moto-4.1.7.dev8/tests/test_neptune/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_neptune/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      842 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_neptune/test_cluster_options.py
--rw-r--r--   0 runner    (1001) docker     (123)      837 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_neptune/test_cluster_tags.py
--rw-r--r--   0 runner    (1001) docker     (123)     4530 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_neptune/test_clusters.py
--rw-r--r--   0 runner    (1001) docker     (123)     1989 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_neptune/test_global_clusters.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:53.157519 moto-4.1.7.dev8/tests/test_opensearch/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_opensearch/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      978 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_opensearch/test_domain_tags.py
--rw-r--r--   0 runner    (1001) docker     (123)     4806 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_opensearch/test_opensearch.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:53.157519 moto-4.1.7.dev8/tests/test_opsworks/
--rw-r--r--   0 runner    (1001) docker     (123)       41 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_opsworks/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     2433 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_opsworks/test_apps.py
--rw-r--r--   0 runner    (1001) docker     (123)     7770 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_opsworks/test_instances.py
--rw-r--r--   0 runner    (1001) docker     (123)     3019 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_opsworks/test_layers.py
--rw-r--r--   0 runner    (1001) docker     (123)     1403 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_opsworks/test_stack.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:53.161519 moto-4.1.7.dev8/tests/test_organizations/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_organizations/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     4891 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_organizations/organizations_test_utils.py
--rw-r--r--   0 runner    (1001) docker     (123)    85363 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_organizations/test_organizations_boto3.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:53.161519 moto-4.1.7.dev8/tests/test_personalize/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_personalize/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     4221 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_personalize/test_personalize_schema.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:53.161519 moto-4.1.7.dev8/tests/test_pinpoint/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_pinpoint/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     4883 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_pinpoint/test_pinpoint.py
--rw-r--r--   0 runner    (1001) docker     (123)     2288 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_pinpoint/test_pinpoint_application_tags.py
--rw-r--r--   0 runner    (1001) docker     (123)     2884 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_pinpoint/test_pinpoint_event_stream.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:53.161519 moto-4.1.7.dev8/tests/test_polly/
--rw-r--r--   0 runner    (1001) docker     (123)       41 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_polly/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     7974 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_polly/test_polly.py
--rw-r--r--   0 runner    (1001) docker     (123)      362 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_polly/test_server.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:53.161519 moto-4.1.7.dev8/tests/test_quicksight/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_quicksight/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     2209 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_quicksight/test_quicksight_datasets.py
--rw-r--r--   0 runner    (1001) docker     (123)     4647 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_quicksight/test_quicksight_groups.py
--rw-r--r--   0 runner    (1001) docker     (123)     9343 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_quicksight/test_quicksight_users.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:53.161519 moto-4.1.7.dev8/tests/test_ram/
--rw-r--r--   0 runner    (1001) docker     (123)    12819 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_ram/test_ram.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:53.165519 moto-4.1.7.dev8/tests/test_rds/
--rw-r--r--   0 runner    (1001) docker     (123)       41 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_rds/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    16282 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_rds/test_filters.py
--rw-r--r--   0 runner    (1001) docker     (123)    91218 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_rds/test_rds.py
--rw-r--r--   0 runner    (1001) docker     (123)    11124 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_rds/test_rds_cloudformation.py
--rw-r--r--   0 runner    (1001) docker     (123)    28931 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_rds/test_rds_clusters.py
--rw-r--r--   0 runner    (1001) docker     (123)     4572 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_rds/test_rds_event_subscriptions.py
--rw-r--r--   0 runner    (1001) docker     (123)     5229 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_rds/test_rds_export_tasks.py
--rw-r--r--   0 runner    (1001) docker     (123)     1194 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_rds/test_server.py
--rw-r--r--   0 runner    (1001) docker     (123)     7876 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_rds/test_utils.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:53.165519 moto-4.1.7.dev8/tests/test_redshift/
--rw-r--r--   0 runner    (1001) docker     (123)       41 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_redshift/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    73309 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_redshift/test_redshift.py
--rw-r--r--   0 runner    (1001) docker     (123)     2095 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_redshift/test_redshift_cloudformation.py
--rw-r--r--   0 runner    (1001) docker     (123)    12934 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_redshift/test_server.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:53.165519 moto-4.1.7.dev8/tests/test_redshiftdata/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_redshiftdata/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     5862 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_redshiftdata/test_redshiftdata.py
--rw-r--r--   0 runner    (1001) docker     (123)      170 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_redshiftdata/test_redshiftdata_constants.py
--rw-r--r--   0 runner    (1001) docker     (123)     7504 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_redshiftdata/test_server.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:53.165519 moto-4.1.7.dev8/tests/test_rekognition/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_rekognition/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     2174 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_rekognition/test_rekognition.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:53.165519 moto-4.1.7.dev8/tests/test_resourcegroups/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_resourcegroups/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     8608 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_resourcegroups/test_resourcegroups.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:53.165519 moto-4.1.7.dev8/tests/test_resourcegroupstaggingapi/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_resourcegroupstaggingapi/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    24449 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_resourcegroupstaggingapi/test_resourcegroupstaggingapi.py
--rw-r--r--   0 runner    (1001) docker     (123)      579 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_resourcegroupstaggingapi/test_server.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:53.169519 moto-4.1.7.dev8/tests/test_route53/
--rw-r--r--   0 runner    (1001) docker     (123)       41 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_route53/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     1642 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_route53/test_change_set_model.py
--rw-r--r--   0 runner    (1001) docker     (123)    52862 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_route53/test_route53.py
--rw-r--r--   0 runner    (1001) docker     (123)     8233 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_route53/test_route53_cloudformation.py
--rw-r--r--   0 runner    (1001) docker     (123)     4160 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_route53/test_route53_delegationsets.py
--rw-r--r--   0 runner    (1001) docker     (123)    10027 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_route53/test_route53_healthchecks.py
--rw-r--r--   0 runner    (1001) docker     (123)    11544 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_route53/test_route53_query_logging_config.py
--rw-r--r--   0 runner    (1001) docker     (123)     9418 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_route53/test_route53_vpcs.py
--rw-r--r--   0 runner    (1001) docker     (123)     1555 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_route53/test_server.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:53.169519 moto-4.1.7.dev8/tests/test_route53resolver/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_route53resolver/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    40356 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_route53resolver/test_route53resolver_endpoint.py
--rw-r--r--   0 runner    (1001) docker     (123)    21968 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_route53resolver/test_route53resolver_rule.py
--rw-r--r--   0 runner    (1001) docker     (123)    17448 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_route53resolver/test_route53resolver_rule_associations.py
--rw-r--r--   0 runner    (1001) docker     (123)     5579 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_route53resolver/test_route53resolver_tags.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:53.173519 moto-4.1.7.dev8/tests/test_s3/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_s3/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     1782 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_s3/test_multiple_accounts_server.py
--rw-r--r--   0 runner    (1001) docker     (123)   114284 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_s3/test_s3.py
--rw-r--r--   0 runner    (1001) docker     (123)    11268 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_s3/test_s3_acl.py
--rw-r--r--   0 runner    (1001) docker     (123)     7102 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_s3/test_s3_auth.py
--rw-r--r--   0 runner    (1001) docker     (123)     4800 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_s3/test_s3_bucket_policy.py
--rw-r--r--   0 runner    (1001) docker     (123)      513 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_s3/test_s3_classdecorator.py
--rw-r--r--   0 runner    (1001) docker     (123)     7924 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_s3/test_s3_cloudformation.py
--rw-r--r--   0 runner    (1001) docker     (123)    18825 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_s3/test_s3_config.py
--rw-r--r--   0 runner    (1001) docker     (123)    12874 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_s3/test_s3_copyobject.py
--rw-r--r--   0 runner    (1001) docker     (123)     3532 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_s3/test_s3_custom_endpoint.py
--rw-r--r--   0 runner    (1001) docker     (123)     4423 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_s3/test_s3_encryption.py
--rw-r--r--   0 runner    (1001) docker     (123)    10625 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_s3/test_s3_file_handles.py
--rw-r--r--   0 runner    (1001) docker     (123)    10568 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_s3/test_s3_lambda_integration.py
--rw-r--r--   0 runner    (1001) docker     (123)    19473 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_s3/test_s3_lifecycle.py
--rw-r--r--   0 runner    (1001) docker     (123)     5944 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_s3/test_s3_lock.py
--rw-r--r--   0 runner    (1001) docker     (123)     9265 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_s3/test_s3_logging.py
--rw-r--r--   0 runner    (1001) docker     (123)      757 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_s3/test_s3_metadata.py
--rw-r--r--   0 runner    (1001) docker     (123)    31026 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_s3/test_s3_multipart.py
--rw-r--r--   0 runner    (1001) docker     (123)     4071 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_s3/test_s3_object_attributes.py
--rw-r--r--   0 runner    (1001) docker     (123)     1605 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_s3/test_s3_ownership.py
--rw-r--r--   0 runner    (1001) docker     (123)     5935 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_s3/test_s3_replication.py
--rw-r--r--   0 runner    (1001) docker     (123)     4172 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_s3/test_s3_select.py
--rw-r--r--   0 runner    (1001) docker     (123)     8580 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_s3/test_s3_storageclass.py
--rw-r--r--   0 runner    (1001) docker     (123)    14479 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_s3/test_s3_tagging.py
--rw-r--r--   0 runner    (1001) docker     (123)     4745 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_s3/test_s3_utils.py
--rw-r--r--   0 runner    (1001) docker     (123)    12808 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_s3/test_server.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:53.173519 moto-4.1.7.dev8/tests/test_s3bucket_path/
--rw-r--r--   0 runner    (1001) docker     (123)       41 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_s3bucket_path/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      447 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_s3bucket_path/test_s3bucket_path_utils.py
--rw-r--r--   0 runner    (1001) docker     (123)     3310 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_s3bucket_path/test_server.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:53.173519 moto-4.1.7.dev8/tests/test_s3control/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_s3control/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     2794 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_s3control/test_s3control.py
--rw-r--r--   0 runner    (1001) docker     (123)     3980 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_s3control/test_s3control_access_points.py
--rw-r--r--   0 runner    (1001) docker     (123)     3591 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_s3control/test_s3control_accesspoint_policy.py
--rw-r--r--   0 runner    (1001) docker     (123)    11881 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_s3control/test_s3control_config_integration.py
--rw-r--r--   0 runner    (1001) docker     (123)     3490 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_s3control/test_s3control_s3.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:53.177519 moto-4.1.7.dev8/tests/test_sagemaker/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_sagemaker/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     9953 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_sagemaker/cloudformation_test_configs.py
--rw-r--r--   0 runner    (1001) docker     (123)    15041 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_sagemaker/test_sagemaker_cloudformation.py
--rw-r--r--   0 runner    (1001) docker     (123)    20469 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_sagemaker/test_sagemaker_endpoint.py
--rw-r--r--   0 runner    (1001) docker     (123)     3162 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_sagemaker/test_sagemaker_experiment.py
--rw-r--r--   0 runner    (1001) docker     (123)     4816 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_sagemaker/test_sagemaker_models.py
--rw-r--r--   0 runner    (1001) docker     (123)    11569 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_sagemaker/test_sagemaker_notebooks.py
--rw-r--r--   0 runner    (1001) docker     (123)    24758 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_sagemaker/test_sagemaker_pipeline.py
--rw-r--r--   0 runner    (1001) docker     (123)    14930 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_sagemaker/test_sagemaker_processing.py
--rw-r--r--   0 runner    (1001) docker     (123)     3810 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_sagemaker/test_sagemaker_search.py
--rw-r--r--   0 runner    (1001) docker     (123)    17756 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_sagemaker/test_sagemaker_training.py
--rw-r--r--   0 runner    (1001) docker     (123)     5338 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_sagemaker/test_sagemaker_trial.py
--rw-r--r--   0 runner    (1001) docker     (123)     8415 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_sagemaker/test_sagemaker_trial_component.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:53.177519 moto-4.1.7.dev8/tests/test_sdb/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_sdb/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     5412 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_sdb/test_sdb_attributes.py
--rw-r--r--   0 runner    (1001) docker     (123)     2113 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_sdb/test_sdb_domains.py
--rw-r--r--   0 runner    (1001) docker     (123)      427 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_sdb/test_server.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:53.177519 moto-4.1.7.dev8/tests/test_secretsmanager/
--rw-r--r--   0 runner    (1001) docker     (123)       41 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_secretsmanager/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     9122 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_secretsmanager/test_list_secrets.py
--rw-r--r--   0 runner    (1001) docker     (123)     2511 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_secretsmanager/test_policy.py
--rw-r--r--   0 runner    (1001) docker     (123)    57270 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_secretsmanager/test_secretsmanager.py
--rw-r--r--   0 runner    (1001) docker     (123)    33144 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_secretsmanager/test_server.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:53.177519 moto-4.1.7.dev8/tests/test_servicediscovery/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_servicediscovery/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      456 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_servicediscovery/test_server.py
--rw-r--r--   0 runner    (1001) docker     (123)     8790 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_servicediscovery/test_servicediscovery_httpnamespaces.py
--rw-r--r--   0 runner    (1001) docker     (123)     4712 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_servicediscovery/test_servicediscovery_operations.py
--rw-r--r--   0 runner    (1001) docker     (123)     7657 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_servicediscovery/test_servicediscovery_service.py
--rw-r--r--   0 runner    (1001) docker     (123)     3419 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_servicediscovery/test_servicediscovery_tags.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:53.181519 moto-4.1.7.dev8/tests/test_servicequotas/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_servicequotas/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     2728 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_servicequotas/test_servicequotas.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:53.181519 moto-4.1.7.dev8/tests/test_ses/
--rw-r--r--   0 runner    (1001) docker     (123)       41 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_ses/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      855 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_ses/test_server.py
--rw-r--r--   0 runner    (1001) docker     (123)    52328 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_ses/test_ses_boto3.py
--rw-r--r--   0 runner    (1001) docker     (123)     6107 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_ses/test_ses_sns_boto3.py
--rw-r--r--   0 runner    (1001) docker     (123)      435 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_ses/test_ses_utils.py
--rw-r--r--   0 runner    (1001) docker     (123)      958 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_ses/test_templating.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:53.181519 moto-4.1.7.dev8/tests/test_signer/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_signer/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      684 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_signer/test_signing_platforms.py
--rw-r--r--   0 runner    (1001) docker     (123)     2261 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_signer/test_signing_profiles.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:53.181519 moto-4.1.7.dev8/tests/test_sns/
--rw-r--r--   0 runner    (1001) docker     (123)       41 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_sns/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    13714 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_sns/test_application_boto3.py
--rw-r--r--   0 runner    (1001) docker     (123)     6321 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_sns/test_publish_batch.py
--rw-r--r--   0 runner    (1001) docker     (123)    42805 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_sns/test_publishing_boto3.py
--rw-r--r--   0 runner    (1001) docker     (123)      761 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_sns/test_server.py
--rw-r--r--   0 runner    (1001) docker     (123)     6161 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_sns/test_sns_cloudformation.py
--rw-r--r--   0 runner    (1001) docker     (123)    19367 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_sns/test_subscriptions_boto3.py
--rw-r--r--   0 runner    (1001) docker     (123)    21472 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_sns/test_topics_boto3.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:53.181519 moto-4.1.7.dev8/tests/test_special_cases/
--rw-r--r--   0 runner    (1001) docker     (123)     2293 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_special_cases/test_custom_amis.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:53.181519 moto-4.1.7.dev8/tests/test_sqs/
--rw-r--r--   0 runner    (1001) docker     (123)       41 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_sqs/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     3210 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_sqs/test_server.py
--rw-r--r--   0 runner    (1001) docker     (123)   108705 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_sqs/test_sqs.py
--rw-r--r--   0 runner    (1001) docker     (123)     7836 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_sqs/test_sqs_cloudformation.py
--rw-r--r--   0 runner    (1001) docker     (123)     4419 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_sqs/test_sqs_integration.py
--rw-r--r--   0 runner    (1001) docker     (123)     1266 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_sqs/test_sqs_multiaccount.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:53.185519 moto-4.1.7.dev8/tests/test_ssm/
--rw-r--r--   0 runner    (1001) docker     (123)       41 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_ssm/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    71927 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_ssm/test_ssm_boto3.py
--rw-r--r--   0 runner    (1001) docker     (123)     2109 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_ssm/test_ssm_cloudformation.py
--rw-r--r--   0 runner    (1001) docker     (123)     1122 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_ssm/test_ssm_default_amis.py
--rw-r--r--   0 runner    (1001) docker     (123)     1476 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_ssm/test_ssm_defaults.py
--rw-r--r--   0 runner    (1001) docker     (123)     6621 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_ssm/test_ssm_doc_permissions.py
--rw-r--r--   0 runner    (1001) docker     (123)    28425 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_ssm/test_ssm_docs.py
--rw-r--r--   0 runner    (1001) docker     (123)      499 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_ssm/test_ssm_ec2_integration.py
--rw-r--r--   0 runner    (1001) docker     (123)      655 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_ssm/test_ssm_ecs_images.py
--rw-r--r--   0 runner    (1001) docker     (123)     5334 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_ssm/test_ssm_maintenance_windows.py
--rw-r--r--   0 runner    (1001) docker     (123)     2807 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_ssm/test_ssm_parameterstore.py
--rw-r--r--   0 runner    (1001) docker     (123)     4747 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_ssm/test_ssm_secretsmanager.py
--rw-r--r--   0 runner    (1001) docker     (123)     3134 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_ssm/test_ssm_utils.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:53.185519 moto-4.1.7.dev8/tests/test_ssm/test_templates/
--rw-r--r--   0 runner    (1001) docker     (123)     1047 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_ssm/test_templates/good.yaml
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:53.185519 moto-4.1.7.dev8/tests/test_ssoadmin/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_ssoadmin/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      866 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_ssoadmin/test_server.py
--rw-r--r--   0 runner    (1001) docker     (123)    13607 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_ssoadmin/test_ssoadmin.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:53.189519 moto-4.1.7.dev8/tests/test_stepfunctions/
--rw-r--r--   0 runner    (1001) docker     (123)       41 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_stepfunctions/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    34000 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_stepfunctions/test_stepfunctions.py
--rw-r--r--   0 runner    (1001) docker     (123)     9078 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_stepfunctions/test_stepfunctions_cloudformation.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:53.189519 moto-4.1.7.dev8/tests/test_sts/
--rw-r--r--   0 runner    (1001) docker     (123)       41 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_sts/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     1501 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_sts/test_server.py
--rw-r--r--   0 runner    (1001) docker     (123)    33741 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_sts/test_sts.py
--rw-r--r--   0 runner    (1001) docker     (123)     8506 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_sts/test_sts_integration.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:53.189519 moto-4.1.7.dev8/tests/test_support/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_support/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     1866 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_support/test_server.py
--rw-r--r--   0 runner    (1001) docker     (123)    24299 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_support/test_support.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:53.189519 moto-4.1.7.dev8/tests/test_swf/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_swf/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:53.193519 moto-4.1.7.dev8/tests/test_swf/models/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_swf/models/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     5333 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_swf/models/test_activity_task.py
--rw-r--r--   0 runner    (1001) docker     (123)     2452 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_swf/models/test_decision_task.py
--rw-r--r--   0 runner    (1001) docker     (123)     4296 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_swf/models/test_domain.py
--rw-r--r--   0 runner    (1001) docker     (123)     1925 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_swf/models/test_generic_type.py
--rw-r--r--   0 runner    (1001) docker     (123)     1004 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_swf/models/test_history_event.py
--rw-r--r--   0 runner    (1001) docker     (123)      539 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_swf/models/test_timeout.py
--rw-r--r--   0 runner    (1001) docker     (123)     1187 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_swf/models/test_timer.py
--rw-r--r--   0 runner    (1001) docker     (123)    25245 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_swf/models/test_workflow_execution.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:53.193519 moto-4.1.7.dev8/tests/test_swf/responses/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_swf/responses/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    10547 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_swf/responses/test_activity_tasks.py
--rw-r--r--   0 runner    (1001) docker     (123)     9946 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_swf/responses/test_activity_types.py
--rw-r--r--   0 runner    (1001) docker     (123)    21702 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_swf/responses/test_decision_tasks.py
--rw-r--r--   0 runner    (1001) docker     (123)     7574 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_swf/responses/test_domains.py
--rw-r--r--   0 runner    (1001) docker     (123)     5841 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_swf/responses/test_timeouts.py
--rw-r--r--   0 runner    (1001) docker     (123)    13819 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_swf/responses/test_workflow_executions.py
--rw-r--r--   0 runner    (1001) docker     (123)    10319 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_swf/responses/test_workflow_types.py
--rw-r--r--   0 runner    (1001) docker     (123)     5190 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_swf/test_exceptions.py
--rw-r--r--   0 runner    (1001) docker     (123)      293 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_swf/test_utils.py
--rw-r--r--   0 runner    (1001) docker     (123)     3875 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_swf/utils.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:53.193519 moto-4.1.7.dev8/tests/test_textract/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_textract/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     3011 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_textract/test_server.py
--rw-r--r--   0 runner    (1001) docker     (123)     2993 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_textract/test_textract.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:53.193519 moto-4.1.7.dev8/tests/test_timestreamwrite/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_timestreamwrite/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      514 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_timestreamwrite/test_server.py
--rw-r--r--   0 runner    (1001) docker     (123)     4386 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_timestreamwrite/test_timestreamwrite_database.py
--rw-r--r--   0 runner    (1001) docker     (123)    11135 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_timestreamwrite/test_timestreamwrite_table.py
--rw-r--r--   0 runner    (1001) docker     (123)     2866 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_timestreamwrite/test_timestreamwrite_tagging.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:53.193519 moto-4.1.7.dev8/tests/test_transcribe/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_transcribe/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    42714 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_transcribe/test_transcribe_boto3.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:53.197519 moto-4.1.7.dev8/tests/test_utilities/
--rw-r--r--   0 runner    (1001) docker     (123)     1058 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_utilities/test_docker_utilities.py
--rw-r--r--   0 runner    (1001) docker     (123)    10316 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_utilities/test_paginator.py
--rw-r--r--   0 runner    (1001) docker     (123)     6764 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_utilities/test_tagging_service.py
--rw-r--r--   0 runner    (1001) docker     (123)     3562 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_utilities/test_threaded_server.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:53.197519 moto-4.1.7.dev8/tests/test_wafv2/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_wafv2/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      400 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_wafv2/test_helper_functions.py
--rw-r--r--   0 runner    (1001) docker     (123)     2793 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_wafv2/test_server.py
--rw-r--r--   0 runner    (1001) docker     (123)      614 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_wafv2/test_utils.py
--rw-r--r--   0 runner    (1001) docker     (123)     7288 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_wafv2/test_wafv2.py
--rw-r--r--   0 runner    (1001) docker     (123)     3506 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_wafv2/test_wafv2_integration.py
--rw-r--r--   0 runner    (1001) docker     (123)      249 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_wafv2/test_wafv2_rules.py
--rw-r--r--   0 runner    (1001) docker     (123)     2600 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_wafv2/test_wafv2_tags.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:17:53.197519 moto-4.1.7.dev8/tests/test_xray/
--rw-r--r--   0 runner    (1001) docker     (123)       41 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_xray/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     4143 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_xray/test_xray_boto3.py
--rw-r--r--   0 runner    (1001) docker     (123)     4990 2023-03-28 19:17:43.000000 moto-4.1.7.dev8/tests/test_xray/test_xray_client.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.668212 moto-4.1.7.dev9/
+-rw-r--r--   0 runner    (1001) docker     (123)     2976 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/AUTHORS.md
+-rw-r--r--   0 runner    (1001) docker     (123)    10834 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (123)      919 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/MANIFEST.in
+-rw-r--r--   0 runner    (1001) docker     (123)     6287 2023-03-28 19:15:35.668212 moto-4.1.7.dev9/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     2512 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/README.md
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.212195 moto-4.1.7.dev9/moto/
+-rw-r--r--   0 runner    (1001) docker     (123)     8775 2023-03-28 19:15:27.000000 moto-4.1.7.dev9/moto/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.212195 moto-4.1.7.dev9/moto/acm/
+-rw-r--r--   0 runner    (1001) docker     (123)      155 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/acm/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      511 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/acm/exceptions.py
+-rw-r--r--   0 runner    (1001) docker     (123)    21261 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/acm/models.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8771 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/acm/responses.py
+-rw-r--r--   0 runner    (1001) docker     (123)      169 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/acm/urls.py
+-rw-r--r--   0 runner    (1001) docker     (123)      313 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/acm/utils.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.216195 moto-4.1.7.dev9/moto/acmpca/
+-rw-r--r--   0 runner    (1001) docker     (123)      191 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/acmpca/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      261 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/acmpca/exceptions.py
+-rw-r--r--   0 runner    (1001) docker     (123)    12457 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/acmpca/models.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6712 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/acmpca/responses.py
+-rw-r--r--   0 runner    (1001) docker     (123)      190 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/acmpca/urls.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.216195 moto-4.1.7.dev9/moto/amp/
+-rw-r--r--   0 runner    (1001) docker     (123)      179 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/amp/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1054 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/amp/exceptions.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7938 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/amp/models.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6717 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/amp/responses.py
+-rw-r--r--   0 runner    (1001) docker     (123)      876 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/amp/urls.py
+-rw-r--r--   0 runner    (1001) docker     (123)      476 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/amp/utils.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.216195 moto-4.1.7.dev9/moto/apigateway/
+-rw-r--r--   0 runner    (1001) docker     (123)      190 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/apigateway/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7520 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/apigateway/exceptions.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.216195 moto-4.1.7.dev9/moto/apigateway/integration_parsers/
+-rw-r--r--   0 runner    (1001) docker     (123)      305 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/apigateway/integration_parsers/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1371 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/apigateway/integration_parsers/aws_parser.py
+-rw-r--r--   0 runner    (1001) docker     (123)      600 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/apigateway/integration_parsers/http_parser.py
+-rw-r--r--   0 runner    (1001) docker     (123)      511 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/apigateway/integration_parsers/unknown_parser.py
+-rw-r--r--   0 runner    (1001) docker     (123)    91746 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/apigateway/models.py
+-rw-r--r--   0 runner    (1001) docker     (123)    40056 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/apigateway/responses.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3687 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/apigateway/urls.py
+-rw-r--r--   0 runner    (1001) docker     (123)      607 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/apigateway/utils.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.220195 moto-4.1.7.dev9/moto/apigatewayv2/
+-rw-r--r--   0 runner    (1001) docker     (123)      215 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/apigatewayv2/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3040 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/apigatewayv2/exceptions.py
+-rw-r--r--   0 runner    (1001) docker     (123)    64715 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/apigatewayv2/models.py
+-rw-r--r--   0 runner    (1001) docker     (123)    36307 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/apigatewayv2/responses.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2415 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/apigatewayv2/urls.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.220195 moto-4.1.7.dev9/moto/applicationautoscaling/
+-rw-r--r--   0 runner    (1001) docker     (123)      172 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/applicationautoscaling/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      197 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/applicationautoscaling/exceptions.py
+-rw-r--r--   0 runner    (1001) docker     (123)    19977 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/applicationautoscaling/models.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9948 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/applicationautoscaling/responses.py
+-rw-r--r--   0 runner    (1001) docker     (123)      197 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/applicationautoscaling/urls.py
+-rw-r--r--   0 runner    (1001) docker     (123)      227 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/applicationautoscaling/utils.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.220195 moto-4.1.7.dev9/moto/appsync/
+-rw-r--r--   0 runner    (1001) docker     (123)      195 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/appsync/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      357 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/appsync/exceptions.py
+-rw-r--r--   0 runner    (1001) docker     (123)    11432 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/appsync/models.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9910 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/appsync/responses.py
+-rw-r--r--   0 runner    (1001) docker     (123)      750 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/appsync/urls.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.224195 moto-4.1.7.dev9/moto/athena/
+-rw-r--r--   0 runner    (1001) docker     (123)      170 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/athena/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      551 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/athena/exceptions.py
+-rw-r--r--   0 runner    (1001) docker     (123)    12434 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/athena/models.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8425 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/athena/responses.py
+-rw-r--r--   0 runner    (1001) docker     (123)      142 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/athena/urls.py
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/athena/utils.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.224195 moto-4.1.7.dev9/moto/autoscaling/
+-rw-r--r--   0 runner    (1001) docker     (123)      195 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/autoscaling/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      718 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/autoscaling/exceptions.py
+-rw-r--r--   0 runner    (1001) docker     (123)    61357 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/autoscaling/models.py
+-rw-r--r--   0 runner    (1001) docker     (123)    65472 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/autoscaling/responses.py
+-rw-r--r--   0 runner    (1001) docker     (123)      157 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/autoscaling/urls.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.224195 moto-4.1.7.dev9/moto/awslambda/
+-rw-r--r--   0 runner    (1001) docker     (123)      170 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/awslambda/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2126 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/awslambda/exceptions.py
+-rw-r--r--   0 runner    (1001) docker     (123)    75083 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/awslambda/models.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6258 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/awslambda/policy.py
+-rw-r--r--   0 runner    (1001) docker     (123)    23480 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/awslambda/responses.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2646 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/awslambda/urls.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1146 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/awslambda/utils.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9961 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/backend_index.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1805 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/backends.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.228196 moto-4.1.7.dev9/moto/batch/
+-rw-r--r--   0 runner    (1001) docker     (123)      165 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/batch/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      433 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/batch/exceptions.py
+-rw-r--r--   0 runner    (1001) docker     (123)    69404 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/batch/models.py
+-rw-r--r--   0 runner    (1001) docker     (123)    10487 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/batch/responses.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1468 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/batch/urls.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1276 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/batch/utils.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.228196 moto-4.1.7.dev9/moto/batch_simple/
+-rw-r--r--   0 runner    (1001) docker     (123)      193 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/batch_simple/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2828 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/batch_simple/models.py
+-rw-r--r--   0 runner    (1001) docker     (123)      377 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/batch_simple/responses.py
+-rw-r--r--   0 runner    (1001) docker     (123)      258 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/batch_simple/urls.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.228196 moto-4.1.7.dev9/moto/budgets/
+-rw-r--r--   0 runner    (1001) docker     (123)      127 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/budgets/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      901 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/budgets/exceptions.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5665 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/budgets/models.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2737 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/budgets/responses.py
+-rw-r--r--   0 runner    (1001) docker     (123)      154 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/budgets/urls.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.228196 moto-4.1.7.dev9/moto/ce/
+-rw-r--r--   0 runner    (1001) docker     (123)      175 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ce/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      294 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ce/exceptions.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5275 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ce/models.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3907 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ce/responses.py
+-rw-r--r--   0 runner    (1001) docker     (123)      193 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ce/urls.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.232196 moto-4.1.7.dev9/moto/cloudformation/
+-rw-r--r--   0 runner    (1001) docker     (123)      210 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/cloudformation/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3450 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/cloudformation/custom_model.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2857 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/cloudformation/exceptions.py
+-rw-r--r--   0 runner    (1001) docker     (123)    45880 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/cloudformation/models.py
+-rw-r--r--   0 runner    (1001) docker     (123)    37479 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/cloudformation/parsing.py
+-rw-r--r--   0 runner    (1001) docker     (123)    53038 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/cloudformation/responses.py
+-rw-r--r--   0 runner    (1001) docker     (123)      266 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/cloudformation/urls.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3751 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/cloudformation/utils.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.232196 moto-4.1.7.dev9/moto/cloudfront/
+-rw-r--r--   0 runner    (1001) docker     (123)      136 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/cloudfront/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2202 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/cloudfront/exceptions.py
+-rw-r--r--   0 runner    (1001) docker     (123)    14571 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/cloudfront/models.py
+-rw-r--r--   0 runner    (1001) docker     (123)    30155 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/cloudfront/responses.py
+-rw-r--r--   0 runner    (1001) docker     (123)      590 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/cloudfront/urls.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.232196 moto-4.1.7.dev9/moto/cloudtrail/
+-rw-r--r--   0 runner    (1001) docker     (123)      207 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/cloudtrail/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2203 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/cloudtrail/exceptions.py
+-rw-r--r--   0 runner    (1001) docker     (123)    15598 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/cloudtrail/models.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7759 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/cloudtrail/responses.py
+-rw-r--r--   0 runner    (1001) docker     (123)      221 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/cloudtrail/urls.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.236196 moto-4.1.7.dev9/moto/cloudwatch/
+-rw-r--r--   0 runner    (1001) docker     (123)      136 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/cloudwatch/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      989 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/cloudwatch/exceptions.py
+-rw-r--r--   0 runner    (1001) docker     (123)    33739 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/cloudwatch/models.py
+-rw-r--r--   0 runner    (1001) docker     (123)    30696 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/cloudwatch/responses.py
+-rw-r--r--   0 runner    (1001) docker     (123)      153 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/cloudwatch/urls.py
+-rw-r--r--   0 runner    (1001) docker     (123)      280 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/cloudwatch/utils.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.236196 moto-4.1.7.dev9/moto/codebuild/
+-rw-r--r--   0 runner    (1001) docker     (123)      133 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/codebuild/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      606 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/codebuild/exceptions.py
+-rw-r--r--   0 runner    (1001) docker     (123)    10568 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/codebuild/models.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6835 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/codebuild/responses.py
+-rw-r--r--   0 runner    (1001) docker     (123)      151 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/codebuild/urls.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.236196 moto-4.1.7.dev9/moto/codecommit/
+-rw-r--r--   0 runner    (1001) docker     (123)      136 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/codecommit/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1075 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/codecommit/exceptions.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3105 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/codecommit/models.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1933 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/codecommit/responses.py
+-rw-r--r--   0 runner    (1001) docker     (123)      154 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/codecommit/urls.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.236196 moto-4.1.7.dev9/moto/codepipeline/
+-rw-r--r--   0 runner    (1001) docker     (123)      142 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/codepipeline/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      916 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/codepipeline/exceptions.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7694 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/codepipeline/models.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1933 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/codepipeline/responses.py
+-rw-r--r--   0 runner    (1001) docker     (123)      160 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/codepipeline/urls.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.240196 moto-4.1.7.dev9/moto/cognitoidentity/
+-rw-r--r--   0 runner    (1001) docker     (123)      151 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/cognitoidentity/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      595 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/cognitoidentity/exceptions.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6990 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/cognitoidentity/models.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3684 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/cognitoidentity/responses.py
+-rw-r--r--   0 runner    (1001) docker     (123)      169 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/cognitoidentity/urls.py
+-rw-r--r--   0 runner    (1001) docker     (123)      143 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/cognitoidentity/utils.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.240196 moto-4.1.7.dev9/moto/cognitoidp/
+-rw-r--r--   0 runner    (1001) docker     (123)      136 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/cognitoidp/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1959 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/cognitoidp/exceptions.py
+-rw-r--r--   0 runner    (1001) docker     (123)    83773 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/cognitoidp/models.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.240196 moto-4.1.7.dev9/moto/cognitoidp/resources/
+-rw-r--r--   0 runner    (1001) docker     (123)      792 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/cognitoidp/resources/jwks-private.json
+-rw-r--r--   0 runner    (1001) docker     (123)      491 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/cognitoidp/resources/jwks-public.json
+-rw-r--r--   0 runner    (1001) docker     (123)    24950 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/cognitoidp/responses.py
+-rw-r--r--   0 runner    (1001) docker     (123)      300 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/cognitoidp/urls.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2940 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/cognitoidp/utils.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.240196 moto-4.1.7.dev9/moto/comprehend/
+-rw-r--r--   0 runner    (1001) docker     (123)      207 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/comprehend/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      318 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/comprehend/exceptions.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4985 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/comprehend/models.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3930 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/comprehend/responses.py
+-rw-r--r--   0 runner    (1001) docker     (123)      205 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/comprehend/urls.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.240196 moto-4.1.7.dev9/moto/config/
+-rw-r--r--   0 runner    (1001) docker     (123)      124 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/config/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    11897 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/config/exceptions.py
+-rw-r--r--   0 runner    (1001) docker     (123)    77608 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/config/models.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.244196 moto-4.1.7.dev9/moto/config/resources/
+-rw-r--r--   0 runner    (1001) docker     (123)   117575 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/config/resources/aws_managed_rules.json
+-rw-r--r--   0 runner    (1001) docker     (123)     8828 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/config/responses.py
+-rw-r--r--   0 runner    (1001) docker     (123)      142 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/config/urls.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.244196 moto-4.1.7.dev9/moto/core/
+-rw-r--r--   0 runner    (1001) docker     (123)      439 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/core/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    11074 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/core/base_backend.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2455 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/core/botocore_stubber.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9179 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/core/common_models.py
+-rw-r--r--   0 runner    (1001) docker     (123)      155 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/core/common_types.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6436 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/core/custom_responses_mock.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5438 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/core/exceptions.py
+-rw-r--r--   0 runner    (1001) docker     (123)      482 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/core/model_instances.py
+-rw-r--r--   0 runner    (1001) docker     (123)    15270 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/core/models.py
+-rw-r--r--   0 runner    (1001) docker     (123)    40468 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/core/responses.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1705 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/core/responses_custom_registry.py
+-rw-r--r--   0 runner    (1001) docker     (123)    10961 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/core/utils.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.248196 moto-4.1.7.dev9/moto/databrew/
+-rw-r--r--   0 runner    (1001) docker     (123)      130 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/databrew/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1398 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/databrew/exceptions.py
+-rw-r--r--   0 runner    (1001) docker     (123)    25372 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/databrew/models.py
+-rw-r--r--   0 runner    (1001) docker     (123)    19227 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/databrew/responses.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1170 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/databrew/urls.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.248196 moto-4.1.7.dev9/moto/datapipeline/
+-rw-r--r--   0 runner    (1001) docker     (123)      142 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/datapipeline/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5687 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/datapipeline/models.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3659 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/datapipeline/responses.py
+-rw-r--r--   0 runner    (1001) docker     (123)      160 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/datapipeline/urls.py
+-rw-r--r--   0 runner    (1001) docker     (123)      878 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/datapipeline/utils.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.248196 moto-4.1.7.dev9/moto/datasync/
+-rw-r--r--   0 runner    (1001) docker     (123)      180 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/datasync/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      351 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/datasync/exceptions.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8414 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/datasync/models.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6465 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/datasync/responses.py
+-rw-r--r--   0 runner    (1001) docker     (123)      156 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/datasync/urls.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.248196 moto-4.1.7.dev9/moto/dax/
+-rw-r--r--   0 runner    (1001) docker     (123)      179 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/dax/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      552 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/dax/exceptions.py
+-rw-r--r--   0 runner    (1001) docker     (123)    10023 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/dax/models.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4729 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/dax/responses.py
+-rw-r--r--   0 runner    (1001) docker     (123)      177 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/dax/urls.py
+-rw-r--r--   0 runner    (1001) docker     (123)      195 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/dax/utils.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.252196 moto-4.1.7.dev9/moto/dms/
+-rw-r--r--   0 runner    (1001) docker     (123)      155 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/dms/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      551 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/dms/exceptions.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7041 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/dms/models.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2859 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/dms/responses.py
+-rw-r--r--   0 runner    (1001) docker     (123)      183 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/dms/urls.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1574 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/dms/utils.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.252196 moto-4.1.7.dev9/moto/ds/
+-rw-r--r--   0 runner    (1001) docker     (123)      175 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ds/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2998 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ds/exceptions.py
+-rw-r--r--   0 runner    (1001) docker     (123)    21712 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ds/models.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6531 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ds/responses.py
+-rw-r--r--   0 runner    (1001) docker     (123)      201 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ds/urls.py
+-rw-r--r--   0 runner    (1001) docker     (123)      475 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ds/utils.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5236 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ds/validations.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.252196 moto-4.1.7.dev9/moto/dynamodb/
+-rw-r--r--   0 runner    (1001) docker     (123)      193 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/dynamodb/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    42639 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/dynamodb/comparisons.py
+-rw-r--r--   0 runner    (1001) docker     (123)    12266 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/dynamodb/exceptions.py
+-rw-r--r--   0 runner    (1001) docker     (123)      192 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/dynamodb/limits.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.252196 moto-4.1.7.dev9/moto/dynamodb/models/
+-rw-r--r--   0 runner    (1001) docker     (123)    29890 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/dynamodb/models/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    16297 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/dynamodb/models/dynamo_type.py
+-rw-r--r--   0 runner    (1001) docker     (123)    39690 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/dynamodb/models/table.py
+-rw-r--r--   0 runner    (1001) docker     (123)      363 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/dynamodb/models/utilities.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.256197 moto-4.1.7.dev9/moto/dynamodb/parsing/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/dynamodb/parsing/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    14200 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/dynamodb/parsing/ast_nodes.py
+-rw-r--r--   0 runner    (1001) docker     (123)    12062 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/dynamodb/parsing/executors.py
+-rw-r--r--   0 runner    (1001) docker     (123)    34656 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/dynamodb/parsing/expressions.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9356 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/dynamodb/parsing/key_condition_expression.py
+-rw-r--r--   0 runner    (1001) docker     (123)      893 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/dynamodb/parsing/reserved_keywords.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4136 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/dynamodb/parsing/reserved_keywords.txt
+-rw-r--r--   0 runner    (1001) docker     (123)     8340 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/dynamodb/parsing/tokens.py
+-rw-r--r--   0 runner    (1001) docker     (123)    18402 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/dynamodb/parsing/validators.py
+-rw-r--r--   0 runner    (1001) docker     (123)    44274 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/dynamodb/responses.py
+-rw-r--r--   0 runner    (1001) docker     (123)      141 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/dynamodb/urls.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.256197 moto-4.1.7.dev9/moto/dynamodb_v20111205/
+-rw-r--r--   0 runner    (1001) docker     (123)      267 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/dynamodb_v20111205/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1193 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/dynamodb_v20111205/comparisons.py
+-rw-r--r--   0 runner    (1001) docker     (123)    13284 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/dynamodb_v20111205/models.py
+-rw-r--r--   0 runner    (1001) docker     (123)    11594 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/dynamodb_v20111205/responses.py
+-rw-r--r--   0 runner    (1001) docker     (123)      141 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/dynamodb_v20111205/urls.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.256197 moto-4.1.7.dev9/moto/dynamodbstreams/
+-rw-r--r--   0 runner    (1001) docker     (123)      215 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/dynamodbstreams/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5453 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/dynamodbstreams/models.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1439 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/dynamodbstreams/responses.py
+-rw-r--r--   0 runner    (1001) docker     (123)      168 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/dynamodbstreams/urls.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.260197 moto-4.1.7.dev9/moto/ebs/
+-rw-r--r--   0 runner    (1001) docker     (123)      179 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ebs/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4892 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ebs/models.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5872 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ebs/responses.py
+-rw-r--r--   0 runner    (1001) docker     (123)      557 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ebs/urls.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.260197 moto-4.1.7.dev9/moto/ec2/
+-rw-r--r--   0 runner    (1001) docker     (123)      115 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ec2/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    24247 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ec2/exceptions.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.268197 moto-4.1.7.dev9/moto/ec2/models/
+-rw-r--r--   0 runner    (1001) docker     (123)    10045 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ec2/models/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    13217 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ec2/models/amis.py
+-rw-r--r--   0 runner    (1001) docker     (123)    12295 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ec2/models/availability_zones_and_regions.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2333 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ec2/models/carrier_gateways.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1513 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ec2/models/core.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3612 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ec2/models/customer_gateways.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4823 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ec2/models/dhcp_options.py
+-rw-r--r--   0 runner    (1001) docker     (123)    19544 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ec2/models/elastic_block_store.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9062 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ec2/models/elastic_ip_addresses.py
+-rw-r--r--   0 runner    (1001) docker     (123)    16013 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ec2/models/elastic_network_interfaces.py
+-rw-r--r--   0 runner    (1001) docker     (123)    12318 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ec2/models/fleets.py
+-rw-r--r--   0 runner    (1001) docker     (123)    11151 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ec2/models/flow_logs.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3271 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ec2/models/hosts.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5723 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ec2/models/iam_instance_profile.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8212 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ec2/models/instance_types.py
+-rw-r--r--   0 runner    (1001) docker     (123)    36950 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ec2/models/instances.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6237 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ec2/models/internet_gateways.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2583 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ec2/models/key_pairs.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8321 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ec2/models/launch_templates.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6670 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ec2/models/managed_prefixes.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5145 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ec2/models/nat_gateways.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9951 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ec2/models/network_acls.py
+-rw-r--r--   0 runner    (1001) docker     (123)    20808 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ec2/models/route_tables.py
+-rw-r--r--   0 runner    (1001) docker     (123)    47173 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ec2/models/security_groups.py
+-rw-r--r--   0 runner    (1001) docker     (123)    20404 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ec2/models/spot_requests.py
+-rw-r--r--   0 runner    (1001) docker     (123)    17073 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ec2/models/subnets.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5290 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ec2/models/tags.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4619 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ec2/models/transit_gateway.py
+-rw-r--r--   0 runner    (1001) docker     (123)    12869 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ec2/models/transit_gateway_attachments.py
+-rw-r--r--   0 runner    (1001) docker     (123)    14765 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ec2/models/transit_gateway_route_tables.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7076 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ec2/models/vpc_peering_connections.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5614 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ec2/models/vpc_service_configuration.py
+-rw-r--r--   0 runner    (1001) docker     (123)    33929 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ec2/models/vpcs.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3356 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ec2/models/vpn_connections.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6508 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ec2/models/vpn_gateway.py
+-rw-r--r--   0 runner    (1001) docker     (123)      381 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ec2/models/windows.py
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ec2/regions.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.268197 moto-4.1.7.dev9/moto/ec2/resources/
+-rw-r--r--   0 runner    (1001) docker     (123)    24777 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ec2/resources/amis.json
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.176194 moto-4.1.7.dev9/moto/ec2/resources/ecs/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.280197 moto-4.1.7.dev9/moto/ec2/resources/ecs/optimized_amis/
+-rw-r--r--   0 runner    (1001) docker     (123)   110385 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ec2/resources/ecs/optimized_amis/af-south-1.json
+-rw-r--r--   0 runner    (1001) docker     (123)   184754 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ec2/resources/ecs/optimized_amis/ap-east-1.json
+-rw-r--r--   0 runner    (1001) docker     (123)   237334 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ec2/resources/ecs/optimized_amis/ap-northeast-1.json
+-rw-r--r--   0 runner    (1001) docker     (123)   205924 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ec2/resources/ecs/optimized_amis/ap-northeast-2.json
+-rw-r--r--   0 runner    (1001) docker     (123)    76970 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ec2/resources/ecs/optimized_amis/ap-northeast-3.json
+-rw-r--r--   0 runner    (1001) docker     (123)   233439 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ec2/resources/ecs/optimized_amis/ap-south-1.json
+-rw-r--r--   0 runner    (1001) docker     (123)    13740 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ec2/resources/ecs/optimized_amis/ap-south-2.json
+-rw-r--r--   0 runner    (1001) docker     (123)   224300 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ec2/resources/ecs/optimized_amis/ap-southeast-1.json
+-rw-r--r--   0 runner    (1001) docker     (123)   237334 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ec2/resources/ecs/optimized_amis/ap-southeast-2.json
+-rw-r--r--   0 runner    (1001) docker     (123)    41214 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ec2/resources/ecs/optimized_amis/ap-southeast-3.json
+-rw-r--r--   0 runner    (1001) docker     (123)   204442 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ec2/resources/ecs/optimized_amis/ca-central-1.json
+-rw-r--r--   0 runner    (1001) docker     (123)   236846 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ec2/resources/ecs/optimized_amis/eu-central-1.json
+-rw-r--r--   0 runner    (1001) docker     (123)    13740 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ec2/resources/ecs/optimized_amis/eu-central-2.json
+-rw-r--r--   0 runner    (1001) docker     (123)   196475 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ec2/resources/ecs/optimized_amis/eu-north-1.json
+-rw-r--r--   0 runner    (1001) docker     (123)   151250 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ec2/resources/ecs/optimized_amis/eu-south-1.json
+-rw-r--r--   0 runner    (1001) docker     (123)    16169 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ec2/resources/ecs/optimized_amis/eu-south-2.json
+-rw-r--r--   0 runner    (1001) docker     (123)   241191 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ec2/resources/ecs/optimized_amis/eu-west-1.json
+-rw-r--r--   0 runner    (1001) docker     (123)   205418 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ec2/resources/ecs/optimized_amis/eu-west-2.json
+-rw-r--r--   0 runner    (1001) docker     (123)   205543 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ec2/resources/ecs/optimized_amis/eu-west-3.json
+-rw-r--r--   0 runner    (1001) docker     (123)    27007 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ec2/resources/ecs/optimized_amis/me-central-1.json
+-rw-r--r--   0 runner    (1001) docker     (123)   170773 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ec2/resources/ecs/optimized_amis/me-south-1.json
+-rw-r--r--   0 runner    (1001) docker     (123)   216660 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ec2/resources/ecs/optimized_amis/sa-east-1.json
+-rw-r--r--   0 runner    (1001) docker     (123)   244124 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ec2/resources/ecs/optimized_amis/us-east-1.json
+-rw-r--r--   0 runner    (1001) docker     (123)   241191 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ec2/resources/ecs/optimized_amis/us-east-2.json
+-rw-r--r--   0 runner    (1001) docker     (123)   219056 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ec2/resources/ecs/optimized_amis/us-west-1.json
+-rw-r--r--   0 runner    (1001) docker     (123)   243613 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ec2/resources/ecs/optimized_amis/us-west-2.json
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.176194 moto-4.1.7.dev9/moto/ec2/resources/instance_type_offerings/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.288198 moto-4.1.7.dev9/moto/ec2/resources/instance_type_offerings/availability-zone/
+-rw-r--r--   0 runner    (1001) docker     (123)    34118 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ec2/resources/instance_type_offerings/availability-zone/af-south-1.json
+-rw-r--r--   0 runner    (1001) docker     (123)    38329 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ec2/resources/instance_type_offerings/availability-zone/ap-east-1.json
+-rw-r--r--   0 runner    (1001) docker     (123)   112314 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ec2/resources/instance_type_offerings/availability-zone/ap-northeast-1.json
+-rw-r--r--   0 runner    (1001) docker     (123)    77322 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ec2/resources/instance_type_offerings/availability-zone/ap-northeast-2.json
+-rw-r--r--   0 runner    (1001) docker     (123)    39526 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ec2/resources/instance_type_offerings/availability-zone/ap-northeast-3.json
+-rw-r--r--   0 runner    (1001) docker     (123)    70185 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ec2/resources/instance_type_offerings/availability-zone/ap-south-1.json
+-rw-r--r--   0 runner    (1001) docker     (123)    23840 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ec2/resources/instance_type_offerings/availability-zone/ap-south-2.json
+-rw-r--r--   0 runner    (1001) docker     (123)   100189 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ec2/resources/instance_type_offerings/availability-zone/ap-southeast-1.json
+-rw-r--r--   0 runner    (1001) docker     (123)    98303 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ec2/resources/instance_type_offerings/availability-zone/ap-southeast-2.json
+-rw-r--r--   0 runner    (1001) docker     (123)    29228 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ec2/resources/instance_type_offerings/availability-zone/ap-southeast-3.json
+-rw-r--r--   0 runner    (1001) docker     (123)    63506 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ec2/resources/instance_type_offerings/availability-zone/ca-central-1.json
+-rw-r--r--   0 runner    (1001) docker     (123)   102387 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ec2/resources/instance_type_offerings/availability-zone/eu-central-1.json
+-rw-r--r--   0 runner    (1001) docker     (123)    23689 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ec2/resources/instance_type_offerings/availability-zone/eu-central-2.json
+-rw-r--r--   0 runner    (1001) docker     (123)    47988 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ec2/resources/instance_type_offerings/availability-zone/eu-north-1.json
+-rw-r--r--   0 runner    (1001) docker     (123)    48293 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ec2/resources/instance_type_offerings/availability-zone/eu-south-1.json
+-rw-r--r--   0 runner    (1001) docker     (123)    23840 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ec2/resources/instance_type_offerings/availability-zone/eu-south-2.json
+-rw-r--r--   0 runner    (1001) docker     (123)   121525 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ec2/resources/instance_type_offerings/availability-zone/eu-west-1.json
+-rw-r--r--   0 runner    (1001) docker     (123)    71490 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ec2/resources/instance_type_offerings/availability-zone/eu-west-2.json
+-rw-r--r--   0 runner    (1001) docker     (123)    58608 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ec2/resources/instance_type_offerings/availability-zone/eu-west-3.json
+-rw-r--r--   0 runner    (1001) docker     (123)    24548 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ec2/resources/instance_type_offerings/availability-zone/me-central-1.json
+-rw-r--r--   0 runner    (1001) docker     (123)    33135 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ec2/resources/instance_type_offerings/availability-zone/me-south-1.json
+-rw-r--r--   0 runner    (1001) docker     (123)    64179 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ec2/resources/instance_type_offerings/availability-zone/sa-east-1.json
+-rw-r--r--   0 runner    (1001) docker     (123)   199785 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ec2/resources/instance_type_offerings/availability-zone/us-east-1.json
+-rw-r--r--   0 runner    (1001) docker     (123)   111712 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ec2/resources/instance_type_offerings/availability-zone/us-east-2.json
+-rw-r--r--   0 runner    (1001) docker     (123)    48786 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ec2/resources/instance_type_offerings/availability-zone/us-west-1.json
+-rw-r--r--   0 runner    (1001) docker     (123)   147856 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ec2/resources/instance_type_offerings/availability-zone/us-west-2.json
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.296198 moto-4.1.7.dev9/moto/ec2/resources/instance_type_offerings/availability-zone-id/
+-rw-r--r--   0 runner    (1001) docker     (123)    32606 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ec2/resources/instance_type_offerings/availability-zone-id/af-south-1.json
+-rw-r--r--   0 runner    (1001) docker     (123)    37177 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ec2/resources/instance_type_offerings/availability-zone-id/ap-east-1.json
+-rw-r--r--   0 runner    (1001) docker     (123)   102960 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ec2/resources/instance_type_offerings/availability-zone-id/ap-northeast-1.json
+-rw-r--r--   0 runner    (1001) docker     (123)    70854 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ec2/resources/instance_type_offerings/availability-zone-id/ap-northeast-2.json
+-rw-r--r--   0 runner    (1001) docker     (123)    36220 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ec2/resources/instance_type_offerings/availability-zone-id/ap-northeast-3.json
+-rw-r--r--   0 runner    (1001) docker     (123)    67077 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ec2/resources/instance_type_offerings/availability-zone-id/ap-south-1.json
+-rw-r--r--   0 runner    (1001) docker     (123)    22778 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ec2/resources/instance_type_offerings/availability-zone-id/ap-south-2.json
+-rw-r--r--   0 runner    (1001) docker     (123)    91831 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ec2/resources/instance_type_offerings/availability-zone-id/ap-southeast-1.json
+-rw-r--r--   0 runner    (1001) docker     (123)    90095 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ec2/resources/instance_type_offerings/availability-zone-id/ap-southeast-2.json
+-rw-r--r--   0 runner    (1001) docker     (123)    26780 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ec2/resources/instance_type_offerings/availability-zone-id/ap-southeast-3.json
+-rw-r--r--   0 runner    (1001) docker     (123)    58961 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ec2/resources/instance_type_offerings/availability-zone-id/ca-central-1.json
+-rw-r--r--   0 runner    (1001) docker     (123)    95067 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ec2/resources/instance_type_offerings/availability-zone-id/eu-central-1.json
+-rw-r--r--   0 runner    (1001) docker     (123)    21984 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ec2/resources/instance_type_offerings/availability-zone-id/eu-central-2.json
+-rw-r--r--   0 runner    (1001) docker     (123)    45867 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ec2/resources/instance_type_offerings/availability-zone-id/eu-north-1.json
+-rw-r--r--   0 runner    (1001) docker     (123)    46157 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ec2/resources/instance_type_offerings/availability-zone-id/eu-south-1.json
+-rw-r--r--   0 runner    (1001) docker     (123)    22778 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ec2/resources/instance_type_offerings/availability-zone-id/eu-south-2.json
+-rw-r--r--   0 runner    (1001) docker     (123)   117899 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ec2/resources/instance_type_offerings/availability-zone-id/eu-west-1.json
+-rw-r--r--   0 runner    (1001) docker     (123)    69350 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ec2/resources/instance_type_offerings/availability-zone-id/eu-west-2.json
+-rw-r--r--   0 runner    (1001) docker     (123)    56856 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ec2/resources/instance_type_offerings/availability-zone-id/eu-west-3.json
+-rw-r--r--   0 runner    (1001) docker     (123)    22778 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ec2/resources/instance_type_offerings/availability-zone-id/me-central-1.json
+-rw-r--r--   0 runner    (1001) docker     (123)    31665 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ec2/resources/instance_type_offerings/availability-zone-id/me-south-1.json
+-rw-r--r--   0 runner    (1001) docker     (123)    62257 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ec2/resources/instance_type_offerings/availability-zone-id/sa-east-1.json
+-rw-r--r--   0 runner    (1001) docker     (123)   193821 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ec2/resources/instance_type_offerings/availability-zone-id/us-east-1.json
+-rw-r--r--   0 runner    (1001) docker     (123)   108380 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ec2/resources/instance_type_offerings/availability-zone-id/us-east-2.json
+-rw-r--r--   0 runner    (1001) docker     (123)    47322 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ec2/resources/instance_type_offerings/availability-zone-id/us-west-1.json
+-rw-r--r--   0 runner    (1001) docker     (123)   143444 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ec2/resources/instance_type_offerings/availability-zone-id/us-west-2.json
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.304198 moto-4.1.7.dev9/moto/ec2/resources/instance_type_offerings/region/
+-rw-r--r--   0 runner    (1001) docker     (123)    11746 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ec2/resources/instance_type_offerings/region/af-south-1.json
+-rw-r--r--   0 runner    (1001) docker     (123)    12719 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ec2/resources/instance_type_offerings/region/ap-east-1.json
+-rw-r--r--   0 runner    (1001) docker     (123)    40058 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ec2/resources/instance_type_offerings/region/ap-northeast-1.json
+-rw-r--r--   0 runner    (1001) docker     (123)    25337 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ec2/resources/instance_type_offerings/region/ap-northeast-2.json
+-rw-r--r--   0 runner    (1001) docker     (123)    15559 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ec2/resources/instance_type_offerings/region/ap-northeast-3.json
+-rw-r--r--   0 runner    (1001) docker     (123)    24687 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ec2/resources/instance_type_offerings/region/ap-south-1.json
+-rw-r--r--   0 runner    (1001) docker     (123)     7830 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ec2/resources/instance_type_offerings/region/ap-south-2.json
+-rw-r--r--   0 runner    (1001) docker     (123)    36117 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ec2/resources/instance_type_offerings/region/ap-southeast-1.json
+-rw-r--r--   0 runner    (1001) docker     (123)    33577 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ec2/resources/instance_type_offerings/region/ap-southeast-2.json
+-rw-r--r--   0 runner    (1001) docker     (123)     9903 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ec2/resources/instance_type_offerings/region/ap-southeast-3.json
+-rw-r--r--   0 runner    (1001) docker     (123)    23616 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ec2/resources/instance_type_offerings/region/ca-central-1.json
+-rw-r--r--   0 runner    (1001) docker     (123)    35491 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ec2/resources/instance_type_offerings/region/eu-central-1.json
+-rw-r--r--   0 runner    (1001) docker     (123)     7879 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ec2/resources/instance_type_offerings/region/eu-central-2.json
+-rw-r--r--   0 runner    (1001) docker     (123)    16599 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ec2/resources/instance_type_offerings/region/eu-north-1.json
+-rw-r--r--   0 runner    (1001) docker     (123)    16182 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ec2/resources/instance_type_offerings/region/eu-south-1.json
+-rw-r--r--   0 runner    (1001) docker     (123)     7830 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ec2/resources/instance_type_offerings/region/eu-south-2.json
+-rw-r--r--   0 runner    (1001) docker     (123)    40817 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ec2/resources/instance_type_offerings/region/eu-west-1.json
+-rw-r--r--   0 runner    (1001) docker     (123)    24748 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ec2/resources/instance_type_offerings/region/eu-west-2.json
+-rw-r--r--   0 runner    (1001) docker     (123)    19711 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ec2/resources/instance_type_offerings/region/eu-west-3.json
+-rw-r--r--   0 runner    (1001) docker     (123)     8066 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ec2/resources/instance_type_offerings/region/me-central-1.json
+-rw-r--r--   0 runner    (1001) docker     (123)    11132 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ec2/resources/instance_type_offerings/region/me-south-1.json
+-rw-r--r--   0 runner    (1001) docker     (123)    24067 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ec2/resources/instance_type_offerings/region/sa-east-1.json
+-rw-r--r--   0 runner    (1001) docker     (123)    41549 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ec2/resources/instance_type_offerings/region/us-east-1.json
+-rw-r--r--   0 runner    (1001) docker     (123)    37729 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ec2/resources/instance_type_offerings/region/us-east-2.json
+-rw-r--r--   0 runner    (1001) docker     (123)    24028 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ec2/resources/instance_type_offerings/region/us-west-1.json
+-rw-r--r--   0 runner    (1001) docker     (123)    41477 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ec2/resources/instance_type_offerings/region/us-west-2.json
+-rw-r--r--   0 runner    (1001) docker     (123)  1293813 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ec2/resources/instance_types.json
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.312199 moto-4.1.7.dev9/moto/ec2/resources/latest_amis/
+-rw-r--r--   0 runner    (1001) docker     (123)     9548 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ec2/resources/latest_amis/af-south-1.json
+-rw-r--r--   0 runner    (1001) docker     (123)     9548 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ec2/resources/latest_amis/ap-east-1.json
+-rw-r--r--   0 runner    (1001) docker     (123)    10558 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ec2/resources/latest_amis/ap-northeast-1.json
+-rw-r--r--   0 runner    (1001) docker     (123)     9548 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ec2/resources/latest_amis/ap-northeast-2.json
+-rw-r--r--   0 runner    (1001) docker     (123)     9548 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ec2/resources/latest_amis/ap-northeast-3.json
+-rw-r--r--   0 runner    (1001) docker     (123)     9548 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ec2/resources/latest_amis/ap-south-1.json
+-rw-r--r--   0 runner    (1001) docker     (123)     7506 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ec2/resources/latest_amis/ap-south-2.json
+-rw-r--r--   0 runner    (1001) docker     (123)    10558 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ec2/resources/latest_amis/ap-southeast-1.json
+-rw-r--r--   0 runner    (1001) docker     (123)    10558 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ec2/resources/latest_amis/ap-southeast-2.json
+-rw-r--r--   0 runner    (1001) docker     (123)     9548 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ec2/resources/latest_amis/ap-southeast-3.json
+-rw-r--r--   0 runner    (1001) docker     (123)     9548 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ec2/resources/latest_amis/ca-central-1.json
+-rw-r--r--   0 runner    (1001) docker     (123)    10558 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ec2/resources/latest_amis/eu-central-1.json
+-rw-r--r--   0 runner    (1001) docker     (123)     7506 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ec2/resources/latest_amis/eu-central-2.json
+-rw-r--r--   0 runner    (1001) docker     (123)     9548 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ec2/resources/latest_amis/eu-north-1.json
+-rw-r--r--   0 runner    (1001) docker     (123)     9548 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ec2/resources/latest_amis/eu-south-1.json
+-rw-r--r--   0 runner    (1001) docker     (123)     7506 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ec2/resources/latest_amis/eu-south-2.json
+-rw-r--r--   0 runner    (1001) docker     (123)    10558 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ec2/resources/latest_amis/eu-west-1.json
+-rw-r--r--   0 runner    (1001) docker     (123)     9548 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ec2/resources/latest_amis/eu-west-2.json
+-rw-r--r--   0 runner    (1001) docker     (123)     9548 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ec2/resources/latest_amis/eu-west-3.json
+-rw-r--r--   0 runner    (1001) docker     (123)     9548 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ec2/resources/latest_amis/me-central-1.json
+-rw-r--r--   0 runner    (1001) docker     (123)     9548 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ec2/resources/latest_amis/me-south-1.json
+-rw-r--r--   0 runner    (1001) docker     (123)    10558 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ec2/resources/latest_amis/sa-east-1.json
+-rw-r--r--   0 runner    (1001) docker     (123)    10558 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ec2/resources/latest_amis/us-east-1.json
+-rw-r--r--   0 runner    (1001) docker     (123)     9548 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ec2/resources/latest_amis/us-east-2.json
+-rw-r--r--   0 runner    (1001) docker     (123)    10558 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ec2/resources/latest_amis/us-west-1.json
+-rw-r--r--   0 runner    (1001) docker     (123)    10558 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ec2/resources/latest_amis/us-west-2.json
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.324199 moto-4.1.7.dev9/moto/ec2/responses/
+-rw-r--r--   0 runner    (1001) docker     (123)     2781 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ec2/responses/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1247 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ec2/responses/_base_response.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1864 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ec2/responses/account_attributes.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8121 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ec2/responses/amis.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1850 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ec2/responses/availability_zones_and_regions.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3694 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ec2/responses/carrier_gateways.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3372 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ec2/responses/customer_gateways.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4986 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ec2/responses/dhcp_options.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3494 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ec2/responses/egress_only_internet_gateways.py
+-rw-r--r--   0 runner    (1001) docker     (123)    19278 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ec2/responses/elastic_block_store.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7313 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ec2/responses/elastic_ip_addresses.py
+-rw-r--r--   0 runner    (1001) docker     (123)    18139 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ec2/responses/elastic_network_interfaces.py
+-rw-r--r--   0 runner    (1001) docker     (123)    24972 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ec2/responses/fleets.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4840 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ec2/responses/flow_logs.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1490 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ec2/responses/general.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4593 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ec2/responses/hosts.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4394 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ec2/responses/iam_instance_profiles.py
+-rw-r--r--   0 runner    (1001) docker     (123)    40932 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ec2/responses/instances.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4373 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ec2/responses/internet_gateways.py
+-rw-r--r--   0 runner    (1001) docker     (123)      493 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ec2/responses/ip_addresses.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2646 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ec2/responses/key_pairs.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9129 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ec2/responses/launch_templates.py
+-rw-r--r--   0 runner    (1001) docker     (123)      428 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ec2/responses/monitoring.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5213 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ec2/responses/nat_gateways.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7903 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ec2/responses/network_acls.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1341 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ec2/responses/reserved_instances.py
+-rw-r--r--   0 runner    (1001) docker     (123)    14035 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ec2/responses/route_tables.py
+-rw-r--r--   0 runner    (1001) docker     (123)    26457 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ec2/responses/security_groups.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2106 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ec2/responses/settings.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8310 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ec2/responses/spot_fleets.py
+-rw-r--r--   0 runner    (1001) docker     (123)    11251 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ec2/responses/spot_instances.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9288 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ec2/responses/subnets.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2065 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ec2/responses/tags.py
+-rw-r--r--   0 runner    (1001) docker     (123)    24840 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ec2/responses/transit_gateway_attachments.py
+-rw-r--r--   0 runner    (1001) docker     (123)    13988 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ec2/responses/transit_gateway_route_tables.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9214 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ec2/responses/transit_gateways.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4910 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ec2/responses/virtual_private_gateways.py
+-rw-r--r--   0 runner    (1001) docker     (123)    11252 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ec2/responses/vpc_peering_connections.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8827 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ec2/responses/vpc_service_configuration.py
+-rw-r--r--   0 runner    (1001) docker     (123)    39221 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ec2/responses/vpcs.py
+-rw-r--r--   0 runner    (1001) docker     (123)    10018 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ec2/responses/vpn_connections.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1308 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ec2/responses/windows.py
+-rw-r--r--   0 runner    (1001) docker     (123)      140 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ec2/urls.py
+-rw-r--r--   0 runner    (1001) docker     (123)    28837 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ec2/utils.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.324199 moto-4.1.7.dev9/moto/ec2instanceconnect/
+-rw-r--r--   0 runner    (1001) docker     (123)      160 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ec2instanceconnect/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      346 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ec2instanceconnect/models.py
+-rw-r--r--   0 runner    (1001) docker     (123)      539 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ec2instanceconnect/responses.py
+-rw-r--r--   0 runner    (1001) docker     (123)      180 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ec2instanceconnect/urls.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.324199 moto-4.1.7.dev9/moto/ecr/
+-rw-r--r--   0 runner    (1001) docker     (123)      155 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ecr/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4096 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ecr/exceptions.py
+-rw-r--r--   0 runner    (1001) docker     (123)    39758 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ecr/models.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8913 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ecr/policy_validation.py
+-rw-r--r--   0 runner    (1001) docker     (123)    11127 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ecr/responses.py
+-rw-r--r--   0 runner    (1001) docker     (123)      188 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ecr/urls.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.324199 moto-4.1.7.dev9/moto/ecs/
+-rw-r--r--   0 runner    (1001) docker     (123)      155 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ecs/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1814 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ecs/exceptions.py
+-rw-r--r--   0 runner    (1001) docker     (123)    86426 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ecs/models.py
+-rw-r--r--   0 runner    (1001) docker     (123)    22481 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ecs/responses.py
+-rw-r--r--   0 runner    (1001) docker     (123)      165 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ecs/urls.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.328199 moto-4.1.7.dev9/moto/efs/
+-rw-r--r--   0 runner    (1001) docker     (123)      155 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/efs/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2180 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/efs/exceptions.py
+-rw-r--r--   0 runner    (1001) docker     (123)    26760 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/efs/models.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8303 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/efs/responses.py
+-rw-r--r--   0 runner    (1001) docker     (123)      927 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/efs/urls.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.328199 moto-4.1.7.dev9/moto/eks/
+-rw-r--r--   0 runner    (1001) docker     (123)      171 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/eks/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      942 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/eks/exceptions.py
+-rw-r--r--   0 runner    (1001) docker     (123)    30391 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/eks/models.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8680 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/eks/responses.py
+-rw-r--r--   0 runner    (1001) docker     (123)      624 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/eks/urls.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1582 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/eks/utils.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.328199 moto-4.1.7.dev9/moto/elasticache/
+-rw-r--r--   0 runner    (1001) docker     (123)      139 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/elasticache/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1592 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/elasticache/exceptions.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2935 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/elasticache/models.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4087 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/elasticache/responses.py
+-rw-r--r--   0 runner    (1001) docker     (123)      209 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/elasticache/urls.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.332199 moto-4.1.7.dev9/moto/elasticbeanstalk/
+-rw-r--r--   0 runner    (1001) docker     (123)      129 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/elasticbeanstalk/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      334 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/elasticbeanstalk/exceptions.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5079 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/elasticbeanstalk/models.py
+-rw-r--r--   0 runner    (1001) docker     (123)    57275 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/elasticbeanstalk/responses.py
+-rw-r--r--   0 runner    (1001) docker     (123)      180 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/elasticbeanstalk/urls.py
+-rw-r--r--   0 runner    (1001) docker     (123)      393 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/elasticbeanstalk/utils.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.332199 moto-4.1.7.dev9/moto/elastictranscoder/
+-rw-r--r--   0 runner    (1001) docker     (123)      157 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/elastictranscoder/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3919 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/elastictranscoder/models.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5079 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/elastictranscoder/responses.py
+-rw-r--r--   0 runner    (1001) docker     (123)      350 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/elastictranscoder/urls.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.332199 moto-4.1.7.dev9/moto/elb/
+-rw-r--r--   0 runner    (1001) docker     (123)      155 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/elb/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2703 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/elb/exceptions.py
+-rw-r--r--   0 runner    (1001) docker     (123)    25335 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/elb/models.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1008 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/elb/policies.py
+-rw-r--r--   0 runner    (1001) docker     (123)    37722 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/elb/responses.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1336 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/elb/urls.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.336200 moto-4.1.7.dev9/moto/elbv2/
+-rw-r--r--   0 runner    (1001) docker     (123)      163 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/elbv2/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5578 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/elbv2/exceptions.py
+-rw-r--r--   0 runner    (1001) docker     (123)    69704 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/elbv2/models.py
+-rw-r--r--   0 runner    (1001) docker     (123)    68565 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/elbv2/responses.py
+-rw-r--r--   0 runner    (1001) docker     (123)      164 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/elbv2/urls.py
+-rw-r--r--   0 runner    (1001) docker     (123)      388 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/elbv2/utils.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.336200 moto-4.1.7.dev9/moto/emr/
+-rw-r--r--   0 runner    (1001) docker     (123)      155 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/emr/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      484 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/emr/exceptions.py
+-rw-r--r--   0 runner    (1001) docker     (123)    28079 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/emr/models.py
+-rw-r--r--   0 runner    (1001) docker     (123)    65244 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/emr/responses.py
+-rw-r--r--   0 runner    (1001) docker     (123)      233 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/emr/urls.py
+-rw-r--r--   0 runner    (1001) docker     (123)    16001 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/emr/utils.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.336200 moto-4.1.7.dev9/moto/emrcontainers/
+-rw-r--r--   0 runner    (1001) docker     (123)      240 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/emrcontainers/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      270 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/emrcontainers/exceptions.py
+-rw-r--r--   0 runner    (1001) docker     (123)    13384 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/emrcontainers/models.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5584 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/emrcontainers/responses.py
+-rw-r--r--   0 runner    (1001) docker     (123)      533 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/emrcontainers/urls.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1651 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/emrcontainers/utils.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.340200 moto-4.1.7.dev9/moto/emrserverless/
+-rw-r--r--   0 runner    (1001) docker     (123)      268 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/emrserverless/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      479 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/emrserverless/exceptions.py
+-rw-r--r--   0 runner    (1001) docker     (123)    10304 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/emrserverless/models.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4886 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/emrserverless/responses.py
+-rw-r--r--   0 runner    (1001) docker     (123)      687 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/emrserverless/urls.py
+-rw-r--r--   0 runner    (1001) docker     (123)      600 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/emrserverless/utils.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.340200 moto-4.1.7.dev9/moto/es/
+-rw-r--r--   0 runner    (1001) docker     (123)      175 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/es/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      858 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/es/exceptions.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5931 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/es/models.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4601 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/es/responses.py
+-rw-r--r--   0 runner    (1001) docker     (123)      931 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/es/urls.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.344200 moto-4.1.7.dev9/moto/events/
+-rw-r--r--   0 runner    (1001) docker     (123)      170 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/events/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1024 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/events/exceptions.py
+-rw-r--r--   0 runner    (1001) docker     (123)    66807 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/events/models.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2247 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/events/notifications.py
+-rw-r--r--   0 runner    (1001) docker     (123)    18552 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/events/responses.py
+-rw-r--r--   0 runner    (1001) docker     (123)      139 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/events/urls.py
+-rw-r--r--   0 runner    (1001) docker     (123)      434 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/events/utils.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.344200 moto-4.1.7.dev9/moto/firehose/
+-rw-r--r--   0 runner    (1001) docker     (123)      199 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/firehose/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1486 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/firehose/exceptions.py
+-rw-r--r--   0 runner    (1001) docker     (123)    29565 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/firehose/models.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5319 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/firehose/responses.py
+-rw-r--r--   0 runner    (1001) docker     (123)      182 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/firehose/urls.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.344200 moto-4.1.7.dev9/moto/forecast/
+-rw-r--r--   0 runner    (1001) docker     (123)      180 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/forecast/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      524 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/forecast/exceptions.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5915 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/forecast/models.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2987 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/forecast/responses.py
+-rw-r--r--   0 runner    (1001) docker     (123)      148 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/forecast/urls.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.344200 moto-4.1.7.dev9/moto/glacier/
+-rw-r--r--   0 runner    (1001) docker     (123)      175 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/glacier/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8181 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/glacier/models.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7306 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/glacier/responses.py
+-rw-r--r--   0 runner    (1001) docker     (123)      885 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/glacier/urls.py
+-rw-r--r--   0 runner    (1001) docker     (123)      293 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/glacier/utils.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.348200 moto-4.1.7.dev9/moto/glue/
+-rw-r--r--   0 runner    (1001) docker     (123)      118 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/glue/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9638 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/glue/exceptions.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1439 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/glue/glue_schema_registry_constants.py
+-rw-r--r--   0 runner    (1001) docker     (123)    15009 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/glue/glue_schema_registry_utils.py
+-rw-r--r--   0 runner    (1001) docker     (123)    52028 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/glue/models.py
+-rw-r--r--   0 runner    (1001) docker     (123)    21842 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/glue/responses.py
+-rw-r--r--   0 runner    (1001) docker     (123)      136 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/glue/urls.py
+-rw-r--r--   0 runner    (1001) docker     (123)    12557 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/glue/utils.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.348200 moto-4.1.7.dev9/moto/greengrass/
+-rw-r--r--   0 runner    (1001) docker     (123)      136 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/greengrass/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1146 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/greengrass/exceptions.py
+-rw-r--r--   0 runner    (1001) docker     (123)    54499 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/greengrass/models.py
+-rw-r--r--   0 runner    (1001) docker     (123)    30895 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/greengrass/responses.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3051 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/greengrass/urls.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.352200 moto-4.1.7.dev9/moto/guardduty/
+-rw-r--r--   0 runner    (1001) docker     (123)      185 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/guardduty/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1039 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/guardduty/exceptions.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7861 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/guardduty/models.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5980 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/guardduty/responses.py
+-rw-r--r--   0 runner    (1001) docker     (123)      553 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/guardduty/urls.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.356201 moto-4.1.7.dev9/moto/iam/
+-rw-r--r--   0 runner    (1001) docker     (123)      115 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/iam/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    16725 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/iam/access_control.py
+-rw-r--r--   0 runner    (1001) docker     (123)  1599363 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/iam/aws_managed_policies.py
+-rw-r--r--   0 runner    (1001) docker     (123)    14247 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/iam/config.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3532 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/iam/exceptions.py
+-rw-r--r--   0 runner    (1001) docker     (123)   118562 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/iam/models.py
+-rw-r--r--   0 runner    (1001) docker     (123)    22588 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/iam/policy_validation.py
+-rw-r--r--   0 runner    (1001) docker     (123)   107097 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/iam/responses.py
+-rw-r--r--   0 runner    (1001) docker     (123)      134 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/iam/urls.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2250 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/iam/utils.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.356201 moto-4.1.7.dev9/moto/identitystore/
+-rw-r--r--   0 runner    (1001) docker     (123)      219 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/identitystore/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)       54 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/identitystore/exceptions.py
+-rw-r--r--   0 runner    (1001) docker     (123)      908 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/identitystore/models.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1117 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/identitystore/responses.py
+-rw-r--r--   0 runner    (1001) docker     (123)      216 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/identitystore/urls.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.356201 moto-4.1.7.dev9/moto/instance_metadata/
+-rw-r--r--   0 runner    (1001) docker     (123)       55 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/instance_metadata/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      266 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/instance_metadata/models.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1767 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/instance_metadata/responses.py
+-rw-r--r--   0 runner    (1001) docker     (123)      207 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/instance_metadata/urls.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.360201 moto-4.1.7.dev9/moto/iot/
+-rw-r--r--   0 runner    (1001) docker     (123)      115 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/iot/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2545 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/iot/exceptions.py
+-rw-r--r--   0 runner    (1001) docker     (123)    70619 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/iot/models.py
+-rw-r--r--   0 runner    (1001) docker     (123)    32365 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/iot/responses.py
+-rw-r--r--   0 runner    (1001) docker     (123)      742 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/iot/urls.py
+-rw-r--r--   0 runner    (1001) docker     (123)      208 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/iot/utils.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.360201 moto-4.1.7.dev9/moto/iotdata/
+-rw-r--r--   0 runner    (1001) docker     (123)      127 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/iotdata/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      693 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/iotdata/exceptions.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7563 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/iotdata/models.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1797 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/iotdata/responses.py
+-rw-r--r--   0 runner    (1001) docker     (123)      373 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/iotdata/urls.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.360201 moto-4.1.7.dev9/moto/kinesis/
+-rw-r--r--   0 runner    (1001) docker     (123)      175 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/kinesis/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3818 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/kinesis/exceptions.py
+-rw-r--r--   0 runner    (1001) docker     (123)    35988 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/kinesis/models.py
+-rw-r--r--   0 runner    (1001) docker     (123)    12283 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/kinesis/responses.py
+-rw-r--r--   0 runner    (1001) docker     (123)      566 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/kinesis/urls.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1922 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/kinesis/utils.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.364201 moto-4.1.7.dev9/moto/kinesisvideo/
+-rw-r--r--   0 runner    (1001) docker     (123)      200 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/kinesisvideo/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      538 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/kinesisvideo/exceptions.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4313 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/kinesisvideo/models.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2221 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/kinesisvideo/responses.py
+-rw-r--r--   0 runner    (1001) docker     (123)      390 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/kinesisvideo/urls.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.364201 moto-4.1.7.dev9/moto/kinesisvideoarchivedmedia/
+-rw-r--r--   0 runner    (1001) docker     (123)      265 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/kinesisvideoarchivedmedia/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)       37 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/kinesisvideoarchivedmedia/exceptions.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2018 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/kinesisvideoarchivedmedia/models.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1812 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/kinesisvideoarchivedmedia/responses.py
+-rw-r--r--   0 runner    (1001) docker     (123)      230 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/kinesisvideoarchivedmedia/urls.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.364201 moto-4.1.7.dev9/moto/kms/
+-rw-r--r--   0 runner    (1001) docker     (123)      155 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/kms/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1182 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/kms/exceptions.py
+-rw-r--r--   0 runner    (1001) docker     (123)    24509 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/kms/models.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1735 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/kms/policy_validator.py
+-rw-r--r--   0 runner    (1001) docker     (123)    25988 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/kms/responses.py
+-rw-r--r--   0 runner    (1001) docker     (123)      133 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/kms/urls.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7658 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/kms/utils.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.368201 moto-4.1.7.dev9/moto/logs/
+-rw-r--r--   0 runner    (1001) docker     (123)      118 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/logs/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1340 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/logs/exceptions.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2742 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/logs/metric_filters.py
+-rw-r--r--   0 runner    (1001) docker     (123)    36704 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/logs/models.py
+-rw-r--r--   0 runner    (1001) docker     (123)    14217 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/logs/responses.py
+-rw-r--r--   0 runner    (1001) docker     (123)      136 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/logs/urls.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1899 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/logs/utils.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.368201 moto-4.1.7.dev9/moto/managedblockchain/
+-rw-r--r--   0 runner    (1001) docker     (123)      225 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/managedblockchain/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3110 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/managedblockchain/exceptions.py
+-rw-r--r--   0 runner    (1001) docker     (123)    37565 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/managedblockchain/models.py
+-rw-r--r--   0 runner    (1001) docker     (123)    16840 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/managedblockchain/responses.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1732 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/managedblockchain/urls.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4185 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/managedblockchain/utils.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.368201 moto-4.1.7.dev9/moto/mediaconnect/
+-rw-r--r--   0 runner    (1001) docker     (123)      200 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/mediaconnect/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      193 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/mediaconnect/exceptions.py
+-rw-r--r--   0 runner    (1001) docker     (123)    15029 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/mediaconnect/models.py
+-rw-r--r--   0 runner    (1001) docker     (123)    10367 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/mediaconnect/responses.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1121 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/mediaconnect/urls.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.372201 moto-4.1.7.dev9/moto/medialive/
+-rw-r--r--   0 runner    (1001) docker     (123)      133 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/medialive/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/medialive/exceptions.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9868 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/medialive/models.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6064 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/medialive/responses.py
+-rw-r--r--   0 runner    (1001) docker     (123)      520 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/medialive/urls.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.372201 moto-4.1.7.dev9/moto/mediapackage/
+-rw-r--r--   0 runner    (1001) docker     (123)      200 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/mediapackage/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      325 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/mediapackage/exceptions.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7327 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/mediapackage/models.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4680 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/mediapackage/responses.py
+-rw-r--r--   0 runner    (1001) docker     (123)      379 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/mediapackage/urls.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.372201 moto-4.1.7.dev9/moto/mediastore/
+-rw-r--r--   0 runner    (1001) docker     (123)      190 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/mediastore/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      872 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/mediastore/exceptions.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4267 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/mediastore/models.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3214 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/mediastore/responses.py
+-rw-r--r--   0 runner    (1001) docker     (123)      221 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/mediastore/urls.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.372201 moto-4.1.7.dev9/moto/mediastoredata/
+-rw-r--r--   0 runner    (1001) docker     (123)      210 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/mediastoredata/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      329 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/mediastoredata/exceptions.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2265 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/mediastoredata/models.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1118 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/mediastoredata/responses.py
+-rw-r--r--   0 runner    (1001) docker     (123)      241 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/mediastoredata/urls.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.376201 moto-4.1.7.dev9/moto/meteringmarketplace/
+-rw-r--r--   0 runner    (1001) docker     (123)      235 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/meteringmarketplace/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1250 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/meteringmarketplace/exceptions.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4374 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/meteringmarketplace/models.py
+-rw-r--r--   0 runner    (1001) docker     (123)      661 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/meteringmarketplace/responses.py
+-rw-r--r--   0 runner    (1001) docker     (123)      236 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/meteringmarketplace/urls.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.376201 moto-4.1.7.dev9/moto/moto_api/
+-rw-r--r--   0 runner    (1001) docker     (123)      367 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/moto_api/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.376201 moto-4.1.7.dev9/moto/moto_api/_internal/
+-rw-r--r--   0 runner    (1001) docker     (123)      339 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/moto_api/_internal/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2590 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/moto_api/_internal/managed_state_model.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1660 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/moto_api/_internal/models.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1032 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/moto_api/_internal/moto_random.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.376201 moto-4.1.7.dev9/moto/moto_api/_internal/recorder/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/moto_api/_internal/recorder/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4950 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/moto_api/_internal/recorder/models.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1606 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/moto_api/_internal/recorder/responses.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5960 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/moto_api/_internal/responses.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2046 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/moto_api/_internal/state_manager.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1347 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/moto_api/_internal/urls.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.380201 moto-4.1.7.dev9/moto/moto_server/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.380201 moto-4.1.7.dev9/moto/moto_server/templates/
+-rw-r--r--   0 runner    (1001) docker     (123)     5985 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/moto_server/templates/dashboard.html
+-rw-r--r--   0 runner    (1001) docker     (123)     1188 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/moto_server/threaded_moto_server.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1071 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/moto_server/utilities.py
+-rw-r--r--   0 runner    (1001) docker     (123)    11718 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/moto_server/werkzeug_app.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.380201 moto-4.1.7.dev9/moto/mq/
+-rw-r--r--   0 runner    (1001) docker     (123)      175 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/mq/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8368 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/mq/configuration.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2410 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/mq/exceptions.py
+-rw-r--r--   0 runner    (1001) docker     (123)    17887 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/mq/models.py
+-rw-r--r--   0 runner    (1001) docker     (123)    10554 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/mq/responses.py
+-rw-r--r--   0 runner    (1001) docker     (123)      793 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/mq/urls.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.380201 moto-4.1.7.dev9/moto/neptune/
+-rw-r--r--   0 runner    (1001) docker     (123)      493 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/neptune/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      848 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/neptune/exceptions.py
+-rw-r--r--   0 runner    (1001) docker     (123)    16523 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/neptune/models.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7895 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/neptune/responses.py
+-rw-r--r--   0 runner    (1001) docker     (123)      151 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/neptune/urls.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.380201 moto-4.1.7.dev9/moto/opensearch/
+-rw-r--r--   0 runner    (1001) docker     (123)      207 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/opensearch/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4473 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/opensearch/data.py
+-rw-r--r--   0 runner    (1001) docker     (123)      266 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/opensearch/exceptions.py
+-rw-r--r--   0 runner    (1001) docker     (123)    13390 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/opensearch/models.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6592 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/opensearch/responses.py
+-rw-r--r--   0 runner    (1001) docker     (123)      223 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/opensearch/urls.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.384201 moto-4.1.7.dev9/moto/opsworks/
+-rw-r--r--   0 runner    (1001) docker     (123)      180 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/opsworks/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      371 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/opsworks/exceptions.py
+-rw-r--r--   0 runner    (1001) docker     (123)    24826 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/opsworks/models.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6762 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/opsworks/responses.py
+-rw-r--r--   0 runner    (1001) docker     (123)      259 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/opsworks/urls.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.384201 moto-4.1.7.dev9/moto/organizations/
+-rw-r--r--   0 runner    (1001) docker     (123)      145 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/organizations/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2748 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/organizations/exceptions.py
+-rw-r--r--   0 runner    (1001) docker     (123)    34112 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/organizations/models.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8160 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/organizations/responses.py
+-rw-r--r--   0 runner    (1001) docker     (123)      163 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/organizations/urls.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4009 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/organizations/utils.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.384201 moto-4.1.7.dev9/moto/packages/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/packages/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.384201 moto-4.1.7.dev9/moto/packages/boto/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/packages/boto/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.384201 moto-4.1.7.dev9/moto/packages/boto/ec2/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/packages/boto/ec2/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3336 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/packages/boto/ec2/blockdevicemapping.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1932 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/packages/boto/ec2/ec2object.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1187 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/packages/boto/ec2/image.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7305 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/packages/boto/ec2/instance.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1941 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/packages/boto/ec2/instancetype.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1605 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/packages/boto/ec2/tag.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.388202 moto-4.1.7.dev9/moto/packages/cfnresponse/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/packages/cfnresponse/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1506 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/packages/cfnresponse/cfnresponse.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.388202 moto-4.1.7.dev9/moto/personalize/
+-rw-r--r--   0 runner    (1001) docker     (123)      211 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/personalize/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      354 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/personalize/exceptions.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1951 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/personalize/models.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1600 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/personalize/responses.py
+-rw-r--r--   0 runner    (1001) docker     (123)      209 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/personalize/urls.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.388202 moto-4.1.7.dev9/moto/pinpoint/
+-rw-r--r--   0 runner    (1001) docker     (123)      199 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/pinpoint/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      465 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/pinpoint/exceptions.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4727 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/pinpoint/models.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5580 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/pinpoint/responses.py
+-rw-r--r--   0 runner    (1001) docker     (123)      554 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/pinpoint/urls.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.392202 moto-4.1.7.dev9/moto/polly/
+-rw-r--r--   0 runner    (1001) docker     (123)      165 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/polly/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3282 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/polly/models.py
+-rw-r--r--   0 runner    (1001) docker     (123)    16652 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/polly/resources.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6956 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/polly/responses.py
+-rw-r--r--   0 runner    (1001) docker     (123)      311 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/polly/urls.py
+-rw-r--r--   0 runner    (1001) docker     (123)      127 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/polly/utils.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.392202 moto-4.1.7.dev9/moto/quicksight/
+-rw-r--r--   0 runner    (1001) docker     (123)      207 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/quicksight/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      236 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/quicksight/exceptions.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7745 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/quicksight/models.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7829 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/quicksight/responses.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1186 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/quicksight/urls.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.392202 moto-4.1.7.dev9/moto/ram/
+-rw-r--r--   0 runner    (1001) docker     (123)      155 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ram/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      933 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ram/exceptions.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8007 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ram/models.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1210 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ram/responses.py
+-rw-r--r--   0 runner    (1001) docker     (123)      495 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ram/urls.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.396202 moto-4.1.7.dev9/moto/rds/
+-rw-r--r--   0 runner    (1001) docker     (123)      155 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/rds/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5788 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/rds/exceptions.py
+-rw-r--r--   0 runner    (1001) docker     (123)   161415 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/rds/models.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.184194 moto-4.1.7.dev9/moto/rds/resources/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.396202 moto-4.1.7.dev9/moto/rds/resources/cluster_options/
+-rw-r--r--   0 runner    (1001) docker     (123)   133645 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/rds/resources/cluster_options/neptune.json
+-rw-r--r--   0 runner    (1001) docker     (123)    57063 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/rds/responses.py
+-rw-r--r--   0 runner    (1001) docker     (123)      166 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/rds/urls.py
+-rw-r--r--   0 runner    (1001) docker     (123)    11479 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/rds/utils.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.396202 moto-4.1.7.dev9/moto/redshift/
+-rw-r--r--   0 runner    (1001) docker     (123)      130 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/redshift/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5210 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/redshift/exceptions.py
+-rw-r--r--   0 runner    (1001) docker     (123)    39885 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/redshift/models.py
+-rw-r--r--   0 runner    (1001) docker     (123)    29120 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/redshift/responses.py
+-rw-r--r--   0 runner    (1001) docker     (123)      148 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/redshift/urls.py
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/redshift/utils.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.400202 moto-4.1.7.dev9/moto/redshiftdata/
+-rw-r--r--   0 runner    (1001) docker     (123)      142 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/redshiftdata/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      334 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/redshiftdata/exceptions.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7211 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/redshiftdata/models.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2150 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/redshiftdata/responses.py
+-rw-r--r--   0 runner    (1001) docker     (123)      196 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/redshiftdata/urls.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.400202 moto-4.1.7.dev9/moto/rekognition/
+-rw-r--r--   0 runner    (1001) docker     (123)      211 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/rekognition/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)       52 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/rekognition/exceptions.py
+-rw-r--r--   0 runner    (1001) docker     (123)    13288 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/rekognition/models.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2281 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/rekognition/responses.py
+-rw-r--r--   0 runner    (1001) docker     (123)      208 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/rekognition/urls.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.400202 moto-4.1.7.dev9/moto/resourcegroups/
+-rw-r--r--   0 runner    (1001) docker     (123)      210 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/resourcegroups/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      226 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/resourcegroups/exceptions.py
+-rw-r--r--   0 runner    (1001) docker     (123)    13344 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/resourcegroups/models.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6386 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/resourcegroups/responses.py
+-rw-r--r--   0 runner    (1001) docker     (123)      934 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/resourcegroups/urls.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.400202 moto-4.1.7.dev9/moto/resourcegroupstaggingapi/
+-rw-r--r--   0 runner    (1001) docker     (123)      260 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/resourcegroupstaggingapi/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    27328 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/resourcegroupstaggingapi/models.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3483 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/resourcegroupstaggingapi/responses.py
+-rw-r--r--   0 runner    (1001) docker     (123)      178 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/resourcegroupstaggingapi/urls.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.404202 moto-4.1.7.dev9/moto/route53/
+-rw-r--r--   0 runner    (1001) docker     (123)      127 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/route53/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5404 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/route53/exceptions.py
+-rw-r--r--   0 runner    (1001) docker     (123)    34262 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/route53/models.py
+-rw-r--r--   0 runner    (1001) docker     (123)    34372 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/route53/responses.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2533 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/route53/urls.py
+-rw-r--r--   0 runner    (1001) docker     (123)      364 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/route53/utils.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.404202 moto-4.1.7.dev9/moto/route53resolver/
+-rw-r--r--   0 runner    (1001) docker     (123)      227 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/route53resolver/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2793 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/route53resolver/exceptions.py
+-rw-r--r--   0 runner    (1001) docker     (123)    35274 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/route53resolver/models.py
+-rw-r--r--   0 runner    (1001) docker     (123)    11715 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/route53resolver/responses.py
+-rw-r--r--   0 runner    (1001) docker     (123)      225 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/route53resolver/urls.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1150 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/route53resolver/utils.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4911 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/route53resolver/validations.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.408203 moto-4.1.7.dev9/moto/s3/
+-rw-r--r--   0 runner    (1001) docker     (123)      112 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/s3/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1259 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/s3/cloud_formation.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4469 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/s3/config.py
+-rw-r--r--   0 runner    (1001) docker     (123)    16719 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/s3/exceptions.py
+-rw-r--r--   0 runner    (1001) docker     (123)    82916 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/s3/models.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3767 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/s3/notifications.py
+-rw-r--r--   0 runner    (1001) docker     (123)   115846 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/s3/responses.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1871 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/s3/select_object_content.py
+-rw-r--r--   0 runner    (1001) docker     (123)      871 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/s3/urls.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6538 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/s3/utils.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.408203 moto-4.1.7.dev9/moto/s3bucket_path/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/s3bucket_path/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      301 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/s3bucket_path/utils.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.408203 moto-4.1.7.dev9/moto/s3control/
+-rw-r--r--   0 runner    (1001) docker     (123)      203 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/s3control/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4922 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/s3control/config.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1376 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/s3control/exceptions.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4813 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/s3control/models.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9040 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/s3control/responses.py
+-rw-r--r--   0 runner    (1001) docker     (123)      607 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/s3control/urls.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.412202 moto-4.1.7.dev9/moto/sagemaker/
+-rw-r--r--   0 runner    (1001) docker     (123)      185 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/sagemaker/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1209 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/sagemaker/exceptions.py
+-rw-r--r--   0 runner    (1001) docker     (123)    91754 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/sagemaker/models.py
+-rw-r--r--   0 runner    (1001) docker     (123)    28604 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/sagemaker/responses.py
+-rw-r--r--   0 runner    (1001) docker     (123)      169 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/sagemaker/urls.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1493 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/sagemaker/utils.py
+-rw-r--r--   0 runner    (1001) docker     (123)      538 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/sagemaker/validators.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.412202 moto-4.1.7.dev9/moto/sdb/
+-rw-r--r--   0 runner    (1001) docker     (123)      179 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/sdb/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1247 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/sdb/exceptions.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3310 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/sdb/models.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3383 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/sdb/responses.py
+-rw-r--r--   0 runner    (1001) docker     (123)      150 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/sdb/urls.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.412202 moto-4.1.7.dev9/moto/secretsmanager/
+-rw-r--r--   0 runner    (1001) docker     (123)      210 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/secretsmanager/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1929 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/secretsmanager/exceptions.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.412202 moto-4.1.7.dev9/moto/secretsmanager/list_secrets/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/secretsmanager/list_secrets/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1169 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/secretsmanager/list_secrets/filters.py
+-rw-r--r--   0 runner    (1001) docker     (123)    30397 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/secretsmanager/models.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8758 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/secretsmanager/responses.py
+-rw-r--r--   0 runner    (1001) docker     (123)      166 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/secretsmanager/urls.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3483 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/secretsmanager/utils.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2749 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/server.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.416203 moto-4.1.7.dev9/moto/servicediscovery/
+-rw-r--r--   0 runner    (1001) docker     (123)      231 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/servicediscovery/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      623 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/servicediscovery/exceptions.py
+-rw-r--r--   0 runner    (1001) docker     (123)    10956 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/servicediscovery/models.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6515 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/servicediscovery/responses.py
+-rw-r--r--   0 runner    (1001) docker     (123)      229 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/servicediscovery/urls.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.416203 moto-4.1.7.dev9/moto/servicequotas/
+-rw-r--r--   0 runner    (1001) docker     (123)      219 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/servicequotas/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      365 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/servicequotas/exceptions.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1149 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/servicequotas/models.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.416203 moto-4.1.7.dev9/moto/servicequotas/resources/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/servicequotas/resources/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.416203 moto-4.1.7.dev9/moto/servicequotas/resources/default_quotas/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/servicequotas/resources/default_quotas/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9458 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/servicequotas/resources/default_quotas/vpc.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1231 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/servicequotas/responses.py
+-rw-r--r--   0 runner    (1001) docker     (123)      217 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/servicequotas/urls.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.420203 moto-4.1.7.dev9/moto/ses/
+-rw-r--r--   0 runner    (1001) docker     (123)      115 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ses/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2283 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ses/exceptions.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2424 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ses/feedback.py
+-rw-r--r--   0 runner    (1001) docker     (123)    21690 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ses/models.py
+-rw-r--r--   0 runner    (1001) docker     (123)    31667 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ses/responses.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1743 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ses/template.py
+-rw-r--r--   0 runner    (1001) docker     (123)      189 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ses/urls.py
+-rw-r--r--   0 runner    (1001) docker     (123)      573 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ses/utils.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4587 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/settings.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.420203 moto-4.1.7.dev9/moto/signer/
+-rw-r--r--   0 runner    (1001) docker     (123)      191 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/signer/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)       47 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/signer/exceptions.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6690 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/signer/models.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1609 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/signer/responses.py
+-rw-r--r--   0 runner    (1001) docker     (123)      302 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/signer/urls.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.420203 moto-4.1.7.dev9/moto/sns/
+-rw-r--r--   0 runner    (1001) docker     (123)      115 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/sns/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2096 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/sns/exceptions.py
+-rw-r--r--   0 runner    (1001) docker     (123)    38878 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/sns/models.py
+-rw-r--r--   0 runner    (1001) docker     (123)    46551 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/sns/responses.py
+-rw-r--r--   0 runner    (1001) docker     (123)      133 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/sns/urls.py
+-rw-r--r--   0 runner    (1001) docker     (123)      424 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/sns/utils.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.424203 moto-4.1.7.dev9/moto/sqs/
+-rw-r--r--   0 runner    (1001) docker     (123)      115 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/sqs/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3058 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/sqs/exceptions.py
+-rw-r--r--   0 runner    (1001) docker     (123)    38213 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/sqs/models.py
+-rw-r--r--   0 runner    (1001) docker     (123)    30771 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/sqs/responses.py
+-rw-r--r--   0 runner    (1001) docker     (123)      255 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/sqs/urls.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2558 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/sqs/utils.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.424203 moto-4.1.7.dev9/moto/ssm/
+-rw-r--r--   0 runner    (1001) docker     (123)      115 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ssm/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3171 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ssm/exceptions.py
+-rw-r--r--   0 runner    (1001) docker     (123)    75789 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ssm/models.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.428203 moto-4.1.7.dev9/moto/ssm/resources/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.436204 moto-4.1.7.dev9/moto/ssm/resources/ami-amazon-linux-latest/
+-rw-r--r--   0 runner    (1001) docker     (123)    10194 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ssm/resources/ami-amazon-linux-latest/af-south-1.json
+-rw-r--r--   0 runner    (1001) docker     (123)    10164 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ssm/resources/ami-amazon-linux-latest/ap-east-1.json
+-rw-r--r--   0 runner    (1001) docker     (123)    11683 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ssm/resources/ami-amazon-linux-latest/ap-northeast-1.json
+-rw-r--r--   0 runner    (1001) docker     (123)    10307 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ssm/resources/ami-amazon-linux-latest/ap-northeast-2.json
+-rw-r--r--   0 runner    (1001) docker     (123)    10310 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ssm/resources/ami-amazon-linux-latest/ap-northeast-3.json
+-rw-r--r--   0 runner    (1001) docker     (123)    10192 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ssm/resources/ami-amazon-linux-latest/ap-south-1.json
+-rw-r--r--   0 runner    (1001) docker     (123)     6642 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ssm/resources/ami-amazon-linux-latest/ap-south-2.json
+-rw-r--r--   0 runner    (1001) docker     (123)    11685 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ssm/resources/ami-amazon-linux-latest/ap-southeast-1.json
+-rw-r--r--   0 runner    (1001) docker     (123)    11683 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ssm/resources/ami-amazon-linux-latest/ap-southeast-2.json
+-rw-r--r--   0 runner    (1001) docker     (123)     9614 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ssm/resources/ami-amazon-linux-latest/ap-southeast-3.json
+-rw-r--r--   0 runner    (1001) docker     (123)    10251 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ssm/resources/ami-amazon-linux-latest/ca-central-1.json
+-rw-r--r--   0 runner    (1001) docker     (123)    11616 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ssm/resources/ami-amazon-linux-latest/eu-central-1.json
+-rw-r--r--   0 runner    (1001) docker     (123)     6682 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ssm/resources/ami-amazon-linux-latest/eu-central-2.json
+-rw-r--r--   0 runner    (1001) docker     (123)    10193 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ssm/resources/ami-amazon-linux-latest/eu-north-1.json
+-rw-r--r--   0 runner    (1001) docker     (123)    10191 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ssm/resources/ami-amazon-linux-latest/eu-south-1.json
+-rw-r--r--   0 runner    (1001) docker     (123)     6645 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ssm/resources/ami-amazon-linux-latest/eu-south-2.json
+-rw-r--r--   0 runner    (1001) docker     (123)    11520 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ssm/resources/ami-amazon-linux-latest/eu-west-1.json
+-rw-r--r--   0 runner    (1001) docker     (123)    10161 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ssm/resources/ami-amazon-linux-latest/eu-west-2.json
+-rw-r--r--   0 runner    (1001) docker     (123)    10160 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ssm/resources/ami-amazon-linux-latest/eu-west-3.json
+-rw-r--r--   0 runner    (1001) docker     (123)     9562 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ssm/resources/ami-amazon-linux-latest/me-central-1.json
+-rw-r--r--   0 runner    (1001) docker     (123)    10193 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ssm/resources/ami-amazon-linux-latest/me-south-1.json
+-rw-r--r--   0 runner    (1001) docker     (123)    11520 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ssm/resources/ami-amazon-linux-latest/sa-east-1.json
+-rw-r--r--   0 runner    (1001) docker     (123)    11520 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ssm/resources/ami-amazon-linux-latest/us-east-1.json
+-rw-r--r--   0 runner    (1001) docker     (123)    10165 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ssm/resources/ami-amazon-linux-latest/us-east-2.json
+-rw-r--r--   0 runner    (1001) docker     (123)    11516 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ssm/resources/ami-amazon-linux-latest/us-west-1.json
+-rw-r--r--   0 runner    (1001) docker     (123)    11520 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ssm/resources/ami-amazon-linux-latest/us-west-2.json
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.188194 moto-4.1.7.dev9/moto/ssm/resources/ecs/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.460204 moto-4.1.7.dev9/moto/ssm/resources/ecs/optimized_amis/
+-rw-r--r--   0 runner    (1001) docker     (123)   416937 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ssm/resources/ecs/optimized_amis/af-south-1.json
+-rw-r--r--   0 runner    (1001) docker     (123)   688021 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ssm/resources/ecs/optimized_amis/ap-east-1.json
+-rw-r--r--   0 runner    (1001) docker     (123)   807102 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ssm/resources/ecs/optimized_amis/ap-northeast-1.json
+-rw-r--r--   0 runner    (1001) docker     (123)   738181 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ssm/resources/ecs/optimized_amis/ap-northeast-2.json
+-rw-r--r--   0 runner    (1001) docker     (123)   360357 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ssm/resources/ecs/optimized_amis/ap-northeast-3.json
+-rw-r--r--   0 runner    (1001) docker     (123)   798560 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ssm/resources/ecs/optimized_amis/ap-south-1.json
+-rw-r--r--   0 runner    (1001) docker     (123)    85325 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ssm/resources/ecs/optimized_amis/ap-south-2.json
+-rw-r--r--   0 runner    (1001) docker     (123)   778515 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ssm/resources/ecs/optimized_amis/ap-southeast-1.json
+-rw-r--r--   0 runner    (1001) docker     (123)   807102 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ssm/resources/ecs/optimized_amis/ap-southeast-2.json
+-rw-r--r--   0 runner    (1001) docker     (123)   239300 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ssm/resources/ecs/optimized_amis/ap-southeast-3.json
+-rw-r--r--   0 runner    (1001) docker     (123)   734929 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ssm/resources/ecs/optimized_amis/ca-central-1.json
+-rw-r--r--   0 runner    (1001) docker     (123)   806032 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ssm/resources/ecs/optimized_amis/eu-central-1.json
+-rw-r--r--   0 runner    (1001) docker     (123)    84904 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ssm/resources/ecs/optimized_amis/eu-central-2.json
+-rw-r--r--   0 runner    (1001) docker     (123)   717425 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ssm/resources/ecs/optimized_amis/eu-north-1.json
+-rw-r--r--   0 runner    (1001) docker     (123)   618637 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ssm/resources/ecs/optimized_amis/eu-south-1.json
+-rw-r--r--   0 runner    (1001) docker     (123)    99223 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ssm/resources/ecs/optimized_amis/eu-south-2.json
+-rw-r--r--   0 runner    (1001) docker     (123)   815560 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ssm/resources/ecs/optimized_amis/eu-west-1.json
+-rw-r--r--   0 runner    (1001) docker     (123)   737073 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ssm/resources/ecs/optimized_amis/eu-west-2.json
+-rw-r--r--   0 runner    (1001) docker     (123)   737391 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ssm/resources/ecs/optimized_amis/eu-west-3.json
+-rw-r--r--   0 runner    (1001) docker     (123)   164329 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ssm/resources/ecs/optimized_amis/me-central-1.json
+-rw-r--r--   0 runner    (1001) docker     (123)   659463 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ssm/resources/ecs/optimized_amis/me-south-1.json
+-rw-r--r--   0 runner    (1001) docker     (123)   761741 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ssm/resources/ecs/optimized_amis/sa-east-1.json
+-rw-r--r--   0 runner    (1001) docker     (123)   823629 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ssm/resources/ecs/optimized_amis/us-east-1.json
+-rw-r--r--   0 runner    (1001) docker     (123)   815560 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ssm/resources/ecs/optimized_amis/us-east-2.json
+-rw-r--r--   0 runner    (1001) docker     (123)   767008 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ssm/resources/ecs/optimized_amis/us-west-1.json
+-rw-r--r--   0 runner    (1001) docker     (123)   820874 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ssm/resources/ecs/optimized_amis/us-west-2.json
+-rw-r--r--   0 runner    (1001) docker     (123)  1703321 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ssm/resources/regions.json
+-rw-r--r--   0 runner    (1001) docker     (123)  1782028 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ssm/resources/services.json
+-rw-r--r--   0 runner    (1001) docker     (123)    15018 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ssm/responses.py
+-rw-r--r--   0 runner    (1001) docker     (123)      219 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ssm/urls.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1224 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ssm/utils.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.460204 moto-4.1.7.dev9/moto/ssoadmin/
+-rw-r--r--   0 runner    (1001) docker     (123)      199 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ssoadmin/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      227 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ssoadmin/exceptions.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8104 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ssoadmin/models.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5455 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ssoadmin/responses.py
+-rw-r--r--   0 runner    (1001) docker     (123)      192 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ssoadmin/urls.py
+-rw-r--r--   0 runner    (1001) docker     (123)      253 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/ssoadmin/utils.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.464205 moto-4.1.7.dev9/moto/stepfunctions/
+-rw-r--r--   0 runner    (1001) docker     (123)      143 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/stepfunctions/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      915 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/stepfunctions/exceptions.py
+-rw-r--r--   0 runner    (1001) docker     (123)    21074 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/stepfunctions/models.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6755 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/stepfunctions/responses.py
+-rw-r--r--   0 runner    (1001) docker     (123)      153 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/stepfunctions/urls.py
+-rw-r--r--   0 runner    (1001) docker     (123)      691 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/stepfunctions/utils.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.464205 moto-4.1.7.dev9/moto/sts/
+-rw-r--r--   0 runner    (1001) docker     (123)      115 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/sts/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      239 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/sts/exceptions.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6610 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/sts/models.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8761 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/sts/responses.py
+-rw-r--r--   0 runner    (1001) docker     (123)      138 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/sts/urls.py
+-rw-r--r--   0 runner    (1001) docker     (123)      759 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/sts/utils.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.464205 moto-4.1.7.dev9/moto/support/
+-rw-r--r--   0 runner    (1001) docker     (123)      127 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/support/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/support/exceptions.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7989 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/support/models.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.464205 moto-4.1.7.dev9/moto/support/resources/
+-rw-r--r--   0 runner    (1001) docker     (123)   172189 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/support/resources/describe_trusted_advisor_checks.json
+-rw-r--r--   0 runner    (1001) docker     (123)     2461 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/support/responses.py
+-rw-r--r--   0 runner    (1001) docker     (123)      153 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/support/urls.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.468205 moto-4.1.7.dev9/moto/swf/
+-rw-r--r--   0 runner    (1001) docker     (123)      115 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/swf/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4265 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/swf/constants.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3795 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/swf/exceptions.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.468205 moto-4.1.7.dev9/moto/swf/models/
+-rw-r--r--   0 runner    (1001) docker     (123)    18122 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/swf/models/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2909 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/swf/models/activity_task.py
+-rw-r--r--   0 runner    (1001) docker     (123)      397 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/swf/models/activity_type.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2904 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/swf/models/decision_task.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4456 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/swf/models/domain.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1982 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/swf/models/generic_type.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2434 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/swf/models/history_event.py
+-rw-r--r--   0 runner    (1001) docker     (123)      310 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/swf/models/timeout.py
+-rw-r--r--   0 runner    (1001) docker     (123)      425 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/swf/models/timer.py
+-rw-r--r--   0 runner    (1001) docker     (123)    30491 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/swf/models/workflow_execution.py
+-rw-r--r--   0 runner    (1001) docker     (123)      409 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/swf/models/workflow_type.py
+-rw-r--r--   0 runner    (1001) docker     (123)    21829 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/swf/responses.py
+-rw-r--r--   0 runner    (1001) docker     (123)      133 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/swf/urls.py
+-rw-r--r--   0 runner    (1001) docker     (123)       59 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/swf/utils.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.472205 moto-4.1.7.dev9/moto/textract/
+-rw-r--r--   0 runner    (1001) docker     (123)      199 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/textract/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      981 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/textract/exceptions.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1937 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/textract/models.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1081 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/textract/responses.py
+-rw-r--r--   0 runner    (1001) docker     (123)      196 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/textract/urls.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.472205 moto-4.1.7.dev9/moto/timestreamwrite/
+-rw-r--r--   0 runner    (1001) docker     (123)      151 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/timestreamwrite/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      313 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/timestreamwrite/exceptions.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8111 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/timestreamwrite/models.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4991 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/timestreamwrite/responses.py
+-rw-r--r--   0 runner    (1001) docker     (123)      463 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/timestreamwrite/urls.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.472205 moto-4.1.7.dev9/moto/transcribe/
+-rw-r--r--   0 runner    (1001) docker     (123)      190 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/transcribe/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      351 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/transcribe/exceptions.py
+-rw-r--r--   0 runner    (1001) docker     (123)    31162 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/transcribe/models.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8194 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/transcribe/responses.py
+-rw-r--r--   0 runner    (1001) docker     (123)      154 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/transcribe/urls.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.476205 moto-4.1.7.dev9/moto/utilities/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/utilities/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2341 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/utilities/aws_headers.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9139 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/utilities/distutils_version.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2318 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/utilities/docker_utilities.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7404 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/utilities/paginator.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7572 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/utilities/tagging_service.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2059 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/utilities/tokenizer.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2784 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/utilities/utils.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.476205 moto-4.1.7.dev9/moto/wafv2/
+-rw-r--r--   0 runner    (1001) docker     (123)      165 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/wafv2/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      633 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/wafv2/exceptions.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6397 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/wafv2/models.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6140 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/wafv2/responses.py
+-rw-r--r--   0 runner    (1001) docker     (123)      151 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/wafv2/urls.py
+-rw-r--r--   0 runner    (1001) docker     (123)      401 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/wafv2/utils.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.480205 moto-4.1.7.dev9/moto/xray/
+-rw-r--r--   0 runner    (1001) docker     (123)      257 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/xray/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      568 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/xray/exceptions.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3548 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/xray/mock_client.py
+-rw-r--r--   0 runner    (1001) docker     (123)    10130 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/xray/models.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5909 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/xray/responses.py
+-rw-r--r--   0 runner    (1001) docker     (123)      393 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/moto/xray/urls.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.212195 moto-4.1.7.dev9/moto.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)     6287 2023-03-28 19:15:35.000000 moto-4.1.7.dev9/moto.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)    65063 2023-03-28 19:15:35.000000 moto-4.1.7.dev9/moto.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-03-28 19:15:35.000000 moto-4.1.7.dev9/moto.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       49 2023-03-28 19:15:35.000000 moto-4.1.7.dev9/moto.egg-info/entry_points.txt
+-rw-r--r--   0 runner    (1001) docker     (123)     2839 2023-03-28 19:15:35.000000 moto-4.1.7.dev9/moto.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        5 2023-03-28 19:15:35.000000 moto-4.1.7.dev9/moto.egg-info/top_level.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       91 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/pyproject.toml
+-rw-r--r--   0 runner    (1001) docker     (123)      162 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/requirements-dev.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       49 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/requirements.txt
+-rw-r--r--   0 runner    (1001) docker     (123)     5500 2023-03-28 19:15:35.668212 moto-4.1.7.dev9/setup.cfg
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.480205 moto-4.1.7.dev9/tests/
+-rw-r--r--   0 runner    (1001) docker     (123)      517 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1310 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/helpers.py
+-rw-r--r--   0 runner    (1001) docker     (123)      196 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/markers.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.480205 moto-4.1.7.dev9/tests/test_acm/
+-rw-r--r--   0 runner    (1001) docker     (123)       41 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_acm/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.480205 moto-4.1.7.dev9/tests/test_acm/resources/
+-rw-r--r--   0 runner    (1001) docker     (123)     1945 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_acm/resources/README.md
+-rw-r--r--   0 runner    (1001) docker     (123)       41 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_acm/resources/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3243 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_acm/resources/ca.key
+-rw-r--r--   0 runner    (1001) docker     (123)     3502 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_acm/resources/ca.pem
+-rw-r--r--   0 runner    (1001) docker     (123)       17 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_acm/resources/ca.srl
+-rw-r--r--   0 runner    (1001) docker     (123)     1589 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_acm/resources/star_moto_com-bad.pem
+-rw-r--r--   0 runner    (1001) docker     (123)     1017 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_acm/resources/star_moto_com.csr
+-rw-r--r--   0 runner    (1001) docker     (123)     1675 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_acm/resources/star_moto_com.key
+-rw-r--r--   0 runner    (1001) docker     (123)     1558 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_acm/resources/star_moto_com.pem
+-rw-r--r--   0 runner    (1001) docker     (123)    25475 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_acm/test_acm.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.480205 moto-4.1.7.dev9/tests/test_acmpca/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_acmpca/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    12974 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_acmpca/test_acmpca.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.484205 moto-4.1.7.dev9/tests/test_amp/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_amp/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2167 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_amp/test_amp_logging_config.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6058 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_amp/test_amp_rulegroupnamespaces.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5042 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_amp/test_amp_workspaces.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.484205 moto-4.1.7.dev9/tests/test_apigateway/
+-rw-r--r--   0 runner    (1001) docker     (123)       41 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_apigateway/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.488206 moto-4.1.7.dev9/tests/test_apigateway/resources/
+-rw-r--r--   0 runner    (1001) docker     (123)    21989 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_apigateway/resources/petstore-swagger-v3.yaml
+-rw-r--r--   0 runner    (1001) docker     (123)     1656 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_apigateway/resources/test_api.json
+-rw-r--r--   0 runner    (1001) docker     (123)     1294 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_apigateway/resources/test_api.yaml
+-rw-r--r--   0 runner    (1001) docker     (123)     1642 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_apigateway/resources/test_api_invalid.json
+-rw-r--r--   0 runner    (1001) docker     (123)     1641 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_apigateway/resources/test_api_invalid_version.json
+-rw-r--r--   0 runner    (1001) docker     (123)     1062 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_apigateway/resources/test_deep_api.yaml
+-rw-r--r--   0 runner    (1001) docker     (123)    91555 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_apigateway/test_apigateway.py
+-rw-r--r--   0 runner    (1001) docker     (123)    10430 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_apigateway/test_apigateway_cloudformation.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7799 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_apigateway/test_apigateway_deployments.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3117 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_apigateway/test_apigateway_export.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5216 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_apigateway/test_apigateway_gatewayresponses.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3228 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_apigateway/test_apigateway_importrestapi.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7942 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_apigateway/test_apigateway_integration.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7637 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_apigateway/test_apigateway_putrestapi.py
+-rw-r--r--   0 runner    (1001) docker     (123)    18926 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_apigateway/test_apigateway_stage.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4856 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_apigateway/test_apigateway_validators.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3144 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_apigateway/test_apigateway_vpclink.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5294 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_apigateway/test_server.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.492205 moto-4.1.7.dev9/tests/test_apigatewayv2/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_apigatewayv2/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    11724 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_apigatewayv2/test_apigatewayv2.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7989 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_apigatewayv2/test_apigatewayv2_authorizers.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3242 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_apigatewayv2/test_apigatewayv2_domains.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6738 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_apigatewayv2/test_apigatewayv2_integrationresponses.py
+-rw-r--r--   0 runner    (1001) docker     (123)    12319 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_apigatewayv2/test_apigatewayv2_integrations.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6837 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_apigatewayv2/test_apigatewayv2_mappings.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3858 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_apigatewayv2/test_apigatewayv2_models.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5621 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_apigatewayv2/test_apigatewayv2_reimport.py
+-rw-r--r--   0 runner    (1001) docker     (123)    11181 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_apigatewayv2/test_apigatewayv2_routes.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1965 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_apigatewayv2/test_apigatewayv2_tags.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5184 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_apigatewayv2/test_apigatewayv2_vpclinks.py
+-rw-r--r--   0 runner    (1001) docker     (123)      360 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_apigatewayv2/test_server.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.492205 moto-4.1.7.dev9/tests/test_applicationautoscaling/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_applicationautoscaling/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    25197 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_applicationautoscaling/test_applicationautoscaling.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4077 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_applicationautoscaling/test_validation.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.492205 moto-4.1.7.dev9/tests/test_appsync/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_appsync/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5489 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_appsync/test_appsync.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3519 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_appsync/test_appsync_apikeys.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2646 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_appsync/test_appsync_schema.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2857 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_appsync/test_appsync_tags.py
+-rw-r--r--   0 runner    (1001) docker     (123)      490 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_appsync/test_server.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.492205 moto-4.1.7.dev9/tests/test_athena/
+-rw-r--r--   0 runner    (1001) docker     (123)       41 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_athena/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    14774 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_athena/test_athena.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5393 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_athena/test_athena_server_api.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.496206 moto-4.1.7.dev9/tests/test_autoscaling/
+-rw-r--r--   0 runner    (1001) docker     (123)       41 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_autoscaling/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    48170 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_autoscaling/test_autoscaling.py
+-rw-r--r--   0 runner    (1001) docker     (123)    17392 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_autoscaling/test_autoscaling_cloudformation.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9658 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_autoscaling/test_autoscaling_groups.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1494 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_autoscaling/test_autoscaling_metrics.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3150 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_autoscaling/test_autoscaling_scheduledactions.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8692 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_autoscaling/test_autoscaling_tags.py
+-rw-r--r--   0 runner    (1001) docker     (123)    40671 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_autoscaling/test_elb.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4184 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_autoscaling/test_elbv2.py
+-rw-r--r--   0 runner    (1001) docker     (123)    12469 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_autoscaling/test_launch_configurations.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5331 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_autoscaling/test_policies.py
+-rw-r--r--   0 runner    (1001) docker     (123)      458 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_autoscaling/test_server.py
+-rw-r--r--   0 runner    (1001) docker     (123)      933 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_autoscaling/utils.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.500206 moto-4.1.7.dev9/tests/test_awslambda/
+-rw-r--r--   0 runner    (1001) docker     (123)       41 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_awslambda/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    11564 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_awslambda/test_awslambda_cloudformation.py
+-rw-r--r--   0 runner    (1001) docker     (123)    46812 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_awslambda/test_lambda.py
+-rw-r--r--   0 runner    (1001) docker     (123)    10044 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_awslambda/test_lambda_alias.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2799 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_awslambda/test_lambda_concurrency.py
+-rw-r--r--   0 runner    (1001) docker     (123)    15860 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_awslambda/test_lambda_eventsourcemapping.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4021 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_awslambda/test_lambda_function_urls.py
+-rw-r--r--   0 runner    (1001) docker     (123)    12979 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_awslambda/test_lambda_invoke.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9713 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_awslambda/test_lambda_layers.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9427 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_awslambda/test_lambda_policy.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4087 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_awslambda/test_lambda_tags.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1380 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_awslambda/test_policy.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5610 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_awslambda/utilities.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.500206 moto-4.1.7.dev9/tests/test_batch/
+-rw-r--r--   0 runner    (1001) docker     (123)     1387 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_batch/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      333 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_batch/test_batch.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9596 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_batch/test_batch_cloudformation.py
+-rw-r--r--   0 runner    (1001) docker     (123)    13474 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_batch/test_batch_compute_envs.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6948 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_batch/test_batch_job_queue.py
+-rw-r--r--   0 runner    (1001) docker     (123)    34446 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_batch/test_batch_jobs.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2989 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_batch/test_batch_scheduling_policy.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2021 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_batch/test_batch_tags_job_definition.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4137 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_batch/test_batch_tags_job_queue.py
+-rw-r--r--   0 runner    (1001) docker     (123)      368 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_batch/test_batch_tags_scheduling_policy.py
+-rw-r--r--   0 runner    (1001) docker     (123)    11540 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_batch/test_batch_task_definition.py
+-rw-r--r--   0 runner    (1001) docker     (123)      381 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_batch/test_server.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.504206 moto-4.1.7.dev9/tests/test_batch_simple/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_batch_simple/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9807 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_batch_simple/test_batch_cloudformation.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3473 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_batch_simple/test_batch_compute_envs.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3374 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_batch_simple/test_batch_jobs.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.504206 moto-4.1.7.dev9/tests/test_budgets/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_budgets/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6679 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_budgets/test_budgets.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6974 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_budgets/test_notifications.py
+-rw-r--r--   0 runner    (1001) docker     (123)      516 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_budgets/test_server.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.504206 moto-4.1.7.dev9/tests/test_ce/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_ce/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4466 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_ce/test_ce.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1998 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_ce/test_ce_tags.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.508206 moto-4.1.7.dev9/tests/test_cloudformation/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_cloudformation/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.512206 moto-4.1.7.dev9/tests/test_cloudformation/fixtures/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_cloudformation/fixtures/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3233 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_cloudformation/fixtures/custom_lambda.py
+-rw-r--r--   0 runner    (1001) docker     (123)       64 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_cloudformation/fixtures/ec2_classic_eip.py
+-rw-r--r--   0 runner    (1001) docker     (123)      243 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_cloudformation/fixtures/fn_join.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1604 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_cloudformation/fixtures/kms_key.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8837 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_cloudformation/fixtures/rds_mysql_with_db_parameter_group.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8550 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_cloudformation/fixtures/rds_mysql_with_read_replica.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7040 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_cloudformation/fixtures/redshift.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1277 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_cloudformation/fixtures/route53_ec2_instance_with_public_ip.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1052 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_cloudformation/fixtures/route53_health_check.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3189 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_cloudformation/fixtures/route53_roundrobin.py
+-rw-r--r--   0 runner    (1001) docker     (123)    10926 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_cloudformation/fixtures/single_instance_with_ebs_volume.py
+-rw-r--r--   0 runner    (1001) docker     (123)      106 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_cloudformation/fixtures/vpc_eip.py
+-rw-r--r--   0 runner    (1001) docker     (123)      939 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_cloudformation/fixtures/vpc_eni.py
+-rw-r--r--   0 runner    (1001) docker     (123)    12162 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_cloudformation/fixtures/vpc_single_instance_in_subnet.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8625 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_cloudformation/test_cloudformation_custom_resources.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5440 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_cloudformation/test_cloudformation_depends_on.py
+-rw-r--r--   0 runner    (1001) docker     (123)    12559 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_cloudformation/test_cloudformation_multi_accounts.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6373 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_cloudformation/test_cloudformation_nested_stacks.py
+-rw-r--r--   0 runner    (1001) docker     (123)    85564 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_cloudformation/test_cloudformation_stack_crud_boto3.py
+-rw-r--r--   0 runner    (1001) docker     (123)    69300 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_cloudformation/test_cloudformation_stack_integration.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4223 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_cloudformation/test_cloudformation_stack_policies.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2949 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_cloudformation/test_import_value.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1051 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_cloudformation/test_server.py
+-rw-r--r--   0 runner    (1001) docker     (123)    20743 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_cloudformation/test_stack_parsing.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4442 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_cloudformation/test_validate.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.512206 moto-4.1.7.dev9/tests/test_cloudfront/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_cloudfront/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2446 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_cloudfront/cloudfront_test_scaffolding.py
+-rw-r--r--   0 runner    (1001) docker     (123)    10114 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_cloudfront/test_cloudfront.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1582 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_cloudfront/test_cloudfront_dist_tags.py
+-rw-r--r--   0 runner    (1001) docker     (123)    28631 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_cloudfront/test_cloudfront_distributions.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2938 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_cloudfront/test_cloudfront_invalidation.py
+-rw-r--r--   0 runner    (1001) docker     (123)      489 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_cloudfront/test_server.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.512206 moto-4.1.7.dev9/tests/test_cloudtrail/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_cloudtrail/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    21003 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_cloudtrail/test_cloudtrail.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6377 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_cloudtrail/test_cloudtrail_eventselectors.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2539 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_cloudtrail/test_cloudtrail_tags.py
+-rw-r--r--   0 runner    (1001) docker     (123)      541 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_cloudtrail/test_server.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.516207 moto-4.1.7.dev9/tests/test_cloudwatch/
+-rw-r--r--   0 runner    (1001) docker     (123)       41 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_cloudwatch/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8634 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_cloudwatch/test_cloudwatch_alarms.py
+-rw-r--r--   0 runner    (1001) docker     (123)    54006 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_cloudwatch/test_cloudwatch_boto3.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3368 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_cloudwatch/test_cloudwatch_dashboards.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6388 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_cloudwatch/test_cloudwatch_tags.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.516207 moto-4.1.7.dev9/tests/test_codebuild/
+-rw-r--r--   0 runner    (1001) docker     (123)    19951 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_codebuild/test_codebuild.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.516207 moto-4.1.7.dev9/tests/test_codecommit/
+-rw-r--r--   0 runner    (1001) docker     (123)     8512 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_codecommit/test_codecommit.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.516207 moto-4.1.7.dev9/tests/test_codepipeline/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_codepipeline/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    25530 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_codepipeline/test_codepipeline.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.516207 moto-4.1.7.dev9/tests/test_cognitoidentity/
+-rw-r--r--   0 runner    (1001) docker     (123)       41 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_cognitoidentity/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8947 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_cognitoidentity/test_cognitoidentity.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3130 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_cognitoidentity/test_server.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.516207 moto-4.1.7.dev9/tests/test_cognitoidp/
+-rw-r--r--   0 runner    (1001) docker     (123)       41 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_cognitoidp/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)   161791 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_cognitoidp/test_cognitoidp.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3560 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_cognitoidp/test_cognitoidp_exceptions.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3858 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_cognitoidp/test_cognitoidp_replay.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6356 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_cognitoidp/test_server.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.516207 moto-4.1.7.dev9/tests/test_comprehend/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_comprehend/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7440 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_comprehend/test_comprehend.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.520207 moto-4.1.7.dev9/tests/test_config/
+-rw-r--r--   0 runner    (1001) docker     (123)       41 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_config/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    78639 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_config/test_config.py
+-rw-r--r--   0 runner    (1001) docker     (123)    18070 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_config/test_config_rules.py
+-rw-r--r--   0 runner    (1001) docker     (123)    11670 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_config/test_config_rules_integration.py
+-rw-r--r--   0 runner    (1001) docker     (123)    11741 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_config/test_config_tags.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.524207 moto-4.1.7.dev9/tests/test_core/
+-rw-r--r--   0 runner    (1001) docker     (123)       41 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_core/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2580 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_core/test_account_id_resolution.py
+-rw-r--r--   0 runner    (1001) docker     (123)    26898 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_core/test_auth.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9624 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_core/test_backenddict.py
+-rw-r--r--   0 runner    (1001) docker     (123)      501 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_core/test_context_manager.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9923 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_core/test_decorator_calls.py
+-rw-r--r--   0 runner    (1001) docker     (123)      929 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_core/test_docker.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1074 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_core/test_environ_patching.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3261 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_core/test_importorder.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1297 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_core/test_instance_metadata.py
+-rw-r--r--   0 runner    (1001) docker     (123)      959 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_core/test_mock_all.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2232 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_core/test_mock_regions.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4951 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_core/test_moto_api.py
+-rw-r--r--   0 runner    (1001) docker     (123)      736 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_core/test_nested.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1493 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_core/test_request_mocking.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8330 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_core/test_responses.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2012 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_core/test_responses_module.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1543 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_core/test_server.py
+-rw-r--r--   0 runner    (1001) docker     (123)      758 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_core/test_settings.py
+-rw-r--r--   0 runner    (1001) docker     (123)      326 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_core/test_socket.py
+-rw-r--r--   0 runner    (1001) docker     (123)      920 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_core/test_url_base_regex.py
+-rw-r--r--   0 runner    (1001) docker     (123)      733 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_core/test_url_mapping.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1455 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_core/test_utils.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.528207 moto-4.1.7.dev9/tests/test_databrew/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_databrew/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8669 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_databrew/test_databrew_datasets.py
+-rw-r--r--   0 runner    (1001) docker     (123)    13383 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_databrew/test_databrew_jobs.py
+-rw-r--r--   0 runner    (1001) docker     (123)    19199 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_databrew/test_databrew_recipes.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5426 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_databrew/test_databrew_rulesets.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.528207 moto-4.1.7.dev9/tests/test_datapipeline/
+-rw-r--r--   0 runner    (1001) docker     (123)       41 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_datapipeline/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6242 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_datapipeline/test_datapipeline.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2736 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_datapipeline/test_datapipeline_cloudformation.py
+-rw-r--r--   0 runner    (1001) docker     (123)      586 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_datapipeline/test_server.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.528207 moto-4.1.7.dev9/tests/test_datasync/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_datasync/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    14878 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_datasync/test_datasync.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.528207 moto-4.1.7.dev9/tests/test_dax/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_dax/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    16182 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_dax/test_dax.py
+-rw-r--r--   0 runner    (1001) docker     (123)      376 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_dax/test_server.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.528207 moto-4.1.7.dev9/tests/test_dms/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_dms/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7191 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_dms/test_dms.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.532207 moto-4.1.7.dev9/tests/test_ds/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_ds/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    13394 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_ds/test_ds.py
+-rw-r--r--   0 runner    (1001) docker     (123)    11204 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_ds/test_ds_ad_connect.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8960 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_ds/test_ds_microsoft_ad.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9095 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_ds/test_ds_simple_ad_directory.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4751 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_ds/test_ds_tags.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.536207 moto-4.1.7.dev9/tests/test_dynamodb/
+-rw-r--r--   0 runner    (1001) docker     (123)       41 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_dynamodb/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      545 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_dynamodb/conftest.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.536207 moto-4.1.7.dev9/tests/test_dynamodb/exceptions/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_dynamodb/exceptions/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    39637 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_dynamodb/exceptions/test_dynamodb_exceptions.py
+-rw-r--r--   0 runner    (1001) docker     (123)    12004 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_dynamodb/exceptions/test_key_length_exceptions.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.536207 moto-4.1.7.dev9/tests/test_dynamodb/models/
+-rw-r--r--   0 runner    (1001) docker     (123)     7419 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_dynamodb/models/test_key_condition_expression_parser.py
+-rw-r--r--   0 runner    (1001) docker     (123)   204428 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_dynamodb/test_dynamodb.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8093 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_dynamodb/test_dynamodb_batch_get_item.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1619 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_dynamodb/test_dynamodb_cloudformation.py
+-rw-r--r--   0 runner    (1001) docker     (123)    15796 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_dynamodb/test_dynamodb_condition_expressions.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5383 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_dynamodb/test_dynamodb_consumedcapacity.py
+-rw-r--r--   0 runner    (1001) docker     (123)    16456 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_dynamodb/test_dynamodb_create_table.py
+-rw-r--r--   0 runner    (1001) docker     (123)    17832 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_dynamodb/test_dynamodb_executor.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9879 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_dynamodb/test_dynamodb_expression_tokenizer.py
+-rw-r--r--   0 runner    (1001) docker     (123)    14053 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_dynamodb/test_dynamodb_expressions.py
+-rw-r--r--   0 runner    (1001) docker     (123)    39804 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_dynamodb/test_dynamodb_table_with_range_key.py
+-rw-r--r--   0 runner    (1001) docker     (123)    20261 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_dynamodb/test_dynamodb_table_without_range_key.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1062 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_dynamodb/test_dynamodb_update_expressions.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2832 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_dynamodb/test_dynamodb_update_table.py
+-rw-r--r--   0 runner    (1001) docker     (123)    16779 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_dynamodb/test_dynamodb_validation.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1095 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_dynamodb/test_server.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.536207 moto-4.1.7.dev9/tests/test_dynamodb_v20111205/
+-rw-r--r--   0 runner    (1001) docker     (123)       41 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_dynamodb_v20111205/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    43145 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_dynamodb_v20111205/test_server.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2391 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_dynamodb_v20111205/test_servermode.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.536207 moto-4.1.7.dev9/tests/test_dynamodbstreams/
+-rw-r--r--   0 runner    (1001) docker     (123)       41 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_dynamodbstreams/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    10314 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_dynamodbstreams/test_dynamodbstreams.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.536207 moto-4.1.7.dev9/tests/test_ebs/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_ebs/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5997 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_ebs/test_ebs.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.548208 moto-4.1.7.dev9/tests/test_ec2/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_ec2/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      496 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_ec2/helpers.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1218 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_ec2/test_account_attributes.py
+-rw-r--r--   0 runner    (1001) docker     (123)      135 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_ec2/test_amazon_dev_pay.py
+-rw-r--r--   0 runner    (1001) docker     (123)    44698 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_ec2/test_amis.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2456 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_ec2/test_availability_zones_and_regions.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3832 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_ec2/test_carrier_gateways.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4131 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_ec2/test_customer_gateways.py
+-rw-r--r--   0 runner    (1001) docker     (123)    17165 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_ec2/test_dhcp_options.py
+-rw-r--r--   0 runner    (1001) docker     (123)    35904 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_ec2/test_ec2_cloudformation.py
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_ec2/test_ec2_core.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1521 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_ec2/test_ec2_integration.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3410 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_ec2/test_egress_only_igw.py
+-rw-r--r--   0 runner    (1001) docker     (123)    42808 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_ec2/test_elastic_block_store.py
+-rw-r--r--   0 runner    (1001) docker     (123)    26968 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_ec2/test_elastic_ip_addresses.py
+-rw-r--r--   0 runner    (1001) docker     (123)    40929 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_ec2/test_elastic_network_interfaces.py
+-rw-r--r--   0 runner    (1001) docker     (123)    22223 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_ec2/test_fleets.py
+-rw-r--r--   0 runner    (1001) docker     (123)    24744 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_ec2/test_flow_logs.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3659 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_ec2/test_flow_logs_cloudformation.py
+-rw-r--r--   0 runner    (1001) docker     (123)      888 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_ec2/test_general.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5099 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_ec2/test_hosts.py
+-rw-r--r--   0 runner    (1001) docker     (123)    10287 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_ec2/test_iam_integration.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3205 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_ec2/test_instance_type_offerings.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6937 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_ec2/test_instance_types.py
+-rw-r--r--   0 runner    (1001) docker     (123)    98932 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_ec2/test_instances.py
+-rw-r--r--   0 runner    (1001) docker     (123)    12355 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_ec2/test_internet_gateways.py
+-rw-r--r--   0 runner    (1001) docker     (123)      133 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_ec2/test_ip_addresses.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9667 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_ec2/test_key_pairs.py
+-rw-r--r--   0 runner    (1001) docker     (123)    22901 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_ec2/test_launch_templates.py
+-rw-r--r--   0 runner    (1001) docker     (123)      131 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_ec2/test_monitoring.py
+-rw-r--r--   0 runner    (1001) docker     (123)    10435 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_ec2/test_nat_gateway.py
+-rw-r--r--   0 runner    (1001) docker     (123)    15234 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_ec2/test_network_acls.py
+-rw-r--r--   0 runner    (1001) docker     (123)      137 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_ec2/test_placement_groups.py
+-rw-r--r--   0 runner    (1001) docker     (123)    11252 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_ec2/test_prefix_lists.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6112 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_ec2/test_regions.py
+-rw-r--r--   0 runner    (1001) docker     (123)      139 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_ec2/test_reserved_instances.py
+-rw-r--r--   0 runner    (1001) docker     (123)    40234 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_ec2/test_route_tables.py
+-rw-r--r--   0 runner    (1001) docker     (123)    64524 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_ec2/test_security_groups.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9376 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_ec2/test_security_groups_cloudformation.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2458 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_ec2/test_server.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1584 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_ec2/test_settings.py
+-rw-r--r--   0 runner    (1001) docker     (123)    20068 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_ec2/test_spot_fleet.py
+-rw-r--r--   0 runner    (1001) docker     (123)    15364 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_ec2/test_spot_instances.py
+-rw-r--r--   0 runner    (1001) docker     (123)    31381 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_ec2/test_subnets.py
+-rw-r--r--   0 runner    (1001) docker     (123)    18120 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_ec2/test_tags.py
+-rw-r--r--   0 runner    (1001) docker     (123)    33200 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_ec2/test_transit_gateway.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3556 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_ec2/test_transit_gateway_cloudformation.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8110 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_ec2/test_transit_gateway_peering_attachments.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2022 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_ec2/test_utils.py
+-rw-r--r--   0 runner    (1001) docker     (123)    10382 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_ec2/test_virtual_private_gateways.py
+-rw-r--r--   0 runner    (1001) docker     (123)      130 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_ec2/test_vm_export.py
+-rw-r--r--   0 runner    (1001) docker     (123)      130 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_ec2/test_vm_import.py
+-rw-r--r--   0 runner    (1001) docker     (123)    11771 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_ec2/test_vpc_endpoint_services_integration.py
+-rw-r--r--   0 runner    (1001) docker     (123)    19510 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_ec2/test_vpc_peering.py
+-rw-r--r--   0 runner    (1001) docker     (123)    13918 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_ec2/test_vpc_service_configuration.py
+-rw-r--r--   0 runner    (1001) docker     (123)    45725 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_ec2/test_vpcs.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4926 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_ec2/test_vpn_connections.py
+-rw-r--r--   0 runner    (1001) docker     (123)      938 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_ec2/test_windows.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.548208 moto-4.1.7.dev9/tests/test_ec2instanceconnect/
+-rw-r--r--   0 runner    (1001) docker     (123)      898 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_ec2instanceconnect/test_ec2instanceconnect_boto3.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.548208 moto-4.1.7.dev9/tests/test_ecr/
+-rw-r--r--   0 runner    (1001) docker     (123)       41 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_ecr/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    90248 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_ecr/test_ecr_boto3.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3133 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_ecr/test_ecr_cloudformation.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2383 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_ecr/test_ecr_helpers.py
+-rw-r--r--   0 runner    (1001) docker     (123)    11690 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_ecr/test_ecr_policy_validation.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.552208 moto-4.1.7.dev9/tests/test_ecs/
+-rw-r--r--   0 runner    (1001) docker     (123)       41 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_ecs/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8223 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_ecs/test_ecs_account_settings.py
+-rw-r--r--   0 runner    (1001) docker     (123)   124666 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_ecs/test_ecs_boto3.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7707 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_ecs/test_ecs_capacity_provider.py
+-rw-r--r--   0 runner    (1001) docker     (123)    14232 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_ecs/test_ecs_cloudformation.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1192 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_ecs/test_ecs_efs.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1499 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_ecs/test_ecs_task_def_tags.py
+-rw-r--r--   0 runner    (1001) docker     (123)    13616 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_ecs/test_ecs_tasksets.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.552208 moto-4.1.7.dev9/tests/test_efs/
+-rw-r--r--   0 runner    (1001) docker     (123)      358 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_efs/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      103 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_efs/junk_drawer.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2318 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_efs/test_access_point_tagging.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4445 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_efs/test_access_points.py
+-rw-r--r--   0 runner    (1001) docker     (123)    13043 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_efs/test_file_system.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1906 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_efs/test_filesystem_tagging.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1554 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_efs/test_lifecycle_config.py
+-rw-r--r--   0 runner    (1001) docker     (123)    13392 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_efs/test_mount_target.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3709 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_efs/test_mount_target_security_groups.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3115 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_efs/test_server.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.556208 moto-4.1.7.dev9/tests/test_eks/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_eks/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    52255 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_eks/test_eks.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7616 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_eks/test_eks_constants.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2240 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_eks/test_eks_ec2.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4344 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_eks/test_eks_utils.py
+-rw-r--r--   0 runner    (1001) docker     (123)    17353 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_eks/test_server.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.556208 moto-4.1.7.dev9/tests/test_elasticache/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_elasticache/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7236 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_elasticache/test_elasticache.py
+-rw-r--r--   0 runner    (1001) docker     (123)      477 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_elasticache/test_server.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.556208 moto-4.1.7.dev9/tests/test_elasticbeanstalk/
+-rw-r--r--   0 runner    (1001) docker     (123)     4486 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_elasticbeanstalk/test_eb.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.556208 moto-4.1.7.dev9/tests/test_elastictranscoder/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_elastictranscoder/__init__
+-rw-r--r--   0 runner    (1001) docker     (123)    14785 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_elastictranscoder/test_elastictranscoder.py
+-rw-r--r--   0 runner    (1001) docker     (123)      423 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_elastictranscoder/test_server.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.556208 moto-4.1.7.dev9/tests/test_elb/
+-rw-r--r--   0 runner    (1001) docker     (123)       41 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_elb/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    41073 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_elb/test_elb.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1982 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_elb/test_elb_availabilityzones.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5096 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_elb/test_elb_cloudformation.py
+-rw-r--r--   0 runner    (1001) docker     (123)    10157 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_elb/test_elb_policies.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1951 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_elb/test_elb_subnets.py
+-rw-r--r--   0 runner    (1001) docker     (123)      394 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_elb/test_server.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.560208 moto-4.1.7.dev9/tests/test_elbv2/
+-rw-r--r--   0 runner    (1001) docker     (123)       41 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_elbv2/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    65284 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_elbv2/test_elbv2.py
+-rw-r--r--   0 runner    (1001) docker     (123)    12345 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_elbv2/test_elbv2_cloudformation.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2419 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_elbv2/test_elbv2_integration.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2777 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_elbv2/test_elbv2_listener_rule_tags.py
+-rw-r--r--   0 runner    (1001) docker     (123)    16854 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_elbv2/test_elbv2_listener_rules.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2365 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_elbv2/test_elbv2_listener_tags.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2738 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_elbv2/test_elbv2_set_subnets.py
+-rw-r--r--   0 runner    (1001) docker     (123)    25515 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_elbv2/test_elbv2_target_groups.py
+-rw-r--r--   0 runner    (1001) docker     (123)      403 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_elbv2/test_server.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.564208 moto-4.1.7.dev9/tests/test_emr/
+-rw-r--r--   0 runner    (1001) docker     (123)       41 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_emr/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    45802 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_emr/test_emr_boto3.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7968 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_emr/test_emr_integration.py
+-rw-r--r--   0 runner    (1001) docker     (123)      403 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_emr/test_server.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1484 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_emr/test_utils.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.564208 moto-4.1.7.dev9/tests/test_emrcontainers/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_emrcontainers/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    20727 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_emrcontainers/test_emrcontainers.py
+-rw-r--r--   0 runner    (1001) docker     (123)      380 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_emrcontainers/test_server.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.564208 moto-4.1.7.dev9/tests/test_emrserverless/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_emrserverless/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    19180 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_emrserverless/test_emrserverless.py
+-rw-r--r--   0 runner    (1001) docker     (123)      386 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_emrserverless/test_server.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.564208 moto-4.1.7.dev9/tests/test_es/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_es/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9146 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_es/test_es.py
+-rw-r--r--   0 runner    (1001) docker     (123)      352 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_es/test_server.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.568209 moto-4.1.7.dev9/tests/test_events/
+-rw-r--r--   0 runner    (1001) docker     (123)       41 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_events/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4186 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_events/test_event_pattern.py
+-rw-r--r--   0 runner    (1001) docker     (123)    81682 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_events/test_events.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5843 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_events/test_events_cloudformation.py
+-rw-r--r--   0 runner    (1001) docker     (123)    13082 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_events/test_events_integration.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9161 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_events/test_events_lambdatriggers_integration.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.568209 moto-4.1.7.dev9/tests/test_firehose/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_firehose/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    20103 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_firehose/test_firehose.py
+-rw-r--r--   0 runner    (1001) docker     (123)    13553 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_firehose/test_firehose_destination_types.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2967 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_firehose/test_firehose_encryption.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5439 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_firehose/test_firehose_put.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5953 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_firehose/test_firehose_tags.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3336 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_firehose/test_http_destinations.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.568209 moto-4.1.7.dev9/tests/test_forecast/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_forecast/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7786 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_forecast/test_forecast.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.572209 moto-4.1.7.dev9/tests/test_glacier/
+-rw-r--r--   0 runner    (1001) docker     (123)       41 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_glacier/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)       38 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_glacier/test.gz
+-rw-r--r--   0 runner    (1001) docker     (123)     1988 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_glacier/test_glacier_archives.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4811 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_glacier/test_glacier_jobs.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2989 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_glacier/test_glacier_vaults.py
+-rw-r--r--   0 runner    (1001) docker     (123)      436 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_glacier/test_server.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.572209 moto-4.1.7.dev9/tests/test_glue/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_glue/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.576209 moto-4.1.7.dev9/tests/test_glue/fixtures/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_glue/fixtures/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2153 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_glue/fixtures/datacatalog.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5015 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_glue/fixtures/schema_registry.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6423 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_glue/helpers.py
+-rw-r--r--   0 runner    (1001) docker     (123)    48038 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_glue/test_datacatalog.py
+-rw-r--r--   0 runner    (1001) docker     (123)    14293 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_glue/test_glue.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4899 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_glue/test_glue_job_runs.py
+-rw-r--r--   0 runner    (1001) docker     (123)    14929 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_glue/test_partition_filter.py
+-rw-r--r--   0 runner    (1001) docker     (123)    47112 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_glue/test_schema_registry.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.576209 moto-4.1.7.dev9/tests/test_greengrass/
+-rw-r--r--   0 runner    (1001) docker     (123)       41 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_greengrass/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    13441 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_greengrass/test_greengrass_core.py
+-rw-r--r--   0 runner    (1001) docker     (123)    18455 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_greengrass/test_greengrass_deployment.py
+-rw-r--r--   0 runner    (1001) docker     (123)    15306 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_greengrass/test_greengrass_device.py
+-rw-r--r--   0 runner    (1001) docker     (123)    16217 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_greengrass/test_greengrass_functions.py
+-rw-r--r--   0 runner    (1001) docker     (123)    19915 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_greengrass/test_greengrass_groups.py
+-rw-r--r--   0 runner    (1001) docker     (123)    21905 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_greengrass/test_greengrass_resource.py
+-rw-r--r--   0 runner    (1001) docker     (123)    20373 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_greengrass/test_greengrass_subscriptions.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.580209 moto-4.1.7.dev9/tests/test_guardduty/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_guardduty/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5080 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_guardduty/test_guardduty.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3179 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_guardduty/test_guardduty_filters.py
+-rw-r--r--   0 runner    (1001) docker     (123)      844 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_guardduty/test_guardduty_organization.py
+-rw-r--r--   0 runner    (1001) docker     (123)      432 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_guardduty/test_server.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.584209 moto-4.1.7.dev9/tests/test_iam/
+-rw-r--r--   0 runner    (1001) docker     (123)       41 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_iam/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)   167646 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_iam/test_iam.py
+-rw-r--r--   0 runner    (1001) docker     (123)      822 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_iam/test_iam_access_integration.py
+-rw-r--r--   0 runner    (1001) docker     (123)      672 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_iam/test_iam_account_aliases.py
+-rw-r--r--   0 runner    (1001) docker     (123)    51772 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_iam/test_iam_cloudformation.py
+-rw-r--r--   0 runner    (1001) docker     (123)    11597 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_iam/test_iam_groups.py
+-rw-r--r--   0 runner    (1001) docker     (123)    13090 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_iam/test_iam_oidc.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1264 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_iam/test_iam_password_last_used.py
+-rw-r--r--   0 runner    (1001) docker     (123)    51265 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_iam/test_iam_policies.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3196 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_iam/test_iam_server_certificates.py
+-rw-r--r--   0 runner    (1001) docker     (123)      594 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_iam/test_server.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.584209 moto-4.1.7.dev9/tests/test_identitystore/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_identitystore/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      761 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_identitystore/test_identitystore.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.588209 moto-4.1.7.dev9/tests/test_iot/
+-rw-r--r--   0 runner    (1001) docker     (123)       41 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_iot/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6115 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_iot/test_iot.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6208 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_iot/test_iot_ca_certificates.py
+-rw-r--r--   0 runner    (1001) docker     (123)    13028 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_iot/test_iot_certificates.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2700 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_iot/test_iot_deprecate_thing_type.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8519 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_iot/test_iot_domain_configuration.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9937 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_iot/test_iot_job_executions.py
+-rw-r--r--   0 runner    (1001) docker     (123)    11995 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_iot/test_iot_jobs.py
+-rw-r--r--   0 runner    (1001) docker     (123)    17661 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_iot/test_iot_policies.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1621 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_iot/test_iot_search.py
+-rw-r--r--   0 runner    (1001) docker     (123)    28056 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_iot/test_iot_thing_groups.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3398 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_iot/test_iot_thing_types.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9267 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_iot/test_iot_things.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5634 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_iot/test_iot_topic_rules.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1467 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_iot/test_server.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.588209 moto-4.1.7.dev9/tests/test_iotdata/
+-rw-r--r--   0 runner    (1001) docker     (123)       41 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_iotdata/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6399 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_iotdata/test_iotdata.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1044 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_iotdata/test_server.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.592209 moto-4.1.7.dev9/tests/test_kinesis/
+-rw-r--r--   0 runner    (1001) docker     (123)       41 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_kinesis/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    31019 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_kinesis/test_kinesis.py
+-rw-r--r--   0 runner    (1001) docker     (123)    13043 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_kinesis/test_kinesis_boto3.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5287 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_kinesis/test_kinesis_cloudformation.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2319 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_kinesis/test_kinesis_encryption.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5415 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_kinesis/test_kinesis_monitoring.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5195 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_kinesis/test_kinesis_stream_consumers.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1967 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_kinesis/test_kinesis_stream_limits.py
+-rw-r--r--   0 runner    (1001) docker     (123)      434 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_kinesis/test_server.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.592209 moto-4.1.7.dev9/tests/test_kinesisvideo/
+-rw-r--r--   0 runner    (1001) docker     (123)       41 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_kinesisvideo/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4857 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_kinesisvideo/test_kinesisvideo.py
+-rw-r--r--   0 runner    (1001) docker     (123)      398 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_kinesisvideo/test_server.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.592209 moto-4.1.7.dev9/tests/test_kinesisvideoarchivedmedia/
+-rw-r--r--   0 runner    (1001) docker     (123)       41 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_kinesisvideoarchivedmedia/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2962 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_kinesisvideoarchivedmedia/test_kinesisvideoarchivedmedia.py
+-rw-r--r--   0 runner    (1001) docker     (123)      500 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_kinesisvideoarchivedmedia/test_server.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.596210 moto-4.1.7.dev9/tests/test_kms/
+-rw-r--r--   0 runner    (1001) docker     (123)       41 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_kms/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    45373 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_kms/test_kms_boto3.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6967 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_kms/test_kms_encrypt.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5945 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_kms/test_kms_grants.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4823 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_kms/test_kms_policy_enforcement.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1183 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_kms/test_model.py
+-rw-r--r--   0 runner    (1001) docker     (123)      457 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_kms/test_server.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5468 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_kms/test_utils.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.600210 moto-4.1.7.dev9/tests/test_logs/
+-rw-r--r--   0 runner    (1001) docker     (123)       41 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_logs/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    19409 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_logs/test_integration.py
+-rw-r--r--   0 runner    (1001) docker     (123)    47011 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_logs/test_logs.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7020 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_logs/test_logs_filter.py
+-rw-r--r--   0 runner    (1001) docker     (123)      772 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_logs/test_models.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.600210 moto-4.1.7.dev9/tests/test_managedblockchain/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_managedblockchain/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2411 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_managedblockchain/helpers.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4768 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_managedblockchain/test_managedblockchain_invitations.py
+-rw-r--r--   0 runner    (1001) docker     (123)    25157 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_managedblockchain/test_managedblockchain_members.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4854 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_managedblockchain/test_managedblockchain_networks.py
+-rw-r--r--   0 runner    (1001) docker     (123)    19320 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_managedblockchain/test_managedblockchain_nodes.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7924 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_managedblockchain/test_managedblockchain_proposals.py
+-rw-r--r--   0 runner    (1001) docker     (123)    22370 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_managedblockchain/test_managedblockchain_proposalvotes.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.604210 moto-4.1.7.dev9/tests/test_mediaconnect/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_mediaconnect/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    25048 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_mediaconnect/test_mediaconnect.py
+-rw-r--r--   0 runner    (1001) docker     (123)      435 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_mediaconnect/test_server.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.604210 moto-4.1.7.dev9/tests/test_medialive/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_medialive/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    12296 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_medialive/test_medialive.py
+-rw-r--r--   0 runner    (1001) docker     (123)      702 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_medialive/test_server.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.604210 moto-4.1.7.dev9/tests/test_mediapackage/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_mediapackage/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    10907 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_mediapackage/test_mediapackage.py
+-rw-r--r--   0 runner    (1001) docker     (123)      741 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_mediapackage/test_server.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.604210 moto-4.1.7.dev9/tests/test_mediastore/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_mediastore/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    10137 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_mediastore/test_mediastore.py
+-rw-r--r--   0 runner    (1001) docker     (123)      508 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_mediastore/test_server.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.604210 moto-4.1.7.dev9/tests/test_mediastoredata/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_mediastoredata/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2442 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_mediastoredata/test_mediastoredata.py
+-rw-r--r--   0 runner    (1001) docker     (123)      411 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_mediastoredata/test_server.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.608210 moto-4.1.7.dev9/tests/test_meteringmarketplace/
+-rw-r--r--   0 runner    (1001) docker     (123)     2822 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_meteringmarketplace/test_meteringmarketplace.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.608210 moto-4.1.7.dev9/tests/test_moto_api/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_moto_api/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.608210 moto-4.1.7.dev9/tests/test_moto_api/mock_random/
+-rw-r--r--   0 runner    (1001) docker     (123)     1251 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_moto_api/mock_random/test_mock_random.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.608210 moto-4.1.7.dev9/tests/test_moto_api/recorder/
+-rw-r--r--   0 runner    (1001) docker     (123)    10193 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_moto_api/recorder/test_recorder.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.608210 moto-4.1.7.dev9/tests/test_moto_api/state_manager/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_moto_api/state_manager/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.608210 moto-4.1.7.dev9/tests/test_moto_api/state_manager/servermode/
+-rw-r--r--   0 runner    (1001) docker     (123)     1990 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_moto_api/state_manager/servermode/test_inmemory_server.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1992 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_moto_api/state_manager/servermode/test_state_manager.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1755 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_moto_api/state_manager/test_batch_integration.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4137 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_moto_api/state_manager/test_managed_state_model.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2067 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_moto_api/state_manager/test_state_manager.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.612210 moto-4.1.7.dev9/tests/test_mq/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_mq/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    14031 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_mq/test_mq.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7095 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_mq/test_mq_configuration.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3255 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_mq/test_mq_tags.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5234 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_mq/test_mq_users.py
+-rw-r--r--   0 runner    (1001) docker     (123)      382 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_mq/test_server.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.612210 moto-4.1.7.dev9/tests/test_neptune/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_neptune/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      842 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_neptune/test_cluster_options.py
+-rw-r--r--   0 runner    (1001) docker     (123)      837 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_neptune/test_cluster_tags.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4530 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_neptune/test_clusters.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1989 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_neptune/test_global_clusters.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.612210 moto-4.1.7.dev9/tests/test_opensearch/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_opensearch/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      978 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_opensearch/test_domain_tags.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4806 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_opensearch/test_opensearch.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.616210 moto-4.1.7.dev9/tests/test_opsworks/
+-rw-r--r--   0 runner    (1001) docker     (123)       41 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_opsworks/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2433 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_opsworks/test_apps.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7770 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_opsworks/test_instances.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3019 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_opsworks/test_layers.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1403 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_opsworks/test_stack.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.616210 moto-4.1.7.dev9/tests/test_organizations/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_organizations/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4891 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_organizations/organizations_test_utils.py
+-rw-r--r--   0 runner    (1001) docker     (123)    85363 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_organizations/test_organizations_boto3.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.616210 moto-4.1.7.dev9/tests/test_personalize/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_personalize/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4221 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_personalize/test_personalize_schema.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.620211 moto-4.1.7.dev9/tests/test_pinpoint/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_pinpoint/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4883 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_pinpoint/test_pinpoint.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2288 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_pinpoint/test_pinpoint_application_tags.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2884 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_pinpoint/test_pinpoint_event_stream.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.620211 moto-4.1.7.dev9/tests/test_polly/
+-rw-r--r--   0 runner    (1001) docker     (123)       41 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_polly/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7974 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_polly/test_polly.py
+-rw-r--r--   0 runner    (1001) docker     (123)      362 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_polly/test_server.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.620211 moto-4.1.7.dev9/tests/test_quicksight/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_quicksight/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2209 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_quicksight/test_quicksight_datasets.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4647 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_quicksight/test_quicksight_groups.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9343 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_quicksight/test_quicksight_users.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.620211 moto-4.1.7.dev9/tests/test_ram/
+-rw-r--r--   0 runner    (1001) docker     (123)    12819 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_ram/test_ram.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.624211 moto-4.1.7.dev9/tests/test_rds/
+-rw-r--r--   0 runner    (1001) docker     (123)       41 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_rds/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    16282 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_rds/test_filters.py
+-rw-r--r--   0 runner    (1001) docker     (123)    91218 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_rds/test_rds.py
+-rw-r--r--   0 runner    (1001) docker     (123)    11124 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_rds/test_rds_cloudformation.py
+-rw-r--r--   0 runner    (1001) docker     (123)    28931 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_rds/test_rds_clusters.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4572 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_rds/test_rds_event_subscriptions.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5229 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_rds/test_rds_export_tasks.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1194 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_rds/test_server.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7876 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_rds/test_utils.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.624211 moto-4.1.7.dev9/tests/test_redshift/
+-rw-r--r--   0 runner    (1001) docker     (123)       41 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_redshift/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    73309 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_redshift/test_redshift.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2095 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_redshift/test_redshift_cloudformation.py
+-rw-r--r--   0 runner    (1001) docker     (123)    12934 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_redshift/test_server.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.628211 moto-4.1.7.dev9/tests/test_redshiftdata/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_redshiftdata/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5862 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_redshiftdata/test_redshiftdata.py
+-rw-r--r--   0 runner    (1001) docker     (123)      170 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_redshiftdata/test_redshiftdata_constants.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7504 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_redshiftdata/test_server.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.628211 moto-4.1.7.dev9/tests/test_rekognition/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_rekognition/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2174 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_rekognition/test_rekognition.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.628211 moto-4.1.7.dev9/tests/test_resourcegroups/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_resourcegroups/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8608 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_resourcegroups/test_resourcegroups.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.628211 moto-4.1.7.dev9/tests/test_resourcegroupstaggingapi/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_resourcegroupstaggingapi/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    24449 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_resourcegroupstaggingapi/test_resourcegroupstaggingapi.py
+-rw-r--r--   0 runner    (1001) docker     (123)      579 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_resourcegroupstaggingapi/test_server.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.628211 moto-4.1.7.dev9/tests/test_route53/
+-rw-r--r--   0 runner    (1001) docker     (123)       41 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_route53/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1642 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_route53/test_change_set_model.py
+-rw-r--r--   0 runner    (1001) docker     (123)    52862 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_route53/test_route53.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8233 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_route53/test_route53_cloudformation.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4160 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_route53/test_route53_delegationsets.py
+-rw-r--r--   0 runner    (1001) docker     (123)    10027 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_route53/test_route53_healthchecks.py
+-rw-r--r--   0 runner    (1001) docker     (123)    11544 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_route53/test_route53_query_logging_config.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9418 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_route53/test_route53_vpcs.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1555 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_route53/test_server.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.632211 moto-4.1.7.dev9/tests/test_route53resolver/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_route53resolver/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    40356 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_route53resolver/test_route53resolver_endpoint.py
+-rw-r--r--   0 runner    (1001) docker     (123)    21968 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_route53resolver/test_route53resolver_rule.py
+-rw-r--r--   0 runner    (1001) docker     (123)    17448 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_route53resolver/test_route53resolver_rule_associations.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5579 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_route53resolver/test_route53resolver_tags.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.636211 moto-4.1.7.dev9/tests/test_s3/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_s3/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1782 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_s3/test_multiple_accounts_server.py
+-rw-r--r--   0 runner    (1001) docker     (123)   114284 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_s3/test_s3.py
+-rw-r--r--   0 runner    (1001) docker     (123)    11268 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_s3/test_s3_acl.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7102 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_s3/test_s3_auth.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4800 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_s3/test_s3_bucket_policy.py
+-rw-r--r--   0 runner    (1001) docker     (123)      513 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_s3/test_s3_classdecorator.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7924 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_s3/test_s3_cloudformation.py
+-rw-r--r--   0 runner    (1001) docker     (123)    18825 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_s3/test_s3_config.py
+-rw-r--r--   0 runner    (1001) docker     (123)    12874 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_s3/test_s3_copyobject.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3532 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_s3/test_s3_custom_endpoint.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4423 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_s3/test_s3_encryption.py
+-rw-r--r--   0 runner    (1001) docker     (123)    10625 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_s3/test_s3_file_handles.py
+-rw-r--r--   0 runner    (1001) docker     (123)    10568 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_s3/test_s3_lambda_integration.py
+-rw-r--r--   0 runner    (1001) docker     (123)    19473 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_s3/test_s3_lifecycle.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5944 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_s3/test_s3_lock.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9265 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_s3/test_s3_logging.py
+-rw-r--r--   0 runner    (1001) docker     (123)      757 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_s3/test_s3_metadata.py
+-rw-r--r--   0 runner    (1001) docker     (123)    31026 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_s3/test_s3_multipart.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4071 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_s3/test_s3_object_attributes.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1605 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_s3/test_s3_ownership.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5935 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_s3/test_s3_replication.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4172 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_s3/test_s3_select.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8580 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_s3/test_s3_storageclass.py
+-rw-r--r--   0 runner    (1001) docker     (123)    14479 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_s3/test_s3_tagging.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4745 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_s3/test_s3_utils.py
+-rw-r--r--   0 runner    (1001) docker     (123)    12808 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_s3/test_server.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.636211 moto-4.1.7.dev9/tests/test_s3bucket_path/
+-rw-r--r--   0 runner    (1001) docker     (123)       41 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_s3bucket_path/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      447 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_s3bucket_path/test_s3bucket_path_utils.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3310 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_s3bucket_path/test_server.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.636211 moto-4.1.7.dev9/tests/test_s3control/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_s3control/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2794 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_s3control/test_s3control.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3980 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_s3control/test_s3control_access_points.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3591 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_s3control/test_s3control_accesspoint_policy.py
+-rw-r--r--   0 runner    (1001) docker     (123)    11881 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_s3control/test_s3control_config_integration.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3490 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_s3control/test_s3control_s3.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.640211 moto-4.1.7.dev9/tests/test_sagemaker/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_sagemaker/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9953 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_sagemaker/cloudformation_test_configs.py
+-rw-r--r--   0 runner    (1001) docker     (123)    15041 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_sagemaker/test_sagemaker_cloudformation.py
+-rw-r--r--   0 runner    (1001) docker     (123)    20469 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_sagemaker/test_sagemaker_endpoint.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3162 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_sagemaker/test_sagemaker_experiment.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4816 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_sagemaker/test_sagemaker_models.py
+-rw-r--r--   0 runner    (1001) docker     (123)    11569 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_sagemaker/test_sagemaker_notebooks.py
+-rw-r--r--   0 runner    (1001) docker     (123)    24758 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_sagemaker/test_sagemaker_pipeline.py
+-rw-r--r--   0 runner    (1001) docker     (123)    14930 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_sagemaker/test_sagemaker_processing.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3810 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_sagemaker/test_sagemaker_search.py
+-rw-r--r--   0 runner    (1001) docker     (123)    17756 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_sagemaker/test_sagemaker_training.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5338 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_sagemaker/test_sagemaker_trial.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8415 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_sagemaker/test_sagemaker_trial_component.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.640211 moto-4.1.7.dev9/tests/test_sdb/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_sdb/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5412 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_sdb/test_sdb_attributes.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2113 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_sdb/test_sdb_domains.py
+-rw-r--r--   0 runner    (1001) docker     (123)      427 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_sdb/test_server.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.640211 moto-4.1.7.dev9/tests/test_secretsmanager/
+-rw-r--r--   0 runner    (1001) docker     (123)       41 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_secretsmanager/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9122 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_secretsmanager/test_list_secrets.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2511 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_secretsmanager/test_policy.py
+-rw-r--r--   0 runner    (1001) docker     (123)    57270 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_secretsmanager/test_secretsmanager.py
+-rw-r--r--   0 runner    (1001) docker     (123)    33144 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_secretsmanager/test_server.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.648212 moto-4.1.7.dev9/tests/test_servicediscovery/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_servicediscovery/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      456 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_servicediscovery/test_server.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8790 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_servicediscovery/test_servicediscovery_httpnamespaces.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4712 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_servicediscovery/test_servicediscovery_operations.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7657 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_servicediscovery/test_servicediscovery_service.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3419 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_servicediscovery/test_servicediscovery_tags.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.648212 moto-4.1.7.dev9/tests/test_servicequotas/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_servicequotas/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2728 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_servicequotas/test_servicequotas.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.648212 moto-4.1.7.dev9/tests/test_ses/
+-rw-r--r--   0 runner    (1001) docker     (123)       41 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_ses/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      855 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_ses/test_server.py
+-rw-r--r--   0 runner    (1001) docker     (123)    52328 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_ses/test_ses_boto3.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6107 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_ses/test_ses_sns_boto3.py
+-rw-r--r--   0 runner    (1001) docker     (123)      435 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_ses/test_ses_utils.py
+-rw-r--r--   0 runner    (1001) docker     (123)      958 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_ses/test_templating.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.648212 moto-4.1.7.dev9/tests/test_signer/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_signer/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      684 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_signer/test_signing_platforms.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2261 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_signer/test_signing_profiles.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.652212 moto-4.1.7.dev9/tests/test_sns/
+-rw-r--r--   0 runner    (1001) docker     (123)       41 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_sns/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    13714 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_sns/test_application_boto3.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6321 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_sns/test_publish_batch.py
+-rw-r--r--   0 runner    (1001) docker     (123)    42805 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_sns/test_publishing_boto3.py
+-rw-r--r--   0 runner    (1001) docker     (123)      761 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_sns/test_server.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6161 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_sns/test_sns_cloudformation.py
+-rw-r--r--   0 runner    (1001) docker     (123)    19367 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_sns/test_subscriptions_boto3.py
+-rw-r--r--   0 runner    (1001) docker     (123)    21472 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_sns/test_topics_boto3.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.652212 moto-4.1.7.dev9/tests/test_special_cases/
+-rw-r--r--   0 runner    (1001) docker     (123)     2293 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_special_cases/test_custom_amis.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.652212 moto-4.1.7.dev9/tests/test_sqs/
+-rw-r--r--   0 runner    (1001) docker     (123)       41 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_sqs/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3210 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_sqs/test_server.py
+-rw-r--r--   0 runner    (1001) docker     (123)   108705 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_sqs/test_sqs.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7836 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_sqs/test_sqs_cloudformation.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4419 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_sqs/test_sqs_integration.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1266 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_sqs/test_sqs_multiaccount.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.656212 moto-4.1.7.dev9/tests/test_ssm/
+-rw-r--r--   0 runner    (1001) docker     (123)       41 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_ssm/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    71927 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_ssm/test_ssm_boto3.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2109 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_ssm/test_ssm_cloudformation.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1122 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_ssm/test_ssm_default_amis.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1476 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_ssm/test_ssm_defaults.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6621 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_ssm/test_ssm_doc_permissions.py
+-rw-r--r--   0 runner    (1001) docker     (123)    28425 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_ssm/test_ssm_docs.py
+-rw-r--r--   0 runner    (1001) docker     (123)      499 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_ssm/test_ssm_ec2_integration.py
+-rw-r--r--   0 runner    (1001) docker     (123)      655 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_ssm/test_ssm_ecs_images.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5334 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_ssm/test_ssm_maintenance_windows.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2807 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_ssm/test_ssm_parameterstore.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4747 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_ssm/test_ssm_secretsmanager.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3134 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_ssm/test_ssm_utils.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.656212 moto-4.1.7.dev9/tests/test_ssm/test_templates/
+-rw-r--r--   0 runner    (1001) docker     (123)     1047 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_ssm/test_templates/good.yaml
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.656212 moto-4.1.7.dev9/tests/test_ssoadmin/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_ssoadmin/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      866 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_ssoadmin/test_server.py
+-rw-r--r--   0 runner    (1001) docker     (123)    13607 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_ssoadmin/test_ssoadmin.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.656212 moto-4.1.7.dev9/tests/test_stepfunctions/
+-rw-r--r--   0 runner    (1001) docker     (123)       41 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_stepfunctions/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    34000 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_stepfunctions/test_stepfunctions.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9078 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_stepfunctions/test_stepfunctions_cloudformation.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.656212 moto-4.1.7.dev9/tests/test_sts/
+-rw-r--r--   0 runner    (1001) docker     (123)       41 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_sts/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1501 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_sts/test_server.py
+-rw-r--r--   0 runner    (1001) docker     (123)    33741 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_sts/test_sts.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8506 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_sts/test_sts_integration.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.656212 moto-4.1.7.dev9/tests/test_support/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_support/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1866 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_support/test_server.py
+-rw-r--r--   0 runner    (1001) docker     (123)    24299 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_support/test_support.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.660212 moto-4.1.7.dev9/tests/test_swf/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_swf/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.660212 moto-4.1.7.dev9/tests/test_swf/models/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_swf/models/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5333 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_swf/models/test_activity_task.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2452 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_swf/models/test_decision_task.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4296 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_swf/models/test_domain.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1925 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_swf/models/test_generic_type.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1004 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_swf/models/test_history_event.py
+-rw-r--r--   0 runner    (1001) docker     (123)      539 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_swf/models/test_timeout.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1187 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_swf/models/test_timer.py
+-rw-r--r--   0 runner    (1001) docker     (123)    25245 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_swf/models/test_workflow_execution.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.660212 moto-4.1.7.dev9/tests/test_swf/responses/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_swf/responses/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    10547 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_swf/responses/test_activity_tasks.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9946 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_swf/responses/test_activity_types.py
+-rw-r--r--   0 runner    (1001) docker     (123)    21702 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_swf/responses/test_decision_tasks.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7574 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_swf/responses/test_domains.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5841 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_swf/responses/test_timeouts.py
+-rw-r--r--   0 runner    (1001) docker     (123)    13819 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_swf/responses/test_workflow_executions.py
+-rw-r--r--   0 runner    (1001) docker     (123)    10319 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_swf/responses/test_workflow_types.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5190 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_swf/test_exceptions.py
+-rw-r--r--   0 runner    (1001) docker     (123)      293 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_swf/test_utils.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3875 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_swf/utils.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.664212 moto-4.1.7.dev9/tests/test_textract/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_textract/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3011 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_textract/test_server.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2993 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_textract/test_textract.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.664212 moto-4.1.7.dev9/tests/test_timestreamwrite/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_timestreamwrite/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      514 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_timestreamwrite/test_server.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4386 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_timestreamwrite/test_timestreamwrite_database.py
+-rw-r--r--   0 runner    (1001) docker     (123)    11135 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_timestreamwrite/test_timestreamwrite_table.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2866 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_timestreamwrite/test_timestreamwrite_tagging.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.664212 moto-4.1.7.dev9/tests/test_transcribe/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_transcribe/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    42714 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_transcribe/test_transcribe_boto3.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.664212 moto-4.1.7.dev9/tests/test_utilities/
+-rw-r--r--   0 runner    (1001) docker     (123)     1058 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_utilities/test_docker_utilities.py
+-rw-r--r--   0 runner    (1001) docker     (123)    10316 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_utilities/test_paginator.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6764 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_utilities/test_tagging_service.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3562 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_utilities/test_threaded_server.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.668212 moto-4.1.7.dev9/tests/test_wafv2/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_wafv2/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      400 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_wafv2/test_helper_functions.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2793 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_wafv2/test_server.py
+-rw-r--r--   0 runner    (1001) docker     (123)      614 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_wafv2/test_utils.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7288 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_wafv2/test_wafv2.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3506 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_wafv2/test_wafv2_integration.py
+-rw-r--r--   0 runner    (1001) docker     (123)      249 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_wafv2/test_wafv2_rules.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2600 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_wafv2/test_wafv2_tags.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 19:15:35.668212 moto-4.1.7.dev9/tests/test_xray/
+-rw-r--r--   0 runner    (1001) docker     (123)       41 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_xray/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4143 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_xray/test_xray_boto3.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4990 2023-03-28 19:15:25.000000 moto-4.1.7.dev9/tests/test_xray/test_xray_client.py
```

### Comparing `moto-4.1.7.dev8/AUTHORS.md` & `moto-4.1.7.dev9/AUTHORS.md`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/LICENSE` & `moto-4.1.7.dev9/LICENSE`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/MANIFEST.in` & `moto-4.1.7.dev9/MANIFEST.in`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/PKG-INFO` & `moto-4.1.7.dev9/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: moto
-Version: 4.1.7.dev8
+Version: 4.1.7.dev9
 Home-page: https://github.com/getmoto/moto
 Author: Steve Pulec
 Author-email: "spulec@gmail.com"
 License: Apache License 2.0
 Project-URL: Documentation, http://docs.getmoto.org/en/latest/
 Project-URL: Issue tracker, https://github.com/getmoto/moto/issues
 Project-URL: Changelog, https://github.com/getmoto/moto/blob/master/CHANGELOG.md
```

### Comparing `moto-4.1.7.dev8/README.md` & `moto-4.1.7.dev9/README.md`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/__init__.py` & `moto-4.1.7.dev9/moto/__init__.py`

 * *Files 0% similar despite different names*

```diff
@@ -188,15 +188,15 @@
 
 mock_all = MockAll
 
 # import logging
 # logging.getLogger('boto').setLevel(logging.CRITICAL)
 
 __title__ = "moto"
-__version__ = "4.1.7.dev8"
+__version__ = "4.1.7.dev9"
 
 
 try:
     # Need to monkey-patch botocore requests back to underlying urllib3 classes
     from botocore.awsrequest import (
         HTTPSConnectionPool,
         HTTPConnectionPool,
```

### Comparing `moto-4.1.7.dev8/moto/acm/models.py` & `moto-4.1.7.dev9/moto/acm/models.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/acm/responses.py` & `moto-4.1.7.dev9/moto/acm/responses.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/acmpca/models.py` & `moto-4.1.7.dev9/moto/acmpca/models.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/acmpca/responses.py` & `moto-4.1.7.dev9/moto/acmpca/responses.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/amp/exceptions.py` & `moto-4.1.7.dev9/moto/amp/exceptions.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/amp/models.py` & `moto-4.1.7.dev9/moto/amp/models.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/amp/responses.py` & `moto-4.1.7.dev9/moto/amp/responses.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/amp/urls.py` & `moto-4.1.7.dev9/moto/amp/urls.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/apigateway/exceptions.py` & `moto-4.1.7.dev9/moto/apigateway/exceptions.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/apigateway/integration_parsers/aws_parser.py` & `moto-4.1.7.dev9/moto/apigateway/integration_parsers/aws_parser.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/apigateway/integration_parsers/http_parser.py` & `moto-4.1.7.dev9/moto/apigateway/integration_parsers/http_parser.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/apigateway/models.py` & `moto-4.1.7.dev9/moto/apigateway/models.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/apigateway/responses.py` & `moto-4.1.7.dev9/moto/apigateway/responses.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/apigateway/urls.py` & `moto-4.1.7.dev9/moto/apigateway/urls.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/apigateway/utils.py` & `moto-4.1.7.dev9/moto/apigateway/utils.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/apigatewayv2/exceptions.py` & `moto-4.1.7.dev9/moto/apigatewayv2/exceptions.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/apigatewayv2/models.py` & `moto-4.1.7.dev9/moto/apigatewayv2/models.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/apigatewayv2/responses.py` & `moto-4.1.7.dev9/moto/apigatewayv2/responses.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/apigatewayv2/urls.py` & `moto-4.1.7.dev9/moto/apigatewayv2/urls.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/applicationautoscaling/models.py` & `moto-4.1.7.dev9/moto/applicationautoscaling/models.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/applicationautoscaling/responses.py` & `moto-4.1.7.dev9/moto/applicationautoscaling/responses.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/appsync/models.py` & `moto-4.1.7.dev9/moto/appsync/models.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/appsync/responses.py` & `moto-4.1.7.dev9/moto/appsync/responses.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/appsync/urls.py` & `moto-4.1.7.dev9/moto/appsync/urls.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/athena/exceptions.py` & `moto-4.1.7.dev9/moto/athena/exceptions.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/athena/models.py` & `moto-4.1.7.dev9/moto/athena/models.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/athena/responses.py` & `moto-4.1.7.dev9/moto/athena/responses.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/autoscaling/exceptions.py` & `moto-4.1.7.dev9/moto/autoscaling/exceptions.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/autoscaling/models.py` & `moto-4.1.7.dev9/moto/autoscaling/models.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/autoscaling/responses.py` & `moto-4.1.7.dev9/moto/autoscaling/responses.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/awslambda/exceptions.py` & `moto-4.1.7.dev9/moto/awslambda/exceptions.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/awslambda/models.py` & `moto-4.1.7.dev9/moto/awslambda/models.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/awslambda/policy.py` & `moto-4.1.7.dev9/moto/awslambda/policy.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/awslambda/responses.py` & `moto-4.1.7.dev9/moto/awslambda/responses.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/awslambda/urls.py` & `moto-4.1.7.dev9/moto/awslambda/urls.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/awslambda/utils.py` & `moto-4.1.7.dev9/moto/awslambda/utils.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/backend_index.py` & `moto-4.1.7.dev9/moto/backend_index.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/backends.py` & `moto-4.1.7.dev9/moto/backends.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/batch/models.py` & `moto-4.1.7.dev9/moto/batch/models.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/batch/responses.py` & `moto-4.1.7.dev9/moto/batch/responses.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/batch/urls.py` & `moto-4.1.7.dev9/moto/batch/urls.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/batch/utils.py` & `moto-4.1.7.dev9/moto/batch/utils.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/batch_simple/models.py` & `moto-4.1.7.dev9/moto/batch_simple/models.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/budgets/exceptions.py` & `moto-4.1.7.dev9/moto/budgets/exceptions.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/budgets/models.py` & `moto-4.1.7.dev9/moto/budgets/models.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/budgets/responses.py` & `moto-4.1.7.dev9/moto/budgets/responses.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ce/models.py` & `moto-4.1.7.dev9/moto/ce/models.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ce/responses.py` & `moto-4.1.7.dev9/moto/ce/responses.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/cloudformation/custom_model.py` & `moto-4.1.7.dev9/moto/cloudformation/custom_model.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/cloudformation/exceptions.py` & `moto-4.1.7.dev9/moto/cloudformation/exceptions.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/cloudformation/models.py` & `moto-4.1.7.dev9/moto/cloudformation/models.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/cloudformation/parsing.py` & `moto-4.1.7.dev9/moto/cloudformation/parsing.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/cloudformation/responses.py` & `moto-4.1.7.dev9/moto/cloudformation/responses.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/cloudformation/utils.py` & `moto-4.1.7.dev9/moto/cloudformation/utils.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/cloudfront/exceptions.py` & `moto-4.1.7.dev9/moto/cloudfront/exceptions.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/cloudfront/models.py` & `moto-4.1.7.dev9/moto/cloudfront/models.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/cloudfront/responses.py` & `moto-4.1.7.dev9/moto/cloudfront/responses.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/cloudfront/urls.py` & `moto-4.1.7.dev9/moto/cloudfront/urls.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/cloudtrail/exceptions.py` & `moto-4.1.7.dev9/moto/cloudtrail/exceptions.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/cloudtrail/models.py` & `moto-4.1.7.dev9/moto/cloudtrail/models.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/cloudtrail/responses.py` & `moto-4.1.7.dev9/moto/cloudtrail/responses.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/cloudwatch/exceptions.py` & `moto-4.1.7.dev9/moto/cloudwatch/exceptions.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/cloudwatch/models.py` & `moto-4.1.7.dev9/moto/cloudwatch/models.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/cloudwatch/responses.py` & `moto-4.1.7.dev9/moto/cloudwatch/responses.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/codebuild/exceptions.py` & `moto-4.1.7.dev9/moto/codebuild/exceptions.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/codebuild/models.py` & `moto-4.1.7.dev9/moto/codebuild/models.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/codebuild/responses.py` & `moto-4.1.7.dev9/moto/codebuild/responses.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/codecommit/exceptions.py` & `moto-4.1.7.dev9/moto/codecommit/exceptions.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/codecommit/models.py` & `moto-4.1.7.dev9/moto/codecommit/models.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/codecommit/responses.py` & `moto-4.1.7.dev9/moto/codecommit/responses.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/codepipeline/exceptions.py` & `moto-4.1.7.dev9/moto/codepipeline/exceptions.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/codepipeline/models.py` & `moto-4.1.7.dev9/moto/codepipeline/models.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/codepipeline/responses.py` & `moto-4.1.7.dev9/moto/codepipeline/responses.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/cognitoidentity/exceptions.py` & `moto-4.1.7.dev9/moto/cognitoidentity/exceptions.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/cognitoidentity/models.py` & `moto-4.1.7.dev9/moto/cognitoidentity/models.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/cognitoidentity/responses.py` & `moto-4.1.7.dev9/moto/cognitoidentity/responses.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/cognitoidp/exceptions.py` & `moto-4.1.7.dev9/moto/cognitoidp/exceptions.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/cognitoidp/models.py` & `moto-4.1.7.dev9/moto/cognitoidp/models.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/cognitoidp/resources/jwks-private.json` & `moto-4.1.7.dev9/moto/cognitoidp/resources/jwks-private.json`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/cognitoidp/responses.py` & `moto-4.1.7.dev9/moto/cognitoidp/responses.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/cognitoidp/utils.py` & `moto-4.1.7.dev9/moto/cognitoidp/utils.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/comprehend/models.py` & `moto-4.1.7.dev9/moto/comprehend/models.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/comprehend/responses.py` & `moto-4.1.7.dev9/moto/comprehend/responses.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/config/exceptions.py` & `moto-4.1.7.dev9/moto/config/exceptions.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/config/models.py` & `moto-4.1.7.dev9/moto/config/models.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/config/resources/aws_managed_rules.json` & `moto-4.1.7.dev9/moto/config/resources/aws_managed_rules.json`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/config/responses.py` & `moto-4.1.7.dev9/moto/config/responses.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/core/base_backend.py` & `moto-4.1.7.dev9/moto/core/base_backend.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/core/botocore_stubber.py` & `moto-4.1.7.dev9/moto/core/botocore_stubber.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/core/common_models.py` & `moto-4.1.7.dev9/moto/core/common_models.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/core/custom_responses_mock.py` & `moto-4.1.7.dev9/moto/core/custom_responses_mock.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/core/exceptions.py` & `moto-4.1.7.dev9/moto/core/exceptions.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/core/models.py` & `moto-4.1.7.dev9/moto/core/models.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/core/responses.py` & `moto-4.1.7.dev9/moto/core/responses.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/core/responses_custom_registry.py` & `moto-4.1.7.dev9/moto/core/responses_custom_registry.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/core/utils.py` & `moto-4.1.7.dev9/moto/core/utils.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/databrew/exceptions.py` & `moto-4.1.7.dev9/moto/databrew/exceptions.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/databrew/models.py` & `moto-4.1.7.dev9/moto/databrew/models.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/databrew/responses.py` & `moto-4.1.7.dev9/moto/databrew/responses.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/databrew/urls.py` & `moto-4.1.7.dev9/moto/databrew/urls.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/datapipeline/models.py` & `moto-4.1.7.dev9/moto/datapipeline/models.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/datapipeline/responses.py` & `moto-4.1.7.dev9/moto/datapipeline/responses.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/datapipeline/utils.py` & `moto-4.1.7.dev9/moto/datapipeline/utils.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/datasync/models.py` & `moto-4.1.7.dev9/moto/datasync/models.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/datasync/responses.py` & `moto-4.1.7.dev9/moto/datasync/responses.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/dax/exceptions.py` & `moto-4.1.7.dev9/moto/dax/exceptions.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/dax/models.py` & `moto-4.1.7.dev9/moto/dax/models.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/dax/responses.py` & `moto-4.1.7.dev9/moto/dax/responses.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/dms/exceptions.py` & `moto-4.1.7.dev9/moto/dms/exceptions.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/dms/models.py` & `moto-4.1.7.dev9/moto/dms/models.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/dms/responses.py` & `moto-4.1.7.dev9/moto/dms/responses.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/dms/utils.py` & `moto-4.1.7.dev9/moto/dms/utils.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ds/exceptions.py` & `moto-4.1.7.dev9/moto/ds/exceptions.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ds/models.py` & `moto-4.1.7.dev9/moto/ds/models.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ds/responses.py` & `moto-4.1.7.dev9/moto/ds/responses.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ds/validations.py` & `moto-4.1.7.dev9/moto/ds/validations.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/dynamodb/comparisons.py` & `moto-4.1.7.dev9/moto/dynamodb/comparisons.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/dynamodb/exceptions.py` & `moto-4.1.7.dev9/moto/dynamodb/exceptions.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/dynamodb/models/__init__.py` & `moto-4.1.7.dev9/moto/dynamodb/models/__init__.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/dynamodb/models/dynamo_type.py` & `moto-4.1.7.dev9/moto/dynamodb/models/dynamo_type.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/dynamodb/models/table.py` & `moto-4.1.7.dev9/moto/dynamodb/models/table.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/dynamodb/parsing/ast_nodes.py` & `moto-4.1.7.dev9/moto/dynamodb/parsing/ast_nodes.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/dynamodb/parsing/executors.py` & `moto-4.1.7.dev9/moto/dynamodb/parsing/executors.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/dynamodb/parsing/expressions.py` & `moto-4.1.7.dev9/moto/dynamodb/parsing/expressions.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/dynamodb/parsing/key_condition_expression.py` & `moto-4.1.7.dev9/moto/dynamodb/parsing/key_condition_expression.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/dynamodb/parsing/reserved_keywords.py` & `moto-4.1.7.dev9/moto/dynamodb/parsing/reserved_keywords.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/dynamodb/parsing/reserved_keywords.txt` & `moto-4.1.7.dev9/moto/dynamodb/parsing/reserved_keywords.txt`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/dynamodb/parsing/tokens.py` & `moto-4.1.7.dev9/moto/dynamodb/parsing/tokens.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/dynamodb/parsing/validators.py` & `moto-4.1.7.dev9/moto/dynamodb/parsing/validators.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/dynamodb/responses.py` & `moto-4.1.7.dev9/moto/dynamodb/responses.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/dynamodb_v20111205/comparisons.py` & `moto-4.1.7.dev9/moto/dynamodb_v20111205/comparisons.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/dynamodb_v20111205/models.py` & `moto-4.1.7.dev9/moto/dynamodb_v20111205/models.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/dynamodb_v20111205/responses.py` & `moto-4.1.7.dev9/moto/dynamodb_v20111205/responses.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/dynamodbstreams/models.py` & `moto-4.1.7.dev9/moto/dynamodbstreams/models.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/dynamodbstreams/responses.py` & `moto-4.1.7.dev9/moto/dynamodbstreams/responses.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ebs/models.py` & `moto-4.1.7.dev9/moto/ebs/models.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ebs/responses.py` & `moto-4.1.7.dev9/moto/ebs/responses.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ebs/urls.py` & `moto-4.1.7.dev9/moto/ebs/urls.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ec2/exceptions.py` & `moto-4.1.7.dev9/moto/ec2/exceptions.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ec2/models/__init__.py` & `moto-4.1.7.dev9/moto/ec2/models/__init__.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ec2/models/amis.py` & `moto-4.1.7.dev9/moto/ec2/models/amis.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ec2/models/availability_zones_and_regions.py` & `moto-4.1.7.dev9/moto/ec2/models/availability_zones_and_regions.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ec2/models/carrier_gateways.py` & `moto-4.1.7.dev9/moto/ec2/models/carrier_gateways.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ec2/models/core.py` & `moto-4.1.7.dev9/moto/ec2/models/core.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ec2/models/customer_gateways.py` & `moto-4.1.7.dev9/moto/ec2/models/customer_gateways.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ec2/models/dhcp_options.py` & `moto-4.1.7.dev9/moto/ec2/models/dhcp_options.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ec2/models/elastic_block_store.py` & `moto-4.1.7.dev9/moto/ec2/models/elastic_block_store.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ec2/models/elastic_ip_addresses.py` & `moto-4.1.7.dev9/moto/ec2/models/elastic_ip_addresses.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ec2/models/elastic_network_interfaces.py` & `moto-4.1.7.dev9/moto/ec2/models/elastic_network_interfaces.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ec2/models/fleets.py` & `moto-4.1.7.dev9/moto/ec2/models/fleets.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ec2/models/flow_logs.py` & `moto-4.1.7.dev9/moto/ec2/models/flow_logs.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ec2/models/hosts.py` & `moto-4.1.7.dev9/moto/ec2/models/hosts.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ec2/models/iam_instance_profile.py` & `moto-4.1.7.dev9/moto/ec2/models/iam_instance_profile.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ec2/models/instance_types.py` & `moto-4.1.7.dev9/moto/ec2/models/instance_types.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ec2/models/instances.py` & `moto-4.1.7.dev9/moto/ec2/models/instances.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ec2/models/internet_gateways.py` & `moto-4.1.7.dev9/moto/ec2/models/internet_gateways.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ec2/models/key_pairs.py` & `moto-4.1.7.dev9/moto/ec2/models/key_pairs.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ec2/models/launch_templates.py` & `moto-4.1.7.dev9/moto/ec2/models/launch_templates.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ec2/models/managed_prefixes.py` & `moto-4.1.7.dev9/moto/ec2/models/managed_prefixes.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ec2/models/nat_gateways.py` & `moto-4.1.7.dev9/moto/ec2/models/nat_gateways.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ec2/models/network_acls.py` & `moto-4.1.7.dev9/moto/ec2/models/network_acls.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ec2/models/route_tables.py` & `moto-4.1.7.dev9/moto/ec2/models/route_tables.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ec2/models/security_groups.py` & `moto-4.1.7.dev9/moto/ec2/models/security_groups.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ec2/models/spot_requests.py` & `moto-4.1.7.dev9/moto/ec2/models/spot_requests.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ec2/models/subnets.py` & `moto-4.1.7.dev9/moto/ec2/models/subnets.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ec2/models/tags.py` & `moto-4.1.7.dev9/moto/ec2/models/tags.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ec2/models/transit_gateway.py` & `moto-4.1.7.dev9/moto/ec2/models/transit_gateway.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ec2/models/transit_gateway_attachments.py` & `moto-4.1.7.dev9/moto/ec2/models/transit_gateway_attachments.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ec2/models/transit_gateway_route_tables.py` & `moto-4.1.7.dev9/moto/ec2/models/transit_gateway_route_tables.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ec2/models/vpc_peering_connections.py` & `moto-4.1.7.dev9/moto/ec2/models/vpc_peering_connections.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ec2/models/vpc_service_configuration.py` & `moto-4.1.7.dev9/moto/ec2/models/vpc_service_configuration.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ec2/models/vpcs.py` & `moto-4.1.7.dev9/moto/ec2/models/vpcs.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ec2/models/vpn_connections.py` & `moto-4.1.7.dev9/moto/ec2/models/vpn_connections.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ec2/models/vpn_gateway.py` & `moto-4.1.7.dev9/moto/ec2/models/vpn_gateway.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ec2/resources/amis.json` & `moto-4.1.7.dev9/moto/ec2/resources/amis.json`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ec2/resources/ecs/optimized_amis/af-south-1.json` & `moto-4.1.7.dev9/moto/ec2/resources/ecs/optimized_amis/af-south-1.json`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ec2/resources/ecs/optimized_amis/ap-east-1.json` & `moto-4.1.7.dev9/moto/ec2/resources/ecs/optimized_amis/ap-east-1.json`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ec2/resources/ecs/optimized_amis/ap-northeast-1.json` & `moto-4.1.7.dev9/moto/ec2/resources/ecs/optimized_amis/ap-northeast-1.json`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ec2/resources/ecs/optimized_amis/ap-northeast-2.json` & `moto-4.1.7.dev9/moto/ec2/resources/ecs/optimized_amis/ap-northeast-2.json`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ec2/resources/ecs/optimized_amis/ap-northeast-3.json` & `moto-4.1.7.dev9/moto/ec2/resources/ecs/optimized_amis/ap-northeast-3.json`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ec2/resources/ecs/optimized_amis/ap-south-1.json` & `moto-4.1.7.dev9/moto/ec2/resources/ecs/optimized_amis/ap-south-1.json`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ec2/resources/ecs/optimized_amis/ap-south-2.json` & `moto-4.1.7.dev9/moto/ec2/resources/ecs/optimized_amis/ap-south-2.json`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ec2/resources/ecs/optimized_amis/ap-southeast-1.json` & `moto-4.1.7.dev9/moto/ec2/resources/ecs/optimized_amis/ap-southeast-1.json`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ec2/resources/ecs/optimized_amis/ap-southeast-2.json` & `moto-4.1.7.dev9/moto/ec2/resources/ecs/optimized_amis/ap-southeast-2.json`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ec2/resources/ecs/optimized_amis/ap-southeast-3.json` & `moto-4.1.7.dev9/moto/ec2/resources/ecs/optimized_amis/ap-southeast-3.json`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ec2/resources/ecs/optimized_amis/ca-central-1.json` & `moto-4.1.7.dev9/moto/ec2/resources/ecs/optimized_amis/ca-central-1.json`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ec2/resources/ecs/optimized_amis/eu-central-1.json` & `moto-4.1.7.dev9/moto/ec2/resources/ecs/optimized_amis/eu-central-1.json`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ec2/resources/ecs/optimized_amis/eu-central-2.json` & `moto-4.1.7.dev9/moto/ec2/resources/ecs/optimized_amis/eu-central-2.json`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ec2/resources/ecs/optimized_amis/eu-north-1.json` & `moto-4.1.7.dev9/moto/ec2/resources/ecs/optimized_amis/eu-north-1.json`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ec2/resources/ecs/optimized_amis/eu-south-1.json` & `moto-4.1.7.dev9/moto/ec2/resources/ecs/optimized_amis/eu-south-1.json`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ec2/resources/ecs/optimized_amis/eu-south-2.json` & `moto-4.1.7.dev9/moto/ec2/resources/ecs/optimized_amis/eu-south-2.json`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ec2/resources/ecs/optimized_amis/eu-west-1.json` & `moto-4.1.7.dev9/moto/ec2/resources/ecs/optimized_amis/eu-west-1.json`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ec2/resources/ecs/optimized_amis/eu-west-2.json` & `moto-4.1.7.dev9/moto/ec2/resources/ecs/optimized_amis/eu-west-2.json`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ec2/resources/ecs/optimized_amis/eu-west-3.json` & `moto-4.1.7.dev9/moto/ec2/resources/ecs/optimized_amis/eu-west-3.json`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ec2/resources/ecs/optimized_amis/me-central-1.json` & `moto-4.1.7.dev9/moto/ec2/resources/ecs/optimized_amis/me-central-1.json`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ec2/resources/ecs/optimized_amis/me-south-1.json` & `moto-4.1.7.dev9/moto/ec2/resources/ecs/optimized_amis/me-south-1.json`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ec2/resources/ecs/optimized_amis/sa-east-1.json` & `moto-4.1.7.dev9/moto/ec2/resources/ecs/optimized_amis/sa-east-1.json`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ec2/resources/ecs/optimized_amis/us-east-1.json` & `moto-4.1.7.dev9/moto/ec2/resources/ecs/optimized_amis/us-east-1.json`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ec2/resources/ecs/optimized_amis/us-east-2.json` & `moto-4.1.7.dev9/moto/ec2/resources/ecs/optimized_amis/us-east-2.json`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ec2/resources/ecs/optimized_amis/us-west-1.json` & `moto-4.1.7.dev9/moto/ec2/resources/ecs/optimized_amis/us-west-1.json`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ec2/resources/ecs/optimized_amis/us-west-2.json` & `moto-4.1.7.dev9/moto/ec2/resources/ecs/optimized_amis/us-west-2.json`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ec2/resources/instance_type_offerings/availability-zone/af-south-1.json` & `moto-4.1.7.dev9/moto/ec2/resources/instance_type_offerings/availability-zone/af-south-1.json`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ec2/resources/instance_type_offerings/availability-zone/ap-east-1.json` & `moto-4.1.7.dev9/moto/ec2/resources/instance_type_offerings/availability-zone/ap-east-1.json`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ec2/resources/instance_type_offerings/availability-zone/ap-northeast-1.json` & `moto-4.1.7.dev9/moto/ec2/resources/instance_type_offerings/availability-zone/ap-northeast-1.json`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ec2/resources/instance_type_offerings/availability-zone/ap-northeast-2.json` & `moto-4.1.7.dev9/moto/ec2/resources/instance_type_offerings/availability-zone/ap-northeast-2.json`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ec2/resources/instance_type_offerings/availability-zone/ap-northeast-3.json` & `moto-4.1.7.dev9/moto/ec2/resources/instance_type_offerings/availability-zone/ap-northeast-3.json`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ec2/resources/instance_type_offerings/availability-zone/ap-south-1.json` & `moto-4.1.7.dev9/moto/ec2/resources/instance_type_offerings/availability-zone/ap-south-1.json`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ec2/resources/instance_type_offerings/availability-zone/ap-south-2.json` & `moto-4.1.7.dev9/moto/ec2/resources/instance_type_offerings/availability-zone/ap-south-2.json`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ec2/resources/instance_type_offerings/availability-zone/ap-southeast-1.json` & `moto-4.1.7.dev9/moto/ec2/resources/instance_type_offerings/availability-zone/ap-southeast-1.json`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ec2/resources/instance_type_offerings/availability-zone/ap-southeast-2.json` & `moto-4.1.7.dev9/moto/ec2/resources/instance_type_offerings/availability-zone/ap-southeast-2.json`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ec2/resources/instance_type_offerings/availability-zone/ap-southeast-3.json` & `moto-4.1.7.dev9/moto/ec2/resources/instance_type_offerings/availability-zone/ap-southeast-3.json`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ec2/resources/instance_type_offerings/availability-zone/ca-central-1.json` & `moto-4.1.7.dev9/moto/ec2/resources/instance_type_offerings/availability-zone/ca-central-1.json`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ec2/resources/instance_type_offerings/availability-zone/eu-central-1.json` & `moto-4.1.7.dev9/moto/ec2/resources/instance_type_offerings/availability-zone/eu-central-1.json`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ec2/resources/instance_type_offerings/availability-zone/eu-central-2.json` & `moto-4.1.7.dev9/moto/ec2/resources/instance_type_offerings/availability-zone/eu-central-2.json`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ec2/resources/instance_type_offerings/availability-zone/eu-north-1.json` & `moto-4.1.7.dev9/moto/ec2/resources/instance_type_offerings/availability-zone/eu-north-1.json`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ec2/resources/instance_type_offerings/availability-zone/eu-south-1.json` & `moto-4.1.7.dev9/moto/ec2/resources/instance_type_offerings/availability-zone/eu-south-1.json`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ec2/resources/instance_type_offerings/availability-zone/eu-south-2.json` & `moto-4.1.7.dev9/moto/ec2/resources/instance_type_offerings/availability-zone/eu-south-2.json`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ec2/resources/instance_type_offerings/availability-zone/eu-west-1.json` & `moto-4.1.7.dev9/moto/ec2/resources/instance_type_offerings/availability-zone/eu-west-1.json`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ec2/resources/instance_type_offerings/availability-zone/eu-west-2.json` & `moto-4.1.7.dev9/moto/ec2/resources/instance_type_offerings/availability-zone/eu-west-2.json`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ec2/resources/instance_type_offerings/availability-zone/eu-west-3.json` & `moto-4.1.7.dev9/moto/ec2/resources/instance_type_offerings/availability-zone/eu-west-3.json`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ec2/resources/instance_type_offerings/availability-zone/me-central-1.json` & `moto-4.1.7.dev9/moto/ec2/resources/instance_type_offerings/availability-zone/me-central-1.json`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ec2/resources/instance_type_offerings/availability-zone/me-south-1.json` & `moto-4.1.7.dev9/moto/ec2/resources/instance_type_offerings/availability-zone/me-south-1.json`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ec2/resources/instance_type_offerings/availability-zone/sa-east-1.json` & `moto-4.1.7.dev9/moto/ec2/resources/instance_type_offerings/availability-zone/sa-east-1.json`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ec2/resources/instance_type_offerings/availability-zone/us-east-1.json` & `moto-4.1.7.dev9/moto/ec2/resources/instance_type_offerings/availability-zone/us-east-1.json`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ec2/resources/instance_type_offerings/availability-zone/us-east-2.json` & `moto-4.1.7.dev9/moto/ec2/resources/instance_type_offerings/availability-zone/us-east-2.json`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ec2/resources/instance_type_offerings/availability-zone/us-west-1.json` & `moto-4.1.7.dev9/moto/ec2/resources/instance_type_offerings/availability-zone/us-west-1.json`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ec2/resources/instance_type_offerings/availability-zone/us-west-2.json` & `moto-4.1.7.dev9/moto/ec2/resources/instance_type_offerings/availability-zone/us-west-2.json`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ec2/resources/instance_type_offerings/availability-zone-id/af-south-1.json` & `moto-4.1.7.dev9/moto/ec2/resources/instance_type_offerings/availability-zone-id/af-south-1.json`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ec2/resources/instance_type_offerings/availability-zone-id/ap-east-1.json` & `moto-4.1.7.dev9/moto/ec2/resources/instance_type_offerings/availability-zone-id/ap-east-1.json`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ec2/resources/instance_type_offerings/availability-zone-id/ap-northeast-1.json` & `moto-4.1.7.dev9/moto/ec2/resources/instance_type_offerings/availability-zone-id/ap-northeast-1.json`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ec2/resources/instance_type_offerings/availability-zone-id/ap-northeast-2.json` & `moto-4.1.7.dev9/moto/ec2/resources/instance_type_offerings/availability-zone-id/ap-northeast-2.json`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ec2/resources/instance_type_offerings/availability-zone-id/ap-northeast-3.json` & `moto-4.1.7.dev9/moto/ec2/resources/instance_type_offerings/availability-zone-id/ap-northeast-3.json`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ec2/resources/instance_type_offerings/availability-zone-id/ap-south-1.json` & `moto-4.1.7.dev9/moto/ec2/resources/instance_type_offerings/availability-zone-id/ap-south-1.json`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ec2/resources/instance_type_offerings/availability-zone-id/ap-south-2.json` & `moto-4.1.7.dev9/moto/ec2/resources/instance_type_offerings/availability-zone-id/ap-south-2.json`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ec2/resources/instance_type_offerings/availability-zone-id/ap-southeast-1.json` & `moto-4.1.7.dev9/moto/ec2/resources/instance_type_offerings/availability-zone-id/ap-southeast-1.json`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ec2/resources/instance_type_offerings/availability-zone-id/ap-southeast-2.json` & `moto-4.1.7.dev9/moto/ec2/resources/instance_type_offerings/availability-zone-id/ap-southeast-2.json`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ec2/resources/instance_type_offerings/availability-zone-id/ap-southeast-3.json` & `moto-4.1.7.dev9/moto/ec2/resources/instance_type_offerings/availability-zone-id/ap-southeast-3.json`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ec2/resources/instance_type_offerings/availability-zone-id/ca-central-1.json` & `moto-4.1.7.dev9/moto/ec2/resources/instance_type_offerings/availability-zone-id/ca-central-1.json`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ec2/resources/instance_type_offerings/availability-zone-id/eu-central-1.json` & `moto-4.1.7.dev9/moto/ec2/resources/instance_type_offerings/availability-zone-id/eu-central-1.json`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ec2/resources/instance_type_offerings/availability-zone-id/eu-central-2.json` & `moto-4.1.7.dev9/moto/ec2/resources/instance_type_offerings/availability-zone-id/eu-central-2.json`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ec2/resources/instance_type_offerings/availability-zone-id/eu-north-1.json` & `moto-4.1.7.dev9/moto/ec2/resources/instance_type_offerings/availability-zone-id/eu-north-1.json`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ec2/resources/instance_type_offerings/availability-zone-id/eu-south-1.json` & `moto-4.1.7.dev9/moto/ec2/resources/instance_type_offerings/availability-zone-id/eu-south-1.json`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ec2/resources/instance_type_offerings/availability-zone-id/eu-south-2.json` & `moto-4.1.7.dev9/moto/ec2/resources/instance_type_offerings/availability-zone-id/eu-south-2.json`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ec2/resources/instance_type_offerings/availability-zone-id/eu-west-1.json` & `moto-4.1.7.dev9/moto/ec2/resources/instance_type_offerings/availability-zone-id/eu-west-1.json`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ec2/resources/instance_type_offerings/availability-zone-id/eu-west-2.json` & `moto-4.1.7.dev9/moto/ec2/resources/instance_type_offerings/availability-zone-id/eu-west-2.json`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ec2/resources/instance_type_offerings/availability-zone-id/eu-west-3.json` & `moto-4.1.7.dev9/moto/ec2/resources/instance_type_offerings/availability-zone-id/eu-west-3.json`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ec2/resources/instance_type_offerings/availability-zone-id/me-central-1.json` & `moto-4.1.7.dev9/moto/ec2/resources/instance_type_offerings/availability-zone-id/me-central-1.json`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ec2/resources/instance_type_offerings/availability-zone-id/me-south-1.json` & `moto-4.1.7.dev9/moto/ec2/resources/instance_type_offerings/availability-zone-id/me-south-1.json`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ec2/resources/instance_type_offerings/availability-zone-id/sa-east-1.json` & `moto-4.1.7.dev9/moto/ec2/resources/instance_type_offerings/availability-zone-id/sa-east-1.json`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ec2/resources/instance_type_offerings/availability-zone-id/us-east-1.json` & `moto-4.1.7.dev9/moto/ec2/resources/instance_type_offerings/availability-zone-id/us-east-1.json`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ec2/resources/instance_type_offerings/availability-zone-id/us-east-2.json` & `moto-4.1.7.dev9/moto/ec2/resources/instance_type_offerings/availability-zone-id/us-east-2.json`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ec2/resources/instance_type_offerings/availability-zone-id/us-west-1.json` & `moto-4.1.7.dev9/moto/ec2/resources/instance_type_offerings/availability-zone-id/us-west-1.json`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ec2/resources/instance_type_offerings/availability-zone-id/us-west-2.json` & `moto-4.1.7.dev9/moto/ec2/resources/instance_type_offerings/availability-zone-id/us-west-2.json`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ec2/resources/instance_type_offerings/region/af-south-1.json` & `moto-4.1.7.dev9/moto/ec2/resources/instance_type_offerings/region/af-south-1.json`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ec2/resources/instance_type_offerings/region/ap-east-1.json` & `moto-4.1.7.dev9/moto/ec2/resources/instance_type_offerings/region/ap-east-1.json`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ec2/resources/instance_type_offerings/region/ap-northeast-1.json` & `moto-4.1.7.dev9/moto/ec2/resources/instance_type_offerings/region/ap-northeast-1.json`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ec2/resources/instance_type_offerings/region/ap-northeast-2.json` & `moto-4.1.7.dev9/moto/ec2/resources/instance_type_offerings/region/ap-northeast-2.json`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ec2/resources/instance_type_offerings/region/ap-northeast-3.json` & `moto-4.1.7.dev9/moto/ec2/resources/instance_type_offerings/region/ap-northeast-3.json`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ec2/resources/instance_type_offerings/region/ap-south-1.json` & `moto-4.1.7.dev9/moto/ec2/resources/instance_type_offerings/region/ap-south-1.json`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ec2/resources/instance_type_offerings/region/ap-south-2.json` & `moto-4.1.7.dev9/moto/ec2/resources/instance_type_offerings/region/ap-south-2.json`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ec2/resources/instance_type_offerings/region/ap-southeast-1.json` & `moto-4.1.7.dev9/moto/ec2/resources/instance_type_offerings/region/ap-southeast-1.json`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ec2/resources/instance_type_offerings/region/ap-southeast-2.json` & `moto-4.1.7.dev9/moto/ec2/resources/instance_type_offerings/region/ap-southeast-2.json`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ec2/resources/instance_type_offerings/region/ap-southeast-3.json` & `moto-4.1.7.dev9/moto/ec2/resources/instance_type_offerings/region/ap-southeast-3.json`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ec2/resources/instance_type_offerings/region/ca-central-1.json` & `moto-4.1.7.dev9/moto/ec2/resources/instance_type_offerings/region/ca-central-1.json`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ec2/resources/instance_type_offerings/region/eu-central-1.json` & `moto-4.1.7.dev9/moto/ec2/resources/instance_type_offerings/region/eu-central-1.json`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ec2/resources/instance_type_offerings/region/eu-central-2.json` & `moto-4.1.7.dev9/moto/ec2/resources/instance_type_offerings/region/eu-central-2.json`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ec2/resources/instance_type_offerings/region/eu-north-1.json` & `moto-4.1.7.dev9/moto/ec2/resources/instance_type_offerings/region/eu-north-1.json`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ec2/resources/instance_type_offerings/region/eu-south-1.json` & `moto-4.1.7.dev9/moto/ec2/resources/instance_type_offerings/region/eu-south-1.json`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ec2/resources/instance_type_offerings/region/eu-south-2.json` & `moto-4.1.7.dev9/moto/ec2/resources/instance_type_offerings/region/eu-south-2.json`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ec2/resources/instance_type_offerings/region/eu-west-1.json` & `moto-4.1.7.dev9/moto/ec2/resources/instance_type_offerings/region/eu-west-1.json`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ec2/resources/instance_type_offerings/region/eu-west-2.json` & `moto-4.1.7.dev9/moto/ec2/resources/instance_type_offerings/region/eu-west-2.json`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ec2/resources/instance_type_offerings/region/eu-west-3.json` & `moto-4.1.7.dev9/moto/ec2/resources/instance_type_offerings/region/eu-west-3.json`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ec2/resources/instance_type_offerings/region/me-central-1.json` & `moto-4.1.7.dev9/moto/ec2/resources/instance_type_offerings/region/me-central-1.json`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ec2/resources/instance_type_offerings/region/me-south-1.json` & `moto-4.1.7.dev9/moto/ec2/resources/instance_type_offerings/region/me-south-1.json`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ec2/resources/instance_type_offerings/region/sa-east-1.json` & `moto-4.1.7.dev9/moto/ec2/resources/instance_type_offerings/region/sa-east-1.json`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ec2/resources/instance_type_offerings/region/us-east-1.json` & `moto-4.1.7.dev9/moto/ec2/resources/instance_type_offerings/region/us-east-1.json`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ec2/resources/instance_type_offerings/region/us-east-2.json` & `moto-4.1.7.dev9/moto/ec2/resources/instance_type_offerings/region/us-east-2.json`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ec2/resources/instance_type_offerings/region/us-west-1.json` & `moto-4.1.7.dev9/moto/ec2/resources/instance_type_offerings/region/us-west-1.json`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ec2/resources/instance_type_offerings/region/us-west-2.json` & `moto-4.1.7.dev9/moto/ec2/resources/instance_type_offerings/region/us-west-2.json`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ec2/resources/instance_types.json` & `moto-4.1.7.dev9/moto/ec2/resources/instance_types.json`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ec2/resources/latest_amis/af-south-1.json` & `moto-4.1.7.dev9/moto/ec2/resources/latest_amis/af-south-1.json`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ec2/resources/latest_amis/ap-east-1.json` & `moto-4.1.7.dev9/moto/ec2/resources/latest_amis/ap-east-1.json`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ec2/resources/latest_amis/ap-northeast-1.json` & `moto-4.1.7.dev9/moto/ec2/resources/latest_amis/ap-northeast-1.json`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ec2/resources/latest_amis/ap-northeast-2.json` & `moto-4.1.7.dev9/moto/ec2/resources/latest_amis/ap-northeast-2.json`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ec2/resources/latest_amis/ap-northeast-3.json` & `moto-4.1.7.dev9/moto/ec2/resources/latest_amis/ap-northeast-3.json`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ec2/resources/latest_amis/ap-south-1.json` & `moto-4.1.7.dev9/moto/ec2/resources/latest_amis/ap-south-1.json`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ec2/resources/latest_amis/ap-south-2.json` & `moto-4.1.7.dev9/moto/ec2/resources/latest_amis/ap-south-2.json`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ec2/resources/latest_amis/ap-southeast-1.json` & `moto-4.1.7.dev9/moto/ec2/resources/latest_amis/ap-southeast-1.json`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ec2/resources/latest_amis/ap-southeast-2.json` & `moto-4.1.7.dev9/moto/ec2/resources/latest_amis/ap-southeast-2.json`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ec2/resources/latest_amis/ap-southeast-3.json` & `moto-4.1.7.dev9/moto/ec2/resources/latest_amis/ap-southeast-3.json`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ec2/resources/latest_amis/ca-central-1.json` & `moto-4.1.7.dev9/moto/ec2/resources/latest_amis/ca-central-1.json`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ec2/resources/latest_amis/eu-central-1.json` & `moto-4.1.7.dev9/moto/ec2/resources/latest_amis/eu-central-1.json`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ec2/resources/latest_amis/eu-central-2.json` & `moto-4.1.7.dev9/moto/ec2/resources/latest_amis/eu-central-2.json`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ec2/resources/latest_amis/eu-north-1.json` & `moto-4.1.7.dev9/moto/ec2/resources/latest_amis/eu-north-1.json`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ec2/resources/latest_amis/eu-south-1.json` & `moto-4.1.7.dev9/moto/ec2/resources/latest_amis/eu-south-1.json`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ec2/resources/latest_amis/eu-south-2.json` & `moto-4.1.7.dev9/moto/ec2/resources/latest_amis/eu-south-2.json`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ec2/resources/latest_amis/eu-west-1.json` & `moto-4.1.7.dev9/moto/ec2/resources/latest_amis/eu-west-1.json`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ec2/resources/latest_amis/eu-west-2.json` & `moto-4.1.7.dev9/moto/ec2/resources/latest_amis/eu-west-2.json`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ec2/resources/latest_amis/eu-west-3.json` & `moto-4.1.7.dev9/moto/ec2/resources/latest_amis/eu-west-3.json`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ec2/resources/latest_amis/me-central-1.json` & `moto-4.1.7.dev9/moto/ec2/resources/latest_amis/me-central-1.json`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ec2/resources/latest_amis/me-south-1.json` & `moto-4.1.7.dev9/moto/ec2/resources/latest_amis/me-south-1.json`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ec2/resources/latest_amis/sa-east-1.json` & `moto-4.1.7.dev9/moto/ec2/resources/latest_amis/sa-east-1.json`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ec2/resources/latest_amis/us-east-1.json` & `moto-4.1.7.dev9/moto/ec2/resources/latest_amis/us-east-1.json`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ec2/resources/latest_amis/us-east-2.json` & `moto-4.1.7.dev9/moto/ec2/resources/latest_amis/us-east-2.json`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ec2/resources/latest_amis/us-west-1.json` & `moto-4.1.7.dev9/moto/ec2/resources/latest_amis/us-west-1.json`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ec2/resources/latest_amis/us-west-2.json` & `moto-4.1.7.dev9/moto/ec2/resources/latest_amis/us-west-2.json`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ec2/responses/__init__.py` & `moto-4.1.7.dev9/moto/ec2/responses/__init__.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ec2/responses/_base_response.py` & `moto-4.1.7.dev9/moto/ec2/responses/_base_response.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ec2/responses/account_attributes.py` & `moto-4.1.7.dev9/moto/ec2/responses/account_attributes.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ec2/responses/amis.py` & `moto-4.1.7.dev9/moto/ec2/responses/amis.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ec2/responses/availability_zones_and_regions.py` & `moto-4.1.7.dev9/moto/ec2/responses/availability_zones_and_regions.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ec2/responses/carrier_gateways.py` & `moto-4.1.7.dev9/moto/ec2/responses/carrier_gateways.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ec2/responses/customer_gateways.py` & `moto-4.1.7.dev9/moto/ec2/responses/customer_gateways.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ec2/responses/dhcp_options.py` & `moto-4.1.7.dev9/moto/ec2/responses/dhcp_options.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ec2/responses/egress_only_internet_gateways.py` & `moto-4.1.7.dev9/moto/ec2/responses/egress_only_internet_gateways.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ec2/responses/elastic_block_store.py` & `moto-4.1.7.dev9/moto/ec2/responses/elastic_block_store.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ec2/responses/elastic_ip_addresses.py` & `moto-4.1.7.dev9/moto/ec2/responses/elastic_ip_addresses.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ec2/responses/elastic_network_interfaces.py` & `moto-4.1.7.dev9/moto/ec2/responses/elastic_network_interfaces.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ec2/responses/fleets.py` & `moto-4.1.7.dev9/moto/ec2/responses/fleets.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ec2/responses/flow_logs.py` & `moto-4.1.7.dev9/moto/ec2/responses/flow_logs.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ec2/responses/general.py` & `moto-4.1.7.dev9/moto/ec2/responses/general.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ec2/responses/hosts.py` & `moto-4.1.7.dev9/moto/ec2/responses/hosts.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ec2/responses/iam_instance_profiles.py` & `moto-4.1.7.dev9/moto/ec2/responses/iam_instance_profiles.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ec2/responses/instances.py` & `moto-4.1.7.dev9/moto/ec2/responses/instances.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ec2/responses/internet_gateways.py` & `moto-4.1.7.dev9/moto/ec2/responses/internet_gateways.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ec2/responses/key_pairs.py` & `moto-4.1.7.dev9/moto/ec2/responses/key_pairs.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ec2/responses/launch_templates.py` & `moto-4.1.7.dev9/moto/ec2/responses/launch_templates.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ec2/responses/nat_gateways.py` & `moto-4.1.7.dev9/moto/ec2/responses/nat_gateways.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ec2/responses/network_acls.py` & `moto-4.1.7.dev9/moto/ec2/responses/network_acls.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ec2/responses/reserved_instances.py` & `moto-4.1.7.dev9/moto/ec2/responses/reserved_instances.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ec2/responses/route_tables.py` & `moto-4.1.7.dev9/moto/ec2/responses/route_tables.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ec2/responses/security_groups.py` & `moto-4.1.7.dev9/moto/ec2/responses/security_groups.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ec2/responses/settings.py` & `moto-4.1.7.dev9/moto/ec2/responses/settings.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ec2/responses/spot_fleets.py` & `moto-4.1.7.dev9/moto/ec2/responses/spot_fleets.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ec2/responses/spot_instances.py` & `moto-4.1.7.dev9/moto/ec2/responses/spot_instances.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ec2/responses/subnets.py` & `moto-4.1.7.dev9/moto/ec2/responses/subnets.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ec2/responses/tags.py` & `moto-4.1.7.dev9/moto/ec2/responses/tags.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ec2/responses/transit_gateway_attachments.py` & `moto-4.1.7.dev9/moto/ec2/responses/transit_gateway_attachments.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ec2/responses/transit_gateway_route_tables.py` & `moto-4.1.7.dev9/moto/ec2/responses/transit_gateway_route_tables.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ec2/responses/transit_gateways.py` & `moto-4.1.7.dev9/moto/ec2/responses/transit_gateways.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ec2/responses/virtual_private_gateways.py` & `moto-4.1.7.dev9/moto/ec2/responses/virtual_private_gateways.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ec2/responses/vpc_peering_connections.py` & `moto-4.1.7.dev9/moto/ec2/responses/vpc_peering_connections.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ec2/responses/vpc_service_configuration.py` & `moto-4.1.7.dev9/moto/ec2/responses/vpc_service_configuration.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ec2/responses/vpcs.py` & `moto-4.1.7.dev9/moto/ec2/responses/vpcs.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ec2/responses/vpn_connections.py` & `moto-4.1.7.dev9/moto/ec2/responses/vpn_connections.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ec2/responses/windows.py` & `moto-4.1.7.dev9/moto/ec2/responses/windows.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ec2/utils.py` & `moto-4.1.7.dev9/moto/ec2/utils.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ec2instanceconnect/responses.py` & `moto-4.1.7.dev9/moto/ec2instanceconnect/responses.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ecr/exceptions.py` & `moto-4.1.7.dev9/moto/ecr/exceptions.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ecr/models.py` & `moto-4.1.7.dev9/moto/ecr/models.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ecr/policy_validation.py` & `moto-4.1.7.dev9/moto/ecr/policy_validation.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ecr/responses.py` & `moto-4.1.7.dev9/moto/ecr/responses.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ecs/exceptions.py` & `moto-4.1.7.dev9/moto/ecs/exceptions.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ecs/models.py` & `moto-4.1.7.dev9/moto/ecs/models.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ecs/responses.py` & `moto-4.1.7.dev9/moto/ecs/responses.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/efs/exceptions.py` & `moto-4.1.7.dev9/moto/efs/exceptions.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/efs/models.py` & `moto-4.1.7.dev9/moto/efs/models.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/efs/responses.py` & `moto-4.1.7.dev9/moto/efs/responses.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/efs/urls.py` & `moto-4.1.7.dev9/moto/efs/urls.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/eks/exceptions.py` & `moto-4.1.7.dev9/moto/eks/exceptions.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/eks/models.py` & `moto-4.1.7.dev9/moto/eks/models.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/eks/responses.py` & `moto-4.1.7.dev9/moto/eks/responses.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/eks/urls.py` & `moto-4.1.7.dev9/moto/eks/urls.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/eks/utils.py` & `moto-4.1.7.dev9/moto/eks/utils.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/elasticache/exceptions.py` & `moto-4.1.7.dev9/moto/elasticache/exceptions.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/elasticache/models.py` & `moto-4.1.7.dev9/moto/elasticache/models.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/elasticache/responses.py` & `moto-4.1.7.dev9/moto/elasticache/responses.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/elasticbeanstalk/models.py` & `moto-4.1.7.dev9/moto/elasticbeanstalk/models.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/elasticbeanstalk/responses.py` & `moto-4.1.7.dev9/moto/elasticbeanstalk/responses.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/elastictranscoder/models.py` & `moto-4.1.7.dev9/moto/elastictranscoder/models.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/elastictranscoder/responses.py` & `moto-4.1.7.dev9/moto/elastictranscoder/responses.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/elb/exceptions.py` & `moto-4.1.7.dev9/moto/elb/exceptions.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/elb/models.py` & `moto-4.1.7.dev9/moto/elb/models.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/elb/policies.py` & `moto-4.1.7.dev9/moto/elb/policies.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/elb/responses.py` & `moto-4.1.7.dev9/moto/elb/responses.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/elb/urls.py` & `moto-4.1.7.dev9/moto/elb/urls.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/elbv2/exceptions.py` & `moto-4.1.7.dev9/moto/elbv2/exceptions.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/elbv2/models.py` & `moto-4.1.7.dev9/moto/elbv2/models.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/elbv2/responses.py` & `moto-4.1.7.dev9/moto/elbv2/responses.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/emr/models.py` & `moto-4.1.7.dev9/moto/emr/models.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/emr/responses.py` & `moto-4.1.7.dev9/moto/emr/responses.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/emr/utils.py` & `moto-4.1.7.dev9/moto/emr/utils.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/emrcontainers/models.py` & `moto-4.1.7.dev9/moto/emrcontainers/models.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/emrcontainers/responses.py` & `moto-4.1.7.dev9/moto/emrcontainers/responses.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/emrcontainers/urls.py` & `moto-4.1.7.dev9/moto/emrcontainers/urls.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/emrcontainers/utils.py` & `moto-4.1.7.dev9/moto/emrcontainers/utils.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/emrserverless/models.py` & `moto-4.1.7.dev9/moto/emrserverless/models.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/emrserverless/responses.py` & `moto-4.1.7.dev9/moto/emrserverless/responses.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/emrserverless/urls.py` & `moto-4.1.7.dev9/moto/emrserverless/urls.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/emrserverless/utils.py` & `moto-4.1.7.dev9/moto/emrserverless/utils.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/es/exceptions.py` & `moto-4.1.7.dev9/moto/es/exceptions.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/es/models.py` & `moto-4.1.7.dev9/moto/es/models.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/es/responses.py` & `moto-4.1.7.dev9/moto/es/responses.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/es/urls.py` & `moto-4.1.7.dev9/moto/es/urls.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/events/exceptions.py` & `moto-4.1.7.dev9/moto/events/exceptions.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/events/models.py` & `moto-4.1.7.dev9/moto/events/models.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/events/notifications.py` & `moto-4.1.7.dev9/moto/events/notifications.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/events/responses.py` & `moto-4.1.7.dev9/moto/events/responses.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/firehose/exceptions.py` & `moto-4.1.7.dev9/moto/firehose/exceptions.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/firehose/models.py` & `moto-4.1.7.dev9/moto/firehose/models.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/firehose/responses.py` & `moto-4.1.7.dev9/moto/firehose/responses.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/forecast/exceptions.py` & `moto-4.1.7.dev9/moto/forecast/exceptions.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/forecast/models.py` & `moto-4.1.7.dev9/moto/forecast/models.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/forecast/responses.py` & `moto-4.1.7.dev9/moto/forecast/responses.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/glacier/models.py` & `moto-4.1.7.dev9/moto/glacier/models.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/glacier/responses.py` & `moto-4.1.7.dev9/moto/glacier/responses.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/glacier/urls.py` & `moto-4.1.7.dev9/moto/glacier/urls.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/glue/exceptions.py` & `moto-4.1.7.dev9/moto/glue/exceptions.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/glue/glue_schema_registry_constants.py` & `moto-4.1.7.dev9/moto/glue/glue_schema_registry_constants.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/glue/glue_schema_registry_utils.py` & `moto-4.1.7.dev9/moto/glue/glue_schema_registry_utils.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/glue/models.py` & `moto-4.1.7.dev9/moto/glue/models.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/glue/responses.py` & `moto-4.1.7.dev9/moto/glue/responses.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/glue/utils.py` & `moto-4.1.7.dev9/moto/glue/utils.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/greengrass/exceptions.py` & `moto-4.1.7.dev9/moto/greengrass/exceptions.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/greengrass/models.py` & `moto-4.1.7.dev9/moto/greengrass/models.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/greengrass/responses.py` & `moto-4.1.7.dev9/moto/greengrass/responses.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/greengrass/urls.py` & `moto-4.1.7.dev9/moto/greengrass/urls.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/guardduty/exceptions.py` & `moto-4.1.7.dev9/moto/guardduty/exceptions.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/guardduty/models.py` & `moto-4.1.7.dev9/moto/guardduty/models.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/guardduty/responses.py` & `moto-4.1.7.dev9/moto/guardduty/responses.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/guardduty/urls.py` & `moto-4.1.7.dev9/moto/guardduty/urls.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/iam/access_control.py` & `moto-4.1.7.dev9/moto/iam/access_control.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/iam/aws_managed_policies.py` & `moto-4.1.7.dev9/moto/iam/aws_managed_policies.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/iam/config.py` & `moto-4.1.7.dev9/moto/iam/config.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/iam/exceptions.py` & `moto-4.1.7.dev9/moto/iam/exceptions.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/iam/models.py` & `moto-4.1.7.dev9/moto/iam/models.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/iam/policy_validation.py` & `moto-4.1.7.dev9/moto/iam/policy_validation.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/iam/responses.py` & `moto-4.1.7.dev9/moto/iam/responses.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/iam/utils.py` & `moto-4.1.7.dev9/moto/iam/utils.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/identitystore/models.py` & `moto-4.1.7.dev9/moto/identitystore/models.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/identitystore/responses.py` & `moto-4.1.7.dev9/moto/identitystore/responses.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/instance_metadata/responses.py` & `moto-4.1.7.dev9/moto/instance_metadata/responses.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/iot/exceptions.py` & `moto-4.1.7.dev9/moto/iot/exceptions.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/iot/models.py` & `moto-4.1.7.dev9/moto/iot/models.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/iot/responses.py` & `moto-4.1.7.dev9/moto/iot/responses.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/iot/urls.py` & `moto-4.1.7.dev9/moto/iot/urls.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/iotdata/exceptions.py` & `moto-4.1.7.dev9/moto/iotdata/exceptions.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/iotdata/models.py` & `moto-4.1.7.dev9/moto/iotdata/models.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/iotdata/responses.py` & `moto-4.1.7.dev9/moto/iotdata/responses.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/kinesis/exceptions.py` & `moto-4.1.7.dev9/moto/kinesis/exceptions.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/kinesis/models.py` & `moto-4.1.7.dev9/moto/kinesis/models.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/kinesis/responses.py` & `moto-4.1.7.dev9/moto/kinesis/responses.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/kinesis/urls.py` & `moto-4.1.7.dev9/moto/kinesis/urls.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/kinesis/utils.py` & `moto-4.1.7.dev9/moto/kinesis/utils.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/kinesisvideo/exceptions.py` & `moto-4.1.7.dev9/moto/kinesisvideo/exceptions.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/kinesisvideo/models.py` & `moto-4.1.7.dev9/moto/kinesisvideo/models.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/kinesisvideo/responses.py` & `moto-4.1.7.dev9/moto/kinesisvideo/responses.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/kinesisvideoarchivedmedia/models.py` & `moto-4.1.7.dev9/moto/kinesisvideoarchivedmedia/models.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/kinesisvideoarchivedmedia/responses.py` & `moto-4.1.7.dev9/moto/kinesisvideoarchivedmedia/responses.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/kms/exceptions.py` & `moto-4.1.7.dev9/moto/kms/exceptions.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/kms/models.py` & `moto-4.1.7.dev9/moto/kms/models.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/kms/policy_validator.py` & `moto-4.1.7.dev9/moto/kms/policy_validator.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/kms/responses.py` & `moto-4.1.7.dev9/moto/kms/responses.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/kms/utils.py` & `moto-4.1.7.dev9/moto/kms/utils.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/logs/exceptions.py` & `moto-4.1.7.dev9/moto/logs/exceptions.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/logs/metric_filters.py` & `moto-4.1.7.dev9/moto/logs/metric_filters.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/logs/models.py` & `moto-4.1.7.dev9/moto/logs/models.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/logs/responses.py` & `moto-4.1.7.dev9/moto/logs/responses.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/logs/utils.py` & `moto-4.1.7.dev9/moto/logs/utils.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/managedblockchain/exceptions.py` & `moto-4.1.7.dev9/moto/managedblockchain/exceptions.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/managedblockchain/models.py` & `moto-4.1.7.dev9/moto/managedblockchain/models.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/managedblockchain/responses.py` & `moto-4.1.7.dev9/moto/managedblockchain/responses.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/managedblockchain/urls.py` & `moto-4.1.7.dev9/moto/managedblockchain/urls.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/managedblockchain/utils.py` & `moto-4.1.7.dev9/moto/managedblockchain/utils.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/mediaconnect/models.py` & `moto-4.1.7.dev9/moto/mediaconnect/models.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/mediaconnect/responses.py` & `moto-4.1.7.dev9/moto/mediaconnect/responses.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/mediaconnect/urls.py` & `moto-4.1.7.dev9/moto/mediaconnect/urls.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/medialive/models.py` & `moto-4.1.7.dev9/moto/medialive/models.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/medialive/responses.py` & `moto-4.1.7.dev9/moto/medialive/responses.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/medialive/urls.py` & `moto-4.1.7.dev9/moto/medialive/urls.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/mediapackage/models.py` & `moto-4.1.7.dev9/moto/mediapackage/models.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/mediapackage/responses.py` & `moto-4.1.7.dev9/moto/mediapackage/responses.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/mediastore/exceptions.py` & `moto-4.1.7.dev9/moto/mediastore/exceptions.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/mediastore/models.py` & `moto-4.1.7.dev9/moto/mediastore/models.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/mediastore/responses.py` & `moto-4.1.7.dev9/moto/mediastore/responses.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/mediastoredata/models.py` & `moto-4.1.7.dev9/moto/mediastoredata/models.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/mediastoredata/responses.py` & `moto-4.1.7.dev9/moto/mediastoredata/responses.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/meteringmarketplace/exceptions.py` & `moto-4.1.7.dev9/moto/meteringmarketplace/exceptions.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/meteringmarketplace/models.py` & `moto-4.1.7.dev9/moto/meteringmarketplace/models.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/meteringmarketplace/responses.py` & `moto-4.1.7.dev9/moto/meteringmarketplace/responses.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/moto_api/_internal/managed_state_model.py` & `moto-4.1.7.dev9/moto/moto_api/_internal/managed_state_model.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/moto_api/_internal/models.py` & `moto-4.1.7.dev9/moto/moto_api/_internal/models.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/moto_api/_internal/moto_random.py` & `moto-4.1.7.dev9/moto/moto_api/_internal/moto_random.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/moto_api/_internal/recorder/models.py` & `moto-4.1.7.dev9/moto/moto_api/_internal/recorder/models.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/moto_api/_internal/recorder/responses.py` & `moto-4.1.7.dev9/moto/moto_api/_internal/recorder/responses.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/moto_api/_internal/responses.py` & `moto-4.1.7.dev9/moto/moto_api/_internal/responses.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/moto_api/_internal/state_manager.py` & `moto-4.1.7.dev9/moto/moto_api/_internal/state_manager.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/moto_api/_internal/urls.py` & `moto-4.1.7.dev9/moto/moto_api/_internal/urls.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/moto_server/templates/dashboard.html` & `moto-4.1.7.dev9/moto/moto_server/templates/dashboard.html`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/moto_server/threaded_moto_server.py` & `moto-4.1.7.dev9/moto/moto_server/threaded_moto_server.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/moto_server/utilities.py` & `moto-4.1.7.dev9/moto/moto_server/utilities.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/moto_server/werkzeug_app.py` & `moto-4.1.7.dev9/moto/moto_server/werkzeug_app.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/mq/configuration.py` & `moto-4.1.7.dev9/moto/mq/configuration.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/mq/exceptions.py` & `moto-4.1.7.dev9/moto/mq/exceptions.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/mq/models.py` & `moto-4.1.7.dev9/moto/mq/models.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/mq/responses.py` & `moto-4.1.7.dev9/moto/mq/responses.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/mq/urls.py` & `moto-4.1.7.dev9/moto/mq/urls.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/neptune/exceptions.py` & `moto-4.1.7.dev9/moto/neptune/exceptions.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/neptune/models.py` & `moto-4.1.7.dev9/moto/neptune/models.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/neptune/responses.py` & `moto-4.1.7.dev9/moto/neptune/responses.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/opensearch/data.py` & `moto-4.1.7.dev9/moto/opensearch/data.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/opensearch/models.py` & `moto-4.1.7.dev9/moto/opensearch/models.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/opensearch/responses.py` & `moto-4.1.7.dev9/moto/opensearch/responses.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/opsworks/models.py` & `moto-4.1.7.dev9/moto/opsworks/models.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/opsworks/responses.py` & `moto-4.1.7.dev9/moto/opsworks/responses.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/organizations/exceptions.py` & `moto-4.1.7.dev9/moto/organizations/exceptions.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/organizations/models.py` & `moto-4.1.7.dev9/moto/organizations/models.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/organizations/responses.py` & `moto-4.1.7.dev9/moto/organizations/responses.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/organizations/utils.py` & `moto-4.1.7.dev9/moto/organizations/utils.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/packages/boto/ec2/blockdevicemapping.py` & `moto-4.1.7.dev9/moto/packages/boto/ec2/blockdevicemapping.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/packages/boto/ec2/ec2object.py` & `moto-4.1.7.dev9/moto/packages/boto/ec2/ec2object.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/packages/boto/ec2/image.py` & `moto-4.1.7.dev9/moto/packages/boto/ec2/image.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/packages/boto/ec2/instance.py` & `moto-4.1.7.dev9/moto/packages/boto/ec2/instance.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/packages/boto/ec2/instancetype.py` & `moto-4.1.7.dev9/moto/packages/boto/ec2/instancetype.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/packages/boto/ec2/tag.py` & `moto-4.1.7.dev9/moto/packages/boto/ec2/tag.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/packages/cfnresponse/cfnresponse.py` & `moto-4.1.7.dev9/moto/packages/cfnresponse/cfnresponse.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/personalize/models.py` & `moto-4.1.7.dev9/moto/personalize/models.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/personalize/responses.py` & `moto-4.1.7.dev9/moto/personalize/responses.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/pinpoint/models.py` & `moto-4.1.7.dev9/moto/pinpoint/models.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/pinpoint/responses.py` & `moto-4.1.7.dev9/moto/pinpoint/responses.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/pinpoint/urls.py` & `moto-4.1.7.dev9/moto/pinpoint/urls.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/polly/models.py` & `moto-4.1.7.dev9/moto/polly/models.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/polly/resources.py` & `moto-4.1.7.dev9/moto/polly/resources.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/polly/responses.py` & `moto-4.1.7.dev9/moto/polly/responses.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/quicksight/models.py` & `moto-4.1.7.dev9/moto/quicksight/models.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/quicksight/responses.py` & `moto-4.1.7.dev9/moto/quicksight/responses.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/quicksight/urls.py` & `moto-4.1.7.dev9/moto/quicksight/urls.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ram/exceptions.py` & `moto-4.1.7.dev9/moto/ram/exceptions.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ram/models.py` & `moto-4.1.7.dev9/moto/ram/models.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ram/responses.py` & `moto-4.1.7.dev9/moto/ram/responses.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/rds/exceptions.py` & `moto-4.1.7.dev9/moto/rds/exceptions.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/rds/models.py` & `moto-4.1.7.dev9/moto/rds/models.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/rds/resources/cluster_options/neptune.json` & `moto-4.1.7.dev9/moto/rds/resources/cluster_options/neptune.json`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/rds/responses.py` & `moto-4.1.7.dev9/moto/rds/responses.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/rds/utils.py` & `moto-4.1.7.dev9/moto/rds/utils.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/redshift/exceptions.py` & `moto-4.1.7.dev9/moto/redshift/exceptions.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/redshift/models.py` & `moto-4.1.7.dev9/moto/redshift/models.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/redshift/responses.py` & `moto-4.1.7.dev9/moto/redshift/responses.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/redshiftdata/models.py` & `moto-4.1.7.dev9/moto/redshiftdata/models.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/redshiftdata/responses.py` & `moto-4.1.7.dev9/moto/redshiftdata/responses.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/rekognition/models.py` & `moto-4.1.7.dev9/moto/rekognition/models.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/rekognition/responses.py` & `moto-4.1.7.dev9/moto/rekognition/responses.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/resourcegroups/models.py` & `moto-4.1.7.dev9/moto/resourcegroups/models.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/resourcegroups/responses.py` & `moto-4.1.7.dev9/moto/resourcegroups/responses.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/resourcegroups/urls.py` & `moto-4.1.7.dev9/moto/resourcegroups/urls.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/resourcegroupstaggingapi/models.py` & `moto-4.1.7.dev9/moto/resourcegroupstaggingapi/models.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/resourcegroupstaggingapi/responses.py` & `moto-4.1.7.dev9/moto/resourcegroupstaggingapi/responses.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/route53/exceptions.py` & `moto-4.1.7.dev9/moto/route53/exceptions.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/route53/models.py` & `moto-4.1.7.dev9/moto/route53/models.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/route53/responses.py` & `moto-4.1.7.dev9/moto/route53/responses.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/route53/urls.py` & `moto-4.1.7.dev9/moto/route53/urls.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/route53resolver/exceptions.py` & `moto-4.1.7.dev9/moto/route53resolver/exceptions.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/route53resolver/models.py` & `moto-4.1.7.dev9/moto/route53resolver/models.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/route53resolver/responses.py` & `moto-4.1.7.dev9/moto/route53resolver/responses.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/route53resolver/utils.py` & `moto-4.1.7.dev9/moto/route53resolver/utils.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/route53resolver/validations.py` & `moto-4.1.7.dev9/moto/route53resolver/validations.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/s3/cloud_formation.py` & `moto-4.1.7.dev9/moto/s3/cloud_formation.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/s3/config.py` & `moto-4.1.7.dev9/moto/s3/config.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/s3/exceptions.py` & `moto-4.1.7.dev9/moto/s3/exceptions.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/s3/models.py` & `moto-4.1.7.dev9/moto/s3/models.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/s3/notifications.py` & `moto-4.1.7.dev9/moto/s3/notifications.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/s3/responses.py` & `moto-4.1.7.dev9/moto/s3/responses.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/s3/select_object_content.py` & `moto-4.1.7.dev9/moto/s3/select_object_content.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/s3/urls.py` & `moto-4.1.7.dev9/moto/s3/urls.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/s3/utils.py` & `moto-4.1.7.dev9/moto/s3/utils.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/s3control/config.py` & `moto-4.1.7.dev9/moto/s3control/config.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/s3control/exceptions.py` & `moto-4.1.7.dev9/moto/s3control/exceptions.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/s3control/models.py` & `moto-4.1.7.dev9/moto/s3control/models.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/s3control/responses.py` & `moto-4.1.7.dev9/moto/s3control/responses.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/s3control/urls.py` & `moto-4.1.7.dev9/moto/s3control/urls.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/sagemaker/exceptions.py` & `moto-4.1.7.dev9/moto/sagemaker/exceptions.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/sagemaker/models.py` & `moto-4.1.7.dev9/moto/sagemaker/models.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/sagemaker/responses.py` & `moto-4.1.7.dev9/moto/sagemaker/responses.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/sagemaker/utils.py` & `moto-4.1.7.dev9/moto/sagemaker/utils.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/sagemaker/validators.py` & `moto-4.1.7.dev9/moto/sagemaker/validators.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/sdb/exceptions.py` & `moto-4.1.7.dev9/moto/sdb/exceptions.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/sdb/models.py` & `moto-4.1.7.dev9/moto/sdb/models.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/sdb/responses.py` & `moto-4.1.7.dev9/moto/sdb/responses.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/secretsmanager/exceptions.py` & `moto-4.1.7.dev9/moto/secretsmanager/exceptions.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/secretsmanager/list_secrets/filters.py` & `moto-4.1.7.dev9/moto/secretsmanager/list_secrets/filters.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/secretsmanager/models.py` & `moto-4.1.7.dev9/moto/secretsmanager/models.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/secretsmanager/responses.py` & `moto-4.1.7.dev9/moto/secretsmanager/responses.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/secretsmanager/utils.py` & `moto-4.1.7.dev9/moto/secretsmanager/utils.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/server.py` & `moto-4.1.7.dev9/moto/server.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/servicediscovery/exceptions.py` & `moto-4.1.7.dev9/moto/servicediscovery/exceptions.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/servicediscovery/models.py` & `moto-4.1.7.dev9/moto/servicediscovery/models.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/servicediscovery/responses.py` & `moto-4.1.7.dev9/moto/servicediscovery/responses.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/servicequotas/models.py` & `moto-4.1.7.dev9/moto/servicequotas/models.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/servicequotas/resources/default_quotas/vpc.py` & `moto-4.1.7.dev9/moto/servicequotas/resources/default_quotas/vpc.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/servicequotas/responses.py` & `moto-4.1.7.dev9/moto/servicequotas/responses.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ses/exceptions.py` & `moto-4.1.7.dev9/moto/ses/exceptions.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ses/feedback.py` & `moto-4.1.7.dev9/moto/ses/feedback.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ses/models.py` & `moto-4.1.7.dev9/moto/ses/models.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ses/responses.py` & `moto-4.1.7.dev9/moto/ses/responses.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ses/template.py` & `moto-4.1.7.dev9/moto/ses/template.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ses/utils.py` & `moto-4.1.7.dev9/moto/ses/utils.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/settings.py` & `moto-4.1.7.dev9/moto/settings.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/signer/models.py` & `moto-4.1.7.dev9/moto/signer/models.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/signer/responses.py` & `moto-4.1.7.dev9/moto/signer/responses.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/sns/exceptions.py` & `moto-4.1.7.dev9/moto/sns/exceptions.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/sns/models.py` & `moto-4.1.7.dev9/moto/sns/models.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/sns/responses.py` & `moto-4.1.7.dev9/moto/sns/responses.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/sqs/exceptions.py` & `moto-4.1.7.dev9/moto/sqs/exceptions.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/sqs/models.py` & `moto-4.1.7.dev9/moto/sqs/models.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/sqs/responses.py` & `moto-4.1.7.dev9/moto/sqs/responses.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/sqs/utils.py` & `moto-4.1.7.dev9/moto/sqs/utils.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ssm/exceptions.py` & `moto-4.1.7.dev9/moto/ssm/exceptions.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ssm/models.py` & `moto-4.1.7.dev9/moto/ssm/models.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ssm/resources/ami-amazon-linux-latest/af-south-1.json` & `moto-4.1.7.dev9/moto/ssm/resources/ami-amazon-linux-latest/af-south-1.json`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ssm/resources/ami-amazon-linux-latest/ap-east-1.json` & `moto-4.1.7.dev9/moto/ssm/resources/ami-amazon-linux-latest/ap-east-1.json`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ssm/resources/ami-amazon-linux-latest/ap-northeast-1.json` & `moto-4.1.7.dev9/moto/ssm/resources/ami-amazon-linux-latest/ap-northeast-1.json`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ssm/resources/ami-amazon-linux-latest/ap-northeast-2.json` & `moto-4.1.7.dev9/moto/ssm/resources/ami-amazon-linux-latest/ap-northeast-2.json`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ssm/resources/ami-amazon-linux-latest/ap-northeast-3.json` & `moto-4.1.7.dev9/moto/ssm/resources/ami-amazon-linux-latest/ap-northeast-3.json`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ssm/resources/ami-amazon-linux-latest/ap-south-1.json` & `moto-4.1.7.dev9/moto/ssm/resources/ami-amazon-linux-latest/ap-south-1.json`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ssm/resources/ami-amazon-linux-latest/ap-south-2.json` & `moto-4.1.7.dev9/moto/ssm/resources/ami-amazon-linux-latest/ap-south-2.json`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ssm/resources/ami-amazon-linux-latest/ap-southeast-1.json` & `moto-4.1.7.dev9/moto/ssm/resources/ami-amazon-linux-latest/ap-southeast-1.json`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ssm/resources/ami-amazon-linux-latest/ap-southeast-2.json` & `moto-4.1.7.dev9/moto/ssm/resources/ami-amazon-linux-latest/ap-southeast-2.json`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ssm/resources/ami-amazon-linux-latest/ap-southeast-3.json` & `moto-4.1.7.dev9/moto/ssm/resources/ami-amazon-linux-latest/ap-southeast-3.json`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ssm/resources/ami-amazon-linux-latest/ca-central-1.json` & `moto-4.1.7.dev9/moto/ssm/resources/ami-amazon-linux-latest/ca-central-1.json`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ssm/resources/ami-amazon-linux-latest/eu-central-1.json` & `moto-4.1.7.dev9/moto/ssm/resources/ami-amazon-linux-latest/eu-central-1.json`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ssm/resources/ami-amazon-linux-latest/eu-central-2.json` & `moto-4.1.7.dev9/moto/ssm/resources/ami-amazon-linux-latest/eu-central-2.json`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ssm/resources/ami-amazon-linux-latest/eu-north-1.json` & `moto-4.1.7.dev9/moto/ssm/resources/ami-amazon-linux-latest/eu-north-1.json`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ssm/resources/ami-amazon-linux-latest/eu-south-1.json` & `moto-4.1.7.dev9/moto/ssm/resources/ami-amazon-linux-latest/eu-south-1.json`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ssm/resources/ami-amazon-linux-latest/eu-south-2.json` & `moto-4.1.7.dev9/moto/ssm/resources/ami-amazon-linux-latest/eu-south-2.json`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ssm/resources/ami-amazon-linux-latest/eu-west-1.json` & `moto-4.1.7.dev9/moto/ssm/resources/ami-amazon-linux-latest/eu-west-1.json`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ssm/resources/ami-amazon-linux-latest/eu-west-2.json` & `moto-4.1.7.dev9/moto/ssm/resources/ami-amazon-linux-latest/eu-west-2.json`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ssm/resources/ami-amazon-linux-latest/eu-west-3.json` & `moto-4.1.7.dev9/moto/ssm/resources/ami-amazon-linux-latest/eu-west-3.json`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ssm/resources/ami-amazon-linux-latest/me-central-1.json` & `moto-4.1.7.dev9/moto/ssm/resources/ami-amazon-linux-latest/me-central-1.json`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ssm/resources/ami-amazon-linux-latest/me-south-1.json` & `moto-4.1.7.dev9/moto/ssm/resources/ami-amazon-linux-latest/me-south-1.json`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ssm/resources/ami-amazon-linux-latest/sa-east-1.json` & `moto-4.1.7.dev9/moto/ssm/resources/ami-amazon-linux-latest/sa-east-1.json`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ssm/resources/ami-amazon-linux-latest/us-east-1.json` & `moto-4.1.7.dev9/moto/ssm/resources/ami-amazon-linux-latest/us-east-1.json`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ssm/resources/ami-amazon-linux-latest/us-east-2.json` & `moto-4.1.7.dev9/moto/ssm/resources/ami-amazon-linux-latest/us-east-2.json`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ssm/resources/ami-amazon-linux-latest/us-west-1.json` & `moto-4.1.7.dev9/moto/ssm/resources/ami-amazon-linux-latest/us-west-1.json`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ssm/resources/ami-amazon-linux-latest/us-west-2.json` & `moto-4.1.7.dev9/moto/ssm/resources/ami-amazon-linux-latest/us-west-2.json`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ssm/resources/ecs/optimized_amis/af-south-1.json` & `moto-4.1.7.dev9/moto/ssm/resources/ecs/optimized_amis/af-south-1.json`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ssm/resources/ecs/optimized_amis/ap-east-1.json` & `moto-4.1.7.dev9/moto/ssm/resources/ecs/optimized_amis/ap-east-1.json`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ssm/resources/ecs/optimized_amis/ap-northeast-1.json` & `moto-4.1.7.dev9/moto/ssm/resources/ecs/optimized_amis/ap-northeast-1.json`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ssm/resources/ecs/optimized_amis/ap-northeast-2.json` & `moto-4.1.7.dev9/moto/ssm/resources/ecs/optimized_amis/ap-northeast-2.json`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ssm/resources/ecs/optimized_amis/ap-northeast-3.json` & `moto-4.1.7.dev9/moto/ssm/resources/ecs/optimized_amis/ap-northeast-3.json`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ssm/resources/ecs/optimized_amis/ap-south-1.json` & `moto-4.1.7.dev9/moto/ssm/resources/ecs/optimized_amis/ap-south-1.json`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ssm/resources/ecs/optimized_amis/ap-south-2.json` & `moto-4.1.7.dev9/moto/ssm/resources/ecs/optimized_amis/ap-south-2.json`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ssm/resources/ecs/optimized_amis/ap-southeast-1.json` & `moto-4.1.7.dev9/moto/ssm/resources/ecs/optimized_amis/ap-southeast-1.json`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ssm/resources/ecs/optimized_amis/ap-southeast-2.json` & `moto-4.1.7.dev9/moto/ssm/resources/ecs/optimized_amis/ap-southeast-2.json`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ssm/resources/ecs/optimized_amis/ap-southeast-3.json` & `moto-4.1.7.dev9/moto/ssm/resources/ecs/optimized_amis/ap-southeast-3.json`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ssm/resources/ecs/optimized_amis/ca-central-1.json` & `moto-4.1.7.dev9/moto/ssm/resources/ecs/optimized_amis/ca-central-1.json`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ssm/resources/ecs/optimized_amis/eu-central-1.json` & `moto-4.1.7.dev9/moto/ssm/resources/ecs/optimized_amis/eu-central-1.json`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ssm/resources/ecs/optimized_amis/eu-central-2.json` & `moto-4.1.7.dev9/moto/ssm/resources/ecs/optimized_amis/eu-central-2.json`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ssm/resources/ecs/optimized_amis/eu-north-1.json` & `moto-4.1.7.dev9/moto/ssm/resources/ecs/optimized_amis/eu-north-1.json`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ssm/resources/ecs/optimized_amis/eu-south-1.json` & `moto-4.1.7.dev9/moto/ssm/resources/ecs/optimized_amis/eu-south-1.json`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ssm/resources/ecs/optimized_amis/eu-south-2.json` & `moto-4.1.7.dev9/moto/ssm/resources/ecs/optimized_amis/eu-south-2.json`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ssm/resources/ecs/optimized_amis/eu-west-1.json` & `moto-4.1.7.dev9/moto/ssm/resources/ecs/optimized_amis/eu-west-1.json`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ssm/resources/ecs/optimized_amis/eu-west-2.json` & `moto-4.1.7.dev9/moto/ssm/resources/ecs/optimized_amis/eu-west-2.json`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ssm/resources/ecs/optimized_amis/eu-west-3.json` & `moto-4.1.7.dev9/moto/ssm/resources/ecs/optimized_amis/eu-west-3.json`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ssm/resources/ecs/optimized_amis/me-central-1.json` & `moto-4.1.7.dev9/moto/ssm/resources/ecs/optimized_amis/me-central-1.json`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ssm/resources/ecs/optimized_amis/me-south-1.json` & `moto-4.1.7.dev9/moto/ssm/resources/ecs/optimized_amis/me-south-1.json`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ssm/resources/ecs/optimized_amis/sa-east-1.json` & `moto-4.1.7.dev9/moto/ssm/resources/ecs/optimized_amis/sa-east-1.json`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ssm/resources/ecs/optimized_amis/us-east-1.json` & `moto-4.1.7.dev9/moto/ssm/resources/ecs/optimized_amis/us-east-1.json`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ssm/resources/ecs/optimized_amis/us-east-2.json` & `moto-4.1.7.dev9/moto/ssm/resources/ecs/optimized_amis/us-east-2.json`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ssm/resources/ecs/optimized_amis/us-west-1.json` & `moto-4.1.7.dev9/moto/ssm/resources/ecs/optimized_amis/us-west-1.json`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ssm/resources/ecs/optimized_amis/us-west-2.json` & `moto-4.1.7.dev9/moto/ssm/resources/ecs/optimized_amis/us-west-2.json`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ssm/resources/regions.json` & `moto-4.1.7.dev9/moto/ssm/resources/regions.json`

 * *Files 0% similar despite different names*

#### Pretty-printed

 * *Similarity: 0.9999803902072643%*

 * *Differences: {"'aws'": "{'service': {'global-infrastructure': {'regions': {'af-south-1': {'services': "*

 * *          "{'launchwizard': OrderedDict([('Value', 'launchwizard')])}}, 'ap-east-1': {'services': "*

 * *          "{'launchwizard': OrderedDict([('Value', 'launchwizard')])}}, 'ap-northeast-1': "*

 * *          "{'services': {'launchwizard': OrderedDict([('Value', 'launchwizard')])}}, "*

 * *          "'ap-northeast-2': {'services': {'launchwizard': OrderedDict([('Value', "*

 * *          "'launchwizard')])}}, 'ap-northeast-3': {'servic […]*

```diff
@@ -783,14 +783,17 @@
                                 "endpoint": {
                                     "Value": "lambda.af-south-1.amazonaws.com"
                                 },
                                 "protocols": {
                                     "Value": "HTTPS"
                                 }
                             },
+                            "launchwizard": {
+                                "Value": "launchwizard"
+                            },
                             "lex-runtime": {
                                 "Value": "lex-runtime",
                                 "endpoint": {
                                     "Value": "runtime-v2-lex.af-south-1.amazonaws.com"
                                 },
                                 "protocols": {
                                     "Value": "HTTPS"
@@ -2269,14 +2272,17 @@
                                 "endpoint": {
                                     "Value": "lambda.ap-east-1.amazonaws.com"
                                 },
                                 "protocols": {
                                     "Value": "HTTPS"
                                 }
                             },
+                            "launchwizard": {
+                                "Value": "launchwizard"
+                            },
                             "license-manager": {
                                 "Value": "license-manager",
                                 "endpoint": {
                                     "Value": "license-manager.ap-east-1.amazonaws.com"
                                 },
                                 "protocols": {
                                     "Value": "HTTPS"
@@ -4349,14 +4355,17 @@
                                 "endpoint": {
                                     "Value": "lambda.ap-northeast-1.amazonaws.com"
                                 },
                                 "protocols": {
                                     "Value": "HTTPS"
                                 }
                             },
+                            "launchwizard": {
+                                "Value": "launchwizard"
+                            },
                             "lex-models": {
                                 "Value": "lex-models",
                                 "endpoint": {
                                     "Value": "models.lex.ap-northeast-1.amazonaws.com"
                                 },
                                 "protocols": {
                                     "Value": "HTTPS"
@@ -6704,14 +6713,17 @@
                                 "endpoint": {
                                     "Value": "lambda.ap-northeast-2.amazonaws.com"
                                 },
                                 "protocols": {
                                     "Value": "HTTPS"
                                 }
                             },
+                            "launchwizard": {
+                                "Value": "launchwizard"
+                            },
                             "lex-runtime": {
                                 "Value": "lex-runtime",
                                 "endpoint": {
                                     "Value": "runtime-v2-lex.ap-northeast-2.amazonaws.com"
                                 },
                                 "protocols": {
                                     "Value": "HTTPS"
@@ -8336,14 +8348,17 @@
                                 "endpoint": {
                                     "Value": "lambda.ap-northeast-3.amazonaws.com"
                                 },
                                 "protocols": {
                                     "Value": "HTTPS"
                                 }
                             },
+                            "launchwizard": {
+                                "Value": "launchwizard"
+                            },
                             "license-manager": {
                                 "Value": "license-manager",
                                 "endpoint": {
                                     "Value": "license-manager.ap-northeast-3.amazonaws.com"
                                 },
                                 "protocols": {
                                     "Value": "HTTPS"
@@ -10079,14 +10094,17 @@
                                 "endpoint": {
                                     "Value": "lambda.ap-south-1.amazonaws.com"
                                 },
                                 "protocols": {
                                     "Value": "HTTPS"
                                 }
                             },
+                            "launchwizard": {
+                                "Value": "launchwizard"
+                            },
                             "license-manager": {
                                 "Value": "license-manager",
                                 "endpoint": {
                                     "Value": "license-manager.ap-south-1.amazonaws.com"
                                 },
                                 "protocols": {
                                     "Value": "HTTPS"
@@ -11094,14 +11112,23 @@
                                 "endpoint": {
                                     "Value": "appconfig.ap-south-2.amazonaws.com"
                                 },
                                 "protocols": {
                                     "Value": "HTTPS"
                                 }
                             },
+                            "appconfigdata": {
+                                "Value": "appconfigdata",
+                                "endpoint": {
+                                    "Value": "appconfigdata.ap-south-2.amazonaws.com"
+                                },
+                                "protocols": {
+                                    "Value": "HTTPS"
+                                }
+                            },
                             "artifact": {
                                 "Value": "artifact"
                             },
                             "aurora": {
                                 "Value": "aurora",
                                 "endpoint": {
                                     "Value": "rds.ap-south-2.amazonaws.com"
@@ -11499,14 +11526,23 @@
                                 "endpoint": {
                                     "Value": "redshift.ap-south-2.amazonaws.com"
                                 },
                                 "protocols": {
                                     "Value": "HTTPS"
                                 }
                             },
+                            "redshift-data": {
+                                "Value": "redshift-data",
+                                "endpoint": {
+                                    "Value": "redshift-data.ap-south-2.amazonaws.com"
+                                },
+                                "protocols": {
+                                    "Value": "HTTPS"
+                                }
+                            },
                             "resource-groups": {
                                 "Value": "resource-groups",
                                 "endpoint": {
                                     "Value": "resource-groups.ap-south-2.amazonaws.com"
                                 },
                                 "protocols": {
                                     "Value": "HTTPS"
@@ -11544,14 +11580,23 @@
                                 "endpoint": {
                                     "Value": "secretsmanager.ap-south-2.amazonaws.com"
                                 },
                                 "protocols": {
                                     "Value": "HTTPS"
                                 }
                             },
+                            "securityhub": {
+                                "Value": "securityhub",
+                                "endpoint": {
+                                    "Value": "securityhub.ap-south-2.amazonaws.com"
+                                },
+                                "protocols": {
+                                    "Value": "HTTPS"
+                                }
+                            },
                             "servicediscovery": {
                                 "Value": "servicediscovery",
                                 "endpoint": {
                                     "Value": "servicediscovery.ap-south-2.amazonaws.com"
                                 },
                                 "protocols": {
                                     "Value": "HTTPS"
@@ -13002,14 +13047,17 @@
                                 "endpoint": {
                                     "Value": "lambda.ap-southeast-1.amazonaws.com"
                                 },
                                 "protocols": {
                                     "Value": "HTTPS"
                                 }
                             },
+                            "launchwizard": {
+                                "Value": "launchwizard"
+                            },
                             "lex-models": {
                                 "Value": "lex-models",
                                 "endpoint": {
                                     "Value": "models.lex.ap-southeast-1.amazonaws.com"
                                 },
                                 "protocols": {
                                     "Value": "HTTPS"
@@ -13716,14 +13764,23 @@
                                 "endpoint": {
                                     "Value": "securityhub.ap-southeast-1.amazonaws.com"
                                 },
                                 "protocols": {
                                     "Value": "HTTPS"
                                 }
                             },
+                            "securitylake": {
+                                "Value": "securitylake",
+                                "endpoint": {
+                                    "Value": "securitylake.ap-southeast-1.amazonaws.com"
+                                },
+                                "protocols": {
+                                    "Value": "HTTPS"
+                                }
+                            },
                             "serverlessrepo": {
                                 "Value": "serverlessrepo",
                                 "endpoint": {
                                     "Value": "serverlessrepo.ap-southeast-1.amazonaws.com"
                                 },
                                 "protocols": {
                                     "Value": "HTTPS"
@@ -15480,14 +15537,17 @@
                                 "endpoint": {
                                     "Value": "lambda.ap-southeast-2.amazonaws.com"
                                 },
                                 "protocols": {
                                     "Value": "HTTPS"
                                 }
                             },
+                            "launchwizard": {
+                                "Value": "launchwizard"
+                            },
                             "lex-models": {
                                 "Value": "lex-models",
                                 "endpoint": {
                                     "Value": "models.lex.ap-southeast-2.amazonaws.com"
                                 },
                                 "protocols": {
                                     "Value": "HTTPS"
@@ -16729,14 +16789,23 @@
                                 "endpoint": {
                                     "Value": "appconfig.ap-southeast-3.amazonaws.com"
                                 },
                                 "protocols": {
                                     "Value": "HTTPS"
                                 }
                             },
+                            "appconfigdata": {
+                                "Value": "appconfigdata",
+                                "endpoint": {
+                                    "Value": "appconfigdata.ap-southeast-3.amazonaws.com"
+                                },
+                                "protocols": {
+                                    "Value": "HTTPS"
+                                }
+                            },
                             "application-autoscaling": {
                                 "Value": "application-autoscaling",
                                 "endpoint": {
                                     "Value": "autoscaling-plans.ap-southeast-3.amazonaws.com"
                                 },
                                 "protocols": {
                                     "Value": "HTTPS, HTTP"
@@ -17807,14 +17876,23 @@
                                 "endpoint": {
                                     "Value": "appconfig.ap-southeast-4.amazonaws.com"
                                 },
                                 "protocols": {
                                     "Value": "HTTPS"
                                 }
                             },
+                            "appconfigdata": {
+                                "Value": "appconfigdata",
+                                "endpoint": {
+                                    "Value": "appconfigdata.ap-southeast-4.amazonaws.com"
+                                },
+                                "protocols": {
+                                    "Value": "HTTPS"
+                                }
+                            },
                             "artifact": {
                                 "Value": "artifact"
                             },
                             "aurora": {
                                 "Value": "aurora",
                                 "endpoint": {
                                     "Value": "rds.ap-southeast-4.amazonaws.com"
@@ -19533,14 +19611,17 @@
                                 "endpoint": {
                                     "Value": "lambda.ca-central-1.amazonaws.com"
                                 },
                                 "protocols": {
                                     "Value": "HTTPS"
                                 }
                             },
+                            "launchwizard": {
+                                "Value": "launchwizard"
+                            },
                             "lex-runtime": {
                                 "Value": "lex-runtime",
                                 "endpoint": {
                                     "Value": "runtime-v2-lex.ca-central-1.amazonaws.com"
                                 },
                                 "protocols": {
                                     "Value": "HTTPS"
@@ -21315,14 +21396,23 @@
                                 "endpoint": {
                                     "Value": "rds.cn-north-1.amazonaws.com.cn"
                                 },
                                 "protocols": {
                                     "Value": "HTTPS, HTTP"
                                 }
                             },
+                            "oam": {
+                                "Value": "oam",
+                                "endpoint": {
+                                    "Value": "oam.cn-north-1.amazonaws.com.cn"
+                                },
+                                "protocols": {
+                                    "Value": "HTTPS"
+                                }
+                            },
                             "organizations": {
                                 "Value": "organizations",
                                 "endpoint": {
                                     "Value": "organizations.cn-northwest-1.amazonaws.com.cn"
                                 },
                                 "protocols": {
                                     "Value": "HTTPS"
@@ -22507,14 +22597,23 @@
                                 "endpoint": {
                                     "Value": "rds.cn-northwest-1.amazonaws.com.cn"
                                 },
                                 "protocols": {
                                     "Value": "HTTPS, HTTP"
                                 }
                             },
+                            "oam": {
+                                "Value": "oam",
+                                "endpoint": {
+                                    "Value": "oam.cn-northwest-1.amazonaws.com.cn"
+                                },
+                                "protocols": {
+                                    "Value": "HTTPS"
+                                }
+                            },
                             "organizations": {
                                 "Value": "organizations",
                                 "endpoint": {
                                     "Value": "organizations.cn-northwest-1.amazonaws.com.cn"
                                 },
                                 "protocols": {
                                     "Value": "HTTPS"
@@ -24334,14 +24433,17 @@
                                 "endpoint": {
                                     "Value": "lambda.eu-central-1.amazonaws.com"
                                 },
                                 "protocols": {
                                     "Value": "HTTPS"
                                 }
                             },
+                            "launchwizard": {
+                                "Value": "launchwizard"
+                            },
                             "lex-models": {
                                 "Value": "lex-models",
                                 "endpoint": {
                                     "Value": "models.lex.eu-central-1.amazonaws.com"
                                 },
                                 "protocols": {
                                     "Value": "HTTPS"
@@ -25579,14 +25681,23 @@
                                 "endpoint": {
                                     "Value": "appconfig.eu-central-2.amazonaws.com"
                                 },
                                 "protocols": {
                                     "Value": "HTTPS"
                                 }
                             },
+                            "appconfigdata": {
+                                "Value": "appconfigdata",
+                                "endpoint": {
+                                    "Value": "appconfigdata.eu-central-2.amazonaws.com"
+                                },
+                                "protocols": {
+                                    "Value": "HTTPS"
+                                }
+                            },
                             "artifact": {
                                 "Value": "artifact"
                             },
                             "aurora": {
                                 "Value": "aurora",
                                 "endpoint": {
                                     "Value": "rds.eu-central-2.amazonaws.com"
@@ -25993,14 +26104,23 @@
                                 "endpoint": {
                                     "Value": "redshift.eu-central-2.amazonaws.com"
                                 },
                                 "protocols": {
                                     "Value": "HTTPS"
                                 }
                             },
+                            "redshift-data": {
+                                "Value": "redshift-data",
+                                "endpoint": {
+                                    "Value": "redshift-data.eu-central-2.amazonaws.com"
+                                },
+                                "protocols": {
+                                    "Value": "HTTPS"
+                                }
+                            },
                             "resource-groups": {
                                 "Value": "resource-groups",
                                 "endpoint": {
                                     "Value": "resource-groups.eu-central-2.amazonaws.com"
                                 },
                                 "protocols": {
                                     "Value": "HTTPS"
@@ -26038,23 +26158,59 @@
                                 "endpoint": {
                                     "Value": "s3.eu-central-2.amazonaws.com"
                                 },
                                 "protocols": {
                                     "Value": "HTTPS, HTTP"
                                 }
                             },
+                            "sagemaker": {
+                                "Value": "sagemaker",
+                                "endpoint": {
+                                    "Value": "api.sagemaker.eu-central-2.amazonaws.com"
+                                },
+                                "protocols": {
+                                    "Value": "HTTPS"
+                                }
+                            },
+                            "sagemaker-metrics": {
+                                "Value": "sagemaker-metrics",
+                                "endpoint": {
+                                    "Value": "metrics.sagemaker.eu-central-2.amazonaws.com"
+                                },
+                                "protocols": {
+                                    "Value": "HTTPS"
+                                }
+                            },
+                            "sagemaker-runtime": {
+                                "Value": "sagemaker-runtime",
+                                "endpoint": {
+                                    "Value": "runtime.sagemaker.eu-central-2.amazonaws.com"
+                                },
+                                "protocols": {
+                                    "Value": "HTTPS"
+                                }
+                            },
                             "secretsmanager": {
                                 "Value": "secretsmanager",
                                 "endpoint": {
                                     "Value": "secretsmanager.eu-central-2.amazonaws.com"
                                 },
                                 "protocols": {
                                     "Value": "HTTPS"
                                 }
                             },
+                            "securityhub": {
+                                "Value": "securityhub",
+                                "endpoint": {
+                                    "Value": "securityhub.eu-central-2.amazonaws.com"
+                                },
+                                "protocols": {
+                                    "Value": "HTTPS"
+                                }
+                            },
                             "servicediscovery": {
                                 "Value": "servicediscovery",
                                 "endpoint": {
                                     "Value": "servicediscovery.eu-central-2.amazonaws.com"
                                 },
                                 "protocols": {
                                     "Value": "HTTPS"
@@ -27200,14 +27356,17 @@
                                 "endpoint": {
                                     "Value": "lambda.eu-north-1.amazonaws.com"
                                 },
                                 "protocols": {
                                     "Value": "HTTPS"
                                 }
                             },
+                            "launchwizard": {
+                                "Value": "launchwizard"
+                            },
                             "license-manager": {
                                 "Value": "license-manager",
                                 "endpoint": {
                                     "Value": "license-manager.eu-north-1.amazonaws.com"
                                 },
                                 "protocols": {
                                     "Value": "HTTPS"
@@ -28836,14 +28995,17 @@
                                 "endpoint": {
                                     "Value": "lambda.eu-south-1.amazonaws.com"
                                 },
                                 "protocols": {
                                     "Value": "HTTPS"
                                 }
                             },
+                            "launchwizard": {
+                                "Value": "launchwizard"
+                            },
                             "license-manager": {
                                 "Value": "license-manager",
                                 "endpoint": {
                                     "Value": "license-manager.eu-south-1.amazonaws.com"
                                 },
                                 "protocols": {
                                     "Value": "HTTPS"
@@ -29485,14 +29647,23 @@
                                 "endpoint": {
                                     "Value": "appconfig.eu-south-2.amazonaws.com"
                                 },
                                 "protocols": {
                                     "Value": "HTTPS"
                                 }
                             },
+                            "appconfigdata": {
+                                "Value": "appconfigdata",
+                                "endpoint": {
+                                    "Value": "appconfigdata.eu-south-2.amazonaws.com"
+                                },
+                                "protocols": {
+                                    "Value": "HTTPS"
+                                }
+                            },
                             "artifact": {
                                 "Value": "artifact"
                             },
                             "aurora": {
                                 "Value": "aurora",
                                 "endpoint": {
                                     "Value": "rds.eu-south-2.amazonaws.com"
@@ -29944,14 +30115,23 @@
                                 "endpoint": {
                                     "Value": "secretsmanager.eu-south-2.amazonaws.com"
                                 },
                                 "protocols": {
                                     "Value": "HTTPS"
                                 }
                             },
+                            "securityhub": {
+                                "Value": "securityhub",
+                                "endpoint": {
+                                    "Value": "securityhub.eu-south-2.amazonaws.com"
+                                },
+                                "protocols": {
+                                    "Value": "HTTPS"
+                                }
+                            },
                             "servicediscovery": {
                                 "Value": "servicediscovery",
                                 "endpoint": {
                                     "Value": "servicediscovery.eu-south-2.amazonaws.com"
                                 },
                                 "protocols": {
                                     "Value": "HTTPS"
@@ -31469,14 +31649,17 @@
                                 "endpoint": {
                                     "Value": "lambda.eu-west-1.amazonaws.com"
                                 },
                                 "protocols": {
                                     "Value": "HTTPS"
                                 }
                             },
+                            "launchwizard": {
+                                "Value": "launchwizard"
+                            },
                             "lex-models": {
                                 "Value": "lex-models",
                                 "endpoint": {
                                     "Value": "models.lex.eu-west-1.amazonaws.com"
                                 },
                                 "protocols": {
                                     "Value": "HTTPS"
@@ -33954,14 +34137,17 @@
                                 "endpoint": {
                                     "Value": "lambda.eu-west-2.amazonaws.com"
                                 },
                                 "protocols": {
                                     "Value": "HTTPS"
                                 }
                             },
+                            "launchwizard": {
+                                "Value": "launchwizard"
+                            },
                             "lex-models": {
                                 "Value": "lex-models",
                                 "endpoint": {
                                     "Value": "models.lex.eu-west-2.amazonaws.com"
                                 },
                                 "protocols": {
                                     "Value": "HTTPS"
@@ -34608,14 +34794,23 @@
                                 "endpoint": {
                                     "Value": "securityhub.eu-west-2.amazonaws.com"
                                 },
                                 "protocols": {
                                     "Value": "HTTPS"
                                 }
                             },
+                            "securitylake": {
+                                "Value": "securitylake",
+                                "endpoint": {
+                                    "Value": "securitylake.eu-west-2.amazonaws.com"
+                                },
+                                "protocols": {
+                                    "Value": "HTTPS"
+                                }
+                            },
                             "serverlessrepo": {
                                 "Value": "serverlessrepo",
                                 "endpoint": {
                                     "Value": "serverlessrepo.eu-west-2.amazonaws.com"
                                 },
                                 "protocols": {
                                     "Value": "HTTPS"
@@ -35949,14 +36144,17 @@
                                 "endpoint": {
                                     "Value": "lambda.eu-west-3.amazonaws.com"
                                 },
                                 "protocols": {
                                     "Value": "HTTPS"
                                 }
                             },
+                            "launchwizard": {
+                                "Value": "launchwizard"
+                            },
                             "license-manager": {
                                 "Value": "license-manager",
                                 "endpoint": {
                                     "Value": "license-manager.eu-west-3.amazonaws.com"
                                 },
                                 "protocols": {
                                     "Value": "HTTPS"
@@ -36865,14 +37063,23 @@
                                 "endpoint": {
                                     "Value": "appconfig.me-central-1.amazonaws.com"
                                 },
                                 "protocols": {
                                     "Value": "HTTPS"
                                 }
                             },
+                            "appconfigdata": {
+                                "Value": "appconfigdata",
+                                "endpoint": {
+                                    "Value": "appconfigdata.me-central-1.amazonaws.com"
+                                },
+                                "protocols": {
+                                    "Value": "HTTPS"
+                                }
+                            },
                             "artifact": {
                                 "Value": "artifact"
                             },
                             "aurora": {
                                 "Value": "aurora",
                                 "endpoint": {
                                     "Value": "rds.me-central-1.amazonaws.com"
@@ -37552,14 +37759,23 @@
                                 "endpoint": {
                                     "Value": "servicequotas.me-central-1.amazonaws.com"
                                 },
                                 "protocols": {
                                     "Value": "HTTPS"
                                 }
                             },
+                            "servicecatalog": {
+                                "Value": "servicecatalog",
+                                "endpoint": {
+                                    "Value": "servicecatalog.me-central-1.amazonaws.com"
+                                },
+                                "protocols": {
+                                    "Value": "HTTPS"
+                                }
+                            },
                             "servicecatalog-appregistry": {
                                 "Value": "servicecatalog-appregistry",
                                 "endpoint": {
                                     "Value": "servicecatalog-appregistry.me-central-1.amazonaws.com"
                                 },
                                 "protocols": {
                                     "Value": "HTTPS"
@@ -38561,14 +38777,17 @@
                                 "endpoint": {
                                     "Value": "lambda.me-south-1.amazonaws.com"
                                 },
                                 "protocols": {
                                     "Value": "HTTPS"
                                 }
                             },
+                            "launchwizard": {
+                                "Value": "launchwizard"
+                            },
                             "license-manager": {
                                 "Value": "license-manager",
                                 "endpoint": {
                                     "Value": "license-manager.me-south-1.amazonaws.com"
                                 },
                                 "protocols": {
                                     "Value": "HTTPS"
@@ -40206,14 +40425,17 @@
                                 "endpoint": {
                                     "Value": "lambda.sa-east-1.amazonaws.com"
                                 },
                                 "protocols": {
                                     "Value": "HTTPS"
                                 }
                             },
+                            "launchwizard": {
+                                "Value": "launchwizard"
+                            },
                             "license-manager": {
                                 "Value": "license-manager",
                                 "endpoint": {
                                     "Value": "license-manager.sa-east-1.amazonaws.com"
                                 },
                                 "protocols": {
                                     "Value": "HTTPS"
@@ -40701,14 +40923,23 @@
                                 "endpoint": {
                                     "Value": "securityhub.sa-east-1.amazonaws.com"
                                 },
                                 "protocols": {
                                     "Value": "HTTPS"
                                 }
                             },
+                            "securitylake": {
+                                "Value": "securitylake",
+                                "endpoint": {
+                                    "Value": "securitylake.sa-east-1.amazonaws.com"
+                                },
+                                "protocols": {
+                                    "Value": "HTTPS"
+                                }
+                            },
                             "serverlessrepo": {
                                 "Value": "serverlessrepo",
                                 "endpoint": {
                                     "Value": "serverlessrepo.sa-east-1.amazonaws.com"
                                 },
                                 "protocols": {
                                     "Value": "HTTPS"
@@ -42696,14 +42927,17 @@
                                 "endpoint": {
                                     "Value": "lambda.us-east-1.amazonaws.com"
                                 },
                                 "protocols": {
                                     "Value": "HTTPS"
                                 }
                             },
+                            "launchwizard": {
+                                "Value": "launchwizard"
+                            },
                             "lex-models": {
                                 "Value": "lex-models",
                                 "endpoint": {
                                     "Value": "models.lex.us-east-1.amazonaws.com"
                                 },
                                 "protocols": {
                                     "Value": "HTTPS"
@@ -45399,14 +45633,17 @@
                                 "endpoint": {
                                     "Value": "lambda.us-east-2.amazonaws.com"
                                 },
                                 "protocols": {
                                     "Value": "HTTPS"
                                 }
                             },
+                            "launchwizard": {
+                                "Value": "launchwizard"
+                            },
                             "license-manager": {
                                 "Value": "license-manager",
                                 "endpoint": {
                                     "Value": "license-manager.us-east-2.amazonaws.com"
                                 },
                                 "protocols": {
                                     "Value": "HTTPS"
@@ -47179,14 +47416,17 @@
                                 "endpoint": {
                                     "Value": "lambda.us-gov-east-1.amazonaws.com"
                                 },
                                 "protocols": {
                                     "Value": "HTTPS"
                                 }
                             },
+                            "launchwizard": {
+                                "Value": "launchwizard"
+                            },
                             "license-manager": {
                                 "Value": "license-manager",
                                 "endpoint": {
                                     "Value": "license-manager.us-gov-east-1.amazonaws.com"
                                 },
                                 "protocols": {
                                     "Value": "HTTPS"
@@ -48503,14 +48743,17 @@
                                 "endpoint": {
                                     "Value": "iotsitewise.us-gov-west-1.amazonaws.com"
                                 },
                                 "protocols": {
                                     "Value": "HTTPS"
                                 }
                             },
+                            "iottwinmaker": {
+                                "Value": "iottwinmaker"
+                            },
                             "kafka": {
                                 "Value": "kafka",
                                 "endpoint": {
                                     "Value": "kafka.us-gov-west-1.amazonaws.com"
                                 },
                                 "protocols": {
                                     "Value": "HTTPS"
@@ -48566,14 +48809,17 @@
                                 "endpoint": {
                                     "Value": "lambda.us-gov-west-1.amazonaws.com"
                                 },
                                 "protocols": {
                                     "Value": "HTTPS"
                                 }
                             },
+                            "launchwizard": {
+                                "Value": "launchwizard"
+                            },
                             "lex-models": {
                                 "Value": "lex-models",
                                 "endpoint": {
                                     "Value": "models.lex.us-gov-west-1.amazonaws.com"
                                 },
                                 "protocols": {
                                     "Value": "HTTPS"
@@ -50181,14 +50427,17 @@
                                 "endpoint": {
                                     "Value": "lambda.us-west-1.amazonaws.com"
                                 },
                                 "protocols": {
                                     "Value": "HTTPS"
                                 }
                             },
+                            "launchwizard": {
+                                "Value": "launchwizard"
+                            },
                             "license-manager": {
                                 "Value": "license-manager",
                                 "endpoint": {
                                     "Value": "license-manager.us-west-1.amazonaws.com"
                                 },
                                 "protocols": {
                                     "Value": "HTTPS"
@@ -52620,14 +52869,17 @@
                                 "endpoint": {
                                     "Value": "lambda.us-west-2.amazonaws.com"
                                 },
                                 "protocols": {
                                     "Value": "HTTPS"
                                 }
                             },
+                            "launchwizard": {
+                                "Value": "launchwizard"
+                            },
                             "lex-models": {
                                 "Value": "lex-models",
                                 "endpoint": {
                                     "Value": "models.lex.us-west-2.amazonaws.com"
                                 },
                                 "protocols": {
                                     "Value": "HTTPS"
@@ -53733,17 +53985,14 @@
                                 "endpoint": {
                                     "Value": "transcribe.us-west-2.amazonaws.com"
                                 },
                                 "protocols": {
                                     "Value": "HTTPS"
                                 }
                             },
-                            "transcribemedical": {
-                                "Value": "transcribemedical"
-                            },
                             "transfer": {
                                 "Value": "transfer",
                                 "endpoint": {
                                     "Value": "transfer.us-west-2.amazonaws.com"
                                 },
                                 "protocols": {
                                     "Value": "HTTPS"
```

### Comparing `moto-4.1.7.dev8/moto/ssm/resources/services.json` & `moto-4.1.7.dev9/moto/ssm/resources/services.json`

 * *Files 0% similar despite different names*

#### Pretty-printed

 * *Similarity: 0.9997412890495516%*

 * *Differences: {"'aws'": "{'service': {'global-infrastructure': {'services': {'appconfigdata': {'regions': "*

 * *          "{'ap-south-2': OrderedDict([('Value', 'ap-south-2'), ('endpoint', "*

 * *          "OrderedDict([('Value', 'appconfigdata.ap-south-2.amazonaws.com')])), ('protocols', "*

 * *          "OrderedDict([('Value', 'HTTPS')]))]), 'ap-southeast-3': OrderedDict([('Value', "*

 * *          "'ap-southeast-3'), ('endpoint', OrderedDict([('Value', "*

 * *          "'appconfigdata.ap-southeast-3.amazonaws.com')])), ('protocols', OrderedD […]*

```diff
@@ -2705,14 +2705,23 @@
                                 "endpoint": {
                                     "Value": "appconfigdata.ap-south-1.amazonaws.com"
                                 },
                                 "protocols": {
                                     "Value": "HTTPS"
                                 }
                             },
+                            "ap-south-2": {
+                                "Value": "ap-south-2",
+                                "endpoint": {
+                                    "Value": "appconfigdata.ap-south-2.amazonaws.com"
+                                },
+                                "protocols": {
+                                    "Value": "HTTPS"
+                                }
+                            },
                             "ap-southeast-1": {
                                 "Value": "ap-southeast-1",
                                 "endpoint": {
                                     "Value": "appconfigdata.ap-southeast-1.amazonaws.com"
                                 },
                                 "protocols": {
                                     "Value": "HTTPS"
@@ -2723,14 +2732,32 @@
                                 "endpoint": {
                                     "Value": "appconfigdata.ap-southeast-2.amazonaws.com"
                                 },
                                 "protocols": {
                                     "Value": "HTTPS"
                                 }
                             },
+                            "ap-southeast-3": {
+                                "Value": "ap-southeast-3",
+                                "endpoint": {
+                                    "Value": "appconfigdata.ap-southeast-3.amazonaws.com"
+                                },
+                                "protocols": {
+                                    "Value": "HTTPS"
+                                }
+                            },
+                            "ap-southeast-4": {
+                                "Value": "ap-southeast-4",
+                                "endpoint": {
+                                    "Value": "appconfigdata.ap-southeast-4.amazonaws.com"
+                                },
+                                "protocols": {
+                                    "Value": "HTTPS"
+                                }
+                            },
                             "ca-central-1": {
                                 "Value": "ca-central-1",
                                 "endpoint": {
                                     "Value": "appconfigdata.ca-central-1.amazonaws.com"
                                 },
                                 "protocols": {
                                     "Value": "HTTPS"
@@ -2759,14 +2786,23 @@
                                 "endpoint": {
                                     "Value": "appconfigdata.eu-central-1.amazonaws.com"
                                 },
                                 "protocols": {
                                     "Value": "HTTPS"
                                 }
                             },
+                            "eu-central-2": {
+                                "Value": "eu-central-2",
+                                "endpoint": {
+                                    "Value": "appconfigdata.eu-central-2.amazonaws.com"
+                                },
+                                "protocols": {
+                                    "Value": "HTTPS"
+                                }
+                            },
                             "eu-north-1": {
                                 "Value": "eu-north-1",
                                 "endpoint": {
                                     "Value": "appconfigdata.eu-north-1.amazonaws.com"
                                 },
                                 "protocols": {
                                     "Value": "HTTPS"
@@ -2777,14 +2813,23 @@
                                 "endpoint": {
                                     "Value": "appconfigdata.eu-south-1.amazonaws.com"
                                 },
                                 "protocols": {
                                     "Value": "HTTPS"
                                 }
                             },
+                            "eu-south-2": {
+                                "Value": "eu-south-2",
+                                "endpoint": {
+                                    "Value": "appconfigdata.eu-south-2.amazonaws.com"
+                                },
+                                "protocols": {
+                                    "Value": "HTTPS"
+                                }
+                            },
                             "eu-west-1": {
                                 "Value": "eu-west-1",
                                 "endpoint": {
                                     "Value": "appconfigdata.eu-west-1.amazonaws.com"
                                 },
                                 "protocols": {
                                     "Value": "HTTPS"
@@ -2804,14 +2849,23 @@
                                 "endpoint": {
                                     "Value": "appconfigdata.eu-west-3.amazonaws.com"
                                 },
                                 "protocols": {
                                     "Value": "HTTPS"
                                 }
                             },
+                            "me-central-1": {
+                                "Value": "me-central-1",
+                                "endpoint": {
+                                    "Value": "appconfigdata.me-central-1.amazonaws.com"
+                                },
+                                "protocols": {
+                                    "Value": "HTTPS"
+                                }
+                            },
                             "me-south-1": {
                                 "Value": "me-south-1",
                                 "endpoint": {
                                     "Value": "appconfigdata.me-south-1.amazonaws.com"
                                 },
                                 "protocols": {
                                     "Value": "HTTPS"
@@ -7049,15 +7103,18 @@
                                 }
                             }
                         }
                     },
                     "cleanrooms": {
                         "Value": "cleanrooms",
                         "longName": {
-                            "Value": "CleanRooms"
+                            "Value": "AWS Clean Rooms"
+                        },
+                        "marketingHomeURL": {
+                            "Value": "https://aws.amazon.com/clean-rooms/"
                         },
                         "regions": {
                             "ap-northeast-1": {
                                 "Value": "ap-northeast-1",
                                 "endpoint": {
                                     "Value": "cleanrooms.ap-northeast-1.amazonaws.com"
                                 },
@@ -28683,14 +28740,17 @@
                             },
                             "eu-west-1": {
                                 "Value": "eu-west-1"
                             },
                             "us-east-1": {
                                 "Value": "us-east-1"
                             },
+                            "us-gov-west-1": {
+                                "Value": "us-gov-west-1"
+                            },
                             "us-west-2": {
                                 "Value": "us-west-2"
                             }
                         }
                     },
                     "iotwireless": {
                         "Value": "iotwireless",
@@ -31033,14 +31093,94 @@
                                 },
                                 "protocols": {
                                     "Value": "HTTPS"
                                 }
                             }
                         }
                     },
+                    "launchwizard": {
+                        "Value": "launchwizard",
+                        "longName": {
+                            "Value": "AWS Launch Wizard"
+                        },
+                        "marketingHomeURL": {
+                            "Value": "https://aws.amazon.com/launchwizard/"
+                        },
+                        "regions": {
+                            "af-south-1": {
+                                "Value": "af-south-1"
+                            },
+                            "ap-east-1": {
+                                "Value": "ap-east-1"
+                            },
+                            "ap-northeast-1": {
+                                "Value": "ap-northeast-1"
+                            },
+                            "ap-northeast-2": {
+                                "Value": "ap-northeast-2"
+                            },
+                            "ap-northeast-3": {
+                                "Value": "ap-northeast-3"
+                            },
+                            "ap-south-1": {
+                                "Value": "ap-south-1"
+                            },
+                            "ap-southeast-1": {
+                                "Value": "ap-southeast-1"
+                            },
+                            "ap-southeast-2": {
+                                "Value": "ap-southeast-2"
+                            },
+                            "ca-central-1": {
+                                "Value": "ca-central-1"
+                            },
+                            "eu-central-1": {
+                                "Value": "eu-central-1"
+                            },
+                            "eu-north-1": {
+                                "Value": "eu-north-1"
+                            },
+                            "eu-south-1": {
+                                "Value": "eu-south-1"
+                            },
+                            "eu-west-1": {
+                                "Value": "eu-west-1"
+                            },
+                            "eu-west-2": {
+                                "Value": "eu-west-2"
+                            },
+                            "eu-west-3": {
+                                "Value": "eu-west-3"
+                            },
+                            "me-south-1": {
+                                "Value": "me-south-1"
+                            },
+                            "sa-east-1": {
+                                "Value": "sa-east-1"
+                            },
+                            "us-east-1": {
+                                "Value": "us-east-1"
+                            },
+                            "us-east-2": {
+                                "Value": "us-east-2"
+                            },
+                            "us-gov-east-1": {
+                                "Value": "us-gov-east-1"
+                            },
+                            "us-gov-west-1": {
+                                "Value": "us-gov-west-1"
+                            },
+                            "us-west-1": {
+                                "Value": "us-west-1"
+                            },
+                            "us-west-2": {
+                                "Value": "us-west-2"
+                            }
+                        }
+                    },
                     "lex-models": {
                         "Value": "lex-models",
                         "longName": {
                             "Value": "Amazon Lex Model Building Service"
                         },
                         "regions": {
                             "ap-northeast-1": {
@@ -36787,14 +36927,32 @@
                                 "endpoint": {
                                     "Value": "oam.ca-central-1.amazonaws.com"
                                 },
                                 "protocols": {
                                     "Value": "HTTPS"
                                 }
                             },
+                            "cn-north-1": {
+                                "Value": "cn-north-1",
+                                "endpoint": {
+                                    "Value": "oam.cn-north-1.amazonaws.com.cn"
+                                },
+                                "protocols": {
+                                    "Value": "HTTPS"
+                                }
+                            },
+                            "cn-northwest-1": {
+                                "Value": "cn-northwest-1",
+                                "endpoint": {
+                                    "Value": "oam.cn-northwest-1.amazonaws.com.cn"
+                                },
+                                "protocols": {
+                                    "Value": "HTTPS"
+                                }
+                            },
                             "eu-central-1": {
                                 "Value": "eu-central-1",
                                 "endpoint": {
                                     "Value": "oam.eu-central-1.amazonaws.com"
                                 },
                                 "protocols": {
                                     "Value": "HTTPS"
@@ -36929,14 +37087,17 @@
                         }
                     },
                     "omics": {
                         "Value": "omics",
                         "longName": {
                             "Value": "Amazon Omics"
                         },
+                        "marketingHomeURL": {
+                            "Value": "https://aws.amazon.com/omics/"
+                        },
                         "regions": {
                             "ap-southeast-1": {
                                 "Value": "ap-southeast-1"
                             },
                             "eu-central-1": {
                                 "Value": "eu-central-1"
                             },
@@ -41510,14 +41671,23 @@
                                 "endpoint": {
                                     "Value": "redshift-data.ap-south-1.amazonaws.com"
                                 },
                                 "protocols": {
                                     "Value": "HTTPS"
                                 }
                             },
+                            "ap-south-2": {
+                                "Value": "ap-south-2",
+                                "endpoint": {
+                                    "Value": "redshift-data.ap-south-2.amazonaws.com"
+                                },
+                                "protocols": {
+                                    "Value": "HTTPS"
+                                }
+                            },
                             "ap-southeast-1": {
                                 "Value": "ap-southeast-1",
                                 "endpoint": {
                                     "Value": "redshift-data.ap-southeast-1.amazonaws.com"
                                 },
                                 "protocols": {
                                     "Value": "HTTPS"
@@ -41573,14 +41743,23 @@
                                 "endpoint": {
                                     "Value": "redshift-data.eu-central-1.amazonaws.com"
                                 },
                                 "protocols": {
                                     "Value": "HTTPS"
                                 }
                             },
+                            "eu-central-2": {
+                                "Value": "eu-central-2",
+                                "endpoint": {
+                                    "Value": "redshift-data.eu-central-2.amazonaws.com"
+                                },
+                                "protocols": {
+                                    "Value": "HTTPS"
+                                }
+                            },
                             "eu-north-1": {
                                 "Value": "eu-north-1",
                                 "endpoint": {
                                     "Value": "redshift-data.eu-north-1.amazonaws.com"
                                 },
                                 "protocols": {
                                     "Value": "HTTPS"
@@ -44768,14 +44947,23 @@
                                 "endpoint": {
                                     "Value": "api.sagemaker.eu-central-1.amazonaws.com"
                                 },
                                 "protocols": {
                                     "Value": "HTTPS"
                                 }
                             },
+                            "eu-central-2": {
+                                "Value": "eu-central-2",
+                                "endpoint": {
+                                    "Value": "api.sagemaker.eu-central-2.amazonaws.com"
+                                },
+                                "protocols": {
+                                    "Value": "HTTPS"
+                                }
+                            },
                             "eu-north-1": {
                                 "Value": "eu-north-1",
                                 "endpoint": {
                                     "Value": "api.sagemaker.eu-north-1.amazonaws.com"
                                 },
                                 "protocols": {
                                     "Value": "HTTPS"
@@ -45297,14 +45485,23 @@
                                 "endpoint": {
                                     "Value": "metrics.sagemaker.eu-central-1.amazonaws.com"
                                 },
                                 "protocols": {
                                     "Value": "HTTPS"
                                 }
                             },
+                            "eu-central-2": {
+                                "Value": "eu-central-2",
+                                "endpoint": {
+                                    "Value": "metrics.sagemaker.eu-central-2.amazonaws.com"
+                                },
+                                "protocols": {
+                                    "Value": "HTTPS"
+                                }
+                            },
                             "eu-north-1": {
                                 "Value": "eu-north-1",
                                 "endpoint": {
                                     "Value": "metrics.sagemaker.eu-north-1.amazonaws.com"
                                 },
                                 "protocols": {
                                     "Value": "HTTPS"
@@ -45521,14 +45718,23 @@
                                 "endpoint": {
                                     "Value": "runtime.sagemaker.eu-central-1.amazonaws.com"
                                 },
                                 "protocols": {
                                     "Value": "HTTPS"
                                 }
                             },
+                            "eu-central-2": {
+                                "Value": "eu-central-2",
+                                "endpoint": {
+                                    "Value": "runtime.sagemaker.eu-central-2.amazonaws.com"
+                                },
+                                "protocols": {
+                                    "Value": "HTTPS"
+                                }
+                            },
                             "eu-north-1": {
                                 "Value": "eu-north-1",
                                 "endpoint": {
                                     "Value": "runtime.sagemaker.eu-north-1.amazonaws.com"
                                 },
                                 "protocols": {
                                     "Value": "HTTPS"
@@ -46523,14 +46729,23 @@
                                 "endpoint": {
                                     "Value": "securityhub.ap-south-1.amazonaws.com"
                                 },
                                 "protocols": {
                                     "Value": "HTTPS"
                                 }
                             },
+                            "ap-south-2": {
+                                "Value": "ap-south-2",
+                                "endpoint": {
+                                    "Value": "securityhub.ap-south-2.amazonaws.com"
+                                },
+                                "protocols": {
+                                    "Value": "HTTPS"
+                                }
+                            },
                             "ap-southeast-1": {
                                 "Value": "ap-southeast-1",
                                 "endpoint": {
                                     "Value": "securityhub.ap-southeast-1.amazonaws.com"
                                 },
                                 "protocols": {
                                     "Value": "HTTPS"
@@ -46586,14 +46801,23 @@
                                 "endpoint": {
                                     "Value": "securityhub.eu-central-1.amazonaws.com"
                                 },
                                 "protocols": {
                                     "Value": "HTTPS"
                                 }
                             },
+                            "eu-central-2": {
+                                "Value": "eu-central-2",
+                                "endpoint": {
+                                    "Value": "securityhub.eu-central-2.amazonaws.com"
+                                },
+                                "protocols": {
+                                    "Value": "HTTPS"
+                                }
+                            },
                             "eu-north-1": {
                                 "Value": "eu-north-1",
                                 "endpoint": {
                                     "Value": "securityhub.eu-north-1.amazonaws.com"
                                 },
                                 "protocols": {
                                     "Value": "HTTPS"
@@ -46604,14 +46828,23 @@
                                 "endpoint": {
                                     "Value": "securityhub.eu-south-1.amazonaws.com"
                                 },
                                 "protocols": {
                                     "Value": "HTTPS"
                                 }
                             },
+                            "eu-south-2": {
+                                "Value": "eu-south-2",
+                                "endpoint": {
+                                    "Value": "securityhub.eu-south-2.amazonaws.com"
+                                },
+                                "protocols": {
+                                    "Value": "HTTPS"
+                                }
+                            },
                             "eu-west-1": {
                                 "Value": "eu-west-1",
                                 "endpoint": {
                                     "Value": "securityhub.eu-west-1.amazonaws.com"
                                 },
                                 "protocols": {
                                     "Value": "HTTPS"
@@ -46732,14 +46965,23 @@
                                 "endpoint": {
                                     "Value": "securitylake.ap-northeast-1.amazonaws.com"
                                 },
                                 "protocols": {
                                     "Value": "HTTPS"
                                 }
                             },
+                            "ap-southeast-1": {
+                                "Value": "ap-southeast-1",
+                                "endpoint": {
+                                    "Value": "securitylake.ap-southeast-1.amazonaws.com"
+                                },
+                                "protocols": {
+                                    "Value": "HTTPS"
+                                }
+                            },
                             "ap-southeast-2": {
                                 "Value": "ap-southeast-2",
                                 "endpoint": {
                                     "Value": "securitylake.ap-southeast-2.amazonaws.com"
                                 },
                                 "protocols": {
                                     "Value": "HTTPS"
@@ -46759,14 +47001,32 @@
                                 "endpoint": {
                                     "Value": "securitylake.eu-west-1.amazonaws.com"
                                 },
                                 "protocols": {
                                     "Value": "HTTPS"
                                 }
                             },
+                            "eu-west-2": {
+                                "Value": "eu-west-2",
+                                "endpoint": {
+                                    "Value": "securitylake.eu-west-2.amazonaws.com"
+                                },
+                                "protocols": {
+                                    "Value": "HTTPS"
+                                }
+                            },
+                            "sa-east-1": {
+                                "Value": "sa-east-1",
+                                "endpoint": {
+                                    "Value": "securitylake.sa-east-1.amazonaws.com"
+                                },
+                                "protocols": {
+                                    "Value": "HTTPS"
+                                }
+                            },
                             "us-east-1": {
                                 "Value": "us-east-1",
                                 "endpoint": {
                                     "Value": "securitylake.us-east-1.amazonaws.com"
                                 },
                                 "protocols": {
                                     "Value": "HTTPS"
@@ -47419,14 +47679,23 @@
                                 "endpoint": {
                                     "Value": "servicecatalog.eu-west-3.amazonaws.com"
                                 },
                                 "protocols": {
                                     "Value": "HTTPS"
                                 }
                             },
+                            "me-central-1": {
+                                "Value": "me-central-1",
+                                "endpoint": {
+                                    "Value": "servicecatalog.me-central-1.amazonaws.com"
+                                },
+                                "protocols": {
+                                    "Value": "HTTPS"
+                                }
+                            },
                             "me-south-1": {
                                 "Value": "me-south-1",
                                 "endpoint": {
                                     "Value": "servicecatalog.me-south-1.amazonaws.com"
                                 },
                                 "protocols": {
                                     "Value": "HTTPS"
@@ -48448,14 +48717,17 @@
                         }
                     },
                     "signer": {
                         "Value": "signer",
                         "longName": {
                             "Value": "AWS Signer"
                         },
+                        "marketingHomeURL": {
+                            "Value": "https://docs.aws.amazon.com/signer/latest/developerguide/Welcome.html"
+                        },
                         "regions": {
                             "af-south-1": {
                                 "Value": "af-south-1",
                                 "endpoint": {
                                     "Value": "signer.af-south-1.amazonaws.com"
                                 },
                                 "protocols": {
@@ -53473,17 +53745,14 @@
                                 "Value": "us-east-1"
                             },
                             "us-east-2": {
                                 "Value": "us-east-2"
                             },
                             "us-west-1": {
                                 "Value": "us-west-1"
-                            },
-                            "us-west-2": {
-                                "Value": "us-west-2"
                             }
                         }
                     },
                     "transfer": {
                         "Value": "transfer",
                         "longName": {
                             "Value": "AWS Transfer Family"
```

### Comparing `moto-4.1.7.dev8/moto/ssm/responses.py` & `moto-4.1.7.dev9/moto/ssm/responses.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ssm/utils.py` & `moto-4.1.7.dev9/moto/ssm/utils.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ssoadmin/models.py` & `moto-4.1.7.dev9/moto/ssoadmin/models.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/ssoadmin/responses.py` & `moto-4.1.7.dev9/moto/ssoadmin/responses.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/stepfunctions/exceptions.py` & `moto-4.1.7.dev9/moto/stepfunctions/exceptions.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/stepfunctions/models.py` & `moto-4.1.7.dev9/moto/stepfunctions/models.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/stepfunctions/responses.py` & `moto-4.1.7.dev9/moto/stepfunctions/responses.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/stepfunctions/utils.py` & `moto-4.1.7.dev9/moto/stepfunctions/utils.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/sts/models.py` & `moto-4.1.7.dev9/moto/sts/models.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/sts/responses.py` & `moto-4.1.7.dev9/moto/sts/responses.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/sts/utils.py` & `moto-4.1.7.dev9/moto/sts/utils.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/support/models.py` & `moto-4.1.7.dev9/moto/support/models.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/support/resources/describe_trusted_advisor_checks.json` & `moto-4.1.7.dev9/moto/support/resources/describe_trusted_advisor_checks.json`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/support/responses.py` & `moto-4.1.7.dev9/moto/support/responses.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/swf/constants.py` & `moto-4.1.7.dev9/moto/swf/constants.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/swf/exceptions.py` & `moto-4.1.7.dev9/moto/swf/exceptions.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/swf/models/__init__.py` & `moto-4.1.7.dev9/moto/swf/models/__init__.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/swf/models/activity_task.py` & `moto-4.1.7.dev9/moto/swf/models/activity_task.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/swf/models/decision_task.py` & `moto-4.1.7.dev9/moto/swf/models/decision_task.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/swf/models/domain.py` & `moto-4.1.7.dev9/moto/swf/models/domain.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/swf/models/generic_type.py` & `moto-4.1.7.dev9/moto/swf/models/generic_type.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/swf/models/history_event.py` & `moto-4.1.7.dev9/moto/swf/models/history_event.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/swf/models/workflow_execution.py` & `moto-4.1.7.dev9/moto/swf/models/workflow_execution.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/swf/responses.py` & `moto-4.1.7.dev9/moto/swf/responses.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/textract/exceptions.py` & `moto-4.1.7.dev9/moto/textract/exceptions.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/textract/models.py` & `moto-4.1.7.dev9/moto/textract/models.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/textract/responses.py` & `moto-4.1.7.dev9/moto/textract/responses.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/timestreamwrite/models.py` & `moto-4.1.7.dev9/moto/timestreamwrite/models.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/timestreamwrite/responses.py` & `moto-4.1.7.dev9/moto/timestreamwrite/responses.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/transcribe/models.py` & `moto-4.1.7.dev9/moto/transcribe/models.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/transcribe/responses.py` & `moto-4.1.7.dev9/moto/transcribe/responses.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/utilities/aws_headers.py` & `moto-4.1.7.dev9/moto/utilities/aws_headers.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/utilities/distutils_version.py` & `moto-4.1.7.dev9/moto/utilities/distutils_version.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/utilities/docker_utilities.py` & `moto-4.1.7.dev9/moto/utilities/docker_utilities.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/utilities/paginator.py` & `moto-4.1.7.dev9/moto/utilities/paginator.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/utilities/tagging_service.py` & `moto-4.1.7.dev9/moto/utilities/tagging_service.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/utilities/tokenizer.py` & `moto-4.1.7.dev9/moto/utilities/tokenizer.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/utilities/utils.py` & `moto-4.1.7.dev9/moto/utilities/utils.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/wafv2/exceptions.py` & `moto-4.1.7.dev9/moto/wafv2/exceptions.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/wafv2/models.py` & `moto-4.1.7.dev9/moto/wafv2/models.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/wafv2/responses.py` & `moto-4.1.7.dev9/moto/wafv2/responses.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/xray/exceptions.py` & `moto-4.1.7.dev9/moto/xray/exceptions.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/xray/mock_client.py` & `moto-4.1.7.dev9/moto/xray/mock_client.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/xray/models.py` & `moto-4.1.7.dev9/moto/xray/models.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto/xray/responses.py` & `moto-4.1.7.dev9/moto/xray/responses.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto.egg-info/PKG-INFO` & `moto-4.1.7.dev9/moto.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: moto
-Version: 4.1.7.dev8
+Version: 4.1.7.dev9
 Home-page: https://github.com/getmoto/moto
 Author: Steve Pulec
 Author-email: "spulec@gmail.com"
 License: Apache License 2.0
 Project-URL: Documentation, http://docs.getmoto.org/en/latest/
 Project-URL: Issue tracker, https://github.com/getmoto/moto/issues
 Project-URL: Changelog, https://github.com/getmoto/moto/blob/master/CHANGELOG.md
```

### Comparing `moto-4.1.7.dev8/moto.egg-info/SOURCES.txt` & `moto-4.1.7.dev9/moto.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/moto.egg-info/requires.txt` & `moto-4.1.7.dev9/moto.egg-info/requires.txt`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/setup.cfg` & `moto-4.1.7.dev9/setup.cfg`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 [metadata]
 name = moto
-version = 4.1.7.dev8
+version = 4.1.7.dev9
 long_description = file:README.md
 long_description_content_type = text/markdown
 author = Steve Pulec
 author_email = "spulec@gmail.com"
 url = https://github.com/getmoto/moto
 license = Apache License 2.0
 test_suite = tests
```

### Comparing `moto-4.1.7.dev8/tests/__init__.py` & `moto-4.1.7.dev9/tests/__init__.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/helpers.py` & `moto-4.1.7.dev9/tests/helpers.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_acm/resources/README.md` & `moto-4.1.7.dev9/tests/test_acm/resources/README.md`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_acm/resources/ca.key` & `moto-4.1.7.dev9/tests/test_acm/resources/ca.key`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_acm/resources/ca.pem` & `moto-4.1.7.dev9/tests/test_acm/resources/ca.pem`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_acm/resources/star_moto_com-bad.pem` & `moto-4.1.7.dev9/tests/test_acm/resources/star_moto_com-bad.pem`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_acm/resources/star_moto_com.csr` & `moto-4.1.7.dev9/tests/test_acm/resources/star_moto_com.csr`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_acm/resources/star_moto_com.key` & `moto-4.1.7.dev9/tests/test_acm/resources/star_moto_com.key`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_acm/resources/star_moto_com.pem` & `moto-4.1.7.dev9/tests/test_acm/resources/star_moto_com.pem`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_acm/test_acm.py` & `moto-4.1.7.dev9/tests/test_acm/test_acm.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_acmpca/test_acmpca.py` & `moto-4.1.7.dev9/tests/test_acmpca/test_acmpca.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_amp/test_amp_logging_config.py` & `moto-4.1.7.dev9/tests/test_amp/test_amp_logging_config.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_amp/test_amp_rulegroupnamespaces.py` & `moto-4.1.7.dev9/tests/test_amp/test_amp_rulegroupnamespaces.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_amp/test_amp_workspaces.py` & `moto-4.1.7.dev9/tests/test_amp/test_amp_workspaces.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_apigateway/resources/petstore-swagger-v3.yaml` & `moto-4.1.7.dev9/tests/test_apigateway/resources/petstore-swagger-v3.yaml`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_apigateway/resources/test_api.json` & `moto-4.1.7.dev9/tests/test_apigateway/resources/test_api.json`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_apigateway/resources/test_api.yaml` & `moto-4.1.7.dev9/tests/test_apigateway/resources/test_api.yaml`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_apigateway/resources/test_api_invalid.json` & `moto-4.1.7.dev9/tests/test_apigateway/resources/test_api_invalid.json`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_apigateway/resources/test_api_invalid_version.json` & `moto-4.1.7.dev9/tests/test_apigateway/resources/test_api_invalid_version.json`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_apigateway/resources/test_deep_api.yaml` & `moto-4.1.7.dev9/tests/test_apigateway/resources/test_deep_api.yaml`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_apigateway/test_apigateway.py` & `moto-4.1.7.dev9/tests/test_apigateway/test_apigateway.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_apigateway/test_apigateway_cloudformation.py` & `moto-4.1.7.dev9/tests/test_apigateway/test_apigateway_cloudformation.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_apigateway/test_apigateway_deployments.py` & `moto-4.1.7.dev9/tests/test_apigateway/test_apigateway_deployments.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_apigateway/test_apigateway_export.py` & `moto-4.1.7.dev9/tests/test_apigateway/test_apigateway_export.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_apigateway/test_apigateway_gatewayresponses.py` & `moto-4.1.7.dev9/tests/test_apigateway/test_apigateway_gatewayresponses.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_apigateway/test_apigateway_importrestapi.py` & `moto-4.1.7.dev9/tests/test_apigateway/test_apigateway_importrestapi.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_apigateway/test_apigateway_integration.py` & `moto-4.1.7.dev9/tests/test_apigateway/test_apigateway_integration.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_apigateway/test_apigateway_putrestapi.py` & `moto-4.1.7.dev9/tests/test_apigateway/test_apigateway_putrestapi.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_apigateway/test_apigateway_stage.py` & `moto-4.1.7.dev9/tests/test_apigateway/test_apigateway_stage.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_apigateway/test_apigateway_validators.py` & `moto-4.1.7.dev9/tests/test_apigateway/test_apigateway_validators.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_apigateway/test_apigateway_vpclink.py` & `moto-4.1.7.dev9/tests/test_apigateway/test_apigateway_vpclink.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_apigateway/test_server.py` & `moto-4.1.7.dev9/tests/test_apigateway/test_server.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_apigatewayv2/test_apigatewayv2.py` & `moto-4.1.7.dev9/tests/test_apigatewayv2/test_apigatewayv2.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_apigatewayv2/test_apigatewayv2_authorizers.py` & `moto-4.1.7.dev9/tests/test_apigatewayv2/test_apigatewayv2_authorizers.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_apigatewayv2/test_apigatewayv2_domains.py` & `moto-4.1.7.dev9/tests/test_apigatewayv2/test_apigatewayv2_domains.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_apigatewayv2/test_apigatewayv2_integrationresponses.py` & `moto-4.1.7.dev9/tests/test_apigatewayv2/test_apigatewayv2_integrationresponses.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_apigatewayv2/test_apigatewayv2_integrations.py` & `moto-4.1.7.dev9/tests/test_apigatewayv2/test_apigatewayv2_integrations.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_apigatewayv2/test_apigatewayv2_mappings.py` & `moto-4.1.7.dev9/tests/test_apigatewayv2/test_apigatewayv2_mappings.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_apigatewayv2/test_apigatewayv2_models.py` & `moto-4.1.7.dev9/tests/test_apigatewayv2/test_apigatewayv2_models.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_apigatewayv2/test_apigatewayv2_reimport.py` & `moto-4.1.7.dev9/tests/test_apigatewayv2/test_apigatewayv2_reimport.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_apigatewayv2/test_apigatewayv2_routes.py` & `moto-4.1.7.dev9/tests/test_apigatewayv2/test_apigatewayv2_routes.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_apigatewayv2/test_apigatewayv2_tags.py` & `moto-4.1.7.dev9/tests/test_apigatewayv2/test_apigatewayv2_tags.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_apigatewayv2/test_apigatewayv2_vpclinks.py` & `moto-4.1.7.dev9/tests/test_apigatewayv2/test_apigatewayv2_vpclinks.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_applicationautoscaling/test_applicationautoscaling.py` & `moto-4.1.7.dev9/tests/test_applicationautoscaling/test_applicationautoscaling.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_applicationautoscaling/test_validation.py` & `moto-4.1.7.dev9/tests/test_applicationautoscaling/test_validation.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_appsync/test_appsync.py` & `moto-4.1.7.dev9/tests/test_appsync/test_appsync.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_appsync/test_appsync_apikeys.py` & `moto-4.1.7.dev9/tests/test_appsync/test_appsync_apikeys.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_appsync/test_appsync_schema.py` & `moto-4.1.7.dev9/tests/test_appsync/test_appsync_schema.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_appsync/test_appsync_tags.py` & `moto-4.1.7.dev9/tests/test_appsync/test_appsync_tags.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_athena/test_athena.py` & `moto-4.1.7.dev9/tests/test_athena/test_athena.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_athena/test_athena_server_api.py` & `moto-4.1.7.dev9/tests/test_athena/test_athena_server_api.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_autoscaling/test_autoscaling.py` & `moto-4.1.7.dev9/tests/test_autoscaling/test_autoscaling.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_autoscaling/test_autoscaling_cloudformation.py` & `moto-4.1.7.dev9/tests/test_autoscaling/test_autoscaling_cloudformation.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_autoscaling/test_autoscaling_groups.py` & `moto-4.1.7.dev9/tests/test_autoscaling/test_autoscaling_groups.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_autoscaling/test_autoscaling_metrics.py` & `moto-4.1.7.dev9/tests/test_autoscaling/test_autoscaling_metrics.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_autoscaling/test_autoscaling_scheduledactions.py` & `moto-4.1.7.dev9/tests/test_autoscaling/test_autoscaling_scheduledactions.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_autoscaling/test_autoscaling_tags.py` & `moto-4.1.7.dev9/tests/test_autoscaling/test_autoscaling_tags.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_autoscaling/test_elb.py` & `moto-4.1.7.dev9/tests/test_autoscaling/test_elb.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_autoscaling/test_elbv2.py` & `moto-4.1.7.dev9/tests/test_autoscaling/test_elbv2.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_autoscaling/test_launch_configurations.py` & `moto-4.1.7.dev9/tests/test_autoscaling/test_launch_configurations.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_autoscaling/test_policies.py` & `moto-4.1.7.dev9/tests/test_autoscaling/test_policies.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_autoscaling/utils.py` & `moto-4.1.7.dev9/tests/test_autoscaling/utils.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_awslambda/test_awslambda_cloudformation.py` & `moto-4.1.7.dev9/tests/test_awslambda/test_awslambda_cloudformation.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_awslambda/test_lambda.py` & `moto-4.1.7.dev9/tests/test_awslambda/test_lambda.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_awslambda/test_lambda_alias.py` & `moto-4.1.7.dev9/tests/test_awslambda/test_lambda_alias.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_awslambda/test_lambda_concurrency.py` & `moto-4.1.7.dev9/tests/test_awslambda/test_lambda_concurrency.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_awslambda/test_lambda_eventsourcemapping.py` & `moto-4.1.7.dev9/tests/test_awslambda/test_lambda_eventsourcemapping.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_awslambda/test_lambda_function_urls.py` & `moto-4.1.7.dev9/tests/test_awslambda/test_lambda_function_urls.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_awslambda/test_lambda_invoke.py` & `moto-4.1.7.dev9/tests/test_awslambda/test_lambda_invoke.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_awslambda/test_lambda_layers.py` & `moto-4.1.7.dev9/tests/test_awslambda/test_lambda_layers.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_awslambda/test_lambda_policy.py` & `moto-4.1.7.dev9/tests/test_awslambda/test_lambda_policy.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_awslambda/test_lambda_tags.py` & `moto-4.1.7.dev9/tests/test_awslambda/test_lambda_tags.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_awslambda/test_policy.py` & `moto-4.1.7.dev9/tests/test_awslambda/test_policy.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_awslambda/utilities.py` & `moto-4.1.7.dev9/tests/test_awslambda/utilities.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_batch/__init__.py` & `moto-4.1.7.dev9/tests/test_batch/__init__.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_batch/test_batch_cloudformation.py` & `moto-4.1.7.dev9/tests/test_batch/test_batch_cloudformation.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_batch/test_batch_compute_envs.py` & `moto-4.1.7.dev9/tests/test_batch/test_batch_compute_envs.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_batch/test_batch_job_queue.py` & `moto-4.1.7.dev9/tests/test_batch/test_batch_job_queue.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_batch/test_batch_jobs.py` & `moto-4.1.7.dev9/tests/test_batch/test_batch_jobs.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_batch/test_batch_scheduling_policy.py` & `moto-4.1.7.dev9/tests/test_batch/test_batch_scheduling_policy.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_batch/test_batch_tags_job_definition.py` & `moto-4.1.7.dev9/tests/test_batch/test_batch_tags_job_definition.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_batch/test_batch_tags_job_queue.py` & `moto-4.1.7.dev9/tests/test_batch/test_batch_tags_job_queue.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_batch/test_batch_task_definition.py` & `moto-4.1.7.dev9/tests/test_batch/test_batch_task_definition.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_batch_simple/test_batch_cloudformation.py` & `moto-4.1.7.dev9/tests/test_batch_simple/test_batch_cloudformation.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_batch_simple/test_batch_compute_envs.py` & `moto-4.1.7.dev9/tests/test_batch_simple/test_batch_compute_envs.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_batch_simple/test_batch_jobs.py` & `moto-4.1.7.dev9/tests/test_batch_simple/test_batch_jobs.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_budgets/test_budgets.py` & `moto-4.1.7.dev9/tests/test_budgets/test_budgets.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_budgets/test_notifications.py` & `moto-4.1.7.dev9/tests/test_budgets/test_notifications.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_budgets/test_server.py` & `moto-4.1.7.dev9/tests/test_budgets/test_server.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_ce/test_ce.py` & `moto-4.1.7.dev9/tests/test_ce/test_ce.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_ce/test_ce_tags.py` & `moto-4.1.7.dev9/tests/test_ce/test_ce_tags.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_cloudformation/fixtures/custom_lambda.py` & `moto-4.1.7.dev9/tests/test_cloudformation/fixtures/custom_lambda.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_cloudformation/fixtures/kms_key.py` & `moto-4.1.7.dev9/tests/test_cloudformation/fixtures/kms_key.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_cloudformation/fixtures/rds_mysql_with_db_parameter_group.py` & `moto-4.1.7.dev9/tests/test_cloudformation/fixtures/rds_mysql_with_db_parameter_group.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_cloudformation/fixtures/rds_mysql_with_read_replica.py` & `moto-4.1.7.dev9/tests/test_cloudformation/fixtures/rds_mysql_with_read_replica.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_cloudformation/fixtures/redshift.py` & `moto-4.1.7.dev9/tests/test_cloudformation/fixtures/redshift.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_cloudformation/fixtures/route53_ec2_instance_with_public_ip.py` & `moto-4.1.7.dev9/tests/test_cloudformation/fixtures/route53_ec2_instance_with_public_ip.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_cloudformation/fixtures/route53_health_check.py` & `moto-4.1.7.dev9/tests/test_cloudformation/fixtures/route53_health_check.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_cloudformation/fixtures/route53_roundrobin.py` & `moto-4.1.7.dev9/tests/test_cloudformation/fixtures/route53_roundrobin.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_cloudformation/fixtures/single_instance_with_ebs_volume.py` & `moto-4.1.7.dev9/tests/test_cloudformation/fixtures/single_instance_with_ebs_volume.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_cloudformation/fixtures/vpc_eni.py` & `moto-4.1.7.dev9/tests/test_cloudformation/fixtures/vpc_eni.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_cloudformation/fixtures/vpc_single_instance_in_subnet.py` & `moto-4.1.7.dev9/tests/test_cloudformation/fixtures/vpc_single_instance_in_subnet.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_cloudformation/test_cloudformation_custom_resources.py` & `moto-4.1.7.dev9/tests/test_cloudformation/test_cloudformation_custom_resources.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_cloudformation/test_cloudformation_depends_on.py` & `moto-4.1.7.dev9/tests/test_cloudformation/test_cloudformation_depends_on.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_cloudformation/test_cloudformation_multi_accounts.py` & `moto-4.1.7.dev9/tests/test_cloudformation/test_cloudformation_multi_accounts.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_cloudformation/test_cloudformation_nested_stacks.py` & `moto-4.1.7.dev9/tests/test_cloudformation/test_cloudformation_nested_stacks.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_cloudformation/test_cloudformation_stack_crud_boto3.py` & `moto-4.1.7.dev9/tests/test_cloudformation/test_cloudformation_stack_crud_boto3.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_cloudformation/test_cloudformation_stack_integration.py` & `moto-4.1.7.dev9/tests/test_cloudformation/test_cloudformation_stack_integration.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_cloudformation/test_cloudformation_stack_policies.py` & `moto-4.1.7.dev9/tests/test_cloudformation/test_cloudformation_stack_policies.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_cloudformation/test_import_value.py` & `moto-4.1.7.dev9/tests/test_cloudformation/test_import_value.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_cloudformation/test_server.py` & `moto-4.1.7.dev9/tests/test_cloudformation/test_server.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_cloudformation/test_stack_parsing.py` & `moto-4.1.7.dev9/tests/test_cloudformation/test_stack_parsing.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_cloudformation/test_validate.py` & `moto-4.1.7.dev9/tests/test_cloudformation/test_validate.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_cloudfront/cloudfront_test_scaffolding.py` & `moto-4.1.7.dev9/tests/test_cloudfront/cloudfront_test_scaffolding.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_cloudfront/test_cloudfront.py` & `moto-4.1.7.dev9/tests/test_cloudfront/test_cloudfront.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_cloudfront/test_cloudfront_dist_tags.py` & `moto-4.1.7.dev9/tests/test_cloudfront/test_cloudfront_dist_tags.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_cloudfront/test_cloudfront_distributions.py` & `moto-4.1.7.dev9/tests/test_cloudfront/test_cloudfront_distributions.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_cloudfront/test_cloudfront_invalidation.py` & `moto-4.1.7.dev9/tests/test_cloudfront/test_cloudfront_invalidation.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_cloudtrail/test_cloudtrail.py` & `moto-4.1.7.dev9/tests/test_cloudtrail/test_cloudtrail.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_cloudtrail/test_cloudtrail_eventselectors.py` & `moto-4.1.7.dev9/tests/test_cloudtrail/test_cloudtrail_eventselectors.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_cloudtrail/test_cloudtrail_tags.py` & `moto-4.1.7.dev9/tests/test_cloudtrail/test_cloudtrail_tags.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_cloudtrail/test_server.py` & `moto-4.1.7.dev9/tests/test_cloudtrail/test_server.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_cloudwatch/test_cloudwatch_alarms.py` & `moto-4.1.7.dev9/tests/test_cloudwatch/test_cloudwatch_alarms.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_cloudwatch/test_cloudwatch_boto3.py` & `moto-4.1.7.dev9/tests/test_cloudwatch/test_cloudwatch_boto3.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_cloudwatch/test_cloudwatch_dashboards.py` & `moto-4.1.7.dev9/tests/test_cloudwatch/test_cloudwatch_dashboards.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_cloudwatch/test_cloudwatch_tags.py` & `moto-4.1.7.dev9/tests/test_cloudwatch/test_cloudwatch_tags.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_codebuild/test_codebuild.py` & `moto-4.1.7.dev9/tests/test_codebuild/test_codebuild.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_codecommit/test_codecommit.py` & `moto-4.1.7.dev9/tests/test_codecommit/test_codecommit.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_codepipeline/test_codepipeline.py` & `moto-4.1.7.dev9/tests/test_codepipeline/test_codepipeline.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_cognitoidentity/test_cognitoidentity.py` & `moto-4.1.7.dev9/tests/test_cognitoidentity/test_cognitoidentity.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_cognitoidentity/test_server.py` & `moto-4.1.7.dev9/tests/test_cognitoidentity/test_server.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_cognitoidp/test_cognitoidp.py` & `moto-4.1.7.dev9/tests/test_cognitoidp/test_cognitoidp.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_cognitoidp/test_cognitoidp_exceptions.py` & `moto-4.1.7.dev9/tests/test_cognitoidp/test_cognitoidp_exceptions.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_cognitoidp/test_cognitoidp_replay.py` & `moto-4.1.7.dev9/tests/test_cognitoidp/test_cognitoidp_replay.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_cognitoidp/test_server.py` & `moto-4.1.7.dev9/tests/test_cognitoidp/test_server.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_comprehend/test_comprehend.py` & `moto-4.1.7.dev9/tests/test_comprehend/test_comprehend.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_config/test_config.py` & `moto-4.1.7.dev9/tests/test_config/test_config.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_config/test_config_rules.py` & `moto-4.1.7.dev9/tests/test_config/test_config_rules.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_config/test_config_rules_integration.py` & `moto-4.1.7.dev9/tests/test_config/test_config_rules_integration.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_config/test_config_tags.py` & `moto-4.1.7.dev9/tests/test_config/test_config_tags.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_core/test_account_id_resolution.py` & `moto-4.1.7.dev9/tests/test_core/test_account_id_resolution.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_core/test_auth.py` & `moto-4.1.7.dev9/tests/test_core/test_auth.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_core/test_backenddict.py` & `moto-4.1.7.dev9/tests/test_core/test_backenddict.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_core/test_decorator_calls.py` & `moto-4.1.7.dev9/tests/test_core/test_decorator_calls.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_core/test_docker.py` & `moto-4.1.7.dev9/tests/test_core/test_docker.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_core/test_environ_patching.py` & `moto-4.1.7.dev9/tests/test_core/test_environ_patching.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_core/test_importorder.py` & `moto-4.1.7.dev9/tests/test_core/test_importorder.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_core/test_instance_metadata.py` & `moto-4.1.7.dev9/tests/test_core/test_instance_metadata.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_core/test_mock_all.py` & `moto-4.1.7.dev9/tests/test_core/test_mock_all.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_core/test_mock_regions.py` & `moto-4.1.7.dev9/tests/test_core/test_mock_regions.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_core/test_moto_api.py` & `moto-4.1.7.dev9/tests/test_core/test_moto_api.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_core/test_nested.py` & `moto-4.1.7.dev9/tests/test_core/test_nested.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_core/test_request_mocking.py` & `moto-4.1.7.dev9/tests/test_core/test_request_mocking.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_core/test_responses.py` & `moto-4.1.7.dev9/tests/test_core/test_responses.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_core/test_responses_module.py` & `moto-4.1.7.dev9/tests/test_core/test_responses_module.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_core/test_server.py` & `moto-4.1.7.dev9/tests/test_core/test_server.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_core/test_settings.py` & `moto-4.1.7.dev9/tests/test_core/test_settings.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_core/test_url_base_regex.py` & `moto-4.1.7.dev9/tests/test_core/test_url_base_regex.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_core/test_url_mapping.py` & `moto-4.1.7.dev9/tests/test_core/test_url_mapping.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_core/test_utils.py` & `moto-4.1.7.dev9/tests/test_core/test_utils.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_databrew/test_databrew_datasets.py` & `moto-4.1.7.dev9/tests/test_databrew/test_databrew_datasets.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_databrew/test_databrew_jobs.py` & `moto-4.1.7.dev9/tests/test_databrew/test_databrew_jobs.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_databrew/test_databrew_recipes.py` & `moto-4.1.7.dev9/tests/test_databrew/test_databrew_recipes.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_databrew/test_databrew_rulesets.py` & `moto-4.1.7.dev9/tests/test_databrew/test_databrew_rulesets.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_datapipeline/test_datapipeline.py` & `moto-4.1.7.dev9/tests/test_datapipeline/test_datapipeline.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_datapipeline/test_datapipeline_cloudformation.py` & `moto-4.1.7.dev9/tests/test_datapipeline/test_datapipeline_cloudformation.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_datapipeline/test_server.py` & `moto-4.1.7.dev9/tests/test_datapipeline/test_server.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_datasync/test_datasync.py` & `moto-4.1.7.dev9/tests/test_datasync/test_datasync.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_dax/test_dax.py` & `moto-4.1.7.dev9/tests/test_dax/test_dax.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_dms/test_dms.py` & `moto-4.1.7.dev9/tests/test_dms/test_dms.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_ds/test_ds.py` & `moto-4.1.7.dev9/tests/test_ds/test_ds.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_ds/test_ds_ad_connect.py` & `moto-4.1.7.dev9/tests/test_ds/test_ds_ad_connect.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_ds/test_ds_microsoft_ad.py` & `moto-4.1.7.dev9/tests/test_ds/test_ds_microsoft_ad.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_ds/test_ds_simple_ad_directory.py` & `moto-4.1.7.dev9/tests/test_ds/test_ds_simple_ad_directory.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_ds/test_ds_tags.py` & `moto-4.1.7.dev9/tests/test_ds/test_ds_tags.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_dynamodb/conftest.py` & `moto-4.1.7.dev9/tests/test_dynamodb/conftest.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_dynamodb/exceptions/test_dynamodb_exceptions.py` & `moto-4.1.7.dev9/tests/test_dynamodb/exceptions/test_dynamodb_exceptions.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_dynamodb/exceptions/test_key_length_exceptions.py` & `moto-4.1.7.dev9/tests/test_dynamodb/exceptions/test_key_length_exceptions.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_dynamodb/models/test_key_condition_expression_parser.py` & `moto-4.1.7.dev9/tests/test_dynamodb/models/test_key_condition_expression_parser.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_dynamodb/test_dynamodb.py` & `moto-4.1.7.dev9/tests/test_dynamodb/test_dynamodb.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_dynamodb/test_dynamodb_batch_get_item.py` & `moto-4.1.7.dev9/tests/test_dynamodb/test_dynamodb_batch_get_item.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_dynamodb/test_dynamodb_cloudformation.py` & `moto-4.1.7.dev9/tests/test_dynamodb/test_dynamodb_cloudformation.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_dynamodb/test_dynamodb_condition_expressions.py` & `moto-4.1.7.dev9/tests/test_dynamodb/test_dynamodb_condition_expressions.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_dynamodb/test_dynamodb_consumedcapacity.py` & `moto-4.1.7.dev9/tests/test_dynamodb/test_dynamodb_consumedcapacity.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_dynamodb/test_dynamodb_create_table.py` & `moto-4.1.7.dev9/tests/test_dynamodb/test_dynamodb_create_table.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_dynamodb/test_dynamodb_executor.py` & `moto-4.1.7.dev9/tests/test_dynamodb/test_dynamodb_executor.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_dynamodb/test_dynamodb_expression_tokenizer.py` & `moto-4.1.7.dev9/tests/test_dynamodb/test_dynamodb_expression_tokenizer.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_dynamodb/test_dynamodb_expressions.py` & `moto-4.1.7.dev9/tests/test_dynamodb/test_dynamodb_expressions.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_dynamodb/test_dynamodb_table_with_range_key.py` & `moto-4.1.7.dev9/tests/test_dynamodb/test_dynamodb_table_with_range_key.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_dynamodb/test_dynamodb_table_without_range_key.py` & `moto-4.1.7.dev9/tests/test_dynamodb/test_dynamodb_table_without_range_key.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_dynamodb/test_dynamodb_update_expressions.py` & `moto-4.1.7.dev9/tests/test_dynamodb/test_dynamodb_update_expressions.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_dynamodb/test_dynamodb_update_table.py` & `moto-4.1.7.dev9/tests/test_dynamodb/test_dynamodb_update_table.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_dynamodb/test_dynamodb_validation.py` & `moto-4.1.7.dev9/tests/test_dynamodb/test_dynamodb_validation.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_dynamodb/test_server.py` & `moto-4.1.7.dev9/tests/test_dynamodb/test_server.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_dynamodb_v20111205/test_server.py` & `moto-4.1.7.dev9/tests/test_dynamodb_v20111205/test_server.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_dynamodb_v20111205/test_servermode.py` & `moto-4.1.7.dev9/tests/test_dynamodb_v20111205/test_servermode.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_dynamodbstreams/test_dynamodbstreams.py` & `moto-4.1.7.dev9/tests/test_dynamodbstreams/test_dynamodbstreams.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_ebs/test_ebs.py` & `moto-4.1.7.dev9/tests/test_ebs/test_ebs.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_ec2/test_account_attributes.py` & `moto-4.1.7.dev9/tests/test_ec2/test_account_attributes.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_ec2/test_amis.py` & `moto-4.1.7.dev9/tests/test_ec2/test_amis.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_ec2/test_availability_zones_and_regions.py` & `moto-4.1.7.dev9/tests/test_ec2/test_availability_zones_and_regions.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_ec2/test_carrier_gateways.py` & `moto-4.1.7.dev9/tests/test_ec2/test_carrier_gateways.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_ec2/test_customer_gateways.py` & `moto-4.1.7.dev9/tests/test_ec2/test_customer_gateways.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_ec2/test_dhcp_options.py` & `moto-4.1.7.dev9/tests/test_ec2/test_dhcp_options.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_ec2/test_ec2_cloudformation.py` & `moto-4.1.7.dev9/tests/test_ec2/test_ec2_cloudformation.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_ec2/test_ec2_integration.py` & `moto-4.1.7.dev9/tests/test_ec2/test_ec2_integration.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_ec2/test_egress_only_igw.py` & `moto-4.1.7.dev9/tests/test_ec2/test_egress_only_igw.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_ec2/test_elastic_block_store.py` & `moto-4.1.7.dev9/tests/test_ec2/test_elastic_block_store.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_ec2/test_elastic_ip_addresses.py` & `moto-4.1.7.dev9/tests/test_ec2/test_elastic_ip_addresses.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_ec2/test_elastic_network_interfaces.py` & `moto-4.1.7.dev9/tests/test_ec2/test_elastic_network_interfaces.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_ec2/test_fleets.py` & `moto-4.1.7.dev9/tests/test_ec2/test_fleets.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_ec2/test_flow_logs.py` & `moto-4.1.7.dev9/tests/test_ec2/test_flow_logs.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_ec2/test_flow_logs_cloudformation.py` & `moto-4.1.7.dev9/tests/test_ec2/test_flow_logs_cloudformation.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_ec2/test_general.py` & `moto-4.1.7.dev9/tests/test_ec2/test_general.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_ec2/test_hosts.py` & `moto-4.1.7.dev9/tests/test_ec2/test_hosts.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_ec2/test_iam_integration.py` & `moto-4.1.7.dev9/tests/test_ec2/test_iam_integration.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_ec2/test_instance_type_offerings.py` & `moto-4.1.7.dev9/tests/test_ec2/test_instance_type_offerings.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_ec2/test_instance_types.py` & `moto-4.1.7.dev9/tests/test_ec2/test_instance_types.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_ec2/test_instances.py` & `moto-4.1.7.dev9/tests/test_ec2/test_instances.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_ec2/test_internet_gateways.py` & `moto-4.1.7.dev9/tests/test_ec2/test_internet_gateways.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_ec2/test_key_pairs.py` & `moto-4.1.7.dev9/tests/test_ec2/test_key_pairs.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_ec2/test_launch_templates.py` & `moto-4.1.7.dev9/tests/test_ec2/test_launch_templates.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_ec2/test_nat_gateway.py` & `moto-4.1.7.dev9/tests/test_ec2/test_nat_gateway.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_ec2/test_network_acls.py` & `moto-4.1.7.dev9/tests/test_ec2/test_network_acls.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_ec2/test_prefix_lists.py` & `moto-4.1.7.dev9/tests/test_ec2/test_prefix_lists.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_ec2/test_regions.py` & `moto-4.1.7.dev9/tests/test_ec2/test_regions.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_ec2/test_route_tables.py` & `moto-4.1.7.dev9/tests/test_ec2/test_route_tables.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_ec2/test_security_groups.py` & `moto-4.1.7.dev9/tests/test_ec2/test_security_groups.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_ec2/test_security_groups_cloudformation.py` & `moto-4.1.7.dev9/tests/test_ec2/test_security_groups_cloudformation.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_ec2/test_server.py` & `moto-4.1.7.dev9/tests/test_ec2/test_server.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_ec2/test_settings.py` & `moto-4.1.7.dev9/tests/test_ec2/test_settings.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_ec2/test_spot_fleet.py` & `moto-4.1.7.dev9/tests/test_ec2/test_spot_fleet.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_ec2/test_spot_instances.py` & `moto-4.1.7.dev9/tests/test_ec2/test_spot_instances.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_ec2/test_subnets.py` & `moto-4.1.7.dev9/tests/test_ec2/test_subnets.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_ec2/test_tags.py` & `moto-4.1.7.dev9/tests/test_ec2/test_tags.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_ec2/test_transit_gateway.py` & `moto-4.1.7.dev9/tests/test_ec2/test_transit_gateway.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_ec2/test_transit_gateway_cloudformation.py` & `moto-4.1.7.dev9/tests/test_ec2/test_transit_gateway_cloudformation.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_ec2/test_transit_gateway_peering_attachments.py` & `moto-4.1.7.dev9/tests/test_ec2/test_transit_gateway_peering_attachments.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_ec2/test_utils.py` & `moto-4.1.7.dev9/tests/test_ec2/test_utils.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_ec2/test_virtual_private_gateways.py` & `moto-4.1.7.dev9/tests/test_ec2/test_virtual_private_gateways.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_ec2/test_vpc_endpoint_services_integration.py` & `moto-4.1.7.dev9/tests/test_ec2/test_vpc_endpoint_services_integration.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_ec2/test_vpc_peering.py` & `moto-4.1.7.dev9/tests/test_ec2/test_vpc_peering.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_ec2/test_vpc_service_configuration.py` & `moto-4.1.7.dev9/tests/test_ec2/test_vpc_service_configuration.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_ec2/test_vpcs.py` & `moto-4.1.7.dev9/tests/test_ec2/test_vpcs.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_ec2/test_vpn_connections.py` & `moto-4.1.7.dev9/tests/test_ec2/test_vpn_connections.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_ec2/test_windows.py` & `moto-4.1.7.dev9/tests/test_ec2/test_windows.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_ec2instanceconnect/test_ec2instanceconnect_boto3.py` & `moto-4.1.7.dev9/tests/test_ec2instanceconnect/test_ec2instanceconnect_boto3.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_ecr/test_ecr_boto3.py` & `moto-4.1.7.dev9/tests/test_ecr/test_ecr_boto3.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_ecr/test_ecr_cloudformation.py` & `moto-4.1.7.dev9/tests/test_ecr/test_ecr_cloudformation.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_ecr/test_ecr_helpers.py` & `moto-4.1.7.dev9/tests/test_ecr/test_ecr_helpers.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_ecr/test_ecr_policy_validation.py` & `moto-4.1.7.dev9/tests/test_ecr/test_ecr_policy_validation.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_ecs/test_ecs_account_settings.py` & `moto-4.1.7.dev9/tests/test_ecs/test_ecs_account_settings.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_ecs/test_ecs_boto3.py` & `moto-4.1.7.dev9/tests/test_ecs/test_ecs_boto3.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_ecs/test_ecs_capacity_provider.py` & `moto-4.1.7.dev9/tests/test_ecs/test_ecs_capacity_provider.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_ecs/test_ecs_cloudformation.py` & `moto-4.1.7.dev9/tests/test_ecs/test_ecs_cloudformation.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_ecs/test_ecs_efs.py` & `moto-4.1.7.dev9/tests/test_ecs/test_ecs_efs.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_ecs/test_ecs_task_def_tags.py` & `moto-4.1.7.dev9/tests/test_ecs/test_ecs_task_def_tags.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_ecs/test_ecs_tasksets.py` & `moto-4.1.7.dev9/tests/test_ecs/test_ecs_tasksets.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_efs/test_access_point_tagging.py` & `moto-4.1.7.dev9/tests/test_efs/test_access_point_tagging.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_efs/test_access_points.py` & `moto-4.1.7.dev9/tests/test_efs/test_access_points.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_efs/test_file_system.py` & `moto-4.1.7.dev9/tests/test_efs/test_file_system.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_efs/test_filesystem_tagging.py` & `moto-4.1.7.dev9/tests/test_efs/test_filesystem_tagging.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_efs/test_lifecycle_config.py` & `moto-4.1.7.dev9/tests/test_efs/test_lifecycle_config.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_efs/test_mount_target.py` & `moto-4.1.7.dev9/tests/test_efs/test_mount_target.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_efs/test_mount_target_security_groups.py` & `moto-4.1.7.dev9/tests/test_efs/test_mount_target_security_groups.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_efs/test_server.py` & `moto-4.1.7.dev9/tests/test_efs/test_server.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_eks/test_eks.py` & `moto-4.1.7.dev9/tests/test_eks/test_eks.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_eks/test_eks_constants.py` & `moto-4.1.7.dev9/tests/test_eks/test_eks_constants.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_eks/test_eks_ec2.py` & `moto-4.1.7.dev9/tests/test_eks/test_eks_ec2.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_eks/test_eks_utils.py` & `moto-4.1.7.dev9/tests/test_eks/test_eks_utils.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_eks/test_server.py` & `moto-4.1.7.dev9/tests/test_eks/test_server.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_elasticache/test_elasticache.py` & `moto-4.1.7.dev9/tests/test_elasticache/test_elasticache.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_elasticbeanstalk/test_eb.py` & `moto-4.1.7.dev9/tests/test_elasticbeanstalk/test_eb.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_elastictranscoder/test_elastictranscoder.py` & `moto-4.1.7.dev9/tests/test_elastictranscoder/test_elastictranscoder.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_elb/test_elb.py` & `moto-4.1.7.dev9/tests/test_elb/test_elb.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_elb/test_elb_availabilityzones.py` & `moto-4.1.7.dev9/tests/test_elb/test_elb_availabilityzones.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_elb/test_elb_cloudformation.py` & `moto-4.1.7.dev9/tests/test_elb/test_elb_cloudformation.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_elb/test_elb_policies.py` & `moto-4.1.7.dev9/tests/test_elb/test_elb_policies.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_elb/test_elb_subnets.py` & `moto-4.1.7.dev9/tests/test_elb/test_elb_subnets.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_elbv2/test_elbv2.py` & `moto-4.1.7.dev9/tests/test_elbv2/test_elbv2.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_elbv2/test_elbv2_cloudformation.py` & `moto-4.1.7.dev9/tests/test_elbv2/test_elbv2_cloudformation.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_elbv2/test_elbv2_integration.py` & `moto-4.1.7.dev9/tests/test_elbv2/test_elbv2_integration.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_elbv2/test_elbv2_listener_rule_tags.py` & `moto-4.1.7.dev9/tests/test_elbv2/test_elbv2_listener_rule_tags.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_elbv2/test_elbv2_listener_rules.py` & `moto-4.1.7.dev9/tests/test_elbv2/test_elbv2_listener_rules.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_elbv2/test_elbv2_listener_tags.py` & `moto-4.1.7.dev9/tests/test_elbv2/test_elbv2_listener_tags.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_elbv2/test_elbv2_set_subnets.py` & `moto-4.1.7.dev9/tests/test_elbv2/test_elbv2_set_subnets.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_elbv2/test_elbv2_target_groups.py` & `moto-4.1.7.dev9/tests/test_elbv2/test_elbv2_target_groups.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_emr/test_emr_boto3.py` & `moto-4.1.7.dev9/tests/test_emr/test_emr_boto3.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_emr/test_emr_integration.py` & `moto-4.1.7.dev9/tests/test_emr/test_emr_integration.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_emr/test_utils.py` & `moto-4.1.7.dev9/tests/test_emr/test_utils.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_emrcontainers/test_emrcontainers.py` & `moto-4.1.7.dev9/tests/test_emrcontainers/test_emrcontainers.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_emrserverless/test_emrserverless.py` & `moto-4.1.7.dev9/tests/test_emrserverless/test_emrserverless.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_es/test_es.py` & `moto-4.1.7.dev9/tests/test_es/test_es.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_events/test_event_pattern.py` & `moto-4.1.7.dev9/tests/test_events/test_event_pattern.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_events/test_events.py` & `moto-4.1.7.dev9/tests/test_events/test_events.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_events/test_events_cloudformation.py` & `moto-4.1.7.dev9/tests/test_events/test_events_cloudformation.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_events/test_events_integration.py` & `moto-4.1.7.dev9/tests/test_events/test_events_integration.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_events/test_events_lambdatriggers_integration.py` & `moto-4.1.7.dev9/tests/test_events/test_events_lambdatriggers_integration.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_firehose/test_firehose.py` & `moto-4.1.7.dev9/tests/test_firehose/test_firehose.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_firehose/test_firehose_destination_types.py` & `moto-4.1.7.dev9/tests/test_firehose/test_firehose_destination_types.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_firehose/test_firehose_encryption.py` & `moto-4.1.7.dev9/tests/test_firehose/test_firehose_encryption.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_firehose/test_firehose_put.py` & `moto-4.1.7.dev9/tests/test_firehose/test_firehose_put.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_firehose/test_firehose_tags.py` & `moto-4.1.7.dev9/tests/test_firehose/test_firehose_tags.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_firehose/test_http_destinations.py` & `moto-4.1.7.dev9/tests/test_firehose/test_http_destinations.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_forecast/test_forecast.py` & `moto-4.1.7.dev9/tests/test_forecast/test_forecast.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_glacier/test_glacier_archives.py` & `moto-4.1.7.dev9/tests/test_glacier/test_glacier_archives.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_glacier/test_glacier_jobs.py` & `moto-4.1.7.dev9/tests/test_glacier/test_glacier_jobs.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_glacier/test_glacier_vaults.py` & `moto-4.1.7.dev9/tests/test_glacier/test_glacier_vaults.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_glue/fixtures/datacatalog.py` & `moto-4.1.7.dev9/tests/test_glue/fixtures/datacatalog.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_glue/fixtures/schema_registry.py` & `moto-4.1.7.dev9/tests/test_glue/fixtures/schema_registry.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_glue/helpers.py` & `moto-4.1.7.dev9/tests/test_glue/helpers.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_glue/test_datacatalog.py` & `moto-4.1.7.dev9/tests/test_glue/test_datacatalog.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_glue/test_glue.py` & `moto-4.1.7.dev9/tests/test_glue/test_glue.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_glue/test_glue_job_runs.py` & `moto-4.1.7.dev9/tests/test_glue/test_glue_job_runs.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_glue/test_partition_filter.py` & `moto-4.1.7.dev9/tests/test_glue/test_partition_filter.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_glue/test_schema_registry.py` & `moto-4.1.7.dev9/tests/test_glue/test_schema_registry.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_greengrass/test_greengrass_core.py` & `moto-4.1.7.dev9/tests/test_greengrass/test_greengrass_core.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_greengrass/test_greengrass_deployment.py` & `moto-4.1.7.dev9/tests/test_greengrass/test_greengrass_deployment.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_greengrass/test_greengrass_device.py` & `moto-4.1.7.dev9/tests/test_greengrass/test_greengrass_device.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_greengrass/test_greengrass_functions.py` & `moto-4.1.7.dev9/tests/test_greengrass/test_greengrass_functions.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_greengrass/test_greengrass_groups.py` & `moto-4.1.7.dev9/tests/test_greengrass/test_greengrass_groups.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_greengrass/test_greengrass_resource.py` & `moto-4.1.7.dev9/tests/test_greengrass/test_greengrass_resource.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_greengrass/test_greengrass_subscriptions.py` & `moto-4.1.7.dev9/tests/test_greengrass/test_greengrass_subscriptions.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_guardduty/test_guardduty.py` & `moto-4.1.7.dev9/tests/test_guardduty/test_guardduty.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_guardduty/test_guardduty_filters.py` & `moto-4.1.7.dev9/tests/test_guardduty/test_guardduty_filters.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_guardduty/test_guardduty_organization.py` & `moto-4.1.7.dev9/tests/test_guardduty/test_guardduty_organization.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_iam/test_iam.py` & `moto-4.1.7.dev9/tests/test_iam/test_iam.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_iam/test_iam_access_integration.py` & `moto-4.1.7.dev9/tests/test_iam/test_iam_access_integration.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_iam/test_iam_account_aliases.py` & `moto-4.1.7.dev9/tests/test_iam/test_iam_account_aliases.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_iam/test_iam_cloudformation.py` & `moto-4.1.7.dev9/tests/test_iam/test_iam_cloudformation.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_iam/test_iam_groups.py` & `moto-4.1.7.dev9/tests/test_iam/test_iam_groups.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_iam/test_iam_oidc.py` & `moto-4.1.7.dev9/tests/test_iam/test_iam_oidc.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_iam/test_iam_password_last_used.py` & `moto-4.1.7.dev9/tests/test_iam/test_iam_password_last_used.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_iam/test_iam_policies.py` & `moto-4.1.7.dev9/tests/test_iam/test_iam_policies.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_iam/test_iam_server_certificates.py` & `moto-4.1.7.dev9/tests/test_iam/test_iam_server_certificates.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_iam/test_server.py` & `moto-4.1.7.dev9/tests/test_iam/test_server.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_identitystore/test_identitystore.py` & `moto-4.1.7.dev9/tests/test_identitystore/test_identitystore.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_iot/test_iot.py` & `moto-4.1.7.dev9/tests/test_iot/test_iot.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_iot/test_iot_ca_certificates.py` & `moto-4.1.7.dev9/tests/test_iot/test_iot_ca_certificates.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_iot/test_iot_certificates.py` & `moto-4.1.7.dev9/tests/test_iot/test_iot_certificates.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_iot/test_iot_deprecate_thing_type.py` & `moto-4.1.7.dev9/tests/test_iot/test_iot_deprecate_thing_type.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_iot/test_iot_domain_configuration.py` & `moto-4.1.7.dev9/tests/test_iot/test_iot_domain_configuration.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_iot/test_iot_job_executions.py` & `moto-4.1.7.dev9/tests/test_iot/test_iot_job_executions.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_iot/test_iot_jobs.py` & `moto-4.1.7.dev9/tests/test_iot/test_iot_jobs.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_iot/test_iot_policies.py` & `moto-4.1.7.dev9/tests/test_iot/test_iot_policies.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_iot/test_iot_search.py` & `moto-4.1.7.dev9/tests/test_iot/test_iot_search.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_iot/test_iot_thing_groups.py` & `moto-4.1.7.dev9/tests/test_iot/test_iot_thing_groups.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_iot/test_iot_thing_types.py` & `moto-4.1.7.dev9/tests/test_iot/test_iot_thing_types.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_iot/test_iot_things.py` & `moto-4.1.7.dev9/tests/test_iot/test_iot_things.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_iot/test_iot_topic_rules.py` & `moto-4.1.7.dev9/tests/test_iot/test_iot_topic_rules.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_iot/test_server.py` & `moto-4.1.7.dev9/tests/test_iot/test_server.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_iotdata/test_iotdata.py` & `moto-4.1.7.dev9/tests/test_iotdata/test_iotdata.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_iotdata/test_server.py` & `moto-4.1.7.dev9/tests/test_iotdata/test_server.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_kinesis/test_kinesis.py` & `moto-4.1.7.dev9/tests/test_kinesis/test_kinesis.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_kinesis/test_kinesis_boto3.py` & `moto-4.1.7.dev9/tests/test_kinesis/test_kinesis_boto3.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_kinesis/test_kinesis_cloudformation.py` & `moto-4.1.7.dev9/tests/test_kinesis/test_kinesis_cloudformation.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_kinesis/test_kinesis_encryption.py` & `moto-4.1.7.dev9/tests/test_kinesis/test_kinesis_encryption.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_kinesis/test_kinesis_monitoring.py` & `moto-4.1.7.dev9/tests/test_kinesis/test_kinesis_monitoring.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_kinesis/test_kinesis_stream_consumers.py` & `moto-4.1.7.dev9/tests/test_kinesis/test_kinesis_stream_consumers.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_kinesis/test_kinesis_stream_limits.py` & `moto-4.1.7.dev9/tests/test_kinesis/test_kinesis_stream_limits.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_kinesisvideo/test_kinesisvideo.py` & `moto-4.1.7.dev9/tests/test_kinesisvideo/test_kinesisvideo.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_kinesisvideoarchivedmedia/test_kinesisvideoarchivedmedia.py` & `moto-4.1.7.dev9/tests/test_kinesisvideoarchivedmedia/test_kinesisvideoarchivedmedia.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_kms/test_kms_boto3.py` & `moto-4.1.7.dev9/tests/test_kms/test_kms_boto3.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_kms/test_kms_encrypt.py` & `moto-4.1.7.dev9/tests/test_kms/test_kms_encrypt.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_kms/test_kms_grants.py` & `moto-4.1.7.dev9/tests/test_kms/test_kms_grants.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_kms/test_kms_policy_enforcement.py` & `moto-4.1.7.dev9/tests/test_kms/test_kms_policy_enforcement.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_kms/test_model.py` & `moto-4.1.7.dev9/tests/test_kms/test_model.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_kms/test_utils.py` & `moto-4.1.7.dev9/tests/test_kms/test_utils.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_logs/test_integration.py` & `moto-4.1.7.dev9/tests/test_logs/test_integration.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_logs/test_logs.py` & `moto-4.1.7.dev9/tests/test_logs/test_logs.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_logs/test_logs_filter.py` & `moto-4.1.7.dev9/tests/test_logs/test_logs_filter.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_logs/test_models.py` & `moto-4.1.7.dev9/tests/test_logs/test_models.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_managedblockchain/helpers.py` & `moto-4.1.7.dev9/tests/test_managedblockchain/helpers.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_managedblockchain/test_managedblockchain_invitations.py` & `moto-4.1.7.dev9/tests/test_managedblockchain/test_managedblockchain_invitations.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_managedblockchain/test_managedblockchain_members.py` & `moto-4.1.7.dev9/tests/test_managedblockchain/test_managedblockchain_members.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_managedblockchain/test_managedblockchain_networks.py` & `moto-4.1.7.dev9/tests/test_managedblockchain/test_managedblockchain_networks.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_managedblockchain/test_managedblockchain_nodes.py` & `moto-4.1.7.dev9/tests/test_managedblockchain/test_managedblockchain_nodes.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_managedblockchain/test_managedblockchain_proposals.py` & `moto-4.1.7.dev9/tests/test_managedblockchain/test_managedblockchain_proposals.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_managedblockchain/test_managedblockchain_proposalvotes.py` & `moto-4.1.7.dev9/tests/test_managedblockchain/test_managedblockchain_proposalvotes.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_mediaconnect/test_mediaconnect.py` & `moto-4.1.7.dev9/tests/test_mediaconnect/test_mediaconnect.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_medialive/test_medialive.py` & `moto-4.1.7.dev9/tests/test_medialive/test_medialive.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_medialive/test_server.py` & `moto-4.1.7.dev9/tests/test_medialive/test_server.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_mediapackage/test_mediapackage.py` & `moto-4.1.7.dev9/tests/test_mediapackage/test_mediapackage.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_mediapackage/test_server.py` & `moto-4.1.7.dev9/tests/test_mediapackage/test_server.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_mediastore/test_mediastore.py` & `moto-4.1.7.dev9/tests/test_mediastore/test_mediastore.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_mediastoredata/test_mediastoredata.py` & `moto-4.1.7.dev9/tests/test_mediastoredata/test_mediastoredata.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_meteringmarketplace/test_meteringmarketplace.py` & `moto-4.1.7.dev9/tests/test_meteringmarketplace/test_meteringmarketplace.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_moto_api/mock_random/test_mock_random.py` & `moto-4.1.7.dev9/tests/test_moto_api/mock_random/test_mock_random.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_moto_api/recorder/test_recorder.py` & `moto-4.1.7.dev9/tests/test_moto_api/recorder/test_recorder.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_moto_api/state_manager/servermode/test_inmemory_server.py` & `moto-4.1.7.dev9/tests/test_moto_api/state_manager/servermode/test_inmemory_server.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_moto_api/state_manager/servermode/test_state_manager.py` & `moto-4.1.7.dev9/tests/test_moto_api/state_manager/servermode/test_state_manager.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_moto_api/state_manager/test_batch_integration.py` & `moto-4.1.7.dev9/tests/test_moto_api/state_manager/test_batch_integration.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_moto_api/state_manager/test_managed_state_model.py` & `moto-4.1.7.dev9/tests/test_moto_api/state_manager/test_managed_state_model.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_moto_api/state_manager/test_state_manager.py` & `moto-4.1.7.dev9/tests/test_moto_api/state_manager/test_state_manager.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_mq/test_mq.py` & `moto-4.1.7.dev9/tests/test_mq/test_mq.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_mq/test_mq_configuration.py` & `moto-4.1.7.dev9/tests/test_mq/test_mq_configuration.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_mq/test_mq_tags.py` & `moto-4.1.7.dev9/tests/test_mq/test_mq_tags.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_mq/test_mq_users.py` & `moto-4.1.7.dev9/tests/test_mq/test_mq_users.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_neptune/test_cluster_options.py` & `moto-4.1.7.dev9/tests/test_neptune/test_cluster_options.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_neptune/test_cluster_tags.py` & `moto-4.1.7.dev9/tests/test_neptune/test_cluster_tags.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_neptune/test_clusters.py` & `moto-4.1.7.dev9/tests/test_neptune/test_clusters.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_neptune/test_global_clusters.py` & `moto-4.1.7.dev9/tests/test_neptune/test_global_clusters.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_opensearch/test_domain_tags.py` & `moto-4.1.7.dev9/tests/test_opensearch/test_domain_tags.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_opensearch/test_opensearch.py` & `moto-4.1.7.dev9/tests/test_opensearch/test_opensearch.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_opsworks/test_apps.py` & `moto-4.1.7.dev9/tests/test_opsworks/test_apps.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_opsworks/test_instances.py` & `moto-4.1.7.dev9/tests/test_opsworks/test_instances.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_opsworks/test_layers.py` & `moto-4.1.7.dev9/tests/test_opsworks/test_layers.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_opsworks/test_stack.py` & `moto-4.1.7.dev9/tests/test_opsworks/test_stack.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_organizations/organizations_test_utils.py` & `moto-4.1.7.dev9/tests/test_organizations/organizations_test_utils.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_organizations/test_organizations_boto3.py` & `moto-4.1.7.dev9/tests/test_organizations/test_organizations_boto3.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_personalize/test_personalize_schema.py` & `moto-4.1.7.dev9/tests/test_personalize/test_personalize_schema.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_pinpoint/test_pinpoint.py` & `moto-4.1.7.dev9/tests/test_pinpoint/test_pinpoint.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_pinpoint/test_pinpoint_application_tags.py` & `moto-4.1.7.dev9/tests/test_pinpoint/test_pinpoint_application_tags.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_pinpoint/test_pinpoint_event_stream.py` & `moto-4.1.7.dev9/tests/test_pinpoint/test_pinpoint_event_stream.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_polly/test_polly.py` & `moto-4.1.7.dev9/tests/test_polly/test_polly.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_quicksight/test_quicksight_datasets.py` & `moto-4.1.7.dev9/tests/test_quicksight/test_quicksight_datasets.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_quicksight/test_quicksight_groups.py` & `moto-4.1.7.dev9/tests/test_quicksight/test_quicksight_groups.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_quicksight/test_quicksight_users.py` & `moto-4.1.7.dev9/tests/test_quicksight/test_quicksight_users.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_ram/test_ram.py` & `moto-4.1.7.dev9/tests/test_ram/test_ram.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_rds/test_filters.py` & `moto-4.1.7.dev9/tests/test_rds/test_filters.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_rds/test_rds.py` & `moto-4.1.7.dev9/tests/test_rds/test_rds.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_rds/test_rds_cloudformation.py` & `moto-4.1.7.dev9/tests/test_rds/test_rds_cloudformation.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_rds/test_rds_clusters.py` & `moto-4.1.7.dev9/tests/test_rds/test_rds_clusters.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_rds/test_rds_event_subscriptions.py` & `moto-4.1.7.dev9/tests/test_rds/test_rds_event_subscriptions.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_rds/test_rds_export_tasks.py` & `moto-4.1.7.dev9/tests/test_rds/test_rds_export_tasks.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_rds/test_server.py` & `moto-4.1.7.dev9/tests/test_rds/test_server.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_rds/test_utils.py` & `moto-4.1.7.dev9/tests/test_rds/test_utils.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_redshift/test_redshift.py` & `moto-4.1.7.dev9/tests/test_redshift/test_redshift.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_redshift/test_redshift_cloudformation.py` & `moto-4.1.7.dev9/tests/test_redshift/test_redshift_cloudformation.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_redshift/test_server.py` & `moto-4.1.7.dev9/tests/test_redshift/test_server.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_redshiftdata/test_redshiftdata.py` & `moto-4.1.7.dev9/tests/test_redshiftdata/test_redshiftdata.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_redshiftdata/test_server.py` & `moto-4.1.7.dev9/tests/test_redshiftdata/test_server.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_rekognition/test_rekognition.py` & `moto-4.1.7.dev9/tests/test_rekognition/test_rekognition.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_resourcegroups/test_resourcegroups.py` & `moto-4.1.7.dev9/tests/test_resourcegroups/test_resourcegroups.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_resourcegroupstaggingapi/test_resourcegroupstaggingapi.py` & `moto-4.1.7.dev9/tests/test_resourcegroupstaggingapi/test_resourcegroupstaggingapi.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_resourcegroupstaggingapi/test_server.py` & `moto-4.1.7.dev9/tests/test_resourcegroupstaggingapi/test_server.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_route53/test_change_set_model.py` & `moto-4.1.7.dev9/tests/test_route53/test_change_set_model.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_route53/test_route53.py` & `moto-4.1.7.dev9/tests/test_route53/test_route53.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_route53/test_route53_cloudformation.py` & `moto-4.1.7.dev9/tests/test_route53/test_route53_cloudformation.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_route53/test_route53_delegationsets.py` & `moto-4.1.7.dev9/tests/test_route53/test_route53_delegationsets.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_route53/test_route53_healthchecks.py` & `moto-4.1.7.dev9/tests/test_route53/test_route53_healthchecks.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_route53/test_route53_query_logging_config.py` & `moto-4.1.7.dev9/tests/test_route53/test_route53_query_logging_config.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_route53/test_route53_vpcs.py` & `moto-4.1.7.dev9/tests/test_route53/test_route53_vpcs.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_route53/test_server.py` & `moto-4.1.7.dev9/tests/test_route53/test_server.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_route53resolver/test_route53resolver_endpoint.py` & `moto-4.1.7.dev9/tests/test_route53resolver/test_route53resolver_endpoint.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_route53resolver/test_route53resolver_rule.py` & `moto-4.1.7.dev9/tests/test_route53resolver/test_route53resolver_rule.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_route53resolver/test_route53resolver_rule_associations.py` & `moto-4.1.7.dev9/tests/test_route53resolver/test_route53resolver_rule_associations.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_route53resolver/test_route53resolver_tags.py` & `moto-4.1.7.dev9/tests/test_route53resolver/test_route53resolver_tags.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_s3/test_multiple_accounts_server.py` & `moto-4.1.7.dev9/tests/test_s3/test_multiple_accounts_server.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_s3/test_s3.py` & `moto-4.1.7.dev9/tests/test_s3/test_s3.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_s3/test_s3_acl.py` & `moto-4.1.7.dev9/tests/test_s3/test_s3_acl.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_s3/test_s3_auth.py` & `moto-4.1.7.dev9/tests/test_s3/test_s3_auth.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_s3/test_s3_bucket_policy.py` & `moto-4.1.7.dev9/tests/test_s3/test_s3_bucket_policy.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_s3/test_s3_classdecorator.py` & `moto-4.1.7.dev9/tests/test_s3/test_s3_classdecorator.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_s3/test_s3_cloudformation.py` & `moto-4.1.7.dev9/tests/test_s3/test_s3_cloudformation.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_s3/test_s3_config.py` & `moto-4.1.7.dev9/tests/test_s3/test_s3_config.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_s3/test_s3_copyobject.py` & `moto-4.1.7.dev9/tests/test_s3/test_s3_copyobject.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_s3/test_s3_custom_endpoint.py` & `moto-4.1.7.dev9/tests/test_s3/test_s3_custom_endpoint.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_s3/test_s3_encryption.py` & `moto-4.1.7.dev9/tests/test_s3/test_s3_encryption.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_s3/test_s3_file_handles.py` & `moto-4.1.7.dev9/tests/test_s3/test_s3_file_handles.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_s3/test_s3_lambda_integration.py` & `moto-4.1.7.dev9/tests/test_s3/test_s3_lambda_integration.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_s3/test_s3_lifecycle.py` & `moto-4.1.7.dev9/tests/test_s3/test_s3_lifecycle.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_s3/test_s3_lock.py` & `moto-4.1.7.dev9/tests/test_s3/test_s3_lock.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_s3/test_s3_logging.py` & `moto-4.1.7.dev9/tests/test_s3/test_s3_logging.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_s3/test_s3_metadata.py` & `moto-4.1.7.dev9/tests/test_s3/test_s3_metadata.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_s3/test_s3_multipart.py` & `moto-4.1.7.dev9/tests/test_s3/test_s3_multipart.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_s3/test_s3_object_attributes.py` & `moto-4.1.7.dev9/tests/test_s3/test_s3_object_attributes.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_s3/test_s3_ownership.py` & `moto-4.1.7.dev9/tests/test_s3/test_s3_ownership.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_s3/test_s3_replication.py` & `moto-4.1.7.dev9/tests/test_s3/test_s3_replication.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_s3/test_s3_select.py` & `moto-4.1.7.dev9/tests/test_s3/test_s3_select.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_s3/test_s3_storageclass.py` & `moto-4.1.7.dev9/tests/test_s3/test_s3_storageclass.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_s3/test_s3_tagging.py` & `moto-4.1.7.dev9/tests/test_s3/test_s3_tagging.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_s3/test_s3_utils.py` & `moto-4.1.7.dev9/tests/test_s3/test_s3_utils.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_s3/test_server.py` & `moto-4.1.7.dev9/tests/test_s3/test_server.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_s3bucket_path/test_server.py` & `moto-4.1.7.dev9/tests/test_s3bucket_path/test_server.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_s3control/test_s3control.py` & `moto-4.1.7.dev9/tests/test_s3control/test_s3control.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_s3control/test_s3control_access_points.py` & `moto-4.1.7.dev9/tests/test_s3control/test_s3control_access_points.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_s3control/test_s3control_accesspoint_policy.py` & `moto-4.1.7.dev9/tests/test_s3control/test_s3control_accesspoint_policy.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_s3control/test_s3control_config_integration.py` & `moto-4.1.7.dev9/tests/test_s3control/test_s3control_config_integration.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_s3control/test_s3control_s3.py` & `moto-4.1.7.dev9/tests/test_s3control/test_s3control_s3.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_sagemaker/cloudformation_test_configs.py` & `moto-4.1.7.dev9/tests/test_sagemaker/cloudformation_test_configs.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_sagemaker/test_sagemaker_cloudformation.py` & `moto-4.1.7.dev9/tests/test_sagemaker/test_sagemaker_cloudformation.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_sagemaker/test_sagemaker_endpoint.py` & `moto-4.1.7.dev9/tests/test_sagemaker/test_sagemaker_endpoint.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_sagemaker/test_sagemaker_experiment.py` & `moto-4.1.7.dev9/tests/test_sagemaker/test_sagemaker_experiment.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_sagemaker/test_sagemaker_models.py` & `moto-4.1.7.dev9/tests/test_sagemaker/test_sagemaker_models.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_sagemaker/test_sagemaker_notebooks.py` & `moto-4.1.7.dev9/tests/test_sagemaker/test_sagemaker_notebooks.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_sagemaker/test_sagemaker_pipeline.py` & `moto-4.1.7.dev9/tests/test_sagemaker/test_sagemaker_pipeline.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_sagemaker/test_sagemaker_processing.py` & `moto-4.1.7.dev9/tests/test_sagemaker/test_sagemaker_processing.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_sagemaker/test_sagemaker_search.py` & `moto-4.1.7.dev9/tests/test_sagemaker/test_sagemaker_search.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_sagemaker/test_sagemaker_training.py` & `moto-4.1.7.dev9/tests/test_sagemaker/test_sagemaker_training.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_sagemaker/test_sagemaker_trial.py` & `moto-4.1.7.dev9/tests/test_sagemaker/test_sagemaker_trial.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_sagemaker/test_sagemaker_trial_component.py` & `moto-4.1.7.dev9/tests/test_sagemaker/test_sagemaker_trial_component.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_sdb/test_sdb_attributes.py` & `moto-4.1.7.dev9/tests/test_sdb/test_sdb_attributes.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_sdb/test_sdb_domains.py` & `moto-4.1.7.dev9/tests/test_sdb/test_sdb_domains.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_secretsmanager/test_list_secrets.py` & `moto-4.1.7.dev9/tests/test_secretsmanager/test_list_secrets.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_secretsmanager/test_policy.py` & `moto-4.1.7.dev9/tests/test_secretsmanager/test_policy.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_secretsmanager/test_secretsmanager.py` & `moto-4.1.7.dev9/tests/test_secretsmanager/test_secretsmanager.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_secretsmanager/test_server.py` & `moto-4.1.7.dev9/tests/test_secretsmanager/test_server.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_servicediscovery/test_servicediscovery_httpnamespaces.py` & `moto-4.1.7.dev9/tests/test_servicediscovery/test_servicediscovery_httpnamespaces.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_servicediscovery/test_servicediscovery_operations.py` & `moto-4.1.7.dev9/tests/test_servicediscovery/test_servicediscovery_operations.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_servicediscovery/test_servicediscovery_service.py` & `moto-4.1.7.dev9/tests/test_servicediscovery/test_servicediscovery_service.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_servicediscovery/test_servicediscovery_tags.py` & `moto-4.1.7.dev9/tests/test_servicediscovery/test_servicediscovery_tags.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_servicequotas/test_servicequotas.py` & `moto-4.1.7.dev9/tests/test_servicequotas/test_servicequotas.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_ses/test_server.py` & `moto-4.1.7.dev9/tests/test_ses/test_server.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_ses/test_ses_boto3.py` & `moto-4.1.7.dev9/tests/test_ses/test_ses_boto3.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_ses/test_ses_sns_boto3.py` & `moto-4.1.7.dev9/tests/test_ses/test_ses_sns_boto3.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_ses/test_templating.py` & `moto-4.1.7.dev9/tests/test_ses/test_templating.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_signer/test_signing_platforms.py` & `moto-4.1.7.dev9/tests/test_signer/test_signing_platforms.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_signer/test_signing_profiles.py` & `moto-4.1.7.dev9/tests/test_signer/test_signing_profiles.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_sns/test_application_boto3.py` & `moto-4.1.7.dev9/tests/test_sns/test_application_boto3.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_sns/test_publish_batch.py` & `moto-4.1.7.dev9/tests/test_sns/test_publish_batch.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_sns/test_publishing_boto3.py` & `moto-4.1.7.dev9/tests/test_sns/test_publishing_boto3.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_sns/test_server.py` & `moto-4.1.7.dev9/tests/test_sns/test_server.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_sns/test_sns_cloudformation.py` & `moto-4.1.7.dev9/tests/test_sns/test_sns_cloudformation.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_sns/test_subscriptions_boto3.py` & `moto-4.1.7.dev9/tests/test_sns/test_subscriptions_boto3.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_sns/test_topics_boto3.py` & `moto-4.1.7.dev9/tests/test_sns/test_topics_boto3.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_special_cases/test_custom_amis.py` & `moto-4.1.7.dev9/tests/test_special_cases/test_custom_amis.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_sqs/test_server.py` & `moto-4.1.7.dev9/tests/test_sqs/test_server.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_sqs/test_sqs.py` & `moto-4.1.7.dev9/tests/test_sqs/test_sqs.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_sqs/test_sqs_cloudformation.py` & `moto-4.1.7.dev9/tests/test_sqs/test_sqs_cloudformation.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_sqs/test_sqs_integration.py` & `moto-4.1.7.dev9/tests/test_sqs/test_sqs_integration.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_sqs/test_sqs_multiaccount.py` & `moto-4.1.7.dev9/tests/test_sqs/test_sqs_multiaccount.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_ssm/test_ssm_boto3.py` & `moto-4.1.7.dev9/tests/test_ssm/test_ssm_boto3.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_ssm/test_ssm_cloudformation.py` & `moto-4.1.7.dev9/tests/test_ssm/test_ssm_cloudformation.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_ssm/test_ssm_default_amis.py` & `moto-4.1.7.dev9/tests/test_ssm/test_ssm_default_amis.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_ssm/test_ssm_defaults.py` & `moto-4.1.7.dev9/tests/test_ssm/test_ssm_defaults.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_ssm/test_ssm_doc_permissions.py` & `moto-4.1.7.dev9/tests/test_ssm/test_ssm_doc_permissions.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_ssm/test_ssm_docs.py` & `moto-4.1.7.dev9/tests/test_ssm/test_ssm_docs.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_ssm/test_ssm_ecs_images.py` & `moto-4.1.7.dev9/tests/test_ssm/test_ssm_ecs_images.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_ssm/test_ssm_maintenance_windows.py` & `moto-4.1.7.dev9/tests/test_ssm/test_ssm_maintenance_windows.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_ssm/test_ssm_parameterstore.py` & `moto-4.1.7.dev9/tests/test_ssm/test_ssm_parameterstore.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_ssm/test_ssm_secretsmanager.py` & `moto-4.1.7.dev9/tests/test_ssm/test_ssm_secretsmanager.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_ssm/test_ssm_utils.py` & `moto-4.1.7.dev9/tests/test_ssm/test_ssm_utils.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_ssm/test_templates/good.yaml` & `moto-4.1.7.dev9/tests/test_ssm/test_templates/good.yaml`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_ssoadmin/test_server.py` & `moto-4.1.7.dev9/tests/test_ssoadmin/test_server.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_ssoadmin/test_ssoadmin.py` & `moto-4.1.7.dev9/tests/test_ssoadmin/test_ssoadmin.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_stepfunctions/test_stepfunctions.py` & `moto-4.1.7.dev9/tests/test_stepfunctions/test_stepfunctions.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_stepfunctions/test_stepfunctions_cloudformation.py` & `moto-4.1.7.dev9/tests/test_stepfunctions/test_stepfunctions_cloudformation.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_sts/test_server.py` & `moto-4.1.7.dev9/tests/test_sts/test_server.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_sts/test_sts.py` & `moto-4.1.7.dev9/tests/test_sts/test_sts.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_sts/test_sts_integration.py` & `moto-4.1.7.dev9/tests/test_sts/test_sts_integration.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_support/test_server.py` & `moto-4.1.7.dev9/tests/test_support/test_server.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_support/test_support.py` & `moto-4.1.7.dev9/tests/test_support/test_support.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_swf/models/test_activity_task.py` & `moto-4.1.7.dev9/tests/test_swf/models/test_activity_task.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_swf/models/test_decision_task.py` & `moto-4.1.7.dev9/tests/test_swf/models/test_decision_task.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_swf/models/test_domain.py` & `moto-4.1.7.dev9/tests/test_swf/models/test_domain.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_swf/models/test_generic_type.py` & `moto-4.1.7.dev9/tests/test_swf/models/test_generic_type.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_swf/models/test_history_event.py` & `moto-4.1.7.dev9/tests/test_swf/models/test_history_event.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_swf/models/test_timeout.py` & `moto-4.1.7.dev9/tests/test_swf/models/test_timeout.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_swf/models/test_timer.py` & `moto-4.1.7.dev9/tests/test_swf/models/test_timer.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_swf/models/test_workflow_execution.py` & `moto-4.1.7.dev9/tests/test_swf/models/test_workflow_execution.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_swf/responses/test_activity_tasks.py` & `moto-4.1.7.dev9/tests/test_swf/responses/test_activity_tasks.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_swf/responses/test_activity_types.py` & `moto-4.1.7.dev9/tests/test_swf/responses/test_activity_types.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_swf/responses/test_decision_tasks.py` & `moto-4.1.7.dev9/tests/test_swf/responses/test_decision_tasks.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_swf/responses/test_domains.py` & `moto-4.1.7.dev9/tests/test_swf/responses/test_domains.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_swf/responses/test_timeouts.py` & `moto-4.1.7.dev9/tests/test_swf/responses/test_timeouts.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_swf/responses/test_workflow_executions.py` & `moto-4.1.7.dev9/tests/test_swf/responses/test_workflow_executions.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_swf/responses/test_workflow_types.py` & `moto-4.1.7.dev9/tests/test_swf/responses/test_workflow_types.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_swf/test_exceptions.py` & `moto-4.1.7.dev9/tests/test_swf/test_exceptions.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_swf/utils.py` & `moto-4.1.7.dev9/tests/test_swf/utils.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_textract/test_server.py` & `moto-4.1.7.dev9/tests/test_textract/test_server.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_textract/test_textract.py` & `moto-4.1.7.dev9/tests/test_textract/test_textract.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_timestreamwrite/test_server.py` & `moto-4.1.7.dev9/tests/test_timestreamwrite/test_server.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_timestreamwrite/test_timestreamwrite_database.py` & `moto-4.1.7.dev9/tests/test_timestreamwrite/test_timestreamwrite_database.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_timestreamwrite/test_timestreamwrite_table.py` & `moto-4.1.7.dev9/tests/test_timestreamwrite/test_timestreamwrite_table.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_timestreamwrite/test_timestreamwrite_tagging.py` & `moto-4.1.7.dev9/tests/test_timestreamwrite/test_timestreamwrite_tagging.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_transcribe/test_transcribe_boto3.py` & `moto-4.1.7.dev9/tests/test_transcribe/test_transcribe_boto3.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_utilities/test_docker_utilities.py` & `moto-4.1.7.dev9/tests/test_utilities/test_docker_utilities.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_utilities/test_paginator.py` & `moto-4.1.7.dev9/tests/test_utilities/test_paginator.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_utilities/test_tagging_service.py` & `moto-4.1.7.dev9/tests/test_utilities/test_tagging_service.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_utilities/test_threaded_server.py` & `moto-4.1.7.dev9/tests/test_utilities/test_threaded_server.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_wafv2/test_server.py` & `moto-4.1.7.dev9/tests/test_wafv2/test_server.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_wafv2/test_utils.py` & `moto-4.1.7.dev9/tests/test_wafv2/test_utils.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_wafv2/test_wafv2.py` & `moto-4.1.7.dev9/tests/test_wafv2/test_wafv2.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_wafv2/test_wafv2_integration.py` & `moto-4.1.7.dev9/tests/test_wafv2/test_wafv2_integration.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_wafv2/test_wafv2_tags.py` & `moto-4.1.7.dev9/tests/test_wafv2/test_wafv2_tags.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_xray/test_xray_boto3.py` & `moto-4.1.7.dev9/tests/test_xray/test_xray_boto3.py`

 * *Files identical despite different names*

### Comparing `moto-4.1.7.dev8/tests/test_xray/test_xray_client.py` & `moto-4.1.7.dev9/tests/test_xray/test_xray_client.py`

 * *Files identical despite different names*

