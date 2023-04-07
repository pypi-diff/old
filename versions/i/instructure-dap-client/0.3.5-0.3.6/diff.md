# Comparing `tmp/instructure-dap-client-0.3.5.tar.gz` & `tmp/instructure-dap-client-0.3.6.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "instructure-dap-client-0.3.5.tar", last modified: Wed Apr  5 14:08:30 2023, max compression
+gzip compressed data, was "instructure-dap-client-0.3.6.tar", last modified: Fri Apr  7 12:35:42 2023, max compression
```

## Comparing `instructure-dap-client-0.3.5.tar` & `instructure-dap-client-0.3.6.tar`

### file list

```diff
@@ -1,62 +1,62 @@
-drwxr-xr-x   0 levente.hunyadi   (503) staff       (20)        0 2023-04-05 14:08:30.113474 instructure-dap-client-0.3.5/
--rw-r--r--   0 levente.hunyadi   (503) staff       (20)     1079 2023-02-24 11:13:34.000000 instructure-dap-client-0.3.5/LICENSE
--rw-r--r--   0 levente.hunyadi   (503) staff       (20)    18491 2023-04-05 14:08:30.113746 instructure-dap-client-0.3.5/PKG-INFO
--rw-r--r--   0 levente.hunyadi   (503) staff       (20)    17692 2023-04-04 12:37:07.000000 instructure-dap-client-0.3.5/README.md
-drwxr-xr-x   0 levente.hunyadi   (503) staff       (20)        0 2023-04-05 14:08:30.092345 instructure-dap-client-0.3.5/dap/
--rw-r--r--   0 levente.hunyadi   (503) staff       (20)       22 2023-04-05 14:05:54.000000 instructure-dap-client-0.3.5/dap/__init__.py
--rw-r--r--   0 levente.hunyadi   (503) staff       (20)     4382 2023-04-04 13:12:06.000000 instructure-dap-client-0.3.5/dap/__main__.py
-drwxr-xr-x   0 levente.hunyadi   (503) staff       (20)        0 2023-04-05 14:08:30.094711 instructure-dap-client-0.3.5/dap/actions/
--rw-r--r--   0 levente.hunyadi   (503) staff       (20)        0 2023-03-30 13:59:23.000000 instructure-dap-client-0.3.5/dap/actions/__init__.py
--rw-r--r--   0 levente.hunyadi   (503) staff       (20)      961 2023-03-30 13:59:23.000000 instructure-dap-client-0.3.5/dap/actions/drop_db.py
--rw-r--r--   0 levente.hunyadi   (503) staff       (20)      565 2023-03-30 13:59:23.000000 instructure-dap-client-0.3.5/dap/actions/init_db.py
--rw-r--r--   0 levente.hunyadi   (503) staff       (20)      566 2023-03-30 13:59:23.000000 instructure-dap-client-0.3.5/dap/actions/sync_db.py
--rw-r--r--   0 levente.hunyadi   (503) staff       (20)    20570 2023-04-04 13:08:40.000000 instructure-dap-client-0.3.5/dap/api.py
--rw-r--r--   0 levente.hunyadi   (503) staff       (20)     2980 2023-03-31 08:29:45.000000 instructure-dap-client-0.3.5/dap/arguments.py
-drwxr-xr-x   0 levente.hunyadi   (503) staff       (20)        0 2023-04-05 14:08:30.101678 instructure-dap-client-0.3.5/dap/commands/
--rw-r--r--   0 levente.hunyadi   (503) staff       (20)        0 2023-02-24 11:13:34.000000 instructure-dap-client-0.3.5/dap/commands/__init__.py
--rw-r--r--   0 levente.hunyadi   (503) staff       (20)      450 2023-03-30 13:59:23.000000 instructure-dap-client-0.3.5/dap/commands/abstract_db_command.py
--rw-r--r--   0 levente.hunyadi   (503) staff       (20)     2011 2023-03-30 13:59:23.000000 instructure-dap-client-0.3.5/dap/commands/base.py
--rw-r--r--   0 levente.hunyadi   (503) staff       (20)     6751 2023-03-31 08:29:45.000000 instructure-dap-client-0.3.5/dap/commands/commands.py
--rw-r--r--   0 levente.hunyadi   (503) staff       (20)     2611 2023-03-31 08:29:45.000000 instructure-dap-client-0.3.5/dap/commands/commonargs.py
--rw-r--r--   0 levente.hunyadi   (503) staff       (20)      502 2023-03-30 13:59:23.000000 instructure-dap-client-0.3.5/dap/commands/dbargs.py
--rw-r--r--   0 levente.hunyadi   (503) staff       (20)     1175 2023-03-30 13:59:23.000000 instructure-dap-client-0.3.5/dap/commands/dropdb_command.py
--rw-r--r--   0 levente.hunyadi   (503) staff       (20)     1361 2023-03-30 13:59:23.000000 instructure-dap-client-0.3.5/dap/commands/initdb_command.py
--rw-r--r--   0 levente.hunyadi   (503) staff       (20)     1322 2023-03-30 13:59:23.000000 instructure-dap-client-0.3.5/dap/commands/queryargs.py
--rw-r--r--   0 levente.hunyadi   (503) staff       (20)     1695 2023-03-30 13:59:23.000000 instructure-dap-client-0.3.5/dap/commands/syncdb_command.py
--rw-r--r--   0 levente.hunyadi   (503) staff       (20)      889 2023-03-30 13:59:23.000000 instructure-dap-client-0.3.5/dap/commands/timestampargs.py
--rw-r--r--   0 levente.hunyadi   (503) staff       (20)     5056 2023-04-04 12:03:12.000000 instructure-dap-client-0.3.5/dap/concurrency.py
--rw-r--r--   0 levente.hunyadi   (503) staff       (20)     2920 2023-03-30 13:59:23.000000 instructure-dap-client-0.3.5/dap/dap_error.py
--rw-r--r--   0 levente.hunyadi   (503) staff       (20)    18455 2023-04-04 13:07:56.000000 instructure-dap-client-0.3.5/dap/dap_types.py
-drwxr-xr-x   0 levente.hunyadi   (503) staff       (20)        0 2023-04-05 14:08:30.106257 instructure-dap-client-0.3.5/dap/database/
--rw-r--r--   0 levente.hunyadi   (503) staff       (20)        0 2023-03-30 13:59:23.000000 instructure-dap-client-0.3.5/dap/database/__init__.py
--rw-r--r--   0 levente.hunyadi   (503) staff       (20)     2203 2023-03-30 13:59:23.000000 instructure-dap-client-0.3.5/dap/database/base_processor.py
--rw-r--r--   0 levente.hunyadi   (503) staff       (20)     2088 2023-03-30 13:59:23.000000 instructure-dap-client-0.3.5/dap/database/connection.py
--rw-r--r--   0 levente.hunyadi   (503) staff       (20)     1117 2023-03-30 13:59:23.000000 instructure-dap-client-0.3.5/dap/database/database_errors.py
--rw-r--r--   0 levente.hunyadi   (503) staff       (20)     6435 2023-04-05 14:04:38.000000 instructure-dap-client-0.3.5/dap/database/db_operations.py
--rw-r--r--   0 levente.hunyadi   (503) staff       (20)     2270 2023-04-05 14:04:38.000000 instructure-dap-client-0.3.5/dap/database/init_processor.py
--rw-r--r--   0 levente.hunyadi   (503) staff       (20)     2801 2023-03-30 13:59:23.000000 instructure-dap-client-0.3.5/dap/database/sync_processor.py
--rw-r--r--   0 levente.hunyadi   (503) staff       (20)     6090 2023-03-31 08:29:45.000000 instructure-dap-client-0.3.5/dap/downloader.py
--rw-r--r--   0 levente.hunyadi   (503) staff       (20)      669 2023-03-30 13:59:23.000000 instructure-dap-client-0.3.5/dap/log.py
-drwxr-xr-x   0 levente.hunyadi   (503) staff       (20)        0 2023-04-05 14:08:30.108129 instructure-dap-client-0.3.5/dap/model/
--rw-r--r--   0 levente.hunyadi   (503) staff       (20)        0 2023-02-24 11:13:34.000000 instructure-dap-client-0.3.5/dap/model/__init__.py
--rw-r--r--   0 levente.hunyadi   (503) staff       (20)     7683 2023-03-30 13:59:23.000000 instructure-dap-client-0.3.5/dap/model/meta_table.py
--rw-r--r--   0 levente.hunyadi   (503) staff       (20)     6184 2023-04-04 12:03:12.000000 instructure-dap-client-0.3.5/dap/model/metadata.py
--rw-r--r--   0 levente.hunyadi   (503) staff       (20)      850 2023-04-04 12:03:12.000000 instructure-dap-client-0.3.5/dap/networking.py
--rw-r--r--   0 levente.hunyadi   (503) staff       (20)     1353 2023-04-05 14:04:38.000000 instructure-dap-client-0.3.5/dap/payload.py
--rw-r--r--   0 levente.hunyadi   (503) staff       (20)      249 2023-03-30 13:59:23.000000 instructure-dap-client-0.3.5/dap/processing_error.py
-drwxr-xr-x   0 levente.hunyadi   (503) staff       (20)        0 2023-04-05 14:08:30.109293 instructure-dap-client-0.3.5/dap/replicator/
--rw-r--r--   0 levente.hunyadi   (503) staff       (20)        0 2023-03-30 14:59:52.000000 instructure-dap-client-0.3.5/dap/replicator/__init__.py
--rw-r--r--   0 levente.hunyadi   (503) staff       (20)     2454 2023-03-30 13:59:23.000000 instructure-dap-client-0.3.5/dap/replicator/sql.py
--rw-r--r--   0 levente.hunyadi   (503) staff       (20)     1450 2023-03-27 20:20:03.000000 instructure-dap-client-0.3.5/dap/timestamp.py
--rw-r--r--   0 levente.hunyadi   (503) staff       (20)     3682 2023-03-31 11:35:13.000000 instructure-dap-client-0.3.5/dap/type_conversion.py
-drwxr-xr-x   0 levente.hunyadi   (503) staff       (20)        0 2023-04-05 14:08:30.113010 instructure-dap-client-0.3.5/instructure_dap_client.egg-info/
--rw-r--r--   0 levente.hunyadi   (503) staff       (20)    18491 2023-04-05 14:08:30.000000 instructure-dap-client-0.3.5/instructure_dap_client.egg-info/PKG-INFO
--rw-r--r--   0 levente.hunyadi   (503) staff       (20)     1332 2023-04-05 14:08:30.000000 instructure-dap-client-0.3.5/instructure_dap_client.egg-info/SOURCES.txt
--rw-r--r--   0 levente.hunyadi   (503) staff       (20)        1 2023-04-05 14:08:30.000000 instructure-dap-client-0.3.5/instructure_dap_client.egg-info/dependency_links.txt
--rw-r--r--   0 levente.hunyadi   (503) staff       (20)       51 2023-04-05 14:08:30.000000 instructure-dap-client-0.3.5/instructure_dap_client.egg-info/entry_points.txt
--rw-r--r--   0 levente.hunyadi   (503) staff       (20)      151 2023-04-05 14:08:30.000000 instructure-dap-client-0.3.5/instructure_dap_client.egg-info/requires.txt
--rw-r--r--   0 levente.hunyadi   (503) staff       (20)        4 2023-04-05 14:08:30.000000 instructure-dap-client-0.3.5/instructure_dap_client.egg-info/top_level.txt
--rw-r--r--   0 levente.hunyadi   (503) staff       (20)        1 2023-04-05 14:08:29.000000 instructure-dap-client-0.3.5/instructure_dap_client.egg-info/zip-safe
--rw-r--r--   0 levente.hunyadi   (503) staff       (20)       94 2022-07-21 14:42:23.000000 instructure-dap-client-0.3.5/pyproject.toml
--rw-r--r--   0 levente.hunyadi   (503) staff       (20)     1170 2023-04-05 14:08:30.114792 instructure-dap-client-0.3.5/setup.cfg
--rw-r--r--   0 levente.hunyadi   (503) staff       (20)       69 2022-07-21 14:42:23.000000 instructure-dap-client-0.3.5/setup.py
+drwxr-xr-x   0 levente.hunyadi   (503) staff       (20)        0 2023-04-07 12:35:42.343059 instructure-dap-client-0.3.6/
+-rw-r--r--   0 levente.hunyadi   (503) staff       (20)     1079 2023-02-24 11:13:34.000000 instructure-dap-client-0.3.6/LICENSE
+-rw-r--r--   0 levente.hunyadi   (503) staff       (20)    18505 2023-04-07 12:35:42.343255 instructure-dap-client-0.3.6/PKG-INFO
+-rw-r--r--   0 levente.hunyadi   (503) staff       (20)    17706 2023-04-07 11:43:57.000000 instructure-dap-client-0.3.6/README.md
+drwxr-xr-x   0 levente.hunyadi   (503) staff       (20)        0 2023-04-07 12:35:42.321272 instructure-dap-client-0.3.6/dap/
+-rw-r--r--   0 levente.hunyadi   (503) staff       (20)       22 2023-04-07 12:35:01.000000 instructure-dap-client-0.3.6/dap/__init__.py
+-rw-r--r--   0 levente.hunyadi   (503) staff       (20)     4382 2023-04-04 13:12:06.000000 instructure-dap-client-0.3.6/dap/__main__.py
+drwxr-xr-x   0 levente.hunyadi   (503) staff       (20)        0 2023-04-07 12:35:42.323633 instructure-dap-client-0.3.6/dap/actions/
+-rw-r--r--   0 levente.hunyadi   (503) staff       (20)        0 2023-03-30 13:59:23.000000 instructure-dap-client-0.3.6/dap/actions/__init__.py
+-rw-r--r--   0 levente.hunyadi   (503) staff       (20)     1064 2023-04-07 11:43:57.000000 instructure-dap-client-0.3.6/dap/actions/drop_db.py
+-rw-r--r--   0 levente.hunyadi   (503) staff       (20)      572 2023-04-07 11:43:57.000000 instructure-dap-client-0.3.6/dap/actions/init_db.py
+-rw-r--r--   0 levente.hunyadi   (503) staff       (20)      573 2023-04-07 11:43:57.000000 instructure-dap-client-0.3.6/dap/actions/sync_db.py
+-rw-r--r--   0 levente.hunyadi   (503) staff       (20)    20570 2023-04-04 13:08:40.000000 instructure-dap-client-0.3.6/dap/api.py
+-rw-r--r--   0 levente.hunyadi   (503) staff       (20)     2980 2023-03-31 08:29:45.000000 instructure-dap-client-0.3.6/dap/arguments.py
+drwxr-xr-x   0 levente.hunyadi   (503) staff       (20)        0 2023-04-07 12:35:42.330824 instructure-dap-client-0.3.6/dap/commands/
+-rw-r--r--   0 levente.hunyadi   (503) staff       (20)        0 2023-02-24 11:13:34.000000 instructure-dap-client-0.3.6/dap/commands/__init__.py
+-rw-r--r--   0 levente.hunyadi   (503) staff       (20)      457 2023-04-07 11:43:57.000000 instructure-dap-client-0.3.6/dap/commands/abstract_db_command.py
+-rw-r--r--   0 levente.hunyadi   (503) staff       (20)     2011 2023-03-30 13:59:23.000000 instructure-dap-client-0.3.6/dap/commands/base.py
+-rw-r--r--   0 levente.hunyadi   (503) staff       (20)     6751 2023-03-31 08:29:45.000000 instructure-dap-client-0.3.6/dap/commands/commands.py
+-rw-r--r--   0 levente.hunyadi   (503) staff       (20)     2611 2023-03-31 08:29:45.000000 instructure-dap-client-0.3.6/dap/commands/commonargs.py
+-rw-r--r--   0 levente.hunyadi   (503) staff       (20)      502 2023-03-30 13:59:23.000000 instructure-dap-client-0.3.6/dap/commands/dbargs.py
+-rw-r--r--   0 levente.hunyadi   (503) staff       (20)     1175 2023-03-30 13:59:23.000000 instructure-dap-client-0.3.6/dap/commands/dropdb_command.py
+-rw-r--r--   0 levente.hunyadi   (503) staff       (20)     1361 2023-03-30 13:59:23.000000 instructure-dap-client-0.3.6/dap/commands/initdb_command.py
+-rw-r--r--   0 levente.hunyadi   (503) staff       (20)     1322 2023-03-30 13:59:23.000000 instructure-dap-client-0.3.6/dap/commands/queryargs.py
+-rw-r--r--   0 levente.hunyadi   (503) staff       (20)     1695 2023-03-30 13:59:23.000000 instructure-dap-client-0.3.6/dap/commands/syncdb_command.py
+-rw-r--r--   0 levente.hunyadi   (503) staff       (20)      889 2023-03-30 13:59:23.000000 instructure-dap-client-0.3.6/dap/commands/timestampargs.py
+-rw-r--r--   0 levente.hunyadi   (503) staff       (20)     5928 2023-04-07 11:43:57.000000 instructure-dap-client-0.3.6/dap/concurrency.py
+-rw-r--r--   0 levente.hunyadi   (503) staff       (20)     2920 2023-03-30 13:59:23.000000 instructure-dap-client-0.3.6/dap/dap_error.py
+-rw-r--r--   0 levente.hunyadi   (503) staff       (20)    18455 2023-04-04 13:07:56.000000 instructure-dap-client-0.3.6/dap/dap_types.py
+drwxr-xr-x   0 levente.hunyadi   (503) staff       (20)        0 2023-04-07 12:35:42.335472 instructure-dap-client-0.3.6/dap/database/
+-rw-r--r--   0 levente.hunyadi   (503) staff       (20)        0 2023-03-30 13:59:23.000000 instructure-dap-client-0.3.6/dap/database/__init__.py
+-rw-r--r--   0 levente.hunyadi   (503) staff       (20)     2316 2023-04-07 11:44:25.000000 instructure-dap-client-0.3.6/dap/database/base_processor.py
+-rw-r--r--   0 levente.hunyadi   (503) staff       (20)     2442 2023-04-07 11:44:25.000000 instructure-dap-client-0.3.6/dap/database/connection.py
+-rw-r--r--   0 levente.hunyadi   (503) staff       (20)     1121 2023-04-07 11:44:25.000000 instructure-dap-client-0.3.6/dap/database/database_errors.py
+-rw-r--r--   0 levente.hunyadi   (503) staff       (20)     3401 2023-04-07 11:43:57.000000 instructure-dap-client-0.3.6/dap/database/database_operations.py
+-rw-r--r--   0 levente.hunyadi   (503) staff       (20)     2720 2023-04-07 11:43:57.000000 instructure-dap-client-0.3.6/dap/database/init_processor.py
+-rw-r--r--   0 levente.hunyadi   (503) staff       (20)     3661 2023-04-07 11:43:57.000000 instructure-dap-client-0.3.6/dap/database/sync_processor.py
+-rw-r--r--   0 levente.hunyadi   (503) staff       (20)     5759 2023-04-07 11:44:25.000000 instructure-dap-client-0.3.6/dap/downloader.py
+-rw-r--r--   0 levente.hunyadi   (503) staff       (20)      669 2023-03-30 13:59:23.000000 instructure-dap-client-0.3.6/dap/log.py
+drwxr-xr-x   0 levente.hunyadi   (503) staff       (20)        0 2023-04-07 12:35:42.336969 instructure-dap-client-0.3.6/dap/model/
+-rw-r--r--   0 levente.hunyadi   (503) staff       (20)        0 2023-02-24 11:13:34.000000 instructure-dap-client-0.3.6/dap/model/__init__.py
+-rw-r--r--   0 levente.hunyadi   (503) staff       (20)     8026 2023-04-07 11:44:25.000000 instructure-dap-client-0.3.6/dap/model/meta_table.py
+-rw-r--r--   0 levente.hunyadi   (503) staff       (20)     6184 2023-04-04 12:03:12.000000 instructure-dap-client-0.3.6/dap/model/metadata.py
+-rw-r--r--   0 levente.hunyadi   (503) staff       (20)      850 2023-04-04 12:03:12.000000 instructure-dap-client-0.3.6/dap/networking.py
+-rw-r--r--   0 levente.hunyadi   (503) staff       (20)     1353 2023-04-05 14:04:38.000000 instructure-dap-client-0.3.6/dap/payload.py
+drwxr-xr-x   0 levente.hunyadi   (503) staff       (20)        0 2023-04-07 12:35:42.338161 instructure-dap-client-0.3.6/dap/replicator/
+-rw-r--r--   0 levente.hunyadi   (503) staff       (20)        0 2023-03-30 14:59:52.000000 instructure-dap-client-0.3.6/dap/replicator/__init__.py
+-rw-r--r--   0 levente.hunyadi   (503) staff       (20)     2550 2023-04-07 11:43:57.000000 instructure-dap-client-0.3.6/dap/replicator/sql.py
+-rw-r--r--   0 levente.hunyadi   (503) staff       (20)     1322 2023-04-07 11:43:57.000000 instructure-dap-client-0.3.6/dap/timer.py
+-rw-r--r--   0 levente.hunyadi   (503) staff       (20)     1450 2023-03-27 20:20:03.000000 instructure-dap-client-0.3.6/dap/timestamp.py
+-rw-r--r--   0 levente.hunyadi   (503) staff       (20)     2869 2023-04-07 11:43:57.000000 instructure-dap-client-0.3.6/dap/type_conversion.py
+drwxr-xr-x   0 levente.hunyadi   (503) staff       (20)        0 2023-04-07 12:35:42.342427 instructure-dap-client-0.3.6/instructure_dap_client.egg-info/
+-rw-r--r--   0 levente.hunyadi   (503) staff       (20)    18505 2023-04-07 12:35:42.000000 instructure-dap-client-0.3.6/instructure_dap_client.egg-info/PKG-INFO
+-rw-r--r--   0 levente.hunyadi   (503) staff       (20)     1327 2023-04-07 12:35:42.000000 instructure-dap-client-0.3.6/instructure_dap_client.egg-info/SOURCES.txt
+-rw-r--r--   0 levente.hunyadi   (503) staff       (20)        1 2023-04-07 12:35:42.000000 instructure-dap-client-0.3.6/instructure_dap_client.egg-info/dependency_links.txt
+-rw-r--r--   0 levente.hunyadi   (503) staff       (20)       51 2023-04-07 12:35:42.000000 instructure-dap-client-0.3.6/instructure_dap_client.egg-info/entry_points.txt
+-rw-r--r--   0 levente.hunyadi   (503) staff       (20)      151 2023-04-07 12:35:42.000000 instructure-dap-client-0.3.6/instructure_dap_client.egg-info/requires.txt
+-rw-r--r--   0 levente.hunyadi   (503) staff       (20)        4 2023-04-07 12:35:42.000000 instructure-dap-client-0.3.6/instructure_dap_client.egg-info/top_level.txt
+-rw-r--r--   0 levente.hunyadi   (503) staff       (20)        1 2023-04-07 12:35:41.000000 instructure-dap-client-0.3.6/instructure_dap_client.egg-info/zip-safe
+-rw-r--r--   0 levente.hunyadi   (503) staff       (20)       94 2022-07-21 14:42:23.000000 instructure-dap-client-0.3.6/pyproject.toml
+-rw-r--r--   0 levente.hunyadi   (503) staff       (20)     1170 2023-04-07 12:35:42.344222 instructure-dap-client-0.3.6/setup.cfg
+-rw-r--r--   0 levente.hunyadi   (503) staff       (20)       69 2022-07-21 14:42:23.000000 instructure-dap-client-0.3.6/setup.py
```

### Comparing `instructure-dap-client-0.3.5/LICENSE` & `instructure-dap-client-0.3.6/LICENSE`

 * *Files identical despite different names*

### Comparing `instructure-dap-client-0.3.5/PKG-INFO` & `instructure-dap-client-0.3.6/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: instructure-dap-client
-Version: 0.3.5
+Version: 0.3.6
 Summary: Data Access Platform client library
 Author: Levente Hunyadi
 Author-email: levente.hunyadi@instructure.com
 Maintainer: Edina Tipter
 Maintainer-email: edina.tipter@instructure.com
 License: MIT
 Classifier: Development Status :: 4 - Beta
