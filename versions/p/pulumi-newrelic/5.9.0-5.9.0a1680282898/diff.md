# Comparing `tmp/pulumi_newrelic-5.9.0.tar.gz` & `tmp/pulumi_newrelic-5.9.0a1680282898.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "pulumi_newrelic-5.9.0.tar", last modified: Fri Mar 31 17:47:26 2023, max compression
+gzip compressed data, was "pulumi_newrelic-5.9.0a1680282898.tar", last modified: Fri Mar 31 17:21:01 2023, max compression
```

## Comparing `pulumi_newrelic-5.9.0.tar` & `pulumi_newrelic-5.9.0a1680282898.tar`

### file list

```diff
@@ -1,96 +1,96 @@
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-31 17:47:26.879414 pulumi_newrelic-5.9.0/
--rw-r--r--   0 runner    (1001) docker     (123)     3776 2023-03-31 17:47:26.879414 pulumi_newrelic-5.9.0/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)     3440 2023-03-31 17:47:26.000000 pulumi_newrelic-5.9.0/README.md
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-31 17:47:26.875414 pulumi_newrelic-5.9.0/pulumi_newrelic/
--rw-r--r--   0 runner    (1001) docker     (123)    10709 2023-03-31 17:47:26.000000 pulumi_newrelic-5.9.0/pulumi_newrelic/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)   448850 2023-03-31 17:47:26.000000 pulumi_newrelic-5.9.0/pulumi_newrelic/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (123)     8081 2023-03-31 17:47:26.000000 pulumi_newrelic-5.9.0/pulumi_newrelic/_utilities.py
--rw-r--r--   0 runner    (1001) docker     (123)     8673 2023-03-31 17:47:26.000000 pulumi_newrelic-5.9.0/pulumi_newrelic/account_management.py
--rw-r--r--   0 runner    (1001) docker     (123)    19378 2023-03-31 17:47:26.000000 pulumi_newrelic-5.9.0/pulumi_newrelic/alert_channel.py
--rw-r--r--   0 runner    (1001) docker     (123)    42951 2023-03-31 17:47:26.000000 pulumi_newrelic-5.9.0/pulumi_newrelic/alert_condition.py
--rw-r--r--   0 runner    (1001) docker     (123)    19077 2023-03-31 17:47:26.000000 pulumi_newrelic-5.9.0/pulumi_newrelic/alert_muting_rule.py
--rw-r--r--   0 runner    (1001) docker     (123)    21313 2023-03-31 17:47:26.000000 pulumi_newrelic-5.9.0/pulumi_newrelic/alert_policy.py
--rw-r--r--   0 runner    (1001) docker     (123)    14505 2023-03-31 17:47:26.000000 pulumi_newrelic-5.9.0/pulumi_newrelic/alert_policy_channel.py
--rw-r--r--   0 runner    (1001) docker     (123)    20485 2023-03-31 17:47:26.000000 pulumi_newrelic-5.9.0/pulumi_newrelic/api_access_key.py
--rw-r--r--   0 runner    (1001) docker     (123)    19290 2023-03-31 17:47:26.000000 pulumi_newrelic-5.9.0/pulumi_newrelic/browser_application.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-31 17:47:26.875414 pulumi_newrelic-5.9.0/pulumi_newrelic/cloud/
--rw-r--r--   0 runner    (1001) docker     (123)      592 2023-03-31 17:47:26.000000 pulumi_newrelic-5.9.0/pulumi_newrelic/cloud/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)   168479 2023-03-31 17:47:26.000000 pulumi_newrelic-5.9.0/pulumi_newrelic/cloud/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (123)    60440 2023-03-31 17:47:26.000000 pulumi_newrelic-5.9.0/pulumi_newrelic/cloud/aws_govcloud_integrations.py
--rw-r--r--   0 runner    (1001) docker     (123)    18999 2023-03-31 17:47:26.000000 pulumi_newrelic-5.9.0/pulumi_newrelic/cloud/aws_govcloud_link_account.py
--rw-r--r--   0 runner    (1001) docker     (123)    27596 2023-03-31 17:47:26.000000 pulumi_newrelic-5.9.0/pulumi_newrelic/cloud/aws_integrations.py
--rw-r--r--   0 runner    (1001) docker     (123)    13021 2023-03-31 17:47:26.000000 pulumi_newrelic-5.9.0/pulumi_newrelic/cloud/aws_link_account.py
--rw-r--r--   0 runner    (1001) docker     (123)    90078 2023-03-31 17:47:26.000000 pulumi_newrelic-5.9.0/pulumi_newrelic/cloud/azure_integrations.py
--rw-r--r--   0 runner    (1001) docker     (123)    16032 2023-03-31 17:47:26.000000 pulumi_newrelic-5.9.0/pulumi_newrelic/cloud/azure_link_account.py
--rw-r--r--   0 runner    (1001) docker     (123)    74614 2023-03-31 17:47:26.000000 pulumi_newrelic-5.9.0/pulumi_newrelic/cloud/gcp_integrations.py
--rw-r--r--   0 runner    (1001) docker     (123)     9754 2023-03-31 17:47:26.000000 pulumi_newrelic-5.9.0/pulumi_newrelic/cloud/gcp_link_account.py
--rw-r--r--   0 runner    (1001) docker     (123)   188009 2023-03-31 17:47:26.000000 pulumi_newrelic-5.9.0/pulumi_newrelic/cloud/outputs.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-31 17:47:26.875414 pulumi_newrelic-5.9.0/pulumi_newrelic/config/
--rw-r--r--   0 runner    (1001) docker     (123)      285 2023-03-31 17:47:26.000000 pulumi_newrelic-5.9.0/pulumi_newrelic/config/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     2110 2023-03-31 17:47:26.000000 pulumi_newrelic-5.9.0/pulumi_newrelic/config/vars.py
--rw-r--r--   0 runner    (1001) docker     (123)    20415 2023-03-31 17:47:26.000000 pulumi_newrelic-5.9.0/pulumi_newrelic/data_partition_rule.py
--rw-r--r--   0 runner    (1001) docker     (123)     8477 2023-03-31 17:47:26.000000 pulumi_newrelic-5.9.0/pulumi_newrelic/entity_tags.py
--rw-r--r--   0 runner    (1001) docker     (123)    15870 2023-03-31 17:47:26.000000 pulumi_newrelic-5.9.0/pulumi_newrelic/events_to_metrics_rule.py
--rw-r--r--   0 runner    (1001) docker     (123)     4449 2023-03-31 17:47:26.000000 pulumi_newrelic-5.9.0/pulumi_newrelic/get_account.py
--rw-r--r--   0 runner    (1001) docker     (123)     5326 2023-03-31 17:47:26.000000 pulumi_newrelic-5.9.0/pulumi_newrelic/get_alert_channel.py
--rw-r--r--   0 runner    (1001) docker     (123)     5873 2023-03-31 17:47:26.000000 pulumi_newrelic-5.9.0/pulumi_newrelic/get_alert_policy.py
--rw-r--r--   0 runner    (1001) docker     (123)     5252 2023-03-31 17:47:26.000000 pulumi_newrelic-5.9.0/pulumi_newrelic/get_application.py
--rw-r--r--   0 runner    (1001) docker     (123)     5127 2023-03-31 17:47:26.000000 pulumi_newrelic-5.9.0/pulumi_newrelic/get_cloud_account.py
--rw-r--r--   0 runner    (1001) docker     (123)     9819 2023-03-31 17:47:26.000000 pulumi_newrelic-5.9.0/pulumi_newrelic/get_entity.py
--rw-r--r--   0 runner    (1001) docker     (123)     4051 2023-03-31 17:47:26.000000 pulumi_newrelic-5.9.0/pulumi_newrelic/get_key_transaction.py
--rw-r--r--   0 runner    (1001) docker     (123)     6801 2023-03-31 17:47:26.000000 pulumi_newrelic-5.9.0/pulumi_newrelic/get_notification_destination.py
--rw-r--r--   0 runner    (1001) docker     (123)     4822 2023-03-31 17:47:26.000000 pulumi_newrelic-5.9.0/pulumi_newrelic/get_obfuscation_expression.py
--rw-r--r--   0 runner    (1001) docker     (123)    16223 2023-03-31 17:47:26.000000 pulumi_newrelic-5.9.0/pulumi_newrelic/get_service_level_alert_helper.py
--rw-r--r--   0 runner    (1001) docker     (123)     5429 2023-03-31 17:47:26.000000 pulumi_newrelic-5.9.0/pulumi_newrelic/get_test_grok_pattern.py
--rw-r--r--   0 runner    (1001) docker     (123)    56153 2023-03-31 17:47:26.000000 pulumi_newrelic-5.9.0/pulumi_newrelic/infra_alert_condition.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-31 17:47:26.875414 pulumi_newrelic-5.9.0/pulumi_newrelic/insights/
--rw-r--r--   0 runner    (1001) docker     (123)      335 2023-03-31 17:47:26.000000 pulumi_newrelic-5.9.0/pulumi_newrelic/insights/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     2765 2023-03-31 17:47:26.000000 pulumi_newrelic-5.9.0/pulumi_newrelic/insights/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (123)    10052 2023-03-31 17:47:26.000000 pulumi_newrelic-5.9.0/pulumi_newrelic/insights/event.py
--rw-r--r--   0 runner    (1001) docker     (123)     1874 2023-03-31 17:47:26.000000 pulumi_newrelic-5.9.0/pulumi_newrelic/insights/outputs.py
--rw-r--r--   0 runner    (1001) docker     (123)    22252 2023-03-31 17:47:26.000000 pulumi_newrelic-5.9.0/pulumi_newrelic/log_parsing_rule.py
--rw-r--r--   0 runner    (1001) docker     (123)    21098 2023-03-31 17:47:26.000000 pulumi_newrelic-5.9.0/pulumi_newrelic/notification_channel.py
--rw-r--r--   0 runner    (1001) docker     (123)    25645 2023-03-31 17:47:26.000000 pulumi_newrelic-5.9.0/pulumi_newrelic/notification_destination.py
--rw-r--r--   0 runner    (1001) docker     (123)    95474 2023-03-31 17:47:26.000000 pulumi_newrelic-5.9.0/pulumi_newrelic/nrql_alert_condition.py
--rw-r--r--   0 runner    (1001) docker     (123)    15708 2023-03-31 17:47:26.000000 pulumi_newrelic-5.9.0/pulumi_newrelic/nrql_drop_rule.py
--rw-r--r--   0 runner    (1001) docker     (123)    12273 2023-03-31 17:47:26.000000 pulumi_newrelic-5.9.0/pulumi_newrelic/obfuscation_expression.py
--rw-r--r--   0 runner    (1001) docker     (123)    17665 2023-03-31 17:47:26.000000 pulumi_newrelic-5.9.0/pulumi_newrelic/obfuscation_rule.py
--rw-r--r--   0 runner    (1001) docker     (123)    21572 2023-03-31 17:47:26.000000 pulumi_newrelic-5.9.0/pulumi_newrelic/one_dashboard.py
--rw-r--r--   0 runner    (1001) docker     (123)    12165 2023-03-31 17:47:26.000000 pulumi_newrelic-5.9.0/pulumi_newrelic/one_dashboard_json.py
--rw-r--r--   0 runner    (1001) docker     (123)    23116 2023-03-31 17:47:26.000000 pulumi_newrelic-5.9.0/pulumi_newrelic/one_dashboard_raw.py
--rw-r--r--   0 runner    (1001) docker     (123)   442238 2023-03-31 17:47:26.000000 pulumi_newrelic-5.9.0/pulumi_newrelic/outputs.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-31 17:47:26.875414 pulumi_newrelic-5.9.0/pulumi_newrelic/plugins/
--rw-r--r--   0 runner    (1001) docker     (123)      374 2023-03-31 17:47:26.000000 pulumi_newrelic-5.9.0/pulumi_newrelic/plugins/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    17030 2023-03-31 17:47:26.000000 pulumi_newrelic-5.9.0/pulumi_newrelic/plugins/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (123)    14922 2023-03-31 17:47:26.000000 pulumi_newrelic-5.9.0/pulumi_newrelic/plugins/application_settings.py
--rw-r--r--   0 runner    (1001) docker     (123)    16843 2023-03-31 17:47:26.000000 pulumi_newrelic-5.9.0/pulumi_newrelic/plugins/outputs.py
--rw-r--r--   0 runner    (1001) docker     (123)    31618 2023-03-31 17:47:26.000000 pulumi_newrelic-5.9.0/pulumi_newrelic/plugins/workload.py
--rw-r--r--   0 runner    (1001) docker     (123)    18680 2023-03-31 17:47:26.000000 pulumi_newrelic-5.9.0/pulumi_newrelic/provider.py
--rw-r--r--   0 runner    (1001) docker     (123)       45 2023-03-31 17:47:26.000000 pulumi_newrelic-5.9.0/pulumi_newrelic/pulumi-plugin.json
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-31 17:47:26.000000 pulumi_newrelic-5.9.0/pulumi_newrelic/py.typed
--rw-r--r--   0 runner    (1001) docker     (123)    26181 2023-03-31 17:47:26.000000 pulumi_newrelic-5.9.0/pulumi_newrelic/service_level.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-31 17:47:26.879414 pulumi_newrelic-5.9.0/pulumi_newrelic/synthetics/
--rw-r--r--   0 runner    (1001) docker     (123)      680 2023-03-31 17:47:26.000000 pulumi_newrelic-5.9.0/pulumi_newrelic/synthetics/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    12981 2023-03-31 17:47:26.000000 pulumi_newrelic-5.9.0/pulumi_newrelic/synthetics/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (123)    19963 2023-03-31 17:47:26.000000 pulumi_newrelic-5.9.0/pulumi_newrelic/synthetics/alert_condition.py
--rw-r--r--   0 runner    (1001) docker     (123)    29006 2023-03-31 17:47:26.000000 pulumi_newrelic-5.9.0/pulumi_newrelic/synthetics/broken_links_monitor.py
--rw-r--r--   0 runner    (1001) docker     (123)    31102 2023-03-31 17:47:26.000000 pulumi_newrelic-5.9.0/pulumi_newrelic/synthetics/cert_check_monitor.py
--rw-r--r--   0 runner    (1001) docker     (123)     5114 2023-03-31 17:47:26.000000 pulumi_newrelic-5.9.0/pulumi_newrelic/synthetics/get_private_location.py
--rw-r--r--   0 runner    (1001) docker     (123)     5404 2023-03-31 17:47:26.000000 pulumi_newrelic-5.9.0/pulumi_newrelic/synthetics/get_secure_credential.py
--rw-r--r--   0 runner    (1001) docker     (123)    56034 2023-03-31 17:47:26.000000 pulumi_newrelic-5.9.0/pulumi_newrelic/synthetics/monitor.py
--rw-r--r--   0 runner    (1001) docker     (123)    30779 2023-03-31 17:47:26.000000 pulumi_newrelic-5.9.0/pulumi_newrelic/synthetics/multi_location_alert_condition.py
--rw-r--r--   0 runner    (1001) docker     (123)    10581 2023-03-31 17:47:26.000000 pulumi_newrelic-5.9.0/pulumi_newrelic/synthetics/outputs.py
--rw-r--r--   0 runner    (1001) docker     (123)    17171 2023-03-31 17:47:26.000000 pulumi_newrelic-5.9.0/pulumi_newrelic/synthetics/private_location.py
--rw-r--r--   0 runner    (1001) docker     (123)    45717 2023-03-31 17:47:26.000000 pulumi_newrelic-5.9.0/pulumi_newrelic/synthetics/script_monitor.py
--rw-r--r--   0 runner    (1001) docker     (123)    15602 2023-03-31 17:47:26.000000 pulumi_newrelic-5.9.0/pulumi_newrelic/synthetics/secure_credential.py
--rw-r--r--   0 runner    (1001) docker     (123)    32106 2023-03-31 17:47:26.000000 pulumi_newrelic-5.9.0/pulumi_newrelic/synthetics/step_monitor.py
--rw-r--r--   0 runner    (1001) docker     (123)    41091 2023-03-31 17:47:26.000000 pulumi_newrelic-5.9.0/pulumi_newrelic/workflow.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-31 17:47:26.875414 pulumi_newrelic-5.9.0/pulumi_newrelic.egg-info/
--rw-r--r--   0 runner    (1001) docker     (123)     3776 2023-03-31 17:47:26.000000 pulumi_newrelic-5.9.0/pulumi_newrelic.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)     3265 2023-03-31 17:47:26.000000 pulumi_newrelic-5.9.0/pulumi_newrelic.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-03-31 17:47:26.000000 pulumi_newrelic-5.9.0/pulumi_newrelic.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-03-31 17:47:26.000000 pulumi_newrelic-5.9.0/pulumi_newrelic.egg-info/not-zip-safe
--rw-r--r--   0 runner    (1001) docker     (123)       49 2023-03-31 17:47:26.000000 pulumi_newrelic-5.9.0/pulumi_newrelic.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (123)       16 2023-03-31 17:47:26.000000 pulumi_newrelic-5.9.0/pulumi_newrelic.egg-info/top_level.txt
--rw-r--r--   0 runner    (1001) docker     (123)       38 2023-03-31 17:47:26.879414 pulumi_newrelic-5.9.0/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (123)     2101 2023-03-31 17:47:26.000000 pulumi_newrelic-5.9.0/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-31 17:21:01.573843 pulumi_newrelic-5.9.0a1680282898/
+-rw-r--r--   0 runner    (1001) docker     (123)     3787 2023-03-31 17:21:01.573843 pulumi_newrelic-5.9.0a1680282898/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     3440 2023-03-31 17:21:01.000000 pulumi_newrelic-5.9.0a1680282898/README.md
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-31 17:21:01.565843 pulumi_newrelic-5.9.0a1680282898/pulumi_newrelic/
+-rw-r--r--   0 runner    (1001) docker     (123)    10709 2023-03-31 17:21:01.000000 pulumi_newrelic-5.9.0a1680282898/pulumi_newrelic/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)   448850 2023-03-31 17:21:01.000000 pulumi_newrelic-5.9.0a1680282898/pulumi_newrelic/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8081 2023-03-31 17:21:01.000000 pulumi_newrelic-5.9.0a1680282898/pulumi_newrelic/_utilities.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8673 2023-03-31 17:21:01.000000 pulumi_newrelic-5.9.0a1680282898/pulumi_newrelic/account_management.py
+-rw-r--r--   0 runner    (1001) docker     (123)    19378 2023-03-31 17:21:01.000000 pulumi_newrelic-5.9.0a1680282898/pulumi_newrelic/alert_channel.py
+-rw-r--r--   0 runner    (1001) docker     (123)    42951 2023-03-31 17:21:01.000000 pulumi_newrelic-5.9.0a1680282898/pulumi_newrelic/alert_condition.py
+-rw-r--r--   0 runner    (1001) docker     (123)    19077 2023-03-31 17:21:01.000000 pulumi_newrelic-5.9.0a1680282898/pulumi_newrelic/alert_muting_rule.py
+-rw-r--r--   0 runner    (1001) docker     (123)    21313 2023-03-31 17:21:01.000000 pulumi_newrelic-5.9.0a1680282898/pulumi_newrelic/alert_policy.py
+-rw-r--r--   0 runner    (1001) docker     (123)    14505 2023-03-31 17:21:01.000000 pulumi_newrelic-5.9.0a1680282898/pulumi_newrelic/alert_policy_channel.py
+-rw-r--r--   0 runner    (1001) docker     (123)    20485 2023-03-31 17:21:01.000000 pulumi_newrelic-5.9.0a1680282898/pulumi_newrelic/api_access_key.py
+-rw-r--r--   0 runner    (1001) docker     (123)    19290 2023-03-31 17:21:01.000000 pulumi_newrelic-5.9.0a1680282898/pulumi_newrelic/browser_application.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-31 17:21:01.569843 pulumi_newrelic-5.9.0a1680282898/pulumi_newrelic/cloud/
+-rw-r--r--   0 runner    (1001) docker     (123)      592 2023-03-31 17:21:01.000000 pulumi_newrelic-5.9.0a1680282898/pulumi_newrelic/cloud/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)   168479 2023-03-31 17:21:01.000000 pulumi_newrelic-5.9.0a1680282898/pulumi_newrelic/cloud/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (123)    60440 2023-03-31 17:21:01.000000 pulumi_newrelic-5.9.0a1680282898/pulumi_newrelic/cloud/aws_govcloud_integrations.py
+-rw-r--r--   0 runner    (1001) docker     (123)    18999 2023-03-31 17:21:01.000000 pulumi_newrelic-5.9.0a1680282898/pulumi_newrelic/cloud/aws_govcloud_link_account.py
+-rw-r--r--   0 runner    (1001) docker     (123)    27596 2023-03-31 17:21:01.000000 pulumi_newrelic-5.9.0a1680282898/pulumi_newrelic/cloud/aws_integrations.py
+-rw-r--r--   0 runner    (1001) docker     (123)    13021 2023-03-31 17:21:01.000000 pulumi_newrelic-5.9.0a1680282898/pulumi_newrelic/cloud/aws_link_account.py
+-rw-r--r--   0 runner    (1001) docker     (123)    90078 2023-03-31 17:21:01.000000 pulumi_newrelic-5.9.0a1680282898/pulumi_newrelic/cloud/azure_integrations.py
+-rw-r--r--   0 runner    (1001) docker     (123)    16032 2023-03-31 17:21:01.000000 pulumi_newrelic-5.9.0a1680282898/pulumi_newrelic/cloud/azure_link_account.py
+-rw-r--r--   0 runner    (1001) docker     (123)    74614 2023-03-31 17:21:01.000000 pulumi_newrelic-5.9.0a1680282898/pulumi_newrelic/cloud/gcp_integrations.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9754 2023-03-31 17:21:01.000000 pulumi_newrelic-5.9.0a1680282898/pulumi_newrelic/cloud/gcp_link_account.py
+-rw-r--r--   0 runner    (1001) docker     (123)   188009 2023-03-31 17:21:01.000000 pulumi_newrelic-5.9.0a1680282898/pulumi_newrelic/cloud/outputs.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-31 17:21:01.569843 pulumi_newrelic-5.9.0a1680282898/pulumi_newrelic/config/
+-rw-r--r--   0 runner    (1001) docker     (123)      285 2023-03-31 17:21:01.000000 pulumi_newrelic-5.9.0a1680282898/pulumi_newrelic/config/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2110 2023-03-31 17:21:01.000000 pulumi_newrelic-5.9.0a1680282898/pulumi_newrelic/config/vars.py
+-rw-r--r--   0 runner    (1001) docker     (123)    20415 2023-03-31 17:21:01.000000 pulumi_newrelic-5.9.0a1680282898/pulumi_newrelic/data_partition_rule.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8477 2023-03-31 17:21:01.000000 pulumi_newrelic-5.9.0a1680282898/pulumi_newrelic/entity_tags.py
+-rw-r--r--   0 runner    (1001) docker     (123)    15870 2023-03-31 17:21:01.000000 pulumi_newrelic-5.9.0a1680282898/pulumi_newrelic/events_to_metrics_rule.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4449 2023-03-31 17:21:01.000000 pulumi_newrelic-5.9.0a1680282898/pulumi_newrelic/get_account.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5326 2023-03-31 17:21:01.000000 pulumi_newrelic-5.9.0a1680282898/pulumi_newrelic/get_alert_channel.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5873 2023-03-31 17:21:01.000000 pulumi_newrelic-5.9.0a1680282898/pulumi_newrelic/get_alert_policy.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5252 2023-03-31 17:21:01.000000 pulumi_newrelic-5.9.0a1680282898/pulumi_newrelic/get_application.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5127 2023-03-31 17:21:01.000000 pulumi_newrelic-5.9.0a1680282898/pulumi_newrelic/get_cloud_account.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9819 2023-03-31 17:21:01.000000 pulumi_newrelic-5.9.0a1680282898/pulumi_newrelic/get_entity.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4051 2023-03-31 17:21:01.000000 pulumi_newrelic-5.9.0a1680282898/pulumi_newrelic/get_key_transaction.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6801 2023-03-31 17:21:01.000000 pulumi_newrelic-5.9.0a1680282898/pulumi_newrelic/get_notification_destination.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4822 2023-03-31 17:21:01.000000 pulumi_newrelic-5.9.0a1680282898/pulumi_newrelic/get_obfuscation_expression.py
+-rw-r--r--   0 runner    (1001) docker     (123)    16223 2023-03-31 17:21:01.000000 pulumi_newrelic-5.9.0a1680282898/pulumi_newrelic/get_service_level_alert_helper.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5429 2023-03-31 17:21:01.000000 pulumi_newrelic-5.9.0a1680282898/pulumi_newrelic/get_test_grok_pattern.py
+-rw-r--r--   0 runner    (1001) docker     (123)    56153 2023-03-31 17:21:01.000000 pulumi_newrelic-5.9.0a1680282898/pulumi_newrelic/infra_alert_condition.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-31 17:21:01.569843 pulumi_newrelic-5.9.0a1680282898/pulumi_newrelic/insights/
+-rw-r--r--   0 runner    (1001) docker     (123)      335 2023-03-31 17:21:01.000000 pulumi_newrelic-5.9.0a1680282898/pulumi_newrelic/insights/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2765 2023-03-31 17:21:01.000000 pulumi_newrelic-5.9.0a1680282898/pulumi_newrelic/insights/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (123)    10052 2023-03-31 17:21:01.000000 pulumi_newrelic-5.9.0a1680282898/pulumi_newrelic/insights/event.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1874 2023-03-31 17:21:01.000000 pulumi_newrelic-5.9.0a1680282898/pulumi_newrelic/insights/outputs.py
+-rw-r--r--   0 runner    (1001) docker     (123)    22252 2023-03-31 17:21:01.000000 pulumi_newrelic-5.9.0a1680282898/pulumi_newrelic/log_parsing_rule.py
+-rw-r--r--   0 runner    (1001) docker     (123)    21098 2023-03-31 17:21:01.000000 pulumi_newrelic-5.9.0a1680282898/pulumi_newrelic/notification_channel.py
+-rw-r--r--   0 runner    (1001) docker     (123)    25645 2023-03-31 17:21:01.000000 pulumi_newrelic-5.9.0a1680282898/pulumi_newrelic/notification_destination.py
+-rw-r--r--   0 runner    (1001) docker     (123)    95474 2023-03-31 17:21:01.000000 pulumi_newrelic-5.9.0a1680282898/pulumi_newrelic/nrql_alert_condition.py
+-rw-r--r--   0 runner    (1001) docker     (123)    15708 2023-03-31 17:21:01.000000 pulumi_newrelic-5.9.0a1680282898/pulumi_newrelic/nrql_drop_rule.py
+-rw-r--r--   0 runner    (1001) docker     (123)    12273 2023-03-31 17:21:01.000000 pulumi_newrelic-5.9.0a1680282898/pulumi_newrelic/obfuscation_expression.py
+-rw-r--r--   0 runner    (1001) docker     (123)    17665 2023-03-31 17:21:01.000000 pulumi_newrelic-5.9.0a1680282898/pulumi_newrelic/obfuscation_rule.py
+-rw-r--r--   0 runner    (1001) docker     (123)    21572 2023-03-31 17:21:01.000000 pulumi_newrelic-5.9.0a1680282898/pulumi_newrelic/one_dashboard.py
+-rw-r--r--   0 runner    (1001) docker     (123)    12165 2023-03-31 17:21:01.000000 pulumi_newrelic-5.9.0a1680282898/pulumi_newrelic/one_dashboard_json.py
+-rw-r--r--   0 runner    (1001) docker     (123)    23116 2023-03-31 17:21:01.000000 pulumi_newrelic-5.9.0a1680282898/pulumi_newrelic/one_dashboard_raw.py
+-rw-r--r--   0 runner    (1001) docker     (123)   442238 2023-03-31 17:21:01.000000 pulumi_newrelic-5.9.0a1680282898/pulumi_newrelic/outputs.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-31 17:21:01.569843 pulumi_newrelic-5.9.0a1680282898/pulumi_newrelic/plugins/
+-rw-r--r--   0 runner    (1001) docker     (123)      374 2023-03-31 17:21:01.000000 pulumi_newrelic-5.9.0a1680282898/pulumi_newrelic/plugins/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    17030 2023-03-31 17:21:01.000000 pulumi_newrelic-5.9.0a1680282898/pulumi_newrelic/plugins/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (123)    14922 2023-03-31 17:21:01.000000 pulumi_newrelic-5.9.0a1680282898/pulumi_newrelic/plugins/application_settings.py
+-rw-r--r--   0 runner    (1001) docker     (123)    16843 2023-03-31 17:21:01.000000 pulumi_newrelic-5.9.0a1680282898/pulumi_newrelic/plugins/outputs.py
+-rw-r--r--   0 runner    (1001) docker     (123)    31618 2023-03-31 17:21:01.000000 pulumi_newrelic-5.9.0a1680282898/pulumi_newrelic/plugins/workload.py
+-rw-r--r--   0 runner    (1001) docker     (123)    18680 2023-03-31 17:21:01.000000 pulumi_newrelic-5.9.0a1680282898/pulumi_newrelic/provider.py
+-rw-r--r--   0 runner    (1001) docker     (123)       45 2023-03-31 17:21:01.000000 pulumi_newrelic-5.9.0a1680282898/pulumi_newrelic/pulumi-plugin.json
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-31 17:21:01.000000 pulumi_newrelic-5.9.0a1680282898/pulumi_newrelic/py.typed
+-rw-r--r--   0 runner    (1001) docker     (123)    26181 2023-03-31 17:21:01.000000 pulumi_newrelic-5.9.0a1680282898/pulumi_newrelic/service_level.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-31 17:21:01.573843 pulumi_newrelic-5.9.0a1680282898/pulumi_newrelic/synthetics/
+-rw-r--r--   0 runner    (1001) docker     (123)      680 2023-03-31 17:21:01.000000 pulumi_newrelic-5.9.0a1680282898/pulumi_newrelic/synthetics/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    12981 2023-03-31 17:21:01.000000 pulumi_newrelic-5.9.0a1680282898/pulumi_newrelic/synthetics/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (123)    19963 2023-03-31 17:21:01.000000 pulumi_newrelic-5.9.0a1680282898/pulumi_newrelic/synthetics/alert_condition.py
+-rw-r--r--   0 runner    (1001) docker     (123)    29006 2023-03-31 17:21:01.000000 pulumi_newrelic-5.9.0a1680282898/pulumi_newrelic/synthetics/broken_links_monitor.py
+-rw-r--r--   0 runner    (1001) docker     (123)    31102 2023-03-31 17:21:01.000000 pulumi_newrelic-5.9.0a1680282898/pulumi_newrelic/synthetics/cert_check_monitor.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5114 2023-03-31 17:21:01.000000 pulumi_newrelic-5.9.0a1680282898/pulumi_newrelic/synthetics/get_private_location.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5404 2023-03-31 17:21:01.000000 pulumi_newrelic-5.9.0a1680282898/pulumi_newrelic/synthetics/get_secure_credential.py
+-rw-r--r--   0 runner    (1001) docker     (123)    56034 2023-03-31 17:21:01.000000 pulumi_newrelic-5.9.0a1680282898/pulumi_newrelic/synthetics/monitor.py
+-rw-r--r--   0 runner    (1001) docker     (123)    30779 2023-03-31 17:21:01.000000 pulumi_newrelic-5.9.0a1680282898/pulumi_newrelic/synthetics/multi_location_alert_condition.py
+-rw-r--r--   0 runner    (1001) docker     (123)    10581 2023-03-31 17:21:01.000000 pulumi_newrelic-5.9.0a1680282898/pulumi_newrelic/synthetics/outputs.py
+-rw-r--r--   0 runner    (1001) docker     (123)    17171 2023-03-31 17:21:01.000000 pulumi_newrelic-5.9.0a1680282898/pulumi_newrelic/synthetics/private_location.py
+-rw-r--r--   0 runner    (1001) docker     (123)    45717 2023-03-31 17:21:01.000000 pulumi_newrelic-5.9.0a1680282898/pulumi_newrelic/synthetics/script_monitor.py
+-rw-r--r--   0 runner    (1001) docker     (123)    15602 2023-03-31 17:21:01.000000 pulumi_newrelic-5.9.0a1680282898/pulumi_newrelic/synthetics/secure_credential.py
+-rw-r--r--   0 runner    (1001) docker     (123)    32106 2023-03-31 17:21:01.000000 pulumi_newrelic-5.9.0a1680282898/pulumi_newrelic/synthetics/step_monitor.py
+-rw-r--r--   0 runner    (1001) docker     (123)    41091 2023-03-31 17:21:01.000000 pulumi_newrelic-5.9.0a1680282898/pulumi_newrelic/workflow.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-31 17:21:01.565843 pulumi_newrelic-5.9.0a1680282898/pulumi_newrelic.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)     3787 2023-03-31 17:21:01.000000 pulumi_newrelic-5.9.0a1680282898/pulumi_newrelic.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     3265 2023-03-31 17:21:01.000000 pulumi_newrelic-5.9.0a1680282898/pulumi_newrelic.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-03-31 17:21:01.000000 pulumi_newrelic-5.9.0a1680282898/pulumi_newrelic.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-03-31 17:21:01.000000 pulumi_newrelic-5.9.0a1680282898/pulumi_newrelic.egg-info/not-zip-safe
+-rw-r--r--   0 runner    (1001) docker     (123)       49 2023-03-31 17:21:01.000000 pulumi_newrelic-5.9.0a1680282898/pulumi_newrelic.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       16 2023-03-31 17:21:01.000000 pulumi_newrelic-5.9.0a1680282898/pulumi_newrelic.egg-info/top_level.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       38 2023-03-31 17:21:01.573843 pulumi_newrelic-5.9.0a1680282898/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (123)     2138 2023-03-31 17:21:01.000000 pulumi_newrelic-5.9.0a1680282898/setup.py
```

### Comparing `pulumi_newrelic-5.9.0/PKG-INFO` & `pulumi_newrelic-5.9.0a1680282898/PKG-INFO`

 * *Files 2% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: pulumi_newrelic
-Version: 5.9.0
+Version: 5.9.0a1680282898
 Summary: A Pulumi package for creating and managing New Relic resources.
 Home-page: https://pulumi.io
 License: Apache-2.0
 Project-URL: Repository, https://github.com/pulumi/pulumi-newrelic
 Keywords: pulumi new relic
 Platform: UNKNOWN
 Description-Content-Type: text/markdown
```

