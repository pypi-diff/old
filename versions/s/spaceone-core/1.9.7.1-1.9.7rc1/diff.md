# Comparing `tmp/spaceone_core-1.9.7.1-py3-none-any.whl.zip` & `tmp/spaceone_core-1.9.7rc1-py3-none-any.whl.zip`

## zipinfo {}

```diff
@@ -1,90 +1,90 @@
-Zip file size: 74645 bytes, number of entries: 88
--rw-r--r--  2.0 unx       64 b- defN 22-May-26 09:29 spaceone/__init__.py
--rw-r--r--  2.0 unx       14 b- defN 22-May-26 09:29 spaceone/core/__init__.py
--rw-r--r--  2.0 unx      355 b- defN 22-May-26 09:29 spaceone/core/base.py
--rw-r--r--  2.0 unx     6806 b- defN 22-May-26 09:29 spaceone/core/command.py
--rw-r--r--  2.0 unx     7039 b- defN 22-May-26 09:29 spaceone/core/error.py
--rw-r--r--  2.0 unx     2764 b- defN 22-May-26 09:29 spaceone/core/locator.py
--rw-r--r--  2.0 unx      324 b- defN 22-May-26 09:29 spaceone/core/manager.py
--rw-r--r--  2.0 unx     2520 b- defN 22-May-26 09:29 spaceone/core/token.py
--rw-r--r--  2.0 unx     2979 b- defN 22-May-26 09:29 spaceone/core/transaction.py
--rw-r--r--  2.0 unx    12782 b- defN 22-May-26 09:29 spaceone/core/utils.py
--rw-r--r--  2.0 unx      215 b- defN 22-May-26 09:29 spaceone/core/auth/__init__.py
--rw-r--r--  2.0 unx      779 b- defN 22-May-26 09:29 spaceone/core/auth/jwt/__init__.py
--rw-r--r--  2.0 unx      942 b- defN 22-May-26 09:29 spaceone/core/auth/jwt/jwt_util.py
--rw-r--r--  2.0 unx     6505 b- defN 22-May-26 09:29 spaceone/core/cache/__init__.py
--rw-r--r--  2.0 unx      902 b- defN 22-May-26 09:29 spaceone/core/cache/local_cache.py
--rw-r--r--  2.0 unx     2192 b- defN 22-May-26 09:29 spaceone/core/cache/redis_cache.py
--rw-r--r--  2.0 unx        0 b- defN 22-May-26 09:29 spaceone/core/celery/__init__.py
--rw-r--r--  2.0 unx     2731 b- defN 22-May-26 09:29 spaceone/core/celery/app.py
--rw-r--r--  2.0 unx     5053 b- defN 22-May-26 09:29 spaceone/core/celery/schedulers.py
--rw-r--r--  2.0 unx      683 b- defN 22-May-26 09:29 spaceone/core/celery/service.py
--rw-r--r--  2.0 unx     4679 b- defN 22-May-26 09:29 spaceone/core/celery/tasks.py
--rw-r--r--  2.0 unx     1679 b- defN 22-May-26 09:29 spaceone/core/celery/types.py
--rw-r--r--  2.0 unx     3878 b- defN 22-May-26 09:29 spaceone/core/config/__init__.py
--rw-r--r--  2.0 unx      700 b- defN 22-May-26 09:29 spaceone/core/config/default_conf.py
--rw-r--r--  2.0 unx      383 b- defN 22-May-26 09:29 spaceone/core/connector/__init__.py
--rw-r--r--  2.0 unx     4175 b- defN 22-May-26 09:29 spaceone/core/connector/space_connector.py
--rw-r--r--  2.0 unx        0 b- defN 22-May-26 09:29 spaceone/core/extension/__init__.py
--rw-r--r--  2.0 unx     1855 b- defN 22-May-26 09:29 spaceone/core/extension/grpc_health.py
--rw-r--r--  2.0 unx     1751 b- defN 22-May-26 09:29 spaceone/core/extension/server_info.py
--rw-r--r--  2.0 unx       69 b- defN 22-May-26 09:29 spaceone/core/fastapi/__init__.py
--rw-r--r--  2.0 unx      744 b- defN 22-May-26 09:29 spaceone/core/fastapi/server.py
--rw-r--r--  2.0 unx     1832 b- defN 22-May-26 09:29 spaceone/core/handler/__init__.py
--rw-r--r--  2.0 unx     2640 b- defN 22-May-26 09:29 spaceone/core/handler/authentication_api_key_handler.py
--rw-r--r--  2.0 unx     3449 b- defN 22-May-26 09:29 spaceone/core/handler/authentication_handler.py
--rw-r--r--  2.0 unx     3650 b- defN 22-May-26 09:29 spaceone/core/handler/authorization_handler.py
--rw-r--r--  2.0 unx     1304 b- defN 22-May-26 09:29 spaceone/core/handler/event_handler.py
--rw-r--r--  2.0 unx     2239 b- defN 22-May-26 09:29 spaceone/core/handler/mutation_handler.py
--rw-r--r--  2.0 unx     4735 b- defN 22-May-26 09:29 spaceone/core/logger/__init__.py
--rw-r--r--  2.0 unx      496 b- defN 22-May-26 09:29 spaceone/core/logger/filters/__init__.py
--rw-r--r--  2.0 unx      492 b- defN 22-May-26 09:29 spaceone/core/logger/filters/error.py
--rw-r--r--  2.0 unx      316 b- defN 22-May-26 09:29 spaceone/core/logger/filters/exclude.py
--rw-r--r--  2.0 unx     1146 b- defN 22-May-26 09:29 spaceone/core/logger/filters/masking.py
--rw-r--r--  2.0 unx      295 b- defN 22-May-26 09:29 spaceone/core/logger/filters/message.py
--rw-r--r--  2.0 unx      608 b- defN 22-May-26 09:29 spaceone/core/logger/filters/parameter.py
--rw-r--r--  2.0 unx      694 b- defN 22-May-26 09:29 spaceone/core/logger/filters/traceback.py
--rw-r--r--  2.0 unx      800 b- defN 22-May-26 09:29 spaceone/core/logger/filters/transaction.py
--rw-r--r--  2.0 unx     6898 b- defN 22-May-26 09:29 spaceone/core/model/__init__.py
--rw-r--r--  2.0 unx    31183 b- defN 22-May-26 09:29 spaceone/core/model/mongo_model/__init__.py
--rw-r--r--  2.0 unx     3549 b- defN 22-May-26 09:29 spaceone/core/model/mongo_model/filter_operator.py
--rw-r--r--  2.0 unx     4962 b- defN 22-May-26 09:29 spaceone/core/model/mongo_model/stat_operator.py
--rw-r--r--  2.0 unx      216 b- defN 22-May-26 09:29 spaceone/core/pygrpc/__init__.py
--rw-r--r--  2.0 unx     4421 b- defN 22-May-26 09:29 spaceone/core/pygrpc/api.py
--rw-r--r--  2.0 unx    19058 b- defN 22-May-26 09:29 spaceone/core/pygrpc/client.py
--rw-r--r--  2.0 unx     4040 b- defN 22-May-26 09:29 spaceone/core/pygrpc/message_type.py
--rw-r--r--  2.0 unx     3680 b- defN 22-May-26 09:29 spaceone/core/pygrpc/server.py
--rw-r--r--  2.0 unx     1556 b- defN 22-May-26 09:29 spaceone/core/queue/__init__.py
--rw-r--r--  2.0 unx     3483 b- defN 22-May-26 09:29 spaceone/core/queue/redis_queue.py
--rw-r--r--  2.0 unx      201 b- defN 22-May-26 09:29 spaceone/core/scheduler/__init__.py
--rw-r--r--  2.0 unx     4169 b- defN 22-May-26 09:29 spaceone/core/scheduler/scheduler.py
--rw-r--r--  2.0 unx     3815 b- defN 22-May-26 09:29 spaceone/core/scheduler/server.py
--rw-r--r--  2.0 unx     1572 b- defN 22-May-26 09:29 spaceone/core/scheduler/task_schema.py
--rw-r--r--  2.0 unx     3646 b- defN 22-May-26 09:29 spaceone/core/scheduler/worker.py
--rw-r--r--  2.0 unx      418 b- defN 22-May-26 09:29 spaceone/core/service/__init__.py
--rw-r--r--  2.0 unx     8496 b- defN 22-May-26 09:29 spaceone/core/service/service.py
--rw-r--r--  2.0 unx     9588 b- defN 22-May-26 09:29 spaceone/core/service/utils.py
--rw-r--r--  2.0 unx        0 b- defN 22-May-26 09:29 spaceone/core/skeleton/__init__.py
--rw-r--r--  2.0 unx        0 b- defN 22-May-26 09:29 spaceone/core/skeleton/api/__init__.py
--rw-r--r--  2.0 unx      532 b- defN 22-May-26 09:29 spaceone/core/skeleton/api/helloworld.py
--rw-r--r--  2.0 unx        0 b- defN 22-May-26 09:29 spaceone/core/skeleton/conf/__init__.py
--rw-r--r--  2.0 unx     1253 b- defN 22-May-26 09:29 spaceone/core/skeleton/conf/global_conf.py
--rw-r--r--  2.0 unx        0 b- defN 22-May-26 09:29 spaceone/core/skeleton/conf/proto_conf.py
--rw-r--r--  2.0 unx        0 b- defN 22-May-26 09:29 spaceone/core/skeleton/connector/__init__.py
--rw-r--r--  2.0 unx        0 b- defN 22-May-26 09:29 spaceone/core/skeleton/error/__init__.py
--rw-r--r--  2.0 unx        0 b- defN 22-May-26 09:29 spaceone/core/skeleton/info/__init__.py
--rw-r--r--  2.0 unx      203 b- defN 22-May-26 09:29 spaceone/core/skeleton/info/helloworld_info.py
--rw-r--r--  2.0 unx        0 b- defN 22-May-26 09:29 spaceone/core/skeleton/manager/__init__.py
--rw-r--r--  2.0 unx      184 b- defN 22-May-26 09:29 spaceone/core/skeleton/manager/helloworld_manager.py
--rw-r--r--  2.0 unx        0 b- defN 22-May-26 09:29 spaceone/core/skeleton/model/__init__.py
--rw-r--r--  2.0 unx        0 b- defN 22-May-26 09:29 spaceone/core/skeleton/service/__init__.py
--rw-r--r--  2.0 unx      379 b- defN 22-May-26 09:29 spaceone/core/skeleton/service/helloworld_service.py
--rw-r--r--  2.0 unx        0 b- defN 22-May-26 09:29 spaceone/core/unittest/__init__.py
--rw-r--r--  2.0 unx     2848 b- defN 22-May-26 09:29 spaceone/core/unittest/result.py
--rw-r--r--  2.0 unx      579 b- defN 22-May-26 09:29 spaceone/core/unittest/runner.py
--rw-r--r--  2.0 unx      853 b- defN 22-May-26 09:29 spaceone_core-1.9.7.1.dist-info/METADATA
--rw-r--r--  2.0 unx       92 b- defN 22-May-26 09:29 spaceone_core-1.9.7.1.dist-info/WHEEL
--rw-r--r--  2.0 unx       56 b- defN 22-May-26 09:29 spaceone_core-1.9.7.1.dist-info/entry_points.txt
--rw-r--r--  2.0 unx        9 b- defN 22-May-26 09:29 spaceone_core-1.9.7.1.dist-info/top_level.txt
-?rw-rw-r--  2.0 unx     8028 b- defN 22-May-26 09:29 spaceone_core-1.9.7.1.dist-info/RECORD
-88 files, 230225 bytes uncompressed, 61653 bytes compressed:  73.2%
+Zip file size: 74648 bytes, number of entries: 88
+-rw-r--r--  2.0 unx       64 b- defN 22-May-17 06:01 spaceone/__init__.py
+-rw-r--r--  2.0 unx       14 b- defN 22-May-17 06:01 spaceone/core/__init__.py
+-rw-r--r--  2.0 unx      355 b- defN 22-May-17 06:01 spaceone/core/base.py
+-rw-r--r--  2.0 unx     6806 b- defN 22-May-17 06:01 spaceone/core/command.py
+-rw-r--r--  2.0 unx     7039 b- defN 22-May-17 06:01 spaceone/core/error.py
+-rw-r--r--  2.0 unx     2764 b- defN 22-May-17 06:01 spaceone/core/locator.py
+-rw-r--r--  2.0 unx      324 b- defN 22-May-17 06:01 spaceone/core/manager.py
+-rw-r--r--  2.0 unx     2520 b- defN 22-May-17 06:01 spaceone/core/token.py
+-rw-r--r--  2.0 unx     2979 b- defN 22-May-17 06:01 spaceone/core/transaction.py
+-rw-r--r--  2.0 unx    12781 b- defN 22-May-17 06:01 spaceone/core/utils.py
+-rw-r--r--  2.0 unx      215 b- defN 22-May-17 06:01 spaceone/core/auth/__init__.py
+-rw-r--r--  2.0 unx      779 b- defN 22-May-17 06:01 spaceone/core/auth/jwt/__init__.py
+-rw-r--r--  2.0 unx      942 b- defN 22-May-17 06:01 spaceone/core/auth/jwt/jwt_util.py
+-rw-r--r--  2.0 unx     6505 b- defN 22-May-17 06:01 spaceone/core/cache/__init__.py
+-rw-r--r--  2.0 unx      902 b- defN 22-May-17 06:01 spaceone/core/cache/local_cache.py
+-rw-r--r--  2.0 unx     2192 b- defN 22-May-17 06:01 spaceone/core/cache/redis_cache.py
+-rw-r--r--  2.0 unx        0 b- defN 22-May-17 06:01 spaceone/core/celery/__init__.py
+-rw-r--r--  2.0 unx     2731 b- defN 22-May-17 06:01 spaceone/core/celery/app.py
+-rw-r--r--  2.0 unx     5053 b- defN 22-May-17 06:01 spaceone/core/celery/schedulers.py
+-rw-r--r--  2.0 unx      683 b- defN 22-May-17 06:01 spaceone/core/celery/service.py
+-rw-r--r--  2.0 unx     4679 b- defN 22-May-17 06:01 spaceone/core/celery/tasks.py
+-rw-r--r--  2.0 unx     1679 b- defN 22-May-17 06:01 spaceone/core/celery/types.py
+-rw-r--r--  2.0 unx     3878 b- defN 22-May-17 06:01 spaceone/core/config/__init__.py
+-rw-r--r--  2.0 unx      700 b- defN 22-May-17 06:01 spaceone/core/config/default_conf.py
+-rw-r--r--  2.0 unx      383 b- defN 22-May-17 06:01 spaceone/core/connector/__init__.py
+-rw-r--r--  2.0 unx     4175 b- defN 22-May-17 06:01 spaceone/core/connector/space_connector.py
+-rw-r--r--  2.0 unx        0 b- defN 22-May-17 06:01 spaceone/core/extension/__init__.py
+-rw-r--r--  2.0 unx     1855 b- defN 22-May-17 06:01 spaceone/core/extension/grpc_health.py
+-rw-r--r--  2.0 unx     1751 b- defN 22-May-17 06:01 spaceone/core/extension/server_info.py
+-rw-r--r--  2.0 unx       69 b- defN 22-May-17 06:01 spaceone/core/fastapi/__init__.py
+-rw-r--r--  2.0 unx      744 b- defN 22-May-17 06:01 spaceone/core/fastapi/server.py
+-rw-r--r--  2.0 unx     1832 b- defN 22-May-17 06:01 spaceone/core/handler/__init__.py
+-rw-r--r--  2.0 unx     2640 b- defN 22-May-17 06:01 spaceone/core/handler/authentication_api_key_handler.py
+-rw-r--r--  2.0 unx     3449 b- defN 22-May-17 06:01 spaceone/core/handler/authentication_handler.py
+-rw-r--r--  2.0 unx     3650 b- defN 22-May-17 06:01 spaceone/core/handler/authorization_handler.py
+-rw-r--r--  2.0 unx     1304 b- defN 22-May-17 06:01 spaceone/core/handler/event_handler.py
+-rw-r--r--  2.0 unx     2239 b- defN 22-May-17 06:01 spaceone/core/handler/mutation_handler.py
+-rw-r--r--  2.0 unx     4735 b- defN 22-May-17 06:01 spaceone/core/logger/__init__.py
+-rw-r--r--  2.0 unx      496 b- defN 22-May-17 06:01 spaceone/core/logger/filters/__init__.py
+-rw-r--r--  2.0 unx      492 b- defN 22-May-17 06:01 spaceone/core/logger/filters/error.py
+-rw-r--r--  2.0 unx      316 b- defN 22-May-17 06:01 spaceone/core/logger/filters/exclude.py
+-rw-r--r--  2.0 unx     1146 b- defN 22-May-17 06:01 spaceone/core/logger/filters/masking.py
+-rw-r--r--  2.0 unx      295 b- defN 22-May-17 06:01 spaceone/core/logger/filters/message.py
+-rw-r--r--  2.0 unx      608 b- defN 22-May-17 06:01 spaceone/core/logger/filters/parameter.py
+-rw-r--r--  2.0 unx      694 b- defN 22-May-17 06:01 spaceone/core/logger/filters/traceback.py
+-rw-r--r--  2.0 unx      800 b- defN 22-May-17 06:01 spaceone/core/logger/filters/transaction.py
+-rw-r--r--  2.0 unx     6898 b- defN 22-May-17 06:01 spaceone/core/model/__init__.py
+-rw-r--r--  2.0 unx    31183 b- defN 22-May-17 06:01 spaceone/core/model/mongo_model/__init__.py
+-rw-r--r--  2.0 unx     3549 b- defN 22-May-17 06:01 spaceone/core/model/mongo_model/filter_operator.py
+-rw-r--r--  2.0 unx     4962 b- defN 22-May-17 06:01 spaceone/core/model/mongo_model/stat_operator.py
+-rw-r--r--  2.0 unx      216 b- defN 22-May-17 06:01 spaceone/core/pygrpc/__init__.py
+-rw-r--r--  2.0 unx     4421 b- defN 22-May-17 06:01 spaceone/core/pygrpc/api.py
+-rw-r--r--  2.0 unx    19058 b- defN 22-May-17 06:01 spaceone/core/pygrpc/client.py
+-rw-r--r--  2.0 unx     4040 b- defN 22-May-17 06:01 spaceone/core/pygrpc/message_type.py
+-rw-r--r--  2.0 unx     3680 b- defN 22-May-17 06:01 spaceone/core/pygrpc/server.py
+-rw-r--r--  2.0 unx     1556 b- defN 22-May-17 06:01 spaceone/core/queue/__init__.py
+-rw-r--r--  2.0 unx     3483 b- defN 22-May-17 06:01 spaceone/core/queue/redis_queue.py
+-rw-r--r--  2.0 unx      201 b- defN 22-May-17 06:01 spaceone/core/scheduler/__init__.py
+-rw-r--r--  2.0 unx     4169 b- defN 22-May-17 06:01 spaceone/core/scheduler/scheduler.py
+-rw-r--r--  2.0 unx     3815 b- defN 22-May-17 06:01 spaceone/core/scheduler/server.py
+-rw-r--r--  2.0 unx     1572 b- defN 22-May-17 06:01 spaceone/core/scheduler/task_schema.py
+-rw-r--r--  2.0 unx     3646 b- defN 22-May-17 06:01 spaceone/core/scheduler/worker.py
+-rw-r--r--  2.0 unx      418 b- defN 22-May-17 06:01 spaceone/core/service/__init__.py
+-rw-r--r--  2.0 unx     8496 b- defN 22-May-17 06:01 spaceone/core/service/service.py
+-rw-r--r--  2.0 unx     9588 b- defN 22-May-17 06:01 spaceone/core/service/utils.py
+-rw-r--r--  2.0 unx        0 b- defN 22-May-17 06:01 spaceone/core/skeleton/__init__.py
+-rw-r--r--  2.0 unx        0 b- defN 22-May-17 06:01 spaceone/core/skeleton/api/__init__.py
+-rw-r--r--  2.0 unx      532 b- defN 22-May-17 06:01 spaceone/core/skeleton/api/helloworld.py
+-rw-r--r--  2.0 unx        0 b- defN 22-May-17 06:01 spaceone/core/skeleton/conf/__init__.py
+-rw-r--r--  2.0 unx     1253 b- defN 22-May-17 06:01 spaceone/core/skeleton/conf/global_conf.py
+-rw-r--r--  2.0 unx        0 b- defN 22-May-17 06:01 spaceone/core/skeleton/conf/proto_conf.py
+-rw-r--r--  2.0 unx        0 b- defN 22-May-17 06:01 spaceone/core/skeleton/connector/__init__.py
+-rw-r--r--  2.0 unx        0 b- defN 22-May-17 06:01 spaceone/core/skeleton/error/__init__.py
+-rw-r--r--  2.0 unx        0 b- defN 22-May-17 06:01 spaceone/core/skeleton/info/__init__.py
+-rw-r--r--  2.0 unx      203 b- defN 22-May-17 06:01 spaceone/core/skeleton/info/helloworld_info.py
+-rw-r--r--  2.0 unx        0 b- defN 22-May-17 06:01 spaceone/core/skeleton/manager/__init__.py
+-rw-r--r--  2.0 unx      184 b- defN 22-May-17 06:01 spaceone/core/skeleton/manager/helloworld_manager.py
+-rw-r--r--  2.0 unx        0 b- defN 22-May-17 06:01 spaceone/core/skeleton/model/__init__.py
+-rw-r--r--  2.0 unx        0 b- defN 22-May-17 06:01 spaceone/core/skeleton/service/__init__.py
+-rw-r--r--  2.0 unx      379 b- defN 22-May-17 06:01 spaceone/core/skeleton/service/helloworld_service.py
+-rw-r--r--  2.0 unx        0 b- defN 22-May-17 06:01 spaceone/core/unittest/__init__.py
+-rw-r--r--  2.0 unx     2848 b- defN 22-May-17 06:01 spaceone/core/unittest/result.py
+-rw-r--r--  2.0 unx      579 b- defN 22-May-17 06:01 spaceone/core/unittest/runner.py
+-rw-r--r--  2.0 unx      822 b- defN 22-May-17 06:01 spaceone_core-1.9.7rc1.dist-info/METADATA
+-rw-r--r--  2.0 unx       92 b- defN 22-May-17 06:01 spaceone_core-1.9.7rc1.dist-info/WHEEL
+-rw-r--r--  2.0 unx       56 b- defN 22-May-17 06:01 spaceone_core-1.9.7rc1.dist-info/entry_points.txt
+-rw-r--r--  2.0 unx        9 b- defN 22-May-17 06:01 spaceone_core-1.9.7rc1.dist-info/top_level.txt
+?rw-rw-r--  2.0 unx     8033 b- defN 22-May-17 06:01 spaceone_core-1.9.7rc1.dist-info/RECORD
+88 files, 230198 bytes uncompressed, 61646 bytes compressed:  73.2%
```