@@ -299,27 +299,27 @@
 2. synchronize a database with the data in DAP.
 
 In order to replicate data in DAP locally, we must first initialize a database:
 
 ```python
 connection_string: str = "postgresql://scott:password@localhost/testdb"
 
-async with DatabaseConnection(connection_string) as db_connection:
+async with DatabaseConnection(connection_string).open() as db_connection:
     async with DAPClient(base_url, credentials) as session:
         await SQLReplicator(session, db_connection).initialize(namespace, table_name)
 ```
 
 Initialization creates a database schema for the DAP namespace, and  a corresponding database table for each DAP table. In addition, it creates a *meta-table*, which is a special database table that holds synchronization information, e.g. the last time the data was synchronized with DAP, and the schema version that the locally stored data conforms to. Finally, it issues a snapshot query to DAP API, and populates the database table with output returned by the snapshot query.
 
 ### Synchronizing data in a local database
 
 Once the table has been initialized, it can be kept up to date using the synchronize operation:
 
 ```python
-async with DatabaseConnection(connection_string) as db_connection:
+async with DatabaseConnection(connection_string).open() as db_connection:
     async with DAPClient(base_url, credentials) as session:
         await SQLReplicator(session, db_connection).synchronize(namespace, table_name)
 ```
 
 This inspects the information in the meta-table, and issues an incremental query to DAP API with a `since` timestamp corresponding to the last synchronization time. Based on the results of the incremental query, it inserts new records, updates existing records, and deletes records that have been added to, updated in, or removed from the DAP service.
 
 If the local schema version in the meta-table is identical to the remote schema version in DAP, inserting, updating and deleting records proceeds normally. However, if there is a mismatch, the table structure of the local database has to evolve to match the current structure of the data in DAP. This includes the following schema changes in the back-end:
```

### Comparing `instructure-dap-client-0.3.5/README.md` & `instructure-dap-client-0.3.6/README.md`

 * *Files 1% similar despite different names*

```diff
@@ -277,27 +277,27 @@
 2. synchronize a database with the data in DAP.
 
 In order to replicate data in DAP locally, we must first initialize a database:
 
 ```python
 connection_string: str = "postgresql://scott:password@localhost/testdb"
 
-async with DatabaseConnection(connection_string) as db_connection:
+async with DatabaseConnection(connection_string).open() as db_connection:
     async with DAPClient(base_url, credentials) as session:
         await SQLReplicator(session, db_connection).initialize(namespace, table_name)
 ```
 
 Initialization creates a database schema for the DAP namespace, and  a corresponding database table for each DAP table. In addition, it creates a *meta-table*, which is a special database table that holds synchronization information, e.g. the last time the data was synchronized with DAP, and the schema version that the locally stored data conforms to. Finally, it issues a snapshot query to DAP API, and populates the database table with output returned by the snapshot query.
 
 ### Synchronizing data in a local database
 
 Once the table has been initialized, it can be kept up to date using the synchronize operation:
 
 ```python
-async with DatabaseConnection(connection_string) as db_connection:
+async with DatabaseConnection(connection_string).open() as db_connection:
     async with DAPClient(base_url, credentials) as session:
         await SQLReplicator(session, db_connection).synchronize(namespace, table_name)
 ```
 
 This inspects the information in the meta-table, and issues an incremental query to DAP API with a `since` timestamp corresponding to the last synchronization time. Based on the results of the incremental query, it inserts new records, updates existing records, and deletes records that have been added to, updated in, or removed from the DAP service.
 
 If the local schema version in the meta-table is identical to the remote schema version in DAP, inserting, updating and deleting records proceeds normally. However, if there is a mismatch, the table structure of the local database has to evolve to match the current structure of the data in DAP. This includes the following schema changes in the back-end:
```

### Comparing `instructure-dap-client-0.3.5/dap/__main__.py` & `instructure-dap-client-0.3.6/dap/__main__.py`

 * *Files identical despite different names*

### Comparing `instructure-dap-client-0.3.5/dap/actions/drop_db.py` & `instructure-dap-client-0.3.6/dap/actions/drop_db.py`

 * *Files 9% similar despite different names*

```diff
@@ -1,21 +1,25 @@
 from sqlalchemy import Connection, Inspector, MetaData, Table, inspect
 
 from ..database.connection import DatabaseConnection
 from ..database.database_errors import NonExistingTableError
-from ..model.meta_table import MetatableManager
+from ..model.meta_table import MetaTableManager
 
 
 def _drop_table(db_connection: Connection, namespace: str, table_name: str) -> None:
     inspector: Inspector = inspect(db_connection)
     if not inspector.has_table(table_name=table_name, schema=namespace):
         raise NonExistingTableError(namespace, table_name)
 
     table_def = Table(table_name, MetaData(schema=namespace))
     table_def.drop(bind=db_connection)
 
 
 async def drop_db(connection_string: str, namespace: str, table_name: str) -> None:
-    async with DatabaseConnection(connection_string) as db_connection:
-        await db_connection.run_sync(lambda c: _drop_table(c, namespace, table_name))
-        await MetatableManager(db_connection, namespace, table_name).drop()
-        await db_connection.commit()
+    async with DatabaseConnection(connection_string).open() as db_connection:
+        async with db_connection.context() as conn:
+            await conn.run_sync(lambda c: _drop_table(c, namespace, table_name))
+
+        await MetaTableManager(db_connection, namespace, table_name).drop()
+
+        async with db_connection.context() as conn:
+            await conn.commit()
```

### Comparing `instructure-dap-client-0.3.5/dap/actions/init_db.py` & `instructure-dap-client-0.3.6/dap/actions/sync_db.py`

 * *Files 7% similar despite different names*

```diff
@@ -1,18 +1,18 @@
 from ..api import DAPClient
 from ..dap_types import Credentials
 from ..database.connection import DatabaseConnection
 from ..replicator.sql import SQLReplicator
 
 
