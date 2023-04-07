# Comparing `tmp/slack_sdk-3.9.0rc2.tar.gz` & `tmp/slack_sdk-3.9.1.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "slack_sdk-3.9.0rc2.tar", last modified: Fri Aug 13 02:56:09 2021, max compression
+gzip compressed data, was "slack_sdk-3.9.1.tar", last modified: Tue Aug 17 11:04:21 2021, max compression
```

## Comparing `slack_sdk-3.9.0rc2.tar` & `slack_sdk-3.9.1.tar`

### file list

```diff
@@ -1,207 +1,207 @@
-drwxr-xr-x   0 ksera      (502) staff       (20)        0 2021-08-13 02:56:09.241269 slack_sdk-3.9.0rc2/
--rw-r--r--   0 ksera      (502) staff       (20)     1095 2019-09-22 23:28:29.000000 slack_sdk-3.9.0rc2/LICENSE
--rw-r--r--   0 ksera      (502) staff       (20)       60 2020-10-27 05:09:55.000000 slack_sdk-3.9.0rc2/MANIFEST.in
--rw-r--r--   0 ksera      (502) staff       (20)    16143 2021-08-13 02:56:09.241744 slack_sdk-3.9.0rc2/PKG-INFO
--rwxr-xr-x   0 ksera      (502) staff       (20)    12741 2021-07-29 08:18:46.000000 slack_sdk-3.9.0rc2/README.md
--rw-r--r--   0 ksera      (502) staff       (20)       63 2021-08-13 02:56:09.249227 slack_sdk-3.9.0rc2/setup.cfg
--rw-r--r--   0 ksera      (502) staff       (20)    10696 2021-08-07 02:47:20.000000 slack_sdk-3.9.0rc2/setup.py
-drwxr-xr-x   0 ksera      (502) staff       (20)        0 2021-08-13 02:56:08.537606 slack_sdk-3.9.0rc2/slack/
--rw-r--r--   0 ksera      (502) staff       (20)      578 2020-10-27 05:09:55.000000 slack_sdk-3.9.0rc2/slack/__init__.py
--rw-r--r--   0 ksera      (502) staff       (20)      426 2020-10-27 05:09:55.000000 slack_sdk-3.9.0rc2/slack/deprecation.py
--rw-r--r--   0 ksera      (502) staff       (20)      432 2020-10-27 05:09:55.000000 slack_sdk-3.9.0rc2/slack/errors.py
--rw-r--r--   0 ksera      (502) staff       (20)        0 2020-09-15 10:26:35.000000 slack_sdk-3.9.0rc2/slack/py.typed
-drwxr-xr-x   0 ksera      (502) staff       (20)        0 2021-08-13 02:56:08.538730 slack_sdk-3.9.0rc2/slack/rtm/
--rw-r--r--   0 ksera      (502) staff       (20)      209 2020-10-27 05:09:55.000000 slack_sdk-3.9.0rc2/slack/rtm/__init__.py
--rw-r--r--   0 ksera      (502) staff       (20)      212 2020-10-27 05:15:56.000000 slack_sdk-3.9.0rc2/slack/rtm/client.py
-drwxr-xr-x   0 ksera      (502) staff       (20)        0 2021-08-13 02:56:08.540013 slack_sdk-3.9.0rc2/slack/signature/
--rw-r--r--   0 ksera      (502) staff       (20)      148 2020-10-27 05:09:55.000000 slack_sdk-3.9.0rc2/slack/signature/__init__.py
--rw-r--r--   0 ksera      (502) staff       (20)     2373 2021-05-07 21:39:57.000000 slack_sdk-3.9.0rc2/slack/signature/verifier.py
--rw-r--r--   0 ksera      (502) staff       (20)       50 2020-10-27 05:15:43.000000 slack_sdk-3.9.0rc2/slack/version.py
-drwxr-xr-x   0 ksera      (502) staff       (20)        0 2021-08-13 02:56:08.547967 slack_sdk-3.9.0rc2/slack/web/
--rw-r--r--   0 ksera      (502) staff       (20)      605 2020-10-27 05:09:55.000000 slack_sdk-3.9.0rc2/slack/web/__init__.py
--rw-r--r--   0 ksera      (502) staff       (20)     5862 2021-05-07 21:39:57.000000 slack_sdk-3.9.0rc2/slack/web/async_base_client.py
--rw-r--r--   0 ksera      (502) staff       (20)      519 2020-10-27 05:16:38.000000 slack_sdk-3.9.0rc2/slack/web/async_client.py
--rw-r--r--   0 ksera      (502) staff       (20)     6080 2020-10-27 05:09:55.000000 slack_sdk-3.9.0rc2/slack/web/async_internal_utils.py
--rw-r--r--   0 ksera      (502) staff       (20)     5825 2021-05-07 21:39:57.000000 slack_sdk-3.9.0rc2/slack/web/async_slack_response.py
--rw-r--r--   0 ksera      (502) staff       (20)    20791 2021-05-07 21:39:57.000000 slack_sdk-3.9.0rc2/slack/web/base_client.py
-drwxr-xr-x   0 ksera      (502) staff       (20)        0 2021-08-13 02:56:08.558173 slack_sdk-3.9.0rc2/slack/web/classes/
--rw-r--r--   0 ksera      (502) staff       (20)      397 2020-10-27 05:09:55.000000 slack_sdk-3.9.0rc2/slack/web/classes/__init__.py
--rw-r--r--   0 ksera      (502) staff       (20)      716 2021-05-07 21:39:57.000000 slack_sdk-3.9.0rc2/slack/web/classes/actions.py
--rw-r--r--   0 ksera      (502) staff       (20)      422 2020-10-27 05:09:55.000000 slack_sdk-3.9.0rc2/slack/web/classes/attachments.py
--rw-r--r--   0 ksera      (502) staff       (20)      645 2020-10-27 05:17:05.000000 slack_sdk-3.9.0rc2/slack/web/classes/blocks.py
--rw-r--r--   0 ksera      (502) staff       (20)      750 2021-05-07 21:39:57.000000 slack_sdk-3.9.0rc2/slack/web/classes/dialog_elements.py
--rw-r--r--   0 ksera      (502) staff       (20)      154 2021-05-07 21:39:57.000000 slack_sdk-3.9.0rc2/slack/web/classes/dialogs.py
--rw-r--r--   0 ksera      (502) staff       (20)     1585 2020-10-27 05:17:31.000000 slack_sdk-3.9.0rc2/slack/web/classes/elements.py
--rw-r--r--   0 ksera      (502) staff       (20)     4539 2020-09-15 10:26:35.000000 slack_sdk-3.9.0rc2/slack/web/classes/interactions.py
--rw-r--r--   0 ksera      (502) staff       (20)       62 2020-10-27 05:09:55.000000 slack_sdk-3.9.0rc2/slack/web/classes/messages.py
--rw-r--r--   0 ksera      (502) staff       (20)      909 2020-10-27 05:17:47.000000 slack_sdk-3.9.0rc2/slack/web/classes/objects.py
--rw-r--r--   0 ksera      (502) staff       (20)      252 2020-10-27 05:17:56.000000 slack_sdk-3.9.0rc2/slack/web/classes/views.py
--rw-r--r--   0 ksera      (502) staff       (20)      167 2020-10-27 05:16:35.000000 slack_sdk-3.9.0rc2/slack/web/client.py
--rw-r--r--   0 ksera      (502) staff       (20)     1018 2020-09-15 10:26:35.000000 slack_sdk-3.9.0rc2/slack/web/deprecation.py
--rw-r--r--   0 ksera      (502) staff       (20)     1635 2020-09-15 10:26:35.000000 slack_sdk-3.9.0rc2/slack/web/internal_utils.py
--rw-r--r--   0 ksera      (502) staff       (20)      200 2020-10-27 05:09:55.000000 slack_sdk-3.9.0rc2/slack/web/slack_response.py
-drwxr-xr-x   0 ksera      (502) staff       (20)        0 2021-08-13 02:56:08.567446 slack_sdk-3.9.0rc2/slack/webhook/
--rw-r--r--   0 ksera      (502) staff       (20)      288 2020-10-27 05:09:55.000000 slack_sdk-3.9.0rc2/slack/webhook/__init__.py
--rw-r--r--   0 ksera      (502) staff       (20)     4575 2021-05-07 21:39:57.000000 slack_sdk-3.9.0rc2/slack/webhook/async_client.py
--rw-r--r--   0 ksera      (502) staff       (20)     4725 2021-05-07 21:39:57.000000 slack_sdk-3.9.0rc2/slack/webhook/client.py
--rw-r--r--   0 ksera      (502) staff       (20)     1223 2021-05-07 21:39:57.000000 slack_sdk-3.9.0rc2/slack/webhook/internal_utils.py
--rw-r--r--   0 ksera      (502) staff       (20)      281 2021-05-07 21:39:57.000000 slack_sdk-3.9.0rc2/slack/webhook/webhook_response.py
-drwxr-xr-x   0 ksera      (502) staff       (20)        0 2021-08-13 02:56:08.575875 slack_sdk-3.9.0rc2/slack_sdk/
--rw-r--r--   0 ksera      (502) staff       (20)     1429 2021-05-07 21:39:57.000000 slack_sdk-3.9.0rc2/slack_sdk/__init__.py
--rw-r--r--   0 ksera      (502) staff       (20)      958 2021-05-07 21:39:57.000000 slack_sdk-3.9.0rc2/slack_sdk/aiohttp_version_checker.py
-drwxr-xr-x   0 ksera      (502) staff       (20)        0 2021-08-13 02:56:08.590214 slack_sdk-3.9.0rc2/slack_sdk/audit_logs/
--rw-r--r--   0 ksera      (502) staff       (20)      279 2021-05-07 21:39:57.000000 slack_sdk-3.9.0rc2/slack_sdk/audit_logs/__init__.py
--rw-r--r--   0 ksera      (502) staff       (20)       58 2021-05-07 21:39:57.000000 slack_sdk-3.9.0rc2/slack_sdk/audit_logs/async_client.py
-drwxr-xr-x   0 ksera      (502) staff       (20)        0 2021-08-13 02:56:08.686148 slack_sdk-3.9.0rc2/slack_sdk/audit_logs/v1/
--rw-r--r--   0 ksera      (502) staff       (20)      181 2021-05-07 21:39:57.000000 slack_sdk-3.9.0rc2/slack_sdk/audit_logs/v1/__init__.py
--rw-r--r--   0 ksera      (502) staff       (20)    14308 2021-08-07 02:47:20.000000 slack_sdk-3.9.0rc2/slack_sdk/audit_logs/v1/async_client.py
--rw-r--r--   0 ksera      (502) staff       (20)    14231 2021-08-07 02:47:20.000000 slack_sdk-3.9.0rc2/slack_sdk/audit_logs/v1/client.py
--rw-r--r--   0 ksera      (502) staff       (20)     1426 2021-05-07 21:39:57.000000 slack_sdk-3.9.0rc2/slack_sdk/audit_logs/v1/internal_utils.py
--rw-r--r--   0 ksera      (502) staff       (20)    16879 2021-07-15 07:11:53.000000 slack_sdk-3.9.0rc2/slack_sdk/audit_logs/v1/logs.py
--rw-r--r--   0 ksera      (502) staff       (20)      774 2021-05-07 21:39:57.000000 slack_sdk-3.9.0rc2/slack_sdk/audit_logs/v1/response.py
-drwxr-xr-x   0 ksera      (502) staff       (20)        0 2021-08-13 02:56:08.688155 slack_sdk-3.9.0rc2/slack_sdk/errors/
--rw-r--r--   0 ksera      (502) staff       (20)     1908 2021-08-07 02:47:20.000000 slack_sdk-3.9.0rc2/slack_sdk/errors/__init__.py
-drwxr-xr-x   0 ksera      (502) staff       (20)        0 2021-08-13 02:56:08.724439 slack_sdk-3.9.0rc2/slack_sdk/http_retry/
--rw-r--r--   0 ksera      (502) staff       (20)      901 2021-08-07 02:47:20.000000 slack_sdk-3.9.0rc2/slack_sdk/http_retry/__init__.py
--rw-r--r--   0 ksera      (502) staff       (20)     2502 2021-08-07 02:47:20.000000 slack_sdk-3.9.0rc2/slack_sdk/http_retry/async_handler.py
--rw-r--r--   0 ksera      (502) staff       (20)     2890 2021-08-07 02:47:20.000000 slack_sdk-3.9.0rc2/slack_sdk/http_retry/builtin_async_handlers.py
--rw-r--r--   0 ksera      (502) staff       (20)     2724 2021-08-07 02:47:20.000000 slack_sdk-3.9.0rc2/slack_sdk/http_retry/builtin_handlers.py
--rw-r--r--   0 ksera      (502) staff       (20)     1622 2021-08-07 02:47:20.000000 slack_sdk-3.9.0rc2/slack_sdk/http_retry/builtin_interval_calculators.py
--rw-r--r--   0 ksera      (502) staff       (20)     2487 2021-08-07 02:47:20.000000 slack_sdk-3.9.0rc2/slack_sdk/http_retry/handler.py
--rw-r--r--   0 ksera      (502) staff       (20)      450 2021-08-07 02:47:20.000000 slack_sdk-3.9.0rc2/slack_sdk/http_retry/interval_calculator.py
--rw-r--r--   0 ksera      (502) staff       (20)      597 2021-08-07 02:47:20.000000 slack_sdk-3.9.0rc2/slack_sdk/http_retry/jitter.py
--rw-r--r--   0 ksera      (502) staff       (20)     1087 2021-08-07 02:47:20.000000 slack_sdk-3.9.0rc2/slack_sdk/http_retry/request.py
--rw-r--r--   0 ksera      (502) staff       (20)      644 2021-08-07 02:47:20.000000 slack_sdk-3.9.0rc2/slack_sdk/http_retry/response.py
--rw-r--r--   0 ksera      (502) staff       (20)      570 2021-08-07 02:47:20.000000 slack_sdk-3.9.0rc2/slack_sdk/http_retry/state.py
-drwxr-xr-x   0 ksera      (502) staff       (20)        0 2021-08-13 02:56:08.730184 slack_sdk-3.9.0rc2/slack_sdk/models/
--rw-r--r--   0 ksera      (502) staff       (20)     1918 2021-05-07 21:39:57.000000 slack_sdk-3.9.0rc2/slack_sdk/models/__init__.py
-drwxr-xr-x   0 ksera      (502) staff       (20)        0 2021-08-13 02:56:08.732058 slack_sdk-3.9.0rc2/slack_sdk/models/attachments/
--rw-r--r--   0 ksera      (502) staff       (20)    24573 2021-05-07 21:39:57.000000 slack_sdk-3.9.0rc2/slack_sdk/models/attachments/__init__.py
--rw-r--r--   0 ksera      (502) staff       (20)     3847 2021-05-07 21:39:57.000000 slack_sdk-3.9.0rc2/slack_sdk/models/basic_objects.py
-drwxr-xr-x   0 ksera      (502) staff       (20)        0 2021-08-13 02:56:08.743856 slack_sdk-3.9.0rc2/slack_sdk/models/blocks/
--rw-r--r--   0 ksera      (502) staff       (20)     2419 2021-05-20 23:17:44.000000 slack_sdk-3.9.0rc2/slack_sdk/models/blocks/__init__.py
--rw-r--r--   0 ksera      (502) staff       (20)    19745 2021-05-07 21:39:57.000000 slack_sdk-3.9.0rc2/slack_sdk/models/blocks/basic_components.py
--rw-r--r--   0 ksera      (502) staff       (20)    40588 2021-06-14 21:14:05.000000 slack_sdk-3.9.0rc2/slack_sdk/models/blocks/block_elements.py
--rw-r--r--   0 ksera      (502) staff       (20)    14144 2021-05-07 21:39:57.000000 slack_sdk-3.9.0rc2/slack_sdk/models/blocks/blocks.py
--rw-r--r--   0 ksera      (502) staff       (20)      810 2021-05-07 21:39:57.000000 slack_sdk-3.9.0rc2/slack_sdk/models/dialoags.py
-drwxr-xr-x   0 ksera      (502) staff       (20)        0 2021-08-13 02:56:08.745741 slack_sdk-3.9.0rc2/slack_sdk/models/dialogs/
--rw-r--r--   0 ksera      (502) staff       (20)    32390 2021-05-07 21:39:57.000000 slack_sdk-3.9.0rc2/slack_sdk/models/dialogs/__init__.py
-drwxr-xr-x   0 ksera      (502) staff       (20)        0 2021-08-13 02:56:08.749865 slack_sdk-3.9.0rc2/slack_sdk/models/messages/
--rw-r--r--   0 ksera      (502) staff       (20)     2736 2020-10-27 05:09:55.000000 slack_sdk-3.9.0rc2/slack_sdk/models/messages/__init__.py
--rw-r--r--   0 ksera      (502) staff       (20)     3039 2021-05-07 21:39:57.000000 slack_sdk-3.9.0rc2/slack_sdk/models/messages/message.py
-drwxr-xr-x   0 ksera      (502) staff       (20)        0 2021-08-13 02:56:08.751764 slack_sdk-3.9.0rc2/slack_sdk/models/views/
--rw-r--r--   0 ksera      (502) staff       (20)     9017 2021-05-28 11:02:50.000000 slack_sdk-3.9.0rc2/slack_sdk/models/views/__init__.py
-drwxr-xr-x   0 ksera      (502) staff       (20)        0 2021-08-13 02:56:08.753760 slack_sdk-3.9.0rc2/slack_sdk/oauth/
--rw-r--r--   0 ksera      (502) staff       (20)      471 2021-08-01 22:11:58.000000 slack_sdk-3.9.0rc2/slack_sdk/oauth/__init__.py
-drwxr-xr-x   0 ksera      (502) staff       (20)        0 2021-08-13 02:56:08.768010 slack_sdk-3.9.0rc2/slack_sdk/oauth/authorize_url_generator/
--rw-r--r--   0 ksera      (502) staff       (20)     2029 2021-08-02 12:24:16.000000 slack_sdk-3.9.0rc2/slack_sdk/oauth/authorize_url_generator/__init__.py
-drwxr-xr-x   0 ksera      (502) staff       (20)        0 2021-08-13 02:56:08.780697 slack_sdk-3.9.0rc2/slack_sdk/oauth/installation_store/
--rw-r--r--   0 ksera      (502) staff       (20)      152 2020-10-27 05:09:55.000000 slack_sdk-3.9.0rc2/slack_sdk/oauth/installation_store/__init__.py
-drwxr-xr-x   0 ksera      (502) staff       (20)        0 2021-08-13 02:56:08.782454 slack_sdk-3.9.0rc2/slack_sdk/oauth/installation_store/amazon_s3/
--rw-r--r--   0 ksera      (502) staff       (20)    12499 2021-08-07 02:47:20.000000 slack_sdk-3.9.0rc2/slack_sdk/oauth/installation_store/amazon_s3/__init__.py
--rw-r--r--   0 ksera      (502) staff       (20)     4751 2021-07-15 07:11:53.000000 slack_sdk-3.9.0rc2/slack_sdk/oauth/installation_store/async_cacheable_installation_store.py
--rw-r--r--   0 ksera      (502) staff       (20)     2995 2021-07-15 07:11:53.000000 slack_sdk-3.9.0rc2/slack_sdk/oauth/installation_store/async_installation_store.py
--rw-r--r--   0 ksera      (502) staff       (20)     4546 2021-07-15 07:11:53.000000 slack_sdk-3.9.0rc2/slack_sdk/oauth/installation_store/cacheable_installation_store.py
-drwxr-xr-x   0 ksera      (502) staff       (20)        0 2021-08-13 02:56:08.784333 slack_sdk-3.9.0rc2/slack_sdk/oauth/installation_store/file/
--rw-r--r--   0 ksera      (502) staff       (20)     8142 2021-07-15 07:11:53.000000 slack_sdk-3.9.0rc2/slack_sdk/oauth/installation_store/file/__init__.py
--rw-r--r--   0 ksera      (502) staff       (20)     2891 2021-07-15 07:11:53.000000 slack_sdk-3.9.0rc2/slack_sdk/oauth/installation_store/installation_store.py
--rw-r--r--   0 ksera      (502) staff       (20)      934 2021-07-15 07:11:53.000000 slack_sdk-3.9.0rc2/slack_sdk/oauth/installation_store/internals.py
-drwxr-xr-x   0 ksera      (502) staff       (20)        0 2021-08-13 02:56:08.789928 slack_sdk-3.9.0rc2/slack_sdk/oauth/installation_store/models/
--rw-r--r--   0 ksera      (502) staff       (20)       76 2020-10-27 05:09:55.000000 slack_sdk-3.9.0rc2/slack_sdk/oauth/installation_store/models/__init__.py
--rw-r--r--   0 ksera      (502) staff       (20)     5010 2021-07-15 07:11:53.000000 slack_sdk-3.9.0rc2/slack_sdk/oauth/installation_store/models/bot.py
--rw-r--r--   0 ksera      (502) staff       (20)     9602 2021-07-15 07:11:53.000000 slack_sdk-3.9.0rc2/slack_sdk/oauth/installation_store/models/installation.py
-drwxr-xr-x   0 ksera      (502) staff       (20)        0 2021-08-13 02:56:08.791832 slack_sdk-3.9.0rc2/slack_sdk/oauth/installation_store/sqlalchemy/
--rw-r--r--   0 ksera      (502) staff       (20)    13051 2021-07-30 07:12:34.000000 slack_sdk-3.9.0rc2/slack_sdk/oauth/installation_store/sqlalchemy/__init__.py
-drwxr-xr-x   0 ksera      (502) staff       (20)        0 2021-08-13 02:56:08.793710 slack_sdk-3.9.0rc2/slack_sdk/oauth/installation_store/sqlite3/
--rw-r--r--   0 ksera      (502) staff       (20)    20886 2021-07-15 07:11:53.000000 slack_sdk-3.9.0rc2/slack_sdk/oauth/installation_store/sqlite3/__init__.py
-drwxr-xr-x   0 ksera      (502) staff       (20)        0 2021-08-13 02:56:08.795813 slack_sdk-3.9.0rc2/slack_sdk/oauth/redirect_uri_page_renderer/
--rw-r--r--   0 ksera      (502) staff       (20)     1991 2021-05-07 21:39:57.000000 slack_sdk-3.9.0rc2/slack_sdk/oauth/redirect_uri_page_renderer/__init__.py
-drwxr-xr-x   0 ksera      (502) staff       (20)        0 2021-08-13 02:56:08.801220 slack_sdk-3.9.0rc2/slack_sdk/oauth/state_store/
--rw-r--r--   0 ksera      (502) staff       (20)      261 2021-05-07 21:39:57.000000 slack_sdk-3.9.0rc2/slack_sdk/oauth/state_store/__init__.py
-drwxr-xr-x   0 ksera      (502) staff       (20)        0 2021-08-13 02:56:08.803263 slack_sdk-3.9.0rc2/slack_sdk/oauth/state_store/amazon_s3/
--rw-r--r--   0 ksera      (502) staff       (20)     2248 2021-05-07 21:39:57.000000 slack_sdk-3.9.0rc2/slack_sdk/oauth/state_store/amazon_s3/__init__.py
--rw-r--r--   0 ksera      (502) staff       (20)      325 2020-11-07 14:22:06.000000 slack_sdk-3.9.0rc2/slack_sdk/oauth/state_store/async_state_store.py
-drwxr-xr-x   0 ksera      (502) staff       (20)        0 2021-08-13 02:56:08.806146 slack_sdk-3.9.0rc2/slack_sdk/oauth/state_store/file/
--rw-r--r--   0 ksera      (502) staff       (20)     2220 2020-11-07 14:22:06.000000 slack_sdk-3.9.0rc2/slack_sdk/oauth/state_store/file/__init__.py
-drwxr-xr-x   0 ksera      (502) staff       (20)        0 2021-08-13 02:56:08.809022 slack_sdk-3.9.0rc2/slack_sdk/oauth/state_store/sqlalchemy/
--rw-r--r--   0 ksera      (502) staff       (20)     2630 2021-06-18 05:18:34.000000 slack_sdk-3.9.0rc2/slack_sdk/oauth/state_store/sqlalchemy/__init__.py
-drwxr-xr-x   0 ksera      (502) staff       (20)        0 2021-08-13 02:56:08.811398 slack_sdk-3.9.0rc2/slack_sdk/oauth/state_store/sqlite3/
--rw-r--r--   0 ksera      (502) staff       (20)     3503 2020-11-07 14:22:06.000000 slack_sdk-3.9.0rc2/slack_sdk/oauth/state_store/sqlite3/__init__.py
--rw-r--r--   0 ksera      (502) staff       (20)      296 2020-11-07 14:03:53.000000 slack_sdk-3.9.0rc2/slack_sdk/oauth/state_store/state_store.py
-drwxr-xr-x   0 ksera      (502) staff       (20)        0 2021-08-13 02:56:08.813751 slack_sdk-3.9.0rc2/slack_sdk/oauth/state_utils/
--rw-r--r--   0 ksera      (502) staff       (20)     1656 2020-11-06 22:42:40.000000 slack_sdk-3.9.0rc2/slack_sdk/oauth/state_utils/__init__.py
-drwxr-xr-x   0 ksera      (502) staff       (20)        0 2021-08-13 02:56:08.823061 slack_sdk-3.9.0rc2/slack_sdk/oauth/token_rotation/
--rw-r--r--   0 ksera      (502) staff       (20)       42 2021-07-15 07:11:53.000000 slack_sdk-3.9.0rc2/slack_sdk/oauth/token_rotation/__init__.py
--rw-r--r--   0 ksera      (502) staff       (20)     5329 2021-07-15 07:11:53.000000 slack_sdk-3.9.0rc2/slack_sdk/oauth/token_rotation/async_rotator.py
--rw-r--r--   0 ksera      (502) staff       (20)     5159 2021-07-15 07:11:53.000000 slack_sdk-3.9.0rc2/slack_sdk/oauth/token_rotation/rotator.py
--rw-r--r--   0 ksera      (502) staff       (20)      599 2021-08-04 09:33:12.000000 slack_sdk-3.9.0rc2/slack_sdk/proxy_env_variable_loader.py
--rw-r--r--   0 ksera      (502) staff       (20)        0 2020-10-27 05:09:55.000000 slack_sdk-3.9.0rc2/slack_sdk/py.typed
-drwxr-xr-x   0 ksera      (502) staff       (20)        0 2021-08-13 02:56:08.825774 slack_sdk-3.9.0rc2/slack_sdk/rtm/
--rw-r--r--   0 ksera      (502) staff       (20)    24014 2021-05-07 21:39:57.000000 slack_sdk-3.9.0rc2/slack_sdk/rtm/__init__.py
-drwxr-xr-x   0 ksera      (502) staff       (20)        0 2021-08-13 02:56:08.828698 slack_sdk-3.9.0rc2/slack_sdk/rtm/v2/
--rw-r--r--   0 ksera      (502) staff       (20)       47 2021-05-07 21:39:57.000000 slack_sdk-3.9.0rc2/slack_sdk/rtm/v2/__init__.py
-drwxr-xr-x   0 ksera      (502) staff       (20)        0 2021-08-13 02:56:08.831520 slack_sdk-3.9.0rc2/slack_sdk/rtm_v2/
--rw-r--r--   0 ksera      (502) staff       (20)    16519 2021-05-07 21:39:57.000000 slack_sdk-3.9.0rc2/slack_sdk/rtm_v2/__init__.py
-drwxr-xr-x   0 ksera      (502) staff       (20)        0 2021-08-13 02:56:08.838062 slack_sdk-3.9.0rc2/slack_sdk/scim/
--rw-r--r--   0 ksera      (502) staff       (20)      585 2021-05-07 21:39:57.000000 slack_sdk-3.9.0rc2/slack_sdk/scim/__init__.py
--rw-r--r--   0 ksera      (502) staff       (20)       53 2021-05-07 21:39:57.000000 slack_sdk-3.9.0rc2/slack_sdk/scim/async_client.py
-drwxr-xr-x   0 ksera      (502) staff       (20)        0 2021-08-13 02:56:08.877431 slack_sdk-3.9.0rc2/slack_sdk/scim/v1/
--rw-r--r--   0 ksera      (502) staff       (20)      283 2021-05-07 21:39:57.000000 slack_sdk-3.9.0rc2/slack_sdk/scim/v1/__init__.py
--rw-r--r--   0 ksera      (502) staff       (20)    15242 2021-08-07 02:47:20.000000 slack_sdk-3.9.0rc2/slack_sdk/scim/v1/async_client.py
--rw-r--r--   0 ksera      (502) staff       (20)    15646 2021-08-07 02:47:20.000000 slack_sdk-3.9.0rc2/slack_sdk/scim/v1/client.py
--rw-r--r--   0 ksera      (502) staff       (20)       53 2021-05-07 21:39:57.000000 slack_sdk-3.9.0rc2/slack_sdk/scim/v1/default_arg.py
--rw-r--r--   0 ksera      (502) staff       (20)     2522 2021-05-07 21:39:57.000000 slack_sdk-3.9.0rc2/slack_sdk/scim/v1/group.py
--rw-r--r--   0 ksera      (502) staff       (20)     5068 2021-05-07 21:39:57.000000 slack_sdk-3.9.0rc2/slack_sdk/scim/v1/internal_utils.py
--rw-r--r--   0 ksera      (502) staff       (20)     7575 2021-05-07 21:39:57.000000 slack_sdk-3.9.0rc2/slack_sdk/scim/v1/response.py
--rw-r--r--   0 ksera      (502) staff       (20)      798 2021-05-07 21:39:57.000000 slack_sdk-3.9.0rc2/slack_sdk/scim/v1/types.py
--rw-r--r--   0 ksera      (502) staff       (20)     8062 2021-05-07 21:39:57.000000 slack_sdk-3.9.0rc2/slack_sdk/scim/v1/user.py
-drwxr-xr-x   0 ksera      (502) staff       (20)        0 2021-08-13 02:56:08.882818 slack_sdk-3.9.0rc2/slack_sdk/signature/
--rw-r--r--   0 ksera      (502) staff       (20)     2419 2021-05-07 21:39:57.000000 slack_sdk-3.9.0rc2/slack_sdk/signature/__init__.py
-drwxr-xr-x   0 ksera      (502) staff       (20)        0 2021-08-13 02:56:08.942875 slack_sdk-3.9.0rc2/slack_sdk/socket_mode/
--rw-r--r--   0 ksera      (502) staff       (20)      327 2021-05-07 21:39:57.000000 slack_sdk-3.9.0rc2/slack_sdk/socket_mode/__init__.py
-drwxr-xr-x   0 ksera      (502) staff       (20)        0 2021-08-13 02:56:08.952450 slack_sdk-3.9.0rc2/slack_sdk/socket_mode/aiohttp/
--rw-r--r--   0 ksera      (502) staff       (20)     9811 2021-07-29 08:18:46.000000 slack_sdk-3.9.0rc2/slack_sdk/socket_mode/aiohttp/__init__.py
--rw-r--r--   0 ksera      (502) staff       (20)     5690 2021-07-29 08:18:46.000000 slack_sdk-3.9.0rc2/slack_sdk/socket_mode/async_client.py
--rw-r--r--   0 ksera      (502) staff       (20)      580 2021-05-07 21:39:57.000000 slack_sdk-3.9.0rc2/slack_sdk/socket_mode/async_listeners.py
-drwxr-xr-x   0 ksera      (502) staff       (20)        0 2021-08-13 02:56:09.214390 slack_sdk-3.9.0rc2/slack_sdk/socket_mode/builtin/
--rw-r--r--   0 ksera      (502) staff       (20)       45 2021-05-07 21:39:57.000000 slack_sdk-3.9.0rc2/slack_sdk/socket_mode/builtin/__init__.py
--rw-r--r--   0 ksera      (502) staff       (20)    11251 2021-05-07 21:39:57.000000 slack_sdk-3.9.0rc2/slack_sdk/socket_mode/builtin/client.py
--rw-r--r--   0 ksera      (502) staff       (20)    19753 2021-05-07 21:39:57.000000 slack_sdk-3.9.0rc2/slack_sdk/socket_mode/builtin/connection.py
--rw-r--r--   0 ksera      (502) staff       (20)     1066 2021-05-07 21:39:57.000000 slack_sdk-3.9.0rc2/slack_sdk/socket_mode/builtin/frame_header.py
--rw-r--r--   0 ksera      (502) staff       (20)    14132 2021-08-13 02:55:27.000000 slack_sdk-3.9.0rc2/slack_sdk/socket_mode/builtin/internals.py
--rw-r--r--   0 ksera      (502) staff       (20)     6175 2021-05-07 21:39:57.000000 slack_sdk-3.9.0rc2/slack_sdk/socket_mode/client.py
--rw-r--r--   0 ksera      (502) staff       (20)      914 2021-06-14 21:14:05.000000 slack_sdk-3.9.0rc2/slack_sdk/socket_mode/interval_runner.py
--rw-r--r--   0 ksera      (502) staff       (20)      509 2021-05-07 21:39:57.000000 slack_sdk-3.9.0rc2/slack_sdk/socket_mode/listeners.py
--rw-r--r--   0 ksera      (502) staff       (20)     1929 2021-05-07 21:39:57.000000 slack_sdk-3.9.0rc2/slack_sdk/socket_mode/request.py
--rw-r--r--   0 ksera      (502) staff       (20)      894 2021-05-07 21:39:57.000000 slack_sdk-3.9.0rc2/slack_sdk/socket_mode/response.py
-drwxr-xr-x   0 ksera      (502) staff       (20)        0 2021-08-13 02:56:09.215808 slack_sdk-3.9.0rc2/slack_sdk/socket_mode/websocket_client/
--rw-r--r--   0 ksera      (502) staff       (20)     9574 2021-05-28 21:12:15.000000 slack_sdk-3.9.0rc2/slack_sdk/socket_mode/websocket_client/__init__.py
-drwxr-xr-x   0 ksera      (502) staff       (20)        0 2021-08-13 02:56:09.217088 slack_sdk-3.9.0rc2/slack_sdk/socket_mode/websockets/
--rw-r--r--   0 ksera      (502) staff       (20)     6740 2021-07-29 08:18:46.000000 slack_sdk-3.9.0rc2/slack_sdk/socket_mode/websockets/__init__.py
--rw-r--r--   0 ksera      (502) staff       (20)       95 2021-08-13 02:55:37.000000 slack_sdk-3.9.0rc2/slack_sdk/version.py
-drwxr-xr-x   0 ksera      (502) staff       (20)        0 2021-08-13 02:56:09.236594 slack_sdk-3.9.0rc2/slack_sdk/web/
--rw-r--r--   0 ksera      (502) staff       (20)      240 2021-05-07 21:39:57.000000 slack_sdk-3.9.0rc2/slack_sdk/web/__init__.py
--rw-r--r--   0 ksera      (502) staff       (20)     7119 2021-08-07 02:47:20.000000 slack_sdk-3.9.0rc2/slack_sdk/web/async_base_client.py
--rw-r--r--   0 ksera      (502) staff       (20)   115237 2021-08-13 02:55:27.000000 slack_sdk-3.9.0rc2/slack_sdk/web/async_client.py
--rw-r--r--   0 ksera      (502) staff       (20)     8150 2021-08-07 02:47:20.000000 slack_sdk-3.9.0rc2/slack_sdk/web/async_internal_utils.py
--rw-r--r--   0 ksera      (502) staff       (20)     6889 2021-05-07 21:39:57.000000 slack_sdk-3.9.0rc2/slack_sdk/web/async_slack_response.py
--rw-r--r--   0 ksera      (502) staff       (20)    23669 2021-08-07 02:47:20.000000 slack_sdk-3.9.0rc2/slack_sdk/web/base_client.py
--rw-r--r--   0 ksera      (502) staff       (20)   109719 2021-08-13 02:55:27.000000 slack_sdk-3.9.0rc2/slack_sdk/web/client.py
--rw-r--r--   0 ksera      (502) staff       (20)     1018 2020-10-27 05:09:55.000000 slack_sdk-3.9.0rc2/slack_sdk/web/deprecation.py
--rw-r--r--   0 ksera      (502) staff       (20)     9361 2021-07-15 07:11:53.000000 slack_sdk-3.9.0rc2/slack_sdk/web/internal_utils.py
--rw-r--r--   0 ksera      (502) staff       (20)    23155 2021-05-07 21:39:57.000000 slack_sdk-3.9.0rc2/slack_sdk/web/legacy_base_client.py
--rw-r--r--   0 ksera      (502) staff       (20)   114522 2021-08-13 02:55:27.000000 slack_sdk-3.9.0rc2/slack_sdk/web/legacy_client.py
--rw-r--r--   0 ksera      (502) staff       (20)     7903 2021-01-29 07:26:58.000000 slack_sdk-3.9.0rc2/slack_sdk/web/legacy_slack_response.py
--rw-r--r--   0 ksera      (502) staff       (20)     6752 2021-07-15 07:11:53.000000 slack_sdk-3.9.0rc2/slack_sdk/web/slack_response.py
-drwxr-xr-x   0 ksera      (502) staff       (20)        0 2021-08-13 02:56:09.240428 slack_sdk-3.9.0rc2/slack_sdk/webhook/
--rw-r--r--   0 ksera      (502) staff       (20)      278 2021-05-07 21:39:57.000000 slack_sdk-3.9.0rc2/slack_sdk/webhook/__init__.py
--rw-r--r--   0 ksera      (502) staff       (20)    11509 2021-08-07 02:47:20.000000 slack_sdk-3.9.0rc2/slack_sdk/webhook/async_client.py
--rw-r--r--   0 ksera      (502) staff       (20)    11775 2021-08-07 02:47:20.000000 slack_sdk-3.9.0rc2/slack_sdk/webhook/client.py
--rw-r--r--   0 ksera      (502) staff       (20)     1351 2021-06-30 09:54:45.000000 slack_sdk-3.9.0rc2/slack_sdk/webhook/internal_utils.py
--rw-r--r--   0 ksera      (502) staff       (20)      281 2021-05-07 21:39:57.000000 slack_sdk-3.9.0rc2/slack_sdk/webhook/webhook_response.py
-drwxr-xr-x   0 ksera      (502) staff       (20)        0 2021-08-13 02:56:08.586651 slack_sdk-3.9.0rc2/slack_sdk.egg-info/
--rw-r--r--   0 ksera      (502) staff       (20)    16143 2021-08-13 02:56:08.000000 slack_sdk-3.9.0rc2/slack_sdk.egg-info/PKG-INFO
--rw-r--r--   0 ksera      (502) staff       (20)     5502 2021-08-13 02:56:08.000000 slack_sdk-3.9.0rc2/slack_sdk.egg-info/SOURCES.txt
--rw-r--r--   0 ksera      (502) staff       (20)        1 2021-08-13 02:56:08.000000 slack_sdk-3.9.0rc2/slack_sdk.egg-info/dependency_links.txt
--rw-r--r--   0 ksera      (502) staff       (20)      300 2021-08-13 02:56:08.000000 slack_sdk-3.9.0rc2/slack_sdk.egg-info/requires.txt
--rw-r--r--   0 ksera      (502) staff       (20)       16 2021-08-13 02:56:08.000000 slack_sdk-3.9.0rc2/slack_sdk.egg-info/top_level.txt
+drwxr-xr-x   0 ksera      (502) staff       (20)        0 2021-08-17 11:04:21.610636 slack_sdk-3.9.1/
+-rw-r--r--   0 ksera      (502) staff       (20)     1095 2019-09-22 23:28:29.000000 slack_sdk-3.9.1/LICENSE
+-rw-r--r--   0 ksera      (502) staff       (20)       60 2020-10-27 05:09:55.000000 slack_sdk-3.9.1/MANIFEST.in
+-rw-r--r--   0 ksera      (502) staff       (20)    16140 2021-08-17 11:04:21.611291 slack_sdk-3.9.1/PKG-INFO
+-rwxr-xr-x   0 ksera      (502) staff       (20)    12741 2021-07-29 08:18:46.000000 slack_sdk-3.9.1/README.md
+-rw-r--r--   0 ksera      (502) staff       (20)       63 2021-08-17 11:04:21.612819 slack_sdk-3.9.1/setup.cfg
+-rw-r--r--   0 ksera      (502) staff       (20)    10696 2021-08-17 07:37:17.000000 slack_sdk-3.9.1/setup.py
+drwxr-xr-x   0 ksera      (502) staff       (20)        0 2021-08-17 11:04:21.420096 slack_sdk-3.9.1/slack/
+-rw-r--r--   0 ksera      (502) staff       (20)      578 2020-10-27 05:09:55.000000 slack_sdk-3.9.1/slack/__init__.py
+-rw-r--r--   0 ksera      (502) staff       (20)      426 2020-10-27 05:09:55.000000 slack_sdk-3.9.1/slack/deprecation.py
+-rw-r--r--   0 ksera      (502) staff       (20)      432 2020-10-27 05:09:55.000000 slack_sdk-3.9.1/slack/errors.py
+-rw-r--r--   0 ksera      (502) staff       (20)        0 2020-09-15 10:26:35.000000 slack_sdk-3.9.1/slack/py.typed
+drwxr-xr-x   0 ksera      (502) staff       (20)        0 2021-08-17 11:04:21.422096 slack_sdk-3.9.1/slack/rtm/
+-rw-r--r--   0 ksera      (502) staff       (20)      209 2020-10-27 05:09:55.000000 slack_sdk-3.9.1/slack/rtm/__init__.py
+-rw-r--r--   0 ksera      (502) staff       (20)      212 2020-10-27 05:15:56.000000 slack_sdk-3.9.1/slack/rtm/client.py
+drwxr-xr-x   0 ksera      (502) staff       (20)        0 2021-08-17 11:04:21.423919 slack_sdk-3.9.1/slack/signature/
+-rw-r--r--   0 ksera      (502) staff       (20)      148 2020-10-27 05:09:55.000000 slack_sdk-3.9.1/slack/signature/__init__.py
+-rw-r--r--   0 ksera      (502) staff       (20)     2373 2021-05-07 21:39:57.000000 slack_sdk-3.9.1/slack/signature/verifier.py
+-rw-r--r--   0 ksera      (502) staff       (20)       50 2020-10-27 05:15:43.000000 slack_sdk-3.9.1/slack/version.py
+drwxr-xr-x   0 ksera      (502) staff       (20)        0 2021-08-17 11:04:21.435924 slack_sdk-3.9.1/slack/web/
+-rw-r--r--   0 ksera      (502) staff       (20)      605 2020-10-27 05:09:55.000000 slack_sdk-3.9.1/slack/web/__init__.py
+-rw-r--r--   0 ksera      (502) staff       (20)     5862 2021-05-07 21:39:57.000000 slack_sdk-3.9.1/slack/web/async_base_client.py
+-rw-r--r--   0 ksera      (502) staff       (20)      519 2020-10-27 05:16:38.000000 slack_sdk-3.9.1/slack/web/async_client.py
+-rw-r--r--   0 ksera      (502) staff       (20)     6080 2020-10-27 05:09:55.000000 slack_sdk-3.9.1/slack/web/async_internal_utils.py
+-rw-r--r--   0 ksera      (502) staff       (20)     5825 2021-05-07 21:39:57.000000 slack_sdk-3.9.1/slack/web/async_slack_response.py
+-rw-r--r--   0 ksera      (502) staff       (20)    20791 2021-05-07 21:39:57.000000 slack_sdk-3.9.1/slack/web/base_client.py
+drwxr-xr-x   0 ksera      (502) staff       (20)        0 2021-08-17 11:04:21.447541 slack_sdk-3.9.1/slack/web/classes/
+-rw-r--r--   0 ksera      (502) staff       (20)      397 2020-10-27 05:09:55.000000 slack_sdk-3.9.1/slack/web/classes/__init__.py
+-rw-r--r--   0 ksera      (502) staff       (20)      716 2021-05-07 21:39:57.000000 slack_sdk-3.9.1/slack/web/classes/actions.py
+-rw-r--r--   0 ksera      (502) staff       (20)      422 2020-10-27 05:09:55.000000 slack_sdk-3.9.1/slack/web/classes/attachments.py
+-rw-r--r--   0 ksera      (502) staff       (20)      645 2020-10-27 05:17:05.000000 slack_sdk-3.9.1/slack/web/classes/blocks.py
+-rw-r--r--   0 ksera      (502) staff       (20)      750 2021-05-07 21:39:57.000000 slack_sdk-3.9.1/slack/web/classes/dialog_elements.py
+-rw-r--r--   0 ksera      (502) staff       (20)      154 2021-05-07 21:39:57.000000 slack_sdk-3.9.1/slack/web/classes/dialogs.py
+-rw-r--r--   0 ksera      (502) staff       (20)     1585 2020-10-27 05:17:31.000000 slack_sdk-3.9.1/slack/web/classes/elements.py
+-rw-r--r--   0 ksera      (502) staff       (20)     4539 2020-09-15 10:26:35.000000 slack_sdk-3.9.1/slack/web/classes/interactions.py
+-rw-r--r--   0 ksera      (502) staff       (20)       62 2020-10-27 05:09:55.000000 slack_sdk-3.9.1/slack/web/classes/messages.py
+-rw-r--r--   0 ksera      (502) staff       (20)      909 2020-10-27 05:17:47.000000 slack_sdk-3.9.1/slack/web/classes/objects.py
+-rw-r--r--   0 ksera      (502) staff       (20)      252 2020-10-27 05:17:56.000000 slack_sdk-3.9.1/slack/web/classes/views.py
+-rw-r--r--   0 ksera      (502) staff       (20)      167 2020-10-27 05:16:35.000000 slack_sdk-3.9.1/slack/web/client.py
+-rw-r--r--   0 ksera      (502) staff       (20)     1018 2020-09-15 10:26:35.000000 slack_sdk-3.9.1/slack/web/deprecation.py
+-rw-r--r--   0 ksera      (502) staff       (20)     1635 2020-09-15 10:26:35.000000 slack_sdk-3.9.1/slack/web/internal_utils.py
+-rw-r--r--   0 ksera      (502) staff       (20)      200 2020-10-27 05:09:55.000000 slack_sdk-3.9.1/slack/web/slack_response.py
+drwxr-xr-x   0 ksera      (502) staff       (20)        0 2021-08-17 11:04:21.452385 slack_sdk-3.9.1/slack/webhook/
+-rw-r--r--   0 ksera      (502) staff       (20)      288 2020-10-27 05:09:55.000000 slack_sdk-3.9.1/slack/webhook/__init__.py
+-rw-r--r--   0 ksera      (502) staff       (20)     4575 2021-05-07 21:39:57.000000 slack_sdk-3.9.1/slack/webhook/async_client.py
+-rw-r--r--   0 ksera      (502) staff       (20)     4725 2021-05-07 21:39:57.000000 slack_sdk-3.9.1/slack/webhook/client.py
+-rw-r--r--   0 ksera      (502) staff       (20)     1223 2021-05-07 21:39:57.000000 slack_sdk-3.9.1/slack/webhook/internal_utils.py
+-rw-r--r--   0 ksera      (502) staff       (20)      281 2021-05-07 21:39:57.000000 slack_sdk-3.9.1/slack/webhook/webhook_response.py
+drwxr-xr-x   0 ksera      (502) staff       (20)        0 2021-08-17 11:04:21.456995 slack_sdk-3.9.1/slack_sdk/
+-rw-r--r--   0 ksera      (502) staff       (20)     1429 2021-05-07 21:39:57.000000 slack_sdk-3.9.1/slack_sdk/__init__.py
+-rw-r--r--   0 ksera      (502) staff       (20)      958 2021-05-07 21:39:57.000000 slack_sdk-3.9.1/slack_sdk/aiohttp_version_checker.py
+drwxr-xr-x   0 ksera      (502) staff       (20)        0 2021-08-17 11:04:21.461630 slack_sdk-3.9.1/slack_sdk/audit_logs/
+-rw-r--r--   0 ksera      (502) staff       (20)      279 2021-05-07 21:39:57.000000 slack_sdk-3.9.1/slack_sdk/audit_logs/__init__.py
+-rw-r--r--   0 ksera      (502) staff       (20)       58 2021-05-07 21:39:57.000000 slack_sdk-3.9.1/slack_sdk/audit_logs/async_client.py
+drwxr-xr-x   0 ksera      (502) staff       (20)        0 2021-08-17 11:04:21.468893 slack_sdk-3.9.1/slack_sdk/audit_logs/v1/
+-rw-r--r--   0 ksera      (502) staff       (20)      181 2021-05-07 21:39:57.000000 slack_sdk-3.9.1/slack_sdk/audit_logs/v1/__init__.py
+-rw-r--r--   0 ksera      (502) staff       (20)    14384 2021-08-13 12:59:33.000000 slack_sdk-3.9.1/slack_sdk/audit_logs/v1/async_client.py
+-rw-r--r--   0 ksera      (502) staff       (20)    14307 2021-08-13 12:59:33.000000 slack_sdk-3.9.1/slack_sdk/audit_logs/v1/client.py
+-rw-r--r--   0 ksera      (502) staff       (20)     1426 2021-05-07 21:39:57.000000 slack_sdk-3.9.1/slack_sdk/audit_logs/v1/internal_utils.py
+-rw-r--r--   0 ksera      (502) staff       (20)    16879 2021-07-15 07:11:53.000000 slack_sdk-3.9.1/slack_sdk/audit_logs/v1/logs.py
+-rw-r--r--   0 ksera      (502) staff       (20)      774 2021-05-07 21:39:57.000000 slack_sdk-3.9.1/slack_sdk/audit_logs/v1/response.py
+drwxr-xr-x   0 ksera      (502) staff       (20)        0 2021-08-17 11:04:21.470084 slack_sdk-3.9.1/slack_sdk/errors/
+-rw-r--r--   0 ksera      (502) staff       (20)     1908 2021-08-07 02:47:20.000000 slack_sdk-3.9.1/slack_sdk/errors/__init__.py
+drwxr-xr-x   0 ksera      (502) staff       (20)        0 2021-08-17 11:04:21.481706 slack_sdk-3.9.1/slack_sdk/http_retry/
+-rw-r--r--   0 ksera      (502) staff       (20)      953 2021-08-13 09:15:11.000000 slack_sdk-3.9.1/slack_sdk/http_retry/__init__.py
+-rw-r--r--   0 ksera      (502) staff       (20)     2502 2021-08-07 02:47:20.000000 slack_sdk-3.9.1/slack_sdk/http_retry/async_handler.py
+-rw-r--r--   0 ksera      (502) staff       (20)     2977 2021-08-17 09:56:00.000000 slack_sdk-3.9.1/slack_sdk/http_retry/builtin_async_handlers.py
+-rw-r--r--   0 ksera      (502) staff       (20)     2914 2021-08-17 09:56:00.000000 slack_sdk-3.9.1/slack_sdk/http_retry/builtin_handlers.py
+-rw-r--r--   0 ksera      (502) staff       (20)     1622 2021-08-07 02:47:20.000000 slack_sdk-3.9.1/slack_sdk/http_retry/builtin_interval_calculators.py
+-rw-r--r--   0 ksera      (502) staff       (20)     2487 2021-08-17 09:17:01.000000 slack_sdk-3.9.1/slack_sdk/http_retry/handler.py
+-rw-r--r--   0 ksera      (502) staff       (20)      450 2021-08-07 02:47:20.000000 slack_sdk-3.9.1/slack_sdk/http_retry/interval_calculator.py
+-rw-r--r--   0 ksera      (502) staff       (20)      597 2021-08-07 02:47:20.000000 slack_sdk-3.9.1/slack_sdk/http_retry/jitter.py
+-rw-r--r--   0 ksera      (502) staff       (20)     1087 2021-08-07 02:47:20.000000 slack_sdk-3.9.1/slack_sdk/http_retry/request.py
+-rw-r--r--   0 ksera      (502) staff       (20)      661 2021-08-17 09:56:00.000000 slack_sdk-3.9.1/slack_sdk/http_retry/response.py
+-rw-r--r--   0 ksera      (502) staff       (20)      570 2021-08-07 02:47:20.000000 slack_sdk-3.9.1/slack_sdk/http_retry/state.py
+drwxr-xr-x   0 ksera      (502) staff       (20)        0 2021-08-17 11:04:21.484931 slack_sdk-3.9.1/slack_sdk/models/
+-rw-r--r--   0 ksera      (502) staff       (20)     1918 2021-05-07 21:39:57.000000 slack_sdk-3.9.1/slack_sdk/models/__init__.py
+drwxr-xr-x   0 ksera      (502) staff       (20)        0 2021-08-17 11:04:21.486380 slack_sdk-3.9.1/slack_sdk/models/attachments/
+-rw-r--r--   0 ksera      (502) staff       (20)    24573 2021-05-07 21:39:57.000000 slack_sdk-3.9.1/slack_sdk/models/attachments/__init__.py
+-rw-r--r--   0 ksera      (502) staff       (20)     3847 2021-05-07 21:39:57.000000 slack_sdk-3.9.1/slack_sdk/models/basic_objects.py
+drwxr-xr-x   0 ksera      (502) staff       (20)        0 2021-08-17 11:04:21.492463 slack_sdk-3.9.1/slack_sdk/models/blocks/
+-rw-r--r--   0 ksera      (502) staff       (20)     2419 2021-05-20 23:17:44.000000 slack_sdk-3.9.1/slack_sdk/models/blocks/__init__.py
+-rw-r--r--   0 ksera      (502) staff       (20)    19745 2021-05-07 21:39:57.000000 slack_sdk-3.9.1/slack_sdk/models/blocks/basic_components.py
+-rw-r--r--   0 ksera      (502) staff       (20)    40588 2021-06-14 21:14:05.000000 slack_sdk-3.9.1/slack_sdk/models/blocks/block_elements.py
+-rw-r--r--   0 ksera      (502) staff       (20)    14144 2021-05-07 21:39:57.000000 slack_sdk-3.9.1/slack_sdk/models/blocks/blocks.py
+-rw-r--r--   0 ksera      (502) staff       (20)      810 2021-05-07 21:39:57.000000 slack_sdk-3.9.1/slack_sdk/models/dialoags.py
+drwxr-xr-x   0 ksera      (502) staff       (20)        0 2021-08-17 11:04:21.493544 slack_sdk-3.9.1/slack_sdk/models/dialogs/
+-rw-r--r--   0 ksera      (502) staff       (20)    32390 2021-05-07 21:39:57.000000 slack_sdk-3.9.1/slack_sdk/models/dialogs/__init__.py
+drwxr-xr-x   0 ksera      (502) staff       (20)        0 2021-08-17 11:04:21.495975 slack_sdk-3.9.1/slack_sdk/models/messages/
+-rw-r--r--   0 ksera      (502) staff       (20)     2736 2020-10-27 05:09:55.000000 slack_sdk-3.9.1/slack_sdk/models/messages/__init__.py
+-rw-r--r--   0 ksera      (502) staff       (20)     3039 2021-05-07 21:39:57.000000 slack_sdk-3.9.1/slack_sdk/models/messages/message.py
+drwxr-xr-x   0 ksera      (502) staff       (20)        0 2021-08-17 11:04:21.497106 slack_sdk-3.9.1/slack_sdk/models/views/
+-rw-r--r--   0 ksera      (502) staff       (20)     9017 2021-05-28 11:02:50.000000 slack_sdk-3.9.1/slack_sdk/models/views/__init__.py
+drwxr-xr-x   0 ksera      (502) staff       (20)        0 2021-08-17 11:04:21.498984 slack_sdk-3.9.1/slack_sdk/oauth/
+-rw-r--r--   0 ksera      (502) staff       (20)      471 2021-08-01 22:11:58.000000 slack_sdk-3.9.1/slack_sdk/oauth/__init__.py
+drwxr-xr-x   0 ksera      (502) staff       (20)        0 2021-08-17 11:04:21.500269 slack_sdk-3.9.1/slack_sdk/oauth/authorize_url_generator/
+-rw-r--r--   0 ksera      (502) staff       (20)     2029 2021-08-02 12:24:16.000000 slack_sdk-3.9.1/slack_sdk/oauth/authorize_url_generator/__init__.py
+drwxr-xr-x   0 ksera      (502) staff       (20)        0 2021-08-17 11:04:21.506710 slack_sdk-3.9.1/slack_sdk/oauth/installation_store/
+-rw-r--r--   0 ksera      (502) staff       (20)      152 2020-10-27 05:09:55.000000 slack_sdk-3.9.1/slack_sdk/oauth/installation_store/__init__.py
+drwxr-xr-x   0 ksera      (502) staff       (20)        0 2021-08-17 11:04:21.507539 slack_sdk-3.9.1/slack_sdk/oauth/installation_store/amazon_s3/
+-rw-r--r--   0 ksera      (502) staff       (20)    12499 2021-08-07 02:47:20.000000 slack_sdk-3.9.1/slack_sdk/oauth/installation_store/amazon_s3/__init__.py
+-rw-r--r--   0 ksera      (502) staff       (20)     4751 2021-07-15 07:11:53.000000 slack_sdk-3.9.1/slack_sdk/oauth/installation_store/async_cacheable_installation_store.py
+-rw-r--r--   0 ksera      (502) staff       (20)     2995 2021-07-15 07:11:53.000000 slack_sdk-3.9.1/slack_sdk/oauth/installation_store/async_installation_store.py
+-rw-r--r--   0 ksera      (502) staff       (20)     4546 2021-07-15 07:11:53.000000 slack_sdk-3.9.1/slack_sdk/oauth/installation_store/cacheable_installation_store.py
+drwxr-xr-x   0 ksera      (502) staff       (20)        0 2021-08-17 11:04:21.508344 slack_sdk-3.9.1/slack_sdk/oauth/installation_store/file/
+-rw-r--r--   0 ksera      (502) staff       (20)     8142 2021-07-15 07:11:53.000000 slack_sdk-3.9.1/slack_sdk/oauth/installation_store/file/__init__.py
+-rw-r--r--   0 ksera      (502) staff       (20)     2891 2021-07-15 07:11:53.000000 slack_sdk-3.9.1/slack_sdk/oauth/installation_store/installation_store.py
+-rw-r--r--   0 ksera      (502) staff       (20)      934 2021-07-15 07:11:53.000000 slack_sdk-3.9.1/slack_sdk/oauth/installation_store/internals.py
+drwxr-xr-x   0 ksera      (502) staff       (20)        0 2021-08-17 11:04:21.510698 slack_sdk-3.9.1/slack_sdk/oauth/installation_store/models/
+-rw-r--r--   0 ksera      (502) staff       (20)       76 2020-10-27 05:09:55.000000 slack_sdk-3.9.1/slack_sdk/oauth/installation_store/models/__init__.py
+-rw-r--r--   0 ksera      (502) staff       (20)     5010 2021-07-15 07:11:53.000000 slack_sdk-3.9.1/slack_sdk/oauth/installation_store/models/bot.py
+-rw-r--r--   0 ksera      (502) staff       (20)     9602 2021-07-15 07:11:53.000000 slack_sdk-3.9.1/slack_sdk/oauth/installation_store/models/installation.py
+drwxr-xr-x   0 ksera      (502) staff       (20)        0 2021-08-17 11:04:21.511468 slack_sdk-3.9.1/slack_sdk/oauth/installation_store/sqlalchemy/
+-rw-r--r--   0 ksera      (502) staff       (20)    13051 2021-07-30 07:12:34.000000 slack_sdk-3.9.1/slack_sdk/oauth/installation_store/sqlalchemy/__init__.py
+drwxr-xr-x   0 ksera      (502) staff       (20)        0 2021-08-17 11:04:21.512729 slack_sdk-3.9.1/slack_sdk/oauth/installation_store/sqlite3/
+-rw-r--r--   0 ksera      (502) staff       (20)    20886 2021-07-15 07:11:53.000000 slack_sdk-3.9.1/slack_sdk/oauth/installation_store/sqlite3/__init__.py
+drwxr-xr-x   0 ksera      (502) staff       (20)        0 2021-08-17 11:04:21.513822 slack_sdk-3.9.1/slack_sdk/oauth/redirect_uri_page_renderer/
+-rw-r--r--   0 ksera      (502) staff       (20)     1991 2021-05-07 21:39:57.000000 slack_sdk-3.9.1/slack_sdk/oauth/redirect_uri_page_renderer/__init__.py
+drwxr-xr-x   0 ksera      (502) staff       (20)        0 2021-08-17 11:04:21.517707 slack_sdk-3.9.1/slack_sdk/oauth/state_store/
+-rw-r--r--   0 ksera      (502) staff       (20)      261 2021-05-07 21:39:57.000000 slack_sdk-3.9.1/slack_sdk/oauth/state_store/__init__.py
+drwxr-xr-x   0 ksera      (502) staff       (20)        0 2021-08-17 11:04:21.519044 slack_sdk-3.9.1/slack_sdk/oauth/state_store/amazon_s3/
+-rw-r--r--   0 ksera      (502) staff       (20)     2248 2021-05-07 21:39:57.000000 slack_sdk-3.9.1/slack_sdk/oauth/state_store/amazon_s3/__init__.py
+-rw-r--r--   0 ksera      (502) staff       (20)      325 2020-11-07 14:22:06.000000 slack_sdk-3.9.1/slack_sdk/oauth/state_store/async_state_store.py
+drwxr-xr-x   0 ksera      (502) staff       (20)        0 2021-08-17 11:04:21.519897 slack_sdk-3.9.1/slack_sdk/oauth/state_store/file/
+-rw-r--r--   0 ksera      (502) staff       (20)     2220 2020-11-07 14:22:06.000000 slack_sdk-3.9.1/slack_sdk/oauth/state_store/file/__init__.py
+drwxr-xr-x   0 ksera      (502) staff       (20)        0 2021-08-17 11:04:21.520773 slack_sdk-3.9.1/slack_sdk/oauth/state_store/sqlalchemy/
+-rw-r--r--   0 ksera      (502) staff       (20)     2630 2021-06-18 05:18:34.000000 slack_sdk-3.9.1/slack_sdk/oauth/state_store/sqlalchemy/__init__.py
+drwxr-xr-x   0 ksera      (502) staff       (20)        0 2021-08-17 11:04:21.522011 slack_sdk-3.9.1/slack_sdk/oauth/state_store/sqlite3/
+-rw-r--r--   0 ksera      (502) staff       (20)     3503 2020-11-07 14:22:06.000000 slack_sdk-3.9.1/slack_sdk/oauth/state_store/sqlite3/__init__.py
+-rw-r--r--   0 ksera      (502) staff       (20)      296 2020-11-07 14:03:53.000000 slack_sdk-3.9.1/slack_sdk/oauth/state_store/state_store.py
+drwxr-xr-x   0 ksera      (502) staff       (20)        0 2021-08-17 11:04:21.522996 slack_sdk-3.9.1/slack_sdk/oauth/state_utils/
+-rw-r--r--   0 ksera      (502) staff       (20)     1656 2020-11-06 22:42:40.000000 slack_sdk-3.9.1/slack_sdk/oauth/state_utils/__init__.py
+drwxr-xr-x   0 ksera      (502) staff       (20)        0 2021-08-17 11:04:21.527222 slack_sdk-3.9.1/slack_sdk/oauth/token_rotation/
+-rw-r--r--   0 ksera      (502) staff       (20)       42 2021-07-15 07:11:53.000000 slack_sdk-3.9.1/slack_sdk/oauth/token_rotation/__init__.py
+-rw-r--r--   0 ksera      (502) staff       (20)     5329 2021-07-15 07:11:53.000000 slack_sdk-3.9.1/slack_sdk/oauth/token_rotation/async_rotator.py
+-rw-r--r--   0 ksera      (502) staff       (20)     5159 2021-07-15 07:11:53.000000 slack_sdk-3.9.1/slack_sdk/oauth/token_rotation/rotator.py
+-rw-r--r--   0 ksera      (502) staff       (20)      843 2021-08-17 04:44:13.000000 slack_sdk-3.9.1/slack_sdk/proxy_env_variable_loader.py
+-rw-r--r--   0 ksera      (502) staff       (20)        0 2020-10-27 05:09:55.000000 slack_sdk-3.9.1/slack_sdk/py.typed
+drwxr-xr-x   0 ksera      (502) staff       (20)        0 2021-08-17 11:04:21.528087 slack_sdk-3.9.1/slack_sdk/rtm/
+-rw-r--r--   0 ksera      (502) staff       (20)    24014 2021-05-07 21:39:57.000000 slack_sdk-3.9.1/slack_sdk/rtm/__init__.py
+drwxr-xr-x   0 ksera      (502) staff       (20)        0 2021-08-17 11:04:21.529430 slack_sdk-3.9.1/slack_sdk/rtm/v2/
+-rw-r--r--   0 ksera      (502) staff       (20)       47 2021-05-07 21:39:57.000000 slack_sdk-3.9.1/slack_sdk/rtm/v2/__init__.py
+drwxr-xr-x   0 ksera      (502) staff       (20)        0 2021-08-17 11:04:21.530663 slack_sdk-3.9.1/slack_sdk/rtm_v2/
+-rw-r--r--   0 ksera      (502) staff       (20)    16519 2021-05-07 21:39:57.000000 slack_sdk-3.9.1/slack_sdk/rtm_v2/__init__.py
+drwxr-xr-x   0 ksera      (502) staff       (20)        0 2021-08-17 11:04:21.534260 slack_sdk-3.9.1/slack_sdk/scim/
+-rw-r--r--   0 ksera      (502) staff       (20)      585 2021-05-07 21:39:57.000000 slack_sdk-3.9.1/slack_sdk/scim/__init__.py
+-rw-r--r--   0 ksera      (502) staff       (20)       53 2021-05-07 21:39:57.000000 slack_sdk-3.9.1/slack_sdk/scim/async_client.py
+drwxr-xr-x   0 ksera      (502) staff       (20)        0 2021-08-17 11:04:21.548954 slack_sdk-3.9.1/slack_sdk/scim/v1/
+-rw-r--r--   0 ksera      (502) staff       (20)      283 2021-05-07 21:39:57.000000 slack_sdk-3.9.1/slack_sdk/scim/v1/__init__.py
+-rw-r--r--   0 ksera      (502) staff       (20)    15318 2021-08-13 12:59:33.000000 slack_sdk-3.9.1/slack_sdk/scim/v1/async_client.py
+-rw-r--r--   0 ksera      (502) staff       (20)    15722 2021-08-13 12:59:33.000000 slack_sdk-3.9.1/slack_sdk/scim/v1/client.py
+-rw-r--r--   0 ksera      (502) staff       (20)       53 2021-05-07 21:39:57.000000 slack_sdk-3.9.1/slack_sdk/scim/v1/default_arg.py
+-rw-r--r--   0 ksera      (502) staff       (20)     2522 2021-05-07 21:39:57.000000 slack_sdk-3.9.1/slack_sdk/scim/v1/group.py
+-rw-r--r--   0 ksera      (502) staff       (20)     5068 2021-05-07 21:39:57.000000 slack_sdk-3.9.1/slack_sdk/scim/v1/internal_utils.py
+-rw-r--r--   0 ksera      (502) staff       (20)     7575 2021-05-07 21:39:57.000000 slack_sdk-3.9.1/slack_sdk/scim/v1/response.py
+-rw-r--r--   0 ksera      (502) staff       (20)      798 2021-05-07 21:39:57.000000 slack_sdk-3.9.1/slack_sdk/scim/v1/types.py
+-rw-r--r--   0 ksera      (502) staff       (20)     8062 2021-05-07 21:39:57.000000 slack_sdk-3.9.1/slack_sdk/scim/v1/user.py
+drwxr-xr-x   0 ksera      (502) staff       (20)        0 2021-08-17 11:04:21.550553 slack_sdk-3.9.1/slack_sdk/signature/
+-rw-r--r--   0 ksera      (502) staff       (20)     2419 2021-05-07 21:39:57.000000 slack_sdk-3.9.1/slack_sdk/signature/__init__.py
+drwxr-xr-x   0 ksera      (502) staff       (20)        0 2021-08-17 11:04:21.564146 slack_sdk-3.9.1/slack_sdk/socket_mode/
+-rw-r--r--   0 ksera      (502) staff       (20)      327 2021-05-07 21:39:57.000000 slack_sdk-3.9.1/slack_sdk/socket_mode/__init__.py
+drwxr-xr-x   0 ksera      (502) staff       (20)        0 2021-08-17 11:04:21.565609 slack_sdk-3.9.1/slack_sdk/socket_mode/aiohttp/
+-rw-r--r--   0 ksera      (502) staff       (20)     9811 2021-07-29 08:18:46.000000 slack_sdk-3.9.1/slack_sdk/socket_mode/aiohttp/__init__.py
+-rw-r--r--   0 ksera      (502) staff       (20)     5690 2021-07-29 08:18:46.000000 slack_sdk-3.9.1/slack_sdk/socket_mode/async_client.py
+-rw-r--r--   0 ksera      (502) staff       (20)      580 2021-05-07 21:39:57.000000 slack_sdk-3.9.1/slack_sdk/socket_mode/async_listeners.py
+drwxr-xr-x   0 ksera      (502) staff       (20)        0 2021-08-17 11:04:21.573804 slack_sdk-3.9.1/slack_sdk/socket_mode/builtin/
+-rw-r--r--   0 ksera      (502) staff       (20)       45 2021-05-07 21:39:57.000000 slack_sdk-3.9.1/slack_sdk/socket_mode/builtin/__init__.py
+-rw-r--r--   0 ksera      (502) staff       (20)    11251 2021-05-07 21:39:57.000000 slack_sdk-3.9.1/slack_sdk/socket_mode/builtin/client.py
+-rw-r--r--   0 ksera      (502) staff       (20)    19753 2021-05-07 21:39:57.000000 slack_sdk-3.9.1/slack_sdk/socket_mode/builtin/connection.py
+-rw-r--r--   0 ksera      (502) staff       (20)     1066 2021-05-07 21:39:57.000000 slack_sdk-3.9.1/slack_sdk/socket_mode/builtin/frame_header.py
+-rw-r--r--   0 ksera      (502) staff       (20)    14132 2021-08-13 08:49:31.000000 slack_sdk-3.9.1/slack_sdk/socket_mode/builtin/internals.py
+-rw-r--r--   0 ksera      (502) staff       (20)     6175 2021-05-07 21:39:57.000000 slack_sdk-3.9.1/slack_sdk/socket_mode/client.py
+-rw-r--r--   0 ksera      (502) staff       (20)      914 2021-06-14 21:14:05.000000 slack_sdk-3.9.1/slack_sdk/socket_mode/interval_runner.py
+-rw-r--r--   0 ksera      (502) staff       (20)      509 2021-05-07 21:39:57.000000 slack_sdk-3.9.1/slack_sdk/socket_mode/listeners.py
+-rw-r--r--   0 ksera      (502) staff       (20)     1929 2021-05-07 21:39:57.000000 slack_sdk-3.9.1/slack_sdk/socket_mode/request.py
+-rw-r--r--   0 ksera      (502) staff       (20)      894 2021-05-07 21:39:57.000000 slack_sdk-3.9.1/slack_sdk/socket_mode/response.py
+drwxr-xr-x   0 ksera      (502) staff       (20)        0 2021-08-17 11:04:21.575481 slack_sdk-3.9.1/slack_sdk/socket_mode/websocket_client/
+-rw-r--r--   0 ksera      (502) staff       (20)     9574 2021-05-28 21:12:15.000000 slack_sdk-3.9.1/slack_sdk/socket_mode/websocket_client/__init__.py
+drwxr-xr-x   0 ksera      (502) staff       (20)        0 2021-08-17 11:04:21.577350 slack_sdk-3.9.1/slack_sdk/socket_mode/websockets/
+-rw-r--r--   0 ksera      (502) staff       (20)     6740 2021-07-29 08:18:46.000000 slack_sdk-3.9.1/slack_sdk/socket_mode/websockets/__init__.py
+-rw-r--r--   0 ksera      (502) staff       (20)       92 2021-08-17 09:56:08.000000 slack_sdk-3.9.1/slack_sdk/version.py
+drwxr-xr-x   0 ksera      (502) staff       (20)        0 2021-08-17 11:04:21.601191 slack_sdk-3.9.1/slack_sdk/web/
+-rw-r--r--   0 ksera      (502) staff       (20)      240 2021-05-07 21:39:57.000000 slack_sdk-3.9.1/slack_sdk/web/__init__.py
+-rw-r--r--   0 ksera      (502) staff       (20)     7195 2021-08-13 12:59:33.000000 slack_sdk-3.9.1/slack_sdk/web/async_base_client.py
+-rw-r--r--   0 ksera      (502) staff       (20)   115237 2021-08-17 09:56:21.000000 slack_sdk-3.9.1/slack_sdk/web/async_client.py
+-rw-r--r--   0 ksera      (502) staff       (20)     8572 2021-08-17 09:56:00.000000 slack_sdk-3.9.1/slack_sdk/web/async_internal_utils.py
+-rw-r--r--   0 ksera      (502) staff       (20)     6889 2021-05-07 21:39:57.000000 slack_sdk-3.9.1/slack_sdk/web/async_slack_response.py
+-rw-r--r--   0 ksera      (502) staff       (20)    24373 2021-08-17 09:56:00.000000 slack_sdk-3.9.1/slack_sdk/web/base_client.py
+-rw-r--r--   0 ksera      (502) staff       (20)   109719 2021-08-13 08:49:31.000000 slack_sdk-3.9.1/slack_sdk/web/client.py
+-rw-r--r--   0 ksera      (502) staff       (20)     1018 2020-10-27 05:09:55.000000 slack_sdk-3.9.1/slack_sdk/web/deprecation.py
+-rw-r--r--   0 ksera      (502) staff       (20)     9361 2021-07-15 07:11:53.000000 slack_sdk-3.9.1/slack_sdk/web/internal_utils.py
+-rw-r--r--   0 ksera      (502) staff       (20)    23155 2021-05-07 21:39:57.000000 slack_sdk-3.9.1/slack_sdk/web/legacy_base_client.py
+-rw-r--r--   0 ksera      (502) staff       (20)   114522 2021-08-17 09:56:21.000000 slack_sdk-3.9.1/slack_sdk/web/legacy_client.py
+-rw-r--r--   0 ksera      (502) staff       (20)     7903 2021-01-29 07:26:58.000000 slack_sdk-3.9.1/slack_sdk/web/legacy_slack_response.py
+-rw-r--r--   0 ksera      (502) staff       (20)     6398 2021-08-17 09:56:00.000000 slack_sdk-3.9.1/slack_sdk/web/slack_response.py
+drwxr-xr-x   0 ksera      (502) staff       (20)        0 2021-08-17 11:04:21.609244 slack_sdk-3.9.1/slack_sdk/webhook/
+-rw-r--r--   0 ksera      (502) staff       (20)      278 2021-05-07 21:39:57.000000 slack_sdk-3.9.1/slack_sdk/webhook/__init__.py
+-rw-r--r--   0 ksera      (502) staff       (20)    11585 2021-08-13 12:59:33.000000 slack_sdk-3.9.1/slack_sdk/webhook/async_client.py
+-rw-r--r--   0 ksera      (502) staff       (20)    11851 2021-08-13 12:59:33.000000 slack_sdk-3.9.1/slack_sdk/webhook/client.py
+-rw-r--r--   0 ksera      (502) staff       (20)     1351 2021-06-30 09:54:45.000000 slack_sdk-3.9.1/slack_sdk/webhook/internal_utils.py
+-rw-r--r--   0 ksera      (502) staff       (20)      281 2021-05-07 21:39:57.000000 slack_sdk-3.9.1/slack_sdk/webhook/webhook_response.py
+drwxr-xr-x   0 ksera      (502) staff       (20)        0 2021-08-17 11:04:21.460019 slack_sdk-3.9.1/slack_sdk.egg-info/
+-rw-r--r--   0 ksera      (502) staff       (20)    16140 2021-08-17 11:04:21.000000 slack_sdk-3.9.1/slack_sdk.egg-info/PKG-INFO
+-rw-r--r--   0 ksera      (502) staff       (20)     5502 2021-08-17 11:04:21.000000 slack_sdk-3.9.1/slack_sdk.egg-info/SOURCES.txt
+-rw-r--r--   0 ksera      (502) staff       (20)        1 2021-08-17 11:04:21.000000 slack_sdk-3.9.1/slack_sdk.egg-info/dependency_links.txt
+-rw-r--r--   0 ksera      (502) staff       (20)      300 2021-08-17 11:04:21.000000 slack_sdk-3.9.1/slack_sdk.egg-info/requires.txt
+-rw-r--r--   0 ksera      (502) staff       (20)       16 2021-08-17 11:04:21.000000 slack_sdk-3.9.1/slack_sdk.egg-info/top_level.txt
```

### Comparing `slack_sdk-3.9.0rc2/LICENSE` & `slack_sdk-3.9.1/LICENSE`

 * *Files identical despite different names*

### Comparing `slack_sdk-3.9.0rc2/PKG-INFO` & `slack_sdk-3.9.1/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: slack_sdk
-Version: 3.9.0rc2
+Version: 3.9.1
 Summary: The Slack API Platform SDK for Python
 Home-page: https://github.com/slackapi/python-slack-sdk
 Author: Slack Technologies, Inc.
 Author-email: opensource@slack.com
 License: MIT
 Description: # Python Slack SDK
