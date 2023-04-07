# Comparing `tmp/yyxx_game_pkg-2023.4.4.1.tar.gz` & `tmp/yyxx_game_pkg-2023.4.7.1.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "yyxx_game_pkg-2023.4.4.1.tar", max compression
+gzip compressed data, was "yyxx_game_pkg-2023.4.7.1.tar", max compression
```

## Comparing `yyxx_game_pkg-2023.4.4.1.tar` & `yyxx_game_pkg-2023.4.7.1.tar`

### file list

```diff
@@ -1,86 +1,89 @@
--rw-r--r--   0        0        0     3888 2023-04-04 08:20:25.426815 yyxx_game_pkg-2023.4.4.1/README.md
--rw-r--r--   0        0        0     1122 2023-04-04 08:20:37.014766 yyxx_game_pkg-2023.4.4.1/pyproject.toml
--rw-r--r--   0        0        0       68 2023-04-04 08:20:25.430815 yyxx_game_pkg-2023.4.4.1/tests/__init__.py
--rw-r--r--   0        0        0       70 2023-04-04 08:20:25.430815 yyxx_game_pkg-2023.4.4.1/tests/dispatch/__init__.py
--rw-r--r--   0        0        0       70 2023-04-04 08:20:25.430815 yyxx_game_pkg-2023.4.4.1/tests/dispatch/config/__init__.py
--rw-r--r--   0        0        0     1228 2023-04-04 08:20:25.430815 yyxx_game_pkg-2023.4.4.1/tests/dispatch/config/celery_local_config.py
--rw-r--r--   0        0        0      676 2023-04-04 08:20:25.430815 yyxx_game_pkg-2023.4.4.1/tests/dispatch/rules/__init__.py
--rw-r--r--   0        0        0     1348 2023-04-04 08:20:25.430815 yyxx_game_pkg-2023.4.4.1/tests/dispatch/rules/rule_temp.py
--rw-r--r--   0        0        0      580 2023-04-04 08:20:25.430815 yyxx_game_pkg-2023.4.4.1/tests/dispatch/test_dispatch.py
--rw-r--r--   0        0        0       84 2023-04-04 08:20:25.430815 yyxx_game_pkg-2023.4.4.1/tests/helpers/__init__.py
--rw-r--r--   0        0        0      439 2023-04-04 08:20:25.430815 yyxx_game_pkg-2023.4.4.1/tests/helpers/test_pika_helper.py
--rw-r--r--   0        0        0      468 2023-04-04 08:20:25.430815 yyxx_game_pkg-2023.4.4.1/tests/helpers/test_redis_helper.py
--rw-r--r--   0        0        0       70 2023-04-04 08:20:25.430815 yyxx_game_pkg-2023.4.4.1/tests/submit/__init__.py
--rw-r--r--   0        0        0       70 2023-04-04 08:20:25.430815 yyxx_game_pkg-2023.4.4.1/tests/submit/schedule_rule/__init__.py
--rw-r--r--   0        0        0       70 2023-04-04 08:20:25.430815 yyxx_game_pkg-2023.4.4.1/tests/submit/schedule_rule/schedule/__init__.py
--rw-r--r--   0        0        0       70 2023-04-04 08:20:25.430815 yyxx_game_pkg-2023.4.4.1/tests/submit/schedule_rule/schedule/statistic_task/__init__.py
--rw-r--r--   0        0        0      431 2023-04-04 08:20:25.430815 yyxx_game_pkg-2023.4.4.1/tests/submit/schedule_rule/schedule/statistic_task/schedule_statistic_collect_test.py
--rw-r--r--   0        0        0      413 2023-04-04 08:20:25.430815 yyxx_game_pkg-2023.4.4.1/tests/submit/schedule_rule/schedule/statistic_task/schedule_statistic_task_test.py
--rw-r--r--   0        0        0       70 2023-04-04 08:20:25.430815 yyxx_game_pkg-2023.4.4.1/tests/submit/schedule_rule/schedule/work_flow/__init__.py
--rw-r--r--   0        0        0     1217 2023-04-04 08:20:25.430815 yyxx_game_pkg-2023.4.4.1/tests/submit/schedule_rule/schedule/work_flow/schedule_work_flow_test.py
--rw-r--r--   0        0        0      305 2023-04-04 08:20:25.430815 yyxx_game_pkg-2023.4.4.1/tests/submit/submit.json
--rw-r--r--   0        0        0     1250 2023-04-04 08:20:25.430815 yyxx_game_pkg-2023.4.4.1/tests/submit/test_submit.py
--rw-r--r--   0        0        0      235 2023-04-04 08:20:25.430815 yyxx_game_pkg-2023.4.4.1/tests/test_ip2region.py
--rw-r--r--   0        0        0      513 2023-04-04 08:20:25.430815 yyxx_game_pkg-2023.4.4.1/tests/test_logger.py
--rw-r--r--   0        0        0      960 2023-04-04 08:20:25.430815 yyxx_game_pkg-2023.4.4.1/tests/test_xtrace.py
--rw-r--r--   0        0        0       81 2023-04-04 08:20:25.430815 yyxx_game_pkg-2023.4.4.1/tests/utils/__init__.py
--rw-r--r--   0        0        0       70 2023-04-04 08:20:25.430815 yyxx_game_pkg-2023.4.4.1/tests/xcelery/__init__.py
--rw-r--r--   0        0        0       70 2023-04-04 08:20:25.430815 yyxx_game_pkg-2023.4.4.1/tests/xcelery/config/__init__.py
--rw-r--r--   0        0        0     1226 2023-04-04 08:20:25.430815 yyxx_game_pkg-2023.4.4.1/tests/xcelery/config/celery_local_config.py
--rw-r--r--   0        0        0      747 2023-04-04 08:20:25.430815 yyxx_game_pkg-2023.4.4.1/tests/xcelery/task_register.py
--rw-r--r--   0        0        0      299 2023-04-04 08:20:25.430815 yyxx_game_pkg-2023.4.4.1/tests/xcelery/test_celery.py
--rw-r--r--   0        0        0       69 2023-04-04 08:20:25.430815 yyxx_game_pkg-2023.4.4.1/yyxx_game_pkg/__init__.py
--rw-r--r--   0        0        0       83 2023-04-04 08:20:25.430815 yyxx_game_pkg-2023.4.4.1/yyxx_game_pkg/dbops/__init__.py
--rw-r--r--   0        0        0     1331 2023-04-04 08:20:25.430815 yyxx_game_pkg-2023.4.4.1/yyxx_game_pkg/dbops/base.py
--rw-r--r--   0        0        0     1295 2023-04-04 08:20:25.430815 yyxx_game_pkg-2023.4.4.1/yyxx_game_pkg/dbops/ch_op.py
--rw-r--r--   0        0        0     5597 2023-04-04 08:20:25.430815 yyxx_game_pkg-2023.4.4.1/yyxx_game_pkg/dbops/das_api.py
--rw-r--r--   0        0        0     1911 2023-04-04 08:20:25.430815 yyxx_game_pkg-2023.4.4.1/yyxx_game_pkg/dbops/es_op.py
--rw-r--r--   0        0        0     1678 2023-04-04 08:20:25.430815 yyxx_game_pkg-2023.4.4.1/yyxx_game_pkg/dbops/hdfs_op.py
--rw-r--r--   0        0        0      979 2023-04-04 08:20:25.430815 yyxx_game_pkg-2023.4.4.1/yyxx_game_pkg/dbops/mongo_op.py
--rw-r--r--   0        0        0     3596 2023-04-04 08:20:25.430815 yyxx_game_pkg-2023.4.4.1/yyxx_game_pkg/dbops/mysql_op.py
--rw-r--r--   0        0        0       81 2023-04-04 08:20:25.430815 yyxx_game_pkg-2023.4.4.1/yyxx_game_pkg/helpers/__init__.py
--rw-r--r--   0        0        0     2100 2023-04-04 08:20:25.430815 yyxx_game_pkg-2023.4.4.1/yyxx_game_pkg/helpers/mysql_helper.py
--rw-r--r--   0        0        0     1266 2023-04-04 08:20:25.430815 yyxx_game_pkg-2023.4.4.1/yyxx_game_pkg/helpers/pika_helper.py
--rw-r--r--   0        0        0     2667 2023-04-04 08:20:25.430815 yyxx_game_pkg-2023.4.4.1/yyxx_game_pkg/helpers/redis_helper.py
--rw-r--r--   0        0        0       79 2023-04-04 08:20:25.430815 yyxx_game_pkg-2023.4.4.1/yyxx_game_pkg/ip2region/__init__.py
--rw-r--r--   0        0        0 11070130 2023-04-04 08:20:25.498815 yyxx_game_pkg-2023.4.4.1/yyxx_game_pkg/ip2region/ip2region.xdb
--rw-r--r--   0        0        0      604 2023-04-04 08:20:25.498815 yyxx_game_pkg-2023.4.4.1/yyxx_game_pkg/ip2region/ip_x.py
--rw-r--r--   0        0        0     5735 2023-04-04 08:20:25.498815 yyxx_game_pkg-2023.4.4.1/yyxx_game_pkg/ip2region/xdbSearcher.py
--rw-r--r--   0        0        0       81 2023-04-04 08:20:25.498815 yyxx_game_pkg-2023.4.4.1/yyxx_game_pkg/logger/__init__.py
--rw-r--r--   0        0        0     2326 2023-04-04 08:20:25.498815 yyxx_game_pkg-2023.4.4.1/yyxx_game_pkg/logger/config.py
--rw-r--r--   0        0        0     3467 2023-04-04 08:20:25.498815 yyxx_game_pkg-2023.4.4.1/yyxx_game_pkg/logger/handlers.py
--rw-r--r--   0        0        0     2154 2023-04-04 08:20:25.498815 yyxx_game_pkg-2023.4.4.1/yyxx_game_pkg/logger/log.py
--rw-r--r--   0        0        0       70 2023-04-04 08:20:25.498815 yyxx_game_pkg-2023.4.4.1/yyxx_game_pkg/stat/__init__.py
--rw-r--r--   0        0        0       68 2023-04-04 08:20:25.498815 yyxx_game_pkg-2023.4.4.1/yyxx_game_pkg/stat/dispatch/__init__.py
--rw-r--r--   0        0        0       70 2023-04-04 08:20:25.498815 yyxx_game_pkg-2023.4.4.1/yyxx_game_pkg/stat/dispatch/common/__init__.py
--rw-r--r--   0        0        0     1530 2023-04-04 08:20:25.498815 yyxx_game_pkg-2023.4.4.1/yyxx_game_pkg/stat/dispatch/common/common.py
--rw-r--r--   0        0        0      378 2023-04-04 08:20:25.498815 yyxx_game_pkg-2023.4.4.1/yyxx_game_pkg/stat/dispatch/common/log.py
--rw-r--r--   0        0        0       69 2023-04-04 08:20:25.498815 yyxx_game_pkg-2023.4.4.1/yyxx_game_pkg/stat/dispatch/core/__init__.py
--rw-r--r--   0        0        0      805 2023-04-04 08:20:25.498815 yyxx_game_pkg-2023.4.4.1/yyxx_game_pkg/stat/dispatch/core/manager.py
--rw-r--r--   0        0        0     1042 2023-04-04 08:20:25.498815 yyxx_game_pkg-2023.4.4.1/yyxx_game_pkg/stat/dispatch/core/structs.py
--rw-r--r--   0        0        0     5533 2023-04-04 08:20:25.498815 yyxx_game_pkg-2023.4.4.1/yyxx_game_pkg/stat/dispatch/core/workflows.py
--rw-r--r--   0        0        0      604 2023-04-04 08:20:25.498815 yyxx_game_pkg-2023.4.4.1/yyxx_game_pkg/stat/dispatch/dispatch.py
--rw-r--r--   0        0        0       70 2023-04-04 08:20:25.498815 yyxx_game_pkg-2023.4.4.1/yyxx_game_pkg/stat/dispatch/logic/__init__.py
--rw-r--r--   0        0        0     4418 2023-04-04 08:20:25.498815 yyxx_game_pkg-2023.4.4.1/yyxx_game_pkg/stat/dispatch/logic/task_logic.py
--rw-r--r--   0        0        0      809 2023-04-04 08:20:25.498815 yyxx_game_pkg-2023.4.4.1/yyxx_game_pkg/stat/dispatch/route.py
--rw-r--r--   0        0        0      693 2023-04-04 08:20:25.498815 yyxx_game_pkg-2023.4.4.1/yyxx_game_pkg/stat/dispatch/rules/__init__.py
--rw-r--r--   0        0        0      689 2023-04-04 08:20:25.498815 yyxx_game_pkg-2023.4.4.1/yyxx_game_pkg/stat/dispatch/rules/rule_base.py
--rw-r--r--   0        0        0     4286 2023-04-04 08:20:25.498815 yyxx_game_pkg-2023.4.4.1/yyxx_game_pkg/stat/dispatch/rules/rule_workflow.py
--rw-r--r--   0        0        0       70 2023-04-04 08:20:25.498815 yyxx_game_pkg-2023.4.4.1/yyxx_game_pkg/stat/submit/__init__.py
--rw-r--r--   0        0        0       70 2023-04-04 08:20:25.498815 yyxx_game_pkg-2023.4.4.1/yyxx_game_pkg/stat/submit/logic/__init__.py
--rw-r--r--   0        0        0     5961 2023-04-04 08:20:25.498815 yyxx_game_pkg-2023.4.4.1/yyxx_game_pkg/stat/submit/logic/submit_logic.py
--rw-r--r--   0        0        0      987 2023-04-04 08:20:25.498815 yyxx_game_pkg-2023.4.4.1/yyxx_game_pkg/stat/submit/submit.py
--rw-r--r--   0        0        0       70 2023-04-04 08:20:25.498815 yyxx_game_pkg-2023.4.4.1/yyxx_game_pkg/stat/xcelery/__init__.py
--rw-r--r--   0        0        0     2110 2023-04-04 08:20:25.498815 yyxx_game_pkg-2023.4.4.1/yyxx_game_pkg/stat/xcelery/instance.py
--rw-r--r--   0        0        0      961 2023-04-04 08:20:25.498815 yyxx_game_pkg-2023.4.4.1/yyxx_game_pkg/stat/xcelery/task_base.py
--rw-r--r--   0        0        0       83 2023-04-04 08:20:25.498815 yyxx_game_pkg-2023.4.4.1/yyxx_game_pkg/utils/__init__.py
--rw-r--r--   0        0        0     5035 2023-04-04 08:20:25.498815 yyxx_game_pkg-2023.4.4.1/yyxx_game_pkg/utils/decorator.py
--rw-r--r--   0        0        0     2845 2023-04-04 08:20:25.498815 yyxx_game_pkg-2023.4.4.1/yyxx_game_pkg/utils/profiler.py
--rw-r--r--   0        0        0     2992 2023-04-04 08:20:25.498815 yyxx_game_pkg-2023.4.4.1/yyxx_game_pkg/utils/xListStr.py
--rw-r--r--   0        0        0     5255 2023-04-04 08:20:25.498815 yyxx_game_pkg-2023.4.4.1/yyxx_game_pkg/utils/xdataframe.py
--rw-r--r--   0        0        0     6161 2023-04-04 08:20:25.498815 yyxx_game_pkg-2023.4.4.1/yyxx_game_pkg/utils/xdate.py
--rw-r--r--   0        0        0     3101 2023-04-04 08:20:25.498815 yyxx_game_pkg-2023.4.4.1/yyxx_game_pkg/utils/xhttp.py
--rw-r--r--   0        0        0      971 2023-04-04 08:20:25.498815 yyxx_game_pkg-2023.4.4.1/yyxx_game_pkg/utils/xmath.py
--rw-r--r--   0        0        0       69 2023-04-04 08:20:25.498815 yyxx_game_pkg-2023.4.4.1/yyxx_game_pkg/xtrace/__init__.py
--rw-r--r--   0        0        0     2858 2023-04-04 08:20:25.498815 yyxx_game_pkg-2023.4.4.1/yyxx_game_pkg/xtrace/helper.py
--rw-r--r--   0        0        0     5442 1970-01-01 00:00:00.000000 yyxx_game_pkg-2023.4.4.1/PKG-INFO
+-rw-r--r--   0        0        0     3888 2023-04-07 09:03:02.119412 yyxx_game_pkg-2023.4.7.1/README.md
+-rw-r--r--   0        0        0     1122 2023-04-07 09:03:12.419337 yyxx_game_pkg-2023.4.7.1/pyproject.toml
+-rw-r--r--   0        0        0       68 2023-04-07 09:03:02.123412 yyxx_game_pkg-2023.4.7.1/tests/__init__.py
+-rw-r--r--   0        0        0       83 2023-04-07 09:03:02.123412 yyxx_game_pkg-2023.4.7.1/tests/dbops/__init__.py
+-rw-r--r--   0        0        0     1341 2023-04-07 09:03:02.123412 yyxx_game_pkg-2023.4.7.1/tests/dbops/mysql_op.py
+-rw-r--r--   0        0        0       70 2023-04-07 09:03:02.123412 yyxx_game_pkg-2023.4.7.1/tests/dispatch/__init__.py
+-rw-r--r--   0        0        0       70 2023-04-07 09:03:02.123412 yyxx_game_pkg-2023.4.7.1/tests/dispatch/config/__init__.py
+-rw-r--r--   0        0        0     1228 2023-04-07 09:03:02.123412 yyxx_game_pkg-2023.4.7.1/tests/dispatch/config/celery_local_config.py
+-rw-r--r--   0        0        0      676 2023-04-07 09:03:02.123412 yyxx_game_pkg-2023.4.7.1/tests/dispatch/rules/__init__.py
+-rw-r--r--   0        0        0     1348 2023-04-07 09:03:02.123412 yyxx_game_pkg-2023.4.7.1/tests/dispatch/rules/rule_temp.py
+-rw-r--r--   0        0        0      580 2023-04-07 09:03:02.123412 yyxx_game_pkg-2023.4.7.1/tests/dispatch/test_dispatch.py
+-rw-r--r--   0        0        0       84 2023-04-07 09:03:02.123412 yyxx_game_pkg-2023.4.7.1/tests/helpers/__init__.py
+-rw-r--r--   0        0        0      522 2023-04-07 09:03:02.123412 yyxx_game_pkg-2023.4.7.1/tests/helpers/test_mysql_helper.py
+-rw-r--r--   0        0        0      455 2023-04-07 09:03:02.123412 yyxx_game_pkg-2023.4.7.1/tests/helpers/test_pika_helper.py
+-rw-r--r--   0        0        0      481 2023-04-07 09:03:02.123412 yyxx_game_pkg-2023.4.7.1/tests/helpers/test_redis_helper.py
+-rw-r--r--   0        0        0       70 2023-04-07 09:03:02.123412 yyxx_game_pkg-2023.4.7.1/tests/submit/__init__.py
+-rw-r--r--   0        0        0       70 2023-04-07 09:03:02.123412 yyxx_game_pkg-2023.4.7.1/tests/submit/schedule_rule/__init__.py
+-rw-r--r--   0        0        0       70 2023-04-07 09:03:02.123412 yyxx_game_pkg-2023.4.7.1/tests/submit/schedule_rule/schedule/__init__.py
+-rw-r--r--   0        0        0       70 2023-04-07 09:03:02.123412 yyxx_game_pkg-2023.4.7.1/tests/submit/schedule_rule/schedule/statistic_task/__init__.py
+-rw-r--r--   0        0        0      431 2023-04-07 09:03:02.123412 yyxx_game_pkg-2023.4.7.1/tests/submit/schedule_rule/schedule/statistic_task/schedule_statistic_collect_test.py
+-rw-r--r--   0        0        0      413 2023-04-07 09:03:02.123412 yyxx_game_pkg-2023.4.7.1/tests/submit/schedule_rule/schedule/statistic_task/schedule_statistic_task_test.py
+-rw-r--r--   0        0        0       70 2023-04-07 09:03:02.123412 yyxx_game_pkg-2023.4.7.1/tests/submit/schedule_rule/schedule/work_flow/__init__.py
+-rw-r--r--   0        0        0     1217 2023-04-07 09:03:02.123412 yyxx_game_pkg-2023.4.7.1/tests/submit/schedule_rule/schedule/work_flow/schedule_work_flow_test.py
+-rw-r--r--   0        0        0      305 2023-04-07 09:03:02.123412 yyxx_game_pkg-2023.4.7.1/tests/submit/submit.json
+-rw-r--r--   0        0        0     1250 2023-04-07 09:03:02.123412 yyxx_game_pkg-2023.4.7.1/tests/submit/test_submit.py
+-rw-r--r--   0        0        0      235 2023-04-07 09:03:02.123412 yyxx_game_pkg-2023.4.7.1/tests/test_ip2region.py
+-rw-r--r--   0        0        0      513 2023-04-07 09:03:02.123412 yyxx_game_pkg-2023.4.7.1/tests/test_logger.py
+-rw-r--r--   0        0        0      960 2023-04-07 09:03:02.123412 yyxx_game_pkg-2023.4.7.1/tests/test_xtrace.py
+-rw-r--r--   0        0        0       81 2023-04-07 09:03:02.123412 yyxx_game_pkg-2023.4.7.1/tests/utils/__init__.py
+-rw-r--r--   0        0        0       70 2023-04-07 09:03:02.123412 yyxx_game_pkg-2023.4.7.1/tests/xcelery/__init__.py
+-rw-r--r--   0        0        0       70 2023-04-07 09:03:02.123412 yyxx_game_pkg-2023.4.7.1/tests/xcelery/config/__init__.py
+-rw-r--r--   0        0        0     1226 2023-04-07 09:03:02.123412 yyxx_game_pkg-2023.4.7.1/tests/xcelery/config/celery_local_config.py
+-rw-r--r--   0        0        0      747 2023-04-07 09:03:02.123412 yyxx_game_pkg-2023.4.7.1/tests/xcelery/task_register.py
+-rw-r--r--   0        0        0      299 2023-04-07 09:03:02.123412 yyxx_game_pkg-2023.4.7.1/tests/xcelery/test_celery.py
+-rw-r--r--   0        0        0       69 2023-04-07 09:03:02.123412 yyxx_game_pkg-2023.4.7.1/yyxx_game_pkg/__init__.py
+-rw-r--r--   0        0        0       83 2023-04-07 09:03:02.123412 yyxx_game_pkg-2023.4.7.1/yyxx_game_pkg/dbops/__init__.py
+-rw-r--r--   0        0        0     1331 2023-04-07 09:03:02.123412 yyxx_game_pkg-2023.4.7.1/yyxx_game_pkg/dbops/base.py
+-rw-r--r--   0        0        0     1295 2023-04-07 09:03:02.123412 yyxx_game_pkg-2023.4.7.1/yyxx_game_pkg/dbops/ch_op.py
+-rw-r--r--   0        0        0     5597 2023-04-07 09:03:02.123412 yyxx_game_pkg-2023.4.7.1/yyxx_game_pkg/dbops/das_api.py
+-rw-r--r--   0        0        0     1911 2023-04-07 09:03:02.123412 yyxx_game_pkg-2023.4.7.1/yyxx_game_pkg/dbops/es_op.py
+-rw-r--r--   0        0        0     1678 2023-04-07 09:03:02.123412 yyxx_game_pkg-2023.4.7.1/yyxx_game_pkg/dbops/hdfs_op.py
+-rw-r--r--   0        0        0      979 2023-04-07 09:03:02.123412 yyxx_game_pkg-2023.4.7.1/yyxx_game_pkg/dbops/mongo_op.py
+-rw-r--r--   0        0        0     3955 2023-04-07 09:03:02.123412 yyxx_game_pkg-2023.4.7.1/yyxx_game_pkg/dbops/mysql_op.py
+-rw-r--r--   0        0        0       81 2023-04-07 09:03:02.123412 yyxx_game_pkg-2023.4.7.1/yyxx_game_pkg/helpers/__init__.py
+-rw-r--r--   0        0        0     2099 2023-04-07 09:03:02.123412 yyxx_game_pkg-2023.4.7.1/yyxx_game_pkg/helpers/mysql_helper.py
+-rw-r--r--   0        0        0     1266 2023-04-07 09:03:02.123412 yyxx_game_pkg-2023.4.7.1/yyxx_game_pkg/helpers/pika_helper.py
+-rw-r--r--   0        0        0     2667 2023-04-07 09:03:02.123412 yyxx_game_pkg-2023.4.7.1/yyxx_game_pkg/helpers/redis_helper.py
+-rw-r--r--   0        0        0       79 2023-04-07 09:03:02.123412 yyxx_game_pkg-2023.4.7.1/yyxx_game_pkg/ip2region/__init__.py
+-rw-r--r--   0        0        0 11070130 2023-04-07 09:03:02.191409 yyxx_game_pkg-2023.4.7.1/yyxx_game_pkg/ip2region/ip2region.xdb
+-rw-r--r--   0        0        0      604 2023-04-07 09:03:02.191409 yyxx_game_pkg-2023.4.7.1/yyxx_game_pkg/ip2region/ip_x.py
+-rw-r--r--   0        0        0     5735 2023-04-07 09:03:02.191409 yyxx_game_pkg-2023.4.7.1/yyxx_game_pkg/ip2region/xdbSearcher.py
+-rw-r--r--   0        0        0       81 2023-04-07 09:03:02.191409 yyxx_game_pkg-2023.4.7.1/yyxx_game_pkg/logger/__init__.py
+-rw-r--r--   0        0        0     2326 2023-04-07 09:03:02.191409 yyxx_game_pkg-2023.4.7.1/yyxx_game_pkg/logger/config.py
+-rw-r--r--   0        0        0     3467 2023-04-07 09:03:02.191409 yyxx_game_pkg-2023.4.7.1/yyxx_game_pkg/logger/handlers.py
+-rw-r--r--   0        0        0     2154 2023-04-07 09:03:02.191409 yyxx_game_pkg-2023.4.7.1/yyxx_game_pkg/logger/log.py
+-rw-r--r--   0        0        0       70 2023-04-07 09:03:02.191409 yyxx_game_pkg-2023.4.7.1/yyxx_game_pkg/stat/__init__.py
+-rw-r--r--   0        0        0       68 2023-04-07 09:03:02.191409 yyxx_game_pkg-2023.4.7.1/yyxx_game_pkg/stat/dispatch/__init__.py
+-rw-r--r--   0        0        0       70 2023-04-07 09:03:02.191409 yyxx_game_pkg-2023.4.7.1/yyxx_game_pkg/stat/dispatch/common/__init__.py
+-rw-r--r--   0        0        0     1530 2023-04-07 09:03:02.191409 yyxx_game_pkg-2023.4.7.1/yyxx_game_pkg/stat/dispatch/common/common.py
+-rw-r--r--   0        0        0      378 2023-04-07 09:03:02.191409 yyxx_game_pkg-2023.4.7.1/yyxx_game_pkg/stat/dispatch/common/log.py
+-rw-r--r--   0        0        0       69 2023-04-07 09:03:02.191409 yyxx_game_pkg-2023.4.7.1/yyxx_game_pkg/stat/dispatch/core/__init__.py
+-rw-r--r--   0        0        0      805 2023-04-07 09:03:02.191409 yyxx_game_pkg-2023.4.7.1/yyxx_game_pkg/stat/dispatch/core/manager.py
+-rw-r--r--   0        0        0     1042 2023-04-07 09:03:02.191409 yyxx_game_pkg-2023.4.7.1/yyxx_game_pkg/stat/dispatch/core/structs.py
+-rw-r--r--   0        0        0     5533 2023-04-07 09:03:02.191409 yyxx_game_pkg-2023.4.7.1/yyxx_game_pkg/stat/dispatch/core/workflows.py
+-rw-r--r--   0        0        0      604 2023-04-07 09:03:02.191409 yyxx_game_pkg-2023.4.7.1/yyxx_game_pkg/stat/dispatch/dispatch.py
+-rw-r--r--   0        0        0       70 2023-04-07 09:03:02.191409 yyxx_game_pkg-2023.4.7.1/yyxx_game_pkg/stat/dispatch/logic/__init__.py
+-rw-r--r--   0        0        0     4418 2023-04-07 09:03:02.191409 yyxx_game_pkg-2023.4.7.1/yyxx_game_pkg/stat/dispatch/logic/task_logic.py
+-rw-r--r--   0        0        0      809 2023-04-07 09:03:02.191409 yyxx_game_pkg-2023.4.7.1/yyxx_game_pkg/stat/dispatch/route.py
+-rw-r--r--   0        0        0      693 2023-04-07 09:03:02.191409 yyxx_game_pkg-2023.4.7.1/yyxx_game_pkg/stat/dispatch/rules/__init__.py
+-rw-r--r--   0        0        0      689 2023-04-07 09:03:02.191409 yyxx_game_pkg-2023.4.7.1/yyxx_game_pkg/stat/dispatch/rules/rule_base.py
+-rw-r--r--   0        0        0     4286 2023-04-07 09:03:02.191409 yyxx_game_pkg-2023.4.7.1/yyxx_game_pkg/stat/dispatch/rules/rule_workflow.py
+-rw-r--r--   0        0        0       70 2023-04-07 09:03:02.191409 yyxx_game_pkg-2023.4.7.1/yyxx_game_pkg/stat/submit/__init__.py
+-rw-r--r--   0        0        0       70 2023-04-07 09:03:02.191409 yyxx_game_pkg-2023.4.7.1/yyxx_game_pkg/stat/submit/logic/__init__.py
+-rw-r--r--   0        0        0     5961 2023-04-07 09:03:02.191409 yyxx_game_pkg-2023.4.7.1/yyxx_game_pkg/stat/submit/logic/submit_logic.py
+-rw-r--r--   0        0        0      987 2023-04-07 09:03:02.191409 yyxx_game_pkg-2023.4.7.1/yyxx_game_pkg/stat/submit/submit.py
+-rw-r--r--   0        0        0       70 2023-04-07 09:03:02.191409 yyxx_game_pkg-2023.4.7.1/yyxx_game_pkg/stat/xcelery/__init__.py
+-rw-r--r--   0        0        0     2110 2023-04-07 09:03:02.191409 yyxx_game_pkg-2023.4.7.1/yyxx_game_pkg/stat/xcelery/instance.py
+-rw-r--r--   0        0        0      961 2023-04-07 09:03:02.191409 yyxx_game_pkg-2023.4.7.1/yyxx_game_pkg/stat/xcelery/task_base.py
+-rw-r--r--   0        0        0       83 2023-04-07 09:03:02.191409 yyxx_game_pkg-2023.4.7.1/yyxx_game_pkg/utils/__init__.py
+-rw-r--r--   0        0        0     5035 2023-04-07 09:03:02.191409 yyxx_game_pkg-2023.4.7.1/yyxx_game_pkg/utils/decorator.py
+-rw-r--r--   0        0        0     2845 2023-04-07 09:03:02.191409 yyxx_game_pkg-2023.4.7.1/yyxx_game_pkg/utils/profiler.py
+-rw-r--r--   0        0        0     3016 2023-04-07 09:03:02.191409 yyxx_game_pkg-2023.4.7.1/yyxx_game_pkg/utils/xListStr.py
+-rw-r--r--   0        0        0     5255 2023-04-07 09:03:02.191409 yyxx_game_pkg-2023.4.7.1/yyxx_game_pkg/utils/xdataframe.py
+-rw-r--r--   0        0        0     6161 2023-04-07 09:03:02.191409 yyxx_game_pkg-2023.4.7.1/yyxx_game_pkg/utils/xdate.py
+-rw-r--r--   0        0        0     3101 2023-04-07 09:03:02.191409 yyxx_game_pkg-2023.4.7.1/yyxx_game_pkg/utils/xhttp.py
+-rw-r--r--   0        0        0      971 2023-04-07 09:03:02.191409 yyxx_game_pkg-2023.4.7.1/yyxx_game_pkg/utils/xmath.py
+-rw-r--r--   0        0        0       69 2023-04-07 09:03:02.191409 yyxx_game_pkg-2023.4.7.1/yyxx_game_pkg/xtrace/__init__.py
+-rw-r--r--   0        0        0     2858 2023-04-07 09:03:02.191409 yyxx_game_pkg-2023.4.7.1/yyxx_game_pkg/xtrace/helper.py
+-rw-r--r--   0        0        0     5442 1970-01-01 00:00:00.000000 yyxx_game_pkg-2023.4.7.1/PKG-INFO
```

### Comparing `yyxx_game_pkg-2023.4.4.1/README.md` & `yyxx_game_pkg-2023.4.7.1/README.md`

 * *Files identical despite different names*

### Comparing `yyxx_game_pkg-2023.4.4.1/pyproject.toml` & `yyxx_game_pkg-2023.4.7.1/pyproject.toml`

 * *Files 1% similar despite different names*

```diff
@@ -1,14 +1,14 @@
 [build-system]
 equires = [ "poetry-core",]
 build-backend = "poetry.core.masonry.api"
 
 [tool.poetry]
 name = "yyxx-game-pkg"
