# Comparing `tmp/volcengine-1.0.84.tar.gz` & `tmp/volcengine-1.0.9.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "dist/volcengine-1.0.84.tar", last modified: Thu Apr  6 14:55:35 2023, max compression
+gzip compressed data, was "dist/volcengine-1.0.9.tar", last modified: Thu Apr  8 02:37:18 2021, max compression
```

## Comparing `volcengine-1.0.84.tar` & `volcengine-1.0.9.tar`

### file list

```diff
@@ -1,694 +1,138 @@
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 14:55:35.000000 volcengine-1.0.84/
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 14:55:35.000000 volcengine-1.0.84/volcengine.egg-info/
--rw-r--r--   0 root         (0) root         (0)       11 2023-04-06 14:55:35.000000 volcengine-1.0.84/volcengine.egg-info/top_level.txt
--rw-r--r--   0 root         (0) root         (0)      293 2023-04-06 14:55:35.000000 volcengine-1.0.84/volcengine.egg-info/PKG-INFO
--rw-r--r--   0 root         (0) root         (0)    30244 2023-04-06 14:55:35.000000 volcengine-1.0.84/volcengine.egg-info/SOURCES.txt
--rw-r--r--   0 root         (0) root         (0)        1 2023-04-06 14:55:35.000000 volcengine-1.0.84/volcengine.egg-info/dependency_links.txt
--rw-r--r--   0 root         (0) root         (0)       58 2023-04-06 14:55:35.000000 volcengine-1.0.84/volcengine.egg-info/requires.txt
--rw-r--r--   0 root         (0) root         (0)      730 2023-04-06 14:55:33.000000 volcengine-1.0.84/setup.py
--rw-r--r--   0 root         (0) root         (0)      293 2023-04-06 14:55:35.000000 volcengine-1.0.84/PKG-INFO
--rw-r--r--   0 root         (0) root         (0)       59 2023-04-06 14:55:35.000000 volcengine-1.0.84/setup.cfg
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 14:55:35.000000 volcengine-1.0.84/volcengine/
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 14:55:35.000000 volcengine-1.0.84/volcengine/iam/
--rw-r--r--   0 root         (0) root         (0)        0 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/iam/__init__.py
--rw-r--r--   0 root         (0) root         (0)    13316 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/iam/IamService.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 14:55:35.000000 volcengine-1.0.84/volcengine/image_registry/
--rw-r--r--   0 root         (0) root         (0)        0 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/image_registry/__init__.py
--rw-r--r--   0 root         (0) root         (0)     9173 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/image_registry/ImageRegistryService.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 14:55:35.000000 volcengine-1.0.84/volcengine/dcdn/
--rw-r--r--   0 root         (0) root         (0)        0 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/dcdn/__init__.py
--rw-r--r--   0 root         (0) root         (0)    15998 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/dcdn/DCDNService.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 14:55:35.000000 volcengine-1.0.84/volcengine/billing/
--rw-r--r--   0 root         (0) root         (0)        0 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/billing/__init__.py
--rw-r--r--   0 root         (0) root         (0)     2291 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/billing/BillingService.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 14:55:35.000000 volcengine-1.0.84/volcengine/code_pipeline/
--rw-r--r--   0 root         (0) root         (0)        0 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/code_pipeline/__init__.py
--rw-r--r--   0 root         (0) root         (0)    13140 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/code_pipeline/CodePipelineService.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 14:55:35.000000 volcengine-1.0.84/volcengine/cdn/
--rw-r--r--   0 root         (0) root         (0)        0 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/cdn/__init__.py
--rw-r--r--   0 root         (0) root         (0)    24455 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/cdn/service.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 14:55:35.000000 volcengine-1.0.84/volcengine/vedit/
--rw-r--r--   0 root         (0) root         (0)        0 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/vedit/__init__.py
--rw-r--r--   0 root         (0) root         (0)     2731 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/vedit/VEditService.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 14:55:35.000000 volcengine-1.0.84/volcengine/vod/
--rw-r--r--   0 root         (0) root         (0)        0 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/vod/__init__.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 14:55:35.000000 volcengine-1.0.84/volcengine/vod/models/
--rw-r--r--   0 root         (0) root         (0)        0 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/vod/models/__init__.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 14:55:35.000000 volcengine-1.0.84/volcengine/vod/models/response/
--rw-r--r--   0 root         (0) root         (0)        0 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/vod/models/response/__init__.py
--rw-r--r--   0 root         (0) root         (0)    69254 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/vod/models/response/response_vod_pb2.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 14:55:35.000000 volcengine-1.0.84/volcengine/vod/models/request/
--rw-r--r--   0 root         (0) root         (0)        0 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/vod/models/request/__init__.py
--rw-r--r--   0 root         (0) root         (0)    69925 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/vod/models/request/request_vod_pb2.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 14:55:35.000000 volcengine-1.0.84/volcengine/vod/models/business/
--rw-r--r--   0 root         (0) root         (0)        0 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/vod/models/business/__init__.py
--rw-r--r--   0 root         (0) root         (0)    16138 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/vod/models/business/vod_common_pb2.py
--rw-r--r--   0 root         (0) root         (0)    25019 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/vod/models/business/vod_measure_pb2.py
--rw-r--r--   0 root         (0) root         (0)    23277 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/vod/models/business/vod_upload_pb2.py
--rw-r--r--   0 root         (0) root         (0)     3416 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/vod/models/business/vod_edit_pb2.py
--rw-r--r--   0 root         (0) root         (0)    22584 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/vod/models/business/vod_cdn_pb2.py
--rw-r--r--   0 root         (0) root         (0)    28824 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/vod/models/business/vod_workflow_pb2.py
--rw-r--r--   0 root         (0) root         (0)     6189 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/vod/models/business/vod_play_pb2.py
--rw-r--r--   0 root         (0) root         (0)     2052 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/vod/models/business/vod_apps_manage_pb2.py
--rw-r--r--   0 root         (0) root         (0)     1848 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/vod/models/business/vod_callback_pb2.py
--rw-r--r--   0 root         (0) root         (0)    33051 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/vod/models/business/vod_media_pb2.py
--rw-r--r--   0 root         (0) root         (0)     4332 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/vod/models/business/vod_smart_strategy_pb2.py
--rw-r--r--   0 root         (0) root         (0)     4524 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/vod/models/business/vod_space_pb2.py
--rw-r--r--   0 root         (0) root         (0)   106666 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/vod/VodService.py
--rw-r--r--   0 root         (0) root         (0)    10577 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/vod/VodServiceConfig.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 14:55:35.000000 volcengine-1.0.84/volcengine/sms/
--rw-r--r--   0 root         (0) root         (0)        0 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/sms/__init__.py
--rw-r--r--   0 root         (0) root         (0)     8664 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/sms/SmsService.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 14:55:35.000000 volcengine-1.0.84/volcengine/util/
--rw-r--r--   0 root         (0) root         (0)        0 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/util/__init__.py
--rw-r--r--   0 root         (0) root         (0)     4094 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/util/Util.py
--rw-r--r--   0 root         (0) root         (0)     1176 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/util/Functions.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 14:55:35.000000 volcengine-1.0.84/volcengine/base/
--rw-r--r--   0 root         (0) root         (0)     9372 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/base/Service.py
--rw-r--r--   0 root         (0) root         (0)        0 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/base/__init__.py
--rw-r--r--   0 root         (0) root         (0)     1232 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/base/Request.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 14:55:35.000000 volcengine-1.0.84/volcengine/base/models/
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 14:55:35.000000 volcengine-1.0.84/volcengine/base/models/base/
--rw-r--r--   0 root         (0) root         (0)     2736 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/base/models/base/base_pb2.py
--rw-r--r--   0 root         (0) root         (0)        0 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/base/models/base/__init__.py
--rw-r--r--   0 root         (0) root         (0)        0 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/base/models/__init__.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 14:55:35.000000 volcengine-1.0.84/volcengine/base/models/business/
--rw-r--r--   0 root         (0) root         (0)     3671 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/base/models/business/deny_config_pb2.py
--rw-r--r--   0 root         (0) root         (0)     3870 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/base/models/business/pull_to_push_pb2.py
--rw-r--r--   0 root         (0) root         (0)     3128 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/base/models/business/record_manage_pb2.py
--rw-r--r--   0 root         (0) root         (0)        0 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/base/models/business/__init__.py
--rw-r--r--   0 root         (0) root         (0)     2942 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/base/models/business/domain_pb2.py
--rw-r--r--   0 root         (0) root         (0)     4484 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/base/models/business/relay_source_pb2.py
--rw-r--r--   0 root         (0) root         (0)     3594 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/base/models/business/snapshot_manage_pb2.py
--rw-r--r--   0 root         (0) root         (0)     6454 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/base/models/business/stream_manage_pb2.py
--rw-r--r--   0 root         (0) root         (0)     5225 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/base/models/business/VQScore_pb2.py
--rw-r--r--   0 root         (0) root         (0)     3922 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/base/models/business/addr_pb2.py
--rw-r--r--   0 root         (0) root         (0)       33 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/__init__.py
--rw-r--r--   0 root         (0) root         (0)      444 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/Credentials.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 14:55:35.000000 volcengine-1.0.84/volcengine/notify/
--rw-r--r--   0 root         (0) root         (0)        0 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/notify/__init__.py
--rw-r--r--   0 root         (0) root         (0)    11061 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/notify/notify.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 14:55:35.000000 volcengine-1.0.84/volcengine/adblocker/
--rw-r--r--   0 root         (0) root         (0)        0 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/adblocker/__init__.py
--rw-r--r--   0 root         (0) root         (0)     1654 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/adblocker/AdBlockerService.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 14:55:35.000000 volcengine-1.0.84/volcengine/imagex/
--rw-r--r--   0 root         (0) root         (0)     3494 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/imagex/__init__.py
--rw-r--r--   0 root         (0) root         (0)     8416 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/imagex/ImageXConfig.py
--rw-r--r--   0 root         (0) root         (0)    39674 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/imagex/ImageXService.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 14:55:35.000000 volcengine-1.0.84/volcengine/imp/
--rw-r--r--   0 root         (0) root         (0)     4260 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/imp/ImpService.py
--rw-r--r--   0 root         (0) root         (0)        0 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/imp/__init__.py
--rw-r--r--   0 root         (0) root         (0)     2061 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/imp/ImpServiceConfig.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 14:55:35.000000 volcengine-1.0.84/volcengine/imp/models/
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 14:55:35.000000 volcengine-1.0.84/volcengine/imp/models/base/
--rw-r--r--   0 root         (0) root         (0)     7196 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/imp/models/base/base_pb2.py
--rw-r--r--   0 root         (0) root         (0)        0 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/imp/models/base/__init__.py
--rw-r--r--   0 root         (0) root         (0)        0 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/imp/models/__init__.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 14:55:35.000000 volcengine-1.0.84/volcengine/imp/models/response/
--rw-r--r--   0 root         (0) root         (0)        0 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/imp/models/response/__init__.py
--rw-r--r--   0 root         (0) root         (0)     9927 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/imp/models/response/response_imp_pb2.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 14:55:35.000000 volcengine-1.0.84/volcengine/imp/models/request/
--rw-r--r--   0 root         (0) root         (0)        0 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/imp/models/request/__init__.py
--rw-r--r--   0 root         (0) root         (0)     7112 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/imp/models/request/request_imp_pb2.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 14:55:35.000000 volcengine-1.0.84/volcengine/imp/models/business/
--rw-r--r--   0 root         (0) root         (0)        0 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/imp/models/business/__init__.py
--rw-r--r--   0 root         (0) root         (0)    14236 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/imp/models/business/imp_common_pb2.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 14:55:35.000000 volcengine-1.0.84/volcengine/const/
--rw-r--r--   0 root         (0) root         (0)     1937 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/const/Const.py
--rw-r--r--   0 root         (0) root         (0)        0 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/const/__init__.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 14:55:35.000000 volcengine-1.0.84/volcengine/visual/
--rw-r--r--   0 root         (0) root         (0)        0 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/visual/__init__.py
--rw-r--r--   0 root         (0) root         (0)    32492 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/visual/VisualService.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 14:55:35.000000 volcengine-1.0.84/volcengine/auth/
--rw-r--r--   0 root         (0) root         (0)      698 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/auth/MetaData.py
--rw-r--r--   0 root         (0) root         (0)      886 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/auth/SignParam.py
--rw-r--r--   0 root         (0) root         (0)        0 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/auth/__init__.py
--rw-r--r--   0 root         (0) root         (0)      444 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/auth/SignResult.py
--rw-r--r--   0 root         (0) root         (0)     8531 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/auth/SignerV4.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 14:55:35.000000 volcengine-1.0.84/volcengine/nlp/
--rw-r--r--   0 root         (0) root         (0)        0 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/nlp/__init__.py
--rw-r--r--   0 root         (0) root         (0)     4044 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/nlp/NLPService.py
--rw-r--r--   0 root         (0) root         (0)      323 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/ApiInfo.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 14:55:35.000000 volcengine-1.0.84/volcengine/livesaas/
--rw-r--r--   0 root         (0) root         (0)    15125 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/livesaas/LivesaasService.py
--rw-r--r--   0 root         (0) root         (0)        0 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/livesaas/__init__.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 14:55:35.000000 volcengine-1.0.84/volcengine/verender/
--rw-r--r--   0 root         (0) root         (0)        0 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/verender/__init__.py
--rw-r--r--   0 root         (0) root         (0)    30090 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/verender/VerenderService.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 14:55:35.000000 volcengine-1.0.84/volcengine/content_security/
--rw-r--r--   0 root         (0) root         (0)        0 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/content_security/__init__.py
--rw-r--r--   0 root         (0) root         (0)    10533 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/content_security/ContentSecurityService.py
--rw-r--r--   0 root         (0) root         (0)     2592 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/Policy.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 14:55:35.000000 volcengine-1.0.84/volcengine/example/
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 14:55:35.000000 volcengine-1.0.84/volcengine/example/rtc/
--rw-r--r--   0 root         (0) root         (0)     2020 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/rtc/example_start_record.py
--rw-r--r--   0 root         (0) root         (0)        0 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/rtc/__init__.py
--rw-r--r--   0 root         (0) root         (0)      620 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/rtc/example_get_record_task.py
--rw-r--r--   0 root         (0) root         (0)      691 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/rtc/example_stop_reocrd.py
--rw-r--r--   0 root         (0) root         (0)     2137 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/rtc/RtcService.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 14:55:35.000000 volcengine-1.0.84/volcengine/example/dcdn/
--rw-r--r--   0 root         (0) root         (0)      488 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/dcdn/stop_domain.py
--rw-r--r--   0 root         (0) root         (0)      499 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/dcdn/describe_domain_config.py
--rw-r--r--   0 root         (0) root         (0)      580 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/dcdn/describe_domain_logs.py
--rw-r--r--   0 root         (0) root         (0)      490 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/dcdn/delete_domain.py
--rw-r--r--   0 root         (0) root         (0)      497 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/dcdn/describe_dcdn_region_and_isp.py
--rw-r--r--   0 root         (0) root         (0)       16 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/dcdn/__init__.py
--rw-r--r--   0 root         (0) root         (0)      584 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/dcdn/describe_domain_isp_data.py
--rw-r--r--   0 root         (0) root         (0)      569 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/dcdn/describe_top_ips.py
--rw-r--r--   0 root         (0) root         (0)      574 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/dcdn/describe_top_domains.py
--rw-r--r--   0 root         (0) root         (0)      727 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/dcdn/describe_origin_statistics_detail.py
--rw-r--r--   0 root         (0) root         (0)      511 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/dcdn/describe_user_domains.py
--rw-r--r--   0 root         (0) root         (0)      489 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/dcdn/start_domain.py
--rw-r--r--   0 root         (0) root         (0)      526 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/dcdn/retry_purge_prefetch_task.py
--rw-r--r--   0 root         (0) root         (0)      469 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/dcdn/get_purge_prefetch_task_quota.py
--rw-r--r--   0 root         (0) root         (0)      613 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/dcdn/describe_realtime_data.py
--rw-r--r--   0 root         (0) root         (0)      720 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/dcdn/describe_statistics_detail.py
--rw-r--r--   0 root         (0) root         (0)      811 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/dcdn/update_domain_config.py
--rw-r--r--   0 root         (0) root         (0)      588 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/dcdn/describe_domain_region_data.py
--rw-r--r--   0 root         (0) root         (0)      570 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/dcdn/describe_top_urls.py
--rw-r--r--   0 root         (0) root         (0)      583 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/dcdn/describe_domain_pv_data.py
--rw-r--r--   0 root         (0) root         (0)      574 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/dcdn/describe_top_referers.py
--rw-r--r--   0 root         (0) root         (0)      583 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/dcdn/describe_domain_uv_data.py
--rw-r--r--   0 root         (0) root         (0)      643 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/dcdn/describe_origin_statistics.py
--rw-r--r--   0 root         (0) root         (0)      635 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/dcdn/describe_statistics.py
--rw-r--r--   0 root         (0) root         (0)      557 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/dcdn/create_purge_prefetch_task.py
--rw-r--r--   0 root         (0) root         (0)      734 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/dcdn/check_purge_prefetch_task.py
--rw-r--r--   0 root         (0) root         (0)      947 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/dcdn/create_domain.py
--rw-r--r--   0 root         (0) root         (0)      621 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/dcdn/describe_origin_realtime_data.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 14:55:35.000000 volcengine-1.0.84/volcengine/example/cdn/
--rw-r--r--   0 root         (0) root         (0)      705 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/cdn/add_cdn_certificate.py
--rw-r--r--   0 root         (0) root         (0)      354 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/cdn/list_resource_tags.py
--rw-r--r--   0 root         (0) root         (0)      669 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/cdn/describe_district_isp_data.py
--rw-r--r--   0 root         (0) root         (0)      570 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/cdn/describe_accounting_data.py
--rw-r--r--   0 root         (0) root         (0)      860 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/cdn/update_cdn_config.py
--rw-r--r--   0 root         (0) root         (0)      448 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/cdn/submit_unblock_task.py
--rw-r--r--   0 root         (0) root         (0)      411 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/cdn/list_cert_info.py
--rw-r--r--   0 root         (0) root         (0)      417 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/cdn/describe_ip_list_info.py
--rw-r--r--   0 root         (0) root         (0)      400 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/cdn/describe_ip_info.py
--rw-r--r--   0 root         (0) root         (0)      426 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/cdn/describe_cdn_region_and_isp.py
--rw-r--r--   0 root         (0) root         (0)       16 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/cdn/__init__.py
--rw-r--r--   0 root         (0) root         (0)      448 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/cdn/submit_preload_task.py
--rw-r--r--   0 root         (0) root         (0)      521 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/cdn/update_resource_tags.py
--rw-r--r--   0 root         (0) root         (0)      436 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/cdn/batch_deploy_cert.py
--rw-r--r--   0 root         (0) root         (0)      909 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/cdn/add_cdn_domain.py
--rw-r--r--   0 root         (0) root         (0)      378 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/cdn/list_cdn_cert_info.py
--rw-r--r--   0 root         (0) root         (0)      410 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/cdn/delete_cdn_domain.py
--rw-r--r--   0 root         (0) root         (0)      564 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/cdn/describe_content_block_tasks.py
--rw-r--r--   0 root         (0) root         (0)      531 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/cdn/describe_edge_top_status_code.py
--rw-r--r--   0 root         (0) root         (0)      582 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/cdn/describe_origin_top_nrt_data.py
--rw-r--r--   0 root         (0) root         (0)      625 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/cdn/describe_edge_top_statistical_data.py
--rw-r--r--   0 root         (0) root         (0)      358 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/cdn/describe_content_quota.py
--rw-r--r--   0 root         (0) root         (0)      410 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/cdn/describe_cert_config.py
--rw-r--r--   0 root         (0) root         (0)      557 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/cdn/describe_edge_nrt_data_summary.py
--rw-r--r--   0 root         (0) root         (0)      533 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/cdn/describe_origin_top_status_code.py
--rw-r--r--   0 root         (0) root         (0)      408 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/cdn/stop_cdn_domain.py
--rw-r--r--   0 root         (0) root         (0)      596 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/cdn/describe_edge_statistical_data.py
--rw-r--r--   0 root         (0) root         (0)      543 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/cdn/describe_cdn_access_log.py
--rw-r--r--   0 root         (0) root         (0)      652 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/cdn/describe_cdn_data_detail.py
--rw-r--r--   0 root         (0) root         (0)      463 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/cdn/describe_content_tasks.py
--rw-r--r--   0 root         (0) root         (0)      521 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/cdn/delete_resource_tags.py
--rw-r--r--   0 root         (0) root         (0)      414 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/cdn/describe_cdn_upper_ip.py
--rw-r--r--   0 root         (0) root         (0)      446 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/cdn/submit_block_task.py
--rw-r--r--   0 root         (0) root         (0)      717 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/cdn/describe_cdn_data.py
--rw-r--r--   0 root         (0) root         (0)      409 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/cdn/start_cdn_domain.py
--rw-r--r--   0 root         (0) root         (0)      595 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/cdn/describe_cdn_origin_data.py
--rw-r--r--   0 root         (0) root         (0)      356 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/cdn/describe_cdn_service.py
--rw-r--r--   0 root         (0) root         (0)      559 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/cdn/describe_origin_nrt_data_summary.py
--rw-r--r--   0 root         (0) root         (0)      411 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/cdn/describe_cdn_config.py
--rw-r--r--   0 root         (0) root         (0)      489 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/cdn/submit_refresh_task.py
--rw-r--r--   0 root         (0) root         (0)      613 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/cdn/describe_edge_top_nrt_data.py
--rw-r--r--   0 root         (0) root         (0)      518 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/cdn/add_resource_tags.py
--rw-r--r--   0 root         (0) root         (0)      452 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/cdn/list_cdn_domains.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 14:55:35.000000 volcengine-1.0.84/volcengine/example/vedit/
--rw-r--r--   0 root         (0) root         (0)        0 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/vedit/__init__.py
--rw-r--r--   0 root         (0) root         (0)     1220 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/vedit/example_edit.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 14:55:35.000000 volcengine-1.0.84/volcengine/example/vod/
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 14:55:35.000000 volcengine-1.0.84/volcengine/example/vod/cdn/
--rw-r--r--   0 root         (0) root         (0)      711 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/vod/cdn/CreateCdnRefreshTaskExample.py
--rw-r--r--   0 root         (0) root         (0)      678 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/vod/cdn/DescribeCdnIpExample.py
--rw-r--r--   0 root         (0) root         (0)        0 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/vod/cdn/__init__.py
--rw-r--r--   0 root         (0) root         (0)      744 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/vod/cdn/ListCdnPvDataExample.py
--rw-r--r--   0 root         (0) root         (0)      832 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/vod/cdn/DescribeVodDomainTrafficDataExample.py
--rw-r--r--   0 root         (0) root         (0)      756 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/vod/cdn/ListCdnStatusDataExample.py
--rw-r--r--   0 root         (0) root         (0)      753 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/vod/cdn/ListCdnUsageDataExample.py
--rw-r--r--   0 root         (0) root         (0)      803 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/vod/cdn/ListCdnTopAccessUrlExample.py
--rw-r--r--   0 root         (0) root         (0)      946 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/vod/cdn/ListCdnTasksExample.py
--rw-r--r--   0 root         (0) root         (0)      691 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/vod/cdn/ListDomainExample.py
--rw-r--r--   0 root         (0) root         (0)      724 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/vod/cdn/CreateCdnPreloadTaskExample.py
--rw-r--r--   0 root         (0) root         (0)      795 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/vod/cdn/ListCdnAccessLogExample.py
--rw-r--r--   0 root         (0) root         (0)      861 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/vod/cdn/DescribeVodDomainBandwidthDataExample.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 14:55:35.000000 volcengine-1.0.84/volcengine/example/vod/space/
--rw-r--r--   0 root         (0) root         (0)        0 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/vod/space/__init__.py
--rw-r--r--   0 root         (0) root         (0)      726 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/vod/space/CreateSpaceExample.py
--rw-r--r--   0 root         (0) root         (0)      732 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/vod/space/UpdateSpaceExample.py
--rw-r--r--   0 root         (0) root         (0)      634 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/vod/space/ListSpaceExample.py
--rw-r--r--   0 root         (0) root         (0)      859 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/vod/space/DescribeVodSpaceStorageDataExample.py
--rw-r--r--   0 root         (0) root         (0)      808 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/vod/space/UpdateSpaceUploadConfigExample.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 14:55:35.000000 volcengine-1.0.84/volcengine/example/vod/vedit/
--rw-r--r--   0 root         (0) root         (0)      622 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/vod/vedit/GetDirectEditProgress.py
--rw-r--r--   0 root         (0) root         (0)      625 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/vod/vedit/GetDirectEditResult.py
--rw-r--r--   0 root         (0) root         (0)        0 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/vod/vedit/__init__.py
--rw-r--r--   0 root         (0) root         (0)     1793 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/vod/vedit/SubmitDirectEditTaskAsync.py
--rw-r--r--   0 root         (0) root         (0)        0 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/vod/__init__.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 14:55:35.000000 volcengine-1.0.84/volcengine/example/vod/workflow/
--rw-r--r--   0 root         (0) root         (0)      795 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/vod/workflow/RetrieveTranscodeResultExample.py
--rw-r--r--   0 root         (0) root         (0)        0 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/vod/workflow/__init__.py
--rw-r--r--   0 root         (0) root         (0)      959 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/vod/workflow/WorkflowExample.py
--rw-r--r--   0 root         (0) root         (0)      747 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/vod/workflow/GetWorkflowExecutionResultExample.py
--rw-r--r--   0 root         (0) root         (0)      758 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/vod/workflow/GetWorkflowExecutionExample.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 14:55:35.000000 volcengine-1.0.84/volcengine/example/vod/callback/
--rw-r--r--   0 root         (0) root         (0)        0 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/vod/callback/__init__.py
--rw-r--r--   0 root         (0) root         (0)      805 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/vod/callback/AddCallbackSubscriptionExample.py
--rw-r--r--   0 root         (0) root         (0)      827 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/vod/callback/SetCallbackEvent.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 14:55:35.000000 volcengine-1.0.84/volcengine/example/vod/measure/
--rw-r--r--   0 root         (0) root         (0)      980 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/vod/measure/DescribeVodSnapshotData.py
--rw-r--r--   0 root         (0) root         (0)        0 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/vod/measure/__init__.py
--rw-r--r--   0 root         (0) root         (0)      902 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/vod/measure/DescribeVodSpaceEditDetailData.py
--rw-r--r--   0 root         (0) root         (0)     1005 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/vod/measure/DescribeVodSpaceDetectStatisData.py
--rw-r--r--   0 root         (0) root         (0)     1050 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/vod/measure/DescribeVodSpaceTranscodeData.py
--rw-r--r--   0 root         (0) root         (0)     1015 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/vod/measure/DescribeVodSpaceSubtitleStatisData.py
--rw-r--r--   0 root         (0) root         (0)      914 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/vod/measure/DescribeVodSpaceWorkflowDetailData.py
--rw-r--r--   0 root         (0) root         (0)      996 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/vod/measure/DescribeVodSpaceAIStatisData.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 14:55:35.000000 volcengine-1.0.84/volcengine/example/vod/upload/
--rw-r--r--   0 root         (0) root         (0)        0 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/vod/upload/__init__.py
--rw-r--r--   0 root         (0) root         (0)     1062 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/vod/upload/UploadUrl.py
--rw-r--r--   0 root         (0) root         (0)     1315 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/vod/upload/CommitUploadInfoExample.py
--rw-r--r--   0 root         (0) root         (0)     1490 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/vod/upload/UploadMedia.py
--rw-r--r--   0 root         (0) root         (0)      933 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/vod/upload/QueryUploadTaskInfo.py
--rw-r--r--   0 root         (0) root         (0)     1092 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/vod/upload/ApplyUploadInfoExample.py
--rw-r--r--   0 root         (0) root         (0)     5086 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/vod/upload/UploadMaterial.py
--rw-r--r--   0 root         (0) root         (0)      445 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/vod/upload/UploadSts2.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 14:55:35.000000 volcengine-1.0.84/volcengine/example/vod/subtitle/
--rw-r--r--   0 root         (0) root         (0)        0 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/vod/subtitle/__init__.py
--rw-r--r--   0 root         (0) root         (0)     2541 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/vod/subtitle/SubtitleExample.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 14:55:35.000000 volcengine-1.0.84/volcengine/example/vod/play/
--rw-r--r--   0 root         (0) root         (0)      839 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/vod/play/GetPlayInfoExample.py
--rw-r--r--   0 root         (0) root         (0)      501 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/vod/play/GetHlsDrmAuthTokenExample.py
--rw-r--r--   0 root         (0) root         (0)        0 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/vod/play/__init__.py
--rw-r--r--   0 root         (0) root         (0)     1489 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/vod/play/GetAllPlayInfoExample.py
--rw-r--r--   0 root         (0) root         (0)      657 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/vod/play/GetPlayAuthTokenExample.py
--rw-r--r--   0 root         (0) root         (0)      776 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/vod/play/GetPrivateDrmPlayAuthExample.py
--rw-r--r--   0 root         (0) root         (0)     1009 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/vod/play/GetPlayInfoWithLiveTimeShiftSceneExample.py
--rw-r--r--   0 root         (0) root         (0)      821 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/vod/play/GetPrivateDrmPlayAuthTokenExample.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 14:55:35.000000 volcengine-1.0.84/volcengine/example/vod/media/
--rw-r--r--   0 root         (0) root         (0)        0 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/vod/media/__init__.py
--rw-r--r--   0 root         (0) root         (0)      632 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/vod/media/GetSubtitleAuthToken.py
--rw-r--r--   0 root         (0) root         (0)     7520 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/vod/media/MediaExample.py
--rw-r--r--   0 root         (0) root         (0)        0 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/vod/media/GetSubtitleToken.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 14:55:35.000000 volcengine-1.0.84/volcengine/example/sms/
--rw-r--r--   0 root         (0) root         (0)      790 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/sms/example_apply_sms_signature.py
--rw-r--r--   0 root         (0) root         (0)      870 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/sms/example_send_batch_sms.py
--rw-r--r--   0 root         (0) root         (0)      905 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/sms/example_vms_template_query.py
--rw-r--r--   0 root         (0) root         (0)        0 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/sms/__init__.py
--rw-r--r--   0 root         (0) root         (0)      713 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/sms/example_get_sub_account_list.py
--rw-r--r--   0 root         (0) root         (0)      716 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/sms/example_delete_sms_template.py
--rw-r--r--   0 root         (0) root         (0)      742 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/sms/example_get_sms_template_and_order_list.py
--rw-r--r--   0 root         (0) root         (0)      774 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/sms/example_get_signature_and_order_list.py
--rw-r--r--   0 root         (0) root         (0)     1216 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/sms/example_apply_sms_template.py
--rw-r--r--   0 root         (0) root         (0)      605 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/sms/example_conversion.py
--rw-r--r--   0 root         (0) root         (0)     1403 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/sms/example_apply_vms_template.py
--rw-r--r--   0 root         (0) root         (0)      672 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/sms/example_get_sub_account_detail.py
--rw-r--r--   0 root         (0) root         (0)      598 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/sms/example_insert_sms_sub_account.py
--rw-r--r--   0 root         (0) root         (0)      657 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/sms/example_delete_signature.py
--rw-r--r--   0 root         (0) root         (0)     1324 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/sms/example_send_sms.py
--rw-r--r--   0 root         (0) root         (0)      819 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/sms/example_send_vms.py
--rw-r--r--   0 root         (0) root         (0)       13 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/__init__.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 14:55:35.000000 volcengine-1.0.84/volcengine/example/notify/
--rw-r--r--   0 root         (0) root         (0)      353 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/notify/example_remuse_task.py
--rw-r--r--   0 root         (0) root         (0)      334 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/notify/example_single_info.py
--rw-r--r--   0 root         (0) root         (0)      538 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/notify/example_create_tts.py
--rw-r--r--   0 root         (0) root         (0)      463 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/notify/example_batch_append_task.py
--rw-r--r--   0 root         (0) root         (0)      689 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/notify/example_create_task.py
--rw-r--r--   0 root         (0) root         (0)        0 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/notify/__init__.py
--rw-r--r--   0 root         (0) root         (0)      704 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/notify/examplae_sigle_batch_append.py
--rw-r--r--   0 root         (0) root         (0)      352 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/notify/example_pause_task.py
--rw-r--r--   0 root         (0) root         (0)      343 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/notify/example_get_reource_upload_url.py
--rw-r--r--   0 root         (0) root         (0)      368 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/notify/example_open_update_resource.py
--rw-r--r--   0 root         (0) root         (0)      368 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/notify/example_delete_resource.py
--rw-r--r--   0 root         (0) root         (0)      336 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/notify/example_single_cancle.py
--rw-r--r--   0 root         (0) root         (0)      304 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/notify/example_query_usable_resource.py
--rw-r--r--   0 root         (0) root         (0)      351 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/notify/example_stop_task.py
--rw-r--r--   0 root         (0) root         (0)      354 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/notify/example_query_open_get_resource.py
--rw-r--r--   0 root         (0) root         (0)      363 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/notify/example_fetch_resource.py
--rw-r--r--   0 root         (0) root         (0)      342 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/notify/example_commit_resource_upload.py
--rw-r--r--   0 root         (0) root         (0)      486 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/notify/example_update_task.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 14:55:35.000000 volcengine-1.0.84/volcengine/example/imagex/
--rw-r--r--   0 root         (0) root         (0)      501 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/imagex/example_common.py
--rw-r--r--   0 root         (0) root         (0)      502 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/imagex/example_upload_sts2.py
--rw-r--r--   0 root         (0) root         (0)        0 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/imagex/__init__.py
--rw-r--r--   0 root         (0) root         (0)      608 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/imagex/example_upload_image.py
--rw-r--r--   0 root         (0) root         (0)      660 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/imagex/example_fetch_url.py
--rw-r--r--   0 root         (0) root         (0)      499 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/imagex/example_get_image_content_block_list.py
--rw-r--r--   0 root         (0) root         (0)      497 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/imagex/example_create_image_content_task.py
--rw-r--r--   0 root         (0) root         (0)      539 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/imagex/example_get_image_content_task_detail.py
--rw-r--r--   0 root         (0) root         (0)      502 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/imagex/example_get_image_erase_result.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 14:55:35.000000 volcengine-1.0.84/volcengine/example/imagex/data/
--rw-r--r--   0 root         (0) root         (0)      634 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/imagex/data/edge_request.py
--rw-r--r--   0 root         (0) root         (0)      557 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/imagex/data/mirror_request_bandwidth.py
--rw-r--r--   0 root         (0) root         (0)      555 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/imagex/data/domain_bandwidth_data.py
--rw-r--r--   0 root         (0) root         (0)      554 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/imagex/data/edge_request_traffic.py
--rw-r--r--   0 root         (0) root         (0)      460 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/imagex/data/imagex_summary.py
--rw-r--r--   0 root         (0) root         (0)       30 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/imagex/data/__init__.py
--rw-r--r--   0 root         (0) root         (0)      524 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/imagex/data/edge_request_region.py
--rw-r--r--   0 root         (0) root         (0)      548 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/imagex/data/compress_usage.py
--rw-r--r--   0 root         (0) root         (0)      555 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/imagex/data/hit_rate_request_data.py
--rw-r--r--   0 root         (0) root         (0)      551 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/imagex/data/request_cnt_usage.py
--rw-r--r--   0 root         (0) root         (0)      546 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/imagex/data/bucket_usage.py
--rw-r--r--   0 root         (0) root         (0)      588 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/imagex/data/cdn_top_request_data.py
--rw-r--r--   0 root         (0) root         (0)      565 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/imagex/data/mirror_request_http_code_by_time.py
--rw-r--r--   0 root         (0) root         (0)      556 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/imagex/data/edge_request_bandwidth.py
--rw-r--r--   0 root         (0) root         (0)      553 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/imagex/data/domain_traffic_data.py
--rw-r--r--   0 root         (0) root         (0)      566 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/imagex/data/mirror_request_http_code_overview.py
--rw-r--r--   0 root         (0) root         (0)      555 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/imagex/data/mirror_request_traffic.py
--rw-r--r--   0 root         (0) root         (0)      555 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/imagex/data/hit_rate_traffic_data.py
--rw-r--r--   0 root         (0) root         (0)      547 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/imagex/data/bucket_base_op_usage.py
--rw-r--r--   0 root         (0) root         (0)      517 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/imagex/example_get_image_super_resolution_result.py
--rw-r--r--   0 root         (0) root         (0)      533 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/imagex/example_get_image_bg_fill_result.py
--rw-r--r--   0 root         (0) root         (0)      600 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/imagex/example_get_image_enhance_result.py
--rw-r--r--   0 root         (0) root         (0)      409 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/imagex/example_delete_image.py
--rw-r--r--   0 root         (0) root         (0)      640 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/imagex/example_describe_imagex_volc_cdn_access_log.py
--rw-r--r--   0 root         (0) root         (0)      480 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/imagex/example_get_license_plate_detection.py
--rw-r--r--   0 root         (0) root         (0)      477 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/imagex/example_get_image_comic_result.py
--rw-r--r--   0 root         (0) root         (0)      431 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/imagex/examle_get_image_erase_models.py
--rw-r--r--   0 root         (0) root         (0)      406 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/imagex/example_get_image_info.py
--rw-r--r--   0 root         (0) root         (0)      454 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/imagex/example_upload_image_token.py
--rw-r--r--   0 root         (0) root         (0)      681 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/imagex/example_get_image_segment.py
--rw-r--r--   0 root         (0) root         (0)      502 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/imagex/example_get_image_ocr.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 14:55:35.000000 volcengine-1.0.84/volcengine/example/imp/
--rw-r--r--   0 root         (0) root         (0)        0 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/imp/__init__.py
--rw-r--r--   0 root         (0) root         (0)      836 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/imp/RetrieveJob.py
--rw-r--r--   0 root         (0) root         (0)      978 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/imp/SubmitJob.py
--rw-r--r--   0 root         (0) root         (0)      771 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/imp/KillJob.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 14:55:35.000000 volcengine-1.0.84/volcengine/example/visual/
--rw-r--r--   0 root         (0) root         (0)      499 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/visual/example_video_summarization_query_task.py
--rw-r--r--   0 root         (0) root         (0)      504 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/visual/example_video_over_resolution_submit_task.py
--rw-r--r--   0 root         (0) root         (0)     4340 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/visual/example_common.py
--rw-r--r--   0 root         (0) root         (0)      431 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/visual/example_image_search_image_delete.py
--rw-r--r--   0 root         (0) root         (0)      478 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/visual/example_video_scene_detect.py
--rw-r--r--   0 root         (0) root         (0)        0 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/visual/__init__.py
--rw-r--r--   0 root         (0) root         (0)      471 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/visual/example_product_search_delete_image.py
--rw-r--r--   0 root         (0) root         (0)      493 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/visual/example_video_inpaint_query_task.py
--rw-r--r--   0 root         (0) root         (0)      489 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/visual/example_image_search_image_search.py
--rw-r--r--   0 root         (0) root         (0)      474 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/visual/example_image_outpaint.py
--rw-r--r--   0 root         (0) root         (0)      494 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/visual/example_image_search_image_add.py
--rw-r--r--   0 root         (0) root         (0)      540 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/visual/example_video_retargeting_submit_task.py
--rw-r--r--   0 root         (0) root         (0)     2571 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/visual/example_ocr_demo.py
--rw-r--r--   0 root         (0) root         (0)      721 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/visual/example_product_search_search_image.py
--rw-r--r--   0 root         (0) root         (0)      501 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/visual/example_video_over_resolution_query_task.py
--rw-r--r--   0 root         (0) root         (0)      442 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/visual/example_video_cover_selection.py
--rw-r--r--   0 root         (0) root         (0)      475 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/visual/example_over_resolution.py
--rw-r--r--   0 root         (0) root         (0)      758 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/visual/example_product_search_add_image.py
--rw-r--r--   0 root         (0) root         (0)      488 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/visual/example_video_inpaint_submit_task.py
--rw-r--r--   0 root         (0) root         (0)      472 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/visual/example_goods_detect.py
--rw-r--r--   0 root         (0) root         (0)      480 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/visual/example_video_highlight_extraction_submit_task.py
--rw-r--r--   0 root         (0) root         (0)      506 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/visual/example_video_highlight_extraction_query_task.py
--rw-r--r--   0 root         (0) root         (0)      512 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/visual/example_video_summarization_submit_task.py
--rw-r--r--   0 root         (0) root         (0)      473 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/visual/example_entity_detect.py
--rw-r--r--   0 root         (0) root         (0)      473 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/visual/example_goods_segment.py
--rw-r--r--   0 root         (0) root         (0)      473 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/visual/example_image_inpaint.py
--rw-r--r--   0 root         (0) root         (0)      497 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/visual/example_video_retargeting_query_task.py
--rw-r--r--   0 root         (0) root         (0)      469 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/visual/example_image_cut.py
--rw-r--r--   0 root         (0) root         (0)     2647 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/visual/example_cert_verify.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 14:55:35.000000 volcengine-1.0.84/volcengine/example/nlp/
--rw-r--r--   0 root         (0) root         (0)       43 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/nlp/__init__.py
--rw-r--r--   0 root         (0) root         (0)      466 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/nlp/example_text_correction_zh_correct.py
--rw-r--r--   0 root         (0) root         (0)     2495 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/nlp/example_keyphrase_extraction_extract.py
--rw-r--r--   0 root         (0) root         (0)      440 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/nlp/example_sentiment_analysis.py
--rw-r--r--   0 root         (0) root         (0)     1085 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/nlp/example_essay_auto_grade.py
--rw-r--r--   0 root         (0) root         (0)      468 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/nlp/example_text_correction_en_correct.py
--rw-r--r--   0 root         (0) root         (0)      693 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/nlp/example_text_summarization.py
--rw-r--r--   0 root         (0) root         (0)      441 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/nlp/example_novel_correction.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 14:55:35.000000 volcengine-1.0.84/volcengine/example/livesaas/
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 14:55:35.000000 volcengine-1.0.84/volcengine/example/livesaas/example_comment/
--rw-r--r--   0 root         (0) root         (0)      477 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/livesaas/example_comment/example_presenter_chat_api.py
--rw-r--r--   0 root         (0) root         (0)        0 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/livesaas/example_comment/__init__.py
--rw-r--r--   0 root         (0) root         (0)      465 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/livesaas/example_comment/example_delete_chat_api.py
--rw-r--r--   0 root         (0) root         (0)        0 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/livesaas/__init__.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 14:55:35.000000 volcengine-1.0.84/volcengine/example/livesaas/example_replay_admin/
--rw-r--r--   0 root         (0) root         (0)      575 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/livesaas/example_replay_admin/example_list_medias_api.py
--rw-r--r--   0 root         (0) root         (0)        0 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/livesaas/example_replay_admin/__init__.py
--rw-r--r--   0 root         (0) root         (0)      523 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/livesaas/example_replay_admin/example_update_media_online_status_api.py
--rw-r--r--   0 root         (0) root         (0)      528 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/livesaas/example_replay_admin/example_upload_replay_api.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 14:55:35.000000 volcengine-1.0.84/volcengine/example/livesaas/example_live_admin/
--rw-r--r--   0 root         (0) root         (0)      607 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/livesaas/example_live_admin/example_list_activity_api.py
--rw-r--r--   0 root         (0) root         (0)        0 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/livesaas/example_live_admin/__init__.py
--rw-r--r--   0 root         (0) root         (0)      657 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/livesaas/example_live_admin/example_create_activity_api.py
--rw-r--r--   0 root         (0) root         (0)      453 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/livesaas/example_live_admin/example_delete_activity_api.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 14:55:35.000000 volcengine-1.0.84/volcengine/example/livesaas/example_live_control/
--rw-r--r--   0 root         (0) root         (0)      522 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/livesaas/example_live_control/example_update_loop_video_status_api.py
--rw-r--r--   0 root         (0) root         (0)        0 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/livesaas/example_live_control/__init__.py
--rw-r--r--   0 root         (0) root         (0)      453 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/livesaas/example_live_control/example_get_activity_api.py
--rw-r--r--   0 root         (0) root         (0)      450 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/livesaas/example_live_control/example_get_streams_api.py
--rw-r--r--   0 root         (0) root         (0)      500 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/livesaas/example_live_control/example_update_activity_status_api.py
--rw-r--r--   0 root         (0) root         (0)     3115 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/livesaas/example_live_control/example_update_activity_basic_config_api.py
--rw-r--r--   0 root         (0) root         (0)      640 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/livesaas/example_live_control/example_update_pull_to_push_api.py
--rw-r--r--   0 root         (0) root         (0)      479 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/livesaas/example_live_control/example_get_activity_basic_config_api.py
--rw-r--r--   0 root         (0) root         (0)      689 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/livesaas/example_live_control/example_update_loop_video_api.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 14:55:35.000000 volcengine-1.0.84/volcengine/example/livesaas/example_client_sdk/
--rw-r--r--   0 root         (0) root         (0)      567 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/livesaas/example_client_sdk/example_get_sdk_token_api.py
--rw-r--r--   0 root         (0) root         (0)        0 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/livesaas/example_client_sdk/__init__.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 14:55:35.000000 volcengine-1.0.84/volcengine/example/bioos/
--rw-r--r--   0 root         (0) root         (0)      746 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/bioos/example_create_workflow.py
--rw-r--r--   0 root         (0) root         (0)      570 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/bioos/example_delete_submission.py
--rw-r--r--   0 root         (0) root         (0)      686 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/bioos/example_create_cluster.py
--rw-r--r--   0 root         (0) root         (0)      495 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/bioos/example_list_workspaces.py
--rw-r--r--   0 root         (0) root         (0)      582 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/bioos/example_create_workspace.py
--rw-r--r--   0 root         (0) root         (0)        0 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/bioos/__init__.py
--rw-r--r--   0 root         (0) root         (0)     1041 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/bioos/example_create_submission.py
--rw-r--r--   0 root         (0) root         (0)      498 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/bioos/example_delete_cluster.py
--rw-r--r--   0 root         (0) root         (0)      583 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/bioos/example_list_runs.py
--rw-r--r--   0 root         (0) root         (0)      539 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/bioos/example_list_data_models.py
--rw-r--r--   0 root         (0) root         (0)      604 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/bioos/example_list_submissions.py
--rw-r--r--   0 root         (0) root         (0)      710 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/bioos/example_list_clusters.py
--rw-r--r--   0 root         (0) root         (0)      500 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/bioos/example_delete_workspace.py
--rw-r--r--   0 root         (0) root         (0)      659 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/bioos/example_update_workspace.py
--rw-r--r--   0 root         (0) root         (0)      961 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/bioos/example_create_data_model.py
--rw-r--r--   0 root         (0) root         (0)      627 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/bioos/example_delete_data_model_rows_and_headers.py
--rw-r--r--   0 root         (0) root         (0)      646 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/bioos/example_list_workflows.py
--rw-r--r--   0 root         (0) root         (0)      602 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/bioos/example_bind_cluster_to_workspace.py
--rw-r--r--   0 root         (0) root         (0)      674 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/bioos/example_list_data_model_rows.py
--rw-r--r--   0 root         (0) root         (0)      604 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/bioos/example_unbind_cluster_and_workspace.py
--rw-r--r--   0 root         (0) root         (0)      566 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/bioos/example_delete_workflow.py
--rw-r--r--   0 root         (0) root         (0)      571 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/bioos/example_cancel_submission.py
--rw-r--r--   0 root         (0) root         (0)      557 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/bioos/example_cancel_run.py
--rw-r--r--   0 root         (0) root         (0)      555 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/bioos/example_list_clusters_of_workspace.py
--rw-r--r--   0 root         (0) root         (0)      559 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/bioos/example_list_tasks.py
--rw-r--r--   0 root         (0) root         (0)      783 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/bioos/example_update_workflow.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 14:55:35.000000 volcengine-1.0.84/volcengine/example/sts/
--rw-r--r--   0 root         (0) root         (0)        0 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/sts/__init__.py
--rw-r--r--   0 root         (0) root         (0)      390 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/sts/example_assume_role.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 14:55:35.000000 volcengine-1.0.84/volcengine/example/rdspostgresql/
--rw-r--r--   0 root         (0) root         (0)        0 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/rdspostgresql/__init__.py
--rw-r--r--   0 root         (0) root         (0)     2966 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/rdspostgresql/example_create_instance.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 14:55:35.000000 volcengine-1.0.84/volcengine/example/tls/
--rw-r--r--   0 root         (0) root         (0)     3913 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/tls/example_alarm.py
--rw-r--r--   0 root         (0) root         (0)        0 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/tls/__init__.py
--rw-r--r--   0 root         (0) root         (0)     5626 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/tls/example_rule.py
--rw-r--r--   0 root         (0) root         (0)     2304 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/tls/example_host_group.py
--rw-r--r--   0 root         (0) root         (0)     3723 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/tls/example_log.py
--rw-r--r--   0 root         (0) root         (0)     1968 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/tls/example_topic.py
--rw-r--r--   0 root         (0) root         (0)     2572 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/tls/example_index.py
--rw-r--r--   0 root         (0) root         (0)     1669 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/tls/example_project.py
--rw-r--r--   0 root         (0) root         (0)      849 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/DemoSignOnly.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 14:55:35.000000 volcengine-1.0.84/volcengine/example/vms/
--rw-r--r--   0 root         (0) root         (0)      364 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/vms/example_enable_or_disable_number.py
--rw-r--r--   0 root         (0) root         (0)      401 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/vms/example_number_pool_list.py
--rw-r--r--   0 root         (0) root         (0)        0 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/vms/__init__.py
--rw-r--r--   0 root         (0) root         (0)      315 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/vms/example_select_number.py
--rw-r--r--   0 root         (0) root         (0)      403 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/vms/example_number_list.py
--rw-r--r--   0 root         (0) root         (0)      378 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/vms/example_query_can_call.py
--rw-r--r--   0 root         (0) root         (0)      423 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/vms/example_update_number_pool.py
--rw-r--r--   0 root         (0) root         (0)      392 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/vms/example_create_number_pool.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 14:55:35.000000 volcengine-1.0.84/volcengine/example/secretnumber/
--rw-r--r--   0 root         (0) root         (0)      419 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/secretnumber/example_unbind_axn.py
--rw-r--r--   0 root         (0) root         (0)      600 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/secretnumber/example_select_number_and_bind_axn.py
--rw-r--r--   0 root         (0) root         (0)      422 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/secretnumber/example_unbind_axyb.py
--rw-r--r--   0 root         (0) root         (0)      549 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/secretnumber/example_bind_axne.py
--rw-r--r--   0 root         (0) root         (0)        0 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/secretnumber/__init__.py
--rw-r--r--   0 root         (0) root         (0)      422 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/secretnumber/example_unbind_axne.py
--rw-r--r--   0 root         (0) root         (0)      525 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/secretnumber/example_query_subscription_for_list.py
--rw-r--r--   0 root         (0) root         (0)      443 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/secretnumber/example_query_subscription.py
--rw-r--r--   0 root         (0) root         (0)      555 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/secretnumber/example_bind_axb.py
--rw-r--r--   0 root         (0) root         (0)      454 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/secretnumber/example_click2_call_lite.py
--rw-r--r--   0 root         (0) root         (0)      510 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/secretnumber/example_bind_yb_for_axyb.py
--rw-r--r--   0 root         (0) root         (0)      519 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/secretnumber/example_upgrade_ax_to_axb.py
--rw-r--r--   0 root         (0) root         (0)      498 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/secretnumber/example_update_axne.py
--rw-r--r--   0 root         (0) root         (0)      596 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/secretnumber/example_bind_axyb.py
--rw-r--r--   0 root         (0) root         (0)      497 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/secretnumber/example_update_axyb.py
--rw-r--r--   0 root         (0) root         (0)      555 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/secretnumber/example_bind_axn.py
--rw-r--r--   0 root         (0) root         (0)      513 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/secretnumber/example_bind_axb_for_axne.py
--rw-r--r--   0 root         (0) root         (0)      419 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/secretnumber/example_unbind_axb.py
--rw-r--r--   0 root         (0) root         (0)      494 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/secretnumber/example_update_axn.py
--rw-r--r--   0 root         (0) root         (0)      530 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/secretnumber/example_select_number_and_bind_axb_form.py
--rw-r--r--   0 root         (0) root         (0)      497 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/secretnumber/example_update_axb.py
--rw-r--r--   0 root         (0) root         (0)      503 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/secretnumber/example_click2_call.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 14:55:35.000000 volcengine-1.0.84/volcengine/example/live/
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 14:55:35.000000 volcengine-1.0.84/volcengine/example/live/example_vqs_task/
--rw-r--r--   0 root         (0) root         (0)        0 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/live/example_vqs_task/__init__.py
--rw-r--r--   0 root         (0) root         (0)      528 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/live/example_vqs_task/example_create_v_q_score_task.py
--rw-r--r--   0 root         (0) root         (0)      501 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/live/example_vqs_task/example_list_v_q_score_task.py
--rw-r--r--   0 root         (0) root         (0)      425 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/live/example_vqs_task/example_describe_v_q_score_task.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 14:55:35.000000 volcengine-1.0.84/volcengine/example/live/example_auth/
--rw-r--r--   0 root         (0) root         (0)        0 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/live/example_auth/__init__.py
--rw-r--r--   0 root         (0) root         (0)      357 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/live/example_auth/example_describe_auth.py
--rw-r--r--   0 root         (0) root         (0)      496 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/live/example_auth/example_update_auth_key.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 14:55:35.000000 volcengine-1.0.84/volcengine/example/live/example_transcode/
--rw-r--r--   0 root         (0) root         (0)      335 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/live/example_transcode/example_list_vhost_transcode_preset.py
--rw-r--r--   0 root         (0) root         (0)        0 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/live/example_transcode/__init__.py
--rw-r--r--   0 root         (0) root         (0)      372 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/live/example_transcode/example_delete_transcode_preset.py
--rw-r--r--   0 root         (0) root         (0)      438 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/live/example_transcode/example_create_transcode_preset.py
--rw-r--r--   0 root         (0) root         (0)      364 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/live/example_transcode/example_list_common_trans_preset_detail.py
--rw-r--r--   0 root         (0) root         (0)      438 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/live/example_transcode/example_update_transcode_preset.py
--rw-r--r--   0 root         (0) root         (0)        0 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/live/__init__.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 14:55:35.000000 volcengine-1.0.84/volcengine/example/live/example_cert/
--rw-r--r--   0 root         (0) root         (0)      350 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/live/example_cert/example_update_cert.py
--rw-r--r--   0 root         (0) root         (0)      367 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/live/example_cert/example_bind_cert.py
--rw-r--r--   0 root         (0) root         (0)      321 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/live/example_cert/example_delete_cert.py
--rw-r--r--   0 root         (0) root         (0)        0 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/live/example_cert/__init__.py
--rw-r--r--   0 root         (0) root         (0)      348 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/live/example_cert/example_create_cert.py
--rw-r--r--   0 root         (0) root         (0)      321 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/live/example_cert/example_un_bind_cert.py
--rw-r--r--   0 root         (0) root         (0)      372 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/live/example_cert/example_list_cert.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 14:55:35.000000 volcengine-1.0.84/volcengine/example/live/example_generate_url/
--rw-r--r--   0 root         (0) root         (0)        0 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/live/example_generate_url/__init__.py
--rw-r--r--   0 root         (0) root         (0)      557 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/live/example_generate_url/example_generate_play_u_r_l.py
--rw-r--r--   0 root         (0) root         (0)      499 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/live/example_generate_url/example_generate_push_u_r_l.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 14:55:35.000000 volcengine-1.0.84/volcengine/example/live/example_audit/
--rw-r--r--   0 root         (0) root         (0)        0 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/live/example_audit/__init__.py
--rw-r--r--   0 root         (0) root         (0)      395 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/live/example_audit/example_delete_snapshot_audit_preset.py
--rw-r--r--   0 root         (0) root         (0)      345 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/live/example_audit/example_list_vhost_snapshot_audit_preset.py
--rw-r--r--   0 root         (0) root         (0)      424 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/live/example_audit/example_update_snapshot_audit_preset.py
--rw-r--r--   0 root         (0) root         (0)      545 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/live/example_audit/example_create_snapshot_audit_preset.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 14:55:35.000000 volcengine-1.0.84/volcengine/example/live/example_index_m3u8/
--rw-r--r--   0 root         (0) root         (0)      519 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/live/example_index_m3u8/example_create_live_stream_record_index_file.py
--rw-r--r--   0 root         (0) root         (0)        0 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/live/example_index_m3u8/__init__.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 14:55:35.000000 volcengine-1.0.84/volcengine/example/live/example_usage/
--rw-r--r--   0 root         (0) root         (0)        0 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/live/example_usage/__init__.py
--rw-r--r--   0 root         (0) root         (0)      522 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/live/example_usage/describe_live_batch_push_stream_metrics.py
--rw-r--r--   0 root         (0) root         (0)      524 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/live/example_usage/describe_live_batch_source_stream_metrics.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 14:55:35.000000 volcengine-1.0.84/volcengine/example/live/example_describe_info/
--rw-r--r--   0 root         (0) root         (0)        0 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/live/example_describe_info/__init__.py
--rw-r--r--   0 root         (0) root         (0)     7666 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/live/example_describe_info/example_describe_info.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 14:55:35.000000 volcengine-1.0.84/volcengine/example/live/example_relay_source/
--rw-r--r--   0 root         (0) root         (0)        0 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/live/example_relay_source/__init__.py
--rw-r--r--   0 root         (0) root         (0)      565 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/live/example_relay_source/example_update_relay_source_v2.py
--rw-r--r--   0 root         (0) root         (0)      447 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/live/example_relay_source/example_delete_relay_source_v2.py
--rw-r--r--   0 root         (0) root         (0)      433 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/live/example_relay_source/example_describe_relay_source_v2.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 14:55:35.000000 volcengine-1.0.84/volcengine/example/live/example_referer/
--rw-r--r--   0 root         (0) root         (0)      573 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/live/example_referer/example_update_referer.py
--rw-r--r--   0 root         (0) root         (0)        0 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/live/example_referer/__init__.py
--rw-r--r--   0 root         (0) root         (0)      341 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/live/example_referer/example_delete_referer.py
--rw-r--r--   0 root         (0) root         (0)      344 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/live/example_referer/example_describe_referer.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 14:55:35.000000 volcengine-1.0.84/volcengine/example/live/example_callback/
--rw-r--r--   0 root         (0) root         (0)      515 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/live/example_callback/example_update_callback.py
--rw-r--r--   0 root         (0) root         (0)        0 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/live/example_callback/__init__.py
--rw-r--r--   0 root         (0) root         (0)      361 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/live/example_callback/example_delete_callback.py
--rw-r--r--   0 root         (0) root         (0)      381 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/live/example_callback/example_describe_callback.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 14:55:35.000000 volcengine-1.0.84/volcengine/example/live/example_domain/
--rw-r--r--   0 root         (0) root         (0)        0 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/live/example_domain/__init__.py
--rw-r--r--   0 root         (0) root         (0)      454 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/live/example_domain/example_create_domain.py
--rw-r--r--   0 root         (0) root         (0)      329 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/live/example_domain/example_disable_domain.py
--rw-r--r--   0 root         (0) root         (0)      377 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/live/example_domain/example_describe_domain.py
--rw-r--r--   0 root         (0) root         (0)      351 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/live/example_domain/example_list_domain_detail.py
--rw-r--r--   0 root         (0) root         (0)      328 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/live/example_domain/example_delete_domain.py
--rw-r--r--   0 root         (0) root         (0)      328 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/live/example_domain/example_enable_domain.py
--rw-r--r--   0 root         (0) root         (0)      368 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/live/example_domain/example_manager_pull_push_domain_bind.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 14:55:35.000000 volcengine-1.0.84/volcengine/example/live/example_stream/
--rw-r--r--   0 root         (0) root         (0)        0 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/live/example_stream/__init__.py
--rw-r--r--   0 root         (0) root         (0)      538 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/live/example_stream/example_describe_forbidden_stream_info_by_page.py
--rw-r--r--   0 root         (0) root         (0)      507 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/live/example_stream/example_describe_closed_stream_info_by_page.py
--rw-r--r--   0 root         (0) root         (0)      446 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/live/example_stream/example_kill_stream.py
--rw-r--r--   0 root         (0) root         (0)      489 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/live/example_stream/example_describe_live_stream_state.py
--rw-r--r--   0 root         (0) root         (0)      363 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/live/example_stream/example_resume_stream.py
--rw-r--r--   0 root         (0) root         (0)      378 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/live/example_stream/example_forbid_stream.py
--rw-r--r--   0 root         (0) root         (0)      501 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/live/example_stream/example_describe_live_stream_info_by_page.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 14:55:35.000000 volcengine-1.0.84/volcengine/example/live/example_record/
--rw-r--r--   0 root         (0) root         (0)      600 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/live/example_record/example_create_record_preset.py
--rw-r--r--   0 root         (0) root         (0)      375 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/live/example_record/example_delete_record_preset.py
--rw-r--r--   0 root         (0) root         (0)      637 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/live/example_record/example_describe_record_task_file_history.py
--rw-r--r--   0 root         (0) root         (0)        0 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/live/example_record/__init__.py
--rw-r--r--   0 root         (0) root         (0)      337 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/live/example_record/example_list_vhost_record_preset.py
--rw-r--r--   0 root         (0) root         (0)      629 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/live/example_record/example_update_record_preset.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 14:55:35.000000 volcengine-1.0.84/volcengine/example/live/example_snapshot/
--rw-r--r--   0 root         (0) root         (0)      535 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/live/example_snapshot/example_update_snapshot_preset.py
--rw-r--r--   0 root         (0) root         (0)        0 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/live/example_snapshot/__init__.py
--rw-r--r--   0 root         (0) root         (0)      371 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/live/example_snapshot/example_delete_snapshot_preset.py
--rw-r--r--   0 root         (0) root         (0)      513 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/live/example_snapshot/example_create_snapshot_preset.py
--rw-r--r--   0 root         (0) root         (0)      334 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/live/example_snapshot/example_list_vhost_snapshot_preset.py
--rw-r--r--   0 root         (0) root         (0)      655 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/live/example_snapshot/example_describe_c_d_n_snapshot_history.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 14:55:35.000000 volcengine-1.0.84/volcengine/example/live/example_pull_to_push/
--rw-r--r--   0 root         (0) root         (0)      429 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/live/example_pull_to_push/example_stop_pull_to_push_task.py
--rw-r--r--   0 root         (0) root         (0)      463 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/live/example_pull_to_push/example_list_pull_to_push_task.py
--rw-r--r--   0 root         (0) root         (0)        0 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/live/example_pull_to_push/__init__.py
--rw-r--r--   0 root         (0) root         (0)      437 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/live/example_pull_to_push/example_delete_pull_to_push_task.py
--rw-r--r--   0 root         (0) root         (0)      603 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/live/example_pull_to_push/example_create_pull_to_push_task.py
--rw-r--r--   0 root         (0) root         (0)      438 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/live/example_pull_to_push/example_restart_pull_to_push_task.py
--rw-r--r--   0 root         (0) root         (0)      623 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/live/example_pull_to_push/example_update_pull_to_push_task.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 14:55:35.000000 volcengine-1.0.84/volcengine/example/emr/
--rw-r--r--   0 root         (0) root         (0)        0 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/emr/__init__.py
--rw-r--r--   0 root         (0) root         (0)      512 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/emr/example_list_clusters.py
--rw-r--r--   0 root         (0) root         (0)      633 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/example/emr/example_list_instance_group.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 14:55:35.000000 volcengine-1.0.84/volcengine/bioos/
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 14:55:35.000000 volcengine-1.0.84/volcengine/bioos/doc/
--rw-r--r--   0 root         (0) root         (0)        0 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/bioos/doc/__init__.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 14:55:35.000000 volcengine-1.0.84/volcengine/bioos/doc/source/
--rw-r--r--   0 root         (0) root         (0)        0 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/bioos/doc/source/__init__.py
--rw-r--r--   0 root         (0) root         (0)     1172 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/bioos/doc/source/conf.py
--rw-r--r--   0 root         (0) root         (0)        0 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/bioos/__init__.py
--rw-r--r--   0 root         (0) root         (0)    46225 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/bioos/BioOsService.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 14:55:35.000000 volcengine-1.0.84/volcengine/business_security/
--rw-r--r--   0 root         (0) root         (0)        0 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/business_security/__init__.py
--rw-r--r--   0 root         (0) root         (0)     5260 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/business_security/RiskDetectionService.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 14:55:35.000000 volcengine-1.0.84/volcengine/sts/
--rw-r--r--   0 root         (0) root         (0)        0 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/sts/__init__.py
--rw-r--r--   0 root         (0) root         (0)     1424 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/sts/StsService.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 14:55:35.000000 volcengine-1.0.84/volcengine/rdspostgresql/
--rw-r--r--   0 root         (0) root         (0)        0 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/rdspostgresql/__init__.py
--rw-r--r--   0 root         (0) root         (0)     4010 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/rdspostgresql/rdspostgresql.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 14:55:35.000000 volcengine-1.0.84/volcengine/tls/
--rw-r--r--   0 root         (0) root         (0)    15196 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/tls/tls_responses.py
--rw-r--r--   0 root         (0) root         (0)    23756 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/tls/TLSService.py
--rw-r--r--   0 root         (0) root         (0)        0 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/tls/__init__.py
--rw-r--r--   0 root         (0) root         (0)    21704 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/tls/data.py
--rw-r--r--   0 root         (0) root         (0)    24342 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/tls/tls_requests.py
--rw-r--r--   0 root         (0) root         (0)     3099 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/tls/log_pb2.py
--rw-r--r--   0 root         (0) root         (0)     6534 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/tls/const.py
--rw-r--r--   0 root         (0) root         (0)     1407 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/tls/tls_exception.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 14:55:35.000000 volcengine-1.0.84/volcengine/vms/
--rw-r--r--   0 root         (0) root         (0)     2298 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/vms/risk.py
--rw-r--r--   0 root         (0) root         (0)        0 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/vms/__init__.py
--rw-r--r--   0 root         (0) root         (0)     4365 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/vms/NumberPoolService.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 14:55:35.000000 volcengine-1.0.84/volcengine/secretnumber/
--rw-r--r--   0 root         (0) root         (0)        0 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/secretnumber/__init__.py
--rw-r--r--   0 root         (0) root         (0)     3136 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/secretnumber/DatacenterService.py
--rw-r--r--   0 root         (0) root         (0)     9226 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/secretnumber/SecretNumberService.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 14:55:35.000000 volcengine-1.0.84/volcengine/live/
--rw-r--r--   0 root         (0) root         (0)       29 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/live/__init__.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 14:55:35.000000 volcengine-1.0.84/volcengine/live/models/
--rw-r--r--   0 root         (0) root         (0)        0 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/live/models/__init__.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 14:55:35.000000 volcengine-1.0.84/volcengine/live/models/response/
--rw-r--r--   0 root         (0) root         (0)        0 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/live/models/response/__init__.py
--rw-r--r--   0 root         (0) root         (0)    27896 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/live/models/response/response_live_pb2.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 14:55:35.000000 volcengine-1.0.84/volcengine/live/models/request/
--rw-r--r--   0 root         (0) root         (0)     1230 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/live/models/request/live_requests.py
--rw-r--r--   0 root         (0) root         (0)        0 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/live/models/request/__init__.py
--rw-r--r--   0 root         (0) root         (0)    28008 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/live/models/request/request_live_pb2.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 14:55:35.000000 volcengine-1.0.84/volcengine/live/models/business/
--rw-r--r--   0 root         (0) root         (0)     3682 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/live/models/business/deny_config_pb2.py
--rw-r--r--   0 root         (0) root         (0)     3870 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/live/models/business/pull_to_push_pb2.py
--rw-r--r--   0 root         (0) root         (0)     3128 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/live/models/business/record_manage_pb2.py
--rw-r--r--   0 root         (0) root         (0)        0 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/live/models/business/__init__.py
--rw-r--r--   0 root         (0) root         (0)     2942 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/live/models/business/domain_pb2.py
--rw-r--r--   0 root         (0) root         (0)     4488 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/live/models/business/relay_source_pb2.py
--rw-r--r--   0 root         (0) root         (0)     3658 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/live/models/business/snapshot_manage_pb2.py
--rw-r--r--   0 root         (0) root         (0)     6407 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/live/models/business/stream_manage_pb2.py
--rw-r--r--   0 root         (0) root         (0)     2552 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/live/models/business/index_m3u8_pb2.py
--rw-r--r--   0 root         (0) root         (0)     5225 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/live/models/business/VQScore_pb2.py
--rw-r--r--   0 root         (0) root         (0)     3922 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/live/models/business/addr_pb2.py
--rw-r--r--   0 root         (0) root         (0)    52984 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/live/LiveService.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 14:55:35.000000 volcengine-1.0.84/volcengine/emr/
--rw-r--r--   0 root         (0) root         (0)        0 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/emr/__init__.py
--rw-r--r--   0 root         (0) root         (0)     5045 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/emr/EMRService.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 14:55:35.000000 volcengine-1.0.84/volcengine/game_protect/
--rw-r--r--   0 root         (0) root         (0)     1738 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/game_protect/GameProtectService.py
--rw-r--r--   0 root         (0) root         (0)        0 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/game_protect/__init__.py
--rw-r--r--   0 root         (0) root         (0)      367 2023-04-06 14:55:33.000000 volcengine-1.0.84/volcengine/ServiceInfo.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2021-04-08 02:37:18.000000 volcengine-1.0.9/
+-rw-r--r--   0 root         (0) root         (0)       38 2021-04-08 02:37:18.000000 volcengine-1.0.9/setup.cfg
+-rw-r--r--   0 root         (0) root         (0)      526 2021-04-08 02:37:09.000000 volcengine-1.0.9/setup.py
+-rw-r--r--   0 root         (0) root         (0)      292 2021-04-08 02:37:18.000000 volcengine-1.0.9/PKG-INFO
+drwxr-xr-x   0 root         (0) root         (0)        0 2021-04-08 02:37:17.000000 volcengine-1.0.9/volcengine.egg-info/
+-rw-r--r--   0 root         (0) root         (0)      292 2021-04-08 02:37:16.000000 volcengine-1.0.9/volcengine.egg-info/PKG-INFO
+-rw-r--r--   0 root         (0) root         (0)       11 2021-04-08 02:37:16.000000 volcengine-1.0.9/volcengine.egg-info/top_level.txt
+-rw-r--r--   0 root         (0) root         (0)        1 2021-04-08 02:37:16.000000 volcengine-1.0.9/volcengine.egg-info/dependency_links.txt
+-rw-r--r--   0 root         (0) root         (0)       43 2021-04-08 02:37:16.000000 volcengine-1.0.9/volcengine.egg-info/requires.txt
+-rw-r--r--   0 root         (0) root         (0)     4441 2021-04-08 02:37:16.000000 volcengine-1.0.9/volcengine.egg-info/SOURCES.txt
+drwxr-xr-x   0 root         (0) root         (0)        0 2021-04-08 02:37:17.000000 volcengine-1.0.9/volcengine/
+drwxr-xr-x   0 root         (0) root         (0)        0 2021-04-08 02:37:17.000000 volcengine-1.0.9/volcengine/iam/
+-rw-r--r--   0 root         (0) root         (0)        0 2021-04-08 02:37:09.000000 volcengine-1.0.9/volcengine/iam/__init__.py
+-rw-r--r--   0 root         (0) root         (0)     1422 2021-04-08 02:37:09.000000 volcengine-1.0.9/volcengine/iam/IamService.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2021-04-08 02:37:17.000000 volcengine-1.0.9/volcengine/const/
+-rw-r--r--   0 root         (0) root         (0)        0 2021-04-08 02:37:09.000000 volcengine-1.0.9/volcengine/const/__init__.py
+-rw-r--r--   0 root         (0) root         (0)     1104 2021-04-08 02:37:09.000000 volcengine-1.0.9/volcengine/const/Const.py
+-rw-r--r--   0 root         (0) root         (0)      291 2021-04-08 02:37:09.000000 volcengine-1.0.9/volcengine/Credentials.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2021-04-08 02:37:17.000000 volcengine-1.0.9/volcengine/models/
+-rw-r--r--   0 root         (0) root         (0)        0 2021-04-08 02:37:09.000000 volcengine-1.0.9/volcengine/models/__init__.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2021-04-08 02:37:17.000000 volcengine-1.0.9/volcengine/models/base/
+-rw-r--r--   0 root         (0) root         (0)        0 2021-04-08 02:37:09.000000 volcengine-1.0.9/volcengine/models/base/__init__.py
+-rw-r--r--   0 root         (0) root         (0)     7059 2021-04-08 02:37:09.000000 volcengine-1.0.9/volcengine/models/base/base_pb2.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2021-04-08 02:37:17.000000 volcengine-1.0.9/volcengine/models/vod/
+-rw-r--r--   0 root         (0) root         (0)        0 2021-04-08 02:37:09.000000 volcengine-1.0.9/volcengine/models/vod/__init__.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2021-04-08 02:37:17.000000 volcengine-1.0.9/volcengine/models/vod/business/
+-rw-r--r--   0 root         (0) root         (0)    16989 2021-04-08 02:37:09.000000 volcengine-1.0.9/volcengine/models/vod/business/vod_play_pb2.py
+-rw-r--r--   0 root         (0) root         (0)        0 2021-04-08 02:37:09.000000 volcengine-1.0.9/volcengine/models/vod/business/__init__.py
+-rw-r--r--   0 root         (0) root         (0)    17950 2021-04-08 02:37:09.000000 volcengine-1.0.9/volcengine/models/vod/business/vod_media_pb2.py
+-rw-r--r--   0 root         (0) root         (0)    22292 2021-04-08 02:37:09.000000 volcengine-1.0.9/volcengine/models/vod/business/vod_workflow_pb2.py
+-rw-r--r--   0 root         (0) root         (0)    36940 2021-04-08 02:37:09.000000 volcengine-1.0.9/volcengine/models/vod/business/vod_upload_pb2.py
+-rw-r--r--   0 root         (0) root         (0)    40077 2021-04-08 02:37:09.000000 volcengine-1.0.9/volcengine/models/vod/business/vod_common_pb2.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2021-04-08 02:37:17.000000 volcengine-1.0.9/volcengine/models/vod/response/
+-rw-r--r--   0 root         (0) root         (0)        0 2021-04-08 02:37:09.000000 volcengine-1.0.9/volcengine/models/vod/response/__init__.py
+-rw-r--r--   0 root         (0) root         (0)    33858 2021-04-08 02:37:09.000000 volcengine-1.0.9/volcengine/models/vod/response/response_vod_pb2.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2021-04-08 02:37:17.000000 volcengine-1.0.9/volcengine/models/vod/request/
+-rw-r--r--   0 root         (0) root         (0)        0 2021-04-08 02:37:09.000000 volcengine-1.0.9/volcengine/models/vod/request/__init__.py
+-rw-r--r--   0 root         (0) root         (0)    40946 2021-04-08 02:37:09.000000 volcengine-1.0.9/volcengine/models/vod/request/request_vod_pb2.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2021-04-08 02:37:18.000000 volcengine-1.0.9/volcengine/visual/
+-rw-r--r--   0 root         (0) root         (0)        0 2021-04-08 02:37:09.000000 volcengine-1.0.9/volcengine/visual/__init__.py
+-rw-r--r--   0 root         (0) root         (0)    10792 2021-04-08 02:37:09.000000 volcengine-1.0.9/volcengine/visual/VisualService.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2021-04-08 02:37:17.000000 volcengine-1.0.9/volcengine/imagex/
+-rw-r--r--   0 root         (0) root         (0)        0 2021-04-08 02:37:09.000000 volcengine-1.0.9/volcengine/imagex/__init__.py
+-rw-r--r--   0 root         (0) root         (0)     9608 2021-04-08 02:37:09.000000 volcengine-1.0.9/volcengine/imagex/ImageXService.py
+-rw-r--r--   0 root         (0) root         (0)       32 2021-04-08 02:37:09.000000 volcengine-1.0.9/volcengine/__init__.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2021-04-08 02:37:17.000000 volcengine-1.0.9/volcengine/base/
+-rw-r--r--   0 root         (0) root         (0)     1232 2021-04-08 02:37:09.000000 volcengine-1.0.9/volcengine/base/Request.py
+-rw-r--r--   0 root         (0) root         (0)        0 2021-04-08 02:37:09.000000 volcengine-1.0.9/volcengine/base/__init__.py
+-rw-r--r--   0 root         (0) root         (0)     7833 2021-04-08 02:37:09.000000 volcengine-1.0.9/volcengine/base/Service.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2021-04-08 02:37:18.000000 volcengine-1.0.9/volcengine/vedit/
+-rw-r--r--   0 root         (0) root         (0)        0 2021-04-08 02:37:09.000000 volcengine-1.0.9/volcengine/vedit/__init__.py
+-rw-r--r--   0 root         (0) root         (0)     2731 2021-04-08 02:37:09.000000 volcengine-1.0.9/volcengine/vedit/VEditService.py
+-rw-r--r--   0 root         (0) root         (0)      323 2021-04-08 02:37:09.000000 volcengine-1.0.9/volcengine/ApiInfo.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2021-04-08 02:37:17.000000 volcengine-1.0.9/volcengine/auth/
+-rw-r--r--   0 root         (0) root         (0)     5289 2021-04-08 02:37:09.000000 volcengine-1.0.9/volcengine/auth/SignerV4.py
+-rw-r--r--   0 root         (0) root         (0)      698 2021-04-08 02:37:09.000000 volcengine-1.0.9/volcengine/auth/MetaData.py
+-rw-r--r--   0 root         (0) root         (0)        0 2021-04-08 02:37:09.000000 volcengine-1.0.9/volcengine/auth/__init__.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2021-04-08 02:37:17.000000 volcengine-1.0.9/volcengine/example/
+drwxr-xr-x   0 root         (0) root         (0)        0 2021-04-08 02:37:17.000000 volcengine-1.0.9/volcengine/example/visual/
+-rw-r--r--   0 root         (0) root         (0)      499 2021-04-08 02:37:09.000000 volcengine-1.0.9/volcengine/example/visual/example_video_summarization_query_task.py
+-rw-r--r--   0 root         (0) root         (0)      488 2021-04-08 02:37:09.000000 volcengine-1.0.9/volcengine/example/visual/example_video_inpaint_submit_task.py
+-rw-r--r--   0 root         (0) root         (0)      501 2021-04-08 02:37:09.000000 volcengine-1.0.9/volcengine/example/visual/example_general_segment.py
+-rw-r--r--   0 root         (0) root         (0)      501 2021-04-08 02:37:09.000000 volcengine-1.0.9/volcengine/example/visual/example_video_over_resolution_query_task.py
+-rw-r--r--   0 root         (0) root         (0)      473 2021-04-08 02:37:09.000000 volcengine-1.0.9/volcengine/example/visual/example_goods_segment.py
+-rw-r--r--   0 root         (0) root         (0)      472 2021-04-08 02:37:09.000000 volcengine-1.0.9/volcengine/example/visual/example_goods_detect.py
+-rw-r--r--   0 root         (0) root         (0)      473 2021-04-08 02:37:09.000000 volcengine-1.0.9/volcengine/example/visual/example_image_inpaint.py
+-rw-r--r--   0 root         (0) root         (0)      473 2021-04-08 02:37:09.000000 volcengine-1.0.9/volcengine/example/visual/example_entity_detect.py
+-rw-r--r--   0 root         (0) root         (0)      499 2021-04-08 02:37:09.000000 volcengine-1.0.9/volcengine/example/visual/example_enhance_photo.py
+-rw-r--r--   0 root         (0) root         (0)        0 2021-04-08 02:37:09.000000 volcengine-1.0.9/volcengine/example/visual/__init__.py
+-rw-r--r--   0 root         (0) root         (0)      493 2021-04-08 02:37:09.000000 volcengine-1.0.9/volcengine/example/visual/example_video_inpaint_query_task.py
+-rw-r--r--   0 root         (0) root         (0)      497 2021-04-08 02:37:09.000000 volcengine-1.0.9/volcengine/example/visual/example_video_retargeting_query_task.py
+-rw-r--r--   0 root         (0) root         (0)      499 2021-04-08 02:37:09.000000 volcengine-1.0.9/volcengine/example/visual/example_convert_photo.py
+-rw-r--r--   0 root         (0) root         (0)      494 2021-04-08 02:37:09.000000 volcengine-1.0.9/volcengine/example/visual/example_jpcartoon.py
+-rw-r--r--   0 root         (0) root         (0)      498 2021-04-08 02:37:09.000000 volcengine-1.0.9/volcengine/example/visual/example_jpcartoon_cut.py
+-rw-r--r--   0 root         (0) root         (0)      499 2021-04-08 02:37:09.000000 volcengine-1.0.9/volcengine/example/visual/example_human_segment.py
+-rw-r--r--   0 root         (0) root         (0)      469 2021-04-08 02:37:09.000000 volcengine-1.0.9/volcengine/example/visual/example_image_cut.py
+-rw-r--r--   0 root         (0) root         (0)      495 2021-04-08 02:37:09.000000 volcengine-1.0.9/volcengine/example/visual/example_ocr_normal.py
+-rw-r--r--   0 root         (0) root         (0)      492 2021-04-08 02:37:09.000000 volcengine-1.0.9/volcengine/example/visual/example_id_card.py
+-rw-r--r--   0 root         (0) root         (0)      578 2021-04-08 02:37:09.000000 volcengine-1.0.9/volcengine/example/visual/example_face_swap.py
+-rw-r--r--   0 root         (0) root         (0)      478 2021-04-08 02:37:09.000000 volcengine-1.0.9/volcengine/example/visual/example_video_scene_detect.py
+-rw-r--r--   0 root         (0) root         (0)      495 2021-04-08 02:37:09.000000 volcengine-1.0.9/volcengine/example/visual/example_bank_card.py
+-rw-r--r--   0 root         (0) root         (0)      540 2021-04-08 02:37:09.000000 volcengine-1.0.9/volcengine/example/visual/example_video_retargeting_submit_task.py
+-rw-r--r--   0 root         (0) root         (0)      504 2021-04-08 02:37:09.000000 volcengine-1.0.9/volcengine/example/visual/example_video_over_resolution_submit_task.py
+-rw-r--r--   0 root         (0) root         (0)      475 2021-04-08 02:37:09.000000 volcengine-1.0.9/volcengine/example/visual/example_over_resolution.py
+-rw-r--r--   0 root         (0) root         (0)      512 2021-04-08 02:37:09.000000 volcengine-1.0.9/volcengine/example/visual/example_video_summarization_submit_task.py
+-rw-r--r--   0 root         (0) root         (0)      474 2021-04-08 02:37:09.000000 volcengine-1.0.9/volcengine/example/visual/example_image_outpaint.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2021-04-08 02:37:17.000000 volcengine-1.0.9/volcengine/example/imagex/
+-rw-r--r--   0 root         (0) root         (0)      406 2021-04-08 02:37:09.000000 volcengine-1.0.9/volcengine/example/imagex/example_get_image_info.py
+-rw-r--r--   0 root         (0) root         (0)      608 2021-04-08 02:37:09.000000 volcengine-1.0.9/volcengine/example/imagex/example_upload_image.py
+-rw-r--r--   0 root         (0) root         (0)      501 2021-04-08 02:37:09.000000 volcengine-1.0.9/volcengine/example/imagex/example_common.py
+-rw-r--r--   0 root         (0) root         (0)        0 2021-04-08 02:37:09.000000 volcengine-1.0.9/volcengine/example/imagex/__init__.py
+-rw-r--r--   0 root         (0) root         (0)      502 2021-04-08 02:37:09.000000 volcengine-1.0.9/volcengine/example/imagex/example_upload_sts2.py
+-rw-r--r--   0 root         (0) root         (0)      458 2021-04-08 02:37:09.000000 volcengine-1.0.9/volcengine/example/imagex/example_update_image.py
+-rw-r--r--   0 root         (0) root         (0)      454 2021-04-08 02:37:09.000000 volcengine-1.0.9/volcengine/example/imagex/example_upload_image_token.py
+-rw-r--r--   0 root         (0) root         (0)      408 2021-04-08 02:37:09.000000 volcengine-1.0.9/volcengine/example/imagex/example_delete_image.py
+-rw-r--r--   0 root         (0) root         (0)       13 2021-04-08 02:37:09.000000 volcengine-1.0.9/volcengine/example/__init__.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2021-04-08 02:37:17.000000 volcengine-1.0.9/volcengine/example/vedit/
+-rw-r--r--   0 root         (0) root         (0)     1220 2021-04-08 02:37:09.000000 volcengine-1.0.9/volcengine/example/vedit/example_edit.py
+-rw-r--r--   0 root         (0) root         (0)        0 2021-04-08 02:37:09.000000 volcengine-1.0.9/volcengine/example/vedit/__init__.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2021-04-08 02:37:17.000000 volcengine-1.0.9/volcengine/example/vod/
+drwxr-xr-x   0 root         (0) root         (0)        0 2021-04-08 02:37:17.000000 volcengine-1.0.9/volcengine/example/vod/play/
+-rw-r--r--   0 root         (0) root         (0)        0 2021-04-08 02:37:09.000000 volcengine-1.0.9/volcengine/example/vod/play/__init__.py
+-rw-r--r--   0 root         (0) root         (0)      592 2021-04-08 02:37:09.000000 volcengine-1.0.9/volcengine/example/vod/play/GetPlayAuthTokenExample.py
+-rw-r--r--   0 root         (0) root         (0)      778 2021-04-08 02:37:09.000000 volcengine-1.0.9/volcengine/example/vod/play/GetPlayInfoExample.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2021-04-08 02:37:17.000000 volcengine-1.0.9/volcengine/example/vod/workflow/
+-rw-r--r--   0 root         (0) root         (0)      924 2021-04-08 02:37:09.000000 volcengine-1.0.9/volcengine/example/vod/workflow/WorkflowExample.py
+-rw-r--r--   0 root         (0) root         (0)        0 2021-04-08 02:37:09.000000 volcengine-1.0.9/volcengine/example/vod/workflow/__init__.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2021-04-08 02:37:17.000000 volcengine-1.0.9/volcengine/example/vod/media/
+-rw-r--r--   0 root         (0) root         (0)     3111 2021-04-08 02:37:09.000000 volcengine-1.0.9/volcengine/example/vod/media/MediaExample.py
+-rw-r--r--   0 root         (0) root         (0)        0 2021-04-08 02:37:09.000000 volcengine-1.0.9/volcengine/example/vod/media/__init__.py
+-rw-r--r--   0 root         (0) root         (0)        0 2021-04-08 02:37:09.000000 volcengine-1.0.9/volcengine/example/vod/__init__.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2021-04-08 02:37:17.000000 volcengine-1.0.9/volcengine/example/vod/upload/
+-rw-r--r--   0 root         (0) root         (0)     1092 2021-04-08 02:37:09.000000 volcengine-1.0.9/volcengine/example/vod/upload/ApplyUploadInfoExample.py
+-rw-r--r--   0 root         (0) root         (0)        0 2021-04-08 02:37:09.000000 volcengine-1.0.9/volcengine/example/vod/upload/__init__.py
+-rw-r--r--   0 root         (0) root         (0)      445 2021-04-08 02:37:09.000000 volcengine-1.0.9/volcengine/example/vod/upload/UploadSts2.py
+-rw-r--r--   0 root         (0) root         (0)     1315 2021-04-08 02:37:09.000000 volcengine-1.0.9/volcengine/example/vod/upload/CommitUploadInfoExample.py
+-rw-r--r--   0 root         (0) root         (0)      990 2021-04-08 02:37:09.000000 volcengine-1.0.9/volcengine/example/vod/upload/UploadUrl.py
+-rw-r--r--   0 root         (0) root         (0)      933 2021-04-08 02:37:09.000000 volcengine-1.0.9/volcengine/example/vod/upload/QueryUploadTaskInfo.py
+-rw-r--r--   0 root         (0) root         (0)     1345 2021-04-08 02:37:09.000000 volcengine-1.0.9/volcengine/example/vod/upload/UploadMedia.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2021-04-08 02:37:18.000000 volcengine-1.0.9/volcengine/util/
+-rw-r--r--   0 root         (0) root         (0)        0 2021-04-08 02:37:09.000000 volcengine-1.0.9/volcengine/util/__init__.py
+-rw-r--r--   0 root         (0) root         (0)     3354 2021-04-08 02:37:09.000000 volcengine-1.0.9/volcengine/util/Util.py
+-rw-r--r--   0 root         (0) root         (0)      717 2021-04-08 02:37:09.000000 volcengine-1.0.9/volcengine/util/Functions.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2021-04-08 02:37:17.000000 volcengine-1.0.9/volcengine/adblocker/
+-rw-r--r--   0 root         (0) root         (0)        0 2021-04-08 02:37:09.000000 volcengine-1.0.9/volcengine/adblocker/__init__.py
+-rw-r--r--   0 root         (0) root         (0)     1647 2021-04-08 02:37:09.000000 volcengine-1.0.9/volcengine/adblocker/AdBlockerService.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2021-04-08 02:37:18.000000 volcengine-1.0.9/volcengine/vod/
+-rw-r--r--   0 root         (0) root         (0)    19351 2021-04-08 02:37:09.000000 volcengine-1.0.9/volcengine/vod/VodService.py
+-rw-r--r--   0 root         (0) root         (0)        0 2021-04-08 02:37:09.000000 volcengine-1.0.9/volcengine/vod/__init__.py
+-rw-r--r--   0 root         (0) root         (0)     3744 2021-04-08 02:37:09.000000 volcengine-1.0.9/volcengine/vod/VodServiceConfig.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2021-04-08 02:37:18.000000 volcengine-1.0.9/volcengine/sms/
+-rw-r--r--   0 root         (0) root         (0)        0 2021-04-08 02:37:09.000000 volcengine-1.0.9/volcengine/sms/__init__.py
+-rw-r--r--   0 root         (0) root         (0)     1444 2021-04-08 02:37:09.000000 volcengine-1.0.9/volcengine/sms/SmsService.py
+-rw-r--r--   0 root         (0) root         (0)      367 2021-04-08 02:37:09.000000 volcengine-1.0.9/volcengine/ServiceInfo.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2021-04-08 02:37:17.000000 volcengine-1.0.9/volcengine/business_security/
+-rw-r--r--   0 root         (0) root         (0)     2693 2021-04-08 02:37:09.000000 volcengine-1.0.9/volcengine/business_security/RiskDetectionService.py
+-rw-r--r--   0 root         (0) root         (0)        0 2021-04-08 02:37:09.000000 volcengine-1.0.9/volcengine/business_security/__init__.py
+-rw-r--r--   0 root         (0) root         (0)     2592 2021-04-08 02:37:09.000000 volcengine-1.0.9/volcengine/Policy.py
```

### Comparing `volcengine-1.0.84/volcengine/billing/BillingService.py` & `volcengine-1.0.9/volcengine/business_security/RiskDetectionService.py`

 * *Files 18% similar despite different names*

```diff
@@ -1,59 +1,63 @@
-# coding:utf-8
 import json
 import threading