```

### Comparing `slack_sdk-3.9.0rc2/README.md` & `slack_sdk-3.9.1/README.md`

 * *Files identical despite different names*

### Comparing `slack_sdk-3.9.0rc2/setup.py` & `slack_sdk-3.9.1/setup.py`

 * *Files identical despite different names*

### Comparing `slack_sdk-3.9.0rc2/slack/__init__.py` & `slack_sdk-3.9.1/slack/__init__.py`

 * *Files identical despite different names*

### Comparing `slack_sdk-3.9.0rc2/slack/signature/verifier.py` & `slack_sdk-3.9.1/slack/signature/verifier.py`

 * *Files identical despite different names*

### Comparing `slack_sdk-3.9.0rc2/slack/web/__init__.py` & `slack_sdk-3.9.1/slack/web/__init__.py`

 * *Files identical despite different names*

### Comparing `slack_sdk-3.9.0rc2/slack/web/async_base_client.py` & `slack_sdk-3.9.1/slack/web/async_base_client.py`

 * *Files identical despite different names*

### Comparing `slack_sdk-3.9.0rc2/slack/web/async_client.py` & `slack_sdk-3.9.1/slack/web/async_client.py`

 * *Files identical despite different names*

### Comparing `slack_sdk-3.9.0rc2/slack/web/async_internal_utils.py` & `slack_sdk-3.9.1/slack/web/async_internal_utils.py`

 * *Files identical despite different names*

### Comparing `slack_sdk-3.9.0rc2/slack/web/async_slack_response.py` & `slack_sdk-3.9.1/slack/web/async_slack_response.py`

 * *Files identical despite different names*

### Comparing `slack_sdk-3.9.0rc2/slack/web/base_client.py` & `slack_sdk-3.9.1/slack/web/base_client.py`

 * *Files identical despite different names*

### Comparing `slack_sdk-3.9.0rc2/slack/web/classes/actions.py` & `slack_sdk-3.9.1/slack/web/classes/actions.py`

 * *Files identical despite different names*

### Comparing `slack_sdk-3.9.0rc2/slack/web/classes/blocks.py` & `slack_sdk-3.9.1/slack/web/classes/blocks.py`

 * *Files identical despite different names*

### Comparing `slack_sdk-3.9.0rc2/slack/web/classes/dialog_elements.py` & `slack_sdk-3.9.1/slack/web/classes/dialog_elements.py`

 * *Files identical despite different names*

### Comparing `slack_sdk-3.9.0rc2/slack/web/classes/elements.py` & `slack_sdk-3.9.1/slack/web/classes/elements.py`

 * *Files identical despite different names*

### Comparing `slack_sdk-3.9.0rc2/slack/web/classes/interactions.py` & `slack_sdk-3.9.1/slack/web/classes/interactions.py`

 * *Files identical despite different names*

### Comparing `slack_sdk-3.9.0rc2/slack/web/classes/objects.py` & `slack_sdk-3.9.1/slack/web/classes/objects.py`

 * *Files identical despite different names*

### Comparing `slack_sdk-3.9.0rc2/slack/web/deprecation.py` & `slack_sdk-3.9.1/slack/web/deprecation.py`

 * *Files identical despite different names*

### Comparing `slack_sdk-3.9.0rc2/slack/web/internal_utils.py` & `slack_sdk-3.9.1/slack/web/internal_utils.py`

 * *Files identical despite different names*

### Comparing `slack_sdk-3.9.0rc2/slack/webhook/async_client.py` & `slack_sdk-3.9.1/slack/webhook/async_client.py`

 * *Files identical despite different names*

### Comparing `slack_sdk-3.9.0rc2/slack/webhook/client.py` & `slack_sdk-3.9.1/slack/webhook/client.py`

 * *Files identical despite different names*

### Comparing `slack_sdk-3.9.0rc2/slack/webhook/internal_utils.py` & `slack_sdk-3.9.1/slack/webhook/internal_utils.py`

 * *Files identical despite different names*

### Comparing `slack_sdk-3.9.0rc2/slack_sdk/__init__.py` & `slack_sdk-3.9.1/slack_sdk/__init__.py`

 * *Files identical despite different names*

### Comparing `slack_sdk-3.9.0rc2/slack_sdk/aiohttp_version_checker.py` & `slack_sdk-3.9.1/slack_sdk/aiohttp_version_checker.py`

 * *Files identical despite different names*

### Comparing `slack_sdk-3.9.0rc2/slack_sdk/audit_logs/v1/async_client.py` & `slack_sdk-3.9.1/slack_sdk/audit_logs/v1/async_client.py`

 * *Files 2% similar despite different names*

```diff
@@ -51,15 +51,15 @@
         session: Optional[ClientSession] = None,
         trust_env_in_session: bool = False,
         auth: Optional[BasicAuth] = None,
         default_headers: Optional[Dict[str, str]] = None,
         user_agent_prefix: Optional[str] = None,
         user_agent_suffix: Optional[str] = None,
         logger: Optional[logging.Logger] = None,
