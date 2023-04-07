# Comparing `tmp/openapify-0.1.1.tar.gz` & `tmp/openapify-0.1.2.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "openapify-0.1.1.tar", last modified: Fri Apr  7 10:28:17 2023, max compression
+gzip compressed data, was "openapify-0.1.2.tar", last modified: Fri Apr  7 11:50:27 2023, max compression
```

## Comparing `openapify-0.1.1.tar` & `openapify-0.1.2.tar`

### file list

```diff
@@ -1,31 +1,31 @@
-drwxr-xr-x   0 alexander.tikhonov   (503) staff       (20)        0 2023-04-07 10:28:17.376541 openapify-0.1.1/
--rw-r--r--   0 alexander.tikhonov   (503) staff       (20)      732 2023-04-07 10:28:17.376418 openapify-0.1.1/PKG-INFO
-drwxr-xr-x   0 alexander.tikhonov   (503) staff       (20)        0 2023-04-07 10:28:17.373241 openapify-0.1.1/openapify/
--rw-r--r--   0 alexander.tikhonov   (503) staff       (20)      198 2023-04-03 17:00:50.000000 openapify-0.1.1/openapify/__init__.py
-drwxr-xr-x   0 alexander.tikhonov   (503) staff       (20)        0 2023-04-07 10:28:17.375168 openapify-0.1.1/openapify/core/
--rw-r--r--   0 alexander.tikhonov   (503) staff       (20)        0 2023-04-03 13:14:57.000000 openapify-0.1.1/openapify/core/__init__.py
--rw-r--r--   0 alexander.tikhonov   (503) staff       (20)     1115 2023-04-03 16:43:44.000000 openapify-0.1.1/openapify/core/apispec.py
--rw-r--r--   0 alexander.tikhonov   (503) staff       (20)    15113 2023-04-06 11:04:29.000000 openapify-0.1.1/openapify/core/builder.py
--rw-r--r--   0 alexander.tikhonov   (503) staff       (20)       92 2023-03-20 20:50:13.000000 openapify-0.1.1/openapify/core/const.py
--rw-r--r--   0 alexander.tikhonov   (503) staff       (20)      591 2023-04-03 13:10:22.000000 openapify-0.1.1/openapify/core/jsonschema.py
--rw-r--r--   0 alexander.tikhonov   (503) staff       (20)     1730 2023-04-03 17:22:07.000000 openapify-0.1.1/openapify/core/models.py
-drwxr-xr-x   0 alexander.tikhonov   (503) staff       (20)        0 2023-04-07 10:28:17.375620 openapify-0.1.1/openapify/core/openapi/
--rw-r--r--   0 alexander.tikhonov   (503) staff       (20)        0 2023-03-20 12:12:59.000000 openapify-0.1.1/openapify/core/openapi/__init__.py
--rw-r--r--   0 alexander.tikhonov   (503) staff       (20)     5218 2023-04-04 09:34:10.000000 openapify-0.1.1/openapify/core/openapi/models.py
--rw-r--r--   0 alexander.tikhonov   (503) staff       (20)     4724 2023-04-06 11:04:29.000000 openapify-0.1.1/openapify/decorators.py
-drwxr-xr-x   0 alexander.tikhonov   (503) staff       (20)        0 2023-04-07 10:28:17.375921 openapify-0.1.1/openapify/ext/
--rw-r--r--   0 alexander.tikhonov   (503) staff       (20)        0 2023-03-17 15:48:32.000000 openapify-0.1.1/openapify/ext/__init__.py
-drwxr-xr-x   0 alexander.tikhonov   (503) staff       (20)        0 2023-04-07 10:28:17.376111 openapify-0.1.1/openapify/ext/web/
--rw-r--r--   0 alexander.tikhonov   (503) staff       (20)        0 2023-03-18 09:45:46.000000 openapify-0.1.1/openapify/ext/web/__init__.py
--rw-r--r--   0 alexander.tikhonov   (503) staff       (20)     4332 2023-04-03 13:47:08.000000 openapify-0.1.1/openapify/ext/web/aiohttp.py
--rw-r--r--   0 alexander.tikhonov   (503) staff       (20)        0 2023-03-17 11:19:37.000000 openapify-0.1.1/openapify/py.typed
-drwxr-xr-x   0 alexander.tikhonov   (503) staff       (20)        0 2023-04-07 10:28:17.373928 openapify-0.1.1/openapify.egg-info/
--rw-r--r--   0 alexander.tikhonov   (503) staff       (20)      732 2023-04-07 10:28:17.000000 openapify-0.1.1/openapify.egg-info/PKG-INFO
--rw-r--r--   0 alexander.tikhonov   (503) staff       (20)      594 2023-04-07 10:28:17.000000 openapify-0.1.1/openapify.egg-info/SOURCES.txt
--rw-r--r--   0 alexander.tikhonov   (503) staff       (20)        1 2023-04-07 10:28:17.000000 openapify-0.1.1/openapify.egg-info/dependency_links.txt
--rw-r--r--   0 alexander.tikhonov   (503) staff       (20)        1 2023-04-07 10:28:17.000000 openapify-0.1.1/openapify.egg-info/not-zip-safe
--rw-r--r--   0 alexander.tikhonov   (503) staff       (20)       42 2023-04-07 10:28:17.000000 openapify-0.1.1/openapify.egg-info/requires.txt
--rw-r--r--   0 alexander.tikhonov   (503) staff       (20)       10 2023-04-07 10:28:17.000000 openapify-0.1.1/openapify.egg-info/top_level.txt
--rw-r--r--   0 alexander.tikhonov   (503) staff       (20)      364 2023-03-17 15:32:02.000000 openapify-0.1.1/pyproject.toml
--rw-r--r--   0 alexander.tikhonov   (503) staff       (20)       38 2023-04-07 10:28:17.376577 openapify-0.1.1/setup.cfg
--rw-r--r--   0 alexander.tikhonov   (503) staff       (20)     1099 2023-04-07 10:24:56.000000 openapify-0.1.1/setup.py
+drwxr-xr-x   0 alexander.tikhonov   (503) staff       (20)        0 2023-04-07 11:50:27.743728 openapify-0.1.2/
+-rw-r--r--   0 alexander.tikhonov   (503) staff       (20)      732 2023-04-07 11:50:27.743556 openapify-0.1.2/PKG-INFO
+drwxr-xr-x   0 alexander.tikhonov   (503) staff       (20)        0 2023-04-07 11:50:27.739756 openapify-0.1.2/openapify/
+-rw-r--r--   0 alexander.tikhonov   (503) staff       (20)      198 2023-04-03 17:00:50.000000 openapify-0.1.2/openapify/__init__.py
+drwxr-xr-x   0 alexander.tikhonov   (503) staff       (20)        0 2023-04-07 11:50:27.742201 openapify-0.1.2/openapify/core/
+-rw-r--r--   0 alexander.tikhonov   (503) staff       (20)        0 2023-04-03 13:14:57.000000 openapify-0.1.2/openapify/core/__init__.py
+-rw-r--r--   0 alexander.tikhonov   (503) staff       (20)     1123 2023-04-07 11:40:06.000000 openapify-0.1.2/openapify/core/apispec.py
+-rw-r--r--   0 alexander.tikhonov   (503) staff       (20)    15113 2023-04-06 11:04:29.000000 openapify-0.1.2/openapify/core/builder.py
+-rw-r--r--   0 alexander.tikhonov   (503) staff       (20)       92 2023-03-20 20:50:13.000000 openapify-0.1.2/openapify/core/const.py
+-rw-r--r--   0 alexander.tikhonov   (503) staff       (20)      591 2023-04-03 13:10:22.000000 openapify-0.1.2/openapify/core/jsonschema.py
+-rw-r--r--   0 alexander.tikhonov   (503) staff       (20)     1748 2023-04-07 11:38:54.000000 openapify-0.1.2/openapify/core/models.py
+drwxr-xr-x   0 alexander.tikhonov   (503) staff       (20)        0 2023-04-07 11:50:27.742527 openapify-0.1.2/openapify/core/openapi/
+-rw-r--r--   0 alexander.tikhonov   (503) staff       (20)        0 2023-03-20 12:12:59.000000 openapify-0.1.2/openapify/core/openapi/__init__.py
+-rw-r--r--   0 alexander.tikhonov   (503) staff       (20)     5270 2023-04-07 11:47:46.000000 openapify-0.1.2/openapify/core/openapi/models.py
+-rw-r--r--   0 alexander.tikhonov   (503) staff       (20)     4769 2023-04-07 11:42:13.000000 openapify-0.1.2/openapify/decorators.py
+drwxr-xr-x   0 alexander.tikhonov   (503) staff       (20)        0 2023-04-07 11:50:27.742761 openapify-0.1.2/openapify/ext/
+-rw-r--r--   0 alexander.tikhonov   (503) staff       (20)        0 2023-03-17 15:48:32.000000 openapify-0.1.2/openapify/ext/__init__.py
+drwxr-xr-x   0 alexander.tikhonov   (503) staff       (20)        0 2023-04-07 11:50:27.742946 openapify-0.1.2/openapify/ext/web/
+-rw-r--r--   0 alexander.tikhonov   (503) staff       (20)        0 2023-03-18 09:45:46.000000 openapify-0.1.2/openapify/ext/web/__init__.py
+-rw-r--r--   0 alexander.tikhonov   (503) staff       (20)     4332 2023-04-03 13:47:08.000000 openapify-0.1.2/openapify/ext/web/aiohttp.py
+-rw-r--r--   0 alexander.tikhonov   (503) staff       (20)        0 2023-03-17 11:19:37.000000 openapify-0.1.2/openapify/py.typed
+drwxr-xr-x   0 alexander.tikhonov   (503) staff       (20)        0 2023-04-07 11:50:27.740610 openapify-0.1.2/openapify.egg-info/
+-rw-r--r--   0 alexander.tikhonov   (503) staff       (20)      732 2023-04-07 11:50:27.000000 openapify-0.1.2/openapify.egg-info/PKG-INFO
+-rw-r--r--   0 alexander.tikhonov   (503) staff       (20)      594 2023-04-07 11:50:27.000000 openapify-0.1.2/openapify.egg-info/SOURCES.txt
+-rw-r--r--   0 alexander.tikhonov   (503) staff       (20)        1 2023-04-07 11:50:27.000000 openapify-0.1.2/openapify.egg-info/dependency_links.txt
+-rw-r--r--   0 alexander.tikhonov   (503) staff       (20)        1 2023-04-07 10:28:17.000000 openapify-0.1.2/openapify.egg-info/not-zip-safe
+-rw-r--r--   0 alexander.tikhonov   (503) staff       (20)       42 2023-04-07 11:50:27.000000 openapify-0.1.2/openapify.egg-info/requires.txt
+-rw-r--r--   0 alexander.tikhonov   (503) staff       (20)       10 2023-04-07 11:50:27.000000 openapify-0.1.2/openapify.egg-info/top_level.txt
+-rw-r--r--   0 alexander.tikhonov   (503) staff       (20)      364 2023-04-07 11:44:47.000000 openapify-0.1.2/pyproject.toml
+-rw-r--r--   0 alexander.tikhonov   (503) staff       (20)       38 2023-04-07 11:50:27.743787 openapify-0.1.2/setup.cfg
+-rw-r--r--   0 alexander.tikhonov   (503) staff       (20)     1099 2023-04-07 11:50:16.000000 openapify-0.1.2/setup.py
```

### Comparing `openapify-0.1.1/PKG-INFO` & `openapify-0.1.2/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: openapify
-Version: 0.1.1
+Version: 0.1.2
 Summary: Generate Open API Specification using decorators
 Author: Alexander Tikhonov
 Author-email: random.gauss@gmail.com
 License: Apache License, Version 2.0
 Platform: all
 Classifier: License :: OSI Approved :: Apache Software License
 Classifier: Intended Audience :: Developers