+import redo
 
 from volcengine.ApiInfo import ApiInfo
 from volcengine.Credentials import Credentials
 from volcengine.base.Service import Service
 from volcengine.ServiceInfo import ServiceInfo
+from requests import exceptions
 
-SERVICE_VERSION = "2022-01-01"
 
-class BillingService(Service):
+class RiskDetectService(Service):
     _instance_lock = threading.Lock()
 
     def __new__(cls, *args, **kwargs):
-        if not hasattr(BillingService, "_instance"):
-            with BillingService._instance_lock:
-                if not hasattr(BillingService, "_instance"):
-                    BillingService._instance = object.__new__(cls)
-        return BillingService._instance
+        if not hasattr(RiskDetectService, "_instance"):
+            with RiskDetectService._instance_lock:
+                if not hasattr(RiskDetectService, "_instance"):
+                    RiskDetectService._instance = object.__new__(cls)
+        return RiskDetectService._instance
 
     def __init__(self):
-        self.service_info = BillingService.get_service_info()
-        self.api_info = BillingService.get_api_info()
-        super(BillingService, self).__init__(self.service_info, self.api_info)
+        self.service_info = RiskDetectService.get_service_info()
+        self.api_info = RiskDetectService.get_api_info()
+        super(RiskDetectService, self).__init__(self.service_info, self.api_info)
 
     @staticmethod
     def get_service_info():