-        retry_handlers: List[AsyncRetryHandler] = async_default_handlers,
+        retry_handlers: Optional[List[AsyncRetryHandler]] = None,
     ):
         """API client for Audit Logs API
         See https://api.slack.com/admins/audit-logs for more details
 
         Args:
             token: An admin user's token, which starts with `xoxp-`
             timeout: Request timeout (in seconds)
@@ -84,15 +84,17 @@
         self.trust_env_in_session = trust_env_in_session
         self.auth = auth
         self.default_headers = default_headers if default_headers else {}
         self.default_headers["User-Agent"] = get_user_agent(
             user_agent_prefix, user_agent_suffix
         )
         self.logger = logger if logger is not None else logging.getLogger(__name__)
-        self.retry_handlers = retry_handlers
+        self.retry_handlers = (
+            retry_handlers if retry_handlers is not None else async_default_handlers()
+        )
 
         if self.proxy is None or len(self.proxy.strip()) == 0:
             env_variable = load_http_proxy_from_env(self.logger)
             if env_variable is not None:
                 self.proxy = env_variable
 
     async def schemas(
```

### Comparing `slack_sdk-3.9.0rc2/slack_sdk/audit_logs/v1/client.py` & `slack_sdk-3.9.1/slack_sdk/audit_logs/v1/client.py`

 * *Files 1% similar despite different names*

```diff
@@ -46,15 +46,15 @@
         ssl: Optional[SSLContext] = None,
         proxy: Optional[str] = None,
         base_url: str = BASE_URL,
         default_headers: Optional[Dict[str, str]] = None,
         user_agent_prefix: Optional[str] = None,
         user_agent_suffix: Optional[str] = None,
         logger: Optional[logging.Logger] = None,
-        retry_handlers: List[RetryHandler] = default_retry_handlers,
+        retry_handlers: Optional[List[RetryHandler]] = None,
     ):
         """API client for Audit Logs API
         See https://api.slack.com/admins/audit-logs for more details
 
         Args:
             token: An admin user's token, which starts with `xoxp-`
             timeout: Request timeout (in seconds)