```

### Comparing `openapify-0.1.1/openapify/core/apispec.py` & `openapify-0.1.2/openapify/core/apispec.py`

 * *Files 4% similar despite different names*

```diff
@@ -1,21 +1,23 @@
+from typing import Any, List, Mapping, Optional, Sequence, Union
+
 import apispec as _apispec
-from typing import Sequence, Any, Optional, Union, List, Dict
-from openapify.core.openapi.models import Server, SecurityScheme
+
+from openapify.core.openapi.models import SecurityScheme, Server
 
 
 class APISpec(_apispec.APISpec):
     def __init__(
         self,
         title: str,
         version: str,
         openapi_version: str,
         plugins: Sequence[_apispec.BasePlugin] = (),
         servers: Optional[List[Union[str, Server]]] = None,
-        security_schemes: Optional[Dict[str, SecurityScheme]] = None,
+        security_schemes: Optional[Mapping[str, SecurityScheme]] = None,
         **options: Any,
     ) -> None:
         _servers = []
         for server in servers or ():
             if isinstance(server, str):
                 _servers.append({"url": server})
             else:
```

### Comparing `openapify-0.1.1/openapify/core/builder.py` & `openapify-0.1.2/openapify/core/builder.py`

 * *Files identical despite different names*

### Comparing `openapify-0.1.1/openapify/core/jsonschema.py` & `openapify-0.1.2/openapify/core/jsonschema.py`

 * *Files identical despite different names*

### Comparing `openapify-0.1.1/openapify/core/models.py` & `openapify-0.1.2/openapify/core/models.py`

 * *Files 6% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 from dataclasses import dataclass
-from typing import Any, Dict, List, NamedTuple, Optional, Type, Union
+from typing import Any, List, Mapping, NamedTuple, Optional, Type, Union
 
 from typing_extensions import TypeAlias
 
 from openapify.core.openapi.models import Example, Parameter, SecurityScheme
 
-SecurityRequirement: TypeAlias = Dict[str, "SecurityScheme"]
+SecurityRequirement: TypeAlias = Mapping[str, "SecurityScheme"]
 
 
 @dataclass
 class RouteDef:
     path: str
     method: str
     handler: Any
@@ -21,42 +21,42 @@
 
 class Body(NamedTuple):
     value_type: Type
     media_type: str = "application/json"
     required: Optional[bool] = None
     description: Optional[str] = None
     example: Optional[Any] = None
-    examples: Optional[Dict[str, Union[Example, Any]]] = None
+    examples: Optional[Mapping[str, Union[Example, Any]]] = None
 
 
 @dataclass
 class Header:
     description: Optional[str] = None
     required: Optional[bool] = None
     value_type: Type = str
     deprecated: Optional[bool] = None
     allowEmptyValue: Optional[bool] = None
     example: Optional[Any] = None
-    examples: Optional[Dict[str, Union[Example, Any]]] = None
+    examples: Optional[Mapping[str, Union[Example, Any]]] = None
 
 
 @dataclass
 class Cookie:
     description: Optional[str] = None
     required: Optional[bool] = None
     value_type: Type = str
     deprecated: Optional[bool] = None
     allowEmptyValue: Optional[bool] = None
     example: Optional[Any] = None
-    examples: Optional[Dict[str, Union[Example, Any]]] = None
+    examples: Optional[Mapping[str, Union[Example, Any]]] = None
 
 
 @dataclass
 class QueryParam:
     value_type: Type = str
     default: Optional[Any] = None
     required: Optional[bool] = None
     description: Optional[str] = None
     deprecated: Optional[bool] = None
     allowEmptyValue: Optional[bool] = None
     example: Optional[Any] = None
-    examples: Optional[Dict[str, Union[Example, Any]]] = None
+    examples: Optional[Mapping[str, Union[Example, Any]]] = None
```

