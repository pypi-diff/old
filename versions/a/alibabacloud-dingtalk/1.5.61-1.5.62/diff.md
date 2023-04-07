# Comparing `tmp/alibabacloud_dingtalk-1.5.61.tar.gz` & `tmp/alibabacloud_dingtalk-1.5.62.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "dist/alibabacloud_dingtalk-1.5.61.tar", last modified: Tue Apr  4 03:45:24 2023, max compression
+gzip compressed data, was "dist/alibabacloud_dingtalk-1.5.62.tar", last modified: Fri Apr  7 09:21:49 2023, max compression
```

## Comparing `alibabacloud_dingtalk-1.5.61.tar` & `alibabacloud_dingtalk-1.5.62.tar`

### file list

```diff
@@ -1,345 +1,345 @@
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/
--rw-r--r--   0 root         (0) root         (0)    18844 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/ChangeLog.md
--rw-r--r--   0 root         (0) root         (0)      600 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/LICENSE
--rw-r--r--   0 root         (0) root         (0)       29 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/MANIFEST.in
--rw-r--r--   0 root         (0) root         (0)     2309 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/PKG-INFO
--rw-r--r--   0 root         (0) root         (0)     1021 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/README-CN.md
--rw-r--r--   0 root         (0) root         (0)     1106 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/README.md
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/
--rw-r--r--   0 root         (0) root         (0)       22 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/__init__.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/algo_1_0/
--rw-r--r--   0 root         (0) root         (0)       22 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/algo_1_0/__init__.py
--rw-r--r--   0 root         (0) root         (0)     8708 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/algo_1_0/client.py
--rw-r--r--   0 root         (0) root         (0)    22962 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/algo_1_0/models.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/alitrip_1_0/
--rw-r--r--   0 root         (0) root         (0)       22 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/alitrip_1_0/__init__.py
--rw-r--r--   0 root         (0) root         (0)    51882 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/alitrip_1_0/client.py
--rw-r--r--   0 root         (0) root         (0)   179168 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/alitrip_1_0/models.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/apaas_1_0/
--rw-r--r--   0 root         (0) root         (0)       22 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/apaas_1_0/__init__.py
--rw-r--r--   0 root         (0) root         (0)    21344 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/apaas_1_0/client.py
--rw-r--r--   0 root         (0) root         (0)    44730 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/apaas_1_0/models.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/app_market_1_0/
--rw-r--r--   0 root         (0) root         (0)       22 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/app_market_1_0/__init__.py
--rw-r--r--   0 root         (0) root         (0)    18586 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/app_market_1_0/client.py
--rw-r--r--   0 root         (0) root         (0)    22436 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/app_market_1_0/models.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/ats_1_0/
--rw-r--r--   0 root         (0) root         (0)       22 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/ats_1_0/__init__.py
--rw-r--r--   0 root         (0) root         (0)    81490 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/ats_1_0/client.py
--rw-r--r--   0 root         (0) root         (0)   140148 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/ats_1_0/models.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/attendance_1_0/
--rw-r--r--   0 root         (0) root         (0)       22 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/attendance_1_0/__init__.py
--rw-r--r--   0 root         (0) root         (0)   134106 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/attendance_1_0/client.py
--rw-r--r--   0 root         (0) root         (0)   293873 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/attendance_1_0/models.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/badge_1_0/
--rw-r--r--   0 root         (0) root         (0)       22 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/badge_1_0/__init__.py
--rw-r--r--   0 root         (0) root         (0)    40908 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/badge_1_0/client.py
--rw-r--r--   0 root         (0) root         (0)    63666 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/badge_1_0/models.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/bizfinance_1_0/
--rw-r--r--   0 root         (0) root         (0)       22 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/bizfinance_1_0/__init__.py
--rw-r--r--   0 root         (0) root         (0)   173592 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/bizfinance_1_0/client.py
--rw-r--r--   0 root         (0) root         (0)   561928 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/bizfinance_1_0/models.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/blackboard_1_0/
--rw-r--r--   0 root         (0) root         (0)       22 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/blackboard_1_0/__init__.py
--rw-r--r--   0 root         (0) root         (0)     4180 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/blackboard_1_0/client.py
--rw-r--r--   0 root         (0) root         (0)     3576 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/blackboard_1_0/models.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/calendar_1_0/
--rw-r--r--   0 root         (0) root         (0)       22 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/calendar_1_0/__init__.py
--rw-r--r--   0 root         (0) root         (0)   130914 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/calendar_1_0/client.py
--rw-r--r--   0 root         (0) root         (0)   326360 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/calendar_1_0/models.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/carbon_1_0/
--rw-r--r--   0 root         (0) root         (0)       22 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/carbon_1_0/__init__.py
--rw-r--r--   0 root         (0) root         (0)    24154 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/carbon_1_0/client.py
--rw-r--r--   0 root         (0) root         (0)    41993 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/carbon_1_0/models.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/card_1_0/
--rw-r--r--   0 root         (0) root         (0)       22 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/card_1_0/__init__.py
--rw-r--r--   0 root         (0) root         (0)    31362 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/card_1_0/client.py
--rw-r--r--   0 root         (0) root         (0)   106693 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/card_1_0/models.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/chengfeng_1_0/
--rw-r--r--   0 root         (0) root         (0)       22 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/chengfeng_1_0/__init__.py
--rw-r--r--   0 root         (0) root         (0)    61834 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/chengfeng_1_0/client.py
--rw-r--r--   0 root         (0) root         (0)   121561 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/chengfeng_1_0/models.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/conference_1_0/
--rw-r--r--   0 root         (0) root         (0)       22 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/conference_1_0/__init__.py
--rw-r--r--   0 root         (0) root         (0)    56162 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/conference_1_0/client.py
--rw-r--r--   0 root         (0) root         (0)    82298 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/conference_1_0/models.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/connector_1_0/
--rw-r--r--   0 root         (0) root         (0)       22 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/connector_1_0/__init__.py
--rw-r--r--   0 root         (0) root         (0)    51372 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/connector_1_0/client.py
--rw-r--r--   0 root         (0) root         (0)   127231 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/connector_1_0/models.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/contact_1_0/
--rw-r--r--   0 root         (0) root         (0)       22 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/contact_1_0/__init__.py
--rw-r--r--   0 root         (0) root         (0)   260294 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/contact_1_0/client.py
--rw-r--r--   0 root         (0) root         (0)   382314 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/contact_1_0/models.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/content_1_0/
--rw-r--r--   0 root         (0) root         (0)       22 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/content_1_0/__init__.py
--rw-r--r--   0 root         (0) root         (0)    18716 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/content_1_0/client.py
--rw-r--r--   0 root         (0) root         (0)    44885 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/content_1_0/models.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/contract_1_0/
--rw-r--r--   0 root         (0) root         (0)       22 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/contract_1_0/__init__.py
--rw-r--r--   0 root         (0) root         (0)     5814 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/contract_1_0/client.py
--rw-r--r--   0 root         (0) root         (0)    10402 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/contract_1_0/models.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/conv_file_1_0/
--rw-r--r--   0 root         (0) root         (0)       22 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/conv_file_1_0/__init__.py
--rw-r--r--   0 root         (0) root         (0)    15642 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/conv_file_1_0/client.py
--rw-r--r--   0 root         (0) root         (0)    32114 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/conv_file_1_0/models.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/crm_1_0/
--rw-r--r--   0 root         (0) root         (0)       22 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/crm_1_0/__init__.py
--rw-r--r--   0 root         (0) root         (0)   194896 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/crm_1_0/client.py
--rw-r--r--   0 root         (0) root         (0)   555654 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/crm_1_0/models.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/crm_2_0/
--rw-r--r--   0 root         (0) root         (0)       22 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/crm_2_0/__init__.py
--rw-r--r--   0 root         (0) root         (0)     4048 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/crm_2_0/client.py
--rw-r--r--   0 root         (0) root         (0)     7207 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/crm_2_0/models.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/customer_service_1_0/
--rw-r--r--   0 root         (0) root         (0)       22 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/customer_service_1_0/__init__.py
--rw-r--r--   0 root         (0) root         (0)    29122 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/customer_service_1_0/client.py
--rw-r--r--   0 root         (0) root         (0)    47050 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/customer_service_1_0/models.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/datacenter_1_0/
--rw-r--r--   0 root         (0) root         (0)       22 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/datacenter_1_0/__init__.py
--rw-r--r--   0 root         (0) root         (0)   340246 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/datacenter_1_0/client.py
--rw-r--r--   0 root         (0) root         (0)   503096 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/datacenter_1_0/models.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/devicemng_1_0/
--rw-r--r--   0 root         (0) root         (0)       22 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/devicemng_1_0/__init__.py
--rw-r--r--   0 root         (0) root         (0)    99276 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/devicemng_1_0/client.py
--rw-r--r--   0 root         (0) root         (0)   149418 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/devicemng_1_0/models.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/dingmi_1_0/
--rw-r--r--   0 root         (0) root         (0)       22 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/dingmi_1_0/__init__.py
--rw-r--r--   0 root         (0) root         (0)    50064 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/dingmi_1_0/client.py
--rw-r--r--   0 root         (0) root         (0)    53792 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/dingmi_1_0/models.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/diot_1_0/
--rw-r--r--   0 root         (0) root         (0)       22 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/diot_1_0/__init__.py
--rw-r--r--   0 root         (0) root         (0)    40488 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/diot_1_0/client.py
--rw-r--r--   0 root         (0) root         (0)    66172 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/diot_1_0/models.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/doc_1_0/
--rw-r--r--   0 root         (0) root         (0)       22 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/doc_1_0/__init__.py
--rw-r--r--   0 root         (0) root         (0)   196916 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/doc_1_0/client.py
--rw-r--r--   0 root         (0) root         (0)   261579 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/doc_1_0/models.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/doc_2_0/
--rw-r--r--   0 root         (0) root         (0)       22 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/doc_2_0/__init__.py
--rw-r--r--   0 root         (0) root         (0)   134506 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/doc_2_0/client.py
--rw-r--r--   0 root         (0) root         (0)   276268 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/doc_2_0/models.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/drive_1_0/
--rw-r--r--   0 root         (0) root         (0)       22 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/drive_1_0/__init__.py
--rw-r--r--   0 root         (0) root         (0)   127432 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/drive_1_0/client.py
--rw-r--r--   0 root         (0) root         (0)   192831 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/drive_1_0/models.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/edu_1_0/
--rw-r--r--   0 root         (0) root         (0)       22 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/edu_1_0/__init__.py
--rw-r--r--   0 root         (0) root         (0)   401586 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/edu_1_0/client.py
--rw-r--r--   0 root         (0) root         (0)   699718 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/edu_1_0/models.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/esign_1_0/
--rw-r--r--   0 root         (0) root         (0)       22 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/esign_1_0/__init__.py
--rw-r--r--   0 root         (0) root         (0)    62504 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/esign_1_0/client.py
--rw-r--r--   0 root         (0) root         (0)   110186 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/esign_1_0/models.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/esign_2_0/
--rw-r--r--   0 root         (0) root         (0)       22 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/esign_2_0/__init__.py
--rw-r--r--   0 root         (0) root         (0)    75706 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/esign_2_0/client.py
--rw-r--r--   0 root         (0) root         (0)   118345 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/esign_2_0/models.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/event_1_0/
--rw-r--r--   0 root         (0) root         (0)       22 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/event_1_0/__init__.py
--rw-r--r--   0 root         (0) root         (0)     4334 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/event_1_0/client.py
--rw-r--r--   0 root         (0) root         (0)     6225 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/event_1_0/models.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/exclusive_1_0/
--rw-r--r--   0 root         (0) root         (0)       22 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/exclusive_1_0/__init__.py
--rw-r--r--   0 root         (0) root         (0)   265864 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/exclusive_1_0/client.py
--rw-r--r--   0 root         (0) root         (0)   411363 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/exclusive_1_0/models.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/finance_1_0/
--rw-r--r--   0 root         (0) root         (0)       22 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/finance_1_0/__init__.py
--rw-r--r--   0 root         (0) root         (0)   140236 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/finance_1_0/client.py
--rw-r--r--   0 root         (0) root         (0)   310177 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/finance_1_0/models.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/flashmeeting_1_0/
--rw-r--r--   0 root         (0) root         (0)       22 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/flashmeeting_1_0/__init__.py
--rw-r--r--   0 root         (0) root         (0)     4520 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/flashmeeting_1_0/client.py
--rw-r--r--   0 root         (0) root         (0)     5052 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/flashmeeting_1_0/models.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/group_blackboard_1_0/
--rw-r--r--   0 root         (0) root         (0)       22 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/group_blackboard_1_0/__init__.py
--rw-r--r--   0 root         (0) root         (0)     9290 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/group_blackboard_1_0/client.py
--rw-r--r--   0 root         (0) root         (0)     9446 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/group_blackboard_1_0/models.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/h3yun_1_0/
--rw-r--r--   0 root         (0) root         (0)       22 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/h3yun_1_0/__init__.py
--rw-r--r--   0 root         (0) root         (0)    69681 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/h3yun_1_0/client.py
--rw-r--r--   0 root         (0) root         (0)   140857 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/h3yun_1_0/models.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/h5package_1_0/
--rw-r--r--   0 root         (0) root         (0)       22 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/h5package_1_0/__init__.py
--rw-r--r--   0 root         (0) root         (0)    14767 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/h5package_1_0/client.py
--rw-r--r--   0 root         (0) root         (0)    18751 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/h5package_1_0/models.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/hrbrain_1_0/
--rw-r--r--   0 root         (0) root         (0)       22 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/hrbrain_1_0/__init__.py
--rw-r--r--   0 root         (0) root         (0)     4620 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/hrbrain_1_0/client.py
--rw-r--r--   0 root         (0) root         (0)     4336 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/hrbrain_1_0/models.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/hrm_1_0/
--rw-r--r--   0 root         (0) root         (0)       22 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/hrm_1_0/__init__.py
--rw-r--r--   0 root         (0) root         (0)    79106 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/hrm_1_0/client.py
--rw-r--r--   0 root         (0) root         (0)   133812 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/hrm_1_0/models.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/im_1_0/
--rw-r--r--   0 root         (0) root         (0)       22 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/im_1_0/__init__.py
--rw-r--r--   0 root         (0) root         (0)   268744 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/im_1_0/client.py
--rw-r--r--   0 root         (0) root         (0)   381405 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/im_1_0/models.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/im_2_0/
--rw-r--r--   0 root         (0) root         (0)       22 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/im_2_0/__init__.py
--rw-r--r--   0 root         (0) root         (0)    12612 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/im_2_0/client.py
--rw-r--r--   0 root         (0) root         (0)    19194 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/im_2_0/models.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/impaas_1_0/
--rw-r--r--   0 root         (0) root         (0)       22 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/impaas_1_0/__init__.py
--rw-r--r--   0 root         (0) root         (0)    76078 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/impaas_1_0/client.py
--rw-r--r--   0 root         (0) root         (0)    83510 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/impaas_1_0/models.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/industry_1_0/
--rw-r--r--   0 root         (0) root         (0)       22 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/industry_1_0/__init__.py
--rw-r--r--   0 root         (0) root         (0)   438740 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/industry_1_0/client.py
--rw-r--r--   0 root         (0) root         (0)   707813 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/industry_1_0/models.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/jzcrm_1_0/
--rw-r--r--   0 root         (0) root         (0)       22 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/jzcrm_1_0/__init__.py
--rw-r--r--   0 root         (0) root         (0)    54446 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/jzcrm_1_0/client.py
--rw-r--r--   0 root         (0) root         (0)   160887 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/jzcrm_1_0/models.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/link_1_0/
--rw-r--r--   0 root         (0) root         (0)       22 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/link_1_0/__init__.py
--rw-r--r--   0 root         (0) root         (0)    54782 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/link_1_0/client.py
--rw-r--r--   0 root         (0) root         (0)   111368 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/link_1_0/models.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/live_1_0/
--rw-r--r--   0 root         (0) root         (0)       22 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/live_1_0/__init__.py
--rw-r--r--   0 root         (0) root         (0)    77806 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/live_1_0/client.py
--rw-r--r--   0 root         (0) root         (0)   129784 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/live_1_0/models.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/manufacturing_1_0/
--rw-r--r--   0 root         (0) root         (0)       22 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/manufacturing_1_0/__init__.py
--rw-r--r--   0 root         (0) root         (0)    14978 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/manufacturing_1_0/client.py
--rw-r--r--   0 root         (0) root         (0)    24607 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/manufacturing_1_0/models.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/micro_app_1_0/
--rw-r--r--   0 root         (0) root         (0)       22 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/micro_app_1_0/__init__.py
--rw-r--r--   0 root         (0) root         (0)   117228 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/micro_app_1_0/client.py
--rw-r--r--   0 root         (0) root         (0)   154147 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/micro_app_1_0/models.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/miniapp_1_0/
--rw-r--r--   0 root         (0) root         (0)       22 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/miniapp_1_0/__init__.py
--rw-r--r--   0 root         (0) root         (0)    45940 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/miniapp_1_0/client.py
--rw-r--r--   0 root         (0) root         (0)    51039 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/miniapp_1_0/models.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/oauth2_1_0/
--rw-r--r--   0 root         (0) root         (0)       22 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/oauth2_1_0/__init__.py
--rw-r--r--   0 root         (0) root         (0)    26123 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/oauth2_1_0/client.py
--rw-r--r--   0 root         (0) root         (0)    39828 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/oauth2_1_0/models.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/occupationauth_1_0/
--rw-r--r--   0 root         (0) root         (0)       22 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/occupationauth_1_0/__init__.py
--rw-r--r--   0 root         (0) root         (0)     7690 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/occupationauth_1_0/client.py
--rw-r--r--   0 root         (0) root         (0)     6891 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/occupationauth_1_0/models.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/okr_1_0/
--rw-r--r--   0 root         (0) root         (0)       22 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/okr_1_0/__init__.py
--rw-r--r--   0 root         (0) root         (0)    67864 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/okr_1_0/client.py
--rw-r--r--   0 root         (0) root         (0)   137575 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/okr_1_0/models.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/org_culture_1_0/
--rw-r--r--   0 root         (0) root         (0)       22 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/org_culture_1_0/__init__.py
--rw-r--r--   0 root         (0) root         (0)    68812 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/org_culture_1_0/client.py
--rw-r--r--   0 root         (0) root         (0)   125156 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/org_culture_1_0/models.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/package_1_0/
--rw-r--r--   0 root         (0) root         (0)       22 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/package_1_0/__init__.py
--rw-r--r--   0 root         (0) root         (0)    48952 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/package_1_0/client.py
--rw-r--r--   0 root         (0) root         (0)    57536 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/package_1_0/models.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/project_1_0/
--rw-r--r--   0 root         (0) root         (0)       22 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/project_1_0/__init__.py
--rw-r--r--   0 root         (0) root         (0)   233262 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/project_1_0/client.py
--rw-r--r--   0 root         (0) root         (0)   399779 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/project_1_0/models.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/project_integration_1_0/
--rw-r--r--   0 root         (0) root         (0)       22 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/project_integration_1_0/__init__.py
--rw-r--r--   0 root         (0) root         (0)    16002 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/project_integration_1_0/client.py
--rw-r--r--   0 root         (0) root         (0)     9973 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/project_integration_1_0/models.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/rcs_call_1_0/
--rw-r--r--   0 root         (0) root         (0)       22 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/rcs_call_1_0/__init__.py
--rw-r--r--   0 root         (0) root         (0)     4606 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/rcs_call_1_0/client.py
--rw-r--r--   0 root         (0) root         (0)     4435 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/rcs_call_1_0/models.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/resident_1_0/
--rw-r--r--   0 root         (0) root         (0)       22 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/resident_1_0/__init__.py
--rw-r--r--   0 root         (0) root         (0)   118728 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/resident_1_0/client.py
--rw-r--r--   0 root         (0) root         (0)   171405 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/resident_1_0/models.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/robot_1_0/
--rw-r--r--   0 root         (0) root         (0)       22 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/robot_1_0/__init__.py
--rw-r--r--   0 root         (0) root         (0)    71838 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/robot_1_0/client.py
--rw-r--r--   0 root         (0) root         (0)    91606 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/robot_1_0/models.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/rooms_1_0/
--rw-r--r--   0 root         (0) root         (0)       22 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/rooms_1_0/__init__.py
--rw-r--r--   0 root         (0) root         (0)    50744 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/rooms_1_0/client.py
--rw-r--r--   0 root         (0) root         (0)    82767 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/rooms_1_0/models.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/search_1_0/
--rw-r--r--   0 root         (0) root         (0)       22 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/search_1_0/__init__.py
--rw-r--r--   0 root         (0) root         (0)    35104 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/search_1_0/client.py
--rw-r--r--   0 root         (0) root         (0)    47649 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/search_1_0/models.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/service_group_1_0/
--rw-r--r--   0 root         (0) root         (0)       22 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/service_group_1_0/__init__.py
--rw-r--r--   0 root         (0) root         (0)   322628 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/service_group_1_0/client.py
--rw-r--r--   0 root         (0) root         (0)   499096 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/service_group_1_0/models.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/smart_device_1_0/
--rw-r--r--   0 root         (0) root         (0)       22 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/smart_device_1_0/__init__.py
--rw-r--r--   0 root         (0) root         (0)    28634 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/smart_device_1_0/client.py
--rw-r--r--   0 root         (0) root         (0)    25101 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/smart_device_1_0/models.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/sns_storage_1_0/
--rw-r--r--   0 root         (0) root         (0)       22 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/sns_storage_1_0/__init__.py
--rw-r--r--   0 root         (0) root         (0)    40406 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/sns_storage_1_0/client.py
--rw-r--r--   0 root         (0) root         (0)   105120 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/sns_storage_1_0/models.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/storage_1_0/
--rw-r--r--   0 root         (0) root         (0)       22 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/storage_1_0/__init__.py
--rw-r--r--   0 root         (0) root         (0)   173162 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/storage_1_0/client.py
--rw-r--r--   0 root         (0) root         (0)   389740 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/storage_1_0/models.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/storage_2_0/
--rw-r--r--   0 root         (0) root         (0)       22 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/storage_2_0/__init__.py
--rw-r--r--   0 root         (0) root         (0)     9158 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/storage_2_0/client.py
--rw-r--r--   0 root         (0) root         (0)    31448 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/storage_2_0/models.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/swform_1_0/
--rw-r--r--   0 root         (0) root         (0)       22 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/swform_1_0/__init__.py
--rw-r--r--   0 root         (0) root         (0)    12420 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/swform_1_0/client.py
--rw-r--r--   0 root         (0) root         (0)    30097 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/swform_1_0/models.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/todo_1_0/
--rw-r--r--   0 root         (0) root         (0)       22 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/todo_1_0/__init__.py
--rw-r--r--   0 root         (0) root         (0)    60784 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/todo_1_0/client.py
--rw-r--r--   0 root         (0) root         (0)   156671 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/todo_1_0/models.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/trade_1_0/
--rw-r--r--   0 root         (0) root         (0)       22 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/trade_1_0/__init__.py
--rw-r--r--   0 root         (0) root         (0)    12502 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/trade_1_0/client.py
--rw-r--r--   0 root         (0) root         (0)    16057 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/trade_1_0/models.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/trajectory_1_0/
--rw-r--r--   0 root         (0) root         (0)       22 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/trajectory_1_0/__init__.py
--rw-r--r--   0 root         (0) root         (0)    12410 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/trajectory_1_0/client.py
--rw-r--r--   0 root         (0) root         (0)    21548 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/trajectory_1_0/models.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/transcribe_1_0/
--rw-r--r--   0 root         (0) root         (0)       22 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/transcribe_1_0/__init__.py
--rw-r--r--   0 root         (0) root         (0)    12290 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/transcribe_1_0/client.py
--rw-r--r--   0 root         (0) root         (0)    17800 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/transcribe_1_0/models.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/trip_1_0/
--rw-r--r--   0 root         (0) root         (0)       22 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/trip_1_0/__init__.py
--rw-r--r--   0 root         (0) root         (0)    16936 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/trip_1_0/client.py
--rw-r--r--   0 root         (0) root         (0)    33576 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/trip_1_0/models.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/village_1_0/
--rw-r--r--   0 root         (0) root         (0)       22 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/village_1_0/__init__.py
--rw-r--r--   0 root         (0) root         (0)    68340 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/village_1_0/client.py
--rw-r--r--   0 root         (0) root         (0)   110827 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/village_1_0/models.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/watt_1_0/
--rw-r--r--   0 root         (0) root         (0)       22 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/watt_1_0/__init__.py
--rw-r--r--   0 root         (0) root         (0)     3452 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/watt_1_0/client.py
--rw-r--r--   0 root         (0) root         (0)     3124 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/watt_1_0/models.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/wiki_1_0/
--rw-r--r--   0 root         (0) root         (0)       22 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/wiki_1_0/__init__.py
--rw-r--r--   0 root         (0) root         (0)     7006 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/wiki_1_0/client.py
--rw-r--r--   0 root         (0) root         (0)    20769 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/wiki_1_0/models.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/wms_1_0/
--rw-r--r--   0 root         (0) root         (0)       22 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/wms_1_0/__init__.py
--rw-r--r--   0 root         (0) root         (0)     4608 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/wms_1_0/client.py
--rw-r--r--   0 root         (0) root         (0)     8329 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/wms_1_0/models.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/workbench_1_0/
--rw-r--r--   0 root         (0) root         (0)       22 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/workbench_1_0/__init__.py
--rw-r--r--   0 root         (0) root         (0)    24540 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/workbench_1_0/client.py
--rw-r--r--   0 root         (0) root         (0)    28057 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/workbench_1_0/models.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/workflow_1_0/
--rw-r--r--   0 root         (0) root         (0)       22 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/workflow_1_0/__init__.py
--rw-r--r--   0 root         (0) root         (0)   154430 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/workflow_1_0/client.py
--rw-r--r--   0 root         (0) root         (0)   385214 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/workflow_1_0/models.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/workrecord_1_0/
--rw-r--r--   0 root         (0) root         (0)       22 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/workrecord_1_0/__init__.py
--rw-r--r--   0 root         (0) root         (0)     4012 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/workrecord_1_0/client.py
--rw-r--r--   0 root         (0) root         (0)     3485 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/workrecord_1_0/models.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/yida_1_0/
--rw-r--r--   0 root         (0) root         (0)       22 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/yida_1_0/__init__.py
--rw-r--r--   0 root         (0) root         (0)   416280 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/yida_1_0/client.py
--rw-r--r--   0 root         (0) root         (0)   690137 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/yida_1_0/models.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk.egg-info/
--rw-r--r--   0 root         (0) root         (0)     2309 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk.egg-info/PKG-INFO
--rw-r--r--   0 root         (0) root         (0)    11356 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk.egg-info/SOURCES.txt
--rw-r--r--   0 root         (0) root         (0)        1 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk.egg-info/dependency_links.txt
--rw-r--r--   0 root         (0) root         (0)      156 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk.egg-info/requires.txt
--rw-r--r--   0 root         (0) root         (0)       22 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk.egg-info/top_level.txt
--rw-r--r--   0 root         (0) root         (0)       73 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/setup.cfg
--rw-r--r--   0 root         (0) root         (0)     2585 2023-04-04 03:45:24.000000 alibabacloud_dingtalk-1.5.61/setup.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/
+-rw-r--r--   0 root         (0) root         (0)    18909 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/ChangeLog.md
+-rw-r--r--   0 root         (0) root         (0)      600 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/LICENSE
+-rw-r--r--   0 root         (0) root         (0)       29 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/MANIFEST.in
+-rw-r--r--   0 root         (0) root         (0)     2309 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/PKG-INFO
+-rw-r--r--   0 root         (0) root         (0)     1021 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/README-CN.md
+-rw-r--r--   0 root         (0) root         (0)     1106 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/README.md
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/
+-rw-r--r--   0 root         (0) root         (0)       22 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/__init__.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/algo_1_0/
+-rw-r--r--   0 root         (0) root         (0)       22 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/algo_1_0/__init__.py
+-rw-r--r--   0 root         (0) root         (0)     8708 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/algo_1_0/client.py
+-rw-r--r--   0 root         (0) root         (0)    22962 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/algo_1_0/models.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/alitrip_1_0/
+-rw-r--r--   0 root         (0) root         (0)       22 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/alitrip_1_0/__init__.py
+-rw-r--r--   0 root         (0) root         (0)    51882 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/alitrip_1_0/client.py
+-rw-r--r--   0 root         (0) root         (0)   179168 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/alitrip_1_0/models.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/apaas_1_0/
+-rw-r--r--   0 root         (0) root         (0)       22 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/apaas_1_0/__init__.py
+-rw-r--r--   0 root         (0) root         (0)    21344 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/apaas_1_0/client.py
+-rw-r--r--   0 root         (0) root         (0)    44730 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/apaas_1_0/models.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/app_market_1_0/
+-rw-r--r--   0 root         (0) root         (0)       22 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/app_market_1_0/__init__.py
+-rw-r--r--   0 root         (0) root         (0)    18586 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/app_market_1_0/client.py
+-rw-r--r--   0 root         (0) root         (0)    22436 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/app_market_1_0/models.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/ats_1_0/
+-rw-r--r--   0 root         (0) root         (0)       22 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/ats_1_0/__init__.py
+-rw-r--r--   0 root         (0) root         (0)    81490 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/ats_1_0/client.py
+-rw-r--r--   0 root         (0) root         (0)   140148 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/ats_1_0/models.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/attendance_1_0/
+-rw-r--r--   0 root         (0) root         (0)       22 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/attendance_1_0/__init__.py
+-rw-r--r--   0 root         (0) root         (0)   134106 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/attendance_1_0/client.py
+-rw-r--r--   0 root         (0) root         (0)   294751 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/attendance_1_0/models.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/badge_1_0/
+-rw-r--r--   0 root         (0) root         (0)       22 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/badge_1_0/__init__.py
+-rw-r--r--   0 root         (0) root         (0)    40908 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/badge_1_0/client.py
+-rw-r--r--   0 root         (0) root         (0)    63666 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/badge_1_0/models.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/bizfinance_1_0/
+-rw-r--r--   0 root         (0) root         (0)       22 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/bizfinance_1_0/__init__.py
+-rw-r--r--   0 root         (0) root         (0)   177626 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/bizfinance_1_0/client.py
+-rw-r--r--   0 root         (0) root         (0)   583083 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/bizfinance_1_0/models.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/blackboard_1_0/
+-rw-r--r--   0 root         (0) root         (0)       22 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/blackboard_1_0/__init__.py
+-rw-r--r--   0 root         (0) root         (0)     4180 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/blackboard_1_0/client.py
+-rw-r--r--   0 root         (0) root         (0)     3576 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/blackboard_1_0/models.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/calendar_1_0/
+-rw-r--r--   0 root         (0) root         (0)       22 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/calendar_1_0/__init__.py
+-rw-r--r--   0 root         (0) root         (0)   130914 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/calendar_1_0/client.py
+-rw-r--r--   0 root         (0) root         (0)   326360 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/calendar_1_0/models.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/carbon_1_0/
+-rw-r--r--   0 root         (0) root         (0)       22 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/carbon_1_0/__init__.py
+-rw-r--r--   0 root         (0) root         (0)    24154 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/carbon_1_0/client.py
+-rw-r--r--   0 root         (0) root         (0)    41993 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/carbon_1_0/models.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/card_1_0/
+-rw-r--r--   0 root         (0) root         (0)       22 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/card_1_0/__init__.py
+-rw-r--r--   0 root         (0) root         (0)    31362 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/card_1_0/client.py
+-rw-r--r--   0 root         (0) root         (0)   106693 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/card_1_0/models.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/chengfeng_1_0/
+-rw-r--r--   0 root         (0) root         (0)       22 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/chengfeng_1_0/__init__.py
+-rw-r--r--   0 root         (0) root         (0)    61834 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/chengfeng_1_0/client.py
+-rw-r--r--   0 root         (0) root         (0)   121561 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/chengfeng_1_0/models.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/conference_1_0/
+-rw-r--r--   0 root         (0) root         (0)       22 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/conference_1_0/__init__.py
+-rw-r--r--   0 root         (0) root         (0)    56162 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/conference_1_0/client.py
+-rw-r--r--   0 root         (0) root         (0)    82298 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/conference_1_0/models.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/connector_1_0/
+-rw-r--r--   0 root         (0) root         (0)       22 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/connector_1_0/__init__.py
+-rw-r--r--   0 root         (0) root         (0)    51372 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/connector_1_0/client.py
+-rw-r--r--   0 root         (0) root         (0)   127231 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/connector_1_0/models.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/contact_1_0/
+-rw-r--r--   0 root         (0) root         (0)       22 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/contact_1_0/__init__.py
+-rw-r--r--   0 root         (0) root         (0)   260294 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/contact_1_0/client.py
+-rw-r--r--   0 root         (0) root         (0)   382552 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/contact_1_0/models.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/content_1_0/
+-rw-r--r--   0 root         (0) root         (0)       22 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/content_1_0/__init__.py
+-rw-r--r--   0 root         (0) root         (0)    18716 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/content_1_0/client.py
+-rw-r--r--   0 root         (0) root         (0)    44885 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/content_1_0/models.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/contract_1_0/
+-rw-r--r--   0 root         (0) root         (0)       22 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/contract_1_0/__init__.py
+-rw-r--r--   0 root         (0) root         (0)     5814 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/contract_1_0/client.py
+-rw-r--r--   0 root         (0) root         (0)    10402 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/contract_1_0/models.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/conv_file_1_0/
+-rw-r--r--   0 root         (0) root         (0)       22 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/conv_file_1_0/__init__.py
+-rw-r--r--   0 root         (0) root         (0)    15642 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/conv_file_1_0/client.py
+-rw-r--r--   0 root         (0) root         (0)    32114 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/conv_file_1_0/models.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/crm_1_0/
+-rw-r--r--   0 root         (0) root         (0)       22 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/crm_1_0/__init__.py
+-rw-r--r--   0 root         (0) root         (0)   194896 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/crm_1_0/client.py
+-rw-r--r--   0 root         (0) root         (0)   555654 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/crm_1_0/models.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/crm_2_0/
+-rw-r--r--   0 root         (0) root         (0)       22 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/crm_2_0/__init__.py
+-rw-r--r--   0 root         (0) root         (0)     4048 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/crm_2_0/client.py
+-rw-r--r--   0 root         (0) root         (0)     7207 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/crm_2_0/models.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/customer_service_1_0/
+-rw-r--r--   0 root         (0) root         (0)       22 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/customer_service_1_0/__init__.py
+-rw-r--r--   0 root         (0) root         (0)    29122 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/customer_service_1_0/client.py
+-rw-r--r--   0 root         (0) root         (0)    47050 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/customer_service_1_0/models.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/datacenter_1_0/
+-rw-r--r--   0 root         (0) root         (0)       22 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/datacenter_1_0/__init__.py
+-rw-r--r--   0 root         (0) root         (0)   340246 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/datacenter_1_0/client.py
+-rw-r--r--   0 root         (0) root         (0)   503096 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/datacenter_1_0/models.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/devicemng_1_0/
+-rw-r--r--   0 root         (0) root         (0)       22 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/devicemng_1_0/__init__.py
+-rw-r--r--   0 root         (0) root         (0)    99276 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/devicemng_1_0/client.py
+-rw-r--r--   0 root         (0) root         (0)   149418 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/devicemng_1_0/models.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/dingmi_1_0/
+-rw-r--r--   0 root         (0) root         (0)       22 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/dingmi_1_0/__init__.py
+-rw-r--r--   0 root         (0) root         (0)    50064 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/dingmi_1_0/client.py
+-rw-r--r--   0 root         (0) root         (0)    53792 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/dingmi_1_0/models.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/diot_1_0/
+-rw-r--r--   0 root         (0) root         (0)       22 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/diot_1_0/__init__.py
+-rw-r--r--   0 root         (0) root         (0)    40488 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/diot_1_0/client.py
+-rw-r--r--   0 root         (0) root         (0)    66172 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/diot_1_0/models.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/doc_1_0/
+-rw-r--r--   0 root         (0) root         (0)       22 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/doc_1_0/__init__.py
+-rw-r--r--   0 root         (0) root         (0)   196916 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/doc_1_0/client.py
+-rw-r--r--   0 root         (0) root         (0)   261579 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/doc_1_0/models.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/doc_2_0/
+-rw-r--r--   0 root         (0) root         (0)       22 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/doc_2_0/__init__.py
+-rw-r--r--   0 root         (0) root         (0)   134506 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/doc_2_0/client.py
+-rw-r--r--   0 root         (0) root         (0)   276268 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/doc_2_0/models.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/drive_1_0/
+-rw-r--r--   0 root         (0) root         (0)       22 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/drive_1_0/__init__.py
+-rw-r--r--   0 root         (0) root         (0)   127432 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/drive_1_0/client.py
+-rw-r--r--   0 root         (0) root         (0)   192831 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/drive_1_0/models.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/edu_1_0/
+-rw-r--r--   0 root         (0) root         (0)       22 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/edu_1_0/__init__.py
+-rw-r--r--   0 root         (0) root         (0)   401586 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/edu_1_0/client.py
+-rw-r--r--   0 root         (0) root         (0)   699718 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/edu_1_0/models.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/esign_1_0/
+-rw-r--r--   0 root         (0) root         (0)       22 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/esign_1_0/__init__.py
+-rw-r--r--   0 root         (0) root         (0)    62504 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/esign_1_0/client.py
+-rw-r--r--   0 root         (0) root         (0)   110186 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/esign_1_0/models.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/esign_2_0/
+-rw-r--r--   0 root         (0) root         (0)       22 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/esign_2_0/__init__.py
+-rw-r--r--   0 root         (0) root         (0)    75706 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/esign_2_0/client.py
+-rw-r--r--   0 root         (0) root         (0)   118345 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/esign_2_0/models.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/event_1_0/
+-rw-r--r--   0 root         (0) root         (0)       22 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/event_1_0/__init__.py
+-rw-r--r--   0 root         (0) root         (0)     4334 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/event_1_0/client.py
+-rw-r--r--   0 root         (0) root         (0)     6225 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/event_1_0/models.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/exclusive_1_0/
+-rw-r--r--   0 root         (0) root         (0)       22 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/exclusive_1_0/__init__.py
+-rw-r--r--   0 root         (0) root         (0)   269266 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/exclusive_1_0/client.py
+-rw-r--r--   0 root         (0) root         (0)   414993 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/exclusive_1_0/models.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/finance_1_0/
+-rw-r--r--   0 root         (0) root         (0)       22 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/finance_1_0/__init__.py
+-rw-r--r--   0 root         (0) root         (0)   140236 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/finance_1_0/client.py
+-rw-r--r--   0 root         (0) root         (0)   310177 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/finance_1_0/models.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/flashmeeting_1_0/
+-rw-r--r--   0 root         (0) root         (0)       22 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/flashmeeting_1_0/__init__.py
+-rw-r--r--   0 root         (0) root         (0)     4520 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/flashmeeting_1_0/client.py
+-rw-r--r--   0 root         (0) root         (0)     5052 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/flashmeeting_1_0/models.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/group_blackboard_1_0/
+-rw-r--r--   0 root         (0) root         (0)       22 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/group_blackboard_1_0/__init__.py
+-rw-r--r--   0 root         (0) root         (0)     9290 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/group_blackboard_1_0/client.py
+-rw-r--r--   0 root         (0) root         (0)     9446 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/group_blackboard_1_0/models.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/h3yun_1_0/
+-rw-r--r--   0 root         (0) root         (0)       22 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/h3yun_1_0/__init__.py
+-rw-r--r--   0 root         (0) root         (0)    69681 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/h3yun_1_0/client.py
+-rw-r--r--   0 root         (0) root         (0)   140857 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/h3yun_1_0/models.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/h5package_1_0/
+-rw-r--r--   0 root         (0) root         (0)       22 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/h5package_1_0/__init__.py
+-rw-r--r--   0 root         (0) root         (0)    14767 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/h5package_1_0/client.py
+-rw-r--r--   0 root         (0) root         (0)    18751 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/h5package_1_0/models.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/hrbrain_1_0/
+-rw-r--r--   0 root         (0) root         (0)       22 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/hrbrain_1_0/__init__.py
+-rw-r--r--   0 root         (0) root         (0)     4620 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/hrbrain_1_0/client.py
+-rw-r--r--   0 root         (0) root         (0)     4336 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/hrbrain_1_0/models.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/hrm_1_0/
+-rw-r--r--   0 root         (0) root         (0)       22 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/hrm_1_0/__init__.py
+-rw-r--r--   0 root         (0) root         (0)    79106 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/hrm_1_0/client.py
+-rw-r--r--   0 root         (0) root         (0)   133812 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/hrm_1_0/models.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/im_1_0/
+-rw-r--r--   0 root         (0) root         (0)       22 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/im_1_0/__init__.py
+-rw-r--r--   0 root         (0) root         (0)   268744 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/im_1_0/client.py
+-rw-r--r--   0 root         (0) root         (0)   381405 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/im_1_0/models.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/im_2_0/
+-rw-r--r--   0 root         (0) root         (0)       22 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/im_2_0/__init__.py
+-rw-r--r--   0 root         (0) root         (0)    12612 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/im_2_0/client.py
+-rw-r--r--   0 root         (0) root         (0)    19194 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/im_2_0/models.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/impaas_1_0/
+-rw-r--r--   0 root         (0) root         (0)       22 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/impaas_1_0/__init__.py
+-rw-r--r--   0 root         (0) root         (0)    76078 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/impaas_1_0/client.py
+-rw-r--r--   0 root         (0) root         (0)    83510 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/impaas_1_0/models.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/industry_1_0/
+-rw-r--r--   0 root         (0) root         (0)       22 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/industry_1_0/__init__.py
+-rw-r--r--   0 root         (0) root         (0)   438740 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/industry_1_0/client.py
+-rw-r--r--   0 root         (0) root         (0)   707813 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/industry_1_0/models.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/jzcrm_1_0/
+-rw-r--r--   0 root         (0) root         (0)       22 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/jzcrm_1_0/__init__.py
+-rw-r--r--   0 root         (0) root         (0)    54446 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/jzcrm_1_0/client.py
+-rw-r--r--   0 root         (0) root         (0)   160887 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/jzcrm_1_0/models.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/link_1_0/
+-rw-r--r--   0 root         (0) root         (0)       22 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/link_1_0/__init__.py
+-rw-r--r--   0 root         (0) root         (0)    54782 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/link_1_0/client.py
+-rw-r--r--   0 root         (0) root         (0)   111368 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/link_1_0/models.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/live_1_0/
+-rw-r--r--   0 root         (0) root         (0)       22 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/live_1_0/__init__.py
+-rw-r--r--   0 root         (0) root         (0)    77806 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/live_1_0/client.py
+-rw-r--r--   0 root         (0) root         (0)   129784 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/live_1_0/models.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/manufacturing_1_0/
+-rw-r--r--   0 root         (0) root         (0)       22 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/manufacturing_1_0/__init__.py
+-rw-r--r--   0 root         (0) root         (0)    14978 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/manufacturing_1_0/client.py
+-rw-r--r--   0 root         (0) root         (0)    24607 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/manufacturing_1_0/models.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/micro_app_1_0/
+-rw-r--r--   0 root         (0) root         (0)       22 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/micro_app_1_0/__init__.py
+-rw-r--r--   0 root         (0) root         (0)   117228 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/micro_app_1_0/client.py
+-rw-r--r--   0 root         (0) root         (0)   154147 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/micro_app_1_0/models.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/miniapp_1_0/
+-rw-r--r--   0 root         (0) root         (0)       22 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/miniapp_1_0/__init__.py
+-rw-r--r--   0 root         (0) root         (0)    45940 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/miniapp_1_0/client.py
+-rw-r--r--   0 root         (0) root         (0)    51039 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/miniapp_1_0/models.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/oauth2_1_0/
+-rw-r--r--   0 root         (0) root         (0)       22 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/oauth2_1_0/__init__.py
+-rw-r--r--   0 root         (0) root         (0)    26123 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/oauth2_1_0/client.py
+-rw-r--r--   0 root         (0) root         (0)    39828 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/oauth2_1_0/models.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/occupationauth_1_0/
+-rw-r--r--   0 root         (0) root         (0)       22 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/occupationauth_1_0/__init__.py
+-rw-r--r--   0 root         (0) root         (0)     7690 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/occupationauth_1_0/client.py
+-rw-r--r--   0 root         (0) root         (0)     6891 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/occupationauth_1_0/models.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/okr_1_0/
+-rw-r--r--   0 root         (0) root         (0)       22 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/okr_1_0/__init__.py
+-rw-r--r--   0 root         (0) root         (0)    67864 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/okr_1_0/client.py
+-rw-r--r--   0 root         (0) root         (0)   137575 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/okr_1_0/models.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/org_culture_1_0/
+-rw-r--r--   0 root         (0) root         (0)       22 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/org_culture_1_0/__init__.py
+-rw-r--r--   0 root         (0) root         (0)    68812 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/org_culture_1_0/client.py
+-rw-r--r--   0 root         (0) root         (0)   125156 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/org_culture_1_0/models.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/package_1_0/
+-rw-r--r--   0 root         (0) root         (0)       22 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/package_1_0/__init__.py
+-rw-r--r--   0 root         (0) root         (0)    48952 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/package_1_0/client.py
+-rw-r--r--   0 root         (0) root         (0)    57536 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/package_1_0/models.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/project_1_0/
+-rw-r--r--   0 root         (0) root         (0)       22 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/project_1_0/__init__.py
+-rw-r--r--   0 root         (0) root         (0)   233262 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/project_1_0/client.py
+-rw-r--r--   0 root         (0) root         (0)   399779 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/project_1_0/models.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/project_integration_1_0/
+-rw-r--r--   0 root         (0) root         (0)       22 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/project_integration_1_0/__init__.py
+-rw-r--r--   0 root         (0) root         (0)    16002 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/project_integration_1_0/client.py
+-rw-r--r--   0 root         (0) root         (0)     9973 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/project_integration_1_0/models.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/rcs_call_1_0/
+-rw-r--r--   0 root         (0) root         (0)       22 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/rcs_call_1_0/__init__.py
+-rw-r--r--   0 root         (0) root         (0)     4606 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/rcs_call_1_0/client.py
+-rw-r--r--   0 root         (0) root         (0)     4435 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/rcs_call_1_0/models.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/resident_1_0/
+-rw-r--r--   0 root         (0) root         (0)       22 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/resident_1_0/__init__.py
+-rw-r--r--   0 root         (0) root         (0)   118728 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/resident_1_0/client.py
+-rw-r--r--   0 root         (0) root         (0)   171405 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/resident_1_0/models.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/robot_1_0/
+-rw-r--r--   0 root         (0) root         (0)       22 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/robot_1_0/__init__.py
+-rw-r--r--   0 root         (0) root         (0)    71838 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/robot_1_0/client.py
+-rw-r--r--   0 root         (0) root         (0)    91606 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/robot_1_0/models.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/rooms_1_0/
+-rw-r--r--   0 root         (0) root         (0)       22 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/rooms_1_0/__init__.py
+-rw-r--r--   0 root         (0) root         (0)    50744 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/rooms_1_0/client.py
+-rw-r--r--   0 root         (0) root         (0)    82767 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/rooms_1_0/models.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/search_1_0/
+-rw-r--r--   0 root         (0) root         (0)       22 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/search_1_0/__init__.py
+-rw-r--r--   0 root         (0) root         (0)    35104 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/search_1_0/client.py
+-rw-r--r--   0 root         (0) root         (0)    47649 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/search_1_0/models.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/service_group_1_0/
+-rw-r--r--   0 root         (0) root         (0)       22 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/service_group_1_0/__init__.py
+-rw-r--r--   0 root         (0) root         (0)   322628 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/service_group_1_0/client.py
+-rw-r--r--   0 root         (0) root         (0)   499096 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/service_group_1_0/models.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/smart_device_1_0/
+-rw-r--r--   0 root         (0) root         (0)       22 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/smart_device_1_0/__init__.py
+-rw-r--r--   0 root         (0) root         (0)    28634 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/smart_device_1_0/client.py
+-rw-r--r--   0 root         (0) root         (0)    25101 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/smart_device_1_0/models.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/sns_storage_1_0/
+-rw-r--r--   0 root         (0) root         (0)       22 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/sns_storage_1_0/__init__.py
+-rw-r--r--   0 root         (0) root         (0)    40406 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/sns_storage_1_0/client.py
+-rw-r--r--   0 root         (0) root         (0)   105120 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/sns_storage_1_0/models.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/storage_1_0/
+-rw-r--r--   0 root         (0) root         (0)       22 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/storage_1_0/__init__.py
+-rw-r--r--   0 root         (0) root         (0)   173162 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/storage_1_0/client.py
+-rw-r--r--   0 root         (0) root         (0)   389740 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/storage_1_0/models.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/storage_2_0/
+-rw-r--r--   0 root         (0) root         (0)       22 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/storage_2_0/__init__.py
+-rw-r--r--   0 root         (0) root         (0)     9158 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/storage_2_0/client.py
+-rw-r--r--   0 root         (0) root         (0)    31448 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/storage_2_0/models.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/swform_1_0/
+-rw-r--r--   0 root         (0) root         (0)       22 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/swform_1_0/__init__.py
+-rw-r--r--   0 root         (0) root         (0)    12420 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/swform_1_0/client.py
+-rw-r--r--   0 root         (0) root         (0)    30097 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/swform_1_0/models.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/todo_1_0/
+-rw-r--r--   0 root         (0) root         (0)       22 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/todo_1_0/__init__.py
+-rw-r--r--   0 root         (0) root         (0)    60784 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/todo_1_0/client.py
+-rw-r--r--   0 root         (0) root         (0)   156671 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/todo_1_0/models.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/trade_1_0/
+-rw-r--r--   0 root         (0) root         (0)       22 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/trade_1_0/__init__.py
+-rw-r--r--   0 root         (0) root         (0)    12502 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/trade_1_0/client.py
+-rw-r--r--   0 root         (0) root         (0)    16057 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/trade_1_0/models.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/trajectory_1_0/
+-rw-r--r--   0 root         (0) root         (0)       22 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/trajectory_1_0/__init__.py
+-rw-r--r--   0 root         (0) root         (0)    12410 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/trajectory_1_0/client.py
+-rw-r--r--   0 root         (0) root         (0)    21548 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/trajectory_1_0/models.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/transcribe_1_0/
+-rw-r--r--   0 root         (0) root         (0)       22 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/transcribe_1_0/__init__.py
+-rw-r--r--   0 root         (0) root         (0)    12290 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/transcribe_1_0/client.py
+-rw-r--r--   0 root         (0) root         (0)    17800 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/transcribe_1_0/models.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/trip_1_0/
+-rw-r--r--   0 root         (0) root         (0)       22 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/trip_1_0/__init__.py
+-rw-r--r--   0 root         (0) root         (0)    16936 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/trip_1_0/client.py
+-rw-r--r--   0 root         (0) root         (0)    33576 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/trip_1_0/models.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/village_1_0/
+-rw-r--r--   0 root         (0) root         (0)       22 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/village_1_0/__init__.py
+-rw-r--r--   0 root         (0) root         (0)    68340 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/village_1_0/client.py
+-rw-r--r--   0 root         (0) root         (0)   110827 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/village_1_0/models.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/watt_1_0/
+-rw-r--r--   0 root         (0) root         (0)       22 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/watt_1_0/__init__.py
+-rw-r--r--   0 root         (0) root         (0)     3452 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/watt_1_0/client.py
+-rw-r--r--   0 root         (0) root         (0)     3124 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/watt_1_0/models.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/wiki_1_0/
+-rw-r--r--   0 root         (0) root         (0)       22 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/wiki_1_0/__init__.py
+-rw-r--r--   0 root         (0) root         (0)     7006 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/wiki_1_0/client.py
+-rw-r--r--   0 root         (0) root         (0)    20769 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/wiki_1_0/models.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/wms_1_0/
+-rw-r--r--   0 root         (0) root         (0)       22 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/wms_1_0/__init__.py
+-rw-r--r--   0 root         (0) root         (0)     4608 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/wms_1_0/client.py
+-rw-r--r--   0 root         (0) root         (0)     8329 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/wms_1_0/models.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/workbench_1_0/
+-rw-r--r--   0 root         (0) root         (0)       22 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/workbench_1_0/__init__.py
+-rw-r--r--   0 root         (0) root         (0)    24540 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/workbench_1_0/client.py
+-rw-r--r--   0 root         (0) root         (0)    28057 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/workbench_1_0/models.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/workflow_1_0/
+-rw-r--r--   0 root         (0) root         (0)       22 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/workflow_1_0/__init__.py
+-rw-r--r--   0 root         (0) root         (0)   154430 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/workflow_1_0/client.py
+-rw-r--r--   0 root         (0) root         (0)   385214 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/workflow_1_0/models.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/workrecord_1_0/
+-rw-r--r--   0 root         (0) root         (0)       22 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/workrecord_1_0/__init__.py
+-rw-r--r--   0 root         (0) root         (0)     4012 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/workrecord_1_0/client.py
+-rw-r--r--   0 root         (0) root         (0)     3485 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/workrecord_1_0/models.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/yida_1_0/
+-rw-r--r--   0 root         (0) root         (0)       22 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/yida_1_0/__init__.py
+-rw-r--r--   0 root         (0) root         (0)   416280 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/yida_1_0/client.py
+-rw-r--r--   0 root         (0) root         (0)   690137 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/yida_1_0/models.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk.egg-info/
+-rw-r--r--   0 root         (0) root         (0)     2309 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk.egg-info/PKG-INFO
+-rw-r--r--   0 root         (0) root         (0)    11356 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk.egg-info/SOURCES.txt
+-rw-r--r--   0 root         (0) root         (0)        1 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk.egg-info/dependency_links.txt
+-rw-r--r--   0 root         (0) root         (0)      156 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk.egg-info/requires.txt
+-rw-r--r--   0 root         (0) root         (0)       22 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk.egg-info/top_level.txt
+-rw-r--r--   0 root         (0) root         (0)       73 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/setup.cfg
+-rw-r--r--   0 root         (0) root         (0)     2585 2023-04-07 09:21:49.000000 alibabacloud_dingtalk-1.5.62/setup.py
```

### Comparing `alibabacloud_dingtalk-1.5.61/ChangeLog.md` & `alibabacloud_dingtalk-1.5.62/ChangeLog.md`

 * *Files 0% similar despite different names*

```diff
@@ -1,7 +1,10 @@
+2023-04-04 Version: 1.5.61
+- Update AddOfficialAccountFollower.
+
 2023-03-27 Version: 1.5.59
 - Update AddOfficialAccountFollower.
 
 2023-03-21 Version: 1.5.58
 - Update AddOfficialAccountFollower.
 
 2023-03-15 Version: 1.5.55