-        service_info = ServiceInfo("billing.volcengineapi.com", {'Accept': 'application/json'},
-                                   Credentials('', '', 'billing', 'cn-north-1'), 5, 5)
+        service_info = ServiceInfo("open.volcengineapi.com", {'Accept': 'application/json'},
+                                   Credentials('', '', 'BusinessSecurity', 'cn-north-1'), 5, 5)
         return service_info
 
     @staticmethod
     def get_api_info():
-        api_info = {"ListBill": ApiInfo("POST", "/", {"Action": "ListBill", "Version": SERVICE_VERSION}, {}, {}),
-                    "ListBillDetail": ApiInfo("POST", "/", {"Action": "ListBillDetail", "Version": SERVICE_VERSION}, {}, {}),
-                    "ListBillOverviewByProd": ApiInfo("POST", "/", {"Action": "ListBillOverviewByProd", "Version": SERVICE_VERSION}, {}, {})}
+        api_info = {"RiskDetection": ApiInfo("POST", "/", {"Action": "RiskDetection", "Version": "2021-02-02"}, {}, {}),
+                    "AsyncRiskDetection": ApiInfo("POST", "/", {"Action": "AsyncRiskDetection", "Version": "2021-02-25"}, {}, {}),
+                    "RiskResult": ApiInfo("GET", "/", {"Action": "RiskResult", "Version": "2021-03-10"}, {}, {})}
+
         return api_info
 
