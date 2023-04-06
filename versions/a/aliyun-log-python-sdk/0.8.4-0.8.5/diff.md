# Comparing `tmp/aliyun-log-python-sdk-0.8.4.tar.gz` & `tmp/aliyun-log-python-sdk-0.8.5.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "aliyun-log-python-sdk-0.8.4.tar", last modified: Wed Mar 29 08:27:23 2023, max compression
+gzip compressed data, was "aliyun-log-python-sdk-0.8.5.tar", last modified: Thu Apr  6 08:57:32 2023, max compression
```

## Comparing `aliyun-log-python-sdk-0.8.4.tar` & `aliyun-log-python-sdk-0.8.5.tar`

### file list

```diff
@@ -1,128 +1,128 @@
-drwxr-xr-x   0 zhhfan     (502) staff       (20)        0 2023-03-29 08:27:23.474049 aliyun-log-python-sdk-0.8.4/
--rw-r--r--   0 zhhfan     (502) staff       (20)     1070 2023-03-29 01:29:33.000000 aliyun-log-python-sdk-0.8.4/LICENSE
--rw-r--r--   0 zhhfan     (502) staff       (20)      863 2023-03-29 08:27:23.473580 aliyun-log-python-sdk-0.8.4/PKG-INFO
--rwxr-xr-x   0 zhhfan     (502) staff       (20)     2677 2023-03-29 01:29:33.000000 aliyun-log-python-sdk-0.8.4/README.md
-drwxr-xr-x   0 zhhfan     (502) staff       (20)        0 2023-03-29 08:27:23.405718 aliyun-log-python-sdk-0.8.4/aliyun/
--rwxr-xr-x   0 zhhfan     (502) staff       (20)        0 2023-03-29 01:29:33.000000 aliyun-log-python-sdk-0.8.4/aliyun/__init__.py
-drwxr-xr-x   0 zhhfan     (502) staff       (20)        0 2023-03-29 08:27:23.444234 aliyun-log-python-sdk-0.8.4/aliyun/log/
--rwxr-xr-x   0 zhhfan     (502) staff       (20)     1648 2023-03-29 01:29:33.000000 aliyun-log-python-sdk-0.8.4/aliyun/log/__init__.py
--rwxr-xr-x   0 zhhfan     (502) staff       (20)      879 2023-03-29 01:29:33.000000 aliyun-log-python-sdk-0.8.4/aliyun/log/acl_config.py
--rwxr-xr-x   0 zhhfan     (502) staff       (20)     1629 2023-03-29 01:29:33.000000 aliyun-log-python-sdk-0.8.4/aliyun/log/acl_response.py
--rw-r--r--   0 zhhfan     (502) staff       (20)     6712 2023-03-29 01:29:33.000000 aliyun-log-python-sdk-0.8.4/aliyun/log/auth.py
--rw-r--r--   0 zhhfan     (502) staff       (20)     2784 2023-03-29 01:29:33.000000 aliyun-log-python-sdk-0.8.4/aliyun/log/common_response.py
-drwxr-xr-x   0 zhhfan     (502) staff       (20)        0 2023-03-29 08:27:23.449091 aliyun-log-python-sdk-0.8.4/aliyun/log/consumer/
--rwxr-xr-x   0 zhhfan     (502) staff       (20)      152 2023-03-29 01:29:33.000000 aliyun-log-python-sdk-0.8.4/aliyun/log/consumer/__init__.py
--rwxr-xr-x   0 zhhfan     (502) staff       (20)     2319 2023-03-29 01:29:33.000000 aliyun-log-python-sdk-0.8.4/aliyun/log/consumer/checkpoint_tracker.py
--rwxr-xr-x   0 zhhfan     (502) staff       (20)     4379 2023-03-29 01:29:33.000000 aliyun-log-python-sdk-0.8.4/aliyun/log/consumer/config.py
--rwxr-xr-x   0 zhhfan     (502) staff       (20)     4577 2023-03-29 01:29:33.000000 aliyun-log-python-sdk-0.8.4/aliyun/log/consumer/consumer_client.py
--rw-r--r--   0 zhhfan     (502) staff       (20)      531 2023-03-29 01:29:33.000000 aliyun-log-python-sdk-0.8.4/aliyun/log/consumer/exceptions.py
--rwxr-xr-x   0 zhhfan     (502) staff       (20)      590 2023-03-29 01:29:33.000000 aliyun-log-python-sdk-0.8.4/aliyun/log/consumer/fetched_log_group.py
--rwxr-xr-x   0 zhhfan     (502) staff       (20)     4159 2023-03-29 01:29:33.000000 aliyun-log-python-sdk-0.8.4/aliyun/log/consumer/heart_beat.py
--rwxr-xr-x   0 zhhfan     (502) staff       (20)    11472 2023-03-29 01:29:33.000000 aliyun-log-python-sdk-0.8.4/aliyun/log/consumer/shard_worker.py
--rwxr-xr-x   0 zhhfan     (502) staff       (20)     7454 2023-03-29 01:29:33.000000 aliyun-log-python-sdk-0.8.4/aliyun/log/consumer/tasks.py
--rwxr-xr-x   0 zhhfan     (502) staff       (20)     8589 2023-03-29 01:29:33.000000 aliyun-log-python-sdk-0.8.4/aliyun/log/consumer/worker.py
--rwxr-xr-x   0 zhhfan     (502) staff       (20)     3285 2023-03-29 01:29:33.000000 aliyun-log-python-sdk-0.8.4/aliyun/log/consumer_group_request.py
--rwxr-xr-x   0 zhhfan     (502) staff       (20)     5252 2023-03-29 01:29:33.000000 aliyun-log-python-sdk-0.8.4/aliyun/log/consumer_group_response.py
--rwxr-xr-x   0 zhhfan     (502) staff       (20)      813 2023-03-29 01:29:33.000000 aliyun-log-python-sdk-0.8.4/aliyun/log/cursor_response.py
--rwxr-xr-x   0 zhhfan     (502) staff       (20)      808 2023-03-29 01:29:33.000000 aliyun-log-python-sdk-0.8.4/aliyun/log/cursor_time_response.py
-drwxr-xr-x   0 zhhfan     (502) staff       (20)        0 2023-03-29 08:27:23.454327 aliyun-log-python-sdk-0.8.4/aliyun/log/es_migration/
--rw-r--r--   0 zhhfan     (502) staff       (20)      171 2023-03-29 01:29:33.000000 aliyun-log-python-sdk-0.8.4/aliyun/log/es_migration/__init__.py
--rw-r--r--   0 zhhfan     (502) staff       (20)     1690 2023-03-29 01:29:33.000000 aliyun-log-python-sdk-0.8.4/aliyun/log/es_migration/doc_logitem_converter.py
--rw-r--r--   0 zhhfan     (502) staff       (20)     2583 2023-03-29 01:29:33.000000 aliyun-log-python-sdk-0.8.4/aliyun/log/es_migration/index_logstore_mappings.py
--rw-r--r--   0 zhhfan     (502) staff       (20)    11037 2023-03-29 01:29:33.000000 aliyun-log-python-sdk-0.8.4/aliyun/log/es_migration/mapping_index_converter.py
--rw-r--r--   0 zhhfan     (502) staff       (20)     2347 2023-03-29 01:29:33.000000 aliyun-log-python-sdk-0.8.4/aliyun/log/es_migration/migration_log.py
--rw-r--r--   0 zhhfan     (502) staff       (20)    16932 2023-03-29 01:29:33.000000 aliyun-log-python-sdk-0.8.4/aliyun/log/es_migration/migration_manager.py
--rw-r--r--   0 zhhfan     (502) staff       (20)      281 2023-03-29 01:29:33.000000 aliyun-log-python-sdk-0.8.4/aliyun/log/es_migration/migration_response.py
--rw-r--r--   0 zhhfan     (502) staff       (20)     8326 2023-03-29 01:29:33.000000 aliyun-log-python-sdk-0.8.4/aliyun/log/es_migration/migration_task.py
--rwxr-xr-x   0 zhhfan     (502) staff       (20)      194 2023-03-29 01:29:33.000000 aliyun-log-python-sdk-0.8.4/aliyun/log/es_migration/util.py
--rw-r--r--   0 zhhfan     (502) staff       (20)     4373 2023-03-29 01:29:33.000000 aliyun-log-python-sdk-0.8.4/aliyun/log/etl_config_response.py
-drwxr-xr-x   0 zhhfan     (502) staff       (20)        0 2023-03-29 08:27:23.458530 aliyun-log-python-sdk-0.8.4/aliyun/log/etl_core/
--rw-r--r--   0 zhhfan     (502) staff       (20)      128 2023-03-29 01:29:33.000000 aliyun-log-python-sdk-0.8.4/aliyun/log/etl_core/__init__.py
--rw-r--r--   0 zhhfan     (502) staff       (20)     2301 2023-03-29 01:29:33.000000 aliyun-log-python-sdk-0.8.4/aliyun/log/etl_core/config_parser.py
--rw-r--r--   0 zhhfan     (502) staff       (20)     5370 2023-03-29 01:29:33.000000 aliyun-log-python-sdk-0.8.4/aliyun/log/etl_core/etl_util.py
--rw-r--r--   0 zhhfan     (502) staff       (20)      450 2023-03-29 01:29:33.000000 aliyun-log-python-sdk-0.8.4/aliyun/log/etl_core/exceptions.py
--rw-r--r--   0 zhhfan     (502) staff       (20)     2723 2023-03-29 01:29:33.000000 aliyun-log-python-sdk-0.8.4/aliyun/log/etl_core/restrict_config_parser.py
--rw-r--r--   0 zhhfan     (502) staff       (20)     1245 2023-03-29 01:29:33.000000 aliyun-log-python-sdk-0.8.4/aliyun/log/etl_core/runner.py
--rw-r--r--   0 zhhfan     (502) staff       (20)     1422 2023-03-29 01:29:33.000000 aliyun-log-python-sdk-0.8.4/aliyun/log/etl_core/settings.py
-drwxr-xr-x   0 zhhfan     (502) staff       (20)        0 2023-03-29 08:27:23.464298 aliyun-log-python-sdk-0.8.4/aliyun/log/etl_core/trans_comp/
--rw-r--r--   0 zhhfan     (502) staff       (20)      500 2023-03-29 01:29:33.000000 aliyun-log-python-sdk-0.8.4/aliyun/log/etl_core/trans_comp/__init__.py
--rw-r--r--   0 zhhfan     (502) staff       (20)     2523 2023-03-29 01:29:33.000000 aliyun-log-python-sdk-0.8.4/aliyun/log/etl_core/trans_comp/trans_base.py
--rw-r--r--   0 zhhfan     (502) staff       (20)     2031 2023-03-29 01:29:33.000000 aliyun-log-python-sdk-0.8.4/aliyun/log/etl_core/trans_comp/trans_csv.py
--rw-r--r--   0 zhhfan     (502) staff       (20)    14656 2023-03-29 01:29:33.000000 aliyun-log-python-sdk-0.8.4/aliyun/log/etl_core/trans_comp/trans_json.py
--rw-r--r--   0 zhhfan     (502) staff       (20)     3649 2023-03-29 01:29:33.000000 aliyun-log-python-sdk-0.8.4/aliyun/log/etl_core/trans_comp/trans_kv.py
--rw-r--r--   0 zhhfan     (502) staff       (20)     9141 2023-03-29 01:29:33.000000 aliyun-log-python-sdk-0.8.4/aliyun/log/etl_core/trans_comp/trans_lookup.py
--rw-r--r--   0 zhhfan     (502) staff       (20)     4051 2023-03-29 01:29:33.000000 aliyun-log-python-sdk-0.8.4/aliyun/log/etl_core/trans_comp/trans_mv.py
--rw-r--r--   0 zhhfan     (502) staff       (20)     5215 2023-03-29 01:29:33.000000 aliyun-log-python-sdk-0.8.4/aliyun/log/etl_core/trans_comp/trans_regex.py
--rw-r--r--   0 zhhfan     (502) staff       (20)     3704 2023-03-29 01:29:33.000000 aliyun-log-python-sdk-0.8.4/aliyun/log/etl_core/trans_comp/trans_set_field.py
-drwxr-xr-x   0 zhhfan     (502) staff       (20)        0 2023-03-29 08:27:23.468915 aliyun-log-python-sdk-0.8.4/aliyun/log/etl_core/transform/
--rw-r--r--   0 zhhfan     (502) staff       (20)      156 2023-03-29 01:29:33.000000 aliyun-log-python-sdk-0.8.4/aliyun/log/etl_core/transform/__init__.py
--rw-r--r--   0 zhhfan     (502) staff       (20)     4419 2023-03-29 01:29:33.000000 aliyun-log-python-sdk-0.8.4/aliyun/log/etl_core/transform/condition_list.py
--rw-r--r--   0 zhhfan     (502) staff       (20)     1923 2023-03-29 01:29:33.000000 aliyun-log-python-sdk-0.8.4/aliyun/log/etl_core/transform/condition_transform.py
--rw-r--r--   0 zhhfan     (502) staff       (20)      903 2023-03-29 01:29:33.000000 aliyun-log-python-sdk-0.8.4/aliyun/log/etl_core/transform/condition_util.py
--rw-r--r--   0 zhhfan     (502) staff       (20)      145 2023-03-29 01:29:33.000000 aliyun-log-python-sdk-0.8.4/aliyun/log/etl_core/transform/transform_base.py
--rw-r--r--   0 zhhfan     (502) staff       (20)     2126 2023-03-29 01:29:33.000000 aliyun-log-python-sdk-0.8.4/aliyun/log/etl_core/transform/transform_list.py
--rw-r--r--   0 zhhfan     (502) staff       (20)     3680 2023-03-29 01:29:33.000000 aliyun-log-python-sdk-0.8.4/aliyun/log/etl_core/transform/transform_meta.py
--rw-r--r--   0 zhhfan     (502) staff       (20)     2764 2023-03-29 01:29:33.000000 aliyun-log-python-sdk-0.8.4/aliyun/log/export_response.py
-drwxr-xr-x   0 zhhfan     (502) staff       (20)        0 2023-03-29 08:27:23.470535 aliyun-log-python-sdk-0.8.4/aliyun/log/ext/
--rwxr-xr-x   0 zhhfan     (502) staff       (20)        0 2023-03-29 01:29:33.000000 aliyun-log-python-sdk-0.8.4/aliyun/log/ext/__init__.py
--rw-r--r--   0 zhhfan     (502) staff       (20)    13130 2023-03-29 01:29:33.000000 aliyun-log-python-sdk-0.8.4/aliyun/log/ext/jupyter_magic.py
--rw-r--r--   0 zhhfan     (502) staff       (20)     7247 2023-03-29 01:29:33.000000 aliyun-log-python-sdk-0.8.4/aliyun/log/ext/syslogclient.py
--rw-r--r--   0 zhhfan     (502) staff       (20)     7849 2023-03-29 01:29:34.000000 aliyun-log-python-sdk-0.8.4/aliyun/log/external_store_config.py
--rw-r--r--   0 zhhfan     (502) staff       (20)     4315 2023-03-29 01:29:34.000000 aliyun-log-python-sdk-0.8.4/aliyun/log/external_store_config_response.py
--rw-r--r--   0 zhhfan     (502) staff       (20)     2931 2023-03-29 01:29:34.000000 aliyun-log-python-sdk-0.8.4/aliyun/log/getcontextlogsresponse.py
--rwxr-xr-x   0 zhhfan     (502) staff       (20)     3400 2023-03-29 01:29:34.000000 aliyun-log-python-sdk-0.8.4/aliyun/log/gethistogramsrequest.py
--rwxr-xr-x   0 zhhfan     (502) staff       (20)     1922 2023-03-29 01:29:34.000000 aliyun-log-python-sdk-0.8.4/aliyun/log/gethistogramsresponse.py
--rwxr-xr-x   0 zhhfan     (502) staff       (20)     6186 2023-03-29 01:29:34.000000 aliyun-log-python-sdk-0.8.4/aliyun/log/getlogsrequest.py
--rwxr-xr-x   0 zhhfan     (502) staff       (20)     4460 2023-03-29 01:29:34.000000 aliyun-log-python-sdk-0.8.4/aliyun/log/getlogsresponse.py
--rwxr-xr-x   0 zhhfan     (502) staff       (20)     1733 2023-03-29 01:29:34.000000 aliyun-log-python-sdk-0.8.4/aliyun/log/histogram.py
--rwxr-xr-x   0 zhhfan     (502) staff       (20)    10335 2023-03-29 01:29:34.000000 aliyun-log-python-sdk-0.8.4/aliyun/log/index_config.py
--rwxr-xr-x   0 zhhfan     (502) staff       (20)     2220 2023-03-29 01:29:34.000000 aliyun-log-python-sdk-0.8.4/aliyun/log/index_config_response.py
--rw-r--r--   0 zhhfan     (502) staff       (20)     5180 2023-03-29 01:29:34.000000 aliyun-log-python-sdk-0.8.4/aliyun/log/ingestion_response.py
--rw-r--r--   0 zhhfan     (502) staff       (20)     6360 2023-03-29 01:29:34.000000 aliyun-log-python-sdk-0.8.4/aliyun/log/job.py
--rwxr-xr-x   0 zhhfan     (502) staff       (20)      407 2023-03-29 01:29:34.000000 aliyun-log-python-sdk-0.8.4/aliyun/log/listlogstoresrequest.py
--rwxr-xr-x   0 zhhfan     (502) staff       (20)     1902 2023-03-29 01:29:34.000000 aliyun-log-python-sdk-0.8.4/aliyun/log/listlogstoresresponse.py
--rwxr-xr-x   0 zhhfan     (502) staff       (20)     1897 2023-03-29 01:29:34.000000 aliyun-log-python-sdk-0.8.4/aliyun/log/listtopicsrequest.py
--rwxr-xr-x   0 zhhfan     (502) staff       (20)     1570 2023-03-29 01:29:34.000000 aliyun-log-python-sdk-0.8.4/aliyun/log/listtopicsresponse.py
--rwxr-xr-x   0 zhhfan     (502) staff       (20)     8952 2023-03-29 01:29:34.000000 aliyun-log-python-sdk-0.8.4/aliyun/log/log_logs_pb2.py
--rw-r--r--   0 zhhfan     (502) staff       (20)     9641 2023-03-29 01:29:34.000000 aliyun-log-python-sdk-0.8.4/aliyun/log/log_logs_raw_pb2.py
--rw-r--r--   0 zhhfan     (502) staff       (20)   203644 2023-03-29 08:25:57.000000 aliyun-log-python-sdk-0.8.4/aliyun/log/logclient.py
--rwxr-xr-x   0 zhhfan     (502) staff       (20)    12625 2023-03-29 01:29:34.000000 aliyun-log-python-sdk-0.8.4/aliyun/log/logclient_core.py
--rw-r--r--   0 zhhfan     (502) staff       (20)    39275 2023-03-29 01:29:34.000000 aliyun-log-python-sdk-0.8.4/aliyun/log/logclient_operator.py
--rwxr-xr-x   0 zhhfan     (502) staff       (20)     1998 2023-03-29 01:29:34.000000 aliyun-log-python-sdk-0.8.4/aliyun/log/logexception.py
--rw-r--r--   0 zhhfan     (502) staff       (20)    23176 2023-03-29 01:29:34.000000 aliyun-log-python-sdk-0.8.4/aliyun/log/logger_hanlder.py
--rwxr-xr-x   0 zhhfan     (502) staff       (20)     1922 2023-03-29 01:29:34.000000 aliyun-log-python-sdk-0.8.4/aliyun/log/logitem.py
--rwxr-xr-x   0 zhhfan     (502) staff       (20)      700 2023-03-29 01:29:34.000000 aliyun-log-python-sdk-0.8.4/aliyun/log/logrequest.py
--rwxr-xr-x   0 zhhfan     (502) staff       (20)     1375 2023-03-29 01:29:34.000000 aliyun-log-python-sdk-0.8.4/aliyun/log/logresponse.py
--rwxr-xr-x   0 zhhfan     (502) staff       (20)     5722 2023-03-29 01:29:34.000000 aliyun-log-python-sdk-0.8.4/aliyun/log/logstore_config_response.py
--rwxr-xr-x   0 zhhfan     (502) staff       (20)    41883 2023-03-29 01:29:34.000000 aliyun-log-python-sdk-0.8.4/aliyun/log/logtail_config_detail.py
--rwxr-xr-x   0 zhhfan     (502) staff       (20)     4086 2023-03-29 01:29:34.000000 aliyun-log-python-sdk-0.8.4/aliyun/log/logtail_config_response.py
--rwxr-xr-x   0 zhhfan     (502) staff       (20)     2826 2023-03-29 01:29:34.000000 aliyun-log-python-sdk-0.8.4/aliyun/log/machine_group_detail.py
--rwxr-xr-x   0 zhhfan     (502) staff       (20)     9341 2023-03-29 01:29:34.000000 aliyun-log-python-sdk-0.8.4/aliyun/log/machinegroup_response.py
--rw-r--r--   0 zhhfan     (502) staff       (20)     2438 2023-03-29 01:29:34.000000 aliyun-log-python-sdk-0.8.4/aliyun/log/odps_sink.py
--rw-r--r--   0 zhhfan     (502) staff       (20)     2517 2023-03-29 01:29:34.000000 aliyun-log-python-sdk-0.8.4/aliyun/log/oss_sink.py
--rw-r--r--   0 zhhfan     (502) staff       (20)     2293 2023-03-29 01:29:34.000000 aliyun-log-python-sdk-0.8.4/aliyun/log/pluralize.py
--rwxr-xr-x   0 zhhfan     (502) staff       (20)     3795 2023-03-29 01:29:34.000000 aliyun-log-python-sdk-0.8.4/aliyun/log/project_response.py
--rwxr-xr-x   0 zhhfan     (502) staff       (20)     6141 2023-03-29 01:29:34.000000 aliyun-log-python-sdk-0.8.4/aliyun/log/pulllog_response.py
--rwxr-xr-x   0 zhhfan     (502) staff       (20)     3388 2023-03-29 01:29:34.000000 aliyun-log-python-sdk-0.8.4/aliyun/log/putlogsrequest.py
--rwxr-xr-x   0 zhhfan     (502) staff       (20)      545 2023-03-29 01:29:34.000000 aliyun-log-python-sdk-0.8.4/aliyun/log/putlogsresponse.py
--rwxr-xr-x   0 zhhfan     (502) staff       (20)     1247 2023-03-29 01:29:34.000000 aliyun-log-python-sdk-0.8.4/aliyun/log/queriedlog.py
--rw-r--r--   0 zhhfan     (502) staff       (20)     9831 2023-03-29 01:29:34.000000 aliyun-log-python-sdk-0.8.4/aliyun/log/resource_params.py
--rw-r--r--   0 zhhfan     (502) staff       (20)     7925 2023-03-29 01:29:34.000000 aliyun-log-python-sdk-0.8.4/aliyun/log/resource_response.py
--rwxr-xr-x   0 zhhfan     (502) staff       (20)     1358 2023-03-29 01:29:34.000000 aliyun-log-python-sdk-0.8.4/aliyun/log/shard_response.py
--rwxr-xr-x   0 zhhfan     (502) staff       (20)     4652 2023-03-29 01:29:34.000000 aliyun-log-python-sdk-0.8.4/aliyun/log/shipper_config.py
--rwxr-xr-x   0 zhhfan     (502) staff       (20)     7532 2023-03-29 01:29:34.000000 aliyun-log-python-sdk-0.8.4/aliyun/log/shipper_response.py
--rw-r--r--   0 zhhfan     (502) staff       (20)      358 2023-03-29 01:29:34.000000 aliyun-log-python-sdk-0.8.4/aliyun/log/sink.py
--rw-r--r--   0 zhhfan     (502) staff       (20)     1775 2023-03-29 01:29:34.000000 aliyun-log-python-sdk-0.8.4/aliyun/log/sql_instance_response.py
--rwxr-xr-x   0 zhhfan     (502) staff       (20)     5833 2023-03-29 01:29:34.000000 aliyun-log-python-sdk-0.8.4/aliyun/log/substore_config_response.py
--rw-r--r--   0 zhhfan     (502) staff       (20)    13437 2023-03-29 01:29:34.000000 aliyun-log-python-sdk-0.8.4/aliyun/log/topostore_params.py
--rw-r--r--   0 zhhfan     (502) staff       (20)    13619 2023-03-29 01:29:34.000000 aliyun-log-python-sdk-0.8.4/aliyun/log/topostore_response.py
--rwxr-xr-x   0 zhhfan     (502) staff       (20)     9206 2023-03-29 01:29:34.000000 aliyun-log-python-sdk-0.8.4/aliyun/log/util.py
--rw-r--r--   0 zhhfan     (502) staff       (20)      341 2023-03-29 08:25:57.000000 aliyun-log-python-sdk-0.8.4/aliyun/log/version.py
-drwxr-xr-x   0 zhhfan     (502) staff       (20)        0 2023-03-29 08:27:23.472838 aliyun-log-python-sdk-0.8.4/aliyun_log_python_sdk.egg-info/
--rw-r--r--   0 zhhfan     (502) staff       (20)      863 2023-03-29 08:27:23.000000 aliyun-log-python-sdk-0.8.4/aliyun_log_python_sdk.egg-info/PKG-INFO
--rw-r--r--   0 zhhfan     (502) staff       (20)     3957 2023-03-29 08:27:23.000000 aliyun-log-python-sdk-0.8.4/aliyun_log_python_sdk.egg-info/SOURCES.txt
--rw-r--r--   0 zhhfan     (502) staff       (20)        1 2023-03-29 08:27:23.000000 aliyun-log-python-sdk-0.8.4/aliyun_log_python_sdk.egg-info/dependency_links.txt
--rw-r--r--   0 zhhfan     (502) staff       (20)       86 2023-03-29 08:27:23.000000 aliyun-log-python-sdk-0.8.4/aliyun_log_python_sdk.egg-info/requires.txt
--rw-r--r--   0 zhhfan     (502) staff       (20)        7 2023-03-29 08:27:23.000000 aliyun-log-python-sdk-0.8.4/aliyun_log_python_sdk.egg-info/top_level.txt
--rw-r--r--   0 zhhfan     (502) staff       (20)       38 2023-03-29 08:27:23.474198 aliyun-log-python-sdk-0.8.4/setup.cfg
--rwxr-xr-x   0 zhhfan     (502) staff       (20)     2847 2023-03-29 01:29:34.000000 aliyun-log-python-sdk-0.8.4/setup.py
+drwxr-xr-x   0 zhhfan     (502) staff       (20)        0 2023-04-06 08:57:32.711578 aliyun-log-python-sdk-0.8.5/
+-rw-r--r--   0 zhhfan     (502) staff       (20)     1070 2023-03-29 01:29:33.000000 aliyun-log-python-sdk-0.8.5/LICENSE
+-rw-r--r--   0 zhhfan     (502) staff       (20)      863 2023-04-06 08:57:32.711046 aliyun-log-python-sdk-0.8.5/PKG-INFO
+-rwxr-xr-x   0 zhhfan     (502) staff       (20)     2677 2023-03-29 01:29:33.000000 aliyun-log-python-sdk-0.8.5/README.md
+drwxr-xr-x   0 zhhfan     (502) staff       (20)        0 2023-04-06 08:57:32.617424 aliyun-log-python-sdk-0.8.5/aliyun/
+-rwxr-xr-x   0 zhhfan     (502) staff       (20)        0 2023-03-29 01:29:33.000000 aliyun-log-python-sdk-0.8.5/aliyun/__init__.py
+drwxr-xr-x   0 zhhfan     (502) staff       (20)        0 2023-04-06 08:57:32.669253 aliyun-log-python-sdk-0.8.5/aliyun/log/
+-rwxr-xr-x   0 zhhfan     (502) staff       (20)     1648 2023-03-29 01:29:33.000000 aliyun-log-python-sdk-0.8.5/aliyun/log/__init__.py
+-rwxr-xr-x   0 zhhfan     (502) staff       (20)      879 2023-03-29 01:29:33.000000 aliyun-log-python-sdk-0.8.5/aliyun/log/acl_config.py
+-rwxr-xr-x   0 zhhfan     (502) staff       (20)     1629 2023-03-29 01:29:33.000000 aliyun-log-python-sdk-0.8.5/aliyun/log/acl_response.py
+-rw-r--r--   0 zhhfan     (502) staff       (20)     6712 2023-03-29 01:29:33.000000 aliyun-log-python-sdk-0.8.5/aliyun/log/auth.py
+-rw-r--r--   0 zhhfan     (502) staff       (20)     2784 2023-03-29 01:29:33.000000 aliyun-log-python-sdk-0.8.5/aliyun/log/common_response.py
+drwxr-xr-x   0 zhhfan     (502) staff       (20)        0 2023-04-06 08:57:32.676019 aliyun-log-python-sdk-0.8.5/aliyun/log/consumer/
+-rwxr-xr-x   0 zhhfan     (502) staff       (20)      152 2023-03-29 01:29:33.000000 aliyun-log-python-sdk-0.8.5/aliyun/log/consumer/__init__.py
+-rwxr-xr-x   0 zhhfan     (502) staff       (20)     2319 2023-03-29 01:29:33.000000 aliyun-log-python-sdk-0.8.5/aliyun/log/consumer/checkpoint_tracker.py
+-rwxr-xr-x   0 zhhfan     (502) staff       (20)     4379 2023-03-29 01:29:33.000000 aliyun-log-python-sdk-0.8.5/aliyun/log/consumer/config.py
+-rwxr-xr-x   0 zhhfan     (502) staff       (20)     4577 2023-03-29 01:29:33.000000 aliyun-log-python-sdk-0.8.5/aliyun/log/consumer/consumer_client.py
+-rw-r--r--   0 zhhfan     (502) staff       (20)      531 2023-03-29 01:29:33.000000 aliyun-log-python-sdk-0.8.5/aliyun/log/consumer/exceptions.py
+-rwxr-xr-x   0 zhhfan     (502) staff       (20)      590 2023-03-29 01:29:33.000000 aliyun-log-python-sdk-0.8.5/aliyun/log/consumer/fetched_log_group.py
+-rwxr-xr-x   0 zhhfan     (502) staff       (20)     4159 2023-03-29 01:29:33.000000 aliyun-log-python-sdk-0.8.5/aliyun/log/consumer/heart_beat.py
+-rwxr-xr-x   0 zhhfan     (502) staff       (20)    11472 2023-03-29 01:29:33.000000 aliyun-log-python-sdk-0.8.5/aliyun/log/consumer/shard_worker.py
+-rwxr-xr-x   0 zhhfan     (502) staff       (20)     7454 2023-03-29 01:29:33.000000 aliyun-log-python-sdk-0.8.5/aliyun/log/consumer/tasks.py
+-rwxr-xr-x   0 zhhfan     (502) staff       (20)     8589 2023-03-29 01:29:33.000000 aliyun-log-python-sdk-0.8.5/aliyun/log/consumer/worker.py
+-rwxr-xr-x   0 zhhfan     (502) staff       (20)     3285 2023-03-29 01:29:33.000000 aliyun-log-python-sdk-0.8.5/aliyun/log/consumer_group_request.py
+-rwxr-xr-x   0 zhhfan     (502) staff       (20)     5252 2023-03-29 01:29:33.000000 aliyun-log-python-sdk-0.8.5/aliyun/log/consumer_group_response.py
+-rwxr-xr-x   0 zhhfan     (502) staff       (20)      813 2023-03-29 01:29:33.000000 aliyun-log-python-sdk-0.8.5/aliyun/log/cursor_response.py
+-rwxr-xr-x   0 zhhfan     (502) staff       (20)      808 2023-03-29 01:29:33.000000 aliyun-log-python-sdk-0.8.5/aliyun/log/cursor_time_response.py
+drwxr-xr-x   0 zhhfan     (502) staff       (20)        0 2023-04-06 08:57:32.684033 aliyun-log-python-sdk-0.8.5/aliyun/log/es_migration/
+-rw-r--r--   0 zhhfan     (502) staff       (20)      171 2023-03-29 01:29:33.000000 aliyun-log-python-sdk-0.8.5/aliyun/log/es_migration/__init__.py
+-rw-r--r--   0 zhhfan     (502) staff       (20)     1690 2023-03-29 01:29:33.000000 aliyun-log-python-sdk-0.8.5/aliyun/log/es_migration/doc_logitem_converter.py
+-rw-r--r--   0 zhhfan     (502) staff       (20)     2583 2023-03-29 01:29:33.000000 aliyun-log-python-sdk-0.8.5/aliyun/log/es_migration/index_logstore_mappings.py
+-rw-r--r--   0 zhhfan     (502) staff       (20)    11037 2023-03-29 01:29:33.000000 aliyun-log-python-sdk-0.8.5/aliyun/log/es_migration/mapping_index_converter.py
+-rw-r--r--   0 zhhfan     (502) staff       (20)     2347 2023-03-29 01:29:33.000000 aliyun-log-python-sdk-0.8.5/aliyun/log/es_migration/migration_log.py
+-rw-r--r--   0 zhhfan     (502) staff       (20)    16932 2023-03-29 01:29:33.000000 aliyun-log-python-sdk-0.8.5/aliyun/log/es_migration/migration_manager.py
+-rw-r--r--   0 zhhfan     (502) staff       (20)      281 2023-03-29 01:29:33.000000 aliyun-log-python-sdk-0.8.5/aliyun/log/es_migration/migration_response.py
+-rw-r--r--   0 zhhfan     (502) staff       (20)     8326 2023-03-29 01:29:33.000000 aliyun-log-python-sdk-0.8.5/aliyun/log/es_migration/migration_task.py
+-rwxr-xr-x   0 zhhfan     (502) staff       (20)      194 2023-03-29 01:29:33.000000 aliyun-log-python-sdk-0.8.5/aliyun/log/es_migration/util.py
+-rw-r--r--   0 zhhfan     (502) staff       (20)     4373 2023-03-29 01:29:33.000000 aliyun-log-python-sdk-0.8.5/aliyun/log/etl_config_response.py
+drwxr-xr-x   0 zhhfan     (502) staff       (20)        0 2023-04-06 08:57:32.688480 aliyun-log-python-sdk-0.8.5/aliyun/log/etl_core/
+-rw-r--r--   0 zhhfan     (502) staff       (20)      128 2023-03-29 01:29:33.000000 aliyun-log-python-sdk-0.8.5/aliyun/log/etl_core/__init__.py
+-rw-r--r--   0 zhhfan     (502) staff       (20)     2301 2023-03-29 01:29:33.000000 aliyun-log-python-sdk-0.8.5/aliyun/log/etl_core/config_parser.py
+-rw-r--r--   0 zhhfan     (502) staff       (20)     5370 2023-03-29 01:29:33.000000 aliyun-log-python-sdk-0.8.5/aliyun/log/etl_core/etl_util.py
+-rw-r--r--   0 zhhfan     (502) staff       (20)      450 2023-03-29 01:29:33.000000 aliyun-log-python-sdk-0.8.5/aliyun/log/etl_core/exceptions.py
+-rw-r--r--   0 zhhfan     (502) staff       (20)     2723 2023-03-29 01:29:33.000000 aliyun-log-python-sdk-0.8.5/aliyun/log/etl_core/restrict_config_parser.py
+-rw-r--r--   0 zhhfan     (502) staff       (20)     1245 2023-03-29 01:29:33.000000 aliyun-log-python-sdk-0.8.5/aliyun/log/etl_core/runner.py
+-rw-r--r--   0 zhhfan     (502) staff       (20)     1422 2023-03-29 01:29:33.000000 aliyun-log-python-sdk-0.8.5/aliyun/log/etl_core/settings.py
+drwxr-xr-x   0 zhhfan     (502) staff       (20)        0 2023-04-06 08:57:32.693851 aliyun-log-python-sdk-0.8.5/aliyun/log/etl_core/trans_comp/
+-rw-r--r--   0 zhhfan     (502) staff       (20)      500 2023-03-29 01:29:33.000000 aliyun-log-python-sdk-0.8.5/aliyun/log/etl_core/trans_comp/__init__.py
+-rw-r--r--   0 zhhfan     (502) staff       (20)     2523 2023-03-29 01:29:33.000000 aliyun-log-python-sdk-0.8.5/aliyun/log/etl_core/trans_comp/trans_base.py
+-rw-r--r--   0 zhhfan     (502) staff       (20)     2031 2023-03-29 01:29:33.000000 aliyun-log-python-sdk-0.8.5/aliyun/log/etl_core/trans_comp/trans_csv.py
+-rw-r--r--   0 zhhfan     (502) staff       (20)    14656 2023-03-29 01:29:33.000000 aliyun-log-python-sdk-0.8.5/aliyun/log/etl_core/trans_comp/trans_json.py
+-rw-r--r--   0 zhhfan     (502) staff       (20)     3649 2023-03-29 01:29:33.000000 aliyun-log-python-sdk-0.8.5/aliyun/log/etl_core/trans_comp/trans_kv.py
+-rw-r--r--   0 zhhfan     (502) staff       (20)     9141 2023-03-29 01:29:33.000000 aliyun-log-python-sdk-0.8.5/aliyun/log/etl_core/trans_comp/trans_lookup.py
+-rw-r--r--   0 zhhfan     (502) staff       (20)     4051 2023-03-29 01:29:33.000000 aliyun-log-python-sdk-0.8.5/aliyun/log/etl_core/trans_comp/trans_mv.py
+-rw-r--r--   0 zhhfan     (502) staff       (20)     5215 2023-03-29 01:29:33.000000 aliyun-log-python-sdk-0.8.5/aliyun/log/etl_core/trans_comp/trans_regex.py
+-rw-r--r--   0 zhhfan     (502) staff       (20)     3704 2023-03-29 01:29:33.000000 aliyun-log-python-sdk-0.8.5/aliyun/log/etl_core/trans_comp/trans_set_field.py
+drwxr-xr-x   0 zhhfan     (502) staff       (20)        0 2023-04-06 08:57:32.698002 aliyun-log-python-sdk-0.8.5/aliyun/log/etl_core/transform/
+-rw-r--r--   0 zhhfan     (502) staff       (20)      156 2023-03-29 01:29:33.000000 aliyun-log-python-sdk-0.8.5/aliyun/log/etl_core/transform/__init__.py
+-rw-r--r--   0 zhhfan     (502) staff       (20)     4419 2023-03-29 01:29:33.000000 aliyun-log-python-sdk-0.8.5/aliyun/log/etl_core/transform/condition_list.py
+-rw-r--r--   0 zhhfan     (502) staff       (20)     1923 2023-03-29 01:29:33.000000 aliyun-log-python-sdk-0.8.5/aliyun/log/etl_core/transform/condition_transform.py
+-rw-r--r--   0 zhhfan     (502) staff       (20)      903 2023-03-29 01:29:33.000000 aliyun-log-python-sdk-0.8.5/aliyun/log/etl_core/transform/condition_util.py
+-rw-r--r--   0 zhhfan     (502) staff       (20)      145 2023-03-29 01:29:33.000000 aliyun-log-python-sdk-0.8.5/aliyun/log/etl_core/transform/transform_base.py
+-rw-r--r--   0 zhhfan     (502) staff       (20)     2126 2023-03-29 01:29:33.000000 aliyun-log-python-sdk-0.8.5/aliyun/log/etl_core/transform/transform_list.py
+-rw-r--r--   0 zhhfan     (502) staff       (20)     3680 2023-03-29 01:29:33.000000 aliyun-log-python-sdk-0.8.5/aliyun/log/etl_core/transform/transform_meta.py
+-rw-r--r--   0 zhhfan     (502) staff       (20)     2764 2023-03-29 01:29:33.000000 aliyun-log-python-sdk-0.8.5/aliyun/log/export_response.py
+drwxr-xr-x   0 zhhfan     (502) staff       (20)        0 2023-04-06 08:57:32.700364 aliyun-log-python-sdk-0.8.5/aliyun/log/ext/
+-rwxr-xr-x   0 zhhfan     (502) staff       (20)        0 2023-03-29 01:29:33.000000 aliyun-log-python-sdk-0.8.5/aliyun/log/ext/__init__.py
+-rw-r--r--   0 zhhfan     (502) staff       (20)    13130 2023-03-29 01:29:33.000000 aliyun-log-python-sdk-0.8.5/aliyun/log/ext/jupyter_magic.py
+-rw-r--r--   0 zhhfan     (502) staff       (20)     7247 2023-03-29 01:29:33.000000 aliyun-log-python-sdk-0.8.5/aliyun/log/ext/syslogclient.py
+-rw-r--r--   0 zhhfan     (502) staff       (20)     7849 2023-04-06 08:53:04.000000 aliyun-log-python-sdk-0.8.5/aliyun/log/external_store_config.py
+-rw-r--r--   0 zhhfan     (502) staff       (20)     4315 2023-03-29 01:29:34.000000 aliyun-log-python-sdk-0.8.5/aliyun/log/external_store_config_response.py
+-rw-r--r--   0 zhhfan     (502) staff       (20)     2931 2023-03-29 01:29:34.000000 aliyun-log-python-sdk-0.8.5/aliyun/log/getcontextlogsresponse.py
+-rwxr-xr-x   0 zhhfan     (502) staff       (20)     3400 2023-03-29 01:29:34.000000 aliyun-log-python-sdk-0.8.5/aliyun/log/gethistogramsrequest.py
+-rwxr-xr-x   0 zhhfan     (502) staff       (20)     1922 2023-03-29 01:29:34.000000 aliyun-log-python-sdk-0.8.5/aliyun/log/gethistogramsresponse.py
+-rwxr-xr-x   0 zhhfan     (502) staff       (20)     6186 2023-03-29 01:29:34.000000 aliyun-log-python-sdk-0.8.5/aliyun/log/getlogsrequest.py
+-rwxr-xr-x   0 zhhfan     (502) staff       (20)     4460 2023-03-29 01:29:34.000000 aliyun-log-python-sdk-0.8.5/aliyun/log/getlogsresponse.py
+-rwxr-xr-x   0 zhhfan     (502) staff       (20)     1733 2023-03-29 01:29:34.000000 aliyun-log-python-sdk-0.8.5/aliyun/log/histogram.py
+-rwxr-xr-x   0 zhhfan     (502) staff       (20)    10335 2023-03-29 01:29:34.000000 aliyun-log-python-sdk-0.8.5/aliyun/log/index_config.py
+-rwxr-xr-x   0 zhhfan     (502) staff       (20)     2220 2023-03-29 01:29:34.000000 aliyun-log-python-sdk-0.8.5/aliyun/log/index_config_response.py
+-rw-r--r--   0 zhhfan     (502) staff       (20)     5180 2023-03-29 01:29:34.000000 aliyun-log-python-sdk-0.8.5/aliyun/log/ingestion_response.py
+-rw-r--r--   0 zhhfan     (502) staff       (20)     6360 2023-03-29 01:29:34.000000 aliyun-log-python-sdk-0.8.5/aliyun/log/job.py
+-rwxr-xr-x   0 zhhfan     (502) staff       (20)      407 2023-03-29 01:29:34.000000 aliyun-log-python-sdk-0.8.5/aliyun/log/listlogstoresrequest.py
+-rwxr-xr-x   0 zhhfan     (502) staff       (20)     1902 2023-03-29 01:29:34.000000 aliyun-log-python-sdk-0.8.5/aliyun/log/listlogstoresresponse.py
+-rwxr-xr-x   0 zhhfan     (502) staff       (20)     1897 2023-03-29 01:29:34.000000 aliyun-log-python-sdk-0.8.5/aliyun/log/listtopicsrequest.py
+-rwxr-xr-x   0 zhhfan     (502) staff       (20)     1570 2023-03-29 01:29:34.000000 aliyun-log-python-sdk-0.8.5/aliyun/log/listtopicsresponse.py
+-rwxr-xr-x   0 zhhfan     (502) staff       (20)     8952 2023-03-29 01:29:34.000000 aliyun-log-python-sdk-0.8.5/aliyun/log/log_logs_pb2.py
+-rw-r--r--   0 zhhfan     (502) staff       (20)     9641 2023-03-29 01:29:34.000000 aliyun-log-python-sdk-0.8.5/aliyun/log/log_logs_raw_pb2.py
+-rw-r--r--   0 zhhfan     (502) staff       (20)   203428 2023-04-06 08:53:15.000000 aliyun-log-python-sdk-0.8.5/aliyun/log/logclient.py
+-rwxr-xr-x   0 zhhfan     (502) staff       (20)    12625 2023-03-29 01:29:34.000000 aliyun-log-python-sdk-0.8.5/aliyun/log/logclient_core.py
+-rw-r--r--   0 zhhfan     (502) staff       (20)    39275 2023-03-29 01:29:34.000000 aliyun-log-python-sdk-0.8.5/aliyun/log/logclient_operator.py
+-rwxr-xr-x   0 zhhfan     (502) staff       (20)     1998 2023-03-29 01:29:34.000000 aliyun-log-python-sdk-0.8.5/aliyun/log/logexception.py
+-rw-r--r--   0 zhhfan     (502) staff       (20)    23176 2023-03-29 01:29:34.000000 aliyun-log-python-sdk-0.8.5/aliyun/log/logger_hanlder.py
+-rwxr-xr-x   0 zhhfan     (502) staff       (20)     1922 2023-03-29 01:29:34.000000 aliyun-log-python-sdk-0.8.5/aliyun/log/logitem.py
+-rwxr-xr-x   0 zhhfan     (502) staff       (20)      700 2023-03-29 01:29:34.000000 aliyun-log-python-sdk-0.8.5/aliyun/log/logrequest.py
+-rwxr-xr-x   0 zhhfan     (502) staff       (20)     1375 2023-03-29 01:29:34.000000 aliyun-log-python-sdk-0.8.5/aliyun/log/logresponse.py
+-rwxr-xr-x   0 zhhfan     (502) staff       (20)     5722 2023-03-29 01:29:34.000000 aliyun-log-python-sdk-0.8.5/aliyun/log/logstore_config_response.py
+-rwxr-xr-x   0 zhhfan     (502) staff       (20)    41883 2023-03-29 01:29:34.000000 aliyun-log-python-sdk-0.8.5/aliyun/log/logtail_config_detail.py
+-rwxr-xr-x   0 zhhfan     (502) staff       (20)     4086 2023-03-29 01:29:34.000000 aliyun-log-python-sdk-0.8.5/aliyun/log/logtail_config_response.py
+-rwxr-xr-x   0 zhhfan     (502) staff       (20)     2826 2023-03-29 01:29:34.000000 aliyun-log-python-sdk-0.8.5/aliyun/log/machine_group_detail.py
+-rwxr-xr-x   0 zhhfan     (502) staff       (20)     9341 2023-03-29 01:29:34.000000 aliyun-log-python-sdk-0.8.5/aliyun/log/machinegroup_response.py
+-rw-r--r--   0 zhhfan     (502) staff       (20)     2438 2023-03-29 01:29:34.000000 aliyun-log-python-sdk-0.8.5/aliyun/log/odps_sink.py
+-rw-r--r--   0 zhhfan     (502) staff       (20)     2517 2023-03-29 01:29:34.000000 aliyun-log-python-sdk-0.8.5/aliyun/log/oss_sink.py
+-rw-r--r--   0 zhhfan     (502) staff       (20)     2293 2023-03-29 01:29:34.000000 aliyun-log-python-sdk-0.8.5/aliyun/log/pluralize.py
+-rwxr-xr-x   0 zhhfan     (502) staff       (20)     3795 2023-03-29 01:29:34.000000 aliyun-log-python-sdk-0.8.5/aliyun/log/project_response.py
+-rwxr-xr-x   0 zhhfan     (502) staff       (20)     6141 2023-03-29 01:29:34.000000 aliyun-log-python-sdk-0.8.5/aliyun/log/pulllog_response.py
+-rwxr-xr-x   0 zhhfan     (502) staff       (20)     3388 2023-03-29 01:29:34.000000 aliyun-log-python-sdk-0.8.5/aliyun/log/putlogsrequest.py
+-rwxr-xr-x   0 zhhfan     (502) staff       (20)      545 2023-03-29 01:29:34.000000 aliyun-log-python-sdk-0.8.5/aliyun/log/putlogsresponse.py
+-rwxr-xr-x   0 zhhfan     (502) staff       (20)     1247 2023-03-29 01:29:34.000000 aliyun-log-python-sdk-0.8.5/aliyun/log/queriedlog.py
+-rw-r--r--   0 zhhfan     (502) staff       (20)     9831 2023-03-29 01:29:34.000000 aliyun-log-python-sdk-0.8.5/aliyun/log/resource_params.py
+-rw-r--r--   0 zhhfan     (502) staff       (20)     7925 2023-03-29 01:29:34.000000 aliyun-log-python-sdk-0.8.5/aliyun/log/resource_response.py
+-rwxr-xr-x   0 zhhfan     (502) staff       (20)     1358 2023-03-29 01:29:34.000000 aliyun-log-python-sdk-0.8.5/aliyun/log/shard_response.py
+-rwxr-xr-x   0 zhhfan     (502) staff       (20)     4652 2023-03-29 01:29:34.000000 aliyun-log-python-sdk-0.8.5/aliyun/log/shipper_config.py
+-rwxr-xr-x   0 zhhfan     (502) staff       (20)     7532 2023-03-29 01:29:34.000000 aliyun-log-python-sdk-0.8.5/aliyun/log/shipper_response.py
+-rw-r--r--   0 zhhfan     (502) staff       (20)      358 2023-03-29 01:29:34.000000 aliyun-log-python-sdk-0.8.5/aliyun/log/sink.py
+-rw-r--r--   0 zhhfan     (502) staff       (20)     1775 2023-03-29 01:29:34.000000 aliyun-log-python-sdk-0.8.5/aliyun/log/sql_instance_response.py
+-rwxr-xr-x   0 zhhfan     (502) staff       (20)     5833 2023-03-29 01:29:34.000000 aliyun-log-python-sdk-0.8.5/aliyun/log/substore_config_response.py
+-rw-r--r--   0 zhhfan     (502) staff       (20)    13437 2023-03-29 01:29:34.000000 aliyun-log-python-sdk-0.8.5/aliyun/log/topostore_params.py
+-rw-r--r--   0 zhhfan     (502) staff       (20)    13619 2023-03-29 01:29:34.000000 aliyun-log-python-sdk-0.8.5/aliyun/log/topostore_response.py
+-rwxr-xr-x   0 zhhfan     (502) staff       (20)     9206 2023-03-29 01:29:34.000000 aliyun-log-python-sdk-0.8.5/aliyun/log/util.py
+-rw-r--r--   0 zhhfan     (502) staff       (20)      341 2023-04-06 08:54:52.000000 aliyun-log-python-sdk-0.8.5/aliyun/log/version.py
+drwxr-xr-x   0 zhhfan     (502) staff       (20)        0 2023-04-06 08:57:32.710159 aliyun-log-python-sdk-0.8.5/aliyun_log_python_sdk.egg-info/
+-rw-r--r--   0 zhhfan     (502) staff       (20)      863 2023-04-06 08:57:32.000000 aliyun-log-python-sdk-0.8.5/aliyun_log_python_sdk.egg-info/PKG-INFO
+-rw-r--r--   0 zhhfan     (502) staff       (20)     3957 2023-04-06 08:57:32.000000 aliyun-log-python-sdk-0.8.5/aliyun_log_python_sdk.egg-info/SOURCES.txt
+-rw-r--r--   0 zhhfan     (502) staff       (20)        1 2023-04-06 08:57:32.000000 aliyun-log-python-sdk-0.8.5/aliyun_log_python_sdk.egg-info/dependency_links.txt
+-rw-r--r--   0 zhhfan     (502) staff       (20)       86 2023-04-06 08:57:32.000000 aliyun-log-python-sdk-0.8.5/aliyun_log_python_sdk.egg-info/requires.txt
+-rw-r--r--   0 zhhfan     (502) staff       (20)        7 2023-04-06 08:57:32.000000 aliyun-log-python-sdk-0.8.5/aliyun_log_python_sdk.egg-info/top_level.txt
+-rw-r--r--   0 zhhfan     (502) staff       (20)       38 2023-04-06 08:57:32.711758 aliyun-log-python-sdk-0.8.5/setup.cfg
+-rwxr-xr-x   0 zhhfan     (502) staff       (20)     2847 2023-03-29 01:29:34.000000 aliyun-log-python-sdk-0.8.5/setup.py
```

### Comparing `aliyun-log-python-sdk-0.8.4/LICENSE` & `aliyun-log-python-sdk-0.8.5/LICENSE`

 * *Files identical despite different names*

### Comparing `aliyun-log-python-sdk-0.8.4/PKG-INFO` & `aliyun-log-python-sdk-0.8.5/PKG-INFO`

 * *Files 11% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: aliyun-log-python-sdk
-Version: 0.8.4
+Version: 0.8.5
 Summary: Aliyun log service Python client SDK
 Home-page: https://github.com/aliyun/aliyun-log-python-sdk
 Author: Aliyun
 Classifier: Development Status :: 5 - Production/Stable
 Classifier: License :: OSI Approved :: MIT License
 Classifier: Operating System :: OS Independent
 Classifier: Programming Language :: Python :: 2.6
```