```

### Comparing `alibabacloud_dingtalk-1.5.61/LICENSE` & `alibabacloud_dingtalk-1.5.62/LICENSE`

 * *Files identical despite different names*

### Comparing `alibabacloud_dingtalk-1.5.61/PKG-INFO` & `alibabacloud_dingtalk-1.5.62/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: alibabacloud_dingtalk
-Version: 1.5.61
+Version: 1.5.62
 Summary: Alibaba Cloud Dingtalk SDK Library for Python
 Home-page: https://github.com/aliyun/alibabacloud-sdk
 Author: Alibaba Cloud SDK
 Author-email: sdk-team@alibabacloud.com
 License: Apache License 2.0
 Description: English | [简体中文](README-CN.md)
         ![](https://aliyunsdk-pages.alicdn.com/icons/AlibabaCloud.svg)
```

### Comparing `alibabacloud_dingtalk-1.5.61/README-CN.md` & `alibabacloud_dingtalk-1.5.62/README-CN.md`

 * *Files identical despite different names*

### Comparing `alibabacloud_dingtalk-1.5.61/README.md` & `alibabacloud_dingtalk-1.5.62/README.md`

 * *Files identical despite different names*

### Comparing `alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/algo_1_0/client.py` & `alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/algo_1_0/client.py`

 * *Files identical despite different names*

### Comparing `alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/algo_1_0/models.py` & `alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/algo_1_0/models.py`

 * *Files identical despite different names*

### Comparing `alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/alitrip_1_0/client.py` & `alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/alitrip_1_0/client.py`

 * *Files identical despite different names*

### Comparing `alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/alitrip_1_0/models.py` & `alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/alitrip_1_0/models.py`

 * *Files identical despite different names*

### Comparing `alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/apaas_1_0/client.py` & `alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/apaas_1_0/client.py`

 * *Files identical despite different names*

### Comparing `alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/apaas_1_0/models.py` & `alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/apaas_1_0/models.py`

 * *Files identical despite different names*

### Comparing `alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/app_market_1_0/client.py` & `alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/app_market_1_0/client.py`

 * *Files identical despite different names*

### Comparing `alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/app_market_1_0/models.py` & `alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/app_market_1_0/models.py`

 * *Files identical despite different names*

### Comparing `alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/ats_1_0/client.py` & `alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/ats_1_0/client.py`

 * *Files identical despite different names*

### Comparing `alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/ats_1_0/models.py` & `alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/ats_1_0/models.py`

 * *Files identical despite different names*

### Comparing `alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/attendance_1_0/client.py` & `alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/attendance_1_0/client.py`

 * *Files identical despite different names*

### Comparing `alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/attendance_1_0/models.py` & `alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/attendance_1_0/models.py`

 * *Files 1% similar despite different names*

```diff
@@ -5509,35 +5509,44 @@
             self.on_off_check_gap_minutes = m.get('onOffCheckGapMinutes')
         return self
 
 
 class GroupAddRequestFreeCheckSetting(TeaModel):
     def __init__(
         self,
+        delimit_offset_minutes_between_days: int = None,
         free_check_gap: GroupAddRequestFreeCheckSettingFreeCheckGap = None,
     ):
+        # 自由工时考勤组考勤开始时间与当天0点偏移分钟数。
+        # 
+        # 例如：540表示9:00
+        self.delimit_offset_minutes_between_days = delimit_offset_minutes_between_days
         # 休息日打卡间隔设置。
         self.free_check_gap = free_check_gap
 
     def validate(self):
         if self.free_check_gap:
             self.free_check_gap.validate()
 
     def to_map(self):
         _map = super().to_map()
         if _map is not None:
             return _map
 
         result = dict()
+        if self.delimit_offset_minutes_between_days is not None:
+            result['delimitOffsetMinutesBetweenDays'] = self.delimit_offset_minutes_between_days
         if self.free_check_gap is not None:
             result['freeCheckGap'] = self.free_check_gap.to_map()
         return result
 
     def from_map(self, m: dict = None):
         m = m or dict()
+        if m.get('delimitOffsetMinutesBetweenDays') is not None:
+            self.delimit_offset_minutes_between_days = m.get('delimitOffsetMinutesBetweenDays')
         if m.get('freeCheckGap') is not None:
             temp_model = GroupAddRequestFreeCheckSettingFreeCheckGap()
             self.free_check_gap = temp_model.from_map(m['freeCheckGap'])
         return self
 
 
 class GroupAddRequestMembers(TeaModel):
@@ -6207,79 +6216,76 @@
             self.op_user_id = m.get('opUserId')
         return self
 
 
 class GroupAddResponseBodyResult(TeaModel):
     def __init__(
         self,
-        group_id: int = None,
-        group_name: str = None,
+        id: int = None,
+        name: str = None,
     ):
-        # 考勤组id
-        self.group_id = group_id
-        # 考勤组名
-        self.group_name = group_name
+        self.id = id
+        self.name = name
 
     def validate(self):
         pass
 
     def to_map(self):
         _map = super().to_map()
         if _map is not None:
             return _map
 
         result = dict()
-        if self.group_id is not None:
-            result['groupId'] = self.group_id
-        if self.group_name is not None:
-            result['groupName'] = self.group_name
+        if self.id is not None:
+            result['id'] = self.id
+        if self.name is not None:
+            result['name'] = self.name
         return result
 
     def from_map(self, m: dict = None):
         m = m or dict()
-        if m.get('groupId') is not None:
-            self.group_id = m.get('groupId')
-        if m.get('groupName') is not None:
-            self.group_name = m.get('groupName')
+        if m.get('id') is not None:
+            self.id = m.get('id')
+        if m.get('name') is not None:
+            self.name = m.get('name')
         return self
 
 
 class GroupAddResponseBody(TeaModel):
     def __init__(
         self,
-        result: List[GroupAddResponseBodyResult] = None,
+        result: GroupAddResponseBodyResult = None,
+        success: bool = None,
     ):
-        # Id of the request
         self.result = result
+        self.success = success
 
     def validate(self):
         if self.result:
-            for k in self.result:
-                if k:
-                    k.validate()
+            self.result.validate()
 
     def to_map(self):
         _map = super().to_map()
         if _map is not None:
             return _map
 
         result = dict()
-        result['result'] = []
         if self.result is not None:
-            for k in self.result:
-                result['result'].append(k.to_map() if k else None)
+            result['result'] = self.result.to_map()
+        if self.success is not None:
+            result['success'] = self.success
         return result
 
     def from_map(self, m: dict = None):
         m = m or dict()
-        self.result = []
         if m.get('result') is not None:
-            for k in m.get('result'):
-                temp_model = GroupAddResponseBodyResult()
-                self.result.append(temp_model.from_map(k))
+            temp_model = GroupAddResponseBodyResult()
+            self.result = temp_model.from_map(m['result'])
+        if m.get('success') is not None:
+            self.success = m.get('success')
         return self
 
 
 class GroupAddResponse(TeaModel):
     def __init__(
         self,
         headers: Dict[str, str] = None,
@@ -6383,35 +6389,44 @@
             self.on_off_check_gap_minutes = m.get('onOffCheckGapMinutes')
         return self
 
 
 class GroupUpdateRequestFreeCheckSetting(TeaModel):
     def __init__(
         self,
+        delimit_offset_minutes_between_days: int = None,
         free_check_gap: GroupUpdateRequestFreeCheckSettingFreeCheckGap = None,
     ):
+        # 自由工时考勤组考勤开始时间与当天0点偏移分钟数。
+        # 
+        # 例如：540表示9:00
+        self.delimit_offset_minutes_between_days = delimit_offset_minutes_between_days
         # 休息日打卡间隔设置。
         self.free_check_gap = free_check_gap
 
     def validate(self):
         if self.free_check_gap:
             self.free_check_gap.validate()
 
     def to_map(self):
         _map = super().to_map()
         if _map is not None:
             return _map
 
         result = dict()
+        if self.delimit_offset_minutes_between_days is not None:
+            result['delimitOffsetMinutesBetweenDays'] = self.delimit_offset_minutes_between_days
         if self.free_check_gap is not None:
             result['freeCheckGap'] = self.free_check_gap.to_map()
         return result
 
     def from_map(self, m: dict = None):
         m = m or dict()
+        if m.get('delimitOffsetMinutesBetweenDays') is not None:
+            self.delimit_offset_minutes_between_days = m.get('delimitOffsetMinutesBetweenDays')
         if m.get('freeCheckGap') is not None:
             temp_model = GroupUpdateRequestFreeCheckSettingFreeCheckGap()
             self.free_check_gap = temp_model.from_map(m['freeCheckGap'])
         return self
 
 
 class GroupUpdateRequestPositions(TeaModel):
@@ -6834,79 +6849,76 @@
             self.op_user_id = m.get('opUserId')
         return self
 
 
 class GroupUpdateResponseBodyResult(TeaModel):
     def __init__(
         self,
-        group_id: int = None,
-        group_name: str = None,
+        id: int = None,
+        name: str = None,
     ):
-        # 考勤组id
-        self.group_id = group_id
-        # 考勤组名
-        self.group_name = group_name
+        self.id = id
+        self.name = name
 
     def validate(self):
         pass
 
     def to_map(self):
         _map = super().to_map()
         if _map is not None:
             return _map
 
         result = dict()
-        if self.group_id is not None:
-            result['groupId'] = self.group_id
-        if self.group_name is not None:
-            result['groupName'] = self.group_name
+        if self.id is not None:
+            result['id'] = self.id
+        if self.name is not None:
+            result['name'] = self.name
         return result
 
     def from_map(self, m: dict = None):
         m = m or dict()
-        if m.get('groupId') is not None:
-            self.group_id = m.get('groupId')
-        if m.get('groupName') is not None:
-            self.group_name = m.get('groupName')
+        if m.get('id') is not None:
+            self.id = m.get('id')
+        if m.get('name') is not None:
+            self.name = m.get('name')
         return self
 
 
 class GroupUpdateResponseBody(TeaModel):
     def __init__(
         self,
-        result: List[GroupUpdateResponseBodyResult] = None,
+        result: GroupUpdateResponseBodyResult = None,
+        success: bool = None,
     ):
-        # Id of the request
         self.result = result
+        self.success = success
 
     def validate(self):
         if self.result:
-            for k in self.result:
-                if k:
-                    k.validate()
+            self.result.validate()
 
     def to_map(self):
         _map = super().to_map()
         if _map is not None:
             return _map
 
         result = dict()
-        result['result'] = []
         if self.result is not None:
-            for k in self.result:
-                result['result'].append(k.to_map() if k else None)
+            result['result'] = self.result.to_map()
+        if self.success is not None:
+            result['success'] = self.success
         return result
 
     def from_map(self, m: dict = None):
         m = m or dict()
-        self.result = []
         if m.get('result') is not None:
-            for k in m.get('result'):
-                temp_model = GroupUpdateResponseBodyResult()
-                self.result.append(temp_model.from_map(k))
+            temp_model = GroupUpdateResponseBodyResult()
+            self.result = temp_model.from_map(m['result'])
+        if m.get('success') is not None:
+            self.success = m.get('success')
         return self
 
 
 class GroupUpdateResponse(TeaModel):
     def __init__(
         self,
         headers: Dict[str, str] = None,
```

### Comparing `alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/badge_1_0/client.py` & `alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/badge_1_0/client.py`

 * *Files identical despite different names*

### Comparing `alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/badge_1_0/models.py` & `alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/badge_1_0/models.py`

 * *Files identical despite different names*

### Comparing `alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/bizfinance_1_0/client.py` & `alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/bizfinance_1_0/client.py`

 * *Files 1% similar despite different names*

```diff
@@ -279,14 +279,18 @@
     ) -> dingtalkbizfinance__1__0_models.CreateCustomerResponse:
         UtilClient.validate_model(request)
         body = {}
         if not UtilClient.is_unset(request.creator):
             body['creator'] = request.creator
         if not UtilClient.is_unset(request.description):
             body['description'] = request.description
+        if not UtilClient.is_unset(request.drawer_email):
+            body['drawerEmail'] = request.drawer_email
+        if not UtilClient.is_unset(request.drawer_telephone):
+            body['drawerTelephone'] = request.drawer_telephone
         if not UtilClient.is_unset(request.name):
             body['name'] = request.name
         if not UtilClient.is_unset(request.purchaser_account):
             body['purchaserAccount'] = request.purchaser_account
         if not UtilClient.is_unset(request.purchaser_address):
             body['purchaserAddress'] = request.purchaser_address
         if not UtilClient.is_unset(request.purchaser_bank_name):
@@ -319,14 +323,18 @@
     ) -> dingtalkbizfinance__1__0_models.CreateCustomerResponse:
         UtilClient.validate_model(request)
         body = {}
         if not UtilClient.is_unset(request.creator):
             body['creator'] = request.creator
         if not UtilClient.is_unset(request.description):
             body['description'] = request.description
+        if not UtilClient.is_unset(request.drawer_email):
+            body['drawerEmail'] = request.drawer_email
+        if not UtilClient.is_unset(request.drawer_telephone):
+            body['drawerTelephone'] = request.drawer_telephone
         if not UtilClient.is_unset(request.name):
             body['name'] = request.name
         if not UtilClient.is_unset(request.purchaser_account):
             body['purchaserAccount'] = request.purchaser_account
         if not UtilClient.is_unset(request.purchaser_address):
             body['purchaserAddress'] = request.purchaser_address
         if not UtilClient.is_unset(request.purchaser_bank_name):
@@ -1799,14 +1807,78 @@
             query=OpenApiUtilClient.query(query)
         )
         return TeaCore.from_map(
             dingtalkbizfinance__1__0_models.QueryProjectByPageResponse(),
             await self.do_roarequest_async('QueryProjectByPage', 'bizfinance_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/bizfinance/projects/list', 'json', req, runtime)
         )
 