-    def list_bill(self, params, body):
-        res = self.json("ListBill", params, json.dumps(body))
+    @redo.retriable(sleeptime=0.1, jitter=0.01, attempts=2, retry_exceptions=(exceptions.ConnectionError, exceptions.ConnectTimeout))
+    def risk_detect(self, params, body):
+        res = self.json("RiskDetection", params, json.dumps(body))
         if res == '':
             raise Exception("empty response")
         res_json = json.loads(res)
         return res_json
 
-    def list_bill_detail(self, params, body):
-        res = self.json("ListBillDetail", params, json.dumps(body))
+    @redo.retriable(sleeptime=0.1, jitter=0.01, attempts=2, retry_exceptions=(exceptions.ConnectionError, exceptions.ConnectTimeout))
+    def async_risk_detect(self, params, body):
+        res = self.json("AsyncRiskDetection", params, json.dumps(body))
         if res == '':
             raise Exception("empty response")
         res_json = json.loads(res)
         return res_json
 
-    def list_bill_overview_by_prod(self, params, body):
-        res = self.json("ListBillOverviewByProd", params, json.dumps(body))
+    @redo.retriable(sleeptime=0.1, jitter=0.01, attempts=2, retry_exceptions=(exceptions.ConnectionError, exceptions.ConnectTimeout))
+    def risk_result(self, params, body):
+        res = self.get("RiskResult", params, json.dumps(body))
         if res == '':
             raise Exception("empty response")
         res_json = json.loads(res)
         return res_json
```

### Comparing `volcengine-1.0.84/volcengine/vedit/VEditService.py` & `volcengine-1.0.9/volcengine/vedit/VEditService.py`

 * *Files identical despite different names*

### Comparing `volcengine-1.0.84/volcengine/util/Util.py` & `volcengine-1.0.9/volcengine/util/Util.py`

 * *Files 22% similar despite different names*

```diff
@@ -37,37 +37,20 @@
 
     @staticmethod
     def hmac_sha256(key, content):
         # type(key) == <class 'bytes'>
         if sys.version_info[0] == 3:
             return hmac.new(key, bytes(content, encoding='utf-8'), hashlib.sha256).digest()
         else:
-            return hmac.new(key, bytes(content.encode('utf-8')), hashlib.sha256).digest()
-
-    @staticmethod
-    def hmac_sha1(key, content):
-        # type(key) == <class 'bytes'>
-        if sys.version_info[0] == 3:
-            return hmac.new(key, bytes(content, encoding='utf-8'), hashlib.sha1).digest()
-        else:
-            return hmac.new(key, bytes(content.encode('utf-8')), hashlib.sha1).digest()
+            return hmac.new(key, content, hashlib.sha256).digest()
 
     @staticmethod
     def sha256(content):
         # type(content) == <class 'str'>
-        if sys.version_info[0] == 3:
-            if isinstance(content, str) is True:
-                return hashlib.sha256(content.encode('utf-8')).hexdigest()
-            else:
-                return hashlib.sha256(content).hexdigest()
-        else:
-            if isinstance(content, (str, unicode)) is True:
-                return hashlib.sha256(content.encode('utf-8')).hexdigest()
-            else:
-                return hashlib.sha256(content).hexdigest()
+        return hashlib.sha256(content.encode('utf-8')).hexdigest()
 
     @staticmethod
     def to_hex(content):
         lst = []
         for ch in content:
             if sys.version_info[0] == 3:
                 hv = hex(ch).replace('0x', '')
```

### Comparing `volcengine-1.0.84/volcengine/util/Functions.py` & `volcengine-1.0.9/volcengine/util/Functions.py`

 * *Files 19% similar despite different names*

```diff
@@ -4,23 +4,16 @@
         return {'Name': 'GetMeta'}
 
     @staticmethod
     def get_snapshot_func(snapshot_time):
         return {'Name': 'Snapshot', 'Input': {'SnapshotTime': snapshot_time}}
 
     @staticmethod
-    def get_add_option_info_func(title, tags, description, classification_id):
-        return {'Name': 'AddOptionInfo', 'Input': {'Title': title, 'Tags': tags, 'Description': description,
-                                                   'ClassificationId': classification_id}}
-
-    @staticmethod
-    def get_add_material_option_info_func(title, tags, description, category, record_type, format_input):
-        return {'Name': 'AddOptionInfo',
-                'Input': {'Title': title, 'Tags': tags, 'Description': description, 'Category': category,
-                          'RecordType': record_type, 'Format': format_input}}
+    def get_add_option_info_func(title, tags, description):
+        return {'Name': 'AddOptionInfo', 'Input': {'Title': title, 'Tags': tags, 'Description': description}}
 
     @staticmethod
     def get_start_workflow_func(template_id):
         return {'Name': 'StartWorkflow', 'Input': {'TemplateId': template_id}}
 
     @staticmethod
     def get_encryption_func(conf, policy):
```

### Comparing `volcengine-1.0.84/volcengine/base/Service.py` & `volcengine-1.0.9/volcengine/base/Service.py`

 * *Files 15% similar despite different names*

```diff
@@ -1,22 +1,17 @@
 # coding: utf-8
 import json
-import logging
 import os
 import time
 from collections import OrderedDict
 try:
     from urllib.parse import urlencode
 except ImportError:
     from urllib import urlencode
 
-try:
-    import configparser as configparser
-except ImportError:
-    import ConfigParser as configparser
 
 import requests
 
 from volcengine.Policy import SecurityToken2, InnerToken, ComplexEncoder
 from volcengine.auth.SignerV4 import SignerV4
 from volcengine.base.Request import Request
 from volcengine.util.Util import *
@@ -33,50 +28,30 @@
     def init(self):
         if 'VOLC_ACCESSKEY' in os.environ and 'VOLC_SECRETKEY' in os.environ:
             self.service_info.credentials.set_ak(os.environ['VOLC_ACCESSKEY'])
             self.service_info.credentials.set_sk(os.environ['VOLC_SECRETKEY'])
         else:
             if os.environ.get('HOME', None) is None:
                 return
-            # 先尝试从credentials中读取ak、sk，credentials不存在则从config中读取
-            path_ini = os.environ['HOME'] + '/.volc/credentials'
-            path_json = os.environ['HOME'] + '/.volc/config'
-            if os.path.isfile(path_ini):
-                conf = configparser.ConfigParser()
-                conf.read(path_ini)
-                default_section, ak_option, sk_option = "default", "access_key_id", "secret_access_key"
-                if conf.has_section(default_section):
-                    if conf.has_option(default_section, ak_option):
-                        ak = conf.get(default_section, ak_option)
-                        self.service_info.credentials.set_ak(ak)
-                    if conf.has_option(default_section, sk_option):
-                        sk = conf.get(default_section, sk_option)
-                        self.service_info.credentials.set_sk(sk)
-            elif os.path.isfile(path_json):
-                with open(path_json, 'r') as f:
-                    try:
-                        j = json.load(f)
-                    except Exception:
-                        logging.warning("%s is not json file", path_json)
-                        return
+
+            path = os.environ['HOME'] + '/.volc/config'
+            if os.path.isfile(path):
+                with open(path, 'r') as f:
+                    j = json.load(f)
                     if 'ak' in j:
                         self.service_info.credentials.set_ak(j['ak'])
                     if 'sk' in j:
                         self.service_info.credentials.set_sk(j['sk'])
 
-
     def set_ak(self, ak):
         self.service_info.credentials.set_ak(ak)
 
     def set_sk(self, sk):
         self.service_info.credentials.set_sk(sk)
 
-    def set_session_token(self, session_token):
-        self.service_info.credentials.set_session_token(session_token)
-
     def set_host(self, host):
         self.service_info.host = host
 
     def set_scheme(self, scheme):
         self.service_info.scheme = scheme
 
     def get_sign_url(self, api, params):
@@ -141,38 +116,35 @@
 
         url = r.build()
         resp = self.session.post(url, headers=r.headers, data=r.body,
                                  timeout=(self.service_info.connection_timeout, self.service_info.socket_timeout))
         if resp.status_code == 200:
             return json.dumps(resp.json())
         else:
-            raise Exception(resp.text.encode("utf-8"))
+            raise Exception(resp.text)
 
     def put(self, url, file_path, headers):
         with open(file_path, 'rb') as f:
             resp = self.session.put(url, headers=headers, data=f)
             if resp.status_code == 200:
-                return True, resp.text.encode("utf-8")
+                return True, resp.text
             else:
-                return False, resp.text.encode("utf-8")
+                return False, resp.text
 
     def put_data(self, url, data, headers):
         resp = self.session.put(url, headers=headers, data=data)
         if resp.status_code == 200:
-            return True, resp.text.encode("utf-8")
+            return True, resp.text
         else:
-            return False, resp.text.encode("utf-8")
+            return False, resp.text
 
     def prepare_request(self, api_info, params, doseq=0):
         for key in params:
-            if type(params[key]) == int or type(params[key]) == float or type(params[key]) == bool:
+            if type(params[key]) == int or type(params[key]) == float:
                 params[key] = str(params[key])
-            elif sys.version_info[0] != 3:
-                if type(params[key]) == unicode:
-                    params[key] = params[key].encode('utf-8')
             elif type(params[key]) == list:
                 if not doseq:
                     params[key] = ','.join(params[key])
 
         connection_timeout = self.service_info.connection_timeout
         socket_timeout = self.service_info.socket_timeout
```

#### encoding

```diff
@@ -1 +1 @@
-utf-8
+us-ascii
```

### Comparing `volcengine-1.0.84/volcengine/base/Request.py` & `volcengine-1.0.9/volcengine/base/Request.py`

 * *Files identical despite different names*

### Comparing `volcengine-1.0.84/volcengine/notify/notify.py` & `volcengine-1.0.9/volcengine/visual/VisualService.py`

 * *Files 16% similar despite different names*

```diff
@@ -1,279 +1,279 @@
 # coding:utf-8
+import json
 import threading
 
-import redo
-
 from volcengine.ApiInfo import ApiInfo
 from volcengine.Credentials import Credentials
-from volcengine.ServiceInfo import ServiceInfo
 from volcengine.base.Service import Service
-from volcengine.const.Const import *
-from volcengine.Policy import *
-from requests import exceptions
-
-
-NOTIFY_SERVICE_NAME = "volc_voice_notify"
-NOTIFY_API_VERSION = "2021-01-01"
-
-service_info_map = {
-    REGION_CN_NORTH1: ServiceInfo(
-        "cloud-vms.volcengineapi.com",
-        {'Accept': 'application/json'},
-        Credentials('', '', NOTIFY_SERVICE_NAME, REGION_CN_NORTH1),
-        10, 10
-    ),
-}
-
-notify_api_info = {
-    "CreateTask":
-        ApiInfo("POST", "/", {"Action": "CreateTask", "Version": NOTIFY_API_VERSION}, {}, {}),
-    "BatchAppend":
-        ApiInfo("POST", "/", {"Action": "BatchAppend", "Version": NOTIFY_API_VERSION}, {}, {}),
-    "PauseTask":
-        ApiInfo("POST", "/", {"Action": "PauseTask", "Version": NOTIFY_API_VERSION}, {}, {}),
-    "ResumeTask":
-        ApiInfo("POST", "/", {"Action": "ResumeTask", "Version": NOTIFY_API_VERSION}, {}, {}),
-    "StopTask":
-        ApiInfo("POST", "/", {"Action": "StopTask", "Version": NOTIFY_API_VERSION}, {}, {}),
-    "UpdateTask":
-        ApiInfo("POST", "/", {"Action": "UpdateTask", "Version": NOTIFY_API_VERSION}, {}, {}),
-    "SingleBatchAppend":
-        ApiInfo("POST", "/", {"Action": "SingleBatchAppend", "Version": NOTIFY_API_VERSION}, {}, {}),
-    "SingleInfo":
-        ApiInfo("GET", "/", {"Action": "SingleInfo", "Version": NOTIFY_API_VERSION}, {}, {}),
-    "SingleCancel":
-        ApiInfo("GET", "/", {"Action": "SingleCancel", "Version": NOTIFY_API_VERSION}, {}, {}),
-    "FetchResource":
-        ApiInfo("POST", "/", {"Action": "FetchResource", "Version": NOTIFY_API_VERSION}, {}, {}),
-    "OpenCreateTts":
-        ApiInfo("POST", "/", {"Action": "OpenCreateTts", "Version": NOTIFY_API_VERSION}, {}, {}),
-    "OpenDeleteResource":
-        ApiInfo("POST", "/", {"Action": "OpenDeleteResource", "Version": NOTIFY_API_VERSION}, {}, {}),
-    "GetResourceUploadUrl":
-        ApiInfo("POST", "/", {"Action": "GetResourceUploadUrl", "Version": NOTIFY_API_VERSION}, {}, {}),
-    "CommitResourceUpload":
-        ApiInfo("POST", "/", {"Action": "CommitResourceUpload", "Version": NOTIFY_API_VERSION}, {}, {}),
-    "OpenUpdateResource":
-        ApiInfo("POST", "/", {"Action": "OpenUpdateResource", "Version": NOTIFY_API_VERSION}, {}, {}),
-    "QueryUsableResource":
-        ApiInfo("POST", "/", {"Action": "QueryUsableResource", "Version": NOTIFY_API_VERSION}, {}, {}),
-    "QueryOpenGetResource":
-    ApiInfo("POST", "/", {"Action": "QueryOpenGetResource", "Version": NOTIFY_API_VERSION}, {}, {}),
-}
-
+from volcengine.ServiceInfo import ServiceInfo
 
-class NotifyService(Service):
 
+class VisualService(Service):
     _instance_lock = threading.Lock()
 
     def __new__(cls, *args, **kwargs):
-        if not hasattr(NotifyService, "_instance"):
-            with NotifyService._instance_lock:
-                if not hasattr(NotifyService, "_instance"):
-                    NotifyService._instance = object.__new__(cls)
-        return NotifyService._instance
-
-    def __init__(self, region=REGION_CN_NORTH1):
-        self.service_info = NotifyService.get_service_info(region)
-        self.api_info = NotifyService.get_api_info()
-        super(NotifyService, self).__init__(self.service_info, self.api_info)
+        if not hasattr(VisualService, "_instance"):
+            with VisualService._instance_lock:
+                if not hasattr(VisualService, "_instance"):
+                    VisualService._instance = object.__new__(cls)
+        return VisualService._instance
+
+    def __init__(self):
+        self.service_info = VisualService.get_service_info()
+        self.api_info = VisualService.get_api_info()
+        super(VisualService, self).__init__(self.service_info, self.api_info)
 
     @staticmethod
-    def get_service_info(region):
-        service_info = service_info_map.get(region, None)
-        if not service_info:
-            raise Exception('Notify service not support region %s' % region)
+    def get_service_info():
+        service_info = ServiceInfo("visual.volcengineapi.com", {},
+                                   Credentials('', '', 'cv', 'cn-north-1'), 10, 10)
         return service_info
 
     @staticmethod
     def get_api_info():
-        return notify_api_info
+        api_info = {
+            "JPCartoonCut": ApiInfo("POST", "/", {"Action": "JPCartoonCut", "Version": "2020-08-26"}, {}, {}),
+            "JPCartoon": ApiInfo("POST", "/", {"Action": "JPCartoon", "Version": "2020-08-26"}, {}, {}),
+            "IDCard": ApiInfo("POST", "/", {"Action": "IDCard", "Version": "2020-08-26"}, {}, {}),
+            "FaceSwap": ApiInfo("POST", "/", {"Action": "FaceSwap", "Version": "2020-08-26"}, {}, {}),
+            "OCRNormal": ApiInfo("POST", "/", {"Action": "OCRNormal", "Version": "2020-08-26"}, {}, {}),
+            "BankCard": ApiInfo("POST", "/", {"Action": "BankCard", "Version": "2020-08-26"}, {}, {}),
+            "HumanSegment": ApiInfo("POST", "/", {"Action": "HumanSegment", "Version": "2020-08-26"}, {}, {}),
+            "GeneralSegment": ApiInfo("POST", "/", {"Action": "GeneralSegment", "Version": "2020-08-26"}, {}, {}),
+            "EnhancePhoto": ApiInfo("POST", "/", {"Action": "EnhancePhoto", "Version": "2020-08-26"}, {}, {}),
+            "ConvertPhoto": ApiInfo("POST", "/", {"Action": "ConvertPhoto", "Version": "2020-08-26"}, {}, {}),
+            "VideoSceneDetect": ApiInfo("POST", "/", {"Action": "VideoSceneDetect", "Version": "2020-08-26"}, {}, {}),
+            "OverResolution": ApiInfo("POST", "/", {"Action": "OverResolution", "Version": "2020-08-26"}, {}, {}),
+            "GoodsSegment": ApiInfo("POST", "/", {"Action": "GoodsSegment", "Version": "2020-08-26"}, {}, {}),
+            "ImageOutpaint": ApiInfo("POST", "/", {"Action": "ImageOutpaint", "Version": "2020-08-26"}, {}, {}),
+            "ImageInpaint": ApiInfo("POST", "/", {"Action": "ImageInpaint", "Version": "2020-08-26"}, {}, {}),
+            "ImageCut": ApiInfo("POST", "/", {"Action": "ImageCut", "Version": "2020-08-26"}, {}, {}),
+            "EntityDetect": ApiInfo("POST", "/", {"Action": "EntityDetect", "Version": "2020-08-26"}, {}, {}),
+            "GoodsDetect": ApiInfo("POST", "/", {"Action": "GoodsDetect", "Version": "2020-08-26"}, {}, {}),
+            "VideoSummarizationSubmitTask": ApiInfo("POST", "/", {"Action": "VideoSummarizationSubmitTask", "Version": "2020-08-26"}, {}, {}),
+            "VideoSummarizationQueryTask": ApiInfo("GET", "/", {"Action": "VideoSummarizationQueryTask", "Version": "2020-08-26"}, {}, {}),
+            "VideoOverResolutionSubmitTask": ApiInfo("POST", "/", {"Action": "VideoOverResolutionSubmitTask", "Version": "2020-08-26"}, {}, {}),
+            "VideoOverResolutionQueryTask": ApiInfo("GET", "/", {"Action": "VideoOverResolutionQueryTask", "Version": "2020-08-26"}, {}, {}),
+            "VideoRetargetingSubmitTask": ApiInfo("POST", "/", {"Action": "VideoRetargetingSubmitTask", "Version": "2020-08-26"}, {}, {}),
+            "VideoRetargetingQueryTask": ApiInfo("GET", "/", {"Action": "VideoRetargetingQueryTask", "Version": "2020-08-26"}, {}, {}),
+            "VideoInpaintSubmitTask": ApiInfo("POST", "/", {"Action": "VideoInpaintSubmitTask", "Version": "2020-08-26"}, {}, {}),
+            "VideoInpaintQueryTask": ApiInfo("GET", "/", {"Action": "VideoInpaintQueryTask", "Version": "2020-08-26"}, {}, {}),
+        }
+        return api_info
 
-    def do_json_handler(self, api, body, params=dict()):
+    def common_handler(self, api, form):
+        params = dict()
         try:
-            res = self.json(api, params, json.dumps(body))
-            return json.loads(res)
+            res = self.post(api, params, form)
+            res_json = json.loads(res)
+            return res_json
         except Exception as e:
             res = str(e)
             try:
                 res_json = json.loads(res)
                 return res_json
             except:
                 raise Exception(str(e))
 
-    def do_query_handler(self, api, params):
+    def common_get_handler(self, api, params):
         try:
             res = self.get(api, params)
-            return json.loads(res)
+            res_json = json.loads(res)
+            return res_json
         except Exception as e:
             res = str(e)
             try:
                 res_json = json.loads(res)
                 return res_json
             except:
                 raise Exception(str(e))
 
-    def do_post_handler(self, api, form, params=dict()):
+    def jpcartoon_cut(self, form):
         try:
-            res = self.post(api, params, form)
-            return json.loads(res)
+            res_json = self.common_handler("JPCartoonCut", form)
+            return res_json
         except Exception as e:
-            res = str(e)
-            try:
-                res_json = json.loads(res)
-                return res_json
-            except:
-                raise Exception(str(e))
+            raise Exception(str(e))
+
+    def jpcartoon(self, form):
+        try:
+            res_json = self.common_handler("JPCartoon", form)
+            return res_json
+        except Exception as e:
+            raise Exception(str(e))
+
+    def id_card(self, form):
+        try:
+            res_json = self.common_handler("IDCard", form)
+            return res_json
+        except Exception as e:
+            raise Exception(str(e))
 
-    @redo.retriable(sleeptime=0.1, jitter=0.01, attempts=2,
-                    retry_exceptions=(exceptions.ConnectionError, exceptions.ConnectTimeout))
-    def create_task(self, body):
+    def face_swap(self, form):
         try:
-            res_json = self.do_json_handler("CreateTask", body)
+            res_json = self.common_handler("FaceSwap", form)
             return res_json
         except Exception as e:
             raise Exception(str(e))
 
-    @redo.retriable(sleeptime=0.1, jitter=0.01, attempts=2,
-                    retry_exceptions=(exceptions.ConnectionError, exceptions.ConnectTimeout))
-    def batch_append_task(self, body):
+    def ocr_normal(self, form):
         try:
-            res_json = self.do_json_handler("BatchAppend", body)
+            res_json = self.common_handler("OCRNormal", form)
             return res_json
         except Exception as e:
             raise Exception(str(e))
 
-    @redo.retriable(sleeptime=0.1, jitter=0.01, attempts=2,
-                    retry_exceptions=(exceptions.ConnectionError, exceptions.ConnectTimeout))
-    def update_task(self, body):
+    def bank_card(self, form):
         try:
-            res_json = self.do_json_handler("UpdateTask", body)
+            res_json = self.common_handler("BankCard", form)
             return res_json
         except Exception as e:
             raise Exception(str(e))
 
-    @redo.retriable(sleeptime=0.1, jitter=0.01, attempts=2,
-                    retry_exceptions=(exceptions.ConnectionError, exceptions.ConnectTimeout))
-    def pause_task(self, params):
+    def human_segment(self, form):
         try:
-            res_json = self.do_json_handler("PauseTask", dict(), params)
+            res_json = self.common_handler("HumanSegment", form)
             return res_json
         except Exception as e:
             raise Exception(str(e))
 
-    @redo.retriable(sleeptime=0.1, jitter=0.01, attempts=2,
-                    retry_exceptions=(exceptions.ConnectionError, exceptions.ConnectTimeout))
-    def resume_task(self, params):
+    def general_segment(self, form):
         try:
-            res_json = self.do_json_handler("ResumeTask", dict(), params)
+            res_json = self.common_handler("GeneralSegment", form)
             return res_json
         except Exception as e:
             raise Exception(str(e))
 
-    @redo.retriable(sleeptime=0.1, jitter=0.01, attempts=2,
-                    retry_exceptions=(exceptions.ConnectionError, exceptions.ConnectTimeout))
-    def stop_task(self, params):
+    def enhance_photo(self, form):
         try:
-            res_json = self.do_json_handler("StopTask", dict(), params)
+            res_json = self.common_handler("EnhancePhoto", form)
             return res_json
         except Exception as e:
             raise Exception(str(e))
 
-    @redo.retriable(sleeptime=0.1, jitter=0.01, attempts=2,
-                    retry_exceptions=(exceptions.ConnectionError, exceptions.ConnectTimeout))
-    def single_batch_append(self, body):
+    def convert_photo(self, form):
         try:
-            res_json = self.do_json_handler("SingleBatchAppend", body)
+            res_json = self.common_handler("ConvertPhoto", form)
             return res_json
         except Exception as e:
             raise Exception(str(e))
 
-    @redo.retriable(sleeptime=0.1, jitter=0.01, attempts=2,
-                    retry_exceptions=(exceptions.ConnectionError, exceptions.ConnectTimeout))
-    def single_info(self, params):
+    def video_scene_detect(self, form):
         try:
-            res_json = self.do_query_handler("SingleInfo", params)
+            res_json = self.common_handler("VideoSceneDetect", form)
             return res_json
         except Exception as e:
             raise Exception(str(e))
 
-    @redo.retriable(sleeptime=0.1, jitter=0.01, attempts=2,
-                    retry_exceptions=(exceptions.ConnectionError, exceptions.ConnectTimeout))
-    def single_cancel(self, params):
+    def over_resolution(self, form):
         try:
-            res_json = self.do_query_handler("SingleCancel", params)
+            res_json = self.common_handler("OverResolution", form)
             return res_json
         except Exception as e:
             raise Exception(str(e))
 
-    @redo.retriable(sleeptime=0.1, jitter=0.01, attempts=2,
-                    retry_exceptions=(exceptions.ConnectionError, exceptions.ConnectTimeout))
-    def fetch_resource(self, body):
+    def goods_segment(self, form):
         try:
-            res_json = self.do_json_handler("FetchResource", body)
+            res_json = self.common_handler("GoodsSegment", form)
             return res_json
         except Exception as e:
             raise Exception(str(e))
 
-    @redo.retriable(sleeptime=0.1, jitter=0.01, attempts=2,
-                    retry_exceptions=(exceptions.ConnectionError, exceptions.ConnectTimeout))
-    def create_tts(self, body):
+    def image_outpaint(self, form):
         try:
-            res_json = self.do_json_handler("OpenCreateTts", body)
+            res_json = self.common_handler("ImageOutpaint", form)
             return res_json
         except Exception as e:
             raise Exception(str(e))
 
-    @redo.retriable(sleeptime=0.1, jitter=0.01, attempts=2,
-                    retry_exceptions=(exceptions.ConnectionError, exceptions.ConnectTimeout))
-    def delete_resource(self, params):
+    def image_inpaint(self, form):
         try:
-            res_json = self.do_json_handler("OpenDeleteResource", dict(), params)
+            res_json = self.common_handler("ImageInpaint", form)
             return res_json
         except Exception as e:
             raise Exception(str(e))
 
-    @redo.retriable(sleeptime=0.1, jitter=0.01, attempts=2,
-                    retry_exceptions=(exceptions.ConnectionError, exceptions.ConnectTimeout))
-    def get_resource_upload_url(self, body):
+    def image_cut(self, form):
         try:
-            res_json = self.do_json_handler("GetResourceUploadUrl", body)
+            res_json = self.common_handler("ImageCut", form)
             return res_json
         except Exception as e:
             raise Exception(str(e))
 
-    @redo.retriable(sleeptime=0.1, jitter=0.01, attempts=2,
-                    retry_exceptions=(exceptions.ConnectionError, exceptions.ConnectTimeout))
-    def commit_resource_upload(self, body):
+    def entity_detect(self, form):
         try:
-            res_json = self.do_json_handler("CommitResourceUpload", body)
+            res_json = self.common_handler("EntityDetect", form)
             return res_json
         except Exception as e:
             raise Exception(str(e))
-    
-    @redo.retriable(sleeptime=0.1, jitter=0.01, attempts=2,
-                    retry_exceptions=(exceptions.ConnectionError, exceptions.ConnectTimeout))
-    def open_update_resource(self, params):
+
+    def goods_detect(self, form):
+        try:
+            res_json = self.common_handler("GoodsDetect", form)
+            return res_json
+        except Exception as e:
+            raise Exception(str(e))
+
+    def video_summarization_submit_task(self, form):
+        try:
+            res_json = self.common_handler(
+                "VideoSummarizationSubmitTask", form)
+            return res_json
+        except Exception as e:
+            raise Exception(str(e))
+
+    def video_summarization_query_task(self, params):
+        try:
+            res_json = self.common_get_handler(
+                "VideoSummarizationQueryTask", params)
+            return res_json
+        except Exception as e:
+            raise Exception(str(e))
+
+    def video_over_resolution_submit_task(self, form):
+        try:
+            res_json = self.common_handler(
+                "VideoOverResolutionSubmitTask", form)
+            return res_json
+        except Exception as e:
+            raise Exception(str(e))
+
+    def video_over_resolution_query_task(self, params):
+        try:
+            res_json = self.common_get_handler(
+                "VideoOverResolutionQueryTask", params)
+            return res_json
+        except Exception as e:
+            raise Exception(str(e))
+
+    def video_retargeting_submit_task(self, form):
+        try:
+            res_json = self.common_handler(
+                "VideoRetargetingSubmitTask", form)
+            return res_json
+        except Exception as e:
+            raise Exception(str(e))
+
+    def video_retargeting_query_task(self, params):
         try:
-            res_json = self.do_post_handler("OpenUpdateResource", {}, params)
+            res_json = self.common_get_handler(
+                "VideoRetargetingQueryTask", params)
             return res_json
         except Exception as e:
             raise Exception(str(e))
 
-    @redo.retriable(sleeptime=0.1, jitter=0.01, attempts=2,
-                    retry_exceptions=(exceptions.ConnectionError, exceptions.ConnectTimeout))
-    def query_usable_resource(self, params):
+    def video_inpaint_submit_task(self, form):
         try:
-            res_json = self.do_post_handler("QueryUsableResource", {}, params)
+            res_json = self.common_handler(
+                "VideoInpaintSubmitTask", form)
             return res_json
         except Exception as e:
             raise Exception(str(e))
 
-    @redo.retriable(sleeptime=0.1, jitter=0.01, attempts=2,
-                    retry_exceptions=(exceptions.ConnectionError, exceptions.ConnectTimeout))
-    def query_open_get_resource(self, body):
+    def video_inpaint_query_task(self, params):
         try:
-            res_json = self.do_json_handler("QueryOpenGetResource", body)
+            res_json = self.common_get_handler(
+                "VideoInpaintQueryTask", params)
             return res_json
         except Exception as e:
             raise Exception(str(e))
```

### Comparing `volcengine-1.0.84/volcengine/adblocker/AdBlockerService.py` & `volcengine-1.0.9/volcengine/adblocker/AdBlockerService.py`

 * *Files 11% similar despite different names*

```diff
@@ -21,15 +21,15 @@
     def __init__(self):
         self.service_info = AdBlockService.get_service_info()
         self.api_info = AdBlockService.get_api_info()
         super(AdBlockService, self).__init__(self.service_info, self.api_info)
 
     @staticmethod
     def get_service_info():