### Comparing `pulumi_newrelic-5.9.0/README.md` & `pulumi_newrelic-5.9.0a1680282898/README.md`

 * *Files identical despite different names*

### Comparing `pulumi_newrelic-5.9.0/pulumi_newrelic/__init__.py` & `pulumi_newrelic-5.9.0a1680282898/pulumi_newrelic/__init__.py`

 * *Files identical despite different names*

### Comparing `pulumi_newrelic-5.9.0/pulumi_newrelic/_inputs.py` & `pulumi_newrelic-5.9.0a1680282898/pulumi_newrelic/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_newrelic-5.9.0/pulumi_newrelic/_utilities.py` & `pulumi_newrelic-5.9.0a1680282898/pulumi_newrelic/_utilities.py`

 * *Files identical despite different names*

### Comparing `pulumi_newrelic-5.9.0/pulumi_newrelic/account_management.py` & `pulumi_newrelic-5.9.0a1680282898/pulumi_newrelic/account_management.py`

 * *Files identical despite different names*

### Comparing `pulumi_newrelic-5.9.0/pulumi_newrelic/alert_channel.py` & `pulumi_newrelic-5.9.0a1680282898/pulumi_newrelic/alert_channel.py`

 * *Files identical despite different names*

### Comparing `pulumi_newrelic-5.9.0/pulumi_newrelic/alert_condition.py` & `pulumi_newrelic-5.9.0a1680282898/pulumi_newrelic/alert_condition.py`

 * *Files identical despite different names*