### Comparing `aliyun-log-python-sdk-0.8.4/README.md` & `aliyun-log-python-sdk-0.8.5/README.md`

 * *Files identical despite different names*

### Comparing `aliyun-log-python-sdk-0.8.4/aliyun/log/__init__.py` & `aliyun-log-python-sdk-0.8.5/aliyun/log/__init__.py`

 * *Files identical despite different names*

### Comparing `aliyun-log-python-sdk-0.8.4/aliyun/log/acl_config.py` & `aliyun-log-python-sdk-0.8.5/aliyun/log/acl_config.py`

 * *Files identical despite different names*

### Comparing `aliyun-log-python-sdk-0.8.4/aliyun/log/acl_response.py` & `aliyun-log-python-sdk-0.8.5/aliyun/log/acl_response.py`

 * *Files identical despite different names*

### Comparing `aliyun-log-python-sdk-0.8.4/aliyun/log/auth.py` & `aliyun-log-python-sdk-0.8.5/aliyun/log/auth.py`

 * *Files identical despite different names*

### Comparing `aliyun-log-python-sdk-0.8.4/aliyun/log/common_response.py` & `aliyun-log-python-sdk-0.8.5/aliyun/log/common_response.py`

 * *Files identical despite different names*

### Comparing `aliyun-log-python-sdk-0.8.4/aliyun/log/consumer/checkpoint_tracker.py` & `aliyun-log-python-sdk-0.8.5/aliyun/log/consumer/checkpoint_tracker.py`

 * *Files identical despite different names*

