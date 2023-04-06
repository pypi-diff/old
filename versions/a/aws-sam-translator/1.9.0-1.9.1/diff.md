# Comparing `tmp/aws-sam-translator-1.9.0.tar.gz` & `tmp/aws-sam-translator-1.9.1.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "dist/aws-sam-translator-1.9.0.tar", last modified: Thu Nov 29 17:57:55 2018, max compression
+gzip compressed data, was "dist/aws-sam-translator-1.9.1.tar", last modified: Thu Feb  7 23:21:23 2019, max compression
```

## Comparing `aws-sam-translator-1.9.0.tar` & `aws-sam-translator-1.9.1.tar`

### file list

```diff
@@ -1,127 +1,127 @@
-drwxr-xr-x   0 root         (0) root         (0)        0 2018-11-29 17:57:55.000000 aws-sam-translator-1.9.0/
-drwxr-xr-x   0 root         (0) root         (0)        0 2018-11-29 17:57:54.000000 aws-sam-translator-1.9.0/aws_sam_translator.egg-info/
--rw-r--r--   0 root         (0) root         (0)        1 2018-11-29 17:57:53.000000 aws-sam-translator-1.9.0/aws_sam_translator.egg-info/dependency_links.txt
--rw-r--r--   0 root         (0) root         (0)     2960 2018-11-29 17:57:53.000000 aws-sam-translator-1.9.0/aws_sam_translator.egg-info/PKG-INFO
--rw-r--r--   0 root         (0) root         (0)      270 2018-11-29 17:57:53.000000 aws-sam-translator-1.9.0/aws_sam_translator.egg-info/requires.txt
--rw-r--r--   0 root         (0) root         (0)     3761 2018-11-29 17:57:53.000000 aws-sam-translator-1.9.0/aws_sam_translator.egg-info/SOURCES.txt
--rw-r--r--   0 root         (0) root         (0)       20 2018-11-29 17:57:53.000000 aws-sam-translator-1.9.0/aws_sam_translator.egg-info/top_level.txt
--rw-r--r--   0 root         (0) root         (0)    11357 2018-11-29 17:53:32.000000 aws-sam-translator-1.9.0/LICENSE
--rwxr-xr-x   0 root         (0) root         (0)      283 2018-11-29 17:53:32.000000 aws-sam-translator-1.9.0/MANIFEST.in
--rw-r--r--   0 root         (0) root         (0)     2960 2018-11-29 17:57:55.000000 aws-sam-translator-1.9.0/PKG-INFO
--rw-r--r--   0 root         (0) root         (0)     1784 2018-11-29 17:53:32.000000 aws-sam-translator-1.9.0/README.md
-drwxr-xr-x   0 root         (0) root         (0)        0 2018-11-29 17:57:54.000000 aws-sam-translator-1.9.0/requirements/
--rwxr-xr-x   0 root         (0) root         (0)       72 2018-11-29 17:53:32.000000 aws-sam-translator-1.9.0/requirements/base.txt
--rw-r--r--   0 root         (0) root         (0)      228 2018-11-29 17:53:32.000000 aws-sam-translator-1.9.0/requirements/dev.txt
-drwxr-xr-x   0 root         (0) root         (0)        0 2018-11-29 17:57:54.000000 aws-sam-translator-1.9.0/samtranslator/
--rw-r--r--   0 root         (0) root         (0)       22 2018-11-29 17:53:32.000000 aws-sam-translator-1.9.0/samtranslator/__init__.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2018-11-29 17:57:54.000000 aws-sam-translator-1.9.0/samtranslator/intrinsics/
--rw-r--r--   0 root         (0) root         (0)        0 2018-11-29 17:53:32.000000 aws-sam-translator-1.9.0/samtranslator/intrinsics/__init__.py
--rw-r--r--   0 root         (0) root         (0)    22078 2018-11-29 17:53:32.000000 aws-sam-translator-1.9.0/samtranslator/intrinsics/actions.py
--rw-r--r--   0 root         (0) root         (0)    11718 2018-11-29 17:53:32.000000 aws-sam-translator-1.9.0/samtranslator/intrinsics/resolver.py
--rw-r--r--   0 root         (0) root         (0)     2940 2018-11-29 17:53:32.000000 aws-sam-translator-1.9.0/samtranslator/intrinsics/resource_refs.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2018-11-29 17:57:54.000000 aws-sam-translator-1.9.0/samtranslator/model/
--rw-r--r--   0 root         (0) root         (0)    21265 2018-11-29 17:53:32.000000 aws-sam-translator-1.9.0/samtranslator/model/__init__.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2018-11-29 17:57:54.000000 aws-sam-translator-1.9.0/samtranslator/model/api/
--rw-r--r--   0 root         (0) root         (0)        0 2018-11-29 17:53:32.000000 aws-sam-translator-1.9.0/samtranslator/model/api/__init__.py
--rw-r--r--   0 root         (0) root         (0)    14610 2018-11-29 17:53:32.000000 aws-sam-translator-1.9.0/samtranslator/model/api/api_generator.py
--rw-r--r--   0 root         (0) root         (0)    10617 2018-11-29 17:53:32.000000 aws-sam-translator-1.9.0/samtranslator/model/apigateway.py
--rw-r--r--   0 root         (0) root         (0)      758 2018-11-29 17:53:32.000000 aws-sam-translator-1.9.0/samtranslator/model/cloudformation.py
--rw-r--r--   0 root         (0) root         (0)     1102 2018-11-29 17:53:32.000000 aws-sam-translator-1.9.0/samtranslator/model/codedeploy.py
--rw-r--r--   0 root         (0) root         (0)     1223 2018-11-29 17:53:32.000000 aws-sam-translator-1.9.0/samtranslator/model/dynamodb.py
--rw-r--r--   0 root         (0) root         (0)      829 2018-11-29 17:53:32.000000 aws-sam-translator-1.9.0/samtranslator/model/events.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2018-11-29 17:57:54.000000 aws-sam-translator-1.9.0/samtranslator/model/eventsources/
--rw-r--r--   0 root         (0) root         (0)        0 2018-11-29 17:53:32.000000 aws-sam-translator-1.9.0/samtranslator/model/eventsources/__init__.py
--rw-r--r--   0 root         (0) root         (0)     2152 2018-11-29 17:53:32.000000 aws-sam-translator-1.9.0/samtranslator/model/eventsources/cloudwatchlogs.py
--rw-r--r--   0 root         (0) root         (0)     4088 2018-11-29 17:53:32.000000 aws-sam-translator-1.9.0/samtranslator/model/eventsources/pull.py
--rw-r--r--   0 root         (0) root         (0)    23274 2018-11-29 17:53:32.000000 aws-sam-translator-1.9.0/samtranslator/model/eventsources/push.py
--rw-r--r--   0 root         (0) root         (0)     3243 2018-11-29 17:53:32.000000 aws-sam-translator-1.9.0/samtranslator/model/exceptions.py
--rw-r--r--   0 root         (0) root         (0)     5827 2018-11-29 17:53:32.000000 aws-sam-translator-1.9.0/samtranslator/model/function_policies.py
--rw-r--r--   0 root         (0) root         (0)     1941 2018-11-29 17:53:32.000000 aws-sam-translator-1.9.0/samtranslator/model/iam.py
--rw-r--r--   0 root         (0) root         (0)     1834 2018-11-29 17:53:32.000000 aws-sam-translator-1.9.0/samtranslator/model/intrinsics.py
--rw-r--r--   0 root         (0) root         (0)      468 2018-11-29 17:53:32.000000 aws-sam-translator-1.9.0/samtranslator/model/iot.py
--rw-r--r--   0 root         (0) root         (0)     3913 2018-11-29 17:53:32.000000 aws-sam-translator-1.9.0/samtranslator/model/lambda_.py
--rw-r--r--   0 root         (0) root         (0)      581 2018-11-29 17:53:32.000000 aws-sam-translator-1.9.0/samtranslator/model/log.py
--rw-r--r--   0 root         (0) root         (0)      427 2018-11-29 17:53:32.000000 aws-sam-translator-1.9.0/samtranslator/model/naming.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2018-11-29 17:57:54.000000 aws-sam-translator-1.9.0/samtranslator/model/preferences/
--rw-r--r--   0 root         (0) root         (0)        0 2018-11-29 17:53:32.000000 aws-sam-translator-1.9.0/samtranslator/model/preferences/__init__.py
--rw-r--r--   0 root         (0) root         (0)     3449 2018-11-29 17:53:32.000000 aws-sam-translator-1.9.0/samtranslator/model/preferences/deployment_preference.py
--rw-r--r--   0 root         (0) root         (0)     6687 2018-11-29 17:53:32.000000 aws-sam-translator-1.9.0/samtranslator/model/preferences/deployment_preference_collection.py
--rw-r--r--   0 root         (0) root         (0)     1434 2018-11-29 17:53:32.000000 aws-sam-translator-1.9.0/samtranslator/model/s3.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2018-11-29 17:57:54.000000 aws-sam-translator-1.9.0/samtranslator/model/s3_utils/
--rw-r--r--   0 root         (0) root         (0)        0 2018-11-29 17:53:32.000000 aws-sam-translator-1.9.0/samtranslator/model/s3_utils/__init__.py
--rw-r--r--   0 root         (0) root         (0)     3142 2018-11-29 17:53:32.000000 aws-sam-translator-1.9.0/samtranslator/model/s3_utils/uri_parser.py
--rw-r--r--   0 root         (0) root         (0)    33153 2018-11-29 17:53:32.000000 aws-sam-translator-1.9.0/samtranslator/model/sam_resources.py
--rw-r--r--   0 root         (0) root         (0)      358 2018-11-29 17:53:32.000000 aws-sam-translator-1.9.0/samtranslator/model/sns.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2018-11-29 17:57:54.000000 aws-sam-translator-1.9.0/samtranslator/model/tags/
--rw-r--r--   0 root         (0) root         (0)        0 2018-11-29 17:53:32.000000 aws-sam-translator-1.9.0/samtranslator/model/tags/__init__.py
--rw-r--r--   0 root         (0) root         (0)      797 2018-11-29 17:53:32.000000 aws-sam-translator-1.9.0/samtranslator/model/tags/resource_tagging.py
--rw-r--r--   0 root         (0) root         (0)     4593 2018-11-29 17:53:32.000000 aws-sam-translator-1.9.0/samtranslator/model/types.py
--rw-r--r--   0 root         (0) root         (0)     1642 2018-11-29 17:53:32.000000 aws-sam-translator-1.9.0/samtranslator/model/update_policy.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2018-11-29 17:57:54.000000 aws-sam-translator-1.9.0/samtranslator/parser/
--rw-r--r--   0 root         (0) root         (0)        0 2018-11-29 17:53:32.000000 aws-sam-translator-1.9.0/samtranslator/parser/__init__.py
--rw-r--r--   0 root         (0) root         (0)     1723 2018-11-29 17:53:32.000000 aws-sam-translator-1.9.0/samtranslator/parser/parser.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2018-11-29 17:57:54.000000 aws-sam-translator-1.9.0/samtranslator/plugins/
--rw-r--r--   0 root         (0) root         (0)     9216 2018-11-29 17:53:32.000000 aws-sam-translator-1.9.0/samtranslator/plugins/__init__.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2018-11-29 17:57:54.000000 aws-sam-translator-1.9.0/samtranslator/plugins/api/
--rw-r--r--   0 root         (0) root         (0)        0 2018-11-29 17:53:32.000000 aws-sam-translator-1.9.0/samtranslator/plugins/api/__init__.py
--rw-r--r--   0 root         (0) root         (0)     1470 2018-11-29 17:53:32.000000 aws-sam-translator-1.9.0/samtranslator/plugins/api/default_definition_body_plugin.py
--rw-r--r--   0 root         (0) root         (0)    11197 2018-11-29 17:53:32.000000 aws-sam-translator-1.9.0/samtranslator/plugins/api/implicit_api_plugin.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2018-11-29 17:57:54.000000 aws-sam-translator-1.9.0/samtranslator/plugins/application/
--rw-r--r--   0 root         (0) root         (0)        0 2018-11-29 17:53:32.000000 aws-sam-translator-1.9.0/samtranslator/plugins/application/__init__.py
--rw-r--r--   0 root         (0) root         (0)    14619 2018-11-29 17:53:32.000000 aws-sam-translator-1.9.0/samtranslator/plugins/application/serverless_app_plugin.py
--rw-r--r--   0 root         (0) root         (0)      498 2018-11-29 17:53:32.000000 aws-sam-translator-1.9.0/samtranslator/plugins/exceptions.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2018-11-29 17:57:54.000000 aws-sam-translator-1.9.0/samtranslator/plugins/globals/
--rw-r--r--   0 root         (0) root         (0)        0 2018-11-29 17:53:32.000000 aws-sam-translator-1.9.0/samtranslator/plugins/globals/__init__.py
--rw-r--r--   0 root         (0) root         (0)    13167 2018-11-29 17:53:32.000000 aws-sam-translator-1.9.0/samtranslator/plugins/globals/globals.py
--rw-r--r--   0 root         (0) root         (0)     1482 2018-11-29 17:53:32.000000 aws-sam-translator-1.9.0/samtranslator/plugins/globals/globals_plugin.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2018-11-29 17:57:54.000000 aws-sam-translator-1.9.0/samtranslator/plugins/policies/
--rw-r--r--   0 root         (0) root         (0)        0 2018-11-29 17:53:32.000000 aws-sam-translator-1.9.0/samtranslator/plugins/policies/__init__.py
--rw-r--r--   0 root         (0) root         (0)     3737 2018-11-29 17:53:32.000000 aws-sam-translator-1.9.0/samtranslator/plugins/policies/policy_templates_plugin.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2018-11-29 17:57:54.000000 aws-sam-translator-1.9.0/samtranslator/policy_template_processor/
--rw-r--r--   0 root         (0) root         (0)        0 2018-11-29 17:53:32.000000 aws-sam-translator-1.9.0/samtranslator/policy_template_processor/__init__.py
--rw-r--r--   0 root         (0) root         (0)      758 2018-11-29 17:53:32.000000 aws-sam-translator-1.9.0/samtranslator/policy_template_processor/exceptions.py
--rw-r--r--   0 root         (0) root         (0)     5692 2018-11-29 17:53:32.000000 aws-sam-translator-1.9.0/samtranslator/policy_template_processor/processor.py
--rw-r--r--   0 root         (0) root         (0)     5617 2018-11-29 17:53:32.000000 aws-sam-translator-1.9.0/samtranslator/policy_template_processor/template.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2018-11-29 17:57:54.000000 aws-sam-translator-1.9.0/samtranslator/policy_templates_data/
--rw-r--r--   0 root         (0) root         (0)      233 2018-11-29 17:53:32.000000 aws-sam-translator-1.9.0/samtranslator/policy_templates_data/__init__.py
--rw-r--r--   0 root         (0) root         (0)    37170 2018-11-29 17:53:32.000000 aws-sam-translator-1.9.0/samtranslator/policy_templates_data/policy_templates.json
--rw-r--r--   0 root         (0) root         (0)     1896 2018-11-29 17:53:32.000000 aws-sam-translator-1.9.0/samtranslator/policy_templates_data/schema.json
-drwxr-xr-x   0 root         (0) root         (0)        0 2018-11-29 17:57:54.000000 aws-sam-translator-1.9.0/samtranslator/public/
--rw-r--r--   0 root         (0) root         (0)      175 2018-11-29 17:53:32.000000 aws-sam-translator-1.9.0/samtranslator/public/__init__.py
--rw-r--r--   0 root         (0) root         (0)      133 2018-11-29 17:53:32.000000 aws-sam-translator-1.9.0/samtranslator/public/exceptions.py
--rw-r--r--   0 root         (0) root         (0)       82 2018-11-29 17:53:32.000000 aws-sam-translator-1.9.0/samtranslator/public/helpers.py
--rw-r--r--   0 root         (0) root         (0)      156 2018-11-29 17:53:32.000000 aws-sam-translator-1.9.0/samtranslator/public/intrinsics.py
--rw-r--r--   0 root         (0) root         (0)       96 2018-11-29 17:53:32.000000 aws-sam-translator-1.9.0/samtranslator/public/models.py
--rw-r--r--   0 root         (0) root         (0)       63 2018-11-29 17:53:32.000000 aws-sam-translator-1.9.0/samtranslator/public/parser.py
--rw-r--r--   0 root         (0) root         (0)       61 2018-11-29 17:53:32.000000 aws-sam-translator-1.9.0/samtranslator/public/plugins.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2018-11-29 17:57:54.000000 aws-sam-translator-1.9.0/samtranslator/public/sdk/
--rw-r--r--   0 root         (0) root         (0)        0 2018-11-29 17:53:32.000000 aws-sam-translator-1.9.0/samtranslator/public/sdk/__init__.py
--rw-r--r--   0 root         (0) root         (0)       83 2018-11-29 17:53:32.000000 aws-sam-translator-1.9.0/samtranslator/public/sdk/resource.py
--rw-r--r--   0 root         (0) root         (0)       66 2018-11-29 17:53:32.000000 aws-sam-translator-1.9.0/samtranslator/public/sdk/template.py
--rw-r--r--   0 root         (0) root         (0)       72 2018-11-29 17:53:32.000000 aws-sam-translator-1.9.0/samtranslator/public/swagger.py
--rw-r--r--   0 root         (0) root         (0)      318 2018-11-29 17:53:32.000000 aws-sam-translator-1.9.0/samtranslator/public/translator.py
--rw-r--r--   0 root         (0) root         (0)      861 2018-11-29 17:53:32.000000 aws-sam-translator-1.9.0/samtranslator/region_configuration.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2018-11-29 17:57:54.000000 aws-sam-translator-1.9.0/samtranslator/sdk/
--rw-r--r--   0 root         (0) root         (0)        0 2018-11-29 17:53:32.000000 aws-sam-translator-1.9.0/samtranslator/sdk/__init__.py
--rw-r--r--   0 root         (0) root         (0)     2068 2018-11-29 17:53:32.000000 aws-sam-translator-1.9.0/samtranslator/sdk/resource.py
--rw-r--r--   0 root         (0) root         (0)     2482 2018-11-29 17:53:32.000000 aws-sam-translator-1.9.0/samtranslator/sdk/template.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2018-11-29 17:57:54.000000 aws-sam-translator-1.9.0/samtranslator/swagger/
--rw-r--r--   0 root         (0) root         (0)        0 2018-11-29 17:53:32.000000 aws-sam-translator-1.9.0/samtranslator/swagger/__init__.py
--rw-r--r--   0 root         (0) root         (0)    19736 2018-11-29 17:53:32.000000 aws-sam-translator-1.9.0/samtranslator/swagger/swagger.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2018-11-29 17:57:55.000000 aws-sam-translator-1.9.0/samtranslator/translator/
--rw-r--r--   0 root         (0) root         (0)        0 2018-11-29 17:53:32.000000 aws-sam-translator-1.9.0/samtranslator/translator/__init__.py
--rw-r--r--   0 root         (0) root         (0)     1938 2018-11-29 17:53:32.000000 aws-sam-translator-1.9.0/samtranslator/translator/arn_generator.py
--rw-r--r--   0 root         (0) root         (0)     3301 2018-11-29 17:53:32.000000 aws-sam-translator-1.9.0/samtranslator/translator/logical_id_generator.py
--rw-r--r--   0 root         (0) root         (0)      879 2018-11-29 17:53:32.000000 aws-sam-translator-1.9.0/samtranslator/translator/managed_policy_translator.py
--rw-r--r--   0 root         (0) root         (0)      672 2018-11-29 17:53:32.000000 aws-sam-translator-1.9.0/samtranslator/translator/transform.py
--rw-r--r--   0 root         (0) root         (0)    11488 2018-11-29 17:53:32.000000 aws-sam-translator-1.9.0/samtranslator/translator/translator.py
--rw-r--r--   0 root         (0) root         (0)      951 2018-11-29 17:53:32.000000 aws-sam-translator-1.9.0/samtranslator/translator/verify_logical_id.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2018-11-29 17:57:55.000000 aws-sam-translator-1.9.0/samtranslator/validator/
--rw-r--r--   0 root         (0) root         (0)        0 2018-11-29 17:53:32.000000 aws-sam-translator-1.9.0/samtranslator/validator/__init__.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2018-11-29 17:57:55.000000 aws-sam-translator-1.9.0/samtranslator/validator/sam_schema/
--rw-r--r--   0 root         (0) root         (0)      134 2018-11-29 17:53:32.000000 aws-sam-translator-1.9.0/samtranslator/validator/sam_schema/__init__.py
--rw-r--r--   0 root         (0) root         (0)    22809 2018-11-29 17:53:32.000000 aws-sam-translator-1.9.0/samtranslator/validator/sam_schema/schema.json
--rw-r--r--   0 root         (0) root         (0)     1722 2018-11-29 17:53:32.000000 aws-sam-translator-1.9.0/samtranslator/validator/validator.py
--rw-r--r--   0 root         (0) root         (0)     1577 2018-11-29 17:53:32.000000 aws-sam-translator-1.9.0/samtranslator/yaml_helper.py
--rw-r--r--   0 root         (0) root         (0)       79 2018-11-29 17:57:55.000000 aws-sam-translator-1.9.0/setup.cfg
--rwxr-xr-x   0 root         (0) root         (0)     2791 2018-11-29 17:53:32.000000 aws-sam-translator-1.9.0/setup.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2019-02-07 23:21:23.000000 aws-sam-translator-1.9.1/
+drwxr-xr-x   0 root         (0) root         (0)        0 2019-02-07 23:21:22.000000 aws-sam-translator-1.9.1/aws_sam_translator.egg-info/
+-rw-r--r--   0 root         (0) root         (0)        1 2019-02-07 23:21:21.000000 aws-sam-translator-1.9.1/aws_sam_translator.egg-info/dependency_links.txt
+-rw-r--r--   0 root         (0) root         (0)     3278 2019-02-07 23:21:21.000000 aws-sam-translator-1.9.1/aws_sam_translator.egg-info/PKG-INFO
+-rw-r--r--   0 root         (0) root         (0)      270 2019-02-07 23:21:21.000000 aws-sam-translator-1.9.1/aws_sam_translator.egg-info/requires.txt
+-rw-r--r--   0 root         (0) root         (0)     3761 2019-02-07 23:21:22.000000 aws-sam-translator-1.9.1/aws_sam_translator.egg-info/SOURCES.txt
+-rw-r--r--   0 root         (0) root         (0)       20 2019-02-07 23:21:21.000000 aws-sam-translator-1.9.1/aws_sam_translator.egg-info/top_level.txt
+-rw-r--r--   0 root         (0) root         (0)    11357 2019-02-07 23:18:47.000000 aws-sam-translator-1.9.1/LICENSE
+-rwxr-xr-x   0 root         (0) root         (0)      283 2019-02-07 23:18:47.000000 aws-sam-translator-1.9.1/MANIFEST.in
+-rw-r--r--   0 root         (0) root         (0)     3278 2019-02-07 23:21:23.000000 aws-sam-translator-1.9.1/PKG-INFO
+-rw-r--r--   0 root         (0) root         (0)     2094 2019-02-07 23:18:47.000000 aws-sam-translator-1.9.1/README.md
+drwxr-xr-x   0 root         (0) root         (0)        0 2019-02-07 23:21:22.000000 aws-sam-translator-1.9.1/requirements/
+-rwxr-xr-x   0 root         (0) root         (0)       72 2019-02-07 23:18:47.000000 aws-sam-translator-1.9.1/requirements/base.txt
+-rw-r--r--   0 root         (0) root         (0)      228 2019-02-07 23:18:47.000000 aws-sam-translator-1.9.1/requirements/dev.txt
+drwxr-xr-x   0 root         (0) root         (0)        0 2019-02-07 23:21:22.000000 aws-sam-translator-1.9.1/samtranslator/
+-rw-r--r--   0 root         (0) root         (0)       22 2019-02-07 23:18:47.000000 aws-sam-translator-1.9.1/samtranslator/__init__.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2019-02-07 23:21:22.000000 aws-sam-translator-1.9.1/samtranslator/intrinsics/
+-rw-r--r--   0 root         (0) root         (0)        0 2019-02-07 23:18:47.000000 aws-sam-translator-1.9.1/samtranslator/intrinsics/__init__.py
+-rw-r--r--   0 root         (0) root         (0)    22078 2019-02-07 23:18:47.000000 aws-sam-translator-1.9.1/samtranslator/intrinsics/actions.py
+-rw-r--r--   0 root         (0) root         (0)    11718 2019-02-07 23:18:47.000000 aws-sam-translator-1.9.1/samtranslator/intrinsics/resolver.py
+-rw-r--r--   0 root         (0) root         (0)     2940 2019-02-07 23:18:47.000000 aws-sam-translator-1.9.1/samtranslator/intrinsics/resource_refs.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2019-02-07 23:21:22.000000 aws-sam-translator-1.9.1/samtranslator/model/
+-rw-r--r--   0 root         (0) root         (0)    21265 2019-02-07 23:18:47.000000 aws-sam-translator-1.9.1/samtranslator/model/__init__.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2019-02-07 23:21:22.000000 aws-sam-translator-1.9.1/samtranslator/model/api/
+-rw-r--r--   0 root         (0) root         (0)        0 2019-02-07 23:18:47.000000 aws-sam-translator-1.9.1/samtranslator/model/api/__init__.py
+-rw-r--r--   0 root         (0) root         (0)    14610 2019-02-07 23:18:47.000000 aws-sam-translator-1.9.1/samtranslator/model/api/api_generator.py
+-rw-r--r--   0 root         (0) root         (0)    10617 2019-02-07 23:18:47.000000 aws-sam-translator-1.9.1/samtranslator/model/apigateway.py
+-rw-r--r--   0 root         (0) root         (0)      758 2019-02-07 23:18:47.000000 aws-sam-translator-1.9.1/samtranslator/model/cloudformation.py
+-rw-r--r--   0 root         (0) root         (0)     1102 2019-02-07 23:18:47.000000 aws-sam-translator-1.9.1/samtranslator/model/codedeploy.py
+-rw-r--r--   0 root         (0) root         (0)     1223 2019-02-07 23:18:47.000000 aws-sam-translator-1.9.1/samtranslator/model/dynamodb.py
+-rw-r--r--   0 root         (0) root         (0)      829 2019-02-07 23:18:47.000000 aws-sam-translator-1.9.1/samtranslator/model/events.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2019-02-07 23:21:22.000000 aws-sam-translator-1.9.1/samtranslator/model/eventsources/
+-rw-r--r--   0 root         (0) root         (0)        0 2019-02-07 23:18:47.000000 aws-sam-translator-1.9.1/samtranslator/model/eventsources/__init__.py
+-rw-r--r--   0 root         (0) root         (0)     2152 2019-02-07 23:18:47.000000 aws-sam-translator-1.9.1/samtranslator/model/eventsources/cloudwatchlogs.py
+-rw-r--r--   0 root         (0) root         (0)     4088 2019-02-07 23:18:47.000000 aws-sam-translator-1.9.1/samtranslator/model/eventsources/pull.py
+-rw-r--r--   0 root         (0) root         (0)    23274 2019-02-07 23:18:47.000000 aws-sam-translator-1.9.1/samtranslator/model/eventsources/push.py
+-rw-r--r--   0 root         (0) root         (0)     3243 2019-02-07 23:18:47.000000 aws-sam-translator-1.9.1/samtranslator/model/exceptions.py
+-rw-r--r--   0 root         (0) root         (0)     5827 2019-02-07 23:18:47.000000 aws-sam-translator-1.9.1/samtranslator/model/function_policies.py
+-rw-r--r--   0 root         (0) root         (0)     1941 2019-02-07 23:18:47.000000 aws-sam-translator-1.9.1/samtranslator/model/iam.py
+-rw-r--r--   0 root         (0) root         (0)     1834 2019-02-07 23:18:47.000000 aws-sam-translator-1.9.1/samtranslator/model/intrinsics.py
+-rw-r--r--   0 root         (0) root         (0)      468 2019-02-07 23:18:47.000000 aws-sam-translator-1.9.1/samtranslator/model/iot.py
+-rw-r--r--   0 root         (0) root         (0)     3913 2019-02-07 23:18:47.000000 aws-sam-translator-1.9.1/samtranslator/model/lambda_.py
+-rw-r--r--   0 root         (0) root         (0)      581 2019-02-07 23:18:47.000000 aws-sam-translator-1.9.1/samtranslator/model/log.py
+-rw-r--r--   0 root         (0) root         (0)      427 2019-02-07 23:18:47.000000 aws-sam-translator-1.9.1/samtranslator/model/naming.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2019-02-07 23:21:22.000000 aws-sam-translator-1.9.1/samtranslator/model/preferences/
+-rw-r--r--   0 root         (0) root         (0)        0 2019-02-07 23:18:47.000000 aws-sam-translator-1.9.1/samtranslator/model/preferences/__init__.py
+-rw-r--r--   0 root         (0) root         (0)     3449 2019-02-07 23:18:47.000000 aws-sam-translator-1.9.1/samtranslator/model/preferences/deployment_preference.py
+-rw-r--r--   0 root         (0) root         (0)     6687 2019-02-07 23:18:47.000000 aws-sam-translator-1.9.1/samtranslator/model/preferences/deployment_preference_collection.py
+-rw-r--r--   0 root         (0) root         (0)     1434 2019-02-07 23:18:47.000000 aws-sam-translator-1.9.1/samtranslator/model/s3.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2019-02-07 23:21:22.000000 aws-sam-translator-1.9.1/samtranslator/model/s3_utils/
+-rw-r--r--   0 root         (0) root         (0)        0 2019-02-07 23:18:47.000000 aws-sam-translator-1.9.1/samtranslator/model/s3_utils/__init__.py
+-rw-r--r--   0 root         (0) root         (0)     3142 2019-02-07 23:18:47.000000 aws-sam-translator-1.9.1/samtranslator/model/s3_utils/uri_parser.py
+-rw-r--r--   0 root         (0) root         (0)    33153 2019-02-07 23:18:47.000000 aws-sam-translator-1.9.1/samtranslator/model/sam_resources.py
+-rw-r--r--   0 root         (0) root         (0)      358 2019-02-07 23:18:47.000000 aws-sam-translator-1.9.1/samtranslator/model/sns.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2019-02-07 23:21:22.000000 aws-sam-translator-1.9.1/samtranslator/model/tags/
+-rw-r--r--   0 root         (0) root         (0)        0 2019-02-07 23:18:47.000000 aws-sam-translator-1.9.1/samtranslator/model/tags/__init__.py
+-rw-r--r--   0 root         (0) root         (0)      797 2019-02-07 23:18:47.000000 aws-sam-translator-1.9.1/samtranslator/model/tags/resource_tagging.py
+-rw-r--r--   0 root         (0) root         (0)     4593 2019-02-07 23:18:47.000000 aws-sam-translator-1.9.1/samtranslator/model/types.py
+-rw-r--r--   0 root         (0) root         (0)     1642 2019-02-07 23:18:47.000000 aws-sam-translator-1.9.1/samtranslator/model/update_policy.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2019-02-07 23:21:22.000000 aws-sam-translator-1.9.1/samtranslator/parser/
+-rw-r--r--   0 root         (0) root         (0)        0 2019-02-07 23:18:47.000000 aws-sam-translator-1.9.1/samtranslator/parser/__init__.py
+-rw-r--r--   0 root         (0) root         (0)     1723 2019-02-07 23:18:47.000000 aws-sam-translator-1.9.1/samtranslator/parser/parser.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2019-02-07 23:21:22.000000 aws-sam-translator-1.9.1/samtranslator/plugins/
+-rw-r--r--   0 root         (0) root         (0)     9216 2019-02-07 23:18:47.000000 aws-sam-translator-1.9.1/samtranslator/plugins/__init__.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2019-02-07 23:21:22.000000 aws-sam-translator-1.9.1/samtranslator/plugins/api/
+-rw-r--r--   0 root         (0) root         (0)        0 2019-02-07 23:18:47.000000 aws-sam-translator-1.9.1/samtranslator/plugins/api/__init__.py
+-rw-r--r--   0 root         (0) root         (0)     1470 2019-02-07 23:18:47.000000 aws-sam-translator-1.9.1/samtranslator/plugins/api/default_definition_body_plugin.py
+-rw-r--r--   0 root         (0) root         (0)    11197 2019-02-07 23:18:47.000000 aws-sam-translator-1.9.1/samtranslator/plugins/api/implicit_api_plugin.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2019-02-07 23:21:22.000000 aws-sam-translator-1.9.1/samtranslator/plugins/application/
+-rw-r--r--   0 root         (0) root         (0)        0 2019-02-07 23:18:47.000000 aws-sam-translator-1.9.1/samtranslator/plugins/application/__init__.py
+-rw-r--r--   0 root         (0) root         (0)    14720 2019-02-07 23:18:47.000000 aws-sam-translator-1.9.1/samtranslator/plugins/application/serverless_app_plugin.py
+-rw-r--r--   0 root         (0) root         (0)      498 2019-02-07 23:18:47.000000 aws-sam-translator-1.9.1/samtranslator/plugins/exceptions.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2019-02-07 23:21:23.000000 aws-sam-translator-1.9.1/samtranslator/plugins/globals/
+-rw-r--r--   0 root         (0) root         (0)        0 2019-02-07 23:18:47.000000 aws-sam-translator-1.9.1/samtranslator/plugins/globals/__init__.py
+-rw-r--r--   0 root         (0) root         (0)    13167 2019-02-07 23:18:47.000000 aws-sam-translator-1.9.1/samtranslator/plugins/globals/globals.py
+-rw-r--r--   0 root         (0) root         (0)     1482 2019-02-07 23:18:47.000000 aws-sam-translator-1.9.1/samtranslator/plugins/globals/globals_plugin.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2019-02-07 23:21:23.000000 aws-sam-translator-1.9.1/samtranslator/plugins/policies/
+-rw-r--r--   0 root         (0) root         (0)        0 2019-02-07 23:18:47.000000 aws-sam-translator-1.9.1/samtranslator/plugins/policies/__init__.py
+-rw-r--r--   0 root         (0) root         (0)     3737 2019-02-07 23:18:47.000000 aws-sam-translator-1.9.1/samtranslator/plugins/policies/policy_templates_plugin.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2019-02-07 23:21:23.000000 aws-sam-translator-1.9.1/samtranslator/policy_template_processor/
+-rw-r--r--   0 root         (0) root         (0)        0 2019-02-07 23:18:47.000000 aws-sam-translator-1.9.1/samtranslator/policy_template_processor/__init__.py
+-rw-r--r--   0 root         (0) root         (0)      758 2019-02-07 23:18:47.000000 aws-sam-translator-1.9.1/samtranslator/policy_template_processor/exceptions.py
+-rw-r--r--   0 root         (0) root         (0)     5692 2019-02-07 23:18:47.000000 aws-sam-translator-1.9.1/samtranslator/policy_template_processor/processor.py
+-rw-r--r--   0 root         (0) root         (0)     5617 2019-02-07 23:18:47.000000 aws-sam-translator-1.9.1/samtranslator/policy_template_processor/template.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2019-02-07 23:21:23.000000 aws-sam-translator-1.9.1/samtranslator/policy_templates_data/
+-rw-r--r--   0 root         (0) root         (0)      233 2019-02-07 23:18:47.000000 aws-sam-translator-1.9.1/samtranslator/policy_templates_data/__init__.py
+-rw-r--r--   0 root         (0) root         (0)    37170 2019-02-07 23:18:47.000000 aws-sam-translator-1.9.1/samtranslator/policy_templates_data/policy_templates.json
+-rw-r--r--   0 root         (0) root         (0)     1896 2019-02-07 23:18:47.000000 aws-sam-translator-1.9.1/samtranslator/policy_templates_data/schema.json
+drwxr-xr-x   0 root         (0) root         (0)        0 2019-02-07 23:21:23.000000 aws-sam-translator-1.9.1/samtranslator/public/
+-rw-r--r--   0 root         (0) root         (0)      175 2019-02-07 23:18:47.000000 aws-sam-translator-1.9.1/samtranslator/public/__init__.py
+-rw-r--r--   0 root         (0) root         (0)      133 2019-02-07 23:18:47.000000 aws-sam-translator-1.9.1/samtranslator/public/exceptions.py
+-rw-r--r--   0 root         (0) root         (0)       82 2019-02-07 23:18:47.000000 aws-sam-translator-1.9.1/samtranslator/public/helpers.py
+-rw-r--r--   0 root         (0) root         (0)      156 2019-02-07 23:18:47.000000 aws-sam-translator-1.9.1/samtranslator/public/intrinsics.py
+-rw-r--r--   0 root         (0) root         (0)       96 2019-02-07 23:18:47.000000 aws-sam-translator-1.9.1/samtranslator/public/models.py
+-rw-r--r--   0 root         (0) root         (0)       63 2019-02-07 23:18:47.000000 aws-sam-translator-1.9.1/samtranslator/public/parser.py
+-rw-r--r--   0 root         (0) root         (0)       61 2019-02-07 23:18:47.000000 aws-sam-translator-1.9.1/samtranslator/public/plugins.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2019-02-07 23:21:23.000000 aws-sam-translator-1.9.1/samtranslator/public/sdk/
+-rw-r--r--   0 root         (0) root         (0)        0 2019-02-07 23:18:47.000000 aws-sam-translator-1.9.1/samtranslator/public/sdk/__init__.py
+-rw-r--r--   0 root         (0) root         (0)       83 2019-02-07 23:18:47.000000 aws-sam-translator-1.9.1/samtranslator/public/sdk/resource.py
+-rw-r--r--   0 root         (0) root         (0)       66 2019-02-07 23:18:47.000000 aws-sam-translator-1.9.1/samtranslator/public/sdk/template.py
+-rw-r--r--   0 root         (0) root         (0)       72 2019-02-07 23:18:47.000000 aws-sam-translator-1.9.1/samtranslator/public/swagger.py
+-rw-r--r--   0 root         (0) root         (0)      318 2019-02-07 23:18:47.000000 aws-sam-translator-1.9.1/samtranslator/public/translator.py
+-rw-r--r--   0 root         (0) root         (0)      861 2019-02-07 23:18:47.000000 aws-sam-translator-1.9.1/samtranslator/region_configuration.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2019-02-07 23:21:23.000000 aws-sam-translator-1.9.1/samtranslator/sdk/
+-rw-r--r--   0 root         (0) root         (0)        0 2019-02-07 23:18:47.000000 aws-sam-translator-1.9.1/samtranslator/sdk/__init__.py
+-rw-r--r--   0 root         (0) root         (0)     2068 2019-02-07 23:18:47.000000 aws-sam-translator-1.9.1/samtranslator/sdk/resource.py
+-rw-r--r--   0 root         (0) root         (0)     2482 2019-02-07 23:18:47.000000 aws-sam-translator-1.9.1/samtranslator/sdk/template.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2019-02-07 23:21:23.000000 aws-sam-translator-1.9.1/samtranslator/swagger/
+-rw-r--r--   0 root         (0) root         (0)        0 2019-02-07 23:18:47.000000 aws-sam-translator-1.9.1/samtranslator/swagger/__init__.py
+-rw-r--r--   0 root         (0) root         (0)    19736 2019-02-07 23:18:47.000000 aws-sam-translator-1.9.1/samtranslator/swagger/swagger.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2019-02-07 23:21:23.000000 aws-sam-translator-1.9.1/samtranslator/translator/
+-rw-r--r--   0 root         (0) root         (0)        0 2019-02-07 23:18:47.000000 aws-sam-translator-1.9.1/samtranslator/translator/__init__.py
+-rw-r--r--   0 root         (0) root         (0)     1938 2019-02-07 23:18:47.000000 aws-sam-translator-1.9.1/samtranslator/translator/arn_generator.py
+-rw-r--r--   0 root         (0) root         (0)     3301 2019-02-07 23:18:47.000000 aws-sam-translator-1.9.1/samtranslator/translator/logical_id_generator.py
+-rw-r--r--   0 root         (0) root         (0)      879 2019-02-07 23:18:47.000000 aws-sam-translator-1.9.1/samtranslator/translator/managed_policy_translator.py
+-rw-r--r--   0 root         (0) root         (0)      672 2019-02-07 23:18:47.000000 aws-sam-translator-1.9.1/samtranslator/translator/transform.py
+-rw-r--r--   0 root         (0) root         (0)    11488 2019-02-07 23:18:47.000000 aws-sam-translator-1.9.1/samtranslator/translator/translator.py
+-rw-r--r--   0 root         (0) root         (0)      951 2019-02-07 23:18:47.000000 aws-sam-translator-1.9.1/samtranslator/translator/verify_logical_id.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2019-02-07 23:21:23.000000 aws-sam-translator-1.9.1/samtranslator/validator/
+-rw-r--r--   0 root         (0) root         (0)        0 2019-02-07 23:18:47.000000 aws-sam-translator-1.9.1/samtranslator/validator/__init__.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2019-02-07 23:21:23.000000 aws-sam-translator-1.9.1/samtranslator/validator/sam_schema/
+-rw-r--r--   0 root         (0) root         (0)      134 2019-02-07 23:18:47.000000 aws-sam-translator-1.9.1/samtranslator/validator/sam_schema/__init__.py
+-rw-r--r--   0 root         (0) root         (0)    22809 2019-02-07 23:18:47.000000 aws-sam-translator-1.9.1/samtranslator/validator/sam_schema/schema.json
+-rw-r--r--   0 root         (0) root         (0)     1722 2019-02-07 23:18:47.000000 aws-sam-translator-1.9.1/samtranslator/validator/validator.py
+-rw-r--r--   0 root         (0) root         (0)     1577 2019-02-07 23:18:47.000000 aws-sam-translator-1.9.1/samtranslator/yaml_helper.py
+-rw-r--r--   0 root         (0) root         (0)       79 2019-02-07 23:21:23.000000 aws-sam-translator-1.9.1/setup.cfg
+-rwxr-xr-x   0 root         (0) root         (0)     2791 2019-02-07 23:18:47.000000 aws-sam-translator-1.9.1/setup.py
```

### Comparing `aws-sam-translator-1.9.0/aws_sam_translator.egg-info/PKG-INFO` & `aws-sam-translator-1.9.1/aws_sam_translator.egg-info/PKG-INFO`

 * *Files 6% similar despite different names*

```diff
@@ -1,17 +1,18 @@
 Metadata-Version: 2.1
 Name: aws-sam-translator
