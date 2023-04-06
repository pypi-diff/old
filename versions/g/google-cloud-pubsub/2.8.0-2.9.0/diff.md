# Comparing `tmp/google-cloud-pubsub-2.8.0.tar.gz` & `tmp/google-cloud-pubsub-2.9.0.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "dist/google-cloud-pubsub-2.8.0.tar", last modified: Mon Sep  6 11:35:55 2021, max compression
+gzip compressed data, was "google-cloud-pubsub-2.9.0.tar", last modified: Wed Nov 10 16:52:04 2021, max compression
```

## Comparing `google-cloud-pubsub-2.8.0.tar` & `google-cloud-pubsub-2.9.0.tar`

### file list

```diff
@@ -1,145 +1,145 @@
-drwxr-sr-x   0 root         (0)     1003        0 2021-09-06 11:35:55.849597 google-cloud-pubsub-2.8.0/
--rw-rw-r--   0 root         (0)     1003    11358 2021-09-06 11:33:18.000000 google-cloud-pubsub-2.8.0/LICENSE
--rw-rw-r--   0 root         (0)     1003      860 2021-09-06 11:33:18.000000 google-cloud-pubsub-2.8.0/MANIFEST.in
--rw-r--r--   0 root         (0)     1003     8613 2021-09-06 11:35:55.853597 google-cloud-pubsub-2.8.0/PKG-INFO
--rw-rw-r--   0 root         (0)     1003     7799 2021-09-06 11:33:18.000000 google-cloud-pubsub-2.8.0/README.rst
-drwxr-sr-x   0 root         (0)     1003        0 2021-09-06 11:35:55.833597 google-cloud-pubsub-2.8.0/google/
--rw-rw-r--   0 root         (0)     1003      774 2021-09-06 11:33:18.000000 google-cloud-pubsub-2.8.0/google/__init__.py
-drwxr-sr-x   0 root         (0)     1003        0 2021-09-06 11:35:55.833597 google-cloud-pubsub-2.8.0/google/cloud/
--rw-rw-r--   0 root         (0)     1003      774 2021-09-06 11:33:18.000000 google-cloud-pubsub-2.8.0/google/cloud/__init__.py
-drwxr-sr-x   0 root         (0)     1003        0 2021-09-06 11:35:55.833597 google-cloud-pubsub-2.8.0/google/cloud/pubsub/
--rw-rw-r--   0 root         (0)     1003      945 2021-09-06 11:33:18.000000 google-cloud-pubsub-2.8.0/google/cloud/pubsub/__init__.py
-drwxr-sr-x   0 root         (0)     1003        0 2021-09-06 11:35:55.833597 google-cloud-pubsub-2.8.0/google/cloud/pubsub_v1/
--rw-rw-r--   0 root         (0)     1003     1209 2021-09-06 11:33:18.000000 google-cloud-pubsub-2.8.0/google/cloud/pubsub_v1/__init__.py
--rw-rw-r--   0 root         (0)     1003     2633 2021-09-06 11:33:18.000000 google-cloud-pubsub-2.8.0/google/cloud/pubsub_v1/_gapic.py
--rw-rw-r--   0 root         (0)     1003      711 2021-09-06 11:33:18.000000 google-cloud-pubsub-2.8.0/google/cloud/pubsub_v1/exceptions.py
--rw-rw-r--   0 root         (0)     1003     1971 2021-09-06 11:33:18.000000 google-cloud-pubsub-2.8.0/google/cloud/pubsub_v1/futures.py
-drwxr-sr-x   0 root         (0)     1003        0 2021-09-06 11:35:55.833597 google-cloud-pubsub-2.8.0/google/cloud/pubsub_v1/proto/
--rw-rw-r--   0 root         (0)     1003    58026 2021-09-06 11:33:18.000000 google-cloud-pubsub-2.8.0/google/cloud/pubsub_v1/proto/pubsub.proto
--rw-rw-r--   0 root         (0)     1003     8781 2021-09-06 11:33:18.000000 google-cloud-pubsub-2.8.0/google/cloud/pubsub_v1/proto/schema.proto
-drwxr-sr-x   0 root         (0)     1003        0 2021-09-06 11:35:55.833597 google-cloud-pubsub-2.8.0/google/cloud/pubsub_v1/publisher/
--rw-rw-r--   0 root         (0)     1003      720 2021-09-06 11:33:18.000000 google-cloud-pubsub-2.8.0/google/cloud/pubsub_v1/publisher/__init__.py
-drwxr-sr-x   0 root         (0)     1003        0 2021-09-06 11:35:55.837597 google-cloud-pubsub-2.8.0/google/cloud/pubsub_v1/publisher/_batch/
--rw-rw-r--   0 root         (0)     1003        0 2021-09-06 11:33:18.000000 google-cloud-pubsub-2.8.0/google/cloud/pubsub_v1/publisher/_batch/__init__.py
--rw-rw-r--   0 root         (0)     1003     5549 2021-09-06 11:33:18.000000 google-cloud-pubsub-2.8.0/google/cloud/pubsub_v1/publisher/_batch/base.py
--rw-rw-r--   0 root         (0)     1003    15570 2021-09-06 11:33:18.000000 google-cloud-pubsub-2.8.0/google/cloud/pubsub_v1/publisher/_batch/thread.py
-drwxr-sr-x   0 root         (0)     1003        0 2021-09-06 11:35:55.837597 google-cloud-pubsub-2.8.0/google/cloud/pubsub_v1/publisher/_sequencer/
--rw-rw-r--   0 root         (0)     1003        0 2021-09-06 11:33:18.000000 google-cloud-pubsub-2.8.0/google/cloud/pubsub_v1/publisher/_sequencer/__init__.py
--rw-rw-r--   0 root         (0)     1003     2807 2021-09-06 11:33:18.000000 google-cloud-pubsub-2.8.0/google/cloud/pubsub_v1/publisher/_sequencer/base.py
--rw-rw-r--   0 root         (0)     1003    14006 2021-09-06 11:33:18.000000 google-cloud-pubsub-2.8.0/google/cloud/pubsub_v1/publisher/_sequencer/ordered_sequencer.py
--rw-rw-r--   0 root         (0)     1003     5579 2021-09-06 11:33:18.000000 google-cloud-pubsub-2.8.0/google/cloud/pubsub_v1/publisher/_sequencer/unordered_sequencer.py
--rw-rw-r--   0 root         (0)     1003    18942 2021-09-06 11:33:18.000000 google-cloud-pubsub-2.8.0/google/cloud/pubsub_v1/publisher/client.py
--rw-rw-r--   0 root         (0)     1003     1689 2021-09-06 11:33:18.000000 google-cloud-pubsub-2.8.0/google/cloud/pubsub_v1/publisher/exceptions.py
--rw-rw-r--   0 root         (0)     1003    12177 2021-09-06 11:33:18.000000 google-cloud-pubsub-2.8.0/google/cloud/pubsub_v1/publisher/flow_controller.py
--rw-rw-r--   0 root         (0)     1003     1917 2021-09-06 11:33:18.000000 google-cloud-pubsub-2.8.0/google/cloud/pubsub_v1/publisher/futures.py
-drwxr-sr-x   0 root         (0)     1003        0 2021-09-06 11:35:55.837597 google-cloud-pubsub-2.8.0/google/cloud/pubsub_v1/subscriber/
--rw-rw-r--   0 root         (0)     1003      721 2021-09-06 11:33:18.000000 google-cloud-pubsub-2.8.0/google/cloud/pubsub_v1/subscriber/__init__.py
-drwxr-sr-x   0 root         (0)     1003        0 2021-09-06 11:35:55.837597 google-cloud-pubsub-2.8.0/google/cloud/pubsub_v1/subscriber/_protocol/
--rw-rw-r--   0 root         (0)     1003        0 2021-09-06 11:33:18.000000 google-cloud-pubsub-2.8.0/google/cloud/pubsub_v1/subscriber/_protocol/__init__.py
--rw-rw-r--   0 root         (0)     1003     7291 2021-09-06 11:33:18.000000 google-cloud-pubsub-2.8.0/google/cloud/pubsub_v1/subscriber/_protocol/dispatcher.py
--rw-rw-r--   0 root         (0)     1003     2385 2021-09-06 11:33:18.000000 google-cloud-pubsub-2.8.0/google/cloud/pubsub_v1/subscriber/_protocol/heartbeater.py
--rw-rw-r--   0 root         (0)     1003     3966 2021-09-06 11:33:18.000000 google-cloud-pubsub-2.8.0/google/cloud/pubsub_v1/subscriber/_protocol/helper_threads.py
--rw-rw-r--   0 root         (0)     1003     5791 2021-09-06 11:33:18.000000 google-cloud-pubsub-2.8.0/google/cloud/pubsub_v1/subscriber/_protocol/histogram.py
--rw-rw-r--   0 root         (0)     1003     8617 2021-09-06 11:33:18.000000 google-cloud-pubsub-2.8.0/google/cloud/pubsub_v1/subscriber/_protocol/leaser.py
--rw-rw-r--   0 root         (0)     1003     6460 2021-09-06 11:33:18.000000 google-cloud-pubsub-2.8.0/google/cloud/pubsub_v1/subscriber/_protocol/messages_on_hold.py
--rw-rw-r--   0 root         (0)     1003     1319 2021-09-06 11:33:18.000000 google-cloud-pubsub-2.8.0/google/cloud/pubsub_v1/subscriber/_protocol/requests.py
--rw-rw-r--   0 root         (0)     1003    31482 2021-09-06 11:33:18.000000 google-cloud-pubsub-2.8.0/google/cloud/pubsub_v1/subscriber/_protocol/streaming_pull_manager.py
--rw-rw-r--   0 root         (0)     1003    10668 2021-09-06 11:33:18.000000 google-cloud-pubsub-2.8.0/google/cloud/pubsub_v1/subscriber/client.py
--rw-rw-r--   0 root         (0)     1003     2421 2021-09-06 11:33:18.000000 google-cloud-pubsub-2.8.0/google/cloud/pubsub_v1/subscriber/futures.py
--rw-rw-r--   0 root         (0)     1003    10372 2021-09-06 11:33:18.000000 google-cloud-pubsub-2.8.0/google/cloud/pubsub_v1/subscriber/message.py
--rw-rw-r--   0 root         (0)     1003     5733 2021-09-06 11:33:18.000000 google-cloud-pubsub-2.8.0/google/cloud/pubsub_v1/subscriber/scheduler.py
--rw-rw-r--   0 root         (0)     1003     7982 2021-09-06 11:33:18.000000 google-cloud-pubsub-2.8.0/google/cloud/pubsub_v1/types.py
-drwxr-sr-x   0 root         (0)     1003        0 2021-09-06 11:35:55.837597 google-cloud-pubsub-2.8.0/google/pubsub/
--rw-rw-r--   0 root         (0)     1003     6154 2021-09-06 11:33:18.000000 google-cloud-pubsub-2.8.0/google/pubsub/__init__.py
--rw-rw-r--   0 root         (0)     1003       74 2021-09-06 11:33:18.000000 google-cloud-pubsub-2.8.0/google/pubsub/py.typed
-drwxr-sr-x   0 root         (0)     1003        0 2021-09-06 11:35:55.841597 google-cloud-pubsub-2.8.0/google/pubsub_v1/
--rw-rw-r--   0 root         (0)     1003     5093 2021-09-06 11:33:18.000000 google-cloud-pubsub-2.8.0/google/pubsub_v1/__init__.py
--rw-rw-r--   0 root         (0)     1003     8657 2021-09-06 11:33:18.000000 google-cloud-pubsub-2.8.0/google/pubsub_v1/gapic_metadata.json
--rw-rw-r--   0 root         (0)     1003       74 2021-09-06 11:33:18.000000 google-cloud-pubsub-2.8.0/google/pubsub_v1/py.typed
-drwxr-sr-x   0 root         (0)     1003        0 2021-09-06 11:35:55.841597 google-cloud-pubsub-2.8.0/google/pubsub_v1/services/
--rw-rw-r--   0 root         (0)     1003      600 2021-09-06 11:33:18.000000 google-cloud-pubsub-2.8.0/google/pubsub_v1/services/__init__.py
-drwxr-sr-x   0 root         (0)     1003        0 2021-09-06 11:35:55.841597 google-cloud-pubsub-2.8.0/google/pubsub_v1/services/publisher/
--rw-rw-r--   0 root         (0)     1003      749 2021-09-06 11:33:18.000000 google-cloud-pubsub-2.8.0/google/pubsub_v1/services/publisher/__init__.py
--rw-rw-r--   0 root         (0)     1003    49405 2021-09-06 11:33:18.000000 google-cloud-pubsub-2.8.0/google/pubsub_v1/services/publisher/async_client.py
--rw-rw-r--   0 root         (0)     1003    56708 2021-09-06 11:33:18.000000 google-cloud-pubsub-2.8.0/google/pubsub_v1/services/publisher/client.py
--rw-rw-r--   0 root         (0)     1003    15546 2021-09-06 11:33:18.000000 google-cloud-pubsub-2.8.0/google/pubsub_v1/services/publisher/pagers.py
-drwxr-sr-x   0 root         (0)     1003        0 2021-09-06 11:35:55.841597 google-cloud-pubsub-2.8.0/google/pubsub_v1/services/publisher/transports/
--rw-rw-r--   0 root         (0)     1003     1149 2021-09-06 11:33:18.000000 google-cloud-pubsub-2.8.0/google/pubsub_v1/services/publisher/transports/__init__.py
--rw-rw-r--   0 root         (0)     1003    14986 2021-09-06 11:33:18.000000 google-cloud-pubsub-2.8.0/google/pubsub_v1/services/publisher/transports/base.py
--rw-rw-r--   0 root         (0)     1003    24881 2021-09-06 11:33:18.000000 google-cloud-pubsub-2.8.0/google/pubsub_v1/services/publisher/transports/grpc.py
--rw-rw-r--   0 root         (0)     1003    25463 2021-09-06 11:33:18.000000 google-cloud-pubsub-2.8.0/google/pubsub_v1/services/publisher/transports/grpc_asyncio.py
-drwxr-sr-x   0 root         (0)     1003        0 2021-09-06 11:35:55.841597 google-cloud-pubsub-2.8.0/google/pubsub_v1/services/schema_service/
--rw-rw-r--   0 root         (0)     1003      765 2021-09-06 11:33:18.000000 google-cloud-pubsub-2.8.0/google/pubsub_v1/services/schema_service/__init__.py
--rw-rw-r--   0 root         (0)     1003    36585 2021-09-06 11:33:18.000000 google-cloud-pubsub-2.8.0/google/pubsub_v1/services/schema_service/async_client.py
--rw-rw-r--   0 root         (0)     1003    45211 2021-09-06 11:33:18.000000 google-cloud-pubsub-2.8.0/google/pubsub_v1/services/schema_service/client.py
--rw-rw-r--   0 root         (0)     1003     5562 2021-09-06 11:33:18.000000 google-cloud-pubsub-2.8.0/google/pubsub_v1/services/schema_service/pagers.py
-drwxr-sr-x   0 root         (0)     1003        0 2021-09-06 11:35:55.841597 google-cloud-pubsub-2.8.0/google/pubsub_v1/services/schema_service/transports/
--rw-rw-r--   0 root         (0)     1003     1185 2021-09-06 11:33:18.000000 google-cloud-pubsub-2.8.0/google/pubsub_v1/services/schema_service/transports/__init__.py
--rw-rw-r--   0 root         (0)     1003     9779 2021-09-06 11:33:18.000000 google-cloud-pubsub-2.8.0/google/pubsub_v1/services/schema_service/transports/base.py
--rw-rw-r--   0 root         (0)     1003    20428 2021-09-06 11:33:18.000000 google-cloud-pubsub-2.8.0/google/pubsub_v1/services/schema_service/transports/grpc.py
--rw-rw-r--   0 root         (0)     1003    20952 2021-09-06 11:33:18.000000 google-cloud-pubsub-2.8.0/google/pubsub_v1/services/schema_service/transports/grpc_asyncio.py
-drwxr-sr-x   0 root         (0)     1003        0 2021-09-06 11:35:55.845597 google-cloud-pubsub-2.8.0/google/pubsub_v1/services/subscriber/
--rw-rw-r--   0 root         (0)     1003      753 2021-09-06 11:33:18.000000 google-cloud-pubsub-2.8.0/google/pubsub_v1/services/subscriber/__init__.py
--rw-rw-r--   0 root         (0)     1003    82598 2021-09-06 11:33:18.000000 google-cloud-pubsub-2.8.0/google/pubsub_v1/services/subscriber/async_client.py
--rw-rw-r--   0 root         (0)     1003    88794 2021-09-06 11:33:18.000000 google-cloud-pubsub-2.8.0/google/pubsub_v1/services/subscriber/client.py
--rw-rw-r--   0 root         (0)     1003    10604 2021-09-06 11:33:18.000000 google-cloud-pubsub-2.8.0/google/pubsub_v1/services/subscriber/pagers.py
-drwxr-sr-x   0 root         (0)     1003        0 2021-09-06 11:35:55.845597 google-cloud-pubsub-2.8.0/google/pubsub_v1/services/subscriber/transports/
--rw-rw-r--   0 root         (0)     1003     1158 2021-09-06 11:33:18.000000 google-cloud-pubsub-2.8.0/google/pubsub_v1/services/subscriber/transports/__init__.py
--rw-rw-r--   0 root         (0)     1003    20400 2021-09-06 11:33:18.000000 google-cloud-pubsub-2.8.0/google/pubsub_v1/services/subscriber/transports/base.py
--rw-rw-r--   0 root         (0)     1003    37304 2021-09-06 11:33:18.000000 google-cloud-pubsub-2.8.0/google/pubsub_v1/services/subscriber/transports/grpc.py
--rw-rw-r--   0 root         (0)     1003    38059 2021-09-06 11:33:18.000000 google-cloud-pubsub-2.8.0/google/pubsub_v1/services/subscriber/transports/grpc_asyncio.py
-drwxr-sr-x   0 root         (0)     1003        0 2021-09-06 11:35:55.845597 google-cloud-pubsub-2.8.0/google/pubsub_v1/types/
--rw-rw-r--   0 root         (0)     1003     3730 2021-09-06 11:33:18.000000 google-cloud-pubsub-2.8.0/google/pubsub_v1/types/__init__.py
--rw-rw-r--   0 root         (0)     1003    55360 2021-09-06 11:33:18.000000 google-cloud-pubsub-2.8.0/google/pubsub_v1/types/pubsub.py
--rw-rw-r--   0 root         (0)     1003     7680 2021-09-06 11:33:18.000000 google-cloud-pubsub-2.8.0/google/pubsub_v1/types/schema.py
-drwxr-sr-x   0 root         (0)     1003        0 2021-09-06 11:35:55.845597 google-cloud-pubsub-2.8.0/google_cloud_pubsub.egg-info/
--rw-r--r--   0 root         (0)     1003     8613 2021-09-06 11:35:55.000000 google-cloud-pubsub-2.8.0/google_cloud_pubsub.egg-info/PKG-INFO
--rw-r--r--   0 root         (0)     1003     5102 2021-09-06 11:35:55.000000 google-cloud-pubsub-2.8.0/google_cloud_pubsub.egg-info/SOURCES.txt
--rw-r--r--   0 root         (0)     1003        1 2021-09-06 11:35:55.000000 google-cloud-pubsub-2.8.0/google_cloud_pubsub.egg-info/dependency_links.txt
--rw-r--r--   0 root         (0)     1003       20 2021-09-06 11:35:55.000000 google-cloud-pubsub-2.8.0/google_cloud_pubsub.egg-info/namespace_packages.txt
--rw-r--r--   0 root         (0)     1003        1 2021-09-06 11:35:55.000000 google-cloud-pubsub-2.8.0/google_cloud_pubsub.egg-info/not-zip-safe
--rw-r--r--   0 root         (0)     1003      148 2021-09-06 11:35:55.000000 google-cloud-pubsub-2.8.0/google_cloud_pubsub.egg-info/requires.txt
--rw-r--r--   0 root         (0)     1003        7 2021-09-06 11:35:55.000000 google-cloud-pubsub-2.8.0/google_cloud_pubsub.egg-info/top_level.txt
-drwxr-sr-x   0 root         (0)     1003        0 2021-09-06 11:35:55.845597 google-cloud-pubsub-2.8.0/scripts/
--rw-rw-r--   0 root         (0)     1003     8403 2021-09-06 11:33:18.000000 google-cloud-pubsub-2.8.0/scripts/fixup_pubsub_v1_keywords.py
--rw-rw-r--   0 root         (0)     1003       67 2021-09-06 11:35:55.853597 google-cloud-pubsub-2.8.0/setup.cfg
--rw-rw-r--   0 root         (0)     1003     3047 2021-09-06 11:33:18.000000 google-cloud-pubsub-2.8.0/setup.py
-drwxr-sr-x   0 root         (0)     1003        0 2021-09-06 11:35:55.845597 google-cloud-pubsub-2.8.0/tests/
--rw-rw-r--   0 root         (0)     1003      600 2021-09-06 11:33:18.000000 google-cloud-pubsub-2.8.0/tests/__init__.py
--rw-rw-r--   0 root         (0)     1003    36835 2021-09-06 11:33:18.000000 google-cloud-pubsub-2.8.0/tests/system.py
-drwxr-sr-x   0 root         (0)     1003        0 2021-09-06 11:35:55.845597 google-cloud-pubsub-2.8.0/tests/unit/
--rw-rw-r--   0 root         (0)     1003      600 2021-09-06 11:33:18.000000 google-cloud-pubsub-2.8.0/tests/unit/__init__.py
-drwxr-sr-x   0 root         (0)     1003        0 2021-09-06 11:35:55.845597 google-cloud-pubsub-2.8.0/tests/unit/gapic/
--rw-rw-r--   0 root         (0)     1003      600 2021-09-06 11:33:18.000000 google-cloud-pubsub-2.8.0/tests/unit/gapic/__init__.py
-drwxr-sr-x   0 root         (0)     1003        0 2021-09-06 11:35:55.849597 google-cloud-pubsub-2.8.0/tests/unit/gapic/pubsub_v1/
--rw-rw-r--   0 root         (0)     1003      600 2021-09-06 11:33:18.000000 google-cloud-pubsub-2.8.0/tests/unit/gapic/pubsub_v1/__init__.py
--rw-rw-r--   0 root         (0)     1003   138857 2021-09-06 11:33:18.000000 google-cloud-pubsub-2.8.0/tests/unit/gapic/pubsub_v1/test_publisher.py
--rw-rw-r--   0 root         (0)     1003   108397 2021-09-06 11:33:18.000000 google-cloud-pubsub-2.8.0/tests/unit/gapic/pubsub_v1/test_schema_service.py
--rw-rw-r--   0 root         (0)     1003   186733 2021-09-06 11:33:18.000000 google-cloud-pubsub-2.8.0/tests/unit/gapic/pubsub_v1/test_subscriber.py
-drwxr-sr-x   0 root         (0)     1003        0 2021-09-06 11:35:55.849597 google-cloud-pubsub-2.8.0/tests/unit/pubsub_v1/
--rw-rw-r--   0 root         (0)     1003      845 2021-09-06 11:33:18.000000 google-cloud-pubsub-2.8.0/tests/unit/pubsub_v1/conftest.py
-drwxr-sr-x   0 root         (0)     1003        0 2021-09-06 11:35:55.849597 google-cloud-pubsub-2.8.0/tests/unit/pubsub_v1/publisher/
-drwxr-sr-x   0 root         (0)     1003        0 2021-09-06 11:35:55.849597 google-cloud-pubsub-2.8.0/tests/unit/pubsub_v1/publisher/batch/
--rw-rw-r--   0 root         (0)     1003     1644 2021-09-06 11:33:18.000000 google-cloud-pubsub-2.8.0/tests/unit/pubsub_v1/publisher/batch/test_base.py
--rw-rw-r--   0 root         (0)     1003    19340 2021-09-06 11:33:18.000000 google-cloud-pubsub-2.8.0/tests/unit/pubsub_v1/publisher/batch/test_thread.py
-drwxr-sr-x   0 root         (0)     1003        0 2021-09-06 11:35:55.849597 google-cloud-pubsub-2.8.0/tests/unit/pubsub_v1/publisher/sequencer/
--rw-rw-r--   0 root         (0)     1003     9804 2021-09-06 11:33:18.000000 google-cloud-pubsub-2.8.0/tests/unit/pubsub_v1/publisher/sequencer/test_ordered_sequencer.py
--rw-rw-r--   0 root         (0)     1003     4756 2021-09-06 11:33:18.000000 google-cloud-pubsub-2.8.0/tests/unit/pubsub_v1/publisher/sequencer/test_unordered_sequencer.py
--rw-rw-r--   0 root         (0)     1003    17769 2021-09-06 11:33:18.000000 google-cloud-pubsub-2.8.0/tests/unit/pubsub_v1/publisher/test_flow_controller.py
--rw-rw-r--   0 root         (0)     1003     1325 2021-09-06 11:33:18.000000 google-cloud-pubsub-2.8.0/tests/unit/pubsub_v1/publisher/test_futures_publisher.py
--rw-rw-r--   0 root         (0)     1003    22464 2021-09-06 11:33:18.000000 google-cloud-pubsub-2.8.0/tests/unit/pubsub_v1/publisher/test_publisher_client.py
-drwxr-sr-x   0 root         (0)     1003        0 2021-09-06 11:35:55.849597 google-cloud-pubsub-2.8.0/tests/unit/pubsub_v1/subscriber/
--rw-rw-r--   0 root         (0)     1003     9832 2021-09-06 11:33:18.000000 google-cloud-pubsub-2.8.0/tests/unit/pubsub_v1/subscriber/test_dispatcher.py
--rw-rw-r--   0 root         (0)     1003     2481 2021-09-06 11:33:18.000000 google-cloud-pubsub-2.8.0/tests/unit/pubsub_v1/subscriber/test_futures_subscriber.py
--rw-rw-r--   0 root         (0)     1003     4226 2021-09-06 11:33:18.000000 google-cloud-pubsub-2.8.0/tests/unit/pubsub_v1/subscriber/test_heartbeater.py
--rw-rw-r--   0 root         (0)     1003     3888 2021-09-06 11:33:18.000000 google-cloud-pubsub-2.8.0/tests/unit/pubsub_v1/subscriber/test_helper_threads.py
--rw-rw-r--   0 root         (0)     1003     2378 2021-09-06 11:33:18.000000 google-cloud-pubsub-2.8.0/tests/unit/pubsub_v1/subscriber/test_histogram.py
--rw-rw-r--   0 root         (0)     1003     8151 2021-09-06 11:33:18.000000 google-cloud-pubsub-2.8.0/tests/unit/pubsub_v1/subscriber/test_leaser.py
--rw-rw-r--   0 root         (0)     1003     5800 2021-09-06 11:33:18.000000 google-cloud-pubsub-2.8.0/tests/unit/pubsub_v1/subscriber/test_message.py
--rw-rw-r--   0 root         (0)     1003     8802 2021-09-06 11:33:18.000000 google-cloud-pubsub-2.8.0/tests/unit/pubsub_v1/subscriber/test_messages_on_hold.py
--rw-rw-r--   0 root         (0)     1003     5542 2021-09-06 11:33:18.000000 google-cloud-pubsub-2.8.0/tests/unit/pubsub_v1/subscriber/test_scheduler.py
--rw-rw-r--   0 root         (0)     1003    38052 2021-09-06 11:33:18.000000 google-cloud-pubsub-2.8.0/tests/unit/pubsub_v1/subscriber/test_streaming_pull_manager.py
--rw-rw-r--   0 root         (0)     1003     9347 2021-09-06 11:33:18.000000 google-cloud-pubsub-2.8.0/tests/unit/pubsub_v1/subscriber/test_subscriber_client.py
--rw-rw-r--   0 root         (0)     1003     2108 2021-09-06 11:33:18.000000 google-cloud-pubsub-2.8.0/tests/unit/pubsub_v1/test__gapic.py
--rw-rw-r--   0 root         (0)     1003     5357 2021-09-06 11:33:18.000000 google-cloud-pubsub-2.8.0/tests/unit/pubsub_v1/test_futures.py
--rw-rw-r--   0 root         (0)     1003      865 2021-09-06 11:33:18.000000 google-cloud-pubsub-2.8.0/tests/unit/test_pubsub.py
+drwxr-sr-x   0 root         (0)     1003        0 2021-11-10 16:52:04.074392 google-cloud-pubsub-2.9.0/
+-rw-rw-r--   0 root         (0)     1003    11358 2021-11-10 16:49:33.000000 google-cloud-pubsub-2.9.0/LICENSE
+-rw-rw-r--   0 root         (0)     1003      860 2021-11-10 16:49:33.000000 google-cloud-pubsub-2.9.0/MANIFEST.in
+-rw-r--r--   0 root         (0)     1003     8708 2021-11-10 16:52:04.074392 google-cloud-pubsub-2.9.0/PKG-INFO
+-rw-rw-r--   0 root         (0)     1003     7793 2021-11-10 16:49:33.000000 google-cloud-pubsub-2.9.0/README.rst
+drwxr-sr-x   0 root         (0)     1003        0 2021-11-10 16:52:04.050380 google-cloud-pubsub-2.9.0/google/
+-rw-rw-r--   0 root         (0)     1003      774 2021-11-10 16:49:33.000000 google-cloud-pubsub-2.9.0/google/__init__.py
+drwxr-sr-x   0 root         (0)     1003        0 2021-11-10 16:52:04.054382 google-cloud-pubsub-2.9.0/google/cloud/
+-rw-rw-r--   0 root         (0)     1003      774 2021-11-10 16:49:33.000000 google-cloud-pubsub-2.9.0/google/cloud/__init__.py
+drwxr-sr-x   0 root         (0)     1003        0 2021-11-10 16:52:04.054382 google-cloud-pubsub-2.9.0/google/cloud/pubsub/
+-rw-rw-r--   0 root         (0)     1003      945 2021-11-10 16:49:33.000000 google-cloud-pubsub-2.9.0/google/cloud/pubsub/__init__.py
+drwxr-sr-x   0 root         (0)     1003        0 2021-11-10 16:52:04.054382 google-cloud-pubsub-2.9.0/google/cloud/pubsub_v1/
+-rw-rw-r--   0 root         (0)     1003     1209 2021-11-10 16:49:33.000000 google-cloud-pubsub-2.9.0/google/cloud/pubsub_v1/__init__.py
+-rw-rw-r--   0 root         (0)     1003     2768 2021-11-10 16:49:33.000000 google-cloud-pubsub-2.9.0/google/cloud/pubsub_v1/_gapic.py
+-rw-rw-r--   0 root         (0)     1003      711 2021-11-10 16:49:33.000000 google-cloud-pubsub-2.9.0/google/cloud/pubsub_v1/exceptions.py
+-rw-rw-r--   0 root         (0)     1003     2007 2021-11-10 16:49:33.000000 google-cloud-pubsub-2.9.0/google/cloud/pubsub_v1/futures.py
+drwxr-sr-x   0 root         (0)     1003        0 2021-11-10 16:52:04.054382 google-cloud-pubsub-2.9.0/google/cloud/pubsub_v1/proto/
+-rw-rw-r--   0 root         (0)     1003    58026 2021-11-10 16:49:33.000000 google-cloud-pubsub-2.9.0/google/cloud/pubsub_v1/proto/pubsub.proto
+-rw-rw-r--   0 root         (0)     1003     8781 2021-11-10 16:49:33.000000 google-cloud-pubsub-2.9.0/google/cloud/pubsub_v1/proto/schema.proto
+drwxr-sr-x   0 root         (0)     1003        0 2021-11-10 16:52:04.054382 google-cloud-pubsub-2.9.0/google/cloud/pubsub_v1/publisher/
+-rw-rw-r--   0 root         (0)     1003      720 2021-11-10 16:49:33.000000 google-cloud-pubsub-2.9.0/google/cloud/pubsub_v1/publisher/__init__.py
+drwxr-sr-x   0 root         (0)     1003        0 2021-11-10 16:52:04.054382 google-cloud-pubsub-2.9.0/google/cloud/pubsub_v1/publisher/_batch/
+-rw-rw-r--   0 root         (0)     1003        0 2021-11-10 16:49:33.000000 google-cloud-pubsub-2.9.0/google/cloud/pubsub_v1/publisher/_batch/__init__.py
+-rw-rw-r--   0 root         (0)     1003     5948 2021-11-10 16:49:33.000000 google-cloud-pubsub-2.9.0/google/cloud/pubsub_v1/publisher/_batch/base.py
+-rw-rw-r--   0 root         (0)     1003    15804 2021-11-10 16:49:33.000000 google-cloud-pubsub-2.9.0/google/cloud/pubsub_v1/publisher/_batch/thread.py
+drwxr-sr-x   0 root         (0)     1003        0 2021-11-10 16:52:04.054382 google-cloud-pubsub-2.9.0/google/cloud/pubsub_v1/publisher/_sequencer/
+-rw-rw-r--   0 root         (0)     1003        0 2021-11-10 16:49:33.000000 google-cloud-pubsub-2.9.0/google/cloud/pubsub_v1/publisher/_sequencer/__init__.py
+-rw-rw-r--   0 root         (0)     1003     2860 2021-11-10 16:49:33.000000 google-cloud-pubsub-2.9.0/google/cloud/pubsub_v1/publisher/_sequencer/base.py
+-rw-rw-r--   0 root         (0)     1003    14319 2021-11-10 16:49:33.000000 google-cloud-pubsub-2.9.0/google/cloud/pubsub_v1/publisher/_sequencer/ordered_sequencer.py
+-rw-rw-r--   0 root         (0)     1003     5782 2021-11-10 16:49:33.000000 google-cloud-pubsub-2.9.0/google/cloud/pubsub_v1/publisher/_sequencer/unordered_sequencer.py
+-rw-rw-r--   0 root         (0)     1003    19485 2021-11-10 16:49:33.000000 google-cloud-pubsub-2.9.0/google/cloud/pubsub_v1/publisher/client.py
+-rw-rw-r--   0 root         (0)     1003     1694 2021-11-10 16:49:33.000000 google-cloud-pubsub-2.9.0/google/cloud/pubsub_v1/publisher/exceptions.py
+-rw-rw-r--   0 root         (0)     1003    12130 2021-11-10 16:49:33.000000 google-cloud-pubsub-2.9.0/google/cloud/pubsub_v1/publisher/flow_controller.py
+-rw-rw-r--   0 root         (0)     1003     1962 2021-11-10 16:49:33.000000 google-cloud-pubsub-2.9.0/google/cloud/pubsub_v1/publisher/futures.py
+drwxr-sr-x   0 root         (0)     1003        0 2021-11-10 16:52:04.058384 google-cloud-pubsub-2.9.0/google/cloud/pubsub_v1/subscriber/
+-rw-rw-r--   0 root         (0)     1003      721 2021-11-10 16:49:33.000000 google-cloud-pubsub-2.9.0/google/cloud/pubsub_v1/subscriber/__init__.py
+drwxr-sr-x   0 root         (0)     1003        0 2021-11-10 16:52:04.058384 google-cloud-pubsub-2.9.0/google/cloud/pubsub_v1/subscriber/_protocol/
+-rw-rw-r--   0 root         (0)     1003        0 2021-11-10 16:49:33.000000 google-cloud-pubsub-2.9.0/google/cloud/pubsub_v1/subscriber/_protocol/__init__.py
+-rw-rw-r--   0 root         (0)     1003     7683 2021-11-10 16:49:33.000000 google-cloud-pubsub-2.9.0/google/cloud/pubsub_v1/subscriber/_protocol/dispatcher.py
+-rw-rw-r--   0 root         (0)     1003     2621 2021-11-10 16:49:33.000000 google-cloud-pubsub-2.9.0/google/cloud/pubsub_v1/subscriber/_protocol/heartbeater.py
+-rw-rw-r--   0 root         (0)     1003     4097 2021-11-10 16:49:33.000000 google-cloud-pubsub-2.9.0/google/cloud/pubsub_v1/subscriber/_protocol/helper_threads.py
+-rw-rw-r--   0 root         (0)     1003     5826 2021-11-10 16:49:33.000000 google-cloud-pubsub-2.9.0/google/cloud/pubsub_v1/subscriber/_protocol/histogram.py
+-rw-rw-r--   0 root         (0)     1003     9064 2021-11-10 16:49:33.000000 google-cloud-pubsub-2.9.0/google/cloud/pubsub_v1/subscriber/_protocol/leaser.py
+-rw-rw-r--   0 root         (0)     1003     6557 2021-11-10 16:49:33.000000 google-cloud-pubsub-2.9.0/google/cloud/pubsub_v1/subscriber/_protocol/messages_on_hold.py
+-rw-rw-r--   0 root         (0)     1003     1246 2021-11-10 16:49:33.000000 google-cloud-pubsub-2.9.0/google/cloud/pubsub_v1/subscriber/_protocol/requests.py
+-rw-rw-r--   0 root         (0)     1003    32045 2021-11-10 16:49:33.000000 google-cloud-pubsub-2.9.0/google/cloud/pubsub_v1/subscriber/_protocol/streaming_pull_manager.py
+-rw-rw-r--   0 root         (0)     1003    10838 2021-11-10 16:49:33.000000 google-cloud-pubsub-2.9.0/google/cloud/pubsub_v1/subscriber/client.py
+-rw-rw-r--   0 root         (0)     1003     2682 2021-11-10 16:49:33.000000 google-cloud-pubsub-2.9.0/google/cloud/pubsub_v1/subscriber/futures.py
+-rw-rw-r--   0 root         (0)     1003    10729 2021-11-10 16:49:33.000000 google-cloud-pubsub-2.9.0/google/cloud/pubsub_v1/subscriber/message.py
+-rw-rw-r--   0 root         (0)     1003     5966 2021-11-10 16:49:33.000000 google-cloud-pubsub-2.9.0/google/cloud/pubsub_v1/subscriber/scheduler.py
+-rw-rw-r--   0 root         (0)     1003     7308 2021-11-10 16:49:33.000000 google-cloud-pubsub-2.9.0/google/cloud/pubsub_v1/types.py
+drwxr-sr-x   0 root         (0)     1003        0 2021-11-10 16:52:04.058384 google-cloud-pubsub-2.9.0/google/pubsub/
+-rw-rw-r--   0 root         (0)     1003     6154 2021-11-10 16:49:33.000000 google-cloud-pubsub-2.9.0/google/pubsub/__init__.py
+-rw-rw-r--   0 root         (0)     1003       74 2021-11-10 16:49:33.000000 google-cloud-pubsub-2.9.0/google/pubsub/py.typed
+drwxr-sr-x   0 root         (0)     1003        0 2021-11-10 16:52:04.058384 google-cloud-pubsub-2.9.0/google/pubsub_v1/
+-rw-rw-r--   0 root         (0)     1003     5093 2021-11-10 16:49:33.000000 google-cloud-pubsub-2.9.0/google/pubsub_v1/__init__.py
+-rw-rw-r--   0 root         (0)     1003     8657 2021-11-10 16:49:33.000000 google-cloud-pubsub-2.9.0/google/pubsub_v1/gapic_metadata.json
+-rw-rw-r--   0 root         (0)     1003       74 2021-11-10 16:49:33.000000 google-cloud-pubsub-2.9.0/google/pubsub_v1/py.typed
+drwxr-sr-x   0 root         (0)     1003        0 2021-11-10 16:52:04.058384 google-cloud-pubsub-2.9.0/google/pubsub_v1/services/
+-rw-rw-r--   0 root         (0)     1003      600 2021-11-10 16:49:33.000000 google-cloud-pubsub-2.9.0/google/pubsub_v1/services/__init__.py
+drwxr-sr-x   0 root         (0)     1003        0 2021-11-10 16:52:04.062386 google-cloud-pubsub-2.9.0/google/pubsub_v1/services/publisher/
+-rw-rw-r--   0 root         (0)     1003      749 2021-11-10 16:49:33.000000 google-cloud-pubsub-2.9.0/google/pubsub_v1/services/publisher/__init__.py
+-rw-rw-r--   0 root         (0)     1003    49824 2021-11-10 16:49:33.000000 google-cloud-pubsub-2.9.0/google/pubsub_v1/services/publisher/async_client.py
+-rw-rw-r--   0 root         (0)     1003    57546 2021-11-10 16:49:33.000000 google-cloud-pubsub-2.9.0/google/pubsub_v1/services/publisher/client.py
+-rw-rw-r--   0 root         (0)     1003    15546 2021-11-10 16:49:33.000000 google-cloud-pubsub-2.9.0/google/pubsub_v1/services/publisher/pagers.py
+drwxr-sr-x   0 root         (0)     1003        0 2021-11-10 16:52:04.062386 google-cloud-pubsub-2.9.0/google/pubsub_v1/services/publisher/transports/
+-rw-rw-r--   0 root         (0)     1003     1149 2021-11-10 16:49:33.000000 google-cloud-pubsub-2.9.0/google/pubsub_v1/services/publisher/transports/__init__.py
+-rw-rw-r--   0 root         (0)     1003    13913 2021-11-10 16:49:33.000000 google-cloud-pubsub-2.9.0/google/pubsub_v1/services/publisher/transports/base.py
+-rw-rw-r--   0 root         (0)     1003    24912 2021-11-10 16:49:33.000000 google-cloud-pubsub-2.9.0/google/pubsub_v1/services/publisher/transports/grpc.py
+-rw-rw-r--   0 root         (0)     1003    25476 2021-11-10 16:49:33.000000 google-cloud-pubsub-2.9.0/google/pubsub_v1/services/publisher/transports/grpc_asyncio.py
+drwxr-sr-x   0 root         (0)     1003        0 2021-11-10 16:52:04.062386 google-cloud-pubsub-2.9.0/google/pubsub_v1/services/schema_service/
+-rw-rw-r--   0 root         (0)     1003      765 2021-11-10 16:49:33.000000 google-cloud-pubsub-2.9.0/google/pubsub_v1/services/schema_service/__init__.py
+-rw-rw-r--   0 root         (0)     1003    36953 2021-11-10 16:49:33.000000 google-cloud-pubsub-2.9.0/google/pubsub_v1/services/schema_service/async_client.py
+-rw-rw-r--   0 root         (0)     1003    45971 2021-11-10 16:49:33.000000 google-cloud-pubsub-2.9.0/google/pubsub_v1/services/schema_service/client.py
+-rw-rw-r--   0 root         (0)     1003     5562 2021-11-10 16:49:33.000000 google-cloud-pubsub-2.9.0/google/pubsub_v1/services/schema_service/pagers.py
+drwxr-sr-x   0 root         (0)     1003        0 2021-11-10 16:52:04.062386 google-cloud-pubsub-2.9.0/google/pubsub_v1/services/schema_service/transports/
+-rw-rw-r--   0 root         (0)     1003     1185 2021-11-10 16:49:33.000000 google-cloud-pubsub-2.9.0/google/pubsub_v1/services/schema_service/transports/__init__.py
+-rw-rw-r--   0 root         (0)     1003     8697 2021-11-10 16:49:33.000000 google-cloud-pubsub-2.9.0/google/pubsub_v1/services/schema_service/transports/base.py
+-rw-rw-r--   0 root         (0)     1003    20459 2021-11-10 16:49:33.000000 google-cloud-pubsub-2.9.0/google/pubsub_v1/services/schema_service/transports/grpc.py
+-rw-rw-r--   0 root         (0)     1003    20965 2021-11-10 16:49:33.000000 google-cloud-pubsub-2.9.0/google/pubsub_v1/services/schema_service/transports/grpc_asyncio.py
+drwxr-sr-x   0 root         (0)     1003        0 2021-11-10 16:52:04.062386 google-cloud-pubsub-2.9.0/google/pubsub_v1/services/subscriber/
+-rw-rw-r--   0 root         (0)     1003      753 2021-11-10 16:49:33.000000 google-cloud-pubsub-2.9.0/google/pubsub_v1/services/subscriber/__init__.py
+-rw-rw-r--   0 root         (0)     1003    83119 2021-11-10 16:49:33.000000 google-cloud-pubsub-2.9.0/google/pubsub_v1/services/subscriber/async_client.py
+-rw-rw-r--   0 root         (0)     1003    89747 2021-11-10 16:49:33.000000 google-cloud-pubsub-2.9.0/google/pubsub_v1/services/subscriber/client.py
+-rw-rw-r--   0 root         (0)     1003    10604 2021-11-10 16:49:33.000000 google-cloud-pubsub-2.9.0/google/pubsub_v1/services/subscriber/pagers.py
+drwxr-sr-x   0 root         (0)     1003        0 2021-11-10 16:52:04.066388 google-cloud-pubsub-2.9.0/google/pubsub_v1/services/subscriber/transports/
+-rw-rw-r--   0 root         (0)     1003     1158 2021-11-10 16:49:33.000000 google-cloud-pubsub-2.9.0/google/pubsub_v1/services/subscriber/transports/__init__.py
+-rw-rw-r--   0 root         (0)     1003    19318 2021-11-10 16:49:33.000000 google-cloud-pubsub-2.9.0/google/pubsub_v1/services/subscriber/transports/base.py
+-rw-rw-r--   0 root         (0)     1003    37335 2021-11-10 16:49:33.000000 google-cloud-pubsub-2.9.0/google/pubsub_v1/services/subscriber/transports/grpc.py
+-rw-rw-r--   0 root         (0)     1003    38072 2021-11-10 16:49:33.000000 google-cloud-pubsub-2.9.0/google/pubsub_v1/services/subscriber/transports/grpc_asyncio.py
+drwxr-sr-x   0 root         (0)     1003        0 2021-11-10 16:52:04.066388 google-cloud-pubsub-2.9.0/google/pubsub_v1/types/
+-rw-rw-r--   0 root         (0)     1003     3730 2021-11-10 16:49:33.000000 google-cloud-pubsub-2.9.0/google/pubsub_v1/types/__init__.py
+-rw-rw-r--   0 root         (0)     1003    55998 2021-11-10 16:49:33.000000 google-cloud-pubsub-2.9.0/google/pubsub_v1/types/pubsub.py
+-rw-rw-r--   0 root         (0)     1003     8145 2021-11-10 16:49:33.000000 google-cloud-pubsub-2.9.0/google/pubsub_v1/types/schema.py
+drwxr-sr-x   0 root         (0)     1003        0 2021-11-10 16:52:04.066388 google-cloud-pubsub-2.9.0/google_cloud_pubsub.egg-info/
+-rw-r--r--   0 root         (0)     1003     8708 2021-11-10 16:52:03.000000 google-cloud-pubsub-2.9.0/google_cloud_pubsub.egg-info/PKG-INFO
+-rw-r--r--   0 root         (0)     1003     5102 2021-11-10 16:52:03.000000 google-cloud-pubsub-2.9.0/google_cloud_pubsub.egg-info/SOURCES.txt
+-rw-r--r--   0 root         (0)     1003        1 2021-11-10 16:52:03.000000 google-cloud-pubsub-2.9.0/google_cloud_pubsub.egg-info/dependency_links.txt
+-rw-r--r--   0 root         (0)     1003       20 2021-11-10 16:52:03.000000 google-cloud-pubsub-2.9.0/google_cloud_pubsub.egg-info/namespace_packages.txt
+-rw-r--r--   0 root         (0)     1003        1 2021-11-10 16:52:03.000000 google-cloud-pubsub-2.9.0/google_cloud_pubsub.egg-info/not-zip-safe
+-rw-r--r--   0 root         (0)     1003      132 2021-11-10 16:52:03.000000 google-cloud-pubsub-2.9.0/google_cloud_pubsub.egg-info/requires.txt
+-rw-r--r--   0 root         (0)     1003        7 2021-11-10 16:52:03.000000 google-cloud-pubsub-2.9.0/google_cloud_pubsub.egg-info/top_level.txt
+drwxr-sr-x   0 root         (0)     1003        0 2021-11-10 16:52:04.066388 google-cloud-pubsub-2.9.0/scripts/
+-rw-rw-r--   0 root         (0)     1003     8341 2021-11-10 16:49:33.000000 google-cloud-pubsub-2.9.0/scripts/fixup_pubsub_v1_keywords.py
+-rw-rw-r--   0 root         (0)     1003      219 2021-11-10 16:52:04.074392 google-cloud-pubsub-2.9.0/setup.cfg
+-rw-rw-r--   0 root         (0)     1003     3121 2021-11-10 16:49:33.000000 google-cloud-pubsub-2.9.0/setup.py
+drwxr-sr-x   0 root         (0)     1003        0 2021-11-10 16:52:04.066388 google-cloud-pubsub-2.9.0/tests/
+-rw-rw-r--   0 root         (0)     1003      600 2021-11-10 16:49:33.000000 google-cloud-pubsub-2.9.0/tests/__init__.py
+-rw-rw-r--   0 root         (0)     1003    36835 2021-11-10 16:49:33.000000 google-cloud-pubsub-2.9.0/tests/system.py
+drwxr-sr-x   0 root         (0)     1003        0 2021-11-10 16:52:04.066388 google-cloud-pubsub-2.9.0/tests/unit/
+-rw-rw-r--   0 root         (0)     1003      600 2021-11-10 16:49:33.000000 google-cloud-pubsub-2.9.0/tests/unit/__init__.py
+drwxr-sr-x   0 root         (0)     1003        0 2021-11-10 16:52:04.066388 google-cloud-pubsub-2.9.0/tests/unit/gapic/
+-rw-rw-r--   0 root         (0)     1003      600 2021-11-10 16:49:33.000000 google-cloud-pubsub-2.9.0/tests/unit/gapic/__init__.py
+drwxr-sr-x   0 root         (0)     1003        0 2021-11-10 16:52:04.070390 google-cloud-pubsub-2.9.0/tests/unit/gapic/pubsub_v1/
+-rw-rw-r--   0 root         (0)     1003      600 2021-11-10 16:49:33.000000 google-cloud-pubsub-2.9.0/tests/unit/gapic/pubsub_v1/__init__.py
+-rw-rw-r--   0 root         (0)     1003   138145 2021-11-10 16:49:33.000000 google-cloud-pubsub-2.9.0/tests/unit/gapic/pubsub_v1/test_publisher.py
+-rw-rw-r--   0 root         (0)     1003   107621 2021-11-10 16:49:33.000000 google-cloud-pubsub-2.9.0/tests/unit/gapic/pubsub_v1/test_schema_service.py
+-rw-rw-r--   0 root         (0)     1003   187214 2021-11-10 16:49:33.000000 google-cloud-pubsub-2.9.0/tests/unit/gapic/pubsub_v1/test_subscriber.py
+drwxr-sr-x   0 root         (0)     1003        0 2021-11-10 16:52:04.070390 google-cloud-pubsub-2.9.0/tests/unit/pubsub_v1/
+-rw-rw-r--   0 root         (0)     1003      845 2021-11-10 16:49:33.000000 google-cloud-pubsub-2.9.0/tests/unit/pubsub_v1/conftest.py
+drwxr-sr-x   0 root         (0)     1003        0 2021-11-10 16:52:04.070390 google-cloud-pubsub-2.9.0/tests/unit/pubsub_v1/publisher/
+drwxr-sr-x   0 root         (0)     1003        0 2021-11-10 16:52:04.070390 google-cloud-pubsub-2.9.0/tests/unit/pubsub_v1/publisher/batch/
+-rw-rw-r--   0 root         (0)     1003     1644 2021-11-10 16:49:33.000000 google-cloud-pubsub-2.9.0/tests/unit/pubsub_v1/publisher/batch/test_base.py
+-rw-rw-r--   0 root         (0)     1003    19340 2021-11-10 16:49:33.000000 google-cloud-pubsub-2.9.0/tests/unit/pubsub_v1/publisher/batch/test_thread.py
+drwxr-sr-x   0 root         (0)     1003        0 2021-11-10 16:52:04.070390 google-cloud-pubsub-2.9.0/tests/unit/pubsub_v1/publisher/sequencer/
+-rw-rw-r--   0 root         (0)     1003     9804 2021-11-10 16:49:33.000000 google-cloud-pubsub-2.9.0/tests/unit/pubsub_v1/publisher/sequencer/test_ordered_sequencer.py
+-rw-rw-r--   0 root         (0)     1003     4756 2021-11-10 16:49:33.000000 google-cloud-pubsub-2.9.0/tests/unit/pubsub_v1/publisher/sequencer/test_unordered_sequencer.py
+-rw-rw-r--   0 root         (0)     1003    17769 2021-11-10 16:49:33.000000 google-cloud-pubsub-2.9.0/tests/unit/pubsub_v1/publisher/test_flow_controller.py
+-rw-rw-r--   0 root         (0)     1003     1325 2021-11-10 16:49:33.000000 google-cloud-pubsub-2.9.0/tests/unit/pubsub_v1/publisher/test_futures_publisher.py
+-rw-rw-r--   0 root         (0)     1003    22464 2021-11-10 16:49:33.000000 google-cloud-pubsub-2.9.0/tests/unit/pubsub_v1/publisher/test_publisher_client.py
+drwxr-sr-x   0 root         (0)     1003        0 2021-11-10 16:52:04.074392 google-cloud-pubsub-2.9.0/tests/unit/pubsub_v1/subscriber/
+-rw-rw-r--   0 root         (0)     1003     9832 2021-11-10 16:49:33.000000 google-cloud-pubsub-2.9.0/tests/unit/pubsub_v1/subscriber/test_dispatcher.py
+-rw-rw-r--   0 root         (0)     1003     2481 2021-11-10 16:49:33.000000 google-cloud-pubsub-2.9.0/tests/unit/pubsub_v1/subscriber/test_futures_subscriber.py
+-rw-rw-r--   0 root         (0)     1003     4226 2021-11-10 16:49:33.000000 google-cloud-pubsub-2.9.0/tests/unit/pubsub_v1/subscriber/test_heartbeater.py
+-rw-rw-r--   0 root         (0)     1003     3888 2021-11-10 16:49:33.000000 google-cloud-pubsub-2.9.0/tests/unit/pubsub_v1/subscriber/test_helper_threads.py
+-rw-rw-r--   0 root         (0)     1003     2378 2021-11-10 16:49:33.000000 google-cloud-pubsub-2.9.0/tests/unit/pubsub_v1/subscriber/test_histogram.py
+-rw-rw-r--   0 root         (0)     1003     8151 2021-11-10 16:49:33.000000 google-cloud-pubsub-2.9.0/tests/unit/pubsub_v1/subscriber/test_leaser.py
+-rw-rw-r--   0 root         (0)     1003     5800 2021-11-10 16:49:33.000000 google-cloud-pubsub-2.9.0/tests/unit/pubsub_v1/subscriber/test_message.py
+-rw-rw-r--   0 root         (0)     1003     8802 2021-11-10 16:49:33.000000 google-cloud-pubsub-2.9.0/tests/unit/pubsub_v1/subscriber/test_messages_on_hold.py
+-rw-rw-r--   0 root         (0)     1003     5542 2021-11-10 16:49:33.000000 google-cloud-pubsub-2.9.0/tests/unit/pubsub_v1/subscriber/test_scheduler.py
+-rw-rw-r--   0 root         (0)     1003    38052 2021-11-10 16:49:33.000000 google-cloud-pubsub-2.9.0/tests/unit/pubsub_v1/subscriber/test_streaming_pull_manager.py
+-rw-rw-r--   0 root         (0)     1003     9347 2021-11-10 16:49:33.000000 google-cloud-pubsub-2.9.0/tests/unit/pubsub_v1/subscriber/test_subscriber_client.py
+-rw-rw-r--   0 root         (0)     1003     2108 2021-11-10 16:49:33.000000 google-cloud-pubsub-2.9.0/tests/unit/pubsub_v1/test__gapic.py
+-rw-rw-r--   0 root         (0)     1003     5357 2021-11-10 16:49:33.000000 google-cloud-pubsub-2.9.0/tests/unit/pubsub_v1/test_futures.py
+-rw-rw-r--   0 root         (0)     1003      865 2021-11-10 16:49:33.000000 google-cloud-pubsub-2.9.0/tests/unit/test_pubsub.py
```

### Comparing `google-cloud-pubsub-2.8.0/LICENSE` & `google-cloud-pubsub-2.9.0/LICENSE`

 * *Files identical despite different names*

### Comparing `google-cloud-pubsub-2.8.0/MANIFEST.in` & `google-cloud-pubsub-2.9.0/MANIFEST.in`

 * *Files identical despite different names*

### Comparing `google-cloud-pubsub-2.8.0/PKG-INFO` & `google-cloud-pubsub-2.9.0/PKG-INFO`

 * *Files 3% similar despite different names*

```diff
@@ -1,24 +1,26 @@
 Metadata-Version: 2.1
 Name: google-cloud-pubsub
-Version: 2.8.0
+Version: 2.9.0
 Summary: Google Cloud Pub/Sub API client library
 Home-page: https://github.com/googleapis/python-pubsub
 Author: Google LLC
 Author-email: googleapis-packages@google.com
 License: Apache 2.0
 Platform: Posix; MacOS X; Windows
 Classifier: Development Status :: 5 - Production/Stable
 Classifier: Intended Audience :: Developers
 Classifier: License :: OSI Approved :: Apache Software License
 Classifier: Programming Language :: Python
 Classifier: Programming Language :: Python :: 3
 Classifier: Programming Language :: Python :: 3.6
 Classifier: Programming Language :: Python :: 3.7
 Classifier: Programming Language :: Python :: 3.8
+Classifier: Programming Language :: Python :: 3.9
+Classifier: Programming Language :: Python :: 3.10
 Classifier: Operating System :: OS Independent
 Classifier: Topic :: Internet
 Requires-Python: >=3.6
 License-File: LICENSE
 
 Python Client for Google Cloud Pub / Sub
 ========================================
@@ -38,15 +40,15 @@
 receivers, Google Cloud Pub/Sub allows developers to communicate between
 independently written applications.
 
 - `Product Documentation`_
 - `Client Library Documentation`_
 
 .. |GA| image:: https://img.shields.io/badge/support-GA-gold.svg
-   :target: https://github.com/googleapis/google-cloud-python/blob/master/README.rst#general-availability
+   :target: https://github.com/googleapis/google-cloud-python/blob/main/README.rst#general-availability
 .. |pypi| image:: https://img.shields.io/pypi/v/google-cloud-pubsub.svg
    :target: https://pypi.org/project/google-cloud-pubsub/
 .. |versions| image:: https://img.shields.io/pypi/pyversions/google-cloud-pubsub.svg
    :target: https://pypi.org/project/google-cloud-pubsub/
 .. _Google Cloud Pub / Sub: https://cloud.google.com/pubsub/
 .. _Product Documentation: https://cloud.google.com/pubsub/docs
 .. _Client Library Documentation: https://googleapis.dev/python/pubsub/latest
@@ -232,15 +234,15 @@
 Contributing
 ------------
 
 Contributions to this library are always welcome and highly encouraged.
 
 See the `CONTRIBUTING doc`_ for more information on how to get started.
 
-.. _CONTRIBUTING doc: https://github.com/googleapis/google-cloud-python/blob/master/CONTRIBUTING.rst
+.. _CONTRIBUTING doc: https://github.com/googleapis/google-cloud-python/blob/main/CONTRIBUTING.rst
 
 Community
 ---------
 
 Google Cloud Platform Python developers hang out in `Slack`_ in the ``#python``
 channel, click here to `get an invitation`_.
 
@@ -248,10 +250,10 @@
 .. _get an invitation: https://gcp-slack.appspot.com/
 
 License
 -------
 
 Apache 2.0 - See `the LICENSE`_ for more information.
 
-.. _the LICENSE: https://github.com/googleapis/google-cloud-python/blob/master/LICENSE
+.. _the LICENSE: https://github.com/googleapis/google-cloud-python/blob/main/LICENSE
```

### Comparing `google-cloud-pubsub-2.8.0/README.rst` & `google-cloud-pubsub-2.9.0/README.rst`

 * *Files 2% similar despite different names*

```diff
@@ -16,15 +16,15 @@
 receivers, Google Cloud Pub/Sub allows developers to communicate between
 independently written applications.
 
 - `Product Documentation`_
 - `Client Library Documentation`_
 
 .. |GA| image:: https://img.shields.io/badge/support-GA-gold.svg
-   :target: https://github.com/googleapis/google-cloud-python/blob/master/README.rst#general-availability
+   :target: https://github.com/googleapis/google-cloud-python/blob/main/README.rst#general-availability
 .. |pypi| image:: https://img.shields.io/pypi/v/google-cloud-pubsub.svg
    :target: https://pypi.org/project/google-cloud-pubsub/
 .. |versions| image:: https://img.shields.io/pypi/pyversions/google-cloud-pubsub.svg
    :target: https://pypi.org/project/google-cloud-pubsub/
 .. _Google Cloud Pub / Sub: https://cloud.google.com/pubsub/
 .. _Product Documentation: https://cloud.google.com/pubsub/docs
 .. _Client Library Documentation: https://googleapis.dev/python/pubsub/latest
@@ -210,15 +210,15 @@
 Contributing
 ------------
 
 Contributions to this library are always welcome and highly encouraged.
 
 See the `CONTRIBUTING doc`_ for more information on how to get started.
 
-.. _CONTRIBUTING doc: https://github.com/googleapis/google-cloud-python/blob/master/CONTRIBUTING.rst
+.. _CONTRIBUTING doc: https://github.com/googleapis/google-cloud-python/blob/main/CONTRIBUTING.rst
 
 Community
 ---------
 
 Google Cloud Platform Python developers hang out in `Slack`_ in the ``#python``
 channel, click here to `get an invitation`_.
 
@@ -226,8 +226,8 @@
 .. _get an invitation: https://gcp-slack.appspot.com/
 
 License
 -------
 
 Apache 2.0 - See `the LICENSE`_ for more information.
 
-.. _the LICENSE: https://github.com/googleapis/google-cloud-python/blob/master/LICENSE
+.. _the LICENSE: https://github.com/googleapis/google-cloud-python/blob/main/LICENSE
```

### Comparing `google-cloud-pubsub-2.8.0/google/__init__.py` & `google-cloud-pubsub-2.9.0/google/__init__.py`

 * *Files identical despite different names*

### Comparing `google-cloud-pubsub-2.8.0/google/cloud/__init__.py` & `google-cloud-pubsub-2.9.0/google/cloud/__init__.py`

 * *Files identical despite different names*

### Comparing `google-cloud-pubsub-2.8.0/google/cloud/pubsub/__init__.py` & `google-cloud-pubsub-2.9.0/google/cloud/pubsub/__init__.py`

 * *Files identical despite different names*

### Comparing `google-cloud-pubsub-2.8.0/google/cloud/pubsub_v1/__init__.py` & `google-cloud-pubsub-2.9.0/google/cloud/pubsub_v1/__init__.py`

 * *Files identical despite different names*

### Comparing `google-cloud-pubsub-2.8.0/google/cloud/pubsub_v1/_gapic.py` & `google-cloud-pubsub-2.9.0/google/cloud/pubsub_v1/_gapic.py`

 * *Files 8% similar despite different names*

```diff
@@ -11,40 +11,43 @@
 # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 # See the License for the specific language governing permissions and
 # limitations under the License.
 
 from __future__ import absolute_import
 
 import functools
+from typing import Callable, Container, Type
 
 
-def add_methods(source_class, denylist=()):
+def add_methods(
+    source_class: Type, denylist: Container[str] = ()
+) -> Callable[[Type], Type]:
     """Add wrapped versions of the `api` member's methods to the class.
 
     Any methods passed in `denylist` are not added.
     Additionally, any methods explicitly defined on the wrapped class are
     not added.
     """
 
-    def wrap(wrapped_fx, lookup_fx):
+    def wrap(wrapped_fx: Callable, lookup_fx: Callable):
         """Wrap a GAPIC method; preserve its name and docstring."""
         # If this is a static or class method, then we do *not*
         # send self as the first argument.
         #
         # For instance methods, we need to send self.api rather
         # than self, since that is where the actual methods were declared.
 
         if isinstance(lookup_fx, (classmethod, staticmethod)):
             fx = lambda *a, **kw: wrapped_fx(*a, **kw)  # noqa
             return staticmethod(functools.wraps(wrapped_fx)(fx))
         else:
             fx = lambda self, *a, **kw: wrapped_fx(self.api, *a, **kw)  # noqa
             return functools.wraps(wrapped_fx)(fx)
 
-    def actual_decorator(cls):
+    def actual_decorator(cls: Type) -> Type:
         # Reflectively iterate over most of the methods on the source class
         # (the GAPIC) and make wrapped versions available on this client.
         for name in dir(source_class):
             # Ignore all private and magic methods.
             if name.startswith("_"):
                 continue
```

### Comparing `google-cloud-pubsub-2.8.0/google/cloud/pubsub_v1/exceptions.py` & `google-cloud-pubsub-2.9.0/google/cloud/pubsub_v1/exceptions.py`

 * *Files identical despite different names*

### Comparing `google-cloud-pubsub-2.8.0/google/cloud/pubsub_v1/futures.py` & `google-cloud-pubsub-2.9.0/google/cloud/pubsub_v1/futures.py`

 * *Files 4% similar despite different names*

```diff
@@ -11,48 +11,46 @@
 # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 # See the License for the specific language governing permissions and
 # limitations under the License.
 
 from __future__ import absolute_import
 
 import concurrent.futures
+from typing import Any, NoReturn
 
 import google.api_core.future
 
 
 class Future(concurrent.futures.Future, google.api_core.future.Future):
     """Encapsulation of the asynchronous execution of an action.
 
     This object is returned from asychronous Pub/Sub calls, and is the
     interface to determine the status of those calls.
 
     This object should not be created directly, but is returned by other
     methods in this library.
     """
 
-    def running(self):
-        """Return ``True`` if the associated Pub/Sub action has not yet completed.
-
-        Returns: bool:
-        """
+    def running(self) -> bool:
+        """Return ``True`` if the associated Pub/Sub action has not yet completed."""
         return not self.done()
 
-    def set_running_or_notify_cancel(self):
+    def set_running_or_notify_cancel(self) -> NoReturn:
         raise NotImplementedError(
             "Only used by executors from `concurrent.futures` package."
         )
 
-    def set_result(self, result):
+    def set_result(self, result: Any):
         """Set the return value of work associated with the future.
 
         Do not use this method, it should only be used internally by the library and its
         unit tests.
         """
         return super().set_result(result=result)
 
-    def set_exception(self, exception):
+    def set_exception(self, exception: Exception):
         """Set the result of the future as being the given exception.
 
         Do not use this method, it should only be used internally by the library and its
         unit tests.
         """
         return super().set_exception(exception=exception)
```

### Comparing `google-cloud-pubsub-2.8.0/google/cloud/pubsub_v1/proto/pubsub.proto` & `google-cloud-pubsub-2.9.0/google/cloud/pubsub_v1/proto/pubsub.proto`

 * *Files identical despite different names*

### Comparing `google-cloud-pubsub-2.8.0/google/cloud/pubsub_v1/proto/schema.proto` & `google-cloud-pubsub-2.9.0/google/cloud/pubsub_v1/proto/schema.proto`

 * *Files identical despite different names*

### Comparing `google-cloud-pubsub-2.8.0/google/cloud/pubsub_v1/publisher/__init__.py` & `google-cloud-pubsub-2.9.0/google/cloud/pubsub_v1/publisher/__init__.py`

 * *Files identical despite different names*

### Comparing `google-cloud-pubsub-2.8.0/google/cloud/pubsub_v1/publisher/_batch/base.py` & `google-cloud-pubsub-2.9.0/google/cloud/pubsub_v1/publisher/_batch/base.py`

 * *Files 8% similar despite different names*

```diff
@@ -12,14 +12,22 @@
 # See the License for the specific language governing permissions and
 # limitations under the License.
 
 from __future__ import absolute_import
 
 import abc
 import enum
+import typing
+from typing import Optional, Sequence
+
+
+if typing.TYPE_CHECKING:  # pragma: NO COVER
+    from google.cloud import pubsub_v1
+    from google.cloud.pubsub_v1 import types
+    from google.pubsub_v1 import types as gapic_types
 
 
 class Batch(metaclass=abc.ABCMeta):
     """The base batching class for Pub/Sub publishing.
 
     Although the :class:`~.pubsub_v1.publisher.batch.thread.Batch` class, based
     on :class:`threading.Thread`, is fine for most cases, advanced
@@ -46,98 +54,102 @@
 
     def __len__(self):
         """Return the number of messages currently in the batch."""
         return len(self.messages)
 
     @staticmethod
     @abc.abstractmethod
-    def make_lock():  # pragma: NO COVER
+    def make_lock() -> None:  # pragma: NO COVER
         """Return a lock in the chosen concurrency model.
 
         Returns:
             ContextManager: A newly created lock.
         """
         raise NotImplementedError
 
     @property
     @abc.abstractmethod
-    def messages(self):  # pragma: NO COVER
+    def messages(self) -> Sequence["gapic_types.PubsubMessage"]:  # pragma: NO COVER
         """Return the messages currently in the batch.
 
         Returns:
-            Sequence: The messages currently in the batch.
+            The messages currently in the batch.
         """
         raise NotImplementedError
 
     @property
     @abc.abstractmethod
-    def size(self):  # pragma: NO COVER
+    def size(self) -> int:  # pragma: NO COVER
         """Return the total size of all of the messages currently in the batch.
 
         The size includes any overhead of the actual ``PublishRequest`` that is
         sent to the backend.
 
         Returns:
             int: The total size of all of the messages currently
                  in the batch (including the request overhead), in bytes.
         """
         raise NotImplementedError
 
     @property
     @abc.abstractmethod
-    def settings(self):  # pragma: NO COVER
+    def settings(self) -> "types.BatchSettings":  # pragma: NO COVER
         """Return the batch settings.
 
         Returns:
-            ~.pubsub_v1.types.BatchSettings: The batch settings. These are
-                considered immutable once the batch has been opened.
+            The batch settings. These are considered immutable once the batch has
+            been opened.
         """
         raise NotImplementedError
 
     @property
     @abc.abstractmethod
-    def status(self):  # pragma: NO COVER
+    def status(self) -> "BatchStatus":  # pragma: NO COVER
         """Return the status of this batch.
 
         Returns:
-            str: The status of this batch. All statuses are human-readable,
-                all-lowercase strings. The ones represented in the
-                :class:`BaseBatch.Status` enum are special, but other statuses
-                are permitted.
+            The status of this batch. All statuses are human-readable, all-lowercase
+            strings. The ones represented in the :class:`BaseBatch.Status` enum are
+            special, but other statuses are permitted.
         """
         raise NotImplementedError
 
-    def cancel(self, cancellation_reason):  # pragma: NO COVER
+    def cancel(
+        self, cancellation_reason: "BatchCancellationReason"
+    ) -> None:  # pragma: NO COVER
         """Complete pending futures with an exception.
 
         This method must be called before publishing starts (ie: while the
         batch is still accepting messages.)
 
         Args:
-            cancellation_reason (BatchCancellationReason): The reason why this
-                batch has been cancelled.
+            cancellation_reason:
+                The reason why this batch has been cancelled.
         """
         raise NotImplementedError
 
     @abc.abstractmethod
-    def publish(self, message):  # pragma: NO COVER
+    def publish(
+        self, message: "gapic_types.PubsubMessage"
+    ) -> Optional["pubsub_v1.publisher.futures.Future"]:  # pragma: NO COVER
         """Publish a single message.
 
         Add the given message to this object; this will cause it to be
         published once the batch either has enough messages or a sufficient
         period of time has elapsed.
 
         This method is called by :meth:`~.PublisherClient.publish`.
 
         Args:
-            message (~.pubsub_v1.types.PubsubMessage): The Pub/Sub message.
+            message: The Pub/Sub message.
 
         Returns:
-            ~google.api_core.future.Future: An object conforming to the
-                :class:`concurrent.futures.Future` interface.
+            An object conforming to the :class:`concurrent.futures.Future` interface.
+            If :data:`None` is returned, that signals that the batch cannot
+            accept a message.
         """
         raise NotImplementedError
 
 
 class BatchStatus(str, enum.Enum):
     """An enum-like class representing valid statuses for a batch."""
```

### Comparing `google-cloud-pubsub-2.8.0/google/cloud/pubsub_v1/publisher/_batch/thread.py` & `google-cloud-pubsub-2.9.0/google/cloud/pubsub_v1/publisher/_batch/thread.py`

 * *Files 5% similar despite different names*

```diff
@@ -13,22 +13,30 @@
 # limitations under the License.
 
 from __future__ import absolute_import
 
 import logging
 import threading
 import time
+import typing
+from typing import Any, Callable, Optional, Sequence
 
 import google.api_core.exceptions
 from google.api_core import gapic_v1
 from google.cloud.pubsub_v1.publisher import exceptions
 from google.cloud.pubsub_v1.publisher import futures
 from google.cloud.pubsub_v1.publisher._batch import base
 from google.pubsub_v1 import types as gapic_types
 
+if typing.TYPE_CHECKING:  # pragma: NO COVER
+    from google import api_core
+    from google.cloud import pubsub_v1
+    from google.cloud.pubsub_v1 import types
+    from google.cloud.pubsub_v1 import PublisherClient
+
 
 _LOGGER = logging.getLogger(__name__)
 _CAN_COMMIT = (base.BatchStatus.ACCEPTING_MESSAGES, base.BatchStatus.STARTING)
 _SERVER_PUBLISH_MAX_BYTES = 10 * 1000 * 1000  # max accepted size of PublishRequest
 
 _raw_proto_pubbsub_message = gapic_types.PubsubMessage.pb()
 
@@ -52,44 +60,44 @@
     :class:`~.pubsub_v1.PublisherClient`.
 
     Any properties or methods on this class which are not defined in
     :class:`~.pubsub_v1.publisher.batch.BaseBatch` should be considered
     implementation details.
 
     Args:
-        client (~.pubsub_v1.PublisherClient): The publisher client used to
-            create this batch.
-        topic (str): The topic. The format for this is
-            ``projects/{project}/topics/{topic}``.
-        settings (~.pubsub_v1.types.BatchSettings): The settings for batch
-            publishing. These should be considered immutable once the batch
-            has been opened.
-        batch_done_callback (Callable[[bool], Any]): Callback called when the
-            response for a batch publish has been received. Called with one
-            boolean argument: successfully published or a permanent error
-            occurred. Temporary errors are not surfaced because they are retried
+        client:
+            The publisher client used to create this batch.
+        topic:
+            The topic. The format for this is ``projects/{project}/topics/{topic}``.
+        settings:
+            The settings for batch publishing. These should be considered immutable
+            once the batch has been opened.
+        batch_done_callback:
+            Callback called when the response for a batch publish has been received.
+            Called with one boolean argument: successfully published or a permanent
+            error occurred. Temporary errors are not surfaced because they are retried
             at a lower level.
-        commit_when_full (bool): Whether to commit the batch when the batch
-            is full.
-        commit_retry (Optional[google.api_core.retry.Retry]): Designation of what
-            errors, if any, should be retried when commiting the batch. If not
-            provided, a default retry is used.
-        commit_timeout (:class:`~.pubsub_v1.types.TimeoutType`):
-                The timeout to apply when commiting the batch. If not provided, a
-                default timeout is used.
+        commit_when_full:
+            Whether to commit the batch when the batch is full.
+        commit_retry:
+            Designation of what errors, if any, should be retried when commiting
+            the batch. If not provided, a default retry is used.
+        commit_timeout:
+            The timeout to apply when commiting the batch. If not provided, a default
+            timeout is used.
     """
 
     def __init__(
         self,
-        client,
-        topic,
-        settings,
-        batch_done_callback=None,
-        commit_when_full=True,
-        commit_retry=gapic_v1.method.DEFAULT,
+        client: "PublisherClient",
+        topic: str,
+        settings: "types.BatchSettings",
+        batch_done_callback: Callable[[bool], Any] = None,
+        commit_when_full: bool = True,
+        commit_retry: "api_core.retry.Retry" = gapic_v1.method.DEFAULT,
         commit_timeout: gapic_types.TimeoutType = gapic_v1.method.DEFAULT,
     ):
         self._client = client
         self._topic = topic
         self._settings = settings
         self._batch_done_callback = batch_done_callback
         self._commit_when_full = commit_when_full
@@ -109,87 +117,86 @@
         self._base_request_size = gapic_types.PublishRequest(topic=topic)._pb.ByteSize()
         self._size = self._base_request_size
 
         self._commit_retry = commit_retry
         self._commit_timeout = commit_timeout
 
     @staticmethod
-    def make_lock():
+    def make_lock() -> threading.Lock:
         """Return a threading lock.
 
         Returns:
-            _thread.Lock: A newly created lock.
+            A newly created lock.
         """
         return threading.Lock()
 
     @property
-    def client(self):
-        """~.pubsub_v1.client.PublisherClient: A publisher client."""
+    def client(self) -> "PublisherClient":
+        """A publisher client."""
         return self._client
 
     @property
-    def messages(self):
-        """Sequence: The messages currently in the batch."""
+    def messages(self) -> Sequence[gapic_types.PubsubMessage]:
+        """The messages currently in the batch."""
         return self._messages
 
     @property
-    def settings(self):
+    def settings(self) -> "types.BatchSettings":
         """Return the batch settings.
 
         Returns:
-            ~.pubsub_v1.types.BatchSettings: The batch settings. These are
-                considered immutable once the batch has been opened.
+            The batch settings. These are considered immutable once the batch has
+            been opened.
         """
         return self._settings
 
     @property
-    def size(self):
+    def size(self) -> int:
         """Return the total size of all of the messages currently in the batch.
 
         The size includes any overhead of the actual ``PublishRequest`` that is
         sent to the backend.
 
         Returns:
-            int: The total size of all of the messages currently
-                 in the batch (including the request overhead), in bytes.
+            The total size of all of the messages currently in the batch (including
+            the request overhead), in bytes.
         """
         return self._size
 
     @property
-    def status(self):
+    def status(self) -> base.BatchStatus:
         """Return the status of this batch.
 
         Returns:
-            str: The status of this batch. All statuses are human-readable,
-                all-lowercase strings.
+            The status of this batch. All statuses are human-readable, all-lowercase
+            strings.
         """
         return self._status
 
-    def cancel(self, cancellation_reason):
+    def cancel(self, cancellation_reason: base.BatchCancellationReason) -> None:
         """Complete pending futures with an exception.
 
         This method must be called before publishing starts (ie: while the
         batch is still accepting messages.)
 
         Args:
-            cancellation_reason (BatchCancellationReason): The reason why this
-                batch has been cancelled.
+            The reason why this batch has been cancelled.
         """
 
         with self._state_lock:
             assert (
                 self._status == base.BatchStatus.ACCEPTING_MESSAGES
             ), "Cancel should not be called after sending has started."
 
             exc = RuntimeError(cancellation_reason.value)
             for future in self._futures:
                 future.set_exception(exc)
             self._status = base.BatchStatus.ERROR
 
-    def commit(self):
+    def commit(self) -> None:
         """Actually publish all of the messages on the active batch.
 
         .. note::
 
             This method is non-blocking. It opens a new thread, which calls
             :meth:`_commit`, which does block.
 
@@ -206,25 +213,25 @@
             if self._status == base.BatchStatus.ACCEPTING_MESSAGES:
                 self._status = base.BatchStatus.STARTING
             else:
                 return
 
         self._start_commit_thread()
 
-    def _start_commit_thread(self):
+    def _start_commit_thread(self) -> None:
         """Start a new thread to actually handle the commit."""
         # NOTE: If the thread is *not* a daemon, a memory leak exists due to a CPython issue.
         # https://github.com/googleapis/python-pubsub/issues/395#issuecomment-829910303
         # https://github.com/googleapis/python-pubsub/issues/395#issuecomment-830092418
         commit_thread = threading.Thread(
             name="Thread-CommitBatchPublisher", target=self._commit, daemon=True
         )
         commit_thread.start()
 
-    def _commit(self):
+    def _commit(self) -> None:
         """Actually publish all of the messages on the active batch.
 
         This moves the batch out from being the active batch to an in progress
         batch on the publisher, and then the batch is discarded upon
         completion.
 
         .. note::
@@ -316,32 +323,33 @@
                 len(response.message_ids),
                 len(self._futures),
             )
 
         if self._batch_done_callback is not None:
             self._batch_done_callback(batch_transport_succeeded)
 
-    def publish(self, message):
+    def publish(
+        self, message: gapic_types.PubsubMessage
+    ) -> Optional["pubsub_v1.publisher.futures.Future"]:
         """Publish a single message.
 
         Add the given message to this object; this will cause it to be
         published once the batch either has enough messages or a sufficient
         period of time has elapsed. If the batch is full or the commit is
         already in progress, the method does not do anything.
 
         This method is called by :meth:`~.PublisherClient.publish`.
 
         Args:
-            message (~.pubsub_v1.types.PubsubMessage): The Pub/Sub message.
+            message: The Pub/Sub message.
 
         Returns:
-            Optional[~google.api_core.future.Future]: An object conforming to
-            the :class:`~concurrent.futures.Future` interface or :data:`None`.
-            If :data:`None` is returned, that signals that the batch cannot
-            accept a message.
+            An object conforming to the :class:`~concurrent.futures.Future` interface
+            or :data:`None`. If :data:`None` is returned, that signals that the batch
+            cannot accept a message.
 
         Raises:
             pubsub_v1.publisher.exceptions.MessageTooLargeError: If publishing
                 the ``message`` would exceed the max size limit on the backend.
         """
 
         # Coerce the type, just in case.
@@ -394,9 +402,9 @@
         # Try to commit, but it must be **without** the lock held, since
         # ``commit()`` will try to obtain the lock.
         if self._commit_when_full and overflow:
             self.commit()
 
         return future
 
-    def _set_status(self, status):
+    def _set_status(self, status: base.BatchStatus):
         self._status = status
```

### Comparing `google-cloud-pubsub-2.8.0/google/cloud/pubsub_v1/publisher/_sequencer/base.py` & `google-cloud-pubsub-2.9.0/google/cloud/pubsub_v1/publisher/_sequencer/base.py`

 * *Files 12% similar despite different names*

```diff
@@ -11,67 +11,72 @@
 # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 # See the License for the specific language governing permissions and
 # limitations under the License.
 
 from __future__ import absolute_import
 
 import abc
+import typing
 
 from google.api_core import gapic_v1
 from google.pubsub_v1 import types as gapic_types
 
+if typing.TYPE_CHECKING:  # pragma: NO COVER
+    from concurrent import futures
+    from google.api_core import retry
+
 
 class Sequencer(metaclass=abc.ABCMeta):
     """The base class for sequencers for Pub/Sub publishing. A sequencer
        sequences messages to be published.
     """
 
     @staticmethod
     @abc.abstractmethod
-    def is_finished(self):  # pragma: NO COVER
+    def is_finished(self) -> bool:  # pragma: NO COVER
         """ Whether the sequencer is finished and should be cleaned up.
 
             Returns:
                 bool: Whether the sequencer is finished and should be cleaned up.
         """
         raise NotImplementedError
 
     @staticmethod
     @abc.abstractmethod
-    def unpause(self, message):  # pragma: NO COVER
+    def unpause(self) -> None:  # pragma: NO COVER
         """ Unpauses this sequencer.
 
         Raises:
             RuntimeError:
                 If called when the sequencer has not been paused.
         """
         raise NotImplementedError
 
     @staticmethod
     @abc.abstractmethod
     def publish(
         self,
-        message,
-        retry=None,
+        message: gapic_types.PubsubMessage,
+        retry: "retry.Retry" = None,
         timeout: gapic_types.TimeoutType = gapic_v1.method.DEFAULT,
-    ):  # pragma: NO COVER
+    ) -> "futures.Future":  # pragma: NO COVER
         """ Publish message for this ordering key.
 
         Args:
-            message (~.pubsub_v1.types.PubsubMessage):
+            message:
                 The Pub/Sub message.
-            retry (Optional[google.api_core.retry.Retry]):
+            retry:
                 The retry settings to apply when publishing the message.
-            timeout (:class:`~.pubsub_v1.types.TimeoutType`):
+            timeout:
                 The timeout to apply when publishing the message.
 
         Returns:
             A class instance that conforms to Python Standard library's
-            :class:`~concurrent.futures.Future` interface (but not an
-            instance of that class). The future might return immediately with a
+            :class:`~concurrent.futures.Future` interface. The future might return
+            immediately with a
             `pubsub_v1.publisher.exceptions.PublishToPausedOrderingKeyException`
             if the ordering key is paused.  Otherwise, the future tracks the
             lifetime of the message publish.
 
         Raises:
             RuntimeError:
                 If called after this sequencer has been stopped, either by
```

### Comparing `google-cloud-pubsub-2.8.0/google/cloud/pubsub_v1/publisher/_sequencer/ordered_sequencer.py` & `google-cloud-pubsub-2.9.0/google/cloud/pubsub_v1/publisher/_sequencer/ordered_sequencer.py`

 * *Files 2% similar despite different names*

```diff
@@ -12,21 +12,28 @@
 # See the License for the specific language governing permissions and
 # limitations under the License.
 
 import enum
 import collections
 import concurrent.futures as futures
 import threading
+import typing
+from typing import Iterable, Sequence
 
 from google.api_core import gapic_v1
 from google.cloud.pubsub_v1.publisher import exceptions
 from google.cloud.pubsub_v1.publisher._sequencer import base as sequencer_base
 from google.cloud.pubsub_v1.publisher._batch import base as batch_base
 from google.pubsub_v1 import types as gapic_types
 
+if typing.TYPE_CHECKING:  # pragma: NO COVER
+    from google.api_core import retry
+    from google.cloud.pubsub_v1 import PublisherClient
+    from google.cloud.pubsub_v1.publisher import _batch
+
 
 class _OrderedSequencerStatus(str, enum.Enum):
     """An enum-like class representing valid statuses for an OrderedSequencer.
 
     Starting state: ACCEPTING_MESSAGES
     Valid transitions:
       ACCEPTING_MESSAGES -> PAUSED (on permanent error)
@@ -73,44 +80,45 @@
         A sequencer always has at least one batch in it, unless paused or stopped.
         When no batches remain, the |publishes_done_callback| is called so the
         client can perform cleanup.
 
         Public methods are thread-safe.
 
         Args:
-            client (~.pubsub_v1.PublisherClient): The publisher client used to
-                create this sequencer.
-            topic (str): The topic. The format for this is
-                ``projects/{project}/topics/{topic}``.
-            ordering_key (str): The ordering key for this sequencer.
+            client:
+                The publisher client used to create this sequencer.
+            topic:
+                The topic. The format for this is ``projects/{project}/topics/{topic}``.
+            ordering_key:
+                The ordering key for this sequencer.
     """
 
-    def __init__(self, client, topic, ordering_key):
+    def __init__(self, client: "PublisherClient", topic: str, ordering_key: str):
         self._client = client
         self._topic = topic
         self._ordering_key = ordering_key
         # Guards the variables below
         self._state_lock = threading.Lock()
         # Batches ordered from first (head/left) to last (right/tail).
         # Invariant: always has at least one batch after the first publish,
         # unless paused or stopped.
         self._ordered_batches = collections.deque()
         # See _OrderedSequencerStatus for valid state transitions.
         self._state = _OrderedSequencerStatus.ACCEPTING_MESSAGES
 
-    def is_finished(self):
+    def is_finished(self) -> bool:
         """ Whether the sequencer is finished and should be cleaned up.
 
             Returns:
-                bool: Whether the sequencer is finished and should be cleaned up.
+                Whether the sequencer is finished and should be cleaned up.
         """
         with self._state_lock:
             return self._state == _OrderedSequencerStatus.FINISHED
 
-    def stop(self):
+    def stop(self) -> None:
         """ Permanently stop this sequencer.
 
             This differs from pausing, which may be resumed. Immediately commits
             the first batch and cancels the rest.
 
             Raises:
                 RuntimeError:
@@ -129,15 +137,15 @@
                 # of batches.
                 while len(self._ordered_batches) > 1:
                     # Pops from the tail until it leaves only the head in the
                     # deque.
                     batch = self._ordered_batches.pop()
                     batch.cancel(batch_base.BatchCancellationReason.CLIENT_STOPPED)
 
-    def commit(self):
+    def commit(self) -> None:
         """ Commit the first batch, if unpaused.
 
             If paused or no batches exist, this method does nothing.
 
             Raises:
                 RuntimeError:
                     If called after stop() has already been called.
@@ -147,15 +155,15 @@
                 raise RuntimeError("Ordered sequencer already stopped.")
 
             if self._state != _OrderedSequencerStatus.PAUSED and self._ordered_batches:
                 # It's okay to commit the same batch more than once. The
                 # operation is idempotent.
                 self._ordered_batches[0].commit()
 
-    def _batch_done_callback(self, success):
+    def _batch_done_callback(self, success: bool) -> None:
         """ Deal with completion of a batch.
 
             Called when a batch has finished publishing, with either a success
             or a failure. (Temporary failures are retried infinitely when
             ordering keys are enabled.)
         """
         ensure_cleanup_and_commit_timer_runs = False
@@ -195,15 +203,15 @@
             else:
                 # Unrecoverable error detected
                 self._pause()
 
         if ensure_cleanup_and_commit_timer_runs:
             self._client.ensure_cleanup_and_commit_timer_runs()
 
-    def _pause(self):
+    def _pause(self) -> None:
         """ Pause this sequencer: set state to paused, cancel all batches, and
             clear the list of ordered batches.
 
             _state_lock must be taken before calling this method.
         """
         assert (
             self._state != _OrderedSequencerStatus.FINISHED
@@ -211,64 +219,64 @@
         self._state = _OrderedSequencerStatus.PAUSED
         for batch in self._ordered_batches:
             batch.cancel(
                 batch_base.BatchCancellationReason.PRIOR_ORDERED_MESSAGE_FAILED
             )
         self._ordered_batches.clear()
 
-    def unpause(self):
+    def unpause(self) -> None:
         """ Unpause this sequencer.
 
         Raises:
             RuntimeError:
                 If called when the ordering key has not been paused.
         """
         with self._state_lock:
             if self._state != _OrderedSequencerStatus.PAUSED:
                 raise RuntimeError("Ordering key is not paused.")
             self._state = _OrderedSequencerStatus.ACCEPTING_MESSAGES
 
     def _create_batch(
         self,
-        commit_retry=gapic_v1.method.DEFAULT,
+        commit_retry: "retry.Retry" = gapic_v1.method.DEFAULT,
         commit_timeout: gapic_types.TimeoutType = gapic_v1.method.DEFAULT,
-    ):
+    ) -> "_batch.thread.Batch":
         """ Create a new batch using the client's batch class and other stored
             settings.
 
         Args:
-            commit_retry (Optional[google.api_core.retry.Retry]):
+            commit_retry:
                 The retry settings to apply when publishing the batch.
-            commit_timeout (:class:`~.pubsub_v1.types.TimeoutType`):
+            commit_timeout:
                 The timeout to apply when publishing the batch.
         """
         return self._client._batch_class(
             client=self._client,
             topic=self._topic,
             settings=self._client.batch_settings,
             batch_done_callback=self._batch_done_callback,
             commit_when_full=False,
             commit_retry=commit_retry,
             commit_timeout=commit_timeout,
         )
 
     def publish(
         self,
-        message,
-        retry=gapic_v1.method.DEFAULT,
+        message: gapic_types.PubsubMessage,
+        retry: "retry.Retry" = gapic_v1.method.DEFAULT,
         timeout: gapic_types.TimeoutType = gapic_v1.method.DEFAULT,
-    ):
+    ) -> futures.Future:
         """ Publish message for this ordering key.
 
         Args:
-            message (~.pubsub_v1.types.PubsubMessage):
+            message:
                 The Pub/Sub message.
-            retry (Optional[google.api_core.retry.Retry]):
+            retry:
                 The retry settings to apply when publishing the message.
-            timeout (:class:`~.pubsub_v1.types.TimeoutType`):
+            timeout:
                 The timeout to apply when publishing the message.
 
         Returns:
             A class instance that conforms to Python Standard library's
             :class:`~concurrent.futures.Future` interface (but not an
             instance of that class). The future might return immediately with a
             PublishToPausedOrderingKeyException if the ordering key is paused.
@@ -313,17 +321,17 @@
                 batch = self._create_batch(commit_retry=retry, commit_timeout=timeout)
                 self._ordered_batches.append(batch)
                 future = batch.publish(message)
 
             return future
 
     # Used only for testing.
-    def _set_batch(self, batch):
+    def _set_batch(self, batch: "_batch.thread.Batch") -> None:
         self._ordered_batches = collections.deque([batch])
 
     # Used only for testing.
-    def _set_batches(self, batches):
+    def _set_batches(self, batches: Iterable["_batch.thread.Batch"]) -> None:
         self._ordered_batches = collections.deque(batches)
 
     # Used only for testing.
-    def _get_batches(self):
+    def _get_batches(self) -> Sequence["_batch.thread.Batch"]:
         return self._ordered_batches
```

### Comparing `google-cloud-pubsub-2.8.0/google/cloud/pubsub_v1/publisher/_sequencer/unordered_sequencer.py` & `google-cloud-pubsub-2.9.0/google/cloud/pubsub_v1/publisher/_sequencer/unordered_sequencer.py`

 * *Files 7% similar despite different names*

```diff
@@ -8,59 +8,67 @@
 #
 # Unless required by applicable law or agreed to in writing, software
 # distributed under the License is distributed on an "AS IS" BASIS,
 # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 # See the License for the specific language governing permissions and
 # limitations under the License.
 
+import typing
+
 from google.api_core import gapic_v1
 
 from google.cloud.pubsub_v1.publisher._sequencer import base
 from google.pubsub_v1 import types as gapic_types
 
+if typing.TYPE_CHECKING:  # pragma: NO COVER
+    from concurrent import futures
+    from google.api_core import retry
+    from google.cloud.pubsub_v1 import PublisherClient
+    from google.cloud.pubsub_v1.publisher import _batch
+
 
 class UnorderedSequencer(base.Sequencer):
     """ Sequences messages into batches for one topic without any ordering.
 
         Public methods are NOT thread-safe.
     """
 
-    def __init__(self, client, topic):
+    def __init__(self, client: "PublisherClient", topic: str):
         self._client = client
         self._topic = topic
         self._current_batch = None
         self._stopped = False
 
-    def is_finished(self):
+    def is_finished(self) -> bool:
         """ Whether the sequencer is finished and should be cleaned up.
 
             Returns:
-                bool: Whether the sequencer is finished and should be cleaned up.
+                Whether the sequencer is finished and should be cleaned up.
         """
         # TODO: Implement. Not implementing yet because of possible performance
         # impact due to extra locking required. This does mean that
         # UnorderedSequencers don't get cleaned up, but this is the same as
         # previously existing behavior.
         return False
 
-    def stop(self):
+    def stop(self) -> None:
         """ Stop the sequencer.
 
             Subsequent publishes will fail.
 
             Raises:
                 RuntimeError:
                     If called after stop() has already been called.
         """
         if self._stopped:
             raise RuntimeError("Unordered sequencer already stopped.")
         self.commit()
         self._stopped = True
 
-    def commit(self):
+    def commit(self) -> None:
         """ Commit the batch.
 
             Raises:
                 RuntimeError:
                     If called after stop() has already been called.
         """
         if self._stopped:
@@ -70,62 +78,61 @@
 
             # At this point, we lose track of the old batch, but we don't
             # care since we just committed it.
             # Setting this to None guarantees the next publish() creates a new
             # batch.
             self._current_batch = None
 
-    def unpause(self):
+    def unpause(self) -> typing.NoReturn:
         """ Not relevant for this class. """
         raise NotImplementedError
 
     def _create_batch(
         self,
-        commit_retry=gapic_v1.method.DEFAULT,
+        commit_retry: "retry.Retry" = gapic_v1.method.DEFAULT,
         commit_timeout: gapic_types.TimeoutType = gapic_v1.method.DEFAULT,
-    ):
+    ) -> "_batch.thread.Batch":
         """ Create a new batch using the client's batch class and other stored
             settings.
 
         Args:
-            commit_retry (Optional[google.api_core.retry.Retry]):
+            commit_retry:
                 The retry settings to apply when publishing the batch.
-            commit_timeout (:class:`~.pubsub_v1.types.TimeoutType`):
+            commit_timeout:
                 The timeout to apply when publishing the batch.
         """
         return self._client._batch_class(
             client=self._client,
             topic=self._topic,
             settings=self._client.batch_settings,
             batch_done_callback=None,
             commit_when_full=True,
             commit_retry=commit_retry,
             commit_timeout=commit_timeout,
         )
 
     def publish(
         self,
-        message,
-        retry=gapic_v1.method.DEFAULT,
+        message: gapic_types.PubsubMessage,
+        retry: "retry.Retry" = gapic_v1.method.DEFAULT,
         timeout: gapic_types.TimeoutType = gapic_v1.method.DEFAULT,
-    ):
+    ) -> "futures.Future":
         """ Batch message into existing or new batch.
 
         Args:
-            message (~.pubsub_v1.types.PubsubMessage):
+            message:
                 The Pub/Sub message.
-            retry (Optional[google.api_core.retry.Retry]):
+            retry:
                 The retry settings to apply when publishing the message.
-            timeout (:class:`~.pubsub_v1.types.TimeoutType`):
+            timeout:
                 The timeout to apply when publishing the message.
 
         Returns:
-            ~google.api_core.future.Future: An object conforming to
-            the :class:`~concurrent.futures.Future` interface. The future tracks
-            the publishing status of the message.
+            An object conforming to the :class:`~concurrent.futures.Future` interface.
+            The future tracks the publishing status of the message.
 
         Raises:
             RuntimeError:
                 If called after stop() has already been called.
 
             pubsub_v1.publisher.exceptions.MessageTooLargeError: If publishing
                 the ``message`` would exceed the max size limit on the backend.
@@ -147,9 +154,9 @@
                 batch = self._create_batch(commit_retry=retry, commit_timeout=timeout)
                 # At this point, we lose track of the old batch, but we don't
                 # care since it's already committed (because it was full.)
                 self._current_batch = batch
         return future
 
     # Used only for testing.
-    def _set_batch(self, batch):
+    def _set_batch(self, batch: "_batch.thread.Batch") -> None:
         self._current_batch = batch
```

### Comparing `google-cloud-pubsub-2.8.0/google/cloud/pubsub_v1/publisher/client.py` & `google-cloud-pubsub-2.9.0/google/cloud/pubsub_v1/publisher/client.py`

 * *Files 14% similar despite different names*

```diff
@@ -16,14 +16,16 @@
 
 import copy
 import logging
 import os
 import pkg_resources
 import threading
 import time
+import typing
+from typing import Any, Sequence, Type, Union
 
 from google.api_core import gapic_v1
 from google.auth.credentials import AnonymousCredentials
 from google.oauth2 import service_account
 
 from google.cloud.pubsub_v1 import _gapic
 from google.cloud.pubsub_v1 import types
@@ -39,14 +41,21 @@
 try:
     __version__ = pkg_resources.get_distribution("google-cloud-pubsub").version
 except pkg_resources.DistributionNotFound:
     # Distribution might not be available if we are not running from within a
     # PIP package.
     __version__ = "0.0"
 
+if typing.TYPE_CHECKING:  # pragma: NO COVER
+    from google import api_core
+    from google.cloud import pubsub_v1
+    from google.cloud.pubsub_v1.publisher._sequencer.base import Sequencer
+    from google.cloud.pubsub_v1.publisher import _batch
+
+
 _LOGGER = logging.getLogger(__name__)
 
 _DENYLISTED_METHODS = (
     "publish",
     "from_service_account_file",
     "from_service_account_json",
 )
@@ -59,21 +68,22 @@
     """A publisher client for Google Cloud Pub/Sub.
 
     This creates an object that is capable of publishing messages.
     Generally, you can instantiate this client with no arguments, and you
     get sensible defaults.
 
     Args:
-        batch_settings (~google.cloud.pubsub_v1.types.BatchSettings): The
-            settings for batch publishing.
-        publisher_options (~google.cloud.pubsub_v1.types.PublisherOptions): The
-            options for the publisher client. Note that enabling message ordering will
-            override the publish retry timeout to be infinite.
-        kwargs (dict): Any additional arguments provided are sent as keyword
-            arguments to the underlying
+        batch_settings:
+            The settings for batch publishing.
+        publisher_options:
+            The options for the publisher client. Note that enabling message ordering
+            will override the publish retry timeout to be infinite.
+        kwargs:
+            Any additional arguments provided are sent as keyword arguments to the
+            underlying
             :class:`~google.cloud.pubsub_v1.gapic.publisher_client.PublisherClient`.
             Generally you should not need to set additional keyword
             arguments. Regional endpoints can be set via ``client_options`` that
             takes a single key-value pair that defines the endpoint.
 
     Example:
 
@@ -100,22 +110,27 @@
             # Optional
             client_options = {
                 "api_endpoint": REGIONAL_ENDPOINT
             }
         )
     """
 
-    def __init__(self, batch_settings=(), publisher_options=(), **kwargs):
+    def __init__(
+        self,
+        batch_settings: Union[types.BatchSettings, Sequence] = (),
+        publisher_options: Union[types.PublisherOptions, Sequence] = (),
+        **kwargs: Any,
+    ):
         assert (
             type(batch_settings) is types.BatchSettings or len(batch_settings) == 0
-        ), "batch_settings must be of type BatchSettings or an empty tuple."
+        ), "batch_settings must be of type BatchSettings or an empty sequence."
         assert (
             type(publisher_options) is types.PublisherOptions
             or len(publisher_options) == 0
-        ), "publisher_options must be of type PublisherOptions or an empty tuple."
+        ), "publisher_options must be of type PublisherOptions or an empty sequence."
 
         # Sanity check: Is our goal to use the emulator?
         # If so, create a grpc insecure channel with the emulator host
         # as the target.
         if os.environ.get("PUBSUB_EMULATOR_HOST"):
             kwargs["client_options"] = {
                 "api_endpoint": os.environ.get("PUBSUB_EMULATOR_HOST")
@@ -142,45 +157,50 @@
         # Thread created to commit all sequencers after a timeout.
         self._commit_thread = None
 
         # The object controlling the message publishing flow
         self._flow_controller = FlowController(self.publisher_options.flow_control)
 
     @classmethod
-    def from_service_account_file(cls, filename, batch_settings=(), **kwargs):
+    def from_service_account_file(
+        cls,
+        filename: str,
+        batch_settings: Union[types.BatchSettings, Sequence] = (),
+        **kwargs: Any,
+    ) -> "Client":
         """Creates an instance of this client using the provided credentials
         file.
 
         Args:
-            filename (str): The path to the service account private key json
-                file.
-            batch_settings (~google.cloud.pubsub_v1.types.BatchSettings): The
-                settings for batch publishing.
-            kwargs: Additional arguments to pass to the constructor.
+            filename:
+                The path to the service account private key JSON file.
+            batch_settings:
+                The settings for batch publishing.
+            kwargs:
+                Additional arguments to pass to the constructor.
 
         Returns:
-            A Publisher :class:`~google.cloud.pubsub_v1.publisher.client.Client`
-            instance that is the constructed client.
+            A Publisher instance that is the constructed client.
         """
         credentials = service_account.Credentials.from_service_account_file(filename)
         kwargs["credentials"] = credentials
         return cls(batch_settings, **kwargs)
 
     from_service_account_json = from_service_account_file
 
     @property
-    def target(self):
+    def target(self) -> str:
         """Return the target (where the API is).
 
         Returns:
-            str: The location of the API.
+            The location of the API.
         """
         return self._target
 
-    def _get_or_create_sequencer(self, topic, ordering_key):
+    def _get_or_create_sequencer(self, topic: str, ordering_key: str) -> "Sequencer":
         """ Get an existing sequencer or create a new one given the (topic,
             ordering_key) pair.
         """
         sequencer_key = (topic, ordering_key)
         sequencer = self._sequencers.get(sequencer_key)
         if sequencer is None:
             if ordering_key == "":
@@ -189,19 +209,19 @@
                 sequencer = ordered_sequencer.OrderedSequencer(
                     self, topic, ordering_key
                 )
             self._sequencers[sequencer_key] = sequencer
 
         return sequencer
 
-    def resume_publish(self, topic, ordering_key):
+    def resume_publish(self, topic: str, ordering_key: str) -> None:
         """ Resume publish on an ordering key that has had unrecoverable errors.
 
         Args:
-            topic (str): The topic to publish messages to.
+            topic: The topic to publish messages to.
             ordering_key: A string that identifies related messages for which
                 publish order should be respected.
 
         Raises:
             RuntimeError:
                 If called after publisher has been stopped by a `stop()` method
                 call.
@@ -227,21 +247,21 @@
                     "been seen before."
                 )
             else:
                 sequencer.unpause()
 
     def publish(
         self,
-        topic,
-        data,
-        ordering_key="",
-        retry=gapic_v1.method.DEFAULT,
+        topic: str,
+        data: bytes,
+        ordering_key: str = "",
+        retry: "api_core.retry.Retry" = gapic_v1.method.DEFAULT,
         timeout: gapic_types.TimeoutType = gapic_v1.method.DEFAULT,
-        **attrs
-    ):
+        **attrs: Union[bytes, str],
+    ) -> "pubsub_v1.publisher.futures.Future":
         """Publish a single message.
 
         .. note::
             Messages in Pub/Sub are blobs of bytes. They are *binary* data,
             not text. You must send data as a bytestring
             (``bytes`` in Python 3; ``str`` in Python 2), and this library
             will raise an exception if you send a text string.
@@ -262,30 +282,30 @@
             >>> from google.cloud import pubsub_v1
             >>> client = pubsub_v1.PublisherClient()
             >>> topic = client.topic_path('[PROJECT]', '[TOPIC]')
             >>> data = b'The rain in Wales falls mainly on the snails.'
             >>> response = client.publish(topic, data, username='guido')
 
         Args:
-            topic (str): The topic to publish messages to.
-            data (bytes): A bytestring representing the message body. This
+            topic: The topic to publish messages to.
+            data: A bytestring representing the message body. This
                 must be a bytestring.
             ordering_key: A string that identifies related messages for which
                 publish order should be respected. Message ordering must be
                 enabled for this client to use this feature.
-            retry (Optional[google.api_core.retry.Retry]): Designation of what
-                errors, if any, should be retried. If `ordering_key` is specified,
-                the total retry deadline will be changed to "infinity".
+            retry:
+                Designation of what errors, if any, should be retried. If `ordering_key`
+                is specified, the total retry deadline will be changed to "infinity".
                 If given, it overides any retry passed into the client through
                 the ``publisher_options`` argument.
-            timeout (:class:`~.pubsub_v1.types.TimeoutType`):
+            timeout:
                 The timeout for the RPC request. Can be used to override any timeout
                 passed in through ``publisher_options`` when instantiating the client.
 
-            attrs (Mapping[str, str]): A dictionary of attributes to be
+            attrs: A dictionary of attributes to be
                 sent as metadata. (These may be text strings or byte strings.)
 
         Returns:
             A :class:`~google.cloud.pubsub_v1.publisher.futures.Future`
             instance that conforms to Python Standard library's
             :class:`~concurrent.futures.Future` interface (but not an
             instance of that class).
@@ -370,70 +390,70 @@
 
             # Create a timer thread if necessary to enforce the batching
             # timeout.
             self._ensure_commit_timer_runs_no_lock()
 
             return future
 
-    def ensure_cleanup_and_commit_timer_runs(self):
+    def ensure_cleanup_and_commit_timer_runs(self) -> None:
         """ Ensure a cleanup/commit timer thread is running.
 
             If a cleanup/commit timer thread is already running, this does nothing.
         """
         with self._batch_lock:
             self._ensure_commit_timer_runs_no_lock()
 
-    def _ensure_commit_timer_runs_no_lock(self):
+    def _ensure_commit_timer_runs_no_lock(self) -> None:
         """ Ensure a commit timer thread is running, without taking
             _batch_lock.
 
             _batch_lock must be held before calling this method.
         """
         if not self._commit_thread and self.batch_settings.max_latency < float("inf"):
             self._start_commit_thread()
 
-    def _start_commit_thread(self):
+    def _start_commit_thread(self) -> None:
         """Start a new thread to actually wait and commit the sequencers."""
         # NOTE: If the thread is *not* a daemon, a memory leak exists due to a CPython issue.
         # https://github.com/googleapis/python-pubsub/issues/395#issuecomment-829910303
         # https://github.com/googleapis/python-pubsub/issues/395#issuecomment-830092418
         self._commit_thread = threading.Thread(
             name="Thread-PubSubBatchCommitter",
             target=self._wait_and_commit_sequencers,
             daemon=True,
         )
         self._commit_thread.start()
 
-    def _wait_and_commit_sequencers(self):
+    def _wait_and_commit_sequencers(self) -> None:
         """ Wait up to the batching timeout, and commit all sequencers.
         """
         # Sleep for however long we should be waiting.
         time.sleep(self.batch_settings.max_latency)
         _LOGGER.debug("Commit thread is waking up")
 
         with self._batch_lock:
             if self._is_stopped:
                 return
             self._commit_sequencers()
             self._commit_thread = None
 
-    def _commit_sequencers(self):
+    def _commit_sequencers(self) -> None:
         """ Clean up finished sequencers and commit the rest. """
         finished_sequencer_keys = [
             key
             for key, sequencer in self._sequencers.items()
             if sequencer.is_finished()
         ]
         for sequencer_key in finished_sequencer_keys:
             del self._sequencers[sequencer_key]
 
         for sequencer in self._sequencers.values():
             sequencer.commit()
 
-    def stop(self):
+    def stop(self) -> None:
         """Immediately publish all outstanding messages.
 
         Asynchronously sends all outstanding messages and
         prevents future calls to `publish()`. Method should
         be invoked prior to deleting this `Client()` object
         in order to ensure that no pending messages are lost.
 
@@ -454,19 +474,23 @@
 
             self._is_stopped = True
 
             for sequencer in self._sequencers.values():
                 sequencer.stop()
 
     # Used only for testing.
-    def _set_batch(self, topic, batch, ordering_key=""):
+    def _set_batch(
+        self, topic: str, batch: "_batch.thread.Batch", ordering_key: str = ""
+    ) -> None:
         sequencer = self._get_or_create_sequencer(topic, ordering_key)
         sequencer._set_batch(batch)
 
     # Used only for testing.
-    def _set_batch_class(self, batch_class):
+    def _set_batch_class(self, batch_class: Type) -> None:
         self._batch_class = batch_class
 
     # Used only for testing.
-    def _set_sequencer(self, topic, sequencer, ordering_key=""):
+    def _set_sequencer(
+        self, topic: str, sequencer: "Sequencer", ordering_key: str = ""
+    ) -> None:
         sequencer_key = (topic, ordering_key)
         self._sequencers[sequencer_key] = sequencer
```

### Comparing `google-cloud-pubsub-2.8.0/google/cloud/pubsub_v1/publisher/exceptions.py` & `google-cloud-pubsub-2.9.0/google/cloud/pubsub_v1/publisher/exceptions.py`

 * *Files 1% similar despite different names*

```diff
@@ -29,15 +29,15 @@
 class PublishToPausedOrderingKeyException(Exception):
     """ Publish attempted to paused ordering key. To resume publishing, call
         the resumePublish method on the publisher Client object with this
         ordering key. Ordering keys are paused if an unrecoverable error
         occurred during publish of a batch for that key.
     """
 
-    def __init__(self, ordering_key):
+    def __init__(self, ordering_key: str):
         self.ordering_key = ordering_key
         super(PublishToPausedOrderingKeyException, self).__init__()
 
 
 class FlowControlLimitError(Exception):
     """An action resulted in exceeding the flow control limits."""
```

### Comparing `google-cloud-pubsub-2.8.0/google/cloud/pubsub_v1/publisher/flow_controller.py` & `google-cloud-pubsub-2.9.0/google/cloud/pubsub_v1/publisher/flow_controller.py`

 * *Files 5% similar despite different names*

```diff
@@ -11,14 +11,15 @@
 # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 # See the License for the specific language governing permissions and
 # limitations under the License.
 
 from collections import OrderedDict
 import logging
 import threading
+from typing import Optional
 import warnings
 
 from google.cloud.pubsub_v1 import types
 from google.cloud.pubsub_v1.publisher import exceptions
 
 
 _LOGGER = logging.getLogger(__name__)
@@ -41,19 +42,18 @@
         )
 
 
 class FlowController(object):
     """A class used to control the flow of messages passing through it.
 
     Args:
-        settings (~google.cloud.pubsub_v1.types.PublishFlowControl):
-            Desired flow control configuration.
+        settings: Desired flow control configuration.
     """
 
-    def __init__(self, settings):
+    def __init__(self, settings: types.PublishFlowControl):
         self._settings = settings
 
         # Load statistics. They represent the number of messages added, but not
         # yet released (and their total size).
         self._message_count = 0
         self._total_bytes = 0
 
@@ -68,22 +68,22 @@
         # The lock is used to protect all internal state (message and byte count,
         # waiting threads to add, etc.).
         self._operational_lock = threading.Lock()
 
         # The condition for blocking the flow if capacity is exceeded.
         self._has_capacity = threading.Condition(lock=self._operational_lock)
 
-    def add(self, message):
+    def add(self, message: types.PubsubMessage) -> None:  # pytype: disable=module-attr
         """Add a message to flow control.
 
         Adding a message updates the internal load statistics, and an action is
         taken if these limits are exceeded (depending on the flow control settings).
 
         Args:
-            message (:class:`~google.cloud.pubsub_v1.types.PubsubMessage`):
+            message:
                 The message entering the flow control.
 
         Raises:
             :exception:`~pubsub_v1.publisher.exceptions.FlowControlLimitError`:
                 Raised when the desired action is
                 :attr:`~google.cloud.pubsub_v1.types.LimitExceededBehavior.ERROR` and
                 the message would exceed flow control limits, or when the desired action
@@ -162,19 +162,21 @@
             # Message accepted, increase the load and remove thread stats.
             self._message_count += 1
             self._total_bytes += message._pb.ByteSize()
             self._reserved_bytes -= self._waiting[current_thread].bytes_reserved
             self._reserved_slots -= 1
             del self._waiting[current_thread]
 
-    def release(self, message):
+    def release(
+        self, message: types.PubsubMessage  # pytype: disable=module-attr
+    ) -> None:
         """Release a mesage from flow control.
 
         Args:
-            message (:class:`~google.cloud.pubsub_v1.types.PubsubMessage`):
+            message:
                 The message entering the flow control.
         """
         if self._settings.limit_exceeded_behavior == types.LimitExceededBehavior.IGNORE:
             return
 
         with self._operational_lock:
             # Releasing a message decreases the load.
@@ -193,15 +195,15 @@
             self._distribute_available_capacity()
 
             # If at least one thread waiting to add() can be unblocked, wake them up.
             if self._ready_to_unblock():
                 _LOGGER.debug("Notifying threads waiting to add messages to flow.")
                 self._has_capacity.notify_all()
 
-    def _distribute_available_capacity(self):
+    def _distribute_available_capacity(self) -> None:
         """Distribute available capacity among the waiting threads in FIFO order.
 
         The method assumes that the caller has obtained ``_operational_lock``.
         """
         available_slots = (
             self._settings.message_limit - self._message_count - self._reserved_slots
         )
@@ -233,44 +235,39 @@
                 bytes_still_needed = 0
 
             can_give = min(bytes_still_needed, available_bytes)
             reservation.bytes_reserved += can_give
             self._reserved_bytes += can_give
             available_bytes -= can_give
 
-    def _ready_to_unblock(self):
+    def _ready_to_unblock(self) -> bool:
         """Determine if any of the threads waiting to add a message can proceed.
 
         The method assumes that the caller has obtained ``_operational_lock``.
-
-        Returns:
-            bool
         """
         if self._waiting:
             # It's enough to only check the head of the queue, because FIFO
             # distribution of any free capacity.
             first_reservation = next(iter(self._waiting.values()))
             return (
                 first_reservation.bytes_reserved >= first_reservation.bytes_needed
                 and first_reservation.has_slot
             )
 
         return False
 
-    def _would_overflow(self, message):
+    def _would_overflow(
+        self, message: types.PubsubMessage  # pytype: disable=module-attr
+    ) -> bool:
         """Determine if accepting a message would exceed flow control limits.
 
         The method assumes that the caller has obtained ``_operational_lock``.
 
         Args:
-            message (:class:`~google.cloud.pubsub_v1.types.PubsubMessage`):
-                The message entering the flow control.
-
-        Returns:
-            bool
+            message: The message entering the flow control.
         """
         reservation = self._waiting.get(threading.current_thread())
 
         if reservation:
             enough_reserved = reservation.bytes_reserved >= reservation.bytes_needed
             has_slot = reservation.has_slot
         else:
@@ -283,30 +280,29 @@
         msg_count_overflow = not has_slot and (
             (self._message_count + self._reserved_slots + 1)
             > self._settings.message_limit
         )
 
         return size_overflow or msg_count_overflow
 
-    def _load_info(self, message_count=None, total_bytes=None):
+    def _load_info(
+        self, message_count: Optional[int] = None, total_bytes: Optional[int] = None
+    ) -> str:
         """Return the current flow control load information.
 
         The caller can optionally adjust some of the values to fit its reporting
         needs.
 
         The method assumes that the caller has obtained ``_operational_lock``.
 
         Args:
-            message_count (Optional[int]):
+            message_count:
                 The value to override the current message count with.
-            total_bytes (Optional[int]):
+            total_bytes:
                 The value to override the current total bytes with.
-
-        Returns:
-            str
         """
         if message_count is None:
             message_count = self._message_count
 
         if total_bytes is None:
             total_bytes = self._total_bytes
```

### Comparing `google-cloud-pubsub-2.8.0/google/cloud/pubsub_v1/publisher/futures.py` & `google-cloud-pubsub-2.9.0/google/cloud/pubsub_v1/publisher/futures.py`

 * *Files 4% similar despite different names*

```diff
@@ -10,51 +10,53 @@
 # distributed under the License is distributed on an "AS IS" BASIS,
 # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 # See the License for the specific language governing permissions and
 # limitations under the License.
 
 from __future__ import absolute_import
 
+from typing import Union
+
 from google.cloud.pubsub_v1 import futures
 
 
 class Future(futures.Future):
     """This future object is returned from asychronous Pub/Sub publishing
     calls.
 
     Calling :meth:`result` will resolve the future by returning the message
     ID, unless an error occurs.
     """
 
-    def cancel(self):
+    def cancel(self) -> bool:
         """Actions in Pub/Sub generally may not be canceled.
 
         This method always returns ``False``.
         """
         return False
 
-    def cancelled(self):
+    def cancelled(self) -> bool:
         """Actions in Pub/Sub generally may not be canceled.
 
         This method always returns ``False``.
         """
         return False
 
-    def result(self, timeout=None):
+    def result(self, timeout: Union[int, float] = None) -> str:
         """Return the message ID or raise an exception.
 
         This blocks until the message has been published successfully and
         returns the message ID unless an exception is raised.
 
         Args:
-            timeout (Union[int, float]): The number of seconds before this call
+            timeout: The number of seconds before this call
                 times out and raises TimeoutError.
 
         Returns:
-            str: The message ID.
+            The message ID.
 
         Raises:
             concurrent.futures.TimeoutError: If the request times out.
             Exception: For undefined exceptions in the underlying
                 call execution.
         """
         return super().result(timeout=timeout)
```

### Comparing `google-cloud-pubsub-2.8.0/google/cloud/pubsub_v1/subscriber/__init__.py` & `google-cloud-pubsub-2.9.0/google/cloud/pubsub_v1/subscriber/__init__.py`

 * *Files identical despite different names*

### Comparing `google-cloud-pubsub-2.8.0/google/cloud/pubsub_v1/subscriber/_protocol/dispatcher.py` & `google-cloud-pubsub-2.9.0/google/cloud/pubsub_v1/subscriber/_protocol/dispatcher.py`

 * *Files 16% similar despite different names*

```diff
@@ -16,19 +16,36 @@
 from __future__ import division
 
 import collections
 import itertools
 import logging
 import math
 import threading
+import typing
+from typing import Sequence, Union
 
 from google.cloud.pubsub_v1.subscriber._protocol import helper_threads
 from google.cloud.pubsub_v1.subscriber._protocol import requests
 from google.pubsub_v1 import types as gapic_types
 
+if typing.TYPE_CHECKING:  # pragma: NO COVER
+    import queue
+    from google.cloud.pubsub_v1.subscriber._protocol.streaming_pull_manager import (
+        StreamingPullManager,
+    )
+
+
+RequestItem = Union[
+    requests.AckRequest,
+    requests.DropRequest,
+    requests.LeaseRequest,
+    requests.ModAckRequest,
+    requests.NackRequest,
+]
+
 
 _LOGGER = logging.getLogger(__name__)
 _CALLBACK_WORKER_NAME = "Thread-CallbackRequestDispatcher"
 
 
 _MAX_BATCH_SIZE = 100
 """The maximum number of requests to process and dispatch at a time."""
@@ -47,22 +64,23 @@
 
 Accounting for some overhead, we should thus only send a maximum of 2500 ACK
 IDs at a time.
 """
 
 
 class Dispatcher(object):
-    def __init__(self, manager, queue):
+    def __init__(self, manager: "StreamingPullManager", queue: "queue.Queue"):
         self._manager = manager
         self._queue = queue
         self._thread = None
         self._operational_lock = threading.Lock()
 
-    def start(self):
+    def start(self) -> None:
         """Start a thread to dispatch requests queued up by callbacks.
+
         Spawns a thread to run :meth:`dispatch_callback`.
         """
         with self._operational_lock:
             if self._thread is not None:
                 raise ValueError("Dispatcher is already running.")
 
             worker = helper_threads.QueueCallbackWorker(
@@ -74,34 +92,29 @@
             # Create and start the helper thread.
             thread = threading.Thread(name=_CALLBACK_WORKER_NAME, target=worker)
             thread.daemon = True
             thread.start()
             _LOGGER.debug("Started helper thread %s", thread.name)
             self._thread = thread
 
-    def stop(self):
+    def stop(self) -> None:
         with self._operational_lock:
             if self._thread is not None:
                 # Signal the worker to stop by queueing a "poison pill"
                 self._queue.put(helper_threads.STOP)
                 self._thread.join()
 
             self._thread = None
 
-    def dispatch_callback(self, items):
+    def dispatch_callback(self, items: Sequence[RequestItem]) -> None:
         """Map the callback request to the appropriate gRPC request.
 
         Args:
-            action (str): The method to be invoked.
-            kwargs (Dict[str, Any]): The keyword arguments for the method
-                specified by ``action``.
-
-        Raises:
-            ValueError: If ``action`` isn't one of the expected actions
-                "ack", "drop", "lease", "modify_ack_deadline" or "nack".
+            items:
+                Queued requests to dispatch.
         """
         batched_commands = collections.defaultdict(list)
 
         for item in items:
             batched_commands[item.__class__].append(item)
 
         _LOGGER.debug("Handling %d batched requests", len(items))
@@ -115,19 +128,19 @@
         if batched_commands[requests.AckRequest]:
             self.ack(batched_commands.pop(requests.AckRequest))
         if batched_commands[requests.NackRequest]:
             self.nack(batched_commands.pop(requests.NackRequest))
         if batched_commands[requests.DropRequest]:
             self.drop(batched_commands.pop(requests.DropRequest))
 
-    def ack(self, items):
+    def ack(self, items: Sequence[requests.AckRequest]) -> None:
         """Acknowledge the given messages.
 
         Args:
-            items(Sequence[AckRequest]): The items to acknowledge.
+            items: The items to acknowledge.
         """
         # If we got timing information, add it to the histogram.
         for item in items:
             time_to_ack = item.time_to_ack
             if time_to_ack is not None:
                 self._manager.ack_histogram.add(time_to_ack)
 
@@ -141,56 +154,61 @@
                 ack_ids=itertools.islice(ack_ids, _ACK_IDS_BATCH_SIZE)
             )
             self._manager.send(request)
 
         # Remove the message from lease management.
         self.drop(items)
 
-    def drop(self, items):
+    def drop(
+        self,
+        items: Sequence[
+            Union[requests.AckRequest, requests.DropRequest, requests.NackRequest]
+        ],
+    ) -> None:
         """Remove the given messages from lease management.
 
         Args:
-            items(Sequence[DropRequest]): The items to drop.
+            items: The items to drop.
         """
         self._manager.leaser.remove(items)
         ordering_keys = (k.ordering_key for k in items if k.ordering_key)
         self._manager.activate_ordering_keys(ordering_keys)
         self._manager.maybe_resume_consumer()
 
-    def lease(self, items):
+    def lease(self, items: Sequence[requests.LeaseRequest]) -> None:
         """Add the given messages to lease management.
 
         Args:
-            items(Sequence[LeaseRequest]): The items to lease.
+            items: The items to lease.
         """
         self._manager.leaser.add(items)
         self._manager.maybe_pause_consumer()
 
-    def modify_ack_deadline(self, items):
+    def modify_ack_deadline(self, items: Sequence[requests.ModAckRequest]) -> None:
         """Modify the ack deadline for the given messages.
 
         Args:
-            items(Sequence[ModAckRequest]): The items to modify.
+            items: The items to modify.
         """
         # We must potentially split the request into multiple smaller requests
         # to avoid the server-side max request size limit.
         ack_ids = (item.ack_id for item in items)
         seconds = (item.seconds for item in items)
         total_chunks = int(math.ceil(len(items) / _ACK_IDS_BATCH_SIZE))
 
         for _ in range(total_chunks):
             request = gapic_types.StreamingPullRequest(
                 modify_deadline_ack_ids=itertools.islice(ack_ids, _ACK_IDS_BATCH_SIZE),
                 modify_deadline_seconds=itertools.islice(seconds, _ACK_IDS_BATCH_SIZE),
             )
             self._manager.send(request)
 
-    def nack(self, items):
+    def nack(self, items: Sequence[requests.NackRequest]) -> None:
         """Explicitly deny receipt of messages.
 
         Args:
-            items(Sequence[NackRequest]): The items to deny.
+            items: The items to deny.
         """
         self.modify_ack_deadline(
             [requests.ModAckRequest(ack_id=item.ack_id, seconds=0) for item in items]
         )
         self.drop([requests.DropRequest(*item) for item in items])
```

### Comparing `google-cloud-pubsub-2.8.0/google/cloud/pubsub_v1/subscriber/_protocol/heartbeater.py` & `google-cloud-pubsub-2.9.0/google/cloud/pubsub_v1/subscriber/_protocol/heartbeater.py`

 * *Files 11% similar despite different names*

```diff
@@ -12,58 +12,64 @@
 # See the License for the specific language governing permissions and
 # limitations under the License.
 
 from __future__ import absolute_import
 
 import logging
 import threading
+import typing
+
+if typing.TYPE_CHECKING:  # pragma: NO COVER
+    from google.cloud.pubsub_v1.subscriber._protocol.streaming_pull_manager import (
+        StreamingPullManager,
+    )
 
 
 _LOGGER = logging.getLogger(__name__)
 _HEARTBEAT_WORKER_NAME = "Thread-Heartbeater"
 # How often to send heartbeats in seconds. Determined as half the period of
 # time where the Pub/Sub server will close the stream as inactive, which is
 # 60 seconds.
 _DEFAULT_PERIOD = 30
 
 
 class Heartbeater(object):
-    def __init__(self, manager, period=_DEFAULT_PERIOD):
+    def __init__(self, manager: "StreamingPullManager", period: int = _DEFAULT_PERIOD):
         self._thread = None
         self._operational_lock = threading.Lock()
         self._manager = manager
         self._stop_event = threading.Event()
         self._period = period
 
-    def heartbeat(self):
+    def heartbeat(self) -> None:
         """Periodically send streaming pull heartbeats.
         """
         while not self._stop_event.is_set():
             if self._manager.heartbeat():
                 _LOGGER.debug("Sent heartbeat.")
             self._stop_event.wait(timeout=self._period)
 
         _LOGGER.info("%s exiting.", _HEARTBEAT_WORKER_NAME)
 
-    def start(self):
+    def start(self) -> None:
         with self._operational_lock:
             if self._thread is not None:
                 raise ValueError("Heartbeater is already running.")
 
             # Create and start the helper thread.
             self._stop_event.clear()
             thread = threading.Thread(
                 name=_HEARTBEAT_WORKER_NAME, target=self.heartbeat
             )
             thread.daemon = True
             thread.start()
             _LOGGER.debug("Started helper thread %s", thread.name)
             self._thread = thread
 
-    def stop(self):
+    def stop(self) -> None:
         with self._operational_lock:
             self._stop_event.set()
 
             if self._thread is not None:
                 # The thread should automatically exit when the consumer is
                 # inactive.
                 self._thread.join()
```

### Comparing `google-cloud-pubsub-2.8.0/google/cloud/pubsub_v1/subscriber/_protocol/helper_threads.py` & `google-cloud-pubsub-2.9.0/google/cloud/pubsub_v1/subscriber/_protocol/helper_threads.py`

 * *Files 9% similar despite different names*

```diff
@@ -11,14 +11,15 @@
 # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 # See the License for the specific language governing permissions and
 # limitations under the License.
 
 import logging
 import queue
 import time
+from typing import Any, Callable, List, Sequence
 import uuid
 
 
 __all__ = ("QueueCallbackWorker", "STOP")
 
 _LOGGER = logging.getLogger(__name__)
 
@@ -26,30 +27,33 @@
 # Helper thread stop indicator. This could be a sentinel object or None,
 # but the sentinel object's ID can change if the process is forked, and
 # None has the possibility of a user accidentally killing the helper
 # thread.
 STOP = uuid.uuid4()
 
 
-def _get_many(queue_, max_items=None, max_latency=0):
+def _get_many(
+    queue_: queue.Queue, max_items: int = None, max_latency: float = 0
+) -> List[Any]:
     """Get multiple items from a Queue.
 
     Gets at least one (blocking) and at most ``max_items`` items
     (non-blocking) from a given Queue. Does not mark the items as done.
 
     Args:
-        queue_ (~queue.Queue`): The Queue to get items from.
-        max_items (int): The maximum number of items to get. If ``None``, then
-            all available items in the queue are returned.
-        max_latency (float):  The maximum number of seconds to wait for more
-            than one item from a queue. This number includes the time required
-            to retrieve the first item.
+        queue_: The Queue to get items from.
+        max_items:
+            The maximum number of items to get. If ``None``, then all available items
+            in the queue are returned.
+        max_latency:
+            The maximum number of seconds to wait for more than one item from a queue.
+            This number includes the time required to retrieve the first item.
 
     Returns:
-        Sequence[Any]: A sequence of items retrieved from the queue.
+        A sequence of items retrieved from the queue.
     """
     start = time.time()
     # Always return at least one item.
     items = [queue_.get()]
     while max_items is None or len(items) < max_items:
         try:
             elapsed = time.time() - start
@@ -63,34 +67,41 @@
 class QueueCallbackWorker(object):
     """A helper that executes a callback for items sent in a queue.
 
     Calls a blocking ``get()`` on the ``queue`` until it encounters
     :attr:`STOP`.
 
     Args:
-        queue (~queue.Queue): A Queue instance, appropriate for crossing the
-            concurrency boundary implemented by ``executor``. Items will
-            be popped off (with a blocking ``get()``) until :attr:`STOP`
-            is encountered.
-        callback (Callable[Sequence[Any], Any]): A callback that can process
-            items pulled off of the queue. Multiple items will be passed to
-            the callback in batches.
-        max_items (int): The maximum amount of items that will be passed to the
-            callback at a time.
-        max_latency (float): The maximum amount of time in seconds to wait for
-            additional items before executing the callback.
+        queue:
+            A Queue instance, appropriate for crossing the concurrency boundary
+            implemented by ``executor``. Items will be popped off (with a blocking
+            ``get()``) until :attr:`STOP` is encountered.
+        callback:
+            A callback that can process items pulled off of the queue. Multiple items
+            will be passed to the callback in batches.
+        max_items:
+            The maximum amount of items that will be passed to the callback at a time.
+        max_latency:
+            The maximum amount of time in seconds to wait for additional items before
+            executing the callback.
     """
 
-    def __init__(self, queue, callback, max_items=100, max_latency=0):
+    def __init__(
+        self,
+        queue: queue.Queue,
+        callback: Callable[[Sequence[Any]], Any],
+        max_items: int = 100,
+        max_latency: float = 0,
+    ):
         self.queue = queue
         self._callback = callback
         self.max_items = max_items
         self.max_latency = max_latency
 
-    def __call__(self):
+    def __call__(self) -> None:
         continue_ = True
         while continue_:
             items = _get_many(
                 self.queue, max_items=self.max_items, max_latency=self.max_latency
             )
 
             # If stop is in the items, process all items up to STOP and then
```

### Comparing `google-cloud-pubsub-2.8.0/google/cloud/pubsub_v1/subscriber/_protocol/histogram.py` & `google-cloud-pubsub-2.9.0/google/cloud/pubsub_v1/subscriber/_protocol/histogram.py`

 * *Files 15% similar despite different names*

```diff
@@ -8,15 +8,15 @@
 #
 # Unless required by applicable law or agreed to in writing, software
 # distributed under the License is distributed on an "AS IS" BASIS,
 # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 # See the License for the specific language governing permissions and
 # limitations under the License.
 
-from __future__ import absolute_import, division
+from typing import Dict, Optional, Union
 
 
 MIN_ACK_DEADLINE = 10
 MAX_ACK_DEADLINE = 600
 
 
 class Histogram(object):
@@ -32,23 +32,23 @@
 
     The precision of data stored is to the nearest integer. Additionally,
     values outside the range of ``MIN_ACK_DEADLINE <= x <= MAX_ACK_DEADLINE`` are stored
     as ``MIN_ACK_DEADLINE`` or ``MAX_ACK_DEADLINE``, since these are the boundaries of
     leases in the actual API.
     """
 
-    def __init__(self, data=None):
+    def __init__(self, data: Optional[Dict[int, int]] = None):
         """Instantiate the histogram.
 
         Args:
-            data (Mapping[str, int]): The data strucure to be used to store
-                the underlying data. The default is an empty dictionary.
-                This can be set to a dictionary-like object if required
-                (for example, if a special object is needed for
-                concurrency reasons).
+            data:
+                The data strucure to be used to store the underlying data. The default
+                is an empty dictionary. This can be set to a dictionary-like object if
+                required (for example, if a special object is needed for concurrency
+                reasons).
         """
         # The data is stored as a dictionary, with the keys being the
         # value being added and the values being the number of times that
         # value was added to the dictionary.
         #
         # This is depending on the Python interpreter's implicit ordering
         # of dictionaries, which is a bitwise sort by the key's ``hash()``
@@ -56,70 +56,68 @@
         # positive integers (negatives would be a problem because the sort
         # is bitwise), we can rely on this.
         if data is None:
             data = {}
         self._data = data
         self._len = 0
 
-    def __len__(self):
+    def __len__(self) -> int:
         """Return the total number of data points in this histogram.
 
         This is cached on a separate counter (rather than computing it using
         ``sum([v for v in self._data.values()])``) to optimize lookup.
 
         Returns:
-            int: The total number of data points in this histogram.
+            The total number of data points in this histogram.
         """
         return self._len
 
-    def __contains__(self, needle):
-        """Return True if needle is present in the histogram, False otherwise.
-
-        Returns:
-            bool: True or False
+    def __contains__(self, needle: int) -> bool:
+        """Return ``True`` if needle is present in the histogram, ``False`` otherwise.
         """
         return needle in self._data
 
     def __repr__(self):
         return "<Histogram: {len} values between {min} and {max}>".format(
             len=len(self), max=self.max, min=self.min
         )
 
     @property
-    def max(self):
+    def max(self) -> int:
         """Return the maximum value in this histogram.
 
         If there are no values in the histogram at all, return ``MAX_ACK_DEADLINE``.
 
         Returns:
-            int: The maximum value in the histogram.
+            The maximum value in the histogram.
         """
         if len(self._data) == 0:
             return MAX_ACK_DEADLINE
         return next(iter(reversed(sorted(self._data.keys()))))
 
     @property
-    def min(self):
+    def min(self) -> int:
         """Return the minimum value in this histogram.
 
         If there are no values in the histogram at all, return ``MIN_ACK_DEADLINE``.
 
         Returns:
-            int: The minimum value in the histogram.
+            The minimum value in the histogram.
         """
         if len(self._data) == 0:
             return MIN_ACK_DEADLINE
         return next(iter(sorted(self._data.keys())))
 
-    def add(self, value):
+    def add(self, value: Union[int, float]) -> None:
         """Add the value to this histogram.
 
         Args:
-            value (int): The value. Values outside of
-            ``MIN_ACK_DEADLINE <= x <= MAX_ACK_DEADLINE``
+            value:
+                The value. Values outside of
+                ``MIN_ACK_DEADLINE <= x <= MAX_ACK_DEADLINE``
                 will be raised to ``MIN_ACK_DEADLINE`` or reduced to
                 ``MAX_ACK_DEADLINE``.
         """
         # If the value is out of bounds, bring it in bounds.
         value = int(value)
         if value < MIN_ACK_DEADLINE:
             value = MIN_ACK_DEADLINE
@@ -127,23 +125,24 @@
             value = MAX_ACK_DEADLINE
 
         # Add the value to the histogram's data dictionary.
         self._data.setdefault(value, 0)
         self._data[value] += 1
         self._len += 1
 
-    def percentile(self, percent):
+    def percentile(self, percent: Union[int, float]) -> int:
         """Return the value that is the Nth precentile in the histogram.
 
         Args:
-            percent (Union[int, float]): The precentile being sought. The
-                default consumer implementations consistently use ``99``.
+            percent:
+                The precentile being sought. The default consumer implementations
+                consistently use ``99``.
 
         Returns:
-            int: The value corresponding to the requested percentile.
+            The value corresponding to the requested percentile.
         """
         # Sanity check: Any value over 100 should become 100.
         if percent >= 100:
             percent = 100
 
         # Determine the actual target number.
         target = len(self) - len(self) * (percent / 100)
```

### Comparing `google-cloud-pubsub-2.8.0/google/cloud/pubsub_v1/subscriber/_protocol/leaser.py` & `google-cloud-pubsub-2.9.0/google/cloud/pubsub_v1/subscriber/_protocol/leaser.py`

 * *Files 12% similar despite different names*

```diff
@@ -16,29 +16,36 @@
 
 import collections
 import copy
 import logging
 import random
 import threading
 import time
+import typing
+from typing import Iterable, Sequence, Union
 
 from google.cloud.pubsub_v1.subscriber._protocol import requests
 
+if typing.TYPE_CHECKING:  # pragma: NO COVER
+    from google.cloud.pubsub_v1.subscriber._protocol.streaming_pull_manager import (
+        StreamingPullManager,
+    )
+
 
 _LOGGER = logging.getLogger(__name__)
 _LEASE_WORKER_NAME = "Thread-LeaseMaintainer"
 
 
 _LeasedMessage = collections.namedtuple(
     "_LeasedMessage", ["sent_time", "size", "ordering_key"]
 )
 
 
 class Leaser(object):
-    def __init__(self, manager):
+    def __init__(self, manager: "StreamingPullManager"):
         self._thread = None
         self._manager = manager
 
         # a lock used for start/stop operations, protecting the _thread attribute
         self._operational_lock = threading.Lock()
 
         # A lock ensuring that add/remove operations are atomic and cannot be
@@ -51,29 +58,29 @@
             ack ID was initially leased in seconds since the epoch."""
         self._bytes = 0
         """int: The total number of bytes consumed by leased messages."""
 
         self._stop_event = threading.Event()
 
     @property
-    def message_count(self):
-        """int: The number of leased messages."""
+    def message_count(self) -> int:
+        """The number of leased messages."""
         return len(self._leased_messages)
 
     @property
-    def ack_ids(self):
-        """Sequence[str]: The ack IDs of all leased messages."""
+    def ack_ids(self) -> Sequence[str]:
+        """The ack IDs of all leased messages."""
         return self._leased_messages.keys()
 
     @property
-    def bytes(self):
-        """int: The total size, in bytes, of all leased messages."""
+    def bytes(self) -> int:
+        """The total size, in bytes, of all leased messages."""
         return self._bytes
 
-    def add(self, items):
+    def add(self, items: Iterable[requests.LeaseRequest]) -> None:
         """Add messages to be managed by the leaser."""
         with self._add_remove_lock:
             for item in items:
                 # Add the ack ID to the set of managed ack IDs, and increment
                 # the size counter.
                 if item.ack_id not in self._leased_messages:
                     self._leased_messages[item.ack_id] = _LeasedMessage(
@@ -81,47 +88,51 @@
                         size=item.byte_size,
                         ordering_key=item.ordering_key,
                     )
                     self._bytes += item.byte_size
                 else:
                     _LOGGER.debug("Message %s is already lease managed", item.ack_id)
 
-    def start_lease_expiry_timer(self, ack_ids):
+    def start_lease_expiry_timer(self, ack_ids: Iterable[str]) -> None:
         """Start the lease expiry timer for `items`.
 
         Args:
-            items (Sequence[str]): Sequence of ack-ids for which to start
-                lease expiry timers.
+            items: Sequence of ack-ids for which to start lease expiry timers.
         """
         with self._add_remove_lock:
             for ack_id in ack_ids:
                 lease_info = self._leased_messages.get(ack_id)
                 # Lease info might not exist for this ack_id because it has already
                 # been removed by remove().
                 if lease_info:
                     self._leased_messages[ack_id] = lease_info._replace(
                         sent_time=time.time()
                     )
 
-    def remove(self, items):
+    def remove(
+        self,
+        items: Iterable[
+            Union[requests.AckRequest, requests.DropRequest, requests.NackRequest]
+        ],
+    ) -> None:
         """Remove messages from lease management."""
         with self._add_remove_lock:
             # Remove the ack ID from lease management, and decrement the
             # byte counter.
             for item in items:
                 if self._leased_messages.pop(item.ack_id, None) is not None:
                     self._bytes -= item.byte_size
                 else:
                     _LOGGER.debug("Item %s was not managed.", item.ack_id)
 
             if self._bytes < 0:
                 _LOGGER.debug("Bytes was unexpectedly negative: %d", self._bytes)
                 self._bytes = 0
 
-    def maintain_leases(self):
+    def maintain_leases(self) -> None:
         """Maintain all of the leases being managed.
 
         This method modifies the ack deadline for all of the managed
         ack IDs, then waits for most of that time (but with jitter), and
         repeats.
         """
         while not self._stop_event.is_set():
@@ -184,30 +195,30 @@
             # where there are many clients.
             snooze = random.uniform(0.0, deadline * 0.9)
             _LOGGER.debug("Snoozing lease management for %f seconds.", snooze)
             self._stop_event.wait(timeout=snooze)
 
         _LOGGER.info("%s exiting.", _LEASE_WORKER_NAME)
 
-    def start(self):
+    def start(self) -> None:
         with self._operational_lock:
             if self._thread is not None:
                 raise ValueError("Leaser is already running.")
 
             # Create and start the helper thread.
             self._stop_event.clear()
             thread = threading.Thread(
                 name=_LEASE_WORKER_NAME, target=self.maintain_leases
             )
             thread.daemon = True
             thread.start()
             _LOGGER.debug("Started helper thread %s", thread.name)
             self._thread = thread
 
-    def stop(self):
+    def stop(self) -> None:
         with self._operational_lock:
             self._stop_event.set()
 
             if self._thread is not None:
                 # The thread should automatically exit when the consumer is
                 # inactive.
                 self._thread.join()
```

### Comparing `google-cloud-pubsub-2.8.0/google/cloud/pubsub_v1/subscriber/_protocol/messages_on_hold.py` & `google-cloud-pubsub-2.9.0/google/cloud/pubsub_v1/subscriber/_protocol/messages_on_hold.py`

 * *Files 4% similar despite different names*

```diff
@@ -9,14 +9,19 @@
 # Unless required by applicable law or agreed to in writing, software
 # distributed under the License is distributed on an "AS IS" BASIS,
 # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 # See the License for the specific language governing permissions and
 # limitations under the License.
 
 import collections
+import typing
+from typing import Any, Callable, Iterable, Optional
+
+if typing.TYPE_CHECKING:  # pragma: NO COVER
+    from google.cloud.pubsub_v1 import subscriber
 
 
 class MessagesOnHold(object):
     """Tracks messages on hold by ordering key. Not thread-safe.
     """
 
     def __init__(self):
@@ -37,35 +42,33 @@
         # that one is acked or nacked, the next message in the queue for that
         # ordering key will be sent.
         # If the queue is empty, it means there's a message for that key in
         # flight, but there are no pending messages.
         self._pending_ordered_messages = {}
 
     @property
-    def size(self):
-        """Return the number of messages on hold across ordered and unordered
-        messages.
+    def size(self) -> int:
+        """Return the number of messages on hold across ordered and unordered messages.
 
         Note that this object may still store information about ordered messages
         in flight even if size is zero.
 
         Returns:
-            int: The size value.
+            The size value.
         """
         return self._size
 
-    def get(self):
+    def get(self) -> Optional["subscriber.message.Message"]:
         """ Gets a message from the on-hold queue. A message with an ordering
         key wont be returned if there's another message with the same key in
         flight.
 
         Returns:
-            Optional[google.cloud.pubsub_v1.subscriber.message.Message]: A message
-                that hasn't been sent to the user yet or None if there are no
-                messages available.
+            A message that hasn't been sent to the user yet or ``None`` if there are no
+            messages available.
         """
         while self._messages_on_hold:
             msg = self._messages_on_hold.popleft()
 
             if msg.ordering_key:
                 pending_queue = self._pending_ordered_messages.get(msg.ordering_key)
                 if pending_queue is None:
@@ -84,36 +87,39 @@
                 # Unordered messages can be returned without any
                 # restrictions.
                 self._size = self._size - 1
                 return msg
 
         return None
 
-    def put(self, message):
+    def put(self, message: "subscriber.message.Message") -> None:
         """Put a message on hold.
 
         Args:
-            message (google.cloud.pubsub_v1.subscriber.message.Message): The
-                message to put on hold.
+            message: The message to put on hold.
         """
         self._messages_on_hold.append(message)
         self._size = self._size + 1
 
-    def activate_ordering_keys(self, ordering_keys, schedule_message_callback):
+    def activate_ordering_keys(
+        self,
+        ordering_keys: Iterable[str],
+        schedule_message_callback: Callable[["subscriber.message.Message"], Any],
+    ) -> None:
         """Send the next message in the queue for each of the passed-in
         ordering keys, if they exist. Clean up state for keys that no longer
         have any queued messages.
 
         See comment at streaming_pull_manager.activate_ordering_keys() for more
         detail about the impact of this method on load.
 
         Args:
-            ordering_keys(Sequence[str]): A sequence of ordering keys to
-                activate. May be empty.
-            schedule_message_callback(Callable[google.cloud.pubsub_v1.subscriber.message.Message]):
+            ordering_keys:
+                The ordering keys to activate. May be empty.
+            schedule_message_callback:
                 The callback to call to schedule a message to be sent to the user.
         """
         for key in ordering_keys:
             assert (
                 self._pending_ordered_messages.get(key) is not None
             ), "A message queue should exist for every ordered message in flight."
             next_msg = self._get_next_for_ordering_key(key)
@@ -122,38 +128,39 @@
                 # Note that this may overload the user's `max_bytes` limit, but
                 # not their `max_messages` limit.
                 schedule_message_callback(next_msg)
             else:
                 # No more messages for this ordering key, so do clean-up.
                 self._clean_up_ordering_key(key)
 
-    def _get_next_for_ordering_key(self, ordering_key):
+    def _get_next_for_ordering_key(
+        self, ordering_key: str
+    ) -> Optional["subscriber.message.Message"]:
         """Get next message for ordering key.
 
         The client should call clean_up_ordering_key() if this method returns
         None.
 
         Args:
-            ordering_key (str): Ordering key for which to get the next message.
+            ordering_key: Ordering key for which to get the next message.
 
         Returns:
-            google.cloud.pubsub_v1.subscriber.message.Message|None: The
-                next message for this ordering key or None if there aren't any.
+            The next message for this ordering key or None if there aren't any.
         """
         queue_for_key = self._pending_ordered_messages.get(ordering_key)
         if queue_for_key:
             self._size = self._size - 1
             return queue_for_key.popleft()
         return None
 
-    def _clean_up_ordering_key(self, ordering_key):
+    def _clean_up_ordering_key(self, ordering_key: str) -> None:
         """Clean up state for an ordering key with no pending messages.
 
         Args:
-            ordering_key (str): The ordering key to clean up.
+            ordering_key: The ordering key to clean up.
         """
         message_queue = self._pending_ordered_messages.get(ordering_key)
         assert (
             message_queue is not None
         ), "Cleaning up ordering key that does not exist."
         assert not len(message_queue), (
             "Ordering key must only be removed if there are no messages "
```

### Comparing `google-cloud-pubsub-2.8.0/google/cloud/pubsub_v1/subscriber/_protocol/streaming_pull_manager.py` & `google-cloud-pubsub-2.9.0/google/cloud/pubsub_v1/subscriber/_protocol/streaming_pull_manager.py`

 * *Files 3% similar despite different names*

```diff
@@ -15,14 +15,16 @@
 from __future__ import division
 
 import collections
 import functools
 import itertools
 import logging
 import threading
+import typing
+from typing import Any, Callable, Iterable
 import uuid
 
 import grpc
 
 from google.api_core import bidi
 from google.api_core import exceptions
 from google.cloud.pubsub_v1 import types
@@ -32,14 +34,19 @@
 from google.cloud.pubsub_v1.subscriber._protocol import leaser
 from google.cloud.pubsub_v1.subscriber._protocol import messages_on_hold
 from google.cloud.pubsub_v1.subscriber._protocol import requests
 import google.cloud.pubsub_v1.subscriber.message
 import google.cloud.pubsub_v1.subscriber.scheduler
 from google.pubsub_v1 import types as gapic_types
 
+if typing.TYPE_CHECKING:  # pragma: NO COVER
+    from google.cloud.pubsub_v1 import subscriber
+    from google.cloud.pubsub_v1.subscriber.scheduler import Scheduler
+
+
 _LOGGER = logging.getLogger(__name__)
 _REGULAR_SHUTDOWN_THREAD_NAME = "Thread-RegularStreamShutdown"
 _RPC_ERROR_THREAD_NAME = "Thread-OnRpcTerminated"
 _RETRYABLE_STREAM_ERRORS = (
     exceptions.DeadlineExceeded,
     exceptions.ServiceUnavailable,
     exceptions.InternalServerError,
@@ -51,39 +58,43 @@
 _MAX_LOAD = 1.0
 """The load threshold above which to pause the incoming message stream."""
 
 _RESUME_THRESHOLD = 0.8
 """The load threshold below which to resume the incoming message stream."""
 
 
-def _wrap_as_exception(maybe_exception):
+def _wrap_as_exception(maybe_exception: Any) -> BaseException:
     """Wrap an object as a Python exception, if needed.
 
     Args:
-        maybe_exception (Any): The object to wrap, usually a gRPC exception class.
+        maybe_exception: The object to wrap, usually a gRPC exception class.
 
     Returns:
          The argument itself if an instance of ``BaseException``, otherwise
          the argument represented as an instance of ``Exception`` (sub)class.
     """
     if isinstance(maybe_exception, grpc.RpcError):
         return exceptions.from_grpc_error(maybe_exception)
     elif isinstance(maybe_exception, BaseException):
         return maybe_exception
 
     return Exception(maybe_exception)
 
 
-def _wrap_callback_errors(callback, on_callback_error, message):
+def _wrap_callback_errors(
+    callback: Callable[["google.cloud.pubsub_v1.subscriber.message.Message"], Any],
+    on_callback_error: Callable[[Exception], Any],
+    message: "google.cloud.pubsub_v1.subscriber.message.Message",
+):
     """Wraps a user callback so that if an exception occurs the message is
     nacked.
 
     Args:
-        callback (Callable[None, Message]): The user callback.
-        message (~Message): The Pub/Sub message.
+        callback: The user callback.
+        message: The Pub/Sub message.
     """
     try:
         callback(message)
     except Exception as exc:
         # Note: the likelihood of this failing is extremely low. This just adds
         # a message to a queue, so if this doesn't work the world is in an
         # unrecoverable state and this thread should just bail.
@@ -95,29 +106,29 @@
 
 
 class StreamingPullManager(object):
     """The streaming pull manager coordinates pulling messages from Pub/Sub,
     leasing them, and scheduling them to be processed.
 
     Args:
-        client (~.pubsub_v1.subscriber.client): The subscriber client used
-            to create this instance.
-        subscription (str): The name of the subscription. The canonical
-            format for this is
+        client:
+            The subscriber client used to create this instance.
+        subscription:
+            The name of the subscription. The canonical format for this is
             ``projects/{project}/subscriptions/{subscription}``.
-        flow_control (~google.cloud.pubsub_v1.types.FlowControl): The flow
-            control settings.
-        use_legacy_flow_control (bool):
+        flow_control:
+            The flow control settings.
+        scheduler:
+            The scheduler to use to process messages. If not provided, a thread
+            pool-based scheduler will be used.
+        use_legacy_flow_control:
             If set to ``True``, flow control at the Cloud Pub/Sub server is disabled,
             though client-side flow control is still enabled. If set to ``False``
             (default), both server-side and client-side flow control are enabled.
-        scheduler (~google.cloud.pubsub_v1.scheduler.Scheduler): The scheduler
-            to use to process messages. If not provided, a thread pool-based
-            scheduler will be used.
-        await_callbacks_on_shutdown (bool):
+        await_callbacks_on_shutdown:
             If ``True``, the shutdown thread will wait until all scheduler threads
             terminate and only then proceed with shutting down the remaining running
             helper threads.
 
             If ``False`` (default), the shutdown thread will shut the scheduler down,
             but it will not wait for the currently executing scheduler threads to
             terminate.
@@ -125,20 +136,20 @@
             This setting affects when the on close callbacks get invoked, and
             consequently, when the StreamingPullFuture associated with the stream gets
             resolved.
     """
 
     def __init__(
         self,
-        client,
-        subscription,
-        flow_control=types.FlowControl(),
-        scheduler=None,
-        use_legacy_flow_control=False,
-        await_callbacks_on_shutdown=False,
+        client: "subscriber.Client",
+        subscription: str,
+        flow_control: types.FlowControl = types.FlowControl(),
+        scheduler: "Scheduler" = None,
+        use_legacy_flow_control: bool = False,
+        await_callbacks_on_shutdown: bool = False,
     ):
         self._client = client
         self._subscription = subscription
         self._flow_control = flow_control
         self._use_legacy_flow_control = use_legacy_flow_control
         self._await_callbacks_on_shutdown = await_callbacks_on_shutdown
         self._ack_histogram = histogram.Histogram()
@@ -187,72 +198,65 @@
         # The threads created in ``.open()``.
         self._dispatcher = None
         self._leaser = None
         self._consumer = None
         self._heartbeater = None
 
     @property
-    def is_active(self):
-        """bool: True if this manager is actively streaming.
+    def is_active(self) -> bool:
+        """``True`` if this manager is actively streaming.
 
         Note that ``False`` does not indicate this is complete shut down,
         just that it stopped getting new messages.
         """
         return self._consumer is not None and self._consumer.is_active
 
     @property
-    def flow_control(self):
-        """google.cloud.pubsub_v1.types.FlowControl: The active flow control
-        settings."""
+    def flow_control(self) -> types.FlowControl:
+        """The active flow control settings."""
         return self._flow_control
 
     @property
-    def dispatcher(self):
-        """google.cloud.pubsub_v1.subscriber._protocol.dispatcher.Dispatcher:
-        The dispatcher helper.
-        """
+    def dispatcher(self) -> dispatcher.Dispatcher:
+        """The dispatcher helper."""
         return self._dispatcher
 
     @property
-    def leaser(self):
-        """google.cloud.pubsub_v1.subscriber._protocol.leaser.Leaser:
-        The leaser helper.
-        """
+    def leaser(self) -> leaser.Leaser:
+        """The leaser helper."""
         return self._leaser
 
     @property
-    def ack_histogram(self):
-        """google.cloud.pubsub_v1.subscriber._protocol.histogram.Histogram:
-        The histogram tracking time-to-acknowledge.
-        """
+    def ack_histogram(self) -> histogram.Histogram:
+        """The histogram tracking time-to-acknowledge."""
         return self._ack_histogram
 
     @property
-    def ack_deadline(self):
+    def ack_deadline(self) -> float:
         """Return the current ACK deadline based on historical data without updating it.
 
         Returns:
-            int: The ack deadline.
+            The ack deadline.
         """
         return self._obtain_ack_deadline(maybe_update=False)
 
-    def _obtain_ack_deadline(self, maybe_update: bool) -> int:
+    def _obtain_ack_deadline(self, maybe_update: bool) -> float:
         """The actual `ack_deadline` implementation.
 
         This method is "sticky". It will only perform the computations to check on the
         right ACK deadline if explicitly requested AND if the histogram with past
         time-to-ack data has gained a significant amount of new information.
 
         Args:
-            maybe_update (bool):
+            maybe_update:
                 If ``True``, also update the current ACK deadline before returning it if
                 enough new ACK data has been gathered.
 
         Returns:
-            int: The current ACK deadline in seconds to use.
+            The current ACK deadline in seconds to use.
         """
         with self._ack_deadline_lock:
             if not maybe_update:
                 return self._ack_deadline
 
             target_size = min(
                 self._last_histogram_size * 2, self._last_histogram_size + 100
@@ -269,29 +273,29 @@
                     self.flow_control.max_duration_per_lease_extension,
                     histogram.MIN_ACK_DEADLINE,
                 )
                 self._ack_deadline = min(self._ack_deadline, flow_control_setting)
             return self._ack_deadline
 
     @property
-    def load(self):
+    def load(self) -> float:
         """Return the current load.
 
         The load is represented as a float, where 1.0 represents having
         hit one of the flow control limits, and values between 0.0 and 1.0
         represent how close we are to them. (0.5 means we have exactly half
         of what the flow control setting allows, for example.)
 
         There are (currently) two flow control settings; this property
         computes how close the manager is to each of them, and returns
         whichever value is higher. (It does not matter that we have lots of
         running room on setting A if setting B is over.)
 
         Returns:
-            float: The load value.
+            The load value.
         """
         if self._leaser is None:
             return 0.0
 
         # Messages that are temporarily put on hold are not being delivered to
         # user's callbacks, thus they should not contribute to the flow control
         # load calculation.
@@ -303,55 +307,57 @@
                 (self._leaser.message_count - self._messages_on_hold.size)
                 / self._flow_control.max_messages,
                 (self._leaser.bytes - self._on_hold_bytes)
                 / self._flow_control.max_bytes,
             ]
         )
 
-    def add_close_callback(self, callback):
+    def add_close_callback(
+        self, callback: Callable[["StreamingPullManager", Any], Any],
+    ) -> None:
         """Schedules a callable when the manager closes.
 
         Args:
-            callback (Callable): The method to call.
+            The method to call.
         """
         self._close_callbacks.append(callback)
 
-    def activate_ordering_keys(self, ordering_keys):
+    def activate_ordering_keys(self, ordering_keys: Iterable[str]) -> None:
         """Send the next message in the queue for each of the passed-in
         ordering keys, if they exist. Clean up state for keys that no longer
         have any queued messages.
 
         Since the load went down by one message, it's probably safe to send the
         user another message for the same key. Since the released message may be
         bigger than the previous one, this may increase the load above the maximum.
         This decision is by design because it simplifies MessagesOnHold.
 
         Args:
-            ordering_keys(Sequence[str]): A sequence of ordering keys to
-                activate. May be empty.
+            ordering_keys:
+                A sequence of ordering keys to activate. May be empty.
         """
         with self._pause_resume_lock:
             if self._scheduler is None:
                 return  # We are shutting down, don't try to dispatch any more messages.
 
             self._messages_on_hold.activate_ordering_keys(
                 ordering_keys, self._schedule_message_on_hold
             )
 
-    def maybe_pause_consumer(self):
+    def maybe_pause_consumer(self) -> None:
         """Check the current load and pause the consumer if needed."""
         with self._pause_resume_lock:
             if self.load >= _MAX_LOAD:
                 if self._consumer is not None and not self._consumer.is_paused:
                     _LOGGER.debug(
                         "Message backlog over load at %.2f, pausing.", self.load
                     )
                     self._consumer.pause()
 
-    def maybe_resume_consumer(self):
+    def maybe_resume_consumer(self) -> None:
         """Check the load and held messages and resume the consumer if needed.
 
         If there are messages held internally, release those messages before
         resuming the consumer. That will avoid leaser overload.
         """
         with self._pause_resume_lock:
             # If we have been paused by flow control, check and see if we are
@@ -371,15 +377,15 @@
 
             if self.load < _RESUME_THRESHOLD:
                 _LOGGER.debug("Current load is %.2f, resuming consumer.", self.load)
                 self._consumer.resume()
             else:
                 _LOGGER.debug("Did not resume, current load is %.2f.", self.load)
 
-    def _maybe_release_messages(self):
+    def _maybe_release_messages(self) -> None:
         """Release (some of) the held messages if the current load allows for it.
 
         The method tries to release as many messages as the current leaser load
         would allow. Each released message is added to the lease management,
         and the user callback is scheduled for it.
 
         If there are currently no messages on hold, or if the leaser is
@@ -393,23 +399,23 @@
             if not msg:
                 break
 
             self._schedule_message_on_hold(msg)
             released_ack_ids.append(msg.ack_id)
         self._leaser.start_lease_expiry_timer(released_ack_ids)
 
-    def _schedule_message_on_hold(self, msg):
-        """Schedule a message on hold to be sent to the user and change
-        on-hold-bytes.
+    def _schedule_message_on_hold(
+        self, msg: "google.cloud.pubsub_v1.subscriber.message.Message"
+    ):
+        """Schedule a message on hold to be sent to the user and change on-hold-bytes.
 
         The method assumes the caller has acquired the ``_pause_resume_lock``.
 
         Args:
-            msg (google.cloud.pubsub_v1.message.Message): The message to
-                schedule to be sent to the user.
+            msg: The message to schedule to be sent to the user.
         """
         assert msg, "Message must not be None."
 
         # On-hold bytes goes down, increasing load.
         self._on_hold_bytes -= msg.size
 
         if self._on_hold_bytes < 0:
@@ -422,21 +428,19 @@
             "Released held message, scheduling callback for it, "
             "still on hold %s (bytes %s).",
             self._messages_on_hold.size,
             self._on_hold_bytes,
         )
         self._scheduler.schedule(self._callback, msg)
 
-    def _send_unary_request(self, request):
-        """Send a request using a separate unary request instead of over the
-        stream.
+    def _send_unary_request(self, request: gapic_types.StreamingPullRequest) -> None:
+        """Send a request using a separate unary request instead of over the stream.
 
         Args:
-            request (gapic_types.StreamingPullRequest): The stream request to be
-                mapped into unary requests.
+            request: The stream request to be mapped into unary requests.
         """
         if request.ack_ids:
             self._client.acknowledge(
                 subscription=self._subscription, ack_ids=list(request.ack_ids)
             )
 
         if request.modify_deadline_ack_ids:
@@ -452,15 +456,15 @@
                     subscription=self._subscription,
                     ack_ids=ack_ids,
                     ack_deadline_seconds=deadline,
                 )
 
         _LOGGER.debug("Sent request(s) over unary RPC.")
 
-    def send(self, request):
+    def send(self, request: gapic_types.StreamingPullRequest) -> None:
         """Queue a request to be sent to the RPC.
 
         If a RetryError occurs, the manager shutdown is triggered, and the
         error is re-raised.
         """
         try:
             self._send_unary_request(request)
@@ -477,34 +481,38 @@
                 exc_info=False,
             )
             # The underlying channel has been suffering from a retryable error
             # for too long, time to give up and shut the streaming pull down.
             self._on_rpc_done(exc)
             raise
 
-    def heartbeat(self):
+    def heartbeat(self) -> bool:
         """Sends an empty request over the streaming pull RPC.
 
         Returns:
-            bool: If a heartbeat request has actually been sent.
+            If a heartbeat request has actually been sent.
         """
         if self._rpc is not None and self._rpc.is_active:
             self._rpc.send(gapic_types.StreamingPullRequest())
             return True
 
         return False
 
-    def open(self, callback, on_callback_error):
+    def open(
+        self,
+        callback: Callable[["google.cloud.pubsub_v1.subscriber.message.Message"], Any],
+        on_callback_error: Callable[[Exception], Any],
+    ) -> None:
         """Begin consuming messages.
 
         Args:
-            callback (Callable[None, google.cloud.pubsub_v1.message.Message]):
+            callback:
                 A callback that will be called for each message received on the
                 stream.
-            on_callback_error (Callable[Exception]):
+            on_callback_error:
                 A callable that will be called if an exception is raised in
                 the provided `callback`.
         """
         if self.is_active:
             raise ValueError("This manager is already open.")
 
         if self._closed:
@@ -532,58 +540,63 @@
         _LOGGER.debug(
             "Creating a stream, default ACK deadline set to {} seconds.".format(
                 stream_ack_deadline_seconds
             )
         )
 
         # Create references to threads
+        # pytype: disable=wrong-arg-types
+        # (pytype incorrectly complains about "self" not being the right argument type)
         self._dispatcher = dispatcher.Dispatcher(self, self._scheduler.queue)
         self._consumer = bidi.BackgroundConsumer(self._rpc, self._on_response)
         self._leaser = leaser.Leaser(self)
         self._heartbeater = heartbeater.Heartbeater(self)
+        # pytype: enable=wrong-arg-types
 
         # Start the thread to pass the requests.
         self._dispatcher.start()
 
         # Start consuming messages.
         self._consumer.start()
 
         # Start the lease maintainer thread.
         self._leaser.start()
 
         # Start the stream heartbeater thread.
         self._heartbeater.start()
 
-    def close(self, reason=None):
+    def close(self, reason: Any = None) -> None:
         """Stop consuming messages and shutdown all helper threads.
 
         This method is idempotent. Additional calls will have no effect.
 
         The method does not block, it delegates the shutdown operations to a background
         thread.
 
         Args:
-            reason (Any): The reason to close this. If ``None``, this is considered
+            reason:
+                The reason to close this. If ``None``, this is considered
                 an "intentional" shutdown. This is passed to the callbacks
                 specified via :meth:`add_close_callback`.
         """
         self._regular_shutdown_thread = threading.Thread(
             name=_REGULAR_SHUTDOWN_THREAD_NAME,
             daemon=True,
             target=self._shutdown,
             kwargs={"reason": reason},
         )
         self._regular_shutdown_thread.start()
 
-    def _shutdown(self, reason=None):
+    def _shutdown(self, reason: Any = None) -> None:
         """Run the actual shutdown sequence (stop the stream and all helper threads).
 
         Args:
-            reason (Any): The reason to close the stream. If ``None``, this is
-                considered an "intentional" shutdown.
+            reason:
+                The reason to close the stream. If ``None``, this is considered
+                an "intentional" shutdown.
         """
         with self._closing:
             if self._closed:
                 return
 
             # Stop consuming messages.
             if self.is_active:
@@ -633,27 +646,28 @@
             self._rpc = None
             self._closed = True
             _LOGGER.debug("Finished stopping manager.")
 
             for callback in self._close_callbacks:
                 callback(self, reason)
 
-    def _get_initial_request(self, stream_ack_deadline_seconds):
+    def _get_initial_request(
+        self, stream_ack_deadline_seconds: int
+    ) -> gapic_types.StreamingPullRequest:
         """Return the initial request for the RPC.
 
         This defines the initial request that must always be sent to Pub/Sub
         immediately upon opening the subscription.
 
         Args:
-            stream_ack_deadline_seconds (int):
+            stream_ack_deadline_seconds:
                 The default message acknowledge deadline for the stream.
 
         Returns:
-            google.pubsub_v1.types.StreamingPullRequest: A request
-            suitable for being the first request on the stream (and not
+            A request suitable for being the first request on the stream (and not
             suitable for any other purpose).
         """
         # Any ack IDs that are under lease management need to have their
         # deadline extended immediately.
         if self._leaser is not None:
             # Explicitly copy the list, as it could be modified by another
             # thread.
@@ -675,15 +689,15 @@
                 0 if self._use_legacy_flow_control else self._flow_control.max_bytes
             ),
         )
 
         # Return the initial request.
         return request
 
-    def _on_response(self, response):
+    def _on_response(self, response: gapic_types.StreamingPullResponse) -> None:
         """Process all received Pub/Sub messages.
 
         For each message, send a modified acknowledgment request to the
         server. This prevents expiration of the message due to buffering by
         gRPC or proxy/firewall. This makes the server and client expiration
         timer closer to each other thus preventing the message being
         redelivered multiple times.
@@ -735,57 +749,57 @@
                 )
                 self.leaser.add([req])
 
             self._maybe_release_messages()
 
         self.maybe_pause_consumer()
 
-    def _should_recover(self, exception):
+    def _should_recover(self, exception: Exception) -> bool:
         """Determine if an error on the RPC stream should be recovered.
 
         If the exception is one of the retryable exceptions, this will signal
         to the consumer thread that it should "recover" from the failure.
 
         This will cause the stream to exit when it returns :data:`False`.
 
         Returns:
-            bool: Indicates if the caller should recover or shut down.
+            Indicates if the caller should recover or shut down.
             Will be :data:`True` if the ``exception`` is "acceptable", i.e.
             in a list of retryable / idempotent exceptions.
         """
         exception = _wrap_as_exception(exception)
         # If this is in the list of idempotent exceptions, then we want to
         # recover.
         if isinstance(exception, _RETRYABLE_STREAM_ERRORS):
             _LOGGER.info("Observed recoverable stream error %s", exception)
             return True
         _LOGGER.info("Observed non-recoverable stream error %s", exception)
         return False
 
-    def _should_terminate(self, exception):
+    def _should_terminate(self, exception: Exception) -> bool:
         """Determine if an error on the RPC stream should be terminated.
 
         If the exception is one of the terminating exceptions, this will signal
         to the consumer thread that it should terminate.
 
         This will cause the stream to exit when it returns :data:`True`.
 
         Returns:
-            bool: Indicates if the caller should terminate or attempt recovery.
+            Indicates if the caller should terminate or attempt recovery.
             Will be :data:`True` if the ``exception`` is "acceptable", i.e.
             in a list of terminating exceptions.
         """
         exception = _wrap_as_exception(exception)
         if isinstance(exception, _TERMINATING_STREAM_ERRORS):
             _LOGGER.info("Observed terminating stream error %s", exception)
             return True
         _LOGGER.info("Observed non-terminating stream error %s", exception)
         return False
 
-    def _on_rpc_done(self, future):
+    def _on_rpc_done(self, future: Any) -> None:
         """Triggered whenever the underlying RPC terminates without recovery.
 
         This is typically triggered from one of two threads: the background
         consumer thread (when calling ``recv()`` produces a non-recoverable
         error) or the grpc management thread (when cancelling the RPC).
 
         This method is *non-blocking*. It will start another thread to deal
```

### Comparing `google-cloud-pubsub-2.8.0/google/cloud/pubsub_v1/subscriber/client.py` & `google-cloud-pubsub-2.9.0/google/cloud/pubsub_v1/subscriber/client.py`

 * *Files 12% similar despite different names*

```diff
@@ -12,24 +12,29 @@
 # See the License for the specific language governing permissions and
 # limitations under the License.
 
 from __future__ import absolute_import
 
 import os
 import pkg_resources
+import typing
+from typing import Any, Callable, Optional, Sequence, Union
 
 from google.auth.credentials import AnonymousCredentials
 from google.oauth2 import service_account
 
 from google.cloud.pubsub_v1 import _gapic
 from google.cloud.pubsub_v1 import types
 from google.cloud.pubsub_v1.subscriber import futures
 from google.cloud.pubsub_v1.subscriber._protocol import streaming_pull_manager
 from google.pubsub_v1.services.subscriber import client as subscriber_client
 
+if typing.TYPE_CHECKING:  # pragma: NO COVER
+    from google.cloud.pubsub_v1 import subscriber
+
 
 try:
     __version__ = pkg_resources.get_distribution("google-cloud-pubsub").version
 except pkg_resources.DistributionNotFound:
     # Distribution might not be available if we are not running from within
     # a PIP package.
     __version__ = "0.0"
@@ -46,15 +51,15 @@
     """A subscriber client for Google Cloud Pub/Sub.
 
     This creates an object that is capable of subscribing to messages.
     Generally, you can instantiate this client with no arguments, and you
     get sensible defaults.
 
     Args:
-        kwargs (dict): Any additional arguments provided are sent as keyword
+        kwargs: Any additional arguments provided are sent as keyword
             keyword arguments to the underlying
             :class:`~google.cloud.pubsub_v1.gapic.subscriber_client.SubscriberClient`.
             Generally you should not need to set additional keyword
             arguments. Optionally, regional endpoints can be set via
             ``client_options`` that takes a single key-value pair that
             defines the endpoint.
 
@@ -68,15 +73,15 @@
             # Optional
             client_options = {
                 "api_endpoint": REGIONAL_ENDPOINT
             }
         )
     """
 
-    def __init__(self, **kwargs):
+    def __init__(self, **kwargs: Any):
         # Sanity check: Is our goal to use the emulator?
         # If so, create a grpc insecure channel with the emulator host
         # as the target.
         if os.environ.get("PUBSUB_EMULATOR_HOST"):
             kwargs["client_options"] = {
                 "api_endpoint": os.environ.get("PUBSUB_EMULATOR_HOST")
             }
@@ -84,64 +89,63 @@
 
         # Instantiate the underlying GAPIC client.
         self._api = subscriber_client.SubscriberClient(**kwargs)
         self._target = self._api._transport._host
         self._closed = False
 
     @classmethod
-    def from_service_account_file(cls, filename, **kwargs):
+    def from_service_account_file(cls, filename: str, **kwargs: Any) -> "Client":
         """Creates an instance of this client using the provided credentials
         file.
 
         Args:
-            filename (str): The path to the service account private key json
-                file.
+            filename: The path to the service account private key json file.
             kwargs: Additional arguments to pass to the constructor.
 
         Returns:
             A Subscriber :class:`~google.cloud.pubsub_v1.subscriber.client.Client`
             instance that is the constructed client.
         """
         credentials = service_account.Credentials.from_service_account_file(filename)
         kwargs["credentials"] = credentials
         return cls(**kwargs)
 
     from_service_account_json = from_service_account_file
 
     @property
-    def target(self):
+    def target(self) -> str:
         """Return the target (where the API is).
 
         Returns:
-            str: The location of the API.
+            The location of the API.
         """
         return self._target
 
     @property
-    def api(self):
+    def api(self) -> subscriber_client.SubscriberClient:
         """The underlying gapic API client."""
         return self._api
 
     @property
     def closed(self) -> bool:
         """Return whether the client has been closed and cannot be used anymore.
 
         .. versionadded:: 2.8.0
         """
         return self._closed
 
     def subscribe(
         self,
-        subscription,
-        callback,
-        flow_control=(),
-        scheduler=None,
-        use_legacy_flow_control=False,
-        await_callbacks_on_shutdown=False,
-    ):
+        subscription: str,
+        callback: Callable[["subscriber.message.Message"], Any],
+        flow_control: Union[types.FlowControl, Sequence] = (),
+        scheduler: Optional["subscriber.scheduler.Scheduler"] = None,
+        use_legacy_flow_control: bool = False,
+        await_callbacks_on_shutdown: bool = False,
+    ) -> futures.StreamingPullFuture:
         """Asynchronously start receiving messages on a given subscription.
 
         This method starts a background thread to begin pulling messages from
         a Pub/Sub subscription and scheduling them to be processed using the
         provided ``callback``.
 
         The ``callback`` will be called with an individual
@@ -197,47 +201,46 @@
             try:
                 future.result()
             except KeyboardInterrupt:
                 future.cancel()  # Trigger the shutdown.
                 future.result()  # Block until the shutdown is complete.
 
         Args:
-            subscription (str): The name of the subscription. The
-                subscription should have already been created (for example,
-                by using :meth:`create_subscription`).
-            callback (Callable[~google.cloud.pubsub_v1.subscriber.message.Message]):
+            subscription:
+                The name of the subscription. The subscription should have already been
+                created (for example, by using :meth:`create_subscription`).
+            callback:
                 The callback function. This function receives the message as
                 its only argument and will be called from a different thread/
                 process depending on the scheduling strategy.
-            flow_control (~google.cloud.pubsub_v1.types.FlowControl): The flow control
-                settings. Use this to prevent situations where you are
+            flow_control:
+                The flow control settings. Use this to prevent situations where you are
                 inundated with too many messages at once.
-            scheduler (~google.cloud.pubsub_v1.subscriber.scheduler.Scheduler): An optional
-                *scheduler* to use when executing the callback. This controls
-                how callbacks are executed concurrently. This object must not be shared
-                across multiple SubscriberClients.
+            scheduler:
+                An optional *scheduler* to use when executing the callback. This
+                controls how callbacks are executed concurrently. This object must not
+                be shared across multiple ``SubscriberClient`` instances.
             use_legacy_flow_control (bool):
                 If set to ``True``, flow control at the Cloud Pub/Sub server is disabled,
                 though client-side flow control is still enabled. If set to ``False``
                 (default), both server-side and client-side flow control are enabled.
-            await_callbacks_on_shutdown (bool):
+            await_callbacks_on_shutdown:
                 If ``True``, after canceling the returned future, the latter's
                 ``result()`` method will block until the background stream and its
                 helper threads have been terminated, and all currently executing message
                 callbacks are done processing.
 
                 If ``False`` (default), the returned future's ``result()`` method will
                 not block after canceling the future. The method will instead return
                 immediately after the background stream and its helper threads have been
                 terminated, but some of the message callback threads might still be
                 running at that point.
 
         Returns:
-            A :class:`~google.cloud.pubsub_v1.subscriber.futures.StreamingPullFuture`
-            instance that can be used to manage the background stream.
+            A future instance that can be used to manage the background stream.
         """
         flow_control = types.FlowControl(*flow_control)
 
         manager = streaming_pull_manager.StreamingPullManager(
             self,
             subscription,
             flow_control=flow_control,
@@ -248,25 +251,25 @@
 
         future = futures.StreamingPullFuture(manager)
 
         manager.open(callback=callback, on_callback_error=future.set_exception)
 
         return future
 
-    def close(self):
+    def close(self) -> None:
         """Close the underlying channel to release socket resources.
 
         After a channel has been closed, the client instance cannot be used
         anymore.
 
         This method is idempotent.
         """
         self.api._transport.grpc_channel.close()
         self._closed = True
 
-    def __enter__(self):
+    def __enter__(self) -> "Client":
         if self._closed:
             raise RuntimeError("Closed subscriber cannot be used as context manager.")
         return self
 
     def __exit__(self, exc_type, exc_val, exc_tb):
         self.close()
```

### Comparing `google-cloud-pubsub-2.8.0/google/cloud/pubsub_v1/subscriber/futures.py` & `google-cloud-pubsub-2.9.0/google/cloud/pubsub_v1/subscriber/futures.py`

 * *Files 16% similar despite different names*

```diff
@@ -10,33 +10,42 @@
 # distributed under the License is distributed on an "AS IS" BASIS,
 # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 # See the License for the specific language governing permissions and
 # limitations under the License.
 
 from __future__ import absolute_import
 
+import typing
+from typing import Any
+
 from google.cloud.pubsub_v1 import futures
 
 
+if typing.TYPE_CHECKING:  # pragma: NO COVER
+    from google.cloud.pubsub_v1.subscriber._protocol.streaming_pull_manager import (
+        StreamingPullManager,
+    )
+
+
 class StreamingPullFuture(futures.Future):
     """Represents a process that asynchronously performs streaming pull and
     schedules messages to be processed.
 
     This future is resolved when the process is stopped (via :meth:`cancel`) or
     if it encounters an unrecoverable error. Calling `.result()` will cause
     the calling thread to block indefinitely.
     """
 
-    def __init__(self, manager):
+    def __init__(self, manager: "StreamingPullManager"):
         super(StreamingPullFuture, self).__init__()
         self.__manager = manager
         self.__manager.add_close_callback(self._on_close_callback)
         self.__cancelled = False
 
-    def _on_close_callback(self, manager, result):
+    def _on_close_callback(self, manager: "StreamingPullManager", result: Any):
         if self.done():
             # The future has already been resolved in a different thread,
             # nothing to do on the streaming pull manager shutdown.
             return
 
         if result is None:
             self.set_result(True)
@@ -53,13 +62,13 @@
            :meth:`result()` after cancelling the future.
         """
         # NOTE: We circumvent the base future's self._state to track the cancellation
         # state, as this state has different meaning with streaming pull futures.
         self.__cancelled = True
         return self.__manager.close()
 
-    def cancelled(self):
+    def cancelled(self) -> bool:
         """
-        returns:
-            bool: ``True`` if the subscription has been cancelled.
+        Returns:
+            ``True`` if the subscription has been cancelled.
         """
         return self.__cancelled
```

### Comparing `google-cloud-pubsub-2.8.0/google/cloud/pubsub_v1/subscriber/message.py` & `google-cloud-pubsub-2.9.0/google/cloud/pubsub_v1/subscriber/message.py`

 * *Files 4% similar despite different names*

```diff
@@ -14,38 +14,47 @@
 
 from __future__ import absolute_import
 
 import datetime as dt
 import json
 import math
 import time
+import typing
+from typing import Optional
 
 from google.cloud.pubsub_v1.subscriber._protocol import requests
 
+if typing.TYPE_CHECKING:  # pragma: NO COVER
+    import datetime
+    import queue
+    from google.cloud.pubsub_v1 import types
+    from google.protobuf.internal import containers
+
 
 _MESSAGE_REPR = """\
 Message {{
   data: {!r}
   ordering_key: {!r}
   attributes: {}
 }}"""
 
 
-def _indent(lines, prefix="  "):
+def _indent(lines: str, prefix: str = "  ") -> str:
     """Indent some text.
 
     Note that this is present as ``textwrap.indent``, but not in Python 2.
 
     Args:
-        lines (str): The newline delimited string to be indented.
-        prefix (Optional[str]): The prefix to indent each line with. Default
-            to two spaces.
+        lines:
+            The newline delimited string to be indented.
+        prefix:
+            The prefix to indent each line with. Defaults to two spaces.
 
     Returns:
-        str: The newly indented content.
+        The newly indented content.
     """
     indented = []
     for line in lines.split("\n"):
         indented.append(prefix + line)
     return "\n".join(indented)
 
 
@@ -56,46 +65,55 @@
     :class:`~.pubsub_v1.subscriber.message.Message` objects is to receive
     them in callbacks on subscriptions; most users should never have a need
     to instantiate them by hand. (The exception to this is if you are
     implementing a custom subclass to
     :class:`~.pubsub_v1.subscriber._consumer.Consumer`.)
 
     Attributes:
-        message_id (str): The message ID. In general, you should not need
-            to use this directly.
-        data (bytes): The data in the message. Note that this will be a
-            :class:`bytes`, not a text string.
-        attributes (.ScalarMapContainer): The attributes sent along with the
-            message. See :attr:`attributes` for more information on this type.
-        publish_time (datetime): The time that this message was originally
-            published.
+        message_id:
+            The message ID. In general, you should not need to use this directly.
+        data:
+            The data in the message. Note that this will be a :class:`bytes`,
+            not a text string.
+        attributes:
+            The attributes sent along with the message. See :attr:`attributes` for more
+            information on this type.
+        publish_time:
+            The time that this message was originally published.
     """
 
-    def __init__(self, message, ack_id, delivery_attempt, request_queue):
+    def __init__(  # pytype: disable=module-attr
+        self,
+        message: "types.PubsubMessage._meta._pb",
+        ack_id: str,
+        delivery_attempt: int,
+        request_queue: "queue.Queue",
+    ):
         """Construct the Message.
 
         .. note::
 
             This class should not be constructed directly; it is the
             responsibility of :class:`BasePolicy` subclasses to do so.
 
         Args:
-            message (`pubsub_v1.types.PubsubMessage._meta._pb`):
+            message:
                 The message received from Pub/Sub. For performance reasons it should be
                 the raw protobuf message normally wrapped by
                 :class:`~pubsub_v1.types.PubsubMessage`. A raw message can be obtained
                 from a  :class:`~pubsub_v1.types.PubsubMessage` instance through the
                 latter's ``._pb`` attribute.
-            ack_id (str): The ack_id received from Pub/Sub.
-            delivery_attempt (int): The delivery attempt counter received
-                from Pub/Sub if a DeadLetterPolicy is set on the subscription,
-                and zero otherwise.
-            request_queue (queue.Queue): A queue provided by the policy that
-                can accept requests; the policy is responsible for handling
-                those requests.
+            ack_id:
+                The ack_id received from Pub/Sub.
+            delivery_attempt:
+                The delivery attempt counter received from Pub/Sub if a DeadLetterPolicy
+                is set on the subscription, and zero otherwise.
+            request_queue:
+                A queue provided by the policy that can accept requests; the policy is
+                responsible for handling those requests.
         """
         self._message = message
         self._ack_id = ack_id
         self._delivery_attempt = delivery_attempt if delivery_attempt > 0 else None
         self._request_queue = request_queue
         self.message_id = message.message_id
 
@@ -127,87 +145,87 @@
         )
         pretty_attrs = _indent(pretty_attrs)
         # We don't actually want the first line indented.
         pretty_attrs = pretty_attrs.lstrip()
         return _MESSAGE_REPR.format(abbv_data, str(self.ordering_key), pretty_attrs)
 
     @property
-    def attributes(self):
+    def attributes(self) -> "containers.ScalarMap":
         """Return the attributes of the underlying Pub/Sub Message.
 
         .. warning::
 
-            A ``ScalarMapContainer`` behaves slightly differently than a
+            A ``ScalarMap`` behaves slightly differently than a
             ``dict``. For a Pub / Sub message this is a ``string->string`` map.
             When trying to access a value via ``map['key']``, if the key is
             not in the map, then the default value for the string type will
             be returned, which is an empty string. It may be more intuitive
             to just cast the map to a ``dict`` or to one use ``map.get``.
 
         Returns:
-            .ScalarMapContainer: The message's attributes. This is a
-            ``dict``-like object provided by ``google.protobuf``.
+            The message's attributes. This is a ``dict``-like object provided by
+            ``google.protobuf``.
         """
         return self._attributes
 
     @property
-    def data(self):
+    def data(self) -> bytes:
         """Return the data for the underlying Pub/Sub Message.
 
         Returns:
-            bytes: The message data. This is always a bytestring; if you
-                want a text string, call :meth:`bytes.decode`.
+            The message data. This is always a bytestring; if you want a text string,
+            call :meth:`bytes.decode`.
         """
         return self._data
 
     @property
-    def publish_time(self):
+    def publish_time(self) -> "datetime.datetime":
         """Return the time that the message was originally published.
 
         Returns:
-            datetime: The date and time that the message was published.
+            The date and time that the message was published.
         """
         return self._publish_time
 
     @property
-    def ordering_key(self):
-        """str: the ordering key used to publish the message."""
+    def ordering_key(self) -> str:
+        """The ordering key used to publish the message."""
         return self._ordering_key
 
     @property
-    def size(self):
+    def size(self) -> int:
         """Return the size of the underlying message, in bytes."""
         return self._size
 
     @property
-    def ack_id(self):
-        """str: the ID used to ack the message."""
+    def ack_id(self) -> str:
+        """the ID used to ack the message."""
         return self._ack_id
 
     @property
-    def delivery_attempt(self):
+    def delivery_attempt(self) -> Optional[int]:
         """The delivery attempt counter is 1 + (the sum of number of NACKs
         and number of ack_deadline exceeds) for this message. It is set to None
         if a DeadLetterPolicy is not set on the subscription.
 
         A NACK is any call to ModifyAckDeadline with a 0 deadline. An ack_deadline
         exceeds event is whenever a message is not acknowledged within
         ack_deadline. Note that ack_deadline is initially
         Subscription.ackDeadlineSeconds, but may get extended automatically by
         the client library.
 
         The first delivery of a given message will have this value as 1. The value
         is calculated at best effort and is approximate.
 
         Returns:
-            Optional[int]: The delivery attempt counter or None.
+            The delivery attempt counter or ``None``.
         """
         return self._delivery_attempt
 
-    def ack(self):
+    def ack(self) -> None:
         """Acknowledge the given message.
 
         Acknowledging a message in Pub/Sub means that you are done
         with it, and it will not be delivered to this subscription again.
         You should avoid acknowledging messages until you have
         *finished* processing them, so that in the event of a failure,
         you receive the message again.
@@ -223,15 +241,15 @@
                 ack_id=self._ack_id,
                 byte_size=self.size,
                 time_to_ack=time_to_ack,
                 ordering_key=self.ordering_key,
             )
         )
 
-    def drop(self):
+    def drop(self) -> None:
         """Release the message from lease management.
 
         This informs the policy to no longer hold on to the lease for this
         message. Pub/Sub will re-deliver the message if it is not acknowledged
         before the existing lease expires.
 
         .. warning::
@@ -242,34 +260,35 @@
         """
         self._request_queue.put(
             requests.DropRequest(
                 ack_id=self._ack_id, byte_size=self.size, ordering_key=self.ordering_key
             )
         )
 
-    def modify_ack_deadline(self, seconds):
+    def modify_ack_deadline(self, seconds: int) -> None:
         """Resets the deadline for acknowledgement.
 
         New deadline will be the given value of seconds from now.
 
         The default implementation handles this for you; you should not need
         to manually deal with setting ack deadlines. The exception case is
         if you are implementing your own custom subclass of
         :class:`~.pubsub_v1.subcriber._consumer.Consumer`.
 
         Args:
-            seconds (int): The number of seconds to set the lease deadline
-                to. This should be between 0 and 600. Due to network latency,
-                values below 10 are advised against.
+            seconds:
+                The number of seconds to set the lease deadline to. This should be
+                between 0 and 600. Due to network latency, values below 10 are advised
+                against.
         """
         self._request_queue.put(
             requests.ModAckRequest(ack_id=self._ack_id, seconds=seconds)
         )
 
-    def nack(self):
+    def nack(self) -> None:
         """Decline to acknowldge the given message.
 
         This will cause the message to be re-delivered to the subscription.
         """
         self._request_queue.put(
             requests.NackRequest(
                 ack_id=self._ack_id, byte_size=self.size, ordering_key=self.ordering_key
```

### Comparing `google-cloud-pubsub-2.8.0/google/cloud/pubsub_v1/subscriber/scheduler.py` & `google-cloud-pubsub-2.9.0/google/cloud/pubsub_v1/subscriber/scheduler.py`

 * *Files 16% similar despite different names*

```diff
@@ -17,132 +17,142 @@
 These are used by the subscriber to call the user-provided callback to process
 each message.
 """
 
 import abc
 import concurrent.futures
 import queue
+import typing
+from typing import Callable, List, Optional
 import warnings
 
+if typing.TYPE_CHECKING:  # pragma: NO COVER
+    from google.cloud import pubsub_v1
+
 
 class Scheduler(metaclass=abc.ABCMeta):
     """Abstract base class for schedulers.
 
     Schedulers are used to schedule callbacks asynchronously.
     """
 
     @property
     @abc.abstractmethod
-    def queue(self):  # pragma: NO COVER
+    def queue(self) -> queue.Queue:  # pragma: NO COVER
         """Queue: A concurrency-safe queue specific to the underlying
         concurrency implementation.
 
         This queue is used to send messages *back* to the scheduling actor.
         """
         raise NotImplementedError
 
     @abc.abstractmethod
-    def schedule(self, callback, *args, **kwargs):  # pragma: NO COVER
+    def schedule(self, callback: Callable, *args, **kwargs) -> None:  # pragma: NO COVER
         """Schedule the callback to be called asynchronously.
 
         Args:
-            callback (Callable): The function to call.
-            args: Positional arguments passed to the function.
-            kwargs: Key-word arguments passed to the function.
+            callback: The function to call.
+            args: Positional arguments passed to the callback.
+            kwargs: Key-word arguments passed to the callback.
 
         Returns:
             None
         """
         raise NotImplementedError
 
     @abc.abstractmethod
-    def shutdown(self, await_msg_callbacks=False):  # pragma: NO COVER
+    def shutdown(
+        self, await_msg_callbacks: bool = False
+    ) -> List["pubsub_v1.subscriber.message.Message"]:  # pragma: NO COVER
         """Shuts down the scheduler and immediately end all pending callbacks.
 
         Args:
-            await_msg_callbacks (bool):
+            await_msg_callbacks:
                 If ``True``, the method will block until all currently executing
                 callbacks are done processing. If ``False`` (default), the
                 method will not wait for the currently running callbacks to complete.
 
         Returns:
-            List[pubsub_v1.subscriber.message.Message]:
-                The messages submitted to the scheduler that were not yet dispatched
-                to their callbacks.
-                It is assumed that each message was submitted to the scheduler as the
-                first positional argument to the provided callback.
+            The messages submitted to the scheduler that were not yet dispatched
+            to their callbacks.
+            It is assumed that each message was submitted to the scheduler as the
+            first positional argument to the provided callback.
         """
         raise NotImplementedError
 
 
-def _make_default_thread_pool_executor():
+def _make_default_thread_pool_executor() -> concurrent.futures.ThreadPoolExecutor:
     return concurrent.futures.ThreadPoolExecutor(
         max_workers=10, thread_name_prefix="ThreadPoolExecutor-ThreadScheduler"
     )
 
 
 class ThreadScheduler(Scheduler):
     """A thread pool-based scheduler. It must not be shared across
        SubscriberClients.
 
     This scheduler is useful in typical I/O-bound message processing.
 
     Args:
-        executor(concurrent.futures.ThreadPoolExecutor): An optional executor
-            to use. If not specified, a default one will be created.
+        executor:
+            An optional executor to use. If not specified, a default one
+            will be created.
     """
 
-    def __init__(self, executor=None):
+    def __init__(
+        self, executor: Optional[concurrent.futures.ThreadPoolExecutor] = None
+    ):
         self._queue = queue.Queue()
         if executor is None:
             self._executor = _make_default_thread_pool_executor()
         else:
             self._executor = executor
 
     @property
     def queue(self):
         """Queue: A thread-safe queue used for communication between callbacks
         and the scheduling thread."""
         return self._queue
 
-    def schedule(self, callback, *args, **kwargs):
+    def schedule(self, callback: Callable, *args, **kwargs) -> None:
         """Schedule the callback to be called asynchronously in a thread pool.
 
         Args:
-            callback (Callable): The function to call.
-            args: Positional arguments passed to the function.
-            kwargs: Key-word arguments passed to the function.
+            callback: The function to call.
+            args: Positional arguments passed to the callback.
+            kwargs: Key-word arguments passed to the callback.
 
         Returns:
             None
         """
         try:
             self._executor.submit(callback, *args, **kwargs)
         except RuntimeError:
             warnings.warn(
                 "Scheduling a callback after executor shutdown.",
                 category=RuntimeWarning,
                 stacklevel=2,
             )
 
-    def shutdown(self, await_msg_callbacks=False):
+    def shutdown(
+        self, await_msg_callbacks: bool = False
+    ) -> List["pubsub_v1.subscriber.message.Message"]:
         """Shut down the scheduler and immediately end all pending callbacks.
 
         Args:
-            await_msg_callbacks (bool):
+            await_msg_callbacks:
                 If ``True``, the method will block until all currently executing
                 executor threads are done processing. If ``False`` (default), the
                 method will not wait for the currently running threads to complete.
 
         Returns:
-            List[pubsub_v1.subscriber.message.Message]:
-                The messages submitted to the scheduler that were not yet dispatched
-                to their callbacks.
-                It is assumed that each message was submitted to the scheduler as the
-                first positional argument to the provided callback.
+            The messages submitted to the scheduler that were not yet dispatched
+            to their callbacks.
+            It is assumed that each message was submitted to the scheduler as the
+            first positional argument to the provided callback.
         """
         dropped_messages = []
 
         # Drop all pending item from the executor. Without this, the executor will also
         # try to process any pending work items before termination, which is undesirable.
         #
         # TODO: Replace the logic below by passing `cancel_futures=True` to shutdown()
```

### Comparing `google-cloud-pubsub-2.8.0/google/cloud/pubsub_v1/types.py` & `google-cloud-pubsub-2.9.0/google/cloud/pubsub_v1/types.py`

 * *Files 11% similar despite different names*

```diff
@@ -14,14 +14,16 @@
 
 from __future__ import absolute_import
 
 import collections
 import enum
 import inspect
 import sys
+import typing
+from typing import Dict, NamedTuple
 
 import proto
 
 from google.api import http_pb2
 from google.api_core import gapic_v1
 from google.iam.v1 import iam_policy_pb2
 from google.iam.v1 import policy_pb2
@@ -33,149 +35,140 @@
 from google.protobuf import timestamp_pb2
 
 from google.api_core.protobuf_helpers import get_messages
 
 from google.pubsub_v1.types import pubsub as pubsub_gapic_types
 
 
+if typing.TYPE_CHECKING:  # pragma: NO COVER
+    from types import ModuleType
+    from google.api_core import retry as retries
+    from google.pubsub_v1 import types as gapic_types
+
+
 # Define the default values for batching.
 #
 # This class is used when creating a publisher or subscriber client, and
 # these settings can be altered to tweak Pub/Sub behavior.
 # The defaults should be fine for most use cases.
-BatchSettings = collections.namedtuple(
-    "BatchSettings", ["max_bytes", "max_latency", "max_messages"]
-)
-BatchSettings.__new__.__defaults__ = (
-    1 * 1000 * 1000,  # max_bytes: 1 MB
-    0.01,  # max_latency: 10 ms
-    100,  # max_messages: 100
-)
-BatchSettings.__doc__ = "The settings for batch publishing the messages."
-BatchSettings.max_bytes.__doc__ = (
-    "The maximum total size of the messages to collect before automatically "
-    "publishing the batch, including any byte size overhead of the publish "
-    "request itself. The maximum value is bound by the server-side limit of "
-    "10_000_000 bytes."
-)
-BatchSettings.max_latency.__doc__ = (
-    "The maximum number of seconds to wait for additional messages before "
-    "automatically publishing the batch."
-)
-BatchSettings.max_messages.__doc__ = (
-    "The maximum number of messages to collect before automatically "
-    "publishing the batch."
-)
+class BatchSettings(NamedTuple):
+    """The settings for batch publishing the messages."""
+
+    max_bytes: int = 1 * 1000 * 1000  # 1 MB
+    (
+        "The maximum total size of the messages to collect before automatically "
+        "publishing the batch, including any byte size overhead of the publish "
+        "request itself. The maximum value is bound by the server-side limit of "
+        "10_000_000 bytes."
+    )
+
+    max_latency: float = 0.01  # 10 ms
+    (
+        "The maximum number of seconds to wait for additional messages before "
+        "automatically publishing the batch."
+    )
+
+    max_messages: int = 100
+    (
+        "The maximum number of messages to collect before automatically "
+        "publishing the batch."
+    )
 
 
 class LimitExceededBehavior(str, enum.Enum):
     """The possible actions when exceeding the publish flow control limits."""
 
     IGNORE = "ignore"
     BLOCK = "block"
     ERROR = "error"
 
 
-PublishFlowControl = collections.namedtuple(
-    "PublishFlowControl", ["message_limit", "byte_limit", "limit_exceeded_behavior"]
-)
-PublishFlowControl.__new__.__defaults__ = (
-    10 * BatchSettings.__new__.__defaults__[2],  # message limit
-    10 * BatchSettings.__new__.__defaults__[0],  # byte limit
-    LimitExceededBehavior.IGNORE,  # desired behavior
-)
-PublishFlowControl.__doc__ = "The client flow control settings for message publishing."
-PublishFlowControl.message_limit.__doc__ = (
-    "The maximum number of messages awaiting to be published."
-)
-PublishFlowControl.byte_limit.__doc__ = (
-    "The maximum total size of messages awaiting to be published."
-)
-PublishFlowControl.limit_exceeded_behavior.__doc__ = (
-    "The action to take when publish flow control limits are exceeded."
-)
+class PublishFlowControl(NamedTuple):
+    """The client flow control settings for message publishing."""
+
+    message_limit: int = 10 * BatchSettings.__new__.__defaults__[2]
+    """The maximum number of messages awaiting to be published."""
+
+    byte_limit: int = 10 * BatchSettings.__new__.__defaults__[0]
+    """The maximum total size of messages awaiting to be published."""
+
+    limit_exceeded_behavior: LimitExceededBehavior = LimitExceededBehavior.IGNORE
+    """The action to take when publish flow control limits are exceeded."""
+
 
 # Define the default publisher options.
 #
 # This class is used when creating a publisher client to pass in options
 # to enable/disable features.
-PublisherOptions = collections.namedtuple(
-    "PublisherOptions", ["enable_message_ordering", "flow_control", "retry", "timeout"]
-)
-PublisherOptions.__new__.__defaults__ = (
-    False,  # enable_message_ordering: False
-    PublishFlowControl(),  # default flow control settings
-    gapic_v1.method.DEFAULT,  # use default api_core value for retry
-    gapic_v1.method.DEFAULT,  # use default api_core value for timeout
-)
-PublisherOptions.__doc__ = "The options for the publisher client."
-PublisherOptions.enable_message_ordering.__doc__ = (
-    "Whether to order messages in a batch by a supplied ordering key."
-)
-PublisherOptions.flow_control.__doc__ = (
-    "Flow control settings for message publishing by the client. By default "
-    "the publisher client does not do any throttling."
-)
-PublisherOptions.retry.__doc__ = (
-    "Retry settings for message publishing by the client. This should be "
-    "an instance of :class:`google.api_core.retry.Retry`."
-)
-PublisherOptions.timeout.__doc__ = (
-    "Timeout settings for message publishing by the client. It should be compatible "
-    "with :class:`~.pubsub_v1.types.TimeoutType`."
-)
+class PublisherOptions(NamedTuple):
+    """The options for the publisher client."""
+
+    enable_message_ordering: bool = False
+    """Whether to order messages in a batch by a supplied ordering key."""
+
+    flow_control: PublishFlowControl = PublishFlowControl()
+    (
+        "Flow control settings for message publishing by the client. By default "
+        "the publisher client does not do any throttling."
+    )
+
+    retry: "retries.Retry" = gapic_v1.method.DEFAULT  # use api_core default
+    (
+        "Retry settings for message publishing by the client. This should be "
+        "an instance of :class:`google.api_core.retry.Retry`."
+    )
+
+    timeout: "gapic_types.TimeoutType" = gapic_v1.method.DEFAULT  # use api_core default
+    (
+        "Timeout settings for message publishing by the client. It should be "
+        "compatible with :class:`~.pubsub_v1.types.TimeoutType`."
+    )
+
 
 # Define the type class and default values for flow control settings.
 #
 # This class is used when creating a publisher or subscriber client, and
 # these settings can be altered to tweak Pub/Sub behavior.
 # The defaults should be fine for most use cases.
-FlowControl = collections.namedtuple(
-    "FlowControl",
-    [
-        "max_bytes",
-        "max_messages",
-        "max_lease_duration",
-        "max_duration_per_lease_extension",
-    ],
-)
-FlowControl.__new__.__defaults__ = (
-    100 * 1024 * 1024,  # max_bytes: 100mb
-    1000,  # max_messages: 1000
-    1 * 60 * 60,  # max_lease_duration: 1 hour.
-    0,  # max_duration_per_lease_extension: disabled
-)
-FlowControl.__doc__ = (
-    "The settings for controlling the rate at which messages are pulled "
-    "with an asynchronous subscription."
-)
-FlowControl.max_bytes.__doc__ = (
-    "The maximum total size of received - but not yet processed - messages "
-    "before pausing the message stream."
-)
-FlowControl.max_messages.__doc__ = (
-    "The maximum number of received - but not yet processed - messages before "
-    "pausing the message stream."
-)
-FlowControl.max_lease_duration.__doc__ = (
-    "The maximum amount of time in seconds to hold a lease on a message "
-    "before dropping it from the lease management."
-)
-FlowControl.max_duration_per_lease_extension.__doc__ = (
-    "The max amount of time in seconds for a single lease extension attempt. "
-    "Bounds the delay before a message redelivery if the subscriber "
-    "fails to extend the deadline. Must be between 10 and 600 (inclusive). Ignored "
-    "if set to 0."
-)
+class FlowControl(NamedTuple):
+    """The settings for controlling the rate at which messages are pulled
+    with an asynchronous subscription.
+    """
+
+    max_bytes: int = 100 * 1024 * 1024  # 100 MiB
+    (
+        "The maximum total size of received - but not yet processed - messages "
+        "before pausing the message stream."
+    )
+
+    max_messages: int = 1000
+    (
+        "The maximum number of received - but not yet processed - messages before "
+        "pausing the message stream."
+    )
+
+    max_lease_duration: float = 1 * 60 * 60  # 1 hour
+    (
+        "The maximum amount of time in seconds to hold a lease on a message "
+        "before dropping it from the lease management."
+    )
+
+    max_duration_per_lease_extension: float = 0  # disabled by default
+    (
+        "The max amount of time in seconds for a single lease extension attempt. "
+        "Bounds the delay before a message redelivery if the subscriber "
+        "fails to extend the deadline. Must be between 10 and 600 (inclusive). Ignored "
+        "if set to 0."
+    )
 
 
 # The current api core helper does not find new proto messages of type proto.Message,
 # thus we need our own helper. Adjusted from
 # https://github.com/googleapis/python-api-core/blob/8595f620e7d8295b6a379d6fd7979af3bef717e2/google/api_core/protobuf_helpers.py#L101-L118
-def _get_protobuf_messages(module):
+def _get_protobuf_messages(module: "ModuleType") -> Dict[str, proto.Message]:
     """Discover all protobuf Message classes in a given import module.
 
     Args:
         module (module): A Python module; :func:`dir` will be run against this
             module to find Message subclasses.
 
     Returns:
```

### Comparing `google-cloud-pubsub-2.8.0/google/pubsub/__init__.py` & `google-cloud-pubsub-2.9.0/google/pubsub/__init__.py`

 * *Files identical despite different names*

### Comparing `google-cloud-pubsub-2.8.0/google/pubsub_v1/__init__.py` & `google-cloud-pubsub-2.9.0/google/pubsub_v1/__init__.py`

 * *Files identical despite different names*

### Comparing `google-cloud-pubsub-2.8.0/google/pubsub_v1/gapic_metadata.json` & `google-cloud-pubsub-2.9.0/google/pubsub_v1/gapic_metadata.json`

 * *Files identical despite different names*

### Comparing `google-cloud-pubsub-2.8.0/google/pubsub_v1/services/__init__.py` & `google-cloud-pubsub-2.9.0/google/pubsub_v1/services/__init__.py`

 * *Files identical despite different names*

### Comparing `google-cloud-pubsub-2.8.0/google/pubsub_v1/services/publisher/__init__.py` & `google-cloud-pubsub-2.9.0/google/pubsub_v1/services/publisher/__init__.py`

 * *Files identical despite different names*

### Comparing `google-cloud-pubsub-2.8.0/google/pubsub_v1/services/publisher/async_client.py` & `google-cloud-pubsub-2.9.0/google/pubsub_v1/services/publisher/async_client.py`

 * *Files 2% similar despite different names*

```diff
@@ -15,22 +15,27 @@
 #
 from collections import OrderedDict
 import functools
 import re
 from typing import Dict, Sequence, Tuple, Type, Union
 import pkg_resources
 
-import google.api_core.client_options as ClientOptions  # type: ignore
-from google.api_core import exceptions as core_exceptions  # type: ignore
-from google.api_core import gapic_v1  # type: ignore
-from google.api_core import retry as retries  # type: ignore
+from google.api_core.client_options import ClientOptions
+from google.api_core import exceptions as core_exceptions
+from google.api_core import gapic_v1
+from google.api_core import retry as retries
 from google.api_core import timeout as timeouts  # type: ignore
 from google.auth import credentials as ga_credentials  # type: ignore
 from google.oauth2 import service_account  # type: ignore
 
+try:
+    OptionalRetry = Union[retries.Retry, gapic_v1.method._MethodDefault]
+except AttributeError:  # pragma: NO COVER
+    OptionalRetry = Union[retries.Retry, object]  # type: ignore
+
 from google.iam.v1 import iam_policy_pb2  # type: ignore
 from google.iam.v1 import policy_pb2  # type: ignore
 from google.protobuf import duration_pb2  # type: ignore
 from google.pubsub_v1.services.publisher import pagers
 from google.pubsub_v1.types import pubsub
 from google.pubsub_v1.types import TimeoutType
 from .transports.base import PublisherTransport, DEFAULT_CLIENT_INFO
@@ -164,27 +169,27 @@
             transport=transport,
             client_options=client_options,
             client_info=client_info,
         )
 
     async def create_topic(
         self,
-        request: pubsub.Topic = None,
+        request: Union[pubsub.Topic, dict] = None,
         *,
         name: str = None,
-        retry: retries.Retry = gapic_v1.method.DEFAULT,
+        retry: OptionalRetry = gapic_v1.method.DEFAULT,
         timeout: TimeoutType = gapic_v1.method.DEFAULT,
         metadata: Sequence[Tuple[str, str]] = (),
     ) -> pubsub.Topic:
         r"""Creates the given topic with the given name. See the [resource
         name rules]
         (https://cloud.google.com/pubsub/docs/admin#resource_names).
 
         Args:
-            request (:class:`google.pubsub_v1.types.Topic`):
+            request (Union[google.pubsub_v1.types.Topic, dict]):
                 The request object. A topic resource.
             name (:class:`str`):
                 Required. The name of the topic. It must have the format
                 ``"projects/{project}/topics/{topic}"``. ``{topic}``
                 must start with a letter, and contain only letters
                 (``[A-Za-z]``), numbers (``[0-9]``), dashes (``-``),
                 underscores (``_``), periods (``.``), tildes (``~``),
@@ -250,25 +255,25 @@
         response = await rpc(request, retry=retry, timeout=timeout, metadata=metadata,)
 
         # Done; return the response.
         return response
 
     async def update_topic(
         self,
-        request: pubsub.UpdateTopicRequest = None,
+        request: Union[pubsub.UpdateTopicRequest, dict] = None,
         *,
-        retry: retries.Retry = gapic_v1.method.DEFAULT,
+        retry: OptionalRetry = gapic_v1.method.DEFAULT,
         timeout: TimeoutType = gapic_v1.method.DEFAULT,
         metadata: Sequence[Tuple[str, str]] = (),
     ) -> pubsub.Topic:
         r"""Updates an existing topic. Note that certain
         properties of a topic are not modifiable.
 
         Args:
-            request (:class:`google.pubsub_v1.types.UpdateTopicRequest`):
+            request (Union[google.pubsub_v1.types.UpdateTopicRequest, dict]):
                 The request object. Request for the UpdateTopic method.
             retry (google.api_core.retry.Retry): Designation of what errors, if any,
                 should be retried.
             timeout (TimeoutType):
                 The timeout for this request.
             metadata (Sequence[Tuple[str, str]]): Strings which should be
                 sent along with the request as metadata.
@@ -309,27 +314,27 @@
         response = await rpc(request, retry=retry, timeout=timeout, metadata=metadata,)
 
         # Done; return the response.
         return response
 
     async def publish(
         self,
-        request: pubsub.PublishRequest = None,
+        request: Union[pubsub.PublishRequest, dict] = None,
         *,
         topic: str = None,
         messages: Sequence[pubsub.PubsubMessage] = None,
-        retry: retries.Retry = gapic_v1.method.DEFAULT,
+        retry: OptionalRetry = gapic_v1.method.DEFAULT,
         timeout: TimeoutType = gapic_v1.method.DEFAULT,
         metadata: Sequence[Tuple[str, str]] = (),
     ) -> pubsub.PublishResponse:
         r"""Adds one or more messages to the topic. Returns ``NOT_FOUND`` if
         the topic does not exist.
 
         Args:
-            request (:class:`google.pubsub_v1.types.PublishRequest`):
+            request (Union[google.pubsub_v1.types.PublishRequest, dict]):
                 The request object. Request for the Publish method.
             topic (:class:`str`):
                 Required. The messages in the request will be published
                 on this topic. Format is
                 ``projects/{project}/topics/{topic}``.
 
                 This corresponds to the ``topic`` field
@@ -403,25 +408,25 @@
         response = await rpc(request, retry=retry, timeout=timeout, metadata=metadata,)
 
         # Done; return the response.
         return response
 
     async def get_topic(
         self,
-        request: pubsub.GetTopicRequest = None,
+        request: Union[pubsub.GetTopicRequest, dict] = None,
         *,
         topic: str = None,
-        retry: retries.Retry = gapic_v1.method.DEFAULT,
+        retry: OptionalRetry = gapic_v1.method.DEFAULT,
         timeout: TimeoutType = gapic_v1.method.DEFAULT,
         metadata: Sequence[Tuple[str, str]] = (),
     ) -> pubsub.Topic:
         r"""Gets the configuration of a topic.
 
         Args:
-            request (:class:`google.pubsub_v1.types.GetTopicRequest`):
+            request (Union[google.pubsub_v1.types.GetTopicRequest, dict]):
                 The request object. Request for the GetTopic method.
             topic (:class:`str`):
                 Required. The name of the topic to get. Format is
                 ``projects/{project}/topics/{topic}``.
 
                 This corresponds to the ``topic`` field
                 on the ``request`` instance; if ``request`` is provided, this
@@ -483,25 +488,25 @@
         response = await rpc(request, retry=retry, timeout=timeout, metadata=metadata,)
 
         # Done; return the response.
         return response
 
     async def list_topics(
         self,
-        request: pubsub.ListTopicsRequest = None,
+        request: Union[pubsub.ListTopicsRequest, dict] = None,
         *,
         project: str = None,
-        retry: retries.Retry = gapic_v1.method.DEFAULT,
+        retry: OptionalRetry = gapic_v1.method.DEFAULT,
         timeout: TimeoutType = gapic_v1.method.DEFAULT,
         metadata: Sequence[Tuple[str, str]] = (),
     ) -> pagers.ListTopicsAsyncPager:
         r"""Lists matching topics.
 
         Args:
-            request (:class:`google.pubsub_v1.types.ListTopicsRequest`):
+            request (Union[google.pubsub_v1.types.ListTopicsRequest, dict]):
                 The request object. Request for the `ListTopics` method.
             project (:class:`str`):
                 Required. The name of the project in which to list
                 topics. Format is ``projects/{project-id}``.
 
                 This corresponds to the ``project`` field
                 on the ``request`` instance; if ``request`` is provided, this
@@ -573,26 +578,26 @@
         )
 
         # Done; return the response.
         return response
 
     async def list_topic_subscriptions(
         self,
-        request: pubsub.ListTopicSubscriptionsRequest = None,
+        request: Union[pubsub.ListTopicSubscriptionsRequest, dict] = None,
         *,
         topic: str = None,
-        retry: retries.Retry = gapic_v1.method.DEFAULT,
+        retry: OptionalRetry = gapic_v1.method.DEFAULT,
         timeout: TimeoutType = gapic_v1.method.DEFAULT,
         metadata: Sequence[Tuple[str, str]] = (),
     ) -> pagers.ListTopicSubscriptionsAsyncPager:
         r"""Lists the names of the attached subscriptions on this
         topic.
 
         Args:
-            request (:class:`google.pubsub_v1.types.ListTopicSubscriptionsRequest`):
+            request (Union[google.pubsub_v1.types.ListTopicSubscriptionsRequest, dict]):
                 The request object. Request for the
                 `ListTopicSubscriptions` method.
             topic (:class:`str`):
                 Required. The name of the topic that subscriptions are
                 attached to. Format is
                 ``projects/{project}/topics/{topic}``.
 
@@ -666,30 +671,30 @@
         )
 
         # Done; return the response.
         return response
 
     async def list_topic_snapshots(
         self,
-        request: pubsub.ListTopicSnapshotsRequest = None,
+        request: Union[pubsub.ListTopicSnapshotsRequest, dict] = None,
         *,
         topic: str = None,
-        retry: retries.Retry = gapic_v1.method.DEFAULT,
+        retry: OptionalRetry = gapic_v1.method.DEFAULT,
         timeout: TimeoutType = gapic_v1.method.DEFAULT,
         metadata: Sequence[Tuple[str, str]] = (),
     ) -> pagers.ListTopicSnapshotsAsyncPager:
         r"""Lists the names of the snapshots on this topic. Snapshots are
         used in
         `Seek <https://cloud.google.com/pubsub/docs/replay-overview>`__
         operations, which allow you to manage message acknowledgments in
         bulk. That is, you can set the acknowledgment state of messages
         in an existing subscription to the state captured by a snapshot.
 
         Args:
-            request (:class:`google.pubsub_v1.types.ListTopicSnapshotsRequest`):
+            request (Union[google.pubsub_v1.types.ListTopicSnapshotsRequest, dict]):
                 The request object. Request for the `ListTopicSnapshots`
                 method.
             topic (:class:`str`):
                 Required. The name of the topic that snapshots are
                 attached to. Format is
                 ``projects/{project}/topics/{topic}``.
 
@@ -763,30 +768,30 @@
         )
 
         # Done; return the response.
         return response
 
     async def delete_topic(
         self,
-        request: pubsub.DeleteTopicRequest = None,
+        request: Union[pubsub.DeleteTopicRequest, dict] = None,
         *,
         topic: str = None,
-        retry: retries.Retry = gapic_v1.method.DEFAULT,
+        retry: OptionalRetry = gapic_v1.method.DEFAULT,
         timeout: TimeoutType = gapic_v1.method.DEFAULT,
         metadata: Sequence[Tuple[str, str]] = (),
     ) -> None:
         r"""Deletes the topic with the given name. Returns ``NOT_FOUND`` if
         the topic does not exist. After a topic is deleted, a new topic
         may be created with the same name; this is an entirely new topic
         with none of the old configuration or subscriptions. Existing
         subscriptions to this topic are not deleted, but their ``topic``
         field is set to ``_deleted-topic_``.
 
         Args:
-            request (:class:`google.pubsub_v1.types.DeleteTopicRequest`):
+            request (Union[google.pubsub_v1.types.DeleteTopicRequest, dict]):
                 The request object. Request for the `DeleteTopic`
                 method.
             topic (:class:`str`):
                 Required. Name of the topic to delete. Format is
                 ``projects/{project}/topics/{topic}``.
 
                 This corresponds to the ``topic`` field
@@ -842,28 +847,28 @@
         # Send the request.
         await rpc(
             request, retry=retry, timeout=timeout, metadata=metadata,
         )
 
     async def detach_subscription(
         self,
-        request: pubsub.DetachSubscriptionRequest = None,
+        request: Union[pubsub.DetachSubscriptionRequest, dict] = None,
         *,
-        retry: retries.Retry = gapic_v1.method.DEFAULT,
+        retry: OptionalRetry = gapic_v1.method.DEFAULT,
         timeout: TimeoutType = gapic_v1.method.DEFAULT,
         metadata: Sequence[Tuple[str, str]] = (),
     ) -> pubsub.DetachSubscriptionResponse:
         r"""Detaches a subscription from this topic. All messages retained
         in the subscription are dropped. Subsequent ``Pull`` and
         ``StreamingPull`` requests will return FAILED_PRECONDITION. If
         the subscription is a push subscription, pushes to the endpoint
         will stop.
 
         Args:
-            request (:class:`google.pubsub_v1.types.DetachSubscriptionRequest`):
+            request (Union[google.pubsub_v1.types.DetachSubscriptionRequest, dict]):
                 The request object. Request for the DetachSubscription
                 method.
             retry (google.api_core.retry.Retry): Designation of what errors, if any,
                 should be retried.
             timeout (TimeoutType):
                 The timeout for this request.
             metadata (Sequence[Tuple[str, str]]): Strings which should be
@@ -909,15 +914,15 @@
         # Done; return the response.
         return response
 
     async def set_iam_policy(
         self,
         request: iam_policy_pb2.SetIamPolicyRequest = None,
         *,
-        retry: retries.Retry = gapic_v1.method.DEFAULT,
+        retry: OptionalRetry = gapic_v1.method.DEFAULT,
         timeout: TimeoutType = gapic_v1.method.DEFAULT,
         metadata: Sequence[Tuple[str, str]] = (),
     ) -> policy_pb2.Policy:
         r"""Sets the IAM access control policy on the specified function.
 
         Replaces any existing policy.
 
@@ -1018,15 +1023,15 @@
         # Done; return the response.
         return response
 
     async def get_iam_policy(
         self,
         request: iam_policy_pb2.GetIamPolicyRequest = None,
         *,
-        retry: retries.Retry = gapic_v1.method.DEFAULT,
+        retry: OptionalRetry = gapic_v1.method.DEFAULT,
         timeout: TimeoutType = gapic_v1.method.DEFAULT,
         metadata: Sequence[Tuple[str, str]] = (),
     ) -> policy_pb2.Policy:
         r"""Gets the IAM access control policy for a function.
 
         Returns an empty policy if the function exists and does
         not have a policy set.
@@ -1128,15 +1133,15 @@
         # Done; return the response.
         return response
 
     async def test_iam_permissions(
         self,
         request: iam_policy_pb2.TestIamPermissionsRequest = None,
         *,
-        retry: retries.Retry = gapic_v1.method.DEFAULT,
+        retry: OptionalRetry = gapic_v1.method.DEFAULT,
         timeout: TimeoutType = gapic_v1.method.DEFAULT,
         metadata: Sequence[Tuple[str, str]] = (),
     ) -> iam_policy_pb2.TestIamPermissionsResponse:
         r"""Tests the specified permissions against the IAM access control
             policy for a function.
 
         If the function does not exist, this will
@@ -1179,14 +1184,20 @@
 
         # Send the request.
         response = await rpc(request, retry=retry, timeout=timeout, metadata=metadata,)
 
         # Done; return the response.
         return response
 
+    async def __aenter__(self):
+        return self
+
+    async def __aexit__(self, exc_type, exc, tb):
+        await self.transport.close()
+
 
 try:
     DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
         client_library_version=pkg_resources.get_distribution(
             "google-cloud-pubsub",
         ).version,
     )
```

### Comparing `google-cloud-pubsub-2.8.0/google/pubsub_v1/services/publisher/client.py` & `google-cloud-pubsub-2.9.0/google/pubsub_v1/services/publisher/client.py`

 * *Files 4% similar despite different names*

```diff
@@ -10,32 +10,36 @@
 # Unless required by applicable law or agreed to in writing, software
 # distributed under the License is distributed on an "AS IS" BASIS,
 # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 # See the License for the specific language governing permissions and
 # limitations under the License.
 #
 from collections import OrderedDict
-from distutils import util
 import functools
 import os
 import re
-from typing import Callable, Dict, Optional, Sequence, Tuple, Type, Union
+from typing import Dict, Optional, Sequence, Tuple, Type, Union
 import pkg_resources
 
-from google.api_core import client_options as client_options_lib  # type: ignore
-from google.api_core import exceptions as core_exceptions  # type: ignore
-from google.api_core import gapic_v1  # type: ignore
-from google.api_core import retry as retries  # type: ignore
+from google.api_core import client_options as client_options_lib
+from google.api_core import exceptions as core_exceptions
+from google.api_core import gapic_v1
+from google.api_core import retry as retries
 from google.api_core import timeout as timeouts  # type: ignore
 from google.auth import credentials as ga_credentials  # type: ignore
 from google.auth.transport import mtls  # type: ignore
 from google.auth.transport.grpc import SslCredentials  # type: ignore
 from google.auth.exceptions import MutualTLSChannelError  # type: ignore
 from google.oauth2 import service_account  # type: ignore
 
+try:
+    OptionalRetry = Union[retries.Retry, gapic_v1.method._MethodDefault]
+except AttributeError:  # pragma: NO COVER
+    OptionalRetry = Union[retries.Retry, object]  # type: ignore
+
 from google.iam.v1 import iam_policy_pb2  # type: ignore
 from google.iam.v1 import policy_pb2  # type: ignore
 from google.protobuf import duration_pb2  # type: ignore
 from google.pubsub_v1.services.publisher import pagers
 from google.pubsub_v1.types import pubsub
 from google.pubsub_v1.types import TimeoutType
 
@@ -323,16 +327,23 @@
         """
         if isinstance(client_options, dict):
             client_options = client_options_lib.from_dict(client_options)
         if client_options is None:
             client_options = client_options_lib.ClientOptions()
 
         # Create SSL credentials for mutual TLS if needed.
-        use_client_cert = bool(
-            util.strtobool(os.getenv("GOOGLE_API_USE_CLIENT_CERTIFICATE", "false"))
+        if os.getenv("GOOGLE_API_USE_CLIENT_CERTIFICATE", "false") not in (
+            "true",
+            "false",
+        ):
+            raise ValueError(
+                "Environment variable `GOOGLE_API_USE_CLIENT_CERTIFICATE` must be either `true` or `false`"
+            )
+        use_client_cert = (
+            os.getenv("GOOGLE_API_USE_CLIENT_CERTIFICATE", "false") == "true"
         )
 
         client_cert_source_func = None
         is_mtls = False
         if use_client_cert:
             if client_options.client_cert_source:
                 is_mtls = True
@@ -395,36 +406,33 @@
                 credentials=credentials,
                 credentials_file=client_options.credentials_file,
                 host=api_endpoint,
                 scopes=client_options.scopes,
                 client_cert_source_for_mtls=client_cert_source_func,
                 quota_project_id=client_options.quota_project_id,
                 client_info=client_info,
-                always_use_jwt_access=(
-                    Transport == type(self).get_transport_class("grpc")
-                    or Transport == type(self).get_transport_class("grpc_asyncio")
-                ),
+                always_use_jwt_access=True,
             )
 
     def create_topic(
         self,
-        request: pubsub.Topic = None,
+        request: Union[pubsub.Topic, dict] = None,
         *,
         name: str = None,
-        retry: retries.Retry = gapic_v1.method.DEFAULT,
+        retry: OptionalRetry = gapic_v1.method.DEFAULT,
         timeout: TimeoutType = gapic_v1.method.DEFAULT,
         metadata: Sequence[Tuple[str, str]] = (),
     ) -> pubsub.Topic:
         r"""Creates the given topic with the given name. See the [resource
         name rules]
         (https://cloud.google.com/pubsub/docs/admin#resource_names).
 
 
         Args:
-            request (google.pubsub_v1.types.Topic):
+            request (Union[google.pubsub_v1.types.Topic, dict]):
                 The request object. A topic resource.
             name (str):
                 Required. The name of the topic. It must have the format
                 ``"projects/{project}/topics/{topic}"``. ``{topic}``
                 must start with a letter, and contain only letters
                 (``[A-Za-z]``), numbers (``[0-9]``), dashes (``-``),
                 underscores (``_``), periods (``.``), tildes (``~``),
@@ -481,26 +489,26 @@
         response = rpc(request, retry=retry, timeout=timeout, metadata=metadata,)
 
         # Done; return the response.
         return response
 
     def update_topic(
         self,
-        request: pubsub.UpdateTopicRequest = None,
+        request: Union[pubsub.UpdateTopicRequest, dict] = None,
         *,
-        retry: retries.Retry = gapic_v1.method.DEFAULT,
+        retry: OptionalRetry = gapic_v1.method.DEFAULT,
         timeout: TimeoutType = gapic_v1.method.DEFAULT,
         metadata: Sequence[Tuple[str, str]] = (),
     ) -> pubsub.Topic:
         r"""Updates an existing topic. Note that certain
         properties of a topic are not modifiable.
 
 
         Args:
-            request (google.pubsub_v1.types.UpdateTopicRequest):
+            request (Union[google.pubsub_v1.types.UpdateTopicRequest, dict]):
                 The request object. Request for the UpdateTopic method.
             retry (google.api_core.retry.Retry): Designation of what errors, if any,
                 should be retried.
             timeout (TimeoutType):
                 The timeout for this request.
             metadata (Sequence[Tuple[str, str]]): Strings which should be
                 sent along with the request as metadata.
@@ -533,28 +541,28 @@
         response = rpc(request, retry=retry, timeout=timeout, metadata=metadata,)
 
         # Done; return the response.
         return response
 
     def publish(
         self,
-        request: pubsub.PublishRequest = None,
+        request: Union[pubsub.PublishRequest, dict] = None,
         *,
         topic: str = None,
         messages: Sequence[pubsub.PubsubMessage] = None,
-        retry: retries.Retry = gapic_v1.method.DEFAULT,
+        retry: OptionalRetry = gapic_v1.method.DEFAULT,
         timeout: TimeoutType = gapic_v1.method.DEFAULT,
         metadata: Sequence[Tuple[str, str]] = (),
     ) -> pubsub.PublishResponse:
         r"""Adds one or more messages to the topic. Returns ``NOT_FOUND`` if
         the topic does not exist.
 
 
         Args:
-            request (google.pubsub_v1.types.PublishRequest):
+            request (Union[google.pubsub_v1.types.PublishRequest, dict]):
                 The request object. Request for the Publish method.
             topic (str):
                 Required. The messages in the request will be published
                 on this topic. Format is
                 ``projects/{project}/topics/{topic}``.
 
                 This corresponds to the ``topic`` field
@@ -613,26 +621,26 @@
         response = rpc(request, retry=retry, timeout=timeout, metadata=metadata,)
 
         # Done; return the response.
         return response
 
     def get_topic(
         self,
-        request: pubsub.GetTopicRequest = None,
+        request: Union[pubsub.GetTopicRequest, dict] = None,
         *,
         topic: str = None,
-        retry: retries.Retry = gapic_v1.method.DEFAULT,
+        retry: OptionalRetry = gapic_v1.method.DEFAULT,
         timeout: TimeoutType = gapic_v1.method.DEFAULT,
         metadata: Sequence[Tuple[str, str]] = (),
     ) -> pubsub.Topic:
         r"""Gets the configuration of a topic.
 
 
         Args:
-            request (google.pubsub_v1.types.GetTopicRequest):
+            request (Union[google.pubsub_v1.types.GetTopicRequest, dict]):
                 The request object. Request for the GetTopic method.
             topic (str):
                 Required. The name of the topic to get. Format is
                 ``projects/{project}/topics/{topic}``.
 
                 This corresponds to the ``topic`` field
                 on the ``request`` instance; if ``request`` is provided, this
@@ -683,26 +691,26 @@
         response = rpc(request, retry=retry, timeout=timeout, metadata=metadata,)
 
         # Done; return the response.
         return response
 
     def list_topics(
         self,
-        request: pubsub.ListTopicsRequest = None,
+        request: Union[pubsub.ListTopicsRequest, dict] = None,
         *,
         project: str = None,
-        retry: retries.Retry = gapic_v1.method.DEFAULT,
+        retry: OptionalRetry = gapic_v1.method.DEFAULT,
         timeout: TimeoutType = gapic_v1.method.DEFAULT,
         metadata: Sequence[Tuple[str, str]] = (),
     ) -> pagers.ListTopicsPager:
         r"""Lists matching topics.
 
 
         Args:
-            request (google.pubsub_v1.types.ListTopicsRequest):
+            request (Union[google.pubsub_v1.types.ListTopicsRequest, dict]):
                 The request object. Request for the `ListTopics` method.
             project (str):
                 Required. The name of the project in which to list
                 topics. Format is ``projects/{project-id}``.
 
                 This corresponds to the ``project`` field
                 on the ``request`` instance; if ``request`` is provided, this
@@ -763,27 +771,27 @@
         )
 
         # Done; return the response.
         return response
 
     def list_topic_subscriptions(
         self,
-        request: pubsub.ListTopicSubscriptionsRequest = None,
+        request: Union[pubsub.ListTopicSubscriptionsRequest, dict] = None,
         *,
         topic: str = None,
-        retry: retries.Retry = gapic_v1.method.DEFAULT,
+        retry: OptionalRetry = gapic_v1.method.DEFAULT,
         timeout: TimeoutType = gapic_v1.method.DEFAULT,
         metadata: Sequence[Tuple[str, str]] = (),
     ) -> pagers.ListTopicSubscriptionsPager:
         r"""Lists the names of the attached subscriptions on this
         topic.
 
 
         Args:
-            request (google.pubsub_v1.types.ListTopicSubscriptionsRequest):
+            request (Union[google.pubsub_v1.types.ListTopicSubscriptionsRequest, dict]):
                 The request object. Request for the
                 `ListTopicSubscriptions` method.
             topic (str):
                 Required. The name of the topic that subscriptions are
                 attached to. Format is
                 ``projects/{project}/topics/{topic}``.
 
@@ -846,31 +854,31 @@
         )
 
         # Done; return the response.
         return response
 
     def list_topic_snapshots(
         self,
-        request: pubsub.ListTopicSnapshotsRequest = None,
+        request: Union[pubsub.ListTopicSnapshotsRequest, dict] = None,
         *,
         topic: str = None,
-        retry: retries.Retry = gapic_v1.method.DEFAULT,
+        retry: OptionalRetry = gapic_v1.method.DEFAULT,
         timeout: TimeoutType = gapic_v1.method.DEFAULT,
         metadata: Sequence[Tuple[str, str]] = (),
     ) -> pagers.ListTopicSnapshotsPager:
         r"""Lists the names of the snapshots on this topic. Snapshots are
         used in
         `Seek <https://cloud.google.com/pubsub/docs/replay-overview>`__
         operations, which allow you to manage message acknowledgments in
         bulk. That is, you can set the acknowledgment state of messages
         in an existing subscription to the state captured by a snapshot.
 
 
         Args:
-            request (google.pubsub_v1.types.ListTopicSnapshotsRequest):
+            request (Union[google.pubsub_v1.types.ListTopicSnapshotsRequest, dict]):
                 The request object. Request for the `ListTopicSnapshots`
                 method.
             topic (str):
                 Required. The name of the topic that snapshots are
                 attached to. Format is
                 ``projects/{project}/topics/{topic}``.
 
@@ -933,31 +941,31 @@
         )
 
         # Done; return the response.
         return response
 
     def delete_topic(
         self,
-        request: pubsub.DeleteTopicRequest = None,
+        request: Union[pubsub.DeleteTopicRequest, dict] = None,
         *,
         topic: str = None,
-        retry: retries.Retry = gapic_v1.method.DEFAULT,
+        retry: OptionalRetry = gapic_v1.method.DEFAULT,
         timeout: TimeoutType = gapic_v1.method.DEFAULT,
         metadata: Sequence[Tuple[str, str]] = (),
     ) -> None:
         r"""Deletes the topic with the given name. Returns ``NOT_FOUND`` if
         the topic does not exist. After a topic is deleted, a new topic
         may be created with the same name; this is an entirely new topic
         with none of the old configuration or subscriptions. Existing
         subscriptions to this topic are not deleted, but their ``topic``
         field is set to ``_deleted-topic_``.
 
 
         Args:
-            request (google.pubsub_v1.types.DeleteTopicRequest):
+            request (Union[google.pubsub_v1.types.DeleteTopicRequest, dict]):
                 The request object. Request for the `DeleteTopic`
                 method.
             topic (str):
                 Required. Name of the topic to delete. Format is
                 ``projects/{project}/topics/{topic}``.
 
                 This corresponds to the ``topic`` field
@@ -1004,29 +1012,29 @@
         # Send the request.
         rpc(
             request, retry=retry, timeout=timeout, metadata=metadata,
         )
 
     def detach_subscription(
         self,
-        request: pubsub.DetachSubscriptionRequest = None,
+        request: Union[pubsub.DetachSubscriptionRequest, dict] = None,
         *,
-        retry: retries.Retry = gapic_v1.method.DEFAULT,
+        retry: OptionalRetry = gapic_v1.method.DEFAULT,
         timeout: TimeoutType = gapic_v1.method.DEFAULT,
         metadata: Sequence[Tuple[str, str]] = (),
     ) -> pubsub.DetachSubscriptionResponse:
         r"""Detaches a subscription from this topic. All messages retained
         in the subscription are dropped. Subsequent ``Pull`` and
         ``StreamingPull`` requests will return FAILED_PRECONDITION. If
         the subscription is a push subscription, pushes to the endpoint
         will stop.
 
 
         Args:
-            request (google.pubsub_v1.types.DetachSubscriptionRequest):
+            request (Union[google.pubsub_v1.types.DetachSubscriptionRequest, dict]):
                 The request object. Request for the DetachSubscription
                 method.
             retry (google.api_core.retry.Retry): Designation of what errors, if any,
                 should be retried.
             timeout (TimeoutType):
                 The timeout for this request.
             metadata (Sequence[Tuple[str, str]]): Strings which should be
@@ -1060,19 +1068,32 @@
 
         # Send the request.
         response = rpc(request, retry=retry, timeout=timeout, metadata=metadata,)
 
         # Done; return the response.
         return response
 
+    def __enter__(self):
+        return self
+
+    def __exit__(self, type, value, traceback):
+        """Releases underlying transport's resources.
+
+        .. warning::
+            ONLY use as a context manager if the transport is NOT shared
+            with other clients! Exiting the with block will CLOSE the transport
+            and may cause errors in other clients!
+        """
+        self.transport.close()
+
     def set_iam_policy(
         self,
         request: iam_policy_pb2.SetIamPolicyRequest = None,
         *,
-        retry: retries.Retry = gapic_v1.method.DEFAULT,
+        retry: OptionalRetry = gapic_v1.method.DEFAULT,
         timeout: TimeoutType = gapic_v1.method.DEFAULT,
         metadata: Sequence[Tuple[str, str]] = (),
     ) -> policy_pb2.Policy:
         r"""Sets the IAM access control policy on the specified function.
 
         Replaces any existing policy.
 
@@ -1177,15 +1198,15 @@
         # Done; return the response.
         return response
 
     def get_iam_policy(
         self,
         request: iam_policy_pb2.GetIamPolicyRequest = None,
         *,
-        retry: retries.Retry = gapic_v1.method.DEFAULT,
+        retry: OptionalRetry = gapic_v1.method.DEFAULT,
         timeout: TimeoutType = gapic_v1.method.DEFAULT,
         metadata: Sequence[Tuple[str, str]] = (),
     ) -> policy_pb2.Policy:
         r"""Gets the IAM access control policy for a function.
 
         Returns an empty policy if the function exists and does not have a
         policy set.
@@ -1291,15 +1312,15 @@
         # Done; return the response.
         return response
 
     def test_iam_permissions(
         self,
         request: iam_policy_pb2.TestIamPermissionsRequest = None,
         *,
-        retry: retries.Retry = gapic_v1.method.DEFAULT,
+        retry: OptionalRetry = gapic_v1.method.DEFAULT,
         timeout: TimeoutType = gapic_v1.method.DEFAULT,
         metadata: Sequence[Tuple[str, str]] = (),
     ) -> iam_policy_pb2.TestIamPermissionsResponse:
         r"""Tests the specified IAM permissions against the IAM access control
             policy for a function.
 
         If the function does not exist, this will return an empty set
```

### Comparing `google-cloud-pubsub-2.8.0/google/pubsub_v1/services/publisher/pagers.py` & `google-cloud-pubsub-2.9.0/google/pubsub_v1/services/publisher/pagers.py`

 * *Files 8% similar despite different names*

```diff
@@ -11,21 +11,21 @@
 # distributed under the License is distributed on an "AS IS" BASIS,
 # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 # See the License for the specific language governing permissions and
 # limitations under the License.
 #
 from typing import (
     Any,
-    AsyncIterable,
+    AsyncIterator,
     Awaitable,
     Callable,
-    Iterable,
     Sequence,
     Tuple,
     Optional,
+    Iterator,
 )
 
 from google.pubsub_v1.types import pubsub
 
 
 class ListTopicsPager:
     """A pager for iterating through ``list_topics`` requests.
@@ -70,22 +70,22 @@
         self._response = response
         self._metadata = metadata
 
     def __getattr__(self, name: str) -> Any:
         return getattr(self._response, name)
 
     @property
-    def pages(self) -> Iterable[pubsub.ListTopicsResponse]:
+    def pages(self) -> Iterator[pubsub.ListTopicsResponse]:
         yield self._response
         while self._response.next_page_token:
             self._request.page_token = self._response.next_page_token
             self._response = self._method(self._request, metadata=self._metadata)
             yield self._response
 
-    def __iter__(self) -> Iterable[pubsub.Topic]:
+    def __iter__(self) -> Iterator[pubsub.Topic]:
         for page in self.pages:
             yield from page.topics
 
     def __repr__(self) -> str:
         return "{0}<{1!r}>".format(self.__class__.__name__, self._response)
 
 
@@ -132,22 +132,22 @@
         self._response = response
         self._metadata = metadata
 
     def __getattr__(self, name: str) -> Any:
         return getattr(self._response, name)
 
     @property
-    async def pages(self) -> AsyncIterable[pubsub.ListTopicsResponse]:
+    async def pages(self) -> AsyncIterator[pubsub.ListTopicsResponse]:
         yield self._response
         while self._response.next_page_token:
             self._request.page_token = self._response.next_page_token
             self._response = await self._method(self._request, metadata=self._metadata)
             yield self._response
 
-    def __aiter__(self) -> AsyncIterable[pubsub.Topic]:
+    def __aiter__(self) -> AsyncIterator[pubsub.Topic]:
         async def async_generator():
             async for page in self.pages:
                 for response in page.topics:
                     yield response
 
         return async_generator()
 
@@ -198,22 +198,22 @@
         self._response = response
         self._metadata = metadata
 
     def __getattr__(self, name: str) -> Any:
         return getattr(self._response, name)
 
     @property
-    def pages(self) -> Iterable[pubsub.ListTopicSubscriptionsResponse]:
+    def pages(self) -> Iterator[pubsub.ListTopicSubscriptionsResponse]:
         yield self._response
         while self._response.next_page_token:
             self._request.page_token = self._response.next_page_token
             self._response = self._method(self._request, metadata=self._metadata)
             yield self._response
 
-    def __iter__(self) -> Iterable[str]:
+    def __iter__(self) -> Iterator[str]:
         for page in self.pages:
             yield from page.subscriptions
 
     def __repr__(self) -> str:
         return "{0}<{1!r}>".format(self.__class__.__name__, self._response)
 
 
@@ -260,22 +260,22 @@
         self._response = response
         self._metadata = metadata
 
     def __getattr__(self, name: str) -> Any:
         return getattr(self._response, name)
 
     @property
-    async def pages(self) -> AsyncIterable[pubsub.ListTopicSubscriptionsResponse]:
+    async def pages(self) -> AsyncIterator[pubsub.ListTopicSubscriptionsResponse]:
         yield self._response
         while self._response.next_page_token:
             self._request.page_token = self._response.next_page_token
             self._response = await self._method(self._request, metadata=self._metadata)
             yield self._response
 
-    def __aiter__(self) -> AsyncIterable[str]:
+    def __aiter__(self) -> AsyncIterator[str]:
         async def async_generator():
             async for page in self.pages:
                 for response in page.subscriptions:
                     yield response
 
         return async_generator()
 
@@ -326,22 +326,22 @@
         self._response = response
         self._metadata = metadata
 
     def __getattr__(self, name: str) -> Any:
         return getattr(self._response, name)
 
     @property
-    def pages(self) -> Iterable[pubsub.ListTopicSnapshotsResponse]:
+    def pages(self) -> Iterator[pubsub.ListTopicSnapshotsResponse]:
         yield self._response
         while self._response.next_page_token:
             self._request.page_token = self._response.next_page_token
             self._response = self._method(self._request, metadata=self._metadata)
             yield self._response
 
-    def __iter__(self) -> Iterable[str]:
+    def __iter__(self) -> Iterator[str]:
         for page in self.pages:
             yield from page.snapshots
 
     def __repr__(self) -> str:
         return "{0}<{1!r}>".format(self.__class__.__name__, self._response)
 
 
@@ -388,22 +388,22 @@
         self._response = response
         self._metadata = metadata
 
     def __getattr__(self, name: str) -> Any:
         return getattr(self._response, name)
 
     @property
-    async def pages(self) -> AsyncIterable[pubsub.ListTopicSnapshotsResponse]:
+    async def pages(self) -> AsyncIterator[pubsub.ListTopicSnapshotsResponse]:
         yield self._response
         while self._response.next_page_token:
             self._request.page_token = self._response.next_page_token
             self._response = await self._method(self._request, metadata=self._metadata)
             yield self._response
 
-    def __aiter__(self) -> AsyncIterable[str]:
+    def __aiter__(self) -> AsyncIterator[str]:
         async def async_generator():
             async for page in self.pages:
                 for response in page.snapshots:
                     yield response
 
         return async_generator()
```

### Comparing `google-cloud-pubsub-2.8.0/google/pubsub_v1/services/publisher/transports/__init__.py` & `google-cloud-pubsub-2.9.0/google/pubsub_v1/services/publisher/transports/__init__.py`

 * *Files identical despite different names*

### Comparing `google-cloud-pubsub-2.8.0/google/pubsub_v1/services/publisher/transports/base.py` & `google-cloud-pubsub-2.9.0/google/pubsub_v1/services/publisher/transports/base.py`

 * *Files 5% similar despite different names*

```diff
@@ -11,22 +11,21 @@
 # distributed under the License is distributed on an "AS IS" BASIS,
 # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 # See the License for the specific language governing permissions and
 # limitations under the License.
 #
 import abc
 from typing import Awaitable, Callable, Dict, Optional, Sequence, Union
-import packaging.version
 import pkg_resources
 
 import google.auth  # type: ignore
-import google.api_core  # type: ignore
-from google.api_core import exceptions as core_exceptions  # type: ignore
-from google.api_core import gapic_v1  # type: ignore
-from google.api_core import retry as retries  # type: ignore
+import google.api_core
+from google.api_core import exceptions as core_exceptions
+from google.api_core import gapic_v1
+from google.api_core import retry as retries
 from google.auth import credentials as ga_credentials  # type: ignore
 from google.oauth2 import service_account  # type: ignore
 
 from google.iam.v1 import iam_policy_pb2  # type: ignore
 from google.iam.v1 import policy_pb2  # type: ignore
 from google.protobuf import empty_pb2  # type: ignore
 from google.pubsub_v1.types import pubsub
@@ -36,23 +35,14 @@
         client_library_version=pkg_resources.get_distribution(
             "google-cloud-pubsub",
         ).version,
     )
 except pkg_resources.DistributionNotFound:
     DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo()
 
-try:
-    # google.auth.__version__ was added in 1.26.0
-    _GOOGLE_AUTH_VERSION = google.auth.__version__
-except AttributeError:
-    try:  # try pkg_resources if it is available
-        _GOOGLE_AUTH_VERSION = pkg_resources.get_distribution("google-auth").version
-    except pkg_resources.DistributionNotFound:  # pragma: NO COVER
-        _GOOGLE_AUTH_VERSION = None
-
 
 class PublisherTransport(abc.ABC):
     """Abstract transport class for Publisher."""
 
     AUTH_SCOPES = (
         "https://www.googleapis.com/auth/cloud-platform",
         "https://www.googleapis.com/auth/pubsub",
@@ -97,15 +87,15 @@
                 be used for service account credentials.
         """
         # Save the hostname. Default to port 443 (HTTPS) if none is specified.
         if ":" not in host:
             host += ":443"
         self._host = host
 
-        scopes_kwargs = self._get_scopes_kwargs(self._host, scopes)
+        scopes_kwargs = {"scopes": scopes, "default_scopes": self.AUTH_SCOPES}
 
         # Save the scopes.
         self._scopes = scopes
 
         # If no credentials are provided, then determine the appropriate
         # defaults.
         if credentials and credentials_file:
@@ -119,75 +109,52 @@
             )
 
         elif credentials is None:
             credentials, _ = google.auth.default(
                 **scopes_kwargs, quota_project_id=quota_project_id
             )
 
-        # If the credentials is service account credentials, then always try to use self signed JWT.
+        # If the credentials are service account credentials, then always try to use self signed JWT.
         if (
             always_use_jwt_access
             and isinstance(credentials, service_account.Credentials)
             and hasattr(service_account.Credentials, "with_always_use_jwt_access")
         ):
             credentials = credentials.with_always_use_jwt_access(True)
 
         # Save the credentials.
         self._credentials = credentials
 
-    # TODO(busunkim): This method is in the base transport
-    # to avoid duplicating code across the transport classes. These functions
-    # should be deleted once the minimum required versions of google-auth is increased.
-
-    # TODO: Remove this function once google-auth >= 1.25.0 is required
-    @classmethod
-    def _get_scopes_kwargs(
-        cls, host: str, scopes: Optional[Sequence[str]]
-    ) -> Dict[str, Optional[Sequence[str]]]:
-        """Returns scopes kwargs to pass to google-auth methods depending on the google-auth version"""
-
-        scopes_kwargs = {}
-
-        if _GOOGLE_AUTH_VERSION and (
-            packaging.version.parse(_GOOGLE_AUTH_VERSION)
-            >= packaging.version.parse("1.25.0")
-        ):
-            scopes_kwargs = {"scopes": scopes, "default_scopes": cls.AUTH_SCOPES}
-        else:
-            scopes_kwargs = {"scopes": scopes or cls.AUTH_SCOPES}
-
-        return scopes_kwargs
-
     def _prep_wrapped_messages(self, client_info):
         # Precompute the wrapped methods.
         self._wrapped_methods = {
             self.create_topic: gapic_v1.method.wrap_method(
                 self.create_topic,
                 default_retry=retries.Retry(
                     initial=0.1,
                     maximum=60.0,
                     multiplier=1.3,
                     predicate=retries.if_exception_type(
                         core_exceptions.ServiceUnavailable,
                     ),
-                    deadline=60.0,
+                    deadline=600.0,
                 ),
                 default_timeout=60.0,
                 client_info=client_info,
             ),
             self.update_topic: gapic_v1.method.wrap_method(
                 self.update_topic,
                 default_retry=retries.Retry(
                     initial=0.1,
                     maximum=60.0,
                     multiplier=1.3,
                     predicate=retries.if_exception_type(
                         core_exceptions.ServiceUnavailable,
                     ),
-                    deadline=60.0,
+                    deadline=600.0,
                 ),
                 default_timeout=60.0,
                 client_info=client_info,
             ),
             self.publish: gapic_v1.method.wrap_method(
                 self.publish,
                 default_retry=retries.Retry(
@@ -199,15 +166,15 @@
                         core_exceptions.Cancelled,
                         core_exceptions.DeadlineExceeded,
                         core_exceptions.InternalServerError,
                         core_exceptions.ResourceExhausted,
                         core_exceptions.ServiceUnavailable,
                         core_exceptions.Unknown,
                     ),
-                    deadline=60.0,
+                    deadline=600.0,
                 ),
                 default_timeout=60.0,
                 client_info=client_info,
             ),
             self.get_topic: gapic_v1.method.wrap_method(
                 self.get_topic,
                 default_retry=retries.Retry(
@@ -215,15 +182,15 @@
                     maximum=60.0,
                     multiplier=1.3,
                     predicate=retries.if_exception_type(
                         core_exceptions.Aborted,
                         core_exceptions.ServiceUnavailable,
                         core_exceptions.Unknown,
                     ),
-                    deadline=60.0,
+                    deadline=600.0,
                 ),
                 default_timeout=60.0,
                 client_info=client_info,
             ),
             self.list_topics: gapic_v1.method.wrap_method(
                 self.list_topics,
                 default_retry=retries.Retry(
@@ -231,15 +198,15 @@
                     maximum=60.0,
                     multiplier=1.3,
                     predicate=retries.if_exception_type(
                         core_exceptions.Aborted,
                         core_exceptions.ServiceUnavailable,
                         core_exceptions.Unknown,
                     ),
-                    deadline=60.0,
+                    deadline=600.0,
                 ),
                 default_timeout=60.0,
                 client_info=client_info,
             ),
             self.list_topic_subscriptions: gapic_v1.method.wrap_method(
                 self.list_topic_subscriptions,
                 default_retry=retries.Retry(
@@ -247,15 +214,15 @@
                     maximum=60.0,
                     multiplier=1.3,
                     predicate=retries.if_exception_type(
                         core_exceptions.Aborted,
                         core_exceptions.ServiceUnavailable,
                         core_exceptions.Unknown,
                     ),
-                    deadline=60.0,
+                    deadline=600.0,
                 ),
                 default_timeout=60.0,
                 client_info=client_info,
             ),
             self.list_topic_snapshots: gapic_v1.method.wrap_method(
                 self.list_topic_snapshots,
                 default_retry=retries.Retry(
@@ -263,49 +230,58 @@
                     maximum=60.0,
                     multiplier=1.3,
                     predicate=retries.if_exception_type(
                         core_exceptions.Aborted,
                         core_exceptions.ServiceUnavailable,
                         core_exceptions.Unknown,
                     ),
-                    deadline=60.0,
+                    deadline=600.0,
                 ),
                 default_timeout=60.0,
                 client_info=client_info,
             ),
             self.delete_topic: gapic_v1.method.wrap_method(
                 self.delete_topic,
                 default_retry=retries.Retry(
                     initial=0.1,
                     maximum=60.0,
                     multiplier=1.3,
                     predicate=retries.if_exception_type(
                         core_exceptions.ServiceUnavailable,
                     ),
-                    deadline=60.0,
+                    deadline=600.0,
                 ),
                 default_timeout=60.0,
                 client_info=client_info,
             ),
             self.detach_subscription: gapic_v1.method.wrap_method(
                 self.detach_subscription,
                 default_retry=retries.Retry(
                     initial=0.1,
                     maximum=60.0,
                     multiplier=1.3,
                     predicate=retries.if_exception_type(
                         core_exceptions.ServiceUnavailable,
                     ),
-                    deadline=60.0,
+                    deadline=600.0,
                 ),
                 default_timeout=60.0,
                 client_info=client_info,
             ),
         }
 
+    def close(self):
+        """Closes resources associated with the transport.
+
+       .. warning::
+            Only call this method if the transport is NOT shared
+            with other clients - this may cause errors in other clients!
+        """
+        raise NotImplementedError()
+
     @property
     def create_topic(
         self,
     ) -> Callable[[pubsub.Topic], Union[pubsub.Topic, Awaitable[pubsub.Topic]]]:
         raise NotImplementedError()
 
     @property
```

### Comparing `google-cloud-pubsub-2.8.0/google/pubsub_v1/services/publisher/transports/grpc.py` & `google-cloud-pubsub-2.9.0/google/pubsub_v1/services/publisher/transports/grpc.py`

 * *Files 0% similar despite different names*

```diff
@@ -12,16 +12,16 @@
 # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 # See the License for the specific language governing permissions and
 # limitations under the License.
 #
 import warnings
 from typing import Callable, Dict, Optional, Sequence, Tuple, Union
 
-from google.api_core import grpc_helpers  # type: ignore
-from google.api_core import gapic_v1  # type: ignore
+from google.api_core import grpc_helpers
+from google.api_core import gapic_v1
 import google.auth  # type: ignore
 from google.auth import credentials as ga_credentials  # type: ignore
 from google.auth.transport.grpc import SslCredentials  # type: ignore
 
 import grpc  # type: ignore
 
 from google.iam.v1 import iam_policy_pb2  # type: ignore
@@ -80,24 +80,24 @@
             scopes (Optional(Sequence[str])): A list of scopes. This argument is
                 ignored if ``channel`` is provided.
             channel (Optional[grpc.Channel]): A ``Channel`` instance through
                 which to make calls.
             api_mtls_endpoint (Optional[str]): Deprecated. The mutual TLS endpoint.
                 If provided, it overrides the ``host`` argument and tries to create
                 a mutual TLS channel with client SSL credentials from
-                ``client_cert_source`` or applicatin default SSL credentials.
+                ``client_cert_source`` or application default SSL credentials.
             client_cert_source (Optional[Callable[[], Tuple[bytes, bytes]]]):
                 Deprecated. A callback to provide client SSL certificate bytes and
                 private key bytes, both in PEM format. It is ignored if
                 ``api_mtls_endpoint`` is None.
             ssl_channel_credentials (grpc.ChannelCredentials): SSL credentials
-                for grpc channel. It is ignored if ``channel`` is provided.
+                for the grpc channel. It is ignored if ``channel`` is provided.
             client_cert_source_for_mtls (Optional[Callable[[], Tuple[bytes, bytes]]]):
                 A callback to provide client certificate bytes and private key bytes,
-                both in PEM format. It is used to configure mutual TLS channel. It is
+                both in PEM format. It is used to configure a mutual TLS channel. It is
                 ignored if ``channel`` or ``ssl_channel_credentials`` is provided.
             quota_project_id (Optional[str]): An optional project to use for billing
                 and quota.
             client_info (google.api_core.gapic_v1.client_info.ClientInfo):
                 The client info used to send a user-agent string along with
                 API requests. If ``None``, then default info will be used.
                 Generally, you only need to set this if you're developing
@@ -555,9 +555,12 @@
             self._stubs["test_iam_permissions"] = self.grpc_channel.unary_unary(
                 "/google.iam.v1.IAMPolicy/TestIamPermissions",
                 request_serializer=iam_policy_pb2.TestIamPermissionsRequest.SerializeToString,
                 response_deserializer=iam_policy_pb2.TestIamPermissionsResponse.FromString,
             )
         return self._stubs["test_iam_permissions"]
 
+    def close(self):
+        self.grpc_channel.close()
+
 
 __all__ = ("PublisherGrpcTransport",)
```

### Comparing `google-cloud-pubsub-2.8.0/google/pubsub_v1/services/publisher/transports/grpc_asyncio.py` & `google-cloud-pubsub-2.9.0/google/pubsub_v1/services/publisher/transports/grpc_asyncio.py`

 * *Files 2% similar despite different names*

```diff
@@ -12,19 +12,18 @@
 # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 # See the License for the specific language governing permissions and
 # limitations under the License.
 #
 import warnings
 from typing import Awaitable, Callable, Dict, Optional, Sequence, Tuple, Union
 
-from google.api_core import gapic_v1  # type: ignore
-from google.api_core import grpc_helpers_async  # type: ignore
+from google.api_core import gapic_v1
+from google.api_core import grpc_helpers_async
 from google.auth import credentials as ga_credentials  # type: ignore
 from google.auth.transport.grpc import SslCredentials  # type: ignore
-import packaging.version
 
 import grpc  # type: ignore
 from grpc.experimental import aio  # type: ignore
 
 from google.iam.v1 import iam_policy_pb2  # type: ignore
 from google.iam.v1 import policy_pb2  # type: ignore
 from google.protobuf import empty_pb2  # type: ignore
@@ -127,24 +126,24 @@
                 service. These are only used when credentials are not specified and
                 are passed to :func:`google.auth.default`.
             channel (Optional[aio.Channel]): A ``Channel`` instance through
                 which to make calls.
             api_mtls_endpoint (Optional[str]): Deprecated. The mutual TLS endpoint.
                 If provided, it overrides the ``host`` argument and tries to create
                 a mutual TLS channel with client SSL credentials from
-                ``client_cert_source`` or applicatin default SSL credentials.
+                ``client_cert_source`` or application default SSL credentials.
             client_cert_source (Optional[Callable[[], Tuple[bytes, bytes]]]):
                 Deprecated. A callback to provide client SSL certificate bytes and
                 private key bytes, both in PEM format. It is ignored if
                 ``api_mtls_endpoint`` is None.
             ssl_channel_credentials (grpc.ChannelCredentials): SSL credentials
-                for grpc channel. It is ignored if ``channel`` is provided.
+                for the grpc channel. It is ignored if ``channel`` is provided.
             client_cert_source_for_mtls (Optional[Callable[[], Tuple[bytes, bytes]]]):
                 A callback to provide client certificate bytes and private key bytes,
-                both in PEM format. It is used to configure mutual TLS channel. It is
+                both in PEM format. It is used to configure a mutual TLS channel. It is
                 ignored if ``channel`` or ``ssl_channel_credentials`` is provided.
             quota_project_id (Optional[str]): An optional project to use for billing
                 and quota.
             client_info (google.api_core.gapic_v1.client_info.ClientInfo):
                 The client info used to send a user-agent string along with
                 API requests. If ``None``, then default info will be used.
                 Generally, you only need to set this if you're developing
@@ -565,9 +564,12 @@
             self._stubs["test_iam_permissions"] = self.grpc_channel.unary_unary(
                 "/google.iam.v1.IAMPolicy/TestIamPermissions",
                 request_serializer=iam_policy_pb2.TestIamPermissionsRequest.SerializeToString,
                 response_deserializer=iam_policy_pb2.TestIamPermissionsResponse.FromString,
             )
         return self._stubs["test_iam_permissions"]
 
+    def close(self):
+        return self.grpc_channel.close()
+
 
 __all__ = ("PublisherGrpcAsyncIOTransport",)
```

### Comparing `google-cloud-pubsub-2.8.0/google/pubsub_v1/services/schema_service/__init__.py` & `google-cloud-pubsub-2.9.0/google/pubsub_v1/services/schema_service/__init__.py`

 * *Files identical despite different names*

### Comparing `google-cloud-pubsub-2.8.0/google/pubsub_v1/services/schema_service/async_client.py` & `google-cloud-pubsub-2.9.0/google/pubsub_v1/services/schema_service/async_client.py`

 * *Files 7% similar despite different names*

```diff
@@ -15,21 +15,26 @@
 #
 from collections import OrderedDict
 import functools
 import re
 from typing import Dict, Sequence, Tuple, Type, Union
 import pkg_resources
 
-import google.api_core.client_options as ClientOptions  # type: ignore
-from google.api_core import exceptions as core_exceptions  # type: ignore
-from google.api_core import gapic_v1  # type: ignore
-from google.api_core import retry as retries  # type: ignore
+from google.api_core.client_options import ClientOptions
+from google.api_core import exceptions as core_exceptions
+from google.api_core import gapic_v1
+from google.api_core import retry as retries
 from google.auth import credentials as ga_credentials  # type: ignore
 from google.oauth2 import service_account  # type: ignore
 
+try:
+    OptionalRetry = Union[retries.Retry, gapic_v1.method._MethodDefault]
+except AttributeError:  # pragma: NO COVER
+    OptionalRetry = Union[retries.Retry, object]  # type: ignore
+
 from google.iam.v1 import iam_policy_pb2  # type: ignore
 from google.iam.v1 import policy_pb2  # type: ignore
 from google.pubsub_v1.services.schema_service import pagers
 from google.pubsub_v1.types import schema
 from google.pubsub_v1.types import schema as gp_schema
 from .transports.base import SchemaServiceTransport, DEFAULT_CLIENT_INFO
 from .transports.grpc_asyncio import SchemaServiceGrpcAsyncIOTransport
@@ -162,27 +167,27 @@
             transport=transport,
             client_options=client_options,
             client_info=client_info,
         )
 
     async def create_schema(
         self,
-        request: gp_schema.CreateSchemaRequest = None,
+        request: Union[gp_schema.CreateSchemaRequest, dict] = None,
         *,
         parent: str = None,
         schema: gp_schema.Schema = None,
         schema_id: str = None,
-        retry: retries.Retry = gapic_v1.method.DEFAULT,
+        retry: OptionalRetry = gapic_v1.method.DEFAULT,
         timeout: float = None,
         metadata: Sequence[Tuple[str, str]] = (),
     ) -> gp_schema.Schema:
         r"""Creates a schema.
 
         Args:
-            request (:class:`google.pubsub_v1.types.CreateSchemaRequest`):
+            request (Union[google.pubsub_v1.types.CreateSchemaRequest, dict]):
                 The request object. Request for the CreateSchema method.
             parent (:class:`str`):
                 Required. The name of the project in which to create the
                 schema. Format is ``projects/{project-id}``.
 
                 This corresponds to the ``parent`` field
                 on the ``request`` instance; if ``request`` is provided, this
@@ -257,25 +262,25 @@
         response = await rpc(request, retry=retry, timeout=timeout, metadata=metadata,)
 
         # Done; return the response.
         return response
 
     async def get_schema(
         self,
-        request: schema.GetSchemaRequest = None,
+        request: Union[schema.GetSchemaRequest, dict] = None,
         *,
         name: str = None,
-        retry: retries.Retry = gapic_v1.method.DEFAULT,
+        retry: OptionalRetry = gapic_v1.method.DEFAULT,
         timeout: float = None,
         metadata: Sequence[Tuple[str, str]] = (),
     ) -> schema.Schema:
         r"""Gets a schema.
 
         Args:
-            request (:class:`google.pubsub_v1.types.GetSchemaRequest`):
+            request (Union[google.pubsub_v1.types.GetSchemaRequest, dict]):
                 The request object. Request for the GetSchema method.
             name (:class:`str`):
                 Required. The name of the schema to get. Format is
                 ``projects/{project}/schemas/{schema}``.
 
                 This corresponds to the ``name`` field
                 on the ``request`` instance; if ``request`` is provided, this
@@ -325,25 +330,25 @@
         response = await rpc(request, retry=retry, timeout=timeout, metadata=metadata,)
 
         # Done; return the response.
         return response
 
     async def list_schemas(
         self,
-        request: schema.ListSchemasRequest = None,
+        request: Union[schema.ListSchemasRequest, dict] = None,
         *,
         parent: str = None,
-        retry: retries.Retry = gapic_v1.method.DEFAULT,
+        retry: OptionalRetry = gapic_v1.method.DEFAULT,
         timeout: float = None,
         metadata: Sequence[Tuple[str, str]] = (),
     ) -> pagers.ListSchemasAsyncPager:
         r"""Lists schemas in a project.
 
         Args:
-            request (:class:`google.pubsub_v1.types.ListSchemasRequest`):
+            request (Union[google.pubsub_v1.types.ListSchemasRequest, dict]):
                 The request object. Request for the `ListSchemas`
                 method.
             parent (:class:`str`):
                 Required. The name of the project in which to list
                 schemas. Format is ``projects/{project-id}``.
 
                 This corresponds to the ``parent`` field
@@ -404,25 +409,25 @@
         )
 
         # Done; return the response.
         return response
 
     async def delete_schema(
         self,
-        request: schema.DeleteSchemaRequest = None,
+        request: Union[schema.DeleteSchemaRequest, dict] = None,
         *,
         name: str = None,
-        retry: retries.Retry = gapic_v1.method.DEFAULT,
+        retry: OptionalRetry = gapic_v1.method.DEFAULT,
         timeout: float = None,
         metadata: Sequence[Tuple[str, str]] = (),
     ) -> None:
         r"""Deletes a schema.
 
         Args:
-            request (:class:`google.pubsub_v1.types.DeleteSchemaRequest`):
+            request (Union[google.pubsub_v1.types.DeleteSchemaRequest, dict]):
                 The request object. Request for the `DeleteSchema`
                 method.
             name (:class:`str`):
                 Required. Name of the schema to delete. Format is
                 ``projects/{project}/schemas/{schema}``.
 
                 This corresponds to the ``name`` field
@@ -468,26 +473,26 @@
         # Send the request.
         await rpc(
             request, retry=retry, timeout=timeout, metadata=metadata,
         )
 
     async def validate_schema(
         self,
-        request: gp_schema.ValidateSchemaRequest = None,
+        request: Union[gp_schema.ValidateSchemaRequest, dict] = None,
         *,
         parent: str = None,
         schema: gp_schema.Schema = None,
-        retry: retries.Retry = gapic_v1.method.DEFAULT,
+        retry: OptionalRetry = gapic_v1.method.DEFAULT,
         timeout: float = None,
         metadata: Sequence[Tuple[str, str]] = (),
     ) -> gp_schema.ValidateSchemaResponse:
         r"""Validates a schema.
 
         Args:
-            request (:class:`google.pubsub_v1.types.ValidateSchemaRequest`):
+            request (Union[google.pubsub_v1.types.ValidateSchemaRequest, dict]):
                 The request object. Request for the `ValidateSchema`
                 method.
             parent (:class:`str`):
                 Required. The name of the project in which to validate
                 schemas. Format is ``projects/{project-id}``.
 
                 This corresponds to the ``parent`` field
@@ -549,24 +554,24 @@
         response = await rpc(request, retry=retry, timeout=timeout, metadata=metadata,)
 
         # Done; return the response.
         return response
 
     async def validate_message(
         self,
-        request: schema.ValidateMessageRequest = None,
+        request: Union[schema.ValidateMessageRequest, dict] = None,
         *,
-        retry: retries.Retry = gapic_v1.method.DEFAULT,
+        retry: OptionalRetry = gapic_v1.method.DEFAULT,
         timeout: float = None,
         metadata: Sequence[Tuple[str, str]] = (),
     ) -> schema.ValidateMessageResponse:
         r"""Validates a message against a schema.
 
         Args:
-            request (:class:`google.pubsub_v1.types.ValidateMessageRequest`):
+            request (Union[google.pubsub_v1.types.ValidateMessageRequest, dict]):
                 The request object. Request for the `ValidateMessage`
                 method.
             retry (google.api_core.retry.Retry): Designation of what errors, if any,
                 should be retried.
             timeout (float): The timeout for this request.
             metadata (Sequence[Tuple[str, str]]): Strings which should be
                 sent along with the request as metadata.
@@ -600,15 +605,15 @@
         # Done; return the response.
         return response
 
     async def set_iam_policy(
         self,
         request: iam_policy_pb2.SetIamPolicyRequest = None,
         *,
-        retry: retries.Retry = gapic_v1.method.DEFAULT,
+        retry: OptionalRetry = gapic_v1.method.DEFAULT,
         timeout: float = None,
         metadata: Sequence[Tuple[str, str]] = (),
     ) -> policy_pb2.Policy:
         r"""Sets the IAM access control policy on the specified function.
 
         Replaces any existing policy.
 
@@ -708,15 +713,15 @@
         # Done; return the response.
         return response
 
     async def get_iam_policy(
         self,
         request: iam_policy_pb2.GetIamPolicyRequest = None,
         *,
-        retry: retries.Retry = gapic_v1.method.DEFAULT,
+        retry: OptionalRetry = gapic_v1.method.DEFAULT,
         timeout: float = None,
         metadata: Sequence[Tuple[str, str]] = (),
     ) -> policy_pb2.Policy:
         r"""Gets the IAM access control policy for a function.
 
         Returns an empty policy if the function exists and does
         not have a policy set.
@@ -817,15 +822,15 @@
         # Done; return the response.
         return response
 
     async def test_iam_permissions(
         self,
         request: iam_policy_pb2.TestIamPermissionsRequest = None,
         *,
-        retry: retries.Retry = gapic_v1.method.DEFAULT,
+        retry: OptionalRetry = gapic_v1.method.DEFAULT,
         timeout: float = None,
         metadata: Sequence[Tuple[str, str]] = (),
     ) -> iam_policy_pb2.TestIamPermissionsResponse:
         r"""Tests the specified permissions against the IAM access control
             policy for a function.
 
         If the function does not exist, this will
@@ -867,14 +872,20 @@
 
         # Send the request.
         response = await rpc(request, retry=retry, timeout=timeout, metadata=metadata,)
 
         # Done; return the response.
         return response
 
+    async def __aenter__(self):
+        return self
+
+    async def __aexit__(self, exc_type, exc, tb):
+        await self.transport.close()
+
 
 try:
     DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
         client_library_version=pkg_resources.get_distribution(
             "google-cloud-pubsub",
         ).version,
     )
```

### Comparing `google-cloud-pubsub-2.8.0/google/pubsub_v1/services/schema_service/client.py` & `google-cloud-pubsub-2.9.0/google/pubsub_v1/services/schema_service/client.py`

 * *Files 2% similar despite different names*

```diff
@@ -10,30 +10,34 @@
 # Unless required by applicable law or agreed to in writing, software
 # distributed under the License is distributed on an "AS IS" BASIS,
 # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 # See the License for the specific language governing permissions and
 # limitations under the License.
 #
 from collections import OrderedDict
-from distutils import util
 import os
 import re
-from typing import Callable, Dict, Optional, Sequence, Tuple, Type, Union
+from typing import Dict, Optional, Sequence, Tuple, Type, Union
 import pkg_resources
 
-from google.api_core import client_options as client_options_lib  # type: ignore
-from google.api_core import exceptions as core_exceptions  # type: ignore
-from google.api_core import gapic_v1  # type: ignore
-from google.api_core import retry as retries  # type: ignore
+from google.api_core import client_options as client_options_lib
+from google.api_core import exceptions as core_exceptions
+from google.api_core import gapic_v1
+from google.api_core import retry as retries
 from google.auth import credentials as ga_credentials  # type: ignore
 from google.auth.transport import mtls  # type: ignore
 from google.auth.transport.grpc import SslCredentials  # type: ignore
 from google.auth.exceptions import MutualTLSChannelError  # type: ignore
 from google.oauth2 import service_account  # type: ignore
 
+try:
+    OptionalRetry = Union[retries.Retry, gapic_v1.method._MethodDefault]
+except AttributeError:  # pragma: NO COVER
+    OptionalRetry = Union[retries.Retry, object]  # type: ignore
+
 from google.iam.v1 import iam_policy_pb2  # type: ignore
 from google.iam.v1 import policy_pb2  # type: ignore
 from google.pubsub_v1.services.schema_service import pagers
 from google.pubsub_v1.types import schema
 from google.pubsub_v1.types import schema as gp_schema
 from .transports.base import SchemaServiceTransport, DEFAULT_CLIENT_INFO
 from .transports.grpc import SchemaServiceGrpcTransport
@@ -275,16 +279,23 @@
         """
         if isinstance(client_options, dict):
             client_options = client_options_lib.from_dict(client_options)
         if client_options is None:
             client_options = client_options_lib.ClientOptions()
 
         # Create SSL credentials for mutual TLS if needed.
-        use_client_cert = bool(
-            util.strtobool(os.getenv("GOOGLE_API_USE_CLIENT_CERTIFICATE", "false"))
+        if os.getenv("GOOGLE_API_USE_CLIENT_CERTIFICATE", "false") not in (
+            "true",
+            "false",
+        ):
+            raise ValueError(
+                "Environment variable `GOOGLE_API_USE_CLIENT_CERTIFICATE` must be either `true` or `false`"
+            )
+        use_client_cert = (
+            os.getenv("GOOGLE_API_USE_CLIENT_CERTIFICATE", "false") == "true"
         )
 
         client_cert_source_func = None
         is_mtls = False
         if use_client_cert:
             if client_options.client_cert_source:
                 is_mtls = True
@@ -338,35 +349,32 @@
                 credentials=credentials,
                 credentials_file=client_options.credentials_file,
                 host=api_endpoint,
                 scopes=client_options.scopes,
                 client_cert_source_for_mtls=client_cert_source_func,
                 quota_project_id=client_options.quota_project_id,
                 client_info=client_info,
-                always_use_jwt_access=(
-                    Transport == type(self).get_transport_class("grpc")
-                    or Transport == type(self).get_transport_class("grpc_asyncio")
-                ),
+                always_use_jwt_access=True,
             )
 
     def create_schema(
         self,
-        request: gp_schema.CreateSchemaRequest = None,
+        request: Union[gp_schema.CreateSchemaRequest, dict] = None,
         *,
         parent: str = None,
         schema: gp_schema.Schema = None,
         schema_id: str = None,
-        retry: retries.Retry = gapic_v1.method.DEFAULT,
+        retry: OptionalRetry = gapic_v1.method.DEFAULT,
         timeout: float = None,
         metadata: Sequence[Tuple[str, str]] = (),
     ) -> gp_schema.Schema:
         r"""Creates a schema.
 
         Args:
-            request (google.pubsub_v1.types.CreateSchemaRequest):
+            request (Union[google.pubsub_v1.types.CreateSchemaRequest, dict]):
                 The request object. Request for the CreateSchema method.
             parent (str):
                 Required. The name of the project in which to create the
                 schema. Format is ``projects/{project-id}``.
 
                 This corresponds to the ``parent`` field
                 on the ``request`` instance; if ``request`` is provided, this
@@ -441,25 +449,25 @@
         response = rpc(request, retry=retry, timeout=timeout, metadata=metadata,)
 
         # Done; return the response.
         return response
 
     def get_schema(
         self,
-        request: schema.GetSchemaRequest = None,
+        request: Union[schema.GetSchemaRequest, dict] = None,
         *,
         name: str = None,
-        retry: retries.Retry = gapic_v1.method.DEFAULT,
+        retry: OptionalRetry = gapic_v1.method.DEFAULT,
         timeout: float = None,
         metadata: Sequence[Tuple[str, str]] = (),
     ) -> schema.Schema:
         r"""Gets a schema.
 
         Args:
-            request (google.pubsub_v1.types.GetSchemaRequest):
+            request (Union[google.pubsub_v1.types.GetSchemaRequest, dict]):
                 The request object. Request for the GetSchema method.
             name (str):
                 Required. The name of the schema to get. Format is
                 ``projects/{project}/schemas/{schema}``.
 
                 This corresponds to the ``name`` field
                 on the ``request`` instance; if ``request`` is provided, this
@@ -509,25 +517,25 @@
         response = rpc(request, retry=retry, timeout=timeout, metadata=metadata,)
 
         # Done; return the response.
         return response
 
     def list_schemas(
         self,
-        request: schema.ListSchemasRequest = None,
+        request: Union[schema.ListSchemasRequest, dict] = None,
         *,
         parent: str = None,
-        retry: retries.Retry = gapic_v1.method.DEFAULT,
+        retry: OptionalRetry = gapic_v1.method.DEFAULT,
         timeout: float = None,
         metadata: Sequence[Tuple[str, str]] = (),
     ) -> pagers.ListSchemasPager:
         r"""Lists schemas in a project.
 
         Args:
-            request (google.pubsub_v1.types.ListSchemasRequest):
+            request (Union[google.pubsub_v1.types.ListSchemasRequest, dict]):
                 The request object. Request for the `ListSchemas`
                 method.
             parent (str):
                 Required. The name of the project in which to list
                 schemas. Format is ``projects/{project-id}``.
 
                 This corresponds to the ``parent`` field
@@ -588,25 +596,25 @@
         )
 
         # Done; return the response.
         return response
 
     def delete_schema(
         self,
-        request: schema.DeleteSchemaRequest = None,
+        request: Union[schema.DeleteSchemaRequest, dict] = None,
         *,
         name: str = None,
-        retry: retries.Retry = gapic_v1.method.DEFAULT,
+        retry: OptionalRetry = gapic_v1.method.DEFAULT,
         timeout: float = None,
         metadata: Sequence[Tuple[str, str]] = (),
     ) -> None:
         r"""Deletes a schema.
 
         Args:
-            request (google.pubsub_v1.types.DeleteSchemaRequest):
+            request (Union[google.pubsub_v1.types.DeleteSchemaRequest, dict]):
                 The request object. Request for the `DeleteSchema`
                 method.
             name (str):
                 Required. Name of the schema to delete. Format is
                 ``projects/{project}/schemas/{schema}``.
 
                 This corresponds to the ``name`` field
@@ -652,26 +660,26 @@
         # Send the request.
         rpc(
             request, retry=retry, timeout=timeout, metadata=metadata,
         )
 
     def validate_schema(
         self,
-        request: gp_schema.ValidateSchemaRequest = None,
+        request: Union[gp_schema.ValidateSchemaRequest, dict] = None,
         *,
         parent: str = None,
         schema: gp_schema.Schema = None,
-        retry: retries.Retry = gapic_v1.method.DEFAULT,
+        retry: OptionalRetry = gapic_v1.method.DEFAULT,
         timeout: float = None,
         metadata: Sequence[Tuple[str, str]] = (),
     ) -> gp_schema.ValidateSchemaResponse:
         r"""Validates a schema.
 
         Args:
-            request (google.pubsub_v1.types.ValidateSchemaRequest):
+            request (Union[google.pubsub_v1.types.ValidateSchemaRequest, dict]):
                 The request object. Request for the `ValidateSchema`
                 method.
             parent (str):
                 Required. The name of the project in which to validate
                 schemas. Format is ``projects/{project-id}``.
 
                 This corresponds to the ``parent`` field
@@ -733,24 +741,24 @@
         response = rpc(request, retry=retry, timeout=timeout, metadata=metadata,)
 
         # Done; return the response.
         return response
 
     def validate_message(
         self,
-        request: schema.ValidateMessageRequest = None,
+        request: Union[schema.ValidateMessageRequest, dict] = None,
         *,
-        retry: retries.Retry = gapic_v1.method.DEFAULT,
+        retry: OptionalRetry = gapic_v1.method.DEFAULT,
         timeout: float = None,
         metadata: Sequence[Tuple[str, str]] = (),
     ) -> schema.ValidateMessageResponse:
         r"""Validates a message against a schema.
 
         Args:
-            request (google.pubsub_v1.types.ValidateMessageRequest):
+            request (Union[google.pubsub_v1.types.ValidateMessageRequest, dict]):
                 The request object. Request for the `ValidateMessage`
                 method.
             retry (google.api_core.retry.Retry): Designation of what errors, if any,
                 should be retried.
             timeout (float): The timeout for this request.
             metadata (Sequence[Tuple[str, str]]): Strings which should be
                 sent along with the request as metadata.
@@ -781,19 +789,32 @@
 
         # Send the request.
         response = rpc(request, retry=retry, timeout=timeout, metadata=metadata,)
 
         # Done; return the response.
         return response
 
+    def __enter__(self):
+        return self
+
+    def __exit__(self, type, value, traceback):
+        """Releases underlying transport's resources.
+
+        .. warning::
+            ONLY use as a context manager if the transport is NOT shared
+            with other clients! Exiting the with block will CLOSE the transport
+            and may cause errors in other clients!
+        """
+        self.transport.close()
+
     def set_iam_policy(
         self,
         request: iam_policy_pb2.SetIamPolicyRequest = None,
         *,
-        retry: retries.Retry = gapic_v1.method.DEFAULT,
+        retry: OptionalRetry = gapic_v1.method.DEFAULT,
         timeout: float = None,
         metadata: Sequence[Tuple[str, str]] = (),
     ) -> policy_pb2.Policy:
         r"""Sets the IAM access control policy on the specified function.
 
         Replaces any existing policy.
 
@@ -893,15 +914,15 @@
         # Done; return the response.
         return response
 
     def get_iam_policy(
         self,
         request: iam_policy_pb2.GetIamPolicyRequest = None,
         *,
-        retry: retries.Retry = gapic_v1.method.DEFAULT,
+        retry: OptionalRetry = gapic_v1.method.DEFAULT,
         timeout: float = None,
         metadata: Sequence[Tuple[str, str]] = (),
     ) -> policy_pb2.Policy:
         r"""Gets the IAM access control policy for a function.
 
         Returns an empty policy if the function exists and does not have a
         policy set.
@@ -1002,15 +1023,15 @@
         # Done; return the response.
         return response
 
     def test_iam_permissions(
         self,
         request: iam_policy_pb2.TestIamPermissionsRequest = None,
         *,
-        retry: retries.Retry = gapic_v1.method.DEFAULT,
+        retry: OptionalRetry = gapic_v1.method.DEFAULT,
         timeout: float = None,
         metadata: Sequence[Tuple[str, str]] = (),
     ) -> iam_policy_pb2.TestIamPermissionsResponse:
         r"""Tests the specified IAM permissions against the IAM access control
             policy for a function.
 
         If the function does not exist, this will return an empty set
```

### Comparing `google-cloud-pubsub-2.8.0/google/pubsub_v1/services/schema_service/pagers.py` & `google-cloud-pubsub-2.9.0/google/pubsub_v1/services/schema_service/pagers.py`

 * *Files 2% similar despite different names*

```diff
@@ -11,21 +11,21 @@
 # distributed under the License is distributed on an "AS IS" BASIS,
 # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 # See the License for the specific language governing permissions and
 # limitations under the License.
 #
 from typing import (
     Any,
-    AsyncIterable,
+    AsyncIterator,
     Awaitable,
     Callable,
-    Iterable,
     Sequence,
     Tuple,
     Optional,
+    Iterator,
 )
 
 from google.pubsub_v1.types import schema
 
 
 class ListSchemasPager:
     """A pager for iterating through ``list_schemas`` requests.
@@ -70,22 +70,22 @@
         self._response = response
         self._metadata = metadata
 
     def __getattr__(self, name: str) -> Any:
         return getattr(self._response, name)
 
     @property
-    def pages(self) -> Iterable[schema.ListSchemasResponse]:
+    def pages(self) -> Iterator[schema.ListSchemasResponse]:
         yield self._response
         while self._response.next_page_token:
             self._request.page_token = self._response.next_page_token
             self._response = self._method(self._request, metadata=self._metadata)
             yield self._response
 
-    def __iter__(self) -> Iterable[schema.Schema]:
+    def __iter__(self) -> Iterator[schema.Schema]:
         for page in self.pages:
             yield from page.schemas
 
     def __repr__(self) -> str:
         return "{0}<{1!r}>".format(self.__class__.__name__, self._response)
 
 
@@ -132,22 +132,22 @@
         self._response = response
         self._metadata = metadata
 
     def __getattr__(self, name: str) -> Any:
         return getattr(self._response, name)
 
     @property
-    async def pages(self) -> AsyncIterable[schema.ListSchemasResponse]:
+    async def pages(self) -> AsyncIterator[schema.ListSchemasResponse]:
         yield self._response
         while self._response.next_page_token:
             self._request.page_token = self._response.next_page_token
             self._response = await self._method(self._request, metadata=self._metadata)
             yield self._response
 
-    def __aiter__(self) -> AsyncIterable[schema.Schema]:
+    def __aiter__(self) -> AsyncIterator[schema.Schema]:
         async def async_generator():
             async for page in self.pages:
                 for response in page.schemas:
                     yield response
 
         return async_generator()
```

### Comparing `google-cloud-pubsub-2.8.0/google/pubsub_v1/services/schema_service/transports/__init__.py` & `google-cloud-pubsub-2.9.0/google/pubsub_v1/services/schema_service/transports/__init__.py`

 * *Files identical despite different names*

### Comparing `google-cloud-pubsub-2.8.0/google/pubsub_v1/services/schema_service/transports/base.py` & `google-cloud-pubsub-2.9.0/google/pubsub_v1/services/schema_service/transports/base.py`

 * *Files 8% similar despite different names*

```diff
@@ -11,22 +11,21 @@
 # distributed under the License is distributed on an "AS IS" BASIS,
 # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 # See the License for the specific language governing permissions and
 # limitations under the License.
 #
 import abc
 from typing import Awaitable, Callable, Dict, Optional, Sequence, Union
-import packaging.version
 import pkg_resources
 
 import google.auth  # type: ignore
-import google.api_core  # type: ignore
-from google.api_core import exceptions as core_exceptions  # type: ignore
-from google.api_core import gapic_v1  # type: ignore
-from google.api_core import retry as retries  # type: ignore
+import google.api_core
+from google.api_core import exceptions as core_exceptions
+from google.api_core import gapic_v1
+from google.api_core import retry as retries
 from google.auth import credentials as ga_credentials  # type: ignore
 from google.oauth2 import service_account  # type: ignore
 
 from google.iam.v1 import iam_policy_pb2  # type: ignore
 from google.iam.v1 import policy_pb2  # type: ignore
 from google.protobuf import empty_pb2  # type: ignore
 from google.pubsub_v1.types import schema
@@ -37,23 +36,14 @@
         client_library_version=pkg_resources.get_distribution(
             "google-cloud-pubsub",
         ).version,
     )
 except pkg_resources.DistributionNotFound:
     DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo()
 
-try:
-    # google.auth.__version__ was added in 1.26.0
-    _GOOGLE_AUTH_VERSION = google.auth.__version__
-except AttributeError:
-    try:  # try pkg_resources if it is available
-        _GOOGLE_AUTH_VERSION = pkg_resources.get_distribution("google-auth").version
-    except pkg_resources.DistributionNotFound:  # pragma: NO COVER
-        _GOOGLE_AUTH_VERSION = None
-
 
 class SchemaServiceTransport(abc.ABC):
     """Abstract transport class for SchemaService."""
 
     AUTH_SCOPES = (
         "https://www.googleapis.com/auth/cloud-platform",
         "https://www.googleapis.com/auth/pubsub",
@@ -98,15 +88,15 @@
                 be used for service account credentials.
         """
         # Save the hostname. Default to port 443 (HTTPS) if none is specified.
         if ":" not in host:
             host += ":443"
         self._host = host
 
-        scopes_kwargs = self._get_scopes_kwargs(self._host, scopes)
+        scopes_kwargs = {"scopes": scopes, "default_scopes": self.AUTH_SCOPES}
 
         # Save the scopes.
         self._scopes = scopes
 
         # If no credentials are provided, then determine the appropriate
         # defaults.
         if credentials and credentials_file:
@@ -120,48 +110,25 @@
             )
 
         elif credentials is None:
             credentials, _ = google.auth.default(
                 **scopes_kwargs, quota_project_id=quota_project_id
             )
 
-        # If the credentials is service account credentials, then always try to use self signed JWT.
+        # If the credentials are service account credentials, then always try to use self signed JWT.
         if (
             always_use_jwt_access
             and isinstance(credentials, service_account.Credentials)
             and hasattr(service_account.Credentials, "with_always_use_jwt_access")
         ):
             credentials = credentials.with_always_use_jwt_access(True)
 
         # Save the credentials.
         self._credentials = credentials
 
-    # TODO(busunkim): This method is in the base transport
-    # to avoid duplicating code across the transport classes. These functions
-    # should be deleted once the minimum required versions of google-auth is increased.
-
-    # TODO: Remove this function once google-auth >= 1.25.0 is required
-    @classmethod
-    def _get_scopes_kwargs(
-        cls, host: str, scopes: Optional[Sequence[str]]
-    ) -> Dict[str, Optional[Sequence[str]]]:
-        """Returns scopes kwargs to pass to google-auth methods depending on the google-auth version"""
-
-        scopes_kwargs = {}
-
-        if _GOOGLE_AUTH_VERSION and (
-            packaging.version.parse(_GOOGLE_AUTH_VERSION)
-            >= packaging.version.parse("1.25.0")
-        ):
-            scopes_kwargs = {"scopes": scopes, "default_scopes": cls.AUTH_SCOPES}
-        else:
-            scopes_kwargs = {"scopes": scopes or cls.AUTH_SCOPES}
-
-        return scopes_kwargs
-
     def _prep_wrapped_messages(self, client_info):
         # Precompute the wrapped methods.
         self._wrapped_methods = {
             self.create_schema: gapic_v1.method.wrap_method(
                 self.create_schema, default_timeout=None, client_info=client_info,
             ),
             self.get_schema: gapic_v1.method.wrap_method(
@@ -177,14 +144,23 @@
                 self.validate_schema, default_timeout=None, client_info=client_info,
             ),
             self.validate_message: gapic_v1.method.wrap_method(
                 self.validate_message, default_timeout=None, client_info=client_info,
             ),
         }
 
+    def close(self):
+        """Closes resources associated with the transport.
+
+       .. warning::
+            Only call this method if the transport is NOT shared
+            with other clients - this may cause errors in other clients!
+        """
+        raise NotImplementedError()
+
     @property
     def create_schema(
         self,
     ) -> Callable[
         [gp_schema.CreateSchemaRequest],
         Union[gp_schema.Schema, Awaitable[gp_schema.Schema]],
     ]:
```

### Comparing `google-cloud-pubsub-2.8.0/google/pubsub_v1/services/schema_service/transports/grpc.py` & `google-cloud-pubsub-2.9.0/google/pubsub_v1/services/schema_service/transports/grpc.py`

 * *Files 2% similar despite different names*

```diff
@@ -12,16 +12,16 @@
 # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 # See the License for the specific language governing permissions and
 # limitations under the License.
 #
 import warnings
 from typing import Callable, Dict, Optional, Sequence, Tuple, Union
 
-from google.api_core import grpc_helpers  # type: ignore
-from google.api_core import gapic_v1  # type: ignore
+from google.api_core import grpc_helpers
+from google.api_core import gapic_v1
 import google.auth  # type: ignore
 from google.auth import credentials as ga_credentials  # type: ignore
 from google.auth.transport.grpc import SslCredentials  # type: ignore
 
 import grpc  # type: ignore
 
 from google.iam.v1 import iam_policy_pb2  # type: ignore
@@ -80,24 +80,24 @@
             scopes (Optional(Sequence[str])): A list of scopes. This argument is
                 ignored if ``channel`` is provided.
             channel (Optional[grpc.Channel]): A ``Channel`` instance through
                 which to make calls.
             api_mtls_endpoint (Optional[str]): Deprecated. The mutual TLS endpoint.
                 If provided, it overrides the ``host`` argument and tries to create
                 a mutual TLS channel with client SSL credentials from
-                ``client_cert_source`` or applicatin default SSL credentials.
+                ``client_cert_source`` or application default SSL credentials.
             client_cert_source (Optional[Callable[[], Tuple[bytes, bytes]]]):
                 Deprecated. A callback to provide client SSL certificate bytes and
                 private key bytes, both in PEM format. It is ignored if
                 ``api_mtls_endpoint`` is None.
             ssl_channel_credentials (grpc.ChannelCredentials): SSL credentials
-                for grpc channel. It is ignored if ``channel`` is provided.
+                for the grpc channel. It is ignored if ``channel`` is provided.
             client_cert_source_for_mtls (Optional[Callable[[], Tuple[bytes, bytes]]]):
                 A callback to provide client certificate bytes and private key bytes,
-                both in PEM format. It is used to configure mutual TLS channel. It is
+                both in PEM format. It is used to configure a mutual TLS channel. It is
                 ignored if ``channel`` or ``ssl_channel_credentials`` is provided.
             quota_project_id (Optional[str]): An optional project to use for billing
                 and quota.
             client_info (google.api_core.gapic_v1.client_info.ClientInfo):
                 The client info used to send a user-agent string along with
                 API requests. If ``None``, then default info will be used.
                 Generally, you only need to set this if you're developing
@@ -458,9 +458,12 @@
             self._stubs["test_iam_permissions"] = self.grpc_channel.unary_unary(
                 "/google.iam.v1.IAMPolicy/TestIamPermissions",
                 request_serializer=iam_policy_pb2.TestIamPermissionsRequest.SerializeToString,
                 response_deserializer=iam_policy_pb2.TestIamPermissionsResponse.FromString,
             )
         return self._stubs["test_iam_permissions"]
 
+    def close(self):
+        self.grpc_channel.close()
+
 
 __all__ = ("SchemaServiceGrpcTransport",)
```

### Comparing `google-cloud-pubsub-2.8.0/google/pubsub_v1/services/schema_service/transports/grpc_asyncio.py` & `google-cloud-pubsub-2.9.0/google/pubsub_v1/services/schema_service/transports/grpc_asyncio.py`

 * *Files 1% similar despite different names*

```diff
@@ -12,19 +12,18 @@
 # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 # See the License for the specific language governing permissions and
 # limitations under the License.
 #
 import warnings
 from typing import Awaitable, Callable, Dict, Optional, Sequence, Tuple, Union
 
-from google.api_core import gapic_v1  # type: ignore
-from google.api_core import grpc_helpers_async  # type: ignore
+from google.api_core import gapic_v1
+from google.api_core import grpc_helpers_async
 from google.auth import credentials as ga_credentials  # type: ignore
 from google.auth.transport.grpc import SslCredentials  # type: ignore
-import packaging.version
 
 import grpc  # type: ignore
 from grpc.experimental import aio  # type: ignore
 
 from google.iam.v1 import iam_policy_pb2  # type: ignore
 from google.iam.v1 import policy_pb2  # type: ignore
 from google.protobuf import empty_pb2  # type: ignore
@@ -127,24 +126,24 @@
                 service. These are only used when credentials are not specified and
                 are passed to :func:`google.auth.default`.
             channel (Optional[aio.Channel]): A ``Channel`` instance through
                 which to make calls.
             api_mtls_endpoint (Optional[str]): Deprecated. The mutual TLS endpoint.
                 If provided, it overrides the ``host`` argument and tries to create
                 a mutual TLS channel with client SSL credentials from
-                ``client_cert_source`` or applicatin default SSL credentials.
+                ``client_cert_source`` or application default SSL credentials.
             client_cert_source (Optional[Callable[[], Tuple[bytes, bytes]]]):
                 Deprecated. A callback to provide client SSL certificate bytes and
                 private key bytes, both in PEM format. It is ignored if
                 ``api_mtls_endpoint`` is None.
             ssl_channel_credentials (grpc.ChannelCredentials): SSL credentials
-                for grpc channel. It is ignored if ``channel`` is provided.
+                for the grpc channel. It is ignored if ``channel`` is provided.
             client_cert_source_for_mtls (Optional[Callable[[], Tuple[bytes, bytes]]]):
                 A callback to provide client certificate bytes and private key bytes,
-                both in PEM format. It is used to configure mutual TLS channel. It is
+                both in PEM format. It is used to configure a mutual TLS channel. It is
                 ignored if ``channel`` or ``ssl_channel_credentials`` is provided.
             quota_project_id (Optional[str]): An optional project to use for billing
                 and quota.
             client_info (google.api_core.gapic_v1.client_info.ClientInfo):
                 The client info used to send a user-agent string along with
                 API requests. If ``None``, then default info will be used.
                 Generally, you only need to set this if you're developing
@@ -469,9 +468,12 @@
             self._stubs["test_iam_permissions"] = self.grpc_channel.unary_unary(
                 "/google.iam.v1.IAMPolicy/TestIamPermissions",
                 request_serializer=iam_policy_pb2.TestIamPermissionsRequest.SerializeToString,
                 response_deserializer=iam_policy_pb2.TestIamPermissionsResponse.FromString,
             )
         return self._stubs["test_iam_permissions"]
 
+    def close(self):
+        return self.grpc_channel.close()
+
 
 __all__ = ("SchemaServiceGrpcAsyncIOTransport",)
```

### Comparing `google-cloud-pubsub-2.8.0/google/pubsub_v1/services/subscriber/__init__.py` & `google-cloud-pubsub-2.9.0/google/pubsub_v1/services/subscriber/__init__.py`

 * *Files identical despite different names*

### Comparing `google-cloud-pubsub-2.8.0/google/pubsub_v1/services/subscriber/async_client.py` & `google-cloud-pubsub-2.9.0/google/pubsub_v1/services/subscriber/async_client.py`

 * *Files 2% similar despite different names*

```diff
@@ -25,21 +25,26 @@
     Tuple,
     Type,
     Union,
 )
 import warnings
 import pkg_resources
 
-import google.api_core.client_options as ClientOptions  # type: ignore
-from google.api_core import exceptions as core_exceptions  # type: ignore
-from google.api_core import gapic_v1  # type: ignore
-from google.api_core import retry as retries  # type: ignore
+from google.api_core.client_options import ClientOptions
+from google.api_core import exceptions as core_exceptions
+from google.api_core import gapic_v1
+from google.api_core import retry as retries
 from google.auth import credentials as ga_credentials  # type: ignore
 from google.oauth2 import service_account  # type: ignore
 
+try:
+    OptionalRetry = Union[retries.Retry, gapic_v1.method._MethodDefault]
+except AttributeError:  # pragma: NO COVER
+    OptionalRetry = Union[retries.Retry, object]  # type: ignore
+
 from google.iam.v1 import iam_policy_pb2  # type: ignore
 from google.iam.v1 import policy_pb2  # type: ignore
 from google.protobuf import duration_pb2  # type: ignore
 from google.protobuf import timestamp_pb2  # type: ignore
 from google.pubsub_v1.services.subscriber import pagers
 from google.pubsub_v1.types import pubsub
 from .transports.base import SubscriberTransport, DEFAULT_CLIENT_INFO
@@ -175,21 +180,21 @@
             transport=transport,
             client_options=client_options,
             client_info=client_info,
         )
 
     async def create_subscription(
         self,
-        request: pubsub.Subscription = None,
+        request: Union[pubsub.Subscription, dict] = None,
         *,
         name: str = None,
         topic: str = None,
         push_config: pubsub.PushConfig = None,
         ack_deadline_seconds: int = None,
-        retry: retries.Retry = gapic_v1.method.DEFAULT,
+        retry: OptionalRetry = gapic_v1.method.DEFAULT,
         timeout: float = None,
         metadata: Sequence[Tuple[str, str]] = (),
     ) -> pubsub.Subscription:
         r"""Creates a subscription to a given topic. See the [resource name
         rules]
         (https://cloud.google.com/pubsub/docs/admin#resource_names). If
         the subscription already exists, returns ``ALREADY_EXISTS``. If
@@ -200,15 +205,15 @@
         as the topic, conforming to the [resource name format]
         (https://cloud.google.com/pubsub/docs/admin#resource_names). The
         generated name is populated in the returned Subscription object.
         Note that for REST API requests, you must specify a name in the
         request.
 
         Args:
-            request (:class:`google.pubsub_v1.types.Subscription`):
+            request (Union[google.pubsub_v1.types.Subscription, dict]):
                 The request object. A subscription resource.
             name (:class:`str`):
                 Required. The name of the subscription. It must have the
                 format
                 ``"projects/{project}/subscriptions/{subscription}"``.
                 ``{subscription}`` must start with a letter, and contain
                 only letters (``[A-Za-z]``), numbers (``[0-9]``), dashes
@@ -330,25 +335,25 @@
         response = await rpc(request, retry=retry, timeout=timeout, metadata=metadata,)
 
         # Done; return the response.
         return response
 
     async def get_subscription(
         self,
-        request: pubsub.GetSubscriptionRequest = None,
+        request: Union[pubsub.GetSubscriptionRequest, dict] = None,
         *,
         subscription: str = None,
-        retry: retries.Retry = gapic_v1.method.DEFAULT,
+        retry: OptionalRetry = gapic_v1.method.DEFAULT,
         timeout: float = None,
         metadata: Sequence[Tuple[str, str]] = (),
     ) -> pubsub.Subscription:
         r"""Gets the configuration details of a subscription.
 
         Args:
-            request (:class:`google.pubsub_v1.types.GetSubscriptionRequest`):
+            request (Union[google.pubsub_v1.types.GetSubscriptionRequest, dict]):
                 The request object. Request for the GetSubscription
                 method.
             subscription (:class:`str`):
                 Required. The name of the subscription to get. Format is
                 ``projects/{project}/subscriptions/{sub}``.
 
                 This corresponds to the ``subscription`` field
@@ -412,26 +417,26 @@
         response = await rpc(request, retry=retry, timeout=timeout, metadata=metadata,)
 
         # Done; return the response.
         return response
 
     async def update_subscription(
         self,
-        request: pubsub.UpdateSubscriptionRequest = None,
+        request: Union[pubsub.UpdateSubscriptionRequest, dict] = None,
         *,
-        retry: retries.Retry = gapic_v1.method.DEFAULT,
+        retry: OptionalRetry = gapic_v1.method.DEFAULT,
         timeout: float = None,
         metadata: Sequence[Tuple[str, str]] = (),
     ) -> pubsub.Subscription:
         r"""Updates an existing subscription. Note that certain
         properties of a subscription, such as its topic, are not
         modifiable.
 
         Args:
-            request (:class:`google.pubsub_v1.types.UpdateSubscriptionRequest`):
+            request (Union[google.pubsub_v1.types.UpdateSubscriptionRequest, dict]):
                 The request object. Request for the UpdateSubscription
                 method.
             retry (google.api_core.retry.Retry): Designation of what errors, if any,
                 should be retried.
             timeout (float): The timeout for this request.
             metadata (Sequence[Tuple[str, str]]): Strings which should be
                 sent along with the request as metadata.
@@ -472,25 +477,25 @@
         response = await rpc(request, retry=retry, timeout=timeout, metadata=metadata,)
 
         # Done; return the response.
         return response
 
     async def list_subscriptions(
         self,
-        request: pubsub.ListSubscriptionsRequest = None,
+        request: Union[pubsub.ListSubscriptionsRequest, dict] = None,
         *,
         project: str = None,
-        retry: retries.Retry = gapic_v1.method.DEFAULT,
+        retry: OptionalRetry = gapic_v1.method.DEFAULT,
         timeout: float = None,
         metadata: Sequence[Tuple[str, str]] = (),
     ) -> pagers.ListSubscriptionsAsyncPager:
         r"""Lists matching subscriptions.
 
         Args:
-            request (:class:`google.pubsub_v1.types.ListSubscriptionsRequest`):
+            request (Union[google.pubsub_v1.types.ListSubscriptionsRequest, dict]):
                 The request object. Request for the `ListSubscriptions`
                 method.
             project (:class:`str`):
                 Required. The name of the project in which to list
                 subscriptions. Format is ``projects/{project-id}``.
 
                 This corresponds to the ``project`` field
@@ -562,30 +567,30 @@
         )
 
         # Done; return the response.
         return response
 
     async def delete_subscription(
         self,
-        request: pubsub.DeleteSubscriptionRequest = None,
+        request: Union[pubsub.DeleteSubscriptionRequest, dict] = None,
         *,
         subscription: str = None,
-        retry: retries.Retry = gapic_v1.method.DEFAULT,
+        retry: OptionalRetry = gapic_v1.method.DEFAULT,
         timeout: float = None,
         metadata: Sequence[Tuple[str, str]] = (),
     ) -> None:
         r"""Deletes an existing subscription. All messages retained in the
         subscription are immediately dropped. Calls to ``Pull`` after
         deletion will return ``NOT_FOUND``. After a subscription is
         deleted, a new one may be created with the same name, but the
         new one has no association with the old subscription or its
         topic unless the same topic is specified.
 
         Args:
-            request (:class:`google.pubsub_v1.types.DeleteSubscriptionRequest`):
+            request (Union[google.pubsub_v1.types.DeleteSubscriptionRequest, dict]):
                 The request object. Request for the DeleteSubscription
                 method.
             subscription (:class:`str`):
                 Required. The subscription to delete. Format is
                 ``projects/{project}/subscriptions/{sub}``.
 
                 This corresponds to the ``subscription`` field
@@ -642,32 +647,32 @@
         # Send the request.
         await rpc(
             request, retry=retry, timeout=timeout, metadata=metadata,
         )
 
     async def modify_ack_deadline(
         self,
-        request: pubsub.ModifyAckDeadlineRequest = None,
+        request: Union[pubsub.ModifyAckDeadlineRequest, dict] = None,
         *,
         subscription: str = None,
         ack_ids: Sequence[str] = None,
         ack_deadline_seconds: int = None,
-        retry: retries.Retry = gapic_v1.method.DEFAULT,
+        retry: OptionalRetry = gapic_v1.method.DEFAULT,
         timeout: float = None,
         metadata: Sequence[Tuple[str, str]] = (),
     ) -> None:
         r"""Modifies the ack deadline for a specific message. This method is
         useful to indicate that more time is needed to process a message
         by the subscriber, or to make the message available for
         redelivery if the processing was interrupted. Note that this
         does not modify the subscription-level ``ackDeadlineSeconds``
         used for subsequent messages.
 
         Args:
-            request (:class:`google.pubsub_v1.types.ModifyAckDeadlineRequest`):
+            request (Union[google.pubsub_v1.types.ModifyAckDeadlineRequest, dict]):
                 The request object. Request for the ModifyAckDeadline
                 method.
             subscription (:class:`str`):
                 Required. The name of the subscription. Format is
                 ``projects/{project}/subscriptions/{sub}``.
 
                 This corresponds to the ``subscription`` field
@@ -749,33 +754,33 @@
         # Send the request.
         await rpc(
             request, retry=retry, timeout=timeout, metadata=metadata,
         )
 
     async def acknowledge(
         self,
-        request: pubsub.AcknowledgeRequest = None,
+        request: Union[pubsub.AcknowledgeRequest, dict] = None,
         *,
         subscription: str = None,
         ack_ids: Sequence[str] = None,
-        retry: retries.Retry = gapic_v1.method.DEFAULT,
+        retry: OptionalRetry = gapic_v1.method.DEFAULT,
         timeout: float = None,
         metadata: Sequence[Tuple[str, str]] = (),
     ) -> None:
         r"""Acknowledges the messages associated with the ``ack_ids`` in the
         ``AcknowledgeRequest``. The Pub/Sub system can remove the
         relevant messages from the subscription.
 
         Acknowledging a message whose ack deadline has expired may
         succeed, but such a message may be redelivered later.
         Acknowledging a message more than once will not result in an
         error.
 
         Args:
-            request (:class:`google.pubsub_v1.types.AcknowledgeRequest`):
+            request (Union[google.pubsub_v1.types.AcknowledgeRequest, dict]):
                 The request object. Request for the Acknowledge method.
             subscription (:class:`str`):
                 Required. The subscription whose message is being
                 acknowledged. Format is
                 ``projects/{project}/subscriptions/{sub}``.
 
                 This corresponds to the ``subscription`` field
@@ -842,29 +847,29 @@
         # Send the request.
         await rpc(
             request, retry=retry, timeout=timeout, metadata=metadata,
         )
 
     async def pull(
         self,
-        request: pubsub.PullRequest = None,
+        request: Union[pubsub.PullRequest, dict] = None,
         *,
         subscription: str = None,
         return_immediately: bool = None,
         max_messages: int = None,
-        retry: retries.Retry = gapic_v1.method.DEFAULT,
+        retry: OptionalRetry = gapic_v1.method.DEFAULT,
         timeout: float = None,
         metadata: Sequence[Tuple[str, str]] = (),
     ) -> pubsub.PullResponse:
         r"""Pulls messages from the server. The server may return
         ``UNAVAILABLE`` if there are too many concurrent pull requests
         pending for the given subscription.
 
         Args:
-            request (:class:`google.pubsub_v1.types.PullRequest`):
+            request (Union[google.pubsub_v1.types.PullRequest, dict]):
                 The request object. Request for the `Pull` method.
             subscription (:class:`str`):
                 Required. The subscription from which messages should be
                 pulled. Format is
                 ``projects/{project}/subscriptions/{sub}``.
 
                 This corresponds to the ``subscription`` field
@@ -964,15 +969,15 @@
         # Done; return the response.
         return response
 
     def streaming_pull(
         self,
         requests: AsyncIterator[pubsub.StreamingPullRequest] = None,
         *,
-        retry: retries.Retry = gapic_v1.method.DEFAULT,
+        retry: OptionalRetry = gapic_v1.method.DEFAULT,
         timeout: float = None,
         metadata: Sequence[Tuple[str, str]] = (),
     ) -> Awaitable[AsyncIterable[pubsub.StreamingPullResponse]]:
         r"""Establishes a stream with the server, which sends messages down
         to the client. The client streams acknowledgements and ack
         deadline modifications back to the server. The server will close
         the stream and return the status on any error. The server may
@@ -1026,32 +1031,32 @@
         response = rpc(requests, retry=retry, timeout=timeout, metadata=metadata,)
 
         # Done; return the response.
         return response
 
     async def modify_push_config(
         self,
-        request: pubsub.ModifyPushConfigRequest = None,
+        request: Union[pubsub.ModifyPushConfigRequest, dict] = None,
         *,
         subscription: str = None,
         push_config: pubsub.PushConfig = None,
-        retry: retries.Retry = gapic_v1.method.DEFAULT,
+        retry: OptionalRetry = gapic_v1.method.DEFAULT,
         timeout: float = None,
         metadata: Sequence[Tuple[str, str]] = (),
     ) -> None:
         r"""Modifies the ``PushConfig`` for a specified subscription.
 
         This may be used to change a push subscription to a pull one
         (signified by an empty ``PushConfig``) or vice versa, or change
         the endpoint URL and other attributes of a push subscription.
         Messages will accumulate for delivery continuously through the
         call regardless of changes to the ``PushConfig``.
 
         Args:
-            request (:class:`google.pubsub_v1.types.ModifyPushConfigRequest`):
+            request (Union[google.pubsub_v1.types.ModifyPushConfigRequest, dict]):
                 The request object. Request for the ModifyPushConfig
                 method.
             subscription (:class:`str`):
                 Required. The name of the subscription. Format is
                 ``projects/{project}/subscriptions/{sub}``.
 
                 This corresponds to the ``subscription`` field
@@ -1122,31 +1127,31 @@
         # Send the request.
         await rpc(
             request, retry=retry, timeout=timeout, metadata=metadata,
         )
 
     async def get_snapshot(
         self,
-        request: pubsub.GetSnapshotRequest = None,
+        request: Union[pubsub.GetSnapshotRequest, dict] = None,
         *,
         snapshot: str = None,
-        retry: retries.Retry = gapic_v1.method.DEFAULT,
+        retry: OptionalRetry = gapic_v1.method.DEFAULT,
         timeout: float = None,
         metadata: Sequence[Tuple[str, str]] = (),
     ) -> pubsub.Snapshot:
         r"""Gets the configuration details of a snapshot.
         Snapshots are used in <a
         href="https://cloud.google.com/pubsub/docs/replay-
         overview">Seek</a> operations, which allow you to manage
         message acknowledgments in bulk. That is, you can set
         the acknowledgment state of messages in an existing
         subscription to the state captured by a snapshot.
 
         Args:
-            request (:class:`google.pubsub_v1.types.GetSnapshotRequest`):
+            request (Union[google.pubsub_v1.types.GetSnapshotRequest, dict]):
                 The request object. Request for the GetSnapshot method.
             snapshot (:class:`str`):
                 Required. The name of the snapshot to get. Format is
                 ``projects/{project}/snapshots/{snap}``.
 
                 This corresponds to the ``snapshot`` field
                 on the ``request`` instance; if ``request`` is provided, this
@@ -1213,29 +1218,29 @@
         response = await rpc(request, retry=retry, timeout=timeout, metadata=metadata,)
 
         # Done; return the response.
         return response
 
     async def list_snapshots(
         self,
-        request: pubsub.ListSnapshotsRequest = None,
+        request: Union[pubsub.ListSnapshotsRequest, dict] = None,
         *,
         project: str = None,
-        retry: retries.Retry = gapic_v1.method.DEFAULT,
+        retry: OptionalRetry = gapic_v1.method.DEFAULT,
         timeout: float = None,
         metadata: Sequence[Tuple[str, str]] = (),
     ) -> pagers.ListSnapshotsAsyncPager:
         r"""Lists the existing snapshots. Snapshots are used in
         `Seek <https://cloud.google.com/pubsub/docs/replay-overview>`__
         operations, which allow you to manage message acknowledgments in
         bulk. That is, you can set the acknowledgment state of messages
         in an existing subscription to the state captured by a snapshot.
 
         Args:
-            request (:class:`google.pubsub_v1.types.ListSnapshotsRequest`):
+            request (Union[google.pubsub_v1.types.ListSnapshotsRequest, dict]):
                 The request object. Request for the `ListSnapshots`
                 method.
             project (:class:`str`):
                 Required. The name of the project in which to list
                 snapshots. Format is ``projects/{project-id}``.
 
                 This corresponds to the ``project`` field
@@ -1307,19 +1312,19 @@
         )
 
         # Done; return the response.
         return response
 
     async def create_snapshot(
         self,
-        request: pubsub.CreateSnapshotRequest = None,
+        request: Union[pubsub.CreateSnapshotRequest, dict] = None,
         *,
         name: str = None,
         subscription: str = None,
-        retry: retries.Retry = gapic_v1.method.DEFAULT,
+        retry: OptionalRetry = gapic_v1.method.DEFAULT,
         timeout: float = None,
         metadata: Sequence[Tuple[str, str]] = (),
     ) -> pubsub.Snapshot:
         r"""Creates a snapshot from the requested subscription. Snapshots
         are used in
         `Seek <https://cloud.google.com/pubsub/docs/replay-overview>`__
         operations, which allow you to manage message acknowledgments in
@@ -1336,15 +1341,15 @@
         the [resource name format]
         (https://cloud.google.com/pubsub/docs/admin#resource_names). The
         generated name is populated in the returned Snapshot object.
         Note that for REST API requests, you must specify a name in the
         request.
 
         Args:
-            request (:class:`google.pubsub_v1.types.CreateSnapshotRequest`):
+            request (Union[google.pubsub_v1.types.CreateSnapshotRequest, dict]):
                 The request object. Request for the `CreateSnapshot`
                 method.
             name (:class:`str`):
                 Required. User-provided name for this snapshot. If the
                 name is not provided in the request, the server will
                 assign a random name for this snapshot on the same
                 project as the subscription. Note that for REST API
@@ -1432,30 +1437,30 @@
         response = await rpc(request, retry=retry, timeout=timeout, metadata=metadata,)
 
         # Done; return the response.
         return response
 
     async def update_snapshot(
         self,
-        request: pubsub.UpdateSnapshotRequest = None,
+        request: Union[pubsub.UpdateSnapshotRequest, dict] = None,
         *,
-        retry: retries.Retry = gapic_v1.method.DEFAULT,
+        retry: OptionalRetry = gapic_v1.method.DEFAULT,
         timeout: float = None,
         metadata: Sequence[Tuple[str, str]] = (),
     ) -> pubsub.Snapshot:
         r"""Updates an existing snapshot. Snapshots are used in
         <a href="https://cloud.google.com/pubsub/docs/replay-
         overview">Seek</a> operations, which allow
         you to manage message acknowledgments in bulk. That is,
         you can set the acknowledgment state of messages in an
         existing subscription to the state captured by a
         snapshot.
 
         Args:
-            request (:class:`google.pubsub_v1.types.UpdateSnapshotRequest`):
+            request (Union[google.pubsub_v1.types.UpdateSnapshotRequest, dict]):
                 The request object. Request for the UpdateSnapshot
                 method.
             retry (google.api_core.retry.Retry): Designation of what errors, if any,
                 should be retried.
             timeout (float): The timeout for this request.
             metadata (Sequence[Tuple[str, str]]): Strings which should be
                 sent along with the request as metadata.
@@ -1502,18 +1507,18 @@
         response = await rpc(request, retry=retry, timeout=timeout, metadata=metadata,)
 
         # Done; return the response.
         return response
 
     async def delete_snapshot(
         self,
-        request: pubsub.DeleteSnapshotRequest = None,
+        request: Union[pubsub.DeleteSnapshotRequest, dict] = None,
         *,
         snapshot: str = None,
-        retry: retries.Retry = gapic_v1.method.DEFAULT,
+        retry: OptionalRetry = gapic_v1.method.DEFAULT,
         timeout: float = None,
         metadata: Sequence[Tuple[str, str]] = (),
     ) -> None:
         r"""Removes an existing snapshot. Snapshots are used in [Seek]
         (https://cloud.google.com/pubsub/docs/replay-overview)
         operations, which allow you to manage message acknowledgments in
         bulk. That is, you can set the acknowledgment state of messages
@@ -1521,15 +1526,15 @@
         When the snapshot is deleted, all messages retained in the
         snapshot are immediately dropped. After a snapshot is deleted, a
         new one may be created with the same name, but the new one has
         no association with the old snapshot or its subscription, unless
         the same subscription is specified.
 
         Args:
-            request (:class:`google.pubsub_v1.types.DeleteSnapshotRequest`):
+            request (Union[google.pubsub_v1.types.DeleteSnapshotRequest, dict]):
                 The request object. Request for the `DeleteSnapshot`
                 method.
             snapshot (:class:`str`):
                 Required. The name of the snapshot to delete. Format is
                 ``projects/{project}/snapshots/{snap}``.
 
                 This corresponds to the ``snapshot`` field
@@ -1584,32 +1589,32 @@
         # Send the request.
         await rpc(
             request, retry=retry, timeout=timeout, metadata=metadata,
         )
 
     async def seek(
         self,
-        request: pubsub.SeekRequest = None,
+        request: Union[pubsub.SeekRequest, dict] = None,
         *,
-        retry: retries.Retry = gapic_v1.method.DEFAULT,
+        retry: OptionalRetry = gapic_v1.method.DEFAULT,
         timeout: float = None,
         metadata: Sequence[Tuple[str, str]] = (),
     ) -> pubsub.SeekResponse:
         r"""Seeks an existing subscription to a point in time or to a given
         snapshot, whichever is provided in the request. Snapshots are
         used in [Seek]
         (https://cloud.google.com/pubsub/docs/replay-overview)
         operations, which allow you to manage message acknowledgments in
         bulk. That is, you can set the acknowledgment state of messages
         in an existing subscription to the state captured by a snapshot.
         Note that both the subscription and the snapshot must be on the
         same topic.
 
         Args:
-            request (:class:`google.pubsub_v1.types.SeekRequest`):
+            request (Union[google.pubsub_v1.types.SeekRequest, dict]):
                 The request object. Request for the `Seek` method.
             retry (google.api_core.retry.Retry): Designation of what errors, if any,
                 should be retried.
             timeout (float): The timeout for this request.
             metadata (Sequence[Tuple[str, str]]): Strings which should be
                 sent along with the request as metadata.
 
@@ -1653,15 +1658,15 @@
         # Done; return the response.
         return response
 
     async def set_iam_policy(
         self,
         request: iam_policy_pb2.SetIamPolicyRequest = None,
         *,
-        retry: retries.Retry = gapic_v1.method.DEFAULT,
+        retry: OptionalRetry = gapic_v1.method.DEFAULT,
         timeout: float = None,
         metadata: Sequence[Tuple[str, str]] = (),
     ) -> policy_pb2.Policy:
         r"""Sets the IAM access control policy on the specified function.
 
         Replaces any existing policy.
 
@@ -1761,15 +1766,15 @@
         # Done; return the response.
         return response
 
     async def get_iam_policy(
         self,
         request: iam_policy_pb2.GetIamPolicyRequest = None,
         *,
-        retry: retries.Retry = gapic_v1.method.DEFAULT,
+        retry: OptionalRetry = gapic_v1.method.DEFAULT,
         timeout: float = None,
         metadata: Sequence[Tuple[str, str]] = (),
     ) -> policy_pb2.Policy:
         r"""Gets the IAM access control policy for a function.
 
         Returns an empty policy if the function exists and does
         not have a policy set.
@@ -1870,15 +1875,15 @@
         # Done; return the response.
         return response
 
     async def test_iam_permissions(
         self,
         request: iam_policy_pb2.TestIamPermissionsRequest = None,
         *,
-        retry: retries.Retry = gapic_v1.method.DEFAULT,
+        retry: OptionalRetry = gapic_v1.method.DEFAULT,
         timeout: float = None,
         metadata: Sequence[Tuple[str, str]] = (),
     ) -> iam_policy_pb2.TestIamPermissionsResponse:
         r"""Tests the specified permissions against the IAM access control
             policy for a function.
 
         If the function does not exist, this will
@@ -1920,14 +1925,20 @@
 
         # Send the request.
         response = await rpc(request, retry=retry, timeout=timeout, metadata=metadata,)
 
         # Done; return the response.
         return response
 
+    async def __aenter__(self):
+        return self
+
+    async def __aexit__(self, exc_type, exc, tb):
+        await self.transport.close()
+
 
 try:
     DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
         client_library_version=pkg_resources.get_distribution(
             "google-cloud-pubsub",
         ).version,
     )
```

### Comparing `google-cloud-pubsub-2.8.0/google/pubsub_v1/services/subscriber/client.py` & `google-cloud-pubsub-2.9.0/google/pubsub_v1/services/subscriber/client.py`

 * *Files 3% similar despite different names*

```diff
@@ -10,42 +10,36 @@
 # Unless required by applicable law or agreed to in writing, software
 # distributed under the License is distributed on an "AS IS" BASIS,
 # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 # See the License for the specific language governing permissions and
 # limitations under the License.
 #
 from collections import OrderedDict
-from distutils import util
 import functools
 import os
 import re
-from typing import (
-    Callable,
-    Dict,
-    Optional,
-    Iterable,
-    Iterator,
-    Sequence,
-    Tuple,
-    Type,
-    Union,
-)
+from typing import Dict, Optional, Iterable, Iterator, Sequence, Tuple, Type, Union
 import warnings
 import pkg_resources
 
-from google.api_core import client_options as client_options_lib  # type: ignore
-from google.api_core import exceptions as core_exceptions  # type: ignore
-from google.api_core import gapic_v1  # type: ignore
-from google.api_core import retry as retries  # type: ignore
+from google.api_core import client_options as client_options_lib
+from google.api_core import exceptions as core_exceptions
+from google.api_core import gapic_v1
+from google.api_core import retry as retries
 from google.auth import credentials as ga_credentials  # type: ignore
 from google.auth.transport import mtls  # type: ignore
 from google.auth.transport.grpc import SslCredentials  # type: ignore
 from google.auth.exceptions import MutualTLSChannelError  # type: ignore
 from google.oauth2 import service_account  # type: ignore
 
+try:
+    OptionalRetry = Union[retries.Retry, gapic_v1.method._MethodDefault]
+except AttributeError:  # pragma: NO COVER
+    OptionalRetry = Union[retries.Retry, object]  # type: ignore
+
 from google.iam.v1 import iam_policy_pb2  # type: ignore
 from google.iam.v1 import policy_pb2  # type: ignore
 from google.protobuf import duration_pb2  # type: ignore
 from google.protobuf import timestamp_pb2  # type: ignore
 from google.pubsub_v1.services.subscriber import pagers
 from google.pubsub_v1.types import pubsub
 
@@ -335,16 +329,23 @@
         """
         if isinstance(client_options, dict):
             client_options = client_options_lib.from_dict(client_options)
         if client_options is None:
             client_options = client_options_lib.ClientOptions()
 
         # Create SSL credentials for mutual TLS if needed.
-        use_client_cert = bool(
-            util.strtobool(os.getenv("GOOGLE_API_USE_CLIENT_CERTIFICATE", "false"))
+        if os.getenv("GOOGLE_API_USE_CLIENT_CERTIFICATE", "false") not in (
+            "true",
+            "false",
+        ):
+            raise ValueError(
+                "Environment variable `GOOGLE_API_USE_CLIENT_CERTIFICATE` must be either `true` or `false`"
+            )
+        use_client_cert = (
+            os.getenv("GOOGLE_API_USE_CLIENT_CERTIFICATE", "false") == "true"
         )
 
         client_cert_source_func = None
         is_mtls = False
         if use_client_cert:
             if client_options.client_cert_source:
                 is_mtls = True
@@ -407,29 +408,26 @@
                 credentials=credentials,
                 credentials_file=client_options.credentials_file,
                 host=api_endpoint,
                 scopes=client_options.scopes,
                 client_cert_source_for_mtls=client_cert_source_func,
                 quota_project_id=client_options.quota_project_id,
                 client_info=client_info,
-                always_use_jwt_access=(
-                    Transport == type(self).get_transport_class("grpc")
-                    or Transport == type(self).get_transport_class("grpc_asyncio")
-                ),
+                always_use_jwt_access=True,
             )
 
     def create_subscription(
         self,
-        request: pubsub.Subscription = None,
+        request: Union[pubsub.Subscription, dict] = None,
         *,
         name: str = None,
         topic: str = None,
         push_config: pubsub.PushConfig = None,
         ack_deadline_seconds: int = None,
-        retry: retries.Retry = gapic_v1.method.DEFAULT,
+        retry: OptionalRetry = gapic_v1.method.DEFAULT,
         timeout: float = None,
         metadata: Sequence[Tuple[str, str]] = (),
     ) -> pubsub.Subscription:
         r"""Creates a subscription to a given topic. See the [resource name
         rules]
         (https://cloud.google.com/pubsub/docs/admin#resource_names). If
         the subscription already exists, returns ``ALREADY_EXISTS``. If
@@ -441,15 +439,15 @@
         (https://cloud.google.com/pubsub/docs/admin#resource_names). The
         generated name is populated in the returned Subscription object.
         Note that for REST API requests, you must specify a name in the
         request.
 
 
         Args:
-            request (google.pubsub_v1.types.Subscription):
+            request (Union[google.pubsub_v1.types.Subscription, dict]):
                 The request object. A subscription resource.
             name (str):
                 Required. The name of the subscription. It must have the
                 format
                 ``"projects/{project}/subscriptions/{subscription}"``.
                 ``{subscription}`` must start with a letter, and contain
                 only letters (``[A-Za-z]``), numbers (``[0-9]``), dashes
@@ -560,26 +558,26 @@
         response = rpc(request, retry=retry, timeout=timeout, metadata=metadata,)
 
         # Done; return the response.
         return response
 
     def get_subscription(
         self,
-        request: pubsub.GetSubscriptionRequest = None,
+        request: Union[pubsub.GetSubscriptionRequest, dict] = None,
         *,
         subscription: str = None,
-        retry: retries.Retry = gapic_v1.method.DEFAULT,
+        retry: OptionalRetry = gapic_v1.method.DEFAULT,
         timeout: float = None,
         metadata: Sequence[Tuple[str, str]] = (),
     ) -> pubsub.Subscription:
         r"""Gets the configuration details of a subscription.
 
 
         Args:
-            request (google.pubsub_v1.types.GetSubscriptionRequest):
+            request (Union[google.pubsub_v1.types.GetSubscriptionRequest, dict]):
                 The request object. Request for the GetSubscription
                 method.
             subscription (str):
                 Required. The name of the subscription to get. Format is
                 ``projects/{project}/subscriptions/{sub}``.
 
                 This corresponds to the ``subscription`` field
@@ -632,27 +630,27 @@
         response = rpc(request, retry=retry, timeout=timeout, metadata=metadata,)
 
         # Done; return the response.
         return response
 
     def update_subscription(
         self,
-        request: pubsub.UpdateSubscriptionRequest = None,
+        request: Union[pubsub.UpdateSubscriptionRequest, dict] = None,
         *,
-        retry: retries.Retry = gapic_v1.method.DEFAULT,
+        retry: OptionalRetry = gapic_v1.method.DEFAULT,
         timeout: float = None,
         metadata: Sequence[Tuple[str, str]] = (),
     ) -> pubsub.Subscription:
         r"""Updates an existing subscription. Note that certain
         properties of a subscription, such as its topic, are not
         modifiable.
 
 
         Args:
-            request (google.pubsub_v1.types.UpdateSubscriptionRequest):
+            request (Union[google.pubsub_v1.types.UpdateSubscriptionRequest, dict]):
                 The request object. Request for the UpdateSubscription
                 method.
             retry (google.api_core.retry.Retry): Designation of what errors, if any,
                 should be retried.
             timeout (float): The timeout for this request.
             metadata (Sequence[Tuple[str, str]]): Strings which should be
                 sent along with the request as metadata.
@@ -685,26 +683,26 @@
         response = rpc(request, retry=retry, timeout=timeout, metadata=metadata,)
 
         # Done; return the response.
         return response
 
     def list_subscriptions(
         self,
-        request: pubsub.ListSubscriptionsRequest = None,
+        request: Union[pubsub.ListSubscriptionsRequest, dict] = None,
         *,
         project: str = None,
-        retry: retries.Retry = gapic_v1.method.DEFAULT,
+        retry: OptionalRetry = gapic_v1.method.DEFAULT,
         timeout: float = None,
         metadata: Sequence[Tuple[str, str]] = (),
     ) -> pagers.ListSubscriptionsPager:
         r"""Lists matching subscriptions.
 
 
         Args:
-            request (google.pubsub_v1.types.ListSubscriptionsRequest):
+            request (Union[google.pubsub_v1.types.ListSubscriptionsRequest, dict]):
                 The request object. Request for the `ListSubscriptions`
                 method.
             project (str):
                 Required. The name of the project in which to list
                 subscriptions. Format is ``projects/{project-id}``.
 
                 This corresponds to the ``project`` field
@@ -765,31 +763,31 @@
         )
 
         # Done; return the response.
         return response
 
     def delete_subscription(
         self,
-        request: pubsub.DeleteSubscriptionRequest = None,
+        request: Union[pubsub.DeleteSubscriptionRequest, dict] = None,
         *,
         subscription: str = None,
-        retry: retries.Retry = gapic_v1.method.DEFAULT,
+        retry: OptionalRetry = gapic_v1.method.DEFAULT,
         timeout: float = None,
         metadata: Sequence[Tuple[str, str]] = (),
     ) -> None:
         r"""Deletes an existing subscription. All messages retained in the
         subscription are immediately dropped. Calls to ``Pull`` after
         deletion will return ``NOT_FOUND``. After a subscription is
         deleted, a new one may be created with the same name, but the
         new one has no association with the old subscription or its
         topic unless the same topic is specified.
 
 
         Args:
-            request (google.pubsub_v1.types.DeleteSubscriptionRequest):
+            request (Union[google.pubsub_v1.types.DeleteSubscriptionRequest, dict]):
                 The request object. Request for the DeleteSubscription
                 method.
             subscription (str):
                 Required. The subscription to delete. Format is
                 ``projects/{project}/subscriptions/{sub}``.
 
                 This corresponds to the ``subscription`` field
@@ -837,33 +835,33 @@
         # Send the request.
         rpc(
             request, retry=retry, timeout=timeout, metadata=metadata,
         )
 
     def modify_ack_deadline(
         self,
-        request: pubsub.ModifyAckDeadlineRequest = None,
+        request: Union[pubsub.ModifyAckDeadlineRequest, dict] = None,
         *,
         subscription: str = None,
         ack_ids: Sequence[str] = None,
         ack_deadline_seconds: int = None,
-        retry: retries.Retry = gapic_v1.method.DEFAULT,
+        retry: OptionalRetry = gapic_v1.method.DEFAULT,
         timeout: float = None,
         metadata: Sequence[Tuple[str, str]] = (),
     ) -> None:
         r"""Modifies the ack deadline for a specific message. This method is
         useful to indicate that more time is needed to process a message
         by the subscriber, or to make the message available for
         redelivery if the processing was interrupted. Note that this
         does not modify the subscription-level ``ackDeadlineSeconds``
         used for subsequent messages.
 
 
         Args:
-            request (google.pubsub_v1.types.ModifyAckDeadlineRequest):
+            request (Union[google.pubsub_v1.types.ModifyAckDeadlineRequest, dict]):
                 The request object. Request for the ModifyAckDeadline
                 method.
             subscription (str):
                 Required. The name of the subscription. Format is
                 ``projects/{project}/subscriptions/{sub}``.
 
                 This corresponds to the ``subscription`` field
@@ -936,34 +934,34 @@
         # Send the request.
         rpc(
             request, retry=retry, timeout=timeout, metadata=metadata,
         )
 
     def acknowledge(
         self,
-        request: pubsub.AcknowledgeRequest = None,
+        request: Union[pubsub.AcknowledgeRequest, dict] = None,
         *,
         subscription: str = None,
         ack_ids: Sequence[str] = None,
-        retry: retries.Retry = gapic_v1.method.DEFAULT,
+        retry: OptionalRetry = gapic_v1.method.DEFAULT,
         timeout: float = None,
         metadata: Sequence[Tuple[str, str]] = (),
     ) -> None:
         r"""Acknowledges the messages associated with the ``ack_ids`` in the
         ``AcknowledgeRequest``. The Pub/Sub system can remove the
         relevant messages from the subscription.
 
         Acknowledging a message whose ack deadline has expired may
         succeed, but such a message may be redelivered later.
         Acknowledging a message more than once will not result in an
         error.
 
 
         Args:
-            request (google.pubsub_v1.types.AcknowledgeRequest):
+            request (Union[google.pubsub_v1.types.AcknowledgeRequest, dict]):
                 The request object. Request for the Acknowledge method.
             subscription (str):
                 Required. The subscription whose message is being
                 acknowledged. Format is
                 ``projects/{project}/subscriptions/{sub}``.
 
                 This corresponds to the ``subscription`` field
@@ -1021,30 +1019,30 @@
         # Send the request.
         rpc(
             request, retry=retry, timeout=timeout, metadata=metadata,
         )
 
     def pull(
         self,
-        request: pubsub.PullRequest = None,
+        request: Union[pubsub.PullRequest, dict] = None,
         *,
         subscription: str = None,
         return_immediately: bool = None,
         max_messages: int = None,
-        retry: retries.Retry = gapic_v1.method.DEFAULT,
+        retry: OptionalRetry = gapic_v1.method.DEFAULT,
         timeout: float = None,
         metadata: Sequence[Tuple[str, str]] = (),
     ) -> pubsub.PullResponse:
         r"""Pulls messages from the server. The server may return
         ``UNAVAILABLE`` if there are too many concurrent pull requests
         pending for the given subscription.
 
 
         Args:
-            request (google.pubsub_v1.types.PullRequest):
+            request (Union[google.pubsub_v1.types.PullRequest, dict]):
                 The request object. Request for the `Pull` method.
             subscription (str):
                 Required. The subscription from which messages should be
                 pulled. Format is
                 ``projects/{project}/subscriptions/{sub}``.
 
                 This corresponds to the ``subscription`` field
@@ -1133,15 +1131,15 @@
         # Done; return the response.
         return response
 
     def streaming_pull(
         self,
         requests: Iterator[pubsub.StreamingPullRequest] = None,
         *,
-        retry: retries.Retry = gapic_v1.method.DEFAULT,
+        retry: OptionalRetry = gapic_v1.method.DEFAULT,
         timeout: float = None,
         metadata: Sequence[Tuple[str, str]] = (),
     ) -> Iterable[pubsub.StreamingPullResponse]:
         r"""Establishes a stream with the server, which sends messages down
         to the client. The client streams acknowledgements and ack
         deadline modifications back to the server. The server will close
         the stream and return the status on any error. The server may
@@ -1184,33 +1182,33 @@
         response = rpc(requests, retry=retry, timeout=timeout, metadata=metadata,)
 
         # Done; return the response.
         return response
 
     def modify_push_config(
         self,
-        request: pubsub.ModifyPushConfigRequest = None,
+        request: Union[pubsub.ModifyPushConfigRequest, dict] = None,
         *,
         subscription: str = None,
         push_config: pubsub.PushConfig = None,
-        retry: retries.Retry = gapic_v1.method.DEFAULT,
+        retry: OptionalRetry = gapic_v1.method.DEFAULT,
         timeout: float = None,
         metadata: Sequence[Tuple[str, str]] = (),
     ) -> None:
         r"""Modifies the ``PushConfig`` for a specified subscription.
 
         This may be used to change a push subscription to a pull one
         (signified by an empty ``PushConfig``) or vice versa, or change
         the endpoint URL and other attributes of a push subscription.
         Messages will accumulate for delivery continuously through the
         call regardless of changes to the ``PushConfig``.
 
 
         Args:
-            request (google.pubsub_v1.types.ModifyPushConfigRequest):
+            request (Union[google.pubsub_v1.types.ModifyPushConfigRequest, dict]):
                 The request object. Request for the ModifyPushConfig
                 method.
             subscription (str):
                 Required. The name of the subscription. Format is
                 ``projects/{project}/subscriptions/{sub}``.
 
                 This corresponds to the ``subscription`` field
@@ -1272,32 +1270,32 @@
         # Send the request.
         rpc(
             request, retry=retry, timeout=timeout, metadata=metadata,
         )
 
     def get_snapshot(
         self,
-        request: pubsub.GetSnapshotRequest = None,
+        request: Union[pubsub.GetSnapshotRequest, dict] = None,
         *,
         snapshot: str = None,
-        retry: retries.Retry = gapic_v1.method.DEFAULT,
+        retry: OptionalRetry = gapic_v1.method.DEFAULT,
         timeout: float = None,
         metadata: Sequence[Tuple[str, str]] = (),
     ) -> pubsub.Snapshot:
         r"""Gets the configuration details of a snapshot.
         Snapshots are used in <a
         href="https://cloud.google.com/pubsub/docs/replay-
         overview">Seek</a> operations, which allow you to manage
         message acknowledgments in bulk. That is, you can set
         the acknowledgment state of messages in an existing
         subscription to the state captured by a snapshot.
 
 
         Args:
-            request (google.pubsub_v1.types.GetSnapshotRequest):
+            request (Union[google.pubsub_v1.types.GetSnapshotRequest, dict]):
                 The request object. Request for the GetSnapshot method.
             snapshot (str):
                 Required. The name of the snapshot to get. Format is
                 ``projects/{project}/snapshots/{snap}``.
 
                 This corresponds to the ``snapshot`` field
                 on the ``request`` instance; if ``request`` is provided, this
@@ -1353,30 +1351,30 @@
         response = rpc(request, retry=retry, timeout=timeout, metadata=metadata,)
 
         # Done; return the response.
         return response
 
     def list_snapshots(
         self,
-        request: pubsub.ListSnapshotsRequest = None,
+        request: Union[pubsub.ListSnapshotsRequest, dict] = None,
         *,
         project: str = None,
-        retry: retries.Retry = gapic_v1.method.DEFAULT,
+        retry: OptionalRetry = gapic_v1.method.DEFAULT,
         timeout: float = None,
         metadata: Sequence[Tuple[str, str]] = (),
     ) -> pagers.ListSnapshotsPager:
         r"""Lists the existing snapshots. Snapshots are used in
         `Seek <https://cloud.google.com/pubsub/docs/replay-overview>`__
         operations, which allow you to manage message acknowledgments in
         bulk. That is, you can set the acknowledgment state of messages
         in an existing subscription to the state captured by a snapshot.
 
 
         Args:
-            request (google.pubsub_v1.types.ListSnapshotsRequest):
+            request (Union[google.pubsub_v1.types.ListSnapshotsRequest, dict]):
                 The request object. Request for the `ListSnapshots`
                 method.
             project (str):
                 Required. The name of the project in which to list
                 snapshots. Format is ``projects/{project-id}``.
 
                 This corresponds to the ``project`` field
@@ -1437,19 +1435,19 @@
         )
 
         # Done; return the response.
         return response
 
     def create_snapshot(
         self,
-        request: pubsub.CreateSnapshotRequest = None,
+        request: Union[pubsub.CreateSnapshotRequest, dict] = None,
         *,
         name: str = None,
         subscription: str = None,
-        retry: retries.Retry = gapic_v1.method.DEFAULT,
+        retry: OptionalRetry = gapic_v1.method.DEFAULT,
         timeout: float = None,
         metadata: Sequence[Tuple[str, str]] = (),
     ) -> pubsub.Snapshot:
         r"""Creates a snapshot from the requested subscription. Snapshots
         are used in
         `Seek <https://cloud.google.com/pubsub/docs/replay-overview>`__
         operations, which allow you to manage message acknowledgments in
@@ -1467,15 +1465,15 @@
         (https://cloud.google.com/pubsub/docs/admin#resource_names). The
         generated name is populated in the returned Snapshot object.
         Note that for REST API requests, you must specify a name in the
         request.
 
 
         Args:
-            request (google.pubsub_v1.types.CreateSnapshotRequest):
+            request (Union[google.pubsub_v1.types.CreateSnapshotRequest, dict]):
                 The request object. Request for the `CreateSnapshot`
                 method.
             name (str):
                 Required. User-provided name for this snapshot. If the
                 name is not provided in the request, the server will
                 assign a random name for this snapshot on the same
                 project as the subscription. Note that for REST API
@@ -1554,31 +1552,31 @@
         response = rpc(request, retry=retry, timeout=timeout, metadata=metadata,)
 
         # Done; return the response.
         return response
 
     def update_snapshot(
         self,
-        request: pubsub.UpdateSnapshotRequest = None,
+        request: Union[pubsub.UpdateSnapshotRequest, dict] = None,
         *,
-        retry: retries.Retry = gapic_v1.method.DEFAULT,
+        retry: OptionalRetry = gapic_v1.method.DEFAULT,
         timeout: float = None,
         metadata: Sequence[Tuple[str, str]] = (),
     ) -> pubsub.Snapshot:
         r"""Updates an existing snapshot. Snapshots are used in
         <a href="https://cloud.google.com/pubsub/docs/replay-
         overview">Seek</a> operations, which allow
         you to manage message acknowledgments in bulk. That is,
         you can set the acknowledgment state of messages in an
         existing subscription to the state captured by a
         snapshot.
 
 
         Args:
-            request (google.pubsub_v1.types.UpdateSnapshotRequest):
+            request (Union[google.pubsub_v1.types.UpdateSnapshotRequest, dict]):
                 The request object. Request for the UpdateSnapshot
                 method.
             retry (google.api_core.retry.Retry): Designation of what errors, if any,
                 should be retried.
             timeout (float): The timeout for this request.
             metadata (Sequence[Tuple[str, str]]): Strings which should be
                 sent along with the request as metadata.
@@ -1617,18 +1615,18 @@
         response = rpc(request, retry=retry, timeout=timeout, metadata=metadata,)
 
         # Done; return the response.
         return response
 
     def delete_snapshot(
         self,
-        request: pubsub.DeleteSnapshotRequest = None,
+        request: Union[pubsub.DeleteSnapshotRequest, dict] = None,
         *,
         snapshot: str = None,
-        retry: retries.Retry = gapic_v1.method.DEFAULT,
+        retry: OptionalRetry = gapic_v1.method.DEFAULT,
         timeout: float = None,
         metadata: Sequence[Tuple[str, str]] = (),
     ) -> None:
         r"""Removes an existing snapshot. Snapshots are used in [Seek]
         (https://cloud.google.com/pubsub/docs/replay-overview)
         operations, which allow you to manage message acknowledgments in
         bulk. That is, you can set the acknowledgment state of messages
@@ -1637,15 +1635,15 @@
         snapshot are immediately dropped. After a snapshot is deleted, a
         new one may be created with the same name, but the new one has
         no association with the old snapshot or its subscription, unless
         the same subscription is specified.
 
 
         Args:
-            request (google.pubsub_v1.types.DeleteSnapshotRequest):
+            request (Union[google.pubsub_v1.types.DeleteSnapshotRequest, dict]):
                 The request object. Request for the `DeleteSnapshot`
                 method.
             snapshot (str):
                 Required. The name of the snapshot to delete. Format is
                 ``projects/{project}/snapshots/{snap}``.
 
                 This corresponds to the ``snapshot`` field
@@ -1691,17 +1689,17 @@
         # Send the request.
         rpc(
             request, retry=retry, timeout=timeout, metadata=metadata,
         )
 
     def seek(
         self,
-        request: pubsub.SeekRequest = None,
+        request: Union[pubsub.SeekRequest, dict] = None,
         *,
-        retry: retries.Retry = gapic_v1.method.DEFAULT,
+        retry: OptionalRetry = gapic_v1.method.DEFAULT,
         timeout: float = None,
         metadata: Sequence[Tuple[str, str]] = (),
     ) -> pubsub.SeekResponse:
         r"""Seeks an existing subscription to a point in time or to a given
         snapshot, whichever is provided in the request. Snapshots are
         used in [Seek]
         (https://cloud.google.com/pubsub/docs/replay-overview)
@@ -1709,15 +1707,15 @@
         bulk. That is, you can set the acknowledgment state of messages
         in an existing subscription to the state captured by a snapshot.
         Note that both the subscription and the snapshot must be on the
         same topic.
 
 
         Args:
-            request (google.pubsub_v1.types.SeekRequest):
+            request (Union[google.pubsub_v1.types.SeekRequest, dict]):
                 The request object. Request for the `Seek` method.
             retry (google.api_core.retry.Retry): Designation of what errors, if any,
                 should be retried.
             timeout (float): The timeout for this request.
             metadata (Sequence[Tuple[str, str]]): Strings which should be
                 sent along with the request as metadata.
 
@@ -1747,19 +1745,32 @@
 
         # Send the request.
         response = rpc(request, retry=retry, timeout=timeout, metadata=metadata,)
 
         # Done; return the response.
         return response
 
+    def __enter__(self):
+        return self
+
+    def __exit__(self, type, value, traceback):
+        """Releases underlying transport's resources.
+
+        .. warning::
+            ONLY use as a context manager if the transport is NOT shared
+            with other clients! Exiting the with block will CLOSE the transport
+            and may cause errors in other clients!
+        """
+        self.transport.close()
+
     def set_iam_policy(
         self,
         request: iam_policy_pb2.SetIamPolicyRequest = None,
         *,
-        retry: retries.Retry = gapic_v1.method.DEFAULT,
+        retry: OptionalRetry = gapic_v1.method.DEFAULT,
         timeout: float = None,
         metadata: Sequence[Tuple[str, str]] = (),
     ) -> policy_pb2.Policy:
         r"""Sets the IAM access control policy on the specified function.
 
         Replaces any existing policy.
 
@@ -1863,15 +1874,15 @@
         # Done; return the response.
         return response
 
     def get_iam_policy(
         self,
         request: iam_policy_pb2.GetIamPolicyRequest = None,
         *,
-        retry: retries.Retry = gapic_v1.method.DEFAULT,
+        retry: OptionalRetry = gapic_v1.method.DEFAULT,
         timeout: float = None,
         metadata: Sequence[Tuple[str, str]] = (),
     ) -> policy_pb2.Policy:
         r"""Gets the IAM access control policy for a function.
 
         Returns an empty policy if the function exists and does not have a
         policy set.
@@ -1976,15 +1987,15 @@
         # Done; return the response.
         return response
 
     def test_iam_permissions(
         self,
         request: iam_policy_pb2.TestIamPermissionsRequest = None,
         *,
-        retry: retries.Retry = gapic_v1.method.DEFAULT,
+        retry: OptionalRetry = gapic_v1.method.DEFAULT,
         timeout: float = None,
         metadata: Sequence[Tuple[str, str]] = (),
     ) -> iam_policy_pb2.TestIamPermissionsResponse:
         r"""Tests the specified IAM permissions against the IAM access control
             policy for a function.
 
         If the function does not exist, this will return an empty set
```

### Comparing `google-cloud-pubsub-2.8.0/google/pubsub_v1/services/subscriber/pagers.py` & `google-cloud-pubsub-2.9.0/google/pubsub_v1/services/subscriber/pagers.py`

 * *Files 4% similar despite different names*

```diff
@@ -11,21 +11,21 @@
 # distributed under the License is distributed on an "AS IS" BASIS,
 # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 # See the License for the specific language governing permissions and
 # limitations under the License.
 #
 from typing import (
     Any,
-    AsyncIterable,
+    AsyncIterator,
     Awaitable,
     Callable,
-    Iterable,
     Sequence,
     Tuple,
     Optional,
+    Iterator,
 )
 
 from google.pubsub_v1.types import pubsub
 
 
 class ListSubscriptionsPager:
     """A pager for iterating through ``list_subscriptions`` requests.
@@ -70,22 +70,22 @@
         self._response = response
         self._metadata = metadata
 
     def __getattr__(self, name: str) -> Any:
         return getattr(self._response, name)
 
     @property
-    def pages(self) -> Iterable[pubsub.ListSubscriptionsResponse]:
+    def pages(self) -> Iterator[pubsub.ListSubscriptionsResponse]:
         yield self._response
         while self._response.next_page_token:
             self._request.page_token = self._response.next_page_token
             self._response = self._method(self._request, metadata=self._metadata)
             yield self._response
 
-    def __iter__(self) -> Iterable[pubsub.Subscription]:
+    def __iter__(self) -> Iterator[pubsub.Subscription]:
         for page in self.pages:
             yield from page.subscriptions
 
     def __repr__(self) -> str:
         return "{0}<{1!r}>".format(self.__class__.__name__, self._response)
 
 
@@ -132,22 +132,22 @@
         self._response = response
         self._metadata = metadata
 
     def __getattr__(self, name: str) -> Any:
         return getattr(self._response, name)
 
     @property
-    async def pages(self) -> AsyncIterable[pubsub.ListSubscriptionsResponse]:
+    async def pages(self) -> AsyncIterator[pubsub.ListSubscriptionsResponse]:
         yield self._response
         while self._response.next_page_token:
             self._request.page_token = self._response.next_page_token
             self._response = await self._method(self._request, metadata=self._metadata)
             yield self._response
 
-    def __aiter__(self) -> AsyncIterable[pubsub.Subscription]:
+    def __aiter__(self) -> AsyncIterator[pubsub.Subscription]:
         async def async_generator():
             async for page in self.pages:
                 for response in page.subscriptions:
                     yield response
 
         return async_generator()
 
@@ -198,22 +198,22 @@
         self._response = response
         self._metadata = metadata
 
     def __getattr__(self, name: str) -> Any:
         return getattr(self._response, name)
 
     @property
-    def pages(self) -> Iterable[pubsub.ListSnapshotsResponse]:
+    def pages(self) -> Iterator[pubsub.ListSnapshotsResponse]:
         yield self._response
         while self._response.next_page_token:
             self._request.page_token = self._response.next_page_token
             self._response = self._method(self._request, metadata=self._metadata)
             yield self._response
 
-    def __iter__(self) -> Iterable[pubsub.Snapshot]:
+    def __iter__(self) -> Iterator[pubsub.Snapshot]:
         for page in self.pages:
             yield from page.snapshots
 
     def __repr__(self) -> str:
         return "{0}<{1!r}>".format(self.__class__.__name__, self._response)
 
 
@@ -260,22 +260,22 @@
         self._response = response
         self._metadata = metadata
 
     def __getattr__(self, name: str) -> Any:
         return getattr(self._response, name)
 
     @property
-    async def pages(self) -> AsyncIterable[pubsub.ListSnapshotsResponse]:
+    async def pages(self) -> AsyncIterator[pubsub.ListSnapshotsResponse]:
         yield self._response
         while self._response.next_page_token:
             self._request.page_token = self._response.next_page_token
             self._response = await self._method(self._request, metadata=self._metadata)
             yield self._response
 
-    def __aiter__(self) -> AsyncIterable[pubsub.Snapshot]:
+    def __aiter__(self) -> AsyncIterator[pubsub.Snapshot]:
         async def async_generator():
             async for page in self.pages:
                 for response in page.snapshots:
                     yield response
 
         return async_generator()
```

### Comparing `google-cloud-pubsub-2.8.0/google/pubsub_v1/services/subscriber/transports/__init__.py` & `google-cloud-pubsub-2.9.0/google/pubsub_v1/services/subscriber/transports/__init__.py`

 * *Files identical despite different names*

### Comparing `google-cloud-pubsub-2.8.0/google/pubsub_v1/services/subscriber/transports/base.py` & `google-cloud-pubsub-2.9.0/google/pubsub_v1/services/subscriber/transports/base.py`

 * *Files 3% similar despite different names*

```diff
@@ -11,22 +11,21 @@
 # distributed under the License is distributed on an "AS IS" BASIS,
 # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 # See the License for the specific language governing permissions and
 # limitations under the License.
 #
 import abc
 from typing import Awaitable, Callable, Dict, Optional, Sequence, Union
-import packaging.version
 import pkg_resources
 
 import google.auth  # type: ignore
-import google.api_core  # type: ignore
-from google.api_core import exceptions as core_exceptions  # type: ignore
-from google.api_core import gapic_v1  # type: ignore
-from google.api_core import retry as retries  # type: ignore
+import google.api_core
+from google.api_core import exceptions as core_exceptions
+from google.api_core import gapic_v1
+from google.api_core import retry as retries
 from google.auth import credentials as ga_credentials  # type: ignore
 from google.oauth2 import service_account  # type: ignore
 
 from google.iam.v1 import iam_policy_pb2  # type: ignore
 from google.iam.v1 import policy_pb2  # type: ignore
 from google.protobuf import empty_pb2  # type: ignore
 from google.pubsub_v1.types import pubsub
@@ -36,23 +35,14 @@
         client_library_version=pkg_resources.get_distribution(
             "google-cloud-pubsub",
         ).version,
     )
 except pkg_resources.DistributionNotFound:
     DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo()
 
-try:
-    # google.auth.__version__ was added in 1.26.0
-    _GOOGLE_AUTH_VERSION = google.auth.__version__
-except AttributeError:
-    try:  # try pkg_resources if it is available
-        _GOOGLE_AUTH_VERSION = pkg_resources.get_distribution("google-auth").version
-    except pkg_resources.DistributionNotFound:  # pragma: NO COVER
-        _GOOGLE_AUTH_VERSION = None
-
 
 class SubscriberTransport(abc.ABC):
     """Abstract transport class for Subscriber."""
 
     AUTH_SCOPES = (
         "https://www.googleapis.com/auth/cloud-platform",
         "https://www.googleapis.com/auth/pubsub",
@@ -97,15 +87,15 @@
                 be used for service account credentials.
         """
         # Save the hostname. Default to port 443 (HTTPS) if none is specified.
         if ":" not in host:
             host += ":443"
         self._host = host
 
-        scopes_kwargs = self._get_scopes_kwargs(self._host, scopes)
+        scopes_kwargs = {"scopes": scopes, "default_scopes": self.AUTH_SCOPES}
 
         # Save the scopes.
         self._scopes = scopes
 
         # If no credentials are provided, then determine the appropriate
         # defaults.
         if credentials and credentials_file:
@@ -119,48 +109,25 @@
             )
 
         elif credentials is None:
             credentials, _ = google.auth.default(
                 **scopes_kwargs, quota_project_id=quota_project_id
             )
 
-        # If the credentials is service account credentials, then always try to use self signed JWT.
+        # If the credentials are service account credentials, then always try to use self signed JWT.
         if (
             always_use_jwt_access
             and isinstance(credentials, service_account.Credentials)
             and hasattr(service_account.Credentials, "with_always_use_jwt_access")
         ):
             credentials = credentials.with_always_use_jwt_access(True)
 
         # Save the credentials.
         self._credentials = credentials
 
-    # TODO(busunkim): This method is in the base transport
-    # to avoid duplicating code across the transport classes. These functions
-    # should be deleted once the minimum required versions of google-auth is increased.
-
-    # TODO: Remove this function once google-auth >= 1.25.0 is required
-    @classmethod
-    def _get_scopes_kwargs(
-        cls, host: str, scopes: Optional[Sequence[str]]
-    ) -> Dict[str, Optional[Sequence[str]]]:
-        """Returns scopes kwargs to pass to google-auth methods depending on the google-auth version"""
-
-        scopes_kwargs = {}
-
-        if _GOOGLE_AUTH_VERSION and (
-            packaging.version.parse(_GOOGLE_AUTH_VERSION)
-            >= packaging.version.parse("1.25.0")
-        ):
-            scopes_kwargs = {"scopes": scopes, "default_scopes": cls.AUTH_SCOPES}
-        else:
-            scopes_kwargs = {"scopes": scopes or cls.AUTH_SCOPES}
-
-        return scopes_kwargs
-
     def _prep_wrapped_messages(self, client_info):
         # Precompute the wrapped methods.
         self._wrapped_methods = {
             self.create_subscription: gapic_v1.method.wrap_method(
                 self.create_subscription,
                 default_retry=retries.Retry(
                     initial=0.1,
@@ -400,14 +367,23 @@
                     deadline=60.0,
                 ),
                 default_timeout=60.0,
                 client_info=client_info,
             ),
         }
 
+    def close(self):
+        """Closes resources associated with the transport.
+
+       .. warning::
+            Only call this method if the transport is NOT shared
+            with other clients - this may cause errors in other clients!
+        """
+        raise NotImplementedError()
+
     @property
     def create_subscription(
         self,
     ) -> Callable[
         [pubsub.Subscription],
         Union[pubsub.Subscription, Awaitable[pubsub.Subscription]],
     ]:
```

### Comparing `google-cloud-pubsub-2.8.0/google/pubsub_v1/services/subscriber/transports/grpc.py` & `google-cloud-pubsub-2.9.0/google/pubsub_v1/services/subscriber/transports/grpc.py`

 * *Files 1% similar despite different names*

```diff
@@ -12,16 +12,16 @@
 # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 # See the License for the specific language governing permissions and
 # limitations under the License.
 #
 import warnings
 from typing import Callable, Dict, Optional, Sequence, Tuple, Union
 
-from google.api_core import grpc_helpers  # type: ignore
-from google.api_core import gapic_v1  # type: ignore
+from google.api_core import grpc_helpers
+from google.api_core import gapic_v1
 import google.auth  # type: ignore
 from google.auth import credentials as ga_credentials  # type: ignore
 from google.auth.transport.grpc import SslCredentials  # type: ignore
 
 import grpc  # type: ignore
 
 from google.iam.v1 import iam_policy_pb2  # type: ignore
@@ -82,24 +82,24 @@
             scopes (Optional(Sequence[str])): A list of scopes. This argument is
                 ignored if ``channel`` is provided.
             channel (Optional[grpc.Channel]): A ``Channel`` instance through
                 which to make calls.
             api_mtls_endpoint (Optional[str]): Deprecated. The mutual TLS endpoint.
                 If provided, it overrides the ``host`` argument and tries to create
                 a mutual TLS channel with client SSL credentials from
-                ``client_cert_source`` or applicatin default SSL credentials.
+                ``client_cert_source`` or application default SSL credentials.
             client_cert_source (Optional[Callable[[], Tuple[bytes, bytes]]]):
                 Deprecated. A callback to provide client SSL certificate bytes and
                 private key bytes, both in PEM format. It is ignored if
                 ``api_mtls_endpoint`` is None.
             ssl_channel_credentials (grpc.ChannelCredentials): SSL credentials
-                for grpc channel. It is ignored if ``channel`` is provided.
+                for the grpc channel. It is ignored if ``channel`` is provided.
             client_cert_source_for_mtls (Optional[Callable[[], Tuple[bytes, bytes]]]):
                 A callback to provide client certificate bytes and private key bytes,
-                both in PEM format. It is used to configure mutual TLS channel. It is
+                both in PEM format. It is used to configure a mutual TLS channel. It is
                 ignored if ``channel`` or ``ssl_channel_credentials`` is provided.
             quota_project_id (Optional[str]): An optional project to use for billing
                 and quota.
             client_info (google.api_core.gapic_v1.client_info.ClientInfo):
                 The client info used to send a user-agent string along with
                 API requests. If ``None``, then default info will be used.
                 Generally, you only need to set this if you're developing
@@ -813,9 +813,12 @@
             self._stubs["test_iam_permissions"] = self.grpc_channel.unary_unary(
                 "/google.iam.v1.IAMPolicy/TestIamPermissions",
                 request_serializer=iam_policy_pb2.TestIamPermissionsRequest.SerializeToString,
                 response_deserializer=iam_policy_pb2.TestIamPermissionsResponse.FromString,
             )
         return self._stubs["test_iam_permissions"]
 
+    def close(self):
+        self.grpc_channel.close()
+
 
 __all__ = ("SubscriberGrpcTransport",)
```

### Comparing `google-cloud-pubsub-2.8.0/google/pubsub_v1/services/subscriber/transports/grpc_asyncio.py` & `google-cloud-pubsub-2.9.0/google/pubsub_v1/services/subscriber/transports/grpc_asyncio.py`

 * *Files 0% similar despite different names*

```diff
@@ -12,19 +12,18 @@
 # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 # See the License for the specific language governing permissions and
 # limitations under the License.
 #
 import warnings
 from typing import Awaitable, Callable, Dict, Optional, Sequence, Tuple, Union
 
-from google.api_core import gapic_v1  # type: ignore
-from google.api_core import grpc_helpers_async  # type: ignore
+from google.api_core import gapic_v1
+from google.api_core import grpc_helpers_async
 from google.auth import credentials as ga_credentials  # type: ignore
 from google.auth.transport.grpc import SslCredentials  # type: ignore
-import packaging.version
 
 import grpc  # type: ignore
 from grpc.experimental import aio  # type: ignore
 
 from google.iam.v1 import iam_policy_pb2  # type: ignore
 from google.iam.v1 import policy_pb2  # type: ignore
 from google.protobuf import empty_pb2  # type: ignore
@@ -129,24 +128,24 @@
                 service. These are only used when credentials are not specified and
                 are passed to :func:`google.auth.default`.
             channel (Optional[aio.Channel]): A ``Channel`` instance through
                 which to make calls.
             api_mtls_endpoint (Optional[str]): Deprecated. The mutual TLS endpoint.
                 If provided, it overrides the ``host`` argument and tries to create
                 a mutual TLS channel with client SSL credentials from
-                ``client_cert_source`` or applicatin default SSL credentials.
+                ``client_cert_source`` or application default SSL credentials.
             client_cert_source (Optional[Callable[[], Tuple[bytes, bytes]]]):
                 Deprecated. A callback to provide client SSL certificate bytes and
                 private key bytes, both in PEM format. It is ignored if
                 ``api_mtls_endpoint`` is None.
             ssl_channel_credentials (grpc.ChannelCredentials): SSL credentials
-                for grpc channel. It is ignored if ``channel`` is provided.
+                for the grpc channel. It is ignored if ``channel`` is provided.
             client_cert_source_for_mtls (Optional[Callable[[], Tuple[bytes, bytes]]]):
                 A callback to provide client certificate bytes and private key bytes,
-                both in PEM format. It is used to configure mutual TLS channel. It is
+                both in PEM format. It is used to configure a mutual TLS channel. It is
                 ignored if ``channel`` or ``ssl_channel_credentials`` is provided.
             quota_project_id (Optional[str]): An optional project to use for billing
                 and quota.
             client_info (google.api_core.gapic_v1.client_info.ClientInfo):
                 The client info used to send a user-agent string along with
                 API requests. If ``None``, then default info will be used.
                 Generally, you only need to set this if you're developing
@@ -826,9 +825,12 @@
             self._stubs["test_iam_permissions"] = self.grpc_channel.unary_unary(
                 "/google.iam.v1.IAMPolicy/TestIamPermissions",
                 request_serializer=iam_policy_pb2.TestIamPermissionsRequest.SerializeToString,
                 response_deserializer=iam_policy_pb2.TestIamPermissionsResponse.FromString,
             )
         return self._stubs["test_iam_permissions"]
 
+    def close(self):
+        return self.grpc_channel.close()
+
 
 __all__ = ("SubscriberGrpcAsyncIOTransport",)
```

### Comparing `google-cloud-pubsub-2.8.0/google/pubsub_v1/types/__init__.py` & `google-cloud-pubsub-2.9.0/google/pubsub_v1/types/__init__.py`

 * *Files identical despite different names*

### Comparing `google-cloud-pubsub-2.8.0/google/pubsub_v1/types/pubsub.py` & `google-cloud-pubsub-2.9.0/google/pubsub_v1/types/pubsub.py`

 * *Files 2% similar despite different names*

```diff
@@ -434,15 +434,16 @@
 
     subscription = proto.Field(proto.STRING, number=1,)
 
 
 class DetachSubscriptionResponse(proto.Message):
     r"""Response for the DetachSubscription method.
     Reserved for future use.
-        """
+
+    """
 
 
 class Subscription(proto.Message):
     r"""A subscription resource.
 
     Attributes:
         name (str):
@@ -687,14 +688,16 @@
 
     ttl = proto.Field(proto.MESSAGE, number=1, message=duration_pb2.Duration,)
 
 
 class PushConfig(proto.Message):
     r"""Configuration for a push delivery endpoint.
 
+    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields
+
     Attributes:
         push_endpoint (str):
             A URL locating the endpoint to which messages should be
             pushed. For example, a Webhook endpoint might use
             ``https://example.com/push``.
         attributes (Sequence[google.pubsub_v1.types.PushConfig.AttributesEntry]):
             Endpoint configuration attributes that can be used to
@@ -726,14 +729,16 @@
             .. raw:: html
 
                 <pre><code>attributes { "x-goog-version": "v1" } </code></pre>
         oidc_token (google.pubsub_v1.types.PushConfig.OidcToken):
             If specified, Pub/Sub will generate and attach an OIDC JWT
             token as an ``Authorization`` header in the HTTP request for
             every pushed message.
+
+            This field is a member of `oneof`_ ``authentication_method``.
     """
 
     class OidcToken(proto.Message):
         r"""Contains information needed for generating an `OpenID Connect
         token <https://developers.google.com/identity/protocols/OpenIDConnect>`__.
 
         Attributes:
@@ -1277,14 +1282,21 @@
 
     snapshot = proto.Field(proto.STRING, number=1,)
 
 
 class SeekRequest(proto.Message):
     r"""Request for the ``Seek`` method.
 
+    This message has `oneof`_ fields (mutually exclusive fields).
+    For each oneof, at most one member field can be set at the same time.
+    Setting any member of the oneof automatically clears all other
+    members.
+
+    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields
+
     Attributes:
         subscription (str):
             Required. The subscription to affect.
         time (google.protobuf.timestamp_pb2.Timestamp):
             The time to seek to. Messages retained in the subscription
             that were published before this time are marked as
             acknowledged, and messages retained in the subscription that
@@ -1294,25 +1306,30 @@
             of ``message_retention_duration`` and
             ``retain_acked_messages``). For example, if ``time``
             corresponds to a point before the message retention window
             (or to a point before the system's notion of the
             subscription creation time), only retained messages will be
             marked as unacknowledged, and already-expunged messages will
             not be restored.
+
+            This field is a member of `oneof`_ ``target``.
         snapshot (str):
             The snapshot to seek to. The snapshot's topic must be the
             same as that of the provided subscription. Format is
             ``projects/{project}/snapshots/{snap}``.
+
+            This field is a member of `oneof`_ ``target``.
     """
 
     subscription = proto.Field(proto.STRING, number=1,)
     time = proto.Field(
         proto.MESSAGE, number=2, oneof="target", message=timestamp_pb2.Timestamp,
     )
     snapshot = proto.Field(proto.STRING, number=3, oneof="target",)
 
 
 class SeekResponse(proto.Message):
-    r"""Response for the ``Seek`` method (this response is empty).    """
+    r"""Response for the ``Seek`` method (this response is empty).
+    """
 
 
 __all__ = tuple(sorted(__protobuf__.manifest))
```

### Comparing `google-cloud-pubsub-2.8.0/google/pubsub_v1/types/schema.py` & `google-cloud-pubsub-2.9.0/google/pubsub_v1/types/schema.py`

 * *Files 6% similar despite different names*

```diff
@@ -191,30 +191,42 @@
     """
 
     parent = proto.Field(proto.STRING, number=1,)
     schema = proto.Field(proto.MESSAGE, number=2, message="Schema",)
 
 
 class ValidateSchemaResponse(proto.Message):
-    r"""Response for the ``ValidateSchema`` method. Empty for now.    """
+    r"""Response for the ``ValidateSchema`` method. Empty for now.
+    """
 
 
 class ValidateMessageRequest(proto.Message):
     r"""Request for the ``ValidateMessage`` method.
 
+    This message has `oneof`_ fields (mutually exclusive fields).
+    For each oneof, at most one member field can be set at the same time.
+    Setting any member of the oneof automatically clears all other
+    members.
+
+    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields
+
     Attributes:
         parent (str):
             Required. The name of the project in which to validate
             schemas. Format is ``projects/{project-id}``.
         name (str):
             Name of the schema against which to validate.
 
             Format is ``projects/{project}/schemas/{schema}``.
+
+            This field is a member of `oneof`_ ``schema_spec``.
         schema (google.pubsub_v1.types.Schema):
             Ad-hoc schema against which to validate
+
+            This field is a member of `oneof`_ ``schema_spec``.
         message (bytes):
             Message to validate against the provided ``schema_spec``.
         encoding (google.pubsub_v1.types.Encoding):
             The encoding expected for messages
     """
 
     parent = proto.Field(proto.STRING, number=1,)
@@ -223,11 +235,12 @@
         proto.MESSAGE, number=3, oneof="schema_spec", message="Schema",
     )
     message = proto.Field(proto.BYTES, number=4,)
     encoding = proto.Field(proto.ENUM, number=5, enum="Encoding",)
 
 
 class ValidateMessageResponse(proto.Message):
-    r"""Response for the ``ValidateMessage`` method. Empty for now.    """
+    r"""Response for the ``ValidateMessage`` method. Empty for now.
+    """
 
 
 __all__ = tuple(sorted(__protobuf__.manifest))
```

### Comparing `google-cloud-pubsub-2.8.0/google_cloud_pubsub.egg-info/PKG-INFO` & `google-cloud-pubsub-2.9.0/google_cloud_pubsub.egg-info/PKG-INFO`

 * *Files 3% similar despite different names*

```diff
@@ -1,24 +1,26 @@
 Metadata-Version: 2.1
 Name: google-cloud-pubsub
-Version: 2.8.0
+Version: 2.9.0
 Summary: Google Cloud Pub/Sub API client library
 Home-page: https://github.com/googleapis/python-pubsub
 Author: Google LLC
 Author-email: googleapis-packages@google.com
 License: Apache 2.0
 Platform: Posix; MacOS X; Windows
 Classifier: Development Status :: 5 - Production/Stable
 Classifier: Intended Audience :: Developers
 Classifier: License :: OSI Approved :: Apache Software License
 Classifier: Programming Language :: Python
 Classifier: Programming Language :: Python :: 3
 Classifier: Programming Language :: Python :: 3.6
 Classifier: Programming Language :: Python :: 3.7
 Classifier: Programming Language :: Python :: 3.8
+Classifier: Programming Language :: Python :: 3.9
+Classifier: Programming Language :: Python :: 3.10
 Classifier: Operating System :: OS Independent
 Classifier: Topic :: Internet
 Requires-Python: >=3.6
 License-File: LICENSE
 
 Python Client for Google Cloud Pub / Sub
 ========================================
@@ -38,15 +40,15 @@
 receivers, Google Cloud Pub/Sub allows developers to communicate between
 independently written applications.
 
 - `Product Documentation`_
 - `Client Library Documentation`_
 
 .. |GA| image:: https://img.shields.io/badge/support-GA-gold.svg
-   :target: https://github.com/googleapis/google-cloud-python/blob/master/README.rst#general-availability
+   :target: https://github.com/googleapis/google-cloud-python/blob/main/README.rst#general-availability
 .. |pypi| image:: https://img.shields.io/pypi/v/google-cloud-pubsub.svg
    :target: https://pypi.org/project/google-cloud-pubsub/
 .. |versions| image:: https://img.shields.io/pypi/pyversions/google-cloud-pubsub.svg
    :target: https://pypi.org/project/google-cloud-pubsub/
 .. _Google Cloud Pub / Sub: https://cloud.google.com/pubsub/
 .. _Product Documentation: https://cloud.google.com/pubsub/docs
 .. _Client Library Documentation: https://googleapis.dev/python/pubsub/latest
@@ -232,15 +234,15 @@
 Contributing
 ------------
 
 Contributions to this library are always welcome and highly encouraged.
 
 See the `CONTRIBUTING doc`_ for more information on how to get started.
 
-.. _CONTRIBUTING doc: https://github.com/googleapis/google-cloud-python/blob/master/CONTRIBUTING.rst
+.. _CONTRIBUTING doc: https://github.com/googleapis/google-cloud-python/blob/main/CONTRIBUTING.rst
 
 Community
 ---------
 
 Google Cloud Platform Python developers hang out in `Slack`_ in the ``#python``
 channel, click here to `get an invitation`_.
 
@@ -248,10 +250,10 @@
 .. _get an invitation: https://gcp-slack.appspot.com/
 
 License
 -------
 
 Apache 2.0 - See `the LICENSE`_ for more information.
 
-.. _the LICENSE: https://github.com/googleapis/google-cloud-python/blob/master/LICENSE
+.. _the LICENSE: https://github.com/googleapis/google-cloud-python/blob/main/LICENSE
```

### Comparing `google-cloud-pubsub-2.8.0/google_cloud_pubsub.egg-info/SOURCES.txt` & `google-cloud-pubsub-2.9.0/google_cloud_pubsub.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `google-cloud-pubsub-2.8.0/scripts/fixup_pubsub_v1_keywords.py` & `google-cloud-pubsub-2.9.0/scripts/fixup_pubsub_v1_keywords.py`

 * *Files 0% similar despite different names*

```diff
@@ -35,45 +35,45 @@
     # Returns trueList, falseList
     return results[1], results[0]
 
 
 class pubsubCallTransformer(cst.CSTTransformer):
     CTRL_PARAMS: Tuple[str] = ('retry', 'timeout', 'metadata')
     METHOD_TO_PARAMS: Dict[str, Tuple[str]] = {
-          'acknowledge': ('subscription', 'ack_ids', ),
-          'create_schema': ('parent', 'schema', 'schema_id', ),
-          'create_snapshot': ('name', 'subscription', 'labels', ),
-          'create_subscription': ('name', 'topic', 'push_config', 'ack_deadline_seconds', 'retain_acked_messages', 'message_retention_duration', 'labels', 'enable_message_ordering', 'expiration_policy', 'filter', 'dead_letter_policy', 'retry_policy', 'detached', 'topic_message_retention_duration', ),
-          'create_topic': ('name', 'labels', 'message_storage_policy', 'kms_key_name', 'schema_settings', 'satisfies_pzs', 'message_retention_duration', ),
-          'delete_schema': ('name', ),
-          'delete_snapshot': ('snapshot', ),
-          'delete_subscription': ('subscription', ),
-          'delete_topic': ('topic', ),
-          'detach_subscription': ('subscription', ),
-          'get_schema': ('name', 'view', ),
-          'get_snapshot': ('snapshot', ),
-          'get_subscription': ('subscription', ),
-          'get_topic': ('topic', ),
-          'list_schemas': ('parent', 'view', 'page_size', 'page_token', ),
-          'list_snapshots': ('project', 'page_size', 'page_token', ),
-          'list_subscriptions': ('project', 'page_size', 'page_token', ),
-          'list_topics': ('project', 'page_size', 'page_token', ),
-          'list_topic_snapshots': ('topic', 'page_size', 'page_token', ),
-          'list_topic_subscriptions': ('topic', 'page_size', 'page_token', ),
-          'modify_ack_deadline': ('subscription', 'ack_ids', 'ack_deadline_seconds', ),
-          'modify_push_config': ('subscription', 'push_config', ),
-          'publish': ('topic', 'messages', ),
-          'pull': ('subscription', 'max_messages', 'return_immediately', ),
-          'seek': ('subscription', 'time', 'snapshot', ),
-          'streaming_pull': ('subscription', 'stream_ack_deadline_seconds', 'ack_ids', 'modify_deadline_seconds', 'modify_deadline_ack_ids', 'client_id', 'max_outstanding_messages', 'max_outstanding_bytes', ),
-          'update_snapshot': ('snapshot', 'update_mask', ),
-          'update_subscription': ('subscription', 'update_mask', ),
-          'update_topic': ('topic', 'update_mask', ),
-          'validate_message': ('parent', 'name', 'schema', 'message', 'encoding', ),
-          'validate_schema': ('parent', 'schema', ),
+        'acknowledge': ('subscription', 'ack_ids', ),
+        'create_schema': ('parent', 'schema', 'schema_id', ),
+        'create_snapshot': ('name', 'subscription', 'labels', ),
+        'create_subscription': ('name', 'topic', 'push_config', 'ack_deadline_seconds', 'retain_acked_messages', 'message_retention_duration', 'labels', 'enable_message_ordering', 'expiration_policy', 'filter', 'dead_letter_policy', 'retry_policy', 'detached', 'topic_message_retention_duration', ),
+        'create_topic': ('name', 'labels', 'message_storage_policy', 'kms_key_name', 'schema_settings', 'satisfies_pzs', 'message_retention_duration', ),
+        'delete_schema': ('name', ),
+        'delete_snapshot': ('snapshot', ),
+        'delete_subscription': ('subscription', ),
+        'delete_topic': ('topic', ),
+        'detach_subscription': ('subscription', ),
+        'get_schema': ('name', 'view', ),
+        'get_snapshot': ('snapshot', ),
+        'get_subscription': ('subscription', ),
+        'get_topic': ('topic', ),
+        'list_schemas': ('parent', 'view', 'page_size', 'page_token', ),
+        'list_snapshots': ('project', 'page_size', 'page_token', ),
+        'list_subscriptions': ('project', 'page_size', 'page_token', ),
+        'list_topics': ('project', 'page_size', 'page_token', ),
+        'list_topic_snapshots': ('topic', 'page_size', 'page_token', ),
+        'list_topic_subscriptions': ('topic', 'page_size', 'page_token', ),
+        'modify_ack_deadline': ('subscription', 'ack_ids', 'ack_deadline_seconds', ),
+        'modify_push_config': ('subscription', 'push_config', ),
+        'publish': ('topic', 'messages', ),
+        'pull': ('subscription', 'max_messages', 'return_immediately', ),
+        'seek': ('subscription', 'time', 'snapshot', ),
+        'streaming_pull': ('subscription', 'stream_ack_deadline_seconds', 'ack_ids', 'modify_deadline_seconds', 'modify_deadline_ack_ids', 'client_id', 'max_outstanding_messages', 'max_outstanding_bytes', ),
+        'update_snapshot': ('snapshot', 'update_mask', ),
+        'update_subscription': ('subscription', 'update_mask', ),
+        'update_topic': ('topic', 'update_mask', ),
+        'validate_message': ('parent', 'name', 'schema', 'message', 'encoding', ),
+        'validate_schema': ('parent', 'schema', ),
     'get_iam_policy': ('resource', 'options', ),
     'set_iam_policy': ('resource', 'policy', ),
     'test_iam_permissions': ('resource', 'permissions', ),
     }
 
     def leave_Call(self, original: cst.Call, updated: cst.Call) -> cst.CSTNode:
         try:
@@ -87,15 +87,15 @@
         # Therefore, all positional args must map to the first parameters.
         args, kwargs = partition(lambda a: not bool(a.keyword), updated.args)
         if any(k.keyword.value == "request" for k in kwargs):
             # We've already fixed this file, don't fix it again.
             return updated
 
         kwargs, ctrl_kwargs = partition(
-            lambda a: not a.keyword.value in self.CTRL_PARAMS,
+            lambda a: a.keyword.value not in self.CTRL_PARAMS,
             kwargs
         )
 
         args, ctrl_args = args[:len(kword_params)], args[len(kword_params):]
         ctrl_kwargs.extend(cst.Arg(value=a.value, keyword=cst.Name(value=ctrl))
                            for a, ctrl in zip(ctrl_args, self.CTRL_PARAMS))
```

### Comparing `google-cloud-pubsub-2.8.0/setup.py` & `google-cloud-pubsub-2.9.0/setup.py`

 * *Files 4% similar despite different names*

```diff
@@ -18,30 +18,29 @@
 import setuptools
 
 
 # Package metadata.
 
 name = "google-cloud-pubsub"
 description = "Google Cloud Pub/Sub API client library"
-version = "2.8.0"
+version = "2.9.0"
 # Should be one of:
 # 'Development Status :: 3 - Alpha'
 # 'Development Status :: 4 - Beta'
 # 'Development Status :: 5 - Production/Stable'
 release_status = "Development Status :: 5 - Production/Stable"
 dependencies = [
     "grpcio >= 1.38.1, < 2.0dev",  # https://github.com/googleapis/python-pubsub/issues/414
     # NOTE: Maintainers, please do not require google-api-core>=2.x.x
     # Until this issue is closed
     # https://github.com/googleapis/google-cloud-python/issues/10566
-    "google-api-core[grpc] >= 1.26.0, <3.0.0dev",
+    "google-api-core[grpc] >= 1.28.0, <3.0.0dev",
     "libcst >= 0.3.10",
     "proto-plus >= 1.7.1",
     "grpc-google-iam-v1 >= 0.12.3, < 0.13dev",
-    "packaging >= 14.3",
 ]
 extras = {}
 
 
 # Setup boilerplate below this line.
 
 package_root = os.path.abspath(os.path.dirname(__file__))
@@ -78,14 +77,16 @@
         "Intended Audience :: Developers",
         "License :: OSI Approved :: Apache Software License",
         "Programming Language :: Python",
         "Programming Language :: Python :: 3",
         "Programming Language :: Python :: 3.6",
         "Programming Language :: Python :: 3.7",
         "Programming Language :: Python :: 3.8",
+        "Programming Language :: Python :: 3.9",
+        "Programming Language :: Python :: 3.10",
         "Operating System :: OS Independent",
         "Topic :: Internet",
     ],
     platforms="Posix; MacOS X; Windows",
     packages=packages,
     namespace_packages=namespaces,
     install_requires=dependencies,
```

### Comparing `google-cloud-pubsub-2.8.0/tests/__init__.py` & `google-cloud-pubsub-2.9.0/tests/__init__.py`

 * *Files identical despite different names*

### Comparing `google-cloud-pubsub-2.8.0/tests/system.py` & `google-cloud-pubsub-2.9.0/tests/system.py`

 * *Files identical despite different names*

### Comparing `google-cloud-pubsub-2.8.0/tests/unit/__init__.py` & `google-cloud-pubsub-2.9.0/tests/unit/__init__.py`

 * *Files identical despite different names*

### Comparing `google-cloud-pubsub-2.8.0/tests/unit/gapic/__init__.py` & `google-cloud-pubsub-2.9.0/tests/unit/gapic/__init__.py`

 * *Files identical despite different names*

### Comparing `google-cloud-pubsub-2.8.0/tests/unit/gapic/pubsub_v1/__init__.py` & `google-cloud-pubsub-2.9.0/tests/unit/gapic/pubsub_v1/__init__.py`

 * *Files identical despite different names*

### Comparing `google-cloud-pubsub-2.8.0/tests/unit/gapic/pubsub_v1/test_publisher.py` & `google-cloud-pubsub-2.9.0/tests/unit/gapic/pubsub_v1/test_publisher.py`

 * *Files 3% similar despite different names*

```diff
@@ -11,61 +11,46 @@
 # distributed under the License is distributed on an "AS IS" BASIS,
 # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 # See the License for the specific language governing permissions and
 # limitations under the License.
 #
 import os
 import mock
-import packaging.version
 
 import grpc
 from grpc.experimental import aio
 import math
 import pytest
 from proto.marshal.rules.dates import DurationRule, TimestampRule
 
 
 from google.api_core import client_options
 from google.api_core import exceptions as core_exceptions
 from google.api_core import gapic_v1
 from google.api_core import grpc_helpers
 from google.api_core import grpc_helpers_async
+from google.api_core import path_template
 from google.auth import credentials as ga_credentials
 from google.auth.exceptions import MutualTLSChannelError
 from google.iam.v1 import iam_policy_pb2  # type: ignore
 from google.iam.v1 import options_pb2  # type: ignore
 from google.iam.v1 import policy_pb2  # type: ignore
 from google.oauth2 import service_account
 from google.protobuf import duration_pb2  # type: ignore
 from google.protobuf import field_mask_pb2  # type: ignore
 from google.protobuf import timestamp_pb2  # type: ignore
 from google.pubsub_v1.services.publisher import PublisherAsyncClient
 from google.pubsub_v1.services.publisher import PublisherClient
 from google.pubsub_v1.services.publisher import pagers
 from google.pubsub_v1.services.publisher import transports
-from google.pubsub_v1.services.publisher.transports.base import _GOOGLE_AUTH_VERSION
 from google.pubsub_v1.types import pubsub
 from google.pubsub_v1.types import schema
 import google.auth
 
 
-# TODO(busunkim): Once google-auth >= 1.25.0 is required transitively
-# through google-api-core:
-# - Delete the auth "less than" test cases
-# - Delete these pytest markers (Make the "greater than or equal to" tests the default).
-requires_google_auth_lt_1_25_0 = pytest.mark.skipif(
-    packaging.version.parse(_GOOGLE_AUTH_VERSION) >= packaging.version.parse("1.25.0"),
-    reason="This test requires google-auth < 1.25.0",
-)
-requires_google_auth_gte_1_25_0 = pytest.mark.skipif(
-    packaging.version.parse(_GOOGLE_AUTH_VERSION) < packaging.version.parse("1.25.0"),
-    reason="This test requires google-auth >= 1.25.0",
-)
-
-
 def client_cert_source_callback():
     return b"cert bytes", b"key bytes"
 
 
 # If default endpoint is localhost, then default mtls endpoint will be the same.
 # This method modifies the default endpoint so the client can produce a different
 # mtls endpoint for endpoint testing purposes.
@@ -201,15 +186,15 @@
         client = client_class(transport=transport_name)
         gtc.assert_called()
 
     # Check the case api_endpoint is provided.
     options = client_options.ClientOptions(api_endpoint="squid.clam.whelk")
     with mock.patch.object(transport_class, "__init__") as patched:
         patched.return_value = None
-        client = client_class(client_options=options)
+        client = client_class(transport=transport_name, client_options=options)
         patched.assert_called_once_with(
             credentials=None,
             credentials_file=None,
             host="squid.clam.whelk",
             scopes=None,
             client_cert_source_for_mtls=None,
             quota_project_id=None,
@@ -218,15 +203,15 @@
         )
 
     # Check the case api_endpoint is not provided and GOOGLE_API_USE_MTLS_ENDPOINT is
     # "never".
     with mock.patch.dict(os.environ, {"GOOGLE_API_USE_MTLS_ENDPOINT": "never"}):
         with mock.patch.object(transport_class, "__init__") as patched:
             patched.return_value = None
-            client = client_class()
+            client = client_class(transport=transport_name)
             patched.assert_called_once_with(
                 credentials=None,
                 credentials_file=None,
                 host=client.DEFAULT_ENDPOINT,
                 scopes=None,
                 client_cert_source_for_mtls=None,
                 quota_project_id=None,
@@ -235,15 +220,15 @@
             )
 
     # Check the case api_endpoint is not provided and GOOGLE_API_USE_MTLS_ENDPOINT is
     # "always".
     with mock.patch.dict(os.environ, {"GOOGLE_API_USE_MTLS_ENDPOINT": "always"}):
         with mock.patch.object(transport_class, "__init__") as patched:
             patched.return_value = None
-            client = client_class()
+            client = client_class(transport=transport_name)
             patched.assert_called_once_with(
                 credentials=None,
                 credentials_file=None,
                 host=client.DEFAULT_MTLS_ENDPOINT,
                 scopes=None,
                 client_cert_source_for_mtls=None,
                 quota_project_id=None,
@@ -264,15 +249,15 @@
         with pytest.raises(ValueError):
             client = client_class()
 
     # Check the case quota_project_id is provided
     options = client_options.ClientOptions(quota_project_id="octopus")
     with mock.patch.object(transport_class, "__init__") as patched:
         patched.return_value = None
-        client = client_class(client_options=options)
+        client = client_class(transport=transport_name, client_options=options)
         patched.assert_called_once_with(
             credentials=None,
             credentials_file=None,
             host=client.DEFAULT_ENDPOINT,
             scopes=None,
             client_cert_source_for_mtls=None,
             quota_project_id="octopus",
@@ -321,15 +306,15 @@
         os.environ, {"GOOGLE_API_USE_CLIENT_CERTIFICATE": use_client_cert_env}
     ):
         options = client_options.ClientOptions(
             client_cert_source=client_cert_source_callback
         )
         with mock.patch.object(transport_class, "__init__") as patched:
             patched.return_value = None
-            client = client_class(client_options=options)
+            client = client_class(transport=transport_name, client_options=options)
 
             if use_client_cert_env == "false":
                 expected_client_cert_source = None
                 expected_host = client.DEFAULT_ENDPOINT
             else:
                 expected_client_cert_source = client_cert_source_callback
                 expected_host = client.DEFAULT_MTLS_ENDPOINT
@@ -363,15 +348,15 @@
                         expected_host = client.DEFAULT_ENDPOINT
                         expected_client_cert_source = None
                     else:
                         expected_host = client.DEFAULT_MTLS_ENDPOINT
                         expected_client_cert_source = client_cert_source_callback
 
                     patched.return_value = None
-                    client = client_class()
+                    client = client_class(transport=transport_name)
                     patched.assert_called_once_with(
                         credentials=None,
                         credentials_file=None,
                         host=expected_host,
                         scopes=None,
                         client_cert_source_for_mtls=expected_client_cert_source,
                         quota_project_id=None,
@@ -385,15 +370,15 @@
     ):
         with mock.patch.object(transport_class, "__init__") as patched:
             with mock.patch(
                 "google.auth.transport.mtls.has_default_client_cert_source",
                 return_value=False,
             ):
                 patched.return_value = None
-                client = client_class()
+                client = client_class(transport=transport_name)
                 patched.assert_called_once_with(
                     credentials=None,
                     credentials_file=None,
                     host=client.DEFAULT_ENDPOINT,
                     scopes=None,
                     client_cert_source_for_mtls=None,
                     quota_project_id=None,
@@ -416,15 +401,15 @@
 def test_publisher_client_client_options_scopes(
     client_class, transport_class, transport_name
 ):
     # Check the case scopes are provided.
     options = client_options.ClientOptions(scopes=["1", "2"],)
     with mock.patch.object(transport_class, "__init__") as patched:
         patched.return_value = None
-        client = client_class(client_options=options)
+        client = client_class(transport=transport_name, client_options=options)
         patched.assert_called_once_with(
             credentials=None,
             credentials_file=None,
             host=client.DEFAULT_ENDPOINT,
             scopes=["1", "2"],
             client_cert_source_for_mtls=None,
             quota_project_id=None,
@@ -447,15 +432,15 @@
 def test_publisher_client_client_options_credentials_file(
     client_class, transport_class, transport_name
 ):
     # Check the case credentials file is provided.
     options = client_options.ClientOptions(credentials_file="credentials.json")
     with mock.patch.object(transport_class, "__init__") as patched:
         patched.return_value = None
-        client = client_class(client_options=options)
+        client = client_class(transport=transport_name, client_options=options)
         patched.assert_called_once_with(
             credentials=None,
             credentials_file="credentials.json",
             host=client.DEFAULT_ENDPOINT,
             scopes=None,
             client_cert_source_for_mtls=None,
             quota_project_id=None,
@@ -631,15 +616,17 @@
         # using the keyword arguments to the method.
         client.create_topic(name="name_value",)
 
         # Establish that the underlying call was made with the expected
         # request object values.
         assert len(call.mock_calls) == 1
         _, args, _ = call.mock_calls[0]
-        assert args[0].name == "name_value"
+        arg = args[0].name
+        mock_val = "name_value"
+        assert arg == mock_val
 
 
 def test_create_topic_flattened_error():
     client = PublisherClient(credentials=ga_credentials.AnonymousCredentials(),)
 
     # Attempting to call a method with both a request object and flattened
     # fields is an error.
@@ -663,15 +650,17 @@
         # using the keyword arguments to the method.
         response = await client.create_topic(name="name_value",)
 
         # Establish that the underlying call was made with the expected
         # request object values.
         assert len(call.mock_calls)
         _, args, _ = call.mock_calls[0]
-        assert args[0].name == "name_value"
+        arg = args[0].name
+        mock_val = "name_value"
+        assert arg == mock_val
 
 
 @pytest.mark.asyncio
 async def test_create_topic_flattened_error_async():
     client = PublisherAsyncClient(credentials=ga_credentials.AnonymousCredentials(),)
 
     # Attempting to call a method with both a request object and flattened
@@ -963,16 +952,20 @@
             topic="topic_value", messages=[pubsub.PubsubMessage(data=b"data_blob")],
         )
 
         # Establish that the underlying call was made with the expected
         # request object values.
         assert len(call.mock_calls) == 1
         _, args, _ = call.mock_calls[0]
-        assert args[0].topic == "topic_value"
-        assert args[0].messages == [pubsub.PubsubMessage(data=b"data_blob")]
+        arg = args[0].topic
+        mock_val = "topic_value"
+        assert arg == mock_val
+        arg = args[0].messages
+        mock_val = [pubsub.PubsubMessage(data=b"data_blob")]
+        assert arg == mock_val
 
 
 def test_publish_flattened_error():
     client = PublisherClient(credentials=ga_credentials.AnonymousCredentials(),)
 
     # Attempting to call a method with both a request object and flattened
     # fields is an error.
@@ -1002,16 +995,20 @@
             topic="topic_value", messages=[pubsub.PubsubMessage(data=b"data_blob")],
         )
 
         # Establish that the underlying call was made with the expected
         # request object values.
         assert len(call.mock_calls)
         _, args, _ = call.mock_calls[0]
-        assert args[0].topic == "topic_value"
-        assert args[0].messages == [pubsub.PubsubMessage(data=b"data_blob")]
+        arg = args[0].topic
+        mock_val = "topic_value"
+        assert arg == mock_val
+        arg = args[0].messages
+        mock_val = [pubsub.PubsubMessage(data=b"data_blob")]
+        assert arg == mock_val
 
 
 @pytest.mark.asyncio
 async def test_publish_flattened_error_async():
     client = PublisherAsyncClient(credentials=ga_credentials.AnonymousCredentials(),)
 
     # Attempting to call a method with both a request object and flattened
@@ -1173,15 +1170,17 @@
         # using the keyword arguments to the method.
         client.get_topic(topic="topic_value",)
 
         # Establish that the underlying call was made with the expected
         # request object values.
         assert len(call.mock_calls) == 1
         _, args, _ = call.mock_calls[0]
-        assert args[0].topic == "topic_value"
+        arg = args[0].topic
+        mock_val = "topic_value"
+        assert arg == mock_val
 
 
 def test_get_topic_flattened_error():
     client = PublisherClient(credentials=ga_credentials.AnonymousCredentials(),)
 
     # Attempting to call a method with both a request object and flattened
     # fields is an error.
@@ -1205,15 +1204,17 @@
         # using the keyword arguments to the method.
         response = await client.get_topic(topic="topic_value",)
 
         # Establish that the underlying call was made with the expected
         # request object values.
         assert len(call.mock_calls)
         _, args, _ = call.mock_calls[0]
-        assert args[0].topic == "topic_value"
+        arg = args[0].topic
+        mock_val = "topic_value"
+        assert arg == mock_val
 
 
 @pytest.mark.asyncio
 async def test_get_topic_flattened_error_async():
     client = PublisherAsyncClient(credentials=ga_credentials.AnonymousCredentials(),)
 
     # Attempting to call a method with both a request object and flattened
@@ -1367,15 +1368,17 @@
         # using the keyword arguments to the method.
         client.list_topics(project="project_value",)
 
         # Establish that the underlying call was made with the expected
         # request object values.
         assert len(call.mock_calls) == 1
         _, args, _ = call.mock_calls[0]
-        assert args[0].project == "project_value"
+        arg = args[0].project
+        mock_val = "project_value"
+        assert arg == mock_val
 
 
 def test_list_topics_flattened_error():
     client = PublisherClient(credentials=ga_credentials.AnonymousCredentials(),)
 
     # Attempting to call a method with both a request object and flattened
     # fields is an error.
@@ -1401,15 +1404,17 @@
         # using the keyword arguments to the method.
         response = await client.list_topics(project="project_value",)
 
         # Establish that the underlying call was made with the expected
         # request object values.
         assert len(call.mock_calls)
         _, args, _ = call.mock_calls[0]
-        assert args[0].project == "project_value"
+        arg = args[0].project
+        mock_val = "project_value"
+        assert arg == mock_val
 
 
 @pytest.mark.asyncio
 async def test_list_topics_flattened_error_async():
     client = PublisherAsyncClient(credentials=ga_credentials.AnonymousCredentials(),)
 
     # Attempting to call a method with both a request object and flattened
@@ -1689,15 +1694,17 @@
         # using the keyword arguments to the method.
         client.list_topic_subscriptions(topic="topic_value",)
 
         # Establish that the underlying call was made with the expected
         # request object values.
         assert len(call.mock_calls) == 1
         _, args, _ = call.mock_calls[0]
-        assert args[0].topic == "topic_value"
+        arg = args[0].topic
+        mock_val = "topic_value"
+        assert arg == mock_val
 
 
 def test_list_topic_subscriptions_flattened_error():
     client = PublisherClient(credentials=ga_credentials.AnonymousCredentials(),)
 
     # Attempting to call a method with both a request object and flattened
     # fields is an error.
@@ -1725,15 +1732,17 @@
         # using the keyword arguments to the method.
         response = await client.list_topic_subscriptions(topic="topic_value",)
 
         # Establish that the underlying call was made with the expected
         # request object values.
         assert len(call.mock_calls)
         _, args, _ = call.mock_calls[0]
-        assert args[0].topic == "topic_value"
+        arg = args[0].topic
+        mock_val = "topic_value"
+        assert arg == mock_val
 
 
 @pytest.mark.asyncio
 async def test_list_topic_subscriptions_flattened_error_async():
     client = PublisherAsyncClient(credentials=ga_credentials.AnonymousCredentials(),)
 
     # Attempting to call a method with both a request object and flattened
@@ -2031,15 +2040,17 @@
         # using the keyword arguments to the method.
         client.list_topic_snapshots(topic="topic_value",)
 
         # Establish that the underlying call was made with the expected
         # request object values.
         assert len(call.mock_calls) == 1
         _, args, _ = call.mock_calls[0]
-        assert args[0].topic == "topic_value"
+        arg = args[0].topic
+        mock_val = "topic_value"
+        assert arg == mock_val
 
 
 def test_list_topic_snapshots_flattened_error():
     client = PublisherClient(credentials=ga_credentials.AnonymousCredentials(),)
 
     # Attempting to call a method with both a request object and flattened
     # fields is an error.
@@ -2067,15 +2078,17 @@
         # using the keyword arguments to the method.
         response = await client.list_topic_snapshots(topic="topic_value",)
 
         # Establish that the underlying call was made with the expected
         # request object values.
         assert len(call.mock_calls)
         _, args, _ = call.mock_calls[0]
-        assert args[0].topic == "topic_value"
+        arg = args[0].topic
+        mock_val = "topic_value"
+        assert arg == mock_val
 
 
 @pytest.mark.asyncio
 async def test_list_topic_snapshots_flattened_error_async():
     client = PublisherAsyncClient(credentials=ga_credentials.AnonymousCredentials(),)
 
     # Attempting to call a method with both a request object and flattened
@@ -2339,15 +2352,17 @@
         # using the keyword arguments to the method.
         client.delete_topic(topic="topic_value",)
 
         # Establish that the underlying call was made with the expected
         # request object values.
         assert len(call.mock_calls) == 1
         _, args, _ = call.mock_calls[0]
-        assert args[0].topic == "topic_value"
+        arg = args[0].topic
+        mock_val = "topic_value"
+        assert arg == mock_val
 
 
 def test_delete_topic_flattened_error():
     client = PublisherClient(credentials=ga_credentials.AnonymousCredentials(),)
 
     # Attempting to call a method with both a request object and flattened
     # fields is an error.
@@ -2371,15 +2386,17 @@
         # using the keyword arguments to the method.
         response = await client.delete_topic(topic="topic_value",)
 
         # Establish that the underlying call was made with the expected
         # request object values.
         assert len(call.mock_calls)
         _, args, _ = call.mock_calls[0]
-        assert args[0].topic == "topic_value"
+        arg = args[0].topic
+        mock_val = "topic_value"
+        assert arg == mock_val
 
 
 @pytest.mark.asyncio
 async def test_delete_topic_flattened_error_async():
     client = PublisherAsyncClient(credentials=ga_credentials.AnonymousCredentials(),)
 
     # Attempting to call a method with both a request object and flattened
@@ -2641,16 +2658,18 @@
         "get_iam_policy",
         "test_iam_permissions",
     )
     for method in methods:
         with pytest.raises(NotImplementedError):
             getattr(transport, method)(request=object())
 
+    with pytest.raises(NotImplementedError):
+        transport.close()
+
 
-@requires_google_auth_gte_1_25_0
 def test_publisher_base_transport_with_credentials_file():
     # Instantiate the base transport with a credentials file
     with mock.patch.object(
         google.auth, "load_credentials_from_file", autospec=True
     ) as load_creds, mock.patch(
         "google.pubsub_v1.services.publisher.transports.PublisherTransport._prep_wrapped_messages"
     ) as Transport:
@@ -2666,49 +2685,25 @@
                 "https://www.googleapis.com/auth/cloud-platform",
                 "https://www.googleapis.com/auth/pubsub",
             ),
             quota_project_id="octopus",
         )
 
 
-@requires_google_auth_lt_1_25_0
-def test_publisher_base_transport_with_credentials_file_old_google_auth():
-    # Instantiate the base transport with a credentials file
-    with mock.patch.object(
-        google.auth, "load_credentials_from_file", autospec=True
-    ) as load_creds, mock.patch(
-        "google.pubsub_v1.services.publisher.transports.PublisherTransport._prep_wrapped_messages"
-    ) as Transport:
-        Transport.return_value = None
-        load_creds.return_value = (ga_credentials.AnonymousCredentials(), None)
-        transport = transports.PublisherTransport(
-            credentials_file="credentials.json", quota_project_id="octopus",
-        )
-        load_creds.assert_called_once_with(
-            "credentials.json",
-            scopes=(
-                "https://www.googleapis.com/auth/cloud-platform",
-                "https://www.googleapis.com/auth/pubsub",
-            ),
-            quota_project_id="octopus",
-        )
-
-
 def test_publisher_base_transport_with_adc():
     # Test the default credentials are used if credentials and credentials_file are None.
     with mock.patch.object(google.auth, "default", autospec=True) as adc, mock.patch(
         "google.pubsub_v1.services.publisher.transports.PublisherTransport._prep_wrapped_messages"
     ) as Transport:
         Transport.return_value = None
         adc.return_value = (ga_credentials.AnonymousCredentials(), None)
         transport = transports.PublisherTransport()
         adc.assert_called_once()
 
 
-@requires_google_auth_gte_1_25_0
 def test_publisher_auth_adc():
     # If no credentials are provided, we should use ADC credentials.
     with mock.patch.object(google.auth, "default", autospec=True) as adc:
         adc.return_value = (ga_credentials.AnonymousCredentials(), None)
         PublisherClient()
         adc.assert_called_once_with(
             scopes=None,
@@ -2716,34 +2711,18 @@
                 "https://www.googleapis.com/auth/cloud-platform",
                 "https://www.googleapis.com/auth/pubsub",
             ),
             quota_project_id=None,
         )
 
 
-@requires_google_auth_lt_1_25_0
-def test_publisher_auth_adc_old_google_auth():
-    # If no credentials are provided, we should use ADC credentials.
-    with mock.patch.object(google.auth, "default", autospec=True) as adc:
-        adc.return_value = (ga_credentials.AnonymousCredentials(), None)
-        PublisherClient()
-        adc.assert_called_once_with(
-            scopes=(
-                "https://www.googleapis.com/auth/cloud-platform",
-                "https://www.googleapis.com/auth/pubsub",
-            ),
-            quota_project_id=None,
-        )
-
-
 @pytest.mark.parametrize(
     "transport_class",
     [transports.PublisherGrpcTransport, transports.PublisherGrpcAsyncIOTransport,],
 )
-@requires_google_auth_gte_1_25_0
 def test_publisher_transport_auth_adc(transport_class):
     # If credentials and host are not provided, the transport class should use
     # ADC credentials.
     with mock.patch.object(google.auth, "default", autospec=True) as adc:
         adc.return_value = (ga_credentials.AnonymousCredentials(), None)
         transport_class(quota_project_id="octopus", scopes=["1", "2"])
         adc.assert_called_once_with(
@@ -2753,34 +2732,14 @@
                 "https://www.googleapis.com/auth/pubsub",
             ),
             quota_project_id="octopus",
         )
 
 
 @pytest.mark.parametrize(
-    "transport_class",
-    [transports.PublisherGrpcTransport, transports.PublisherGrpcAsyncIOTransport,],
-)
-@requires_google_auth_lt_1_25_0
-def test_publisher_transport_auth_adc_old_google_auth(transport_class):
-    # If credentials and host are not provided, the transport class should use
-    # ADC credentials.
-    with mock.patch.object(google.auth, "default", autospec=True) as adc:
-        adc.return_value = (ga_credentials.AnonymousCredentials(), None)
-        transport_class(quota_project_id="octopus")
-        adc.assert_called_once_with(
-            scopes=(
-                "https://www.googleapis.com/auth/cloud-platform",
-                "https://www.googleapis.com/auth/pubsub",
-            ),
-            quota_project_id="octopus",
-        )
-
-
-@pytest.mark.parametrize(
     "transport_class,grpc_helpers",
     [
         (transports.PublisherGrpcTransport, grpc_helpers),
         (transports.PublisherGrpcAsyncIOTransport, grpc_helpers_async),
     ],
 )
 def test_publisher_transport_create_channel(transport_class, grpc_helpers):
@@ -3622,7 +3581,53 @@
         response = await client.test_iam_permissions(
             request={
                 "resource": "resource_value",
                 "permissions": ["permissions_value"],
             }
         )
         call.assert_called()
+
+
+@pytest.mark.asyncio
+async def test_transport_close_async():
+    client = PublisherAsyncClient(
+        credentials=ga_credentials.AnonymousCredentials(), transport="grpc_asyncio",
+    )
+    with mock.patch.object(
+        type(getattr(client.transport, "grpc_channel")), "close"
+    ) as close:
+        async with client:
+            close.assert_not_called()
+        close.assert_called_once()
+
+
+def test_transport_close():
+    transports = {
+        "grpc": "_grpc_channel",
+    }
+
+    for transport, close_name in transports.items():
+        client = PublisherClient(
+            credentials=ga_credentials.AnonymousCredentials(), transport=transport
+        )
+        with mock.patch.object(
+            type(getattr(client.transport, close_name)), "close"
+        ) as close:
+            with client:
+                close.assert_not_called()
+            close.assert_called_once()
+
+
+def test_client_ctx():
+    transports = [
+        "grpc",
+    ]
+    for transport in transports:
+        client = PublisherClient(
+            credentials=ga_credentials.AnonymousCredentials(), transport=transport
+        )
+        # Test client calls underlying transport.
+        with mock.patch.object(type(client.transport), "close") as close:
+            close.assert_not_called()
+            with client:
+                pass
+            close.assert_called()
```

### Comparing `google-cloud-pubsub-2.8.0/tests/unit/gapic/pubsub_v1/test_schema_service.py` & `google-cloud-pubsub-2.9.0/tests/unit/gapic/pubsub_v1/test_schema_service.py`

 * *Files 0% similar despite different names*

```diff
@@ -11,60 +11,43 @@
 # distributed under the License is distributed on an "AS IS" BASIS,
 # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 # See the License for the specific language governing permissions and
 # limitations under the License.
 #
 import os
 import mock
-import packaging.version
 
 import grpc
 from grpc.experimental import aio
 import math
 import pytest
 from proto.marshal.rules.dates import DurationRule, TimestampRule
 
 
 from google.api_core import client_options
 from google.api_core import exceptions as core_exceptions
 from google.api_core import gapic_v1
 from google.api_core import grpc_helpers
 from google.api_core import grpc_helpers_async
+from google.api_core import path_template
 from google.auth import credentials as ga_credentials
 from google.auth.exceptions import MutualTLSChannelError
 from google.iam.v1 import iam_policy_pb2  # type: ignore
 from google.iam.v1 import options_pb2  # type: ignore
 from google.iam.v1 import policy_pb2  # type: ignore
 from google.oauth2 import service_account
 from google.pubsub_v1.services.schema_service import SchemaServiceAsyncClient
 from google.pubsub_v1.services.schema_service import SchemaServiceClient
 from google.pubsub_v1.services.schema_service import pagers
 from google.pubsub_v1.services.schema_service import transports
-from google.pubsub_v1.services.schema_service.transports.base import (
-    _GOOGLE_AUTH_VERSION,
-)
 from google.pubsub_v1.types import schema
 from google.pubsub_v1.types import schema as gp_schema
 import google.auth
 
 
-# TODO(busunkim): Once google-auth >= 1.25.0 is required transitively
-# through google-api-core:
-# - Delete the auth "less than" test cases
-# - Delete these pytest markers (Make the "greater than or equal to" tests the default).
-requires_google_auth_lt_1_25_0 = pytest.mark.skipif(
-    packaging.version.parse(_GOOGLE_AUTH_VERSION) >= packaging.version.parse("1.25.0"),
-    reason="This test requires google-auth < 1.25.0",
-)
-requires_google_auth_gte_1_25_0 = pytest.mark.skipif(
-    packaging.version.parse(_GOOGLE_AUTH_VERSION) < packaging.version.parse("1.25.0"),
-    reason="This test requires google-auth >= 1.25.0",
-)
-
-
 def client_cert_source_callback():
     return b"cert bytes", b"key bytes"
 
 
 # If default endpoint is localhost, then default mtls endpoint will be the same.
 # This method modifies the default endpoint so the client can produce a different
 # mtls endpoint for endpoint testing purposes.
@@ -213,15 +196,15 @@
         client = client_class(transport=transport_name)
         gtc.assert_called()
 
     # Check the case api_endpoint is provided.
     options = client_options.ClientOptions(api_endpoint="squid.clam.whelk")
     with mock.patch.object(transport_class, "__init__") as patched:
         patched.return_value = None
-        client = client_class(client_options=options)
+        client = client_class(transport=transport_name, client_options=options)
         patched.assert_called_once_with(
             credentials=None,
             credentials_file=None,
             host="squid.clam.whelk",
             scopes=None,
             client_cert_source_for_mtls=None,
             quota_project_id=None,
@@ -230,15 +213,15 @@
         )
 
     # Check the case api_endpoint is not provided and GOOGLE_API_USE_MTLS_ENDPOINT is
     # "never".
     with mock.patch.dict(os.environ, {"GOOGLE_API_USE_MTLS_ENDPOINT": "never"}):
         with mock.patch.object(transport_class, "__init__") as patched:
             patched.return_value = None
-            client = client_class()
+            client = client_class(transport=transport_name)
             patched.assert_called_once_with(
                 credentials=None,
                 credentials_file=None,
                 host=client.DEFAULT_ENDPOINT,
                 scopes=None,
                 client_cert_source_for_mtls=None,
                 quota_project_id=None,
@@ -247,15 +230,15 @@
             )
 
     # Check the case api_endpoint is not provided and GOOGLE_API_USE_MTLS_ENDPOINT is
     # "always".
     with mock.patch.dict(os.environ, {"GOOGLE_API_USE_MTLS_ENDPOINT": "always"}):
         with mock.patch.object(transport_class, "__init__") as patched:
             patched.return_value = None
-            client = client_class()
+            client = client_class(transport=transport_name)
             patched.assert_called_once_with(
                 credentials=None,
                 credentials_file=None,
                 host=client.DEFAULT_MTLS_ENDPOINT,
                 scopes=None,
                 client_cert_source_for_mtls=None,
                 quota_project_id=None,
@@ -276,15 +259,15 @@
         with pytest.raises(ValueError):
             client = client_class()
 
     # Check the case quota_project_id is provided
     options = client_options.ClientOptions(quota_project_id="octopus")
     with mock.patch.object(transport_class, "__init__") as patched:
         patched.return_value = None
-        client = client_class(client_options=options)
+        client = client_class(transport=transport_name, client_options=options)
         patched.assert_called_once_with(
             credentials=None,
             credentials_file=None,
             host=client.DEFAULT_ENDPOINT,
             scopes=None,
             client_cert_source_for_mtls=None,
             quota_project_id="octopus",
@@ -335,15 +318,15 @@
         os.environ, {"GOOGLE_API_USE_CLIENT_CERTIFICATE": use_client_cert_env}
     ):
         options = client_options.ClientOptions(
             client_cert_source=client_cert_source_callback
         )
         with mock.patch.object(transport_class, "__init__") as patched:
             patched.return_value = None
-            client = client_class(client_options=options)
+            client = client_class(transport=transport_name, client_options=options)
 
             if use_client_cert_env == "false":
                 expected_client_cert_source = None
                 expected_host = client.DEFAULT_ENDPOINT
             else:
                 expected_client_cert_source = client_cert_source_callback
                 expected_host = client.DEFAULT_MTLS_ENDPOINT
@@ -377,15 +360,15 @@
                         expected_host = client.DEFAULT_ENDPOINT
                         expected_client_cert_source = None
                     else:
                         expected_host = client.DEFAULT_MTLS_ENDPOINT
                         expected_client_cert_source = client_cert_source_callback
 
                     patched.return_value = None
-                    client = client_class()
+                    client = client_class(transport=transport_name)
                     patched.assert_called_once_with(
                         credentials=None,
                         credentials_file=None,
                         host=expected_host,
                         scopes=None,
                         client_cert_source_for_mtls=expected_client_cert_source,
                         quota_project_id=None,
@@ -399,15 +382,15 @@
     ):
         with mock.patch.object(transport_class, "__init__") as patched:
             with mock.patch(
                 "google.auth.transport.mtls.has_default_client_cert_source",
                 return_value=False,
             ):
                 patched.return_value = None
-                client = client_class()
+                client = client_class(transport=transport_name)
                 patched.assert_called_once_with(
                     credentials=None,
                     credentials_file=None,
                     host=client.DEFAULT_ENDPOINT,
                     scopes=None,
                     client_cert_source_for_mtls=None,
                     quota_project_id=None,
@@ -430,15 +413,15 @@
 def test_schema_service_client_client_options_scopes(
     client_class, transport_class, transport_name
 ):
     # Check the case scopes are provided.
     options = client_options.ClientOptions(scopes=["1", "2"],)
     with mock.patch.object(transport_class, "__init__") as patched:
         patched.return_value = None
-        client = client_class(client_options=options)
+        client = client_class(transport=transport_name, client_options=options)
         patched.assert_called_once_with(
             credentials=None,
             credentials_file=None,
             host=client.DEFAULT_ENDPOINT,
             scopes=["1", "2"],
             client_cert_source_for_mtls=None,
             quota_project_id=None,
@@ -461,15 +444,15 @@
 def test_schema_service_client_client_options_credentials_file(
     client_class, transport_class, transport_name
 ):
     # Check the case credentials file is provided.
     options = client_options.ClientOptions(credentials_file="credentials.json")
     with mock.patch.object(transport_class, "__init__") as patched:
         patched.return_value = None
-        client = client_class(client_options=options)
+        client = client_class(transport=transport_name, client_options=options)
         patched.assert_called_once_with(
             credentials=None,
             credentials_file="credentials.json",
             host=client.DEFAULT_ENDPOINT,
             scopes=None,
             client_cert_source_for_mtls=None,
             quota_project_id=None,
@@ -657,17 +640,23 @@
             schema_id="schema_id_value",
         )
 
         # Establish that the underlying call was made with the expected
         # request object values.
         assert len(call.mock_calls) == 1
         _, args, _ = call.mock_calls[0]
-        assert args[0].parent == "parent_value"
-        assert args[0].schema == gp_schema.Schema(name="name_value")
-        assert args[0].schema_id == "schema_id_value"
+        arg = args[0].parent
+        mock_val = "parent_value"
+        assert arg == mock_val
+        arg = args[0].schema
+        mock_val = gp_schema.Schema(name="name_value")
+        assert arg == mock_val
+        arg = args[0].schema_id
+        mock_val = "schema_id_value"
+        assert arg == mock_val
 
 
 def test_create_schema_flattened_error():
     client = SchemaServiceClient(credentials=ga_credentials.AnonymousCredentials(),)
 
     # Attempting to call a method with both a request object and flattened
     # fields is an error.
@@ -700,17 +689,23 @@
             schema_id="schema_id_value",
         )
 
         # Establish that the underlying call was made with the expected
         # request object values.
         assert len(call.mock_calls)
         _, args, _ = call.mock_calls[0]
-        assert args[0].parent == "parent_value"
-        assert args[0].schema == gp_schema.Schema(name="name_value")
-        assert args[0].schema_id == "schema_id_value"
+        arg = args[0].parent
+        mock_val = "parent_value"
+        assert arg == mock_val
+        arg = args[0].schema
+        mock_val = gp_schema.Schema(name="name_value")
+        assert arg == mock_val
+        arg = args[0].schema_id
+        mock_val = "schema_id_value"
+        assert arg == mock_val
 
 
 @pytest.mark.asyncio
 async def test_create_schema_flattened_error_async():
     client = SchemaServiceAsyncClient(
         credentials=ga_credentials.AnonymousCredentials(),
     )
@@ -879,15 +874,17 @@
         # using the keyword arguments to the method.
         client.get_schema(name="name_value",)
 
         # Establish that the underlying call was made with the expected
         # request object values.
         assert len(call.mock_calls) == 1
         _, args, _ = call.mock_calls[0]
-        assert args[0].name == "name_value"
+        arg = args[0].name
+        mock_val = "name_value"
+        assert arg == mock_val
 
 
 def test_get_schema_flattened_error():
     client = SchemaServiceClient(credentials=ga_credentials.AnonymousCredentials(),)
 
     # Attempting to call a method with both a request object and flattened
     # fields is an error.
@@ -913,15 +910,17 @@
         # using the keyword arguments to the method.
         response = await client.get_schema(name="name_value",)
 
         # Establish that the underlying call was made with the expected
         # request object values.
         assert len(call.mock_calls)
         _, args, _ = call.mock_calls[0]
-        assert args[0].name == "name_value"
+        arg = args[0].name
+        mock_val = "name_value"
+        assert arg == mock_val
 
 
 @pytest.mark.asyncio
 async def test_get_schema_flattened_error_async():
     client = SchemaServiceAsyncClient(
         credentials=ga_credentials.AnonymousCredentials(),
     )
@@ -1079,15 +1078,17 @@
         # using the keyword arguments to the method.
         client.list_schemas(parent="parent_value",)
 
         # Establish that the underlying call was made with the expected
         # request object values.
         assert len(call.mock_calls) == 1
         _, args, _ = call.mock_calls[0]
-        assert args[0].parent == "parent_value"
+        arg = args[0].parent
+        mock_val = "parent_value"
+        assert arg == mock_val
 
 
 def test_list_schemas_flattened_error():
     client = SchemaServiceClient(credentials=ga_credentials.AnonymousCredentials(),)
 
     # Attempting to call a method with both a request object and flattened
     # fields is an error.
@@ -1115,15 +1116,17 @@
         # using the keyword arguments to the method.
         response = await client.list_schemas(parent="parent_value",)
 
         # Establish that the underlying call was made with the expected
         # request object values.
         assert len(call.mock_calls)
         _, args, _ = call.mock_calls[0]
-        assert args[0].parent == "parent_value"
+        arg = args[0].parent
+        mock_val = "parent_value"
+        assert arg == mock_val
 
 
 @pytest.mark.asyncio
 async def test_list_schemas_flattened_error_async():
     client = SchemaServiceAsyncClient(
         credentials=ga_credentials.AnonymousCredentials(),
     )
@@ -1389,15 +1392,17 @@
         # using the keyword arguments to the method.
         client.delete_schema(name="name_value",)
 
         # Establish that the underlying call was made with the expected
         # request object values.
         assert len(call.mock_calls) == 1
         _, args, _ = call.mock_calls[0]
-        assert args[0].name == "name_value"
+        arg = args[0].name
+        mock_val = "name_value"
+        assert arg == mock_val
 
 
 def test_delete_schema_flattened_error():
     client = SchemaServiceClient(credentials=ga_credentials.AnonymousCredentials(),)
 
     # Attempting to call a method with both a request object and flattened
     # fields is an error.
@@ -1423,15 +1428,17 @@
         # using the keyword arguments to the method.
         response = await client.delete_schema(name="name_value",)
 
         # Establish that the underlying call was made with the expected
         # request object values.
         assert len(call.mock_calls)
         _, args, _ = call.mock_calls[0]
-        assert args[0].name == "name_value"
+        arg = args[0].name
+        mock_val = "name_value"
+        assert arg == mock_val
 
 
 @pytest.mark.asyncio
 async def test_delete_schema_flattened_error_async():
     client = SchemaServiceAsyncClient(
         credentials=ga_credentials.AnonymousCredentials(),
     )
@@ -1589,16 +1596,20 @@
             parent="parent_value", schema=gp_schema.Schema(name="name_value"),
         )
 
         # Establish that the underlying call was made with the expected
         # request object values.
         assert len(call.mock_calls) == 1
         _, args, _ = call.mock_calls[0]
-        assert args[0].parent == "parent_value"
-        assert args[0].schema == gp_schema.Schema(name="name_value")
+        arg = args[0].parent
+        mock_val = "parent_value"
+        assert arg == mock_val
+        arg = args[0].schema
+        mock_val = gp_schema.Schema(name="name_value")
+        assert arg == mock_val
 
 
 def test_validate_schema_flattened_error():
     client = SchemaServiceClient(credentials=ga_credentials.AnonymousCredentials(),)
 
     # Attempting to call a method with both a request object and flattened
     # fields is an error.
@@ -1630,16 +1641,20 @@
             parent="parent_value", schema=gp_schema.Schema(name="name_value"),
         )
 
         # Establish that the underlying call was made with the expected
         # request object values.
         assert len(call.mock_calls)
         _, args, _ = call.mock_calls[0]
-        assert args[0].parent == "parent_value"
-        assert args[0].schema == gp_schema.Schema(name="name_value")
+        arg = args[0].parent
+        mock_val = "parent_value"
+        assert arg == mock_val
+        arg = args[0].schema
+        mock_val = gp_schema.Schema(name="name_value")
+        assert arg == mock_val
 
 
 @pytest.mark.asyncio
 async def test_validate_schema_flattened_error_async():
     client = SchemaServiceAsyncClient(
         credentials=ga_credentials.AnonymousCredentials(),
     )
@@ -1893,16 +1908,18 @@
         "get_iam_policy",
         "test_iam_permissions",
     )
     for method in methods:
         with pytest.raises(NotImplementedError):
             getattr(transport, method)(request=object())
 
+    with pytest.raises(NotImplementedError):
+        transport.close()
+
 
-@requires_google_auth_gte_1_25_0
 def test_schema_service_base_transport_with_credentials_file():
     # Instantiate the base transport with a credentials file
     with mock.patch.object(
         google.auth, "load_credentials_from_file", autospec=True
     ) as load_creds, mock.patch(
         "google.pubsub_v1.services.schema_service.transports.SchemaServiceTransport._prep_wrapped_messages"
     ) as Transport:
@@ -1918,49 +1935,25 @@
                 "https://www.googleapis.com/auth/cloud-platform",
                 "https://www.googleapis.com/auth/pubsub",
             ),
             quota_project_id="octopus",
         )
 
 
-@requires_google_auth_lt_1_25_0
-def test_schema_service_base_transport_with_credentials_file_old_google_auth():
-    # Instantiate the base transport with a credentials file
-    with mock.patch.object(
-        google.auth, "load_credentials_from_file", autospec=True
-    ) as load_creds, mock.patch(
-        "google.pubsub_v1.services.schema_service.transports.SchemaServiceTransport._prep_wrapped_messages"
-    ) as Transport:
-        Transport.return_value = None
-        load_creds.return_value = (ga_credentials.AnonymousCredentials(), None)
-        transport = transports.SchemaServiceTransport(
-            credentials_file="credentials.json", quota_project_id="octopus",
-        )
-        load_creds.assert_called_once_with(
-            "credentials.json",
-            scopes=(
-                "https://www.googleapis.com/auth/cloud-platform",
-                "https://www.googleapis.com/auth/pubsub",
-            ),
-            quota_project_id="octopus",
-        )
-
-
 def test_schema_service_base_transport_with_adc():
     # Test the default credentials are used if credentials and credentials_file are None.
     with mock.patch.object(google.auth, "default", autospec=True) as adc, mock.patch(
         "google.pubsub_v1.services.schema_service.transports.SchemaServiceTransport._prep_wrapped_messages"
     ) as Transport:
         Transport.return_value = None
         adc.return_value = (ga_credentials.AnonymousCredentials(), None)
         transport = transports.SchemaServiceTransport()
         adc.assert_called_once()
 
 
-@requires_google_auth_gte_1_25_0
 def test_schema_service_auth_adc():
     # If no credentials are provided, we should use ADC credentials.
     with mock.patch.object(google.auth, "default", autospec=True) as adc:
         adc.return_value = (ga_credentials.AnonymousCredentials(), None)
         SchemaServiceClient()
         adc.assert_called_once_with(
             scopes=None,
@@ -1968,37 +1961,21 @@
                 "https://www.googleapis.com/auth/cloud-platform",
                 "https://www.googleapis.com/auth/pubsub",
             ),
             quota_project_id=None,
         )
 
 
-@requires_google_auth_lt_1_25_0
-def test_schema_service_auth_adc_old_google_auth():
-    # If no credentials are provided, we should use ADC credentials.
-    with mock.patch.object(google.auth, "default", autospec=True) as adc:
-        adc.return_value = (ga_credentials.AnonymousCredentials(), None)
-        SchemaServiceClient()
-        adc.assert_called_once_with(
-            scopes=(
-                "https://www.googleapis.com/auth/cloud-platform",
-                "https://www.googleapis.com/auth/pubsub",
-            ),
-            quota_project_id=None,
-        )
-
-
 @pytest.mark.parametrize(
     "transport_class",
     [
         transports.SchemaServiceGrpcTransport,
         transports.SchemaServiceGrpcAsyncIOTransport,
     ],
 )
-@requires_google_auth_gte_1_25_0
 def test_schema_service_transport_auth_adc(transport_class):
     # If credentials and host are not provided, the transport class should use
     # ADC credentials.
     with mock.patch.object(google.auth, "default", autospec=True) as adc:
         adc.return_value = (ga_credentials.AnonymousCredentials(), None)
         transport_class(quota_project_id="octopus", scopes=["1", "2"])
         adc.assert_called_once_with(
@@ -2008,37 +1985,14 @@
                 "https://www.googleapis.com/auth/pubsub",
             ),
             quota_project_id="octopus",
         )
 
 
 @pytest.mark.parametrize(
-    "transport_class",
-    [
-        transports.SchemaServiceGrpcTransport,
-        transports.SchemaServiceGrpcAsyncIOTransport,
-    ],
-)
-@requires_google_auth_lt_1_25_0
-def test_schema_service_transport_auth_adc_old_google_auth(transport_class):
-    # If credentials and host are not provided, the transport class should use
-    # ADC credentials.
-    with mock.patch.object(google.auth, "default", autospec=True) as adc:
-        adc.return_value = (ga_credentials.AnonymousCredentials(), None)
-        transport_class(quota_project_id="octopus")
-        adc.assert_called_once_with(
-            scopes=(
-                "https://www.googleapis.com/auth/cloud-platform",
-                "https://www.googleapis.com/auth/pubsub",
-            ),
-            quota_project_id="octopus",
-        )
-
-
-@pytest.mark.parametrize(
     "transport_class,grpc_helpers",
     [
         (transports.SchemaServiceGrpcTransport, grpc_helpers),
         (transports.SchemaServiceGrpcAsyncIOTransport, grpc_helpers_async),
     ],
 )
 def test_schema_service_transport_create_channel(transport_class, grpc_helpers):
@@ -2859,7 +2813,53 @@
         response = await client.test_iam_permissions(
             request={
                 "resource": "resource_value",
                 "permissions": ["permissions_value"],
             }
         )
         call.assert_called()
+
+
+@pytest.mark.asyncio
+async def test_transport_close_async():
+    client = SchemaServiceAsyncClient(
+        credentials=ga_credentials.AnonymousCredentials(), transport="grpc_asyncio",
+    )
+    with mock.patch.object(
+        type(getattr(client.transport, "grpc_channel")), "close"
+    ) as close:
+        async with client:
+            close.assert_not_called()
+        close.assert_called_once()
+
+
+def test_transport_close():
+    transports = {
+        "grpc": "_grpc_channel",
+    }
+
+    for transport, close_name in transports.items():
+        client = SchemaServiceClient(
+            credentials=ga_credentials.AnonymousCredentials(), transport=transport
+        )
+        with mock.patch.object(
+            type(getattr(client.transport, close_name)), "close"
+        ) as close:
+            with client:
+                close.assert_not_called()
+            close.assert_called_once()
+
+
+def test_client_ctx():
+    transports = [
+        "grpc",
+    ]
+    for transport in transports:
+        client = SchemaServiceClient(
+            credentials=ga_credentials.AnonymousCredentials(), transport=transport
+        )
+        # Test client calls underlying transport.
+        with mock.patch.object(type(client.transport), "close") as close:
+            close.assert_not_called()
+            with client:
+                pass
+            close.assert_called()
```

### Comparing `google-cloud-pubsub-2.8.0/tests/unit/gapic/pubsub_v1/test_subscriber.py` & `google-cloud-pubsub-2.9.0/tests/unit/gapic/pubsub_v1/test_subscriber.py`

 * *Files 4% similar despite different names*

```diff
@@ -12,60 +12,45 @@
 # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 # See the License for the specific language governing permissions and
 # limitations under the License.
 #
 import os
 import mock
 import warnings
-import packaging.version
 
 import grpc
 from grpc.experimental import aio
 import math
 import pytest
 from proto.marshal.rules.dates import DurationRule, TimestampRule
 
 
 from google.api_core import client_options
 from google.api_core import exceptions as core_exceptions
 from google.api_core import gapic_v1
 from google.api_core import grpc_helpers
 from google.api_core import grpc_helpers_async
+from google.api_core import path_template
 from google.auth import credentials as ga_credentials
 from google.auth.exceptions import MutualTLSChannelError
 from google.iam.v1 import iam_policy_pb2  # type: ignore
 from google.iam.v1 import options_pb2  # type: ignore
 from google.iam.v1 import policy_pb2  # type: ignore
 from google.oauth2 import service_account
 from google.protobuf import duration_pb2  # type: ignore
 from google.protobuf import field_mask_pb2  # type: ignore
 from google.protobuf import timestamp_pb2  # type: ignore
 from google.pubsub_v1.services.subscriber import SubscriberAsyncClient
 from google.pubsub_v1.services.subscriber import SubscriberClient
 from google.pubsub_v1.services.subscriber import pagers
 from google.pubsub_v1.services.subscriber import transports
-from google.pubsub_v1.services.subscriber.transports.base import _GOOGLE_AUTH_VERSION
 from google.pubsub_v1.types import pubsub
 import google.auth
 
 
-# TODO(busunkim): Once google-auth >= 1.25.0 is required transitively
-# through google-api-core:
-# - Delete the auth "less than" test cases
-# - Delete these pytest markers (Make the "greater than or equal to" tests the default).
-requires_google_auth_lt_1_25_0 = pytest.mark.skipif(
-    packaging.version.parse(_GOOGLE_AUTH_VERSION) >= packaging.version.parse("1.25.0"),
-    reason="This test requires google-auth < 1.25.0",
-)
-requires_google_auth_gte_1_25_0 = pytest.mark.skipif(
-    packaging.version.parse(_GOOGLE_AUTH_VERSION) < packaging.version.parse("1.25.0"),
-    reason="This test requires google-auth >= 1.25.0",
-)
-
-
 def client_cert_source_callback():
     return b"cert bytes", b"key bytes"
 
 
 # If default endpoint is localhost, then default mtls endpoint will be the same.
 # This method modifies the default endpoint so the client can produce a different
 # mtls endpoint for endpoint testing purposes.
@@ -205,15 +190,15 @@
         client = client_class(transport=transport_name)
         gtc.assert_called()
 
     # Check the case api_endpoint is provided.
     options = client_options.ClientOptions(api_endpoint="squid.clam.whelk")
     with mock.patch.object(transport_class, "__init__") as patched:
         patched.return_value = None
-        client = client_class(client_options=options)
+        client = client_class(transport=transport_name, client_options=options)
         patched.assert_called_once_with(
             credentials=None,
             credentials_file=None,
             host="squid.clam.whelk",
             scopes=None,
             client_cert_source_for_mtls=None,
             quota_project_id=None,
@@ -222,15 +207,15 @@
         )
 
     # Check the case api_endpoint is not provided and GOOGLE_API_USE_MTLS_ENDPOINT is
     # "never".
     with mock.patch.dict(os.environ, {"GOOGLE_API_USE_MTLS_ENDPOINT": "never"}):
         with mock.patch.object(transport_class, "__init__") as patched:
             patched.return_value = None
-            client = client_class()
+            client = client_class(transport=transport_name)
             patched.assert_called_once_with(
                 credentials=None,
                 credentials_file=None,
                 host=client.DEFAULT_ENDPOINT,
                 scopes=None,
                 client_cert_source_for_mtls=None,
                 quota_project_id=None,
@@ -239,15 +224,15 @@
             )
 
     # Check the case api_endpoint is not provided and GOOGLE_API_USE_MTLS_ENDPOINT is
     # "always".
     with mock.patch.dict(os.environ, {"GOOGLE_API_USE_MTLS_ENDPOINT": "always"}):
         with mock.patch.object(transport_class, "__init__") as patched:
             patched.return_value = None
-            client = client_class()
+            client = client_class(transport=transport_name)
             patched.assert_called_once_with(
                 credentials=None,
                 credentials_file=None,
                 host=client.DEFAULT_MTLS_ENDPOINT,
                 scopes=None,
                 client_cert_source_for_mtls=None,
                 quota_project_id=None,
@@ -268,15 +253,15 @@
         with pytest.raises(ValueError):
             client = client_class()
 
     # Check the case quota_project_id is provided
     options = client_options.ClientOptions(quota_project_id="octopus")
     with mock.patch.object(transport_class, "__init__") as patched:
         patched.return_value = None
-        client = client_class(client_options=options)
+        client = client_class(transport=transport_name, client_options=options)
         patched.assert_called_once_with(
             credentials=None,
             credentials_file=None,
             host=client.DEFAULT_ENDPOINT,
             scopes=None,
             client_cert_source_for_mtls=None,
             quota_project_id="octopus",
@@ -325,15 +310,15 @@
         os.environ, {"GOOGLE_API_USE_CLIENT_CERTIFICATE": use_client_cert_env}
     ):
         options = client_options.ClientOptions(
             client_cert_source=client_cert_source_callback
         )
         with mock.patch.object(transport_class, "__init__") as patched:
             patched.return_value = None
-            client = client_class(client_options=options)
+            client = client_class(transport=transport_name, client_options=options)
 
             if use_client_cert_env == "false":
                 expected_client_cert_source = None
                 expected_host = client.DEFAULT_ENDPOINT
             else:
                 expected_client_cert_source = client_cert_source_callback
                 expected_host = client.DEFAULT_MTLS_ENDPOINT
@@ -367,15 +352,15 @@
                         expected_host = client.DEFAULT_ENDPOINT
                         expected_client_cert_source = None
                     else:
                         expected_host = client.DEFAULT_MTLS_ENDPOINT
                         expected_client_cert_source = client_cert_source_callback
 
                     patched.return_value = None
-                    client = client_class()
+                    client = client_class(transport=transport_name)
                     patched.assert_called_once_with(
                         credentials=None,
                         credentials_file=None,
                         host=expected_host,
                         scopes=None,
                         client_cert_source_for_mtls=expected_client_cert_source,
                         quota_project_id=None,
@@ -389,15 +374,15 @@
     ):
         with mock.patch.object(transport_class, "__init__") as patched:
             with mock.patch(
                 "google.auth.transport.mtls.has_default_client_cert_source",
                 return_value=False,
             ):
                 patched.return_value = None
-                client = client_class()
+                client = client_class(transport=transport_name)
                 patched.assert_called_once_with(
                     credentials=None,
                     credentials_file=None,
                     host=client.DEFAULT_ENDPOINT,
                     scopes=None,
                     client_cert_source_for_mtls=None,
                     quota_project_id=None,
@@ -420,15 +405,15 @@
 def test_subscriber_client_client_options_scopes(
     client_class, transport_class, transport_name
 ):
     # Check the case scopes are provided.
     options = client_options.ClientOptions(scopes=["1", "2"],)
     with mock.patch.object(transport_class, "__init__") as patched:
         patched.return_value = None
-        client = client_class(client_options=options)
+        client = client_class(transport=transport_name, client_options=options)
         patched.assert_called_once_with(
             credentials=None,
             credentials_file=None,
             host=client.DEFAULT_ENDPOINT,
             scopes=["1", "2"],
             client_cert_source_for_mtls=None,
             quota_project_id=None,
@@ -451,15 +436,15 @@
 def test_subscriber_client_client_options_credentials_file(
     client_class, transport_class, transport_name
 ):
     # Check the case credentials file is provided.
     options = client_options.ClientOptions(credentials_file="credentials.json")
     with mock.patch.object(transport_class, "__init__") as patched:
         patched.return_value = None
-        client = client_class(client_options=options)
+        client = client_class(transport=transport_name, client_options=options)
         patched.assert_called_once_with(
             credentials=None,
             credentials_file="credentials.json",
             host=client.DEFAULT_ENDPOINT,
             scopes=None,
             client_cert_source_for_mtls=None,
             quota_project_id=None,
@@ -670,20 +655,26 @@
             ack_deadline_seconds=2066,
         )
 
         # Establish that the underlying call was made with the expected
         # request object values.
         assert len(call.mock_calls) == 1
         _, args, _ = call.mock_calls[0]
-        assert args[0].name == "name_value"
-        assert args[0].topic == "topic_value"
-        assert args[0].push_config == pubsub.PushConfig(
-            push_endpoint="push_endpoint_value"
-        )
-        assert args[0].ack_deadline_seconds == 2066
+        arg = args[0].name
+        mock_val = "name_value"
+        assert arg == mock_val
+        arg = args[0].topic
+        mock_val = "topic_value"
+        assert arg == mock_val
+        arg = args[0].push_config
+        mock_val = pubsub.PushConfig(push_endpoint="push_endpoint_value")
+        assert arg == mock_val
+        arg = args[0].ack_deadline_seconds
+        mock_val = 2066
+        assert arg == mock_val
 
 
 def test_create_subscription_flattened_error():
     client = SubscriberClient(credentials=ga_credentials.AnonymousCredentials(),)
 
     # Attempting to call a method with both a request object and flattened
     # fields is an error.
@@ -718,20 +709,26 @@
             ack_deadline_seconds=2066,
         )
 
         # Establish that the underlying call was made with the expected
         # request object values.
         assert len(call.mock_calls)
         _, args, _ = call.mock_calls[0]
-        assert args[0].name == "name_value"
-        assert args[0].topic == "topic_value"
-        assert args[0].push_config == pubsub.PushConfig(
-            push_endpoint="push_endpoint_value"
-        )
-        assert args[0].ack_deadline_seconds == 2066
+        arg = args[0].name
+        mock_val = "name_value"
+        assert arg == mock_val
+        arg = args[0].topic
+        mock_val = "topic_value"
+        assert arg == mock_val
+        arg = args[0].push_config
+        mock_val = pubsub.PushConfig(push_endpoint="push_endpoint_value")
+        assert arg == mock_val
+        arg = args[0].ack_deadline_seconds
+        mock_val = 2066
+        assert arg == mock_val
 
 
 @pytest.mark.asyncio
 async def test_create_subscription_flattened_error_async():
     client = SubscriberAsyncClient(credentials=ga_credentials.AnonymousCredentials(),)
 
     # Attempting to call a method with both a request object and flattened
@@ -919,15 +916,17 @@
         # using the keyword arguments to the method.
         client.get_subscription(subscription="subscription_value",)
 
         # Establish that the underlying call was made with the expected
         # request object values.
         assert len(call.mock_calls) == 1
         _, args, _ = call.mock_calls[0]
-        assert args[0].subscription == "subscription_value"
+        arg = args[0].subscription
+        mock_val = "subscription_value"
+        assert arg == mock_val
 
 
 def test_get_subscription_flattened_error():
     client = SubscriberClient(credentials=ga_credentials.AnonymousCredentials(),)
 
     # Attempting to call a method with both a request object and flattened
     # fields is an error.
@@ -951,15 +950,17 @@
         # using the keyword arguments to the method.
         response = await client.get_subscription(subscription="subscription_value",)
 
         # Establish that the underlying call was made with the expected
         # request object values.
         assert len(call.mock_calls)
         _, args, _ = call.mock_calls[0]
-        assert args[0].subscription == "subscription_value"
+        arg = args[0].subscription
+        mock_val = "subscription_value"
+        assert arg == mock_val
 
 
 @pytest.mark.asyncio
 async def test_get_subscription_flattened_error_async():
     client = SubscriberAsyncClient(credentials=ga_credentials.AnonymousCredentials(),)
 
     # Attempting to call a method with both a request object and flattened
@@ -1301,15 +1302,17 @@
         # using the keyword arguments to the method.
         client.list_subscriptions(project="project_value",)
 
         # Establish that the underlying call was made with the expected
         # request object values.
         assert len(call.mock_calls) == 1
         _, args, _ = call.mock_calls[0]
-        assert args[0].project == "project_value"
+        arg = args[0].project
+        mock_val = "project_value"
+        assert arg == mock_val
 
 
 def test_list_subscriptions_flattened_error():
     client = SubscriberClient(credentials=ga_credentials.AnonymousCredentials(),)
 
     # Attempting to call a method with both a request object and flattened
     # fields is an error.
@@ -1337,15 +1340,17 @@
         # using the keyword arguments to the method.
         response = await client.list_subscriptions(project="project_value",)
 
         # Establish that the underlying call was made with the expected
         # request object values.
         assert len(call.mock_calls)
         _, args, _ = call.mock_calls[0]
-        assert args[0].project == "project_value"
+        arg = args[0].project
+        mock_val = "project_value"
+        assert arg == mock_val
 
 
 @pytest.mark.asyncio
 async def test_list_subscriptions_flattened_error_async():
     client = SubscriberAsyncClient(credentials=ga_credentials.AnonymousCredentials(),)
 
     # Attempting to call a method with both a request object and flattened
@@ -1655,15 +1660,17 @@
         # using the keyword arguments to the method.
         client.delete_subscription(subscription="subscription_value",)
 
         # Establish that the underlying call was made with the expected
         # request object values.
         assert len(call.mock_calls) == 1
         _, args, _ = call.mock_calls[0]
-        assert args[0].subscription == "subscription_value"
+        arg = args[0].subscription
+        mock_val = "subscription_value"
+        assert arg == mock_val
 
 
 def test_delete_subscription_flattened_error():
     client = SubscriberClient(credentials=ga_credentials.AnonymousCredentials(),)
 
     # Attempting to call a method with both a request object and flattened
     # fields is an error.
@@ -1689,15 +1696,17 @@
         # using the keyword arguments to the method.
         response = await client.delete_subscription(subscription="subscription_value",)
 
         # Establish that the underlying call was made with the expected
         # request object values.
         assert len(call.mock_calls)
         _, args, _ = call.mock_calls[0]
-        assert args[0].subscription == "subscription_value"
+        arg = args[0].subscription
+        mock_val = "subscription_value"
+        assert arg == mock_val
 
 
 @pytest.mark.asyncio
 async def test_delete_subscription_flattened_error_async():
     client = SubscriberAsyncClient(credentials=ga_credentials.AnonymousCredentials(),)
 
     # Attempting to call a method with both a request object and flattened
@@ -1865,17 +1874,23 @@
             ack_deadline_seconds=2066,
         )
 
         # Establish that the underlying call was made with the expected
         # request object values.
         assert len(call.mock_calls) == 1
         _, args, _ = call.mock_calls[0]
-        assert args[0].subscription == "subscription_value"
-        assert args[0].ack_ids == ["ack_ids_value"]
-        assert args[0].ack_deadline_seconds == 2066
+        arg = args[0].subscription
+        mock_val = "subscription_value"
+        assert arg == mock_val
+        arg = args[0].ack_ids
+        mock_val = ["ack_ids_value"]
+        assert arg == mock_val
+        arg = args[0].ack_deadline_seconds
+        mock_val = 2066
+        assert arg == mock_val
 
 
 def test_modify_ack_deadline_flattened_error():
     client = SubscriberClient(credentials=ga_credentials.AnonymousCredentials(),)
 
     # Attempting to call a method with both a request object and flattened
     # fields is an error.
@@ -1908,17 +1923,23 @@
             ack_deadline_seconds=2066,
         )
 
         # Establish that the underlying call was made with the expected
         # request object values.
         assert len(call.mock_calls)
         _, args, _ = call.mock_calls[0]
-        assert args[0].subscription == "subscription_value"
-        assert args[0].ack_ids == ["ack_ids_value"]
-        assert args[0].ack_deadline_seconds == 2066
+        arg = args[0].subscription
+        mock_val = "subscription_value"
+        assert arg == mock_val
+        arg = args[0].ack_ids
+        mock_val = ["ack_ids_value"]
+        assert arg == mock_val
+        arg = args[0].ack_deadline_seconds
+        mock_val = 2066
+        assert arg == mock_val
 
 
 @pytest.mark.asyncio
 async def test_modify_ack_deadline_flattened_error_async():
     client = SubscriberAsyncClient(credentials=ga_credentials.AnonymousCredentials(),)
 
     # Attempting to call a method with both a request object and flattened
@@ -2073,16 +2094,20 @@
             subscription="subscription_value", ack_ids=["ack_ids_value"],
         )
 
         # Establish that the underlying call was made with the expected
         # request object values.
         assert len(call.mock_calls) == 1
         _, args, _ = call.mock_calls[0]
-        assert args[0].subscription == "subscription_value"
-        assert args[0].ack_ids == ["ack_ids_value"]
+        arg = args[0].subscription
+        mock_val = "subscription_value"
+        assert arg == mock_val
+        arg = args[0].ack_ids
+        mock_val = ["ack_ids_value"]
+        assert arg == mock_val
 
 
 def test_acknowledge_flattened_error():
     client = SubscriberClient(credentials=ga_credentials.AnonymousCredentials(),)
 
     # Attempting to call a method with both a request object and flattened
     # fields is an error.
@@ -2110,16 +2135,20 @@
             subscription="subscription_value", ack_ids=["ack_ids_value"],
         )
 
         # Establish that the underlying call was made with the expected
         # request object values.
         assert len(call.mock_calls)
         _, args, _ = call.mock_calls[0]
-        assert args[0].subscription == "subscription_value"
-        assert args[0].ack_ids == ["ack_ids_value"]
+        arg = args[0].subscription
+        mock_val = "subscription_value"
+        assert arg == mock_val
+        arg = args[0].ack_ids
+        mock_val = ["ack_ids_value"]
+        assert arg == mock_val
 
 
 @pytest.mark.asyncio
 async def test_acknowledge_flattened_error_async():
     client = SubscriberAsyncClient(credentials=ga_credentials.AnonymousCredentials(),)
 
     # Attempting to call a method with both a request object and flattened
@@ -2277,17 +2306,23 @@
                 max_messages=1277,
             )
 
         # Establish that the underlying call was made with the expected
         # request object values.
         assert len(call.mock_calls) == 1
         _, args, _ = call.mock_calls[0]
-        assert args[0].subscription == "subscription_value"
-        assert args[0].return_immediately == True
-        assert args[0].max_messages == 1277
+        arg = args[0].subscription
+        mock_val = "subscription_value"
+        assert arg == mock_val
+        arg = args[0].return_immediately
+        mock_val = True
+        assert arg == mock_val
+        arg = args[0].max_messages
+        mock_val = 1277
+        assert arg == mock_val
 
 
 def test_pull_flattened_error():
     client = SubscriberClient(credentials=ga_credentials.AnonymousCredentials(),)
 
     # Attempting to call a method with both a request object and flattened
     # fields is an error.
@@ -2320,17 +2355,23 @@
                 max_messages=1277,
             )
 
         # Establish that the underlying call was made with the expected
         # request object values.
         assert len(call.mock_calls)
         _, args, _ = call.mock_calls[0]
-        assert args[0].subscription == "subscription_value"
-        assert args[0].return_immediately == True
-        assert args[0].max_messages == 1277
+        arg = args[0].subscription
+        mock_val = "subscription_value"
+        assert arg == mock_val
+        arg = args[0].return_immediately
+        mock_val = True
+        assert arg == mock_val
+        arg = args[0].max_messages
+        mock_val = 1277
+        assert arg == mock_val
 
 
 @pytest.mark.asyncio
 async def test_pull_flattened_error_async():
     client = SubscriberAsyncClient(credentials=ga_credentials.AnonymousCredentials(),)
 
     # Attempting to call a method with both a request object and flattened
@@ -2569,18 +2610,20 @@
             push_config=pubsub.PushConfig(push_endpoint="push_endpoint_value"),
         )
 
         # Establish that the underlying call was made with the expected
         # request object values.
         assert len(call.mock_calls) == 1
         _, args, _ = call.mock_calls[0]
-        assert args[0].subscription == "subscription_value"
-        assert args[0].push_config == pubsub.PushConfig(
-            push_endpoint="push_endpoint_value"
-        )
+        arg = args[0].subscription
+        mock_val = "subscription_value"
+        assert arg == mock_val
+        arg = args[0].push_config
+        mock_val = pubsub.PushConfig(push_endpoint="push_endpoint_value")
+        assert arg == mock_val
 
 
 def test_modify_push_config_flattened_error():
     client = SubscriberClient(credentials=ga_credentials.AnonymousCredentials(),)
 
     # Attempting to call a method with both a request object and flattened
     # fields is an error.
@@ -2611,18 +2654,20 @@
             push_config=pubsub.PushConfig(push_endpoint="push_endpoint_value"),
         )
 
         # Establish that the underlying call was made with the expected
         # request object values.
         assert len(call.mock_calls)
         _, args, _ = call.mock_calls[0]
-        assert args[0].subscription == "subscription_value"
-        assert args[0].push_config == pubsub.PushConfig(
-            push_endpoint="push_endpoint_value"
-        )
+        arg = args[0].subscription
+        mock_val = "subscription_value"
+        assert arg == mock_val
+        arg = args[0].push_config
+        mock_val = pubsub.PushConfig(push_endpoint="push_endpoint_value")
+        assert arg == mock_val
 
 
 @pytest.mark.asyncio
 async def test_modify_push_config_flattened_error_async():
     client = SubscriberAsyncClient(credentials=ga_credentials.AnonymousCredentials(),)
 
     # Attempting to call a method with both a request object and flattened
@@ -2776,15 +2821,17 @@
         # using the keyword arguments to the method.
         client.get_snapshot(snapshot="snapshot_value",)
 
         # Establish that the underlying call was made with the expected
         # request object values.
         assert len(call.mock_calls) == 1
         _, args, _ = call.mock_calls[0]
-        assert args[0].snapshot == "snapshot_value"
+        arg = args[0].snapshot
+        mock_val = "snapshot_value"
+        assert arg == mock_val
 
 
 def test_get_snapshot_flattened_error():
     client = SubscriberClient(credentials=ga_credentials.AnonymousCredentials(),)
 
     # Attempting to call a method with both a request object and flattened
     # fields is an error.
@@ -2808,15 +2855,17 @@
         # using the keyword arguments to the method.
         response = await client.get_snapshot(snapshot="snapshot_value",)
 
         # Establish that the underlying call was made with the expected
         # request object values.
         assert len(call.mock_calls)
         _, args, _ = call.mock_calls[0]
-        assert args[0].snapshot == "snapshot_value"
+        arg = args[0].snapshot
+        mock_val = "snapshot_value"
+        assert arg == mock_val
 
 
 @pytest.mark.asyncio
 async def test_get_snapshot_flattened_error_async():
     client = SubscriberAsyncClient(credentials=ga_credentials.AnonymousCredentials(),)
 
     # Attempting to call a method with both a request object and flattened
@@ -2972,15 +3021,17 @@
         # using the keyword arguments to the method.
         client.list_snapshots(project="project_value",)
 
         # Establish that the underlying call was made with the expected
         # request object values.
         assert len(call.mock_calls) == 1
         _, args, _ = call.mock_calls[0]
-        assert args[0].project == "project_value"
+        arg = args[0].project
+        mock_val = "project_value"
+        assert arg == mock_val
 
 
 def test_list_snapshots_flattened_error():
     client = SubscriberClient(credentials=ga_credentials.AnonymousCredentials(),)
 
     # Attempting to call a method with both a request object and flattened
     # fields is an error.
@@ -3006,15 +3057,17 @@
         # using the keyword arguments to the method.
         response = await client.list_snapshots(project="project_value",)
 
         # Establish that the underlying call was made with the expected
         # request object values.
         assert len(call.mock_calls)
         _, args, _ = call.mock_calls[0]
-        assert args[0].project == "project_value"
+        arg = args[0].project
+        mock_val = "project_value"
+        assert arg == mock_val
 
 
 @pytest.mark.asyncio
 async def test_list_snapshots_flattened_error_async():
     client = SubscriberAsyncClient(credentials=ga_credentials.AnonymousCredentials(),)
 
     # Attempting to call a method with both a request object and flattened
@@ -3292,16 +3345,20 @@
             name="name_value", subscription="subscription_value",
         )
 
         # Establish that the underlying call was made with the expected
         # request object values.
         assert len(call.mock_calls) == 1
         _, args, _ = call.mock_calls[0]
-        assert args[0].name == "name_value"
-        assert args[0].subscription == "subscription_value"
+        arg = args[0].name
+        mock_val = "name_value"
+        assert arg == mock_val
+        arg = args[0].subscription
+        mock_val = "subscription_value"
+        assert arg == mock_val
 
 
 def test_create_snapshot_flattened_error():
     client = SubscriberClient(credentials=ga_credentials.AnonymousCredentials(),)
 
     # Attempting to call a method with both a request object and flattened
     # fields is an error.
@@ -3329,16 +3386,20 @@
             name="name_value", subscription="subscription_value",
         )
 
         # Establish that the underlying call was made with the expected
         # request object values.
         assert len(call.mock_calls)
         _, args, _ = call.mock_calls[0]
-        assert args[0].name == "name_value"
-        assert args[0].subscription == "subscription_value"
+        arg = args[0].name
+        mock_val = "name_value"
+        assert arg == mock_val
+        arg = args[0].subscription
+        mock_val = "subscription_value"
+        assert arg == mock_val
 
 
 @pytest.mark.asyncio
 async def test_create_snapshot_flattened_error_async():
     client = SubscriberAsyncClient(credentials=ga_credentials.AnonymousCredentials(),)
 
     # Attempting to call a method with both a request object and flattened
@@ -3624,15 +3685,17 @@
         # using the keyword arguments to the method.
         client.delete_snapshot(snapshot="snapshot_value",)
 
         # Establish that the underlying call was made with the expected
         # request object values.
         assert len(call.mock_calls) == 1
         _, args, _ = call.mock_calls[0]
-        assert args[0].snapshot == "snapshot_value"
+        arg = args[0].snapshot
+        mock_val = "snapshot_value"
+        assert arg == mock_val
 
 
 def test_delete_snapshot_flattened_error():
     client = SubscriberClient(credentials=ga_credentials.AnonymousCredentials(),)
 
     # Attempting to call a method with both a request object and flattened
     # fields is an error.
@@ -3656,15 +3719,17 @@
         # using the keyword arguments to the method.
         response = await client.delete_snapshot(snapshot="snapshot_value",)
 
         # Establish that the underlying call was made with the expected
         # request object values.
         assert len(call.mock_calls)
         _, args, _ = call.mock_calls[0]
-        assert args[0].snapshot == "snapshot_value"
+        arg = args[0].snapshot
+        mock_val = "snapshot_value"
+        assert arg == mock_val
 
 
 @pytest.mark.asyncio
 async def test_delete_snapshot_flattened_error_async():
     client = SubscriberAsyncClient(credentials=ga_credentials.AnonymousCredentials(),)
 
     # Attempting to call a method with both a request object and flattened
@@ -3917,16 +3982,18 @@
         "get_iam_policy",
         "test_iam_permissions",
     )
     for method in methods:
         with pytest.raises(NotImplementedError):
             getattr(transport, method)(request=object())
 
+    with pytest.raises(NotImplementedError):
+        transport.close()
+
 
-@requires_google_auth_gte_1_25_0
 def test_subscriber_base_transport_with_credentials_file():
     # Instantiate the base transport with a credentials file
     with mock.patch.object(
         google.auth, "load_credentials_from_file", autospec=True
     ) as load_creds, mock.patch(
         "google.pubsub_v1.services.subscriber.transports.SubscriberTransport._prep_wrapped_messages"
     ) as Transport:
@@ -3942,49 +4009,25 @@
                 "https://www.googleapis.com/auth/cloud-platform",
                 "https://www.googleapis.com/auth/pubsub",
             ),
             quota_project_id="octopus",
         )
 
 
-@requires_google_auth_lt_1_25_0
-def test_subscriber_base_transport_with_credentials_file_old_google_auth():
-    # Instantiate the base transport with a credentials file
-    with mock.patch.object(
-        google.auth, "load_credentials_from_file", autospec=True
-    ) as load_creds, mock.patch(
-        "google.pubsub_v1.services.subscriber.transports.SubscriberTransport._prep_wrapped_messages"
-    ) as Transport:
-        Transport.return_value = None
-        load_creds.return_value = (ga_credentials.AnonymousCredentials(), None)
-        transport = transports.SubscriberTransport(
-            credentials_file="credentials.json", quota_project_id="octopus",
-        )
-        load_creds.assert_called_once_with(
-            "credentials.json",
-            scopes=(
-                "https://www.googleapis.com/auth/cloud-platform",
-                "https://www.googleapis.com/auth/pubsub",
-            ),
-            quota_project_id="octopus",
-        )
-
-
 def test_subscriber_base_transport_with_adc():
     # Test the default credentials are used if credentials and credentials_file are None.
     with mock.patch.object(google.auth, "default", autospec=True) as adc, mock.patch(
         "google.pubsub_v1.services.subscriber.transports.SubscriberTransport._prep_wrapped_messages"
     ) as Transport:
         Transport.return_value = None
         adc.return_value = (ga_credentials.AnonymousCredentials(), None)
         transport = transports.SubscriberTransport()
         adc.assert_called_once()
 
 
-@requires_google_auth_gte_1_25_0
 def test_subscriber_auth_adc():
     # If no credentials are provided, we should use ADC credentials.
     with mock.patch.object(google.auth, "default", autospec=True) as adc:
         adc.return_value = (ga_credentials.AnonymousCredentials(), None)
         SubscriberClient()
         adc.assert_called_once_with(
             scopes=None,
@@ -3992,34 +4035,18 @@
                 "https://www.googleapis.com/auth/cloud-platform",
                 "https://www.googleapis.com/auth/pubsub",
             ),
             quota_project_id=None,
         )
 
 
-@requires_google_auth_lt_1_25_0
-def test_subscriber_auth_adc_old_google_auth():
-    # If no credentials are provided, we should use ADC credentials.
-    with mock.patch.object(google.auth, "default", autospec=True) as adc:
-        adc.return_value = (ga_credentials.AnonymousCredentials(), None)
-        SubscriberClient()
-        adc.assert_called_once_with(
-            scopes=(
-                "https://www.googleapis.com/auth/cloud-platform",
-                "https://www.googleapis.com/auth/pubsub",
-            ),
-            quota_project_id=None,
-        )
-
-
 @pytest.mark.parametrize(
     "transport_class",
     [transports.SubscriberGrpcTransport, transports.SubscriberGrpcAsyncIOTransport,],
 )
-@requires_google_auth_gte_1_25_0
 def test_subscriber_transport_auth_adc(transport_class):
     # If credentials and host are not provided, the transport class should use
     # ADC credentials.
     with mock.patch.object(google.auth, "default", autospec=True) as adc:
         adc.return_value = (ga_credentials.AnonymousCredentials(), None)
         transport_class(quota_project_id="octopus", scopes=["1", "2"])
         adc.assert_called_once_with(
@@ -4029,34 +4056,14 @@
                 "https://www.googleapis.com/auth/pubsub",
             ),
             quota_project_id="octopus",
         )
 
 
 @pytest.mark.parametrize(
-    "transport_class",
-    [transports.SubscriberGrpcTransport, transports.SubscriberGrpcAsyncIOTransport,],
-)
-@requires_google_auth_lt_1_25_0
-def test_subscriber_transport_auth_adc_old_google_auth(transport_class):
-    # If credentials and host are not provided, the transport class should use
-    # ADC credentials.
-    with mock.patch.object(google.auth, "default", autospec=True) as adc:
-        adc.return_value = (ga_credentials.AnonymousCredentials(), None)
-        transport_class(quota_project_id="octopus")
-        adc.assert_called_once_with(
-            scopes=(
-                "https://www.googleapis.com/auth/cloud-platform",
-                "https://www.googleapis.com/auth/pubsub",
-            ),
-            quota_project_id="octopus",
-        )
-
-
-@pytest.mark.parametrize(
     "transport_class,grpc_helpers",
     [
         (transports.SubscriberGrpcTransport, grpc_helpers),
         (transports.SubscriberGrpcAsyncIOTransport, grpc_helpers_async),
     ],
 )
 def test_subscriber_transport_create_channel(transport_class, grpc_helpers):
@@ -4898,7 +4905,53 @@
         response = await client.test_iam_permissions(
             request={
                 "resource": "resource_value",
                 "permissions": ["permissions_value"],
             }
         )
         call.assert_called()
+
+
+@pytest.mark.asyncio
+async def test_transport_close_async():
+    client = SubscriberAsyncClient(
+        credentials=ga_credentials.AnonymousCredentials(), transport="grpc_asyncio",
+    )
+    with mock.patch.object(
+        type(getattr(client.transport, "grpc_channel")), "close"
+    ) as close:
+        async with client:
+            close.assert_not_called()
+        close.assert_called_once()
+
+
+def test_transport_close():
+    transports = {
+        "grpc": "_grpc_channel",
+    }
+
+    for transport, close_name in transports.items():
+        client = SubscriberClient(
+            credentials=ga_credentials.AnonymousCredentials(), transport=transport
+        )
+        with mock.patch.object(
+            type(getattr(client.transport, close_name)), "close"
+        ) as close:
+            with client:
+                close.assert_not_called()
+            close.assert_called_once()
+
+
+def test_client_ctx():
+    transports = [
+        "grpc",
+    ]
+    for transport in transports:
+        client = SubscriberClient(
+            credentials=ga_credentials.AnonymousCredentials(), transport=transport
+        )
+        # Test client calls underlying transport.
+        with mock.patch.object(type(client.transport), "close") as close:
+            close.assert_not_called()
+            with client:
+                pass
+            close.assert_called()
```

### Comparing `google-cloud-pubsub-2.8.0/tests/unit/pubsub_v1/conftest.py` & `google-cloud-pubsub-2.9.0/tests/unit/pubsub_v1/conftest.py`

 * *Files identical despite different names*

### Comparing `google-cloud-pubsub-2.8.0/tests/unit/pubsub_v1/publisher/batch/test_base.py` & `google-cloud-pubsub-2.9.0/tests/unit/pubsub_v1/publisher/batch/test_base.py`

 * *Files identical despite different names*

### Comparing `google-cloud-pubsub-2.8.0/tests/unit/pubsub_v1/publisher/batch/test_thread.py` & `google-cloud-pubsub-2.9.0/tests/unit/pubsub_v1/publisher/batch/test_thread.py`

 * *Files identical despite different names*

### Comparing `google-cloud-pubsub-2.8.0/tests/unit/pubsub_v1/publisher/sequencer/test_ordered_sequencer.py` & `google-cloud-pubsub-2.9.0/tests/unit/pubsub_v1/publisher/sequencer/test_ordered_sequencer.py`

 * *Files identical despite different names*

### Comparing `google-cloud-pubsub-2.8.0/tests/unit/pubsub_v1/publisher/sequencer/test_unordered_sequencer.py` & `google-cloud-pubsub-2.9.0/tests/unit/pubsub_v1/publisher/sequencer/test_unordered_sequencer.py`

 * *Files identical despite different names*

### Comparing `google-cloud-pubsub-2.8.0/tests/unit/pubsub_v1/publisher/test_flow_controller.py` & `google-cloud-pubsub-2.9.0/tests/unit/pubsub_v1/publisher/test_flow_controller.py`

 * *Files identical despite different names*

### Comparing `google-cloud-pubsub-2.8.0/tests/unit/pubsub_v1/publisher/test_futures_publisher.py` & `google-cloud-pubsub-2.9.0/tests/unit/pubsub_v1/publisher/test_futures_publisher.py`

 * *Files identical despite different names*

### Comparing `google-cloud-pubsub-2.8.0/tests/unit/pubsub_v1/publisher/test_publisher_client.py` & `google-cloud-pubsub-2.9.0/tests/unit/pubsub_v1/publisher/test_publisher_client.py`

 * *Files identical despite different names*

### Comparing `google-cloud-pubsub-2.8.0/tests/unit/pubsub_v1/subscriber/test_dispatcher.py` & `google-cloud-pubsub-2.9.0/tests/unit/pubsub_v1/subscriber/test_dispatcher.py`

 * *Files identical despite different names*

### Comparing `google-cloud-pubsub-2.8.0/tests/unit/pubsub_v1/subscriber/test_futures_subscriber.py` & `google-cloud-pubsub-2.9.0/tests/unit/pubsub_v1/subscriber/test_futures_subscriber.py`

 * *Files identical despite different names*

### Comparing `google-cloud-pubsub-2.8.0/tests/unit/pubsub_v1/subscriber/test_heartbeater.py` & `google-cloud-pubsub-2.9.0/tests/unit/pubsub_v1/subscriber/test_heartbeater.py`

 * *Files identical despite different names*

### Comparing `google-cloud-pubsub-2.8.0/tests/unit/pubsub_v1/subscriber/test_helper_threads.py` & `google-cloud-pubsub-2.9.0/tests/unit/pubsub_v1/subscriber/test_helper_threads.py`

 * *Files identical despite different names*

### Comparing `google-cloud-pubsub-2.8.0/tests/unit/pubsub_v1/subscriber/test_histogram.py` & `google-cloud-pubsub-2.9.0/tests/unit/pubsub_v1/subscriber/test_histogram.py`

 * *Files identical despite different names*

### Comparing `google-cloud-pubsub-2.8.0/tests/unit/pubsub_v1/subscriber/test_leaser.py` & `google-cloud-pubsub-2.9.0/tests/unit/pubsub_v1/subscriber/test_leaser.py`

 * *Files identical despite different names*

### Comparing `google-cloud-pubsub-2.8.0/tests/unit/pubsub_v1/subscriber/test_message.py` & `google-cloud-pubsub-2.9.0/tests/unit/pubsub_v1/subscriber/test_message.py`

 * *Files identical despite different names*

### Comparing `google-cloud-pubsub-2.8.0/tests/unit/pubsub_v1/subscriber/test_messages_on_hold.py` & `google-cloud-pubsub-2.9.0/tests/unit/pubsub_v1/subscriber/test_messages_on_hold.py`

 * *Files identical despite different names*

### Comparing `google-cloud-pubsub-2.8.0/tests/unit/pubsub_v1/subscriber/test_scheduler.py` & `google-cloud-pubsub-2.9.0/tests/unit/pubsub_v1/subscriber/test_scheduler.py`

 * *Files identical despite different names*

### Comparing `google-cloud-pubsub-2.8.0/tests/unit/pubsub_v1/subscriber/test_streaming_pull_manager.py` & `google-cloud-pubsub-2.9.0/tests/unit/pubsub_v1/subscriber/test_streaming_pull_manager.py`

 * *Files identical despite different names*

### Comparing `google-cloud-pubsub-2.8.0/tests/unit/pubsub_v1/subscriber/test_subscriber_client.py` & `google-cloud-pubsub-2.9.0/tests/unit/pubsub_v1/subscriber/test_subscriber_client.py`

 * *Files identical despite different names*

### Comparing `google-cloud-pubsub-2.8.0/tests/unit/pubsub_v1/test__gapic.py` & `google-cloud-pubsub-2.9.0/tests/unit/pubsub_v1/test__gapic.py`

 * *Files identical despite different names*

### Comparing `google-cloud-pubsub-2.8.0/tests/unit/pubsub_v1/test_futures.py` & `google-cloud-pubsub-2.9.0/tests/unit/pubsub_v1/test_futures.py`

 * *Files identical despite different names*

### Comparing `google-cloud-pubsub-2.8.0/tests/unit/test_pubsub.py` & `google-cloud-pubsub-2.9.0/tests/unit/test_pubsub.py`

 * *Files identical despite different names*