### Comparing `aliyun-log-python-sdk-0.8.4/aliyun/log/consumer/config.py` & `aliyun-log-python-sdk-0.8.5/aliyun/log/consumer/config.py`

 * *Files identical despite different names*

### Comparing `aliyun-log-python-sdk-0.8.4/aliyun/log/consumer/consumer_client.py` & `aliyun-log-python-sdk-0.8.5/aliyun/log/consumer/consumer_client.py`

 * *Files identical despite different names*

### Comparing `aliyun-log-python-sdk-0.8.4/aliyun/log/consumer/exceptions.py` & `aliyun-log-python-sdk-0.8.5/aliyun/log/consumer/exceptions.py`

 * *Files identical despite different names*

### Comparing `aliyun-log-python-sdk-0.8.4/aliyun/log/consumer/fetched_log_group.py` & `aliyun-log-python-sdk-0.8.5/aliyun/log/consumer/fetched_log_group.py`

 * *Files identical despite different names*

### Comparing `aliyun-log-python-sdk-0.8.4/aliyun/log/consumer/heart_beat.py` & `aliyun-log-python-sdk-0.8.5/aliyun/log/consumer/heart_beat.py`

 * *Files identical despite different names*

### Comparing `aliyun-log-python-sdk-0.8.4/aliyun/log/consumer/shard_worker.py` & `aliyun-log-python-sdk-0.8.5/aliyun/log/consumer/shard_worker.py`

 * *Files identical despite different names*

