# Comparing `tmp/byteplus-sdk-1.0.8.tar.gz` & `tmp/byteplus-sdk-1.0.9.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "dist/byteplus-sdk-1.0.8.tar", last modified: Tue Oct 18 10:16:14 2022, max compression
+gzip compressed data, was "dist/byteplus-sdk-1.0.9.tar", last modified: Tue Nov 15 03:29:11 2022, max compression
```

## Comparing `byteplus-sdk-1.0.8.tar` & `byteplus-sdk-1.0.9.tar`

### file list

```diff
@@ -1,84 +1,87 @@
-drwxr-xr-x   0 hongsyonjiang   (502) staff       (20)        0 2022-10-18 10:16:14.000000 byteplus-sdk-1.0.8/
--rw-r--r--   0 hongsyonjiang   (502) staff       (20)      298 2022-10-18 10:16:14.000000 byteplus-sdk-1.0.8/PKG-INFO
--rw-r--r--   0 hongsyonjiang   (502) staff       (20)     1215 2022-08-11 06:56:16.000000 byteplus-sdk-1.0.8/README.md
--rw-r--r--   0 hongsyonjiang   (502) staff       (20)      541 2022-08-11 06:56:16.000000 byteplus-sdk-1.0.8/setup.py
--rw-r--r--   0 hongsyonjiang   (502) staff       (20)       38 2022-10-18 10:16:14.000000 byteplus-sdk-1.0.8/setup.cfg
-drwxr-xr-x   0 hongsyonjiang   (502) staff       (20)        0 2022-10-18 10:16:14.000000 byteplus-sdk-1.0.8/byteplus_sdk/
-drwxr-xr-x   0 hongsyonjiang   (502) staff       (20)        0 2022-10-18 10:16:14.000000 byteplus-sdk-1.0.8/byteplus_sdk/util/
--rw-r--r--   0 hongsyonjiang   (502) staff       (20)     1058 2022-08-11 06:56:16.000000 byteplus-sdk-1.0.8/byteplus_sdk/util/Functions.py
--rw-r--r--   0 hongsyonjiang   (502) staff       (20)     3653 2022-08-11 06:56:16.000000 byteplus-sdk-1.0.8/byteplus_sdk/util/Util.py
--rw-r--r--   0 hongsyonjiang   (502) staff       (20)        0 2022-08-11 06:56:16.000000 byteplus-sdk-1.0.8/byteplus_sdk/util/__init__.py
-drwxr-xr-x   0 hongsyonjiang   (502) staff       (20)        0 2022-10-18 10:16:14.000000 byteplus-sdk-1.0.8/byteplus_sdk/sms/
--rw-r--r--   0 hongsyonjiang   (502) staff       (20)        0 2022-08-11 06:56:16.000000 byteplus-sdk-1.0.8/byteplus_sdk/sms/__init__.py
--rw-r--r--   0 hongsyonjiang   (502) staff       (20)     5393 2022-10-18 10:14:27.000000 byteplus-sdk-1.0.8/byteplus_sdk/sms/SmsService.py
--rw-r--r--   0 hongsyonjiang   (502) staff       (20)      291 2022-08-11 06:56:16.000000 byteplus-sdk-1.0.8/byteplus_sdk/Credentials.py
-drwxr-xr-x   0 hongsyonjiang   (502) staff       (20)        0 2022-10-18 10:16:14.000000 byteplus-sdk-1.0.8/byteplus_sdk/auth/
--rw-r--r--   0 hongsyonjiang   (502) staff       (20)      699 2022-08-11 06:56:16.000000 byteplus-sdk-1.0.8/byteplus_sdk/auth/MetaData.py
--rw-r--r--   0 hongsyonjiang   (502) staff       (20)        0 2022-08-11 06:56:16.000000 byteplus-sdk-1.0.8/byteplus_sdk/auth/__init__.py
--rw-r--r--   0 hongsyonjiang   (502) staff       (20)     5557 2022-08-11 06:56:16.000000 byteplus-sdk-1.0.8/byteplus_sdk/auth/SignerV4.py
-drwxr-xr-x   0 hongsyonjiang   (502) staff       (20)        0 2022-10-18 10:16:14.000000 byteplus-sdk-1.0.8/byteplus_sdk/example/
--rw-r--r--   0 hongsyonjiang   (502) staff       (20)       17 2022-08-11 06:56:16.000000 byteplus-sdk-1.0.8/byteplus_sdk/example/__init__.py
-drwxr-xr-x   0 hongsyonjiang   (502) staff       (20)        0 2022-10-18 10:16:14.000000 byteplus-sdk-1.0.8/byteplus_sdk/example/cdn/
--rw-r--r--   0 hongsyonjiang   (502) staff       (20)      410 2022-08-11 06:56:16.000000 byteplus-sdk-1.0.8/byteplus_sdk/example/cdn/start_cdn_domain.py
--rw-r--r--   0 hongsyonjiang   (502) staff       (20)      534 2022-08-11 06:56:16.000000 byteplus-sdk-1.0.8/byteplus_sdk/example/cdn/describe_origin_top_status_code.py
--rw-r--r--   0 hongsyonjiang   (502) staff       (20)      614 2022-08-11 06:56:16.000000 byteplus-sdk-1.0.8/byteplus_sdk/example/cdn/describe_cdn_domain_top_data.py
--rw-r--r--   0 hongsyonjiang   (502) staff       (20)      409 2022-08-11 06:56:16.000000 byteplus-sdk-1.0.8/byteplus_sdk/example/cdn/stop_cdn_domain.py
--rw-r--r--   0 hongsyonjiang   (502) staff       (20)      412 2022-08-11 06:56:16.000000 byteplus-sdk-1.0.8/byteplus_sdk/example/cdn/describe_cdn_config.py
--rw-r--r--   0 hongsyonjiang   (502) staff       (20)      449 2022-08-11 06:56:16.000000 byteplus-sdk-1.0.8/byteplus_sdk/example/cdn/submit_unblock_task.py
--rw-r--r--   0 hongsyonjiang   (502) staff       (20)      571 2022-08-11 06:56:16.000000 byteplus-sdk-1.0.8/byteplus_sdk/example/cdn/describe_accounting_data.py
--rw-r--r--   0 hongsyonjiang   (502) staff       (20)      596 2022-08-11 06:56:16.000000 byteplus-sdk-1.0.8/byteplus_sdk/example/cdn/describe_cdn_origin_data.py
--rw-r--r--   0 hongsyonjiang   (502) staff       (20)      417 2022-08-11 06:56:16.000000 byteplus-sdk-1.0.8/byteplus_sdk/example/cdn/describe_iplist_info.py
--rw-r--r--   0 hongsyonjiang   (502) staff       (20)      558 2022-08-11 06:56:16.000000 byteplus-sdk-1.0.8/byteplus_sdk/example/cdn/describe_edge_nrt_data_summary.py
--rw-r--r--   0 hongsyonjiang   (502) staff       (20)      401 2022-08-11 06:56:16.000000 byteplus-sdk-1.0.8/byteplus_sdk/example/cdn/describe_ip_info.py
--rw-r--r--   0 hongsyonjiang   (502) staff       (20)       30 2022-08-11 06:56:16.000000 byteplus-sdk-1.0.8/byteplus_sdk/example/cdn/__init__.py
--rw-r--r--   0 hongsyonjiang   (502) staff       (20)      490 2022-08-11 06:56:16.000000 byteplus-sdk-1.0.8/byteplus_sdk/example/cdn/submit_refresh_task.py
--rw-r--r--   0 hongsyonjiang   (502) staff       (20)      519 2022-08-11 06:56:16.000000 byteplus-sdk-1.0.8/byteplus_sdk/example/cdn/add_resource_tags.py
--rw-r--r--   0 hongsyonjiang   (502) staff       (20)      449 2022-08-11 06:56:16.000000 byteplus-sdk-1.0.8/byteplus_sdk/example/cdn/submit_preload_task.py
--rw-r--r--   0 hongsyonjiang   (502) staff       (20)      358 2022-08-11 06:56:16.000000 byteplus-sdk-1.0.8/byteplus_sdk/example/cdn/describe_content_quota.py
--rw-r--r--   0 hongsyonjiang   (502) staff       (20)      910 2022-08-11 06:56:16.000000 byteplus-sdk-1.0.8/byteplus_sdk/example/cdn/add_cdn_domain.py
--rw-r--r--   0 hongsyonjiang   (502) staff       (20)      357 2022-08-11 06:56:16.000000 byteplus-sdk-1.0.8/byteplus_sdk/example/cdn/describe_cdn_service.py
--rw-r--r--   0 hongsyonjiang   (502) staff       (20)      411 2022-08-11 06:56:16.000000 byteplus-sdk-1.0.8/byteplus_sdk/example/cdn/delete_cdn_domain.py
--rw-r--r--   0 hongsyonjiang   (502) staff       (20)      614 2022-08-11 06:56:16.000000 byteplus-sdk-1.0.8/byteplus_sdk/example/cdn/describe_edge_top_nrt_data.py
--rw-r--r--   0 hongsyonjiang   (502) staff       (20)      544 2022-08-11 06:56:16.000000 byteplus-sdk-1.0.8/byteplus_sdk/example/cdn/describe_cdn_access_log.py
--rw-r--r--   0 hongsyonjiang   (502) staff       (20)      652 2022-08-11 06:56:16.000000 byteplus-sdk-1.0.8/byteplus_sdk/example/cdn/describe_cdn_detail.py
--rw-r--r--   0 hongsyonjiang   (502) staff       (20)      583 2022-08-11 06:56:16.000000 byteplus-sdk-1.0.8/byteplus_sdk/example/cdn/describe_origin_top_nrt_data.py
--rw-r--r--   0 hongsyonjiang   (502) staff       (20)      391 2022-08-11 06:56:16.000000 byteplus-sdk-1.0.8/byteplus_sdk/example/cdn/list_cdn_domains.py
--rw-r--r--   0 hongsyonjiang   (502) staff       (20)      718 2022-08-11 06:56:16.000000 byteplus-sdk-1.0.8/byteplus_sdk/example/cdn/describe_cdn_data.py
--rw-r--r--   0 hongsyonjiang   (502) staff       (20)      626 2022-08-11 06:56:16.000000 byteplus-sdk-1.0.8/byteplus_sdk/example/cdn/describe_edge_top_statistical_data.py
--rw-r--r--   0 hongsyonjiang   (502) staff       (20)      597 2022-08-11 06:56:16.000000 byteplus-sdk-1.0.8/byteplus_sdk/example/cdn/describe_edge_statistical_data.py
--rw-r--r--   0 hongsyonjiang   (502) staff       (20)      565 2022-08-11 06:56:16.000000 byteplus-sdk-1.0.8/byteplus_sdk/example/cdn/describe_content_block_tasks.py
--rw-r--r--   0 hongsyonjiang   (502) staff       (20)      447 2022-08-11 06:56:16.000000 byteplus-sdk-1.0.8/byteplus_sdk/example/cdn/submit_block_task.py
--rw-r--r--   0 hongsyonjiang   (502) staff       (20)      560 2022-08-11 06:56:16.000000 byteplus-sdk-1.0.8/byteplus_sdk/example/cdn/describe_origin_nrt_data_summary.py
--rw-r--r--   0 hongsyonjiang   (502) staff       (20)      532 2022-08-11 06:56:16.000000 byteplus-sdk-1.0.8/byteplus_sdk/example/cdn/describe_edge_top_status_code.py
--rw-r--r--   0 hongsyonjiang   (502) staff       (20)      464 2022-08-11 06:56:16.000000 byteplus-sdk-1.0.8/byteplus_sdk/example/cdn/describe_content_tasks.py
--rw-r--r--   0 hongsyonjiang   (502) staff       (20)      415 2022-08-11 06:56:16.000000 byteplus-sdk-1.0.8/byteplus_sdk/example/cdn/describe_cdn_upper_ip.py
--rw-r--r--   0 hongsyonjiang   (502) staff       (20)      427 2022-08-11 06:56:16.000000 byteplus-sdk-1.0.8/byteplus_sdk/example/cdn/describe_cdn_region_and_isp.py
-drwxr-xr-x   0 hongsyonjiang   (502) staff       (20)        0 2022-10-18 10:16:14.000000 byteplus-sdk-1.0.8/byteplus_sdk/example/visual/
--rw-r--r--   0 hongsyonjiang   (502) staff       (20)     1045 2022-08-24 03:47:33.000000 byteplus-sdk-1.0.8/byteplus_sdk/example/visual/example_common.py
--rw-r--r--   0 hongsyonjiang   (502) staff       (20)        0 2022-08-24 03:47:33.000000 byteplus-sdk-1.0.8/byteplus_sdk/example/visual/__init__.py
--rw-r--r--   0 hongsyonjiang   (502) staff       (20)     2592 2022-08-11 06:56:16.000000 byteplus-sdk-1.0.8/byteplus_sdk/Policy.py
--rw-r--r--   0 hongsyonjiang   (502) staff       (20)       34 2022-10-18 10:14:27.000000 byteplus-sdk-1.0.8/byteplus_sdk/__init__.py
--rw-r--r--   0 hongsyonjiang   (502) staff       (20)      367 2022-08-11 06:56:16.000000 byteplus-sdk-1.0.8/byteplus_sdk/ServiceInfo.py
-drwxr-xr-x   0 hongsyonjiang   (502) staff       (20)        0 2022-10-18 10:16:14.000000 byteplus-sdk-1.0.8/byteplus_sdk/const/
--rw-r--r--   0 hongsyonjiang   (502) staff       (20)        0 2022-08-11 06:56:16.000000 byteplus-sdk-1.0.8/byteplus_sdk/const/__init__.py
--rw-r--r--   0 hongsyonjiang   (502) staff       (20)     1600 2022-10-18 10:14:27.000000 byteplus-sdk-1.0.8/byteplus_sdk/const/Const.py
-drwxr-xr-x   0 hongsyonjiang   (502) staff       (20)        0 2022-10-18 10:16:14.000000 byteplus-sdk-1.0.8/byteplus_sdk/iam/
--rw-r--r--   0 hongsyonjiang   (502) staff       (20)     1432 2022-08-11 06:56:16.000000 byteplus-sdk-1.0.8/byteplus_sdk/iam/IamService.py
--rw-r--r--   0 hongsyonjiang   (502) staff       (20)        0 2022-08-11 06:56:16.000000 byteplus-sdk-1.0.8/byteplus_sdk/iam/__init__.py
-drwxr-xr-x   0 hongsyonjiang   (502) staff       (20)        0 2022-10-18 10:16:14.000000 byteplus-sdk-1.0.8/byteplus_sdk/cdn/
--rw-r--r--   0 hongsyonjiang   (502) staff       (20)    16709 2022-08-11 06:56:16.000000 byteplus-sdk-1.0.8/byteplus_sdk/cdn/service.py
--rw-r--r--   0 hongsyonjiang   (502) staff       (20)        0 2022-08-11 06:56:16.000000 byteplus-sdk-1.0.8/byteplus_sdk/cdn/__init__.py
-drwxr-xr-x   0 hongsyonjiang   (502) staff       (20)        0 2022-10-18 10:16:14.000000 byteplus-sdk-1.0.8/byteplus_sdk/visual/
--rw-r--r--   0 hongsyonjiang   (502) staff       (20)        0 2022-08-24 03:47:33.000000 byteplus-sdk-1.0.8/byteplus_sdk/visual/__init__.py
--rw-r--r--   0 hongsyonjiang   (502) staff       (20)     2602 2022-08-24 03:47:33.000000 byteplus-sdk-1.0.8/byteplus_sdk/visual/VisualService.py
--rw-r--r--   0 hongsyonjiang   (502) staff       (20)      323 2022-08-11 06:56:16.000000 byteplus-sdk-1.0.8/byteplus_sdk/ApiInfo.py
-drwxr-xr-x   0 hongsyonjiang   (502) staff       (20)        0 2022-10-18 10:16:14.000000 byteplus-sdk-1.0.8/byteplus_sdk/base/
--rw-r--r--   0 hongsyonjiang   (502) staff       (20)     8165 2022-10-18 10:14:27.000000 byteplus-sdk-1.0.8/byteplus_sdk/base/Service.py
--rw-r--r--   0 hongsyonjiang   (502) staff       (20)     1232 2022-08-11 06:56:16.000000 byteplus-sdk-1.0.8/byteplus_sdk/base/Request.py
--rw-r--r--   0 hongsyonjiang   (502) staff       (20)        0 2022-08-11 06:56:16.000000 byteplus-sdk-1.0.8/byteplus_sdk/base/__init__.py
-drwxr-xr-x   0 hongsyonjiang   (502) staff       (20)        0 2022-10-18 10:16:14.000000 byteplus-sdk-1.0.8/byteplus_sdk.egg-info/
--rw-r--r--   0 hongsyonjiang   (502) staff       (20)      298 2022-10-18 10:16:14.000000 byteplus-sdk-1.0.8/byteplus_sdk.egg-info/PKG-INFO
--rw-r--r--   0 hongsyonjiang   (502) staff       (20)     2747 2022-10-18 10:16:14.000000 byteplus-sdk-1.0.8/byteplus_sdk.egg-info/SOURCES.txt
--rw-r--r--   0 hongsyonjiang   (502) staff       (20)       47 2022-10-18 10:16:14.000000 byteplus-sdk-1.0.8/byteplus_sdk.egg-info/requires.txt
--rw-r--r--   0 hongsyonjiang   (502) staff       (20)       13 2022-10-18 10:16:14.000000 byteplus-sdk-1.0.8/byteplus_sdk.egg-info/top_level.txt
--rw-r--r--   0 hongsyonjiang   (502) staff       (20)        1 2022-10-18 10:16:14.000000 byteplus-sdk-1.0.8/byteplus_sdk.egg-info/dependency_links.txt
+drwxr-xr-x   0 chizhang   (502) staff       (20)        0 2022-11-15 03:29:11.314056 byteplus-sdk-1.0.9/
+-rw-r--r--   0 chizhang   (502) staff       (20)      298 2022-11-15 03:29:11.312328 byteplus-sdk-1.0.9/PKG-INFO
+-rw-r--r--   0 chizhang   (502) staff       (20)     1215 2022-11-15 03:20:47.000000 byteplus-sdk-1.0.9/README.md
+drwxr-xr-x   0 chizhang   (502) staff       (20)        0 2022-11-15 03:29:11.132559 byteplus-sdk-1.0.9/byteplus_sdk/
+-rw-r--r--   0 chizhang   (502) staff       (20)      323 2021-07-13 09:43:20.000000 byteplus-sdk-1.0.9/byteplus_sdk/ApiInfo.py
+-rw-r--r--   0 chizhang   (502) staff       (20)      291 2021-07-13 09:43:20.000000 byteplus-sdk-1.0.9/byteplus_sdk/Credentials.py
+-rw-r--r--   0 chizhang   (502) staff       (20)     2592 2021-07-13 09:43:20.000000 byteplus-sdk-1.0.9/byteplus_sdk/Policy.py
+-rw-r--r--   0 chizhang   (502) staff       (20)      367 2021-07-13 09:43:20.000000 byteplus-sdk-1.0.9/byteplus_sdk/ServiceInfo.py
+-rw-r--r--   0 chizhang   (502) staff       (20)       34 2022-11-15 03:28:56.000000 byteplus-sdk-1.0.9/byteplus_sdk/__init__.py
+drwxr-xr-x   0 chizhang   (502) staff       (20)        0 2022-11-15 03:29:11.145430 byteplus-sdk-1.0.9/byteplus_sdk/auth/
+-rw-r--r--   0 chizhang   (502) staff       (20)      699 2021-07-13 12:34:48.000000 byteplus-sdk-1.0.9/byteplus_sdk/auth/MetaData.py
+-rw-r--r--   0 chizhang   (502) staff       (20)     5556 2022-11-15 03:20:47.000000 byteplus-sdk-1.0.9/byteplus_sdk/auth/SignerV4.py
+-rw-r--r--   0 chizhang   (502) staff       (20)        0 2021-07-13 09:43:20.000000 byteplus-sdk-1.0.9/byteplus_sdk/auth/__init__.py
+drwxr-xr-x   0 chizhang   (502) staff       (20)        0 2022-11-15 03:29:11.150370 byteplus-sdk-1.0.9/byteplus_sdk/base/
+-rw-r--r--   0 chizhang   (502) staff       (20)     1231 2022-11-15 03:20:47.000000 byteplus-sdk-1.0.9/byteplus_sdk/base/Request.py
+-rw-r--r--   0 chizhang   (502) staff       (20)     8165 2022-11-15 03:20:47.000000 byteplus-sdk-1.0.9/byteplus_sdk/base/Service.py
+-rw-r--r--   0 chizhang   (502) staff       (20)        0 2021-07-13 09:43:20.000000 byteplus-sdk-1.0.9/byteplus_sdk/base/__init__.py
+drwxr-xr-x   0 chizhang   (502) staff       (20)        0 2022-11-15 03:29:11.152202 byteplus-sdk-1.0.9/byteplus_sdk/cdn/
+-rw-r--r--   0 chizhang   (502) staff       (20)        0 2022-11-15 03:20:47.000000 byteplus-sdk-1.0.9/byteplus_sdk/cdn/__init__.py
+-rw-r--r--   0 chizhang   (502) staff       (20)    18444 2022-11-15 03:20:47.000000 byteplus-sdk-1.0.9/byteplus_sdk/cdn/service.py
+drwxr-xr-x   0 chizhang   (502) staff       (20)        0 2022-11-15 03:29:11.155635 byteplus-sdk-1.0.9/byteplus_sdk/const/
+-rw-r--r--   0 chizhang   (502) staff       (20)     1600 2022-11-15 03:20:47.000000 byteplus-sdk-1.0.9/byteplus_sdk/const/Const.py
+-rw-r--r--   0 chizhang   (502) staff       (20)        0 2021-07-13 09:43:20.000000 byteplus-sdk-1.0.9/byteplus_sdk/const/__init__.py
+drwxr-xr-x   0 chizhang   (502) staff       (20)        0 2022-11-15 03:29:11.156912 byteplus-sdk-1.0.9/byteplus_sdk/example/
+-rw-r--r--   0 chizhang   (502) staff       (20)       17 2021-07-13 10:03:37.000000 byteplus-sdk-1.0.9/byteplus_sdk/example/__init__.py
+drwxr-xr-x   0 chizhang   (502) staff       (20)        0 2022-11-15 03:29:11.260546 byteplus-sdk-1.0.9/byteplus_sdk/example/cdn/
+-rw-r--r--   0 chizhang   (502) staff       (20)       30 2022-11-15 03:20:47.000000 byteplus-sdk-1.0.9/byteplus_sdk/example/cdn/__init__.py
+-rw-r--r--   0 chizhang   (502) staff       (20)      709 2022-11-15 03:20:47.000000 byteplus-sdk-1.0.9/byteplus_sdk/example/cdn/add_cdn_certificate.py
+-rw-r--r--   0 chizhang   (502) staff       (20)      910 2022-11-15 03:20:47.000000 byteplus-sdk-1.0.9/byteplus_sdk/example/cdn/add_cdn_domain.py
+-rw-r--r--   0 chizhang   (502) staff       (20)      411 2022-11-15 03:20:47.000000 byteplus-sdk-1.0.9/byteplus_sdk/example/cdn/delete_cdn_domain.py
+-rw-r--r--   0 chizhang   (502) staff       (20)      571 2022-11-15 03:20:47.000000 byteplus-sdk-1.0.9/byteplus_sdk/example/cdn/describe_accounting_data.py
+-rw-r--r--   0 chizhang   (502) staff       (20)      544 2022-11-15 03:20:47.000000 byteplus-sdk-1.0.9/byteplus_sdk/example/cdn/describe_cdn_access_log.py
+-rw-r--r--   0 chizhang   (502) staff       (20)      412 2022-11-15 03:20:47.000000 byteplus-sdk-1.0.9/byteplus_sdk/example/cdn/describe_cdn_config.py
+-rw-r--r--   0 chizhang   (502) staff       (20)      718 2022-11-15 03:20:47.000000 byteplus-sdk-1.0.9/byteplus_sdk/example/cdn/describe_cdn_data.py
+-rw-r--r--   0 chizhang   (502) staff       (20)      574 2022-11-15 03:20:47.000000 byteplus-sdk-1.0.9/byteplus_sdk/example/cdn/describe_cdn_data_detail.py
+-rw-r--r--   0 chizhang   (502) staff       (20)      652 2022-11-15 03:20:47.000000 byteplus-sdk-1.0.9/byteplus_sdk/example/cdn/describe_cdn_detail.py
+-rw-r--r--   0 chizhang   (502) staff       (20)      596 2022-11-15 03:20:47.000000 byteplus-sdk-1.0.9/byteplus_sdk/example/cdn/describe_cdn_origin_data.py
+-rw-r--r--   0 chizhang   (502) staff       (20)      427 2022-11-15 03:20:47.000000 byteplus-sdk-1.0.9/byteplus_sdk/example/cdn/describe_cdn_region_and_isp.py
+-rw-r--r--   0 chizhang   (502) staff       (20)      357 2022-11-15 03:20:47.000000 byteplus-sdk-1.0.9/byteplus_sdk/example/cdn/describe_cdn_service.py
+-rw-r--r--   0 chizhang   (502) staff       (20)      415 2022-11-15 03:20:47.000000 byteplus-sdk-1.0.9/byteplus_sdk/example/cdn/describe_cdn_upper_ip.py
+-rw-r--r--   0 chizhang   (502) staff       (20)      565 2022-11-15 03:20:47.000000 byteplus-sdk-1.0.9/byteplus_sdk/example/cdn/describe_content_block_tasks.py
+-rw-r--r--   0 chizhang   (502) staff       (20)      358 2022-11-15 03:20:47.000000 byteplus-sdk-1.0.9/byteplus_sdk/example/cdn/describe_content_quota.py
+-rw-r--r--   0 chizhang   (502) staff       (20)      464 2022-11-15 03:20:47.000000 byteplus-sdk-1.0.9/byteplus_sdk/example/cdn/describe_content_tasks.py
+-rw-r--r--   0 chizhang   (502) staff       (20)      558 2022-11-15 03:20:47.000000 byteplus-sdk-1.0.9/byteplus_sdk/example/cdn/describe_edge_nrt_data_summary.py
+-rw-r--r--   0 chizhang   (502) staff       (20)      597 2022-11-15 03:20:47.000000 byteplus-sdk-1.0.9/byteplus_sdk/example/cdn/describe_edge_statistical_data.py
+-rw-r--r--   0 chizhang   (502) staff       (20)      614 2022-11-15 03:20:47.000000 byteplus-sdk-1.0.9/byteplus_sdk/example/cdn/describe_edge_top_nrt_data.py
+-rw-r--r--   0 chizhang   (502) staff       (20)      626 2022-11-15 03:20:47.000000 byteplus-sdk-1.0.9/byteplus_sdk/example/cdn/describe_edge_top_statistical_data.py
+-rw-r--r--   0 chizhang   (502) staff       (20)      532 2022-11-15 03:20:47.000000 byteplus-sdk-1.0.9/byteplus_sdk/example/cdn/describe_edge_top_status_code.py
+-rw-r--r--   0 chizhang   (502) staff       (20)      401 2022-11-15 03:20:47.000000 byteplus-sdk-1.0.9/byteplus_sdk/example/cdn/describe_ip_info.py
+-rw-r--r--   0 chizhang   (502) staff       (20)      421 2022-11-15 03:20:47.000000 byteplus-sdk-1.0.9/byteplus_sdk/example/cdn/describe_ip_list_info.py
+-rw-r--r--   0 chizhang   (502) staff       (20)      560 2022-11-15 03:20:47.000000 byteplus-sdk-1.0.9/byteplus_sdk/example/cdn/describe_origin_nrt_data_summary.py
+-rw-r--r--   0 chizhang   (502) staff       (20)      583 2022-11-15 03:20:47.000000 byteplus-sdk-1.0.9/byteplus_sdk/example/cdn/describe_origin_top_nrt_data.py
+-rw-r--r--   0 chizhang   (502) staff       (20)      534 2022-11-15 03:20:47.000000 byteplus-sdk-1.0.9/byteplus_sdk/example/cdn/describe_origin_top_status_code.py
+-rw-r--r--   0 chizhang   (502) staff       (20)      382 2022-11-15 03:20:47.000000 byteplus-sdk-1.0.9/byteplus_sdk/example/cdn/list_cdn_cert_info.py
+-rw-r--r--   0 chizhang   (502) staff       (20)      391 2022-11-15 03:20:47.000000 byteplus-sdk-1.0.9/byteplus_sdk/example/cdn/list_cdn_domains.py
+-rw-r--r--   0 chizhang   (502) staff       (20)      415 2022-11-15 03:20:47.000000 byteplus-sdk-1.0.9/byteplus_sdk/example/cdn/list_cert_info.py
+-rw-r--r--   0 chizhang   (502) staff       (20)      410 2022-11-15 03:20:47.000000 byteplus-sdk-1.0.9/byteplus_sdk/example/cdn/start_cdn_domain.py
+-rw-r--r--   0 chizhang   (502) staff       (20)      409 2022-11-15 03:20:47.000000 byteplus-sdk-1.0.9/byteplus_sdk/example/cdn/stop_cdn_domain.py
+-rw-r--r--   0 chizhang   (502) staff       (20)      447 2022-11-15 03:20:47.000000 byteplus-sdk-1.0.9/byteplus_sdk/example/cdn/submit_block_task.py
+-rw-r--r--   0 chizhang   (502) staff       (20)      449 2022-11-15 03:20:47.000000 byteplus-sdk-1.0.9/byteplus_sdk/example/cdn/submit_preload_task.py
+-rw-r--r--   0 chizhang   (502) staff       (20)      490 2022-11-15 03:20:47.000000 byteplus-sdk-1.0.9/byteplus_sdk/example/cdn/submit_refresh_task.py
+-rw-r--r--   0 chizhang   (502) staff       (20)      449 2022-11-15 03:20:47.000000 byteplus-sdk-1.0.9/byteplus_sdk/example/cdn/submit_unblock_task.py
+-rw-r--r--   0 chizhang   (502) staff       (20)      864 2022-11-15 03:20:47.000000 byteplus-sdk-1.0.9/byteplus_sdk/example/cdn/update_cdn_config.py
+drwxr-xr-x   0 chizhang   (502) staff       (20)        0 2022-11-15 03:29:11.277626 byteplus-sdk-1.0.9/byteplus_sdk/example/visual/
+-rw-r--r--   0 chizhang   (502) staff       (20)        0 2022-11-15 03:20:47.000000 byteplus-sdk-1.0.9/byteplus_sdk/example/visual/__init__.py
+-rw-r--r--   0 chizhang   (502) staff       (20)     1045 2022-11-15 03:20:47.000000 byteplus-sdk-1.0.9/byteplus_sdk/example/visual/example_common.py
+drwxr-xr-x   0 chizhang   (502) staff       (20)        0 2022-11-15 03:29:11.290029 byteplus-sdk-1.0.9/byteplus_sdk/iam/
+-rw-r--r--   0 chizhang   (502) staff       (20)     1432 2021-07-13 10:14:58.000000 byteplus-sdk-1.0.9/byteplus_sdk/iam/IamService.py
+-rw-r--r--   0 chizhang   (502) staff       (20)        0 2021-07-13 09:43:20.000000 byteplus-sdk-1.0.9/byteplus_sdk/iam/__init__.py
+drwxr-xr-x   0 chizhang   (502) staff       (20)        0 2022-11-15 03:29:11.292522 byteplus-sdk-1.0.9/byteplus_sdk/sms/
+-rw-r--r--   0 chizhang   (502) staff       (20)     5393 2022-11-15 03:20:47.000000 byteplus-sdk-1.0.9/byteplus_sdk/sms/SmsService.py
+-rw-r--r--   0 chizhang   (502) staff       (20)        0 2022-02-22 07:07:43.000000 byteplus-sdk-1.0.9/byteplus_sdk/sms/__init__.py
+drwxr-xr-x   0 chizhang   (502) staff       (20)        0 2022-11-15 03:29:11.304167 byteplus-sdk-1.0.9/byteplus_sdk/util/
+-rw-r--r--   0 chizhang   (502) staff       (20)     1058 2021-07-13 09:43:20.000000 byteplus-sdk-1.0.9/byteplus_sdk/util/Functions.py
+-rw-r--r--   0 chizhang   (502) staff       (20)     3653 2021-07-13 10:15:13.000000 byteplus-sdk-1.0.9/byteplus_sdk/util/Util.py
+-rw-r--r--   0 chizhang   (502) staff       (20)        0 2021-07-13 09:43:20.000000 byteplus-sdk-1.0.9/byteplus_sdk/util/__init__.py
+drwxr-xr-x   0 chizhang   (502) staff       (20)        0 2022-11-15 03:29:11.310122 byteplus-sdk-1.0.9/byteplus_sdk/visual/
+-rw-r--r--   0 chizhang   (502) staff       (20)     2602 2022-11-15 03:20:47.000000 byteplus-sdk-1.0.9/byteplus_sdk/visual/VisualService.py
+-rw-r--r--   0 chizhang   (502) staff       (20)        0 2022-11-15 03:20:47.000000 byteplus-sdk-1.0.9/byteplus_sdk/visual/__init__.py
+drwxr-xr-x   0 chizhang   (502) staff       (20)        0 2022-11-15 03:29:11.139862 byteplus-sdk-1.0.9/byteplus_sdk.egg-info/
+-rw-r--r--   0 chizhang   (502) staff       (20)      298 2022-11-15 03:29:10.000000 byteplus-sdk-1.0.9/byteplus_sdk.egg-info/PKG-INFO
+-rw-r--r--   0 chizhang   (502) staff       (20)     2882 2022-11-15 03:29:10.000000 byteplus-sdk-1.0.9/byteplus_sdk.egg-info/SOURCES.txt
+-rw-r--r--   0 chizhang   (502) staff       (20)        1 2022-11-15 03:29:10.000000 byteplus-sdk-1.0.9/byteplus_sdk.egg-info/dependency_links.txt
+-rw-r--r--   0 chizhang   (502) staff       (20)       47 2022-11-15 03:29:10.000000 byteplus-sdk-1.0.9/byteplus_sdk.egg-info/requires.txt
+-rw-r--r--   0 chizhang   (502) staff       (20)       13 2022-11-15 03:29:10.000000 byteplus-sdk-1.0.9/byteplus_sdk.egg-info/top_level.txt
+-rw-r--r--   0 chizhang   (502) staff       (20)       38 2022-11-15 03:29:11.314534 byteplus-sdk-1.0.9/setup.cfg
+-rw-r--r--   0 chizhang   (502) staff       (20)      541 2021-07-13 10:03:13.000000 byteplus-sdk-1.0.9/setup.py
```

### filetype from file(1)

```diff
@@ -1 +1 @@
-POSIX tar archive (GNU)
+POSIX tar archive
```

### Comparing `byteplus-sdk-1.0.8/README.md` & `byteplus-sdk-1.0.9/README.md`

 * *Files identical despite different names*

### Comparing `byteplus-sdk-1.0.8/setup.py` & `byteplus-sdk-1.0.9/setup.py`

 * *Files identical despite different names*

### Comparing `byteplus-sdk-1.0.8/byteplus_sdk/util/Functions.py` & `byteplus-sdk-1.0.9/byteplus_sdk/util/Functions.py`

 * *Files identical despite different names*

### Comparing `byteplus-sdk-1.0.8/byteplus_sdk/util/Util.py` & `byteplus-sdk-1.0.9/byteplus_sdk/util/Util.py`

 * *Files identical despite different names*

### Comparing `byteplus-sdk-1.0.8/byteplus_sdk/sms/SmsService.py` & `byteplus-sdk-1.0.9/byteplus_sdk/sms/SmsService.py`

 * *Files identical despite different names*

### Comparing `byteplus-sdk-1.0.8/byteplus_sdk/auth/MetaData.py` & `byteplus-sdk-1.0.9/byteplus_sdk/auth/MetaData.py`

 * *Files identical despite different names*

### Comparing `byteplus-sdk-1.0.8/byteplus_sdk/auth/SignerV4.py` & `byteplus-sdk-1.0.9/byteplus_sdk/auth/SignerV4.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-# coding : utf-8
+# coding: utf-8
 import datetime
 import sys
 import json
 import pytz
 
 try:
     from urllib import urlencode