### Comparing `pulumi_newrelic-5.9.0/pulumi_newrelic/alert_muting_rule.py` & `pulumi_newrelic-5.9.0a1680282898/pulumi_newrelic/alert_muting_rule.py`

 * *Files identical despite different names*

### Comparing `pulumi_newrelic-5.9.0/pulumi_newrelic/alert_policy.py` & `pulumi_newrelic-5.9.0a1680282898/pulumi_newrelic/alert_policy.py`

 * *Files identical despite different names*

### Comparing `pulumi_newrelic-5.9.0/pulumi_newrelic/alert_policy_channel.py` & `pulumi_newrelic-5.9.0a1680282898/pulumi_newrelic/alert_policy_channel.py`

 * *Files identical despite different names*

### Comparing `pulumi_newrelic-5.9.0/pulumi_newrelic/api_access_key.py` & `pulumi_newrelic-5.9.0a1680282898/pulumi_newrelic/api_access_key.py`

 * *Files identical despite different names*

### Comparing `pulumi_newrelic-5.9.0/pulumi_newrelic/browser_application.py` & `pulumi_newrelic-5.9.0a1680282898/pulumi_newrelic/browser_application.py`

 * *Files identical despite different names*

### Comparing `pulumi_newrelic-5.9.0/pulumi_newrelic/cloud/__init__.py` & `pulumi_newrelic-5.9.0a1680282898/pulumi_newrelic/cloud/__init__.py`

 * *Files identical despite different names*