## zipnote {}

```diff
@@ -243,23 +243,23 @@
 
 Filename: spaceone/core/unittest/result.py
 Comment: 
 
 Filename: spaceone/core/unittest/runner.py
 Comment: 
 
-Filename: spaceone_core-1.9.7.1.dist-info/METADATA
+Filename: spaceone_core-1.9.7rc1.dist-info/METADATA
 Comment: 
 
-Filename: spaceone_core-1.9.7.1.dist-info/WHEEL
+Filename: spaceone_core-1.9.7rc1.dist-info/WHEEL
 Comment: 
 
-Filename: spaceone_core-1.9.7.1.dist-info/entry_points.txt
+Filename: spaceone_core-1.9.7rc1.dist-info/entry_points.txt
 Comment: 
 
-Filename: spaceone_core-1.9.7.1.dist-info/top_level.txt
+Filename: spaceone_core-1.9.7rc1.dist-info/top_level.txt
 Comment: 
 
-Filename: spaceone_core-1.9.7.1.dist-info/RECORD
+Filename: spaceone_core-1.9.7rc1.dist-info/RECORD
 Comment: 
 
 Zip file comment:
```

## spaceone/core/utils.py

```diff
@@ -137,15 +137,14 @@
         ssl_enabled = False
 
     return {
         'endpoint': f'{endpoint_info["hostname"]}:{endpoint_info["port"]}',
         'ssl_enabled': ssl_enabled
     }
 
-
 def parse_grpc_uri(uri: str) -> dict:
     try:
         endpoint_info = parse_endpoint(uri)
 
         if endpoint_info['scheme'] not in  ['grpc', 'grpc+ssl']:
             raise ValueError(f'Unsupported protocol. (supported_protocol=grpc|grpc+ssl, uri={uri})')
```