### Comparing `openapify-0.1.1/openapify/core/openapi/models.py` & `openapify-0.1.2/openapify/core/openapi/models.py`

 * *Files 4% similar despite different names*

```diff
@@ -1,17 +1,17 @@
 from dataclasses import dataclass
 from enum import Enum
-from typing import Any, Dict, List, Literal, Optional, Union
+from typing import Any, Dict, List, Literal, Mapping, Optional, Union
 
 from mashumaro import DataClassDictMixin
 from mashumaro.config import BaseConfig
 from typing_extensions import TypeAlias
 
 HttpCode: TypeAlias = Union[str, int]
-Schema: TypeAlias = Dict[str, Any]
+Schema: TypeAlias = Mapping[str, Any]
 
 
 @dataclass
 class Object(DataClassDictMixin):
     class Config(BaseConfig):
         omit_none = True
 
@@ -23,15 +23,15 @@
     description: Optional[str] = None
 
 
 @dataclass
 class Server(Object):
     url: str
     description: Optional[str] = None
-    variables: Optional[Dict[str, ServerVariable]] = None
+    variables: Optional[Mapping[str, ServerVariable]] = None
 
 
 @dataclass
 class Example(Object):
     summary: Optional[str] = None
     description: Optional[str] = None
     value: Optional[Any] = None
@@ -41,43 +41,43 @@
 class Header(Object):
     schema: Schema
     description: Optional[str] = None
     required: Optional[bool] = None
     deprecated: Optional[bool] = None
     allowEmptyValue: Optional[bool] = None
     example: Optional[Any] = None
-    examples: Optional[Dict[str, Example]] = None
+    examples: Optional[Mapping[str, Example]] = None
 
 
 @dataclass
 class MediaType(Object):
     schema: Optional[Schema]
     example: Optional[Any] = None
-    examples: Optional[Dict[str, Example]] = None
+    examples: Optional[Mapping[str, Example]] = None
     encoding: Optional[str] = None
 
 
 @dataclass
 class RequestBody(Object):
     description: Optional[str] = None
-    content: Optional[Dict[str, MediaType]] = None
+    content: Optional[Mapping[str, MediaType]] = None
     required: Optional[bool] = None
 
 
 @dataclass
 class Response(Object):
     description: Optional[str] = None
-    headers: Optional[Dict[str, Header]] = None
-    content: Optional[Dict[str, MediaType]] = None
+    headers: Optional[Mapping[str, Header]] = None
+    content: Optional[Mapping[str, MediaType]] = None
 
 
 @dataclass
 class Responses(Object):
     default: Optional[Response] = None
-    codes: Dict[HttpCode, Response] = None
+    codes: Optional[Mapping[HttpCode, Response]] = None
 
     def __post_serialize__(self, d: Dict[Any, Any]):
         codes = d.pop("codes", None)
         if codes:
             d.update(codes)
         return d
 
@@ -102,16 +102,16 @@
     required: Optional[bool] = None
     deprecated: Optional[bool] = None
     allowEmptyValue: Optional[bool] = None
     style: Optional[ParameterStyle] = None
     explode: Optional[bool] = None
     schema: Optional[Schema] = None
     example: Optional[Any] = None
-    examples: Optional[Dict[str, Example]] = None
-    content: Optional[Dict[str, MediaType]] = None
+    examples: Optional[Mapping[str, Example]] = None
+    content: Optional[Mapping[str, MediaType]] = None
 
     class Config(Object.Config):
         serialize_by_alias = True
         aliases = {"location": "in"}
 
 
 @dataclass
@@ -185,15 +185,15 @@
     summary: Optional[str] = None
     description: Optional[str] = None
     externalDocs: Optional[ExternalDocumentation] = None
     parameters: Optional[List[Parameter]] = None
     requestBody: Optional[RequestBody] = None
     responses: Optional[Responses] = None
     deprecated: Optional[bool] = None
-    security: Optional[List[Dict[str, str]]] = None
+    security: Optional[List[Mapping[str, str]]] = None
 
 
 @dataclass
 class PathItem(Object):
     # TODO: Do we need this class?
     ref: Optional[str] = None
     summary: Optional[str] = None
```