### Comparing `pulumi_newrelic-5.9.0/pulumi_newrelic/cloud/_inputs.py` & `pulumi_newrelic-5.9.0a1680282898/pulumi_newrelic/cloud/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_newrelic-5.9.0/pulumi_newrelic/cloud/aws_govcloud_integrations.py` & `pulumi_newrelic-5.9.0a1680282898/pulumi_newrelic/cloud/aws_govcloud_integrations.py`

 * *Files identical despite different names*

### Comparing `pulumi_newrelic-5.9.0/pulumi_newrelic/cloud/aws_govcloud_link_account.py` & `pulumi_newrelic-5.9.0a1680282898/pulumi_newrelic/cloud/aws_govcloud_link_account.py`

 * *Files identical despite different names*

### Comparing `pulumi_newrelic-5.9.0/pulumi_newrelic/cloud/aws_integrations.py` & `pulumi_newrelic-5.9.0a1680282898/pulumi_newrelic/cloud/aws_integrations.py`

 * *Files identical despite different names*

### Comparing `pulumi_newrelic-5.9.0/pulumi_newrelic/cloud/aws_link_account.py` & `pulumi_newrelic-5.9.0a1680282898/pulumi_newrelic/cloud/aws_link_account.py`

 * *Files identical despite different names*

### Comparing `pulumi_newrelic-5.9.0/pulumi_newrelic/cloud/azure_integrations.py` & `pulumi_newrelic-5.9.0a1680282898/pulumi_newrelic/cloud/azure_integrations.py`

 * *Files identical despite different names*

