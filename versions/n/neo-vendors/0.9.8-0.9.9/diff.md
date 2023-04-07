# Comparing `tmp/neo_vendors-0.9.8.tar.gz` & `tmp/neo_vendors-0.9.9.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "neo_vendors-0.9.8.tar", max compression
+gzip compressed data, was "neo_vendors-0.9.9.tar", max compression
```

## Comparing `neo_vendors-0.9.8.tar` & `neo_vendors-0.9.9.tar`

### file list

```diff
@@ -1,21 +1,21 @@
--rw-r--r--   0        0        0        0 2023-03-01 08:28:27.592486 neo_vendors-0.9.8/README.md
--rw-r--r--   0        0        0        0 2023-03-02 06:55:12.976282 neo_vendors-0.9.8/neo_vendors/__init__.py
--rw-r--r--   0        0        0      987 2023-03-01 09:02:10.008650 neo_vendors-0.9.8/neo_vendors/date_time.py
--rw-r--r--   0        0        0        0 2023-03-02 12:12:10.796939 neo_vendors-0.9.8/neo_vendors/fastapi_tools/__init__.py
--rw-r--r--   0        0        0        0 2023-03-02 12:41:48.687529 neo_vendors-0.9.8/neo_vendors/fastapi_tools/errors/__init__.py
--rw-r--r--   0        0        0      208 2023-03-02 12:43:16.769389 neo_vendors-0.9.8/neo_vendors/fastapi_tools/errors/base.py
--rw-r--r--   0        0        0      527 2023-03-02 12:45:29.987597 neo_vendors-0.9.8/neo_vendors/fastapi_tools/errors/exceptions.py
--rw-r--r--   0        0        0     1466 2023-03-02 12:53:53.383667 neo_vendors-0.9.8/neo_vendors/fastapi_tools/errors/handlers.py
--rw-r--r--   0        0        0      142 2023-03-02 12:46:34.075800 neo_vendors-0.9.8/neo_vendors/fastapi_tools/errors/payloads.py
--rw-r--r--   0        0        0        0 2023-03-02 12:23:40.559204 neo_vendors-0.9.8/neo_vendors/fastapi_tools/middlewares/__init__.py
--rw-r--r--   0        0        0     2515 2023-03-02 12:25:10.480551 neo_vendors-0.9.8/neo_vendors/fastapi_tools/middlewares/request_handler_middleware.py
--rw-r--r--   0        0        0     2915 2023-03-02 12:53:53.381379 neo_vendors-0.9.8/neo_vendors/fastapi_tools/request_context.py
--rw-r--r--   0        0        0        0 2023-01-31 10:56:51.612860 neo_vendors-0.9.8/neo_vendors/http/__init__.py
--rw-r--r--   0        0        0    10291 2023-03-05 19:29:41.939148 neo_vendors-0.9.8/neo_vendors/http/async_transport.py
--rw-r--r--   0        0        0      368 2023-03-05 20:15:49.828712 neo_vendors-0.9.8/neo_vendors/http/http_methods.py
--rw-r--r--   0        0        0     1089 2023-03-05 19:29:41.939712 neo_vendors-0.9.8/neo_vendors/http/request_context.py
--rw-r--r--   0        0        0     5625 2023-03-02 09:45:38.525873 neo_vendors-0.9.8/neo_vendors/loggers.py
--rw-r--r--   0        0        0       23 2022-03-27 08:54:54.000000 neo_vendors-0.9.8/neo_vendors/telegram_log/__init__.py
--rw-r--r--   0        0        0     2827 2023-03-01 10:50:46.616212 neo_vendors-0.9.8/neo_vendors/telegram_log/handler.py
--rw-r--r--   0        0        0      619 2023-03-05 20:16:16.093431 neo_vendors-0.9.8/pyproject.toml
--rw-r--r--   0        0        0      774 1970-01-01 00:00:00.000000 neo_vendors-0.9.8/PKG-INFO
+-rw-r--r--   0        0        0        0 2023-03-01 08:28:27.592486 neo_vendors-0.9.9/README.md
+-rw-r--r--   0        0        0        0 2023-03-02 06:55:12.976282 neo_vendors-0.9.9/neo_vendors/__init__.py
+-rw-r--r--   0        0        0      987 2023-03-01 09:02:10.008650 neo_vendors-0.9.9/neo_vendors/date_time.py
+-rw-r--r--   0        0        0        0 2023-03-02 12:12:10.796939 neo_vendors-0.9.9/neo_vendors/fastapi_tools/__init__.py
+-rw-r--r--   0        0        0        0 2023-03-02 12:41:48.687529 neo_vendors-0.9.9/neo_vendors/fastapi_tools/errors/__init__.py
+-rw-r--r--   0        0        0      208 2023-03-02 12:43:16.769389 neo_vendors-0.9.9/neo_vendors/fastapi_tools/errors/base.py
+-rw-r--r--   0        0        0      527 2023-03-02 12:45:29.987597 neo_vendors-0.9.9/neo_vendors/fastapi_tools/errors/exceptions.py
+-rw-r--r--   0        0        0     1466 2023-03-02 12:53:53.383667 neo_vendors-0.9.9/neo_vendors/fastapi_tools/errors/handlers.py
+-rw-r--r--   0        0        0      142 2023-03-02 12:46:34.075800 neo_vendors-0.9.9/neo_vendors/fastapi_tools/errors/payloads.py
+-rw-r--r--   0        0        0        0 2023-03-02 12:23:40.559204 neo_vendors-0.9.9/neo_vendors/fastapi_tools/middlewares/__init__.py
+-rw-r--r--   0        0        0     2515 2023-03-02 12:25:10.480551 neo_vendors-0.9.9/neo_vendors/fastapi_tools/middlewares/request_handler_middleware.py
+-rw-r--r--   0        0        0     2915 2023-03-02 12:53:53.381379 neo_vendors-0.9.9/neo_vendors/fastapi_tools/request_context.py
+-rw-r--r--   0        0        0        0 2023-01-31 10:56:51.612860 neo_vendors-0.9.9/neo_vendors/http/__init__.py
+-rw-r--r--   0        0        0    10894 2023-03-05 20:29:09.730120 neo_vendors-0.9.9/neo_vendors/http/async_transport.py
+-rw-r--r--   0        0        0      368 2023-03-05 20:15:49.828712 neo_vendors-0.9.9/neo_vendors/http/http_methods.py
+-rw-r--r--   0        0        0     1089 2023-03-05 19:29:41.939712 neo_vendors-0.9.9/neo_vendors/http/request_context.py
+-rw-r--r--   0        0        0     5625 2023-03-02 09:45:38.525873 neo_vendors-0.9.9/neo_vendors/loggers.py
+-rw-r--r--   0        0        0       23 2022-03-27 08:54:54.000000 neo_vendors-0.9.9/neo_vendors/telegram_log/__init__.py
+-rw-r--r--   0        0        0     2827 2023-03-01 10:50:46.616212 neo_vendors-0.9.9/neo_vendors/telegram_log/handler.py
+-rw-r--r--   0        0        0      619 2023-03-05 20:29:09.722672 neo_vendors-0.9.9/pyproject.toml
+-rw-r--r--   0        0        0      774 1970-01-01 00:00:00.000000 neo_vendors-0.9.9/PKG-INFO
```

### Comparing `neo_vendors-0.9.8/neo_vendors/date_time.py` & `neo_vendors-0.9.9/neo_vendors/date_time.py`

 * *Files identical despite different names*

### Comparing `neo_vendors-0.9.8/neo_vendors/fastapi_tools/errors/exceptions.py` & `neo_vendors-0.9.9/neo_vendors/fastapi_tools/errors/exceptions.py`

 * *Files identical despite different names*

### Comparing `neo_vendors-0.9.8/neo_vendors/fastapi_tools/errors/handlers.py` & `neo_vendors-0.9.9/neo_vendors/fastapi_tools/errors/handlers.py`

 * *Files identical despite different names*

### Comparing `neo_vendors-0.9.8/neo_vendors/fastapi_tools/middlewares/request_handler_middleware.py` & `neo_vendors-0.9.9/neo_vendors/fastapi_tools/middlewares/request_handler_middleware.py`

 * *Files identical despite different names*

### Comparing `neo_vendors-0.9.8/neo_vendors/fastapi_tools/request_context.py` & `neo_vendors-0.9.9/neo_vendors/fastapi_tools/request_context.py`

 * *Files identical despite different names*

### Comparing `neo_vendors-0.9.8/neo_vendors/http/async_transport.py` & `neo_vendors-0.9.9/neo_vendors/http/async_transport.py`

 * *Files 6% similar despite different names*

```diff
@@ -176,14 +176,32 @@
             method=http_methods.HttpMethodsEnum.GET,
             query_params=query_params,
             request_body=None,
             max_tries=max_tries,
             relax_time=relax_time,
         )
 