+    def query_receipt_detail_for_invoice(
+        self,
+        request: dingtalkbizfinance__1__0_models.QueryReceiptDetailForInvoiceRequest,
+    ) -> dingtalkbizfinance__1__0_models.QueryReceiptDetailForInvoiceResponse:
+        runtime = util_models.RuntimeOptions()
+        headers = dingtalkbizfinance__1__0_models.QueryReceiptDetailForInvoiceHeaders()
+        return self.query_receipt_detail_for_invoice_with_options(request, headers, runtime)
+
+    async def query_receipt_detail_for_invoice_async(
+        self,
+        request: dingtalkbizfinance__1__0_models.QueryReceiptDetailForInvoiceRequest,
+    ) -> dingtalkbizfinance__1__0_models.QueryReceiptDetailForInvoiceResponse:
+        runtime = util_models.RuntimeOptions()
+        headers = dingtalkbizfinance__1__0_models.QueryReceiptDetailForInvoiceHeaders()
+        return await self.query_receipt_detail_for_invoice_with_options_async(request, headers, runtime)
+
+    def query_receipt_detail_for_invoice_with_options(
+        self,
+        request: dingtalkbizfinance__1__0_models.QueryReceiptDetailForInvoiceRequest,
+        headers: dingtalkbizfinance__1__0_models.QueryReceiptDetailForInvoiceHeaders,
+        runtime: util_models.RuntimeOptions,
+    ) -> dingtalkbizfinance__1__0_models.QueryReceiptDetailForInvoiceResponse:
+        UtilClient.validate_model(request)
+        query = {}
+        if not UtilClient.is_unset(request.instance_id):
+            query['instanceId'] = request.instance_id
+        real_headers = {}
+        if not UtilClient.is_unset(headers.common_headers):
+            real_headers = headers.common_headers
+        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
+            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
+        req = open_api_models.OpenApiRequest(
+            headers=real_headers,
+            query=OpenApiUtilClient.query(query)
+        )
+        return TeaCore.from_map(
+            dingtalkbizfinance__1__0_models.QueryReceiptDetailForInvoiceResponse(),
+            self.do_roarequest('QueryReceiptDetailForInvoice', 'bizfinance_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/bizfinance/invoices/receipts/details', 'json', req, runtime)
+        )
+
+    async def query_receipt_detail_for_invoice_with_options_async(
+        self,
+        request: dingtalkbizfinance__1__0_models.QueryReceiptDetailForInvoiceRequest,
+        headers: dingtalkbizfinance__1__0_models.QueryReceiptDetailForInvoiceHeaders,
+        runtime: util_models.RuntimeOptions,
+    ) -> dingtalkbizfinance__1__0_models.QueryReceiptDetailForInvoiceResponse:
+        UtilClient.validate_model(request)
+        query = {}
+        if not UtilClient.is_unset(request.instance_id):
+            query['instanceId'] = request.instance_id
+        real_headers = {}
+        if not UtilClient.is_unset(headers.common_headers):
+            real_headers = headers.common_headers
+        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
+            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
+        req = open_api_models.OpenApiRequest(
+            headers=real_headers,
+            query=OpenApiUtilClient.query(query)
+        )
+        return TeaCore.from_map(
+            dingtalkbizfinance__1__0_models.QueryReceiptDetailForInvoiceResponse(),
+            await self.do_roarequest_async('QueryReceiptDetailForInvoice', 'bizfinance_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/bizfinance/invoices/receipts/details', 'json', req, runtime)
+        )
+
     def query_receipt_for_invoice(
         self,
         request: dingtalkbizfinance__1__0_models.QueryReceiptForInvoiceRequest,
     ) -> dingtalkbizfinance__1__0_models.QueryReceiptForInvoiceResponse:
         runtime = util_models.RuntimeOptions()
         headers = dingtalkbizfinance__1__0_models.QueryReceiptForInvoiceHeaders()
         return self.query_receipt_for_invoice_with_options(request, headers, runtime)
