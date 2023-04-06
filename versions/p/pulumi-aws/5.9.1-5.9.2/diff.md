# Comparing `tmp/pulumi_aws-5.9.1.tar.gz` & `tmp/pulumi_aws-5.9.2.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "dist/pulumi_aws-5.9.1.tar", last modified: Tue Jun 21 22:50:29 2022, max compression
+gzip compressed data, was "dist/pulumi_aws-5.9.2.tar", last modified: Fri Jun 24 22:23:25 2022, max compression
```

## Comparing `pulumi_aws-5.9.1.tar` & `pulumi_aws-5.9.2.tar`

### file list

```diff
@@ -1,2059 +1,2059 @@
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-21 22:50:29.000000 pulumi_aws-5.9.1/
--rw-r--r--   0 runner    (1001) docker     (121)    10151 2022-06-21 22:50:29.000000 pulumi_aws-5.9.1/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (121)     8590 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/README.md
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-21 22:50:28.000000 pulumi_aws-5.9.1/pulumi_aws/
--rw-r--r--   0 runner    (1001) docker     (121)   203842 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     1140 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/_enums.py
--rw-r--r--   0 runner    (1001) docker     (121)   181075 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)     7667 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/_utilities.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-21 22:50:28.000000 pulumi_aws-5.9.1/pulumi_aws/accessanalyzer/
--rw-r--r--   0 runner    (1001) docker     (121)      293 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/accessanalyzer/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    15135 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/accessanalyzer/analyzer.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-21 22:50:28.000000 pulumi_aws-5.9.1/pulumi_aws/account/
--rw-r--r--   0 runner    (1001) docker     (121)      304 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/account/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    18354 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/account/alternative_contact.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-21 22:50:28.000000 pulumi_aws-5.9.1/pulumi_aws/acm/
--rw-r--r--   0 runner    (1001) docker     (121)      410 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/acm/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     6817 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/acm/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    44216 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/acm/certificate.py
--rw-r--r--   0 runner    (1001) docker     (121)    15415 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/acm/certificate_validation.py
--rw-r--r--   0 runner    (1001) docker     (121)    11052 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/acm/get_certificate.py
--rw-r--r--   0 runner    (1001) docker     (121)     7598 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/acm/outputs.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-21 22:50:28.000000 pulumi_aws-5.9.1/pulumi_aws/acmpca/
--rw-r--r--   0 runner    (1001) docker     (121)      521 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/acmpca/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    24902 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/acmpca/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    21275 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/acmpca/certificate.py
--rw-r--r--   0 runner    (1001) docker     (121)    43082 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/acmpca/certificate_authority.py
--rw-r--r--   0 runner    (1001) docker     (121)    20101 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/acmpca/certificate_authority_certificate.py
--rw-r--r--   0 runner    (1001) docker     (121)     5724 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/acmpca/get_certificate.py
--rw-r--r--   0 runner    (1001) docker     (121)    13445 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/acmpca/get_certificate_authority.py
--rw-r--r--   0 runner    (1001) docker     (121)    23238 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/acmpca/outputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    12620 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/acmpca/policy.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-21 22:50:28.000000 pulumi_aws-5.9.1/pulumi_aws/alb/
--rw-r--r--   0 runner    (1001) docker     (121)      614 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/alb/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)      440 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/alb/_enums.py
--rw-r--r--   0 runner    (1001) docker     (121)    98592 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/alb/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)     8158 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/alb/get_listener.py
--rw-r--r--   0 runner    (1001) docker     (121)    13831 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/alb/get_load_balancer.py
--rw-r--r--   0 runner    (1001) docker     (121)    12411 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/alb/get_target_group.py
--rw-r--r--   0 runner    (1001) docker     (121)    40568 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/alb/listener.py
--rw-r--r--   0 runner    (1001) docker     (121)    10903 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/alb/listener_certificate.py
--rw-r--r--   0 runner    (1001) docker     (121)    34480 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/alb/listener_rule.py
--rw-r--r--   0 runner    (1001) docker     (121)    69182 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/alb/load_balancer.py
--rw-r--r--   0 runner    (1001) docker     (121)   108001 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/alb/outputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    61612 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/alb/target_group.py
--rw-r--r--   0 runner    (1001) docker     (121)    18032 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/alb/target_group_attachment.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-21 22:50:28.000000 pulumi_aws-5.9.1/pulumi_aws/amp/
--rw-r--r--   0 runner    (1001) docker     (121)      370 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/amp/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    10626 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/amp/alert_manager_definition.py
--rw-r--r--   0 runner    (1001) docker     (121)    11968 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/amp/rule_group_namespace.py
--rw-r--r--   0 runner    (1001) docker     (121)    15508 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/amp/workspace.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-21 22:50:28.000000 pulumi_aws-5.9.1/pulumi_aws/amplify/
--rw-r--r--   0 runner    (1001) docker     (121)      447 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/amplify/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    15473 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/amplify/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    61933 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/amplify/app.py
--rw-r--r--   0 runner    (1001) docker     (121)    14535 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/amplify/backend_environment.py
--rw-r--r--   0 runner    (1001) docker     (121)    57659 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/amplify/branch.py
--rw-r--r--   0 runner    (1001) docker     (121)    18870 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/amplify/domain_association.py
--rw-r--r--   0 runner    (1001) docker     (121)    14037 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/amplify/outputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    12484 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/amplify/webhook.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-21 22:50:28.000000 pulumi_aws-5.9.1/pulumi_aws/apigateway/
--rw-r--r--   0 runner    (1001) docker     (121)     1169 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/apigateway/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    35129 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/apigateway/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    13087 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/apigateway/account.py
--rw-r--r--   0 runner    (1001) docker     (121)    20255 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/apigateway/api_key.py
--rw-r--r--   0 runner    (1001) docker     (121)    37189 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/apigateway/authorizer.py
--rw-r--r--   0 runner    (1001) docker     (121)    16540 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/apigateway/base_path_mapping.py
--rw-r--r--   0 runner    (1001) docker     (121)    15668 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/apigateway/client_certificate.py
--rw-r--r--   0 runner    (1001) docker     (121)    32058 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/apigateway/deployment.py
--rw-r--r--   0 runner    (1001) docker     (121)    13567 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/apigateway/documentation_part.py
--rw-r--r--   0 runner    (1001) docker     (121)    11928 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/apigateway/documentation_version.py
--rw-r--r--   0 runner    (1001) docker     (121)    71877 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/apigateway/domain_name.py
--rw-r--r--   0 runner    (1001) docker     (121)    11613 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/apigateway/get_domain_name.py
--rw-r--r--   0 runner    (1001) docker     (121)     8428 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/apigateway/get_export.py
--rw-r--r--   0 runner    (1001) docker     (121)     6021 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/apigateway/get_key.py
--rw-r--r--   0 runner    (1001) docker     (121)     5091 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/apigateway/get_resource.py
--rw-r--r--   0 runner    (1001) docker     (121)     9517 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/apigateway/get_rest_api.py
--rw-r--r--   0 runner    (1001) docker     (121)     7942 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/apigateway/get_sdk.py
--rw-r--r--   0 runner    (1001) docker     (121)     6332 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/apigateway/get_vpc_link.py
--rw-r--r--   0 runner    (1001) docker     (121)    71695 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/apigateway/integration.py
--rw-r--r--   0 runner    (1001) docker     (121)    30964 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/apigateway/integration_response.py
--rw-r--r--   0 runner    (1001) docker     (121)    37954 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/apigateway/method.py
--rw-r--r--   0 runner    (1001) docker     (121)    21035 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/apigateway/method_response.py
--rw-r--r--   0 runner    (1001) docker     (121)    18612 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/apigateway/method_settings.py
--rw-r--r--   0 runner    (1001) docker     (121)    13858 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/apigateway/model.py
--rw-r--r--   0 runner    (1001) docker     (121)    36863 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/apigateway/outputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    13613 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/apigateway/request_validator.py
--rw-r--r--   0 runner    (1001) docker     (121)    11667 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/apigateway/resource.py
--rw-r--r--   0 runner    (1001) docker     (121)    17203 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/apigateway/response.py
--rw-r--r--   0 runner    (1001) docker     (121)    71567 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/apigateway/rest_api.py
--rw-r--r--   0 runner    (1001) docker     (121)    10249 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/apigateway/rest_api_policy.py
--rw-r--r--   0 runner    (1001) docker     (121)    49413 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/apigateway/stage.py
--rw-r--r--   0 runner    (1001) docker     (121)    27887 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/apigateway/usage_plan.py
--rw-r--r--   0 runner    (1001) docker     (121)    13442 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/apigateway/usage_plan_key.py
--rw-r--r--   0 runner    (1001) docker     (121)    16707 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/apigateway/vpc_link.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-21 22:50:28.000000 pulumi_aws-5.9.1/pulumi_aws/apigatewayv2/
--rw-r--r--   0 runner    (1001) docker     (121)      692 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/apigatewayv2/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    30148 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/apigatewayv2/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    55324 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/apigatewayv2/api.py
--rw-r--r--   0 runner    (1001) docker     (121)    14151 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/apigatewayv2/api_mapping.py
--rw-r--r--   0 runner    (1001) docker     (121)    39499 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/apigatewayv2/authorizer.py
--rw-r--r--   0 runner    (1001) docker     (121)    13810 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/apigatewayv2/deployment.py
--rw-r--r--   0 runner    (1001) docker     (121)    24087 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/apigatewayv2/domain_name.py
--rw-r--r--   0 runner    (1001) docker     (121)    10509 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/apigatewayv2/get_api.py
--rw-r--r--   0 runner    (1001) docker     (121)     4619 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/apigatewayv2/get_apis.py
--rw-r--r--   0 runner    (1001) docker     (121)     8061 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/apigatewayv2/get_export.py
--rw-r--r--   0 runner    (1001) docker     (121)    75096 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/apigatewayv2/integration.py
--rw-r--r--   0 runner    (1001) docker     (121)    21925 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/apigatewayv2/integration_response.py
--rw-r--r--   0 runner    (1001) docker     (121)    16550 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/apigatewayv2/model.py
--rw-r--r--   0 runner    (1001) docker     (121)    33037 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/apigatewayv2/outputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    43442 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/apigatewayv2/route.py
--rw-r--r--   0 runner    (1001) docker     (121)    17359 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/apigatewayv2/route_response.py
--rw-r--r--   0 runner    (1001) docker     (121)    41165 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/apigatewayv2/stage.py
--rw-r--r--   0 runner    (1001) docker     (121)    17331 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/apigatewayv2/vpc_link.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-21 22:50:28.000000 pulumi_aws-5.9.1/pulumi_aws/appautoscaling/
--rw-r--r--   0 runner    (1001) docker     (121)      390 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/appautoscaling/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    22755 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/appautoscaling/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    22861 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/appautoscaling/outputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    42828 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/appautoscaling/policy.py
--rw-r--r--   0 runner    (1001) docker     (121)    39812 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/appautoscaling/scheduled_action.py
--rw-r--r--   0 runner    (1001) docker     (121)    30990 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/appautoscaling/target.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-21 22:50:28.000000 pulumi_aws-5.9.1/pulumi_aws/appconfig/
--rw-r--r--   0 runner    (1001) docker     (121)      543 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/appconfig/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     3602 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/appconfig/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    14431 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/appconfig/application.py
--rw-r--r--   0 runner    (1001) docker     (121)    34435 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/appconfig/configuration_profile.py
--rw-r--r--   0 runner    (1001) docker     (121)    29431 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/appconfig/deployment.py
--rw-r--r--   0 runner    (1001) docker     (121)    29185 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/appconfig/deployment_strategy.py
--rw-r--r--   0 runner    (1001) docker     (121)    22958 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/appconfig/environment.py
--rw-r--r--   0 runner    (1001) docker     (121)    20776 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/appconfig/event_integration.py
--rw-r--r--   0 runner    (1001) docker     (121)    23444 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/appconfig/hosted_configuration_version.py
--rw-r--r--   0 runner    (1001) docker     (121)     3434 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/appconfig/outputs.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-21 22:50:28.000000 pulumi_aws-5.9.1/pulumi_aws/appflow/
--rw-r--r--   0 runner    (1001) docker     (121)      367 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/appflow/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)   318810 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/appflow/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    26462 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/appflow/connector_profile.py
--rw-r--r--   0 runner    (1001) docker     (121)    37753 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/appflow/flow.py
--rw-r--r--   0 runner    (1001) docker     (121)   326161 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/appflow/outputs.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-21 22:50:28.000000 pulumi_aws-5.9.1/pulumi_aws/applicationloadbalancing/
--rw-r--r--   0 runner    (1001) docker     (121)      614 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/applicationloadbalancing/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)      440 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/applicationloadbalancing/_enums.py
--rw-r--r--   0 runner    (1001) docker     (121)    98592 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/applicationloadbalancing/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)     8610 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/applicationloadbalancing/get_listener.py
--rw-r--r--   0 runner    (1001) docker     (121)    14317 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/applicationloadbalancing/get_load_balancer.py
--rw-r--r--   0 runner    (1001) docker     (121)    12889 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/applicationloadbalancing/get_target_group.py
--rw-r--r--   0 runner    (1001) docker     (121)    40850 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/applicationloadbalancing/listener.py
--rw-r--r--   0 runner    (1001) docker     (121)    11240 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/applicationloadbalancing/listener_certificate.py
--rw-r--r--   0 runner    (1001) docker     (121)    34782 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/applicationloadbalancing/listener_rule.py
--rw-r--r--   0 runner    (1001) docker     (121)    69484 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/applicationloadbalancing/load_balancer.py
--rw-r--r--   0 runner    (1001) docker     (121)   108001 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/applicationloadbalancing/outputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    61909 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/applicationloadbalancing/target_group.py
--rw-r--r--   0 runner    (1001) docker     (121)    18337 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/applicationloadbalancing/target_group_attachment.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-21 22:50:28.000000 pulumi_aws-5.9.1/pulumi_aws/appmesh/
--rw-r--r--   0 runner    (1001) docker     (121)      563 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/appmesh/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)   278013 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/appmesh/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    27745 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/appmesh/gateway_route.py
--rw-r--r--   0 runner    (1001) docker     (121)     7079 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/appmesh/get_mesh.py
--rw-r--r--   0 runner    (1001) docker     (121)     8401 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/appmesh/get_virtual_service.py
--rw-r--r--   0 runner    (1001) docker     (121)    18857 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/appmesh/mesh.py
--rw-r--r--   0 runner    (1001) docker     (121)   277292 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/appmesh/outputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    34208 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/appmesh/route.py
--rw-r--r--   0 runner    (1001) docker     (121)    26819 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/appmesh/virtual_gateway.py
--rw-r--r--   0 runner    (1001) docker     (121)    34516 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/appmesh/virtual_node.py
--rw-r--r--   0 runner    (1001) docker     (121)    25260 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/appmesh/virtual_router.py
--rw-r--r--   0 runner    (1001) docker     (121)    25233 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/appmesh/virtual_service.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-21 22:50:28.000000 pulumi_aws-5.9.1/pulumi_aws/apprunner/
--rw-r--r--   0 runner    (1001) docker     (121)      483 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/apprunner/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    37661 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/apprunner/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    25757 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/apprunner/auto_scaling_configuration_version.py
--rw-r--r--   0 runner    (1001) docker     (121)    16028 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/apprunner/connection.py
--rw-r--r--   0 runner    (1001) docker     (121)    19214 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/apprunner/custom_domain_association.py
--rw-r--r--   0 runner    (1001) docker     (121)    38808 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/apprunner/outputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    43125 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/apprunner/service.py
--rw-r--r--   0 runner    (1001) docker     (121)    22045 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/apprunner/vpc_connector.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-21 22:50:28.000000 pulumi_aws-5.9.1/pulumi_aws/appstream/
--rw-r--r--   0 runner    (1001) docker     (121)      514 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/appstream/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    18918 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/appstream/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    16560 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/appstream/directory_config.py
--rw-r--r--   0 runner    (1001) docker     (121)    51603 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/appstream/fleet.py
--rw-r--r--   0 runner    (1001) docker     (121)     9478 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/appstream/fleet_stack_association.py
--rw-r--r--   0 runner    (1001) docker     (121)    42239 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/appstream/image_builder.py
--rw-r--r--   0 runner    (1001) docker     (121)    20772 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/appstream/outputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    36260 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/appstream/stack.py
--rw-r--r--   0 runner    (1001) docker     (121)    19263 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/appstream/user.py
--rw-r--r--   0 runner    (1001) docker     (121)    14729 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/appstream/user_stack_association.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-21 22:50:28.000000 pulumi_aws-5.9.1/pulumi_aws/appsync/
--rw-r--r--   0 runner    (1001) docker     (121)      535 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/appsync/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    52133 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/appsync/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    18542 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/appsync/api_cache.py
--rw-r--r--   0 runner    (1001) docker     (121)    12034 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/appsync/api_key.py
--rw-r--r--   0 runner    (1001) docker     (121)    31383 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/appsync/data_source.py
--rw-r--r--   0 runner    (1001) docker     (121)    14048 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/appsync/domain_name.py
--rw-r--r--   0 runner    (1001) docker     (121)     8626 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/appsync/domain_name_api_association.py
--rw-r--r--   0 runner    (1001) docker     (121)    29365 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/appsync/function.py
--rw-r--r--   0 runner    (1001) docker     (121)    46549 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/appsync/graph_ql_api.py
--rw-r--r--   0 runner    (1001) docker     (121)    55789 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/appsync/outputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    34156 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/appsync/resolver.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-21 22:50:28.000000 pulumi_aws-5.9.1/pulumi_aws/athena/
--rw-r--r--   0 runner    (1001) docker     (121)      418 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/athena/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    19263 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/athena/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    24629 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/athena/data_catalog.py
--rw-r--r--   0 runner    (1001) docker     (121)    26291 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/athena/database.py
--rw-r--r--   0 runner    (1001) docker     (121)    16068 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/athena/named_query.py
--rw-r--r--   0 runner    (1001) docker     (121)    21006 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/athena/outputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    21675 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/athena/workgroup.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-21 22:50:28.000000 pulumi_aws-5.9.1/pulumi_aws/autoscaling/
--rw-r--r--   0 runner    (1001) docker     (121)      558 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/autoscaling/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     1748 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/autoscaling/_enums.py
--rw-r--r--   0 runner    (1001) docker     (121)   144801 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/autoscaling/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    16273 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/autoscaling/attachment.py
--rw-r--r--   0 runner    (1001) docker     (121)     5977 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/autoscaling/get_ami_ids.py
--rw-r--r--   0 runner    (1001) docker     (121)    14114 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/autoscaling/get_group.py
--rw-r--r--   0 runner    (1001) docker     (121)   145637 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/autoscaling/group.py
--rw-r--r--   0 runner    (1001) docker     (121)    31037 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/autoscaling/lifecycle_hook.py
--rw-r--r--   0 runner    (1001) docker     (121)    13877 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/autoscaling/notification.py
--rw-r--r--   0 runner    (1001) docker     (121)   139988 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/autoscaling/outputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    55718 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/autoscaling/policy.py
--rw-r--r--   0 runner    (1001) docker     (121)    30907 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/autoscaling/schedule.py
--rw-r--r--   0 runner    (1001) docker     (121)     8621 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/autoscaling/tag.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-21 22:50:28.000000 pulumi_aws-5.9.1/pulumi_aws/autoscalingplans/
--rw-r--r--   0 runner    (1001) docker     (121)      342 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/autoscalingplans/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    37628 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/autoscalingplans/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    36367 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/autoscalingplans/outputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    16378 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/autoscalingplans/scaling_plan.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-21 22:50:28.000000 pulumi_aws-5.9.1/pulumi_aws/backup/
--rw-r--r--   0 runner    (1001) docker     (121)      735 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/backup/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    35190 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/backup/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    26988 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/backup/framework.py
--rw-r--r--   0 runner    (1001) docker     (121)     7671 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/backup/get_framework.py
--rw-r--r--   0 runner    (1001) docker     (121)     4884 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/backup/get_plan.py
--rw-r--r--   0 runner    (1001) docker     (121)     7472 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/backup/get_report_plan.py
--rw-r--r--   0 runner    (1001) docker     (121)     5639 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/backup/get_selection.py
--rw-r--r--   0 runner    (1001) docker     (121)     5079 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/backup/get_vault.py
--rw-r--r--   0 runner    (1001) docker     (121)     7425 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/backup/global_settings.py
--rw-r--r--   0 runner    (1001) docker     (121)    41682 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/backup/outputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    19919 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/backup/plan.py
--rw-r--r--   0 runner    (1001) docker     (121)    12261 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/backup/region_settings.py
--rw-r--r--   0 runner    (1001) docker     (121)    27055 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/backup/report_plan.py
--rw-r--r--   0 runner    (1001) docker     (121)    31506 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/backup/selection.py
--rw-r--r--   0 runner    (1001) docker     (121)    15024 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/backup/vault.py
--rw-r--r--   0 runner    (1001) docker     (121)    15559 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/backup/vault_lock_configuration.py
--rw-r--r--   0 runner    (1001) docker     (121)    15388 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/backup/vault_notifications.py
--rw-r--r--   0 runner    (1001) docker     (121)    11511 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/backup/vault_policy.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-21 22:50:28.000000 pulumi_aws-5.9.1/pulumi_aws/batch/
--rw-r--r--   0 runner    (1001) docker     (121)      542 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/batch/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    32642 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/batch/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    40843 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/batch/compute_environment.py
--rw-r--r--   0 runner    (1001) docker     (121)     7979 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/batch/get_compute_environment.py
--rw-r--r--   0 runner    (1001) docker     (121)     7993 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/batch/get_job_queue.py
--rw-r--r--   0 runner    (1001) docker     (121)     4959 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/batch/get_scheduling_policy.py
--rw-r--r--   0 runner    (1001) docker     (121)    37517 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/batch/job_definition.py
--rw-r--r--   0 runner    (1001) docker     (121)    26370 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/batch/job_queue.py
--rw-r--r--   0 runner    (1001) docker     (121)    37266 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/batch/outputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    16390 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/batch/scheduling_policy.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-21 22:50:28.000000 pulumi_aws-5.9.1/pulumi_aws/budgets/
--rw-r--r--   0 runner    (1001) docker     (121)      365 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/budgets/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    26616 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/budgets/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    45784 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/budgets/budget.py
--rw-r--r--   0 runner    (1001) docker     (121)    34780 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/budgets/budget_action.py
--rw-r--r--   0 runner    (1001) docker     (121)    26097 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/budgets/outputs.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-21 22:50:28.000000 pulumi_aws-5.9.1/pulumi_aws/cfg/
--rw-r--r--   0 runner    (1001) docker     (121)      699 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/cfg/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    32730 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/cfg/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    13607 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/cfg/aggregate_authorization.py
--rw-r--r--   0 runner    (1001) docker     (121)    21739 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/cfg/configuration_aggregator.py
--rw-r--r--   0 runner    (1001) docker     (121)    28387 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/cfg/conformance_pack.py
--rw-r--r--   0 runner    (1001) docker     (121)    21947 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/cfg/delivery_channel.py
--rw-r--r--   0 runner    (1001) docker     (121)    34649 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/cfg/organization_conformance_pack.py
--rw-r--r--   0 runner    (1001) docker     (121)    36285 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/cfg/organization_custom_rule.py
--rw-r--r--   0 runner    (1001) docker     (121)    33065 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/cfg/organization_managed_rule.py
--rw-r--r--   0 runner    (1001) docker     (121)    35470 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/cfg/outputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    13775 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/cfg/recorder.py
--rw-r--r--   0 runner    (1001) docker     (121)    11627 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/cfg/recorder_status.py
--rw-r--r--   0 runner    (1001) docker     (121)    33725 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/cfg/remediation_configuration.py
--rw-r--r--   0 runner    (1001) docker     (121)    32351 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/cfg/rule.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-21 22:50:28.000000 pulumi_aws-5.9.1/pulumi_aws/chime/
--rw-r--r--   0 runner    (1001) docker     (121)      604 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/chime/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     6304 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/chime/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)     5486 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/chime/outputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    12580 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/chime/voice_connector.py
--rw-r--r--   0 runner    (1001) docker     (121)    11129 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/chime/voice_connector_group.py
--rw-r--r--   0 runner    (1001) docker     (121)    10112 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/chime/voice_connector_logging.py
--rw-r--r--   0 runner    (1001) docker     (121)    14381 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/chime/voice_connector_organization.py
--rw-r--r--   0 runner    (1001) docker     (121)    15601 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/chime/voice_connector_streaming.py
--rw-r--r--   0 runner    (1001) docker     (121)    19770 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/chime/voice_connector_termination.py
--rw-r--r--   0 runner    (1001) docker     (121)    12644 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/chime/voice_connector_termination_credentials.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-21 22:50:28.000000 pulumi_aws-5.9.1/pulumi_aws/cloud9/
--rw-r--r--   0 runner    (1001) docker     (121)      338 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/cloud9/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    34461 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/cloud9/environment_ec2.py
--rw-r--r--   0 runner    (1001) docker     (121)    13825 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/cloud9/environment_membership.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-21 22:50:28.000000 pulumi_aws-5.9.1/pulumi_aws/cloudcontrol/
--rw-r--r--   0 runner    (1001) docker     (121)      321 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/cloudcontrol/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     6145 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/cloudcontrol/get_resource.py
--rw-r--r--   0 runner    (1001) docker     (121)    18195 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/cloudcontrol/resource.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-21 22:50:28.000000 pulumi_aws-5.9.1/pulumi_aws/cloudformation/
--rw-r--r--   0 runner    (1001) docker     (121)      521 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/cloudformation/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    13376 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/cloudformation/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    36044 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/cloudformation/cloud_formation_type.py
--rw-r--r--   0 runner    (1001) docker     (121)    12006 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/cloudformation/get_cloud_formation_type.py
--rw-r--r--   0 runner    (1001) docker     (121)     5300 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/cloudformation/get_export.py
--rw-r--r--   0 runner    (1001) docker     (121)     8808 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/cloudformation/get_stack.py
--rw-r--r--   0 runner    (1001) docker     (121)    15232 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/cloudformation/outputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    41265 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/cloudformation/stack.py
--rw-r--r--   0 runner    (1001) docker     (121)    54563 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/cloudformation/stack_set.py
--rw-r--r--   0 runner    (1001) docker     (121)    38604 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/cloudformation/stack_set_instance.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-21 22:50:28.000000 pulumi_aws-5.9.1/pulumi_aws/cloudfront/
--rw-r--r--   0 runner    (1001) docker     (121)     1075 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/cloudfront/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)   176699 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/cloudfront/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    25221 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/cloudfront/cache_policy.py
--rw-r--r--   0 runner    (1001) docker     (121)    96004 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/cloudfront/distribution.py
--rw-r--r--   0 runner    (1001) docker     (121)    20439 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/cloudfront/field_level_encryption_config.py
--rw-r--r--   0 runner    (1001) docker     (121)    16600 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/cloudfront/field_level_encryption_profile.py
--rw-r--r--   0 runner    (1001) docker     (121)    19341 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/cloudfront/function.py
--rw-r--r--   0 runner    (1001) docker     (121)     6993 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/cloudfront/get_cache_policy.py
--rw-r--r--   0 runner    (1001) docker     (121)     8214 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/cloudfront/get_distribution.py
--rw-r--r--   0 runner    (1001) docker     (121)     6646 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/cloudfront/get_function.py
--rw-r--r--   0 runner    (1001) docker     (121)     5232 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/cloudfront/get_log_delivery_canonical_user_id.py
--rw-r--r--   0 runner    (1001) docker     (121)     5735 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/cloudfront/get_origin_access_identities.py
--rw-r--r--   0 runner    (1001) docker     (121)     6092 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/cloudfront/get_origin_access_identity.py
--rw-r--r--   0 runner    (1001) docker     (121)     6781 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/cloudfront/get_origin_request_policy.py
--rw-r--r--   0 runner    (1001) docker     (121)     5417 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/cloudfront/get_realtime_log_config.py
--rw-r--r--   0 runner    (1001) docker     (121)     7560 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/cloudfront/get_response_headers_policy.py
--rw-r--r--   0 runner    (1001) docker     (121)    11627 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/cloudfront/key_group.py
--rw-r--r--   0 runner    (1001) docker     (121)    11976 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/cloudfront/monitoring_subscription.py
--rw-r--r--   0 runner    (1001) docker     (121)    19455 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/cloudfront/origin_access_identity.py
--rw-r--r--   0 runner    (1001) docker     (121)    23360 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/cloudfront/origin_request_policy.py
--rw-r--r--   0 runner    (1001) docker     (121)   222138 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/cloudfront/outputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    15247 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/cloudfront/public_key.py
--rw-r--r--   0 runner    (1001) docker     (121)    20098 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/cloudfront/realtime_log_config.py
--rw-r--r--   0 runner    (1001) docker     (121)    30889 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/cloudfront/response_headers_policy.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-21 22:50:28.000000 pulumi_aws-5.9.1/pulumi_aws/cloudhsmv2/
--rw-r--r--   0 runner    (1001) docker     (121)      383 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/cloudhsmv2/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     3222 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/cloudhsmv2/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    25824 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/cloudhsmv2/cluster.py
--rw-r--r--   0 runner    (1001) docker     (121)     6744 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/cloudhsmv2/get_cluster.py
--rw-r--r--   0 runner    (1001) docker     (121)    16530 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/cloudhsmv2/hsm.py
--rw-r--r--   0 runner    (1001) docker     (121)     4785 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/cloudhsmv2/outputs.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-21 22:50:28.000000 pulumi_aws-5.9.1/pulumi_aws/cloudsearch/
--rw-r--r--   0 runner    (1001) docker     (121)      380 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/cloudsearch/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    12450 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/cloudsearch/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    24612 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/cloudsearch/domain.py
--rw-r--r--   0 runner    (1001) docker     (121)    11233 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/cloudsearch/domain_service_access_policy.py
--rw-r--r--   0 runner    (1001) docker     (121)    12014 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/cloudsearch/outputs.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-21 22:50:28.000000 pulumi_aws-5.9.1/pulumi_aws/cloudtrail/
--rw-r--r--   0 runner    (1001) docker     (121)      430 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/cloudtrail/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    24249 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/cloudtrail/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    36099 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/cloudtrail/event_data_store.py
--rw-r--r--   0 runner    (1001) docker     (121)     7056 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/cloudtrail/get_function.py
--rw-r--r--   0 runner    (1001) docker     (121)     5678 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/cloudtrail/get_service_account.py
--rw-r--r--   0 runner    (1001) docker     (121)    23183 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/cloudtrail/outputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    75455 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/cloudtrail/trail.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-21 22:50:28.000000 pulumi_aws-5.9.1/pulumi_aws/cloudwatch/
--rw-r--r--   0 runner    (1001) docker     (121)     1083 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/cloudwatch/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    86079 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/cloudwatch/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    32423 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/cloudwatch/composite_alarm.py
--rw-r--r--   0 runner    (1001) docker     (121)    13384 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/cloudwatch/dashboard.py
--rw-r--r--   0 runner    (1001) docker     (121)    22231 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/cloudwatch/event_api_destination.py
--rw-r--r--   0 runner    (1001) docker     (121)    18597 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/cloudwatch/event_archive.py
--rw-r--r--   0 runner    (1001) docker     (121)    16009 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/cloudwatch/event_bus.py
--rw-r--r--   0 runner    (1001) docker     (121)    16665 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/cloudwatch/event_bus_policy.py
--rw-r--r--   0 runner    (1001) docker     (121)    25515 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/cloudwatch/event_connection.py
--rw-r--r--   0 runner    (1001) docker     (121)    19895 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/cloudwatch/event_permission.py
--rw-r--r--   0 runner    (1001) docker     (121)    33255 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/cloudwatch/event_rule.py
--rw-r--r--   0 runner    (1001) docker     (121)    73858 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/cloudwatch/event_target.py
--rw-r--r--   0 runner    (1001) docker     (121)     3486 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/cloudwatch/get_event_bus.py
--rw-r--r--   0 runner    (1001) docker     (121)     4853 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/cloudwatch/get_event_connection.py
--rw-r--r--   0 runner    (1001) docker     (121)     5501 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/cloudwatch/get_event_source.py
--rw-r--r--   0 runner    (1001) docker     (121)     5884 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/cloudwatch/get_log_group.py
--rw-r--r--   0 runner    (1001) docker     (121)     4260 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/cloudwatch/get_log_groups.py
--rw-r--r--   0 runner    (1001) docker     (121)    11998 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/cloudwatch/log_destination.py
--rw-r--r--   0 runner    (1001) docker     (121)    13682 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/cloudwatch/log_destination_policy.py
--rw-r--r--   0 runner    (1001) docker     (121)    23294 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/cloudwatch/log_group.py
--rw-r--r--   0 runner    (1001) docker     (121)    15504 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/cloudwatch/log_metric_filter.py
--rw-r--r--   0 runner    (1001) docker     (121)    13196 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/cloudwatch/log_resource_policy.py
--rw-r--r--   0 runner    (1001) docker     (121)     9956 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/cloudwatch/log_stream.py
--rw-r--r--   0 runner    (1001) docker     (121)    21782 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/cloudwatch/log_subscription_filter.py
--rw-r--r--   0 runner    (1001) docker     (121)    83958 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/cloudwatch/metric_alarm.py
--rw-r--r--   0 runner    (1001) docker     (121)    51529 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/cloudwatch/metric_stream.py
--rw-r--r--   0 runner    (1001) docker     (121)    84523 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/cloudwatch/outputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    13536 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/cloudwatch/query_definition.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-21 22:50:28.000000 pulumi_aws-5.9.1/pulumi_aws/codeartifact/
--rw-r--r--   0 runner    (1001) docker     (121)      519 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/codeartifact/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     2807 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/codeartifact/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    21250 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/codeartifact/domain.py
--rw-r--r--   0 runner    (1001) docker     (121)    16987 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/codeartifact/domain_permissions.py
--rw-r--r--   0 runner    (1001) docker     (121)     6344 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/codeartifact/get_authorization_token.py
--rw-r--r--   0 runner    (1001) docker     (121)     6416 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/codeartifact/get_repository_endpoint.py
--rw-r--r--   0 runner    (1001) docker     (121)     3390 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/codeartifact/outputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    29357 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/codeartifact/repository.py
--rw-r--r--   0 runner    (1001) docker     (121)    19899 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/codeartifact/repository_permissions_policy.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-21 22:50:28.000000 pulumi_aws-5.9.1/pulumi_aws/codebuild/
--rw-r--r--   0 runner    (1001) docker     (121)      452 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/codebuild/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    86494 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/codebuild/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    81754 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/codebuild/outputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    82917 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/codebuild/project.py
--rw-r--r--   0 runner    (1001) docker     (121)    23135 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/codebuild/report_group.py
--rw-r--r--   0 runner    (1001) docker     (121)    13286 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/codebuild/resource_policy.py
--rw-r--r--   0 runner    (1001) docker     (121)    16676 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/codebuild/source_credential.py
--rw-r--r--   0 runner    (1001) docker     (121)    24773 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/codebuild/webhook.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-21 22:50:28.000000 pulumi_aws-5.9.1/pulumi_aws/codecommit/
--rw-r--r--   0 runner    (1001) docker     (121)      523 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/codecommit/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     4436 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/codecommit/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    18955 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/codecommit/approval_rule_template.py
--rw-r--r--   0 runner    (1001) docker     (121)    10565 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/codecommit/approval_rule_template_association.py
--rw-r--r--   0 runner    (1001) docker     (121)     7432 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/codecommit/get_approval_rule_template.py
--rw-r--r--   0 runner    (1001) docker     (121)     5361 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/codecommit/get_repository.py
--rw-r--r--   0 runner    (1001) docker     (121)     4121 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/codecommit/outputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    20253 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/codecommit/repository.py
--rw-r--r--   0 runner    (1001) docker     (121)     9909 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/codecommit/trigger.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-21 22:50:28.000000 pulumi_aws-5.9.1/pulumi_aws/codedeploy/
--rw-r--r--   0 runner    (1001) docker     (121)      406 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/codedeploy/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    49133 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/codedeploy/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    18533 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/codedeploy/application.py
--rw-r--r--   0 runner    (1001) docker     (121)    22789 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/codedeploy/deployment_config.py
--rw-r--r--   0 runner    (1001) docker     (121)    72884 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/codedeploy/deployment_group.py
--rw-r--r--   0 runner    (1001) docker     (121)    48707 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/codedeploy/outputs.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-21 22:50:28.000000 pulumi_aws-5.9.1/pulumi_aws/codepipeline/
--rw-r--r--   0 runner    (1001) docker     (121)      361 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/codepipeline/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    18164 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/codepipeline/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    16639 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/codepipeline/outputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    28681 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/codepipeline/pipeline.py
--rw-r--r--   0 runner    (1001) docker     (121)    31259 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/codepipeline/webhook.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-21 22:50:28.000000 pulumi_aws-5.9.1/pulumi_aws/codestarconnections/
--rw-r--r--   0 runner    (1001) docker     (121)      390 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/codestarconnections/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     3664 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/codestarconnections/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    22770 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/codestarconnections/connection.py
--rw-r--r--   0 runner    (1001) docker     (121)     6616 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/codestarconnections/get_connection.py
--rw-r--r--   0 runner    (1001) docker     (121)    18005 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/codestarconnections/host.py
--rw-r--r--   0 runner    (1001) docker     (121)     3637 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/codestarconnections/outputs.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-21 22:50:28.000000 pulumi_aws-5.9.1/pulumi_aws/codestarnotifications/
--rw-r--r--   0 runner    (1001) docker     (121)      347 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/codestarnotifications/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     2270 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/codestarnotifications/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    27263 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/codestarnotifications/notification_rule.py
--rw-r--r--   0 runner    (1001) docker     (121)     1796 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/codestarnotifications/outputs.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-21 22:50:28.000000 pulumi_aws-5.9.1/pulumi_aws/cognito/
--rw-r--r--   0 runner    (1001) docker     (121)      862 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/cognito/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    66712 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/cognito/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    18725 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/cognito/get_user_pool_client.py
--rw-r--r--   0 runner    (1001) docker     (121)     4264 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/cognito/get_user_pool_clients.py
--rw-r--r--   0 runner    (1001) docker     (121)     3933 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/cognito/get_user_pool_signing_certificate.py
--rw-r--r--   0 runner    (1001) docker     (121)     4695 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/cognito/get_user_pools.py
--rw-r--r--   0 runner    (1001) docker     (121)    35481 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/cognito/identity_pool.py
--rw-r--r--   0 runner    (1001) docker     (121)    13593 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/cognito/identity_pool_provider_principal_tag.py
--rw-r--r--   0 runner    (1001) docker     (121)    17631 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/cognito/identity_pool_role_attachment.py
--rw-r--r--   0 runner    (1001) docker     (121)    21931 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/cognito/identity_provider.py
--rw-r--r--   0 runner    (1001) docker     (121)    73184 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/cognito/outputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    14941 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/cognito/resource_server.py
--rw-r--r--   0 runner    (1001) docker     (121)    53262 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/cognito/user.py
--rw-r--r--   0 runner    (1001) docker     (121)    15583 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/cognito/user_group.py
--rw-r--r--   0 runner    (1001) docker     (121)    11574 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/cognito/user_in_group.py
--rw-r--r--   0 runner    (1001) docker     (121)    90511 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/cognito/user_pool.py
--rw-r--r--   0 runner    (1001) docker     (121)    73606 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/cognito/user_pool_client.py
--rw-r--r--   0 runner    (1001) docker     (121)    18109 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/cognito/user_pool_domain.py
--rw-r--r--   0 runner    (1001) docker     (121)    23695 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/cognito/user_pool_ui_customization.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-21 22:50:28.000000 pulumi_aws-5.9.1/pulumi_aws/config/
--rw-r--r--   0 runner    (1001) docker     (121)      285 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/config/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)   107985 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/config/outputs.py
--rw-r--r--   0 runner    (1001) docker     (121)     8173 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/config/vars.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-21 22:50:28.000000 pulumi_aws-5.9.1/pulumi_aws/connect/
--rw-r--r--   0 runner    (1001) docker     (121)     1116 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/connect/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    54095 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/connect/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    14391 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/connect/bot_association.py
--rw-r--r--   0 runner    (1001) docker     (121)    30680 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/connect/contact_flow.py
--rw-r--r--   0 runner    (1001) docker     (121)    30141 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/connect/contact_flow_module.py
--rw-r--r--   0 runner    (1001) docker     (121)     4555 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/connect/get_bot_association.py
--rw-r--r--   0 runner    (1001) docker     (121)     7962 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/connect/get_contact_flow.py
--rw-r--r--   0 runner    (1001) docker     (121)     8686 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/connect/get_contact_flow_module.py
--rw-r--r--   0 runner    (1001) docker     (121)     9505 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/connect/get_hours_of_operation.py
--rw-r--r--   0 runner    (1001) docker     (121)    10692 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/connect/get_instance.py
--rw-r--r--   0 runner    (1001) docker     (121)     4612 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/connect/get_lambda_function_association.py
--rw-r--r--   0 runner    (1001) docker     (121)     4527 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/connect/get_prompt.py
--rw-r--r--   0 runner    (1001) docker     (121)     8995 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/connect/get_queue.py
--rw-r--r--   0 runner    (1001) docker     (121)     7879 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/connect/get_quick_connect.py
--rw-r--r--   0 runner    (1001) docker     (121)     9368 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/connect/get_routing_profile.py
--rw-r--r--   0 runner    (1001) docker     (121)     8342 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/connect/get_security_profile.py
--rw-r--r--   0 runner    (1001) docker     (121)     4156 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/connect/get_user_hierarchy_structure.py
--rw-r--r--   0 runner    (1001) docker     (121)    27398 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/connect/hours_of_operation.py
--rw-r--r--   0 runner    (1001) docker     (121)    35574 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/connect/instance.py
--rw-r--r--   0 runner    (1001) docker     (121)    10774 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/connect/lambda_function_association.py
--rw-r--r--   0 runner    (1001) docker     (121)    73245 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/connect/outputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    35890 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/connect/queue.py
--rw-r--r--   0 runner    (1001) docker     (121)    23638 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/connect/quick_connect.py
--rw-r--r--   0 runner    (1001) docker     (121)    32521 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/connect/routing_profile.py
--rw-r--r--   0 runner    (1001) docker     (121)    23343 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/connect/security_profile.py
--rw-r--r--   0 runner    (1001) docker     (121)    24705 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/connect/user_hierarchy_group.py
--rw-r--r--   0 runner    (1001) docker     (121)    13706 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/connect/user_hierarchy_structure.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-21 22:50:28.000000 pulumi_aws-5.9.1/pulumi_aws/costexplorer/
--rw-r--r--   0 runner    (1001) docker     (121)      431 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/costexplorer/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    94491 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/costexplorer/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    17207 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/costexplorer/anomaly_monitor.py
--rw-r--r--   0 runner    (1001) docker     (121)    22774 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/costexplorer/cost_category.py
--rw-r--r--   0 runner    (1001) docker     (121)     6395 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/costexplorer/get_cost_category.py
--rw-r--r--   0 runner    (1001) docker     (121)     7096 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/costexplorer/get_tags.py
--rw-r--r--   0 runner    (1001) docker     (121)   121588 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/costexplorer/outputs.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-21 22:50:28.000000 pulumi_aws-5.9.1/pulumi_aws/cur/
--rw-r--r--   0 runner    (1001) docker     (121)      339 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/cur/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     9003 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/cur/get_report_definition.py
--rw-r--r--   0 runner    (1001) docker     (121)    35405 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/cur/report_definition.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-21 22:50:28.000000 pulumi_aws-5.9.1/pulumi_aws/dataexchange/
--rw-r--r--   0 runner    (1001) docker     (121)      317 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/dataexchange/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    17250 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/dataexchange/data_set.py
--rw-r--r--   0 runner    (1001) docker     (121)    15878 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/dataexchange/revision.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-21 22:50:28.000000 pulumi_aws-5.9.1/pulumi_aws/datapipeline/
--rw-r--r--   0 runner    (1001) docker     (121)      440 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/datapipeline/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     8813 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/datapipeline/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)     4521 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/datapipeline/get_pipeline.py
--rw-r--r--   0 runner    (1001) docker     (121)     5847 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/datapipeline/get_pipeline_definition.py
--rw-r--r--   0 runner    (1001) docker     (121)    12685 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/datapipeline/outputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    12326 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/datapipeline/pipeline.py
--rw-r--r--   0 runner    (1001) docker     (121)    21912 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/datapipeline/pipeline_definition.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-21 22:50:28.000000 pulumi_aws-5.9.1/pulumi_aws/datasync/
--rw-r--r--   0 runner    (1001) docker     (121)      606 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/datasync/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    27590 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/datasync/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    29878 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/datasync/agent.py
--rw-r--r--   0 runner    (1001) docker     (121)    18956 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/datasync/efs_location.py
--rw-r--r--   0 runner    (1001) docker     (121)    25463 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/datasync/fsx_open_zfs_file_system.py
--rw-r--r--   0 runner    (1001) docker     (121)    21841 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/datasync/location_fsx_lustre.py
--rw-r--r--   0 runner    (1001) docker     (121)    27324 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/datasync/location_fsx_windows.py
--rw-r--r--   0 runner    (1001) docker     (121)    50555 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/datasync/location_hdfs.py
--rw-r--r--   0 runner    (1001) docker     (121)    28193 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/datasync/location_smb.py
--rw-r--r--   0 runner    (1001) docker     (121)    22296 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/datasync/nfs_location.py
--rw-r--r--   0 runner    (1001) docker     (121)    27796 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/datasync/outputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    23994 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/datasync/s3_location.py
--rw-r--r--   0 runner    (1001) docker     (121)    29776 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/datasync/task.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-21 22:50:28.000000 pulumi_aws-5.9.1/pulumi_aws/dax/
--rw-r--r--   0 runner    (1001) docker     (121)      396 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/dax/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     4044 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/dax/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    52164 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/dax/cluster.py
--rw-r--r--   0 runner    (1001) docker     (121)     3521 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/dax/outputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    11273 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/dax/parameter_group.py
--rw-r--r--   0 runner    (1001) docker     (121)    11347 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/dax/subnet_group.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-21 22:50:28.000000 pulumi_aws-5.9.1/pulumi_aws/detective/
--rw-r--r--   0 runner    (1001) docker     (121)      347 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/detective/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    11407 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/detective/graph.py
--rw-r--r--   0 runner    (1001) docker     (121)     8382 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/detective/invitation_accepter.py
--rw-r--r--   0 runner    (1001) docker     (121)    25080 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/detective/member.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-21 22:50:28.000000 pulumi_aws-5.9.1/pulumi_aws/devicefarm/
--rw-r--r--   0 runner    (1001) docker     (121)      482 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/devicefarm/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     4949 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/devicefarm/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    22351 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/devicefarm/device_pool.py
--rw-r--r--   0 runner    (1001) docker     (121)    24257 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/devicefarm/instance_profile.py
--rw-r--r--   0 runner    (1001) docker     (121)    40408 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/devicefarm/network_profile.py
--rw-r--r--   0 runner    (1001) docker     (121)     4546 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/devicefarm/outputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    15864 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/devicefarm/project.py
--rw-r--r--   0 runner    (1001) docker     (121)    17914 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/devicefarm/test_grid_project.py
--rw-r--r--   0 runner    (1001) docker     (121)    20266 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/devicefarm/upload.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-21 22:50:28.000000 pulumi_aws-5.9.1/pulumi_aws/directconnect/
--rw-r--r--   0 runner    (1001) docker     (121)     1118 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/directconnect/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    21880 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/directconnect/bgp_peer.py
--rw-r--r--   0 runner    (1001) docker     (121)    25773 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/directconnect/connection.py
--rw-r--r--   0 runner    (1001) docker     (121)     9173 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/directconnect/connection_association.py
--rw-r--r--   0 runner    (1001) docker     (121)     6530 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/directconnect/connection_confirmation.py
--rw-r--r--   0 runner    (1001) docker     (121)    10139 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/directconnect/gateway.py
--rw-r--r--   0 runner    (1001) docker     (121)    30877 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/directconnect/gateway_association.py
--rw-r--r--   0 runner    (1001) docker     (121)    21361 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/directconnect/gateway_association_proposal.py
--rw-r--r--   0 runner    (1001) docker     (121)     6538 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/directconnect/get_connection.py
--rw-r--r--   0 runner    (1001) docker     (121)     3895 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/directconnect/get_gateway.py
--rw-r--r--   0 runner    (1001) docker     (121)     6043 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/directconnect/get_location.py
--rw-r--r--   0 runner    (1001) docker     (121)     2921 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/directconnect/get_locations.py
--rw-r--r--   0 runner    (1001) docker     (121)    28816 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/directconnect/hosted_connection.py
--rw-r--r--   0 runner    (1001) docker     (121)    31972 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/directconnect/hosted_private_virtual_interface.py
--rw-r--r--   0 runner    (1001) docker     (121)    19989 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/directconnect/hosted_private_virtual_interface_accepter.py
--rw-r--r--   0 runner    (1001) docker     (121)    30888 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/directconnect/hosted_public_virtual_interface.py
--rw-r--r--   0 runner    (1001) docker     (121)    15370 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/directconnect/hosted_public_virtual_interface_accepter.py
--rw-r--r--   0 runner    (1001) docker     (121)    32040 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/directconnect/hosted_transit_virtual_interface.py
--rw-r--r--   0 runner    (1001) docker     (121)    18978 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/directconnect/hosted_transit_virtual_interface_acceptor.py
--rw-r--r--   0 runner    (1001) docker     (121)    30178 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/directconnect/link_aggregation_group.py
--rw-r--r--   0 runner    (1001) docker     (121)    39909 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/directconnect/private_virtual_interface.py
--rw-r--r--   0 runner    (1001) docker     (121)    32590 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/directconnect/public_virtual_interface.py
--rw-r--r--   0 runner    (1001) docker     (121)    38324 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/directconnect/transit_virtual_interface.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-21 22:50:28.000000 pulumi_aws-5.9.1/pulumi_aws/directoryservice/
--rw-r--r--   0 runner    (1001) docker     (121)      431 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/directoryservice/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     6343 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/directoryservice/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    11874 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/directoryservice/conditional_forwader.py
--rw-r--r--   0 runner    (1001) docker     (121)    42616 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/directoryservice/directory.py
--rw-r--r--   0 runner    (1001) docker     (121)    10586 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/directoryservice/get_directory.py
--rw-r--r--   0 runner    (1001) docker     (121)    12830 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/directoryservice/log_service.py
--rw-r--r--   0 runner    (1001) docker     (121)     9982 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/directoryservice/outputs.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-21 22:50:28.000000 pulumi_aws-5.9.1/pulumi_aws/dlm/
--rw-r--r--   0 runner    (1001) docker     (121)      346 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/dlm/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    55991 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/dlm/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    29352 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/dlm/lifecycle_policy.py
--rw-r--r--   0 runner    (1001) docker     (121)    56336 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/dlm/outputs.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-21 22:50:28.000000 pulumi_aws-5.9.1/pulumi_aws/dms/
--rw-r--r--   0 runner    (1001) docker     (121)      507 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/dms/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    66045 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/dms/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    18471 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/dms/certificate.py
--rw-r--r--   0 runner    (1001) docker     (121)    68131 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/dms/endpoint.py
--rw-r--r--   0 runner    (1001) docker     (121)    23673 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/dms/event_subscription.py
--rw-r--r--   0 runner    (1001) docker     (121)    59960 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/dms/outputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    61278 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/dms/replication_instance.py
--rw-r--r--   0 runner    (1001) docker     (121)    20305 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/dms/replication_subnet_group.py
--rw-r--r--   0 runner    (1001) docker     (121)    41962 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/dms/replication_task.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-21 22:50:28.000000 pulumi_aws-5.9.1/pulumi_aws/docdb/
--rw-r--r--   0 runner    (1001) docker     (121)      607 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/docdb/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     3564 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/docdb/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    82759 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/docdb/cluster.py
--rw-r--r--   0 runner    (1001) docker     (121)    58376 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/docdb/cluster_instance.py
--rw-r--r--   0 runner    (1001) docker     (121)    22098 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/docdb/cluster_parameter_group.py
--rw-r--r--   0 runner    (1001) docker     (121)    22875 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/docdb/cluster_snapshot.py
--rw-r--r--   0 runner    (1001) docker     (121)    31024 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/docdb/event_subscription.py
--rw-r--r--   0 runner    (1001) docker     (121)    10215 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/docdb/get_engine_version.py
--rw-r--r--   0 runner    (1001) docker     (121)     8934 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/docdb/get_orderable_db_instance.py
--rw-r--r--   0 runner    (1001) docker     (121)    28361 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/docdb/global_cluster.py
--rw-r--r--   0 runner    (1001) docker     (121)     4028 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/docdb/outputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    19151 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/docdb/subnet_group.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-21 22:50:28.000000 pulumi_aws-5.9.1/pulumi_aws/dynamodb/
--rw-r--r--   0 runner    (1001) docker     (121)      514 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/dynamodb/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    16777 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/dynamodb/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)     8888 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/dynamodb/contributor_insights.py
--rw-r--r--   0 runner    (1001) docker     (121)    11987 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/dynamodb/get_table.py
--rw-r--r--   0 runner    (1001) docker     (121)    14562 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/dynamodb/global_table.py
--rw-r--r--   0 runner    (1001) docker     (121)    11148 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/dynamodb/kinesis_streaming_destination.py
--rw-r--r--   0 runner    (1001) docker     (121)    22116 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/dynamodb/outputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    70444 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/dynamodb/table.py
--rw-r--r--   0 runner    (1001) docker     (121)    15279 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/dynamodb/table_item.py
--rw-r--r--   0 runner    (1001) docker     (121)     9204 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/dynamodb/tag.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-21 22:50:28.000000 pulumi_aws-5.9.1/pulumi_aws/ebs/
--rw-r--r--   0 runner    (1001) docker     (121)      681 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ebs/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    10723 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ebs/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)     8377 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ebs/default_kms_key.py
--rw-r--r--   0 runner    (1001) docker     (121)     7392 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ebs/encryption_by_default.py
--rw-r--r--   0 runner    (1001) docker     (121)     2633 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ebs/get_default_kms_key.py
--rw-r--r--   0 runner    (1001) docker     (121)     4463 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ebs/get_ebs_volumes.py
--rw-r--r--   0 runner    (1001) docker     (121)     2482 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ebs/get_encryption_by_default.py
--rw-r--r--   0 runner    (1001) docker     (121)    14728 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ebs/get_snapshot.py
--rw-r--r--   0 runner    (1001) docker     (121)     6470 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ebs/get_snapshot_ids.py
--rw-r--r--   0 runner    (1001) docker     (121)    11339 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ebs/get_volume.py
--rw-r--r--   0 runner    (1001) docker     (121)    10320 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ebs/outputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    31525 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ebs/snapshot.py
--rw-r--r--   0 runner    (1001) docker     (121)    33170 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ebs/snapshot_copy.py
--rw-r--r--   0 runner    (1001) docker     (121)    39908 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ebs/snapshot_import.py
--rw-r--r--   0 runner    (1001) docker     (121)    33092 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ebs/volume.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-21 22:50:28.000000 pulumi_aws-5.9.1/pulumi_aws/ec2/
--rw-r--r--   0 runner    (1001) docker     (121)     5396 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ec2/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    14508 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ec2/_enums.py
--rw-r--r--   0 runner    (1001) docker     (121)   485832 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ec2/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    64164 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ec2/ami.py
--rw-r--r--   0 runner    (1001) docker     (121)    62901 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ec2/ami_copy.py
--rw-r--r--   0 runner    (1001) docker     (121)    55704 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ec2/ami_from_instance.py
--rw-r--r--   0 runner    (1001) docker     (121)    16444 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ec2/ami_launch_permission.py
--rw-r--r--   0 runner    (1001) docker     (121)     9831 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ec2/availability_zone_group.py
--rw-r--r--   0 runner    (1001) docker     (121)    40792 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ec2/capacity_reservation.py
--rw-r--r--   0 runner    (1001) docker     (121)    13591 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ec2/carrier_gateway.py
--rw-r--r--   0 runner    (1001) docker     (121)    21044 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ec2/customer_gateway.py
--rw-r--r--   0 runner    (1001) docker     (121)    27168 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ec2/dedicated_host.py
--rw-r--r--   0 runner    (1001) docker     (121)    34225 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ec2/default_network_acl.py
--rw-r--r--   0 runner    (1001) docker     (121)    24139 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ec2/default_route_table.py
--rw-r--r--   0 runner    (1001) docker     (121)    28652 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ec2/default_security_group.py
--rw-r--r--   0 runner    (1001) docker     (121)    40214 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ec2/default_subnet.py
--rw-r--r--   0 runner    (1001) docker     (121)    34748 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ec2/default_vpc.py
--rw-r--r--   0 runner    (1001) docker     (121)    20289 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ec2/default_vpc_dhcp_options.py
--rw-r--r--   0 runner    (1001) docker     (121)    12312 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ec2/egress_only_internet_gateway.py
--rw-r--r--   0 runner    (1001) docker     (121)    44648 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ec2/eip.py
--rw-r--r--   0 runner    (1001) docker     (121)    23192 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ec2/eip_association.py
--rw-r--r--   0 runner    (1001) docker     (121)    39855 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ec2/fleet.py
--rw-r--r--   0 runner    (1001) docker     (121)    40861 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ec2/flow_log.py
--rw-r--r--   0 runner    (1001) docker     (121)    25840 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ec2/get_ami.py
--rw-r--r--   0 runner    (1001) docker     (121)     8332 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ec2/get_ami_ids.py
--rw-r--r--   0 runner    (1001) docker     (121)     6998 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ec2/get_coip_pool.py
--rw-r--r--   0 runner    (1001) docker     (121)     4226 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ec2/get_coip_pools.py
--rw-r--r--   0 runner    (1001) docker     (121)     7907 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ec2/get_customer_gateway.py
--rw-r--r--   0 runner    (1001) docker     (121)     9845 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ec2/get_dedicated_host.py
--rw-r--r--   0 runner    (1001) docker     (121)     5265 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ec2/get_eips.py
--rw-r--r--   0 runner    (1001) docker     (121)    13917 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ec2/get_elastic_ip.py
--rw-r--r--   0 runner    (1001) docker     (121)    31213 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ec2/get_instance.py
--rw-r--r--   0 runner    (1001) docker     (121)    41419 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ec2/get_instance_type.py
--rw-r--r--   0 runner    (1001) docker     (121)     7250 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ec2/get_instance_type_offering.py
--rw-r--r--   0 runner    (1001) docker     (121)     7163 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ec2/get_instance_type_offerings.py
--rw-r--r--   0 runner    (1001) docker     (121)     5327 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ec2/get_instance_types.py
--rw-r--r--   0 runner    (1001) docker     (121)     7741 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ec2/get_instances.py
--rw-r--r--   0 runner    (1001) docker     (121)     6779 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ec2/get_internet_gateway.py
--rw-r--r--   0 runner    (1001) docker     (121)     6008 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ec2/get_ipam_preview_next_cidr.py
--rw-r--r--   0 runner    (1001) docker     (121)     6750 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ec2/get_key_pair.py
--rw-r--r--   0 runner    (1001) docker     (121)    13646 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ec2/get_launch_configuration.py
--rw-r--r--   0 runner    (1001) docker     (121)    24338 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ec2/get_launch_template.py
--rw-r--r--   0 runner    (1001) docker     (121)     6394 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ec2/get_local_gateway.py
--rw-r--r--   0 runner    (1001) docker     (121)     8593 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ec2/get_local_gateway_route_table.py
--rw-r--r--   0 runner    (1001) docker     (121)     4582 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ec2/get_local_gateway_route_tables.py
--rw-r--r--   0 runner    (1001) docker     (121)     9586 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ec2/get_local_gateway_virtual_interface.py
--rw-r--r--   0 runner    (1001) docker     (121)     7551 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ec2/get_local_gateway_virtual_interface_group.py
--rw-r--r--   0 runner    (1001) docker     (121)     6784 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ec2/get_local_gateway_virtual_interface_groups.py
--rw-r--r--   0 runner    (1001) docker     (121)     4938 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ec2/get_local_gateways.py
--rw-r--r--   0 runner    (1001) docker     (121)     9326 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ec2/get_managed_prefix_list.py
--rw-r--r--   0 runner    (1001) docker     (121)     9672 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ec2/get_nat_gateway.py
--rw-r--r--   0 runner    (1001) docker     (121)     4879 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ec2/get_nat_gateways.py
--rw-r--r--   0 runner    (1001) docker     (121)     6677 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ec2/get_network_acls.py
--rw-r--r--   0 runner    (1001) docker     (121)    13414 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ec2/get_network_interface.py
--rw-r--r--   0 runner    (1001) docker     (121)     6274 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ec2/get_network_interfaces.py
--rw-r--r--   0 runner    (1001) docker     (121)     7111 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ec2/get_prefix_list.py
--rw-r--r--   0 runner    (1001) docker     (121)    16232 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ec2/get_route.py
--rw-r--r--   0 runner    (1001) docker     (121)    10450 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ec2/get_route_table.py
--rw-r--r--   0 runner    (1001) docker     (121)     4879 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ec2/get_route_tables.py
--rw-r--r--   0 runner    (1001) docker     (121)     7898 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ec2/get_security_group.py
--rw-r--r--   0 runner    (1001) docker     (121)     6644 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ec2/get_security_groups.py
--rw-r--r--   0 runner    (1001) docker     (121)     2480 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ec2/get_serial_console_access.py
--rw-r--r--   0 runner    (1001) docker     (121)     6843 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ec2/get_spot_price.py
--rw-r--r--   0 runner    (1001) docker     (121)    21289 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ec2/get_subnet.py
--rw-r--r--   0 runner    (1001) docker     (121)     5231 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ec2/get_subnet_ids.py
--rw-r--r--   0 runner    (1001) docker     (121)     4016 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ec2/get_subnets.py
--rw-r--r--   0 runner    (1001) docker     (121)     5333 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ec2/get_transit_gateway_route_tables.py
--rw-r--r--   0 runner    (1001) docker     (121)    12158 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ec2/get_vpc.py
--rw-r--r--   0 runner    (1001) docker     (121)     9664 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ec2/get_vpc_dhcp_options.py
--rw-r--r--   0 runner    (1001) docker     (121)    14931 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ec2/get_vpc_endpoint.py
--rw-r--r--   0 runner    (1001) docker     (121)    14017 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ec2/get_vpc_endpoint_service.py
--rw-r--r--   0 runner    (1001) docker     (121)    16194 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ec2/get_vpc_iam_pool.py
--rw-r--r--   0 runner    (1001) docker     (121)    15402 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ec2/get_vpc_peering_connection.py
--rw-r--r--   0 runner    (1001) docker     (121)     4640 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ec2/get_vpc_peering_connections.py
--rw-r--r--   0 runner    (1001) docker     (121)     4184 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ec2/get_vpcs.py
--rw-r--r--   0 runner    (1001) docker     (121)     8164 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ec2/get_vpn_gateway.py
--rw-r--r--   0 runner    (1001) docker     (121)   162185 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ec2/instance.py
--rw-r--r--   0 runner    (1001) docker     (121)    13689 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ec2/internet_gateway.py
--rw-r--r--   0 runner    (1001) docker     (121)     9373 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ec2/internet_gateway_attachment.py
--rw-r--r--   0 runner    (1001) docker     (121)    19260 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ec2/key_pair.py
--rw-r--r--   0 runner    (1001) docker     (121)    74869 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ec2/launch_configuration.py
--rw-r--r--   0 runner    (1001) docker     (121)   117094 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ec2/launch_template.py
--rw-r--r--   0 runner    (1001) docker     (121)    14218 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ec2/local_gateway_route.py
--rw-r--r--   0 runner    (1001) docker     (121)    16237 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ec2/local_gateway_route_table_vpc_association.py
--rw-r--r--   0 runner    (1001) docker     (121)    11787 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ec2/main_route_table_association.py
--rw-r--r--   0 runner    (1001) docker     (121)    22037 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ec2/managed_prefix_list.py
--rw-r--r--   0 runner    (1001) docker     (121)    11558 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ec2/managed_prefix_list_entry.py
--rw-r--r--   0 runner    (1001) docker     (121)    20590 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ec2/nat_gateway.py
--rw-r--r--   0 runner    (1001) docker     (121)    20000 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ec2/network_acl.py
--rw-r--r--   0 runner    (1001) docker     (121)     8238 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ec2/network_acl_association.py
--rw-r--r--   0 runner    (1001) docker     (121)    30623 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ec2/network_acl_rule.py
--rw-r--r--   0 runner    (1001) docker     (121)    25229 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ec2/network_insights_path.py
--rw-r--r--   0 runner    (1001) docker     (121)    67113 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ec2/network_interface.py
--rw-r--r--   0 runner    (1001) docker     (121)    12783 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ec2/network_interface_attachment.py
--rw-r--r--   0 runner    (1001) docker     (121)    13825 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ec2/network_interface_security_group_attachment.py
--rw-r--r--   0 runner    (1001) docker     (121)   524457 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ec2/outputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    23207 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ec2/peering_connection_options.py
--rw-r--r--   0 runner    (1001) docker     (121)    18601 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ec2/placement_group.py
--rw-r--r--   0 runner    (1001) docker     (121)    11038 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ec2/proxy_protocol_policy.py
--rw-r--r--   0 runner    (1001) docker     (121)    44522 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ec2/route.py
--rw-r--r--   0 runner    (1001) docker     (121)    21153 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ec2/route_table.py
--rw-r--r--   0 runner    (1001) docker     (121)    13230 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ec2/route_table_association.py
--rw-r--r--   0 runner    (1001) docker     (121)    28775 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ec2/security_group.py
--rw-r--r--   0 runner    (1001) docker     (121)    13480 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ec2/security_group_association.py
--rw-r--r--   0 runner    (1001) docker     (121)    41534 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ec2/security_group_rule.py
--rw-r--r--   0 runner    (1001) docker     (121)     6803 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ec2/serial_console_access.py
--rw-r--r--   0 runner    (1001) docker     (121)     9250 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ec2/snapshot_create_volume_permission.py
--rw-r--r--   0 runner    (1001) docker     (121)     9683 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ec2/spot_datafeed_subscription.py
--rw-r--r--   0 runner    (1001) docker     (121)    85616 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ec2/spot_fleet_request.py
--rw-r--r--   0 runner    (1001) docker     (121)   186619 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ec2/spot_instance_request.py
--rw-r--r--   0 runner    (1001) docker     (121)    58037 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ec2/subnet.py
--rw-r--r--   0 runner    (1001) docker     (121)    14346 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ec2/subnet_cidr_reservation.py
--rw-r--r--   0 runner    (1001) docker     (121)    11979 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ec2/tag.py
--rw-r--r--   0 runner    (1001) docker     (121)    15303 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ec2/traffic_mirror_filter.py
--rw-r--r--   0 runner    (1001) docker     (121)    36168 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ec2/traffic_mirror_filter_rule.py
--rw-r--r--   0 runner    (1001) docker     (121)    32594 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ec2/traffic_mirror_session.py
--rw-r--r--   0 runner    (1001) docker     (121)    19328 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ec2/traffic_mirror_target.py
--rw-r--r--   0 runner    (1001) docker     (121)    17933 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ec2/transit_gateway_peering_attachment_accepter.py
--rw-r--r--   0 runner    (1001) docker     (121)    27015 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ec2/volume_attachment.py
--rw-r--r--   0 runner    (1001) docker     (121)    64450 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ec2/vpc.py
--rw-r--r--   0 runner    (1001) docker     (121)    27900 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ec2/vpc_dhcp_options.py
--rw-r--r--   0 runner    (1001) docker     (121)     9814 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ec2/vpc_dhcp_options_association.py
--rw-r--r--   0 runner    (1001) docker     (121)    49787 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ec2/vpc_endpoint.py
--rw-r--r--   0 runner    (1001) docker     (121)    12473 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ec2/vpc_endpoint_connection_accepter.py
--rw-r--r--   0 runner    (1001) docker     (121)    20311 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ec2/vpc_endpoint_connection_notification.py
--rw-r--r--   0 runner    (1001) docker     (121)     9465 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ec2/vpc_endpoint_policy.py
--rw-r--r--   0 runner    (1001) docker     (121)    10129 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ec2/vpc_endpoint_route_table_association.py
--rw-r--r--   0 runner    (1001) docker     (121)    36282 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ec2/vpc_endpoint_service.py
--rw-r--r--   0 runner    (1001) docker     (121)    10601 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ec2/vpc_endpoint_service_allowed_principle.py
--rw-r--r--   0 runner    (1001) docker     (121)    10739 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ec2/vpc_endpoint_subnet_association.py
--rw-r--r--   0 runner    (1001) docker     (121)    26151 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ec2/vpc_ipam.py
--rw-r--r--   0 runner    (1001) docker     (121)    11193 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ec2/vpc_ipam_organization_admin_account.py
--rw-r--r--   0 runner    (1001) docker     (121)    51149 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ec2/vpc_ipam_pool.py
--rw-r--r--   0 runner    (1001) docker     (121)    14635 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ec2/vpc_ipam_pool_cidr.py
--rw-r--r--   0 runner    (1001) docker     (121)    23522 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ec2/vpc_ipam_pool_cidr_allocation.py
--rw-r--r--   0 runner    (1001) docker     (121)    14034 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ec2/vpc_ipam_preview_next_cidr.py
--rw-r--r--   0 runner    (1001) docker     (121)    15979 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ec2/vpc_ipam_scope.py
--rw-r--r--   0 runner    (1001) docker     (121)    17049 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ec2/vpc_ipv4_cidr_block_association.py
--rw-r--r--   0 runner    (1001) docker     (121)    18439 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ec2/vpc_ipv6_cidr_block_association.py
--rw-r--r--   0 runner    (1001) docker     (121)    36834 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ec2/vpc_peering_connection.py
--rw-r--r--   0 runner    (1001) docker     (121)    31202 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ec2/vpc_peering_connection_accepter.py
--rw-r--r--   0 runner    (1001) docker     (121)   193564 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ec2/vpn_connection.py
--rw-r--r--   0 runner    (1001) docker     (121)    10200 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ec2/vpn_connection_route.py
--rw-r--r--   0 runner    (1001) docker     (121)    16954 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ec2/vpn_gateway.py
--rw-r--r--   0 runner    (1001) docker     (121)     9783 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ec2/vpn_gateway_attachment.py
--rw-r--r--   0 runner    (1001) docker     (121)     9584 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ec2/vpn_gateway_route_propagation.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-21 22:50:28.000000 pulumi_aws-5.9.1/pulumi_aws/ec2clientvpn/
--rw-r--r--   0 runner    (1001) docker     (121)      456 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ec2clientvpn/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    11882 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ec2clientvpn/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    18600 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ec2clientvpn/authorization_rule.py
--rw-r--r--   0 runner    (1001) docker     (121)    59719 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ec2clientvpn/endpoint.py
--rw-r--r--   0 runner    (1001) docker     (121)    15781 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ec2clientvpn/get_endpoint.py
--rw-r--r--   0 runner    (1001) docker     (121)    18214 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ec2clientvpn/network_association.py
--rw-r--r--   0 runner    (1001) docker     (121)    15851 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ec2clientvpn/outputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    18589 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ec2clientvpn/route.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-21 22:50:28.000000 pulumi_aws-5.9.1/pulumi_aws/ec2transitgateway/
--rw-r--r--   0 runner    (1001) docker     (121)     1169 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ec2transitgateway/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    12766 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ec2transitgateway/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    22115 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ec2transitgateway/connect.py
--rw-r--r--   0 runner    (1001) docker     (121)    27657 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ec2transitgateway/connect_peer.py
--rw-r--r--   0 runner    (1001) docker     (121)     7383 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ec2transitgateway/get_connect.py
--rw-r--r--   0 runner    (1001) docker     (121)     9445 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ec2transitgateway/get_connect_peer.py
--rw-r--r--   0 runner    (1001) docker     (121)     6964 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ec2transitgateway/get_direct_connect_gateway_attachment.py
--rw-r--r--   0 runner    (1001) docker     (121)    12563 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ec2transitgateway/get_multicast_domain.py
--rw-r--r--   0 runner    (1001) docker     (121)     7617 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ec2transitgateway/get_peering_attachment.py
--rw-r--r--   0 runner    (1001) docker     (121)     7943 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ec2transitgateway/get_route_table.py
--rw-r--r--   0 runner    (1001) docker     (121)    13346 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ec2transitgateway/get_transit_gateway.py
--rw-r--r--   0 runner    (1001) docker     (121)     8756 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ec2transitgateway/get_vpc_attachment.py
--rw-r--r--   0 runner    (1001) docker     (121)     3474 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ec2transitgateway/get_vpc_attachments.py
--rw-r--r--   0 runner    (1001) docker     (121)     7599 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ec2transitgateway/get_vpn_attachment.py
--rw-r--r--   0 runner    (1001) docker     (121)    29489 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ec2transitgateway/multicast_domain.py
--rw-r--r--   0 runner    (1001) docker     (121)    13789 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ec2transitgateway/multicast_domain_association.py
--rw-r--r--   0 runner    (1001) docker     (121)    12916 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ec2transitgateway/multicast_group_member.py
--rw-r--r--   0 runner    (1001) docker     (121)    12914 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ec2transitgateway/multicast_group_source.py
--rw-r--r--   0 runner    (1001) docker     (121)    14099 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ec2transitgateway/outputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    21127 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ec2transitgateway/peering_attachment.py
--rw-r--r--   0 runner    (1001) docker     (121)    16886 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ec2transitgateway/prefix_list_reference.py
--rw-r--r--   0 runner    (1001) docker     (121)    16400 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ec2transitgateway/route.py
--rw-r--r--   0 runner    (1001) docker     (121)    16011 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ec2transitgateway/route_table.py
--rw-r--r--   0 runner    (1001) docker     (121)    12945 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ec2transitgateway/route_table_association.py
--rw-r--r--   0 runner    (1001) docker     (121)    12945 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ec2transitgateway/route_table_propagation.py
--rw-r--r--   0 runner    (1001) docker     (121)    39889 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ec2transitgateway/transit_gateway.py
--rw-r--r--   0 runner    (1001) docker     (121)    35038 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ec2transitgateway/vpc_attachment.py
--rw-r--r--   0 runner    (1001) docker     (121)    29990 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ec2transitgateway/vpc_attachment_accepter.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-21 22:50:28.000000 pulumi_aws-5.9.1/pulumi_aws/ecr/
--rw-r--r--   0 runner    (1001) docker     (121)      688 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ecr/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    12225 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ecr/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)     6167 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ecr/get_authorization_token.py
--rw-r--r--   0 runner    (1001) docker     (121)     4007 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ecr/get_credentials.py
--rw-r--r--   0 runner    (1001) docker     (121)     7330 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ecr/get_image.py
--rw-r--r--   0 runner    (1001) docker     (121)     7741 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ecr/get_repository.py
--rw-r--r--   0 runner    (1001) docker     (121)    14626 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ecr/lifecycle_policy.py
--rw-r--r--   0 runner    (1001) docker     (121)    15912 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ecr/outputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    11728 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ecr/pull_through_cache_rule.py
--rw-r--r--   0 runner    (1001) docker     (121)     8319 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ecr/registry_policy.py
--rw-r--r--   0 runner    (1001) docker     (121)    14747 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ecr/registry_scanning_configuration.py
--rw-r--r--   0 runner    (1001) docker     (121)    14750 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ecr/replication_configuration.py
--rw-r--r--   0 runner    (1001) docker     (121)    25545 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ecr/repository.py
--rw-r--r--   0 runner    (1001) docker     (121)    11909 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ecr/repository_policy.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-21 22:50:28.000000 pulumi_aws-5.9.1/pulumi_aws/ecrpublic/
--rw-r--r--   0 runner    (1001) docker     (121)      412 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ecrpublic/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     6431 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ecrpublic/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)     4193 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ecrpublic/get_authorization_token.py
--rw-r--r--   0 runner    (1001) docker     (121)     6014 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ecrpublic/outputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    15133 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ecrpublic/repository.py
--rw-r--r--   0 runner    (1001) docker     (121)    11956 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ecrpublic/repository_policy.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-21 22:50:28.000000 pulumi_aws-5.9.1/pulumi_aws/ecs/
--rw-r--r--   0 runner    (1001) docker     (121)      677 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ecs/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    81094 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ecs/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    11564 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ecs/account_setting_default.py
--rw-r--r--   0 runner    (1001) docker     (121)    17651 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ecs/capacity_provider.py
--rw-r--r--   0 runner    (1001) docker     (121)    31717 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ecs/cluster.py
--rw-r--r--   0 runner    (1001) docker     (121)    15308 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ecs/cluster_capacity_providers.py
--rw-r--r--   0 runner    (1001) docker     (121)     6418 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ecs/get_cluster.py
--rw-r--r--   0 runner    (1001) docker     (121)     8437 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ecs/get_container_definition.py
--rw-r--r--   0 runner    (1001) docker     (121)     6402 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ecs/get_service.py
--rw-r--r--   0 runner    (1001) docker     (121)     7717 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ecs/get_task_definition.py
--rw-r--r--   0 runner    (1001) docker     (121)    82647 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ecs/outputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    97431 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ecs/service.py
--rw-r--r--   0 runner    (1001) docker     (121)    10166 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ecs/tag.py
--rw-r--r--   0 runner    (1001) docker     (121)    73875 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ecs/task_definition.py
--rw-r--r--   0 runner    (1001) docker     (121)    52215 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ecs/task_set.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-21 22:50:28.000000 pulumi_aws-5.9.1/pulumi_aws/efs/
--rw-r--r--   0 runner    (1001) docker     (121)      629 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/efs/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    14847 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/efs/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    19177 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/efs/access_point.py
--rw-r--r--   0 runner    (1001) docker     (121)     9667 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/efs/backup_policy.py
--rw-r--r--   0 runner    (1001) docker     (121)    43096 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/efs/file_system.py
--rw-r--r--   0 runner    (1001) docker     (121)    17642 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/efs/file_system_policy.py
--rw-r--r--   0 runner    (1001) docker     (121)     6976 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/efs/get_access_point.py
--rw-r--r--   0 runner    (1001) docker     (121)     3906 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/efs/get_access_points.py
--rw-r--r--   0 runner    (1001) docker     (121)    11576 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/efs/get_file_system.py
--rw-r--r--   0 runner    (1001) docker     (121)    11574 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/efs/get_mount_target.py
--rw-r--r--   0 runner    (1001) docker     (121)    24345 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/efs/mount_target.py
--rw-r--r--   0 runner    (1001) docker     (121)    19891 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/efs/outputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    20087 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/efs/replication_configuration.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-21 22:50:28.000000 pulumi_aws-5.9.1/pulumi_aws/eks/
--rw-r--r--   0 runner    (1001) docker     (121)      661 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/eks/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    34939 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/eks/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    33822 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/eks/addon.py
--rw-r--r--   0 runner    (1001) docker     (121)    55482 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/eks/cluster.py
--rw-r--r--   0 runner    (1001) docker     (121)    28355 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/eks/fargate_profile.py
--rw-r--r--   0 runner    (1001) docker     (121)     7734 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/eks/get_addon.py
--rw-r--r--   0 runner    (1001) docker     (121)     6951 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/eks/get_addon_version.py
--rw-r--r--   0 runner    (1001) docker     (121)    11213 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/eks/get_cluster.py
--rw-r--r--   0 runner    (1001) docker     (121)     3636 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/eks/get_cluster_auth.py
--rw-r--r--   0 runner    (1001) docker     (121)     2025 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/eks/get_clusters.py
--rw-r--r--   0 runner    (1001) docker     (121)    11788 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/eks/get_node_group.py
--rw-r--r--   0 runner    (1001) docker     (121)     3279 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/eks/get_node_groups.py
--rw-r--r--   0 runner    (1001) docker     (121)    17040 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/eks/identity_provider_config.py
--rw-r--r--   0 runner    (1001) docker     (121)    69935 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/eks/node_group.py
--rw-r--r--   0 runner    (1001) docker     (121)    44776 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/eks/outputs.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-21 22:50:28.000000 pulumi_aws-5.9.1/pulumi_aws/elasticache/
--rw-r--r--   0 runner    (1001) docker     (121)      671 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/elasticache/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    12018 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/elasticache/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)   112528 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/elasticache/cluster.py
--rw-r--r--   0 runner    (1001) docker     (121)    15694 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/elasticache/get_cluster.py
--rw-r--r--   0 runner    (1001) docker     (121)    15989 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/elasticache/get_replication_group.py
--rw-r--r--   0 runner    (1001) docker     (121)     6501 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/elasticache/get_user.py
--rw-r--r--   0 runner    (1001) docker     (121)    38782 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/elasticache/global_replication_group.py
--rw-r--r--   0 runner    (1001) docker     (121)    15077 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/elasticache/outputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    20087 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/elasticache/parameter_group.py
--rw-r--r--   0 runner    (1001) docker     (121)   161194 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/elasticache/replication_group.py
--rw-r--r--   0 runner    (1001) docker     (121)    12834 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/elasticache/security_group.py
--rw-r--r--   0 runner    (1001) docker     (121)    17414 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/elasticache/subnet_group.py
--rw-r--r--   0 runner    (1001) docker     (121)    22887 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/elasticache/user.py
--rw-r--r--   0 runner    (1001) docker     (121)    14799 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/elasticache/user_group.py
--rw-r--r--   0 runner    (1001) docker     (121)    10755 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/elasticache/user_group_association.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-21 22:50:28.000000 pulumi_aws-5.9.1/pulumi_aws/elasticbeanstalk/
--rw-r--r--   0 runner    (1001) docker     (121)      537 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/elasticbeanstalk/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     8858 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/elasticbeanstalk/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    17319 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/elasticbeanstalk/application.py
--rw-r--r--   0 runner    (1001) docker     (121)    24340 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/elasticbeanstalk/application_version.py
--rw-r--r--   0 runner    (1001) docker     (121)    20869 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/elasticbeanstalk/configuration_template.py
--rw-r--r--   0 runner    (1001) docker     (121)    58767 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/elasticbeanstalk/environment.py
--rw-r--r--   0 runner    (1001) docker     (121)     4551 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/elasticbeanstalk/get_application.py
--rw-r--r--   0 runner    (1001) docker     (121)     3240 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/elasticbeanstalk/get_hosted_zone.py
--rw-r--r--   0 runner    (1001) docker     (121)     4870 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/elasticbeanstalk/get_solution_stack.py
--rw-r--r--   0 runner    (1001) docker     (121)     9333 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/elasticbeanstalk/outputs.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-21 22:50:28.000000 pulumi_aws-5.9.1/pulumi_aws/elasticloadbalancing/
--rw-r--r--   0 runner    (1001) docker     (121)      725 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/elasticloadbalancing/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    11561 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/elasticloadbalancing/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    15205 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/elasticloadbalancing/app_cookie_stickiness_policy.py
--rw-r--r--   0 runner    (1001) docker     (121)     9299 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/elasticloadbalancing/attachment.py
--rw-r--r--   0 runner    (1001) docker     (121)     4405 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/elasticloadbalancing/get_hosted_zone_id.py
--rw-r--r--   0 runner    (1001) docker     (121)    13304 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/elasticloadbalancing/get_load_balancer.py
--rw-r--r--   0 runner    (1001) docker     (121)     6550 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/elasticloadbalancing/get_service_account.py
--rw-r--r--   0 runner    (1001) docker     (121)    17158 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/elasticloadbalancing/listener_policy.py
--rw-r--r--   0 runner    (1001) docker     (121)    58963 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/elasticloadbalancing/load_balancer.py
--rw-r--r--   0 runner    (1001) docker     (121)    15097 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/elasticloadbalancing/load_balancer_backend_server_policy.py
--rw-r--r--   0 runner    (1001) docker     (121)    15403 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/elasticloadbalancing/load_balancer_cookie_stickiness_policy.py
--rw-r--r--   0 runner    (1001) docker     (121)    19958 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/elasticloadbalancing/load_balancer_policy.py
--rw-r--r--   0 runner    (1001) docker     (121)    14246 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/elasticloadbalancing/outputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    17551 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/elasticloadbalancing/ssl_negotiation_policy.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-21 22:50:28.000000 pulumi_aws-5.9.1/pulumi_aws/elasticloadbalancingv2/
--rw-r--r--   0 runner    (1001) docker     (121)      592 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/elasticloadbalancingv2/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    98570 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/elasticloadbalancingv2/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)     8599 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/elasticloadbalancingv2/get_listener.py
--rw-r--r--   0 runner    (1001) docker     (121)    14306 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/elasticloadbalancingv2/get_load_balancer.py
--rw-r--r--   0 runner    (1001) docker     (121)    12878 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/elasticloadbalancingv2/get_target_group.py
--rw-r--r--   0 runner    (1001) docker     (121)    40835 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/elasticloadbalancingv2/listener.py
--rw-r--r--   0 runner    (1001) docker     (121)    11225 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/elasticloadbalancingv2/listener_certificate.py
--rw-r--r--   0 runner    (1001) docker     (121)    34767 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/elasticloadbalancingv2/listener_rule.py
--rw-r--r--   0 runner    (1001) docker     (121)    69469 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/elasticloadbalancingv2/load_balancer.py
--rw-r--r--   0 runner    (1001) docker     (121)   107979 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/elasticloadbalancingv2/outputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    61894 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/elasticloadbalancingv2/target_group.py
--rw-r--r--   0 runner    (1001) docker     (121)    18326 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/elasticloadbalancingv2/target_group_attachment.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-21 22:50:28.000000 pulumi_aws-5.9.1/pulumi_aws/elasticsearch/
--rw-r--r--   0 runner    (1001) docker     (121)      426 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/elasticsearch/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    49044 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/elasticsearch/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    67348 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/elasticsearch/domain.py
--rw-r--r--   0 runner    (1001) docker     (121)     9618 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/elasticsearch/domain_policy.py
--rw-r--r--   0 runner    (1001) docker     (121)    11167 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/elasticsearch/domain_saml_options.py
--rw-r--r--   0 runner    (1001) docker     (121)    15177 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/elasticsearch/get_domain.py
--rw-r--r--   0 runner    (1001) docker     (121)    70268 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/elasticsearch/outputs.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-21 22:50:28.000000 pulumi_aws-5.9.1/pulumi_aws/elastictranscoder/
--rw-r--r--   0 runner    (1001) docker     (121)      360 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/elastictranscoder/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    46964 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/elastictranscoder/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    44339 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/elastictranscoder/outputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    34802 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/elastictranscoder/pipeline.py
--rw-r--r--   0 runner    (1001) docker     (121)    31433 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/elastictranscoder/preset.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-21 22:50:28.000000 pulumi_aws-5.9.1/pulumi_aws/elb/
--rw-r--r--   0 runner    (1001) docker     (121)      725 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/elb/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    11561 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/elb/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    14858 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/elb/app_cookie_stickiness_policy.py
--rw-r--r--   0 runner    (1001) docker     (121)     9061 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/elb/attachment.py
--rw-r--r--   0 runner    (1001) docker     (121)     3933 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/elb/get_hosted_zone_id.py
--rw-r--r--   0 runner    (1001) docker     (121)    12834 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/elb/get_load_balancer.py
--rw-r--r--   0 runner    (1001) docker     (121)     6064 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/elb/get_service_account.py
--rw-r--r--   0 runner    (1001) docker     (121)    16900 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/elb/listener_policy.py
--rw-r--r--   0 runner    (1001) docker     (121)    58681 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/elb/load_balancer.py
--rw-r--r--   0 runner    (1001) docker     (121)    14754 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/elb/load_balancer_backend_server_policy.py
--rw-r--r--   0 runner    (1001) docker     (121)    15045 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/elb/load_balancer_cookie_stickiness_policy.py
--rw-r--r--   0 runner    (1001) docker     (121)    19680 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/elb/load_balancer_policy.py
--rw-r--r--   0 runner    (1001) docker     (121)    14246 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/elb/outputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    17263 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/elb/ssl_negotiation_policy.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-21 22:50:28.000000 pulumi_aws-5.9.1/pulumi_aws/emr/
--rw-r--r--   0 runner    (1001) docker     (121)      567 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/emr/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)   120467 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/emr/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)   139613 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/emr/cluster.py
--rw-r--r--   0 runner    (1001) docker     (121)     4263 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/emr/get_release_labels.py
--rw-r--r--   0 runner    (1001) docker     (121)    26544 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/emr/instance_fleet.py
--rw-r--r--   0 runner    (1001) docker     (121)    31747 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/emr/instance_group.py
--rw-r--r--   0 runner    (1001) docker     (121)    11997 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/emr/managed_scaling_policy.py
--rw-r--r--   0 runner    (1001) docker     (121)   117475 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/emr/outputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    13294 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/emr/security_configuration.py
--rw-r--r--   0 runner    (1001) docker     (121)    46815 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/emr/studio.py
--rw-r--r--   0 runner    (1001) docker     (121)    17790 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/emr/studio_session_mapping.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-21 22:50:28.000000 pulumi_aws-5.9.1/pulumi_aws/emrcontainers/
--rw-r--r--   0 runner    (1001) docker     (121)      380 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/emrcontainers/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     3959 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/emrcontainers/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)     6692 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/emrcontainers/get_virtual_cluster.py
--rw-r--r--   0 runner    (1001) docker     (121)     6653 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/emrcontainers/outputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    16529 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/emrcontainers/virtual_cluster.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-21 22:50:28.000000 pulumi_aws-5.9.1/pulumi_aws/emrserverless/
--rw-r--r--   0 runner    (1001) docker     (121)      341 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/emrserverless/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    12136 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/emrserverless/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    35959 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/emrserverless/application.py
--rw-r--r--   0 runner    (1001) docker     (121)    12110 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/emrserverless/outputs.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-21 22:50:28.000000 pulumi_aws-5.9.1/pulumi_aws/fms/
--rw-r--r--   0 runner    (1001) docker     (121)      365 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/fms/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     6841 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/fms/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)     8209 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/fms/admin_account.py
--rw-r--r--   0 runner    (1001) docker     (121)     6182 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/fms/outputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    49126 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/fms/policy.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-21 22:50:28.000000 pulumi_aws-5.9.1/pulumi_aws/fsx/
--rw-r--r--   0 runner    (1001) docker     (121)      654 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/fsx/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    62704 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/fsx/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    22592 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/fsx/backup.py
--rw-r--r--   0 runner    (1001) docker     (121)    44515 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/fsx/data_repository_association.py
--rw-r--r--   0 runner    (1001) docker     (121)    91132 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/fsx/lustre_file_system.py
--rw-r--r--   0 runner    (1001) docker     (121)    64803 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/fsx/ontap_file_system.py
--rw-r--r--   0 runner    (1001) docker     (121)    33198 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/fsx/ontap_storage_virtual_machine.py
--rw-r--r--   0 runner    (1001) docker     (121)    38726 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/fsx/ontap_volume.py
--rw-r--r--   0 runner    (1001) docker     (121)    62962 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/fsx/open_zfs_file_system.py
--rw-r--r--   0 runner    (1001) docker     (121)    19792 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/fsx/open_zfs_snapshot.py
--rw-r--r--   0 runner    (1001) docker     (121)    42163 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/fsx/open_zfs_volume.py
--rw-r--r--   0 runner    (1001) docker     (121)    62498 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/fsx/outputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    79805 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/fsx/windows_file_system.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-21 22:50:28.000000 pulumi_aws-5.9.1/pulumi_aws/gamelift/
--rw-r--r--   0 runner    (1001) docker     (121)      466 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/gamelift/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    27119 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/gamelift/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    16014 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/gamelift/alias.py
--rw-r--r--   0 runner    (1001) docker     (121)    19161 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/gamelift/build.py
--rw-r--r--   0 runner    (1001) docker     (121)    48875 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/gamelift/fleet.py
--rw-r--r--   0 runner    (1001) docker     (121)    45981 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/gamelift/game_server_group.py
--rw-r--r--   0 runner    (1001) docker     (121)    21149 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/gamelift/game_session_queue.py
--rw-r--r--   0 runner    (1001) docker     (121)    29239 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/gamelift/outputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    20014 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/gamelift/script.py
--rw-r--r--   0 runner    (1001) docker     (121)    26157 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/get_ami.py
--rw-r--r--   0 runner    (1001) docker     (121)     8675 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/get_ami_ids.py
--rw-r--r--   0 runner    (1001) docker     (121)     5435 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/get_arn.py
--rw-r--r--   0 runner    (1001) docker     (121)     6688 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/get_autoscaling_groups.py
--rw-r--r--   0 runner    (1001) docker     (121)    12721 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/get_availability_zone.py
--rw-r--r--   0 runner    (1001) docker     (121)    11772 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/get_availability_zones.py
--rw-r--r--   0 runner    (1001) docker     (121)     3531 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/get_billing_service_account.py
--rw-r--r--   0 runner    (1001) docker     (121)     3442 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/get_caller_identity.py
--rw-r--r--   0 runner    (1001) docker     (121)     3337 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/get_canonical_user_id.py
--rw-r--r--   0 runner    (1001) docker     (121)     2968 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/get_default_tags.py
--rw-r--r--   0 runner    (1001) docker     (121)    14284 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/get_elastic_ip.py
--rw-r--r--   0 runner    (1001) docker     (121)     9281 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/get_ip_ranges.py
--rw-r--r--   0 runner    (1001) docker     (121)     3768 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/get_partition.py
--rw-r--r--   0 runner    (1001) docker     (121)     7486 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/get_prefix_list.py
--rw-r--r--   0 runner    (1001) docker     (121)     4841 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/get_region.py
--rw-r--r--   0 runner    (1001) docker     (121)     5942 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/get_regions.py
--rw-r--r--   0 runner    (1001) docker     (121)     8510 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/get_service.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-21 22:50:28.000000 pulumi_aws-5.9.1/pulumi_aws/glacier/
--rw-r--r--   0 runner    (1001) docker     (121)      361 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/glacier/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     1698 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/glacier/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)     1885 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/glacier/outputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    21662 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/glacier/vault.py
--rw-r--r--   0 runner    (1001) docker     (121)    22404 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/glacier/vault_lock.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-21 22:50:28.000000 pulumi_aws-5.9.1/pulumi_aws/globalaccelerator/
--rw-r--r--   0 runner    (1001) docker     (121)      426 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/globalaccelerator/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    11661 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/globalaccelerator/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    23086 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/globalaccelerator/accelerator.py
--rw-r--r--   0 runner    (1001) docker     (121)    38023 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/globalaccelerator/endpoint_group.py
--rw-r--r--   0 runner    (1001) docker     (121)     7200 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/globalaccelerator/get_accelerator.py
--rw-r--r--   0 runner    (1001) docker     (121)    18414 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/globalaccelerator/listener.py
--rw-r--r--   0 runner    (1001) docker     (121)    14344 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/globalaccelerator/outputs.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-21 22:50:28.000000 pulumi_aws-5.9.1/pulumi_aws/glue/
--rw-r--r--   0 runner    (1001) docker     (121)      936 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/glue/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)   132646 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/glue/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    25119 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/glue/catalog_database.py
--rw-r--r--   0 runner    (1001) docker     (121)    45572 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/glue/catalog_table.py
--rw-r--r--   0 runner    (1001) docker     (121)    19114 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/glue/classifier.py
--rw-r--r--   0 runner    (1001) docker     (121)    29835 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/glue/connection.py
--rw-r--r--   0 runner    (1001) docker     (121)    63856 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/glue/crawler.py
--rw-r--r--   0 runner    (1001) docker     (121)    12779 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/glue/data_catalog_encryption_settings.py
--rw-r--r--   0 runner    (1001) docker     (121)    55175 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/glue/dev_endpoint.py
--rw-r--r--   0 runner    (1001) docker     (121)     7833 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/glue/get_connection.py
--rw-r--r--   0 runner    (1001) docker     (121)     4459 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/glue/get_data_catalog_encryption_settings.py
--rw-r--r--   0 runner    (1001) docker     (121)    19258 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/glue/get_script.py
--rw-r--r--   0 runner    (1001) docker     (121)    57287 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/glue/job.py
--rw-r--r--   0 runner    (1001) docker     (121)    48070 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/glue/ml_transform.py
--rw-r--r--   0 runner    (1001) docker     (121)   141516 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/glue/outputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    23992 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/glue/partition.py
--rw-r--r--   0 runner    (1001) docker     (121)    20754 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/glue/partition_index.py
--rw-r--r--   0 runner    (1001) docker     (121)    13768 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/glue/registry.py
--rw-r--r--   0 runner    (1001) docker     (121)     9130 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/glue/resource_policy.py
--rw-r--r--   0 runner    (1001) docker     (121)    29168 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/glue/schema.py
--rw-r--r--   0 runner    (1001) docker     (121)    11191 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/glue/security_configuration.py
--rw-r--r--   0 runner    (1001) docker     (121)    41976 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/glue/trigger.py
--rw-r--r--   0 runner    (1001) docker     (121)    22562 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/glue/user_defined_function.py
--rw-r--r--   0 runner    (1001) docker     (121)    21382 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/glue/workflow.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-21 22:50:28.000000 pulumi_aws-5.9.1/pulumi_aws/grafana/
--rw-r--r--   0 runner    (1001) docker     (121)      434 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/grafana/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    13854 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/grafana/get_workspace.py
--rw-r--r--   0 runner    (1001) docker     (121)    13795 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/grafana/license_association.py
--rw-r--r--   0 runner    (1001) docker     (121)    15186 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/grafana/role_association.py
--rw-r--r--   0 runner    (1001) docker     (121)    45618 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/grafana/workspace.py
--rw-r--r--   0 runner    (1001) docker     (121)    35867 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/grafana/workspace_saml_configuration.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-21 22:50:28.000000 pulumi_aws-5.9.1/pulumi_aws/guardduty/
--rw-r--r--   0 runner    (1001) docker     (121)      617 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/guardduty/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    13697 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/guardduty/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    24658 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/guardduty/detector.py
--rw-r--r--   0 runner    (1001) docker     (121)    26049 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/guardduty/filter.py
--rw-r--r--   0 runner    (1001) docker     (121)     4098 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/guardduty/get_detector.py
--rw-r--r--   0 runner    (1001) docker     (121)    10988 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/guardduty/invite_accepter.py
--rw-r--r--   0 runner    (1001) docker     (121)    21715 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/guardduty/ip_set.py
--rw-r--r--   0 runner    (1001) docker     (121)    21666 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/guardduty/member.py
--rw-r--r--   0 runner    (1001) docker     (121)     8663 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/guardduty/organization_admin_account.py
--rw-r--r--   0 runner    (1001) docker     (121)    15005 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/guardduty/organization_configuration.py
--rw-r--r--   0 runner    (1001) docker     (121)    14211 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/guardduty/outputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    21160 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/guardduty/publishing_destination.py
--rw-r--r--   0 runner    (1001) docker     (121)    22757 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/guardduty/threat_intel_set.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-21 22:50:28.000000 pulumi_aws-5.9.1/pulumi_aws/iam/
--rw-r--r--   0 runner    (1001) docker     (121)     1622 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/iam/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    26347 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/iam/_enums.py
--rw-r--r--   0 runner    (1001) docker     (121)    15504 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/iam/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    23580 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/iam/access_key.py
--rw-r--r--   0 runner    (1001) docker     (121)     6629 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/iam/account_alias.py
--rw-r--r--   0 runner    (1001) docker     (121)    29708 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/iam/account_password_policy.py
--rw-r--r--   0 runner    (1001) docker     (121)     2501 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/iam/get_account_alias.py
--rw-r--r--   0 runner    (1001) docker     (121)     4926 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/iam/get_group.py
--rw-r--r--   0 runner    (1001) docker     (121)     6099 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/iam/get_instance_profile.py
--rw-r--r--   0 runner    (1001) docker     (121)     4684 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/iam/get_instance_profiles.py
--rw-r--r--   0 runner    (1001) docker     (121)     6687 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/iam/get_openid_connect_provider.py
--rw-r--r--   0 runner    (1001) docker     (121)     7019 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/iam/get_policy.py
--rw-r--r--   0 runner    (1001) docker     (121)    28240 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/iam/get_policy_document.py
--rw-r--r--   0 runner    (1001) docker     (121)     7788 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/iam/get_role.py
--rw-r--r--   0 runner    (1001) docker     (121)     7451 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/iam/get_roles.py
--rw-r--r--   0 runner    (1001) docker     (121)     6136 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/iam/get_saml_provider.py
--rw-r--r--   0 runner    (1001) docker     (121)     8426 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/iam/get_server_certificate.py
--rw-r--r--   0 runner    (1001) docker     (121)     4766 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/iam/get_session_context.py
--rw-r--r--   0 runner    (1001) docker     (121)     5873 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/iam/get_user.py
--rw-r--r--   0 runner    (1001) docker     (121)     6514 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/iam/get_user_ssh_key.py
--rw-r--r--   0 runner    (1001) docker     (121)     6393 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/iam/get_users.py
--rw-r--r--   0 runner    (1001) docker     (121)    11181 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/iam/group.py
--rw-r--r--   0 runner    (1001) docker     (121)    11223 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/iam/group_membership.py
--rw-r--r--   0 runner    (1001) docker     (121)    13344 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/iam/group_policy.py
--rw-r--r--   0 runner    (1001) docker     (121)     9384 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/iam/group_policy_attachment.py
--rw-r--r--   0 runner    (1001) docker     (121)    25393 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/iam/instance_profile.py
--rw-r--r--   0 runner    (1001) docker     (121)    19404 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/iam/open_id_connect_provider.py
--rw-r--r--   0 runner    (1001) docker     (121)    14814 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/iam/outputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    20816 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/iam/policy.py
--rw-r--r--   0 runner    (1001) docker     (121)    18429 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/iam/policy_attachment.py
--rw-r--r--   0 runner    (1001) docker     (121)    53016 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/iam/role.py
--rw-r--r--   0 runner    (1001) docker     (121)    14422 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/iam/role_policy.py
--rw-r--r--   0 runner    (1001) docker     (121)    11229 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/iam/role_policy_attachment.py
--rw-r--r--   0 runner    (1001) docker     (121)    15898 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/iam/saml_provider.py
--rw-r--r--   0 runner    (1001) docker     (121)    34304 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/iam/server_certificate.py
--rw-r--r--   0 runner    (1001) docker     (121)    23130 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/iam/service_linked_role.py
--rw-r--r--   0 runner    (1001) docker     (121)    18566 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/iam/service_specific_credential.py
--rw-r--r--   0 runner    (1001) docker     (121)    12509 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/iam/signing_certificate.py
--rw-r--r--   0 runner    (1001) docker     (121)    17687 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/iam/ssh_key.py
--rw-r--r--   0 runner    (1001) docker     (121)    22531 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/iam/user.py
--rw-r--r--   0 runner    (1001) docker     (121)     9806 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/iam/user_group_membership.py
--rw-r--r--   0 runner    (1001) docker     (121)    20885 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/iam/user_login_profile.py
--rw-r--r--   0 runner    (1001) docker     (121)    13182 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/iam/user_policy.py
--rw-r--r--   0 runner    (1001) docker     (121)     9301 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/iam/user_policy_attachment.py
--rw-r--r--   0 runner    (1001) docker     (121)    19519 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/iam/virtual_mfa_device.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-21 22:50:28.000000 pulumi_aws-5.9.1/pulumi_aws/identitystore/
--rw-r--r--   0 runner    (1001) docker     (121)      363 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/identitystore/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     2988 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/identitystore/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)     5005 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/identitystore/get_group.py
--rw-r--r--   0 runner    (1001) docker     (121)     4910 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/identitystore/get_user.py
--rw-r--r--   0 runner    (1001) docker     (121)     2524 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/identitystore/outputs.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-21 22:50:28.000000 pulumi_aws-5.9.1/pulumi_aws/imagebuilder/
--rw-r--r--   0 runner    (1001) docker     (121)     1017 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/imagebuilder/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    70066 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/imagebuilder/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    33558 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/imagebuilder/component.py
--rw-r--r--   0 runner    (1001) docker     (121)    46882 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/imagebuilder/container_recipe.py
--rw-r--r--   0 runner    (1001) docker     (121)    21720 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/imagebuilder/distribution_configuration.py
--rw-r--r--   0 runner    (1001) docker     (121)     9336 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/imagebuilder/get_component.py
--rw-r--r--   0 runner    (1001) docker     (121)     5214 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/imagebuilder/get_components.py
--rw-r--r--   0 runner    (1001) docker     (121)    11876 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/imagebuilder/get_container_recipe.py
--rw-r--r--   0 runner    (1001) docker     (121)     5447 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/imagebuilder/get_container_recipes.py
--rw-r--r--   0 runner    (1001) docker     (121)     6739 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/imagebuilder/get_distribution_configuration.py
--rw-r--r--   0 runner    (1001) docker     (121)     4935 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/imagebuilder/get_distribution_configurations.py
--rw-r--r--   0 runner    (1001) docker     (121)    11781 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/imagebuilder/get_image.py
--rw-r--r--   0 runner    (1001) docker     (121)    12492 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/imagebuilder/get_image_pipeline.py
--rw-r--r--   0 runner    (1001) docker     (121)     4539 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/imagebuilder/get_image_pipelines.py
--rw-r--r--   0 runner    (1001) docker     (121)     9401 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/imagebuilder/get_image_recipe.py
--rw-r--r--   0 runner    (1001) docker     (121)     5299 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/imagebuilder/get_image_recipes.py
--rw-r--r--   0 runner    (1001) docker     (121)    12800 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/imagebuilder/get_infrastructure_configuration.py
--rw-r--r--   0 runner    (1001) docker     (121)     5001 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/imagebuilder/get_infrastructure_configurations.py
--rw-r--r--   0 runner    (1001) docker     (121)    33555 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/imagebuilder/image.py
--rw-r--r--   0 runner    (1001) docker     (121)    40865 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/imagebuilder/image_pipeline.py
--rw-r--r--   0 runner    (1001) docker     (121)    37331 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/imagebuilder/image_recipe.py
--rw-r--r--   0 runner    (1001) docker     (121)    43248 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/imagebuilder/infrastructure_configuration.py
--rw-r--r--   0 runner    (1001) docker     (121)   108615 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/imagebuilder/outputs.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-21 22:50:28.000000 pulumi_aws-5.9.1/pulumi_aws/inspector/
--rw-r--r--   0 runner    (1001) docker     (121)      401 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/inspector/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    10839 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/inspector/assessment_target.py
--rw-r--r--   0 runner    (1001) docker     (121)    19346 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/inspector/assessment_template.py
--rw-r--r--   0 runner    (1001) docker     (121)     2928 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/inspector/get_rules_packages.py
--rw-r--r--   0 runner    (1001) docker     (121)     7869 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/inspector/resource_group.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-21 22:50:28.000000 pulumi_aws-5.9.1/pulumi_aws/iot/
--rw-r--r--   0 runner    (1001) docker     (121)      800 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/iot/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)   133920 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/iot/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    23673 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/iot/authorizer.py
--rw-r--r--   0 runner    (1001) docker     (121)    22675 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/iot/certificate.py
--rw-r--r--   0 runner    (1001) docker     (121)     3835 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/iot/get_endpoint.py
--rw-r--r--   0 runner    (1001) docker     (121)    13809 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/iot/indexing_configuration.py
--rw-r--r--   0 runner    (1001) docker     (121)    11430 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/iot/logging_options.py
--rw-r--r--   0 runner    (1001) docker     (121)   133442 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/iot/outputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    11259 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/iot/policy.py
--rw-r--r--   0 runner    (1001) docker     (121)     8680 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/iot/policy_attachment.py
--rw-r--r--   0 runner    (1001) docker     (121)    31001 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/iot/provisioning_template.py
--rw-r--r--   0 runner    (1001) docker     (121)    13236 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/iot/role_alias.py
--rw-r--r--   0 runner    (1001) docker     (121)    13079 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/iot/thing.py
--rw-r--r--   0 runner    (1001) docker     (121)    17226 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/iot/thing_group.py
--rw-r--r--   0 runner    (1001) docker     (121)    13124 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/iot/thing_group_membership.py
--rw-r--r--   0 runner    (1001) docker     (121)     8404 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/iot/thing_principal_attachment.py
--rw-r--r--   0 runner    (1001) docker     (121)    16341 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/iot/thing_type.py
--rw-r--r--   0 runner    (1001) docker     (121)    59278 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/iot/topic_rule.py
--rw-r--r--   0 runner    (1001) docker     (121)    11092 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/iot/topic_rule_destination.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-21 22:50:28.000000 pulumi_aws-5.9.1/pulumi_aws/kendra/
--rw-r--r--   0 runner    (1001) docker     (121)      335 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/kendra/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    30850 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/kendra/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    53613 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/kendra/index.py
--rw-r--r--   0 runner    (1001) docker     (121)    31390 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/kendra/outputs.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-21 22:50:28.000000 pulumi_aws-5.9.1/pulumi_aws/keyspaces/
--rw-r--r--   0 runner    (1001) docker     (121)      359 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/keyspaces/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    13961 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/keyspaces/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    12854 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/keyspaces/keyspace.py
--rw-r--r--   0 runner    (1001) docker     (121)    13335 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/keyspaces/outputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    38228 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/keyspaces/table.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-21 22:50:28.000000 pulumi_aws-5.9.1/pulumi_aws/kinesis/
--rw-r--r--   0 runner    (1001) docker     (121)      577 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/kinesis/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)   238352 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/kinesis/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    46754 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/kinesis/analytics_application.py
--rw-r--r--   0 runner    (1001) docker     (121)    82112 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/kinesis/firehose_delivery_stream.py
--rw-r--r--   0 runner    (1001) docker     (121)     3873 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/kinesis/get_firehose_delivery_stream.py
--rw-r--r--   0 runner    (1001) docker     (121)     8908 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/kinesis/get_stream.py
--rw-r--r--   0 runner    (1001) docker     (121)     5886 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/kinesis/get_stream_consumer.py
--rw-r--r--   0 runner    (1001) docker     (121)   239935 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/kinesis/outputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    38220 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/kinesis/stream.py
--rw-r--r--   0 runner    (1001) docker     (121)    12165 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/kinesis/stream_consumer.py
--rw-r--r--   0 runner    (1001) docker     (121)    29540 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/kinesis/video_stream.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-21 22:50:28.000000 pulumi_aws-5.9.1/pulumi_aws/kinesisanalyticsv2/
--rw-r--r--   0 runner    (1001) docker     (121)      377 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/kinesisanalyticsv2/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)   102491 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/kinesisanalyticsv2/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    60942 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/kinesisanalyticsv2/application.py
--rw-r--r--   0 runner    (1001) docker     (121)    13130 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/kinesisanalyticsv2/application_snapshot.py
--rw-r--r--   0 runner    (1001) docker     (121)   116604 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/kinesisanalyticsv2/outputs.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-21 22:50:28.000000 pulumi_aws-5.9.1/pulumi_aws/kms/
--rw-r--r--   0 runner    (1001) docker     (121)      654 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/kms/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     7222 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/kms/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    14467 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/kms/alias.py
--rw-r--r--   0 runner    (1001) docker     (121)    12731 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/kms/ciphertext.py
--rw-r--r--   0 runner    (1001) docker     (121)    38873 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/kms/external_key.py
--rw-r--r--   0 runner    (1001) docker     (121)     4524 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/kms/get_alias.py
--rw-r--r--   0 runner    (1001) docker     (121)     5983 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/kms/get_cipher_text.py
--rw-r--r--   0 runner    (1001) docker     (121)    11689 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/kms/get_key.py
--rw-r--r--   0 runner    (1001) docker     (121)     9424 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/kms/get_public_key.py
--rw-r--r--   0 runner    (1001) docker     (121)     2588 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/kms/get_secret.py
--rw-r--r--   0 runner    (1001) docker     (121)     3468 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/kms/get_secrets.py
--rw-r--r--   0 runner    (1001) docker     (121)    37712 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/kms/grant.py
--rw-r--r--   0 runner    (1001) docker     (121)    42240 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/kms/key.py
--rw-r--r--   0 runner    (1001) docker     (121)     8663 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/kms/outputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    44708 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/kms/replica_external_key.py
--rw-r--r--   0 runner    (1001) docker     (121)    35590 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/kms/replica_key.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-21 22:50:28.000000 pulumi_aws-5.9.1/pulumi_aws/lakeformation/
--rw-r--r--   0 runner    (1001) docker     (121)      496 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/lakeformation/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    22238 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/lakeformation/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    23816 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/lakeformation/data_lake_settings.py
--rw-r--r--   0 runner    (1001) docker     (121)     6567 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/lakeformation/get_data_lake_settings.py
--rw-r--r--   0 runner    (1001) docker     (121)    13075 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/lakeformation/get_permissions.py
--rw-r--r--   0 runner    (1001) docker     (121)     3962 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/lakeformation/get_resource.py
--rw-r--r--   0 runner    (1001) docker     (121)    21978 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/lakeformation/outputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    32802 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/lakeformation/permissions.py
--rw-r--r--   0 runner    (1001) docker     (121)    10990 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/lakeformation/resource.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-21 22:50:28.000000 pulumi_aws-5.9.1/pulumi_aws/lambda_/
--rw-r--r--   0 runner    (1001) docker     (121)      878 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/lambda_/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)      915 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/lambda_/_enums.py
--rw-r--r--   0 runner    (1001) docker     (121)    31361 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/lambda_/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    19343 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/lambda_/alias.py
--rw-r--r--   0 runner    (1001) docker     (121)    18215 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/lambda_/code_signing_config.py
--rw-r--r--   0 runner    (1001) docker     (121)    93975 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/lambda_/event_source_mapping.py
--rw-r--r--   0 runner    (1001) docker     (121)   110551 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/lambda_/function.py
--rw-r--r--   0 runner    (1001) docker     (121)    25054 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/lambda_/function_event_invoke_config.py
--rw-r--r--   0 runner    (1001) docker     (121)    20697 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/lambda_/function_url.py
--rw-r--r--   0 runner    (1001) docker     (121)     5538 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/lambda_/get_alias.py
--rw-r--r--   0 runner    (1001) docker     (121)     6827 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/lambda_/get_code_signing_config.py
--rw-r--r--   0 runner    (1001) docker     (121)    19263 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/lambda_/get_function.py
--rw-r--r--   0 runner    (1001) docker     (121)     7983 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/lambda_/get_function_url.py
--rw-r--r--   0 runner    (1001) docker     (121)     4974 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/lambda_/get_invocation.py
--rw-r--r--   0 runner    (1001) docker     (121)    13020 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/lambda_/get_layer_version.py
--rw-r--r--   0 runner    (1001) docker     (121)    14538 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/lambda_/invocation.py
--rw-r--r--   0 runner    (1001) docker     (121)    45846 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/lambda_/layer_version.py
--rw-r--r--   0 runner    (1001) docker     (121)    23321 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/lambda_/layer_version_permission.py
--rw-r--r--   0 runner    (1001) docker     (121)    38486 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/lambda_/outputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    45598 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/lambda_/permission.py
--rw-r--r--   0 runner    (1001) docker     (121)    13301 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/lambda_/provisioned_concurrency_config.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-21 22:50:28.000000 pulumi_aws-5.9.1/pulumi_aws/lb/
--rw-r--r--   0 runner    (1001) docker     (121)      626 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/lb/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    98570 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/lb/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)     5357 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/lb/get_hosted_zone_id.py
--rw-r--r--   0 runner    (1001) docker     (121)     8157 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/lb/get_listener.py
--rw-r--r--   0 runner    (1001) docker     (121)    13830 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/lb/get_load_balancer.py
--rw-r--r--   0 runner    (1001) docker     (121)    12410 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/lb/get_target_group.py
--rw-r--r--   0 runner    (1001) docker     (121)    40563 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/lb/listener.py
--rw-r--r--   0 runner    (1001) docker     (121)    10898 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/lb/listener_certificate.py
--rw-r--r--   0 runner    (1001) docker     (121)    34475 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/lb/listener_rule.py
--rw-r--r--   0 runner    (1001) docker     (121)    69177 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/lb/load_balancer.py
--rw-r--r--   0 runner    (1001) docker     (121)   107979 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/lb/outputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    61607 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/lb/target_group.py
--rw-r--r--   0 runner    (1001) docker     (121)    18029 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/lb/target_group_attachment.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-21 22:50:28.000000 pulumi_aws-5.9.1/pulumi_aws/lex/
--rw-r--r--   0 runner    (1001) docker     (121)      512 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/lex/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    64967 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/lex/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    66767 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/lex/bot.py
--rw-r--r--   0 runner    (1001) docker     (121)    20824 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/lex/bot_alias.py
--rw-r--r--   0 runner    (1001) docker     (121)    11746 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/lex/get_bot.py
--rw-r--r--   0 runner    (1001) docker     (121)     6668 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/lex/get_bot_alias.py
--rw-r--r--   0 runner    (1001) docker     (121)     7067 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/lex/get_intent.py
--rw-r--r--   0 runner    (1001) docker     (121)     7743 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/lex/get_slot_type.py
--rw-r--r--   0 runner    (1001) docker     (121)    64048 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/lex/intent.py
--rw-r--r--   0 runner    (1001) docker     (121)    68292 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/lex/outputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    28159 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/lex/slot_type.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-21 22:50:28.000000 pulumi_aws-5.9.1/pulumi_aws/licensemanager/
--rw-r--r--   0 runner    (1001) docker     (121)      333 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/licensemanager/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    11122 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/licensemanager/association.py
--rw-r--r--   0 runner    (1001) docker     (121)    27705 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/licensemanager/license_configuration.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-21 22:50:28.000000 pulumi_aws-5.9.1/pulumi_aws/lightsail/
--rw-r--r--   0 runner    (1001) docker     (121)      567 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/lightsail/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    15974 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/lightsail/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    37776 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/lightsail/container_service.py
--rw-r--r--   0 runner    (1001) docker     (121)    19495 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/lightsail/container_service_deployment_version.py
--rw-r--r--   0 runner    (1001) docker     (121)     8201 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/lightsail/domain.py
--rw-r--r--   0 runner    (1001) docker     (121)    39798 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/lightsail/instance.py
--rw-r--r--   0 runner    (1001) docker     (121)    11869 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/lightsail/instance_public_ports.py
--rw-r--r--   0 runner    (1001) docker     (121)    21158 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/lightsail/key_pair.py
--rw-r--r--   0 runner    (1001) docker     (121)    15826 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/lightsail/outputs.py
--rw-r--r--   0 runner    (1001) docker     (121)     9199 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/lightsail/static_ip.py
--rw-r--r--   0 runner    (1001) docker     (121)    11031 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/lightsail/static_ip_attachment.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-21 22:50:28.000000 pulumi_aws-5.9.1/pulumi_aws/location/
--rw-r--r--   0 runner    (1001) docker     (121)      414 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/location/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     2289 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/location/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)     6147 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/location/get_map.py
--rw-r--r--   0 runner    (1001) docker     (121)     7134 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/location/get_place_index.py
--rw-r--r--   0 runner    (1001) docker     (121)    17010 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/location/map.py
--rw-r--r--   0 runner    (1001) docker     (121)     3466 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/location/outputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    20156 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/location/place_index.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-21 22:50:28.000000 pulumi_aws-5.9.1/pulumi_aws/macie/
--rw-r--r--   0 runner    (1001) docker     (121)      462 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/macie/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     9265 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/macie/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    31789 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/macie/custom_data_identifier.py
--rw-r--r--   0 runner    (1001) docker     (121)    24353 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/macie/findings_filter.py
--rw-r--r--   0 runner    (1001) docker     (121)     8004 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/macie/member_account_association.py
--rw-r--r--   0 runner    (1001) docker     (121)     8483 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/macie/outputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    16480 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/macie/s3_bucket_association.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-21 22:50:28.000000 pulumi_aws-5.9.1/pulumi_aws/macie2/
--rw-r--r--   0 runner    (1001) docker     (121)      470 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/macie2/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    30129 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/macie2/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    15593 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/macie2/account.py
--rw-r--r--   0 runner    (1001) docker     (121)    43824 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/macie2/classification_job.py
--rw-r--r--   0 runner    (1001) docker     (121)     9924 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/macie2/invitation_accepter.py
--rw-r--r--   0 runner    (1001) docker     (121)    32068 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/macie2/member.py
--rw-r--r--   0 runner    (1001) docker     (121)     8078 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/macie2/organization_admin_account.py
--rw-r--r--   0 runner    (1001) docker     (121)    28661 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/macie2/outputs.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-21 22:50:28.000000 pulumi_aws-5.9.1/pulumi_aws/mediaconvert/
--rw-r--r--   0 runner    (1001) docker     (121)      335 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/mediaconvert/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     2429 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/mediaconvert/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)     2600 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/mediaconvert/outputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    20991 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/mediaconvert/queue.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-21 22:50:28.000000 pulumi_aws-5.9.1/pulumi_aws/mediapackage/
--rw-r--r--   0 runner    (1001) docker     (121)      337 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/mediapackage/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     2992 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/mediapackage/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    15502 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/mediapackage/channel.py
--rw-r--r--   0 runner    (1001) docker     (121)     2818 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/mediapackage/outputs.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-21 22:50:28.000000 pulumi_aws-5.9.1/pulumi_aws/mediastore/
--rw-r--r--   0 runner    (1001) docker     (121)      326 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/mediastore/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    12751 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/mediastore/container.py
--rw-r--r--   0 runner    (1001) docker     (121)    10004 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/mediastore/container_policy.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-21 22:50:28.000000 pulumi_aws-5.9.1/pulumi_aws/memorydb/
--rw-r--r--   0 runner    (1001) docker     (121)      628 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/memorydb/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    19777 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/memorydb/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    18176 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/memorydb/acl.py
--rw-r--r--   0 runner    (1001) docker     (121)    70938 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/memorydb/cluster.py
--rw-r--r--   0 runner    (1001) docker     (121)     4853 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/memorydb/get_acl.py
--rw-r--r--   0 runner    (1001) docker     (121)    16123 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/memorydb/get_cluster.py
--rw-r--r--   0 runner    (1001) docker     (121)     5638 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/memorydb/get_parameter_group.py
--rw-r--r--   0 runner    (1001) docker     (121)     6213 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/memorydb/get_snapshot.py
--rw-r--r--   0 runner    (1001) docker     (121)     5401 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/memorydb/get_subnet_group.py
--rw-r--r--   0 runner    (1001) docker     (121)     5752 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/memorydb/get_user.py
--rw-r--r--   0 runner    (1001) docker     (121)    29306 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/memorydb/outputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    22066 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/memorydb/parameter_group.py
--rw-r--r--   0 runner    (1001) docker     (121)    22299 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/memorydb/snapshot.py
--rw-r--r--   0 runner    (1001) docker     (121)    20138 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/memorydb/subnet_group.py
--rw-r--r--   0 runner    (1001) docker     (121)    20256 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/memorydb/user.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-21 22:50:28.000000 pulumi_aws-5.9.1/pulumi_aws/mq/
--rw-r--r--   0 runner    (1001) docker     (121)      434 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/mq/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    19543 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/mq/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    71259 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/mq/broker.py
--rw-r--r--   0 runner    (1001) docker     (121)    26085 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/mq/configuration.py
--rw-r--r--   0 runner    (1001) docker     (121)    13436 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/mq/get_broker.py
--rw-r--r--   0 runner    (1001) docker     (121)     6581 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/mq/get_instance_type_offerings.py
--rw-r--r--   0 runner    (1001) docker     (121)    28981 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/mq/outputs.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-21 22:50:28.000000 pulumi_aws-5.9.1/pulumi_aws/msk/
--rw-r--r--   0 runner    (1001) docker     (121)      531 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/msk/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    36494 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/msk/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    80810 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/msk/cluster.py
--rw-r--r--   0 runner    (1001) docker     (121)    16652 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/msk/configuration.py
--rw-r--r--   0 runner    (1001) docker     (121)     3610 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/msk/get_broker_nodes.py
--rw-r--r--   0 runner    (1001) docker     (121)    16125 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/msk/get_cluster.py
--rw-r--r--   0 runner    (1001) docker     (121)     5427 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/msk/get_configuration.py
--rw-r--r--   0 runner    (1001) docker     (121)     4914 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/msk/get_kafka_version.py
--rw-r--r--   0 runner    (1001) docker     (121)    41111 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/msk/outputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    12352 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/msk/scram_secret_association.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-21 22:50:28.000000 pulumi_aws-5.9.1/pulumi_aws/mskconnect/
--rw-r--r--   0 runner    (1001) docker     (121)      506 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/mskconnect/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    30217 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/mskconnect/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    45904 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/mskconnect/connector.py
--rw-r--r--   0 runner    (1001) docker     (121)    17367 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/mskconnect/custom_plugin.py
--rw-r--r--   0 runner    (1001) docker     (121)     4120 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/mskconnect/get_connector.py
--rw-r--r--   0 runner    (1001) docker     (121)     4769 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/mskconnect/get_custom_plugin.py
--rw-r--r--   0 runner    (1001) docker     (121)     5213 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/mskconnect/get_worker_configuration.py
--rw-r--r--   0 runner    (1001) docker     (121)    33712 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/mskconnect/outputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    14197 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/mskconnect/worker_configuration.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-21 22:50:28.000000 pulumi_aws-5.9.1/pulumi_aws/mwaa/
--rw-r--r--   0 runner    (1001) docker     (121)      341 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/mwaa/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    20959 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/mwaa/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    84052 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/mwaa/environment.py
--rw-r--r--   0 runner    (1001) docker     (121)    22349 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/mwaa/outputs.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-21 22:50:28.000000 pulumi_aws-5.9.1/pulumi_aws/neptune/
--rw-r--r--   0 runner    (1001) docker     (121)      640 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/neptune/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     3956 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/neptune/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    89812 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/neptune/cluster.py
--rw-r--r--   0 runner    (1001) docker     (121)    25030 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/neptune/cluster_endpoint.py
--rw-r--r--   0 runner    (1001) docker     (121)    60070 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/neptune/cluster_instance.py
--rw-r--r--   0 runner    (1001) docker     (121)    21415 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/neptune/cluster_parameter_group.py
--rw-r--r--   0 runner    (1001) docker     (121)    25200 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/neptune/cluster_snapshot.py
--rw-r--r--   0 runner    (1001) docker     (121)    32035 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/neptune/event_subscription.py
--rw-r--r--   0 runner    (1001) docker     (121)    11437 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/neptune/get_engine_version.py
--rw-r--r--   0 runner    (1001) docker     (121)    17803 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/neptune/get_orderable_db_instance.py
--rw-r--r--   0 runner    (1001) docker     (121)     4207 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/neptune/outputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    18641 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/neptune/parameter_group.py
--rw-r--r--   0 runner    (1001) docker     (121)    19189 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/neptune/subnet_group.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-21 22:50:28.000000 pulumi_aws-5.9.1/pulumi_aws/networkfirewall/
--rw-r--r--   0 runner    (1001) docker     (121)      463 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/networkfirewall/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    87520 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/networkfirewall/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    34608 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/networkfirewall/firewall.py
--rw-r--r--   0 runner    (1001) docker     (121)    21821 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/networkfirewall/firewall_policy.py
--rw-r--r--   0 runner    (1001) docker     (121)    15259 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/networkfirewall/logging_configuration.py
--rw-r--r--   0 runner    (1001) docker     (121)    92376 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/networkfirewall/outputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    11889 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/networkfirewall/resource_policy.py
--rw-r--r--   0 runner    (1001) docker     (121)    44249 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/networkfirewall/rule_group.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-21 22:50:28.000000 pulumi_aws-5.9.1/pulumi_aws/networkmanager/
--rw-r--r--   0 runner    (1001) docker     (121)      937 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/networkmanager/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    39513 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/networkmanager/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    20952 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/networkmanager/connection.py
--rw-r--r--   0 runner    (1001) docker     (121)    16565 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/networkmanager/customer_gateway_association.py
--rw-r--r--   0 runner    (1001) docker     (121)    25216 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/networkmanager/device.py
--rw-r--r--   0 runner    (1001) docker     (121)     7753 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/networkmanager/get_connection.py
--rw-r--r--   0 runner    (1001) docker     (121)     5157 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/networkmanager/get_connections.py
--rw-r--r--   0 runner    (1001) docker     (121)    16714 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/networkmanager/get_core_network_policy_document.py
--rw-r--r--   0 runner    (1001) docker     (121)     8559 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/networkmanager/get_device.py
--rw-r--r--   0 runner    (1001) docker     (121)     4975 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/networkmanager/get_devices.py
--rw-r--r--   0 runner    (1001) docker     (121)     4811 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/networkmanager/get_global_network.py
--rw-r--r--   0 runner    (1001) docker     (121)     3498 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/networkmanager/get_global_networks.py
--rw-r--r--   0 runner    (1001) docker     (121)     7156 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/networkmanager/get_link.py
--rw-r--r--   0 runner    (1001) docker     (121)     6241 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/networkmanager/get_links.py
--rw-r--r--   0 runner    (1001) docker     (121)     5795 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/networkmanager/get_site.py
--rw-r--r--   0 runner    (1001) docker     (121)     4227 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/networkmanager/get_sites.py
--rw-r--r--   0 runner    (1001) docker     (121)     9725 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/networkmanager/global_network.py
--rw-r--r--   0 runner    (1001) docker     (121)    19727 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/networkmanager/link.py
--rw-r--r--   0 runner    (1001) docker     (121)    11221 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/networkmanager/link_association.py
--rw-r--r--   0 runner    (1001) docker     (121)    38461 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/networkmanager/outputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    14102 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/networkmanager/site.py
--rw-r--r--   0 runner    (1001) docker     (121)    14635 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/networkmanager/transit_gateway_connect_peer_association.py
--rw-r--r--   0 runner    (1001) docker     (121)    10914 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/networkmanager/transit_gateway_registration.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-21 22:50:28.000000 pulumi_aws-5.9.1/pulumi_aws/opensearch/
--rw-r--r--   0 runner    (1001) docker     (121)      426 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/opensearch/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    48898 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/opensearch/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    70459 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/opensearch/domain.py
--rw-r--r--   0 runner    (1001) docker     (121)     9701 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/opensearch/domain_policy.py
--rw-r--r--   0 runner    (1001) docker     (121)    11125 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/opensearch/domain_saml_options.py
--rw-r--r--   0 runner    (1001) docker     (121)    15019 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/opensearch/get_domain.py
--rw-r--r--   0 runner    (1001) docker     (121)    70072 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/opensearch/outputs.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-21 22:50:28.000000 pulumi_aws-5.9.1/pulumi_aws/opsworks/
--rw-r--r--   0 runner    (1001) docker     (121)      802 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/opsworks/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)   135246 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/opsworks/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    46395 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/opsworks/application.py
--rw-r--r--   0 runner    (1001) docker     (121)    62734 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/opsworks/custom_layer.py
--rw-r--r--   0 runner    (1001) docker     (121)    59671 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/opsworks/ecs_cluster_layer.py
--rw-r--r--   0 runner    (1001) docker     (121)    64406 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/opsworks/ganglia_layer.py
--rw-r--r--   0 runner    (1001) docker     (121)    71586 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/opsworks/haproxy_layer.py
--rw-r--r--   0 runner    (1001) docker     (121)    98619 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/opsworks/instance.py
--rw-r--r--   0 runner    (1001) docker     (121)    69135 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/opsworks/java_app_layer.py
--rw-r--r--   0 runner    (1001) docker     (121)    61448 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/opsworks/memcached_layer.py
--rw-r--r--   0 runner    (1001) docker     (121)    63831 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/opsworks/mysql_layer.py
--rw-r--r--   0 runner    (1001) docker     (121)    61103 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/opsworks/nodejs_app_layer.py
--rw-r--r--   0 runner    (1001) docker     (121)   125980 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/opsworks/outputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    14380 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/opsworks/permission.py
--rw-r--r--   0 runner    (1001) docker     (121)    59282 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/opsworks/php_app_layer.py
--rw-r--r--   0 runner    (1001) docker     (121)    72023 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/opsworks/rails_app_layer.py
--rw-r--r--   0 runner    (1001) docker     (121)    12743 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/opsworks/rds_db_instance.py
--rw-r--r--   0 runner    (1001) docker     (121)    62234 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/opsworks/stack.py
--rw-r--r--   0 runner    (1001) docker     (121)    58838 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/opsworks/static_web_layer.py
--rw-r--r--   0 runner    (1001) docker     (121)    12594 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/opsworks/user_profile.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-21 22:50:28.000000 pulumi_aws-5.9.1/pulumi_aws/organizations/
--rw-r--r--   0 runner    (1001) docker     (121)      681 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/organizations/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    11485 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/organizations/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    37313 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/organizations/account.py
--rw-r--r--   0 runner    (1001) docker     (121)    18877 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/organizations/delegated_administrator.py
--rw-r--r--   0 runner    (1001) docker     (121)     4834 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/organizations/get_delegated_administrators.py
--rw-r--r--   0 runner    (1001) docker     (121)     4057 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/organizations/get_delegated_services.py
--rw-r--r--   0 runner    (1001) docker     (121)     9701 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/organizations/get_organization.py
--rw-r--r--   0 runner    (1001) docker     (121)     4009 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/organizations/get_organizational_units.py
--rw-r--r--   0 runner    (1001) docker     (121)     3947 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/organizations/get_resource_tags.py
--rw-r--r--   0 runner    (1001) docker     (121)    29349 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/organizations/organization.py
--rw-r--r--   0 runner    (1001) docker     (121)    15803 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/organizations/organizational_unit.py
--rw-r--r--   0 runner    (1001) docker     (121)    20181 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/organizations/outputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    23187 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/organizations/policy.py
--rw-r--r--   0 runner    (1001) docker     (121)    11096 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/organizations/policy_attachment.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-21 22:50:28.000000 pulumi_aws-5.9.1/pulumi_aws/outposts/
--rw-r--r--   0 runner    (1001) docker     (121)      456 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/outposts/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     6158 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/outposts/get_outpost.py
--rw-r--r--   0 runner    (1001) docker     (121)     5009 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/outposts/get_outpost_instance_type.py
--rw-r--r--   0 runner    (1001) docker     (121)     3638 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/outposts/get_outpost_instance_types.py
--rw-r--r--   0 runner    (1001) docker     (121)     6043 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/outposts/get_outposts.py
--rw-r--r--   0 runner    (1001) docker     (121)     3703 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/outposts/get_site.py
--rw-r--r--   0 runner    (1001) docker     (121)     2121 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/outposts/get_sites.py
--rw-r--r--   0 runner    (1001) docker     (121)    10664 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/outputs.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-21 22:50:28.000000 pulumi_aws-5.9.1/pulumi_aws/pinpoint/
--rw-r--r--   0 runner    (1001) docker     (121)      638 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/pinpoint/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     7167 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/pinpoint/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    13237 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/pinpoint/adm_channel.py
--rw-r--r--   0 runner    (1001) docker     (121)    27996 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/pinpoint/apns_channel.py
--rw-r--r--   0 runner    (1001) docker     (121)    28312 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/pinpoint/apns_sandbox_channel.py
--rw-r--r--   0 runner    (1001) docker     (121)    28148 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/pinpoint/apns_voip_channel.py
--rw-r--r--   0 runner    (1001) docker     (121)    28408 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/pinpoint/apns_voip_sandbox_channel.py
--rw-r--r--   0 runner    (1001) docker     (121)    23877 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/pinpoint/app.py
--rw-r--r--   0 runner    (1001) docker     (121)    12483 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/pinpoint/baidu_channel.py
--rw-r--r--   0 runner    (1001) docker     (121)    21632 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/pinpoint/email_channel.py
--rw-r--r--   0 runner    (1001) docker     (121)    13861 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/pinpoint/event_stream.py
--rw-r--r--   0 runner    (1001) docker     (121)    10420 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/pinpoint/gcm_channel.py
--rw-r--r--   0 runner    (1001) docker     (121)     6902 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/pinpoint/outputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    15373 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/pinpoint/sms_channel.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-21 22:50:28.000000 pulumi_aws-5.9.1/pulumi_aws/pricing/
--rw-r--r--   0 runner    (1001) docker     (121)      341 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/pricing/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     1358 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/pricing/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)     7773 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/pricing/get_product.py
--rw-r--r--   0 runner    (1001) docker     (121)     1183 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/pricing/outputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    48683 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/provider.py
--rw-r--r--   0 runner    (1001) docker     (121)       40 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/pulumi-plugin.json
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/py.typed
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-21 22:50:28.000000 pulumi_aws-5.9.1/pulumi_aws/qldb/
--rw-r--r--   0 runner    (1001) docker     (121)      384 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/qldb/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     2023 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/qldb/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)     5039 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/qldb/get_ledger.py
--rw-r--r--   0 runner    (1001) docker     (121)    19719 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/qldb/ledger.py
--rw-r--r--   0 runner    (1001) docker     (121)     2338 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/qldb/outputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    29413 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/qldb/stream.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-21 22:50:28.000000 pulumi_aws-5.9.1/pulumi_aws/quicksight/
--rw-r--r--   0 runner    (1001) docker     (121)      414 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/quicksight/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    46897 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/quicksight/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    36821 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/quicksight/data_source.py
--rw-r--r--   0 runner    (1001) docker     (121)    13721 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/quicksight/group.py
--rw-r--r--   0 runner    (1001) docker     (121)    14480 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/quicksight/group_membership.py
--rw-r--r--   0 runner    (1001) docker     (121)    41805 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/quicksight/outputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    26091 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/quicksight/user.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-21 22:50:28.000000 pulumi_aws-5.9.1/pulumi_aws/ram/
--rw-r--r--   0 runner    (1001) docker     (121)      490 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ram/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     1316 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ram/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)     9060 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ram/get_resource_share.py
--rw-r--r--   0 runner    (1001) docker     (121)     1131 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ram/outputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    13558 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ram/principal_association.py
--rw-r--r--   0 runner    (1001) docker     (121)    10782 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ram/resource_association.py
--rw-r--r--   0 runner    (1001) docker     (121)    19655 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ram/resource_share.py
--rw-r--r--   0 runner    (1001) docker     (121)    18473 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ram/resource_share_accepter.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-21 22:50:28.000000 pulumi_aws-5.9.1/pulumi_aws/rds/
--rw-r--r--   0 runner    (1001) docker     (121)     1356 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/rds/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     3396 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/rds/_enums.py
--rw-r--r--   0 runner    (1001) docker     (121)    48509 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/rds/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)   172650 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/rds/cluster.py
--rw-r--r--   0 runner    (1001) docker     (121)    20947 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/rds/cluster_activity_stream.py
--rw-r--r--   0 runner    (1001) docker     (121)    29277 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/rds/cluster_endpoint.py
--rw-r--r--   0 runner    (1001) docker     (121)    91017 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/rds/cluster_instance.py
--rw-r--r--   0 runner    (1001) docker     (121)    24514 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/rds/cluster_parameter_group.py
--rw-r--r--   0 runner    (1001) docker     (121)    14561 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/rds/cluster_role_association.py
--rw-r--r--   0 runner    (1001) docker     (121)    29876 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/rds/cluster_snapshot.py
--rw-r--r--   0 runner    (1001) docker     (121)    31357 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/rds/event_subscription.py
--rw-r--r--   0 runner    (1001) docker     (121)     7275 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/rds/get_certificate.py
--rw-r--r--   0 runner    (1001) docker     (121)    17007 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/rds/get_cluster.py
--rw-r--r--   0 runner    (1001) docker     (121)    18799 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/rds/get_cluster_snapshot.py
--rw-r--r--   0 runner    (1001) docker     (121)    16455 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/rds/get_engine_version.py
--rw-r--r--   0 runner    (1001) docker     (121)     4701 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/rds/get_event_categories.py
--rw-r--r--   0 runner    (1001) docker     (121)    25502 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/rds/get_instance.py
--rw-r--r--   0 runner    (1001) docker     (121)    29409 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/rds/get_orderable_db_instance.py
--rw-r--r--   0 runner    (1001) docker     (121)     8605 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/rds/get_proxy.py
--rw-r--r--   0 runner    (1001) docker     (121)    19406 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/rds/get_snapshot.py
--rw-r--r--   0 runner    (1001) docker     (121)     5186 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/rds/get_subnet_group.py
--rw-r--r--   0 runner    (1001) docker     (121)    30318 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/rds/global_cluster.py
--rw-r--r--   0 runner    (1001) docker     (121)   218146 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/rds/instance.py
--rw-r--r--   0 runner    (1001) docker     (121)    22650 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/rds/instance_automated_backups_replication.py
--rw-r--r--   0 runner    (1001) docker     (121)    28914 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/rds/option_group.py
--rw-r--r--   0 runner    (1001) docker     (121)    49497 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/rds/outputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    22984 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/rds/parameter_group.py
--rw-r--r--   0 runner    (1001) docker     (121)    42252 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/rds/proxy.py
--rw-r--r--   0 runner    (1001) docker     (121)    15246 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/rds/proxy_default_target_group.py
--rw-r--r--   0 runner    (1001) docker     (121)    26869 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/rds/proxy_endpoint.py
--rw-r--r--   0 runner    (1001) docker     (121)    23890 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/rds/proxy_target.py
--rw-r--r--   0 runner    (1001) docker     (121)    14786 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/rds/role_association.py
--rw-r--r--   0 runner    (1001) docker     (121)    16888 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/rds/security_group.py
--rw-r--r--   0 runner    (1001) docker     (121)    34496 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/rds/snapshot.py
--rw-r--r--   0 runner    (1001) docker     (121)    44647 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/rds/snapshot_copy.py
--rw-r--r--   0 runner    (1001) docker     (121)    19057 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/rds/subnet_group.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-21 22:50:29.000000 pulumi_aws-5.9.1/pulumi_aws/redshift/
--rw-r--r--   0 runner    (1001) docker     (121)      975 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/redshift/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    25770 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/redshift/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    11211 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/redshift/authentication_profile.py
--rw-r--r--   0 runner    (1001) docker     (121)   127150 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/redshift/cluster.py
--rw-r--r--   0 runner    (1001) docker     (121)    13433 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/redshift/cluster_iam_roles.py
--rw-r--r--   0 runner    (1001) docker     (121)    21664 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/redshift/endpoint_access.py
--rw-r--r--   0 runner    (1001) docker     (121)    31939 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/redshift/event_subscription.py
--rw-r--r--   0 runner    (1001) docker     (121)    27318 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/redshift/get_cluster.py
--rw-r--r--   0 runner    (1001) docker     (121)    10194 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/redshift/get_cluster_credentials.py
--rw-r--r--   0 runner    (1001) docker     (121)     6970 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/redshift/get_orderable_cluster.py
--rw-r--r--   0 runner    (1001) docker     (121)     5826 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/redshift/get_service_account.py
--rw-r--r--   0 runner    (1001) docker     (121)     5144 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/redshift/get_subnet_group.py
--rw-r--r--   0 runner    (1001) docker     (121)    16412 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/redshift/hsm_client_certificate.py
--rw-r--r--   0 runner    (1001) docker     (121)    27419 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/redshift/hsm_configuration.py
--rw-r--r--   0 runner    (1001) docker     (121)    28410 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/redshift/outputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    19650 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/redshift/parameter_group.py
--rw-r--r--   0 runner    (1001) docker     (121)    27036 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/redshift/scheduled_action.py
--rw-r--r--   0 runner    (1001) docker     (121)    11414 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/redshift/security_group.py
--rw-r--r--   0 runner    (1001) docker     (121)    17036 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/redshift/snapshot_copy_grant.py
--rw-r--r--   0 runner    (1001) docker     (121)    22715 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/redshift/snapshot_schedule.py
--rw-r--r--   0 runner    (1001) docker     (121)    10662 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/redshift/snapshot_schedule_association.py
--rw-r--r--   0 runner    (1001) docker     (121)    18003 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/redshift/subnet_group.py
--rw-r--r--   0 runner    (1001) docker     (121)    28490 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/redshift/usage_limit.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-21 22:50:29.000000 pulumi_aws-5.9.1/pulumi_aws/redshiftdata/
--rw-r--r--   0 runner    (1001) docker     (121)      339 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/redshiftdata/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     1076 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/redshiftdata/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)      808 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/redshiftdata/outputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    20974 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/redshiftdata/statement.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-21 22:50:29.000000 pulumi_aws-5.9.1/pulumi_aws/resourcegroups/
--rw-r--r--   0 runner    (1001) docker     (121)      335 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/resourcegroups/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     1513 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/resourcegroups/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    17631 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/resourcegroups/group.py
--rw-r--r--   0 runner    (1001) docker     (121)     1207 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/resourcegroups/outputs.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-21 22:50:29.000000 pulumi_aws-5.9.1/pulumi_aws/resourcegroupstaggingapi/
--rw-r--r--   0 runner    (1001) docker     (121)      343 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/resourcegroupstaggingapi/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     1465 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/resourcegroupstaggingapi/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    10619 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/resourcegroupstaggingapi/get_resources.py
--rw-r--r--   0 runner    (1001) docker     (121)     4601 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/resourcegroupstaggingapi/outputs.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-21 22:50:29.000000 pulumi_aws-5.9.1/pulumi_aws/route53/
--rw-r--r--   0 runner    (1001) docker     (121)     1337 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/route53/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)      465 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/route53/_enums.py
--rw-r--r--   0 runner    (1001) docker     (121)    42528 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/route53/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    10313 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/route53/delegation_set.py
--rw-r--r--   0 runner    (1001) docker     (121)     4179 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/route53/get_delegation_set.py
--rw-r--r--   0 runner    (1001) docker     (121)     7652 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/route53/get_resolver_endpoint.py
--rw-r--r--   0 runner    (1001) docker     (121)     9603 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/route53/get_resolver_rule.py
--rw-r--r--   0 runner    (1001) docker     (121)     9234 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/route53/get_resolver_rules.py
--rw-r--r--   0 runner    (1001) docker     (121)    11174 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/route53/get_traffic_policy_document.py
--rw-r--r--   0 runner    (1001) docker     (121)    11226 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/route53/get_zone.py
--rw-r--r--   0 runner    (1001) docker     (121)    70665 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/route53/health_check.py
--rw-r--r--   0 runner    (1001) docker     (121)    16132 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/route53/hosted_zone_dns_sec.py
--rw-r--r--   0 runner    (1001) docker     (121)    38591 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/route53/key_signing_key.py
--rw-r--r--   0 runner    (1001) docker     (121)    36317 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/route53/outputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    14120 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/route53/query_log.py
--rw-r--r--   0 runner    (1001) docker     (121)    55413 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/route53/record.py
--rw-r--r--   0 runner    (1001) docker     (121)    11518 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/route53/resolver_dns_sec_config.py
--rw-r--r--   0 runner    (1001) docker     (121)    25348 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/route53/resolver_endpoint.py
--rw-r--r--   0 runner    (1001) docker     (121)    14594 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/route53/resolver_firewall_config.py
--rw-r--r--   0 runner    (1001) docker     (121)    14544 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/route53/resolver_firewall_domain_list.py
--rw-r--r--   0 runner    (1001) docker     (121)    29886 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/route53/resolver_firewall_rule.py
--rw-r--r--   0 runner    (1001) docker     (121)    15880 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/route53/resolver_firewall_rule_group.py
--rw-r--r--   0 runner    (1001) docker     (121)    24469 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/route53/resolver_firewall_rule_group_association.py
--rw-r--r--   0 runner    (1001) docker     (121)    19283 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/route53/resolver_query_log_config.py
--rw-r--r--   0 runner    (1001) docker     (121)    10882 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/route53/resolver_query_log_config_association.py
--rw-r--r--   0 runner    (1001) docker     (121)    28233 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/route53/resolver_rule.py
--rw-r--r--   0 runner    (1001) docker     (121)    11398 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/route53/resolver_rule_association.py
--rw-r--r--   0 runner    (1001) docker     (121)    14733 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/route53/traffic_policy.py
--rw-r--r--   0 runner    (1001) docker     (121)    17523 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/route53/traffic_policy_instance.py
--rw-r--r--   0 runner    (1001) docker     (121)    13427 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/route53/vpc_association_authorization.py
--rw-r--r--   0 runner    (1001) docker     (121)    28097 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/route53/zone.py
--rw-r--r--   0 runner    (1001) docker     (121)    15362 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/route53/zone_association.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-21 22:50:29.000000 pulumi_aws-5.9.1/pulumi_aws/route53domains/
--rw-r--r--   0 runner    (1001) docker     (121)      347 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/route53domains/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    31460 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/route53domains/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    27957 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/route53domains/outputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    49635 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/route53domains/registered_domain.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-21 22:50:29.000000 pulumi_aws-5.9.1/pulumi_aws/route53recoverycontrol/
--rw-r--r--   0 runner    (1001) docker     (121)      424 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/route53recoverycontrol/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     3202 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/route53recoverycontrol/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    10268 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/route53recoverycontrol/cluster.py
--rw-r--r--   0 runner    (1001) docker     (121)    13597 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/route53recoverycontrol/control_panel.py
--rw-r--r--   0 runner    (1001) docker     (121)     2404 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/route53recoverycontrol/outputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    14369 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/route53recoverycontrol/routing_control.py
--rw-r--r--   0 runner    (1001) docker     (121)    27687 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/route53recoverycontrol/safety_rule.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-21 22:50:29.000000 pulumi_aws-5.9.1/pulumi_aws/route53recoveryreadiness/
--rw-r--r--   0 runner    (1001) docker     (121)      423 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/route53recoveryreadiness/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    11094 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/route53recoveryreadiness/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    15647 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/route53recoveryreadiness/cell.py
--rw-r--r--   0 runner    (1001) docker     (121)    11602 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/route53recoveryreadiness/outputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    15122 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/route53recoveryreadiness/readiness_check.py
--rw-r--r--   0 runner    (1001) docker     (121)    14886 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/route53recoveryreadiness/recovery_group.py
--rw-r--r--   0 runner    (1001) docker     (121)    17773 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/route53recoveryreadiness/resource_set.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-21 22:50:29.000000 pulumi_aws-5.9.1/pulumi_aws/s3/
--rw-r--r--   0 runner    (1001) docker     (121)     1550 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/s3/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)      702 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/s3/_enums.py
--rw-r--r--   0 runner    (1001) docker     (121)   269035 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/s3/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    35312 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/s3/access_point.py
--rw-r--r--   0 runner    (1001) docker     (121)    26825 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/s3/account_public_access_block.py
--rw-r--r--   0 runner    (1001) docker     (121)    17506 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/s3/analytics_configuration.py
--rw-r--r--   0 runner    (1001) docker     (121)    97790 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/s3/bucket.py
--rw-r--r--   0 runner    (1001) docker     (121)    12938 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/s3/bucket_accelerate_configuration_v2.py
--rw-r--r--   0 runner    (1001) docker     (121)    19585 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/s3/bucket_acl_v2.py
--rw-r--r--   0 runner    (1001) docker     (121)    15865 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/s3/bucket_cors_configuration_v2.py
--rw-r--r--   0 runner    (1001) docker     (121)    20413 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/s3/bucket_intelligent_tiering_configuration.py
--rw-r--r--   0 runner    (1001) docker     (121)    13850 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/s3/bucket_lifecycle_configuration_v2.py
--rw-r--r--   0 runner    (1001) docker     (121)    19189 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/s3/bucket_logging_v2.py
--rw-r--r--   0 runner    (1001) docker     (121)    13093 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/s3/bucket_metric.py
--rw-r--r--   0 runner    (1001) docker     (121)    31525 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/s3/bucket_notification.py
--rw-r--r--   0 runner    (1001) docker     (121)    85499 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/s3/bucket_object.py
--rw-r--r--   0 runner    (1001) docker     (121)    26511 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/s3/bucket_object_lock_configuration_v2.py
--rw-r--r--   0 runner    (1001) docker     (121)    84292 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/s3/bucket_objectv2.py
--rw-r--r--   0 runner    (1001) docker     (121)    10108 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/s3/bucket_ownership_controls.py
--rw-r--r--   0 runner    (1001) docker     (121)    11082 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/s3/bucket_policy.py
--rw-r--r--   0 runner    (1001) docker     (121)    25638 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/s3/bucket_public_access_block.py
--rw-r--r--   0 runner    (1001) docker     (121)    28203 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/s3/bucket_replication_config.py
--rw-r--r--   0 runner    (1001) docker     (121)    13263 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/s3/bucket_request_payment_configuration_v2.py
--rw-r--r--   0 runner    (1001) docker     (121)    15177 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/s3/bucket_server_side_encryption_configuration_v2.py
--rw-r--r--   0 runner    (1001) docker     (121)   136875 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/s3/bucket_v2.py
--rw-r--r--   0 runner    (1001) docker     (121)    20424 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/s3/bucket_versioning_v2.py
--rw-r--r--   0 runner    (1001) docker     (121)    33509 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/s3/bucket_website_configuration_v2.py
--rw-r--r--   0 runner    (1001) docker     (121)     8814 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/s3/get_bucket.py
--rw-r--r--   0 runner    (1001) docker     (121)    22177 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/s3/get_bucket_object.py
--rw-r--r--   0 runner    (1001) docker     (121)    10307 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/s3/get_bucket_objects.py
--rw-r--r--   0 runner    (1001) docker     (121)     3549 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/s3/get_bucket_policy.py
--rw-r--r--   0 runner    (1001) docker     (121)     3067 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/s3/get_canonical_user_id.py
--rw-r--r--   0 runner    (1001) docker     (121)    21514 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/s3/get_object.py
--rw-r--r--   0 runner    (1001) docker     (121)     9186 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/s3/get_objects.py
--rw-r--r--   0 runner    (1001) docker     (121)    27604 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/s3/inventory.py
--rw-r--r--   0 runner    (1001) docker     (121)   131651 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/s3/object_copy.py
--rw-r--r--   0 runner    (1001) docker     (121)   257905 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/s3/outputs.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-21 22:50:29.000000 pulumi_aws-5.9.1/pulumi_aws/s3control/
--rw-r--r--   0 runner    (1001) docker     (121)      626 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/s3control/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    28775 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/s3control/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    12547 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/s3control/access_point_policy.py
--rw-r--r--   0 runner    (1001) docker     (121)    16903 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/s3control/bucket.py
--rw-r--r--   0 runner    (1001) docker     (121)    12577 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/s3control/bucket_lifecycle_configuration.py
--rw-r--r--   0 runner    (1001) docker     (121)     9842 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/s3control/bucket_policy.py
--rw-r--r--   0 runner    (1001) docker     (121)    18254 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/s3control/multi_region_access_point.py
--rw-r--r--   0 runner    (1001) docker     (121)    14874 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/s3control/multi_region_access_point_policy.py
--rw-r--r--   0 runner    (1001) docker     (121)    14371 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/s3control/object_lambda_access_point.py
--rw-r--r--   0 runner    (1001) docker     (121)    14632 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/s3control/object_lambda_access_point_policy.py
--rw-r--r--   0 runner    (1001) docker     (121)    29537 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/s3control/outputs.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-21 22:50:29.000000 pulumi_aws-5.9.1/pulumi_aws/s3outposts/
--rw-r--r--   0 runner    (1001) docker     (121)      338 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/s3outposts/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     1230 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/s3outposts/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    16354 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/s3outposts/endpoint.py
--rw-r--r--   0 runner    (1001) docker     (121)     1634 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/s3outposts/outputs.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-21 22:50:29.000000 pulumi_aws-5.9.1/pulumi_aws/sagemaker/
--rw-r--r--   0 runner    (1001) docker     (121)     1034 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/sagemaker/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)   168382 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/sagemaker/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    21069 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/sagemaker/app.py
--rw-r--r--   0 runner    (1001) docker     (121)    18358 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/sagemaker/app_image_config.py
--rw-r--r--   0 runner    (1001) docker     (121)    17592 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/sagemaker/code_repository.py
--rw-r--r--   0 runner    (1001) docker     (121)    11155 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/sagemaker/device.py
--rw-r--r--   0 runner    (1001) docker     (121)    23710 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/sagemaker/device_fleet.py
--rw-r--r--   0 runner    (1001) docker     (121)    39201 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/sagemaker/domain.py
--rw-r--r--   0 runner    (1001) docker     (121)    17552 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/sagemaker/endpoint.py
--rw-r--r--   0 runner    (1001) docker     (121)    25038 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/sagemaker/endpoint_configuration.py
--rw-r--r--   0 runner    (1001) docker     (121)    33860 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/sagemaker/feature_group.py
--rw-r--r--   0 runner    (1001) docker     (121)    36456 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/sagemaker/flow_definition.py
--rw-r--r--   0 runner    (1001) docker     (121)     9442 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/sagemaker/get_prebuilt_ecr_image.py
--rw-r--r--   0 runner    (1001) docker     (121)    15483 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/sagemaker/human_task_ui.py
--rw-r--r--   0 runner    (1001) docker     (121)    18665 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/sagemaker/image.py
--rw-r--r--   0 runner    (1001) docker     (121)    13264 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/sagemaker/image_version.py
--rw-r--r--   0 runner    (1001) docker     (121)    32299 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/sagemaker/model.py
--rw-r--r--   0 runner    (1001) docker     (121)    15343 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/sagemaker/model_package_group.py
--rw-r--r--   0 runner    (1001) docker     (121)     8494 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/sagemaker/model_package_group_policy.py
--rw-r--r--   0 runner    (1001) docker     (121)    53133 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/sagemaker/notebook_instance.py
--rw-r--r--   0 runner    (1001) docker     (121)    12857 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/sagemaker/notebook_instance_lifecycle_configuration.py
--rw-r--r--   0 runner    (1001) docker     (121)   178499 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/sagemaker/outputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    21418 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/sagemaker/project.py
--rw-r--r--   0 runner    (1001) docker     (121)    19258 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/sagemaker/studio_lifecycle_config.py
--rw-r--r--   0 runner    (1001) docker     (121)    26397 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/sagemaker/user_profile.py
--rw-r--r--   0 runner    (1001) docker     (121)    22053 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/sagemaker/workforce.py
--rw-r--r--   0 runner    (1001) docker     (121)    29220 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/sagemaker/workteam.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-21 22:50:29.000000 pulumi_aws-5.9.1/pulumi_aws/schemas/
--rw-r--r--   0 runner    (1001) docker     (121)      341 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/schemas/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    14644 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/schemas/discoverer.py
--rw-r--r--   0 runner    (1001) docker     (121)    14737 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/schemas/registry.py
--rw-r--r--   0 runner    (1001) docker     (121)    25370 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/schemas/schema.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-21 22:50:29.000000 pulumi_aws-5.9.1/pulumi_aws/secretsmanager/
--rw-r--r--   0 runner    (1001) docker     (121)      548 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/secretsmanager/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     7257 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/secretsmanager/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)     8560 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/secretsmanager/get_secret.py
--rw-r--r--   0 runner    (1001) docker     (121)     5714 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/secretsmanager/get_secret_rotation.py
--rw-r--r--   0 runner    (1001) docker     (121)     8374 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/secretsmanager/get_secret_version.py
--rw-r--r--   0 runner    (1001) docker     (121)     4313 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/secretsmanager/get_secrets.py
--rw-r--r--   0 runner    (1001) docker     (121)     8608 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/secretsmanager/outputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    50501 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/secretsmanager/secret.py
--rw-r--r--   0 runner    (1001) docker     (121)    14001 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/secretsmanager/secret_policy.py
--rw-r--r--   0 runner    (1001) docker     (121)    19659 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/secretsmanager/secret_rotation.py
--rw-r--r--   0 runner    (1001) docker     (121)    23497 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/secretsmanager/secret_version.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-21 22:50:29.000000 pulumi_aws-5.9.1/pulumi_aws/securityhub/
--rw-r--r--   0 runner    (1001) docker     (121)      667 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/securityhub/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)   246761 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/securityhub/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)     4484 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/securityhub/account.py
--rw-r--r--   0 runner    (1001) docker     (121)    11710 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/securityhub/action_target.py
--rw-r--r--   0 runner    (1001) docker     (121)    15675 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/securityhub/finding_aggregator.py
--rw-r--r--   0 runner    (1001) docker     (121)    20675 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/securityhub/insight.py
--rw-r--r--   0 runner    (1001) docker     (121)     9315 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/securityhub/invite_accepter.py
--rw-r--r--   0 runner    (1001) docker     (121)    12819 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/securityhub/member.py
--rw-r--r--   0 runner    (1001) docker     (121)     9301 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/securityhub/organization_admin_account.py
--rw-r--r--   0 runner    (1001) docker     (121)     9382 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/securityhub/organization_configuration.py
--rw-r--r--   0 runner    (1001) docker     (121)   200993 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/securityhub/outputs.py
--rw-r--r--   0 runner    (1001) docker     (121)     9436 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/securityhub/product_subscription.py
--rw-r--r--   0 runner    (1001) docker     (121)    22477 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/securityhub/standards_control.py
--rw-r--r--   0 runner    (1001) docker     (121)     8148 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/securityhub/standards_subscription.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-21 22:50:29.000000 pulumi_aws-5.9.1/pulumi_aws/serverlessrepository/
--rw-r--r--   0 runner    (1001) docker     (121)      337 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/serverlessrepository/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    24180 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/serverlessrepository/cloud_formation_stack.py
--rw-r--r--   0 runner    (1001) docker     (121)     7312 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/serverlessrepository/get_application.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-21 22:50:29.000000 pulumi_aws-5.9.1/pulumi_aws/servicecatalog/
--rw-r--r--   0 runner    (1001) docker     (121)      924 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/servicecatalog/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    22372 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/servicecatalog/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)     9093 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/servicecatalog/budget_resource_association.py
--rw-r--r--   0 runner    (1001) docker     (121)    19923 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/servicecatalog/constraint.py
--rw-r--r--   0 runner    (1001) docker     (121)     6919 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/servicecatalog/get_constraint.py
--rw-r--r--   0 runner    (1001) docker     (121)     4858 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/servicecatalog/get_launch_paths.py
--rw-r--r--   0 runner    (1001) docker     (121)     6304 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/servicecatalog/get_portfolio.py
--rw-r--r--   0 runner    (1001) docker     (121)     5873 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/servicecatalog/get_portfolio_constraints.py
--rw-r--r--   0 runner    (1001) docker     (121)     9831 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/servicecatalog/get_product.py
--rw-r--r--   0 runner    (1001) docker     (121)     7285 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/servicecatalog/organizations_access.py
--rw-r--r--   0 runner    (1001) docker     (121)    26100 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/servicecatalog/outputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    16155 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/servicecatalog/portfolio.py
--rw-r--r--   0 runner    (1001) docker     (121)    23923 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/servicecatalog/portfolio_share.py
--rw-r--r--   0 runner    (1001) docker     (121)    14569 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/servicecatalog/principal_portfolio_association.py
--rw-r--r--   0 runner    (1001) docker     (121)    38089 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/servicecatalog/product.py
--rw-r--r--   0 runner    (1001) docker     (121)    13749 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/servicecatalog/product_portfolio_association.py
--rw-r--r--   0 runner    (1001) docker     (121)    65881 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/servicecatalog/provisioned_product.py
--rw-r--r--   0 runner    (1001) docker     (121)    34405 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/servicecatalog/provisioning_artifact.py
--rw-r--r--   0 runner    (1001) docker     (121)    13526 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/servicecatalog/service_action.py
--rw-r--r--   0 runner    (1001) docker     (121)    10181 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/servicecatalog/tag_option.py
--rw-r--r--   0 runner    (1001) docker     (121)    13903 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/servicecatalog/tag_option_resource_association.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-21 22:50:29.000000 pulumi_aws-5.9.1/pulumi_aws/servicediscovery/
--rw-r--r--   0 runner    (1001) docker     (121)      497 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/servicediscovery/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     8001 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/servicediscovery/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)     5107 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/servicediscovery/get_dns_namespace.py
--rw-r--r--   0 runner    (1001) docker     (121)    13838 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/servicediscovery/http_namespace.py
--rw-r--r--   0 runner    (1001) docker     (121)    15544 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/servicediscovery/instance.py
--rw-r--r--   0 runner    (1001) docker     (121)     8408 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/servicediscovery/outputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    17538 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/servicediscovery/private_dns_namespace.py
--rw-r--r--   0 runner    (1001) docker     (121)    15348 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/servicediscovery/public_dns_namespace.py
--rw-r--r--   0 runner    (1001) docker     (121)    30763 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/servicediscovery/service.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-21 22:50:29.000000 pulumi_aws-5.9.1/pulumi_aws/servicequotas/
--rw-r--r--   0 runner    (1001) docker     (121)      358 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/servicequotas/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     4464 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/servicequotas/get_service.py
--rw-r--r--   0 runner    (1001) docker     (121)     9882 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/servicequotas/get_service_quota.py
--rw-r--r--   0 runner    (1001) docker     (121)    22422 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/servicequotas/service_quota.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-21 22:50:29.000000 pulumi_aws-5.9.1/pulumi_aws/ses/
--rw-r--r--   0 runner    (1001) docker     (121)      908 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ses/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    22779 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ses/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)     7180 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ses/active_receipt_rule_set.py
--rw-r--r--   0 runner    (1001) docker     (121)    18187 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ses/confguration_set.py
--rw-r--r--   0 runner    (1001) docker     (121)    18010 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ses/configuration_set.py
--rw-r--r--   0 runner    (1001) docker     (121)    10825 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ses/domain_dkim.py
--rw-r--r--   0 runner    (1001) docker     (121)    11064 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ses/domain_identity.py
--rw-r--r--   0 runner    (1001) docker     (121)     9163 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ses/domain_identity_verification.py
--rw-r--r--   0 runner    (1001) docker     (121)     7146 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ses/email_identity.py
--rw-r--r--   0 runner    (1001) docker     (121)    26658 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ses/event_destination.py
--rw-r--r--   0 runner    (1001) docker     (121)     2833 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ses/get_active_receipt_rule_set.py
--rw-r--r--   0 runner    (1001) docker     (121)     4024 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ses/get_domain_identity.py
--rw-r--r--   0 runner    (1001) docker     (121)     3304 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ses/get_email_identity.py
--rw-r--r--   0 runner    (1001) docker     (121)    16183 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ses/identity_notification_topic.py
--rw-r--r--   0 runner    (1001) docker     (121)    11507 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ses/identity_policy.py
--rw-r--r--   0 runner    (1001) docker     (121)    16907 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ses/mail_from.py
--rw-r--r--   0 runner    (1001) docker     (121)    24946 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ses/outputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    10445 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ses/receipt_filter.py
--rw-r--r--   0 runner    (1001) docker     (121)    39512 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ses/receipt_rule.py
--rw-r--r--   0 runner    (1001) docker     (121)     7387 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ses/receipt_rule_set.py
--rw-r--r--   0 runner    (1001) docker     (121)    14207 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ses/template.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-21 22:50:29.000000 pulumi_aws-5.9.1/pulumi_aws/sfn/
--rw-r--r--   0 runner    (1001) docker     (121)      428 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/sfn/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     4052 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/sfn/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    11641 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/sfn/activity.py
--rw-r--r--   0 runner    (1001) docker     (121)     3936 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/sfn/get_activity.py
--rw-r--r--   0 runner    (1001) docker     (121)     5485 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/sfn/get_state_machine.py
--rw-r--r--   0 runner    (1001) docker     (121)     4040 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/sfn/outputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    35305 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/sfn/state_machine.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-21 22:50:29.000000 pulumi_aws-5.9.1/pulumi_aws/shield/
--rw-r--r--   0 runner    (1001) docker     (121)      378 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/shield/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    15276 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/shield/protection.py
--rw-r--r--   0 runner    (1001) docker     (121)    26892 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/shield/protection_group.py
--rw-r--r--   0 runner    (1001) docker     (121)    13369 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/shield/protection_health_check_association.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-21 22:50:29.000000 pulumi_aws-5.9.1/pulumi_aws/signer/
--rw-r--r--   0 runner    (1001) docker     (121)      480 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/signer/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    10765 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/signer/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    11419 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/signer/get_signing_job.py
--rw-r--r--   0 runner    (1001) docker     (121)     8285 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/signer/get_signing_profile.py
--rw-r--r--   0 runner    (1001) docker     (121)    13451 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/signer/outputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    34380 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/signer/signing_job.py
--rw-r--r--   0 runner    (1001) docker     (121)    27628 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/signer/signing_profile.py
--rw-r--r--   0 runner    (1001) docker     (121)    21369 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/signer/signing_profile_permission.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-21 22:50:29.000000 pulumi_aws-5.9.1/pulumi_aws/simpledb/
--rw-r--r--   0 runner    (1001) docker     (121)      291 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/simpledb/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     5920 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/simpledb/domain.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-21 22:50:29.000000 pulumi_aws-5.9.1/pulumi_aws/sns/
--rw-r--r--   0 runner    (1001) docker     (121)      444 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/sns/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     3490 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/sns/get_topic.py
--rw-r--r--   0 runner    (1001) docker     (121)    41542 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/sns/platform_application.py
--rw-r--r--   0 runner    (1001) docker     (121)    20873 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/sns/sms_preferences.py
--rw-r--r--   0 runner    (1001) docker     (121)    76362 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/sns/topic.py
--rw-r--r--   0 runner    (1001) docker     (121)    11817 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/sns/topic_policy.py
--rw-r--r--   0 runner    (1001) docker     (121)    56986 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/sns/topic_subscription.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-21 22:50:29.000000 pulumi_aws-5.9.1/pulumi_aws/sqs/
--rw-r--r--   0 runner    (1001) docker     (121)      343 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/sqs/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     4452 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/sqs/get_queue.py
--rw-r--r--   0 runner    (1001) docker     (121)    70050 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/sqs/queue.py
--rw-r--r--   0 runner    (1001) docker     (121)     9641 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/sqs/queue_policy.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-21 22:50:29.000000 pulumi_aws-5.9.1/pulumi_aws/ssm/
--rw-r--r--   0 runner    (1001) docker     (121)      840 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ssm/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)      365 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ssm/_enums.py
--rw-r--r--   0 runner    (1001) docker     (121)    52894 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ssm/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    26093 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ssm/activation.py
--rw-r--r--   0 runner    (1001) docker     (121)    51231 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ssm/association.py
--rw-r--r--   0 runner    (1001) docker     (121)    51296 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ssm/document.py
--rw-r--r--   0 runner    (1001) docker     (121)     6833 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ssm/get_document.py
--rw-r--r--   0 runner    (1001) docker     (121)     3818 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ssm/get_instances.py
--rw-r--r--   0 runner    (1001) docker     (121)     4075 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ssm/get_maintenance_windows.py
--rw-r--r--   0 runner    (1001) docker     (121)     5382 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ssm/get_parameter.py
--rw-r--r--   0 runner    (1001) docker     (121)     5793 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ssm/get_parameters_by_path.py
--rw-r--r--   0 runner    (1001) docker     (121)    12661 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ssm/get_patch_baseline.py
--rw-r--r--   0 runner    (1001) docker     (121)    35771 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ssm/maintenance_window.py
--rw-r--r--   0 runner    (1001) docker     (121)    23617 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ssm/maintenance_window_target.py
--rw-r--r--   0 runner    (1001) docker     (121)    45098 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ssm/maintenance_window_task.py
--rw-r--r--   0 runner    (1001) docker     (121)    54527 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ssm/outputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    38705 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ssm/parameter.py
--rw-r--r--   0 runner    (1001) docker     (121)    54960 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ssm/patch_baseline.py
--rw-r--r--   0 runner    (1001) docker     (121)     8784 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ssm/patch_group.py
--rw-r--r--   0 runner    (1001) docker     (121)    11585 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ssm/resource_data_sync.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-21 22:50:29.000000 pulumi_aws-5.9.1/pulumi_aws/ssoadmin/
--rw-r--r--   0 runner    (1001) docker     (121)      481 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ssoadmin/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    19159 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ssoadmin/account_assignment.py
--rw-r--r--   0 runner    (1001) docker     (121)     2764 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ssoadmin/get_instances.py
--rw-r--r--   0 runner    (1001) docker     (121)     6944 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ssoadmin/get_permission_set.py
--rw-r--r--   0 runner    (1001) docker     (121)    14017 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ssoadmin/managed_policy_attachment.py
--rw-r--r--   0 runner    (1001) docker     (121)    22725 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ssoadmin/permission_set.py
--rw-r--r--   0 runner    (1001) docker     (121)    12519 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/ssoadmin/permission_set_inline_policy.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-21 22:50:29.000000 pulumi_aws-5.9.1/pulumi_aws/storagegateway/
--rw-r--r--   0 runner    (1001) docker     (121)      642 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/storagegateway/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    18226 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/storagegateway/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)     9381 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/storagegateway/cache.py
--rw-r--r--   0 runner    (1001) docker     (121)    43947 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/storagegateway/caches_iscsi_volume.py
--rw-r--r--   0 runner    (1001) docker     (121)    31089 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/storagegateway/file_system_association.py
--rw-r--r--   0 runner    (1001) docker     (121)    78466 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/storagegateway/gateway.py
--rw-r--r--   0 runner    (1001) docker     (121)     5438 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/storagegateway/get_local_disk.py
--rw-r--r--   0 runner    (1001) docker     (121)    65740 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/storagegateway/nfs_file_share.py
--rw-r--r--   0 runner    (1001) docker     (121)    19732 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/storagegateway/outputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    82977 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/storagegateway/smb_file_share.py
--rw-r--r--   0 runner    (1001) docker     (121)    45060 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/storagegateway/stored_iscsi_volume.py
--rw-r--r--   0 runner    (1001) docker     (121)    24082 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/storagegateway/tape_pool.py
--rw-r--r--   0 runner    (1001) docker     (121)    12892 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/storagegateway/upload_buffer.py
--rw-r--r--   0 runner    (1001) docker     (121)     9675 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/storagegateway/working_storage.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-21 22:50:29.000000 pulumi_aws-5.9.1/pulumi_aws/swf/
--rw-r--r--   0 runner    (1001) docker     (121)      291 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/swf/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    19773 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/swf/domain.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-21 22:50:29.000000 pulumi_aws-5.9.1/pulumi_aws/synthetics/
--rw-r--r--   0 runner    (1001) docker     (121)      336 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/synthetics/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    14317 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/synthetics/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    60794 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/synthetics/canary.py
--rw-r--r--   0 runner    (1001) docker     (121)    15261 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/synthetics/outputs.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-21 22:50:29.000000 pulumi_aws-5.9.1/pulumi_aws/timestreamwrite/
--rw-r--r--   0 runner    (1001) docker     (121)      359 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/timestreamwrite/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     9470 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/timestreamwrite/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    18385 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/timestreamwrite/database.py
--rw-r--r--   0 runner    (1001) docker     (121)    10690 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/timestreamwrite/outputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    23532 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/timestreamwrite/table.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-21 22:50:29.000000 pulumi_aws-5.9.1/pulumi_aws/transfer/
--rw-r--r--   0 runner    (1001) docker     (121)      451 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/transfer/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    60059 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/transfer/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    29665 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/transfer/access.py
--rw-r--r--   0 runner    (1001) docker     (121)     9138 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/transfer/get_server.py
--rw-r--r--   0 runner    (1001) docker     (121)    60272 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/transfer/outputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    72742 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/transfer/server.py
--rw-r--r--   0 runner    (1001) docker     (121)    13060 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/transfer/ssh_key.py
--rw-r--r--   0 runner    (1001) docker     (121)    37669 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/transfer/user.py
--rw-r--r--   0 runner    (1001) docker     (121)    17068 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/transfer/workflow.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-21 22:50:29.000000 pulumi_aws-5.9.1/pulumi_aws/waf/
--rw-r--r--   0 runner    (1001) docker     (121)      773 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/waf/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    53462 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/waf/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    11211 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/waf/byte_match_set.py
--rw-r--r--   0 runner    (1001) docker     (121)    11232 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/waf/geo_match_set.py
--rw-r--r--   0 runner    (1001) docker     (121)     2687 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/waf/get_ipset.py
--rw-r--r--   0 runner    (1001) docker     (121)     2949 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/waf/get_rate_based_rule.py
--rw-r--r--   0 runner    (1001) docker     (121)     2653 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/waf/get_rule.py
--rw-r--r--   0 runner    (1001) docker     (121)     2726 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/waf/get_web_acl.py
--rw-r--r--   0 runner    (1001) docker     (121)    11061 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/waf/ip_set.py
--rw-r--r--   0 runner    (1001) docker     (121)    51941 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/waf/outputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    21914 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/waf/rate_based_rule.py
--rw-r--r--   0 runner    (1001) docker     (121)    12201 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/waf/regex_match_set.py
--rw-r--r--   0 runner    (1001) docker     (121)    10442 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/waf/regex_pattern_set.py
--rw-r--r--   0 runner    (1001) docker     (121)    17601 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/waf/rule.py
--rw-r--r--   0 runner    (1001) docker     (121)    17091 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/waf/rule_group.py
--rw-r--r--   0 runner    (1001) docker     (121)    11239 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/waf/size_constraint_set.py
--rw-r--r--   0 runner    (1001) docker     (121)    11514 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/waf/sql_injection_match_set.py
--rw-r--r--   0 runner    (1001) docker     (121)    27078 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/waf/web_acl.py
--rw-r--r--   0 runner    (1001) docker     (121)    11423 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/waf/xss_match_set.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-21 22:50:29.000000 pulumi_aws-5.9.1/pulumi_aws/wafregional/
--rw-r--r--   0 runner    (1001) docker     (121)      807 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/wafregional/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    45579 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/wafregional/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    11217 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/wafregional/byte_match_set.py
--rw-r--r--   0 runner    (1001) docker     (121)    10511 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/wafregional/geo_match_set.py
--rw-r--r--   0 runner    (1001) docker     (121)     2779 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/wafregional/get_ipset.py
--rw-r--r--   0 runner    (1001) docker     (121)     3019 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/wafregional/get_rate_based_mod.py
--rw-r--r--   0 runner    (1001) docker     (121)     2745 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/wafregional/get_rule.py
--rw-r--r--   0 runner    (1001) docker     (121)     2818 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/wafregional/get_web_acl.py
--rw-r--r--   0 runner    (1001) docker     (121)    11263 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/wafregional/ip_set.py
--rw-r--r--   0 runner    (1001) docker     (121)    44100 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/wafregional/outputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    22090 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/wafregional/rate_based_rule.py
--rw-r--r--   0 runner    (1001) docker     (121)    11456 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/wafregional/regex_match_set.py
--rw-r--r--   0 runner    (1001) docker     (121)     9641 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/wafregional/regex_pattern_set.py
--rw-r--r--   0 runner    (1001) docker     (121)    18253 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/wafregional/rule.py
--rw-r--r--   0 runner    (1001) docker     (121)    17251 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/wafregional/rule_group.py
--rw-r--r--   0 runner    (1001) docker     (121)    11173 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/wafregional/size_constraint_set.py
--rw-r--r--   0 runner    (1001) docker     (121)    11680 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/wafregional/sql_injection_match_set.py
--rw-r--r--   0 runner    (1001) docker     (121)    27836 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/wafregional/web_acl.py
--rw-r--r--   0 runner    (1001) docker     (121)    17670 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/wafregional/web_acl_association.py
--rw-r--r--   0 runner    (1001) docker     (121)    10508 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/wafregional/xss_match_set.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-21 22:50:29.000000 pulumi_aws-5.9.1/pulumi_aws/wafv2/
--rw-r--r--   0 runner    (1001) docker     (121)      618 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/wafv2/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)  9094354 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/wafv2/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)     5790 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/wafv2/get_ip_set.py
--rw-r--r--   0 runner    (1001) docker     (121)     5727 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/wafv2/get_regex_pattern_set.py
--rw-r--r--   0 runner    (1001) docker     (121)     4768 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/wafv2/get_rule_group.py
--rw-r--r--   0 runner    (1001) docker     (121)     4674 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/wafv2/get_web_acl.py
--rw-r--r--   0 runner    (1001) docker     (121)    23504 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/wafv2/ip_set.py
--rw-r--r--   0 runner    (1001) docker     (121)  8545270 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/wafv2/outputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    22942 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/wafv2/regex_pattern_set.py
--rw-r--r--   0 runner    (1001) docker     (121)    57600 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/wafv2/rule_group.py
--rw-r--r--   0 runner    (1001) docker     (121)    50144 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/wafv2/web_acl.py
--rw-r--r--   0 runner    (1001) docker     (121)    14786 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/wafv2/web_acl_association.py
--rw-r--r--   0 runner    (1001) docker     (121)    25303 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/wafv2/web_acl_logging_configuration.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-21 22:50:29.000000 pulumi_aws-5.9.1/pulumi_aws/worklink/
--rw-r--r--   0 runner    (1001) docker     (121)      392 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/worklink/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     3692 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/worklink/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    28567 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/worklink/fleet.py
--rw-r--r--   0 runner    (1001) docker     (121)     4019 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/worklink/outputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    12467 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/worklink/website_certificate_authority_association.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-21 22:50:29.000000 pulumi_aws-5.9.1/pulumi_aws/workspaces/
--rw-r--r--   0 runner    (1001) docker     (121)      497 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/workspaces/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    21453 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/workspaces/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    45328 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/workspaces/directory.py
--rw-r--r--   0 runner    (1001) docker     (121)     7163 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/workspaces/get_bundle.py
--rw-r--r--   0 runner    (1001) docker     (121)    12048 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/workspaces/get_directory.py
--rw-r--r--   0 runner    (1001) docker     (121)     5449 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/workspaces/get_image.py
--rw-r--r--   0 runner    (1001) docker     (121)    10781 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/workspaces/get_workspace.py
--rw-r--r--   0 runner    (1001) docker     (121)    16204 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/workspaces/ip_group.py
--rw-r--r--   0 runner    (1001) docker     (121)    35399 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/workspaces/outputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    31829 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/workspaces/workspace.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-21 22:50:29.000000 pulumi_aws-5.9.1/pulumi_aws/xray/
--rw-r--r--   0 runner    (1001) docker     (121)      397 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/xray/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     1845 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/xray/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    10614 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/xray/encryption_config.py
--rw-r--r--   0 runner    (1001) docker     (121)    18341 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/xray/group.py
--rw-r--r--   0 runner    (1001) docker     (121)     2151 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/xray/outputs.py
--rw-r--r--   0 runner    (1001) docker     (121)    36166 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/pulumi_aws/xray/sampling_rule.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-21 22:50:28.000000 pulumi_aws-5.9.1/pulumi_aws.egg-info/
--rw-r--r--   0 runner    (1001) docker     (121)    10151 2022-06-21 22:50:28.000000 pulumi_aws-5.9.1/pulumi_aws.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (121)    70754 2022-06-21 22:50:28.000000 pulumi_aws-5.9.1/pulumi_aws.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (121)        1 2022-06-21 22:50:28.000000 pulumi_aws-5.9.1/pulumi_aws.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (121)        1 2022-06-21 22:50:28.000000 pulumi_aws-5.9.1/pulumi_aws.egg-info/not-zip-safe
--rw-r--r--   0 runner    (1001) docker     (121)       49 2022-06-21 22:50:28.000000 pulumi_aws-5.9.1/pulumi_aws.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (121)       11 2022-06-21 22:50:28.000000 pulumi_aws-5.9.1/pulumi_aws.egg-info/top_level.txt
--rw-r--r--   0 runner    (1001) docker     (121)       38 2022-06-21 22:50:29.000000 pulumi_aws-5.9.1/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (121)     2082 2022-06-21 22:50:27.000000 pulumi_aws-5.9.1/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-24 22:23:25.000000 pulumi_aws-5.9.2/
+-rw-r--r--   0 runner    (1001) docker     (121)    10151 2022-06-24 22:23:25.000000 pulumi_aws-5.9.2/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (121)     8590 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/README.md
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-24 22:23:25.000000 pulumi_aws-5.9.2/pulumi_aws/
+-rw-r--r--   0 runner    (1001) docker     (121)   203842 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1140 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/_enums.py
+-rw-r--r--   0 runner    (1001) docker     (121)   181075 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7667 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/_utilities.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-24 22:23:25.000000 pulumi_aws-5.9.2/pulumi_aws/accessanalyzer/
+-rw-r--r--   0 runner    (1001) docker     (121)      293 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/accessanalyzer/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    15135 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/accessanalyzer/analyzer.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-24 22:23:25.000000 pulumi_aws-5.9.2/pulumi_aws/account/
+-rw-r--r--   0 runner    (1001) docker     (121)      304 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/account/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    18354 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/account/alternative_contact.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-24 22:23:25.000000 pulumi_aws-5.9.2/pulumi_aws/acm/
+-rw-r--r--   0 runner    (1001) docker     (121)      410 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/acm/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6817 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/acm/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    44216 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/acm/certificate.py
+-rw-r--r--   0 runner    (1001) docker     (121)    15415 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/acm/certificate_validation.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11052 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/acm/get_certificate.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7598 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/acm/outputs.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-24 22:23:25.000000 pulumi_aws-5.9.2/pulumi_aws/acmpca/
+-rw-r--r--   0 runner    (1001) docker     (121)      521 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/acmpca/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    24902 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/acmpca/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    21275 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/acmpca/certificate.py
+-rw-r--r--   0 runner    (1001) docker     (121)    43082 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/acmpca/certificate_authority.py
+-rw-r--r--   0 runner    (1001) docker     (121)    20101 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/acmpca/certificate_authority_certificate.py
+-rw-r--r--   0 runner    (1001) docker     (121)     5724 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/acmpca/get_certificate.py
+-rw-r--r--   0 runner    (1001) docker     (121)    13445 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/acmpca/get_certificate_authority.py
+-rw-r--r--   0 runner    (1001) docker     (121)    23238 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/acmpca/outputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    12620 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/acmpca/policy.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-24 22:23:25.000000 pulumi_aws-5.9.2/pulumi_aws/alb/
+-rw-r--r--   0 runner    (1001) docker     (121)      614 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/alb/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)      440 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/alb/_enums.py
+-rw-r--r--   0 runner    (1001) docker     (121)    98592 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/alb/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)     8158 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/alb/get_listener.py
+-rw-r--r--   0 runner    (1001) docker     (121)    13831 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/alb/get_load_balancer.py
+-rw-r--r--   0 runner    (1001) docker     (121)    12411 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/alb/get_target_group.py
+-rw-r--r--   0 runner    (1001) docker     (121)    40568 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/alb/listener.py
+-rw-r--r--   0 runner    (1001) docker     (121)    10903 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/alb/listener_certificate.py
+-rw-r--r--   0 runner    (1001) docker     (121)    34480 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/alb/listener_rule.py
+-rw-r--r--   0 runner    (1001) docker     (121)    69182 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/alb/load_balancer.py
+-rw-r--r--   0 runner    (1001) docker     (121)   108001 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/alb/outputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    61612 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/alb/target_group.py
+-rw-r--r--   0 runner    (1001) docker     (121)    18032 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/alb/target_group_attachment.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-24 22:23:25.000000 pulumi_aws-5.9.2/pulumi_aws/amp/
+-rw-r--r--   0 runner    (1001) docker     (121)      370 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/amp/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    10626 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/amp/alert_manager_definition.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11968 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/amp/rule_group_namespace.py
+-rw-r--r--   0 runner    (1001) docker     (121)    15508 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/amp/workspace.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-24 22:23:25.000000 pulumi_aws-5.9.2/pulumi_aws/amplify/
+-rw-r--r--   0 runner    (1001) docker     (121)      447 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/amplify/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    15473 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/amplify/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    61933 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/amplify/app.py
+-rw-r--r--   0 runner    (1001) docker     (121)    14535 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/amplify/backend_environment.py
+-rw-r--r--   0 runner    (1001) docker     (121)    57659 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/amplify/branch.py
+-rw-r--r--   0 runner    (1001) docker     (121)    18870 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/amplify/domain_association.py
+-rw-r--r--   0 runner    (1001) docker     (121)    14037 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/amplify/outputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    12484 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/amplify/webhook.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-24 22:23:25.000000 pulumi_aws-5.9.2/pulumi_aws/apigateway/
+-rw-r--r--   0 runner    (1001) docker     (121)     1169 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/apigateway/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    35129 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/apigateway/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    13087 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/apigateway/account.py
+-rw-r--r--   0 runner    (1001) docker     (121)    20255 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/apigateway/api_key.py
+-rw-r--r--   0 runner    (1001) docker     (121)    37189 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/apigateway/authorizer.py
+-rw-r--r--   0 runner    (1001) docker     (121)    16540 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/apigateway/base_path_mapping.py
+-rw-r--r--   0 runner    (1001) docker     (121)    15668 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/apigateway/client_certificate.py
+-rw-r--r--   0 runner    (1001) docker     (121)    32058 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/apigateway/deployment.py
+-rw-r--r--   0 runner    (1001) docker     (121)    13567 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/apigateway/documentation_part.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11928 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/apigateway/documentation_version.py
+-rw-r--r--   0 runner    (1001) docker     (121)    71877 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/apigateway/domain_name.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11613 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/apigateway/get_domain_name.py
+-rw-r--r--   0 runner    (1001) docker     (121)     8428 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/apigateway/get_export.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6021 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/apigateway/get_key.py
+-rw-r--r--   0 runner    (1001) docker     (121)     5091 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/apigateway/get_resource.py
+-rw-r--r--   0 runner    (1001) docker     (121)     9517 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/apigateway/get_rest_api.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7942 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/apigateway/get_sdk.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6332 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/apigateway/get_vpc_link.py
+-rw-r--r--   0 runner    (1001) docker     (121)    71695 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/apigateway/integration.py
+-rw-r--r--   0 runner    (1001) docker     (121)    30964 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/apigateway/integration_response.py
+-rw-r--r--   0 runner    (1001) docker     (121)    37954 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/apigateway/method.py
+-rw-r--r--   0 runner    (1001) docker     (121)    21035 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/apigateway/method_response.py
+-rw-r--r--   0 runner    (1001) docker     (121)    18612 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/apigateway/method_settings.py
+-rw-r--r--   0 runner    (1001) docker     (121)    13858 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/apigateway/model.py
+-rw-r--r--   0 runner    (1001) docker     (121)    36863 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/apigateway/outputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    13613 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/apigateway/request_validator.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11667 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/apigateway/resource.py
+-rw-r--r--   0 runner    (1001) docker     (121)    17203 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/apigateway/response.py
+-rw-r--r--   0 runner    (1001) docker     (121)    71567 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/apigateway/rest_api.py
+-rw-r--r--   0 runner    (1001) docker     (121)    10249 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/apigateway/rest_api_policy.py
+-rw-r--r--   0 runner    (1001) docker     (121)    49413 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/apigateway/stage.py
+-rw-r--r--   0 runner    (1001) docker     (121)    27887 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/apigateway/usage_plan.py
+-rw-r--r--   0 runner    (1001) docker     (121)    13442 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/apigateway/usage_plan_key.py
+-rw-r--r--   0 runner    (1001) docker     (121)    16707 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/apigateway/vpc_link.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-24 22:23:25.000000 pulumi_aws-5.9.2/pulumi_aws/apigatewayv2/
+-rw-r--r--   0 runner    (1001) docker     (121)      692 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/apigatewayv2/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    30148 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/apigatewayv2/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    55324 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/apigatewayv2/api.py
+-rw-r--r--   0 runner    (1001) docker     (121)    14151 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/apigatewayv2/api_mapping.py
+-rw-r--r--   0 runner    (1001) docker     (121)    39499 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/apigatewayv2/authorizer.py
+-rw-r--r--   0 runner    (1001) docker     (121)    13810 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/apigatewayv2/deployment.py
+-rw-r--r--   0 runner    (1001) docker     (121)    24087 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/apigatewayv2/domain_name.py
+-rw-r--r--   0 runner    (1001) docker     (121)    10509 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/apigatewayv2/get_api.py
+-rw-r--r--   0 runner    (1001) docker     (121)     4619 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/apigatewayv2/get_apis.py
+-rw-r--r--   0 runner    (1001) docker     (121)     8061 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/apigatewayv2/get_export.py
+-rw-r--r--   0 runner    (1001) docker     (121)    75096 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/apigatewayv2/integration.py
+-rw-r--r--   0 runner    (1001) docker     (121)    21925 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/apigatewayv2/integration_response.py
+-rw-r--r--   0 runner    (1001) docker     (121)    16550 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/apigatewayv2/model.py
+-rw-r--r--   0 runner    (1001) docker     (121)    33037 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/apigatewayv2/outputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    43442 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/apigatewayv2/route.py
+-rw-r--r--   0 runner    (1001) docker     (121)    17359 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/apigatewayv2/route_response.py
+-rw-r--r--   0 runner    (1001) docker     (121)    41165 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/apigatewayv2/stage.py
+-rw-r--r--   0 runner    (1001) docker     (121)    17331 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/apigatewayv2/vpc_link.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-24 22:23:25.000000 pulumi_aws-5.9.2/pulumi_aws/appautoscaling/
+-rw-r--r--   0 runner    (1001) docker     (121)      390 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/appautoscaling/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    22755 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/appautoscaling/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    22861 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/appautoscaling/outputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    42828 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/appautoscaling/policy.py
+-rw-r--r--   0 runner    (1001) docker     (121)    39812 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/appautoscaling/scheduled_action.py
+-rw-r--r--   0 runner    (1001) docker     (121)    30990 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/appautoscaling/target.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-24 22:23:25.000000 pulumi_aws-5.9.2/pulumi_aws/appconfig/
+-rw-r--r--   0 runner    (1001) docker     (121)      543 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/appconfig/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     3602 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/appconfig/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    14431 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/appconfig/application.py
+-rw-r--r--   0 runner    (1001) docker     (121)    34435 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/appconfig/configuration_profile.py
+-rw-r--r--   0 runner    (1001) docker     (121)    29431 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/appconfig/deployment.py
+-rw-r--r--   0 runner    (1001) docker     (121)    29185 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/appconfig/deployment_strategy.py
+-rw-r--r--   0 runner    (1001) docker     (121)    22958 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/appconfig/environment.py
+-rw-r--r--   0 runner    (1001) docker     (121)    20776 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/appconfig/event_integration.py
+-rw-r--r--   0 runner    (1001) docker     (121)    23444 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/appconfig/hosted_configuration_version.py
+-rw-r--r--   0 runner    (1001) docker     (121)     3434 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/appconfig/outputs.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-24 22:23:25.000000 pulumi_aws-5.9.2/pulumi_aws/appflow/
+-rw-r--r--   0 runner    (1001) docker     (121)      367 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/appflow/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)   318810 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/appflow/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    26462 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/appflow/connector_profile.py
+-rw-r--r--   0 runner    (1001) docker     (121)    37753 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/appflow/flow.py
+-rw-r--r--   0 runner    (1001) docker     (121)   326161 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/appflow/outputs.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-24 22:23:25.000000 pulumi_aws-5.9.2/pulumi_aws/applicationloadbalancing/
+-rw-r--r--   0 runner    (1001) docker     (121)      614 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/applicationloadbalancing/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)      440 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/applicationloadbalancing/_enums.py
+-rw-r--r--   0 runner    (1001) docker     (121)    98592 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/applicationloadbalancing/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)     8610 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/applicationloadbalancing/get_listener.py
+-rw-r--r--   0 runner    (1001) docker     (121)    14317 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/applicationloadbalancing/get_load_balancer.py
+-rw-r--r--   0 runner    (1001) docker     (121)    12889 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/applicationloadbalancing/get_target_group.py
+-rw-r--r--   0 runner    (1001) docker     (121)    40850 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/applicationloadbalancing/listener.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11240 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/applicationloadbalancing/listener_certificate.py
+-rw-r--r--   0 runner    (1001) docker     (121)    34782 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/applicationloadbalancing/listener_rule.py
+-rw-r--r--   0 runner    (1001) docker     (121)    69484 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/applicationloadbalancing/load_balancer.py
+-rw-r--r--   0 runner    (1001) docker     (121)   108001 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/applicationloadbalancing/outputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    61909 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/applicationloadbalancing/target_group.py
+-rw-r--r--   0 runner    (1001) docker     (121)    18337 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/applicationloadbalancing/target_group_attachment.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-24 22:23:25.000000 pulumi_aws-5.9.2/pulumi_aws/appmesh/
+-rw-r--r--   0 runner    (1001) docker     (121)      563 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/appmesh/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)   278013 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/appmesh/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    27745 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/appmesh/gateway_route.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7079 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/appmesh/get_mesh.py
+-rw-r--r--   0 runner    (1001) docker     (121)     8401 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/appmesh/get_virtual_service.py
+-rw-r--r--   0 runner    (1001) docker     (121)    18857 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/appmesh/mesh.py
+-rw-r--r--   0 runner    (1001) docker     (121)   277292 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/appmesh/outputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    34208 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/appmesh/route.py
+-rw-r--r--   0 runner    (1001) docker     (121)    26819 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/appmesh/virtual_gateway.py
+-rw-r--r--   0 runner    (1001) docker     (121)    34516 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/appmesh/virtual_node.py
+-rw-r--r--   0 runner    (1001) docker     (121)    25260 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/appmesh/virtual_router.py
+-rw-r--r--   0 runner    (1001) docker     (121)    25233 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/appmesh/virtual_service.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-24 22:23:25.000000 pulumi_aws-5.9.2/pulumi_aws/apprunner/
+-rw-r--r--   0 runner    (1001) docker     (121)      483 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/apprunner/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    37661 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/apprunner/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    25757 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/apprunner/auto_scaling_configuration_version.py
+-rw-r--r--   0 runner    (1001) docker     (121)    16028 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/apprunner/connection.py
+-rw-r--r--   0 runner    (1001) docker     (121)    19214 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/apprunner/custom_domain_association.py
+-rw-r--r--   0 runner    (1001) docker     (121)    38808 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/apprunner/outputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    43125 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/apprunner/service.py
+-rw-r--r--   0 runner    (1001) docker     (121)    22045 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/apprunner/vpc_connector.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-24 22:23:25.000000 pulumi_aws-5.9.2/pulumi_aws/appstream/
+-rw-r--r--   0 runner    (1001) docker     (121)      514 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/appstream/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    18918 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/appstream/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    16560 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/appstream/directory_config.py
+-rw-r--r--   0 runner    (1001) docker     (121)    51603 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/appstream/fleet.py
+-rw-r--r--   0 runner    (1001) docker     (121)     9478 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/appstream/fleet_stack_association.py
+-rw-r--r--   0 runner    (1001) docker     (121)    42239 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/appstream/image_builder.py
+-rw-r--r--   0 runner    (1001) docker     (121)    20772 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/appstream/outputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    36260 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/appstream/stack.py
+-rw-r--r--   0 runner    (1001) docker     (121)    19263 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/appstream/user.py
+-rw-r--r--   0 runner    (1001) docker     (121)    14729 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/appstream/user_stack_association.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-24 22:23:25.000000 pulumi_aws-5.9.2/pulumi_aws/appsync/
+-rw-r--r--   0 runner    (1001) docker     (121)      535 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/appsync/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    52133 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/appsync/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    18542 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/appsync/api_cache.py
+-rw-r--r--   0 runner    (1001) docker     (121)    12034 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/appsync/api_key.py
+-rw-r--r--   0 runner    (1001) docker     (121)    31383 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/appsync/data_source.py
+-rw-r--r--   0 runner    (1001) docker     (121)    14048 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/appsync/domain_name.py
+-rw-r--r--   0 runner    (1001) docker     (121)     8626 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/appsync/domain_name_api_association.py
+-rw-r--r--   0 runner    (1001) docker     (121)    29365 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/appsync/function.py
+-rw-r--r--   0 runner    (1001) docker     (121)    46549 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/appsync/graph_ql_api.py
+-rw-r--r--   0 runner    (1001) docker     (121)    55789 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/appsync/outputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    34156 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/appsync/resolver.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-24 22:23:25.000000 pulumi_aws-5.9.2/pulumi_aws/athena/
+-rw-r--r--   0 runner    (1001) docker     (121)      418 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/athena/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    19263 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/athena/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    24629 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/athena/data_catalog.py
+-rw-r--r--   0 runner    (1001) docker     (121)    26291 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/athena/database.py
+-rw-r--r--   0 runner    (1001) docker     (121)    16068 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/athena/named_query.py
+-rw-r--r--   0 runner    (1001) docker     (121)    21006 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/athena/outputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    21675 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/athena/workgroup.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-24 22:23:25.000000 pulumi_aws-5.9.2/pulumi_aws/autoscaling/
+-rw-r--r--   0 runner    (1001) docker     (121)      558 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/autoscaling/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1748 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/autoscaling/_enums.py
+-rw-r--r--   0 runner    (1001) docker     (121)   144801 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/autoscaling/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    16273 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/autoscaling/attachment.py
+-rw-r--r--   0 runner    (1001) docker     (121)     5977 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/autoscaling/get_ami_ids.py
+-rw-r--r--   0 runner    (1001) docker     (121)    14114 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/autoscaling/get_group.py
+-rw-r--r--   0 runner    (1001) docker     (121)   145637 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/autoscaling/group.py
+-rw-r--r--   0 runner    (1001) docker     (121)    31037 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/autoscaling/lifecycle_hook.py
+-rw-r--r--   0 runner    (1001) docker     (121)    13877 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/autoscaling/notification.py
+-rw-r--r--   0 runner    (1001) docker     (121)   139988 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/autoscaling/outputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    55718 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/autoscaling/policy.py
+-rw-r--r--   0 runner    (1001) docker     (121)    30907 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/autoscaling/schedule.py
+-rw-r--r--   0 runner    (1001) docker     (121)     8621 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/autoscaling/tag.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-24 22:23:25.000000 pulumi_aws-5.9.2/pulumi_aws/autoscalingplans/
+-rw-r--r--   0 runner    (1001) docker     (121)      342 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/autoscalingplans/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    37628 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/autoscalingplans/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    36367 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/autoscalingplans/outputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    16378 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/autoscalingplans/scaling_plan.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-24 22:23:25.000000 pulumi_aws-5.9.2/pulumi_aws/backup/
+-rw-r--r--   0 runner    (1001) docker     (121)      735 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/backup/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    35190 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/backup/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    26988 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/backup/framework.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7671 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/backup/get_framework.py
+-rw-r--r--   0 runner    (1001) docker     (121)     4884 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/backup/get_plan.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7472 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/backup/get_report_plan.py
+-rw-r--r--   0 runner    (1001) docker     (121)     5639 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/backup/get_selection.py
+-rw-r--r--   0 runner    (1001) docker     (121)     5079 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/backup/get_vault.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7425 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/backup/global_settings.py
+-rw-r--r--   0 runner    (1001) docker     (121)    41682 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/backup/outputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    19919 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/backup/plan.py
+-rw-r--r--   0 runner    (1001) docker     (121)    12261 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/backup/region_settings.py
+-rw-r--r--   0 runner    (1001) docker     (121)    27055 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/backup/report_plan.py
+-rw-r--r--   0 runner    (1001) docker     (121)    31506 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/backup/selection.py
+-rw-r--r--   0 runner    (1001) docker     (121)    15024 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/backup/vault.py
+-rw-r--r--   0 runner    (1001) docker     (121)    15559 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/backup/vault_lock_configuration.py
+-rw-r--r--   0 runner    (1001) docker     (121)    15388 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/backup/vault_notifications.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11511 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/backup/vault_policy.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-24 22:23:25.000000 pulumi_aws-5.9.2/pulumi_aws/batch/
+-rw-r--r--   0 runner    (1001) docker     (121)      542 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/batch/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    32642 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/batch/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    40843 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/batch/compute_environment.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7979 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/batch/get_compute_environment.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7993 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/batch/get_job_queue.py
+-rw-r--r--   0 runner    (1001) docker     (121)     4959 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/batch/get_scheduling_policy.py
+-rw-r--r--   0 runner    (1001) docker     (121)    37517 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/batch/job_definition.py
+-rw-r--r--   0 runner    (1001) docker     (121)    26370 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/batch/job_queue.py
+-rw-r--r--   0 runner    (1001) docker     (121)    37266 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/batch/outputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    16390 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/batch/scheduling_policy.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-24 22:23:25.000000 pulumi_aws-5.9.2/pulumi_aws/budgets/
+-rw-r--r--   0 runner    (1001) docker     (121)      365 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/budgets/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    26616 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/budgets/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    45784 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/budgets/budget.py
+-rw-r--r--   0 runner    (1001) docker     (121)    34780 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/budgets/budget_action.py
+-rw-r--r--   0 runner    (1001) docker     (121)    26097 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/budgets/outputs.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-24 22:23:25.000000 pulumi_aws-5.9.2/pulumi_aws/cfg/
+-rw-r--r--   0 runner    (1001) docker     (121)      699 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/cfg/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    32730 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/cfg/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    13607 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/cfg/aggregate_authorization.py
+-rw-r--r--   0 runner    (1001) docker     (121)    21739 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/cfg/configuration_aggregator.py
+-rw-r--r--   0 runner    (1001) docker     (121)    28387 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/cfg/conformance_pack.py
+-rw-r--r--   0 runner    (1001) docker     (121)    21947 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/cfg/delivery_channel.py
+-rw-r--r--   0 runner    (1001) docker     (121)    34649 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/cfg/organization_conformance_pack.py
+-rw-r--r--   0 runner    (1001) docker     (121)    36285 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/cfg/organization_custom_rule.py
+-rw-r--r--   0 runner    (1001) docker     (121)    33065 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/cfg/organization_managed_rule.py
+-rw-r--r--   0 runner    (1001) docker     (121)    35470 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/cfg/outputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    13775 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/cfg/recorder.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11627 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/cfg/recorder_status.py
+-rw-r--r--   0 runner    (1001) docker     (121)    33725 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/cfg/remediation_configuration.py
+-rw-r--r--   0 runner    (1001) docker     (121)    32351 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/cfg/rule.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-24 22:23:25.000000 pulumi_aws-5.9.2/pulumi_aws/chime/
+-rw-r--r--   0 runner    (1001) docker     (121)      604 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/chime/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6304 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/chime/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)     5486 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/chime/outputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    12580 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/chime/voice_connector.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11129 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/chime/voice_connector_group.py
+-rw-r--r--   0 runner    (1001) docker     (121)    10112 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/chime/voice_connector_logging.py
+-rw-r--r--   0 runner    (1001) docker     (121)    14381 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/chime/voice_connector_organization.py
+-rw-r--r--   0 runner    (1001) docker     (121)    15601 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/chime/voice_connector_streaming.py
+-rw-r--r--   0 runner    (1001) docker     (121)    19770 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/chime/voice_connector_termination.py
+-rw-r--r--   0 runner    (1001) docker     (121)    12644 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/chime/voice_connector_termination_credentials.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-24 22:23:25.000000 pulumi_aws-5.9.2/pulumi_aws/cloud9/
+-rw-r--r--   0 runner    (1001) docker     (121)      338 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/cloud9/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    34461 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/cloud9/environment_ec2.py
+-rw-r--r--   0 runner    (1001) docker     (121)    13825 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/cloud9/environment_membership.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-24 22:23:25.000000 pulumi_aws-5.9.2/pulumi_aws/cloudcontrol/
+-rw-r--r--   0 runner    (1001) docker     (121)      321 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/cloudcontrol/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6145 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/cloudcontrol/get_resource.py
+-rw-r--r--   0 runner    (1001) docker     (121)    18195 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/cloudcontrol/resource.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-24 22:23:25.000000 pulumi_aws-5.9.2/pulumi_aws/cloudformation/
+-rw-r--r--   0 runner    (1001) docker     (121)      521 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/cloudformation/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    13376 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/cloudformation/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    36044 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/cloudformation/cloud_formation_type.py
+-rw-r--r--   0 runner    (1001) docker     (121)    12006 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/cloudformation/get_cloud_formation_type.py
+-rw-r--r--   0 runner    (1001) docker     (121)     5300 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/cloudformation/get_export.py
+-rw-r--r--   0 runner    (1001) docker     (121)     8808 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/cloudformation/get_stack.py
+-rw-r--r--   0 runner    (1001) docker     (121)    15232 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/cloudformation/outputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    41265 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/cloudformation/stack.py
+-rw-r--r--   0 runner    (1001) docker     (121)    54563 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/cloudformation/stack_set.py
+-rw-r--r--   0 runner    (1001) docker     (121)    38604 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/cloudformation/stack_set_instance.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-24 22:23:25.000000 pulumi_aws-5.9.2/pulumi_aws/cloudfront/
+-rw-r--r--   0 runner    (1001) docker     (121)     1075 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/cloudfront/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)   176699 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/cloudfront/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    25221 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/cloudfront/cache_policy.py
+-rw-r--r--   0 runner    (1001) docker     (121)    96004 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/cloudfront/distribution.py
+-rw-r--r--   0 runner    (1001) docker     (121)    20439 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/cloudfront/field_level_encryption_config.py
+-rw-r--r--   0 runner    (1001) docker     (121)    16600 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/cloudfront/field_level_encryption_profile.py
+-rw-r--r--   0 runner    (1001) docker     (121)    19341 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/cloudfront/function.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6993 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/cloudfront/get_cache_policy.py
+-rw-r--r--   0 runner    (1001) docker     (121)     8214 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/cloudfront/get_distribution.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6646 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/cloudfront/get_function.py
+-rw-r--r--   0 runner    (1001) docker     (121)     5232 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/cloudfront/get_log_delivery_canonical_user_id.py
+-rw-r--r--   0 runner    (1001) docker     (121)     5735 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/cloudfront/get_origin_access_identities.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6092 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/cloudfront/get_origin_access_identity.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6781 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/cloudfront/get_origin_request_policy.py
+-rw-r--r--   0 runner    (1001) docker     (121)     5417 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/cloudfront/get_realtime_log_config.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7560 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/cloudfront/get_response_headers_policy.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11627 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/cloudfront/key_group.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11976 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/cloudfront/monitoring_subscription.py
+-rw-r--r--   0 runner    (1001) docker     (121)    19455 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/cloudfront/origin_access_identity.py
+-rw-r--r--   0 runner    (1001) docker     (121)    23360 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/cloudfront/origin_request_policy.py
+-rw-r--r--   0 runner    (1001) docker     (121)   222138 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/cloudfront/outputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    15247 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/cloudfront/public_key.py
+-rw-r--r--   0 runner    (1001) docker     (121)    20098 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/cloudfront/realtime_log_config.py
+-rw-r--r--   0 runner    (1001) docker     (121)    30889 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/cloudfront/response_headers_policy.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-24 22:23:25.000000 pulumi_aws-5.9.2/pulumi_aws/cloudhsmv2/
+-rw-r--r--   0 runner    (1001) docker     (121)      383 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/cloudhsmv2/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     3222 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/cloudhsmv2/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    25824 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/cloudhsmv2/cluster.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6744 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/cloudhsmv2/get_cluster.py
+-rw-r--r--   0 runner    (1001) docker     (121)    16530 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/cloudhsmv2/hsm.py
+-rw-r--r--   0 runner    (1001) docker     (121)     4785 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/cloudhsmv2/outputs.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-24 22:23:25.000000 pulumi_aws-5.9.2/pulumi_aws/cloudsearch/
+-rw-r--r--   0 runner    (1001) docker     (121)      380 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/cloudsearch/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    12450 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/cloudsearch/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    24612 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/cloudsearch/domain.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11233 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/cloudsearch/domain_service_access_policy.py
+-rw-r--r--   0 runner    (1001) docker     (121)    12014 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/cloudsearch/outputs.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-24 22:23:25.000000 pulumi_aws-5.9.2/pulumi_aws/cloudtrail/
+-rw-r--r--   0 runner    (1001) docker     (121)      430 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/cloudtrail/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    24249 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/cloudtrail/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    36099 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/cloudtrail/event_data_store.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7056 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/cloudtrail/get_function.py
+-rw-r--r--   0 runner    (1001) docker     (121)     5678 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/cloudtrail/get_service_account.py
+-rw-r--r--   0 runner    (1001) docker     (121)    23183 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/cloudtrail/outputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    75455 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/cloudtrail/trail.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-24 22:23:25.000000 pulumi_aws-5.9.2/pulumi_aws/cloudwatch/
+-rw-r--r--   0 runner    (1001) docker     (121)     1083 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/cloudwatch/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    86079 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/cloudwatch/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    32423 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/cloudwatch/composite_alarm.py
+-rw-r--r--   0 runner    (1001) docker     (121)    13384 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/cloudwatch/dashboard.py
+-rw-r--r--   0 runner    (1001) docker     (121)    22231 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/cloudwatch/event_api_destination.py
+-rw-r--r--   0 runner    (1001) docker     (121)    18597 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/cloudwatch/event_archive.py
+-rw-r--r--   0 runner    (1001) docker     (121)    16009 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/cloudwatch/event_bus.py
+-rw-r--r--   0 runner    (1001) docker     (121)    16665 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/cloudwatch/event_bus_policy.py
+-rw-r--r--   0 runner    (1001) docker     (121)    25515 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/cloudwatch/event_connection.py
+-rw-r--r--   0 runner    (1001) docker     (121)    19895 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/cloudwatch/event_permission.py
+-rw-r--r--   0 runner    (1001) docker     (121)    33255 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/cloudwatch/event_rule.py
+-rw-r--r--   0 runner    (1001) docker     (121)    73858 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/cloudwatch/event_target.py
+-rw-r--r--   0 runner    (1001) docker     (121)     3486 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/cloudwatch/get_event_bus.py
+-rw-r--r--   0 runner    (1001) docker     (121)     4853 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/cloudwatch/get_event_connection.py
+-rw-r--r--   0 runner    (1001) docker     (121)     5501 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/cloudwatch/get_event_source.py
+-rw-r--r--   0 runner    (1001) docker     (121)     5884 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/cloudwatch/get_log_group.py
+-rw-r--r--   0 runner    (1001) docker     (121)     4260 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/cloudwatch/get_log_groups.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11998 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/cloudwatch/log_destination.py
+-rw-r--r--   0 runner    (1001) docker     (121)    13682 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/cloudwatch/log_destination_policy.py
+-rw-r--r--   0 runner    (1001) docker     (121)    23294 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/cloudwatch/log_group.py
+-rw-r--r--   0 runner    (1001) docker     (121)    15504 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/cloudwatch/log_metric_filter.py
+-rw-r--r--   0 runner    (1001) docker     (121)    13196 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/cloudwatch/log_resource_policy.py
+-rw-r--r--   0 runner    (1001) docker     (121)     9956 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/cloudwatch/log_stream.py
+-rw-r--r--   0 runner    (1001) docker     (121)    21782 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/cloudwatch/log_subscription_filter.py
+-rw-r--r--   0 runner    (1001) docker     (121)    83958 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/cloudwatch/metric_alarm.py
+-rw-r--r--   0 runner    (1001) docker     (121)    51529 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/cloudwatch/metric_stream.py
+-rw-r--r--   0 runner    (1001) docker     (121)    84523 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/cloudwatch/outputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    13536 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/cloudwatch/query_definition.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-24 22:23:25.000000 pulumi_aws-5.9.2/pulumi_aws/codeartifact/
+-rw-r--r--   0 runner    (1001) docker     (121)      519 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/codeartifact/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2807 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/codeartifact/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    21250 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/codeartifact/domain.py
+-rw-r--r--   0 runner    (1001) docker     (121)    16987 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/codeartifact/domain_permissions.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6344 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/codeartifact/get_authorization_token.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6416 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/codeartifact/get_repository_endpoint.py
+-rw-r--r--   0 runner    (1001) docker     (121)     3390 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/codeartifact/outputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    29357 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/codeartifact/repository.py
+-rw-r--r--   0 runner    (1001) docker     (121)    19899 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/codeartifact/repository_permissions_policy.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-24 22:23:25.000000 pulumi_aws-5.9.2/pulumi_aws/codebuild/
+-rw-r--r--   0 runner    (1001) docker     (121)      452 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/codebuild/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    86494 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/codebuild/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    81754 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/codebuild/outputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    82917 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/codebuild/project.py
+-rw-r--r--   0 runner    (1001) docker     (121)    23135 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/codebuild/report_group.py
+-rw-r--r--   0 runner    (1001) docker     (121)    13286 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/codebuild/resource_policy.py
+-rw-r--r--   0 runner    (1001) docker     (121)    16676 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/codebuild/source_credential.py
+-rw-r--r--   0 runner    (1001) docker     (121)    24773 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/codebuild/webhook.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-24 22:23:25.000000 pulumi_aws-5.9.2/pulumi_aws/codecommit/
+-rw-r--r--   0 runner    (1001) docker     (121)      523 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/codecommit/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     4436 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/codecommit/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    18955 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/codecommit/approval_rule_template.py
+-rw-r--r--   0 runner    (1001) docker     (121)    10565 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/codecommit/approval_rule_template_association.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7432 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/codecommit/get_approval_rule_template.py
+-rw-r--r--   0 runner    (1001) docker     (121)     5361 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/codecommit/get_repository.py
+-rw-r--r--   0 runner    (1001) docker     (121)     4121 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/codecommit/outputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    20253 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/codecommit/repository.py
+-rw-r--r--   0 runner    (1001) docker     (121)     9909 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/codecommit/trigger.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-24 22:23:25.000000 pulumi_aws-5.9.2/pulumi_aws/codedeploy/
+-rw-r--r--   0 runner    (1001) docker     (121)      406 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/codedeploy/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    49133 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/codedeploy/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    18533 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/codedeploy/application.py
+-rw-r--r--   0 runner    (1001) docker     (121)    22789 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/codedeploy/deployment_config.py
+-rw-r--r--   0 runner    (1001) docker     (121)    72884 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/codedeploy/deployment_group.py
+-rw-r--r--   0 runner    (1001) docker     (121)    48707 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/codedeploy/outputs.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-24 22:23:25.000000 pulumi_aws-5.9.2/pulumi_aws/codepipeline/
+-rw-r--r--   0 runner    (1001) docker     (121)      361 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/codepipeline/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    18164 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/codepipeline/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    16639 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/codepipeline/outputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    28681 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/codepipeline/pipeline.py
+-rw-r--r--   0 runner    (1001) docker     (121)    31259 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/codepipeline/webhook.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-24 22:23:25.000000 pulumi_aws-5.9.2/pulumi_aws/codestarconnections/
+-rw-r--r--   0 runner    (1001) docker     (121)      390 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/codestarconnections/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     3664 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/codestarconnections/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    22770 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/codestarconnections/connection.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6616 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/codestarconnections/get_connection.py
+-rw-r--r--   0 runner    (1001) docker     (121)    18005 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/codestarconnections/host.py
+-rw-r--r--   0 runner    (1001) docker     (121)     3637 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/codestarconnections/outputs.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-24 22:23:25.000000 pulumi_aws-5.9.2/pulumi_aws/codestarnotifications/
+-rw-r--r--   0 runner    (1001) docker     (121)      347 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/codestarnotifications/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2270 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/codestarnotifications/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    27263 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/codestarnotifications/notification_rule.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1796 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/codestarnotifications/outputs.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-24 22:23:25.000000 pulumi_aws-5.9.2/pulumi_aws/cognito/
+-rw-r--r--   0 runner    (1001) docker     (121)      862 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/cognito/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    66712 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/cognito/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    18725 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/cognito/get_user_pool_client.py
+-rw-r--r--   0 runner    (1001) docker     (121)     4264 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/cognito/get_user_pool_clients.py
+-rw-r--r--   0 runner    (1001) docker     (121)     3933 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/cognito/get_user_pool_signing_certificate.py
+-rw-r--r--   0 runner    (1001) docker     (121)     4695 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/cognito/get_user_pools.py
+-rw-r--r--   0 runner    (1001) docker     (121)    35481 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/cognito/identity_pool.py
+-rw-r--r--   0 runner    (1001) docker     (121)    13593 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/cognito/identity_pool_provider_principal_tag.py
+-rw-r--r--   0 runner    (1001) docker     (121)    17631 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/cognito/identity_pool_role_attachment.py
+-rw-r--r--   0 runner    (1001) docker     (121)    21931 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/cognito/identity_provider.py
+-rw-r--r--   0 runner    (1001) docker     (121)    73184 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/cognito/outputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    14941 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/cognito/resource_server.py
+-rw-r--r--   0 runner    (1001) docker     (121)    53262 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/cognito/user.py
+-rw-r--r--   0 runner    (1001) docker     (121)    15583 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/cognito/user_group.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11574 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/cognito/user_in_group.py
+-rw-r--r--   0 runner    (1001) docker     (121)    90511 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/cognito/user_pool.py
+-rw-r--r--   0 runner    (1001) docker     (121)    73606 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/cognito/user_pool_client.py
+-rw-r--r--   0 runner    (1001) docker     (121)    18109 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/cognito/user_pool_domain.py
+-rw-r--r--   0 runner    (1001) docker     (121)    23695 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/cognito/user_pool_ui_customization.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-24 22:23:25.000000 pulumi_aws-5.9.2/pulumi_aws/config/
+-rw-r--r--   0 runner    (1001) docker     (121)      285 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/config/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)   107985 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/config/outputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)     8173 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/config/vars.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-24 22:23:25.000000 pulumi_aws-5.9.2/pulumi_aws/connect/
+-rw-r--r--   0 runner    (1001) docker     (121)     1116 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/connect/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    54095 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/connect/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    14391 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/connect/bot_association.py
+-rw-r--r--   0 runner    (1001) docker     (121)    30680 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/connect/contact_flow.py
+-rw-r--r--   0 runner    (1001) docker     (121)    30141 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/connect/contact_flow_module.py
+-rw-r--r--   0 runner    (1001) docker     (121)     4555 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/connect/get_bot_association.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7962 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/connect/get_contact_flow.py
+-rw-r--r--   0 runner    (1001) docker     (121)     8686 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/connect/get_contact_flow_module.py
+-rw-r--r--   0 runner    (1001) docker     (121)     9505 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/connect/get_hours_of_operation.py
+-rw-r--r--   0 runner    (1001) docker     (121)    10692 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/connect/get_instance.py
+-rw-r--r--   0 runner    (1001) docker     (121)     4612 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/connect/get_lambda_function_association.py
+-rw-r--r--   0 runner    (1001) docker     (121)     4527 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/connect/get_prompt.py
+-rw-r--r--   0 runner    (1001) docker     (121)     8995 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/connect/get_queue.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7879 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/connect/get_quick_connect.py
+-rw-r--r--   0 runner    (1001) docker     (121)     9368 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/connect/get_routing_profile.py
+-rw-r--r--   0 runner    (1001) docker     (121)     8342 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/connect/get_security_profile.py
+-rw-r--r--   0 runner    (1001) docker     (121)     4156 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/connect/get_user_hierarchy_structure.py
+-rw-r--r--   0 runner    (1001) docker     (121)    27398 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/connect/hours_of_operation.py
+-rw-r--r--   0 runner    (1001) docker     (121)    35574 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/connect/instance.py
+-rw-r--r--   0 runner    (1001) docker     (121)    10774 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/connect/lambda_function_association.py
+-rw-r--r--   0 runner    (1001) docker     (121)    73245 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/connect/outputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    35890 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/connect/queue.py
+-rw-r--r--   0 runner    (1001) docker     (121)    23638 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/connect/quick_connect.py
+-rw-r--r--   0 runner    (1001) docker     (121)    32521 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/connect/routing_profile.py
+-rw-r--r--   0 runner    (1001) docker     (121)    23343 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/connect/security_profile.py
+-rw-r--r--   0 runner    (1001) docker     (121)    24705 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/connect/user_hierarchy_group.py
+-rw-r--r--   0 runner    (1001) docker     (121)    13706 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/connect/user_hierarchy_structure.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-24 22:23:25.000000 pulumi_aws-5.9.2/pulumi_aws/costexplorer/
+-rw-r--r--   0 runner    (1001) docker     (121)      431 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/costexplorer/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    94491 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/costexplorer/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    17207 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/costexplorer/anomaly_monitor.py
+-rw-r--r--   0 runner    (1001) docker     (121)    22774 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/costexplorer/cost_category.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6395 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/costexplorer/get_cost_category.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7096 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/costexplorer/get_tags.py
+-rw-r--r--   0 runner    (1001) docker     (121)   121588 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/costexplorer/outputs.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-24 22:23:25.000000 pulumi_aws-5.9.2/pulumi_aws/cur/
+-rw-r--r--   0 runner    (1001) docker     (121)      339 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/cur/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     9003 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/cur/get_report_definition.py
+-rw-r--r--   0 runner    (1001) docker     (121)    35405 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/cur/report_definition.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-24 22:23:25.000000 pulumi_aws-5.9.2/pulumi_aws/dataexchange/
+-rw-r--r--   0 runner    (1001) docker     (121)      317 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/dataexchange/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    17250 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/dataexchange/data_set.py
+-rw-r--r--   0 runner    (1001) docker     (121)    15878 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/dataexchange/revision.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-24 22:23:25.000000 pulumi_aws-5.9.2/pulumi_aws/datapipeline/
+-rw-r--r--   0 runner    (1001) docker     (121)      440 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/datapipeline/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     8813 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/datapipeline/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)     4521 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/datapipeline/get_pipeline.py
+-rw-r--r--   0 runner    (1001) docker     (121)     5847 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/datapipeline/get_pipeline_definition.py
+-rw-r--r--   0 runner    (1001) docker     (121)    12685 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/datapipeline/outputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    12326 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/datapipeline/pipeline.py
+-rw-r--r--   0 runner    (1001) docker     (121)    21912 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/datapipeline/pipeline_definition.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-24 22:23:25.000000 pulumi_aws-5.9.2/pulumi_aws/datasync/
+-rw-r--r--   0 runner    (1001) docker     (121)      606 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/datasync/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    27590 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/datasync/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    29878 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/datasync/agent.py
+-rw-r--r--   0 runner    (1001) docker     (121)    18956 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/datasync/efs_location.py
+-rw-r--r--   0 runner    (1001) docker     (121)    25463 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/datasync/fsx_open_zfs_file_system.py
+-rw-r--r--   0 runner    (1001) docker     (121)    21841 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/datasync/location_fsx_lustre.py
+-rw-r--r--   0 runner    (1001) docker     (121)    27324 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/datasync/location_fsx_windows.py
+-rw-r--r--   0 runner    (1001) docker     (121)    50555 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/datasync/location_hdfs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    28193 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/datasync/location_smb.py
+-rw-r--r--   0 runner    (1001) docker     (121)    22296 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/datasync/nfs_location.py
+-rw-r--r--   0 runner    (1001) docker     (121)    27796 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/datasync/outputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    23994 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/datasync/s3_location.py
+-rw-r--r--   0 runner    (1001) docker     (121)    29776 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/datasync/task.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-24 22:23:25.000000 pulumi_aws-5.9.2/pulumi_aws/dax/
+-rw-r--r--   0 runner    (1001) docker     (121)      396 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/dax/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     4044 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/dax/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    52164 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/dax/cluster.py
+-rw-r--r--   0 runner    (1001) docker     (121)     3521 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/dax/outputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11273 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/dax/parameter_group.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11347 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/dax/subnet_group.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-24 22:23:25.000000 pulumi_aws-5.9.2/pulumi_aws/detective/
+-rw-r--r--   0 runner    (1001) docker     (121)      347 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/detective/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11407 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/detective/graph.py
+-rw-r--r--   0 runner    (1001) docker     (121)     8382 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/detective/invitation_accepter.py
+-rw-r--r--   0 runner    (1001) docker     (121)    25080 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/detective/member.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-24 22:23:25.000000 pulumi_aws-5.9.2/pulumi_aws/devicefarm/
+-rw-r--r--   0 runner    (1001) docker     (121)      482 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/devicefarm/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     4949 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/devicefarm/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    22351 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/devicefarm/device_pool.py
+-rw-r--r--   0 runner    (1001) docker     (121)    24257 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/devicefarm/instance_profile.py
+-rw-r--r--   0 runner    (1001) docker     (121)    40408 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/devicefarm/network_profile.py
+-rw-r--r--   0 runner    (1001) docker     (121)     4546 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/devicefarm/outputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    15864 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/devicefarm/project.py
+-rw-r--r--   0 runner    (1001) docker     (121)    17914 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/devicefarm/test_grid_project.py
+-rw-r--r--   0 runner    (1001) docker     (121)    20266 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/devicefarm/upload.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-24 22:23:25.000000 pulumi_aws-5.9.2/pulumi_aws/directconnect/
+-rw-r--r--   0 runner    (1001) docker     (121)     1118 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/directconnect/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    21880 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/directconnect/bgp_peer.py
+-rw-r--r--   0 runner    (1001) docker     (121)    25773 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/directconnect/connection.py
+-rw-r--r--   0 runner    (1001) docker     (121)     9173 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/directconnect/connection_association.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6530 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/directconnect/connection_confirmation.py
+-rw-r--r--   0 runner    (1001) docker     (121)    10139 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/directconnect/gateway.py
+-rw-r--r--   0 runner    (1001) docker     (121)    30877 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/directconnect/gateway_association.py
+-rw-r--r--   0 runner    (1001) docker     (121)    21361 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/directconnect/gateway_association_proposal.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6538 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/directconnect/get_connection.py
+-rw-r--r--   0 runner    (1001) docker     (121)     3895 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/directconnect/get_gateway.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6043 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/directconnect/get_location.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2921 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/directconnect/get_locations.py
+-rw-r--r--   0 runner    (1001) docker     (121)    28816 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/directconnect/hosted_connection.py
+-rw-r--r--   0 runner    (1001) docker     (121)    31972 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/directconnect/hosted_private_virtual_interface.py
+-rw-r--r--   0 runner    (1001) docker     (121)    19989 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/directconnect/hosted_private_virtual_interface_accepter.py
+-rw-r--r--   0 runner    (1001) docker     (121)    30888 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/directconnect/hosted_public_virtual_interface.py
+-rw-r--r--   0 runner    (1001) docker     (121)    15370 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/directconnect/hosted_public_virtual_interface_accepter.py
+-rw-r--r--   0 runner    (1001) docker     (121)    32040 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/directconnect/hosted_transit_virtual_interface.py
+-rw-r--r--   0 runner    (1001) docker     (121)    18978 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/directconnect/hosted_transit_virtual_interface_acceptor.py
+-rw-r--r--   0 runner    (1001) docker     (121)    30178 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/directconnect/link_aggregation_group.py
+-rw-r--r--   0 runner    (1001) docker     (121)    39909 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/directconnect/private_virtual_interface.py
+-rw-r--r--   0 runner    (1001) docker     (121)    32590 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/directconnect/public_virtual_interface.py
+-rw-r--r--   0 runner    (1001) docker     (121)    38324 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/directconnect/transit_virtual_interface.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-24 22:23:25.000000 pulumi_aws-5.9.2/pulumi_aws/directoryservice/
+-rw-r--r--   0 runner    (1001) docker     (121)      431 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/directoryservice/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6343 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/directoryservice/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11874 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/directoryservice/conditional_forwader.py
+-rw-r--r--   0 runner    (1001) docker     (121)    42616 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/directoryservice/directory.py
+-rw-r--r--   0 runner    (1001) docker     (121)    10586 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/directoryservice/get_directory.py
+-rw-r--r--   0 runner    (1001) docker     (121)    12830 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/directoryservice/log_service.py
+-rw-r--r--   0 runner    (1001) docker     (121)     9982 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/directoryservice/outputs.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-24 22:23:25.000000 pulumi_aws-5.9.2/pulumi_aws/dlm/
+-rw-r--r--   0 runner    (1001) docker     (121)      346 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/dlm/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    55991 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/dlm/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    29352 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/dlm/lifecycle_policy.py
+-rw-r--r--   0 runner    (1001) docker     (121)    56336 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/dlm/outputs.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-24 22:23:25.000000 pulumi_aws-5.9.2/pulumi_aws/dms/
+-rw-r--r--   0 runner    (1001) docker     (121)      507 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/dms/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    66045 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/dms/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    18471 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/dms/certificate.py
+-rw-r--r--   0 runner    (1001) docker     (121)    68131 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/dms/endpoint.py
+-rw-r--r--   0 runner    (1001) docker     (121)    23673 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/dms/event_subscription.py
+-rw-r--r--   0 runner    (1001) docker     (121)    59960 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/dms/outputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    61278 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/dms/replication_instance.py
+-rw-r--r--   0 runner    (1001) docker     (121)    20305 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/dms/replication_subnet_group.py
+-rw-r--r--   0 runner    (1001) docker     (121)    41962 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/dms/replication_task.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-24 22:23:25.000000 pulumi_aws-5.9.2/pulumi_aws/docdb/
+-rw-r--r--   0 runner    (1001) docker     (121)      607 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/docdb/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     3564 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/docdb/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    82759 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/docdb/cluster.py
+-rw-r--r--   0 runner    (1001) docker     (121)    58376 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/docdb/cluster_instance.py
+-rw-r--r--   0 runner    (1001) docker     (121)    22098 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/docdb/cluster_parameter_group.py
+-rw-r--r--   0 runner    (1001) docker     (121)    22875 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/docdb/cluster_snapshot.py
+-rw-r--r--   0 runner    (1001) docker     (121)    31024 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/docdb/event_subscription.py
+-rw-r--r--   0 runner    (1001) docker     (121)    10215 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/docdb/get_engine_version.py
+-rw-r--r--   0 runner    (1001) docker     (121)     8934 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/docdb/get_orderable_db_instance.py
+-rw-r--r--   0 runner    (1001) docker     (121)    28361 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/docdb/global_cluster.py
+-rw-r--r--   0 runner    (1001) docker     (121)     4028 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/docdb/outputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    19151 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/docdb/subnet_group.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-24 22:23:25.000000 pulumi_aws-5.9.2/pulumi_aws/dynamodb/
+-rw-r--r--   0 runner    (1001) docker     (121)      514 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/dynamodb/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    16777 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/dynamodb/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)     8888 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/dynamodb/contributor_insights.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11987 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/dynamodb/get_table.py
+-rw-r--r--   0 runner    (1001) docker     (121)    14562 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/dynamodb/global_table.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11148 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/dynamodb/kinesis_streaming_destination.py
+-rw-r--r--   0 runner    (1001) docker     (121)    22116 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/dynamodb/outputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    70444 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/dynamodb/table.py
+-rw-r--r--   0 runner    (1001) docker     (121)    15279 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/dynamodb/table_item.py
+-rw-r--r--   0 runner    (1001) docker     (121)     9204 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/dynamodb/tag.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-24 22:23:25.000000 pulumi_aws-5.9.2/pulumi_aws/ebs/
+-rw-r--r--   0 runner    (1001) docker     (121)      681 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ebs/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    10723 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ebs/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)     8377 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ebs/default_kms_key.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7392 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ebs/encryption_by_default.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2633 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ebs/get_default_kms_key.py
+-rw-r--r--   0 runner    (1001) docker     (121)     4463 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ebs/get_ebs_volumes.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2482 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ebs/get_encryption_by_default.py
+-rw-r--r--   0 runner    (1001) docker     (121)    14728 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ebs/get_snapshot.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6470 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ebs/get_snapshot_ids.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11339 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ebs/get_volume.py
+-rw-r--r--   0 runner    (1001) docker     (121)    10320 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ebs/outputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    31525 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ebs/snapshot.py
+-rw-r--r--   0 runner    (1001) docker     (121)    33170 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ebs/snapshot_copy.py
+-rw-r--r--   0 runner    (1001) docker     (121)    39908 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ebs/snapshot_import.py
+-rw-r--r--   0 runner    (1001) docker     (121)    33092 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ebs/volume.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-24 22:23:25.000000 pulumi_aws-5.9.2/pulumi_aws/ec2/
+-rw-r--r--   0 runner    (1001) docker     (121)     5396 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ec2/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    14508 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ec2/_enums.py
+-rw-r--r--   0 runner    (1001) docker     (121)   485832 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ec2/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    64164 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ec2/ami.py
+-rw-r--r--   0 runner    (1001) docker     (121)    62901 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ec2/ami_copy.py
+-rw-r--r--   0 runner    (1001) docker     (121)    55704 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ec2/ami_from_instance.py
+-rw-r--r--   0 runner    (1001) docker     (121)    16444 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ec2/ami_launch_permission.py
+-rw-r--r--   0 runner    (1001) docker     (121)     9831 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ec2/availability_zone_group.py
+-rw-r--r--   0 runner    (1001) docker     (121)    40792 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ec2/capacity_reservation.py
+-rw-r--r--   0 runner    (1001) docker     (121)    13591 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ec2/carrier_gateway.py
+-rw-r--r--   0 runner    (1001) docker     (121)    21044 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ec2/customer_gateway.py
+-rw-r--r--   0 runner    (1001) docker     (121)    27168 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ec2/dedicated_host.py
+-rw-r--r--   0 runner    (1001) docker     (121)    34225 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ec2/default_network_acl.py
+-rw-r--r--   0 runner    (1001) docker     (121)    24139 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ec2/default_route_table.py
+-rw-r--r--   0 runner    (1001) docker     (121)    28652 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ec2/default_security_group.py
+-rw-r--r--   0 runner    (1001) docker     (121)    40214 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ec2/default_subnet.py
+-rw-r--r--   0 runner    (1001) docker     (121)    34748 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ec2/default_vpc.py
+-rw-r--r--   0 runner    (1001) docker     (121)    20289 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ec2/default_vpc_dhcp_options.py
+-rw-r--r--   0 runner    (1001) docker     (121)    12312 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ec2/egress_only_internet_gateway.py
+-rw-r--r--   0 runner    (1001) docker     (121)    44648 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ec2/eip.py
+-rw-r--r--   0 runner    (1001) docker     (121)    23192 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ec2/eip_association.py
+-rw-r--r--   0 runner    (1001) docker     (121)    39855 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ec2/fleet.py
+-rw-r--r--   0 runner    (1001) docker     (121)    40861 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ec2/flow_log.py
+-rw-r--r--   0 runner    (1001) docker     (121)    25840 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ec2/get_ami.py
+-rw-r--r--   0 runner    (1001) docker     (121)     8332 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ec2/get_ami_ids.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6998 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ec2/get_coip_pool.py
+-rw-r--r--   0 runner    (1001) docker     (121)     4226 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ec2/get_coip_pools.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7907 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ec2/get_customer_gateway.py
+-rw-r--r--   0 runner    (1001) docker     (121)     9845 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ec2/get_dedicated_host.py
+-rw-r--r--   0 runner    (1001) docker     (121)     5265 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ec2/get_eips.py
+-rw-r--r--   0 runner    (1001) docker     (121)    13917 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ec2/get_elastic_ip.py
+-rw-r--r--   0 runner    (1001) docker     (121)    31213 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ec2/get_instance.py
+-rw-r--r--   0 runner    (1001) docker     (121)    41419 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ec2/get_instance_type.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7250 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ec2/get_instance_type_offering.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7163 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ec2/get_instance_type_offerings.py
+-rw-r--r--   0 runner    (1001) docker     (121)     5327 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ec2/get_instance_types.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7741 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ec2/get_instances.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6779 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ec2/get_internet_gateway.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6008 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ec2/get_ipam_preview_next_cidr.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6750 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ec2/get_key_pair.py
+-rw-r--r--   0 runner    (1001) docker     (121)    13646 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ec2/get_launch_configuration.py
+-rw-r--r--   0 runner    (1001) docker     (121)    24338 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ec2/get_launch_template.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6394 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ec2/get_local_gateway.py
+-rw-r--r--   0 runner    (1001) docker     (121)     8593 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ec2/get_local_gateway_route_table.py
+-rw-r--r--   0 runner    (1001) docker     (121)     4582 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ec2/get_local_gateway_route_tables.py
+-rw-r--r--   0 runner    (1001) docker     (121)     9586 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ec2/get_local_gateway_virtual_interface.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7551 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ec2/get_local_gateway_virtual_interface_group.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6784 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ec2/get_local_gateway_virtual_interface_groups.py
+-rw-r--r--   0 runner    (1001) docker     (121)     4938 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ec2/get_local_gateways.py
+-rw-r--r--   0 runner    (1001) docker     (121)     9326 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ec2/get_managed_prefix_list.py
+-rw-r--r--   0 runner    (1001) docker     (121)     9672 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ec2/get_nat_gateway.py
+-rw-r--r--   0 runner    (1001) docker     (121)     4879 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ec2/get_nat_gateways.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6677 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ec2/get_network_acls.py
+-rw-r--r--   0 runner    (1001) docker     (121)    13414 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ec2/get_network_interface.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6274 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ec2/get_network_interfaces.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7111 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ec2/get_prefix_list.py
+-rw-r--r--   0 runner    (1001) docker     (121)    16232 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ec2/get_route.py
+-rw-r--r--   0 runner    (1001) docker     (121)    10450 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ec2/get_route_table.py
+-rw-r--r--   0 runner    (1001) docker     (121)     4879 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ec2/get_route_tables.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7898 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ec2/get_security_group.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6644 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ec2/get_security_groups.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2480 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ec2/get_serial_console_access.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6843 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ec2/get_spot_price.py
+-rw-r--r--   0 runner    (1001) docker     (121)    21289 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ec2/get_subnet.py
+-rw-r--r--   0 runner    (1001) docker     (121)     5231 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ec2/get_subnet_ids.py
+-rw-r--r--   0 runner    (1001) docker     (121)     4016 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ec2/get_subnets.py
+-rw-r--r--   0 runner    (1001) docker     (121)     5333 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ec2/get_transit_gateway_route_tables.py
+-rw-r--r--   0 runner    (1001) docker     (121)    12158 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ec2/get_vpc.py
+-rw-r--r--   0 runner    (1001) docker     (121)     9664 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ec2/get_vpc_dhcp_options.py
+-rw-r--r--   0 runner    (1001) docker     (121)    14931 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ec2/get_vpc_endpoint.py
+-rw-r--r--   0 runner    (1001) docker     (121)    14017 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ec2/get_vpc_endpoint_service.py
+-rw-r--r--   0 runner    (1001) docker     (121)    16194 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ec2/get_vpc_iam_pool.py
+-rw-r--r--   0 runner    (1001) docker     (121)    15402 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ec2/get_vpc_peering_connection.py
+-rw-r--r--   0 runner    (1001) docker     (121)     4640 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ec2/get_vpc_peering_connections.py
+-rw-r--r--   0 runner    (1001) docker     (121)     4184 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ec2/get_vpcs.py
+-rw-r--r--   0 runner    (1001) docker     (121)     8164 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ec2/get_vpn_gateway.py
+-rw-r--r--   0 runner    (1001) docker     (121)   162185 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ec2/instance.py
+-rw-r--r--   0 runner    (1001) docker     (121)    13689 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ec2/internet_gateway.py
+-rw-r--r--   0 runner    (1001) docker     (121)     9373 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ec2/internet_gateway_attachment.py
+-rw-r--r--   0 runner    (1001) docker     (121)    19260 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ec2/key_pair.py
+-rw-r--r--   0 runner    (1001) docker     (121)    74869 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ec2/launch_configuration.py
+-rw-r--r--   0 runner    (1001) docker     (121)   117094 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ec2/launch_template.py
+-rw-r--r--   0 runner    (1001) docker     (121)    14218 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ec2/local_gateway_route.py
+-rw-r--r--   0 runner    (1001) docker     (121)    16237 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ec2/local_gateway_route_table_vpc_association.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11787 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ec2/main_route_table_association.py
+-rw-r--r--   0 runner    (1001) docker     (121)    22037 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ec2/managed_prefix_list.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11558 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ec2/managed_prefix_list_entry.py
+-rw-r--r--   0 runner    (1001) docker     (121)    20590 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ec2/nat_gateway.py
+-rw-r--r--   0 runner    (1001) docker     (121)    20000 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ec2/network_acl.py
+-rw-r--r--   0 runner    (1001) docker     (121)     8238 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ec2/network_acl_association.py
+-rw-r--r--   0 runner    (1001) docker     (121)    30623 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ec2/network_acl_rule.py
+-rw-r--r--   0 runner    (1001) docker     (121)    25229 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ec2/network_insights_path.py
+-rw-r--r--   0 runner    (1001) docker     (121)    67113 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ec2/network_interface.py
+-rw-r--r--   0 runner    (1001) docker     (121)    12783 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ec2/network_interface_attachment.py
+-rw-r--r--   0 runner    (1001) docker     (121)    13825 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ec2/network_interface_security_group_attachment.py
+-rw-r--r--   0 runner    (1001) docker     (121)   524457 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ec2/outputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    23207 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ec2/peering_connection_options.py
+-rw-r--r--   0 runner    (1001) docker     (121)    18601 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ec2/placement_group.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11038 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ec2/proxy_protocol_policy.py
+-rw-r--r--   0 runner    (1001) docker     (121)    44522 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ec2/route.py
+-rw-r--r--   0 runner    (1001) docker     (121)    21153 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ec2/route_table.py
+-rw-r--r--   0 runner    (1001) docker     (121)    13230 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ec2/route_table_association.py
+-rw-r--r--   0 runner    (1001) docker     (121)    28775 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ec2/security_group.py
+-rw-r--r--   0 runner    (1001) docker     (121)    13480 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ec2/security_group_association.py
+-rw-r--r--   0 runner    (1001) docker     (121)    41534 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ec2/security_group_rule.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6803 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ec2/serial_console_access.py
+-rw-r--r--   0 runner    (1001) docker     (121)     9250 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ec2/snapshot_create_volume_permission.py
+-rw-r--r--   0 runner    (1001) docker     (121)     9683 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ec2/spot_datafeed_subscription.py
+-rw-r--r--   0 runner    (1001) docker     (121)    85616 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ec2/spot_fleet_request.py
+-rw-r--r--   0 runner    (1001) docker     (121)   186619 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ec2/spot_instance_request.py
+-rw-r--r--   0 runner    (1001) docker     (121)    58037 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ec2/subnet.py
+-rw-r--r--   0 runner    (1001) docker     (121)    14346 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ec2/subnet_cidr_reservation.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11979 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ec2/tag.py
+-rw-r--r--   0 runner    (1001) docker     (121)    15303 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ec2/traffic_mirror_filter.py
+-rw-r--r--   0 runner    (1001) docker     (121)    36168 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ec2/traffic_mirror_filter_rule.py
+-rw-r--r--   0 runner    (1001) docker     (121)    32594 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ec2/traffic_mirror_session.py
+-rw-r--r--   0 runner    (1001) docker     (121)    19328 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ec2/traffic_mirror_target.py
+-rw-r--r--   0 runner    (1001) docker     (121)    17933 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ec2/transit_gateway_peering_attachment_accepter.py
+-rw-r--r--   0 runner    (1001) docker     (121)    27015 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ec2/volume_attachment.py
+-rw-r--r--   0 runner    (1001) docker     (121)    64450 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ec2/vpc.py
+-rw-r--r--   0 runner    (1001) docker     (121)    27900 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ec2/vpc_dhcp_options.py
+-rw-r--r--   0 runner    (1001) docker     (121)     9814 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ec2/vpc_dhcp_options_association.py
+-rw-r--r--   0 runner    (1001) docker     (121)    49787 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ec2/vpc_endpoint.py
+-rw-r--r--   0 runner    (1001) docker     (121)    12473 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ec2/vpc_endpoint_connection_accepter.py
+-rw-r--r--   0 runner    (1001) docker     (121)    20311 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ec2/vpc_endpoint_connection_notification.py
+-rw-r--r--   0 runner    (1001) docker     (121)     9465 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ec2/vpc_endpoint_policy.py
+-rw-r--r--   0 runner    (1001) docker     (121)    10129 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ec2/vpc_endpoint_route_table_association.py
+-rw-r--r--   0 runner    (1001) docker     (121)    36282 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ec2/vpc_endpoint_service.py
+-rw-r--r--   0 runner    (1001) docker     (121)    10601 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ec2/vpc_endpoint_service_allowed_principle.py
+-rw-r--r--   0 runner    (1001) docker     (121)    10739 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ec2/vpc_endpoint_subnet_association.py
+-rw-r--r--   0 runner    (1001) docker     (121)    26151 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ec2/vpc_ipam.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11193 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ec2/vpc_ipam_organization_admin_account.py
+-rw-r--r--   0 runner    (1001) docker     (121)    51149 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ec2/vpc_ipam_pool.py
+-rw-r--r--   0 runner    (1001) docker     (121)    14635 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ec2/vpc_ipam_pool_cidr.py
+-rw-r--r--   0 runner    (1001) docker     (121)    23522 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ec2/vpc_ipam_pool_cidr_allocation.py
+-rw-r--r--   0 runner    (1001) docker     (121)    14034 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ec2/vpc_ipam_preview_next_cidr.py
+-rw-r--r--   0 runner    (1001) docker     (121)    15979 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ec2/vpc_ipam_scope.py
+-rw-r--r--   0 runner    (1001) docker     (121)    17049 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ec2/vpc_ipv4_cidr_block_association.py
+-rw-r--r--   0 runner    (1001) docker     (121)    18439 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ec2/vpc_ipv6_cidr_block_association.py
+-rw-r--r--   0 runner    (1001) docker     (121)    36834 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ec2/vpc_peering_connection.py
+-rw-r--r--   0 runner    (1001) docker     (121)    31202 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ec2/vpc_peering_connection_accepter.py
+-rw-r--r--   0 runner    (1001) docker     (121)   193564 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ec2/vpn_connection.py
+-rw-r--r--   0 runner    (1001) docker     (121)    10200 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ec2/vpn_connection_route.py
+-rw-r--r--   0 runner    (1001) docker     (121)    16954 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ec2/vpn_gateway.py
+-rw-r--r--   0 runner    (1001) docker     (121)     9783 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ec2/vpn_gateway_attachment.py
+-rw-r--r--   0 runner    (1001) docker     (121)     9584 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ec2/vpn_gateway_route_propagation.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-24 22:23:25.000000 pulumi_aws-5.9.2/pulumi_aws/ec2clientvpn/
+-rw-r--r--   0 runner    (1001) docker     (121)      456 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ec2clientvpn/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11882 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ec2clientvpn/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    18600 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ec2clientvpn/authorization_rule.py
+-rw-r--r--   0 runner    (1001) docker     (121)    59719 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ec2clientvpn/endpoint.py
+-rw-r--r--   0 runner    (1001) docker     (121)    15781 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ec2clientvpn/get_endpoint.py
+-rw-r--r--   0 runner    (1001) docker     (121)    18214 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ec2clientvpn/network_association.py
+-rw-r--r--   0 runner    (1001) docker     (121)    15851 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ec2clientvpn/outputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    18589 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ec2clientvpn/route.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-24 22:23:25.000000 pulumi_aws-5.9.2/pulumi_aws/ec2transitgateway/
+-rw-r--r--   0 runner    (1001) docker     (121)     1169 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ec2transitgateway/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    12766 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ec2transitgateway/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    22115 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ec2transitgateway/connect.py
+-rw-r--r--   0 runner    (1001) docker     (121)    27657 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ec2transitgateway/connect_peer.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7383 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ec2transitgateway/get_connect.py
+-rw-r--r--   0 runner    (1001) docker     (121)     9445 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ec2transitgateway/get_connect_peer.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6964 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ec2transitgateway/get_direct_connect_gateway_attachment.py
+-rw-r--r--   0 runner    (1001) docker     (121)    12563 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ec2transitgateway/get_multicast_domain.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7617 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ec2transitgateway/get_peering_attachment.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7943 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ec2transitgateway/get_route_table.py
+-rw-r--r--   0 runner    (1001) docker     (121)    13346 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ec2transitgateway/get_transit_gateway.py
+-rw-r--r--   0 runner    (1001) docker     (121)     8756 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ec2transitgateway/get_vpc_attachment.py
+-rw-r--r--   0 runner    (1001) docker     (121)     3474 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ec2transitgateway/get_vpc_attachments.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7599 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ec2transitgateway/get_vpn_attachment.py
+-rw-r--r--   0 runner    (1001) docker     (121)    29489 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ec2transitgateway/multicast_domain.py
+-rw-r--r--   0 runner    (1001) docker     (121)    13789 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ec2transitgateway/multicast_domain_association.py
+-rw-r--r--   0 runner    (1001) docker     (121)    12916 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ec2transitgateway/multicast_group_member.py
+-rw-r--r--   0 runner    (1001) docker     (121)    12914 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ec2transitgateway/multicast_group_source.py
+-rw-r--r--   0 runner    (1001) docker     (121)    14099 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ec2transitgateway/outputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    21127 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ec2transitgateway/peering_attachment.py
+-rw-r--r--   0 runner    (1001) docker     (121)    16886 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ec2transitgateway/prefix_list_reference.py
+-rw-r--r--   0 runner    (1001) docker     (121)    16400 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ec2transitgateway/route.py
+-rw-r--r--   0 runner    (1001) docker     (121)    16011 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ec2transitgateway/route_table.py
+-rw-r--r--   0 runner    (1001) docker     (121)    12945 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ec2transitgateway/route_table_association.py
+-rw-r--r--   0 runner    (1001) docker     (121)    12945 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ec2transitgateway/route_table_propagation.py
+-rw-r--r--   0 runner    (1001) docker     (121)    39889 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ec2transitgateway/transit_gateway.py
+-rw-r--r--   0 runner    (1001) docker     (121)    35038 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ec2transitgateway/vpc_attachment.py
+-rw-r--r--   0 runner    (1001) docker     (121)    29990 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ec2transitgateway/vpc_attachment_accepter.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-24 22:23:25.000000 pulumi_aws-5.9.2/pulumi_aws/ecr/
+-rw-r--r--   0 runner    (1001) docker     (121)      688 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ecr/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    12225 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ecr/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6167 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ecr/get_authorization_token.py
+-rw-r--r--   0 runner    (1001) docker     (121)     4007 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ecr/get_credentials.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7330 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ecr/get_image.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7741 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ecr/get_repository.py
+-rw-r--r--   0 runner    (1001) docker     (121)    14626 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ecr/lifecycle_policy.py
+-rw-r--r--   0 runner    (1001) docker     (121)    15912 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ecr/outputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11728 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ecr/pull_through_cache_rule.py
+-rw-r--r--   0 runner    (1001) docker     (121)     8319 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ecr/registry_policy.py
+-rw-r--r--   0 runner    (1001) docker     (121)    14747 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ecr/registry_scanning_configuration.py
+-rw-r--r--   0 runner    (1001) docker     (121)    14750 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ecr/replication_configuration.py
+-rw-r--r--   0 runner    (1001) docker     (121)    25545 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ecr/repository.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11909 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ecr/repository_policy.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-24 22:23:25.000000 pulumi_aws-5.9.2/pulumi_aws/ecrpublic/
+-rw-r--r--   0 runner    (1001) docker     (121)      412 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ecrpublic/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6431 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ecrpublic/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)     4193 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ecrpublic/get_authorization_token.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6014 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ecrpublic/outputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    15133 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ecrpublic/repository.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11956 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ecrpublic/repository_policy.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-24 22:23:25.000000 pulumi_aws-5.9.2/pulumi_aws/ecs/
+-rw-r--r--   0 runner    (1001) docker     (121)      677 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ecs/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    81094 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ecs/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11564 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ecs/account_setting_default.py
+-rw-r--r--   0 runner    (1001) docker     (121)    17651 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ecs/capacity_provider.py
+-rw-r--r--   0 runner    (1001) docker     (121)    31717 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ecs/cluster.py
+-rw-r--r--   0 runner    (1001) docker     (121)    15308 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ecs/cluster_capacity_providers.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6418 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ecs/get_cluster.py
+-rw-r--r--   0 runner    (1001) docker     (121)     8437 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ecs/get_container_definition.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6402 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ecs/get_service.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7717 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ecs/get_task_definition.py
+-rw-r--r--   0 runner    (1001) docker     (121)    82647 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ecs/outputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    97431 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ecs/service.py
+-rw-r--r--   0 runner    (1001) docker     (121)    10166 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ecs/tag.py
+-rw-r--r--   0 runner    (1001) docker     (121)    73875 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ecs/task_definition.py
+-rw-r--r--   0 runner    (1001) docker     (121)    52215 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ecs/task_set.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-24 22:23:25.000000 pulumi_aws-5.9.2/pulumi_aws/efs/
+-rw-r--r--   0 runner    (1001) docker     (121)      629 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/efs/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    14847 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/efs/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    19177 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/efs/access_point.py
+-rw-r--r--   0 runner    (1001) docker     (121)     9667 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/efs/backup_policy.py
+-rw-r--r--   0 runner    (1001) docker     (121)    43096 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/efs/file_system.py
+-rw-r--r--   0 runner    (1001) docker     (121)    17642 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/efs/file_system_policy.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6976 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/efs/get_access_point.py
+-rw-r--r--   0 runner    (1001) docker     (121)     3906 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/efs/get_access_points.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11576 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/efs/get_file_system.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11574 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/efs/get_mount_target.py
+-rw-r--r--   0 runner    (1001) docker     (121)    24345 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/efs/mount_target.py
+-rw-r--r--   0 runner    (1001) docker     (121)    19891 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/efs/outputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    20087 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/efs/replication_configuration.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-24 22:23:25.000000 pulumi_aws-5.9.2/pulumi_aws/eks/
+-rw-r--r--   0 runner    (1001) docker     (121)      661 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/eks/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    34939 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/eks/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    33822 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/eks/addon.py
+-rw-r--r--   0 runner    (1001) docker     (121)    55482 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/eks/cluster.py
+-rw-r--r--   0 runner    (1001) docker     (121)    28355 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/eks/fargate_profile.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7734 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/eks/get_addon.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6951 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/eks/get_addon_version.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11213 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/eks/get_cluster.py
+-rw-r--r--   0 runner    (1001) docker     (121)     3636 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/eks/get_cluster_auth.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2025 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/eks/get_clusters.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11788 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/eks/get_node_group.py
+-rw-r--r--   0 runner    (1001) docker     (121)     3279 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/eks/get_node_groups.py
+-rw-r--r--   0 runner    (1001) docker     (121)    17040 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/eks/identity_provider_config.py
+-rw-r--r--   0 runner    (1001) docker     (121)    69935 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/eks/node_group.py
+-rw-r--r--   0 runner    (1001) docker     (121)    44776 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/eks/outputs.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-24 22:23:25.000000 pulumi_aws-5.9.2/pulumi_aws/elasticache/
+-rw-r--r--   0 runner    (1001) docker     (121)      671 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/elasticache/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    12018 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/elasticache/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)   112528 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/elasticache/cluster.py
+-rw-r--r--   0 runner    (1001) docker     (121)    15694 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/elasticache/get_cluster.py
+-rw-r--r--   0 runner    (1001) docker     (121)    15989 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/elasticache/get_replication_group.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6501 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/elasticache/get_user.py
+-rw-r--r--   0 runner    (1001) docker     (121)    38782 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/elasticache/global_replication_group.py
+-rw-r--r--   0 runner    (1001) docker     (121)    15077 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/elasticache/outputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    20087 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/elasticache/parameter_group.py
+-rw-r--r--   0 runner    (1001) docker     (121)   161194 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/elasticache/replication_group.py
+-rw-r--r--   0 runner    (1001) docker     (121)    12834 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/elasticache/security_group.py
+-rw-r--r--   0 runner    (1001) docker     (121)    17414 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/elasticache/subnet_group.py
+-rw-r--r--   0 runner    (1001) docker     (121)    22887 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/elasticache/user.py
+-rw-r--r--   0 runner    (1001) docker     (121)    14799 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/elasticache/user_group.py
+-rw-r--r--   0 runner    (1001) docker     (121)    10755 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/elasticache/user_group_association.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-24 22:23:25.000000 pulumi_aws-5.9.2/pulumi_aws/elasticbeanstalk/
+-rw-r--r--   0 runner    (1001) docker     (121)      537 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/elasticbeanstalk/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     8858 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/elasticbeanstalk/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    17319 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/elasticbeanstalk/application.py
+-rw-r--r--   0 runner    (1001) docker     (121)    24340 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/elasticbeanstalk/application_version.py
+-rw-r--r--   0 runner    (1001) docker     (121)    20869 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/elasticbeanstalk/configuration_template.py
+-rw-r--r--   0 runner    (1001) docker     (121)    58767 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/elasticbeanstalk/environment.py
+-rw-r--r--   0 runner    (1001) docker     (121)     4551 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/elasticbeanstalk/get_application.py
+-rw-r--r--   0 runner    (1001) docker     (121)     3240 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/elasticbeanstalk/get_hosted_zone.py
+-rw-r--r--   0 runner    (1001) docker     (121)     4870 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/elasticbeanstalk/get_solution_stack.py
+-rw-r--r--   0 runner    (1001) docker     (121)     9333 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/elasticbeanstalk/outputs.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-24 22:23:25.000000 pulumi_aws-5.9.2/pulumi_aws/elasticloadbalancing/
+-rw-r--r--   0 runner    (1001) docker     (121)      725 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/elasticloadbalancing/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11561 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/elasticloadbalancing/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    15205 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/elasticloadbalancing/app_cookie_stickiness_policy.py
+-rw-r--r--   0 runner    (1001) docker     (121)     9299 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/elasticloadbalancing/attachment.py
+-rw-r--r--   0 runner    (1001) docker     (121)     4405 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/elasticloadbalancing/get_hosted_zone_id.py
+-rw-r--r--   0 runner    (1001) docker     (121)    13304 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/elasticloadbalancing/get_load_balancer.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6550 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/elasticloadbalancing/get_service_account.py
+-rw-r--r--   0 runner    (1001) docker     (121)    17158 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/elasticloadbalancing/listener_policy.py
+-rw-r--r--   0 runner    (1001) docker     (121)    58963 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/elasticloadbalancing/load_balancer.py
+-rw-r--r--   0 runner    (1001) docker     (121)    15097 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/elasticloadbalancing/load_balancer_backend_server_policy.py
+-rw-r--r--   0 runner    (1001) docker     (121)    15403 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/elasticloadbalancing/load_balancer_cookie_stickiness_policy.py
+-rw-r--r--   0 runner    (1001) docker     (121)    19958 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/elasticloadbalancing/load_balancer_policy.py
+-rw-r--r--   0 runner    (1001) docker     (121)    14246 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/elasticloadbalancing/outputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    17551 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/elasticloadbalancing/ssl_negotiation_policy.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-24 22:23:25.000000 pulumi_aws-5.9.2/pulumi_aws/elasticloadbalancingv2/
+-rw-r--r--   0 runner    (1001) docker     (121)      592 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/elasticloadbalancingv2/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    98570 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/elasticloadbalancingv2/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)     8599 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/elasticloadbalancingv2/get_listener.py
+-rw-r--r--   0 runner    (1001) docker     (121)    14306 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/elasticloadbalancingv2/get_load_balancer.py
+-rw-r--r--   0 runner    (1001) docker     (121)    12878 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/elasticloadbalancingv2/get_target_group.py
+-rw-r--r--   0 runner    (1001) docker     (121)    40835 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/elasticloadbalancingv2/listener.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11225 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/elasticloadbalancingv2/listener_certificate.py
+-rw-r--r--   0 runner    (1001) docker     (121)    34767 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/elasticloadbalancingv2/listener_rule.py
+-rw-r--r--   0 runner    (1001) docker     (121)    69469 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/elasticloadbalancingv2/load_balancer.py
+-rw-r--r--   0 runner    (1001) docker     (121)   107979 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/elasticloadbalancingv2/outputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    61894 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/elasticloadbalancingv2/target_group.py
+-rw-r--r--   0 runner    (1001) docker     (121)    18326 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/elasticloadbalancingv2/target_group_attachment.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-24 22:23:25.000000 pulumi_aws-5.9.2/pulumi_aws/elasticsearch/
+-rw-r--r--   0 runner    (1001) docker     (121)      426 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/elasticsearch/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    49044 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/elasticsearch/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    67348 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/elasticsearch/domain.py
+-rw-r--r--   0 runner    (1001) docker     (121)     9618 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/elasticsearch/domain_policy.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11167 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/elasticsearch/domain_saml_options.py
+-rw-r--r--   0 runner    (1001) docker     (121)    15177 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/elasticsearch/get_domain.py
+-rw-r--r--   0 runner    (1001) docker     (121)    70268 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/elasticsearch/outputs.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-24 22:23:25.000000 pulumi_aws-5.9.2/pulumi_aws/elastictranscoder/
+-rw-r--r--   0 runner    (1001) docker     (121)      360 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/elastictranscoder/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    46964 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/elastictranscoder/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    44339 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/elastictranscoder/outputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    34802 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/elastictranscoder/pipeline.py
+-rw-r--r--   0 runner    (1001) docker     (121)    31433 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/elastictranscoder/preset.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-24 22:23:25.000000 pulumi_aws-5.9.2/pulumi_aws/elb/
+-rw-r--r--   0 runner    (1001) docker     (121)      725 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/elb/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11561 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/elb/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    14858 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/elb/app_cookie_stickiness_policy.py
+-rw-r--r--   0 runner    (1001) docker     (121)     9061 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/elb/attachment.py
+-rw-r--r--   0 runner    (1001) docker     (121)     3933 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/elb/get_hosted_zone_id.py
+-rw-r--r--   0 runner    (1001) docker     (121)    12834 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/elb/get_load_balancer.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6064 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/elb/get_service_account.py
+-rw-r--r--   0 runner    (1001) docker     (121)    16900 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/elb/listener_policy.py
+-rw-r--r--   0 runner    (1001) docker     (121)    58681 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/elb/load_balancer.py
+-rw-r--r--   0 runner    (1001) docker     (121)    14754 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/elb/load_balancer_backend_server_policy.py
+-rw-r--r--   0 runner    (1001) docker     (121)    15045 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/elb/load_balancer_cookie_stickiness_policy.py
+-rw-r--r--   0 runner    (1001) docker     (121)    19680 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/elb/load_balancer_policy.py
+-rw-r--r--   0 runner    (1001) docker     (121)    14246 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/elb/outputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    17263 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/elb/ssl_negotiation_policy.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-24 22:23:25.000000 pulumi_aws-5.9.2/pulumi_aws/emr/
+-rw-r--r--   0 runner    (1001) docker     (121)      567 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/emr/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)   120467 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/emr/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)   139613 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/emr/cluster.py
+-rw-r--r--   0 runner    (1001) docker     (121)     4263 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/emr/get_release_labels.py
+-rw-r--r--   0 runner    (1001) docker     (121)    26544 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/emr/instance_fleet.py
+-rw-r--r--   0 runner    (1001) docker     (121)    31747 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/emr/instance_group.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11997 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/emr/managed_scaling_policy.py
+-rw-r--r--   0 runner    (1001) docker     (121)   117475 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/emr/outputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    13294 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/emr/security_configuration.py
+-rw-r--r--   0 runner    (1001) docker     (121)    46815 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/emr/studio.py
+-rw-r--r--   0 runner    (1001) docker     (121)    17790 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/emr/studio_session_mapping.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-24 22:23:25.000000 pulumi_aws-5.9.2/pulumi_aws/emrcontainers/
+-rw-r--r--   0 runner    (1001) docker     (121)      380 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/emrcontainers/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     3959 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/emrcontainers/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6692 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/emrcontainers/get_virtual_cluster.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6653 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/emrcontainers/outputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    16529 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/emrcontainers/virtual_cluster.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-24 22:23:25.000000 pulumi_aws-5.9.2/pulumi_aws/emrserverless/
+-rw-r--r--   0 runner    (1001) docker     (121)      341 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/emrserverless/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    12136 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/emrserverless/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    35959 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/emrserverless/application.py
+-rw-r--r--   0 runner    (1001) docker     (121)    12110 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/emrserverless/outputs.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-24 22:23:25.000000 pulumi_aws-5.9.2/pulumi_aws/fms/
+-rw-r--r--   0 runner    (1001) docker     (121)      365 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/fms/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6841 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/fms/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)     8209 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/fms/admin_account.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6182 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/fms/outputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    49126 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/fms/policy.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-24 22:23:25.000000 pulumi_aws-5.9.2/pulumi_aws/fsx/
+-rw-r--r--   0 runner    (1001) docker     (121)      654 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/fsx/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    62704 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/fsx/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    22592 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/fsx/backup.py
+-rw-r--r--   0 runner    (1001) docker     (121)    44515 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/fsx/data_repository_association.py
+-rw-r--r--   0 runner    (1001) docker     (121)    91132 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/fsx/lustre_file_system.py
+-rw-r--r--   0 runner    (1001) docker     (121)    64803 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/fsx/ontap_file_system.py
+-rw-r--r--   0 runner    (1001) docker     (121)    33198 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/fsx/ontap_storage_virtual_machine.py
+-rw-r--r--   0 runner    (1001) docker     (121)    38726 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/fsx/ontap_volume.py
+-rw-r--r--   0 runner    (1001) docker     (121)    62962 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/fsx/open_zfs_file_system.py
+-rw-r--r--   0 runner    (1001) docker     (121)    19792 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/fsx/open_zfs_snapshot.py
+-rw-r--r--   0 runner    (1001) docker     (121)    42163 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/fsx/open_zfs_volume.py
+-rw-r--r--   0 runner    (1001) docker     (121)    62498 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/fsx/outputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    79805 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/fsx/windows_file_system.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-24 22:23:25.000000 pulumi_aws-5.9.2/pulumi_aws/gamelift/
+-rw-r--r--   0 runner    (1001) docker     (121)      466 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/gamelift/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    27119 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/gamelift/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    16014 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/gamelift/alias.py
+-rw-r--r--   0 runner    (1001) docker     (121)    19161 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/gamelift/build.py
+-rw-r--r--   0 runner    (1001) docker     (121)    48875 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/gamelift/fleet.py
+-rw-r--r--   0 runner    (1001) docker     (121)    45981 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/gamelift/game_server_group.py
+-rw-r--r--   0 runner    (1001) docker     (121)    21149 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/gamelift/game_session_queue.py
+-rw-r--r--   0 runner    (1001) docker     (121)    29239 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/gamelift/outputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    20014 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/gamelift/script.py
+-rw-r--r--   0 runner    (1001) docker     (121)    26157 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/get_ami.py
+-rw-r--r--   0 runner    (1001) docker     (121)     8675 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/get_ami_ids.py
+-rw-r--r--   0 runner    (1001) docker     (121)     5435 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/get_arn.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6688 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/get_autoscaling_groups.py
+-rw-r--r--   0 runner    (1001) docker     (121)    12721 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/get_availability_zone.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11772 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/get_availability_zones.py
+-rw-r--r--   0 runner    (1001) docker     (121)     3531 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/get_billing_service_account.py
+-rw-r--r--   0 runner    (1001) docker     (121)     3442 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/get_caller_identity.py
+-rw-r--r--   0 runner    (1001) docker     (121)     3337 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/get_canonical_user_id.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2968 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/get_default_tags.py
+-rw-r--r--   0 runner    (1001) docker     (121)    14284 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/get_elastic_ip.py
+-rw-r--r--   0 runner    (1001) docker     (121)     9281 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/get_ip_ranges.py
+-rw-r--r--   0 runner    (1001) docker     (121)     3768 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/get_partition.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7486 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/get_prefix_list.py
+-rw-r--r--   0 runner    (1001) docker     (121)     4841 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/get_region.py
+-rw-r--r--   0 runner    (1001) docker     (121)     5942 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/get_regions.py
+-rw-r--r--   0 runner    (1001) docker     (121)     8510 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/get_service.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-24 22:23:25.000000 pulumi_aws-5.9.2/pulumi_aws/glacier/
+-rw-r--r--   0 runner    (1001) docker     (121)      361 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/glacier/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1698 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/glacier/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1885 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/glacier/outputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    21662 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/glacier/vault.py
+-rw-r--r--   0 runner    (1001) docker     (121)    22404 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/glacier/vault_lock.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-24 22:23:25.000000 pulumi_aws-5.9.2/pulumi_aws/globalaccelerator/
+-rw-r--r--   0 runner    (1001) docker     (121)      426 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/globalaccelerator/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11661 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/globalaccelerator/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    23086 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/globalaccelerator/accelerator.py
+-rw-r--r--   0 runner    (1001) docker     (121)    38023 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/globalaccelerator/endpoint_group.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7200 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/globalaccelerator/get_accelerator.py
+-rw-r--r--   0 runner    (1001) docker     (121)    18414 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/globalaccelerator/listener.py
+-rw-r--r--   0 runner    (1001) docker     (121)    14344 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/globalaccelerator/outputs.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-24 22:23:25.000000 pulumi_aws-5.9.2/pulumi_aws/glue/
+-rw-r--r--   0 runner    (1001) docker     (121)      936 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/glue/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)   132646 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/glue/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    25119 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/glue/catalog_database.py
+-rw-r--r--   0 runner    (1001) docker     (121)    45572 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/glue/catalog_table.py
+-rw-r--r--   0 runner    (1001) docker     (121)    19114 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/glue/classifier.py
+-rw-r--r--   0 runner    (1001) docker     (121)    29835 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/glue/connection.py
+-rw-r--r--   0 runner    (1001) docker     (121)    63856 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/glue/crawler.py
+-rw-r--r--   0 runner    (1001) docker     (121)    12779 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/glue/data_catalog_encryption_settings.py
+-rw-r--r--   0 runner    (1001) docker     (121)    55175 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/glue/dev_endpoint.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7833 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/glue/get_connection.py
+-rw-r--r--   0 runner    (1001) docker     (121)     4459 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/glue/get_data_catalog_encryption_settings.py
+-rw-r--r--   0 runner    (1001) docker     (121)    19258 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/glue/get_script.py
+-rw-r--r--   0 runner    (1001) docker     (121)    57287 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/glue/job.py
+-rw-r--r--   0 runner    (1001) docker     (121)    48070 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/glue/ml_transform.py
+-rw-r--r--   0 runner    (1001) docker     (121)   141516 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/glue/outputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    23992 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/glue/partition.py
+-rw-r--r--   0 runner    (1001) docker     (121)    20754 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/glue/partition_index.py
+-rw-r--r--   0 runner    (1001) docker     (121)    13768 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/glue/registry.py
+-rw-r--r--   0 runner    (1001) docker     (121)     9130 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/glue/resource_policy.py
+-rw-r--r--   0 runner    (1001) docker     (121)    29168 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/glue/schema.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11191 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/glue/security_configuration.py
+-rw-r--r--   0 runner    (1001) docker     (121)    41976 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/glue/trigger.py
+-rw-r--r--   0 runner    (1001) docker     (121)    22562 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/glue/user_defined_function.py
+-rw-r--r--   0 runner    (1001) docker     (121)    21382 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/glue/workflow.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-24 22:23:25.000000 pulumi_aws-5.9.2/pulumi_aws/grafana/
+-rw-r--r--   0 runner    (1001) docker     (121)      434 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/grafana/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    13854 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/grafana/get_workspace.py
+-rw-r--r--   0 runner    (1001) docker     (121)    13795 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/grafana/license_association.py
+-rw-r--r--   0 runner    (1001) docker     (121)    15186 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/grafana/role_association.py
+-rw-r--r--   0 runner    (1001) docker     (121)    45618 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/grafana/workspace.py
+-rw-r--r--   0 runner    (1001) docker     (121)    35867 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/grafana/workspace_saml_configuration.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-24 22:23:25.000000 pulumi_aws-5.9.2/pulumi_aws/guardduty/
+-rw-r--r--   0 runner    (1001) docker     (121)      617 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/guardduty/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    13697 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/guardduty/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    24658 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/guardduty/detector.py
+-rw-r--r--   0 runner    (1001) docker     (121)    26049 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/guardduty/filter.py
+-rw-r--r--   0 runner    (1001) docker     (121)     4098 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/guardduty/get_detector.py
+-rw-r--r--   0 runner    (1001) docker     (121)    10988 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/guardduty/invite_accepter.py
+-rw-r--r--   0 runner    (1001) docker     (121)    21715 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/guardduty/ip_set.py
+-rw-r--r--   0 runner    (1001) docker     (121)    21666 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/guardduty/member.py
+-rw-r--r--   0 runner    (1001) docker     (121)     8663 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/guardduty/organization_admin_account.py
+-rw-r--r--   0 runner    (1001) docker     (121)    15005 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/guardduty/organization_configuration.py
+-rw-r--r--   0 runner    (1001) docker     (121)    14211 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/guardduty/outputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    21160 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/guardduty/publishing_destination.py
+-rw-r--r--   0 runner    (1001) docker     (121)    22757 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/guardduty/threat_intel_set.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-24 22:23:25.000000 pulumi_aws-5.9.2/pulumi_aws/iam/
+-rw-r--r--   0 runner    (1001) docker     (121)     1622 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/iam/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    26347 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/iam/_enums.py
+-rw-r--r--   0 runner    (1001) docker     (121)    15504 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/iam/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    23580 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/iam/access_key.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6629 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/iam/account_alias.py
+-rw-r--r--   0 runner    (1001) docker     (121)    29708 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/iam/account_password_policy.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2501 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/iam/get_account_alias.py
+-rw-r--r--   0 runner    (1001) docker     (121)     4926 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/iam/get_group.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6099 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/iam/get_instance_profile.py
+-rw-r--r--   0 runner    (1001) docker     (121)     4684 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/iam/get_instance_profiles.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6687 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/iam/get_openid_connect_provider.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7019 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/iam/get_policy.py
+-rw-r--r--   0 runner    (1001) docker     (121)    28240 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/iam/get_policy_document.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7788 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/iam/get_role.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7451 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/iam/get_roles.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6136 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/iam/get_saml_provider.py
+-rw-r--r--   0 runner    (1001) docker     (121)     8426 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/iam/get_server_certificate.py
+-rw-r--r--   0 runner    (1001) docker     (121)     4766 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/iam/get_session_context.py
+-rw-r--r--   0 runner    (1001) docker     (121)     5873 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/iam/get_user.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6514 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/iam/get_user_ssh_key.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6393 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/iam/get_users.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11181 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/iam/group.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11223 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/iam/group_membership.py
+-rw-r--r--   0 runner    (1001) docker     (121)    13344 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/iam/group_policy.py
+-rw-r--r--   0 runner    (1001) docker     (121)     9384 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/iam/group_policy_attachment.py
+-rw-r--r--   0 runner    (1001) docker     (121)    25393 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/iam/instance_profile.py
+-rw-r--r--   0 runner    (1001) docker     (121)    19404 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/iam/open_id_connect_provider.py
+-rw-r--r--   0 runner    (1001) docker     (121)    14814 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/iam/outputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    20816 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/iam/policy.py
+-rw-r--r--   0 runner    (1001) docker     (121)    18429 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/iam/policy_attachment.py
+-rw-r--r--   0 runner    (1001) docker     (121)    53016 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/iam/role.py
+-rw-r--r--   0 runner    (1001) docker     (121)    14422 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/iam/role_policy.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11229 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/iam/role_policy_attachment.py
+-rw-r--r--   0 runner    (1001) docker     (121)    15898 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/iam/saml_provider.py
+-rw-r--r--   0 runner    (1001) docker     (121)    34304 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/iam/server_certificate.py
+-rw-r--r--   0 runner    (1001) docker     (121)    23130 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/iam/service_linked_role.py
+-rw-r--r--   0 runner    (1001) docker     (121)    18566 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/iam/service_specific_credential.py
+-rw-r--r--   0 runner    (1001) docker     (121)    12509 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/iam/signing_certificate.py
+-rw-r--r--   0 runner    (1001) docker     (121)    17687 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/iam/ssh_key.py
+-rw-r--r--   0 runner    (1001) docker     (121)    22531 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/iam/user.py
+-rw-r--r--   0 runner    (1001) docker     (121)     9806 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/iam/user_group_membership.py
+-rw-r--r--   0 runner    (1001) docker     (121)    20885 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/iam/user_login_profile.py
+-rw-r--r--   0 runner    (1001) docker     (121)    13182 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/iam/user_policy.py
+-rw-r--r--   0 runner    (1001) docker     (121)     9301 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/iam/user_policy_attachment.py
+-rw-r--r--   0 runner    (1001) docker     (121)    19519 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/iam/virtual_mfa_device.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-24 22:23:25.000000 pulumi_aws-5.9.2/pulumi_aws/identitystore/
+-rw-r--r--   0 runner    (1001) docker     (121)      363 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/identitystore/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2988 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/identitystore/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)     5005 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/identitystore/get_group.py
+-rw-r--r--   0 runner    (1001) docker     (121)     4910 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/identitystore/get_user.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2524 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/identitystore/outputs.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-24 22:23:25.000000 pulumi_aws-5.9.2/pulumi_aws/imagebuilder/
+-rw-r--r--   0 runner    (1001) docker     (121)     1017 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/imagebuilder/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    70066 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/imagebuilder/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    33558 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/imagebuilder/component.py
+-rw-r--r--   0 runner    (1001) docker     (121)    46882 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/imagebuilder/container_recipe.py
+-rw-r--r--   0 runner    (1001) docker     (121)    21720 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/imagebuilder/distribution_configuration.py
+-rw-r--r--   0 runner    (1001) docker     (121)     9336 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/imagebuilder/get_component.py
+-rw-r--r--   0 runner    (1001) docker     (121)     5214 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/imagebuilder/get_components.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11876 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/imagebuilder/get_container_recipe.py
+-rw-r--r--   0 runner    (1001) docker     (121)     5447 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/imagebuilder/get_container_recipes.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6739 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/imagebuilder/get_distribution_configuration.py
+-rw-r--r--   0 runner    (1001) docker     (121)     4935 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/imagebuilder/get_distribution_configurations.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11781 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/imagebuilder/get_image.py
+-rw-r--r--   0 runner    (1001) docker     (121)    12492 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/imagebuilder/get_image_pipeline.py
+-rw-r--r--   0 runner    (1001) docker     (121)     4539 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/imagebuilder/get_image_pipelines.py
+-rw-r--r--   0 runner    (1001) docker     (121)     9401 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/imagebuilder/get_image_recipe.py
+-rw-r--r--   0 runner    (1001) docker     (121)     5299 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/imagebuilder/get_image_recipes.py
+-rw-r--r--   0 runner    (1001) docker     (121)    12800 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/imagebuilder/get_infrastructure_configuration.py
+-rw-r--r--   0 runner    (1001) docker     (121)     5001 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/imagebuilder/get_infrastructure_configurations.py
+-rw-r--r--   0 runner    (1001) docker     (121)    33555 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/imagebuilder/image.py
+-rw-r--r--   0 runner    (1001) docker     (121)    40865 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/imagebuilder/image_pipeline.py
+-rw-r--r--   0 runner    (1001) docker     (121)    37331 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/imagebuilder/image_recipe.py
+-rw-r--r--   0 runner    (1001) docker     (121)    43248 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/imagebuilder/infrastructure_configuration.py
+-rw-r--r--   0 runner    (1001) docker     (121)   108615 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/imagebuilder/outputs.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-24 22:23:25.000000 pulumi_aws-5.9.2/pulumi_aws/inspector/
+-rw-r--r--   0 runner    (1001) docker     (121)      401 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/inspector/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    10839 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/inspector/assessment_target.py
+-rw-r--r--   0 runner    (1001) docker     (121)    19346 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/inspector/assessment_template.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2928 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/inspector/get_rules_packages.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7869 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/inspector/resource_group.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-24 22:23:25.000000 pulumi_aws-5.9.2/pulumi_aws/iot/
+-rw-r--r--   0 runner    (1001) docker     (121)      800 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/iot/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)   133920 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/iot/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    23673 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/iot/authorizer.py
+-rw-r--r--   0 runner    (1001) docker     (121)    22675 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/iot/certificate.py
+-rw-r--r--   0 runner    (1001) docker     (121)     3835 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/iot/get_endpoint.py
+-rw-r--r--   0 runner    (1001) docker     (121)    13809 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/iot/indexing_configuration.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11430 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/iot/logging_options.py
+-rw-r--r--   0 runner    (1001) docker     (121)   133442 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/iot/outputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11259 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/iot/policy.py
+-rw-r--r--   0 runner    (1001) docker     (121)     8680 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/iot/policy_attachment.py
+-rw-r--r--   0 runner    (1001) docker     (121)    31001 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/iot/provisioning_template.py
+-rw-r--r--   0 runner    (1001) docker     (121)    13236 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/iot/role_alias.py
+-rw-r--r--   0 runner    (1001) docker     (121)    13079 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/iot/thing.py
+-rw-r--r--   0 runner    (1001) docker     (121)    17226 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/iot/thing_group.py
+-rw-r--r--   0 runner    (1001) docker     (121)    13124 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/iot/thing_group_membership.py
+-rw-r--r--   0 runner    (1001) docker     (121)     8404 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/iot/thing_principal_attachment.py
+-rw-r--r--   0 runner    (1001) docker     (121)    16341 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/iot/thing_type.py
+-rw-r--r--   0 runner    (1001) docker     (121)    59278 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/iot/topic_rule.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11092 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/iot/topic_rule_destination.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-24 22:23:25.000000 pulumi_aws-5.9.2/pulumi_aws/kendra/
+-rw-r--r--   0 runner    (1001) docker     (121)      335 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/kendra/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    30850 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/kendra/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    53613 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/kendra/index.py
+-rw-r--r--   0 runner    (1001) docker     (121)    31390 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/kendra/outputs.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-24 22:23:25.000000 pulumi_aws-5.9.2/pulumi_aws/keyspaces/
+-rw-r--r--   0 runner    (1001) docker     (121)      359 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/keyspaces/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    13961 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/keyspaces/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    12854 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/keyspaces/keyspace.py
+-rw-r--r--   0 runner    (1001) docker     (121)    13335 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/keyspaces/outputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    38228 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/keyspaces/table.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-24 22:23:25.000000 pulumi_aws-5.9.2/pulumi_aws/kinesis/
+-rw-r--r--   0 runner    (1001) docker     (121)      577 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/kinesis/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)   238352 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/kinesis/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    46754 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/kinesis/analytics_application.py
+-rw-r--r--   0 runner    (1001) docker     (121)    82112 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/kinesis/firehose_delivery_stream.py
+-rw-r--r--   0 runner    (1001) docker     (121)     3873 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/kinesis/get_firehose_delivery_stream.py
+-rw-r--r--   0 runner    (1001) docker     (121)     8908 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/kinesis/get_stream.py
+-rw-r--r--   0 runner    (1001) docker     (121)     5886 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/kinesis/get_stream_consumer.py
+-rw-r--r--   0 runner    (1001) docker     (121)   239935 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/kinesis/outputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    38220 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/kinesis/stream.py
+-rw-r--r--   0 runner    (1001) docker     (121)    12165 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/kinesis/stream_consumer.py
+-rw-r--r--   0 runner    (1001) docker     (121)    29540 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/kinesis/video_stream.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-24 22:23:25.000000 pulumi_aws-5.9.2/pulumi_aws/kinesisanalyticsv2/
+-rw-r--r--   0 runner    (1001) docker     (121)      377 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/kinesisanalyticsv2/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)   102491 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/kinesisanalyticsv2/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    60942 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/kinesisanalyticsv2/application.py
+-rw-r--r--   0 runner    (1001) docker     (121)    13130 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/kinesisanalyticsv2/application_snapshot.py
+-rw-r--r--   0 runner    (1001) docker     (121)   116604 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/kinesisanalyticsv2/outputs.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-24 22:23:25.000000 pulumi_aws-5.9.2/pulumi_aws/kms/
+-rw-r--r--   0 runner    (1001) docker     (121)      654 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/kms/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7222 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/kms/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    14467 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/kms/alias.py
+-rw-r--r--   0 runner    (1001) docker     (121)    12731 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/kms/ciphertext.py
+-rw-r--r--   0 runner    (1001) docker     (121)    38873 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/kms/external_key.py
+-rw-r--r--   0 runner    (1001) docker     (121)     4524 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/kms/get_alias.py
+-rw-r--r--   0 runner    (1001) docker     (121)     5983 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/kms/get_cipher_text.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11689 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/kms/get_key.py
+-rw-r--r--   0 runner    (1001) docker     (121)     9424 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/kms/get_public_key.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2588 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/kms/get_secret.py
+-rw-r--r--   0 runner    (1001) docker     (121)     3468 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/kms/get_secrets.py
+-rw-r--r--   0 runner    (1001) docker     (121)    37712 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/kms/grant.py
+-rw-r--r--   0 runner    (1001) docker     (121)    42240 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/kms/key.py
+-rw-r--r--   0 runner    (1001) docker     (121)     8663 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/kms/outputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    44708 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/kms/replica_external_key.py
+-rw-r--r--   0 runner    (1001) docker     (121)    35590 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/kms/replica_key.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-24 22:23:25.000000 pulumi_aws-5.9.2/pulumi_aws/lakeformation/
+-rw-r--r--   0 runner    (1001) docker     (121)      496 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/lakeformation/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    22238 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/lakeformation/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    23816 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/lakeformation/data_lake_settings.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6567 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/lakeformation/get_data_lake_settings.py
+-rw-r--r--   0 runner    (1001) docker     (121)    13075 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/lakeformation/get_permissions.py
+-rw-r--r--   0 runner    (1001) docker     (121)     3962 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/lakeformation/get_resource.py
+-rw-r--r--   0 runner    (1001) docker     (121)    21978 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/lakeformation/outputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    32802 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/lakeformation/permissions.py
+-rw-r--r--   0 runner    (1001) docker     (121)    10990 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/lakeformation/resource.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-24 22:23:25.000000 pulumi_aws-5.9.2/pulumi_aws/lambda_/
+-rw-r--r--   0 runner    (1001) docker     (121)      878 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/lambda_/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)      915 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/lambda_/_enums.py
+-rw-r--r--   0 runner    (1001) docker     (121)    31361 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/lambda_/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    19343 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/lambda_/alias.py
+-rw-r--r--   0 runner    (1001) docker     (121)    18215 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/lambda_/code_signing_config.py
+-rw-r--r--   0 runner    (1001) docker     (121)    93975 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/lambda_/event_source_mapping.py
+-rw-r--r--   0 runner    (1001) docker     (121)   110551 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/lambda_/function.py
+-rw-r--r--   0 runner    (1001) docker     (121)    25054 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/lambda_/function_event_invoke_config.py
+-rw-r--r--   0 runner    (1001) docker     (121)    20697 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/lambda_/function_url.py
+-rw-r--r--   0 runner    (1001) docker     (121)     5538 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/lambda_/get_alias.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6827 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/lambda_/get_code_signing_config.py
+-rw-r--r--   0 runner    (1001) docker     (121)    19263 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/lambda_/get_function.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7983 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/lambda_/get_function_url.py
+-rw-r--r--   0 runner    (1001) docker     (121)     4974 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/lambda_/get_invocation.py
+-rw-r--r--   0 runner    (1001) docker     (121)    13020 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/lambda_/get_layer_version.py
+-rw-r--r--   0 runner    (1001) docker     (121)    14538 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/lambda_/invocation.py
+-rw-r--r--   0 runner    (1001) docker     (121)    45846 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/lambda_/layer_version.py
+-rw-r--r--   0 runner    (1001) docker     (121)    23321 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/lambda_/layer_version_permission.py
+-rw-r--r--   0 runner    (1001) docker     (121)    38486 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/lambda_/outputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    45598 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/lambda_/permission.py
+-rw-r--r--   0 runner    (1001) docker     (121)    13301 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/lambda_/provisioned_concurrency_config.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-24 22:23:25.000000 pulumi_aws-5.9.2/pulumi_aws/lb/
+-rw-r--r--   0 runner    (1001) docker     (121)      626 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/lb/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    98570 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/lb/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)     5357 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/lb/get_hosted_zone_id.py
+-rw-r--r--   0 runner    (1001) docker     (121)     8157 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/lb/get_listener.py
+-rw-r--r--   0 runner    (1001) docker     (121)    13830 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/lb/get_load_balancer.py
+-rw-r--r--   0 runner    (1001) docker     (121)    12410 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/lb/get_target_group.py
+-rw-r--r--   0 runner    (1001) docker     (121)    40563 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/lb/listener.py
+-rw-r--r--   0 runner    (1001) docker     (121)    10898 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/lb/listener_certificate.py
+-rw-r--r--   0 runner    (1001) docker     (121)    34475 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/lb/listener_rule.py
+-rw-r--r--   0 runner    (1001) docker     (121)    69177 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/lb/load_balancer.py
+-rw-r--r--   0 runner    (1001) docker     (121)   107979 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/lb/outputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    61607 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/lb/target_group.py
+-rw-r--r--   0 runner    (1001) docker     (121)    18029 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/lb/target_group_attachment.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-24 22:23:25.000000 pulumi_aws-5.9.2/pulumi_aws/lex/
+-rw-r--r--   0 runner    (1001) docker     (121)      512 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/lex/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    64967 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/lex/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    66767 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/lex/bot.py
+-rw-r--r--   0 runner    (1001) docker     (121)    20824 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/lex/bot_alias.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11746 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/lex/get_bot.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6668 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/lex/get_bot_alias.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7067 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/lex/get_intent.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7743 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/lex/get_slot_type.py
+-rw-r--r--   0 runner    (1001) docker     (121)    64048 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/lex/intent.py
+-rw-r--r--   0 runner    (1001) docker     (121)    68292 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/lex/outputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    28159 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/lex/slot_type.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-24 22:23:25.000000 pulumi_aws-5.9.2/pulumi_aws/licensemanager/
+-rw-r--r--   0 runner    (1001) docker     (121)      333 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/licensemanager/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11122 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/licensemanager/association.py
+-rw-r--r--   0 runner    (1001) docker     (121)    27705 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/licensemanager/license_configuration.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-24 22:23:25.000000 pulumi_aws-5.9.2/pulumi_aws/lightsail/
+-rw-r--r--   0 runner    (1001) docker     (121)      567 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/lightsail/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    15974 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/lightsail/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    37776 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/lightsail/container_service.py
+-rw-r--r--   0 runner    (1001) docker     (121)    19495 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/lightsail/container_service_deployment_version.py
+-rw-r--r--   0 runner    (1001) docker     (121)     8201 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/lightsail/domain.py
+-rw-r--r--   0 runner    (1001) docker     (121)    39798 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/lightsail/instance.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11869 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/lightsail/instance_public_ports.py
+-rw-r--r--   0 runner    (1001) docker     (121)    21158 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/lightsail/key_pair.py
+-rw-r--r--   0 runner    (1001) docker     (121)    15826 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/lightsail/outputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)     9199 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/lightsail/static_ip.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11031 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/lightsail/static_ip_attachment.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-24 22:23:25.000000 pulumi_aws-5.9.2/pulumi_aws/location/
+-rw-r--r--   0 runner    (1001) docker     (121)      414 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/location/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2289 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/location/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6147 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/location/get_map.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7134 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/location/get_place_index.py
+-rw-r--r--   0 runner    (1001) docker     (121)    17010 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/location/map.py
+-rw-r--r--   0 runner    (1001) docker     (121)     3466 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/location/outputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    20156 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/location/place_index.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-24 22:23:25.000000 pulumi_aws-5.9.2/pulumi_aws/macie/
+-rw-r--r--   0 runner    (1001) docker     (121)      462 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/macie/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     9265 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/macie/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    31789 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/macie/custom_data_identifier.py
+-rw-r--r--   0 runner    (1001) docker     (121)    24353 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/macie/findings_filter.py
+-rw-r--r--   0 runner    (1001) docker     (121)     8004 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/macie/member_account_association.py
+-rw-r--r--   0 runner    (1001) docker     (121)     8483 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/macie/outputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    16480 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/macie/s3_bucket_association.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-24 22:23:25.000000 pulumi_aws-5.9.2/pulumi_aws/macie2/
+-rw-r--r--   0 runner    (1001) docker     (121)      470 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/macie2/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    30129 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/macie2/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    15593 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/macie2/account.py
+-rw-r--r--   0 runner    (1001) docker     (121)    43824 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/macie2/classification_job.py
+-rw-r--r--   0 runner    (1001) docker     (121)     9924 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/macie2/invitation_accepter.py
+-rw-r--r--   0 runner    (1001) docker     (121)    32068 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/macie2/member.py
+-rw-r--r--   0 runner    (1001) docker     (121)     8078 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/macie2/organization_admin_account.py
+-rw-r--r--   0 runner    (1001) docker     (121)    28661 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/macie2/outputs.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-24 22:23:25.000000 pulumi_aws-5.9.2/pulumi_aws/mediaconvert/
+-rw-r--r--   0 runner    (1001) docker     (121)      335 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/mediaconvert/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2429 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/mediaconvert/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2600 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/mediaconvert/outputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    20991 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/mediaconvert/queue.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-24 22:23:25.000000 pulumi_aws-5.9.2/pulumi_aws/mediapackage/
+-rw-r--r--   0 runner    (1001) docker     (121)      337 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/mediapackage/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2992 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/mediapackage/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    15502 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/mediapackage/channel.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2818 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/mediapackage/outputs.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-24 22:23:25.000000 pulumi_aws-5.9.2/pulumi_aws/mediastore/
+-rw-r--r--   0 runner    (1001) docker     (121)      326 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/mediastore/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    12751 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/mediastore/container.py
+-rw-r--r--   0 runner    (1001) docker     (121)    10004 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/mediastore/container_policy.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-24 22:23:25.000000 pulumi_aws-5.9.2/pulumi_aws/memorydb/
+-rw-r--r--   0 runner    (1001) docker     (121)      628 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/memorydb/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    19777 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/memorydb/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    18176 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/memorydb/acl.py
+-rw-r--r--   0 runner    (1001) docker     (121)    70938 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/memorydb/cluster.py
+-rw-r--r--   0 runner    (1001) docker     (121)     4853 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/memorydb/get_acl.py
+-rw-r--r--   0 runner    (1001) docker     (121)    16123 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/memorydb/get_cluster.py
+-rw-r--r--   0 runner    (1001) docker     (121)     5638 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/memorydb/get_parameter_group.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6213 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/memorydb/get_snapshot.py
+-rw-r--r--   0 runner    (1001) docker     (121)     5401 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/memorydb/get_subnet_group.py
+-rw-r--r--   0 runner    (1001) docker     (121)     5752 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/memorydb/get_user.py
+-rw-r--r--   0 runner    (1001) docker     (121)    29306 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/memorydb/outputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    22066 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/memorydb/parameter_group.py
+-rw-r--r--   0 runner    (1001) docker     (121)    22299 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/memorydb/snapshot.py
+-rw-r--r--   0 runner    (1001) docker     (121)    20138 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/memorydb/subnet_group.py
+-rw-r--r--   0 runner    (1001) docker     (121)    20256 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/memorydb/user.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-24 22:23:25.000000 pulumi_aws-5.9.2/pulumi_aws/mq/
+-rw-r--r--   0 runner    (1001) docker     (121)      434 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/mq/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    19543 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/mq/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    71259 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/mq/broker.py
+-rw-r--r--   0 runner    (1001) docker     (121)    26085 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/mq/configuration.py
+-rw-r--r--   0 runner    (1001) docker     (121)    13436 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/mq/get_broker.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6581 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/mq/get_instance_type_offerings.py
+-rw-r--r--   0 runner    (1001) docker     (121)    28981 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/mq/outputs.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-24 22:23:25.000000 pulumi_aws-5.9.2/pulumi_aws/msk/
+-rw-r--r--   0 runner    (1001) docker     (121)      531 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/msk/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    36494 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/msk/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    80810 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/msk/cluster.py
+-rw-r--r--   0 runner    (1001) docker     (121)    16652 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/msk/configuration.py
+-rw-r--r--   0 runner    (1001) docker     (121)     3610 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/msk/get_broker_nodes.py
+-rw-r--r--   0 runner    (1001) docker     (121)    16125 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/msk/get_cluster.py
+-rw-r--r--   0 runner    (1001) docker     (121)     5427 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/msk/get_configuration.py
+-rw-r--r--   0 runner    (1001) docker     (121)     4914 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/msk/get_kafka_version.py
+-rw-r--r--   0 runner    (1001) docker     (121)    41111 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/msk/outputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    12352 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/msk/scram_secret_association.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-24 22:23:25.000000 pulumi_aws-5.9.2/pulumi_aws/mskconnect/
+-rw-r--r--   0 runner    (1001) docker     (121)      506 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/mskconnect/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    30217 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/mskconnect/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    45904 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/mskconnect/connector.py
+-rw-r--r--   0 runner    (1001) docker     (121)    17367 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/mskconnect/custom_plugin.py
+-rw-r--r--   0 runner    (1001) docker     (121)     4120 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/mskconnect/get_connector.py
+-rw-r--r--   0 runner    (1001) docker     (121)     4769 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/mskconnect/get_custom_plugin.py
+-rw-r--r--   0 runner    (1001) docker     (121)     5213 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/mskconnect/get_worker_configuration.py
+-rw-r--r--   0 runner    (1001) docker     (121)    33712 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/mskconnect/outputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    14197 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/mskconnect/worker_configuration.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-24 22:23:25.000000 pulumi_aws-5.9.2/pulumi_aws/mwaa/
+-rw-r--r--   0 runner    (1001) docker     (121)      341 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/mwaa/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    20959 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/mwaa/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    84052 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/mwaa/environment.py
+-rw-r--r--   0 runner    (1001) docker     (121)    22349 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/mwaa/outputs.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-24 22:23:25.000000 pulumi_aws-5.9.2/pulumi_aws/neptune/
+-rw-r--r--   0 runner    (1001) docker     (121)      640 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/neptune/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     3956 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/neptune/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    89812 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/neptune/cluster.py
+-rw-r--r--   0 runner    (1001) docker     (121)    25030 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/neptune/cluster_endpoint.py
+-rw-r--r--   0 runner    (1001) docker     (121)    60070 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/neptune/cluster_instance.py
+-rw-r--r--   0 runner    (1001) docker     (121)    21415 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/neptune/cluster_parameter_group.py
+-rw-r--r--   0 runner    (1001) docker     (121)    25200 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/neptune/cluster_snapshot.py
+-rw-r--r--   0 runner    (1001) docker     (121)    32035 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/neptune/event_subscription.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11437 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/neptune/get_engine_version.py
+-rw-r--r--   0 runner    (1001) docker     (121)    17803 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/neptune/get_orderable_db_instance.py
+-rw-r--r--   0 runner    (1001) docker     (121)     4207 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/neptune/outputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    18641 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/neptune/parameter_group.py
+-rw-r--r--   0 runner    (1001) docker     (121)    19189 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/neptune/subnet_group.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-24 22:23:25.000000 pulumi_aws-5.9.2/pulumi_aws/networkfirewall/
+-rw-r--r--   0 runner    (1001) docker     (121)      463 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/networkfirewall/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    87520 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/networkfirewall/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    34608 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/networkfirewall/firewall.py
+-rw-r--r--   0 runner    (1001) docker     (121)    21821 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/networkfirewall/firewall_policy.py
+-rw-r--r--   0 runner    (1001) docker     (121)    15259 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/networkfirewall/logging_configuration.py
+-rw-r--r--   0 runner    (1001) docker     (121)    92376 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/networkfirewall/outputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11889 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/networkfirewall/resource_policy.py
+-rw-r--r--   0 runner    (1001) docker     (121)    44249 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/networkfirewall/rule_group.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-24 22:23:25.000000 pulumi_aws-5.9.2/pulumi_aws/networkmanager/
+-rw-r--r--   0 runner    (1001) docker     (121)      937 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/networkmanager/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    39513 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/networkmanager/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    20952 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/networkmanager/connection.py
+-rw-r--r--   0 runner    (1001) docker     (121)    16565 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/networkmanager/customer_gateway_association.py
+-rw-r--r--   0 runner    (1001) docker     (121)    25216 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/networkmanager/device.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7753 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/networkmanager/get_connection.py
+-rw-r--r--   0 runner    (1001) docker     (121)     5157 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/networkmanager/get_connections.py
+-rw-r--r--   0 runner    (1001) docker     (121)    16714 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/networkmanager/get_core_network_policy_document.py
+-rw-r--r--   0 runner    (1001) docker     (121)     8559 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/networkmanager/get_device.py
+-rw-r--r--   0 runner    (1001) docker     (121)     4975 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/networkmanager/get_devices.py
+-rw-r--r--   0 runner    (1001) docker     (121)     4811 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/networkmanager/get_global_network.py
+-rw-r--r--   0 runner    (1001) docker     (121)     3498 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/networkmanager/get_global_networks.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7156 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/networkmanager/get_link.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6241 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/networkmanager/get_links.py
+-rw-r--r--   0 runner    (1001) docker     (121)     5795 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/networkmanager/get_site.py
+-rw-r--r--   0 runner    (1001) docker     (121)     4227 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/networkmanager/get_sites.py
+-rw-r--r--   0 runner    (1001) docker     (121)     9725 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/networkmanager/global_network.py
+-rw-r--r--   0 runner    (1001) docker     (121)    19727 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/networkmanager/link.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11221 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/networkmanager/link_association.py
+-rw-r--r--   0 runner    (1001) docker     (121)    38461 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/networkmanager/outputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    14102 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/networkmanager/site.py
+-rw-r--r--   0 runner    (1001) docker     (121)    14635 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/networkmanager/transit_gateway_connect_peer_association.py
+-rw-r--r--   0 runner    (1001) docker     (121)    10914 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/networkmanager/transit_gateway_registration.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-24 22:23:25.000000 pulumi_aws-5.9.2/pulumi_aws/opensearch/
+-rw-r--r--   0 runner    (1001) docker     (121)      426 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/opensearch/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    48898 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/opensearch/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    70459 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/opensearch/domain.py
+-rw-r--r--   0 runner    (1001) docker     (121)     9701 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/opensearch/domain_policy.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11125 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/opensearch/domain_saml_options.py
+-rw-r--r--   0 runner    (1001) docker     (121)    15019 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/opensearch/get_domain.py
+-rw-r--r--   0 runner    (1001) docker     (121)    70072 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/opensearch/outputs.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-24 22:23:25.000000 pulumi_aws-5.9.2/pulumi_aws/opsworks/
+-rw-r--r--   0 runner    (1001) docker     (121)      802 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/opsworks/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)   135246 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/opsworks/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    46395 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/opsworks/application.py
+-rw-r--r--   0 runner    (1001) docker     (121)    62734 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/opsworks/custom_layer.py
+-rw-r--r--   0 runner    (1001) docker     (121)    59671 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/opsworks/ecs_cluster_layer.py
+-rw-r--r--   0 runner    (1001) docker     (121)    64406 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/opsworks/ganglia_layer.py
+-rw-r--r--   0 runner    (1001) docker     (121)    71586 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/opsworks/haproxy_layer.py
+-rw-r--r--   0 runner    (1001) docker     (121)    98619 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/opsworks/instance.py
+-rw-r--r--   0 runner    (1001) docker     (121)    69135 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/opsworks/java_app_layer.py
+-rw-r--r--   0 runner    (1001) docker     (121)    61448 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/opsworks/memcached_layer.py
+-rw-r--r--   0 runner    (1001) docker     (121)    63831 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/opsworks/mysql_layer.py
+-rw-r--r--   0 runner    (1001) docker     (121)    61103 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/opsworks/nodejs_app_layer.py
+-rw-r--r--   0 runner    (1001) docker     (121)   125980 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/opsworks/outputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    14380 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/opsworks/permission.py
+-rw-r--r--   0 runner    (1001) docker     (121)    59282 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/opsworks/php_app_layer.py
+-rw-r--r--   0 runner    (1001) docker     (121)    72023 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/opsworks/rails_app_layer.py
+-rw-r--r--   0 runner    (1001) docker     (121)    12743 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/opsworks/rds_db_instance.py
+-rw-r--r--   0 runner    (1001) docker     (121)    62234 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/opsworks/stack.py
+-rw-r--r--   0 runner    (1001) docker     (121)    58838 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/opsworks/static_web_layer.py
+-rw-r--r--   0 runner    (1001) docker     (121)    12594 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/opsworks/user_profile.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-24 22:23:25.000000 pulumi_aws-5.9.2/pulumi_aws/organizations/
+-rw-r--r--   0 runner    (1001) docker     (121)      681 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/organizations/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11485 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/organizations/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    37313 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/organizations/account.py
+-rw-r--r--   0 runner    (1001) docker     (121)    18877 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/organizations/delegated_administrator.py
+-rw-r--r--   0 runner    (1001) docker     (121)     4834 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/organizations/get_delegated_administrators.py
+-rw-r--r--   0 runner    (1001) docker     (121)     4057 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/organizations/get_delegated_services.py
+-rw-r--r--   0 runner    (1001) docker     (121)     9701 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/organizations/get_organization.py
+-rw-r--r--   0 runner    (1001) docker     (121)     4009 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/organizations/get_organizational_units.py
+-rw-r--r--   0 runner    (1001) docker     (121)     3947 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/organizations/get_resource_tags.py
+-rw-r--r--   0 runner    (1001) docker     (121)    29349 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/organizations/organization.py
+-rw-r--r--   0 runner    (1001) docker     (121)    15803 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/organizations/organizational_unit.py
+-rw-r--r--   0 runner    (1001) docker     (121)    20181 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/organizations/outputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    23187 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/organizations/policy.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11096 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/organizations/policy_attachment.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-24 22:23:25.000000 pulumi_aws-5.9.2/pulumi_aws/outposts/
+-rw-r--r--   0 runner    (1001) docker     (121)      456 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/outposts/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6158 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/outposts/get_outpost.py
+-rw-r--r--   0 runner    (1001) docker     (121)     5009 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/outposts/get_outpost_instance_type.py
+-rw-r--r--   0 runner    (1001) docker     (121)     3638 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/outposts/get_outpost_instance_types.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6043 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/outposts/get_outposts.py
+-rw-r--r--   0 runner    (1001) docker     (121)     3703 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/outposts/get_site.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2121 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/outposts/get_sites.py
+-rw-r--r--   0 runner    (1001) docker     (121)    10664 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/outputs.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-24 22:23:25.000000 pulumi_aws-5.9.2/pulumi_aws/pinpoint/
+-rw-r--r--   0 runner    (1001) docker     (121)      638 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/pinpoint/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7167 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/pinpoint/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    13237 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/pinpoint/adm_channel.py
+-rw-r--r--   0 runner    (1001) docker     (121)    27996 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/pinpoint/apns_channel.py
+-rw-r--r--   0 runner    (1001) docker     (121)    28312 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/pinpoint/apns_sandbox_channel.py
+-rw-r--r--   0 runner    (1001) docker     (121)    28148 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/pinpoint/apns_voip_channel.py
+-rw-r--r--   0 runner    (1001) docker     (121)    28408 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/pinpoint/apns_voip_sandbox_channel.py
+-rw-r--r--   0 runner    (1001) docker     (121)    23877 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/pinpoint/app.py
+-rw-r--r--   0 runner    (1001) docker     (121)    12483 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/pinpoint/baidu_channel.py
+-rw-r--r--   0 runner    (1001) docker     (121)    21632 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/pinpoint/email_channel.py
+-rw-r--r--   0 runner    (1001) docker     (121)    13861 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/pinpoint/event_stream.py
+-rw-r--r--   0 runner    (1001) docker     (121)    10420 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/pinpoint/gcm_channel.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6902 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/pinpoint/outputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    15373 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/pinpoint/sms_channel.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-24 22:23:25.000000 pulumi_aws-5.9.2/pulumi_aws/pricing/
+-rw-r--r--   0 runner    (1001) docker     (121)      341 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/pricing/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1358 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/pricing/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7773 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/pricing/get_product.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1183 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/pricing/outputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    48683 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/provider.py
+-rw-r--r--   0 runner    (1001) docker     (121)       40 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/pulumi-plugin.json
+-rw-r--r--   0 runner    (1001) docker     (121)        0 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/py.typed
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-24 22:23:25.000000 pulumi_aws-5.9.2/pulumi_aws/qldb/
+-rw-r--r--   0 runner    (1001) docker     (121)      384 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/qldb/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2023 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/qldb/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)     5039 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/qldb/get_ledger.py
+-rw-r--r--   0 runner    (1001) docker     (121)    19719 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/qldb/ledger.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2338 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/qldb/outputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    29413 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/qldb/stream.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-24 22:23:25.000000 pulumi_aws-5.9.2/pulumi_aws/quicksight/
+-rw-r--r--   0 runner    (1001) docker     (121)      414 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/quicksight/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    46897 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/quicksight/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    36821 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/quicksight/data_source.py
+-rw-r--r--   0 runner    (1001) docker     (121)    13721 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/quicksight/group.py
+-rw-r--r--   0 runner    (1001) docker     (121)    14480 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/quicksight/group_membership.py
+-rw-r--r--   0 runner    (1001) docker     (121)    41805 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/quicksight/outputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    26091 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/quicksight/user.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-24 22:23:25.000000 pulumi_aws-5.9.2/pulumi_aws/ram/
+-rw-r--r--   0 runner    (1001) docker     (121)      490 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ram/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1316 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ram/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)     9060 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ram/get_resource_share.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1131 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ram/outputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    13558 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ram/principal_association.py
+-rw-r--r--   0 runner    (1001) docker     (121)    10782 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ram/resource_association.py
+-rw-r--r--   0 runner    (1001) docker     (121)    19655 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ram/resource_share.py
+-rw-r--r--   0 runner    (1001) docker     (121)    18473 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ram/resource_share_accepter.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-24 22:23:25.000000 pulumi_aws-5.9.2/pulumi_aws/rds/
+-rw-r--r--   0 runner    (1001) docker     (121)     1356 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/rds/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     3396 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/rds/_enums.py
+-rw-r--r--   0 runner    (1001) docker     (121)    48509 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/rds/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)   172650 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/rds/cluster.py
+-rw-r--r--   0 runner    (1001) docker     (121)    20947 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/rds/cluster_activity_stream.py
+-rw-r--r--   0 runner    (1001) docker     (121)    29277 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/rds/cluster_endpoint.py
+-rw-r--r--   0 runner    (1001) docker     (121)    91017 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/rds/cluster_instance.py
+-rw-r--r--   0 runner    (1001) docker     (121)    24514 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/rds/cluster_parameter_group.py
+-rw-r--r--   0 runner    (1001) docker     (121)    14561 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/rds/cluster_role_association.py
+-rw-r--r--   0 runner    (1001) docker     (121)    29876 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/rds/cluster_snapshot.py
+-rw-r--r--   0 runner    (1001) docker     (121)    31357 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/rds/event_subscription.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7275 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/rds/get_certificate.py
+-rw-r--r--   0 runner    (1001) docker     (121)    17007 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/rds/get_cluster.py
+-rw-r--r--   0 runner    (1001) docker     (121)    18799 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/rds/get_cluster_snapshot.py
+-rw-r--r--   0 runner    (1001) docker     (121)    16455 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/rds/get_engine_version.py
+-rw-r--r--   0 runner    (1001) docker     (121)     4701 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/rds/get_event_categories.py
+-rw-r--r--   0 runner    (1001) docker     (121)    25502 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/rds/get_instance.py
+-rw-r--r--   0 runner    (1001) docker     (121)    29409 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/rds/get_orderable_db_instance.py
+-rw-r--r--   0 runner    (1001) docker     (121)     8605 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/rds/get_proxy.py
+-rw-r--r--   0 runner    (1001) docker     (121)    19406 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/rds/get_snapshot.py
+-rw-r--r--   0 runner    (1001) docker     (121)     5186 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/rds/get_subnet_group.py
+-rw-r--r--   0 runner    (1001) docker     (121)    30318 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/rds/global_cluster.py
+-rw-r--r--   0 runner    (1001) docker     (121)   218146 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/rds/instance.py
+-rw-r--r--   0 runner    (1001) docker     (121)    22650 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/rds/instance_automated_backups_replication.py
+-rw-r--r--   0 runner    (1001) docker     (121)    28914 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/rds/option_group.py
+-rw-r--r--   0 runner    (1001) docker     (121)    49497 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/rds/outputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    22984 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/rds/parameter_group.py
+-rw-r--r--   0 runner    (1001) docker     (121)    42252 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/rds/proxy.py
+-rw-r--r--   0 runner    (1001) docker     (121)    15246 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/rds/proxy_default_target_group.py
+-rw-r--r--   0 runner    (1001) docker     (121)    26869 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/rds/proxy_endpoint.py
+-rw-r--r--   0 runner    (1001) docker     (121)    23890 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/rds/proxy_target.py
+-rw-r--r--   0 runner    (1001) docker     (121)    14786 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/rds/role_association.py
+-rw-r--r--   0 runner    (1001) docker     (121)    16888 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/rds/security_group.py
+-rw-r--r--   0 runner    (1001) docker     (121)    34496 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/rds/snapshot.py
+-rw-r--r--   0 runner    (1001) docker     (121)    44647 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/rds/snapshot_copy.py
+-rw-r--r--   0 runner    (1001) docker     (121)    19057 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/rds/subnet_group.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-24 22:23:25.000000 pulumi_aws-5.9.2/pulumi_aws/redshift/
+-rw-r--r--   0 runner    (1001) docker     (121)      975 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/redshift/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    25770 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/redshift/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11211 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/redshift/authentication_profile.py
+-rw-r--r--   0 runner    (1001) docker     (121)   127150 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/redshift/cluster.py
+-rw-r--r--   0 runner    (1001) docker     (121)    13433 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/redshift/cluster_iam_roles.py
+-rw-r--r--   0 runner    (1001) docker     (121)    21664 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/redshift/endpoint_access.py
+-rw-r--r--   0 runner    (1001) docker     (121)    31939 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/redshift/event_subscription.py
+-rw-r--r--   0 runner    (1001) docker     (121)    27318 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/redshift/get_cluster.py
+-rw-r--r--   0 runner    (1001) docker     (121)    10194 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/redshift/get_cluster_credentials.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6970 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/redshift/get_orderable_cluster.py
+-rw-r--r--   0 runner    (1001) docker     (121)     5826 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/redshift/get_service_account.py
+-rw-r--r--   0 runner    (1001) docker     (121)     5144 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/redshift/get_subnet_group.py
+-rw-r--r--   0 runner    (1001) docker     (121)    16412 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/redshift/hsm_client_certificate.py
+-rw-r--r--   0 runner    (1001) docker     (121)    27419 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/redshift/hsm_configuration.py
+-rw-r--r--   0 runner    (1001) docker     (121)    28410 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/redshift/outputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    19650 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/redshift/parameter_group.py
+-rw-r--r--   0 runner    (1001) docker     (121)    27036 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/redshift/scheduled_action.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11414 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/redshift/security_group.py
+-rw-r--r--   0 runner    (1001) docker     (121)    17036 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/redshift/snapshot_copy_grant.py
+-rw-r--r--   0 runner    (1001) docker     (121)    22715 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/redshift/snapshot_schedule.py
+-rw-r--r--   0 runner    (1001) docker     (121)    10662 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/redshift/snapshot_schedule_association.py
+-rw-r--r--   0 runner    (1001) docker     (121)    18003 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/redshift/subnet_group.py
+-rw-r--r--   0 runner    (1001) docker     (121)    28490 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/redshift/usage_limit.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-24 22:23:25.000000 pulumi_aws-5.9.2/pulumi_aws/redshiftdata/
+-rw-r--r--   0 runner    (1001) docker     (121)      339 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/redshiftdata/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1076 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/redshiftdata/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)      808 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/redshiftdata/outputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    20974 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/redshiftdata/statement.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-24 22:23:25.000000 pulumi_aws-5.9.2/pulumi_aws/resourcegroups/
+-rw-r--r--   0 runner    (1001) docker     (121)      335 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/resourcegroups/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1513 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/resourcegroups/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    17631 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/resourcegroups/group.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1207 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/resourcegroups/outputs.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-24 22:23:25.000000 pulumi_aws-5.9.2/pulumi_aws/resourcegroupstaggingapi/
+-rw-r--r--   0 runner    (1001) docker     (121)      343 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/resourcegroupstaggingapi/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1465 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/resourcegroupstaggingapi/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    10619 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/resourcegroupstaggingapi/get_resources.py
+-rw-r--r--   0 runner    (1001) docker     (121)     4601 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/resourcegroupstaggingapi/outputs.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-24 22:23:25.000000 pulumi_aws-5.9.2/pulumi_aws/route53/
+-rw-r--r--   0 runner    (1001) docker     (121)     1337 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/route53/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)      465 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/route53/_enums.py
+-rw-r--r--   0 runner    (1001) docker     (121)    42528 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/route53/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    10313 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/route53/delegation_set.py
+-rw-r--r--   0 runner    (1001) docker     (121)     4179 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/route53/get_delegation_set.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7652 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/route53/get_resolver_endpoint.py
+-rw-r--r--   0 runner    (1001) docker     (121)     9603 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/route53/get_resolver_rule.py
+-rw-r--r--   0 runner    (1001) docker     (121)     9234 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/route53/get_resolver_rules.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11174 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/route53/get_traffic_policy_document.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11226 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/route53/get_zone.py
+-rw-r--r--   0 runner    (1001) docker     (121)    70665 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/route53/health_check.py
+-rw-r--r--   0 runner    (1001) docker     (121)    16132 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/route53/hosted_zone_dns_sec.py
+-rw-r--r--   0 runner    (1001) docker     (121)    38591 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/route53/key_signing_key.py
+-rw-r--r--   0 runner    (1001) docker     (121)    36317 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/route53/outputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    14120 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/route53/query_log.py
+-rw-r--r--   0 runner    (1001) docker     (121)    55413 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/route53/record.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11518 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/route53/resolver_dns_sec_config.py
+-rw-r--r--   0 runner    (1001) docker     (121)    25348 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/route53/resolver_endpoint.py
+-rw-r--r--   0 runner    (1001) docker     (121)    14594 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/route53/resolver_firewall_config.py
+-rw-r--r--   0 runner    (1001) docker     (121)    14544 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/route53/resolver_firewall_domain_list.py
+-rw-r--r--   0 runner    (1001) docker     (121)    29886 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/route53/resolver_firewall_rule.py
+-rw-r--r--   0 runner    (1001) docker     (121)    15880 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/route53/resolver_firewall_rule_group.py
+-rw-r--r--   0 runner    (1001) docker     (121)    24469 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/route53/resolver_firewall_rule_group_association.py
+-rw-r--r--   0 runner    (1001) docker     (121)    19283 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/route53/resolver_query_log_config.py
+-rw-r--r--   0 runner    (1001) docker     (121)    10882 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/route53/resolver_query_log_config_association.py
+-rw-r--r--   0 runner    (1001) docker     (121)    28233 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/route53/resolver_rule.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11398 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/route53/resolver_rule_association.py
+-rw-r--r--   0 runner    (1001) docker     (121)    14733 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/route53/traffic_policy.py
+-rw-r--r--   0 runner    (1001) docker     (121)    17523 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/route53/traffic_policy_instance.py
+-rw-r--r--   0 runner    (1001) docker     (121)    13427 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/route53/vpc_association_authorization.py
+-rw-r--r--   0 runner    (1001) docker     (121)    28097 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/route53/zone.py
+-rw-r--r--   0 runner    (1001) docker     (121)    15362 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/route53/zone_association.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-24 22:23:25.000000 pulumi_aws-5.9.2/pulumi_aws/route53domains/
+-rw-r--r--   0 runner    (1001) docker     (121)      347 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/route53domains/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    31460 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/route53domains/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    27957 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/route53domains/outputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    49635 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/route53domains/registered_domain.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-24 22:23:25.000000 pulumi_aws-5.9.2/pulumi_aws/route53recoverycontrol/
+-rw-r--r--   0 runner    (1001) docker     (121)      424 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/route53recoverycontrol/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     3202 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/route53recoverycontrol/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    10268 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/route53recoverycontrol/cluster.py
+-rw-r--r--   0 runner    (1001) docker     (121)    13597 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/route53recoverycontrol/control_panel.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2404 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/route53recoverycontrol/outputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    14369 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/route53recoverycontrol/routing_control.py
+-rw-r--r--   0 runner    (1001) docker     (121)    27687 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/route53recoverycontrol/safety_rule.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-24 22:23:25.000000 pulumi_aws-5.9.2/pulumi_aws/route53recoveryreadiness/
+-rw-r--r--   0 runner    (1001) docker     (121)      423 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/route53recoveryreadiness/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11094 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/route53recoveryreadiness/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    15647 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/route53recoveryreadiness/cell.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11602 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/route53recoveryreadiness/outputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    15122 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/route53recoveryreadiness/readiness_check.py
+-rw-r--r--   0 runner    (1001) docker     (121)    14886 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/route53recoveryreadiness/recovery_group.py
+-rw-r--r--   0 runner    (1001) docker     (121)    17773 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/route53recoveryreadiness/resource_set.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-24 22:23:25.000000 pulumi_aws-5.9.2/pulumi_aws/s3/
+-rw-r--r--   0 runner    (1001) docker     (121)     1550 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/s3/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)      702 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/s3/_enums.py
+-rw-r--r--   0 runner    (1001) docker     (121)   269035 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/s3/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    35312 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/s3/access_point.py
+-rw-r--r--   0 runner    (1001) docker     (121)    26825 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/s3/account_public_access_block.py
+-rw-r--r--   0 runner    (1001) docker     (121)    17506 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/s3/analytics_configuration.py
+-rw-r--r--   0 runner    (1001) docker     (121)    97790 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/s3/bucket.py
+-rw-r--r--   0 runner    (1001) docker     (121)    12938 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/s3/bucket_accelerate_configuration_v2.py
+-rw-r--r--   0 runner    (1001) docker     (121)    19585 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/s3/bucket_acl_v2.py
+-rw-r--r--   0 runner    (1001) docker     (121)    15865 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/s3/bucket_cors_configuration_v2.py
+-rw-r--r--   0 runner    (1001) docker     (121)    20413 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/s3/bucket_intelligent_tiering_configuration.py
+-rw-r--r--   0 runner    (1001) docker     (121)    13850 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/s3/bucket_lifecycle_configuration_v2.py
+-rw-r--r--   0 runner    (1001) docker     (121)    19189 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/s3/bucket_logging_v2.py
+-rw-r--r--   0 runner    (1001) docker     (121)    13093 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/s3/bucket_metric.py
+-rw-r--r--   0 runner    (1001) docker     (121)    31525 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/s3/bucket_notification.py
+-rw-r--r--   0 runner    (1001) docker     (121)    85499 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/s3/bucket_object.py
+-rw-r--r--   0 runner    (1001) docker     (121)    26511 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/s3/bucket_object_lock_configuration_v2.py
+-rw-r--r--   0 runner    (1001) docker     (121)    84292 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/s3/bucket_objectv2.py
+-rw-r--r--   0 runner    (1001) docker     (121)    10108 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/s3/bucket_ownership_controls.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11082 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/s3/bucket_policy.py
+-rw-r--r--   0 runner    (1001) docker     (121)    25638 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/s3/bucket_public_access_block.py
+-rw-r--r--   0 runner    (1001) docker     (121)    28203 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/s3/bucket_replication_config.py
+-rw-r--r--   0 runner    (1001) docker     (121)    13263 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/s3/bucket_request_payment_configuration_v2.py
+-rw-r--r--   0 runner    (1001) docker     (121)    15177 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/s3/bucket_server_side_encryption_configuration_v2.py
+-rw-r--r--   0 runner    (1001) docker     (121)   136875 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/s3/bucket_v2.py
+-rw-r--r--   0 runner    (1001) docker     (121)    20424 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/s3/bucket_versioning_v2.py
+-rw-r--r--   0 runner    (1001) docker     (121)    33509 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/s3/bucket_website_configuration_v2.py
+-rw-r--r--   0 runner    (1001) docker     (121)     8814 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/s3/get_bucket.py
+-rw-r--r--   0 runner    (1001) docker     (121)    22177 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/s3/get_bucket_object.py
+-rw-r--r--   0 runner    (1001) docker     (121)    10307 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/s3/get_bucket_objects.py
+-rw-r--r--   0 runner    (1001) docker     (121)     3549 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/s3/get_bucket_policy.py
+-rw-r--r--   0 runner    (1001) docker     (121)     3067 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/s3/get_canonical_user_id.py
+-rw-r--r--   0 runner    (1001) docker     (121)    21514 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/s3/get_object.py
+-rw-r--r--   0 runner    (1001) docker     (121)     9186 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/s3/get_objects.py
+-rw-r--r--   0 runner    (1001) docker     (121)    27604 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/s3/inventory.py
+-rw-r--r--   0 runner    (1001) docker     (121)   131651 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/s3/object_copy.py
+-rw-r--r--   0 runner    (1001) docker     (121)   257905 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/s3/outputs.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-24 22:23:25.000000 pulumi_aws-5.9.2/pulumi_aws/s3control/
+-rw-r--r--   0 runner    (1001) docker     (121)      626 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/s3control/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    28775 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/s3control/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    12547 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/s3control/access_point_policy.py
+-rw-r--r--   0 runner    (1001) docker     (121)    16903 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/s3control/bucket.py
+-rw-r--r--   0 runner    (1001) docker     (121)    12577 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/s3control/bucket_lifecycle_configuration.py
+-rw-r--r--   0 runner    (1001) docker     (121)     9842 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/s3control/bucket_policy.py
+-rw-r--r--   0 runner    (1001) docker     (121)    18254 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/s3control/multi_region_access_point.py
+-rw-r--r--   0 runner    (1001) docker     (121)    14874 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/s3control/multi_region_access_point_policy.py
+-rw-r--r--   0 runner    (1001) docker     (121)    14371 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/s3control/object_lambda_access_point.py
+-rw-r--r--   0 runner    (1001) docker     (121)    14632 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/s3control/object_lambda_access_point_policy.py
+-rw-r--r--   0 runner    (1001) docker     (121)    29537 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/s3control/outputs.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-24 22:23:25.000000 pulumi_aws-5.9.2/pulumi_aws/s3outposts/
+-rw-r--r--   0 runner    (1001) docker     (121)      338 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/s3outposts/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1230 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/s3outposts/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    16354 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/s3outposts/endpoint.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1634 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/s3outposts/outputs.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-24 22:23:25.000000 pulumi_aws-5.9.2/pulumi_aws/sagemaker/
+-rw-r--r--   0 runner    (1001) docker     (121)     1034 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/sagemaker/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)   168382 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/sagemaker/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    21069 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/sagemaker/app.py
+-rw-r--r--   0 runner    (1001) docker     (121)    18358 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/sagemaker/app_image_config.py
+-rw-r--r--   0 runner    (1001) docker     (121)    17592 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/sagemaker/code_repository.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11155 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/sagemaker/device.py
+-rw-r--r--   0 runner    (1001) docker     (121)    23710 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/sagemaker/device_fleet.py
+-rw-r--r--   0 runner    (1001) docker     (121)    39201 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/sagemaker/domain.py
+-rw-r--r--   0 runner    (1001) docker     (121)    17552 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/sagemaker/endpoint.py
+-rw-r--r--   0 runner    (1001) docker     (121)    25038 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/sagemaker/endpoint_configuration.py
+-rw-r--r--   0 runner    (1001) docker     (121)    33860 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/sagemaker/feature_group.py
+-rw-r--r--   0 runner    (1001) docker     (121)    36456 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/sagemaker/flow_definition.py
+-rw-r--r--   0 runner    (1001) docker     (121)     9442 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/sagemaker/get_prebuilt_ecr_image.py
+-rw-r--r--   0 runner    (1001) docker     (121)    15483 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/sagemaker/human_task_ui.py
+-rw-r--r--   0 runner    (1001) docker     (121)    18665 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/sagemaker/image.py
+-rw-r--r--   0 runner    (1001) docker     (121)    13264 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/sagemaker/image_version.py
+-rw-r--r--   0 runner    (1001) docker     (121)    32299 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/sagemaker/model.py
+-rw-r--r--   0 runner    (1001) docker     (121)    15343 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/sagemaker/model_package_group.py
+-rw-r--r--   0 runner    (1001) docker     (121)     8494 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/sagemaker/model_package_group_policy.py
+-rw-r--r--   0 runner    (1001) docker     (121)    53133 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/sagemaker/notebook_instance.py
+-rw-r--r--   0 runner    (1001) docker     (121)    12857 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/sagemaker/notebook_instance_lifecycle_configuration.py
+-rw-r--r--   0 runner    (1001) docker     (121)   178499 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/sagemaker/outputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    21418 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/sagemaker/project.py
+-rw-r--r--   0 runner    (1001) docker     (121)    19258 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/sagemaker/studio_lifecycle_config.py
+-rw-r--r--   0 runner    (1001) docker     (121)    26397 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/sagemaker/user_profile.py
+-rw-r--r--   0 runner    (1001) docker     (121)    22053 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/sagemaker/workforce.py
+-rw-r--r--   0 runner    (1001) docker     (121)    29220 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/sagemaker/workteam.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-24 22:23:25.000000 pulumi_aws-5.9.2/pulumi_aws/schemas/
+-rw-r--r--   0 runner    (1001) docker     (121)      341 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/schemas/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    14644 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/schemas/discoverer.py
+-rw-r--r--   0 runner    (1001) docker     (121)    14737 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/schemas/registry.py
+-rw-r--r--   0 runner    (1001) docker     (121)    25370 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/schemas/schema.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-24 22:23:25.000000 pulumi_aws-5.9.2/pulumi_aws/secretsmanager/
+-rw-r--r--   0 runner    (1001) docker     (121)      548 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/secretsmanager/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7257 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/secretsmanager/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)     8560 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/secretsmanager/get_secret.py
+-rw-r--r--   0 runner    (1001) docker     (121)     5714 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/secretsmanager/get_secret_rotation.py
+-rw-r--r--   0 runner    (1001) docker     (121)     8374 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/secretsmanager/get_secret_version.py
+-rw-r--r--   0 runner    (1001) docker     (121)     4313 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/secretsmanager/get_secrets.py
+-rw-r--r--   0 runner    (1001) docker     (121)     8608 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/secretsmanager/outputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    50501 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/secretsmanager/secret.py
+-rw-r--r--   0 runner    (1001) docker     (121)    14001 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/secretsmanager/secret_policy.py
+-rw-r--r--   0 runner    (1001) docker     (121)    19659 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/secretsmanager/secret_rotation.py
+-rw-r--r--   0 runner    (1001) docker     (121)    23497 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/secretsmanager/secret_version.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-24 22:23:25.000000 pulumi_aws-5.9.2/pulumi_aws/securityhub/
+-rw-r--r--   0 runner    (1001) docker     (121)      667 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/securityhub/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)   246761 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/securityhub/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)     4484 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/securityhub/account.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11710 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/securityhub/action_target.py
+-rw-r--r--   0 runner    (1001) docker     (121)    15675 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/securityhub/finding_aggregator.py
+-rw-r--r--   0 runner    (1001) docker     (121)    20675 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/securityhub/insight.py
+-rw-r--r--   0 runner    (1001) docker     (121)     9315 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/securityhub/invite_accepter.py
+-rw-r--r--   0 runner    (1001) docker     (121)    12819 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/securityhub/member.py
+-rw-r--r--   0 runner    (1001) docker     (121)     9301 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/securityhub/organization_admin_account.py
+-rw-r--r--   0 runner    (1001) docker     (121)     9382 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/securityhub/organization_configuration.py
+-rw-r--r--   0 runner    (1001) docker     (121)   200993 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/securityhub/outputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)     9436 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/securityhub/product_subscription.py
+-rw-r--r--   0 runner    (1001) docker     (121)    22477 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/securityhub/standards_control.py
+-rw-r--r--   0 runner    (1001) docker     (121)     8148 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/securityhub/standards_subscription.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-24 22:23:25.000000 pulumi_aws-5.9.2/pulumi_aws/serverlessrepository/
+-rw-r--r--   0 runner    (1001) docker     (121)      337 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/serverlessrepository/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    24180 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/serverlessrepository/cloud_formation_stack.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7312 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/serverlessrepository/get_application.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-24 22:23:25.000000 pulumi_aws-5.9.2/pulumi_aws/servicecatalog/
+-rw-r--r--   0 runner    (1001) docker     (121)      924 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/servicecatalog/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    22372 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/servicecatalog/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)     9093 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/servicecatalog/budget_resource_association.py
+-rw-r--r--   0 runner    (1001) docker     (121)    19923 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/servicecatalog/constraint.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6919 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/servicecatalog/get_constraint.py
+-rw-r--r--   0 runner    (1001) docker     (121)     4858 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/servicecatalog/get_launch_paths.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6304 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/servicecatalog/get_portfolio.py
+-rw-r--r--   0 runner    (1001) docker     (121)     5873 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/servicecatalog/get_portfolio_constraints.py
+-rw-r--r--   0 runner    (1001) docker     (121)     9831 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/servicecatalog/get_product.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7285 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/servicecatalog/organizations_access.py
+-rw-r--r--   0 runner    (1001) docker     (121)    26100 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/servicecatalog/outputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    16155 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/servicecatalog/portfolio.py
+-rw-r--r--   0 runner    (1001) docker     (121)    23923 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/servicecatalog/portfolio_share.py
+-rw-r--r--   0 runner    (1001) docker     (121)    14569 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/servicecatalog/principal_portfolio_association.py
+-rw-r--r--   0 runner    (1001) docker     (121)    38089 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/servicecatalog/product.py
+-rw-r--r--   0 runner    (1001) docker     (121)    13749 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/servicecatalog/product_portfolio_association.py
+-rw-r--r--   0 runner    (1001) docker     (121)    65881 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/servicecatalog/provisioned_product.py
+-rw-r--r--   0 runner    (1001) docker     (121)    34405 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/servicecatalog/provisioning_artifact.py
+-rw-r--r--   0 runner    (1001) docker     (121)    13526 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/servicecatalog/service_action.py
+-rw-r--r--   0 runner    (1001) docker     (121)    10181 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/servicecatalog/tag_option.py
+-rw-r--r--   0 runner    (1001) docker     (121)    13903 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/servicecatalog/tag_option_resource_association.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-24 22:23:25.000000 pulumi_aws-5.9.2/pulumi_aws/servicediscovery/
+-rw-r--r--   0 runner    (1001) docker     (121)      497 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/servicediscovery/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     8001 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/servicediscovery/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)     5107 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/servicediscovery/get_dns_namespace.py
+-rw-r--r--   0 runner    (1001) docker     (121)    13838 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/servicediscovery/http_namespace.py
+-rw-r--r--   0 runner    (1001) docker     (121)    15544 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/servicediscovery/instance.py
+-rw-r--r--   0 runner    (1001) docker     (121)     8408 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/servicediscovery/outputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    17538 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/servicediscovery/private_dns_namespace.py
+-rw-r--r--   0 runner    (1001) docker     (121)    15348 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/servicediscovery/public_dns_namespace.py
+-rw-r--r--   0 runner    (1001) docker     (121)    30763 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/servicediscovery/service.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-24 22:23:25.000000 pulumi_aws-5.9.2/pulumi_aws/servicequotas/
+-rw-r--r--   0 runner    (1001) docker     (121)      358 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/servicequotas/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     4464 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/servicequotas/get_service.py
+-rw-r--r--   0 runner    (1001) docker     (121)     9882 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/servicequotas/get_service_quota.py
+-rw-r--r--   0 runner    (1001) docker     (121)    22422 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/servicequotas/service_quota.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-24 22:23:25.000000 pulumi_aws-5.9.2/pulumi_aws/ses/
+-rw-r--r--   0 runner    (1001) docker     (121)      908 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ses/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    22779 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ses/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7180 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ses/active_receipt_rule_set.py
+-rw-r--r--   0 runner    (1001) docker     (121)    18187 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ses/confguration_set.py
+-rw-r--r--   0 runner    (1001) docker     (121)    18010 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ses/configuration_set.py
+-rw-r--r--   0 runner    (1001) docker     (121)    10825 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ses/domain_dkim.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11064 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ses/domain_identity.py
+-rw-r--r--   0 runner    (1001) docker     (121)     9163 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ses/domain_identity_verification.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7146 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ses/email_identity.py
+-rw-r--r--   0 runner    (1001) docker     (121)    26658 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ses/event_destination.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2833 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ses/get_active_receipt_rule_set.py
+-rw-r--r--   0 runner    (1001) docker     (121)     4024 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ses/get_domain_identity.py
+-rw-r--r--   0 runner    (1001) docker     (121)     3304 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ses/get_email_identity.py
+-rw-r--r--   0 runner    (1001) docker     (121)    16183 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ses/identity_notification_topic.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11507 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ses/identity_policy.py
+-rw-r--r--   0 runner    (1001) docker     (121)    16907 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ses/mail_from.py
+-rw-r--r--   0 runner    (1001) docker     (121)    24946 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ses/outputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    10445 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ses/receipt_filter.py
+-rw-r--r--   0 runner    (1001) docker     (121)    39512 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ses/receipt_rule.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7387 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ses/receipt_rule_set.py
+-rw-r--r--   0 runner    (1001) docker     (121)    14207 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ses/template.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-24 22:23:25.000000 pulumi_aws-5.9.2/pulumi_aws/sfn/
+-rw-r--r--   0 runner    (1001) docker     (121)      428 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/sfn/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     4052 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/sfn/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11641 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/sfn/activity.py
+-rw-r--r--   0 runner    (1001) docker     (121)     3936 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/sfn/get_activity.py
+-rw-r--r--   0 runner    (1001) docker     (121)     5485 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/sfn/get_state_machine.py
+-rw-r--r--   0 runner    (1001) docker     (121)     4040 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/sfn/outputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    35305 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/sfn/state_machine.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-24 22:23:25.000000 pulumi_aws-5.9.2/pulumi_aws/shield/
+-rw-r--r--   0 runner    (1001) docker     (121)      378 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/shield/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    15276 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/shield/protection.py
+-rw-r--r--   0 runner    (1001) docker     (121)    26892 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/shield/protection_group.py
+-rw-r--r--   0 runner    (1001) docker     (121)    13369 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/shield/protection_health_check_association.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-24 22:23:25.000000 pulumi_aws-5.9.2/pulumi_aws/signer/
+-rw-r--r--   0 runner    (1001) docker     (121)      480 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/signer/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    10765 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/signer/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11419 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/signer/get_signing_job.py
+-rw-r--r--   0 runner    (1001) docker     (121)     8285 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/signer/get_signing_profile.py
+-rw-r--r--   0 runner    (1001) docker     (121)    13451 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/signer/outputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    34380 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/signer/signing_job.py
+-rw-r--r--   0 runner    (1001) docker     (121)    27628 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/signer/signing_profile.py
+-rw-r--r--   0 runner    (1001) docker     (121)    21369 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/signer/signing_profile_permission.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-24 22:23:25.000000 pulumi_aws-5.9.2/pulumi_aws/simpledb/
+-rw-r--r--   0 runner    (1001) docker     (121)      291 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/simpledb/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     5920 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/simpledb/domain.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-24 22:23:25.000000 pulumi_aws-5.9.2/pulumi_aws/sns/
+-rw-r--r--   0 runner    (1001) docker     (121)      444 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/sns/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     3490 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/sns/get_topic.py
+-rw-r--r--   0 runner    (1001) docker     (121)    41542 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/sns/platform_application.py
+-rw-r--r--   0 runner    (1001) docker     (121)    20873 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/sns/sms_preferences.py
+-rw-r--r--   0 runner    (1001) docker     (121)    76362 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/sns/topic.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11817 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/sns/topic_policy.py
+-rw-r--r--   0 runner    (1001) docker     (121)    56986 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/sns/topic_subscription.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-24 22:23:25.000000 pulumi_aws-5.9.2/pulumi_aws/sqs/
+-rw-r--r--   0 runner    (1001) docker     (121)      343 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/sqs/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     4452 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/sqs/get_queue.py
+-rw-r--r--   0 runner    (1001) docker     (121)    70050 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/sqs/queue.py
+-rw-r--r--   0 runner    (1001) docker     (121)     9641 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/sqs/queue_policy.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-24 22:23:25.000000 pulumi_aws-5.9.2/pulumi_aws/ssm/
+-rw-r--r--   0 runner    (1001) docker     (121)      840 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ssm/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)      365 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ssm/_enums.py
+-rw-r--r--   0 runner    (1001) docker     (121)    52894 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ssm/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    26093 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ssm/activation.py
+-rw-r--r--   0 runner    (1001) docker     (121)    51231 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ssm/association.py
+-rw-r--r--   0 runner    (1001) docker     (121)    51296 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ssm/document.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6833 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ssm/get_document.py
+-rw-r--r--   0 runner    (1001) docker     (121)     3818 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ssm/get_instances.py
+-rw-r--r--   0 runner    (1001) docker     (121)     4075 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ssm/get_maintenance_windows.py
+-rw-r--r--   0 runner    (1001) docker     (121)     5382 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ssm/get_parameter.py
+-rw-r--r--   0 runner    (1001) docker     (121)     5793 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ssm/get_parameters_by_path.py
+-rw-r--r--   0 runner    (1001) docker     (121)    12661 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ssm/get_patch_baseline.py
+-rw-r--r--   0 runner    (1001) docker     (121)    35771 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ssm/maintenance_window.py
+-rw-r--r--   0 runner    (1001) docker     (121)    23617 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ssm/maintenance_window_target.py
+-rw-r--r--   0 runner    (1001) docker     (121)    45098 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ssm/maintenance_window_task.py
+-rw-r--r--   0 runner    (1001) docker     (121)    54527 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ssm/outputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    38705 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ssm/parameter.py
+-rw-r--r--   0 runner    (1001) docker     (121)    54960 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ssm/patch_baseline.py
+-rw-r--r--   0 runner    (1001) docker     (121)     8784 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ssm/patch_group.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11585 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ssm/resource_data_sync.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-24 22:23:25.000000 pulumi_aws-5.9.2/pulumi_aws/ssoadmin/
+-rw-r--r--   0 runner    (1001) docker     (121)      481 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ssoadmin/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    19159 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ssoadmin/account_assignment.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2764 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ssoadmin/get_instances.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6944 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ssoadmin/get_permission_set.py
+-rw-r--r--   0 runner    (1001) docker     (121)    14017 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ssoadmin/managed_policy_attachment.py
+-rw-r--r--   0 runner    (1001) docker     (121)    22725 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ssoadmin/permission_set.py
+-rw-r--r--   0 runner    (1001) docker     (121)    12519 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/ssoadmin/permission_set_inline_policy.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-24 22:23:25.000000 pulumi_aws-5.9.2/pulumi_aws/storagegateway/
+-rw-r--r--   0 runner    (1001) docker     (121)      642 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/storagegateway/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    18226 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/storagegateway/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)     9381 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/storagegateway/cache.py
+-rw-r--r--   0 runner    (1001) docker     (121)    43947 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/storagegateway/caches_iscsi_volume.py
+-rw-r--r--   0 runner    (1001) docker     (121)    31089 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/storagegateway/file_system_association.py
+-rw-r--r--   0 runner    (1001) docker     (121)    78466 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/storagegateway/gateway.py
+-rw-r--r--   0 runner    (1001) docker     (121)     5438 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/storagegateway/get_local_disk.py
+-rw-r--r--   0 runner    (1001) docker     (121)    65740 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/storagegateway/nfs_file_share.py
+-rw-r--r--   0 runner    (1001) docker     (121)    19732 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/storagegateway/outputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    82977 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/storagegateway/smb_file_share.py
+-rw-r--r--   0 runner    (1001) docker     (121)    45060 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/storagegateway/stored_iscsi_volume.py
+-rw-r--r--   0 runner    (1001) docker     (121)    24082 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/storagegateway/tape_pool.py
+-rw-r--r--   0 runner    (1001) docker     (121)    12892 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/storagegateway/upload_buffer.py
+-rw-r--r--   0 runner    (1001) docker     (121)     9675 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/storagegateway/working_storage.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-24 22:23:25.000000 pulumi_aws-5.9.2/pulumi_aws/swf/
+-rw-r--r--   0 runner    (1001) docker     (121)      291 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/swf/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    19773 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/swf/domain.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-24 22:23:25.000000 pulumi_aws-5.9.2/pulumi_aws/synthetics/
+-rw-r--r--   0 runner    (1001) docker     (121)      336 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/synthetics/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    14317 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/synthetics/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    60794 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/synthetics/canary.py
+-rw-r--r--   0 runner    (1001) docker     (121)    15261 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/synthetics/outputs.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-24 22:23:25.000000 pulumi_aws-5.9.2/pulumi_aws/timestreamwrite/
+-rw-r--r--   0 runner    (1001) docker     (121)      359 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/timestreamwrite/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     9470 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/timestreamwrite/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    18385 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/timestreamwrite/database.py
+-rw-r--r--   0 runner    (1001) docker     (121)    10690 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/timestreamwrite/outputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    23532 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/timestreamwrite/table.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-24 22:23:25.000000 pulumi_aws-5.9.2/pulumi_aws/transfer/
+-rw-r--r--   0 runner    (1001) docker     (121)      451 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/transfer/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    60059 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/transfer/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    29665 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/transfer/access.py
+-rw-r--r--   0 runner    (1001) docker     (121)     9138 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/transfer/get_server.py
+-rw-r--r--   0 runner    (1001) docker     (121)    60272 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/transfer/outputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    72742 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/transfer/server.py
+-rw-r--r--   0 runner    (1001) docker     (121)    13060 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/transfer/ssh_key.py
+-rw-r--r--   0 runner    (1001) docker     (121)    37669 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/transfer/user.py
+-rw-r--r--   0 runner    (1001) docker     (121)    17068 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/transfer/workflow.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-24 22:23:25.000000 pulumi_aws-5.9.2/pulumi_aws/waf/
+-rw-r--r--   0 runner    (1001) docker     (121)      773 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/waf/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    53462 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/waf/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11211 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/waf/byte_match_set.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11232 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/waf/geo_match_set.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2687 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/waf/get_ipset.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2949 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/waf/get_rate_based_rule.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2653 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/waf/get_rule.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2726 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/waf/get_web_acl.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11061 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/waf/ip_set.py
+-rw-r--r--   0 runner    (1001) docker     (121)    51941 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/waf/outputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    21914 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/waf/rate_based_rule.py
+-rw-r--r--   0 runner    (1001) docker     (121)    12201 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/waf/regex_match_set.py
+-rw-r--r--   0 runner    (1001) docker     (121)    10442 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/waf/regex_pattern_set.py
+-rw-r--r--   0 runner    (1001) docker     (121)    17601 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/waf/rule.py
+-rw-r--r--   0 runner    (1001) docker     (121)    17091 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/waf/rule_group.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11239 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/waf/size_constraint_set.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11514 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/waf/sql_injection_match_set.py
+-rw-r--r--   0 runner    (1001) docker     (121)    27078 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/waf/web_acl.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11423 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/waf/xss_match_set.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-24 22:23:25.000000 pulumi_aws-5.9.2/pulumi_aws/wafregional/
+-rw-r--r--   0 runner    (1001) docker     (121)      807 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/wafregional/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    45579 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/wafregional/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11217 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/wafregional/byte_match_set.py
+-rw-r--r--   0 runner    (1001) docker     (121)    10511 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/wafregional/geo_match_set.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2779 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/wafregional/get_ipset.py
+-rw-r--r--   0 runner    (1001) docker     (121)     3019 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/wafregional/get_rate_based_mod.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2745 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/wafregional/get_rule.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2818 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/wafregional/get_web_acl.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11263 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/wafregional/ip_set.py
+-rw-r--r--   0 runner    (1001) docker     (121)    44100 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/wafregional/outputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    22090 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/wafregional/rate_based_rule.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11456 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/wafregional/regex_match_set.py
+-rw-r--r--   0 runner    (1001) docker     (121)     9641 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/wafregional/regex_pattern_set.py
+-rw-r--r--   0 runner    (1001) docker     (121)    18253 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/wafregional/rule.py
+-rw-r--r--   0 runner    (1001) docker     (121)    17251 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/wafregional/rule_group.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11173 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/wafregional/size_constraint_set.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11680 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/wafregional/sql_injection_match_set.py
+-rw-r--r--   0 runner    (1001) docker     (121)    27836 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/wafregional/web_acl.py
+-rw-r--r--   0 runner    (1001) docker     (121)    17670 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/wafregional/web_acl_association.py
+-rw-r--r--   0 runner    (1001) docker     (121)    10508 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/wafregional/xss_match_set.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-24 22:23:25.000000 pulumi_aws-5.9.2/pulumi_aws/wafv2/
+-rw-r--r--   0 runner    (1001) docker     (121)      618 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/wafv2/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)  9094354 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/wafv2/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)     5790 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/wafv2/get_ip_set.py
+-rw-r--r--   0 runner    (1001) docker     (121)     5727 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/wafv2/get_regex_pattern_set.py
+-rw-r--r--   0 runner    (1001) docker     (121)     4768 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/wafv2/get_rule_group.py
+-rw-r--r--   0 runner    (1001) docker     (121)     4674 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/wafv2/get_web_acl.py
+-rw-r--r--   0 runner    (1001) docker     (121)    23504 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/wafv2/ip_set.py
+-rw-r--r--   0 runner    (1001) docker     (121)  8545270 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/wafv2/outputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    22942 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/wafv2/regex_pattern_set.py
+-rw-r--r--   0 runner    (1001) docker     (121)    57600 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/wafv2/rule_group.py
+-rw-r--r--   0 runner    (1001) docker     (121)    50144 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/wafv2/web_acl.py
+-rw-r--r--   0 runner    (1001) docker     (121)    14786 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/wafv2/web_acl_association.py
+-rw-r--r--   0 runner    (1001) docker     (121)    25303 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/wafv2/web_acl_logging_configuration.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-24 22:23:25.000000 pulumi_aws-5.9.2/pulumi_aws/worklink/
+-rw-r--r--   0 runner    (1001) docker     (121)      392 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/worklink/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     3692 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/worklink/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    28567 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/worklink/fleet.py
+-rw-r--r--   0 runner    (1001) docker     (121)     4019 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/worklink/outputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    12467 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/worklink/website_certificate_authority_association.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-24 22:23:25.000000 pulumi_aws-5.9.2/pulumi_aws/workspaces/
+-rw-r--r--   0 runner    (1001) docker     (121)      497 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/workspaces/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    21453 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/workspaces/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    45328 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/workspaces/directory.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7163 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/workspaces/get_bundle.py
+-rw-r--r--   0 runner    (1001) docker     (121)    12048 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/workspaces/get_directory.py
+-rw-r--r--   0 runner    (1001) docker     (121)     5449 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/workspaces/get_image.py
+-rw-r--r--   0 runner    (1001) docker     (121)    10781 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/workspaces/get_workspace.py
+-rw-r--r--   0 runner    (1001) docker     (121)    16204 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/workspaces/ip_group.py
+-rw-r--r--   0 runner    (1001) docker     (121)    35399 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/workspaces/outputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    31829 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/workspaces/workspace.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-24 22:23:25.000000 pulumi_aws-5.9.2/pulumi_aws/xray/
+-rw-r--r--   0 runner    (1001) docker     (121)      397 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/xray/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1845 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/xray/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    10614 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/xray/encryption_config.py
+-rw-r--r--   0 runner    (1001) docker     (121)    18341 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/xray/group.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2151 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/xray/outputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    36166 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/pulumi_aws/xray/sampling_rule.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-24 22:23:25.000000 pulumi_aws-5.9.2/pulumi_aws.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (121)    10151 2022-06-24 22:23:25.000000 pulumi_aws-5.9.2/pulumi_aws.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (121)    70754 2022-06-24 22:23:25.000000 pulumi_aws-5.9.2/pulumi_aws.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (121)        1 2022-06-24 22:23:25.000000 pulumi_aws-5.9.2/pulumi_aws.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (121)        1 2022-06-24 22:23:25.000000 pulumi_aws-5.9.2/pulumi_aws.egg-info/not-zip-safe
+-rw-r--r--   0 runner    (1001) docker     (121)       49 2022-06-24 22:23:25.000000 pulumi_aws-5.9.2/pulumi_aws.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (121)       11 2022-06-24 22:23:25.000000 pulumi_aws-5.9.2/pulumi_aws.egg-info/top_level.txt
+-rw-r--r--   0 runner    (1001) docker     (121)       38 2022-06-24 22:23:25.000000 pulumi_aws-5.9.2/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (121)     2082 2022-06-24 22:23:24.000000 pulumi_aws-5.9.2/setup.py
```

### Comparing `pulumi_aws-5.9.1/PKG-INFO` & `pulumi_aws-5.9.2/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: pulumi_aws
-Version: 5.9.1
+Version: 5.9.2
 Summary: A Pulumi package for creating and managing Amazon Web Services (AWS) cloud resources.
 Home-page: https://pulumi.io
 License: Apache-2.0
 Project-URL: Repository, https://github.com/pulumi/pulumi-aws
 Description: [![Actions Status](https://github.com/pulumi/pulumi-aws/workflows/master/badge.svg)](https://github.com/pulumi/pulumi-aws/actions)
         [![Slack](http://www.pulumi.com/images/docs/badges/slack.svg)](https://slack.pulumi.com)
         [![NPM version](https://badge.fury.io/js/%40pulumi%2Faws.svg)](https://www.npmjs.com/package/@pulumi/aws)
```

#### html2text {}

```diff
@@ -1,8 +1,8 @@
-Metadata-Version: 2.1 Name: pulumi_aws Version: 5.9.1 Summary: A Pulumi package
+Metadata-Version: 2.1 Name: pulumi_aws Version: 5.9.2 Summary: A Pulumi package
 for creating and managing Amazon Web Services (AWS) cloud resources. Home-page:
 https://pulumi.io License: Apache-2.0 Project-URL: Repository, https://
 github.com/pulumi/pulumi-aws Description: [![Actions Status](https://
 github.com/pulumi/pulumi-aws/workflows/master/badge.svg)](https://github.com/
 pulumi/pulumi-aws/actions) [![Slack](http://www.pulumi.com/images/docs/badges/
 slack.svg)](https://slack.pulumi.com) [![NPM version](https://badge.fury.io/js/
 %40pulumi%2Faws.svg)](https://www.npmjs.com/package/@pulumi/aws) [![Python
```

### Comparing `pulumi_aws-5.9.1/README.md` & `pulumi_aws-5.9.2/README.md`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/__init__.py` & `pulumi_aws-5.9.2/pulumi_aws/__init__.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/_enums.py` & `pulumi_aws-5.9.2/pulumi_aws/_enums.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/_inputs.py` & `pulumi_aws-5.9.2/pulumi_aws/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/_utilities.py` & `pulumi_aws-5.9.2/pulumi_aws/_utilities.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/accessanalyzer/analyzer.py` & `pulumi_aws-5.9.2/pulumi_aws/accessanalyzer/analyzer.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/account/alternative_contact.py` & `pulumi_aws-5.9.2/pulumi_aws/account/alternative_contact.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/acm/_inputs.py` & `pulumi_aws-5.9.2/pulumi_aws/acm/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/acm/certificate.py` & `pulumi_aws-5.9.2/pulumi_aws/acm/certificate.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/acm/certificate_validation.py` & `pulumi_aws-5.9.2/pulumi_aws/acm/certificate_validation.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/acm/get_certificate.py` & `pulumi_aws-5.9.2/pulumi_aws/acm/get_certificate.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/acm/outputs.py` & `pulumi_aws-5.9.2/pulumi_aws/acm/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/acmpca/__init__.py` & `pulumi_aws-5.9.2/pulumi_aws/acmpca/__init__.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/acmpca/_inputs.py` & `pulumi_aws-5.9.2/pulumi_aws/acmpca/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/acmpca/certificate.py` & `pulumi_aws-5.9.2/pulumi_aws/acmpca/certificate.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/acmpca/certificate_authority.py` & `pulumi_aws-5.9.2/pulumi_aws/acmpca/certificate_authority.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/acmpca/certificate_authority_certificate.py` & `pulumi_aws-5.9.2/pulumi_aws/acmpca/certificate_authority_certificate.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/acmpca/get_certificate.py` & `pulumi_aws-5.9.2/pulumi_aws/acmpca/get_certificate.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/acmpca/get_certificate_authority.py` & `pulumi_aws-5.9.2/pulumi_aws/acmpca/get_certificate_authority.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/acmpca/outputs.py` & `pulumi_aws-5.9.2/pulumi_aws/acmpca/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/acmpca/policy.py` & `pulumi_aws-5.9.2/pulumi_aws/acmpca/policy.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/alb/__init__.py` & `pulumi_aws-5.9.2/pulumi_aws/alb/__init__.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/alb/_inputs.py` & `pulumi_aws-5.9.2/pulumi_aws/alb/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/alb/get_listener.py` & `pulumi_aws-5.9.2/pulumi_aws/alb/get_listener.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/alb/get_load_balancer.py` & `pulumi_aws-5.9.2/pulumi_aws/alb/get_load_balancer.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/alb/get_target_group.py` & `pulumi_aws-5.9.2/pulumi_aws/alb/get_target_group.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/alb/listener.py` & `pulumi_aws-5.9.2/pulumi_aws/alb/listener.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/alb/listener_certificate.py` & `pulumi_aws-5.9.2/pulumi_aws/alb/listener_certificate.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/alb/listener_rule.py` & `pulumi_aws-5.9.2/pulumi_aws/alb/listener_rule.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/alb/load_balancer.py` & `pulumi_aws-5.9.2/pulumi_aws/alb/load_balancer.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/alb/outputs.py` & `pulumi_aws-5.9.2/pulumi_aws/alb/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/alb/target_group.py` & `pulumi_aws-5.9.2/pulumi_aws/alb/target_group.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/alb/target_group_attachment.py` & `pulumi_aws-5.9.2/pulumi_aws/alb/target_group_attachment.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/amp/alert_manager_definition.py` & `pulumi_aws-5.9.2/pulumi_aws/amp/alert_manager_definition.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/amp/rule_group_namespace.py` & `pulumi_aws-5.9.2/pulumi_aws/amp/rule_group_namespace.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/amp/workspace.py` & `pulumi_aws-5.9.2/pulumi_aws/amp/workspace.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/amplify/_inputs.py` & `pulumi_aws-5.9.2/pulumi_aws/amplify/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/amplify/app.py` & `pulumi_aws-5.9.2/pulumi_aws/amplify/app.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/amplify/backend_environment.py` & `pulumi_aws-5.9.2/pulumi_aws/amplify/backend_environment.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/amplify/branch.py` & `pulumi_aws-5.9.2/pulumi_aws/amplify/branch.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/amplify/domain_association.py` & `pulumi_aws-5.9.2/pulumi_aws/amplify/domain_association.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/amplify/outputs.py` & `pulumi_aws-5.9.2/pulumi_aws/amplify/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/amplify/webhook.py` & `pulumi_aws-5.9.2/pulumi_aws/amplify/webhook.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/apigateway/__init__.py` & `pulumi_aws-5.9.2/pulumi_aws/apigateway/__init__.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/apigateway/_inputs.py` & `pulumi_aws-5.9.2/pulumi_aws/apigateway/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/apigateway/account.py` & `pulumi_aws-5.9.2/pulumi_aws/apigateway/account.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/apigateway/api_key.py` & `pulumi_aws-5.9.2/pulumi_aws/apigateway/api_key.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/apigateway/authorizer.py` & `pulumi_aws-5.9.2/pulumi_aws/apigateway/authorizer.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/apigateway/base_path_mapping.py` & `pulumi_aws-5.9.2/pulumi_aws/apigateway/base_path_mapping.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/apigateway/client_certificate.py` & `pulumi_aws-5.9.2/pulumi_aws/apigateway/client_certificate.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/apigateway/deployment.py` & `pulumi_aws-5.9.2/pulumi_aws/apigateway/deployment.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/apigateway/documentation_part.py` & `pulumi_aws-5.9.2/pulumi_aws/apigateway/documentation_part.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/apigateway/documentation_version.py` & `pulumi_aws-5.9.2/pulumi_aws/apigateway/documentation_version.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/apigateway/domain_name.py` & `pulumi_aws-5.9.2/pulumi_aws/apigateway/domain_name.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/apigateway/get_domain_name.py` & `pulumi_aws-5.9.2/pulumi_aws/apigateway/get_domain_name.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/apigateway/get_export.py` & `pulumi_aws-5.9.2/pulumi_aws/apigateway/get_export.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/apigateway/get_key.py` & `pulumi_aws-5.9.2/pulumi_aws/apigateway/get_key.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/apigateway/get_resource.py` & `pulumi_aws-5.9.2/pulumi_aws/apigateway/get_resource.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/apigateway/get_rest_api.py` & `pulumi_aws-5.9.2/pulumi_aws/apigateway/get_rest_api.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/apigateway/get_sdk.py` & `pulumi_aws-5.9.2/pulumi_aws/apigateway/get_sdk.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/apigateway/get_vpc_link.py` & `pulumi_aws-5.9.2/pulumi_aws/apigateway/get_vpc_link.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/apigateway/integration.py` & `pulumi_aws-5.9.2/pulumi_aws/apigateway/integration.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/apigateway/integration_response.py` & `pulumi_aws-5.9.2/pulumi_aws/apigateway/integration_response.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/apigateway/method.py` & `pulumi_aws-5.9.2/pulumi_aws/apigateway/method.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/apigateway/method_response.py` & `pulumi_aws-5.9.2/pulumi_aws/apigateway/method_response.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/apigateway/method_settings.py` & `pulumi_aws-5.9.2/pulumi_aws/apigateway/method_settings.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/apigateway/model.py` & `pulumi_aws-5.9.2/pulumi_aws/apigateway/model.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/apigateway/outputs.py` & `pulumi_aws-5.9.2/pulumi_aws/apigateway/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/apigateway/request_validator.py` & `pulumi_aws-5.9.2/pulumi_aws/apigateway/request_validator.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/apigateway/resource.py` & `pulumi_aws-5.9.2/pulumi_aws/apigateway/resource.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/apigateway/response.py` & `pulumi_aws-5.9.2/pulumi_aws/apigateway/response.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/apigateway/rest_api.py` & `pulumi_aws-5.9.2/pulumi_aws/apigateway/rest_api.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/apigateway/rest_api_policy.py` & `pulumi_aws-5.9.2/pulumi_aws/apigateway/rest_api_policy.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/apigateway/stage.py` & `pulumi_aws-5.9.2/pulumi_aws/apigateway/stage.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/apigateway/usage_plan.py` & `pulumi_aws-5.9.2/pulumi_aws/apigateway/usage_plan.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/apigateway/usage_plan_key.py` & `pulumi_aws-5.9.2/pulumi_aws/apigateway/usage_plan_key.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/apigateway/vpc_link.py` & `pulumi_aws-5.9.2/pulumi_aws/apigateway/vpc_link.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/apigatewayv2/__init__.py` & `pulumi_aws-5.9.2/pulumi_aws/apigatewayv2/__init__.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/apigatewayv2/_inputs.py` & `pulumi_aws-5.9.2/pulumi_aws/apigatewayv2/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/apigatewayv2/api.py` & `pulumi_aws-5.9.2/pulumi_aws/apigatewayv2/api.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/apigatewayv2/api_mapping.py` & `pulumi_aws-5.9.2/pulumi_aws/apigatewayv2/api_mapping.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/apigatewayv2/authorizer.py` & `pulumi_aws-5.9.2/pulumi_aws/apigatewayv2/authorizer.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/apigatewayv2/deployment.py` & `pulumi_aws-5.9.2/pulumi_aws/apigatewayv2/deployment.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/apigatewayv2/domain_name.py` & `pulumi_aws-5.9.2/pulumi_aws/apigatewayv2/domain_name.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/apigatewayv2/get_api.py` & `pulumi_aws-5.9.2/pulumi_aws/apigatewayv2/get_api.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/apigatewayv2/get_apis.py` & `pulumi_aws-5.9.2/pulumi_aws/apigatewayv2/get_apis.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/apigatewayv2/get_export.py` & `pulumi_aws-5.9.2/pulumi_aws/apigatewayv2/get_export.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/apigatewayv2/integration.py` & `pulumi_aws-5.9.2/pulumi_aws/apigatewayv2/integration.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/apigatewayv2/integration_response.py` & `pulumi_aws-5.9.2/pulumi_aws/apigatewayv2/integration_response.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/apigatewayv2/model.py` & `pulumi_aws-5.9.2/pulumi_aws/apigatewayv2/model.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/apigatewayv2/outputs.py` & `pulumi_aws-5.9.2/pulumi_aws/apigatewayv2/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/apigatewayv2/route.py` & `pulumi_aws-5.9.2/pulumi_aws/apigatewayv2/route.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/apigatewayv2/route_response.py` & `pulumi_aws-5.9.2/pulumi_aws/apigatewayv2/route_response.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/apigatewayv2/stage.py` & `pulumi_aws-5.9.2/pulumi_aws/apigatewayv2/stage.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/apigatewayv2/vpc_link.py` & `pulumi_aws-5.9.2/pulumi_aws/apigatewayv2/vpc_link.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/appautoscaling/_inputs.py` & `pulumi_aws-5.9.2/pulumi_aws/appautoscaling/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/appautoscaling/outputs.py` & `pulumi_aws-5.9.2/pulumi_aws/appautoscaling/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/appautoscaling/policy.py` & `pulumi_aws-5.9.2/pulumi_aws/appautoscaling/policy.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/appautoscaling/scheduled_action.py` & `pulumi_aws-5.9.2/pulumi_aws/appautoscaling/scheduled_action.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/appautoscaling/target.py` & `pulumi_aws-5.9.2/pulumi_aws/appautoscaling/target.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/appconfig/__init__.py` & `pulumi_aws-5.9.2/pulumi_aws/appconfig/__init__.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/appconfig/_inputs.py` & `pulumi_aws-5.9.2/pulumi_aws/appconfig/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/appconfig/application.py` & `pulumi_aws-5.9.2/pulumi_aws/appconfig/application.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/appconfig/configuration_profile.py` & `pulumi_aws-5.9.2/pulumi_aws/appconfig/configuration_profile.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/appconfig/deployment.py` & `pulumi_aws-5.9.2/pulumi_aws/appconfig/deployment.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/appconfig/deployment_strategy.py` & `pulumi_aws-5.9.2/pulumi_aws/appconfig/deployment_strategy.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/appconfig/environment.py` & `pulumi_aws-5.9.2/pulumi_aws/appconfig/environment.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/appconfig/event_integration.py` & `pulumi_aws-5.9.2/pulumi_aws/appconfig/event_integration.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/appconfig/hosted_configuration_version.py` & `pulumi_aws-5.9.2/pulumi_aws/appconfig/hosted_configuration_version.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/appconfig/outputs.py` & `pulumi_aws-5.9.2/pulumi_aws/appconfig/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/appflow/_inputs.py` & `pulumi_aws-5.9.2/pulumi_aws/appflow/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/appflow/connector_profile.py` & `pulumi_aws-5.9.2/pulumi_aws/appflow/connector_profile.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/appflow/flow.py` & `pulumi_aws-5.9.2/pulumi_aws/appflow/flow.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/appflow/outputs.py` & `pulumi_aws-5.9.2/pulumi_aws/appflow/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/applicationloadbalancing/__init__.py` & `pulumi_aws-5.9.2/pulumi_aws/applicationloadbalancing/__init__.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/applicationloadbalancing/_inputs.py` & `pulumi_aws-5.9.2/pulumi_aws/applicationloadbalancing/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/applicationloadbalancing/get_listener.py` & `pulumi_aws-5.9.2/pulumi_aws/applicationloadbalancing/get_listener.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/applicationloadbalancing/get_load_balancer.py` & `pulumi_aws-5.9.2/pulumi_aws/applicationloadbalancing/get_load_balancer.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/applicationloadbalancing/get_target_group.py` & `pulumi_aws-5.9.2/pulumi_aws/applicationloadbalancing/get_target_group.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/applicationloadbalancing/listener.py` & `pulumi_aws-5.9.2/pulumi_aws/applicationloadbalancing/listener.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/applicationloadbalancing/listener_certificate.py` & `pulumi_aws-5.9.2/pulumi_aws/applicationloadbalancing/listener_certificate.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/applicationloadbalancing/listener_rule.py` & `pulumi_aws-5.9.2/pulumi_aws/applicationloadbalancing/listener_rule.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/applicationloadbalancing/load_balancer.py` & `pulumi_aws-5.9.2/pulumi_aws/applicationloadbalancing/load_balancer.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/applicationloadbalancing/outputs.py` & `pulumi_aws-5.9.2/pulumi_aws/applicationloadbalancing/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/applicationloadbalancing/target_group.py` & `pulumi_aws-5.9.2/pulumi_aws/applicationloadbalancing/target_group.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/applicationloadbalancing/target_group_attachment.py` & `pulumi_aws-5.9.2/pulumi_aws/applicationloadbalancing/target_group_attachment.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/appmesh/__init__.py` & `pulumi_aws-5.9.2/pulumi_aws/appmesh/__init__.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/appmesh/_inputs.py` & `pulumi_aws-5.9.2/pulumi_aws/appmesh/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/appmesh/gateway_route.py` & `pulumi_aws-5.9.2/pulumi_aws/appmesh/gateway_route.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/appmesh/get_mesh.py` & `pulumi_aws-5.9.2/pulumi_aws/appmesh/get_mesh.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/appmesh/get_virtual_service.py` & `pulumi_aws-5.9.2/pulumi_aws/appmesh/get_virtual_service.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/appmesh/mesh.py` & `pulumi_aws-5.9.2/pulumi_aws/appmesh/mesh.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/appmesh/outputs.py` & `pulumi_aws-5.9.2/pulumi_aws/appmesh/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/appmesh/route.py` & `pulumi_aws-5.9.2/pulumi_aws/appmesh/route.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/appmesh/virtual_gateway.py` & `pulumi_aws-5.9.2/pulumi_aws/appmesh/virtual_gateway.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/appmesh/virtual_node.py` & `pulumi_aws-5.9.2/pulumi_aws/appmesh/virtual_node.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/appmesh/virtual_router.py` & `pulumi_aws-5.9.2/pulumi_aws/appmesh/virtual_router.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/appmesh/virtual_service.py` & `pulumi_aws-5.9.2/pulumi_aws/appmesh/virtual_service.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/apprunner/_inputs.py` & `pulumi_aws-5.9.2/pulumi_aws/apprunner/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/apprunner/auto_scaling_configuration_version.py` & `pulumi_aws-5.9.2/pulumi_aws/apprunner/auto_scaling_configuration_version.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/apprunner/connection.py` & `pulumi_aws-5.9.2/pulumi_aws/apprunner/connection.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/apprunner/custom_domain_association.py` & `pulumi_aws-5.9.2/pulumi_aws/apprunner/custom_domain_association.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/apprunner/outputs.py` & `pulumi_aws-5.9.2/pulumi_aws/apprunner/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/apprunner/service.py` & `pulumi_aws-5.9.2/pulumi_aws/apprunner/service.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/apprunner/vpc_connector.py` & `pulumi_aws-5.9.2/pulumi_aws/apprunner/vpc_connector.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/appstream/__init__.py` & `pulumi_aws-5.9.2/pulumi_aws/appstream/__init__.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/appstream/_inputs.py` & `pulumi_aws-5.9.2/pulumi_aws/appstream/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/appstream/directory_config.py` & `pulumi_aws-5.9.2/pulumi_aws/appstream/directory_config.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/appstream/fleet.py` & `pulumi_aws-5.9.2/pulumi_aws/appstream/fleet.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/appstream/fleet_stack_association.py` & `pulumi_aws-5.9.2/pulumi_aws/appstream/fleet_stack_association.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/appstream/image_builder.py` & `pulumi_aws-5.9.2/pulumi_aws/appstream/image_builder.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/appstream/outputs.py` & `pulumi_aws-5.9.2/pulumi_aws/appstream/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/appstream/stack.py` & `pulumi_aws-5.9.2/pulumi_aws/appstream/stack.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/appstream/user.py` & `pulumi_aws-5.9.2/pulumi_aws/appstream/user.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/appstream/user_stack_association.py` & `pulumi_aws-5.9.2/pulumi_aws/appstream/user_stack_association.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/appsync/__init__.py` & `pulumi_aws-5.9.2/pulumi_aws/appsync/__init__.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/appsync/_inputs.py` & `pulumi_aws-5.9.2/pulumi_aws/appsync/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/appsync/api_cache.py` & `pulumi_aws-5.9.2/pulumi_aws/appsync/api_cache.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/appsync/api_key.py` & `pulumi_aws-5.9.2/pulumi_aws/appsync/api_key.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/appsync/data_source.py` & `pulumi_aws-5.9.2/pulumi_aws/appsync/data_source.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/appsync/domain_name.py` & `pulumi_aws-5.9.2/pulumi_aws/appsync/domain_name.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/appsync/domain_name_api_association.py` & `pulumi_aws-5.9.2/pulumi_aws/appsync/domain_name_api_association.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/appsync/function.py` & `pulumi_aws-5.9.2/pulumi_aws/appsync/function.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/appsync/graph_ql_api.py` & `pulumi_aws-5.9.2/pulumi_aws/appsync/graph_ql_api.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/appsync/outputs.py` & `pulumi_aws-5.9.2/pulumi_aws/appsync/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/appsync/resolver.py` & `pulumi_aws-5.9.2/pulumi_aws/appsync/resolver.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/athena/_inputs.py` & `pulumi_aws-5.9.2/pulumi_aws/athena/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/athena/data_catalog.py` & `pulumi_aws-5.9.2/pulumi_aws/athena/data_catalog.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/athena/database.py` & `pulumi_aws-5.9.2/pulumi_aws/athena/database.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/athena/named_query.py` & `pulumi_aws-5.9.2/pulumi_aws/athena/named_query.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/athena/outputs.py` & `pulumi_aws-5.9.2/pulumi_aws/athena/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/athena/workgroup.py` & `pulumi_aws-5.9.2/pulumi_aws/athena/workgroup.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/autoscaling/__init__.py` & `pulumi_aws-5.9.2/pulumi_aws/autoscaling/__init__.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/autoscaling/_enums.py` & `pulumi_aws-5.9.2/pulumi_aws/autoscaling/_enums.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/autoscaling/_inputs.py` & `pulumi_aws-5.9.2/pulumi_aws/autoscaling/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/autoscaling/attachment.py` & `pulumi_aws-5.9.2/pulumi_aws/autoscaling/attachment.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/autoscaling/get_ami_ids.py` & `pulumi_aws-5.9.2/pulumi_aws/autoscaling/get_ami_ids.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/autoscaling/get_group.py` & `pulumi_aws-5.9.2/pulumi_aws/autoscaling/get_group.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/autoscaling/group.py` & `pulumi_aws-5.9.2/pulumi_aws/autoscaling/group.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/autoscaling/lifecycle_hook.py` & `pulumi_aws-5.9.2/pulumi_aws/autoscaling/lifecycle_hook.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/autoscaling/notification.py` & `pulumi_aws-5.9.2/pulumi_aws/autoscaling/notification.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/autoscaling/outputs.py` & `pulumi_aws-5.9.2/pulumi_aws/autoscaling/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/autoscaling/policy.py` & `pulumi_aws-5.9.2/pulumi_aws/autoscaling/policy.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/autoscaling/schedule.py` & `pulumi_aws-5.9.2/pulumi_aws/autoscaling/schedule.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/autoscaling/tag.py` & `pulumi_aws-5.9.2/pulumi_aws/autoscaling/tag.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/autoscalingplans/_inputs.py` & `pulumi_aws-5.9.2/pulumi_aws/autoscalingplans/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/autoscalingplans/outputs.py` & `pulumi_aws-5.9.2/pulumi_aws/autoscalingplans/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/autoscalingplans/scaling_plan.py` & `pulumi_aws-5.9.2/pulumi_aws/autoscalingplans/scaling_plan.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/backup/__init__.py` & `pulumi_aws-5.9.2/pulumi_aws/backup/__init__.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/backup/_inputs.py` & `pulumi_aws-5.9.2/pulumi_aws/backup/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/backup/framework.py` & `pulumi_aws-5.9.2/pulumi_aws/backup/framework.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/backup/get_framework.py` & `pulumi_aws-5.9.2/pulumi_aws/backup/get_framework.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/backup/get_plan.py` & `pulumi_aws-5.9.2/pulumi_aws/backup/get_plan.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/backup/get_report_plan.py` & `pulumi_aws-5.9.2/pulumi_aws/backup/get_report_plan.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/backup/get_selection.py` & `pulumi_aws-5.9.2/pulumi_aws/backup/get_selection.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/backup/get_vault.py` & `pulumi_aws-5.9.2/pulumi_aws/backup/get_vault.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/backup/global_settings.py` & `pulumi_aws-5.9.2/pulumi_aws/backup/global_settings.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/backup/outputs.py` & `pulumi_aws-5.9.2/pulumi_aws/backup/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/backup/plan.py` & `pulumi_aws-5.9.2/pulumi_aws/backup/plan.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/backup/region_settings.py` & `pulumi_aws-5.9.2/pulumi_aws/backup/region_settings.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/backup/report_plan.py` & `pulumi_aws-5.9.2/pulumi_aws/backup/report_plan.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/backup/selection.py` & `pulumi_aws-5.9.2/pulumi_aws/backup/selection.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/backup/vault.py` & `pulumi_aws-5.9.2/pulumi_aws/backup/vault.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/backup/vault_lock_configuration.py` & `pulumi_aws-5.9.2/pulumi_aws/backup/vault_lock_configuration.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/backup/vault_notifications.py` & `pulumi_aws-5.9.2/pulumi_aws/backup/vault_notifications.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/backup/vault_policy.py` & `pulumi_aws-5.9.2/pulumi_aws/backup/vault_policy.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/batch/__init__.py` & `pulumi_aws-5.9.2/pulumi_aws/batch/__init__.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/batch/_inputs.py` & `pulumi_aws-5.9.2/pulumi_aws/batch/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/batch/compute_environment.py` & `pulumi_aws-5.9.2/pulumi_aws/batch/compute_environment.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/batch/get_compute_environment.py` & `pulumi_aws-5.9.2/pulumi_aws/batch/get_compute_environment.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/batch/get_job_queue.py` & `pulumi_aws-5.9.2/pulumi_aws/batch/get_job_queue.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/batch/get_scheduling_policy.py` & `pulumi_aws-5.9.2/pulumi_aws/batch/get_scheduling_policy.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/batch/job_definition.py` & `pulumi_aws-5.9.2/pulumi_aws/batch/job_definition.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/batch/job_queue.py` & `pulumi_aws-5.9.2/pulumi_aws/batch/job_queue.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/batch/outputs.py` & `pulumi_aws-5.9.2/pulumi_aws/batch/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/batch/scheduling_policy.py` & `pulumi_aws-5.9.2/pulumi_aws/batch/scheduling_policy.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/budgets/_inputs.py` & `pulumi_aws-5.9.2/pulumi_aws/budgets/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/budgets/budget.py` & `pulumi_aws-5.9.2/pulumi_aws/budgets/budget.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/budgets/budget_action.py` & `pulumi_aws-5.9.2/pulumi_aws/budgets/budget_action.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/budgets/outputs.py` & `pulumi_aws-5.9.2/pulumi_aws/budgets/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/cfg/__init__.py` & `pulumi_aws-5.9.2/pulumi_aws/cfg/__init__.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/cfg/_inputs.py` & `pulumi_aws-5.9.2/pulumi_aws/cfg/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/cfg/aggregate_authorization.py` & `pulumi_aws-5.9.2/pulumi_aws/cfg/aggregate_authorization.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/cfg/configuration_aggregator.py` & `pulumi_aws-5.9.2/pulumi_aws/cfg/configuration_aggregator.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/cfg/conformance_pack.py` & `pulumi_aws-5.9.2/pulumi_aws/cfg/conformance_pack.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/cfg/delivery_channel.py` & `pulumi_aws-5.9.2/pulumi_aws/cfg/delivery_channel.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/cfg/organization_conformance_pack.py` & `pulumi_aws-5.9.2/pulumi_aws/cfg/organization_conformance_pack.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/cfg/organization_custom_rule.py` & `pulumi_aws-5.9.2/pulumi_aws/cfg/organization_custom_rule.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/cfg/organization_managed_rule.py` & `pulumi_aws-5.9.2/pulumi_aws/cfg/organization_managed_rule.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/cfg/outputs.py` & `pulumi_aws-5.9.2/pulumi_aws/cfg/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/cfg/recorder.py` & `pulumi_aws-5.9.2/pulumi_aws/cfg/recorder.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/cfg/recorder_status.py` & `pulumi_aws-5.9.2/pulumi_aws/cfg/recorder_status.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/cfg/remediation_configuration.py` & `pulumi_aws-5.9.2/pulumi_aws/cfg/remediation_configuration.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/cfg/rule.py` & `pulumi_aws-5.9.2/pulumi_aws/cfg/rule.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/chime/__init__.py` & `pulumi_aws-5.9.2/pulumi_aws/chime/__init__.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/chime/_inputs.py` & `pulumi_aws-5.9.2/pulumi_aws/chime/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/chime/outputs.py` & `pulumi_aws-5.9.2/pulumi_aws/chime/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/chime/voice_connector.py` & `pulumi_aws-5.9.2/pulumi_aws/chime/voice_connector.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/chime/voice_connector_group.py` & `pulumi_aws-5.9.2/pulumi_aws/chime/voice_connector_group.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/chime/voice_connector_logging.py` & `pulumi_aws-5.9.2/pulumi_aws/chime/voice_connector_logging.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/chime/voice_connector_organization.py` & `pulumi_aws-5.9.2/pulumi_aws/chime/voice_connector_organization.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/chime/voice_connector_streaming.py` & `pulumi_aws-5.9.2/pulumi_aws/chime/voice_connector_streaming.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/chime/voice_connector_termination.py` & `pulumi_aws-5.9.2/pulumi_aws/chime/voice_connector_termination.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/chime/voice_connector_termination_credentials.py` & `pulumi_aws-5.9.2/pulumi_aws/chime/voice_connector_termination_credentials.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/cloud9/environment_ec2.py` & `pulumi_aws-5.9.2/pulumi_aws/cloud9/environment_ec2.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/cloud9/environment_membership.py` & `pulumi_aws-5.9.2/pulumi_aws/cloud9/environment_membership.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/cloudcontrol/get_resource.py` & `pulumi_aws-5.9.2/pulumi_aws/cloudcontrol/get_resource.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/cloudcontrol/resource.py` & `pulumi_aws-5.9.2/pulumi_aws/cloudcontrol/resource.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/cloudformation/__init__.py` & `pulumi_aws-5.9.2/pulumi_aws/cloudformation/__init__.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/cloudformation/_inputs.py` & `pulumi_aws-5.9.2/pulumi_aws/cloudformation/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/cloudformation/cloud_formation_type.py` & `pulumi_aws-5.9.2/pulumi_aws/cloudformation/cloud_formation_type.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/cloudformation/get_cloud_formation_type.py` & `pulumi_aws-5.9.2/pulumi_aws/cloudformation/get_cloud_formation_type.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/cloudformation/get_export.py` & `pulumi_aws-5.9.2/pulumi_aws/cloudformation/get_export.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/cloudformation/get_stack.py` & `pulumi_aws-5.9.2/pulumi_aws/cloudformation/get_stack.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/cloudformation/outputs.py` & `pulumi_aws-5.9.2/pulumi_aws/cloudformation/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/cloudformation/stack.py` & `pulumi_aws-5.9.2/pulumi_aws/cloudformation/stack.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/cloudformation/stack_set.py` & `pulumi_aws-5.9.2/pulumi_aws/cloudformation/stack_set.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/cloudformation/stack_set_instance.py` & `pulumi_aws-5.9.2/pulumi_aws/cloudformation/stack_set_instance.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/cloudfront/__init__.py` & `pulumi_aws-5.9.2/pulumi_aws/cloudfront/__init__.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/cloudfront/_inputs.py` & `pulumi_aws-5.9.2/pulumi_aws/cloudfront/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/cloudfront/cache_policy.py` & `pulumi_aws-5.9.2/pulumi_aws/cloudfront/cache_policy.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/cloudfront/distribution.py` & `pulumi_aws-5.9.2/pulumi_aws/cloudfront/distribution.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/cloudfront/field_level_encryption_config.py` & `pulumi_aws-5.9.2/pulumi_aws/cloudfront/field_level_encryption_config.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/cloudfront/field_level_encryption_profile.py` & `pulumi_aws-5.9.2/pulumi_aws/cloudfront/field_level_encryption_profile.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/cloudfront/function.py` & `pulumi_aws-5.9.2/pulumi_aws/cloudfront/function.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/cloudfront/get_cache_policy.py` & `pulumi_aws-5.9.2/pulumi_aws/cloudfront/get_cache_policy.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/cloudfront/get_distribution.py` & `pulumi_aws-5.9.2/pulumi_aws/cloudfront/get_distribution.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/cloudfront/get_function.py` & `pulumi_aws-5.9.2/pulumi_aws/cloudfront/get_function.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/cloudfront/get_log_delivery_canonical_user_id.py` & `pulumi_aws-5.9.2/pulumi_aws/cloudfront/get_log_delivery_canonical_user_id.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/cloudfront/get_origin_access_identities.py` & `pulumi_aws-5.9.2/pulumi_aws/cloudfront/get_origin_access_identities.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/cloudfront/get_origin_access_identity.py` & `pulumi_aws-5.9.2/pulumi_aws/cloudfront/get_origin_access_identity.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/cloudfront/get_origin_request_policy.py` & `pulumi_aws-5.9.2/pulumi_aws/cloudfront/get_origin_request_policy.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/cloudfront/get_realtime_log_config.py` & `pulumi_aws-5.9.2/pulumi_aws/cloudfront/get_realtime_log_config.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/cloudfront/get_response_headers_policy.py` & `pulumi_aws-5.9.2/pulumi_aws/cloudfront/get_response_headers_policy.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/cloudfront/key_group.py` & `pulumi_aws-5.9.2/pulumi_aws/cloudfront/key_group.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/cloudfront/monitoring_subscription.py` & `pulumi_aws-5.9.2/pulumi_aws/cloudfront/monitoring_subscription.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/cloudfront/origin_access_identity.py` & `pulumi_aws-5.9.2/pulumi_aws/cloudfront/origin_access_identity.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/cloudfront/origin_request_policy.py` & `pulumi_aws-5.9.2/pulumi_aws/cloudfront/origin_request_policy.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/cloudfront/outputs.py` & `pulumi_aws-5.9.2/pulumi_aws/cloudfront/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/cloudfront/public_key.py` & `pulumi_aws-5.9.2/pulumi_aws/cloudfront/public_key.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/cloudfront/realtime_log_config.py` & `pulumi_aws-5.9.2/pulumi_aws/cloudfront/realtime_log_config.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/cloudfront/response_headers_policy.py` & `pulumi_aws-5.9.2/pulumi_aws/cloudfront/response_headers_policy.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/cloudhsmv2/_inputs.py` & `pulumi_aws-5.9.2/pulumi_aws/cloudhsmv2/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/cloudhsmv2/cluster.py` & `pulumi_aws-5.9.2/pulumi_aws/cloudhsmv2/cluster.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/cloudhsmv2/get_cluster.py` & `pulumi_aws-5.9.2/pulumi_aws/cloudhsmv2/get_cluster.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/cloudhsmv2/hsm.py` & `pulumi_aws-5.9.2/pulumi_aws/cloudhsmv2/hsm.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/cloudhsmv2/outputs.py` & `pulumi_aws-5.9.2/pulumi_aws/cloudhsmv2/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/cloudsearch/_inputs.py` & `pulumi_aws-5.9.2/pulumi_aws/cloudsearch/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/cloudsearch/domain.py` & `pulumi_aws-5.9.2/pulumi_aws/cloudsearch/domain.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/cloudsearch/domain_service_access_policy.py` & `pulumi_aws-5.9.2/pulumi_aws/cloudsearch/domain_service_access_policy.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/cloudsearch/outputs.py` & `pulumi_aws-5.9.2/pulumi_aws/cloudsearch/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/cloudtrail/_inputs.py` & `pulumi_aws-5.9.2/pulumi_aws/cloudtrail/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/cloudtrail/event_data_store.py` & `pulumi_aws-5.9.2/pulumi_aws/cloudtrail/event_data_store.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/cloudtrail/get_function.py` & `pulumi_aws-5.9.2/pulumi_aws/cloudtrail/get_function.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/cloudtrail/get_service_account.py` & `pulumi_aws-5.9.2/pulumi_aws/cloudtrail/get_service_account.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/cloudtrail/outputs.py` & `pulumi_aws-5.9.2/pulumi_aws/cloudtrail/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/cloudtrail/trail.py` & `pulumi_aws-5.9.2/pulumi_aws/cloudtrail/trail.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/cloudwatch/__init__.py` & `pulumi_aws-5.9.2/pulumi_aws/cloudwatch/__init__.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/cloudwatch/_inputs.py` & `pulumi_aws-5.9.2/pulumi_aws/cloudwatch/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/cloudwatch/composite_alarm.py` & `pulumi_aws-5.9.2/pulumi_aws/cloudwatch/composite_alarm.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/cloudwatch/dashboard.py` & `pulumi_aws-5.9.2/pulumi_aws/cloudwatch/dashboard.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/cloudwatch/event_api_destination.py` & `pulumi_aws-5.9.2/pulumi_aws/cloudwatch/event_api_destination.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/cloudwatch/event_archive.py` & `pulumi_aws-5.9.2/pulumi_aws/cloudwatch/event_archive.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/cloudwatch/event_bus.py` & `pulumi_aws-5.9.2/pulumi_aws/cloudwatch/event_bus.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/cloudwatch/event_bus_policy.py` & `pulumi_aws-5.9.2/pulumi_aws/cloudwatch/event_bus_policy.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/cloudwatch/event_connection.py` & `pulumi_aws-5.9.2/pulumi_aws/cloudwatch/event_connection.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/cloudwatch/event_permission.py` & `pulumi_aws-5.9.2/pulumi_aws/cloudwatch/event_permission.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/cloudwatch/event_rule.py` & `pulumi_aws-5.9.2/pulumi_aws/cloudwatch/event_rule.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/cloudwatch/event_target.py` & `pulumi_aws-5.9.2/pulumi_aws/cloudwatch/event_target.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/cloudwatch/get_event_bus.py` & `pulumi_aws-5.9.2/pulumi_aws/cloudwatch/get_event_bus.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/cloudwatch/get_event_connection.py` & `pulumi_aws-5.9.2/pulumi_aws/cloudwatch/get_event_connection.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/cloudwatch/get_event_source.py` & `pulumi_aws-5.9.2/pulumi_aws/cloudwatch/get_event_source.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/cloudwatch/get_log_group.py` & `pulumi_aws-5.9.2/pulumi_aws/cloudwatch/get_log_group.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/cloudwatch/get_log_groups.py` & `pulumi_aws-5.9.2/pulumi_aws/cloudwatch/get_log_groups.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/cloudwatch/log_destination.py` & `pulumi_aws-5.9.2/pulumi_aws/cloudwatch/log_destination.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/cloudwatch/log_destination_policy.py` & `pulumi_aws-5.9.2/pulumi_aws/cloudwatch/log_destination_policy.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/cloudwatch/log_group.py` & `pulumi_aws-5.9.2/pulumi_aws/cloudwatch/log_group.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/cloudwatch/log_metric_filter.py` & `pulumi_aws-5.9.2/pulumi_aws/cloudwatch/log_metric_filter.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/cloudwatch/log_resource_policy.py` & `pulumi_aws-5.9.2/pulumi_aws/cloudwatch/log_resource_policy.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/cloudwatch/log_stream.py` & `pulumi_aws-5.9.2/pulumi_aws/cloudwatch/log_stream.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/cloudwatch/log_subscription_filter.py` & `pulumi_aws-5.9.2/pulumi_aws/cloudwatch/log_subscription_filter.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/cloudwatch/metric_alarm.py` & `pulumi_aws-5.9.2/pulumi_aws/cloudwatch/metric_alarm.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/cloudwatch/metric_stream.py` & `pulumi_aws-5.9.2/pulumi_aws/cloudwatch/metric_stream.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/cloudwatch/outputs.py` & `pulumi_aws-5.9.2/pulumi_aws/cloudwatch/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/cloudwatch/query_definition.py` & `pulumi_aws-5.9.2/pulumi_aws/cloudwatch/query_definition.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/codeartifact/__init__.py` & `pulumi_aws-5.9.2/pulumi_aws/codeartifact/__init__.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/codeartifact/_inputs.py` & `pulumi_aws-5.9.2/pulumi_aws/codeartifact/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/codeartifact/domain.py` & `pulumi_aws-5.9.2/pulumi_aws/codeartifact/domain.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/codeartifact/domain_permissions.py` & `pulumi_aws-5.9.2/pulumi_aws/codeartifact/domain_permissions.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/codeartifact/get_authorization_token.py` & `pulumi_aws-5.9.2/pulumi_aws/codeartifact/get_authorization_token.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/codeartifact/get_repository_endpoint.py` & `pulumi_aws-5.9.2/pulumi_aws/codeartifact/get_repository_endpoint.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/codeartifact/outputs.py` & `pulumi_aws-5.9.2/pulumi_aws/codeartifact/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/codeartifact/repository.py` & `pulumi_aws-5.9.2/pulumi_aws/codeartifact/repository.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/codeartifact/repository_permissions_policy.py` & `pulumi_aws-5.9.2/pulumi_aws/codeartifact/repository_permissions_policy.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/codebuild/_inputs.py` & `pulumi_aws-5.9.2/pulumi_aws/codebuild/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/codebuild/outputs.py` & `pulumi_aws-5.9.2/pulumi_aws/codebuild/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/codebuild/project.py` & `pulumi_aws-5.9.2/pulumi_aws/codebuild/project.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/codebuild/report_group.py` & `pulumi_aws-5.9.2/pulumi_aws/codebuild/report_group.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/codebuild/resource_policy.py` & `pulumi_aws-5.9.2/pulumi_aws/codebuild/resource_policy.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/codebuild/source_credential.py` & `pulumi_aws-5.9.2/pulumi_aws/codebuild/source_credential.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/codebuild/webhook.py` & `pulumi_aws-5.9.2/pulumi_aws/codebuild/webhook.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/codecommit/__init__.py` & `pulumi_aws-5.9.2/pulumi_aws/codecommit/__init__.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/codecommit/_inputs.py` & `pulumi_aws-5.9.2/pulumi_aws/codecommit/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/codecommit/approval_rule_template.py` & `pulumi_aws-5.9.2/pulumi_aws/codecommit/approval_rule_template.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/codecommit/approval_rule_template_association.py` & `pulumi_aws-5.9.2/pulumi_aws/codecommit/approval_rule_template_association.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/codecommit/get_approval_rule_template.py` & `pulumi_aws-5.9.2/pulumi_aws/codecommit/get_approval_rule_template.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/codecommit/get_repository.py` & `pulumi_aws-5.9.2/pulumi_aws/codecommit/get_repository.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/codecommit/outputs.py` & `pulumi_aws-5.9.2/pulumi_aws/codecommit/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/codecommit/repository.py` & `pulumi_aws-5.9.2/pulumi_aws/codecommit/repository.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/codecommit/trigger.py` & `pulumi_aws-5.9.2/pulumi_aws/codecommit/trigger.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/codedeploy/_inputs.py` & `pulumi_aws-5.9.2/pulumi_aws/codedeploy/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/codedeploy/application.py` & `pulumi_aws-5.9.2/pulumi_aws/codedeploy/application.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/codedeploy/deployment_config.py` & `pulumi_aws-5.9.2/pulumi_aws/codedeploy/deployment_config.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/codedeploy/deployment_group.py` & `pulumi_aws-5.9.2/pulumi_aws/codedeploy/deployment_group.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/codedeploy/outputs.py` & `pulumi_aws-5.9.2/pulumi_aws/codedeploy/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/codepipeline/_inputs.py` & `pulumi_aws-5.9.2/pulumi_aws/codepipeline/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/codepipeline/outputs.py` & `pulumi_aws-5.9.2/pulumi_aws/codepipeline/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/codepipeline/pipeline.py` & `pulumi_aws-5.9.2/pulumi_aws/codepipeline/pipeline.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/codepipeline/webhook.py` & `pulumi_aws-5.9.2/pulumi_aws/codepipeline/webhook.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/codestarconnections/_inputs.py` & `pulumi_aws-5.9.2/pulumi_aws/codestarconnections/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/codestarconnections/connection.py` & `pulumi_aws-5.9.2/pulumi_aws/codestarconnections/connection.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/codestarconnections/get_connection.py` & `pulumi_aws-5.9.2/pulumi_aws/codestarconnections/get_connection.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/codestarconnections/host.py` & `pulumi_aws-5.9.2/pulumi_aws/codestarconnections/host.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/codestarconnections/outputs.py` & `pulumi_aws-5.9.2/pulumi_aws/codestarconnections/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/codestarnotifications/_inputs.py` & `pulumi_aws-5.9.2/pulumi_aws/codestarnotifications/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/codestarnotifications/notification_rule.py` & `pulumi_aws-5.9.2/pulumi_aws/codestarnotifications/notification_rule.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/codestarnotifications/outputs.py` & `pulumi_aws-5.9.2/pulumi_aws/codestarnotifications/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/cognito/__init__.py` & `pulumi_aws-5.9.2/pulumi_aws/cognito/__init__.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/cognito/_inputs.py` & `pulumi_aws-5.9.2/pulumi_aws/cognito/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/cognito/get_user_pool_client.py` & `pulumi_aws-5.9.2/pulumi_aws/cognito/get_user_pool_client.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/cognito/get_user_pool_clients.py` & `pulumi_aws-5.9.2/pulumi_aws/cognito/get_user_pool_clients.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/cognito/get_user_pool_signing_certificate.py` & `pulumi_aws-5.9.2/pulumi_aws/cognito/get_user_pool_signing_certificate.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/cognito/get_user_pools.py` & `pulumi_aws-5.9.2/pulumi_aws/cognito/get_user_pools.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/cognito/identity_pool.py` & `pulumi_aws-5.9.2/pulumi_aws/cognito/identity_pool.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/cognito/identity_pool_provider_principal_tag.py` & `pulumi_aws-5.9.2/pulumi_aws/cognito/identity_pool_provider_principal_tag.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/cognito/identity_pool_role_attachment.py` & `pulumi_aws-5.9.2/pulumi_aws/cognito/identity_pool_role_attachment.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/cognito/identity_provider.py` & `pulumi_aws-5.9.2/pulumi_aws/cognito/identity_provider.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/cognito/outputs.py` & `pulumi_aws-5.9.2/pulumi_aws/cognito/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/cognito/resource_server.py` & `pulumi_aws-5.9.2/pulumi_aws/cognito/resource_server.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/cognito/user.py` & `pulumi_aws-5.9.2/pulumi_aws/cognito/user.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/cognito/user_group.py` & `pulumi_aws-5.9.2/pulumi_aws/cognito/user_group.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/cognito/user_in_group.py` & `pulumi_aws-5.9.2/pulumi_aws/cognito/user_in_group.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/cognito/user_pool.py` & `pulumi_aws-5.9.2/pulumi_aws/cognito/user_pool.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/cognito/user_pool_client.py` & `pulumi_aws-5.9.2/pulumi_aws/cognito/user_pool_client.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/cognito/user_pool_domain.py` & `pulumi_aws-5.9.2/pulumi_aws/cognito/user_pool_domain.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/cognito/user_pool_ui_customization.py` & `pulumi_aws-5.9.2/pulumi_aws/cognito/user_pool_ui_customization.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/config/outputs.py` & `pulumi_aws-5.9.2/pulumi_aws/config/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/config/vars.py` & `pulumi_aws-5.9.2/pulumi_aws/config/vars.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/connect/__init__.py` & `pulumi_aws-5.9.2/pulumi_aws/connect/__init__.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/connect/_inputs.py` & `pulumi_aws-5.9.2/pulumi_aws/connect/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/connect/bot_association.py` & `pulumi_aws-5.9.2/pulumi_aws/connect/bot_association.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/connect/contact_flow.py` & `pulumi_aws-5.9.2/pulumi_aws/connect/contact_flow.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/connect/contact_flow_module.py` & `pulumi_aws-5.9.2/pulumi_aws/connect/contact_flow_module.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/connect/get_bot_association.py` & `pulumi_aws-5.9.2/pulumi_aws/connect/get_bot_association.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/connect/get_contact_flow.py` & `pulumi_aws-5.9.2/pulumi_aws/connect/get_contact_flow.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/connect/get_contact_flow_module.py` & `pulumi_aws-5.9.2/pulumi_aws/connect/get_contact_flow_module.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/connect/get_hours_of_operation.py` & `pulumi_aws-5.9.2/pulumi_aws/connect/get_hours_of_operation.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/connect/get_instance.py` & `pulumi_aws-5.9.2/pulumi_aws/connect/get_instance.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/connect/get_lambda_function_association.py` & `pulumi_aws-5.9.2/pulumi_aws/connect/get_lambda_function_association.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/connect/get_prompt.py` & `pulumi_aws-5.9.2/pulumi_aws/connect/get_prompt.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/connect/get_queue.py` & `pulumi_aws-5.9.2/pulumi_aws/connect/get_queue.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/connect/get_quick_connect.py` & `pulumi_aws-5.9.2/pulumi_aws/connect/get_quick_connect.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/connect/get_routing_profile.py` & `pulumi_aws-5.9.2/pulumi_aws/connect/get_routing_profile.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/connect/get_security_profile.py` & `pulumi_aws-5.9.2/pulumi_aws/connect/get_security_profile.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/connect/get_user_hierarchy_structure.py` & `pulumi_aws-5.9.2/pulumi_aws/connect/get_user_hierarchy_structure.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/connect/hours_of_operation.py` & `pulumi_aws-5.9.2/pulumi_aws/connect/hours_of_operation.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/connect/instance.py` & `pulumi_aws-5.9.2/pulumi_aws/connect/instance.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/connect/lambda_function_association.py` & `pulumi_aws-5.9.2/pulumi_aws/connect/lambda_function_association.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/connect/outputs.py` & `pulumi_aws-5.9.2/pulumi_aws/connect/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/connect/queue.py` & `pulumi_aws-5.9.2/pulumi_aws/connect/queue.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/connect/quick_connect.py` & `pulumi_aws-5.9.2/pulumi_aws/connect/quick_connect.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/connect/routing_profile.py` & `pulumi_aws-5.9.2/pulumi_aws/connect/routing_profile.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/connect/security_profile.py` & `pulumi_aws-5.9.2/pulumi_aws/connect/security_profile.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/connect/user_hierarchy_group.py` & `pulumi_aws-5.9.2/pulumi_aws/connect/user_hierarchy_group.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/connect/user_hierarchy_structure.py` & `pulumi_aws-5.9.2/pulumi_aws/connect/user_hierarchy_structure.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/costexplorer/_inputs.py` & `pulumi_aws-5.9.2/pulumi_aws/costexplorer/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/costexplorer/anomaly_monitor.py` & `pulumi_aws-5.9.2/pulumi_aws/costexplorer/anomaly_monitor.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/costexplorer/cost_category.py` & `pulumi_aws-5.9.2/pulumi_aws/costexplorer/cost_category.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/costexplorer/get_cost_category.py` & `pulumi_aws-5.9.2/pulumi_aws/costexplorer/get_cost_category.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/costexplorer/get_tags.py` & `pulumi_aws-5.9.2/pulumi_aws/costexplorer/get_tags.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/costexplorer/outputs.py` & `pulumi_aws-5.9.2/pulumi_aws/costexplorer/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/cur/get_report_definition.py` & `pulumi_aws-5.9.2/pulumi_aws/cur/get_report_definition.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/cur/report_definition.py` & `pulumi_aws-5.9.2/pulumi_aws/cur/report_definition.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/dataexchange/data_set.py` & `pulumi_aws-5.9.2/pulumi_aws/dataexchange/data_set.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/dataexchange/revision.py` & `pulumi_aws-5.9.2/pulumi_aws/dataexchange/revision.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/datapipeline/_inputs.py` & `pulumi_aws-5.9.2/pulumi_aws/datapipeline/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/datapipeline/get_pipeline.py` & `pulumi_aws-5.9.2/pulumi_aws/datapipeline/get_pipeline.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/datapipeline/get_pipeline_definition.py` & `pulumi_aws-5.9.2/pulumi_aws/datapipeline/get_pipeline_definition.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/datapipeline/outputs.py` & `pulumi_aws-5.9.2/pulumi_aws/datapipeline/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/datapipeline/pipeline.py` & `pulumi_aws-5.9.2/pulumi_aws/datapipeline/pipeline.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/datapipeline/pipeline_definition.py` & `pulumi_aws-5.9.2/pulumi_aws/datapipeline/pipeline_definition.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/datasync/__init__.py` & `pulumi_aws-5.9.2/pulumi_aws/datasync/__init__.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/datasync/_inputs.py` & `pulumi_aws-5.9.2/pulumi_aws/datasync/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/datasync/agent.py` & `pulumi_aws-5.9.2/pulumi_aws/datasync/agent.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/datasync/efs_location.py` & `pulumi_aws-5.9.2/pulumi_aws/datasync/efs_location.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/datasync/fsx_open_zfs_file_system.py` & `pulumi_aws-5.9.2/pulumi_aws/datasync/fsx_open_zfs_file_system.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/datasync/location_fsx_lustre.py` & `pulumi_aws-5.9.2/pulumi_aws/datasync/location_fsx_lustre.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/datasync/location_fsx_windows.py` & `pulumi_aws-5.9.2/pulumi_aws/datasync/location_fsx_windows.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/datasync/location_hdfs.py` & `pulumi_aws-5.9.2/pulumi_aws/datasync/location_hdfs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/datasync/location_smb.py` & `pulumi_aws-5.9.2/pulumi_aws/datasync/location_smb.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/datasync/nfs_location.py` & `pulumi_aws-5.9.2/pulumi_aws/datasync/nfs_location.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/datasync/outputs.py` & `pulumi_aws-5.9.2/pulumi_aws/datasync/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/datasync/s3_location.py` & `pulumi_aws-5.9.2/pulumi_aws/datasync/s3_location.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/datasync/task.py` & `pulumi_aws-5.9.2/pulumi_aws/datasync/task.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/dax/_inputs.py` & `pulumi_aws-5.9.2/pulumi_aws/dax/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/dax/cluster.py` & `pulumi_aws-5.9.2/pulumi_aws/dax/cluster.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/dax/outputs.py` & `pulumi_aws-5.9.2/pulumi_aws/dax/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/dax/parameter_group.py` & `pulumi_aws-5.9.2/pulumi_aws/dax/parameter_group.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/dax/subnet_group.py` & `pulumi_aws-5.9.2/pulumi_aws/dax/subnet_group.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/detective/graph.py` & `pulumi_aws-5.9.2/pulumi_aws/detective/graph.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/detective/invitation_accepter.py` & `pulumi_aws-5.9.2/pulumi_aws/detective/invitation_accepter.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/detective/member.py` & `pulumi_aws-5.9.2/pulumi_aws/detective/member.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/devicefarm/_inputs.py` & `pulumi_aws-5.9.2/pulumi_aws/devicefarm/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/devicefarm/device_pool.py` & `pulumi_aws-5.9.2/pulumi_aws/devicefarm/device_pool.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/devicefarm/instance_profile.py` & `pulumi_aws-5.9.2/pulumi_aws/devicefarm/instance_profile.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/devicefarm/network_profile.py` & `pulumi_aws-5.9.2/pulumi_aws/devicefarm/network_profile.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/devicefarm/outputs.py` & `pulumi_aws-5.9.2/pulumi_aws/devicefarm/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/devicefarm/project.py` & `pulumi_aws-5.9.2/pulumi_aws/devicefarm/project.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/devicefarm/test_grid_project.py` & `pulumi_aws-5.9.2/pulumi_aws/devicefarm/test_grid_project.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/devicefarm/upload.py` & `pulumi_aws-5.9.2/pulumi_aws/devicefarm/upload.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/directconnect/__init__.py` & `pulumi_aws-5.9.2/pulumi_aws/directconnect/__init__.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/directconnect/bgp_peer.py` & `pulumi_aws-5.9.2/pulumi_aws/directconnect/bgp_peer.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/directconnect/connection.py` & `pulumi_aws-5.9.2/pulumi_aws/directconnect/connection.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/directconnect/connection_association.py` & `pulumi_aws-5.9.2/pulumi_aws/directconnect/connection_association.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/directconnect/connection_confirmation.py` & `pulumi_aws-5.9.2/pulumi_aws/directconnect/connection_confirmation.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/directconnect/gateway.py` & `pulumi_aws-5.9.2/pulumi_aws/directconnect/gateway.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/directconnect/gateway_association.py` & `pulumi_aws-5.9.2/pulumi_aws/directconnect/gateway_association.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/directconnect/gateway_association_proposal.py` & `pulumi_aws-5.9.2/pulumi_aws/directconnect/gateway_association_proposal.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/directconnect/get_connection.py` & `pulumi_aws-5.9.2/pulumi_aws/directconnect/get_connection.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/directconnect/get_gateway.py` & `pulumi_aws-5.9.2/pulumi_aws/directconnect/get_gateway.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/directconnect/get_location.py` & `pulumi_aws-5.9.2/pulumi_aws/directconnect/get_location.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/directconnect/get_locations.py` & `pulumi_aws-5.9.2/pulumi_aws/directconnect/get_locations.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/directconnect/hosted_connection.py` & `pulumi_aws-5.9.2/pulumi_aws/directconnect/hosted_connection.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/directconnect/hosted_private_virtual_interface.py` & `pulumi_aws-5.9.2/pulumi_aws/directconnect/hosted_private_virtual_interface.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/directconnect/hosted_private_virtual_interface_accepter.py` & `pulumi_aws-5.9.2/pulumi_aws/directconnect/hosted_private_virtual_interface_accepter.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/directconnect/hosted_public_virtual_interface.py` & `pulumi_aws-5.9.2/pulumi_aws/directconnect/hosted_public_virtual_interface.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/directconnect/hosted_public_virtual_interface_accepter.py` & `pulumi_aws-5.9.2/pulumi_aws/directconnect/hosted_public_virtual_interface_accepter.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/directconnect/hosted_transit_virtual_interface.py` & `pulumi_aws-5.9.2/pulumi_aws/directconnect/hosted_transit_virtual_interface.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/directconnect/hosted_transit_virtual_interface_acceptor.py` & `pulumi_aws-5.9.2/pulumi_aws/directconnect/hosted_transit_virtual_interface_acceptor.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/directconnect/link_aggregation_group.py` & `pulumi_aws-5.9.2/pulumi_aws/directconnect/link_aggregation_group.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/directconnect/private_virtual_interface.py` & `pulumi_aws-5.9.2/pulumi_aws/directconnect/private_virtual_interface.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/directconnect/public_virtual_interface.py` & `pulumi_aws-5.9.2/pulumi_aws/directconnect/public_virtual_interface.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/directconnect/transit_virtual_interface.py` & `pulumi_aws-5.9.2/pulumi_aws/directconnect/transit_virtual_interface.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/directoryservice/_inputs.py` & `pulumi_aws-5.9.2/pulumi_aws/directoryservice/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/directoryservice/conditional_forwader.py` & `pulumi_aws-5.9.2/pulumi_aws/directoryservice/conditional_forwader.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/directoryservice/directory.py` & `pulumi_aws-5.9.2/pulumi_aws/directoryservice/directory.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/directoryservice/get_directory.py` & `pulumi_aws-5.9.2/pulumi_aws/directoryservice/get_directory.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/directoryservice/log_service.py` & `pulumi_aws-5.9.2/pulumi_aws/directoryservice/log_service.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/directoryservice/outputs.py` & `pulumi_aws-5.9.2/pulumi_aws/directoryservice/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/dlm/_inputs.py` & `pulumi_aws-5.9.2/pulumi_aws/dlm/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/dlm/lifecycle_policy.py` & `pulumi_aws-5.9.2/pulumi_aws/dlm/lifecycle_policy.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/dlm/outputs.py` & `pulumi_aws-5.9.2/pulumi_aws/dlm/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/dms/_inputs.py` & `pulumi_aws-5.9.2/pulumi_aws/dms/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/dms/certificate.py` & `pulumi_aws-5.9.2/pulumi_aws/dms/certificate.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/dms/endpoint.py` & `pulumi_aws-5.9.2/pulumi_aws/dms/endpoint.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/dms/event_subscription.py` & `pulumi_aws-5.9.2/pulumi_aws/dms/event_subscription.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/dms/outputs.py` & `pulumi_aws-5.9.2/pulumi_aws/dms/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/dms/replication_instance.py` & `pulumi_aws-5.9.2/pulumi_aws/dms/replication_instance.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/dms/replication_subnet_group.py` & `pulumi_aws-5.9.2/pulumi_aws/dms/replication_subnet_group.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/dms/replication_task.py` & `pulumi_aws-5.9.2/pulumi_aws/dms/replication_task.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/docdb/__init__.py` & `pulumi_aws-5.9.2/pulumi_aws/docdb/__init__.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/docdb/_inputs.py` & `pulumi_aws-5.9.2/pulumi_aws/docdb/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/docdb/cluster.py` & `pulumi_aws-5.9.2/pulumi_aws/docdb/cluster.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/docdb/cluster_instance.py` & `pulumi_aws-5.9.2/pulumi_aws/docdb/cluster_instance.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/docdb/cluster_parameter_group.py` & `pulumi_aws-5.9.2/pulumi_aws/docdb/cluster_parameter_group.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/docdb/cluster_snapshot.py` & `pulumi_aws-5.9.2/pulumi_aws/docdb/cluster_snapshot.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/docdb/event_subscription.py` & `pulumi_aws-5.9.2/pulumi_aws/docdb/event_subscription.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/docdb/get_engine_version.py` & `pulumi_aws-5.9.2/pulumi_aws/docdb/get_engine_version.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/docdb/get_orderable_db_instance.py` & `pulumi_aws-5.9.2/pulumi_aws/docdb/get_orderable_db_instance.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/docdb/global_cluster.py` & `pulumi_aws-5.9.2/pulumi_aws/docdb/global_cluster.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/docdb/outputs.py` & `pulumi_aws-5.9.2/pulumi_aws/docdb/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/docdb/subnet_group.py` & `pulumi_aws-5.9.2/pulumi_aws/docdb/subnet_group.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/dynamodb/__init__.py` & `pulumi_aws-5.9.2/pulumi_aws/dynamodb/__init__.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/dynamodb/_inputs.py` & `pulumi_aws-5.9.2/pulumi_aws/dynamodb/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/dynamodb/contributor_insights.py` & `pulumi_aws-5.9.2/pulumi_aws/dynamodb/contributor_insights.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/dynamodb/get_table.py` & `pulumi_aws-5.9.2/pulumi_aws/dynamodb/get_table.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/dynamodb/global_table.py` & `pulumi_aws-5.9.2/pulumi_aws/dynamodb/global_table.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/dynamodb/kinesis_streaming_destination.py` & `pulumi_aws-5.9.2/pulumi_aws/dynamodb/kinesis_streaming_destination.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/dynamodb/outputs.py` & `pulumi_aws-5.9.2/pulumi_aws/dynamodb/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/dynamodb/table.py` & `pulumi_aws-5.9.2/pulumi_aws/dynamodb/table.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/dynamodb/table_item.py` & `pulumi_aws-5.9.2/pulumi_aws/dynamodb/table_item.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/dynamodb/tag.py` & `pulumi_aws-5.9.2/pulumi_aws/dynamodb/tag.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ebs/__init__.py` & `pulumi_aws-5.9.2/pulumi_aws/ebs/__init__.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ebs/_inputs.py` & `pulumi_aws-5.9.2/pulumi_aws/ebs/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ebs/default_kms_key.py` & `pulumi_aws-5.9.2/pulumi_aws/ebs/default_kms_key.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ebs/encryption_by_default.py` & `pulumi_aws-5.9.2/pulumi_aws/ebs/encryption_by_default.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ebs/get_default_kms_key.py` & `pulumi_aws-5.9.2/pulumi_aws/ebs/get_default_kms_key.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ebs/get_ebs_volumes.py` & `pulumi_aws-5.9.2/pulumi_aws/ebs/get_ebs_volumes.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ebs/get_encryption_by_default.py` & `pulumi_aws-5.9.2/pulumi_aws/ebs/get_encryption_by_default.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ebs/get_snapshot.py` & `pulumi_aws-5.9.2/pulumi_aws/ebs/get_snapshot.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ebs/get_snapshot_ids.py` & `pulumi_aws-5.9.2/pulumi_aws/ebs/get_snapshot_ids.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ebs/get_volume.py` & `pulumi_aws-5.9.2/pulumi_aws/ebs/get_volume.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ebs/outputs.py` & `pulumi_aws-5.9.2/pulumi_aws/ebs/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ebs/snapshot.py` & `pulumi_aws-5.9.2/pulumi_aws/ebs/snapshot.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ebs/snapshot_copy.py` & `pulumi_aws-5.9.2/pulumi_aws/ebs/snapshot_copy.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ebs/snapshot_import.py` & `pulumi_aws-5.9.2/pulumi_aws/ebs/snapshot_import.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ebs/volume.py` & `pulumi_aws-5.9.2/pulumi_aws/ebs/volume.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ec2/__init__.py` & `pulumi_aws-5.9.2/pulumi_aws/ec2/__init__.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ec2/_enums.py` & `pulumi_aws-5.9.2/pulumi_aws/ec2/_enums.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ec2/_inputs.py` & `pulumi_aws-5.9.2/pulumi_aws/ec2/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ec2/ami.py` & `pulumi_aws-5.9.2/pulumi_aws/ec2/ami.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ec2/ami_copy.py` & `pulumi_aws-5.9.2/pulumi_aws/ec2/ami_copy.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ec2/ami_from_instance.py` & `pulumi_aws-5.9.2/pulumi_aws/ec2/ami_from_instance.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ec2/ami_launch_permission.py` & `pulumi_aws-5.9.2/pulumi_aws/ec2/ami_launch_permission.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ec2/availability_zone_group.py` & `pulumi_aws-5.9.2/pulumi_aws/ec2/availability_zone_group.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ec2/capacity_reservation.py` & `pulumi_aws-5.9.2/pulumi_aws/ec2/capacity_reservation.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ec2/carrier_gateway.py` & `pulumi_aws-5.9.2/pulumi_aws/ec2/carrier_gateway.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ec2/customer_gateway.py` & `pulumi_aws-5.9.2/pulumi_aws/ec2/customer_gateway.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ec2/dedicated_host.py` & `pulumi_aws-5.9.2/pulumi_aws/ec2/dedicated_host.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ec2/default_network_acl.py` & `pulumi_aws-5.9.2/pulumi_aws/ec2/default_network_acl.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ec2/default_route_table.py` & `pulumi_aws-5.9.2/pulumi_aws/ec2/default_route_table.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ec2/default_security_group.py` & `pulumi_aws-5.9.2/pulumi_aws/ec2/default_security_group.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ec2/default_subnet.py` & `pulumi_aws-5.9.2/pulumi_aws/ec2/default_subnet.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ec2/default_vpc.py` & `pulumi_aws-5.9.2/pulumi_aws/ec2/default_vpc.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ec2/default_vpc_dhcp_options.py` & `pulumi_aws-5.9.2/pulumi_aws/ec2/default_vpc_dhcp_options.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ec2/egress_only_internet_gateway.py` & `pulumi_aws-5.9.2/pulumi_aws/ec2/egress_only_internet_gateway.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ec2/eip.py` & `pulumi_aws-5.9.2/pulumi_aws/ec2/eip.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ec2/eip_association.py` & `pulumi_aws-5.9.2/pulumi_aws/ec2/eip_association.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ec2/fleet.py` & `pulumi_aws-5.9.2/pulumi_aws/ec2/fleet.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ec2/flow_log.py` & `pulumi_aws-5.9.2/pulumi_aws/ec2/flow_log.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ec2/get_ami.py` & `pulumi_aws-5.9.2/pulumi_aws/ec2/get_ami.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ec2/get_ami_ids.py` & `pulumi_aws-5.9.2/pulumi_aws/ec2/get_ami_ids.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ec2/get_coip_pool.py` & `pulumi_aws-5.9.2/pulumi_aws/ec2/get_coip_pool.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ec2/get_coip_pools.py` & `pulumi_aws-5.9.2/pulumi_aws/ec2/get_coip_pools.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ec2/get_customer_gateway.py` & `pulumi_aws-5.9.2/pulumi_aws/ec2/get_customer_gateway.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ec2/get_dedicated_host.py` & `pulumi_aws-5.9.2/pulumi_aws/ec2/get_dedicated_host.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ec2/get_eips.py` & `pulumi_aws-5.9.2/pulumi_aws/ec2/get_eips.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ec2/get_elastic_ip.py` & `pulumi_aws-5.9.2/pulumi_aws/ec2/get_elastic_ip.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ec2/get_instance.py` & `pulumi_aws-5.9.2/pulumi_aws/ec2/get_instance.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ec2/get_instance_type.py` & `pulumi_aws-5.9.2/pulumi_aws/ec2/get_instance_type.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ec2/get_instance_type_offering.py` & `pulumi_aws-5.9.2/pulumi_aws/ec2/get_instance_type_offering.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ec2/get_instance_type_offerings.py` & `pulumi_aws-5.9.2/pulumi_aws/ec2/get_instance_type_offerings.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ec2/get_instance_types.py` & `pulumi_aws-5.9.2/pulumi_aws/ec2/get_instance_types.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ec2/get_instances.py` & `pulumi_aws-5.9.2/pulumi_aws/ec2/get_instances.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ec2/get_internet_gateway.py` & `pulumi_aws-5.9.2/pulumi_aws/ec2/get_internet_gateway.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ec2/get_ipam_preview_next_cidr.py` & `pulumi_aws-5.9.2/pulumi_aws/ec2/get_ipam_preview_next_cidr.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ec2/get_key_pair.py` & `pulumi_aws-5.9.2/pulumi_aws/ec2/get_key_pair.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ec2/get_launch_configuration.py` & `pulumi_aws-5.9.2/pulumi_aws/ec2/get_launch_configuration.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ec2/get_launch_template.py` & `pulumi_aws-5.9.2/pulumi_aws/ec2/get_launch_template.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ec2/get_local_gateway.py` & `pulumi_aws-5.9.2/pulumi_aws/ec2/get_local_gateway.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ec2/get_local_gateway_route_table.py` & `pulumi_aws-5.9.2/pulumi_aws/ec2/get_local_gateway_route_table.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ec2/get_local_gateway_route_tables.py` & `pulumi_aws-5.9.2/pulumi_aws/ec2/get_local_gateway_route_tables.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ec2/get_local_gateway_virtual_interface.py` & `pulumi_aws-5.9.2/pulumi_aws/ec2/get_local_gateway_virtual_interface.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ec2/get_local_gateway_virtual_interface_group.py` & `pulumi_aws-5.9.2/pulumi_aws/ec2/get_local_gateway_virtual_interface_group.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ec2/get_local_gateway_virtual_interface_groups.py` & `pulumi_aws-5.9.2/pulumi_aws/ec2/get_local_gateway_virtual_interface_groups.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ec2/get_local_gateways.py` & `pulumi_aws-5.9.2/pulumi_aws/ec2/get_local_gateways.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ec2/get_managed_prefix_list.py` & `pulumi_aws-5.9.2/pulumi_aws/ec2/get_managed_prefix_list.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ec2/get_nat_gateway.py` & `pulumi_aws-5.9.2/pulumi_aws/ec2/get_nat_gateway.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ec2/get_nat_gateways.py` & `pulumi_aws-5.9.2/pulumi_aws/ec2/get_nat_gateways.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ec2/get_network_acls.py` & `pulumi_aws-5.9.2/pulumi_aws/ec2/get_network_acls.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ec2/get_network_interface.py` & `pulumi_aws-5.9.2/pulumi_aws/ec2/get_network_interface.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ec2/get_network_interfaces.py` & `pulumi_aws-5.9.2/pulumi_aws/ec2/get_network_interfaces.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ec2/get_prefix_list.py` & `pulumi_aws-5.9.2/pulumi_aws/ec2/get_prefix_list.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ec2/get_route.py` & `pulumi_aws-5.9.2/pulumi_aws/ec2/get_route.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ec2/get_route_table.py` & `pulumi_aws-5.9.2/pulumi_aws/ec2/get_route_table.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ec2/get_route_tables.py` & `pulumi_aws-5.9.2/pulumi_aws/ec2/get_route_tables.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ec2/get_security_group.py` & `pulumi_aws-5.9.2/pulumi_aws/ec2/get_security_group.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ec2/get_security_groups.py` & `pulumi_aws-5.9.2/pulumi_aws/ec2/get_security_groups.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ec2/get_serial_console_access.py` & `pulumi_aws-5.9.2/pulumi_aws/ec2/get_serial_console_access.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ec2/get_spot_price.py` & `pulumi_aws-5.9.2/pulumi_aws/ec2/get_spot_price.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ec2/get_subnet.py` & `pulumi_aws-5.9.2/pulumi_aws/ec2/get_subnet.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ec2/get_subnet_ids.py` & `pulumi_aws-5.9.2/pulumi_aws/ec2/get_subnet_ids.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ec2/get_subnets.py` & `pulumi_aws-5.9.2/pulumi_aws/ec2/get_subnets.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ec2/get_transit_gateway_route_tables.py` & `pulumi_aws-5.9.2/pulumi_aws/ec2/get_transit_gateway_route_tables.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ec2/get_vpc.py` & `pulumi_aws-5.9.2/pulumi_aws/ec2/get_vpc.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ec2/get_vpc_dhcp_options.py` & `pulumi_aws-5.9.2/pulumi_aws/ec2/get_vpc_dhcp_options.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ec2/get_vpc_endpoint.py` & `pulumi_aws-5.9.2/pulumi_aws/ec2/get_vpc_endpoint.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ec2/get_vpc_endpoint_service.py` & `pulumi_aws-5.9.2/pulumi_aws/ec2/get_vpc_endpoint_service.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ec2/get_vpc_iam_pool.py` & `pulumi_aws-5.9.2/pulumi_aws/ec2/get_vpc_iam_pool.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ec2/get_vpc_peering_connection.py` & `pulumi_aws-5.9.2/pulumi_aws/ec2/get_vpc_peering_connection.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ec2/get_vpc_peering_connections.py` & `pulumi_aws-5.9.2/pulumi_aws/ec2/get_vpc_peering_connections.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ec2/get_vpcs.py` & `pulumi_aws-5.9.2/pulumi_aws/ec2/get_vpcs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ec2/get_vpn_gateway.py` & `pulumi_aws-5.9.2/pulumi_aws/ec2/get_vpn_gateway.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ec2/instance.py` & `pulumi_aws-5.9.2/pulumi_aws/ec2/instance.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ec2/internet_gateway.py` & `pulumi_aws-5.9.2/pulumi_aws/ec2/internet_gateway.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ec2/internet_gateway_attachment.py` & `pulumi_aws-5.9.2/pulumi_aws/ec2/internet_gateway_attachment.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ec2/key_pair.py` & `pulumi_aws-5.9.2/pulumi_aws/ec2/key_pair.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ec2/launch_configuration.py` & `pulumi_aws-5.9.2/pulumi_aws/ec2/launch_configuration.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ec2/launch_template.py` & `pulumi_aws-5.9.2/pulumi_aws/ec2/launch_template.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ec2/local_gateway_route.py` & `pulumi_aws-5.9.2/pulumi_aws/ec2/local_gateway_route.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ec2/local_gateway_route_table_vpc_association.py` & `pulumi_aws-5.9.2/pulumi_aws/ec2/local_gateway_route_table_vpc_association.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ec2/main_route_table_association.py` & `pulumi_aws-5.9.2/pulumi_aws/ec2/main_route_table_association.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ec2/managed_prefix_list.py` & `pulumi_aws-5.9.2/pulumi_aws/ec2/managed_prefix_list.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ec2/managed_prefix_list_entry.py` & `pulumi_aws-5.9.2/pulumi_aws/ec2/managed_prefix_list_entry.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ec2/nat_gateway.py` & `pulumi_aws-5.9.2/pulumi_aws/ec2/nat_gateway.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ec2/network_acl.py` & `pulumi_aws-5.9.2/pulumi_aws/ec2/network_acl.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ec2/network_acl_association.py` & `pulumi_aws-5.9.2/pulumi_aws/ec2/network_acl_association.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ec2/network_acl_rule.py` & `pulumi_aws-5.9.2/pulumi_aws/ec2/network_acl_rule.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ec2/network_insights_path.py` & `pulumi_aws-5.9.2/pulumi_aws/ec2/network_insights_path.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ec2/network_interface.py` & `pulumi_aws-5.9.2/pulumi_aws/ec2/network_interface.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ec2/network_interface_attachment.py` & `pulumi_aws-5.9.2/pulumi_aws/ec2/network_interface_attachment.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ec2/network_interface_security_group_attachment.py` & `pulumi_aws-5.9.2/pulumi_aws/ec2/network_interface_security_group_attachment.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ec2/outputs.py` & `pulumi_aws-5.9.2/pulumi_aws/ec2/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ec2/peering_connection_options.py` & `pulumi_aws-5.9.2/pulumi_aws/ec2/peering_connection_options.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ec2/placement_group.py` & `pulumi_aws-5.9.2/pulumi_aws/ec2/placement_group.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ec2/proxy_protocol_policy.py` & `pulumi_aws-5.9.2/pulumi_aws/ec2/proxy_protocol_policy.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ec2/route.py` & `pulumi_aws-5.9.2/pulumi_aws/ec2/route.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ec2/route_table.py` & `pulumi_aws-5.9.2/pulumi_aws/ec2/route_table.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ec2/route_table_association.py` & `pulumi_aws-5.9.2/pulumi_aws/ec2/route_table_association.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ec2/security_group.py` & `pulumi_aws-5.9.2/pulumi_aws/ec2/security_group.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ec2/security_group_association.py` & `pulumi_aws-5.9.2/pulumi_aws/ec2/security_group_association.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ec2/security_group_rule.py` & `pulumi_aws-5.9.2/pulumi_aws/ec2/security_group_rule.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ec2/serial_console_access.py` & `pulumi_aws-5.9.2/pulumi_aws/ec2/serial_console_access.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ec2/snapshot_create_volume_permission.py` & `pulumi_aws-5.9.2/pulumi_aws/ec2/snapshot_create_volume_permission.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ec2/spot_datafeed_subscription.py` & `pulumi_aws-5.9.2/pulumi_aws/ec2/spot_datafeed_subscription.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ec2/spot_fleet_request.py` & `pulumi_aws-5.9.2/pulumi_aws/ec2/spot_fleet_request.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ec2/spot_instance_request.py` & `pulumi_aws-5.9.2/pulumi_aws/ec2/spot_instance_request.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ec2/subnet.py` & `pulumi_aws-5.9.2/pulumi_aws/ec2/subnet.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ec2/subnet_cidr_reservation.py` & `pulumi_aws-5.9.2/pulumi_aws/ec2/subnet_cidr_reservation.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ec2/tag.py` & `pulumi_aws-5.9.2/pulumi_aws/ec2/tag.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ec2/traffic_mirror_filter.py` & `pulumi_aws-5.9.2/pulumi_aws/ec2/traffic_mirror_filter.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ec2/traffic_mirror_filter_rule.py` & `pulumi_aws-5.9.2/pulumi_aws/ec2/traffic_mirror_filter_rule.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ec2/traffic_mirror_session.py` & `pulumi_aws-5.9.2/pulumi_aws/ec2/traffic_mirror_session.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ec2/traffic_mirror_target.py` & `pulumi_aws-5.9.2/pulumi_aws/ec2/traffic_mirror_target.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ec2/transit_gateway_peering_attachment_accepter.py` & `pulumi_aws-5.9.2/pulumi_aws/ec2/transit_gateway_peering_attachment_accepter.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ec2/volume_attachment.py` & `pulumi_aws-5.9.2/pulumi_aws/ec2/volume_attachment.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ec2/vpc.py` & `pulumi_aws-5.9.2/pulumi_aws/ec2/vpc.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ec2/vpc_dhcp_options.py` & `pulumi_aws-5.9.2/pulumi_aws/ec2/vpc_dhcp_options.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ec2/vpc_dhcp_options_association.py` & `pulumi_aws-5.9.2/pulumi_aws/ec2/vpc_dhcp_options_association.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ec2/vpc_endpoint.py` & `pulumi_aws-5.9.2/pulumi_aws/ec2/vpc_endpoint.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ec2/vpc_endpoint_connection_accepter.py` & `pulumi_aws-5.9.2/pulumi_aws/ec2/vpc_endpoint_connection_accepter.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ec2/vpc_endpoint_connection_notification.py` & `pulumi_aws-5.9.2/pulumi_aws/ec2/vpc_endpoint_connection_notification.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ec2/vpc_endpoint_policy.py` & `pulumi_aws-5.9.2/pulumi_aws/ec2/vpc_endpoint_policy.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ec2/vpc_endpoint_route_table_association.py` & `pulumi_aws-5.9.2/pulumi_aws/ec2/vpc_endpoint_route_table_association.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ec2/vpc_endpoint_service.py` & `pulumi_aws-5.9.2/pulumi_aws/ec2/vpc_endpoint_service.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ec2/vpc_endpoint_service_allowed_principle.py` & `pulumi_aws-5.9.2/pulumi_aws/ec2/vpc_endpoint_service_allowed_principle.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ec2/vpc_endpoint_subnet_association.py` & `pulumi_aws-5.9.2/pulumi_aws/ec2/vpc_endpoint_subnet_association.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ec2/vpc_ipam.py` & `pulumi_aws-5.9.2/pulumi_aws/ec2/vpc_ipam.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ec2/vpc_ipam_organization_admin_account.py` & `pulumi_aws-5.9.2/pulumi_aws/ec2/vpc_ipam_organization_admin_account.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ec2/vpc_ipam_pool.py` & `pulumi_aws-5.9.2/pulumi_aws/ec2/vpc_ipam_pool.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ec2/vpc_ipam_pool_cidr.py` & `pulumi_aws-5.9.2/pulumi_aws/ec2/vpc_ipam_pool_cidr.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ec2/vpc_ipam_pool_cidr_allocation.py` & `pulumi_aws-5.9.2/pulumi_aws/ec2/vpc_ipam_pool_cidr_allocation.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ec2/vpc_ipam_preview_next_cidr.py` & `pulumi_aws-5.9.2/pulumi_aws/ec2/vpc_ipam_preview_next_cidr.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ec2/vpc_ipam_scope.py` & `pulumi_aws-5.9.2/pulumi_aws/ec2/vpc_ipam_scope.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ec2/vpc_ipv4_cidr_block_association.py` & `pulumi_aws-5.9.2/pulumi_aws/ec2/vpc_ipv4_cidr_block_association.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ec2/vpc_ipv6_cidr_block_association.py` & `pulumi_aws-5.9.2/pulumi_aws/ec2/vpc_ipv6_cidr_block_association.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ec2/vpc_peering_connection.py` & `pulumi_aws-5.9.2/pulumi_aws/ec2/vpc_peering_connection.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ec2/vpc_peering_connection_accepter.py` & `pulumi_aws-5.9.2/pulumi_aws/ec2/vpc_peering_connection_accepter.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ec2/vpn_connection.py` & `pulumi_aws-5.9.2/pulumi_aws/ec2/vpn_connection.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ec2/vpn_connection_route.py` & `pulumi_aws-5.9.2/pulumi_aws/ec2/vpn_connection_route.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ec2/vpn_gateway.py` & `pulumi_aws-5.9.2/pulumi_aws/ec2/vpn_gateway.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ec2/vpn_gateway_attachment.py` & `pulumi_aws-5.9.2/pulumi_aws/ec2/vpn_gateway_attachment.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ec2/vpn_gateway_route_propagation.py` & `pulumi_aws-5.9.2/pulumi_aws/ec2/vpn_gateway_route_propagation.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ec2clientvpn/_inputs.py` & `pulumi_aws-5.9.2/pulumi_aws/ec2clientvpn/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ec2clientvpn/authorization_rule.py` & `pulumi_aws-5.9.2/pulumi_aws/ec2clientvpn/authorization_rule.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ec2clientvpn/endpoint.py` & `pulumi_aws-5.9.2/pulumi_aws/ec2clientvpn/endpoint.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ec2clientvpn/get_endpoint.py` & `pulumi_aws-5.9.2/pulumi_aws/ec2clientvpn/get_endpoint.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ec2clientvpn/network_association.py` & `pulumi_aws-5.9.2/pulumi_aws/ec2clientvpn/network_association.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ec2clientvpn/outputs.py` & `pulumi_aws-5.9.2/pulumi_aws/ec2clientvpn/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ec2clientvpn/route.py` & `pulumi_aws-5.9.2/pulumi_aws/ec2clientvpn/route.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ec2transitgateway/__init__.py` & `pulumi_aws-5.9.2/pulumi_aws/ec2transitgateway/__init__.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ec2transitgateway/_inputs.py` & `pulumi_aws-5.9.2/pulumi_aws/ec2transitgateway/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ec2transitgateway/connect.py` & `pulumi_aws-5.9.2/pulumi_aws/ec2transitgateway/connect.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ec2transitgateway/connect_peer.py` & `pulumi_aws-5.9.2/pulumi_aws/ec2transitgateway/connect_peer.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ec2transitgateway/get_connect.py` & `pulumi_aws-5.9.2/pulumi_aws/ec2transitgateway/get_connect.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ec2transitgateway/get_connect_peer.py` & `pulumi_aws-5.9.2/pulumi_aws/ec2transitgateway/get_connect_peer.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ec2transitgateway/get_direct_connect_gateway_attachment.py` & `pulumi_aws-5.9.2/pulumi_aws/ec2transitgateway/get_direct_connect_gateway_attachment.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ec2transitgateway/get_multicast_domain.py` & `pulumi_aws-5.9.2/pulumi_aws/ec2transitgateway/get_multicast_domain.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ec2transitgateway/get_peering_attachment.py` & `pulumi_aws-5.9.2/pulumi_aws/ec2transitgateway/get_peering_attachment.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ec2transitgateway/get_route_table.py` & `pulumi_aws-5.9.2/pulumi_aws/ec2transitgateway/get_route_table.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ec2transitgateway/get_transit_gateway.py` & `pulumi_aws-5.9.2/pulumi_aws/ec2transitgateway/get_transit_gateway.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ec2transitgateway/get_vpc_attachment.py` & `pulumi_aws-5.9.2/pulumi_aws/ec2transitgateway/get_vpc_attachment.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ec2transitgateway/get_vpc_attachments.py` & `pulumi_aws-5.9.2/pulumi_aws/ec2transitgateway/get_vpc_attachments.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ec2transitgateway/get_vpn_attachment.py` & `pulumi_aws-5.9.2/pulumi_aws/ec2transitgateway/get_vpn_attachment.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ec2transitgateway/multicast_domain.py` & `pulumi_aws-5.9.2/pulumi_aws/ec2transitgateway/multicast_domain.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ec2transitgateway/multicast_domain_association.py` & `pulumi_aws-5.9.2/pulumi_aws/ec2transitgateway/multicast_domain_association.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ec2transitgateway/multicast_group_member.py` & `pulumi_aws-5.9.2/pulumi_aws/ec2transitgateway/multicast_group_member.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ec2transitgateway/multicast_group_source.py` & `pulumi_aws-5.9.2/pulumi_aws/ec2transitgateway/multicast_group_source.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ec2transitgateway/outputs.py` & `pulumi_aws-5.9.2/pulumi_aws/ec2transitgateway/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ec2transitgateway/peering_attachment.py` & `pulumi_aws-5.9.2/pulumi_aws/ec2transitgateway/peering_attachment.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ec2transitgateway/prefix_list_reference.py` & `pulumi_aws-5.9.2/pulumi_aws/ec2transitgateway/prefix_list_reference.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ec2transitgateway/route.py` & `pulumi_aws-5.9.2/pulumi_aws/ec2transitgateway/route.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ec2transitgateway/route_table.py` & `pulumi_aws-5.9.2/pulumi_aws/ec2transitgateway/route_table.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ec2transitgateway/route_table_association.py` & `pulumi_aws-5.9.2/pulumi_aws/ec2transitgateway/route_table_association.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ec2transitgateway/route_table_propagation.py` & `pulumi_aws-5.9.2/pulumi_aws/ec2transitgateway/route_table_propagation.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ec2transitgateway/transit_gateway.py` & `pulumi_aws-5.9.2/pulumi_aws/ec2transitgateway/transit_gateway.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ec2transitgateway/vpc_attachment.py` & `pulumi_aws-5.9.2/pulumi_aws/ec2transitgateway/vpc_attachment.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ec2transitgateway/vpc_attachment_accepter.py` & `pulumi_aws-5.9.2/pulumi_aws/ec2transitgateway/vpc_attachment_accepter.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ecr/__init__.py` & `pulumi_aws-5.9.2/pulumi_aws/ecr/__init__.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ecr/_inputs.py` & `pulumi_aws-5.9.2/pulumi_aws/ecr/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ecr/get_authorization_token.py` & `pulumi_aws-5.9.2/pulumi_aws/ecr/get_authorization_token.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ecr/get_credentials.py` & `pulumi_aws-5.9.2/pulumi_aws/ecr/get_credentials.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ecr/get_image.py` & `pulumi_aws-5.9.2/pulumi_aws/ecr/get_image.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ecr/get_repository.py` & `pulumi_aws-5.9.2/pulumi_aws/ecr/get_repository.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ecr/lifecycle_policy.py` & `pulumi_aws-5.9.2/pulumi_aws/ecr/lifecycle_policy.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ecr/outputs.py` & `pulumi_aws-5.9.2/pulumi_aws/ecr/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ecr/pull_through_cache_rule.py` & `pulumi_aws-5.9.2/pulumi_aws/ecr/pull_through_cache_rule.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ecr/registry_policy.py` & `pulumi_aws-5.9.2/pulumi_aws/ecr/registry_policy.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ecr/registry_scanning_configuration.py` & `pulumi_aws-5.9.2/pulumi_aws/ecr/registry_scanning_configuration.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ecr/replication_configuration.py` & `pulumi_aws-5.9.2/pulumi_aws/ecr/replication_configuration.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ecr/repository.py` & `pulumi_aws-5.9.2/pulumi_aws/ecr/repository.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ecr/repository_policy.py` & `pulumi_aws-5.9.2/pulumi_aws/ecr/repository_policy.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ecrpublic/_inputs.py` & `pulumi_aws-5.9.2/pulumi_aws/ecrpublic/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ecrpublic/get_authorization_token.py` & `pulumi_aws-5.9.2/pulumi_aws/ecrpublic/get_authorization_token.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ecrpublic/outputs.py` & `pulumi_aws-5.9.2/pulumi_aws/ecrpublic/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ecrpublic/repository.py` & `pulumi_aws-5.9.2/pulumi_aws/ecrpublic/repository.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ecrpublic/repository_policy.py` & `pulumi_aws-5.9.2/pulumi_aws/ecrpublic/repository_policy.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ecs/__init__.py` & `pulumi_aws-5.9.2/pulumi_aws/ecs/__init__.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ecs/_inputs.py` & `pulumi_aws-5.9.2/pulumi_aws/ecs/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ecs/account_setting_default.py` & `pulumi_aws-5.9.2/pulumi_aws/ecs/account_setting_default.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ecs/capacity_provider.py` & `pulumi_aws-5.9.2/pulumi_aws/ecs/capacity_provider.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ecs/cluster.py` & `pulumi_aws-5.9.2/pulumi_aws/ecs/cluster.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ecs/cluster_capacity_providers.py` & `pulumi_aws-5.9.2/pulumi_aws/ecs/cluster_capacity_providers.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ecs/get_cluster.py` & `pulumi_aws-5.9.2/pulumi_aws/ecs/get_cluster.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ecs/get_container_definition.py` & `pulumi_aws-5.9.2/pulumi_aws/ecs/get_container_definition.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ecs/get_service.py` & `pulumi_aws-5.9.2/pulumi_aws/ecs/get_service.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ecs/get_task_definition.py` & `pulumi_aws-5.9.2/pulumi_aws/ecs/get_task_definition.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ecs/outputs.py` & `pulumi_aws-5.9.2/pulumi_aws/ecs/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ecs/service.py` & `pulumi_aws-5.9.2/pulumi_aws/ecs/service.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ecs/tag.py` & `pulumi_aws-5.9.2/pulumi_aws/ecs/tag.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ecs/task_definition.py` & `pulumi_aws-5.9.2/pulumi_aws/ecs/task_definition.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ecs/task_set.py` & `pulumi_aws-5.9.2/pulumi_aws/ecs/task_set.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/efs/__init__.py` & `pulumi_aws-5.9.2/pulumi_aws/efs/__init__.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/efs/_inputs.py` & `pulumi_aws-5.9.2/pulumi_aws/efs/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/efs/access_point.py` & `pulumi_aws-5.9.2/pulumi_aws/efs/access_point.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/efs/backup_policy.py` & `pulumi_aws-5.9.2/pulumi_aws/efs/backup_policy.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/efs/file_system.py` & `pulumi_aws-5.9.2/pulumi_aws/efs/file_system.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/efs/file_system_policy.py` & `pulumi_aws-5.9.2/pulumi_aws/efs/file_system_policy.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/efs/get_access_point.py` & `pulumi_aws-5.9.2/pulumi_aws/efs/get_access_point.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/efs/get_access_points.py` & `pulumi_aws-5.9.2/pulumi_aws/efs/get_access_points.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/efs/get_file_system.py` & `pulumi_aws-5.9.2/pulumi_aws/efs/get_file_system.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/efs/get_mount_target.py` & `pulumi_aws-5.9.2/pulumi_aws/efs/get_mount_target.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/efs/mount_target.py` & `pulumi_aws-5.9.2/pulumi_aws/efs/mount_target.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/efs/outputs.py` & `pulumi_aws-5.9.2/pulumi_aws/efs/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/efs/replication_configuration.py` & `pulumi_aws-5.9.2/pulumi_aws/efs/replication_configuration.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/eks/__init__.py` & `pulumi_aws-5.9.2/pulumi_aws/eks/__init__.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/eks/_inputs.py` & `pulumi_aws-5.9.2/pulumi_aws/eks/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/eks/addon.py` & `pulumi_aws-5.9.2/pulumi_aws/eks/addon.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/eks/cluster.py` & `pulumi_aws-5.9.2/pulumi_aws/eks/cluster.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/eks/fargate_profile.py` & `pulumi_aws-5.9.2/pulumi_aws/eks/fargate_profile.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/eks/get_addon.py` & `pulumi_aws-5.9.2/pulumi_aws/eks/get_addon.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/eks/get_addon_version.py` & `pulumi_aws-5.9.2/pulumi_aws/eks/get_addon_version.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/eks/get_cluster.py` & `pulumi_aws-5.9.2/pulumi_aws/eks/get_cluster.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/eks/get_cluster_auth.py` & `pulumi_aws-5.9.2/pulumi_aws/eks/get_cluster_auth.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/eks/get_clusters.py` & `pulumi_aws-5.9.2/pulumi_aws/eks/get_clusters.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/eks/get_node_group.py` & `pulumi_aws-5.9.2/pulumi_aws/eks/get_node_group.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/eks/get_node_groups.py` & `pulumi_aws-5.9.2/pulumi_aws/eks/get_node_groups.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/eks/identity_provider_config.py` & `pulumi_aws-5.9.2/pulumi_aws/eks/identity_provider_config.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/eks/node_group.py` & `pulumi_aws-5.9.2/pulumi_aws/eks/node_group.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/eks/outputs.py` & `pulumi_aws-5.9.2/pulumi_aws/eks/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/elasticache/__init__.py` & `pulumi_aws-5.9.2/pulumi_aws/elasticache/__init__.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/elasticache/_inputs.py` & `pulumi_aws-5.9.2/pulumi_aws/elasticache/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/elasticache/cluster.py` & `pulumi_aws-5.9.2/pulumi_aws/elasticache/cluster.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/elasticache/get_cluster.py` & `pulumi_aws-5.9.2/pulumi_aws/elasticache/get_cluster.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/elasticache/get_replication_group.py` & `pulumi_aws-5.9.2/pulumi_aws/elasticache/get_replication_group.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/elasticache/get_user.py` & `pulumi_aws-5.9.2/pulumi_aws/elasticache/get_user.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/elasticache/global_replication_group.py` & `pulumi_aws-5.9.2/pulumi_aws/elasticache/global_replication_group.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/elasticache/outputs.py` & `pulumi_aws-5.9.2/pulumi_aws/elasticache/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/elasticache/parameter_group.py` & `pulumi_aws-5.9.2/pulumi_aws/elasticache/parameter_group.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/elasticache/replication_group.py` & `pulumi_aws-5.9.2/pulumi_aws/elasticache/replication_group.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/elasticache/security_group.py` & `pulumi_aws-5.9.2/pulumi_aws/elasticache/security_group.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/elasticache/subnet_group.py` & `pulumi_aws-5.9.2/pulumi_aws/elasticache/subnet_group.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/elasticache/user.py` & `pulumi_aws-5.9.2/pulumi_aws/elasticache/user.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/elasticache/user_group.py` & `pulumi_aws-5.9.2/pulumi_aws/elasticache/user_group.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/elasticache/user_group_association.py` & `pulumi_aws-5.9.2/pulumi_aws/elasticache/user_group_association.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/elasticbeanstalk/__init__.py` & `pulumi_aws-5.9.2/pulumi_aws/elasticbeanstalk/__init__.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/elasticbeanstalk/_inputs.py` & `pulumi_aws-5.9.2/pulumi_aws/elasticbeanstalk/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/elasticbeanstalk/application.py` & `pulumi_aws-5.9.2/pulumi_aws/elasticbeanstalk/application.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/elasticbeanstalk/application_version.py` & `pulumi_aws-5.9.2/pulumi_aws/elasticbeanstalk/application_version.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/elasticbeanstalk/configuration_template.py` & `pulumi_aws-5.9.2/pulumi_aws/elasticbeanstalk/configuration_template.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/elasticbeanstalk/environment.py` & `pulumi_aws-5.9.2/pulumi_aws/elasticbeanstalk/environment.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/elasticbeanstalk/get_application.py` & `pulumi_aws-5.9.2/pulumi_aws/elasticbeanstalk/get_application.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/elasticbeanstalk/get_hosted_zone.py` & `pulumi_aws-5.9.2/pulumi_aws/elasticbeanstalk/get_hosted_zone.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/elasticbeanstalk/get_solution_stack.py` & `pulumi_aws-5.9.2/pulumi_aws/elasticbeanstalk/get_solution_stack.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/elasticbeanstalk/outputs.py` & `pulumi_aws-5.9.2/pulumi_aws/elasticbeanstalk/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/elasticloadbalancing/__init__.py` & `pulumi_aws-5.9.2/pulumi_aws/elasticloadbalancing/__init__.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/elasticloadbalancing/_inputs.py` & `pulumi_aws-5.9.2/pulumi_aws/elasticloadbalancing/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/elasticloadbalancing/app_cookie_stickiness_policy.py` & `pulumi_aws-5.9.2/pulumi_aws/elasticloadbalancing/app_cookie_stickiness_policy.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/elasticloadbalancing/attachment.py` & `pulumi_aws-5.9.2/pulumi_aws/elasticloadbalancing/attachment.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/elasticloadbalancing/get_hosted_zone_id.py` & `pulumi_aws-5.9.2/pulumi_aws/elasticloadbalancing/get_hosted_zone_id.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/elasticloadbalancing/get_load_balancer.py` & `pulumi_aws-5.9.2/pulumi_aws/elasticloadbalancing/get_load_balancer.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/elasticloadbalancing/get_service_account.py` & `pulumi_aws-5.9.2/pulumi_aws/elasticloadbalancing/get_service_account.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/elasticloadbalancing/listener_policy.py` & `pulumi_aws-5.9.2/pulumi_aws/elasticloadbalancing/listener_policy.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/elasticloadbalancing/load_balancer.py` & `pulumi_aws-5.9.2/pulumi_aws/elasticloadbalancing/load_balancer.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/elasticloadbalancing/load_balancer_backend_server_policy.py` & `pulumi_aws-5.9.2/pulumi_aws/elasticloadbalancing/load_balancer_backend_server_policy.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/elasticloadbalancing/load_balancer_cookie_stickiness_policy.py` & `pulumi_aws-5.9.2/pulumi_aws/elasticloadbalancing/load_balancer_cookie_stickiness_policy.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/elasticloadbalancing/load_balancer_policy.py` & `pulumi_aws-5.9.2/pulumi_aws/elasticloadbalancing/load_balancer_policy.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/elasticloadbalancing/outputs.py` & `pulumi_aws-5.9.2/pulumi_aws/elasticloadbalancing/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/elasticloadbalancing/ssl_negotiation_policy.py` & `pulumi_aws-5.9.2/pulumi_aws/elasticloadbalancing/ssl_negotiation_policy.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/elasticloadbalancingv2/__init__.py` & `pulumi_aws-5.9.2/pulumi_aws/elasticloadbalancingv2/__init__.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/elasticloadbalancingv2/_inputs.py` & `pulumi_aws-5.9.2/pulumi_aws/elasticloadbalancingv2/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/elasticloadbalancingv2/get_listener.py` & `pulumi_aws-5.9.2/pulumi_aws/elasticloadbalancingv2/get_listener.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/elasticloadbalancingv2/get_load_balancer.py` & `pulumi_aws-5.9.2/pulumi_aws/elasticloadbalancingv2/get_load_balancer.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/elasticloadbalancingv2/get_target_group.py` & `pulumi_aws-5.9.2/pulumi_aws/elasticloadbalancingv2/get_target_group.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/elasticloadbalancingv2/listener.py` & `pulumi_aws-5.9.2/pulumi_aws/elasticloadbalancingv2/listener.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/elasticloadbalancingv2/listener_certificate.py` & `pulumi_aws-5.9.2/pulumi_aws/elasticloadbalancingv2/listener_certificate.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/elasticloadbalancingv2/listener_rule.py` & `pulumi_aws-5.9.2/pulumi_aws/elasticloadbalancingv2/listener_rule.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/elasticloadbalancingv2/load_balancer.py` & `pulumi_aws-5.9.2/pulumi_aws/elasticloadbalancingv2/load_balancer.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/elasticloadbalancingv2/outputs.py` & `pulumi_aws-5.9.2/pulumi_aws/elasticloadbalancingv2/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/elasticloadbalancingv2/target_group.py` & `pulumi_aws-5.9.2/pulumi_aws/elasticloadbalancingv2/target_group.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/elasticloadbalancingv2/target_group_attachment.py` & `pulumi_aws-5.9.2/pulumi_aws/elasticloadbalancingv2/target_group_attachment.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/elasticsearch/_inputs.py` & `pulumi_aws-5.9.2/pulumi_aws/elasticsearch/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/elasticsearch/domain.py` & `pulumi_aws-5.9.2/pulumi_aws/elasticsearch/domain.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/elasticsearch/domain_policy.py` & `pulumi_aws-5.9.2/pulumi_aws/elasticsearch/domain_policy.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/elasticsearch/domain_saml_options.py` & `pulumi_aws-5.9.2/pulumi_aws/elasticsearch/domain_saml_options.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/elasticsearch/get_domain.py` & `pulumi_aws-5.9.2/pulumi_aws/elasticsearch/get_domain.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/elasticsearch/outputs.py` & `pulumi_aws-5.9.2/pulumi_aws/elasticsearch/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/elastictranscoder/_inputs.py` & `pulumi_aws-5.9.2/pulumi_aws/elastictranscoder/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/elastictranscoder/outputs.py` & `pulumi_aws-5.9.2/pulumi_aws/elastictranscoder/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/elastictranscoder/pipeline.py` & `pulumi_aws-5.9.2/pulumi_aws/elastictranscoder/pipeline.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/elastictranscoder/preset.py` & `pulumi_aws-5.9.2/pulumi_aws/elastictranscoder/preset.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/elb/__init__.py` & `pulumi_aws-5.9.2/pulumi_aws/elb/__init__.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/elb/_inputs.py` & `pulumi_aws-5.9.2/pulumi_aws/elb/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/elb/app_cookie_stickiness_policy.py` & `pulumi_aws-5.9.2/pulumi_aws/elb/app_cookie_stickiness_policy.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/elb/attachment.py` & `pulumi_aws-5.9.2/pulumi_aws/elb/attachment.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/elb/get_hosted_zone_id.py` & `pulumi_aws-5.9.2/pulumi_aws/elb/get_hosted_zone_id.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/elb/get_load_balancer.py` & `pulumi_aws-5.9.2/pulumi_aws/elb/get_load_balancer.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/elb/get_service_account.py` & `pulumi_aws-5.9.2/pulumi_aws/elb/get_service_account.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/elb/listener_policy.py` & `pulumi_aws-5.9.2/pulumi_aws/elb/listener_policy.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/elb/load_balancer.py` & `pulumi_aws-5.9.2/pulumi_aws/elb/load_balancer.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/elb/load_balancer_backend_server_policy.py` & `pulumi_aws-5.9.2/pulumi_aws/elb/load_balancer_backend_server_policy.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/elb/load_balancer_cookie_stickiness_policy.py` & `pulumi_aws-5.9.2/pulumi_aws/elb/load_balancer_cookie_stickiness_policy.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/elb/load_balancer_policy.py` & `pulumi_aws-5.9.2/pulumi_aws/elb/load_balancer_policy.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/elb/outputs.py` & `pulumi_aws-5.9.2/pulumi_aws/elb/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/elb/ssl_negotiation_policy.py` & `pulumi_aws-5.9.2/pulumi_aws/elb/ssl_negotiation_policy.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/emr/__init__.py` & `pulumi_aws-5.9.2/pulumi_aws/emr/__init__.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/emr/_inputs.py` & `pulumi_aws-5.9.2/pulumi_aws/emr/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/emr/cluster.py` & `pulumi_aws-5.9.2/pulumi_aws/emr/cluster.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/emr/get_release_labels.py` & `pulumi_aws-5.9.2/pulumi_aws/emr/get_release_labels.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/emr/instance_fleet.py` & `pulumi_aws-5.9.2/pulumi_aws/emr/instance_fleet.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/emr/instance_group.py` & `pulumi_aws-5.9.2/pulumi_aws/emr/instance_group.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/emr/managed_scaling_policy.py` & `pulumi_aws-5.9.2/pulumi_aws/emr/managed_scaling_policy.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/emr/outputs.py` & `pulumi_aws-5.9.2/pulumi_aws/emr/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/emr/security_configuration.py` & `pulumi_aws-5.9.2/pulumi_aws/emr/security_configuration.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/emr/studio.py` & `pulumi_aws-5.9.2/pulumi_aws/emr/studio.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/emr/studio_session_mapping.py` & `pulumi_aws-5.9.2/pulumi_aws/emr/studio_session_mapping.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/emrcontainers/_inputs.py` & `pulumi_aws-5.9.2/pulumi_aws/emrcontainers/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/emrcontainers/get_virtual_cluster.py` & `pulumi_aws-5.9.2/pulumi_aws/emrcontainers/get_virtual_cluster.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/emrcontainers/outputs.py` & `pulumi_aws-5.9.2/pulumi_aws/emrcontainers/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/emrcontainers/virtual_cluster.py` & `pulumi_aws-5.9.2/pulumi_aws/emrcontainers/virtual_cluster.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/emrserverless/_inputs.py` & `pulumi_aws-5.9.2/pulumi_aws/emrserverless/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/emrserverless/application.py` & `pulumi_aws-5.9.2/pulumi_aws/emrserverless/application.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/emrserverless/outputs.py` & `pulumi_aws-5.9.2/pulumi_aws/emrserverless/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/fms/_inputs.py` & `pulumi_aws-5.9.2/pulumi_aws/fms/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/fms/admin_account.py` & `pulumi_aws-5.9.2/pulumi_aws/fms/admin_account.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/fms/outputs.py` & `pulumi_aws-5.9.2/pulumi_aws/fms/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/fms/policy.py` & `pulumi_aws-5.9.2/pulumi_aws/fms/policy.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/fsx/__init__.py` & `pulumi_aws-5.9.2/pulumi_aws/fsx/__init__.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/fsx/_inputs.py` & `pulumi_aws-5.9.2/pulumi_aws/fsx/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/fsx/backup.py` & `pulumi_aws-5.9.2/pulumi_aws/fsx/backup.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/fsx/data_repository_association.py` & `pulumi_aws-5.9.2/pulumi_aws/fsx/data_repository_association.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/fsx/lustre_file_system.py` & `pulumi_aws-5.9.2/pulumi_aws/fsx/lustre_file_system.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/fsx/ontap_file_system.py` & `pulumi_aws-5.9.2/pulumi_aws/fsx/ontap_file_system.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/fsx/ontap_storage_virtual_machine.py` & `pulumi_aws-5.9.2/pulumi_aws/fsx/ontap_storage_virtual_machine.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/fsx/ontap_volume.py` & `pulumi_aws-5.9.2/pulumi_aws/fsx/ontap_volume.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/fsx/open_zfs_file_system.py` & `pulumi_aws-5.9.2/pulumi_aws/fsx/open_zfs_file_system.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/fsx/open_zfs_snapshot.py` & `pulumi_aws-5.9.2/pulumi_aws/fsx/open_zfs_snapshot.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/fsx/open_zfs_volume.py` & `pulumi_aws-5.9.2/pulumi_aws/fsx/open_zfs_volume.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/fsx/outputs.py` & `pulumi_aws-5.9.2/pulumi_aws/fsx/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/fsx/windows_file_system.py` & `pulumi_aws-5.9.2/pulumi_aws/fsx/windows_file_system.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/gamelift/_inputs.py` & `pulumi_aws-5.9.2/pulumi_aws/gamelift/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/gamelift/alias.py` & `pulumi_aws-5.9.2/pulumi_aws/gamelift/alias.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/gamelift/build.py` & `pulumi_aws-5.9.2/pulumi_aws/gamelift/build.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/gamelift/fleet.py` & `pulumi_aws-5.9.2/pulumi_aws/gamelift/fleet.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/gamelift/game_server_group.py` & `pulumi_aws-5.9.2/pulumi_aws/gamelift/game_server_group.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/gamelift/game_session_queue.py` & `pulumi_aws-5.9.2/pulumi_aws/gamelift/game_session_queue.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/gamelift/outputs.py` & `pulumi_aws-5.9.2/pulumi_aws/gamelift/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/gamelift/script.py` & `pulumi_aws-5.9.2/pulumi_aws/gamelift/script.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/get_ami.py` & `pulumi_aws-5.9.2/pulumi_aws/get_ami.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/get_ami_ids.py` & `pulumi_aws-5.9.2/pulumi_aws/get_ami_ids.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/get_arn.py` & `pulumi_aws-5.9.2/pulumi_aws/get_arn.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/get_autoscaling_groups.py` & `pulumi_aws-5.9.2/pulumi_aws/get_autoscaling_groups.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/get_availability_zone.py` & `pulumi_aws-5.9.2/pulumi_aws/get_availability_zone.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/get_availability_zones.py` & `pulumi_aws-5.9.2/pulumi_aws/get_availability_zones.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/get_billing_service_account.py` & `pulumi_aws-5.9.2/pulumi_aws/get_billing_service_account.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/get_caller_identity.py` & `pulumi_aws-5.9.2/pulumi_aws/get_caller_identity.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/get_canonical_user_id.py` & `pulumi_aws-5.9.2/pulumi_aws/get_canonical_user_id.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/get_default_tags.py` & `pulumi_aws-5.9.2/pulumi_aws/get_default_tags.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/get_elastic_ip.py` & `pulumi_aws-5.9.2/pulumi_aws/get_elastic_ip.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/get_ip_ranges.py` & `pulumi_aws-5.9.2/pulumi_aws/get_ip_ranges.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/get_partition.py` & `pulumi_aws-5.9.2/pulumi_aws/get_partition.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/get_prefix_list.py` & `pulumi_aws-5.9.2/pulumi_aws/get_prefix_list.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/get_region.py` & `pulumi_aws-5.9.2/pulumi_aws/get_region.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/get_regions.py` & `pulumi_aws-5.9.2/pulumi_aws/get_regions.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/get_service.py` & `pulumi_aws-5.9.2/pulumi_aws/get_service.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/glacier/_inputs.py` & `pulumi_aws-5.9.2/pulumi_aws/glacier/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/glacier/outputs.py` & `pulumi_aws-5.9.2/pulumi_aws/glacier/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/glacier/vault.py` & `pulumi_aws-5.9.2/pulumi_aws/glacier/vault.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/glacier/vault_lock.py` & `pulumi_aws-5.9.2/pulumi_aws/glacier/vault_lock.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/globalaccelerator/_inputs.py` & `pulumi_aws-5.9.2/pulumi_aws/globalaccelerator/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/globalaccelerator/accelerator.py` & `pulumi_aws-5.9.2/pulumi_aws/globalaccelerator/accelerator.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/globalaccelerator/endpoint_group.py` & `pulumi_aws-5.9.2/pulumi_aws/globalaccelerator/endpoint_group.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/globalaccelerator/get_accelerator.py` & `pulumi_aws-5.9.2/pulumi_aws/globalaccelerator/get_accelerator.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/globalaccelerator/listener.py` & `pulumi_aws-5.9.2/pulumi_aws/globalaccelerator/listener.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/globalaccelerator/outputs.py` & `pulumi_aws-5.9.2/pulumi_aws/globalaccelerator/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/glue/__init__.py` & `pulumi_aws-5.9.2/pulumi_aws/glue/__init__.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/glue/_inputs.py` & `pulumi_aws-5.9.2/pulumi_aws/glue/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/glue/catalog_database.py` & `pulumi_aws-5.9.2/pulumi_aws/glue/catalog_database.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/glue/catalog_table.py` & `pulumi_aws-5.9.2/pulumi_aws/glue/catalog_table.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/glue/classifier.py` & `pulumi_aws-5.9.2/pulumi_aws/glue/classifier.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/glue/connection.py` & `pulumi_aws-5.9.2/pulumi_aws/glue/connection.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/glue/crawler.py` & `pulumi_aws-5.9.2/pulumi_aws/glue/crawler.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/glue/data_catalog_encryption_settings.py` & `pulumi_aws-5.9.2/pulumi_aws/glue/data_catalog_encryption_settings.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/glue/dev_endpoint.py` & `pulumi_aws-5.9.2/pulumi_aws/glue/dev_endpoint.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/glue/get_connection.py` & `pulumi_aws-5.9.2/pulumi_aws/glue/get_connection.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/glue/get_data_catalog_encryption_settings.py` & `pulumi_aws-5.9.2/pulumi_aws/glue/get_data_catalog_encryption_settings.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/glue/get_script.py` & `pulumi_aws-5.9.2/pulumi_aws/glue/get_script.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/glue/job.py` & `pulumi_aws-5.9.2/pulumi_aws/glue/job.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/glue/ml_transform.py` & `pulumi_aws-5.9.2/pulumi_aws/glue/ml_transform.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/glue/outputs.py` & `pulumi_aws-5.9.2/pulumi_aws/glue/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/glue/partition.py` & `pulumi_aws-5.9.2/pulumi_aws/glue/partition.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/glue/partition_index.py` & `pulumi_aws-5.9.2/pulumi_aws/glue/partition_index.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/glue/registry.py` & `pulumi_aws-5.9.2/pulumi_aws/glue/registry.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/glue/resource_policy.py` & `pulumi_aws-5.9.2/pulumi_aws/glue/resource_policy.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/glue/schema.py` & `pulumi_aws-5.9.2/pulumi_aws/glue/schema.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/glue/security_configuration.py` & `pulumi_aws-5.9.2/pulumi_aws/glue/security_configuration.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/glue/trigger.py` & `pulumi_aws-5.9.2/pulumi_aws/glue/trigger.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/glue/user_defined_function.py` & `pulumi_aws-5.9.2/pulumi_aws/glue/user_defined_function.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/glue/workflow.py` & `pulumi_aws-5.9.2/pulumi_aws/glue/workflow.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/grafana/get_workspace.py` & `pulumi_aws-5.9.2/pulumi_aws/grafana/get_workspace.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/grafana/license_association.py` & `pulumi_aws-5.9.2/pulumi_aws/grafana/license_association.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/grafana/role_association.py` & `pulumi_aws-5.9.2/pulumi_aws/grafana/role_association.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/grafana/workspace.py` & `pulumi_aws-5.9.2/pulumi_aws/grafana/workspace.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/grafana/workspace_saml_configuration.py` & `pulumi_aws-5.9.2/pulumi_aws/grafana/workspace_saml_configuration.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/guardduty/__init__.py` & `pulumi_aws-5.9.2/pulumi_aws/guardduty/__init__.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/guardduty/_inputs.py` & `pulumi_aws-5.9.2/pulumi_aws/guardduty/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/guardduty/detector.py` & `pulumi_aws-5.9.2/pulumi_aws/guardduty/detector.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/guardduty/filter.py` & `pulumi_aws-5.9.2/pulumi_aws/guardduty/filter.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/guardduty/get_detector.py` & `pulumi_aws-5.9.2/pulumi_aws/guardduty/get_detector.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/guardduty/invite_accepter.py` & `pulumi_aws-5.9.2/pulumi_aws/guardduty/invite_accepter.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/guardduty/ip_set.py` & `pulumi_aws-5.9.2/pulumi_aws/guardduty/ip_set.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/guardduty/member.py` & `pulumi_aws-5.9.2/pulumi_aws/guardduty/member.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/guardduty/organization_admin_account.py` & `pulumi_aws-5.9.2/pulumi_aws/guardduty/organization_admin_account.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/guardduty/organization_configuration.py` & `pulumi_aws-5.9.2/pulumi_aws/guardduty/organization_configuration.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/guardduty/outputs.py` & `pulumi_aws-5.9.2/pulumi_aws/guardduty/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/guardduty/publishing_destination.py` & `pulumi_aws-5.9.2/pulumi_aws/guardduty/publishing_destination.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/guardduty/threat_intel_set.py` & `pulumi_aws-5.9.2/pulumi_aws/guardduty/threat_intel_set.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/iam/__init__.py` & `pulumi_aws-5.9.2/pulumi_aws/iam/__init__.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/iam/_enums.py` & `pulumi_aws-5.9.2/pulumi_aws/iam/_enums.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/iam/_inputs.py` & `pulumi_aws-5.9.2/pulumi_aws/iam/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/iam/access_key.py` & `pulumi_aws-5.9.2/pulumi_aws/iam/access_key.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/iam/account_alias.py` & `pulumi_aws-5.9.2/pulumi_aws/iam/account_alias.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/iam/account_password_policy.py` & `pulumi_aws-5.9.2/pulumi_aws/iam/account_password_policy.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/iam/get_account_alias.py` & `pulumi_aws-5.9.2/pulumi_aws/iam/get_account_alias.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/iam/get_group.py` & `pulumi_aws-5.9.2/pulumi_aws/iam/get_group.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/iam/get_instance_profile.py` & `pulumi_aws-5.9.2/pulumi_aws/iam/get_instance_profile.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/iam/get_instance_profiles.py` & `pulumi_aws-5.9.2/pulumi_aws/iam/get_instance_profiles.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/iam/get_openid_connect_provider.py` & `pulumi_aws-5.9.2/pulumi_aws/iam/get_openid_connect_provider.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/iam/get_policy.py` & `pulumi_aws-5.9.2/pulumi_aws/iam/get_policy.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/iam/get_policy_document.py` & `pulumi_aws-5.9.2/pulumi_aws/iam/get_policy_document.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/iam/get_role.py` & `pulumi_aws-5.9.2/pulumi_aws/iam/get_role.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/iam/get_roles.py` & `pulumi_aws-5.9.2/pulumi_aws/iam/get_roles.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/iam/get_saml_provider.py` & `pulumi_aws-5.9.2/pulumi_aws/iam/get_saml_provider.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/iam/get_server_certificate.py` & `pulumi_aws-5.9.2/pulumi_aws/iam/get_server_certificate.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/iam/get_session_context.py` & `pulumi_aws-5.9.2/pulumi_aws/iam/get_session_context.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/iam/get_user.py` & `pulumi_aws-5.9.2/pulumi_aws/iam/get_user.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/iam/get_user_ssh_key.py` & `pulumi_aws-5.9.2/pulumi_aws/iam/get_user_ssh_key.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/iam/get_users.py` & `pulumi_aws-5.9.2/pulumi_aws/iam/get_users.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/iam/group.py` & `pulumi_aws-5.9.2/pulumi_aws/iam/group.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/iam/group_membership.py` & `pulumi_aws-5.9.2/pulumi_aws/iam/group_membership.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/iam/group_policy.py` & `pulumi_aws-5.9.2/pulumi_aws/iam/group_policy.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/iam/group_policy_attachment.py` & `pulumi_aws-5.9.2/pulumi_aws/iam/group_policy_attachment.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/iam/instance_profile.py` & `pulumi_aws-5.9.2/pulumi_aws/iam/instance_profile.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/iam/open_id_connect_provider.py` & `pulumi_aws-5.9.2/pulumi_aws/iam/open_id_connect_provider.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/iam/outputs.py` & `pulumi_aws-5.9.2/pulumi_aws/iam/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/iam/policy.py` & `pulumi_aws-5.9.2/pulumi_aws/iam/policy.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/iam/policy_attachment.py` & `pulumi_aws-5.9.2/pulumi_aws/iam/policy_attachment.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/iam/role.py` & `pulumi_aws-5.9.2/pulumi_aws/iam/role.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/iam/role_policy.py` & `pulumi_aws-5.9.2/pulumi_aws/iam/role_policy.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/iam/role_policy_attachment.py` & `pulumi_aws-5.9.2/pulumi_aws/iam/role_policy_attachment.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/iam/saml_provider.py` & `pulumi_aws-5.9.2/pulumi_aws/iam/saml_provider.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/iam/server_certificate.py` & `pulumi_aws-5.9.2/pulumi_aws/iam/server_certificate.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/iam/service_linked_role.py` & `pulumi_aws-5.9.2/pulumi_aws/iam/service_linked_role.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/iam/service_specific_credential.py` & `pulumi_aws-5.9.2/pulumi_aws/iam/service_specific_credential.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/iam/signing_certificate.py` & `pulumi_aws-5.9.2/pulumi_aws/iam/signing_certificate.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/iam/ssh_key.py` & `pulumi_aws-5.9.2/pulumi_aws/iam/ssh_key.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/iam/user.py` & `pulumi_aws-5.9.2/pulumi_aws/iam/user.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/iam/user_group_membership.py` & `pulumi_aws-5.9.2/pulumi_aws/iam/user_group_membership.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/iam/user_login_profile.py` & `pulumi_aws-5.9.2/pulumi_aws/iam/user_login_profile.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/iam/user_policy.py` & `pulumi_aws-5.9.2/pulumi_aws/iam/user_policy.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/iam/user_policy_attachment.py` & `pulumi_aws-5.9.2/pulumi_aws/iam/user_policy_attachment.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/iam/virtual_mfa_device.py` & `pulumi_aws-5.9.2/pulumi_aws/iam/virtual_mfa_device.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/identitystore/_inputs.py` & `pulumi_aws-5.9.2/pulumi_aws/identitystore/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/identitystore/get_group.py` & `pulumi_aws-5.9.2/pulumi_aws/identitystore/get_group.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/identitystore/get_user.py` & `pulumi_aws-5.9.2/pulumi_aws/identitystore/get_user.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/identitystore/outputs.py` & `pulumi_aws-5.9.2/pulumi_aws/identitystore/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/imagebuilder/__init__.py` & `pulumi_aws-5.9.2/pulumi_aws/imagebuilder/__init__.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/imagebuilder/_inputs.py` & `pulumi_aws-5.9.2/pulumi_aws/imagebuilder/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/imagebuilder/component.py` & `pulumi_aws-5.9.2/pulumi_aws/imagebuilder/component.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/imagebuilder/container_recipe.py` & `pulumi_aws-5.9.2/pulumi_aws/imagebuilder/container_recipe.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/imagebuilder/distribution_configuration.py` & `pulumi_aws-5.9.2/pulumi_aws/imagebuilder/distribution_configuration.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/imagebuilder/get_component.py` & `pulumi_aws-5.9.2/pulumi_aws/imagebuilder/get_component.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/imagebuilder/get_components.py` & `pulumi_aws-5.9.2/pulumi_aws/imagebuilder/get_components.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/imagebuilder/get_container_recipe.py` & `pulumi_aws-5.9.2/pulumi_aws/imagebuilder/get_container_recipe.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/imagebuilder/get_container_recipes.py` & `pulumi_aws-5.9.2/pulumi_aws/imagebuilder/get_container_recipes.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/imagebuilder/get_distribution_configuration.py` & `pulumi_aws-5.9.2/pulumi_aws/imagebuilder/get_distribution_configuration.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/imagebuilder/get_distribution_configurations.py` & `pulumi_aws-5.9.2/pulumi_aws/imagebuilder/get_distribution_configurations.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/imagebuilder/get_image.py` & `pulumi_aws-5.9.2/pulumi_aws/imagebuilder/get_image.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/imagebuilder/get_image_pipeline.py` & `pulumi_aws-5.9.2/pulumi_aws/imagebuilder/get_image_pipeline.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/imagebuilder/get_image_pipelines.py` & `pulumi_aws-5.9.2/pulumi_aws/imagebuilder/get_image_pipelines.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/imagebuilder/get_image_recipe.py` & `pulumi_aws-5.9.2/pulumi_aws/imagebuilder/get_image_recipe.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/imagebuilder/get_image_recipes.py` & `pulumi_aws-5.9.2/pulumi_aws/imagebuilder/get_image_recipes.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/imagebuilder/get_infrastructure_configuration.py` & `pulumi_aws-5.9.2/pulumi_aws/imagebuilder/get_infrastructure_configuration.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/imagebuilder/get_infrastructure_configurations.py` & `pulumi_aws-5.9.2/pulumi_aws/imagebuilder/get_infrastructure_configurations.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/imagebuilder/image.py` & `pulumi_aws-5.9.2/pulumi_aws/imagebuilder/image.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/imagebuilder/image_pipeline.py` & `pulumi_aws-5.9.2/pulumi_aws/imagebuilder/image_pipeline.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/imagebuilder/image_recipe.py` & `pulumi_aws-5.9.2/pulumi_aws/imagebuilder/image_recipe.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/imagebuilder/infrastructure_configuration.py` & `pulumi_aws-5.9.2/pulumi_aws/imagebuilder/infrastructure_configuration.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/imagebuilder/outputs.py` & `pulumi_aws-5.9.2/pulumi_aws/imagebuilder/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/inspector/assessment_target.py` & `pulumi_aws-5.9.2/pulumi_aws/inspector/assessment_target.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/inspector/assessment_template.py` & `pulumi_aws-5.9.2/pulumi_aws/inspector/assessment_template.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/inspector/get_rules_packages.py` & `pulumi_aws-5.9.2/pulumi_aws/inspector/get_rules_packages.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/inspector/resource_group.py` & `pulumi_aws-5.9.2/pulumi_aws/inspector/resource_group.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/iot/__init__.py` & `pulumi_aws-5.9.2/pulumi_aws/iot/__init__.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/iot/_inputs.py` & `pulumi_aws-5.9.2/pulumi_aws/iot/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/iot/authorizer.py` & `pulumi_aws-5.9.2/pulumi_aws/iot/authorizer.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/iot/certificate.py` & `pulumi_aws-5.9.2/pulumi_aws/iot/certificate.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/iot/get_endpoint.py` & `pulumi_aws-5.9.2/pulumi_aws/iot/get_endpoint.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/iot/indexing_configuration.py` & `pulumi_aws-5.9.2/pulumi_aws/iot/indexing_configuration.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/iot/logging_options.py` & `pulumi_aws-5.9.2/pulumi_aws/iot/logging_options.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/iot/outputs.py` & `pulumi_aws-5.9.2/pulumi_aws/iot/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/iot/policy.py` & `pulumi_aws-5.9.2/pulumi_aws/iot/policy.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/iot/policy_attachment.py` & `pulumi_aws-5.9.2/pulumi_aws/iot/policy_attachment.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/iot/provisioning_template.py` & `pulumi_aws-5.9.2/pulumi_aws/iot/provisioning_template.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/iot/role_alias.py` & `pulumi_aws-5.9.2/pulumi_aws/iot/role_alias.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/iot/thing.py` & `pulumi_aws-5.9.2/pulumi_aws/iot/thing.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/iot/thing_group.py` & `pulumi_aws-5.9.2/pulumi_aws/iot/thing_group.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/iot/thing_group_membership.py` & `pulumi_aws-5.9.2/pulumi_aws/iot/thing_group_membership.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/iot/thing_principal_attachment.py` & `pulumi_aws-5.9.2/pulumi_aws/iot/thing_principal_attachment.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/iot/thing_type.py` & `pulumi_aws-5.9.2/pulumi_aws/iot/thing_type.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/iot/topic_rule.py` & `pulumi_aws-5.9.2/pulumi_aws/iot/topic_rule.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/iot/topic_rule_destination.py` & `pulumi_aws-5.9.2/pulumi_aws/iot/topic_rule_destination.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/kendra/_inputs.py` & `pulumi_aws-5.9.2/pulumi_aws/kendra/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/kendra/index.py` & `pulumi_aws-5.9.2/pulumi_aws/kendra/index.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/kendra/outputs.py` & `pulumi_aws-5.9.2/pulumi_aws/kendra/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/keyspaces/_inputs.py` & `pulumi_aws-5.9.2/pulumi_aws/keyspaces/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/keyspaces/keyspace.py` & `pulumi_aws-5.9.2/pulumi_aws/keyspaces/keyspace.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/keyspaces/outputs.py` & `pulumi_aws-5.9.2/pulumi_aws/keyspaces/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/keyspaces/table.py` & `pulumi_aws-5.9.2/pulumi_aws/keyspaces/table.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/kinesis/__init__.py` & `pulumi_aws-5.9.2/pulumi_aws/kinesis/__init__.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/kinesis/_inputs.py` & `pulumi_aws-5.9.2/pulumi_aws/kinesis/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/kinesis/analytics_application.py` & `pulumi_aws-5.9.2/pulumi_aws/kinesis/analytics_application.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/kinesis/firehose_delivery_stream.py` & `pulumi_aws-5.9.2/pulumi_aws/kinesis/firehose_delivery_stream.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/kinesis/get_firehose_delivery_stream.py` & `pulumi_aws-5.9.2/pulumi_aws/kinesis/get_firehose_delivery_stream.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/kinesis/get_stream.py` & `pulumi_aws-5.9.2/pulumi_aws/kinesis/get_stream.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/kinesis/get_stream_consumer.py` & `pulumi_aws-5.9.2/pulumi_aws/kinesis/get_stream_consumer.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/kinesis/outputs.py` & `pulumi_aws-5.9.2/pulumi_aws/kinesis/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/kinesis/stream.py` & `pulumi_aws-5.9.2/pulumi_aws/kinesis/stream.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/kinesis/stream_consumer.py` & `pulumi_aws-5.9.2/pulumi_aws/kinesis/stream_consumer.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/kinesis/video_stream.py` & `pulumi_aws-5.9.2/pulumi_aws/kinesis/video_stream.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/kinesisanalyticsv2/_inputs.py` & `pulumi_aws-5.9.2/pulumi_aws/kinesisanalyticsv2/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/kinesisanalyticsv2/application.py` & `pulumi_aws-5.9.2/pulumi_aws/kinesisanalyticsv2/application.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/kinesisanalyticsv2/application_snapshot.py` & `pulumi_aws-5.9.2/pulumi_aws/kinesisanalyticsv2/application_snapshot.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/kinesisanalyticsv2/outputs.py` & `pulumi_aws-5.9.2/pulumi_aws/kinesisanalyticsv2/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/kms/__init__.py` & `pulumi_aws-5.9.2/pulumi_aws/kms/__init__.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/kms/_inputs.py` & `pulumi_aws-5.9.2/pulumi_aws/kms/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/kms/alias.py` & `pulumi_aws-5.9.2/pulumi_aws/kms/alias.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/kms/ciphertext.py` & `pulumi_aws-5.9.2/pulumi_aws/kms/ciphertext.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/kms/external_key.py` & `pulumi_aws-5.9.2/pulumi_aws/kms/external_key.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/kms/get_alias.py` & `pulumi_aws-5.9.2/pulumi_aws/kms/get_alias.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/kms/get_cipher_text.py` & `pulumi_aws-5.9.2/pulumi_aws/kms/get_cipher_text.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/kms/get_key.py` & `pulumi_aws-5.9.2/pulumi_aws/kms/get_key.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/kms/get_public_key.py` & `pulumi_aws-5.9.2/pulumi_aws/kms/get_public_key.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/kms/get_secret.py` & `pulumi_aws-5.9.2/pulumi_aws/kms/get_secret.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/kms/get_secrets.py` & `pulumi_aws-5.9.2/pulumi_aws/kms/get_secrets.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/kms/grant.py` & `pulumi_aws-5.9.2/pulumi_aws/kms/grant.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/kms/key.py` & `pulumi_aws-5.9.2/pulumi_aws/kms/key.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/kms/outputs.py` & `pulumi_aws-5.9.2/pulumi_aws/kms/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/kms/replica_external_key.py` & `pulumi_aws-5.9.2/pulumi_aws/kms/replica_external_key.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/kms/replica_key.py` & `pulumi_aws-5.9.2/pulumi_aws/kms/replica_key.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/lakeformation/_inputs.py` & `pulumi_aws-5.9.2/pulumi_aws/lakeformation/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/lakeformation/data_lake_settings.py` & `pulumi_aws-5.9.2/pulumi_aws/lakeformation/data_lake_settings.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/lakeformation/get_data_lake_settings.py` & `pulumi_aws-5.9.2/pulumi_aws/lakeformation/get_data_lake_settings.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/lakeformation/get_permissions.py` & `pulumi_aws-5.9.2/pulumi_aws/lakeformation/get_permissions.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/lakeformation/get_resource.py` & `pulumi_aws-5.9.2/pulumi_aws/lakeformation/get_resource.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/lakeformation/outputs.py` & `pulumi_aws-5.9.2/pulumi_aws/lakeformation/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/lakeformation/permissions.py` & `pulumi_aws-5.9.2/pulumi_aws/lakeformation/permissions.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/lakeformation/resource.py` & `pulumi_aws-5.9.2/pulumi_aws/lakeformation/resource.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/lambda_/__init__.py` & `pulumi_aws-5.9.2/pulumi_aws/lambda_/__init__.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/lambda_/_enums.py` & `pulumi_aws-5.9.2/pulumi_aws/lambda_/_enums.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/lambda_/_inputs.py` & `pulumi_aws-5.9.2/pulumi_aws/lambda_/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/lambda_/alias.py` & `pulumi_aws-5.9.2/pulumi_aws/lambda_/alias.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/lambda_/code_signing_config.py` & `pulumi_aws-5.9.2/pulumi_aws/lambda_/code_signing_config.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/lambda_/event_source_mapping.py` & `pulumi_aws-5.9.2/pulumi_aws/lambda_/event_source_mapping.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/lambda_/function.py` & `pulumi_aws-5.9.2/pulumi_aws/lambda_/function.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/lambda_/function_event_invoke_config.py` & `pulumi_aws-5.9.2/pulumi_aws/lambda_/function_event_invoke_config.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/lambda_/function_url.py` & `pulumi_aws-5.9.2/pulumi_aws/lambda_/function_url.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/lambda_/get_alias.py` & `pulumi_aws-5.9.2/pulumi_aws/lambda_/get_alias.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/lambda_/get_code_signing_config.py` & `pulumi_aws-5.9.2/pulumi_aws/lambda_/get_code_signing_config.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/lambda_/get_function.py` & `pulumi_aws-5.9.2/pulumi_aws/lambda_/get_function.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/lambda_/get_function_url.py` & `pulumi_aws-5.9.2/pulumi_aws/lambda_/get_function_url.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/lambda_/get_invocation.py` & `pulumi_aws-5.9.2/pulumi_aws/lambda_/get_invocation.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/lambda_/get_layer_version.py` & `pulumi_aws-5.9.2/pulumi_aws/lambda_/get_layer_version.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/lambda_/invocation.py` & `pulumi_aws-5.9.2/pulumi_aws/lambda_/invocation.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/lambda_/layer_version.py` & `pulumi_aws-5.9.2/pulumi_aws/lambda_/layer_version.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/lambda_/layer_version_permission.py` & `pulumi_aws-5.9.2/pulumi_aws/lambda_/layer_version_permission.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/lambda_/outputs.py` & `pulumi_aws-5.9.2/pulumi_aws/lambda_/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/lambda_/permission.py` & `pulumi_aws-5.9.2/pulumi_aws/lambda_/permission.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/lambda_/provisioned_concurrency_config.py` & `pulumi_aws-5.9.2/pulumi_aws/lambda_/provisioned_concurrency_config.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/lb/__init__.py` & `pulumi_aws-5.9.2/pulumi_aws/lb/__init__.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/lb/_inputs.py` & `pulumi_aws-5.9.2/pulumi_aws/lb/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/lb/get_hosted_zone_id.py` & `pulumi_aws-5.9.2/pulumi_aws/lb/get_hosted_zone_id.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/lb/get_listener.py` & `pulumi_aws-5.9.2/pulumi_aws/lb/get_listener.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/lb/get_load_balancer.py` & `pulumi_aws-5.9.2/pulumi_aws/lb/get_load_balancer.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/lb/get_target_group.py` & `pulumi_aws-5.9.2/pulumi_aws/lb/get_target_group.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/lb/listener.py` & `pulumi_aws-5.9.2/pulumi_aws/lb/listener.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/lb/listener_certificate.py` & `pulumi_aws-5.9.2/pulumi_aws/lb/listener_certificate.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/lb/listener_rule.py` & `pulumi_aws-5.9.2/pulumi_aws/lb/listener_rule.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/lb/load_balancer.py` & `pulumi_aws-5.9.2/pulumi_aws/lb/load_balancer.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/lb/outputs.py` & `pulumi_aws-5.9.2/pulumi_aws/lb/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/lb/target_group.py` & `pulumi_aws-5.9.2/pulumi_aws/lb/target_group.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/lb/target_group_attachment.py` & `pulumi_aws-5.9.2/pulumi_aws/lb/target_group_attachment.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/lex/__init__.py` & `pulumi_aws-5.9.2/pulumi_aws/lex/__init__.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/lex/_inputs.py` & `pulumi_aws-5.9.2/pulumi_aws/lex/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/lex/bot.py` & `pulumi_aws-5.9.2/pulumi_aws/lex/bot.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/lex/bot_alias.py` & `pulumi_aws-5.9.2/pulumi_aws/lex/bot_alias.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/lex/get_bot.py` & `pulumi_aws-5.9.2/pulumi_aws/lex/get_bot.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/lex/get_bot_alias.py` & `pulumi_aws-5.9.2/pulumi_aws/lex/get_bot_alias.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/lex/get_intent.py` & `pulumi_aws-5.9.2/pulumi_aws/lex/get_intent.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/lex/get_slot_type.py` & `pulumi_aws-5.9.2/pulumi_aws/lex/get_slot_type.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/lex/intent.py` & `pulumi_aws-5.9.2/pulumi_aws/lex/intent.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/lex/outputs.py` & `pulumi_aws-5.9.2/pulumi_aws/lex/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/lex/slot_type.py` & `pulumi_aws-5.9.2/pulumi_aws/lex/slot_type.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/licensemanager/association.py` & `pulumi_aws-5.9.2/pulumi_aws/licensemanager/association.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/licensemanager/license_configuration.py` & `pulumi_aws-5.9.2/pulumi_aws/licensemanager/license_configuration.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/lightsail/__init__.py` & `pulumi_aws-5.9.2/pulumi_aws/lightsail/__init__.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/lightsail/_inputs.py` & `pulumi_aws-5.9.2/pulumi_aws/lightsail/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/lightsail/container_service.py` & `pulumi_aws-5.9.2/pulumi_aws/lightsail/container_service.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/lightsail/container_service_deployment_version.py` & `pulumi_aws-5.9.2/pulumi_aws/lightsail/container_service_deployment_version.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/lightsail/domain.py` & `pulumi_aws-5.9.2/pulumi_aws/lightsail/domain.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/lightsail/instance.py` & `pulumi_aws-5.9.2/pulumi_aws/lightsail/instance.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/lightsail/instance_public_ports.py` & `pulumi_aws-5.9.2/pulumi_aws/lightsail/instance_public_ports.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/lightsail/key_pair.py` & `pulumi_aws-5.9.2/pulumi_aws/lightsail/key_pair.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/lightsail/outputs.py` & `pulumi_aws-5.9.2/pulumi_aws/lightsail/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/lightsail/static_ip.py` & `pulumi_aws-5.9.2/pulumi_aws/lightsail/static_ip.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/lightsail/static_ip_attachment.py` & `pulumi_aws-5.9.2/pulumi_aws/lightsail/static_ip_attachment.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/location/_inputs.py` & `pulumi_aws-5.9.2/pulumi_aws/location/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/location/get_map.py` & `pulumi_aws-5.9.2/pulumi_aws/location/get_map.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/location/get_place_index.py` & `pulumi_aws-5.9.2/pulumi_aws/location/get_place_index.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/location/map.py` & `pulumi_aws-5.9.2/pulumi_aws/location/map.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/location/outputs.py` & `pulumi_aws-5.9.2/pulumi_aws/location/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/location/place_index.py` & `pulumi_aws-5.9.2/pulumi_aws/location/place_index.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/macie/_inputs.py` & `pulumi_aws-5.9.2/pulumi_aws/macie/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/macie/custom_data_identifier.py` & `pulumi_aws-5.9.2/pulumi_aws/macie/custom_data_identifier.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/macie/findings_filter.py` & `pulumi_aws-5.9.2/pulumi_aws/macie/findings_filter.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/macie/member_account_association.py` & `pulumi_aws-5.9.2/pulumi_aws/macie/member_account_association.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/macie/outputs.py` & `pulumi_aws-5.9.2/pulumi_aws/macie/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/macie/s3_bucket_association.py` & `pulumi_aws-5.9.2/pulumi_aws/macie/s3_bucket_association.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/macie2/_inputs.py` & `pulumi_aws-5.9.2/pulumi_aws/macie2/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/macie2/account.py` & `pulumi_aws-5.9.2/pulumi_aws/macie2/account.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/macie2/classification_job.py` & `pulumi_aws-5.9.2/pulumi_aws/macie2/classification_job.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/macie2/invitation_accepter.py` & `pulumi_aws-5.9.2/pulumi_aws/macie2/invitation_accepter.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/macie2/member.py` & `pulumi_aws-5.9.2/pulumi_aws/macie2/member.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/macie2/organization_admin_account.py` & `pulumi_aws-5.9.2/pulumi_aws/macie2/organization_admin_account.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/macie2/outputs.py` & `pulumi_aws-5.9.2/pulumi_aws/macie2/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/mediaconvert/_inputs.py` & `pulumi_aws-5.9.2/pulumi_aws/mediaconvert/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/mediaconvert/outputs.py` & `pulumi_aws-5.9.2/pulumi_aws/mediaconvert/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/mediaconvert/queue.py` & `pulumi_aws-5.9.2/pulumi_aws/mediaconvert/queue.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/mediapackage/_inputs.py` & `pulumi_aws-5.9.2/pulumi_aws/mediapackage/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/mediapackage/channel.py` & `pulumi_aws-5.9.2/pulumi_aws/mediapackage/channel.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/mediapackage/outputs.py` & `pulumi_aws-5.9.2/pulumi_aws/mediapackage/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/mediastore/container.py` & `pulumi_aws-5.9.2/pulumi_aws/mediastore/container.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/mediastore/container_policy.py` & `pulumi_aws-5.9.2/pulumi_aws/mediastore/container_policy.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/memorydb/__init__.py` & `pulumi_aws-5.9.2/pulumi_aws/memorydb/__init__.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/memorydb/_inputs.py` & `pulumi_aws-5.9.2/pulumi_aws/memorydb/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/memorydb/acl.py` & `pulumi_aws-5.9.2/pulumi_aws/memorydb/acl.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/memorydb/cluster.py` & `pulumi_aws-5.9.2/pulumi_aws/memorydb/cluster.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/memorydb/get_acl.py` & `pulumi_aws-5.9.2/pulumi_aws/memorydb/get_acl.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/memorydb/get_cluster.py` & `pulumi_aws-5.9.2/pulumi_aws/memorydb/get_cluster.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/memorydb/get_parameter_group.py` & `pulumi_aws-5.9.2/pulumi_aws/memorydb/get_parameter_group.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/memorydb/get_snapshot.py` & `pulumi_aws-5.9.2/pulumi_aws/memorydb/get_snapshot.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/memorydb/get_subnet_group.py` & `pulumi_aws-5.9.2/pulumi_aws/memorydb/get_subnet_group.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/memorydb/get_user.py` & `pulumi_aws-5.9.2/pulumi_aws/memorydb/get_user.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/memorydb/outputs.py` & `pulumi_aws-5.9.2/pulumi_aws/memorydb/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/memorydb/parameter_group.py` & `pulumi_aws-5.9.2/pulumi_aws/memorydb/parameter_group.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/memorydb/snapshot.py` & `pulumi_aws-5.9.2/pulumi_aws/memorydb/snapshot.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/memorydb/subnet_group.py` & `pulumi_aws-5.9.2/pulumi_aws/memorydb/subnet_group.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/memorydb/user.py` & `pulumi_aws-5.9.2/pulumi_aws/memorydb/user.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/mq/_inputs.py` & `pulumi_aws-5.9.2/pulumi_aws/mq/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/mq/broker.py` & `pulumi_aws-5.9.2/pulumi_aws/mq/broker.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/mq/configuration.py` & `pulumi_aws-5.9.2/pulumi_aws/mq/configuration.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/mq/get_broker.py` & `pulumi_aws-5.9.2/pulumi_aws/mq/get_broker.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/mq/get_instance_type_offerings.py` & `pulumi_aws-5.9.2/pulumi_aws/mq/get_instance_type_offerings.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/mq/outputs.py` & `pulumi_aws-5.9.2/pulumi_aws/mq/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/msk/__init__.py` & `pulumi_aws-5.9.2/pulumi_aws/msk/__init__.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/msk/_inputs.py` & `pulumi_aws-5.9.2/pulumi_aws/msk/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/msk/cluster.py` & `pulumi_aws-5.9.2/pulumi_aws/msk/cluster.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/msk/configuration.py` & `pulumi_aws-5.9.2/pulumi_aws/msk/configuration.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/msk/get_broker_nodes.py` & `pulumi_aws-5.9.2/pulumi_aws/msk/get_broker_nodes.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/msk/get_cluster.py` & `pulumi_aws-5.9.2/pulumi_aws/msk/get_cluster.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/msk/get_configuration.py` & `pulumi_aws-5.9.2/pulumi_aws/msk/get_configuration.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/msk/get_kafka_version.py` & `pulumi_aws-5.9.2/pulumi_aws/msk/get_kafka_version.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/msk/outputs.py` & `pulumi_aws-5.9.2/pulumi_aws/msk/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/msk/scram_secret_association.py` & `pulumi_aws-5.9.2/pulumi_aws/msk/scram_secret_association.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/mskconnect/_inputs.py` & `pulumi_aws-5.9.2/pulumi_aws/mskconnect/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/mskconnect/connector.py` & `pulumi_aws-5.9.2/pulumi_aws/mskconnect/connector.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/mskconnect/custom_plugin.py` & `pulumi_aws-5.9.2/pulumi_aws/mskconnect/custom_plugin.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/mskconnect/get_connector.py` & `pulumi_aws-5.9.2/pulumi_aws/mskconnect/get_connector.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/mskconnect/get_custom_plugin.py` & `pulumi_aws-5.9.2/pulumi_aws/mskconnect/get_custom_plugin.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/mskconnect/get_worker_configuration.py` & `pulumi_aws-5.9.2/pulumi_aws/mskconnect/get_worker_configuration.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/mskconnect/outputs.py` & `pulumi_aws-5.9.2/pulumi_aws/mskconnect/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/mskconnect/worker_configuration.py` & `pulumi_aws-5.9.2/pulumi_aws/mskconnect/worker_configuration.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/mwaa/_inputs.py` & `pulumi_aws-5.9.2/pulumi_aws/mwaa/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/mwaa/environment.py` & `pulumi_aws-5.9.2/pulumi_aws/mwaa/environment.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/mwaa/outputs.py` & `pulumi_aws-5.9.2/pulumi_aws/mwaa/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/neptune/__init__.py` & `pulumi_aws-5.9.2/pulumi_aws/neptune/__init__.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/neptune/_inputs.py` & `pulumi_aws-5.9.2/pulumi_aws/neptune/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/neptune/cluster.py` & `pulumi_aws-5.9.2/pulumi_aws/neptune/cluster.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/neptune/cluster_endpoint.py` & `pulumi_aws-5.9.2/pulumi_aws/neptune/cluster_endpoint.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/neptune/cluster_instance.py` & `pulumi_aws-5.9.2/pulumi_aws/neptune/cluster_instance.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/neptune/cluster_parameter_group.py` & `pulumi_aws-5.9.2/pulumi_aws/neptune/cluster_parameter_group.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/neptune/cluster_snapshot.py` & `pulumi_aws-5.9.2/pulumi_aws/neptune/cluster_snapshot.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/neptune/event_subscription.py` & `pulumi_aws-5.9.2/pulumi_aws/neptune/event_subscription.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/neptune/get_engine_version.py` & `pulumi_aws-5.9.2/pulumi_aws/neptune/get_engine_version.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/neptune/get_orderable_db_instance.py` & `pulumi_aws-5.9.2/pulumi_aws/neptune/get_orderable_db_instance.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/neptune/outputs.py` & `pulumi_aws-5.9.2/pulumi_aws/neptune/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/neptune/parameter_group.py` & `pulumi_aws-5.9.2/pulumi_aws/neptune/parameter_group.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/neptune/subnet_group.py` & `pulumi_aws-5.9.2/pulumi_aws/neptune/subnet_group.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/networkfirewall/_inputs.py` & `pulumi_aws-5.9.2/pulumi_aws/networkfirewall/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/networkfirewall/firewall.py` & `pulumi_aws-5.9.2/pulumi_aws/networkfirewall/firewall.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/networkfirewall/firewall_policy.py` & `pulumi_aws-5.9.2/pulumi_aws/networkfirewall/firewall_policy.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/networkfirewall/logging_configuration.py` & `pulumi_aws-5.9.2/pulumi_aws/networkfirewall/logging_configuration.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/networkfirewall/outputs.py` & `pulumi_aws-5.9.2/pulumi_aws/networkfirewall/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/networkfirewall/resource_policy.py` & `pulumi_aws-5.9.2/pulumi_aws/networkfirewall/resource_policy.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/networkfirewall/rule_group.py` & `pulumi_aws-5.9.2/pulumi_aws/networkfirewall/rule_group.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/networkmanager/__init__.py` & `pulumi_aws-5.9.2/pulumi_aws/networkmanager/__init__.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/networkmanager/_inputs.py` & `pulumi_aws-5.9.2/pulumi_aws/networkmanager/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/networkmanager/connection.py` & `pulumi_aws-5.9.2/pulumi_aws/networkmanager/connection.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/networkmanager/customer_gateway_association.py` & `pulumi_aws-5.9.2/pulumi_aws/networkmanager/customer_gateway_association.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/networkmanager/device.py` & `pulumi_aws-5.9.2/pulumi_aws/networkmanager/device.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/networkmanager/get_connection.py` & `pulumi_aws-5.9.2/pulumi_aws/networkmanager/get_connection.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/networkmanager/get_connections.py` & `pulumi_aws-5.9.2/pulumi_aws/networkmanager/get_connections.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/networkmanager/get_core_network_policy_document.py` & `pulumi_aws-5.9.2/pulumi_aws/networkmanager/get_core_network_policy_document.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/networkmanager/get_device.py` & `pulumi_aws-5.9.2/pulumi_aws/networkmanager/get_device.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/networkmanager/get_devices.py` & `pulumi_aws-5.9.2/pulumi_aws/networkmanager/get_devices.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/networkmanager/get_global_network.py` & `pulumi_aws-5.9.2/pulumi_aws/networkmanager/get_global_network.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/networkmanager/get_global_networks.py` & `pulumi_aws-5.9.2/pulumi_aws/networkmanager/get_global_networks.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/networkmanager/get_link.py` & `pulumi_aws-5.9.2/pulumi_aws/networkmanager/get_link.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/networkmanager/get_links.py` & `pulumi_aws-5.9.2/pulumi_aws/networkmanager/get_links.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/networkmanager/get_site.py` & `pulumi_aws-5.9.2/pulumi_aws/networkmanager/get_site.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/networkmanager/get_sites.py` & `pulumi_aws-5.9.2/pulumi_aws/networkmanager/get_sites.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/networkmanager/global_network.py` & `pulumi_aws-5.9.2/pulumi_aws/networkmanager/global_network.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/networkmanager/link.py` & `pulumi_aws-5.9.2/pulumi_aws/networkmanager/link.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/networkmanager/link_association.py` & `pulumi_aws-5.9.2/pulumi_aws/networkmanager/link_association.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/networkmanager/outputs.py` & `pulumi_aws-5.9.2/pulumi_aws/networkmanager/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/networkmanager/site.py` & `pulumi_aws-5.9.2/pulumi_aws/networkmanager/site.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/networkmanager/transit_gateway_connect_peer_association.py` & `pulumi_aws-5.9.2/pulumi_aws/networkmanager/transit_gateway_connect_peer_association.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/networkmanager/transit_gateway_registration.py` & `pulumi_aws-5.9.2/pulumi_aws/networkmanager/transit_gateway_registration.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/opensearch/_inputs.py` & `pulumi_aws-5.9.2/pulumi_aws/opensearch/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/opensearch/domain.py` & `pulumi_aws-5.9.2/pulumi_aws/opensearch/domain.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/opensearch/domain_policy.py` & `pulumi_aws-5.9.2/pulumi_aws/opensearch/domain_policy.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/opensearch/domain_saml_options.py` & `pulumi_aws-5.9.2/pulumi_aws/opensearch/domain_saml_options.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/opensearch/get_domain.py` & `pulumi_aws-5.9.2/pulumi_aws/opensearch/get_domain.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/opensearch/outputs.py` & `pulumi_aws-5.9.2/pulumi_aws/opensearch/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/opsworks/__init__.py` & `pulumi_aws-5.9.2/pulumi_aws/opsworks/__init__.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/opsworks/_inputs.py` & `pulumi_aws-5.9.2/pulumi_aws/opsworks/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/opsworks/application.py` & `pulumi_aws-5.9.2/pulumi_aws/opsworks/application.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/opsworks/custom_layer.py` & `pulumi_aws-5.9.2/pulumi_aws/opsworks/custom_layer.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/opsworks/ecs_cluster_layer.py` & `pulumi_aws-5.9.2/pulumi_aws/opsworks/ecs_cluster_layer.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/opsworks/ganglia_layer.py` & `pulumi_aws-5.9.2/pulumi_aws/opsworks/ganglia_layer.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/opsworks/haproxy_layer.py` & `pulumi_aws-5.9.2/pulumi_aws/opsworks/haproxy_layer.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/opsworks/instance.py` & `pulumi_aws-5.9.2/pulumi_aws/opsworks/instance.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/opsworks/java_app_layer.py` & `pulumi_aws-5.9.2/pulumi_aws/opsworks/java_app_layer.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/opsworks/memcached_layer.py` & `pulumi_aws-5.9.2/pulumi_aws/opsworks/memcached_layer.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/opsworks/mysql_layer.py` & `pulumi_aws-5.9.2/pulumi_aws/opsworks/mysql_layer.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/opsworks/nodejs_app_layer.py` & `pulumi_aws-5.9.2/pulumi_aws/opsworks/nodejs_app_layer.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/opsworks/outputs.py` & `pulumi_aws-5.9.2/pulumi_aws/opsworks/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/opsworks/permission.py` & `pulumi_aws-5.9.2/pulumi_aws/opsworks/permission.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/opsworks/php_app_layer.py` & `pulumi_aws-5.9.2/pulumi_aws/opsworks/php_app_layer.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/opsworks/rails_app_layer.py` & `pulumi_aws-5.9.2/pulumi_aws/opsworks/rails_app_layer.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/opsworks/rds_db_instance.py` & `pulumi_aws-5.9.2/pulumi_aws/opsworks/rds_db_instance.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/opsworks/stack.py` & `pulumi_aws-5.9.2/pulumi_aws/opsworks/stack.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/opsworks/static_web_layer.py` & `pulumi_aws-5.9.2/pulumi_aws/opsworks/static_web_layer.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/opsworks/user_profile.py` & `pulumi_aws-5.9.2/pulumi_aws/opsworks/user_profile.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/organizations/__init__.py` & `pulumi_aws-5.9.2/pulumi_aws/organizations/__init__.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/organizations/_inputs.py` & `pulumi_aws-5.9.2/pulumi_aws/organizations/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/organizations/account.py` & `pulumi_aws-5.9.2/pulumi_aws/organizations/account.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/organizations/delegated_administrator.py` & `pulumi_aws-5.9.2/pulumi_aws/organizations/delegated_administrator.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/organizations/get_delegated_administrators.py` & `pulumi_aws-5.9.2/pulumi_aws/organizations/get_delegated_administrators.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/organizations/get_delegated_services.py` & `pulumi_aws-5.9.2/pulumi_aws/organizations/get_delegated_services.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/organizations/get_organization.py` & `pulumi_aws-5.9.2/pulumi_aws/organizations/get_organization.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/organizations/get_organizational_units.py` & `pulumi_aws-5.9.2/pulumi_aws/organizations/get_organizational_units.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/organizations/get_resource_tags.py` & `pulumi_aws-5.9.2/pulumi_aws/organizations/get_resource_tags.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/organizations/organization.py` & `pulumi_aws-5.9.2/pulumi_aws/organizations/organization.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/organizations/organizational_unit.py` & `pulumi_aws-5.9.2/pulumi_aws/organizations/organizational_unit.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/organizations/outputs.py` & `pulumi_aws-5.9.2/pulumi_aws/organizations/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/organizations/policy.py` & `pulumi_aws-5.9.2/pulumi_aws/organizations/policy.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/organizations/policy_attachment.py` & `pulumi_aws-5.9.2/pulumi_aws/organizations/policy_attachment.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/outposts/get_outpost.py` & `pulumi_aws-5.9.2/pulumi_aws/outposts/get_outpost.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/outposts/get_outpost_instance_type.py` & `pulumi_aws-5.9.2/pulumi_aws/outposts/get_outpost_instance_type.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/outposts/get_outpost_instance_types.py` & `pulumi_aws-5.9.2/pulumi_aws/outposts/get_outpost_instance_types.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/outposts/get_outposts.py` & `pulumi_aws-5.9.2/pulumi_aws/outposts/get_outposts.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/outposts/get_site.py` & `pulumi_aws-5.9.2/pulumi_aws/outposts/get_site.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/outposts/get_sites.py` & `pulumi_aws-5.9.2/pulumi_aws/outposts/get_sites.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/outputs.py` & `pulumi_aws-5.9.2/pulumi_aws/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/pinpoint/__init__.py` & `pulumi_aws-5.9.2/pulumi_aws/pinpoint/__init__.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/pinpoint/_inputs.py` & `pulumi_aws-5.9.2/pulumi_aws/pinpoint/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/pinpoint/adm_channel.py` & `pulumi_aws-5.9.2/pulumi_aws/pinpoint/adm_channel.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/pinpoint/apns_channel.py` & `pulumi_aws-5.9.2/pulumi_aws/pinpoint/apns_channel.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/pinpoint/apns_sandbox_channel.py` & `pulumi_aws-5.9.2/pulumi_aws/pinpoint/apns_sandbox_channel.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/pinpoint/apns_voip_channel.py` & `pulumi_aws-5.9.2/pulumi_aws/pinpoint/apns_voip_channel.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/pinpoint/apns_voip_sandbox_channel.py` & `pulumi_aws-5.9.2/pulumi_aws/pinpoint/apns_voip_sandbox_channel.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/pinpoint/app.py` & `pulumi_aws-5.9.2/pulumi_aws/pinpoint/app.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/pinpoint/baidu_channel.py` & `pulumi_aws-5.9.2/pulumi_aws/pinpoint/baidu_channel.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/pinpoint/email_channel.py` & `pulumi_aws-5.9.2/pulumi_aws/pinpoint/email_channel.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/pinpoint/event_stream.py` & `pulumi_aws-5.9.2/pulumi_aws/pinpoint/event_stream.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/pinpoint/gcm_channel.py` & `pulumi_aws-5.9.2/pulumi_aws/pinpoint/gcm_channel.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/pinpoint/outputs.py` & `pulumi_aws-5.9.2/pulumi_aws/pinpoint/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/pinpoint/sms_channel.py` & `pulumi_aws-5.9.2/pulumi_aws/pinpoint/sms_channel.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/pricing/_inputs.py` & `pulumi_aws-5.9.2/pulumi_aws/pricing/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/pricing/get_product.py` & `pulumi_aws-5.9.2/pulumi_aws/pricing/get_product.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/pricing/outputs.py` & `pulumi_aws-5.9.2/pulumi_aws/pricing/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/provider.py` & `pulumi_aws-5.9.2/pulumi_aws/provider.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/qldb/_inputs.py` & `pulumi_aws-5.9.2/pulumi_aws/qldb/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/qldb/get_ledger.py` & `pulumi_aws-5.9.2/pulumi_aws/qldb/get_ledger.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/qldb/ledger.py` & `pulumi_aws-5.9.2/pulumi_aws/qldb/ledger.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/qldb/outputs.py` & `pulumi_aws-5.9.2/pulumi_aws/qldb/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/qldb/stream.py` & `pulumi_aws-5.9.2/pulumi_aws/qldb/stream.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/quicksight/_inputs.py` & `pulumi_aws-5.9.2/pulumi_aws/quicksight/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/quicksight/data_source.py` & `pulumi_aws-5.9.2/pulumi_aws/quicksight/data_source.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/quicksight/group.py` & `pulumi_aws-5.9.2/pulumi_aws/quicksight/group.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/quicksight/group_membership.py` & `pulumi_aws-5.9.2/pulumi_aws/quicksight/group_membership.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/quicksight/outputs.py` & `pulumi_aws-5.9.2/pulumi_aws/quicksight/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/quicksight/user.py` & `pulumi_aws-5.9.2/pulumi_aws/quicksight/user.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ram/_inputs.py` & `pulumi_aws-5.9.2/pulumi_aws/ram/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ram/get_resource_share.py` & `pulumi_aws-5.9.2/pulumi_aws/ram/get_resource_share.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ram/outputs.py` & `pulumi_aws-5.9.2/pulumi_aws/ram/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ram/principal_association.py` & `pulumi_aws-5.9.2/pulumi_aws/ram/principal_association.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ram/resource_association.py` & `pulumi_aws-5.9.2/pulumi_aws/ram/resource_association.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ram/resource_share.py` & `pulumi_aws-5.9.2/pulumi_aws/ram/resource_share.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ram/resource_share_accepter.py` & `pulumi_aws-5.9.2/pulumi_aws/ram/resource_share_accepter.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/rds/__init__.py` & `pulumi_aws-5.9.2/pulumi_aws/rds/__init__.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/rds/_enums.py` & `pulumi_aws-5.9.2/pulumi_aws/rds/_enums.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/rds/_inputs.py` & `pulumi_aws-5.9.2/pulumi_aws/rds/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/rds/cluster.py` & `pulumi_aws-5.9.2/pulumi_aws/rds/cluster.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/rds/cluster_activity_stream.py` & `pulumi_aws-5.9.2/pulumi_aws/rds/cluster_activity_stream.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/rds/cluster_endpoint.py` & `pulumi_aws-5.9.2/pulumi_aws/rds/cluster_endpoint.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/rds/cluster_instance.py` & `pulumi_aws-5.9.2/pulumi_aws/rds/cluster_instance.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/rds/cluster_parameter_group.py` & `pulumi_aws-5.9.2/pulumi_aws/rds/cluster_parameter_group.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/rds/cluster_role_association.py` & `pulumi_aws-5.9.2/pulumi_aws/rds/cluster_role_association.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/rds/cluster_snapshot.py` & `pulumi_aws-5.9.2/pulumi_aws/rds/cluster_snapshot.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/rds/event_subscription.py` & `pulumi_aws-5.9.2/pulumi_aws/rds/event_subscription.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/rds/get_certificate.py` & `pulumi_aws-5.9.2/pulumi_aws/rds/get_certificate.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/rds/get_cluster.py` & `pulumi_aws-5.9.2/pulumi_aws/rds/get_cluster.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/rds/get_cluster_snapshot.py` & `pulumi_aws-5.9.2/pulumi_aws/rds/get_cluster_snapshot.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/rds/get_engine_version.py` & `pulumi_aws-5.9.2/pulumi_aws/rds/get_engine_version.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/rds/get_event_categories.py` & `pulumi_aws-5.9.2/pulumi_aws/rds/get_event_categories.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/rds/get_instance.py` & `pulumi_aws-5.9.2/pulumi_aws/rds/get_instance.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/rds/get_orderable_db_instance.py` & `pulumi_aws-5.9.2/pulumi_aws/rds/get_orderable_db_instance.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/rds/get_proxy.py` & `pulumi_aws-5.9.2/pulumi_aws/rds/get_proxy.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/rds/get_snapshot.py` & `pulumi_aws-5.9.2/pulumi_aws/rds/get_snapshot.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/rds/get_subnet_group.py` & `pulumi_aws-5.9.2/pulumi_aws/rds/get_subnet_group.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/rds/global_cluster.py` & `pulumi_aws-5.9.2/pulumi_aws/rds/global_cluster.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/rds/instance.py` & `pulumi_aws-5.9.2/pulumi_aws/rds/instance.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/rds/instance_automated_backups_replication.py` & `pulumi_aws-5.9.2/pulumi_aws/rds/instance_automated_backups_replication.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/rds/option_group.py` & `pulumi_aws-5.9.2/pulumi_aws/rds/option_group.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/rds/outputs.py` & `pulumi_aws-5.9.2/pulumi_aws/rds/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/rds/parameter_group.py` & `pulumi_aws-5.9.2/pulumi_aws/rds/parameter_group.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/rds/proxy.py` & `pulumi_aws-5.9.2/pulumi_aws/rds/proxy.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/rds/proxy_default_target_group.py` & `pulumi_aws-5.9.2/pulumi_aws/rds/proxy_default_target_group.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/rds/proxy_endpoint.py` & `pulumi_aws-5.9.2/pulumi_aws/rds/proxy_endpoint.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/rds/proxy_target.py` & `pulumi_aws-5.9.2/pulumi_aws/rds/proxy_target.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/rds/role_association.py` & `pulumi_aws-5.9.2/pulumi_aws/rds/role_association.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/rds/security_group.py` & `pulumi_aws-5.9.2/pulumi_aws/rds/security_group.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/rds/snapshot.py` & `pulumi_aws-5.9.2/pulumi_aws/rds/snapshot.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/rds/snapshot_copy.py` & `pulumi_aws-5.9.2/pulumi_aws/rds/snapshot_copy.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/rds/subnet_group.py` & `pulumi_aws-5.9.2/pulumi_aws/rds/subnet_group.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/redshift/__init__.py` & `pulumi_aws-5.9.2/pulumi_aws/redshift/__init__.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/redshift/_inputs.py` & `pulumi_aws-5.9.2/pulumi_aws/redshift/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/redshift/authentication_profile.py` & `pulumi_aws-5.9.2/pulumi_aws/redshift/authentication_profile.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/redshift/cluster.py` & `pulumi_aws-5.9.2/pulumi_aws/redshift/cluster.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/redshift/cluster_iam_roles.py` & `pulumi_aws-5.9.2/pulumi_aws/redshift/cluster_iam_roles.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/redshift/endpoint_access.py` & `pulumi_aws-5.9.2/pulumi_aws/redshift/endpoint_access.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/redshift/event_subscription.py` & `pulumi_aws-5.9.2/pulumi_aws/redshift/event_subscription.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/redshift/get_cluster.py` & `pulumi_aws-5.9.2/pulumi_aws/redshift/get_cluster.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/redshift/get_cluster_credentials.py` & `pulumi_aws-5.9.2/pulumi_aws/redshift/get_cluster_credentials.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/redshift/get_orderable_cluster.py` & `pulumi_aws-5.9.2/pulumi_aws/redshift/get_orderable_cluster.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/redshift/get_service_account.py` & `pulumi_aws-5.9.2/pulumi_aws/redshift/get_service_account.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/redshift/get_subnet_group.py` & `pulumi_aws-5.9.2/pulumi_aws/redshift/get_subnet_group.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/redshift/hsm_client_certificate.py` & `pulumi_aws-5.9.2/pulumi_aws/redshift/hsm_client_certificate.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/redshift/hsm_configuration.py` & `pulumi_aws-5.9.2/pulumi_aws/redshift/hsm_configuration.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/redshift/outputs.py` & `pulumi_aws-5.9.2/pulumi_aws/redshift/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/redshift/parameter_group.py` & `pulumi_aws-5.9.2/pulumi_aws/redshift/parameter_group.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/redshift/scheduled_action.py` & `pulumi_aws-5.9.2/pulumi_aws/redshift/scheduled_action.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/redshift/security_group.py` & `pulumi_aws-5.9.2/pulumi_aws/redshift/security_group.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/redshift/snapshot_copy_grant.py` & `pulumi_aws-5.9.2/pulumi_aws/redshift/snapshot_copy_grant.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/redshift/snapshot_schedule.py` & `pulumi_aws-5.9.2/pulumi_aws/redshift/snapshot_schedule.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/redshift/snapshot_schedule_association.py` & `pulumi_aws-5.9.2/pulumi_aws/redshift/snapshot_schedule_association.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/redshift/subnet_group.py` & `pulumi_aws-5.9.2/pulumi_aws/redshift/subnet_group.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/redshift/usage_limit.py` & `pulumi_aws-5.9.2/pulumi_aws/redshift/usage_limit.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/redshiftdata/_inputs.py` & `pulumi_aws-5.9.2/pulumi_aws/redshiftdata/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/redshiftdata/outputs.py` & `pulumi_aws-5.9.2/pulumi_aws/redshiftdata/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/redshiftdata/statement.py` & `pulumi_aws-5.9.2/pulumi_aws/redshiftdata/statement.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/resourcegroups/_inputs.py` & `pulumi_aws-5.9.2/pulumi_aws/resourcegroups/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/resourcegroups/group.py` & `pulumi_aws-5.9.2/pulumi_aws/resourcegroups/group.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/resourcegroups/outputs.py` & `pulumi_aws-5.9.2/pulumi_aws/resourcegroups/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/resourcegroupstaggingapi/_inputs.py` & `pulumi_aws-5.9.2/pulumi_aws/resourcegroupstaggingapi/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/resourcegroupstaggingapi/get_resources.py` & `pulumi_aws-5.9.2/pulumi_aws/resourcegroupstaggingapi/get_resources.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/resourcegroupstaggingapi/outputs.py` & `pulumi_aws-5.9.2/pulumi_aws/resourcegroupstaggingapi/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/route53/__init__.py` & `pulumi_aws-5.9.2/pulumi_aws/route53/__init__.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/route53/_inputs.py` & `pulumi_aws-5.9.2/pulumi_aws/route53/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/route53/delegation_set.py` & `pulumi_aws-5.9.2/pulumi_aws/route53/delegation_set.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/route53/get_delegation_set.py` & `pulumi_aws-5.9.2/pulumi_aws/route53/get_delegation_set.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/route53/get_resolver_endpoint.py` & `pulumi_aws-5.9.2/pulumi_aws/route53/get_resolver_endpoint.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/route53/get_resolver_rule.py` & `pulumi_aws-5.9.2/pulumi_aws/route53/get_resolver_rule.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/route53/get_resolver_rules.py` & `pulumi_aws-5.9.2/pulumi_aws/route53/get_resolver_rules.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/route53/get_traffic_policy_document.py` & `pulumi_aws-5.9.2/pulumi_aws/route53/get_traffic_policy_document.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/route53/get_zone.py` & `pulumi_aws-5.9.2/pulumi_aws/route53/get_zone.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/route53/health_check.py` & `pulumi_aws-5.9.2/pulumi_aws/route53/health_check.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/route53/hosted_zone_dns_sec.py` & `pulumi_aws-5.9.2/pulumi_aws/route53/hosted_zone_dns_sec.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/route53/key_signing_key.py` & `pulumi_aws-5.9.2/pulumi_aws/route53/key_signing_key.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/route53/outputs.py` & `pulumi_aws-5.9.2/pulumi_aws/route53/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/route53/query_log.py` & `pulumi_aws-5.9.2/pulumi_aws/route53/query_log.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/route53/record.py` & `pulumi_aws-5.9.2/pulumi_aws/route53/record.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/route53/resolver_dns_sec_config.py` & `pulumi_aws-5.9.2/pulumi_aws/route53/resolver_dns_sec_config.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/route53/resolver_endpoint.py` & `pulumi_aws-5.9.2/pulumi_aws/route53/resolver_endpoint.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/route53/resolver_firewall_config.py` & `pulumi_aws-5.9.2/pulumi_aws/route53/resolver_firewall_config.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/route53/resolver_firewall_domain_list.py` & `pulumi_aws-5.9.2/pulumi_aws/route53/resolver_firewall_domain_list.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/route53/resolver_firewall_rule.py` & `pulumi_aws-5.9.2/pulumi_aws/route53/resolver_firewall_rule.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/route53/resolver_firewall_rule_group.py` & `pulumi_aws-5.9.2/pulumi_aws/route53/resolver_firewall_rule_group.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/route53/resolver_firewall_rule_group_association.py` & `pulumi_aws-5.9.2/pulumi_aws/route53/resolver_firewall_rule_group_association.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/route53/resolver_query_log_config.py` & `pulumi_aws-5.9.2/pulumi_aws/route53/resolver_query_log_config.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/route53/resolver_query_log_config_association.py` & `pulumi_aws-5.9.2/pulumi_aws/route53/resolver_query_log_config_association.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/route53/resolver_rule.py` & `pulumi_aws-5.9.2/pulumi_aws/route53/resolver_rule.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/route53/resolver_rule_association.py` & `pulumi_aws-5.9.2/pulumi_aws/route53/resolver_rule_association.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/route53/traffic_policy.py` & `pulumi_aws-5.9.2/pulumi_aws/route53/traffic_policy.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/route53/traffic_policy_instance.py` & `pulumi_aws-5.9.2/pulumi_aws/route53/traffic_policy_instance.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/route53/vpc_association_authorization.py` & `pulumi_aws-5.9.2/pulumi_aws/route53/vpc_association_authorization.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/route53/zone.py` & `pulumi_aws-5.9.2/pulumi_aws/route53/zone.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/route53/zone_association.py` & `pulumi_aws-5.9.2/pulumi_aws/route53/zone_association.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/route53domains/_inputs.py` & `pulumi_aws-5.9.2/pulumi_aws/route53domains/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/route53domains/outputs.py` & `pulumi_aws-5.9.2/pulumi_aws/route53domains/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/route53domains/registered_domain.py` & `pulumi_aws-5.9.2/pulumi_aws/route53domains/registered_domain.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/route53recoverycontrol/_inputs.py` & `pulumi_aws-5.9.2/pulumi_aws/route53recoverycontrol/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/route53recoverycontrol/cluster.py` & `pulumi_aws-5.9.2/pulumi_aws/route53recoverycontrol/cluster.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/route53recoverycontrol/control_panel.py` & `pulumi_aws-5.9.2/pulumi_aws/route53recoverycontrol/control_panel.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/route53recoverycontrol/outputs.py` & `pulumi_aws-5.9.2/pulumi_aws/route53recoverycontrol/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/route53recoverycontrol/routing_control.py` & `pulumi_aws-5.9.2/pulumi_aws/route53recoverycontrol/routing_control.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/route53recoverycontrol/safety_rule.py` & `pulumi_aws-5.9.2/pulumi_aws/route53recoverycontrol/safety_rule.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/route53recoveryreadiness/_inputs.py` & `pulumi_aws-5.9.2/pulumi_aws/route53recoveryreadiness/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/route53recoveryreadiness/cell.py` & `pulumi_aws-5.9.2/pulumi_aws/route53recoveryreadiness/cell.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/route53recoveryreadiness/outputs.py` & `pulumi_aws-5.9.2/pulumi_aws/route53recoveryreadiness/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/route53recoveryreadiness/readiness_check.py` & `pulumi_aws-5.9.2/pulumi_aws/route53recoveryreadiness/readiness_check.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/route53recoveryreadiness/recovery_group.py` & `pulumi_aws-5.9.2/pulumi_aws/route53recoveryreadiness/recovery_group.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/route53recoveryreadiness/resource_set.py` & `pulumi_aws-5.9.2/pulumi_aws/route53recoveryreadiness/resource_set.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/s3/__init__.py` & `pulumi_aws-5.9.2/pulumi_aws/s3/__init__.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/s3/_enums.py` & `pulumi_aws-5.9.2/pulumi_aws/s3/_enums.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/s3/_inputs.py` & `pulumi_aws-5.9.2/pulumi_aws/s3/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/s3/access_point.py` & `pulumi_aws-5.9.2/pulumi_aws/s3/access_point.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/s3/account_public_access_block.py` & `pulumi_aws-5.9.2/pulumi_aws/s3/account_public_access_block.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/s3/analytics_configuration.py` & `pulumi_aws-5.9.2/pulumi_aws/s3/analytics_configuration.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/s3/bucket.py` & `pulumi_aws-5.9.2/pulumi_aws/s3/bucket.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/s3/bucket_accelerate_configuration_v2.py` & `pulumi_aws-5.9.2/pulumi_aws/s3/bucket_accelerate_configuration_v2.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/s3/bucket_acl_v2.py` & `pulumi_aws-5.9.2/pulumi_aws/s3/bucket_acl_v2.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/s3/bucket_cors_configuration_v2.py` & `pulumi_aws-5.9.2/pulumi_aws/s3/bucket_cors_configuration_v2.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/s3/bucket_intelligent_tiering_configuration.py` & `pulumi_aws-5.9.2/pulumi_aws/s3/bucket_intelligent_tiering_configuration.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/s3/bucket_lifecycle_configuration_v2.py` & `pulumi_aws-5.9.2/pulumi_aws/s3/bucket_lifecycle_configuration_v2.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/s3/bucket_logging_v2.py` & `pulumi_aws-5.9.2/pulumi_aws/s3/bucket_logging_v2.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/s3/bucket_metric.py` & `pulumi_aws-5.9.2/pulumi_aws/s3/bucket_metric.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/s3/bucket_notification.py` & `pulumi_aws-5.9.2/pulumi_aws/s3/bucket_notification.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/s3/bucket_object.py` & `pulumi_aws-5.9.2/pulumi_aws/s3/bucket_object.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/s3/bucket_object_lock_configuration_v2.py` & `pulumi_aws-5.9.2/pulumi_aws/s3/bucket_object_lock_configuration_v2.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/s3/bucket_objectv2.py` & `pulumi_aws-5.9.2/pulumi_aws/s3/bucket_objectv2.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/s3/bucket_ownership_controls.py` & `pulumi_aws-5.9.2/pulumi_aws/s3/bucket_ownership_controls.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/s3/bucket_policy.py` & `pulumi_aws-5.9.2/pulumi_aws/s3/bucket_policy.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/s3/bucket_public_access_block.py` & `pulumi_aws-5.9.2/pulumi_aws/s3/bucket_public_access_block.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/s3/bucket_replication_config.py` & `pulumi_aws-5.9.2/pulumi_aws/s3/bucket_replication_config.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/s3/bucket_request_payment_configuration_v2.py` & `pulumi_aws-5.9.2/pulumi_aws/s3/bucket_request_payment_configuration_v2.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/s3/bucket_server_side_encryption_configuration_v2.py` & `pulumi_aws-5.9.2/pulumi_aws/s3/bucket_server_side_encryption_configuration_v2.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/s3/bucket_v2.py` & `pulumi_aws-5.9.2/pulumi_aws/s3/bucket_v2.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/s3/bucket_versioning_v2.py` & `pulumi_aws-5.9.2/pulumi_aws/s3/bucket_versioning_v2.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/s3/bucket_website_configuration_v2.py` & `pulumi_aws-5.9.2/pulumi_aws/s3/bucket_website_configuration_v2.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/s3/get_bucket.py` & `pulumi_aws-5.9.2/pulumi_aws/s3/get_bucket.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/s3/get_bucket_object.py` & `pulumi_aws-5.9.2/pulumi_aws/s3/get_bucket_object.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/s3/get_bucket_objects.py` & `pulumi_aws-5.9.2/pulumi_aws/s3/get_bucket_objects.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/s3/get_bucket_policy.py` & `pulumi_aws-5.9.2/pulumi_aws/s3/get_bucket_policy.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/s3/get_canonical_user_id.py` & `pulumi_aws-5.9.2/pulumi_aws/s3/get_canonical_user_id.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/s3/get_object.py` & `pulumi_aws-5.9.2/pulumi_aws/s3/get_object.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/s3/get_objects.py` & `pulumi_aws-5.9.2/pulumi_aws/s3/get_objects.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/s3/inventory.py` & `pulumi_aws-5.9.2/pulumi_aws/s3/inventory.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/s3/object_copy.py` & `pulumi_aws-5.9.2/pulumi_aws/s3/object_copy.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/s3/outputs.py` & `pulumi_aws-5.9.2/pulumi_aws/s3/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/s3control/__init__.py` & `pulumi_aws-5.9.2/pulumi_aws/s3control/__init__.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/s3control/_inputs.py` & `pulumi_aws-5.9.2/pulumi_aws/s3control/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/s3control/access_point_policy.py` & `pulumi_aws-5.9.2/pulumi_aws/s3control/access_point_policy.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/s3control/bucket.py` & `pulumi_aws-5.9.2/pulumi_aws/s3control/bucket.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/s3control/bucket_lifecycle_configuration.py` & `pulumi_aws-5.9.2/pulumi_aws/s3control/bucket_lifecycle_configuration.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/s3control/bucket_policy.py` & `pulumi_aws-5.9.2/pulumi_aws/s3control/bucket_policy.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/s3control/multi_region_access_point.py` & `pulumi_aws-5.9.2/pulumi_aws/s3control/multi_region_access_point.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/s3control/multi_region_access_point_policy.py` & `pulumi_aws-5.9.2/pulumi_aws/s3control/multi_region_access_point_policy.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/s3control/object_lambda_access_point.py` & `pulumi_aws-5.9.2/pulumi_aws/s3control/object_lambda_access_point.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/s3control/object_lambda_access_point_policy.py` & `pulumi_aws-5.9.2/pulumi_aws/s3control/object_lambda_access_point_policy.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/s3control/outputs.py` & `pulumi_aws-5.9.2/pulumi_aws/s3control/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/s3outposts/_inputs.py` & `pulumi_aws-5.9.2/pulumi_aws/s3outposts/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/s3outposts/endpoint.py` & `pulumi_aws-5.9.2/pulumi_aws/s3outposts/endpoint.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/s3outposts/outputs.py` & `pulumi_aws-5.9.2/pulumi_aws/s3outposts/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/sagemaker/__init__.py` & `pulumi_aws-5.9.2/pulumi_aws/sagemaker/__init__.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/sagemaker/_inputs.py` & `pulumi_aws-5.9.2/pulumi_aws/sagemaker/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/sagemaker/app.py` & `pulumi_aws-5.9.2/pulumi_aws/sagemaker/app.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/sagemaker/app_image_config.py` & `pulumi_aws-5.9.2/pulumi_aws/sagemaker/app_image_config.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/sagemaker/code_repository.py` & `pulumi_aws-5.9.2/pulumi_aws/sagemaker/code_repository.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/sagemaker/device.py` & `pulumi_aws-5.9.2/pulumi_aws/sagemaker/device.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/sagemaker/device_fleet.py` & `pulumi_aws-5.9.2/pulumi_aws/sagemaker/device_fleet.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/sagemaker/domain.py` & `pulumi_aws-5.9.2/pulumi_aws/sagemaker/domain.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/sagemaker/endpoint.py` & `pulumi_aws-5.9.2/pulumi_aws/sagemaker/endpoint.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/sagemaker/endpoint_configuration.py` & `pulumi_aws-5.9.2/pulumi_aws/sagemaker/endpoint_configuration.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/sagemaker/feature_group.py` & `pulumi_aws-5.9.2/pulumi_aws/sagemaker/feature_group.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/sagemaker/flow_definition.py` & `pulumi_aws-5.9.2/pulumi_aws/sagemaker/flow_definition.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/sagemaker/get_prebuilt_ecr_image.py` & `pulumi_aws-5.9.2/pulumi_aws/sagemaker/get_prebuilt_ecr_image.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/sagemaker/human_task_ui.py` & `pulumi_aws-5.9.2/pulumi_aws/sagemaker/human_task_ui.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/sagemaker/image.py` & `pulumi_aws-5.9.2/pulumi_aws/sagemaker/image.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/sagemaker/image_version.py` & `pulumi_aws-5.9.2/pulumi_aws/sagemaker/image_version.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/sagemaker/model.py` & `pulumi_aws-5.9.2/pulumi_aws/sagemaker/model.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/sagemaker/model_package_group.py` & `pulumi_aws-5.9.2/pulumi_aws/sagemaker/model_package_group.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/sagemaker/model_package_group_policy.py` & `pulumi_aws-5.9.2/pulumi_aws/sagemaker/model_package_group_policy.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/sagemaker/notebook_instance.py` & `pulumi_aws-5.9.2/pulumi_aws/sagemaker/notebook_instance.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/sagemaker/notebook_instance_lifecycle_configuration.py` & `pulumi_aws-5.9.2/pulumi_aws/sagemaker/notebook_instance_lifecycle_configuration.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/sagemaker/outputs.py` & `pulumi_aws-5.9.2/pulumi_aws/sagemaker/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/sagemaker/project.py` & `pulumi_aws-5.9.2/pulumi_aws/sagemaker/project.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/sagemaker/studio_lifecycle_config.py` & `pulumi_aws-5.9.2/pulumi_aws/sagemaker/studio_lifecycle_config.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/sagemaker/user_profile.py` & `pulumi_aws-5.9.2/pulumi_aws/sagemaker/user_profile.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/sagemaker/workforce.py` & `pulumi_aws-5.9.2/pulumi_aws/sagemaker/workforce.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/sagemaker/workteam.py` & `pulumi_aws-5.9.2/pulumi_aws/sagemaker/workteam.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/schemas/discoverer.py` & `pulumi_aws-5.9.2/pulumi_aws/schemas/discoverer.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/schemas/registry.py` & `pulumi_aws-5.9.2/pulumi_aws/schemas/registry.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/schemas/schema.py` & `pulumi_aws-5.9.2/pulumi_aws/schemas/schema.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/secretsmanager/__init__.py` & `pulumi_aws-5.9.2/pulumi_aws/secretsmanager/__init__.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/secretsmanager/_inputs.py` & `pulumi_aws-5.9.2/pulumi_aws/secretsmanager/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/secretsmanager/get_secret.py` & `pulumi_aws-5.9.2/pulumi_aws/secretsmanager/get_secret.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/secretsmanager/get_secret_rotation.py` & `pulumi_aws-5.9.2/pulumi_aws/secretsmanager/get_secret_rotation.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/secretsmanager/get_secret_version.py` & `pulumi_aws-5.9.2/pulumi_aws/secretsmanager/get_secret_version.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/secretsmanager/get_secrets.py` & `pulumi_aws-5.9.2/pulumi_aws/secretsmanager/get_secrets.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/secretsmanager/outputs.py` & `pulumi_aws-5.9.2/pulumi_aws/secretsmanager/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/secretsmanager/secret.py` & `pulumi_aws-5.9.2/pulumi_aws/secretsmanager/secret.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/secretsmanager/secret_policy.py` & `pulumi_aws-5.9.2/pulumi_aws/secretsmanager/secret_policy.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/secretsmanager/secret_rotation.py` & `pulumi_aws-5.9.2/pulumi_aws/secretsmanager/secret_rotation.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/secretsmanager/secret_version.py` & `pulumi_aws-5.9.2/pulumi_aws/secretsmanager/secret_version.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/securityhub/__init__.py` & `pulumi_aws-5.9.2/pulumi_aws/securityhub/__init__.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/securityhub/_inputs.py` & `pulumi_aws-5.9.2/pulumi_aws/securityhub/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/securityhub/account.py` & `pulumi_aws-5.9.2/pulumi_aws/securityhub/account.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/securityhub/action_target.py` & `pulumi_aws-5.9.2/pulumi_aws/securityhub/action_target.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/securityhub/finding_aggregator.py` & `pulumi_aws-5.9.2/pulumi_aws/securityhub/finding_aggregator.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/securityhub/insight.py` & `pulumi_aws-5.9.2/pulumi_aws/securityhub/insight.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/securityhub/invite_accepter.py` & `pulumi_aws-5.9.2/pulumi_aws/securityhub/invite_accepter.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/securityhub/member.py` & `pulumi_aws-5.9.2/pulumi_aws/securityhub/member.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/securityhub/organization_admin_account.py` & `pulumi_aws-5.9.2/pulumi_aws/securityhub/organization_admin_account.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/securityhub/organization_configuration.py` & `pulumi_aws-5.9.2/pulumi_aws/securityhub/organization_configuration.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/securityhub/outputs.py` & `pulumi_aws-5.9.2/pulumi_aws/securityhub/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/securityhub/product_subscription.py` & `pulumi_aws-5.9.2/pulumi_aws/securityhub/product_subscription.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/securityhub/standards_control.py` & `pulumi_aws-5.9.2/pulumi_aws/securityhub/standards_control.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/securityhub/standards_subscription.py` & `pulumi_aws-5.9.2/pulumi_aws/securityhub/standards_subscription.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/serverlessrepository/cloud_formation_stack.py` & `pulumi_aws-5.9.2/pulumi_aws/serverlessrepository/cloud_formation_stack.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/serverlessrepository/get_application.py` & `pulumi_aws-5.9.2/pulumi_aws/serverlessrepository/get_application.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/servicecatalog/__init__.py` & `pulumi_aws-5.9.2/pulumi_aws/servicecatalog/__init__.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/servicecatalog/_inputs.py` & `pulumi_aws-5.9.2/pulumi_aws/servicecatalog/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/servicecatalog/budget_resource_association.py` & `pulumi_aws-5.9.2/pulumi_aws/servicecatalog/budget_resource_association.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/servicecatalog/constraint.py` & `pulumi_aws-5.9.2/pulumi_aws/servicecatalog/constraint.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/servicecatalog/get_constraint.py` & `pulumi_aws-5.9.2/pulumi_aws/servicecatalog/get_constraint.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/servicecatalog/get_launch_paths.py` & `pulumi_aws-5.9.2/pulumi_aws/servicecatalog/get_launch_paths.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/servicecatalog/get_portfolio.py` & `pulumi_aws-5.9.2/pulumi_aws/servicecatalog/get_portfolio.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/servicecatalog/get_portfolio_constraints.py` & `pulumi_aws-5.9.2/pulumi_aws/servicecatalog/get_portfolio_constraints.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/servicecatalog/get_product.py` & `pulumi_aws-5.9.2/pulumi_aws/servicecatalog/get_product.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/servicecatalog/organizations_access.py` & `pulumi_aws-5.9.2/pulumi_aws/servicecatalog/organizations_access.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/servicecatalog/outputs.py` & `pulumi_aws-5.9.2/pulumi_aws/servicecatalog/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/servicecatalog/portfolio.py` & `pulumi_aws-5.9.2/pulumi_aws/servicecatalog/portfolio.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/servicecatalog/portfolio_share.py` & `pulumi_aws-5.9.2/pulumi_aws/servicecatalog/portfolio_share.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/servicecatalog/principal_portfolio_association.py` & `pulumi_aws-5.9.2/pulumi_aws/servicecatalog/principal_portfolio_association.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/servicecatalog/product.py` & `pulumi_aws-5.9.2/pulumi_aws/servicecatalog/product.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/servicecatalog/product_portfolio_association.py` & `pulumi_aws-5.9.2/pulumi_aws/servicecatalog/product_portfolio_association.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/servicecatalog/provisioned_product.py` & `pulumi_aws-5.9.2/pulumi_aws/servicecatalog/provisioned_product.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/servicecatalog/provisioning_artifact.py` & `pulumi_aws-5.9.2/pulumi_aws/servicecatalog/provisioning_artifact.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/servicecatalog/service_action.py` & `pulumi_aws-5.9.2/pulumi_aws/servicecatalog/service_action.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/servicecatalog/tag_option.py` & `pulumi_aws-5.9.2/pulumi_aws/servicecatalog/tag_option.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/servicecatalog/tag_option_resource_association.py` & `pulumi_aws-5.9.2/pulumi_aws/servicecatalog/tag_option_resource_association.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/servicediscovery/_inputs.py` & `pulumi_aws-5.9.2/pulumi_aws/servicediscovery/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/servicediscovery/get_dns_namespace.py` & `pulumi_aws-5.9.2/pulumi_aws/servicediscovery/get_dns_namespace.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/servicediscovery/http_namespace.py` & `pulumi_aws-5.9.2/pulumi_aws/servicediscovery/http_namespace.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/servicediscovery/instance.py` & `pulumi_aws-5.9.2/pulumi_aws/servicediscovery/instance.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/servicediscovery/outputs.py` & `pulumi_aws-5.9.2/pulumi_aws/servicediscovery/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/servicediscovery/private_dns_namespace.py` & `pulumi_aws-5.9.2/pulumi_aws/servicediscovery/private_dns_namespace.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/servicediscovery/public_dns_namespace.py` & `pulumi_aws-5.9.2/pulumi_aws/servicediscovery/public_dns_namespace.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/servicediscovery/service.py` & `pulumi_aws-5.9.2/pulumi_aws/servicediscovery/service.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/servicequotas/get_service.py` & `pulumi_aws-5.9.2/pulumi_aws/servicequotas/get_service.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/servicequotas/get_service_quota.py` & `pulumi_aws-5.9.2/pulumi_aws/servicequotas/get_service_quota.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/servicequotas/service_quota.py` & `pulumi_aws-5.9.2/pulumi_aws/servicequotas/service_quota.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ses/__init__.py` & `pulumi_aws-5.9.2/pulumi_aws/ses/__init__.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ses/_inputs.py` & `pulumi_aws-5.9.2/pulumi_aws/ses/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ses/active_receipt_rule_set.py` & `pulumi_aws-5.9.2/pulumi_aws/ses/active_receipt_rule_set.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ses/confguration_set.py` & `pulumi_aws-5.9.2/pulumi_aws/ses/confguration_set.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ses/configuration_set.py` & `pulumi_aws-5.9.2/pulumi_aws/ses/configuration_set.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ses/domain_dkim.py` & `pulumi_aws-5.9.2/pulumi_aws/ses/domain_dkim.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ses/domain_identity.py` & `pulumi_aws-5.9.2/pulumi_aws/ses/domain_identity.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ses/domain_identity_verification.py` & `pulumi_aws-5.9.2/pulumi_aws/ses/domain_identity_verification.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ses/email_identity.py` & `pulumi_aws-5.9.2/pulumi_aws/ses/email_identity.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ses/event_destination.py` & `pulumi_aws-5.9.2/pulumi_aws/ses/event_destination.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ses/get_active_receipt_rule_set.py` & `pulumi_aws-5.9.2/pulumi_aws/ses/get_active_receipt_rule_set.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ses/get_domain_identity.py` & `pulumi_aws-5.9.2/pulumi_aws/ses/get_domain_identity.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ses/get_email_identity.py` & `pulumi_aws-5.9.2/pulumi_aws/ses/get_email_identity.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ses/identity_notification_topic.py` & `pulumi_aws-5.9.2/pulumi_aws/ses/identity_notification_topic.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ses/identity_policy.py` & `pulumi_aws-5.9.2/pulumi_aws/ses/identity_policy.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ses/mail_from.py` & `pulumi_aws-5.9.2/pulumi_aws/ses/mail_from.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ses/outputs.py` & `pulumi_aws-5.9.2/pulumi_aws/ses/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ses/receipt_filter.py` & `pulumi_aws-5.9.2/pulumi_aws/ses/receipt_filter.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ses/receipt_rule.py` & `pulumi_aws-5.9.2/pulumi_aws/ses/receipt_rule.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ses/receipt_rule_set.py` & `pulumi_aws-5.9.2/pulumi_aws/ses/receipt_rule_set.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ses/template.py` & `pulumi_aws-5.9.2/pulumi_aws/ses/template.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/sfn/_inputs.py` & `pulumi_aws-5.9.2/pulumi_aws/sfn/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/sfn/activity.py` & `pulumi_aws-5.9.2/pulumi_aws/sfn/activity.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/sfn/get_activity.py` & `pulumi_aws-5.9.2/pulumi_aws/sfn/get_activity.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/sfn/get_state_machine.py` & `pulumi_aws-5.9.2/pulumi_aws/sfn/get_state_machine.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/sfn/outputs.py` & `pulumi_aws-5.9.2/pulumi_aws/sfn/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/sfn/state_machine.py` & `pulumi_aws-5.9.2/pulumi_aws/sfn/state_machine.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/shield/protection.py` & `pulumi_aws-5.9.2/pulumi_aws/shield/protection.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/shield/protection_group.py` & `pulumi_aws-5.9.2/pulumi_aws/shield/protection_group.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/shield/protection_health_check_association.py` & `pulumi_aws-5.9.2/pulumi_aws/shield/protection_health_check_association.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/signer/_inputs.py` & `pulumi_aws-5.9.2/pulumi_aws/signer/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/signer/get_signing_job.py` & `pulumi_aws-5.9.2/pulumi_aws/signer/get_signing_job.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/signer/get_signing_profile.py` & `pulumi_aws-5.9.2/pulumi_aws/signer/get_signing_profile.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/signer/outputs.py` & `pulumi_aws-5.9.2/pulumi_aws/signer/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/signer/signing_job.py` & `pulumi_aws-5.9.2/pulumi_aws/signer/signing_job.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/signer/signing_profile.py` & `pulumi_aws-5.9.2/pulumi_aws/signer/signing_profile.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/signer/signing_profile_permission.py` & `pulumi_aws-5.9.2/pulumi_aws/signer/signing_profile_permission.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/simpledb/domain.py` & `pulumi_aws-5.9.2/pulumi_aws/simpledb/domain.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/sns/get_topic.py` & `pulumi_aws-5.9.2/pulumi_aws/sns/get_topic.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/sns/platform_application.py` & `pulumi_aws-5.9.2/pulumi_aws/sns/platform_application.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/sns/sms_preferences.py` & `pulumi_aws-5.9.2/pulumi_aws/sns/sms_preferences.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/sns/topic.py` & `pulumi_aws-5.9.2/pulumi_aws/sns/topic.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/sns/topic_policy.py` & `pulumi_aws-5.9.2/pulumi_aws/sns/topic_policy.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/sns/topic_subscription.py` & `pulumi_aws-5.9.2/pulumi_aws/sns/topic_subscription.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/sqs/get_queue.py` & `pulumi_aws-5.9.2/pulumi_aws/sqs/get_queue.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/sqs/queue.py` & `pulumi_aws-5.9.2/pulumi_aws/sqs/queue.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/sqs/queue_policy.py` & `pulumi_aws-5.9.2/pulumi_aws/sqs/queue_policy.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ssm/__init__.py` & `pulumi_aws-5.9.2/pulumi_aws/ssm/__init__.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ssm/_inputs.py` & `pulumi_aws-5.9.2/pulumi_aws/ssm/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ssm/activation.py` & `pulumi_aws-5.9.2/pulumi_aws/ssm/activation.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ssm/association.py` & `pulumi_aws-5.9.2/pulumi_aws/ssm/association.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ssm/document.py` & `pulumi_aws-5.9.2/pulumi_aws/ssm/document.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ssm/get_document.py` & `pulumi_aws-5.9.2/pulumi_aws/ssm/get_document.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ssm/get_instances.py` & `pulumi_aws-5.9.2/pulumi_aws/ssm/get_instances.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ssm/get_maintenance_windows.py` & `pulumi_aws-5.9.2/pulumi_aws/ssm/get_maintenance_windows.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ssm/get_parameter.py` & `pulumi_aws-5.9.2/pulumi_aws/ssm/get_parameter.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ssm/get_parameters_by_path.py` & `pulumi_aws-5.9.2/pulumi_aws/ssm/get_parameters_by_path.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ssm/get_patch_baseline.py` & `pulumi_aws-5.9.2/pulumi_aws/ssm/get_patch_baseline.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ssm/maintenance_window.py` & `pulumi_aws-5.9.2/pulumi_aws/ssm/maintenance_window.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ssm/maintenance_window_target.py` & `pulumi_aws-5.9.2/pulumi_aws/ssm/maintenance_window_target.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ssm/maintenance_window_task.py` & `pulumi_aws-5.9.2/pulumi_aws/ssm/maintenance_window_task.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ssm/outputs.py` & `pulumi_aws-5.9.2/pulumi_aws/ssm/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ssm/parameter.py` & `pulumi_aws-5.9.2/pulumi_aws/ssm/parameter.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ssm/patch_baseline.py` & `pulumi_aws-5.9.2/pulumi_aws/ssm/patch_baseline.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ssm/patch_group.py` & `pulumi_aws-5.9.2/pulumi_aws/ssm/patch_group.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ssm/resource_data_sync.py` & `pulumi_aws-5.9.2/pulumi_aws/ssm/resource_data_sync.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ssoadmin/account_assignment.py` & `pulumi_aws-5.9.2/pulumi_aws/ssoadmin/account_assignment.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ssoadmin/get_instances.py` & `pulumi_aws-5.9.2/pulumi_aws/ssoadmin/get_instances.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ssoadmin/get_permission_set.py` & `pulumi_aws-5.9.2/pulumi_aws/ssoadmin/get_permission_set.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ssoadmin/managed_policy_attachment.py` & `pulumi_aws-5.9.2/pulumi_aws/ssoadmin/managed_policy_attachment.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ssoadmin/permission_set.py` & `pulumi_aws-5.9.2/pulumi_aws/ssoadmin/permission_set.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/ssoadmin/permission_set_inline_policy.py` & `pulumi_aws-5.9.2/pulumi_aws/ssoadmin/permission_set_inline_policy.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/storagegateway/__init__.py` & `pulumi_aws-5.9.2/pulumi_aws/storagegateway/__init__.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/storagegateway/_inputs.py` & `pulumi_aws-5.9.2/pulumi_aws/storagegateway/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/storagegateway/cache.py` & `pulumi_aws-5.9.2/pulumi_aws/storagegateway/cache.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/storagegateway/caches_iscsi_volume.py` & `pulumi_aws-5.9.2/pulumi_aws/storagegateway/caches_iscsi_volume.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/storagegateway/file_system_association.py` & `pulumi_aws-5.9.2/pulumi_aws/storagegateway/file_system_association.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/storagegateway/gateway.py` & `pulumi_aws-5.9.2/pulumi_aws/storagegateway/gateway.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/storagegateway/get_local_disk.py` & `pulumi_aws-5.9.2/pulumi_aws/storagegateway/get_local_disk.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/storagegateway/nfs_file_share.py` & `pulumi_aws-5.9.2/pulumi_aws/storagegateway/nfs_file_share.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/storagegateway/outputs.py` & `pulumi_aws-5.9.2/pulumi_aws/storagegateway/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/storagegateway/smb_file_share.py` & `pulumi_aws-5.9.2/pulumi_aws/storagegateway/smb_file_share.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/storagegateway/stored_iscsi_volume.py` & `pulumi_aws-5.9.2/pulumi_aws/storagegateway/stored_iscsi_volume.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/storagegateway/tape_pool.py` & `pulumi_aws-5.9.2/pulumi_aws/storagegateway/tape_pool.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/storagegateway/upload_buffer.py` & `pulumi_aws-5.9.2/pulumi_aws/storagegateway/upload_buffer.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/storagegateway/working_storage.py` & `pulumi_aws-5.9.2/pulumi_aws/storagegateway/working_storage.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/swf/domain.py` & `pulumi_aws-5.9.2/pulumi_aws/swf/domain.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/synthetics/_inputs.py` & `pulumi_aws-5.9.2/pulumi_aws/synthetics/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/synthetics/canary.py` & `pulumi_aws-5.9.2/pulumi_aws/synthetics/canary.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/synthetics/outputs.py` & `pulumi_aws-5.9.2/pulumi_aws/synthetics/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/timestreamwrite/_inputs.py` & `pulumi_aws-5.9.2/pulumi_aws/timestreamwrite/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/timestreamwrite/database.py` & `pulumi_aws-5.9.2/pulumi_aws/timestreamwrite/database.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/timestreamwrite/outputs.py` & `pulumi_aws-5.9.2/pulumi_aws/timestreamwrite/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/timestreamwrite/table.py` & `pulumi_aws-5.9.2/pulumi_aws/timestreamwrite/table.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/transfer/_inputs.py` & `pulumi_aws-5.9.2/pulumi_aws/transfer/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/transfer/access.py` & `pulumi_aws-5.9.2/pulumi_aws/transfer/access.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/transfer/get_server.py` & `pulumi_aws-5.9.2/pulumi_aws/transfer/get_server.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/transfer/outputs.py` & `pulumi_aws-5.9.2/pulumi_aws/transfer/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/transfer/server.py` & `pulumi_aws-5.9.2/pulumi_aws/transfer/server.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/transfer/ssh_key.py` & `pulumi_aws-5.9.2/pulumi_aws/transfer/ssh_key.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/transfer/user.py` & `pulumi_aws-5.9.2/pulumi_aws/transfer/user.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/transfer/workflow.py` & `pulumi_aws-5.9.2/pulumi_aws/transfer/workflow.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/waf/__init__.py` & `pulumi_aws-5.9.2/pulumi_aws/waf/__init__.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/waf/_inputs.py` & `pulumi_aws-5.9.2/pulumi_aws/waf/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/waf/byte_match_set.py` & `pulumi_aws-5.9.2/pulumi_aws/waf/byte_match_set.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/waf/geo_match_set.py` & `pulumi_aws-5.9.2/pulumi_aws/waf/geo_match_set.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/waf/get_ipset.py` & `pulumi_aws-5.9.2/pulumi_aws/waf/get_ipset.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/waf/get_rate_based_rule.py` & `pulumi_aws-5.9.2/pulumi_aws/waf/get_rate_based_rule.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/waf/get_rule.py` & `pulumi_aws-5.9.2/pulumi_aws/waf/get_rule.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/waf/get_web_acl.py` & `pulumi_aws-5.9.2/pulumi_aws/waf/get_web_acl.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/waf/ip_set.py` & `pulumi_aws-5.9.2/pulumi_aws/waf/ip_set.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/waf/outputs.py` & `pulumi_aws-5.9.2/pulumi_aws/waf/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/waf/rate_based_rule.py` & `pulumi_aws-5.9.2/pulumi_aws/waf/rate_based_rule.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/waf/regex_match_set.py` & `pulumi_aws-5.9.2/pulumi_aws/waf/regex_match_set.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/waf/regex_pattern_set.py` & `pulumi_aws-5.9.2/pulumi_aws/waf/regex_pattern_set.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/waf/rule.py` & `pulumi_aws-5.9.2/pulumi_aws/waf/rule.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/waf/rule_group.py` & `pulumi_aws-5.9.2/pulumi_aws/waf/rule_group.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/waf/size_constraint_set.py` & `pulumi_aws-5.9.2/pulumi_aws/waf/size_constraint_set.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/waf/sql_injection_match_set.py` & `pulumi_aws-5.9.2/pulumi_aws/waf/sql_injection_match_set.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/waf/web_acl.py` & `pulumi_aws-5.9.2/pulumi_aws/waf/web_acl.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/waf/xss_match_set.py` & `pulumi_aws-5.9.2/pulumi_aws/waf/xss_match_set.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/wafregional/__init__.py` & `pulumi_aws-5.9.2/pulumi_aws/wafregional/__init__.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/wafregional/_inputs.py` & `pulumi_aws-5.9.2/pulumi_aws/wafregional/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/wafregional/byte_match_set.py` & `pulumi_aws-5.9.2/pulumi_aws/wafregional/byte_match_set.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/wafregional/geo_match_set.py` & `pulumi_aws-5.9.2/pulumi_aws/wafregional/geo_match_set.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/wafregional/get_ipset.py` & `pulumi_aws-5.9.2/pulumi_aws/wafregional/get_ipset.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/wafregional/get_rate_based_mod.py` & `pulumi_aws-5.9.2/pulumi_aws/wafregional/get_rate_based_mod.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/wafregional/get_rule.py` & `pulumi_aws-5.9.2/pulumi_aws/wafregional/get_rule.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/wafregional/get_web_acl.py` & `pulumi_aws-5.9.2/pulumi_aws/wafregional/get_web_acl.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/wafregional/ip_set.py` & `pulumi_aws-5.9.2/pulumi_aws/wafregional/ip_set.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/wafregional/outputs.py` & `pulumi_aws-5.9.2/pulumi_aws/wafregional/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/wafregional/rate_based_rule.py` & `pulumi_aws-5.9.2/pulumi_aws/wafregional/rate_based_rule.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/wafregional/regex_match_set.py` & `pulumi_aws-5.9.2/pulumi_aws/wafregional/regex_match_set.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/wafregional/regex_pattern_set.py` & `pulumi_aws-5.9.2/pulumi_aws/wafregional/regex_pattern_set.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/wafregional/rule.py` & `pulumi_aws-5.9.2/pulumi_aws/wafregional/rule.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/wafregional/rule_group.py` & `pulumi_aws-5.9.2/pulumi_aws/wafregional/rule_group.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/wafregional/size_constraint_set.py` & `pulumi_aws-5.9.2/pulumi_aws/wafregional/size_constraint_set.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/wafregional/sql_injection_match_set.py` & `pulumi_aws-5.9.2/pulumi_aws/wafregional/sql_injection_match_set.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/wafregional/web_acl.py` & `pulumi_aws-5.9.2/pulumi_aws/wafregional/web_acl.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/wafregional/web_acl_association.py` & `pulumi_aws-5.9.2/pulumi_aws/wafregional/web_acl_association.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/wafregional/xss_match_set.py` & `pulumi_aws-5.9.2/pulumi_aws/wafregional/xss_match_set.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/wafv2/__init__.py` & `pulumi_aws-5.9.2/pulumi_aws/wafv2/__init__.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/wafv2/_inputs.py` & `pulumi_aws-5.9.2/pulumi_aws/wafv2/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/wafv2/get_ip_set.py` & `pulumi_aws-5.9.2/pulumi_aws/wafv2/get_ip_set.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/wafv2/get_regex_pattern_set.py` & `pulumi_aws-5.9.2/pulumi_aws/wafv2/get_regex_pattern_set.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/wafv2/get_rule_group.py` & `pulumi_aws-5.9.2/pulumi_aws/wafv2/get_rule_group.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/wafv2/get_web_acl.py` & `pulumi_aws-5.9.2/pulumi_aws/wafv2/get_web_acl.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/wafv2/ip_set.py` & `pulumi_aws-5.9.2/pulumi_aws/wafv2/ip_set.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/wafv2/outputs.py` & `pulumi_aws-5.9.2/pulumi_aws/wafv2/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/wafv2/regex_pattern_set.py` & `pulumi_aws-5.9.2/pulumi_aws/wafv2/regex_pattern_set.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/wafv2/rule_group.py` & `pulumi_aws-5.9.2/pulumi_aws/wafv2/rule_group.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/wafv2/web_acl.py` & `pulumi_aws-5.9.2/pulumi_aws/wafv2/web_acl.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/wafv2/web_acl_association.py` & `pulumi_aws-5.9.2/pulumi_aws/wafv2/web_acl_association.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/wafv2/web_acl_logging_configuration.py` & `pulumi_aws-5.9.2/pulumi_aws/wafv2/web_acl_logging_configuration.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/worklink/_inputs.py` & `pulumi_aws-5.9.2/pulumi_aws/worklink/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/worklink/fleet.py` & `pulumi_aws-5.9.2/pulumi_aws/worklink/fleet.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/worklink/outputs.py` & `pulumi_aws-5.9.2/pulumi_aws/worklink/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/worklink/website_certificate_authority_association.py` & `pulumi_aws-5.9.2/pulumi_aws/worklink/website_certificate_authority_association.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/workspaces/_inputs.py` & `pulumi_aws-5.9.2/pulumi_aws/workspaces/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/workspaces/directory.py` & `pulumi_aws-5.9.2/pulumi_aws/workspaces/directory.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/workspaces/get_bundle.py` & `pulumi_aws-5.9.2/pulumi_aws/workspaces/get_bundle.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/workspaces/get_directory.py` & `pulumi_aws-5.9.2/pulumi_aws/workspaces/get_directory.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/workspaces/get_image.py` & `pulumi_aws-5.9.2/pulumi_aws/workspaces/get_image.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/workspaces/get_workspace.py` & `pulumi_aws-5.9.2/pulumi_aws/workspaces/get_workspace.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/workspaces/ip_group.py` & `pulumi_aws-5.9.2/pulumi_aws/workspaces/ip_group.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/workspaces/outputs.py` & `pulumi_aws-5.9.2/pulumi_aws/workspaces/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/workspaces/workspace.py` & `pulumi_aws-5.9.2/pulumi_aws/workspaces/workspace.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/xray/_inputs.py` & `pulumi_aws-5.9.2/pulumi_aws/xray/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/xray/encryption_config.py` & `pulumi_aws-5.9.2/pulumi_aws/xray/encryption_config.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/xray/group.py` & `pulumi_aws-5.9.2/pulumi_aws/xray/group.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/xray/outputs.py` & `pulumi_aws-5.9.2/pulumi_aws/xray/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws/xray/sampling_rule.py` & `pulumi_aws-5.9.2/pulumi_aws/xray/sampling_rule.py`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/pulumi_aws.egg-info/PKG-INFO` & `pulumi_aws-5.9.2/pulumi_aws.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: pulumi-aws
-Version: 5.9.1
+Version: 5.9.2
 Summary: A Pulumi package for creating and managing Amazon Web Services (AWS) cloud resources.
 Home-page: https://pulumi.io
 License: Apache-2.0
 Project-URL: Repository, https://github.com/pulumi/pulumi-aws
 Description: [![Actions Status](https://github.com/pulumi/pulumi-aws/workflows/master/badge.svg)](https://github.com/pulumi/pulumi-aws/actions)
         [![Slack](http://www.pulumi.com/images/docs/badges/slack.svg)](https://slack.pulumi.com)
         [![NPM version](https://badge.fury.io/js/%40pulumi%2Faws.svg)](https://www.npmjs.com/package/@pulumi/aws)
```

#### html2text {}

```diff
@@ -1,8 +1,8 @@
-Metadata-Version: 2.1 Name: pulumi-aws Version: 5.9.1 Summary: A Pulumi package
+Metadata-Version: 2.1 Name: pulumi-aws Version: 5.9.2 Summary: A Pulumi package
 for creating and managing Amazon Web Services (AWS) cloud resources. Home-page:
 https://pulumi.io License: Apache-2.0 Project-URL: Repository, https://
 github.com/pulumi/pulumi-aws Description: [![Actions Status](https://
 github.com/pulumi/pulumi-aws/workflows/master/badge.svg)](https://github.com/
 pulumi/pulumi-aws/actions) [![Slack](http://www.pulumi.com/images/docs/badges/
 slack.svg)](https://slack.pulumi.com) [![NPM version](https://badge.fury.io/js/
 %40pulumi%2Faws.svg)](https://www.npmjs.com/package/@pulumi/aws) [![Python
```

### Comparing `pulumi_aws-5.9.1/pulumi_aws.egg-info/SOURCES.txt` & `pulumi_aws-5.9.2/pulumi_aws.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `pulumi_aws-5.9.1/setup.py` & `pulumi_aws-5.9.2/setup.py`

 * *Files 5% similar despite different names*

```diff
@@ -4,16 +4,16 @@
 
 import errno
 from setuptools import setup, find_packages
 from setuptools.command.install import install
 from subprocess import check_call
 
 
-VERSION = "5.9.1"
-PLUGIN_VERSION = "5.9.1"
+VERSION = "5.9.2"
+PLUGIN_VERSION = "5.9.2"
 
 class InstallPluginCommand(install):
     def run(self):
         install.run(self)
         try:
             check_call(['pulumi', 'plugin', 'install', 'resource', 'aws', PLUGIN_VERSION])
         except OSError as error:
```