```

### Comparing `byteplus-sdk-1.0.8/byteplus_sdk/example/cdn/describe_origin_top_status_code.py` & `byteplus-sdk-1.0.9/byteplus_sdk/example/cdn/describe_origin_top_status_code.py`

 * *Files identical despite different names*

### Comparing `byteplus-sdk-1.0.8/byteplus_sdk/example/cdn/describe_cdn_domain_top_data.py` & `byteplus-sdk-1.0.9/byteplus_sdk/example/cdn/describe_edge_statistical_data.py`

 * *Files 8% similar despite different names*

```diff
@@ -11,15 +11,14 @@
     svc = CDNService()
     svc.set_ak(ak)
     svc.set_sk(sk)
     now = int(datetime.datetime.now().strftime("%s"))
     body = {
         'StartTime': now - 86400,
         'EndTime': now,
-        'Metric': 'pv',
+        'Metric': 'clientIp',
         'Domain': 'example.com',
-        'Item': 'region'
     }
     print(body)
 
-    resp = svc.describe_cdn_domain_top_data(body)
+    resp = svc.describe_edge_statistical_data(body)
     print(resp)
```

### Comparing `byteplus-sdk-1.0.8/byteplus_sdk/example/cdn/describe_accounting_data.py` & `byteplus-sdk-1.0.9/byteplus_sdk/example/cdn/describe_accounting_data.py`

 * *Files identical despite different names*

### Comparing `byteplus-sdk-1.0.8/byteplus_sdk/example/cdn/describe_cdn_origin_data.py` & `byteplus-sdk-1.0.9/byteplus_sdk/example/cdn/describe_cdn_origin_data.py`

 * *Files identical despite different names*

### Comparing `byteplus-sdk-1.0.8/byteplus_sdk/example/cdn/describe_edge_nrt_data_summary.py` & `byteplus-sdk-1.0.9/byteplus_sdk/example/cdn/describe_edge_nrt_data_summary.py`

 * *Files identical despite different names*

### Comparing `byteplus-sdk-1.0.8/byteplus_sdk/example/cdn/add_resource_tags.py` & `byteplus-sdk-1.0.9/byteplus_sdk/example/cdn/describe_cdn_data.py`

 * *Files 17% similar despite different names*

```diff
@@ -1,22 +1,29 @@
 #  -*- coding: utf-8 -*-
 import sys
 import os
 sys.path.append(os.path.dirname(os.path.realpath(__file__))+"/../../../")