-Version: 1.9.0
+Version: 1.9.1
 Summary: AWS SAM Translator is a library that transform SAM templates into AWS CloudFormation templates
 Home-page: https://github.com/awslabs/serverless-application-model
 Author: Amazon Web Services
 Author-email: aws-sam-developers@amazon.com
 License: Apache License 2.0
 Description: [![Build Status](https://travis-ci.org/awslabs/serverless-application-model.svg?branch=develop)](https://travis-ci.org/awslabs/serverless-application-model)
         [![PyPI version](https://badge.fury.io/py/aws-sam-translator.svg)](https://badge.fury.io/py/aws-sam-translator)
+        [![Codecov Test Coverage](https://codecov.io/gh/awslabs/serverless-application-model/branch/master/graphs/badge.svg?style=flat)](https://codecov.io/gh/awslabs/serverless-application-model)
         
         ![Logo](aws_sam_introduction.png)
         
         # AWS Serverless Application Model (AWS SAM)
         You can use SAM to define serverless applications in simple and clean syntax.
         
         This GitHub project is the starting point for AWS SAM. It contains the SAM specification, the code that translates SAM templates into AWS CloudFormation stacks, general information about the model, and examples of common applications.
@@ -21,15 +22,15 @@
         Documentation about using AWS SAM to define, test, and deploy serverless applications is available at [AWS Serverless Application Model Developer Guide](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/what-is-sam.html).
         
         ## Contributing new features and enhancements to SAM
         You can build serverless applications faster and further simplify your development of serverless applications by defining new event sources, new resource types, and new parameters within SAM. Additionally, you can modify SAM to integrate it with other frameworks and deployment providers from the community for building serverless applications.
         
         [Read the Development Guide](DEVELOPMENT_GUIDE.rst) for in-depth information on how to start making changes.
         
-        [Join the SAM developers channel (#samdev) on Slack](https://awssamopensource.splashthat.com/) to collaborate with fellow community members and the AWS SAM team.
+        [Join the SAM developers channel (#samdev) on Slack](https://join.slack.com/t/awsdevelopers/shared_invite/enQtMzg3NTc5OTM2MzcxLTdjYTdhYWE3OTQyYTU4Njk1ZWY4Y2ZjYjBhMTUxNGYzNDg5MWQ1ZTc5MTRlOGY0OTI4NTdlZTMwNmI5YTgwOGM/) to collaborate with fellow community members and the AWS SAM team.
         
 Keywords: AWS SAM Serverless Application Model
 Platform: UNKNOWN
 Classifier: Development Status :: 4 - Beta
 Classifier: Environment :: Console
 Classifier: Environment :: Other Environment
 Classifier: Intended Audience :: Developers
```

### Comparing `aws-sam-translator-1.9.0/aws_sam_translator.egg-info/SOURCES.txt` & `aws-sam-translator-1.9.1/aws_sam_translator.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `aws-sam-translator-1.9.0/LICENSE` & `aws-sam-translator-1.9.1/LICENSE`

 * *Files identical despite different names*

### Comparing `aws-sam-translator-1.9.0/PKG-INFO` & `aws-sam-translator-1.9.1/PKG-INFO`

 * *Files 6% similar despite different names*

```diff
@@ -1,17 +1,18 @@
 Metadata-Version: 2.1
 Name: aws-sam-translator
-Version: 1.9.0
+Version: 1.9.1
 Summary: AWS SAM Translator is a library that transform SAM templates into AWS CloudFormation templates
 Home-page: https://github.com/awslabs/serverless-application-model
 Author: Amazon Web Services
 Author-email: aws-sam-developers@amazon.com
 License: Apache License 2.0
 Description: [![Build Status](https://travis-ci.org/awslabs/serverless-application-model.svg?branch=develop)](https://travis-ci.org/awslabs/serverless-application-model)
         [![PyPI version](https://badge.fury.io/py/aws-sam-translator.svg)](https://badge.fury.io/py/aws-sam-translator)
+        [![Codecov Test Coverage](https://codecov.io/gh/awslabs/serverless-application-model/branch/master/graphs/badge.svg?style=flat)](https://codecov.io/gh/awslabs/serverless-application-model)
         
         ![Logo](aws_sam_introduction.png)
         
         # AWS Serverless Application Model (AWS SAM)
         You can use SAM to define serverless applications in simple and clean syntax.
         
         This GitHub project is the starting point for AWS SAM. It contains the SAM specification, the code that translates SAM templates into AWS CloudFormation stacks, general information about the model, and examples of common applications.
@@ -21,15 +22,15 @@
         Documentation about using AWS SAM to define, test, and deploy serverless applications is available at [AWS Serverless Application Model Developer Guide](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/what-is-sam.html).
         
         ## Contributing new features and enhancements to SAM
         You can build serverless applications faster and further simplify your development of serverless applications by defining new event sources, new resource types, and new parameters within SAM. Additionally, you can modify SAM to integrate it with other frameworks and deployment providers from the community for building serverless applications.
         
         [Read the Development Guide](DEVELOPMENT_GUIDE.rst) for in-depth information on how to start making changes.
         
-        [Join the SAM developers channel (#samdev) on Slack](https://awssamopensource.splashthat.com/) to collaborate with fellow community members and the AWS SAM team.
+        [Join the SAM developers channel (#samdev) on Slack](https://join.slack.com/t/awsdevelopers/shared_invite/enQtMzg3NTc5OTM2MzcxLTdjYTdhYWE3OTQyYTU4Njk1ZWY4Y2ZjYjBhMTUxNGYzNDg5MWQ1ZTc5MTRlOGY0OTI4NTdlZTMwNmI5YTgwOGM/) to collaborate with fellow community members and the AWS SAM team.
         
 Keywords: AWS SAM Serverless Application Model
 Platform: UNKNOWN
 Classifier: Development Status :: 4 - Beta
 Classifier: Environment :: Console
 Classifier: Environment :: Other Environment
 Classifier: Intended Audience :: Developers
```

### Comparing `aws-sam-translator-1.9.0/README.md` & `aws-sam-translator-1.9.1/README.md`

 * *Files 10% similar despite different names*

```diff
@@ -1,9 +1,10 @@
 [![Build Status](https://travis-ci.org/awslabs/serverless-application-model.svg?branch=develop)](https://travis-ci.org/awslabs/serverless-application-model)
 [![PyPI version](https://badge.fury.io/py/aws-sam-translator.svg)](https://badge.fury.io/py/aws-sam-translator)
+[![Codecov Test Coverage](https://codecov.io/gh/awslabs/serverless-application-model/branch/master/graphs/badge.svg?style=flat)](https://codecov.io/gh/awslabs/serverless-application-model)
 
 ![Logo](aws_sam_introduction.png)
 
 # AWS Serverless Application Model (AWS SAM)
 You can use SAM to define serverless applications in simple and clean syntax.
 
 This GitHub project is the starting point for AWS SAM. It contains the SAM specification, the code that translates SAM templates into AWS CloudFormation stacks, general information about the model, and examples of common applications.
@@ -13,8 +14,8 @@
 Documentation about using AWS SAM to define, test, and deploy serverless applications is available at [AWS Serverless Application Model Developer Guide](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/what-is-sam.html).
 
 ## Contributing new features and enhancements to SAM
 You can build serverless applications faster and further simplify your development of serverless applications by defining new event sources, new resource types, and new parameters within SAM. Additionally, you can modify SAM to integrate it with other frameworks and deployment providers from the community for building serverless applications.
 
 [Read the Development Guide](DEVELOPMENT_GUIDE.rst) for in-depth information on how to start making changes.
 
-[Join the SAM developers channel (#samdev) on Slack](https://awssamopensource.splashthat.com/) to collaborate with fellow community members and the AWS SAM team.
+[Join the SAM developers channel (#samdev) on Slack](https://join.slack.com/t/awsdevelopers/shared_invite/enQtMzg3NTc5OTM2MzcxLTdjYTdhYWE3OTQyYTU4Njk1ZWY4Y2ZjYjBhMTUxNGYzNDg5MWQ1ZTc5MTRlOGY0OTI4NTdlZTMwNmI5YTgwOGM/) to collaborate with fellow community members and the AWS SAM team.
```

### Comparing `aws-sam-translator-1.9.0/samtranslator/intrinsics/actions.py` & `aws-sam-translator-1.9.1/samtranslator/intrinsics/actions.py`

 * *Files identical despite different names*

### Comparing `aws-sam-translator-1.9.0/samtranslator/intrinsics/resolver.py` & `aws-sam-translator-1.9.1/samtranslator/intrinsics/resolver.py`

 * *Files identical despite different names*

### Comparing `aws-sam-translator-1.9.0/samtranslator/intrinsics/resource_refs.py` & `aws-sam-translator-1.9.1/samtranslator/intrinsics/resource_refs.py`

 * *Files identical despite different names*

### Comparing `aws-sam-translator-1.9.0/samtranslator/model/__init__.py` & `aws-sam-translator-1.9.1/samtranslator/model/__init__.py`

 * *Files identical despite different names*

### Comparing `aws-sam-translator-1.9.0/samtranslator/model/api/api_generator.py` & `aws-sam-translator-1.9.1/samtranslator/model/api/api_generator.py`

 * *Files identical despite different names*

### Comparing `aws-sam-translator-1.9.0/samtranslator/model/apigateway.py` & `aws-sam-translator-1.9.1/samtranslator/model/apigateway.py`

 * *Files identical despite different names*

### Comparing `aws-sam-translator-1.9.0/samtranslator/model/cloudformation.py` & `aws-sam-translator-1.9.1/samtranslator/model/cloudformation.py`

 * *Files identical despite different names*

### Comparing `aws-sam-translator-1.9.0/samtranslator/model/codedeploy.py` & `aws-sam-translator-1.9.1/samtranslator/model/codedeploy.py`

 * *Files identical despite different names*

### Comparing `aws-sam-translator-1.9.0/samtranslator/model/dynamodb.py` & `aws-sam-translator-1.9.1/samtranslator/model/dynamodb.py`

 * *Files identical despite different names*

### Comparing `aws-sam-translator-1.9.0/samtranslator/model/events.py` & `aws-sam-translator-1.9.1/samtranslator/model/events.py`

 * *Files identical despite different names*

### Comparing `aws-sam-translator-1.9.0/samtranslator/model/eventsources/cloudwatchlogs.py` & `aws-sam-translator-1.9.1/samtranslator/model/eventsources/cloudwatchlogs.py`

 * *Files identical despite different names*

### Comparing `aws-sam-translator-1.9.0/samtranslator/model/eventsources/pull.py` & `aws-sam-translator-1.9.1/samtranslator/model/eventsources/pull.py`

 * *Files identical despite different names*

### Comparing `aws-sam-translator-1.9.0/samtranslator/model/eventsources/push.py` & `aws-sam-translator-1.9.1/samtranslator/model/eventsources/push.py`

 * *Files identical despite different names*

### Comparing `aws-sam-translator-1.9.0/samtranslator/model/exceptions.py` & `aws-sam-translator-1.9.1/samtranslator/model/exceptions.py`

 * *Files identical despite different names*

### Comparing `aws-sam-translator-1.9.0/samtranslator/model/function_policies.py` & `aws-sam-translator-1.9.1/samtranslator/model/function_policies.py`

 * *Files identical despite different names*

### Comparing `aws-sam-translator-1.9.0/samtranslator/model/iam.py` & `aws-sam-translator-1.9.1/samtranslator/model/iam.py`

 * *Files identical despite different names*

### Comparing `aws-sam-translator-1.9.0/samtranslator/model/intrinsics.py` & `aws-sam-translator-1.9.1/samtranslator/model/intrinsics.py`

 * *Files identical despite different names*

### Comparing `aws-sam-translator-1.9.0/samtranslator/model/lambda_.py` & `aws-sam-translator-1.9.1/samtranslator/model/lambda_.py`

 * *Files identical despite different names*

### Comparing `aws-sam-translator-1.9.0/samtranslator/model/log.py` & `aws-sam-translator-1.9.1/samtranslator/model/log.py`

 * *Files identical despite different names*

### Comparing `aws-sam-translator-1.9.0/samtranslator/model/preferences/deployment_preference.py` & `aws-sam-translator-1.9.1/samtranslator/model/preferences/deployment_preference.py`

 * *Files identical despite different names*

### Comparing `aws-sam-translator-1.9.0/samtranslator/model/preferences/deployment_preference_collection.py` & `aws-sam-translator-1.9.1/samtranslator/model/preferences/deployment_preference_collection.py`

 * *Files identical despite different names*

### Comparing `aws-sam-translator-1.9.0/samtranslator/model/s3.py` & `aws-sam-translator-1.9.1/samtranslator/model/s3.py`

 * *Files identical despite different names*

### Comparing `aws-sam-translator-1.9.0/samtranslator/model/s3_utils/uri_parser.py` & `aws-sam-translator-1.9.1/samtranslator/model/s3_utils/uri_parser.py`

 * *Files identical despite different names*

### Comparing `aws-sam-translator-1.9.0/samtranslator/model/sam_resources.py` & `aws-sam-translator-1.9.1/samtranslator/model/sam_resources.py`

 * *Files identical despite different names*

### Comparing `aws-sam-translator-1.9.0/samtranslator/model/tags/resource_tagging.py` & `aws-sam-translator-1.9.1/samtranslator/model/tags/resource_tagging.py`

 * *Files identical despite different names*

### Comparing `aws-sam-translator-1.9.0/samtranslator/model/types.py` & `aws-sam-translator-1.9.1/samtranslator/model/types.py`

 * *Files identical despite different names*

### Comparing `aws-sam-translator-1.9.0/samtranslator/model/update_policy.py` & `aws-sam-translator-1.9.1/samtranslator/model/update_policy.py`

 * *Files identical despite different names*

### Comparing `aws-sam-translator-1.9.0/samtranslator/parser/parser.py` & `aws-sam-translator-1.9.1/samtranslator/parser/parser.py`

 * *Files identical despite different names*

### Comparing `aws-sam-translator-1.9.0/samtranslator/plugins/__init__.py` & `aws-sam-translator-1.9.1/samtranslator/plugins/__init__.py`

 * *Files identical despite different names*

### Comparing `aws-sam-translator-1.9.0/samtranslator/plugins/api/default_definition_body_plugin.py` & `aws-sam-translator-1.9.1/samtranslator/plugins/api/default_definition_body_plugin.py`

 * *Files identical despite different names*

### Comparing `aws-sam-translator-1.9.0/samtranslator/plugins/api/implicit_api_plugin.py` & `aws-sam-translator-1.9.1/samtranslator/plugins/api/implicit_api_plugin.py`

 * *Files identical despite different names*

### Comparing `aws-sam-translator-1.9.0/samtranslator/plugins/application/serverless_app_plugin.py` & `aws-sam-translator-1.9.1/samtranslator/plugins/application/serverless_app_plugin.py`

 * *Files 1% similar despite different names*

```diff
@@ -44,18 +44,15 @@
         :param boto3.client sar_client: The boto3 client to use to access the Serverless Application Repository
         :param bool wait_for_template_active_status: Flag to turn on the option to wait for all templates to become active
         :param bool validate_only: Flag to only validate application access (uses get_application API instead)
         """
         super(ServerlessAppPlugin, self).__init__(ServerlessAppPlugin.__name__)
         self._applications = {}
         self._in_progress_templates = []
-        if sar_client:
-            self._sar_client = sar_client
-        else:
-            self._sar_client = boto3.client('serverlessrepo')
+        self._sar_client = sar_client
         self._wait_for_template_active_status = wait_for_template_active_status
         self._validate_only = validate_only
 
         # make sure the flag combination makes sense
         if self._validate_only == True and self._wait_for_template_active_status == True:
             message = "Cannot set both validate_only and wait_for_template_active_status flags to True."
             raise InvalidPluginException(ServerlessAppPlugin.__name__, message)
@@ -85,14 +82,17 @@
                 continue
 
             app_id = app.properties[self.LOCATION_KEY].get(self.APPLICATION_ID_KEY)
             semver = app.properties[self.LOCATION_KEY].get(self.SEMANTIC_VERSION_KEY)
             key = (app_id, semver)
             if key not in self._applications:
                 try:
+                    # Lazy initialization of the client- create it when it is needed
+                    if not self._sar_client:
+                        self._sar_client = boto3.client('serverlessrepo')
                     service_call(app_id, semver, key, logical_id)
                 except InvalidResourceException as e:
                     # Catch all InvalidResourceExceptions, raise those in the before_resource_transform target.
                     self._applications[key] = e
 
 
     def _can_process_application(self, app):
```

### Comparing `aws-sam-translator-1.9.0/samtranslator/plugins/globals/globals.py` & `aws-sam-translator-1.9.1/samtranslator/plugins/globals/globals.py`

 * *Files identical despite different names*

### Comparing `aws-sam-translator-1.9.0/samtranslator/plugins/globals/globals_plugin.py` & `aws-sam-translator-1.9.1/samtranslator/plugins/globals/globals_plugin.py`

 * *Files identical despite different names*

### Comparing `aws-sam-translator-1.9.0/samtranslator/plugins/policies/policy_templates_plugin.py` & `aws-sam-translator-1.9.1/samtranslator/plugins/policies/policy_templates_plugin.py`

 * *Files identical despite different names*

### Comparing `aws-sam-translator-1.9.0/samtranslator/policy_template_processor/exceptions.py` & `aws-sam-translator-1.9.1/samtranslator/policy_template_processor/exceptions.py`

 * *Files identical despite different names*

### Comparing `aws-sam-translator-1.9.0/samtranslator/policy_template_processor/processor.py` & `aws-sam-translator-1.9.1/samtranslator/policy_template_processor/processor.py`

 * *Files identical despite different names*

### Comparing `aws-sam-translator-1.9.0/samtranslator/policy_template_processor/template.py` & `aws-sam-translator-1.9.1/samtranslator/policy_template_processor/template.py`

 * *Files identical despite different names*

### Comparing `aws-sam-translator-1.9.0/samtranslator/policy_templates_data/policy_templates.json` & `aws-sam-translator-1.9.1/samtranslator/policy_templates_data/policy_templates.json`

 * *Files identical despite different names*

### Comparing `aws-sam-translator-1.9.0/samtranslator/policy_templates_data/schema.json` & `aws-sam-translator-1.9.1/samtranslator/policy_templates_data/schema.json`

 * *Files identical despite different names*

### Comparing `aws-sam-translator-1.9.0/samtranslator/region_configuration.py` & `aws-sam-translator-1.9.1/samtranslator/region_configuration.py`

 * *Files identical despite different names*

### Comparing `aws-sam-translator-1.9.0/samtranslator/sdk/resource.py` & `aws-sam-translator-1.9.1/samtranslator/sdk/resource.py`

 * *Files identical despite different names*

### Comparing `aws-sam-translator-1.9.0/samtranslator/sdk/template.py` & `aws-sam-translator-1.9.1/samtranslator/sdk/template.py`

 * *Files identical despite different names*

### Comparing `aws-sam-translator-1.9.0/samtranslator/swagger/swagger.py` & `aws-sam-translator-1.9.1/samtranslator/swagger/swagger.py`

 * *Files identical despite different names*

### Comparing `aws-sam-translator-1.9.0/samtranslator/translator/arn_generator.py` & `aws-sam-translator-1.9.1/samtranslator/translator/arn_generator.py`

 * *Files identical despite different names*

### Comparing `aws-sam-translator-1.9.0/samtranslator/translator/logical_id_generator.py` & `aws-sam-translator-1.9.1/samtranslator/translator/logical_id_generator.py`

 * *Files identical despite different names*

### Comparing `aws-sam-translator-1.9.0/samtranslator/translator/managed_policy_translator.py` & `aws-sam-translator-1.9.1/samtranslator/translator/managed_policy_translator.py`

 * *Files identical despite different names*

### Comparing `aws-sam-translator-1.9.0/samtranslator/translator/transform.py` & `aws-sam-translator-1.9.1/samtranslator/translator/transform.py`

 * *Files identical despite different names*

### Comparing `aws-sam-translator-1.9.0/samtranslator/translator/translator.py` & `aws-sam-translator-1.9.1/samtranslator/translator/translator.py`

 * *Files identical despite different names*

### Comparing `aws-sam-translator-1.9.0/samtranslator/translator/verify_logical_id.py` & `aws-sam-translator-1.9.1/samtranslator/translator/verify_logical_id.py`

 * *Files identical despite different names*

### Comparing `aws-sam-translator-1.9.0/samtranslator/validator/sam_schema/schema.json` & `aws-sam-translator-1.9.1/samtranslator/validator/sam_schema/schema.json`

 * *Files identical despite different names*

### Comparing `aws-sam-translator-1.9.0/samtranslator/validator/validator.py` & `aws-sam-translator-1.9.1/samtranslator/validator/validator.py`

 * *Files identical despite different names*

### Comparing `aws-sam-translator-1.9.0/samtranslator/yaml_helper.py` & `aws-sam-translator-1.9.1/samtranslator/yaml_helper.py`

 * *Files identical despite different names*

### Comparing `aws-sam-translator-1.9.0/setup.py` & `aws-sam-translator-1.9.1/setup.py`

 * *Files identical despite different names*

