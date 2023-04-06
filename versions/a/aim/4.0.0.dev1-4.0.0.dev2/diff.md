# Comparing `tmp/aim-4.0.0.dev1.tar.gz` & `tmp/aim-4.0.0.dev2.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "aim-4.0.0.dev1.tar", last modified: Mon Mar 13 14:51:39 2023, max compression
+gzip compressed data, was "aim-4.0.0.dev2.tar", last modified: Wed Apr  5 11:38:00 2023, max compression
```

## Comparing `aim-4.0.0.dev1.tar` & `aim-4.0.0.dev2.tar`

### file list

```diff
@@ -1,460 +1,460 @@
-drwxr-xr-x   0 github     (503) staff       (20)        0 2023-03-13 14:51:39.952595 aim-4.0.0.dev1/
--rw-r--r--   0 github     (503) staff       (20)    11347 2022-08-06 00:13:01.000000 aim-4.0.0.dev1/LICENSE
--rw-r--r--   0 github     (503) staff       (20)      185 2022-04-19 22:29:06.000000 aim-4.0.0.dev1/MANIFEST.in
--rw-r--r--   0 github     (503) staff       (20)    26572 2023-03-13 14:51:39.952694 aim-4.0.0.dev1/PKG-INFO
--rw-r--r--   0 github     (503) staff       (20)    25885 2023-03-07 20:10:31.000000 aim-4.0.0.dev1/README.md
-drwxr-xr-x   0 github     (503) staff       (20)        0 2023-03-13 14:51:39.872845 aim-4.0.0.dev1/aim/
--rw-r--r--   0 github     (503) staff       (20)       10 2023-03-13 14:51:31.000000 aim-4.0.0.dev1/aim/VERSION
--rw-r--r--   0 github     (503) staff       (20)      825 2022-04-19 22:29:06.000000 aim-4.0.0.dev1/aim/__about__.py
--rw-r--r--   0 github     (503) staff       (20)      377 2023-02-01 20:08:30.000000 aim-4.0.0.dev1/aim/__init__.py
--rw-r--r--   0 github     (503) staff       (20)      183 2022-04-19 22:29:06.000000 aim-4.0.0.dev1/aim/__version__.py
--rw-r--r--   0 github     (503) staff       (20)      100 2023-01-13 20:10:23.000000 aim-4.0.0.dev1/aim/acme.py
--rw-r--r--   0 github     (503) staff       (20)       96 2022-05-06 13:59:46.000000 aim-4.0.0.dev1/aim/catboost.py
-drwxr-xr-x   0 github     (503) staff       (20)        0 2023-03-13 14:51:39.874679 aim-4.0.0.dev1/aim/cli/
--rw-r--r--   0 github     (503) staff       (20)        0 2022-04-19 22:29:06.000000 aim-4.0.0.dev1/aim/cli/__init__.py
--rw-r--r--   0 github     (503) staff       (20)     1323 2023-01-24 20:09:40.000000 aim-4.0.0.dev1/aim/cli/cli.py
--rw-r--r--   0 github     (503) staff       (20)      166 2022-06-17 00:13:19.000000 aim-4.0.0.dev1/aim/cli/configs.py
-drwxr-xr-x   0 github     (503) staff       (20)        0 2023-03-13 14:51:39.875035 aim-4.0.0.dev1/aim/cli/convert/
--rw-r--r--   0 github     (503) staff       (20)        0 2022-04-19 22:29:06.000000 aim-4.0.0.dev1/aim/cli/convert/__init__.py
--rw-r--r--   0 github     (503) staff       (20)     2998 2022-08-20 12:34:00.000000 aim-4.0.0.dev1/aim/cli/convert/commands.py
-drwxr-xr-x   0 github     (503) staff       (20)        0 2023-03-13 14:51:39.876039 aim-4.0.0.dev1/aim/cli/convert/processors/
--rw-r--r--   0 github     (503) staff       (20)      113 2022-08-20 12:34:00.000000 aim-4.0.0.dev1/aim/cli/convert/processors/__init__.py
--rw-r--r--   0 github     (503) staff       (20)     5914 2022-09-01 19:23:53.000000 aim-4.0.0.dev1/aim/cli/convert/processors/mlflow.py
--rw-r--r--   0 github     (503) staff       (20)    10372 2022-08-06 00:13:01.000000 aim-4.0.0.dev1/aim/cli/convert/processors/tensorboard.py
--rw-r--r--   0 github     (503) staff       (20)     6816 2023-01-04 20:08:59.000000 aim-4.0.0.dev1/aim/cli/convert/processors/wandb.py
-drwxr-xr-x   0 github     (503) staff       (20)        0 2023-03-13 14:51:39.876360 aim-4.0.0.dev1/aim/cli/init/
--rw-r--r--   0 github     (503) staff       (20)        0 2022-04-19 22:29:06.000000 aim-4.0.0.dev1/aim/cli/init/__init__.py
--rw-r--r--   0 github     (503) staff       (20)     1442 2023-01-24 20:09:40.000000 aim-4.0.0.dev1/aim/cli/init/commands.py
-drwxr-xr-x   0 github     (503) staff       (20)        0 2023-03-13 14:51:39.876636 aim-4.0.0.dev1/aim/cli/manager/
--rw-r--r--   0 github     (503) staff       (20)        0 2022-04-19 22:29:06.000000 aim-4.0.0.dev1/aim/cli/manager/__init__.py
--rw-r--r--   0 github     (503) staff       (20)     3382 2022-08-11 13:58:02.000000 aim-4.0.0.dev1/aim/cli/manager/manager.py
-drwxr-xr-x   0 github     (503) staff       (20)        0 2023-03-13 14:51:39.876983 aim-4.0.0.dev1/aim/cli/reindex/
--rw-r--r--   0 github     (503) staff       (20)        0 2022-04-19 22:29:06.000000 aim-4.0.0.dev1/aim/cli/reindex/__init__.py
--rw-r--r--   0 github     (503) staff       (20)      736 2022-11-25 20:09:54.000000 aim-4.0.0.dev1/aim/cli/reindex/commands.py
-drwxr-xr-x   0 github     (503) staff       (20)        0 2023-03-13 14:51:39.877623 aim-4.0.0.dev1/aim/cli/runs/
--rw-r--r--   0 github     (503) staff       (20)        0 2022-04-19 22:29:06.000000 aim-4.0.0.dev1/aim/cli/runs/__init__.py
--rw-r--r--   0 github     (503) staff       (20)     6319 2023-02-01 20:08:30.000000 aim-4.0.0.dev1/aim/cli/runs/commands.py
--rw-r--r--   0 github     (503) staff       (20)     2570 2022-11-25 20:09:54.000000 aim-4.0.0.dev1/aim/cli/runs/utils.py
-drwxr-xr-x   0 github     (503) staff       (20)        0 2023-03-13 14:51:39.878060 aim-4.0.0.dev1/aim/cli/server/
--rw-r--r--   0 github     (503) staff       (20)        0 2022-04-19 22:29:06.000000 aim-4.0.0.dev1/aim/cli/server/__init__.py
--rw-r--r--   0 github     (503) staff       (20)     3495 2023-01-24 20:09:40.000000 aim-4.0.0.dev1/aim/cli/server/commands.py
-drwxr-xr-x   0 github     (503) staff       (20)        0 2023-03-13 14:51:39.878415 aim-4.0.0.dev1/aim/cli/storage/
--rw-r--r--   0 github     (503) staff       (20)        0 2022-06-17 00:13:19.000000 aim-4.0.0.dev1/aim/cli/storage/__init__.py
--rw-r--r--   0 github     (503) staff       (20)     7253 2022-11-25 20:09:54.000000 aim-4.0.0.dev1/aim/cli/storage/commands.py
-drwxr-xr-x   0 github     (503) staff       (20)        0 2023-03-13 14:51:39.878810 aim-4.0.0.dev1/aim/cli/telemetry/
--rw-r--r--   0 github     (503) staff       (20)        0 2023-01-24 20:09:40.000000 aim-4.0.0.dev1/aim/cli/telemetry/__init__.py
--rw-r--r--   0 github     (503) staff       (20)      305 2023-01-24 20:09:40.000000 aim-4.0.0.dev1/aim/cli/telemetry/commands.py
-drwxr-xr-x   0 github     (503) staff       (20)        0 2023-03-13 14:51:39.879406 aim-4.0.0.dev1/aim/cli/up/
--rw-r--r--   0 github     (503) staff       (20)        0 2022-04-19 22:29:06.000000 aim-4.0.0.dev1/aim/cli/up/__init__.py
--rw-r--r--   0 github     (503) staff       (20)     5953 2023-01-24 20:09:40.000000 aim-4.0.0.dev1/aim/cli/up/commands.py
--rw-r--r--   0 github     (503) staff       (20)     1446 2022-06-21 18:01:08.000000 aim-4.0.0.dev1/aim/cli/up/utils.py
-drwxr-xr-x   0 github     (503) staff       (20)        0 2023-03-13 14:51:39.879972 aim-4.0.0.dev1/aim/cli/upgrade/
--rw-r--r--   0 github     (503) staff       (20)        0 2022-04-19 22:29:06.000000 aim-4.0.0.dev1/aim/cli/upgrade/__init__.py
-drwxr-xr-x   0 github     (503) staff       (20)        0 2023-03-13 14:51:39.880765 aim-4.0.0.dev1/aim/cli/upgrade/_legacy_repo/
--rw-r--r--   0 github     (503) staff       (20)      258 2022-04-19 22:29:06.000000 aim-4.0.0.dev1/aim/cli/upgrade/_legacy_repo/__init__.py
--rw-r--r--   0 github     (503) staff       (20)      734 2022-04-19 22:29:06.000000 aim-4.0.0.dev1/aim/cli/upgrade/_legacy_repo/configs.py
--rw-r--r--   0 github     (503) staff       (20)      448 2022-04-19 22:29:06.000000 aim-4.0.0.dev1/aim/cli/upgrade/_legacy_repo/metric_artifact.py
-drwxr-xr-x   0 github     (503) staff       (20)        0 2023-03-13 14:51:39.881333 aim-4.0.0.dev1/aim/cli/upgrade/_legacy_repo/proto/
--rw-r--r--   0 github     (503) staff       (20)        0 2022-04-19 22:29:06.000000 aim-4.0.0.dev1/aim/cli/upgrade/_legacy_repo/proto/__init__.py
--rw-r--r--   0 github     (503) staff       (20)      263 2023-01-13 20:10:23.000000 aim-4.0.0.dev1/aim/cli/upgrade/_legacy_repo/proto/base_pb2.py
--rw-r--r--   0 github     (503) staff       (20)      267 2023-01-13 20:10:23.000000 aim-4.0.0.dev1/aim/cli/upgrade/_legacy_repo/proto/metric_pb2.py
-drwxr-xr-x   0 github     (503) staff       (20)        0 2023-03-13 14:51:39.881801 aim-4.0.0.dev1/aim/cli/upgrade/_legacy_repo/proto/v3/
--rw-r--r--   0 github     (503) staff       (20)        0 2023-01-13 20:10:23.000000 aim-4.0.0.dev1/aim/cli/upgrade/_legacy_repo/proto/v3/__init__.py
--rw-r--r--   0 github     (503) staff       (20)     3396 2023-01-13 20:10:23.000000 aim-4.0.0.dev1/aim/cli/upgrade/_legacy_repo/proto/v3/base_pb2.py
--rw-r--r--   0 github     (503) staff       (20)     1919 2023-01-13 20:10:23.000000 aim-4.0.0.dev1/aim/cli/upgrade/_legacy_repo/proto/v3/metric_pb2.py
-drwxr-xr-x   0 github     (503) staff       (20)        0 2023-03-13 14:51:39.882237 aim-4.0.0.dev1/aim/cli/upgrade/_legacy_repo/proto/v4/
--rw-r--r--   0 github     (503) staff       (20)        0 2023-01-13 20:10:23.000000 aim-4.0.0.dev1/aim/cli/upgrade/_legacy_repo/proto/v4/__init__.py
--rw-r--r--   0 github     (503) staff       (20)     1111 2023-01-13 20:10:23.000000 aim-4.0.0.dev1/aim/cli/upgrade/_legacy_repo/proto/v4/base_pb2.py
--rw-r--r--   0 github     (503) staff       (20)      969 2023-01-13 20:10:23.000000 aim-4.0.0.dev1/aim/cli/upgrade/_legacy_repo/proto/v4/metric_pb2.py
-drwxr-xr-x   0 github     (503) staff       (20)        0 2023-03-13 14:51:39.883383 aim-4.0.0.dev1/aim/cli/upgrade/_legacy_repo/repo/
--rw-r--r--   0 github     (503) staff       (20)        1 2022-04-19 22:29:06.000000 aim-4.0.0.dev1/aim/cli/upgrade/_legacy_repo/repo/__init__.py
--rw-r--r--   0 github     (503) staff       (20)     1722 2022-04-19 22:29:06.000000 aim-4.0.0.dev1/aim/cli/upgrade/_legacy_repo/repo/metric.py
--rw-r--r--   0 github     (503) staff       (20)     3722 2022-04-19 22:29:06.000000 aim-4.0.0.dev1/aim/cli/upgrade/_legacy_repo/repo/repo.py
--rw-r--r--   0 github     (503) staff       (20)     4062 2022-04-19 22:29:06.000000 aim-4.0.0.dev1/aim/cli/upgrade/_legacy_repo/repo/run.py
--rw-r--r--   0 github     (503) staff       (20)     1357 2022-04-19 22:29:06.000000 aim-4.0.0.dev1/aim/cli/upgrade/_legacy_repo/repo/trace.py
--rw-r--r--   0 github     (503) staff       (20)     1211 2022-04-19 22:29:06.000000 aim-4.0.0.dev1/aim/cli/upgrade/_legacy_repo/repo/utils.py
--rw-r--r--   0 github     (503) staff       (20)     6635 2022-04-19 22:29:06.000000 aim-4.0.0.dev1/aim/cli/upgrade/utils.py
--rw-r--r--   0 github     (503) staff       (20)      370 2022-04-19 22:29:06.000000 aim-4.0.0.dev1/aim/cli/utils.py
-drwxr-xr-x   0 github     (503) staff       (20)        0 2023-03-13 14:51:39.883633 aim-4.0.0.dev1/aim/cli/version/
--rw-r--r--   0 github     (503) staff       (20)        0 2022-04-19 22:29:06.000000 aim-4.0.0.dev1/aim/cli/version/__init__.py
--rw-r--r--   0 github     (503) staff       (20)      149 2022-04-19 22:29:06.000000 aim-4.0.0.dev1/aim/cli/version/commands.py
--rw-r--r--   0 github     (503) staff       (20)     9960 2023-01-24 20:09:40.000000 aim-4.0.0.dev1/aim/cli/watcher_cli.py
-drwxr-xr-x   0 github     (503) staff       (20)        0 2023-03-13 14:51:39.884298 aim-4.0.0.dev1/aim/ext/
--rw-r--r--   0 github     (503) staff       (20)        0 2022-04-19 22:29:06.000000 aim-4.0.0.dev1/aim/ext/__init__.py
-drwxr-xr-x   0 github     (503) staff       (20)        0 2023-03-13 14:51:39.884591 aim-4.0.0.dev1/aim/ext/cleanup/
--rw-r--r--   0 github     (503) staff       (20)     3579 2022-11-12 00:14:35.000000 aim-4.0.0.dev1/aim/ext/cleanup/__init__.py
--rw-r--r--   0 github     (503) staff       (20)     2021 2023-03-02 20:49:40.000000 aim-4.0.0.dev1/aim/ext/exception_resistant.py
-drwxr-xr-x   0 github     (503) staff       (20)        0 2023-03-13 14:51:39.884951 aim-4.0.0.dev1/aim/ext/notebook/
--rw-r--r--   0 github     (503) staff       (20)        0 2022-04-19 22:29:06.000000 aim-4.0.0.dev1/aim/ext/notebook/__init__.py
--rw-r--r--   0 github     (503) staff       (20)     7314 2022-04-19 22:29:06.000000 aim-4.0.0.dev1/aim/ext/notebook/notebook.py
-drwxr-xr-x   0 github     (503) staff       (20)        0 2023-03-13 14:51:39.887231 aim-4.0.0.dev1/aim/ext/notifier/
--rw-r--r--   0 github     (503) staff       (20)      589 2022-08-20 12:34:00.000000 aim-4.0.0.dev1/aim/ext/notifier/__init__.py
--rw-r--r--   0 github     (503) staff       (20)      305 2022-08-20 12:34:00.000000 aim-4.0.0.dev1/aim/ext/notifier/base_notifier.py
--rw-r--r--   0 github     (503) staff       (20)     1858 2022-11-25 20:09:54.000000 aim-4.0.0.dev1/aim/ext/notifier/config.py
--rw-r--r--   0 github     (503) staff       (20)      361 2022-08-20 12:34:00.000000 aim-4.0.0.dev1/aim/ext/notifier/config_default.json
--rw-r--r--   0 github     (503) staff       (20)       70 2022-08-20 12:34:00.000000 aim-4.0.0.dev1/aim/ext/notifier/config_empty.json
--rw-r--r--   0 github     (503) staff       (20)      522 2022-08-20 12:34:00.000000 aim-4.0.0.dev1/aim/ext/notifier/logging_notifier.py
--rw-r--r--   0 github     (503) staff       (20)     1428 2022-08-20 12:34:00.000000 aim-4.0.0.dev1/aim/ext/notifier/notifier.py
--rw-r--r--   0 github     (503) staff       (20)     1158 2022-08-20 12:34:00.000000 aim-4.0.0.dev1/aim/ext/notifier/notifier_builder.py
--rw-r--r--   0 github     (503) staff       (20)      524 2022-08-20 12:34:00.000000 aim-4.0.0.dev1/aim/ext/notifier/slack_notifier.py
--rw-r--r--   0 github     (503) staff       (20)     1034 2022-08-20 12:34:00.000000 aim-4.0.0.dev1/aim/ext/notifier/utils.py
--rw-r--r--   0 github     (503) staff       (20)      862 2022-08-20 12:34:00.000000 aim-4.0.0.dev1/aim/ext/notifier/workplace_notifier.py
-drwxr-xr-x   0 github     (503) staff       (20)        0 2023-03-13 14:51:39.888490 aim-4.0.0.dev1/aim/ext/resource/
--rw-r--r--   0 github     (503) staff       (20)       92 2022-04-19 22:29:06.000000 aim-4.0.0.dev1/aim/ext/resource/__init__.py
--rw-r--r--   0 github     (503) staff       (20)      100 2022-04-19 22:29:06.000000 aim-4.0.0.dev1/aim/ext/resource/configs.py
--rw-r--r--   0 github     (503) staff       (20)      726 2022-05-16 21:25:24.000000 aim-4.0.0.dev1/aim/ext/resource/log.py
--rw-r--r--   0 github     (503) staff       (20)     6700 2023-01-04 20:08:59.000000 aim-4.0.0.dev1/aim/ext/resource/stat.py
--rw-r--r--   0 github     (503) staff       (20)     7511 2023-01-04 20:08:59.000000 aim-4.0.0.dev1/aim/ext/resource/tracker.py
--rw-r--r--   0 github     (503) staff       (20)       56 2022-04-19 22:29:06.000000 aim-4.0.0.dev1/aim/ext/resource/utils.py
-drwxr-xr-x   0 github     (503) staff       (20)        0 2023-03-13 14:51:39.888770 aim-4.0.0.dev1/aim/ext/sshfs/
--rw-r--r--   0 github     (503) staff       (20)        0 2022-04-19 22:29:06.000000 aim-4.0.0.dev1/aim/ext/sshfs/__init__.py
--rw-r--r--   0 github     (503) staff       (20)     7768 2022-04-19 22:29:06.000000 aim-4.0.0.dev1/aim/ext/sshfs/utils.py
-drwxr-xr-x   0 github     (503) staff       (20)        0 2023-03-13 14:51:39.889059 aim-4.0.0.dev1/aim/ext/task_queue/
--rw-r--r--   0 github     (503) staff       (20)        0 2022-04-19 22:29:06.000000 aim-4.0.0.dev1/aim/ext/task_queue/__init__.py
--rw-r--r--   0 github     (503) staff       (20)     2069 2022-04-19 22:29:06.000000 aim-4.0.0.dev1/aim/ext/task_queue/queue.py
-drwxr-xr-x   0 github     (503) staff       (20)        0 2023-03-13 14:51:39.889761 aim-4.0.0.dev1/aim/ext/tensorboard_tracker/
--rw-r--r--   0 github     (503) staff       (20)       48 2023-01-04 20:08:59.000000 aim-4.0.0.dev1/aim/ext/tensorboard_tracker/__init__.py
--rw-r--r--   0 github     (503) staff       (20)      919 2023-01-04 20:08:59.000000 aim-4.0.0.dev1/aim/ext/tensorboard_tracker/run.py
--rw-r--r--   0 github     (503) staff       (20)     7201 2023-01-04 20:08:59.000000 aim-4.0.0.dev1/aim/ext/tensorboard_tracker/tracker.py
-drwxr-xr-x   0 github     (503) staff       (20)        0 2023-03-13 14:51:39.892771 aim-4.0.0.dev1/aim/ext/transport/
--rw-r--r--   0 github     (503) staff       (20)        0 2022-04-19 22:29:06.000000 aim-4.0.0.dev1/aim/ext/transport/__init__.py
--rw-r--r--   0 github     (503) staff       (20)    12932 2023-02-27 08:16:06.000000 aim-4.0.0.dev1/aim/ext/transport/client.py
--rw-r--r--   0 github     (503) staff       (20)      515 2022-04-19 22:29:06.000000 aim-4.0.0.dev1/aim/ext/transport/config.py
--rw-r--r--   0 github     (503) staff       (20)     3298 2023-01-23 20:08:00.000000 aim-4.0.0.dev1/aim/ext/transport/handlers.py
--rw-r--r--   0 github     (503) staff       (20)     5555 2023-01-13 20:10:23.000000 aim-4.0.0.dev1/aim/ext/transport/health.py
--rw-r--r--   0 github     (503) staff       (20)     5616 2023-01-13 20:10:23.000000 aim-4.0.0.dev1/aim/ext/transport/heartbeat.py
--rw-r--r--   0 github     (503) staff       (20)     3347 2023-01-13 20:10:23.000000 aim-4.0.0.dev1/aim/ext/transport/message_utils.py
-drwxr-xr-x   0 github     (503) staff       (20)        0 2023-03-13 14:51:39.893996 aim-4.0.0.dev1/aim/ext/transport/proto/
--rw-r--r--   0 github     (503) staff       (20)        0 2023-01-13 20:10:23.000000 aim-4.0.0.dev1/aim/ext/transport/proto/__init__.py
--rw-r--r--   0 github     (503) staff       (20)      245 2023-01-13 20:10:23.000000 aim-4.0.0.dev1/aim/ext/transport/proto/health_pb2.py
--rw-r--r--   0 github     (503) staff       (20)     3991 2023-01-13 20:10:23.000000 aim-4.0.0.dev1/aim/ext/transport/proto/health_pb2_grpc.py
--rw-r--r--   0 github     (503) staff       (20)      259 2023-01-13 20:10:23.000000 aim-4.0.0.dev1/aim/ext/transport/proto/remote_router_pb2.py
--rw-r--r--   0 github     (503) staff       (20)     8855 2023-01-13 20:10:23.000000 aim-4.0.0.dev1/aim/ext/transport/proto/remote_router_pb2_grpc.py
--rw-r--r--   0 github     (503) staff       (20)      263 2023-01-13 20:10:23.000000 aim-4.0.0.dev1/aim/ext/transport/proto/remote_tracking_pb2.py
--rw-r--r--   0 github     (503) staff       (20)     9444 2023-01-13 20:10:23.000000 aim-4.0.0.dev1/aim/ext/transport/proto/remote_tracking_pb2_grpc.py
-drwxr-xr-x   0 github     (503) staff       (20)        0 2023-03-13 14:51:39.894809 aim-4.0.0.dev1/aim/ext/transport/proto/v3/
--rw-r--r--   0 github     (503) staff       (20)        0 2023-01-13 20:10:23.000000 aim-4.0.0.dev1/aim/ext/transport/proto/v3/__init__.py
--rw-r--r--   0 github     (503) staff       (20)     6195 2023-01-13 20:10:23.000000 aim-4.0.0.dev1/aim/ext/transport/proto/v3/health_pb2.py
--rw-r--r--   0 github     (503) staff       (20)    25245 2023-01-13 20:10:23.000000 aim-4.0.0.dev1/aim/ext/transport/proto/v3/remote_router_pb2.py
--rw-r--r--   0 github     (503) staff       (20)    37567 2023-01-13 20:10:23.000000 aim-4.0.0.dev1/aim/ext/transport/proto/v3/remote_tracking_pb2.py
-drwxr-xr-x   0 github     (503) staff       (20)        0 2023-03-13 14:51:39.895537 aim-4.0.0.dev1/aim/ext/transport/proto/v4/
--rw-r--r--   0 github     (503) staff       (20)        0 2023-01-13 20:10:23.000000 aim-4.0.0.dev1/aim/ext/transport/proto/v4/__init__.py
--rw-r--r--   0 github     (503) staff       (20)     1749 2023-01-13 20:10:23.000000 aim-4.0.0.dev1/aim/ext/transport/proto/v4/health_pb2.py
--rw-r--r--   0 github     (503) staff       (20)     4280 2023-01-13 20:10:23.000000 aim-4.0.0.dev1/aim/ext/transport/proto/v4/remote_router_pb2.py
--rw-r--r--   0 github     (503) staff       (20)     5662 2023-01-13 20:10:23.000000 aim-4.0.0.dev1/aim/ext/transport/proto/v4/remote_tracking_pb2.py
--rw-r--r--   0 github     (503) staff       (20)      428 2022-04-19 22:29:06.000000 aim-4.0.0.dev1/aim/ext/transport/remote_resource.py
--rw-r--r--   0 github     (503) staff       (20)     8078 2023-01-23 10:30:27.000000 aim-4.0.0.dev1/aim/ext/transport/remote_tracking.py
--rw-r--r--   0 github     (503) staff       (20)     3637 2023-01-13 20:10:23.000000 aim-4.0.0.dev1/aim/ext/transport/router.py
--rw-r--r--   0 github     (503) staff       (20)     3728 2022-11-18 00:13:03.000000 aim-4.0.0.dev1/aim/ext/transport/rpc_queue.py
--rw-r--r--   0 github     (503) staff       (20)     4609 2023-01-23 10:30:27.000000 aim-4.0.0.dev1/aim/ext/transport/server.py
--rw-r--r--   0 github     (503) staff       (20)     3419 2023-01-13 20:10:23.000000 aim-4.0.0.dev1/aim/ext/transport/worker.py
--rw-r--r--   0 github     (503) staff       (20)     2103 2022-08-20 12:34:00.000000 aim-4.0.0.dev1/aim/ext/utils.py
--rw-r--r--   0 github     (503) staff       (20)       92 2022-09-25 12:02:15.000000 aim-4.0.0.dev1/aim/fastai.py
--rw-r--r--   0 github     (503) staff       (20)      127 2023-01-13 20:10:23.000000 aim-4.0.0.dev1/aim/hf_dataset.py
--rw-r--r--   0 github     (503) staff       (20)      105 2022-04-19 22:29:06.000000 aim-4.0.0.dev1/aim/hugging_face.py
--rw-r--r--   0 github     (503) staff       (20)      103 2022-04-19 22:29:06.000000 aim-4.0.0.dev1/aim/keras.py
--rw-r--r--   0 github     (503) staff       (20)      103 2022-08-20 12:34:00.000000 aim-4.0.0.dev1/aim/keras_tuner.py
--rw-r--r--   0 github     (503) staff       (20)       98 2022-05-06 13:59:46.000000 aim-4.0.0.dev1/aim/lightgbm.py
--rw-r--r--   0 github     (503) staff       (20)       97 2022-10-04 00:16:28.000000 aim-4.0.0.dev1/aim/mxnet.py
--rw-r--r--   0 github     (503) staff       (20)       98 2022-11-12 00:14:35.000000 aim-4.0.0.dev1/aim/optuna.py
--rw-r--r--   0 github     (503) staff       (20)       99 2022-11-12 00:14:35.000000 aim-4.0.0.dev1/aim/paddle.py
--rw-r--r--   0 github     (503) staff       (20)       93 2023-01-31 20:08:25.000000 aim-4.0.0.dev1/aim/prophet.py
--rw-r--r--   0 github     (503) staff       (20)      115 2022-04-19 22:29:06.000000 aim-4.0.0.dev1/aim/pytorch.py
--rw-r--r--   0 github     (503) staff       (20)      107 2022-04-19 22:29:06.000000 aim-4.0.0.dev1/aim/pytorch_ignite.py
--rw-r--r--   0 github     (503) staff       (20)      113 2022-04-19 22:29:06.000000 aim-4.0.0.dev1/aim/pytorch_lightning.py
--rw-r--r--   0 github     (503) staff       (20)       87 2023-01-13 20:10:23.000000 aim-4.0.0.dev1/aim/sb3.py
-drwxr-xr-x   0 github     (503) staff       (20)        0 2023-03-13 14:51:39.902017 aim-4.0.0.dev1/aim/sdk/
--rw-r--r--   0 github     (503) staff       (20)      915 2022-11-25 20:09:54.000000 aim-4.0.0.dev1/aim/sdk/__init__.py
-drwxr-xr-x   0 github     (503) staff       (20)        0 2023-03-13 14:51:39.906200 aim-4.0.0.dev1/aim/sdk/adapters/
--rw-r--r--   0 github     (503) staff       (20)        0 2022-04-19 22:29:06.000000 aim-4.0.0.dev1/aim/sdk/adapters/__init__.py
--rw-r--r--   0 github     (503) staff       (20)     2609 2023-03-02 20:49:40.000000 aim-4.0.0.dev1/aim/sdk/adapters/acme.py
--rw-r--r--   0 github     (503) staff       (20)     3371 2023-03-02 20:49:40.000000 aim-4.0.0.dev1/aim/sdk/adapters/catboost.py
--rw-r--r--   0 github     (503) staff       (20)     5510 2023-03-02 20:49:40.000000 aim-4.0.0.dev1/aim/sdk/adapters/fastai.py
--rw-r--r--   0 github     (503) staff       (20)     5620 2023-03-02 20:49:40.000000 aim-4.0.0.dev1/aim/sdk/adapters/hugging_face.py
--rw-r--r--   0 github     (503) staff       (20)     2579 2023-03-02 20:49:40.000000 aim-4.0.0.dev1/aim/sdk/adapters/keras.py
--rw-r--r--   0 github     (503) staff       (20)     1128 2022-04-19 22:29:06.000000 aim-4.0.0.dev1/aim/sdk/adapters/keras_mixins.py
--rw-r--r--   0 github     (503) staff       (20)     2805 2023-03-02 20:49:40.000000 aim-4.0.0.dev1/aim/sdk/adapters/keras_tuner.py
--rw-r--r--   0 github     (503) staff       (20)     3266 2023-03-02 20:49:40.000000 aim-4.0.0.dev1/aim/sdk/adapters/lightgbm.py
--rw-r--r--   0 github     (503) staff       (20)     8261 2023-03-02 20:49:40.000000 aim-4.0.0.dev1/aim/sdk/adapters/mxnet.py
--rw-r--r--   0 github     (503) staff       (20)     7159 2023-03-02 20:49:40.000000 aim-4.0.0.dev1/aim/sdk/adapters/optuna.py
--rw-r--r--   0 github     (503) staff       (20)     3495 2023-03-02 20:49:40.000000 aim-4.0.0.dev1/aim/sdk/adapters/paddle.py
--rw-r--r--   0 github     (503) staff       (20)     2911 2023-03-02 20:49:40.000000 aim-4.0.0.dev1/aim/sdk/adapters/prophet.py
--rw-r--r--   0 github     (503) staff       (20)     2458 2022-07-09 00:13:12.000000 aim-4.0.0.dev1/aim/sdk/adapters/pytorch.py
--rw-r--r--   0 github     (503) staff       (20)     9025 2023-03-02 20:49:40.000000 aim-4.0.0.dev1/aim/sdk/adapters/pytorch_ignite.py
--rw-r--r--   0 github     (503) staff       (20)     5602 2023-03-02 20:49:40.000000 aim-4.0.0.dev1/aim/sdk/adapters/pytorch_lightning.py
--rw-r--r--   0 github     (503) staff       (20)     4533 2023-03-02 20:49:40.000000 aim-4.0.0.dev1/aim/sdk/adapters/sb3.py
--rw-r--r--   0 github     (503) staff       (20)     2600 2023-03-02 20:49:40.000000 aim-4.0.0.dev1/aim/sdk/adapters/tensorflow.py
--rw-r--r--   0 github     (503) staff       (20)     2934 2023-03-02 20:49:40.000000 aim-4.0.0.dev1/aim/sdk/adapters/xgboost.py
--rw-r--r--   0 github     (503) staff       (20)     5109 2023-01-24 20:09:40.000000 aim-4.0.0.dev1/aim/sdk/base_run.py
-drwxr-xr-x   0 github     (503) staff       (20)        0 2023-03-13 14:51:39.907035 aim-4.0.0.dev1/aim/sdk/callbacks/
--rw-r--r--   0 github     (503) staff       (20)      196 2022-11-25 20:09:54.000000 aim-4.0.0.dev1/aim/sdk/callbacks/__init__.py
--rw-r--r--   0 github     (503) staff       (20)     1493 2022-11-25 20:09:54.000000 aim-4.0.0.dev1/aim/sdk/callbacks/caller.py
--rw-r--r--   0 github     (503) staff       (20)      495 2022-11-25 20:09:54.000000 aim-4.0.0.dev1/aim/sdk/callbacks/events.py
--rw-r--r--   0 github     (503) staff       (20)     1416 2022-11-25 20:09:54.000000 aim-4.0.0.dev1/aim/sdk/callbacks/helpers.py
--rw-r--r--   0 github     (503) staff       (20)      253 2022-09-26 00:13:35.000000 aim-4.0.0.dev1/aim/sdk/configs.py
--rw-r--r--   0 github     (503) staff       (20)       22 2022-11-24 20:09:30.000000 aim-4.0.0.dev1/aim/sdk/data_version.py
--rw-r--r--   0 github     (503) staff       (20)      145 2022-11-25 20:09:54.000000 aim-4.0.0.dev1/aim/sdk/errors.py
--rw-r--r--   0 github     (503) staff       (20)     4990 2023-01-23 20:08:00.000000 aim-4.0.0.dev1/aim/sdk/index_manager.py
-drwxr-xr-x   0 github     (503) staff       (20)        0 2023-03-13 14:51:39.908074 aim-4.0.0.dev1/aim/sdk/legacy/
--rw-r--r--   0 github     (503) staff       (20)        0 2022-04-19 22:29:06.000000 aim-4.0.0.dev1/aim/sdk/legacy/__init__.py
--rw-r--r--   0 github     (503) staff       (20)      288 2022-04-19 22:29:06.000000 aim-4.0.0.dev1/aim/sdk/legacy/deprecation_warning.py
--rw-r--r--   0 github     (503) staff       (20)       94 2022-04-19 22:29:06.000000 aim-4.0.0.dev1/aim/sdk/legacy/flush.py
--rw-r--r--   0 github     (503) staff       (20)      185 2022-04-19 22:29:06.000000 aim-4.0.0.dev1/aim/sdk/legacy/init.py
--rw-r--r--   0 github     (503) staff       (20)      702 2022-04-19 22:29:06.000000 aim-4.0.0.dev1/aim/sdk/legacy/select.py
-drwxr-xr-x   0 github     (503) staff       (20)        0 2023-03-13 14:51:39.908567 aim-4.0.0.dev1/aim/sdk/legacy/session/
--rw-r--r--   0 github     (503) staff       (20)       67 2022-04-19 22:29:06.000000 aim-4.0.0.dev1/aim/sdk/legacy/session/__init__.py
--rw-r--r--   0 github     (503) staff       (20)       30 2022-04-19 22:29:06.000000 aim-4.0.0.dev1/aim/sdk/legacy/session/configs.py
--rw-r--r--   0 github     (503) staff       (20)     4277 2022-04-19 22:29:06.000000 aim-4.0.0.dev1/aim/sdk/legacy/session/session.py
--rw-r--r--   0 github     (503) staff       (20)      410 2022-04-19 22:29:06.000000 aim-4.0.0.dev1/aim/sdk/legacy/track.py
--rw-r--r--   0 github     (503) staff       (20)     6513 2023-02-01 20:08:30.000000 aim-4.0.0.dev1/aim/sdk/lock_manager.py
-drwxr-xr-x   0 github     (503) staff       (20)        0 2023-03-13 14:51:39.908902 aim-4.0.0.dev1/aim/sdk/logging/
--rw-r--r--   0 github     (503) staff       (20)       61 2022-11-25 20:09:54.000000 aim-4.0.0.dev1/aim/sdk/logging/__init__.py
--rw-r--r--   0 github     (503) staff       (20)     1863 2023-02-03 15:21:38.000000 aim-4.0.0.dev1/aim/sdk/logging/log_record.py
--rw-r--r--   0 github     (503) staff       (20)      954 2022-11-25 20:09:54.000000 aim-4.0.0.dev1/aim/sdk/maintenance_run.py
--rw-r--r--   0 github     (503) staff       (20)     3273 2022-10-06 17:29:25.000000 aim-4.0.0.dev1/aim/sdk/num_utils.py
-drwxr-xr-x   0 github     (503) staff       (20)        0 2023-03-13 14:51:39.910077 aim-4.0.0.dev1/aim/sdk/objects/
--rw-r--r--   0 github     (503) staff       (20)      214 2022-04-19 22:29:06.000000 aim-4.0.0.dev1/aim/sdk/objects/__init__.py
--rw-r--r--   0 github     (503) staff       (20)     3264 2022-11-11 08:24:45.000000 aim-4.0.0.dev1/aim/sdk/objects/audio.py
--rw-r--r--   0 github     (503) staff       (20)     4232 2023-01-04 20:08:59.000000 aim-4.0.0.dev1/aim/sdk/objects/distribution.py
--rw-r--r--   0 github     (503) staff       (20)     2885 2023-01-04 20:08:59.000000 aim-4.0.0.dev1/aim/sdk/objects/figure.py
--rw-r--r--   0 github     (503) staff       (20)     9914 2023-03-03 20:09:01.000000 aim-4.0.0.dev1/aim/sdk/objects/image.py
-drwxr-xr-x   0 github     (503) staff       (20)        0 2023-03-13 14:51:39.910452 aim-4.0.0.dev1/aim/sdk/objects/io/
--rw-r--r--   0 github     (503) staff       (20)        0 2022-04-19 22:29:06.000000 aim-4.0.0.dev1/aim/sdk/objects/io/__init__.py
--rw-r--r--   0 github     (503) staff       (20)    21094 2022-04-19 22:29:06.000000 aim-4.0.0.dev1/aim/sdk/objects/io/wavfile.py
-drwxr-xr-x   0 github     (503) staff       (20)        0 2023-03-13 14:51:39.911587 aim-4.0.0.dev1/aim/sdk/objects/plugins/
--rw-r--r--   0 github     (503) staff       (20)        0 2022-04-19 22:29:06.000000 aim-4.0.0.dev1/aim/sdk/objects/plugins/__init__.py
--rw-r--r--   0 github     (503) staff       (20)     1983 2023-01-23 20:08:00.000000 aim-4.0.0.dev1/aim/sdk/objects/plugins/dvc_metadata.py
--rw-r--r--   0 github     (503) staff       (20)     3648 2023-02-02 20:09:54.000000 aim-4.0.0.dev1/aim/sdk/objects/plugins/hf_datasets_metadata.py
--rw-r--r--   0 github     (503) staff       (20)     1272 2022-04-19 22:29:06.000000 aim-4.0.0.dev1/aim/sdk/objects/plugins/hub_dataset.py
--rw-r--r--   0 github     (503) staff       (20)      694 2022-04-19 22:29:06.000000 aim-4.0.0.dev1/aim/sdk/objects/text.py
--rw-r--r--   0 github     (503) staff       (20)     6048 2022-09-01 19:23:53.000000 aim-4.0.0.dev1/aim/sdk/query_utils.py
--rw-r--r--   0 github     (503) staff       (20)     1050 2023-01-23 10:30:27.000000 aim-4.0.0.dev1/aim/sdk/remote_repo_proxy.py
--rw-r--r--   0 github     (503) staff       (20)     2171 2023-01-23 10:30:27.000000 aim-4.0.0.dev1/aim/sdk/remote_run_reporter.py
--rw-r--r--   0 github     (503) staff       (20)    34519 2023-03-03 20:09:01.000000 aim-4.0.0.dev1/aim/sdk/repo.py
--rw-r--r--   0 github     (503) staff       (20)      929 2022-06-15 14:05:59.000000 aim-4.0.0.dev1/aim/sdk/repo_utils.py
-drwxr-xr-x   0 github     (503) staff       (20)        0 2023-03-13 14:51:39.912268 aim-4.0.0.dev1/aim/sdk/reporter/
--rw-r--r--   0 github     (503) staff       (20)    31012 2023-01-23 20:08:00.000000 aim-4.0.0.dev1/aim/sdk/reporter/__init__.py
--rw-r--r--   0 github     (503) staff       (20)     1832 2023-01-23 10:30:27.000000 aim-4.0.0.dev1/aim/sdk/reporter/file_manager.py
--rw-r--r--   0 github     (503) staff       (20)    30746 2023-03-03 20:09:01.000000 aim-4.0.0.dev1/aim/sdk/run.py
--rw-r--r--   0 github     (503) staff       (20)    13171 2023-02-03 15:21:38.000000 aim-4.0.0.dev1/aim/sdk/run_status_watcher.py
--rw-r--r--   0 github     (503) staff       (20)    12970 2023-03-02 20:49:40.000000 aim-4.0.0.dev1/aim/sdk/sequence.py
--rw-r--r--   0 github     (503) staff       (20)     9944 2022-07-21 10:42:47.000000 aim-4.0.0.dev1/aim/sdk/sequence_collection.py
-drwxr-xr-x   0 github     (503) staff       (20)        0 2023-03-13 14:51:39.913731 aim-4.0.0.dev1/aim/sdk/sequences/
--rw-r--r--   0 github     (503) staff       (20)        0 2022-04-19 22:29:06.000000 aim-4.0.0.dev1/aim/sdk/sequences/__init__.py
--rw-r--r--   0 github     (503) staff       (20)      458 2022-04-19 22:29:06.000000 aim-4.0.0.dev1/aim/sdk/sequences/audio_sequence.py
--rw-r--r--   0 github     (503) staff       (20)      408 2023-03-02 20:49:40.000000 aim-4.0.0.dev1/aim/sdk/sequences/distribution_sequence.py
--rw-r--r--   0 github     (503) staff       (20)      452 2023-03-02 20:49:40.000000 aim-4.0.0.dev1/aim/sdk/sequences/figure_sequence.py
--rw-r--r--   0 github     (503) staff       (20)      482 2022-04-19 22:29:06.000000 aim-4.0.0.dev1/aim/sdk/sequences/image_sequence.py
--rw-r--r--   0 github     (503) staff       (20)     3936 2022-07-09 00:13:12.000000 aim-4.0.0.dev1/aim/sdk/sequences/metric.py
--rw-r--r--   0 github     (503) staff       (20)      458 2022-04-19 22:29:06.000000 aim-4.0.0.dev1/aim/sdk/sequences/text_sequence.py
--rw-r--r--   0 github     (503) staff       (20)    10545 2022-09-25 12:02:15.000000 aim-4.0.0.dev1/aim/sdk/tracker.py
--rw-r--r--   0 github     (503) staff       (20)     2202 2023-03-02 20:49:40.000000 aim-4.0.0.dev1/aim/sdk/training_flow.py
--rw-r--r--   0 github     (503) staff       (20)      159 2022-06-18 00:13:24.000000 aim-4.0.0.dev1/aim/sdk/types.py
--rw-r--r--   0 github     (503) staff       (20)     2940 2022-04-19 22:29:06.000000 aim-4.0.0.dev1/aim/sdk/uri_service.py
--rw-r--r--   0 github     (503) staff       (20)     4046 2022-11-25 20:09:54.000000 aim-4.0.0.dev1/aim/sdk/utils.py
-drwxr-xr-x   0 github     (503) staff       (20)        0 2023-03-13 14:51:39.926758 aim-4.0.0.dev1/aim/storage/
--rw-r--r--   0 github     (503) staff       (20)        0 2022-04-19 22:29:06.000000 aim-4.0.0.dev1/aim/storage/__init__.py
--rw-r--r--   0 github     (503) staff       (20)   439810 2023-03-13 14:51:36.000000 aim-4.0.0.dev1/aim/storage/arrayview.cpp
--rw-r--r--   0 github     (503) staff       (20)      278 2022-04-19 22:29:06.000000 aim-4.0.0.dev1/aim/storage/arrayview.pxd
--rw-r--r--   0 github     (503) staff       (20)     2649 2022-06-15 14:05:59.000000 aim-4.0.0.dev1/aim/storage/arrayview.py
--rw-r--r--   0 github     (503) staff       (20)   844368 2023-03-13 14:51:36.000000 aim-4.0.0.dev1/aim/storage/container.cpp
--rw-r--r--   0 github     (503) staff       (20)      951 2022-04-19 22:29:06.000000 aim-4.0.0.dev1/aim/storage/container.pxd
--rw-r--r--   0 github     (503) staff       (20)    10477 2022-04-19 22:29:06.000000 aim-4.0.0.dev1/aim/storage/container.py
--rw-r--r--   0 github     (503) staff       (20)   912217 2023-03-13 14:51:37.000000 aim-4.0.0.dev1/aim/storage/containertreeview.cpp
--rw-r--r--   0 github     (503) staff       (20)      313 2022-04-19 22:29:06.000000 aim-4.0.0.dev1/aim/storage/containertreeview.pxd
--rw-r--r--   0 github     (503) staff       (20)     6026 2023-01-24 20:09:40.000000 aim-4.0.0.dev1/aim/storage/containertreeview.py
--rw-r--r--   0 github     (503) staff       (20)     1212 2022-06-15 14:05:59.000000 aim-4.0.0.dev1/aim/storage/context.py
-drwxr-xr-x   0 github     (503) staff       (20)        0 2023-03-13 14:51:39.928218 aim-4.0.0.dev1/aim/storage/encoding/
--rw-r--r--   0 github     (503) staff       (20)   148655 2023-03-13 14:51:37.000000 aim-4.0.0.dev1/aim/storage/encoding/__init__.cpp
--rw-r--r--   0 github     (503) staff       (20)      155 2022-04-19 22:29:06.000000 aim-4.0.0.dev1/aim/storage/encoding/__init__.pxd
--rw-r--r--   0 github     (503) staff       (20)       95 2022-04-19 22:29:06.000000 aim-4.0.0.dev1/aim/storage/encoding/__init__.py
--rw-r--r--   0 github     (503) staff       (20)   378105 2023-03-13 14:51:37.000000 aim-4.0.0.dev1/aim/storage/encoding/encoding.cpp
--rw-r--r--   0 github     (503) staff       (20)      507 2022-04-19 22:29:06.000000 aim-4.0.0.dev1/aim/storage/encoding/encoding.pxd
--rw-r--r--   0 github     (503) staff       (20)     7373 2022-04-19 22:29:06.000000 aim-4.0.0.dev1/aim/storage/encoding/encoding.pyx
--rw-r--r--   0 github     (503) staff       (20)   353597 2023-03-13 14:51:37.000000 aim-4.0.0.dev1/aim/storage/encoding/encoding_native.cpp
--rw-r--r--   0 github     (503) staff       (20)      930 2022-04-19 22:29:06.000000 aim-4.0.0.dev1/aim/storage/encoding/encoding_native.pxd
--rw-r--r--   0 github     (503) staff       (20)     5974 2022-04-19 22:29:06.000000 aim-4.0.0.dev1/aim/storage/encoding/encoding_native.pyx
--rw-r--r--   0 github     (503) staff       (20)      337 2022-04-19 22:29:06.000000 aim-4.0.0.dev1/aim/storage/env.py
-drwxr-xr-x   0 github     (503) staff       (20)        0 2023-03-13 14:51:39.929549 aim-4.0.0.dev1/aim/storage/hashing/
--rw-r--r--   0 github     (503) staff       (20)   141729 2023-03-13 14:51:37.000000 aim-4.0.0.dev1/aim/storage/hashing/__init__.cpp
--rw-r--r--   0 github     (503) staff       (20)       85 2022-04-19 22:29:06.000000 aim-4.0.0.dev1/aim/storage/hashing/__init__.pxd
--rw-r--r--   0 github     (503) staff       (20)       50 2022-04-19 22:29:06.000000 aim-4.0.0.dev1/aim/storage/hashing/__init__.py
--rw-r--r--   0 github     (503) staff       (20)   205598 2023-03-13 14:51:37.000000 aim-4.0.0.dev1/aim/storage/hashing/c_hash.cpp
--rw-r--r--   0 github     (503) staff       (20)      151 2022-04-19 22:29:06.000000 aim-4.0.0.dev1/aim/storage/hashing/c_hash.pxd
--rw-r--r--   0 github     (503) staff       (20)     1077 2022-04-19 22:29:06.000000 aim-4.0.0.dev1/aim/storage/hashing/c_hash.pyx
-drwxr-xr-x   0 github     (503) staff       (20)        0 2023-03-13 14:51:39.929660 aim-4.0.0.dev1/aim/storage/hashing/hash/
--rw-r--r--   0 github     (503) staff       (20)     1412 2022-04-19 22:29:06.000000 aim-4.0.0.dev1/aim/storage/hashing/hash/hash.h
--rw-r--r--   0 github     (503) staff       (20)   392224 2023-03-13 14:51:37.000000 aim-4.0.0.dev1/aim/storage/hashing/hashing.cpp
--rw-r--r--   0 github     (503) staff       (20)     1009 2022-04-19 22:29:06.000000 aim-4.0.0.dev1/aim/storage/hashing/hashing.pxd
--rw-r--r--   0 github     (503) staff       (20)     5562 2023-01-24 20:09:40.000000 aim-4.0.0.dev1/aim/storage/hashing/hashing.py
--rw-r--r--   0 github     (503) staff       (20)   672756 2023-03-13 14:51:37.000000 aim-4.0.0.dev1/aim/storage/inmemorytreeview.cpp
--rw-r--r--   0 github     (503) staff       (20)      196 2022-04-19 22:29:06.000000 aim-4.0.0.dev1/aim/storage/inmemorytreeview.pxd
--rw-r--r--   0 github     (503) staff       (20)     4341 2023-01-24 20:09:40.000000 aim-4.0.0.dev1/aim/storage/inmemorytreeview.py
--rw-r--r--   0 github     (503) staff       (20)     1322 2022-11-25 20:09:54.000000 aim-4.0.0.dev1/aim/storage/lock_proxy.py
--rw-r--r--   0 github     (503) staff       (20)     6336 2022-12-01 15:54:09.000000 aim-4.0.0.dev1/aim/storage/locking.py
-drwxr-xr-x   0 github     (503) staff       (20)        0 2023-03-13 14:51:39.930974 aim-4.0.0.dev1/aim/storage/migrations/
--rw-r--r--   0 github     (503) staff       (20)       38 2022-04-19 22:29:06.000000 aim-4.0.0.dev1/aim/storage/migrations/README
--rw-r--r--   0 github     (503) staff       (20)        0 2022-04-19 22:29:06.000000 aim-4.0.0.dev1/aim/storage/migrations/__init__.py
--rw-r--r--   0 github     (503) staff       (20)     2218 2022-04-19 22:29:06.000000 aim-4.0.0.dev1/aim/storage/migrations/alembic.ini
--rw-r--r--   0 github     (503) staff       (20)     2215 2022-04-19 22:29:06.000000 aim-4.0.0.dev1/aim/storage/migrations/alembic_dev.ini
--rw-r--r--   0 github     (503) staff       (20)     2339 2022-04-19 22:29:06.000000 aim-4.0.0.dev1/aim/storage/migrations/env.py
--rw-r--r--   0 github     (503) staff       (20)      494 2022-04-19 22:29:06.000000 aim-4.0.0.dev1/aim/storage/migrations/script.py.mako
--rw-r--r--   0 github     (503) staff       (20)      965 2022-04-19 22:29:06.000000 aim-4.0.0.dev1/aim/storage/migrations/utils.py
-drwxr-xr-x   0 github     (503) staff       (20)        0 2023-03-13 14:51:39.932212 aim-4.0.0.dev1/aim/storage/migrations/versions/
--rw-r--r--   0 github     (503) staff       (20)     2841 2022-04-19 22:29:06.000000 aim-4.0.0.dev1/aim/storage/migrations/versions/1ecf8222220d_initial_schema.py
--rw-r--r--   0 github     (503) staff       (20)      658 2022-04-19 22:29:06.000000 aim-4.0.0.dev1/aim/storage/migrations/versions/3c4f22db7a46_run_end_time.py
--rw-r--r--   0 github     (503) staff       (20)     1475 2022-11-25 20:09:54.000000 aim-4.0.0.dev1/aim/storage/migrations/versions/46b89d830ad8_.py
--rw-r--r--   0 github     (503) staff       (20)      653 2022-04-19 22:29:06.000000 aim-4.0.0.dev1/aim/storage/migrations/versions/9ba30ab3b2b4_.py
--rw-r--r--   0 github     (503) staff       (20)     1516 2022-04-19 22:29:06.000000 aim-4.0.0.dev1/aim/storage/migrations/versions/b07e7b07c8ce_.py
--rw-r--r--   0 github     (503) staff       (20)      789 2022-04-19 22:29:06.000000 aim-4.0.0.dev1/aim/storage/migrations/versions/fbfe5c4702fb_soft_delete.py
--rw-r--r--   0 github     (503) staff       (20)     1650 2022-04-19 22:29:06.000000 aim-4.0.0.dev1/aim/storage/object.py
--rw-r--r--   0 github     (503) staff       (20)   959785 2023-03-13 14:51:38.000000 aim-4.0.0.dev1/aim/storage/prefixview.cpp
--rw-r--r--   0 github     (503) staff       (20)      770 2022-04-19 22:29:06.000000 aim-4.0.0.dev1/aim/storage/prefixview.pxd
--rw-r--r--   0 github     (503) staff       (20)    11248 2022-04-19 22:29:06.000000 aim-4.0.0.dev1/aim/storage/prefixview.py
--rw-r--r--   0 github     (503) staff       (20)    11648 2022-06-15 14:05:59.000000 aim-4.0.0.dev1/aim/storage/proxy.py
--rw-r--r--   0 github     (503) staff       (20)     4816 2022-07-21 10:42:47.000000 aim-4.0.0.dev1/aim/storage/query.py
--rw-r--r--   0 github     (503) staff       (20)  1056280 2023-03-13 14:51:38.000000 aim-4.0.0.dev1/aim/storage/rockscontainer.cpp
--rw-r--r--   0 github     (503) staff       (20)    18514 2023-01-23 20:08:00.000000 aim-4.0.0.dev1/aim/storage/rockscontainer.pyx
-drwxr-xr-x   0 github     (503) staff       (20)        0 2023-03-13 14:51:39.932925 aim-4.0.0.dev1/aim/storage/structured/
--rw-r--r--   0 github     (503) staff       (20)        0 2022-04-19 22:29:06.000000 aim-4.0.0.dev1/aim/storage/structured/__init__.py
--rw-r--r--   0 github     (503) staff       (20)     3183 2022-04-19 22:29:06.000000 aim-4.0.0.dev1/aim/storage/structured/db.py
--rw-r--r--   0 github     (503) staff       (20)     5355 2022-11-25 20:09:54.000000 aim-4.0.0.dev1/aim/storage/structured/entities.py
--rw-r--r--   0 github     (503) staff       (20)     2959 2022-11-12 00:14:35.000000 aim-4.0.0.dev1/aim/storage/structured/proxy.py
-drwxr-xr-x   0 github     (503) staff       (20)        0 2023-03-13 14:51:39.934113 aim-4.0.0.dev1/aim/storage/structured/sql_engine/
--rw-r--r--   0 github     (503) staff       (20)        0 2022-04-19 22:29:06.000000 aim-4.0.0.dev1/aim/storage/structured/sql_engine/__init__.py
--rw-r--r--   0 github     (503) staff       (20)    19882 2023-01-25 20:08:55.000000 aim-4.0.0.dev1/aim/storage/structured/sql_engine/entities.py
--rw-r--r--   0 github     (503) staff       (20)     3484 2022-04-19 22:29:06.000000 aim-4.0.0.dev1/aim/storage/structured/sql_engine/factory.py
--rw-r--r--   0 github     (503) staff       (20)     4888 2022-11-25 20:09:54.000000 aim-4.0.0.dev1/aim/storage/structured/sql_engine/models.py
--rw-r--r--   0 github     (503) staff       (20)     4811 2022-04-19 22:29:06.000000 aim-4.0.0.dev1/aim/storage/structured/sql_engine/utils.py
--rw-r--r--   0 github     (503) staff       (20)   697830 2023-03-13 14:51:38.000000 aim-4.0.0.dev1/aim/storage/treearrayview.cpp
--rw-r--r--   0 github     (503) staff       (20)      251 2022-04-19 22:29:06.000000 aim-4.0.0.dev1/aim/storage/treearrayview.pxd
--rw-r--r--   0 github     (503) staff       (20)     3033 2022-08-02 09:43:44.000000 aim-4.0.0.dev1/aim/storage/treearrayview.py
--rw-r--r--   0 github     (503) staff       (20)   722166 2023-03-13 14:51:38.000000 aim-4.0.0.dev1/aim/storage/treeutils.cpp
--rw-r--r--   0 github     (503) staff       (20)     8365 2022-06-15 14:05:59.000000 aim-4.0.0.dev1/aim/storage/treeutils.pyx
--rw-r--r--   0 github     (503) staff       (20)      707 2022-04-19 22:29:06.000000 aim-4.0.0.dev1/aim/storage/treeutils_non_native.py
--rw-r--r--   0 github     (503) staff       (20)   515752 2023-03-13 14:51:38.000000 aim-4.0.0.dev1/aim/storage/treeview.cpp
--rw-r--r--   0 github     (503) staff       (20)      311 2022-04-19 22:29:06.000000 aim-4.0.0.dev1/aim/storage/treeview.pxd
--rw-r--r--   0 github     (503) staff       (20)     2765 2023-01-24 20:09:40.000000 aim-4.0.0.dev1/aim/storage/treeview.py
--rw-r--r--   0 github     (503) staff       (20)     8241 2023-02-27 08:16:06.000000 aim-4.0.0.dev1/aim/storage/treeviewproxy.py
--rw-r--r--   0 github     (503) staff       (20)     1357 2022-04-19 22:29:06.000000 aim-4.0.0.dev1/aim/storage/types.py
--rw-r--r--   0 github     (503) staff       (20)   812526 2023-03-13 14:51:38.000000 aim-4.0.0.dev1/aim/storage/union.cpp
--rw-r--r--   0 github     (503) staff       (20)     7919 2023-01-23 20:08:00.000000 aim-4.0.0.dev1/aim/storage/union.pyx
--rw-r--r--   0 github     (503) staff       (20)   810540 2023-03-13 14:51:39.000000 aim-4.0.0.dev1/aim/storage/utils.cpp
--rw-r--r--   0 github     (503) staff       (20)      469 2022-04-19 22:29:06.000000 aim-4.0.0.dev1/aim/storage/utils.pxd
--rw-r--r--   0 github     (503) staff       (20)     2102 2022-04-19 22:29:06.000000 aim-4.0.0.dev1/aim/storage/utils.py
--rw-r--r--   0 github     (503) staff       (20)      119 2022-04-19 22:29:06.000000 aim-4.0.0.dev1/aim/tensorflow.py
-drwxr-xr-x   0 github     (503) staff       (20)        0 2023-03-13 14:51:39.934809 aim-4.0.0.dev1/aim/utils/
--rw-r--r--   0 github     (503) staff       (20)       84 2023-03-02 20:49:40.000000 aim-4.0.0.dev1/aim/utils/__init__.py
--rw-r--r--   0 github     (503) staff       (20)     1209 2023-02-01 20:08:30.000000 aim-4.0.0.dev1/aim/utils/deprecation.py
--rw-r--r--   0 github     (503) staff       (20)     4728 2023-02-27 08:16:06.000000 aim-4.0.0.dev1/aim/utils/tracking.py
-drwxr-xr-x   0 github     (503) staff       (20)        0 2023-03-13 14:51:39.935651 aim-4.0.0.dev1/aim/web/
--rw-r--r--   0 github     (503) staff       (20)        0 2022-04-19 22:29:06.000000 aim-4.0.0.dev1/aim/web/__init__.py
-drwxr-xr-x   0 github     (503) staff       (20)        0 2023-03-13 14:51:39.936649 aim-4.0.0.dev1/aim/web/api/
--rw-r--r--   0 github     (503) staff       (20)     3504 2023-01-23 10:30:27.000000 aim-4.0.0.dev1/aim/web/api/__init__.py
-drwxr-xr-x   0 github     (503) staff       (20)        0 2023-03-13 14:51:39.937569 aim-4.0.0.dev1/aim/web/api/dashboard_apps/
--rw-r--r--   0 github     (503) staff       (20)        0 2022-04-19 22:29:06.000000 aim-4.0.0.dev1/aim/web/api/dashboard_apps/__init__.py
--rw-r--r--   0 github     (503) staff       (20)      939 2022-04-19 22:29:06.000000 aim-4.0.0.dev1/aim/web/api/dashboard_apps/models.py
--rw-r--r--   0 github     (503) staff       (20)      542 2022-04-19 22:29:06.000000 aim-4.0.0.dev1/aim/web/api/dashboard_apps/pydantic_models.py
--rw-r--r--   0 github     (503) staff       (20)      445 2022-04-19 22:29:06.000000 aim-4.0.0.dev1/aim/web/api/dashboard_apps/serializers.py
--rw-r--r--   0 github     (503) staff       (20)     2974 2022-04-19 22:29:06.000000 aim-4.0.0.dev1/aim/web/api/dashboard_apps/views.py
-drwxr-xr-x   0 github     (503) staff       (20)        0 2023-03-13 14:51:39.938485 aim-4.0.0.dev1/aim/web/api/dashboards/
--rw-r--r--   0 github     (503) staff       (20)        0 2022-04-19 22:29:06.000000 aim-4.0.0.dev1/aim/web/api/dashboards/__init__.py
--rw-r--r--   0 github     (503) staff       (20)      667 2022-04-19 22:29:06.000000 aim-4.0.0.dev1/aim/web/api/dashboards/models.py
--rw-r--r--   0 github     (503) staff       (20)      652 2022-10-06 00:17:33.000000 aim-4.0.0.dev1/aim/web/api/dashboards/pydantic_models.py
--rw-r--r--   0 github     (503) staff       (20)      775 2022-10-06 00:17:33.000000 aim-4.0.0.dev1/aim/web/api/dashboards/serializers.py
--rw-r--r--   0 github     (503) staff       (20)     3341 2022-04-19 22:29:06.000000 aim-4.0.0.dev1/aim/web/api/dashboards/views.py
--rw-r--r--   0 github     (503) staff       (20)      820 2022-04-19 22:29:06.000000 aim-4.0.0.dev1/aim/web/api/db.py
-drwxr-xr-x   0 github     (503) staff       (20)        0 2023-03-13 14:51:39.938988 aim-4.0.0.dev1/aim/web/api/experiments/
--rw-r--r--   0 github     (503) staff       (20)        0 2022-04-19 22:29:06.000000 aim-4.0.0.dev1/aim/web/api/experiments/__init__.py
--rw-r--r--   0 github     (503) staff       (20)      974 2022-11-24 20:09:30.000000 aim-4.0.0.dev1/aim/web/api/experiments/pydantic_models.py
--rw-r--r--   0 github     (503) staff       (20)     8931 2023-01-19 20:08:35.000000 aim-4.0.0.dev1/aim/web/api/experiments/views.py
-drwxr-xr-x   0 github     (503) staff       (20)        0 2023-03-13 14:51:39.939823 aim-4.0.0.dev1/aim/web/api/projects/
--rw-r--r--   0 github     (503) staff       (20)        0 2022-04-19 22:29:06.000000 aim-4.0.0.dev1/aim/web/api/projects/__init__.py
--rw-r--r--   0 github     (503) staff       (20)      735 2022-04-19 22:29:06.000000 aim-4.0.0.dev1/aim/web/api/projects/project.py
--rw-r--r--   0 github     (503) staff       (20)      943 2022-10-06 00:17:33.000000 aim-4.0.0.dev1/aim/web/api/projects/pydantic_models.py
--rw-r--r--   0 github     (503) staff       (20)     5200 2023-01-24 20:09:40.000000 aim-4.0.0.dev1/aim/web/api/projects/views.py
-drwxr-xr-x   0 github     (503) staff       (20)        0 2023-03-13 14:51:39.942425 aim-4.0.0.dev1/aim/web/api/runs/
--rw-r--r--   0 github     (503) staff       (20)        0 2022-04-19 22:29:06.000000 aim-4.0.0.dev1/aim/web/api/runs/__init__.py
--rw-r--r--   0 github     (503) staff       (20)    12969 2022-07-21 10:42:47.000000 aim-4.0.0.dev1/aim/web/api/runs/object_api_utils.py
--rw-r--r--   0 github     (503) staff       (20)     6683 2022-07-21 10:42:47.000000 aim-4.0.0.dev1/aim/web/api/runs/object_views.py
--rw-r--r--   0 github     (503) staff       (20)     4420 2022-12-23 10:19:51.000000 aim-4.0.0.dev1/aim/web/api/runs/pydantic_models.py
--rw-r--r--   0 github     (503) staff       (20)    15418 2023-02-03 15:21:38.000000 aim-4.0.0.dev1/aim/web/api/runs/utils.py
--rw-r--r--   0 github     (503) staff       (20)    12137 2023-02-03 15:21:38.000000 aim-4.0.0.dev1/aim/web/api/runs/views.py
-drwxr-xr-x   0 github     (503) staff       (20)        0 2023-03-13 14:51:39.942952 aim-4.0.0.dev1/aim/web/api/tags/
--rw-r--r--   0 github     (503) staff       (20)        0 2022-04-19 22:29:06.000000 aim-4.0.0.dev1/aim/web/api/tags/__init__.py
--rw-r--r--   0 github     (503) staff       (20)      871 2022-04-19 22:29:06.000000 aim-4.0.0.dev1/aim/web/api/tags/pydantic_models.py
--rw-r--r--   0 github     (503) staff       (20)     4272 2022-04-19 22:29:06.000000 aim-4.0.0.dev1/aim/web/api/tags/views.py
--rw-r--r--   0 github     (503) staff       (20)     1169 2022-04-19 22:29:06.000000 aim-4.0.0.dev1/aim/web/api/utils.py
--rw-r--r--   0 github     (503) staff       (20)     1589 2022-05-16 21:25:24.000000 aim-4.0.0.dev1/aim/web/api/views.py
--rw-r--r--   0 github     (503) staff       (20)      508 2022-08-11 13:58:02.000000 aim-4.0.0.dev1/aim/web/configs.py
-drwxr-xr-x   0 github     (503) staff       (20)        0 2023-03-13 14:51:39.943126 aim-4.0.0.dev1/aim/web/middlewares/
--rw-r--r--   0 github     (503) staff       (20)        0 2022-04-19 22:29:06.000000 aim-4.0.0.dev1/aim/web/middlewares/__init__.py
-drwxr-xr-x   0 github     (503) staff       (20)        0 2023-03-13 14:51:39.943505 aim-4.0.0.dev1/aim/web/middlewares/profiler/
--rw-r--r--   0 github     (503) staff       (20)       81 2022-04-19 22:29:06.000000 aim-4.0.0.dev1/aim/web/middlewares/profiler/__init__.py
--rw-r--r--   0 github     (503) staff       (20)     3654 2022-04-19 22:29:06.000000 aim-4.0.0.dev1/aim/web/middlewares/profiler/profiler.py
-drwxr-xr-x   0 github     (503) staff       (20)        0 2023-03-13 14:51:39.944338 aim-4.0.0.dev1/aim/web/migrations/
--rw-r--r--   0 github     (503) staff       (20)       38 2022-04-19 22:29:06.000000 aim-4.0.0.dev1/aim/web/migrations/README
--rw-r--r--   0 github     (503) staff       (20)      810 2022-04-19 22:29:06.000000 aim-4.0.0.dev1/aim/web/migrations/alembic.ini
--rw-r--r--   0 github     (503) staff       (20)      807 2022-04-19 22:29:06.000000 aim-4.0.0.dev1/aim/web/migrations/alembic_dev.ini
--rw-r--r--   0 github     (503) staff       (20)     2792 2022-04-19 22:29:06.000000 aim-4.0.0.dev1/aim/web/migrations/env.py
--rw-r--r--   0 github     (503) staff       (20)      494 2022-04-19 22:29:06.000000 aim-4.0.0.dev1/aim/web/migrations/script.py.mako
-drwxr-xr-x   0 github     (503) staff       (20)        0 2023-03-13 14:51:39.944959 aim-4.0.0.dev1/aim/web/migrations/versions/
--rw-r--r--   0 github     (503) staff       (20)     2183 2022-04-19 22:29:06.000000 aim-4.0.0.dev1/aim/web/migrations/versions/11672b13f92c_.py
--rw-r--r--   0 github     (503) staff       (20)     1545 2022-04-19 22:29:06.000000 aim-4.0.0.dev1/aim/web/migrations/versions/517a45b2e62c_.py
--rw-r--r--   0 github     (503) staff       (20)     5592 2022-04-19 22:29:06.000000 aim-4.0.0.dev1/aim/web/migrations/versions/5ae8371b7481_.py
--rw-r--r--   0 github     (503) staff       (20)     7262 2022-04-19 22:29:06.000000 aim-4.0.0.dev1/aim/web/migrations/versions/73a3d004c227_.py
--rw-r--r--   0 github     (503) staff       (20)       55 2022-04-19 22:29:06.000000 aim-4.0.0.dev1/aim/web/run.py
--rw-r--r--   0 github     (503) staff       (20)     3055 2022-04-19 22:29:06.000000 aim-4.0.0.dev1/aim/web/utils.py
--rw-r--r--   0 github     (503) staff       (20)       96 2022-04-19 22:29:06.000000 aim-4.0.0.dev1/aim/xgboost.py
-drwxr-xr-x   0 github     (503) staff       (20)        0 2023-03-13 14:51:39.873687 aim-4.0.0.dev1/aim.egg-info/
--rw-r--r--   0 github     (503) staff       (20)    26572 2023-03-13 14:51:39.000000 aim-4.0.0.dev1/aim.egg-info/PKG-INFO
--rw-r--r--   0 github     (503) staff       (20)    11901 2023-03-13 14:51:39.000000 aim-4.0.0.dev1/aim.egg-info/SOURCES.txt
--rw-r--r--   0 github     (503) staff       (20)        1 2023-03-13 14:51:39.000000 aim-4.0.0.dev1/aim.egg-info/dependency_links.txt
--rw-r--r--   0 github     (503) staff       (20)      102 2023-03-13 14:51:39.000000 aim-4.0.0.dev1/aim.egg-info/entry_points.txt
--rw-r--r--   0 github     (503) staff       (20)      422 2023-03-13 14:51:39.000000 aim-4.0.0.dev1/aim.egg-info/requires.txt
--rw-r--r--   0 github     (503) staff       (20)       28 2023-03-13 14:51:39.000000 aim-4.0.0.dev1/aim.egg-info/top_level.txt
-drwxr-xr-x   0 github     (503) staff       (20)        0 2023-03-13 14:51:39.865575 aim-4.0.0.dev1/performance_tests/
-drwxr-xr-x   0 github     (503) staff       (20)        0 2023-03-13 14:51:39.945835 aim-4.0.0.dev1/performance_tests/sdk/
--rw-r--r--   0 github     (503) staff       (20)        0 2022-04-19 22:29:06.000000 aim-4.0.0.dev1/performance_tests/sdk/__init__.py
--rw-r--r--   0 github     (503) staff       (20)      469 2022-04-19 22:29:06.000000 aim-4.0.0.dev1/performance_tests/sdk/queries.py
--rw-r--r--   0 github     (503) staff       (20)     1199 2022-04-19 22:29:06.000000 aim-4.0.0.dev1/performance_tests/sdk/test_data_collection.py
--rw-r--r--   0 github     (503) staff       (20)     1134 2022-04-19 22:29:06.000000 aim-4.0.0.dev1/performance_tests/sdk/test_query.py
--rw-r--r--   0 github     (503) staff       (20)     1881 2022-06-18 00:13:24.000000 aim-4.0.0.dev1/performance_tests/sdk/utils.py
-drwxr-xr-x   0 github     (503) staff       (20)        0 2023-03-13 14:51:39.946732 aim-4.0.0.dev1/performance_tests/storage/
--rw-r--r--   0 github     (503) staff       (20)        0 2022-04-19 22:29:06.000000 aim-4.0.0.dev1/performance_tests/storage/__init__.py
--rw-r--r--   0 github     (503) staff       (20)      678 2022-04-19 22:29:06.000000 aim-4.0.0.dev1/performance_tests/storage/test_container_open.py
--rw-r--r--   0 github     (503) staff       (20)      690 2022-04-19 22:29:06.000000 aim-4.0.0.dev1/performance_tests/storage/test_iterative_access.py
--rw-r--r--   0 github     (503) staff       (20)      802 2022-04-19 22:29:06.000000 aim-4.0.0.dev1/performance_tests/storage/test_random_access.py
--rw-r--r--   0 github     (503) staff       (20)     1262 2022-06-18 00:13:24.000000 aim-4.0.0.dev1/performance_tests/storage/utils.py
--rw-r--r--   0 github     (503) staff       (20)       84 2023-03-02 20:49:40.000000 aim-4.0.0.dev1/pyproject.toml
--rw-r--r--   0 github     (503) staff       (20)      336 2023-03-13 14:51:39.952977 aim-4.0.0.dev1/setup.cfg
--rw-r--r--   0 github     (503) staff       (20)     6716 2023-03-02 20:49:40.000000 aim-4.0.0.dev1/setup.py
-drwxr-xr-x   0 github     (503) staff       (20)        0 2023-03-13 14:51:39.865876 aim-4.0.0.dev1/tests/
-drwxr-xr-x   0 github     (503) staff       (20)        0 2023-03-13 14:51:39.948515 aim-4.0.0.dev1/tests/api/
--rw-r--r--   0 github     (503) staff       (20)        0 2022-04-19 22:29:06.000000 aim-4.0.0.dev1/tests/api/__init__.py
--rw-r--r--   0 github     (503) staff       (20)     5155 2022-04-19 22:29:06.000000 aim-4.0.0.dev1/tests/api/test_dashboards_api.py
--rw-r--r--   0 github     (503) staff       (20)     4335 2022-09-25 12:02:15.000000 aim-4.0.0.dev1/tests/api/test_project_api.py
--rw-r--r--   0 github     (503) staff       (20)    10653 2023-01-23 10:30:27.000000 aim-4.0.0.dev1/tests/api/test_run_api.py
--rw-r--r--   0 github     (503) staff       (20)    21533 2023-01-23 10:30:27.000000 aim-4.0.0.dev1/tests/api/test_run_images_api.py
--rw-r--r--   0 github     (503) staff       (20)    12787 2023-01-23 10:30:27.000000 aim-4.0.0.dev1/tests/api/test_structured_data_api.py
-drwxr-xr-x   0 github     (503) staff       (20)        0 2023-03-13 14:51:39.949269 aim-4.0.0.dev1/tests/integrations/
--rw-r--r--   0 github     (503) staff       (20)        0 2022-04-19 22:29:06.000000 aim-4.0.0.dev1/tests/integrations/__init__.py
--rw-r--r--   0 github     (503) staff       (20)     1167 2022-04-19 22:29:06.000000 aim-4.0.0.dev1/tests/integrations/test_dvc_metadata.py
--rw-r--r--   0 github     (503) staff       (20)     1093 2023-01-13 20:10:23.000000 aim-4.0.0.dev1/tests/integrations/test_hf_datasets.py
--rw-r--r--   0 github     (503) staff       (20)      961 2022-04-19 22:29:06.000000 aim-4.0.0.dev1/tests/integrations/test_hub_dataset.py
-drwxr-xr-x   0 github     (503) staff       (20)        0 2023-03-13 14:51:39.951676 aim-4.0.0.dev1/tests/sdk/
--rw-r--r--   0 github     (503) staff       (20)        0 2022-04-19 22:29:06.000000 aim-4.0.0.dev1/tests/sdk/__init__.py
--rw-r--r--   0 github     (503) staff       (20)     2312 2022-04-19 22:29:06.000000 aim-4.0.0.dev1/tests/sdk/test_image_construction.py
--rw-r--r--   0 github     (503) staff       (20)     2665 2022-09-25 12:02:15.000000 aim-4.0.0.dev1/tests/sdk/test_resource_tracker.py
--rw-r--r--   0 github     (503) staff       (20)     1022 2022-11-01 00:13:35.000000 aim-4.0.0.dev1/tests/sdk/test_run_apis.py
--rw-r--r--   0 github     (503) staff       (20)     1147 2022-09-01 19:23:53.000000 aim-4.0.0.dev1/tests/sdk/test_run_creation_checks.py
--rw-r--r--   0 github     (503) staff       (20)     1661 2022-04-19 22:29:06.000000 aim-4.0.0.dev1/tests/sdk/test_run_finalization_time.py
--rw-r--r--   0 github     (503) staff       (20)     1214 2022-11-01 00:13:35.000000 aim-4.0.0.dev1/tests/sdk/test_run_metric_types.py
--rw-r--r--   0 github     (503) staff       (20)     4631 2022-09-25 12:02:15.000000 aim-4.0.0.dev1/tests/sdk/test_run_track_type_checking.py
--rw-r--r--   0 github     (503) staff       (20)    10444 2022-09-25 12:02:15.000000 aim-4.0.0.dev1/tests/sdk/test_run_write_container_data.py
--rw-r--r--   0 github     (503) staff       (20)     4517 2022-06-01 01:05:15.000000 aim-4.0.0.dev1/tests/sdk/test_utils.py
-drwxr-xr-x   0 github     (503) staff       (20)        0 2023-03-13 14:51:39.952423 aim-4.0.0.dev1/tests/storage/
--rw-r--r--   0 github     (503) staff       (20)        0 2022-04-19 22:29:06.000000 aim-4.0.0.dev1/tests/storage/__init__.py
--rw-r--r--   0 github     (503) staff       (20)     5677 2022-09-25 12:02:15.000000 aim-4.0.0.dev1/tests/storage/test_query.py
--rw-r--r--   0 github     (503) staff       (20)     1482 2022-06-18 00:13:24.000000 aim-4.0.0.dev1/tests/storage/test_query_with_epoch_none.py
--rw-r--r--   0 github     (503) staff       (20)     1342 2022-09-25 12:02:15.000000 aim-4.0.0.dev1/tests/storage/test_structured_db.py
+drwxr-xr-x   0 github     (503) staff       (20)        0 2023-04-05 11:38:00.768688 aim-4.0.0.dev2/
+-rw-r--r--   0 github     (503) staff       (20)    11347 2022-08-06 00:13:01.000000 aim-4.0.0.dev2/LICENSE
+-rw-r--r--   0 github     (503) staff       (20)      185 2022-04-19 22:29:06.000000 aim-4.0.0.dev2/MANIFEST.in
+-rw-r--r--   0 github     (503) staff       (20)    37083 2023-04-05 11:38:00.768831 aim-4.0.0.dev2/PKG-INFO
+-rw-r--r--   0 github     (503) staff       (20)    36396 2023-03-24 14:18:45.000000 aim-4.0.0.dev2/README.md
+drwxr-xr-x   0 github     (503) staff       (20)        0 2023-04-05 11:38:00.686277 aim-4.0.0.dev2/aim/
+-rw-r--r--   0 github     (503) staff       (20)       10 2023-04-05 11:37:51.000000 aim-4.0.0.dev2/aim/VERSION
+-rw-r--r--   0 github     (503) staff       (20)      825 2022-04-19 22:29:06.000000 aim-4.0.0.dev2/aim/__about__.py
+-rw-r--r--   0 github     (503) staff       (20)      377 2023-02-01 20:08:30.000000 aim-4.0.0.dev2/aim/__init__.py
+-rw-r--r--   0 github     (503) staff       (20)      183 2022-04-19 22:29:06.000000 aim-4.0.0.dev2/aim/__version__.py
+-rw-r--r--   0 github     (503) staff       (20)      100 2023-01-13 20:10:23.000000 aim-4.0.0.dev2/aim/acme.py
+-rw-r--r--   0 github     (503) staff       (20)       96 2022-05-06 13:59:46.000000 aim-4.0.0.dev2/aim/catboost.py
+drwxr-xr-x   0 github     (503) staff       (20)        0 2023-04-05 11:38:00.688501 aim-4.0.0.dev2/aim/cli/
+-rw-r--r--   0 github     (503) staff       (20)        0 2022-04-19 22:29:06.000000 aim-4.0.0.dev2/aim/cli/__init__.py
+-rw-r--r--   0 github     (503) staff       (20)     1323 2023-01-24 20:09:40.000000 aim-4.0.0.dev2/aim/cli/cli.py
+-rw-r--r--   0 github     (503) staff       (20)      166 2022-06-17 00:13:19.000000 aim-4.0.0.dev2/aim/cli/configs.py
+drwxr-xr-x   0 github     (503) staff       (20)        0 2023-04-05 11:38:00.688947 aim-4.0.0.dev2/aim/cli/convert/
+-rw-r--r--   0 github     (503) staff       (20)        0 2022-04-19 22:29:06.000000 aim-4.0.0.dev2/aim/cli/convert/__init__.py
+-rw-r--r--   0 github     (503) staff       (20)     2998 2022-08-20 12:34:00.000000 aim-4.0.0.dev2/aim/cli/convert/commands.py
+drwxr-xr-x   0 github     (503) staff       (20)        0 2023-04-05 11:38:00.689946 aim-4.0.0.dev2/aim/cli/convert/processors/
+-rw-r--r--   0 github     (503) staff       (20)      113 2022-08-20 12:34:00.000000 aim-4.0.0.dev2/aim/cli/convert/processors/__init__.py
+-rw-r--r--   0 github     (503) staff       (20)     5914 2022-09-01 19:23:53.000000 aim-4.0.0.dev2/aim/cli/convert/processors/mlflow.py
+-rw-r--r--   0 github     (503) staff       (20)    10372 2022-08-06 00:13:01.000000 aim-4.0.0.dev2/aim/cli/convert/processors/tensorboard.py
+-rw-r--r--   0 github     (503) staff       (20)     6816 2023-01-04 20:08:59.000000 aim-4.0.0.dev2/aim/cli/convert/processors/wandb.py
+drwxr-xr-x   0 github     (503) staff       (20)        0 2023-04-05 11:38:00.690306 aim-4.0.0.dev2/aim/cli/init/
+-rw-r--r--   0 github     (503) staff       (20)        0 2022-04-19 22:29:06.000000 aim-4.0.0.dev2/aim/cli/init/__init__.py
+-rw-r--r--   0 github     (503) staff       (20)     1592 2023-03-24 14:18:45.000000 aim-4.0.0.dev2/aim/cli/init/commands.py
+drwxr-xr-x   0 github     (503) staff       (20)        0 2023-04-05 11:38:00.690650 aim-4.0.0.dev2/aim/cli/manager/
+-rw-r--r--   0 github     (503) staff       (20)        0 2022-04-19 22:29:06.000000 aim-4.0.0.dev2/aim/cli/manager/__init__.py
+-rw-r--r--   0 github     (503) staff       (20)     3382 2022-08-11 13:58:02.000000 aim-4.0.0.dev2/aim/cli/manager/manager.py
+drwxr-xr-x   0 github     (503) staff       (20)        0 2023-04-05 11:38:00.690996 aim-4.0.0.dev2/aim/cli/reindex/
+-rw-r--r--   0 github     (503) staff       (20)        0 2022-04-19 22:29:06.000000 aim-4.0.0.dev2/aim/cli/reindex/__init__.py
+-rw-r--r--   0 github     (503) staff       (20)      736 2022-11-25 20:09:54.000000 aim-4.0.0.dev2/aim/cli/reindex/commands.py
+drwxr-xr-x   0 github     (503) staff       (20)        0 2023-04-05 11:38:00.691599 aim-4.0.0.dev2/aim/cli/runs/
+-rw-r--r--   0 github     (503) staff       (20)        0 2022-04-19 22:29:06.000000 aim-4.0.0.dev2/aim/cli/runs/__init__.py
+-rw-r--r--   0 github     (503) staff       (20)     6621 2023-03-24 14:18:45.000000 aim-4.0.0.dev2/aim/cli/runs/commands.py
+-rw-r--r--   0 github     (503) staff       (20)     2570 2022-11-25 20:09:54.000000 aim-4.0.0.dev2/aim/cli/runs/utils.py
+drwxr-xr-x   0 github     (503) staff       (20)        0 2023-04-05 11:38:00.691937 aim-4.0.0.dev2/aim/cli/server/
+-rw-r--r--   0 github     (503) staff       (20)        0 2022-04-19 22:29:06.000000 aim-4.0.0.dev2/aim/cli/server/__init__.py
+-rw-r--r--   0 github     (503) staff       (20)     3709 2023-03-24 14:18:45.000000 aim-4.0.0.dev2/aim/cli/server/commands.py
+drwxr-xr-x   0 github     (503) staff       (20)        0 2023-04-05 11:38:00.692267 aim-4.0.0.dev2/aim/cli/storage/
+-rw-r--r--   0 github     (503) staff       (20)        0 2022-06-17 00:13:19.000000 aim-4.0.0.dev2/aim/cli/storage/__init__.py
+-rw-r--r--   0 github     (503) staff       (20)     7537 2023-03-24 14:18:45.000000 aim-4.0.0.dev2/aim/cli/storage/commands.py
+drwxr-xr-x   0 github     (503) staff       (20)        0 2023-04-05 11:38:00.692627 aim-4.0.0.dev2/aim/cli/telemetry/
+-rw-r--r--   0 github     (503) staff       (20)        0 2023-01-24 20:09:40.000000 aim-4.0.0.dev2/aim/cli/telemetry/__init__.py
+-rw-r--r--   0 github     (503) staff       (20)      305 2023-01-24 20:09:40.000000 aim-4.0.0.dev2/aim/cli/telemetry/commands.py
+drwxr-xr-x   0 github     (503) staff       (20)        0 2023-04-05 11:38:00.693280 aim-4.0.0.dev2/aim/cli/up/
+-rw-r--r--   0 github     (503) staff       (20)        0 2022-04-19 22:29:06.000000 aim-4.0.0.dev2/aim/cli/up/__init__.py
+-rw-r--r--   0 github     (503) staff       (20)     5953 2023-01-24 20:09:40.000000 aim-4.0.0.dev2/aim/cli/up/commands.py
+-rw-r--r--   0 github     (503) staff       (20)     1446 2022-06-21 18:01:08.000000 aim-4.0.0.dev2/aim/cli/up/utils.py
+drwxr-xr-x   0 github     (503) staff       (20)        0 2023-04-05 11:38:00.693760 aim-4.0.0.dev2/aim/cli/upgrade/
+-rw-r--r--   0 github     (503) staff       (20)        0 2022-04-19 22:29:06.000000 aim-4.0.0.dev2/aim/cli/upgrade/__init__.py
+drwxr-xr-x   0 github     (503) staff       (20)        0 2023-04-05 11:38:00.694514 aim-4.0.0.dev2/aim/cli/upgrade/_legacy_repo/
+-rw-r--r--   0 github     (503) staff       (20)      258 2022-04-19 22:29:06.000000 aim-4.0.0.dev2/aim/cli/upgrade/_legacy_repo/__init__.py
+-rw-r--r--   0 github     (503) staff       (20)      734 2022-04-19 22:29:06.000000 aim-4.0.0.dev2/aim/cli/upgrade/_legacy_repo/configs.py
+-rw-r--r--   0 github     (503) staff       (20)      448 2022-04-19 22:29:06.000000 aim-4.0.0.dev2/aim/cli/upgrade/_legacy_repo/metric_artifact.py
+drwxr-xr-x   0 github     (503) staff       (20)        0 2023-04-05 11:38:00.695140 aim-4.0.0.dev2/aim/cli/upgrade/_legacy_repo/proto/
+-rw-r--r--   0 github     (503) staff       (20)        0 2022-04-19 22:29:06.000000 aim-4.0.0.dev2/aim/cli/upgrade/_legacy_repo/proto/__init__.py
+-rw-r--r--   0 github     (503) staff       (20)      263 2023-01-13 20:10:23.000000 aim-4.0.0.dev2/aim/cli/upgrade/_legacy_repo/proto/base_pb2.py
+-rw-r--r--   0 github     (503) staff       (20)      267 2023-01-13 20:10:23.000000 aim-4.0.0.dev2/aim/cli/upgrade/_legacy_repo/proto/metric_pb2.py
+drwxr-xr-x   0 github     (503) staff       (20)        0 2023-04-05 11:38:00.695638 aim-4.0.0.dev2/aim/cli/upgrade/_legacy_repo/proto/v3/
+-rw-r--r--   0 github     (503) staff       (20)        0 2023-01-13 20:10:23.000000 aim-4.0.0.dev2/aim/cli/upgrade/_legacy_repo/proto/v3/__init__.py
+-rw-r--r--   0 github     (503) staff       (20)     3396 2023-01-13 20:10:23.000000 aim-4.0.0.dev2/aim/cli/upgrade/_legacy_repo/proto/v3/base_pb2.py
+-rw-r--r--   0 github     (503) staff       (20)     1919 2023-01-13 20:10:23.000000 aim-4.0.0.dev2/aim/cli/upgrade/_legacy_repo/proto/v3/metric_pb2.py
+drwxr-xr-x   0 github     (503) staff       (20)        0 2023-04-05 11:38:00.696100 aim-4.0.0.dev2/aim/cli/upgrade/_legacy_repo/proto/v4/
+-rw-r--r--   0 github     (503) staff       (20)        0 2023-01-13 20:10:23.000000 aim-4.0.0.dev2/aim/cli/upgrade/_legacy_repo/proto/v4/__init__.py
+-rw-r--r--   0 github     (503) staff       (20)     1111 2023-01-13 20:10:23.000000 aim-4.0.0.dev2/aim/cli/upgrade/_legacy_repo/proto/v4/base_pb2.py
+-rw-r--r--   0 github     (503) staff       (20)      969 2023-01-13 20:10:23.000000 aim-4.0.0.dev2/aim/cli/upgrade/_legacy_repo/proto/v4/metric_pb2.py
+drwxr-xr-x   0 github     (503) staff       (20)        0 2023-04-05 11:38:00.697270 aim-4.0.0.dev2/aim/cli/upgrade/_legacy_repo/repo/
+-rw-r--r--   0 github     (503) staff       (20)        1 2022-04-19 22:29:06.000000 aim-4.0.0.dev2/aim/cli/upgrade/_legacy_repo/repo/__init__.py
+-rw-r--r--   0 github     (503) staff       (20)     1722 2022-04-19 22:29:06.000000 aim-4.0.0.dev2/aim/cli/upgrade/_legacy_repo/repo/metric.py
+-rw-r--r--   0 github     (503) staff       (20)     3722 2022-04-19 22:29:06.000000 aim-4.0.0.dev2/aim/cli/upgrade/_legacy_repo/repo/repo.py
+-rw-r--r--   0 github     (503) staff       (20)     4062 2022-04-19 22:29:06.000000 aim-4.0.0.dev2/aim/cli/upgrade/_legacy_repo/repo/run.py
+-rw-r--r--   0 github     (503) staff       (20)     1357 2022-04-19 22:29:06.000000 aim-4.0.0.dev2/aim/cli/upgrade/_legacy_repo/repo/trace.py
+-rw-r--r--   0 github     (503) staff       (20)     1211 2022-04-19 22:29:06.000000 aim-4.0.0.dev2/aim/cli/upgrade/_legacy_repo/repo/utils.py
+-rw-r--r--   0 github     (503) staff       (20)     6635 2022-04-19 22:29:06.000000 aim-4.0.0.dev2/aim/cli/upgrade/utils.py
+-rw-r--r--   0 github     (503) staff       (20)      370 2022-04-19 22:29:06.000000 aim-4.0.0.dev2/aim/cli/utils.py
+drwxr-xr-x   0 github     (503) staff       (20)        0 2023-04-05 11:38:00.697533 aim-4.0.0.dev2/aim/cli/version/
+-rw-r--r--   0 github     (503) staff       (20)        0 2022-04-19 22:29:06.000000 aim-4.0.0.dev2/aim/cli/version/__init__.py
+-rw-r--r--   0 github     (503) staff       (20)      149 2022-04-19 22:29:06.000000 aim-4.0.0.dev2/aim/cli/version/commands.py
+-rw-r--r--   0 github     (503) staff       (20)     9960 2023-01-24 20:09:40.000000 aim-4.0.0.dev2/aim/cli/watcher_cli.py
+drwxr-xr-x   0 github     (503) staff       (20)        0 2023-04-05 11:38:00.698059 aim-4.0.0.dev2/aim/ext/
+-rw-r--r--   0 github     (503) staff       (20)        0 2022-04-19 22:29:06.000000 aim-4.0.0.dev2/aim/ext/__init__.py
+drwxr-xr-x   0 github     (503) staff       (20)        0 2023-04-05 11:38:00.698307 aim-4.0.0.dev2/aim/ext/cleanup/
+-rw-r--r--   0 github     (503) staff       (20)     3579 2022-11-12 00:14:35.000000 aim-4.0.0.dev2/aim/ext/cleanup/__init__.py
+-rw-r--r--   0 github     (503) staff       (20)     2021 2023-03-02 20:49:40.000000 aim-4.0.0.dev2/aim/ext/exception_resistant.py
+drwxr-xr-x   0 github     (503) staff       (20)        0 2023-04-05 11:38:00.698647 aim-4.0.0.dev2/aim/ext/notebook/
+-rw-r--r--   0 github     (503) staff       (20)        0 2022-04-19 22:29:06.000000 aim-4.0.0.dev2/aim/ext/notebook/__init__.py
+-rw-r--r--   0 github     (503) staff       (20)     7314 2022-04-19 22:29:06.000000 aim-4.0.0.dev2/aim/ext/notebook/notebook.py
+drwxr-xr-x   0 github     (503) staff       (20)        0 2023-04-05 11:38:00.700767 aim-4.0.0.dev2/aim/ext/notifier/
+-rw-r--r--   0 github     (503) staff       (20)      589 2022-08-20 12:34:00.000000 aim-4.0.0.dev2/aim/ext/notifier/__init__.py
+-rw-r--r--   0 github     (503) staff       (20)      305 2022-08-20 12:34:00.000000 aim-4.0.0.dev2/aim/ext/notifier/base_notifier.py
+-rw-r--r--   0 github     (503) staff       (20)     1858 2022-11-25 20:09:54.000000 aim-4.0.0.dev2/aim/ext/notifier/config.py
+-rw-r--r--   0 github     (503) staff       (20)      361 2022-08-20 12:34:00.000000 aim-4.0.0.dev2/aim/ext/notifier/config_default.json
+-rw-r--r--   0 github     (503) staff       (20)       70 2022-08-20 12:34:00.000000 aim-4.0.0.dev2/aim/ext/notifier/config_empty.json
+-rw-r--r--   0 github     (503) staff       (20)      522 2022-08-20 12:34:00.000000 aim-4.0.0.dev2/aim/ext/notifier/logging_notifier.py
+-rw-r--r--   0 github     (503) staff       (20)     1428 2022-08-20 12:34:00.000000 aim-4.0.0.dev2/aim/ext/notifier/notifier.py
+-rw-r--r--   0 github     (503) staff       (20)     1158 2022-08-20 12:34:00.000000 aim-4.0.0.dev2/aim/ext/notifier/notifier_builder.py
+-rw-r--r--   0 github     (503) staff       (20)      524 2022-08-20 12:34:00.000000 aim-4.0.0.dev2/aim/ext/notifier/slack_notifier.py
+-rw-r--r--   0 github     (503) staff       (20)     1034 2022-08-20 12:34:00.000000 aim-4.0.0.dev2/aim/ext/notifier/utils.py
+-rw-r--r--   0 github     (503) staff       (20)      862 2022-08-20 12:34:00.000000 aim-4.0.0.dev2/aim/ext/notifier/workplace_notifier.py
+drwxr-xr-x   0 github     (503) staff       (20)        0 2023-04-05 11:38:00.702138 aim-4.0.0.dev2/aim/ext/resource/
+-rw-r--r--   0 github     (503) staff       (20)       92 2022-04-19 22:29:06.000000 aim-4.0.0.dev2/aim/ext/resource/__init__.py
+-rw-r--r--   0 github     (503) staff       (20)      100 2022-04-19 22:29:06.000000 aim-4.0.0.dev2/aim/ext/resource/configs.py
+-rw-r--r--   0 github     (503) staff       (20)      726 2022-05-16 21:25:24.000000 aim-4.0.0.dev2/aim/ext/resource/log.py
+-rw-r--r--   0 github     (503) staff       (20)     6700 2023-01-04 20:08:59.000000 aim-4.0.0.dev2/aim/ext/resource/stat.py
+-rw-r--r--   0 github     (503) staff       (20)     7511 2023-01-04 20:08:59.000000 aim-4.0.0.dev2/aim/ext/resource/tracker.py
+-rw-r--r--   0 github     (503) staff       (20)       56 2022-04-19 22:29:06.000000 aim-4.0.0.dev2/aim/ext/resource/utils.py
+drwxr-xr-x   0 github     (503) staff       (20)        0 2023-04-05 11:38:00.702417 aim-4.0.0.dev2/aim/ext/sshfs/
+-rw-r--r--   0 github     (503) staff       (20)        0 2022-04-19 22:29:06.000000 aim-4.0.0.dev2/aim/ext/sshfs/__init__.py
+-rw-r--r--   0 github     (503) staff       (20)     7768 2022-04-19 22:29:06.000000 aim-4.0.0.dev2/aim/ext/sshfs/utils.py
+drwxr-xr-x   0 github     (503) staff       (20)        0 2023-04-05 11:38:00.702686 aim-4.0.0.dev2/aim/ext/task_queue/
+-rw-r--r--   0 github     (503) staff       (20)        0 2022-04-19 22:29:06.000000 aim-4.0.0.dev2/aim/ext/task_queue/__init__.py
+-rw-r--r--   0 github     (503) staff       (20)     2069 2022-04-19 22:29:06.000000 aim-4.0.0.dev2/aim/ext/task_queue/queue.py
+drwxr-xr-x   0 github     (503) staff       (20)        0 2023-04-05 11:38:00.703264 aim-4.0.0.dev2/aim/ext/tensorboard_tracker/
+-rw-r--r--   0 github     (503) staff       (20)       48 2023-01-04 20:08:59.000000 aim-4.0.0.dev2/aim/ext/tensorboard_tracker/__init__.py
+-rw-r--r--   0 github     (503) staff       (20)      919 2023-01-04 20:08:59.000000 aim-4.0.0.dev2/aim/ext/tensorboard_tracker/run.py
+-rw-r--r--   0 github     (503) staff       (20)     7201 2023-01-04 20:08:59.000000 aim-4.0.0.dev2/aim/ext/tensorboard_tracker/tracker.py
+drwxr-xr-x   0 github     (503) staff       (20)        0 2023-04-05 11:38:00.706428 aim-4.0.0.dev2/aim/ext/transport/
+-rw-r--r--   0 github     (503) staff       (20)        0 2022-04-19 22:29:06.000000 aim-4.0.0.dev2/aim/ext/transport/__init__.py
+-rw-r--r--   0 github     (503) staff       (20)    12932 2023-02-27 08:16:06.000000 aim-4.0.0.dev2/aim/ext/transport/client.py
+-rw-r--r--   0 github     (503) staff       (20)      515 2022-04-19 22:29:06.000000 aim-4.0.0.dev2/aim/ext/transport/config.py
+-rw-r--r--   0 github     (503) staff       (20)     3298 2023-01-23 20:08:00.000000 aim-4.0.0.dev2/aim/ext/transport/handlers.py
+-rw-r--r--   0 github     (503) staff       (20)     5555 2023-01-13 20:10:23.000000 aim-4.0.0.dev2/aim/ext/transport/health.py
+-rw-r--r--   0 github     (503) staff       (20)     5616 2023-01-13 20:10:23.000000 aim-4.0.0.dev2/aim/ext/transport/heartbeat.py
+-rw-r--r--   0 github     (503) staff       (20)     3347 2023-01-13 20:10:23.000000 aim-4.0.0.dev2/aim/ext/transport/message_utils.py
+drwxr-xr-x   0 github     (503) staff       (20)        0 2023-04-05 11:38:00.707755 aim-4.0.0.dev2/aim/ext/transport/proto/
+-rw-r--r--   0 github     (503) staff       (20)        0 2023-01-13 20:10:23.000000 aim-4.0.0.dev2/aim/ext/transport/proto/__init__.py
+-rw-r--r--   0 github     (503) staff       (20)      245 2023-01-13 20:10:23.000000 aim-4.0.0.dev2/aim/ext/transport/proto/health_pb2.py
+-rw-r--r--   0 github     (503) staff       (20)     3991 2023-01-13 20:10:23.000000 aim-4.0.0.dev2/aim/ext/transport/proto/health_pb2_grpc.py
+-rw-r--r--   0 github     (503) staff       (20)      259 2023-01-13 20:10:23.000000 aim-4.0.0.dev2/aim/ext/transport/proto/remote_router_pb2.py
+-rw-r--r--   0 github     (503) staff       (20)     8855 2023-01-13 20:10:23.000000 aim-4.0.0.dev2/aim/ext/transport/proto/remote_router_pb2_grpc.py
+-rw-r--r--   0 github     (503) staff       (20)      263 2023-01-13 20:10:23.000000 aim-4.0.0.dev2/aim/ext/transport/proto/remote_tracking_pb2.py
+-rw-r--r--   0 github     (503) staff       (20)     9444 2023-01-13 20:10:23.000000 aim-4.0.0.dev2/aim/ext/transport/proto/remote_tracking_pb2_grpc.py
+drwxr-xr-x   0 github     (503) staff       (20)        0 2023-04-05 11:38:00.708651 aim-4.0.0.dev2/aim/ext/transport/proto/v3/
+-rw-r--r--   0 github     (503) staff       (20)        0 2023-01-13 20:10:23.000000 aim-4.0.0.dev2/aim/ext/transport/proto/v3/__init__.py
+-rw-r--r--   0 github     (503) staff       (20)     6195 2023-01-13 20:10:23.000000 aim-4.0.0.dev2/aim/ext/transport/proto/v3/health_pb2.py
+-rw-r--r--   0 github     (503) staff       (20)    25245 2023-01-13 20:10:23.000000 aim-4.0.0.dev2/aim/ext/transport/proto/v3/remote_router_pb2.py
+-rw-r--r--   0 github     (503) staff       (20)    37567 2023-01-13 20:10:23.000000 aim-4.0.0.dev2/aim/ext/transport/proto/v3/remote_tracking_pb2.py
+drwxr-xr-x   0 github     (503) staff       (20)        0 2023-04-05 11:38:00.709454 aim-4.0.0.dev2/aim/ext/transport/proto/v4/
+-rw-r--r--   0 github     (503) staff       (20)        0 2023-01-13 20:10:23.000000 aim-4.0.0.dev2/aim/ext/transport/proto/v4/__init__.py
+-rw-r--r--   0 github     (503) staff       (20)     1749 2023-01-13 20:10:23.000000 aim-4.0.0.dev2/aim/ext/transport/proto/v4/health_pb2.py
+-rw-r--r--   0 github     (503) staff       (20)     4280 2023-01-13 20:10:23.000000 aim-4.0.0.dev2/aim/ext/transport/proto/v4/remote_router_pb2.py
+-rw-r--r--   0 github     (503) staff       (20)     5662 2023-01-13 20:10:23.000000 aim-4.0.0.dev2/aim/ext/transport/proto/v4/remote_tracking_pb2.py
+-rw-r--r--   0 github     (503) staff       (20)      428 2022-04-19 22:29:06.000000 aim-4.0.0.dev2/aim/ext/transport/remote_resource.py
+-rw-r--r--   0 github     (503) staff       (20)     8078 2023-01-23 10:30:27.000000 aim-4.0.0.dev2/aim/ext/transport/remote_tracking.py
+-rw-r--r--   0 github     (503) staff       (20)     3637 2023-01-13 20:10:23.000000 aim-4.0.0.dev2/aim/ext/transport/router.py
+-rw-r--r--   0 github     (503) staff       (20)     3728 2022-11-18 00:13:03.000000 aim-4.0.0.dev2/aim/ext/transport/rpc_queue.py
+-rw-r--r--   0 github     (503) staff       (20)     4609 2023-01-23 10:30:27.000000 aim-4.0.0.dev2/aim/ext/transport/server.py
+-rw-r--r--   0 github     (503) staff       (20)     3419 2023-01-13 20:10:23.000000 aim-4.0.0.dev2/aim/ext/transport/worker.py
+-rw-r--r--   0 github     (503) staff       (20)     2103 2022-08-20 12:34:00.000000 aim-4.0.0.dev2/aim/ext/utils.py
+-rw-r--r--   0 github     (503) staff       (20)       92 2022-09-25 12:02:15.000000 aim-4.0.0.dev2/aim/fastai.py
+-rw-r--r--   0 github     (503) staff       (20)      127 2023-01-13 20:10:23.000000 aim-4.0.0.dev2/aim/hf_dataset.py
+-rw-r--r--   0 github     (503) staff       (20)      105 2022-04-19 22:29:06.000000 aim-4.0.0.dev2/aim/hugging_face.py
+-rw-r--r--   0 github     (503) staff       (20)      103 2022-04-19 22:29:06.000000 aim-4.0.0.dev2/aim/keras.py
+-rw-r--r--   0 github     (503) staff       (20)      103 2022-08-20 12:34:00.000000 aim-4.0.0.dev2/aim/keras_tuner.py
+-rw-r--r--   0 github     (503) staff       (20)       98 2022-05-06 13:59:46.000000 aim-4.0.0.dev2/aim/lightgbm.py
+-rw-r--r--   0 github     (503) staff       (20)       97 2022-10-04 00:16:28.000000 aim-4.0.0.dev2/aim/mxnet.py
+-rw-r--r--   0 github     (503) staff       (20)       98 2022-11-12 00:14:35.000000 aim-4.0.0.dev2/aim/optuna.py
+-rw-r--r--   0 github     (503) staff       (20)       99 2022-11-12 00:14:35.000000 aim-4.0.0.dev2/aim/paddle.py
+-rw-r--r--   0 github     (503) staff       (20)       93 2023-01-31 20:08:25.000000 aim-4.0.0.dev2/aim/prophet.py
+-rw-r--r--   0 github     (503) staff       (20)      115 2022-04-19 22:29:06.000000 aim-4.0.0.dev2/aim/pytorch.py
+-rw-r--r--   0 github     (503) staff       (20)      107 2022-04-19 22:29:06.000000 aim-4.0.0.dev2/aim/pytorch_ignite.py
+-rw-r--r--   0 github     (503) staff       (20)      113 2022-04-19 22:29:06.000000 aim-4.0.0.dev2/aim/pytorch_lightning.py
+-rw-r--r--   0 github     (503) staff       (20)       87 2023-01-13 20:10:23.000000 aim-4.0.0.dev2/aim/sb3.py
+drwxr-xr-x   0 github     (503) staff       (20)        0 2023-04-05 11:38:00.717622 aim-4.0.0.dev2/aim/sdk/
+-rw-r--r--   0 github     (503) staff       (20)      915 2022-11-25 20:09:54.000000 aim-4.0.0.dev2/aim/sdk/__init__.py
+drwxr-xr-x   0 github     (503) staff       (20)        0 2023-04-05 11:38:00.721398 aim-4.0.0.dev2/aim/sdk/adapters/
+-rw-r--r--   0 github     (503) staff       (20)        0 2022-04-19 22:29:06.000000 aim-4.0.0.dev2/aim/sdk/adapters/__init__.py
+-rw-r--r--   0 github     (503) staff       (20)     2609 2023-03-02 20:49:40.000000 aim-4.0.0.dev2/aim/sdk/adapters/acme.py
+-rw-r--r--   0 github     (503) staff       (20)     3371 2023-03-02 20:49:40.000000 aim-4.0.0.dev2/aim/sdk/adapters/catboost.py
+-rw-r--r--   0 github     (503) staff       (20)     5510 2023-03-02 20:49:40.000000 aim-4.0.0.dev2/aim/sdk/adapters/fastai.py
+-rw-r--r--   0 github     (503) staff       (20)     5664 2023-03-24 14:18:45.000000 aim-4.0.0.dev2/aim/sdk/adapters/hugging_face.py
+-rw-r--r--   0 github     (503) staff       (20)     2579 2023-03-02 20:49:40.000000 aim-4.0.0.dev2/aim/sdk/adapters/keras.py
+-rw-r--r--   0 github     (503) staff       (20)     1128 2022-04-19 22:29:06.000000 aim-4.0.0.dev2/aim/sdk/adapters/keras_mixins.py
+-rw-r--r--   0 github     (503) staff       (20)     2805 2023-03-02 20:49:40.000000 aim-4.0.0.dev2/aim/sdk/adapters/keras_tuner.py
+-rw-r--r--   0 github     (503) staff       (20)     3266 2023-03-02 20:49:40.000000 aim-4.0.0.dev2/aim/sdk/adapters/lightgbm.py
+-rw-r--r--   0 github     (503) staff       (20)     8261 2023-03-02 20:49:40.000000 aim-4.0.0.dev2/aim/sdk/adapters/mxnet.py
+-rw-r--r--   0 github     (503) staff       (20)     7159 2023-03-02 20:49:40.000000 aim-4.0.0.dev2/aim/sdk/adapters/optuna.py
+-rw-r--r--   0 github     (503) staff       (20)     3495 2023-03-02 20:49:40.000000 aim-4.0.0.dev2/aim/sdk/adapters/paddle.py
+-rw-r--r--   0 github     (503) staff       (20)     2911 2023-03-02 20:49:40.000000 aim-4.0.0.dev2/aim/sdk/adapters/prophet.py
+-rw-r--r--   0 github     (503) staff       (20)     2458 2022-07-09 00:13:12.000000 aim-4.0.0.dev2/aim/sdk/adapters/pytorch.py
+-rw-r--r--   0 github     (503) staff       (20)     9025 2023-03-02 20:49:40.000000 aim-4.0.0.dev2/aim/sdk/adapters/pytorch_ignite.py
+-rw-r--r--   0 github     (503) staff       (20)     5837 2023-03-24 14:18:45.000000 aim-4.0.0.dev2/aim/sdk/adapters/pytorch_lightning.py
+-rw-r--r--   0 github     (503) staff       (20)     4533 2023-03-02 20:49:40.000000 aim-4.0.0.dev2/aim/sdk/adapters/sb3.py
+-rw-r--r--   0 github     (503) staff       (20)     2600 2023-03-02 20:49:40.000000 aim-4.0.0.dev2/aim/sdk/adapters/tensorflow.py
+-rw-r--r--   0 github     (503) staff       (20)     2934 2023-03-02 20:49:40.000000 aim-4.0.0.dev2/aim/sdk/adapters/xgboost.py
+-rw-r--r--   0 github     (503) staff       (20)     5138 2023-03-16 00:07:12.000000 aim-4.0.0.dev2/aim/sdk/base_run.py
+drwxr-xr-x   0 github     (503) staff       (20)        0 2023-04-05 11:38:00.722208 aim-4.0.0.dev2/aim/sdk/callbacks/
+-rw-r--r--   0 github     (503) staff       (20)      196 2022-11-25 20:09:54.000000 aim-4.0.0.dev2/aim/sdk/callbacks/__init__.py
+-rw-r--r--   0 github     (503) staff       (20)     1493 2022-11-25 20:09:54.000000 aim-4.0.0.dev2/aim/sdk/callbacks/caller.py
+-rw-r--r--   0 github     (503) staff       (20)      495 2022-11-25 20:09:54.000000 aim-4.0.0.dev2/aim/sdk/callbacks/events.py
+-rw-r--r--   0 github     (503) staff       (20)     1416 2022-11-25 20:09:54.000000 aim-4.0.0.dev2/aim/sdk/callbacks/helpers.py
+-rw-r--r--   0 github     (503) staff       (20)      253 2022-09-26 00:13:35.000000 aim-4.0.0.dev2/aim/sdk/configs.py
+-rw-r--r--   0 github     (503) staff       (20)       22 2022-11-24 20:09:30.000000 aim-4.0.0.dev2/aim/sdk/data_version.py
+-rw-r--r--   0 github     (503) staff       (20)      145 2022-11-25 20:09:54.000000 aim-4.0.0.dev2/aim/sdk/errors.py
+-rw-r--r--   0 github     (503) staff       (20)     4990 2023-01-23 20:08:00.000000 aim-4.0.0.dev2/aim/sdk/index_manager.py
+drwxr-xr-x   0 github     (503) staff       (20)        0 2023-04-05 11:38:00.723248 aim-4.0.0.dev2/aim/sdk/legacy/
+-rw-r--r--   0 github     (503) staff       (20)        0 2022-04-19 22:29:06.000000 aim-4.0.0.dev2/aim/sdk/legacy/__init__.py
+-rw-r--r--   0 github     (503) staff       (20)      288 2022-04-19 22:29:06.000000 aim-4.0.0.dev2/aim/sdk/legacy/deprecation_warning.py
+-rw-r--r--   0 github     (503) staff       (20)       94 2022-04-19 22:29:06.000000 aim-4.0.0.dev2/aim/sdk/legacy/flush.py
+-rw-r--r--   0 github     (503) staff       (20)      185 2022-04-19 22:29:06.000000 aim-4.0.0.dev2/aim/sdk/legacy/init.py
+-rw-r--r--   0 github     (503) staff       (20)      702 2022-04-19 22:29:06.000000 aim-4.0.0.dev2/aim/sdk/legacy/select.py
+drwxr-xr-x   0 github     (503) staff       (20)        0 2023-04-05 11:38:00.723718 aim-4.0.0.dev2/aim/sdk/legacy/session/
+-rw-r--r--   0 github     (503) staff       (20)       67 2022-04-19 22:29:06.000000 aim-4.0.0.dev2/aim/sdk/legacy/session/__init__.py
+-rw-r--r--   0 github     (503) staff       (20)       30 2022-04-19 22:29:06.000000 aim-4.0.0.dev2/aim/sdk/legacy/session/configs.py
+-rw-r--r--   0 github     (503) staff       (20)     4277 2022-04-19 22:29:06.000000 aim-4.0.0.dev2/aim/sdk/legacy/session/session.py
+-rw-r--r--   0 github     (503) staff       (20)      410 2022-04-19 22:29:06.000000 aim-4.0.0.dev2/aim/sdk/legacy/track.py
+-rw-r--r--   0 github     (503) staff       (20)     6513 2023-02-01 20:08:30.000000 aim-4.0.0.dev2/aim/sdk/lock_manager.py
+drwxr-xr-x   0 github     (503) staff       (20)        0 2023-04-05 11:38:00.724038 aim-4.0.0.dev2/aim/sdk/logging/
+-rw-r--r--   0 github     (503) staff       (20)       61 2022-11-25 20:09:54.000000 aim-4.0.0.dev2/aim/sdk/logging/__init__.py
+-rw-r--r--   0 github     (503) staff       (20)     1863 2023-02-03 15:21:38.000000 aim-4.0.0.dev2/aim/sdk/logging/log_record.py
+-rw-r--r--   0 github     (503) staff       (20)      954 2022-11-25 20:09:54.000000 aim-4.0.0.dev2/aim/sdk/maintenance_run.py
+-rw-r--r--   0 github     (503) staff       (20)     3397 2023-03-16 00:07:12.000000 aim-4.0.0.dev2/aim/sdk/num_utils.py
+drwxr-xr-x   0 github     (503) staff       (20)        0 2023-04-05 11:38:00.725205 aim-4.0.0.dev2/aim/sdk/objects/
+-rw-r--r--   0 github     (503) staff       (20)      214 2022-04-19 22:29:06.000000 aim-4.0.0.dev2/aim/sdk/objects/__init__.py
+-rw-r--r--   0 github     (503) staff       (20)     3264 2022-11-11 08:24:45.000000 aim-4.0.0.dev2/aim/sdk/objects/audio.py
+-rw-r--r--   0 github     (503) staff       (20)     4232 2023-01-04 20:08:59.000000 aim-4.0.0.dev2/aim/sdk/objects/distribution.py
+-rw-r--r--   0 github     (503) staff       (20)     2885 2023-01-04 20:08:59.000000 aim-4.0.0.dev2/aim/sdk/objects/figure.py
+-rw-r--r--   0 github     (503) staff       (20)     9914 2023-03-03 20:09:01.000000 aim-4.0.0.dev2/aim/sdk/objects/image.py
+drwxr-xr-x   0 github     (503) staff       (20)        0 2023-04-05 11:38:00.725559 aim-4.0.0.dev2/aim/sdk/objects/io/
+-rw-r--r--   0 github     (503) staff       (20)        0 2022-04-19 22:29:06.000000 aim-4.0.0.dev2/aim/sdk/objects/io/__init__.py
+-rw-r--r--   0 github     (503) staff       (20)    21094 2022-04-19 22:29:06.000000 aim-4.0.0.dev2/aim/sdk/objects/io/wavfile.py
+drwxr-xr-x   0 github     (503) staff       (20)        0 2023-04-05 11:38:00.726710 aim-4.0.0.dev2/aim/sdk/objects/plugins/
+-rw-r--r--   0 github     (503) staff       (20)        0 2022-04-19 22:29:06.000000 aim-4.0.0.dev2/aim/sdk/objects/plugins/__init__.py
+-rw-r--r--   0 github     (503) staff       (20)     1983 2023-01-23 20:08:00.000000 aim-4.0.0.dev2/aim/sdk/objects/plugins/dvc_metadata.py
+-rw-r--r--   0 github     (503) staff       (20)     3648 2023-02-02 20:09:54.000000 aim-4.0.0.dev2/aim/sdk/objects/plugins/hf_datasets_metadata.py
+-rw-r--r--   0 github     (503) staff       (20)     1272 2022-04-19 22:29:06.000000 aim-4.0.0.dev2/aim/sdk/objects/plugins/hub_dataset.py
+-rw-r--r--   0 github     (503) staff       (20)      694 2022-04-19 22:29:06.000000 aim-4.0.0.dev2/aim/sdk/objects/text.py
+-rw-r--r--   0 github     (503) staff       (20)     6048 2022-09-01 19:23:53.000000 aim-4.0.0.dev2/aim/sdk/query_utils.py
+-rw-r--r--   0 github     (503) staff       (20)     1050 2023-01-23 10:30:27.000000 aim-4.0.0.dev2/aim/sdk/remote_repo_proxy.py
+-rw-r--r--   0 github     (503) staff       (20)     2171 2023-01-23 10:30:27.000000 aim-4.0.0.dev2/aim/sdk/remote_run_reporter.py
+-rw-r--r--   0 github     (503) staff       (20)    34519 2023-03-03 20:09:01.000000 aim-4.0.0.dev2/aim/sdk/repo.py
+-rw-r--r--   0 github     (503) staff       (20)     1022 2023-03-16 00:07:12.000000 aim-4.0.0.dev2/aim/sdk/repo_utils.py
+drwxr-xr-x   0 github     (503) staff       (20)        0 2023-04-05 11:38:00.727347 aim-4.0.0.dev2/aim/sdk/reporter/
+-rw-r--r--   0 github     (503) staff       (20)    31012 2023-01-23 20:08:00.000000 aim-4.0.0.dev2/aim/sdk/reporter/__init__.py
+-rw-r--r--   0 github     (503) staff       (20)     1832 2023-01-23 10:30:27.000000 aim-4.0.0.dev2/aim/sdk/reporter/file_manager.py
+-rw-r--r--   0 github     (503) staff       (20)    30774 2023-03-16 00:07:12.000000 aim-4.0.0.dev2/aim/sdk/run.py
+-rw-r--r--   0 github     (503) staff       (20)    13171 2023-02-03 15:21:38.000000 aim-4.0.0.dev2/aim/sdk/run_status_watcher.py
+-rw-r--r--   0 github     (503) staff       (20)    12970 2023-03-02 20:49:40.000000 aim-4.0.0.dev2/aim/sdk/sequence.py
+-rw-r--r--   0 github     (503) staff       (20)     9944 2022-07-21 10:42:47.000000 aim-4.0.0.dev2/aim/sdk/sequence_collection.py
+drwxr-xr-x   0 github     (503) staff       (20)        0 2023-04-05 11:38:00.729025 aim-4.0.0.dev2/aim/sdk/sequences/
+-rw-r--r--   0 github     (503) staff       (20)        0 2022-04-19 22:29:06.000000 aim-4.0.0.dev2/aim/sdk/sequences/__init__.py
+-rw-r--r--   0 github     (503) staff       (20)      458 2022-04-19 22:29:06.000000 aim-4.0.0.dev2/aim/sdk/sequences/audio_sequence.py
+-rw-r--r--   0 github     (503) staff       (20)      408 2023-03-02 20:49:40.000000 aim-4.0.0.dev2/aim/sdk/sequences/distribution_sequence.py
+-rw-r--r--   0 github     (503) staff       (20)      452 2023-03-02 20:49:40.000000 aim-4.0.0.dev2/aim/sdk/sequences/figure_sequence.py
+-rw-r--r--   0 github     (503) staff       (20)      482 2022-04-19 22:29:06.000000 aim-4.0.0.dev2/aim/sdk/sequences/image_sequence.py
+-rw-r--r--   0 github     (503) staff       (20)     3936 2022-07-09 00:13:12.000000 aim-4.0.0.dev2/aim/sdk/sequences/metric.py
+-rw-r--r--   0 github     (503) staff       (20)      458 2022-04-19 22:29:06.000000 aim-4.0.0.dev2/aim/sdk/sequences/text_sequence.py
+-rw-r--r--   0 github     (503) staff       (20)    10545 2022-09-25 12:02:15.000000 aim-4.0.0.dev2/aim/sdk/tracker.py
+-rw-r--r--   0 github     (503) staff       (20)     2202 2023-03-02 20:49:40.000000 aim-4.0.0.dev2/aim/sdk/training_flow.py
+-rw-r--r--   0 github     (503) staff       (20)      159 2022-06-18 00:13:24.000000 aim-4.0.0.dev2/aim/sdk/types.py
+-rw-r--r--   0 github     (503) staff       (20)     2940 2022-04-19 22:29:06.000000 aim-4.0.0.dev2/aim/sdk/uri_service.py
+-rw-r--r--   0 github     (503) staff       (20)     4046 2022-11-25 20:09:54.000000 aim-4.0.0.dev2/aim/sdk/utils.py
+drwxr-xr-x   0 github     (503) staff       (20)        0 2023-04-05 11:38:00.742572 aim-4.0.0.dev2/aim/storage/
+-rw-r--r--   0 github     (503) staff       (20)        0 2022-04-19 22:29:06.000000 aim-4.0.0.dev2/aim/storage/__init__.py
+-rw-r--r--   0 github     (503) staff       (20)   439810 2023-04-05 11:37:56.000000 aim-4.0.0.dev2/aim/storage/arrayview.cpp
+-rw-r--r--   0 github     (503) staff       (20)      278 2022-04-19 22:29:06.000000 aim-4.0.0.dev2/aim/storage/arrayview.pxd
+-rw-r--r--   0 github     (503) staff       (20)     2649 2022-06-15 14:05:59.000000 aim-4.0.0.dev2/aim/storage/arrayview.py
+-rw-r--r--   0 github     (503) staff       (20)   844368 2023-04-05 11:37:57.000000 aim-4.0.0.dev2/aim/storage/container.cpp
+-rw-r--r--   0 github     (503) staff       (20)      951 2022-04-19 22:29:06.000000 aim-4.0.0.dev2/aim/storage/container.pxd
+-rw-r--r--   0 github     (503) staff       (20)    10477 2022-04-19 22:29:06.000000 aim-4.0.0.dev2/aim/storage/container.py
+-rw-r--r--   0 github     (503) staff       (20)   912217 2023-04-05 11:37:58.000000 aim-4.0.0.dev2/aim/storage/containertreeview.cpp
+-rw-r--r--   0 github     (503) staff       (20)      313 2022-04-19 22:29:06.000000 aim-4.0.0.dev2/aim/storage/containertreeview.pxd
+-rw-r--r--   0 github     (503) staff       (20)     6026 2023-01-24 20:09:40.000000 aim-4.0.0.dev2/aim/storage/containertreeview.py
+-rw-r--r--   0 github     (503) staff       (20)     1212 2022-06-15 14:05:59.000000 aim-4.0.0.dev2/aim/storage/context.py
+drwxr-xr-x   0 github     (503) staff       (20)        0 2023-04-05 11:38:00.744415 aim-4.0.0.dev2/aim/storage/encoding/
+-rw-r--r--   0 github     (503) staff       (20)   148655 2023-04-05 11:37:58.000000 aim-4.0.0.dev2/aim/storage/encoding/__init__.cpp
+-rw-r--r--   0 github     (503) staff       (20)      155 2022-04-19 22:29:06.000000 aim-4.0.0.dev2/aim/storage/encoding/__init__.pxd
+-rw-r--r--   0 github     (503) staff       (20)       95 2022-04-19 22:29:06.000000 aim-4.0.0.dev2/aim/storage/encoding/__init__.py
+-rw-r--r--   0 github     (503) staff       (20)   378105 2023-04-05 11:37:58.000000 aim-4.0.0.dev2/aim/storage/encoding/encoding.cpp
+-rw-r--r--   0 github     (503) staff       (20)      507 2022-04-19 22:29:06.000000 aim-4.0.0.dev2/aim/storage/encoding/encoding.pxd
+-rw-r--r--   0 github     (503) staff       (20)     7373 2022-04-19 22:29:06.000000 aim-4.0.0.dev2/aim/storage/encoding/encoding.pyx
+-rw-r--r--   0 github     (503) staff       (20)   353597 2023-04-05 11:37:58.000000 aim-4.0.0.dev2/aim/storage/encoding/encoding_native.cpp
+-rw-r--r--   0 github     (503) staff       (20)      930 2022-04-19 22:29:06.000000 aim-4.0.0.dev2/aim/storage/encoding/encoding_native.pxd
+-rw-r--r--   0 github     (503) staff       (20)     5974 2022-04-19 22:29:06.000000 aim-4.0.0.dev2/aim/storage/encoding/encoding_native.pyx
+-rw-r--r--   0 github     (503) staff       (20)      337 2022-04-19 22:29:06.000000 aim-4.0.0.dev2/aim/storage/env.py
+drwxr-xr-x   0 github     (503) staff       (20)        0 2023-04-05 11:38:00.746354 aim-4.0.0.dev2/aim/storage/hashing/
+-rw-r--r--   0 github     (503) staff       (20)   141729 2023-04-05 11:37:58.000000 aim-4.0.0.dev2/aim/storage/hashing/__init__.cpp
+-rw-r--r--   0 github     (503) staff       (20)       85 2022-04-19 22:29:06.000000 aim-4.0.0.dev2/aim/storage/hashing/__init__.pxd
+-rw-r--r--   0 github     (503) staff       (20)       50 2022-04-19 22:29:06.000000 aim-4.0.0.dev2/aim/storage/hashing/__init__.py
+-rw-r--r--   0 github     (503) staff       (20)   205598 2023-04-05 11:37:58.000000 aim-4.0.0.dev2/aim/storage/hashing/c_hash.cpp
+-rw-r--r--   0 github     (503) staff       (20)      151 2022-04-19 22:29:06.000000 aim-4.0.0.dev2/aim/storage/hashing/c_hash.pxd
+-rw-r--r--   0 github     (503) staff       (20)     1077 2022-04-19 22:29:06.000000 aim-4.0.0.dev2/aim/storage/hashing/c_hash.pyx
+drwxr-xr-x   0 github     (503) staff       (20)        0 2023-04-05 11:38:00.746512 aim-4.0.0.dev2/aim/storage/hashing/hash/
+-rw-r--r--   0 github     (503) staff       (20)     1412 2022-04-19 22:29:06.000000 aim-4.0.0.dev2/aim/storage/hashing/hash/hash.h
+-rw-r--r--   0 github     (503) staff       (20)   392224 2023-04-05 11:37:58.000000 aim-4.0.0.dev2/aim/storage/hashing/hashing.cpp
+-rw-r--r--   0 github     (503) staff       (20)     1009 2022-04-19 22:29:06.000000 aim-4.0.0.dev2/aim/storage/hashing/hashing.pxd
+-rw-r--r--   0 github     (503) staff       (20)     5562 2023-01-24 20:09:40.000000 aim-4.0.0.dev2/aim/storage/hashing/hashing.py
+-rw-r--r--   0 github     (503) staff       (20)   672756 2023-04-05 11:37:58.000000 aim-4.0.0.dev2/aim/storage/inmemorytreeview.cpp
+-rw-r--r--   0 github     (503) staff       (20)      196 2022-04-19 22:29:06.000000 aim-4.0.0.dev2/aim/storage/inmemorytreeview.pxd
+-rw-r--r--   0 github     (503) staff       (20)     4341 2023-01-24 20:09:40.000000 aim-4.0.0.dev2/aim/storage/inmemorytreeview.py
+-rw-r--r--   0 github     (503) staff       (20)     1322 2022-11-25 20:09:54.000000 aim-4.0.0.dev2/aim/storage/lock_proxy.py
+-rw-r--r--   0 github     (503) staff       (20)     6344 2023-03-31 20:11:31.000000 aim-4.0.0.dev2/aim/storage/locking.py
+drwxr-xr-x   0 github     (503) staff       (20)        0 2023-04-05 11:38:00.748007 aim-4.0.0.dev2/aim/storage/migrations/
+-rw-r--r--   0 github     (503) staff       (20)       38 2022-04-19 22:29:06.000000 aim-4.0.0.dev2/aim/storage/migrations/README
+-rw-r--r--   0 github     (503) staff       (20)        0 2022-04-19 22:29:06.000000 aim-4.0.0.dev2/aim/storage/migrations/__init__.py
+-rw-r--r--   0 github     (503) staff       (20)     2218 2022-04-19 22:29:06.000000 aim-4.0.0.dev2/aim/storage/migrations/alembic.ini
+-rw-r--r--   0 github     (503) staff       (20)     2215 2022-04-19 22:29:06.000000 aim-4.0.0.dev2/aim/storage/migrations/alembic_dev.ini
+-rw-r--r--   0 github     (503) staff       (20)     2339 2022-04-19 22:29:06.000000 aim-4.0.0.dev2/aim/storage/migrations/env.py
+-rw-r--r--   0 github     (503) staff       (20)      494 2022-04-19 22:29:06.000000 aim-4.0.0.dev2/aim/storage/migrations/script.py.mako
+-rw-r--r--   0 github     (503) staff       (20)      965 2022-04-19 22:29:06.000000 aim-4.0.0.dev2/aim/storage/migrations/utils.py
+drwxr-xr-x   0 github     (503) staff       (20)        0 2023-04-05 11:38:00.749109 aim-4.0.0.dev2/aim/storage/migrations/versions/
+-rw-r--r--   0 github     (503) staff       (20)     2841 2022-04-19 22:29:06.000000 aim-4.0.0.dev2/aim/storage/migrations/versions/1ecf8222220d_initial_schema.py
+-rw-r--r--   0 github     (503) staff       (20)      658 2022-04-19 22:29:06.000000 aim-4.0.0.dev2/aim/storage/migrations/versions/3c4f22db7a46_run_end_time.py
+-rw-r--r--   0 github     (503) staff       (20)     1475 2022-11-25 20:09:54.000000 aim-4.0.0.dev2/aim/storage/migrations/versions/46b89d830ad8_.py
+-rw-r--r--   0 github     (503) staff       (20)      653 2022-04-19 22:29:06.000000 aim-4.0.0.dev2/aim/storage/migrations/versions/9ba30ab3b2b4_.py
+-rw-r--r--   0 github     (503) staff       (20)     1516 2022-04-19 22:29:06.000000 aim-4.0.0.dev2/aim/storage/migrations/versions/b07e7b07c8ce_.py
+-rw-r--r--   0 github     (503) staff       (20)      789 2022-04-19 22:29:06.000000 aim-4.0.0.dev2/aim/storage/migrations/versions/fbfe5c4702fb_soft_delete.py
+-rw-r--r--   0 github     (503) staff       (20)     1650 2022-04-19 22:29:06.000000 aim-4.0.0.dev2/aim/storage/object.py
+-rw-r--r--   0 github     (503) staff       (20)   959785 2023-04-05 11:37:58.000000 aim-4.0.0.dev2/aim/storage/prefixview.cpp
+-rw-r--r--   0 github     (503) staff       (20)      770 2022-04-19 22:29:06.000000 aim-4.0.0.dev2/aim/storage/prefixview.pxd
+-rw-r--r--   0 github     (503) staff       (20)    11248 2022-04-19 22:29:06.000000 aim-4.0.0.dev2/aim/storage/prefixview.py
+-rw-r--r--   0 github     (503) staff       (20)    11648 2022-06-15 14:05:59.000000 aim-4.0.0.dev2/aim/storage/proxy.py
+-rw-r--r--   0 github     (503) staff       (20)     4816 2022-07-21 10:42:47.000000 aim-4.0.0.dev2/aim/storage/query.py
+-rw-r--r--   0 github     (503) staff       (20)  1056280 2023-04-05 11:37:59.000000 aim-4.0.0.dev2/aim/storage/rockscontainer.cpp
+-rw-r--r--   0 github     (503) staff       (20)    18514 2023-01-23 20:08:00.000000 aim-4.0.0.dev2/aim/storage/rockscontainer.pyx
+drwxr-xr-x   0 github     (503) staff       (20)        0 2023-04-05 11:38:00.749864 aim-4.0.0.dev2/aim/storage/structured/
+-rw-r--r--   0 github     (503) staff       (20)        0 2022-04-19 22:29:06.000000 aim-4.0.0.dev2/aim/storage/structured/__init__.py
+-rw-r--r--   0 github     (503) staff       (20)     3183 2022-04-19 22:29:06.000000 aim-4.0.0.dev2/aim/storage/structured/db.py
+-rw-r--r--   0 github     (503) staff       (20)     5355 2022-11-25 20:09:54.000000 aim-4.0.0.dev2/aim/storage/structured/entities.py
+-rw-r--r--   0 github     (503) staff       (20)     2959 2022-11-12 00:14:35.000000 aim-4.0.0.dev2/aim/storage/structured/proxy.py
+drwxr-xr-x   0 github     (503) staff       (20)        0 2023-04-05 11:38:00.750980 aim-4.0.0.dev2/aim/storage/structured/sql_engine/
+-rw-r--r--   0 github     (503) staff       (20)        0 2022-04-19 22:29:06.000000 aim-4.0.0.dev2/aim/storage/structured/sql_engine/__init__.py
+-rw-r--r--   0 github     (503) staff       (20)    19882 2023-01-25 20:08:55.000000 aim-4.0.0.dev2/aim/storage/structured/sql_engine/entities.py
+-rw-r--r--   0 github     (503) staff       (20)     3484 2022-04-19 22:29:06.000000 aim-4.0.0.dev2/aim/storage/structured/sql_engine/factory.py
+-rw-r--r--   0 github     (503) staff       (20)     4888 2022-11-25 20:09:54.000000 aim-4.0.0.dev2/aim/storage/structured/sql_engine/models.py
+-rw-r--r--   0 github     (503) staff       (20)     4811 2022-04-19 22:29:06.000000 aim-4.0.0.dev2/aim/storage/structured/sql_engine/utils.py
+-rw-r--r--   0 github     (503) staff       (20)   697830 2023-04-05 11:37:59.000000 aim-4.0.0.dev2/aim/storage/treearrayview.cpp
+-rw-r--r--   0 github     (503) staff       (20)      251 2022-04-19 22:29:06.000000 aim-4.0.0.dev2/aim/storage/treearrayview.pxd
+-rw-r--r--   0 github     (503) staff       (20)     3033 2022-08-02 09:43:44.000000 aim-4.0.0.dev2/aim/storage/treearrayview.py
+-rw-r--r--   0 github     (503) staff       (20)   722166 2023-04-05 11:37:59.000000 aim-4.0.0.dev2/aim/storage/treeutils.cpp
+-rw-r--r--   0 github     (503) staff       (20)     8365 2022-06-15 14:05:59.000000 aim-4.0.0.dev2/aim/storage/treeutils.pyx
+-rw-r--r--   0 github     (503) staff       (20)      707 2022-04-19 22:29:06.000000 aim-4.0.0.dev2/aim/storage/treeutils_non_native.py
+-rw-r--r--   0 github     (503) staff       (20)   515752 2023-04-05 11:37:59.000000 aim-4.0.0.dev2/aim/storage/treeview.cpp
+-rw-r--r--   0 github     (503) staff       (20)      311 2022-04-19 22:29:06.000000 aim-4.0.0.dev2/aim/storage/treeview.pxd
+-rw-r--r--   0 github     (503) staff       (20)     2765 2023-01-24 20:09:40.000000 aim-4.0.0.dev2/aim/storage/treeview.py
+-rw-r--r--   0 github     (503) staff       (20)     8241 2023-02-27 08:16:06.000000 aim-4.0.0.dev2/aim/storage/treeviewproxy.py
+-rw-r--r--   0 github     (503) staff       (20)     1357 2022-04-19 22:29:06.000000 aim-4.0.0.dev2/aim/storage/types.py
+-rw-r--r--   0 github     (503) staff       (20)   812526 2023-04-05 11:37:59.000000 aim-4.0.0.dev2/aim/storage/union.cpp
+-rw-r--r--   0 github     (503) staff       (20)     7919 2023-01-23 20:08:00.000000 aim-4.0.0.dev2/aim/storage/union.pyx
+-rw-r--r--   0 github     (503) staff       (20)   810540 2023-04-05 11:38:00.000000 aim-4.0.0.dev2/aim/storage/utils.cpp
+-rw-r--r--   0 github     (503) staff       (20)      469 2022-04-19 22:29:06.000000 aim-4.0.0.dev2/aim/storage/utils.pxd
+-rw-r--r--   0 github     (503) staff       (20)     2102 2022-04-19 22:29:06.000000 aim-4.0.0.dev2/aim/storage/utils.py
+-rw-r--r--   0 github     (503) staff       (20)      119 2022-04-19 22:29:06.000000 aim-4.0.0.dev2/aim/tensorflow.py
+drwxr-xr-x   0 github     (503) staff       (20)        0 2023-04-05 11:38:00.751612 aim-4.0.0.dev2/aim/utils/
+-rw-r--r--   0 github     (503) staff       (20)       84 2023-03-02 20:49:40.000000 aim-4.0.0.dev2/aim/utils/__init__.py
+-rw-r--r--   0 github     (503) staff       (20)     1209 2023-02-01 20:08:30.000000 aim-4.0.0.dev2/aim/utils/deprecation.py
+-rw-r--r--   0 github     (503) staff       (20)     4728 2023-02-27 08:16:06.000000 aim-4.0.0.dev2/aim/utils/tracking.py
+drwxr-xr-x   0 github     (503) staff       (20)        0 2023-04-05 11:38:00.752481 aim-4.0.0.dev2/aim/web/
+-rw-r--r--   0 github     (503) staff       (20)        0 2022-04-19 22:29:06.000000 aim-4.0.0.dev2/aim/web/__init__.py
+drwxr-xr-x   0 github     (503) staff       (20)        0 2023-04-05 11:38:00.753439 aim-4.0.0.dev2/aim/web/api/
+-rw-r--r--   0 github     (503) staff       (20)     3504 2023-01-23 10:30:27.000000 aim-4.0.0.dev2/aim/web/api/__init__.py
+drwxr-xr-x   0 github     (503) staff       (20)        0 2023-04-05 11:38:00.754340 aim-4.0.0.dev2/aim/web/api/dashboard_apps/
+-rw-r--r--   0 github     (503) staff       (20)        0 2022-04-19 22:29:06.000000 aim-4.0.0.dev2/aim/web/api/dashboard_apps/__init__.py
+-rw-r--r--   0 github     (503) staff       (20)      939 2022-04-19 22:29:06.000000 aim-4.0.0.dev2/aim/web/api/dashboard_apps/models.py
+-rw-r--r--   0 github     (503) staff       (20)      542 2022-04-19 22:29:06.000000 aim-4.0.0.dev2/aim/web/api/dashboard_apps/pydantic_models.py
+-rw-r--r--   0 github     (503) staff       (20)      445 2022-04-19 22:29:06.000000 aim-4.0.0.dev2/aim/web/api/dashboard_apps/serializers.py
+-rw-r--r--   0 github     (503) staff       (20)     2974 2022-04-19 22:29:06.000000 aim-4.0.0.dev2/aim/web/api/dashboard_apps/views.py
+drwxr-xr-x   0 github     (503) staff       (20)        0 2023-04-05 11:38:00.755231 aim-4.0.0.dev2/aim/web/api/dashboards/
+-rw-r--r--   0 github     (503) staff       (20)        0 2022-04-19 22:29:06.000000 aim-4.0.0.dev2/aim/web/api/dashboards/__init__.py
+-rw-r--r--   0 github     (503) staff       (20)      667 2022-04-19 22:29:06.000000 aim-4.0.0.dev2/aim/web/api/dashboards/models.py
+-rw-r--r--   0 github     (503) staff       (20)      652 2022-10-06 00:17:33.000000 aim-4.0.0.dev2/aim/web/api/dashboards/pydantic_models.py
+-rw-r--r--   0 github     (503) staff       (20)      775 2022-10-06 00:17:33.000000 aim-4.0.0.dev2/aim/web/api/dashboards/serializers.py
+-rw-r--r--   0 github     (503) staff       (20)     3341 2022-04-19 22:29:06.000000 aim-4.0.0.dev2/aim/web/api/dashboards/views.py
+-rw-r--r--   0 github     (503) staff       (20)      820 2022-04-19 22:29:06.000000 aim-4.0.0.dev2/aim/web/api/db.py
+drwxr-xr-x   0 github     (503) staff       (20)        0 2023-04-05 11:38:00.755763 aim-4.0.0.dev2/aim/web/api/experiments/
+-rw-r--r--   0 github     (503) staff       (20)        0 2022-04-19 22:29:06.000000 aim-4.0.0.dev2/aim/web/api/experiments/__init__.py
+-rw-r--r--   0 github     (503) staff       (20)      974 2022-11-24 20:09:30.000000 aim-4.0.0.dev2/aim/web/api/experiments/pydantic_models.py
+-rw-r--r--   0 github     (503) staff       (20)     8931 2023-01-19 20:08:35.000000 aim-4.0.0.dev2/aim/web/api/experiments/views.py
+drwxr-xr-x   0 github     (503) staff       (20)        0 2023-04-05 11:38:00.756571 aim-4.0.0.dev2/aim/web/api/projects/
+-rw-r--r--   0 github     (503) staff       (20)        0 2022-04-19 22:29:06.000000 aim-4.0.0.dev2/aim/web/api/projects/__init__.py
+-rw-r--r--   0 github     (503) staff       (20)      735 2022-04-19 22:29:06.000000 aim-4.0.0.dev2/aim/web/api/projects/project.py
+-rw-r--r--   0 github     (503) staff       (20)      943 2022-10-06 00:17:33.000000 aim-4.0.0.dev2/aim/web/api/projects/pydantic_models.py
+-rw-r--r--   0 github     (503) staff       (20)     5200 2023-01-24 20:09:40.000000 aim-4.0.0.dev2/aim/web/api/projects/views.py
+drwxr-xr-x   0 github     (503) staff       (20)        0 2023-04-05 11:38:00.758053 aim-4.0.0.dev2/aim/web/api/runs/
+-rw-r--r--   0 github     (503) staff       (20)        0 2022-04-19 22:29:06.000000 aim-4.0.0.dev2/aim/web/api/runs/__init__.py
+-rw-r--r--   0 github     (503) staff       (20)    12969 2022-07-21 10:42:47.000000 aim-4.0.0.dev2/aim/web/api/runs/object_api_utils.py
+-rw-r--r--   0 github     (503) staff       (20)     6683 2022-07-21 10:42:47.000000 aim-4.0.0.dev2/aim/web/api/runs/object_views.py
+-rw-r--r--   0 github     (503) staff       (20)     4420 2022-12-23 10:19:51.000000 aim-4.0.0.dev2/aim/web/api/runs/pydantic_models.py
+-rw-r--r--   0 github     (503) staff       (20)    15418 2023-02-03 15:21:38.000000 aim-4.0.0.dev2/aim/web/api/runs/utils.py
+-rw-r--r--   0 github     (503) staff       (20)    12137 2023-02-03 15:21:38.000000 aim-4.0.0.dev2/aim/web/api/runs/views.py
+drwxr-xr-x   0 github     (503) staff       (20)        0 2023-04-05 11:38:00.758543 aim-4.0.0.dev2/aim/web/api/tags/
+-rw-r--r--   0 github     (503) staff       (20)        0 2022-04-19 22:29:06.000000 aim-4.0.0.dev2/aim/web/api/tags/__init__.py
+-rw-r--r--   0 github     (503) staff       (20)      871 2022-04-19 22:29:06.000000 aim-4.0.0.dev2/aim/web/api/tags/pydantic_models.py
+-rw-r--r--   0 github     (503) staff       (20)     4272 2022-04-19 22:29:06.000000 aim-4.0.0.dev2/aim/web/api/tags/views.py
+-rw-r--r--   0 github     (503) staff       (20)     1169 2022-04-19 22:29:06.000000 aim-4.0.0.dev2/aim/web/api/utils.py
+-rw-r--r--   0 github     (503) staff       (20)     1589 2022-05-16 21:25:24.000000 aim-4.0.0.dev2/aim/web/api/views.py
+-rw-r--r--   0 github     (503) staff       (20)      508 2022-08-11 13:58:02.000000 aim-4.0.0.dev2/aim/web/configs.py
+drwxr-xr-x   0 github     (503) staff       (20)        0 2023-04-05 11:38:00.758705 aim-4.0.0.dev2/aim/web/middlewares/
+-rw-r--r--   0 github     (503) staff       (20)        0 2022-04-19 22:29:06.000000 aim-4.0.0.dev2/aim/web/middlewares/__init__.py
+drwxr-xr-x   0 github     (503) staff       (20)        0 2023-04-05 11:38:00.759049 aim-4.0.0.dev2/aim/web/middlewares/profiler/
+-rw-r--r--   0 github     (503) staff       (20)       81 2022-04-19 22:29:06.000000 aim-4.0.0.dev2/aim/web/middlewares/profiler/__init__.py
+-rw-r--r--   0 github     (503) staff       (20)     3654 2022-04-19 22:29:06.000000 aim-4.0.0.dev2/aim/web/middlewares/profiler/profiler.py
+drwxr-xr-x   0 github     (503) staff       (20)        0 2023-04-05 11:38:00.759900 aim-4.0.0.dev2/aim/web/migrations/
+-rw-r--r--   0 github     (503) staff       (20)       38 2022-04-19 22:29:06.000000 aim-4.0.0.dev2/aim/web/migrations/README
+-rw-r--r--   0 github     (503) staff       (20)      810 2022-04-19 22:29:06.000000 aim-4.0.0.dev2/aim/web/migrations/alembic.ini
+-rw-r--r--   0 github     (503) staff       (20)      807 2022-04-19 22:29:06.000000 aim-4.0.0.dev2/aim/web/migrations/alembic_dev.ini
+-rw-r--r--   0 github     (503) staff       (20)     2792 2022-04-19 22:29:06.000000 aim-4.0.0.dev2/aim/web/migrations/env.py
+-rw-r--r--   0 github     (503) staff       (20)      494 2022-04-19 22:29:06.000000 aim-4.0.0.dev2/aim/web/migrations/script.py.mako
+drwxr-xr-x   0 github     (503) staff       (20)        0 2023-04-05 11:38:00.760584 aim-4.0.0.dev2/aim/web/migrations/versions/
+-rw-r--r--   0 github     (503) staff       (20)     2183 2022-04-19 22:29:06.000000 aim-4.0.0.dev2/aim/web/migrations/versions/11672b13f92c_.py
+-rw-r--r--   0 github     (503) staff       (20)     1545 2022-04-19 22:29:06.000000 aim-4.0.0.dev2/aim/web/migrations/versions/517a45b2e62c_.py
+-rw-r--r--   0 github     (503) staff       (20)     5592 2022-04-19 22:29:06.000000 aim-4.0.0.dev2/aim/web/migrations/versions/5ae8371b7481_.py
+-rw-r--r--   0 github     (503) staff       (20)     7262 2022-04-19 22:29:06.000000 aim-4.0.0.dev2/aim/web/migrations/versions/73a3d004c227_.py
+-rw-r--r--   0 github     (503) staff       (20)       55 2022-04-19 22:29:06.000000 aim-4.0.0.dev2/aim/web/run.py
+-rw-r--r--   0 github     (503) staff       (20)     3055 2022-04-19 22:29:06.000000 aim-4.0.0.dev2/aim/web/utils.py
+-rw-r--r--   0 github     (503) staff       (20)       96 2022-04-19 22:29:06.000000 aim-4.0.0.dev2/aim/xgboost.py
+drwxr-xr-x   0 github     (503) staff       (20)        0 2023-04-05 11:38:00.687344 aim-4.0.0.dev2/aim.egg-info/
+-rw-r--r--   0 github     (503) staff       (20)    37083 2023-04-05 11:38:00.000000 aim-4.0.0.dev2/aim.egg-info/PKG-INFO
+-rw-r--r--   0 github     (503) staff       (20)    11901 2023-04-05 11:38:00.000000 aim-4.0.0.dev2/aim.egg-info/SOURCES.txt
+-rw-r--r--   0 github     (503) staff       (20)        1 2023-04-05 11:38:00.000000 aim-4.0.0.dev2/aim.egg-info/dependency_links.txt
+-rw-r--r--   0 github     (503) staff       (20)      102 2023-04-05 11:38:00.000000 aim-4.0.0.dev2/aim.egg-info/entry_points.txt
+-rw-r--r--   0 github     (503) staff       (20)      422 2023-04-05 11:38:00.000000 aim-4.0.0.dev2/aim.egg-info/requires.txt
+-rw-r--r--   0 github     (503) staff       (20)       28 2023-04-05 11:38:00.000000 aim-4.0.0.dev2/aim.egg-info/top_level.txt
+drwxr-xr-x   0 github     (503) staff       (20)        0 2023-04-05 11:38:00.678887 aim-4.0.0.dev2/performance_tests/
+drwxr-xr-x   0 github     (503) staff       (20)        0 2023-04-05 11:38:00.761949 aim-4.0.0.dev2/performance_tests/sdk/
+-rw-r--r--   0 github     (503) staff       (20)        0 2022-04-19 22:29:06.000000 aim-4.0.0.dev2/performance_tests/sdk/__init__.py
+-rw-r--r--   0 github     (503) staff       (20)      469 2022-04-19 22:29:06.000000 aim-4.0.0.dev2/performance_tests/sdk/queries.py
+-rw-r--r--   0 github     (503) staff       (20)     1199 2022-04-19 22:29:06.000000 aim-4.0.0.dev2/performance_tests/sdk/test_data_collection.py
+-rw-r--r--   0 github     (503) staff       (20)     1134 2022-04-19 22:29:06.000000 aim-4.0.0.dev2/performance_tests/sdk/test_query.py
+-rw-r--r--   0 github     (503) staff       (20)     1881 2022-06-18 00:13:24.000000 aim-4.0.0.dev2/performance_tests/sdk/utils.py
+drwxr-xr-x   0 github     (503) staff       (20)        0 2023-04-05 11:38:00.762822 aim-4.0.0.dev2/performance_tests/storage/
+-rw-r--r--   0 github     (503) staff       (20)        0 2022-04-19 22:29:06.000000 aim-4.0.0.dev2/performance_tests/storage/__init__.py
+-rw-r--r--   0 github     (503) staff       (20)      678 2022-04-19 22:29:06.000000 aim-4.0.0.dev2/performance_tests/storage/test_container_open.py
+-rw-r--r--   0 github     (503) staff       (20)      690 2022-04-19 22:29:06.000000 aim-4.0.0.dev2/performance_tests/storage/test_iterative_access.py
+-rw-r--r--   0 github     (503) staff       (20)      802 2022-04-19 22:29:06.000000 aim-4.0.0.dev2/performance_tests/storage/test_random_access.py
+-rw-r--r--   0 github     (503) staff       (20)     1262 2022-06-18 00:13:24.000000 aim-4.0.0.dev2/performance_tests/storage/utils.py
+-rw-r--r--   0 github     (503) staff       (20)       84 2023-03-02 20:49:40.000000 aim-4.0.0.dev2/pyproject.toml
+-rw-r--r--   0 github     (503) staff       (20)      336 2023-04-05 11:38:00.769132 aim-4.0.0.dev2/setup.cfg
+-rw-r--r--   0 github     (503) staff       (20)     6716 2023-03-02 20:49:40.000000 aim-4.0.0.dev2/setup.py
+drwxr-xr-x   0 github     (503) staff       (20)        0 2023-04-05 11:38:00.679152 aim-4.0.0.dev2/tests/
+drwxr-xr-x   0 github     (503) staff       (20)        0 2023-04-05 11:38:00.764587 aim-4.0.0.dev2/tests/api/
+-rw-r--r--   0 github     (503) staff       (20)        0 2022-04-19 22:29:06.000000 aim-4.0.0.dev2/tests/api/__init__.py
+-rw-r--r--   0 github     (503) staff       (20)     5155 2022-04-19 22:29:06.000000 aim-4.0.0.dev2/tests/api/test_dashboards_api.py
+-rw-r--r--   0 github     (503) staff       (20)     4335 2022-09-25 12:02:15.000000 aim-4.0.0.dev2/tests/api/test_project_api.py
+-rw-r--r--   0 github     (503) staff       (20)    10653 2023-01-23 10:30:27.000000 aim-4.0.0.dev2/tests/api/test_run_api.py
+-rw-r--r--   0 github     (503) staff       (20)    21533 2023-01-23 10:30:27.000000 aim-4.0.0.dev2/tests/api/test_run_images_api.py
+-rw-r--r--   0 github     (503) staff       (20)    12787 2023-01-23 10:30:27.000000 aim-4.0.0.dev2/tests/api/test_structured_data_api.py
+drwxr-xr-x   0 github     (503) staff       (20)        0 2023-04-05 11:38:00.765352 aim-4.0.0.dev2/tests/integrations/
+-rw-r--r--   0 github     (503) staff       (20)        0 2022-04-19 22:29:06.000000 aim-4.0.0.dev2/tests/integrations/__init__.py
+-rw-r--r--   0 github     (503) staff       (20)     1167 2022-04-19 22:29:06.000000 aim-4.0.0.dev2/tests/integrations/test_dvc_metadata.py
+-rw-r--r--   0 github     (503) staff       (20)     1093 2023-01-13 20:10:23.000000 aim-4.0.0.dev2/tests/integrations/test_hf_datasets.py
+-rw-r--r--   0 github     (503) staff       (20)      961 2022-04-19 22:29:06.000000 aim-4.0.0.dev2/tests/integrations/test_hub_dataset.py
+drwxr-xr-x   0 github     (503) staff       (20)        0 2023-04-05 11:38:00.767668 aim-4.0.0.dev2/tests/sdk/
+-rw-r--r--   0 github     (503) staff       (20)        0 2022-04-19 22:29:06.000000 aim-4.0.0.dev2/tests/sdk/__init__.py
+-rw-r--r--   0 github     (503) staff       (20)     2312 2022-04-19 22:29:06.000000 aim-4.0.0.dev2/tests/sdk/test_image_construction.py
+-rw-r--r--   0 github     (503) staff       (20)     2665 2022-09-25 12:02:15.000000 aim-4.0.0.dev2/tests/sdk/test_resource_tracker.py
+-rw-r--r--   0 github     (503) staff       (20)     1022 2022-11-01 00:13:35.000000 aim-4.0.0.dev2/tests/sdk/test_run_apis.py
+-rw-r--r--   0 github     (503) staff       (20)     1147 2022-09-01 19:23:53.000000 aim-4.0.0.dev2/tests/sdk/test_run_creation_checks.py
+-rw-r--r--   0 github     (503) staff       (20)     1661 2022-04-19 22:29:06.000000 aim-4.0.0.dev2/tests/sdk/test_run_finalization_time.py
+-rw-r--r--   0 github     (503) staff       (20)     1214 2022-11-01 00:13:35.000000 aim-4.0.0.dev2/tests/sdk/test_run_metric_types.py
+-rw-r--r--   0 github     (503) staff       (20)     4631 2022-09-25 12:02:15.000000 aim-4.0.0.dev2/tests/sdk/test_run_track_type_checking.py
+-rw-r--r--   0 github     (503) staff       (20)    10444 2022-09-25 12:02:15.000000 aim-4.0.0.dev2/tests/sdk/test_run_write_container_data.py
+-rw-r--r--   0 github     (503) staff       (20)     4517 2022-06-01 01:05:15.000000 aim-4.0.0.dev2/tests/sdk/test_utils.py
+drwxr-xr-x   0 github     (503) staff       (20)        0 2023-04-05 11:38:00.768516 aim-4.0.0.dev2/tests/storage/
+-rw-r--r--   0 github     (503) staff       (20)        0 2022-04-19 22:29:06.000000 aim-4.0.0.dev2/tests/storage/__init__.py
+-rw-r--r--   0 github     (503) staff       (20)     5677 2022-09-25 12:02:15.000000 aim-4.0.0.dev2/tests/storage/test_query.py
+-rw-r--r--   0 github     (503) staff       (20)     1482 2022-06-18 00:13:24.000000 aim-4.0.0.dev2/tests/storage/test_query_with_epoch_none.py
+-rw-r--r--   0 github     (503) staff       (20)     1342 2022-09-25 12:02:15.000000 aim-4.0.0.dev2/tests/storage/test_structured_db.py
```

### Comparing `aim-4.0.0.dev1/LICENSE` & `aim-4.0.0.dev2/LICENSE`

 * *Files identical despite different names*

### Comparing `aim-4.0.0.dev1/PKG-INFO` & `aim-4.0.0.dev2/PKG-INFO`

 * *Files 24% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: aim
-Version: 4.0.0.dev1
+Version: 4.0.0.dev2
 Summary: A super-easy way to record, search and compare AI experiments.
 Classifier: License :: OSI Approved :: Apache Software License
 Classifier: Programming Language :: Python
 Classifier: Programming Language :: Python :: 3
 Classifier: Programming Language :: Python :: 3.7
 Classifier: Programming Language :: Python :: 3.8
 Classifier: Programming Language :: Python :: 3.9
@@ -12,135 +12,221 @@
 Classifier: Programming Language :: Python :: 3.11
 Classifier: Programming Language :: Python :: Implementation :: PyPy
 Requires-Python: >=3.7.0
 Description-Content-Type: text/markdown
 License-File: LICENSE
 
 <div align="center">
-  <img src="https://user-images.githubusercontent.com/13848158/154338760-edfe1885-06f3-4e02-87fe-4b13a403516b.png">
-  <h3>An easy-to-use & supercharged open-source experiment tracker</h3>
-  Aim logs your training runs, enables a beautiful UI to compare them and an API to query them programmatically.
+  <table>
+    <tbody>
+      <tr>
+        <td>Drop a star to support Aim ⭐</td>
+        <td>
+          <a href="https://community.aimstack.io/">Join Aim discord community</a>
+          <img width="20px" src="https://user-images.githubusercontent.com/13848158/226759622-063b725d-8b3e-4c75-80c7-11fb04b7adf5.png">
+        </td>
+      </tr>
+    </tbody>
+  </table>
 </div>
 
-<br/>
-
-<img src="https://user-images.githubusercontent.com/13848158/154338753-34484cda-95b8-4da8-a610-7fdf198c05fd.png">
+<div align="center">
+  <img src="https://user-images.githubusercontent.com/13848158/225620298-9f9293e9-a138-41fd-bd77-21d53d0490b7.png">
+  <h3>
+    An easy-to-use & supercharged open-source experiment tracker
+  </h3>
+  Aim logs your training runs and any AI Metadata, enables a beautiful UI to compare, observe them and an API to query them programmatically.
+</div>
 
-<p align="center">
-  <a href="#about-aim"><b>About</b></a> &bull;
-  <a href="#why-use-aim"><b>Features</b></a> &bull;
-  <a href="#demos"><b>Demos</b></a> &bull;
-  <a href="https://github.com/aimhubio/aim/tree/main/examples"><b>Examples</b></a> &bull;
-  <a href="#quick-start"><b>Quick Start</b></a> &bull;
-  <a href="https://aimstack.readthedocs.io/en/latest/"><b>Documentation</b></a> &bull;
-  <a href="#roadmap"><b>Roadmap</b></a> &bull;
-  <a href="https://community.aimstack.io/"><b>Discord Community</b></a> &bull;
-  <a href="https://twitter.com/aimstackio"><b>Twitter</b></a>
-</p>
+<br/>
 
 <div align="center">
   
+  [![Discord Server](https://dcbadge.vercel.app/api/server/zXq2NfVdtF?compact=true&style=flat)](https://community.aimstack.io/)
+  [![Twitter Follow](https://img.shields.io/twitter/follow/aimstackio?style=social)](https://twitter.com/aimstackio)
+  [![Medium](https://img.shields.io/badge/Medium-12100E?style=flat&logo=medium&logoColor=white)](https://medium.com/aimstack)
+  
   [![Platform Support](https://img.shields.io/badge/platform-Linux%20%7C%20macOS-blue)]()
-  [![PyPI - Python Version](https://img.shields.io/pypi/pyversions/aim)](https://pypi.org/project/aim/)
+  [![PyPI - Python Version](https://img.shields.io/badge/python-%3E%3D%203.7-blue)](https://pypi.org/project/aim/)
   [![PyPI Package](https://img.shields.io/pypi/v/aim?color=yellow)](https://pypi.org/project/aim/)
   [![License](https://img.shields.io/badge/License-Apache%202.0-orange.svg)](https://opensource.org/licenses/Apache-2.0)
   [![PyPI Downloads](https://img.shields.io/pypi/dw/aim?color=green)](https://pypi.org/project/aim/)
   [![Issues](https://img.shields.io/github/issues/aimhubio/aim)](http://github.com/aimhubio/aim/issues)
   
 </div>
 
 <div align="center">
-  <sub>Integrates seamlessly with your favorite tools</sub>
   <br/>
+  <kbd>
+    <img src="https://user-images.githubusercontent.com/13848158/136374529-af267918-5dc6-4a4e-8ed2-f6333a332f96.gif" />
+  </kbd>
+</div>
+
+</br>
+
+<div align="center">
+  <sub><strong>SEAMLESSLY INTEGRATES WITH:</strong></sub>
   <br/>
-  <img src="https://user-images.githubusercontent.com/13848158/155354389-d0301620-77ea-4629-a743-f7aa249e14b5.png" width="60" />
-  <img src="https://user-images.githubusercontent.com/13848158/155354496-b39d7b1c-63ef-40f0-9e59-c08d2c5e337c.png" width="60" />
-  <img src="https://user-images.githubusercontent.com/13848158/155354380-3755c741-6960-42ca-b93e-84a8791f088c.png" width="60" />
-  <img src="https://user-images.githubusercontent.com/13848158/155354342-7df0ef5e-63d2-4df7-b9f1-d2fc0e95f53f.png" width="60" />
-  <img src="https://user-images.githubusercontent.com/13848158/155354392-afbff3de-c845-4d86-855d-53df569f91d1.png" width="60" />
-  <img src="https://user-images.githubusercontent.com/13848158/155354355-89210506-e7e5-4d37-b2d6-ad3fda62ef13.png" width="60" />
-  <img src="https://user-images.githubusercontent.com/13848158/155354397-8af8e1d3-4067-405e-9d42-1f131663ed22.png" width="60" />
   <br/>
-  <img src="https://user-images.githubusercontent.com/13848158/155354513-f7486146-3891-4f3f-934f-e58bbf9ce695.png" width="60" />
-  <img src="https://user-images.githubusercontent.com/13848158/155354500-c0471ce6-b2ce-4172-b9e4-07a197256303.png" width="60" />
-  <img src="https://user-images.githubusercontent.com/13848158/155354361-9f911785-008d-4b75-877e-651e026cf47e.png" width="60" />
-  <img src="https://user-images.githubusercontent.com/13848158/155354373-1879ae61-b5d1-41f0-a4f1-04b639b6f05e.png" width="60" />
-  <img src="https://user-images.githubusercontent.com/13848158/155354483-75d9853f-7154-4d95-8190-9ad7a73d6654.png" width="60" />
-  <img src="https://user-images.githubusercontent.com/13848158/155354329-cf7c3352-a72a-478d-82a7-04e3833b03b7.png" width="60" />
-  <img src="https://user-images.githubusercontent.com/13848158/155354349-dcdf3bc3-d7a9-4f34-8258-4824a57f59c7.png" width="60" />
-  <img src="https://user-images.githubusercontent.com/13848158/155354471-518f1814-7a41-4b23-9caf-e516507343f1.png" width="60" />
-  <img src="https://user-images.githubusercontent.com/48801049/165162736-2cc5da39-38aa-4093-874f-e56d0ba9cea2.png" width="60" />
-  <img src="https://user-images.githubusercontent.com/48801049/165074282-36ad18eb-1124-434d-8439-728c22cd7ac7.png" width="60" />
+  <img src="https://user-images.githubusercontent.com/97726819/225954732-2b263308-8ed8-4df3-810b-704840328e98.png" height="60" />
+  <img src="https://user-images.githubusercontent.com/97726819/225954727-04eccf0e-51ed-4f2d-8f3b-c9a675ca8e8f.png" height="60" />
+  <img src="https://user-images.githubusercontent.com/97726819/225954728-ca2f498d-51a7-487b-bd69-ffb5f0c2af58.png" height="60" />
+  <img src="https://user-images.githubusercontent.com/97726819/225954689-1076998c-42f4-4e31-ab47-d9f39575fda1.png" height="60" />
+  <img src="https://user-images.githubusercontent.com/97726819/225954739-0231d659-3202-4458-9c35-ba92d1f079b8.png" height="60" />
+  <img src="https://user-images.githubusercontent.com/97726819/225954697-ef2c7091-b089-4b68-8543-80ce7275b683.png" height="60" />
+  <img src="https://user-images.githubusercontent.com/97726819/225954743-dbfe1e98-7b9f-446a-9fe4-ad4fd562f3df.png" height="60" />
+  <img src="https://user-images.githubusercontent.com/97726819/225954736-7c52ab5a-6780-4375-a6f8-b394dae3ad31.png" height="60" />
+  <img src="https://user-images.githubusercontent.com/97726819/225954710-36551a71-b26d-4665-af20-44ee452dd5dd.png" height="60" />
+  <img src="https://user-images.githubusercontent.com/97726819/225954707-4bc078b5-ae6f-4847-bc2c-3f81959accb2.png" height="60" />
+  <img src="https://user-images.githubusercontent.com/97726819/225954725-a4d4c32c-75db-470a-b1da-698982faa23c.png" height="60" />
+  <img src="https://user-images.githubusercontent.com/97726819/225954665-8d844747-a857-41b8-9104-7c27a8bdb81a.png" height="60" />
+  <img src="https://user-images.githubusercontent.com/97726819/225954686-b9c8ec57-d4fc-44e1-a4b8-443db381a00f.png" height="60" />
+  <img src="https://user-images.githubusercontent.com/97726819/225954693-94bc20b4-f51a-4130-8d5f-ddee30d81205.png" height="60" />
+  <img src="https://user-images.githubusercontent.com/97726819/225954674-42fbfdb3-0351-492d-9ea3-1d3ab2b545f5.png" height="60" />
+  <img src="https://user-images.githubusercontent.com/97726819/225954678-25f1b626-2cb1-4e7e-ad83-f7c8ab679c6f.png" height="60" />
+  <img src="https://user-images.githubusercontent.com/97726819/225954702-d18d2706-dc87-4e09-a678-f010f6d95736.png" height="60" />
 </div>
 
+<br/>
+
 <div align="center">
+  <sub><strong>TRUSTED BY ML TEAMS FROM:</strong></sub>  
   <br/>
-  <kbd>
-    <img src="https://user-images.githubusercontent.com/13848158/136374529-af267918-5dc6-4a4e-8ed2-f6333a332f96.gif" />
-  </kbd>
+  <br/>
+  <img src="https://user-images.githubusercontent.com/97726819/225952594-a21546f4-987f-42bd-9154-c22b50632b55.png" height="55" />
+  <img src="https://user-images.githubusercontent.com/97726819/225953224-291fbb6d-e31a-4e36-90ba-92a1dc20bacc.png" height="55" />
+  <img src="https://user-images.githubusercontent.com/97726819/225953339-4fcc3c99-dda2-4529-ac2a-29c8293be323.png" height="55" />
+  <img src="https://user-images.githubusercontent.com/97726819/225953084-1d88325a-ad5f-49eb-aa67-f064c4b9f39c.png" height="55" />
+  <img src="https://user-images.githubusercontent.com/97726819/225952955-397e0f26-f01e-4b25-bd70-9f292a6f77c2.png" height="55" />
+  <img src="https://user-images.githubusercontent.com/97726819/225952682-a843827b-e870-429d-96d8-3b4fd45471cd.png" height="55" />
+  <img src="https://user-images.githubusercontent.com/97726819/225952831-1c0e36aa-4120-4635-ab4e-bf1bc685477b.png" height="55" />
+  <img src="https://user-images.githubusercontent.com/97726819/225953432-4b27653a-aa12-4fbf-897c-01349afa2ad0.png" height="55" />
 </div>
 
-# About Aim
+<br/>
 
-| Track and version ML runs | Visualize runs via beautiful UI | Query runs metadata via SDK |
-|:--------------------:|:------------------------:|:-------------------:|
-| <img width="600px" src="https://user-images.githubusercontent.com/13848158/154337794-e9310239-6614-41b3-a95b-bb91f0bb6c4f.png"> | <img width="600px" src="https://user-images.githubusercontent.com/13848158/154337788-03fe5b31-0fa3-44af-ae79-2861707d8602.png"> | <img width="600px" src="https://user-images.githubusercontent.com/13848158/154337793-85175c78-5659-4dd0-bb2d-05017278e2fa.png"> |
+<p align="center">
+  AimStack offers enterprise support that's beyond core Aim. Contact via <a href="mailto:hello@aimstack.io">hello@aimstack.io</a> e-mail.
+</p>
 
-Aim is an open-source, self-hosted ML experiment tracking tool. 
-It's good at tracking lots (1000s) of training runs and it allows you to compare them with a performant and beautiful UI.
+---
 
-You can use not only the great Aim UI but also its SDK to query your runs' metadata programmatically. 
-That's especially useful for automations and additional analysis on a Jupyter Notebook.
+<h3 align="center">
+  <a href="#-about"><b>About</b></a> &bull;
+  <a href="#-demos"><b>Demos</b></a> &bull;
+  <a href="#-ecosystem"><b>Ecosystem</b></a> &bull;
+  <a href="#-quick-start"><b>Quick Start</b></a> &bull;
+  <a href="https://github.com/aimhubio/aim/tree/main/examples"><b>Examples</b></a> &bull;
+  <a href="https://aimstack.readthedocs.io/en/latest/"><b>Documentation</b></a> &bull;
+  <a href="#-community"><b>Community</b></a> &bull;
+  <a href="https://aimstack.io/blog"><b>Blog</b></a>
+</h3>  
 
+---
 
-Aim's mission is to democratize AI dev tools.
+# ℹ️ About
 
-# Why use Aim?
+Aim is an open-source, self-hosted ML experiment tracking tool designed to handle 10,000s of training runs.
 
-### Compare 100s of runs in a few clicks - build models faster
+Aim provides a performant and beautiful UI for exploring and comparing training runs.
+Additionally, its SDK enables programmatic access to tracked metadata — perfect for automations and Jupyter Notebook analysis.
 
-- Compare, group and aggregate 100s of metrics thanks to effective visualizations.
-- Analyze, learn correlations and patterns between hparams and metrics.
-- Easy pythonic search to query the runs you want to explore.
+<p align="center">
+  <strong>Aim's mission is to democratize AI dev tools 🎯 </strong>
+</p>
 
-### Deep dive into details of each run for easy debugging
+<div align="center">
+  <img src="https://user-images.githubusercontent.com/13848158/226426018-f7c11c9b-78d9-4ee4-b292-df28b3e8eaa6.jpg" height="140" />
+  <img src="https://user-images.githubusercontent.com/13848158/226426005-f7e83923-0f92-44a4-88e4-1735a3d3e119.jpg" height="140" />
+  <img src="https://user-images.githubusercontent.com/13848158/226426015-4f1122d8-c96a-443f-8698-3db942b1972a.jpg" height="140" />
+</div>
 
-- Hyperparameters, metrics, images, distributions, audio, text - all available at hand on an intuitive UI to understand the performance of your model.
-- Easily track plots built via your favourite visualisation tools, like plotly and matplotlib.
-- Analyze system resource usage to effectively utilize computational resources.
+</br>
 
-### Have all relevant information organised and accessible for easy governance
+<div align="center">
+  <table>
+    <tbody>
+      <tr>
+        <th>Log Metadata Across Your ML Pipeline 💾</th>
+        <th>Visualize & Compare Metadata via UI 📊</th>
+      </tr>
+      <tr>
+        <td>
+          <ul>
+            <li>ML experiments and any metadata tracking</li>
+            <li>Integration with popular ML frameworks</li>
+            <li>Easy migration from other experiment trackers</li>
+            </ul>
+          </td>
+        <td>
+          <ul>
+            <li>Metadata visualization via Aim Explorers</li>
+            <li>Grouping and aggregation</li>
+            <li>Querying using Python expressions</li>
+          </ul>
+        </td>
+      </tr>
+      <tr>
+        <th>Run ML Trainings Effectively ⚡</th>
+        <th>Organize Your Experiments 🗂️</th>
+      </tr>
+      <tr>
+        <td>
+          <ul>
+            <li>System info and resource usage tracking</li>
+            <li>Real-time alerting on training progress</li>
+            <li>Logging and configurable notifications</li>
+          </ul>
+        </td>
+        <td>
+          <ul>
+            <li>Detailed run information for easy debugging</li>
+            <li>Centralized dashboard for holistic view</li>
+            <li>Runs grouping with tags and experiments</li></ul>
+        </td>
+      </tr>
+    </tbody>
+  </table>
+</div>
 
-- Centralized dashboard to holistically view all your runs, their hparams and results.
-- Use SDK to query/access all your runs and tracked metadata.
-- You own your data - Aim is open source and self hosted.
+# 🎬 Demos
 
-# Demos
+Check out live Aim demos NOW to see it in action.
 
-| Machine translation | lightweight-GAN |
+| [Machine translation experiments](http://play.aimstack.io:10001/metrics?grouping=HQGdK9Xxy35e6sY1CYkCmk1WbWMN2AsCNfJJ3d1RJYLtrVPMoF5UpGiA6CF8bEJnfzRsKpqespf3AEuKSVrhUYvYk9MxzNGA9XZWYUf6phEg8AMbZGLRVDXnAPDuo8tueqsST1ZLizWzQwDYJWHUza6pyB2Eojt9uWqNHUdb858TqDRnCJzqiVJXKXEzFWUyvU8MckJo1qpqWWCTb4GpYN6DUJZx2GXDGR21e2xxd4m7PmNUnbA9B3apLttZoipJF6c3v7tNUKmb6irpqnNB3yc57tqYDa1XZuKfDxkMtyFdQ1x95K4jjsTVwhftEWLze35QNcxNXRCGGS9o9yEfTLG26GUX2zjPZFCjjMGU6vV7z1xRccK8MyoGrLSgAQCbvk68dTGBHpXUBvCRq8N&chart=FviZzVrt4fVQPjpCLr9sVGGrcR5etSroyqambiKpm3nTgpyv4eQxKuwNX9uN8UtKmzYUhUyTMBEANHmtbwjLApkvnYeNbxGNC6PVcoqi65m1XJnSrvgt8WiD89BapFAWRUwAGx6SWD7KZPsk3RQyysU7W7FjD3Q99NusxFGhsEfD6HXc7i8xH9KHDRGjLwh6x9VTtSp4FS8HEvpLSiiJoX7LCTi8pB7dXvrQ8G5w3jPsFz4qXYFdsVaCNL1BpFFZuiqQNkfbnM84gEq7UmiV1VzM4oS3AgQHxADG3kpBVp6eKTey9F1Swd4FcUkFA9QEPjgQgqwRGjkquZ2bdDDVLBnCh7JPvboP2kifCiZZ5MDdV9MMx6PKHp4DusWyWLXiHQYPkpGPWBiuccMUXDsuJaCWJbuABdY7CyiJMv1jdHYkjabygSxehPVyEDefWAtjBfv2vaeM1xv63jadbmpKYFxft7qmuT9HvVxiGvRgs4RQFxy8K4rtFBca3HNs1mDaaY81gy9MGXyw7BS5Fniu92jaJpsWDdg6Y3AQBLZtrpJy2obEZ4yzJaCVT7JUNPAyyCUNLck393VFLoEkaD9CU5npK5R7tj1c1G3gkMNQXnSXy5NpSj8deMmXV5qz3JKu1nq2caGQKcqjzy2gLkExdm674AMFjSg9yFjK6VqASXQ17NKtWRUvaYoxGbHDAFQaMKWKh8QLm22QA9mKT8NksLptWozbgDvafnQLNMvezLU5bvKV5o75PAWYiRB56RcYfEhzaB6YWdgL7TJicyY5rFi6Az8UZ7wqB3N5iMuZdpxhKn5KbZDxyuUMuvVt24i5LVPPmmwQtqxMoJ4aLo48a2YvDW6TAkdQjNjvn6KcEEz6GTixujb1YHhMUD8v4AepWKEwKz1ddEca1P2wLQjbpihCuaqbxeohnuZZLogJdUBojBEDgrnrrVpPBaLLEkGSpkJbtrsKUuEeBo1AF3yNgHftLbynGpobVF5DhmsmddmiA6c8vSTokJxHhjpnW8mAcNHBRtmVJCT7VkdHSAhNypM4Hivwfx5jCccG9LauKmCeRMDzHiA57TX9W6ttcPHSvUyQorARQAd2oeNY4H83hZjHh9Bt8iwKZRt4xK6hrTR8tif7hq8eURXrGH9Ys7TzykXK8FHHWvLNzNnYf3E4a9NkD43MjfKvMM1hj4Q2K8MHbmRCqrmFrHP5kim9shq6mhLPTgwha32nvnrBkfPQVPwpGTzKuwE&select=CdsQ7jVNkogQhRzQR3e28Ek39AZ4Ma2y37k5zJaf9EZmQhMjy8GtGm4LGU6dRFuAVG7mYww5xDrQAE74KHQ3Kk1e6661RmcmNALAUjtHyCmrTVBMCnBGNiuq1y7EzmxoodYHU1BV1rnoefQAw2kTBtbWi11hV1P4LcwFCcXfUWF6rpRC7ehEnUCTqUV4bkGVJPLcmk9mdmiGwa2YgmnSShNGPVGZiEi1rMVECyngSRVdqdZwAeXBGWFLfqF1KbZeCo4MTF4SSmFupJ9zLhYbuojEbopyFWHQ6xs3sq9epPeaQziLM4Js7oFYRmuFWUYdFqnZngmewXWmi7tQAgVqhiT6dMjG2eTdfgX6WuRSuoHALkh2XJhHA6GfZLUcxC5Ni9YyKuBTamtaYarbNNJJ8z15WWvuUkLpjgHdEpE2h924xFdu8aoZNuiQxYGvcndaW1BTGMXS5fTKPqYfe2n8Ky2HWPkcX3hEXtyawu1F9BndKNaXLPgsdAoFBArBZnSe28YtSmTa5LRucKVBAxakvv5MWMXchAmpaGFQbZyYUoMgQLcJd7Y96x6zSR7nhwr5Ar81BrmqYz2WFLuk7osUbwsc9HbSG6CQt8p6Vg2u7DjKaZXW8pjkPHAKrHWtHEDiJPJ5rj6VsdFm3) | [lightweight-GAN experiments](http://play.aimstack.io:10002/images?grouping=E1zQzcmtDR3wibEa1MVysTvCyZEv1T8ixkCxTWExCyMnHtX2HyiF9eszvPgfd2xdJ5TUTKGpSs1bsLVq5tHAV3uWtsZmmckn6HjNtVCMyQDJpwhiEy5tAyw&select=2NEXuD7fFoaLcwRjymjA1wLmUrGs9s3AiXcCW82C367SwJt18CAB6xzkMGowrUDuDwggE1huaPVcQJpQUsmAQx1CnGiqCUBp2jPMd5mMNPX2QKQMcmvu9ZykBNkeBvCQFPd9ERuQD2g1EjWuvyJ3H53mAZTfp94LCXvR9CUsG5ei2CjQUzfZLM6DCyUr1GPaEVnY5f1EwzicNxXuoutkBgqCqaobJ7Do4q4eHAA6ooiWU6ekS3D2sLj6qYwhVTjfGCPfbWwBiH83nFkY3fLExzdeTY2zeUHeeYikQR9S7xHbVD8WvjekdQVp8X4dNLJZxiVmEqHpPRnU3ZrYsMhE7yFAAgjJwPNUzLTt6YFrtZBcmc4rwAC2oyrqysUSEr6gzL6LcJ6yuqDGf9D5tzftHbTLDkhc8B2sCgTS&images=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)|
 |:---:|:---:|
-| <a href="http://play.aimstack.io:10001/metrics?grouping=HQGdK9Xxy35e6sY1CYkCmk1WbWMN2AsCNfJJ3d1RJYLtrVPMoF5UpGiA6CF8bEJnfzRsKpqespf3AEuKSVrhUYvYk9MxzNGA9XZWYUf6phEg8AMbZGLRVDXnAPDuo8tueqsST1ZLizWzQwDYJWHUza6pyB2Eojt9uWqNHUdb858TqDRnCJzqiVJXKXEzFWUyvU8MckJo1qpqWWCTb4GpYN6DUJZx2GXDGR21e2xxd4m7PmNUnbA9B3apLttZoipJF6c3v7tNUKmb6irpqnNB3yc57tqYDa1XZuKfDxkMtyFdQ1x95K4jjsTVwhftEWLze35QNcxNXRCGGS9o9yEfTLG26GUX2zjPZFCjjMGU6vV7z1xRccK8MyoGrLSgAQCbvk68dTGBHpXUBvCRq8N&chart=FviZzVrt4fVQPjpCLr9sVGGrcR5etSroyqambiKpm3nTgpyv4eQxKuwNX9uN8UtKmzYUhUyTMBEANHmtbwjLApkvnYeNbxGNC6PVcoqi65m1XJnSrvgt8WiD89BapFAWRUwAGx6SWD7KZPsk3RQyysU7W7FjD3Q99NusxFGhsEfD6HXc7i8xH9KHDRGjLwh6x9VTtSp4FS8HEvpLSiiJoX7LCTi8pB7dXvrQ8G5w3jPsFz4qXYFdsVaCNL1BpFFZuiqQNkfbnM84gEq7UmiV1VzM4oS3AgQHxADG3kpBVp6eKTey9F1Swd4FcUkFA9QEPjgQgqwRGjkquZ2bdDDVLBnCh7JPvboP2kifCiZZ5MDdV9MMx6PKHp4DusWyWLXiHQYPkpGPWBiuccMUXDsuJaCWJbuABdY7CyiJMv1jdHYkjabygSxehPVyEDefWAtjBfv2vaeM1xv63jadbmpKYFxft7qmuT9HvVxiGvRgs4RQFxy8K4rtFBca3HNs1mDaaY81gy9MGXyw7BS5Fniu92jaJpsWDdg6Y3AQBLZtrpJy2obEZ4yzJaCVT7JUNPAyyCUNLck393VFLoEkaD9CU5npK5R7tj1c1G3gkMNQXnSXy5NpSj8deMmXV5qz3JKu1nq2caGQKcqjzy2gLkExdm674AMFjSg9yFjK6VqASXQ17NKtWRUvaYoxGbHDAFQaMKWKh8QLm22QA9mKT8NksLptWozbgDvafnQLNMvezLU5bvKV5o75PAWYiRB56RcYfEhzaB6YWdgL7TJicyY5rFi6Az8UZ7wqB3N5iMuZdpxhKn5KbZDxyuUMuvVt24i5LVPPmmwQtqxMoJ4aLo48a2YvDW6TAkdQjNjvn6KcEEz6GTixujb1YHhMUD8v4AepWKEwKz1ddEca1P2wLQjbpihCuaqbxeohnuZZLogJdUBojBEDgrnrrVpPBaLLEkGSpkJbtrsKUuEeBo1AF3yNgHftLbynGpobVF5DhmsmddmiA6c8vSTokJxHhjpnW8mAcNHBRtmVJCT7VkdHSAhNypM4Hivwfx5jCccG9LauKmCeRMDzHiA57TX9W6ttcPHSvUyQorARQAd2oeNY4H83hZjHh9Bt8iwKZRt4xK6hrTR8tif7hq8eURXrGH9Ys7TzykXK8FHHWvLNzNnYf3E4a9NkD43MjfKvMM1hj4Q2K8MHbmRCqrmFrHP5kim9shq6mhLPTgwha32nvnrBkfPQVPwpGTzKuwE&select=CdsQ7jVNkogQhRzQR3e28Ek39AZ4Ma2y37k5zJaf9EZmQhMjy8GtGm4LGU6dRFuAVG7mYww5xDrQAE74KHQ3Kk1e6661RmcmNALAUjtHyCmrTVBMCnBGNiuq1y7EzmxoodYHU1BV1rnoefQAw2kTBtbWi11hV1P4LcwFCcXfUWF6rpRC7ehEnUCTqUV4bkGVJPLcmk9mdmiGwa2YgmnSShNGPVGZiEi1rMVECyngSRVdqdZwAeXBGWFLfqF1KbZeCo4MTF4SSmFupJ9zLhYbuojEbopyFWHQ6xs3sq9epPeaQziLM4Js7oFYRmuFWUYdFqnZngmewXWmi7tQAgVqhiT6dMjG2eTdfgX6WuRSuoHALkh2XJhHA6GfZLUcxC5Ni9YyKuBTamtaYarbNNJJ8z15WWvuUkLpjgHdEpE2h924xFdu8aoZNuiQxYGvcndaW1BTGMXS5fTKPqYfe2n8Ky2HWPkcX3hEXtyawu1F9BndKNaXLPgsdAoFBArBZnSe28YtSmTa5LRucKVBAxakvv5MWMXchAmpaGFQbZyYUoMgQLcJd7Y96x6zSR7nhwr5Ar81BrmqYz2WFLuk7osUbwsc9HbSG6CQt8p6Vg2u7DjKaZXW8pjkPHAKrHWtHEDiJPJ5rj6VsdFm3"> <img width="800px" src="https://user-images.githubusercontent.com/13848158/154340796-c9e91b13-8ee0-4a67-bcde-8cf3aaa7ba99.jpg"> </a> | <a href="http://play.aimstack.io:10002/images?grouping=E1zQzcmtDR3wibEa1MVysTvCyZEv1T8ixkCxTWExCyMnHtX2HyiF9eszvPgfd2xdJ5TUTKGpSs1bsLVq5tHAV3uWtsZmmckn6HjNtVCMyQDJpwhiEy5tAyw&select=2NEXuD7fFoaLcwRjymjA1wLmUrGs9s3AiXcCW82C367SwJt18CAB6xzkMGowrUDuDwggE1huaPVcQJpQUsmAQx1CnGiqCUBp2jPMd5mMNPX2QKQMcmvu9ZykBNkeBvCQFPd9ERuQD2g1EjWuvyJ3H53mAZTfp94LCXvR9CUsG5ei2CjQUzfZLM6DCyUr1GPaEVnY5f1EwzicNxXuoutkBgqCqaobJ7Do4q4eHAA6ooiWU6ekS3D2sLj6qYwhVTjfGCPfbWwBiH83nFkY3fLExzdeTY2zeUHeeYikQR9S7xHbVD8WvjekdQVp8X4dNLJZxiVmEqHpPRnU3ZrYsMhE7yFAAgjJwPNUzLTt6YFrtZBcmc4rwAC2oyrqysUSEr6gzL6LcJ6yuqDGf9D5tzftHbTLDkhc8B2sCgTS&images=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"> <img width="800px" src="https://user-images.githubusercontent.com/13848158/154340790-bc7b7a21-e8a1-43a1-809d-4060b5bfb60f.jpg"> </a> |
+| <a href="http://play.aimstack.io:10001/metrics?grouping=HQGdK9Xxy35e6sY1CYkCmk1WbWMN2AsCNfJJ3d1RJYLtrVPMoF5UpGiA6CF8bEJnfzRsKpqespf3AEuKSVrhUYvYk9MxzNGA9XZWYUf6phEg8AMbZGLRVDXnAPDuo8tueqsST1ZLizWzQwDYJWHUza6pyB2Eojt9uWqNHUdb858TqDRnCJzqiVJXKXEzFWUyvU8MckJo1qpqWWCTb4GpYN6DUJZx2GXDGR21e2xxd4m7PmNUnbA9B3apLttZoipJF6c3v7tNUKmb6irpqnNB3yc57tqYDa1XZuKfDxkMtyFdQ1x95K4jjsTVwhftEWLze35QNcxNXRCGGS9o9yEfTLG26GUX2zjPZFCjjMGU6vV7z1xRccK8MyoGrLSgAQCbvk68dTGBHpXUBvCRq8N&chart=FviZzVrt4fVQPjpCLr9sVGGrcR5etSroyqambiKpm3nTgpyv4eQxKuwNX9uN8UtKmzYUhUyTMBEANHmtbwjLApkvnYeNbxGNC6PVcoqi65m1XJnSrvgt8WiD89BapFAWRUwAGx6SWD7KZPsk3RQyysU7W7FjD3Q99NusxFGhsEfD6HXc7i8xH9KHDRGjLwh6x9VTtSp4FS8HEvpLSiiJoX7LCTi8pB7dXvrQ8G5w3jPsFz4qXYFdsVaCNL1BpFFZuiqQNkfbnM84gEq7UmiV1VzM4oS3AgQHxADG3kpBVp6eKTey9F1Swd4FcUkFA9QEPjgQgqwRGjkquZ2bdDDVLBnCh7JPvboP2kifCiZZ5MDdV9MMx6PKHp4DusWyWLXiHQYPkpGPWBiuccMUXDsuJaCWJbuABdY7CyiJMv1jdHYkjabygSxehPVyEDefWAtjBfv2vaeM1xv63jadbmpKYFxft7qmuT9HvVxiGvRgs4RQFxy8K4rtFBca3HNs1mDaaY81gy9MGXyw7BS5Fniu92jaJpsWDdg6Y3AQBLZtrpJy2obEZ4yzJaCVT7JUNPAyyCUNLck393VFLoEkaD9CU5npK5R7tj1c1G3gkMNQXnSXy5NpSj8deMmXV5qz3JKu1nq2caGQKcqjzy2gLkExdm674AMFjSg9yFjK6VqASXQ17NKtWRUvaYoxGbHDAFQaMKWKh8QLm22QA9mKT8NksLptWozbgDvafnQLNMvezLU5bvKV5o75PAWYiRB56RcYfEhzaB6YWdgL7TJicyY5rFi6Az8UZ7wqB3N5iMuZdpxhKn5KbZDxyuUMuvVt24i5LVPPmmwQtqxMoJ4aLo48a2YvDW6TAkdQjNjvn6KcEEz6GTixujb1YHhMUD8v4AepWKEwKz1ddEca1P2wLQjbpihCuaqbxeohnuZZLogJdUBojBEDgrnrrVpPBaLLEkGSpkJbtrsKUuEeBo1AF3yNgHftLbynGpobVF5DhmsmddmiA6c8vSTokJxHhjpnW8mAcNHBRtmVJCT7VkdHSAhNypM4Hivwfx5jCccG9LauKmCeRMDzHiA57TX9W6ttcPHSvUyQorARQAd2oeNY4H83hZjHh9Bt8iwKZRt4xK6hrTR8tif7hq8eURXrGH9Ys7TzykXK8FHHWvLNzNnYf3E4a9NkD43MjfKvMM1hj4Q2K8MHbmRCqrmFrHP5kim9shq6mhLPTgwha32nvnrBkfPQVPwpGTzKuwE&select=CdsQ7jVNkogQhRzQR3e28Ek39AZ4Ma2y37k5zJaf9EZmQhMjy8GtGm4LGU6dRFuAVG7mYww5xDrQAE74KHQ3Kk1e6661RmcmNALAUjtHyCmrTVBMCnBGNiuq1y7EzmxoodYHU1BV1rnoefQAw2kTBtbWi11hV1P4LcwFCcXfUWF6rpRC7ehEnUCTqUV4bkGVJPLcmk9mdmiGwa2YgmnSShNGPVGZiEi1rMVECyngSRVdqdZwAeXBGWFLfqF1KbZeCo4MTF4SSmFupJ9zLhYbuojEbopyFWHQ6xs3sq9epPeaQziLM4Js7oFYRmuFWUYdFqnZngmewXWmi7tQAgVqhiT6dMjG2eTdfgX6WuRSuoHALkh2XJhHA6GfZLUcxC5Ni9YyKuBTamtaYarbNNJJ8z15WWvuUkLpjgHdEpE2h924xFdu8aoZNuiQxYGvcndaW1BTGMXS5fTKPqYfe2n8Ky2HWPkcX3hEXtyawu1F9BndKNaXLPgsdAoFBArBZnSe28YtSmTa5LRucKVBAxakvv5MWMXchAmpaGFQbZyYUoMgQLcJd7Y96x6zSR7nhwr5Ar81BrmqYz2WFLuk7osUbwsc9HbSG6CQt8p6Vg2u7DjKaZXW8pjkPHAKrHWtHEDiJPJ5rj6VsdFm3"> <img src="https://user-images.githubusercontent.com/97726819/225964524-0051c2c7-8554-43ae-82b8-adcb77bcf1ba.png"> </a> | <a href="http://play.aimstack.io:10002/images?grouping=E1zQzcmtDR3wibEa1MVysTvCyZEv1T8ixkCxTWExCyMnHtX2HyiF9eszvPgfd2xdJ5TUTKGpSs1bsLVq5tHAV3uWtsZmmckn6HjNtVCMyQDJpwhiEy5tAyw&select=2NEXuD7fFoaLcwRjymjA1wLmUrGs9s3AiXcCW82C367SwJt18CAB6xzkMGowrUDuDwggE1huaPVcQJpQUsmAQx1CnGiqCUBp2jPMd5mMNPX2QKQMcmvu9ZykBNkeBvCQFPd9ERuQD2g1EjWuvyJ3H53mAZTfp94LCXvR9CUsG5ei2CjQUzfZLM6DCyUr1GPaEVnY5f1EwzicNxXuoutkBgqCqaobJ7Do4q4eHAA6ooiWU6ekS3D2sLj6qYwhVTjfGCPfbWwBiH83nFkY3fLExzdeTY2zeUHeeYikQR9S7xHbVD8WvjekdQVp8X4dNLJZxiVmEqHpPRnU3ZrYsMhE7yFAAgjJwPNUzLTt6YFrtZBcmc4rwAC2oyrqysUSEr6gzL6LcJ6yuqDGf9D5tzftHbTLDkhc8B2sCgTS&images=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"> <img src="https://user-images.githubusercontent.com/97726819/225948275-a41946ea-89f4-45f1-bce1-251c84dcddca.png"> </a> |
 | Training logs of a neural translation model(from WMT'19 competition). | Training logs of 'lightweight' GAN, proposed in ICLR 2021. |
 
-| FastSpeech 2 | Simple MNIST |
+| [FastSpeech 2 experiments](http://play.aimstack.io:10004/runs/d9e89aa7875e44b2ba85612a/audios)| [Simple MNIST](http://play.aimstack.io:10003/runs/7f083da898624a2c98e0f363/distributions) |
 |:---:|:---:|
-| <a href="http://play.aimstack.io:10004/runs/d9e89aa7875e44b2ba85612a/audios"> <img width="800px" src="https://user-images.githubusercontent.com/13848158/154340778-dbe19620-2f27-4298-b0cb-caf3904760f1.jpg"> </a> | <a href="http://play.aimstack.io:10003/runs/7f083da898624a2c98e0f363/distributions"> <img width="800px" src="https://user-images.githubusercontent.com/13848158/154340785-a7e4d9fd-d048-4207-8cd1-c4edff9cca6a.jpg"> </a> |
+| <a href="http://play.aimstack.io:10004/runs/d9e89aa7875e44b2ba85612a/audios"> <img src="https://user-images.githubusercontent.com/97726819/225948457-567526da-a329-4c53-a9a7-98dfe392d4c4.png"> </a> | <a href="http://play.aimstack.io:10003/runs/7f083da898624a2c98e0f363/distributions"> <img src="https://user-images.githubusercontent.com/97726819/225948599-ff39c5b7-ae7d-4deb-8bc9-5eee1e189d89.png"> </a> |
 | Training logs of Microsoft's "FastSpeech 2: Fast and High-Quality End-to-End Text to Speech". | Simple MNIST training logs. |
 
-# Quick Start
+# 🌍 Ecosystem
+
+Aim is not just an experiment tracker. It's a groundwork for an ecosystem. 
+Check out the two most famous Aim-based tools.
+
+| [aimlflow](https://github.com/aimhubio/aimlflow) | [Aim-spaCy](https://github.com/aimhubio/aim-spacy) |
+|:---:|:---:|
+| ![aimlflow](https://user-images.githubusercontent.com/97726819/225957836-cdec88e3-4993-435a-a135-d78be3ac1635.png) | ![Aim-spaCy](https://user-images.githubusercontent.com/97726819/225957990-4edc4525-1f65-4405-b663-ce7af888bdfa.png) |
+| Exploring MLflow experiments with a powerful UI | an Aim-based spaCy experiment tracker |
+
+# 🏁 Quick start
 
 Follow the steps below to get started with Aim.
 
-**1. Install Aim on your training environment**
+## 1. Install Aim on your training environment
 
 ```shell
 pip3 install aim
 ```
 
-**2. Integrate Aim with your code**
+## 2. Integrate Aim with your code
 
 ```python
 from aim import Run
 
 # Initialize a new run
 run = Run()
 
@@ -154,237 +240,130 @@
 for i in range(10):
     run.track(i, name='loss', step=i, context={ "subset":"train" })
     run.track(i, name='acc', step=i, context={ "subset":"train" })
 ```
 
 _See the full list of supported trackable objects(e.g. images, text, etc) [here](https://aimstack.readthedocs.io/en/latest/quick_start/supported_types.html)._
 
-**3. Run the training as usual and start Aim UI**
+## 3. Run the training as usual and start Aim UI
 
 ```shell
 aim up
 ```
 
-**4. Or query runs programmatically via SDK**
-
-```python
-from aim import Repo
-
-my_repo = Repo('/path/to/aim/repo')
-
-query = "metric.name == 'loss'" # Example query
-
-# Get collection of metrics
-for run_metrics_collection in my_repo.query_metrics(query).iter_runs():
-    for metric in run_metrics_collection:
-        # Get run params
-        params = metric.run[...]
-        # Get metric values
-        steps, metric_values = metric.values.sparse_numpy()
-```
-
-# Integrations
+## Learn more
 
 <details>
 <summary>
-  Integrate PyTorch Lightning
+<strong>Migrate from other tools</strong>
 </summary>
 
-```python
-from aim.pytorch_lightning import AimLogger
-
-# ...
-trainer = pl.Trainer(logger=AimLogger(experiment='experiment_name'))
-# ...
-```
+</br>
 
-_See documentation [here](https://aimstack.readthedocs.io/en/latest/quick_start/integrations.html#integration-with-pytorch-lightning)._
+Aim has built-in converters to easily migrate logs from other tools. 
+These migrations cover the most common usage scenarios.
+In case of custom and complex scenarios you can use Aim SDK to implement your own conversion script.
+
+- [TensorBoard logs converter](https://aimstack.readthedocs.io/en/latest/quick_start/convert_data.html#show-tensorboard-logs-in-aim)
+- [MLFlow logs converter](https://aimstack.readthedocs.io/en/latest/quick_start/convert_data.html#show-mlflow-logs-in-aim)
+- [Weights & Biases logs converter](https://aimstack.readthedocs.io/en/latest/quick_start/convert_data.html#show-weights-and-biases-logs-in-aim)
 
 </details>
 
 <details>
 <summary>
-  Integrate Hugging Face
+<strong>Integrate Aim into an existing project</strong>
 </summary>
 
-```python
-from aim.hugging_face import AimCallback
+</br>
 
-# ...
-aim_callback = AimCallback(repo='/path/to/logs/dir', experiment='mnli')
-trainer = Trainer(
-    model=model,
-    args=training_args,
-    train_dataset=train_dataset if training_args.do_train else None,
-    eval_dataset=eval_dataset if training_args.do_eval else None,
-    callbacks=[aim_callback],
-    # ...
-)
-# ...
-```
+Aim easily integrates with a wide range of ML frameworks, providing built-in callbacks for most of them.
 
-_See documentation [here](https://aimstack.readthedocs.io/en/latest/quick_start/integrations.html#integration-with-hugging-face)._
+- [Integration with Pytorch Ignite](https://aimstack.readthedocs.io/en/latest/quick_start/integrations.html#integration-with-pytorch-ignite)
+- [Integration with Pytorch Lightning](https://aimstack.readthedocs.io/en/latest/quick_start/integrations.html#integration-with-pytorch-lightning)
+- [Integration with Hugging Face](https://aimstack.readthedocs.io/en/latest/quick_start/integrations.html#integration-with-hugging-face)
+- [Integration with Keras & tf.Keras](https://aimstack.readthedocs.io/en/latest/quick_start/integrations.html#integration-with-keras-tf-keras)
+- [Integration with Keras Tuner](https://aimstack.readthedocs.io/en/latest/quick_start/integrations.html#integration-with-keras-tuner)
+- [Integration with XGboost](https://aimstack.readthedocs.io/en/latest/quick_start/integrations.html#integration-with-xgboost)
+- [Integration with CatBoost](https://aimstack.readthedocs.io/en/latest/quick_start/integrations.html#integration-with-catboost)
+- [Integration with LightGBM](https://aimstack.readthedocs.io/en/latest/quick_start/integrations.html#integration-with-lightgbm)
+- [Integration with fastai](https://aimstack.readthedocs.io/en/latest/quick_start/integrations.html#integration-with-fastai)
+- [Integration with MXNet](https://aimstack.readthedocs.io/en/latest/quick_start/integrations.html#integration-with-mxnet)
+- [Integration with Optuna](https://aimstack.readthedocs.io/en/latest/quick_start/integrations.html#integration-with-optuna)
+- [Integration with PaddlePaddle](https://aimstack.readthedocs.io/en/latest/quick_start/integrations.html#integration-with-paddlepaddle)
+- [Integration with Stable-Baselines3](https://aimstack.readthedocs.io/en/latest/quick_start/integrations.html#integration-with-stable-baselines3)
+- [Integration with Acme](https://aimstack.readthedocs.io/en/latest/quick_start/integrations.html#integration-with-acme)
+- [Integration with Prophet](https://aimstack.readthedocs.io/en/latest/quick_start/integrations.html#integration-with-prophet)
 
 </details>
 
 <details>
 <summary>
-  Integrate Keras & tf.keras
+<strong>Query runs programmatically via SDK</strong>
 </summary>
 
-```python
-import aim
-
-# ...
-model.fit(x_train, y_train, epochs=epochs, callbacks=[
-    aim.keras.AimCallback(repo='/path/to/logs/dir', experiment='experiment_name')
-    
-    # Use aim.tensorflow.AimCallback in case of tf.keras
-    aim.tensorflow.AimCallback(repo='/path/to/logs/dir', experiment='experiment_name')
-])
-# ...
-```
-
-_See documentation [here](https://aimstack.readthedocs.io/en/latest/quick_start/integrations.html#integration-with-keras-tf-keras)._
-
-</details>
+</br>
 
-<details>
-<summary>
-  Integrate KerasTuner
-</summary>
+Aim Python SDK empowers you to query and access any piece of tracked metadata with ease.
 
 ```python
-from aim.keras_tuner import AimCallback
-
-# ...
-tuner.search(
-    train_ds,
-    validation_data=test_ds,
-    callbacks=[AimCallback(tuner=tuner, repo='.', experiment='keras_tuner_test')],
-)
-# ...
-```
-
-_See documentation [here](https://aimstack.readthedocs.io/en/latest/quick_start/integrations.html#integration-with-kerastuner)._
-
-</details>
+from aim import Repo
 
-<details>
-<summary>
-  Integrate XGBoost
-</summary>
+my_repo = Repo('/path/to/aim/repo')
 
-```python
-from aim.xgboost import AimCallback
+query = "metric.name == 'loss'" # Example query
 
-# ...
-aim_callback = AimCallback(repo='/path/to/logs/dir', experiment='experiment_name')
-bst = xgb.train(param, xg_train, num_round, watchlist, callbacks=[aim_callback])
-# ...
+# Get collection of metrics
+for run_metrics_collection in my_repo.query_metrics(query).iter_runs():
+    for metric in run_metrics_collection:
+        # Get run params
+        params = metric.run[...]
+        # Get metric values
+        steps, metric_values = metric.values.sparse_numpy()
 ```
 
-_See documentation [here](https://aimstack.readthedocs.io/en/latest/quick_start/integrations.html#integration-with-xgboost)._
 </details>
 
-
 <details>
 <summary>
-  Integrate CatBoost
+<strong>Set up a centralized tracking server</strong>
 </summary>
 
-```python
-from aim.catboost import AimLogger
-
-# ...
-model.fit(train_data, train_labels, log_cout=AimLogger(loss_function='Logloss'), logging_level="Info")
-# ...
-```
-
-_See documentation [here](https://aimstack.readthedocs.io/en/latest/quick_start/integrations.html#integration-with-catboost)._
-</details>
+</br>
 
+Aim remote tracking server allows running experiments in a multi-host environment and collect tracked data in a centralized location.
 
+See the docs on how to [set up the remote server](https://aimstack.readthedocs.io/en/latest/using/remote_tracking.html).
 
-<details>
-<summary>
-  Integrate fastai
-</summary>
-
-```python
-from aim.fastai import AimCallback
-
-# ...
-learn = cnn_learner(dls, resnet18, pretrained=True,
-                    loss_func=CrossEntropyLossFlat(),
-                    metrics=accuracy, model_dir="/tmp/model/",
-                    cbs=AimCallback(repo='.', experiment='fastai_test'))
-# ...
-```
-
-_See documentation [here](https://aimstack.readthedocs.io/en/latest/quick_start/integrations.html#integration-with-fastai)._
 </details>
 
-
 <details>
 <summary>
-  Integrate LightGBM
+<strong>Deploy Aim on kubernetes</strong>
 </summary>
 
-```python
-from aim.lightgbm import AimCallback
+</br>
+
+- The official Aim docker image: https://hub.docker.com/r/aimstack/aim
+- A guide on how to deploy Aim on kubernetes: https://aimstack.readthedocs.io/en/latest/using/k8s_deployment.html
 
-# ...
-aim_callback = AimCallback(experiment='lgb_test')
-aim_callback.experiment['hparams'] = params
-
-gbm = lgb.train(params,
-                lgb_train,
-                num_boost_round=20,
-                valid_sets=lgb_eval,
-                callbacks=[aim_callback, lgb.early_stopping(stopping_rounds=5)])
-# ...
-```
 
-_See documentation [here](https://aimstack.readthedocs.io/en/latest/quick_start/integrations.html#integration-with-lightgbm)._
 </details>
 
+Read the full documentation on [aimstack.readthedocs.io](https://aimstack.readthedocs.io) 📖
+
+# 🆚 Comparisons to familiar tools
 
 <details>
 <summary>
-  Integrate PyTorch Ignite
+  <strong>TensorBoard vs Aim</strong>
 </summary>
 
-```python
-from aim.pytorch_ignite import AimLogger
-
-# ...
-aim_logger = AimLogger()
-
-aim_logger.log_params({
-    "model": model.__class__.__name__,
-    "pytorch_version": str(torch.__version__),
-    "ignite_version": str(ignite.__version__),
-})
-
-aim_logger.attach_output_handler(
-    trainer,
-    event_name=Events.ITERATION_COMPLETED,
-    tag="train",
-    output_transform=lambda loss: {'loss': loss}
-)
-# ...
-```
-
-_See documentation [here](https://aimstack.readthedocs.io/en/latest/quick_start/integrations.html#integration-with-pytorch-ignite)._
-</details>
-
-# Comparisons to familiar tools
+</br>
 
-### Tensorboard
 **Training run comparison**
 
 Order of magnitude faster training run comparison with Aim
 - The tracked params are first class citizens at Aim. You can search, group, aggregate via params - deeply explore all the tracked data (metrics, params, images) on the UI.
 - With tensorboard the users are forced to record those parameters in the training run name to be able to search and compare. This causes a super-tedius comparison experience and usability issues on the UI when there are many experiments and params. **TensorBoard doesn't have features to group, aggregate the metrics**
 
 **Scalability**
@@ -393,49 +372,117 @@
 - TensorBoard becomes really slow and hard to use when a few hundred training runs are queried / compared.
 
 **Beloved TB visualizations to be added on Aim**
 
 - Embedding projector.
 - Neural network visualization.
 
-### MLFlow
+</details>
+
+<details>
+<summary>
+  <strong>MLflow vs Aim</strong>
+</summary>
+
+</br>
+
 MLFlow is an end-to-end ML Lifecycle tool.
 Aim is focused on training tracking.
 The main differences of Aim and MLflow are around the UI scalability and run comparison features.
 
+Aim and MLflow are a perfect match - check out the [aimlflow](https://github.com/aimhubio/aimlflow) - the tool that enables Aim supoerpowers on Mlflow.
+
 **Run comparison**
 
 - Aim treats tracked parameters as first-class citizens. Users can query runs, metrics, images and filter using the params.
 - MLFlow does have a search by tracked config, but there are no grouping, aggregation, subplotting by hyparparams and other comparison features available.
 
 **UI Scalability**
 
 - Aim UI can handle several thousands of metrics at the same time smoothly with 1000s of steps. It may get shaky when you explore 1000s of metrics with 10000s of steps each. But we are constantly optimizing!
 - MLflow UI becomes slow to use when there are a few hundreds of runs.
 
-### Weights and Biases
+</details>
+
+<details>
+<summary>
+  <strong>Weights and Biases vs Aim</strong>
+</summary>
+
+</br>
 
 Hosted vs self-hosted
+
 - Weights and Biases is a hosted closed-source MLOps platform.
 - Aim is self-hosted, free and open-source experiment tracking tool.
 
-# Roadmap
+</details>
+
+# 🛣️ Roadmap
 
-## Detailed Sprints
+## Detailed milestones
 
-:sparkle: The [Aim product roadmap](https://github.com/orgs/aimhubio/projects/3)
+The [Aim product roadmap](https://github.com/orgs/aimhubio/projects/3) :sparkle: 
 
 - The `Backlog` contains the issues we are going to choose from and prioritize weekly
 - The issues are mainly prioritized by the highly-requested features
 
 ## High-level roadmap
 
-The high-level features we are going to work on the next few months
+The high-level features we are going to work on the next few months:
+
+**In progress**
+
+- [ ] Aim SDK low-level interface
+- [ ] Dashboards – customizable layouts with embedded explorers
+- [ ] Ergonomic UI kit
+- [ ] Text Explorer
+
+<details>
+<summary>
+  <strong>Next-up</strong>
+</summary>
+
+</br>
+
+**Aim UI**
+
+- Runs management
+    - Runs explorer – query and visualize runs data(images, audio, distributions, ...) in a central dashboard
+- Explorers
+    - Distributions Explorer
+
+**SDK and Storage**
+
+- Scalability
+    - Smooth UI and SDK experience with over 10.000 runs
+- Runs management
+    - CLI commands
+        - Reporting - runs summary and run details in a CLI compatible format
+        - Manipulations – copy, move, delete runs, params and sequences
+- Cloud storage support – store runs blob(e.g. images) data on the cloud
+- Artifact storage – store files, model checkpoints, and beyond
+
+**Integrations**
+
+- ML Frameworks:
+    - Shortlist: scikit-learn
+- Resource management tools
+    - Shortlist: Kubeflow, Slurm
+- Workflow orchestration tools
+
+</details>
+
+<details>
+<summary>
+  <strong>Done</strong>
+</summary>
+
+</br>
 
-### Done
   - [x] Live updates (Shipped: _Oct 18 2021_)
   - [x] Images tracking and visualization (Start: _Oct 18 2021_, Shipped: _Nov 19 2021_)
   - [x] Distributions tracking and visualization (Start: _Nov 10 2021_, Shipped: _Dec 3 2021_)
   - [x] Jupyter integration (Start: _Nov 18 2021_, Shipped: _Dec 3 2021_)
   - [x] Audio tracking and visualization (Start: _Dec 6 2021_, Shipped: _Dec 17 2021_)
   - [x] Transcripts tracking and visualization (Start: _Dec 6 2021_, Shipped: _Dec 17 2021_)
   - [x] Plotly integration (Start: _Dec 1 2021_, Shipped: _Dec 17 2021_)
@@ -463,54 +510,58 @@
   - [x] Integration with MXNet (Start: _Sep 20 2022_, Shipped: _Oct 6 2022_)
   - [x] Project overview page (Start: _Sep 1 2022_, Shipped: _Oct 6 2022_)
   - [x] Remote tracking server scaling (Start: _Sep 11 2022_, Shipped: _Nov 26 2022_)
   - [x] Integration with PaddlePaddle (Start: _Oct 2 2022_, Shipped: _Nov 26 2022_)
   - [x] Integration with Optuna (Start: _Oct 2 2022_, Shipped: _Nov 26 2022_)
   - [x] Audios Explorer (Start: _Oct 30 2022_, Shipped: _Nov 26 2022_)
   - [x] Experiment page (Start: _Nov 9 2022_, Shipped: _Nov 26 2022_)
+  - [x] HuggingFace datasets (Start: _Dec 29 2022_, _Feb 3 2023_)
 
-### In Progress
-  - [ ] Aim SDK low-level interface (Start: _Aug 22 2022_, )
-  - [ ] HuggingFace datasets (Start: _Dec 29 2022_, )
+</details>
 
-### To Do
+# 👥 Community
 
-**Aim UI**
+## Aim README badge
 
-- Runs management
-    - Runs explorer – query and visualize runs data(images, audio, distributions, ...) in a central dashboard
-- Explorers
-    - Text Explorer
-    - Distributions Explorer
-- Dashboards – customizable layouts with embedded explorers
+Add Aim badge to your README, if you've enjoyed using Aim in your work:
 
-**SDK and Storage**
+[![Aim](https://img.shields.io/badge/powered%20by-Aim-%231473E6)](https://github.com/aimhubio/aim)
 
-- Scalability
-    - Smooth UI and SDK experience with over 10.000 runs
-- Runs management
-    - CLI interfaces
-        - Reporting - runs summary and run details in a CLI compatible format
-        - Manipulations – copy, move, delete runs, params and sequences
+```
+[![Aim](https://img.shields.io/badge/powered%20by-Aim-%231473E6)](https://github.com/aimhubio/aim)
+```
 
-**Integrations**
+## Cite Aim in your papers
 
-- ML Frameworks:
-    - Shortlist: MONAI, SpaCy, Raytune
-- Resource management tools
-    - Shortlist: Kubeflow, Slurm
-- Workflow orchestration tools
-- Others: Hydra, Google MLMD, Streamlit, ...
+In case you've found Aim helpful in your research journey, we'd be thrilled if you could acknowledge Aim's contribution:
+
+```bibtex
+@software{Arakelyan_Aim_2020,
+  author = {Arakelyan, Gor and Soghomonyan, Gevorg and {The Aim team}},
+  doi = {10.5281/zenodo.6536395},
+  license = {Apache-2.0},
+  month = {6},
+  title = {{Aim}},
+  url = {https://github.com/aimhubio/aim},
+  version = {3.9.3},
+  year = {2020}
+}
+```
+
+## Contributing to Aim
+
+Considering contibuting to Aim? 
+To get started, please take a moment to read the [CONTRIBUTING.md](https://github.com/aimhubio/aim/blob/main/CONTRIBUTING.md) guide. 
 
-### On hold
+Join Aim contributors by submitting your first pull request. Happy coding! 😊
 
-- scikit-learn integration
-- Cloud storage support – store runs blob(e.g. images) data on the cloud (Start: _Mar 21 2022_)
-- Artifact storage – store files, model checkpoints, and beyond (Start: _Mar 21 2022_)
+<a href="https://github.com/aimhubio/aim/graphs/contributors">
+  <img src="https://contrib.rocks/image?repo=aimhubio/aim" />
+</a>
 
-## Community
+Made with [contrib.rocks](https://contrib.rocks).
 
-### If you have questions
+## More questions?
 
 1. [Read the docs](https://aimstack.readthedocs.io/en/latest/)
 2. [Open a feature request or report a bug](https://github.com/aimhubio/aim/issues)
 3. [Join Discord community server](https://community.aimstack.io/)
```

#### html2text {}

```diff
@@ -1,219 +1,270 @@
-Metadata-Version: 2.1 Name: aim Version: 4.0.0.dev1 Summary: A super-easy way
+Metadata-Version: 2.1 Name: aim Version: 4.0.0.dev2 Summary: A super-easy way
 to record, search and compare AI experiments. Classifier: License :: OSI
 Approved :: Apache Software License Classifier: Programming Language :: Python
 Classifier: Programming Language :: Python :: 3 Classifier: Programming
 Language :: Python :: 3.7 Classifier: Programming Language :: Python :: 3.8
 Classifier: Programming Language :: Python :: 3.9 Classifier: Programming
 Language :: Python :: 3.10 Classifier: Programming Language :: Python :: 3.11
 Classifier: Programming Language :: Python :: Implementation :: PyPy Requires-
 Python: >=3.7.0 Description-Content-Type: text/markdown License-File: LICENSE
- [https://user-images.githubusercontent.com/13848158/154338760-edfe1885-06f3-
-                          4e02-87fe-4b13a403516b.png]
+                               Join_Aim_discord_community [https://user-
+Drop a star to support Aim â­images.githubusercontent.com/13848158/226759622-
+                               063b725d-8b3e-4c75-80c7-11fb04b7adf5.png]
+ [https://user-images.githubusercontent.com/13848158/225620298-9f9293e9-a138-
+                          41fd-bd77-21d53d0490b7.png]
     **** An easy-to-use & supercharged open-source experiment tracker ****
-Aim logs your training runs, enables a beautiful UI to compare them and an API
-                        to query them programmatically.
+  Aim logs your training runs and any AI Metadata, enables a beautiful UI to
+       compare, observe them and an API to query them programmatically.
 
-[https://user-images.githubusercontent.com/13848158/154338753-34484cda-95b8-
-4da8-a610-7fdf198c05fd.png]
- About • Features • Demos • Examples • Quick_Start • Documentation • Roadmap •
-                          Discord_Community • Twitter
-[![Platform Support](https://img.shields.io/badge/platform-Linux%20%7C%20macOS-
-blue)]() [![PyPI - Python Version](https://img.shields.io/pypi/pyversions/aim)]
-(https://pypi.org/project/aim/) [![PyPI Package](https://img.shields.io/pypi/v/
-    aim?color=yellow)](https://pypi.org/project/aim/) [![License](https://
-img.shields.io/badge/License-Apache%202.0-orange.svg)](https://opensource.org/
-    licenses/Apache-2.0) [![PyPI Downloads](https://img.shields.io/pypi/dw/
-     aim?color=green)](https://pypi.org/project/aim/) [![Issues](https://
-  img.shields.io/github/issues/aimhubio/aim)](http://github.com/aimhubio/aim/
-                                    issues)
-                Integrates seamlessly with your favorite tools
-
- [https://user-images.githubusercontent.com/13848158/155354389-d0301620-77ea-
-    4629-a743-f7aa249e14b5.png] [https://user-images.githubusercontent.com/
-  13848158/155354496-b39d7b1c-63ef-40f0-9e59-c08d2c5e337c.png] [https://user-
-   images.githubusercontent.com/13848158/155354380-3755c741-6960-42ca-b93e-
-    84a8791f088c.png] [https://user-images.githubusercontent.com/13848158/
-      155354342-7df0ef5e-63d2-4df7-b9f1-d2fc0e95f53f.png] [https://user-
-   images.githubusercontent.com/13848158/155354392-afbff3de-c845-4d86-855d-
-    53df569f91d1.png] [https://user-images.githubusercontent.com/13848158/
-      155354355-89210506-e7e5-4d37-b2d6-ad3fda62ef13.png] [https://user-
-   images.githubusercontent.com/13848158/155354397-8af8e1d3-4067-405e-9d42-
-                              1f131663ed22.png]
- [https://user-images.githubusercontent.com/13848158/155354513-f7486146-3891-
-    4f3f-934f-e58bbf9ce695.png] [https://user-images.githubusercontent.com/
-  13848158/155354500-c0471ce6-b2ce-4172-b9e4-07a197256303.png] [https://user-
-   images.githubusercontent.com/13848158/155354361-9f911785-008d-4b75-877e-
-    651e026cf47e.png] [https://user-images.githubusercontent.com/13848158/
-      155354373-1879ae61-b5d1-41f0-a4f1-04b639b6f05e.png] [https://user-
-   images.githubusercontent.com/13848158/155354483-75d9853f-7154-4d95-8190-
-    9ad7a73d6654.png] [https://user-images.githubusercontent.com/13848158/
-      155354329-cf7c3352-a72a-478d-82a7-04e3833b03b7.png] [https://user-
-   images.githubusercontent.com/13848158/155354349-dcdf3bc3-d7a9-4f34-8258-
-    4824a57f59c7.png] [https://user-images.githubusercontent.com/13848158/
-      155354471-518f1814-7a41-4b23-9caf-e516507343f1.png] [https://user-
-   images.githubusercontent.com/48801049/165162736-2cc5da39-38aa-4093-874f-
-    e56d0ba9cea2.png] [https://user-images.githubusercontent.com/48801049/
-              165074282-36ad18eb-1124-434d-8439-728c22cd7ac7.png]
+           [![Discord Server](https://dcbadge.vercel.app/api/server/
+zXq2NfVdtF?compact=true&style=flat)](https://community.aimstack.io/) [![Twitter
+Follow](https://img.shields.io/twitter/follow/aimstackio?style=social)](https:/
+   /twitter.com/aimstackio) [![Medium](https://img.shields.io/badge/Medium-
+12100E?style=flat&logo=medium&logoColor=white)](https://medium.com/aimstack) [!
+ [Platform Support](https://img.shields.io/badge/platform-Linux%20%7C%20macOS-
+    blue)]() [![PyPI - Python Version](https://img.shields.io/badge/python-
+ %3E%3D%203.7-blue)](https://pypi.org/project/aim/) [![PyPI Package](https://
+  img.shields.io/pypi/v/aim?color=yellow)](https://pypi.org/project/aim/) [!
+[License](https://img.shields.io/badge/License-Apache%202.0-orange.svg)](https:
+       //opensource.org/licenses/Apache-2.0) [![PyPI Downloads](https://
+  img.shields.io/pypi/dw/aim?color=green)](https://pypi.org/project/aim/) [!
+[Issues](https://img.shields.io/github/issues/aimhubio/aim)](http://github.com/
+                             aimhubio/aim/issues)
 
  [https://user-images.githubusercontent.com/13848158/136374529-af267918-5dc6-
                           4a4e-8ed2-f6333a332f96.gif]
-# About Aim | Track and version ML runs | Visualize runs via beautiful UI |
-Query runs metadata via SDK | |:--------------------:|:-----------------------
--:|:-------------------:| | [https://user-images.githubusercontent.com/
-13848158/154337794-e9310239-6614-41b3-a95b-bb91f0bb6c4f.png] | [https://user-
-images.githubusercontent.com/13848158/154337788-03fe5b31-0fa3-44af-ae79-
-2861707d8602.png] | [https://user-images.githubusercontent.com/13848158/
-154337793-85175c78-5659-4dd0-bb2d-05017278e2fa.png] | Aim is an open-source,
-self-hosted ML experiment tracking tool. It's good at tracking lots (1000s) of
-training runs and it allows you to compare them with a performant and beautiful
-UI. You can use not only the great Aim UI but also its SDK to query your runs'
-metadata programmatically. That's especially useful for automations and
-additional analysis on a Jupyter Notebook. Aim's mission is to democratize AI
-dev tools. # Why use Aim? ### Compare 100s of runs in a few clicks - build
-models faster - Compare, group and aggregate 100s of metrics thanks to
-effective visualizations. - Analyze, learn correlations and patterns between
-hparams and metrics. - Easy pythonic search to query the runs you want to
-explore. ### Deep dive into details of each run for easy debugging -
-Hyperparameters, metrics, images, distributions, audio, text - all available at
-hand on an intuitive UI to understand the performance of your model. - Easily
-track plots built via your favourite visualisation tools, like plotly and
-matplotlib. - Analyze system resource usage to effectively utilize
-computational resources. ### Have all relevant information organised and
-accessible for easy governance - Centralized dashboard to holistically view all
-your runs, their hparams and results. - Use SDK to query/access all your runs
-and tracked metadata. - You own your data - Aim is open source and self hosted.
-# Demos | Machine translation | lightweight-GAN | |:---:|:---:| | [https://
-user-images.githubusercontent.com/13848158/154340796-c9e91b13-8ee0-4a67-bcde-
-8cf3aaa7ba99.jpg] | [https://user-images.githubusercontent.com/13848158/
-154340790-bc7b7a21-e8a1-43a1-809d-4060b5bfb60f.jpg] | | Training logs of a
-neural translation model(from WMT'19 competition). | Training logs of
-'lightweight' GAN, proposed in ICLR 2021. | | FastSpeech 2 | Simple MNIST | |:-
---:|:---:| | [https://user-images.githubusercontent.com/13848158/154340778-
-dbe19620-2f27-4298-b0cb-caf3904760f1.jpg] | [https://user-
-images.githubusercontent.com/13848158/154340785-a7e4d9fd-d048-4207-8cd1-
-c4edff9cca6a.jpg] | | Training logs of Microsoft's "FastSpeech 2: Fast and
-High-Quality End-to-End Text to Speech". | Simple MNIST training logs. | #
-Quick Start Follow the steps below to get started with Aim. **1. Install Aim on
-your training environment** ```shell pip3 install aim ``` **2. Integrate Aim
-with your code** ```python from aim import Run # Initialize a new run run = Run
-() # Log run parameters run["hparams"] = { "learning_rate": 0.001,
+                         SEAMLESSLY INTEGRATES WITH:
+
+ [https://user-images.githubusercontent.com/97726819/225954732-2b263308-8ed8-
+    4df3-810b-704840328e98.png] [https://user-images.githubusercontent.com/
+  97726819/225954727-04eccf0e-51ed-4f2d-8f3b-c9a675ca8e8f.png] [https://user-
+   images.githubusercontent.com/97726819/225954728-ca2f498d-51a7-487b-bd69-
+    ffb5f0c2af58.png] [https://user-images.githubusercontent.com/97726819/
+      225954689-1076998c-42f4-4e31-ab47-d9f39575fda1.png] [https://user-
+   images.githubusercontent.com/97726819/225954739-0231d659-3202-4458-9c35-
+    ba92d1f079b8.png] [https://user-images.githubusercontent.com/97726819/
+      225954697-ef2c7091-b089-4b68-8543-80ce7275b683.png] [https://user-
+   images.githubusercontent.com/97726819/225954743-dbfe1e98-7b9f-446a-9fe4-
+    ad4fd562f3df.png] [https://user-images.githubusercontent.com/97726819/
+      225954736-7c52ab5a-6780-4375-a6f8-b394dae3ad31.png] [https://user-
+   images.githubusercontent.com/97726819/225954710-36551a71-b26d-4665-af20-
+    44ee452dd5dd.png] [https://user-images.githubusercontent.com/97726819/
+      225954707-4bc078b5-ae6f-4847-bc2c-3f81959accb2.png] [https://user-
+   images.githubusercontent.com/97726819/225954725-a4d4c32c-75db-470a-b1da-
+    698982faa23c.png] [https://user-images.githubusercontent.com/97726819/
+      225954665-8d844747-a857-41b8-9104-7c27a8bdb81a.png] [https://user-
+   images.githubusercontent.com/97726819/225954686-b9c8ec57-d4fc-44e1-a4b8-
+    443db381a00f.png] [https://user-images.githubusercontent.com/97726819/
+      225954693-94bc20b4-f51a-4130-8d5f-ddee30d81205.png] [https://user-
+   images.githubusercontent.com/97726819/225954674-42fbfdb3-0351-492d-9ea3-
+    1d3ab2b545f5.png] [https://user-images.githubusercontent.com/97726819/
+      225954678-25f1b626-2cb1-4e7e-ad83-f7c8ab679c6f.png] [https://user-
+   images.githubusercontent.com/97726819/225954702-d18d2706-dc87-4e09-a678-
+                               f010f6d95736.png]
+
+                          TRUSTED BY ML TEAMS FROM:
+
+ [https://user-images.githubusercontent.com/97726819/225952594-a21546f4-987f-
+    42bd-9154-c22b50632b55.png] [https://user-images.githubusercontent.com/
+  97726819/225953224-291fbb6d-e31a-4e36-90ba-92a1dc20bacc.png] [https://user-
+   images.githubusercontent.com/97726819/225953339-4fcc3c99-dda2-4529-ac2a-
+    29c8293be323.png] [https://user-images.githubusercontent.com/97726819/
+      225953084-1d88325a-ad5f-49eb-aa67-f064c4b9f39c.png] [https://user-
+   images.githubusercontent.com/97726819/225952955-397e0f26-f01e-4b25-bd70-
+    9f292a6f77c2.png] [https://user-images.githubusercontent.com/97726819/
+      225952682-a843827b-e870-429d-96d8-3b4fd45471cd.png] [https://user-
+   images.githubusercontent.com/97726819/225952831-1c0e36aa-4120-4635-ab4e-
+    bf1bc685477b.png] [https://user-images.githubusercontent.com/97726819/
+              225953432-4b27653a-aa12-4fbf-897c-01349afa2ad0.png]
+
+    AimStack offers enterprise support that's beyond core Aim. Contact via
+                           hello@aimstack.io e-mail.
+---
+   **** About • Demos • Ecosystem • Quick_Start • Examples • Documentation •
+                             Community • Blog ****
+--- # â¹ï¸ About Aim is an open-source, self-hosted ML experiment tracking
+tool designed to handle 10,000s of training runs. Aim provides a performant and
+beautiful UI for exploring and comparing training runs. Additionally, its SDK
+enables programmatic access to tracked metadata â perfect for automations and
+Jupyter Notebook analysis.
+               Aim's mission is to democratize AI dev tools ð¯
+ [https://user-images.githubusercontent.com/13848158/226426018-f7c11c9b-78d9-
+    4ee4-b292-df28b3e8eaa6.jpg] [https://user-images.githubusercontent.com/
+  13848158/226426005-f7e83923-0f92-44a4-88e4-1735a3d3e119.jpg] [https://user-
+   images.githubusercontent.com/13848158/226426015-4f1122d8-c96a-443f-8698-
+                               3db942b1972a.jpg]
+Log Metadata Across Your ML Pipeline  Visualize & Compare Metadata via UI ð
+ð¾
+    * ML experiments and any metadata
+      tracking                            * Metadata visualization via Aim
+    * Integration with popular ML           Explorers
+      frameworks                          * Grouping and aggregation
+    * Easy migration from other           * Querying using Python expressions
+      experiment trackers
+Run ML Trainings Effectively â¡   Organize Your Experiments ðï¸
+    * System info and resource usage      * Detailed run information for easy
+      tracking                              debugging
+    * Real-time alerting on training      * Centralized dashboard for holistic
+      progress                              view
+    * Logging and configurable            * Runs grouping with tags and
+      notifications                         experiments
+# ð¬ Demos Check out live Aim demos NOW to see it in action. | [Machine
+translation experiments](http://play.aimstack.io:10001/
+metrics?grouping=HQGdK9Xxy35e6sY1CYkCmk1WbWMN2AsCNfJJ3d1RJYLtrVPMoF5UpGiA6CF8bEJnfzRsKpqespf3AEuKSVrhUYvYk9MxzNGA9XZWYUf6phEg8AMbZGLRVDXnAPDuo8tueqsST1ZLizWzQwDYJWHUza6pyB2Eojt9uWqNHUdb858TqDRnCJzqiVJXKXEzFWUyvU8MckJo1qpqWWCTb4GpYN6DUJZx2GXDGR21e2xxd4m7PmNUnbA9B3apLttZoipJF6c3v7tNUKmb6irpqnNB3yc57tqYDa1XZuKfDxkMtyFdQ1x95K4jjsTVwhftEWLze35QNcxNXRCGGS9o9yEfTLG26GUX2zjPZFCjjMGU6vV7z1xRccK8MyoGrLSgAQCbvk68dTGBHpXUBvCRq8N&chart=FviZzVrt4fVQPjpCLr9sVGGrcR5etSroyqambiKpm3nTgpyv4eQxKuwNX9uN8UtKmzYUhUyTMBEANHmtbwjLApkvnYeNbxGNC6PVcoqi65m1XJnSrvgt8WiD89BapFAWRUwAGx6SWD7KZPsk3RQyysU7W7FjD3Q99NusxFGhsEfD6HXc7i8xH9KHDRGjLwh6x9VTtSp4FS8HEvpLSiiJoX7LCTi8pB7dXvrQ8G5w3jPsFz4qXYFdsVaCNL1BpFFZuiqQNkfbnM84gEq7UmiV1VzM4oS3AgQHxADG3kpBVp6eKTey9F1Swd4FcUkFA9QEPjgQgqwRGjkquZ2bdDDVLBnCh7JPvboP2kifCiZZ5MDdV9MMx6PKHp4DusWyWLXiHQYPkpGPWBiuccMUXDsuJaCWJbuABdY7CyiJMv1jdHYkjabygSxehPVyEDefWAtjBfv2vaeM1xv63jadbmpKYFxft7qmuT9HvVxiGvRgs4RQFxy8K4rtFBca3HNs1mDaaY81gy9MGXyw7BS5Fniu92jaJpsWDdg6Y3AQBLZtrpJy2obEZ4yzJaCVT7JUNPAyyCUNLck393VFLoEkaD9CU5npK5R7tj1c1G3gkMNQXnSXy5NpSj8deMmXV5qz3JKu1nq2caGQKcqjzy2gLkExdm674AMFjSg9yFjK6VqASXQ17NKtWRUvaYoxGbHDAFQaMKWKh8QLm22QA9mKT8NksLptWozbgDvafnQLNMvezLU5bvKV5o75PAWYiRB56RcYfEhzaB6YWdgL7TJicyY5rFi6Az8UZ7wqB3N5iMuZdpxhKn5KbZDxyuUMuvVt24i5LVPPmmwQtqxMoJ4aLo48a2YvDW6TAkdQjNjvn6KcEEz6GTixujb1YHhMUD8v4AepWKEwKz1ddEca1P2wLQjbpihCuaqbxeohnuZZLogJdUBojBEDgrnrrVpPBaLLEkGSpkJbtrsKUuEeBo1AF3yNgHftLbynGpobVF5DhmsmddmiA6c8vSTokJxHhjpnW8mAcNHBRtmVJCT7VkdHSAhNypM4Hivwfx5jCccG9LauKmCeRMDzHiA57TX9W6ttcPHSvUyQorARQAd2oeNY4H83hZjHh9Bt8iwKZRt4xK6hrTR8tif7hq8eURXrGH9Ys7TzykXK8FHHWvLNzNnYf3E4a9NkD43MjfKvMM1hj4Q2K8MHbmRCqrmFrHP5kim9shq6mhLPTgwha32nvnrBkfPQVPwpGTzKuwE&select=CdsQ7jVNkogQhRzQR3e28Ek39AZ4Ma2y37k5zJaf9EZmQhMjy8GtGm4LGU6dRFuAVG7mYww5xDrQAE74KHQ3Kk1e6661RmcmNALAUjtHyCmrTVBMCnBGNiuq1y7EzmxoodYHU1BV1rnoefQAw2kTBtbWi11hV1P4LcwFCcXfUWF6rpRC7ehEnUCTqUV4bkGVJPLcmk9mdmiGwa2YgmnSShNGPVGZiEi1rMVECyngSRVdqdZwAeXBGWFLfqF1KbZeCo4MTF4SSmFupJ9zLhYbuojEbopyFWHQ6xs3sq9epPeaQziLM4Js7oFYRmuFWUYdFqnZngmewXWmi7tQAgVqhiT6dMjG2eTdfgX6WuRSuoHALkh2XJhHA6GfZLUcxC5Ni9YyKuBTamtaYarbNNJJ8z15WWvuUkLpjgHdEpE2h924xFdu8aoZNuiQxYGvcndaW1BTGMXS5fTKPqYfe2n8Ky2HWPkcX3hEXtyawu1F9BndKNaXLPgsdAoFBArBZnSe28YtSmTa5LRucKVBAxakvv5MWMXchAmpaGFQbZyYUoMgQLcJd7Y96x6zSR7nhwr5Ar81BrmqYz2WFLuk7osUbwsc9HbSG6CQt8p6Vg2u7DjKaZXW8pjkPHAKrHWtHEDiJPJ5rj6VsdFm3)
+| [lightweight-GAN experiments](http://play.aimstack.io:10002/
+images?grouping=E1zQzcmtDR3wibEa1MVysTvCyZEv1T8ixkCxTWExCyMnHtX2HyiF9eszvPgfd2xdJ5TUTKGpSs1bsLVq5tHAV3uWtsZmmckn6HjNtVCMyQDJpwhiEy5tAyw&select=2NEXuD7fFoaLcwRjymjA1wLmUrGs9s3AiXcCW82C367SwJt18CAB6xzkMGowrUDuDwggE1huaPVcQJpQUsmAQx1CnGiqCUBp2jPMd5mMNPX2QKQMcmvu9ZykBNkeBvCQFPd9ERuQD2g1EjWuvyJ3H53mAZTfp94LCXvR9CUsG5ei2CjQUzfZLM6DCyUr1GPaEVnY5f1EwzicNxXuoutkBgqCqaobJ7Do4q4eHAA6ooiWU6ekS3D2sLj6qYwhVTjfGCPfbWwBiH83nFkY3fLExzdeTY2zeUHeeYikQR9S7xHbVD8WvjekdQVp8X4dNLJZxiVmEqHpPRnU3ZrYsMhE7yFAAgjJwPNUzLTt6YFrtZBcmc4rwAC2oyrqysUSEr6gzL6LcJ6yuqDGf9D5tzftHbTLDkhc8B2sCgTS&images=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)|
+|:---:|:---:| | [https://user-images.githubusercontent.com/97726819/225964524-
+0051c2c7-8554-43ae-82b8-adcb77bcf1ba.png] | [https://user-
+images.githubusercontent.com/97726819/225948275-a41946ea-89f4-45f1-bce1-
+251c84dcddca.png] | | Training logs of a neural translation model(from WMT'19
+competition). | Training logs of 'lightweight' GAN, proposed in ICLR 2021. | |
+[FastSpeech 2 experiments](http://play.aimstack.io:10004/runs/
+d9e89aa7875e44b2ba85612a/audios)| [Simple MNIST](http://play.aimstack.io:10003/
+runs/7f083da898624a2c98e0f363/distributions) | |:---:|:---:| | [https://user-
+images.githubusercontent.com/97726819/225948457-567526da-a329-4c53-a9a7-
+98dfe392d4c4.png] | [https://user-images.githubusercontent.com/97726819/
+225948599-ff39c5b7-ae7d-4deb-8bc9-5eee1e189d89.png] | | Training logs of
+Microsoft's "FastSpeech 2: Fast and High-Quality End-to-End Text to Speech". |
+Simple MNIST training logs. | # ð Ecosystem Aim is not just an experiment
+tracker. It's a groundwork for an ecosystem. Check out the two most famous Aim-
+based tools. | [aimlflow](https://github.com/aimhubio/aimlflow) | [Aim-spaCy]
+(https://github.com/aimhubio/aim-spacy) | |:---:|:---:| | ![aimlflow](https://
+user-images.githubusercontent.com/97726819/225957836-cdec88e3-4993-435a-a135-
+d78be3ac1635.png) | ![Aim-spaCy](https://user-images.githubusercontent.com/
+97726819/225957990-4edc4525-1f65-4405-b663-ce7af888bdfa.png) | | Exploring
+MLflow experiments with a powerful UI | an Aim-based spaCy experiment tracker |
+# ð Quick start Follow the steps below to get started with Aim. ## 1.
+Install Aim on your training environment ```shell pip3 install aim ``` ## 2.
+Integrate Aim with your code ```python from aim import Run # Initialize a new
+run run = Run() # Log run parameters run["hparams"] = { "learning_rate": 0.001,
 "batch_size": 32, } # Log metrics for i in range(10): run.track(i, name='loss',
 step=i, context={ "subset":"train" }) run.track(i, name='acc', step=i, context=
 { "subset":"train" }) ``` _See the full list of supported trackable objects
 (e.g. images, text, etc) [here](https://aimstack.readthedocs.io/en/latest/
-quick_start/supported_types.html)._ **3. Run the training as usual and start
-Aim UI** ```shell aim up ``` **4. Or query runs programmatically via SDK**
-```python from aim import Repo my_repo = Repo('/path/to/aim/repo') query =
-"metric.name == 'loss'" # Example query # Get collection of metrics for
-run_metrics_collection in my_repo.query_metrics(query).iter_runs(): for metric
-in run_metrics_collection: # Get run params params = metric.run[...] # Get
-metric values steps, metric_values = metric.values.sparse_numpy() ``` #
-Integrations   Integrate PyTorch Lightning  ```python from
-aim.pytorch_lightning import AimLogger # ... trainer = pl.Trainer
-(logger=AimLogger(experiment='experiment_name')) # ... ``` _See documentation
-[here](https://aimstack.readthedocs.io/en/latest/quick_start/
-integrations.html#integration-with-pytorch-lightning)._    Integrate Hugging
-Face  ```python from aim.hugging_face import AimCallback # ... aim_callback =
-AimCallback(repo='/path/to/logs/dir', experiment='mnli') trainer = Trainer
-( model=model, args=training_args, train_dataset=train_dataset if
-training_args.do_train else None, eval_dataset=eval_dataset if
-training_args.do_eval else None, callbacks=[aim_callback], # ... ) # ... ```
-_See documentation [here](https://aimstack.readthedocs.io/en/latest/
-quick_start/integrations.html#integration-with-hugging-face)._    Integrate
-Keras & tf.keras  ```python import aim # ... model.fit(x_train, y_train,
-epochs=epochs, callbacks=[ aim.keras.AimCallback(repo='/path/to/logs/dir',
-experiment='experiment_name') # Use aim.tensorflow.AimCallback in case of
-tf.keras aim.tensorflow.AimCallback(repo='/path/to/logs/dir',
-experiment='experiment_name') ]) # ... ``` _See documentation [here](https://
-aimstack.readthedocs.io/en/latest/quick_start/integrations.html#integration-
-with-keras-tf-keras)._    Integrate KerasTuner  ```python from aim.keras_tuner
-import AimCallback # ... tuner.search( train_ds, validation_data=test_ds,
-callbacks=[AimCallback(tuner=tuner, repo='.', experiment='keras_tuner_test')],
-) # ... ``` _See documentation [here](https://aimstack.readthedocs.io/en/
-latest/quick_start/integrations.html#integration-with-kerastuner)._
-Integrate XGBoost  ```python from aim.xgboost import AimCallback # ...
-aim_callback = AimCallback(repo='/path/to/logs/dir',
-experiment='experiment_name') bst = xgb.train(param, xg_train, num_round,
-watchlist, callbacks=[aim_callback]) # ... ``` _See documentation [here](https:
+quick_start/supported_types.html)._ ## 3. Run the training as usual and start
+Aim UI ```shell aim up ``` ## Learn more   Migrate from other tools   Aim has
+built-in converters to easily migrate logs from other tools. These migrations
+cover the most common usage scenarios. In case of custom and complex scenarios
+you can use Aim SDK to implement your own conversion script. - [TensorBoard
+logs converter](https://aimstack.readthedocs.io/en/latest/quick_start/
+convert_data.html#show-tensorboard-logs-in-aim) - [MLFlow logs converter]
+(https://aimstack.readthedocs.io/en/latest/quick_start/convert_data.html#show-
+mlflow-logs-in-aim) - [Weights & Biases logs converter](https://
+aimstack.readthedocs.io/en/latest/quick_start/convert_data.html#show-weights-
+and-biases-logs-in-aim)    Integrate Aim into an existing project   Aim easily
+integrates with a wide range of ML frameworks, providing built-in callbacks for
+most of them. - [Integration with Pytorch Ignite](https://
+aimstack.readthedocs.io/en/latest/quick_start/integrations.html#integration-
+with-pytorch-ignite) - [Integration with Pytorch Lightning](https://
+aimstack.readthedocs.io/en/latest/quick_start/integrations.html#integration-
+with-pytorch-lightning) - [Integration with Hugging Face](https://
+aimstack.readthedocs.io/en/latest/quick_start/integrations.html#integration-
+with-hugging-face) - [Integration with Keras & tf.Keras](https://
+aimstack.readthedocs.io/en/latest/quick_start/integrations.html#integration-
+with-keras-tf-keras) - [Integration with Keras Tuner](https://
+aimstack.readthedocs.io/en/latest/quick_start/integrations.html#integration-
+with-keras-tuner) - [Integration with XGboost](https://aimstack.readthedocs.io/
+en/latest/quick_start/integrations.html#integration-with-xgboost) -
+[Integration with CatBoost](https://aimstack.readthedocs.io/en/latest/
+quick_start/integrations.html#integration-with-catboost) - [Integration with
+LightGBM](https://aimstack.readthedocs.io/en/latest/quick_start/
+integrations.html#integration-with-lightgbm) - [Integration with fastai](https:
 //aimstack.readthedocs.io/en/latest/quick_start/integrations.html#integration-
-with-xgboost)._    Integrate CatBoost  ```python from aim.catboost import
-AimLogger # ... model.fit(train_data, train_labels, log_cout=AimLogger
-(loss_function='Logloss'), logging_level="Info") # ... ``` _See documentation
-[here](https://aimstack.readthedocs.io/en/latest/quick_start/
-integrations.html#integration-with-catboost)._    Integrate fastai  ```python
-from aim.fastai import AimCallback # ... learn = cnn_learner(dls, resnet18,
-pretrained=True, loss_func=CrossEntropyLossFlat(), metrics=accuracy,
-model_dir="/tmp/model/", cbs=AimCallback(repo='.', experiment='fastai_test')) #
-... ``` _See documentation [here](https://aimstack.readthedocs.io/en/latest/
-quick_start/integrations.html#integration-with-fastai)._    Integrate LightGBM
-```python from aim.lightgbm import AimCallback # ... aim_callback = AimCallback
-(experiment='lgb_test') aim_callback.experiment['hparams'] = params gbm =
-lgb.train(params, lgb_train, num_boost_round=20, valid_sets=lgb_eval,
-callbacks=[aim_callback, lgb.early_stopping(stopping_rounds=5)]) # ... ``` _See
-documentation [here](https://aimstack.readthedocs.io/en/latest/quick_start/
-integrations.html#integration-with-lightgbm)._    Integrate PyTorch Ignite
-```python from aim.pytorch_ignite import AimLogger # ... aim_logger = AimLogger
-() aim_logger.log_params({ "model": model.__class__.__name__,
-"pytorch_version": str(torch.__version__), "ignite_version": str
-(ignite.__version__), }) aim_logger.attach_output_handler( trainer,
-event_name=Events.ITERATION_COMPLETED, tag="train", output_transform=lambda
-loss: {'loss': loss} ) # ... ``` _See documentation [here](https://
-aimstack.readthedocs.io/en/latest/quick_start/integrations.html#integration-
-with-pytorch-ignite)._  # Comparisons to familiar tools ### Tensorboard
-**Training run comparison** Order of magnitude faster training run comparison
-with Aim - The tracked params are first class citizens at Aim. You can search,
-group, aggregate via params - deeply explore all the tracked data (metrics,
-params, images) on the UI. - With tensorboard the users are forced to record
-those parameters in the training run name to be able to search and compare.
-This causes a super-tedius comparison experience and usability issues on the UI
-when there are many experiments and params. **TensorBoard doesn't have features
-to group, aggregate the metrics** **Scalability** - Aim is built to handle
-1000s of training runs - both on the backend and on the UI. - TensorBoard
-becomes really slow and hard to use when a few hundred training runs are
-queried / compared. **Beloved TB visualizations to be added on Aim** -
-Embedding projector. - Neural network visualization. ### MLFlow MLFlow is an
-end-to-end ML Lifecycle tool. Aim is focused on training tracking. The main
+with-fastai) - [Integration with MXNet](https://aimstack.readthedocs.io/en/
+latest/quick_start/integrations.html#integration-with-mxnet) - [Integration
+with Optuna](https://aimstack.readthedocs.io/en/latest/quick_start/
+integrations.html#integration-with-optuna) - [Integration with PaddlePaddle]
+(https://aimstack.readthedocs.io/en/latest/quick_start/
+integrations.html#integration-with-paddlepaddle) - [Integration with Stable-
+Baselines3](https://aimstack.readthedocs.io/en/latest/quick_start/
+integrations.html#integration-with-stable-baselines3) - [Integration with Acme]
+(https://aimstack.readthedocs.io/en/latest/quick_start/
+integrations.html#integration-with-acme) - [Integration with Prophet](https://
+aimstack.readthedocs.io/en/latest/quick_start/integrations.html#integration-
+with-prophet)    Query runs programmatically via SDK   Aim Python SDK empowers
+you to query and access any piece of tracked metadata with ease. ```python from
+aim import Repo my_repo = Repo('/path/to/aim/repo') query = "metric.name ==
+'loss'" # Example query # Get collection of metrics for run_metrics_collection
+in my_repo.query_metrics(query).iter_runs(): for metric in
+run_metrics_collection: # Get run params params = metric.run[...] # Get metric
+values steps, metric_values = metric.values.sparse_numpy() ```    Set up a
+centralized tracking server   Aim remote tracking server allows running
+experiments in a multi-host environment and collect tracked data in a
+centralized location. See the docs on how to [set up the remote server](https:/
+/aimstack.readthedocs.io/en/latest/using/remote_tracking.html).    Deploy Aim
+on kubernetes   - The official Aim docker image: https://hub.docker.com/r/
+aimstack/aim - A guide on how to deploy Aim on kubernetes: https://
+aimstack.readthedocs.io/en/latest/using/k8s_deployment.html  Read the full
+documentation on [aimstack.readthedocs.io](https://aimstack.readthedocs.io)
+ð # ð Comparisons to familiar tools   TensorBoard vs Aim   **Training run
+comparison** Order of magnitude faster training run comparison with Aim - The
+tracked params are first class citizens at Aim. You can search, group,
+aggregate via params - deeply explore all the tracked data (metrics, params,
+images) on the UI. - With tensorboard the users are forced to record those
+parameters in the training run name to be able to search and compare. This
+causes a super-tedius comparison experience and usability issues on the UI when
+there are many experiments and params. **TensorBoard doesn't have features to
+group, aggregate the metrics** **Scalability** - Aim is built to handle 1000s
+of training runs - both on the backend and on the UI. - TensorBoard becomes
+really slow and hard to use when a few hundred training runs are queried /
+compared. **Beloved TB visualizations to be added on Aim** - Embedding
+projector. - Neural network visualization.    MLflow vs Aim   MLFlow is an end-
+to-end ML Lifecycle tool. Aim is focused on training tracking. The main
 differences of Aim and MLflow are around the UI scalability and run comparison
-features. **Run comparison** - Aim treats tracked parameters as first-class
+features. Aim and MLflow are a perfect match - check out the [aimlflow](https:/
+/github.com/aimhubio/aimlflow) - the tool that enables Aim supoerpowers on
+Mlflow. **Run comparison** - Aim treats tracked parameters as first-class
 citizens. Users can query runs, metrics, images and filter using the params. -
 MLFlow does have a search by tracked config, but there are no grouping,
 aggregation, subplotting by hyparparams and other comparison features
 available. **UI Scalability** - Aim UI can handle several thousands of metrics
 at the same time smoothly with 1000s of steps. It may get shaky when you
 explore 1000s of metrics with 10000s of steps each. But we are constantly
 optimizing! - MLflow UI becomes slow to use when there are a few hundreds of
-runs. ### Weights and Biases Hosted vs self-hosted - Weights and Biases is a
-hosted closed-source MLOps platform. - Aim is self-hosted, free and open-source
-experiment tracking tool. # Roadmap ## Detailed Sprints :sparkle: The [Aim
-product roadmap](https://github.com/orgs/aimhubio/projects/3) - The `Backlog`
-contains the issues we are going to choose from and prioritize weekly - The
-issues are mainly prioritized by the highly-requested features ## High-level
-roadmap The high-level features we are going to work on the next few months ###
-Done - [x] Live updates (Shipped: _Oct 18 2021_) - [x] Images tracking and
-visualization (Start: _Oct 18 2021_, Shipped: _Nov 19 2021_) - [x]
-Distributions tracking and visualization (Start: _Nov 10 2021_, Shipped: _Dec 3
-2021_) - [x] Jupyter integration (Start: _Nov 18 2021_, Shipped: _Dec 3 2021_)
-- [x] Audio tracking and visualization (Start: _Dec 6 2021_, Shipped: _Dec 17
-2021_) - [x] Transcripts tracking and visualization (Start: _Dec 6 2021_,
-Shipped: _Dec 17 2021_) - [x] Plotly integration (Start: _Dec 1 2021_, Shipped:
-_Dec 17 2021_) - [x] Colab integration (Start: _Nov 18 2021_, Shipped: _Dec 17
-2021_) - [x] Centralized tracking server (Start: _Oct 18 2021_, Shipped: _Jan
-22 2022_) - [x] Tensorboard adaptor - visualize TensorBoard logs with Aim
-(Start: _Dec 17 2021_, Shipped: _Feb 3 2022_) - [x] Track git info, env vars,
-CLI arguments, dependencies (Start: _Jan 17 2022_, Shipped: _Feb 3 2022_) - [x]
-MLFlow adaptor (visualize MLflow logs with Aim) (Start: _Feb 14 2022_, Shipped:
-_Feb 22 2022_) - [x] Activeloop Hub integration (Start: _Feb 14 2022_, Shipped:
-_Feb 22 2022_) - [x] PyTorch-Ignite integration (Start: _Feb 14 2022_, Shipped:
-_Feb 22 2022_) - [x] Run summary and overview info(system params, CLI args, git
-info, ...) (Start: _Feb 14 2022_, Shipped: _Mar 9 2022_) - [x] Add DVC related
-metadata into aim run (Start: _Mar 7 2022_, Shipped: _Mar 26 2022_) - [x]
-Ability to attach notes to Run from UI (Start: _Mar 7 2022_, Shipped: _Apr 29
-2022_) - [x] Fairseq integration (Start: _Mar 27 2022_, Shipped: _Mar 29 2022_)
-- [x] LightGBM integration (Start: _Apr 14 2022_, Shipped: _May 17 2022_) - [x]
+runs.    Weights and Biases vs Aim   Hosted vs self-hosted - Weights and Biases
+is a hosted closed-source MLOps platform. - Aim is self-hosted, free and open-
+source experiment tracking tool.  # ð£ï¸ Roadmap ## Detailed milestones The
+[Aim product roadmap](https://github.com/orgs/aimhubio/projects/3) :sparkle: -
+The `Backlog` contains the issues we are going to choose from and prioritize
+weekly - The issues are mainly prioritized by the highly-requested features ##
+High-level roadmap The high-level features we are going to work on the next few
+months: **In progress** - [ ] Aim SDK low-level interface - [ ] Dashboards â
+customizable layouts with embedded explorers - [ ] Ergonomic UI kit - [ ] Text
+Explorer   Next-up   **Aim UI** - Runs management - Runs explorer â query and
+visualize runs data(images, audio, distributions, ...) in a central dashboard -
+Explorers - Distributions Explorer **SDK and Storage** - Scalability - Smooth
+UI and SDK experience with over 10.000 runs - Runs management - CLI commands -
+Reporting - runs summary and run details in a CLI compatible format -
+Manipulations â copy, move, delete runs, params and sequences - Cloud storage
+support â store runs blob(e.g. images) data on the cloud - Artifact storage
+â store files, model checkpoints, and beyond **Integrations** - ML
+Frameworks: - Shortlist: scikit-learn - Resource management tools - Shortlist:
+Kubeflow, Slurm - Workflow orchestration tools    Done   - [x] Live updates
+(Shipped: _Oct 18 2021_) - [x] Images tracking and visualization (Start: _Oct
+18 2021_, Shipped: _Nov 19 2021_) - [x] Distributions tracking and
+visualization (Start: _Nov 10 2021_, Shipped: _Dec 3 2021_) - [x] Jupyter
+integration (Start: _Nov 18 2021_, Shipped: _Dec 3 2021_) - [x] Audio tracking
+and visualization (Start: _Dec 6 2021_, Shipped: _Dec 17 2021_) - [x]
+Transcripts tracking and visualization (Start: _Dec 6 2021_, Shipped: _Dec 17
+2021_) - [x] Plotly integration (Start: _Dec 1 2021_, Shipped: _Dec 17 2021_) -
+[x] Colab integration (Start: _Nov 18 2021_, Shipped: _Dec 17 2021_) - [x]
+Centralized tracking server (Start: _Oct 18 2021_, Shipped: _Jan 22 2022_) -
+[x] Tensorboard adaptor - visualize TensorBoard logs with Aim (Start: _Dec 17
+2021_, Shipped: _Feb 3 2022_) - [x] Track git info, env vars, CLI arguments,
+dependencies (Start: _Jan 17 2022_, Shipped: _Feb 3 2022_) - [x] MLFlow adaptor
+(visualize MLflow logs with Aim) (Start: _Feb 14 2022_, Shipped: _Feb 22 2022_)
+- [x] Activeloop Hub integration (Start: _Feb 14 2022_, Shipped: _Feb 22 2022_)
+- [x] PyTorch-Ignite integration (Start: _Feb 14 2022_, Shipped: _Feb 22 2022_)
+- [x] Run summary and overview info(system params, CLI args, git info, ...)
+(Start: _Feb 14 2022_, Shipped: _Mar 9 2022_) - [x] Add DVC related metadata
+into aim run (Start: _Mar 7 2022_, Shipped: _Mar 26 2022_) - [x] Ability to
+attach notes to Run from UI (Start: _Mar 7 2022_, Shipped: _Apr 29 2022_) - [x]
+Fairseq integration (Start: _Mar 27 2022_, Shipped: _Mar 29 2022_) - [x]
+LightGBM integration (Start: _Apr 14 2022_, Shipped: _May 17 2022_) - [x]
 CatBoost integration (Start: _Apr 20 2022_, Shipped: _May 17 2022_) - [x] Run
 execution details(display stdout/stderr logs) (Start: _Apr 25 2022_, Shipped:
 _May 17 2022_) - [x] Long sequences(up to 5M of steps) support (Start: _Apr 25
 2022_, Shipped: _Jun 22 2022_) - [x] Figures Explorer (Start: _Mar 1 2022_,
 Shipped: _Aug 21 2022_) - [x] Notify on stuck runs (Start: _Jul 22 2022_,
 Shipped: _Aug 21 2022_) - [x] Integration with KerasTuner (Start: _Aug 10
 2022_, Shipped: _Aug 21 2022_) - [x] Integration with WandB (Start: _Aug 15
@@ -222,25 +273,26 @@
 22 2022_, Shipped: _Oct 6 2022_) - [x] Integration with MXNet (Start: _Sep 20
 2022_, Shipped: _Oct 6 2022_) - [x] Project overview page (Start: _Sep 1 2022_,
 Shipped: _Oct 6 2022_) - [x] Remote tracking server scaling (Start: _Sep 11
 2022_, Shipped: _Nov 26 2022_) - [x] Integration with PaddlePaddle (Start: _Oct
 2 2022_, Shipped: _Nov 26 2022_) - [x] Integration with Optuna (Start: _Oct 2
 2022_, Shipped: _Nov 26 2022_) - [x] Audios Explorer (Start: _Oct 30 2022_,
 Shipped: _Nov 26 2022_) - [x] Experiment page (Start: _Nov 9 2022_, Shipped:
-_Nov 26 2022_) ### In Progress - [ ] Aim SDK low-level interface (Start: _Aug
-22 2022_, ) - [ ] HuggingFace datasets (Start: _Dec 29 2022_, ) ### To Do **Aim
-UI** - Runs management - Runs explorer â query and visualize runs data
-(images, audio, distributions, ...) in a central dashboard - Explorers - Text
-Explorer - Distributions Explorer - Dashboards â customizable layouts with
-embedded explorers **SDK and Storage** - Scalability - Smooth UI and SDK
-experience with over 10.000 runs - Runs management - CLI interfaces - Reporting
-- runs summary and run details in a CLI compatible format - Manipulations â
-copy, move, delete runs, params and sequences **Integrations** - ML Frameworks:
-- Shortlist: MONAI, SpaCy, Raytune - Resource management tools - Shortlist:
-Kubeflow, Slurm - Workflow orchestration tools - Others: Hydra, Google MLMD,
-Streamlit, ... ### On hold - scikit-learn integration - Cloud storage support
-â store runs blob(e.g. images) data on the cloud (Start: _Mar 21 2022_) -
-Artifact storage â store files, model checkpoints, and beyond (Start: _Mar 21
-2022_) ## Community ### If you have questions 1. [Read the docs](https://
-aimstack.readthedocs.io/en/latest/) 2. [Open a feature request or report a bug]
-(https://github.com/aimhubio/aim/issues) 3. [Join Discord community server]
-(https://community.aimstack.io/)
+_Nov 26 2022_) - [x] HuggingFace datasets (Start: _Dec 29 2022_, _Feb 3 2023_)
+# ð¥ Community ## Aim README badge Add Aim badge to your README, if you've
+enjoyed using Aim in your work: [![Aim](https://img.shields.io/badge/
+powered%20by-Aim-%231473E6)](https://github.com/aimhubio/aim) ``` [![Aim]
+(https://img.shields.io/badge/powered%20by-Aim-%231473E6)](https://github.com/
+aimhubio/aim) ``` ## Cite Aim in your papers In case you've found Aim helpful
+in your research journey, we'd be thrilled if you could acknowledge Aim's
+contribution: ```bibtex @software{Arakelyan_Aim_2020, author = {Arakelyan, Gor
+and Soghomonyan, Gevorg and {The Aim team}}, doi = {10.5281/zenodo.6536395},
+license = {Apache-2.0}, month = {6}, title = {{Aim}}, url = {https://
+github.com/aimhubio/aim}, version = {3.9.3}, year = {2020} } ``` ##
+Contributing to Aim Considering contibuting to Aim? To get started, please take
+a moment to read the [CONTRIBUTING.md](https://github.com/aimhubio/aim/blob/
+main/CONTRIBUTING.md) guide. Join Aim contributors by submitting your first
+pull request. Happy coding! ð [https://contrib.rocks/image?repo=aimhubio/
+aim] Made with [contrib.rocks](https://contrib.rocks). ## More questions? 1.
+[Read the docs](https://aimstack.readthedocs.io/en/latest/) 2. [Open a feature
+request or report a bug](https://github.com/aimhubio/aim/issues) 3. [Join
+Discord community server](https://community.aimstack.io/)
```

### Comparing `aim-4.0.0.dev1/README.md` & `aim-4.0.0.dev2/README.md`

 * *Files 26% similar despite different names*

```diff
@@ -1,129 +1,215 @@
 <div align="center">
-  <img src="https://user-images.githubusercontent.com/13848158/154338760-edfe1885-06f3-4e02-87fe-4b13a403516b.png">
-  <h3>An easy-to-use & supercharged open-source experiment tracker</h3>
-  Aim logs your training runs, enables a beautiful UI to compare them and an API to query them programmatically.
+  <table>
+    <tbody>
+      <tr>
+        <td>Drop a star to support Aim ⭐</td>
+        <td>
+          <a href="https://community.aimstack.io/">Join Aim discord community</a>
+          <img width="20px" src="https://user-images.githubusercontent.com/13848158/226759622-063b725d-8b3e-4c75-80c7-11fb04b7adf5.png">
+        </td>
+      </tr>
+    </tbody>
+  </table>
 </div>
 
-<br/>
-
-<img src="https://user-images.githubusercontent.com/13848158/154338753-34484cda-95b8-4da8-a610-7fdf198c05fd.png">
+<div align="center">
+  <img src="https://user-images.githubusercontent.com/13848158/225620298-9f9293e9-a138-41fd-bd77-21d53d0490b7.png">
+  <h3>
+    An easy-to-use & supercharged open-source experiment tracker
+  </h3>
+  Aim logs your training runs and any AI Metadata, enables a beautiful UI to compare, observe them and an API to query them programmatically.
+</div>
 
-<p align="center">
-  <a href="#about-aim"><b>About</b></a> &bull;
-  <a href="#why-use-aim"><b>Features</b></a> &bull;
-  <a href="#demos"><b>Demos</b></a> &bull;
-  <a href="https://github.com/aimhubio/aim/tree/main/examples"><b>Examples</b></a> &bull;
-  <a href="#quick-start"><b>Quick Start</b></a> &bull;
-  <a href="https://aimstack.readthedocs.io/en/latest/"><b>Documentation</b></a> &bull;
-  <a href="#roadmap"><b>Roadmap</b></a> &bull;
-  <a href="https://community.aimstack.io/"><b>Discord Community</b></a> &bull;
-  <a href="https://twitter.com/aimstackio"><b>Twitter</b></a>
-</p>
+<br/>
 
 <div align="center">
   
+  [![Discord Server](https://dcbadge.vercel.app/api/server/zXq2NfVdtF?compact=true&style=flat)](https://community.aimstack.io/)
+  [![Twitter Follow](https://img.shields.io/twitter/follow/aimstackio?style=social)](https://twitter.com/aimstackio)
+  [![Medium](https://img.shields.io/badge/Medium-12100E?style=flat&logo=medium&logoColor=white)](https://medium.com/aimstack)
+  
   [![Platform Support](https://img.shields.io/badge/platform-Linux%20%7C%20macOS-blue)]()
-  [![PyPI - Python Version](https://img.shields.io/pypi/pyversions/aim)](https://pypi.org/project/aim/)
+  [![PyPI - Python Version](https://img.shields.io/badge/python-%3E%3D%203.7-blue)](https://pypi.org/project/aim/)
   [![PyPI Package](https://img.shields.io/pypi/v/aim?color=yellow)](https://pypi.org/project/aim/)
   [![License](https://img.shields.io/badge/License-Apache%202.0-orange.svg)](https://opensource.org/licenses/Apache-2.0)
   [![PyPI Downloads](https://img.shields.io/pypi/dw/aim?color=green)](https://pypi.org/project/aim/)
   [![Issues](https://img.shields.io/github/issues/aimhubio/aim)](http://github.com/aimhubio/aim/issues)
   
 </div>
 
 <div align="center">
-  <sub>Integrates seamlessly with your favorite tools</sub>
   <br/>
+  <kbd>
+    <img src="https://user-images.githubusercontent.com/13848158/136374529-af267918-5dc6-4a4e-8ed2-f6333a332f96.gif" />
+  </kbd>
+</div>
+
+</br>
+
+<div align="center">
+  <sub><strong>SEAMLESSLY INTEGRATES WITH:</strong></sub>
   <br/>
-  <img src="https://user-images.githubusercontent.com/13848158/155354389-d0301620-77ea-4629-a743-f7aa249e14b5.png" width="60" />
-  <img src="https://user-images.githubusercontent.com/13848158/155354496-b39d7b1c-63ef-40f0-9e59-c08d2c5e337c.png" width="60" />
-  <img src="https://user-images.githubusercontent.com/13848158/155354380-3755c741-6960-42ca-b93e-84a8791f088c.png" width="60" />
-  <img src="https://user-images.githubusercontent.com/13848158/155354342-7df0ef5e-63d2-4df7-b9f1-d2fc0e95f53f.png" width="60" />
-  <img src="https://user-images.githubusercontent.com/13848158/155354392-afbff3de-c845-4d86-855d-53df569f91d1.png" width="60" />
-  <img src="https://user-images.githubusercontent.com/13848158/155354355-89210506-e7e5-4d37-b2d6-ad3fda62ef13.png" width="60" />
-  <img src="https://user-images.githubusercontent.com/13848158/155354397-8af8e1d3-4067-405e-9d42-1f131663ed22.png" width="60" />
   <br/>
-  <img src="https://user-images.githubusercontent.com/13848158/155354513-f7486146-3891-4f3f-934f-e58bbf9ce695.png" width="60" />
-  <img src="https://user-images.githubusercontent.com/13848158/155354500-c0471ce6-b2ce-4172-b9e4-07a197256303.png" width="60" />
-  <img src="https://user-images.githubusercontent.com/13848158/155354361-9f911785-008d-4b75-877e-651e026cf47e.png" width="60" />
-  <img src="https://user-images.githubusercontent.com/13848158/155354373-1879ae61-b5d1-41f0-a4f1-04b639b6f05e.png" width="60" />
-  <img src="https://user-images.githubusercontent.com/13848158/155354483-75d9853f-7154-4d95-8190-9ad7a73d6654.png" width="60" />
-  <img src="https://user-images.githubusercontent.com/13848158/155354329-cf7c3352-a72a-478d-82a7-04e3833b03b7.png" width="60" />
-  <img src="https://user-images.githubusercontent.com/13848158/155354349-dcdf3bc3-d7a9-4f34-8258-4824a57f59c7.png" width="60" />
-  <img src="https://user-images.githubusercontent.com/13848158/155354471-518f1814-7a41-4b23-9caf-e516507343f1.png" width="60" />
-  <img src="https://user-images.githubusercontent.com/48801049/165162736-2cc5da39-38aa-4093-874f-e56d0ba9cea2.png" width="60" />
-  <img src="https://user-images.githubusercontent.com/48801049/165074282-36ad18eb-1124-434d-8439-728c22cd7ac7.png" width="60" />
+  <img src="https://user-images.githubusercontent.com/97726819/225954732-2b263308-8ed8-4df3-810b-704840328e98.png" height="60" />
+  <img src="https://user-images.githubusercontent.com/97726819/225954727-04eccf0e-51ed-4f2d-8f3b-c9a675ca8e8f.png" height="60" />
+  <img src="https://user-images.githubusercontent.com/97726819/225954728-ca2f498d-51a7-487b-bd69-ffb5f0c2af58.png" height="60" />
+  <img src="https://user-images.githubusercontent.com/97726819/225954689-1076998c-42f4-4e31-ab47-d9f39575fda1.png" height="60" />
+  <img src="https://user-images.githubusercontent.com/97726819/225954739-0231d659-3202-4458-9c35-ba92d1f079b8.png" height="60" />
+  <img src="https://user-images.githubusercontent.com/97726819/225954697-ef2c7091-b089-4b68-8543-80ce7275b683.png" height="60" />
+  <img src="https://user-images.githubusercontent.com/97726819/225954743-dbfe1e98-7b9f-446a-9fe4-ad4fd562f3df.png" height="60" />
+  <img src="https://user-images.githubusercontent.com/97726819/225954736-7c52ab5a-6780-4375-a6f8-b394dae3ad31.png" height="60" />
+  <img src="https://user-images.githubusercontent.com/97726819/225954710-36551a71-b26d-4665-af20-44ee452dd5dd.png" height="60" />
+  <img src="https://user-images.githubusercontent.com/97726819/225954707-4bc078b5-ae6f-4847-bc2c-3f81959accb2.png" height="60" />
+  <img src="https://user-images.githubusercontent.com/97726819/225954725-a4d4c32c-75db-470a-b1da-698982faa23c.png" height="60" />
+  <img src="https://user-images.githubusercontent.com/97726819/225954665-8d844747-a857-41b8-9104-7c27a8bdb81a.png" height="60" />
+  <img src="https://user-images.githubusercontent.com/97726819/225954686-b9c8ec57-d4fc-44e1-a4b8-443db381a00f.png" height="60" />
+  <img src="https://user-images.githubusercontent.com/97726819/225954693-94bc20b4-f51a-4130-8d5f-ddee30d81205.png" height="60" />
+  <img src="https://user-images.githubusercontent.com/97726819/225954674-42fbfdb3-0351-492d-9ea3-1d3ab2b545f5.png" height="60" />
+  <img src="https://user-images.githubusercontent.com/97726819/225954678-25f1b626-2cb1-4e7e-ad83-f7c8ab679c6f.png" height="60" />
+  <img src="https://user-images.githubusercontent.com/97726819/225954702-d18d2706-dc87-4e09-a678-f010f6d95736.png" height="60" />
 </div>
 
+<br/>
+
 <div align="center">
+  <sub><strong>TRUSTED BY ML TEAMS FROM:</strong></sub>  
   <br/>
-  <kbd>
-    <img src="https://user-images.githubusercontent.com/13848158/136374529-af267918-5dc6-4a4e-8ed2-f6333a332f96.gif" />
-  </kbd>
+  <br/>
+  <img src="https://user-images.githubusercontent.com/97726819/225952594-a21546f4-987f-42bd-9154-c22b50632b55.png" height="55" />
+  <img src="https://user-images.githubusercontent.com/97726819/225953224-291fbb6d-e31a-4e36-90ba-92a1dc20bacc.png" height="55" />
+  <img src="https://user-images.githubusercontent.com/97726819/225953339-4fcc3c99-dda2-4529-ac2a-29c8293be323.png" height="55" />
+  <img src="https://user-images.githubusercontent.com/97726819/225953084-1d88325a-ad5f-49eb-aa67-f064c4b9f39c.png" height="55" />
+  <img src="https://user-images.githubusercontent.com/97726819/225952955-397e0f26-f01e-4b25-bd70-9f292a6f77c2.png" height="55" />
+  <img src="https://user-images.githubusercontent.com/97726819/225952682-a843827b-e870-429d-96d8-3b4fd45471cd.png" height="55" />
+  <img src="https://user-images.githubusercontent.com/97726819/225952831-1c0e36aa-4120-4635-ab4e-bf1bc685477b.png" height="55" />
+  <img src="https://user-images.githubusercontent.com/97726819/225953432-4b27653a-aa12-4fbf-897c-01349afa2ad0.png" height="55" />
 </div>
 
-# About Aim
+<br/>
 
-| Track and version ML runs | Visualize runs via beautiful UI | Query runs metadata via SDK |
-|:--------------------:|:------------------------:|:-------------------:|
-| <img width="600px" src="https://user-images.githubusercontent.com/13848158/154337794-e9310239-6614-41b3-a95b-bb91f0bb6c4f.png"> | <img width="600px" src="https://user-images.githubusercontent.com/13848158/154337788-03fe5b31-0fa3-44af-ae79-2861707d8602.png"> | <img width="600px" src="https://user-images.githubusercontent.com/13848158/154337793-85175c78-5659-4dd0-bb2d-05017278e2fa.png"> |
+<p align="center">
+  AimStack offers enterprise support that's beyond core Aim. Contact via <a href="mailto:hello@aimstack.io">hello@aimstack.io</a> e-mail.
+</p>
 
-Aim is an open-source, self-hosted ML experiment tracking tool. 
-It's good at tracking lots (1000s) of training runs and it allows you to compare them with a performant and beautiful UI.
+---
 
-You can use not only the great Aim UI but also its SDK to query your runs' metadata programmatically. 
-That's especially useful for automations and additional analysis on a Jupyter Notebook.
+<h3 align="center">
+  <a href="#-about"><b>About</b></a> &bull;
+  <a href="#-demos"><b>Demos</b></a> &bull;
+  <a href="#-ecosystem"><b>Ecosystem</b></a> &bull;
+  <a href="#-quick-start"><b>Quick Start</b></a> &bull;
+  <a href="https://github.com/aimhubio/aim/tree/main/examples"><b>Examples</b></a> &bull;
+  <a href="https://aimstack.readthedocs.io/en/latest/"><b>Documentation</b></a> &bull;
+  <a href="#-community"><b>Community</b></a> &bull;
+  <a href="https://aimstack.io/blog"><b>Blog</b></a>
+</h3>  
 
+---
 
-Aim's mission is to democratize AI dev tools.
+# ℹ️ About
 
-# Why use Aim?
+Aim is an open-source, self-hosted ML experiment tracking tool designed to handle 10,000s of training runs.
 
-### Compare 100s of runs in a few clicks - build models faster
+Aim provides a performant and beautiful UI for exploring and comparing training runs.
+Additionally, its SDK enables programmatic access to tracked metadata — perfect for automations and Jupyter Notebook analysis.
 
-- Compare, group and aggregate 100s of metrics thanks to effective visualizations.
-- Analyze, learn correlations and patterns between hparams and metrics.
-- Easy pythonic search to query the runs you want to explore.
+<p align="center">
+  <strong>Aim's mission is to democratize AI dev tools 🎯 </strong>
+</p>
 
-### Deep dive into details of each run for easy debugging
+<div align="center">
+  <img src="https://user-images.githubusercontent.com/13848158/226426018-f7c11c9b-78d9-4ee4-b292-df28b3e8eaa6.jpg" height="140" />
+  <img src="https://user-images.githubusercontent.com/13848158/226426005-f7e83923-0f92-44a4-88e4-1735a3d3e119.jpg" height="140" />
+  <img src="https://user-images.githubusercontent.com/13848158/226426015-4f1122d8-c96a-443f-8698-3db942b1972a.jpg" height="140" />
+</div>
 
-- Hyperparameters, metrics, images, distributions, audio, text - all available at hand on an intuitive UI to understand the performance of your model.
-- Easily track plots built via your favourite visualisation tools, like plotly and matplotlib.
-- Analyze system resource usage to effectively utilize computational resources.
+</br>
 
-### Have all relevant information organised and accessible for easy governance
+<div align="center">
+  <table>
+    <tbody>
+      <tr>
+        <th>Log Metadata Across Your ML Pipeline 💾</th>
+        <th>Visualize & Compare Metadata via UI 📊</th>
+      </tr>
+      <tr>
+        <td>
+          <ul>
+            <li>ML experiments and any metadata tracking</li>
+            <li>Integration with popular ML frameworks</li>
+            <li>Easy migration from other experiment trackers</li>
+            </ul>
+          </td>
+        <td>
+          <ul>
+            <li>Metadata visualization via Aim Explorers</li>
+            <li>Grouping and aggregation</li>
+            <li>Querying using Python expressions</li>
+          </ul>
+        </td>
+      </tr>
+      <tr>
+        <th>Run ML Trainings Effectively ⚡</th>
+        <th>Organize Your Experiments 🗂️</th>
+      </tr>
+      <tr>
+        <td>
+          <ul>
+            <li>System info and resource usage tracking</li>
+            <li>Real-time alerting on training progress</li>
+            <li>Logging and configurable notifications</li>
+          </ul>
+        </td>
+        <td>
+          <ul>
+            <li>Detailed run information for easy debugging</li>
+            <li>Centralized dashboard for holistic view</li>
+            <li>Runs grouping with tags and experiments</li></ul>
+        </td>
+      </tr>
+    </tbody>
+  </table>
+</div>
 
-- Centralized dashboard to holistically view all your runs, their hparams and results.
-- Use SDK to query/access all your runs and tracked metadata.
-- You own your data - Aim is open source and self hosted.
+# 🎬 Demos
 
-# Demos
+Check out live Aim demos NOW to see it in action.
 
-| Machine translation | lightweight-GAN |
+| [Machine translation experiments](http://play.aimstack.io:10001/metrics?grouping=HQGdK9Xxy35e6sY1CYkCmk1WbWMN2AsCNfJJ3d1RJYLtrVPMoF5UpGiA6CF8bEJnfzRsKpqespf3AEuKSVrhUYvYk9MxzNGA9XZWYUf6phEg8AMbZGLRVDXnAPDuo8tueqsST1ZLizWzQwDYJWHUza6pyB2Eojt9uWqNHUdb858TqDRnCJzqiVJXKXEzFWUyvU8MckJo1qpqWWCTb4GpYN6DUJZx2GXDGR21e2xxd4m7PmNUnbA9B3apLttZoipJF6c3v7tNUKmb6irpqnNB3yc57tqYDa1XZuKfDxkMtyFdQ1x95K4jjsTVwhftEWLze35QNcxNXRCGGS9o9yEfTLG26GUX2zjPZFCjjMGU6vV7z1xRccK8MyoGrLSgAQCbvk68dTGBHpXUBvCRq8N&chart=FviZzVrt4fVQPjpCLr9sVGGrcR5etSroyqambiKpm3nTgpyv4eQxKuwNX9uN8UtKmzYUhUyTMBEANHmtbwjLApkvnYeNbxGNC6PVcoqi65m1XJnSrvgt8WiD89BapFAWRUwAGx6SWD7KZPsk3RQyysU7W7FjD3Q99NusxFGhsEfD6HXc7i8xH9KHDRGjLwh6x9VTtSp4FS8HEvpLSiiJoX7LCTi8pB7dXvrQ8G5w3jPsFz4qXYFdsVaCNL1BpFFZuiqQNkfbnM84gEq7UmiV1VzM4oS3AgQHxADG3kpBVp6eKTey9F1Swd4FcUkFA9QEPjgQgqwRGjkquZ2bdDDVLBnCh7JPvboP2kifCiZZ5MDdV9MMx6PKHp4DusWyWLXiHQYPkpGPWBiuccMUXDsuJaCWJbuABdY7CyiJMv1jdHYkjabygSxehPVyEDefWAtjBfv2vaeM1xv63jadbmpKYFxft7qmuT9HvVxiGvRgs4RQFxy8K4rtFBca3HNs1mDaaY81gy9MGXyw7BS5Fniu92jaJpsWDdg6Y3AQBLZtrpJy2obEZ4yzJaCVT7JUNPAyyCUNLck393VFLoEkaD9CU5npK5R7tj1c1G3gkMNQXnSXy5NpSj8deMmXV5qz3JKu1nq2caGQKcqjzy2gLkExdm674AMFjSg9yFjK6VqASXQ17NKtWRUvaYoxGbHDAFQaMKWKh8QLm22QA9mKT8NksLptWozbgDvafnQLNMvezLU5bvKV5o75PAWYiRB56RcYfEhzaB6YWdgL7TJicyY5rFi6Az8UZ7wqB3N5iMuZdpxhKn5KbZDxyuUMuvVt24i5LVPPmmwQtqxMoJ4aLo48a2YvDW6TAkdQjNjvn6KcEEz6GTixujb1YHhMUD8v4AepWKEwKz1ddEca1P2wLQjbpihCuaqbxeohnuZZLogJdUBojBEDgrnrrVpPBaLLEkGSpkJbtrsKUuEeBo1AF3yNgHftLbynGpobVF5DhmsmddmiA6c8vSTokJxHhjpnW8mAcNHBRtmVJCT7VkdHSAhNypM4Hivwfx5jCccG9LauKmCeRMDzHiA57TX9W6ttcPHSvUyQorARQAd2oeNY4H83hZjHh9Bt8iwKZRt4xK6hrTR8tif7hq8eURXrGH9Ys7TzykXK8FHHWvLNzNnYf3E4a9NkD43MjfKvMM1hj4Q2K8MHbmRCqrmFrHP5kim9shq6mhLPTgwha32nvnrBkfPQVPwpGTzKuwE&select=CdsQ7jVNkogQhRzQR3e28Ek39AZ4Ma2y37k5zJaf9EZmQhMjy8GtGm4LGU6dRFuAVG7mYww5xDrQAE74KHQ3Kk1e6661RmcmNALAUjtHyCmrTVBMCnBGNiuq1y7EzmxoodYHU1BV1rnoefQAw2kTBtbWi11hV1P4LcwFCcXfUWF6rpRC7ehEnUCTqUV4bkGVJPLcmk9mdmiGwa2YgmnSShNGPVGZiEi1rMVECyngSRVdqdZwAeXBGWFLfqF1KbZeCo4MTF4SSmFupJ9zLhYbuojEbopyFWHQ6xs3sq9epPeaQziLM4Js7oFYRmuFWUYdFqnZngmewXWmi7tQAgVqhiT6dMjG2eTdfgX6WuRSuoHALkh2XJhHA6GfZLUcxC5Ni9YyKuBTamtaYarbNNJJ8z15WWvuUkLpjgHdEpE2h924xFdu8aoZNuiQxYGvcndaW1BTGMXS5fTKPqYfe2n8Ky2HWPkcX3hEXtyawu1F9BndKNaXLPgsdAoFBArBZnSe28YtSmTa5LRucKVBAxakvv5MWMXchAmpaGFQbZyYUoMgQLcJd7Y96x6zSR7nhwr5Ar81BrmqYz2WFLuk7osUbwsc9HbSG6CQt8p6Vg2u7DjKaZXW8pjkPHAKrHWtHEDiJPJ5rj6VsdFm3) | [lightweight-GAN experiments](http://play.aimstack.io:10002/images?grouping=E1zQzcmtDR3wibEa1MVysTvCyZEv1T8ixkCxTWExCyMnHtX2HyiF9eszvPgfd2xdJ5TUTKGpSs1bsLVq5tHAV3uWtsZmmckn6HjNtVCMyQDJpwhiEy5tAyw&select=2NEXuD7fFoaLcwRjymjA1wLmUrGs9s3AiXcCW82C367SwJt18CAB6xzkMGowrUDuDwggE1huaPVcQJpQUsmAQx1CnGiqCUBp2jPMd5mMNPX2QKQMcmvu9ZykBNkeBvCQFPd9ERuQD2g1EjWuvyJ3H53mAZTfp94LCXvR9CUsG5ei2CjQUzfZLM6DCyUr1GPaEVnY5f1EwzicNxXuoutkBgqCqaobJ7Do4q4eHAA6ooiWU6ekS3D2sLj6qYwhVTjfGCPfbWwBiH83nFkY3fLExzdeTY2zeUHeeYikQR9S7xHbVD8WvjekdQVp8X4dNLJZxiVmEqHpPRnU3ZrYsMhE7yFAAgjJwPNUzLTt6YFrtZBcmc4rwAC2oyrqysUSEr6gzL6LcJ6yuqDGf9D5tzftHbTLDkhc8B2sCgTS&images=9vt2MvuQj2Q7jxGQYhNH6ZnWw4CsEzubFcFotuqCHfzvuruDs6pyWfhqhinD4hCiYsAURXgJbmq2L5z4vEQMbrE7iTy8XHNndPBPyuCEvRpxGwwFkukX3YGkVhNDQmUPtBagKbsMAgUASJM8hFtKboqbu9KWTModsjd4Qag7aL1KbJCzBYmZLCpKMSf6eKUTQtfwLLWbgquEx6oahAoSujV6aZ5cjsjN4JdGtPbicySpccgLDQHaQYTHCseA6sPVaEwCsoQDJAcTnjEVFFUUUW5HbPkrNgeRKb8M9pxudrweRQ3gNukLx5yizxQKrmcKU7saxLraqYUA2y5LmEQohsWGUq8sKkvGDH6oNLx2ytJsdVM5PGieENXMAaPg3KuWYXXTwixzwscdDsHSWeiXTGj1QxUKiBCnfwkZ7pZbYMCSgczSn9WpwygrKhb2znSYhn4gFzCsdjiXPPDv9LpPzkFVbsMCvk1CadqpwxTfxNmteKm7CQVViyCrvheGAk5rKpPzaBc5agyvfKpUqgRarxojnG8a4s1Y7qFT1rNVSC13C9h5fG54dDoFHxDyvej3bVTMDYsAiie3eVA3yEskyBGwApPNtjLY2H4b9jTmR3V7jnA9moFGfwMiXUjt8eoJsWTNkqBdRGSnqdva8zi5bApQaggnLebgCRpK1g8VvPrVS3ABQC8aMZJ2vibebHePWs1ahWZ2AXUUYwcuSRkiUWHwgtG9U1x6rR41UxFFNvW9rpDsU99DWzYpdgxfU75wTEPb2qeXYPxV1zVt5ixcFfA3Lvtsp5XXyfHY9FaNFeKKzAUQXPAkMWG4yH4Tp5me8Nt4puBC4pvJrboVcQdSsYhtxj2YwUjzN7Jyn9BV28dtRFPdtFUUc9pKpLvhZAD6XPDtKqrN3pG3LwYTKAiMDtC6tHvDqhQGuJGQZH5cVyTKkT48Xup4znass8tJxUJwacVQa6x2ewyd8AXCfc4j9bPQssabADmc1ho5Eghn5qe82cEcyG1okdfBCRMfmZ5EeCeKQYmoXddxM2cAwfJzCzG9bGtaMvXk3VV8TrSiRKjg3Exbftv8gx12QAzoBP9zosuULFpEAPZF1TvHJbEUmYgu9gwuRTAS3qYiywB7dsCq8wsTr7qmwt8WFFucpte8WvrkRGYy1GA7bD6uPhvS6sr1Wv259oB7Tkr5kirMo6Vdkz8ex9zVd4h2AP1J1dy8cqXaSk5B3HTZ6n1qdAMt4faLtt8SNqg4EqcvXx6r2J1czzXAPa9oSseYifvedcMyxnWkcTvno4QA6sp6zH25ubEwPAVzZZk35nNoJPasH3PgEgLafGPLCsPDD2sku5djPjfqkbDLUWMYm7BbTr7xK8v4UoTS485rPiF6VKoNQSuEnKQMT3uNRTS4EXNMjyRfUs4gk1217EhGVLhfqiZQyG4gqEhcJE3phLydLskk36PyGEbyFyvigjwvrK6boJnFpesze6Czc13HdWbWp6LHLseYujigdmdktU6EQb5KmghstmJ9gUF14JVPjYP57xtv19UT8XDuaJfwJn9z3U17ZDFnQ5zbXKSwD9ikMEd6VFo1xLBRHSmRdFSqcC96s23qWmMhheGtv6tTQAkq7CB1J1gy3skuFJXqhs1RvFWbFFUCLmHeTCtskEsQVP5Rkzat5Jn3QtSqCiRpEGc9Ykd5bWFAaqoudGcqEt993tVfVS3ZrVKAa6NDmbtAcdnfsUZxDt2muRPJDNVCBNW5k8XvevMpMsL3uCETtdutufp1VyLur2Yyx5WA8AeeFeDBxRxad3ZHbH27XdMpxWHF26hnbQAewspG1weRpVW9Ebc4Lc53RBeu8gVmTbKydrri1FHaYySZqCxht8bN4kdqSmkymmcTN3cfRN9DmzcmfKG6GbTDeCA9oXz5cVqrGXZcAiaj1oinnByW7W8GwhtK1Tzd7LG74Nu35DUdPCJXMH2ug4SEa3yXERXCaLvAHvFZAS89e7RUPpr3nTTrQLurjHSdkJ39pwEJpDcDjeWHsJSmTG1x195e6xvMmgPxAZd3Lzyk8Cxme8p1cY7FehSbTPc3zAAwi9LDGYyoQRcdbRHPLJ2W8rt9KeNfNq9moa1RVFPCPvhGuuyycT4f4QkP4Nvy4iUCaB5d8B1hcgmtg2X9Zpg6GUR32RYneQigK6S9ZYPNnaFeCNZZrwaYjkDpKMTMB6N24JC1TEAH8en3kXzf8CpLWeJpxoyB3hcCxjFHLYaovzgfGPeFBPY6ADDUcT3xkpUUEybdxE1cX7drHvBwyGqeU5g7i424tydxqufUgPY5sF9bM6mdoA3AvqDD9B3Zai71irxYXX8e6rRck4RwptJgBMX2gbotizoz9LrUwFQ2naBfJvbfEhZNCzME8a7H2YiVcq4Z6pkfbT1uMLfaixfw8nQCzVRbJAyVZgGzVbBj242LpD48R6VmxGcU5t2XkN8hZyYdBk1Uds9QyUG9VpC8ka7HjkvxBMknk6v4BjMnHnAj4ZxDUxMWEDbWw6iWD3iYWzVn3n5dzRcAqCQv3m2ZUnwuHHCTVJVZKZVyxrFP5eznpNv87RUXMfjbXypoLJFVtMoq81y82hYRFSkbAUwzhhoXBAGeBGDmDcwky2Hf7ZmfkzDLnRke916VxhTRLr8c6nXokCn8xwweuJHFeBqx7D88gpRbn5RrnH33545zyzyNpZpabQUGY3L7G3QznVw6wCS9x7FMixW2mgCeeWFhPDiz5Kz6DyyjaT413VSoRBCRakNcitYHUXqqCUPsFmZ3LTedA8jN99fYzse5LX36TSVbjnM7XmiZ8vNoH5mUsawmvG7NXbhgoyhx4rzL7t57A4g7sQg4YhGAFzEbXrh416riiPH8r52on2VEqkjNPDnybSg3cwuR6rPfMWA7YoyEAp14aStUPaKqbM9omConMxZde5o2DpjS86G5vDBY1o7F4LnBHLHRxKfqAkTPjvEdhaYY2uY6i598po9b2fAtpUGCbXnzcNrV5Vei5WkiQAqRT6whGr29PTLsAVGed71drx7BqzNiDcFJBL9dVrVoPqYLvrYVGi89MuuWuirD7CRhXWahysjrNpFf4aHXmuXS3UD7SFgkqAZzL1hrVq77K8UhGMMWLUzE9gjP6PH4xL6fJetKaRGZNpbsqDoKuBkBAk9j1nGpYMAyuo2H2AWUyj8PUgAbi1e4KPeqNqMVT85oZ9jkCggYczgNhT8gw5QsMarouMctMdbokxRfxz2xt9r2DuNmbEmq9e13Tqv94VrzR91R2o7pvH7YUFtJvcoJwR8K5jyof5SfKHT53zaBKxkLfCpPP3qR9ZCbAzVbreFKsQnCcZpd643VA9wtgKXxc375NwKj4QbnvafKNU9qc455d3S3o57mU4DFA7yHSqY1q41zySxfXYx4txL4TiqeyyTQu7KcHYbTUYRs69pkE1rWRW84N1qmisw2o7iLQPrhWkixrRDRk5toYWQg6ZDZExCyedYBGjsUAut)|
 |:---:|:---:|
-| <a href="http://play.aimstack.io:10001/metrics?grouping=HQGdK9Xxy35e6sY1CYkCmk1WbWMN2AsCNfJJ3d1RJYLtrVPMoF5UpGiA6CF8bEJnfzRsKpqespf3AEuKSVrhUYvYk9MxzNGA9XZWYUf6phEg8AMbZGLRVDXnAPDuo8tueqsST1ZLizWzQwDYJWHUza6pyB2Eojt9uWqNHUdb858TqDRnCJzqiVJXKXEzFWUyvU8MckJo1qpqWWCTb4GpYN6DUJZx2GXDGR21e2xxd4m7PmNUnbA9B3apLttZoipJF6c3v7tNUKmb6irpqnNB3yc57tqYDa1XZuKfDxkMtyFdQ1x95K4jjsTVwhftEWLze35QNcxNXRCGGS9o9yEfTLG26GUX2zjPZFCjjMGU6vV7z1xRccK8MyoGrLSgAQCbvk68dTGBHpXUBvCRq8N&chart=FviZzVrt4fVQPjpCLr9sVGGrcR5etSroyqambiKpm3nTgpyv4eQxKuwNX9uN8UtKmzYUhUyTMBEANHmtbwjLApkvnYeNbxGNC6PVcoqi65m1XJnSrvgt8WiD89BapFAWRUwAGx6SWD7KZPsk3RQyysU7W7FjD3Q99NusxFGhsEfD6HXc7i8xH9KHDRGjLwh6x9VTtSp4FS8HEvpLSiiJoX7LCTi8pB7dXvrQ8G5w3jPsFz4qXYFdsVaCNL1BpFFZuiqQNkfbnM84gEq7UmiV1VzM4oS3AgQHxADG3kpBVp6eKTey9F1Swd4FcUkFA9QEPjgQgqwRGjkquZ2bdDDVLBnCh7JPvboP2kifCiZZ5MDdV9MMx6PKHp4DusWyWLXiHQYPkpGPWBiuccMUXDsuJaCWJbuABdY7CyiJMv1jdHYkjabygSxehPVyEDefWAtjBfv2vaeM1xv63jadbmpKYFxft7qmuT9HvVxiGvRgs4RQFxy8K4rtFBca3HNs1mDaaY81gy9MGXyw7BS5Fniu92jaJpsWDdg6Y3AQBLZtrpJy2obEZ4yzJaCVT7JUNPAyyCUNLck393VFLoEkaD9CU5npK5R7tj1c1G3gkMNQXnSXy5NpSj8deMmXV5qz3JKu1nq2caGQKcqjzy2gLkExdm674AMFjSg9yFjK6VqASXQ17NKtWRUvaYoxGbHDAFQaMKWKh8QLm22QA9mKT8NksLptWozbgDvafnQLNMvezLU5bvKV5o75PAWYiRB56RcYfEhzaB6YWdgL7TJicyY5rFi6Az8UZ7wqB3N5iMuZdpxhKn5KbZDxyuUMuvVt24i5LVPPmmwQtqxMoJ4aLo48a2YvDW6TAkdQjNjvn6KcEEz6GTixujb1YHhMUD8v4AepWKEwKz1ddEca1P2wLQjbpihCuaqbxeohnuZZLogJdUBojBEDgrnrrVpPBaLLEkGSpkJbtrsKUuEeBo1AF3yNgHftLbynGpobVF5DhmsmddmiA6c8vSTokJxHhjpnW8mAcNHBRtmVJCT7VkdHSAhNypM4Hivwfx5jCccG9LauKmCeRMDzHiA57TX9W6ttcPHSvUyQorARQAd2oeNY4H83hZjHh9Bt8iwKZRt4xK6hrTR8tif7hq8eURXrGH9Ys7TzykXK8FHHWvLNzNnYf3E4a9NkD43MjfKvMM1hj4Q2K8MHbmRCqrmFrHP5kim9shq6mhLPTgwha32nvnrBkfPQVPwpGTzKuwE&select=CdsQ7jVNkogQhRzQR3e28Ek39AZ4Ma2y37k5zJaf9EZmQhMjy8GtGm4LGU6dRFuAVG7mYww5xDrQAE74KHQ3Kk1e6661RmcmNALAUjtHyCmrTVBMCnBGNiuq1y7EzmxoodYHU1BV1rnoefQAw2kTBtbWi11hV1P4LcwFCcXfUWF6rpRC7ehEnUCTqUV4bkGVJPLcmk9mdmiGwa2YgmnSShNGPVGZiEi1rMVECyngSRVdqdZwAeXBGWFLfqF1KbZeCo4MTF4SSmFupJ9zLhYbuojEbopyFWHQ6xs3sq9epPeaQziLM4Js7oFYRmuFWUYdFqnZngmewXWmi7tQAgVqhiT6dMjG2eTdfgX6WuRSuoHALkh2XJhHA6GfZLUcxC5Ni9YyKuBTamtaYarbNNJJ8z15WWvuUkLpjgHdEpE2h924xFdu8aoZNuiQxYGvcndaW1BTGMXS5fTKPqYfe2n8Ky2HWPkcX3hEXtyawu1F9BndKNaXLPgsdAoFBArBZnSe28YtSmTa5LRucKVBAxakvv5MWMXchAmpaGFQbZyYUoMgQLcJd7Y96x6zSR7nhwr5Ar81BrmqYz2WFLuk7osUbwsc9HbSG6CQt8p6Vg2u7DjKaZXW8pjkPHAKrHWtHEDiJPJ5rj6VsdFm3"> <img width="800px" src="https://user-images.githubusercontent.com/13848158/154340796-c9e91b13-8ee0-4a67-bcde-8cf3aaa7ba99.jpg"> </a> | <a href="http://play.aimstack.io:10002/images?grouping=E1zQzcmtDR3wibEa1MVysTvCyZEv1T8ixkCxTWExCyMnHtX2HyiF9eszvPgfd2xdJ5TUTKGpSs1bsLVq5tHAV3uWtsZmmckn6HjNtVCMyQDJpwhiEy5tAyw&select=2NEXuD7fFoaLcwRjymjA1wLmUrGs9s3AiXcCW82C367SwJt18CAB6xzkMGowrUDuDwggE1huaPVcQJpQUsmAQx1CnGiqCUBp2jPMd5mMNPX2QKQMcmvu9ZykBNkeBvCQFPd9ERuQD2g1EjWuvyJ3H53mAZTfp94LCXvR9CUsG5ei2CjQUzfZLM6DCyUr1GPaEVnY5f1EwzicNxXuoutkBgqCqaobJ7Do4q4eHAA6ooiWU6ekS3D2sLj6qYwhVTjfGCPfbWwBiH83nFkY3fLExzdeTY2zeUHeeYikQR9S7xHbVD8WvjekdQVp8X4dNLJZxiVmEqHpPRnU3ZrYsMhE7yFAAgjJwPNUzLTt6YFrtZBcmc4rwAC2oyrqysUSEr6gzL6LcJ6yuqDGf9D5tzftHbTLDkhc8B2sCgTS&images=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"> <img width="800px" src="https://user-images.githubusercontent.com/13848158/154340790-bc7b7a21-e8a1-43a1-809d-4060b5bfb60f.jpg"> </a> |
+| <a href="http://play.aimstack.io:10001/metrics?grouping=HQGdK9Xxy35e6sY1CYkCmk1WbWMN2AsCNfJJ3d1RJYLtrVPMoF5UpGiA6CF8bEJnfzRsKpqespf3AEuKSVrhUYvYk9MxzNGA9XZWYUf6phEg8AMbZGLRVDXnAPDuo8tueqsST1ZLizWzQwDYJWHUza6pyB2Eojt9uWqNHUdb858TqDRnCJzqiVJXKXEzFWUyvU8MckJo1qpqWWCTb4GpYN6DUJZx2GXDGR21e2xxd4m7PmNUnbA9B3apLttZoipJF6c3v7tNUKmb6irpqnNB3yc57tqYDa1XZuKfDxkMtyFdQ1x95K4jjsTVwhftEWLze35QNcxNXRCGGS9o9yEfTLG26GUX2zjPZFCjjMGU6vV7z1xRccK8MyoGrLSgAQCbvk68dTGBHpXUBvCRq8N&chart=FviZzVrt4fVQPjpCLr9sVGGrcR5etSroyqambiKpm3nTgpyv4eQxKuwNX9uN8UtKmzYUhUyTMBEANHmtbwjLApkvnYeNbxGNC6PVcoqi65m1XJnSrvgt8WiD89BapFAWRUwAGx6SWD7KZPsk3RQyysU7W7FjD3Q99NusxFGhsEfD6HXc7i8xH9KHDRGjLwh6x9VTtSp4FS8HEvpLSiiJoX7LCTi8pB7dXvrQ8G5w3jPsFz4qXYFdsVaCNL1BpFFZuiqQNkfbnM84gEq7UmiV1VzM4oS3AgQHxADG3kpBVp6eKTey9F1Swd4FcUkFA9QEPjgQgqwRGjkquZ2bdDDVLBnCh7JPvboP2kifCiZZ5MDdV9MMx6PKHp4DusWyWLXiHQYPkpGPWBiuccMUXDsuJaCWJbuABdY7CyiJMv1jdHYkjabygSxehPVyEDefWAtjBfv2vaeM1xv63jadbmpKYFxft7qmuT9HvVxiGvRgs4RQFxy8K4rtFBca3HNs1mDaaY81gy9MGXyw7BS5Fniu92jaJpsWDdg6Y3AQBLZtrpJy2obEZ4yzJaCVT7JUNPAyyCUNLck393VFLoEkaD9CU5npK5R7tj1c1G3gkMNQXnSXy5NpSj8deMmXV5qz3JKu1nq2caGQKcqjzy2gLkExdm674AMFjSg9yFjK6VqASXQ17NKtWRUvaYoxGbHDAFQaMKWKh8QLm22QA9mKT8NksLptWozbgDvafnQLNMvezLU5bvKV5o75PAWYiRB56RcYfEhzaB6YWdgL7TJicyY5rFi6Az8UZ7wqB3N5iMuZdpxhKn5KbZDxyuUMuvVt24i5LVPPmmwQtqxMoJ4aLo48a2YvDW6TAkdQjNjvn6KcEEz6GTixujb1YHhMUD8v4AepWKEwKz1ddEca1P2wLQjbpihCuaqbxeohnuZZLogJdUBojBEDgrnrrVpPBaLLEkGSpkJbtrsKUuEeBo1AF3yNgHftLbynGpobVF5DhmsmddmiA6c8vSTokJxHhjpnW8mAcNHBRtmVJCT7VkdHSAhNypM4Hivwfx5jCccG9LauKmCeRMDzHiA57TX9W6ttcPHSvUyQorARQAd2oeNY4H83hZjHh9Bt8iwKZRt4xK6hrTR8tif7hq8eURXrGH9Ys7TzykXK8FHHWvLNzNnYf3E4a9NkD43MjfKvMM1hj4Q2K8MHbmRCqrmFrHP5kim9shq6mhLPTgwha32nvnrBkfPQVPwpGTzKuwE&select=CdsQ7jVNkogQhRzQR3e28Ek39AZ4Ma2y37k5zJaf9EZmQhMjy8GtGm4LGU6dRFuAVG7mYww5xDrQAE74KHQ3Kk1e6661RmcmNALAUjtHyCmrTVBMCnBGNiuq1y7EzmxoodYHU1BV1rnoefQAw2kTBtbWi11hV1P4LcwFCcXfUWF6rpRC7ehEnUCTqUV4bkGVJPLcmk9mdmiGwa2YgmnSShNGPVGZiEi1rMVECyngSRVdqdZwAeXBGWFLfqF1KbZeCo4MTF4SSmFupJ9zLhYbuojEbopyFWHQ6xs3sq9epPeaQziLM4Js7oFYRmuFWUYdFqnZngmewXWmi7tQAgVqhiT6dMjG2eTdfgX6WuRSuoHALkh2XJhHA6GfZLUcxC5Ni9YyKuBTamtaYarbNNJJ8z15WWvuUkLpjgHdEpE2h924xFdu8aoZNuiQxYGvcndaW1BTGMXS5fTKPqYfe2n8Ky2HWPkcX3hEXtyawu1F9BndKNaXLPgsdAoFBArBZnSe28YtSmTa5LRucKVBAxakvv5MWMXchAmpaGFQbZyYUoMgQLcJd7Y96x6zSR7nhwr5Ar81BrmqYz2WFLuk7osUbwsc9HbSG6CQt8p6Vg2u7DjKaZXW8pjkPHAKrHWtHEDiJPJ5rj6VsdFm3"> <img src="https://user-images.githubusercontent.com/97726819/225964524-0051c2c7-8554-43ae-82b8-adcb77bcf1ba.png"> </a> | <a href="http://play.aimstack.io:10002/images?grouping=E1zQzcmtDR3wibEa1MVysTvCyZEv1T8ixkCxTWExCyMnHtX2HyiF9eszvPgfd2xdJ5TUTKGpSs1bsLVq5tHAV3uWtsZmmckn6HjNtVCMyQDJpwhiEy5tAyw&select=2NEXuD7fFoaLcwRjymjA1wLmUrGs9s3AiXcCW82C367SwJt18CAB6xzkMGowrUDuDwggE1huaPVcQJpQUsmAQx1CnGiqCUBp2jPMd5mMNPX2QKQMcmvu9ZykBNkeBvCQFPd9ERuQD2g1EjWuvyJ3H53mAZTfp94LCXvR9CUsG5ei2CjQUzfZLM6DCyUr1GPaEVnY5f1EwzicNxXuoutkBgqCqaobJ7Do4q4eHAA6ooiWU6ekS3D2sLj6qYwhVTjfGCPfbWwBiH83nFkY3fLExzdeTY2zeUHeeYikQR9S7xHbVD8WvjekdQVp8X4dNLJZxiVmEqHpPRnU3ZrYsMhE7yFAAgjJwPNUzLTt6YFrtZBcmc4rwAC2oyrqysUSEr6gzL6LcJ6yuqDGf9D5tzftHbTLDkhc8B2sCgTS&images=9vt2MvuQj2Q7jxGQYhNH6ZnWw4CsEzubFcFotuqCHfzvuruDs6pyWfhqhinD4hCiYsAURXgJbmq2L5z4vEQMbrE7iTy8XHNndPBPyuCEvRpxGwwFkukX3YGkVhNDQmUPtBagKbsMAgUASJM8hFtKboqbu9KWTModsjd4Qag7aL1KbJCzBYmZLCpKMSf6eKUTQtfwLLWbgquEx6oahAoSujV6aZ5cjsjN4JdGtPbicySpccgLDQHaQYTHCseA6sPVaEwCsoQDJAcTnjEVFFUUUW5HbPkrNgeRKb8M9pxudrweRQ3gNukLx5yizxQKrmcKU7saxLraqYUA2y5LmEQohsWGUq8sKkvGDH6oNLx2ytJsdVM5PGieENXMAaPg3KuWYXXTwixzwscdDsHSWeiXTGj1QxUKiBCnfwkZ7pZbYMCSgczSn9WpwygrKhb2znSYhn4gFzCsdjiXPPDv9LpPzkFVbsMCvk1CadqpwxTfxNmteKm7CQVViyCrvheGAk5rKpPzaBc5agyvfKpUqgRarxojnG8a4s1Y7qFT1rNVSC13C9h5fG54dDoFHxDyvej3bVTMDYsAiie3eVA3yEskyBGwApPNtjLY2H4b9jTmR3V7jnA9moFGfwMiXUjt8eoJsWTNkqBdRGSnqdva8zi5bApQaggnLebgCRpK1g8VvPrVS3ABQC8aMZJ2vibebHePWs1ahWZ2AXUUYwcuSRkiUWHwgtG9U1x6rR41UxFFNvW9rpDsU99DWzYpdgxfU75wTEPb2qeXYPxV1zVt5ixcFfA3Lvtsp5XXyfHY9FaNFeKKzAUQXPAkMWG4yH4Tp5me8Nt4puBC4pvJrboVcQdSsYhtxj2YwUjzN7Jyn9BV28dtRFPdtFUUc9pKpLvhZAD6XPDtKqrN3pG3LwYTKAiMDtC6tHvDqhQGuJGQZH5cVyTKkT48Xup4znass8tJxUJwacVQa6x2ewyd8AXCfc4j9bPQssabADmc1ho5Eghn5qe82cEcyG1okdfBCRMfmZ5EeCeKQYmoXddxM2cAwfJzCzG9bGtaMvXk3VV8TrSiRKjg3Exbftv8gx12QAzoBP9zosuULFpEAPZF1TvHJbEUmYgu9gwuRTAS3qYiywB7dsCq8wsTr7qmwt8WFFucpte8WvrkRGYy1GA7bD6uPhvS6sr1Wv259oB7Tkr5kirMo6Vdkz8ex9zVd4h2AP1J1dy8cqXaSk5B3HTZ6n1qdAMt4faLtt8SNqg4EqcvXx6r2J1czzXAPa9oSseYifvedcMyxnWkcTvno4QA6sp6zH25ubEwPAVzZZk35nNoJPasH3PgEgLafGPLCsPDD2sku5djPjfqkbDLUWMYm7BbTr7xK8v4UoTS485rPiF6VKoNQSuEnKQMT3uNRTS4EXNMjyRfUs4gk1217EhGVLhfqiZQyG4gqEhcJE3phLydLskk36PyGEbyFyvigjwvrK6boJnFpesze6Czc13HdWbWp6LHLseYujigdmdktU6EQb5KmghstmJ9gUF14JVPjYP57xtv19UT8XDuaJfwJn9z3U17ZDFnQ5zbXKSwD9ikMEd6VFo1xLBRHSmRdFSqcC96s23qWmMhheGtv6tTQAkq7CB1J1gy3skuFJXqhs1RvFWbFFUCLmHeTCtskEsQVP5Rkzat5Jn3QtSqCiRpEGc9Ykd5bWFAaqoudGcqEt993tVfVS3ZrVKAa6NDmbtAcdnfsUZxDt2muRPJDNVCBNW5k8XvevMpMsL3uCETtdutufp1VyLur2Yyx5WA8AeeFeDBxRxad3ZHbH27XdMpxWHF26hnbQAewspG1weRpVW9Ebc4Lc53RBeu8gVmTbKydrri1FHaYySZqCxht8bN4kdqSmkymmcTN3cfRN9DmzcmfKG6GbTDeCA9oXz5cVqrGXZcAiaj1oinnByW7W8GwhtK1Tzd7LG74Nu35DUdPCJXMH2ug4SEa3yXERXCaLvAHvFZAS89e7RUPpr3nTTrQLurjHSdkJ39pwEJpDcDjeWHsJSmTG1x195e6xvMmgPxAZd3Lzyk8Cxme8p1cY7FehSbTPc3zAAwi9LDGYyoQRcdbRHPLJ2W8rt9KeNfNq9moa1RVFPCPvhGuuyycT4f4QkP4Nvy4iUCaB5d8B1hcgmtg2X9Zpg6GUR32RYneQigK6S9ZYPNnaFeCNZZrwaYjkDpKMTMB6N24JC1TEAH8en3kXzf8CpLWeJpxoyB3hcCxjFHLYaovzgfGPeFBPY6ADDUcT3xkpUUEybdxE1cX7drHvBwyGqeU5g7i424tydxqufUgPY5sF9bM6mdoA3AvqDD9B3Zai71irxYXX8e6rRck4RwptJgBMX2gbotizoz9LrUwFQ2naBfJvbfEhZNCzME8a7H2YiVcq4Z6pkfbT1uMLfaixfw8nQCzVRbJAyVZgGzVbBj242LpD48R6VmxGcU5t2XkN8hZyYdBk1Uds9QyUG9VpC8ka7HjkvxBMknk6v4BjMnHnAj4ZxDUxMWEDbWw6iWD3iYWzVn3n5dzRcAqCQv3m2ZUnwuHHCTVJVZKZVyxrFP5eznpNv87RUXMfjbXypoLJFVtMoq81y82hYRFSkbAUwzhhoXBAGeBGDmDcwky2Hf7ZmfkzDLnRke916VxhTRLr8c6nXokCn8xwweuJHFeBqx7D88gpRbn5RrnH33545zyzyNpZpabQUGY3L7G3QznVw6wCS9x7FMixW2mgCeeWFhPDiz5Kz6DyyjaT413VSoRBCRakNcitYHUXqqCUPsFmZ3LTedA8jN99fYzse5LX36TSVbjnM7XmiZ8vNoH5mUsawmvG7NXbhgoyhx4rzL7t57A4g7sQg4YhGAFzEbXrh416riiPH8r52on2VEqkjNPDnybSg3cwuR6rPfMWA7YoyEAp14aStUPaKqbM9omConMxZde5o2DpjS86G5vDBY1o7F4LnBHLHRxKfqAkTPjvEdhaYY2uY6i598po9b2fAtpUGCbXnzcNrV5Vei5WkiQAqRT6whGr29PTLsAVGed71drx7BqzNiDcFJBL9dVrVoPqYLvrYVGi89MuuWuirD7CRhXWahysjrNpFf4aHXmuXS3UD7SFgkqAZzL1hrVq77K8UhGMMWLUzE9gjP6PH4xL6fJetKaRGZNpbsqDoKuBkBAk9j1nGpYMAyuo2H2AWUyj8PUgAbi1e4KPeqNqMVT85oZ9jkCggYczgNhT8gw5QsMarouMctMdbokxRfxz2xt9r2DuNmbEmq9e13Tqv94VrzR91R2o7pvH7YUFtJvcoJwR8K5jyof5SfKHT53zaBKxkLfCpPP3qR9ZCbAzVbreFKsQnCcZpd643VA9wtgKXxc375NwKj4QbnvafKNU9qc455d3S3o57mU4DFA7yHSqY1q41zySxfXYx4txL4TiqeyyTQu7KcHYbTUYRs69pkE1rWRW84N1qmisw2o7iLQPrhWkixrRDRk5toYWQg6ZDZExCyedYBGjsUAut"> <img src="https://user-images.githubusercontent.com/97726819/225948275-a41946ea-89f4-45f1-bce1-251c84dcddca.png"> </a> |
 | Training logs of a neural translation model(from WMT'19 competition). | Training logs of 'lightweight' GAN, proposed in ICLR 2021. |
 
-| FastSpeech 2 | Simple MNIST |
+| [FastSpeech 2 experiments](http://play.aimstack.io:10004/runs/d9e89aa7875e44b2ba85612a/audios)| [Simple MNIST](http://play.aimstack.io:10003/runs/7f083da898624a2c98e0f363/distributions) |
 |:---:|:---:|
-| <a href="http://play.aimstack.io:10004/runs/d9e89aa7875e44b2ba85612a/audios"> <img width="800px" src="https://user-images.githubusercontent.com/13848158/154340778-dbe19620-2f27-4298-b0cb-caf3904760f1.jpg"> </a> | <a href="http://play.aimstack.io:10003/runs/7f083da898624a2c98e0f363/distributions"> <img width="800px" src="https://user-images.githubusercontent.com/13848158/154340785-a7e4d9fd-d048-4207-8cd1-c4edff9cca6a.jpg"> </a> |
+| <a href="http://play.aimstack.io:10004/runs/d9e89aa7875e44b2ba85612a/audios"> <img src="https://user-images.githubusercontent.com/97726819/225948457-567526da-a329-4c53-a9a7-98dfe392d4c4.png"> </a> | <a href="http://play.aimstack.io:10003/runs/7f083da898624a2c98e0f363/distributions"> <img src="https://user-images.githubusercontent.com/97726819/225948599-ff39c5b7-ae7d-4deb-8bc9-5eee1e189d89.png"> </a> |
 | Training logs of Microsoft's "FastSpeech 2: Fast and High-Quality End-to-End Text to Speech". | Simple MNIST training logs. |
 
-# Quick Start
+# 🌍 Ecosystem
+
+Aim is not just an experiment tracker. It's a groundwork for an ecosystem. 
+Check out the two most famous Aim-based tools.
+
+| [aimlflow](https://github.com/aimhubio/aimlflow) | [Aim-spaCy](https://github.com/aimhubio/aim-spacy) |
+|:---:|:---:|
+| ![aimlflow](https://user-images.githubusercontent.com/97726819/225957836-cdec88e3-4993-435a-a135-d78be3ac1635.png) | ![Aim-spaCy](https://user-images.githubusercontent.com/97726819/225957990-4edc4525-1f65-4405-b663-ce7af888bdfa.png) |
+| Exploring MLflow experiments with a powerful UI | an Aim-based spaCy experiment tracker |
+
+# 🏁 Quick start
 
 Follow the steps below to get started with Aim.
 
-**1. Install Aim on your training environment**
+## 1. Install Aim on your training environment
 
 ```shell
 pip3 install aim
 ```
 
-**2. Integrate Aim with your code**
+## 2. Integrate Aim with your code
 
 ```python
 from aim import Run
 
 # Initialize a new run
 run = Run()
 
@@ -137,237 +223,130 @@
 for i in range(10):
     run.track(i, name='loss', step=i, context={ "subset":"train" })
     run.track(i, name='acc', step=i, context={ "subset":"train" })
 ```
 
 _See the full list of supported trackable objects(e.g. images, text, etc) [here](https://aimstack.readthedocs.io/en/latest/quick_start/supported_types.html)._
 
-**3. Run the training as usual and start Aim UI**
+## 3. Run the training as usual and start Aim UI
 
 ```shell
 aim up
 ```
 
-**4. Or query runs programmatically via SDK**
-
-```python
-from aim import Repo
-
-my_repo = Repo('/path/to/aim/repo')
-
-query = "metric.name == 'loss'" # Example query
-
-# Get collection of metrics
-for run_metrics_collection in my_repo.query_metrics(query).iter_runs():
-    for metric in run_metrics_collection:
-        # Get run params
-        params = metric.run[...]
-        # Get metric values
-        steps, metric_values = metric.values.sparse_numpy()
-```
-
-# Integrations
+## Learn more
 
 <details>
 <summary>
-  Integrate PyTorch Lightning
+<strong>Migrate from other tools</strong>
 </summary>
 
-```python
-from aim.pytorch_lightning import AimLogger
-
-# ...
-trainer = pl.Trainer(logger=AimLogger(experiment='experiment_name'))
-# ...
-```
+</br>
 
-_See documentation [here](https://aimstack.readthedocs.io/en/latest/quick_start/integrations.html#integration-with-pytorch-lightning)._
+Aim has built-in converters to easily migrate logs from other tools. 
+These migrations cover the most common usage scenarios.
+In case of custom and complex scenarios you can use Aim SDK to implement your own conversion script.
+
+- [TensorBoard logs converter](https://aimstack.readthedocs.io/en/latest/quick_start/convert_data.html#show-tensorboard-logs-in-aim)
+- [MLFlow logs converter](https://aimstack.readthedocs.io/en/latest/quick_start/convert_data.html#show-mlflow-logs-in-aim)
+- [Weights & Biases logs converter](https://aimstack.readthedocs.io/en/latest/quick_start/convert_data.html#show-weights-and-biases-logs-in-aim)
 
 </details>
 
 <details>
 <summary>
-  Integrate Hugging Face
+<strong>Integrate Aim into an existing project</strong>
 </summary>
 
-```python
-from aim.hugging_face import AimCallback
+</br>
 
-# ...
-aim_callback = AimCallback(repo='/path/to/logs/dir', experiment='mnli')
-trainer = Trainer(
-    model=model,
-    args=training_args,
-    train_dataset=train_dataset if training_args.do_train else None,
-    eval_dataset=eval_dataset if training_args.do_eval else None,
-    callbacks=[aim_callback],
-    # ...
-)
-# ...
-```
+Aim easily integrates with a wide range of ML frameworks, providing built-in callbacks for most of them.
 
-_See documentation [here](https://aimstack.readthedocs.io/en/latest/quick_start/integrations.html#integration-with-hugging-face)._
+- [Integration with Pytorch Ignite](https://aimstack.readthedocs.io/en/latest/quick_start/integrations.html#integration-with-pytorch-ignite)
+- [Integration with Pytorch Lightning](https://aimstack.readthedocs.io/en/latest/quick_start/integrations.html#integration-with-pytorch-lightning)
+- [Integration with Hugging Face](https://aimstack.readthedocs.io/en/latest/quick_start/integrations.html#integration-with-hugging-face)
+- [Integration with Keras & tf.Keras](https://aimstack.readthedocs.io/en/latest/quick_start/integrations.html#integration-with-keras-tf-keras)
+- [Integration with Keras Tuner](https://aimstack.readthedocs.io/en/latest/quick_start/integrations.html#integration-with-keras-tuner)
+- [Integration with XGboost](https://aimstack.readthedocs.io/en/latest/quick_start/integrations.html#integration-with-xgboost)
+- [Integration with CatBoost](https://aimstack.readthedocs.io/en/latest/quick_start/integrations.html#integration-with-catboost)
+- [Integration with LightGBM](https://aimstack.readthedocs.io/en/latest/quick_start/integrations.html#integration-with-lightgbm)
+- [Integration with fastai](https://aimstack.readthedocs.io/en/latest/quick_start/integrations.html#integration-with-fastai)
+- [Integration with MXNet](https://aimstack.readthedocs.io/en/latest/quick_start/integrations.html#integration-with-mxnet)
+- [Integration with Optuna](https://aimstack.readthedocs.io/en/latest/quick_start/integrations.html#integration-with-optuna)
+- [Integration with PaddlePaddle](https://aimstack.readthedocs.io/en/latest/quick_start/integrations.html#integration-with-paddlepaddle)
+- [Integration with Stable-Baselines3](https://aimstack.readthedocs.io/en/latest/quick_start/integrations.html#integration-with-stable-baselines3)
+- [Integration with Acme](https://aimstack.readthedocs.io/en/latest/quick_start/integrations.html#integration-with-acme)
+- [Integration with Prophet](https://aimstack.readthedocs.io/en/latest/quick_start/integrations.html#integration-with-prophet)
 
 </details>
 
 <details>
 <summary>
-  Integrate Keras & tf.keras
+<strong>Query runs programmatically via SDK</strong>
 </summary>
 
-```python
-import aim
-
-# ...
-model.fit(x_train, y_train, epochs=epochs, callbacks=[
-    aim.keras.AimCallback(repo='/path/to/logs/dir', experiment='experiment_name')
-    
-    # Use aim.tensorflow.AimCallback in case of tf.keras
-    aim.tensorflow.AimCallback(repo='/path/to/logs/dir', experiment='experiment_name')
-])
-# ...
-```
-
-_See documentation [here](https://aimstack.readthedocs.io/en/latest/quick_start/integrations.html#integration-with-keras-tf-keras)._
-
-</details>
+</br>
 
-<details>
-<summary>
-  Integrate KerasTuner
-</summary>
+Aim Python SDK empowers you to query and access any piece of tracked metadata with ease.
 
 ```python
-from aim.keras_tuner import AimCallback
-
-# ...
-tuner.search(
-    train_ds,
-    validation_data=test_ds,
-    callbacks=[AimCallback(tuner=tuner, repo='.', experiment='keras_tuner_test')],
-)
-# ...
-```
-
-_See documentation [here](https://aimstack.readthedocs.io/en/latest/quick_start/integrations.html#integration-with-kerastuner)._
-
-</details>
+from aim import Repo
 
-<details>
-<summary>
-  Integrate XGBoost
-</summary>
+my_repo = Repo('/path/to/aim/repo')
 
-```python
-from aim.xgboost import AimCallback
+query = "metric.name == 'loss'" # Example query
 
-# ...
-aim_callback = AimCallback(repo='/path/to/logs/dir', experiment='experiment_name')
-bst = xgb.train(param, xg_train, num_round, watchlist, callbacks=[aim_callback])
-# ...
+# Get collection of metrics
+for run_metrics_collection in my_repo.query_metrics(query).iter_runs():
+    for metric in run_metrics_collection:
+        # Get run params
+        params = metric.run[...]
+        # Get metric values
+        steps, metric_values = metric.values.sparse_numpy()
 ```
 
-_See documentation [here](https://aimstack.readthedocs.io/en/latest/quick_start/integrations.html#integration-with-xgboost)._
 </details>
 
-
 <details>
 <summary>
-  Integrate CatBoost
+<strong>Set up a centralized tracking server</strong>
 </summary>
 
-```python
-from aim.catboost import AimLogger
-
-# ...
-model.fit(train_data, train_labels, log_cout=AimLogger(loss_function='Logloss'), logging_level="Info")
-# ...
-```
-
-_See documentation [here](https://aimstack.readthedocs.io/en/latest/quick_start/integrations.html#integration-with-catboost)._
-</details>
+</br>
 
+Aim remote tracking server allows running experiments in a multi-host environment and collect tracked data in a centralized location.
 
+See the docs on how to [set up the remote server](https://aimstack.readthedocs.io/en/latest/using/remote_tracking.html).
 
-<details>
-<summary>
-  Integrate fastai
-</summary>
-
-```python
-from aim.fastai import AimCallback
-
-# ...
-learn = cnn_learner(dls, resnet18, pretrained=True,
-                    loss_func=CrossEntropyLossFlat(),
-                    metrics=accuracy, model_dir="/tmp/model/",
-                    cbs=AimCallback(repo='.', experiment='fastai_test'))
-# ...
-```
-
-_See documentation [here](https://aimstack.readthedocs.io/en/latest/quick_start/integrations.html#integration-with-fastai)._
 </details>
 
-
 <details>
 <summary>
-  Integrate LightGBM
+<strong>Deploy Aim on kubernetes</strong>
 </summary>
 
-```python
-from aim.lightgbm import AimCallback
+</br>
+
+- The official Aim docker image: https://hub.docker.com/r/aimstack/aim
+- A guide on how to deploy Aim on kubernetes: https://aimstack.readthedocs.io/en/latest/using/k8s_deployment.html
 
-# ...
-aim_callback = AimCallback(experiment='lgb_test')
-aim_callback.experiment['hparams'] = params
-
-gbm = lgb.train(params,
-                lgb_train,
-                num_boost_round=20,
-                valid_sets=lgb_eval,
-                callbacks=[aim_callback, lgb.early_stopping(stopping_rounds=5)])
-# ...
-```
 
-_See documentation [here](https://aimstack.readthedocs.io/en/latest/quick_start/integrations.html#integration-with-lightgbm)._
 </details>
 
+Read the full documentation on [aimstack.readthedocs.io](https://aimstack.readthedocs.io) 📖
+
+# 🆚 Comparisons to familiar tools
 
 <details>
 <summary>
-  Integrate PyTorch Ignite
+  <strong>TensorBoard vs Aim</strong>
 </summary>
 
-```python
-from aim.pytorch_ignite import AimLogger
-
-# ...
-aim_logger = AimLogger()
-
-aim_logger.log_params({
-    "model": model.__class__.__name__,
-    "pytorch_version": str(torch.__version__),
-    "ignite_version": str(ignite.__version__),
-})
-
-aim_logger.attach_output_handler(
-    trainer,
-    event_name=Events.ITERATION_COMPLETED,
-    tag="train",
-    output_transform=lambda loss: {'loss': loss}
-)
-# ...
-```
-
-_See documentation [here](https://aimstack.readthedocs.io/en/latest/quick_start/integrations.html#integration-with-pytorch-ignite)._
-</details>
-
-# Comparisons to familiar tools
+</br>
 
-### Tensorboard
 **Training run comparison**
 
 Order of magnitude faster training run comparison with Aim
 - The tracked params are first class citizens at Aim. You can search, group, aggregate via params - deeply explore all the tracked data (metrics, params, images) on the UI.
 - With tensorboard the users are forced to record those parameters in the training run name to be able to search and compare. This causes a super-tedius comparison experience and usability issues on the UI when there are many experiments and params. **TensorBoard doesn't have features to group, aggregate the metrics**
 
 **Scalability**
@@ -376,49 +355,117 @@
 - TensorBoard becomes really slow and hard to use when a few hundred training runs are queried / compared.
 
 **Beloved TB visualizations to be added on Aim**
 
 - Embedding projector.
 - Neural network visualization.
 
-### MLFlow
+</details>
+
+<details>
+<summary>
+  <strong>MLflow vs Aim</strong>
+</summary>
+
+</br>
+
 MLFlow is an end-to-end ML Lifecycle tool.
 Aim is focused on training tracking.
 The main differences of Aim and MLflow are around the UI scalability and run comparison features.
 
+Aim and MLflow are a perfect match - check out the [aimlflow](https://github.com/aimhubio/aimlflow) - the tool that enables Aim supoerpowers on Mlflow.
+
 **Run comparison**
 
 - Aim treats tracked parameters as first-class citizens. Users can query runs, metrics, images and filter using the params.
 - MLFlow does have a search by tracked config, but there are no grouping, aggregation, subplotting by hyparparams and other comparison features available.
 
 **UI Scalability**
 
 - Aim UI can handle several thousands of metrics at the same time smoothly with 1000s of steps. It may get shaky when you explore 1000s of metrics with 10000s of steps each. But we are constantly optimizing!
 - MLflow UI becomes slow to use when there are a few hundreds of runs.
 
-### Weights and Biases
+</details>
+
+<details>
+<summary>
+  <strong>Weights and Biases vs Aim</strong>
+</summary>
+
+</br>
 
 Hosted vs self-hosted
+
 - Weights and Biases is a hosted closed-source MLOps platform.
 - Aim is self-hosted, free and open-source experiment tracking tool.
 
-# Roadmap
+</details>
+
+# 🛣️ Roadmap
 
-## Detailed Sprints
+## Detailed milestones
 
-:sparkle: The [Aim product roadmap](https://github.com/orgs/aimhubio/projects/3)
+The [Aim product roadmap](https://github.com/orgs/aimhubio/projects/3) :sparkle: 
 
 - The `Backlog` contains the issues we are going to choose from and prioritize weekly
 - The issues are mainly prioritized by the highly-requested features
 
 ## High-level roadmap
 
-The high-level features we are going to work on the next few months
+The high-level features we are going to work on the next few months:
+
+**In progress**
+
+- [ ] Aim SDK low-level interface
+- [ ] Dashboards – customizable layouts with embedded explorers
+- [ ] Ergonomic UI kit
+- [ ] Text Explorer
+
+<details>
+<summary>
+  <strong>Next-up</strong>
+</summary>
+
+</br>
+
+**Aim UI**
+
+- Runs management
+    - Runs explorer – query and visualize runs data(images, audio, distributions, ...) in a central dashboard
+- Explorers
+    - Distributions Explorer
+
+**SDK and Storage**
+
+- Scalability
+    - Smooth UI and SDK experience with over 10.000 runs
+- Runs management
+    - CLI commands
+        - Reporting - runs summary and run details in a CLI compatible format
+        - Manipulations – copy, move, delete runs, params and sequences
+- Cloud storage support – store runs blob(e.g. images) data on the cloud
+- Artifact storage – store files, model checkpoints, and beyond
+
+**Integrations**
+
+- ML Frameworks:
+    - Shortlist: scikit-learn
+- Resource management tools
+    - Shortlist: Kubeflow, Slurm
+- Workflow orchestration tools
+
+</details>
+
+<details>
+<summary>
+  <strong>Done</strong>
+</summary>
+
+</br>
 
-### Done
   - [x] Live updates (Shipped: _Oct 18 2021_)
   - [x] Images tracking and visualization (Start: _Oct 18 2021_, Shipped: _Nov 19 2021_)
   - [x] Distributions tracking and visualization (Start: _Nov 10 2021_, Shipped: _Dec 3 2021_)
   - [x] Jupyter integration (Start: _Nov 18 2021_, Shipped: _Dec 3 2021_)
   - [x] Audio tracking and visualization (Start: _Dec 6 2021_, Shipped: _Dec 17 2021_)
   - [x] Transcripts tracking and visualization (Start: _Dec 6 2021_, Shipped: _Dec 17 2021_)
   - [x] Plotly integration (Start: _Dec 1 2021_, Shipped: _Dec 17 2021_)
@@ -446,54 +493,58 @@
   - [x] Integration with MXNet (Start: _Sep 20 2022_, Shipped: _Oct 6 2022_)
   - [x] Project overview page (Start: _Sep 1 2022_, Shipped: _Oct 6 2022_)
   - [x] Remote tracking server scaling (Start: _Sep 11 2022_, Shipped: _Nov 26 2022_)
   - [x] Integration with PaddlePaddle (Start: _Oct 2 2022_, Shipped: _Nov 26 2022_)
   - [x] Integration with Optuna (Start: _Oct 2 2022_, Shipped: _Nov 26 2022_)
   - [x] Audios Explorer (Start: _Oct 30 2022_, Shipped: _Nov 26 2022_)
   - [x] Experiment page (Start: _Nov 9 2022_, Shipped: _Nov 26 2022_)
+  - [x] HuggingFace datasets (Start: _Dec 29 2022_, _Feb 3 2023_)
 
-### In Progress
-  - [ ] Aim SDK low-level interface (Start: _Aug 22 2022_, )
-  - [ ] HuggingFace datasets (Start: _Dec 29 2022_, )
+</details>
 
-### To Do
+# 👥 Community
 
-**Aim UI**
+## Aim README badge
 
-- Runs management
-    - Runs explorer – query and visualize runs data(images, audio, distributions, ...) in a central dashboard
-- Explorers
-    - Text Explorer
-    - Distributions Explorer
-- Dashboards – customizable layouts with embedded explorers
+Add Aim badge to your README, if you've enjoyed using Aim in your work:
 
-**SDK and Storage**
+[![Aim](https://img.shields.io/badge/powered%20by-Aim-%231473E6)](https://github.com/aimhubio/aim)
 
-- Scalability
-    - Smooth UI and SDK experience with over 10.000 runs
-- Runs management
-    - CLI interfaces
-        - Reporting - runs summary and run details in a CLI compatible format
-        - Manipulations – copy, move, delete runs, params and sequences
+```
+[![Aim](https://img.shields.io/badge/powered%20by-Aim-%231473E6)](https://github.com/aimhubio/aim)
+```
 
-**Integrations**
+## Cite Aim in your papers
 
-- ML Frameworks:
-    - Shortlist: MONAI, SpaCy, Raytune
-- Resource management tools
-    - Shortlist: Kubeflow, Slurm
-- Workflow orchestration tools
-- Others: Hydra, Google MLMD, Streamlit, ...
+In case you've found Aim helpful in your research journey, we'd be thrilled if you could acknowledge Aim's contribution:
+
+```bibtex
+@software{Arakelyan_Aim_2020,
+  author = {Arakelyan, Gor and Soghomonyan, Gevorg and {The Aim team}},
+  doi = {10.5281/zenodo.6536395},
+  license = {Apache-2.0},
+  month = {6},
+  title = {{Aim}},
+  url = {https://github.com/aimhubio/aim},
+  version = {3.9.3},
+  year = {2020}
+}
+```
+
+## Contributing to Aim
+
+Considering contibuting to Aim? 
+To get started, please take a moment to read the [CONTRIBUTING.md](https://github.com/aimhubio/aim/blob/main/CONTRIBUTING.md) guide. 
 
-### On hold
+Join Aim contributors by submitting your first pull request. Happy coding! 😊
 
-- scikit-learn integration
-- Cloud storage support – store runs blob(e.g. images) data on the cloud (Start: _Mar 21 2022_)
-- Artifact storage – store files, model checkpoints, and beyond (Start: _Mar 21 2022_)
+<a href="https://github.com/aimhubio/aim/graphs/contributors">
+  <img src="https://contrib.rocks/image?repo=aimhubio/aim" />
+</a>
 
-## Community
+Made with [contrib.rocks](https://contrib.rocks).
 
-### If you have questions
+## More questions?
 
 1. [Read the docs](https://aimstack.readthedocs.io/en/latest/)
 2. [Open a feature request or report a bug](https://github.com/aimhubio/aim/issues)
 3. [Join Discord community server](https://community.aimstack.io/)
```

#### html2text {}

```diff
@@ -1,210 +1,261 @@
- [https://user-images.githubusercontent.com/13848158/154338760-edfe1885-06f3-
-                          4e02-87fe-4b13a403516b.png]
+                               Join_Aim_discord_community [https://user-
+Drop a star to support Aim â­images.githubusercontent.com/13848158/226759622-
+                               063b725d-8b3e-4c75-80c7-11fb04b7adf5.png]
+ [https://user-images.githubusercontent.com/13848158/225620298-9f9293e9-a138-
+                          41fd-bd77-21d53d0490b7.png]
     **** An easy-to-use & supercharged open-source experiment tracker ****
-Aim logs your training runs, enables a beautiful UI to compare them and an API
-                        to query them programmatically.
+  Aim logs your training runs and any AI Metadata, enables a beautiful UI to
+       compare, observe them and an API to query them programmatically.
 
-[https://user-images.githubusercontent.com/13848158/154338753-34484cda-95b8-
-4da8-a610-7fdf198c05fd.png]
- About • Features • Demos • Examples • Quick_Start • Documentation • Roadmap •
-                          Discord_Community • Twitter
-[![Platform Support](https://img.shields.io/badge/platform-Linux%20%7C%20macOS-
-blue)]() [![PyPI - Python Version](https://img.shields.io/pypi/pyversions/aim)]
-(https://pypi.org/project/aim/) [![PyPI Package](https://img.shields.io/pypi/v/
-    aim?color=yellow)](https://pypi.org/project/aim/) [![License](https://
-img.shields.io/badge/License-Apache%202.0-orange.svg)](https://opensource.org/
-    licenses/Apache-2.0) [![PyPI Downloads](https://img.shields.io/pypi/dw/
-     aim?color=green)](https://pypi.org/project/aim/) [![Issues](https://
-  img.shields.io/github/issues/aimhubio/aim)](http://github.com/aimhubio/aim/
-                                    issues)
-                Integrates seamlessly with your favorite tools
-
- [https://user-images.githubusercontent.com/13848158/155354389-d0301620-77ea-
-    4629-a743-f7aa249e14b5.png] [https://user-images.githubusercontent.com/
-  13848158/155354496-b39d7b1c-63ef-40f0-9e59-c08d2c5e337c.png] [https://user-
-   images.githubusercontent.com/13848158/155354380-3755c741-6960-42ca-b93e-
-    84a8791f088c.png] [https://user-images.githubusercontent.com/13848158/
-      155354342-7df0ef5e-63d2-4df7-b9f1-d2fc0e95f53f.png] [https://user-
-   images.githubusercontent.com/13848158/155354392-afbff3de-c845-4d86-855d-
-    53df569f91d1.png] [https://user-images.githubusercontent.com/13848158/
-      155354355-89210506-e7e5-4d37-b2d6-ad3fda62ef13.png] [https://user-
-   images.githubusercontent.com/13848158/155354397-8af8e1d3-4067-405e-9d42-
-                              1f131663ed22.png]
- [https://user-images.githubusercontent.com/13848158/155354513-f7486146-3891-
-    4f3f-934f-e58bbf9ce695.png] [https://user-images.githubusercontent.com/
-  13848158/155354500-c0471ce6-b2ce-4172-b9e4-07a197256303.png] [https://user-
-   images.githubusercontent.com/13848158/155354361-9f911785-008d-4b75-877e-
-    651e026cf47e.png] [https://user-images.githubusercontent.com/13848158/
-      155354373-1879ae61-b5d1-41f0-a4f1-04b639b6f05e.png] [https://user-
-   images.githubusercontent.com/13848158/155354483-75d9853f-7154-4d95-8190-
-    9ad7a73d6654.png] [https://user-images.githubusercontent.com/13848158/
-      155354329-cf7c3352-a72a-478d-82a7-04e3833b03b7.png] [https://user-
-   images.githubusercontent.com/13848158/155354349-dcdf3bc3-d7a9-4f34-8258-
-    4824a57f59c7.png] [https://user-images.githubusercontent.com/13848158/
-      155354471-518f1814-7a41-4b23-9caf-e516507343f1.png] [https://user-
-   images.githubusercontent.com/48801049/165162736-2cc5da39-38aa-4093-874f-
-    e56d0ba9cea2.png] [https://user-images.githubusercontent.com/48801049/
-              165074282-36ad18eb-1124-434d-8439-728c22cd7ac7.png]
+           [![Discord Server](https://dcbadge.vercel.app/api/server/
+zXq2NfVdtF?compact=true&style=flat)](https://community.aimstack.io/) [![Twitter
+Follow](https://img.shields.io/twitter/follow/aimstackio?style=social)](https:/
+   /twitter.com/aimstackio) [![Medium](https://img.shields.io/badge/Medium-
+12100E?style=flat&logo=medium&logoColor=white)](https://medium.com/aimstack) [!
+ [Platform Support](https://img.shields.io/badge/platform-Linux%20%7C%20macOS-
+    blue)]() [![PyPI - Python Version](https://img.shields.io/badge/python-
+ %3E%3D%203.7-blue)](https://pypi.org/project/aim/) [![PyPI Package](https://
+  img.shields.io/pypi/v/aim?color=yellow)](https://pypi.org/project/aim/) [!
+[License](https://img.shields.io/badge/License-Apache%202.0-orange.svg)](https:
+       //opensource.org/licenses/Apache-2.0) [![PyPI Downloads](https://
+  img.shields.io/pypi/dw/aim?color=green)](https://pypi.org/project/aim/) [!
+[Issues](https://img.shields.io/github/issues/aimhubio/aim)](http://github.com/
+                             aimhubio/aim/issues)
 
  [https://user-images.githubusercontent.com/13848158/136374529-af267918-5dc6-
                           4a4e-8ed2-f6333a332f96.gif]
-# About Aim | Track and version ML runs | Visualize runs via beautiful UI |
-Query runs metadata via SDK | |:--------------------:|:-----------------------
--:|:-------------------:| | [https://user-images.githubusercontent.com/
-13848158/154337794-e9310239-6614-41b3-a95b-bb91f0bb6c4f.png] | [https://user-
-images.githubusercontent.com/13848158/154337788-03fe5b31-0fa3-44af-ae79-
-2861707d8602.png] | [https://user-images.githubusercontent.com/13848158/
-154337793-85175c78-5659-4dd0-bb2d-05017278e2fa.png] | Aim is an open-source,
-self-hosted ML experiment tracking tool. It's good at tracking lots (1000s) of
-training runs and it allows you to compare them with a performant and beautiful
-UI. You can use not only the great Aim UI but also its SDK to query your runs'
-metadata programmatically. That's especially useful for automations and
-additional analysis on a Jupyter Notebook. Aim's mission is to democratize AI
-dev tools. # Why use Aim? ### Compare 100s of runs in a few clicks - build
-models faster - Compare, group and aggregate 100s of metrics thanks to
-effective visualizations. - Analyze, learn correlations and patterns between
-hparams and metrics. - Easy pythonic search to query the runs you want to
-explore. ### Deep dive into details of each run for easy debugging -
-Hyperparameters, metrics, images, distributions, audio, text - all available at
-hand on an intuitive UI to understand the performance of your model. - Easily
-track plots built via your favourite visualisation tools, like plotly and
-matplotlib. - Analyze system resource usage to effectively utilize
-computational resources. ### Have all relevant information organised and
-accessible for easy governance - Centralized dashboard to holistically view all
-your runs, their hparams and results. - Use SDK to query/access all your runs
-and tracked metadata. - You own your data - Aim is open source and self hosted.
-# Demos | Machine translation | lightweight-GAN | |:---:|:---:| | [https://
-user-images.githubusercontent.com/13848158/154340796-c9e91b13-8ee0-4a67-bcde-
-8cf3aaa7ba99.jpg] | [https://user-images.githubusercontent.com/13848158/
-154340790-bc7b7a21-e8a1-43a1-809d-4060b5bfb60f.jpg] | | Training logs of a
-neural translation model(from WMT'19 competition). | Training logs of
-'lightweight' GAN, proposed in ICLR 2021. | | FastSpeech 2 | Simple MNIST | |:-
---:|:---:| | [https://user-images.githubusercontent.com/13848158/154340778-
-dbe19620-2f27-4298-b0cb-caf3904760f1.jpg] | [https://user-
-images.githubusercontent.com/13848158/154340785-a7e4d9fd-d048-4207-8cd1-
-c4edff9cca6a.jpg] | | Training logs of Microsoft's "FastSpeech 2: Fast and
-High-Quality End-to-End Text to Speech". | Simple MNIST training logs. | #
-Quick Start Follow the steps below to get started with Aim. **1. Install Aim on
-your training environment** ```shell pip3 install aim ``` **2. Integrate Aim
-with your code** ```python from aim import Run # Initialize a new run run = Run
-() # Log run parameters run["hparams"] = { "learning_rate": 0.001,
+                         SEAMLESSLY INTEGRATES WITH:
+
+ [https://user-images.githubusercontent.com/97726819/225954732-2b263308-8ed8-
+    4df3-810b-704840328e98.png] [https://user-images.githubusercontent.com/
+  97726819/225954727-04eccf0e-51ed-4f2d-8f3b-c9a675ca8e8f.png] [https://user-
+   images.githubusercontent.com/97726819/225954728-ca2f498d-51a7-487b-bd69-
+    ffb5f0c2af58.png] [https://user-images.githubusercontent.com/97726819/
+      225954689-1076998c-42f4-4e31-ab47-d9f39575fda1.png] [https://user-
+   images.githubusercontent.com/97726819/225954739-0231d659-3202-4458-9c35-
+    ba92d1f079b8.png] [https://user-images.githubusercontent.com/97726819/
+      225954697-ef2c7091-b089-4b68-8543-80ce7275b683.png] [https://user-
+   images.githubusercontent.com/97726819/225954743-dbfe1e98-7b9f-446a-9fe4-
+    ad4fd562f3df.png] [https://user-images.githubusercontent.com/97726819/
+      225954736-7c52ab5a-6780-4375-a6f8-b394dae3ad31.png] [https://user-
+   images.githubusercontent.com/97726819/225954710-36551a71-b26d-4665-af20-
+    44ee452dd5dd.png] [https://user-images.githubusercontent.com/97726819/
+      225954707-4bc078b5-ae6f-4847-bc2c-3f81959accb2.png] [https://user-
+   images.githubusercontent.com/97726819/225954725-a4d4c32c-75db-470a-b1da-
+    698982faa23c.png] [https://user-images.githubusercontent.com/97726819/
+      225954665-8d844747-a857-41b8-9104-7c27a8bdb81a.png] [https://user-
+   images.githubusercontent.com/97726819/225954686-b9c8ec57-d4fc-44e1-a4b8-
+    443db381a00f.png] [https://user-images.githubusercontent.com/97726819/
+      225954693-94bc20b4-f51a-4130-8d5f-ddee30d81205.png] [https://user-
+   images.githubusercontent.com/97726819/225954674-42fbfdb3-0351-492d-9ea3-
+    1d3ab2b545f5.png] [https://user-images.githubusercontent.com/97726819/
+      225954678-25f1b626-2cb1-4e7e-ad83-f7c8ab679c6f.png] [https://user-
+   images.githubusercontent.com/97726819/225954702-d18d2706-dc87-4e09-a678-
+                               f010f6d95736.png]
+
+                          TRUSTED BY ML TEAMS FROM:
+
+ [https://user-images.githubusercontent.com/97726819/225952594-a21546f4-987f-
+    42bd-9154-c22b50632b55.png] [https://user-images.githubusercontent.com/
+  97726819/225953224-291fbb6d-e31a-4e36-90ba-92a1dc20bacc.png] [https://user-
+   images.githubusercontent.com/97726819/225953339-4fcc3c99-dda2-4529-ac2a-
+    29c8293be323.png] [https://user-images.githubusercontent.com/97726819/
+      225953084-1d88325a-ad5f-49eb-aa67-f064c4b9f39c.png] [https://user-
+   images.githubusercontent.com/97726819/225952955-397e0f26-f01e-4b25-bd70-
+    9f292a6f77c2.png] [https://user-images.githubusercontent.com/97726819/
+      225952682-a843827b-e870-429d-96d8-3b4fd45471cd.png] [https://user-
+   images.githubusercontent.com/97726819/225952831-1c0e36aa-4120-4635-ab4e-
+    bf1bc685477b.png] [https://user-images.githubusercontent.com/97726819/
+              225953432-4b27653a-aa12-4fbf-897c-01349afa2ad0.png]
+
+    AimStack offers enterprise support that's beyond core Aim. Contact via
+                           hello@aimstack.io e-mail.
+---
+   **** About • Demos • Ecosystem • Quick_Start • Examples • Documentation •
+                             Community • Blog ****
+--- # â¹ï¸ About Aim is an open-source, self-hosted ML experiment tracking
+tool designed to handle 10,000s of training runs. Aim provides a performant and
+beautiful UI for exploring and comparing training runs. Additionally, its SDK
+enables programmatic access to tracked metadata â perfect for automations and
+Jupyter Notebook analysis.
+               Aim's mission is to democratize AI dev tools ð¯
+ [https://user-images.githubusercontent.com/13848158/226426018-f7c11c9b-78d9-
+    4ee4-b292-df28b3e8eaa6.jpg] [https://user-images.githubusercontent.com/
+  13848158/226426005-f7e83923-0f92-44a4-88e4-1735a3d3e119.jpg] [https://user-
+   images.githubusercontent.com/13848158/226426015-4f1122d8-c96a-443f-8698-
+                               3db942b1972a.jpg]
+Log Metadata Across Your ML Pipeline  Visualize & Compare Metadata via UI ð
+ð¾
+    * ML experiments and any metadata
+      tracking                            * Metadata visualization via Aim
+    * Integration with popular ML           Explorers
+      frameworks                          * Grouping and aggregation
+    * Easy migration from other           * Querying using Python expressions
+      experiment trackers
+Run ML Trainings Effectively â¡   Organize Your Experiments ðï¸
+    * System info and resource usage      * Detailed run information for easy
+      tracking                              debugging
+    * Real-time alerting on training      * Centralized dashboard for holistic
+      progress                              view
+    * Logging and configurable            * Runs grouping with tags and
+      notifications                         experiments
+# ð¬ Demos Check out live Aim demos NOW to see it in action. | [Machine
+translation experiments](http://play.aimstack.io:10001/
+metrics?grouping=HQGdK9Xxy35e6sY1CYkCmk1WbWMN2AsCNfJJ3d1RJYLtrVPMoF5UpGiA6CF8bEJnfzRsKpqespf3AEuKSVrhUYvYk9MxzNGA9XZWYUf6phEg8AMbZGLRVDXnAPDuo8tueqsST1ZLizWzQwDYJWHUza6pyB2Eojt9uWqNHUdb858TqDRnCJzqiVJXKXEzFWUyvU8MckJo1qpqWWCTb4GpYN6DUJZx2GXDGR21e2xxd4m7PmNUnbA9B3apLttZoipJF6c3v7tNUKmb6irpqnNB3yc57tqYDa1XZuKfDxkMtyFdQ1x95K4jjsTVwhftEWLze35QNcxNXRCGGS9o9yEfTLG26GUX2zjPZFCjjMGU6vV7z1xRccK8MyoGrLSgAQCbvk68dTGBHpXUBvCRq8N&chart=FviZzVrt4fVQPjpCLr9sVGGrcR5etSroyqambiKpm3nTgpyv4eQxKuwNX9uN8UtKmzYUhUyTMBEANHmtbwjLApkvnYeNbxGNC6PVcoqi65m1XJnSrvgt8WiD89BapFAWRUwAGx6SWD7KZPsk3RQyysU7W7FjD3Q99NusxFGhsEfD6HXc7i8xH9KHDRGjLwh6x9VTtSp4FS8HEvpLSiiJoX7LCTi8pB7dXvrQ8G5w3jPsFz4qXYFdsVaCNL1BpFFZuiqQNkfbnM84gEq7UmiV1VzM4oS3AgQHxADG3kpBVp6eKTey9F1Swd4FcUkFA9QEPjgQgqwRGjkquZ2bdDDVLBnCh7JPvboP2kifCiZZ5MDdV9MMx6PKHp4DusWyWLXiHQYPkpGPWBiuccMUXDsuJaCWJbuABdY7CyiJMv1jdHYkjabygSxehPVyEDefWAtjBfv2vaeM1xv63jadbmpKYFxft7qmuT9HvVxiGvRgs4RQFxy8K4rtFBca3HNs1mDaaY81gy9MGXyw7BS5Fniu92jaJpsWDdg6Y3AQBLZtrpJy2obEZ4yzJaCVT7JUNPAyyCUNLck393VFLoEkaD9CU5npK5R7tj1c1G3gkMNQXnSXy5NpSj8deMmXV5qz3JKu1nq2caGQKcqjzy2gLkExdm674AMFjSg9yFjK6VqASXQ17NKtWRUvaYoxGbHDAFQaMKWKh8QLm22QA9mKT8NksLptWozbgDvafnQLNMvezLU5bvKV5o75PAWYiRB56RcYfEhzaB6YWdgL7TJicyY5rFi6Az8UZ7wqB3N5iMuZdpxhKn5KbZDxyuUMuvVt24i5LVPPmmwQtqxMoJ4aLo48a2YvDW6TAkdQjNjvn6KcEEz6GTixujb1YHhMUD8v4AepWKEwKz1ddEca1P2wLQjbpihCuaqbxeohnuZZLogJdUBojBEDgrnrrVpPBaLLEkGSpkJbtrsKUuEeBo1AF3yNgHftLbynGpobVF5DhmsmddmiA6c8vSTokJxHhjpnW8mAcNHBRtmVJCT7VkdHSAhNypM4Hivwfx5jCccG9LauKmCeRMDzHiA57TX9W6ttcPHSvUyQorARQAd2oeNY4H83hZjHh9Bt8iwKZRt4xK6hrTR8tif7hq8eURXrGH9Ys7TzykXK8FHHWvLNzNnYf3E4a9NkD43MjfKvMM1hj4Q2K8MHbmRCqrmFrHP5kim9shq6mhLPTgwha32nvnrBkfPQVPwpGTzKuwE&select=CdsQ7jVNkogQhRzQR3e28Ek39AZ4Ma2y37k5zJaf9EZmQhMjy8GtGm4LGU6dRFuAVG7mYww5xDrQAE74KHQ3Kk1e6661RmcmNALAUjtHyCmrTVBMCnBGNiuq1y7EzmxoodYHU1BV1rnoefQAw2kTBtbWi11hV1P4LcwFCcXfUWF6rpRC7ehEnUCTqUV4bkGVJPLcmk9mdmiGwa2YgmnSShNGPVGZiEi1rMVECyngSRVdqdZwAeXBGWFLfqF1KbZeCo4MTF4SSmFupJ9zLhYbuojEbopyFWHQ6xs3sq9epPeaQziLM4Js7oFYRmuFWUYdFqnZngmewXWmi7tQAgVqhiT6dMjG2eTdfgX6WuRSuoHALkh2XJhHA6GfZLUcxC5Ni9YyKuBTamtaYarbNNJJ8z15WWvuUkLpjgHdEpE2h924xFdu8aoZNuiQxYGvcndaW1BTGMXS5fTKPqYfe2n8Ky2HWPkcX3hEXtyawu1F9BndKNaXLPgsdAoFBArBZnSe28YtSmTa5LRucKVBAxakvv5MWMXchAmpaGFQbZyYUoMgQLcJd7Y96x6zSR7nhwr5Ar81BrmqYz2WFLuk7osUbwsc9HbSG6CQt8p6Vg2u7DjKaZXW8pjkPHAKrHWtHEDiJPJ5rj6VsdFm3)
+| [lightweight-GAN experiments](http://play.aimstack.io:10002/
+images?grouping=E1zQzcmtDR3wibEa1MVysTvCyZEv1T8ixkCxTWExCyMnHtX2HyiF9eszvPgfd2xdJ5TUTKGpSs1bsLVq5tHAV3uWtsZmmckn6HjNtVCMyQDJpwhiEy5tAyw&select=2NEXuD7fFoaLcwRjymjA1wLmUrGs9s3AiXcCW82C367SwJt18CAB6xzkMGowrUDuDwggE1huaPVcQJpQUsmAQx1CnGiqCUBp2jPMd5mMNPX2QKQMcmvu9ZykBNkeBvCQFPd9ERuQD2g1EjWuvyJ3H53mAZTfp94LCXvR9CUsG5ei2CjQUzfZLM6DCyUr1GPaEVnY5f1EwzicNxXuoutkBgqCqaobJ7Do4q4eHAA6ooiWU6ekS3D2sLj6qYwhVTjfGCPfbWwBiH83nFkY3fLExzdeTY2zeUHeeYikQR9S7xHbVD8WvjekdQVp8X4dNLJZxiVmEqHpPRnU3ZrYsMhE7yFAAgjJwPNUzLTt6YFrtZBcmc4rwAC2oyrqysUSEr6gzL6LcJ6yuqDGf9D5tzftHbTLDkhc8B2sCgTS&images=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)|
+|:---:|:---:| | [https://user-images.githubusercontent.com/97726819/225964524-
+0051c2c7-8554-43ae-82b8-adcb77bcf1ba.png] | [https://user-
+images.githubusercontent.com/97726819/225948275-a41946ea-89f4-45f1-bce1-
+251c84dcddca.png] | | Training logs of a neural translation model(from WMT'19
+competition). | Training logs of 'lightweight' GAN, proposed in ICLR 2021. | |
+[FastSpeech 2 experiments](http://play.aimstack.io:10004/runs/
+d9e89aa7875e44b2ba85612a/audios)| [Simple MNIST](http://play.aimstack.io:10003/
+runs/7f083da898624a2c98e0f363/distributions) | |:---:|:---:| | [https://user-
+images.githubusercontent.com/97726819/225948457-567526da-a329-4c53-a9a7-
+98dfe392d4c4.png] | [https://user-images.githubusercontent.com/97726819/
+225948599-ff39c5b7-ae7d-4deb-8bc9-5eee1e189d89.png] | | Training logs of
+Microsoft's "FastSpeech 2: Fast and High-Quality End-to-End Text to Speech". |
+Simple MNIST training logs. | # ð Ecosystem Aim is not just an experiment
+tracker. It's a groundwork for an ecosystem. Check out the two most famous Aim-
+based tools. | [aimlflow](https://github.com/aimhubio/aimlflow) | [Aim-spaCy]
+(https://github.com/aimhubio/aim-spacy) | |:---:|:---:| | ![aimlflow](https://
+user-images.githubusercontent.com/97726819/225957836-cdec88e3-4993-435a-a135-
+d78be3ac1635.png) | ![Aim-spaCy](https://user-images.githubusercontent.com/
+97726819/225957990-4edc4525-1f65-4405-b663-ce7af888bdfa.png) | | Exploring
+MLflow experiments with a powerful UI | an Aim-based spaCy experiment tracker |
+# ð Quick start Follow the steps below to get started with Aim. ## 1.
+Install Aim on your training environment ```shell pip3 install aim ``` ## 2.
+Integrate Aim with your code ```python from aim import Run # Initialize a new
+run run = Run() # Log run parameters run["hparams"] = { "learning_rate": 0.001,
 "batch_size": 32, } # Log metrics for i in range(10): run.track(i, name='loss',
 step=i, context={ "subset":"train" }) run.track(i, name='acc', step=i, context=
 { "subset":"train" }) ``` _See the full list of supported trackable objects
 (e.g. images, text, etc) [here](https://aimstack.readthedocs.io/en/latest/
-quick_start/supported_types.html)._ **3. Run the training as usual and start
-Aim UI** ```shell aim up ``` **4. Or query runs programmatically via SDK**
-```python from aim import Repo my_repo = Repo('/path/to/aim/repo') query =
-"metric.name == 'loss'" # Example query # Get collection of metrics for
-run_metrics_collection in my_repo.query_metrics(query).iter_runs(): for metric
-in run_metrics_collection: # Get run params params = metric.run[...] # Get
-metric values steps, metric_values = metric.values.sparse_numpy() ``` #
-Integrations   Integrate PyTorch Lightning  ```python from
-aim.pytorch_lightning import AimLogger # ... trainer = pl.Trainer
-(logger=AimLogger(experiment='experiment_name')) # ... ``` _See documentation
-[here](https://aimstack.readthedocs.io/en/latest/quick_start/
-integrations.html#integration-with-pytorch-lightning)._    Integrate Hugging
-Face  ```python from aim.hugging_face import AimCallback # ... aim_callback =
-AimCallback(repo='/path/to/logs/dir', experiment='mnli') trainer = Trainer
-( model=model, args=training_args, train_dataset=train_dataset if
-training_args.do_train else None, eval_dataset=eval_dataset if
-training_args.do_eval else None, callbacks=[aim_callback], # ... ) # ... ```
-_See documentation [here](https://aimstack.readthedocs.io/en/latest/
-quick_start/integrations.html#integration-with-hugging-face)._    Integrate
-Keras & tf.keras  ```python import aim # ... model.fit(x_train, y_train,
-epochs=epochs, callbacks=[ aim.keras.AimCallback(repo='/path/to/logs/dir',
-experiment='experiment_name') # Use aim.tensorflow.AimCallback in case of
-tf.keras aim.tensorflow.AimCallback(repo='/path/to/logs/dir',
-experiment='experiment_name') ]) # ... ``` _See documentation [here](https://
-aimstack.readthedocs.io/en/latest/quick_start/integrations.html#integration-
-with-keras-tf-keras)._    Integrate KerasTuner  ```python from aim.keras_tuner
-import AimCallback # ... tuner.search( train_ds, validation_data=test_ds,
-callbacks=[AimCallback(tuner=tuner, repo='.', experiment='keras_tuner_test')],
-) # ... ``` _See documentation [here](https://aimstack.readthedocs.io/en/
-latest/quick_start/integrations.html#integration-with-kerastuner)._
-Integrate XGBoost  ```python from aim.xgboost import AimCallback # ...
-aim_callback = AimCallback(repo='/path/to/logs/dir',
-experiment='experiment_name') bst = xgb.train(param, xg_train, num_round,
-watchlist, callbacks=[aim_callback]) # ... ``` _See documentation [here](https:
+quick_start/supported_types.html)._ ## 3. Run the training as usual and start
+Aim UI ```shell aim up ``` ## Learn more   Migrate from other tools   Aim has
+built-in converters to easily migrate logs from other tools. These migrations
+cover the most common usage scenarios. In case of custom and complex scenarios
+you can use Aim SDK to implement your own conversion script. - [TensorBoard
+logs converter](https://aimstack.readthedocs.io/en/latest/quick_start/
+convert_data.html#show-tensorboard-logs-in-aim) - [MLFlow logs converter]
+(https://aimstack.readthedocs.io/en/latest/quick_start/convert_data.html#show-
+mlflow-logs-in-aim) - [Weights & Biases logs converter](https://
+aimstack.readthedocs.io/en/latest/quick_start/convert_data.html#show-weights-
+and-biases-logs-in-aim)    Integrate Aim into an existing project   Aim easily
+integrates with a wide range of ML frameworks, providing built-in callbacks for
+most of them. - [Integration with Pytorch Ignite](https://
+aimstack.readthedocs.io/en/latest/quick_start/integrations.html#integration-
+with-pytorch-ignite) - [Integration with Pytorch Lightning](https://
+aimstack.readthedocs.io/en/latest/quick_start/integrations.html#integration-
+with-pytorch-lightning) - [Integration with Hugging Face](https://
+aimstack.readthedocs.io/en/latest/quick_start/integrations.html#integration-
+with-hugging-face) - [Integration with Keras & tf.Keras](https://
+aimstack.readthedocs.io/en/latest/quick_start/integrations.html#integration-
+with-keras-tf-keras) - [Integration with Keras Tuner](https://
+aimstack.readthedocs.io/en/latest/quick_start/integrations.html#integration-
+with-keras-tuner) - [Integration with XGboost](https://aimstack.readthedocs.io/
+en/latest/quick_start/integrations.html#integration-with-xgboost) -
+[Integration with CatBoost](https://aimstack.readthedocs.io/en/latest/
+quick_start/integrations.html#integration-with-catboost) - [Integration with
+LightGBM](https://aimstack.readthedocs.io/en/latest/quick_start/
+integrations.html#integration-with-lightgbm) - [Integration with fastai](https:
 //aimstack.readthedocs.io/en/latest/quick_start/integrations.html#integration-
-with-xgboost)._    Integrate CatBoost  ```python from aim.catboost import
-AimLogger # ... model.fit(train_data, train_labels, log_cout=AimLogger
-(loss_function='Logloss'), logging_level="Info") # ... ``` _See documentation
-[here](https://aimstack.readthedocs.io/en/latest/quick_start/
-integrations.html#integration-with-catboost)._    Integrate fastai  ```python
-from aim.fastai import AimCallback # ... learn = cnn_learner(dls, resnet18,
-pretrained=True, loss_func=CrossEntropyLossFlat(), metrics=accuracy,
-model_dir="/tmp/model/", cbs=AimCallback(repo='.', experiment='fastai_test')) #
-... ``` _See documentation [here](https://aimstack.readthedocs.io/en/latest/
-quick_start/integrations.html#integration-with-fastai)._    Integrate LightGBM
-```python from aim.lightgbm import AimCallback # ... aim_callback = AimCallback
-(experiment='lgb_test') aim_callback.experiment['hparams'] = params gbm =
-lgb.train(params, lgb_train, num_boost_round=20, valid_sets=lgb_eval,
-callbacks=[aim_callback, lgb.early_stopping(stopping_rounds=5)]) # ... ``` _See
-documentation [here](https://aimstack.readthedocs.io/en/latest/quick_start/
-integrations.html#integration-with-lightgbm)._    Integrate PyTorch Ignite
-```python from aim.pytorch_ignite import AimLogger # ... aim_logger = AimLogger
-() aim_logger.log_params({ "model": model.__class__.__name__,
-"pytorch_version": str(torch.__version__), "ignite_version": str
-(ignite.__version__), }) aim_logger.attach_output_handler( trainer,
-event_name=Events.ITERATION_COMPLETED, tag="train", output_transform=lambda
-loss: {'loss': loss} ) # ... ``` _See documentation [here](https://
-aimstack.readthedocs.io/en/latest/quick_start/integrations.html#integration-
-with-pytorch-ignite)._  # Comparisons to familiar tools ### Tensorboard
-**Training run comparison** Order of magnitude faster training run comparison
-with Aim - The tracked params are first class citizens at Aim. You can search,
-group, aggregate via params - deeply explore all the tracked data (metrics,
-params, images) on the UI. - With tensorboard the users are forced to record
-those parameters in the training run name to be able to search and compare.
-This causes a super-tedius comparison experience and usability issues on the UI
-when there are many experiments and params. **TensorBoard doesn't have features
-to group, aggregate the metrics** **Scalability** - Aim is built to handle
-1000s of training runs - both on the backend and on the UI. - TensorBoard
-becomes really slow and hard to use when a few hundred training runs are
-queried / compared. **Beloved TB visualizations to be added on Aim** -
-Embedding projector. - Neural network visualization. ### MLFlow MLFlow is an
-end-to-end ML Lifecycle tool. Aim is focused on training tracking. The main
+with-fastai) - [Integration with MXNet](https://aimstack.readthedocs.io/en/
+latest/quick_start/integrations.html#integration-with-mxnet) - [Integration
+with Optuna](https://aimstack.readthedocs.io/en/latest/quick_start/
+integrations.html#integration-with-optuna) - [Integration with PaddlePaddle]
+(https://aimstack.readthedocs.io/en/latest/quick_start/
+integrations.html#integration-with-paddlepaddle) - [Integration with Stable-
+Baselines3](https://aimstack.readthedocs.io/en/latest/quick_start/
+integrations.html#integration-with-stable-baselines3) - [Integration with Acme]
+(https://aimstack.readthedocs.io/en/latest/quick_start/
+integrations.html#integration-with-acme) - [Integration with Prophet](https://
+aimstack.readthedocs.io/en/latest/quick_start/integrations.html#integration-
+with-prophet)    Query runs programmatically via SDK   Aim Python SDK empowers
+you to query and access any piece of tracked metadata with ease. ```python from
+aim import Repo my_repo = Repo('/path/to/aim/repo') query = "metric.name ==
+'loss'" # Example query # Get collection of metrics for run_metrics_collection
+in my_repo.query_metrics(query).iter_runs(): for metric in
+run_metrics_collection: # Get run params params = metric.run[...] # Get metric
+values steps, metric_values = metric.values.sparse_numpy() ```    Set up a
+centralized tracking server   Aim remote tracking server allows running
+experiments in a multi-host environment and collect tracked data in a
+centralized location. See the docs on how to [set up the remote server](https:/
+/aimstack.readthedocs.io/en/latest/using/remote_tracking.html).    Deploy Aim
+on kubernetes   - The official Aim docker image: https://hub.docker.com/r/
+aimstack/aim - A guide on how to deploy Aim on kubernetes: https://
+aimstack.readthedocs.io/en/latest/using/k8s_deployment.html  Read the full
+documentation on [aimstack.readthedocs.io](https://aimstack.readthedocs.io)
+ð # ð Comparisons to familiar tools   TensorBoard vs Aim   **Training run
+comparison** Order of magnitude faster training run comparison with Aim - The
+tracked params are first class citizens at Aim. You can search, group,
+aggregate via params - deeply explore all the tracked data (metrics, params,
+images) on the UI. - With tensorboard the users are forced to record those
+parameters in the training run name to be able to search and compare. This
+causes a super-tedius comparison experience and usability issues on the UI when
+there are many experiments and params. **TensorBoard doesn't have features to
+group, aggregate the metrics** **Scalability** - Aim is built to handle 1000s
+of training runs - both on the backend and on the UI. - TensorBoard becomes
+really slow and hard to use when a few hundred training runs are queried /
+compared. **Beloved TB visualizations to be added on Aim** - Embedding
+projector. - Neural network visualization.    MLflow vs Aim   MLFlow is an end-
+to-end ML Lifecycle tool. Aim is focused on training tracking. The main
 differences of Aim and MLflow are around the UI scalability and run comparison
-features. **Run comparison** - Aim treats tracked parameters as first-class
+features. Aim and MLflow are a perfect match - check out the [aimlflow](https:/
+/github.com/aimhubio/aimlflow) - the tool that enables Aim supoerpowers on
+Mlflow. **Run comparison** - Aim treats tracked parameters as first-class
 citizens. Users can query runs, metrics, images and filter using the params. -
 MLFlow does have a search by tracked config, but there are no grouping,
 aggregation, subplotting by hyparparams and other comparison features
 available. **UI Scalability** - Aim UI can handle several thousands of metrics
 at the same time smoothly with 1000s of steps. It may get shaky when you
 explore 1000s of metrics with 10000s of steps each. But we are constantly
 optimizing! - MLflow UI becomes slow to use when there are a few hundreds of
-runs. ### Weights and Biases Hosted vs self-hosted - Weights and Biases is a
-hosted closed-source MLOps platform. - Aim is self-hosted, free and open-source
-experiment tracking tool. # Roadmap ## Detailed Sprints :sparkle: The [Aim
-product roadmap](https://github.com/orgs/aimhubio/projects/3) - The `Backlog`
-contains the issues we are going to choose from and prioritize weekly - The
-issues are mainly prioritized by the highly-requested features ## High-level
-roadmap The high-level features we are going to work on the next few months ###
-Done - [x] Live updates (Shipped: _Oct 18 2021_) - [x] Images tracking and
-visualization (Start: _Oct 18 2021_, Shipped: _Nov 19 2021_) - [x]
-Distributions tracking and visualization (Start: _Nov 10 2021_, Shipped: _Dec 3
-2021_) - [x] Jupyter integration (Start: _Nov 18 2021_, Shipped: _Dec 3 2021_)
-- [x] Audio tracking and visualization (Start: _Dec 6 2021_, Shipped: _Dec 17
-2021_) - [x] Transcripts tracking and visualization (Start: _Dec 6 2021_,
-Shipped: _Dec 17 2021_) - [x] Plotly integration (Start: _Dec 1 2021_, Shipped:
-_Dec 17 2021_) - [x] Colab integration (Start: _Nov 18 2021_, Shipped: _Dec 17
-2021_) - [x] Centralized tracking server (Start: _Oct 18 2021_, Shipped: _Jan
-22 2022_) - [x] Tensorboard adaptor - visualize TensorBoard logs with Aim
-(Start: _Dec 17 2021_, Shipped: _Feb 3 2022_) - [x] Track git info, env vars,
-CLI arguments, dependencies (Start: _Jan 17 2022_, Shipped: _Feb 3 2022_) - [x]
-MLFlow adaptor (visualize MLflow logs with Aim) (Start: _Feb 14 2022_, Shipped:
-_Feb 22 2022_) - [x] Activeloop Hub integration (Start: _Feb 14 2022_, Shipped:
-_Feb 22 2022_) - [x] PyTorch-Ignite integration (Start: _Feb 14 2022_, Shipped:
-_Feb 22 2022_) - [x] Run summary and overview info(system params, CLI args, git
-info, ...) (Start: _Feb 14 2022_, Shipped: _Mar 9 2022_) - [x] Add DVC related
-metadata into aim run (Start: _Mar 7 2022_, Shipped: _Mar 26 2022_) - [x]
-Ability to attach notes to Run from UI (Start: _Mar 7 2022_, Shipped: _Apr 29
-2022_) - [x] Fairseq integration (Start: _Mar 27 2022_, Shipped: _Mar 29 2022_)
-- [x] LightGBM integration (Start: _Apr 14 2022_, Shipped: _May 17 2022_) - [x]
+runs.    Weights and Biases vs Aim   Hosted vs self-hosted - Weights and Biases
+is a hosted closed-source MLOps platform. - Aim is self-hosted, free and open-
+source experiment tracking tool.  # ð£ï¸ Roadmap ## Detailed milestones The
+[Aim product roadmap](https://github.com/orgs/aimhubio/projects/3) :sparkle: -
+The `Backlog` contains the issues we are going to choose from and prioritize
+weekly - The issues are mainly prioritized by the highly-requested features ##
+High-level roadmap The high-level features we are going to work on the next few
+months: **In progress** - [ ] Aim SDK low-level interface - [ ] Dashboards â
+customizable layouts with embedded explorers - [ ] Ergonomic UI kit - [ ] Text
+Explorer   Next-up   **Aim UI** - Runs management - Runs explorer â query and
+visualize runs data(images, audio, distributions, ...) in a central dashboard -
+Explorers - Distributions Explorer **SDK and Storage** - Scalability - Smooth
+UI and SDK experience with over 10.000 runs - Runs management - CLI commands -
+Reporting - runs summary and run details in a CLI compatible format -
+Manipulations â copy, move, delete runs, params and sequences - Cloud storage
+support â store runs blob(e.g. images) data on the cloud - Artifact storage
+â store files, model checkpoints, and beyond **Integrations** - ML
+Frameworks: - Shortlist: scikit-learn - Resource management tools - Shortlist:
+Kubeflow, Slurm - Workflow orchestration tools    Done   - [x] Live updates
+(Shipped: _Oct 18 2021_) - [x] Images tracking and visualization (Start: _Oct
+18 2021_, Shipped: _Nov 19 2021_) - [x] Distributions tracking and
+visualization (Start: _Nov 10 2021_, Shipped: _Dec 3 2021_) - [x] Jupyter
+integration (Start: _Nov 18 2021_, Shipped: _Dec 3 2021_) - [x] Audio tracking
+and visualization (Start: _Dec 6 2021_, Shipped: _Dec 17 2021_) - [x]
+Transcripts tracking and visualization (Start: _Dec 6 2021_, Shipped: _Dec 17
+2021_) - [x] Plotly integration (Start: _Dec 1 2021_, Shipped: _Dec 17 2021_) -
+[x] Colab integration (Start: _Nov 18 2021_, Shipped: _Dec 17 2021_) - [x]
+Centralized tracking server (Start: _Oct 18 2021_, Shipped: _Jan 22 2022_) -
+[x] Tensorboard adaptor - visualize TensorBoard logs with Aim (Start: _Dec 17
+2021_, Shipped: _Feb 3 2022_) - [x] Track git info, env vars, CLI arguments,
+dependencies (Start: _Jan 17 2022_, Shipped: _Feb 3 2022_) - [x] MLFlow adaptor
+(visualize MLflow logs with Aim) (Start: _Feb 14 2022_, Shipped: _Feb 22 2022_)
+- [x] Activeloop Hub integration (Start: _Feb 14 2022_, Shipped: _Feb 22 2022_)
+- [x] PyTorch-Ignite integration (Start: _Feb 14 2022_, Shipped: _Feb 22 2022_)
+- [x] Run summary and overview info(system params, CLI args, git info, ...)
+(Start: _Feb 14 2022_, Shipped: _Mar 9 2022_) - [x] Add DVC related metadata
+into aim run (Start: _Mar 7 2022_, Shipped: _Mar 26 2022_) - [x] Ability to
+attach notes to Run from UI (Start: _Mar 7 2022_, Shipped: _Apr 29 2022_) - [x]
+Fairseq integration (Start: _Mar 27 2022_, Shipped: _Mar 29 2022_) - [x]
+LightGBM integration (Start: _Apr 14 2022_, Shipped: _May 17 2022_) - [x]
 CatBoost integration (Start: _Apr 20 2022_, Shipped: _May 17 2022_) - [x] Run
 execution details(display stdout/stderr logs) (Start: _Apr 25 2022_, Shipped:
 _May 17 2022_) - [x] Long sequences(up to 5M of steps) support (Start: _Apr 25
 2022_, Shipped: _Jun 22 2022_) - [x] Figures Explorer (Start: _Mar 1 2022_,
 Shipped: _Aug 21 2022_) - [x] Notify on stuck runs (Start: _Jul 22 2022_,
 Shipped: _Aug 21 2022_) - [x] Integration with KerasTuner (Start: _Aug 10
 2022_, Shipped: _Aug 21 2022_) - [x] Integration with WandB (Start: _Aug 15
@@ -213,25 +264,26 @@
 22 2022_, Shipped: _Oct 6 2022_) - [x] Integration with MXNet (Start: _Sep 20
 2022_, Shipped: _Oct 6 2022_) - [x] Project overview page (Start: _Sep 1 2022_,
 Shipped: _Oct 6 2022_) - [x] Remote tracking server scaling (Start: _Sep 11
 2022_, Shipped: _Nov 26 2022_) - [x] Integration with PaddlePaddle (Start: _Oct
 2 2022_, Shipped: _Nov 26 2022_) - [x] Integration with Optuna (Start: _Oct 2
 2022_, Shipped: _Nov 26 2022_) - [x] Audios Explorer (Start: _Oct 30 2022_,
 Shipped: _Nov 26 2022_) - [x] Experiment page (Start: _Nov 9 2022_, Shipped:
-_Nov 26 2022_) ### In Progress - [ ] Aim SDK low-level interface (Start: _Aug
-22 2022_, ) - [ ] HuggingFace datasets (Start: _Dec 29 2022_, ) ### To Do **Aim
-UI** - Runs management - Runs explorer â query and visualize runs data
-(images, audio, distributions, ...) in a central dashboard - Explorers - Text
-Explorer - Distributions Explorer - Dashboards â customizable layouts with
-embedded explorers **SDK and Storage** - Scalability - Smooth UI and SDK
-experience with over 10.000 runs - Runs management - CLI interfaces - Reporting
-- runs summary and run details in a CLI compatible format - Manipulations â
-copy, move, delete runs, params and sequences **Integrations** - ML Frameworks:
-- Shortlist: MONAI, SpaCy, Raytune - Resource management tools - Shortlist:
-Kubeflow, Slurm - Workflow orchestration tools - Others: Hydra, Google MLMD,
-Streamlit, ... ### On hold - scikit-learn integration - Cloud storage support
-â store runs blob(e.g. images) data on the cloud (Start: _Mar 21 2022_) -
-Artifact storage â store files, model checkpoints, and beyond (Start: _Mar 21
-2022_) ## Community ### If you have questions 1. [Read the docs](https://
-aimstack.readthedocs.io/en/latest/) 2. [Open a feature request or report a bug]
-(https://github.com/aimhubio/aim/issues) 3. [Join Discord community server]
-(https://community.aimstack.io/)
+_Nov 26 2022_) - [x] HuggingFace datasets (Start: _Dec 29 2022_, _Feb 3 2023_)
+# ð¥ Community ## Aim README badge Add Aim badge to your README, if you've
+enjoyed using Aim in your work: [![Aim](https://img.shields.io/badge/
+powered%20by-Aim-%231473E6)](https://github.com/aimhubio/aim) ``` [![Aim]
+(https://img.shields.io/badge/powered%20by-Aim-%231473E6)](https://github.com/
+aimhubio/aim) ``` ## Cite Aim in your papers In case you've found Aim helpful
+in your research journey, we'd be thrilled if you could acknowledge Aim's
+contribution: ```bibtex @software{Arakelyan_Aim_2020, author = {Arakelyan, Gor
+and Soghomonyan, Gevorg and {The Aim team}}, doi = {10.5281/zenodo.6536395},
+license = {Apache-2.0}, month = {6}, title = {{Aim}}, url = {https://
+github.com/aimhubio/aim}, version = {3.9.3}, year = {2020} } ``` ##
+Contributing to Aim Considering contibuting to Aim? To get started, please take
+a moment to read the [CONTRIBUTING.md](https://github.com/aimhubio/aim/blob/
+main/CONTRIBUTING.md) guide. Join Aim contributors by submitting your first
+pull request. Happy coding! ð [https://contrib.rocks/image?repo=aimhubio/
+aim] Made with [contrib.rocks](https://contrib.rocks). ## More questions? 1.
+[Read the docs](https://aimstack.readthedocs.io/en/latest/) 2. [Open a feature
+request or report a bug](https://github.com/aimhubio/aim/issues) 3. [Join
+Discord community server](https://community.aimstack.io/)
```

### Comparing `aim-4.0.0.dev1/aim/__about__.py` & `aim-4.0.0.dev2/aim/__about__.py`

 * *Files identical despite different names*

### Comparing `aim-4.0.0.dev1/aim/cli/cli.py` & `aim-4.0.0.dev2/aim/cli/cli.py`

 * *Files identical despite different names*

### Comparing `aim-4.0.0.dev1/aim/cli/convert/commands.py` & `aim-4.0.0.dev2/aim/cli/convert/commands.py`

 * *Files identical despite different names*

### Comparing `aim-4.0.0.dev1/aim/cli/convert/processors/mlflow.py` & `aim-4.0.0.dev2/aim/cli/convert/processors/mlflow.py`

 * *Files identical despite different names*

### Comparing `aim-4.0.0.dev1/aim/cli/convert/processors/tensorboard.py` & `aim-4.0.0.dev2/aim/cli/convert/processors/tensorboard.py`

 * *Files identical despite different names*

### Comparing `aim-4.0.0.dev1/aim/cli/convert/processors/wandb.py` & `aim-4.0.0.dev2/aim/cli/convert/processors/wandb.py`

 * *Files identical despite different names*

### Comparing `aim-4.0.0.dev1/aim/cli/init/commands.py` & `aim-4.0.0.dev2/aim/cli/init/commands.py`

 * *Files 12% similar despite different names*

```diff
@@ -8,25 +8,29 @@
 
 
 @click.command()
 @click.option('--repo', required=False, type=click.Path(exists=True,
                                                         file_okay=False,
                                                         dir_okay=True,
                                                         writable=True))
-def init(repo):
+@click.option('-y', '--yes', is_flag=True, help='Automatically confirm prompt')
+def init(repo, yes):
     """
     Initializes new repository in the --repo directory.
     Initializes new repository in the current working directory if --repo argument is not provided:
      - Creates .aim directory & runs upgrades for structured DB
     """
     repo_path = clean_repo_path(repo) or os.getcwd()
     re_init = False
     if Repo.exists(repo_path):
-        re_init = click.confirm('Aim repository is already initialized. '
-                                'Do you want to re-initialize to empty Aim repository?')
+        if yes:
+            re_init = True
+        else:
+            re_init = click.confirm('Aim repository is already initialized. '
+                                    'Do you want to re-initialize to empty Aim repository?')
         if not re_init:
             return
         # Clear old repo
         Repo.rm(repo_path)
 
     repo = Repo.from_path(repo_path, init=True)
     if re_init:
```

### Comparing `aim-4.0.0.dev1/aim/cli/manager/manager.py` & `aim-4.0.0.dev2/aim/cli/manager/manager.py`

 * *Files identical despite different names*

### Comparing `aim-4.0.0.dev1/aim/cli/reindex/commands.py` & `aim-4.0.0.dev2/aim/cli/reindex/commands.py`

 * *Files identical despite different names*

### Comparing `aim-4.0.0.dev1/aim/cli/runs/commands.py` & `aim-4.0.0.dev2/aim/cli/runs/commands.py`

 * *Files 2% similar despite different names*

```diff
@@ -41,25 +41,29 @@
     click.echo('\t'.join(run_hashes))
     click.echo(f'Total {len(run_hashes)} runs.')
 
 
 @runs.command(name='rm')
 @click.argument('hashes', nargs=-1, type=str)
 @click.pass_context
-def remove_runs(ctx, hashes):
+@click.option('-y', '--yes', is_flag=True, help='Automatically confirm prompt')
+def remove_runs(ctx, hashes, yes):
     """Remove Run data for given run hashes."""
     if len(hashes) == 0:
         click.echo('Please specify at least one Run to delete.')
         exit(1)
     repo_path = ctx.obj['repo']
     repo = Repo.from_path(repo_path)
 
     matched_hashes = match_runs(repo_path, hashes)
-    confirmed = click.confirm(f'This command will permanently delete {len(matched_hashes)} runs from aim repo '
-                              f'located at \'{repo_path}\'. Do you want to proceed?')
+    if yes:
+        confirmed = True
+    else:
+        confirmed = click.confirm(f'This command will permanently delete {len(matched_hashes)} runs from aim repo '
+                                  f'located at \'{repo_path}\'. Do you want to proceed?')
     if not confirmed:
         return
 
     success, remaining_runs = repo.delete_runs(matched_hashes)
     if success:
         click.echo(f'Successfully deleted {len(matched_hashes)} runs.')
     else:
@@ -143,26 +147,31 @@
     else:
         click.echo(f'The storage backup failed because of the following error: {uploaded_zip_file_name}.')
 
 
 @runs.command(name='close')
 @click.argument('hashes', nargs=-1, type=str)
 @click.pass_context
-def close_runs(ctx, hashes):
+@click.option('-y', '--yes', is_flag=True, help='Automatically confirm prompt')
+def close_runs(ctx, hashes, yes):
     """Close failed/stalled Runs."""
     repo_path = ctx.obj['repo']
     repo = Repo.from_path(repo_path)
 
     if len(hashes) == 0:
         click.echo('Please specify at least one Run to close.')
         exit(1)
 
     click.secho(f'This command will forcefully close {len(hashes)} Runs from Aim Repo \'{repo_path}\'. '
                 f'Please make sure Runs are not active. Data corruption may occur otherwise.')
-    if not click.confirm('Do you want to proceed?'):
+    if yes:
+        confirmed = True
+    else:
+        confirmed = click.confirm('Do you want to proceed?')
+    if not confirmed:
         return
 
     lock_manager = LockManager(repo.path)
     index_manager = RepoIndexManager.get_index_manager(repo)
 
     def close_run(run_hash):
         if lock_manager.release_locks(run_hash, force=True):
```

### Comparing `aim-4.0.0.dev1/aim/cli/runs/utils.py` & `aim-4.0.0.dev2/aim/cli/runs/utils.py`

 * *Files identical despite different names*

### Comparing `aim-4.0.0.dev1/aim/cli/server/commands.py` & `aim-4.0.0.dev2/aim/cli/server/commands.py`

 * *Files 10% similar despite different names*

```diff
@@ -23,33 +23,40 @@
                                                                dir_okay=False,
                                                                readable=True))
 @click.option('--ssl-certfile', required=False, type=click.Path(exists=True,
                                                                 file_okay=True,
                                                                 dir_okay=False,
                                                                 readable=True))
 @click.option('--log-level', required=False, default='', type=str)
+@click.option('-y', '--yes', is_flag=True, help='Automatically confirm prompt')
 def server(host, port, workers,
            repo, ssl_keyfile, ssl_certfile,
-           log_level):
+           log_level, yes):
     # TODO [MV, AT] remove code duplication with aim up cmd implementation
     if log_level:
         set_log_level(log_level)
 
     repo_path = clean_repo_path(repo) or Repo.default_repo_path()
     repo_status = Repo.check_repo_status(repo_path)
     if repo_status == RepoStatus.MISSING:
-        init_repo = click.confirm(f'\'{repo_path}\' is not a valid Aim repository. Do you want to initialize it?')
+        if yes:
+            init_repo = True
+        else:
+            init_repo = click.confirm(f'\'{repo_path}\' is not a valid Aim repository. Do you want to initialize it?')
 
         if not init_repo:
             click.echo('To initialize repo please run the following command:')
             click.secho('aim init', fg='yellow')
             return
         repo_inst = Repo.from_path(repo_path, init=True)
     elif repo_status == RepoStatus.UPDATE_REQUIRED:
-        upgrade_repo = click.confirm(f'\'{repo_path}\' requires upgrade. Do you want to run upgrade automatically?')
+        if yes:
+            upgrade_repo = True
+        else:
+            upgrade_repo = click.confirm(f'\'{repo_path}\' requires upgrade. Do you want to run upgrade automatically?')
         if upgrade_repo:
             from aim.cli.upgrade.utils import convert_2to3
             repo_inst = convert_2to3(repo_path, drop_existing=False, skip_failed_runs=False, skip_checks=False)
         else:
             click.echo('To upgrade repo please run the following command:')
             click.secho(f'aim upgrade --repo {repo_path} 2to3', fg='yellow')
             return
```

### Comparing `aim-4.0.0.dev1/aim/cli/storage/commands.py` & `aim-4.0.0.dev2/aim/cli/storage/commands.py`

 * *Files 4% similar despite different names*

```diff
@@ -43,27 +43,31 @@
     repo_path = ctx.obj['repo']
     convert_2to3(repo_path, drop_existing, skip_failed_runs, skip_checks)
 
 
 @upgrade.command(name='3.11+')
 @click.argument('hashes', nargs=-1, type=str)
 @click.pass_context
-def to_3_11(ctx, hashes):
+@click.option('-y', '--yes', is_flag=True, help='Automatically confirm prompt')
+def to_3_11(ctx, hashes, yes):
     """Optimize Runs Metrics data for read access."""
     if len(hashes) == 0:
         click.echo('Please specify at least one Run to update.')
         exit(1)
     repo_path = ctx.obj['repo']
     repo = Repo.from_path(repo_path)
 
     matched_hashes = match_runs(repo_path, hashes)
     remaining_runs = []
-    confirmed = click.confirm(f'This command will optimize the metrics data for {len(matched_hashes)} runs from aim '
-                              f'repo located at \'{repo_path}\'. This process might take a while. '
-                              f'Do you want to proceed?')
+    if yes:
+        confirmed = True
+    else:
+        confirmed = click.confirm(f'This command will optimize the metrics data for {len(matched_hashes)} '
+                                  f'runs from aim repo located at \'{repo_path}\'. This process might take a while. '
+                                  f'Do you want to proceed?')
     if not confirmed:
         return
 
     index_manager = RepoIndexManager.get_index_manager(repo)
     for run_hash in tqdm(matched_hashes):
         try:
             run = Run(run_hash, repo=repo)
@@ -84,25 +88,29 @@
     click.echo('In case of any issues the following command can be used to restore data:')
     click.secho(f'aim storage --repo {repo.root_path} restore \'*\'', fg='yellow')
 
 
 @storage.command(name='restore')
 @click.argument('hashes', nargs=-1, type=str)
 @click.pass_context
-def restore_runs(ctx, hashes):
+@click.option('-y', '--yes', is_flag=True, help='Automatically confirm prompt')
+def restore_runs(ctx, hashes, yes):
     """Rollback Runs data for given run hashes to the previous metric format. """
     if len(hashes) == 0:
         click.echo('Please specify at least one Run to delete.')
         exit(1)
     repo_path = ctx.obj['repo']
     repo = Repo.from_path(repo_path)
 
     matched_hashes = match_runs(repo_path, hashes, lookup_dir='bcp')
-    confirmed = click.confirm(f'This command will restore {len(matched_hashes)} runs from aim repo '
-                              f'located at \'{repo_path}\'. Do you want to proceed?')
+    if yes:
+        confirmed = True
+    else:
+        confirmed = click.confirm(f'This command will restore {len(matched_hashes)} runs from aim repo '
+                                  f'located at \'{repo_path}\'. Do you want to proceed?')
     if not confirmed:
         return
 
     remaining_runs = []
     index_manager = RepoIndexManager.get_index_manager(repo)
     for run_hash in tqdm(matched_hashes):
         try:
```

### Comparing `aim-4.0.0.dev1/aim/cli/up/commands.py` & `aim-4.0.0.dev2/aim/cli/up/commands.py`

 * *Files identical despite different names*

### Comparing `aim-4.0.0.dev1/aim/cli/up/utils.py` & `aim-4.0.0.dev2/aim/cli/up/utils.py`

 * *Files identical despite different names*

### Comparing `aim-4.0.0.dev1/aim/cli/upgrade/_legacy_repo/configs.py` & `aim-4.0.0.dev2/aim/cli/upgrade/_legacy_repo/configs.py`

 * *Files identical despite different names*

### Comparing `aim-4.0.0.dev1/aim/cli/upgrade/_legacy_repo/proto/v3/base_pb2.py` & `aim-4.0.0.dev2/aim/cli/upgrade/_legacy_repo/proto/v3/base_pb2.py`

 * *Files identical despite different names*

### Comparing `aim-4.0.0.dev1/aim/cli/upgrade/_legacy_repo/proto/v3/metric_pb2.py` & `aim-4.0.0.dev2/aim/cli/upgrade/_legacy_repo/proto/v3/metric_pb2.py`

 * *Files identical despite different names*

### Comparing `aim-4.0.0.dev1/aim/cli/upgrade/_legacy_repo/proto/v4/base_pb2.py` & `aim-4.0.0.dev2/aim/cli/upgrade/_legacy_repo/proto/v4/base_pb2.py`

 * *Files identical despite different names*

### Comparing `aim-4.0.0.dev1/aim/cli/upgrade/_legacy_repo/proto/v4/metric_pb2.py` & `aim-4.0.0.dev2/aim/cli/upgrade/_legacy_repo/proto/v4/metric_pb2.py`

 * *Files identical despite different names*

### Comparing `aim-4.0.0.dev1/aim/cli/upgrade/_legacy_repo/repo/metric.py` & `aim-4.0.0.dev2/aim/cli/upgrade/_legacy_repo/repo/metric.py`

 * *Files identical despite different names*

### Comparing `aim-4.0.0.dev1/aim/cli/upgrade/_legacy_repo/repo/repo.py` & `aim-4.0.0.dev2/aim/cli/upgrade/_legacy_repo/repo/repo.py`

 * *Files identical despite different names*

### Comparing `aim-4.0.0.dev1/aim/cli/upgrade/_legacy_repo/repo/run.py` & `aim-4.0.0.dev2/aim/cli/upgrade/_legacy_repo/repo/run.py`

 * *Files identical despite different names*

### Comparing `aim-4.0.0.dev1/aim/cli/upgrade/_legacy_repo/repo/trace.py` & `aim-4.0.0.dev2/aim/cli/upgrade/_legacy_repo/repo/trace.py`

 * *Files identical despite different names*

### Comparing `aim-4.0.0.dev1/aim/cli/upgrade/_legacy_repo/repo/utils.py` & `aim-4.0.0.dev2/aim/cli/upgrade/_legacy_repo/repo/utils.py`

 * *Files identical despite different names*

### Comparing `aim-4.0.0.dev1/aim/cli/upgrade/utils.py` & `aim-4.0.0.dev2/aim/cli/upgrade/utils.py`

 * *Files identical despite different names*

### Comparing `aim-4.0.0.dev1/aim/cli/watcher_cli.py` & `aim-4.0.0.dev2/aim/cli/watcher_cli.py`

 * *Files identical despite different names*

### Comparing `aim-4.0.0.dev1/aim/ext/cleanup/__init__.py` & `aim-4.0.0.dev2/aim/ext/cleanup/__init__.py`

 * *Files identical despite different names*

### Comparing `aim-4.0.0.dev1/aim/ext/exception_resistant.py` & `aim-4.0.0.dev2/aim/ext/exception_resistant.py`

 * *Files identical despite different names*

### Comparing `aim-4.0.0.dev1/aim/ext/notebook/notebook.py` & `aim-4.0.0.dev2/aim/ext/notebook/notebook.py`

 * *Files identical despite different names*

### Comparing `aim-4.0.0.dev1/aim/ext/notifier/__init__.py` & `aim-4.0.0.dev2/aim/ext/notifier/__init__.py`

 * *Files identical despite different names*

### Comparing `aim-4.0.0.dev1/aim/ext/notifier/config.py` & `aim-4.0.0.dev2/aim/ext/notifier/config.py`

 * *Files identical despite different names*

### Comparing `aim-4.0.0.dev1/aim/ext/notifier/logging_notifier.py` & `aim-4.0.0.dev2/aim/ext/notifier/logging_notifier.py`

 * *Files identical despite different names*

### Comparing `aim-4.0.0.dev1/aim/ext/notifier/notifier.py` & `aim-4.0.0.dev2/aim/ext/notifier/notifier.py`

 * *Files identical despite different names*

### Comparing `aim-4.0.0.dev1/aim/ext/notifier/notifier_builder.py` & `aim-4.0.0.dev2/aim/ext/notifier/notifier_builder.py`

 * *Files identical despite different names*

### Comparing `aim-4.0.0.dev1/aim/ext/notifier/slack_notifier.py` & `aim-4.0.0.dev2/aim/ext/notifier/slack_notifier.py`

 * *Files identical despite different names*

### Comparing `aim-4.0.0.dev1/aim/ext/notifier/utils.py` & `aim-4.0.0.dev2/aim/ext/notifier/utils.py`

 * *Files identical despite different names*

### Comparing `aim-4.0.0.dev1/aim/ext/notifier/workplace_notifier.py` & `aim-4.0.0.dev2/aim/ext/notifier/workplace_notifier.py`

 * *Files identical despite different names*

### Comparing `aim-4.0.0.dev1/aim/ext/resource/log.py` & `aim-4.0.0.dev2/aim/ext/resource/log.py`

 * *Files identical despite different names*

### Comparing `aim-4.0.0.dev1/aim/ext/resource/stat.py` & `aim-4.0.0.dev2/aim/ext/resource/stat.py`

 * *Files identical despite different names*

### Comparing `aim-4.0.0.dev1/aim/ext/resource/tracker.py` & `aim-4.0.0.dev2/aim/ext/resource/tracker.py`

 * *Files identical despite different names*

### Comparing `aim-4.0.0.dev1/aim/ext/sshfs/utils.py` & `aim-4.0.0.dev2/aim/ext/sshfs/utils.py`

 * *Files identical despite different names*

### Comparing `aim-4.0.0.dev1/aim/ext/task_queue/queue.py` & `aim-4.0.0.dev2/aim/ext/task_queue/queue.py`

 * *Files identical despite different names*

### Comparing `aim-4.0.0.dev1/aim/ext/tensorboard_tracker/run.py` & `aim-4.0.0.dev2/aim/ext/tensorboard_tracker/run.py`

 * *Files identical despite different names*

### Comparing `aim-4.0.0.dev1/aim/ext/tensorboard_tracker/tracker.py` & `aim-4.0.0.dev2/aim/ext/tensorboard_tracker/tracker.py`

 * *Files identical despite different names*

### Comparing `aim-4.0.0.dev1/aim/ext/transport/client.py` & `aim-4.0.0.dev2/aim/ext/transport/client.py`

 * *Files identical despite different names*

### Comparing `aim-4.0.0.dev1/aim/ext/transport/config.py` & `aim-4.0.0.dev2/aim/ext/transport/config.py`

 * *Files identical despite different names*

### Comparing `aim-4.0.0.dev1/aim/ext/transport/handlers.py` & `aim-4.0.0.dev2/aim/ext/transport/handlers.py`

 * *Files identical despite different names*

### Comparing `aim-4.0.0.dev1/aim/ext/transport/health.py` & `aim-4.0.0.dev2/aim/ext/transport/health.py`

 * *Files identical despite different names*

### Comparing `aim-4.0.0.dev1/aim/ext/transport/heartbeat.py` & `aim-4.0.0.dev2/aim/ext/transport/heartbeat.py`

 * *Files identical despite different names*

### Comparing `aim-4.0.0.dev1/aim/ext/transport/message_utils.py` & `aim-4.0.0.dev2/aim/ext/transport/message_utils.py`

 * *Files identical despite different names*

### Comparing `aim-4.0.0.dev1/aim/ext/transport/proto/health_pb2_grpc.py` & `aim-4.0.0.dev2/aim/ext/transport/proto/health_pb2_grpc.py`

 * *Files identical despite different names*

### Comparing `aim-4.0.0.dev1/aim/ext/transport/proto/remote_router_pb2_grpc.py` & `aim-4.0.0.dev2/aim/ext/transport/proto/remote_router_pb2_grpc.py`

 * *Files identical despite different names*

### Comparing `aim-4.0.0.dev1/aim/ext/transport/proto/remote_tracking_pb2_grpc.py` & `aim-4.0.0.dev2/aim/ext/transport/proto/remote_tracking_pb2_grpc.py`

 * *Files identical despite different names*

### Comparing `aim-4.0.0.dev1/aim/ext/transport/proto/v3/health_pb2.py` & `aim-4.0.0.dev2/aim/ext/transport/proto/v3/health_pb2.py`

 * *Files identical despite different names*

### Comparing `aim-4.0.0.dev1/aim/ext/transport/proto/v3/remote_router_pb2.py` & `aim-4.0.0.dev2/aim/ext/transport/proto/v3/remote_router_pb2.py`

 * *Files identical despite different names*

### Comparing `aim-4.0.0.dev1/aim/ext/transport/proto/v3/remote_tracking_pb2.py` & `aim-4.0.0.dev2/aim/ext/transport/proto/v3/remote_tracking_pb2.py`

 * *Files identical despite different names*

### Comparing `aim-4.0.0.dev1/aim/ext/transport/proto/v4/health_pb2.py` & `aim-4.0.0.dev2/aim/ext/transport/proto/v4/health_pb2.py`

 * *Files identical despite different names*

### Comparing `aim-4.0.0.dev1/aim/ext/transport/proto/v4/remote_router_pb2.py` & `aim-4.0.0.dev2/aim/ext/transport/proto/v4/remote_router_pb2.py`

 * *Files identical despite different names*

### Comparing `aim-4.0.0.dev1/aim/ext/transport/proto/v4/remote_tracking_pb2.py` & `aim-4.0.0.dev2/aim/ext/transport/proto/v4/remote_tracking_pb2.py`

 * *Files identical despite different names*

### Comparing `aim-4.0.0.dev1/aim/ext/transport/remote_tracking.py` & `aim-4.0.0.dev2/aim/ext/transport/remote_tracking.py`

 * *Files identical despite different names*

### Comparing `aim-4.0.0.dev1/aim/ext/transport/router.py` & `aim-4.0.0.dev2/aim/ext/transport/router.py`

 * *Files identical despite different names*

### Comparing `aim-4.0.0.dev1/aim/ext/transport/rpc_queue.py` & `aim-4.0.0.dev2/aim/ext/transport/rpc_queue.py`

 * *Files identical despite different names*

### Comparing `aim-4.0.0.dev1/aim/ext/transport/server.py` & `aim-4.0.0.dev2/aim/ext/transport/server.py`

 * *Files identical despite different names*

### Comparing `aim-4.0.0.dev1/aim/ext/transport/worker.py` & `aim-4.0.0.dev2/aim/ext/transport/worker.py`

 * *Files identical despite different names*

### Comparing `aim-4.0.0.dev1/aim/ext/utils.py` & `aim-4.0.0.dev2/aim/ext/utils.py`

 * *Files identical despite different names*

### Comparing `aim-4.0.0.dev1/aim/sdk/__init__.py` & `aim-4.0.0.dev2/aim/sdk/__init__.py`

 * *Files identical despite different names*

### Comparing `aim-4.0.0.dev1/aim/sdk/adapters/acme.py` & `aim-4.0.0.dev2/aim/sdk/adapters/acme.py`

 * *Files identical despite different names*

### Comparing `aim-4.0.0.dev1/aim/sdk/adapters/catboost.py` & `aim-4.0.0.dev2/aim/sdk/adapters/catboost.py`

 * *Files identical despite different names*

### Comparing `aim-4.0.0.dev1/aim/sdk/adapters/fastai.py` & `aim-4.0.0.dev2/aim/sdk/adapters/fastai.py`

 * *Files identical despite different names*

### Comparing `aim-4.0.0.dev1/aim/sdk/adapters/hugging_face.py` & `aim-4.0.0.dev2/aim/sdk/adapters/hugging_face.py`

 * *Files 4% similar despite different names*

```diff
@@ -65,15 +65,16 @@
                 self._run_hash = self._run.hash
 
         if args:
             combined_dict = {**args.to_sanitized_dict()}
             for key, value in combined_dict.items():
                 self._run.set(('hparams', key), value, strict=False)
         if model:
-            self._run.set('model', {**vars(model.config), 'num_labels': model.num_labels}, strict=False)
+            self._run.set('model', {**vars(model.config), 'num_labels': getattr(model, 'num_labels', None)},
+                          strict=False)
 
         # Store model configs as well
         # if hasattr(model, 'config') and model.config is not None:
         #     model_config = model.config.to_dict()
         #     self._run['model'] = model_config
 
     def on_train_begin(self, args, state, control, model=None, **kwargs):
```

### Comparing `aim-4.0.0.dev1/aim/sdk/adapters/keras.py` & `aim-4.0.0.dev2/aim/sdk/adapters/keras.py`

 * *Files identical despite different names*

### Comparing `aim-4.0.0.dev1/aim/sdk/adapters/keras_mixins.py` & `aim-4.0.0.dev2/aim/sdk/adapters/keras_mixins.py`

 * *Files identical despite different names*

### Comparing `aim-4.0.0.dev1/aim/sdk/adapters/keras_tuner.py` & `aim-4.0.0.dev2/aim/sdk/adapters/keras_tuner.py`

 * *Files identical despite different names*

### Comparing `aim-4.0.0.dev1/aim/sdk/adapters/lightgbm.py` & `aim-4.0.0.dev2/aim/sdk/adapters/lightgbm.py`

 * *Files identical despite different names*

### Comparing `aim-4.0.0.dev1/aim/sdk/adapters/mxnet.py` & `aim-4.0.0.dev2/aim/sdk/adapters/mxnet.py`

 * *Files identical despite different names*

### Comparing `aim-4.0.0.dev1/aim/sdk/adapters/optuna.py` & `aim-4.0.0.dev2/aim/sdk/adapters/optuna.py`

 * *Files identical despite different names*

### Comparing `aim-4.0.0.dev1/aim/sdk/adapters/paddle.py` & `aim-4.0.0.dev2/aim/sdk/adapters/paddle.py`

 * *Files identical despite different names*

### Comparing `aim-4.0.0.dev1/aim/sdk/adapters/prophet.py` & `aim-4.0.0.dev2/aim/sdk/adapters/prophet.py`

 * *Files identical despite different names*

### Comparing `aim-4.0.0.dev1/aim/sdk/adapters/pytorch.py` & `aim-4.0.0.dev2/aim/sdk/adapters/pytorch.py`

 * *Files identical despite different names*

### Comparing `aim-4.0.0.dev1/aim/sdk/adapters/pytorch_ignite.py` & `aim-4.0.0.dev2/aim/sdk/adapters/pytorch_ignite.py`

 * *Files identical despite different names*

### Comparing `aim-4.0.0.dev1/aim/sdk/adapters/pytorch_lightning.py` & `aim-4.0.0.dev2/aim/sdk/adapters/pytorch_lightning.py`

 * *Files 2% similar despite different names*

```diff
@@ -38,29 +38,32 @@
                  train_metric_prefix: Optional[str] = 'train_',
                  val_metric_prefix: Optional[str] = 'val_',
                  test_metric_prefix: Optional[str] = 'test_',
                  system_tracking_interval: Optional[int]
                  = DEFAULT_SYSTEM_TRACKING_INT,
                  log_system_params: Optional[bool] = True,
                  capture_terminal_logs: Optional[bool] = True,
+                 run_name: Optional[str] = None,
+                 run_hash: Optional[str] = None,
                  ):
         super().__init__()
 
         self._experiment_name = experiment
+        self._run_name = run_name
         self._repo_path = repo
 
         self._train_metric_prefix = train_metric_prefix
         self._val_metric_prefix = val_metric_prefix
         self._test_metric_prefix = test_metric_prefix
         self._system_tracking_interval = system_tracking_interval
         self._log_system_params = log_system_params
         self._capture_terminal_logs = capture_terminal_logs
 
         self._run = None
-        self._run_hash = None
+        self._run_hash = run_hash
 
     @staticmethod
     def _convert_params(params: Union[Dict[str, Any], Namespace]) -> Dict[str, Any]:
         # in case converting from namespace
         if isinstance(params, Namespace):
             params = vars(params)
 
@@ -76,14 +79,16 @@
             if self._run_hash:
                 self._run = Run(
                     self._run_hash,
                     repo=self._repo_path,
                     system_tracking_interval=self._system_tracking_interval,
                     capture_terminal_logs=self._capture_terminal_logs
                 )
+                if self._run_name is not None:
+                    self._run.name = self._run_name
             else:
                 self._run = Run(
                     repo=self._repo_path,
                     experiment=self._experiment_name,
                     system_tracking_interval=self._system_tracking_interval,
                     log_system_params=self._log_system_params,
                     capture_terminal_logs=self._capture_terminal_logs,
```

### Comparing `aim-4.0.0.dev1/aim/sdk/adapters/sb3.py` & `aim-4.0.0.dev2/aim/sdk/adapters/sb3.py`

 * *Files identical despite different names*

### Comparing `aim-4.0.0.dev1/aim/sdk/adapters/tensorflow.py` & `aim-4.0.0.dev2/aim/sdk/adapters/tensorflow.py`

 * *Files identical despite different names*

### Comparing `aim-4.0.0.dev1/aim/sdk/adapters/xgboost.py` & `aim-4.0.0.dev2/aim/sdk/adapters/xgboost.py`

 * *Files identical despite different names*

### Comparing `aim-4.0.0.dev1/aim/sdk/base_run.py` & `aim-4.0.0.dev2/aim/sdk/base_run.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,11 @@
 import logging
 from typing import Dict, Optional, Union
 from typing import TYPE_CHECKING
+import pathlib
 
 from aim.storage.hashing import hash_auto
 from aim.storage.treeview import TreeView
 from aim.sdk.utils import generate_run_hash
 from aim.sdk.repo_utils import get_repo
 from aim.sdk.errors import MissingRunError
 from aim.sdk.tracker import STEP_HASH_FUNCTIONS
@@ -21,15 +22,15 @@
     def __new__(cls, *args, **kwargs):
         # prevent BaseRun from being instantiated directly
         if cls is BaseRun:
             raise TypeError(f'Only children of \'{cls.__name__}\' may be instantiated.')
         return object.__new__(cls)
 
     def __init__(self, run_hash: Optional[str] = None,
-                 repo: Optional[Union[str, 'Repo']] = None,
+                 repo: Optional[Union[str, 'Repo', pathlib.Path]] = None,
                  read_only: bool = False,
                  force_resume: bool = False):
         self._hash = None
         self._lock = None
 
         self.read_only = read_only
         self.repo = get_repo(repo)
```

### Comparing `aim-4.0.0.dev1/aim/sdk/callbacks/caller.py` & `aim-4.0.0.dev2/aim/sdk/callbacks/caller.py`

 * *Files identical despite different names*

### Comparing `aim-4.0.0.dev1/aim/sdk/callbacks/helpers.py` & `aim-4.0.0.dev2/aim/sdk/callbacks/helpers.py`

 * *Files identical despite different names*

### Comparing `aim-4.0.0.dev1/aim/sdk/index_manager.py` & `aim-4.0.0.dev2/aim/sdk/index_manager.py`

 * *Files identical despite different names*

### Comparing `aim-4.0.0.dev1/aim/sdk/legacy/select.py` & `aim-4.0.0.dev2/aim/sdk/legacy/select.py`

 * *Files identical despite different names*

### Comparing `aim-4.0.0.dev1/aim/sdk/legacy/session/session.py` & `aim-4.0.0.dev2/aim/sdk/legacy/session/session.py`

 * *Files identical despite different names*

### Comparing `aim-4.0.0.dev1/aim/sdk/lock_manager.py` & `aim-4.0.0.dev2/aim/sdk/lock_manager.py`

 * *Files identical despite different names*

### Comparing `aim-4.0.0.dev1/aim/sdk/logging/log_record.py` & `aim-4.0.0.dev2/aim/sdk/logging/log_record.py`

 * *Files identical despite different names*

### Comparing `aim-4.0.0.dev1/aim/sdk/maintenance_run.py` & `aim-4.0.0.dev2/aim/sdk/maintenance_run.py`

 * *Files identical despite different names*

### Comparing `aim-4.0.0.dev1/aim/sdk/num_utils.py` & `aim-4.0.0.dev2/aim/sdk/num_utils.py`

 * *Files 18% similar despite different names*

```diff
@@ -63,15 +63,19 @@
     return inst_has_typename(inst, ['tensorflow', 'Tensor'])
 
 
 def is_jax_device_array(inst):
     """
     Check whether `inst` is instance of jax device array
     """
-    return inst_has_typename(inst, ['jaxlib', 'xla_extension', 'DeviceArray'])
+    if inst_has_typename(inst, ['jaxlib', 'xla_extension', 'Array']):
+        return True
+    if inst_has_typename(inst, ['jaxlib', 'xla_extension', 'DeviceArray']):
+        return True
+    return False
 
 
 def is_numpy_array(inst):
     """
     Check whether `inst` is instance of numpy array
     """
     return inst_has_typename(inst, ['numpy', 'ndarray'])
```

### Comparing `aim-4.0.0.dev1/aim/sdk/objects/audio.py` & `aim-4.0.0.dev2/aim/sdk/objects/audio.py`

 * *Files identical despite different names*

### Comparing `aim-4.0.0.dev1/aim/sdk/objects/distribution.py` & `aim-4.0.0.dev2/aim/sdk/objects/distribution.py`

 * *Files identical despite different names*

### Comparing `aim-4.0.0.dev1/aim/sdk/objects/figure.py` & `aim-4.0.0.dev2/aim/sdk/objects/figure.py`

 * *Files identical despite different names*

### Comparing `aim-4.0.0.dev1/aim/sdk/objects/image.py` & `aim-4.0.0.dev2/aim/sdk/objects/image.py`

 * *Files identical despite different names*

### Comparing `aim-4.0.0.dev1/aim/sdk/objects/io/wavfile.py` & `aim-4.0.0.dev2/aim/sdk/objects/io/wavfile.py`

 * *Files identical despite different names*

### Comparing `aim-4.0.0.dev1/aim/sdk/objects/plugins/dvc_metadata.py` & `aim-4.0.0.dev2/aim/sdk/objects/plugins/dvc_metadata.py`

 * *Files identical despite different names*

### Comparing `aim-4.0.0.dev1/aim/sdk/objects/plugins/hf_datasets_metadata.py` & `aim-4.0.0.dev2/aim/sdk/objects/plugins/hf_datasets_metadata.py`

 * *Files identical despite different names*

### Comparing `aim-4.0.0.dev1/aim/sdk/objects/plugins/hub_dataset.py` & `aim-4.0.0.dev2/aim/sdk/objects/plugins/hub_dataset.py`

 * *Files identical despite different names*

### Comparing `aim-4.0.0.dev1/aim/sdk/objects/text.py` & `aim-4.0.0.dev2/aim/sdk/objects/text.py`

 * *Files identical despite different names*

### Comparing `aim-4.0.0.dev1/aim/sdk/query_utils.py` & `aim-4.0.0.dev2/aim/sdk/query_utils.py`

 * *Files identical despite different names*

### Comparing `aim-4.0.0.dev1/aim/sdk/remote_repo_proxy.py` & `aim-4.0.0.dev2/aim/sdk/remote_repo_proxy.py`

 * *Files identical despite different names*

### Comparing `aim-4.0.0.dev1/aim/sdk/remote_run_reporter.py` & `aim-4.0.0.dev2/aim/sdk/remote_run_reporter.py`

 * *Files identical despite different names*

### Comparing `aim-4.0.0.dev1/aim/sdk/repo.py` & `aim-4.0.0.dev2/aim/sdk/repo.py`

 * *Files identical despite different names*

### Comparing `aim-4.0.0.dev1/aim/sdk/repo_utils.py` & `aim-4.0.0.dev2/aim/sdk/repo_utils.py`

 * *Files 23% similar despite different names*

```diff
@@ -1,21 +1,24 @@
 import logging
 from typing import Optional, Union, TYPE_CHECKING
+import pathlib
 
 if TYPE_CHECKING:
     from aim.sdk.repo import Repo
 
 logger = logging.getLogger(__name__)
 
 
-def get_repo(repo: Optional[Union[str, 'Repo']]) -> 'Repo':
+def get_repo(repo: Optional[Union[str, 'Repo', pathlib.Path]]) -> 'Repo':
     from aim.sdk.repo import Repo, RepoStatus
 
     if repo is None:
         repo = Repo.default_repo_path()
+    if isinstance(repo, pathlib.Path):
+        repo = str(repo)
     if isinstance(repo, str):
         repo_status = Repo.check_repo_status(repo)
         if repo_status == RepoStatus.UPDATE_REQUIRED:
             logger.error(f'Trying to open repository {repo}, which is out of date. '
                          f'Please upgrade repository with the following command: '
                          f'`aim upgrade --repo {repo} 2to3`.')
             raise RuntimeError()
```

### Comparing `aim-4.0.0.dev1/aim/sdk/reporter/__init__.py` & `aim-4.0.0.dev2/aim/sdk/reporter/__init__.py`

 * *Files identical despite different names*

### Comparing `aim-4.0.0.dev1/aim/sdk/reporter/file_manager.py` & `aim-4.0.0.dev2/aim/sdk/reporter/file_manager.py`

 * *Files identical despite different names*

### Comparing `aim-4.0.0.dev1/aim/sdk/run.py` & `aim-4.0.0.dev2/aim/sdk/run.py`

 * *Files 0% similar despite different names*

```diff
@@ -263,15 +263,15 @@
 
 
 class BasicRun(BaseRun, StructuredRunMixin):
 
     _metric_version_warning_shown = False
 
     def __init__(self, run_hash: Optional[str] = None, *,
-                 repo: Optional[Union[str, 'Repo']] = None,
+                 repo: Optional[Union[str, 'Repo', pathlib.Path]] = None,
                  read_only: bool = False,
                  experiment: Optional[str] = None,
                  force_resume: bool = False,
                  ):
         self._resources: Optional[BasicRunAutoClean] = None
         super().__init__(run_hash, repo=repo, read_only=read_only, force_resume=force_resume)
 
@@ -814,15 +814,15 @@
             metrics (CPU, Memory, etc.). Set to `None` to disable system metrics tracking.
          log_system_params (:obj:`bool`, optional): Enable/Disable logging of system params such as installed packages,
             git info, environment variables, etc.
     """
 
     @noexcept
     def __init__(self, run_hash: Optional[str] = None, *,
-                 repo: Optional[Union[str, 'Repo']] = None,
+                 repo: Optional[Union[str, 'Repo', pathlib.Path]] = None,
                  read_only: bool = False,
                  experiment: Optional[str] = None,
                  force_resume: bool = False,
                  system_tracking_interval: Optional[Union[int, float]] = DEFAULT_SYSTEM_TRACKING_INT,
                  log_system_params: Optional[bool] = False,
                  capture_terminal_logs: Optional[bool] = True):
         super().__init__(run_hash, repo=repo, read_only=read_only, experiment=experiment, force_resume=force_resume)
```

### Comparing `aim-4.0.0.dev1/aim/sdk/run_status_watcher.py` & `aim-4.0.0.dev2/aim/sdk/run_status_watcher.py`

 * *Files identical despite different names*

### Comparing `aim-4.0.0.dev1/aim/sdk/sequence.py` & `aim-4.0.0.dev2/aim/sdk/sequence.py`

 * *Files identical despite different names*

### Comparing `aim-4.0.0.dev1/aim/sdk/sequence_collection.py` & `aim-4.0.0.dev2/aim/sdk/sequence_collection.py`

 * *Files identical despite different names*

### Comparing `aim-4.0.0.dev1/aim/sdk/sequences/metric.py` & `aim-4.0.0.dev2/aim/sdk/sequences/metric.py`

 * *Files identical despite different names*

### Comparing `aim-4.0.0.dev1/aim/sdk/tracker.py` & `aim-4.0.0.dev2/aim/sdk/tracker.py`

 * *Files identical despite different names*

### Comparing `aim-4.0.0.dev1/aim/sdk/training_flow.py` & `aim-4.0.0.dev2/aim/sdk/training_flow.py`

 * *Files identical despite different names*

### Comparing `aim-4.0.0.dev1/aim/sdk/uri_service.py` & `aim-4.0.0.dev2/aim/sdk/uri_service.py`

 * *Files identical despite different names*

### Comparing `aim-4.0.0.dev1/aim/sdk/utils.py` & `aim-4.0.0.dev2/aim/sdk/utils.py`

 * *Files identical despite different names*

### Comparing `aim-4.0.0.dev1/aim/storage/arrayview.cpp` & `aim-4.0.0.dev2/aim/storage/arrayview.cpp`

 * *Files 0% similar despite different names*

```diff
@@ -10,22 +10,22 @@
             "-Wextra",
             "-Wconversion",
             "-fno-strict-aliasing",
             "-fno-rtti",
             "-fPIC"
         ],
         "include_dirs": [
-            "/tmp/build-env-347o2c0y/lib/python3.10/site-packages/aimrocks/include"
+            "/tmp/build-env-pa2lz81q/lib/python3.10/site-packages/aimrocks/include"
         ],
         "language": "c++",
         "libraries": [
             "rocksdb"
         ],
         "library_dirs": [
-            "/tmp/build-env-347o2c0y/lib/python3.10/site-packages/aimrocks"
+            "/tmp/build-env-pa2lz81q/lib/python3.10/site-packages/aimrocks"
         ],
         "name": "aim.storage.arrayview",
         "sources": [
             "aim/storage/arrayview.py"
         ]
     },
     "module_name": "aim.storage.arrayview"
```

### Comparing `aim-4.0.0.dev1/aim/storage/arrayview.py` & `aim-4.0.0.dev2/aim/storage/arrayview.py`

 * *Files identical despite different names*

### Comparing `aim-4.0.0.dev1/aim/storage/container.cpp` & `aim-4.0.0.dev2/aim/storage/container.cpp`

 * *Files 0% similar despite different names*

```diff
@@ -1,56 +1,56 @@
 /* Generated by Cython 3.0.0a11 */
 
 /* BEGIN: Cython Metadata
 {
     "distutils": {
         "depends": [
-            "/tmp/build-env-347o2c0y/lib/python3.10/site-packages/aimrocks/include/rdb_include/comparator_wrapper.hpp",
-            "/tmp/build-env-347o2c0y/lib/python3.10/site-packages/aimrocks/include/rdb_include/filter_policy_wrapper.hpp",
-            "/tmp/build-env-347o2c0y/lib/python3.10/site-packages/aimrocks/include/rdb_include/memtable_factories.hpp",
-            "/tmp/build-env-347o2c0y/lib/python3.10/site-packages/aimrocks/include/rdb_include/merge_operator_wrapper.hpp",
-            "/tmp/build-env-347o2c0y/lib/python3.10/site-packages/aimrocks/include/rdb_include/slice_transform_wrapper.hpp",
-            "/tmp/build-env-347o2c0y/lib/python3.10/site-packages/aimrocks/include/rdb_include/utils.hpp",
-            "/tmp/build-env-347o2c0y/lib/python3.10/site-packages/aimrocks/include/rdb_include/write_batch_iter_helper.hpp",
-            "/tmp/build-env-347o2c0y/lib/python3.10/site-packages/aimrocks/include/rocksdb/cache.h",
-            "/tmp/build-env-347o2c0y/lib/python3.10/site-packages/aimrocks/include/rocksdb/comparator.h",
-            "/tmp/build-env-347o2c0y/lib/python3.10/site-packages/aimrocks/include/rocksdb/db.h",
-            "/tmp/build-env-347o2c0y/lib/python3.10/site-packages/aimrocks/include/rocksdb/env.h",
-            "/tmp/build-env-347o2c0y/lib/python3.10/site-packages/aimrocks/include/rocksdb/filter_policy.h",
-            "/tmp/build-env-347o2c0y/lib/python3.10/site-packages/aimrocks/include/rocksdb/iterator.h",
-            "/tmp/build-env-347o2c0y/lib/python3.10/site-packages/aimrocks/include/rocksdb/memtablerep.h",
-            "/tmp/build-env-347o2c0y/lib/python3.10/site-packages/aimrocks/include/rocksdb/merge_operator.h",
-            "/tmp/build-env-347o2c0y/lib/python3.10/site-packages/aimrocks/include/rocksdb/options.h",
-            "/tmp/build-env-347o2c0y/lib/python3.10/site-packages/aimrocks/include/rocksdb/slice.h",
-            "/tmp/build-env-347o2c0y/lib/python3.10/site-packages/aimrocks/include/rocksdb/slice_transform.h",
-            "/tmp/build-env-347o2c0y/lib/python3.10/site-packages/aimrocks/include/rocksdb/status.h",
-            "/tmp/build-env-347o2c0y/lib/python3.10/site-packages/aimrocks/include/rocksdb/table.h",
-            "/tmp/build-env-347o2c0y/lib/python3.10/site-packages/aimrocks/include/rocksdb/universal_compaction.h",
-            "/tmp/build-env-347o2c0y/lib/python3.10/site-packages/aimrocks/include/rocksdb/utilities/backup_engine.h",
-            "/tmp/build-env-347o2c0y/lib/python3.10/site-packages/aimrocks/include/rocksdb/write_batch.h"
+            "/tmp/build-env-pa2lz81q/lib/python3.10/site-packages/aimrocks/include/rdb_include/comparator_wrapper.hpp",
+            "/tmp/build-env-pa2lz81q/lib/python3.10/site-packages/aimrocks/include/rdb_include/filter_policy_wrapper.hpp",
+            "/tmp/build-env-pa2lz81q/lib/python3.10/site-packages/aimrocks/include/rdb_include/memtable_factories.hpp",
+            "/tmp/build-env-pa2lz81q/lib/python3.10/site-packages/aimrocks/include/rdb_include/merge_operator_wrapper.hpp",
+            "/tmp/build-env-pa2lz81q/lib/python3.10/site-packages/aimrocks/include/rdb_include/slice_transform_wrapper.hpp",
+            "/tmp/build-env-pa2lz81q/lib/python3.10/site-packages/aimrocks/include/rdb_include/utils.hpp",
+            "/tmp/build-env-pa2lz81q/lib/python3.10/site-packages/aimrocks/include/rdb_include/write_batch_iter_helper.hpp",
+            "/tmp/build-env-pa2lz81q/lib/python3.10/site-packages/aimrocks/include/rocksdb/cache.h",
+            "/tmp/build-env-pa2lz81q/lib/python3.10/site-packages/aimrocks/include/rocksdb/comparator.h",
+            "/tmp/build-env-pa2lz81q/lib/python3.10/site-packages/aimrocks/include/rocksdb/db.h",
+            "/tmp/build-env-pa2lz81q/lib/python3.10/site-packages/aimrocks/include/rocksdb/env.h",
+            "/tmp/build-env-pa2lz81q/lib/python3.10/site-packages/aimrocks/include/rocksdb/filter_policy.h",
+            "/tmp/build-env-pa2lz81q/lib/python3.10/site-packages/aimrocks/include/rocksdb/iterator.h",
+            "/tmp/build-env-pa2lz81q/lib/python3.10/site-packages/aimrocks/include/rocksdb/memtablerep.h",
+            "/tmp/build-env-pa2lz81q/lib/python3.10/site-packages/aimrocks/include/rocksdb/merge_operator.h",
+            "/tmp/build-env-pa2lz81q/lib/python3.10/site-packages/aimrocks/include/rocksdb/options.h",
+            "/tmp/build-env-pa2lz81q/lib/python3.10/site-packages/aimrocks/include/rocksdb/slice.h",
+            "/tmp/build-env-pa2lz81q/lib/python3.10/site-packages/aimrocks/include/rocksdb/slice_transform.h",
+            "/tmp/build-env-pa2lz81q/lib/python3.10/site-packages/aimrocks/include/rocksdb/status.h",
+            "/tmp/build-env-pa2lz81q/lib/python3.10/site-packages/aimrocks/include/rocksdb/table.h",
+            "/tmp/build-env-pa2lz81q/lib/python3.10/site-packages/aimrocks/include/rocksdb/universal_compaction.h",
+            "/tmp/build-env-pa2lz81q/lib/python3.10/site-packages/aimrocks/include/rocksdb/utilities/backup_engine.h",
+            "/tmp/build-env-pa2lz81q/lib/python3.10/site-packages/aimrocks/include/rocksdb/write_batch.h"
         ],
         "extra_compile_args": [
             "-std=c++11",
             "-O3",
             "-Wall",
             "-Wextra",
             "-Wconversion",
             "-fno-strict-aliasing",
             "-fno-rtti",
             "-fPIC"
         ],
         "include_dirs": [
-            "/tmp/build-env-347o2c0y/lib/python3.10/site-packages/aimrocks/include"
+            "/tmp/build-env-pa2lz81q/lib/python3.10/site-packages/aimrocks/include"
         ],
         "language": "c++",
         "libraries": [
             "rocksdb"
         ],
         "library_dirs": [
-            "/tmp/build-env-347o2c0y/lib/python3.10/site-packages/aimrocks"
+            "/tmp/build-env-pa2lz81q/lib/python3.10/site-packages/aimrocks"
         ],
         "name": "aim.storage.container",
         "sources": [
             "aim/storage/container.py"
         ]
     },
     "module_name": "aim.storage.container"
```

### Comparing `aim-4.0.0.dev1/aim/storage/container.pxd` & `aim-4.0.0.dev2/aim/storage/container.pxd`

 * *Files identical despite different names*

### Comparing `aim-4.0.0.dev1/aim/storage/container.py` & `aim-4.0.0.dev2/aim/storage/container.py`

 * *Files identical despite different names*

### Comparing `aim-4.0.0.dev1/aim/storage/containertreeview.cpp` & `aim-4.0.0.dev2/aim/storage/containertreeview.cpp`

 * *Files 0% similar despite different names*

```diff
@@ -1,56 +1,56 @@
 /* Generated by Cython 3.0.0a11 */
 
 /* BEGIN: Cython Metadata
 {
     "distutils": {
         "depends": [
-            "/tmp/build-env-347o2c0y/lib/python3.10/site-packages/aimrocks/include/rdb_include/comparator_wrapper.hpp",
-            "/tmp/build-env-347o2c0y/lib/python3.10/site-packages/aimrocks/include/rdb_include/filter_policy_wrapper.hpp",
-            "/tmp/build-env-347o2c0y/lib/python3.10/site-packages/aimrocks/include/rdb_include/memtable_factories.hpp",
-            "/tmp/build-env-347o2c0y/lib/python3.10/site-packages/aimrocks/include/rdb_include/merge_operator_wrapper.hpp",
-            "/tmp/build-env-347o2c0y/lib/python3.10/site-packages/aimrocks/include/rdb_include/slice_transform_wrapper.hpp",
-            "/tmp/build-env-347o2c0y/lib/python3.10/site-packages/aimrocks/include/rdb_include/utils.hpp",
-            "/tmp/build-env-347o2c0y/lib/python3.10/site-packages/aimrocks/include/rdb_include/write_batch_iter_helper.hpp",
-            "/tmp/build-env-347o2c0y/lib/python3.10/site-packages/aimrocks/include/rocksdb/cache.h",
-            "/tmp/build-env-347o2c0y/lib/python3.10/site-packages/aimrocks/include/rocksdb/comparator.h",
-            "/tmp/build-env-347o2c0y/lib/python3.10/site-packages/aimrocks/include/rocksdb/db.h",
-            "/tmp/build-env-347o2c0y/lib/python3.10/site-packages/aimrocks/include/rocksdb/env.h",
-            "/tmp/build-env-347o2c0y/lib/python3.10/site-packages/aimrocks/include/rocksdb/filter_policy.h",
-            "/tmp/build-env-347o2c0y/lib/python3.10/site-packages/aimrocks/include/rocksdb/iterator.h",
-            "/tmp/build-env-347o2c0y/lib/python3.10/site-packages/aimrocks/include/rocksdb/memtablerep.h",
-            "/tmp/build-env-347o2c0y/lib/python3.10/site-packages/aimrocks/include/rocksdb/merge_operator.h",
-            "/tmp/build-env-347o2c0y/lib/python3.10/site-packages/aimrocks/include/rocksdb/options.h",
-            "/tmp/build-env-347o2c0y/lib/python3.10/site-packages/aimrocks/include/rocksdb/slice.h",
-            "/tmp/build-env-347o2c0y/lib/python3.10/site-packages/aimrocks/include/rocksdb/slice_transform.h",
-            "/tmp/build-env-347o2c0y/lib/python3.10/site-packages/aimrocks/include/rocksdb/status.h",
-            "/tmp/build-env-347o2c0y/lib/python3.10/site-packages/aimrocks/include/rocksdb/table.h",
-            "/tmp/build-env-347o2c0y/lib/python3.10/site-packages/aimrocks/include/rocksdb/universal_compaction.h",
-            "/tmp/build-env-347o2c0y/lib/python3.10/site-packages/aimrocks/include/rocksdb/utilities/backup_engine.h",
-            "/tmp/build-env-347o2c0y/lib/python3.10/site-packages/aimrocks/include/rocksdb/write_batch.h"
+            "/tmp/build-env-pa2lz81q/lib/python3.10/site-packages/aimrocks/include/rdb_include/comparator_wrapper.hpp",
+            "/tmp/build-env-pa2lz81q/lib/python3.10/site-packages/aimrocks/include/rdb_include/filter_policy_wrapper.hpp",
+            "/tmp/build-env-pa2lz81q/lib/python3.10/site-packages/aimrocks/include/rdb_include/memtable_factories.hpp",
+            "/tmp/build-env-pa2lz81q/lib/python3.10/site-packages/aimrocks/include/rdb_include/merge_operator_wrapper.hpp",
+            "/tmp/build-env-pa2lz81q/lib/python3.10/site-packages/aimrocks/include/rdb_include/slice_transform_wrapper.hpp",
+            "/tmp/build-env-pa2lz81q/lib/python3.10/site-packages/aimrocks/include/rdb_include/utils.hpp",
+            "/tmp/build-env-pa2lz81q/lib/python3.10/site-packages/aimrocks/include/rdb_include/write_batch_iter_helper.hpp",
+            "/tmp/build-env-pa2lz81q/lib/python3.10/site-packages/aimrocks/include/rocksdb/cache.h",
+            "/tmp/build-env-pa2lz81q/lib/python3.10/site-packages/aimrocks/include/rocksdb/comparator.h",
+            "/tmp/build-env-pa2lz81q/lib/python3.10/site-packages/aimrocks/include/rocksdb/db.h",
+            "/tmp/build-env-pa2lz81q/lib/python3.10/site-packages/aimrocks/include/rocksdb/env.h",
+            "/tmp/build-env-pa2lz81q/lib/python3.10/site-packages/aimrocks/include/rocksdb/filter_policy.h",
+            "/tmp/build-env-pa2lz81q/lib/python3.10/site-packages/aimrocks/include/rocksdb/iterator.h",
+            "/tmp/build-env-pa2lz81q/lib/python3.10/site-packages/aimrocks/include/rocksdb/memtablerep.h",
+            "/tmp/build-env-pa2lz81q/lib/python3.10/site-packages/aimrocks/include/rocksdb/merge_operator.h",
+            "/tmp/build-env-pa2lz81q/lib/python3.10/site-packages/aimrocks/include/rocksdb/options.h",
+            "/tmp/build-env-pa2lz81q/lib/python3.10/site-packages/aimrocks/include/rocksdb/slice.h",
+            "/tmp/build-env-pa2lz81q/lib/python3.10/site-packages/aimrocks/include/rocksdb/slice_transform.h",
+            "/tmp/build-env-pa2lz81q/lib/python3.10/site-packages/aimrocks/include/rocksdb/status.h",
+            "/tmp/build-env-pa2lz81q/lib/python3.10/site-packages/aimrocks/include/rocksdb/table.h",
+            "/tmp/build-env-pa2lz81q/lib/python3.10/site-packages/aimrocks/include/rocksdb/universal_compaction.h",
+            "/tmp/build-env-pa2lz81q/lib/python3.10/site-packages/aimrocks/include/rocksdb/utilities/backup_engine.h",
+            "/tmp/build-env-pa2lz81q/lib/python3.10/site-packages/aimrocks/include/rocksdb/write_batch.h"
         ],
         "extra_compile_args": [
             "-std=c++11",
             "-O3",
             "-Wall",
             "-Wextra",
             "-Wconversion",
             "-fno-strict-aliasing",
             "-fno-rtti",
             "-fPIC"
         ],
         "include_dirs": [
-            "/tmp/build-env-347o2c0y/lib/python3.10/site-packages/aimrocks/include"
+            "/tmp/build-env-pa2lz81q/lib/python3.10/site-packages/aimrocks/include"
         ],
         "language": "c++",
         "libraries": [
             "rocksdb"
         ],
         "library_dirs": [
-            "/tmp/build-env-347o2c0y/lib/python3.10/site-packages/aimrocks"
+            "/tmp/build-env-pa2lz81q/lib/python3.10/site-packages/aimrocks"
         ],
         "name": "aim.storage.containertreeview",
         "sources": [
             "aim/storage/containertreeview.py"
         ]
     },
     "module_name": "aim.storage.containertreeview"
```

### Comparing `aim-4.0.0.dev1/aim/storage/containertreeview.py` & `aim-4.0.0.dev2/aim/storage/containertreeview.py`

 * *Files identical despite different names*

### Comparing `aim-4.0.0.dev1/aim/storage/context.py` & `aim-4.0.0.dev2/aim/storage/context.py`

 * *Files identical despite different names*

### Comparing `aim-4.0.0.dev1/aim/storage/encoding/__init__.cpp` & `aim-4.0.0.dev2/aim/storage/encoding/__init__.cpp`

 * *Files 0% similar despite different names*

```diff
@@ -11,22 +11,22 @@
             "-Wextra",
             "-Wconversion",
             "-fno-strict-aliasing",
             "-fno-rtti",
             "-fPIC"
         ],
         "include_dirs": [
-            "/tmp/build-env-347o2c0y/lib/python3.10/site-packages/aimrocks/include"
+            "/tmp/build-env-pa2lz81q/lib/python3.10/site-packages/aimrocks/include"
         ],
         "language": "c++",
         "libraries": [
             "rocksdb"
         ],
         "library_dirs": [
-            "/tmp/build-env-347o2c0y/lib/python3.10/site-packages/aimrocks"
+            "/tmp/build-env-pa2lz81q/lib/python3.10/site-packages/aimrocks"
         ],
         "name": "aim.storage.encoding",
         "sources": [
             "aim/storage/encoding/__init__.py"
         ]
     },
     "module_name": "aim.storage.encoding"
```

### Comparing `aim-4.0.0.dev1/aim/storage/encoding/encoding.cpp` & `aim-4.0.0.dev2/aim/storage/encoding/encoding.cpp`

 * *Files 0% similar despite different names*

```diff
@@ -11,22 +11,22 @@
             "-Wextra",
             "-Wconversion",
             "-fno-strict-aliasing",
             "-fno-rtti",
             "-fPIC"
         ],
         "include_dirs": [
-            "/tmp/build-env-347o2c0y/lib/python3.10/site-packages/aimrocks/include"
+            "/tmp/build-env-pa2lz81q/lib/python3.10/site-packages/aimrocks/include"
         ],
         "language": "c++",
         "libraries": [
             "rocksdb"
         ],
         "library_dirs": [
-            "/tmp/build-env-347o2c0y/lib/python3.10/site-packages/aimrocks"
+            "/tmp/build-env-pa2lz81q/lib/python3.10/site-packages/aimrocks"
         ],
         "name": "aim.storage.encoding.encoding",
         "sources": [
             "aim/storage/encoding/encoding.pyx"
         ]
     },
     "module_name": "aim.storage.encoding.encoding"
```

### Comparing `aim-4.0.0.dev1/aim/storage/encoding/encoding.pyx` & `aim-4.0.0.dev2/aim/storage/encoding/encoding.pyx`

 * *Files identical despite different names*

### Comparing `aim-4.0.0.dev1/aim/storage/encoding/encoding_native.cpp` & `aim-4.0.0.dev2/aim/storage/encoding/encoding_native.cpp`

 * *Files 0% similar despite different names*

```diff
@@ -11,22 +11,22 @@
             "-Wextra",
             "-Wconversion",
             "-fno-strict-aliasing",
             "-fno-rtti",
             "-fPIC"
         ],
         "include_dirs": [
-            "/tmp/build-env-347o2c0y/lib/python3.10/site-packages/aimrocks/include"
+            "/tmp/build-env-pa2lz81q/lib/python3.10/site-packages/aimrocks/include"
         ],
         "language": "c++",
         "libraries": [
             "rocksdb"
         ],
         "library_dirs": [
-            "/tmp/build-env-347o2c0y/lib/python3.10/site-packages/aimrocks"
+            "/tmp/build-env-pa2lz81q/lib/python3.10/site-packages/aimrocks"
         ],
         "name": "aim.storage.encoding.encoding_native",
         "sources": [
             "aim/storage/encoding/encoding_native.pyx"
         ]
     },
     "module_name": "aim.storage.encoding.encoding_native"
```

### Comparing `aim-4.0.0.dev1/aim/storage/encoding/encoding_native.pxd` & `aim-4.0.0.dev2/aim/storage/encoding/encoding_native.pxd`

 * *Files identical despite different names*

### Comparing `aim-4.0.0.dev1/aim/storage/encoding/encoding_native.pyx` & `aim-4.0.0.dev2/aim/storage/encoding/encoding_native.pyx`

 * *Files identical despite different names*

### Comparing `aim-4.0.0.dev1/aim/storage/hashing/__init__.cpp` & `aim-4.0.0.dev2/aim/storage/hashing/__init__.cpp`

 * *Files 0% similar despite different names*

```diff
@@ -14,22 +14,22 @@
             "-Wconversion",
             "-fno-strict-aliasing",
             "-fno-rtti",
             "-fPIC"
         ],
         "include_dirs": [
             "aim/storage/hashing",
-            "/tmp/build-env-347o2c0y/lib/python3.10/site-packages/aimrocks/include"
+            "/tmp/build-env-pa2lz81q/lib/python3.10/site-packages/aimrocks/include"
         ],
         "language": "c++",
         "libraries": [
             "rocksdb"
         ],
         "library_dirs": [
-            "/tmp/build-env-347o2c0y/lib/python3.10/site-packages/aimrocks"
+            "/tmp/build-env-pa2lz81q/lib/python3.10/site-packages/aimrocks"
         ],
         "name": "aim.storage.hashing",
         "sources": [
             "aim/storage/hashing/__init__.py"
         ]
     },
     "module_name": "aim.storage.hashing"
```

### Comparing `aim-4.0.0.dev1/aim/storage/hashing/c_hash.cpp` & `aim-4.0.0.dev2/aim/storage/hashing/c_hash.cpp`

 * *Files 0% similar despite different names*

```diff
@@ -14,23 +14,23 @@
             "-Wconversion",
             "-fno-strict-aliasing",
             "-fno-rtti",
             "-fPIC"
         ],
         "include_dirs": [
             "aim/storage/hashing",
-            "/tmp/build-env-347o2c0y/lib/python3.10/site-packages/aimrocks/include"
+            "/tmp/build-env-pa2lz81q/lib/python3.10/site-packages/aimrocks/include"
         ],
         "language": "c++",
         "language_level": "3",
         "libraries": [
             "rocksdb"
         ],
         "library_dirs": [
-            "/tmp/build-env-347o2c0y/lib/python3.10/site-packages/aimrocks"
+            "/tmp/build-env-pa2lz81q/lib/python3.10/site-packages/aimrocks"
         ],
         "name": "aim.storage.hashing.c_hash",
         "sources": [
             "aim/storage/hashing/c_hash.pyx"
         ]
     },
     "module_name": "aim.storage.hashing.c_hash"
```

### Comparing `aim-4.0.0.dev1/aim/storage/hashing/c_hash.pyx` & `aim-4.0.0.dev2/aim/storage/hashing/c_hash.pyx`

 * *Files identical despite different names*

### Comparing `aim-4.0.0.dev1/aim/storage/hashing/hash/hash.h` & `aim-4.0.0.dev2/aim/storage/hashing/hash/hash.h`

 * *Files identical despite different names*

### Comparing `aim-4.0.0.dev1/aim/storage/hashing/hashing.cpp` & `aim-4.0.0.dev2/aim/storage/hashing/hashing.cpp`

 * *Files 0% similar despite different names*

```diff
@@ -14,22 +14,22 @@
             "-Wconversion",
             "-fno-strict-aliasing",
             "-fno-rtti",
             "-fPIC"
         ],
         "include_dirs": [
             "aim/storage/hashing",
-            "/tmp/build-env-347o2c0y/lib/python3.10/site-packages/aimrocks/include"
+            "/tmp/build-env-pa2lz81q/lib/python3.10/site-packages/aimrocks/include"
         ],
         "language": "c++",
         "libraries": [
             "rocksdb"
         ],
         "library_dirs": [
-            "/tmp/build-env-347o2c0y/lib/python3.10/site-packages/aimrocks"
+            "/tmp/build-env-pa2lz81q/lib/python3.10/site-packages/aimrocks"
         ],
         "name": "aim.storage.hashing.hashing",
         "sources": [
             "aim/storage/hashing/hashing.py"
         ]
     },
     "module_name": "aim.storage.hashing.hashing"
```

### Comparing `aim-4.0.0.dev1/aim/storage/hashing/hashing.pxd` & `aim-4.0.0.dev2/aim/storage/hashing/hashing.pxd`

 * *Files identical despite different names*

### Comparing `aim-4.0.0.dev1/aim/storage/hashing/hashing.py` & `aim-4.0.0.dev2/aim/storage/hashing/hashing.py`

 * *Files identical despite different names*

### Comparing `aim-4.0.0.dev1/aim/storage/inmemorytreeview.cpp` & `aim-4.0.0.dev2/aim/storage/inmemorytreeview.cpp`

 * *Files 0% similar despite different names*

```diff
@@ -10,22 +10,22 @@
             "-Wextra",
             "-Wconversion",
             "-fno-strict-aliasing",
             "-fno-rtti",
             "-fPIC"
         ],
         "include_dirs": [
-            "/tmp/build-env-347o2c0y/lib/python3.10/site-packages/aimrocks/include"
+            "/tmp/build-env-pa2lz81q/lib/python3.10/site-packages/aimrocks/include"
         ],
         "language": "c++",
         "libraries": [
             "rocksdb"
         ],
         "library_dirs": [
-            "/tmp/build-env-347o2c0y/lib/python3.10/site-packages/aimrocks"
+            "/tmp/build-env-pa2lz81q/lib/python3.10/site-packages/aimrocks"
         ],
         "name": "aim.storage.inmemorytreeview",
         "sources": [
             "aim/storage/inmemorytreeview.py"
         ]
     },
     "module_name": "aim.storage.inmemorytreeview"
```

### Comparing `aim-4.0.0.dev1/aim/storage/inmemorytreeview.py` & `aim-4.0.0.dev2/aim/storage/inmemorytreeview.py`

 * *Files identical despite different names*

### Comparing `aim-4.0.0.dev1/aim/storage/lock_proxy.py` & `aim-4.0.0.dev2/aim/storage/lock_proxy.py`

 * *Files identical despite different names*

### Comparing `aim-4.0.0.dev1/aim/storage/locking.py` & `aim-4.0.0.dev2/aim/storage/locking.py`

 * *Files 1% similar despite different names*

```diff
@@ -24,15 +24,15 @@
     (e.g. remote filesystems, including NFS<4, BeeGFS, Lustre, etc.)
     """
     GLOBAL_FILE_LOCK_CAPABLE_FILESYSTEMS: Set[str] = {
         # The most popular local filesystems
         'ext3', 'ext4', 'xfs', 'zfs', 'apfs',
         # We include only NFS v4 filesystems here (yet).
         # NFS v3 does not support file locks.
-        'nfs4',
+        'nfs4', 'ceph',
     }
     warned_devices: Set[int] = set()
 
     @classmethod
     def _warn_only_once(
         cls,
         path: str,
```

### Comparing `aim-4.0.0.dev1/aim/storage/migrations/alembic.ini` & `aim-4.0.0.dev2/aim/storage/migrations/alembic.ini`

 * *Files identical despite different names*

### Comparing `aim-4.0.0.dev1/aim/storage/migrations/alembic_dev.ini` & `aim-4.0.0.dev2/aim/storage/migrations/alembic_dev.ini`

 * *Files identical despite different names*

### Comparing `aim-4.0.0.dev1/aim/storage/migrations/env.py` & `aim-4.0.0.dev2/aim/storage/migrations/env.py`

 * *Files identical despite different names*

### Comparing `aim-4.0.0.dev1/aim/storage/migrations/utils.py` & `aim-4.0.0.dev2/aim/storage/migrations/utils.py`

 * *Files identical despite different names*

### Comparing `aim-4.0.0.dev1/aim/storage/migrations/versions/1ecf8222220d_initial_schema.py` & `aim-4.0.0.dev2/aim/storage/migrations/versions/1ecf8222220d_initial_schema.py`

 * *Files identical despite different names*

### Comparing `aim-4.0.0.dev1/aim/storage/migrations/versions/3c4f22db7a46_run_end_time.py` & `aim-4.0.0.dev2/aim/storage/migrations/versions/3c4f22db7a46_run_end_time.py`

 * *Files identical despite different names*

### Comparing `aim-4.0.0.dev1/aim/storage/migrations/versions/46b89d830ad8_.py` & `aim-4.0.0.dev2/aim/storage/migrations/versions/46b89d830ad8_.py`

 * *Files identical despite different names*

### Comparing `aim-4.0.0.dev1/aim/storage/migrations/versions/9ba30ab3b2b4_.py` & `aim-4.0.0.dev2/aim/storage/migrations/versions/9ba30ab3b2b4_.py`

 * *Files identical despite different names*

### Comparing `aim-4.0.0.dev1/aim/storage/migrations/versions/b07e7b07c8ce_.py` & `aim-4.0.0.dev2/aim/storage/migrations/versions/b07e7b07c8ce_.py`

 * *Files identical despite different names*

### Comparing `aim-4.0.0.dev1/aim/storage/migrations/versions/fbfe5c4702fb_soft_delete.py` & `aim-4.0.0.dev2/aim/storage/migrations/versions/fbfe5c4702fb_soft_delete.py`

 * *Files identical despite different names*

### Comparing `aim-4.0.0.dev1/aim/storage/object.py` & `aim-4.0.0.dev2/aim/storage/object.py`

 * *Files identical despite different names*

### Comparing `aim-4.0.0.dev1/aim/storage/prefixview.cpp` & `aim-4.0.0.dev2/aim/storage/prefixview.cpp`

 * *Files 1% similar despite different names*

```diff
@@ -1,56 +1,56 @@
 /* Generated by Cython 3.0.0a11 */
 
 /* BEGIN: Cython Metadata
 {
     "distutils": {
         "depends": [
-            "/tmp/build-env-347o2c0y/lib/python3.10/site-packages/aimrocks/include/rdb_include/comparator_wrapper.hpp",
-            "/tmp/build-env-347o2c0y/lib/python3.10/site-packages/aimrocks/include/rdb_include/filter_policy_wrapper.hpp",
-            "/tmp/build-env-347o2c0y/lib/python3.10/site-packages/aimrocks/include/rdb_include/memtable_factories.hpp",
-            "/tmp/build-env-347o2c0y/lib/python3.10/site-packages/aimrocks/include/rdb_include/merge_operator_wrapper.hpp",
-            "/tmp/build-env-347o2c0y/lib/python3.10/site-packages/aimrocks/include/rdb_include/slice_transform_wrapper.hpp",
-            "/tmp/build-env-347o2c0y/lib/python3.10/site-packages/aimrocks/include/rdb_include/utils.hpp",
-            "/tmp/build-env-347o2c0y/lib/python3.10/site-packages/aimrocks/include/rdb_include/write_batch_iter_helper.hpp",
-            "/tmp/build-env-347o2c0y/lib/python3.10/site-packages/aimrocks/include/rocksdb/cache.h",
-            "/tmp/build-env-347o2c0y/lib/python3.10/site-packages/aimrocks/include/rocksdb/comparator.h",
-            "/tmp/build-env-347o2c0y/lib/python3.10/site-packages/aimrocks/include/rocksdb/db.h",
-            "/tmp/build-env-347o2c0y/lib/python3.10/site-packages/aimrocks/include/rocksdb/env.h",
-            "/tmp/build-env-347o2c0y/lib/python3.10/site-packages/aimrocks/include/rocksdb/filter_policy.h",
-            "/tmp/build-env-347o2c0y/lib/python3.10/site-packages/aimrocks/include/rocksdb/iterator.h",
-            "/tmp/build-env-347o2c0y/lib/python3.10/site-packages/aimrocks/include/rocksdb/memtablerep.h",
-            "/tmp/build-env-347o2c0y/lib/python3.10/site-packages/aimrocks/include/rocksdb/merge_operator.h",
-            "/tmp/build-env-347o2c0y/lib/python3.10/site-packages/aimrocks/include/rocksdb/options.h",
-            "/tmp/build-env-347o2c0y/lib/python3.10/site-packages/aimrocks/include/rocksdb/slice.h",
-            "/tmp/build-env-347o2c0y/lib/python3.10/site-packages/aimrocks/include/rocksdb/slice_transform.h",
-            "/tmp/build-env-347o2c0y/lib/python3.10/site-packages/aimrocks/include/rocksdb/status.h",
-            "/tmp/build-env-347o2c0y/lib/python3.10/site-packages/aimrocks/include/rocksdb/table.h",
-            "/tmp/build-env-347o2c0y/lib/python3.10/site-packages/aimrocks/include/rocksdb/universal_compaction.h",
-            "/tmp/build-env-347o2c0y/lib/python3.10/site-packages/aimrocks/include/rocksdb/utilities/backup_engine.h",
-            "/tmp/build-env-347o2c0y/lib/python3.10/site-packages/aimrocks/include/rocksdb/write_batch.h"
+            "/tmp/build-env-pa2lz81q/lib/python3.10/site-packages/aimrocks/include/rdb_include/comparator_wrapper.hpp",
+            "/tmp/build-env-pa2lz81q/lib/python3.10/site-packages/aimrocks/include/rdb_include/filter_policy_wrapper.hpp",
+            "/tmp/build-env-pa2lz81q/lib/python3.10/site-packages/aimrocks/include/rdb_include/memtable_factories.hpp",
+            "/tmp/build-env-pa2lz81q/lib/python3.10/site-packages/aimrocks/include/rdb_include/merge_operator_wrapper.hpp",
+            "/tmp/build-env-pa2lz81q/lib/python3.10/site-packages/aimrocks/include/rdb_include/slice_transform_wrapper.hpp",
+            "/tmp/build-env-pa2lz81q/lib/python3.10/site-packages/aimrocks/include/rdb_include/utils.hpp",
+            "/tmp/build-env-pa2lz81q/lib/python3.10/site-packages/aimrocks/include/rdb_include/write_batch_iter_helper.hpp",
+            "/tmp/build-env-pa2lz81q/lib/python3.10/site-packages/aimrocks/include/rocksdb/cache.h",
+            "/tmp/build-env-pa2lz81q/lib/python3.10/site-packages/aimrocks/include/rocksdb/comparator.h",
+            "/tmp/build-env-pa2lz81q/lib/python3.10/site-packages/aimrocks/include/rocksdb/db.h",
+            "/tmp/build-env-pa2lz81q/lib/python3.10/site-packages/aimrocks/include/rocksdb/env.h",
+            "/tmp/build-env-pa2lz81q/lib/python3.10/site-packages/aimrocks/include/rocksdb/filter_policy.h",
+            "/tmp/build-env-pa2lz81q/lib/python3.10/site-packages/aimrocks/include/rocksdb/iterator.h",
+            "/tmp/build-env-pa2lz81q/lib/python3.10/site-packages/aimrocks/include/rocksdb/memtablerep.h",
+            "/tmp/build-env-pa2lz81q/lib/python3.10/site-packages/aimrocks/include/rocksdb/merge_operator.h",
+            "/tmp/build-env-pa2lz81q/lib/python3.10/site-packages/aimrocks/include/rocksdb/options.h",
+            "/tmp/build-env-pa2lz81q/lib/python3.10/site-packages/aimrocks/include/rocksdb/slice.h",
+            "/tmp/build-env-pa2lz81q/lib/python3.10/site-packages/aimrocks/include/rocksdb/slice_transform.h",
+            "/tmp/build-env-pa2lz81q/lib/python3.10/site-packages/aimrocks/include/rocksdb/status.h",
+            "/tmp/build-env-pa2lz81q/lib/python3.10/site-packages/aimrocks/include/rocksdb/table.h",
+            "/tmp/build-env-pa2lz81q/lib/python3.10/site-packages/aimrocks/include/rocksdb/universal_compaction.h",
+            "/tmp/build-env-pa2lz81q/lib/python3.10/site-packages/aimrocks/include/rocksdb/utilities/backup_engine.h",
+            "/tmp/build-env-pa2lz81q/lib/python3.10/site-packages/aimrocks/include/rocksdb/write_batch.h"
         ],
         "extra_compile_args": [
             "-std=c++11",
             "-O3",
             "-Wall",
             "-Wextra",
             "-Wconversion",
             "-fno-strict-aliasing",
             "-fno-rtti",
             "-fPIC"
         ],
         "include_dirs": [
-            "/tmp/build-env-347o2c0y/lib/python3.10/site-packages/aimrocks/include"
+            "/tmp/build-env-pa2lz81q/lib/python3.10/site-packages/aimrocks/include"
         ],
         "language": "c++",
         "libraries": [
             "rocksdb"
         ],
         "library_dirs": [
-            "/tmp/build-env-347o2c0y/lib/python3.10/site-packages/aimrocks"
+            "/tmp/build-env-pa2lz81q/lib/python3.10/site-packages/aimrocks"
         ],
         "name": "aim.storage.prefixview",
         "sources": [
             "aim/storage/prefixview.py"
         ]
     },
     "module_name": "aim.storage.prefixview"
```

### Comparing `aim-4.0.0.dev1/aim/storage/prefixview.pxd` & `aim-4.0.0.dev2/aim/storage/prefixview.pxd`

 * *Files identical despite different names*

### Comparing `aim-4.0.0.dev1/aim/storage/prefixview.py` & `aim-4.0.0.dev2/aim/storage/prefixview.py`

 * *Files identical despite different names*

### Comparing `aim-4.0.0.dev1/aim/storage/proxy.py` & `aim-4.0.0.dev2/aim/storage/proxy.py`

 * *Files identical despite different names*

### Comparing `aim-4.0.0.dev1/aim/storage/query.py` & `aim-4.0.0.dev2/aim/storage/query.py`

 * *Files identical despite different names*

### Comparing `aim-4.0.0.dev1/aim/storage/rockscontainer.cpp` & `aim-4.0.0.dev2/aim/storage/rockscontainer.cpp`

 * *Files 0% similar despite different names*

```diff
@@ -10,22 +10,22 @@
             "-Wextra",
             "-Wconversion",
             "-fno-strict-aliasing",
             "-fno-rtti",
             "-fPIC"
         ],
         "include_dirs": [
-            "/tmp/build-env-347o2c0y/lib/python3.10/site-packages/aimrocks/include"
+            "/tmp/build-env-pa2lz81q/lib/python3.10/site-packages/aimrocks/include"
         ],
         "language": "c++",
         "libraries": [
             "rocksdb"
         ],
         "library_dirs": [
-            "/tmp/build-env-347o2c0y/lib/python3.10/site-packages/aimrocks"
+            "/tmp/build-env-pa2lz81q/lib/python3.10/site-packages/aimrocks"
         ],
         "name": "aim.storage.rockscontainer",
         "sources": [
             "aim/storage/rockscontainer.pyx"
         ]
     },
     "module_name": "aim.storage.rockscontainer"
```

### Comparing `aim-4.0.0.dev1/aim/storage/rockscontainer.pyx` & `aim-4.0.0.dev2/aim/storage/rockscontainer.pyx`

 * *Files identical despite different names*

### Comparing `aim-4.0.0.dev1/aim/storage/structured/db.py` & `aim-4.0.0.dev2/aim/storage/structured/db.py`

 * *Files identical despite different names*

### Comparing `aim-4.0.0.dev1/aim/storage/structured/entities.py` & `aim-4.0.0.dev2/aim/storage/structured/entities.py`

 * *Files identical despite different names*

### Comparing `aim-4.0.0.dev1/aim/storage/structured/proxy.py` & `aim-4.0.0.dev2/aim/storage/structured/proxy.py`

 * *Files identical despite different names*

### Comparing `aim-4.0.0.dev1/aim/storage/structured/sql_engine/entities.py` & `aim-4.0.0.dev2/aim/storage/structured/sql_engine/entities.py`

 * *Files identical despite different names*

### Comparing `aim-4.0.0.dev1/aim/storage/structured/sql_engine/factory.py` & `aim-4.0.0.dev2/aim/storage/structured/sql_engine/factory.py`

 * *Files identical despite different names*

### Comparing `aim-4.0.0.dev1/aim/storage/structured/sql_engine/models.py` & `aim-4.0.0.dev2/aim/storage/structured/sql_engine/models.py`

 * *Files identical despite different names*

### Comparing `aim-4.0.0.dev1/aim/storage/structured/sql_engine/utils.py` & `aim-4.0.0.dev2/aim/storage/structured/sql_engine/utils.py`

 * *Files identical despite different names*

### Comparing `aim-4.0.0.dev1/aim/storage/treearrayview.cpp` & `aim-4.0.0.dev2/aim/storage/treearrayview.cpp`

 * *Files 0% similar despite different names*

```diff
@@ -10,22 +10,22 @@
             "-Wextra",
             "-Wconversion",
             "-fno-strict-aliasing",
             "-fno-rtti",
             "-fPIC"
         ],
         "include_dirs": [
-            "/tmp/build-env-347o2c0y/lib/python3.10/site-packages/aimrocks/include"
+            "/tmp/build-env-pa2lz81q/lib/python3.10/site-packages/aimrocks/include"
         ],
         "language": "c++",
         "libraries": [
             "rocksdb"
         ],
         "library_dirs": [
-            "/tmp/build-env-347o2c0y/lib/python3.10/site-packages/aimrocks"
+            "/tmp/build-env-pa2lz81q/lib/python3.10/site-packages/aimrocks"
         ],
         "name": "aim.storage.treearrayview",
         "sources": [
             "aim/storage/treearrayview.py"
         ]
     },
     "module_name": "aim.storage.treearrayview"
```

### Comparing `aim-4.0.0.dev1/aim/storage/treearrayview.py` & `aim-4.0.0.dev2/aim/storage/treearrayview.py`

 * *Files identical despite different names*

### Comparing `aim-4.0.0.dev1/aim/storage/treeutils.cpp` & `aim-4.0.0.dev2/aim/storage/treeutils.cpp`

 * *Files 0% similar despite different names*

```diff
@@ -11,22 +11,22 @@
             "-Wextra",
             "-Wconversion",
             "-fno-strict-aliasing",
             "-fno-rtti",
             "-fPIC"
         ],
         "include_dirs": [
-            "/tmp/build-env-347o2c0y/lib/python3.10/site-packages/aimrocks/include"
+            "/tmp/build-env-pa2lz81q/lib/python3.10/site-packages/aimrocks/include"
         ],
         "language": "c++",
         "libraries": [
             "rocksdb"
         ],
         "library_dirs": [
-            "/tmp/build-env-347o2c0y/lib/python3.10/site-packages/aimrocks"
+            "/tmp/build-env-pa2lz81q/lib/python3.10/site-packages/aimrocks"
         ],
         "name": "aim.storage.treeutils",
         "sources": [
             "aim/storage/treeutils.pyx"
         ]
     },
     "module_name": "aim.storage.treeutils"
```

### Comparing `aim-4.0.0.dev1/aim/storage/treeutils.pyx` & `aim-4.0.0.dev2/aim/storage/treeutils.pyx`

 * *Files identical despite different names*

### Comparing `aim-4.0.0.dev1/aim/storage/treeutils_non_native.py` & `aim-4.0.0.dev2/aim/storage/treeutils_non_native.py`

 * *Files identical despite different names*

### Comparing `aim-4.0.0.dev1/aim/storage/treeview.cpp` & `aim-4.0.0.dev2/aim/storage/treeview.cpp`

 * *Files 0% similar despite different names*

```diff
@@ -10,22 +10,22 @@
             "-Wextra",
             "-Wconversion",
             "-fno-strict-aliasing",
             "-fno-rtti",
             "-fPIC"
         ],
         "include_dirs": [
-            "/tmp/build-env-347o2c0y/lib/python3.10/site-packages/aimrocks/include"
+            "/tmp/build-env-pa2lz81q/lib/python3.10/site-packages/aimrocks/include"
         ],
         "language": "c++",
         "libraries": [
             "rocksdb"
         ],
         "library_dirs": [
-            "/tmp/build-env-347o2c0y/lib/python3.10/site-packages/aimrocks"
+            "/tmp/build-env-pa2lz81q/lib/python3.10/site-packages/aimrocks"
         ],
         "name": "aim.storage.treeview",
         "sources": [
             "aim/storage/treeview.py"
         ]
     },
     "module_name": "aim.storage.treeview"
```

### Comparing `aim-4.0.0.dev1/aim/storage/treeview.py` & `aim-4.0.0.dev2/aim/storage/treeview.py`

 * *Files identical despite different names*

### Comparing `aim-4.0.0.dev1/aim/storage/treeviewproxy.py` & `aim-4.0.0.dev2/aim/storage/treeviewproxy.py`

 * *Files identical despite different names*

### Comparing `aim-4.0.0.dev1/aim/storage/types.py` & `aim-4.0.0.dev2/aim/storage/types.py`

 * *Files identical despite different names*

### Comparing `aim-4.0.0.dev1/aim/storage/union.cpp` & `aim-4.0.0.dev2/aim/storage/union.cpp`

 * *Files 0% similar despite different names*

```diff
@@ -10,22 +10,22 @@
             "-Wextra",
             "-Wconversion",
             "-fno-strict-aliasing",
             "-fno-rtti",
             "-fPIC"
         ],
         "include_dirs": [
-            "/tmp/build-env-347o2c0y/lib/python3.10/site-packages/aimrocks/include"
+            "/tmp/build-env-pa2lz81q/lib/python3.10/site-packages/aimrocks/include"
         ],
         "language": "c++",
         "libraries": [
             "rocksdb"
         ],
         "library_dirs": [
-            "/tmp/build-env-347o2c0y/lib/python3.10/site-packages/aimrocks"
+            "/tmp/build-env-pa2lz81q/lib/python3.10/site-packages/aimrocks"
         ],
         "name": "aim.storage.union",
         "sources": [
             "aim/storage/union.pyx"
         ]
     },
     "module_name": "aim.storage.union"
```

### Comparing `aim-4.0.0.dev1/aim/storage/union.pyx` & `aim-4.0.0.dev2/aim/storage/union.pyx`

 * *Files identical despite different names*

### Comparing `aim-4.0.0.dev1/aim/storage/utils.cpp` & `aim-4.0.0.dev2/aim/storage/utils.cpp`

 * *Files 1% similar despite different names*

```diff
@@ -1,56 +1,56 @@
 /* Generated by Cython 3.0.0a11 */
 
 /* BEGIN: Cython Metadata
 {
     "distutils": {
         "depends": [
-            "/tmp/build-env-347o2c0y/lib/python3.10/site-packages/aimrocks/include/rdb_include/comparator_wrapper.hpp",
-            "/tmp/build-env-347o2c0y/lib/python3.10/site-packages/aimrocks/include/rdb_include/filter_policy_wrapper.hpp",
-            "/tmp/build-env-347o2c0y/lib/python3.10/site-packages/aimrocks/include/rdb_include/memtable_factories.hpp",
-            "/tmp/build-env-347o2c0y/lib/python3.10/site-packages/aimrocks/include/rdb_include/merge_operator_wrapper.hpp",
-            "/tmp/build-env-347o2c0y/lib/python3.10/site-packages/aimrocks/include/rdb_include/slice_transform_wrapper.hpp",
-            "/tmp/build-env-347o2c0y/lib/python3.10/site-packages/aimrocks/include/rdb_include/utils.hpp",
-            "/tmp/build-env-347o2c0y/lib/python3.10/site-packages/aimrocks/include/rdb_include/write_batch_iter_helper.hpp",
-            "/tmp/build-env-347o2c0y/lib/python3.10/site-packages/aimrocks/include/rocksdb/cache.h",
-            "/tmp/build-env-347o2c0y/lib/python3.10/site-packages/aimrocks/include/rocksdb/comparator.h",
-            "/tmp/build-env-347o2c0y/lib/python3.10/site-packages/aimrocks/include/rocksdb/db.h",
-            "/tmp/build-env-347o2c0y/lib/python3.10/site-packages/aimrocks/include/rocksdb/env.h",
-            "/tmp/build-env-347o2c0y/lib/python3.10/site-packages/aimrocks/include/rocksdb/filter_policy.h",
-            "/tmp/build-env-347o2c0y/lib/python3.10/site-packages/aimrocks/include/rocksdb/iterator.h",
-            "/tmp/build-env-347o2c0y/lib/python3.10/site-packages/aimrocks/include/rocksdb/memtablerep.h",
-            "/tmp/build-env-347o2c0y/lib/python3.10/site-packages/aimrocks/include/rocksdb/merge_operator.h",
-            "/tmp/build-env-347o2c0y/lib/python3.10/site-packages/aimrocks/include/rocksdb/options.h",
-            "/tmp/build-env-347o2c0y/lib/python3.10/site-packages/aimrocks/include/rocksdb/slice.h",
-            "/tmp/build-env-347o2c0y/lib/python3.10/site-packages/aimrocks/include/rocksdb/slice_transform.h",
-            "/tmp/build-env-347o2c0y/lib/python3.10/site-packages/aimrocks/include/rocksdb/status.h",
-            "/tmp/build-env-347o2c0y/lib/python3.10/site-packages/aimrocks/include/rocksdb/table.h",
-            "/tmp/build-env-347o2c0y/lib/python3.10/site-packages/aimrocks/include/rocksdb/universal_compaction.h",
-            "/tmp/build-env-347o2c0y/lib/python3.10/site-packages/aimrocks/include/rocksdb/utilities/backup_engine.h",
-            "/tmp/build-env-347o2c0y/lib/python3.10/site-packages/aimrocks/include/rocksdb/write_batch.h"
+            "/tmp/build-env-pa2lz81q/lib/python3.10/site-packages/aimrocks/include/rdb_include/comparator_wrapper.hpp",
+            "/tmp/build-env-pa2lz81q/lib/python3.10/site-packages/aimrocks/include/rdb_include/filter_policy_wrapper.hpp",
+            "/tmp/build-env-pa2lz81q/lib/python3.10/site-packages/aimrocks/include/rdb_include/memtable_factories.hpp",
+            "/tmp/build-env-pa2lz81q/lib/python3.10/site-packages/aimrocks/include/rdb_include/merge_operator_wrapper.hpp",
+            "/tmp/build-env-pa2lz81q/lib/python3.10/site-packages/aimrocks/include/rdb_include/slice_transform_wrapper.hpp",
+            "/tmp/build-env-pa2lz81q/lib/python3.10/site-packages/aimrocks/include/rdb_include/utils.hpp",
+            "/tmp/build-env-pa2lz81q/lib/python3.10/site-packages/aimrocks/include/rdb_include/write_batch_iter_helper.hpp",
+            "/tmp/build-env-pa2lz81q/lib/python3.10/site-packages/aimrocks/include/rocksdb/cache.h",
+            "/tmp/build-env-pa2lz81q/lib/python3.10/site-packages/aimrocks/include/rocksdb/comparator.h",
+            "/tmp/build-env-pa2lz81q/lib/python3.10/site-packages/aimrocks/include/rocksdb/db.h",
+            "/tmp/build-env-pa2lz81q/lib/python3.10/site-packages/aimrocks/include/rocksdb/env.h",
+            "/tmp/build-env-pa2lz81q/lib/python3.10/site-packages/aimrocks/include/rocksdb/filter_policy.h",
+            "/tmp/build-env-pa2lz81q/lib/python3.10/site-packages/aimrocks/include/rocksdb/iterator.h",
+            "/tmp/build-env-pa2lz81q/lib/python3.10/site-packages/aimrocks/include/rocksdb/memtablerep.h",
+            "/tmp/build-env-pa2lz81q/lib/python3.10/site-packages/aimrocks/include/rocksdb/merge_operator.h",
+            "/tmp/build-env-pa2lz81q/lib/python3.10/site-packages/aimrocks/include/rocksdb/options.h",
+            "/tmp/build-env-pa2lz81q/lib/python3.10/site-packages/aimrocks/include/rocksdb/slice.h",
+            "/tmp/build-env-pa2lz81q/lib/python3.10/site-packages/aimrocks/include/rocksdb/slice_transform.h",
+            "/tmp/build-env-pa2lz81q/lib/python3.10/site-packages/aimrocks/include/rocksdb/status.h",
+            "/tmp/build-env-pa2lz81q/lib/python3.10/site-packages/aimrocks/include/rocksdb/table.h",
+            "/tmp/build-env-pa2lz81q/lib/python3.10/site-packages/aimrocks/include/rocksdb/universal_compaction.h",
+            "/tmp/build-env-pa2lz81q/lib/python3.10/site-packages/aimrocks/include/rocksdb/utilities/backup_engine.h",
+            "/tmp/build-env-pa2lz81q/lib/python3.10/site-packages/aimrocks/include/rocksdb/write_batch.h"
         ],
         "extra_compile_args": [
             "-std=c++11",
             "-O3",
             "-Wall",
             "-Wextra",
             "-Wconversion",
             "-fno-strict-aliasing",
             "-fno-rtti",
             "-fPIC"
         ],
         "include_dirs": [
-            "/tmp/build-env-347o2c0y/lib/python3.10/site-packages/aimrocks/include"
+            "/tmp/build-env-pa2lz81q/lib/python3.10/site-packages/aimrocks/include"
         ],
         "language": "c++",
         "libraries": [
             "rocksdb"
         ],
         "library_dirs": [
-            "/tmp/build-env-347o2c0y/lib/python3.10/site-packages/aimrocks"
+            "/tmp/build-env-pa2lz81q/lib/python3.10/site-packages/aimrocks"
         ],
         "name": "aim.storage.utils",
         "sources": [
             "aim/storage/utils.py"
         ]
     },
     "module_name": "aim.storage.utils"
```

### Comparing `aim-4.0.0.dev1/aim/storage/utils.py` & `aim-4.0.0.dev2/aim/storage/utils.py`

 * *Files identical despite different names*

### Comparing `aim-4.0.0.dev1/aim/utils/deprecation.py` & `aim-4.0.0.dev2/aim/utils/deprecation.py`

 * *Files identical despite different names*

### Comparing `aim-4.0.0.dev1/aim/utils/tracking.py` & `aim-4.0.0.dev2/aim/utils/tracking.py`

 * *Files identical despite different names*

### Comparing `aim-4.0.0.dev1/aim/web/api/__init__.py` & `aim-4.0.0.dev2/aim/web/api/__init__.py`

 * *Files identical despite different names*

### Comparing `aim-4.0.0.dev1/aim/web/api/dashboard_apps/models.py` & `aim-4.0.0.dev2/aim/web/api/dashboard_apps/models.py`

 * *Files identical despite different names*

### Comparing `aim-4.0.0.dev1/aim/web/api/dashboard_apps/pydantic_models.py` & `aim-4.0.0.dev2/aim/web/api/dashboard_apps/pydantic_models.py`

 * *Files identical despite different names*

### Comparing `aim-4.0.0.dev1/aim/web/api/dashboard_apps/views.py` & `aim-4.0.0.dev2/aim/web/api/dashboard_apps/views.py`

 * *Files identical despite different names*

### Comparing `aim-4.0.0.dev1/aim/web/api/dashboards/models.py` & `aim-4.0.0.dev2/aim/web/api/dashboards/models.py`

 * *Files identical despite different names*

### Comparing `aim-4.0.0.dev1/aim/web/api/dashboards/pydantic_models.py` & `aim-4.0.0.dev2/aim/web/api/dashboards/pydantic_models.py`

 * *Files identical despite different names*

### Comparing `aim-4.0.0.dev1/aim/web/api/dashboards/serializers.py` & `aim-4.0.0.dev2/aim/web/api/dashboards/serializers.py`

 * *Files identical despite different names*

### Comparing `aim-4.0.0.dev1/aim/web/api/dashboards/views.py` & `aim-4.0.0.dev2/aim/web/api/dashboards/views.py`

 * *Files identical despite different names*

### Comparing `aim-4.0.0.dev1/aim/web/api/db.py` & `aim-4.0.0.dev2/aim/web/api/db.py`

 * *Files identical despite different names*

### Comparing `aim-4.0.0.dev1/aim/web/api/experiments/pydantic_models.py` & `aim-4.0.0.dev2/aim/web/api/experiments/pydantic_models.py`

 * *Files identical despite different names*

### Comparing `aim-4.0.0.dev1/aim/web/api/experiments/views.py` & `aim-4.0.0.dev2/aim/web/api/experiments/views.py`

 * *Files identical despite different names*

### Comparing `aim-4.0.0.dev1/aim/web/api/projects/project.py` & `aim-4.0.0.dev2/aim/web/api/projects/project.py`

 * *Files identical despite different names*

### Comparing `aim-4.0.0.dev1/aim/web/api/projects/pydantic_models.py` & `aim-4.0.0.dev2/aim/web/api/projects/pydantic_models.py`

 * *Files identical despite different names*

### Comparing `aim-4.0.0.dev1/aim/web/api/projects/views.py` & `aim-4.0.0.dev2/aim/web/api/projects/views.py`

 * *Files identical despite different names*

### Comparing `aim-4.0.0.dev1/aim/web/api/runs/object_api_utils.py` & `aim-4.0.0.dev2/aim/web/api/runs/object_api_utils.py`

 * *Files identical despite different names*

### Comparing `aim-4.0.0.dev1/aim/web/api/runs/object_views.py` & `aim-4.0.0.dev2/aim/web/api/runs/object_views.py`

 * *Files identical despite different names*

### Comparing `aim-4.0.0.dev1/aim/web/api/runs/pydantic_models.py` & `aim-4.0.0.dev2/aim/web/api/runs/pydantic_models.py`

 * *Files identical despite different names*

### Comparing `aim-4.0.0.dev1/aim/web/api/runs/utils.py` & `aim-4.0.0.dev2/aim/web/api/runs/utils.py`

 * *Files identical despite different names*

### Comparing `aim-4.0.0.dev1/aim/web/api/runs/views.py` & `aim-4.0.0.dev2/aim/web/api/runs/views.py`

 * *Files identical despite different names*

### Comparing `aim-4.0.0.dev1/aim/web/api/tags/pydantic_models.py` & `aim-4.0.0.dev2/aim/web/api/tags/pydantic_models.py`

 * *Files identical despite different names*

### Comparing `aim-4.0.0.dev1/aim/web/api/tags/views.py` & `aim-4.0.0.dev2/aim/web/api/tags/views.py`

 * *Files identical despite different names*

### Comparing `aim-4.0.0.dev1/aim/web/api/utils.py` & `aim-4.0.0.dev2/aim/web/api/utils.py`

 * *Files identical despite different names*

### Comparing `aim-4.0.0.dev1/aim/web/api/views.py` & `aim-4.0.0.dev2/aim/web/api/views.py`

 * *Files identical despite different names*

### Comparing `aim-4.0.0.dev1/aim/web/middlewares/profiler/profiler.py` & `aim-4.0.0.dev2/aim/web/middlewares/profiler/profiler.py`

 * *Files identical despite different names*

### Comparing `aim-4.0.0.dev1/aim/web/migrations/alembic.ini` & `aim-4.0.0.dev2/aim/web/migrations/alembic.ini`

 * *Files identical despite different names*

### Comparing `aim-4.0.0.dev1/aim/web/migrations/alembic_dev.ini` & `aim-4.0.0.dev2/aim/web/migrations/alembic_dev.ini`

 * *Files identical despite different names*

### Comparing `aim-4.0.0.dev1/aim/web/migrations/env.py` & `aim-4.0.0.dev2/aim/web/migrations/env.py`

 * *Files identical despite different names*

### Comparing `aim-4.0.0.dev1/aim/web/migrations/versions/11672b13f92c_.py` & `aim-4.0.0.dev2/aim/web/migrations/versions/11672b13f92c_.py`

 * *Files identical despite different names*

### Comparing `aim-4.0.0.dev1/aim/web/migrations/versions/517a45b2e62c_.py` & `aim-4.0.0.dev2/aim/web/migrations/versions/517a45b2e62c_.py`

 * *Files identical despite different names*

### Comparing `aim-4.0.0.dev1/aim/web/migrations/versions/5ae8371b7481_.py` & `aim-4.0.0.dev2/aim/web/migrations/versions/5ae8371b7481_.py`

 * *Files identical despite different names*

### Comparing `aim-4.0.0.dev1/aim/web/migrations/versions/73a3d004c227_.py` & `aim-4.0.0.dev2/aim/web/migrations/versions/73a3d004c227_.py`

 * *Files identical despite different names*

### Comparing `aim-4.0.0.dev1/aim/web/utils.py` & `aim-4.0.0.dev2/aim/web/utils.py`

 * *Files identical despite different names*

### Comparing `aim-4.0.0.dev1/aim.egg-info/PKG-INFO` & `aim-4.0.0.dev2/aim.egg-info/PKG-INFO`

 * *Files 24% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: aim
-Version: 4.0.0.dev1
+Version: 4.0.0.dev2
 Summary: A super-easy way to record, search and compare AI experiments.
 Classifier: License :: OSI Approved :: Apache Software License
 Classifier: Programming Language :: Python
 Classifier: Programming Language :: Python :: 3
 Classifier: Programming Language :: Python :: 3.7
 Classifier: Programming Language :: Python :: 3.8
 Classifier: Programming Language :: Python :: 3.9
@@ -12,135 +12,221 @@
 Classifier: Programming Language :: Python :: 3.11
 Classifier: Programming Language :: Python :: Implementation :: PyPy
 Requires-Python: >=3.7.0
 Description-Content-Type: text/markdown
 License-File: LICENSE
 
 <div align="center">
-  <img src="https://user-images.githubusercontent.com/13848158/154338760-edfe1885-06f3-4e02-87fe-4b13a403516b.png">
-  <h3>An easy-to-use & supercharged open-source experiment tracker</h3>
-  Aim logs your training runs, enables a beautiful UI to compare them and an API to query them programmatically.
+  <table>
+    <tbody>
+      <tr>
+        <td>Drop a star to support Aim ⭐</td>
+        <td>
+          <a href="https://community.aimstack.io/">Join Aim discord community</a>
+          <img width="20px" src="https://user-images.githubusercontent.com/13848158/226759622-063b725d-8b3e-4c75-80c7-11fb04b7adf5.png">
+        </td>
+      </tr>
+    </tbody>
+  </table>
 </div>
 
-<br/>
-
-<img src="https://user-images.githubusercontent.com/13848158/154338753-34484cda-95b8-4da8-a610-7fdf198c05fd.png">
+<div align="center">
+  <img src="https://user-images.githubusercontent.com/13848158/225620298-9f9293e9-a138-41fd-bd77-21d53d0490b7.png">
+  <h3>
+    An easy-to-use & supercharged open-source experiment tracker
+  </h3>
+  Aim logs your training runs and any AI Metadata, enables a beautiful UI to compare, observe them and an API to query them programmatically.
+</div>
 
-<p align="center">
-  <a href="#about-aim"><b>About</b></a> &bull;
-  <a href="#why-use-aim"><b>Features</b></a> &bull;
-  <a href="#demos"><b>Demos</b></a> &bull;
-  <a href="https://github.com/aimhubio/aim/tree/main/examples"><b>Examples</b></a> &bull;
-  <a href="#quick-start"><b>Quick Start</b></a> &bull;
-  <a href="https://aimstack.readthedocs.io/en/latest/"><b>Documentation</b></a> &bull;
-  <a href="#roadmap"><b>Roadmap</b></a> &bull;
-  <a href="https://community.aimstack.io/"><b>Discord Community</b></a> &bull;
-  <a href="https://twitter.com/aimstackio"><b>Twitter</b></a>
-</p>
+<br/>
 
 <div align="center">
   
+  [![Discord Server](https://dcbadge.vercel.app/api/server/zXq2NfVdtF?compact=true&style=flat)](https://community.aimstack.io/)
+  [![Twitter Follow](https://img.shields.io/twitter/follow/aimstackio?style=social)](https://twitter.com/aimstackio)
+  [![Medium](https://img.shields.io/badge/Medium-12100E?style=flat&logo=medium&logoColor=white)](https://medium.com/aimstack)
+  
   [![Platform Support](https://img.shields.io/badge/platform-Linux%20%7C%20macOS-blue)]()
-  [![PyPI - Python Version](https://img.shields.io/pypi/pyversions/aim)](https://pypi.org/project/aim/)
+  [![PyPI - Python Version](https://img.shields.io/badge/python-%3E%3D%203.7-blue)](https://pypi.org/project/aim/)
   [![PyPI Package](https://img.shields.io/pypi/v/aim?color=yellow)](https://pypi.org/project/aim/)
   [![License](https://img.shields.io/badge/License-Apache%202.0-orange.svg)](https://opensource.org/licenses/Apache-2.0)
   [![PyPI Downloads](https://img.shields.io/pypi/dw/aim?color=green)](https://pypi.org/project/aim/)
   [![Issues](https://img.shields.io/github/issues/aimhubio/aim)](http://github.com/aimhubio/aim/issues)
   
 </div>
 
 <div align="center">
-  <sub>Integrates seamlessly with your favorite tools</sub>
   <br/>
+  <kbd>
+    <img src="https://user-images.githubusercontent.com/13848158/136374529-af267918-5dc6-4a4e-8ed2-f6333a332f96.gif" />
+  </kbd>
+</div>
+
+</br>
+
+<div align="center">
+  <sub><strong>SEAMLESSLY INTEGRATES WITH:</strong></sub>
   <br/>
-  <img src="https://user-images.githubusercontent.com/13848158/155354389-d0301620-77ea-4629-a743-f7aa249e14b5.png" width="60" />
-  <img src="https://user-images.githubusercontent.com/13848158/155354496-b39d7b1c-63ef-40f0-9e59-c08d2c5e337c.png" width="60" />
-  <img src="https://user-images.githubusercontent.com/13848158/155354380-3755c741-6960-42ca-b93e-84a8791f088c.png" width="60" />
-  <img src="https://user-images.githubusercontent.com/13848158/155354342-7df0ef5e-63d2-4df7-b9f1-d2fc0e95f53f.png" width="60" />
-  <img src="https://user-images.githubusercontent.com/13848158/155354392-afbff3de-c845-4d86-855d-53df569f91d1.png" width="60" />
-  <img src="https://user-images.githubusercontent.com/13848158/155354355-89210506-e7e5-4d37-b2d6-ad3fda62ef13.png" width="60" />
-  <img src="https://user-images.githubusercontent.com/13848158/155354397-8af8e1d3-4067-405e-9d42-1f131663ed22.png" width="60" />
   <br/>
-  <img src="https://user-images.githubusercontent.com/13848158/155354513-f7486146-3891-4f3f-934f-e58bbf9ce695.png" width="60" />
-  <img src="https://user-images.githubusercontent.com/13848158/155354500-c0471ce6-b2ce-4172-b9e4-07a197256303.png" width="60" />
-  <img src="https://user-images.githubusercontent.com/13848158/155354361-9f911785-008d-4b75-877e-651e026cf47e.png" width="60" />
-  <img src="https://user-images.githubusercontent.com/13848158/155354373-1879ae61-b5d1-41f0-a4f1-04b639b6f05e.png" width="60" />
-  <img src="https://user-images.githubusercontent.com/13848158/155354483-75d9853f-7154-4d95-8190-9ad7a73d6654.png" width="60" />
-  <img src="https://user-images.githubusercontent.com/13848158/155354329-cf7c3352-a72a-478d-82a7-04e3833b03b7.png" width="60" />
-  <img src="https://user-images.githubusercontent.com/13848158/155354349-dcdf3bc3-d7a9-4f34-8258-4824a57f59c7.png" width="60" />
-  <img src="https://user-images.githubusercontent.com/13848158/155354471-518f1814-7a41-4b23-9caf-e516507343f1.png" width="60" />
-  <img src="https://user-images.githubusercontent.com/48801049/165162736-2cc5da39-38aa-4093-874f-e56d0ba9cea2.png" width="60" />
-  <img src="https://user-images.githubusercontent.com/48801049/165074282-36ad18eb-1124-434d-8439-728c22cd7ac7.png" width="60" />
+  <img src="https://user-images.githubusercontent.com/97726819/225954732-2b263308-8ed8-4df3-810b-704840328e98.png" height="60" />
+  <img src="https://user-images.githubusercontent.com/97726819/225954727-04eccf0e-51ed-4f2d-8f3b-c9a675ca8e8f.png" height="60" />
+  <img src="https://user-images.githubusercontent.com/97726819/225954728-ca2f498d-51a7-487b-bd69-ffb5f0c2af58.png" height="60" />
+  <img src="https://user-images.githubusercontent.com/97726819/225954689-1076998c-42f4-4e31-ab47-d9f39575fda1.png" height="60" />
+  <img src="https://user-images.githubusercontent.com/97726819/225954739-0231d659-3202-4458-9c35-ba92d1f079b8.png" height="60" />
+  <img src="https://user-images.githubusercontent.com/97726819/225954697-ef2c7091-b089-4b68-8543-80ce7275b683.png" height="60" />
+  <img src="https://user-images.githubusercontent.com/97726819/225954743-dbfe1e98-7b9f-446a-9fe4-ad4fd562f3df.png" height="60" />
+  <img src="https://user-images.githubusercontent.com/97726819/225954736-7c52ab5a-6780-4375-a6f8-b394dae3ad31.png" height="60" />
+  <img src="https://user-images.githubusercontent.com/97726819/225954710-36551a71-b26d-4665-af20-44ee452dd5dd.png" height="60" />
+  <img src="https://user-images.githubusercontent.com/97726819/225954707-4bc078b5-ae6f-4847-bc2c-3f81959accb2.png" height="60" />
+  <img src="https://user-images.githubusercontent.com/97726819/225954725-a4d4c32c-75db-470a-b1da-698982faa23c.png" height="60" />
+  <img src="https://user-images.githubusercontent.com/97726819/225954665-8d844747-a857-41b8-9104-7c27a8bdb81a.png" height="60" />
+  <img src="https://user-images.githubusercontent.com/97726819/225954686-b9c8ec57-d4fc-44e1-a4b8-443db381a00f.png" height="60" />
+  <img src="https://user-images.githubusercontent.com/97726819/225954693-94bc20b4-f51a-4130-8d5f-ddee30d81205.png" height="60" />
+  <img src="https://user-images.githubusercontent.com/97726819/225954674-42fbfdb3-0351-492d-9ea3-1d3ab2b545f5.png" height="60" />
+  <img src="https://user-images.githubusercontent.com/97726819/225954678-25f1b626-2cb1-4e7e-ad83-f7c8ab679c6f.png" height="60" />
+  <img src="https://user-images.githubusercontent.com/97726819/225954702-d18d2706-dc87-4e09-a678-f010f6d95736.png" height="60" />
 </div>
 
+<br/>
+
 <div align="center">
+  <sub><strong>TRUSTED BY ML TEAMS FROM:</strong></sub>  
   <br/>
-  <kbd>
-    <img src="https://user-images.githubusercontent.com/13848158/136374529-af267918-5dc6-4a4e-8ed2-f6333a332f96.gif" />
-  </kbd>
+  <br/>
+  <img src="https://user-images.githubusercontent.com/97726819/225952594-a21546f4-987f-42bd-9154-c22b50632b55.png" height="55" />
+  <img src="https://user-images.githubusercontent.com/97726819/225953224-291fbb6d-e31a-4e36-90ba-92a1dc20bacc.png" height="55" />
+  <img src="https://user-images.githubusercontent.com/97726819/225953339-4fcc3c99-dda2-4529-ac2a-29c8293be323.png" height="55" />
+  <img src="https://user-images.githubusercontent.com/97726819/225953084-1d88325a-ad5f-49eb-aa67-f064c4b9f39c.png" height="55" />
+  <img src="https://user-images.githubusercontent.com/97726819/225952955-397e0f26-f01e-4b25-bd70-9f292a6f77c2.png" height="55" />
+  <img src="https://user-images.githubusercontent.com/97726819/225952682-a843827b-e870-429d-96d8-3b4fd45471cd.png" height="55" />
+  <img src="https://user-images.githubusercontent.com/97726819/225952831-1c0e36aa-4120-4635-ab4e-bf1bc685477b.png" height="55" />
+  <img src="https://user-images.githubusercontent.com/97726819/225953432-4b27653a-aa12-4fbf-897c-01349afa2ad0.png" height="55" />
 </div>
 
-# About Aim
+<br/>
 
-| Track and version ML runs | Visualize runs via beautiful UI | Query runs metadata via SDK |
-|:--------------------:|:------------------------:|:-------------------:|
-| <img width="600px" src="https://user-images.githubusercontent.com/13848158/154337794-e9310239-6614-41b3-a95b-bb91f0bb6c4f.png"> | <img width="600px" src="https://user-images.githubusercontent.com/13848158/154337788-03fe5b31-0fa3-44af-ae79-2861707d8602.png"> | <img width="600px" src="https://user-images.githubusercontent.com/13848158/154337793-85175c78-5659-4dd0-bb2d-05017278e2fa.png"> |
+<p align="center">
+  AimStack offers enterprise support that's beyond core Aim. Contact via <a href="mailto:hello@aimstack.io">hello@aimstack.io</a> e-mail.
+</p>
 
-Aim is an open-source, self-hosted ML experiment tracking tool. 
-It's good at tracking lots (1000s) of training runs and it allows you to compare them with a performant and beautiful UI.
+---
 
-You can use not only the great Aim UI but also its SDK to query your runs' metadata programmatically. 
-That's especially useful for automations and additional analysis on a Jupyter Notebook.
+<h3 align="center">
+  <a href="#-about"><b>About</b></a> &bull;
+  <a href="#-demos"><b>Demos</b></a> &bull;
+  <a href="#-ecosystem"><b>Ecosystem</b></a> &bull;
+  <a href="#-quick-start"><b>Quick Start</b></a> &bull;
+  <a href="https://github.com/aimhubio/aim/tree/main/examples"><b>Examples</b></a> &bull;
+  <a href="https://aimstack.readthedocs.io/en/latest/"><b>Documentation</b></a> &bull;
+  <a href="#-community"><b>Community</b></a> &bull;
+  <a href="https://aimstack.io/blog"><b>Blog</b></a>
+</h3>  
 
+---
 
-Aim's mission is to democratize AI dev tools.
+# ℹ️ About
 
-# Why use Aim?
+Aim is an open-source, self-hosted ML experiment tracking tool designed to handle 10,000s of training runs.
 
-### Compare 100s of runs in a few clicks - build models faster
+Aim provides a performant and beautiful UI for exploring and comparing training runs.
+Additionally, its SDK enables programmatic access to tracked metadata — perfect for automations and Jupyter Notebook analysis.
 
-- Compare, group and aggregate 100s of metrics thanks to effective visualizations.
-- Analyze, learn correlations and patterns between hparams and metrics.
-- Easy pythonic search to query the runs you want to explore.
+<p align="center">
+  <strong>Aim's mission is to democratize AI dev tools 🎯 </strong>
+</p>
 
-### Deep dive into details of each run for easy debugging
+<div align="center">
+  <img src="https://user-images.githubusercontent.com/13848158/226426018-f7c11c9b-78d9-4ee4-b292-df28b3e8eaa6.jpg" height="140" />
+  <img src="https://user-images.githubusercontent.com/13848158/226426005-f7e83923-0f92-44a4-88e4-1735a3d3e119.jpg" height="140" />
+  <img src="https://user-images.githubusercontent.com/13848158/226426015-4f1122d8-c96a-443f-8698-3db942b1972a.jpg" height="140" />
+</div>
 
-- Hyperparameters, metrics, images, distributions, audio, text - all available at hand on an intuitive UI to understand the performance of your model.
-- Easily track plots built via your favourite visualisation tools, like plotly and matplotlib.
-- Analyze system resource usage to effectively utilize computational resources.
+</br>
 
-### Have all relevant information organised and accessible for easy governance
+<div align="center">
+  <table>
+    <tbody>
+      <tr>
+        <th>Log Metadata Across Your ML Pipeline 💾</th>
+        <th>Visualize & Compare Metadata via UI 📊</th>
+      </tr>
+      <tr>
+        <td>
+          <ul>
+            <li>ML experiments and any metadata tracking</li>
+            <li>Integration with popular ML frameworks</li>
+            <li>Easy migration from other experiment trackers</li>
+            </ul>
+          </td>
+        <td>
+          <ul>
+            <li>Metadata visualization via Aim Explorers</li>
+            <li>Grouping and aggregation</li>
+            <li>Querying using Python expressions</li>
+          </ul>
+        </td>
+      </tr>
+      <tr>
+        <th>Run ML Trainings Effectively ⚡</th>
+        <th>Organize Your Experiments 🗂️</th>
+      </tr>
+      <tr>
+        <td>
+          <ul>
+            <li>System info and resource usage tracking</li>
+            <li>Real-time alerting on training progress</li>
+            <li>Logging and configurable notifications</li>
+          </ul>
+        </td>
+        <td>
+          <ul>
+            <li>Detailed run information for easy debugging</li>
+            <li>Centralized dashboard for holistic view</li>
+            <li>Runs grouping with tags and experiments</li></ul>
+        </td>
+      </tr>
+    </tbody>
+  </table>
+</div>
 
-- Centralized dashboard to holistically view all your runs, their hparams and results.
-- Use SDK to query/access all your runs and tracked metadata.
-- You own your data - Aim is open source and self hosted.
+# 🎬 Demos
 
-# Demos
+Check out live Aim demos NOW to see it in action.
 
-| Machine translation | lightweight-GAN |
+| [Machine translation experiments](http://play.aimstack.io:10001/metrics?grouping=HQGdK9Xxy35e6sY1CYkCmk1WbWMN2AsCNfJJ3d1RJYLtrVPMoF5UpGiA6CF8bEJnfzRsKpqespf3AEuKSVrhUYvYk9MxzNGA9XZWYUf6phEg8AMbZGLRVDXnAPDuo8tueqsST1ZLizWzQwDYJWHUza6pyB2Eojt9uWqNHUdb858TqDRnCJzqiVJXKXEzFWUyvU8MckJo1qpqWWCTb4GpYN6DUJZx2GXDGR21e2xxd4m7PmNUnbA9B3apLttZoipJF6c3v7tNUKmb6irpqnNB3yc57tqYDa1XZuKfDxkMtyFdQ1x95K4jjsTVwhftEWLze35QNcxNXRCGGS9o9yEfTLG26GUX2zjPZFCjjMGU6vV7z1xRccK8MyoGrLSgAQCbvk68dTGBHpXUBvCRq8N&chart=FviZzVrt4fVQPjpCLr9sVGGrcR5etSroyqambiKpm3nTgpyv4eQxKuwNX9uN8UtKmzYUhUyTMBEANHmtbwjLApkvnYeNbxGNC6PVcoqi65m1XJnSrvgt8WiD89BapFAWRUwAGx6SWD7KZPsk3RQyysU7W7FjD3Q99NusxFGhsEfD6HXc7i8xH9KHDRGjLwh6x9VTtSp4FS8HEvpLSiiJoX7LCTi8pB7dXvrQ8G5w3jPsFz4qXYFdsVaCNL1BpFFZuiqQNkfbnM84gEq7UmiV1VzM4oS3AgQHxADG3kpBVp6eKTey9F1Swd4FcUkFA9QEPjgQgqwRGjkquZ2bdDDVLBnCh7JPvboP2kifCiZZ5MDdV9MMx6PKHp4DusWyWLXiHQYPkpGPWBiuccMUXDsuJaCWJbuABdY7CyiJMv1jdHYkjabygSxehPVyEDefWAtjBfv2vaeM1xv63jadbmpKYFxft7qmuT9HvVxiGvRgs4RQFxy8K4rtFBca3HNs1mDaaY81gy9MGXyw7BS5Fniu92jaJpsWDdg6Y3AQBLZtrpJy2obEZ4yzJaCVT7JUNPAyyCUNLck393VFLoEkaD9CU5npK5R7tj1c1G3gkMNQXnSXy5NpSj8deMmXV5qz3JKu1nq2caGQKcqjzy2gLkExdm674AMFjSg9yFjK6VqASXQ17NKtWRUvaYoxGbHDAFQaMKWKh8QLm22QA9mKT8NksLptWozbgDvafnQLNMvezLU5bvKV5o75PAWYiRB56RcYfEhzaB6YWdgL7TJicyY5rFi6Az8UZ7wqB3N5iMuZdpxhKn5KbZDxyuUMuvVt24i5LVPPmmwQtqxMoJ4aLo48a2YvDW6TAkdQjNjvn6KcEEz6GTixujb1YHhMUD8v4AepWKEwKz1ddEca1P2wLQjbpihCuaqbxeohnuZZLogJdUBojBEDgrnrrVpPBaLLEkGSpkJbtrsKUuEeBo1AF3yNgHftLbynGpobVF5DhmsmddmiA6c8vSTokJxHhjpnW8mAcNHBRtmVJCT7VkdHSAhNypM4Hivwfx5jCccG9LauKmCeRMDzHiA57TX9W6ttcPHSvUyQorARQAd2oeNY4H83hZjHh9Bt8iwKZRt4xK6hrTR8tif7hq8eURXrGH9Ys7TzykXK8FHHWvLNzNnYf3E4a9NkD43MjfKvMM1hj4Q2K8MHbmRCqrmFrHP5kim9shq6mhLPTgwha32nvnrBkfPQVPwpGTzKuwE&select=CdsQ7jVNkogQhRzQR3e28Ek39AZ4Ma2y37k5zJaf9EZmQhMjy8GtGm4LGU6dRFuAVG7mYww5xDrQAE74KHQ3Kk1e6661RmcmNALAUjtHyCmrTVBMCnBGNiuq1y7EzmxoodYHU1BV1rnoefQAw2kTBtbWi11hV1P4LcwFCcXfUWF6rpRC7ehEnUCTqUV4bkGVJPLcmk9mdmiGwa2YgmnSShNGPVGZiEi1rMVECyngSRVdqdZwAeXBGWFLfqF1KbZeCo4MTF4SSmFupJ9zLhYbuojEbopyFWHQ6xs3sq9epPeaQziLM4Js7oFYRmuFWUYdFqnZngmewXWmi7tQAgVqhiT6dMjG2eTdfgX6WuRSuoHALkh2XJhHA6GfZLUcxC5Ni9YyKuBTamtaYarbNNJJ8z15WWvuUkLpjgHdEpE2h924xFdu8aoZNuiQxYGvcndaW1BTGMXS5fTKPqYfe2n8Ky2HWPkcX3hEXtyawu1F9BndKNaXLPgsdAoFBArBZnSe28YtSmTa5LRucKVBAxakvv5MWMXchAmpaGFQbZyYUoMgQLcJd7Y96x6zSR7nhwr5Ar81BrmqYz2WFLuk7osUbwsc9HbSG6CQt8p6Vg2u7DjKaZXW8pjkPHAKrHWtHEDiJPJ5rj6VsdFm3) | [lightweight-GAN experiments](http://play.aimstack.io:10002/images?grouping=E1zQzcmtDR3wibEa1MVysTvCyZEv1T8ixkCxTWExCyMnHtX2HyiF9eszvPgfd2xdJ5TUTKGpSs1bsLVq5tHAV3uWtsZmmckn6HjNtVCMyQDJpwhiEy5tAyw&select=2NEXuD7fFoaLcwRjymjA1wLmUrGs9s3AiXcCW82C367SwJt18CAB6xzkMGowrUDuDwggE1huaPVcQJpQUsmAQx1CnGiqCUBp2jPMd5mMNPX2QKQMcmvu9ZykBNkeBvCQFPd9ERuQD2g1EjWuvyJ3H53mAZTfp94LCXvR9CUsG5ei2CjQUzfZLM6DCyUr1GPaEVnY5f1EwzicNxXuoutkBgqCqaobJ7Do4q4eHAA6ooiWU6ekS3D2sLj6qYwhVTjfGCPfbWwBiH83nFkY3fLExzdeTY2zeUHeeYikQR9S7xHbVD8WvjekdQVp8X4dNLJZxiVmEqHpPRnU3ZrYsMhE7yFAAgjJwPNUzLTt6YFrtZBcmc4rwAC2oyrqysUSEr6gzL6LcJ6yuqDGf9D5tzftHbTLDkhc8B2sCgTS&images=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)|
 |:---:|:---:|
-| <a href="http://play.aimstack.io:10001/metrics?grouping=HQGdK9Xxy35e6sY1CYkCmk1WbWMN2AsCNfJJ3d1RJYLtrVPMoF5UpGiA6CF8bEJnfzRsKpqespf3AEuKSVrhUYvYk9MxzNGA9XZWYUf6phEg8AMbZGLRVDXnAPDuo8tueqsST1ZLizWzQwDYJWHUza6pyB2Eojt9uWqNHUdb858TqDRnCJzqiVJXKXEzFWUyvU8MckJo1qpqWWCTb4GpYN6DUJZx2GXDGR21e2xxd4m7PmNUnbA9B3apLttZoipJF6c3v7tNUKmb6irpqnNB3yc57tqYDa1XZuKfDxkMtyFdQ1x95K4jjsTVwhftEWLze35QNcxNXRCGGS9o9yEfTLG26GUX2zjPZFCjjMGU6vV7z1xRccK8MyoGrLSgAQCbvk68dTGBHpXUBvCRq8N&chart=FviZzVrt4fVQPjpCLr9sVGGrcR5etSroyqambiKpm3nTgpyv4eQxKuwNX9uN8UtKmzYUhUyTMBEANHmtbwjLApkvnYeNbxGNC6PVcoqi65m1XJnSrvgt8WiD89BapFAWRUwAGx6SWD7KZPsk3RQyysU7W7FjD3Q99NusxFGhsEfD6HXc7i8xH9KHDRGjLwh6x9VTtSp4FS8HEvpLSiiJoX7LCTi8pB7dXvrQ8G5w3jPsFz4qXYFdsVaCNL1BpFFZuiqQNkfbnM84gEq7UmiV1VzM4oS3AgQHxADG3kpBVp6eKTey9F1Swd4FcUkFA9QEPjgQgqwRGjkquZ2bdDDVLBnCh7JPvboP2kifCiZZ5MDdV9MMx6PKHp4DusWyWLXiHQYPkpGPWBiuccMUXDsuJaCWJbuABdY7CyiJMv1jdHYkjabygSxehPVyEDefWAtjBfv2vaeM1xv63jadbmpKYFxft7qmuT9HvVxiGvRgs4RQFxy8K4rtFBca3HNs1mDaaY81gy9MGXyw7BS5Fniu92jaJpsWDdg6Y3AQBLZtrpJy2obEZ4yzJaCVT7JUNPAyyCUNLck393VFLoEkaD9CU5npK5R7tj1c1G3gkMNQXnSXy5NpSj8deMmXV5qz3JKu1nq2caGQKcqjzy2gLkExdm674AMFjSg9yFjK6VqASXQ17NKtWRUvaYoxGbHDAFQaMKWKh8QLm22QA9mKT8NksLptWozbgDvafnQLNMvezLU5bvKV5o75PAWYiRB56RcYfEhzaB6YWdgL7TJicyY5rFi6Az8UZ7wqB3N5iMuZdpxhKn5KbZDxyuUMuvVt24i5LVPPmmwQtqxMoJ4aLo48a2YvDW6TAkdQjNjvn6KcEEz6GTixujb1YHhMUD8v4AepWKEwKz1ddEca1P2wLQjbpihCuaqbxeohnuZZLogJdUBojBEDgrnrrVpPBaLLEkGSpkJbtrsKUuEeBo1AF3yNgHftLbynGpobVF5DhmsmddmiA6c8vSTokJxHhjpnW8mAcNHBRtmVJCT7VkdHSAhNypM4Hivwfx5jCccG9LauKmCeRMDzHiA57TX9W6ttcPHSvUyQorARQAd2oeNY4H83hZjHh9Bt8iwKZRt4xK6hrTR8tif7hq8eURXrGH9Ys7TzykXK8FHHWvLNzNnYf3E4a9NkD43MjfKvMM1hj4Q2K8MHbmRCqrmFrHP5kim9shq6mhLPTgwha32nvnrBkfPQVPwpGTzKuwE&select=CdsQ7jVNkogQhRzQR3e28Ek39AZ4Ma2y37k5zJaf9EZmQhMjy8GtGm4LGU6dRFuAVG7mYww5xDrQAE74KHQ3Kk1e6661RmcmNALAUjtHyCmrTVBMCnBGNiuq1y7EzmxoodYHU1BV1rnoefQAw2kTBtbWi11hV1P4LcwFCcXfUWF6rpRC7ehEnUCTqUV4bkGVJPLcmk9mdmiGwa2YgmnSShNGPVGZiEi1rMVECyngSRVdqdZwAeXBGWFLfqF1KbZeCo4MTF4SSmFupJ9zLhYbuojEbopyFWHQ6xs3sq9epPeaQziLM4Js7oFYRmuFWUYdFqnZngmewXWmi7tQAgVqhiT6dMjG2eTdfgX6WuRSuoHALkh2XJhHA6GfZLUcxC5Ni9YyKuBTamtaYarbNNJJ8z15WWvuUkLpjgHdEpE2h924xFdu8aoZNuiQxYGvcndaW1BTGMXS5fTKPqYfe2n8Ky2HWPkcX3hEXtyawu1F9BndKNaXLPgsdAoFBArBZnSe28YtSmTa5LRucKVBAxakvv5MWMXchAmpaGFQbZyYUoMgQLcJd7Y96x6zSR7nhwr5Ar81BrmqYz2WFLuk7osUbwsc9HbSG6CQt8p6Vg2u7DjKaZXW8pjkPHAKrHWtHEDiJPJ5rj6VsdFm3"> <img width="800px" src="https://user-images.githubusercontent.com/13848158/154340796-c9e91b13-8ee0-4a67-bcde-8cf3aaa7ba99.jpg"> </a> | <a href="http://play.aimstack.io:10002/images?grouping=E1zQzcmtDR3wibEa1MVysTvCyZEv1T8ixkCxTWExCyMnHtX2HyiF9eszvPgfd2xdJ5TUTKGpSs1bsLVq5tHAV3uWtsZmmckn6HjNtVCMyQDJpwhiEy5tAyw&select=2NEXuD7fFoaLcwRjymjA1wLmUrGs9s3AiXcCW82C367SwJt18CAB6xzkMGowrUDuDwggE1huaPVcQJpQUsmAQx1CnGiqCUBp2jPMd5mMNPX2QKQMcmvu9ZykBNkeBvCQFPd9ERuQD2g1EjWuvyJ3H53mAZTfp94LCXvR9CUsG5ei2CjQUzfZLM6DCyUr1GPaEVnY5f1EwzicNxXuoutkBgqCqaobJ7Do4q4eHAA6ooiWU6ekS3D2sLj6qYwhVTjfGCPfbWwBiH83nFkY3fLExzdeTY2zeUHeeYikQR9S7xHbVD8WvjekdQVp8X4dNLJZxiVmEqHpPRnU3ZrYsMhE7yFAAgjJwPNUzLTt6YFrtZBcmc4rwAC2oyrqysUSEr6gzL6LcJ6yuqDGf9D5tzftHbTLDkhc8B2sCgTS&images=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"> <img width="800px" src="https://user-images.githubusercontent.com/13848158/154340790-bc7b7a21-e8a1-43a1-809d-4060b5bfb60f.jpg"> </a> |
+| <a href="http://play.aimstack.io:10001/metrics?grouping=HQGdK9Xxy35e6sY1CYkCmk1WbWMN2AsCNfJJ3d1RJYLtrVPMoF5UpGiA6CF8bEJnfzRsKpqespf3AEuKSVrhUYvYk9MxzNGA9XZWYUf6phEg8AMbZGLRVDXnAPDuo8tueqsST1ZLizWzQwDYJWHUza6pyB2Eojt9uWqNHUdb858TqDRnCJzqiVJXKXEzFWUyvU8MckJo1qpqWWCTb4GpYN6DUJZx2GXDGR21e2xxd4m7PmNUnbA9B3apLttZoipJF6c3v7tNUKmb6irpqnNB3yc57tqYDa1XZuKfDxkMtyFdQ1x95K4jjsTVwhftEWLze35QNcxNXRCGGS9o9yEfTLG26GUX2zjPZFCjjMGU6vV7z1xRccK8MyoGrLSgAQCbvk68dTGBHpXUBvCRq8N&chart=FviZzVrt4fVQPjpCLr9sVGGrcR5etSroyqambiKpm3nTgpyv4eQxKuwNX9uN8UtKmzYUhUyTMBEANHmtbwjLApkvnYeNbxGNC6PVcoqi65m1XJnSrvgt8WiD89BapFAWRUwAGx6SWD7KZPsk3RQyysU7W7FjD3Q99NusxFGhsEfD6HXc7i8xH9KHDRGjLwh6x9VTtSp4FS8HEvpLSiiJoX7LCTi8pB7dXvrQ8G5w3jPsFz4qXYFdsVaCNL1BpFFZuiqQNkfbnM84gEq7UmiV1VzM4oS3AgQHxADG3kpBVp6eKTey9F1Swd4FcUkFA9QEPjgQgqwRGjkquZ2bdDDVLBnCh7JPvboP2kifCiZZ5MDdV9MMx6PKHp4DusWyWLXiHQYPkpGPWBiuccMUXDsuJaCWJbuABdY7CyiJMv1jdHYkjabygSxehPVyEDefWAtjBfv2vaeM1xv63jadbmpKYFxft7qmuT9HvVxiGvRgs4RQFxy8K4rtFBca3HNs1mDaaY81gy9MGXyw7BS5Fniu92jaJpsWDdg6Y3AQBLZtrpJy2obEZ4yzJaCVT7JUNPAyyCUNLck393VFLoEkaD9CU5npK5R7tj1c1G3gkMNQXnSXy5NpSj8deMmXV5qz3JKu1nq2caGQKcqjzy2gLkExdm674AMFjSg9yFjK6VqASXQ17NKtWRUvaYoxGbHDAFQaMKWKh8QLm22QA9mKT8NksLptWozbgDvafnQLNMvezLU5bvKV5o75PAWYiRB56RcYfEhzaB6YWdgL7TJicyY5rFi6Az8UZ7wqB3N5iMuZdpxhKn5KbZDxyuUMuvVt24i5LVPPmmwQtqxMoJ4aLo48a2YvDW6TAkdQjNjvn6KcEEz6GTixujb1YHhMUD8v4AepWKEwKz1ddEca1P2wLQjbpihCuaqbxeohnuZZLogJdUBojBEDgrnrrVpPBaLLEkGSpkJbtrsKUuEeBo1AF3yNgHftLbynGpobVF5DhmsmddmiA6c8vSTokJxHhjpnW8mAcNHBRtmVJCT7VkdHSAhNypM4Hivwfx5jCccG9LauKmCeRMDzHiA57TX9W6ttcPHSvUyQorARQAd2oeNY4H83hZjHh9Bt8iwKZRt4xK6hrTR8tif7hq8eURXrGH9Ys7TzykXK8FHHWvLNzNnYf3E4a9NkD43MjfKvMM1hj4Q2K8MHbmRCqrmFrHP5kim9shq6mhLPTgwha32nvnrBkfPQVPwpGTzKuwE&select=CdsQ7jVNkogQhRzQR3e28Ek39AZ4Ma2y37k5zJaf9EZmQhMjy8GtGm4LGU6dRFuAVG7mYww5xDrQAE74KHQ3Kk1e6661RmcmNALAUjtHyCmrTVBMCnBGNiuq1y7EzmxoodYHU1BV1rnoefQAw2kTBtbWi11hV1P4LcwFCcXfUWF6rpRC7ehEnUCTqUV4bkGVJPLcmk9mdmiGwa2YgmnSShNGPVGZiEi1rMVECyngSRVdqdZwAeXBGWFLfqF1KbZeCo4MTF4SSmFupJ9zLhYbuojEbopyFWHQ6xs3sq9epPeaQziLM4Js7oFYRmuFWUYdFqnZngmewXWmi7tQAgVqhiT6dMjG2eTdfgX6WuRSuoHALkh2XJhHA6GfZLUcxC5Ni9YyKuBTamtaYarbNNJJ8z15WWvuUkLpjgHdEpE2h924xFdu8aoZNuiQxYGvcndaW1BTGMXS5fTKPqYfe2n8Ky2HWPkcX3hEXtyawu1F9BndKNaXLPgsdAoFBArBZnSe28YtSmTa5LRucKVBAxakvv5MWMXchAmpaGFQbZyYUoMgQLcJd7Y96x6zSR7nhwr5Ar81BrmqYz2WFLuk7osUbwsc9HbSG6CQt8p6Vg2u7DjKaZXW8pjkPHAKrHWtHEDiJPJ5rj6VsdFm3"> <img src="https://user-images.githubusercontent.com/97726819/225964524-0051c2c7-8554-43ae-82b8-adcb77bcf1ba.png"> </a> | <a href="http://play.aimstack.io:10002/images?grouping=E1zQzcmtDR3wibEa1MVysTvCyZEv1T8ixkCxTWExCyMnHtX2HyiF9eszvPgfd2xdJ5TUTKGpSs1bsLVq5tHAV3uWtsZmmckn6HjNtVCMyQDJpwhiEy5tAyw&select=2NEXuD7fFoaLcwRjymjA1wLmUrGs9s3AiXcCW82C367SwJt18CAB6xzkMGowrUDuDwggE1huaPVcQJpQUsmAQx1CnGiqCUBp2jPMd5mMNPX2QKQMcmvu9ZykBNkeBvCQFPd9ERuQD2g1EjWuvyJ3H53mAZTfp94LCXvR9CUsG5ei2CjQUzfZLM6DCyUr1GPaEVnY5f1EwzicNxXuoutkBgqCqaobJ7Do4q4eHAA6ooiWU6ekS3D2sLj6qYwhVTjfGCPfbWwBiH83nFkY3fLExzdeTY2zeUHeeYikQR9S7xHbVD8WvjekdQVp8X4dNLJZxiVmEqHpPRnU3ZrYsMhE7yFAAgjJwPNUzLTt6YFrtZBcmc4rwAC2oyrqysUSEr6gzL6LcJ6yuqDGf9D5tzftHbTLDkhc8B2sCgTS&images=9vt2MvuQj2Q7jxGQYhNH6ZnWw4CsEzubFcFotuqCHfzvuruDs6pyWfhqhinD4hCiYsAURXgJbmq2L5z4vEQMbrE7iTy8XHNndPBPyuCEvRpxGwwFkukX3YGkVhNDQmUPtBagKbsMAgUASJM8hFtKboqbu9KWTModsjd4Qag7aL1KbJCzBYmZLCpKMSf6eKUTQtfwLLWbgquEx6oahAoSujV6aZ5cjsjN4JdGtPbicySpccgLDQHaQYTHCseA6sPVaEwCsoQDJAcTnjEVFFUUUW5HbPkrNgeRKb8M9pxudrweRQ3gNukLx5yizxQKrmcKU7saxLraqYUA2y5LmEQohsWGUq8sKkvGDH6oNLx2ytJsdVM5PGieENXMAaPg3KuWYXXTwixzwscdDsHSWeiXTGj1QxUKiBCnfwkZ7pZbYMCSgczSn9WpwygrKhb2znSYhn4gFzCsdjiXPPDv9LpPzkFVbsMCvk1CadqpwxTfxNmteKm7CQVViyCrvheGAk5rKpPzaBc5agyvfKpUqgRarxojnG8a4s1Y7qFT1rNVSC13C9h5fG54dDoFHxDyvej3bVTMDYsAiie3eVA3yEskyBGwApPNtjLY2H4b9jTmR3V7jnA9moFGfwMiXUjt8eoJsWTNkqBdRGSnqdva8zi5bApQaggnLebgCRpK1g8VvPrVS3ABQC8aMZJ2vibebHePWs1ahWZ2AXUUYwcuSRkiUWHwgtG9U1x6rR41UxFFNvW9rpDsU99DWzYpdgxfU75wTEPb2qeXYPxV1zVt5ixcFfA3Lvtsp5XXyfHY9FaNFeKKzAUQXPAkMWG4yH4Tp5me8Nt4puBC4pvJrboVcQdSsYhtxj2YwUjzN7Jyn9BV28dtRFPdtFUUc9pKpLvhZAD6XPDtKqrN3pG3LwYTKAiMDtC6tHvDqhQGuJGQZH5cVyTKkT48Xup4znass8tJxUJwacVQa6x2ewyd8AXCfc4j9bPQssabADmc1ho5Eghn5qe82cEcyG1okdfBCRMfmZ5EeCeKQYmoXddxM2cAwfJzCzG9bGtaMvXk3VV8TrSiRKjg3Exbftv8gx12QAzoBP9zosuULFpEAPZF1TvHJbEUmYgu9gwuRTAS3qYiywB7dsCq8wsTr7qmwt8WFFucpte8WvrkRGYy1GA7bD6uPhvS6sr1Wv259oB7Tkr5kirMo6Vdkz8ex9zVd4h2AP1J1dy8cqXaSk5B3HTZ6n1qdAMt4faLtt8SNqg4EqcvXx6r2J1czzXAPa9oSseYifvedcMyxnWkcTvno4QA6sp6zH25ubEwPAVzZZk35nNoJPasH3PgEgLafGPLCsPDD2sku5djPjfqkbDLUWMYm7BbTr7xK8v4UoTS485rPiF6VKoNQSuEnKQMT3uNRTS4EXNMjyRfUs4gk1217EhGVLhfqiZQyG4gqEhcJE3phLydLskk36PyGEbyFyvigjwvrK6boJnFpesze6Czc13HdWbWp6LHLseYujigdmdktU6EQb5KmghstmJ9gUF14JVPjYP57xtv19UT8XDuaJfwJn9z3U17ZDFnQ5zbXKSwD9ikMEd6VFo1xLBRHSmRdFSqcC96s23qWmMhheGtv6tTQAkq7CB1J1gy3skuFJXqhs1RvFWbFFUCLmHeTCtskEsQVP5Rkzat5Jn3QtSqCiRpEGc9Ykd5bWFAaqoudGcqEt993tVfVS3ZrVKAa6NDmbtAcdnfsUZxDt2muRPJDNVCBNW5k8XvevMpMsL3uCETtdutufp1VyLur2Yyx5WA8AeeFeDBxRxad3ZHbH27XdMpxWHF26hnbQAewspG1weRpVW9Ebc4Lc53RBeu8gVmTbKydrri1FHaYySZqCxht8bN4kdqSmkymmcTN3cfRN9DmzcmfKG6GbTDeCA9oXz5cVqrGXZcAiaj1oinnByW7W8GwhtK1Tzd7LG74Nu35DUdPCJXMH2ug4SEa3yXERXCaLvAHvFZAS89e7RUPpr3nTTrQLurjHSdkJ39pwEJpDcDjeWHsJSmTG1x195e6xvMmgPxAZd3Lzyk8Cxme8p1cY7FehSbTPc3zAAwi9LDGYyoQRcdbRHPLJ2W8rt9KeNfNq9moa1RVFPCPvhGuuyycT4f4QkP4Nvy4iUCaB5d8B1hcgmtg2X9Zpg6GUR32RYneQigK6S9ZYPNnaFeCNZZrwaYjkDpKMTMB6N24JC1TEAH8en3kXzf8CpLWeJpxoyB3hcCxjFHLYaovzgfGPeFBPY6ADDUcT3xkpUUEybdxE1cX7drHvBwyGqeU5g7i424tydxqufUgPY5sF9bM6mdoA3AvqDD9B3Zai71irxYXX8e6rRck4RwptJgBMX2gbotizoz9LrUwFQ2naBfJvbfEhZNCzME8a7H2YiVcq4Z6pkfbT1uMLfaixfw8nQCzVRbJAyVZgGzVbBj242LpD48R6VmxGcU5t2XkN8hZyYdBk1Uds9QyUG9VpC8ka7HjkvxBMknk6v4BjMnHnAj4ZxDUxMWEDbWw6iWD3iYWzVn3n5dzRcAqCQv3m2ZUnwuHHCTVJVZKZVyxrFP5eznpNv87RUXMfjbXypoLJFVtMoq81y82hYRFSkbAUwzhhoXBAGeBGDmDcwky2Hf7ZmfkzDLnRke916VxhTRLr8c6nXokCn8xwweuJHFeBqx7D88gpRbn5RrnH33545zyzyNpZpabQUGY3L7G3QznVw6wCS9x7FMixW2mgCeeWFhPDiz5Kz6DyyjaT413VSoRBCRakNcitYHUXqqCUPsFmZ3LTedA8jN99fYzse5LX36TSVbjnM7XmiZ8vNoH5mUsawmvG7NXbhgoyhx4rzL7t57A4g7sQg4YhGAFzEbXrh416riiPH8r52on2VEqkjNPDnybSg3cwuR6rPfMWA7YoyEAp14aStUPaKqbM9omConMxZde5o2DpjS86G5vDBY1o7F4LnBHLHRxKfqAkTPjvEdhaYY2uY6i598po9b2fAtpUGCbXnzcNrV5Vei5WkiQAqRT6whGr29PTLsAVGed71drx7BqzNiDcFJBL9dVrVoPqYLvrYVGi89MuuWuirD7CRhXWahysjrNpFf4aHXmuXS3UD7SFgkqAZzL1hrVq77K8UhGMMWLUzE9gjP6PH4xL6fJetKaRGZNpbsqDoKuBkBAk9j1nGpYMAyuo2H2AWUyj8PUgAbi1e4KPeqNqMVT85oZ9jkCggYczgNhT8gw5QsMarouMctMdbokxRfxz2xt9r2DuNmbEmq9e13Tqv94VrzR91R2o7pvH7YUFtJvcoJwR8K5jyof5SfKHT53zaBKxkLfCpPP3qR9ZCbAzVbreFKsQnCcZpd643VA9wtgKXxc375NwKj4QbnvafKNU9qc455d3S3o57mU4DFA7yHSqY1q41zySxfXYx4txL4TiqeyyTQu7KcHYbTUYRs69pkE1rWRW84N1qmisw2o7iLQPrhWkixrRDRk5toYWQg6ZDZExCyedYBGjsUAut"> <img src="https://user-images.githubusercontent.com/97726819/225948275-a41946ea-89f4-45f1-bce1-251c84dcddca.png"> </a> |
 | Training logs of a neural translation model(from WMT'19 competition). | Training logs of 'lightweight' GAN, proposed in ICLR 2021. |
 
-| FastSpeech 2 | Simple MNIST |
+| [FastSpeech 2 experiments](http://play.aimstack.io:10004/runs/d9e89aa7875e44b2ba85612a/audios)| [Simple MNIST](http://play.aimstack.io:10003/runs/7f083da898624a2c98e0f363/distributions) |
 |:---:|:---:|
-| <a href="http://play.aimstack.io:10004/runs/d9e89aa7875e44b2ba85612a/audios"> <img width="800px" src="https://user-images.githubusercontent.com/13848158/154340778-dbe19620-2f27-4298-b0cb-caf3904760f1.jpg"> </a> | <a href="http://play.aimstack.io:10003/runs/7f083da898624a2c98e0f363/distributions"> <img width="800px" src="https://user-images.githubusercontent.com/13848158/154340785-a7e4d9fd-d048-4207-8cd1-c4edff9cca6a.jpg"> </a> |
+| <a href="http://play.aimstack.io:10004/runs/d9e89aa7875e44b2ba85612a/audios"> <img src="https://user-images.githubusercontent.com/97726819/225948457-567526da-a329-4c53-a9a7-98dfe392d4c4.png"> </a> | <a href="http://play.aimstack.io:10003/runs/7f083da898624a2c98e0f363/distributions"> <img src="https://user-images.githubusercontent.com/97726819/225948599-ff39c5b7-ae7d-4deb-8bc9-5eee1e189d89.png"> </a> |
 | Training logs of Microsoft's "FastSpeech 2: Fast and High-Quality End-to-End Text to Speech". | Simple MNIST training logs. |
 
-# Quick Start
+# 🌍 Ecosystem
+
+Aim is not just an experiment tracker. It's a groundwork for an ecosystem. 
+Check out the two most famous Aim-based tools.
+
+| [aimlflow](https://github.com/aimhubio/aimlflow) | [Aim-spaCy](https://github.com/aimhubio/aim-spacy) |
+|:---:|:---:|
+| ![aimlflow](https://user-images.githubusercontent.com/97726819/225957836-cdec88e3-4993-435a-a135-d78be3ac1635.png) | ![Aim-spaCy](https://user-images.githubusercontent.com/97726819/225957990-4edc4525-1f65-4405-b663-ce7af888bdfa.png) |
+| Exploring MLflow experiments with a powerful UI | an Aim-based spaCy experiment tracker |
+
+# 🏁 Quick start
 
 Follow the steps below to get started with Aim.
 
-**1. Install Aim on your training environment**
+## 1. Install Aim on your training environment
 
 ```shell
 pip3 install aim
 ```
 
-**2. Integrate Aim with your code**
+## 2. Integrate Aim with your code
 
 ```python
 from aim import Run
 
 # Initialize a new run
 run = Run()
 
@@ -154,237 +240,130 @@
 for i in range(10):
     run.track(i, name='loss', step=i, context={ "subset":"train" })
     run.track(i, name='acc', step=i, context={ "subset":"train" })
 ```
 
 _See the full list of supported trackable objects(e.g. images, text, etc) [here](https://aimstack.readthedocs.io/en/latest/quick_start/supported_types.html)._
 
-**3. Run the training as usual and start Aim UI**
+## 3. Run the training as usual and start Aim UI
 
 ```shell
 aim up
 ```
 
-**4. Or query runs programmatically via SDK**
-
-```python
-from aim import Repo
-
-my_repo = Repo('/path/to/aim/repo')
-
-query = "metric.name == 'loss'" # Example query
-
-# Get collection of metrics
-for run_metrics_collection in my_repo.query_metrics(query).iter_runs():
-    for metric in run_metrics_collection:
-        # Get run params
-        params = metric.run[...]
-        # Get metric values
-        steps, metric_values = metric.values.sparse_numpy()
-```
-
-# Integrations
+## Learn more
 
 <details>
 <summary>
-  Integrate PyTorch Lightning
+<strong>Migrate from other tools</strong>
 </summary>
 
-```python
-from aim.pytorch_lightning import AimLogger
-
-# ...
-trainer = pl.Trainer(logger=AimLogger(experiment='experiment_name'))
-# ...
-```
+</br>
 
-_See documentation [here](https://aimstack.readthedocs.io/en/latest/quick_start/integrations.html#integration-with-pytorch-lightning)._
+Aim has built-in converters to easily migrate logs from other tools. 
+These migrations cover the most common usage scenarios.
+In case of custom and complex scenarios you can use Aim SDK to implement your own conversion script.
+
+- [TensorBoard logs converter](https://aimstack.readthedocs.io/en/latest/quick_start/convert_data.html#show-tensorboard-logs-in-aim)
+- [MLFlow logs converter](https://aimstack.readthedocs.io/en/latest/quick_start/convert_data.html#show-mlflow-logs-in-aim)
+- [Weights & Biases logs converter](https://aimstack.readthedocs.io/en/latest/quick_start/convert_data.html#show-weights-and-biases-logs-in-aim)
 
 </details>
 
 <details>
 <summary>
-  Integrate Hugging Face
+<strong>Integrate Aim into an existing project</strong>
 </summary>
 
-```python
-from aim.hugging_face import AimCallback
+</br>
 
-# ...
-aim_callback = AimCallback(repo='/path/to/logs/dir', experiment='mnli')
-trainer = Trainer(
-    model=model,
-    args=training_args,
-    train_dataset=train_dataset if training_args.do_train else None,
-    eval_dataset=eval_dataset if training_args.do_eval else None,
-    callbacks=[aim_callback],
-    # ...
-)
-# ...
-```
+Aim easily integrates with a wide range of ML frameworks, providing built-in callbacks for most of them.
 
-_See documentation [here](https://aimstack.readthedocs.io/en/latest/quick_start/integrations.html#integration-with-hugging-face)._
+- [Integration with Pytorch Ignite](https://aimstack.readthedocs.io/en/latest/quick_start/integrations.html#integration-with-pytorch-ignite)
+- [Integration with Pytorch Lightning](https://aimstack.readthedocs.io/en/latest/quick_start/integrations.html#integration-with-pytorch-lightning)
+- [Integration with Hugging Face](https://aimstack.readthedocs.io/en/latest/quick_start/integrations.html#integration-with-hugging-face)
+- [Integration with Keras & tf.Keras](https://aimstack.readthedocs.io/en/latest/quick_start/integrations.html#integration-with-keras-tf-keras)
+- [Integration with Keras Tuner](https://aimstack.readthedocs.io/en/latest/quick_start/integrations.html#integration-with-keras-tuner)
+- [Integration with XGboost](https://aimstack.readthedocs.io/en/latest/quick_start/integrations.html#integration-with-xgboost)
+- [Integration with CatBoost](https://aimstack.readthedocs.io/en/latest/quick_start/integrations.html#integration-with-catboost)
+- [Integration with LightGBM](https://aimstack.readthedocs.io/en/latest/quick_start/integrations.html#integration-with-lightgbm)
+- [Integration with fastai](https://aimstack.readthedocs.io/en/latest/quick_start/integrations.html#integration-with-fastai)
+- [Integration with MXNet](https://aimstack.readthedocs.io/en/latest/quick_start/integrations.html#integration-with-mxnet)
+- [Integration with Optuna](https://aimstack.readthedocs.io/en/latest/quick_start/integrations.html#integration-with-optuna)
+- [Integration with PaddlePaddle](https://aimstack.readthedocs.io/en/latest/quick_start/integrations.html#integration-with-paddlepaddle)
+- [Integration with Stable-Baselines3](https://aimstack.readthedocs.io/en/latest/quick_start/integrations.html#integration-with-stable-baselines3)
+- [Integration with Acme](https://aimstack.readthedocs.io/en/latest/quick_start/integrations.html#integration-with-acme)
+- [Integration with Prophet](https://aimstack.readthedocs.io/en/latest/quick_start/integrations.html#integration-with-prophet)
 
 </details>
 
 <details>
 <summary>
-  Integrate Keras & tf.keras
+<strong>Query runs programmatically via SDK</strong>
 </summary>
 
-```python
-import aim
-
-# ...
-model.fit(x_train, y_train, epochs=epochs, callbacks=[
-    aim.keras.AimCallback(repo='/path/to/logs/dir', experiment='experiment_name')
-    
-    # Use aim.tensorflow.AimCallback in case of tf.keras
-    aim.tensorflow.AimCallback(repo='/path/to/logs/dir', experiment='experiment_name')
-])
-# ...
-```
-
-_See documentation [here](https://aimstack.readthedocs.io/en/latest/quick_start/integrations.html#integration-with-keras-tf-keras)._
-
-</details>
+</br>
 
-<details>
-<summary>
-  Integrate KerasTuner
-</summary>
+Aim Python SDK empowers you to query and access any piece of tracked metadata with ease.
 
 ```python
-from aim.keras_tuner import AimCallback
-
-# ...
-tuner.search(
-    train_ds,
-    validation_data=test_ds,
-    callbacks=[AimCallback(tuner=tuner, repo='.', experiment='keras_tuner_test')],
-)
-# ...
-```
-
-_See documentation [here](https://aimstack.readthedocs.io/en/latest/quick_start/integrations.html#integration-with-kerastuner)._
-
-</details>
+from aim import Repo
 
-<details>
-<summary>
-  Integrate XGBoost
-</summary>
+my_repo = Repo('/path/to/aim/repo')
 
-```python
-from aim.xgboost import AimCallback
+query = "metric.name == 'loss'" # Example query
 
-# ...
-aim_callback = AimCallback(repo='/path/to/logs/dir', experiment='experiment_name')
-bst = xgb.train(param, xg_train, num_round, watchlist, callbacks=[aim_callback])
-# ...
+# Get collection of metrics
+for run_metrics_collection in my_repo.query_metrics(query).iter_runs():
+    for metric in run_metrics_collection:
+        # Get run params
+        params = metric.run[...]
+        # Get metric values
+        steps, metric_values = metric.values.sparse_numpy()
 ```
 
-_See documentation [here](https://aimstack.readthedocs.io/en/latest/quick_start/integrations.html#integration-with-xgboost)._
 </details>
 
-
 <details>
 <summary>
-  Integrate CatBoost
+<strong>Set up a centralized tracking server</strong>
 </summary>
 
-```python
-from aim.catboost import AimLogger
-
-# ...
-model.fit(train_data, train_labels, log_cout=AimLogger(loss_function='Logloss'), logging_level="Info")
-# ...
-```
-
-_See documentation [here](https://aimstack.readthedocs.io/en/latest/quick_start/integrations.html#integration-with-catboost)._
-</details>
+</br>
 
+Aim remote tracking server allows running experiments in a multi-host environment and collect tracked data in a centralized location.
 
+See the docs on how to [set up the remote server](https://aimstack.readthedocs.io/en/latest/using/remote_tracking.html).
 
-<details>
-<summary>
-  Integrate fastai
-</summary>
-
-```python
-from aim.fastai import AimCallback
-
-# ...
-learn = cnn_learner(dls, resnet18, pretrained=True,
-                    loss_func=CrossEntropyLossFlat(),
-                    metrics=accuracy, model_dir="/tmp/model/",
-                    cbs=AimCallback(repo='.', experiment='fastai_test'))
-# ...
-```
-
-_See documentation [here](https://aimstack.readthedocs.io/en/latest/quick_start/integrations.html#integration-with-fastai)._
 </details>
 
-
 <details>
 <summary>
-  Integrate LightGBM
+<strong>Deploy Aim on kubernetes</strong>
 </summary>
 
-```python
-from aim.lightgbm import AimCallback
+</br>
+
+- The official Aim docker image: https://hub.docker.com/r/aimstack/aim
+- A guide on how to deploy Aim on kubernetes: https://aimstack.readthedocs.io/en/latest/using/k8s_deployment.html
 
-# ...
-aim_callback = AimCallback(experiment='lgb_test')
-aim_callback.experiment['hparams'] = params
-
-gbm = lgb.train(params,
-                lgb_train,
-                num_boost_round=20,
-                valid_sets=lgb_eval,
-                callbacks=[aim_callback, lgb.early_stopping(stopping_rounds=5)])
-# ...
-```
 
-_See documentation [here](https://aimstack.readthedocs.io/en/latest/quick_start/integrations.html#integration-with-lightgbm)._
 </details>
 
+Read the full documentation on [aimstack.readthedocs.io](https://aimstack.readthedocs.io) 📖
+
+# 🆚 Comparisons to familiar tools
 
 <details>
 <summary>
-  Integrate PyTorch Ignite
+  <strong>TensorBoard vs Aim</strong>
 </summary>
 
-```python
-from aim.pytorch_ignite import AimLogger
-
-# ...
-aim_logger = AimLogger()
-
-aim_logger.log_params({
-    "model": model.__class__.__name__,
-    "pytorch_version": str(torch.__version__),
-    "ignite_version": str(ignite.__version__),
-})
-
-aim_logger.attach_output_handler(
-    trainer,
-    event_name=Events.ITERATION_COMPLETED,
-    tag="train",
-    output_transform=lambda loss: {'loss': loss}
-)
-# ...
-```
-
-_See documentation [here](https://aimstack.readthedocs.io/en/latest/quick_start/integrations.html#integration-with-pytorch-ignite)._
-</details>
-
-# Comparisons to familiar tools
+</br>
 
-### Tensorboard
 **Training run comparison**
 
 Order of magnitude faster training run comparison with Aim
 - The tracked params are first class citizens at Aim. You can search, group, aggregate via params - deeply explore all the tracked data (metrics, params, images) on the UI.
 - With tensorboard the users are forced to record those parameters in the training run name to be able to search and compare. This causes a super-tedius comparison experience and usability issues on the UI when there are many experiments and params. **TensorBoard doesn't have features to group, aggregate the metrics**
 
 **Scalability**
@@ -393,49 +372,117 @@
 - TensorBoard becomes really slow and hard to use when a few hundred training runs are queried / compared.
 
 **Beloved TB visualizations to be added on Aim**
 
 - Embedding projector.
 - Neural network visualization.
 
-### MLFlow
+</details>
+
+<details>
+<summary>
+  <strong>MLflow vs Aim</strong>
+</summary>
+
+</br>
+
 MLFlow is an end-to-end ML Lifecycle tool.
 Aim is focused on training tracking.
 The main differences of Aim and MLflow are around the UI scalability and run comparison features.
 
+Aim and MLflow are a perfect match - check out the [aimlflow](https://github.com/aimhubio/aimlflow) - the tool that enables Aim supoerpowers on Mlflow.
+
 **Run comparison**
 
 - Aim treats tracked parameters as first-class citizens. Users can query runs, metrics, images and filter using the params.
 - MLFlow does have a search by tracked config, but there are no grouping, aggregation, subplotting by hyparparams and other comparison features available.
 
 **UI Scalability**
 
 - Aim UI can handle several thousands of metrics at the same time smoothly with 1000s of steps. It may get shaky when you explore 1000s of metrics with 10000s of steps each. But we are constantly optimizing!
 - MLflow UI becomes slow to use when there are a few hundreds of runs.
 
-### Weights and Biases
+</details>
+
+<details>
+<summary>
+  <strong>Weights and Biases vs Aim</strong>
+</summary>
+
+</br>
 
 Hosted vs self-hosted
+
 - Weights and Biases is a hosted closed-source MLOps platform.
 - Aim is self-hosted, free and open-source experiment tracking tool.
 
-# Roadmap
+</details>
+
+# 🛣️ Roadmap
 
-## Detailed Sprints
+## Detailed milestones
 
-:sparkle: The [Aim product roadmap](https://github.com/orgs/aimhubio/projects/3)
+The [Aim product roadmap](https://github.com/orgs/aimhubio/projects/3) :sparkle: 
 
 - The `Backlog` contains the issues we are going to choose from and prioritize weekly
 - The issues are mainly prioritized by the highly-requested features
 
 ## High-level roadmap
 
-The high-level features we are going to work on the next few months
+The high-level features we are going to work on the next few months:
+
+**In progress**
+
+- [ ] Aim SDK low-level interface
+- [ ] Dashboards – customizable layouts with embedded explorers
+- [ ] Ergonomic UI kit
+- [ ] Text Explorer
+
+<details>
+<summary>
+  <strong>Next-up</strong>
+</summary>
+
+</br>
+
+**Aim UI**
+
+- Runs management
+    - Runs explorer – query and visualize runs data(images, audio, distributions, ...) in a central dashboard
+- Explorers
+    - Distributions Explorer
+
+**SDK and Storage**
+
+- Scalability
+    - Smooth UI and SDK experience with over 10.000 runs
+- Runs management
+    - CLI commands
+        - Reporting - runs summary and run details in a CLI compatible format
+        - Manipulations – copy, move, delete runs, params and sequences
+- Cloud storage support – store runs blob(e.g. images) data on the cloud
+- Artifact storage – store files, model checkpoints, and beyond
+
+**Integrations**
+
+- ML Frameworks:
+    - Shortlist: scikit-learn
+- Resource management tools
+    - Shortlist: Kubeflow, Slurm
+- Workflow orchestration tools
+
+</details>
+
+<details>
+<summary>
+  <strong>Done</strong>
+</summary>
+
+</br>
 
-### Done
   - [x] Live updates (Shipped: _Oct 18 2021_)
   - [x] Images tracking and visualization (Start: _Oct 18 2021_, Shipped: _Nov 19 2021_)
   - [x] Distributions tracking and visualization (Start: _Nov 10 2021_, Shipped: _Dec 3 2021_)
   - [x] Jupyter integration (Start: _Nov 18 2021_, Shipped: _Dec 3 2021_)
   - [x] Audio tracking and visualization (Start: _Dec 6 2021_, Shipped: _Dec 17 2021_)
   - [x] Transcripts tracking and visualization (Start: _Dec 6 2021_, Shipped: _Dec 17 2021_)
   - [x] Plotly integration (Start: _Dec 1 2021_, Shipped: _Dec 17 2021_)
@@ -463,54 +510,58 @@
   - [x] Integration with MXNet (Start: _Sep 20 2022_, Shipped: _Oct 6 2022_)
   - [x] Project overview page (Start: _Sep 1 2022_, Shipped: _Oct 6 2022_)
   - [x] Remote tracking server scaling (Start: _Sep 11 2022_, Shipped: _Nov 26 2022_)
   - [x] Integration with PaddlePaddle (Start: _Oct 2 2022_, Shipped: _Nov 26 2022_)
   - [x] Integration with Optuna (Start: _Oct 2 2022_, Shipped: _Nov 26 2022_)
   - [x] Audios Explorer (Start: _Oct 30 2022_, Shipped: _Nov 26 2022_)
   - [x] Experiment page (Start: _Nov 9 2022_, Shipped: _Nov 26 2022_)
+  - [x] HuggingFace datasets (Start: _Dec 29 2022_, _Feb 3 2023_)
 
-### In Progress
-  - [ ] Aim SDK low-level interface (Start: _Aug 22 2022_, )
-  - [ ] HuggingFace datasets (Start: _Dec 29 2022_, )
+</details>
 
-### To Do
+# 👥 Community
 
-**Aim UI**
+## Aim README badge
 
-- Runs management
-    - Runs explorer – query and visualize runs data(images, audio, distributions, ...) in a central dashboard
-- Explorers
-    - Text Explorer
-    - Distributions Explorer
-- Dashboards – customizable layouts with embedded explorers
+Add Aim badge to your README, if you've enjoyed using Aim in your work:
 
-**SDK and Storage**
+[![Aim](https://img.shields.io/badge/powered%20by-Aim-%231473E6)](https://github.com/aimhubio/aim)
 
-- Scalability
-    - Smooth UI and SDK experience with over 10.000 runs
-- Runs management
-    - CLI interfaces
-        - Reporting - runs summary and run details in a CLI compatible format
-        - Manipulations – copy, move, delete runs, params and sequences
+```
+[![Aim](https://img.shields.io/badge/powered%20by-Aim-%231473E6)](https://github.com/aimhubio/aim)
+```
 
-**Integrations**
+## Cite Aim in your papers
 
-- ML Frameworks:
-    - Shortlist: MONAI, SpaCy, Raytune
-- Resource management tools
-    - Shortlist: Kubeflow, Slurm
-- Workflow orchestration tools
-- Others: Hydra, Google MLMD, Streamlit, ...
+In case you've found Aim helpful in your research journey, we'd be thrilled if you could acknowledge Aim's contribution:
+
+```bibtex
+@software{Arakelyan_Aim_2020,
+  author = {Arakelyan, Gor and Soghomonyan, Gevorg and {The Aim team}},
+  doi = {10.5281/zenodo.6536395},
+  license = {Apache-2.0},
+  month = {6},
+  title = {{Aim}},
+  url = {https://github.com/aimhubio/aim},
+  version = {3.9.3},
+  year = {2020}
+}
+```
+
+## Contributing to Aim
+
+Considering contibuting to Aim? 
+To get started, please take a moment to read the [CONTRIBUTING.md](https://github.com/aimhubio/aim/blob/main/CONTRIBUTING.md) guide. 
 
-### On hold
+Join Aim contributors by submitting your first pull request. Happy coding! 😊
 
-- scikit-learn integration
-- Cloud storage support – store runs blob(e.g. images) data on the cloud (Start: _Mar 21 2022_)
-- Artifact storage – store files, model checkpoints, and beyond (Start: _Mar 21 2022_)
+<a href="https://github.com/aimhubio/aim/graphs/contributors">
+  <img src="https://contrib.rocks/image?repo=aimhubio/aim" />
+</a>
 
-## Community
+Made with [contrib.rocks](https://contrib.rocks).
 
-### If you have questions
+## More questions?
 
 1. [Read the docs](https://aimstack.readthedocs.io/en/latest/)
 2. [Open a feature request or report a bug](https://github.com/aimhubio/aim/issues)
 3. [Join Discord community server](https://community.aimstack.io/)
```

#### html2text {}

```diff
@@ -1,219 +1,270 @@
-Metadata-Version: 2.1 Name: aim Version: 4.0.0.dev1 Summary: A super-easy way
+Metadata-Version: 2.1 Name: aim Version: 4.0.0.dev2 Summary: A super-easy way
 to record, search and compare AI experiments. Classifier: License :: OSI
 Approved :: Apache Software License Classifier: Programming Language :: Python
 Classifier: Programming Language :: Python :: 3 Classifier: Programming
 Language :: Python :: 3.7 Classifier: Programming Language :: Python :: 3.8
 Classifier: Programming Language :: Python :: 3.9 Classifier: Programming
 Language :: Python :: 3.10 Classifier: Programming Language :: Python :: 3.11
 Classifier: Programming Language :: Python :: Implementation :: PyPy Requires-
 Python: >=3.7.0 Description-Content-Type: text/markdown License-File: LICENSE
- [https://user-images.githubusercontent.com/13848158/154338760-edfe1885-06f3-
-                          4e02-87fe-4b13a403516b.png]
+                               Join_Aim_discord_community [https://user-
+Drop a star to support Aim â­images.githubusercontent.com/13848158/226759622-
+                               063b725d-8b3e-4c75-80c7-11fb04b7adf5.png]
+ [https://user-images.githubusercontent.com/13848158/225620298-9f9293e9-a138-
+                          41fd-bd77-21d53d0490b7.png]
     **** An easy-to-use & supercharged open-source experiment tracker ****
-Aim logs your training runs, enables a beautiful UI to compare them and an API
-                        to query them programmatically.
+  Aim logs your training runs and any AI Metadata, enables a beautiful UI to
+       compare, observe them and an API to query them programmatically.
 
-[https://user-images.githubusercontent.com/13848158/154338753-34484cda-95b8-
-4da8-a610-7fdf198c05fd.png]
- About • Features • Demos • Examples • Quick_Start • Documentation • Roadmap •
-                          Discord_Community • Twitter
-[![Platform Support](https://img.shields.io/badge/platform-Linux%20%7C%20macOS-
-blue)]() [![PyPI - Python Version](https://img.shields.io/pypi/pyversions/aim)]
-(https://pypi.org/project/aim/) [![PyPI Package](https://img.shields.io/pypi/v/
-    aim?color=yellow)](https://pypi.org/project/aim/) [![License](https://
-img.shields.io/badge/License-Apache%202.0-orange.svg)](https://opensource.org/
-    licenses/Apache-2.0) [![PyPI Downloads](https://img.shields.io/pypi/dw/
-     aim?color=green)](https://pypi.org/project/aim/) [![Issues](https://
-  img.shields.io/github/issues/aimhubio/aim)](http://github.com/aimhubio/aim/
-                                    issues)
-                Integrates seamlessly with your favorite tools
-
- [https://user-images.githubusercontent.com/13848158/155354389-d0301620-77ea-
-    4629-a743-f7aa249e14b5.png] [https://user-images.githubusercontent.com/
-  13848158/155354496-b39d7b1c-63ef-40f0-9e59-c08d2c5e337c.png] [https://user-
-   images.githubusercontent.com/13848158/155354380-3755c741-6960-42ca-b93e-
-    84a8791f088c.png] [https://user-images.githubusercontent.com/13848158/
-      155354342-7df0ef5e-63d2-4df7-b9f1-d2fc0e95f53f.png] [https://user-
-   images.githubusercontent.com/13848158/155354392-afbff3de-c845-4d86-855d-
-    53df569f91d1.png] [https://user-images.githubusercontent.com/13848158/
-      155354355-89210506-e7e5-4d37-b2d6-ad3fda62ef13.png] [https://user-
-   images.githubusercontent.com/13848158/155354397-8af8e1d3-4067-405e-9d42-
-                              1f131663ed22.png]
- [https://user-images.githubusercontent.com/13848158/155354513-f7486146-3891-
-    4f3f-934f-e58bbf9ce695.png] [https://user-images.githubusercontent.com/
-  13848158/155354500-c0471ce6-b2ce-4172-b9e4-07a197256303.png] [https://user-
-   images.githubusercontent.com/13848158/155354361-9f911785-008d-4b75-877e-
-    651e026cf47e.png] [https://user-images.githubusercontent.com/13848158/
-      155354373-1879ae61-b5d1-41f0-a4f1-04b639b6f05e.png] [https://user-
-   images.githubusercontent.com/13848158/155354483-75d9853f-7154-4d95-8190-
-    9ad7a73d6654.png] [https://user-images.githubusercontent.com/13848158/
-      155354329-cf7c3352-a72a-478d-82a7-04e3833b03b7.png] [https://user-
-   images.githubusercontent.com/13848158/155354349-dcdf3bc3-d7a9-4f34-8258-
-    4824a57f59c7.png] [https://user-images.githubusercontent.com/13848158/
-      155354471-518f1814-7a41-4b23-9caf-e516507343f1.png] [https://user-
-   images.githubusercontent.com/48801049/165162736-2cc5da39-38aa-4093-874f-
-    e56d0ba9cea2.png] [https://user-images.githubusercontent.com/48801049/
-              165074282-36ad18eb-1124-434d-8439-728c22cd7ac7.png]
+           [![Discord Server](https://dcbadge.vercel.app/api/server/
+zXq2NfVdtF?compact=true&style=flat)](https://community.aimstack.io/) [![Twitter
+Follow](https://img.shields.io/twitter/follow/aimstackio?style=social)](https:/
+   /twitter.com/aimstackio) [![Medium](https://img.shields.io/badge/Medium-
+12100E?style=flat&logo=medium&logoColor=white)](https://medium.com/aimstack) [!
+ [Platform Support](https://img.shields.io/badge/platform-Linux%20%7C%20macOS-
+    blue)]() [![PyPI - Python Version](https://img.shields.io/badge/python-
+ %3E%3D%203.7-blue)](https://pypi.org/project/aim/) [![PyPI Package](https://
+  img.shields.io/pypi/v/aim?color=yellow)](https://pypi.org/project/aim/) [!
+[License](https://img.shields.io/badge/License-Apache%202.0-orange.svg)](https:
+       //opensource.org/licenses/Apache-2.0) [![PyPI Downloads](https://
+  img.shields.io/pypi/dw/aim?color=green)](https://pypi.org/project/aim/) [!
+[Issues](https://img.shields.io/github/issues/aimhubio/aim)](http://github.com/
+                             aimhubio/aim/issues)
 
  [https://user-images.githubusercontent.com/13848158/136374529-af267918-5dc6-
                           4a4e-8ed2-f6333a332f96.gif]
-# About Aim | Track and version ML runs | Visualize runs via beautiful UI |
-Query runs metadata via SDK | |:--------------------:|:-----------------------
--:|:-------------------:| | [https://user-images.githubusercontent.com/
-13848158/154337794-e9310239-6614-41b3-a95b-bb91f0bb6c4f.png] | [https://user-
-images.githubusercontent.com/13848158/154337788-03fe5b31-0fa3-44af-ae79-
-2861707d8602.png] | [https://user-images.githubusercontent.com/13848158/
-154337793-85175c78-5659-4dd0-bb2d-05017278e2fa.png] | Aim is an open-source,
-self-hosted ML experiment tracking tool. It's good at tracking lots (1000s) of
-training runs and it allows you to compare them with a performant and beautiful
-UI. You can use not only the great Aim UI but also its SDK to query your runs'
-metadata programmatically. That's especially useful for automations and
-additional analysis on a Jupyter Notebook. Aim's mission is to democratize AI
-dev tools. # Why use Aim? ### Compare 100s of runs in a few clicks - build
-models faster - Compare, group and aggregate 100s of metrics thanks to
-effective visualizations. - Analyze, learn correlations and patterns between
-hparams and metrics. - Easy pythonic search to query the runs you want to
-explore. ### Deep dive into details of each run for easy debugging -
-Hyperparameters, metrics, images, distributions, audio, text - all available at
-hand on an intuitive UI to understand the performance of your model. - Easily
-track plots built via your favourite visualisation tools, like plotly and
-matplotlib. - Analyze system resource usage to effectively utilize
-computational resources. ### Have all relevant information organised and
-accessible for easy governance - Centralized dashboard to holistically view all
-your runs, their hparams and results. - Use SDK to query/access all your runs
-and tracked metadata. - You own your data - Aim is open source and self hosted.
-# Demos | Machine translation | lightweight-GAN | |:---:|:---:| | [https://
-user-images.githubusercontent.com/13848158/154340796-c9e91b13-8ee0-4a67-bcde-
-8cf3aaa7ba99.jpg] | [https://user-images.githubusercontent.com/13848158/
-154340790-bc7b7a21-e8a1-43a1-809d-4060b5bfb60f.jpg] | | Training logs of a
-neural translation model(from WMT'19 competition). | Training logs of
-'lightweight' GAN, proposed in ICLR 2021. | | FastSpeech 2 | Simple MNIST | |:-
---:|:---:| | [https://user-images.githubusercontent.com/13848158/154340778-
-dbe19620-2f27-4298-b0cb-caf3904760f1.jpg] | [https://user-
-images.githubusercontent.com/13848158/154340785-a7e4d9fd-d048-4207-8cd1-
-c4edff9cca6a.jpg] | | Training logs of Microsoft's "FastSpeech 2: Fast and
-High-Quality End-to-End Text to Speech". | Simple MNIST training logs. | #
-Quick Start Follow the steps below to get started with Aim. **1. Install Aim on
-your training environment** ```shell pip3 install aim ``` **2. Integrate Aim
-with your code** ```python from aim import Run # Initialize a new run run = Run
-() # Log run parameters run["hparams"] = { "learning_rate": 0.001,
+                         SEAMLESSLY INTEGRATES WITH:
+
+ [https://user-images.githubusercontent.com/97726819/225954732-2b263308-8ed8-
+    4df3-810b-704840328e98.png] [https://user-images.githubusercontent.com/
+  97726819/225954727-04eccf0e-51ed-4f2d-8f3b-c9a675ca8e8f.png] [https://user-
+   images.githubusercontent.com/97726819/225954728-ca2f498d-51a7-487b-bd69-
+    ffb5f0c2af58.png] [https://user-images.githubusercontent.com/97726819/
+      225954689-1076998c-42f4-4e31-ab47-d9f39575fda1.png] [https://user-
+   images.githubusercontent.com/97726819/225954739-0231d659-3202-4458-9c35-
+    ba92d1f079b8.png] [https://user-images.githubusercontent.com/97726819/
+      225954697-ef2c7091-b089-4b68-8543-80ce7275b683.png] [https://user-
+   images.githubusercontent.com/97726819/225954743-dbfe1e98-7b9f-446a-9fe4-
+    ad4fd562f3df.png] [https://user-images.githubusercontent.com/97726819/
+      225954736-7c52ab5a-6780-4375-a6f8-b394dae3ad31.png] [https://user-
+   images.githubusercontent.com/97726819/225954710-36551a71-b26d-4665-af20-
+    44ee452dd5dd.png] [https://user-images.githubusercontent.com/97726819/
+      225954707-4bc078b5-ae6f-4847-bc2c-3f81959accb2.png] [https://user-
+   images.githubusercontent.com/97726819/225954725-a4d4c32c-75db-470a-b1da-
+    698982faa23c.png] [https://user-images.githubusercontent.com/97726819/
+      225954665-8d844747-a857-41b8-9104-7c27a8bdb81a.png] [https://user-
+   images.githubusercontent.com/97726819/225954686-b9c8ec57-d4fc-44e1-a4b8-
+    443db381a00f.png] [https://user-images.githubusercontent.com/97726819/
+      225954693-94bc20b4-f51a-4130-8d5f-ddee30d81205.png] [https://user-
+   images.githubusercontent.com/97726819/225954674-42fbfdb3-0351-492d-9ea3-
+    1d3ab2b545f5.png] [https://user-images.githubusercontent.com/97726819/
+      225954678-25f1b626-2cb1-4e7e-ad83-f7c8ab679c6f.png] [https://user-
+   images.githubusercontent.com/97726819/225954702-d18d2706-dc87-4e09-a678-
+                               f010f6d95736.png]
+
+                          TRUSTED BY ML TEAMS FROM:
+
+ [https://user-images.githubusercontent.com/97726819/225952594-a21546f4-987f-
+    42bd-9154-c22b50632b55.png] [https://user-images.githubusercontent.com/
+  97726819/225953224-291fbb6d-e31a-4e36-90ba-92a1dc20bacc.png] [https://user-
+   images.githubusercontent.com/97726819/225953339-4fcc3c99-dda2-4529-ac2a-
+    29c8293be323.png] [https://user-images.githubusercontent.com/97726819/
+      225953084-1d88325a-ad5f-49eb-aa67-f064c4b9f39c.png] [https://user-
+   images.githubusercontent.com/97726819/225952955-397e0f26-f01e-4b25-bd70-
+    9f292a6f77c2.png] [https://user-images.githubusercontent.com/97726819/
+      225952682-a843827b-e870-429d-96d8-3b4fd45471cd.png] [https://user-
+   images.githubusercontent.com/97726819/225952831-1c0e36aa-4120-4635-ab4e-
+    bf1bc685477b.png] [https://user-images.githubusercontent.com/97726819/
+              225953432-4b27653a-aa12-4fbf-897c-01349afa2ad0.png]
+
+    AimStack offers enterprise support that's beyond core Aim. Contact via
+                           hello@aimstack.io e-mail.
+---
+   **** About • Demos • Ecosystem • Quick_Start • Examples • Documentation •
+                             Community • Blog ****
+--- # â¹ï¸ About Aim is an open-source, self-hosted ML experiment tracking
+tool designed to handle 10,000s of training runs. Aim provides a performant and
+beautiful UI for exploring and comparing training runs. Additionally, its SDK
+enables programmatic access to tracked metadata â perfect for automations and
+Jupyter Notebook analysis.
+               Aim's mission is to democratize AI dev tools ð¯
+ [https://user-images.githubusercontent.com/13848158/226426018-f7c11c9b-78d9-
+    4ee4-b292-df28b3e8eaa6.jpg] [https://user-images.githubusercontent.com/
+  13848158/226426005-f7e83923-0f92-44a4-88e4-1735a3d3e119.jpg] [https://user-
+   images.githubusercontent.com/13848158/226426015-4f1122d8-c96a-443f-8698-
+                               3db942b1972a.jpg]
+Log Metadata Across Your ML Pipeline  Visualize & Compare Metadata via UI ð
+ð¾
+    * ML experiments and any metadata
+      tracking                            * Metadata visualization via Aim
+    * Integration with popular ML           Explorers
+      frameworks                          * Grouping and aggregation
+    * Easy migration from other           * Querying using Python expressions
+      experiment trackers
+Run ML Trainings Effectively â¡   Organize Your Experiments ðï¸
+    * System info and resource usage      * Detailed run information for easy
+      tracking                              debugging
+    * Real-time alerting on training      * Centralized dashboard for holistic
+      progress                              view
+    * Logging and configurable            * Runs grouping with tags and
+      notifications                         experiments
+# ð¬ Demos Check out live Aim demos NOW to see it in action. | [Machine
+translation experiments](http://play.aimstack.io:10001/
+metrics?grouping=HQGdK9Xxy35e6sY1CYkCmk1WbWMN2AsCNfJJ3d1RJYLtrVPMoF5UpGiA6CF8bEJnfzRsKpqespf3AEuKSVrhUYvYk9MxzNGA9XZWYUf6phEg8AMbZGLRVDXnAPDuo8tueqsST1ZLizWzQwDYJWHUza6pyB2Eojt9uWqNHUdb858TqDRnCJzqiVJXKXEzFWUyvU8MckJo1qpqWWCTb4GpYN6DUJZx2GXDGR21e2xxd4m7PmNUnbA9B3apLttZoipJF6c3v7tNUKmb6irpqnNB3yc57tqYDa1XZuKfDxkMtyFdQ1x95K4jjsTVwhftEWLze35QNcxNXRCGGS9o9yEfTLG26GUX2zjPZFCjjMGU6vV7z1xRccK8MyoGrLSgAQCbvk68dTGBHpXUBvCRq8N&chart=FviZzVrt4fVQPjpCLr9sVGGrcR5etSroyqambiKpm3nTgpyv4eQxKuwNX9uN8UtKmzYUhUyTMBEANHmtbwjLApkvnYeNbxGNC6PVcoqi65m1XJnSrvgt8WiD89BapFAWRUwAGx6SWD7KZPsk3RQyysU7W7FjD3Q99NusxFGhsEfD6HXc7i8xH9KHDRGjLwh6x9VTtSp4FS8HEvpLSiiJoX7LCTi8pB7dXvrQ8G5w3jPsFz4qXYFdsVaCNL1BpFFZuiqQNkfbnM84gEq7UmiV1VzM4oS3AgQHxADG3kpBVp6eKTey9F1Swd4FcUkFA9QEPjgQgqwRGjkquZ2bdDDVLBnCh7JPvboP2kifCiZZ5MDdV9MMx6PKHp4DusWyWLXiHQYPkpGPWBiuccMUXDsuJaCWJbuABdY7CyiJMv1jdHYkjabygSxehPVyEDefWAtjBfv2vaeM1xv63jadbmpKYFxft7qmuT9HvVxiGvRgs4RQFxy8K4rtFBca3HNs1mDaaY81gy9MGXyw7BS5Fniu92jaJpsWDdg6Y3AQBLZtrpJy2obEZ4yzJaCVT7JUNPAyyCUNLck393VFLoEkaD9CU5npK5R7tj1c1G3gkMNQXnSXy5NpSj8deMmXV5qz3JKu1nq2caGQKcqjzy2gLkExdm674AMFjSg9yFjK6VqASXQ17NKtWRUvaYoxGbHDAFQaMKWKh8QLm22QA9mKT8NksLptWozbgDvafnQLNMvezLU5bvKV5o75PAWYiRB56RcYfEhzaB6YWdgL7TJicyY5rFi6Az8UZ7wqB3N5iMuZdpxhKn5KbZDxyuUMuvVt24i5LVPPmmwQtqxMoJ4aLo48a2YvDW6TAkdQjNjvn6KcEEz6GTixujb1YHhMUD8v4AepWKEwKz1ddEca1P2wLQjbpihCuaqbxeohnuZZLogJdUBojBEDgrnrrVpPBaLLEkGSpkJbtrsKUuEeBo1AF3yNgHftLbynGpobVF5DhmsmddmiA6c8vSTokJxHhjpnW8mAcNHBRtmVJCT7VkdHSAhNypM4Hivwfx5jCccG9LauKmCeRMDzHiA57TX9W6ttcPHSvUyQorARQAd2oeNY4H83hZjHh9Bt8iwKZRt4xK6hrTR8tif7hq8eURXrGH9Ys7TzykXK8FHHWvLNzNnYf3E4a9NkD43MjfKvMM1hj4Q2K8MHbmRCqrmFrHP5kim9shq6mhLPTgwha32nvnrBkfPQVPwpGTzKuwE&select=CdsQ7jVNkogQhRzQR3e28Ek39AZ4Ma2y37k5zJaf9EZmQhMjy8GtGm4LGU6dRFuAVG7mYww5xDrQAE74KHQ3Kk1e6661RmcmNALAUjtHyCmrTVBMCnBGNiuq1y7EzmxoodYHU1BV1rnoefQAw2kTBtbWi11hV1P4LcwFCcXfUWF6rpRC7ehEnUCTqUV4bkGVJPLcmk9mdmiGwa2YgmnSShNGPVGZiEi1rMVECyngSRVdqdZwAeXBGWFLfqF1KbZeCo4MTF4SSmFupJ9zLhYbuojEbopyFWHQ6xs3sq9epPeaQziLM4Js7oFYRmuFWUYdFqnZngmewXWmi7tQAgVqhiT6dMjG2eTdfgX6WuRSuoHALkh2XJhHA6GfZLUcxC5Ni9YyKuBTamtaYarbNNJJ8z15WWvuUkLpjgHdEpE2h924xFdu8aoZNuiQxYGvcndaW1BTGMXS5fTKPqYfe2n8Ky2HWPkcX3hEXtyawu1F9BndKNaXLPgsdAoFBArBZnSe28YtSmTa5LRucKVBAxakvv5MWMXchAmpaGFQbZyYUoMgQLcJd7Y96x6zSR7nhwr5Ar81BrmqYz2WFLuk7osUbwsc9HbSG6CQt8p6Vg2u7DjKaZXW8pjkPHAKrHWtHEDiJPJ5rj6VsdFm3)
+| [lightweight-GAN experiments](http://play.aimstack.io:10002/
+images?grouping=E1zQzcmtDR3wibEa1MVysTvCyZEv1T8ixkCxTWExCyMnHtX2HyiF9eszvPgfd2xdJ5TUTKGpSs1bsLVq5tHAV3uWtsZmmckn6HjNtVCMyQDJpwhiEy5tAyw&select=2NEXuD7fFoaLcwRjymjA1wLmUrGs9s3AiXcCW82C367SwJt18CAB6xzkMGowrUDuDwggE1huaPVcQJpQUsmAQx1CnGiqCUBp2jPMd5mMNPX2QKQMcmvu9ZykBNkeBvCQFPd9ERuQD2g1EjWuvyJ3H53mAZTfp94LCXvR9CUsG5ei2CjQUzfZLM6DCyUr1GPaEVnY5f1EwzicNxXuoutkBgqCqaobJ7Do4q4eHAA6ooiWU6ekS3D2sLj6qYwhVTjfGCPfbWwBiH83nFkY3fLExzdeTY2zeUHeeYikQR9S7xHbVD8WvjekdQVp8X4dNLJZxiVmEqHpPRnU3ZrYsMhE7yFAAgjJwPNUzLTt6YFrtZBcmc4rwAC2oyrqysUSEr6gzL6LcJ6yuqDGf9D5tzftHbTLDkhc8B2sCgTS&images=9vt2MvuQj2Q7jxGQYhNH6ZnWw4CsEzubFcFotuqCHfzvuruDs6pyWfhqhinD4hCiYsAURXgJbmq2L5z4vEQMbrE7iTy8XHNndPBPyuCEvRpxGwwFkukX3YGkVhNDQmUPtBagKbsMAgUASJM8hFtKboqbu9KWTModsjd4Qag7aL1KbJCzBYmZLCpKMSf6eKUTQtfwLLWbgquEx6oahAoSujV6aZ5cjsjN4JdGtPbicySpccgLDQHaQYTHCseA6sPVaEwCsoQDJAcTnjEVFFUUUW5HbPkrNgeRKb8M9pxudrweRQ3gNukLx5yizxQKrmcKU7saxLraqYUA2y5LmEQohsWGUq8sKkvGDH6oNLx2ytJsdVM5PGieENXMAaPg3KuWYXXTwixzwscdDsHSWeiXTGj1QxUKiBCnfwkZ7pZbYMCSgczSn9WpwygrKhb2znSYhn4gFzCsdjiXPPDv9LpPzkFVbsMCvk1CadqpwxTfxNmteKm7CQVViyCrvheGAk5rKpPzaBc5agyvfKpUqgRarxojnG8a4s1Y7qFT1rNVSC13C9h5fG54dDoFHxDyvej3bVTMDYsAiie3eVA3yEskyBGwApPNtjLY2H4b9jTmR3V7jnA9moFGfwMiXUjt8eoJsWTNkqBdRGSnqdva8zi5bApQaggnLebgCRpK1g8VvPrVS3ABQC8aMZJ2vibebHePWs1ahWZ2AXUUYwcuSRkiUWHwgtG9U1x6rR41UxFFNvW9rpDsU99DWzYpdgxfU75wTEPb2qeXYPxV1zVt5ixcFfA3Lvtsp5XXyfHY9FaNFeKKzAUQXPAkMWG4yH4Tp5me8Nt4puBC4pvJrboVcQdSsYhtxj2YwUjzN7Jyn9BV28dtRFPdtFUUc9pKpLvhZAD6XPDtKqrN3pG3LwYTKAiMDtC6tHvDqhQGuJGQZH5cVyTKkT48Xup4znass8tJxUJwacVQa6x2ewyd8AXCfc4j9bPQssabADmc1ho5Eghn5qe82cEcyG1okdfBCRMfmZ5EeCeKQYmoXddxM2cAwfJzCzG9bGtaMvXk3VV8TrSiRKjg3Exbftv8gx12QAzoBP9zosuULFpEAPZF1TvHJbEUmYgu9gwuRTAS3qYiywB7dsCq8wsTr7qmwt8WFFucpte8WvrkRGYy1GA7bD6uPhvS6sr1Wv259oB7Tkr5kirMo6Vdkz8ex9zVd4h2AP1J1dy8cqXaSk5B3HTZ6n1qdAMt4faLtt8SNqg4EqcvXx6r2J1czzXAPa9oSseYifvedcMyxnWkcTvno4QA6sp6zH25ubEwPAVzZZk35nNoJPasH3PgEgLafGPLCsPDD2sku5djPjfqkbDLUWMYm7BbTr7xK8v4UoTS485rPiF6VKoNQSuEnKQMT3uNRTS4EXNMjyRfUs4gk1217EhGVLhfqiZQyG4gqEhcJE3phLydLskk36PyGEbyFyvigjwvrK6boJnFpesze6Czc13HdWbWp6LHLseYujigdmdktU6EQb5KmghstmJ9gUF14JVPjYP57xtv19UT8XDuaJfwJn9z3U17ZDFnQ5zbXKSwD9ikMEd6VFo1xLBRHSmRdFSqcC96s23qWmMhheGtv6tTQAkq7CB1J1gy3skuFJXqhs1RvFWbFFUCLmHeTCtskEsQVP5Rkzat5Jn3QtSqCiRpEGc9Ykd5bWFAaqoudGcqEt993tVfVS3ZrVKAa6NDmbtAcdnfsUZxDt2muRPJDNVCBNW5k8XvevMpMsL3uCETtdutufp1VyLur2Yyx5WA8AeeFeDBxRxad3ZHbH27XdMpxWHF26hnbQAewspG1weRpVW9Ebc4Lc53RBeu8gVmTbKydrri1FHaYySZqCxht8bN4kdqSmkymmcTN3cfRN9DmzcmfKG6GbTDeCA9oXz5cVqrGXZcAiaj1oinnByW7W8GwhtK1Tzd7LG74Nu35DUdPCJXMH2ug4SEa3yXERXCaLvAHvFZAS89e7RUPpr3nTTrQLurjHSdkJ39pwEJpDcDjeWHsJSmTG1x195e6xvMmgPxAZd3Lzyk8Cxme8p1cY7FehSbTPc3zAAwi9LDGYyoQRcdbRHPLJ2W8rt9KeNfNq9moa1RVFPCPvhGuuyycT4f4QkP4Nvy4iUCaB5d8B1hcgmtg2X9Zpg6GUR32RYneQigK6S9ZYPNnaFeCNZZrwaYjkDpKMTMB6N24JC1TEAH8en3kXzf8CpLWeJpxoyB3hcCxjFHLYaovzgfGPeFBPY6ADDUcT3xkpUUEybdxE1cX7drHvBwyGqeU5g7i424tydxqufUgPY5sF9bM6mdoA3AvqDD9B3Zai71irxYXX8e6rRck4RwptJgBMX2gbotizoz9LrUwFQ2naBfJvbfEhZNCzME8a7H2YiVcq4Z6pkfbT1uMLfaixfw8nQCzVRbJAyVZgGzVbBj242LpD48R6VmxGcU5t2XkN8hZyYdBk1Uds9QyUG9VpC8ka7HjkvxBMknk6v4BjMnHnAj4ZxDUxMWEDbWw6iWD3iYWzVn3n5dzRcAqCQv3m2ZUnwuHHCTVJVZKZVyxrFP5eznpNv87RUXMfjbXypoLJFVtMoq81y82hYRFSkbAUwzhhoXBAGeBGDmDcwky2Hf7ZmfkzDLnRke916VxhTRLr8c6nXokCn8xwweuJHFeBqx7D88gpRbn5RrnH33545zyzyNpZpabQUGY3L7G3QznVw6wCS9x7FMixW2mgCeeWFhPDiz5Kz6DyyjaT413VSoRBCRakNcitYHUXqqCUPsFmZ3LTedA8jN99fYzse5LX36TSVbjnM7XmiZ8vNoH5mUsawmvG7NXbhgoyhx4rzL7t57A4g7sQg4YhGAFzEbXrh416riiPH8r52on2VEqkjNPDnybSg3cwuR6rPfMWA7YoyEAp14aStUPaKqbM9omConMxZde5o2DpjS86G5vDBY1o7F4LnBHLHRxKfqAkTPjvEdhaYY2uY6i598po9b2fAtpUGCbXnzcNrV5Vei5WkiQAqRT6whGr29PTLsAVGed71drx7BqzNiDcFJBL9dVrVoPqYLvrYVGi89MuuWuirD7CRhXWahysjrNpFf4aHXmuXS3UD7SFgkqAZzL1hrVq77K8UhGMMWLUzE9gjP6PH4xL6fJetKaRGZNpbsqDoKuBkBAk9j1nGpYMAyuo2H2AWUyj8PUgAbi1e4KPeqNqMVT85oZ9jkCggYczgNhT8gw5QsMarouMctMdbokxRfxz2xt9r2DuNmbEmq9e13Tqv94VrzR91R2o7pvH7YUFtJvcoJwR8K5jyof5SfKHT53zaBKxkLfCpPP3qR9ZCbAzVbreFKsQnCcZpd643VA9wtgKXxc375NwKj4QbnvafKNU9qc455d3S3o57mU4DFA7yHSqY1q41zySxfXYx4txL4TiqeyyTQu7KcHYbTUYRs69pkE1rWRW84N1qmisw2o7iLQPrhWkixrRDRk5toYWQg6ZDZExCyedYBGjsUAut)|
+|:---:|:---:| | [https://user-images.githubusercontent.com/97726819/225964524-
+0051c2c7-8554-43ae-82b8-adcb77bcf1ba.png] | [https://user-
+images.githubusercontent.com/97726819/225948275-a41946ea-89f4-45f1-bce1-
+251c84dcddca.png] | | Training logs of a neural translation model(from WMT'19
+competition). | Training logs of 'lightweight' GAN, proposed in ICLR 2021. | |
+[FastSpeech 2 experiments](http://play.aimstack.io:10004/runs/
+d9e89aa7875e44b2ba85612a/audios)| [Simple MNIST](http://play.aimstack.io:10003/
+runs/7f083da898624a2c98e0f363/distributions) | |:---:|:---:| | [https://user-
+images.githubusercontent.com/97726819/225948457-567526da-a329-4c53-a9a7-
+98dfe392d4c4.png] | [https://user-images.githubusercontent.com/97726819/
+225948599-ff39c5b7-ae7d-4deb-8bc9-5eee1e189d89.png] | | Training logs of
+Microsoft's "FastSpeech 2: Fast and High-Quality End-to-End Text to Speech". |
+Simple MNIST training logs. | # ð Ecosystem Aim is not just an experiment
+tracker. It's a groundwork for an ecosystem. Check out the two most famous Aim-
+based tools. | [aimlflow](https://github.com/aimhubio/aimlflow) | [Aim-spaCy]
+(https://github.com/aimhubio/aim-spacy) | |:---:|:---:| | ![aimlflow](https://
+user-images.githubusercontent.com/97726819/225957836-cdec88e3-4993-435a-a135-
+d78be3ac1635.png) | ![Aim-spaCy](https://user-images.githubusercontent.com/
+97726819/225957990-4edc4525-1f65-4405-b663-ce7af888bdfa.png) | | Exploring
+MLflow experiments with a powerful UI | an Aim-based spaCy experiment tracker |
+# ð Quick start Follow the steps below to get started with Aim. ## 1.
+Install Aim on your training environment ```shell pip3 install aim ``` ## 2.
+Integrate Aim with your code ```python from aim import Run # Initialize a new
+run run = Run() # Log run parameters run["hparams"] = { "learning_rate": 0.001,
 "batch_size": 32, } # Log metrics for i in range(10): run.track(i, name='loss',
 step=i, context={ "subset":"train" }) run.track(i, name='acc', step=i, context=
 { "subset":"train" }) ``` _See the full list of supported trackable objects
 (e.g. images, text, etc) [here](https://aimstack.readthedocs.io/en/latest/
-quick_start/supported_types.html)._ **3. Run the training as usual and start
-Aim UI** ```shell aim up ``` **4. Or query runs programmatically via SDK**
-```python from aim import Repo my_repo = Repo('/path/to/aim/repo') query =
-"metric.name == 'loss'" # Example query # Get collection of metrics for
-run_metrics_collection in my_repo.query_metrics(query).iter_runs(): for metric
-in run_metrics_collection: # Get run params params = metric.run[...] # Get
-metric values steps, metric_values = metric.values.sparse_numpy() ``` #
-Integrations   Integrate PyTorch Lightning  ```python from
-aim.pytorch_lightning import AimLogger # ... trainer = pl.Trainer
-(logger=AimLogger(experiment='experiment_name')) # ... ``` _See documentation
-[here](https://aimstack.readthedocs.io/en/latest/quick_start/
-integrations.html#integration-with-pytorch-lightning)._    Integrate Hugging
-Face  ```python from aim.hugging_face import AimCallback # ... aim_callback =
-AimCallback(repo='/path/to/logs/dir', experiment='mnli') trainer = Trainer
-( model=model, args=training_args, train_dataset=train_dataset if
-training_args.do_train else None, eval_dataset=eval_dataset if
-training_args.do_eval else None, callbacks=[aim_callback], # ... ) # ... ```
-_See documentation [here](https://aimstack.readthedocs.io/en/latest/
-quick_start/integrations.html#integration-with-hugging-face)._    Integrate
-Keras & tf.keras  ```python import aim # ... model.fit(x_train, y_train,
-epochs=epochs, callbacks=[ aim.keras.AimCallback(repo='/path/to/logs/dir',
-experiment='experiment_name') # Use aim.tensorflow.AimCallback in case of
-tf.keras aim.tensorflow.AimCallback(repo='/path/to/logs/dir',
-experiment='experiment_name') ]) # ... ``` _See documentation [here](https://
-aimstack.readthedocs.io/en/latest/quick_start/integrations.html#integration-
-with-keras-tf-keras)._    Integrate KerasTuner  ```python from aim.keras_tuner
-import AimCallback # ... tuner.search( train_ds, validation_data=test_ds,
-callbacks=[AimCallback(tuner=tuner, repo='.', experiment='keras_tuner_test')],
-) # ... ``` _See documentation [here](https://aimstack.readthedocs.io/en/
-latest/quick_start/integrations.html#integration-with-kerastuner)._
-Integrate XGBoost  ```python from aim.xgboost import AimCallback # ...
-aim_callback = AimCallback(repo='/path/to/logs/dir',
-experiment='experiment_name') bst = xgb.train(param, xg_train, num_round,
-watchlist, callbacks=[aim_callback]) # ... ``` _See documentation [here](https:
+quick_start/supported_types.html)._ ## 3. Run the training as usual and start
+Aim UI ```shell aim up ``` ## Learn more   Migrate from other tools   Aim has
+built-in converters to easily migrate logs from other tools. These migrations
+cover the most common usage scenarios. In case of custom and complex scenarios
+you can use Aim SDK to implement your own conversion script. - [TensorBoard
+logs converter](https://aimstack.readthedocs.io/en/latest/quick_start/
+convert_data.html#show-tensorboard-logs-in-aim) - [MLFlow logs converter]
+(https://aimstack.readthedocs.io/en/latest/quick_start/convert_data.html#show-
+mlflow-logs-in-aim) - [Weights & Biases logs converter](https://
+aimstack.readthedocs.io/en/latest/quick_start/convert_data.html#show-weights-
+and-biases-logs-in-aim)    Integrate Aim into an existing project   Aim easily
+integrates with a wide range of ML frameworks, providing built-in callbacks for
+most of them. - [Integration with Pytorch Ignite](https://
+aimstack.readthedocs.io/en/latest/quick_start/integrations.html#integration-
+with-pytorch-ignite) - [Integration with Pytorch Lightning](https://
+aimstack.readthedocs.io/en/latest/quick_start/integrations.html#integration-
+with-pytorch-lightning) - [Integration with Hugging Face](https://
+aimstack.readthedocs.io/en/latest/quick_start/integrations.html#integration-
+with-hugging-face) - [Integration with Keras & tf.Keras](https://
+aimstack.readthedocs.io/en/latest/quick_start/integrations.html#integration-
+with-keras-tf-keras) - [Integration with Keras Tuner](https://
+aimstack.readthedocs.io/en/latest/quick_start/integrations.html#integration-
+with-keras-tuner) - [Integration with XGboost](https://aimstack.readthedocs.io/
+en/latest/quick_start/integrations.html#integration-with-xgboost) -
+[Integration with CatBoost](https://aimstack.readthedocs.io/en/latest/
+quick_start/integrations.html#integration-with-catboost) - [Integration with
+LightGBM](https://aimstack.readthedocs.io/en/latest/quick_start/
+integrations.html#integration-with-lightgbm) - [Integration with fastai](https:
 //aimstack.readthedocs.io/en/latest/quick_start/integrations.html#integration-
-with-xgboost)._    Integrate CatBoost  ```python from aim.catboost import
-AimLogger # ... model.fit(train_data, train_labels, log_cout=AimLogger
-(loss_function='Logloss'), logging_level="Info") # ... ``` _See documentation
-[here](https://aimstack.readthedocs.io/en/latest/quick_start/
-integrations.html#integration-with-catboost)._    Integrate fastai  ```python
-from aim.fastai import AimCallback # ... learn = cnn_learner(dls, resnet18,
-pretrained=True, loss_func=CrossEntropyLossFlat(), metrics=accuracy,
-model_dir="/tmp/model/", cbs=AimCallback(repo='.', experiment='fastai_test')) #
-... ``` _See documentation [here](https://aimstack.readthedocs.io/en/latest/
-quick_start/integrations.html#integration-with-fastai)._    Integrate LightGBM
-```python from aim.lightgbm import AimCallback # ... aim_callback = AimCallback
-(experiment='lgb_test') aim_callback.experiment['hparams'] = params gbm =
-lgb.train(params, lgb_train, num_boost_round=20, valid_sets=lgb_eval,
-callbacks=[aim_callback, lgb.early_stopping(stopping_rounds=5)]) # ... ``` _See
-documentation [here](https://aimstack.readthedocs.io/en/latest/quick_start/
-integrations.html#integration-with-lightgbm)._    Integrate PyTorch Ignite
-```python from aim.pytorch_ignite import AimLogger # ... aim_logger = AimLogger
-() aim_logger.log_params({ "model": model.__class__.__name__,
-"pytorch_version": str(torch.__version__), "ignite_version": str
-(ignite.__version__), }) aim_logger.attach_output_handler( trainer,
-event_name=Events.ITERATION_COMPLETED, tag="train", output_transform=lambda
-loss: {'loss': loss} ) # ... ``` _See documentation [here](https://
-aimstack.readthedocs.io/en/latest/quick_start/integrations.html#integration-
-with-pytorch-ignite)._  # Comparisons to familiar tools ### Tensorboard
-**Training run comparison** Order of magnitude faster training run comparison
-with Aim - The tracked params are first class citizens at Aim. You can search,
-group, aggregate via params - deeply explore all the tracked data (metrics,
-params, images) on the UI. - With tensorboard the users are forced to record
-those parameters in the training run name to be able to search and compare.
-This causes a super-tedius comparison experience and usability issues on the UI
-when there are many experiments and params. **TensorBoard doesn't have features
-to group, aggregate the metrics** **Scalability** - Aim is built to handle
-1000s of training runs - both on the backend and on the UI. - TensorBoard
-becomes really slow and hard to use when a few hundred training runs are
-queried / compared. **Beloved TB visualizations to be added on Aim** -
-Embedding projector. - Neural network visualization. ### MLFlow MLFlow is an
-end-to-end ML Lifecycle tool. Aim is focused on training tracking. The main
+with-fastai) - [Integration with MXNet](https://aimstack.readthedocs.io/en/
+latest/quick_start/integrations.html#integration-with-mxnet) - [Integration
+with Optuna](https://aimstack.readthedocs.io/en/latest/quick_start/
+integrations.html#integration-with-optuna) - [Integration with PaddlePaddle]
+(https://aimstack.readthedocs.io/en/latest/quick_start/
+integrations.html#integration-with-paddlepaddle) - [Integration with Stable-
+Baselines3](https://aimstack.readthedocs.io/en/latest/quick_start/
+integrations.html#integration-with-stable-baselines3) - [Integration with Acme]
+(https://aimstack.readthedocs.io/en/latest/quick_start/
+integrations.html#integration-with-acme) - [Integration with Prophet](https://
+aimstack.readthedocs.io/en/latest/quick_start/integrations.html#integration-
+with-prophet)    Query runs programmatically via SDK   Aim Python SDK empowers
+you to query and access any piece of tracked metadata with ease. ```python from
+aim import Repo my_repo = Repo('/path/to/aim/repo') query = "metric.name ==
+'loss'" # Example query # Get collection of metrics for run_metrics_collection
+in my_repo.query_metrics(query).iter_runs(): for metric in
+run_metrics_collection: # Get run params params = metric.run[...] # Get metric
+values steps, metric_values = metric.values.sparse_numpy() ```    Set up a
+centralized tracking server   Aim remote tracking server allows running
+experiments in a multi-host environment and collect tracked data in a
+centralized location. See the docs on how to [set up the remote server](https:/
+/aimstack.readthedocs.io/en/latest/using/remote_tracking.html).    Deploy Aim
+on kubernetes   - The official Aim docker image: https://hub.docker.com/r/
+aimstack/aim - A guide on how to deploy Aim on kubernetes: https://
+aimstack.readthedocs.io/en/latest/using/k8s_deployment.html  Read the full
+documentation on [aimstack.readthedocs.io](https://aimstack.readthedocs.io)
+ð # ð Comparisons to familiar tools   TensorBoard vs Aim   **Training run
+comparison** Order of magnitude faster training run comparison with Aim - The
+tracked params are first class citizens at Aim. You can search, group,
+aggregate via params - deeply explore all the tracked data (metrics, params,
+images) on the UI. - With tensorboard the users are forced to record those
+parameters in the training run name to be able to search and compare. This
+causes a super-tedius comparison experience and usability issues on the UI when
+there are many experiments and params. **TensorBoard doesn't have features to
+group, aggregate the metrics** **Scalability** - Aim is built to handle 1000s
+of training runs - both on the backend and on the UI. - TensorBoard becomes
+really slow and hard to use when a few hundred training runs are queried /
+compared. **Beloved TB visualizations to be added on Aim** - Embedding
+projector. - Neural network visualization.    MLflow vs Aim   MLFlow is an end-
+to-end ML Lifecycle tool. Aim is focused on training tracking. The main
 differences of Aim and MLflow are around the UI scalability and run comparison
-features. **Run comparison** - Aim treats tracked parameters as first-class
+features. Aim and MLflow are a perfect match - check out the [aimlflow](https:/
+/github.com/aimhubio/aimlflow) - the tool that enables Aim supoerpowers on
+Mlflow. **Run comparison** - Aim treats tracked parameters as first-class
 citizens. Users can query runs, metrics, images and filter using the params. -
 MLFlow does have a search by tracked config, but there are no grouping,
 aggregation, subplotting by hyparparams and other comparison features
 available. **UI Scalability** - Aim UI can handle several thousands of metrics
 at the same time smoothly with 1000s of steps. It may get shaky when you
 explore 1000s of metrics with 10000s of steps each. But we are constantly
 optimizing! - MLflow UI becomes slow to use when there are a few hundreds of
-runs. ### Weights and Biases Hosted vs self-hosted - Weights and Biases is a
-hosted closed-source MLOps platform. - Aim is self-hosted, free and open-source
-experiment tracking tool. # Roadmap ## Detailed Sprints :sparkle: The [Aim
-product roadmap](https://github.com/orgs/aimhubio/projects/3) - The `Backlog`
-contains the issues we are going to choose from and prioritize weekly - The
-issues are mainly prioritized by the highly-requested features ## High-level
-roadmap The high-level features we are going to work on the next few months ###
-Done - [x] Live updates (Shipped: _Oct 18 2021_) - [x] Images tracking and
-visualization (Start: _Oct 18 2021_, Shipped: _Nov 19 2021_) - [x]
-Distributions tracking and visualization (Start: _Nov 10 2021_, Shipped: _Dec 3
-2021_) - [x] Jupyter integration (Start: _Nov 18 2021_, Shipped: _Dec 3 2021_)
-- [x] Audio tracking and visualization (Start: _Dec 6 2021_, Shipped: _Dec 17
-2021_) - [x] Transcripts tracking and visualization (Start: _Dec 6 2021_,
-Shipped: _Dec 17 2021_) - [x] Plotly integration (Start: _Dec 1 2021_, Shipped:
-_Dec 17 2021_) - [x] Colab integration (Start: _Nov 18 2021_, Shipped: _Dec 17
-2021_) - [x] Centralized tracking server (Start: _Oct 18 2021_, Shipped: _Jan
-22 2022_) - [x] Tensorboard adaptor - visualize TensorBoard logs with Aim
-(Start: _Dec 17 2021_, Shipped: _Feb 3 2022_) - [x] Track git info, env vars,
-CLI arguments, dependencies (Start: _Jan 17 2022_, Shipped: _Feb 3 2022_) - [x]
-MLFlow adaptor (visualize MLflow logs with Aim) (Start: _Feb 14 2022_, Shipped:
-_Feb 22 2022_) - [x] Activeloop Hub integration (Start: _Feb 14 2022_, Shipped:
-_Feb 22 2022_) - [x] PyTorch-Ignite integration (Start: _Feb 14 2022_, Shipped:
-_Feb 22 2022_) - [x] Run summary and overview info(system params, CLI args, git
-info, ...) (Start: _Feb 14 2022_, Shipped: _Mar 9 2022_) - [x] Add DVC related
-metadata into aim run (Start: _Mar 7 2022_, Shipped: _Mar 26 2022_) - [x]
-Ability to attach notes to Run from UI (Start: _Mar 7 2022_, Shipped: _Apr 29
-2022_) - [x] Fairseq integration (Start: _Mar 27 2022_, Shipped: _Mar 29 2022_)
-- [x] LightGBM integration (Start: _Apr 14 2022_, Shipped: _May 17 2022_) - [x]
+runs.    Weights and Biases vs Aim   Hosted vs self-hosted - Weights and Biases
+is a hosted closed-source MLOps platform. - Aim is self-hosted, free and open-
+source experiment tracking tool.  # ð£ï¸ Roadmap ## Detailed milestones The
+[Aim product roadmap](https://github.com/orgs/aimhubio/projects/3) :sparkle: -
+The `Backlog` contains the issues we are going to choose from and prioritize
+weekly - The issues are mainly prioritized by the highly-requested features ##
+High-level roadmap The high-level features we are going to work on the next few
+months: **In progress** - [ ] Aim SDK low-level interface - [ ] Dashboards â
+customizable layouts with embedded explorers - [ ] Ergonomic UI kit - [ ] Text
+Explorer   Next-up   **Aim UI** - Runs management - Runs explorer â query and
+visualize runs data(images, audio, distributions, ...) in a central dashboard -
+Explorers - Distributions Explorer **SDK and Storage** - Scalability - Smooth
+UI and SDK experience with over 10.000 runs - Runs management - CLI commands -
+Reporting - runs summary and run details in a CLI compatible format -
+Manipulations â copy, move, delete runs, params and sequences - Cloud storage
+support â store runs blob(e.g. images) data on the cloud - Artifact storage
+â store files, model checkpoints, and beyond **Integrations** - ML
+Frameworks: - Shortlist: scikit-learn - Resource management tools - Shortlist:
+Kubeflow, Slurm - Workflow orchestration tools    Done   - [x] Live updates
+(Shipped: _Oct 18 2021_) - [x] Images tracking and visualization (Start: _Oct
+18 2021_, Shipped: _Nov 19 2021_) - [x] Distributions tracking and
+visualization (Start: _Nov 10 2021_, Shipped: _Dec 3 2021_) - [x] Jupyter
+integration (Start: _Nov 18 2021_, Shipped: _Dec 3 2021_) - [x] Audio tracking
+and visualization (Start: _Dec 6 2021_, Shipped: _Dec 17 2021_) - [x]
+Transcripts tracking and visualization (Start: _Dec 6 2021_, Shipped: _Dec 17
+2021_) - [x] Plotly integration (Start: _Dec 1 2021_, Shipped: _Dec 17 2021_) -
+[x] Colab integration (Start: _Nov 18 2021_, Shipped: _Dec 17 2021_) - [x]
+Centralized tracking server (Start: _Oct 18 2021_, Shipped: _Jan 22 2022_) -
+[x] Tensorboard adaptor - visualize TensorBoard logs with Aim (Start: _Dec 17
+2021_, Shipped: _Feb 3 2022_) - [x] Track git info, env vars, CLI arguments,
+dependencies (Start: _Jan 17 2022_, Shipped: _Feb 3 2022_) - [x] MLFlow adaptor
+(visualize MLflow logs with Aim) (Start: _Feb 14 2022_, Shipped: _Feb 22 2022_)
+- [x] Activeloop Hub integration (Start: _Feb 14 2022_, Shipped: _Feb 22 2022_)
+- [x] PyTorch-Ignite integration (Start: _Feb 14 2022_, Shipped: _Feb 22 2022_)
+- [x] Run summary and overview info(system params, CLI args, git info, ...)
+(Start: _Feb 14 2022_, Shipped: _Mar 9 2022_) - [x] Add DVC related metadata
+into aim run (Start: _Mar 7 2022_, Shipped: _Mar 26 2022_) - [x] Ability to
+attach notes to Run from UI (Start: _Mar 7 2022_, Shipped: _Apr 29 2022_) - [x]
+Fairseq integration (Start: _Mar 27 2022_, Shipped: _Mar 29 2022_) - [x]
+LightGBM integration (Start: _Apr 14 2022_, Shipped: _May 17 2022_) - [x]
 CatBoost integration (Start: _Apr 20 2022_, Shipped: _May 17 2022_) - [x] Run
 execution details(display stdout/stderr logs) (Start: _Apr 25 2022_, Shipped:
 _May 17 2022_) - [x] Long sequences(up to 5M of steps) support (Start: _Apr 25
 2022_, Shipped: _Jun 22 2022_) - [x] Figures Explorer (Start: _Mar 1 2022_,
 Shipped: _Aug 21 2022_) - [x] Notify on stuck runs (Start: _Jul 22 2022_,
 Shipped: _Aug 21 2022_) - [x] Integration with KerasTuner (Start: _Aug 10
 2022_, Shipped: _Aug 21 2022_) - [x] Integration with WandB (Start: _Aug 15
@@ -222,25 +273,26 @@
 22 2022_, Shipped: _Oct 6 2022_) - [x] Integration with MXNet (Start: _Sep 20
 2022_, Shipped: _Oct 6 2022_) - [x] Project overview page (Start: _Sep 1 2022_,
 Shipped: _Oct 6 2022_) - [x] Remote tracking server scaling (Start: _Sep 11
 2022_, Shipped: _Nov 26 2022_) - [x] Integration with PaddlePaddle (Start: _Oct
 2 2022_, Shipped: _Nov 26 2022_) - [x] Integration with Optuna (Start: _Oct 2
 2022_, Shipped: _Nov 26 2022_) - [x] Audios Explorer (Start: _Oct 30 2022_,
 Shipped: _Nov 26 2022_) - [x] Experiment page (Start: _Nov 9 2022_, Shipped:
-_Nov 26 2022_) ### In Progress - [ ] Aim SDK low-level interface (Start: _Aug
-22 2022_, ) - [ ] HuggingFace datasets (Start: _Dec 29 2022_, ) ### To Do **Aim
-UI** - Runs management - Runs explorer â query and visualize runs data
-(images, audio, distributions, ...) in a central dashboard - Explorers - Text
-Explorer - Distributions Explorer - Dashboards â customizable layouts with
-embedded explorers **SDK and Storage** - Scalability - Smooth UI and SDK
-experience with over 10.000 runs - Runs management - CLI interfaces - Reporting
-- runs summary and run details in a CLI compatible format - Manipulations â
-copy, move, delete runs, params and sequences **Integrations** - ML Frameworks:
-- Shortlist: MONAI, SpaCy, Raytune - Resource management tools - Shortlist:
-Kubeflow, Slurm - Workflow orchestration tools - Others: Hydra, Google MLMD,
-Streamlit, ... ### On hold - scikit-learn integration - Cloud storage support
-â store runs blob(e.g. images) data on the cloud (Start: _Mar 21 2022_) -
-Artifact storage â store files, model checkpoints, and beyond (Start: _Mar 21
-2022_) ## Community ### If you have questions 1. [Read the docs](https://
-aimstack.readthedocs.io/en/latest/) 2. [Open a feature request or report a bug]
-(https://github.com/aimhubio/aim/issues) 3. [Join Discord community server]
-(https://community.aimstack.io/)
+_Nov 26 2022_) - [x] HuggingFace datasets (Start: _Dec 29 2022_, _Feb 3 2023_)
+# ð¥ Community ## Aim README badge Add Aim badge to your README, if you've
+enjoyed using Aim in your work: [![Aim](https://img.shields.io/badge/
+powered%20by-Aim-%231473E6)](https://github.com/aimhubio/aim) ``` [![Aim]
+(https://img.shields.io/badge/powered%20by-Aim-%231473E6)](https://github.com/
+aimhubio/aim) ``` ## Cite Aim in your papers In case you've found Aim helpful
+in your research journey, we'd be thrilled if you could acknowledge Aim's
+contribution: ```bibtex @software{Arakelyan_Aim_2020, author = {Arakelyan, Gor
+and Soghomonyan, Gevorg and {The Aim team}}, doi = {10.5281/zenodo.6536395},
+license = {Apache-2.0}, month = {6}, title = {{Aim}}, url = {https://
+github.com/aimhubio/aim}, version = {3.9.3}, year = {2020} } ``` ##
+Contributing to Aim Considering contibuting to Aim? To get started, please take
+a moment to read the [CONTRIBUTING.md](https://github.com/aimhubio/aim/blob/
+main/CONTRIBUTING.md) guide. Join Aim contributors by submitting your first
+pull request. Happy coding! ð [https://contrib.rocks/image?repo=aimhubio/
+aim] Made with [contrib.rocks](https://contrib.rocks). ## More questions? 1.
+[Read the docs](https://aimstack.readthedocs.io/en/latest/) 2. [Open a feature
+request or report a bug](https://github.com/aimhubio/aim/issues) 3. [Join
+Discord community server](https://community.aimstack.io/)
```

### Comparing `aim-4.0.0.dev1/aim.egg-info/SOURCES.txt` & `aim-4.0.0.dev2/aim.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `aim-4.0.0.dev1/performance_tests/sdk/test_data_collection.py` & `aim-4.0.0.dev2/performance_tests/sdk/test_data_collection.py`

 * *Files identical despite different names*

### Comparing `aim-4.0.0.dev1/performance_tests/sdk/test_query.py` & `aim-4.0.0.dev2/performance_tests/sdk/test_query.py`

 * *Files identical despite different names*

### Comparing `aim-4.0.0.dev1/performance_tests/sdk/utils.py` & `aim-4.0.0.dev2/performance_tests/sdk/utils.py`

 * *Files identical despite different names*

### Comparing `aim-4.0.0.dev1/performance_tests/storage/test_container_open.py` & `aim-4.0.0.dev2/performance_tests/storage/test_container_open.py`

 * *Files identical despite different names*

### Comparing `aim-4.0.0.dev1/performance_tests/storage/test_iterative_access.py` & `aim-4.0.0.dev2/performance_tests/storage/test_iterative_access.py`

 * *Files identical despite different names*

### Comparing `aim-4.0.0.dev1/performance_tests/storage/test_random_access.py` & `aim-4.0.0.dev2/performance_tests/storage/test_random_access.py`

 * *Files identical despite different names*

### Comparing `aim-4.0.0.dev1/performance_tests/storage/utils.py` & `aim-4.0.0.dev2/performance_tests/storage/utils.py`

 * *Files identical despite different names*

### Comparing `aim-4.0.0.dev1/setup.py` & `aim-4.0.0.dev2/setup.py`

 * *Files identical despite different names*

### Comparing `aim-4.0.0.dev1/tests/api/test_dashboards_api.py` & `aim-4.0.0.dev2/tests/api/test_dashboards_api.py`

 * *Files identical despite different names*

### Comparing `aim-4.0.0.dev1/tests/api/test_project_api.py` & `aim-4.0.0.dev2/tests/api/test_project_api.py`

 * *Files identical despite different names*

### Comparing `aim-4.0.0.dev1/tests/api/test_run_api.py` & `aim-4.0.0.dev2/tests/api/test_run_api.py`

 * *Files identical despite different names*

### Comparing `aim-4.0.0.dev1/tests/api/test_run_images_api.py` & `aim-4.0.0.dev2/tests/api/test_run_images_api.py`

 * *Files identical despite different names*

### Comparing `aim-4.0.0.dev1/tests/api/test_structured_data_api.py` & `aim-4.0.0.dev2/tests/api/test_structured_data_api.py`

 * *Files identical despite different names*

### Comparing `aim-4.0.0.dev1/tests/integrations/test_dvc_metadata.py` & `aim-4.0.0.dev2/tests/integrations/test_dvc_metadata.py`

 * *Files identical despite different names*

### Comparing `aim-4.0.0.dev1/tests/integrations/test_hf_datasets.py` & `aim-4.0.0.dev2/tests/integrations/test_hf_datasets.py`

 * *Files identical despite different names*

### Comparing `aim-4.0.0.dev1/tests/integrations/test_hub_dataset.py` & `aim-4.0.0.dev2/tests/integrations/test_hub_dataset.py`

 * *Files identical despite different names*

### Comparing `aim-4.0.0.dev1/tests/sdk/test_image_construction.py` & `aim-4.0.0.dev2/tests/sdk/test_image_construction.py`

 * *Files identical despite different names*

### Comparing `aim-4.0.0.dev1/tests/sdk/test_resource_tracker.py` & `aim-4.0.0.dev2/tests/sdk/test_resource_tracker.py`

 * *Files identical despite different names*

### Comparing `aim-4.0.0.dev1/tests/sdk/test_run_apis.py` & `aim-4.0.0.dev2/tests/sdk/test_run_apis.py`

 * *Files identical despite different names*

### Comparing `aim-4.0.0.dev1/tests/sdk/test_run_creation_checks.py` & `aim-4.0.0.dev2/tests/sdk/test_run_creation_checks.py`

 * *Files identical despite different names*

### Comparing `aim-4.0.0.dev1/tests/sdk/test_run_finalization_time.py` & `aim-4.0.0.dev2/tests/sdk/test_run_finalization_time.py`

 * *Files identical despite different names*

### Comparing `aim-4.0.0.dev1/tests/sdk/test_run_metric_types.py` & `aim-4.0.0.dev2/tests/sdk/test_run_metric_types.py`

 * *Files identical despite different names*

### Comparing `aim-4.0.0.dev1/tests/sdk/test_run_track_type_checking.py` & `aim-4.0.0.dev2/tests/sdk/test_run_track_type_checking.py`

 * *Files identical despite different names*

### Comparing `aim-4.0.0.dev1/tests/sdk/test_run_write_container_data.py` & `aim-4.0.0.dev2/tests/sdk/test_run_write_container_data.py`

 * *Files identical despite different names*

### Comparing `aim-4.0.0.dev1/tests/sdk/test_utils.py` & `aim-4.0.0.dev2/tests/sdk/test_utils.py`

 * *Files identical despite different names*

### Comparing `aim-4.0.0.dev1/tests/storage/test_query.py` & `aim-4.0.0.dev2/tests/storage/test_query.py`

 * *Files identical despite different names*

### Comparing `aim-4.0.0.dev1/tests/storage/test_query_with_epoch_none.py` & `aim-4.0.0.dev2/tests/storage/test_query_with_epoch_none.py`

 * *Files identical despite different names*

### Comparing `aim-4.0.0.dev1/tests/storage/test_structured_db.py` & `aim-4.0.0.dev2/tests/storage/test_structured_db.py`

 * *Files identical despite different names*