### Comparing `aliyun-log-python-sdk-0.8.4/aliyun/log/consumer/tasks.py` & `aliyun-log-python-sdk-0.8.5/aliyun/log/consumer/tasks.py`

 * *Files identical despite different names*

### Comparing `aliyun-log-python-sdk-0.8.4/aliyun/log/consumer/worker.py` & `aliyun-log-python-sdk-0.8.5/aliyun/log/consumer/worker.py`

 * *Files identical despite different names*

### Comparing `aliyun-log-python-sdk-0.8.4/aliyun/log/consumer_group_request.py` & `aliyun-log-python-sdk-0.8.5/aliyun/log/consumer_group_request.py`

 * *Files identical despite different names*

### Comparing `aliyun-log-python-sdk-0.8.4/aliyun/log/consumer_group_response.py` & `aliyun-log-python-sdk-0.8.5/aliyun/log/consumer_group_response.py`

 * *Files identical despite different names*

### Comparing `aliyun-log-python-sdk-0.8.4/aliyun/log/cursor_response.py` & `aliyun-log-python-sdk-0.8.5/aliyun/log/cursor_response.py`

 * *Files identical despite different names*

### Comparing `aliyun-log-python-sdk-0.8.4/aliyun/log/cursor_time_response.py` & `aliyun-log-python-sdk-0.8.5/aliyun/log/cursor_time_response.py`

 * *Files identical despite different names*