@@ -73,15 +73,17 @@
         self.proxy = proxy
         self.base_url = base_url
         self.default_headers = default_headers if default_headers else {}
         self.default_headers["User-Agent"] = get_user_agent(
             user_agent_prefix, user_agent_suffix
         )
         self.logger = logger if logger is not None else logging.getLogger(__name__)
-        self.retry_handlers = retry_handlers
+        self.retry_handlers = (
+            retry_handlers if retry_handlers is not None else default_retry_handlers()
+        )
 
         if self.proxy is None or len(self.proxy.strip()) == 0:
             env_variable = load_http_proxy_from_env(self.logger)
             if env_variable is not None:
                 self.proxy = env_variable
 
     def schemas(
```

### Comparing `slack_sdk-3.9.0rc2/slack_sdk/audit_logs/v1/internal_utils.py` & `slack_sdk-3.9.1/slack_sdk/audit_logs/v1/internal_utils.py`

 * *Files identical despite different names*

### Comparing `slack_sdk-3.9.0rc2/slack_sdk/audit_logs/v1/logs.py` & `slack_sdk-3.9.1/slack_sdk/audit_logs/v1/logs.py`

 * *Files identical despite different names*

### Comparing `slack_sdk-3.9.0rc2/slack_sdk/audit_logs/v1/response.py` & `slack_sdk-3.9.1/slack_sdk/audit_logs/v1/response.py`

 * *Files identical despite different names*

### Comparing `slack_sdk-3.9.0rc2/slack_sdk/errors/__init__.py` & `slack_sdk-3.9.1/slack_sdk/errors/__init__.py`

 * *Files identical despite different names*

### Comparing `slack_sdk-3.9.0rc2/slack_sdk/http_retry/async_handler.py` & `slack_sdk-3.9.1/slack_sdk/http_retry/async_handler.py`

 * *Files identical despite different names*

### Comparing `slack_sdk-3.9.0rc2/slack_sdk/http_retry/builtin_async_handlers.py` & `slack_sdk-3.9.1/slack_sdk/http_retry/builtin_async_handlers.py`

 * *Files 2% similar despite different names*

```diff
@@ -66,25 +66,27 @@
         request: HttpRequest,
         response: Optional[HttpResponse] = None,
         error: Optional[Exception] = None,
     ) -> None:
         if response is None:
             raise error
 