-version = "v2023.04.04.001"
+version = "v2023.04.07.001"
 description = "yyxx game custom module"
 authors = [ "yyxx-game",]
 license = "MIT"
 homepage = "https://github.com/yyxxgame/yyxxgame-pkg"
 repository = "https://github.com/yyxxgame/yyxxgame-pkg"
 readme = "README.md"
 classifiers = [ "Programming Language :: Python :: 3", "License :: OSI Approved :: MIT License", "Operating System :: OS Independent",]
```

### Comparing `yyxx_game_pkg-2023.4.4.1/tests/dispatch/config/celery_local_config.py` & `yyxx_game_pkg-2023.4.7.1/tests/dispatch/config/celery_local_config.py`

 * *Files identical despite different names*

### Comparing `yyxx_game_pkg-2023.4.4.1/tests/dispatch/rules/__init__.py` & `yyxx_game_pkg-2023.4.7.1/tests/dispatch/rules/__init__.py`

 * *Files identical despite different names*

### Comparing `yyxx_game_pkg-2023.4.4.1/tests/dispatch/rules/rule_temp.py` & `yyxx_game_pkg-2023.4.7.1/tests/dispatch/rules/rule_temp.py`

 * *Files identical despite different names*

### Comparing `yyxx_game_pkg-2023.4.4.1/tests/dispatch/test_dispatch.py` & `yyxx_game_pkg-2023.4.7.1/tests/dispatch/test_dispatch.py`

 * *Files identical despite different names*

### Comparing `yyxx_game_pkg-2023.4.4.1/tests/submit/schedule_rule/schedule/work_flow/schedule_work_flow_test.py` & `yyxx_game_pkg-2023.4.7.1/tests/submit/schedule_rule/schedule/work_flow/schedule_work_flow_test.py`

 * *Files identical despite different names*

### Comparing `yyxx_game_pkg-2023.4.4.1/tests/submit/test_submit.py` & `yyxx_game_pkg-2023.4.7.1/tests/submit/test_submit.py`

 * *Files identical despite different names*

### Comparing `yyxx_game_pkg-2023.4.4.1/tests/test_logger.py` & `yyxx_game_pkg-2023.4.7.1/tests/test_logger.py`

 * *Files identical despite different names*

### Comparing `yyxx_game_pkg-2023.4.4.1/tests/test_xtrace.py` & `yyxx_game_pkg-2023.4.7.1/tests/test_xtrace.py`

 * *Files identical despite different names*

### Comparing `yyxx_game_pkg-2023.4.4.1/tests/xcelery/config/celery_local_config.py` & `yyxx_game_pkg-2023.4.7.1/tests/xcelery/config/celery_local_config.py`

 * *Files identical despite different names*

### Comparing `yyxx_game_pkg-2023.4.4.1/tests/xcelery/task_register.py` & `yyxx_game_pkg-2023.4.7.1/tests/xcelery/task_register.py`

 * *Files identical despite different names*

### Comparing `yyxx_game_pkg-2023.4.4.1/yyxx_game_pkg/dbops/base.py` & `yyxx_game_pkg-2023.4.7.1/yyxx_game_pkg/dbops/base.py`

 * *Files identical despite different names*

### Comparing `yyxx_game_pkg-2023.4.4.1/yyxx_game_pkg/dbops/ch_op.py` & `yyxx_game_pkg-2023.4.7.1/yyxx_game_pkg/dbops/ch_op.py`

 * *Files identical despite different names*

### Comparing `yyxx_game_pkg-2023.4.4.1/yyxx_game_pkg/dbops/das_api.py` & `yyxx_game_pkg-2023.4.7.1/yyxx_game_pkg/dbops/das_api.py`

 * *Files identical despite different names*

### Comparing `yyxx_game_pkg-2023.4.4.1/yyxx_game_pkg/dbops/es_op.py` & `yyxx_game_pkg-2023.4.7.1/yyxx_game_pkg/dbops/es_op.py`

 * *Files identical despite different names*

### Comparing `yyxx_game_pkg-2023.4.4.1/yyxx_game_pkg/dbops/hdfs_op.py` & `yyxx_game_pkg-2023.4.7.1/yyxx_game_pkg/dbops/hdfs_op.py`

 * *Files identical despite different names*

### Comparing `yyxx_game_pkg-2023.4.4.1/yyxx_game_pkg/dbops/mongo_op.py` & `yyxx_game_pkg-2023.4.7.1/yyxx_game_pkg/dbops/mongo_op.py`

 * *Files identical despite different names*

### Comparing `yyxx_game_pkg-2023.4.4.1/yyxx_game_pkg/dbops/mysql_op.py` & `yyxx_game_pkg-2023.4.7.1/yyxx_game_pkg/dbops/mysql_op.py`

 * *Files 4% similar despite different names*

```diff
@@ -7,63 +7,67 @@
 import pandas as pd
 from yyxx_game_pkg.dbops.base import DatabaseOperation
 from yyxx_game_pkg.utils import xListStr
 
 
 class MysqlOperation(DatabaseOperation):
     """
-    Mysql数据库操作
+    Mysql数据库操作 
     """
 
     def execute(self, sql, conn, params=None):
         """
         执行sql返回处理结果
         :param sql:
         :param conn:
         :param params:
         :return:
         """