### Comparing `openapify-0.1.1/openapify/decorators.py` & `openapify-0.1.2/openapify/decorators.py`

 * *Files 5% similar despite different names*

```diff
@@ -1,12 +1,12 @@
 from typing import (
     Any,
     Callable,
-    Dict,
     List,
+    Mapping,
     Optional,
     Sequence,
     Tuple,
     Type,
     TypeVar,
     Union,
     overload,
@@ -27,48 +27,48 @@
 Handler = TypeVar("Handler")
 
 
 @overload
 def request_schema(
     body: Optional[Body] = None,
     *,
-    query_params: Optional[Dict[str, Union[Type, QueryParam]]] = None,
-    headers: Optional[Dict[str, Union[str, Header]]] = None,
-    cookies: Optional[Dict[str, Union[str, Cookie]]] = None,
+    query_params: Optional[Mapping[str, Union[Type, QueryParam]]] = None,
+    headers: Optional[Mapping[str, Union[str, Header]]] = None,
+    cookies: Optional[Mapping[str, Union[str, Cookie]]] = None,
 ) -> Callable[[Handler], Handler]:
     ...
 
 
 @overload
 def request_schema(
     body: Optional[Type] = None,
     *,
     media_type: str = "application/json",
     body_required: bool = False,
     body_description: Optional[str] = None,
     body_example: Optional[Any] = None,
-    body_examples: Optional[Dict[str, Union[Example, Any]]] = None,
-    query_params: Optional[Dict[str, Union[Type, QueryParam]]] = None,
-    headers: Optional[Dict[str, Union[str, Header]]] = None,
-    cookies: Optional[Dict[str, Union[str, Cookie]]] = None,
+    body_examples: Optional[Mapping[str, Union[Example, Any]]] = None,
+    query_params: Optional[Mapping[str, Union[Type, QueryParam]]] = None,
+    headers: Optional[Mapping[str, Union[str, Header]]] = None,
+    cookies: Optional[Mapping[str, Union[str, Cookie]]] = None,
 ) -> Callable[[Handler], Handler]:
     ...
 
 
 def request_schema(
     body: Optional[Type] = None,
     *,
     media_type: str = "application/json",
     body_required: bool = False,
     body_description: Optional[str] = None,
     body_example: Optional[Any] = None,
-    body_examples: Optional[Dict[str, Union[Example, Any]]] = None,
-    query_params: Optional[Dict[str, Union[Type, QueryParam]]] = None,
-    headers: Optional[Dict[str, Union[str, Header]]] = None,
-    cookies: Optional[Dict[str, Union[str, Cookie]]] = None,
+    body_examples: Optional[Mapping[str, Union[Example, Any]]] = None,
+    query_params: Optional[Mapping[str, Union[Type, QueryParam]]] = None,
+    headers: Optional[Mapping[str, Union[str, Header]]] = None,
+    cookies: Optional[Mapping[str, Union[str, Cookie]]] = None,
 ) -> Callable[[Handler], Handler]:
     def decorator(handler: Handler) -> Handler:
         meta = getattr(handler, __openapify__, [])
         if not meta:
             handler.__openapify__ = meta
         meta.append(
             (
@@ -92,17 +92,17 @@
 
 
 def response_schema(
     schema: Type,
     http_code: HttpCode = 200,
     media_type: str = "application/json",
     description: Optional[str] = None,
-    headers: Optional[Dict[str, Union[str, Header]]] = None,
+    headers: Optional[Mapping[str, Union[str, Header]]] = None,
     example: Optional[Any] = None,
-    examples: Optional[Dict[str, Union[Example, Any]]] = None,
+    examples: Optional[Mapping[str, Union[Example, Any]]] = None,
 ):
     def decorator(handler):
         meta = getattr(handler, __openapify__, [])
         if not meta:
             handler.__openapify__ = meta
         meta.append(
             (
@@ -123,15 +123,15 @@
     return decorator
 
 
 def path_docs(
     summary: Optional[str] = None,
     description: Optional[str] = None,
     tags: Optional[Sequence[str]] = None,
-    parameters: Optional[Dict[str, Union[str, Parameter]]] = None,
+    parameters: Optional[Mapping[str, Union[str, Parameter]]] = None,
     external_docs: Optional[Union[str, Tuple[str, str]]] = None,
     deprecated: Optional[bool] = None,
 ):
     def decorator(handler):
         meta = getattr(handler, __openapify__, [])
         if not meta:
             handler.__openapify__ = meta
```