-        service_info = ServiceInfo("riskcontrol.volcengineapi.com", {'Accept': 'application/json'},
+        service_info = ServiceInfo("open.volcengineapi.com", {'Accept': 'application/json'},
                                    Credentials('', '', 'AdBlocker', 'cn-north-1'), 5, 5)
         return service_info
 
     @staticmethod
     def get_api_info():
         api_info = {"AdBlock": ApiInfo("POST", "/", {"Action": "AdBlock", "Version": "2021-01-06"}, {}, {})}
         return api_info
```

### Comparing `volcengine-1.0.84/volcengine/imp/ImpServiceConfig.py` & `volcengine-1.0.9/volcengine/iam/IamService.py`

 * *Files 21% similar despite different names*

```diff
@@ -1,59 +1,42 @@
 # coding:utf-8
-
-from __future__ import print_function
-
+import json
 import threading
-from zlib import crc32
 
 from volcengine.ApiInfo import ApiInfo
 from volcengine.Credentials import Credentials
-from volcengine.ServiceInfo import ServiceInfo
 from volcengine.base.Service import Service
+from volcengine.ServiceInfo import ServiceInfo
 
 
-class ImpServiceConfig(Service):
+class IamService(Service):
     _instance_lock = threading.Lock()
 
     def __new__(cls, *args, **kwargs):
-        if not hasattr(cls, "_instance"):
-            with cls._instance_lock:
-                if not hasattr(cls, "_instance"):
-                    cls._instance = object.__new__(cls)
-        return cls._instance
-
-    def __init__(self, region='cn-north-1'):
-        self.service_info = ImpServiceConfig.get_service_info(region)
-        self.api_info = ImpServiceConfig.get_api_info()
-        self.domain_cache = {}
-        self.fallback_domain_weights = {}
-        self.update_interval = 10
-        self.lock = threading.Lock()
-        super(ImpServiceConfig, self).__init__(self.service_info, self.api_info)
+        if not hasattr(IamService, "_instance"):
+            with IamService._instance_lock:
+                if not hasattr(IamService, "_instance"):
+                    IamService._instance = object.__new__(cls)
+        return IamService._instance
+
+    def __init__(self):
+        self.service_info = IamService.get_service_info()
+        self.api_info = IamService.get_api_info()
+        super(IamService, self).__init__(self.service_info, self.api_info)
 
     @staticmethod
-    def get_service_info(region):
-        service_info_map = {
-            'cn-north-1': ServiceInfo("imp.volcengineapi.com", {'Accept': 'application/json'},
-                                      Credentials('', '', 'imp', 'cn-north-1'), 10, 10),
-        }
-        service_info = service_info_map.get(region, None)
-        if not service_info:
-            raise Exception('Cant find the region, please check it carefully')
-
+    def get_service_info():
+        service_info = ServiceInfo("open.volcengineapi.com", {'Accept': 'application/json'},
+                                   Credentials('', '', 'iam', 'cn-north-1'), 5, 5)
         return service_info
 
     @staticmethod
     def get_api_info():
-        api_info = {
-            "SubmitJob": ApiInfo("GET", "/", {"Action": "SubmitJob", "Version": "2021-06-11"}, {}, {}),
-            "KillJob": ApiInfo("GET", "/", {"Action": "KillJob", "Version": "2021-06-11"}, {}, {}),
-            "RetrieveJob": ApiInfo("GET", "/", {"Action": "RetrieveJob", "Version": "2021-06-11"}, {}, {}),
-        }
+        api_info = {"ListUsers": ApiInfo("GET", "/", {"Action": "ListUsers", "Version": "2018-01-01"}, {}, {})}
         return api_info
 
-    @staticmethod
-    def crc32(file_path):
-        prev = 0
-        for eachLine in open(file_path, "rb"):
-            prev = crc32(eachLine, prev)
-        return prev & 0xFFFFFFFF
+    def list_users(self, params):
+        res = self.get("ListUsers", params)
+        if res == '':
+            raise Exception("empty response")
+        res_json = json.loads(res)
+        return res_json
```

### Comparing `volcengine-1.0.84/volcengine/imp/models/base/base_pb2.py` & `volcengine-1.0.9/volcengine/models/base/base_pb2.py`

 * *Files 4% similar despite different names*

```diff
@@ -12,70 +12,70 @@
 
 
 from google.protobuf import descriptor_pb2 as google_dot_protobuf_dot_descriptor__pb2
 
 
 DESCRIPTOR = _descriptor.FileDescriptor(
   name='base/base.proto',
-  package='Volcengine.Vod.Models.Base',
+  package='Volcengine.Models.Base',
   syntax='proto3',
-  serialized_options=b'\n%com.volcengine.service.vod.model.baseB\004BaseP\001Z=github.com/volcengine/volc-sdk-golang/service/vod/models/base\240\001\001\330\001\001\302\002\000\312\002\034Volc\\Service\\Vod\\Models\\Base\342\002#Volc\\Service\\Vod\\Models\\GPBMetadata',
+  serialized_options=b'\n\031com.volcengine.model.baseB\004BaseP\001Z1github.com/volcengine/volc-sdk-golang/models/base\240\001\001\330\001\001\302\002\000\312\002\020Volc\\Models\\Base\342\002\034Volc\\Models\\Base\\GPBMetadata',
   create_key=_descriptor._internal_create_key,
-  serialized_pb=b'\n\x0f\x62\x61se/base.proto\x12\x1aVolcengine.Vod.Models.Base\x1a google/protobuf/descriptor.proto\"\xa1\x01\n\x10ResponseMetadata\x12\x11\n\tRequestId\x18\x01 \x01(\t\x12\x0e\n\x06\x41\x63tion\x18\x02 \x01(\t\x12\x0f\n\x07Version\x18\x03 \x01(\t\x12\x0f\n\x07Service\x18\x04 \x01(\t\x12\x0e\n\x06Region\x18\x05 \x01(\t\x12\x38\n\x05\x45rror\x18\x06 \x01(\x0b\x32).Volcengine.Vod.Models.Base.ResponseError\".\n\rResponseError\x12\x0c\n\x04\x43ode\x18\x01 \x01(\t\x12\x0f\n\x07Message\x18\x02 \x01(\tB\xbc\x01\n%com.volcengine.service.vod.model.baseB\x04\x42\x61seP\x01Z=github.com/volcengine/volc-sdk-golang/service/vod/models/base\xa0\x01\x01\xd8\x01\x01\xc2\x02\x00\xca\x02\x1cVolc\\Service\\Vod\\Models\\Base\xe2\x02#Volc\\Service\\Vod\\Models\\GPBMetadatab\x06proto3'
+  serialized_pb=b'\n\x0f\x62\x61se/base.proto\x12\x16Volcengine.Models.Base\x1a google/protobuf/descriptor.proto\"\x9d\x01\n\x10ResponseMetadata\x12\x11\n\tRequestId\x18\x01 \x01(\t\x12\x0e\n\x06\x41\x63tion\x18\x02 \x01(\t\x12\x0f\n\x07Version\x18\x03 \x01(\t\x12\x0f\n\x07Service\x18\x04 \x01(\t\x12\x0e\n\x06Region\x18\x05 \x01(\t\x12\x34\n\x05\x45rror\x18\x06 \x01(\x0b\x32%.Volcengine.Models.Base.ResponseError\".\n\rResponseError\x12\x0c\n\x04\x43ode\x18\x01 \x01(\t\x12\x0f\n\x07Message\x18\x02 \x01(\tB\x91\x01\n\x19\x63om.volcengine.model.baseB\x04\x42\x61seP\x01Z1github.com/volcengine/volc-sdk-golang/models/base\xa0\x01\x01\xd8\x01\x01\xc2\x02\x00\xca\x02\x10Volc\\Models\\Base\xe2\x02\x1cVolc\\Models\\Base\\GPBMetadatab\x06proto3'
   ,
   dependencies=[google_dot_protobuf_dot_descriptor__pb2.DESCRIPTOR,])
 
 
 
 
 _RESPONSEMETADATA = _descriptor.Descriptor(
   name='ResponseMetadata',
-  full_name='Volcengine.Vod.Models.Base.ResponseMetadata',
+  full_name='Volcengine.Models.Base.ResponseMetadata',
   filename=None,
   file=DESCRIPTOR,
   containing_type=None,
   create_key=_descriptor._internal_create_key,
   fields=[
     _descriptor.FieldDescriptor(
-      name='RequestId', full_name='Volcengine.Vod.Models.Base.ResponseMetadata.RequestId', index=0,
+      name='RequestId', full_name='Volcengine.Models.Base.ResponseMetadata.RequestId', index=0,
       number=1, type=9, cpp_type=9, label=1,
       has_default_value=False, default_value=b"".decode('utf-8'),
       message_type=None, enum_type=None, containing_type=None,
       is_extension=False, extension_scope=None,
       serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
     _descriptor.FieldDescriptor(
-      name='Action', full_name='Volcengine.Vod.Models.Base.ResponseMetadata.Action', index=1,
+      name='Action', full_name='Volcengine.Models.Base.ResponseMetadata.Action', index=1,
       number=2, type=9, cpp_type=9, label=1,
       has_default_value=False, default_value=b"".decode('utf-8'),
       message_type=None, enum_type=None, containing_type=None,
       is_extension=False, extension_scope=None,
       serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
     _descriptor.FieldDescriptor(
-      name='Version', full_name='Volcengine.Vod.Models.Base.ResponseMetadata.Version', index=2,
+      name='Version', full_name='Volcengine.Models.Base.ResponseMetadata.Version', index=2,
       number=3, type=9, cpp_type=9, label=1,
       has_default_value=False, default_value=b"".decode('utf-8'),
       message_type=None, enum_type=None, containing_type=None,
       is_extension=False, extension_scope=None,
       serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
     _descriptor.FieldDescriptor(
-      name='Service', full_name='Volcengine.Vod.Models.Base.ResponseMetadata.Service', index=3,
+      name='Service', full_name='Volcengine.Models.Base.ResponseMetadata.Service', index=3,
       number=4, type=9, cpp_type=9, label=1,
       has_default_value=False, default_value=b"".decode('utf-8'),
       message_type=None, enum_type=None, containing_type=None,
       is_extension=False, extension_scope=None,
       serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
     _descriptor.FieldDescriptor(
-      name='Region', full_name='Volcengine.Vod.Models.Base.ResponseMetadata.Region', index=4,
+      name='Region', full_name='Volcengine.Models.Base.ResponseMetadata.Region', index=4,
       number=5, type=9, cpp_type=9, label=1,
       has_default_value=False, default_value=b"".decode('utf-8'),
       message_type=None, enum_type=None, containing_type=None,
       is_extension=False, extension_scope=None,
       serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
     _descriptor.FieldDescriptor(
-      name='Error', full_name='Volcengine.Vod.Models.Base.ResponseMetadata.Error', index=5,
+      name='Error', full_name='Volcengine.Models.Base.ResponseMetadata.Error', index=5,
       number=6, type=11, cpp_type=10, label=1,
       has_default_value=False, default_value=None,
       message_type=None, enum_type=None, containing_type=None,
       is_extension=False, extension_scope=None,
       serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
   ],
   extensions=[
@@ -85,36 +85,36 @@
   ],
   serialized_options=None,
   is_extendable=False,
   syntax='proto3',
   extension_ranges=[],
   oneofs=[
   ],
-  serialized_start=82,
-  serialized_end=243,
+  serialized_start=78,
+  serialized_end=235,
 )
 
 
 _RESPONSEERROR = _descriptor.Descriptor(
   name='ResponseError',
-  full_name='Volcengine.Vod.Models.Base.ResponseError',
+  full_name='Volcengine.Models.Base.ResponseError',
   filename=None,
   file=DESCRIPTOR,
   containing_type=None,
   create_key=_descriptor._internal_create_key,
   fields=[
     _descriptor.FieldDescriptor(
-      name='Code', full_name='Volcengine.Vod.Models.Base.ResponseError.Code', index=0,
+      name='Code', full_name='Volcengine.Models.Base.ResponseError.Code', index=0,
       number=1, type=9, cpp_type=9, label=1,
       has_default_value=False, default_value=b"".decode('utf-8'),
       message_type=None, enum_type=None, containing_type=None,
       is_extension=False, extension_scope=None,
       serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
     _descriptor.FieldDescriptor(
-      name='Message', full_name='Volcengine.Vod.Models.Base.ResponseError.Message', index=1,
+      name='Message', full_name='Volcengine.Models.Base.ResponseError.Message', index=1,
       number=2, type=9, cpp_type=9, label=1,
       has_default_value=False, default_value=b"".decode('utf-8'),
       message_type=None, enum_type=None, containing_type=None,
       is_extension=False, extension_scope=None,
       serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
   ],
   extensions=[
@@ -124,33 +124,33 @@
   ],
   serialized_options=None,
   is_extendable=False,
   syntax='proto3',
   extension_ranges=[],
   oneofs=[
   ],
-  serialized_start=245,
-  serialized_end=291,
+  serialized_start=237,
+  serialized_end=283,
 )
 
 _RESPONSEMETADATA.fields_by_name['Error'].message_type = _RESPONSEERROR
 DESCRIPTOR.message_types_by_name['ResponseMetadata'] = _RESPONSEMETADATA
 DESCRIPTOR.message_types_by_name['ResponseError'] = _RESPONSEERROR
 _sym_db.RegisterFileDescriptor(DESCRIPTOR)
 
 ResponseMetadata = _reflection.GeneratedProtocolMessageType('ResponseMetadata', (_message.Message,), {
   'DESCRIPTOR' : _RESPONSEMETADATA,
   '__module__' : 'base.base_pb2'
-  # @@protoc_insertion_point(class_scope:Volcengine.Vod.Models.Base.ResponseMetadata)
+  # @@protoc_insertion_point(class_scope:Volcengine.Models.Base.ResponseMetadata)
   })
 _sym_db.RegisterMessage(ResponseMetadata)
 
 ResponseError = _reflection.GeneratedProtocolMessageType('ResponseError', (_message.Message,), {
   'DESCRIPTOR' : _RESPONSEERROR,
   '__module__' : 'base.base_pb2'
-  # @@protoc_insertion_point(class_scope:Volcengine.Vod.Models.Base.ResponseError)
+  # @@protoc_insertion_point(class_scope:Volcengine.Models.Base.ResponseError)
   })
 _sym_db.RegisterMessage(ResponseError)
 
 
 DESCRIPTOR._options = None
 # @@protoc_insertion_point(module_scope)
```

### Comparing `volcengine-1.0.84/volcengine/imp/models/business/imp_common_pb2.py` & `volcengine-1.0.9/volcengine/models/vod/business/vod_play_pb2.py`

 * *Files 19% similar despite different names*

```diff
@@ -1,162 +1,165 @@
 # -*- coding: utf-8 -*-
 # Generated by the protocol buffer compiler.  DO NOT EDIT!
-# source: imp/business/imp_common.proto
+# source: vod/business/vod_play.proto
 
+from google.protobuf.internal import enum_type_wrapper
 from google.protobuf import descriptor as _descriptor
 from google.protobuf import message as _message
 from google.protobuf import reflection as _reflection
 from google.protobuf import symbol_database as _symbol_database
 # @@protoc_insertion_point(imports)
 
 _sym_db = _symbol_database.Default()
 
 
+from volcengine.models.vod.business import vod_common_pb2 as vod_dot_business_dot_vod__common__pb2
 
 
 DESCRIPTOR = _descriptor.FileDescriptor(
-  name='imp/business/imp_common.proto',
-  package='Volcengine.Imp.Models.Business',
+  name='vod/business/vod_play.proto',
+  package='Volcengine.Models.Vod.Business',
   syntax='proto3',
-  serialized_options=b'\n)com.volcengine.service.imp.model.businessB\013ImpWorkflowP\001ZAgithub.com/volcengine/volc-sdk-golang/service/imp/models/business\240\001\001\330\001\001\312\002 Volc\\Service\\Imp\\Models\\Business\342\002#Volc\\Service\\Imp\\Models\\GPBMetadata',
+  serialized_options=b'\n!com.volcengine.model.vod.businessB\007VodPlayP\001Z9github.com/volcengine/volc-sdk-golang/models/vod/business\240\001\001\330\001\001\302\002\000\312\002\030Volc\\Models\\Vod\\Business\342\002\033Volc\\Models\\Vod\\GPBMetadata',
   create_key=_descriptor._internal_create_key,
-  serialized_pb=b'\n\x1dimp/business/imp_common.proto\x12\x1eVolcengine.Imp.Models.Business\"R\n\tInputPath\x12\x0c\n\x04Type\x18\x01 \x01(\t\x12\x11\n\tTosBucket\x18\x02 \x01(\t\x12\x14\n\x0cVodSpaceName\x18\x03 \x01(\t\x12\x0e\n\x06\x46ileId\x18\x04 \x01(\t\"\xc8\x01\n\tJobOutput\x12\x12\n\nTemplateId\x18\x01 \x01(\t\x12\x12\n\nProperties\x18\x02 \x01(\t\x12\x0c\n\x04\x43ode\x18\x03 \x01(\t\x12\x15\n\rFileMessageId\x18\x04 \x01(\t\x12\x10\n\x08TaskType\x18\x05 \x01(\t\x12\x0e\n\x06Status\x18\x06 \x01(\t\x12\x12\n\nActivityId\x18\x07 \x01(\t\x12\x11\n\tStartTime\x18\x08 \x01(\t\x12\x0f\n\x07\x45ndTime\x18\t \x01(\t\x12\x14\n\x0cTemplateName\x18\n \x01(\t\"\xe0\x01\n\x0cJobExecution\x12\r\n\x05JobId\x18\x01 \x01(\t\x12<\n\tInputPath\x18\x02 \x01(\x0b\x32).Volcengine.Imp.Models.Business.InputPath\x12\x39\n\x06Output\x18\x03 \x03(\x0b\x32).Volcengine.Imp.Models.Business.JobOutput\x12\x0e\n\x06Status\x18\x04 \x01(\t\x12\x10\n\x08\x43reateAt\x18\x05 \x01(\t\x12\x12\n\nFinishedAt\x18\x06 \x01(\t\x12\x12\n\nTemplateId\x18\x07 \x01(\tB\xcc\x01\n)com.volcengine.service.imp.model.businessB\x0bImpWorkflowP\x01ZAgithub.com/volcengine/volc-sdk-golang/service/imp/models/business\xa0\x01\x01\xd8\x01\x01\xca\x02 Volc\\Service\\Imp\\Models\\Business\xe2\x02#Volc\\Service\\Imp\\Models\\GPBMetadatab\x06proto3'
+  serialized_pb=b'\n\x1bvod/business/vod_play.proto\x12\x1eVolcengine.Models.Vod.Business\x1a\x1dvod/business/vod_common.proto\"\xab\x03\n\x10VodPlayInfoModel\x12H\n\x07Version\x18\n \x01(\x0e\x32\x37.Volcengine.Models.Vod.Business.VodPlayInfoModelVersion\x12\x0b\n\x03Vid\x18\x01 \x01(\t\x12\x0e\n\x06Status\x18\x02 \x01(\x05\x12\x11\n\tPosterUrl\x18\x03 \x01(\t\x12\x10\n\x08\x44uration\x18\x04 \x01(\x02\x12\x10\n\x08\x46ileType\x18\x05 \x01(\t\x12\x16\n\x0e\x45nableAdaptive\x18\x06 \x01(\x08\x12\x12\n\nTotalCount\x18\x07 \x01(\x05\x12\x45\n\x0c\x41\x64\x61ptiveInfo\x18\x08 \x01(\x0b\x32/.Volcengine.Models.Vod.Business.VodAdaptiveInfo\x12\x41\n\x0cPlayInfoList\x18\t \x03(\x0b\x32+.Volcengine.Models.Vod.Business.VodPlayInfo\x12\x43\n\rThumbInfoList\x18\x0b \x03(\x0b\x32,.Volcengine.Models.Vod.Business.VodThumbInfo\"\xd8\x01\n\x1cVodGetOriginalPlayInfoResult\x12\x10\n\x08\x46ileType\x18\x01 \x01(\t\x12\x10\n\x08\x44uration\x18\x02 \x01(\x02\x12\x0c\n\x04Size\x18\x03 \x01(\x01\x12\x0e\n\x06Height\x18\x04 \x01(\x05\x12\r\n\x05Width\x18\x05 \x01(\x05\x12\x0e\n\x06\x46ormat\x18\x06 \x01(\t\x12\r\n\x05\x43odec\x18\x07 \x01(\t\x12\x0f\n\x07\x42itrate\x18\x08 \x01(\x05\x12\x0b\n\x03Md5\x18\t \x01(\t\x12\x13\n\x0bMainPlayUrl\x18\n \x01(\t\x12\x15\n\rBackupPlayUrl\x18\x0b \x01(\t*\xd6\x01\n\x17VodPlayInfoModelVersion\x12$\n UndefinedVodPlayInfoModelVersion\x10\x00\x12%\n!InternalV1VodPlayInfoModelVersion\x10\x01\x12%\n!InternalV2VodPlayInfoModelVersion\x10\x02\x12%\n!InternalV3VodPlayInfoModelVersion\x10\x03\x12 \n\x1cToBV1VodPlayInfoModelVersion\x10\x04\x42\xab\x01\n!com.volcengine.model.vod.businessB\x07VodPlayP\x01Z9github.com/volcengine/volc-sdk-golang/models/vod/business\xa0\x01\x01\xd8\x01\x01\xc2\x02\x00\xca\x02\x18Volc\\Models\\Vod\\Business\xe2\x02\x1bVolc\\Models\\Vod\\GPBMetadatab\x06proto3'
+  ,
+  dependencies=[vod_dot_business_dot_vod__common__pb2.DESCRIPTOR,])
+
+_VODPLAYINFOMODELVERSION = _descriptor.EnumDescriptor(
+  name='VodPlayInfoModelVersion',
+  full_name='Volcengine.Models.Vod.Business.VodPlayInfoModelVersion',
+  filename=None,
+  file=DESCRIPTOR,
+  create_key=_descriptor._internal_create_key,
+  values=[
+    _descriptor.EnumValueDescriptor(
+      name='UndefinedVodPlayInfoModelVersion', index=0, number=0,
+      serialized_options=None,
+      type=None,
+      create_key=_descriptor._internal_create_key),
+    _descriptor.EnumValueDescriptor(
+      name='InternalV1VodPlayInfoModelVersion', index=1, number=1,
+      serialized_options=None,
+      type=None,
+      create_key=_descriptor._internal_create_key),
+    _descriptor.EnumValueDescriptor(
+      name='InternalV2VodPlayInfoModelVersion', index=2, number=2,
+      serialized_options=None,
+      type=None,
+      create_key=_descriptor._internal_create_key),
+    _descriptor.EnumValueDescriptor(
+      name='InternalV3VodPlayInfoModelVersion', index=3, number=3,
+      serialized_options=None,
+      type=None,
+      create_key=_descriptor._internal_create_key),
+    _descriptor.EnumValueDescriptor(
+      name='ToBV1VodPlayInfoModelVersion', index=4, number=4,
+      serialized_options=None,
+      type=None,
+      create_key=_descriptor._internal_create_key),
+  ],
+  containing_type=None,
+  serialized_options=None,
+  serialized_start=744,
+  serialized_end=958,
 )
+_sym_db.RegisterEnumDescriptor(_VODPLAYINFOMODELVERSION)
 
+VodPlayInfoModelVersion = enum_type_wrapper.EnumTypeWrapper(_VODPLAYINFOMODELVERSION)
+UndefinedVodPlayInfoModelVersion = 0
+InternalV1VodPlayInfoModelVersion = 1
+InternalV2VodPlayInfoModelVersion = 2
+InternalV3VodPlayInfoModelVersion = 3
+ToBV1VodPlayInfoModelVersion = 4
 
 
 
-_INPUTPATH = _descriptor.Descriptor(
-  name='InputPath',
-  full_name='Volcengine.Imp.Models.Business.InputPath',
+_VODPLAYINFOMODEL = _descriptor.Descriptor(
+  name='VodPlayInfoModel',
+  full_name='Volcengine.Models.Vod.Business.VodPlayInfoModel',
   filename=None,
   file=DESCRIPTOR,
   containing_type=None,
   create_key=_descriptor._internal_create_key,
   fields=[
     _descriptor.FieldDescriptor(
-      name='Type', full_name='Volcengine.Imp.Models.Business.InputPath.Type', index=0,
-      number=1, type=9, cpp_type=9, label=1,
-      has_default_value=False, default_value=b"".decode('utf-8'),
-      message_type=None, enum_type=None, containing_type=None,
-      is_extension=False, extension_scope=None,
-      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
-    _descriptor.FieldDescriptor(
-      name='TosBucket', full_name='Volcengine.Imp.Models.Business.InputPath.TosBucket', index=1,
-      number=2, type=9, cpp_type=9, label=1,
-      has_default_value=False, default_value=b"".decode('utf-8'),
+      name='Version', full_name='Volcengine.Models.Vod.Business.VodPlayInfoModel.Version', index=0,
+      number=10, type=14, cpp_type=8, label=1,
+      has_default_value=False, default_value=0,
       message_type=None, enum_type=None, containing_type=None,
       is_extension=False, extension_scope=None,
       serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
     _descriptor.FieldDescriptor(
-      name='VodSpaceName', full_name='Volcengine.Imp.Models.Business.InputPath.VodSpaceName', index=2,
-      number=3, type=9, cpp_type=9, label=1,
-      has_default_value=False, default_value=b"".decode('utf-8'),
-      message_type=None, enum_type=None, containing_type=None,
-      is_extension=False, extension_scope=None,
-      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
-    _descriptor.FieldDescriptor(
-      name='FileId', full_name='Volcengine.Imp.Models.Business.InputPath.FileId', index=3,
-      number=4, type=9, cpp_type=9, label=1,
-      has_default_value=False, default_value=b"".decode('utf-8'),
-      message_type=None, enum_type=None, containing_type=None,
-      is_extension=False, extension_scope=None,
-      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
-  ],
-  extensions=[
-  ],
-  nested_types=[],
-  enum_types=[
-  ],
-  serialized_options=None,
-  is_extendable=False,
-  syntax='proto3',
-  extension_ranges=[],
-  oneofs=[
-  ],
-  serialized_start=65,
-  serialized_end=147,
-)
-
-
-_JOBOUTPUT = _descriptor.Descriptor(
-  name='JobOutput',
-  full_name='Volcengine.Imp.Models.Business.JobOutput',
-  filename=None,
-  file=DESCRIPTOR,
-  containing_type=None,
-  create_key=_descriptor._internal_create_key,
-  fields=[
-    _descriptor.FieldDescriptor(
-      name='TemplateId', full_name='Volcengine.Imp.Models.Business.JobOutput.TemplateId', index=0,
+      name='Vid', full_name='Volcengine.Models.Vod.Business.VodPlayInfoModel.Vid', index=1,
       number=1, type=9, cpp_type=9, label=1,
       has_default_value=False, default_value=b"".decode('utf-8'),
       message_type=None, enum_type=None, containing_type=None,
       is_extension=False, extension_scope=None,
       serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
     _descriptor.FieldDescriptor(
-      name='Properties', full_name='Volcengine.Imp.Models.Business.JobOutput.Properties', index=1,
-      number=2, type=9, cpp_type=9, label=1,
-      has_default_value=False, default_value=b"".decode('utf-8'),
+      name='Status', full_name='Volcengine.Models.Vod.Business.VodPlayInfoModel.Status', index=2,
+      number=2, type=5, cpp_type=1, label=1,
+      has_default_value=False, default_value=0,
       message_type=None, enum_type=None, containing_type=None,
       is_extension=False, extension_scope=None,
       serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
     _descriptor.FieldDescriptor(
-      name='Code', full_name='Volcengine.Imp.Models.Business.JobOutput.Code', index=2,
+      name='PosterUrl', full_name='Volcengine.Models.Vod.Business.VodPlayInfoModel.PosterUrl', index=3,
       number=3, type=9, cpp_type=9, label=1,
       has_default_value=False, default_value=b"".decode('utf-8'),
       message_type=None, enum_type=None, containing_type=None,
       is_extension=False, extension_scope=None,
       serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
     _descriptor.FieldDescriptor(
-      name='FileMessageId', full_name='Volcengine.Imp.Models.Business.JobOutput.FileMessageId', index=3,
-      number=4, type=9, cpp_type=9, label=1,
-      has_default_value=False, default_value=b"".decode('utf-8'),
+      name='Duration', full_name='Volcengine.Models.Vod.Business.VodPlayInfoModel.Duration', index=4,
+      number=4, type=2, cpp_type=6, label=1,
+      has_default_value=False, default_value=float(0),
       message_type=None, enum_type=None, containing_type=None,
       is_extension=False, extension_scope=None,
       serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
     _descriptor.FieldDescriptor(
-      name='TaskType', full_name='Volcengine.Imp.Models.Business.JobOutput.TaskType', index=4,
+      name='FileType', full_name='Volcengine.Models.Vod.Business.VodPlayInfoModel.FileType', index=5,
       number=5, type=9, cpp_type=9, label=1,
       has_default_value=False, default_value=b"".decode('utf-8'),
       message_type=None, enum_type=None, containing_type=None,
       is_extension=False, extension_scope=None,
       serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
     _descriptor.FieldDescriptor(
-      name='Status', full_name='Volcengine.Imp.Models.Business.JobOutput.Status', index=5,
-      number=6, type=9, cpp_type=9, label=1,
-      has_default_value=False, default_value=b"".decode('utf-8'),
+      name='EnableAdaptive', full_name='Volcengine.Models.Vod.Business.VodPlayInfoModel.EnableAdaptive', index=6,
+      number=6, type=8, cpp_type=7, label=1,
+      has_default_value=False, default_value=False,
       message_type=None, enum_type=None, containing_type=None,
       is_extension=False, extension_scope=None,
       serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
     _descriptor.FieldDescriptor(
-      name='ActivityId', full_name='Volcengine.Imp.Models.Business.JobOutput.ActivityId', index=6,
-      number=7, type=9, cpp_type=9, label=1,
-      has_default_value=False, default_value=b"".decode('utf-8'),
+      name='TotalCount', full_name='Volcengine.Models.Vod.Business.VodPlayInfoModel.TotalCount', index=7,
+      number=7, type=5, cpp_type=1, label=1,
+      has_default_value=False, default_value=0,
       message_type=None, enum_type=None, containing_type=None,
       is_extension=False, extension_scope=None,
       serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
     _descriptor.FieldDescriptor(
-      name='StartTime', full_name='Volcengine.Imp.Models.Business.JobOutput.StartTime', index=7,
-      number=8, type=9, cpp_type=9, label=1,
-      has_default_value=False, default_value=b"".decode('utf-8'),
+      name='AdaptiveInfo', full_name='Volcengine.Models.Vod.Business.VodPlayInfoModel.AdaptiveInfo', index=8,
+      number=8, type=11, cpp_type=10, label=1,
+      has_default_value=False, default_value=None,
       message_type=None, enum_type=None, containing_type=None,
       is_extension=False, extension_scope=None,
       serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
     _descriptor.FieldDescriptor(
-      name='EndTime', full_name='Volcengine.Imp.Models.Business.JobOutput.EndTime', index=8,
-      number=9, type=9, cpp_type=9, label=1,
-      has_default_value=False, default_value=b"".decode('utf-8'),
+      name='PlayInfoList', full_name='Volcengine.Models.Vod.Business.VodPlayInfoModel.PlayInfoList', index=9,
+      number=9, type=11, cpp_type=10, label=3,
+      has_default_value=False, default_value=[],
       message_type=None, enum_type=None, containing_type=None,
       is_extension=False, extension_scope=None,
       serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
     _descriptor.FieldDescriptor(
-      name='TemplateName', full_name='Volcengine.Imp.Models.Business.JobOutput.TemplateName', index=9,
-      number=10, type=9, cpp_type=9, label=1,
-      has_default_value=False, default_value=b"".decode('utf-8'),
+      name='ThumbInfoList', full_name='Volcengine.Models.Vod.Business.VodPlayInfoModel.ThumbInfoList', index=10,
+      number=11, type=11, cpp_type=10, label=3,
+      has_default_value=False, default_value=[],
       message_type=None, enum_type=None, containing_type=None,
       is_extension=False, extension_scope=None,
       serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
   ],
   extensions=[
   ],
   nested_types=[],
@@ -164,116 +167,139 @@
   ],
   serialized_options=None,
   is_extendable=False,
   syntax='proto3',
   extension_ranges=[],
   oneofs=[
   ],
-  serialized_start=150,
-  serialized_end=350,
+  serialized_start=95,
+  serialized_end=522,
 )
 
 
-_JOBEXECUTION = _descriptor.Descriptor(
-  name='JobExecution',
-  full_name='Volcengine.Imp.Models.Business.JobExecution',
+_VODGETORIGINALPLAYINFORESULT = _descriptor.Descriptor(
+  name='VodGetOriginalPlayInfoResult',
+  full_name='Volcengine.Models.Vod.Business.VodGetOriginalPlayInfoResult',
   filename=None,
   file=DESCRIPTOR,
   containing_type=None,
   create_key=_descriptor._internal_create_key,
   fields=[
     _descriptor.FieldDescriptor(
-      name='JobId', full_name='Volcengine.Imp.Models.Business.JobExecution.JobId', index=0,
+      name='FileType', full_name='Volcengine.Models.Vod.Business.VodGetOriginalPlayInfoResult.FileType', index=0,
       number=1, type=9, cpp_type=9, label=1,
       has_default_value=False, default_value=b"".decode('utf-8'),
       message_type=None, enum_type=None, containing_type=None,
       is_extension=False, extension_scope=None,
       serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
     _descriptor.FieldDescriptor(
-      name='InputPath', full_name='Volcengine.Imp.Models.Business.JobExecution.InputPath', index=1,
-      number=2, type=11, cpp_type=10, label=1,
-      has_default_value=False, default_value=None,
+      name='Duration', full_name='Volcengine.Models.Vod.Business.VodGetOriginalPlayInfoResult.Duration', index=1,
+      number=2, type=2, cpp_type=6, label=1,
+      has_default_value=False, default_value=float(0),
       message_type=None, enum_type=None, containing_type=None,
       is_extension=False, extension_scope=None,
       serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
     _descriptor.FieldDescriptor(
-      name='Output', full_name='Volcengine.Imp.Models.Business.JobExecution.Output', index=2,
-      number=3, type=11, cpp_type=10, label=3,
-      has_default_value=False, default_value=[],
+      name='Size', full_name='Volcengine.Models.Vod.Business.VodGetOriginalPlayInfoResult.Size', index=2,
+      number=3, type=1, cpp_type=5, label=1,
+      has_default_value=False, default_value=float(0),
       message_type=None, enum_type=None, containing_type=None,
       is_extension=False, extension_scope=None,
       serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
     _descriptor.FieldDescriptor(
-      name='Status', full_name='Volcengine.Imp.Models.Business.JobExecution.Status', index=3,
-      number=4, type=9, cpp_type=9, label=1,
-      has_default_value=False, default_value=b"".decode('utf-8'),
+      name='Height', full_name='Volcengine.Models.Vod.Business.VodGetOriginalPlayInfoResult.Height', index=3,
+      number=4, type=5, cpp_type=1, label=1,
+      has_default_value=False, default_value=0,
       message_type=None, enum_type=None, containing_type=None,
       is_extension=False, extension_scope=None,
       serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
     _descriptor.FieldDescriptor(
-      name='CreateAt', full_name='Volcengine.Imp.Models.Business.JobExecution.CreateAt', index=4,
-      number=5, type=9, cpp_type=9, label=1,
-      has_default_value=False, default_value=b"".decode('utf-8'),
+      name='Width', full_name='Volcengine.Models.Vod.Business.VodGetOriginalPlayInfoResult.Width', index=4,
+      number=5, type=5, cpp_type=1, label=1,
+      has_default_value=False, default_value=0,
       message_type=None, enum_type=None, containing_type=None,
       is_extension=False, extension_scope=None,
       serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
     _descriptor.FieldDescriptor(
-      name='FinishedAt', full_name='Volcengine.Imp.Models.Business.JobExecution.FinishedAt', index=5,
+      name='Format', full_name='Volcengine.Models.Vod.Business.VodGetOriginalPlayInfoResult.Format', index=5,
       number=6, type=9, cpp_type=9, label=1,
       has_default_value=False, default_value=b"".decode('utf-8'),
       message_type=None, enum_type=None, containing_type=None,
       is_extension=False, extension_scope=None,
       serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
     _descriptor.FieldDescriptor(
-      name='TemplateId', full_name='Volcengine.Imp.Models.Business.JobExecution.TemplateId', index=6,
+      name='Codec', full_name='Volcengine.Models.Vod.Business.VodGetOriginalPlayInfoResult.Codec', index=6,
       number=7, type=9, cpp_type=9, label=1,
       has_default_value=False, default_value=b"".decode('utf-8'),
       message_type=None, enum_type=None, containing_type=None,
       is_extension=False, extension_scope=None,
       serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
+    _descriptor.FieldDescriptor(
+      name='Bitrate', full_name='Volcengine.Models.Vod.Business.VodGetOriginalPlayInfoResult.Bitrate', index=7,
+      number=8, type=5, cpp_type=1, label=1,
+      has_default_value=False, default_value=0,
+      message_type=None, enum_type=None, containing_type=None,
+      is_extension=False, extension_scope=None,
+      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
+    _descriptor.FieldDescriptor(
+      name='Md5', full_name='Volcengine.Models.Vod.Business.VodGetOriginalPlayInfoResult.Md5', index=8,
+      number=9, type=9, cpp_type=9, label=1,
+      has_default_value=False, default_value=b"".decode('utf-8'),
+      message_type=None, enum_type=None, containing_type=None,
+      is_extension=False, extension_scope=None,
+      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
+    _descriptor.FieldDescriptor(
+      name='MainPlayUrl', full_name='Volcengine.Models.Vod.Business.VodGetOriginalPlayInfoResult.MainPlayUrl', index=9,
+      number=10, type=9, cpp_type=9, label=1,
+      has_default_value=False, default_value=b"".decode('utf-8'),
+      message_type=None, enum_type=None, containing_type=None,
+      is_extension=False, extension_scope=None,
+      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
+    _descriptor.FieldDescriptor(
+      name='BackupPlayUrl', full_name='Volcengine.Models.Vod.Business.VodGetOriginalPlayInfoResult.BackupPlayUrl', index=10,
+      number=11, type=9, cpp_type=9, label=1,
+      has_default_value=False, default_value=b"".decode('utf-8'),
+      message_type=None, enum_type=None, containing_type=None,
+      is_extension=False, extension_scope=None,
+      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
   ],
   extensions=[
   ],
   nested_types=[],
   enum_types=[
   ],
   serialized_options=None,
   is_extendable=False,
   syntax='proto3',
   extension_ranges=[],
   oneofs=[
   ],
-  serialized_start=353,
-  serialized_end=577,
+  serialized_start=525,
+  serialized_end=741,
 )
 
-_JOBEXECUTION.fields_by_name['InputPath'].message_type = _INPUTPATH
-_JOBEXECUTION.fields_by_name['Output'].message_type = _JOBOUTPUT
-DESCRIPTOR.message_types_by_name['InputPath'] = _INPUTPATH
-DESCRIPTOR.message_types_by_name['JobOutput'] = _JOBOUTPUT
-DESCRIPTOR.message_types_by_name['JobExecution'] = _JOBEXECUTION
+_VODPLAYINFOMODEL.fields_by_name['Version'].enum_type = _VODPLAYINFOMODELVERSION
+_VODPLAYINFOMODEL.fields_by_name['AdaptiveInfo'].message_type = vod_dot_business_dot_vod__common__pb2._VODADAPTIVEINFO
+_VODPLAYINFOMODEL.fields_by_name['PlayInfoList'].message_type = vod_dot_business_dot_vod__common__pb2._VODPLAYINFO
+_VODPLAYINFOMODEL.fields_by_name['ThumbInfoList'].message_type = vod_dot_business_dot_vod__common__pb2._VODTHUMBINFO
+DESCRIPTOR.message_types_by_name['VodPlayInfoModel'] = _VODPLAYINFOMODEL
+DESCRIPTOR.message_types_by_name['VodGetOriginalPlayInfoResult'] = _VODGETORIGINALPLAYINFORESULT
+DESCRIPTOR.enum_types_by_name['VodPlayInfoModelVersion'] = _VODPLAYINFOMODELVERSION
 _sym_db.RegisterFileDescriptor(DESCRIPTOR)
 
-InputPath = _reflection.GeneratedProtocolMessageType('InputPath', (_message.Message,), {
-  'DESCRIPTOR' : _INPUTPATH,
-  '__module__' : 'imp.business.imp_common_pb2'
-  # @@protoc_insertion_point(class_scope:Volcengine.Imp.Models.Business.InputPath)
-  })
-_sym_db.RegisterMessage(InputPath)
-
-JobOutput = _reflection.GeneratedProtocolMessageType('JobOutput', (_message.Message,), {
-  'DESCRIPTOR' : _JOBOUTPUT,
-  '__module__' : 'imp.business.imp_common_pb2'
-  # @@protoc_insertion_point(class_scope:Volcengine.Imp.Models.Business.JobOutput)
+VodPlayInfoModel = _reflection.GeneratedProtocolMessageType('VodPlayInfoModel', (_message.Message,), {
+  'DESCRIPTOR' : _VODPLAYINFOMODEL,
+  '__module__' : 'vod.business.vod_play_pb2'
+  # @@protoc_insertion_point(class_scope:Volcengine.Models.Vod.Business.VodPlayInfoModel)
   })
-_sym_db.RegisterMessage(JobOutput)
+_sym_db.RegisterMessage(VodPlayInfoModel)
 
-JobExecution = _reflection.GeneratedProtocolMessageType('JobExecution', (_message.Message,), {
-  'DESCRIPTOR' : _JOBEXECUTION,
-  '__module__' : 'imp.business.imp_common_pb2'
-  # @@protoc_insertion_point(class_scope:Volcengine.Imp.Models.Business.JobExecution)
+VodGetOriginalPlayInfoResult = _reflection.GeneratedProtocolMessageType('VodGetOriginalPlayInfoResult', (_message.Message,), {
+  'DESCRIPTOR' : _VODGETORIGINALPLAYINFORESULT,
+  '__module__' : 'vod.business.vod_play_pb2'
+  # @@protoc_insertion_point(class_scope:Volcengine.Models.Vod.Business.VodGetOriginalPlayInfoResult)
   })
-_sym_db.RegisterMessage(JobExecution)
+_sym_db.RegisterMessage(VodGetOriginalPlayInfoResult)
 
 
 DESCRIPTOR._options = None
 # @@protoc_insertion_point(module_scope)
```

### Comparing `volcengine-1.0.84/volcengine/auth/MetaData.py` & `volcengine-1.0.9/volcengine/auth/MetaData.py`

 * *Files identical despite different names*

### Comparing `volcengine-1.0.84/volcengine/auth/SignerV4.py` & `volcengine-1.0.9/volcengine/auth/SignerV4.py`

 * *Files 25% similar despite different names*

```diff
@@ -7,29 +7,25 @@
 try:
     from urllib import urlencode
 except:
     from urllib.parse import urlencode
 
 from volcengine.auth.MetaData import MetaData
 from volcengine.util.Util import Util
-from volcengine.base.Request import Request
-from volcengine.auth.SignResult import SignResult
 
 class SignerV4(object):
     @staticmethod
     def sign(request, credentials):
         if request.path == '':
             request.path = '/'
         if request.method != 'GET' and not ('Content-Type' in request.headers):
             request.headers['Content-Type'] = 'application/x-www-form-urlencoded; charset=utf-8'
 
         format_date = SignerV4.get_current_format_date()
         request.headers['X-Date'] = format_date
-        if credentials.session_token != '':
-            request.headers['X-Security-Token'] = credentials.session_token
 
         md = MetaData()
         md.set_algorithm('HMAC-SHA256')
         md.set_service(credentials.service)
         md.set_region(credentials.region)
         md.set_date(format_date[:8])
 
@@ -59,106 +55,41 @@
         query['X-Date'] = format_date
         query['X-NotSignBody'] = ''
         query['X-Credential'] = credentials.ak + '/' + md.credential_scope
         query['X-Algorithm'] = md.algorithm
         query['X-SignedHeaders'] = md.signed_headers
         query['X-SignedQueries'] = ''
         query['X-SignedQueries'] = ';'.join(sorted(query.keys()))
-        if credentials.session_token != '':
-            query['X-Security-Token'] = credentials.session_token
 
         hashed_canon_req = SignerV4.hashed_simple_canonical_request_v4(request, md)
         signing_str = '\n'.join([md.algorithm, format_date, md.credential_scope, hashed_canon_req])
         signing_key = SignerV4.get_signing_secret_key_v4(credentials.sk, md.date, md.region, md.service)
         sign = SignerV4.signature_v4(signing_key, signing_str)
 
         query['X-Signature'] = sign
         return urlencode(query)
 
     @staticmethod
-    def sign_only(param, credentials):
-        request = Request()
-        request.host = param.host
-        request.method = param.method
-        request.path = param.path
-        request.body = param.body
-        request.query = param.query
-        request.headers = param.header_list
-
-        format_date = param.date.strftime("%Y%m%dT%H%M%SZ")
-        date = format_date[:8]
-        request.headers['X-Date'] = format_date
-        md = MetaData()
-        md.set_algorithm('HMAC-SHA256')
-        md.set_service(credentials.service)
-        md.set_region(credentials.region)
-        md.set_date(date)
-        md.set_credential_scope('/'.join([md.date, md.region, md.service, 'request']))
-
-        if param.is_sign_url:
-            md.set_signed_headers('')
-            md.set_credential_scope('/'.join([md.date, md.region, md.service, 'request']))
-            query = request.query
-            query['X-Date'] = format_date
-            query['X-NotSignBody'] = ''
-            query['X-Credential'] = credentials.ak + '/' + md.credential_scope
-            query['X-Algorithm'] = md.algorithm
-            query['X-SignedHeaders'] = md.signed_headers
-            query['X-SignedQueries'] = ''
-            query['X-SignedQueries'] = ';'.join(sorted(query.keys()))
-            if credentials.session_token != '':
-                query['X-Security-Token'] = credentials.session_token
-            hashed_canon_req = SignerV4.hashed_simple_canonical_request_v4(request, md)
-        else:
-            if credentials.session_token != '':
-                request.headers['X-Security-Token'] = credentials.session_token
-            hashed_canon_req = SignerV4.hashed_canonical_request_v4(request, md)
-
-        signing_str = '\n'.join([md.algorithm, format_date, md.credential_scope, hashed_canon_req])
-        signing_key = SignerV4.get_signing_secret_key_v4(credentials.sk, md.date, md.region, md.service)
-        sign = SignerV4.signature_v4(signing_key, signing_str)
-
-        result = SignResult()
-        result.xdate = format_date
-        result.xAlgorithm = md.algorithm
-        if param.is_sign_url:
-            result.xSignedQueries = request.query['X-SignedQueries']
-        result.xSignedHeaders = md.signed_headers
-        result.xCredential = credentials.ak + '/' + md.credential_scope
-        result.xSignature = sign
-        result.xContextSha256 = request.headers['X-Content-Sha256']
-        result.authorization = result.xAlgorithm + " Credential=" + result.xCredential + ", SignedHeaders=" + md.signed_headers + ", Signature=" + result.xSignature
-        result.xSecurityToken = credentials.session_token
-
-        return result
-
-    @staticmethod
     def hashed_simple_canonical_request_v4(request, meta):
         body = bytes()
-        # if sys.version_info[0] == 3:
-        #     body_hash = Util.sha256(body.decode('utf-8'))
-        # else:
-        body_hash = Util.sha256(body)
+        if sys.version_info[0] == 3:
+            body_hash = Util.sha256(body.decode('utf-8'))
+        else:
+            body_hash = Util.sha256(body)
 
         if request.path == '':
             request.path = '/'
 
         canoncial_request = '\n'.join(
             [request.method, Util.norm_uri(request.path), Util.norm_query(request.query), '\n',
              meta.signed_headers, body_hash])
-        # if sys.version_info[0] == 3:
-        #     return Util.sha256(canoncial_request.decode('utf-8'))
-        # else:
         return Util.sha256(canoncial_request)
 
     @staticmethod
     def hashed_canonical_request_v4(request, meta):
-        # if sys.version_info[0] == 3:
-        #     body_hash = Util.sha256(request.body.decode('utf-8'))
-        # else:
         body_hash = Util.sha256(request.body)
         request.headers['X-Content-Sha256'] = body_hash
 
         signed_headers = dict()
         for key in request.headers:
             if key in ['Content-Type', 'Content-Md5', 'Host'] or key.startswith('X-'):
                 signed_headers[key.lower()] = request.headers[key]
@@ -188,15 +119,15 @@
         return Util.to_hex(Util.hmac_sha256(signing_key, signing_str))
 
     @staticmethod
     def get_signing_secret_key_v4(sk, date, region, service):
         if sys.version_info[0] == 3:
             kdate = Util.hmac_sha256(bytes(sk, encoding='utf-8'), date)
         else:
-            kdate = Util.hmac_sha256(sk.encode('utf-8'), date)
+            kdate = Util.hmac_sha256(sk, date)
         kregion = Util.hmac_sha256(kdate, region)
         kservice = Util.hmac_sha256(kregion, service)
         return Util.hmac_sha256(kservice, 'request')
 
     @staticmethod
     def build_auth_header_v4(signature, meta, credentials):
         credential = credentials.ak + '/' + meta.credential_scope
```

### Comparing `volcengine-1.0.84/volcengine/Policy.py` & `volcengine-1.0.9/volcengine/Policy.py`

 * *Files identical despite different names*

### Comparing `volcengine-1.0.84/volcengine/example/rtc/RtcService.py` & `volcengine-1.0.9/volcengine/sms/SmsService.py`

 * *Files 18% similar despite different names*

```diff
@@ -4,57 +4,42 @@
 
 from volcengine.ApiInfo import ApiInfo
 from volcengine.Credentials import Credentials
 from volcengine.base.Service import Service
 from volcengine.ServiceInfo import ServiceInfo
 
 
-class RtcService(Service):
+class SmsService(Service):
     _instance_lock = threading.Lock()
 
     def __new__(cls, *args, **kwargs):
-        if not hasattr(RtcService, "_instance"):
-            with RtcService._instance_lock:
-                if not hasattr(RtcService, "_instance"):
-                    RtcService._instance = object.__new__(cls)
-        return RtcService._instance
+        if not hasattr(SmsService, "_instance"):
+            with SmsService._instance_lock:
+                if not hasattr(SmsService, "_instance"):
+                    SmsService._instance = object.__new__(cls)
+        return SmsService._instance
 
     def __init__(self):
-        self.service_info = RtcService.get_service_info()
-        self.api_info = RtcService.get_api_info()
-        super(RtcService, self).__init__(self.service_info, self.api_info)
+        self.service_info = SmsService.get_service_info()
+        self.api_info = SmsService.get_api_info()
+        super(SmsService, self).__init__(self.service_info, self.api_info)
 
     @staticmethod
     def get_service_info():
-        service_info = ServiceInfo("rtc.volcengineapi.com", {'Accept': 'application/json'},
-                                   Credentials('', '', 'rtc', 'cn-north-1'), 5, 5)
+        service_info = ServiceInfo("open.volcengineapi.com", {'Accept': 'application/json'},
+                                   Credentials('', '', 'volcSMS', 'cn-north-1'), 5, 5)
         return service_info
 
     @staticmethod
     def get_api_info():
         api_info = {
-            "StartRecord": ApiInfo("POST", "/", {"Action": "StartRecord", "Version": "2022-06-01"}, {}, {}),
-            "StopRecord": ApiInfo("POST", "/", {"Action": "StopRecord", "Version": "2022-06-01"}, {}, {}),
-            "GetRecordTask": ApiInfo("GET", "/", {"Action": "GetRecordTask", "Version": "2022-06-01"}, {}, {}),
+            "SendSms": ApiInfo("POST", "/", {"Action": "SendSms", "Version": "2020-01-01"}, {}, {}),
         }
         return api_info
 
-    def start_record(self, body):
-        res = self.json("StartRecord", {}, body)
+    def send_sms(self, body):
+        res = self.json('SendSms', {}, body)
         if res == '':
-            raise Exception("StartRecord: empty response")
+            raise Exception("empty response")
         res_json = json.loads(res)
-        return res_json
 
-    def stop_record(self, body):
-        res = self.json("StopRecord", {}, body)
-        if res == '':
-            raise Exception("StopRecord: empty response")
-        res_json = json.loads(res)
-        return res_json
-
-    def get_record_task(self, params):
-        res = self.get("GetRecordTask", params)
-        if res == '':
-            raise Exception("GetRecordTask: empty response")
-        res_json = json.loads(res)
         return res_json
```

### Comparing `volcengine-1.0.84/volcengine/example/vedit/example_edit.py` & `volcengine-1.0.9/volcengine/example/vedit/example_edit.py`

 * *Files identical despite different names*

### Comparing `volcengine-1.0.84/volcengine/example/vod/cdn/CreateCdnRefreshTaskExample.py` & `volcengine-1.0.9/volcengine/example/vod/upload/UploadUrl.py`

 * *Files 24% similar despite different names*

```diff
@@ -1,21 +1,33 @@
 # coding:utf-8
 from __future__ import print_function
 
+from volcengine.models.vod.request.request_vod_pb2 import VodUrlUploadRequest
 from volcengine.vod.VodService import VodService
-from volcengine.vod.models.request.request_vod_pb2 import VodCreateCdnRefreshTaskRequest
 
 if __name__ == '__main__':
     vod_service = VodService()
+
     # call below method if you dont set ak and sk in $HOME/.vcloud/config
     vod_service.set_ak('your ak')
     vod_service.set_sk('your sk')
+
+    space_name = 'your space'
+    url = 'url'
+
     try:
-        req = VodCreateCdnRefreshTaskRequest()
-        req.SpaceName = 'your space name'
-        resp = vod_service.create_cdn_refresh_task(req)
+        req = VodUrlUploadRequest()
+        req.SpaceName = space_name
+        url_set = req.URLSets.add()
+        url_set.SourceUrl = url
+        resp = vod_service.upload_media_by_url(req)
     except Exception:
         raise
     else:
         print(resp)
-        if resp.ResponseMetadata.Error.Code != '':
+        if resp.ResponseMetadata.Error.Code == '':
+            print(resp.Result.Data)
+            print(resp.Result.Data[0].JobId)
+            print(resp.Result.Data[0].SourceUrl)
+        else:
             print(resp.ResponseMetadata.Error)
+            print(resp.ResponseMetadata.RequestId)
```

### Comparing `volcengine-1.0.84/volcengine/example/vod/cdn/DescribeCdnIpExample.py` & `volcengine-1.0.9/volcengine/example/vod/play/GetPlayInfoExample.py`

 * *Files 17% similar despite different names*

```diff
@@ -1,21 +1,26 @@
 # coding:utf-8
 from __future__ import print_function
 
+from volcengine.models.vod.request.request_vod_pb2 import *
 from volcengine.vod.VodService import VodService
-from volcengine.vod.models.request.request_vod_pb2 import VodDescribeIPInfoRequest
 
 if __name__ == '__main__':
     vod_service = VodService()
     # call below method if you dont set ak and sk in $HOME/.vcloud/config
-    vod_service.set_ak('your ak')
-    vod_service.set_sk('your sk')
+    # vod_service.set_ak('ak')
+    # vod_service.set_sk('sk')
     try:
-        req = VodDescribeIPInfoRequest()
-        req.Ips = "1.1.1.1"
-        resp = vod_service.describe_ip_info(req)
+        vid = 'your vid'
+        req = VodGetPlayInfoRequest()
+        req.Vid = vid
+        req.Ssl = '1'
+        resp = vod_service.get_play_info(req)
     except Exception:
         raise
     else:
         print(resp)
-        if resp.ResponseMetadata.Error.Code != '':
+        if resp.ResponseMetadata.Error.Code == '':
+            print(resp.Result.PlayInfoList[0].MainPlayUrl)
+        else:
             print(resp.ResponseMetadata.Error)
+    print('*' * 100)
```

### Comparing `volcengine-1.0.84/volcengine/example/vod/cdn/ListCdnPvDataExample.py` & `volcengine-1.0.9/volcengine/example/vod/play/GetPlayAuthTokenExample.py`

 * *Files 18% similar despite different names*

```diff
@@ -1,23 +1,22 @@
 # coding:utf-8
 from __future__ import print_function
 
+from volcengine.models.vod.request.request_vod_pb2 import *
 from volcengine.vod.VodService import VodService
-from volcengine.vod.models.request.request_vod_pb2 import VodListCdnPvDataRequest
 
 if __name__ == '__main__':
+
     vod_service = VodService()
     # call below method if you dont set ak and sk in $HOME/.vcloud/config
-    vod_service.set_ak('your ak')
-    vod_service.set_sk('your sk')
+    # vod_service.set_ak('ak')
+    # vod_service.set_sk('sk')
     try:
-        req = VodListCdnPvDataRequest()
-        req.Domains = 'your domian'
-        req.StartTimestamp = 0
-        req.EndTimestamp = 0
-        resp = vod_service.list_cdn_pv_data(req)
+        vid = 'your vid'
+        req = VodGetPlayInfoRequest()
+        req.Vid = vid
+        resp = vod_service.get_play_auth_token(req)
     except Exception:
         raise
     else:
         print(resp)
-        if resp.ResponseMetadata.Error.Code != '':
-            print(resp.ResponseMetadata.Error)
+    print('*' * 100)
```

### Comparing `volcengine-1.0.84/volcengine/example/vod/cdn/DescribeVodDomainTrafficDataExample.py` & `volcengine-1.0.9/volcengine/example/vod/upload/QueryUploadTaskInfo.py`

 * *Files 22% similar despite different names*

```diff
@@ -1,26 +1,33 @@
 # coding:utf-8
 from __future__ import print_function
 
+from volcengine.models.vod.request.request_vod_pb2 import VodQueryUploadTaskInfoRequest
 from volcengine.vod.VodService import VodService
-from volcengine.vod.models.request.request_vod_pb2 import VodDescribeVodDomainTrafficDataRequest
 
 if __name__ == '__main__':
     vod_service = VodService()
+
     # call below method if you dont set ak and sk in $HOME/.vcloud/config
     vod_service.set_ak('your ak')
     vod_service.set_sk('your sk')
-    try:
-        req = VodDescribeVodDomainTrafficDataRequest()
 
-        req.DomainList = ""
-        req.StartTime = ""
-        req.EndTime = ""
-        req.Aggregation = 0
-        req.TrafficType = ""
-        resp = vod_service.describe_vod_domain_traffic_data(req)
+    jobId = 'url jobId'
+
+    jobIds = [jobId]
+    comma = ','
+    s = comma.join(jobIds)
+
+    req = VodQueryUploadTaskInfoRequest()
+    req.JobIds = s
+    try:
+        resp = vod_service.query_upload_task_info(req)
     except Exception:
         raise
     else:
         print(resp)
-        if resp.ResponseMetadata.Error.Code != '':
+        if resp.ResponseMetadata.Error.Code == '':
+            print(resp.Result.Data)
+            print(resp.Result.Data.MediaInfoList[0].State)
+        else:
             print(resp.ResponseMetadata.Error)
+            print(resp.ResponseMetadata.RequestId)
```

### Comparing `volcengine-1.0.84/volcengine/example/vod/cdn/ListCdnUsageDataExample.py` & `volcengine-1.0.9/volcengine/example/vod/workflow/WorkflowExample.py`

 * *Files 24% similar despite different names*

```diff
@@ -1,23 +1,29 @@
 # coding:utf-8
 from __future__ import print_function
 
+from volcengine.models.vod.request.request_vod_pb2 import *
+from volcengine.models.vod.business.vod_workflow_pb2 import *
 from volcengine.vod.VodService import VodService
-from volcengine.vod.models.request.request_vod_pb2 import VodListCdnUsageDataRequest
 
 if __name__ == '__main__':
     vod_service = VodService()
     # call below method if you dont set ak and sk in $HOME/.vcloud/config
     vod_service.set_ak('your ak')
     vod_service.set_sk('your sk')
     try:
-        req = VodListCdnUsageDataRequest()
-        req.Domains = 'your domian'
-        req.StartTimestamp = 0
-        req.EndTimestamp = 0
-        resp = vod_service.list_cdn_usage_data(req)
+        req = VodStartWorkflowRequest()
+        req.Vid = 'your vid'
+        req.TemplateId = 'your template id'
+        req.Input.MergeFrom(WorkflowParams())
+        req.Priority = 0
+        req.CallbackArgs = 'your callback args'
+        resp = vod_service.start_workflow(req)
     except Exception:
         raise
     else:
         print(resp)
-        if resp.ResponseMetadata.Error.Code != '':
+        if resp.ResponseMetadata.Error.Code == '':
+            print(resp.Result)
+        else:
             print(resp.ResponseMetadata.Error)
+
```

### Comparing `volcengine-1.0.84/volcengine/example/vod/cdn/ListDomainExample.py` & `volcengine-1.0.9/volcengine/example/vod/upload/ApplyUploadInfoExample.py`

 * *Files 20% similar despite different names*

```diff
@@ -1,22 +1,34 @@
 # coding:utf-8
 from __future__ import print_function
 
+from volcengine.models.vod.request.request_vod_pb2 import VodApplyUploadInfoRequest
 from volcengine.vod.VodService import VodService
-from volcengine.vod.models.request.request_vod_pb2 import VodListDomainRequest
 
 if __name__ == '__main__':
     vod_service = VodService()
+
     # call below method if you dont set ak and sk in $HOME/.vcloud/config
     vod_service.set_ak('your ak')
     vod_service.set_sk('your sk')
+
+    space_name = 'your space'
+
     try:
-        req = VodListDomainRequest()
-        req.SpaceName = 'your space name'
-        resp = vod_service.list_domain(req)
+        req = VodApplyUploadInfoRequest()
+        req.SpaceName = space_name
+
+        resp = vod_service.apply_upload_info(req)
     except Exception:
         raise
     else:
         print(resp)
-        if resp.ResponseMetadata.Error.Code != '':
+        if resp.ResponseMetadata.Error.Code == '':
+            print(resp.Result.Data)
+            print(resp.Result.Data.UploadAddress.StoreInfos[0].StoreUri)
+            print(resp.Result.Data.UploadAddress.StoreInfos[0].Auth)
+            print(resp.Result.Data.UploadAddress.UploadHosts[0])
+            print(resp.Result.Data.UploadAddress.SessionKey)
+        else:
             print(resp.ResponseMetadata.Error)
-            
+            print(resp.ResponseMetadata.RequestId)
+
```

### Comparing `volcengine-1.0.84/volcengine/example/vod/space/CreateSpaceExample.py` & `volcengine-1.0.9/volcengine/example/vod/upload/UploadMedia.py`

 * *Files 26% similar despite different names*

```diff
@@ -1,22 +1,43 @@
 # coding:utf-8
 from __future__ import print_function
 
+import json
+
+from volcengine.models.vod.request.request_vod_pb2 import VodUploadMediaRequest
+from volcengine.util.Functions import Function
 from volcengine.vod.VodService import VodService
-from volcengine.vod.models.request.request_vod_pb2 import VodCreateSpaceRequest
 
 if __name__ == '__main__':
     vod_service = VodService()
+
     # call below method if you dont set ak and sk in $HOME/.vcloud/config
     vod_service.set_ak('your ak')
     vod_service.set_sk('your sk')
+
+    space_name = 'your space name'
+    file_path = 'your file path'
+
+    get_meta_function = Function.get_meta_func()
+    snapshot_function = Function.get_snapshot_func(2.3)
+
     try:
-        req = VodCreateSpaceRequest()
-        req.SpaceName = 'your space name'
-        req.ProjectName = 'your space name'
-        resp = vod_service.create_space(req)
+        req = VodUploadMediaRequest()
+        req.SpaceName = space_name
+        req.FilePath = file_path
+        req.Functions = json.dumps([get_meta_function, snapshot_function])
+        req.CallbackArgs = ''
+
+        resp = vod_service.upload_media(req)
     except Exception:
         raise
     else:
         print(resp)
-        if resp.ResponseMetadata.Error.Code != '':
+        if resp.ResponseMetadata.Error.Code == '':
+            print(resp.Result.Data)
+            print(resp.Result.Data.Vid)
+            print(resp.Result.Data.PosterUri)
+            print(resp.Result.Data.SourceInfo.Height)
+            print(resp.Result.Data.SourceInfo.Width)
+        else:
             print(resp.ResponseMetadata.Error)
+            print(resp.ResponseMetadata.RequestId)
```

### Comparing `volcengine-1.0.84/volcengine/example/vod/measure/DescribeVodSnapshotData.py` & `volcengine-1.0.9/volcengine/example/vod/upload/CommitUploadInfoExample.py`

 * *Files 26% similar despite different names*

```diff
@@ -1,28 +1,39 @@
 # coding:utf-8
 from __future__ import print_function
 
+import json
+
+from volcengine.models.vod.request.request_vod_pb2 import VodCommitUploadInfoRequest
+from volcengine.util.Functions import Function
 from volcengine.vod.VodService import VodService
-from volcengine.vod.models.request.request_vod_pb2 import DescribeVodSnapshotDataRequest
 
 if __name__ == '__main__':
     vod_service = VodService()
+
     # call below method if you dont set ak and sk in $HOME/.vcloud/config
     vod_service.set_ak('your ak')
     vod_service.set_sk('your sk')
+
+    space_name = 'your space'
+    session = ''
     try:
-        req = DescribeVodSnapshotDataRequest()
-        req.SpaceList = 'your SpaceList'
-        req.StartTime = 'your StartTime'
-        req.EndTime = 'your EndTime'
-        req.SnapshotType = 'your SnapshotType'
-        req.TaskStageList = 'your TaskStageList'
-        req.Aggregation = 0
-        req.DetailFieldList = 'your DetailFieldList'
-        resp = vod_service.describe_vod_snapshot_data(req)
+        req = VodCommitUploadInfoRequest()
+        req.SpaceName = space_name
+        req.SessionKey = session
+        get_meta_function = Function.get_meta_func()
+        snapshot_function = Function.get_snapshot_func(2.3)
+        req.Functions = json.dumps([get_meta_function, snapshot_function])
+        resp = vod_service.commit_upload_info(req)
     except Exception:
         raise
     else:
         print(resp)
-        if resp.ResponseMetadata.Error.Code != '':
+        if resp.ResponseMetadata.Error.Code == '':
+            print(resp.Result.Data)
+            print(resp.Result.Data.Vid)
+            print(resp.Result.Data.PosterUri)
+            print(resp.Result.Data.SourceInfo.Height)
+            print(resp.Result.Data.SourceInfo.Width)
+        else:
             print(resp.ResponseMetadata.Error)
-            
+            print(resp.ResponseMetadata.RequestId)
```

### Comparing `volcengine-1.0.84/volcengine/example/sms/example_insert_sms_sub_account.py` & `volcengine-1.0.9/volcengine/example/visual/example_video_retargeting_submit_task.py`

 * *Files 26% similar despite different names*

```diff
@@ -1,25 +1,23 @@
 # coding:utf-8
 from __future__ import print_function
 
-import json
+import time
 
-from volcengine.sms.SmsService import SmsService
-from volcengine.const.Const import *
+from volcengine.visual.VisualService import VisualService
 
 if __name__ == '__main__':
-    sms_service = SmsService()
-    # oversea
-    # sms_service = SmsService(REGION_AP_SINGAPORE1)
+    visual_service = VisualService()
 
     # call below method if you dont set ak and sk in $HOME/.volc/config
-    sms_service.set_ak('ak')
-    sms_service.set_sk('sk')
-    # sms_service.set_host('host')
-
-    body = {
-        "subAccountName": "smsAccount",
-        "desc": "desc",
+    visual_service.set_ak('ak')
+    visual_service.set_sk('sk')
+
+    form = {
+        "strategy": "STATIC_CROPPING",
+        "aspect_ratio": 1,
+        "crop_size": 1,
+        "video_url": ""
     }
 
-    resp = sms_service.insert_sms_sub_account(body)
+    resp = visual_service.video_retargeting_submit_task(form)
     print(resp)
```

### Comparing `volcengine-1.0.84/volcengine/example/imagex/example_upload_image.py` & `volcengine-1.0.9/volcengine/example/imagex/example_upload_image.py`

 * *Files identical despite different names*

### Comparing `volcengine-1.0.84/volcengine/example/visual/example_video_summarization_submit_task.py` & `volcengine-1.0.9/volcengine/example/visual/example_video_summarization_submit_task.py`

 * *Files identical despite different names*

