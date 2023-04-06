# Comparing `tmp/lesscode-py-0.3.8.tar.gz` & `tmp/lesscode-py-0.3.9.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "dist/lesscode-py-0.3.8.tar", last modified: Thu Apr  6 10:54:24 2023, max compression
+gzip compressed data, was "dist/lesscode-py-0.3.9.tar", last modified: Thu Apr  6 11:34:35 2023, max compression
```

## Comparing `lesscode-py-0.3.8.tar` & `lesscode-py-0.3.9.tar`

### file list

```diff
@@ -1,137 +1,137 @@
-drwxr-xr-x   0 baai       (501) staff       (20)        0 2023-04-06 10:54:24.000000 lesscode-py-0.3.8/
--rw-r--r--   0 baai       (501) staff       (20)     8235 2023-04-06 10:54:24.000000 lesscode-py-0.3.8/PKG-INFO
--rw-r--r--   0 baai       (501) staff       (20)     7735 2023-01-10 01:37:52.000000 lesscode-py-0.3.8/README.md
-drwxr-xr-x   0 baai       (501) staff       (20)        0 2023-04-06 10:54:24.000000 lesscode-py-0.3.8/bin/
--rw-r--r--   0 baai       (501) staff       (20)        0 2022-12-07 01:03:51.000000 lesscode-py-0.3.8/bin/__init__.py
--rwxr-xr-x   0 baai       (501) staff       (20)     6921 2023-02-08 00:54:15.000000 lesscode-py-0.3.8/bin/lesscode.py
-drwxr-xr-x   0 baai       (501) staff       (20)        0 2023-04-06 10:54:24.000000 lesscode-py-0.3.8/lesscode/
--rw-r--r--   0 baai       (501) staff       (20)        0 2022-03-02 04:02:57.000000 lesscode-py-0.3.8/lesscode/__init__.py
-drwxr-xr-x   0 baai       (501) staff       (20)        0 2023-04-06 10:54:24.000000 lesscode-py-0.3.8/lesscode/db/
--rw-r--r--   0 baai       (501) staff       (20)        0 2022-03-02 04:02:57.000000 lesscode-py-0.3.8/lesscode/db/__init__.py
--rw-r--r--   0 baai       (501) staff       (20)      570 2022-03-14 03:20:03.000000 lesscode-py-0.3.8/lesscode/db/base_connection_pool.py
--rw-r--r--   0 baai       (501) staff       (20)     9011 2022-08-26 08:57:53.000000 lesscode-py-0.3.8/lesscode/db/base_sql_helper.py
--rw-r--r--   0 baai       (501) staff       (20)     6271 2022-03-08 03:18:23.000000 lesscode-py-0.3.8/lesscode/db/condition_wrapper.py
--rw-r--r--   0 baai       (501) staff       (20)     1093 2022-03-02 04:02:57.000000 lesscode-py-0.3.8/lesscode/db/connection_info.py
--rw-r--r--   0 baai       (501) staff       (20)      232 2022-03-02 04:02:57.000000 lesscode-py-0.3.8/lesscode/db/db_function.py
--rw-r--r--   0 baai       (501) staff       (20)     7783 2023-03-15 08:14:11.000000 lesscode-py-0.3.8/lesscode/db/ds_helper.py
-drwxr-xr-x   0 baai       (501) staff       (20)        0 2023-04-06 10:54:24.000000 lesscode-py-0.3.8/lesscode/db/elasticsearch/
--rw-r--r--   0 baai       (501) staff       (20)        0 2022-03-02 04:02:57.000000 lesscode-py-0.3.8/lesscode/db/elasticsearch/__init__.py
--rw-r--r--   0 baai       (501) staff       (20)    28228 2022-04-21 10:07:48.000000 lesscode-py-0.3.8/lesscode/db/elasticsearch/elasticsearch_helper.py
--rw-r--r--   0 baai       (501) staff       (20)     1134 2022-03-14 08:18:46.000000 lesscode-py-0.3.8/lesscode/db/elasticsearch/elasticsearch_pool.py
-drwxr-xr-x   0 baai       (501) staff       (20)        0 2023-04-06 10:54:24.000000 lesscode-py-0.3.8/lesscode/db/es/
--rw-r--r--   0 baai       (501) staff       (20)        0 2022-03-02 04:02:57.000000 lesscode-py-0.3.8/lesscode/db/es/__init__.py
--rw-r--r--   0 baai       (501) staff       (20)    22060 2023-04-06 10:54:20.000000 lesscode-py-0.3.8/lesscode/db/es/es_helper.py
--rw-r--r--   0 baai       (501) staff       (20)      953 2022-03-14 08:38:27.000000 lesscode-py-0.3.8/lesscode/db/es/es_pool.py
--rw-r--r--   0 baai       (501) staff       (20)     4704 2023-03-30 02:52:57.000000 lesscode-py-0.3.8/lesscode/db/es/es_request.py
--rw-r--r--   0 baai       (501) staff       (20)    12086 2023-02-28 01:04:29.000000 lesscode-py-0.3.8/lesscode/db/init_connection_pool.py
-drwxr-xr-x   0 baai       (501) staff       (20)        0 2023-04-06 10:54:24.000000 lesscode-py-0.3.8/lesscode/db/mongodb/
--rw-r--r--   0 baai       (501) staff       (20)        0 2022-03-02 04:02:57.000000 lesscode-py-0.3.8/lesscode/db/mongodb/__init__.py
--rw-r--r--   0 baai       (501) staff       (20)    18632 2022-08-16 01:45:52.000000 lesscode-py-0.3.8/lesscode/db/mongodb/mongodb_helper.py
--rw-r--r--   0 baai       (501) staff       (20)     1940 2022-06-06 00:45:03.000000 lesscode-py-0.3.8/lesscode/db/mongodb/mongodb_pool.py
-drwxr-xr-x   0 baai       (501) staff       (20)        0 2023-04-06 10:54:24.000000 lesscode-py-0.3.8/lesscode/db/mysql/
--rw-r--r--   0 baai       (501) staff       (20)        0 2022-03-02 04:02:57.000000 lesscode-py-0.3.8/lesscode/db/mysql/__init__.py
--rw-r--r--   0 baai       (501) staff       (20)     5593 2022-07-14 01:16:33.000000 lesscode-py-0.3.8/lesscode/db/mysql/mysql_helper.py
--rw-r--r--   0 baai       (501) staff       (20)     1943 2022-07-07 02:40:37.000000 lesscode-py-0.3.8/lesscode/db/mysql/mysql_pool.py
-drwxr-xr-x   0 baai       (501) staff       (20)        0 2023-04-06 10:54:24.000000 lesscode-py-0.3.8/lesscode/db/mysql_sqlalchemy/
--rw-r--r--   0 baai       (501) staff       (20)      996 2022-04-20 03:58:45.000000 lesscode-py-0.3.8/lesscode/db/mysql_sqlalchemy/SqlAlchemy.py
--rw-r--r--   0 baai       (501) staff       (20)        0 2022-04-18 10:45:21.000000 lesscode-py-0.3.8/lesscode/db/mysql_sqlalchemy/__init__.py
--rw-r--r--   0 baai       (501) staff       (20)      850 2022-06-23 03:51:47.000000 lesscode-py-0.3.8/lesscode/db/mysql_sqlalchemy/mysql_sqlalchemy_pool.py
-drwxr-xr-x   0 baai       (501) staff       (20)        0 2023-04-06 10:54:24.000000 lesscode-py-0.3.8/lesscode/db/nebula/
--rw-r--r--   0 baai       (501) staff       (20)        0 2023-02-28 01:04:29.000000 lesscode-py-0.3.8/lesscode/db/nebula/__init__.py
--rw-r--r--   0 baai       (501) staff       (20)     7219 2023-03-23 06:07:18.000000 lesscode-py-0.3.8/lesscode/db/nebula/nebula_helper.py
--rw-r--r--   0 baai       (501) staff       (20)     1868 2023-03-01 05:33:17.000000 lesscode-py-0.3.8/lesscode/db/nebula/nebula_pool.py
-drwxr-xr-x   0 baai       (501) staff       (20)        0 2023-04-06 10:54:24.000000 lesscode-py-0.3.8/lesscode/db/neo4j/
--rw-r--r--   0 baai       (501) staff       (20)        0 2022-03-02 04:02:57.000000 lesscode-py-0.3.8/lesscode/db/neo4j/__init__.py
--rw-r--r--   0 baai       (501) staff       (20)    49480 2023-02-28 01:04:29.000000 lesscode-py-0.3.8/lesscode/db/neo4j/neo4j_helper.py
--rw-r--r--   0 baai       (501) staff       (20)      973 2022-12-19 02:35:02.000000 lesscode-py-0.3.8/lesscode/db/neo4j/neo4j_pool.py
--rw-r--r--   0 baai       (501) staff       (20)      995 2022-04-16 02:10:07.000000 lesscode-py-0.3.8/lesscode/db/page.py
-drwxr-xr-x   0 baai       (501) staff       (20)        0 2023-04-06 10:54:24.000000 lesscode-py-0.3.8/lesscode/db/postgresql/
--rw-r--r--   0 baai       (501) staff       (20)        0 2022-03-02 04:02:57.000000 lesscode-py-0.3.8/lesscode/db/postgresql/__init__.py
--rw-r--r--   0 baai       (501) staff       (20)     6659 2022-05-19 02:32:47.000000 lesscode-py-0.3.8/lesscode/db/postgresql/postgresql_helper.py
--rw-r--r--   0 baai       (501) staff       (20)     1198 2022-05-19 02:09:25.000000 lesscode-py-0.3.8/lesscode/db/postgresql/postgresql_pool.py
-drwxr-xr-x   0 baai       (501) staff       (20)        0 2023-04-06 10:54:24.000000 lesscode-py-0.3.8/lesscode/db/redis/
--rw-r--r--   0 baai       (501) staff       (20)        0 2022-03-02 04:02:57.000000 lesscode-py-0.3.8/lesscode/db/redis/__init__.py
--rw-r--r--   0 baai       (501) staff       (20)     7297 2023-02-28 01:04:29.000000 lesscode-py-0.3.8/lesscode/db/redis/redis_helper.py
--rw-r--r--   0 baai       (501) staff       (20)     1209 2022-04-12 06:38:46.000000 lesscode-py-0.3.8/lesscode/db/redis/redis_pool.py
--rw-r--r--   0 baai       (501) staff       (20)    14050 2022-08-01 09:14:55.000000 lesscode-py-0.3.8/lesscode/db/relational_db_helper.py
-drwxr-xr-x   0 baai       (501) staff       (20)        0 2023-04-06 10:54:24.000000 lesscode-py-0.3.8/lesscode/db/sqlalchemy/
--rw-r--r--   0 baai       (501) staff       (20)        0 2022-08-03 09:11:29.000000 lesscode-py-0.3.8/lesscode/db/sqlalchemy/__init__.py
--rw-r--r--   0 baai       (501) staff       (20)     2831 2023-03-31 13:31:12.000000 lesscode-py-0.3.8/lesscode/db/sqlalchemy/sqlalchemy_helper.py
--rw-r--r--   0 baai       (501) staff       (20)     2306 2022-08-18 08:21:28.000000 lesscode-py-0.3.8/lesscode/db/sqlalchemy/sqlalchemy_pool.py
-drwxr-xr-x   0 baai       (501) staff       (20)        0 2023-04-06 10:54:24.000000 lesscode-py-0.3.8/lesscode/extend_handlers/
--rw-r--r--   0 baai       (501) staff       (20)        0 2022-06-06 01:16:54.000000 lesscode-py-0.3.8/lesscode/extend_handlers/__init__.py
-drwxr-xr-x   0 baai       (501) staff       (20)        0 2023-04-06 10:54:24.000000 lesscode-py-0.3.8/lesscode/extend_handlers/doc/
--rw-r--r--   0 baai       (501) staff       (20)        0 2022-06-06 02:07:06.000000 lesscode-py-0.3.8/lesscode/extend_handlers/doc/__init__.py
--rw-r--r--   0 baai       (501) staff       (20)     1819 2023-02-08 02:37:00.000000 lesscode-py-0.3.8/lesscode/extend_handlers/doc/swagger_interface_doc_handler.py
--rw-r--r--   0 baai       (501) staff       (20)     2067 2022-12-22 08:48:13.000000 lesscode-py-0.3.8/lesscode/extend_handlers/not_found_handler.py
-drwxr-xr-x   0 baai       (501) staff       (20)        0 2023-04-06 10:54:24.000000 lesscode-py-0.3.8/lesscode/mq/
--rw-r--r--   0 baai       (501) staff       (20)      110 2022-08-23 06:39:09.000000 lesscode-py-0.3.8/lesscode/mq/__init__.py
-drwxr-xr-x   0 baai       (501) staff       (20)        0 2023-04-06 10:54:24.000000 lesscode-py-0.3.8/lesscode/mq/kafka/
--rw-r--r--   0 baai       (501) staff       (20)      110 2022-08-24 02:10:15.000000 lesscode-py-0.3.8/lesscode/mq/kafka/__init__.py
--rw-r--r--   0 baai       (501) staff       (20)     2812 2022-08-25 09:55:37.000000 lesscode-py-0.3.8/lesscode/mq/kafka/kafka_helper.py
-drwxr-xr-x   0 baai       (501) staff       (20)        0 2023-04-06 10:54:24.000000 lesscode-py-0.3.8/lesscode/mq/rabbitmq/
--rw-r--r--   0 baai       (501) staff       (20)      110 2022-08-23 06:39:32.000000 lesscode-py-0.3.8/lesscode/mq/rabbitmq/__init__.py
--rw-r--r--   0 baai       (501) staff       (20)     2674 2022-08-24 01:34:31.000000 lesscode-py-0.3.8/lesscode/mq/rabbitmq/rabbitmq_helper.py
-drwxr-xr-x   0 baai       (501) staff       (20)        0 2023-04-06 10:54:24.000000 lesscode-py-0.3.8/lesscode/task/
--rw-r--r--   0 baai       (501) staff       (20)        0 2022-07-01 07:54:56.000000 lesscode-py-0.3.8/lesscode/task/__init__.py
--rw-r--r--   0 baai       (501) staff       (20)     3975 2022-07-01 08:36:04.000000 lesscode-py-0.3.8/lesscode/task/task_helper.py
-drwxr-xr-x   0 baai       (501) staff       (20)        0 2023-04-06 10:54:24.000000 lesscode-py-0.3.8/lesscode/utils/
--rw-r--r--   0 baai       (501) staff       (20)     2794 2023-02-20 02:34:15.000000 lesscode-py-0.3.8/lesscode/utils/CacheUtil.py
--rw-r--r--   0 baai       (501) staff       (20)     9684 2023-04-06 10:52:25.000000 lesscode-py-0.3.8/lesscode/utils/EsUtil.py
--rw-r--r--   0 baai       (501) staff       (20)      304 2022-06-07 09:54:57.000000 lesscode-py-0.3.8/lesscode/utils/JsonUtil.py
--rw-r--r--   0 baai       (501) staff       (20)     2012 2023-03-09 02:41:17.000000 lesscode-py-0.3.8/lesscode/utils/MongodbUtil.py
--rw-r--r--   0 baai       (501) staff       (20)      718 2022-04-24 03:03:42.000000 lesscode-py-0.3.8/lesscode/utils/ThreadUtil.py
--rw-r--r--   0 baai       (501) staff       (20)       35 2022-04-18 10:45:21.000000 lesscode-py-0.3.8/lesscode/utils/__init__.py
--rw-r--r--   0 baai       (501) staff       (20)     3066 2023-03-09 02:41:06.000000 lesscode-py-0.3.8/lesscode/utils/business.py
-drwxr-xr-x   0 baai       (501) staff       (20)        0 2023-04-06 10:54:24.000000 lesscode-py-0.3.8/lesscode/utils/chart/
--rw-r--r--   0 baai       (501) staff       (20)      121 2023-02-15 02:40:26.000000 lesscode-py-0.3.8/lesscode/utils/chart/__init__.py
--rw-r--r--   0 baai       (501) staff       (20)     9706 2023-03-09 08:04:16.000000 lesscode-py-0.3.8/lesscode/utils/chart/common2chart.py
--rw-r--r--   0 baai       (501) staff       (20)     4647 2023-02-15 02:29:13.000000 lesscode-py-0.3.8/lesscode/utils/chart/es2chart.py
--rw-r--r--   0 baai       (501) staff       (20)        0 2023-02-10 05:53:19.000000 lesscode-py-0.3.8/lesscode/utils/chart/mongo2chart.py
--rw-r--r--   0 baai       (501) staff       (20)        0 2023-02-10 05:53:33.000000 lesscode-py-0.3.8/lesscode/utils/chart/mysql2chart.py
--rw-r--r--   0 baai       (501) staff       (20)        0 2023-02-10 05:54:05.000000 lesscode-py-0.3.8/lesscode/utils/chart/neo4j2chart.py
--rw-r--r--   0 baai       (501) staff       (20)      812 2023-04-06 08:24:19.000000 lesscode-py-0.3.8/lesscode/utils/common.py
-drwxr-xr-x   0 baai       (501) staff       (20)        0 2023-04-06 10:54:24.000000 lesscode-py-0.3.8/lesscode/utils/doc/
--rw-r--r--   0 baai       (501) staff       (20)        0 2022-04-27 05:04:57.000000 lesscode-py-0.3.8/lesscode/utils/doc/__init__.py
--rw-r--r--   0 baai       (501) staff       (20)     6339 2022-12-22 08:05:26.000000 lesscode-py-0.3.8/lesscode/utils/doc/interface_doc_handler.py
--rw-r--r--   0 baai       (501) staff       (20)     3148 2022-04-19 02:49:20.000000 lesscode-py-0.3.8/lesscode/utils/encryption.py
-drwxr-xr-x   0 baai       (501) staff       (20)        0 2023-04-06 10:54:24.000000 lesscode-py-0.3.8/lesscode/utils/encryption_algorithm/
--rw-r--r--   0 baai       (501) staff       (20)      226 2022-04-19 02:49:20.000000 lesscode-py-0.3.8/lesscode/utils/encryption_algorithm/__init__.py
--rw-r--r--   0 baai       (501) staff       (20)     1532 2022-04-29 06:56:37.000000 lesscode-py-0.3.8/lesscode/utils/encryption_algorithm/aes.py
--rw-r--r--   0 baai       (501) staff       (20)      403 2022-04-18 10:45:21.000000 lesscode-py-0.3.8/lesscode/utils/encryption_algorithm/base64.py
--rw-r--r--   0 baai       (501) staff       (20)      826 2022-04-18 11:33:08.000000 lesscode-py-0.3.8/lesscode/utils/encryption_algorithm/des.py
--rw-r--r--   0 baai       (501) staff       (20)      363 2022-04-18 11:12:14.000000 lesscode-py-0.3.8/lesscode/utils/encryption_algorithm/hmac.py
--rw-r--r--   0 baai       (501) staff       (20)      203 2022-04-18 10:45:21.000000 lesscode-py-0.3.8/lesscode/utils/encryption_algorithm/md5.py
--rw-r--r--   0 baai       (501) staff       (20)     1222 2022-04-18 10:45:21.000000 lesscode-py-0.3.8/lesscode/utils/encryption_algorithm/rsa.py
--rw-r--r--   0 baai       (501) staff       (20)      205 2022-04-18 10:45:21.000000 lesscode-py-0.3.8/lesscode/utils/encryption_algorithm/sha1.py
--rw-r--r--   0 baai       (501) staff       (20)      209 2022-04-18 10:45:21.000000 lesscode-py-0.3.8/lesscode/utils/encryption_algorithm/sha256.py
--rw-r--r--   0 baai       (501) staff       (20)     2828 2022-04-19 02:20:10.000000 lesscode-py-0.3.8/lesscode/utils/encryption_algorithm/smx.py
-drwxr-xr-x   0 baai       (501) staff       (20)        0 2023-04-06 10:54:24.000000 lesscode-py-0.3.8/lesscode/utils/es_log/
--rw-r--r--   0 baai       (501) staff       (20)      110 2022-11-07 08:36:53.000000 lesscode-py-0.3.8/lesscode/utils/es_log/__init__.py
--rw-r--r--   0 baai       (501) staff       (20)     2397 2023-04-04 06:30:29.000000 lesscode-py-0.3.8/lesscode/utils/es_log/record_log.py
--rw-r--r--   0 baai       (501) staff       (20)      534 2022-04-21 09:20:15.000000 lesscode-py-0.3.8/lesscode/utils/json.py
-drwxr-xr-x   0 baai       (501) staff       (20)        0 2023-04-06 10:54:24.000000 lesscode-py-0.3.8/lesscode/utils/oss/
--rw-r--r--   0 baai       (501) staff       (20)        0 2022-05-09 01:28:27.000000 lesscode-py-0.3.8/lesscode/utils/oss/__init__.py
--rw-r--r--   0 baai       (501) staff       (20)     7613 2023-04-04 07:52:17.000000 lesscode-py-0.3.8/lesscode/utils/oss/ks3_oss.py
--rw-r--r--   0 baai       (501) staff       (20)    13164 2023-03-02 11:15:37.000000 lesscode-py-0.3.8/lesscode/utils/request.py
--rw-r--r--   0 baai       (501) staff       (20)     1461 2022-04-24 03:28:39.000000 lesscode-py-0.3.8/lesscode/utils/thread_task.py
--rw-r--r--   0 baai       (501) staff       (20)     1776 2022-08-10 03:37:58.000000 lesscode-py-0.3.8/lesscode/utils/upms_util.py
--rw-r--r--   0 baai       (501) staff       (20)     2335 2022-12-15 08:19:45.000000 lesscode-py-0.3.8/lesscode/utils/wrapper.py
--rw-r--r--   0 baai       (501) staff       (20)      198 2023-04-06 10:54:20.000000 lesscode-py-0.3.8/lesscode/version.py
-drwxr-xr-x   0 baai       (501) staff       (20)        0 2023-04-06 10:54:24.000000 lesscode-py-0.3.8/lesscode/web/
--rw-r--r--   0 baai       (501) staff       (20)        0 2022-03-02 04:02:57.000000 lesscode-py-0.3.8/lesscode/web/__init__.py
--rw-r--r--   0 baai       (501) staff       (20)    17305 2023-03-31 11:49:59.000000 lesscode-py-0.3.8/lesscode/web/base_handler.py
--rw-r--r--   0 baai       (501) staff       (20)      399 2022-03-02 04:02:57.000000 lesscode-py-0.3.8/lesscode/web/business_exception.py
--rw-r--r--   0 baai       (501) staff       (20)     2986 2022-11-10 08:39:11.000000 lesscode-py-0.3.8/lesscode/web/native_handler.py
--rw-r--r--   0 baai       (501) staff       (20)      772 2022-03-02 04:02:57.000000 lesscode-py-0.3.8/lesscode/web/response_result.py
--rw-r--r--   0 baai       (501) staff       (20)     8186 2022-12-22 08:05:26.000000 lesscode-py-0.3.8/lesscode/web/router_mapping.py
--rw-r--r--   0 baai       (501) staff       (20)     7624 2023-03-13 03:09:17.000000 lesscode-py-0.3.8/lesscode/web/status_code.py
--rw-r--r--   0 baai       (501) staff       (20)    15120 2023-04-06 03:31:11.000000 lesscode-py-0.3.8/lesscode/web/web_server.py
-drwxr-xr-x   0 baai       (501) staff       (20)        0 2023-04-06 10:54:24.000000 lesscode-py-0.3.8/lesscode_py.egg-info/
--rw-r--r--   0 baai       (501) staff       (20)     8235 2023-04-06 10:54:24.000000 lesscode-py-0.3.8/lesscode_py.egg-info/PKG-INFO
--rw-r--r--   0 baai       (501) staff       (20)     3565 2023-04-06 10:54:24.000000 lesscode-py-0.3.8/lesscode_py.egg-info/SOURCES.txt
--rw-r--r--   0 baai       (501) staff       (20)        1 2023-04-06 10:54:24.000000 lesscode-py-0.3.8/lesscode_py.egg-info/dependency_links.txt
--rw-r--r--   0 baai       (501) staff       (20)      388 2023-04-06 10:54:24.000000 lesscode-py-0.3.8/lesscode_py.egg-info/requires.txt
--rw-r--r--   0 baai       (501) staff       (20)       13 2023-04-06 10:54:24.000000 lesscode-py-0.3.8/lesscode_py.egg-info/top_level.txt
--rw-r--r--   0 baai       (501) staff       (20)       38 2023-04-06 10:54:24.000000 lesscode-py-0.3.8/setup.cfg
--rw-r--r--   0 baai       (501) staff       (20)     2637 2023-03-31 13:33:31.000000 lesscode-py-0.3.8/setup.py
+drwxr-xr-x   0 baai       (501) staff       (20)        0 2023-04-06 11:34:35.000000 lesscode-py-0.3.9/
+-rw-r--r--   0 baai       (501) staff       (20)     8235 2023-04-06 11:34:35.000000 lesscode-py-0.3.9/PKG-INFO
+-rw-r--r--   0 baai       (501) staff       (20)     7735 2023-01-10 01:37:52.000000 lesscode-py-0.3.9/README.md
+drwxr-xr-x   0 baai       (501) staff       (20)        0 2023-04-06 11:34:35.000000 lesscode-py-0.3.9/bin/
+-rw-r--r--   0 baai       (501) staff       (20)        0 2022-12-07 01:03:51.000000 lesscode-py-0.3.9/bin/__init__.py
+-rwxr-xr-x   0 baai       (501) staff       (20)     6921 2023-02-08 00:54:15.000000 lesscode-py-0.3.9/bin/lesscode.py
+drwxr-xr-x   0 baai       (501) staff       (20)        0 2023-04-06 11:34:35.000000 lesscode-py-0.3.9/lesscode/
+-rw-r--r--   0 baai       (501) staff       (20)        0 2022-03-02 04:02:57.000000 lesscode-py-0.3.9/lesscode/__init__.py
+drwxr-xr-x   0 baai       (501) staff       (20)        0 2023-04-06 11:34:35.000000 lesscode-py-0.3.9/lesscode/db/
+-rw-r--r--   0 baai       (501) staff       (20)        0 2022-03-02 04:02:57.000000 lesscode-py-0.3.9/lesscode/db/__init__.py
+-rw-r--r--   0 baai       (501) staff       (20)      570 2022-03-14 03:20:03.000000 lesscode-py-0.3.9/lesscode/db/base_connection_pool.py
+-rw-r--r--   0 baai       (501) staff       (20)     9011 2022-08-26 08:57:53.000000 lesscode-py-0.3.9/lesscode/db/base_sql_helper.py
+-rw-r--r--   0 baai       (501) staff       (20)     6271 2022-03-08 03:18:23.000000 lesscode-py-0.3.9/lesscode/db/condition_wrapper.py
+-rw-r--r--   0 baai       (501) staff       (20)     1093 2022-03-02 04:02:57.000000 lesscode-py-0.3.9/lesscode/db/connection_info.py
+-rw-r--r--   0 baai       (501) staff       (20)      232 2022-03-02 04:02:57.000000 lesscode-py-0.3.9/lesscode/db/db_function.py
+-rw-r--r--   0 baai       (501) staff       (20)     7783 2023-03-15 08:14:11.000000 lesscode-py-0.3.9/lesscode/db/ds_helper.py
+drwxr-xr-x   0 baai       (501) staff       (20)        0 2023-04-06 11:34:35.000000 lesscode-py-0.3.9/lesscode/db/elasticsearch/
+-rw-r--r--   0 baai       (501) staff       (20)        0 2022-03-02 04:02:57.000000 lesscode-py-0.3.9/lesscode/db/elasticsearch/__init__.py
+-rw-r--r--   0 baai       (501) staff       (20)    28228 2022-04-21 10:07:48.000000 lesscode-py-0.3.9/lesscode/db/elasticsearch/elasticsearch_helper.py
+-rw-r--r--   0 baai       (501) staff       (20)     1134 2022-03-14 08:18:46.000000 lesscode-py-0.3.9/lesscode/db/elasticsearch/elasticsearch_pool.py
+drwxr-xr-x   0 baai       (501) staff       (20)        0 2023-04-06 11:34:35.000000 lesscode-py-0.3.9/lesscode/db/es/
+-rw-r--r--   0 baai       (501) staff       (20)        0 2022-03-02 04:02:57.000000 lesscode-py-0.3.9/lesscode/db/es/__init__.py
+-rw-r--r--   0 baai       (501) staff       (20)    22081 2023-04-06 11:34:31.000000 lesscode-py-0.3.9/lesscode/db/es/es_helper.py
+-rw-r--r--   0 baai       (501) staff       (20)      953 2022-03-14 08:38:27.000000 lesscode-py-0.3.9/lesscode/db/es/es_pool.py
+-rw-r--r--   0 baai       (501) staff       (20)     4704 2023-03-30 02:52:57.000000 lesscode-py-0.3.9/lesscode/db/es/es_request.py
+-rw-r--r--   0 baai       (501) staff       (20)    12086 2023-02-28 01:04:29.000000 lesscode-py-0.3.9/lesscode/db/init_connection_pool.py
+drwxr-xr-x   0 baai       (501) staff       (20)        0 2023-04-06 11:34:35.000000 lesscode-py-0.3.9/lesscode/db/mongodb/
+-rw-r--r--   0 baai       (501) staff       (20)        0 2022-03-02 04:02:57.000000 lesscode-py-0.3.9/lesscode/db/mongodb/__init__.py
+-rw-r--r--   0 baai       (501) staff       (20)    18632 2022-08-16 01:45:52.000000 lesscode-py-0.3.9/lesscode/db/mongodb/mongodb_helper.py
+-rw-r--r--   0 baai       (501) staff       (20)     1940 2022-06-06 00:45:03.000000 lesscode-py-0.3.9/lesscode/db/mongodb/mongodb_pool.py
+drwxr-xr-x   0 baai       (501) staff       (20)        0 2023-04-06 11:34:35.000000 lesscode-py-0.3.9/lesscode/db/mysql/
+-rw-r--r--   0 baai       (501) staff       (20)        0 2022-03-02 04:02:57.000000 lesscode-py-0.3.9/lesscode/db/mysql/__init__.py
+-rw-r--r--   0 baai       (501) staff       (20)     5593 2022-07-14 01:16:33.000000 lesscode-py-0.3.9/lesscode/db/mysql/mysql_helper.py
+-rw-r--r--   0 baai       (501) staff       (20)     1943 2022-07-07 02:40:37.000000 lesscode-py-0.3.9/lesscode/db/mysql/mysql_pool.py
+drwxr-xr-x   0 baai       (501) staff       (20)        0 2023-04-06 11:34:35.000000 lesscode-py-0.3.9/lesscode/db/mysql_sqlalchemy/
+-rw-r--r--   0 baai       (501) staff       (20)      996 2022-04-20 03:58:45.000000 lesscode-py-0.3.9/lesscode/db/mysql_sqlalchemy/SqlAlchemy.py
+-rw-r--r--   0 baai       (501) staff       (20)        0 2022-04-18 10:45:21.000000 lesscode-py-0.3.9/lesscode/db/mysql_sqlalchemy/__init__.py
+-rw-r--r--   0 baai       (501) staff       (20)      850 2022-06-23 03:51:47.000000 lesscode-py-0.3.9/lesscode/db/mysql_sqlalchemy/mysql_sqlalchemy_pool.py
+drwxr-xr-x   0 baai       (501) staff       (20)        0 2023-04-06 11:34:35.000000 lesscode-py-0.3.9/lesscode/db/nebula/
+-rw-r--r--   0 baai       (501) staff       (20)        0 2023-02-28 01:04:29.000000 lesscode-py-0.3.9/lesscode/db/nebula/__init__.py
+-rw-r--r--   0 baai       (501) staff       (20)     7219 2023-03-23 06:07:18.000000 lesscode-py-0.3.9/lesscode/db/nebula/nebula_helper.py
+-rw-r--r--   0 baai       (501) staff       (20)     1868 2023-03-01 05:33:17.000000 lesscode-py-0.3.9/lesscode/db/nebula/nebula_pool.py
+drwxr-xr-x   0 baai       (501) staff       (20)        0 2023-04-06 11:34:35.000000 lesscode-py-0.3.9/lesscode/db/neo4j/
+-rw-r--r--   0 baai       (501) staff       (20)        0 2022-03-02 04:02:57.000000 lesscode-py-0.3.9/lesscode/db/neo4j/__init__.py
+-rw-r--r--   0 baai       (501) staff       (20)    49480 2023-02-28 01:04:29.000000 lesscode-py-0.3.9/lesscode/db/neo4j/neo4j_helper.py
+-rw-r--r--   0 baai       (501) staff       (20)      973 2022-12-19 02:35:02.000000 lesscode-py-0.3.9/lesscode/db/neo4j/neo4j_pool.py
+-rw-r--r--   0 baai       (501) staff       (20)      995 2022-04-16 02:10:07.000000 lesscode-py-0.3.9/lesscode/db/page.py
+drwxr-xr-x   0 baai       (501) staff       (20)        0 2023-04-06 11:34:35.000000 lesscode-py-0.3.9/lesscode/db/postgresql/
+-rw-r--r--   0 baai       (501) staff       (20)        0 2022-03-02 04:02:57.000000 lesscode-py-0.3.9/lesscode/db/postgresql/__init__.py
+-rw-r--r--   0 baai       (501) staff       (20)     6659 2022-05-19 02:32:47.000000 lesscode-py-0.3.9/lesscode/db/postgresql/postgresql_helper.py
+-rw-r--r--   0 baai       (501) staff       (20)     1198 2022-05-19 02:09:25.000000 lesscode-py-0.3.9/lesscode/db/postgresql/postgresql_pool.py
+drwxr-xr-x   0 baai       (501) staff       (20)        0 2023-04-06 11:34:35.000000 lesscode-py-0.3.9/lesscode/db/redis/
+-rw-r--r--   0 baai       (501) staff       (20)        0 2022-03-02 04:02:57.000000 lesscode-py-0.3.9/lesscode/db/redis/__init__.py
+-rw-r--r--   0 baai       (501) staff       (20)     7297 2023-02-28 01:04:29.000000 lesscode-py-0.3.9/lesscode/db/redis/redis_helper.py
+-rw-r--r--   0 baai       (501) staff       (20)     1209 2022-04-12 06:38:46.000000 lesscode-py-0.3.9/lesscode/db/redis/redis_pool.py
+-rw-r--r--   0 baai       (501) staff       (20)    14050 2022-08-01 09:14:55.000000 lesscode-py-0.3.9/lesscode/db/relational_db_helper.py
+drwxr-xr-x   0 baai       (501) staff       (20)        0 2023-04-06 11:34:35.000000 lesscode-py-0.3.9/lesscode/db/sqlalchemy/
+-rw-r--r--   0 baai       (501) staff       (20)        0 2022-08-03 09:11:29.000000 lesscode-py-0.3.9/lesscode/db/sqlalchemy/__init__.py
+-rw-r--r--   0 baai       (501) staff       (20)     2831 2023-03-31 13:31:12.000000 lesscode-py-0.3.9/lesscode/db/sqlalchemy/sqlalchemy_helper.py
+-rw-r--r--   0 baai       (501) staff       (20)     2306 2022-08-18 08:21:28.000000 lesscode-py-0.3.9/lesscode/db/sqlalchemy/sqlalchemy_pool.py
+drwxr-xr-x   0 baai       (501) staff       (20)        0 2023-04-06 11:34:35.000000 lesscode-py-0.3.9/lesscode/extend_handlers/
+-rw-r--r--   0 baai       (501) staff       (20)        0 2022-06-06 01:16:54.000000 lesscode-py-0.3.9/lesscode/extend_handlers/__init__.py
+drwxr-xr-x   0 baai       (501) staff       (20)        0 2023-04-06 11:34:35.000000 lesscode-py-0.3.9/lesscode/extend_handlers/doc/
+-rw-r--r--   0 baai       (501) staff       (20)        0 2022-06-06 02:07:06.000000 lesscode-py-0.3.9/lesscode/extend_handlers/doc/__init__.py
+-rw-r--r--   0 baai       (501) staff       (20)     1819 2023-02-08 02:37:00.000000 lesscode-py-0.3.9/lesscode/extend_handlers/doc/swagger_interface_doc_handler.py
+-rw-r--r--   0 baai       (501) staff       (20)     2067 2022-12-22 08:48:13.000000 lesscode-py-0.3.9/lesscode/extend_handlers/not_found_handler.py
+drwxr-xr-x   0 baai       (501) staff       (20)        0 2023-04-06 11:34:35.000000 lesscode-py-0.3.9/lesscode/mq/
+-rw-r--r--   0 baai       (501) staff       (20)      110 2022-08-23 06:39:09.000000 lesscode-py-0.3.9/lesscode/mq/__init__.py
+drwxr-xr-x   0 baai       (501) staff       (20)        0 2023-04-06 11:34:35.000000 lesscode-py-0.3.9/lesscode/mq/kafka/
+-rw-r--r--   0 baai       (501) staff       (20)      110 2022-08-24 02:10:15.000000 lesscode-py-0.3.9/lesscode/mq/kafka/__init__.py
+-rw-r--r--   0 baai       (501) staff       (20)     2812 2022-08-25 09:55:37.000000 lesscode-py-0.3.9/lesscode/mq/kafka/kafka_helper.py
+drwxr-xr-x   0 baai       (501) staff       (20)        0 2023-04-06 11:34:35.000000 lesscode-py-0.3.9/lesscode/mq/rabbitmq/
+-rw-r--r--   0 baai       (501) staff       (20)      110 2022-08-23 06:39:32.000000 lesscode-py-0.3.9/lesscode/mq/rabbitmq/__init__.py
+-rw-r--r--   0 baai       (501) staff       (20)     2674 2022-08-24 01:34:31.000000 lesscode-py-0.3.9/lesscode/mq/rabbitmq/rabbitmq_helper.py
+drwxr-xr-x   0 baai       (501) staff       (20)        0 2023-04-06 11:34:35.000000 lesscode-py-0.3.9/lesscode/task/
+-rw-r--r--   0 baai       (501) staff       (20)        0 2022-07-01 07:54:56.000000 lesscode-py-0.3.9/lesscode/task/__init__.py
+-rw-r--r--   0 baai       (501) staff       (20)     3975 2022-07-01 08:36:04.000000 lesscode-py-0.3.9/lesscode/task/task_helper.py
+drwxr-xr-x   0 baai       (501) staff       (20)        0 2023-04-06 11:34:35.000000 lesscode-py-0.3.9/lesscode/utils/
+-rw-r--r--   0 baai       (501) staff       (20)     2794 2023-02-20 02:34:15.000000 lesscode-py-0.3.9/lesscode/utils/CacheUtil.py
+-rw-r--r--   0 baai       (501) staff       (20)     9684 2023-04-06 10:52:25.000000 lesscode-py-0.3.9/lesscode/utils/EsUtil.py
+-rw-r--r--   0 baai       (501) staff       (20)      304 2022-06-07 09:54:57.000000 lesscode-py-0.3.9/lesscode/utils/JsonUtil.py
+-rw-r--r--   0 baai       (501) staff       (20)     2012 2023-03-09 02:41:17.000000 lesscode-py-0.3.9/lesscode/utils/MongodbUtil.py
+-rw-r--r--   0 baai       (501) staff       (20)      718 2022-04-24 03:03:42.000000 lesscode-py-0.3.9/lesscode/utils/ThreadUtil.py
+-rw-r--r--   0 baai       (501) staff       (20)       35 2022-04-18 10:45:21.000000 lesscode-py-0.3.9/lesscode/utils/__init__.py
+-rw-r--r--   0 baai       (501) staff       (20)     3066 2023-03-09 02:41:06.000000 lesscode-py-0.3.9/lesscode/utils/business.py
+drwxr-xr-x   0 baai       (501) staff       (20)        0 2023-04-06 11:34:35.000000 lesscode-py-0.3.9/lesscode/utils/chart/
+-rw-r--r--   0 baai       (501) staff       (20)      121 2023-02-15 02:40:26.000000 lesscode-py-0.3.9/lesscode/utils/chart/__init__.py
+-rw-r--r--   0 baai       (501) staff       (20)     9706 2023-03-09 08:04:16.000000 lesscode-py-0.3.9/lesscode/utils/chart/common2chart.py
+-rw-r--r--   0 baai       (501) staff       (20)     4647 2023-02-15 02:29:13.000000 lesscode-py-0.3.9/lesscode/utils/chart/es2chart.py
+-rw-r--r--   0 baai       (501) staff       (20)        0 2023-02-10 05:53:19.000000 lesscode-py-0.3.9/lesscode/utils/chart/mongo2chart.py
+-rw-r--r--   0 baai       (501) staff       (20)        0 2023-02-10 05:53:33.000000 lesscode-py-0.3.9/lesscode/utils/chart/mysql2chart.py
+-rw-r--r--   0 baai       (501) staff       (20)        0 2023-02-10 05:54:05.000000 lesscode-py-0.3.9/lesscode/utils/chart/neo4j2chart.py
+-rw-r--r--   0 baai       (501) staff       (20)      812 2023-04-06 08:24:19.000000 lesscode-py-0.3.9/lesscode/utils/common.py
+drwxr-xr-x   0 baai       (501) staff       (20)        0 2023-04-06 11:34:35.000000 lesscode-py-0.3.9/lesscode/utils/doc/
+-rw-r--r--   0 baai       (501) staff       (20)        0 2022-04-27 05:04:57.000000 lesscode-py-0.3.9/lesscode/utils/doc/__init__.py
+-rw-r--r--   0 baai       (501) staff       (20)     6339 2022-12-22 08:05:26.000000 lesscode-py-0.3.9/lesscode/utils/doc/interface_doc_handler.py
+-rw-r--r--   0 baai       (501) staff       (20)     3148 2022-04-19 02:49:20.000000 lesscode-py-0.3.9/lesscode/utils/encryption.py
+drwxr-xr-x   0 baai       (501) staff       (20)        0 2023-04-06 11:34:35.000000 lesscode-py-0.3.9/lesscode/utils/encryption_algorithm/
+-rw-r--r--   0 baai       (501) staff       (20)      226 2022-04-19 02:49:20.000000 lesscode-py-0.3.9/lesscode/utils/encryption_algorithm/__init__.py
+-rw-r--r--   0 baai       (501) staff       (20)     1532 2022-04-29 06:56:37.000000 lesscode-py-0.3.9/lesscode/utils/encryption_algorithm/aes.py
+-rw-r--r--   0 baai       (501) staff       (20)      403 2022-04-18 10:45:21.000000 lesscode-py-0.3.9/lesscode/utils/encryption_algorithm/base64.py
+-rw-r--r--   0 baai       (501) staff       (20)      826 2022-04-18 11:33:08.000000 lesscode-py-0.3.9/lesscode/utils/encryption_algorithm/des.py
+-rw-r--r--   0 baai       (501) staff       (20)      363 2022-04-18 11:12:14.000000 lesscode-py-0.3.9/lesscode/utils/encryption_algorithm/hmac.py
+-rw-r--r--   0 baai       (501) staff       (20)      203 2022-04-18 10:45:21.000000 lesscode-py-0.3.9/lesscode/utils/encryption_algorithm/md5.py
+-rw-r--r--   0 baai       (501) staff       (20)     1222 2022-04-18 10:45:21.000000 lesscode-py-0.3.9/lesscode/utils/encryption_algorithm/rsa.py
+-rw-r--r--   0 baai       (501) staff       (20)      205 2022-04-18 10:45:21.000000 lesscode-py-0.3.9/lesscode/utils/encryption_algorithm/sha1.py
+-rw-r--r--   0 baai       (501) staff       (20)      209 2022-04-18 10:45:21.000000 lesscode-py-0.3.9/lesscode/utils/encryption_algorithm/sha256.py
+-rw-r--r--   0 baai       (501) staff       (20)     2828 2022-04-19 02:20:10.000000 lesscode-py-0.3.9/lesscode/utils/encryption_algorithm/smx.py
+drwxr-xr-x   0 baai       (501) staff       (20)        0 2023-04-06 11:34:35.000000 lesscode-py-0.3.9/lesscode/utils/es_log/
+-rw-r--r--   0 baai       (501) staff       (20)      110 2022-11-07 08:36:53.000000 lesscode-py-0.3.9/lesscode/utils/es_log/__init__.py
+-rw-r--r--   0 baai       (501) staff       (20)     2397 2023-04-04 06:30:29.000000 lesscode-py-0.3.9/lesscode/utils/es_log/record_log.py
+-rw-r--r--   0 baai       (501) staff       (20)      534 2022-04-21 09:20:15.000000 lesscode-py-0.3.9/lesscode/utils/json.py
+drwxr-xr-x   0 baai       (501) staff       (20)        0 2023-04-06 11:34:35.000000 lesscode-py-0.3.9/lesscode/utils/oss/
+-rw-r--r--   0 baai       (501) staff       (20)        0 2022-05-09 01:28:27.000000 lesscode-py-0.3.9/lesscode/utils/oss/__init__.py
+-rw-r--r--   0 baai       (501) staff       (20)     7613 2023-04-04 07:52:17.000000 lesscode-py-0.3.9/lesscode/utils/oss/ks3_oss.py
+-rw-r--r--   0 baai       (501) staff       (20)    13164 2023-03-02 11:15:37.000000 lesscode-py-0.3.9/lesscode/utils/request.py
+-rw-r--r--   0 baai       (501) staff       (20)     1461 2022-04-24 03:28:39.000000 lesscode-py-0.3.9/lesscode/utils/thread_task.py
+-rw-r--r--   0 baai       (501) staff       (20)     1776 2022-08-10 03:37:58.000000 lesscode-py-0.3.9/lesscode/utils/upms_util.py
+-rw-r--r--   0 baai       (501) staff       (20)     2335 2022-12-15 08:19:45.000000 lesscode-py-0.3.9/lesscode/utils/wrapper.py
+-rw-r--r--   0 baai       (501) staff       (20)      198 2023-04-06 11:34:31.000000 lesscode-py-0.3.9/lesscode/version.py
+drwxr-xr-x   0 baai       (501) staff       (20)        0 2023-04-06 11:34:35.000000 lesscode-py-0.3.9/lesscode/web/
+-rw-r--r--   0 baai       (501) staff       (20)        0 2022-03-02 04:02:57.000000 lesscode-py-0.3.9/lesscode/web/__init__.py
+-rw-r--r--   0 baai       (501) staff       (20)    17305 2023-03-31 11:49:59.000000 lesscode-py-0.3.9/lesscode/web/base_handler.py
+-rw-r--r--   0 baai       (501) staff       (20)      399 2022-03-02 04:02:57.000000 lesscode-py-0.3.9/lesscode/web/business_exception.py
+-rw-r--r--   0 baai       (501) staff       (20)     2986 2022-11-10 08:39:11.000000 lesscode-py-0.3.9/lesscode/web/native_handler.py
+-rw-r--r--   0 baai       (501) staff       (20)      772 2022-03-02 04:02:57.000000 lesscode-py-0.3.9/lesscode/web/response_result.py
+-rw-r--r--   0 baai       (501) staff       (20)     8186 2022-12-22 08:05:26.000000 lesscode-py-0.3.9/lesscode/web/router_mapping.py
+-rw-r--r--   0 baai       (501) staff       (20)     7624 2023-03-13 03:09:17.000000 lesscode-py-0.3.9/lesscode/web/status_code.py
+-rw-r--r--   0 baai       (501) staff       (20)    15120 2023-04-06 03:31:11.000000 lesscode-py-0.3.9/lesscode/web/web_server.py
+drwxr-xr-x   0 baai       (501) staff       (20)        0 2023-04-06 11:34:35.000000 lesscode-py-0.3.9/lesscode_py.egg-info/
+-rw-r--r--   0 baai       (501) staff       (20)     8235 2023-04-06 11:34:35.000000 lesscode-py-0.3.9/lesscode_py.egg-info/PKG-INFO
+-rw-r--r--   0 baai       (501) staff       (20)     3565 2023-04-06 11:34:35.000000 lesscode-py-0.3.9/lesscode_py.egg-info/SOURCES.txt
+-rw-r--r--   0 baai       (501) staff       (20)        1 2023-04-06 11:34:35.000000 lesscode-py-0.3.9/lesscode_py.egg-info/dependency_links.txt
+-rw-r--r--   0 baai       (501) staff       (20)      388 2023-04-06 11:34:35.000000 lesscode-py-0.3.9/lesscode_py.egg-info/requires.txt
+-rw-r--r--   0 baai       (501) staff       (20)       13 2023-04-06 11:34:35.000000 lesscode-py-0.3.9/lesscode_py.egg-info/top_level.txt
+-rw-r--r--   0 baai       (501) staff       (20)       38 2023-04-06 11:34:35.000000 lesscode-py-0.3.9/setup.cfg
+-rw-r--r--   0 baai       (501) staff       (20)     2637 2023-03-31 13:33:31.000000 lesscode-py-0.3.9/setup.py
```

### Comparing `lesscode-py-0.3.8/PKG-INFO` & `lesscode-py-0.3.9/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: lesscode-py
-Version: 0.3.8
+Version: 0.3.9
 Summary: lesscode-python 是基于tornado的web开发脚手架项目，该项目初衷为简化开发过程，让研发人员更加关注业务。
 Home-page: https://gitee.com/yongchao9/lesscode-python
 Author: Chao.yy
 Author-email: yuyc@ishangqi.com
 License: UNKNOWN
 Platform: python
 Classifier: Programming Language :: Python :: 3