+import datetime
 
 from byteplus_sdk.example.cdn import ak, sk
 from byteplus_sdk.cdn.service import CDNService
 
 if __name__ == '__main__':
     svc = CDNService()
     svc.set_ak(ak)
     svc.set_sk(sk)
-
+    now = int(datetime.datetime.now().strftime("%s"))
     body = {
-        'Resources': ['example.com', 'example1.com'],
-        'ResourceTags': [
-            {'Key': 'userKey', 'Value': 'userVal'}
-        ]
+        'StartTime': now - 86400,
+        'EndTime': now,
+        'Metric': 'pv',
+        'Domain': 'example.com',
+        'Interval': '5min',
+        'Isp': 'CT',
+        'Region': 'BJ',
+        'Protocol': 'http',
+        'IpVersion': 'ipv4',
+        "OnlyTotal": True
     }
 
-    resp = svc.add_resource_tags(body)
+    resp = svc.describe_cdn_data(body)
     print(resp)
```

### Comparing `byteplus-sdk-1.0.8/byteplus_sdk/example/cdn/add_cdn_domain.py` & `byteplus-sdk-1.0.9/byteplus_sdk/example/cdn/add_cdn_domain.py`

 * *Files identical despite different names*

### Comparing `byteplus-sdk-1.0.8/byteplus_sdk/example/cdn/describe_edge_top_nrt_data.py` & `byteplus-sdk-1.0.9/byteplus_sdk/example/cdn/describe_edge_top_nrt_data.py`

 * *Files identical despite different names*

### Comparing `byteplus-sdk-1.0.8/byteplus_sdk/example/cdn/describe_cdn_access_log.py` & `byteplus-sdk-1.0.9/byteplus_sdk/example/cdn/describe_cdn_access_log.py`

 * *Files identical despite different names*

### Comparing `byteplus-sdk-1.0.8/byteplus_sdk/example/cdn/describe_cdn_detail.py` & `byteplus-sdk-1.0.9/byteplus_sdk/example/cdn/describe_cdn_detail.py`

 * *Files identical despite different names*

### Comparing `byteplus-sdk-1.0.8/byteplus_sdk/example/cdn/describe_origin_top_nrt_data.py` & `byteplus-sdk-1.0.9/byteplus_sdk/example/cdn/describe_origin_top_nrt_data.py`

 * *Files identical despite different names*

### Comparing `byteplus-sdk-1.0.8/byteplus_sdk/example/cdn/describe_cdn_data.py` & `byteplus-sdk-1.0.9/byteplus_sdk/example/cdn/describe_edge_top_statistical_data.py`

 * *Files 13% similar despite different names*

```diff
@@ -11,19 +11,15 @@
     svc = CDNService()
     svc.set_ak(ak)
     svc.set_sk(sk)
     now = int(datetime.datetime.now().strftime("%s"))
     body = {
         'StartTime': now - 86400,
         'EndTime': now,
-        'Metric': 'pv',
+        'Metric': 'clientip',
         'Domain': 'example.com',
-        'Interval': '5min',
-        'Isp': 'CT',
-        'Region': 'BJ',
-        'Protocol': 'http',
-        'IpVersion': 'ipv4',
-        "OnlyTotal": True
+        'Item': 'region'
     }