+    async def make_post(
+            self,
+            *,
+            path: str,
+            query_params: typing.Optional[typing.Dict[str, str]] = None,
+            request_body: typing.Optional[typing.Dict] = None,
+            max_tries: int = 1,
+            relax_time: typing.Optional[datetime.timedelta] = None,
+    ) -> bytes:
+        return await self.make_http(
+            path=path,
+            method=http_methods.HttpMethodsEnum.GET,
+            query_params=query_params,
+            request_body=request_body,
+            max_tries=max_tries,
+            relax_time=relax_time,
+        )
+
 
 class RequestContextWrapper(types.SimpleNamespace):
     context: request_context.RequestOutgoing
 
     def __init__(self, trace_request_ctx: typing.Optional[types.SimpleNamespace] = None):
         self.context = request_context.RequestOutgoing()
         super(RequestContextWrapper, self).__init__()
```

### Comparing `neo_vendors-0.9.8/neo_vendors/http/request_context.py` & `neo_vendors-0.9.9/neo_vendors/http/request_context.py`

 * *Files identical despite different names*

### Comparing `neo_vendors-0.9.8/neo_vendors/loggers.py` & `neo_vendors-0.9.9/neo_vendors/loggers.py`

 * *Files identical despite different names*

### Comparing `neo_vendors-0.9.8/neo_vendors/telegram_log/handler.py` & `neo_vendors-0.9.9/neo_vendors/telegram_log/handler.py`

 * *Files identical despite different names*

### Comparing `neo_vendors-0.9.8/pyproject.toml` & `neo_vendors-0.9.9/pyproject.toml`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 [tool.poetry]
 name = "neo-vendors"
-version = "0.9.8"
+version = "0.9.9"
 description = ""
 authors = ["ruslangilfanov <rgilfanov@fix.ru>"]
 readme = "README.md"
 packages = [{include = "neo_vendors"}]
 
 [tool.poetry.dependencies]
 python = "^3.10"
```

### Comparing `neo_vendors-0.9.8/PKG-INFO` & `neo_vendors-0.9.9/PKG-INFO`

 * *Files 10% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: neo-vendors
-Version: 0.9.8
+Version: 0.9.9
 Summary: 
 Author: ruslangilfanov
 Author-email: rgilfanov@fix.ru
 Requires-Python: >=3.10,<4.0
 Classifier: Programming Language :: Python :: 3
 Classifier: Programming Language :: Python :: 3.10
 Classifier: Programming Language :: Python :: 3.11
```