### Comparing `aliyun-log-python-sdk-0.8.4/aliyun/log/es_migration/doc_logitem_converter.py` & `aliyun-log-python-sdk-0.8.5/aliyun/log/es_migration/doc_logitem_converter.py`

 * *Files identical despite different names*

### Comparing `aliyun-log-python-sdk-0.8.4/aliyun/log/es_migration/index_logstore_mappings.py` & `aliyun-log-python-sdk-0.8.5/aliyun/log/es_migration/index_logstore_mappings.py`

 * *Files identical despite different names*

### Comparing `aliyun-log-python-sdk-0.8.4/aliyun/log/es_migration/mapping_index_converter.py` & `aliyun-log-python-sdk-0.8.5/aliyun/log/es_migration/mapping_index_converter.py`

 * *Files identical despite different names*

### Comparing `aliyun-log-python-sdk-0.8.4/aliyun/log/es_migration/migration_log.py` & `aliyun-log-python-sdk-0.8.5/aliyun/log/es_migration/migration_log.py`

 * *Files identical despite different names*

### Comparing `aliyun-log-python-sdk-0.8.4/aliyun/log/es_migration/migration_manager.py` & `aliyun-log-python-sdk-0.8.5/aliyun/log/es_migration/migration_manager.py`

 * *Files identical despite different names*