### Comparing `pulumi_newrelic-5.9.0/pulumi_newrelic/cloud/azure_link_account.py` & `pulumi_newrelic-5.9.0a1680282898/pulumi_newrelic/cloud/azure_link_account.py`

 * *Files identical despite different names*

### Comparing `pulumi_newrelic-5.9.0/pulumi_newrelic/cloud/gcp_integrations.py` & `pulumi_newrelic-5.9.0a1680282898/pulumi_newrelic/cloud/gcp_integrations.py`

 * *Files identical despite different names*

### Comparing `pulumi_newrelic-5.9.0/pulumi_newrelic/cloud/gcp_link_account.py` & `pulumi_newrelic-5.9.0a1680282898/pulumi_newrelic/cloud/gcp_link_account.py`

 * *Files identical despite different names*

### Comparing `pulumi_newrelic-5.9.0/pulumi_newrelic/cloud/outputs.py` & `pulumi_newrelic-5.9.0a1680282898/pulumi_newrelic/cloud/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_newrelic-5.9.0/pulumi_newrelic/config/vars.py` & `pulumi_newrelic-5.9.0a1680282898/pulumi_newrelic/config/vars.py`

 * *Files identical despite different names*

### Comparing `pulumi_newrelic-5.9.0/pulumi_newrelic/data_partition_rule.py` & `pulumi_newrelic-5.9.0a1680282898/pulumi_newrelic/data_partition_rule.py`

 * *Files identical despite different names*

