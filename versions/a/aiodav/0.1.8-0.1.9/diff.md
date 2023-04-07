# Comparing `tmp/aiodav-0.1.8.tar.gz` & `tmp/aiodav-0.1.9.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "aiodav-0.1.8.tar", last modified: Mon Oct 18 15:55:03 2021, max compression
+gzip compressed data, was "aiodav-0.1.9.tar", last modified: Thu Aug 25 17:25:23 2022, max compression
```

## Comparing `aiodav-0.1.8.tar` & `aiodav-0.1.9.tar`

### file list

```diff
@@ -1,18 +1,18 @@
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-10-18 15:55:03.075536 aiodav-0.1.8/
--rw-r--r--   0 runner    (1001) docker     (121)     1084 2021-10-18 15:54:54.000000 aiodav-0.1.8/LICENSE
--rw-r--r--   0 runner    (1001) docker     (121)     2328 2021-10-18 15:55:03.075536 aiodav-0.1.8/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (121)     1516 2021-10-18 15:54:54.000000 aiodav-0.1.8/README.md
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-10-18 15:55:03.071536 aiodav-0.1.8/aiodav/
--rw-r--r--   0 runner    (1001) docker     (121)      100 2021-10-18 15:54:54.000000 aiodav-0.1.8/aiodav/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    45720 2021-10-18 15:54:54.000000 aiodav-0.1.8/aiodav/client.py
--rw-r--r--   0 runner    (1001) docker     (121)     2659 2021-10-18 15:54:54.000000 aiodav-0.1.8/aiodav/exceptions.py
--rw-r--r--   0 runner    (1001) docker     (121)     2113 2021-10-18 15:54:54.000000 aiodav-0.1.8/aiodav/urn.py
--rw-r--r--   0 runner    (1001) docker     (121)    10551 2021-10-18 15:54:54.000000 aiodav-0.1.8/aiodav/utils.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-10-18 15:55:03.075536 aiodav-0.1.8/aiodav.egg-info/
--rw-r--r--   0 runner    (1001) docker     (121)     2328 2021-10-18 15:55:02.000000 aiodav-0.1.8/aiodav.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (121)      262 2021-10-18 15:55:02.000000 aiodav-0.1.8/aiodav.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (121)        1 2021-10-18 15:55:02.000000 aiodav-0.1.8/aiodav.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (121)       38 2021-10-18 15:55:02.000000 aiodav-0.1.8/aiodav.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (121)        7 2021-10-18 15:55:02.000000 aiodav-0.1.8/aiodav.egg-info/top_level.txt
--rw-r--r--   0 runner    (1001) docker     (121)       38 2021-10-18 15:55:03.075536 aiodav-0.1.8/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (121)     1430 2021-10-18 15:54:54.000000 aiodav-0.1.8/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-08-25 17:25:23.804350 aiodav-0.1.9/
+-rw-r--r--   0 runner    (1001) docker     (121)     1084 2022-08-25 17:25:11.000000 aiodav-0.1.9/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (121)     2360 2022-08-25 17:25:23.804350 aiodav-0.1.9/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (121)     1568 2022-08-25 17:25:11.000000 aiodav-0.1.9/README.md
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-08-25 17:25:23.804350 aiodav-0.1.9/aiodav/
+-rw-r--r--   0 runner    (1001) docker     (121)      100 2022-08-25 17:25:11.000000 aiodav-0.1.9/aiodav/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    47471 2022-08-25 17:25:11.000000 aiodav-0.1.9/aiodav/client.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2559 2022-08-25 17:25:11.000000 aiodav-0.1.9/aiodav/exceptions.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2100 2022-08-25 17:25:11.000000 aiodav-0.1.9/aiodav/urn.py
+-rw-r--r--   0 runner    (1001) docker     (121)    10689 2022-08-25 17:25:11.000000 aiodav-0.1.9/aiodav/utils.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-08-25 17:25:23.804350 aiodav-0.1.9/aiodav.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (121)     2360 2022-08-25 17:25:23.000000 aiodav-0.1.9/aiodav.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (121)      262 2022-08-25 17:25:23.000000 aiodav-0.1.9/aiodav.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (121)        1 2022-08-25 17:25:23.000000 aiodav-0.1.9/aiodav.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (121)       38 2022-08-25 17:25:23.000000 aiodav-0.1.9/aiodav.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (121)        7 2022-08-25 17:25:23.000000 aiodav-0.1.9/aiodav.egg-info/top_level.txt
+-rw-r--r--   0 runner    (1001) docker     (121)       38 2022-08-25 17:25:23.804350 aiodav-0.1.9/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (121)     1373 2022-08-25 17:25:11.000000 aiodav-0.1.9/setup.py
```

### Comparing `aiodav-0.1.8/LICENSE` & `aiodav-0.1.9/LICENSE`

 * *Files identical despite different names*

### Comparing `aiodav-0.1.8/PKG-INFO` & `aiodav-0.1.9/PKG-INFO`

 * *Files 6% similar despite different names*

```diff
@@ -1,17 +1,16 @@
 Metadata-Version: 2.1
 Name: aiodav
-Version: 0.1.8
+Version: 0.1.9
 Summary: A Python Async WebDAV Client
 Home-page: https://github.com/jorgeajimenezl/aiodav
 Author: Jorge Alejandro Jimenez Luna
 Author-email: jorgeajimenezl17@gmail.com
 License: MIT License
 Keywords: webdav,client,files,internet,download,upload
-Platform: UNKNOWN
 Classifier: Intended Audience :: Developers
 Classifier: License :: OSI Approved :: MIT License
 Classifier: Operating System :: OS Independent
 Classifier: Programming Language :: Python
 Classifier: Programming Language :: Python :: 3.5
 Classifier: Programming Language :: Python :: 3.6
 Classifier: Programming Language :: Python :: 3.7