+    print(body)
 
-    resp = svc.describe_cdn_data(body)
+    resp = svc.describe_edge_top_statistical_data(body)
     print(resp)
```

### Comparing `byteplus-sdk-1.0.8/byteplus_sdk/example/cdn/describe_edge_top_statistical_data.py` & `byteplus-sdk-1.0.9/byteplus_sdk/example/cdn/describe_content_block_tasks.py`

 * *Files 12% similar despite different names*

```diff
@@ -9,17 +9,15 @@
 
 if __name__ == '__main__':
     svc = CDNService()
     svc.set_ak(ak)
     svc.set_sk(sk)
     now = int(datetime.datetime.now().strftime("%s"))
     body = {
+        'TaskType': 'block_url',
         'StartTime': now - 86400,
         'EndTime': now,
-        'Metric': 'clientip',
-        'Domain': 'example.com',
-        'Item': 'region'
     }
     print(body)
 
-    resp = svc.describe_edge_top_statistical_data(body)
+    resp = svc.describe_content_block_tasks(body)
     print(resp)
```

### Comparing `byteplus-sdk-1.0.8/byteplus_sdk/example/cdn/describe_content_block_tasks.py` & `byteplus-sdk-1.0.9/byteplus_sdk/example/cdn/describe_origin_nrt_data_summary.py`

 * *Files 5% similar despite different names*

```diff
@@ -9,15 +9,15 @@
 
 if __name__ == '__main__':
     svc = CDNService()
     svc.set_ak(ak)
     svc.set_sk(sk)
     now = int(datetime.datetime.now().strftime("%s"))
     body = {
-        'TaskType': 'block_url',
         'StartTime': now - 86400,
         'EndTime': now,
+        'Metric': 'pv',
     }
     print(body)
 