### Comparing `pulumi_newrelic-5.9.0/pulumi_newrelic/entity_tags.py` & `pulumi_newrelic-5.9.0a1680282898/pulumi_newrelic/entity_tags.py`

 * *Files identical despite different names*

### Comparing `pulumi_newrelic-5.9.0/pulumi_newrelic/events_to_metrics_rule.py` & `pulumi_newrelic-5.9.0a1680282898/pulumi_newrelic/events_to_metrics_rule.py`

 * *Files identical despite different names*

### Comparing `pulumi_newrelic-5.9.0/pulumi_newrelic/get_account.py` & `pulumi_newrelic-5.9.0a1680282898/pulumi_newrelic/get_account.py`

 * *Files identical despite different names*

### Comparing `pulumi_newrelic-5.9.0/pulumi_newrelic/get_alert_channel.py` & `pulumi_newrelic-5.9.0a1680282898/pulumi_newrelic/get_alert_channel.py`

 * *Files identical despite different names*

### Comparing `pulumi_newrelic-5.9.0/pulumi_newrelic/get_alert_policy.py` & `pulumi_newrelic-5.9.0a1680282898/pulumi_newrelic/get_alert_policy.py`

 * *Files identical despite different names*

### Comparing `pulumi_newrelic-5.9.0/pulumi_newrelic/get_application.py` & `pulumi_newrelic-5.9.0a1680282898/pulumi_newrelic/get_application.py`

 * *Files identical despite different names*