-        cursor = conn.cursor()
-        if params is None:
-            cursor.execute(sql)
-        else:
-            cursor.execute(sql, params)
-        return cursor.submit()
+        sql = self.check_sql(sql)
+        with conn:
+            with conn.cursor() as cursor:
+                if params is None:
+                    cursor.execute(sql)
+                else:
+                    cursor.execute(sql, params)
+                conn.commit()
 
     def get_one(self, sql, conn, params=None):
         """
         查询一条数据, 返回元组结构
         :param sql:
         :param conn:
         :param params:
         :return:
         """
-        cursor = conn.cursor()
         sql = self.check_sql(sql)
-        if params is None:
-            cursor.execute(sql)
-        else:
-            cursor.execute(sql, params)
-        return cursor.fetchone()
+        with conn:
+            with conn.cursor() as cursor:
+                if params is None:
+                    cursor.execute(sql)
+                else:
+                    cursor.execute(sql, params)
+                return cursor.fetchone()
 
     def get_all(self, sql, conn, params=None):
         """
         查询多条数据，返回list(元组) 结构
         :param sql:
         :param conn:
         :param params:
         :return:
         """
-        cursor = conn.cursor()
         sql = self.check_sql(sql)
-        if params is None:
-            cursor.execute(sql)
-        else:
-            cursor.execute(sql, params)
-        return cursor.fetchall()
+        with conn:
+            with conn.cursor() as cursor:
+                if params is None:
+                    cursor.execute(sql)
+                else:
+                    cursor.execute(sql, params)
+                return cursor.fetchall()
 
     def get_one_df(self, *args, **kwargs):
         """
         获取单次数据
         :param args:
         :param kwargs:
         :return:
@@ -72,63 +76,63 @@
     def get_all_df(self, sql, connection):
         """
         获取所有数据 dataframe
         :param sql:
         :param connection:
         :return:
         """
-        pd.read_sql(sql, connection)
+        return pd.read_sql(sql, connection)
 
     def insert(self, conn, save_table, results):
         """
         :param conn:
         :param save_table:
         :param results:
         :return:
         """
-        cursor = conn.cursor()
-
         def get_field_str(_data):
             """
             根据数据长度生成{data_value}
             :param _data:
             :return:
             """
             _size = len(_data[0])
             _list = []
             for _ in range(_size):
                 _list.append("%s")
             _str = ",".join(_list)
             return _str
 
-        def get_table_desc(_table_name, _data_list):
+        def get_table_desc(_table_name, _data_list, _cs):
             """
             :param _table_name:
             :param _data_list:
             :return:
             """
             sql = f"describe {_table_name}"
-            cursor.execute(sql)
-            _desc = cursor.fetchall()
+            _cs.execute(sql)
+            _desc = _cs.fetchall()
             _column = []
             for _data in _desc:
                 if _data[0] in ("id", "create_time"):  # 自增id和默认插入时间过滤
                     continue
                 _column.append(_data[0])
             _size = len(_data_list[0])
             table_column = _column[:_size]
             return ",".join(table_column)
 
         insert_sql_template = (
             "INSERT INTO {save_table} ({column_value}) VALUES({data_value})"
         )
         results = xListStr.split_list(results)
-        for result in results:
-            if not result:
-                continue
-            field_str = get_field_str(result)
-            column_value = get_table_desc(save_table, result)
-            insert_sql = insert_sql_template.format(
-                save_table=save_table, column_value=column_value, data_value=field_str
-            )
-            cursor.executemany(insert_sql, result)
-            conn.commit()
+        with conn:
+            with conn.cursor() as cursor:
+                for result in results:
+                    if not result:
+                        continue
+                    field_str = get_field_str(result)
+                    column_value = get_table_desc(save_table, result, cursor)
+                    insert_sql = insert_sql_template.format(
+                        save_table=save_table, column_value=column_value, data_value=field_str
+                    )
+                    cursor.executemany(insert_sql, result)
+                    conn.commit()
```

### Comparing `yyxx_game_pkg-2023.4.4.1/yyxx_game_pkg/helpers/mysql_helper.py` & `yyxx_game_pkg-2023.4.7.1/yyxx_game_pkg/helpers/mysql_helper.py`

 * *Files 1% similar despite different names*

```diff
@@ -31,15 +31,15 @@
     USER = None
     PASSWD = None
     DB = None
     USE_UNICODE = None
     CHARSET = None
 
     def __str__(self):
-        return "host:{},port:{}, db:{},use_unicode:{},charset:{}".format(
+        return "host:{},port:{},db:{},use_unicode:{},charset:{}".format(
             self.HOST, self.PORT, self.DB, self.USE_UNICODE, self.CHARSET
         )
 
 
 @singleton_unique
 class MysqlDbPool(object):
```

### Comparing `yyxx_game_pkg-2023.4.4.1/yyxx_game_pkg/helpers/pika_helper.py` & `yyxx_game_pkg-2023.4.7.1/yyxx_game_pkg/helpers/pika_helper.py`

 * *Files identical despite different names*

### Comparing `yyxx_game_pkg-2023.4.4.1/yyxx_game_pkg/helpers/redis_helper.py` & `yyxx_game_pkg-2023.4.7.1/yyxx_game_pkg/helpers/redis_helper.py`

 * *Files identical despite different names*

### Comparing `yyxx_game_pkg-2023.4.4.1/yyxx_game_pkg/ip2region/ip2region.xdb` & `yyxx_game_pkg-2023.4.7.1/yyxx_game_pkg/ip2region/ip2region.xdb`

 * *Files identical despite different names*

### Comparing `yyxx_game_pkg-2023.4.4.1/yyxx_game_pkg/ip2region/ip_x.py` & `yyxx_game_pkg-2023.4.7.1/yyxx_game_pkg/ip2region/ip_x.py`

 * *Files identical despite different names*

### Comparing `yyxx_game_pkg-2023.4.4.1/yyxx_game_pkg/ip2region/xdbSearcher.py` & `yyxx_game_pkg-2023.4.7.1/yyxx_game_pkg/ip2region/xdbSearcher.py`

 * *Files identical despite different names*

### Comparing `yyxx_game_pkg-2023.4.4.1/yyxx_game_pkg/logger/config.py` & `yyxx_game_pkg-2023.4.7.1/yyxx_game_pkg/logger/config.py`

 * *Files identical despite different names*

### Comparing `yyxx_game_pkg-2023.4.4.1/yyxx_game_pkg/logger/handlers.py` & `yyxx_game_pkg-2023.4.7.1/yyxx_game_pkg/logger/handlers.py`

 * *Files identical despite different names*

### Comparing `yyxx_game_pkg-2023.4.4.1/yyxx_game_pkg/logger/log.py` & `yyxx_game_pkg-2023.4.7.1/yyxx_game_pkg/logger/log.py`

 * *Files identical despite different names*

### Comparing `yyxx_game_pkg-2023.4.4.1/yyxx_game_pkg/stat/dispatch/common/common.py` & `yyxx_game_pkg-2023.4.7.1/yyxx_game_pkg/stat/dispatch/common/common.py`

 * *Files identical despite different names*

### Comparing `yyxx_game_pkg-2023.4.4.1/yyxx_game_pkg/stat/dispatch/core/manager.py` & `yyxx_game_pkg-2023.4.7.1/yyxx_game_pkg/stat/dispatch/core/manager.py`

 * *Files identical despite different names*

### Comparing `yyxx_game_pkg-2023.4.4.1/yyxx_game_pkg/stat/dispatch/core/structs.py` & `yyxx_game_pkg-2023.4.7.1/yyxx_game_pkg/stat/dispatch/core/structs.py`

 * *Files identical despite different names*

### Comparing `yyxx_game_pkg-2023.4.4.1/yyxx_game_pkg/stat/dispatch/core/workflows.py` & `yyxx_game_pkg-2023.4.7.1/yyxx_game_pkg/stat/dispatch/core/workflows.py`

 * *Files identical despite different names*

### Comparing `yyxx_game_pkg-2023.4.4.1/yyxx_game_pkg/stat/dispatch/dispatch.py` & `yyxx_game_pkg-2023.4.7.1/yyxx_game_pkg/stat/dispatch/dispatch.py`

 * *Files identical despite different names*

### Comparing `yyxx_game_pkg-2023.4.4.1/yyxx_game_pkg/stat/dispatch/logic/task_logic.py` & `yyxx_game_pkg-2023.4.7.1/yyxx_game_pkg/stat/dispatch/logic/task_logic.py`

 * *Files identical despite different names*

### Comparing `yyxx_game_pkg-2023.4.4.1/yyxx_game_pkg/stat/dispatch/route.py` & `yyxx_game_pkg-2023.4.7.1/yyxx_game_pkg/stat/dispatch/route.py`

 * *Files identical despite different names*

### Comparing `yyxx_game_pkg-2023.4.4.1/yyxx_game_pkg/stat/dispatch/rules/__init__.py` & `yyxx_game_pkg-2023.4.7.1/yyxx_game_pkg/stat/dispatch/rules/__init__.py`

 * *Files identical despite different names*

### Comparing `yyxx_game_pkg-2023.4.4.1/yyxx_game_pkg/stat/dispatch/rules/rule_base.py` & `yyxx_game_pkg-2023.4.7.1/yyxx_game_pkg/stat/dispatch/rules/rule_base.py`

 * *Files identical despite different names*

### Comparing `yyxx_game_pkg-2023.4.4.1/yyxx_game_pkg/stat/dispatch/rules/rule_workflow.py` & `yyxx_game_pkg-2023.4.7.1/yyxx_game_pkg/stat/dispatch/rules/rule_workflow.py`

 * *Files identical despite different names*

### Comparing `yyxx_game_pkg-2023.4.4.1/yyxx_game_pkg/stat/submit/logic/submit_logic.py` & `yyxx_game_pkg-2023.4.7.1/yyxx_game_pkg/stat/submit/logic/submit_logic.py`

 * *Files identical despite different names*

### Comparing `yyxx_game_pkg-2023.4.4.1/yyxx_game_pkg/stat/submit/submit.py` & `yyxx_game_pkg-2023.4.7.1/yyxx_game_pkg/stat/submit/submit.py`

 * *Files identical despite different names*

### Comparing `yyxx_game_pkg-2023.4.4.1/yyxx_game_pkg/stat/xcelery/instance.py` & `yyxx_game_pkg-2023.4.7.1/yyxx_game_pkg/stat/xcelery/instance.py`

 * *Files identical despite different names*

### Comparing `yyxx_game_pkg-2023.4.4.1/yyxx_game_pkg/stat/xcelery/task_base.py` & `yyxx_game_pkg-2023.4.7.1/yyxx_game_pkg/stat/xcelery/task_base.py`

 * *Files identical despite different names*

### Comparing `yyxx_game_pkg-2023.4.4.1/yyxx_game_pkg/utils/decorator.py` & `yyxx_game_pkg-2023.4.7.1/yyxx_game_pkg/utils/decorator.py`

 * *Files identical despite different names*

### Comparing `yyxx_game_pkg-2023.4.4.1/yyxx_game_pkg/utils/profiler.py` & `yyxx_game_pkg-2023.4.7.1/yyxx_game_pkg/utils/profiler.py`

 * *Files identical despite different names*

### Comparing `yyxx_game_pkg-2023.4.4.1/yyxx_game_pkg/utils/xListStr.py` & `yyxx_game_pkg-2023.4.7.1/yyxx_game_pkg/utils/xListStr.py`

 * *Files 2% similar despite different names*

```diff
@@ -82,15 +82,15 @@
     split_list([1, 2, 3, 4, 5], 3) -> [[1, 2, 3], [4, 5]]
     :param pending_lst:
     :param split_size:
     :return:
     """
     if not isinstance(pending_lst, (list, tuple)):
         return pending_lst