-    resp = svc.describe_content_block_tasks(body)
+    resp = svc.describe_origin_nrt_data_summary(body)
     print(resp)
```

### Comparing `byteplus-sdk-1.0.8/byteplus_sdk/example/cdn/describe_origin_nrt_data_summary.py` & `byteplus-sdk-1.0.9/byteplus_sdk/example/cdn/describe_cdn_data_detail.py`

 * *Files 9% similar despite different names*

```diff
@@ -1,23 +1,25 @@
 #  -*- coding: utf-8 -*-
-import sys
 import os
-sys.path.append(os.path.dirname(os.path.realpath(__file__))+"/../../../")
-import datetime
+import sys
+import datetime 
+
+sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../../../")
 
 from byteplus_sdk.example.cdn import ak, sk
 from byteplus_sdk.cdn.service import CDNService
 
 if __name__ == '__main__':
     svc = CDNService()
     svc.set_ak(ak)
     svc.set_sk(sk)
+
     now = int(datetime.datetime.now().strftime("%s"))
     body = {
-        'StartTime': now - 86400,
+        'StartTime': now - 600,
         'EndTime': now,
-        'Metric': 'pv',
+        'Metric': 'flux',
+        'Domain': 'example.com',
     }
-    print(body)
 
-    resp = svc.describe_origin_nrt_data_summary(body)
+    resp = svc.describe_cdn_data_detail(body)
     print(resp)
