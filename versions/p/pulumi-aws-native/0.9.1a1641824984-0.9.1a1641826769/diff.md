# Comparing `tmp/pulumi_aws_native-0.9.1a1641824984.tar.gz` & `tmp/pulumi_aws_native-0.9.1a1641826769.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "dist/pulumi_aws_native-0.9.1a1641824984.tar", last modified: Mon Jan 10 14:35:49 2022, max compression
+gzip compressed data, was "dist/pulumi_aws_native-0.9.1a1641826769.tar", last modified: Mon Jan 10 15:05:10 2022, max compression
```

## Comparing `pulumi_aws_native-0.9.1a1641824984.tar` & `pulumi_aws_native-0.9.1a1641826769.tar`

### file list

```diff
@@ -1,1725 +1,1725 @@
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 14:35:49.000000 pulumi_aws_native-0.9.1a1641824984/
--rw-r--r--   0 runner    (1001) docker     (121)     3304 2022-01-10 14:35:49.000000 pulumi_aws_native-0.9.1a1641824984/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (121)     2414 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/README.md
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/
--rw-r--r--   0 runner    (1001) docker     (121)   101207 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     2123 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/_enums.py
--rw-r--r--   0 runner    (1001) docker     (121)   107777 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)     7560 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/_utilities.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/accessanalyzer/
--rw-r--r--   0 runner    (1001) docker     (121)      322 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/accessanalyzer/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     5629 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/accessanalyzer/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)     8728 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/accessanalyzer/analyzer.py
--rw-r--r--   0 runner    (1001) docker     (121)     4920 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/accessanalyzer/outputs.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/acmpca/
--rw-r--r--   0 runner    (1001) docker     (121)      436 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/acmpca/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    54885 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/acmpca/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    15662 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/acmpca/certificate.py
--rw-r--r--   0 runner    (1001) docker     (121)    16814 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/acmpca/certificate_authority.py
--rw-r--r--   0 runner    (1001) docker     (121)     9680 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/acmpca/certificate_authority_activation.py
--rw-r--r--   0 runner    (1001) docker     (121)    56255 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/acmpca/outputs.py
--rw-r--r--   0 runner    (1001) docker     (121)     9591 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/acmpca/permission.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/amazonmq/
--rw-r--r--   0 runner    (1001) docker     (121)      390 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/amazonmq/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    13282 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/amazonmq/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    25043 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/amazonmq/broker.py
--rw-r--r--   0 runner    (1001) docker     (121)    10833 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/amazonmq/configuration.py
--rw-r--r--   0 runner    (1001) docker     (121)     6422 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/amazonmq/configuration_association.py
--rw-r--r--   0 runner    (1001) docker     (121)    11805 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/amazonmq/outputs.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/amplify/
--rw-r--r--   0 runner    (1001) docker     (121)      383 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/amplify/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)      646 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/amplify/_enums.py
--rw-r--r--   0 runner    (1001) docker     (121)    14363 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/amplify/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    18352 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/amplify/app.py
--rw-r--r--   0 runner    (1001) docker     (121)    15696 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/amplify/branch.py
--rw-r--r--   0 runner    (1001) docker     (121)    11123 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/amplify/domain.py
--rw-r--r--   0 runner    (1001) docker     (121)    12515 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/amplify/outputs.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/amplifyuibuilder/
--rw-r--r--   0 runner    (1001) docker     (121)      344 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/amplifyuibuilder/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     6010 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/amplifyuibuilder/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    14376 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/amplifyuibuilder/component.py
--rw-r--r--   0 runner    (1001) docker     (121)     5485 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/amplifyuibuilder/outputs.py
--rw-r--r--   0 runner    (1001) docker     (121)     8101 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/amplifyuibuilder/theme.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/apigateway/
--rw-r--r--   0 runner    (1001) docker     (121)      840 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/apigateway/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     1938 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/apigateway/_enums.py
--rw-r--r--   0 runner    (1001) docker     (121)    87809 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/apigateway/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)     5118 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/apigateway/account.py
--rw-r--r--   0 runner    (1001) docker     (121)    14915 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/apigateway/api_key.py
--rw-r--r--   0 runner    (1001) docker     (121)    17466 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/apigateway/authorizer.py
--rw-r--r--   0 runner    (1001) docker     (121)     8338 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/apigateway/base_path_mapping.py
--rw-r--r--   0 runner    (1001) docker     (121)     6915 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/apigateway/client_certificate.py
--rw-r--r--   0 runner    (1001) docker     (121)    11220 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/apigateway/deployment.py
--rw-r--r--   0 runner    (1001) docker     (121)     7061 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/apigateway/documentation_part.py
--rw-r--r--   0 runner    (1001) docker     (121)     7528 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/apigateway/documentation_version.py
--rw-r--r--   0 runner    (1001) docker     (121)    13636 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/apigateway/domain_name.py
--rw-r--r--   0 runner    (1001) docker     (121)    10379 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/apigateway/gateway_response.py
--rw-r--r--   0 runner    (1001) docker     (121)    22516 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/apigateway/method.py
--rw-r--r--   0 runner    (1001) docker     (121)     9722 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/apigateway/model.py
--rw-r--r--   0 runner    (1001) docker     (121)    83010 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/apigateway/outputs.py
--rw-r--r--   0 runner    (1001) docker     (121)     9439 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/apigateway/request_validator.py
--rw-r--r--   0 runner    (1001) docker     (121)     7515 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/apigateway/resource.py
--rw-r--r--   0 runner    (1001) docker     (121)    18120 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/apigateway/rest_api.py
--rw-r--r--   0 runner    (1001) docker     (121)    23677 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/apigateway/stage.py
--rw-r--r--   0 runner    (1001) docker     (121)    11995 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/apigateway/usage_plan.py
--rw-r--r--   0 runner    (1001) docker     (121)     7313 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/apigateway/usage_plan_key.py
--rw-r--r--   0 runner    (1001) docker     (121)     7573 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/apigateway/vpc_link.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/apigatewayv2/
--rw-r--r--   0 runner    (1001) docker     (121)      648 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/apigatewayv2/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    26786 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/apigatewayv2/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    19707 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/apigatewayv2/api.py
--rw-r--r--   0 runner    (1001) docker     (121)     8515 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/apigatewayv2/api_gateway_managed_overrides.py
--rw-r--r--   0 runner    (1001) docker     (121)     7490 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/apigatewayv2/api_mapping.py
--rw-r--r--   0 runner    (1001) docker     (121)    15642 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/apigatewayv2/authorizer.py
--rw-r--r--   0 runner    (1001) docker     (121)     6566 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/apigatewayv2/deployment.py
--rw-r--r--   0 runner    (1001) docker     (121)     9102 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/apigatewayv2/domain_name.py
--rw-r--r--   0 runner    (1001) docker     (121)    21514 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/apigatewayv2/integration.py
--rw-r--r--   0 runner    (1001) docker     (121)    11339 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/apigatewayv2/integration_response.py
--rw-r--r--   0 runner    (1001) docker     (121)     7887 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/apigatewayv2/model.py
--rw-r--r--   0 runner    (1001) docker     (121)    26988 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/apigatewayv2/outputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    15434 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/apigatewayv2/route.py
--rw-r--r--   0 runner    (1001) docker     (121)     9759 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/apigatewayv2/route_response.py
--rw-r--r--   0 runner    (1001) docker     (121)    14958 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/apigatewayv2/stage.py
--rw-r--r--   0 runner    (1001) docker     (121)     7489 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/apigatewayv2/vpc_link.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/appconfig/
--rw-r--r--   0 runner    (1001) docker     (121)      494 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/appconfig/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     6578 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/appconfig/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)     6682 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/appconfig/application.py
--rw-r--r--   0 runner    (1001) docker     (121)    11652 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/appconfig/configuration_profile.py
--rw-r--r--   0 runner    (1001) docker     (121)    11181 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/appconfig/deployment.py
--rw-r--r--   0 runner    (1001) docker     (121)    11985 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/appconfig/deployment_strategy.py
--rw-r--r--   0 runner    (1001) docker     (121)     8691 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/appconfig/environment.py
--rw-r--r--   0 runner    (1001) docker     (121)    10134 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/appconfig/hosted_configuration_version.py
--rw-r--r--   0 runner    (1001) docker     (121)     5177 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/appconfig/outputs.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/appflow/
--rw-r--r--   0 runner    (1001) docker     (121)      373 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/appflow/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    12565 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/appflow/_enums.py
--rw-r--r--   0 runner    (1001) docker     (121)   144759 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/appflow/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    12922 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/appflow/connector_profile.py
--rw-r--r--   0 runner    (1001) docker     (121)    15237 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/appflow/flow.py
--rw-r--r--   0 runner    (1001) docker     (121)   145650 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/appflow/outputs.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/appintegrations/
--rw-r--r--   0 runner    (1001) docker     (121)      331 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/appintegrations/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     1947 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/appintegrations/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    11090 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/appintegrations/event_integration.py
--rw-r--r--   0 runner    (1001) docker     (121)     6428 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/appintegrations/outputs.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/applicationautoscaling/
--rw-r--r--   0 runner    (1001) docker     (121)      359 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/applicationautoscaling/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    18725 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/applicationautoscaling/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    19117 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/applicationautoscaling/outputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    12365 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/applicationautoscaling/scalable_target.py
--rw-r--r--   0 runner    (1001) docker     (121)    13194 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/applicationautoscaling/scaling_policy.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/applicationinsights/
--rw-r--r--   0 runner    (1001) docker     (121)      347 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/applicationinsights/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     1449 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/applicationinsights/_enums.py
--rw-r--r--   0 runner    (1001) docker     (121)    32907 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/applicationinsights/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    18569 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/applicationinsights/application.py
--rw-r--r--   0 runner    (1001) docker     (121)    34411 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/applicationinsights/outputs.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/appmesh/
--rw-r--r--   0 runner    (1001) docker     (121)      488 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/appmesh/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)   151114 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/appmesh/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    10471 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/appmesh/gateway_route.py
--rw-r--r--   0 runner    (1001) docker     (121)     7497 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/appmesh/mesh.py
--rw-r--r--   0 runner    (1001) docker     (121)   152616 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/appmesh/outputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    10065 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/appmesh/route.py
--rw-r--r--   0 runner    (1001) docker     (121)     9511 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/appmesh/virtual_gateway.py
--rw-r--r--   0 runner    (1001) docker     (121)     9352 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/appmesh/virtual_node.py
--rw-r--r--   0 runner    (1001) docker     (121)     9458 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/appmesh/virtual_router.py
--rw-r--r--   0 runner    (1001) docker     (121)     9501 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/appmesh/virtual_service.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/apprunner/
--rw-r--r--   0 runner    (1001) docker     (121)      343 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/apprunner/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     1125 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/apprunner/_enums.py
--rw-r--r--   0 runner    (1001) docker     (121)    24254 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/apprunner/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    24844 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/apprunner/outputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    13695 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/apprunner/service.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/appstream/
--rw-r--r--   0 runner    (1001) docker     (121)      673 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/appstream/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    20049 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/appstream/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)     9806 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/appstream/app_block.py
--rw-r--r--   0 runner    (1001) docker     (121)    15611 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/appstream/application.py
--rw-r--r--   0 runner    (1001) docker     (121)     6964 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/appstream/application_entitlement_association.py
--rw-r--r--   0 runner    (1001) docker     (121)     5725 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/appstream/application_fleet_association.py
--rw-r--r--   0 runner    (1001) docker     (121)     8265 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/appstream/directory_config.py
--rw-r--r--   0 runner    (1001) docker     (121)     8652 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/appstream/entitlement.py
--rw-r--r--   0 runner    (1001) docker     (121)    23608 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/appstream/fleet.py
--rw-r--r--   0 runner    (1001) docker     (121)    17028 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/appstream/image_builder.py
--rw-r--r--   0 runner    (1001) docker     (121)    23129 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/appstream/outputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    17442 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/appstream/stack.py
--rw-r--r--   0 runner    (1001) docker     (121)     6108 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/appstream/stack_fleet_association.py
--rw-r--r--   0 runner    (1001) docker     (121)     8191 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/appstream/stack_user_association.py
--rw-r--r--   0 runner    (1001) docker     (121)     8388 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/appstream/user.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/appsync/
--rw-r--r--   0 runner    (1001) docker     (121)      564 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/appsync/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    28331 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/appsync/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)     9648 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/appsync/api_cache.py
--rw-r--r--   0 runner    (1001) docker     (121)     7063 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/appsync/api_key.py
--rw-r--r--   0 runner    (1001) docker     (121)    15684 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/appsync/data_source.py
--rw-r--r--   0 runner    (1001) docker     (121)     6146 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/appsync/domain_name.py
--rw-r--r--   0 runner    (1001) docker     (121)     5835 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/appsync/domain_name_api_association.py
--rw-r--r--   0 runner    (1001) docker     (121)    15108 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/appsync/function_configuration.py
--rw-r--r--   0 runner    (1001) docker     (121)    14670 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/appsync/graph_ql_api.py
--rw-r--r--   0 runner    (1001) docker     (121)     6818 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/appsync/graph_ql_schema.py
--rw-r--r--   0 runner    (1001) docker     (121)    32820 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/appsync/outputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    16583 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/appsync/resolver.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/aps/
--rw-r--r--   0 runner    (1001) docker     (121)      360 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/aps/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     4154 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/aps/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)     3702 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/aps/outputs.py
--rw-r--r--   0 runner    (1001) docker     (121)     8779 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/aps/rule_groups_namespace.py
--rw-r--r--   0 runner    (1001) docker     (121)     8351 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/aps/workspace.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ask/
--rw-r--r--   0 runner    (1001) docker     (121)      319 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ask/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     4364 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ask/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)     4530 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ask/outputs.py
--rw-r--r--   0 runner    (1001) docker     (121)     7409 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ask/skill.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/athena/
--rw-r--r--   0 runner    (1001) docker     (121)      435 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/athena/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     1037 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/athena/_enums.py
--rw-r--r--   0 runner    (1001) docker     (121)    17819 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/athena/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    10822 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/athena/data_catalog.py
--rw-r--r--   0 runner    (1001) docker     (121)     9455 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/athena/named_query.py
--rw-r--r--   0 runner    (1001) docker     (121)    19028 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/athena/outputs.py
--rw-r--r--   0 runner    (1001) docker     (121)     8680 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/athena/prepared_statement.py
--rw-r--r--   0 runner    (1001) docker     (121)    13901 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/athena/work_group.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/auditmanager/
--rw-r--r--   0 runner    (1001) docker     (121)      346 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/auditmanager/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)      944 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/auditmanager/_enums.py
--rw-r--r--   0 runner    (1001) docker     (121)     8601 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/auditmanager/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    14100 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/auditmanager/assessment.py
--rw-r--r--   0 runner    (1001) docker     (121)    14624 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/auditmanager/outputs.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/autoscaling/
--rw-r--r--   0 runner    (1001) docker     (121)      485 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/autoscaling/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    66762 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/autoscaling/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    34132 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/autoscaling/auto_scaling_group.py
--rw-r--r--   0 runner    (1001) docker     (121)    32906 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/autoscaling/launch_configuration.py
--rw-r--r--   0 runner    (1001) docker     (121)    18325 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/autoscaling/lifecycle_hook.py
--rw-r--r--   0 runner    (1001) docker     (121)    64682 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/autoscaling/outputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    16460 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/autoscaling/scaling_policy.py
--rw-r--r--   0 runner    (1001) docker     (121)    11153 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/autoscaling/scheduled_action.py
--rw-r--r--   0 runner    (1001) docker     (121)     7404 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/autoscaling/warm_pool.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/autoscalingplans/
--rw-r--r--   0 runner    (1001) docker     (121)      326 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/autoscalingplans/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    22982 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/autoscalingplans/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    21762 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/autoscalingplans/outputs.py
--rw-r--r--   0 runner    (1001) docker     (121)     7449 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/autoscalingplans/scaling_plan.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/backup/
--rw-r--r--   0 runner    (1001) docker     (121)      437 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/backup/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    37338 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/backup/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)     6329 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/backup/backup_plan.py
--rw-r--r--   0 runner    (1001) docker     (121)     6102 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/backup/backup_selection.py
--rw-r--r--   0 runner    (1001) docker     (121)     9882 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/backup/backup_vault.py
--rw-r--r--   0 runner    (1001) docker     (121)    13350 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/backup/framework.py
--rw-r--r--   0 runner    (1001) docker     (121)    39459 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/backup/outputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    13437 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/backup/report_plan.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/batch/
--rw-r--r--   0 runner    (1001) docker     (121)      421 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/batch/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    52769 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/batch/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    10530 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/batch/compute_environment.py
--rw-r--r--   0 runner    (1001) docker     (121)    14861 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/batch/job_definition.py
--rw-r--r--   0 runner    (1001) docker     (121)     9729 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/batch/job_queue.py
--rw-r--r--   0 runner    (1001) docker     (121)    53446 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/batch/outputs.py
--rw-r--r--   0 runner    (1001) docker     (121)     6991 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/batch/scheduling_policy.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/budgets/
--rw-r--r--   0 runner    (1001) docker     (121)      372 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/budgets/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     1158 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/budgets/_enums.py
--rw-r--r--   0 runner    (1001) docker     (121)    23085 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/budgets/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)     6520 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/budgets/budget.py
--rw-r--r--   0 runner    (1001) docker     (121)    12600 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/budgets/budgets_action.py
--rw-r--r--   0 runner    (1001) docker     (121)    21533 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/budgets/outputs.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/cassandra/
--rw-r--r--   0 runner    (1001) docker     (121)      365 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/cassandra/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)      713 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/cassandra/_enums.py
--rw-r--r--   0 runner    (1001) docker     (121)     7176 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/cassandra/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)     5681 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/cassandra/keyspace.py
--rw-r--r--   0 runner    (1001) docker     (121)     8412 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/cassandra/outputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    18365 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/cassandra/table.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ce/
--rw-r--r--   0 runner    (1001) docker     (121)      416 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ce/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     1156 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ce/_enums.py
--rw-r--r--   0 runner    (1001) docker     (121)     1710 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ce/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    10942 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ce/anomaly_monitor.py
--rw-r--r--   0 runner    (1001) docker     (121)    12274 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ce/anomaly_subscription.py
--rw-r--r--   0 runner    (1001) docker     (121)     9934 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ce/cost_category.py
--rw-r--r--   0 runner    (1001) docker     (121)     1222 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ce/outputs.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/certificatemanager/
--rw-r--r--   0 runner    (1001) docker     (121)      348 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/certificatemanager/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     3231 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/certificatemanager/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)     5245 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/certificatemanager/account.py
--rw-r--r--   0 runner    (1001) docker     (121)    12295 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/certificatemanager/certificate.py
--rw-r--r--   0 runner    (1001) docker     (121)     3679 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/certificatemanager/outputs.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/chatbot/
--rw-r--r--   0 runner    (1001) docker     (121)      296 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/chatbot/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    16028 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/chatbot/slack_channel_configuration.py
--rw-r--r--   0 runner    (1001) docker     (121)     2122 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/cidr.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/cloud9/
--rw-r--r--   0 runner    (1001) docker     (121)      329 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/cloud9/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     1986 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/cloud9/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    13558 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/cloud9/environment_ec2.py
--rw-r--r--   0 runner    (1001) docker     (121)     2070 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/cloud9/outputs.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/cloudformation/
--rw-r--r--   0 runner    (1001) docker     (121)      716 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/cloudformation/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     3821 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/cloudformation/_enums.py
--rw-r--r--   0 runner    (1001) docker     (121)    18734 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/cloudformation/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)     5141 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/cloudformation/custom_resource.py
--rw-r--r--   0 runner    (1001) docker     (121)     8228 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/cloudformation/macro.py
--rw-r--r--   0 runner    (1001) docker     (121)     7457 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/cloudformation/module_default_version.py
--rw-r--r--   0 runner    (1001) docker     (121)     9767 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/cloudformation/module_version.py
--rw-r--r--   0 runner    (1001) docker     (121)    19691 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/cloudformation/outputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    11527 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/cloudformation/public_type_version.py
--rw-r--r--   0 runner    (1001) docker     (121)     9654 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/cloudformation/publisher.py
--rw-r--r--   0 runner    (1001) docker     (121)     8384 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/cloudformation/resource_default_version.py
--rw-r--r--   0 runner    (1001) docker     (121)    14948 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/cloudformation/resource_version.py
--rw-r--r--   0 runner    (1001) docker     (121)     8708 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/cloudformation/stack.py
--rw-r--r--   0 runner    (1001) docker     (121)    31552 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/cloudformation/stack_set.py
--rw-r--r--   0 runner    (1001) docker     (121)    20665 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/cloudformation/type_activation.py
--rw-r--r--   0 runner    (1001) docker     (121)     6618 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/cloudformation/wait_condition.py
--rw-r--r--   0 runner    (1001) docker     (121)     4348 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/cloudformation/wait_condition_handle.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/cloudfront/
--rw-r--r--   0 runner    (1001) docker     (121)      628 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/cloudfront/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)   116322 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/cloudfront/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)     5110 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/cloudfront/cache_policy.py
--rw-r--r--   0 runner    (1001) docker     (121)     6006 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/cloudfront/cloud_front_origin_access_identity.py
--rw-r--r--   0 runner    (1001) docker     (121)     6087 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/cloudfront/distribution.py
--rw-r--r--   0 runner    (1001) docker     (121)     8698 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/cloudfront/function.py
--rw-r--r--   0 runner    (1001) docker     (121)     4978 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/cloudfront/key_group.py
--rw-r--r--   0 runner    (1001) docker     (121)     5479 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/cloudfront/origin_request_policy.py
--rw-r--r--   0 runner    (1001) docker     (121)   112633 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/cloudfront/outputs.py
--rw-r--r--   0 runner    (1001) docker     (121)     4993 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/cloudfront/public_key.py
--rw-r--r--   0 runner    (1001) docker     (121)     7695 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/cloudfront/realtime_log_config.py
--rw-r--r--   0 runner    (1001) docker     (121)     5567 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/cloudfront/response_headers_policy.py
--rw-r--r--   0 runner    (1001) docker     (121)     7180 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/cloudfront/streaming_distribution.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/cloudtrail/
--rw-r--r--   0 runner    (1001) docker     (121)      341 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/cloudtrail/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)      587 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/cloudtrail/_enums.py
--rw-r--r--   0 runner    (1001) docker     (121)     9378 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/cloudtrail/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)     9623 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/cloudtrail/outputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    33128 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/cloudtrail/trail.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/cloudwatch/
--rw-r--r--   0 runner    (1001) docker     (121)      464 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/cloudwatch/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    20941 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/cloudwatch/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    24353 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/cloudwatch/alarm.py
--rw-r--r--   0 runner    (1001) docker     (121)    11797 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/cloudwatch/anomaly_detector.py
--rw-r--r--   0 runner    (1001) docker     (121)    15166 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/cloudwatch/composite_alarm.py
--rw-r--r--   0 runner    (1001) docker     (121)     5943 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/cloudwatch/dashboard.py
--rw-r--r--   0 runner    (1001) docker     (121)     7820 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/cloudwatch/insight_rule.py
--rw-r--r--   0 runner    (1001) docker     (121)    16693 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/cloudwatch/metric_stream.py
--rw-r--r--   0 runner    (1001) docker     (121)    19333 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/cloudwatch/outputs.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/codeartifact/
--rw-r--r--   0 runner    (1001) docker     (121)      346 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/codeartifact/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     4138 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/codeartifact/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)     8767 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/codeartifact/domain.py
--rw-r--r--   0 runner    (1001) docker     (121)     3686 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/codeartifact/outputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    13084 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/codeartifact/repository.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/codebuild/
--rw-r--r--   0 runner    (1001) docker     (121)      382 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/codebuild/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    38573 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/codebuild/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    37364 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/codebuild/outputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    28509 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/codebuild/project.py
--rw-r--r--   0 runner    (1001) docker     (121)     8874 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/codebuild/report_group.py
--rw-r--r--   0 runner    (1001) docker     (121)     7520 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/codebuild/source_credential.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/codecommit/
--rw-r--r--   0 runner    (1001) docker     (121)      324 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/codecommit/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     5296 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/codecommit/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)     5232 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/codecommit/outputs.py
--rw-r--r--   0 runner    (1001) docker     (121)     9945 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/codecommit/repository.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/codedeploy/
--rw-r--r--   0 runner    (1001) docker     (121)      390 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/codedeploy/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    32606 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/codedeploy/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)     7057 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/codedeploy/application.py
--rw-r--r--   0 runner    (1001) docker     (121)     8928 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/codedeploy/deployment_config.py
--rw-r--r--   0 runner    (1001) docker     (121)    24966 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/codedeploy/deployment_group.py
--rw-r--r--   0 runner    (1001) docker     (121)    35145 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/codedeploy/outputs.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/codeguruprofiler/
--rw-r--r--   0 runner    (1001) docker     (121)      351 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/codeguruprofiler/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)      411 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/codeguruprofiler/_enums.py
--rw-r--r--   0 runner    (1001) docker     (121)     4254 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/codeguruprofiler/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)     4369 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/codeguruprofiler/outputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    13053 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/codeguruprofiler/profiling_group.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/codegurureviewer/
--rw-r--r--   0 runner    (1001) docker     (121)      358 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/codegurureviewer/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)      489 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/codegurureviewer/_enums.py
--rw-r--r--   0 runner    (1001) docker     (121)     2329 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/codegurureviewer/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)     2103 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/codegurureviewer/outputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    12199 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/codegurureviewer/repository_association.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/codepipeline/
--rw-r--r--   0 runner    (1001) docker     (121)      379 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/codepipeline/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    22323 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/codepipeline/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    12905 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/codepipeline/custom_action_type.py
--rw-r--r--   0 runner    (1001) docker     (121)    20047 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/codepipeline/outputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    13009 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/codepipeline/pipeline.py
--rw-r--r--   0 runner    (1001) docker     (121)    12544 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/codepipeline/webhook.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/codestar/
--rw-r--r--   0 runner    (1001) docker     (121)      332 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/codestar/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     2013 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/codestar/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    11904 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/codestar/git_hub_repository.py
--rw-r--r--   0 runner    (1001) docker     (121)     2035 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/codestar/outputs.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/codestarconnections/
--rw-r--r--   0 runner    (1001) docker     (121)      324 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/codestarconnections/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     2239 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/codestarconnections/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    11044 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/codestarconnections/connection.py
--rw-r--r--   0 runner    (1001) docker     (121)     2013 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/codestarconnections/outputs.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/codestarnotifications/
--rw-r--r--   0 runner    (1001) docker     (121)      353 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/codestarnotifications/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)      448 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/codestarnotifications/_enums.py
--rw-r--r--   0 runner    (1001) docker     (121)     1259 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/codestarnotifications/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    12850 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/codestarnotifications/notification_rule.py
--rw-r--r--   0 runner    (1001) docker     (121)     1605 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/codestarnotifications/outputs.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/cognito/
--rw-r--r--   0 runner    (1001) docker     (121)      764 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/cognito/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    57789 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/cognito/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    16676 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/cognito/identity_pool.py
--rw-r--r--   0 runner    (1001) docker     (121)     6925 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/cognito/identity_pool_role_attachment.py
--rw-r--r--   0 runner    (1001) docker     (121)    64254 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/cognito/outputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    29578 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/cognito/user_pool.py
--rw-r--r--   0 runner    (1001) docker     (121)    26513 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/cognito/user_pool_client.py
--rw-r--r--   0 runner    (1001) docker     (121)     7208 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/cognito/user_pool_domain.py
--rw-r--r--   0 runner    (1001) docker     (121)     8348 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/cognito/user_pool_group.py
--rw-r--r--   0 runner    (1001) docker     (121)    10027 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/cognito/user_pool_identity_provider.py
--rw-r--r--   0 runner    (1001) docker     (121)     8062 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/cognito/user_pool_resource_server.py
--rw-r--r--   0 runner    (1001) docker     (121)    11798 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/cognito/user_pool_risk_configuration_attachment.py
--rw-r--r--   0 runner    (1001) docker     (121)     7125 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/cognito/user_pool_ui_customization_attachment.py
--rw-r--r--   0 runner    (1001) docker     (121)    12408 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/cognito/user_pool_user.py
--rw-r--r--   0 runner    (1001) docker     (121)     7130 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/cognito/user_pool_user_to_group_attachment.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/config/
--rw-r--r--   0 runner    (1001) docker     (121)      269 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/config/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    78929 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/config/outputs.py
--rw-r--r--   0 runner    (1001) docker     (121)     6489 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/config/vars.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/configuration/
--rw-r--r--   0 runner    (1001) docker     (121)      662 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/configuration/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    30525 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/configuration/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)     8767 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/configuration/aggregation_authorization.py
--rw-r--r--   0 runner    (1001) docker     (121)    11113 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/configuration/config_rule.py
--rw-r--r--   0 runner    (1001) docker     (121)    10441 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/configuration/configuration_aggregator.py
--rw-r--r--   0 runner    (1001) docker     (121)     7137 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/configuration/configuration_recorder.py
--rw-r--r--   0 runner    (1001) docker     (121)    13936 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/configuration/conformance_pack.py
--rw-r--r--   0 runner    (1001) docker     (121)    10225 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/configuration/delivery_channel.py
--rw-r--r--   0 runner    (1001) docker     (121)     9955 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/configuration/organization_config_rule.py
--rw-r--r--   0 runner    (1001) docker     (121)    15090 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/configuration/organization_conformance_pack.py
--rw-r--r--   0 runner    (1001) docker     (121)    32449 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/configuration/outputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    13980 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/configuration/remediation_configuration.py
--rw-r--r--   0 runner    (1001) docker     (121)     8268 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/configuration/stored_query.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/connect/
--rw-r--r--   0 runner    (1001) docker     (121)      502 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/connect/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     1994 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/connect/_enums.py
--rw-r--r--   0 runner    (1001) docker     (121)    21885 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/connect/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    11959 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/connect/contact_flow.py
--rw-r--r--   0 runner    (1001) docker     (121)    11549 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/connect/contact_flow_module.py
--rw-r--r--   0 runner    (1001) docker     (121)    11714 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/connect/hours_of_operation.py
--rw-r--r--   0 runner    (1001) docker     (121)    22788 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/connect/outputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    10316 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/connect/quick_connect.py
--rw-r--r--   0 runner    (1001) docker     (121)    17719 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/connect/user.py
--rw-r--r--   0 runner    (1001) docker     (121)     7738 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/connect/user_hierarchy_group.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/cur/
--rw-r--r--   0 runner    (1001) docker     (121)      308 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/cur/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     1661 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/cur/_enums.py
--rw-r--r--   0 runner    (1001) docker     (121)    24282 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/cur/report_definition.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/customerprofiles/
--rw-r--r--   0 runner    (1001) docker     (121)      396 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/customerprofiles/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     5795 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/customerprofiles/_enums.py
--rw-r--r--   0 runner    (1001) docker     (121)    35152 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/customerprofiles/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    10976 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/customerprofiles/domain.py
--rw-r--r--   0 runner    (1001) docker     (121)    10663 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/customerprofiles/integration.py
--rw-r--r--   0 runner    (1001) docker     (121)    17534 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/customerprofiles/object_type.py
--rw-r--r--   0 runner    (1001) docker     (121)    34978 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/customerprofiles/outputs.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/databrew/
--rw-r--r--   0 runner    (1001) docker     (121)      454 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/databrew/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     2808 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/databrew/_enums.py
--rw-r--r--   0 runner    (1001) docker     (121)   123545 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/databrew/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    10257 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/databrew/dataset.py
--rw-r--r--   0 runner    (1001) docker     (121)    26778 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/databrew/job.py
--rw-r--r--   0 runner    (1001) docker     (121)   111282 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/databrew/outputs.py
--rw-r--r--   0 runner    (1001) docker     (121)     9737 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/databrew/project.py
--rw-r--r--   0 runner    (1001) docker     (121)     7418 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/databrew/recipe.py
--rw-r--r--   0 runner    (1001) docker     (121)     9205 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/databrew/ruleset.py
--rw-r--r--   0 runner    (1001) docker     (121)     7536 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/databrew/schedule.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/datapipeline/
--rw-r--r--   0 runner    (1001) docker     (121)      322 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/datapipeline/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     6003 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/datapipeline/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)     5746 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/datapipeline/outputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    11364 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/datapipeline/pipeline.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/datasync/
--rw-r--r--   0 runner    (1001) docker     (121)      577 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/datasync/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     6505 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/datasync/_enums.py
--rw-r--r--   0 runner    (1001) docker     (121)    34740 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/datasync/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    12768 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/datasync/agent.py
--rw-r--r--   0 runner    (1001) docker     (121)     9917 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/datasync/location_efs.py
--rw-r--r--   0 runner    (1001) docker     (121)    14215 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/datasync/location_f_sx_windows.py
--rw-r--r--   0 runner    (1001) docker     (121)    23250 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/datasync/location_hdfs.py
--rw-r--r--   0 runner    (1001) docker     (121)    11023 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/datasync/location_nfs.py
--rw-r--r--   0 runner    (1001) docker     (121)    17875 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/datasync/location_object_storage.py
--rw-r--r--   0 runner    (1001) docker     (121)    11413 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/datasync/location_s3.py
--rw-r--r--   0 runner    (1001) docker     (121)    15411 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/datasync/location_smb.py
--rw-r--r--   0 runner    (1001) docker     (121)    33362 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/datasync/outputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    16639 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/datasync/task.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/dax/
--rw-r--r--   0 runner    (1001) docker     (121)      380 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/dax/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)      922 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/dax/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    18892 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/dax/cluster.py
--rw-r--r--   0 runner    (1001) docker     (121)     1344 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/dax/outputs.py
--rw-r--r--   0 runner    (1001) docker     (121)     6988 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/dax/parameter_group.py
--rw-r--r--   0 runner    (1001) docker     (121)     6892 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/dax/subnet_group.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/detective/
--rw-r--r--   0 runner    (1001) docker     (121)      352 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/detective/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     2345 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/detective/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)     4698 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/detective/graph.py
--rw-r--r--   0 runner    (1001) docker     (121)    11321 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/detective/member_invitation.py
--rw-r--r--   0 runner    (1001) docker     (121)     2099 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/detective/outputs.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/devicefarm/
--rw-r--r--   0 runner    (1001) docker     (121)      500 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/devicefarm/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     1183 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/devicefarm/_enums.py
--rw-r--r--   0 runner    (1001) docker     (121)     8607 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/devicefarm/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)     9129 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/devicefarm/device_pool.py
--rw-r--r--   0 runner    (1001) docker     (121)     9715 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/devicefarm/instance_profile.py
--rw-r--r--   0 runner    (1001) docker     (121)    15238 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/devicefarm/network_profile.py
--rw-r--r--   0 runner    (1001) docker     (121)     6744 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/devicefarm/outputs.py
--rw-r--r--   0 runner    (1001) docker     (121)     6559 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/devicefarm/project.py
--rw-r--r--   0 runner    (1001) docker     (121)     7471 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/devicefarm/test_grid_project.py
--rw-r--r--   0 runner    (1001) docker     (121)     9296 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/devicefarm/vpce_configuration.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/devopsguru/
--rw-r--r--   0 runner    (1001) docker     (121)      391 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/devopsguru/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)      378 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/devopsguru/_enums.py
--rw-r--r--   0 runner    (1001) docker     (121)     3684 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/devopsguru/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)     4804 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/devopsguru/notification_channel.py
--rw-r--r--   0 runner    (1001) docker     (121)     5240 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/devopsguru/outputs.py
--rw-r--r--   0 runner    (1001) docker     (121)     5606 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/devopsguru/resource_collection.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/directoryservice/
--rw-r--r--   0 runner    (1001) docker     (121)      351 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/directoryservice/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     2118 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/directoryservice/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    10607 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/directoryservice/microsoft_ad.py
--rw-r--r--   0 runner    (1001) docker     (121)     2715 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/directoryservice/outputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    11324 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/directoryservice/simple_ad.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/dlm/
--rw-r--r--   0 runner    (1001) docker     (121)      330 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/dlm/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    32665 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/dlm/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)     9116 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/dlm/lifecycle_policy.py
--rw-r--r--   0 runner    (1001) docker     (121)    32397 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/dlm/outputs.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/dms/
--rw-r--r--   0 runner    (1001) docker     (121)      491 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/dms/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    49988 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/dms/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)     7085 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/dms/certificate.py
--rw-r--r--   0 runner    (1001) docker     (121)    35369 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/dms/endpoint.py
--rw-r--r--   0 runner    (1001) docker     (121)    10858 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/dms/event_subscription.py
--rw-r--r--   0 runner    (1001) docker     (121)    48226 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/dms/outputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    20950 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/dms/replication_instance.py
--rw-r--r--   0 runner    (1001) docker     (121)     9106 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/dms/replication_subnet_group.py
--rw-r--r--   0 runner    (1001) docker     (121)    17317 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/dms/replication_task.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/docdb/
--rw-r--r--   0 runner    (1001) docker     (121)      424 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/docdb/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     3202 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/docdb/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    23535 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/docdb/db_cluster.py
--rw-r--r--   0 runner    (1001) docker     (121)     8592 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/docdb/db_cluster_parameter_group.py
--rw-r--r--   0 runner    (1001) docker     (121)    11976 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/docdb/db_instance.py
--rw-r--r--   0 runner    (1001) docker     (121)     8443 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/docdb/db_subnet_group.py
--rw-r--r--   0 runner    (1001) docker     (121)     2142 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/docdb/outputs.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/dynamodb/
--rw-r--r--   0 runner    (1001) docker     (121)      347 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/dynamodb/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    39826 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/dynamodb/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    18247 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/dynamodb/global_table.py
--rw-r--r--   0 runner    (1001) docker     (121)    46003 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/dynamodb/outputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    22860 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/dynamodb/table.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 14:35:49.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ec2/
--rw-r--r--   0 runner    (1001) docker     (121)     3261 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ec2/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    14897 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ec2/_enums.py
--rw-r--r--   0 runner    (1001) docker     (121)   303634 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ec2/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    17488 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ec2/capacity_reservation.py
--rw-r--r--   0 runner    (1001) docker     (121)    14294 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ec2/capacity_reservation_fleet.py
--rw-r--r--   0 runner    (1001) docker     (121)     7031 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ec2/carrier_gateway.py
--rw-r--r--   0 runner    (1001) docker     (121)     9364 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ec2/client_vpn_authorization_rule.py
--rw-r--r--   0 runner    (1001) docker     (121)    19384 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ec2/client_vpn_endpoint.py
--rw-r--r--   0 runner    (1001) docker     (121)     8261 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ec2/client_vpn_route.py
--rw-r--r--   0 runner    (1001) docker     (121)     6571 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ec2/client_vpn_target_network_association.py
--rw-r--r--   0 runner    (1001) docker     (121)     7682 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ec2/customer_gateway.py
--rw-r--r--   0 runner    (1001) docker     (121)    12516 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ec2/dhcp_options.py
--rw-r--r--   0 runner    (1001) docker     (121)    17650 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ec2/ec2_fleet.py
--rw-r--r--   0 runner    (1001) docker     (121)     5054 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ec2/egress_only_internet_gateway.py
--rw-r--r--   0 runner    (1001) docker     (121)     7711 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ec2/eip.py
--rw-r--r--   0 runner    (1001) docker     (121)     8664 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ec2/eipassociation.py
--rw-r--r--   0 runner    (1001) docker     (121)     8792 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ec2/enclave_certificate_iam_role_association.py
--rw-r--r--   0 runner    (1001) docker     (121)    22563 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ec2/flow_log.py
--rw-r--r--   0 runner    (1001) docker     (121)     6837 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ec2/gateway_route_table_association.py
--rw-r--r--   0 runner    (1001) docker     (121)    10312 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ec2/host.py
--rw-r--r--   0 runner    (1001) docker     (121)    46153 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ec2/instance.py
--rw-r--r--   0 runner    (1001) docker     (121)     5464 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ec2/internet_gateway.py
--rw-r--r--   0 runner    (1001) docker     (121)     9434 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ec2/ipam.py
--rw-r--r--   0 runner    (1001) docker     (121)     8294 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ec2/ipam_allocation.py
--rw-r--r--   0 runner    (1001) docker     (121)    27172 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ec2/ipam_pool.py
--rw-r--r--   0 runner    (1001) docker     (121)     8977 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ec2/ipam_scope.py
--rw-r--r--   0 runner    (1001) docker     (121)     8388 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ec2/launch_template.py
--rw-r--r--   0 runner    (1001) docker     (121)     9010 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ec2/local_gateway_route.py
--rw-r--r--   0 runner    (1001) docker     (121)     9272 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ec2/local_gateway_route_table_vpcassociation.py
--rw-r--r--   0 runner    (1001) docker     (121)     7813 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ec2/nat_gateway.py
--rw-r--r--   0 runner    (1001) docker     (121)     5970 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ec2/network_acl.py
--rw-r--r--   0 runner    (1001) docker     (121)    19877 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ec2/network_acl_entry.py
--rw-r--r--   0 runner    (1001) docker     (121)     8894 2022-01-10 14:35:47.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ec2/network_insights_access_scope.py
--rw-r--r--   0 runner    (1001) docker     (121)     8839 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ec2/network_insights_access_scope_analysis.py
--rw-r--r--   0 runner    (1001) docker     (121)    10128 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ec2/network_insights_analysis.py
--rw-r--r--   0 runner    (1001) docker     (121)    10941 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ec2/network_insights_path.py
--rw-r--r--   0 runner    (1001) docker     (121)    25145 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ec2/network_interface.py
--rw-r--r--   0 runner    (1001) docker     (121)     8368 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ec2/network_interface_attachment.py
--rw-r--r--   0 runner    (1001) docker     (121)     7309 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ec2/network_interface_permission.py
--rw-r--r--   0 runner    (1001) docker     (121)   325272 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ec2/outputs.py
--rw-r--r--   0 runner    (1001) docker     (121)     4960 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ec2/placement_group.py
--rw-r--r--   0 runner    (1001) docker     (121)    11177 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ec2/prefix_list.py
--rw-r--r--   0 runner    (1001) docker     (121)    16872 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ec2/route.py
--rw-r--r--   0 runner    (1001) docker     (121)     6283 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ec2/route_table.py
--rw-r--r--   0 runner    (1001) docker     (121)    10732 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ec2/security_group.py
--rw-r--r--   0 runner    (1001) docker     (121)    12385 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ec2/security_group_egress.py
--rw-r--r--   0 runner    (1001) docker     (121)    15342 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ec2/security_group_ingress.py
--rw-r--r--   0 runner    (1001) docker     (121)     5047 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ec2/spot_fleet.py
--rw-r--r--   0 runner    (1001) docker     (121)    12014 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ec2/subnet.py
--rw-r--r--   0 runner    (1001) docker     (121)     6026 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ec2/subnet_cidr_block.py
--rw-r--r--   0 runner    (1001) docker     (121)     6435 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ec2/subnet_network_acl_association.py
--rw-r--r--   0 runner    (1001) docker     (121)     5667 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ec2/subnet_route_table_association.py
--rw-r--r--   0 runner    (1001) docker     (121)     7270 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ec2/traffic_mirror_filter.py
--rw-r--r--   0 runner    (1001) docker     (121)    14741 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ec2/traffic_mirror_filter_rule.py
--rw-r--r--   0 runner    (1001) docker     (121)    12378 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ec2/traffic_mirror_session.py
--rw-r--r--   0 runner    (1001) docker     (121)     8314 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ec2/traffic_mirror_target.py
--rw-r--r--   0 runner    (1001) docker     (121)    16591 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ec2/transit_gateway.py
--rw-r--r--   0 runner    (1001) docker     (121)     8342 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ec2/transit_gateway_attachment.py
--rw-r--r--   0 runner    (1001) docker     (121)     9793 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ec2/transit_gateway_connect.py
--rw-r--r--   0 runner    (1001) docker     (121)     9693 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ec2/transit_gateway_multicast_domain.py
--rw-r--r--   0 runner    (1001) docker     (121)     9657 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ec2/transit_gateway_multicast_domain_association.py
--rw-r--r--   0 runner    (1001) docker     (121)    11424 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ec2/transit_gateway_multicast_group_member.py
--rw-r--r--   0 runner    (1001) docker     (121)    11424 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ec2/transit_gateway_multicast_group_source.py
--rw-r--r--   0 runner    (1001) docker     (121)    13595 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ec2/transit_gateway_peering_attachment.py
--rw-r--r--   0 runner    (1001) docker     (121)     8560 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ec2/transit_gateway_route.py
--rw-r--r--   0 runner    (1001) docker     (121)     6532 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ec2/transit_gateway_route_table.py
--rw-r--r--   0 runner    (1001) docker     (121)     7143 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ec2/transit_gateway_route_table_association.py
--rw-r--r--   0 runner    (1001) docker     (121)     7143 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ec2/transit_gateway_route_table_propagation.py
--rw-r--r--   0 runner    (1001) docker     (121)    11164 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ec2/transit_gateway_vpc_attachment.py
--rw-r--r--   0 runner    (1001) docker     (121)    14339 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ec2/volume.py
--rw-r--r--   0 runner    (1001) docker     (121)     6749 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ec2/volume_attachment.py
--rw-r--r--   0 runner    (1001) docker     (121)    16196 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ec2/vpc.py
--rw-r--r--   0 runner    (1001) docker     (121)     8729 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ec2/vpc_cidr_block.py
--rw-r--r--   0 runner    (1001) docker     (121)    12637 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ec2/vpc_endpoint.py
--rw-r--r--   0 runner    (1001) docker     (121)     8730 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ec2/vpc_endpoint_connection_notification.py
--rw-r--r--   0 runner    (1001) docker     (121)     8810 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ec2/vpc_endpoint_service.py
--rw-r--r--   0 runner    (1001) docker     (121)     6508 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ec2/vpc_endpoint_service_permissions.py
--rw-r--r--   0 runner    (1001) docker     (121)     7019 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ec2/vpc_gateway_attachment.py
--rw-r--r--   0 runner    (1001) docker     (121)     9721 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ec2/vpc_peering_connection.py
--rw-r--r--   0 runner    (1001) docker     (121)     6369 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ec2/vpcdhcp_options_association.py
--rw-r--r--   0 runner    (1001) docker     (121)    11534 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ec2/vpn_connection.py
--rw-r--r--   0 runner    (1001) docker     (121)     6378 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ec2/vpn_connection_route.py
--rw-r--r--   0 runner    (1001) docker     (121)     6764 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ec2/vpn_gateway.py
--rw-r--r--   0 runner    (1001) docker     (121)     6502 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ec2/vpn_gateway_route_propagation.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 14:35:49.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ecr/
--rw-r--r--   0 runner    (1001) docker     (121)      451 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ecr/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)      756 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ecr/_enums.py
--rw-r--r--   0 runner    (1001) docker     (121)    16208 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ecr/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    18753 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ecr/outputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    13367 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ecr/public_repository.py
--rw-r--r--   0 runner    (1001) docker     (121)     6513 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ecr/registry_policy.py
--rw-r--r--   0 runner    (1001) docker     (121)     5968 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ecr/replication_configuration.py
--rw-r--r--   0 runner    (1001) docker     (121)    16427 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ecr/repository.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 14:35:49.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ecs/
--rw-r--r--   0 runner    (1001) docker     (121)      540 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ecs/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     2893 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ecs/_enums.py
--rw-r--r--   0 runner    (1001) docker     (121)   113649 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ecs/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)     6925 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ecs/capacity_provider.py
--rw-r--r--   0 runner    (1001) docker     (121)    11539 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ecs/cluster.py
--rw-r--r--   0 runner    (1001) docker     (121)     8200 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ecs/cluster_capacity_provider_associations.py
--rw-r--r--   0 runner    (1001) docker     (121)   111338 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ecs/outputs.py
--rw-r--r--   0 runner    (1001) docker     (121)     7636 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ecs/primary_task_set.py
--rw-r--r--   0 runner    (1001) docker     (121)    27131 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ecs/service.py
--rw-r--r--   0 runner    (1001) docker     (121)    21822 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ecs/task_definition.py
--rw-r--r--   0 runner    (1001) docker     (121)    20616 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ecs/task_set.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 14:35:49.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/efs/
--rw-r--r--   0 runner    (1001) docker     (121)      381 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/efs/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    10630 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/efs/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    13087 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/efs/access_point.py
--rw-r--r--   0 runner    (1001) docker     (121)    17840 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/efs/file_system.py
--rw-r--r--   0 runner    (1001) docker     (121)     7304 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/efs/mount_target.py
--rw-r--r--   0 runner    (1001) docker     (121)    10710 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/efs/outputs.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 14:35:49.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/eks/
--rw-r--r--   0 runner    (1001) docker     (121)      420 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/eks/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)      608 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/eks/_enums.py
--rw-r--r--   0 runner    (1001) docker     (121)    28356 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/eks/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    11340 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/eks/addon.py
--rw-r--r--   0 runner    (1001) docker     (121)    16475 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/eks/cluster.py
--rw-r--r--   0 runner    (1001) docker     (121)    11157 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/eks/fargate_profile.py
--rw-r--r--   0 runner    (1001) docker     (121)    20947 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/eks/nodegroup.py
--rw-r--r--   0 runner    (1001) docker     (121)    27870 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/eks/outputs.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 14:35:49.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/elasticache/
--rw-r--r--   0 runner    (1001) docker     (121)      595 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/elasticache/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)      645 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/elasticache/_enums.py
--rw-r--r--   0 runner    (1001) docker     (121)    23112 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/elasticache/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    31486 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/elasticache/cache_cluster.py
--rw-r--r--   0 runner    (1001) docker     (121)    19833 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/elasticache/global_replication_group.py
--rw-r--r--   0 runner    (1001) docker     (121)    25211 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/elasticache/outputs.py
--rw-r--r--   0 runner    (1001) docker     (121)     8045 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/elasticache/parameter_group.py
--rw-r--r--   0 runner    (1001) docker     (121)    51830 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/elasticache/replication_group.py
--rw-r--r--   0 runner    (1001) docker     (121)     6068 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/elasticache/security_group.py
--rw-r--r--   0 runner    (1001) docker     (121)     7786 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/elasticache/security_group_ingress.py
--rw-r--r--   0 runner    (1001) docker     (121)     8086 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/elasticache/subnet_group.py
--rw-r--r--   0 runner    (1001) docker     (121)    11405 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/elasticache/user.py
--rw-r--r--   0 runner    (1001) docker     (121)     7770 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/elasticache/user_group.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 14:35:49.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/elasticbeanstalk/
--rw-r--r--   0 runner    (1001) docker     (121)      425 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/elasticbeanstalk/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    13202 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/elasticbeanstalk/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)     7337 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/elasticbeanstalk/application.py
--rw-r--r--   0 runner    (1001) docker     (121)     7332 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/elasticbeanstalk/application_version.py
--rw-r--r--   0 runner    (1001) docker     (121)    11724 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/elasticbeanstalk/configuration_template.py
--rw-r--r--   0 runner    (1001) docker     (121)    15766 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/elasticbeanstalk/environment.py
--rw-r--r--   0 runner    (1001) docker     (121)    14438 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/elasticbeanstalk/outputs.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 14:35:49.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/elasticloadbalancing/
--rw-r--r--   0 runner    (1001) docker     (121)      327 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/elasticloadbalancing/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    13693 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/elasticloadbalancing/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    25444 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/elasticloadbalancing/load_balancer.py
--rw-r--r--   0 runner    (1001) docker     (121)    14099 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/elasticloadbalancing/outputs.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 14:35:49.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/elasticloadbalancingv2/
--rw-r--r--   0 runner    (1001) docker     (121)      444 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/elasticloadbalancingv2/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    62045 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/elasticloadbalancingv2/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    10543 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/elasticloadbalancingv2/listener.py
--rw-r--r--   0 runner    (1001) docker     (121)     6586 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/elasticloadbalancingv2/listener_certificate.py
--rw-r--r--   0 runner    (1001) docker     (121)     8147 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/elasticloadbalancingv2/listener_rule.py
--rw-r--r--   0 runner    (1001) docker     (121)    14064 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/elasticloadbalancingv2/load_balancer.py
--rw-r--r--   0 runner    (1001) docker     (121)    59592 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/elasticloadbalancingv2/outputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    23654 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/elasticloadbalancingv2/target_group.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 14:35:49.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/elasticsearch/
--rw-r--r--   0 runner    (1001) docker     (121)      320 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/elasticsearch/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    21883 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/elasticsearch/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    21494 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/elasticsearch/domain.py
--rw-r--r--   0 runner    (1001) docker     (121)    22570 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/elasticsearch/outputs.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 14:35:49.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/emr/
--rw-r--r--   0 runner    (1001) docker     (121)      535 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/emr/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)      686 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/emr/_enums.py
--rw-r--r--   0 runner    (1001) docker     (121)    95167 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/emr/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    26635 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/emr/cluster.py
--rw-r--r--   0 runner    (1001) docker     (121)    11970 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/emr/instance_fleet_config.py
--rw-r--r--   0 runner    (1001) docker     (121)    14956 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/emr/instance_group_config.py
--rw-r--r--   0 runner    (1001) docker     (121)    95382 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/emr/outputs.py
--rw-r--r--   0 runner    (1001) docker     (121)     6076 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/emr/security_configuration.py
--rw-r--r--   0 runner    (1001) docker     (121)     7755 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/emr/step.py
--rw-r--r--   0 runner    (1001) docker     (121)    26554 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/emr/studio.py
--rw-r--r--   0 runner    (1001) docker     (121)    10534 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/emr/studio_session_mapping.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 14:35:49.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/emrcontainers/
--rw-r--r--   0 runner    (1001) docker     (121)      329 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/emrcontainers/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     4703 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/emrcontainers/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)     4366 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/emrcontainers/outputs.py
--rw-r--r--   0 runner    (1001) docker     (121)     8022 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/emrcontainers/virtual_cluster.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 14:35:49.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/events/
--rw-r--r--   0 runner    (1001) docker     (121)      477 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/events/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)      751 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/events/_enums.py
--rw-r--r--   0 runner    (1001) docker     (121)    47936 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/events/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    10488 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/events/api_destination.py
--rw-r--r--   0 runner    (1001) docker     (121)     7369 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/events/archive.py
--rw-r--r--   0 runner    (1001) docker     (121)     8631 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/events/connection.py
--rw-r--r--   0 runner    (1001) docker     (121)     7166 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/events/event_bus.py
--rw-r--r--   0 runner    (1001) docker     (121)     9273 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/events/event_bus_policy.py
--rw-r--r--   0 runner    (1001) docker     (121)    46553 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/events/outputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    10994 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/events/rule.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 14:35:49.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/eventschemas/
--rw-r--r--   0 runner    (1001) docker     (121)      401 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/eventschemas/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     2486 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/eventschemas/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)     8282 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/eventschemas/discoverer.py
--rw-r--r--   0 runner    (1001) docker     (121)     1691 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/eventschemas/outputs.py
--rw-r--r--   0 runner    (1001) docker     (121)     7086 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/eventschemas/registry.py
--rw-r--r--   0 runner    (1001) docker     (121)     6131 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/eventschemas/registry_policy.py
--rw-r--r--   0 runner    (1001) docker     (121)     9697 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/eventschemas/schema.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 14:35:49.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/evidently/
--rw-r--r--   0 runner    (1001) docker     (121)      414 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/evidently/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)      516 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/evidently/_enums.py
--rw-r--r--   0 runner    (1001) docker     (121)    27085 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/evidently/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    13099 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/evidently/experiment.py
--rw-r--r--   0 runner    (1001) docker     (121)    12006 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/evidently/feature.py
--rw-r--r--   0 runner    (1001) docker     (121)    12164 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/evidently/launch.py
--rw-r--r--   0 runner    (1001) docker     (121)    28225 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/evidently/outputs.py
--rw-r--r--   0 runner    (1001) docker     (121)     7778 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/evidently/project.py
--rw-r--r--   0 runner    (1001) docker     (121)     6031 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/extension_resource.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 14:35:49.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/finspace/
--rw-r--r--   0 runner    (1001) docker     (121)      347 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/finspace/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)      833 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/finspace/_enums.py
--rw-r--r--   0 runner    (1001) docker     (121)     6760 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/finspace/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    14925 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/finspace/environment.py
--rw-r--r--   0 runner    (1001) docker     (121)     7034 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/finspace/outputs.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 14:35:49.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/fis/
--rw-r--r--   0 runner    (1001) docker     (121)      333 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/fis/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     1581 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/fis/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)     9413 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/fis/experiment_template.py
--rw-r--r--   0 runner    (1001) docker     (121)     1399 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/fis/outputs.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 14:35:49.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/fms/
--rw-r--r--   0 runner    (1001) docker     (121)      378 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/fms/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)      663 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/fms/_enums.py
--rw-r--r--   0 runner    (1001) docker     (121)     4225 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/fms/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)     5704 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/fms/notification_channel.py
--rw-r--r--   0 runner    (1001) docker     (121)     4281 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/fms/outputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    16455 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/fms/policy.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 14:35:49.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/frauddetector/
--rw-r--r--   0 runner    (1001) docker     (121)      465 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/frauddetector/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     5396 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/frauddetector/_enums.py
--rw-r--r--   0 runner    (1001) docker     (121)    47700 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/frauddetector/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    15382 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/frauddetector/detector.py
--rw-r--r--   0 runner    (1001) docker     (121)     7941 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/frauddetector/entity_type.py
--rw-r--r--   0 runner    (1001) docker     (121)    11540 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/frauddetector/event_type.py
--rw-r--r--   0 runner    (1001) docker     (121)     7714 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/frauddetector/label.py
--rw-r--r--   0 runner    (1001) docker     (121)     7800 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/frauddetector/outcome.py
--rw-r--r--   0 runner    (1001) docker     (121)    38967 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/frauddetector/outputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    13355 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/frauddetector/variable.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 14:35:49.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/fsx/
--rw-r--r--   0 runner    (1001) docker     (121)      325 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/fsx/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    38450 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/fsx/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    18593 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/fsx/file_system.py
--rw-r--r--   0 runner    (1001) docker     (121)    35450 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/fsx/outputs.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 14:35:49.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/gamelift/
--rw-r--r--   0 runner    (1001) docker     (121)      549 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/gamelift/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     2671 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/gamelift/_enums.py
--rw-r--r--   0 runner    (1001) docker     (121)    39310 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/gamelift/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)     8132 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/gamelift/alias.py
--rw-r--r--   0 runner    (1001) docker     (121)     7543 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/gamelift/build.py
--rw-r--r--   0 runner    (1001) docker     (121)    53499 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/gamelift/fleet.py
--rw-r--r--   0 runner    (1001) docker     (121)    24548 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/gamelift/game_server_group.py
--rw-r--r--   0 runner    (1001) docker     (121)    14414 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/gamelift/game_session_queue.py
--rw-r--r--   0 runner    (1001) docker     (121)    19810 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/gamelift/matchmaking_configuration.py
--rw-r--r--   0 runner    (1001) docker     (121)     7174 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/gamelift/matchmaking_rule_set.py
--rw-r--r--   0 runner    (1001) docker     (121)    46051 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/gamelift/outputs.py
--rw-r--r--   0 runner    (1001) docker     (121)     7803 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/gamelift/script.py
--rw-r--r--   0 runner    (1001) docker     (121)     1611 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/get_account_id.py
--rw-r--r--   0 runner    (1001) docker     (121)     1851 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/get_azs.py
--rw-r--r--   0 runner    (1001) docker     (121)     1579 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/get_partition.py
--rw-r--r--   0 runner    (1001) docker     (121)     1507 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/get_region.py
--rw-r--r--   0 runner    (1001) docker     (121)     2105 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/get_ssm_parameter_list.py
--rw-r--r--   0 runner    (1001) docker     (121)     2129 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/get_ssm_parameter_string.py
--rw-r--r--   0 runner    (1001) docker     (121)     1611 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/get_url_suffix.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 14:35:49.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/globalaccelerator/
--rw-r--r--   0 runner    (1001) docker     (121)      401 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/globalaccelerator/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)      988 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/globalaccelerator/_enums.py
--rw-r--r--   0 runner    (1001) docker     (121)     5767 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/globalaccelerator/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    10239 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/globalaccelerator/accelerator.py
--rw-r--r--   0 runner    (1001) docker     (121)    19032 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/globalaccelerator/endpoint_group.py
--rw-r--r--   0 runner    (1001) docker     (121)     9246 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/globalaccelerator/listener.py
--rw-r--r--   0 runner    (1001) docker     (121)     6613 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/globalaccelerator/outputs.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 14:35:49.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/glue/
--rw-r--r--   0 runner    (1001) docker     (121)      788 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/glue/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)      762 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/glue/_enums.py
--rw-r--r--   0 runner    (1001) docker     (121)   102144 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/glue/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)     8634 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/glue/classifier.py
--rw-r--r--   0 runner    (1001) docker     (121)     6147 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/glue/connection.py
--rw-r--r--   0 runner    (1001) docker     (121)    15883 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/glue/crawler.py
--rw-r--r--   0 runner    (1001) docker     (121)     7004 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/glue/data_catalog_encryption_settings.py
--rw-r--r--   0 runner    (1001) docker     (121)     6051 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/glue/database.py
--rw-r--r--   0 runner    (1001) docker     (121)    17697 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/glue/dev_endpoint.py
--rw-r--r--   0 runner    (1001) docker     (121)    20079 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/glue/job.py
--rw-r--r--   0 runner    (1001) docker     (121)    16075 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/glue/ml_transform.py
--rw-r--r--   0 runner    (1001) docker     (121)   105346 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/glue/outputs.py
--rw-r--r--   0 runner    (1001) docker     (121)     7912 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/glue/partition.py
--rw-r--r--   0 runner    (1001) docker     (121)     8129 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/glue/registry.py
--rw-r--r--   0 runner    (1001) docker     (121)    14160 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/glue/schema.py
--rw-r--r--   0 runner    (1001) docker     (121)     6425 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/glue/schema_version.py
--rw-r--r--   0 runner    (1001) docker     (121)     7088 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/glue/schema_version_metadata.py
--rw-r--r--   0 runner    (1001) docker     (121)     6544 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/glue/security_configuration.py
--rw-r--r--   0 runner    (1001) docker     (121)     6842 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/glue/table.py
--rw-r--r--   0 runner    (1001) docker     (121)    11587 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/glue/trigger.py
--rw-r--r--   0 runner    (1001) docker     (121)     7197 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/glue/workflow.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 14:35:49.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/greengrass/
--rw-r--r--   0 runner    (1001) docker     (121)      888 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/greengrass/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    76877 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/greengrass/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)     7330 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/greengrass/connector_definition.py
--rw-r--r--   0 runner    (1001) docker     (121)     6914 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/greengrass/connector_definition_version.py
--rw-r--r--   0 runner    (1001) docker     (121)     7185 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/greengrass/core_definition.py
--rw-r--r--   0 runner    (1001) docker     (121)     6559 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/greengrass/core_definition_version.py
--rw-r--r--   0 runner    (1001) docker     (121)     7243 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/greengrass/device_definition.py
--rw-r--r--   0 runner    (1001) docker     (121)     6701 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/greengrass/device_definition_version.py
--rw-r--r--   0 runner    (1001) docker     (121)     7301 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/greengrass/function_definition.py
--rw-r--r--   0 runner    (1001) docker     (121)     8039 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/greengrass/function_definition_version.py
--rw-r--r--   0 runner    (1001) docker     (121)     8001 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/greengrass/group.py
--rw-r--r--   0 runner    (1001) docker     (121)    13454 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/greengrass/group_version.py
--rw-r--r--   0 runner    (1001) docker     (121)     7243 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/greengrass/logger_definition.py
--rw-r--r--   0 runner    (1001) docker     (121)     6701 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/greengrass/logger_definition_version.py
--rw-r--r--   0 runner    (1001) docker     (121)    78650 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/greengrass/outputs.py
--rw-r--r--   0 runner    (1001) docker     (121)     7301 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/greengrass/resource_definition.py
--rw-r--r--   0 runner    (1001) docker     (121)     6891 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/greengrass/resource_definition_version.py
--rw-r--r--   0 runner    (1001) docker     (121)     7417 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/greengrass/subscription_definition.py
--rw-r--r--   0 runner    (1001) docker     (121)     7127 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/greengrass/subscription_definition_version.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 14:35:49.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/greengrassv2/
--rw-r--r--   0 runner    (1001) docker     (121)      353 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/greengrassv2/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)      916 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/greengrassv2/_enums.py
--rw-r--r--   0 runner    (1001) docker     (121)    19747 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/greengrassv2/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)     7227 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/greengrassv2/component_version.py
--rw-r--r--   0 runner    (1001) docker     (121)    18649 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/greengrassv2/outputs.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 14:35:49.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/groundstation/
--rw-r--r--   0 runner    (1001) docker     (121)      412 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/groundstation/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)      827 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/groundstation/_enums.py
--rw-r--r--   0 runner    (1001) docker     (121)    29448 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/groundstation/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)     6625 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/groundstation/config.py
--rw-r--r--   0 runner    (1001) docker     (121)     6443 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/groundstation/dataflow_endpoint_group.py
--rw-r--r--   0 runner    (1001) docker     (121)    13896 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/groundstation/mission_profile.py
--rw-r--r--   0 runner    (1001) docker     (121)    29162 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/groundstation/outputs.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 14:35:49.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/guardduty/
--rw-r--r--   0 runner    (1001) docker     (121)      442 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/guardduty/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     4566 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/guardduty/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)     7180 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/guardduty/detector.py
--rw-r--r--   0 runner    (1001) docker     (121)     9194 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/guardduty/filter.py
--rw-r--r--   0 runner    (1001) docker     (121)     7983 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/guardduty/ip_set.py
--rw-r--r--   0 runner    (1001) docker     (121)     6037 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/guardduty/master.py
--rw-r--r--   0 runner    (1001) docker     (121)     8524 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/guardduty/member.py
--rw-r--r--   0 runner    (1001) docker     (121)     4380 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/guardduty/outputs.py
--rw-r--r--   0 runner    (1001) docker     (121)     8190 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/guardduty/threat_intel_set.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 14:35:49.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/healthlake/
--rw-r--r--   0 runner    (1001) docker     (121)      350 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/healthlake/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     1289 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/healthlake/_enums.py
--rw-r--r--   0 runner    (1001) docker     (121)     5261 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/healthlake/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    10619 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/healthlake/fhir_datastore.py
--rw-r--r--   0 runner    (1001) docker     (121)     7470 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/healthlake/outputs.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 14:35:49.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/iam/
--rw-r--r--   0 runner    (1001) docker     (121)      668 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/iam/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    14586 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/iam/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)     6673 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/iam/access_key.py
--rw-r--r--   0 runner    (1001) docker     (121)     7924 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/iam/group.py
--rw-r--r--   0 runner    (1001) docker     (121)     7023 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/iam/instance_profile.py
--rw-r--r--   0 runner    (1001) docker     (121)    10147 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/iam/managed_policy.py
--rw-r--r--   0 runner    (1001) docker     (121)     7711 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/iam/oidc_provider.py
--rw-r--r--   0 runner    (1001) docker     (121)    14514 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/iam/outputs.py
--rw-r--r--   0 runner    (1001) docker     (121)     8310 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/iam/policy.py
--rw-r--r--   0 runner    (1001) docker     (121)    17170 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/iam/role.py
--rw-r--r--   0 runner    (1001) docker     (121)     6690 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/iam/saml_provider.py
--rw-r--r--   0 runner    (1001) docker     (121)     9569 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/iam/server_certificate.py
--rw-r--r--   0 runner    (1001) docker     (121)     6959 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/iam/service_linked_role.py
--rw-r--r--   0 runner    (1001) docker     (121)    11745 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/iam/user.py
--rw-r--r--   0 runner    (1001) docker     (121)     6053 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/iam/user_to_group_addition.py
--rw-r--r--   0 runner    (1001) docker     (121)     7622 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/iam/virtual_mfa_device.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 14:35:49.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/imagebuilder/
--rw-r--r--   0 runner    (1001) docker     (121)      542 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/imagebuilder/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     3006 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/imagebuilder/_enums.py
--rw-r--r--   0 runner    (1001) docker     (121)    59017 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/imagebuilder/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    15758 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/imagebuilder/component.py
--rw-r--r--   0 runner    (1001) docker     (121)    26453 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/imagebuilder/container_recipe.py
--rw-r--r--   0 runner    (1001) docker     (121)     9115 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/imagebuilder/distribution_configuration.py
--rw-r--r--   0 runner    (1001) docker     (121)    15500 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/imagebuilder/image.py
--rw-r--r--   0 runner    (1001) docker     (121)    20043 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/imagebuilder/image_pipeline.py
--rw-r--r--   0 runner    (1001) docker     (121)    16441 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/imagebuilder/image_recipe.py
--rw-r--r--   0 runner    (1001) docker     (121)    22089 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/imagebuilder/infrastructure_configuration.py
--rw-r--r--   0 runner    (1001) docker     (121)    63466 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/imagebuilder/outputs.py
--rw-r--r--   0 runner    (1001) docker     (121)     1947 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/import_value.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 14:35:49.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/inspector/
--rw-r--r--   0 runner    (1001) docker     (121)      396 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/inspector/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     1774 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/inspector/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)     6486 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/inspector/assessment_target.py
--rw-r--r--   0 runner    (1001) docker     (121)    10378 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/inspector/assessment_template.py
--rw-r--r--   0 runner    (1001) docker     (121)     1244 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/inspector/outputs.py
--rw-r--r--   0 runner    (1001) docker     (121)     5744 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/inspector/resource_group.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 14:35:49.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/inspectorv2/
--rw-r--r--   0 runner    (1001) docker     (121)      342 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/inspectorv2/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)      539 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/inspectorv2/_enums.py
--rw-r--r--   0 runner    (1001) docker     (121)    28479 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/inspectorv2/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)     8489 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/inspectorv2/filter.py
--rw-r--r--   0 runner    (1001) docker     (121)    23568 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/inspectorv2/outputs.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 14:35:49.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/iot/
--rw-r--r--   0 runner    (1001) docker     (121)      951 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/iot/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     6607 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/iot/_enums.py
--rw-r--r--   0 runner    (1001) docker     (121)   138789 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/iot/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    10471 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/iot/account_audit_configuration.py
--rw-r--r--   0 runner    (1001) docker     (121)    10491 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/iot/authorizer.py
--rw-r--r--   0 runner    (1001) docker     (121)     8798 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/iot/certificate.py
--rw-r--r--   0 runner    (1001) docker     (121)    10572 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/iot/custom_metric.py
--rw-r--r--   0 runner    (1001) docker     (121)     9033 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/iot/dimension.py
--rw-r--r--   0 runner    (1001) docker     (121)    13460 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/iot/domain_configuration.py
--rw-r--r--   0 runner    (1001) docker     (121)    16917 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/iot/fleet_metric.py
--rw-r--r--   0 runner    (1001) docker     (121)    19655 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/iot/job_template.py
--rw-r--r--   0 runner    (1001) docker     (121)     8097 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/iot/logging.py
--rw-r--r--   0 runner    (1001) docker     (121)     9124 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/iot/mitigation_action.py
--rw-r--r--   0 runner    (1001) docker     (121)   141776 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/iot/outputs.py
--rw-r--r--   0 runner    (1001) docker     (121)     5948 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/iot/policy.py
--rw-r--r--   0 runner    (1001) docker     (121)     6148 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/iot/policy_principal_attachment.py
--rw-r--r--   0 runner    (1001) docker     (121)    10812 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/iot/provisioning_template.py
--rw-r--r--   0 runner    (1001) docker     (121)     8493 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/iot/resource_specific_logging.py
--rw-r--r--   0 runner    (1001) docker     (121)    13972 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/iot/scheduled_audit.py
--rw-r--r--   0 runner    (1001) docker     (121)    15489 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/iot/security_profile.py
--rw-r--r--   0 runner    (1001) docker     (121)     6014 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/iot/thing.py
--rw-r--r--   0 runner    (1001) docker     (121)     6106 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/iot/thing_principal_attachment.py
--rw-r--r--   0 runner    (1001) docker     (121)     6749 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/iot/topic_rule.py
--rw-r--r--   0 runner    (1001) docker     (121)     9032 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/iot/topic_rule_destination.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 14:35:49.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/iot1click/
--rw-r--r--   0 runner    (1001) docker     (121)      368 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/iot1click/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     1404 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/iot1click/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)     5245 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/iot1click/device.py
--rw-r--r--   0 runner    (1001) docker     (121)     1811 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/iot1click/outputs.py
--rw-r--r--   0 runner    (1001) docker     (121)     7546 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/iot1click/placement.py
--rw-r--r--   0 runner    (1001) docker     (121)     7199 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/iot1click/project.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 14:35:49.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/iotanalytics/
--rw-r--r--   0 runner    (1001) docker     (121)      415 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/iotanalytics/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)      351 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/iotanalytics/_enums.py
--rw-r--r--   0 runner    (1001) docker     (121)    62655 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/iotanalytics/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)     7599 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/iotanalytics/channel.py
--rw-r--r--   0 runner    (1001) docker     (121)    12585 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/iotanalytics/dataset.py
--rw-r--r--   0 runner    (1001) docker     (121)    10291 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/iotanalytics/datastore.py
--rw-r--r--   0 runner    (1001) docker     (121)    67810 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/iotanalytics/outputs.py
--rw-r--r--   0 runner    (1001) docker     (121)     6752 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/iotanalytics/pipeline.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 14:35:49.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/iotcoredeviceadvisor/
--rw-r--r--   0 runner    (1001) docker     (121)      330 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/iotcoredeviceadvisor/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     6082 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/iotcoredeviceadvisor/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)     6168 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/iotcoredeviceadvisor/outputs.py
--rw-r--r--   0 runner    (1001) docker     (121)     7905 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/iotcoredeviceadvisor/suite_definition.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 14:35:49.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/iotevents/
--rw-r--r--   0 runner    (1001) docker     (121)      371 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/iotevents/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)      443 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/iotevents/_enums.py
--rw-r--r--   0 runner    (1001) docker     (121)    65833 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/iotevents/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    17266 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/iotevents/detector_model.py
--rw-r--r--   0 runner    (1001) docker     (121)     9691 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/iotevents/input.py
--rw-r--r--   0 runner    (1001) docker     (121)    71022 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/iotevents/outputs.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 14:35:49.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/iotfleethub/
--rw-r--r--   0 runner    (1001) docker     (121)      325 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/iotfleethub/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     2291 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/iotfleethub/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    12895 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/iotfleethub/application.py
--rw-r--r--   0 runner    (1001) docker     (121)     2119 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/iotfleethub/outputs.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 14:35:49.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/iotsitewise/
--rw-r--r--   0 runner    (1001) docker     (121)      490 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/iotsitewise/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)      906 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/iotsitewise/_enums.py
--rw-r--r--   0 runner    (1001) docker     (121)    38909 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/iotsitewise/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)     9784 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/iotsitewise/access_policy.py
--rw-r--r--   0 runner    (1001) docker     (121)    10449 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/iotsitewise/asset.py
--rw-r--r--   0 runner    (1001) docker     (121)    15383 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/iotsitewise/asset_model.py
--rw-r--r--   0 runner    (1001) docker     (121)    10940 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/iotsitewise/dashboard.py
--rw-r--r--   0 runner    (1001) docker     (121)    10243 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/iotsitewise/gateway.py
--rw-r--r--   0 runner    (1001) docker     (121)    38600 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/iotsitewise/outputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    16755 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/iotsitewise/portal.py
--rw-r--r--   0 runner    (1001) docker     (121)    10626 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/iotsitewise/project.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 14:35:49.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/iotthingsgraph/
--rw-r--r--   0 runner    (1001) docker     (121)      327 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/iotthingsgraph/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     1108 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/iotthingsgraph/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)     6457 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/iotthingsgraph/flow_template.py
--rw-r--r--   0 runner    (1001) docker     (121)      831 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/iotthingsgraph/outputs.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 14:35:49.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/iotwireless/
--rw-r--r--   0 runner    (1001) docker     (121)      590 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/iotwireless/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)      914 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/iotwireless/_enums.py
--rw-r--r--   0 runner    (1001) docker     (121)    47400 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/iotwireless/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    11099 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/iotwireless/destination.py
--rw-r--r--   0 runner    (1001) docker     (121)     8259 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/iotwireless/device_profile.py
--rw-r--r--   0 runner    (1001) docker     (121)    17990 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/iotwireless/fuota_task.py
--rw-r--r--   0 runner    (1001) docker     (121)    12226 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/iotwireless/multicast_group.py
--rw-r--r--   0 runner    (1001) docker     (121)    48563 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/iotwireless/outputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    14649 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/iotwireless/partner_account.py
--rw-r--r--   0 runner    (1001) docker     (121)     8244 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/iotwireless/service_profile.py
--rw-r--r--   0 runner    (1001) docker     (121)    13597 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/iotwireless/task_definition.py
--rw-r--r--   0 runner    (1001) docker     (121)    15073 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/iotwireless/wireless_device.py
--rw-r--r--   0 runner    (1001) docker     (121)    12439 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/iotwireless/wireless_gateway.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 14:35:49.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ivs/
--rw-r--r--   0 runner    (1001) docker     (121)      441 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ivs/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)      855 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ivs/_enums.py
--rw-r--r--   0 runner    (1001) docker     (121)     4521 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ivs/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    12811 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ivs/channel.py
--rw-r--r--   0 runner    (1001) docker     (121)     3940 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ivs/outputs.py
--rw-r--r--   0 runner    (1001) docker     (121)     8622 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ivs/playback_key_pair.py
--rw-r--r--   0 runner    (1001) docker     (121)     8512 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ivs/recording_configuration.py
--rw-r--r--   0 runner    (1001) docker     (121)     6787 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ivs/stream_key.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 14:35:49.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/kendra/
--rw-r--r--   0 runner    (1001) docker     (121)      387 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/kendra/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     5112 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/kendra/_enums.py
--rw-r--r--   0 runner    (1001) docker     (121)   127018 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/kendra/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    11133 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/kendra/data_source.py
--rw-r--r--   0 runner    (1001) docker     (121)    11211 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/kendra/faq.py
--rw-r--r--   0 runner    (1001) docker     (121)    16589 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/kendra/index.py
--rw-r--r--   0 runner    (1001) docker     (121)   124925 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/kendra/outputs.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 14:35:49.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/kinesis/
--rw-r--r--   0 runner    (1001) docker     (121)      373 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/kinesis/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)      575 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/kinesis/_enums.py
--rw-r--r--   0 runner    (1001) docker     (121)     5235 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/kinesis/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)     6010 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/kinesis/outputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    12602 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/kinesis/stream.py
--rw-r--r--   0 runner    (1001) docker     (121)     6855 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/kinesis/stream_consumer.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 14:35:49.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/kinesisanalytics/
--rw-r--r--   0 runner    (1001) docker     (121)      417 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/kinesisanalytics/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    32531 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/kinesisanalytics/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)     8210 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/kinesisanalytics/application.py
--rw-r--r--   0 runner    (1001) docker     (121)     6480 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/kinesisanalytics/application_output_resource.py
--rw-r--r--   0 runner    (1001) docker     (121)     7054 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/kinesisanalytics/application_reference_data_source.py
--rw-r--r--   0 runner    (1001) docker     (121)    39541 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/kinesisanalytics/outputs.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 14:35:49.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/kinesisanalyticsv2/
--rw-r--r--   0 runner    (1001) docker     (121)      471 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/kinesisanalyticsv2/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    61368 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/kinesisanalyticsv2/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    11599 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/kinesisanalyticsv2/application.py
--rw-r--r--   0 runner    (1001) docker     (121)     7293 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/kinesisanalyticsv2/application_cloud_watch_logging_option.py
--rw-r--r--   0 runner    (1001) docker     (121)     6486 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/kinesisanalyticsv2/application_output_resource.py
--rw-r--r--   0 runner    (1001) docker     (121)     7060 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/kinesisanalyticsv2/application_reference_data_source.py
--rw-r--r--   0 runner    (1001) docker     (121)    73933 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/kinesisanalyticsv2/outputs.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 14:35:49.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/kinesisfirehose/
--rw-r--r--   0 runner    (1001) docker     (121)      351 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/kinesisfirehose/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     3442 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/kinesisfirehose/_enums.py
--rw-r--r--   0 runner    (1001) docker     (121)    90575 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/kinesisfirehose/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    22145 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/kinesisfirehose/delivery_stream.py
--rw-r--r--   0 runner    (1001) docker     (121)    91357 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/kinesisfirehose/outputs.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 14:35:49.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/kinesisvideo/
--rw-r--r--   0 runner    (1001) docker     (121)      375 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/kinesisvideo/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)      451 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/kinesisvideo/_enums.py
--rw-r--r--   0 runner    (1001) docker     (121)     4061 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/kinesisvideo/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)     3624 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/kinesisvideo/outputs.py
--rw-r--r--   0 runner    (1001) docker     (121)     9615 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/kinesisvideo/signaling_channel.py
--rw-r--r--   0 runner    (1001) docker     (121)    11788 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/kinesisvideo/stream.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 14:35:49.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/kms/
--rw-r--r--   0 runner    (1001) docker     (121)      387 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/kms/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     1086 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/kms/_enums.py
--rw-r--r--   0 runner    (1001) docker     (121)     4146 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/kms/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)     7705 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/kms/alias.py
--rw-r--r--   0 runner    (1001) docker     (121)    19125 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/kms/key.py
--rw-r--r--   0 runner    (1001) docker     (121)     3694 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/kms/outputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    13977 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/kms/replica_key.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 14:35:49.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/lakeformation/
--rw-r--r--   0 runner    (1001) docker     (121)      383 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/lakeformation/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    11344 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/lakeformation/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)     6439 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/lakeformation/data_lake_settings.py
--rw-r--r--   0 runner    (1001) docker     (121)    12841 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/lakeformation/outputs.py
--rw-r--r--   0 runner    (1001) docker     (121)     8686 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/lakeformation/permissions.py
--rw-r--r--   0 runner    (1001) docker     (121)     6910 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/lakeformation/resource.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 14:35:49.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/lambda_/
--rw-r--r--   0 runner    (1001) docker     (121)      608 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/lambda_/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     2138 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/lambda_/_enums.py
--rw-r--r--   0 runner    (1001) docker     (121)    34361 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/lambda_/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    10073 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/lambda_/alias.py
--rw-r--r--   0 runner    (1001) docker     (121)     9560 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/lambda_/code_signing_config.py
--rw-r--r--   0 runner    (1001) docker     (121)     9508 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/lambda_/event_invoke_config.py
--rw-r--r--   0 runner    (1001) docker     (121)    33870 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/lambda_/event_source_mapping.py
--rw-r--r--   0 runner    (1001) docker     (121)    36104 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/lambda_/function.py
--rw-r--r--   0 runner    (1001) docker     (121)    10024 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/lambda_/layer_version.py
--rw-r--r--   0 runner    (1001) docker     (121)     7902 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/lambda_/layer_version_permission.py
--rw-r--r--   0 runner    (1001) docker     (121)    38417 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/lambda_/outputs.py
--rw-r--r--   0 runner    (1001) docker     (121)     9352 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/lambda_/permission.py
--rw-r--r--   0 runner    (1001) docker     (121)    10192 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/lambda_/url.py
--rw-r--r--   0 runner    (1001) docker     (121)     8397 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/lambda_/version.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 14:35:49.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/lex/
--rw-r--r--   0 runner    (1001) docker     (121)      422 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/lex/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)      967 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/lex/_enums.py
--rw-r--r--   0 runner    (1001) docker     (121)    98707 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/lex/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    16710 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/lex/bot.py
--rw-r--r--   0 runner    (1001) docker     (121)    14259 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/lex/bot_alias.py
--rw-r--r--   0 runner    (1001) docker     (121)     7335 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/lex/bot_version.py
--rw-r--r--   0 runner    (1001) docker     (121)   108415 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/lex/outputs.py
--rw-r--r--   0 runner    (1001) docker     (121)     5849 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/lex/resource_policy.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 14:35:49.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/licensemanager/
--rw-r--r--   0 runner    (1001) docker     (121)      342 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/licensemanager/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     9053 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/licensemanager/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    10269 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/licensemanager/grant.py
--rw-r--r--   0 runner    (1001) docker     (121)    16436 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/licensemanager/license.py
--rw-r--r--   0 runner    (1001) docker     (121)     9507 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/licensemanager/outputs.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 14:35:49.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/lightsail/
--rw-r--r--   0 runner    (1001) docker     (121)      530 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/lightsail/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)      788 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/lightsail/_enums.py
--rw-r--r--   0 runner    (1001) docker     (121)    40687 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/lightsail/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    21321 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/lightsail/alarm.py
--rw-r--r--   0 runner    (1001) docker     (121)    14250 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/lightsail/bucket.py
--rw-r--r--   0 runner    (1001) docker     (121)    30830 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/lightsail/database.py
--rw-r--r--   0 runner    (1001) docker     (121)    13526 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/lightsail/disk.py
--rw-r--r--   0 runner    (1001) docker     (121)    21973 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/lightsail/instance.py
--rw-r--r--   0 runner    (1001) docker     (121)    16533 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/lightsail/load_balancer.py
--rw-r--r--   0 runner    (1001) docker     (121)    11938 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/lightsail/load_balancer_tls_certificate.py
--rw-r--r--   0 runner    (1001) docker     (121)    42739 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/lightsail/outputs.py
--rw-r--r--   0 runner    (1001) docker     (121)     6833 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/lightsail/static_ip.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 14:35:49.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/location/
--rw-r--r--   0 runner    (1001) docker     (121)      488 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/location/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     1571 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/location/_enums.py
--rw-r--r--   0 runner    (1001) docker     (121)     1442 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/location/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)     9485 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/location/geofence_collection.py
--rw-r--r--   0 runner    (1001) docker     (121)     8315 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/location/map.py
--rw-r--r--   0 runner    (1001) docker     (121)     1740 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/location/outputs.py
--rw-r--r--   0 runner    (1001) docker     (121)     9547 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/location/place_index.py
--rw-r--r--   0 runner    (1001) docker     (121)     8385 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/location/route_calculator.py
--rw-r--r--   0 runner    (1001) docker     (121)    10206 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/location/tracker.py
--rw-r--r--   0 runner    (1001) docker     (121)     5473 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/location/tracker_consumer.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 14:35:49.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/logs/
--rw-r--r--   0 runner    (1001) docker     (121)      503 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/logs/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     3998 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/logs/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)     7991 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/logs/destination.py
--rw-r--r--   0 runner    (1001) docker     (121)     9862 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/logs/log_group.py
--rw-r--r--   0 runner    (1001) docker     (121)     5939 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/logs/log_stream.py
--rw-r--r--   0 runner    (1001) docker     (121)     7567 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/logs/metric_filter.py
--rw-r--r--   0 runner    (1001) docker     (121)     3965 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/logs/outputs.py
--rw-r--r--   0 runner    (1001) docker     (121)     7769 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/logs/query_definition.py
--rw-r--r--   0 runner    (1001) docker     (121)     5974 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/logs/resource_policy.py
--rw-r--r--   0 runner    (1001) docker     (121)     7949 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/logs/subscription_filter.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 14:35:49.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/lookoutequipment/
--rw-r--r--   0 runner    (1001) docker     (121)      355 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/lookoutequipment/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)      496 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/lookoutequipment/_enums.py
--rw-r--r--   0 runner    (1001) docker     (121)     9515 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/lookoutequipment/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    20296 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/lookoutequipment/inference_scheduler.py
--rw-r--r--   0 runner    (1001) docker     (121)    10245 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/lookoutequipment/outputs.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 14:35:49.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/lookoutmetrics/
--rw-r--r--   0 runner    (1001) docker     (121)      373 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/lookoutmetrics/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     1182 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/lookoutmetrics/_enums.py
--rw-r--r--   0 runner    (1001) docker     (121)    35065 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/lookoutmetrics/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    10872 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/lookoutmetrics/alert.py
--rw-r--r--   0 runner    (1001) docker     (121)    11516 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/lookoutmetrics/anomaly_detector.py
--rw-r--r--   0 runner    (1001) docker     (121)    37159 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/lookoutmetrics/outputs.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 14:35:49.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/lookoutvision/
--rw-r--r--   0 runner    (1001) docker     (121)      276 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/lookoutvision/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     4833 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/lookoutvision/project.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 14:35:49.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/macie/
--rw-r--r--   0 runner    (1001) docker     (121)      412 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/macie/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)      822 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/macie/_enums.py
--rw-r--r--   0 runner    (1001) docker     (121)     1173 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/macie/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    10982 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/macie/custom_data_identifier.py
--rw-r--r--   0 runner    (1001) docker     (121)    10161 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/macie/findings_filter.py
--rw-r--r--   0 runner    (1001) docker     (121)     1799 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/macie/outputs.py
--rw-r--r--   0 runner    (1001) docker     (121)     7640 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/macie/session.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 14:35:49.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/managedblockchain/
--rw-r--r--   0 runner    (1001) docker     (121)      340 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/managedblockchain/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    11486 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/managedblockchain/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)     8537 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/managedblockchain/member.py
--rw-r--r--   0 runner    (1001) docker     (121)     7388 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/managedblockchain/node.py
--rw-r--r--   0 runner    (1001) docker     (121)    13285 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/managedblockchain/outputs.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 14:35:49.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/mediaconnect/
--rw-r--r--   0 runner    (1001) docker     (121)      460 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/mediaconnect/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     3324 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/mediaconnect/_enums.py
--rw-r--r--   0 runner    (1001) docker     (121)    40692 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/mediaconnect/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)     9724 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/mediaconnect/flow.py
--rw-r--r--   0 runner    (1001) docker     (121)    14171 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/mediaconnect/flow_entitlement.py
--rw-r--r--   0 runner    (1001) docker     (121)    23232 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/mediaconnect/flow_output.py
--rw-r--r--   0 runner    (1001) docker     (121)    21461 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/mediaconnect/flow_source.py
--rw-r--r--   0 runner    (1001) docker     (121)    10516 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/mediaconnect/flow_vpc_interface.py
--rw-r--r--   0 runner    (1001) docker     (121)    38390 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/mediaconnect/outputs.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 14:35:49.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/mediaconvert/
--rw-r--r--   0 runner    (1001) docker     (121)      369 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/mediaconvert/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     2159 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/mediaconvert/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    13279 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/mediaconvert/job_template.py
--rw-r--r--   0 runner    (1001) docker     (121)     2157 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/mediaconvert/outputs.py
--rw-r--r--   0 runner    (1001) docker     (121)     8011 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/mediaconvert/preset.py
--rw-r--r--   0 runner    (1001) docker     (121)     7982 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/mediaconvert/queue.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 14:35:49.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/medialive/
--rw-r--r--   0 runner    (1001) docker     (121)      378 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/medialive/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)   366723 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/medialive/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    15352 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/medialive/channel.py
--rw-r--r--   0 runner    (1001) docker     (121)    13856 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/medialive/input.py
--rw-r--r--   0 runner    (1001) docker     (121)     6537 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/medialive/input_security_group.py
--rw-r--r--   0 runner    (1001) docker     (121)   360164 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/medialive/outputs.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 14:35:49.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/mediapackage/
--rw-r--r--   0 runner    (1001) docker     (121)      465 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/mediapackage/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    11030 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/mediapackage/_enums.py
--rw-r--r--   0 runner    (1001) docker     (121)   105847 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/mediapackage/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    10938 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/mediapackage/asset.py
--rw-r--r--   0 runner    (1001) docker     (121)     9995 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/mediapackage/channel.py
--rw-r--r--   0 runner    (1001) docker     (121)    22306 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/mediapackage/origin_endpoint.py
--rw-r--r--   0 runner    (1001) docker     (121)   111244 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/mediapackage/outputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    13238 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/mediapackage/packaging_configuration.py
--rw-r--r--   0 runner    (1001) docker     (121)     8804 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/mediapackage/packaging_group.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 14:35:49.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/mediastore/
--rw-r--r--   0 runner    (1001) docker     (121)      323 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/mediastore/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     6148 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/mediastore/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    11191 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/mediastore/container.py
--rw-r--r--   0 runner    (1001) docker     (121)     6304 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/mediastore/outputs.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 14:35:49.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/memorydb/
--rw-r--r--   0 runner    (1001) docker     (121)      441 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/memorydb/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)      400 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/memorydb/_enums.py
--rw-r--r--   0 runner    (1001) docker     (121)    10291 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/memorydb/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)     7810 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/memorydb/acl.py
--rw-r--r--   0 runner    (1001) docker     (121)    42210 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/memorydb/cluster.py
--rw-r--r--   0 runner    (1001) docker     (121)     8410 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/memorydb/outputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    10686 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/memorydb/parameter_group.py
--rw-r--r--   0 runner    (1001) docker     (121)     9514 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/memorydb/subnet_group.py
--rw-r--r--   0 runner    (1001) docker     (121)     9104 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/memorydb/user.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 14:35:49.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/msk/
--rw-r--r--   0 runner    (1001) docker     (121)      321 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/msk/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    22665 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/msk/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    15614 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/msk/cluster.py
--rw-r--r--   0 runner    (1001) docker     (121)    24820 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/msk/outputs.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 14:35:49.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/mwaa/
--rw-r--r--   0 runner    (1001) docker     (121)      347 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/mwaa/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)      660 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/mwaa/_enums.py
--rw-r--r--   0 runner    (1001) docker     (121)     7221 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/mwaa/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    25370 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/mwaa/environment.py
--rw-r--r--   0 runner    (1001) docker     (121)     7733 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/mwaa/outputs.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 14:35:49.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/neptune/
--rw-r--r--   0 runner    (1001) docker     (121)      458 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/neptune/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     4844 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/neptune/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    27767 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/neptune/db_cluster.py
--rw-r--r--   0 runner    (1001) docker     (121)     8598 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/neptune/db_cluster_parameter_group.py
--rw-r--r--   0 runner    (1001) docker     (121)    16258 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/neptune/db_instance.py
--rw-r--r--   0 runner    (1001) docker     (121)     8395 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/neptune/db_parameter_group.py
--rw-r--r--   0 runner    (1001) docker     (121)     8449 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/neptune/db_subnet_group.py
--rw-r--r--   0 runner    (1001) docker     (121)     3833 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/neptune/outputs.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 14:35:49.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/networkfirewall/
--rw-r--r--   0 runner    (1001) docker     (121)      438 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/networkfirewall/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     2144 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/networkfirewall/_enums.py
--rw-r--r--   0 runner    (1001) docker     (121)    40623 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/networkfirewall/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    13463 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/networkfirewall/firewall.py
--rw-r--r--   0 runner    (1001) docker     (121)     8258 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/networkfirewall/firewall_policy.py
--rw-r--r--   0 runner    (1001) docker     (121)     6935 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/networkfirewall/logging_configuration.py
--rw-r--r--   0 runner    (1001) docker     (121)    42863 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/networkfirewall/outputs.py
--rw-r--r--   0 runner    (1001) docker     (121)     9472 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/networkfirewall/rule_group.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 14:35:49.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/networkmanager/
--rw-r--r--   0 runner    (1001) docker     (121)      510 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/networkmanager/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     8846 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/networkmanager/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)     8840 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/networkmanager/customer_gateway_association.py
--rw-r--r--   0 runner    (1001) docker     (121)    13969 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/networkmanager/device.py
--rw-r--r--   0 runner    (1001) docker     (121)     6527 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/networkmanager/global_network.py
--rw-r--r--   0 runner    (1001) docker     (121)    12011 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/networkmanager/link.py
--rw-r--r--   0 runner    (1001) docker     (121)     7268 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/networkmanager/link_association.py
--rw-r--r--   0 runner    (1001) docker     (121)     7398 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/networkmanager/outputs.py
--rw-r--r--   0 runner    (1001) docker     (121)     8933 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/networkmanager/site.py
--rw-r--r--   0 runner    (1001) docker     (121)     7054 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/networkmanager/transit_gateway_registration.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 14:35:49.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/nimblestudio/
--rw-r--r--   0 runner    (1001) docker     (121)      435 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/nimblestudio/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     2121 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/nimblestudio/_enums.py
--rw-r--r--   0 runner    (1001) docker     (121)    31493 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/nimblestudio/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    15571 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/nimblestudio/launch_profile.py
--rw-r--r--   0 runner    (1001) docker     (121)    33024 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/nimblestudio/outputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    11163 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/nimblestudio/streaming_image.py
--rw-r--r--   0 runner    (1001) docker     (121)    12894 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/nimblestudio/studio.py
--rw-r--r--   0 runner    (1001) docker     (121)    16549 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/nimblestudio/studio_component.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 14:35:49.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/opensearchservice/
--rw-r--r--   0 runner    (1001) docker     (121)      320 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/opensearchservice/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    20703 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/opensearchservice/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    21668 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/opensearchservice/domain.py
--rw-r--r--   0 runner    (1001) docker     (121)    25282 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/opensearchservice/outputs.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 14:35:49.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/opsworks/
--rw-r--r--   0 runner    (1001) docker     (121)      481 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/opsworks/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    34244 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/opsworks/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    14684 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/opsworks/app.py
--rw-r--r--   0 runner    (1001) docker     (121)     6551 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/opsworks/elastic_load_balancer_attachment.py
--rw-r--r--   0 runner    (1001) docker     (121)    24657 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/opsworks/instance.py
--rw-r--r--   0 runner    (1001) docker     (121)    23481 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/opsworks/layer.py
--rw-r--r--   0 runner    (1001) docker     (121)    31642 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/opsworks/outputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    28968 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/opsworks/stack.py
--rw-r--r--   0 runner    (1001) docker     (121)     7855 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/opsworks/user_profile.py
--rw-r--r--   0 runner    (1001) docker     (121)     7339 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/opsworks/volume.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 14:35:49.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/opsworkscm/
--rw-r--r--   0 runner    (1001) docker     (121)      320 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/opsworkscm/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     1909 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/opsworkscm/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)     1356 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/opsworkscm/outputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    24614 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/opsworkscm/server.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 14:35:49.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/panorama/
--rw-r--r--   0 runner    (1001) docker     (121)      410 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/panorama/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     1480 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/panorama/_enums.py
--rw-r--r--   0 runner    (1001) docker     (121)     3344 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/panorama/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    16593 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/panorama/application_instance.py
--rw-r--r--   0 runner    (1001) docker     (121)     6473 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/panorama/outputs.py
--rw-r--r--   0 runner    (1001) docker     (121)     6360 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/panorama/package.py
--rw-r--r--   0 runner    (1001) docker     (121)    10872 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/panorama/package_version.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 14:35:49.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/pinpoint/
--rw-r--r--   0 runner    (1001) docker     (121)      874 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/pinpoint/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)      737 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/pinpoint/_enums.py
--rw-r--r--   0 runner    (1001) docker     (121)    79028 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/pinpoint/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)     7604 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/pinpoint/adm_channel.py
--rw-r--r--   0 runner    (1001) docker     (121)    11981 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/pinpoint/apns_channel.py
--rw-r--r--   0 runner    (1001) docker     (121)    12142 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/pinpoint/apns_sandbox_channel.py
--rw-r--r--   0 runner    (1001) docker     (121)    12073 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/pinpoint/apns_voip_channel.py
--rw-r--r--   0 runner    (1001) docker     (121)    12234 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/pinpoint/apns_voip_sandbox_channel.py
--rw-r--r--   0 runner    (1001) docker     (121)     5484 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/pinpoint/app.py
--rw-r--r--   0 runner    (1001) docker     (121)     9594 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/pinpoint/application_settings.py
--rw-r--r--   0 runner    (1001) docker     (121)     7555 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/pinpoint/baidu_channel.py
--rw-r--r--   0 runner    (1001) docker     (121)    19507 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/pinpoint/campaign.py
--rw-r--r--   0 runner    (1001) docker     (121)     9346 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/pinpoint/email_channel.py
--rw-r--r--   0 runner    (1001) docker     (121)    10421 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/pinpoint/email_template.py
--rw-r--r--   0 runner    (1001) docker     (121)     7017 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/pinpoint/event_stream.py
--rw-r--r--   0 runner    (1001) docker     (121)     6631 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/pinpoint/gcm_channel.py
--rw-r--r--   0 runner    (1001) docker     (121)     9263 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/pinpoint/in_app_template.py
--rw-r--r--   0 runner    (1001) docker     (121)    76556 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/pinpoint/outputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    13258 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/pinpoint/push_template.py
--rw-r--r--   0 runner    (1001) docker     (121)     8812 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/pinpoint/segment.py
--rw-r--r--   0 runner    (1001) docker     (121)     7468 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/pinpoint/sms_channel.py
--rw-r--r--   0 runner    (1001) docker     (121)     8684 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/pinpoint/sms_template.py
--rw-r--r--   0 runner    (1001) docker     (121)     5856 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/pinpoint/voice_channel.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 14:35:49.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/pinpointemail/
--rw-r--r--   0 runner    (1001) docker     (121)      439 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/pinpointemail/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    15649 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/pinpointemail/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    10805 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/pinpointemail/configuration_set.py
--rw-r--r--   0 runner    (1001) docker     (121)     8180 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/pinpointemail/configuration_set_event_destination.py
--rw-r--r--   0 runner    (1001) docker     (121)     6116 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/pinpointemail/dedicated_ip_pool.py
--rw-r--r--   0 runner    (1001) docker     (121)    11118 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/pinpointemail/identity.py
--rw-r--r--   0 runner    (1001) docker     (121)    18780 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/pinpointemail/outputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    34730 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/provider.py
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/py.typed
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 14:35:49.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/qldb/
--rw-r--r--   0 runner    (1001) docker     (121)      342 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/qldb/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     4046 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/qldb/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)     8473 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/qldb/ledger.py
--rw-r--r--   0 runner    (1001) docker     (121)     3888 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/qldb/outputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    11019 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/qldb/stream.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 14:35:49.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/quicksight/
--rw-r--r--   0 runner    (1001) docker     (121)      465 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/quicksight/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     5667 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/quicksight/_enums.py
--rw-r--r--   0 runner    (1001) docker     (121)   138391 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/quicksight/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    18097 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/quicksight/analysis.py
--rw-r--r--   0 runner    (1001) docker     (121)    19728 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/quicksight/dashboard.py
--rw-r--r--   0 runner    (1001) docker     (121)    22131 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/quicksight/data_set.py
--rw-r--r--   0 runner    (1001) docker     (121)    23050 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/quicksight/data_source.py
--rw-r--r--   0 runner    (1001) docker     (121)   171641 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/quicksight/outputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    14689 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/quicksight/template.py
--rw-r--r--   0 runner    (1001) docker     (121)    16880 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/quicksight/theme.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 14:35:49.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ram/
--rw-r--r--   0 runner    (1001) docker     (121)      328 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ram/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     1048 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ram/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)      783 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ram/outputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    10222 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ram/resource_share.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 14:35:49.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/rds/
--rw-r--r--   0 runner    (1001) docker     (121)      740 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/rds/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     1825 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/rds/_enums.py
--rw-r--r--   0 runner    (1001) docker     (121)    27242 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/rds/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    41151 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/rds/db_cluster.py
--rw-r--r--   0 runner    (1001) docker     (121)     7880 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/rds/db_cluster_parameter_group.py
--rw-r--r--   0 runner    (1001) docker     (121)    58976 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/rds/db_instance.py
--rw-r--r--   0 runner    (1001) docker     (121)     7637 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/rds/db_parameter_group.py
--rw-r--r--   0 runner    (1001) docker     (121)    19405 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/rds/db_proxy.py
--rw-r--r--   0 runner    (1001) docker     (121)    15328 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/rds/db_proxy_endpoint.py
--rw-r--r--   0 runner    (1001) docker     (121)    11004 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/rds/db_proxy_target_group.py
--rw-r--r--   0 runner    (1001) docker     (121)     8602 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/rds/db_security_group.py
--rw-r--r--   0 runner    (1001) docker     (121)     9582 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/rds/db_security_group_ingress.py
--rw-r--r--   0 runner    (1001) docker     (121)     8437 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/rds/db_subnet_group.py
--rw-r--r--   0 runner    (1001) docker     (121)     8835 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/rds/event_subscription.py
--rw-r--r--   0 runner    (1001) docker     (121)    15039 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/rds/global_cluster.py
--rw-r--r--   0 runner    (1001) docker     (121)     9687 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/rds/option_group.py
--rw-r--r--   0 runner    (1001) docker     (121)    24668 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/rds/outputs.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 14:35:49.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/redshift/
--rw-r--r--   0 runner    (1001) docker     (121)      637 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/redshift/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     1499 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/redshift/_enums.py
--rw-r--r--   0 runner    (1001) docker     (121)    15066 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/redshift/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    89824 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/redshift/cluster.py
--rw-r--r--   0 runner    (1001) docker     (121)     8565 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/redshift/cluster_parameter_group.py
--rw-r--r--   0 runner    (1001) docker     (121)     6262 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/redshift/cluster_security_group.py
--rw-r--r--   0 runner    (1001) docker     (121)     8706 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/redshift/cluster_security_group_ingress.py
--rw-r--r--   0 runner    (1001) docker     (121)     7212 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/redshift/cluster_subnet_group.py
--rw-r--r--   0 runner    (1001) docker     (121)    13872 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/redshift/endpoint_access.py
--rw-r--r--   0 runner    (1001) docker     (121)    11872 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/redshift/endpoint_authorization.py
--rw-r--r--   0 runner    (1001) docker     (121)    18364 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/redshift/event_subscription.py
--rw-r--r--   0 runner    (1001) docker     (121)    23295 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/redshift/outputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    15319 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/redshift/scheduled_action.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 14:35:49.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/refactorspaces/
--rw-r--r--   0 runner    (1001) docker     (121)      418 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/refactorspaces/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     1056 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/refactorspaces/_enums.py
--rw-r--r--   0 runner    (1001) docker     (121)     9200 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/refactorspaces/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    11978 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/refactorspaces/application.py
--rw-r--r--   0 runner    (1001) docker     (121)     8794 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/refactorspaces/environment.py
--rw-r--r--   0 runner    (1001) docker     (121)     8761 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/refactorspaces/outputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    11131 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/refactorspaces/route.py
--rw-r--r--   0 runner    (1001) docker     (121)    13394 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/refactorspaces/service.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 14:35:49.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/rekognition/
--rw-r--r--   0 runner    (1001) docker     (121)      276 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/rekognition/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     4841 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/rekognition/project.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 14:35:49.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/resiliencehub/
--rw-r--r--   0 runner    (1001) docker     (121)      372 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/resiliencehub/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)      750 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/resiliencehub/_enums.py
--rw-r--r--   0 runner    (1001) docker     (121)     4578 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/resiliencehub/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    11107 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/resiliencehub/app.py
--rw-r--r--   0 runner    (1001) docker     (121)     4857 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/resiliencehub/outputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    11222 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/resiliencehub/resiliency_policy.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 14:35:49.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/resourcegroups/
--rw-r--r--   0 runner    (1001) docker     (121)      341 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/resourcegroups/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)      373 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/resourcegroups/_enums.py
--rw-r--r--   0 runner    (1001) docker     (121)     6958 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/resourcegroups/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)     9957 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/resourcegroups/group.py
--rw-r--r--   0 runner    (1001) docker     (121)     5392 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/resourcegroups/outputs.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 14:35:49.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/robomaker/
--rw-r--r--   0 runner    (1001) docker     (121)      520 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/robomaker/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     1971 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/robomaker/_enums.py
--rw-r--r--   0 runner    (1001) docker     (121)     9276 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/robomaker/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)     5602 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/robomaker/fleet.py
--rw-r--r--   0 runner    (1001) docker     (121)     8704 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/robomaker/outputs.py
--rw-r--r--   0 runner    (1001) docker     (121)     9188 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/robomaker/robot.py
--rw-r--r--   0 runner    (1001) docker     (121)     9297 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/robomaker/robot_application.py
--rw-r--r--   0 runner    (1001) docker     (121)     6502 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/robomaker/robot_application_version.py
--rw-r--r--   0 runner    (1001) docker     (121)    15738 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/robomaker/simulation_application.py
--rw-r--r--   0 runner    (1001) docker     (121)     6587 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/robomaker/simulation_application_version.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 14:35:49.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/route53/
--rw-r--r--   0 runner    (1001) docker     (121)      486 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/route53/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     1027 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/route53/_enums.py
--rw-r--r--   0 runner    (1001) docker     (121)    29555 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/route53/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)     4855 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/route53/dnssec.py
--rw-r--r--   0 runner    (1001) docker     (121)     7384 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/route53/health_check.py
--rw-r--r--   0 runner    (1001) docker     (121)    13671 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/route53/hosted_zone.py
--rw-r--r--   0 runner    (1001) docker     (121)    10126 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/route53/key_signing_key.py
--rw-r--r--   0 runner    (1001) docker     (121)    28244 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/route53/outputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    17135 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/route53/record_set.py
--rw-r--r--   0 runner    (1001) docker     (121)     8035 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/route53/record_set_group.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 14:35:49.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/route53recoverycontrol/
--rw-r--r--   0 runner    (1001) docker     (121)      430 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/route53recoverycontrol/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     1559 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/route53recoverycontrol/_enums.py
--rw-r--r--   0 runner    (1001) docker     (121)    11024 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/route53recoverycontrol/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)     7175 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/route53recoverycontrol/cluster.py
--rw-r--r--   0 runner    (1001) docker     (121)     9254 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/route53recoverycontrol/control_panel.py
--rw-r--r--   0 runner    (1001) docker     (121)    11506 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/route53recoverycontrol/outputs.py
--rw-r--r--   0 runner    (1001) docker     (121)     8124 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/route53recoverycontrol/routing_control.py
--rw-r--r--   0 runner    (1001) docker     (121)    11069 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/route53recoverycontrol/safety_rule.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 14:35:49.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/route53recoveryreadiness/
--rw-r--r--   0 runner    (1001) docker     (121)      407 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/route53recoveryreadiness/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    13774 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/route53recoveryreadiness/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)     8460 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/route53recoveryreadiness/cell.py
--rw-r--r--   0 runner    (1001) docker     (121)    13339 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/route53recoveryreadiness/outputs.py
--rw-r--r--   0 runner    (1001) docker     (121)     8153 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/route53recoveryreadiness/readiness_check.py
--rw-r--r--   0 runner    (1001) docker     (121)     8175 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/route53recoveryreadiness/recovery_group.py
--rw-r--r--   0 runner    (1001) docker     (121)    11957 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/route53recoveryreadiness/resource_set.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 14:35:49.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/route53resolver/
--rw-r--r--   0 runner    (1001) docker     (121)      712 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/route53resolver/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     5158 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/route53resolver/_enums.py
--rw-r--r--   0 runner    (1001) docker     (121)    15611 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/route53resolver/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    10726 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/route53resolver/firewall_domain_list.py
--rw-r--r--   0 runner    (1001) docker     (121)    10503 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/route53resolver/firewall_rule_group.py
--rw-r--r--   0 runner    (1001) docker     (121)    13570 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/route53resolver/firewall_rule_group_association.py
--rw-r--r--   0 runner    (1001) docker     (121)    14012 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/route53resolver/outputs.py
--rw-r--r--   0 runner    (1001) docker     (121)     7845 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/route53resolver/resolver_config.py
--rw-r--r--   0 runner    (1001) docker     (121)     5559 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/route53resolver/resolver_dnssec_config.py
--rw-r--r--   0 runner    (1001) docker     (121)    10313 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/route53resolver/resolver_endpoint.py
--rw-r--r--   0 runner    (1001) docker     (121)     8263 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/route53resolver/resolver_query_logging_config.py
--rw-r--r--   0 runner    (1001) docker     (121)     7903 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/route53resolver/resolver_query_logging_config_association.py
--rw-r--r--   0 runner    (1001) docker     (121)    14237 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/route53resolver/resolver_rule.py
--rw-r--r--   0 runner    (1001) docker     (121)     8054 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/route53resolver/resolver_rule_association.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 14:35:49.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/rum/
--rw-r--r--   0 runner    (1001) docker     (121)      347 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/rum/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)      345 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/rum/_enums.py
--rw-r--r--   0 runner    (1001) docker     (121)    11315 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/rum/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    10462 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/rum/app_monitor.py
--rw-r--r--   0 runner    (1001) docker     (121)    10301 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/rum/outputs.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 14:35:49.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/s3/
--rw-r--r--   0 runner    (1001) docker     (121)      516 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/s3/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     8282 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/s3/_enums.py
--rw-r--r--   0 runner    (1001) docker     (121)   141353 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/s3/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    14416 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/s3/access_point.py
--rw-r--r--   0 runner    (1001) docker     (121)    39434 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/s3/bucket.py
--rw-r--r--   0 runner    (1001) docker     (121)     5801 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/s3/bucket_policy.py
--rw-r--r--   0 runner    (1001) docker     (121)    11380 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/s3/multi_region_access_point.py
--rw-r--r--   0 runner    (1001) docker     (121)     6572 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/s3/multi_region_access_point_policy.py
--rw-r--r--   0 runner    (1001) docker     (121)   147485 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/s3/outputs.py
--rw-r--r--   0 runner    (1001) docker     (121)     6674 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/s3/storage_lens.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 14:35:49.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/s3objectlambda/
--rw-r--r--   0 runner    (1001) docker     (121)      361 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/s3objectlambda/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     4335 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/s3objectlambda/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)     8892 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/s3objectlambda/access_point.py
--rw-r--r--   0 runner    (1001) docker     (121)     7746 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/s3objectlambda/access_point_policy.py
--rw-r--r--   0 runner    (1001) docker     (121)    13130 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/s3objectlambda/outputs.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 14:35:49.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/s3outposts/
--rw-r--r--   0 runner    (1001) docker     (121)      423 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/s3outposts/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)      811 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/s3outposts/_enums.py
--rw-r--r--   0 runner    (1001) docker     (121)    11970 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/s3outposts/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)     8960 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/s3outposts/access_point.py
--rw-r--r--   0 runner    (1001) docker     (121)     9537 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/s3outposts/bucket.py
--rw-r--r--   0 runner    (1001) docker     (121)     6067 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/s3outposts/bucket_policy.py
--rw-r--r--   0 runner    (1001) docker     (121)    12847 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/s3outposts/endpoint.py
--rw-r--r--   0 runner    (1001) docker     (121)    13452 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/s3outposts/outputs.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 14:35:49.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/sagemaker/
--rw-r--r--   0 runner    (1001) docker     (121)     1060 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/sagemaker/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    12570 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/sagemaker/_enums.py
--rw-r--r--   0 runner    (1001) docker     (121)   278376 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/sagemaker/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    11221 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/sagemaker/app.py
--rw-r--r--   0 runner    (1001) docker     (121)     8661 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/sagemaker/app_image_config.py
--rw-r--r--   0 runner    (1001) docker     (121)     7322 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/sagemaker/code_repository.py
--rw-r--r--   0 runner    (1001) docker     (121)    18433 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/sagemaker/data_quality_job_definition.py
--rw-r--r--   0 runner    (1001) docker     (121)     7417 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/sagemaker/device.py
--rw-r--r--   0 runner    (1001) docker     (121)    10186 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/sagemaker/device_fleet.py
--rw-r--r--   0 runner    (1001) docker     (121)    16764 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/sagemaker/domain.py
--rw-r--r--   0 runner    (1001) docker     (121)    12068 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/sagemaker/endpoint.py
--rw-r--r--   0 runner    (1001) docker     (121)    11063 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/sagemaker/endpoint_config.py
--rw-r--r--   0 runner    (1001) docker     (121)    15772 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/sagemaker/feature_group.py
--rw-r--r--   0 runner    (1001) docker     (121)     8858 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/sagemaker/image.py
--rw-r--r--   0 runner    (1001) docker     (121)     6353 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/sagemaker/image_version.py
--rw-r--r--   0 runner    (1001) docker     (121)    12567 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/sagemaker/model.py
--rw-r--r--   0 runner    (1001) docker     (121)    18109 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/sagemaker/model_bias_job_definition.py
--rw-r--r--   0 runner    (1001) docker     (121)    19729 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/sagemaker/model_explainability_job_definition.py
--rw-r--r--   0 runner    (1001) docker     (121)     9671 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/sagemaker/model_package_group.py
--rw-r--r--   0 runner    (1001) docker     (121)    18595 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/sagemaker/model_quality_job_definition.py
--rw-r--r--   0 runner    (1001) docker     (121)    14819 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/sagemaker/monitoring_schedule.py
--rw-r--r--   0 runner    (1001) docker     (121)    19239 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/sagemaker/notebook_instance.py
--rw-r--r--   0 runner    (1001) docker     (121)     8716 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/sagemaker/notebook_instance_lifecycle_config.py
--rw-r--r--   0 runner    (1001) docker     (121)   310639 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/sagemaker/outputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    10339 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/sagemaker/pipeline.py
--rw-r--r--   0 runner    (1001) docker     (121)    10701 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/sagemaker/project.py
--rw-r--r--   0 runner    (1001) docker     (121)    13902 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/sagemaker/user_profile.py
--rw-r--r--   0 runner    (1001) docker     (121)     9481 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/sagemaker/workteam.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 14:35:49.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/sdb/
--rw-r--r--   0 runner    (1001) docker     (121)      275 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/sdb/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     4824 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/sdb/domain.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 14:35:49.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/secretsmanager/
--rw-r--r--   0 runner    (1001) docker     (121)      424 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/secretsmanager/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    12914 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/secretsmanager/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    12515 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/secretsmanager/outputs.py
--rw-r--r--   0 runner    (1001) docker     (121)     6972 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/secretsmanager/resource_policy.py
--rw-r--r--   0 runner    (1001) docker     (121)     8622 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/secretsmanager/rotation_schedule.py
--rw-r--r--   0 runner    (1001) docker     (121)    10780 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/secretsmanager/secret.py
--rw-r--r--   0 runner    (1001) docker     (121)     7005 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/secretsmanager/secret_target_attachment.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 14:35:49.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/securityhub/
--rw-r--r--   0 runner    (1001) docker     (121)      272 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/securityhub/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     4597 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/securityhub/hub.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 14:35:49.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/servicecatalog/
--rw-r--r--   0 runner    (1001) docker     (121)      938 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/servicecatalog/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)      862 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/servicecatalog/_enums.py
--rw-r--r--   0 runner    (1001) docker     (121)    10886 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/servicecatalog/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)     6234 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/servicecatalog/accepted_portfolio_share.py
--rw-r--r--   0 runner    (1001) docker     (121)    16111 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/servicecatalog/cloud_formation_product.py
--rw-r--r--   0 runner    (1001) docker     (121)    18259 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/servicecatalog/cloud_formation_provisioned_product.py
--rw-r--r--   0 runner    (1001) docker     (121)     9209 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/servicecatalog/launch_notification_constraint.py
--rw-r--r--   0 runner    (1001) docker     (121)     9612 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/servicecatalog/launch_role_constraint.py
--rw-r--r--   0 runner    (1001) docker     (121)     8733 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/servicecatalog/launch_template_constraint.py
--rw-r--r--   0 runner    (1001) docker     (121)     9305 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/servicecatalog/outputs.py
--rw-r--r--   0 runner    (1001) docker     (121)     8965 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/servicecatalog/portfolio.py
--rw-r--r--   0 runner    (1001) docker     (121)     8284 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/servicecatalog/portfolio_principal_association.py
--rw-r--r--   0 runner    (1001) docker     (121)     8225 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/servicecatalog/portfolio_product_association.py
--rw-r--r--   0 runner    (1001) docker     (121)     7896 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/servicecatalog/portfolio_share.py
--rw-r--r--   0 runner    (1001) docker     (121)     9285 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/servicecatalog/resource_update_constraint.py
--rw-r--r--   0 runner    (1001) docker     (121)     8621 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/servicecatalog/service_action.py
--rw-r--r--   0 runner    (1001) docker     (121)     6843 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/servicecatalog/service_action_association.py
--rw-r--r--   0 runner    (1001) docker     (121)    12888 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/servicecatalog/stack_set_constraint.py
--rw-r--r--   0 runner    (1001) docker     (121)     6315 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/servicecatalog/tag_option.py
--rw-r--r--   0 runner    (1001) docker     (121)     6174 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/servicecatalog/tag_option_association.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 14:35:49.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/servicecatalogappregistry/
--rw-r--r--   0 runner    (1001) docker     (121)      457 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/servicecatalogappregistry/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)      403 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/servicecatalogappregistry/_enums.py
--rw-r--r--   0 runner    (1001) docker     (121)      592 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/servicecatalogappregistry/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)     6796 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/servicecatalogappregistry/application.py
--rw-r--r--   0 runner    (1001) docker     (121)     7660 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/servicecatalogappregistry/attribute_group.py
--rw-r--r--   0 runner    (1001) docker     (121)     6905 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/servicecatalogappregistry/attribute_group_association.py
--rw-r--r--   0 runner    (1001) docker     (121)      590 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/servicecatalogappregistry/outputs.py
--rw-r--r--   0 runner    (1001) docker     (121)     8141 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/servicecatalogappregistry/resource_association.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 14:35:49.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/servicediscovery/
--rw-r--r--   0 runner    (1001) docker     (121)      448 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/servicediscovery/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    11391 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/servicediscovery/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)     6955 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/servicediscovery/http_namespace.py
--rw-r--r--   0 runner    (1001) docker     (121)     6182 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/servicediscovery/instance.py
--rw-r--r--   0 runner    (1001) docker     (121)    14043 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/servicediscovery/outputs.py
--rw-r--r--   0 runner    (1001) docker     (121)     8869 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/servicediscovery/private_dns_namespace.py
--rw-r--r--   0 runner    (1001) docker     (121)     8128 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/servicediscovery/public_dns_namespace.py
--rw-r--r--   0 runner    (1001) docker     (121)    11923 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/servicediscovery/service.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 14:35:49.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ses/
--rw-r--r--   0 runner    (1001) docker     (121)      524 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ses/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    29409 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ses/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)     4636 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ses/configuration_set.py
--rw-r--r--   0 runner    (1001) docker     (121)     7093 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ses/configuration_set_event_destination.py
--rw-r--r--   0 runner    (1001) docker     (121)     8886 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ses/contact_list.py
--rw-r--r--   0 runner    (1001) docker     (121)    31210 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ses/outputs.py
--rw-r--r--   0 runner    (1001) docker     (121)     5141 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ses/receipt_filter.py
--rw-r--r--   0 runner    (1001) docker     (121)     6692 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ses/receipt_rule.py
--rw-r--r--   0 runner    (1001) docker     (121)     5080 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ses/receipt_rule_set.py
--rw-r--r--   0 runner    (1001) docker     (121)     5009 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ses/template.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 14:35:49.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/signer/
--rw-r--r--   0 runner    (1001) docker     (121)      385 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/signer/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)      509 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/signer/_enums.py
--rw-r--r--   0 runner    (1001) docker     (121)     2239 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/signer/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)     1626 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/signer/outputs.py
--rw-r--r--   0 runner    (1001) docker     (121)     8084 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/signer/profile_permission.py
--rw-r--r--   0 runner    (1001) docker     (121)     9975 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/signer/signing_profile.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 14:35:49.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/sns/
--rw-r--r--   0 runner    (1001) docker     (121)      375 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/sns/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     1814 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/sns/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)     1260 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/sns/outputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    11878 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/sns/subscription.py
--rw-r--r--   0 runner    (1001) docker     (121)    10758 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/sns/topic.py
--rw-r--r--   0 runner    (1001) docker     (121)     5911 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/sns/topic_policy.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 14:35:49.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/sqs/
--rw-r--r--   0 runner    (1001) docker     (121)      347 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/sqs/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     1032 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/sqs/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)      767 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/sqs/outputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    19248 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/sqs/queue.py
--rw-r--r--   0 runner    (1001) docker     (121)     7745 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/sqs/queue_policy.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 14:35:49.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ssm/
--rw-r--r--   0 runner    (1001) docker     (121)      574 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ssm/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     1725 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ssm/_enums.py
--rw-r--r--   0 runner    (1001) docker     (121)    39156 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ssm/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    23030 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ssm/association.py
--rw-r--r--   0 runner    (1001) docker     (121)    17501 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ssm/document.py
--rw-r--r--   0 runner    (1001) docker     (121)    13923 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ssm/maintenance_window.py
--rw-r--r--   0 runner    (1001) docker     (121)     9866 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ssm/maintenance_window_target.py
--rw-r--r--   0 runner    (1001) docker     (121)    17445 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ssm/maintenance_window_task.py
--rw-r--r--   0 runner    (1001) docker     (121)    37739 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ssm/outputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    10939 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ssm/parameter.py
--rw-r--r--   0 runner    (1001) docker     (121)    17770 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ssm/patch_baseline.py
--rw-r--r--   0 runner    (1001) docker     (121)    11348 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ssm/resource_data_sync.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 14:35:49.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ssmcontacts/
--rw-r--r--   0 runner    (1001) docker     (121)      374 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ssmcontacts/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)      776 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ssmcontacts/_enums.py
--rw-r--r--   0 runner    (1001) docker     (121)     6522 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ssmcontacts/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)     9925 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ssmcontacts/contact.py
--rw-r--r--   0 runner    (1001) docker     (121)    11451 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ssmcontacts/contact_channel.py
--rw-r--r--   0 runner    (1001) docker     (121)     7998 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ssmcontacts/outputs.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 14:35:49.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ssmincidents/
--rw-r--r--   0 runner    (1001) docker     (121)      380 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ssmincidents/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)      504 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ssmincidents/_enums.py
--rw-r--r--   0 runner    (1001) docker     (121)    13071 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ssmincidents/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    14618 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ssmincidents/outputs.py
--rw-r--r--   0 runner    (1001) docker     (121)     6515 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ssmincidents/replication_set.py
--rw-r--r--   0 runner    (1001) docker     (121)    12442 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ssmincidents/response_plan.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 14:35:49.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/sso/
--rw-r--r--   0 runner    (1001) docker     (121)      439 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/sso/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)      555 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/sso/_enums.py
--rw-r--r--   0 runner    (1001) docker     (121)     4035 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/sso/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    11511 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/sso/assignment.py
--rw-r--r--   0 runner    (1001) docker     (121)    10311 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/sso/instance_access_control_attribute_configuration.py
--rw-r--r--   0 runner    (1001) docker     (121)     4007 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/sso/outputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    13467 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/sso/permission_set.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 14:35:49.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/stepfunctions/
--rw-r--r--   0 runner    (1001) docker     (121)      373 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/stepfunctions/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)      492 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/stepfunctions/_enums.py
--rw-r--r--   0 runner    (1001) docker     (121)     7030 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/stepfunctions/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)     5421 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/stepfunctions/activity.py
--rw-r--r--   0 runner    (1001) docker     (121)     6809 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/stepfunctions/outputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    15052 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/stepfunctions/state_machine.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 14:35:49.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/synthetics/
--rw-r--r--   0 runner    (1001) docker     (121)      320 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/synthetics/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    15548 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/synthetics/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    22631 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/synthetics/canary.py
--rw-r--r--   0 runner    (1001) docker     (121)    16825 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/synthetics/outputs.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 14:35:49.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/timestream/
--rw-r--r--   0 runner    (1001) docker     (121)      396 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/timestream/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     1354 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/timestream/_enums.py
--rw-r--r--   0 runner    (1001) docker     (121)    22951 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/timestream/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)     8462 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/timestream/database.py
--rw-r--r--   0 runner    (1001) docker     (121)    27061 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/timestream/outputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    19901 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/timestream/scheduled_query.py
--rw-r--r--   0 runner    (1001) docker     (121)    10098 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/timestream/table.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 14:35:49.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/transfer/
--rw-r--r--   0 runner    (1001) docker     (121)      386 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/transfer/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)      647 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/transfer/_enums.py
--rw-r--r--   0 runner    (1001) docker     (121)    26737 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/transfer/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    26607 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/transfer/outputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    16631 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/transfer/server.py
--rw-r--r--   0 runner    (1001) docker     (121)    13858 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/transfer/user.py
--rw-r--r--   0 runner    (1001) docker     (121)    10485 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/transfer/workflow.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 14:35:49.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/waf/
--rw-r--r--   0 runner    (1001) docker     (121)      496 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/waf/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    13594 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/waf/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)     6191 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/waf/byte_match_set.py
--rw-r--r--   0 runner    (1001) docker     (121)     5998 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/waf/ip_set.py
--rw-r--r--   0 runner    (1001) docker     (121)    13226 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/waf/outputs.py
--rw-r--r--   0 runner    (1001) docker     (121)     6649 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/waf/rule.py
--rw-r--r--   0 runner    (1001) docker     (121)     6349 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/waf/size_constraint_set.py
--rw-r--r--   0 runner    (1001) docker     (121)     6631 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/waf/sql_injection_match_set.py
--rw-r--r--   0 runner    (1001) docker     (121)     7753 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/waf/web_acl.py
--rw-r--r--   0 runner    (1001) docker     (121)     6167 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/waf/xss_match_set.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 14:35:49.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/wafregional/
--rw-r--r--   0 runner    (1001) docker     (121)      623 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/wafregional/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    15337 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/wafregional/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)     6215 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/wafregional/byte_match_set.py
--rw-r--r--   0 runner    (1001) docker     (121)     6282 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/wafregional/geo_match_set.py
--rw-r--r--   0 runner    (1001) docker     (121)     6022 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/wafregional/ip_set.py
--rw-r--r--   0 runner    (1001) docker     (121)    14849 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/wafregional/outputs.py
--rw-r--r--   0 runner    (1001) docker     (121)     8796 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/wafregional/rate_based_rule.py
--rw-r--r--   0 runner    (1001) docker     (121)     6131 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/wafregional/regex_pattern_set.py
--rw-r--r--   0 runner    (1001) docker     (121)     6673 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/wafregional/rule.py
--rw-r--r--   0 runner    (1001) docker     (121)     6344 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/wafregional/size_constraint_set.py
--rw-r--r--   0 runner    (1001) docker     (121)     6655 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/wafregional/sql_injection_match_set.py
--rw-r--r--   0 runner    (1001) docker     (121)     7705 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/wafregional/web_acl.py
--rw-r--r--   0 runner    (1001) docker     (121)     6058 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/wafregional/web_aclassociation.py
--rw-r--r--   0 runner    (1001) docker     (121)     6162 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/wafregional/xss_match_set.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 14:35:49.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/wafv2/
--rw-r--r--   0 runner    (1001) docker     (121)      495 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/wafv2/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     8780 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/wafv2/_enums.py
--rw-r--r--   0 runner    (1001) docker     (121)   145232 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/wafv2/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)     9482 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/wafv2/ip_set.py
--rw-r--r--   0 runner    (1001) docker     (121)    12135 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/wafv2/logging_configuration.py
--rw-r--r--   0 runner    (1001) docker     (121)   149784 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/wafv2/outputs.py
--rw-r--r--   0 runner    (1001) docker     (121)     9998 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/wafv2/regex_pattern_set.py
--rw-r--r--   0 runner    (1001) docker     (121)    13802 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/wafv2/rule_group.py
--rw-r--r--   0 runner    (1001) docker     (121)    14501 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/wafv2/web_acl.py
--rw-r--r--   0 runner    (1001) docker     (121)     5515 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/wafv2/web_aclassociation.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 14:35:49.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/wisdom/
--rw-r--r--   0 runner    (1001) docker     (121)      412 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/wisdom/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)      529 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/wisdom/_enums.py
--rw-r--r--   0 runner    (1001) docker     (121)     6771 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/wisdom/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)     9009 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/wisdom/assistant.py
--rw-r--r--   0 runner    (1001) docker     (121)     8964 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/wisdom/assistant_association.py
--rw-r--r--   0 runner    (1001) docker     (121)    12120 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/wisdom/knowledge_base.py
--rw-r--r--   0 runner    (1001) docker     (121)     8652 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/wisdom/outputs.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 14:35:49.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/workspaces/
--rw-r--r--   0 runner    (1001) docker     (121)      377 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/workspaces/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)      744 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/workspaces/_enums.py
--rw-r--r--   0 runner    (1001) docker     (121)     4716 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/workspaces/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)     6568 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/workspaces/connection_alias.py
--rw-r--r--   0 runner    (1001) docker     (121)     6594 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/workspaces/outputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    12348 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/workspaces/workspace.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 14:35:49.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/xray/
--rw-r--r--   0 runner    (1001) docker     (121)      348 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/xray/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    20512 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/xray/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)     8835 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/xray/group.py
--rw-r--r--   0 runner    (1001) docker     (121)    18816 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/xray/outputs.py
--rw-r--r--   0 runner    (1001) docker     (121)     9208 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/xray/sampling_rule.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native.egg-info/
--rw-r--r--   0 runner    (1001) docker     (121)     3304 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (121)    66269 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (121)        1 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (121)        1 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native.egg-info/not-zip-safe
--rw-r--r--   0 runner    (1001) docker     (121)       49 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (121)       18 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native.egg-info/top_level.txt
--rw-r--r--   0 runner    (1001) docker     (121)       38 2022-01-10 14:35:49.000000 pulumi_aws_native-0.9.1a1641824984/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (121)     2156 2022-01-10 14:35:48.000000 pulumi_aws_native-0.9.1a1641824984/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 15:05:10.000000 pulumi_aws_native-0.9.1a1641826769/
+-rw-r--r--   0 runner    (1001) docker     (121)     3304 2022-01-10 15:05:10.000000 pulumi_aws_native-0.9.1a1641826769/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (121)     2414 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/README.md
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 15:05:10.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/
+-rw-r--r--   0 runner    (1001) docker     (121)   101207 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2123 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/_enums.py
+-rw-r--r--   0 runner    (1001) docker     (121)   107777 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7560 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/_utilities.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 15:05:10.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/accessanalyzer/
+-rw-r--r--   0 runner    (1001) docker     (121)      322 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/accessanalyzer/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     5629 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/accessanalyzer/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)     8728 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/accessanalyzer/analyzer.py
+-rw-r--r--   0 runner    (1001) docker     (121)     4920 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/accessanalyzer/outputs.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 15:05:10.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/acmpca/
+-rw-r--r--   0 runner    (1001) docker     (121)      436 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/acmpca/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    54885 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/acmpca/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    15662 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/acmpca/certificate.py
+-rw-r--r--   0 runner    (1001) docker     (121)    16814 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/acmpca/certificate_authority.py
+-rw-r--r--   0 runner    (1001) docker     (121)     9680 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/acmpca/certificate_authority_activation.py
+-rw-r--r--   0 runner    (1001) docker     (121)    56255 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/acmpca/outputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)     9591 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/acmpca/permission.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 15:05:10.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/amazonmq/
+-rw-r--r--   0 runner    (1001) docker     (121)      390 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/amazonmq/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    13282 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/amazonmq/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    25043 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/amazonmq/broker.py
+-rw-r--r--   0 runner    (1001) docker     (121)    10833 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/amazonmq/configuration.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6422 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/amazonmq/configuration_association.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11805 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/amazonmq/outputs.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 15:05:10.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/amplify/
+-rw-r--r--   0 runner    (1001) docker     (121)      383 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/amplify/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)      646 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/amplify/_enums.py
+-rw-r--r--   0 runner    (1001) docker     (121)    14363 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/amplify/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    18352 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/amplify/app.py
+-rw-r--r--   0 runner    (1001) docker     (121)    15696 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/amplify/branch.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11123 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/amplify/domain.py
+-rw-r--r--   0 runner    (1001) docker     (121)    12515 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/amplify/outputs.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 15:05:10.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/amplifyuibuilder/
+-rw-r--r--   0 runner    (1001) docker     (121)      344 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/amplifyuibuilder/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6010 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/amplifyuibuilder/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    14376 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/amplifyuibuilder/component.py
+-rw-r--r--   0 runner    (1001) docker     (121)     5485 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/amplifyuibuilder/outputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)     8101 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/amplifyuibuilder/theme.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 15:05:10.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/apigateway/
+-rw-r--r--   0 runner    (1001) docker     (121)      840 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/apigateway/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1938 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/apigateway/_enums.py
+-rw-r--r--   0 runner    (1001) docker     (121)    87809 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/apigateway/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)     5118 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/apigateway/account.py
+-rw-r--r--   0 runner    (1001) docker     (121)    14915 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/apigateway/api_key.py
+-rw-r--r--   0 runner    (1001) docker     (121)    17466 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/apigateway/authorizer.py
+-rw-r--r--   0 runner    (1001) docker     (121)     8338 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/apigateway/base_path_mapping.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6915 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/apigateway/client_certificate.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11220 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/apigateway/deployment.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7061 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/apigateway/documentation_part.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7528 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/apigateway/documentation_version.py
+-rw-r--r--   0 runner    (1001) docker     (121)    13636 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/apigateway/domain_name.py
+-rw-r--r--   0 runner    (1001) docker     (121)    10379 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/apigateway/gateway_response.py
+-rw-r--r--   0 runner    (1001) docker     (121)    22516 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/apigateway/method.py
+-rw-r--r--   0 runner    (1001) docker     (121)     9722 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/apigateway/model.py
+-rw-r--r--   0 runner    (1001) docker     (121)    83010 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/apigateway/outputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)     9439 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/apigateway/request_validator.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7515 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/apigateway/resource.py
+-rw-r--r--   0 runner    (1001) docker     (121)    18120 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/apigateway/rest_api.py
+-rw-r--r--   0 runner    (1001) docker     (121)    23677 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/apigateway/stage.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11995 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/apigateway/usage_plan.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7313 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/apigateway/usage_plan_key.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7573 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/apigateway/vpc_link.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 15:05:10.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/apigatewayv2/
+-rw-r--r--   0 runner    (1001) docker     (121)      648 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/apigatewayv2/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    26786 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/apigatewayv2/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    19707 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/apigatewayv2/api.py
+-rw-r--r--   0 runner    (1001) docker     (121)     8515 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/apigatewayv2/api_gateway_managed_overrides.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7490 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/apigatewayv2/api_mapping.py
+-rw-r--r--   0 runner    (1001) docker     (121)    15642 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/apigatewayv2/authorizer.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6566 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/apigatewayv2/deployment.py
+-rw-r--r--   0 runner    (1001) docker     (121)     9102 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/apigatewayv2/domain_name.py
+-rw-r--r--   0 runner    (1001) docker     (121)    21514 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/apigatewayv2/integration.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11339 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/apigatewayv2/integration_response.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7887 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/apigatewayv2/model.py
+-rw-r--r--   0 runner    (1001) docker     (121)    26988 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/apigatewayv2/outputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    15434 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/apigatewayv2/route.py
+-rw-r--r--   0 runner    (1001) docker     (121)     9759 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/apigatewayv2/route_response.py
+-rw-r--r--   0 runner    (1001) docker     (121)    14958 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/apigatewayv2/stage.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7489 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/apigatewayv2/vpc_link.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 15:05:10.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/appconfig/
+-rw-r--r--   0 runner    (1001) docker     (121)      494 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/appconfig/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6578 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/appconfig/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6682 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/appconfig/application.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11652 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/appconfig/configuration_profile.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11181 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/appconfig/deployment.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11985 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/appconfig/deployment_strategy.py
+-rw-r--r--   0 runner    (1001) docker     (121)     8691 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/appconfig/environment.py
+-rw-r--r--   0 runner    (1001) docker     (121)    10134 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/appconfig/hosted_configuration_version.py
+-rw-r--r--   0 runner    (1001) docker     (121)     5177 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/appconfig/outputs.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 15:05:10.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/appflow/
+-rw-r--r--   0 runner    (1001) docker     (121)      373 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/appflow/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    12565 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/appflow/_enums.py
+-rw-r--r--   0 runner    (1001) docker     (121)   144759 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/appflow/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    12922 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/appflow/connector_profile.py
+-rw-r--r--   0 runner    (1001) docker     (121)    15237 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/appflow/flow.py
+-rw-r--r--   0 runner    (1001) docker     (121)   145650 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/appflow/outputs.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 15:05:10.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/appintegrations/
+-rw-r--r--   0 runner    (1001) docker     (121)      331 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/appintegrations/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1947 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/appintegrations/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11090 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/appintegrations/event_integration.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6428 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/appintegrations/outputs.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 15:05:10.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/applicationautoscaling/
+-rw-r--r--   0 runner    (1001) docker     (121)      359 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/applicationautoscaling/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    18725 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/applicationautoscaling/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    19117 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/applicationautoscaling/outputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    12365 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/applicationautoscaling/scalable_target.py
+-rw-r--r--   0 runner    (1001) docker     (121)    13194 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/applicationautoscaling/scaling_policy.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 15:05:10.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/applicationinsights/
+-rw-r--r--   0 runner    (1001) docker     (121)      347 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/applicationinsights/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1449 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/applicationinsights/_enums.py
+-rw-r--r--   0 runner    (1001) docker     (121)    32907 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/applicationinsights/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    18569 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/applicationinsights/application.py
+-rw-r--r--   0 runner    (1001) docker     (121)    34411 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/applicationinsights/outputs.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 15:05:10.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/appmesh/
+-rw-r--r--   0 runner    (1001) docker     (121)      488 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/appmesh/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)   151114 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/appmesh/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    10471 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/appmesh/gateway_route.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7497 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/appmesh/mesh.py
+-rw-r--r--   0 runner    (1001) docker     (121)   152616 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/appmesh/outputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    10065 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/appmesh/route.py
+-rw-r--r--   0 runner    (1001) docker     (121)     9511 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/appmesh/virtual_gateway.py
+-rw-r--r--   0 runner    (1001) docker     (121)     9352 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/appmesh/virtual_node.py
+-rw-r--r--   0 runner    (1001) docker     (121)     9458 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/appmesh/virtual_router.py
+-rw-r--r--   0 runner    (1001) docker     (121)     9501 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/appmesh/virtual_service.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 15:05:10.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/apprunner/
+-rw-r--r--   0 runner    (1001) docker     (121)      343 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/apprunner/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1125 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/apprunner/_enums.py
+-rw-r--r--   0 runner    (1001) docker     (121)    24254 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/apprunner/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    24844 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/apprunner/outputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    13695 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/apprunner/service.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 15:05:10.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/appstream/
+-rw-r--r--   0 runner    (1001) docker     (121)      673 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/appstream/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    20049 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/appstream/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)     9806 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/appstream/app_block.py
+-rw-r--r--   0 runner    (1001) docker     (121)    15611 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/appstream/application.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6964 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/appstream/application_entitlement_association.py
+-rw-r--r--   0 runner    (1001) docker     (121)     5725 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/appstream/application_fleet_association.py
+-rw-r--r--   0 runner    (1001) docker     (121)     8265 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/appstream/directory_config.py
+-rw-r--r--   0 runner    (1001) docker     (121)     8652 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/appstream/entitlement.py
+-rw-r--r--   0 runner    (1001) docker     (121)    23608 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/appstream/fleet.py
+-rw-r--r--   0 runner    (1001) docker     (121)    17028 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/appstream/image_builder.py
+-rw-r--r--   0 runner    (1001) docker     (121)    23129 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/appstream/outputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    17442 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/appstream/stack.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6108 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/appstream/stack_fleet_association.py
+-rw-r--r--   0 runner    (1001) docker     (121)     8191 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/appstream/stack_user_association.py
+-rw-r--r--   0 runner    (1001) docker     (121)     8388 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/appstream/user.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 15:05:10.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/appsync/
+-rw-r--r--   0 runner    (1001) docker     (121)      564 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/appsync/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    28331 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/appsync/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)     9648 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/appsync/api_cache.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7063 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/appsync/api_key.py
+-rw-r--r--   0 runner    (1001) docker     (121)    15684 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/appsync/data_source.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6146 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/appsync/domain_name.py
+-rw-r--r--   0 runner    (1001) docker     (121)     5835 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/appsync/domain_name_api_association.py
+-rw-r--r--   0 runner    (1001) docker     (121)    15108 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/appsync/function_configuration.py
+-rw-r--r--   0 runner    (1001) docker     (121)    14670 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/appsync/graph_ql_api.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6818 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/appsync/graph_ql_schema.py
+-rw-r--r--   0 runner    (1001) docker     (121)    32820 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/appsync/outputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    16583 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/appsync/resolver.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 15:05:10.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/aps/
+-rw-r--r--   0 runner    (1001) docker     (121)      360 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/aps/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     4154 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/aps/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)     3702 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/aps/outputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)     8779 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/aps/rule_groups_namespace.py
+-rw-r--r--   0 runner    (1001) docker     (121)     8351 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/aps/workspace.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 15:05:10.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ask/
+-rw-r--r--   0 runner    (1001) docker     (121)      319 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ask/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     4364 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ask/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)     4530 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ask/outputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7409 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ask/skill.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 15:05:10.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/athena/
+-rw-r--r--   0 runner    (1001) docker     (121)      435 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/athena/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1037 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/athena/_enums.py
+-rw-r--r--   0 runner    (1001) docker     (121)    17819 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/athena/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    10822 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/athena/data_catalog.py
+-rw-r--r--   0 runner    (1001) docker     (121)     9455 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/athena/named_query.py
+-rw-r--r--   0 runner    (1001) docker     (121)    19028 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/athena/outputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)     8680 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/athena/prepared_statement.py
+-rw-r--r--   0 runner    (1001) docker     (121)    13901 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/athena/work_group.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 15:05:10.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/auditmanager/
+-rw-r--r--   0 runner    (1001) docker     (121)      346 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/auditmanager/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)      944 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/auditmanager/_enums.py
+-rw-r--r--   0 runner    (1001) docker     (121)     8601 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/auditmanager/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    14100 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/auditmanager/assessment.py
+-rw-r--r--   0 runner    (1001) docker     (121)    14624 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/auditmanager/outputs.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 15:05:10.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/autoscaling/
+-rw-r--r--   0 runner    (1001) docker     (121)      485 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/autoscaling/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    66762 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/autoscaling/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    34132 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/autoscaling/auto_scaling_group.py
+-rw-r--r--   0 runner    (1001) docker     (121)    32906 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/autoscaling/launch_configuration.py
+-rw-r--r--   0 runner    (1001) docker     (121)    18325 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/autoscaling/lifecycle_hook.py
+-rw-r--r--   0 runner    (1001) docker     (121)    64682 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/autoscaling/outputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    16460 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/autoscaling/scaling_policy.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11153 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/autoscaling/scheduled_action.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7404 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/autoscaling/warm_pool.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 15:05:10.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/autoscalingplans/
+-rw-r--r--   0 runner    (1001) docker     (121)      326 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/autoscalingplans/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    22982 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/autoscalingplans/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    21762 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/autoscalingplans/outputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7449 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/autoscalingplans/scaling_plan.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 15:05:10.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/backup/
+-rw-r--r--   0 runner    (1001) docker     (121)      437 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/backup/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    37338 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/backup/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6329 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/backup/backup_plan.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6102 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/backup/backup_selection.py
+-rw-r--r--   0 runner    (1001) docker     (121)     9882 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/backup/backup_vault.py
+-rw-r--r--   0 runner    (1001) docker     (121)    13350 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/backup/framework.py
+-rw-r--r--   0 runner    (1001) docker     (121)    39459 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/backup/outputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    13437 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/backup/report_plan.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 15:05:10.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/batch/
+-rw-r--r--   0 runner    (1001) docker     (121)      421 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/batch/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    52769 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/batch/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    10530 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/batch/compute_environment.py
+-rw-r--r--   0 runner    (1001) docker     (121)    14861 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/batch/job_definition.py
+-rw-r--r--   0 runner    (1001) docker     (121)     9729 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/batch/job_queue.py
+-rw-r--r--   0 runner    (1001) docker     (121)    53446 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/batch/outputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6991 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/batch/scheduling_policy.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 15:05:10.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/budgets/
+-rw-r--r--   0 runner    (1001) docker     (121)      372 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/budgets/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1158 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/budgets/_enums.py
+-rw-r--r--   0 runner    (1001) docker     (121)    23085 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/budgets/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6520 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/budgets/budget.py
+-rw-r--r--   0 runner    (1001) docker     (121)    12600 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/budgets/budgets_action.py
+-rw-r--r--   0 runner    (1001) docker     (121)    21533 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/budgets/outputs.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 15:05:10.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/cassandra/
+-rw-r--r--   0 runner    (1001) docker     (121)      365 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/cassandra/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)      713 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/cassandra/_enums.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7176 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/cassandra/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)     5681 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/cassandra/keyspace.py
+-rw-r--r--   0 runner    (1001) docker     (121)     8412 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/cassandra/outputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    18365 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/cassandra/table.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 15:05:10.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ce/
+-rw-r--r--   0 runner    (1001) docker     (121)      416 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ce/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1156 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ce/_enums.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1710 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ce/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    10942 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ce/anomaly_monitor.py
+-rw-r--r--   0 runner    (1001) docker     (121)    12274 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ce/anomaly_subscription.py
+-rw-r--r--   0 runner    (1001) docker     (121)     9934 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ce/cost_category.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1222 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ce/outputs.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 15:05:10.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/certificatemanager/
+-rw-r--r--   0 runner    (1001) docker     (121)      348 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/certificatemanager/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     3231 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/certificatemanager/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)     5245 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/certificatemanager/account.py
+-rw-r--r--   0 runner    (1001) docker     (121)    12295 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/certificatemanager/certificate.py
+-rw-r--r--   0 runner    (1001) docker     (121)     3679 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/certificatemanager/outputs.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 15:05:10.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/chatbot/
+-rw-r--r--   0 runner    (1001) docker     (121)      296 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/chatbot/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    16028 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/chatbot/slack_channel_configuration.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2122 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/cidr.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 15:05:10.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/cloud9/
+-rw-r--r--   0 runner    (1001) docker     (121)      329 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/cloud9/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1986 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/cloud9/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    13558 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/cloud9/environment_ec2.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2070 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/cloud9/outputs.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 15:05:10.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/cloudformation/
+-rw-r--r--   0 runner    (1001) docker     (121)      716 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/cloudformation/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     3821 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/cloudformation/_enums.py
+-rw-r--r--   0 runner    (1001) docker     (121)    18734 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/cloudformation/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)     5141 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/cloudformation/custom_resource.py
+-rw-r--r--   0 runner    (1001) docker     (121)     8228 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/cloudformation/macro.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7457 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/cloudformation/module_default_version.py
+-rw-r--r--   0 runner    (1001) docker     (121)     9767 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/cloudformation/module_version.py
+-rw-r--r--   0 runner    (1001) docker     (121)    19691 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/cloudformation/outputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11527 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/cloudformation/public_type_version.py
+-rw-r--r--   0 runner    (1001) docker     (121)     9654 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/cloudformation/publisher.py
+-rw-r--r--   0 runner    (1001) docker     (121)     8384 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/cloudformation/resource_default_version.py
+-rw-r--r--   0 runner    (1001) docker     (121)    14948 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/cloudformation/resource_version.py
+-rw-r--r--   0 runner    (1001) docker     (121)     8708 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/cloudformation/stack.py
+-rw-r--r--   0 runner    (1001) docker     (121)    31552 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/cloudformation/stack_set.py
+-rw-r--r--   0 runner    (1001) docker     (121)    20665 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/cloudformation/type_activation.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6618 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/cloudformation/wait_condition.py
+-rw-r--r--   0 runner    (1001) docker     (121)     4348 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/cloudformation/wait_condition_handle.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 15:05:10.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/cloudfront/
+-rw-r--r--   0 runner    (1001) docker     (121)      628 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/cloudfront/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)   116322 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/cloudfront/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)     5110 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/cloudfront/cache_policy.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6006 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/cloudfront/cloud_front_origin_access_identity.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6087 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/cloudfront/distribution.py
+-rw-r--r--   0 runner    (1001) docker     (121)     8698 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/cloudfront/function.py
+-rw-r--r--   0 runner    (1001) docker     (121)     4978 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/cloudfront/key_group.py
+-rw-r--r--   0 runner    (1001) docker     (121)     5479 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/cloudfront/origin_request_policy.py
+-rw-r--r--   0 runner    (1001) docker     (121)   112633 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/cloudfront/outputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)     4993 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/cloudfront/public_key.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7695 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/cloudfront/realtime_log_config.py
+-rw-r--r--   0 runner    (1001) docker     (121)     5567 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/cloudfront/response_headers_policy.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7180 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/cloudfront/streaming_distribution.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 15:05:10.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/cloudtrail/
+-rw-r--r--   0 runner    (1001) docker     (121)      341 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/cloudtrail/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)      587 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/cloudtrail/_enums.py
+-rw-r--r--   0 runner    (1001) docker     (121)     9378 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/cloudtrail/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)     9623 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/cloudtrail/outputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    33128 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/cloudtrail/trail.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 15:05:10.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/cloudwatch/
+-rw-r--r--   0 runner    (1001) docker     (121)      464 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/cloudwatch/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    20941 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/cloudwatch/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    24353 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/cloudwatch/alarm.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11797 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/cloudwatch/anomaly_detector.py
+-rw-r--r--   0 runner    (1001) docker     (121)    15166 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/cloudwatch/composite_alarm.py
+-rw-r--r--   0 runner    (1001) docker     (121)     5943 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/cloudwatch/dashboard.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7820 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/cloudwatch/insight_rule.py
+-rw-r--r--   0 runner    (1001) docker     (121)    16693 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/cloudwatch/metric_stream.py
+-rw-r--r--   0 runner    (1001) docker     (121)    19333 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/cloudwatch/outputs.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 15:05:10.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/codeartifact/
+-rw-r--r--   0 runner    (1001) docker     (121)      346 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/codeartifact/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     4138 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/codeartifact/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)     8767 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/codeartifact/domain.py
+-rw-r--r--   0 runner    (1001) docker     (121)     3686 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/codeartifact/outputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    13084 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/codeartifact/repository.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 15:05:10.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/codebuild/
+-rw-r--r--   0 runner    (1001) docker     (121)      382 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/codebuild/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    38573 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/codebuild/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    37364 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/codebuild/outputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    28509 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/codebuild/project.py
+-rw-r--r--   0 runner    (1001) docker     (121)     8874 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/codebuild/report_group.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7520 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/codebuild/source_credential.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 15:05:10.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/codecommit/
+-rw-r--r--   0 runner    (1001) docker     (121)      324 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/codecommit/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     5296 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/codecommit/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)     5232 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/codecommit/outputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)     9945 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/codecommit/repository.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 15:05:10.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/codedeploy/
+-rw-r--r--   0 runner    (1001) docker     (121)      390 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/codedeploy/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    32606 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/codedeploy/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7057 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/codedeploy/application.py
+-rw-r--r--   0 runner    (1001) docker     (121)     8928 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/codedeploy/deployment_config.py
+-rw-r--r--   0 runner    (1001) docker     (121)    24966 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/codedeploy/deployment_group.py
+-rw-r--r--   0 runner    (1001) docker     (121)    35145 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/codedeploy/outputs.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 15:05:10.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/codeguruprofiler/
+-rw-r--r--   0 runner    (1001) docker     (121)      351 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/codeguruprofiler/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)      411 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/codeguruprofiler/_enums.py
+-rw-r--r--   0 runner    (1001) docker     (121)     4254 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/codeguruprofiler/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)     4369 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/codeguruprofiler/outputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    13053 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/codeguruprofiler/profiling_group.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 15:05:10.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/codegurureviewer/
+-rw-r--r--   0 runner    (1001) docker     (121)      358 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/codegurureviewer/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)      489 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/codegurureviewer/_enums.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2329 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/codegurureviewer/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2103 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/codegurureviewer/outputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    12199 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/codegurureviewer/repository_association.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 15:05:10.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/codepipeline/
+-rw-r--r--   0 runner    (1001) docker     (121)      379 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/codepipeline/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    22323 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/codepipeline/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    12905 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/codepipeline/custom_action_type.py
+-rw-r--r--   0 runner    (1001) docker     (121)    20047 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/codepipeline/outputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    13009 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/codepipeline/pipeline.py
+-rw-r--r--   0 runner    (1001) docker     (121)    12544 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/codepipeline/webhook.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 15:05:10.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/codestar/
+-rw-r--r--   0 runner    (1001) docker     (121)      332 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/codestar/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2013 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/codestar/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11904 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/codestar/git_hub_repository.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2035 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/codestar/outputs.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 15:05:10.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/codestarconnections/
+-rw-r--r--   0 runner    (1001) docker     (121)      324 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/codestarconnections/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2239 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/codestarconnections/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11044 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/codestarconnections/connection.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2013 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/codestarconnections/outputs.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 15:05:10.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/codestarnotifications/
+-rw-r--r--   0 runner    (1001) docker     (121)      353 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/codestarnotifications/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)      448 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/codestarnotifications/_enums.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1259 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/codestarnotifications/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    12850 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/codestarnotifications/notification_rule.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1605 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/codestarnotifications/outputs.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 15:05:10.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/cognito/
+-rw-r--r--   0 runner    (1001) docker     (121)      764 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/cognito/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    57789 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/cognito/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    16676 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/cognito/identity_pool.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6925 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/cognito/identity_pool_role_attachment.py
+-rw-r--r--   0 runner    (1001) docker     (121)    64254 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/cognito/outputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    29578 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/cognito/user_pool.py
+-rw-r--r--   0 runner    (1001) docker     (121)    26513 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/cognito/user_pool_client.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7208 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/cognito/user_pool_domain.py
+-rw-r--r--   0 runner    (1001) docker     (121)     8348 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/cognito/user_pool_group.py
+-rw-r--r--   0 runner    (1001) docker     (121)    10027 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/cognito/user_pool_identity_provider.py
+-rw-r--r--   0 runner    (1001) docker     (121)     8062 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/cognito/user_pool_resource_server.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11798 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/cognito/user_pool_risk_configuration_attachment.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7125 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/cognito/user_pool_ui_customization_attachment.py
+-rw-r--r--   0 runner    (1001) docker     (121)    12408 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/cognito/user_pool_user.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7130 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/cognito/user_pool_user_to_group_attachment.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 15:05:10.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/config/
+-rw-r--r--   0 runner    (1001) docker     (121)      269 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/config/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    78929 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/config/outputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6489 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/config/vars.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 15:05:10.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/configuration/
+-rw-r--r--   0 runner    (1001) docker     (121)      662 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/configuration/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    30525 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/configuration/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)     8767 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/configuration/aggregation_authorization.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11113 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/configuration/config_rule.py
+-rw-r--r--   0 runner    (1001) docker     (121)    10441 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/configuration/configuration_aggregator.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7137 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/configuration/configuration_recorder.py
+-rw-r--r--   0 runner    (1001) docker     (121)    13936 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/configuration/conformance_pack.py
+-rw-r--r--   0 runner    (1001) docker     (121)    10225 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/configuration/delivery_channel.py
+-rw-r--r--   0 runner    (1001) docker     (121)     9955 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/configuration/organization_config_rule.py
+-rw-r--r--   0 runner    (1001) docker     (121)    15090 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/configuration/organization_conformance_pack.py
+-rw-r--r--   0 runner    (1001) docker     (121)    32449 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/configuration/outputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    13980 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/configuration/remediation_configuration.py
+-rw-r--r--   0 runner    (1001) docker     (121)     8268 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/configuration/stored_query.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 15:05:10.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/connect/
+-rw-r--r--   0 runner    (1001) docker     (121)      502 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/connect/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1994 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/connect/_enums.py
+-rw-r--r--   0 runner    (1001) docker     (121)    21885 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/connect/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11959 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/connect/contact_flow.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11549 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/connect/contact_flow_module.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11714 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/connect/hours_of_operation.py
+-rw-r--r--   0 runner    (1001) docker     (121)    22788 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/connect/outputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    10316 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/connect/quick_connect.py
+-rw-r--r--   0 runner    (1001) docker     (121)    17719 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/connect/user.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7738 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/connect/user_hierarchy_group.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 15:05:10.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/cur/
+-rw-r--r--   0 runner    (1001) docker     (121)      308 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/cur/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1661 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/cur/_enums.py
+-rw-r--r--   0 runner    (1001) docker     (121)    24282 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/cur/report_definition.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 15:05:10.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/customerprofiles/
+-rw-r--r--   0 runner    (1001) docker     (121)      396 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/customerprofiles/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     5795 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/customerprofiles/_enums.py
+-rw-r--r--   0 runner    (1001) docker     (121)    35152 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/customerprofiles/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    10976 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/customerprofiles/domain.py
+-rw-r--r--   0 runner    (1001) docker     (121)    10663 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/customerprofiles/integration.py
+-rw-r--r--   0 runner    (1001) docker     (121)    17534 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/customerprofiles/object_type.py
+-rw-r--r--   0 runner    (1001) docker     (121)    34978 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/customerprofiles/outputs.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 15:05:10.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/databrew/
+-rw-r--r--   0 runner    (1001) docker     (121)      454 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/databrew/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2808 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/databrew/_enums.py
+-rw-r--r--   0 runner    (1001) docker     (121)   123545 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/databrew/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    10257 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/databrew/dataset.py
+-rw-r--r--   0 runner    (1001) docker     (121)    26778 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/databrew/job.py
+-rw-r--r--   0 runner    (1001) docker     (121)   111282 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/databrew/outputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)     9737 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/databrew/project.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7418 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/databrew/recipe.py
+-rw-r--r--   0 runner    (1001) docker     (121)     9205 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/databrew/ruleset.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7536 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/databrew/schedule.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 15:05:10.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/datapipeline/
+-rw-r--r--   0 runner    (1001) docker     (121)      322 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/datapipeline/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6003 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/datapipeline/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)     5746 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/datapipeline/outputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11364 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/datapipeline/pipeline.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 15:05:10.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/datasync/
+-rw-r--r--   0 runner    (1001) docker     (121)      577 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/datasync/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6505 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/datasync/_enums.py
+-rw-r--r--   0 runner    (1001) docker     (121)    34740 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/datasync/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    12768 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/datasync/agent.py
+-rw-r--r--   0 runner    (1001) docker     (121)     9917 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/datasync/location_efs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    14215 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/datasync/location_f_sx_windows.py
+-rw-r--r--   0 runner    (1001) docker     (121)    23250 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/datasync/location_hdfs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11023 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/datasync/location_nfs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    17875 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/datasync/location_object_storage.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11413 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/datasync/location_s3.py
+-rw-r--r--   0 runner    (1001) docker     (121)    15411 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/datasync/location_smb.py
+-rw-r--r--   0 runner    (1001) docker     (121)    33362 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/datasync/outputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    16639 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/datasync/task.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 15:05:10.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/dax/
+-rw-r--r--   0 runner    (1001) docker     (121)      380 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/dax/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)      922 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/dax/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    18892 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/dax/cluster.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1344 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/dax/outputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6988 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/dax/parameter_group.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6892 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/dax/subnet_group.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 15:05:10.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/detective/
+-rw-r--r--   0 runner    (1001) docker     (121)      352 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/detective/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2345 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/detective/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)     4698 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/detective/graph.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11321 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/detective/member_invitation.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2099 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/detective/outputs.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 15:05:10.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/devicefarm/
+-rw-r--r--   0 runner    (1001) docker     (121)      500 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/devicefarm/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1183 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/devicefarm/_enums.py
+-rw-r--r--   0 runner    (1001) docker     (121)     8607 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/devicefarm/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)     9129 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/devicefarm/device_pool.py
+-rw-r--r--   0 runner    (1001) docker     (121)     9715 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/devicefarm/instance_profile.py
+-rw-r--r--   0 runner    (1001) docker     (121)    15238 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/devicefarm/network_profile.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6744 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/devicefarm/outputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6559 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/devicefarm/project.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7471 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/devicefarm/test_grid_project.py
+-rw-r--r--   0 runner    (1001) docker     (121)     9296 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/devicefarm/vpce_configuration.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 15:05:10.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/devopsguru/
+-rw-r--r--   0 runner    (1001) docker     (121)      391 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/devopsguru/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)      378 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/devopsguru/_enums.py
+-rw-r--r--   0 runner    (1001) docker     (121)     3684 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/devopsguru/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)     4804 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/devopsguru/notification_channel.py
+-rw-r--r--   0 runner    (1001) docker     (121)     5240 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/devopsguru/outputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)     5606 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/devopsguru/resource_collection.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 15:05:10.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/directoryservice/
+-rw-r--r--   0 runner    (1001) docker     (121)      351 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/directoryservice/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2118 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/directoryservice/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    10607 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/directoryservice/microsoft_ad.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2715 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/directoryservice/outputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11324 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/directoryservice/simple_ad.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 15:05:10.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/dlm/
+-rw-r--r--   0 runner    (1001) docker     (121)      330 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/dlm/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    32665 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/dlm/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)     9116 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/dlm/lifecycle_policy.py
+-rw-r--r--   0 runner    (1001) docker     (121)    32397 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/dlm/outputs.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 15:05:10.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/dms/
+-rw-r--r--   0 runner    (1001) docker     (121)      491 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/dms/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    49988 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/dms/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7085 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/dms/certificate.py
+-rw-r--r--   0 runner    (1001) docker     (121)    35369 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/dms/endpoint.py
+-rw-r--r--   0 runner    (1001) docker     (121)    10858 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/dms/event_subscription.py
+-rw-r--r--   0 runner    (1001) docker     (121)    48226 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/dms/outputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    20950 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/dms/replication_instance.py
+-rw-r--r--   0 runner    (1001) docker     (121)     9106 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/dms/replication_subnet_group.py
+-rw-r--r--   0 runner    (1001) docker     (121)    17317 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/dms/replication_task.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 15:05:10.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/docdb/
+-rw-r--r--   0 runner    (1001) docker     (121)      424 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/docdb/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     3202 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/docdb/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    23535 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/docdb/db_cluster.py
+-rw-r--r--   0 runner    (1001) docker     (121)     8592 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/docdb/db_cluster_parameter_group.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11976 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/docdb/db_instance.py
+-rw-r--r--   0 runner    (1001) docker     (121)     8443 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/docdb/db_subnet_group.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2142 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/docdb/outputs.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 15:05:10.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/dynamodb/
+-rw-r--r--   0 runner    (1001) docker     (121)      347 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/dynamodb/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    39826 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/dynamodb/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    18247 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/dynamodb/global_table.py
+-rw-r--r--   0 runner    (1001) docker     (121)    46003 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/dynamodb/outputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    22860 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/dynamodb/table.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 15:05:10.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ec2/
+-rw-r--r--   0 runner    (1001) docker     (121)     3261 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ec2/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    14897 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ec2/_enums.py
+-rw-r--r--   0 runner    (1001) docker     (121)   303634 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ec2/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    17488 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ec2/capacity_reservation.py
+-rw-r--r--   0 runner    (1001) docker     (121)    14294 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ec2/capacity_reservation_fleet.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7031 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ec2/carrier_gateway.py
+-rw-r--r--   0 runner    (1001) docker     (121)     9364 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ec2/client_vpn_authorization_rule.py
+-rw-r--r--   0 runner    (1001) docker     (121)    19384 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ec2/client_vpn_endpoint.py
+-rw-r--r--   0 runner    (1001) docker     (121)     8261 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ec2/client_vpn_route.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6571 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ec2/client_vpn_target_network_association.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7682 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ec2/customer_gateway.py
+-rw-r--r--   0 runner    (1001) docker     (121)    12516 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ec2/dhcp_options.py
+-rw-r--r--   0 runner    (1001) docker     (121)    17650 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ec2/ec2_fleet.py
+-rw-r--r--   0 runner    (1001) docker     (121)     5054 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ec2/egress_only_internet_gateway.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7711 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ec2/eip.py
+-rw-r--r--   0 runner    (1001) docker     (121)     8664 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ec2/eipassociation.py
+-rw-r--r--   0 runner    (1001) docker     (121)     8792 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ec2/enclave_certificate_iam_role_association.py
+-rw-r--r--   0 runner    (1001) docker     (121)    22563 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ec2/flow_log.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6837 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ec2/gateway_route_table_association.py
+-rw-r--r--   0 runner    (1001) docker     (121)    10312 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ec2/host.py
+-rw-r--r--   0 runner    (1001) docker     (121)    46153 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ec2/instance.py
+-rw-r--r--   0 runner    (1001) docker     (121)     5464 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ec2/internet_gateway.py
+-rw-r--r--   0 runner    (1001) docker     (121)     9434 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ec2/ipam.py
+-rw-r--r--   0 runner    (1001) docker     (121)     8294 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ec2/ipam_allocation.py
+-rw-r--r--   0 runner    (1001) docker     (121)    27172 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ec2/ipam_pool.py
+-rw-r--r--   0 runner    (1001) docker     (121)     8977 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ec2/ipam_scope.py
+-rw-r--r--   0 runner    (1001) docker     (121)     8388 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ec2/launch_template.py
+-rw-r--r--   0 runner    (1001) docker     (121)     9010 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ec2/local_gateway_route.py
+-rw-r--r--   0 runner    (1001) docker     (121)     9272 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ec2/local_gateway_route_table_vpcassociation.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7813 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ec2/nat_gateway.py
+-rw-r--r--   0 runner    (1001) docker     (121)     5970 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ec2/network_acl.py
+-rw-r--r--   0 runner    (1001) docker     (121)    19877 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ec2/network_acl_entry.py
+-rw-r--r--   0 runner    (1001) docker     (121)     8894 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ec2/network_insights_access_scope.py
+-rw-r--r--   0 runner    (1001) docker     (121)     8839 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ec2/network_insights_access_scope_analysis.py
+-rw-r--r--   0 runner    (1001) docker     (121)    10128 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ec2/network_insights_analysis.py
+-rw-r--r--   0 runner    (1001) docker     (121)    10941 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ec2/network_insights_path.py
+-rw-r--r--   0 runner    (1001) docker     (121)    25145 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ec2/network_interface.py
+-rw-r--r--   0 runner    (1001) docker     (121)     8368 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ec2/network_interface_attachment.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7309 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ec2/network_interface_permission.py
+-rw-r--r--   0 runner    (1001) docker     (121)   325272 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ec2/outputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)     4960 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ec2/placement_group.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11177 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ec2/prefix_list.py
+-rw-r--r--   0 runner    (1001) docker     (121)    16872 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ec2/route.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6283 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ec2/route_table.py
+-rw-r--r--   0 runner    (1001) docker     (121)    10732 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ec2/security_group.py
+-rw-r--r--   0 runner    (1001) docker     (121)    12385 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ec2/security_group_egress.py
+-rw-r--r--   0 runner    (1001) docker     (121)    15342 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ec2/security_group_ingress.py
+-rw-r--r--   0 runner    (1001) docker     (121)     5047 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ec2/spot_fleet.py
+-rw-r--r--   0 runner    (1001) docker     (121)    12014 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ec2/subnet.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6026 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ec2/subnet_cidr_block.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6435 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ec2/subnet_network_acl_association.py
+-rw-r--r--   0 runner    (1001) docker     (121)     5667 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ec2/subnet_route_table_association.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7270 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ec2/traffic_mirror_filter.py
+-rw-r--r--   0 runner    (1001) docker     (121)    14741 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ec2/traffic_mirror_filter_rule.py
+-rw-r--r--   0 runner    (1001) docker     (121)    12378 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ec2/traffic_mirror_session.py
+-rw-r--r--   0 runner    (1001) docker     (121)     8314 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ec2/traffic_mirror_target.py
+-rw-r--r--   0 runner    (1001) docker     (121)    16591 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ec2/transit_gateway.py
+-rw-r--r--   0 runner    (1001) docker     (121)     8342 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ec2/transit_gateway_attachment.py
+-rw-r--r--   0 runner    (1001) docker     (121)     9793 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ec2/transit_gateway_connect.py
+-rw-r--r--   0 runner    (1001) docker     (121)     9693 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ec2/transit_gateway_multicast_domain.py
+-rw-r--r--   0 runner    (1001) docker     (121)     9657 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ec2/transit_gateway_multicast_domain_association.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11424 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ec2/transit_gateway_multicast_group_member.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11424 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ec2/transit_gateway_multicast_group_source.py
+-rw-r--r--   0 runner    (1001) docker     (121)    13595 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ec2/transit_gateway_peering_attachment.py
+-rw-r--r--   0 runner    (1001) docker     (121)     8560 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ec2/transit_gateway_route.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6532 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ec2/transit_gateway_route_table.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7143 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ec2/transit_gateway_route_table_association.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7143 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ec2/transit_gateway_route_table_propagation.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11164 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ec2/transit_gateway_vpc_attachment.py
+-rw-r--r--   0 runner    (1001) docker     (121)    14339 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ec2/volume.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6749 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ec2/volume_attachment.py
+-rw-r--r--   0 runner    (1001) docker     (121)    16196 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ec2/vpc.py
+-rw-r--r--   0 runner    (1001) docker     (121)     8729 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ec2/vpc_cidr_block.py
+-rw-r--r--   0 runner    (1001) docker     (121)    12637 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ec2/vpc_endpoint.py
+-rw-r--r--   0 runner    (1001) docker     (121)     8730 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ec2/vpc_endpoint_connection_notification.py
+-rw-r--r--   0 runner    (1001) docker     (121)     8810 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ec2/vpc_endpoint_service.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6508 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ec2/vpc_endpoint_service_permissions.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7019 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ec2/vpc_gateway_attachment.py
+-rw-r--r--   0 runner    (1001) docker     (121)     9721 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ec2/vpc_peering_connection.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6369 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ec2/vpcdhcp_options_association.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11534 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ec2/vpn_connection.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6378 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ec2/vpn_connection_route.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6764 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ec2/vpn_gateway.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6502 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ec2/vpn_gateway_route_propagation.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 15:05:10.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ecr/
+-rw-r--r--   0 runner    (1001) docker     (121)      451 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ecr/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)      756 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ecr/_enums.py
+-rw-r--r--   0 runner    (1001) docker     (121)    16208 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ecr/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    18753 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ecr/outputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    13367 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ecr/public_repository.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6513 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ecr/registry_policy.py
+-rw-r--r--   0 runner    (1001) docker     (121)     5968 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ecr/replication_configuration.py
+-rw-r--r--   0 runner    (1001) docker     (121)    16427 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ecr/repository.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 15:05:10.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ecs/
+-rw-r--r--   0 runner    (1001) docker     (121)      540 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ecs/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2893 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ecs/_enums.py
+-rw-r--r--   0 runner    (1001) docker     (121)   113649 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ecs/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6925 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ecs/capacity_provider.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11539 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ecs/cluster.py
+-rw-r--r--   0 runner    (1001) docker     (121)     8200 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ecs/cluster_capacity_provider_associations.py
+-rw-r--r--   0 runner    (1001) docker     (121)   111338 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ecs/outputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7636 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ecs/primary_task_set.py
+-rw-r--r--   0 runner    (1001) docker     (121)    27131 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ecs/service.py
+-rw-r--r--   0 runner    (1001) docker     (121)    21822 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ecs/task_definition.py
+-rw-r--r--   0 runner    (1001) docker     (121)    20616 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ecs/task_set.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 15:05:10.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/efs/
+-rw-r--r--   0 runner    (1001) docker     (121)      381 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/efs/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    10630 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/efs/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    13087 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/efs/access_point.py
+-rw-r--r--   0 runner    (1001) docker     (121)    17840 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/efs/file_system.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7304 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/efs/mount_target.py
+-rw-r--r--   0 runner    (1001) docker     (121)    10710 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/efs/outputs.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 15:05:10.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/eks/
+-rw-r--r--   0 runner    (1001) docker     (121)      420 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/eks/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)      608 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/eks/_enums.py
+-rw-r--r--   0 runner    (1001) docker     (121)    28356 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/eks/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11340 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/eks/addon.py
+-rw-r--r--   0 runner    (1001) docker     (121)    16475 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/eks/cluster.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11157 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/eks/fargate_profile.py
+-rw-r--r--   0 runner    (1001) docker     (121)    20947 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/eks/nodegroup.py
+-rw-r--r--   0 runner    (1001) docker     (121)    27870 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/eks/outputs.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 15:05:10.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/elasticache/
+-rw-r--r--   0 runner    (1001) docker     (121)      595 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/elasticache/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)      645 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/elasticache/_enums.py
+-rw-r--r--   0 runner    (1001) docker     (121)    23112 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/elasticache/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    31486 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/elasticache/cache_cluster.py
+-rw-r--r--   0 runner    (1001) docker     (121)    19833 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/elasticache/global_replication_group.py
+-rw-r--r--   0 runner    (1001) docker     (121)    25211 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/elasticache/outputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)     8045 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/elasticache/parameter_group.py
+-rw-r--r--   0 runner    (1001) docker     (121)    51830 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/elasticache/replication_group.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6068 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/elasticache/security_group.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7786 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/elasticache/security_group_ingress.py
+-rw-r--r--   0 runner    (1001) docker     (121)     8086 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/elasticache/subnet_group.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11405 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/elasticache/user.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7770 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/elasticache/user_group.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 15:05:10.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/elasticbeanstalk/
+-rw-r--r--   0 runner    (1001) docker     (121)      425 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/elasticbeanstalk/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    13202 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/elasticbeanstalk/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7337 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/elasticbeanstalk/application.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7332 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/elasticbeanstalk/application_version.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11724 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/elasticbeanstalk/configuration_template.py
+-rw-r--r--   0 runner    (1001) docker     (121)    15766 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/elasticbeanstalk/environment.py
+-rw-r--r--   0 runner    (1001) docker     (121)    14438 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/elasticbeanstalk/outputs.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 15:05:10.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/elasticloadbalancing/
+-rw-r--r--   0 runner    (1001) docker     (121)      327 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/elasticloadbalancing/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    13693 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/elasticloadbalancing/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    25444 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/elasticloadbalancing/load_balancer.py
+-rw-r--r--   0 runner    (1001) docker     (121)    14099 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/elasticloadbalancing/outputs.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 15:05:10.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/elasticloadbalancingv2/
+-rw-r--r--   0 runner    (1001) docker     (121)      444 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/elasticloadbalancingv2/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    62045 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/elasticloadbalancingv2/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    10543 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/elasticloadbalancingv2/listener.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6586 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/elasticloadbalancingv2/listener_certificate.py
+-rw-r--r--   0 runner    (1001) docker     (121)     8147 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/elasticloadbalancingv2/listener_rule.py
+-rw-r--r--   0 runner    (1001) docker     (121)    14064 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/elasticloadbalancingv2/load_balancer.py
+-rw-r--r--   0 runner    (1001) docker     (121)    59592 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/elasticloadbalancingv2/outputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    23654 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/elasticloadbalancingv2/target_group.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 15:05:10.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/elasticsearch/
+-rw-r--r--   0 runner    (1001) docker     (121)      320 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/elasticsearch/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    21883 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/elasticsearch/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    21494 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/elasticsearch/domain.py
+-rw-r--r--   0 runner    (1001) docker     (121)    22570 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/elasticsearch/outputs.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 15:05:10.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/emr/
+-rw-r--r--   0 runner    (1001) docker     (121)      535 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/emr/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)      686 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/emr/_enums.py
+-rw-r--r--   0 runner    (1001) docker     (121)    95167 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/emr/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    26635 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/emr/cluster.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11970 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/emr/instance_fleet_config.py
+-rw-r--r--   0 runner    (1001) docker     (121)    14956 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/emr/instance_group_config.py
+-rw-r--r--   0 runner    (1001) docker     (121)    95382 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/emr/outputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6076 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/emr/security_configuration.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7755 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/emr/step.py
+-rw-r--r--   0 runner    (1001) docker     (121)    26554 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/emr/studio.py
+-rw-r--r--   0 runner    (1001) docker     (121)    10534 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/emr/studio_session_mapping.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 15:05:10.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/emrcontainers/
+-rw-r--r--   0 runner    (1001) docker     (121)      329 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/emrcontainers/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     4703 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/emrcontainers/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)     4366 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/emrcontainers/outputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)     8022 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/emrcontainers/virtual_cluster.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 15:05:10.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/events/
+-rw-r--r--   0 runner    (1001) docker     (121)      477 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/events/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)      751 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/events/_enums.py
+-rw-r--r--   0 runner    (1001) docker     (121)    47936 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/events/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    10488 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/events/api_destination.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7369 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/events/archive.py
+-rw-r--r--   0 runner    (1001) docker     (121)     8631 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/events/connection.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7166 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/events/event_bus.py
+-rw-r--r--   0 runner    (1001) docker     (121)     9273 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/events/event_bus_policy.py
+-rw-r--r--   0 runner    (1001) docker     (121)    46553 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/events/outputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    10994 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/events/rule.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 15:05:10.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/eventschemas/
+-rw-r--r--   0 runner    (1001) docker     (121)      401 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/eventschemas/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2486 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/eventschemas/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)     8282 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/eventschemas/discoverer.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1691 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/eventschemas/outputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7086 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/eventschemas/registry.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6131 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/eventschemas/registry_policy.py
+-rw-r--r--   0 runner    (1001) docker     (121)     9697 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/eventschemas/schema.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 15:05:10.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/evidently/
+-rw-r--r--   0 runner    (1001) docker     (121)      414 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/evidently/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)      516 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/evidently/_enums.py
+-rw-r--r--   0 runner    (1001) docker     (121)    27085 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/evidently/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    13099 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/evidently/experiment.py
+-rw-r--r--   0 runner    (1001) docker     (121)    12006 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/evidently/feature.py
+-rw-r--r--   0 runner    (1001) docker     (121)    12164 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/evidently/launch.py
+-rw-r--r--   0 runner    (1001) docker     (121)    28225 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/evidently/outputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7778 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/evidently/project.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6031 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/extension_resource.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 15:05:10.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/finspace/
+-rw-r--r--   0 runner    (1001) docker     (121)      347 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/finspace/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)      833 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/finspace/_enums.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6760 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/finspace/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    14925 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/finspace/environment.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7034 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/finspace/outputs.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 15:05:10.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/fis/
+-rw-r--r--   0 runner    (1001) docker     (121)      333 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/fis/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1581 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/fis/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)     9413 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/fis/experiment_template.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1399 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/fis/outputs.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 15:05:10.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/fms/
+-rw-r--r--   0 runner    (1001) docker     (121)      378 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/fms/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)      663 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/fms/_enums.py
+-rw-r--r--   0 runner    (1001) docker     (121)     4225 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/fms/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)     5704 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/fms/notification_channel.py
+-rw-r--r--   0 runner    (1001) docker     (121)     4281 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/fms/outputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    16455 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/fms/policy.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 15:05:10.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/frauddetector/
+-rw-r--r--   0 runner    (1001) docker     (121)      465 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/frauddetector/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     5396 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/frauddetector/_enums.py
+-rw-r--r--   0 runner    (1001) docker     (121)    47700 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/frauddetector/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    15382 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/frauddetector/detector.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7941 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/frauddetector/entity_type.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11540 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/frauddetector/event_type.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7714 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/frauddetector/label.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7800 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/frauddetector/outcome.py
+-rw-r--r--   0 runner    (1001) docker     (121)    38967 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/frauddetector/outputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    13355 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/frauddetector/variable.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 15:05:10.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/fsx/
+-rw-r--r--   0 runner    (1001) docker     (121)      325 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/fsx/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    38450 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/fsx/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    18593 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/fsx/file_system.py
+-rw-r--r--   0 runner    (1001) docker     (121)    35450 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/fsx/outputs.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 15:05:10.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/gamelift/
+-rw-r--r--   0 runner    (1001) docker     (121)      549 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/gamelift/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2671 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/gamelift/_enums.py
+-rw-r--r--   0 runner    (1001) docker     (121)    39310 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/gamelift/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)     8132 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/gamelift/alias.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7543 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/gamelift/build.py
+-rw-r--r--   0 runner    (1001) docker     (121)    53499 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/gamelift/fleet.py
+-rw-r--r--   0 runner    (1001) docker     (121)    24548 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/gamelift/game_server_group.py
+-rw-r--r--   0 runner    (1001) docker     (121)    14414 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/gamelift/game_session_queue.py
+-rw-r--r--   0 runner    (1001) docker     (121)    19810 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/gamelift/matchmaking_configuration.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7174 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/gamelift/matchmaking_rule_set.py
+-rw-r--r--   0 runner    (1001) docker     (121)    46051 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/gamelift/outputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7803 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/gamelift/script.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1611 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/get_account_id.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1851 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/get_azs.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1579 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/get_partition.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1507 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/get_region.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2105 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/get_ssm_parameter_list.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2129 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/get_ssm_parameter_string.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1611 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/get_url_suffix.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 15:05:10.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/globalaccelerator/
+-rw-r--r--   0 runner    (1001) docker     (121)      401 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/globalaccelerator/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)      988 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/globalaccelerator/_enums.py
+-rw-r--r--   0 runner    (1001) docker     (121)     5767 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/globalaccelerator/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    10239 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/globalaccelerator/accelerator.py
+-rw-r--r--   0 runner    (1001) docker     (121)    19032 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/globalaccelerator/endpoint_group.py
+-rw-r--r--   0 runner    (1001) docker     (121)     9246 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/globalaccelerator/listener.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6613 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/globalaccelerator/outputs.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 15:05:10.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/glue/
+-rw-r--r--   0 runner    (1001) docker     (121)      788 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/glue/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)      762 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/glue/_enums.py
+-rw-r--r--   0 runner    (1001) docker     (121)   102144 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/glue/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)     8634 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/glue/classifier.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6147 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/glue/connection.py
+-rw-r--r--   0 runner    (1001) docker     (121)    15883 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/glue/crawler.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7004 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/glue/data_catalog_encryption_settings.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6051 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/glue/database.py
+-rw-r--r--   0 runner    (1001) docker     (121)    17697 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/glue/dev_endpoint.py
+-rw-r--r--   0 runner    (1001) docker     (121)    20079 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/glue/job.py
+-rw-r--r--   0 runner    (1001) docker     (121)    16075 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/glue/ml_transform.py
+-rw-r--r--   0 runner    (1001) docker     (121)   105346 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/glue/outputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7912 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/glue/partition.py
+-rw-r--r--   0 runner    (1001) docker     (121)     8129 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/glue/registry.py
+-rw-r--r--   0 runner    (1001) docker     (121)    14160 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/glue/schema.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6425 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/glue/schema_version.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7088 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/glue/schema_version_metadata.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6544 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/glue/security_configuration.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6842 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/glue/table.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11587 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/glue/trigger.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7197 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/glue/workflow.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 15:05:10.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/greengrass/
+-rw-r--r--   0 runner    (1001) docker     (121)      888 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/greengrass/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    76877 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/greengrass/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7330 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/greengrass/connector_definition.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6914 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/greengrass/connector_definition_version.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7185 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/greengrass/core_definition.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6559 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/greengrass/core_definition_version.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7243 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/greengrass/device_definition.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6701 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/greengrass/device_definition_version.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7301 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/greengrass/function_definition.py
+-rw-r--r--   0 runner    (1001) docker     (121)     8039 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/greengrass/function_definition_version.py
+-rw-r--r--   0 runner    (1001) docker     (121)     8001 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/greengrass/group.py
+-rw-r--r--   0 runner    (1001) docker     (121)    13454 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/greengrass/group_version.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7243 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/greengrass/logger_definition.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6701 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/greengrass/logger_definition_version.py
+-rw-r--r--   0 runner    (1001) docker     (121)    78650 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/greengrass/outputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7301 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/greengrass/resource_definition.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6891 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/greengrass/resource_definition_version.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7417 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/greengrass/subscription_definition.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7127 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/greengrass/subscription_definition_version.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 15:05:10.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/greengrassv2/
+-rw-r--r--   0 runner    (1001) docker     (121)      353 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/greengrassv2/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)      916 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/greengrassv2/_enums.py
+-rw-r--r--   0 runner    (1001) docker     (121)    19747 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/greengrassv2/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7227 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/greengrassv2/component_version.py
+-rw-r--r--   0 runner    (1001) docker     (121)    18649 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/greengrassv2/outputs.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 15:05:10.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/groundstation/
+-rw-r--r--   0 runner    (1001) docker     (121)      412 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/groundstation/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)      827 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/groundstation/_enums.py
+-rw-r--r--   0 runner    (1001) docker     (121)    29448 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/groundstation/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6625 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/groundstation/config.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6443 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/groundstation/dataflow_endpoint_group.py
+-rw-r--r--   0 runner    (1001) docker     (121)    13896 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/groundstation/mission_profile.py
+-rw-r--r--   0 runner    (1001) docker     (121)    29162 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/groundstation/outputs.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 15:05:10.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/guardduty/
+-rw-r--r--   0 runner    (1001) docker     (121)      442 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/guardduty/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     4566 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/guardduty/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7180 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/guardduty/detector.py
+-rw-r--r--   0 runner    (1001) docker     (121)     9194 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/guardduty/filter.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7983 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/guardduty/ip_set.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6037 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/guardduty/master.py
+-rw-r--r--   0 runner    (1001) docker     (121)     8524 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/guardduty/member.py
+-rw-r--r--   0 runner    (1001) docker     (121)     4380 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/guardduty/outputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)     8190 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/guardduty/threat_intel_set.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 15:05:10.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/healthlake/
+-rw-r--r--   0 runner    (1001) docker     (121)      350 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/healthlake/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1289 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/healthlake/_enums.py
+-rw-r--r--   0 runner    (1001) docker     (121)     5261 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/healthlake/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    10619 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/healthlake/fhir_datastore.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7470 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/healthlake/outputs.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 15:05:10.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/iam/
+-rw-r--r--   0 runner    (1001) docker     (121)      668 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/iam/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    14586 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/iam/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6673 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/iam/access_key.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7924 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/iam/group.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7023 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/iam/instance_profile.py
+-rw-r--r--   0 runner    (1001) docker     (121)    10147 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/iam/managed_policy.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7711 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/iam/oidc_provider.py
+-rw-r--r--   0 runner    (1001) docker     (121)    14514 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/iam/outputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)     8310 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/iam/policy.py
+-rw-r--r--   0 runner    (1001) docker     (121)    17170 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/iam/role.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6690 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/iam/saml_provider.py
+-rw-r--r--   0 runner    (1001) docker     (121)     9569 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/iam/server_certificate.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6959 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/iam/service_linked_role.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11745 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/iam/user.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6053 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/iam/user_to_group_addition.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7622 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/iam/virtual_mfa_device.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 15:05:10.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/imagebuilder/
+-rw-r--r--   0 runner    (1001) docker     (121)      542 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/imagebuilder/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     3006 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/imagebuilder/_enums.py
+-rw-r--r--   0 runner    (1001) docker     (121)    59017 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/imagebuilder/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    15758 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/imagebuilder/component.py
+-rw-r--r--   0 runner    (1001) docker     (121)    26453 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/imagebuilder/container_recipe.py
+-rw-r--r--   0 runner    (1001) docker     (121)     9115 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/imagebuilder/distribution_configuration.py
+-rw-r--r--   0 runner    (1001) docker     (121)    15500 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/imagebuilder/image.py
+-rw-r--r--   0 runner    (1001) docker     (121)    20043 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/imagebuilder/image_pipeline.py
+-rw-r--r--   0 runner    (1001) docker     (121)    16441 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/imagebuilder/image_recipe.py
+-rw-r--r--   0 runner    (1001) docker     (121)    22089 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/imagebuilder/infrastructure_configuration.py
+-rw-r--r--   0 runner    (1001) docker     (121)    63466 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/imagebuilder/outputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1947 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/import_value.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 15:05:10.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/inspector/
+-rw-r--r--   0 runner    (1001) docker     (121)      396 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/inspector/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1774 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/inspector/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6486 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/inspector/assessment_target.py
+-rw-r--r--   0 runner    (1001) docker     (121)    10378 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/inspector/assessment_template.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1244 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/inspector/outputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)     5744 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/inspector/resource_group.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 15:05:10.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/inspectorv2/
+-rw-r--r--   0 runner    (1001) docker     (121)      342 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/inspectorv2/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)      539 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/inspectorv2/_enums.py
+-rw-r--r--   0 runner    (1001) docker     (121)    28479 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/inspectorv2/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)     8489 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/inspectorv2/filter.py
+-rw-r--r--   0 runner    (1001) docker     (121)    23568 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/inspectorv2/outputs.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 15:05:10.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/iot/
+-rw-r--r--   0 runner    (1001) docker     (121)      951 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/iot/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6607 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/iot/_enums.py
+-rw-r--r--   0 runner    (1001) docker     (121)   138789 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/iot/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    10471 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/iot/account_audit_configuration.py
+-rw-r--r--   0 runner    (1001) docker     (121)    10491 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/iot/authorizer.py
+-rw-r--r--   0 runner    (1001) docker     (121)     8798 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/iot/certificate.py
+-rw-r--r--   0 runner    (1001) docker     (121)    10572 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/iot/custom_metric.py
+-rw-r--r--   0 runner    (1001) docker     (121)     9033 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/iot/dimension.py
+-rw-r--r--   0 runner    (1001) docker     (121)    13460 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/iot/domain_configuration.py
+-rw-r--r--   0 runner    (1001) docker     (121)    16917 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/iot/fleet_metric.py
+-rw-r--r--   0 runner    (1001) docker     (121)    19655 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/iot/job_template.py
+-rw-r--r--   0 runner    (1001) docker     (121)     8097 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/iot/logging.py
+-rw-r--r--   0 runner    (1001) docker     (121)     9124 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/iot/mitigation_action.py
+-rw-r--r--   0 runner    (1001) docker     (121)   141776 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/iot/outputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)     5948 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/iot/policy.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6148 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/iot/policy_principal_attachment.py
+-rw-r--r--   0 runner    (1001) docker     (121)    10812 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/iot/provisioning_template.py
+-rw-r--r--   0 runner    (1001) docker     (121)     8493 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/iot/resource_specific_logging.py
+-rw-r--r--   0 runner    (1001) docker     (121)    13972 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/iot/scheduled_audit.py
+-rw-r--r--   0 runner    (1001) docker     (121)    15489 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/iot/security_profile.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6014 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/iot/thing.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6106 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/iot/thing_principal_attachment.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6749 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/iot/topic_rule.py
+-rw-r--r--   0 runner    (1001) docker     (121)     9032 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/iot/topic_rule_destination.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 15:05:10.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/iot1click/
+-rw-r--r--   0 runner    (1001) docker     (121)      368 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/iot1click/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1404 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/iot1click/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)     5245 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/iot1click/device.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1811 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/iot1click/outputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7546 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/iot1click/placement.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7199 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/iot1click/project.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 15:05:10.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/iotanalytics/
+-rw-r--r--   0 runner    (1001) docker     (121)      415 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/iotanalytics/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)      351 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/iotanalytics/_enums.py
+-rw-r--r--   0 runner    (1001) docker     (121)    62655 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/iotanalytics/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7599 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/iotanalytics/channel.py
+-rw-r--r--   0 runner    (1001) docker     (121)    12585 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/iotanalytics/dataset.py
+-rw-r--r--   0 runner    (1001) docker     (121)    10291 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/iotanalytics/datastore.py
+-rw-r--r--   0 runner    (1001) docker     (121)    67810 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/iotanalytics/outputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6752 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/iotanalytics/pipeline.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 15:05:10.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/iotcoredeviceadvisor/
+-rw-r--r--   0 runner    (1001) docker     (121)      330 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/iotcoredeviceadvisor/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6082 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/iotcoredeviceadvisor/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6168 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/iotcoredeviceadvisor/outputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7905 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/iotcoredeviceadvisor/suite_definition.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 15:05:10.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/iotevents/
+-rw-r--r--   0 runner    (1001) docker     (121)      371 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/iotevents/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)      443 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/iotevents/_enums.py
+-rw-r--r--   0 runner    (1001) docker     (121)    65833 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/iotevents/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    17266 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/iotevents/detector_model.py
+-rw-r--r--   0 runner    (1001) docker     (121)     9691 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/iotevents/input.py
+-rw-r--r--   0 runner    (1001) docker     (121)    71022 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/iotevents/outputs.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 15:05:10.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/iotfleethub/
+-rw-r--r--   0 runner    (1001) docker     (121)      325 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/iotfleethub/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2291 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/iotfleethub/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    12895 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/iotfleethub/application.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2119 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/iotfleethub/outputs.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 15:05:10.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/iotsitewise/
+-rw-r--r--   0 runner    (1001) docker     (121)      490 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/iotsitewise/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)      906 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/iotsitewise/_enums.py
+-rw-r--r--   0 runner    (1001) docker     (121)    38909 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/iotsitewise/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)     9784 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/iotsitewise/access_policy.py
+-rw-r--r--   0 runner    (1001) docker     (121)    10449 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/iotsitewise/asset.py
+-rw-r--r--   0 runner    (1001) docker     (121)    15383 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/iotsitewise/asset_model.py
+-rw-r--r--   0 runner    (1001) docker     (121)    10940 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/iotsitewise/dashboard.py
+-rw-r--r--   0 runner    (1001) docker     (121)    10243 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/iotsitewise/gateway.py
+-rw-r--r--   0 runner    (1001) docker     (121)    38600 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/iotsitewise/outputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    16755 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/iotsitewise/portal.py
+-rw-r--r--   0 runner    (1001) docker     (121)    10626 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/iotsitewise/project.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 15:05:10.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/iotthingsgraph/
+-rw-r--r--   0 runner    (1001) docker     (121)      327 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/iotthingsgraph/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1108 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/iotthingsgraph/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6457 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/iotthingsgraph/flow_template.py
+-rw-r--r--   0 runner    (1001) docker     (121)      831 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/iotthingsgraph/outputs.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 15:05:10.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/iotwireless/
+-rw-r--r--   0 runner    (1001) docker     (121)      590 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/iotwireless/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)      914 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/iotwireless/_enums.py
+-rw-r--r--   0 runner    (1001) docker     (121)    47400 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/iotwireless/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11099 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/iotwireless/destination.py
+-rw-r--r--   0 runner    (1001) docker     (121)     8259 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/iotwireless/device_profile.py
+-rw-r--r--   0 runner    (1001) docker     (121)    17990 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/iotwireless/fuota_task.py
+-rw-r--r--   0 runner    (1001) docker     (121)    12226 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/iotwireless/multicast_group.py
+-rw-r--r--   0 runner    (1001) docker     (121)    48563 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/iotwireless/outputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    14649 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/iotwireless/partner_account.py
+-rw-r--r--   0 runner    (1001) docker     (121)     8244 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/iotwireless/service_profile.py
+-rw-r--r--   0 runner    (1001) docker     (121)    13597 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/iotwireless/task_definition.py
+-rw-r--r--   0 runner    (1001) docker     (121)    15073 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/iotwireless/wireless_device.py
+-rw-r--r--   0 runner    (1001) docker     (121)    12439 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/iotwireless/wireless_gateway.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 15:05:10.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ivs/
+-rw-r--r--   0 runner    (1001) docker     (121)      441 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ivs/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)      855 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ivs/_enums.py
+-rw-r--r--   0 runner    (1001) docker     (121)     4521 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ivs/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    12811 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ivs/channel.py
+-rw-r--r--   0 runner    (1001) docker     (121)     3940 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ivs/outputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)     8622 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ivs/playback_key_pair.py
+-rw-r--r--   0 runner    (1001) docker     (121)     8512 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ivs/recording_configuration.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6787 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ivs/stream_key.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 15:05:10.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/kendra/
+-rw-r--r--   0 runner    (1001) docker     (121)      387 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/kendra/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     5112 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/kendra/_enums.py
+-rw-r--r--   0 runner    (1001) docker     (121)   127018 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/kendra/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11133 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/kendra/data_source.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11211 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/kendra/faq.py
+-rw-r--r--   0 runner    (1001) docker     (121)    16589 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/kendra/index.py
+-rw-r--r--   0 runner    (1001) docker     (121)   124925 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/kendra/outputs.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 15:05:10.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/kinesis/
+-rw-r--r--   0 runner    (1001) docker     (121)      373 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/kinesis/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)      575 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/kinesis/_enums.py
+-rw-r--r--   0 runner    (1001) docker     (121)     5235 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/kinesis/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6010 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/kinesis/outputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    12602 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/kinesis/stream.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6855 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/kinesis/stream_consumer.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 15:05:10.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/kinesisanalytics/
+-rw-r--r--   0 runner    (1001) docker     (121)      417 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/kinesisanalytics/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    32531 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/kinesisanalytics/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)     8210 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/kinesisanalytics/application.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6480 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/kinesisanalytics/application_output_resource.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7054 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/kinesisanalytics/application_reference_data_source.py
+-rw-r--r--   0 runner    (1001) docker     (121)    39541 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/kinesisanalytics/outputs.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 15:05:10.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/kinesisanalyticsv2/
+-rw-r--r--   0 runner    (1001) docker     (121)      471 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/kinesisanalyticsv2/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    61368 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/kinesisanalyticsv2/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11599 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/kinesisanalyticsv2/application.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7293 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/kinesisanalyticsv2/application_cloud_watch_logging_option.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6486 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/kinesisanalyticsv2/application_output_resource.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7060 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/kinesisanalyticsv2/application_reference_data_source.py
+-rw-r--r--   0 runner    (1001) docker     (121)    73933 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/kinesisanalyticsv2/outputs.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 15:05:10.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/kinesisfirehose/
+-rw-r--r--   0 runner    (1001) docker     (121)      351 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/kinesisfirehose/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     3442 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/kinesisfirehose/_enums.py
+-rw-r--r--   0 runner    (1001) docker     (121)    90575 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/kinesisfirehose/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    22145 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/kinesisfirehose/delivery_stream.py
+-rw-r--r--   0 runner    (1001) docker     (121)    91357 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/kinesisfirehose/outputs.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 15:05:10.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/kinesisvideo/
+-rw-r--r--   0 runner    (1001) docker     (121)      375 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/kinesisvideo/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)      451 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/kinesisvideo/_enums.py
+-rw-r--r--   0 runner    (1001) docker     (121)     4061 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/kinesisvideo/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)     3624 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/kinesisvideo/outputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)     9615 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/kinesisvideo/signaling_channel.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11788 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/kinesisvideo/stream.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 15:05:10.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/kms/
+-rw-r--r--   0 runner    (1001) docker     (121)      387 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/kms/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1086 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/kms/_enums.py
+-rw-r--r--   0 runner    (1001) docker     (121)     4146 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/kms/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7705 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/kms/alias.py
+-rw-r--r--   0 runner    (1001) docker     (121)    19125 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/kms/key.py
+-rw-r--r--   0 runner    (1001) docker     (121)     3694 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/kms/outputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    13977 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/kms/replica_key.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 15:05:10.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/lakeformation/
+-rw-r--r--   0 runner    (1001) docker     (121)      383 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/lakeformation/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11344 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/lakeformation/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6439 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/lakeformation/data_lake_settings.py
+-rw-r--r--   0 runner    (1001) docker     (121)    12841 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/lakeformation/outputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)     8686 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/lakeformation/permissions.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6910 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/lakeformation/resource.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 15:05:10.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/lambda_/
+-rw-r--r--   0 runner    (1001) docker     (121)      608 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/lambda_/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2138 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/lambda_/_enums.py
+-rw-r--r--   0 runner    (1001) docker     (121)    34361 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/lambda_/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    10073 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/lambda_/alias.py
+-rw-r--r--   0 runner    (1001) docker     (121)     9560 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/lambda_/code_signing_config.py
+-rw-r--r--   0 runner    (1001) docker     (121)     9508 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/lambda_/event_invoke_config.py
+-rw-r--r--   0 runner    (1001) docker     (121)    33870 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/lambda_/event_source_mapping.py
+-rw-r--r--   0 runner    (1001) docker     (121)    36104 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/lambda_/function.py
+-rw-r--r--   0 runner    (1001) docker     (121)    10024 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/lambda_/layer_version.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7902 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/lambda_/layer_version_permission.py
+-rw-r--r--   0 runner    (1001) docker     (121)    38417 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/lambda_/outputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)     9352 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/lambda_/permission.py
+-rw-r--r--   0 runner    (1001) docker     (121)    10192 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/lambda_/url.py
+-rw-r--r--   0 runner    (1001) docker     (121)     8397 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/lambda_/version.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 15:05:10.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/lex/
+-rw-r--r--   0 runner    (1001) docker     (121)      422 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/lex/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)      967 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/lex/_enums.py
+-rw-r--r--   0 runner    (1001) docker     (121)    98707 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/lex/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    16710 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/lex/bot.py
+-rw-r--r--   0 runner    (1001) docker     (121)    14259 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/lex/bot_alias.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7335 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/lex/bot_version.py
+-rw-r--r--   0 runner    (1001) docker     (121)   108415 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/lex/outputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)     5849 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/lex/resource_policy.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 15:05:10.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/licensemanager/
+-rw-r--r--   0 runner    (1001) docker     (121)      342 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/licensemanager/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     9053 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/licensemanager/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    10269 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/licensemanager/grant.py
+-rw-r--r--   0 runner    (1001) docker     (121)    16436 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/licensemanager/license.py
+-rw-r--r--   0 runner    (1001) docker     (121)     9507 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/licensemanager/outputs.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 15:05:10.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/lightsail/
+-rw-r--r--   0 runner    (1001) docker     (121)      530 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/lightsail/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)      788 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/lightsail/_enums.py
+-rw-r--r--   0 runner    (1001) docker     (121)    40687 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/lightsail/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    21321 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/lightsail/alarm.py
+-rw-r--r--   0 runner    (1001) docker     (121)    14250 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/lightsail/bucket.py
+-rw-r--r--   0 runner    (1001) docker     (121)    30830 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/lightsail/database.py
+-rw-r--r--   0 runner    (1001) docker     (121)    13526 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/lightsail/disk.py
+-rw-r--r--   0 runner    (1001) docker     (121)    21973 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/lightsail/instance.py
+-rw-r--r--   0 runner    (1001) docker     (121)    16533 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/lightsail/load_balancer.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11938 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/lightsail/load_balancer_tls_certificate.py
+-rw-r--r--   0 runner    (1001) docker     (121)    42739 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/lightsail/outputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6833 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/lightsail/static_ip.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 15:05:10.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/location/
+-rw-r--r--   0 runner    (1001) docker     (121)      488 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/location/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1571 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/location/_enums.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1442 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/location/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)     9485 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/location/geofence_collection.py
+-rw-r--r--   0 runner    (1001) docker     (121)     8315 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/location/map.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1740 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/location/outputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)     9547 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/location/place_index.py
+-rw-r--r--   0 runner    (1001) docker     (121)     8385 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/location/route_calculator.py
+-rw-r--r--   0 runner    (1001) docker     (121)    10206 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/location/tracker.py
+-rw-r--r--   0 runner    (1001) docker     (121)     5473 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/location/tracker_consumer.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 15:05:10.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/logs/
+-rw-r--r--   0 runner    (1001) docker     (121)      503 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/logs/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     3998 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/logs/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7991 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/logs/destination.py
+-rw-r--r--   0 runner    (1001) docker     (121)     9862 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/logs/log_group.py
+-rw-r--r--   0 runner    (1001) docker     (121)     5939 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/logs/log_stream.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7567 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/logs/metric_filter.py
+-rw-r--r--   0 runner    (1001) docker     (121)     3965 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/logs/outputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7769 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/logs/query_definition.py
+-rw-r--r--   0 runner    (1001) docker     (121)     5974 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/logs/resource_policy.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7949 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/logs/subscription_filter.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 15:05:10.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/lookoutequipment/
+-rw-r--r--   0 runner    (1001) docker     (121)      355 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/lookoutequipment/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)      496 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/lookoutequipment/_enums.py
+-rw-r--r--   0 runner    (1001) docker     (121)     9515 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/lookoutequipment/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    20296 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/lookoutequipment/inference_scheduler.py
+-rw-r--r--   0 runner    (1001) docker     (121)    10245 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/lookoutequipment/outputs.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 15:05:10.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/lookoutmetrics/
+-rw-r--r--   0 runner    (1001) docker     (121)      373 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/lookoutmetrics/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1182 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/lookoutmetrics/_enums.py
+-rw-r--r--   0 runner    (1001) docker     (121)    35065 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/lookoutmetrics/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    10872 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/lookoutmetrics/alert.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11516 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/lookoutmetrics/anomaly_detector.py
+-rw-r--r--   0 runner    (1001) docker     (121)    37159 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/lookoutmetrics/outputs.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 15:05:10.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/lookoutvision/
+-rw-r--r--   0 runner    (1001) docker     (121)      276 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/lookoutvision/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     4833 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/lookoutvision/project.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 15:05:10.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/macie/
+-rw-r--r--   0 runner    (1001) docker     (121)      412 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/macie/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)      822 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/macie/_enums.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1173 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/macie/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    10982 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/macie/custom_data_identifier.py
+-rw-r--r--   0 runner    (1001) docker     (121)    10161 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/macie/findings_filter.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1799 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/macie/outputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7640 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/macie/session.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 15:05:10.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/managedblockchain/
+-rw-r--r--   0 runner    (1001) docker     (121)      340 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/managedblockchain/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11486 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/managedblockchain/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)     8537 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/managedblockchain/member.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7388 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/managedblockchain/node.py
+-rw-r--r--   0 runner    (1001) docker     (121)    13285 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/managedblockchain/outputs.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 15:05:10.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/mediaconnect/
+-rw-r--r--   0 runner    (1001) docker     (121)      460 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/mediaconnect/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     3324 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/mediaconnect/_enums.py
+-rw-r--r--   0 runner    (1001) docker     (121)    40692 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/mediaconnect/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)     9724 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/mediaconnect/flow.py
+-rw-r--r--   0 runner    (1001) docker     (121)    14171 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/mediaconnect/flow_entitlement.py
+-rw-r--r--   0 runner    (1001) docker     (121)    23232 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/mediaconnect/flow_output.py
+-rw-r--r--   0 runner    (1001) docker     (121)    21461 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/mediaconnect/flow_source.py
+-rw-r--r--   0 runner    (1001) docker     (121)    10516 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/mediaconnect/flow_vpc_interface.py
+-rw-r--r--   0 runner    (1001) docker     (121)    38390 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/mediaconnect/outputs.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 15:05:10.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/mediaconvert/
+-rw-r--r--   0 runner    (1001) docker     (121)      369 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/mediaconvert/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2159 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/mediaconvert/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    13279 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/mediaconvert/job_template.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2157 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/mediaconvert/outputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)     8011 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/mediaconvert/preset.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7982 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/mediaconvert/queue.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 15:05:10.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/medialive/
+-rw-r--r--   0 runner    (1001) docker     (121)      378 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/medialive/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)   366723 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/medialive/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    15352 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/medialive/channel.py
+-rw-r--r--   0 runner    (1001) docker     (121)    13856 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/medialive/input.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6537 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/medialive/input_security_group.py
+-rw-r--r--   0 runner    (1001) docker     (121)   360164 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/medialive/outputs.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 15:05:10.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/mediapackage/
+-rw-r--r--   0 runner    (1001) docker     (121)      465 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/mediapackage/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11030 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/mediapackage/_enums.py
+-rw-r--r--   0 runner    (1001) docker     (121)   105847 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/mediapackage/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    10938 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/mediapackage/asset.py
+-rw-r--r--   0 runner    (1001) docker     (121)     9995 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/mediapackage/channel.py
+-rw-r--r--   0 runner    (1001) docker     (121)    22306 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/mediapackage/origin_endpoint.py
+-rw-r--r--   0 runner    (1001) docker     (121)   111244 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/mediapackage/outputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    13238 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/mediapackage/packaging_configuration.py
+-rw-r--r--   0 runner    (1001) docker     (121)     8804 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/mediapackage/packaging_group.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 15:05:10.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/mediastore/
+-rw-r--r--   0 runner    (1001) docker     (121)      323 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/mediastore/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6148 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/mediastore/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11191 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/mediastore/container.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6304 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/mediastore/outputs.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 15:05:10.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/memorydb/
+-rw-r--r--   0 runner    (1001) docker     (121)      441 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/memorydb/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)      400 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/memorydb/_enums.py
+-rw-r--r--   0 runner    (1001) docker     (121)    10291 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/memorydb/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7810 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/memorydb/acl.py
+-rw-r--r--   0 runner    (1001) docker     (121)    42210 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/memorydb/cluster.py
+-rw-r--r--   0 runner    (1001) docker     (121)     8410 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/memorydb/outputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    10686 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/memorydb/parameter_group.py
+-rw-r--r--   0 runner    (1001) docker     (121)     9514 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/memorydb/subnet_group.py
+-rw-r--r--   0 runner    (1001) docker     (121)     9104 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/memorydb/user.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 15:05:10.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/msk/
+-rw-r--r--   0 runner    (1001) docker     (121)      321 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/msk/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    22665 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/msk/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    15614 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/msk/cluster.py
+-rw-r--r--   0 runner    (1001) docker     (121)    24820 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/msk/outputs.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 15:05:10.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/mwaa/
+-rw-r--r--   0 runner    (1001) docker     (121)      347 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/mwaa/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)      660 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/mwaa/_enums.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7221 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/mwaa/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    25370 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/mwaa/environment.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7733 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/mwaa/outputs.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 15:05:10.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/neptune/
+-rw-r--r--   0 runner    (1001) docker     (121)      458 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/neptune/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     4844 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/neptune/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    27767 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/neptune/db_cluster.py
+-rw-r--r--   0 runner    (1001) docker     (121)     8598 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/neptune/db_cluster_parameter_group.py
+-rw-r--r--   0 runner    (1001) docker     (121)    16258 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/neptune/db_instance.py
+-rw-r--r--   0 runner    (1001) docker     (121)     8395 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/neptune/db_parameter_group.py
+-rw-r--r--   0 runner    (1001) docker     (121)     8449 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/neptune/db_subnet_group.py
+-rw-r--r--   0 runner    (1001) docker     (121)     3833 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/neptune/outputs.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 15:05:10.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/networkfirewall/
+-rw-r--r--   0 runner    (1001) docker     (121)      438 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/networkfirewall/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2144 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/networkfirewall/_enums.py
+-rw-r--r--   0 runner    (1001) docker     (121)    40623 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/networkfirewall/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    13463 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/networkfirewall/firewall.py
+-rw-r--r--   0 runner    (1001) docker     (121)     8258 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/networkfirewall/firewall_policy.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6935 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/networkfirewall/logging_configuration.py
+-rw-r--r--   0 runner    (1001) docker     (121)    42863 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/networkfirewall/outputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)     9472 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/networkfirewall/rule_group.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 15:05:10.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/networkmanager/
+-rw-r--r--   0 runner    (1001) docker     (121)      510 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/networkmanager/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     8846 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/networkmanager/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)     8840 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/networkmanager/customer_gateway_association.py
+-rw-r--r--   0 runner    (1001) docker     (121)    13969 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/networkmanager/device.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6527 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/networkmanager/global_network.py
+-rw-r--r--   0 runner    (1001) docker     (121)    12011 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/networkmanager/link.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7268 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/networkmanager/link_association.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7398 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/networkmanager/outputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)     8933 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/networkmanager/site.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7054 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/networkmanager/transit_gateway_registration.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 15:05:10.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/nimblestudio/
+-rw-r--r--   0 runner    (1001) docker     (121)      435 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/nimblestudio/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2121 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/nimblestudio/_enums.py
+-rw-r--r--   0 runner    (1001) docker     (121)    31493 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/nimblestudio/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    15571 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/nimblestudio/launch_profile.py
+-rw-r--r--   0 runner    (1001) docker     (121)    33024 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/nimblestudio/outputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11163 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/nimblestudio/streaming_image.py
+-rw-r--r--   0 runner    (1001) docker     (121)    12894 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/nimblestudio/studio.py
+-rw-r--r--   0 runner    (1001) docker     (121)    16549 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/nimblestudio/studio_component.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 15:05:10.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/opensearchservice/
+-rw-r--r--   0 runner    (1001) docker     (121)      320 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/opensearchservice/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    20703 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/opensearchservice/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    21668 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/opensearchservice/domain.py
+-rw-r--r--   0 runner    (1001) docker     (121)    25282 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/opensearchservice/outputs.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 15:05:10.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/opsworks/
+-rw-r--r--   0 runner    (1001) docker     (121)      481 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/opsworks/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    34244 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/opsworks/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    14684 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/opsworks/app.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6551 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/opsworks/elastic_load_balancer_attachment.py
+-rw-r--r--   0 runner    (1001) docker     (121)    24657 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/opsworks/instance.py
+-rw-r--r--   0 runner    (1001) docker     (121)    23481 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/opsworks/layer.py
+-rw-r--r--   0 runner    (1001) docker     (121)    31642 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/opsworks/outputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    28968 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/opsworks/stack.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7855 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/opsworks/user_profile.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7339 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/opsworks/volume.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 15:05:10.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/opsworkscm/
+-rw-r--r--   0 runner    (1001) docker     (121)      320 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/opsworkscm/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1909 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/opsworkscm/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1356 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/opsworkscm/outputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    24614 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/opsworkscm/server.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 15:05:10.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/panorama/
+-rw-r--r--   0 runner    (1001) docker     (121)      410 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/panorama/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1480 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/panorama/_enums.py
+-rw-r--r--   0 runner    (1001) docker     (121)     3344 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/panorama/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    16593 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/panorama/application_instance.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6473 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/panorama/outputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6360 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/panorama/package.py
+-rw-r--r--   0 runner    (1001) docker     (121)    10872 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/panorama/package_version.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 15:05:10.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/pinpoint/
+-rw-r--r--   0 runner    (1001) docker     (121)      874 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/pinpoint/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)      737 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/pinpoint/_enums.py
+-rw-r--r--   0 runner    (1001) docker     (121)    79028 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/pinpoint/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7604 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/pinpoint/adm_channel.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11981 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/pinpoint/apns_channel.py
+-rw-r--r--   0 runner    (1001) docker     (121)    12142 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/pinpoint/apns_sandbox_channel.py
+-rw-r--r--   0 runner    (1001) docker     (121)    12073 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/pinpoint/apns_voip_channel.py
+-rw-r--r--   0 runner    (1001) docker     (121)    12234 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/pinpoint/apns_voip_sandbox_channel.py
+-rw-r--r--   0 runner    (1001) docker     (121)     5484 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/pinpoint/app.py
+-rw-r--r--   0 runner    (1001) docker     (121)     9594 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/pinpoint/application_settings.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7555 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/pinpoint/baidu_channel.py
+-rw-r--r--   0 runner    (1001) docker     (121)    19507 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/pinpoint/campaign.py
+-rw-r--r--   0 runner    (1001) docker     (121)     9346 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/pinpoint/email_channel.py
+-rw-r--r--   0 runner    (1001) docker     (121)    10421 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/pinpoint/email_template.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7017 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/pinpoint/event_stream.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6631 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/pinpoint/gcm_channel.py
+-rw-r--r--   0 runner    (1001) docker     (121)     9263 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/pinpoint/in_app_template.py
+-rw-r--r--   0 runner    (1001) docker     (121)    76556 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/pinpoint/outputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    13258 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/pinpoint/push_template.py
+-rw-r--r--   0 runner    (1001) docker     (121)     8812 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/pinpoint/segment.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7468 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/pinpoint/sms_channel.py
+-rw-r--r--   0 runner    (1001) docker     (121)     8684 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/pinpoint/sms_template.py
+-rw-r--r--   0 runner    (1001) docker     (121)     5856 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/pinpoint/voice_channel.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 15:05:10.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/pinpointemail/
+-rw-r--r--   0 runner    (1001) docker     (121)      439 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/pinpointemail/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    15649 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/pinpointemail/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    10805 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/pinpointemail/configuration_set.py
+-rw-r--r--   0 runner    (1001) docker     (121)     8180 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/pinpointemail/configuration_set_event_destination.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6116 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/pinpointemail/dedicated_ip_pool.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11118 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/pinpointemail/identity.py
+-rw-r--r--   0 runner    (1001) docker     (121)    18780 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/pinpointemail/outputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    34730 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/provider.py
+-rw-r--r--   0 runner    (1001) docker     (121)        0 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/py.typed
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 15:05:10.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/qldb/
+-rw-r--r--   0 runner    (1001) docker     (121)      342 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/qldb/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     4046 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/qldb/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)     8473 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/qldb/ledger.py
+-rw-r--r--   0 runner    (1001) docker     (121)     3888 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/qldb/outputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11019 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/qldb/stream.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 15:05:10.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/quicksight/
+-rw-r--r--   0 runner    (1001) docker     (121)      465 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/quicksight/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     5667 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/quicksight/_enums.py
+-rw-r--r--   0 runner    (1001) docker     (121)   138391 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/quicksight/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    18097 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/quicksight/analysis.py
+-rw-r--r--   0 runner    (1001) docker     (121)    19728 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/quicksight/dashboard.py
+-rw-r--r--   0 runner    (1001) docker     (121)    22131 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/quicksight/data_set.py
+-rw-r--r--   0 runner    (1001) docker     (121)    23050 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/quicksight/data_source.py
+-rw-r--r--   0 runner    (1001) docker     (121)   171641 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/quicksight/outputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    14689 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/quicksight/template.py
+-rw-r--r--   0 runner    (1001) docker     (121)    16880 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/quicksight/theme.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 15:05:10.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ram/
+-rw-r--r--   0 runner    (1001) docker     (121)      328 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ram/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1048 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ram/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)      783 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ram/outputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    10222 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ram/resource_share.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 15:05:10.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/rds/
+-rw-r--r--   0 runner    (1001) docker     (121)      740 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/rds/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1825 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/rds/_enums.py
+-rw-r--r--   0 runner    (1001) docker     (121)    27242 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/rds/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    41151 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/rds/db_cluster.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7880 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/rds/db_cluster_parameter_group.py
+-rw-r--r--   0 runner    (1001) docker     (121)    58976 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/rds/db_instance.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7637 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/rds/db_parameter_group.py
+-rw-r--r--   0 runner    (1001) docker     (121)    19405 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/rds/db_proxy.py
+-rw-r--r--   0 runner    (1001) docker     (121)    15328 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/rds/db_proxy_endpoint.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11004 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/rds/db_proxy_target_group.py
+-rw-r--r--   0 runner    (1001) docker     (121)     8602 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/rds/db_security_group.py
+-rw-r--r--   0 runner    (1001) docker     (121)     9582 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/rds/db_security_group_ingress.py
+-rw-r--r--   0 runner    (1001) docker     (121)     8437 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/rds/db_subnet_group.py
+-rw-r--r--   0 runner    (1001) docker     (121)     8835 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/rds/event_subscription.py
+-rw-r--r--   0 runner    (1001) docker     (121)    15039 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/rds/global_cluster.py
+-rw-r--r--   0 runner    (1001) docker     (121)     9687 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/rds/option_group.py
+-rw-r--r--   0 runner    (1001) docker     (121)    24668 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/rds/outputs.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 15:05:10.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/redshift/
+-rw-r--r--   0 runner    (1001) docker     (121)      637 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/redshift/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1499 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/redshift/_enums.py
+-rw-r--r--   0 runner    (1001) docker     (121)    15066 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/redshift/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    89824 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/redshift/cluster.py
+-rw-r--r--   0 runner    (1001) docker     (121)     8565 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/redshift/cluster_parameter_group.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6262 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/redshift/cluster_security_group.py
+-rw-r--r--   0 runner    (1001) docker     (121)     8706 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/redshift/cluster_security_group_ingress.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7212 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/redshift/cluster_subnet_group.py
+-rw-r--r--   0 runner    (1001) docker     (121)    13872 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/redshift/endpoint_access.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11872 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/redshift/endpoint_authorization.py
+-rw-r--r--   0 runner    (1001) docker     (121)    18364 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/redshift/event_subscription.py
+-rw-r--r--   0 runner    (1001) docker     (121)    23295 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/redshift/outputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    15319 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/redshift/scheduled_action.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 15:05:10.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/refactorspaces/
+-rw-r--r--   0 runner    (1001) docker     (121)      418 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/refactorspaces/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1056 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/refactorspaces/_enums.py
+-rw-r--r--   0 runner    (1001) docker     (121)     9200 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/refactorspaces/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11978 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/refactorspaces/application.py
+-rw-r--r--   0 runner    (1001) docker     (121)     8794 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/refactorspaces/environment.py
+-rw-r--r--   0 runner    (1001) docker     (121)     8761 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/refactorspaces/outputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11131 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/refactorspaces/route.py
+-rw-r--r--   0 runner    (1001) docker     (121)    13394 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/refactorspaces/service.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 15:05:10.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/rekognition/
+-rw-r--r--   0 runner    (1001) docker     (121)      276 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/rekognition/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     4841 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/rekognition/project.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 15:05:10.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/resiliencehub/
+-rw-r--r--   0 runner    (1001) docker     (121)      372 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/resiliencehub/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)      750 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/resiliencehub/_enums.py
+-rw-r--r--   0 runner    (1001) docker     (121)     4578 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/resiliencehub/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11107 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/resiliencehub/app.py
+-rw-r--r--   0 runner    (1001) docker     (121)     4857 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/resiliencehub/outputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11222 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/resiliencehub/resiliency_policy.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 15:05:10.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/resourcegroups/
+-rw-r--r--   0 runner    (1001) docker     (121)      341 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/resourcegroups/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)      373 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/resourcegroups/_enums.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6958 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/resourcegroups/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)     9957 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/resourcegroups/group.py
+-rw-r--r--   0 runner    (1001) docker     (121)     5392 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/resourcegroups/outputs.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 15:05:10.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/robomaker/
+-rw-r--r--   0 runner    (1001) docker     (121)      520 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/robomaker/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1971 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/robomaker/_enums.py
+-rw-r--r--   0 runner    (1001) docker     (121)     9276 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/robomaker/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)     5602 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/robomaker/fleet.py
+-rw-r--r--   0 runner    (1001) docker     (121)     8704 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/robomaker/outputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)     9188 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/robomaker/robot.py
+-rw-r--r--   0 runner    (1001) docker     (121)     9297 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/robomaker/robot_application.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6502 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/robomaker/robot_application_version.py
+-rw-r--r--   0 runner    (1001) docker     (121)    15738 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/robomaker/simulation_application.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6587 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/robomaker/simulation_application_version.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 15:05:10.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/route53/
+-rw-r--r--   0 runner    (1001) docker     (121)      486 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/route53/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1027 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/route53/_enums.py
+-rw-r--r--   0 runner    (1001) docker     (121)    29555 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/route53/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)     4855 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/route53/dnssec.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7384 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/route53/health_check.py
+-rw-r--r--   0 runner    (1001) docker     (121)    13671 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/route53/hosted_zone.py
+-rw-r--r--   0 runner    (1001) docker     (121)    10126 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/route53/key_signing_key.py
+-rw-r--r--   0 runner    (1001) docker     (121)    28244 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/route53/outputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    17135 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/route53/record_set.py
+-rw-r--r--   0 runner    (1001) docker     (121)     8035 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/route53/record_set_group.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 15:05:10.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/route53recoverycontrol/
+-rw-r--r--   0 runner    (1001) docker     (121)      430 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/route53recoverycontrol/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1559 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/route53recoverycontrol/_enums.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11024 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/route53recoverycontrol/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7175 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/route53recoverycontrol/cluster.py
+-rw-r--r--   0 runner    (1001) docker     (121)     9254 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/route53recoverycontrol/control_panel.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11506 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/route53recoverycontrol/outputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)     8124 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/route53recoverycontrol/routing_control.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11069 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/route53recoverycontrol/safety_rule.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 15:05:10.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/route53recoveryreadiness/
+-rw-r--r--   0 runner    (1001) docker     (121)      407 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/route53recoveryreadiness/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    13774 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/route53recoveryreadiness/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)     8460 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/route53recoveryreadiness/cell.py
+-rw-r--r--   0 runner    (1001) docker     (121)    13339 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/route53recoveryreadiness/outputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)     8153 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/route53recoveryreadiness/readiness_check.py
+-rw-r--r--   0 runner    (1001) docker     (121)     8175 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/route53recoveryreadiness/recovery_group.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11957 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/route53recoveryreadiness/resource_set.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 15:05:10.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/route53resolver/
+-rw-r--r--   0 runner    (1001) docker     (121)      712 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/route53resolver/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     5158 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/route53resolver/_enums.py
+-rw-r--r--   0 runner    (1001) docker     (121)    15611 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/route53resolver/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    10726 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/route53resolver/firewall_domain_list.py
+-rw-r--r--   0 runner    (1001) docker     (121)    10503 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/route53resolver/firewall_rule_group.py
+-rw-r--r--   0 runner    (1001) docker     (121)    13570 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/route53resolver/firewall_rule_group_association.py
+-rw-r--r--   0 runner    (1001) docker     (121)    14012 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/route53resolver/outputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7845 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/route53resolver/resolver_config.py
+-rw-r--r--   0 runner    (1001) docker     (121)     5559 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/route53resolver/resolver_dnssec_config.py
+-rw-r--r--   0 runner    (1001) docker     (121)    10313 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/route53resolver/resolver_endpoint.py
+-rw-r--r--   0 runner    (1001) docker     (121)     8263 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/route53resolver/resolver_query_logging_config.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7903 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/route53resolver/resolver_query_logging_config_association.py
+-rw-r--r--   0 runner    (1001) docker     (121)    14237 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/route53resolver/resolver_rule.py
+-rw-r--r--   0 runner    (1001) docker     (121)     8054 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/route53resolver/resolver_rule_association.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 15:05:10.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/rum/
+-rw-r--r--   0 runner    (1001) docker     (121)      347 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/rum/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)      345 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/rum/_enums.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11315 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/rum/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    10462 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/rum/app_monitor.py
+-rw-r--r--   0 runner    (1001) docker     (121)    10301 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/rum/outputs.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 15:05:10.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/s3/
+-rw-r--r--   0 runner    (1001) docker     (121)      516 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/s3/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     8282 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/s3/_enums.py
+-rw-r--r--   0 runner    (1001) docker     (121)   141353 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/s3/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    14416 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/s3/access_point.py
+-rw-r--r--   0 runner    (1001) docker     (121)    39434 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/s3/bucket.py
+-rw-r--r--   0 runner    (1001) docker     (121)     5801 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/s3/bucket_policy.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11380 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/s3/multi_region_access_point.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6572 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/s3/multi_region_access_point_policy.py
+-rw-r--r--   0 runner    (1001) docker     (121)   147485 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/s3/outputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6674 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/s3/storage_lens.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 15:05:10.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/s3objectlambda/
+-rw-r--r--   0 runner    (1001) docker     (121)      361 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/s3objectlambda/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     4335 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/s3objectlambda/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)     8892 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/s3objectlambda/access_point.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7746 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/s3objectlambda/access_point_policy.py
+-rw-r--r--   0 runner    (1001) docker     (121)    13130 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/s3objectlambda/outputs.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 15:05:10.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/s3outposts/
+-rw-r--r--   0 runner    (1001) docker     (121)      423 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/s3outposts/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)      811 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/s3outposts/_enums.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11970 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/s3outposts/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)     8960 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/s3outposts/access_point.py
+-rw-r--r--   0 runner    (1001) docker     (121)     9537 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/s3outposts/bucket.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6067 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/s3outposts/bucket_policy.py
+-rw-r--r--   0 runner    (1001) docker     (121)    12847 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/s3outposts/endpoint.py
+-rw-r--r--   0 runner    (1001) docker     (121)    13452 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/s3outposts/outputs.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 15:05:10.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/sagemaker/
+-rw-r--r--   0 runner    (1001) docker     (121)     1060 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/sagemaker/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    12570 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/sagemaker/_enums.py
+-rw-r--r--   0 runner    (1001) docker     (121)   278376 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/sagemaker/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11221 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/sagemaker/app.py
+-rw-r--r--   0 runner    (1001) docker     (121)     8661 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/sagemaker/app_image_config.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7322 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/sagemaker/code_repository.py
+-rw-r--r--   0 runner    (1001) docker     (121)    18433 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/sagemaker/data_quality_job_definition.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7417 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/sagemaker/device.py
+-rw-r--r--   0 runner    (1001) docker     (121)    10186 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/sagemaker/device_fleet.py
+-rw-r--r--   0 runner    (1001) docker     (121)    16764 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/sagemaker/domain.py
+-rw-r--r--   0 runner    (1001) docker     (121)    12068 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/sagemaker/endpoint.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11063 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/sagemaker/endpoint_config.py
+-rw-r--r--   0 runner    (1001) docker     (121)    15772 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/sagemaker/feature_group.py
+-rw-r--r--   0 runner    (1001) docker     (121)     8858 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/sagemaker/image.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6353 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/sagemaker/image_version.py
+-rw-r--r--   0 runner    (1001) docker     (121)    12567 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/sagemaker/model.py
+-rw-r--r--   0 runner    (1001) docker     (121)    18109 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/sagemaker/model_bias_job_definition.py
+-rw-r--r--   0 runner    (1001) docker     (121)    19729 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/sagemaker/model_explainability_job_definition.py
+-rw-r--r--   0 runner    (1001) docker     (121)     9671 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/sagemaker/model_package_group.py
+-rw-r--r--   0 runner    (1001) docker     (121)    18595 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/sagemaker/model_quality_job_definition.py
+-rw-r--r--   0 runner    (1001) docker     (121)    14819 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/sagemaker/monitoring_schedule.py
+-rw-r--r--   0 runner    (1001) docker     (121)    19239 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/sagemaker/notebook_instance.py
+-rw-r--r--   0 runner    (1001) docker     (121)     8716 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/sagemaker/notebook_instance_lifecycle_config.py
+-rw-r--r--   0 runner    (1001) docker     (121)   310639 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/sagemaker/outputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    10339 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/sagemaker/pipeline.py
+-rw-r--r--   0 runner    (1001) docker     (121)    10701 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/sagemaker/project.py
+-rw-r--r--   0 runner    (1001) docker     (121)    13902 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/sagemaker/user_profile.py
+-rw-r--r--   0 runner    (1001) docker     (121)     9481 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/sagemaker/workteam.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 15:05:10.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/sdb/
+-rw-r--r--   0 runner    (1001) docker     (121)      275 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/sdb/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     4824 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/sdb/domain.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 15:05:10.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/secretsmanager/
+-rw-r--r--   0 runner    (1001) docker     (121)      424 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/secretsmanager/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    12914 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/secretsmanager/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    12515 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/secretsmanager/outputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6972 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/secretsmanager/resource_policy.py
+-rw-r--r--   0 runner    (1001) docker     (121)     8622 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/secretsmanager/rotation_schedule.py
+-rw-r--r--   0 runner    (1001) docker     (121)    10780 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/secretsmanager/secret.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7005 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/secretsmanager/secret_target_attachment.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 15:05:10.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/securityhub/
+-rw-r--r--   0 runner    (1001) docker     (121)      272 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/securityhub/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     4597 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/securityhub/hub.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 15:05:10.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/servicecatalog/
+-rw-r--r--   0 runner    (1001) docker     (121)      938 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/servicecatalog/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)      862 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/servicecatalog/_enums.py
+-rw-r--r--   0 runner    (1001) docker     (121)    10886 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/servicecatalog/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6234 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/servicecatalog/accepted_portfolio_share.py
+-rw-r--r--   0 runner    (1001) docker     (121)    16111 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/servicecatalog/cloud_formation_product.py
+-rw-r--r--   0 runner    (1001) docker     (121)    18259 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/servicecatalog/cloud_formation_provisioned_product.py
+-rw-r--r--   0 runner    (1001) docker     (121)     9209 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/servicecatalog/launch_notification_constraint.py
+-rw-r--r--   0 runner    (1001) docker     (121)     9612 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/servicecatalog/launch_role_constraint.py
+-rw-r--r--   0 runner    (1001) docker     (121)     8733 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/servicecatalog/launch_template_constraint.py
+-rw-r--r--   0 runner    (1001) docker     (121)     9305 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/servicecatalog/outputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)     8965 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/servicecatalog/portfolio.py
+-rw-r--r--   0 runner    (1001) docker     (121)     8284 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/servicecatalog/portfolio_principal_association.py
+-rw-r--r--   0 runner    (1001) docker     (121)     8225 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/servicecatalog/portfolio_product_association.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7896 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/servicecatalog/portfolio_share.py
+-rw-r--r--   0 runner    (1001) docker     (121)     9285 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/servicecatalog/resource_update_constraint.py
+-rw-r--r--   0 runner    (1001) docker     (121)     8621 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/servicecatalog/service_action.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6843 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/servicecatalog/service_action_association.py
+-rw-r--r--   0 runner    (1001) docker     (121)    12888 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/servicecatalog/stack_set_constraint.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6315 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/servicecatalog/tag_option.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6174 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/servicecatalog/tag_option_association.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 15:05:10.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/servicecatalogappregistry/
+-rw-r--r--   0 runner    (1001) docker     (121)      457 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/servicecatalogappregistry/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)      403 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/servicecatalogappregistry/_enums.py
+-rw-r--r--   0 runner    (1001) docker     (121)      592 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/servicecatalogappregistry/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6796 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/servicecatalogappregistry/application.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7660 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/servicecatalogappregistry/attribute_group.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6905 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/servicecatalogappregistry/attribute_group_association.py
+-rw-r--r--   0 runner    (1001) docker     (121)      590 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/servicecatalogappregistry/outputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)     8141 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/servicecatalogappregistry/resource_association.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 15:05:10.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/servicediscovery/
+-rw-r--r--   0 runner    (1001) docker     (121)      448 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/servicediscovery/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11391 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/servicediscovery/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6955 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/servicediscovery/http_namespace.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6182 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/servicediscovery/instance.py
+-rw-r--r--   0 runner    (1001) docker     (121)    14043 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/servicediscovery/outputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)     8869 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/servicediscovery/private_dns_namespace.py
+-rw-r--r--   0 runner    (1001) docker     (121)     8128 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/servicediscovery/public_dns_namespace.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11923 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/servicediscovery/service.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 15:05:10.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ses/
+-rw-r--r--   0 runner    (1001) docker     (121)      524 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ses/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    29409 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ses/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)     4636 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ses/configuration_set.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7093 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ses/configuration_set_event_destination.py
+-rw-r--r--   0 runner    (1001) docker     (121)     8886 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ses/contact_list.py
+-rw-r--r--   0 runner    (1001) docker     (121)    31210 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ses/outputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)     5141 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ses/receipt_filter.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6692 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ses/receipt_rule.py
+-rw-r--r--   0 runner    (1001) docker     (121)     5080 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ses/receipt_rule_set.py
+-rw-r--r--   0 runner    (1001) docker     (121)     5009 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ses/template.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 15:05:10.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/signer/
+-rw-r--r--   0 runner    (1001) docker     (121)      385 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/signer/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)      509 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/signer/_enums.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2239 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/signer/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1626 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/signer/outputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)     8084 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/signer/profile_permission.py
+-rw-r--r--   0 runner    (1001) docker     (121)     9975 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/signer/signing_profile.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 15:05:10.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/sns/
+-rw-r--r--   0 runner    (1001) docker     (121)      375 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/sns/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1814 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/sns/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1260 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/sns/outputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11878 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/sns/subscription.py
+-rw-r--r--   0 runner    (1001) docker     (121)    10758 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/sns/topic.py
+-rw-r--r--   0 runner    (1001) docker     (121)     5911 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/sns/topic_policy.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 15:05:10.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/sqs/
+-rw-r--r--   0 runner    (1001) docker     (121)      347 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/sqs/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1032 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/sqs/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)      767 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/sqs/outputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    19248 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/sqs/queue.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7745 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/sqs/queue_policy.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 15:05:10.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ssm/
+-rw-r--r--   0 runner    (1001) docker     (121)      574 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ssm/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1725 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ssm/_enums.py
+-rw-r--r--   0 runner    (1001) docker     (121)    39156 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ssm/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    23030 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ssm/association.py
+-rw-r--r--   0 runner    (1001) docker     (121)    17501 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ssm/document.py
+-rw-r--r--   0 runner    (1001) docker     (121)    13923 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ssm/maintenance_window.py
+-rw-r--r--   0 runner    (1001) docker     (121)     9866 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ssm/maintenance_window_target.py
+-rw-r--r--   0 runner    (1001) docker     (121)    17445 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ssm/maintenance_window_task.py
+-rw-r--r--   0 runner    (1001) docker     (121)    37739 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ssm/outputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    10939 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ssm/parameter.py
+-rw-r--r--   0 runner    (1001) docker     (121)    17770 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ssm/patch_baseline.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11348 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ssm/resource_data_sync.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 15:05:10.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ssmcontacts/
+-rw-r--r--   0 runner    (1001) docker     (121)      374 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ssmcontacts/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)      776 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ssmcontacts/_enums.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6522 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ssmcontacts/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)     9925 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ssmcontacts/contact.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11451 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ssmcontacts/contact_channel.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7998 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ssmcontacts/outputs.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 15:05:10.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ssmincidents/
+-rw-r--r--   0 runner    (1001) docker     (121)      380 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ssmincidents/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)      504 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ssmincidents/_enums.py
+-rw-r--r--   0 runner    (1001) docker     (121)    13071 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ssmincidents/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    14618 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ssmincidents/outputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6515 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ssmincidents/replication_set.py
+-rw-r--r--   0 runner    (1001) docker     (121)    12442 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ssmincidents/response_plan.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 15:05:10.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/sso/
+-rw-r--r--   0 runner    (1001) docker     (121)      439 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/sso/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)      555 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/sso/_enums.py
+-rw-r--r--   0 runner    (1001) docker     (121)     4035 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/sso/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11511 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/sso/assignment.py
+-rw-r--r--   0 runner    (1001) docker     (121)    10311 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/sso/instance_access_control_attribute_configuration.py
+-rw-r--r--   0 runner    (1001) docker     (121)     4007 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/sso/outputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    13467 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/sso/permission_set.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 15:05:10.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/stepfunctions/
+-rw-r--r--   0 runner    (1001) docker     (121)      373 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/stepfunctions/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)      492 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/stepfunctions/_enums.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7030 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/stepfunctions/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)     5421 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/stepfunctions/activity.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6809 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/stepfunctions/outputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    15052 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/stepfunctions/state_machine.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 15:05:10.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/synthetics/
+-rw-r--r--   0 runner    (1001) docker     (121)      320 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/synthetics/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    15548 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/synthetics/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    22631 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/synthetics/canary.py
+-rw-r--r--   0 runner    (1001) docker     (121)    16825 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/synthetics/outputs.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 15:05:10.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/timestream/
+-rw-r--r--   0 runner    (1001) docker     (121)      396 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/timestream/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1354 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/timestream/_enums.py
+-rw-r--r--   0 runner    (1001) docker     (121)    22951 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/timestream/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)     8462 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/timestream/database.py
+-rw-r--r--   0 runner    (1001) docker     (121)    27061 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/timestream/outputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    19901 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/timestream/scheduled_query.py
+-rw-r--r--   0 runner    (1001) docker     (121)    10098 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/timestream/table.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 15:05:10.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/transfer/
+-rw-r--r--   0 runner    (1001) docker     (121)      386 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/transfer/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)      647 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/transfer/_enums.py
+-rw-r--r--   0 runner    (1001) docker     (121)    26737 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/transfer/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    26607 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/transfer/outputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    16631 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/transfer/server.py
+-rw-r--r--   0 runner    (1001) docker     (121)    13858 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/transfer/user.py
+-rw-r--r--   0 runner    (1001) docker     (121)    10485 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/transfer/workflow.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 15:05:10.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/waf/
+-rw-r--r--   0 runner    (1001) docker     (121)      496 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/waf/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    13594 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/waf/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6191 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/waf/byte_match_set.py
+-rw-r--r--   0 runner    (1001) docker     (121)     5998 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/waf/ip_set.py
+-rw-r--r--   0 runner    (1001) docker     (121)    13226 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/waf/outputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6649 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/waf/rule.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6349 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/waf/size_constraint_set.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6631 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/waf/sql_injection_match_set.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7753 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/waf/web_acl.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6167 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/waf/xss_match_set.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 15:05:10.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/wafregional/
+-rw-r--r--   0 runner    (1001) docker     (121)      623 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/wafregional/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    15337 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/wafregional/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6215 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/wafregional/byte_match_set.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6282 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/wafregional/geo_match_set.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6022 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/wafregional/ip_set.py
+-rw-r--r--   0 runner    (1001) docker     (121)    14849 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/wafregional/outputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)     8796 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/wafregional/rate_based_rule.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6131 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/wafregional/regex_pattern_set.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6673 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/wafregional/rule.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6344 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/wafregional/size_constraint_set.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6655 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/wafregional/sql_injection_match_set.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7705 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/wafregional/web_acl.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6058 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/wafregional/web_aclassociation.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6162 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/wafregional/xss_match_set.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 15:05:10.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/wafv2/
+-rw-r--r--   0 runner    (1001) docker     (121)      495 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/wafv2/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     8780 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/wafv2/_enums.py
+-rw-r--r--   0 runner    (1001) docker     (121)   145232 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/wafv2/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)     9482 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/wafv2/ip_set.py
+-rw-r--r--   0 runner    (1001) docker     (121)    12135 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/wafv2/logging_configuration.py
+-rw-r--r--   0 runner    (1001) docker     (121)   149784 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/wafv2/outputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)     9998 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/wafv2/regex_pattern_set.py
+-rw-r--r--   0 runner    (1001) docker     (121)    13802 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/wafv2/rule_group.py
+-rw-r--r--   0 runner    (1001) docker     (121)    14501 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/wafv2/web_acl.py
+-rw-r--r--   0 runner    (1001) docker     (121)     5515 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/wafv2/web_aclassociation.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 15:05:10.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/wisdom/
+-rw-r--r--   0 runner    (1001) docker     (121)      412 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/wisdom/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)      529 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/wisdom/_enums.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6771 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/wisdom/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)     9009 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/wisdom/assistant.py
+-rw-r--r--   0 runner    (1001) docker     (121)     8964 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/wisdom/assistant_association.py
+-rw-r--r--   0 runner    (1001) docker     (121)    12120 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/wisdom/knowledge_base.py
+-rw-r--r--   0 runner    (1001) docker     (121)     8652 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/wisdom/outputs.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 15:05:10.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/workspaces/
+-rw-r--r--   0 runner    (1001) docker     (121)      377 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/workspaces/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)      744 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/workspaces/_enums.py
+-rw-r--r--   0 runner    (1001) docker     (121)     4716 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/workspaces/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6568 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/workspaces/connection_alias.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6594 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/workspaces/outputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    12348 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/workspaces/workspace.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 15:05:10.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/xray/
+-rw-r--r--   0 runner    (1001) docker     (121)      348 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/xray/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    20512 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/xray/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)     8835 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/xray/group.py
+-rw-r--r--   0 runner    (1001) docker     (121)    18816 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/xray/outputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)     9208 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/xray/sampling_rule.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-10 15:05:10.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (121)     3304 2022-01-10 15:05:10.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (121)    66269 2022-01-10 15:05:10.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (121)        1 2022-01-10 15:05:10.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (121)        1 2022-01-10 15:05:10.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native.egg-info/not-zip-safe
+-rw-r--r--   0 runner    (1001) docker     (121)       49 2022-01-10 15:05:10.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (121)       18 2022-01-10 15:05:10.000000 pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native.egg-info/top_level.txt
+-rw-r--r--   0 runner    (1001) docker     (121)       38 2022-01-10 15:05:10.000000 pulumi_aws_native-0.9.1a1641826769/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (121)     2156 2022-01-10 15:05:09.000000 pulumi_aws_native-0.9.1a1641826769/setup.py
```

### Comparing `pulumi_aws_native-0.9.1a1641824984/PKG-INFO` & `pulumi_aws_native-0.9.1a1641826769/PKG-INFO`

 * *Files 2% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: pulumi_aws_native
-Version: 0.9.1a1641824984
+Version: 0.9.1a1641826769
 Summary: A native Pulumi package for creating and managing Amazon Web Services (AWS) resources.
 Home-page: https://pulumi.com
 License: Apache-2.0
 Project-URL: Repository, https://github.com/pulumi/pulumi-aws-native
 Description: # Pulumi AWS Native Provider (preview)
         
         The Pulumi AWS Native Provider enables you to build, deploy, and manage [any AWS resource that's supported by the AWS Cloud Control API](https://github.com/pulumi/pulumi-aws-native/blob/master/provider/cmd/pulumi-gen-aws-native/supported-types.txt).
```

### Comparing `pulumi_aws_native-0.9.1a1641824984/README.md` & `pulumi_aws_native-0.9.1a1641826769/README.md`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/__init__.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/__init__.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/_enums.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/_enums.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/_inputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/_utilities.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/_utilities.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/accessanalyzer/_inputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/accessanalyzer/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/accessanalyzer/analyzer.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/accessanalyzer/analyzer.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/accessanalyzer/outputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/accessanalyzer/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/acmpca/_inputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/acmpca/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/acmpca/certificate.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/acmpca/certificate.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/acmpca/certificate_authority.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/acmpca/certificate_authority.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/acmpca/certificate_authority_activation.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/acmpca/certificate_authority_activation.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/acmpca/outputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/acmpca/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/acmpca/permission.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/acmpca/permission.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/amazonmq/_inputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/amazonmq/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/amazonmq/broker.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/amazonmq/broker.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/amazonmq/configuration.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/amazonmq/configuration.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/amazonmq/configuration_association.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/amazonmq/configuration_association.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/amazonmq/outputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/amazonmq/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/amplify/_enums.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/amplify/_enums.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/amplify/_inputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/amplify/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/amplify/app.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/amplify/app.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/amplify/branch.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/amplify/branch.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/amplify/domain.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/amplify/domain.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/amplify/outputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/amplify/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/amplifyuibuilder/_inputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/amplifyuibuilder/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/amplifyuibuilder/component.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/amplifyuibuilder/component.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/amplifyuibuilder/outputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/amplifyuibuilder/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/amplifyuibuilder/theme.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/amplifyuibuilder/theme.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/apigateway/__init__.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/apigateway/__init__.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/apigateway/_enums.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/apigateway/_enums.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/apigateway/_inputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/apigateway/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/apigateway/account.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/apigateway/account.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/apigateway/api_key.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/apigateway/api_key.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/apigateway/authorizer.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/apigateway/authorizer.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/apigateway/base_path_mapping.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/apigateway/base_path_mapping.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/apigateway/client_certificate.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/apigateway/client_certificate.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/apigateway/deployment.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/apigateway/deployment.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/apigateway/documentation_part.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/apigateway/documentation_part.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/apigateway/documentation_version.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/apigateway/documentation_version.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/apigateway/domain_name.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/apigateway/domain_name.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/apigateway/gateway_response.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/apigateway/gateway_response.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/apigateway/method.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/apigateway/method.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/apigateway/model.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/apigateway/model.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/apigateway/outputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/apigateway/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/apigateway/request_validator.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/apigateway/request_validator.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/apigateway/resource.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/apigateway/resource.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/apigateway/rest_api.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/apigateway/rest_api.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/apigateway/stage.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/apigateway/stage.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/apigateway/usage_plan.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/apigateway/usage_plan.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/apigateway/usage_plan_key.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/apigateway/usage_plan_key.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/apigateway/vpc_link.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/apigateway/vpc_link.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/apigatewayv2/__init__.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/apigatewayv2/__init__.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/apigatewayv2/_inputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/apigatewayv2/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/apigatewayv2/api.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/apigatewayv2/api.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/apigatewayv2/api_gateway_managed_overrides.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/apigatewayv2/api_gateway_managed_overrides.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/apigatewayv2/api_mapping.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/apigatewayv2/api_mapping.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/apigatewayv2/authorizer.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/apigatewayv2/authorizer.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/apigatewayv2/deployment.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/apigatewayv2/deployment.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/apigatewayv2/domain_name.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/apigatewayv2/domain_name.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/apigatewayv2/integration.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/apigatewayv2/integration.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/apigatewayv2/integration_response.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/apigatewayv2/integration_response.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/apigatewayv2/model.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/apigatewayv2/model.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/apigatewayv2/outputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/apigatewayv2/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/apigatewayv2/route.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/apigatewayv2/route.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/apigatewayv2/route_response.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/apigatewayv2/route_response.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/apigatewayv2/stage.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/apigatewayv2/stage.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/apigatewayv2/vpc_link.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/apigatewayv2/vpc_link.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/appconfig/_inputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/appconfig/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/appconfig/application.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/appconfig/application.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/appconfig/configuration_profile.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/appconfig/configuration_profile.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/appconfig/deployment.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/appconfig/deployment.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/appconfig/deployment_strategy.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/appconfig/deployment_strategy.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/appconfig/environment.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/appconfig/environment.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/appconfig/hosted_configuration_version.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/appconfig/hosted_configuration_version.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/appconfig/outputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/appconfig/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/appflow/_enums.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/appflow/_enums.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/appflow/_inputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/appflow/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/appflow/connector_profile.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/appflow/connector_profile.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/appflow/flow.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/appflow/flow.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/appflow/outputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/appflow/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/appintegrations/_inputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/appintegrations/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/appintegrations/event_integration.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/appintegrations/event_integration.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/appintegrations/outputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/appintegrations/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/applicationautoscaling/_inputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/applicationautoscaling/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/applicationautoscaling/outputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/applicationautoscaling/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/applicationautoscaling/scalable_target.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/applicationautoscaling/scalable_target.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/applicationautoscaling/scaling_policy.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/applicationautoscaling/scaling_policy.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/applicationinsights/_enums.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/applicationinsights/_enums.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/applicationinsights/_inputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/applicationinsights/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/applicationinsights/application.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/applicationinsights/application.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/applicationinsights/outputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/applicationinsights/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/appmesh/_inputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/appmesh/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/appmesh/gateway_route.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/appmesh/gateway_route.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/appmesh/mesh.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/appmesh/mesh.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/appmesh/outputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/appmesh/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/appmesh/route.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/appmesh/route.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/appmesh/virtual_gateway.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/appmesh/virtual_gateway.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/appmesh/virtual_node.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/appmesh/virtual_node.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/appmesh/virtual_router.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/appmesh/virtual_router.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/appmesh/virtual_service.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/appmesh/virtual_service.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/apprunner/_enums.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/apprunner/_enums.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/apprunner/_inputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/apprunner/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/apprunner/outputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/apprunner/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/apprunner/service.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/apprunner/service.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/appstream/__init__.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/appstream/__init__.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/appstream/_inputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/appstream/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/appstream/app_block.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/appstream/app_block.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/appstream/application.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/appstream/application.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/appstream/application_entitlement_association.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/appstream/application_entitlement_association.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/appstream/application_fleet_association.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/appstream/application_fleet_association.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/appstream/directory_config.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/appstream/directory_config.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/appstream/entitlement.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/appstream/entitlement.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/appstream/fleet.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/appstream/fleet.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/appstream/image_builder.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/appstream/image_builder.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/appstream/outputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/appstream/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/appstream/stack.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/appstream/stack.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/appstream/stack_fleet_association.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/appstream/stack_fleet_association.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/appstream/stack_user_association.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/appstream/stack_user_association.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/appstream/user.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/appstream/user.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/appsync/__init__.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/appsync/__init__.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/appsync/_inputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/appsync/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/appsync/api_cache.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/appsync/api_cache.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/appsync/api_key.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/appsync/api_key.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/appsync/data_source.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/appsync/data_source.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/appsync/domain_name.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/appsync/domain_name.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/appsync/domain_name_api_association.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/appsync/domain_name_api_association.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/appsync/function_configuration.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/appsync/function_configuration.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/appsync/graph_ql_api.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/appsync/graph_ql_api.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/appsync/graph_ql_schema.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/appsync/graph_ql_schema.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/appsync/outputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/appsync/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/appsync/resolver.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/appsync/resolver.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/aps/_inputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/aps/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/aps/outputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/aps/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/aps/rule_groups_namespace.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/aps/rule_groups_namespace.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/aps/workspace.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/aps/workspace.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ask/_inputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ask/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ask/outputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ask/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ask/skill.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ask/skill.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/athena/_enums.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/athena/_enums.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/athena/_inputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/athena/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/athena/data_catalog.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/athena/data_catalog.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/athena/named_query.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/athena/named_query.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/athena/outputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/athena/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/athena/prepared_statement.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/athena/prepared_statement.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/athena/work_group.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/athena/work_group.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/auditmanager/_enums.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/auditmanager/_enums.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/auditmanager/_inputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/auditmanager/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/auditmanager/assessment.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/auditmanager/assessment.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/auditmanager/outputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/auditmanager/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/autoscaling/_inputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/autoscaling/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/autoscaling/auto_scaling_group.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/autoscaling/auto_scaling_group.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/autoscaling/launch_configuration.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/autoscaling/launch_configuration.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/autoscaling/lifecycle_hook.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/autoscaling/lifecycle_hook.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/autoscaling/outputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/autoscaling/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/autoscaling/scaling_policy.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/autoscaling/scaling_policy.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/autoscaling/scheduled_action.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/autoscaling/scheduled_action.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/autoscaling/warm_pool.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/autoscaling/warm_pool.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/autoscalingplans/_inputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/autoscalingplans/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/autoscalingplans/outputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/autoscalingplans/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/autoscalingplans/scaling_plan.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/autoscalingplans/scaling_plan.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/backup/_inputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/backup/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/backup/backup_plan.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/backup/backup_plan.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/backup/backup_selection.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/backup/backup_selection.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/backup/backup_vault.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/backup/backup_vault.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/backup/framework.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/backup/framework.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/backup/outputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/backup/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/backup/report_plan.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/backup/report_plan.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/batch/_inputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/batch/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/batch/compute_environment.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/batch/compute_environment.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/batch/job_definition.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/batch/job_definition.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/batch/job_queue.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/batch/job_queue.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/batch/outputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/batch/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/batch/scheduling_policy.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/batch/scheduling_policy.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/budgets/_enums.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/budgets/_enums.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/budgets/_inputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/budgets/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/budgets/budget.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/budgets/budget.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/budgets/budgets_action.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/budgets/budgets_action.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/budgets/outputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/budgets/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/cassandra/_enums.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/cassandra/_enums.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/cassandra/_inputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/cassandra/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/cassandra/keyspace.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/cassandra/keyspace.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/cassandra/outputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/cassandra/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/cassandra/table.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/cassandra/table.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ce/_enums.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ce/_enums.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ce/_inputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ce/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ce/anomaly_monitor.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ce/anomaly_monitor.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ce/anomaly_subscription.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ce/anomaly_subscription.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ce/cost_category.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ce/cost_category.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ce/outputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ce/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/certificatemanager/_inputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/certificatemanager/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/certificatemanager/account.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/certificatemanager/account.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/certificatemanager/certificate.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/certificatemanager/certificate.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/certificatemanager/outputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/certificatemanager/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/chatbot/slack_channel_configuration.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/chatbot/slack_channel_configuration.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/cidr.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/cidr.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/cloud9/_inputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/cloud9/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/cloud9/environment_ec2.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/cloud9/environment_ec2.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/cloud9/outputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/cloud9/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/cloudformation/__init__.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/cloudformation/__init__.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/cloudformation/_enums.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/cloudformation/_enums.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/cloudformation/_inputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/cloudformation/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/cloudformation/custom_resource.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/cloudformation/custom_resource.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/cloudformation/macro.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/cloudformation/macro.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/cloudformation/module_default_version.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/cloudformation/module_default_version.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/cloudformation/module_version.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/cloudformation/module_version.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/cloudformation/outputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/cloudformation/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/cloudformation/public_type_version.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/cloudformation/public_type_version.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/cloudformation/publisher.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/cloudformation/publisher.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/cloudformation/resource_default_version.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/cloudformation/resource_default_version.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/cloudformation/resource_version.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/cloudformation/resource_version.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/cloudformation/stack.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/cloudformation/stack.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/cloudformation/stack_set.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/cloudformation/stack_set.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/cloudformation/type_activation.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/cloudformation/type_activation.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/cloudformation/wait_condition.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/cloudformation/wait_condition.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/cloudformation/wait_condition_handle.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/cloudformation/wait_condition_handle.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/cloudfront/__init__.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/cloudfront/__init__.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/cloudfront/_inputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/cloudfront/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/cloudfront/cache_policy.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/cloudfront/cache_policy.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/cloudfront/cloud_front_origin_access_identity.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/cloudfront/cloud_front_origin_access_identity.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/cloudfront/distribution.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/cloudfront/distribution.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/cloudfront/function.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/cloudfront/function.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/cloudfront/key_group.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/cloudfront/key_group.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/cloudfront/origin_request_policy.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/cloudfront/origin_request_policy.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/cloudfront/outputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/cloudfront/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/cloudfront/public_key.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/cloudfront/public_key.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/cloudfront/realtime_log_config.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/cloudfront/realtime_log_config.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/cloudfront/response_headers_policy.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/cloudfront/response_headers_policy.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/cloudfront/streaming_distribution.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/cloudfront/streaming_distribution.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/cloudtrail/_enums.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/cloudtrail/_enums.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/cloudtrail/_inputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/cloudtrail/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/cloudtrail/outputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/cloudtrail/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/cloudtrail/trail.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/cloudtrail/trail.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/cloudwatch/_inputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/cloudwatch/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/cloudwatch/alarm.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/cloudwatch/alarm.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/cloudwatch/anomaly_detector.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/cloudwatch/anomaly_detector.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/cloudwatch/composite_alarm.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/cloudwatch/composite_alarm.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/cloudwatch/dashboard.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/cloudwatch/dashboard.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/cloudwatch/insight_rule.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/cloudwatch/insight_rule.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/cloudwatch/metric_stream.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/cloudwatch/metric_stream.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/cloudwatch/outputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/cloudwatch/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/codeartifact/_inputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/codeartifact/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/codeartifact/domain.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/codeartifact/domain.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/codeartifact/outputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/codeartifact/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/codeartifact/repository.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/codeartifact/repository.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/codebuild/_inputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/codebuild/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/codebuild/outputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/codebuild/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/codebuild/project.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/codebuild/project.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/codebuild/report_group.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/codebuild/report_group.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/codebuild/source_credential.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/codebuild/source_credential.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/codecommit/_inputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/codecommit/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/codecommit/outputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/codecommit/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/codecommit/repository.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/codecommit/repository.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/codedeploy/_inputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/codedeploy/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/codedeploy/application.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/codedeploy/application.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/codedeploy/deployment_config.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/codedeploy/deployment_config.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/codedeploy/deployment_group.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/codedeploy/deployment_group.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/codedeploy/outputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/codedeploy/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/codeguruprofiler/_inputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/codeguruprofiler/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/codeguruprofiler/outputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/codeguruprofiler/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/codeguruprofiler/profiling_group.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/codeguruprofiler/profiling_group.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/codegurureviewer/_inputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/codegurureviewer/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/codegurureviewer/outputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/codegurureviewer/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/codegurureviewer/repository_association.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/codegurureviewer/repository_association.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/codepipeline/_inputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/codepipeline/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/codepipeline/custom_action_type.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/codepipeline/custom_action_type.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/codepipeline/outputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/codepipeline/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/codepipeline/pipeline.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/codepipeline/pipeline.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/codepipeline/webhook.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/codepipeline/webhook.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/codestar/_inputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/codestar/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/codestar/git_hub_repository.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/codestar/git_hub_repository.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/codestar/outputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/codestar/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/codestarconnections/_inputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/codestarconnections/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/codestarconnections/connection.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/codestarconnections/connection.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/codestarconnections/outputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/codestarconnections/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/codestarnotifications/_inputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/codestarnotifications/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/codestarnotifications/notification_rule.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/codestarnotifications/notification_rule.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/codestarnotifications/outputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/codestarnotifications/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/cognito/__init__.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/cognito/__init__.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/cognito/_inputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/cognito/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/cognito/identity_pool.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/cognito/identity_pool.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/cognito/identity_pool_role_attachment.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/cognito/identity_pool_role_attachment.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/cognito/outputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/cognito/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/cognito/user_pool.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/cognito/user_pool.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/cognito/user_pool_client.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/cognito/user_pool_client.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/cognito/user_pool_domain.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/cognito/user_pool_domain.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/cognito/user_pool_group.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/cognito/user_pool_group.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/cognito/user_pool_identity_provider.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/cognito/user_pool_identity_provider.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/cognito/user_pool_resource_server.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/cognito/user_pool_resource_server.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/cognito/user_pool_risk_configuration_attachment.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/cognito/user_pool_risk_configuration_attachment.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/cognito/user_pool_ui_customization_attachment.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/cognito/user_pool_ui_customization_attachment.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/cognito/user_pool_user.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/cognito/user_pool_user.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/cognito/user_pool_user_to_group_attachment.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/cognito/user_pool_user_to_group_attachment.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/config/outputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/config/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/config/vars.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/config/vars.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/configuration/__init__.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/configuration/__init__.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/configuration/_inputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/configuration/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/configuration/aggregation_authorization.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/configuration/aggregation_authorization.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/configuration/config_rule.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/configuration/config_rule.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/configuration/configuration_aggregator.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/configuration/configuration_aggregator.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/configuration/configuration_recorder.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/configuration/configuration_recorder.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/configuration/conformance_pack.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/configuration/conformance_pack.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/configuration/delivery_channel.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/configuration/delivery_channel.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/configuration/organization_config_rule.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/configuration/organization_config_rule.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/configuration/organization_conformance_pack.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/configuration/organization_conformance_pack.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/configuration/outputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/configuration/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/configuration/remediation_configuration.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/configuration/remediation_configuration.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/configuration/stored_query.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/configuration/stored_query.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/connect/_enums.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/connect/_enums.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/connect/_inputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/connect/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/connect/contact_flow.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/connect/contact_flow.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/connect/contact_flow_module.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/connect/contact_flow_module.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/connect/hours_of_operation.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/connect/hours_of_operation.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/connect/outputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/connect/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/connect/quick_connect.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/connect/quick_connect.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/connect/user.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/connect/user.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/connect/user_hierarchy_group.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/connect/user_hierarchy_group.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/cur/_enums.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/cur/_enums.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/cur/report_definition.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/cur/report_definition.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/customerprofiles/_enums.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/customerprofiles/_enums.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/customerprofiles/_inputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/customerprofiles/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/customerprofiles/domain.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/customerprofiles/domain.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/customerprofiles/integration.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/customerprofiles/integration.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/customerprofiles/object_type.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/customerprofiles/object_type.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/customerprofiles/outputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/customerprofiles/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/databrew/_enums.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/databrew/_enums.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/databrew/_inputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/databrew/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/databrew/dataset.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/databrew/dataset.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/databrew/job.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/databrew/job.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/databrew/outputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/databrew/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/databrew/project.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/databrew/project.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/databrew/recipe.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/databrew/recipe.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/databrew/ruleset.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/databrew/ruleset.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/databrew/schedule.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/databrew/schedule.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/datapipeline/_inputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/datapipeline/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/datapipeline/outputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/datapipeline/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/datapipeline/pipeline.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/datapipeline/pipeline.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/datasync/__init__.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/datasync/__init__.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/datasync/_enums.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/datasync/_enums.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/datasync/_inputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/datasync/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/datasync/agent.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/datasync/agent.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/datasync/location_efs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/datasync/location_efs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/datasync/location_f_sx_windows.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/datasync/location_f_sx_windows.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/datasync/location_hdfs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/datasync/location_hdfs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/datasync/location_nfs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/datasync/location_nfs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/datasync/location_object_storage.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/datasync/location_object_storage.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/datasync/location_s3.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/datasync/location_s3.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/datasync/location_smb.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/datasync/location_smb.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/datasync/outputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/datasync/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/datasync/task.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/datasync/task.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/dax/_inputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/dax/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/dax/cluster.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/dax/cluster.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/dax/outputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/dax/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/dax/parameter_group.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/dax/parameter_group.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/dax/subnet_group.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/dax/subnet_group.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/detective/_inputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/detective/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/detective/graph.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/detective/graph.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/detective/member_invitation.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/detective/member_invitation.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/detective/outputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/detective/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/devicefarm/_enums.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/devicefarm/_enums.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/devicefarm/_inputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/devicefarm/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/devicefarm/device_pool.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/devicefarm/device_pool.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/devicefarm/instance_profile.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/devicefarm/instance_profile.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/devicefarm/network_profile.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/devicefarm/network_profile.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/devicefarm/outputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/devicefarm/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/devicefarm/project.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/devicefarm/project.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/devicefarm/test_grid_project.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/devicefarm/test_grid_project.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/devicefarm/vpce_configuration.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/devicefarm/vpce_configuration.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/devopsguru/_inputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/devopsguru/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/devopsguru/notification_channel.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/devopsguru/notification_channel.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/devopsguru/outputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/devopsguru/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/devopsguru/resource_collection.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/devopsguru/resource_collection.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/directoryservice/_inputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/directoryservice/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/directoryservice/microsoft_ad.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/directoryservice/microsoft_ad.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/directoryservice/outputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/directoryservice/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/directoryservice/simple_ad.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/directoryservice/simple_ad.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/dlm/_inputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/dlm/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/dlm/lifecycle_policy.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/dlm/lifecycle_policy.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/dlm/outputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/dlm/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/dms/_inputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/dms/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/dms/certificate.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/dms/certificate.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/dms/endpoint.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/dms/endpoint.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/dms/event_subscription.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/dms/event_subscription.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/dms/outputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/dms/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/dms/replication_instance.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/dms/replication_instance.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/dms/replication_subnet_group.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/dms/replication_subnet_group.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/dms/replication_task.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/dms/replication_task.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/docdb/_inputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/docdb/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/docdb/db_cluster.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/docdb/db_cluster.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/docdb/db_cluster_parameter_group.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/docdb/db_cluster_parameter_group.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/docdb/db_instance.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/docdb/db_instance.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/docdb/db_subnet_group.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/docdb/db_subnet_group.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/docdb/outputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/docdb/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/dynamodb/_inputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/dynamodb/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/dynamodb/global_table.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/dynamodb/global_table.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/dynamodb/outputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/dynamodb/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/dynamodb/table.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/dynamodb/table.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ec2/__init__.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ec2/__init__.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ec2/_enums.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ec2/_enums.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ec2/_inputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ec2/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ec2/capacity_reservation.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ec2/capacity_reservation.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ec2/capacity_reservation_fleet.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ec2/capacity_reservation_fleet.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ec2/carrier_gateway.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ec2/carrier_gateway.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ec2/client_vpn_authorization_rule.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ec2/client_vpn_authorization_rule.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ec2/client_vpn_endpoint.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ec2/client_vpn_endpoint.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ec2/client_vpn_route.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ec2/client_vpn_route.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ec2/client_vpn_target_network_association.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ec2/client_vpn_target_network_association.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ec2/customer_gateway.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ec2/customer_gateway.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ec2/dhcp_options.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ec2/dhcp_options.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ec2/ec2_fleet.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ec2/ec2_fleet.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ec2/egress_only_internet_gateway.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ec2/egress_only_internet_gateway.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ec2/eip.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ec2/eip.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ec2/eipassociation.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ec2/eipassociation.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ec2/enclave_certificate_iam_role_association.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ec2/enclave_certificate_iam_role_association.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ec2/flow_log.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ec2/flow_log.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ec2/gateway_route_table_association.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ec2/gateway_route_table_association.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ec2/host.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ec2/host.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ec2/instance.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ec2/instance.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ec2/internet_gateway.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ec2/internet_gateway.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ec2/ipam.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ec2/ipam.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ec2/ipam_allocation.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ec2/ipam_allocation.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ec2/ipam_pool.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ec2/ipam_pool.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ec2/ipam_scope.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ec2/ipam_scope.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ec2/launch_template.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ec2/launch_template.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ec2/local_gateway_route.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ec2/local_gateway_route.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ec2/local_gateway_route_table_vpcassociation.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ec2/local_gateway_route_table_vpcassociation.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ec2/nat_gateway.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ec2/nat_gateway.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ec2/network_acl.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ec2/network_acl.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ec2/network_acl_entry.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ec2/network_acl_entry.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ec2/network_insights_access_scope.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ec2/network_insights_access_scope.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ec2/network_insights_access_scope_analysis.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ec2/network_insights_access_scope_analysis.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ec2/network_insights_analysis.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ec2/network_insights_analysis.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ec2/network_insights_path.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ec2/network_insights_path.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ec2/network_interface.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ec2/network_interface.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ec2/network_interface_attachment.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ec2/network_interface_attachment.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ec2/network_interface_permission.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ec2/network_interface_permission.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ec2/outputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ec2/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ec2/placement_group.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ec2/placement_group.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ec2/prefix_list.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ec2/prefix_list.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ec2/route.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ec2/route.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ec2/route_table.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ec2/route_table.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ec2/security_group.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ec2/security_group.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ec2/security_group_egress.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ec2/security_group_egress.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ec2/security_group_ingress.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ec2/security_group_ingress.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ec2/spot_fleet.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ec2/spot_fleet.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ec2/subnet.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ec2/subnet.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ec2/subnet_cidr_block.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ec2/subnet_cidr_block.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ec2/subnet_network_acl_association.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ec2/subnet_network_acl_association.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ec2/subnet_route_table_association.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ec2/subnet_route_table_association.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ec2/traffic_mirror_filter.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ec2/traffic_mirror_filter.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ec2/traffic_mirror_filter_rule.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ec2/traffic_mirror_filter_rule.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ec2/traffic_mirror_session.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ec2/traffic_mirror_session.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ec2/traffic_mirror_target.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ec2/traffic_mirror_target.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ec2/transit_gateway.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ec2/transit_gateway.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ec2/transit_gateway_attachment.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ec2/transit_gateway_attachment.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ec2/transit_gateway_connect.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ec2/transit_gateway_connect.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ec2/transit_gateway_multicast_domain.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ec2/transit_gateway_multicast_domain.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ec2/transit_gateway_multicast_domain_association.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ec2/transit_gateway_multicast_domain_association.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ec2/transit_gateway_multicast_group_member.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ec2/transit_gateway_multicast_group_member.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ec2/transit_gateway_multicast_group_source.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ec2/transit_gateway_multicast_group_source.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ec2/transit_gateway_peering_attachment.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ec2/transit_gateway_peering_attachment.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ec2/transit_gateway_route.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ec2/transit_gateway_route.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ec2/transit_gateway_route_table.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ec2/transit_gateway_route_table.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ec2/transit_gateway_route_table_association.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ec2/transit_gateway_route_table_association.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ec2/transit_gateway_route_table_propagation.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ec2/transit_gateway_route_table_propagation.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ec2/transit_gateway_vpc_attachment.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ec2/transit_gateway_vpc_attachment.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ec2/volume.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ec2/volume.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ec2/volume_attachment.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ec2/volume_attachment.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ec2/vpc.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ec2/vpc.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ec2/vpc_cidr_block.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ec2/vpc_cidr_block.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ec2/vpc_endpoint.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ec2/vpc_endpoint.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ec2/vpc_endpoint_connection_notification.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ec2/vpc_endpoint_connection_notification.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ec2/vpc_endpoint_service.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ec2/vpc_endpoint_service.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ec2/vpc_endpoint_service_permissions.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ec2/vpc_endpoint_service_permissions.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ec2/vpc_gateway_attachment.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ec2/vpc_gateway_attachment.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ec2/vpc_peering_connection.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ec2/vpc_peering_connection.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ec2/vpcdhcp_options_association.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ec2/vpcdhcp_options_association.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ec2/vpn_connection.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ec2/vpn_connection.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ec2/vpn_connection_route.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ec2/vpn_connection_route.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ec2/vpn_gateway.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ec2/vpn_gateway.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ec2/vpn_gateway_route_propagation.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ec2/vpn_gateway_route_propagation.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ecr/_enums.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ecr/_enums.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ecr/_inputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ecr/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ecr/outputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ecr/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ecr/public_repository.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ecr/public_repository.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ecr/registry_policy.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ecr/registry_policy.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ecr/replication_configuration.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ecr/replication_configuration.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ecr/repository.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ecr/repository.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ecs/__init__.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ecs/__init__.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ecs/_enums.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ecs/_enums.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ecs/_inputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ecs/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ecs/capacity_provider.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ecs/capacity_provider.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ecs/cluster.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ecs/cluster.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ecs/cluster_capacity_provider_associations.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ecs/cluster_capacity_provider_associations.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ecs/outputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ecs/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ecs/primary_task_set.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ecs/primary_task_set.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ecs/service.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ecs/service.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ecs/task_definition.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ecs/task_definition.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ecs/task_set.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ecs/task_set.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/efs/_inputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/efs/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/efs/access_point.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/efs/access_point.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/efs/file_system.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/efs/file_system.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/efs/mount_target.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/efs/mount_target.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/efs/outputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/efs/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/eks/_enums.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/eks/_enums.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/eks/_inputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/eks/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/eks/addon.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/eks/addon.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/eks/cluster.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/eks/cluster.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/eks/fargate_profile.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/eks/fargate_profile.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/eks/nodegroup.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/eks/nodegroup.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/eks/outputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/eks/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/elasticache/__init__.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/elasticache/__init__.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/elasticache/_enums.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/elasticache/_enums.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/elasticache/_inputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/elasticache/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/elasticache/cache_cluster.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/elasticache/cache_cluster.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/elasticache/global_replication_group.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/elasticache/global_replication_group.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/elasticache/outputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/elasticache/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/elasticache/parameter_group.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/elasticache/parameter_group.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/elasticache/replication_group.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/elasticache/replication_group.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/elasticache/security_group.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/elasticache/security_group.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/elasticache/security_group_ingress.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/elasticache/security_group_ingress.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/elasticache/subnet_group.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/elasticache/subnet_group.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/elasticache/user.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/elasticache/user.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/elasticache/user_group.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/elasticache/user_group.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/elasticbeanstalk/_inputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/elasticbeanstalk/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/elasticbeanstalk/application.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/elasticbeanstalk/application.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/elasticbeanstalk/application_version.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/elasticbeanstalk/application_version.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/elasticbeanstalk/configuration_template.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/elasticbeanstalk/configuration_template.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/elasticbeanstalk/environment.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/elasticbeanstalk/environment.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/elasticbeanstalk/outputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/elasticbeanstalk/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/elasticloadbalancing/_inputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/elasticloadbalancing/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/elasticloadbalancing/load_balancer.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/elasticloadbalancing/load_balancer.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/elasticloadbalancing/outputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/elasticloadbalancing/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/elasticloadbalancingv2/_inputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/elasticloadbalancingv2/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/elasticloadbalancingv2/listener.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/elasticloadbalancingv2/listener.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/elasticloadbalancingv2/listener_certificate.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/elasticloadbalancingv2/listener_certificate.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/elasticloadbalancingv2/listener_rule.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/elasticloadbalancingv2/listener_rule.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/elasticloadbalancingv2/load_balancer.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/elasticloadbalancingv2/load_balancer.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/elasticloadbalancingv2/outputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/elasticloadbalancingv2/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/elasticloadbalancingv2/target_group.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/elasticloadbalancingv2/target_group.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/elasticsearch/_inputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/elasticsearch/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/elasticsearch/domain.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/elasticsearch/domain.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/elasticsearch/outputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/elasticsearch/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/emr/__init__.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/emr/__init__.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/emr/_enums.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/emr/_enums.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/emr/_inputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/emr/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/emr/cluster.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/emr/cluster.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/emr/instance_fleet_config.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/emr/instance_fleet_config.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/emr/instance_group_config.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/emr/instance_group_config.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/emr/outputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/emr/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/emr/security_configuration.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/emr/security_configuration.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/emr/step.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/emr/step.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/emr/studio.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/emr/studio.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/emr/studio_session_mapping.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/emr/studio_session_mapping.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/emrcontainers/_inputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/emrcontainers/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/emrcontainers/outputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/emrcontainers/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/emrcontainers/virtual_cluster.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/emrcontainers/virtual_cluster.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/events/_enums.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/events/_enums.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/events/_inputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/events/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/events/api_destination.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/events/api_destination.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/events/archive.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/events/archive.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/events/connection.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/events/connection.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/events/event_bus.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/events/event_bus.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/events/event_bus_policy.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/events/event_bus_policy.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/events/outputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/events/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/events/rule.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/events/rule.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/eventschemas/_inputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/eventschemas/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/eventschemas/discoverer.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/eventschemas/discoverer.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/eventschemas/outputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/eventschemas/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/eventschemas/registry.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/eventschemas/registry.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/eventschemas/registry_policy.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/eventschemas/registry_policy.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/eventschemas/schema.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/eventschemas/schema.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/evidently/_enums.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/evidently/_enums.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/evidently/_inputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/evidently/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/evidently/experiment.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/evidently/experiment.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/evidently/feature.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/evidently/feature.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/evidently/launch.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/evidently/launch.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/evidently/outputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/evidently/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/evidently/project.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/evidently/project.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/extension_resource.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/extension_resource.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/finspace/_enums.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/finspace/_enums.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/finspace/_inputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/finspace/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/finspace/environment.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/finspace/environment.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/finspace/outputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/finspace/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/fis/_inputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/fis/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/fis/experiment_template.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/fis/experiment_template.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/fis/outputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/fis/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/fms/_enums.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/fms/_enums.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/fms/_inputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/fms/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/fms/notification_channel.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/fms/notification_channel.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/fms/outputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/fms/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/fms/policy.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/fms/policy.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/frauddetector/_enums.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/frauddetector/_enums.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/frauddetector/_inputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/frauddetector/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/frauddetector/detector.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/frauddetector/detector.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/frauddetector/entity_type.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/frauddetector/entity_type.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/frauddetector/event_type.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/frauddetector/event_type.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/frauddetector/label.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/frauddetector/label.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/frauddetector/outcome.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/frauddetector/outcome.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/frauddetector/outputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/frauddetector/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/frauddetector/variable.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/frauddetector/variable.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/fsx/_inputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/fsx/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/fsx/file_system.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/fsx/file_system.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/fsx/outputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/fsx/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/gamelift/__init__.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/gamelift/__init__.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/gamelift/_enums.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/gamelift/_enums.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/gamelift/_inputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/gamelift/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/gamelift/alias.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/gamelift/alias.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/gamelift/build.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/gamelift/build.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/gamelift/fleet.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/gamelift/fleet.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/gamelift/game_server_group.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/gamelift/game_server_group.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/gamelift/game_session_queue.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/gamelift/game_session_queue.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/gamelift/matchmaking_configuration.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/gamelift/matchmaking_configuration.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/gamelift/matchmaking_rule_set.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/gamelift/matchmaking_rule_set.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/gamelift/outputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/gamelift/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/gamelift/script.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/gamelift/script.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/get_account_id.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/get_account_id.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/get_azs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/get_azs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/get_partition.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/get_partition.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/get_region.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/get_region.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/get_ssm_parameter_list.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/get_ssm_parameter_list.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/get_ssm_parameter_string.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/get_ssm_parameter_string.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/get_url_suffix.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/get_url_suffix.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/globalaccelerator/_enums.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/globalaccelerator/_enums.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/globalaccelerator/_inputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/globalaccelerator/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/globalaccelerator/accelerator.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/globalaccelerator/accelerator.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/globalaccelerator/endpoint_group.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/globalaccelerator/endpoint_group.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/globalaccelerator/listener.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/globalaccelerator/listener.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/globalaccelerator/outputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/globalaccelerator/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/glue/__init__.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/glue/__init__.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/glue/_enums.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/glue/_enums.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/glue/_inputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/glue/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/glue/classifier.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/glue/classifier.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/glue/connection.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/glue/connection.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/glue/crawler.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/glue/crawler.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/glue/data_catalog_encryption_settings.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/glue/data_catalog_encryption_settings.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/glue/database.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/glue/database.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/glue/dev_endpoint.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/glue/dev_endpoint.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/glue/job.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/glue/job.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/glue/ml_transform.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/glue/ml_transform.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/glue/outputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/glue/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/glue/partition.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/glue/partition.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/glue/registry.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/glue/registry.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/glue/schema.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/glue/schema.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/glue/schema_version.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/glue/schema_version.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/glue/schema_version_metadata.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/glue/schema_version_metadata.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/glue/security_configuration.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/glue/security_configuration.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/glue/table.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/glue/table.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/glue/trigger.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/glue/trigger.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/glue/workflow.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/glue/workflow.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/greengrass/__init__.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/greengrass/__init__.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/greengrass/_inputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/greengrass/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/greengrass/connector_definition.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/greengrass/connector_definition.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/greengrass/connector_definition_version.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/greengrass/connector_definition_version.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/greengrass/core_definition.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/greengrass/core_definition.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/greengrass/core_definition_version.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/greengrass/core_definition_version.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/greengrass/device_definition.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/greengrass/device_definition.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/greengrass/device_definition_version.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/greengrass/device_definition_version.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/greengrass/function_definition.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/greengrass/function_definition.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/greengrass/function_definition_version.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/greengrass/function_definition_version.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/greengrass/group.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/greengrass/group.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/greengrass/group_version.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/greengrass/group_version.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/greengrass/logger_definition.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/greengrass/logger_definition.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/greengrass/logger_definition_version.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/greengrass/logger_definition_version.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/greengrass/outputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/greengrass/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/greengrass/resource_definition.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/greengrass/resource_definition.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/greengrass/resource_definition_version.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/greengrass/resource_definition_version.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/greengrass/subscription_definition.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/greengrass/subscription_definition.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/greengrass/subscription_definition_version.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/greengrass/subscription_definition_version.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/greengrassv2/_enums.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/greengrassv2/_enums.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/greengrassv2/_inputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/greengrassv2/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/greengrassv2/component_version.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/greengrassv2/component_version.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/greengrassv2/outputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/greengrassv2/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/groundstation/_enums.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/groundstation/_enums.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/groundstation/_inputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/groundstation/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/groundstation/config.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/groundstation/config.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/groundstation/dataflow_endpoint_group.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/groundstation/dataflow_endpoint_group.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/groundstation/mission_profile.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/groundstation/mission_profile.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/groundstation/outputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/groundstation/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/guardduty/_inputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/guardduty/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/guardduty/detector.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/guardduty/detector.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/guardduty/filter.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/guardduty/filter.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/guardduty/ip_set.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/guardduty/ip_set.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/guardduty/master.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/guardduty/master.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/guardduty/member.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/guardduty/member.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/guardduty/outputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/guardduty/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/guardduty/threat_intel_set.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/guardduty/threat_intel_set.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/healthlake/_enums.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/healthlake/_enums.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/healthlake/_inputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/healthlake/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/healthlake/fhir_datastore.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/healthlake/fhir_datastore.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/healthlake/outputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/healthlake/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/iam/__init__.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/iam/__init__.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/iam/_inputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/iam/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/iam/access_key.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/iam/access_key.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/iam/group.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/iam/group.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/iam/instance_profile.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/iam/instance_profile.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/iam/managed_policy.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/iam/managed_policy.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/iam/oidc_provider.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/iam/oidc_provider.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/iam/outputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/iam/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/iam/policy.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/iam/policy.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/iam/role.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/iam/role.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/iam/saml_provider.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/iam/saml_provider.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/iam/server_certificate.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/iam/server_certificate.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/iam/service_linked_role.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/iam/service_linked_role.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/iam/user.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/iam/user.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/iam/user_to_group_addition.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/iam/user_to_group_addition.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/iam/virtual_mfa_device.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/iam/virtual_mfa_device.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/imagebuilder/__init__.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/imagebuilder/__init__.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/imagebuilder/_enums.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/imagebuilder/_enums.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/imagebuilder/_inputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/imagebuilder/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/imagebuilder/component.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/imagebuilder/component.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/imagebuilder/container_recipe.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/imagebuilder/container_recipe.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/imagebuilder/distribution_configuration.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/imagebuilder/distribution_configuration.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/imagebuilder/image.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/imagebuilder/image.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/imagebuilder/image_pipeline.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/imagebuilder/image_pipeline.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/imagebuilder/image_recipe.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/imagebuilder/image_recipe.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/imagebuilder/infrastructure_configuration.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/imagebuilder/infrastructure_configuration.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/imagebuilder/outputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/imagebuilder/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/import_value.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/import_value.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/inspector/_inputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/inspector/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/inspector/assessment_target.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/inspector/assessment_target.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/inspector/assessment_template.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/inspector/assessment_template.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/inspector/outputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/inspector/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/inspector/resource_group.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/inspector/resource_group.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/inspectorv2/_enums.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/inspectorv2/_enums.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/inspectorv2/_inputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/inspectorv2/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/inspectorv2/filter.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/inspectorv2/filter.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/inspectorv2/outputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/inspectorv2/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/iot/__init__.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/iot/__init__.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/iot/_enums.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/iot/_enums.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/iot/_inputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/iot/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/iot/account_audit_configuration.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/iot/account_audit_configuration.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/iot/authorizer.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/iot/authorizer.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/iot/certificate.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/iot/certificate.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/iot/custom_metric.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/iot/custom_metric.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/iot/dimension.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/iot/dimension.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/iot/domain_configuration.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/iot/domain_configuration.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/iot/fleet_metric.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/iot/fleet_metric.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/iot/job_template.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/iot/job_template.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/iot/logging.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/iot/logging.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/iot/mitigation_action.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/iot/mitigation_action.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/iot/outputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/iot/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/iot/policy.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/iot/policy.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/iot/policy_principal_attachment.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/iot/policy_principal_attachment.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/iot/provisioning_template.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/iot/provisioning_template.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/iot/resource_specific_logging.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/iot/resource_specific_logging.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/iot/scheduled_audit.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/iot/scheduled_audit.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/iot/security_profile.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/iot/security_profile.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/iot/thing.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/iot/thing.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/iot/thing_principal_attachment.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/iot/thing_principal_attachment.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/iot/topic_rule.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/iot/topic_rule.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/iot/topic_rule_destination.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/iot/topic_rule_destination.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/iot1click/_inputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/iot1click/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/iot1click/device.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/iot1click/device.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/iot1click/outputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/iot1click/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/iot1click/placement.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/iot1click/placement.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/iot1click/project.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/iot1click/project.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/iotanalytics/_inputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/iotanalytics/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/iotanalytics/channel.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/iotanalytics/channel.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/iotanalytics/dataset.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/iotanalytics/dataset.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/iotanalytics/datastore.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/iotanalytics/datastore.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/iotanalytics/outputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/iotanalytics/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/iotanalytics/pipeline.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/iotanalytics/pipeline.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/iotcoredeviceadvisor/_inputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/iotcoredeviceadvisor/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/iotcoredeviceadvisor/outputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/iotcoredeviceadvisor/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/iotcoredeviceadvisor/suite_definition.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/iotcoredeviceadvisor/suite_definition.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/iotevents/_inputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/iotevents/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/iotevents/detector_model.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/iotevents/detector_model.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/iotevents/input.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/iotevents/input.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/iotevents/outputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/iotevents/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/iotfleethub/_inputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/iotfleethub/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/iotfleethub/application.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/iotfleethub/application.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/iotfleethub/outputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/iotfleethub/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/iotsitewise/_enums.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/iotsitewise/_enums.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/iotsitewise/_inputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/iotsitewise/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/iotsitewise/access_policy.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/iotsitewise/access_policy.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/iotsitewise/asset.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/iotsitewise/asset.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/iotsitewise/asset_model.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/iotsitewise/asset_model.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/iotsitewise/dashboard.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/iotsitewise/dashboard.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/iotsitewise/gateway.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/iotsitewise/gateway.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/iotsitewise/outputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/iotsitewise/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/iotsitewise/portal.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/iotsitewise/portal.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/iotsitewise/project.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/iotsitewise/project.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/iotthingsgraph/_inputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/iotthingsgraph/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/iotthingsgraph/flow_template.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/iotthingsgraph/flow_template.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/iotthingsgraph/outputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/iotthingsgraph/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/iotwireless/__init__.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/iotwireless/__init__.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/iotwireless/_enums.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/iotwireless/_enums.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/iotwireless/_inputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/iotwireless/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/iotwireless/destination.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/iotwireless/destination.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/iotwireless/device_profile.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/iotwireless/device_profile.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/iotwireless/fuota_task.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/iotwireless/fuota_task.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/iotwireless/multicast_group.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/iotwireless/multicast_group.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/iotwireless/outputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/iotwireless/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/iotwireless/partner_account.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/iotwireless/partner_account.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/iotwireless/service_profile.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/iotwireless/service_profile.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/iotwireless/task_definition.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/iotwireless/task_definition.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/iotwireless/wireless_device.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/iotwireless/wireless_device.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/iotwireless/wireless_gateway.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/iotwireless/wireless_gateway.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ivs/_enums.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ivs/_enums.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ivs/_inputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ivs/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ivs/channel.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ivs/channel.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ivs/outputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ivs/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ivs/playback_key_pair.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ivs/playback_key_pair.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ivs/recording_configuration.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ivs/recording_configuration.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ivs/stream_key.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ivs/stream_key.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/kendra/_enums.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/kendra/_enums.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/kendra/_inputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/kendra/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/kendra/data_source.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/kendra/data_source.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/kendra/faq.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/kendra/faq.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/kendra/index.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/kendra/index.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/kendra/outputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/kendra/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/kinesis/_enums.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/kinesis/_enums.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/kinesis/_inputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/kinesis/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/kinesis/outputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/kinesis/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/kinesis/stream.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/kinesis/stream.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/kinesis/stream_consumer.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/kinesis/stream_consumer.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/kinesisanalytics/_inputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/kinesisanalytics/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/kinesisanalytics/application.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/kinesisanalytics/application.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/kinesisanalytics/application_output_resource.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/kinesisanalytics/application_output_resource.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/kinesisanalytics/application_reference_data_source.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/kinesisanalytics/application_reference_data_source.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/kinesisanalytics/outputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/kinesisanalytics/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/kinesisanalyticsv2/_inputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/kinesisanalyticsv2/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/kinesisanalyticsv2/application.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/kinesisanalyticsv2/application.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/kinesisanalyticsv2/application_cloud_watch_logging_option.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/kinesisanalyticsv2/application_cloud_watch_logging_option.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/kinesisanalyticsv2/application_output_resource.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/kinesisanalyticsv2/application_output_resource.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/kinesisanalyticsv2/application_reference_data_source.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/kinesisanalyticsv2/application_reference_data_source.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/kinesisanalyticsv2/outputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/kinesisanalyticsv2/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/kinesisfirehose/_enums.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/kinesisfirehose/_enums.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/kinesisfirehose/_inputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/kinesisfirehose/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/kinesisfirehose/delivery_stream.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/kinesisfirehose/delivery_stream.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/kinesisfirehose/outputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/kinesisfirehose/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/kinesisvideo/_inputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/kinesisvideo/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/kinesisvideo/outputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/kinesisvideo/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/kinesisvideo/signaling_channel.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/kinesisvideo/signaling_channel.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/kinesisvideo/stream.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/kinesisvideo/stream.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/kms/_enums.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/kms/_enums.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/kms/_inputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/kms/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/kms/alias.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/kms/alias.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/kms/key.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/kms/key.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/kms/outputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/kms/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/kms/replica_key.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/kms/replica_key.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/lakeformation/_inputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/lakeformation/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/lakeformation/data_lake_settings.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/lakeformation/data_lake_settings.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/lakeformation/outputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/lakeformation/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/lakeformation/permissions.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/lakeformation/permissions.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/lakeformation/resource.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/lakeformation/resource.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/lambda_/__init__.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/lambda_/__init__.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/lambda_/_enums.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/lambda_/_enums.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/lambda_/_inputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/lambda_/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/lambda_/alias.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/lambda_/alias.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/lambda_/code_signing_config.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/lambda_/code_signing_config.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/lambda_/event_invoke_config.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/lambda_/event_invoke_config.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/lambda_/event_source_mapping.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/lambda_/event_source_mapping.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/lambda_/function.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/lambda_/function.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/lambda_/layer_version.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/lambda_/layer_version.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/lambda_/layer_version_permission.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/lambda_/layer_version_permission.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/lambda_/outputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/lambda_/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/lambda_/permission.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/lambda_/permission.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/lambda_/url.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/lambda_/url.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/lambda_/version.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/lambda_/version.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/lex/_enums.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/lex/_enums.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/lex/_inputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/lex/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/lex/bot.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/lex/bot.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/lex/bot_alias.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/lex/bot_alias.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/lex/bot_version.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/lex/bot_version.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/lex/outputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/lex/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/lex/resource_policy.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/lex/resource_policy.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/licensemanager/_inputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/licensemanager/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/licensemanager/grant.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/licensemanager/grant.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/licensemanager/license.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/licensemanager/license.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/licensemanager/outputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/licensemanager/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/lightsail/__init__.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/lightsail/__init__.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/lightsail/_enums.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/lightsail/_enums.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/lightsail/_inputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/lightsail/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/lightsail/alarm.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/lightsail/alarm.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/lightsail/bucket.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/lightsail/bucket.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/lightsail/database.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/lightsail/database.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/lightsail/disk.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/lightsail/disk.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/lightsail/instance.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/lightsail/instance.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/lightsail/load_balancer.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/lightsail/load_balancer.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/lightsail/load_balancer_tls_certificate.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/lightsail/load_balancer_tls_certificate.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/lightsail/outputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/lightsail/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/lightsail/static_ip.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/lightsail/static_ip.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/location/_enums.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/location/_enums.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/location/_inputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/location/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/location/geofence_collection.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/location/geofence_collection.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/location/map.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/location/map.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/location/outputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/location/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/location/place_index.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/location/place_index.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/location/route_calculator.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/location/route_calculator.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/location/tracker.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/location/tracker.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/location/tracker_consumer.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/location/tracker_consumer.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/logs/_inputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/logs/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/logs/destination.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/logs/destination.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/logs/log_group.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/logs/log_group.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/logs/log_stream.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/logs/log_stream.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/logs/metric_filter.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/logs/metric_filter.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/logs/outputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/logs/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/logs/query_definition.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/logs/query_definition.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/logs/resource_policy.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/logs/resource_policy.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/logs/subscription_filter.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/logs/subscription_filter.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/lookoutequipment/_inputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/lookoutequipment/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/lookoutequipment/inference_scheduler.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/lookoutequipment/inference_scheduler.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/lookoutequipment/outputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/lookoutequipment/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/lookoutmetrics/_enums.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/lookoutmetrics/_enums.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/lookoutmetrics/_inputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/lookoutmetrics/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/lookoutmetrics/alert.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/lookoutmetrics/alert.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/lookoutmetrics/anomaly_detector.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/lookoutmetrics/anomaly_detector.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/lookoutmetrics/outputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/lookoutmetrics/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/lookoutvision/project.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/lookoutvision/project.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/macie/_enums.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/macie/_enums.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/macie/_inputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/macie/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/macie/custom_data_identifier.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/macie/custom_data_identifier.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/macie/findings_filter.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/macie/findings_filter.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/macie/outputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/macie/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/macie/session.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/macie/session.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/managedblockchain/_inputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/managedblockchain/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/managedblockchain/member.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/managedblockchain/member.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/managedblockchain/node.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/managedblockchain/node.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/managedblockchain/outputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/managedblockchain/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/mediaconnect/_enums.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/mediaconnect/_enums.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/mediaconnect/_inputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/mediaconnect/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/mediaconnect/flow.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/mediaconnect/flow.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/mediaconnect/flow_entitlement.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/mediaconnect/flow_entitlement.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/mediaconnect/flow_output.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/mediaconnect/flow_output.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/mediaconnect/flow_source.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/mediaconnect/flow_source.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/mediaconnect/flow_vpc_interface.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/mediaconnect/flow_vpc_interface.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/mediaconnect/outputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/mediaconnect/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/mediaconvert/_inputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/mediaconvert/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/mediaconvert/job_template.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/mediaconvert/job_template.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/mediaconvert/outputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/mediaconvert/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/mediaconvert/preset.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/mediaconvert/preset.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/mediaconvert/queue.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/mediaconvert/queue.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/medialive/_inputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/medialive/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/medialive/channel.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/medialive/channel.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/medialive/input.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/medialive/input.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/medialive/input_security_group.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/medialive/input_security_group.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/medialive/outputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/medialive/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/mediapackage/_enums.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/mediapackage/_enums.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/mediapackage/_inputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/mediapackage/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/mediapackage/asset.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/mediapackage/asset.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/mediapackage/channel.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/mediapackage/channel.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/mediapackage/origin_endpoint.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/mediapackage/origin_endpoint.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/mediapackage/outputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/mediapackage/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/mediapackage/packaging_configuration.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/mediapackage/packaging_configuration.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/mediapackage/packaging_group.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/mediapackage/packaging_group.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/mediastore/_inputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/mediastore/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/mediastore/container.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/mediastore/container.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/mediastore/outputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/mediastore/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/memorydb/_inputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/memorydb/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/memorydb/acl.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/memorydb/acl.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/memorydb/cluster.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/memorydb/cluster.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/memorydb/outputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/memorydb/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/memorydb/parameter_group.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/memorydb/parameter_group.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/memorydb/subnet_group.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/memorydb/subnet_group.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/memorydb/user.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/memorydb/user.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/msk/_inputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/msk/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/msk/cluster.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/msk/cluster.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/msk/outputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/msk/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/mwaa/_enums.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/mwaa/_enums.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/mwaa/_inputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/mwaa/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/mwaa/environment.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/mwaa/environment.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/mwaa/outputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/mwaa/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/neptune/_inputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/neptune/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/neptune/db_cluster.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/neptune/db_cluster.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/neptune/db_cluster_parameter_group.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/neptune/db_cluster_parameter_group.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/neptune/db_instance.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/neptune/db_instance.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/neptune/db_parameter_group.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/neptune/db_parameter_group.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/neptune/db_subnet_group.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/neptune/db_subnet_group.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/neptune/outputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/neptune/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/networkfirewall/_enums.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/networkfirewall/_enums.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/networkfirewall/_inputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/networkfirewall/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/networkfirewall/firewall.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/networkfirewall/firewall.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/networkfirewall/firewall_policy.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/networkfirewall/firewall_policy.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/networkfirewall/logging_configuration.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/networkfirewall/logging_configuration.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/networkfirewall/outputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/networkfirewall/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/networkfirewall/rule_group.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/networkfirewall/rule_group.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/networkmanager/_inputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/networkmanager/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/networkmanager/customer_gateway_association.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/networkmanager/customer_gateway_association.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/networkmanager/device.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/networkmanager/device.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/networkmanager/global_network.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/networkmanager/global_network.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/networkmanager/link.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/networkmanager/link.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/networkmanager/link_association.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/networkmanager/link_association.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/networkmanager/outputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/networkmanager/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/networkmanager/site.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/networkmanager/site.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/networkmanager/transit_gateway_registration.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/networkmanager/transit_gateway_registration.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/nimblestudio/_enums.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/nimblestudio/_enums.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/nimblestudio/_inputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/nimblestudio/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/nimblestudio/launch_profile.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/nimblestudio/launch_profile.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/nimblestudio/outputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/nimblestudio/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/nimblestudio/streaming_image.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/nimblestudio/streaming_image.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/nimblestudio/studio.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/nimblestudio/studio.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/nimblestudio/studio_component.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/nimblestudio/studio_component.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/opensearchservice/_inputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/opensearchservice/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/opensearchservice/domain.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/opensearchservice/domain.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/opensearchservice/outputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/opensearchservice/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/opsworks/_inputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/opsworks/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/opsworks/app.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/opsworks/app.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/opsworks/elastic_load_balancer_attachment.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/opsworks/elastic_load_balancer_attachment.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/opsworks/instance.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/opsworks/instance.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/opsworks/layer.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/opsworks/layer.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/opsworks/outputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/opsworks/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/opsworks/stack.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/opsworks/stack.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/opsworks/user_profile.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/opsworks/user_profile.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/opsworks/volume.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/opsworks/volume.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/opsworkscm/_inputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/opsworkscm/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/opsworkscm/outputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/opsworkscm/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/opsworkscm/server.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/opsworkscm/server.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/panorama/_enums.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/panorama/_enums.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/panorama/_inputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/panorama/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/panorama/application_instance.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/panorama/application_instance.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/panorama/outputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/panorama/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/panorama/package.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/panorama/package.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/panorama/package_version.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/panorama/package_version.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/pinpoint/__init__.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/pinpoint/__init__.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/pinpoint/_enums.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/pinpoint/_enums.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/pinpoint/_inputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/pinpoint/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/pinpoint/adm_channel.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/pinpoint/adm_channel.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/pinpoint/apns_channel.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/pinpoint/apns_channel.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/pinpoint/apns_sandbox_channel.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/pinpoint/apns_sandbox_channel.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/pinpoint/apns_voip_channel.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/pinpoint/apns_voip_channel.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/pinpoint/apns_voip_sandbox_channel.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/pinpoint/apns_voip_sandbox_channel.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/pinpoint/app.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/pinpoint/app.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/pinpoint/application_settings.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/pinpoint/application_settings.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/pinpoint/baidu_channel.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/pinpoint/baidu_channel.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/pinpoint/campaign.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/pinpoint/campaign.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/pinpoint/email_channel.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/pinpoint/email_channel.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/pinpoint/email_template.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/pinpoint/email_template.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/pinpoint/event_stream.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/pinpoint/event_stream.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/pinpoint/gcm_channel.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/pinpoint/gcm_channel.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/pinpoint/in_app_template.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/pinpoint/in_app_template.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/pinpoint/outputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/pinpoint/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/pinpoint/push_template.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/pinpoint/push_template.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/pinpoint/segment.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/pinpoint/segment.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/pinpoint/sms_channel.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/pinpoint/sms_channel.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/pinpoint/sms_template.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/pinpoint/sms_template.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/pinpoint/voice_channel.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/pinpoint/voice_channel.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/pinpointemail/_inputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/pinpointemail/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/pinpointemail/configuration_set.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/pinpointemail/configuration_set.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/pinpointemail/configuration_set_event_destination.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/pinpointemail/configuration_set_event_destination.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/pinpointemail/dedicated_ip_pool.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/pinpointemail/dedicated_ip_pool.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/pinpointemail/identity.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/pinpointemail/identity.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/pinpointemail/outputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/pinpointemail/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/provider.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/provider.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/qldb/_inputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/qldb/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/qldb/ledger.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/qldb/ledger.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/qldb/outputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/qldb/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/qldb/stream.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/qldb/stream.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/quicksight/_enums.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/quicksight/_enums.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/quicksight/_inputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/quicksight/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/quicksight/analysis.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/quicksight/analysis.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/quicksight/dashboard.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/quicksight/dashboard.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/quicksight/data_set.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/quicksight/data_set.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/quicksight/data_source.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/quicksight/data_source.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/quicksight/outputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/quicksight/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/quicksight/template.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/quicksight/template.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/quicksight/theme.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/quicksight/theme.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ram/_inputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ram/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ram/outputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ram/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ram/resource_share.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ram/resource_share.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/rds/__init__.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/rds/__init__.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/rds/_enums.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/rds/_enums.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/rds/_inputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/rds/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/rds/db_cluster.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/rds/db_cluster.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/rds/db_cluster_parameter_group.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/rds/db_cluster_parameter_group.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/rds/db_instance.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/rds/db_instance.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/rds/db_parameter_group.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/rds/db_parameter_group.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/rds/db_proxy.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/rds/db_proxy.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/rds/db_proxy_endpoint.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/rds/db_proxy_endpoint.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/rds/db_proxy_target_group.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/rds/db_proxy_target_group.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/rds/db_security_group.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/rds/db_security_group.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/rds/db_security_group_ingress.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/rds/db_security_group_ingress.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/rds/db_subnet_group.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/rds/db_subnet_group.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/rds/event_subscription.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/rds/event_subscription.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/rds/global_cluster.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/rds/global_cluster.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/rds/option_group.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/rds/option_group.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/rds/outputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/rds/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/redshift/__init__.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/redshift/__init__.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/redshift/_enums.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/redshift/_enums.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/redshift/_inputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/redshift/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/redshift/cluster.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/redshift/cluster.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/redshift/cluster_parameter_group.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/redshift/cluster_parameter_group.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/redshift/cluster_security_group.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/redshift/cluster_security_group.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/redshift/cluster_security_group_ingress.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/redshift/cluster_security_group_ingress.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/redshift/cluster_subnet_group.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/redshift/cluster_subnet_group.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/redshift/endpoint_access.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/redshift/endpoint_access.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/redshift/endpoint_authorization.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/redshift/endpoint_authorization.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/redshift/event_subscription.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/redshift/event_subscription.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/redshift/outputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/redshift/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/redshift/scheduled_action.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/redshift/scheduled_action.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/refactorspaces/_enums.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/refactorspaces/_enums.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/refactorspaces/_inputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/refactorspaces/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/refactorspaces/application.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/refactorspaces/application.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/refactorspaces/environment.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/refactorspaces/environment.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/refactorspaces/outputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/refactorspaces/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/refactorspaces/route.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/refactorspaces/route.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/refactorspaces/service.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/refactorspaces/service.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/rekognition/project.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/rekognition/project.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/resiliencehub/_enums.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/resiliencehub/_enums.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/resiliencehub/_inputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/resiliencehub/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/resiliencehub/app.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/resiliencehub/app.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/resiliencehub/outputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/resiliencehub/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/resiliencehub/resiliency_policy.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/resiliencehub/resiliency_policy.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/resourcegroups/_inputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/resourcegroups/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/resourcegroups/group.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/resourcegroups/group.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/resourcegroups/outputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/resourcegroups/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/robomaker/__init__.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/robomaker/__init__.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/robomaker/_enums.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/robomaker/_enums.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/robomaker/_inputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/robomaker/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/robomaker/fleet.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/robomaker/fleet.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/robomaker/outputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/robomaker/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/robomaker/robot.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/robomaker/robot.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/robomaker/robot_application.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/robomaker/robot_application.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/robomaker/robot_application_version.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/robomaker/robot_application_version.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/robomaker/simulation_application.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/robomaker/simulation_application.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/robomaker/simulation_application_version.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/robomaker/simulation_application_version.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/route53/_enums.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/route53/_enums.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/route53/_inputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/route53/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/route53/dnssec.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/route53/dnssec.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/route53/health_check.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/route53/health_check.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/route53/hosted_zone.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/route53/hosted_zone.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/route53/key_signing_key.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/route53/key_signing_key.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/route53/outputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/route53/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/route53/record_set.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/route53/record_set.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/route53/record_set_group.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/route53/record_set_group.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/route53recoverycontrol/_enums.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/route53recoverycontrol/_enums.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/route53recoverycontrol/_inputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/route53recoverycontrol/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/route53recoverycontrol/cluster.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/route53recoverycontrol/cluster.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/route53recoverycontrol/control_panel.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/route53recoverycontrol/control_panel.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/route53recoverycontrol/outputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/route53recoverycontrol/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/route53recoverycontrol/routing_control.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/route53recoverycontrol/routing_control.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/route53recoverycontrol/safety_rule.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/route53recoverycontrol/safety_rule.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/route53recoveryreadiness/_inputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/route53recoveryreadiness/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/route53recoveryreadiness/cell.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/route53recoveryreadiness/cell.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/route53recoveryreadiness/outputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/route53recoveryreadiness/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/route53recoveryreadiness/readiness_check.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/route53recoveryreadiness/readiness_check.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/route53recoveryreadiness/recovery_group.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/route53recoveryreadiness/recovery_group.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/route53recoveryreadiness/resource_set.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/route53recoveryreadiness/resource_set.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/route53resolver/__init__.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/route53resolver/__init__.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/route53resolver/_enums.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/route53resolver/_enums.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/route53resolver/_inputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/route53resolver/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/route53resolver/firewall_domain_list.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/route53resolver/firewall_domain_list.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/route53resolver/firewall_rule_group.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/route53resolver/firewall_rule_group.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/route53resolver/firewall_rule_group_association.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/route53resolver/firewall_rule_group_association.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/route53resolver/outputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/route53resolver/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/route53resolver/resolver_config.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/route53resolver/resolver_config.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/route53resolver/resolver_dnssec_config.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/route53resolver/resolver_dnssec_config.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/route53resolver/resolver_endpoint.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/route53resolver/resolver_endpoint.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/route53resolver/resolver_query_logging_config.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/route53resolver/resolver_query_logging_config.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/route53resolver/resolver_query_logging_config_association.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/route53resolver/resolver_query_logging_config_association.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/route53resolver/resolver_rule.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/route53resolver/resolver_rule.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/route53resolver/resolver_rule_association.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/route53resolver/resolver_rule_association.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/rum/_inputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/rum/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/rum/app_monitor.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/rum/app_monitor.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/rum/outputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/rum/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/s3/__init__.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/s3/__init__.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/s3/_enums.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/s3/_enums.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/s3/_inputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/s3/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/s3/access_point.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/s3/access_point.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/s3/bucket.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/s3/bucket.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/s3/bucket_policy.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/s3/bucket_policy.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/s3/multi_region_access_point.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/s3/multi_region_access_point.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/s3/multi_region_access_point_policy.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/s3/multi_region_access_point_policy.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/s3/outputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/s3/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/s3/storage_lens.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/s3/storage_lens.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/s3objectlambda/_inputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/s3objectlambda/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/s3objectlambda/access_point.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/s3objectlambda/access_point.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/s3objectlambda/access_point_policy.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/s3objectlambda/access_point_policy.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/s3objectlambda/outputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/s3objectlambda/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/s3outposts/_enums.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/s3outposts/_enums.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/s3outposts/_inputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/s3outposts/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/s3outposts/access_point.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/s3outposts/access_point.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/s3outposts/bucket.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/s3outposts/bucket.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/s3outposts/bucket_policy.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/s3outposts/bucket_policy.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/s3outposts/endpoint.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/s3outposts/endpoint.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/s3outposts/outputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/s3outposts/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/sagemaker/__init__.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/sagemaker/__init__.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/sagemaker/_enums.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/sagemaker/_enums.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/sagemaker/_inputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/sagemaker/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/sagemaker/app.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/sagemaker/app.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/sagemaker/app_image_config.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/sagemaker/app_image_config.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/sagemaker/code_repository.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/sagemaker/code_repository.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/sagemaker/data_quality_job_definition.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/sagemaker/data_quality_job_definition.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/sagemaker/device.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/sagemaker/device.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/sagemaker/device_fleet.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/sagemaker/device_fleet.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/sagemaker/domain.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/sagemaker/domain.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/sagemaker/endpoint.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/sagemaker/endpoint.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/sagemaker/endpoint_config.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/sagemaker/endpoint_config.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/sagemaker/feature_group.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/sagemaker/feature_group.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/sagemaker/image.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/sagemaker/image.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/sagemaker/image_version.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/sagemaker/image_version.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/sagemaker/model.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/sagemaker/model.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/sagemaker/model_bias_job_definition.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/sagemaker/model_bias_job_definition.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/sagemaker/model_explainability_job_definition.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/sagemaker/model_explainability_job_definition.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/sagemaker/model_package_group.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/sagemaker/model_package_group.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/sagemaker/model_quality_job_definition.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/sagemaker/model_quality_job_definition.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/sagemaker/monitoring_schedule.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/sagemaker/monitoring_schedule.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/sagemaker/notebook_instance.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/sagemaker/notebook_instance.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/sagemaker/notebook_instance_lifecycle_config.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/sagemaker/notebook_instance_lifecycle_config.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/sagemaker/outputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/sagemaker/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/sagemaker/pipeline.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/sagemaker/pipeline.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/sagemaker/project.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/sagemaker/project.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/sagemaker/user_profile.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/sagemaker/user_profile.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/sagemaker/workteam.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/sagemaker/workteam.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/sdb/domain.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/sdb/domain.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/secretsmanager/_inputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/secretsmanager/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/secretsmanager/outputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/secretsmanager/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/secretsmanager/resource_policy.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/secretsmanager/resource_policy.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/secretsmanager/rotation_schedule.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/secretsmanager/rotation_schedule.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/secretsmanager/secret.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/secretsmanager/secret.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/secretsmanager/secret_target_attachment.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/secretsmanager/secret_target_attachment.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/securityhub/hub.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/securityhub/hub.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/servicecatalog/__init__.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/servicecatalog/__init__.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/servicecatalog/_enums.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/servicecatalog/_enums.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/servicecatalog/_inputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/servicecatalog/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/servicecatalog/accepted_portfolio_share.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/servicecatalog/accepted_portfolio_share.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/servicecatalog/cloud_formation_product.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/servicecatalog/cloud_formation_product.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/servicecatalog/cloud_formation_provisioned_product.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/servicecatalog/cloud_formation_provisioned_product.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/servicecatalog/launch_notification_constraint.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/servicecatalog/launch_notification_constraint.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/servicecatalog/launch_role_constraint.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/servicecatalog/launch_role_constraint.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/servicecatalog/launch_template_constraint.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/servicecatalog/launch_template_constraint.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/servicecatalog/outputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/servicecatalog/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/servicecatalog/portfolio.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/servicecatalog/portfolio.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/servicecatalog/portfolio_principal_association.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/servicecatalog/portfolio_principal_association.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/servicecatalog/portfolio_product_association.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/servicecatalog/portfolio_product_association.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/servicecatalog/portfolio_share.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/servicecatalog/portfolio_share.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/servicecatalog/resource_update_constraint.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/servicecatalog/resource_update_constraint.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/servicecatalog/service_action.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/servicecatalog/service_action.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/servicecatalog/service_action_association.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/servicecatalog/service_action_association.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/servicecatalog/stack_set_constraint.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/servicecatalog/stack_set_constraint.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/servicecatalog/tag_option.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/servicecatalog/tag_option.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/servicecatalog/tag_option_association.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/servicecatalog/tag_option_association.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/servicecatalogappregistry/_inputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/servicecatalogappregistry/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/servicecatalogappregistry/application.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/servicecatalogappregistry/application.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/servicecatalogappregistry/attribute_group.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/servicecatalogappregistry/attribute_group.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/servicecatalogappregistry/attribute_group_association.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/servicecatalogappregistry/attribute_group_association.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/servicecatalogappregistry/outputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/servicecatalogappregistry/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/servicecatalogappregistry/resource_association.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/servicecatalogappregistry/resource_association.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/servicediscovery/_inputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/servicediscovery/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/servicediscovery/http_namespace.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/servicediscovery/http_namespace.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/servicediscovery/instance.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/servicediscovery/instance.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/servicediscovery/outputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/servicediscovery/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/servicediscovery/private_dns_namespace.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/servicediscovery/private_dns_namespace.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/servicediscovery/public_dns_namespace.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/servicediscovery/public_dns_namespace.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/servicediscovery/service.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/servicediscovery/service.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ses/__init__.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ses/__init__.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ses/_inputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ses/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ses/configuration_set.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ses/configuration_set.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ses/configuration_set_event_destination.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ses/configuration_set_event_destination.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ses/contact_list.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ses/contact_list.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ses/outputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ses/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ses/receipt_filter.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ses/receipt_filter.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ses/receipt_rule.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ses/receipt_rule.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ses/receipt_rule_set.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ses/receipt_rule_set.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ses/template.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ses/template.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/signer/_inputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/signer/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/signer/outputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/signer/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/signer/profile_permission.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/signer/profile_permission.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/signer/signing_profile.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/signer/signing_profile.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/sns/_inputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/sns/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/sns/outputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/sns/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/sns/subscription.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/sns/subscription.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/sns/topic.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/sns/topic.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/sns/topic_policy.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/sns/topic_policy.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/sqs/_inputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/sqs/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/sqs/outputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/sqs/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/sqs/queue.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/sqs/queue.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/sqs/queue_policy.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/sqs/queue_policy.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ssm/__init__.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ssm/__init__.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ssm/_enums.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ssm/_enums.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ssm/_inputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ssm/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ssm/association.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ssm/association.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ssm/document.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ssm/document.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ssm/maintenance_window.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ssm/maintenance_window.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ssm/maintenance_window_target.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ssm/maintenance_window_target.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ssm/maintenance_window_task.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ssm/maintenance_window_task.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ssm/outputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ssm/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ssm/parameter.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ssm/parameter.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ssm/patch_baseline.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ssm/patch_baseline.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ssm/resource_data_sync.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ssm/resource_data_sync.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ssmcontacts/_enums.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ssmcontacts/_enums.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ssmcontacts/_inputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ssmcontacts/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ssmcontacts/contact.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ssmcontacts/contact.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ssmcontacts/contact_channel.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ssmcontacts/contact_channel.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ssmcontacts/outputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ssmcontacts/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ssmincidents/_inputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ssmincidents/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ssmincidents/outputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ssmincidents/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ssmincidents/replication_set.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ssmincidents/replication_set.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/ssmincidents/response_plan.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/ssmincidents/response_plan.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/sso/_enums.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/sso/_enums.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/sso/_inputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/sso/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/sso/assignment.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/sso/assignment.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/sso/instance_access_control_attribute_configuration.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/sso/instance_access_control_attribute_configuration.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/sso/outputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/sso/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/sso/permission_set.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/sso/permission_set.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/stepfunctions/_inputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/stepfunctions/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/stepfunctions/activity.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/stepfunctions/activity.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/stepfunctions/outputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/stepfunctions/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/stepfunctions/state_machine.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/stepfunctions/state_machine.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/synthetics/_inputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/synthetics/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/synthetics/canary.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/synthetics/canary.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/synthetics/outputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/synthetics/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/timestream/_enums.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/timestream/_enums.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/timestream/_inputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/timestream/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/timestream/database.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/timestream/database.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/timestream/outputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/timestream/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/timestream/scheduled_query.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/timestream/scheduled_query.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/timestream/table.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/timestream/table.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/transfer/_enums.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/transfer/_enums.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/transfer/_inputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/transfer/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/transfer/outputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/transfer/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/transfer/server.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/transfer/server.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/transfer/user.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/transfer/user.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/transfer/workflow.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/transfer/workflow.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/waf/_inputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/waf/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/waf/byte_match_set.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/waf/byte_match_set.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/waf/ip_set.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/waf/ip_set.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/waf/outputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/waf/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/waf/rule.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/waf/rule.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/waf/size_constraint_set.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/waf/size_constraint_set.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/waf/sql_injection_match_set.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/waf/sql_injection_match_set.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/waf/web_acl.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/waf/web_acl.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/waf/xss_match_set.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/waf/xss_match_set.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/wafregional/__init__.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/wafregional/__init__.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/wafregional/_inputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/wafregional/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/wafregional/byte_match_set.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/wafregional/byte_match_set.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/wafregional/geo_match_set.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/wafregional/geo_match_set.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/wafregional/ip_set.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/wafregional/ip_set.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/wafregional/outputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/wafregional/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/wafregional/rate_based_rule.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/wafregional/rate_based_rule.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/wafregional/regex_pattern_set.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/wafregional/regex_pattern_set.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/wafregional/rule.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/wafregional/rule.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/wafregional/size_constraint_set.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/wafregional/size_constraint_set.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/wafregional/sql_injection_match_set.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/wafregional/sql_injection_match_set.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/wafregional/web_acl.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/wafregional/web_acl.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/wafregional/web_aclassociation.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/wafregional/web_aclassociation.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/wafregional/xss_match_set.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/wafregional/xss_match_set.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/wafv2/_enums.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/wafv2/_enums.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/wafv2/_inputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/wafv2/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/wafv2/ip_set.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/wafv2/ip_set.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/wafv2/logging_configuration.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/wafv2/logging_configuration.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/wafv2/outputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/wafv2/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/wafv2/regex_pattern_set.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/wafv2/regex_pattern_set.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/wafv2/rule_group.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/wafv2/rule_group.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/wafv2/web_acl.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/wafv2/web_acl.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/wafv2/web_aclassociation.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/wafv2/web_aclassociation.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/wisdom/_enums.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/wisdom/_enums.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/wisdom/_inputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/wisdom/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/wisdom/assistant.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/wisdom/assistant.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/wisdom/assistant_association.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/wisdom/assistant_association.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/wisdom/knowledge_base.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/wisdom/knowledge_base.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/wisdom/outputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/wisdom/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/workspaces/_enums.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/workspaces/_enums.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/workspaces/_inputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/workspaces/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/workspaces/connection_alias.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/workspaces/connection_alias.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/workspaces/outputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/workspaces/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/workspaces/workspace.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/workspaces/workspace.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/xray/_inputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/xray/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/xray/group.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/xray/group.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/xray/outputs.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/xray/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native/xray/sampling_rule.py` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native/xray/sampling_rule.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native.egg-info/PKG-INFO` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native.egg-info/PKG-INFO`

 * *Files 4% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: pulumi-aws-native
-Version: 0.9.1a1641824984
+Version: 0.9.1a1641826769
 Summary: A native Pulumi package for creating and managing Amazon Web Services (AWS) resources.
 Home-page: https://pulumi.com
 License: Apache-2.0
 Project-URL: Repository, https://github.com/pulumi/pulumi-aws-native
 Description: # Pulumi AWS Native Provider (preview)
         
         The Pulumi AWS Native Provider enables you to build, deploy, and manage [any AWS resource that's supported by the AWS Cloud Control API](https://github.com/pulumi/pulumi-aws-native/blob/master/provider/cmd/pulumi-gen-aws-native/supported-types.txt).
```

### Comparing `pulumi_aws_native-0.9.1a1641824984/pulumi_aws_native.egg-info/SOURCES.txt` & `pulumi_aws_native-0.9.1a1641826769/pulumi_aws_native.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `pulumi_aws_native-0.9.1a1641824984/setup.py` & `pulumi_aws_native-0.9.1a1641826769/setup.py`

 * *Files 10% similar despite different names*

```diff
@@ -4,16 +4,16 @@
 
 import errno
 from setuptools import setup, find_packages
 from setuptools.command.install import install
 from subprocess import check_call
 
 
-VERSION = "0.9.1a1641824984"
-PLUGIN_VERSION = "0.9.1-alpha.1641824984+c74e82a1"
+VERSION = "0.9.1a1641826769"
+PLUGIN_VERSION = "0.9.1-alpha.1641826769+561a96a7"
 
 class InstallPluginCommand(install):
     def run(self):
         install.run(self)
         try:
             check_call(['pulumi', 'plugin', 'install', 'resource', 'aws-native', PLUGIN_VERSION])
         except OSError as error:
```