```

### Comparing `alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/bizfinance_1_0/models.py` & `alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/bizfinance_1_0/models.py`

 * *Files 0% similar despite different names*

```diff
@@ -1060,24 +1060,30 @@
         return self
 
 
 class BatchCreateCustomerRequestCreateCustomerRequestList(TeaModel):
     def __init__(
         self,
         description: str = None,
+        drawer_email: str = None,
+        drawer_telephone: str = None,
         name: str = None,
         purchaser_account: str = None,
         purchaser_address: str = None,
         purchaser_bank_name: str = None,
         purchaser_name: str = None,
         purchaser_tax_no: str = None,
         purchaser_tel: str = None,
     ):
         # 客户描述
         self.description = description
+        # 开票人邮箱
+        self.drawer_email = drawer_email
+        # 开票人手机号
+        self.drawer_telephone = drawer_telephone
         # 客户名字
         self.name = name
         # 购方账户
         self.purchaser_account = purchaser_account
         # 购房地址
         self.purchaser_address = purchaser_address
         # 购方银行
@@ -1096,14 +1102,18 @@
         _map = super().to_map()
         if _map is not None:
             return _map
 
         result = dict()
         if self.description is not None:
             result['description'] = self.description
+        if self.drawer_email is not None:
+            result['drawerEmail'] = self.drawer_email
+        if self.drawer_telephone is not None:
+            result['drawerTelephone'] = self.drawer_telephone
         if self.name is not None:
             result['name'] = self.name
         if self.purchaser_account is not None:
             result['purchaserAccount'] = self.purchaser_account
         if self.purchaser_address is not None:
             result['purchaserAddress'] = self.purchaser_address
         if self.purchaser_bank_name is not None:
@@ -1116,14 +1126,18 @@
             result['purchaserTel'] = self.purchaser_tel
         return result
 
     def from_map(self, m: dict = None):
         m = m or dict()
         if m.get('description') is not None:
             self.description = m.get('description')
+        if m.get('drawerEmail') is not None:
+            self.drawer_email = m.get('drawerEmail')
+        if m.get('drawerTelephone') is not None:
+            self.drawer_telephone = m.get('drawerTelephone')
         if m.get('name') is not None:
             self.name = m.get('name')
         if m.get('purchaserAccount') is not None:
             self.purchaser_account = m.get('purchaserAccount')
         if m.get('purchaserAddress') is not None:
             self.purchaser_address = m.get('purchaserAddress')
         if m.get('purchaserBankName') is not None:
@@ -1511,26 +1525,32 @@
 
 
 class CreateCustomerRequest(TeaModel):
     def __init__(
         self,
         creator: str = None,
         description: str = None,
+        drawer_email: str = None,
+        drawer_telephone: str = None,
         name: str = None,
         purchaser_account: str = None,
         purchaser_address: str = None,
         purchaser_bank_name: str = None,
         purchaser_name: str = None,
         purchaser_tax_no: str = None,
         purchaser_tel: str = None,
     ):
         # 创建人userId
         self.creator = creator
         # 客户描述
         self.description = description
+        # 开票人邮箱
+        self.drawer_email = drawer_email
+        # 开票人手机号
+        self.drawer_telephone = drawer_telephone
         # 客户名字
         self.name = name
         # 购方账户
         self.purchaser_account = purchaser_account
         # 购房地址
         self.purchaser_address = purchaser_address
         # 购方银行
@@ -1551,14 +1571,18 @@
             return _map
 
         result = dict()
         if self.creator is not None:
             result['creator'] = self.creator
         if self.description is not None:
             result['description'] = self.description
+        if self.drawer_email is not None:
+            result['drawerEmail'] = self.drawer_email
+        if self.drawer_telephone is not None:
+            result['drawerTelephone'] = self.drawer_telephone
         if self.name is not None:
             result['name'] = self.name
         if self.purchaser_account is not None:
             result['purchaserAccount'] = self.purchaser_account
         if self.purchaser_address is not None:
             result['purchaserAddress'] = self.purchaser_address
         if self.purchaser_bank_name is not None:
@@ -1573,14 +1597,18 @@
 
     def from_map(self, m: dict = None):
         m = m or dict()
         if m.get('creator') is not None:
             self.creator = m.get('creator')
         if m.get('description') is not None:
             self.description = m.get('description')
+        if m.get('drawerEmail') is not None:
+            self.drawer_email = m.get('drawerEmail')
+        if m.get('drawerTelephone') is not None:
+            self.drawer_telephone = m.get('drawerTelephone')
         if m.get('name') is not None:
             self.name = m.get('name')
         if m.get('purchaserAccount') is not None:
             self.purchaser_account = m.get('purchaserAccount')
         if m.get('purchaserAddress') is not None:
             self.purchaser_address = m.get('purchaserAddress')
         if m.get('purchaserBankName') is not None:
@@ -5302,14 +5330,16 @@
         code: str = None,
         contact_address: str = None,
         contact_company_telephone: str = None,
         contact_email: str = None,
         contact_name: str = None,
         contact_telephone: str = None,
         description: str = None,
+        drawer_email: str = None,
+        drawer_telephone: str = None,
         name: str = None,
         purchaser_account: str = None,
         purchaser_address: str = None,
         purchaser_name: str = None,
         purchaser_tax_no: str = None,
         purchaser_tel: str = None,
         purchaserr_bank_name: str = None,
@@ -5321,14 +5351,18 @@
         self.contact_address = contact_address
         self.contact_company_telephone = contact_company_telephone
         self.contact_email = contact_email
         self.contact_name = contact_name
         self.contact_telephone = contact_telephone
         # 客户描述
         self.description = description
+        # 开票人邮箱
+        self.drawer_email = drawer_email
+        # 开票人手机号
+        self.drawer_telephone = drawer_telephone
         # 客户名字
         self.name = name
         # 购方账户
         self.purchaser_account = purchaser_account
         # 购方地址
         self.purchaser_address = purchaser_address
         # 购方姓名
@@ -5363,14 +5397,18 @@
             result['contactEmail'] = self.contact_email
         if self.contact_name is not None:
             result['contactName'] = self.contact_name
         if self.contact_telephone is not None:
             result['contactTelephone'] = self.contact_telephone
         if self.description is not None:
             result['description'] = self.description
+        if self.drawer_email is not None:
+            result['drawerEmail'] = self.drawer_email
+        if self.drawer_telephone is not None:
+            result['drawerTelephone'] = self.drawer_telephone
         if self.name is not None:
             result['name'] = self.name
         if self.purchaser_account is not None:
             result['purchaserAccount'] = self.purchaser_account
         if self.purchaser_address is not None:
             result['purchaserAddress'] = self.purchaser_address
         if self.purchaser_name is not None:
@@ -5399,14 +5437,18 @@
             self.contact_email = m.get('contactEmail')
         if m.get('contactName') is not None:
             self.contact_name = m.get('contactName')
         if m.get('contactTelephone') is not None:
             self.contact_telephone = m.get('contactTelephone')
         if m.get('description') is not None:
             self.description = m.get('description')
+        if m.get('drawerEmail') is not None:
+            self.drawer_email = m.get('drawerEmail')
+        if m.get('drawerTelephone') is not None:
+            self.drawer_telephone = m.get('drawerTelephone')
         if m.get('name') is not None:
             self.name = m.get('name')
         if m.get('purchaserAccount') is not None:
             self.purchaser_account = m.get('purchaserAccount')
         if m.get('purchaserAddress') is not None:
             self.purchaser_address = m.get('purchaserAddress')
         if m.get('purchaserName') is not None:
@@ -6800,14 +6842,478 @@
             self.headers = m.get('headers')
         if m.get('body') is not None:
             temp_model = QueryProjectByPageResponseBody()
             self.body = temp_model.from_map(m['body'])
         return self
 
 