```

### Comparing `byteplus-sdk-1.0.8/byteplus_sdk/example/cdn/describe_edge_top_status_code.py` & `byteplus-sdk-1.0.9/byteplus_sdk/example/cdn/describe_edge_top_status_code.py`

 * *Files identical despite different names*

### Comparing `byteplus-sdk-1.0.8/byteplus_sdk/example/visual/example_common.py` & `byteplus-sdk-1.0.9/byteplus_sdk/example/visual/example_common.py`

 * *Files identical despite different names*

### Comparing `byteplus-sdk-1.0.8/byteplus_sdk/Policy.py` & `byteplus-sdk-1.0.9/byteplus_sdk/Policy.py`

 * *Files identical despite different names*

### Comparing `byteplus-sdk-1.0.8/byteplus_sdk/const/Const.py` & `byteplus-sdk-1.0.9/byteplus_sdk/const/Const.py`

 * *Files identical despite different names*

### Comparing `byteplus-sdk-1.0.8/byteplus_sdk/iam/IamService.py` & `byteplus-sdk-1.0.9/byteplus_sdk/iam/IamService.py`

 * *Files identical despite different names*

### Comparing `byteplus-sdk-1.0.8/byteplus_sdk/cdn/service.py` & `byteplus-sdk-1.0.9/byteplus_sdk/cdn/service.py`

 * *Files 3% similar despite different names*

```diff
@@ -1,24 +1,24 @@
-# coding=utf-8
+#  -*- coding: utf-8 -*-
 import json
 import threading