-        state.increment_current_attempt()
+        state.next_attempt_requested = True
         retry_after_header_name: Optional[str] = None
         for k in response.headers.keys():
             if k.lower() == "retry-after":
                 retry_after_header_name = k
                 break
         duration = 1
         if retry_after_header_name is None:
             # This situation usually does not arise. Just in case.
             duration += random.random()
         else:
             duration = (
                 int(response.headers.get(retry_after_header_name)[0]) + random.random()
             )
         await asyncio.sleep(duration)
+        state.increment_current_attempt()
 
 
-async_default_handlers = [AsyncConnectionErrorRetryHandler()]
+def async_default_handlers() -> List[AsyncRetryHandler]:
+    return [AsyncConnectionErrorRetryHandler()]
```

### Comparing `slack_sdk-3.9.0rc2/slack_sdk/http_retry/builtin_handlers.py` & `slack_sdk-3.9.1/slack_sdk/http_retry/builtin_handlers.py`

 * *Files 6% similar despite different names*

```diff
@@ -35,14 +35,18 @@
         request: HttpRequest,
         response: Optional[HttpResponse] = None,
         error: Optional[Exception] = None,
     ) -> bool:
         if error is None:
             return False
 
+        if isinstance(error, URLError):
+            if response is not None:
+                return False  # status 40x
+
         for error_type in self.error_types_to_do_retries:
             if isinstance(error, error_type):
                 return True
         return False
 
 
 class RateLimitErrorRetryHandler(RetryHandler):