+class QueryReceiptDetailForInvoiceHeaders(TeaModel):
+    def __init__(
+        self,
+        common_headers: Dict[str, str] = None,
+        x_acs_dingtalk_access_token: str = None,
+    ):
+        self.common_headers = common_headers
+        self.x_acs_dingtalk_access_token = x_acs_dingtalk_access_token
+
+    def validate(self):
+        pass
+
+    def to_map(self):
+        _map = super().to_map()
+        if _map is not None:
+            return _map
+
+        result = dict()
+        if self.common_headers is not None:
+            result['commonHeaders'] = self.common_headers
+        if self.x_acs_dingtalk_access_token is not None:
+            result['x-acs-dingtalk-access-token'] = self.x_acs_dingtalk_access_token
+        return result
+
+    def from_map(self, m: dict = None):
+        m = m or dict()
+        if m.get('commonHeaders') is not None:
+            self.common_headers = m.get('commonHeaders')
+        if m.get('x-acs-dingtalk-access-token') is not None:
+            self.x_acs_dingtalk_access_token = m.get('x-acs-dingtalk-access-token')
+        return self
+
+
+class QueryReceiptDetailForInvoiceRequest(TeaModel):
+    def __init__(
+        self,
+        instance_id: str = None,
+    ):
+        # 审批单id
+        self.instance_id = instance_id
+
+    def validate(self):
+        pass
+
+    def to_map(self):
+        _map = super().to_map()
+        if _map is not None:
+            return _map
+
+        result = dict()
+        if self.instance_id is not None:
+            result['instanceId'] = self.instance_id
+        return result
+
+    def from_map(self, m: dict = None):
+        m = m or dict()
+        if m.get('instanceId') is not None:
+            self.instance_id = m.get('instanceId')
+        return self
+
+
+class QueryReceiptDetailForInvoiceResponseBodyResultCreator(TeaModel):
+    def __init__(
+        self,
+        avatar_url: str = None,
+        nick: str = None,
+        user_id: str = None,
+    ):
+        # 创建人头像
+        self.avatar_url = avatar_url
+        # 创建人昵称
+        self.nick = nick
+        # 创建人工号
+        self.user_id = user_id
+
+    def validate(self):
+        pass
+
+    def to_map(self):
+        _map = super().to_map()
+        if _map is not None:
+            return _map
+
+        result = dict()
+        if self.avatar_url is not None:
+            result['avatarUrl'] = self.avatar_url
+        if self.nick is not None:
+            result['nick'] = self.nick
+        if self.user_id is not None:
+            result['userId'] = self.user_id
+        return result
+
+    def from_map(self, m: dict = None):
+        m = m or dict()
+        if m.get('avatarUrl') is not None:
+            self.avatar_url = m.get('avatarUrl')
+        if m.get('nick') is not None:
+            self.nick = m.get('nick')
+        if m.get('userId') is not None:
+            self.user_id = m.get('userId')
+        return self
+
+
+class QueryReceiptDetailForInvoiceResponseBodyResultCustomer(TeaModel):
+    def __init__(
+        self,
+        code: str = None,
+        name: str = None,
+    ):
+        # 客户code
+        self.code = code
+        # 客户名字
+        self.name = name
+
+    def validate(self):
+        pass
+
+    def to_map(self):
+        _map = super().to_map()
+        if _map is not None:
+            return _map
+
+        result = dict()
+        if self.code is not None:
+            result['code'] = self.code
+        if self.name is not None:
+            result['name'] = self.name
+        return result
+
+    def from_map(self, m: dict = None):
+        m = m or dict()
+        if m.get('code') is not None:
+            self.code = m.get('code')
+        if m.get('name') is not None:
+            self.name = m.get('name')
+        return self
+
+
+class QueryReceiptDetailForInvoiceResponseBodyResultProductInfoList(TeaModel):
+    def __init__(
+        self,
+        amount_with_tax: str = None,
+        name: str = None,
+        quantity: str = None,
+        specification: str = None,
+        tax_rate: str = None,
+        unit: str = None,
+        unit_price_with_tax: str = None,
+    ):
+        # 含税金额
+        self.amount_with_tax = amount_with_tax
+        # 商品名称
+        self.name = name
+        # 数量
+        self.quantity = quantity
+        # 规格型号
+        self.specification = specification
+        # 税率
+        self.tax_rate = tax_rate
+        # 计量单位
+        self.unit = unit
+        # 含税单价
+        self.unit_price_with_tax = unit_price_with_tax
+
+    def validate(self):
+        pass
+
+    def to_map(self):
+        _map = super().to_map()
+        if _map is not None:
+            return _map
+
+        result = dict()
+        if self.amount_with_tax is not None:
+            result['amountWithTax'] = self.amount_with_tax
+        if self.name is not None:
+            result['name'] = self.name
+        if self.quantity is not None:
+            result['quantity'] = self.quantity
+        if self.specification is not None:
+            result['specification'] = self.specification
+        if self.tax_rate is not None:
+            result['taxRate'] = self.tax_rate
+        if self.unit is not None:
+            result['unit'] = self.unit
+        if self.unit_price_with_tax is not None:
+            result['unitPriceWithTax'] = self.unit_price_with_tax
+        return result
+
+    def from_map(self, m: dict = None):
+        m = m or dict()
+        if m.get('amountWithTax') is not None:
+            self.amount_with_tax = m.get('amountWithTax')
+        if m.get('name') is not None:
+            self.name = m.get('name')
+        if m.get('quantity') is not None:
+            self.quantity = m.get('quantity')
+        if m.get('specification') is not None:
+            self.specification = m.get('specification')
+        if m.get('taxRate') is not None:
+            self.tax_rate = m.get('taxRate')
+        if m.get('unit') is not None:
+            self.unit = m.get('unit')
+        if m.get('unitPriceWithTax') is not None:
+            self.unit_price_with_tax = m.get('unitPriceWithTax')
+        return self
+
+
+class QueryReceiptDetailForInvoiceResponseBodyResult(TeaModel):
+    def __init__(
+        self,
+        amount: str = None,
+        apply_status: str = None,
+        create_time: str = None,
+        creator: QueryReceiptDetailForInvoiceResponseBodyResultCreator = None,
+        customer: QueryReceiptDetailForInvoiceResponseBodyResultCustomer = None,
+        drawer_email: str = None,
+        drawer_telephone: str = None,
+        invoice_type: str = None,
+        model_id: str = None,
+        product_info_list: List[QueryReceiptDetailForInvoiceResponseBodyResultProductInfoList] = None,
+        purchaser_account: str = None,
+        purchaser_address: str = None,
+        purchaser_bank_name: str = None,
+        purchaser_name: str = None,
+        purchaser_tax_no: str = None,
+        purchaser_tel: str = None,
+        receipt_id: str = None,
+        record_time: str = None,
+        remark: str = None,
+        source: str = None,
+        status: str = None,
+        title: str = None,
+    ):
+        # 金额
+        self.amount = amount
+        # 开票状态
+        self.apply_status = apply_status
+        # 创建时间
+        self.create_time = create_time
+        # 创建人
+        self.creator = creator
+        # 客户
+        self.customer = customer
+        # 开票人邮箱
+        self.drawer_email = drawer_email
+        # 开票人手机号码
+        self.drawer_telephone = drawer_telephone
+        # 发票种类
+        self.invoice_type = invoice_type
+        # 主数据modelId
+        self.model_id = model_id
+        # 商品列表
+        self.product_info_list = product_info_list
+        # 购方账户
+        self.purchaser_account = purchaser_account
+        # 购方地址
+        self.purchaser_address = purchaser_address
+        # 购方银行
+        self.purchaser_bank_name = purchaser_bank_name
+        # 购方抬头
+        self.purchaser_name = purchaser_name
+        # 购方税号
+        self.purchaser_tax_no = purchaser_tax_no
+        # 购方电话
+        self.purchaser_tel = purchaser_tel
+        # 单据ID
+        self.receipt_id = receipt_id
+        # 记录时间，默认为审批通过时间
+        self.record_time = record_time
+        # 备注
+        self.remark = remark
+        # 来源
+        self.source = source
+        # 状态 agree running
+        self.status = status
+        # 单据标题
+        self.title = title
+
+    def validate(self):
+        if self.creator:
+            self.creator.validate()
+        if self.customer:
+            self.customer.validate()
+        if self.product_info_list:
+            for k in self.product_info_list:
+                if k:
+                    k.validate()
+
+    def to_map(self):
+        _map = super().to_map()
+        if _map is not None:
+            return _map
+
+        result = dict()
+        if self.amount is not None:
+            result['amount'] = self.amount
+        if self.apply_status is not None:
+            result['applyStatus'] = self.apply_status
+        if self.create_time is not None:
+            result['createTime'] = self.create_time
+        if self.creator is not None:
+            result['creator'] = self.creator.to_map()
+        if self.customer is not None:
+            result['customer'] = self.customer.to_map()
+        if self.drawer_email is not None:
+            result['drawerEmail'] = self.drawer_email
+        if self.drawer_telephone is not None:
+            result['drawerTelephone'] = self.drawer_telephone
+        if self.invoice_type is not None:
+            result['invoiceType'] = self.invoice_type
+        if self.model_id is not None:
+            result['modelId'] = self.model_id
+        result['productInfoList'] = []
+        if self.product_info_list is not None:
+            for k in self.product_info_list:
+                result['productInfoList'].append(k.to_map() if k else None)
+        if self.purchaser_account is not None:
+            result['purchaserAccount'] = self.purchaser_account
+        if self.purchaser_address is not None:
+            result['purchaserAddress'] = self.purchaser_address
+        if self.purchaser_bank_name is not None:
+            result['purchaserBankName'] = self.purchaser_bank_name
+        if self.purchaser_name is not None:
+            result['purchaserName'] = self.purchaser_name
+        if self.purchaser_tax_no is not None:
+            result['purchaserTaxNo'] = self.purchaser_tax_no
+        if self.purchaser_tel is not None:
+            result['purchaserTel'] = self.purchaser_tel
+        if self.receipt_id is not None:
+            result['receiptId'] = self.receipt_id
+        if self.record_time is not None:
+            result['recordTime'] = self.record_time
+        if self.remark is not None:
+            result['remark'] = self.remark
+        if self.source is not None:
+            result['source'] = self.source
+        if self.status is not None:
+            result['status'] = self.status
+        if self.title is not None:
+            result['title'] = self.title
+        return result
+
+    def from_map(self, m: dict = None):
+        m = m or dict()
+        if m.get('amount') is not None:
+            self.amount = m.get('amount')
+        if m.get('applyStatus') is not None:
+            self.apply_status = m.get('applyStatus')
+        if m.get('createTime') is not None:
+            self.create_time = m.get('createTime')
+        if m.get('creator') is not None:
+            temp_model = QueryReceiptDetailForInvoiceResponseBodyResultCreator()
+            self.creator = temp_model.from_map(m['creator'])
+        if m.get('customer') is not None:
+            temp_model = QueryReceiptDetailForInvoiceResponseBodyResultCustomer()
+            self.customer = temp_model.from_map(m['customer'])
+        if m.get('drawerEmail') is not None:
+            self.drawer_email = m.get('drawerEmail')
+        if m.get('drawerTelephone') is not None:
+            self.drawer_telephone = m.get('drawerTelephone')
+        if m.get('invoiceType') is not None:
+            self.invoice_type = m.get('invoiceType')
+        if m.get('modelId') is not None:
+            self.model_id = m.get('modelId')
+        self.product_info_list = []
+        if m.get('productInfoList') is not None:
+            for k in m.get('productInfoList'):
+                temp_model = QueryReceiptDetailForInvoiceResponseBodyResultProductInfoList()
+                self.product_info_list.append(temp_model.from_map(k))
+        if m.get('purchaserAccount') is not None:
+            self.purchaser_account = m.get('purchaserAccount')
+        if m.get('purchaserAddress') is not None:
+            self.purchaser_address = m.get('purchaserAddress')
+        if m.get('purchaserBankName') is not None:
+            self.purchaser_bank_name = m.get('purchaserBankName')
+        if m.get('purchaserName') is not None:
+            self.purchaser_name = m.get('purchaserName')
+        if m.get('purchaserTaxNo') is not None:
+            self.purchaser_tax_no = m.get('purchaserTaxNo')
+        if m.get('purchaserTel') is not None:
+            self.purchaser_tel = m.get('purchaserTel')
+        if m.get('receiptId') is not None:
+            self.receipt_id = m.get('receiptId')
+        if m.get('recordTime') is not None:
+            self.record_time = m.get('recordTime')
+        if m.get('remark') is not None:
+            self.remark = m.get('remark')
+        if m.get('source') is not None:
+            self.source = m.get('source')
+        if m.get('status') is not None:
+            self.status = m.get('status')
+        if m.get('title') is not None:
+            self.title = m.get('title')
+        return self
+
+
+class QueryReceiptDetailForInvoiceResponseBody(TeaModel):
+    def __init__(
+        self,
+        result: QueryReceiptDetailForInvoiceResponseBodyResult = None,
+    ):
+        # 结果
+        self.result = result
+
+    def validate(self):
+        if self.result:
+            self.result.validate()
+
+    def to_map(self):
+        _map = super().to_map()
+        if _map is not None:
+            return _map
+
+        result = dict()
+        if self.result is not None:
+            result['result'] = self.result.to_map()
+        return result
+
+    def from_map(self, m: dict = None):
+        m = m or dict()
+        if m.get('result') is not None:
+            temp_model = QueryReceiptDetailForInvoiceResponseBodyResult()
+            self.result = temp_model.from_map(m['result'])
+        return self
+
+
+class QueryReceiptDetailForInvoiceResponse(TeaModel):
+    def __init__(
+        self,
+        headers: Dict[str, str] = None,
+        body: QueryReceiptDetailForInvoiceResponseBody = None,
+    ):
+        self.headers = headers
+        self.body = body
+
+    def validate(self):
+        self.validate_required(self.headers, 'headers')
+        self.validate_required(self.body, 'body')
+        if self.body:
+            self.body.validate()
+
+    def to_map(self):
+        _map = super().to_map()
+        if _map is not None:
+            return _map
+
+        result = dict()
+        if self.headers is not None:
+            result['headers'] = self.headers
+        if self.body is not None:
+            result['body'] = self.body.to_map()
+        return result
+
+    def from_map(self, m: dict = None):
+        m = m or dict()
+        if m.get('headers') is not None:
+            self.headers = m.get('headers')
+        if m.get('body') is not None:
+            temp_model = QueryReceiptDetailForInvoiceResponseBody()
+            self.body = temp_model.from_map(m['body'])
+        return self
+
+
 class QueryReceiptForInvoiceHeaders(TeaModel):
     def __init__(
         self,
         common_headers: Dict[str, str] = None,
         x_acs_dingtalk_access_token: str = None,
     ):
         self.common_headers = common_headers
@@ -6979,24 +7485,97 @@
         if m.get('code') is not None:
             self.code = m.get('code')
         if m.get('name') is not None:
             self.name = m.get('name')
         return self
 
 