### Comparing `aliyun-log-python-sdk-0.8.4/aliyun/log/es_migration/migration_task.py` & `aliyun-log-python-sdk-0.8.5/aliyun/log/es_migration/migration_task.py`

 * *Files identical despite different names*

### Comparing `aliyun-log-python-sdk-0.8.4/aliyun/log/etl_config_response.py` & `aliyun-log-python-sdk-0.8.5/aliyun/log/etl_config_response.py`

 * *Files identical despite different names*

### Comparing `aliyun-log-python-sdk-0.8.4/aliyun/log/etl_core/config_parser.py` & `aliyun-log-python-sdk-0.8.5/aliyun/log/etl_core/config_parser.py`

 * *Files identical despite different names*

### Comparing `aliyun-log-python-sdk-0.8.4/aliyun/log/etl_core/etl_util.py` & `aliyun-log-python-sdk-0.8.5/aliyun/log/etl_core/etl_util.py`

 * *Files identical despite different names*

### Comparing `aliyun-log-python-sdk-0.8.4/aliyun/log/etl_core/restrict_config_parser.py` & `aliyun-log-python-sdk-0.8.5/aliyun/log/etl_core/restrict_config_parser.py`

 * *Files identical despite different names*

### Comparing `aliyun-log-python-sdk-0.8.4/aliyun/log/etl_core/runner.py` & `aliyun-log-python-sdk-0.8.5/aliyun/log/etl_core/runner.py`

 * *Files identical despite different names*