@@ -52,35 +56,36 @@
         self,
         *,
         state: RetryState,
         request: HttpRequest,
         response: Optional[HttpResponse] = None,
         error: Optional[Exception] = None,
     ) -> bool:
-        return response.status_code == 429
+        return response is not None and response.status_code == 429
 
     def prepare_for_next_attempt(
         self,
         *,
         state: RetryState,
         request: HttpRequest,
         response: Optional[HttpResponse] = None,
         error: Optional[Exception] = None,
     ) -> None:
         if response is None:
             raise error
 
-        state.increment_current_attempt()
+        state.next_attempt_requested = True
         retry_after_header_name: Optional[str] = None
         for k in response.headers.keys():
             if k.lower() == "retry-after":
                 retry_after_header_name = k
                 break
         duration = 1
         if retry_after_header_name is None:
             # This situation usually does not arise. Just in case.
             duration += random.random()
         else:
             duration = (
                 int(response.headers.get(retry_after_header_name)[0]) + random.random()
             )
         time.sleep(duration)
+        state.increment_current_attempt()
```

### Comparing `slack_sdk-3.9.0rc2/slack_sdk/http_retry/builtin_interval_calculators.py` & `slack_sdk-3.9.1/slack_sdk/http_retry/builtin_interval_calculators.py`

 * *Files identical despite different names*

### Comparing `slack_sdk-3.9.0rc2/slack_sdk/http_retry/handler.py` & `slack_sdk-3.9.1/slack_sdk/http_retry/handler.py`

 * *Files identical despite different names*

### Comparing `slack_sdk-3.9.0rc2/slack_sdk/http_retry/jitter.py` & `slack_sdk-3.9.1/slack_sdk/http_retry/jitter.py`

 * *Files identical despite different names*

### Comparing `slack_sdk-3.9.0rc2/slack_sdk/http_retry/request.py` & `slack_sdk-3.9.1/slack_sdk/http_retry/request.py`

 * *Files identical despite different names*

### Comparing `slack_sdk-3.9.0rc2/slack_sdk/http_retry/response.py` & `slack_sdk-3.9.1/slack_sdk/http_retry/response.py`

 * *Files 19% similar despite different names*

```diff
@@ -8,18 +8,18 @@
     headers: Dict[str, List[str]]
     body: Optional[Dict[str, Any]]
     data: Optional[bytes]
 
     def __init__(
         self,
         *,
-        status_code: int,
+        status_code: Union[int, str],
         headers: Dict[str, Union[str, List[str]]],
         body: Optional[Dict[str, Any]] = None,
         data: Optional[bytes] = None,
     ):