### Comparing `pulumi_newrelic-5.9.0/pulumi_newrelic/get_cloud_account.py` & `pulumi_newrelic-5.9.0a1680282898/pulumi_newrelic/get_cloud_account.py`

 * *Files identical despite different names*

### Comparing `pulumi_newrelic-5.9.0/pulumi_newrelic/get_entity.py` & `pulumi_newrelic-5.9.0a1680282898/pulumi_newrelic/get_entity.py`

 * *Files identical despite different names*

### Comparing `pulumi_newrelic-5.9.0/pulumi_newrelic/get_key_transaction.py` & `pulumi_newrelic-5.9.0a1680282898/pulumi_newrelic/get_key_transaction.py`

 * *Files identical despite different names*

### Comparing `pulumi_newrelic-5.9.0/pulumi_newrelic/get_notification_destination.py` & `pulumi_newrelic-5.9.0a1680282898/pulumi_newrelic/get_notification_destination.py`

 * *Files identical despite different names*

### Comparing `pulumi_newrelic-5.9.0/pulumi_newrelic/get_obfuscation_expression.py` & `pulumi_newrelic-5.9.0a1680282898/pulumi_newrelic/get_obfuscation_expression.py`

 * *Files identical despite different names*

### Comparing `pulumi_newrelic-5.9.0/pulumi_newrelic/get_service_level_alert_helper.py` & `pulumi_newrelic-5.9.0a1680282898/pulumi_newrelic/get_service_level_alert_helper.py`

 * *Files identical despite different names*

### Comparing `pulumi_newrelic-5.9.0/pulumi_newrelic/get_test_grok_pattern.py` & `pulumi_newrelic-5.9.0a1680282898/pulumi_newrelic/get_test_grok_pattern.py`

 * *Files identical despite different names*

### Comparing `pulumi_newrelic-5.9.0/pulumi_newrelic/infra_alert_condition.py` & `pulumi_newrelic-5.9.0a1680282898/pulumi_newrelic/infra_alert_condition.py`

 * *Files identical despite different names*

### Comparing `pulumi_newrelic-5.9.0/pulumi_newrelic/insights/_inputs.py` & `pulumi_newrelic-5.9.0a1680282898/pulumi_newrelic/insights/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_newrelic-5.9.0/pulumi_newrelic/insights/event.py` & `pulumi_newrelic-5.9.0a1680282898/pulumi_newrelic/insights/event.py`

 * *Files identical despite different names*

### Comparing `pulumi_newrelic-5.9.0/pulumi_newrelic/insights/outputs.py` & `pulumi_newrelic-5.9.0a1680282898/pulumi_newrelic/insights/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_newrelic-5.9.0/pulumi_newrelic/log_parsing_rule.py` & `pulumi_newrelic-5.9.0a1680282898/pulumi_newrelic/log_parsing_rule.py`

 * *Files identical despite different names*

### Comparing `pulumi_newrelic-5.9.0/pulumi_newrelic/notification_channel.py` & `pulumi_newrelic-5.9.0a1680282898/pulumi_newrelic/notification_channel.py`

 * *Files identical despite different names*

### Comparing `pulumi_newrelic-5.9.0/pulumi_newrelic/notification_destination.py` & `pulumi_newrelic-5.9.0a1680282898/pulumi_newrelic/notification_destination.py`

 * *Files identical despite different names*

### Comparing `pulumi_newrelic-5.9.0/pulumi_newrelic/nrql_alert_condition.py` & `pulumi_newrelic-5.9.0a1680282898/pulumi_newrelic/nrql_alert_condition.py`

 * *Files identical despite different names*

### Comparing `pulumi_newrelic-5.9.0/pulumi_newrelic/nrql_drop_rule.py` & `pulumi_newrelic-5.9.0a1680282898/pulumi_newrelic/nrql_drop_rule.py`

 * *Files identical despite different names*

### Comparing `pulumi_newrelic-5.9.0/pulumi_newrelic/obfuscation_expression.py` & `pulumi_newrelic-5.9.0a1680282898/pulumi_newrelic/obfuscation_expression.py`

 * *Files identical despite different names*

### Comparing `pulumi_newrelic-5.9.0/pulumi_newrelic/obfuscation_rule.py` & `pulumi_newrelic-5.9.0a1680282898/pulumi_newrelic/obfuscation_rule.py`

 * *Files identical despite different names*

### Comparing `pulumi_newrelic-5.9.0/pulumi_newrelic/one_dashboard.py` & `pulumi_newrelic-5.9.0a1680282898/pulumi_newrelic/one_dashboard.py`

 * *Files identical despite different names*

### Comparing `pulumi_newrelic-5.9.0/pulumi_newrelic/one_dashboard_json.py` & `pulumi_newrelic-5.9.0a1680282898/pulumi_newrelic/one_dashboard_json.py`

 * *Files identical despite different names*

### Comparing `pulumi_newrelic-5.9.0/pulumi_newrelic/one_dashboard_raw.py` & `pulumi_newrelic-5.9.0a1680282898/pulumi_newrelic/one_dashboard_raw.py`

 * *Files identical despite different names*