+class QueryReceiptForInvoiceResponseBodyListProductInfoList(TeaModel):
+    def __init__(
+        self,
+        amount_with_tax: str = None,
+        name: str = None,
+        quantity: str = None,
+        specification: str = None,
+        tax_rate: str = None,
+        unit: str = None,
+        unit_price_with_tax: str = None,
+    ):
+        # 含税金额
+        self.amount_with_tax = amount_with_tax
+        # 商品名称
+        self.name = name
+        # 数量
+        self.quantity = quantity
+        # 规格型号
+        self.specification = specification
+        # 税率
+        self.tax_rate = tax_rate
+        # 计量单位
+        self.unit = unit
+        # 含税单价
+        self.unit_price_with_tax = unit_price_with_tax
+
+    def validate(self):
+        pass
+
+    def to_map(self):
+        _map = super().to_map()
+        if _map is not None:
+            return _map
+
+        result = dict()
+        if self.amount_with_tax is not None:
+            result['amountWithTax'] = self.amount_with_tax
+        if self.name is not None:
+            result['name'] = self.name
+        if self.quantity is not None:
+            result['quantity'] = self.quantity
+        if self.specification is not None:
+            result['specification'] = self.specification
+        if self.tax_rate is not None:
+            result['taxRate'] = self.tax_rate
+        if self.unit is not None:
+            result['unit'] = self.unit
+        if self.unit_price_with_tax is not None:
+            result['unitPriceWithTax'] = self.unit_price_with_tax
+        return result
+
+    def from_map(self, m: dict = None):
+        m = m or dict()
+        if m.get('amountWithTax') is not None:
+            self.amount_with_tax = m.get('amountWithTax')
+        if m.get('name') is not None:
+            self.name = m.get('name')
+        if m.get('quantity') is not None:
+            self.quantity = m.get('quantity')
+        if m.get('specification') is not None:
+            self.specification = m.get('specification')
+        if m.get('taxRate') is not None:
+            self.tax_rate = m.get('taxRate')
+        if m.get('unit') is not None:
+            self.unit = m.get('unit')
+        if m.get('unitPriceWithTax') is not None:
+            self.unit_price_with_tax = m.get('unitPriceWithTax')
+        return self
+
+
 class QueryReceiptForInvoiceResponseBodyList(TeaModel):
     def __init__(
         self,
         amount: str = None,
         apply_status: str = None,
         create_time: str = None,
         creator: QueryReceiptForInvoiceResponseBodyListCreator = None,
         customer: QueryReceiptForInvoiceResponseBodyListCustomer = None,
+        drawer_email: str = None,
+        drawer_telephone: str = None,
         invoice_type: str = None,
         model_id: str = None,
+        product_info_list: List[QueryReceiptForInvoiceResponseBodyListProductInfoList] = None,
         purchaser_account: str = None,
         purchaser_address: str = None,
         purchaser_bank_name: str = None,
         purchaser_name: str = None,
         purchaser_tax_no: str = None,
         purchaser_tel: str = None,
         receipt_id: str = None,
@@ -7012,18 +7591,24 @@
         self.apply_status = apply_status
         # 创建时间
         self.create_time = create_time
         # 创建人
         self.creator = creator
         # 客户
         self.customer = customer
+        # 开票人邮箱
+        self.drawer_email = drawer_email
+        # 开票人手机号码
+        self.drawer_telephone = drawer_telephone
         # 发票种类
         self.invoice_type = invoice_type
         # 主数据modelId
         self.model_id = model_id
+        # 商品列表
+        self.product_info_list = product_info_list
         # 购方账户
         self.purchaser_account = purchaser_account
         # 购方地址
         self.purchaser_address = purchaser_address
         # 购方银行
         self.purchaser_bank_name = purchaser_bank_name
         # 购方抬头
@@ -7046,14 +7631,18 @@
         self.title = title
 
     def validate(self):
         if self.creator:
             self.creator.validate()
         if self.customer:
             self.customer.validate()
+        if self.product_info_list:
+            for k in self.product_info_list:
+                if k:
+                    k.validate()
 
     def to_map(self):
         _map = super().to_map()
         if _map is not None:
             return _map
 
         result = dict()
@@ -7063,18 +7652,26 @@
             result['applyStatus'] = self.apply_status
         if self.create_time is not None:
             result['createTime'] = self.create_time
         if self.creator is not None:
             result['creator'] = self.creator.to_map()
         if self.customer is not None:
             result['customer'] = self.customer.to_map()
+        if self.drawer_email is not None:
+            result['drawerEmail'] = self.drawer_email
+        if self.drawer_telephone is not None:
+            result['drawerTelephone'] = self.drawer_telephone
         if self.invoice_type is not None:
             result['invoiceType'] = self.invoice_type
         if self.model_id is not None:
             result['modelId'] = self.model_id
+        result['productInfoList'] = []
+        if self.product_info_list is not None:
+            for k in self.product_info_list:
+                result['productInfoList'].append(k.to_map() if k else None)
         if self.purchaser_account is not None:
             result['purchaserAccount'] = self.purchaser_account
         if self.purchaser_address is not None:
             result['purchaserAddress'] = self.purchaser_address
         if self.purchaser_bank_name is not None:
             result['purchaserBankName'] = self.purchaser_bank_name
         if self.purchaser_name is not None:
@@ -7107,18 +7704,27 @@
             self.create_time = m.get('createTime')
         if m.get('creator') is not None:
             temp_model = QueryReceiptForInvoiceResponseBodyListCreator()
             self.creator = temp_model.from_map(m['creator'])
         if m.get('customer') is not None:
             temp_model = QueryReceiptForInvoiceResponseBodyListCustomer()
             self.customer = temp_model.from_map(m['customer'])
+        if m.get('drawerEmail') is not None:
+            self.drawer_email = m.get('drawerEmail')
+        if m.get('drawerTelephone') is not None:
+            self.drawer_telephone = m.get('drawerTelephone')
         if m.get('invoiceType') is not None:
             self.invoice_type = m.get('invoiceType')
         if m.get('modelId') is not None:
             self.model_id = m.get('modelId')
+        self.product_info_list = []
+        if m.get('productInfoList') is not None:
+            for k in m.get('productInfoList'):
+                temp_model = QueryReceiptForInvoiceResponseBodyListProductInfoList()
+                self.product_info_list.append(temp_model.from_map(k))
         if m.get('purchaserAccount') is not None:
             self.purchaser_account = m.get('purchaserAccount')
         if m.get('purchaserAddress') is not None:
             self.purchaser_address = m.get('purchaserAddress')
         if m.get('purchaserBankName') is not None:
             self.purchaser_bank_name = m.get('purchaserBankName')
         if m.get('purchaserName') is not None:
```

### Comparing `alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/blackboard_1_0/client.py` & `alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/blackboard_1_0/client.py`

 * *Files identical despite different names*

### Comparing `alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/blackboard_1_0/models.py` & `alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/blackboard_1_0/models.py`

 * *Files identical despite different names*

### Comparing `alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/calendar_1_0/client.py` & `alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/calendar_1_0/client.py`

 * *Files identical despite different names*

### Comparing `alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/calendar_1_0/models.py` & `alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/calendar_1_0/models.py`

 * *Files identical despite different names*

### Comparing `alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/carbon_1_0/client.py` & `alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/carbon_1_0/client.py`

 * *Files identical despite different names*

### Comparing `alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/carbon_1_0/models.py` & `alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/carbon_1_0/models.py`

 * *Files identical despite different names*

### Comparing `alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/card_1_0/client.py` & `alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/card_1_0/client.py`

 * *Files identical despite different names*

### Comparing `alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/card_1_0/models.py` & `alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/card_1_0/models.py`

 * *Files identical despite different names*

### Comparing `alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/chengfeng_1_0/client.py` & `alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/chengfeng_1_0/client.py`

 * *Files identical despite different names*

### Comparing `alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/chengfeng_1_0/models.py` & `alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/chengfeng_1_0/models.py`

 * *Files identical despite different names*

### Comparing `alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/conference_1_0/client.py` & `alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/conference_1_0/client.py`

 * *Files identical despite different names*

### Comparing `alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/conference_1_0/models.py` & `alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/conference_1_0/models.py`

 * *Files identical despite different names*

### Comparing `alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/connector_1_0/client.py` & `alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/connector_1_0/client.py`

 * *Files identical despite different names*

### Comparing `alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/connector_1_0/models.py` & `alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/connector_1_0/models.py`

 * *Files identical despite different names*

### Comparing `alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/contact_1_0/client.py` & `alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/contact_1_0/client.py`

 * *Files identical despite different names*

### Comparing `alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/contact_1_0/models.py` & `alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/contact_1_0/models.py`

 * *Files 0% similar despite different names*

```diff
@@ -2883,15 +2883,15 @@
         if m.get('label') is not None:
             self.label = m.get('label')
         if m.get('value') is not None:
             self.value = m.get('value')
         return self
 
 
-class GetCardInfoResponseBodyExtensionCardContactInfoTelephone(TeaModel):
+class GetCardInfoResponseBodyExtensionCardContactInfoLink(TeaModel):
     def __init__(
         self,
         label: str = None,
         value: str = None,
     ):
         self.label = label
         self.value = value
@@ -2916,15 +2916,15 @@
         if m.get('label') is not None:
             self.label = m.get('label')
         if m.get('value') is not None:
             self.value = m.get('value')
         return self
 
 
-class GetCardInfoResponseBodyExtensionCardContactInfoWechat(TeaModel):
+class GetCardInfoResponseBodyExtensionCardContactInfoTelephone(TeaModel):
     def __init__(
         self,
         label: str = None,
         value: str = None,
     ):
         self.label = label
         self.value = value
@@ -2954,41 +2954,41 @@
 
 
 class GetCardInfoResponseBodyExtensionCardContactInfo(TeaModel):
     def __init__(
         self,
         address: List[GetCardInfoResponseBodyExtensionCardContactInfoAddress] = None,
         email: List[GetCardInfoResponseBodyExtensionCardContactInfoEmail] = None,
+        link: List[GetCardInfoResponseBodyExtensionCardContactInfoLink] = None,
         telephone: List[GetCardInfoResponseBodyExtensionCardContactInfoTelephone] = None,
-        wechat: List[GetCardInfoResponseBodyExtensionCardContactInfoWechat] = None,
     ):
         # 地址
         self.address = address
         # 邮箱
         self.email = email
+        # 微信
+        self.link = link
         # 电话
         self.telephone = telephone
-        # 微信
-        self.wechat = wechat
 
     def validate(self):
         if self.address:
             for k in self.address:
                 if k:
                     k.validate()
         if self.email:
             for k in self.email:
                 if k:
                     k.validate()
-        if self.telephone:
-            for k in self.telephone:
+        if self.link:
+            for k in self.link:
                 if k:
                     k.validate()
-        if self.wechat:
-            for k in self.wechat:
+        if self.telephone:
+            for k in self.telephone:
                 if k:
                     k.validate()
 
     def to_map(self):
         _map = super().to_map()
         if _map is not None:
             return _map
@@ -2998,46 +2998,46 @@
         if self.address is not None:
             for k in self.address:
                 result['address'].append(k.to_map() if k else None)
         result['email'] = []
         if self.email is not None:
             for k in self.email:
                 result['email'].append(k.to_map() if k else None)
+        result['link'] = []
+        if self.link is not None:
+            for k in self.link:
+                result['link'].append(k.to_map() if k else None)
         result['telephone'] = []
         if self.telephone is not None:
             for k in self.telephone:
                 result['telephone'].append(k.to_map() if k else None)
-        result['wechat'] = []
-        if self.wechat is not None:
-            for k in self.wechat:
-                result['wechat'].append(k.to_map() if k else None)
         return result
 
     def from_map(self, m: dict = None):
         m = m or dict()
         self.address = []
         if m.get('address') is not None:
             for k in m.get('address'):
                 temp_model = GetCardInfoResponseBodyExtensionCardContactInfoAddress()
                 self.address.append(temp_model.from_map(k))
         self.email = []
         if m.get('email') is not None:
             for k in m.get('email'):
                 temp_model = GetCardInfoResponseBodyExtensionCardContactInfoEmail()
                 self.email.append(temp_model.from_map(k))
+        self.link = []
+        if m.get('link') is not None:
+            for k in m.get('link'):
+                temp_model = GetCardInfoResponseBodyExtensionCardContactInfoLink()
+                self.link.append(temp_model.from_map(k))
         self.telephone = []
         if m.get('telephone') is not None:
             for k in m.get('telephone'):
                 temp_model = GetCardInfoResponseBodyExtensionCardContactInfoTelephone()
                 self.telephone.append(temp_model.from_map(k))
-        self.wechat = []
-        if m.get('wechat') is not None:
-            for k in m.get('wechat'):
-                temp_model = GetCardInfoResponseBodyExtensionCardContactInfoWechat()
-                self.wechat.append(temp_model.from_map(k))
         return self
 
 
 class GetCardInfoResponseBodyExtension(TeaModel):
     def __init__(
         self,
         card_contact_info: GetCardInfoResponseBodyExtensionCardContactInfo = None,
@@ -10085,14 +10085,15 @@
         avatar_url: str = None,
         card_id: str = None,
         extension: Dict[str, Any] = None,
         industry_name: str = None,
         introduce: str = None,
         name: str = None,
         org_name: str = None,
+        settings: Dict[str, Any] = None,
         template_id: str = None,
         title: str = None,
     ):
         # 图标
         self.avatar_url = avatar_url
         # 名片id
         self.card_id = card_id
@@ -10102,14 +10103,16 @@
         self.industry_name = industry_name
         # 介绍
         self.introduce = introduce
         # 名称
         self.name = name
         # 组织名
         self.org_name = org_name
+        # 用户设置
+        self.settings = settings
         # 模版id
         self.template_id = template_id
         # 标题
         self.title = title
 
     def validate(self):
         pass
@@ -10130,14 +10133,16 @@
             result['industryName'] = self.industry_name
         if self.introduce is not None:
             result['introduce'] = self.introduce
         if self.name is not None:
             result['name'] = self.name
         if self.org_name is not None:
             result['orgName'] = self.org_name
+        if self.settings is not None:
+            result['settings'] = self.settings
         if self.template_id is not None:
             result['templateId'] = self.template_id
         if self.title is not None:
             result['title'] = self.title
         return result
 
     def from_map(self, m: dict = None):
@@ -10152,14 +10157,16 @@
             self.industry_name = m.get('industryName')
         if m.get('introduce') is not None:
             self.introduce = m.get('introduce')
         if m.get('name') is not None:
             self.name = m.get('name')
         if m.get('orgName') is not None:
             self.org_name = m.get('orgName')
+        if m.get('settings') is not None:
+            self.settings = m.get('settings')
         if m.get('templateId') is not None:
             self.template_id = m.get('templateId')
         if m.get('title') is not None:
             self.title = m.get('title')
         return self
```

### Comparing `alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/content_1_0/client.py` & `alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/content_1_0/client.py`

 * *Files identical despite different names*

### Comparing `alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/content_1_0/models.py` & `alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/content_1_0/models.py`

 * *Files identical despite different names*

### Comparing `alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/contract_1_0/client.py` & `alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/contract_1_0/client.py`

 * *Files identical despite different names*

### Comparing `alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/contract_1_0/models.py` & `alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/contract_1_0/models.py`

 * *Files identical despite different names*

### Comparing `alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/conv_file_1_0/client.py` & `alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/conv_file_1_0/client.py`

 * *Files identical despite different names*

### Comparing `alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/conv_file_1_0/models.py` & `alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/conv_file_1_0/models.py`

 * *Files identical despite different names*

### Comparing `alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/crm_1_0/client.py` & `alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/crm_1_0/client.py`

 * *Files identical despite different names*

### Comparing `alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/crm_1_0/models.py` & `alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/crm_1_0/models.py`

 * *Files identical despite different names*

### Comparing `alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/crm_2_0/client.py` & `alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/crm_2_0/client.py`

 * *Files identical despite different names*

### Comparing `alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/crm_2_0/models.py` & `alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/crm_2_0/models.py`

 * *Files identical despite different names*

### Comparing `alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/customer_service_1_0/client.py` & `alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/customer_service_1_0/client.py`

 * *Files identical despite different names*

### Comparing `alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/customer_service_1_0/models.py` & `alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/customer_service_1_0/models.py`

 * *Files identical despite different names*

### Comparing `alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/datacenter_1_0/client.py` & `alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/datacenter_1_0/client.py`

 * *Files identical despite different names*

### Comparing `alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/datacenter_1_0/models.py` & `alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/datacenter_1_0/models.py`

 * *Files identical despite different names*

### Comparing `alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/devicemng_1_0/client.py` & `alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/devicemng_1_0/client.py`

 * *Files identical despite different names*

### Comparing `alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/devicemng_1_0/models.py` & `alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/devicemng_1_0/models.py`

 * *Files identical despite different names*

### Comparing `alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/dingmi_1_0/client.py` & `alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/dingmi_1_0/client.py`

 * *Files identical despite different names*

### Comparing `alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/dingmi_1_0/models.py` & `alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/dingmi_1_0/models.py`

 * *Files identical despite different names*

### Comparing `alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/diot_1_0/client.py` & `alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/diot_1_0/client.py`

 * *Files identical despite different names*

### Comparing `alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/diot_1_0/models.py` & `alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/diot_1_0/models.py`

 * *Files identical despite different names*

### Comparing `alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/doc_1_0/client.py` & `alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/doc_1_0/client.py`

 * *Files identical despite different names*

### Comparing `alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/doc_1_0/models.py` & `alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/doc_1_0/models.py`

 * *Files identical despite different names*

### Comparing `alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/doc_2_0/client.py` & `alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/doc_2_0/client.py`

 * *Files identical despite different names*

### Comparing `alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/doc_2_0/models.py` & `alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/doc_2_0/models.py`

 * *Files identical despite different names*

### Comparing `alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/drive_1_0/client.py` & `alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/drive_1_0/client.py`

 * *Files identical despite different names*

### Comparing `alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/drive_1_0/models.py` & `alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/drive_1_0/models.py`

 * *Files identical despite different names*

### Comparing `alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/edu_1_0/client.py` & `alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/edu_1_0/client.py`

 * *Files identical despite different names*

### Comparing `alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/edu_1_0/models.py` & `alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/edu_1_0/models.py`

 * *Files identical despite different names*

### Comparing `alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/esign_1_0/client.py` & `alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/esign_1_0/client.py`

 * *Files identical despite different names*

### Comparing `alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/esign_1_0/models.py` & `alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/esign_1_0/models.py`

 * *Files identical despite different names*

### Comparing `alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/esign_2_0/client.py` & `alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/esign_2_0/client.py`

 * *Files identical despite different names*

### Comparing `alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/esign_2_0/models.py` & `alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/esign_2_0/models.py`

 * *Files identical despite different names*

### Comparing `alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/event_1_0/client.py` & `alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/event_1_0/client.py`

 * *Files identical despite different names*

### Comparing `alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/event_1_0/models.py` & `alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/event_1_0/models.py`

 * *Files identical despite different names*

### Comparing `alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/exclusive_1_0/client.py` & `alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/exclusive_1_0/client.py`

 * *Files 0% similar despite different names*

```diff
@@ -4283,14 +4283,82 @@
             body=OpenApiUtilClient.parse_to_map(body)
         )
         return TeaCore.from_map(
             dingtalkexclusive__1__0_models.SaveAndSubmitAuthInfoResponse(),
             await self.do_roarequest_async('SaveAndSubmitAuthInfo', 'exclusive_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/exclusive/ognizations/authInfos/saveAndSubmit', 'json', req, runtime)
         )
 
+    def save_white_app(
+        self,
+        request: dingtalkexclusive__1__0_models.SaveWhiteAppRequest,
+    ) -> dingtalkexclusive__1__0_models.SaveWhiteAppResponse:
+        runtime = util_models.RuntimeOptions()
+        headers = dingtalkexclusive__1__0_models.SaveWhiteAppHeaders()
+        return self.save_white_app_with_options(request, headers, runtime)
+
+    async def save_white_app_async(
+        self,
+        request: dingtalkexclusive__1__0_models.SaveWhiteAppRequest,
+    ) -> dingtalkexclusive__1__0_models.SaveWhiteAppResponse:
+        runtime = util_models.RuntimeOptions()
+        headers = dingtalkexclusive__1__0_models.SaveWhiteAppHeaders()
+        return await self.save_white_app_with_options_async(request, headers, runtime)
+
+    def save_white_app_with_options(
+        self,
+        request: dingtalkexclusive__1__0_models.SaveWhiteAppRequest,
+        headers: dingtalkexclusive__1__0_models.SaveWhiteAppHeaders,
+        runtime: util_models.RuntimeOptions,
+    ) -> dingtalkexclusive__1__0_models.SaveWhiteAppResponse:
+        UtilClient.validate_model(request)
+        body = {}
+        if not UtilClient.is_unset(request.agent_id_list):
+            body['agentIdList'] = request.agent_id_list
+        if not UtilClient.is_unset(request.operation):
+            body['operation'] = request.operation
+        real_headers = {}
+        if not UtilClient.is_unset(headers.common_headers):
+            real_headers = headers.common_headers
+        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
+            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
+        req = open_api_models.OpenApiRequest(
+            headers=real_headers,
+            body=OpenApiUtilClient.parse_to_map(body)
+        )
+        return TeaCore.from_map(
+            dingtalkexclusive__1__0_models.SaveWhiteAppResponse(),
+            self.do_roarequest('SaveWhiteApp', 'exclusive_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/exclusive/miniApps/whiteLists/save', 'json', req, runtime)
+        )
+
+    async def save_white_app_with_options_async(
+        self,
+        request: dingtalkexclusive__1__0_models.SaveWhiteAppRequest,
+        headers: dingtalkexclusive__1__0_models.SaveWhiteAppHeaders,
+        runtime: util_models.RuntimeOptions,
+    ) -> dingtalkexclusive__1__0_models.SaveWhiteAppResponse:
+        UtilClient.validate_model(request)
+        body = {}
+        if not UtilClient.is_unset(request.agent_id_list):
+            body['agentIdList'] = request.agent_id_list
+        if not UtilClient.is_unset(request.operation):
+            body['operation'] = request.operation
+        real_headers = {}
+        if not UtilClient.is_unset(headers.common_headers):
+            real_headers = headers.common_headers
+        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
+            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
+        req = open_api_models.OpenApiRequest(
+            headers=real_headers,
+            body=OpenApiUtilClient.parse_to_map(body)
+        )
+        return TeaCore.from_map(
+            dingtalkexclusive__1__0_models.SaveWhiteAppResponse(),
+            await self.do_roarequest_async('SaveWhiteApp', 'exclusive_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/exclusive/miniApps/whiteLists/save', 'json', req, runtime)
+        )
+
     def search_org_inner_group_info(
         self,
         request: dingtalkexclusive__1__0_models.SearchOrgInnerGroupInfoRequest,
     ) -> dingtalkexclusive__1__0_models.SearchOrgInnerGroupInfoResponse:
         runtime = util_models.RuntimeOptions()
         headers = dingtalkexclusive__1__0_models.SearchOrgInnerGroupInfoHeaders()
         return self.search_org_inner_group_info_with_options(request, headers, runtime)
```

### Comparing `alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/exclusive_1_0/models.py` & `alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/exclusive_1_0/models.py`

 * *Files 0% similar despite different names*

```diff
@@ -11853,14 +11853,146 @@
             self.headers = m.get('headers')
         if m.get('body') is not None:
             temp_model = SaveAndSubmitAuthInfoResponseBody()
             self.body = temp_model.from_map(m['body'])
         return self
 
 