@@ -20,14 +19,15 @@
 Description-Content-Type: text/markdown
 License-File: LICENSE
 
 # Python Async WebDAV Client
 [![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=jorgeajimenezl_aiodav&metric=alert_status)](https://sonarcloud.io/dashboard?id=jorgeajimenezl_aiodav)
 [![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=jorgeajimenezl_aiodav&metric=sqale_rating)](https://sonarcloud.io/dashboard?id=jorgeajimenezl_aiodav)
 ![PyPI](https://img.shields.io/pypi/v/aiodav)
+![Downloads](https://img.shields.io/pypi/dm/aiodav)
 ![PyPI - Python Version](https://img.shields.io/pypi/pyversions/aiodav)
 
 A asynchronous WebDAV client that use `asyncio` 
 
 > Based on [webdavclient3](https://github.com/ezhov-evgeny/webdav-client-python-3)
 
 ## Installation
@@ -61,9 +61,7 @@
                                     progress=progress)
 
 asyncio.run(main())
 ```
 
 ## License
 [MIT License](./LICENSE)
-
-
```

### Comparing `aiodav-0.1.8/README.md` & `aiodav-0.1.9/README.md`

 * *Files 4% similar despite different names*

```diff
@@ -1,11 +1,12 @@
 # Python Async WebDAV Client
 [![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=jorgeajimenezl_aiodav&metric=alert_status)](https://sonarcloud.io/dashboard?id=jorgeajimenezl_aiodav)
 [![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=jorgeajimenezl_aiodav&metric=sqale_rating)](https://sonarcloud.io/dashboard?id=jorgeajimenezl_aiodav)
 ![PyPI](https://img.shields.io/pypi/v/aiodav)
+![Downloads](https://img.shields.io/pypi/dm/aiodav)
 ![PyPI - Python Version](https://img.shields.io/pypi/pyversions/aiodav)
 
 A asynchronous WebDAV client that use `asyncio` 
 
 > Based on [webdavclient3](https://github.com/ezhov-evgeny/webdav-client-python-3)
 
 ## Installation
```

### Comparing `aiodav-0.1.8/aiodav/client.py` & `aiodav-0.1.9/aiodav/client.py`

 * *Files 4% similar despite different names*

```diff
@@ -1,13 +1,27 @@
 import logging
 import asyncio
 import os
 import shutil
 from types import TracebackType
-from typing import Any, AsyncGenerator, Callable, Coroutine, Dict, Generator, IO, Iterable, Optional, Tuple, Type, Union, List
+from typing import (
+    Any,
+    AsyncGenerator,
+    Callable,
+    Coroutine,
+    Dict,
+    Generator,
+    IO,
+    Iterable,
+    Optional,
+    Tuple,
+    Type,
+    Union,
+    List,
+)
 from aiofiles.threadpool.binary import AsyncBufferedIOBase
 
 import aiohttp
 import aiofiles
 from aiohttp.client import DEFAULT_TIMEOUT
 
 from aiodav.utils import WebDavXmlUtils
@@ -55,48 +69,56 @@
 
         chunk_size (``int``, *optional*):
             Size of buffer used to transfer data from/to server. This data will be
             loaded in memory. This parameter afect the progress callback in
             download/upload functions. Default is 65536 bytes (65K)
     """
 
-    ROOT = '/'
+    ROOT = "/"
 
     # HTTP headers for different actions
     DEFAULT_HTTP_HEADER = {
-        'list': ["Accept: */*", "Depth: 1"],
-        'free': ["Accept: */*", "Depth: 0", "Content-Type: text/xml"],
-        'copy': ["Accept: */*"],
-        'move': ["Accept: */*"],
-        'mkdir': ["Accept: */*", "Connection: Keep-Alive"],
-        'clean': ["Accept: */*", "Connection: Keep-Alive"],
-        'check': ["Accept: */*"],
-        'info': ["Accept: */*", "Depth: 1"],
-        'get_property': ["Accept: */*", "Depth: 1", "Content-Type: application/x-www-form-urlencoded"],
-        'set_property': ["Accept: */*", "Depth: 1", "Content-Type: application/x-www-form-urlencoded"]
+        "list": ["Accept: */*", "Depth: 1"],
+        "free": ["Accept: */*", "Depth: 0", "Content-Type: text/xml"],
+        "copy": ["Accept: */*"],
+        "move": ["Accept: */*"],
+        "mkdir": ["Accept: */*", "Connection: Keep-Alive"],
+        "clean": ["Accept: */*", "Connection: Keep-Alive"],
+        "check": ["Accept: */*"],
+        "info": ["Accept: */*", "Depth: 1"],
+        "get_property": [
+            "Accept: */*",
+            "Depth: 1",
+            "Content-Type: application/x-www-form-urlencoded",
+        ],
+        "set_property": [
+            "Accept: */*",
+            "Depth: 1",
+            "Content-Type: application/x-www-form-urlencoded",
+        ],
     }
 
     # mapping of actions to WebDAV methods
     DEFAULT_REQUESTS = {
-        'options': 'OPTIONS',
-        'download': "GET",
-        'upload': "PUT",
-        'copy': "COPY",
-        'move': "MOVE",
-        'mkdir': "MKCOL",
-        'clean': "DELETE",
-        'check': "HEAD",
-        'list': "PROPFIND",
-        'free': "PROPFIND",
-        'info': "PROPFIND",
-        'publish': "PROPPATCH",
-        'unpublish': "PROPPATCH",
-        'published': "PROPPATCH",
-        'get_property': "PROPFIND",
-        'set_property': "PROPPATCH"
+        "options": "OPTIONS",
+        "download": "GET",
+        "upload": "PUT",
+        "copy": "COPY",
+        "move": "MOVE",
+        "mkdir": "MKCOL",
+        "clean": "DELETE",
+        "check": "HEAD",
+        "list": "PROPFIND",
+        "free": "PROPFIND",
+        "info": "PROPFIND",
+        "publish": "PROPPATCH",
+        "unpublish": "PROPPATCH",
+        "published": "PROPPATCH",
+        "get_property": "PROPFIND",
+        "set_property": "PROPPATCH",
     }
 
     def __init__(
         self,
         hostname: str,
         login: Optional[str] = None,
         password: Optional[str] = None,
@@ -105,93 +127,104 @@
         timeout: Optional[int] = None,
         chunk_size: Optional[int] = None,
         proxy: Optional[str] = None,
         proxy_user: Optional[str] = None,
         proxy_password: Optional[str] = None,
         insecure: Optional[bool] = False,
         loop: Optional[asyncio.AbstractEventLoop] = None,
-        **kwargs: Any
+        **kwargs: Any,
     ) -> None:
         self._hostname = hostname.rstrip(Urn.separate)
         self._token = token
-        self._root = (Urn(root).quote() if root else '').rstrip(Urn.separate)
+        self._root = (Urn(root).quote() if root else "").rstrip(Urn.separate)
         self._chunk_size = chunk_size if chunk_size else 65536
         self._proxy = proxy
-        self._proxy_auth = aiohttp.BasicAuth(proxy_user, proxy_password) if (
-            proxy_user and proxy_password) else None
+        self._proxy_auth = (
+            aiohttp.BasicAuth(proxy_user, proxy_password)
+            if (proxy_user and proxy_password)
+            else None
+        )
         self._insecure = insecure
-        self.session = aiohttp.ClientSession(
+        self.session = (
+            kwargs.get("session", None) or
+            aiohttp.ClientSession(
             loop=loop,
-            timeout=aiohttp.ClientTimeout(total=timeout) if timeout else DEFAULT_TIMEOUT,
-            auth=aiohttp.BasicAuth(login, password) if (
-                login and password) else None,
-            connector=kwargs.get('connector', None)
+            timeout=aiohttp.ClientTimeout(total=timeout)
+            if timeout
+            else DEFAULT_TIMEOUT,
+            auth=aiohttp.BasicAuth(login, password) if (login and password) else None,
+            connector=kwargs.get("connector", None),
+            )
         )
 
     def _get_headers(
-        self,
-        action: str,
-        headers_ext: Optional[Dict[str, str]] = None
+        self, action: str, headers_ext: Optional[Dict[str, str]] = None
     ) -> Dict[str, str]:
         headers = None
         if action in Client.DEFAULT_HTTP_HEADER:
-            headers = dict([map(lambda s: s.strip(), x.split(':', 1)) for x in Client.DEFAULT_HTTP_HEADER[action]])
+            headers = dict(
+                [
+                    map(lambda s: s.strip(), x.split(":", 1))
+                    for x in Client.DEFAULT_HTTP_HEADER[action]
+                ]
+            )
         else:
             headers = dict()
 
         if headers_ext:
             for k, v in headers_ext.items():
                 headers[k] = v
 
         if self._token:
-            headers['Authorization'] = f'Bearer {self._token}'
+            headers["Authorization"] = f"Bearer {self._token}"
 
         return headers
 
-    def _get_url(
-        self,
-        path: Union[str, "os.PathLike[str]"]
-    ) -> str:
+    def _get_url(self, path: Union[str, "os.PathLike[str]"]) -> str:
         return f"{self._hostname}{self._root}{path}"
 
-    def get_full_path(
-        self,
-        urn: Urn
-    ) -> str:
+    def get_full_path(self, urn: Urn) -> str:
         return f"{self._root}{urn.path()}"
 
-    async def _execute_request(self,
-                               action: str,
-                               path: Union[str, "os.PathLike[str]"],
-                               data: Optional[Any] = None,
-                               headers_ext: Optional[Dict[str, str]] = None
-                               ) -> aiohttp.ClientResponse:
+    async def _execute_request(
+        self,
+        action: str,
+        path: Union[str, "os.PathLike[str]"],
+        data: Optional[Any] = None,
+        headers_ext: Optional[Dict[str, str]] = None,
+    ) -> aiohttp.ClientResponse:
         try:
             if self.session.auth:
-                await self.session.get(url=self._hostname)  # (Re)Authenticates against the proxy
+                await self.session.get(
+                    url=self._hostname
+                )  # (Re)Authenticates against the proxy
 
             response = await self.session.request(
                 method=Client.DEFAULT_REQUESTS[action],
                 url=self._get_url(path),
                 headers=self._get_headers(action, headers_ext),
                 data=data,
                 proxy=self._proxy,
                 proxy_auth=self._proxy_auth,
                 # chunked = self._chunk_size,
-                ssl=False if self._insecure else None
+                ssl=False if self._insecure else None,
             )
 
             if response.status == 507:
                 raise NotEnoughSpace()
             if response.status == 404:
                 raise RemoteResourceNotFound(path=path)
             if response.status == 405:
                 raise MethodNotSupported(name=action, server=self._hostname)
             if response.status >= 400:
-                raise ResponseErrorCode(url=self._get_url(path), code=response.status, message=response.content)
+                raise ResponseErrorCode(
+                    url=self._get_url(path),
+                    code=response.status,
+                    message=response.content,
+                )
 
             return response
         except aiohttp.ClientConnectionError:
             raise NoConnection(self._hostname)
         except aiohttp.ClientResponseError as re:
             raise ConnectionException(re)
         except Exception as e:
@@ -221,15 +254,15 @@
         exc_tb: Optional[TracebackType],
     ) -> None:
         await self.session.close()
 
     async def list(
         self,
         path: Optional[Union[str, "os.PathLike[str]"]] = ROOT,
-        get_info: Optional[bool] = False
+        get_info: Optional[bool] = False,
     ) -> Union[List[str], List[Dict[str, str]]]:
         """
         Returns list of nested files and directories for remote WebDAV directory by path.
         More information you can find by link http://webdav.org/specs/rfc4918.html#METHOD_PROPFIN
 
         Parameters:
             path (``str``):
@@ -248,72 +281,78 @@
                 `size`: size of resource,
                 `modified`: date of resource modification,
                 `etag`: etag of resource,
                 `isdir`: type of resource,
                 `path`: path of resource.
         """
         directory_urn = Urn(path, directory=True)
-        if directory_urn.path() != Client.ROOT and not (await self.exists(directory_urn.path())):
+        if directory_urn.path() != Client.ROOT and not (
+            await self.exists(directory_urn.path())
+        ):
             raise RemoteResourceNotFound(directory_urn.path())
 
         path = Urn.normalize_path(self.get_full_path(directory_urn))
-        response = await self._execute_request(action='list', path=directory_urn.quote())
+        response = await self._execute_request(
+            action="list", path=directory_urn.quote()
+        )
         text = await response.text()
 
         if get_info:
             subfiles = WebDavXmlUtils.parse_get_list_info_response(text)
-            return [subfile for subfile in subfiles if Urn.compare_path(path, subfile.get('path')) is False]
+            return [
+                subfile
+                for subfile in subfiles
+                if Urn.compare_path(path, subfile.get("path")) is False
+            ]
 
         urns = WebDavXmlUtils.parse_get_list_response(text)
-        return [urn.filename() for urn in urns if Urn.compare_path(path, urn.path()) is False]
+        return [
+            urn.filename()
+            for urn in urns
+            if Urn.compare_path(path, urn.path()) is False
+        ]
 
     async def free(self) -> int:
         """
         Returns an amount of free space on remote WebDAV server.
         More information you can find by link http://webdav.org/specs/rfc4918.html#METHOD_PROPFIND
 
         Returns:
             :obj:`int`: An amount of free space in bytes.
         """
 
         data = WebDavXmlUtils.create_free_space_request_content()
-        response = await self._execute_request(action='free', path='', data=data)
+        response = await self._execute_request(action="free", path="", data=data)
         text = await response.text()
         return WebDavXmlUtils.parse_free_space_response(text, self._hostname)
 
-    async def exists(
-        self,
-        path: Union[str, "os.PathLike[str]"]
-    ) -> bool:
+    async def exists(self, path: Union[str, "os.PathLike[str]"]) -> bool:
         """
         Checks an existence of remote resource on WebDAV server by remote path.
         More information you can find by link http://webdav.org/specs/rfc4918.html#rfc.section.9.4
 
         Parameters:
             path (``str``):
                 Path to remote resource.
 
          Returns:
             :obj:`bool`: True if resource is exist or False otherwise.
         """
 
         urn = Urn(path)
         try:
-            response = await self._execute_request(action='check', path=urn.quote())
+            response = await self._execute_request(action="check", path=urn.quote())
         except RemoteResourceNotFound:
             return False
         except ResponseErrorCode:
             return False
 
-        return (int(response.status) == 200)
+        return int(response.status) == 200
 
-    async def create_directory(
-        self,
-        path: Union[str, "os.PathLike[str]"]
-    ) -> bool:
+    async def create_directory(self, path: Union[str, "os.PathLike[str]"]) -> bool:
         """
         Makes new directory on WebDAV server.
         More information you can find by link http://webdav.org/specs/rfc4918.html#METHOD_MKCOL
 
         Parameters:
             path (``str``):
                 Path to remote directory.
@@ -323,57 +362,55 @@
         """
 
         directory_urn = Urn(path, directory=True)
         if not (await self.exists(directory_urn.parent())):
             raise RemoteParentNotFound(directory_urn.path())
 
         try:
-            response = await self._execute_request(action='mkdir', path=directory_urn.quote())
+            response = await self._execute_request(
+                action="mkdir", path=directory_urn.quote()
+            )
         except MethodNotSupported:
             # Yandex WebDAV returns 405 status code when directory already exists
             return True
         return response.status in (200, 201)
 
     async def _check_remote_resource(
-        self,
-        path: Union[str, "os.PathLike[str]"],
-        urn: Urn
+        self, path: Union[str, "os.PathLike[str]"], urn: Urn
     ) -> None:
-        if not (await self.exists(urn.path())) and not (await self.exists(Urn(path, directory=True).path())):
+        if not (await self.exists(urn.path())) and not (
+            await self.exists(Urn(path, directory=True).path())
+        ):
             raise RemoteResourceNotFound(path)
 
-    async def is_directory(
-        self,
-        path: Union[str, "os.PathLike[str]"]
-    ) -> bool:
+    async def is_directory(self, path: Union[str, "os.PathLike[str]"]) -> bool:
         """
-        Checks is the remote resource directory.
+        Checks if the remote resource is a directory.
         More information you can find by link http://webdav.org/specs/rfc4918.html#METHOD_PROPFINDL
 
         Parameters:
             path (``str``):
                 Path to remote directory.
 
          Returns:
             :obj:`bool`: True in case the remote resource is directory and False otherwise.
         """
 
         urn = Urn(path)
         parent_urn = Urn(urn.parent())
         await self._check_remote_resource(path, urn)
 
-        response = await self._execute_request(action='info', path=parent_urn.quote())
+        response = await self._execute_request(action="info", path=parent_urn.quote())
         text = await response.text()
         path = self.get_full_path(urn)
-        return WebDavXmlUtils.parse_is_dir_response(content=text, path=path, hostname=self._hostname)
+        return WebDavXmlUtils.parse_is_dir_response(
+            content=text, path=path, hostname=self._hostname
+        )
 
-    async def info(
-        self,
-        path: Union[str, "os.PathLike[str]"]
-    ) -> Dict[str, str]:
+    async def info(self, path: Union[str, "os.PathLike[str]"]) -> Dict[str, str]:
         """
         Gets information about resource on WebDAV.
         More information you can find by link http://webdav.org/specs/rfc4918.html#METHOD_PROPFIND
 
         Parameters:
             path (``str``):
                 Path to remote resource.
@@ -387,40 +424,36 @@
                 `modified`: date of resource modification,
                 `etag`: etag of resource.
         """
 
         urn = Urn(path)
         await self._check_remote_resource(path, urn)
 
-        response = await self._execute_request(action='info', path=urn.quote())
+        response = await self._execute_request(action="info", path=urn.quote())
         text = await response.text()
         path = self.get_full_path(urn)
-        return WebDavXmlUtils.parse_info_response(content=text, path=path, hostname=self._hostname)
+        return WebDavXmlUtils.parse_info_response(
+            content=text, path=path, hostname=self._hostname
+        )
 
-    async def unlink(
-        self,
-        path: Union[str, "os.PathLike[str]"]
-    ) -> None:
+    async def unlink(self, path: Union[str, "os.PathLike[str]"]) -> None:
         """
         Cleans (Deletes) a remote resource on WebDAV server. The name of method is not changed for back compatibility
         with original library.
         More information you can find by link http://webdav.org/specs/rfc4918.html#METHOD_DELETE
 
         Parameters:
             path (``str``):
                 Path to remote resource.
         """
 
         urn = Urn(path)
-        await self._execute_request(action='clean', path=urn.quote())
+        await self._execute_request(action="clean", path=urn.quote())
 
-    async def delete(
-        self,
-        path: Union[str, "os.PathLike[str]"]
-    ) -> None:
+    async def delete(self, path: Union[str, "os.PathLike[str]"]) -> None:
         """
         Cleans (Deletes) a remote resource on WebDAV server. The name of method is not changed for back compatibility
         with original library.
         More information you can find by link http://webdav.org/specs/rfc4918.html#METHOD_DELETE
 
         Parameters:
             path (``str``):
@@ -429,15 +462,15 @@
 
         await self.unlink(path)
 
     async def move(
         self,
         source: Union[str, "os.PathLike[str]"],
         destination: Union[str, "os.PathLike[str]"],
-        overwrite: Optional[bool] = False
+        overwrite: Optional[bool] = False,
     ) -> None:
         """
         Moves resource from one place to another on WebDAV server.
         More information you can find by link http://webdav.org/specs/rfc4918.html#METHOD_MOVE
 
         Parameters:
             source (``str``):
@@ -455,25 +488,27 @@
             raise RemoteResourceNotFound(urn_from.path())
 
         urn_to = Urn(destination)
         if not (await self.exists(urn_to.parent())):
             raise RemoteParentNotFound(urn_to.path())
 
         headers = {
-            'Destination': self._get_url(urn_to.quote()),
-            'Overwrite': ('T' if overwrite else 'F')
+            "Destination": self._get_url(urn_to.quote()),
+            "Overwrite": ("T" if overwrite else "F"),
         }
 
-        await self._execute_request(action='move', path=urn_from.quote(), headers_ext=headers)
+        await self._execute_request(
+            action="move", path=urn_from.quote(), headers_ext=headers
+        )
 
     async def copy(
         self,
         source: Union[str, "os.PathLike[str]"],
         destination: Union[str, "os.PathLike[str]"],
-        depth: Optional[int] = 1
+        depth: Optional[int] = 1,
     ) -> None:
         """
         Copies resource from one place to another on WebDAV server.
         More information you can find by link http://webdav.org/specs/rfc4918.html#METHOD_COPY
 
         Parameters:
             source (``str``):
@@ -490,25 +525,24 @@
         if not (await self.exists(urn_from.path())):
             raise RemoteResourceNotFound(urn_from.path())
 
         urn_to = Urn(destination)
         if not (await self.exists(urn_to.parent())):
             raise RemoteParentNotFound(urn_to.path())
 
-        headers = {
-            "Destination": self._get_url(urn_to.quote())
-        }
-        if (await self.is_directory(urn_from.path())):
+        headers = {"Destination": self._get_url(urn_to.quote())}
+        if await self.is_directory(urn_from.path()):
             headers["Depth"] = depth
 
-        await self._execute_request(action='copy', path=urn_from.quote(), headers_ext=headers)
+        await self._execute_request(
+            action="copy", path=urn_from.quote(), headers_ext=headers
+        )
 
     async def download_iter(
-        self,
-        path: Union[str, "os.PathLike[str]"]
+        self, path: Union[str, "os.PathLike[str]"]
     ) -> Generator[bytes, None, None]:
         """
         Downloads file from server and return content in generator.
         More information you can find by link http://webdav.org/specs/rfc4918.html#rfc.section.9.4
 
         Parameters:
             path (``str``):
@@ -523,29 +557,29 @@
                 ...
                 async for chunk in client.download_iter('/path/to/file.zip'):
                     file.write(chunk)
                 ...
         """
 
         urn = Urn(path)
-        if (await self.is_directory(urn.path())):
+        if await self.is_directory(urn.path()):
             raise OptionNotValid(name="path", value=path)
 
         if not (await self.exists(urn.path())):
             raise RemoteResourceNotFound(urn.path())
 
-        response = await self._execute_request(action='download', path=urn.quote())
+        response = await self._execute_request(action="download", path=urn.quote())
         return response.content.iter_chunked(self._chunk_size)
 
     async def download_to(
         self,
         path: Union[str, "os.PathLike[str]"],
         buffer: IO,
         progress: Optional[Callable[[int, int, Tuple], None]] = None,
-        progress_args: Optional[Tuple] = ()
+        progress_args: Optional[Tuple] = (),
     ) -> None:
         """
         Downloads file from server and writes it in buffer.
         More information you can find by link http://webdav.org/specs/rfc4918.html#rfc.section.9.4
 
         Parameters:
             path (``str``):
@@ -585,22 +619,22 @@
 
                 async with aiofiles.open('file.zip', 'wb') as file:
                     await client.download_to('/path/to/file.zip', file, progress=progress)
                 ...
         """
 
         urn = Urn(path)
-        if (await self.is_directory(urn.path())):
+        if await self.is_directory(urn.path()):
             raise OptionNotValid(name="path", value=path)
 
         if not (await self.exists(urn.path())):
             raise RemoteResourceNotFound(urn.path())
 
-        response = await self._execute_request('download', urn.quote())
-        total = int(response.headers['content-length'])
+        response = await self._execute_request("download", urn.quote())
+        total = int(response.headers["content-length"])
         current = 0
 
         if callable(progress):
             if asyncio.iscoroutinefunction(progress):
                 await progress(current, total, *progress_args)
             else:
                 progress(current, total, *progress_args)
@@ -620,15 +654,15 @@
                     progress(current, total, *progress_args)
 
     async def download_file(
         self,
         remote_path: Union[str, "os.PathLike[str]"],
         local_path: Union[str, "os.PathLike[str]"],
         progress: Optional[Callable[[int, int, Tuple], None]] = None,
-        progress_args: Optional[Tuple] = ()
+        progress_args: Optional[Tuple] = (),
     ) -> None:
         """
         Downloads file from server and write to a file.
         More information you can find by link http://webdav.org/specs/rfc4918.html#rfc.section.9.4
 
         Parameters:
             remote_path (``str``):
@@ -666,23 +700,25 @@
                 def progress(current, total):
                     print(f"{current * 100 / total:.1f}%")
 
                 await client.download_to('/path/to/file.zip', '/home/file.zip', progress=progress)
                 ...
         """
 
-        async with aiofiles.open(local_path, 'wb') as file:
-            await self.download_to(remote_path, file, progress=progress, progress_args=progress_args)
+        async with aiofiles.open(local_path, "wb") as file:
+            await self.download_to(
+                remote_path, file, progress=progress, progress_args=progress_args
+            )
 
     async def download_directory(
         self,
         remote_path: Union[str, "os.PathLike[str]"],
         local_path: Union[str, "os.PathLike[str]"],
         progress: Optional[Callable[[int, int, Tuple], None]] = None,
-        progress_args: Optional[Tuple] = ()
+        progress_args: Optional[Tuple] = (),
     ) -> None:
         """
         Downloads directory and downloads all nested files and directories from remote server to local.
         If there is something on local path it deletes directories and files then creates new.
         More information you can find by link http://webdav.org/specs/rfc4918.html#rfc.section.9.4
 
         WARNING: Destructive method
@@ -726,22 +762,27 @@
 
         os.makedirs(local_path)
         async for resource_name in self.list(urn.path()):
             if urn.path().endswith(resource_name):
                 continue
             _remote_path = f"{urn.path()}{resource_name}"
             _local_path = os.path.join(local_path, resource_name)
-            await self.download(local_path=_local_path, remote_path=_remote_path, progress=progress, progress_args=progress_args)
+            await self.download(
+                local_path=_local_path,
+                remote_path=_remote_path,
+                progress=progress,
+                progress_args=progress_args,
+            )
 
     async def download(
         self,
         remote_path: Union[str, "os.PathLike[str]"],
         local_path: Union[str, "os.PathLike[str]"],
         progress: Optional[Callable[[int, int, Tuple], None]] = None,
-        progress_args: Optional[Tuple] = ()
+        progress_args: Optional[Tuple] = (),
     ) -> None:
         """
         Download a remote resourse and put in local path.
         More information you can find by link http://webdav.org/specs/rfc4918.html#rfc.section.9.4
 
         WARNING: DESTRUCTIVE METHOD (This method can call `self.download_directory`)
 
@@ -771,39 +812,54 @@
 
             *args (``tuple``, *optional*):
                 Extra custom arguments as defined in the ``progress_args`` parameter.
                 You can either keep ``*args`` or add every single extra argument in your function signature.
         """
 
         urn = Urn(remote_path)
-        if (await self.is_directory(urn.path())):
-            await self.download_directory(local_path=local_path, remote_path=remote_path, progress=progress, progress_args=progress_args)
+        if await self.is_directory(urn.path()):
+            await self.download_directory(
+                local_path=local_path,
+                remote_path=remote_path,
+                progress=progress,
+                progress_args=progress_args,
+            )
         else:
-            await self.download_file(local_path=local_path, remote_path=remote_path, progress=progress, progress_args=progress_args)
+            await self.download_file(
+                local_path=local_path,
+                remote_path=remote_path,
+                progress=progress,
+                progress_args=progress_args,
+            )
 
     async def upload_to(
         self,
         path: Union[str, "os.PathLike[str]"],
         buffer: Union[IO, AsyncGenerator[bytes, None]],
         buffer_size: Optional[int] = None,
+        overwrite: bool = True,
         progress: Optional[Callable[[int, int, Tuple], None]] = None,
-        progress_args: Optional[Tuple] = ()
+        progress_args: Optional[Tuple] = (),
     ) -> None:
         """
         Uploads file from buffer to remote path on WebDAV server.
         More information you can find by link http://webdav.org/specs/rfc4918.html#METHOD_PUT
 
         Parameters:
             path (``str``):
                 The path to remote resource
 
             buffer (``IO``)
                 IO like object to read the data or a asynchronous generator to get buffer data.
                 In order do you select use a async generator `progress` callback cannot be called.
 
+            overwrite (``bool``)
+                If true the will be overwriten by the new data if the a file with the same path exists. 
+                (Default to true)
+
             progress (``callable``, *optional*):
                 Pass a callback function to view the file transmission progress.
                 The function must take *(current, total)* as positional arguments (look at Other Parameters below for a
                 detailed description) and will be called back each time a new file chunk has been successfully
                 transmitted.
 
             progress_args (``tuple``, *optional*):
@@ -834,62 +890,76 @@
                 ...
         """
 
         urn = Urn(path)
         if urn.is_dir():
             raise OptionNotValid(name="path", value=path)
 
+        if not overwrite and (await self.exists(urn.path())):
+            return
+
         if not (await self.exists(urn.parent())):
             raise RemoteParentNotFound(urn.path())
 
         if callable(progress) and not asyncio.iscoroutinefunction(buffer):
+
             async def file_sender(buff: IO):
                 current = 0
 
                 if asyncio.iscoroutinefunction(progress):
                     await progress(current, buffer_size, *progress_args)
                 else:
                     progress(current, buffer_size, *progress_args)
 
                 while current < buffer_size:
-                    chunk = await buffer.read(self._chunk_size) if isinstance(buffer, AsyncBufferedIOBase) \
+                    chunk = (
+                        await buffer.read(self._chunk_size)
+                        if isinstance(buffer, AsyncBufferedIOBase)
                         else buffer.read(self._chunk_size)
+                    )
                     if not chunk:
                         break
 
                     current += len(chunk)
 
                     if asyncio.iscoroutinefunction(progress):
                         await progress(current, buffer_size, *progress_args)
                     else:
                         progress(current, buffer_size, *progress_args)
                     yield chunk
 
-            await self._execute_request(action='upload', path=urn.quote(), data=file_sender(buffer))
+            await self._execute_request(
+                action="upload", path=urn.quote(), data=file_sender(buffer)
+            )
         else:
-            await self._execute_request(action='upload', path=urn.quote(), data=buffer)
+            await self._execute_request(action="upload", path=urn.quote(), data=buffer)
 
     async def upload_file(
         self,
         remote_path: Union[str, "os.PathLike[str]"],
         local_path: Union[str, "os.PathLike[str]"],
+        overwrite: bool = True,
         progress: Optional[Callable[[int, int, Tuple], None]] = None,
-        progress_args: Optional[Tuple] = ()
+        progress_args: Optional[Tuple] = (),
     ) -> None:
         """
         Uploads file to remote path on WebDAV server. File should be 2Gb or less.
         More information you can find by link http://webdav.org/specs/rfc4918.html#METHOD_PUT
 
         Parameters:
             remote_path (``str``):
                 The path to uploading file on WebDAV server.
 
             local_path (``str``):
                 The path to local file for uploading.
 
+            overwrite (``bool``)
+                If true the will be overwriten by the new data if the a file with the same path exists. 
+                (Default to true)
+
             progress (``callable``, *optional*):
                 Pass a callback function to view the file transmission progress.
                 The function must take *(current, total)* as positional arguments (look at Other Parameters below for a
                 detailed description) and will be called back each time a new file chunk has been successfully
                 transmitted.
 
             progress_args (``tuple``, *optional*):
@@ -915,25 +985,32 @@
                 def progress(current, total):
                     print(f"{current * 100 / total:.1f}%")
 
                 await client.upload_file('/path/to/file.zip', 'file.zip', progress=progress)
                 ...
         """
 
-        async with aiofiles.open(local_path, 'rb') as file:
+        async with aiofiles.open(local_path, "rb") as file:
             size = os.path.getsize(local_path)
-            await self.upload_to(path=remote_path, buffer=file, buffer_size=size,
-                                 progress=progress, progress_args=progress_args)
+            await self.upload_to(
+                path=remote_path,
+                buffer=file,
+                buffer_size=size,
+                overwrite=overwrite,
+                progress=progress,
+                progress_args=progress_args,
+            )
 
     async def upload_directory(
         self,
         remote_path: Union[str, "os.PathLike[str]"],
         local_path: Union[str, "os.PathLike[str]"],
+        overwrite: bool = True,
         progress: Optional[Callable[[int, int, Tuple], None]] = None,
-        progress_args: Optional[Tuple] = ()
+        progress_args: Optional[Tuple] = (),
     ) -> None:
         """
         Uploads directory to remote path on WebDAV server. In case directory is exist
         on remote server it will delete it and then upload directory with nested files
         and directories.
         More information you can find by link http://webdav.org/specs/rfc4918.html#METHOD_PUT
 
@@ -942,14 +1019,18 @@
         Parameters:
             remote_path (``str``):
                 The path to directory for uploading on WebDAV server.
 
             local_path (``str``):
                 The path to local directory for uploading.
 
+            overwrite (``bool``)
+                If true the will be overwriten by the new data if the directory with the same path exists. 
+                (Default to true)
+
             progress (``callable``, *optional*):
                 Pass a callback function to view the file transmission progress.
                 The function must take *(current, total)* as positional arguments (look at Other Parameters below for a
                 detailed description) and will be called back each time a new file chunk has been successfully
                 transmitted.
 
             progress_args (``tuple``, *optional*):
@@ -975,29 +1056,37 @@
         if not os.path.isdir(local_path):
             raise OptionNotValid(name="local_path", value=local_path)
 
         if not os.path.exists(local_path):
             raise LocalResourceNotFound(local_path)
 
         if (await self.exists(urn.path())):
-            await self.unlink(urn.path())
+            if overwrite:
+                await self.unlink(urn.path())
+            else:
+                return
 
         await self.create_directory(remote_path)
 
         for resource_name in os.listdir(local_path):
-            _remote_path = f"{urn.path()}{resource_name}".replace('\\', '')
+            _remote_path = f"{urn.path()}{resource_name}".replace("\\", "")
             _local_path = os.path.join(local_path, resource_name)
-            await self.upload(local_path=_local_path, remote_path=_remote_path, progress=progress, progress_args=progress_args)
+            await self.upload(
+                local_path=_local_path,
+                remote_path=_remote_path,
+                progress=progress,
+                progress_args=progress_args,
+            )
 
     async def upload(
         self,
         remote_path: Union[str, "os.PathLike[str]"],
         local_path: Union[str, "os.PathLike[str]"],
         progress: Optional[Callable[[int, int, Tuple], None]] = None,
-        progress_args: Optional[Tuple] = ()
+        progress_args: Optional[Tuple] = (),
     ) -> None:
         """
         Uploads resource to remote path on WebDAV server.
         In case resource is directory it will upload all nested files and directories.
         More information you can find by link http://webdav.org/specs/rfc4918.html#METHOD_PUT
 
         WARNING: DESTRUCTIVE METHOD
@@ -1028,22 +1117,30 @@
 
             *args (``tuple``, *optional*):
                 Extra custom arguments as defined in the ``progress_args`` parameter.
                 You can either keep ``*args`` or add every single extra argument in your function signature.
         """
 
         if os.path.isdir(local_path):
-            self.upload_directory(local_path=local_path, remote_path=remote_path, progress=progress, progress_args=progress_args)
+            self.upload_directory(
+                local_path=local_path,
+                remote_path=remote_path,
+                progress=progress,
+                progress_args=progress_args,
+            )
         else:
-            self.upload_file(local_path=local_path, remote_path=remote_path, progress=progress, progress_args=progress_args)
+            self.upload_file(
+                local_path=local_path,
+                remote_path=remote_path,
+                progress=progress,
+                progress_args=progress_args,
+            )
 
     async def get_property(
-        self,
-        path: Union[str, "os.PathLike[str]"],
-        option: Dict[str, str]
+        self, path: Union[str, "os.PathLike[str]"], option: Dict[str, str]
     ) -> Union[str, None]:
         """
         Gets metadata property of remote resource on WebDAV server.
         More information you can find by link http://webdav.org/specs/rfc4918.html#METHOD_PROPFIND
 
         Parameters:
             path (``str``):
@@ -1058,22 +1155,22 @@
         """
 
         urn = Urn(path)
         if not (await self.exists(urn.path())):
             raise RemoteResourceNotFound(urn.path())
 
         data = WebDavXmlUtils.create_get_property_request_content(option)
-        response = await self._execute_request(action='get_property', path=urn.quote(), data=data)
+        response = await self._execute_request(
+            action="get_property", path=urn.quote(), data=data
+        )
         text = await response.text()
-        return WebDavXmlUtils.parse_get_property_response(text, option['name'])
+        return WebDavXmlUtils.parse_get_property_response(text, option["name"])
 
     async def set_property(
-        self,
-        path: Union[str, "os.PathLike[str]"],
-        option: Dict[str, str]
+        self, path: Union[str, "os.PathLike[str]"], option: Dict[str, str]
     ) -> None:
         """
         Sets metadata property of remote resource on WebDAV server.
         More information you can find by link http://webdav.org/specs/rfc4918.html#METHOD_PROPPATCH
 
         Parameters:
             path (``str``):
@@ -1086,28 +1183,25 @@
         """
 
         urn = Urn(path)
         if not (await self.check(urn.path())):
             raise RemoteResourceNotFound(urn.path())
 
         data = WebDavXmlUtils.create_set_property_batch_request_content(option)
-        await self._execute_request(action='set_property', path=urn.quote(), data=data)
+        await self._execute_request(action="set_property", path=urn.quote(), data=data)
 
     async def close(self):
         """
         Close underlying http session.
         Release all acquired resources.
         """
 
         await self.session.close()
 
-    def resource(
-        self,
-        path: Union[str, "os.PathLike[str]"]
-    ) -> "Resource":
+    def resource(self, path: Union[str, "os.PathLike[str]"]) -> "Resource":
         """
         Get associated resource from path
 
         Parameters:
             path (``str``):
                 Path to remote directory.
 
@@ -1120,19 +1214,15 @@
 
 
 class Resource(object):
     """
     Remote resource.
     """
 
-    def __init__(
-        self,
-        client: Client,
-        urn: Urn
-    ) -> None:
+    def __init__(self, client: Client, urn: Urn) -> None:
         self.client = client
         self.urn = urn
 
     def __str__(self) -> str:
         return f"resource {self.urn.path()}"
 
     async def is_directory(self) -> bool:
@@ -1140,18 +1230,15 @@
         Determine if the resource is a directory.
 
         Returns:
             :obj:`bool`: True if the resource is a directory or False else.
         """
         return await self.client.is_directory(self.urn.path())
 
-    async def rename(
-        self,
-        name: str
-    ) -> None:
+    async def rename(self, name: str) -> None:
         """
         Rename the resource.
 
         Parameters:
             name (``str``):
                 New name to resource.
         """
@@ -1159,51 +1246,42 @@
         parent_path = self.urn.parent()
         name = Urn(name).filename()
         new_path = f"{parent_path}{name}"
 
         await self.client.move(source=old_path, destination=new_path)
         self.urn = Urn(new_path)
 
-    async def move(
-        self,
-        path: Union[str, "os.PathLike[str]"]
-    ) -> None:
+    async def move(self, path: Union[str, "os.PathLike[str]"]) -> None:
         """
         Move the resource to new path.
 
         Parameters:
             path (``str``):
                 New path of the resource.
         """
         new_urn = Urn(path)
         await self.client.move(source=self.urn.path(), destination=new_urn.path())
         self.urn = new_urn
 
-    async def copy(
-        self,
-        path: Union[str, "os.PathLike[str]"]
-    ) -> "Resource":
+    async def copy(self, path: Union[str, "os.PathLike[str]"]) -> "Resource":
         """
         Copy the resource to a another path.
 
         Parameters:
             path (``str``):
                 The path where resource will be copied.
 
         Returns:
             :obj:`Resource`: The value of property or None if property is not found.
         """
         urn = Urn(path)
         await self.client.copy(source=self.urn.path(), destination=path)
         return Resource(self.client, urn)
 
-    async def info(
-        self,
-        filter: Optional[Iterable[str]] = None
-    ) -> Dict[str, str]:
+    async def info(self, filter: Optional[Iterable[str]] = None) -> Dict[str, str]:
         """
         Get a dictionary with resource information.
 
         Parameters:
             filter (``Iterable[str]``, *optional*):
                 If filter is not `None` then only return properties
                 contained in filter iterable.
```

### Comparing `aiodav-0.1.8/aiodav/exceptions.py` & `aiodav-0.1.9/aiodav/exceptions.py`

 * *Files 18% similar despite different names*

```diff
@@ -9,16 +9,17 @@
 class OptionNotValid(NotValid):
     def __init__(self, name, value, ns=""):
         self.name = name
         self.value = value
         self.ns = ns
 
     def __str__(self):
-        return "Option ({ns}{name}={value}) have invalid name or value".format(ns=self.ns, name=self.name,
-                                                                               value=self.value)
+        return "Option ({ns}{name}={value}) have invalid name or value".format(
+            ns=self.ns, name=self.name, value=self.value
+        )
 
 
 class CertificateNotValid(NotValid):
     pass
 
 
 class NotFound(WebDavException):
@@ -51,15 +52,17 @@
 
 class MethodNotSupported(WebDavException):
     def __init__(self, name, server):
         self.name = name
         self.server = server
 
     def __str__(self):
-        return "Method '{name}' not supported for {server}".format(name=self.name, server=self.server)
+        return "Method '{name}' not supported for {server}".format(
+            name=self.name, server=self.server
+        )
 
 
 class ConnectionException(WebDavException):
     def __init__(self, exception):
         self.exception = exception
 
     def __str__(self):
@@ -86,17 +89,18 @@
 class ResponseErrorCode(WebDavException):
     def __init__(self, url, code, message):
         self.url = url
         self.code = code
         self.message = message
 
     def __str__(self):
-        return "Request to {url} failed with code {code} and message: {message}".format(url=self.url, code=self.code,
-                                                                                        message=self.message)
+        return "Request to {url} failed with code {code} and message: {message}".format(
+            url=self.url, code=self.code, message=self.message
+        )
 
 
 class NotEnoughSpace(WebDavException):
     def __init__(self):
         self.message = "Not enough space on the server"
 
     def __str__(self):
-        return self.message
+        return self.message
```

### Comparing `aiodav-0.1.8/aiodav/urn.py` & `aiodav-0.1.9/aiodav/urn.py`

 * *Files 10% similar despite different names*

```diff
@@ -9,55 +9,55 @@
     def __init__(self, path: str, directory: Optional[bool] = False) -> None:
         self._path = quote(path)
         expressions = "/\.+/", "/+"
         for expression in expressions:
             self._path = sub(expression, Urn.separate, self._path)
 
         if not self._path.startswith(Urn.separate):
-            self._path = "{begin}{end}".format(
-                begin=Urn.separate, end=self._path)
+            self._path = "{begin}{end}".format(begin=Urn.separate, end=self._path)
 
         if directory and not self._path.endswith(Urn.separate):
-            self._path = "{begin}{end}".format(
-                begin=self._path, end=Urn.separate)
+            self._path = "{begin}{end}".format(begin=self._path, end=Urn.separate)
 
     def __str__(self) -> str:
         return self.path()
 
     def path(self) -> str:
         return unquote(self._path)
 
     def quote(self) -> str:
         return self._path
 
     def filename(self) -> str:
         path_split = self._path.split(Urn.separate)
-        name = path_split[-2] + \
-            Urn.separate if path_split[-1] == '' else path_split[-1]
+        name = path_split[-2] + Urn.separate if path_split[-1] == "" else path_split[-1]
         return unquote(name)
 
     def parent(self) -> str:
         path_split = self._path.split(Urn.separate)
         nesting_level = self.nesting_level()
         parent_path_split = path_split[:nesting_level]
-        parent = self.separate.join(
-            parent_path_split) if nesting_level != 1 else Urn.separate
+        parent = (
+            self.separate.join(parent_path_split)
+            if nesting_level != 1
+            else Urn.separate
+        )
         if not parent.endswith(Urn.separate):
             return unquote(parent + Urn.separate)
         else:
             return unquote(parent)
 
     def nesting_level(self) -> int:
         return self._path.count(Urn.separate, 0, -1)
 
     def is_dir(self) -> bool:
         return self._path[-1] == Urn.separate
 
     @staticmethod
     def normalize_path(path: str) -> str:
-        result = sub('/{2,}', '/', path)
+        result = sub("/{2,}", "/", path)
         return result if len(result) < 1 or result[-1] != Urn.separate else result[:-1]
 
     @staticmethod
     def compare_path(path_a: str, href: str) -> bool:
         unqouted_path = Urn.separate + unquote(urlsplit(href).path)
         return Urn.normalize_path(path_a) == Urn.normalize_path(unqouted_path)
```

### Comparing `aiodav-0.1.8/aiodav/utils.py` & `aiodav-0.1.9/aiodav/utils.py`

 * *Files 2% similar despite different names*

```diff
@@ -2,14 +2,15 @@
 from aiodav.exceptions import *
 from aiodav.urn import Urn
 
 import lxml.etree as etree
 from urllib.parse import unquote, urlsplit, urlparse
 from io import BytesIO
 
+
 class WebDavXmlUtils:
     def __init__(self) -> None:
         pass
 
     @staticmethod
     def parse_get_list_info_response(content):
         """
@@ -32,16 +33,16 @@
                 href_el = next(iter(response.findall(".//{DAV:}href")), None)
                 if href_el is None:
                     continue
                 path = unquote(urlsplit(href_el.text).path)
                 info = dict()
                 is_dir = len(response.findall(".//{DAV:}collection")) > 0
                 info = WebDavXmlUtils.get_info_from_response(response)
-                info['isdir'] = is_dir
-                info['path'] = path
+                info["isdir"] = is_dir
+                info["path"] = path
                 infos.append(info)
             return infos
         except etree.XMLSyntaxError:
             return list()
 
     @staticmethod
     def parse_get_list_response(content):
@@ -83,42 +84,42 @@
 
         :param content: the XML content of HTTP response from WebDAV server for getting free space.
         :param hostname: the server hostname.
         :return: an amount of free space in bytes.
         """
         try:
             tree = etree.fromstring(content.encode())
-            node = tree.find('.//{DAV:}quota-available-bytes')
+            node = tree.find(".//{DAV:}quota-available-bytes")
             if node is not None:
                 return int(node.text)
             else:
-                raise MethodNotSupported(name='free', server=hostname)
+                raise MethodNotSupported(name="free", server=hostname)
         except TypeError:
-            raise MethodNotSupported(name='free', server=hostname)
+            raise MethodNotSupported(name="free", server=hostname)
         except etree.XMLSyntaxError:
-            return -1 # TODO: replace
+            return -1  # TODO: replace
 
     @staticmethod
     def get_info_from_response(response):
-        """ Get information attributes from response
+        """Get information attributes from response
 
         :param response: XML object of response for the remote resource defined by path
         :return: a dictionary of information attributes and them values with following keys:
                  `created`: date of resource creation,
                  `name`: name of resource,
                  `size`: size of resource,
                  `modified`: date of resource modification,
                  `etag`: etag of resource
         """
         find_attributes = {
-            'created': ".//{DAV:}creationdate",
-            'name': ".//{DAV:}displayname",
-            'size': ".//{DAV:}getcontentlength",
-            'modified': ".//{DAV:}getlastmodified",
-            'etag': ".//{DAV:}getetag",
+            "created": ".//{DAV:}creationdate",
+            "name": ".//{DAV:}displayname",
+            "size": ".//{DAV:}getcontentlength",
+            "modified": ".//{DAV:}getlastmodified",
+            "etag": ".//{DAV:}getetag",
         }
         info = dict()
         for (name, value) in find_attributes.items():
             info[name] = response.findtext(value)
         return info
 
     @staticmethod
@@ -131,27 +132,31 @@
         :return: a dictionary of information attributes and them values with following keys:
                  `created`: date of resource creation,
                  `name`: name of resource,
                  `size`: size of resource,
                  `modified`: date of resource modification,
                  `etag`: etag of resource.
         """
-        response = WebDavXmlUtils.extract_response_for_path(content=content, path=path, hostname=hostname)
+        response = WebDavXmlUtils.extract_response_for_path(
+            content=content, path=path, hostname=hostname
+        )
         return WebDavXmlUtils.get_info_from_response(response)
 
     @staticmethod
     def parse_is_dir_response(content, path, hostname):
         """Parses of response content XML from WebDAV server and extract an information about resource.
 
         :param content: the XML content of HTTP response from WebDAV server.
         :param path: the path to resource.
         :param hostname: the server hostname.
         :return: True in case the remote resource is directory and False otherwise.
         """
-        response = WebDavXmlUtils.extract_response_for_path(content=content, path=path, hostname=hostname)
+        response = WebDavXmlUtils.extract_response_for_path(
+            content=content, path=path, hostname=hostname
+        )
         resource_type = response.find(".//{DAV:}resourcetype")
         if resource_type is None:
             raise MethodNotSupported(name="is_dir", server=hostname)
         dir_type = resource_type.find("{DAV:}collection")
 
         return True if dir_type is not None else False
 
@@ -162,57 +167,61 @@
         :param option: the property attributes as dictionary with following keys:
                        `namespace`: (optional) the namespace for XML property which will be get,
                        `name`: the name of property which will be get.
         :return: the XML string of request content.
         """
         root = etree.Element("propfind", xmlns="DAV:")
         prop = etree.SubElement(root, "prop")
-        etree.SubElement(prop, option.get('name', ""), xmlns=option.get('namespace', ""))
+        etree.SubElement(
+            prop, option.get("name", ""), xmlns=option.get("namespace", "")
+        )
         tree = etree.ElementTree(root)
         return WebDavXmlUtils.etree_to_string(tree)
 
     @staticmethod
     def parse_get_property_response(content, name):
         """Parses of response content XML from WebDAV server for getting metadata property value for some resource.
 
         :param content: the XML content of response as string.
         :param name: the name of property for finding a value in response
         :return: the value of property if it has been found or None otherwise.
         """
         tree = etree.fromstring(content.encode())
-        return tree.xpath('//*[local-name() = $name]', name=name)[0].text
+        return tree.xpath("//*[local-name() = $name]", name=name)[0].text
 
     @staticmethod
     def create_set_property_batch_request_content(options):
         """Creates an XML for requesting of setting a property values for remote WebDAV resource in batch.
 
         :param options: the property attributes as list of dictionaries with following keys:
                        `namespace`: (optional) the namespace for XML property which will be set,
                        `name`: the name of property which will be set,
                        `value`: (optional) the value of property which will be set. Defaults is empty string.
         :return: the XML string of request content.
         """
-        root_node = etree.Element('propertyupdate', xmlns='DAV:')
-        set_node = etree.SubElement(root_node, 'set')
-        prop_node = etree.SubElement(set_node, 'prop')
+        root_node = etree.Element("propertyupdate", xmlns="DAV:")
+        set_node = etree.SubElement(root_node, "set")
+        prop_node = etree.SubElement(set_node, "prop")
         for option in options:
-            opt_node = etree.SubElement(prop_node, option['name'], xmlns=option.get('namespace', ''))
-            opt_node.text = option.get('value', '')
+            opt_node = etree.SubElement(
+                prop_node, option["name"], xmlns=option.get("namespace", "")
+            )
+            opt_node.text = option.get("value", "")
         tree = etree.ElementTree(root_node)
         return WebDavXmlUtils.etree_to_string(tree)
 
     @staticmethod
     def etree_to_string(tree):
         """Creates string from lxml.etree.ElementTree with XML declaration and UTF-8 encoding.
 
         :param tree: the instance of ElementTree
         :return: the string of XML.
         """
         buff = BytesIO()
-        tree.write(buff, xml_declaration=True, encoding='UTF-8')
+        tree.write(buff, xml_declaration=True, encoding="UTF-8")
         return buff.getvalue()
 
     @staticmethod
     def extract_response_for_path(content, path, hostname):
         """Extracts single response for specified remote resource.
 
         :param content: raw content of response as string.
@@ -227,13 +236,15 @@
             n_path = Urn.normalize_path(path)
 
             for resp in responses:
                 href = resp.findtext("{DAV:}href")
 
                 if Urn.compare_path(n_path, href) is True:
                     return resp
-                href_without_prefix = href[len(prefix):] if href.startswith(prefix) else href
+                href_without_prefix = (
+                    href[len(prefix) :] if href.startswith(prefix) else href
+                )
                 if Urn.compare_path(n_path, href_without_prefix) is True:
                     return resp
             raise RemoteResourceNotFound(path)
         except etree.XMLSyntaxError:
             raise MethodNotSupported(name="is_dir", server=hostname)
```

### Comparing `aiodav-0.1.8/aiodav.egg-info/PKG-INFO` & `aiodav-0.1.9/aiodav.egg-info/PKG-INFO`

 * *Files 6% similar despite different names*

```diff
@@ -1,17 +1,16 @@
 Metadata-Version: 2.1
 Name: aiodav
-Version: 0.1.8
+Version: 0.1.9
 Summary: A Python Async WebDAV Client
 Home-page: https://github.com/jorgeajimenezl/aiodav
 Author: Jorge Alejandro Jimenez Luna
 Author-email: jorgeajimenezl17@gmail.com
 License: MIT License
 Keywords: webdav,client,files,internet,download,upload
-Platform: UNKNOWN
 Classifier: Intended Audience :: Developers
 Classifier: License :: OSI Approved :: MIT License
 Classifier: Operating System :: OS Independent
 Classifier: Programming Language :: Python
 Classifier: Programming Language :: Python :: 3.5
 Classifier: Programming Language :: Python :: 3.6
 Classifier: Programming Language :: Python :: 3.7
@@ -20,14 +19,15 @@
 Description-Content-Type: text/markdown
 License-File: LICENSE
 
 # Python Async WebDAV Client
 [![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=jorgeajimenezl_aiodav&metric=alert_status)](https://sonarcloud.io/dashboard?id=jorgeajimenezl_aiodav)
 [![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=jorgeajimenezl_aiodav&metric=sqale_rating)](https://sonarcloud.io/dashboard?id=jorgeajimenezl_aiodav)
 ![PyPI](https://img.shields.io/pypi/v/aiodav)
+![Downloads](https://img.shields.io/pypi/dm/aiodav)
 ![PyPI - Python Version](https://img.shields.io/pypi/pyversions/aiodav)
 
 A asynchronous WebDAV client that use `asyncio` 
 
 > Based on [webdavclient3](https://github.com/ezhov-evgeny/webdav-client-python-3)
 
 ## Installation
@@ -61,9 +61,7 @@
                                     progress=progress)
 
 asyncio.run(main())
 ```
 
 ## License
 [MIT License](./LICENSE)
-
-
```

### Comparing `aiodav-0.1.8/setup.py` & `aiodav-0.1.9/setup.py`

 * *Files 19% similar despite different names*

```diff
@@ -1,24 +1,25 @@
 import re
 from setuptools import setup, find_packages
 
-with open('aiodav/__init__.py', 'r') as fd:
-    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]',
-                        fd.read(), re.MULTILINE).group(1)
-                        
-with open('requirements.txt', 'r') as file:                        
+with open("aiodav/__init__.py", "r") as fd:
+    version = re.search(
+        r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', fd.read(), re.MULTILINE
+    ).group(1)
+
+with open("requirements.txt", "r") as file:
     INSTALL_REQUIRES = file.readlines()
 
-with open('README.md') as readme:
+with open("README.md") as readme:
     setup(
-        name='aiodav',
+        name="aiodav",
         version=version,
         description="A Python Async WebDAV Client",
         long_description=readme.read(),
-        long_description_content_type='text/markdown',
+        long_description_content_type="text/markdown",
         license="MIT License",
         author="Jorge Alejandro Jimenez Luna",
         author_email="jorgeajimenezl17@gmail.com",
         url="https://github.com/jorgeajimenezl/aiodav",
         classifiers=[
             "Intended Audience :: Developers",
             "License :: OSI Approved :: MIT License",
@@ -29,8 +30,8 @@
             "Programming Language :: Python :: 3.7",
             "Programming Language :: Python :: 3.8",
             "Programming Language :: Python :: 3.9",
         ],
         keywords="webdav, client, files, internet, download, upload",
         install_requires=INSTALL_REQUIRES,
         packages=find_packages(),
-    )
+    )
```