-    if len(pending_lst) != 1:
+    if not isinstance(pending_lst[0], (list, tuple)):
         pending_lst = [pending_lst]
     base_num = split_size
     result = pending_lst[0]
     size = len(result) / base_num
     if len(result) % base_num != 0:
         size += 1
     data_list = []
```

### Comparing `yyxx_game_pkg-2023.4.4.1/yyxx_game_pkg/utils/xdataframe.py` & `yyxx_game_pkg-2023.4.7.1/yyxx_game_pkg/utils/xdataframe.py`

 * *Files identical despite different names*

### Comparing `yyxx_game_pkg-2023.4.4.1/yyxx_game_pkg/utils/xdate.py` & `yyxx_game_pkg-2023.4.7.1/yyxx_game_pkg/utils/xdate.py`

 * *Files identical despite different names*

### Comparing `yyxx_game_pkg-2023.4.4.1/yyxx_game_pkg/utils/xhttp.py` & `yyxx_game_pkg-2023.4.7.1/yyxx_game_pkg/utils/xhttp.py`

 * *Files identical despite different names*

### Comparing `yyxx_game_pkg-2023.4.4.1/yyxx_game_pkg/utils/xmath.py` & `yyxx_game_pkg-2023.4.7.1/yyxx_game_pkg/utils/xmath.py`

 * *Files identical despite different names*

### Comparing `yyxx_game_pkg-2023.4.4.1/yyxx_game_pkg/xtrace/helper.py` & `yyxx_game_pkg-2023.4.7.1/yyxx_game_pkg/xtrace/helper.py`

 * *Files identical despite different names*

### Comparing `yyxx_game_pkg-2023.4.4.1/PKG-INFO` & `yyxx_game_pkg-2023.4.7.1/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: yyxx-game-pkg
-Version: 2023.4.4.1
+Version: 2023.4.7.1
 Summary: yyxx game custom module
 Home-page: https://github.com/yyxxgame/yyxxgame-pkg
 License: MIT
 Author: yyxx-game
 Requires-Python: >=3.8,<4
 Classifier: License :: OSI Approved :: MIT License
 Classifier: Operating System :: OS Independent
```

#### html2text {}

```diff
@@ -1,8 +1,8 @@
-Metadata-Version: 2.1 Name: yyxx-game-pkg Version: 2023.4.4.1 Summary: yyxx
+Metadata-Version: 2.1 Name: yyxx-game-pkg Version: 2023.4.7.1 Summary: yyxx
 game custom module Home-page: https://github.com/yyxxgame/yyxxgame-pkg License:
 MIT Author: yyxx-game Requires-Python: >=3.8,<4 Classifier: License :: OSI
 Approved :: MIT License Classifier: Operating System :: OS Independent
 Classifier: Programming Language :: Python :: 3 Classifier: Programming
 Language :: Python :: 3.8 Classifier: Programming Language :: Python :: 3.9
 Classifier: Programming Language :: Python :: 3.10 Classifier: Programming
 Language :: Python :: 3.11 Classifier: Programming Language :: Python :: 3
```