-        self.status_code = status_code
+        self.status_code = int(status_code)
         self.headers = {
             k: v if isinstance(v, list) else [v] for k, v in headers.items()
         }
         self.body = body
         self.data = data
```

### Comparing `slack_sdk-3.9.0rc2/slack_sdk/http_retry/state.py` & `slack_sdk-3.9.1/slack_sdk/http_retry/state.py`

 * *Files identical despite different names*

### Comparing `slack_sdk-3.9.0rc2/slack_sdk/models/__init__.py` & `slack_sdk-3.9.1/slack_sdk/models/__init__.py`

 * *Files identical despite different names*

### Comparing `slack_sdk-3.9.0rc2/slack_sdk/models/attachments/__init__.py` & `slack_sdk-3.9.1/slack_sdk/models/attachments/__init__.py`

 * *Files identical despite different names*

### Comparing `slack_sdk-3.9.0rc2/slack_sdk/models/basic_objects.py` & `slack_sdk-3.9.1/slack_sdk/models/basic_objects.py`

 * *Files identical despite different names*

### Comparing `slack_sdk-3.9.0rc2/slack_sdk/models/blocks/__init__.py` & `slack_sdk-3.9.1/slack_sdk/models/blocks/__init__.py`

 * *Files identical despite different names*

### Comparing `slack_sdk-3.9.0rc2/slack_sdk/models/blocks/basic_components.py` & `slack_sdk-3.9.1/slack_sdk/models/blocks/basic_components.py`

 * *Files identical despite different names*

### Comparing `slack_sdk-3.9.0rc2/slack_sdk/models/blocks/block_elements.py` & `slack_sdk-3.9.1/slack_sdk/models/blocks/block_elements.py`

 * *Files identical despite different names*

### Comparing `slack_sdk-3.9.0rc2/slack_sdk/models/blocks/blocks.py` & `slack_sdk-3.9.1/slack_sdk/models/blocks/blocks.py`

 * *Files identical despite different names*

### Comparing `slack_sdk-3.9.0rc2/slack_sdk/models/dialoags.py` & `slack_sdk-3.9.1/slack_sdk/models/dialoags.py`

 * *Files identical despite different names*

### Comparing `slack_sdk-3.9.0rc2/slack_sdk/models/dialogs/__init__.py` & `slack_sdk-3.9.1/slack_sdk/models/dialogs/__init__.py`

 * *Files identical despite different names*

### Comparing `slack_sdk-3.9.0rc2/slack_sdk/models/messages/__init__.py` & `slack_sdk-3.9.1/slack_sdk/models/messages/__init__.py`

 * *Files identical despite different names*

### Comparing `slack_sdk-3.9.0rc2/slack_sdk/models/messages/message.py` & `slack_sdk-3.9.1/slack_sdk/models/messages/message.py`

 * *Files identical despite different names*

### Comparing `slack_sdk-3.9.0rc2/slack_sdk/models/views/__init__.py` & `slack_sdk-3.9.1/slack_sdk/models/views/__init__.py`

 * *Files identical despite different names*

### Comparing `slack_sdk-3.9.0rc2/slack_sdk/oauth/authorize_url_generator/__init__.py` & `slack_sdk-3.9.1/slack_sdk/oauth/authorize_url_generator/__init__.py`

 * *Files identical despite different names*

### Comparing `slack_sdk-3.9.0rc2/slack_sdk/oauth/installation_store/amazon_s3/__init__.py` & `slack_sdk-3.9.1/slack_sdk/oauth/installation_store/amazon_s3/__init__.py`

 * *Files identical despite different names*

### Comparing `slack_sdk-3.9.0rc2/slack_sdk/oauth/installation_store/async_cacheable_installation_store.py` & `slack_sdk-3.9.1/slack_sdk/oauth/installation_store/async_cacheable_installation_store.py`

 * *Files identical despite different names*

### Comparing `slack_sdk-3.9.0rc2/slack_sdk/oauth/installation_store/async_installation_store.py` & `slack_sdk-3.9.1/slack_sdk/oauth/installation_store/async_installation_store.py`

 * *Files identical despite different names*

### Comparing `slack_sdk-3.9.0rc2/slack_sdk/oauth/installation_store/cacheable_installation_store.py` & `slack_sdk-3.9.1/slack_sdk/oauth/installation_store/cacheable_installation_store.py`

 * *Files identical despite different names*

### Comparing `slack_sdk-3.9.0rc2/slack_sdk/oauth/installation_store/file/__init__.py` & `slack_sdk-3.9.1/slack_sdk/oauth/installation_store/file/__init__.py`

 * *Files identical despite different names*

### Comparing `slack_sdk-3.9.0rc2/slack_sdk/oauth/installation_store/installation_store.py` & `slack_sdk-3.9.1/slack_sdk/oauth/installation_store/installation_store.py`

 * *Files identical despite different names*

### Comparing `slack_sdk-3.9.0rc2/slack_sdk/oauth/installation_store/internals.py` & `slack_sdk-3.9.1/slack_sdk/oauth/installation_store/internals.py`

 * *Files identical despite different names*

### Comparing `slack_sdk-3.9.0rc2/slack_sdk/oauth/installation_store/models/bot.py` & `slack_sdk-3.9.1/slack_sdk/oauth/installation_store/models/bot.py`

 * *Files identical despite different names*

### Comparing `slack_sdk-3.9.0rc2/slack_sdk/oauth/installation_store/models/installation.py` & `slack_sdk-3.9.1/slack_sdk/oauth/installation_store/models/installation.py`

 * *Files identical despite different names*

### Comparing `slack_sdk-3.9.0rc2/slack_sdk/oauth/installation_store/sqlalchemy/__init__.py` & `slack_sdk-3.9.1/slack_sdk/oauth/installation_store/sqlalchemy/__init__.py`

 * *Files identical despite different names*

### Comparing `slack_sdk-3.9.0rc2/slack_sdk/oauth/installation_store/sqlite3/__init__.py` & `slack_sdk-3.9.1/slack_sdk/oauth/installation_store/sqlite3/__init__.py`

 * *Files identical despite different names*

### Comparing `slack_sdk-3.9.0rc2/slack_sdk/oauth/redirect_uri_page_renderer/__init__.py` & `slack_sdk-3.9.1/slack_sdk/oauth/redirect_uri_page_renderer/__init__.py`

 * *Files identical despite different names*

### Comparing `slack_sdk-3.9.0rc2/slack_sdk/oauth/state_store/amazon_s3/__init__.py` & `slack_sdk-3.9.1/slack_sdk/oauth/state_store/amazon_s3/__init__.py`

 * *Files identical despite different names*

### Comparing `slack_sdk-3.9.0rc2/slack_sdk/oauth/state_store/file/__init__.py` & `slack_sdk-3.9.1/slack_sdk/oauth/state_store/file/__init__.py`

 * *Files identical despite different names*

### Comparing `slack_sdk-3.9.0rc2/slack_sdk/oauth/state_store/sqlalchemy/__init__.py` & `slack_sdk-3.9.1/slack_sdk/oauth/state_store/sqlalchemy/__init__.py`

 * *Files identical despite different names*

### Comparing `slack_sdk-3.9.0rc2/slack_sdk/oauth/state_store/sqlite3/__init__.py` & `slack_sdk-3.9.1/slack_sdk/oauth/state_store/sqlite3/__init__.py`

 * *Files identical despite different names*

### Comparing `slack_sdk-3.9.0rc2/slack_sdk/oauth/state_utils/__init__.py` & `slack_sdk-3.9.1/slack_sdk/oauth/state_utils/__init__.py`

 * *Files identical despite different names*

### Comparing `slack_sdk-3.9.0rc2/slack_sdk/oauth/token_rotation/async_rotator.py` & `slack_sdk-3.9.1/slack_sdk/oauth/token_rotation/async_rotator.py`

 * *Files identical despite different names*

### Comparing `slack_sdk-3.9.0rc2/slack_sdk/oauth/token_rotation/rotator.py` & `slack_sdk-3.9.1/slack_sdk/oauth/token_rotation/rotator.py`

 * *Files identical despite different names*

### Comparing `slack_sdk-3.9.0rc2/slack_sdk/proxy_env_variable_loader.py` & `slack_sdk-3.9.1/slack_sdk/proxy_env_variable_loader.py`

 * *Files 27% similar despite different names*

```diff
@@ -9,12 +9,18 @@
 def load_http_proxy_from_env(logger: logging.Logger = _default_logger) -> Optional[str]:
     proxy_url = (
         os.environ.get("HTTPS_PROXY")
         or os.environ.get("https_proxy")
         or os.environ.get("HTTP_PROXY")
         or os.environ.get("http_proxy")
     )
-    if proxy_url is not None:
+    if proxy_url is None:
+        return None
+    if len(proxy_url.strip()) == 0:
+        # If the value is an empty string, the intention should be unsetting it
         logger.debug(
-            f"HTTP proxy URL has been loaded from an env variable: {proxy_url}"
+            "The Slack SDK ignored the proxy env variable as an empty value is set."
         )
+        return None
+
+    logger.debug(f"HTTP proxy URL has been loaded from an env variable: {proxy_url}")
     return proxy_url
```

### Comparing `slack_sdk-3.9.0rc2/slack_sdk/rtm/__init__.py` & `slack_sdk-3.9.1/slack_sdk/rtm/__init__.py`

 * *Files identical despite different names*

### Comparing `slack_sdk-3.9.0rc2/slack_sdk/rtm_v2/__init__.py` & `slack_sdk-3.9.1/slack_sdk/rtm_v2/__init__.py`

 * *Files identical despite different names*

### Comparing `slack_sdk-3.9.0rc2/slack_sdk/scim/__init__.py` & `slack_sdk-3.9.1/slack_sdk/scim/__init__.py`

 * *Files identical despite different names*

### Comparing `slack_sdk-3.9.0rc2/slack_sdk/scim/v1/async_client.py` & `slack_sdk-3.9.1/slack_sdk/scim/v1/async_client.py`

 * *Files 2% similar despite different names*

```diff
@@ -66,15 +66,15 @@
         session: Optional[ClientSession] = None,
         trust_env_in_session: bool = False,
         auth: Optional[BasicAuth] = None,
         default_headers: Optional[Dict[str, str]] = None,
         user_agent_prefix: Optional[str] = None,
         user_agent_suffix: Optional[str] = None,
         logger: Optional[logging.Logger] = None,
-        retry_handlers: List[AsyncRetryHandler] = async_default_handlers,
+        retry_handlers: Optional[List[AsyncRetryHandler]] = None,
     ):
         """API client for SCIM API
         See https://api.slack.com/scim for more details
 
         Args:
             token: An admin user's token, which starts with `xoxp-`
             timeout: Request timeout (in seconds)
@@ -99,15 +99,17 @@
         self.trust_env_in_session = trust_env_in_session
         self.auth = auth
         self.default_headers = default_headers if default_headers else {}
         self.default_headers["User-Agent"] = get_user_agent(
             user_agent_prefix, user_agent_suffix
         )
         self.logger = logger if logger is not None else logging.getLogger(__name__)
-        self.retry_handlers = retry_handlers
+        self.retry_handlers = (
+            retry_handlers if retry_handlers is not None else async_default_handlers()
+        )
 
         if self.proxy is None or len(self.proxy.strip()) == 0:
             env_variable = load_http_proxy_from_env(self.logger)
             if env_variable is not None:
                 self.proxy = env_variable
 
     # -------------------------
```

### Comparing `slack_sdk-3.9.0rc2/slack_sdk/scim/v1/client.py` & `slack_sdk-3.9.1/slack_sdk/scim/v1/client.py`

 * *Files 1% similar despite different names*

```diff
@@ -68,15 +68,15 @@
         ssl: Optional[SSLContext] = None,
         proxy: Optional[str] = None,
         base_url: str = BASE_URL,
         default_headers: Optional[Dict[str, str]] = None,
         user_agent_prefix: Optional[str] = None,
         user_agent_suffix: Optional[str] = None,
         logger: Optional[logging.Logger] = None,
-        retry_handlers: List[RetryHandler] = default_retry_handlers,
+        retry_handlers: Optional[List[RetryHandler]] = None,
     ):
         """API client for SCIM API
         See https://api.slack.com/scim for more details
 
         Args:
             token: An admin user's token, which starts with `xoxp-`
             timeout: Request timeout (in seconds)
@@ -95,15 +95,17 @@
         self.proxy = proxy
         self.base_url = base_url
         self.default_headers = default_headers if default_headers else {}
         self.default_headers["User-Agent"] = get_user_agent(
             user_agent_prefix, user_agent_suffix
         )
         self.logger = logger if logger is not None else logging.getLogger(__name__)
-        self.retry_handlers = retry_handlers
+        self.retry_handlers = (
+            retry_handlers if retry_handlers is not None else default_retry_handlers()
+        )
 
         if self.proxy is None or len(self.proxy.strip()) == 0:
             env_variable = load_http_proxy_from_env(self.logger)
             if env_variable is not None:
                 self.proxy = env_variable
 
     # -------------------------
