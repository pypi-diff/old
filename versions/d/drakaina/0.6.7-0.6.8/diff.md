# Comparing `tmp/drakaina-0.6.7.tar.gz` & `tmp/drakaina-0.6.8.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "drakaina-0.6.7.tar", max compression
+gzip compressed data, was "drakaina-0.6.8.tar", max compression
```

## Comparing `drakaina-0.6.7.tar` & `drakaina-0.6.8.tar`

### file list

```diff
@@ -1,43 +1,43 @@
--rw-r--r--   0        0        0     9542 2023-04-05 08:32:48.122842 drakaina-0.6.7/drakaina/__init__.py
--rw-r--r--   0        0        0     5953 2023-04-04 20:58:00.642760 drakaina-0.6.7/drakaina/_types.py
--rw-r--r--   0        0        0     1494 2023-01-27 12:48:38.216236 drakaina-0.6.7/drakaina/asgi.py
--rw-r--r--   0        0        0     3699 2023-02-13 13:22:12.183448 drakaina-0.6.7/drakaina/client/__init__.py
--rw-r--r--   0        0        0     6158 2022-07-08 05:47:38.000000 drakaina-0.6.7/drakaina/client/base.py
--rw-r--r--   0        0        0     1832 2022-07-08 05:47:38.000000 drakaina-0.6.7/drakaina/client/http.py
--rw-r--r--   0        0        0    11280 2023-01-27 12:55:37.114745 drakaina-0.6.7/drakaina/client/tcp.py
--rw-r--r--   0        0        0     8797 2022-07-08 05:47:38.000000 drakaina-0.6.7/drakaina/client/websocket.py
--rw-r--r--   0        0        0        0 2023-01-24 15:15:01.981448 drakaina-0.6.7/drakaina/contrib/__init__.py
--rw-r--r--   0        0        0     1225 2023-04-04 16:39:30.455695 drakaina-0.6.7/drakaina/contrib/django/__init__.py
--rw-r--r--   0        0        0     1670 2023-04-04 16:03:12.444188 drakaina-0.6.7/drakaina/contrib/django/__rpc_methods.py
--rw-r--r--   0        0        0     6176 2023-04-05 13:26:05.508215 drakaina-0.6.7/drakaina/contrib/django/middleware.py
--rw-r--r--   0        0        0     3182 2023-04-05 13:26:05.517214 drakaina-0.6.7/drakaina/contrib/django/views.py
--rw-r--r--   0        0        0      340 2023-04-05 08:32:48.122842 drakaina-0.6.7/drakaina/contrib/jwt/__init__.py
--rw-r--r--   0        0        0     4831 2023-02-21 13:52:45.250648 drakaina-0.6.7/drakaina/contrib/jwt/auth_procedures.py
--rw-r--r--   0        0        0      348 2023-03-10 11:02:10.213372 drakaina-0.6.7/drakaina/contrib/jwt/errors.py
--rw-r--r--   0        0        0     9194 2023-04-05 08:32:48.124842 drakaina-0.6.7/drakaina/contrib/jwt/middleware.py
--rw-r--r--   0        0        0      913 2023-04-03 15:58:34.495338 drakaina-0.6.7/drakaina/contrib/jwt/types.py
--rw-r--r--   0        0        0    11148 2023-04-05 10:54:01.194233 drakaina-0.6.7/drakaina/contrib/jwt/utils.py
--rw-r--r--   0        0        0     1147 2023-04-05 18:02:08.709862 drakaina-0.6.7/drakaina/exceptions.py
--rw-r--r--   0        0        0      357 2023-04-04 11:19:41.564726 drakaina-0.6.7/drakaina/middleware/__init__.py
--rw-r--r--   0        0        0     1378 2023-03-29 21:57:07.601330 drakaina-0.6.7/drakaina/middleware/base.py
--rw-r--r--   0        0        0     7586 2023-04-05 08:32:48.126844 drakaina-0.6.7/drakaina/middleware/cors.py
--rw-r--r--   0        0        0     2112 2023-04-05 08:32:48.126844 drakaina-0.6.7/drakaina/middleware/exception.py
--rw-r--r--   0        0        0      406 2023-04-04 11:19:41.598921 drakaina-0.6.7/drakaina/middleware/gzip.py
--rw-r--r--   0        0        0      983 2023-04-04 11:19:41.525282 drakaina-0.6.7/drakaina/middleware/logging.py
--rw-r--r--   0        0        0     1138 2023-01-18 00:52:37.644550 drakaina-0.6.7/drakaina/middleware/openapi/__init__.py
--rw-r--r--   0        0        0     1079 2023-04-04 11:19:41.580823 drakaina-0.6.7/drakaina/middleware/request_wrapper.py
--rw-r--r--   0        0        0     3678 2023-04-05 08:32:48.127841 drakaina-0.6.7/drakaina/registries.py
--rw-r--r--   0        0        0      155 2023-03-02 17:41:49.563857 drakaina-0.6.7/drakaina/rpc_protocols/__init__.py
--rw-r--r--   0        0        0     3893 2023-03-03 10:53:57.947758 drakaina-0.6.7/drakaina/rpc_protocols/base.py
--rw-r--r--   0        0        0     8696 2023-04-05 18:02:08.717570 drakaina-0.6.7/drakaina/rpc_protocols/jsonrpc20.py
--rw-r--r--   0        0        0      200 2023-01-09 10:12:10.047554 drakaina-0.6.7/drakaina/rsgi.py
--rw-r--r--   0        0        0     4646 2023-02-27 17:00:44.197509 drakaina-0.6.7/drakaina/serializers.py
--rw-r--r--   0        0        0    11142 2023-01-27 12:51:42.029067 drakaina-0.6.7/drakaina/tcp.py
--rw-r--r--   0        0        0      937 2023-04-05 08:32:48.128841 drakaina-0.6.7/drakaina/utils.py
--rw-r--r--   0        0        0      162 2023-01-25 16:44:10.299855 drakaina-0.6.7/drakaina/ws.py
--rw-r--r--   0        0        0     7896 2023-04-05 08:32:48.129839 drakaina-0.6.7/drakaina/wsgi.py
--rw-r--r--   0        0        0    11372 2023-01-24 23:31:45.206801 drakaina-0.6.7/LICENSE
--rw-r--r--   0        0        0     2461 2023-04-05 18:02:48.122643 drakaina-0.6.7/pyproject.toml
--rw-r--r--   0        0        0     5017 2023-04-05 08:32:48.121846 drakaina-0.6.7/README.md
--rw-r--r--   0        0        0     6109 1970-01-01 00:00:00.000000 drakaina-0.6.7/setup.py
--rw-r--r--   0        0        0     6371 1970-01-01 00:00:00.000000 drakaina-0.6.7/PKG-INFO
+-rw-r--r--   0        0        0     9542 2023-04-05 08:32:48.122842 drakaina-0.6.8/drakaina/__init__.py
+-rw-r--r--   0        0        0     5953 2023-04-04 20:58:00.642760 drakaina-0.6.8/drakaina/_types.py
+-rw-r--r--   0        0        0     1494 2023-01-27 12:48:38.216236 drakaina-0.6.8/drakaina/asgi.py
+-rw-r--r--   0        0        0     3699 2023-02-13 13:22:12.183448 drakaina-0.6.8/drakaina/client/__init__.py
+-rw-r--r--   0        0        0     6158 2022-07-08 05:47:38.000000 drakaina-0.6.8/drakaina/client/base.py
+-rw-r--r--   0        0        0     1832 2022-07-08 05:47:38.000000 drakaina-0.6.8/drakaina/client/http.py
+-rw-r--r--   0        0        0    11280 2023-01-27 12:55:37.114745 drakaina-0.6.8/drakaina/client/tcp.py
+-rw-r--r--   0        0        0     8797 2022-07-08 05:47:38.000000 drakaina-0.6.8/drakaina/client/websocket.py
+-rw-r--r--   0        0        0        0 2023-01-24 15:15:01.981448 drakaina-0.6.8/drakaina/contrib/__init__.py
+-rw-r--r--   0        0        0     1225 2023-04-04 16:39:30.455695 drakaina-0.6.8/drakaina/contrib/django/__init__.py
+-rw-r--r--   0        0        0     1670 2023-04-04 16:03:12.444188 drakaina-0.6.8/drakaina/contrib/django/__rpc_methods.py
+-rw-r--r--   0        0        0     6176 2023-04-05 13:26:05.508215 drakaina-0.6.8/drakaina/contrib/django/middleware.py
+-rw-r--r--   0        0        0     3182 2023-04-05 13:26:05.517214 drakaina-0.6.8/drakaina/contrib/django/views.py
+-rw-r--r--   0        0        0      340 2023-04-05 08:32:48.122842 drakaina-0.6.8/drakaina/contrib/jwt/__init__.py
+-rw-r--r--   0        0        0     4831 2023-02-21 13:52:45.250648 drakaina-0.6.8/drakaina/contrib/jwt/auth_procedures.py
+-rw-r--r--   0        0        0      348 2023-03-10 11:02:10.213372 drakaina-0.6.8/drakaina/contrib/jwt/errors.py
+-rw-r--r--   0        0        0     9194 2023-04-05 08:32:48.124842 drakaina-0.6.8/drakaina/contrib/jwt/middleware.py
+-rw-r--r--   0        0        0      913 2023-04-03 15:58:34.495338 drakaina-0.6.8/drakaina/contrib/jwt/types.py
+-rw-r--r--   0        0        0    11148 2023-04-05 10:54:01.194233 drakaina-0.6.8/drakaina/contrib/jwt/utils.py
+-rw-r--r--   0        0        0     1147 2023-04-05 18:02:08.709862 drakaina-0.6.8/drakaina/exceptions.py
+-rw-r--r--   0        0        0      357 2023-04-04 11:19:41.564726 drakaina-0.6.8/drakaina/middleware/__init__.py
+-rw-r--r--   0        0        0     1378 2023-03-29 21:57:07.601330 drakaina-0.6.8/drakaina/middleware/base.py
+-rw-r--r--   0        0        0     7586 2023-04-05 08:32:48.126844 drakaina-0.6.8/drakaina/middleware/cors.py
+-rw-r--r--   0        0        0     2112 2023-04-05 08:32:48.126844 drakaina-0.6.8/drakaina/middleware/exception.py
+-rw-r--r--   0        0        0      406 2023-04-04 11:19:41.598921 drakaina-0.6.8/drakaina/middleware/gzip.py
+-rw-r--r--   0        0        0      983 2023-04-04 11:19:41.525282 drakaina-0.6.8/drakaina/middleware/logging.py
+-rw-r--r--   0        0        0     1138 2023-01-18 00:52:37.644550 drakaina-0.6.8/drakaina/middleware/openapi/__init__.py
+-rw-r--r--   0        0        0     1079 2023-04-04 11:19:41.580823 drakaina-0.6.8/drakaina/middleware/request_wrapper.py
+-rw-r--r--   0        0        0     3678 2023-04-05 08:32:48.127841 drakaina-0.6.8/drakaina/registries.py
+-rw-r--r--   0        0        0      155 2023-03-02 17:41:49.563857 drakaina-0.6.8/drakaina/rpc_protocols/__init__.py
+-rw-r--r--   0        0        0     4128 2023-04-06 11:06:25.511203 drakaina-0.6.8/drakaina/rpc_protocols/base.py
+-rw-r--r--   0        0        0     8777 2023-04-06 10:57:47.842893 drakaina-0.6.8/drakaina/rpc_protocols/jsonrpc20.py
+-rw-r--r--   0        0        0      200 2023-01-09 10:12:10.047554 drakaina-0.6.8/drakaina/rsgi.py
+-rw-r--r--   0        0        0     4646 2023-02-27 17:00:44.197509 drakaina-0.6.8/drakaina/serializers.py
+-rw-r--r--   0        0        0    11142 2023-01-27 12:51:42.029067 drakaina-0.6.8/drakaina/tcp.py
+-rw-r--r--   0        0        0      937 2023-04-05 08:32:48.128841 drakaina-0.6.8/drakaina/utils.py
+-rw-r--r--   0        0        0      162 2023-01-25 16:44:10.299855 drakaina-0.6.8/drakaina/ws.py
+-rw-r--r--   0        0        0     7896 2023-04-05 08:32:48.129839 drakaina-0.6.8/drakaina/wsgi.py
+-rw-r--r--   0        0        0    11372 2023-01-24 23:31:45.206801 drakaina-0.6.8/LICENSE
+-rw-r--r--   0        0        0     2461 2023-04-06 11:11:40.331682 drakaina-0.6.8/pyproject.toml
+-rw-r--r--   0        0        0     5017 2023-04-05 08:32:48.121846 drakaina-0.6.8/README.md
+-rw-r--r--   0        0        0     6109 1970-01-01 00:00:00.000000 drakaina-0.6.8/setup.py
+-rw-r--r--   0        0        0     6371 1970-01-01 00:00:00.000000 drakaina-0.6.8/PKG-INFO
```

### Comparing `drakaina-0.6.7/drakaina/__init__.py` & `drakaina-0.6.8/drakaina/__init__.py`

 * *Files identical despite different names*

### Comparing `drakaina-0.6.7/drakaina/_types.py` & `drakaina-0.6.8/drakaina/_types.py`

 * *Files identical despite different names*

### Comparing `drakaina-0.6.7/drakaina/asgi.py` & `drakaina-0.6.8/drakaina/asgi.py`

 * *Files identical despite different names*

### Comparing `drakaina-0.6.7/drakaina/client/__init__.py` & `drakaina-0.6.8/drakaina/client/__init__.py`

 * *Files identical despite different names*

### Comparing `drakaina-0.6.7/drakaina/client/base.py` & `drakaina-0.6.8/drakaina/client/base.py`

 * *Files identical despite different names*

### Comparing `drakaina-0.6.7/drakaina/client/http.py` & `drakaina-0.6.8/drakaina/client/http.py`

 * *Files identical despite different names*

### Comparing `drakaina-0.6.7/drakaina/client/tcp.py` & `drakaina-0.6.8/drakaina/client/tcp.py`

 * *Files identical despite different names*

### Comparing `drakaina-0.6.7/drakaina/client/websocket.py` & `drakaina-0.6.8/drakaina/client/websocket.py`

 * *Files identical despite different names*

### Comparing `drakaina-0.6.7/drakaina/contrib/django/__init__.py` & `drakaina-0.6.8/drakaina/contrib/django/__init__.py`

 * *Files identical despite different names*

### Comparing `drakaina-0.6.7/drakaina/contrib/django/__rpc_methods.py` & `drakaina-0.6.8/drakaina/contrib/django/__rpc_methods.py`

 * *Files identical despite different names*

### Comparing `drakaina-0.6.7/drakaina/contrib/django/middleware.py` & `drakaina-0.6.8/drakaina/contrib/django/middleware.py`

 * *Files identical despite different names*

### Comparing `drakaina-0.6.7/drakaina/contrib/django/views.py` & `drakaina-0.6.8/drakaina/contrib/django/views.py`

 * *Files identical despite different names*

### Comparing `drakaina-0.6.7/drakaina/contrib/jwt/auth_procedures.py` & `drakaina-0.6.8/drakaina/contrib/jwt/auth_procedures.py`

 * *Files identical despite different names*

### Comparing `drakaina-0.6.7/drakaina/contrib/jwt/middleware.py` & `drakaina-0.6.8/drakaina/contrib/jwt/middleware.py`

 * *Files identical despite different names*

### Comparing `drakaina-0.6.7/drakaina/contrib/jwt/types.py` & `drakaina-0.6.8/drakaina/contrib/jwt/types.py`

 * *Files identical despite different names*

### Comparing `drakaina-0.6.7/drakaina/contrib/jwt/utils.py` & `drakaina-0.6.8/drakaina/contrib/jwt/utils.py`

 * *Files identical despite different names*

### Comparing `drakaina-0.6.7/drakaina/exceptions.py` & `drakaina-0.6.8/drakaina/exceptions.py`

 * *Files identical despite different names*

### Comparing `drakaina-0.6.7/drakaina/middleware/base.py` & `drakaina-0.6.8/drakaina/middleware/base.py`

 * *Files identical despite different names*

### Comparing `drakaina-0.6.7/drakaina/middleware/cors.py` & `drakaina-0.6.8/drakaina/middleware/cors.py`

 * *Files identical despite different names*

### Comparing `drakaina-0.6.7/drakaina/middleware/exception.py` & `drakaina-0.6.8/drakaina/middleware/exception.py`

 * *Files identical despite different names*

### Comparing `drakaina-0.6.7/drakaina/middleware/logging.py` & `drakaina-0.6.8/drakaina/middleware/logging.py`

 * *Files identical despite different names*

### Comparing `drakaina-0.6.7/drakaina/middleware/openapi/__init__.py` & `drakaina-0.6.8/drakaina/middleware/openapi/__init__.py`

 * *Files identical despite different names*

### Comparing `drakaina-0.6.7/drakaina/middleware/request_wrapper.py` & `drakaina-0.6.8/drakaina/middleware/request_wrapper.py`

 * *Files identical despite different names*

### Comparing `drakaina-0.6.7/drakaina/registries.py` & `drakaina-0.6.8/drakaina/registries.py`

 * *Files identical despite different names*

### Comparing `drakaina-0.6.7/drakaina/rpc_protocols/base.py` & `drakaina-0.6.8/drakaina/rpc_protocols/base.py`

 * *Files 2% similar despite different names*

```diff
@@ -83,16 +83,22 @@
             Raw error data.
 
         """
 
         if isinstance(error, type) and issubclass(error, Exception):
             error = error()
 
-        rpc_error_class = self._errors_map.get(type(error), self.default_error)
-        rpc_error = rpc_error_class(str(error))
+        if isinstance(error, self.base_error_class):
+            rpc_error = error
+        else:
+            rpc_error_class = self._errors_map.get(
+                type(error),
+                self.default_error_class,
+            )
+            rpc_error = rpc_error_class(str(error))
 
         return self.serializer.serialize(rpc_error.as_dict())
 
     def handle(self, rpc_request: Any, request: Optional[Any] = None) -> Any:
         """Handles a procedure call.
 
         :param rpc_request:
@@ -105,15 +111,19 @@
 
         """
         raise NotImplementedError(
             "You must implement the `handle` method in the child class",
         )
 
     @property
-    def default_error(self):
+    def base_error_class(self):
+        return RPCError
+
+    @property
+    def default_error_class(self):
         return InternalServerError
 
     @property
     def content_type(self) -> str:
         return self.serializer.content_type
 
     def smd_scheme(self) -> bytes:
```

### Comparing `drakaina-0.6.7/drakaina/rpc_protocols/jsonrpc20.py` & `drakaina-0.6.8/drakaina/rpc_protocols/jsonrpc20.py`

 * *Files 1% similar despite different names*

```diff
@@ -295,12 +295,16 @@
 
         if request_id is None:
             return None
 
         return dict(jsonrpc="2.0", result=result, id=request_id)
 
     @property
-    def default_error(self):
+    def base_error_class(self):
+        return JsonRPCError
+
+    @property
+    def default_error_class(self):
         return InternalError
 
     def smd_scheme(self):
         return {}
```

### Comparing `drakaina-0.6.7/drakaina/serializers.py` & `drakaina-0.6.8/drakaina/serializers.py`

 * *Files identical despite different names*

### Comparing `drakaina-0.6.7/drakaina/tcp.py` & `drakaina-0.6.8/drakaina/tcp.py`

 * *Files identical despite different names*

### Comparing `drakaina-0.6.7/drakaina/utils.py` & `drakaina-0.6.8/drakaina/utils.py`

 * *Files identical despite different names*

### Comparing `drakaina-0.6.7/drakaina/wsgi.py` & `drakaina-0.6.8/drakaina/wsgi.py`

 * *Files identical despite different names*

### Comparing `drakaina-0.6.7/LICENSE` & `drakaina-0.6.8/LICENSE`

 * *Files identical despite different names*

### Comparing `drakaina-0.6.7/pyproject.toml` & `drakaina-0.6.8/pyproject.toml`

 * *Files 2% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 [tool.poetry]
 name = "drakaina"
-version = "0.6.7"
+version = "0.6.8"
 description = "Module for simple RPC service implementation"
 authors = ["Aleksey Terentyev <terentyev.a@pm.me>"]
 license = "Apache License 2.0"
 readme = "README.md"
 classifiers = [
     "Development Status :: 4 - Beta",
     "Environment :: Web Environment",
```

### Comparing `drakaina-0.6.7/README.md` & `drakaina-0.6.8/README.md`

 * *Files identical despite different names*

### Comparing `drakaina-0.6.7/setup.py` & `drakaina-0.6.8/setup.py`

 * *Files 1% similar despite different names*

```diff
@@ -22,15 +22,15 @@
  'msgpack': ['msgpack>=1.0.4,<2.0.0'],
  'orjson': ['orjson>=3.8.5,<4.0.0'],
  'tests': ['pyjwt>=2.6.0,<3.0.0'],
  'ujson': ['ujson>=5.7.0,<6.0.0']}
 
 setup_kwargs = {
     'name': 'drakaina',
-    'version': '0.6.7',
+    'version': '0.6.8',
     'description': 'Module for simple RPC service implementation',
     'long_description': '# drakaina\n\n![Drakaina](content/drakaina.png "Drakaina"){width=200px height=205px}\n\n[![image](https://img.shields.io/pypi/v/drakaina.svg)](https://pypi.python.org/pypi/drakaina)\n[![image](https://img.shields.io/pypi/l/drakaina.svg)](https://pypi.python.org/pypi/drakaina)\n[![image](https://img.shields.io/pypi/pyversions/drakaina.svg)](https://pypi.python.org/pypi/drakaina)\n[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/charliermarsh/ruff/main/assets/badge/v1.json)](https://github.com/charliermarsh/ruff)\n[![Code style: black](https://img.shields.io/badge/code%20style-black-black.svg)](https://github.com/psf/black)\n[![libera manifesto](https://img.shields.io/badge/libera-manifesto-lightgrey.svg)](https://liberamanifesto.com)\n\n❗ WIP\n\nModule for simple RPC service implementation\n\n\n## Quickstart\n\nDrakaina may be installed via `pip` and requires Python 3.7 or higher :\n\n```shell\npip install drakaina\n```\n\nA minimal Drakaina example is:\n\n```python\nfrom drakaina import remote_procedure\nfrom drakaina.wsgi import WSGIHandler\n\n\n@remote_procedure\ndef my_method():\n    return "Hello Bro! ✋️"\n\n\n@remote_procedure(name="something.get")\ndef get_some_string():\n    return "You called `something.get`."\n\n\n@remote_procedure(provide_request=True)\ndef do_something_with_environ(request):\n    return f"You called `do_something_with_environ`. Request: {request}."\n\n\n@remote_procedure()\ndef tell_the_middleware_something():\n    return "You called `tell_the_middleware_something`. It has a some extra conditions."\n\n\nasync def asynchronous_procedure():\n    await asyncio.sleep(5)\n    return "Ding-Dong 🔔!"\n\n\n"""\n>>> JsonRPCv2().handle({"jsonrpc": "2.0", "method": "my_method", "id": 1})\nor define WSGI application\n"""\napp = WSGIHandler(route="/jrpc")\n```\n\nDrakaina may be ran with any WSGI-compliant server,\nsuch as [Gunicorn](http://gunicorn.org).\n\n```shell\ngunicorn main:app\n```\n\n\n## Features\n\n- WSGI protocol implementation\n  - Implemented CORS middleware\n  - Compatible with simple middlewares for others wsgi-frameworks,\n    like as [Werkzeug](https://palletsprojects.com/p/werkzeug/),\n    [Flask](https://palletsprojects.com/p/flask/)\n\n\n# Documentation\n\n\n## Installation\n\n```shell\npip install drakaina\n```\n\n\n## Middlewares\n\n\n### CORS\n\n\n### JWT\n\nDrakaina may be installed via `pip` and requires Python 3.7 or higher :\n\n```shell\npip install drakaina[jwt]\n```\n\nA minimal Drakaina example is:\n\n```python\nfrom functools import partial\nfrom drakaina import ENV_IS_AUTHENTICATED\nfrom drakaina import ENV_USER_ID\nfrom drakaina import remote_procedure\nfrom drakaina import check_permissions\nfrom drakaina import login_required\nfrom drakaina import match_any\nfrom drakaina.contrib.jwt.middleware import JWTAuthenticationMiddleware\nfrom drakaina.wsgi import WSGIHandler\n\n\n@login_required\n@remote_procedure(provide_request=True)\ndef my_method(request):\n    assert request[ENV_IS_AUTHENTICATED]\n    return f"Hello Bro ✋! Your ID={request[ENV_USER_ID]}"\n\n\n@check_permissions(\n    scopes=["user_read", "app/user:admin", "username:johndoe"],\n    comparator=match_any,\n)\n@remote_procedure\ndef my_method():\n    return "Hello Bro! ✋️"\n\n\n\n\napp = WSGIHandler(\n    middlewares=[\n        partial(\n            JWTAuthenticationMiddleware,\n            secret_phrase="_secret_",\n            credentials_required=True,\n        )\n    ]\n)\n```\n\n\n### Using with Django\n\nCreate file `rpc_views.py` in your django application.\nDefine function and wrap it `remote_procedure` decorator:\n\n```python\nfrom drakaina import remote_procedure\n\n@remote_procedure\ndef my_method():\n    return "Hello, Django Bro! ✋"\n```\n\nAdd `RPCView` class to urlpatterns. The `as_view` method\nmust accept the `autodiscover` argument as the name of\nthe remote procedure files.\n\n```python\nfrom django.urls import path\nfrom drakaina.contrib.django.views import RPCView\n\nurlpatterns = [\n    ...,\n    path("api/", RPCView.as_view(autodiscover="rpc_views")),\n]\n```\n\n\n### JWT Authentication in your Django project\n\nWrap an instance of `RPCView` with the `JWTAuthenticationMiddleware`.\n\n```python\nfrom django.urls import path\nfrom drakaina.contrib.django import RPCView, JWTAuthenticationMiddleware\n\nurlpatterns = [\n    ...,\n    path("api/", JWTAuthenticationMiddleware(\n        RPCView.as_view(autodiscover="rpc_views")\n    )),\n]\n```\n\nDefine the parameters in the `settings.py` file.\n\n```python\n...\n\nDRAKAINA_JWT_SECRET_KEY = SECRET_KEY\n\n...\n```\n\n\n## License\n\nApache License 2.0\n\n## Artwork\n\n"[drakaina.png](content/drakaina.png)" by Korolko Anastasia is licensed under\n<a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/"><img alt="License Creative Commons" style="border-width:0" src="https://i.creativecommons.org/l/by-sa/4.0/80x15.png" /></a> ([CC BY-SA 4.0](http://creativecommons.org/licenses/by-sa/4.0/)).\n',
     'author': 'Aleksey Terentyev',
     'author_email': 'terentyev.a@pm.me',
     'maintainer': 'None',
     'maintainer_email': 'None',
     'url': 'https://gitlab.com/tau_lex/drakaina',
```

### Comparing `drakaina-0.6.7/PKG-INFO` & `drakaina-0.6.8/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: drakaina
-Version: 0.6.7
+Version: 0.6.8
 Summary: Module for simple RPC service implementation
 Home-page: https://gitlab.com/tau_lex/drakaina
 License: Apache-2.0
 Keywords: rpc,jsonrpc
 Author: Aleksey Terentyev
 Author-email: terentyev.a@pm.me
 Requires-Python: >=3.7,<4.0
```