## Comparing `spaceone_core-1.9.7.1.dist-info/METADATA` & `spaceone_core-1.9.7rc1.dist-info/METADATA`

 * *Files 21% similar despite different names*

```diff
@@ -1,17 +1,16 @@
 Metadata-Version: 2.1
 Name: spaceone-core
-Version: 1.9.7.1
+Version: 1.9.7rc1
 Summary: SpaceONE core library
 Home-page: https://www.spaceone.dev/
 Author: MEGAZONE SpaceONE Team
 Author-email: admin@spaceone.dev
 License: Apache License 2.0
 Platform: UNKNOWN
-Requires-Dist: protobuf (==3.*)
 Requires-Dist: grpcio-reflection
 Requires-Dist: google-api-core
 Requires-Dist: grpcio-health-checking
 Requires-Dist: asyncio
 Requires-Dist: PyYAML
 Requires-Dist: unittest-xml-reporting (>=3.0.0)
 Requires-Dist: pycryptodome
```

## Comparing `spaceone_core-1.9.7.1.dist-info/RECORD` & `spaceone_core-1.9.7rc1.dist-info/RECORD`

 * *Files 2% similar despite different names*

```diff
@@ -3,15 +3,15 @@
 spaceone/core/base.py,sha256=0XQZyuHrjpzgxQRQf74R2bJIK7GyWgnUOn3Uu_JJuuk,355
 spaceone/core/command.py,sha256=MZK3akaSH_MQdyE36ih5TtODC4ra3Si6_QatZQdtriM,6806
 spaceone/core/error.py,sha256=rW9pNM_SmKzkKxpmQPJeCKiL8iAp1KrmVwhQZCiw1Qk,7039
 spaceone/core/locator.py,sha256=Gq7W5HtK4y7RT9-t7qKTA-NOWhpGI_c15gHtvyQNkdo,2764
 spaceone/core/manager.py,sha256=Z-a3iJq2bhdIEGc3JgP0HklTbQBrkN8ICa4Vibv3DOw,324
 spaceone/core/token.py,sha256=5eY6Ls0vjwsoFBEXtKePyePAsWcmjqy2VUw03Wq4H4A,2520
 spaceone/core/transaction.py,sha256=Vhtm1YXPnHdjUxiU--I2nXt9MgTJ2RpiOxuHwsLZvhs,2979
-spaceone/core/utils.py,sha256=TXZruOPCLrZWZoJCHp9Zt7Uq0KBO1PUJ_ggPGynCUrI,12782
+spaceone/core/utils.py,sha256=IulTfr89Wpdp21HBpSVEoOBLaPlL60fizB0kf-Xj5sk,12781
 spaceone/core/auth/__init__.py,sha256=dJzvlTIwtD0w8tfRqbPxd8KRU5mTdDxykuy-I3IKEl0,215
 spaceone/core/auth/jwt/__init__.py,sha256=pY244pvH4nFButbXAIcyoSa1MPs3fYGXOVsamR0NqMI,779
 spaceone/core/auth/jwt/jwt_util.py,sha256=FHzIrbsDKz5PnygzXRJGAs76tcrDuWK3yzUtI0iNmKo,942
 spaceone/core/cache/__init__.py,sha256=Z7Q5fQQofofapPLs8CKNQDEeSsJL3PCv4p52NwgvK5s,6505
 spaceone/core/cache/local_cache.py,sha256=chLPlx2ZiDltFI8S7DyVCqyHcTAQpkhXxZqbtoIkszA,902
 spaceone/core/cache/redis_cache.py,sha256=twJrBxBdErpsCRloxrRHaKUhXfMid9WOuapDb0WVxts,2192
 spaceone/core/celery/__init__.py,sha256=47DEQpj8HBSa-_TImW-5JCeuQeRkm5NMpJWZG3hSuFU,0
@@ -77,12 +77,12 @@
 spaceone/core/skeleton/manager/helloworld_manager.py,sha256=Qse8oWPS4zgNpEgpAGhV2BoS39M5e5il5YQ6B29XVWE,184
 spaceone/core/skeleton/model/__init__.py,sha256=47DEQpj8HBSa-_TImW-5JCeuQeRkm5NMpJWZG3hSuFU,0
 spaceone/core/skeleton/service/__init__.py,sha256=47DEQpj8HBSa-_TImW-5JCeuQeRkm5NMpJWZG3hSuFU,0
 spaceone/core/skeleton/service/helloworld_service.py,sha256=7sbtZ95dirBq8-gSJ_vcXc5UTetHaP4dI_dRf729D-E,379
 spaceone/core/unittest/__init__.py,sha256=47DEQpj8HBSa-_TImW-5JCeuQeRkm5NMpJWZG3hSuFU,0
 spaceone/core/unittest/result.py,sha256=P3UYQjyW1Dbk2zAU3MW9oI4gFjY-YQuVuZAFfQi_3dc,2848
 spaceone/core/unittest/runner.py,sha256=Tsfy2DysJnIhcjtyp6podMo1Fmuf4n0APt4QCGxz_Qw,579
-spaceone_core-1.9.7.1.dist-info/METADATA,sha256=7gBqiO6QqgxLOKMR8IUPMKns8jmYCUILGZcNvNgAGtI,853
-spaceone_core-1.9.7.1.dist-info/WHEEL,sha256=G16H4A3IeoQmnOrYV4ueZGKSjhipXx8zc8nu9FGlvMA,92
-spaceone_core-1.9.7.1.dist-info/entry_points.txt,sha256=VAyJbSGOciZTThFSTEHOlpXiDHjU28Y5sU2xV_t9AnQ,56
-spaceone_core-1.9.7.1.dist-info/top_level.txt,sha256=ihEDWQFt9VC1K7rt_uBlNUKrx7ixKzPRVA1agrFCIfQ,9
-spaceone_core-1.9.7.1.dist-info/RECORD,,
+spaceone_core-1.9.7rc1.dist-info/METADATA,sha256=pxnOdqJ1n4M430VG4B5rKoWYrv0I0GPfFXr7jCQ8wWM,822
+spaceone_core-1.9.7rc1.dist-info/WHEEL,sha256=G16H4A3IeoQmnOrYV4ueZGKSjhipXx8zc8nu9FGlvMA,92
+spaceone_core-1.9.7rc1.dist-info/entry_points.txt,sha256=VAyJbSGOciZTThFSTEHOlpXiDHjU28Y5sU2xV_t9AnQ,56
+spaceone_core-1.9.7rc1.dist-info/top_level.txt,sha256=ihEDWQFt9VC1K7rt_uBlNUKrx7ixKzPRVA1agrFCIfQ,9
+spaceone_core-1.9.7rc1.dist-info/RECORD,,
```