```

### Comparing `lesscode-py-0.3.8/README.md` & `lesscode-py-0.3.9/README.md`

 * *Files identical despite different names*

### Comparing `lesscode-py-0.3.8/bin/lesscode.py` & `lesscode-py-0.3.9/bin/lesscode.py`

 * *Files identical despite different names*

### Comparing `lesscode-py-0.3.8/lesscode/db/base_connection_pool.py` & `lesscode-py-0.3.9/lesscode/db/base_connection_pool.py`

 * *Files identical despite different names*

### Comparing `lesscode-py-0.3.8/lesscode/db/base_sql_helper.py` & `lesscode-py-0.3.9/lesscode/db/base_sql_helper.py`

 * *Files identical despite different names*

### Comparing `lesscode-py-0.3.8/lesscode/db/condition_wrapper.py` & `lesscode-py-0.3.9/lesscode/db/condition_wrapper.py`

 * *Files identical despite different names*

### Comparing `lesscode-py-0.3.8/lesscode/db/connection_info.py` & `lesscode-py-0.3.9/lesscode/db/connection_info.py`

 * *Files identical despite different names*

### Comparing `lesscode-py-0.3.8/lesscode/db/ds_helper.py` & `lesscode-py-0.3.9/lesscode/db/ds_helper.py`

 * *Files identical despite different names*

### Comparing `lesscode-py-0.3.8/lesscode/db/elasticsearch/elasticsearch_helper.py` & `lesscode-py-0.3.9/lesscode/db/elasticsearch/elasticsearch_helper.py`

 * *Files identical despite different names*

### Comparing `lesscode-py-0.3.8/lesscode/db/elasticsearch/elasticsearch_pool.py` & `lesscode-py-0.3.9/lesscode/db/elasticsearch/elasticsearch_pool.py`

 * *Files identical despite different names*

### Comparing `lesscode-py-0.3.8/lesscode/db/es/es_helper.py` & `lesscode-py-0.3.9/lesscode/db/es/es_helper.py`

 * *Files 0% similar despite different names*

```diff
@@ -16,15 +16,15 @@
 
 from lesscode.db.base_sql_helper import BaseSqlHelper, echo_sql
 from lesscode.db.condition_wrapper import ConditionWrapper
 from lesscode.db.connection_info import ConnectionInfo
 from lesscode.db.es.es_pool import EsPool
 from lesscode.db.es.es_request import EsRequest
 from lesscode.db.page import Page