```

### Comparing `slack_sdk-3.9.0rc2/slack_sdk/scim/v1/group.py` & `slack_sdk-3.9.1/slack_sdk/scim/v1/group.py`

 * *Files identical despite different names*

### Comparing `slack_sdk-3.9.0rc2/slack_sdk/scim/v1/internal_utils.py` & `slack_sdk-3.9.1/slack_sdk/scim/v1/internal_utils.py`

 * *Files identical despite different names*

### Comparing `slack_sdk-3.9.0rc2/slack_sdk/scim/v1/response.py` & `slack_sdk-3.9.1/slack_sdk/scim/v1/response.py`

 * *Files identical despite different names*

### Comparing `slack_sdk-3.9.0rc2/slack_sdk/scim/v1/types.py` & `slack_sdk-3.9.1/slack_sdk/scim/v1/types.py`

 * *Files identical despite different names*

### Comparing `slack_sdk-3.9.0rc2/slack_sdk/scim/v1/user.py` & `slack_sdk-3.9.1/slack_sdk/scim/v1/user.py`

 * *Files identical despite different names*

### Comparing `slack_sdk-3.9.0rc2/slack_sdk/signature/__init__.py` & `slack_sdk-3.9.1/slack_sdk/signature/__init__.py`

 * *Files identical despite different names*

### Comparing `slack_sdk-3.9.0rc2/slack_sdk/socket_mode/aiohttp/__init__.py` & `slack_sdk-3.9.1/slack_sdk/socket_mode/aiohttp/__init__.py`

 * *Files identical despite different names*

### Comparing `slack_sdk-3.9.0rc2/slack_sdk/socket_mode/async_client.py` & `slack_sdk-3.9.1/slack_sdk/socket_mode/async_client.py`

 * *Files identical despite different names*

### Comparing `slack_sdk-3.9.0rc2/slack_sdk/socket_mode/async_listeners.py` & `slack_sdk-3.9.1/slack_sdk/socket_mode/async_listeners.py`

 * *Files identical despite different names*

### Comparing `slack_sdk-3.9.0rc2/slack_sdk/socket_mode/builtin/client.py` & `slack_sdk-3.9.1/slack_sdk/socket_mode/builtin/client.py`

 * *Files identical despite different names*

### Comparing `slack_sdk-3.9.0rc2/slack_sdk/socket_mode/builtin/connection.py` & `slack_sdk-3.9.1/slack_sdk/socket_mode/builtin/connection.py`

 * *Files identical despite different names*

### Comparing `slack_sdk-3.9.0rc2/slack_sdk/socket_mode/builtin/frame_header.py` & `slack_sdk-3.9.1/slack_sdk/socket_mode/builtin/frame_header.py`

 * *Files identical despite different names*

### Comparing `slack_sdk-3.9.0rc2/slack_sdk/socket_mode/builtin/internals.py` & `slack_sdk-3.9.1/slack_sdk/socket_mode/builtin/internals.py`

 * *Files identical despite different names*

### Comparing `slack_sdk-3.9.0rc2/slack_sdk/socket_mode/client.py` & `slack_sdk-3.9.1/slack_sdk/socket_mode/client.py`

 * *Files identical despite different names*

### Comparing `slack_sdk-3.9.0rc2/slack_sdk/socket_mode/interval_runner.py` & `slack_sdk-3.9.1/slack_sdk/socket_mode/interval_runner.py`

 * *Files identical despite different names*

### Comparing `slack_sdk-3.9.0rc2/slack_sdk/socket_mode/request.py` & `slack_sdk-3.9.1/slack_sdk/socket_mode/request.py`

 * *Files identical despite different names*

### Comparing `slack_sdk-3.9.0rc2/slack_sdk/socket_mode/response.py` & `slack_sdk-3.9.1/slack_sdk/socket_mode/response.py`

 * *Files identical despite different names*

### Comparing `slack_sdk-3.9.0rc2/slack_sdk/socket_mode/websocket_client/__init__.py` & `slack_sdk-3.9.1/slack_sdk/socket_mode/websocket_client/__init__.py`

 * *Files identical despite different names*

### Comparing `slack_sdk-3.9.0rc2/slack_sdk/socket_mode/websockets/__init__.py` & `slack_sdk-3.9.1/slack_sdk/socket_mode/websockets/__init__.py`

 * *Files identical despite different names*

### Comparing `slack_sdk-3.9.0rc2/slack_sdk/web/async_base_client.py` & `slack_sdk-3.9.1/slack_sdk/web/async_base_client.py`

 * *Files 2% similar despite different names*

```diff
@@ -37,15 +37,15 @@
         trust_env_in_session: bool = False,
         headers: Optional[dict] = None,
         user_agent_prefix: Optional[str] = None,
         user_agent_suffix: Optional[str] = None,
         # for Org-Wide App installation
         team_id: Optional[str] = None,
         logger: Optional[logging.Logger] = None,
-        retry_handlers: List[RetryHandler] = async_default_handlers,
+        retry_handlers: Optional[List[RetryHandler]] = None,
     ):
         self.token = None if token is None else token.strip()
         self.base_url = base_url
         self.timeout = timeout
         self.ssl = ssl
         self.proxy = proxy
         self.session = session
@@ -55,15 +55,17 @@
         self.headers["User-Agent"] = get_user_agent(
             user_agent_prefix, user_agent_suffix
         )
         self.default_params = {}
         if team_id is not None:
             self.default_params["team_id"] = team_id
         self._logger = logger if logger is not None else logging.getLogger(__name__)
-        self.retry_handlers = retry_handlers
+        self.retry_handlers = (
+            retry_handlers if retry_handlers is not None else async_default_handlers()
+        )
 
         if self.proxy is None or len(self.proxy.strip()) == 0:
             env_variable = load_http_proxy_from_env(self._logger)
             if env_variable is not None:
                 self.proxy = env_variable
 
     async def api_call(  # skipcq: PYL-R1710
```

### Comparing `slack_sdk-3.9.0rc2/slack_sdk/web/async_client.py` & `slack_sdk-3.9.1/slack_sdk/web/async_client.py`

 * *Files identical despite different names*

### Comparing `slack_sdk-3.9.0rc2/slack_sdk/web/async_internal_utils.py` & `slack_sdk-3.9.1/slack_sdk/web/async_internal_utils.py`

 * *Files 3% similar despite different names*

```diff
@@ -139,14 +139,23 @@
                                 raise SlackApiError(message, res)
                             except Exception as e:
                                 raise SlackApiError(
                                     f"Unexpectedly failed to read the response body: {str(e)}",
                                     res,
                                 )
 
+                    if logger.level <= logging.DEBUG:
+                        body = data if isinstance(data, dict) else "(binary)"
+                        logger.debug(
+                            "Received the following response - "
+                            f"status: {res.status}, "
+                            f"headers: {dict(res.headers)}, "
+                            f"body: {body}"
+                        )
+
                     if res.status == 429:
                         for handler in retry_handlers:
                             if await handler.can_retry_async(
                                 state=retry_state,
                                 request=retry_request,
                                 response=retry_response,
                             ):
```

### Comparing `slack_sdk-3.9.0rc2/slack_sdk/web/async_slack_response.py` & `slack_sdk-3.9.1/slack_sdk/web/async_slack_response.py`

 * *Files identical despite different names*

### Comparing `slack_sdk-3.9.0rc2/slack_sdk/web/base_client.py` & `slack_sdk-3.9.1/slack_sdk/web/base_client.py`

 * *Files 2% similar despite different names*

```diff
@@ -50,15 +50,15 @@
         proxy: Optional[str] = None,
         headers: Optional[dict] = None,
         user_agent_prefix: Optional[str] = None,
         user_agent_suffix: Optional[str] = None,
         # for Org-Wide App installation
         team_id: Optional[str] = None,
         logger: Optional[logging.Logger] = None,
-        retry_handlers: List[RetryHandler] = default_retry_handlers,
+        retry_handlers: Optional[List[RetryHandler]] = None,
     ):
         self.token = None if token is None else token.strip()
         self.base_url = base_url
         self.timeout = timeout
         self.ssl = ssl
         self.proxy = proxy
         self.headers = headers or {}
@@ -66,15 +66,17 @@
             user_agent_prefix, user_agent_suffix
         )
         self.default_params = {}
         if team_id is not None:
             self.default_params["team_id"] = team_id
         self._logger = logger if logger is not None else logging.getLogger(__name__)
 
-        self.retry_handlers = retry_handlers
+        self.retry_handlers = (
+            retry_handlers if retry_handlers is not None else default_retry_handlers()
+        )
 
         if self.proxy is None or len(self.proxy.strip()) == 0:
             env_variable = load_http_proxy_from_env(self._logger)
             if env_variable is not None:
                 self.proxy = env_variable
 
     def api_call(  # skipcq: PYL-R1710
@@ -516,18 +518,32 @@
             else:
                 resp = urlopen(  # skipcq: BAN-B310
                     req, context=self.ssl, timeout=self.timeout
                 )
             if resp.headers.get_content_type() == "application/gzip":
                 # admin.analytics.getFile
                 body: bytes = resp.read()
+                if self._logger.level <= logging.DEBUG:
+                    self._logger.debug(
+                        "Received the following response - "
+                        f"status: {resp.code}, "
+                        f"headers: {dict(resp.headers)}, "
+                        f"body: (binary)"
+                    )
                 return {"status": resp.code, "headers": resp.headers, "body": body}
 
             charset = resp.headers.get_content_charset() or "utf-8"
             body: str = resp.read().decode(charset)  # read the response body here
+            if self._logger.level <= logging.DEBUG:
+                self._logger.debug(
+                    "Received the following response - "
+                    f"status: {resp.code}, "
+                    f"headers: {dict(resp.headers)}, "
+                    f"body: {body}"
+                )
             return {"status": resp.code, "headers": resp.headers, "body": body}
         raise SlackRequestError(f"Invalid URL detected: {url}")
 
     def _build_urllib_request_headers(
         self, token: str, has_json: bool, has_files: bool, additional_headers: dict
     ) -> Dict[str, str]:
         headers = {"Content-Type": "application/x-www-form-urlencoded"}
```

### Comparing `slack_sdk-3.9.0rc2/slack_sdk/web/client.py` & `slack_sdk-3.9.1/slack_sdk/web/client.py`

 * *Files identical despite different names*

### Comparing `slack_sdk-3.9.0rc2/slack_sdk/web/deprecation.py` & `slack_sdk-3.9.1/slack_sdk/web/deprecation.py`

 * *Files identical despite different names*

### Comparing `slack_sdk-3.9.0rc2/slack_sdk/web/internal_utils.py` & `slack_sdk-3.9.1/slack_sdk/web/internal_utils.py`

 * *Files identical despite different names*

### Comparing `slack_sdk-3.9.0rc2/slack_sdk/web/legacy_base_client.py` & `slack_sdk-3.9.1/slack_sdk/web/legacy_base_client.py`

 * *Files identical despite different names*

### Comparing `slack_sdk-3.9.0rc2/slack_sdk/web/legacy_client.py` & `slack_sdk-3.9.1/slack_sdk/web/legacy_client.py`

 * *Files identical despite different names*

### Comparing `slack_sdk-3.9.0rc2/slack_sdk/web/legacy_slack_response.py` & `slack_sdk-3.9.1/slack_sdk/web/legacy_slack_response.py`

 * *Files identical despite different names*

### Comparing `slack_sdk-3.9.0rc2/slack_sdk/web/slack_response.py` & `slack_sdk-3.9.1/slack_sdk/web/slack_response.py`

 * *Files 2% similar despite different names*

```diff
@@ -182,22 +182,14 @@
         Returns:
             (SlackResponse)
                 This method returns it's own object. e.g. 'self'
 
         Raises:
             SlackApiError: The request to the Slack API failed.
         """
-        if self._logger.level <= logging.DEBUG:
-            body = self.data if isinstance(self.data, dict) else "(binary)"
-            self._logger.debug(
-                "Received the following response - "
-                f"status: {self.status_code}, "
-                f"headers: {dict(self.headers)}, "
-                f"body: {body}"
-            )
         if (
             self.status_code == 200
             and self.data
             and (isinstance(self.data, bytes) or self.data.get("ok", False))
         ):
             return self
         msg = "The request to the Slack API failed."
```

### Comparing `slack_sdk-3.9.0rc2/slack_sdk/webhook/async_client.py` & `slack_sdk-3.9.1/slack_sdk/webhook/async_client.py`

 * *Files 2% similar despite different names*

```diff
@@ -45,15 +45,15 @@
         session: Optional[ClientSession] = None,
         trust_env_in_session: bool = False,
         auth: Optional[BasicAuth] = None,
         default_headers: Optional[Dict[str, str]] = None,
         user_agent_prefix: Optional[str] = None,
         user_agent_suffix: Optional[str] = None,
         logger: Optional[logging.Logger] = None,
-        retry_handlers: List[AsyncRetryHandler] = async_default_handlers,
+        retry_handlers: Optional[List[AsyncRetryHandler]] = None,
     ):
         """API client for Incoming Webhooks and `response_url`
 
         https://api.slack.com/messaging/webhooks
 
         Args:
             url: Complete URL to send data (e.g., `https://hooks.slack.com/XXX`)
@@ -76,15 +76,17 @@
         self.session = session
         self.auth = auth
         self.default_headers = default_headers if default_headers else {}
         self.default_headers["User-Agent"] = get_user_agent(
             user_agent_prefix, user_agent_suffix
         )
         self.logger = logger if logger is not None else logging.getLogger(__name__)
-        self.retry_handlers = retry_handlers
+        self.retry_handlers = (
+            retry_handlers if retry_handlers is not None else async_default_handlers()
+        )
 
         if self.proxy is None or len(self.proxy.strip()) == 0:
             env_variable = load_http_proxy_from_env(self.logger)
             if env_variable is not None:
                 self.proxy = env_variable
 
     async def send(
```

### Comparing `slack_sdk-3.9.0rc2/slack_sdk/webhook/client.py` & `slack_sdk-3.9.1/slack_sdk/webhook/client.py`

 * *Files 2% similar despite different names*

```diff
@@ -40,15 +40,15 @@
         timeout: int = 30,
         ssl: Optional[SSLContext] = None,
         proxy: Optional[str] = None,
         default_headers: Optional[Dict[str, str]] = None,
         user_agent_prefix: Optional[str] = None,
         user_agent_suffix: Optional[str] = None,
         logger: Optional[logging.Logger] = None,
-        retry_handlers: List[RetryHandler] = default_retry_handlers,
+        retry_handlers: Optional[List[RetryHandler]] = None,
     ):
         """API client for Incoming Webhooks and `response_url`
 
         https://api.slack.com/messaging/webhooks
 
         Args:
             url: Complete URL to send data (e.g., `https://hooks.slack.com/XXX`)
@@ -66,15 +66,17 @@
         self.ssl = ssl
         self.proxy = proxy
         self.default_headers = default_headers if default_headers else {}
         self.default_headers["User-Agent"] = get_user_agent(
             user_agent_prefix, user_agent_suffix
         )
         self.logger = logger if logger is not None else logging.getLogger(__name__)
-        self.retry_handlers = retry_handlers
+        self.retry_handlers = (
+            retry_handlers if retry_handlers is not None else default_retry_handlers()
+        )
 
         if self.proxy is None or len(self.proxy.strip()) == 0:
             env_variable = load_http_proxy_from_env(self.logger)
             if env_variable is not None:
                 self.proxy = env_variable
 
     def send(
```

### Comparing `slack_sdk-3.9.0rc2/slack_sdk/webhook/internal_utils.py` & `slack_sdk-3.9.1/slack_sdk/webhook/internal_utils.py`

 * *Files identical despite different names*

### Comparing `slack_sdk-3.9.0rc2/slack_sdk.egg-info/PKG-INFO` & `slack_sdk-3.9.1/slack_sdk.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: slack-sdk
-Version: 3.9.0rc2
+Version: 3.9.1
 Summary: The Slack API Platform SDK for Python
 Home-page: https://github.com/slackapi/python-slack-sdk
 Author: Slack Technologies, Inc.
 Author-email: opensource@slack.com
 License: MIT
 Description: # Python Slack SDK
```

### Comparing `slack_sdk-3.9.0rc2/slack_sdk.egg-info/SOURCES.txt` & `slack_sdk-3.9.1/slack_sdk.egg-info/SOURCES.txt`

 * *Files identical despite different names*