### Comparing `openapify-0.1.1/openapify/ext/web/aiohttp.py` & `openapify-0.1.2/openapify/ext/web/aiohttp.py`

 * *Files identical despite different names*

### Comparing `openapify-0.1.1/openapify.egg-info/PKG-INFO` & `openapify-0.1.2/openapify.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: openapify
-Version: 0.1.1
+Version: 0.1.2
 Summary: Generate Open API Specification using decorators
 Author: Alexander Tikhonov
 Author-email: random.gauss@gmail.com
 License: Apache License, Version 2.0
 Platform: all
 Classifier: License :: OSI Approved :: Apache Software License
 Classifier: Intended Audience :: Developers
```

### Comparing `openapify-0.1.1/openapify.egg-info/SOURCES.txt` & `openapify-0.1.2/openapify.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `openapify-0.1.1/setup.py` & `openapify-0.1.2/setup.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,14 +1,14 @@
 #!/usr/bin/env python
 
 from setuptools import find_packages, setup
 
 setup(
     name="openapify",
-    version="0.1.1",
+    version="0.1.2",
     description="Generate Open API Specification using decorators",
     platforms="all",
     classifiers=[
         "License :: OSI Approved :: Apache Software License",
         "Intended Audience :: Developers",
         "Programming Language :: Python :: 3 :: Only",
         "Programming Language :: Python :: 3.7",
```