+class SaveWhiteAppHeaders(TeaModel):
+    def __init__(
+        self,
+        common_headers: Dict[str, str] = None,
+        x_acs_dingtalk_access_token: str = None,
+    ):
+        self.common_headers = common_headers
+        self.x_acs_dingtalk_access_token = x_acs_dingtalk_access_token
+
+    def validate(self):
+        pass
+
+    def to_map(self):
+        _map = super().to_map()
+        if _map is not None:
+            return _map
+
+        result = dict()
+        if self.common_headers is not None:
+            result['commonHeaders'] = self.common_headers
+        if self.x_acs_dingtalk_access_token is not None:
+            result['x-acs-dingtalk-access-token'] = self.x_acs_dingtalk_access_token
+        return result
+
+    def from_map(self, m: dict = None):
+        m = m or dict()
+        if m.get('commonHeaders') is not None:
+            self.common_headers = m.get('commonHeaders')
+        if m.get('x-acs-dingtalk-access-token') is not None:
+            self.x_acs_dingtalk_access_token = m.get('x-acs-dingtalk-access-token')
+        return self
+
+
+class SaveWhiteAppRequest(TeaModel):
+    def __init__(
+        self,
+        agent_id_list: List[int] = None,
+        operation: str = None,
+    ):
+        # 微应用白名单AgentID
+        self.agent_id_list = agent_id_list
+        # 操作符
+        self.operation = operation
+
+    def validate(self):
+        pass
+
+    def to_map(self):
+        _map = super().to_map()
+        if _map is not None:
+            return _map
+
+        result = dict()
+        if self.agent_id_list is not None:
+            result['agentIdList'] = self.agent_id_list
+        if self.operation is not None:
+            result['operation'] = self.operation
+        return result
+
+    def from_map(self, m: dict = None):
+        m = m or dict()
+        if m.get('agentIdList') is not None:
+            self.agent_id_list = m.get('agentIdList')
+        if m.get('operation') is not None:
+            self.operation = m.get('operation')
+        return self
+
+
+class SaveWhiteAppResponseBody(TeaModel):
+    def __init__(
+        self,
+        success: bool = None,
+    ):
+        self.success = success
+
+    def validate(self):
+        pass
+
+    def to_map(self):
+        _map = super().to_map()
+        if _map is not None:
+            return _map
+
+        result = dict()
+        if self.success is not None:
+            result['success'] = self.success
+        return result
+
+    def from_map(self, m: dict = None):
+        m = m or dict()
+        if m.get('success') is not None:
+            self.success = m.get('success')
+        return self
+
+
+class SaveWhiteAppResponse(TeaModel):
+    def __init__(
+        self,
+        headers: Dict[str, str] = None,
+        body: SaveWhiteAppResponseBody = None,
+    ):
+        self.headers = headers
+        self.body = body
+
+    def validate(self):
+        self.validate_required(self.headers, 'headers')
+        self.validate_required(self.body, 'body')
+        if self.body:
+            self.body.validate()
+
+    def to_map(self):
+        _map = super().to_map()
+        if _map is not None:
+            return _map
+
+        result = dict()
+        if self.headers is not None:
+            result['headers'] = self.headers
+        if self.body is not None:
+            result['body'] = self.body.to_map()
+        return result
+
+    def from_map(self, m: dict = None):
+        m = m or dict()
+        if m.get('headers') is not None:
+            self.headers = m.get('headers')
+        if m.get('body') is not None:
+            temp_model = SaveWhiteAppResponseBody()
+            self.body = temp_model.from_map(m['body'])
+        return self
+
+
 class SearchOrgInnerGroupInfoHeaders(TeaModel):
     def __init__(
         self,
         common_headers: Dict[str, str] = None,
         x_acs_dingtalk_access_token: str = None,
     ):
         self.common_headers = common_headers
```

### Comparing `alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/finance_1_0/client.py` & `alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/finance_1_0/client.py`

 * *Files identical despite different names*

### Comparing `alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/finance_1_0/models.py` & `alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/finance_1_0/models.py`

 * *Files identical despite different names*

### Comparing `alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/flashmeeting_1_0/client.py` & `alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/flashmeeting_1_0/client.py`

 * *Files identical despite different names*

### Comparing `alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/flashmeeting_1_0/models.py` & `alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/flashmeeting_1_0/models.py`

 * *Files identical despite different names*

### Comparing `alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/group_blackboard_1_0/client.py` & `alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/group_blackboard_1_0/client.py`

 * *Files identical despite different names*

### Comparing `alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/group_blackboard_1_0/models.py` & `alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/group_blackboard_1_0/models.py`

 * *Files identical despite different names*

### Comparing `alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/h3yun_1_0/client.py` & `alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/h3yun_1_0/client.py`

 * *Files identical despite different names*

### Comparing `alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/h3yun_1_0/models.py` & `alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/h3yun_1_0/models.py`

 * *Files identical despite different names*

### Comparing `alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/h5package_1_0/client.py` & `alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/h5package_1_0/client.py`

 * *Files identical despite different names*

### Comparing `alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/h5package_1_0/models.py` & `alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/h5package_1_0/models.py`

 * *Files identical despite different names*

### Comparing `alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/hrbrain_1_0/client.py` & `alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/hrbrain_1_0/client.py`

 * *Files identical despite different names*

### Comparing `alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/hrbrain_1_0/models.py` & `alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/hrbrain_1_0/models.py`

 * *Files identical despite different names*

### Comparing `alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/hrm_1_0/client.py` & `alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/hrm_1_0/client.py`

 * *Files identical despite different names*

### Comparing `alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/hrm_1_0/models.py` & `alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/hrm_1_0/models.py`

 * *Files identical despite different names*

### Comparing `alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/im_1_0/client.py` & `alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/im_1_0/client.py`

 * *Files identical despite different names*

### Comparing `alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/im_1_0/models.py` & `alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/im_1_0/models.py`

 * *Files identical despite different names*

### Comparing `alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/im_2_0/client.py` & `alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/im_2_0/client.py`

 * *Files identical despite different names*

### Comparing `alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/im_2_0/models.py` & `alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/im_2_0/models.py`

 * *Files identical despite different names*

### Comparing `alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/impaas_1_0/client.py` & `alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/impaas_1_0/client.py`

 * *Files identical despite different names*

### Comparing `alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/impaas_1_0/models.py` & `alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/impaas_1_0/models.py`

 * *Files identical despite different names*

### Comparing `alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/industry_1_0/client.py` & `alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/industry_1_0/client.py`

 * *Files identical despite different names*

### Comparing `alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/industry_1_0/models.py` & `alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/industry_1_0/models.py`

 * *Files 0% similar despite different names*

```diff
@@ -10191,15 +10191,15 @@
         return self
 
 
 class DigitalStoreUpdateAuthInfoRequestUpdateUserListRoleList(TeaModel):
     def __init__(
         self,
         role_name: str = None,
-        source_role_id: int = None,
+        source_role_id: str = None,
     ):
         self.role_name = role_name
         self.source_role_id = source_role_id
 
     def validate(self):
         pass
 
@@ -10223,16 +10223,16 @@
             self.source_role_id = m.get('sourceRoleId')
         return self
 
 
 class DigitalStoreUpdateAuthInfoRequestUpdateUserListUserAuthList(TeaModel):
     def __init__(
         self,
-        ding_dept_id: int = None,
-        source_dept_id: int = None,
+        ding_dept_id: str = None,
+        source_dept_id: str = None,
     ):
         self.ding_dept_id = ding_dept_id
         self.source_dept_id = source_dept_id
 
     def validate(self):
         pass
```

### Comparing `alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/jzcrm_1_0/client.py` & `alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/jzcrm_1_0/client.py`

 * *Files identical despite different names*

### Comparing `alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/jzcrm_1_0/models.py` & `alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/jzcrm_1_0/models.py`

 * *Files identical despite different names*

### Comparing `alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/link_1_0/client.py` & `alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/link_1_0/client.py`

 * *Files identical despite different names*

### Comparing `alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/link_1_0/models.py` & `alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/link_1_0/models.py`

 * *Files identical despite different names*

### Comparing `alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/live_1_0/client.py` & `alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/live_1_0/client.py`

 * *Files identical despite different names*

### Comparing `alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/live_1_0/models.py` & `alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/live_1_0/models.py`

 * *Files identical despite different names*

### Comparing `alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/manufacturing_1_0/client.py` & `alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/manufacturing_1_0/client.py`

 * *Files identical despite different names*

### Comparing `alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/manufacturing_1_0/models.py` & `alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/manufacturing_1_0/models.py`

 * *Files identical despite different names*

### Comparing `alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/micro_app_1_0/client.py` & `alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/micro_app_1_0/client.py`

 * *Files identical despite different names*

### Comparing `alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/micro_app_1_0/models.py` & `alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/micro_app_1_0/models.py`

 * *Files identical despite different names*

### Comparing `alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/miniapp_1_0/client.py` & `alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/miniapp_1_0/client.py`

 * *Files identical despite different names*

### Comparing `alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/miniapp_1_0/models.py` & `alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/miniapp_1_0/models.py`

 * *Files identical despite different names*

### Comparing `alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/oauth2_1_0/client.py` & `alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/oauth2_1_0/client.py`

 * *Files identical despite different names*

### Comparing `alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/oauth2_1_0/models.py` & `alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/oauth2_1_0/models.py`

 * *Files identical despite different names*

### Comparing `alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/occupationauth_1_0/client.py` & `alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/occupationauth_1_0/client.py`

 * *Files identical despite different names*

### Comparing `alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/occupationauth_1_0/models.py` & `alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/occupationauth_1_0/models.py`

 * *Files identical despite different names*

### Comparing `alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/okr_1_0/client.py` & `alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/okr_1_0/client.py`

 * *Files identical despite different names*

### Comparing `alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/okr_1_0/models.py` & `alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/okr_1_0/models.py`

 * *Files identical despite different names*

### Comparing `alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/org_culture_1_0/client.py` & `alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/org_culture_1_0/client.py`

 * *Files identical despite different names*

### Comparing `alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/org_culture_1_0/models.py` & `alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/org_culture_1_0/models.py`

 * *Files identical despite different names*

### Comparing `alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/package_1_0/client.py` & `alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/package_1_0/client.py`

 * *Files identical despite different names*

### Comparing `alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/package_1_0/models.py` & `alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/package_1_0/models.py`

 * *Files identical despite different names*

### Comparing `alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/project_1_0/client.py` & `alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/project_1_0/client.py`

 * *Files identical despite different names*

### Comparing `alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/project_1_0/models.py` & `alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/project_1_0/models.py`

 * *Files identical despite different names*

### Comparing `alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/project_integration_1_0/client.py` & `alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/project_integration_1_0/client.py`

 * *Files identical despite different names*

### Comparing `alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/project_integration_1_0/models.py` & `alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/project_integration_1_0/models.py`

 * *Files identical despite different names*

### Comparing `alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/rcs_call_1_0/client.py` & `alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/rcs_call_1_0/client.py`

 * *Files identical despite different names*

### Comparing `alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/rcs_call_1_0/models.py` & `alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/rcs_call_1_0/models.py`

 * *Files identical despite different names*

### Comparing `alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/resident_1_0/client.py` & `alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/resident_1_0/client.py`

 * *Files identical despite different names*

### Comparing `alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/resident_1_0/models.py` & `alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/resident_1_0/models.py`

 * *Files identical despite different names*

### Comparing `alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/robot_1_0/client.py` & `alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/robot_1_0/client.py`

 * *Files identical despite different names*

### Comparing `alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/robot_1_0/models.py` & `alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/robot_1_0/models.py`

 * *Files identical despite different names*

### Comparing `alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/rooms_1_0/client.py` & `alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/rooms_1_0/client.py`

 * *Files identical despite different names*

### Comparing `alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/rooms_1_0/models.py` & `alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/rooms_1_0/models.py`

 * *Files identical despite different names*

### Comparing `alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/search_1_0/client.py` & `alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/search_1_0/client.py`

 * *Files identical despite different names*

### Comparing `alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/search_1_0/models.py` & `alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/search_1_0/models.py`

 * *Files identical despite different names*

### Comparing `alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/service_group_1_0/client.py` & `alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/service_group_1_0/client.py`

 * *Files identical despite different names*

### Comparing `alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/service_group_1_0/models.py` & `alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/service_group_1_0/models.py`

 * *Files identical despite different names*

### Comparing `alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/smart_device_1_0/client.py` & `alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/smart_device_1_0/client.py`

 * *Files identical despite different names*

### Comparing `alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/smart_device_1_0/models.py` & `alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/smart_device_1_0/models.py`

 * *Files identical despite different names*

### Comparing `alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/sns_storage_1_0/client.py` & `alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/sns_storage_1_0/client.py`

 * *Files identical despite different names*

### Comparing `alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/sns_storage_1_0/models.py` & `alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/sns_storage_1_0/models.py`

 * *Files identical despite different names*

### Comparing `alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/storage_1_0/client.py` & `alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/storage_1_0/client.py`

 * *Files identical despite different names*

### Comparing `alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/storage_1_0/models.py` & `alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/storage_1_0/models.py`

 * *Files identical despite different names*

### Comparing `alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/storage_2_0/client.py` & `alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/storage_2_0/client.py`

 * *Files identical despite different names*

### Comparing `alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/storage_2_0/models.py` & `alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/storage_2_0/models.py`

 * *Files identical despite different names*

### Comparing `alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/swform_1_0/client.py` & `alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/swform_1_0/client.py`

 * *Files identical despite different names*

### Comparing `alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/swform_1_0/models.py` & `alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/swform_1_0/models.py`

 * *Files identical despite different names*

### Comparing `alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/todo_1_0/client.py` & `alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/todo_1_0/client.py`

 * *Files identical despite different names*

### Comparing `alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/todo_1_0/models.py` & `alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/todo_1_0/models.py`

 * *Files identical despite different names*

### Comparing `alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/trade_1_0/client.py` & `alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/trade_1_0/client.py`

 * *Files identical despite different names*

### Comparing `alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/trade_1_0/models.py` & `alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/trade_1_0/models.py`

 * *Files identical despite different names*

### Comparing `alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/trajectory_1_0/client.py` & `alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/trajectory_1_0/client.py`

 * *Files identical despite different names*

### Comparing `alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/trajectory_1_0/models.py` & `alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/trajectory_1_0/models.py`

 * *Files identical despite different names*

### Comparing `alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/transcribe_1_0/client.py` & `alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/transcribe_1_0/client.py`

 * *Files identical despite different names*

### Comparing `alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/transcribe_1_0/models.py` & `alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/transcribe_1_0/models.py`

 * *Files identical despite different names*

### Comparing `alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/trip_1_0/client.py` & `alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/trip_1_0/client.py`

 * *Files identical despite different names*

### Comparing `alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/trip_1_0/models.py` & `alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/trip_1_0/models.py`

 * *Files identical despite different names*

### Comparing `alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/village_1_0/client.py` & `alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/village_1_0/client.py`

 * *Files identical despite different names*

### Comparing `alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/village_1_0/models.py` & `alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/village_1_0/models.py`

 * *Files identical despite different names*

### Comparing `alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/watt_1_0/client.py` & `alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/watt_1_0/client.py`

 * *Files identical despite different names*

### Comparing `alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/watt_1_0/models.py` & `alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/watt_1_0/models.py`

 * *Files identical despite different names*

### Comparing `alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/wiki_1_0/client.py` & `alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/wiki_1_0/client.py`

 * *Files identical despite different names*

### Comparing `alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/wiki_1_0/models.py` & `alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/wiki_1_0/models.py`

 * *Files identical despite different names*

### Comparing `alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/wms_1_0/client.py` & `alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/wms_1_0/client.py`

 * *Files identical despite different names*

### Comparing `alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/wms_1_0/models.py` & `alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/wms_1_0/models.py`

 * *Files identical despite different names*

### Comparing `alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/workbench_1_0/client.py` & `alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/workbench_1_0/client.py`

 * *Files identical despite different names*

### Comparing `alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/workbench_1_0/models.py` & `alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/workbench_1_0/models.py`

 * *Files identical despite different names*

### Comparing `alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/workflow_1_0/client.py` & `alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/workflow_1_0/client.py`

 * *Files identical despite different names*

### Comparing `alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/workflow_1_0/models.py` & `alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/workflow_1_0/models.py`

 * *Files identical despite different names*

### Comparing `alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/workrecord_1_0/client.py` & `alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/workrecord_1_0/client.py`

 * *Files identical despite different names*

### Comparing `alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/workrecord_1_0/models.py` & `alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/workrecord_1_0/models.py`

 * *Files identical despite different names*

### Comparing `alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/yida_1_0/client.py` & `alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/yida_1_0/client.py`

 * *Files identical despite different names*

### Comparing `alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk/yida_1_0/models.py` & `alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk/yida_1_0/models.py`

 * *Files identical despite different names*

### Comparing `alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk.egg-info/PKG-INFO` & `alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: alibabacloud-dingtalk
-Version: 1.5.61
+Version: 1.5.62
 Summary: Alibaba Cloud Dingtalk SDK Library for Python
 Home-page: https://github.com/aliyun/alibabacloud-sdk
 Author: Alibaba Cloud SDK
 Author-email: sdk-team@alibabacloud.com
 License: Apache License 2.0
 Description: English | [简体中文](README-CN.md)
         ![](https://aliyunsdk-pages.alicdn.com/icons/AlibabaCloud.svg)
```

### Comparing `alibabacloud_dingtalk-1.5.61/alibabacloud_dingtalk.egg-info/SOURCES.txt` & `alibabacloud_dingtalk-1.5.62/alibabacloud_dingtalk.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `alibabacloud_dingtalk-1.5.61/setup.py` & `alibabacloud_dingtalk-1.5.62/setup.py`

 * *Files 0% similar despite different names*

```diff
@@ -20,15 +20,15 @@
 
 import os
 from setuptools import setup, find_packages
 
 """
 setup module for alibabacloud_dingtalk.
 
-Created on 04/04/2023
+Created on 07/04/2023
 
 @author: Alibaba Cloud SDK
 """
 
 PACKAGE = "alibabacloud_dingtalk"
 NAME = "alibabacloud_dingtalk" or "alibabacloud-package"
 DESCRIPTION = "Alibaba Cloud Dingtalk SDK Library for Python"
```