-async def init_db(
+async def sync_db(
     base_url: str,
     credentials: Credentials,
     connection_string: str,
     namespace: str,
     table_name: str,
 ) -> None:
-    async with DatabaseConnection(connection_string) as db_connection:
+    async with DatabaseConnection(connection_string).open() as db_connection:
         async with DAPClient(base_url, credentials) as session:
-            await SQLReplicator(session, db_connection).initialize(
+            await SQLReplicator(session, db_connection).synchronize(
                 namespace, table_name
             )
```

### Comparing `instructure-dap-client-0.3.5/dap/actions/sync_db.py` & `instructure-dap-client-0.3.6/dap/actions/init_db.py`

 * *Files 25% similar despite different names*

```diff
@@ -1,18 +1,18 @@
 from ..api import DAPClient
 from ..dap_types import Credentials
 from ..database.connection import DatabaseConnection
 from ..replicator.sql import SQLReplicator
 
 
-async def sync_db(
+async def init_db(
     base_url: str,
     credentials: Credentials,
     connection_string: str,
     namespace: str,
     table_name: str,
 ) -> None:
-    async with DatabaseConnection(connection_string) as db_connection:
+    async with DatabaseConnection(connection_string).open() as db_connection:
         async with DAPClient(base_url, credentials) as session:
-            await SQLReplicator(session, db_connection).synchronize(
+            await SQLReplicator(session, db_connection).initialize(
                 namespace, table_name
             )
```

### Comparing `instructure-dap-client-0.3.5/dap/api.py` & `instructure-dap-client-0.3.6/dap/api.py`

 * *Files identical despite different names*

### Comparing `instructure-dap-client-0.3.5/dap/arguments.py` & `instructure-dap-client-0.3.6/dap/arguments.py`

 * *Files identical despite different names*

### Comparing `instructure-dap-client-0.3.5/dap/commands/base.py` & `instructure-dap-client-0.3.6/dap/commands/base.py`

 * *Files identical despite different names*

### Comparing `instructure-dap-client-0.3.5/dap/commands/commands.py` & `instructure-dap-client-0.3.6/dap/commands/commands.py`

 * *Files identical despite different names*

### Comparing `instructure-dap-client-0.3.5/dap/commands/commonargs.py` & `instructure-dap-client-0.3.6/dap/commands/commonargs.py`

 * *Files identical despite different names*

### Comparing `instructure-dap-client-0.3.5/dap/commands/dropdb_command.py` & `instructure-dap-client-0.3.6/dap/commands/dropdb_command.py`

 * *Files identical despite different names*

### Comparing `instructure-dap-client-0.3.5/dap/commands/initdb_command.py` & `instructure-dap-client-0.3.6/dap/commands/initdb_command.py`

 * *Files identical despite different names*

### Comparing `instructure-dap-client-0.3.5/dap/commands/queryargs.py` & `instructure-dap-client-0.3.6/dap/commands/queryargs.py`

 * *Files identical despite different names*

### Comparing `instructure-dap-client-0.3.5/dap/commands/syncdb_command.py` & `instructure-dap-client-0.3.6/dap/commands/syncdb_command.py`

 * *Files identical despite different names*

### Comparing `instructure-dap-client-0.3.5/dap/commands/timestampargs.py` & `instructure-dap-client-0.3.6/dap/commands/timestampargs.py`

 * *Files identical despite different names*

### Comparing `instructure-dap-client-0.3.5/dap/concurrency.py` & `instructure-dap-client-0.3.6/dap/concurrency.py`

 * *Files 13% similar despite different names*

```diff
@@ -31,26 +31,38 @@
     :raises asyncio.CancelledError: Raised when one of the tasks in cancelled.
     """
 
     iterator = iter(coroutines)
     pending = set(
         _make_task(coroutine) for _, coroutine in zip(range(concurrency), iterator)
     )
-    while pending:
-        done, pending = await asyncio.wait(pending, return_when=asyncio.FIRST_COMPLETED)
-
-        for task in done:
-            if task.cancelled():
-                raise asyncio.CancelledError
-            exc = task.exception()
-            if exc:
-                raise exc
-
-        for _, coroutine in zip(range(len(done)), iterator):
+    try:
+        while pending:
+            done, pending = await asyncio.wait(
+                pending, return_when=asyncio.FIRST_COMPLETED
+            )
+
+            for task in done:
+                if task.cancelled():
+                    raise asyncio.CancelledError
+                exc = task.exception()
+                if exc:
+                    raise exc
+
+            # schedule some tasks up to degree of concurrency
+            for _, coroutine in zip(range(len(done)), iterator):
+                pending.add(_make_task(coroutine))
+    finally:
+        # cancel remaining unscheduled tasks
+        for coroutine in iterator:
             pending.add(_make_task(coroutine))
+        if pending:
+            for task in pending:
+                task.cancel()
+            await asyncio.wait(pending)
 
 
 def _task_result(task: Task) -> Any:
     "Unwraps the result or exception from a task."
 
     exc = task.exception()
     if exc:
@@ -80,28 +92,43 @@
 
     tasks: List[Task] = []
     pending: Set[Task] = set()
     for _, coroutine in zip(range(concurrency), iterator):
         task = _make_task(coroutine)
         tasks.append(task)
         pending.add(task)
-    while pending:
-        done, pending = await asyncio.wait(pending, return_when=asyncio.FIRST_COMPLETED)
-
-        for task in done:
-            if task.cancelled():
-                raise asyncio.CancelledError
-            exc = task.exception()
-            if exc and not return_exceptions:
-                raise exc
 
-        for _, coroutine in zip(range(len(done)), iterator):
+    try:
+        while pending:
+            done, pending = await asyncio.wait(
+                pending, return_when=asyncio.FIRST_COMPLETED
+            )
+
+            for task in done:
+                if task.cancelled():
+                    raise asyncio.CancelledError
+                exc = task.exception()
+                if exc and not return_exceptions:
+                    raise exc
+
+            # schedule some tasks up to degree of concurrency
+            for _, coroutine in zip(range(len(done)), iterator):
+                task = _make_task(coroutine)
+                tasks.append(task)
+                pending.add(task)
+    finally:
+        # cancel remaining unscheduled tasks
+        for coroutine in iterator:
             task = _make_task(coroutine)
             tasks.append(task)
             pending.add(task)
+        if pending:
+            for task in pending:
+                task.cancel()
+            await asyncio.wait(pending)
 
     return (_task_result(task) for task in tasks)
 
 
 @overload
 async def gather_n(
     coroutines: List[Invokable[T]], *, concurrency: int, return_exceptions: bool = False
```

### Comparing `instructure-dap-client-0.3.5/dap/dap_error.py` & `instructure-dap-client-0.3.6/dap/dap_error.py`

 * *Files identical despite different names*

### Comparing `instructure-dap-client-0.3.5/dap/dap_types.py` & `instructure-dap-client-0.3.6/dap/dap_types.py`

 * *Files identical despite different names*

### Comparing `instructure-dap-client-0.3.5/dap/database/database_errors.py` & `instructure-dap-client-0.3.6/dap/database/database_errors.py`

 * *Files 17% similar despite different names*

```diff
@@ -25,12 +25,12 @@
 
 class DatabaseProtocolError(DatabaseError):
     """
     Raised when connection cannot be established with database due to invalid protocol issue.
     """
 
 
-class SchemaVersionMismatchError(Exception):
+class SchemaVersionMismatchError(DatabaseError):
     def __init__(self, expected_version: int, actual_version: int) -> None:
         super().__init__(
             f"schema version mismatch; expected: {expected_version}, got: {actual_version}"
         )
```

### Comparing `instructure-dap-client-0.3.5/dap/database/init_processor.py` & `instructure-dap-client-0.3.6/dap/database/init_processor.py`

 * *Files 24% similar despite different names*

```diff
@@ -1,19 +1,20 @@
-from typing import Tuple
+from types import TracebackType
+from typing import Optional, Tuple, Type
 
 from sqlalchemy import Connection, Inspector, Table, inspect
-from sqlalchemy.ext.asyncio import AsyncConnection
 from sqlalchemy.sql.ddl import CreateSchema
 
 from ..dap_types import VersionedSchema
-from ..database.db_operations import DBOperations
 from ..model.metadata import create_table_definition
 from ..type_conversion import JsonRecord, create_copy_converters
-from .base_processor import BaseInitProcessor, ContextAwareObject
+from .base_processor import BaseBatch, BaseInitProcessor, ContextAwareObject
+from .connection import DatabaseSession
 from .database_errors import TableAlreadyExistsError
+from .database_operations import DatabaseCopy
 
 
 def _create_tables(db_conn: Connection, table_def: Table) -> None:
     inspector: Inspector = inspect(db_conn)
 
     if inspector.has_table(table_def.name, table_def.schema):
         raise TableAlreadyExistsError(table_def.name, table_def.schema)
@@ -22,40 +23,61 @@
         db_conn.execute(CreateSchema(table_def.schema))  # type: ignore
 
     table_def.metadata.create_all(db_conn)
 
 
 class InitProcessor(BaseInitProcessor):
     """
-    Handles processing of data entries during initialization.
-    In `prepare` it creates table specified by `namespace` and `table_name`.
-    Then it passes JSON records towards `DBOperations.copy`.
-    Finally, it makes `DBOperations` flush it's content in `close` method.
+    Creates and populates an empty database table with records acquired from the DAP service.
     """
 
-    _db_connection: AsyncConnection
+    _db_connection: DatabaseSession
     _table_def: Table
-    _db_operations: DBOperations
     _converters: Tuple
 
     def __init__(
         self,
-        db_connection: AsyncConnection,
+        db_connection: DatabaseSession,
         namespace: str,
         table_name: str,
         table_schema: VersionedSchema,
     ) -> None:
         self._db_connection = db_connection
         self._table_def = create_table_definition(namespace, table_name, table_schema)
-        self._db_operations = DBOperations(db_connection, self._table_def)
         self._converters = create_copy_converters(self._table_def)
 
     async def prepare(self) -> None:
-        await self._db_connection.run_sync(lambda c: _create_tables(c, self._table_def))
+        async with self._db_connection.context() as conn:
+            await conn.run_sync(lambda c: _create_tables(c, self._table_def))
 
-    async def process(self, record: JsonRecord, obj: ContextAwareObject) -> None:
-        await self._db_operations.copy(
-            tuple(converter(record) for converter in self._converters), obj
+    def batch(self, obj: ContextAwareObject) -> BaseBatch:
+        return InitBatch(
+            DatabaseCopy(self._db_connection, self._table_def, obj), self._converters
         )
 
     async def close(self) -> None:
-        await self._db_operations.flush()
+        pass
+
+
+class InitBatch(BaseBatch):
+    _db_copy_op: DatabaseCopy
+    _converters: Tuple
+
+    def __init__(self, copy_op: DatabaseCopy, converters: Tuple) -> None:
+        self._db_copy_op = copy_op
+        self._converters = converters
+
+    async def process(self, record: JsonRecord) -> None:
+        await self._db_copy_op.process(
+            tuple(converter(record) for converter in self._converters)
+        )
+
+    async def __aenter__(self) -> "BaseBatch":
+        return self
+
+    async def __aexit__(
+        self,
+        exc_type: Optional[Type[BaseException]],
+        exc_val: Optional[BaseException],
+        exc_tb: Optional[TracebackType],
+    ) -> None:
+        await self._db_copy_op.flush()
```

### Comparing `instructure-dap-client-0.3.5/dap/downloader.py` & `instructure-dap-client-0.3.6/dap/downloader.py`

 * *Files 6% similar despite different names*

```diff
@@ -15,20 +15,15 @@
 )
 from .database.base_processor import (
     BaseInitProcessor,
     BaseSyncProcessor,
     ContextAwareObject,
 )
 from .payload import get_json_lines_from_gzip_stream
-from .processing_error import SchemaVersionMismatchError
-from .type_conversion import (
-    AbstractRecordVisitor,
-    JsonRecord,
-    process_resource_for_sync,
-)
+from .database.database_errors import SchemaVersionMismatchError
 
 CONCURRENCY: int = 4
 
 SnapshotDownloader = Callable[[BaseInitProcessor], Awaitable[None]]
 
 
 @dataclass(frozen=True)
@@ -98,36 +93,22 @@
         if len(resource_array) != 1:
             raise DownloadError("unable to get resource URLs for objects")
 
         logging.info(f"Downloading {obj}")
 
         resource = resource_array[0]
         async with self._session.stream_resource(resource) as stream:
-            async for record in get_json_lines_from_gzip_stream(stream):
-                await processor.process(record, obj)
+            async with processor.batch(obj) as batch:
+                async for record in get_json_lines_from_gzip_stream(stream):
+                    await batch.process(record)
 
 
 IncrementalDownloader = Callable[[BaseSyncProcessor], Awaitable[None]]
 
 
-class RecordVisitor(AbstractRecordVisitor):
-    obj: ContextAwareObject
-    processor: BaseSyncProcessor
-
-    def __init__(self, obj: ContextAwareObject, processor: BaseSyncProcessor) -> None:
-        self.obj = obj
-        self.processor = processor
-
-    async def upsert(self, record: JsonRecord) -> None:
-        await self.processor.process_upsert(record, self.obj)
-
-    async def delete(self, record: JsonRecord) -> None:
-        await self.processor.process_delete(record, self.obj)
-
-
 @dataclass(frozen=True)
 class IncrementalClient:
     table_data: GetTableDataResult
     table_schema: VersionedSchema
     download: IncrementalDownloader
 
 
@@ -178,14 +159,18 @@
         return IncrementalClient(
             download=download, table_data=table_data, table_schema=table_schema
         )
 
     async def _download_and_save(
         self, obj: ContextAwareObject, processor: BaseSyncProcessor
     ) -> None:
+        "Reads JSON records from a stream and makes them upserted or deleted via the processor."
+
         resource_array = await self._session.get_resources([Object(id=obj.id)])
         if len(resource_array) != 1:
             raise DownloadError("unable to get resource URLs for objects")
 
         resource = resource_array[0]
         async with self._session.stream_resource(resource) as stream:
-            await process_resource_for_sync(stream, RecordVisitor(obj, processor))
+            async with processor.batch(obj) as batch:
+                async for json_content in get_json_lines_from_gzip_stream(stream):
+                    await batch.process(json_content)
```

### Comparing `instructure-dap-client-0.3.5/dap/log.py` & `instructure-dap-client-0.3.6/dap/log.py`

 * *Files identical despite different names*

### Comparing `instructure-dap-client-0.3.5/dap/model/meta_table.py` & `instructure-dap-client-0.3.6/dap/model/meta_table.py`

 * *Files 5% similar despite different names*

```diff
@@ -1,19 +1,19 @@
 import json
 from datetime import datetime, timezone
 
 import sqlalchemy
-from sqlalchemy import bindparam, Connection, Inspector, inspect
-from sqlalchemy.ext.asyncio import AsyncConnection
+from sqlalchemy import Connection, Inspector, bindparam, inspect
 from sqlalchemy.sql.ddl import CreateSchema
 from strong_typing.core import JsonType, Schema
-from strong_typing.serialization import json_to_object, json_dump_string
+from strong_typing.serialization import json_dump_string, json_to_object
 
-from ..dap_types import VersionedSchema, GetTableDataResult
-from ..processing_error import SchemaVersionMismatchError
+from ..dap_types import GetTableDataResult, VersionedSchema
+from ..database.connection import DatabaseSession
+from ..database.database_errors import SchemaVersionMismatchError
 
 
 def _create_metatable_def(namespace: str) -> sqlalchemy.Table:
     metadata = sqlalchemy.MetaData(schema=namespace)
     metatable = sqlalchemy.Table(
         "dap_meta",
         metadata,
@@ -44,23 +44,25 @@
     versioned_schema: VersionedSchema
     metadata: sqlalchemy.MetaData
 
     @staticmethod
     async def load(
         namespace: str,
         table_name: str,
-        db_conn: AsyncConnection,
+        db_conn: DatabaseSession,
         metatable_def: sqlalchemy.Table,
     ) -> "_MetatableRecord":
-        result = await db_conn.execute(
-            metatable_def.select()
-            .where(metatable_def.c.namespace == namespace)
-            .where(metatable_def.c.source_table == table_name)
-        )
-        metatable_record = result.first()
+        async with db_conn.context() as conn:
+            result = await conn.execute(
+                metatable_def.select()
+                .where(metatable_def.c.namespace == namespace)
+                .where(metatable_def.c.source_table == table_name)
+            )
+            metatable_record = result.first()
+
         if metatable_record is None:
             raise NoMetadataError(namespace, table_name)
 
         schema_description_format: str = metatable_record._mapping[
             "schema_description_format"
         ]
         if schema_description_format != "json":
@@ -90,22 +92,22 @@
     ) -> None:
         self.namespace = namespace
         self.table_name = table_name
         self.versioned_schema = versioned_schema
         self.metadata = metadata
 
 
-class MetatableManager:
-    _db_connection: AsyncConnection
+class MetaTableManager:
+    _db_connection: DatabaseSession
     _namespace: str
     _table_name: str
     _metatable_def: sqlalchemy.Table
 
     def __init__(
-        self, db_connection: AsyncConnection, namespace: str, table_name: str
+        self, db_connection: DatabaseSession, namespace: str, table_name: str
     ) -> None:
         self._db_connection = db_connection
         self._namespace = namespace
         self._table_name = table_name
         self._metatable_def = _create_metatable_def(namespace)
 
     async def last_sync_datetime(self) -> datetime:
@@ -119,70 +121,75 @@
 
     async def initialize(
         self, table_schema: VersionedSchema, table_data: GetTableDataResult
     ) -> None:
         """
         Creates table in database schema and records an entry in it.
         """
-        await self._db_connection.run_sync(lambda c: self._create_tables(c))
-        await self._db_connection.execute(
-            self._metatable_def.insert(),
-            [
-                {
-                    "namespace": self._namespace,
-                    "source_table": self._table_name,
-                    "timestamp": table_data.timestamp.astimezone(
-                        tz=timezone.utc
-                    ).replace(tzinfo=None),
-                    "schema_version": table_data.schema_version,
-                    "target_schema": self._namespace,
-                    "target_table": self._table_name,
-                    "schema_description_format": "json",
-                    "schema_description": json_dump_string(table_schema.schema),
-                }
-            ],
-        )
+
+        async with self._db_connection.context() as conn:
+            await conn.run_sync(lambda c: self._create_tables(c))
+            await conn.execute(
+                self._metatable_def.insert(),
+                [
+                    {
+                        "namespace": self._namespace,
+                        "source_table": self._table_name,
+                        "timestamp": table_data.timestamp.astimezone(
+                            tz=timezone.utc
+                        ).replace(tzinfo=None),
+                        "schema_version": table_data.schema_version,
+                        "target_schema": self._namespace,
+                        "target_table": self._table_name,
+                        "schema_description_format": "json",
+                        "schema_description": json_dump_string(table_schema.schema),
+                    }
+                ],
+            )
 
     async def synchronize(self, table_data: GetTableDataResult) -> None:
         """
         Updates related record of meta table with recent table data.
         """
+
         await self._check_sync(table_data)
-        await self._db_connection.execute(
-            (
-                self._metatable_def.update()
-                .where(self._metatable_def.c.namespace == self._namespace)
-                .where(self._metatable_def.c.source_table == self._table_name)
-                .values(timestamp=bindparam("new_timestamp"))
-            ),
-            [
-                {
-                    "new_timestamp": table_data.timestamp.astimezone(
-                        timezone.utc
-                    ).replace(tzinfo=None)
-                }
-            ],
-        )
+        async with self._db_connection.context() as conn:
+            await conn.execute(
+                (
+                    self._metatable_def.update()
+                    .where(self._metatable_def.c.namespace == self._namespace)
+                    .where(self._metatable_def.c.source_table == self._table_name)
+                    .values(timestamp=bindparam("new_timestamp"))
+                ),
+                [
+                    {
+                        "new_timestamp": table_data.timestamp.astimezone(
+                            timezone.utc
+                        ).replace(tzinfo=None)
+                    }
+                ],
+            )
 
     async def _check_sync(self, table_data: GetTableDataResult) -> None:
         metatable_record = await _MetatableRecord.load(
             self._namespace, self._table_name, self._db_connection, self._metatable_def
         )
 
         if metatable_record.versioned_schema.version != table_data.schema_version:
             raise SchemaVersionMismatchError(
                 table_data.schema_version, metatable_record.versioned_schema.version
             )
 
     async def drop(self) -> None:
-        await self._db_connection.execute(
-            self._metatable_def.delete()
-            .where(self._metatable_def.c.namespace == self._namespace)
-            .where(self._metatable_def.c.source_table == self._table_name)
-        )
+        async with self._db_connection.context() as conn:
+            await conn.execute(
+                self._metatable_def.delete()
+                .where(self._metatable_def.c.namespace == self._namespace)
+                .where(self._metatable_def.c.source_table == self._table_name)
+            )
 
     def _create_tables(self, db_conn: Connection) -> None:
         inspector: Inspector = inspect(db_conn)
         if self._metatable_def.schema is not None and not inspector.has_schema(
             self._metatable_def.schema
         ):
             db_conn.execute(CreateSchema(self._metatable_def.schema))  # type: ignore
```

### Comparing `instructure-dap-client-0.3.5/dap/model/metadata.py` & `instructure-dap-client-0.3.6/dap/model/metadata.py`

 * *Files identical despite different names*

### Comparing `instructure-dap-client-0.3.5/dap/networking.py` & `instructure-dap-client-0.3.6/dap/networking.py`

 * *Files identical despite different names*

### Comparing `instructure-dap-client-0.3.5/dap/payload.py` & `instructure-dap-client-0.3.6/dap/payload.py`

 * *Files identical despite different names*

### Comparing `instructure-dap-client-0.3.5/dap/replicator/sql.py` & `instructure-dap-client-0.3.6/dap/replicator/sql.py`

 * *Files 13% similar despite different names*

```diff
@@ -1,25 +1,24 @@
 from typing import Optional
 
-from sqlalchemy.ext.asyncio import AsyncConnection
-
 from ..api import DAPSession
-from ..database.base_processor import BaseSyncProcessor, BaseInitProcessor
+from ..database.base_processor import BaseInitProcessor, BaseSyncProcessor
+from ..database.connection import DatabaseSession
 from ..database.init_processor import InitProcessor
 from ..database.sync_processor import SyncProcessor
 from ..downloader import IncrementalClientFactory, SnapshotClientFactory
-from ..model.meta_table import MetatableManager
+from ..model.meta_table import MetaTableManager
 
 
 class SQLReplicator:
     """
     Encapsulates logic that replicates changes acquired from DAP API in a SQL database.
     """
 
-    def __init__(self, session: DAPSession, connection: AsyncConnection) -> None:
+    def __init__(self, session: DAPSession, connection: DatabaseSession) -> None:
         self._session = session
         self._connection = connection
 
     async def initialize(
         self,
         namespace: str,
         table_name: str,
@@ -38,31 +37,32 @@
                 namespace=namespace,
                 table_name=table_name,
                 table_schema=client.table_schema,
             )
 
         await processor.prepare()
 
-        await MetatableManager(self._connection, namespace, table_name).initialize(
+        await MetaTableManager(self._connection, namespace, table_name).initialize(
             table_schema=client.table_schema, table_data=client.table_data
         )
 
         await client.download(processor)
 
-        await self._connection.commit()
+        async with self._connection.context() as conn:
+            await conn.commit()
 
     async def synchronize(
         self,
         namespace: str,
         table_name: str,
         processor: Optional[BaseSyncProcessor] = None,
     ) -> None:
-        metatable_manager = MetatableManager(self._connection, namespace, table_name)
+        meta_table_manager = MetaTableManager(self._connection, namespace, table_name)
 
-        since = await metatable_manager.last_sync_datetime()
+        since = await meta_table_manager.last_sync_datetime()
 
         client = await IncrementalClientFactory(
             self._session, namespace, table_name, since
         ).get_client()
 
         if processor is None:
             processor = SyncProcessor(
@@ -70,10 +70,12 @@
                 namespace=namespace,
                 table_name=table_name,
                 schema=client.table_schema,
             )
 
         await processor.prepare()
 
-        await metatable_manager.synchronize(client.table_data)
+        await meta_table_manager.synchronize(client.table_data)
         await client.download(processor)
-        await self._connection.commit()
+
+        async with self._connection.context() as conn:
+            await conn.commit()
```

### Comparing `instructure-dap-client-0.3.5/dap/timestamp.py` & `instructure-dap-client-0.3.6/dap/timestamp.py`

 * *Files identical despite different names*

### Comparing `instructure-dap-client-0.3.5/dap/type_conversion.py` & `instructure-dap-client-0.3.6/dap/type_conversion.py`

 * *Files 24% similar despite different names*

```diff
@@ -1,18 +1,15 @@
-import abc
 from typing import Any, Callable, Dict, Optional, Tuple, TypeVar
 
-import aiohttp
 from sqlalchemy import ARRAY, JSON, TIMESTAMP, BigInteger, Boolean, Column, Double
 from sqlalchemy import Enum as SqlEnum
 from sqlalchemy import Float, Integer, SmallInteger, String, Table
 from strong_typing.core import JsonType
 from strong_typing.serialization import json_dump_string
 
-from .payload import get_json_lines_from_gzip_stream
 from .timestamp import valid_naive_datetime
 
 T = TypeVar("T")
 
 JsonRecord = Dict[str, JsonType]
 
 
@@ -87,31 +84,7 @@
 def create_delete_converters(table_def: Table) -> ConverterDict:
     # create a tuple of converter objects for each column for DELETE records
     return {col.name: _get_column_converter(col) for col in table_def.primary_key}
 
 
 def create_copy_converters(table_def: Table) -> Tuple:
     return tuple(_get_column_converter(col) for col in table_def.columns)
-
-
-class AbstractRecordVisitor(abc.ABC):
-    "Base class for synchronization visitors that insert/update, or delete a record."
-
-    @abc.abstractmethod
-    async def upsert(self, record: JsonRecord) -> None:
-        ...
-
-    @abc.abstractmethod
-    async def delete(self, record: JsonRecord) -> None:
-        ...
-
-
-async def process_resource_for_sync(
-    stream: aiohttp.StreamReader, visitor: AbstractRecordVisitor
-) -> None:
-    "Reads JSON records from a stream and makes them upserted or deleted via the visitor."
-
-    async for json_content in get_json_lines_from_gzip_stream(stream):
-        if "value" in json_content:
-            await visitor.upsert(json_content)
-        else:
-            await visitor.delete(json_content)
```

### Comparing `instructure-dap-client-0.3.5/instructure_dap_client.egg-info/PKG-INFO` & `instructure-dap-client-0.3.6/instructure_dap_client.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: instructure-dap-client
-Version: 0.3.5
+Version: 0.3.6
 Summary: Data Access Platform client library
 Author: Levente Hunyadi
 Author-email: levente.hunyadi@instructure.com
 Maintainer: Edina Tipter
 Maintainer-email: edina.tipter@instructure.com
 License: MIT
 Classifier: Development Status :: 4 - Beta
@@ -299,27 +299,27 @@
 2. synchronize a database with the data in DAP.
 
 In order to replicate data in DAP locally, we must first initialize a database:
 
 ```python
 connection_string: str = "postgresql://scott:password@localhost/testdb"
 
-async with DatabaseConnection(connection_string) as db_connection:
+async with DatabaseConnection(connection_string).open() as db_connection:
     async with DAPClient(base_url, credentials) as session:
         await SQLReplicator(session, db_connection).initialize(namespace, table_name)
 ```
 
 Initialization creates a database schema for the DAP namespace, and  a corresponding database table for each DAP table. In addition, it creates a *meta-table*, which is a special database table that holds synchronization information, e.g. the last time the data was synchronized with DAP, and the schema version that the locally stored data conforms to. Finally, it issues a snapshot query to DAP API, and populates the database table with output returned by the snapshot query.
 
 ### Synchronizing data in a local database
 
 Once the table has been initialized, it can be kept up to date using the synchronize operation:
 
 ```python
-async with DatabaseConnection(connection_string) as db_connection:
+async with DatabaseConnection(connection_string).open() as db_connection:
     async with DAPClient(base_url, credentials) as session:
         await SQLReplicator(session, db_connection).synchronize(namespace, table_name)
 ```
 
 This inspects the information in the meta-table, and issues an incremental query to DAP API with a `since` timestamp corresponding to the last synchronization time. Based on the results of the incremental query, it inserts new records, updates existing records, and deletes records that have been added to, updated in, or removed from the DAP service.
 
 If the local schema version in the meta-table is identical to the remote schema version in DAP, inserting, updating and deleting records proceeds normally. However, if there is a mismatch, the table structure of the local database has to evolve to match the current structure of the data in DAP. This includes the following schema changes in the back-end:
```

### Comparing `instructure-dap-client-0.3.5/instructure_dap_client.egg-info/SOURCES.txt` & `instructure-dap-client-0.3.6/instructure_dap_client.egg-info/SOURCES.txt`

 * *Files 14% similar despite different names*

```diff
@@ -10,15 +10,15 @@
 dap/concurrency.py
 dap/dap_error.py
 dap/dap_types.py
 dap/downloader.py
 dap/log.py
 dap/networking.py
 dap/payload.py
-dap/processing_error.py
+dap/timer.py
 dap/timestamp.py
 dap/type_conversion.py
 dap/actions/__init__.py
 dap/actions/drop_db.py
 dap/actions/init_db.py
 dap/actions/sync_db.py
 dap/commands/__init__.py
@@ -32,15 +32,15 @@
 dap/commands/queryargs.py
 dap/commands/syncdb_command.py
 dap/commands/timestampargs.py
 dap/database/__init__.py
 dap/database/base_processor.py
 dap/database/connection.py
 dap/database/database_errors.py
-dap/database/db_operations.py
+dap/database/database_operations.py
 dap/database/init_processor.py
 dap/database/sync_processor.py
 dap/model/__init__.py
 dap/model/meta_table.py
 dap/model/metadata.py
 dap/replicator/__init__.py
 dap/replicator/sql.py
```

### Comparing `instructure-dap-client-0.3.5/setup.cfg` & `instructure-dap-client-0.3.6/setup.cfg`

 * *Files identical despite different names*