+
 from byteplus_sdk.ApiInfo import ApiInfo
 from byteplus_sdk.Credentials import Credentials
 from byteplus_sdk.base.Service import Service
 from byteplus_sdk.ServiceInfo import ServiceInfo
 
 SERVICE_VERSION = "2021-03-01"
 
 service_info_map = {
-    "ap-singapore-1": ServiceInfo("open.byteplusapi.com", {'Accept': 'application/json', },
-                                  Credentials('', '', "CDN", "ap-singapore-1"), 60 * 1, 60 * 5, 'https'),
+    "ap-singapore-1": ServiceInfo("open.byteplusapi.com", {'accept': 'application/json', },
+                              Credentials('', '', "CDN", "ap-singapore-1"), 60 * 1, 60 * 5, "https"),
 }
 
 api_info = {
-
     "AddCdnDomain": ApiInfo("POST", "/", {
         "Action": "AddCdnDomain", "Version": SERVICE_VERSION}, {}, {}),
 
     "StartCdnDomain": ApiInfo("POST", "/", {
         "Action": "StartCdnDomain", "Version": SERVICE_VERSION}, {}, {}),
 
     "StopCdnDomain": ApiInfo("POST", "/", {
@@ -68,17 +68,14 @@
 
     "DescribeEdgeTopStatisticalData": ApiInfo("POST", "/", {
         "Action": "DescribeEdgeTopStatisticalData", "Version": SERVICE_VERSION}, {}, {}),
 
     "DescribeCdnRegionAndIsp": ApiInfo("POST", "/", {
         "Action": "DescribeCdnRegionAndIsp", "Version": SERVICE_VERSION}, {}, {}),
 
-    "DescribeCdnDomainTopData": ApiInfo("POST", "/", {
-        "Action": "DescribeCdnDomainTopData", "Version": SERVICE_VERSION}, {}, {}),
-
     "DescribeCdnService": ApiInfo("POST", "/", {
         "Action": "DescribeCdnService", "Version": SERVICE_VERSION}, {}, {}),
 
     "DescribeAccountingData": ApiInfo("POST", "/", {
         "Action": "DescribeAccountingData", "Version": SERVICE_VERSION}, {}, {}),
 
     "SubmitRefreshTask": ApiInfo("POST", "/", {
@@ -109,14 +106,31 @@
         "Action": "DescribeIPInfo", "Version": SERVICE_VERSION}, {}, {}),
 
     "DescribeIPListInfo": ApiInfo("POST", "/", {
         "Action": "DescribeIPListInfo", "Version": SERVICE_VERSION}, {}, {}),
 
     "DescribeCdnUpperIp": ApiInfo("POST", "/", {
         "Action": "DescribeCdnUpperIp", "Version": SERVICE_VERSION}, {}, {}),
+
+    "AddCdnCertificate": ApiInfo("POST", "/", {
+        "Action": "AddCdnCertificate", "Version": SERVICE_VERSION}, {}, {}),
+
+    "ListCertInfo": ApiInfo("POST", "/", {
+        "Action": "ListCertInfo", "Version": SERVICE_VERSION}, {}, {}),
+
+    "ListCdnCertInfo": ApiInfo("POST", "/", {
+        "Action": "ListCdnCertInfo", "Version": SERVICE_VERSION}, {}, {}),
+
+    "DescribeCertConfig": ApiInfo("POST", "/", {
+        "Action": "DescribeCertConfig", "Version": SERVICE_VERSION}, {}, {}),
+
+    "BatchDeployCert": ApiInfo("POST", "/", {
+        "Action": "BatchDeployCert", "Version": SERVICE_VERSION}, {}, {}),
+
+
 }
 
 
 class CDNService(Service):
     _instance_lock = threading.Lock()
 
     def __new__(cls, *args, **kwargs):
@@ -328,24 +342,14 @@
         action = "DescribeCdnRegionAndIsp"
         res = self.json(action, [], params)
         if res == '':
             raise Exception("%s: empty response" % action)
         res_json = json.loads(res)
         return res_json
 
-    def describe_cdn_domain_top_data(self, params=None):
-        if params is None:
-            params = {}
-        action = "DescribeCdnDomainTopData"
-        res = self.json(action, [], params)
-        if res == '':
-            raise Exception("%s: empty response" % action)
-        res_json = json.loads(res)
-        return res_json
-
     def describe_cdn_service(self, params=None):
         if params is None:
             params = {}
         action = "DescribeCdnService"
         res = self.json(action, [], params)
         if res == '':
             raise Exception("%s: empty response" % action)
@@ -471,7 +475,57 @@
             params = {}
         action = "DescribeCdnUpperIp"
         res = self.json(action, [], params)
         if res == '':
             raise Exception("%s: empty response" % action)
         res_json = json.loads(res)
         return res_json
+
+    def add_cdn_certificate(self, params=None):
+        if params is None:
+            params = {}
+        action = "AddCdnCertificate"
+        res = self.json(action, [], params)
+        if res == '':
+            raise Exception("%s: empty response" % action)
+        res_json = json.loads(res)
+        return res_json
+
+    def list_cert_info(self, params=None):
+        if params is None:
+            params = {}
+        action = "ListCertInfo"
+        res = self.json(action, [], params)
+        if res == '':
+            raise Exception("%s: empty response" % action)
+        res_json = json.loads(res)
+        return res_json
+
+    def list_cdn_cert_info(self, params=None):
+        if params is None:
+            params = {}
+        action = "ListCdnCertInfo"
+        res = self.json(action, [], params)
+        if res == '':
+            raise Exception("%s: empty response" % action)
+        res_json = json.loads(res)
+        return res_json
+
+    def describe_cert_config(self, params=None):
+        if params is None:
+            params = {}
+        action = "DescribeCertConfig"
+        res = self.json(action, [], params)
+        if res == '':
+            raise Exception("%s: empty response" % action)
+        res_json = json.loads(res)
+        return res_json
+
+    def batch_deploy_cert(self, params=None):
+        if params is None:
+            params = {}
+        action = "BatchDeployCert"
+        res = self.json(action, [], params)
+        if res == '':
+            raise Exception("%s: empty response" % action)
+        res_json = json.loads(res)
+        return res_json
```

### Comparing `byteplus-sdk-1.0.8/byteplus_sdk/visual/VisualService.py` & `byteplus-sdk-1.0.9/byteplus_sdk/visual/VisualService.py`

 * *Files identical despite different names*

### Comparing `byteplus-sdk-1.0.8/byteplus_sdk/base/Service.py` & `byteplus-sdk-1.0.9/byteplus_sdk/base/Service.py`

 * *Files identical despite different names*

### Comparing `byteplus-sdk-1.0.8/byteplus_sdk/base/Request.py` & `byteplus-sdk-1.0.9/byteplus_sdk/base/Request.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-# coding : utf-8
+# coding: utf-8
 from collections import OrderedDict
 
 try:
     from urllib import urlencode
 except:
     from urllib.parse import urlencode
```

### Comparing `byteplus-sdk-1.0.8/byteplus_sdk.egg-info/SOURCES.txt` & `byteplus-sdk-1.0.9/byteplus_sdk.egg-info/SOURCES.txt`

 * *Files 2% similar despite different names*

```diff
@@ -18,47 +18,50 @@
 byteplus_sdk/base/__init__.py
 byteplus_sdk/cdn/__init__.py
 byteplus_sdk/cdn/service.py
 byteplus_sdk/const/Const.py
 byteplus_sdk/const/__init__.py
 byteplus_sdk/example/__init__.py
 byteplus_sdk/example/cdn/__init__.py
+byteplus_sdk/example/cdn/add_cdn_certificate.py
 byteplus_sdk/example/cdn/add_cdn_domain.py
-byteplus_sdk/example/cdn/add_resource_tags.py
 byteplus_sdk/example/cdn/delete_cdn_domain.py
 byteplus_sdk/example/cdn/describe_accounting_data.py
 byteplus_sdk/example/cdn/describe_cdn_access_log.py
 byteplus_sdk/example/cdn/describe_cdn_config.py
 byteplus_sdk/example/cdn/describe_cdn_data.py
+byteplus_sdk/example/cdn/describe_cdn_data_detail.py
 byteplus_sdk/example/cdn/describe_cdn_detail.py
-byteplus_sdk/example/cdn/describe_cdn_domain_top_data.py
 byteplus_sdk/example/cdn/describe_cdn_origin_data.py
 byteplus_sdk/example/cdn/describe_cdn_region_and_isp.py
 byteplus_sdk/example/cdn/describe_cdn_service.py
 byteplus_sdk/example/cdn/describe_cdn_upper_ip.py
 byteplus_sdk/example/cdn/describe_content_block_tasks.py
 byteplus_sdk/example/cdn/describe_content_quota.py
 byteplus_sdk/example/cdn/describe_content_tasks.py
 byteplus_sdk/example/cdn/describe_edge_nrt_data_summary.py
 byteplus_sdk/example/cdn/describe_edge_statistical_data.py
 byteplus_sdk/example/cdn/describe_edge_top_nrt_data.py
 byteplus_sdk/example/cdn/describe_edge_top_statistical_data.py
 byteplus_sdk/example/cdn/describe_edge_top_status_code.py
 byteplus_sdk/example/cdn/describe_ip_info.py
-byteplus_sdk/example/cdn/describe_iplist_info.py
+byteplus_sdk/example/cdn/describe_ip_list_info.py
 byteplus_sdk/example/cdn/describe_origin_nrt_data_summary.py
 byteplus_sdk/example/cdn/describe_origin_top_nrt_data.py
 byteplus_sdk/example/cdn/describe_origin_top_status_code.py
+byteplus_sdk/example/cdn/list_cdn_cert_info.py
 byteplus_sdk/example/cdn/list_cdn_domains.py
+byteplus_sdk/example/cdn/list_cert_info.py
 byteplus_sdk/example/cdn/start_cdn_domain.py
 byteplus_sdk/example/cdn/stop_cdn_domain.py
 byteplus_sdk/example/cdn/submit_block_task.py
 byteplus_sdk/example/cdn/submit_preload_task.py
 byteplus_sdk/example/cdn/submit_refresh_task.py
 byteplus_sdk/example/cdn/submit_unblock_task.py
+byteplus_sdk/example/cdn/update_cdn_config.py
 byteplus_sdk/example/visual/__init__.py
 byteplus_sdk/example/visual/example_common.py
 byteplus_sdk/iam/IamService.py
 byteplus_sdk/iam/__init__.py
 byteplus_sdk/sms/SmsService.py
 byteplus_sdk/sms/__init__.py
 byteplus_sdk/util/Functions.py
```