### Comparing `pulumi_newrelic-5.9.0/pulumi_newrelic/outputs.py` & `pulumi_newrelic-5.9.0a1680282898/pulumi_newrelic/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_newrelic-5.9.0/pulumi_newrelic/plugins/_inputs.py` & `pulumi_newrelic-5.9.0a1680282898/pulumi_newrelic/plugins/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_newrelic-5.9.0/pulumi_newrelic/plugins/application_settings.py` & `pulumi_newrelic-5.9.0a1680282898/pulumi_newrelic/plugins/application_settings.py`

 * *Files identical despite different names*

### Comparing `pulumi_newrelic-5.9.0/pulumi_newrelic/plugins/outputs.py` & `pulumi_newrelic-5.9.0a1680282898/pulumi_newrelic/plugins/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_newrelic-5.9.0/pulumi_newrelic/plugins/workload.py` & `pulumi_newrelic-5.9.0a1680282898/pulumi_newrelic/plugins/workload.py`

 * *Files identical despite different names*

### Comparing `pulumi_newrelic-5.9.0/pulumi_newrelic/provider.py` & `pulumi_newrelic-5.9.0a1680282898/pulumi_newrelic/provider.py`

 * *Files identical despite different names*

### Comparing `pulumi_newrelic-5.9.0/pulumi_newrelic/service_level.py` & `pulumi_newrelic-5.9.0a1680282898/pulumi_newrelic/service_level.py`

 * *Files identical despite different names*

### Comparing `pulumi_newrelic-5.9.0/pulumi_newrelic/synthetics/__init__.py` & `pulumi_newrelic-5.9.0a1680282898/pulumi_newrelic/synthetics/__init__.py`

 * *Files identical despite different names*

### Comparing `pulumi_newrelic-5.9.0/pulumi_newrelic/synthetics/_inputs.py` & `pulumi_newrelic-5.9.0a1680282898/pulumi_newrelic/synthetics/_inputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_newrelic-5.9.0/pulumi_newrelic/synthetics/alert_condition.py` & `pulumi_newrelic-5.9.0a1680282898/pulumi_newrelic/synthetics/alert_condition.py`

 * *Files identical despite different names*

### Comparing `pulumi_newrelic-5.9.0/pulumi_newrelic/synthetics/broken_links_monitor.py` & `pulumi_newrelic-5.9.0a1680282898/pulumi_newrelic/synthetics/broken_links_monitor.py`

 * *Files identical despite different names*

### Comparing `pulumi_newrelic-5.9.0/pulumi_newrelic/synthetics/cert_check_monitor.py` & `pulumi_newrelic-5.9.0a1680282898/pulumi_newrelic/synthetics/cert_check_monitor.py`

 * *Files identical despite different names*

### Comparing `pulumi_newrelic-5.9.0/pulumi_newrelic/synthetics/get_private_location.py` & `pulumi_newrelic-5.9.0a1680282898/pulumi_newrelic/synthetics/get_private_location.py`

 * *Files identical despite different names*

### Comparing `pulumi_newrelic-5.9.0/pulumi_newrelic/synthetics/get_secure_credential.py` & `pulumi_newrelic-5.9.0a1680282898/pulumi_newrelic/synthetics/get_secure_credential.py`

 * *Files identical despite different names*

### Comparing `pulumi_newrelic-5.9.0/pulumi_newrelic/synthetics/monitor.py` & `pulumi_newrelic-5.9.0a1680282898/pulumi_newrelic/synthetics/monitor.py`

 * *Files identical despite different names*

### Comparing `pulumi_newrelic-5.9.0/pulumi_newrelic/synthetics/multi_location_alert_condition.py` & `pulumi_newrelic-5.9.0a1680282898/pulumi_newrelic/synthetics/multi_location_alert_condition.py`

 * *Files identical despite different names*

### Comparing `pulumi_newrelic-5.9.0/pulumi_newrelic/synthetics/outputs.py` & `pulumi_newrelic-5.9.0a1680282898/pulumi_newrelic/synthetics/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_newrelic-5.9.0/pulumi_newrelic/synthetics/private_location.py` & `pulumi_newrelic-5.9.0a1680282898/pulumi_newrelic/synthetics/private_location.py`

 * *Files identical despite different names*

### Comparing `pulumi_newrelic-5.9.0/pulumi_newrelic/synthetics/script_monitor.py` & `pulumi_newrelic-5.9.0a1680282898/pulumi_newrelic/synthetics/script_monitor.py`

 * *Files identical despite different names*

### Comparing `pulumi_newrelic-5.9.0/pulumi_newrelic/synthetics/secure_credential.py` & `pulumi_newrelic-5.9.0a1680282898/pulumi_newrelic/synthetics/secure_credential.py`

 * *Files identical despite different names*

### Comparing `pulumi_newrelic-5.9.0/pulumi_newrelic/synthetics/step_monitor.py` & `pulumi_newrelic-5.9.0a1680282898/pulumi_newrelic/synthetics/step_monitor.py`

 * *Files identical despite different names*

### Comparing `pulumi_newrelic-5.9.0/pulumi_newrelic/workflow.py` & `pulumi_newrelic-5.9.0a1680282898/pulumi_newrelic/workflow.py`

 * *Files identical despite different names*

### Comparing `pulumi_newrelic-5.9.0/pulumi_newrelic.egg-info/PKG-INFO` & `pulumi_newrelic-5.9.0a1680282898/pulumi_newrelic.egg-info/PKG-INFO`

 * *Files 2% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: pulumi-newrelic
-Version: 5.9.0
+Version: 5.9.0a1680282898
 Summary: A Pulumi package for creating and managing New Relic resources.
 Home-page: https://pulumi.io
 License: Apache-2.0
 Project-URL: Repository, https://github.com/pulumi/pulumi-newrelic
 Keywords: pulumi new relic
 Platform: UNKNOWN
 Description-Content-Type: text/markdown
```

### Comparing `pulumi_newrelic-5.9.0/pulumi_newrelic.egg-info/SOURCES.txt` & `pulumi_newrelic-5.9.0a1680282898/pulumi_newrelic.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `pulumi_newrelic-5.9.0/setup.py` & `pulumi_newrelic-5.9.0a1680282898/setup.py`

 * *Files 10% similar despite different names*

```diff
@@ -4,16 +4,16 @@
 
 import errno
 from setuptools import setup, find_packages
 from setuptools.command.install import install
 from subprocess import check_call
 
 
-VERSION = "5.9.0"
-PLUGIN_VERSION = "5.9.0"
+VERSION = "5.9.0a1680282898"
+PLUGIN_VERSION = "5.9.0-alpha.1680282898+b0d47700"
 
 class InstallPluginCommand(install):
     def run(self):
         install.run(self)
         try:
             check_call(['pulumi', 'plugin', 'install', 'resource', 'newrelic', PLUGIN_VERSION])
         except OSError as error:
```