### Comparing `aliyun-log-python-sdk-0.8.4/aliyun/log/etl_core/settings.py` & `aliyun-log-python-sdk-0.8.5/aliyun/log/etl_core/settings.py`

 * *Files identical despite different names*

### Comparing `aliyun-log-python-sdk-0.8.4/aliyun/log/etl_core/trans_comp/trans_base.py` & `aliyun-log-python-sdk-0.8.5/aliyun/log/etl_core/trans_comp/trans_base.py`

 * *Files identical despite different names*

### Comparing `aliyun-log-python-sdk-0.8.4/aliyun/log/etl_core/trans_comp/trans_csv.py` & `aliyun-log-python-sdk-0.8.5/aliyun/log/etl_core/trans_comp/trans_csv.py`

 * *Files identical despite different names*

### Comparing `aliyun-log-python-sdk-0.8.4/aliyun/log/etl_core/trans_comp/trans_json.py` & `aliyun-log-python-sdk-0.8.5/aliyun/log/etl_core/trans_comp/trans_json.py`

 * *Files identical despite different names*

### Comparing `aliyun-log-python-sdk-0.8.4/aliyun/log/etl_core/trans_comp/trans_kv.py` & `aliyun-log-python-sdk-0.8.5/aliyun/log/etl_core/trans_comp/trans_kv.py`

 * *Files identical despite different names*

### Comparing `aliyun-log-python-sdk-0.8.4/aliyun/log/etl_core/trans_comp/trans_lookup.py` & `aliyun-log-python-sdk-0.8.5/aliyun/log/etl_core/trans_comp/trans_lookup.py`

 * *Files identical despite different names*

### Comparing `aliyun-log-python-sdk-0.8.4/aliyun/log/etl_core/trans_comp/trans_mv.py` & `aliyun-log-python-sdk-0.8.5/aliyun/log/etl_core/trans_comp/trans_mv.py`

 * *Files identical despite different names*

### Comparing `aliyun-log-python-sdk-0.8.4/aliyun/log/etl_core/trans_comp/trans_regex.py` & `aliyun-log-python-sdk-0.8.5/aliyun/log/etl_core/trans_comp/trans_regex.py`

 * *Files identical despite different names*

### Comparing `aliyun-log-python-sdk-0.8.4/aliyun/log/etl_core/trans_comp/trans_set_field.py` & `aliyun-log-python-sdk-0.8.5/aliyun/log/etl_core/trans_comp/trans_set_field.py`

 * *Files identical despite different names*

### Comparing `aliyun-log-python-sdk-0.8.4/aliyun/log/etl_core/transform/condition_list.py` & `aliyun-log-python-sdk-0.8.5/aliyun/log/etl_core/transform/condition_list.py`

 * *Files identical despite different names*

### Comparing `aliyun-log-python-sdk-0.8.4/aliyun/log/etl_core/transform/condition_transform.py` & `aliyun-log-python-sdk-0.8.5/aliyun/log/etl_core/transform/condition_transform.py`

 * *Files identical despite different names*

### Comparing `aliyun-log-python-sdk-0.8.4/aliyun/log/etl_core/transform/condition_util.py` & `aliyun-log-python-sdk-0.8.5/aliyun/log/etl_core/transform/condition_util.py`

 * *Files identical despite different names*

### Comparing `aliyun-log-python-sdk-0.8.4/aliyun/log/etl_core/transform/transform_list.py` & `aliyun-log-python-sdk-0.8.5/aliyun/log/etl_core/transform/transform_list.py`

 * *Files identical despite different names*

### Comparing `aliyun-log-python-sdk-0.8.4/aliyun/log/etl_core/transform/transform_meta.py` & `aliyun-log-python-sdk-0.8.5/aliyun/log/etl_core/transform/transform_meta.py`

 * *Files identical despite different names*

### Comparing `aliyun-log-python-sdk-0.8.4/aliyun/log/export_response.py` & `aliyun-log-python-sdk-0.8.5/aliyun/log/export_response.py`

 * *Files identical despite different names*

### Comparing `aliyun-log-python-sdk-0.8.4/aliyun/log/ext/jupyter_magic.py` & `aliyun-log-python-sdk-0.8.5/aliyun/log/ext/jupyter_magic.py`

 * *Files identical despite different names*

### Comparing `aliyun-log-python-sdk-0.8.4/aliyun/log/ext/syslogclient.py` & `aliyun-log-python-sdk-0.8.5/aliyun/log/ext/syslogclient.py`

 * *Files identical despite different names*

### Comparing `aliyun-log-python-sdk-0.8.4/aliyun/log/external_store_config.py` & `aliyun-log-python-sdk-0.8.5/aliyun/log/external_store_config.py`

 * *Files identical despite different names*

### Comparing `aliyun-log-python-sdk-0.8.4/aliyun/log/external_store_config_response.py` & `aliyun-log-python-sdk-0.8.5/aliyun/log/external_store_config_response.py`

 * *Files identical despite different names*

### Comparing `aliyun-log-python-sdk-0.8.4/aliyun/log/getcontextlogsresponse.py` & `aliyun-log-python-sdk-0.8.5/aliyun/log/getcontextlogsresponse.py`

 * *Files identical despite different names*

### Comparing `aliyun-log-python-sdk-0.8.4/aliyun/log/gethistogramsrequest.py` & `aliyun-log-python-sdk-0.8.5/aliyun/log/gethistogramsrequest.py`

 * *Files identical despite different names*

### Comparing `aliyun-log-python-sdk-0.8.4/aliyun/log/gethistogramsresponse.py` & `aliyun-log-python-sdk-0.8.5/aliyun/log/gethistogramsresponse.py`

 * *Files identical despite different names*

### Comparing `aliyun-log-python-sdk-0.8.4/aliyun/log/getlogsrequest.py` & `aliyun-log-python-sdk-0.8.5/aliyun/log/getlogsrequest.py`

 * *Files identical despite different names*

### Comparing `aliyun-log-python-sdk-0.8.4/aliyun/log/getlogsresponse.py` & `aliyun-log-python-sdk-0.8.5/aliyun/log/getlogsresponse.py`

 * *Files identical despite different names*

### Comparing `aliyun-log-python-sdk-0.8.4/aliyun/log/histogram.py` & `aliyun-log-python-sdk-0.8.5/aliyun/log/histogram.py`

 * *Files identical despite different names*

### Comparing `aliyun-log-python-sdk-0.8.4/aliyun/log/index_config.py` & `aliyun-log-python-sdk-0.8.5/aliyun/log/index_config.py`

 * *Files identical despite different names*

### Comparing `aliyun-log-python-sdk-0.8.4/aliyun/log/index_config_response.py` & `aliyun-log-python-sdk-0.8.5/aliyun/log/index_config_response.py`

 * *Files identical despite different names*

### Comparing `aliyun-log-python-sdk-0.8.4/aliyun/log/ingestion_response.py` & `aliyun-log-python-sdk-0.8.5/aliyun/log/ingestion_response.py`

 * *Files identical despite different names*

### Comparing `aliyun-log-python-sdk-0.8.4/aliyun/log/job.py` & `aliyun-log-python-sdk-0.8.5/aliyun/log/job.py`

 * *Files identical despite different names*

### Comparing `aliyun-log-python-sdk-0.8.4/aliyun/log/listlogstoresresponse.py` & `aliyun-log-python-sdk-0.8.5/aliyun/log/listlogstoresresponse.py`

 * *Files identical despite different names*

### Comparing `aliyun-log-python-sdk-0.8.4/aliyun/log/listtopicsrequest.py` & `aliyun-log-python-sdk-0.8.5/aliyun/log/listtopicsrequest.py`

 * *Files identical despite different names*

### Comparing `aliyun-log-python-sdk-0.8.4/aliyun/log/listtopicsresponse.py` & `aliyun-log-python-sdk-0.8.5/aliyun/log/listtopicsresponse.py`

 * *Files identical despite different names*

### Comparing `aliyun-log-python-sdk-0.8.4/aliyun/log/log_logs_pb2.py` & `aliyun-log-python-sdk-0.8.5/aliyun/log/log_logs_pb2.py`

 * *Files identical despite different names*

### Comparing `aliyun-log-python-sdk-0.8.4/aliyun/log/log_logs_raw_pb2.py` & `aliyun-log-python-sdk-0.8.5/aliyun/log/log_logs_raw_pb2.py`

 * *Files identical despite different names*

### Comparing `aliyun-log-python-sdk-0.8.4/aliyun/log/logclient.py` & `aliyun-log-python-sdk-0.8.5/aliyun/log/logclient.py`

 * *Files 0% similar despite different names*