-from lesscode.utils.EsUtil import format_es_param_result,  es_mapping2dict
+from lesscode.utils.EsUtil import format_es_param_result, es_mapping2dict
 from lesscode.utils.common import dict2single_dict
 from lesscode.utils.encryption_algorithm import AES
 
 
 class EsHelper:
     """
     ElasticsearchHelper  ES数据库操作实现
@@ -468,15 +468,15 @@
         if "error" in res:
             raise Exception(f"res={res}")
         return res
 
     def correction_body(self, route_key, body):
         try:
             es_mapping_res = self.sync_es_mapping(route_key)
-            es_mapping = es_mapping_res.get(route_key, {}).get("mappings", {})
+            es_mapping = es_mapping_res.get(route_key, {}).get("mappings", {}).get("properties", {})
             self.correction_param(body, es_mapping)
         except Exception as e:
             traceback.format_exc()
 
     def sync_es_search_format_hits(self, route_key, body):
         res = self.sync_es_search(route_key, body)
         hits = res.get("hits", {})
```

### Comparing `lesscode-py-0.3.8/lesscode/db/es/es_pool.py` & `lesscode-py-0.3.9/lesscode/db/es/es_pool.py`

 * *Files identical despite different names*

### Comparing `lesscode-py-0.3.8/lesscode/db/es/es_request.py` & `lesscode-py-0.3.9/lesscode/db/es/es_request.py`

 * *Files identical despite different names*

### Comparing `lesscode-py-0.3.8/lesscode/db/init_connection_pool.py` & `lesscode-py-0.3.9/lesscode/db/init_connection_pool.py`

 * *Files identical despite different names*

### Comparing `lesscode-py-0.3.8/lesscode/db/mongodb/mongodb_helper.py` & `lesscode-py-0.3.9/lesscode/db/mongodb/mongodb_helper.py`

 * *Files identical despite different names*

### Comparing `lesscode-py-0.3.8/lesscode/db/mongodb/mongodb_pool.py` & `lesscode-py-0.3.9/lesscode/db/mongodb/mongodb_pool.py`

 * *Files identical despite different names*

### Comparing `lesscode-py-0.3.8/lesscode/db/mysql/mysql_helper.py` & `lesscode-py-0.3.9/lesscode/db/mysql/mysql_helper.py`

 * *Files identical despite different names*

### Comparing `lesscode-py-0.3.8/lesscode/db/mysql/mysql_pool.py` & `lesscode-py-0.3.9/lesscode/db/mysql/mysql_pool.py`

 * *Files identical despite different names*

### Comparing `lesscode-py-0.3.8/lesscode/db/mysql_sqlalchemy/SqlAlchemy.py` & `lesscode-py-0.3.9/lesscode/db/mysql_sqlalchemy/SqlAlchemy.py`

 * *Files identical despite different names*

### Comparing `lesscode-py-0.3.8/lesscode/db/mysql_sqlalchemy/mysql_sqlalchemy_pool.py` & `lesscode-py-0.3.9/lesscode/db/mysql_sqlalchemy/mysql_sqlalchemy_pool.py`

 * *Files identical despite different names*

### Comparing `lesscode-py-0.3.8/lesscode/db/nebula/nebula_helper.py` & `lesscode-py-0.3.9/lesscode/db/nebula/nebula_helper.py`

 * *Files identical despite different names*

### Comparing `lesscode-py-0.3.8/lesscode/db/nebula/nebula_pool.py` & `lesscode-py-0.3.9/lesscode/db/nebula/nebula_pool.py`

 * *Files identical despite different names*

### Comparing `lesscode-py-0.3.8/lesscode/db/neo4j/neo4j_helper.py` & `lesscode-py-0.3.9/lesscode/db/neo4j/neo4j_helper.py`

 * *Files identical despite different names*

### Comparing `lesscode-py-0.3.8/lesscode/db/neo4j/neo4j_pool.py` & `lesscode-py-0.3.9/lesscode/db/neo4j/neo4j_pool.py`

 * *Files identical despite different names*

### Comparing `lesscode-py-0.3.8/lesscode/db/page.py` & `lesscode-py-0.3.9/lesscode/db/page.py`

 * *Files identical despite different names*

### Comparing `lesscode-py-0.3.8/lesscode/db/postgresql/postgresql_helper.py` & `lesscode-py-0.3.9/lesscode/db/postgresql/postgresql_helper.py`

 * *Files identical despite different names*

### Comparing `lesscode-py-0.3.8/lesscode/db/postgresql/postgresql_pool.py` & `lesscode-py-0.3.9/lesscode/db/postgresql/postgresql_pool.py`

 * *Files identical despite different names*

### Comparing `lesscode-py-0.3.8/lesscode/db/redis/redis_helper.py` & `lesscode-py-0.3.9/lesscode/db/redis/redis_helper.py`

 * *Files identical despite different names*

### Comparing `lesscode-py-0.3.8/lesscode/db/redis/redis_pool.py` & `lesscode-py-0.3.9/lesscode/db/redis/redis_pool.py`

 * *Files identical despite different names*

### Comparing `lesscode-py-0.3.8/lesscode/db/relational_db_helper.py` & `lesscode-py-0.3.9/lesscode/db/relational_db_helper.py`

 * *Files identical despite different names*

### Comparing `lesscode-py-0.3.8/lesscode/db/sqlalchemy/sqlalchemy_helper.py` & `lesscode-py-0.3.9/lesscode/db/sqlalchemy/sqlalchemy_helper.py`

 * *Files identical despite different names*

### Comparing `lesscode-py-0.3.8/lesscode/db/sqlalchemy/sqlalchemy_pool.py` & `lesscode-py-0.3.9/lesscode/db/sqlalchemy/sqlalchemy_pool.py`

 * *Files identical despite different names*

### Comparing `lesscode-py-0.3.8/lesscode/extend_handlers/doc/swagger_interface_doc_handler.py` & `lesscode-py-0.3.9/lesscode/extend_handlers/doc/swagger_interface_doc_handler.py`

 * *Files identical despite different names*

### Comparing `lesscode-py-0.3.8/lesscode/extend_handlers/not_found_handler.py` & `lesscode-py-0.3.9/lesscode/extend_handlers/not_found_handler.py`

 * *Files identical despite different names*

### Comparing `lesscode-py-0.3.8/lesscode/mq/kafka/kafka_helper.py` & `lesscode-py-0.3.9/lesscode/mq/kafka/kafka_helper.py`

 * *Files identical despite different names*

### Comparing `lesscode-py-0.3.8/lesscode/mq/rabbitmq/rabbitmq_helper.py` & `lesscode-py-0.3.9/lesscode/mq/rabbitmq/rabbitmq_helper.py`

 * *Files identical despite different names*

### Comparing `lesscode-py-0.3.8/lesscode/task/task_helper.py` & `lesscode-py-0.3.9/lesscode/task/task_helper.py`

 * *Files identical despite different names*

### Comparing `lesscode-py-0.3.8/lesscode/utils/CacheUtil.py` & `lesscode-py-0.3.9/lesscode/utils/CacheUtil.py`

 * *Files identical despite different names*

### Comparing `lesscode-py-0.3.8/lesscode/utils/EsUtil.py` & `lesscode-py-0.3.9/lesscode/utils/EsUtil.py`

 * *Files identical despite different names*

### Comparing `lesscode-py-0.3.8/lesscode/utils/MongodbUtil.py` & `lesscode-py-0.3.9/lesscode/utils/MongodbUtil.py`

 * *Files identical despite different names*

### Comparing `lesscode-py-0.3.8/lesscode/utils/ThreadUtil.py` & `lesscode-py-0.3.9/lesscode/utils/ThreadUtil.py`

 * *Files identical despite different names*

### Comparing `lesscode-py-0.3.8/lesscode/utils/business.py` & `lesscode-py-0.3.9/lesscode/utils/business.py`

 * *Files identical despite different names*

### Comparing `lesscode-py-0.3.8/lesscode/utils/chart/common2chart.py` & `lesscode-py-0.3.9/lesscode/utils/chart/common2chart.py`

 * *Files identical despite different names*

### Comparing `lesscode-py-0.3.8/lesscode/utils/chart/es2chart.py` & `lesscode-py-0.3.9/lesscode/utils/chart/es2chart.py`

 * *Files identical despite different names*

### Comparing `lesscode-py-0.3.8/lesscode/utils/common.py` & `lesscode-py-0.3.9/lesscode/utils/common.py`

 * *Files identical despite different names*

### Comparing `lesscode-py-0.3.8/lesscode/utils/doc/interface_doc_handler.py` & `lesscode-py-0.3.9/lesscode/utils/doc/interface_doc_handler.py`

 * *Files identical despite different names*

### Comparing `lesscode-py-0.3.8/lesscode/utils/encryption.py` & `lesscode-py-0.3.9/lesscode/utils/encryption.py`

 * *Files identical despite different names*

### Comparing `lesscode-py-0.3.8/lesscode/utils/encryption_algorithm/aes.py` & `lesscode-py-0.3.9/lesscode/utils/encryption_algorithm/aes.py`

 * *Files identical despite different names*

### Comparing `lesscode-py-0.3.8/lesscode/utils/encryption_algorithm/des.py` & `lesscode-py-0.3.9/lesscode/utils/encryption_algorithm/des.py`

 * *Files identical despite different names*

### Comparing `lesscode-py-0.3.8/lesscode/utils/encryption_algorithm/rsa.py` & `lesscode-py-0.3.9/lesscode/utils/encryption_algorithm/rsa.py`

 * *Files identical despite different names*

### Comparing `lesscode-py-0.3.8/lesscode/utils/encryption_algorithm/smx.py` & `lesscode-py-0.3.9/lesscode/utils/encryption_algorithm/smx.py`

 * *Files identical despite different names*

### Comparing `lesscode-py-0.3.8/lesscode/utils/es_log/record_log.py` & `lesscode-py-0.3.9/lesscode/utils/es_log/record_log.py`

 * *Files identical despite different names*

### Comparing `lesscode-py-0.3.8/lesscode/utils/json.py` & `lesscode-py-0.3.9/lesscode/utils/json.py`

 * *Files identical despite different names*

### Comparing `lesscode-py-0.3.8/lesscode/utils/oss/ks3_oss.py` & `lesscode-py-0.3.9/lesscode/utils/oss/ks3_oss.py`

 * *Files identical despite different names*

### Comparing `lesscode-py-0.3.8/lesscode/utils/request.py` & `lesscode-py-0.3.9/lesscode/utils/request.py`

 * *Files identical despite different names*

### Comparing `lesscode-py-0.3.8/lesscode/utils/thread_task.py` & `lesscode-py-0.3.9/lesscode/utils/thread_task.py`

 * *Files identical despite different names*

### Comparing `lesscode-py-0.3.8/lesscode/utils/upms_util.py` & `lesscode-py-0.3.9/lesscode/utils/upms_util.py`

 * *Files identical despite different names*

### Comparing `lesscode-py-0.3.8/lesscode/utils/wrapper.py` & `lesscode-py-0.3.9/lesscode/utils/wrapper.py`

 * *Files identical despite different names*

### Comparing `lesscode-py-0.3.8/lesscode/web/base_handler.py` & `lesscode-py-0.3.9/lesscode/web/base_handler.py`

 * *Files identical despite different names*

### Comparing `lesscode-py-0.3.8/lesscode/web/native_handler.py` & `lesscode-py-0.3.9/lesscode/web/native_handler.py`

 * *Files identical despite different names*

### Comparing `lesscode-py-0.3.8/lesscode/web/response_result.py` & `lesscode-py-0.3.9/lesscode/web/response_result.py`

 * *Files identical despite different names*

### Comparing `lesscode-py-0.3.8/lesscode/web/router_mapping.py` & `lesscode-py-0.3.9/lesscode/web/router_mapping.py`

 * *Files identical despite different names*

### Comparing `lesscode-py-0.3.8/lesscode/web/status_code.py` & `lesscode-py-0.3.9/lesscode/web/status_code.py`

 * *Files identical despite different names*

### Comparing `lesscode-py-0.3.8/lesscode/web/web_server.py` & `lesscode-py-0.3.9/lesscode/web/web_server.py`

 * *Files identical despite different names*

### Comparing `lesscode-py-0.3.8/lesscode_py.egg-info/PKG-INFO` & `lesscode-py-0.3.9/lesscode_py.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: lesscode-py
-Version: 0.3.8
+Version: 0.3.9
 Summary: lesscode-python 是基于tornado的web开发脚手架项目，该项目初衷为简化开发过程，让研发人员更加关注业务。
 Home-page: https://gitee.com/yongchao9/lesscode-python
 Author: Chao.yy
 Author-email: yuyc@ishangqi.com
 License: UNKNOWN
 Platform: python
 Classifier: Programming Language :: Python :: 3
```

### Comparing `lesscode-py-0.3.8/lesscode_py.egg-info/SOURCES.txt` & `lesscode-py-0.3.9/lesscode_py.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `lesscode-py-0.3.8/setup.py` & `lesscode-py-0.3.9/setup.py`

 * *Files identical despite different names*