```diff
@@ -1152,15 +1152,15 @@
         :type append_meta: bool
         :param append_meta: allow to append meta info (server received time and IP for external IP to each received log)
 
         :type auto_split: bool
         :param auto_split: auto split shard, max_split_shard will be 64 by default is True
 
         :type max_split_shard: int
-        :param max_split_shard: max shard to split, up to 64
+        :param max_split_shard: max shard to split, up to 256
 
         :type preserve_storage: bool
         :param preserve_storage: if always persist data, TTL will be ignored.
 
         :type encrypt_conf: dict
         :param encrypt_conf :  following is a sample
         +       {
@@ -1179,16 +1179,14 @@
         :type mode: string
         :param mode: type of logstore, can be choose between lite and standard, default value standard
 
         :return: CreateLogStoreResponse
         
         :raise: LogException
         """
-        if auto_split and (max_split_shard <= 0 or max_split_shard >= 64):
-            max_split_shard = 64
         if preserve_storage:
             ttl = 3650
 
         params = {}
         resource = "/logstores"
         headers = {"x-log-bodyrawsize": '0', "Content-Type": "application/json"}
         body = {"logstoreName": logstore_name, "ttl": int(ttl), "shardCount": int(shard_count),
@@ -1299,15 +1297,15 @@
         :type append_meta: bool
         :param append_meta: allow to append meta info (server received time and IP for external IP to each received log)
 
         :type auto_split: bool
         :param auto_split: auto split shard, max_split_shard will be 64 by default is True
 
         :type max_split_shard: int
-        :param max_split_shard: max shard to split, up to 64
+        :param max_split_shard: max shard to split, up to 256
 
         :type preserve_storage: bool
         :param preserve_storage: if always persist data, TTL will be ignored.
 
         :type encrypt_conf: dict
         :param encrypt_conf :  following is a sample
 +                {
@@ -1343,16 +1341,14 @@
         if auto_split is None:
             auto_split = res.auto_split
         if append_meta is None:
             append_meta = res.append_meta
         if max_split_shard is None:
             max_split_shard = res.max_split_shard
 
-        if auto_split and (max_split_shard <= 0 or max_split_shard >= 64):
-            max_split_shard = 64
         if preserve_storage:
             ttl = 3650
 
         headers = {"x-log-bodyrawsize": '0', "Content-Type": "application/json"}
         params = {}
         resource = "/logstores/" + logstore_name
         body = {
@@ -3521,15 +3517,15 @@
         :type append_meta: bool
         :param append_meta: allow to append meta info (server received time and IP for external IP to each received log)
 
         :type auto_split: bool
         :param auto_split: auto split shard, max_split_shard will be 64 by default is True
 
         :type max_split_shard: int
-        :param max_split_shard: max shard to split, up to 64
+        :param max_split_shard: max shard to split, up to 256
 
         :type preserve_storage: bool
         :param preserve_storage: if always persist data, TTL will be ignored.
 
         :type encrypt_conf: dict
         :param encrypt_conf :  following is a sample
         +       {
@@ -3641,15 +3637,15 @@
         :type append_meta: bool
         :param append_meta: allow to append meta info (server received time and IP for external IP to each received log)
 
         :type auto_split: bool
         :param auto_split: auto split shard, max_split_shard will be 64 by default is True
 
         :type max_split_shard: int
-        :param max_split_shard: max shard to split, up to 64
+        :param max_split_shard: max shard to split, up to 256
 
         :type preserve_storage: bool
         :param preserve_storage: if always persist data, TTL will be ignored.
 
         :type encrypt_conf: dict
         :param encrypt_conf :  following is a sample
 +                {
```

### Comparing `aliyun-log-python-sdk-0.8.4/aliyun/log/logclient_core.py` & `aliyun-log-python-sdk-0.8.5/aliyun/log/logclient_core.py`

 * *Files identical despite different names*

### Comparing `aliyun-log-python-sdk-0.8.4/aliyun/log/logclient_operator.py` & `aliyun-log-python-sdk-0.8.5/aliyun/log/logclient_operator.py`

 * *Files identical despite different names*

### Comparing `aliyun-log-python-sdk-0.8.4/aliyun/log/logexception.py` & `aliyun-log-python-sdk-0.8.5/aliyun/log/logexception.py`

 * *Files identical despite different names*

### Comparing `aliyun-log-python-sdk-0.8.4/aliyun/log/logger_hanlder.py` & `aliyun-log-python-sdk-0.8.5/aliyun/log/logger_hanlder.py`

 * *Files identical despite different names*

### Comparing `aliyun-log-python-sdk-0.8.4/aliyun/log/logitem.py` & `aliyun-log-python-sdk-0.8.5/aliyun/log/logitem.py`

 * *Files identical despite different names*

### Comparing `aliyun-log-python-sdk-0.8.4/aliyun/log/logrequest.py` & `aliyun-log-python-sdk-0.8.5/aliyun/log/logrequest.py`

 * *Files identical despite different names*

### Comparing `aliyun-log-python-sdk-0.8.4/aliyun/log/logresponse.py` & `aliyun-log-python-sdk-0.8.5/aliyun/log/logresponse.py`

 * *Files identical despite different names*

### Comparing `aliyun-log-python-sdk-0.8.4/aliyun/log/logstore_config_response.py` & `aliyun-log-python-sdk-0.8.5/aliyun/log/logstore_config_response.py`

 * *Files identical despite different names*

### Comparing `aliyun-log-python-sdk-0.8.4/aliyun/log/logtail_config_detail.py` & `aliyun-log-python-sdk-0.8.5/aliyun/log/logtail_config_detail.py`

 * *Files identical despite different names*

### Comparing `aliyun-log-python-sdk-0.8.4/aliyun/log/logtail_config_response.py` & `aliyun-log-python-sdk-0.8.5/aliyun/log/logtail_config_response.py`

 * *Files identical despite different names*

### Comparing `aliyun-log-python-sdk-0.8.4/aliyun/log/machine_group_detail.py` & `aliyun-log-python-sdk-0.8.5/aliyun/log/machine_group_detail.py`

 * *Files identical despite different names*

### Comparing `aliyun-log-python-sdk-0.8.4/aliyun/log/machinegroup_response.py` & `aliyun-log-python-sdk-0.8.5/aliyun/log/machinegroup_response.py`

 * *Files identical despite different names*

### Comparing `aliyun-log-python-sdk-0.8.4/aliyun/log/odps_sink.py` & `aliyun-log-python-sdk-0.8.5/aliyun/log/odps_sink.py`

 * *Files identical despite different names*

### Comparing `aliyun-log-python-sdk-0.8.4/aliyun/log/oss_sink.py` & `aliyun-log-python-sdk-0.8.5/aliyun/log/oss_sink.py`

 * *Files identical despite different names*

### Comparing `aliyun-log-python-sdk-0.8.4/aliyun/log/pluralize.py` & `aliyun-log-python-sdk-0.8.5/aliyun/log/pluralize.py`

 * *Files identical despite different names*

### Comparing `aliyun-log-python-sdk-0.8.4/aliyun/log/project_response.py` & `aliyun-log-python-sdk-0.8.5/aliyun/log/project_response.py`

 * *Files identical despite different names*

### Comparing `aliyun-log-python-sdk-0.8.4/aliyun/log/pulllog_response.py` & `aliyun-log-python-sdk-0.8.5/aliyun/log/pulllog_response.py`

 * *Files identical despite different names*

### Comparing `aliyun-log-python-sdk-0.8.4/aliyun/log/putlogsrequest.py` & `aliyun-log-python-sdk-0.8.5/aliyun/log/putlogsrequest.py`

 * *Files identical despite different names*

### Comparing `aliyun-log-python-sdk-0.8.4/aliyun/log/putlogsresponse.py` & `aliyun-log-python-sdk-0.8.5/aliyun/log/putlogsresponse.py`

 * *Files identical despite different names*

### Comparing `aliyun-log-python-sdk-0.8.4/aliyun/log/queriedlog.py` & `aliyun-log-python-sdk-0.8.5/aliyun/log/queriedlog.py`

 * *Files identical despite different names*

### Comparing `aliyun-log-python-sdk-0.8.4/aliyun/log/resource_params.py` & `aliyun-log-python-sdk-0.8.5/aliyun/log/resource_params.py`

 * *Files identical despite different names*

### Comparing `aliyun-log-python-sdk-0.8.4/aliyun/log/resource_response.py` & `aliyun-log-python-sdk-0.8.5/aliyun/log/resource_response.py`

 * *Files identical despite different names*

### Comparing `aliyun-log-python-sdk-0.8.4/aliyun/log/shard_response.py` & `aliyun-log-python-sdk-0.8.5/aliyun/log/shard_response.py`

 * *Files identical despite different names*

### Comparing `aliyun-log-python-sdk-0.8.4/aliyun/log/shipper_config.py` & `aliyun-log-python-sdk-0.8.5/aliyun/log/shipper_config.py`

 * *Files identical despite different names*

### Comparing `aliyun-log-python-sdk-0.8.4/aliyun/log/shipper_response.py` & `aliyun-log-python-sdk-0.8.5/aliyun/log/shipper_response.py`

 * *Files identical despite different names*

### Comparing `aliyun-log-python-sdk-0.8.4/aliyun/log/sql_instance_response.py` & `aliyun-log-python-sdk-0.8.5/aliyun/log/sql_instance_response.py`

 * *Files identical despite different names*

### Comparing `aliyun-log-python-sdk-0.8.4/aliyun/log/substore_config_response.py` & `aliyun-log-python-sdk-0.8.5/aliyun/log/substore_config_response.py`

 * *Files identical despite different names*

### Comparing `aliyun-log-python-sdk-0.8.4/aliyun/log/topostore_params.py` & `aliyun-log-python-sdk-0.8.5/aliyun/log/topostore_params.py`

 * *Files identical despite different names*

### Comparing `aliyun-log-python-sdk-0.8.4/aliyun/log/topostore_response.py` & `aliyun-log-python-sdk-0.8.5/aliyun/log/topostore_response.py`

 * *Files identical despite different names*

### Comparing `aliyun-log-python-sdk-0.8.4/aliyun/log/util.py` & `aliyun-log-python-sdk-0.8.5/aliyun/log/util.py`

 * *Files identical despite different names*

### Comparing `aliyun-log-python-sdk-0.8.4/aliyun_log_python_sdk.egg-info/PKG-INFO` & `aliyun-log-python-sdk-0.8.5/aliyun_log_python_sdk.egg-info/PKG-INFO`

 * *Files 11% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: aliyun-log-python-sdk
-Version: 0.8.4
+Version: 0.8.5
 Summary: Aliyun log service Python client SDK
 Home-page: https://github.com/aliyun/aliyun-log-python-sdk
 Author: Aliyun
 Classifier: Development Status :: 5 - Production/Stable
 Classifier: License :: OSI Approved :: MIT License
 Classifier: Operating System :: OS Independent
 Classifier: Programming Language :: Python :: 2.6
```

### Comparing `aliyun-log-python-sdk-0.8.4/aliyun_log_python_sdk.egg-info/SOURCES.txt` & `aliyun-log-python-sdk-0.8.5/aliyun_log_python_sdk.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `aliyun-log-python-sdk-0.8.4/setup.py` & `aliyun-log-python-sdk-0.8.5/setup.py`

 * *Files identical despite different names*

