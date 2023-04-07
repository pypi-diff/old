# Comparing `tmp/metablock-0.5.1.tar.gz` & `tmp/metablock-0.5.2.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "metablock-0.5.1.tar", max compression
+gzip compressed data, was "metablock-0.5.2.tar", max compression
```

## Comparing `metablock-0.5.1.tar` & `metablock-0.5.2.tar`

### file list

```diff
@@ -1,13 +1,12 @@
--rw-r--r--   0        0        0     1482 2022-12-20 21:17:05.892180 metablock-0.5.1/LICENSE
--rw-r--r--   0        0        0      502 2022-12-20 21:17:05.892180 metablock-0.5.1/metablock/__init__.py
--rw-r--r--   0        0        0     4118 2022-12-20 21:17:05.892180 metablock-0.5.1/metablock/client.py
--rw-r--r--   0        0        0     7868 2022-12-20 21:17:05.892180 metablock-0.5.1/metablock/components.py
--rw-r--r--   0        0        0      540 2022-12-20 21:17:05.892180 metablock-0.5.1/metablock/extensions.py
--rw-r--r--   0        0        0     1850 2022-12-20 21:17:05.892180 metablock-0.5.1/metablock/orgs.py
--rw-r--r--   0        0        0     3029 2022-12-20 21:17:05.892180 metablock-0.5.1/metablock/spaces.py
--rw-r--r--   0        0        0     1350 2022-12-20 21:17:05.892180 metablock-0.5.1/metablock/user.py
--rw-r--r--   0        0        0      531 2022-12-20 21:17:05.892180 metablock-0.5.1/metablock/utils.py
--rw-r--r--   0        0        0      586 2022-12-20 21:17:05.896180 metablock-0.5.1/pyproject.toml
--rw-r--r--   0        0        0     1010 2022-12-20 21:17:05.896180 metablock-0.5.1/readme.md
--rw-r--r--   0        0        0     1655 1970-01-01 00:00:00.000000 metablock-0.5.1/setup.py
--rw-r--r--   0        0        0     1472 1970-01-01 00:00:00.000000 metablock-0.5.1/PKG-INFO
+-rw-r--r--   0        0        0     1482 2023-04-07 10:33:56.321380 metablock-0.5.2/LICENSE
+-rw-r--r--   0        0        0      502 2023-04-07 10:33:56.321380 metablock-0.5.2/metablock/__init__.py
+-rw-r--r--   0        0        0     4119 2023-04-07 10:33:56.321380 metablock-0.5.2/metablock/client.py
+-rw-r--r--   0        0        0     7937 2023-04-07 10:33:56.321380 metablock-0.5.2/metablock/components.py
+-rw-r--r--   0        0        0      540 2023-04-07 10:33:56.321380 metablock-0.5.2/metablock/extensions.py
+-rw-r--r--   0        0        0     1850 2023-04-07 10:33:56.325380 metablock-0.5.2/metablock/orgs.py
+-rw-r--r--   0        0        0     3029 2023-04-07 10:33:56.325380 metablock-0.5.2/metablock/spaces.py
+-rw-r--r--   0        0        0     1350 2023-04-07 10:33:56.325380 metablock-0.5.2/metablock/user.py
+-rw-r--r--   0        0        0      531 2023-04-07 10:33:56.325380 metablock-0.5.2/metablock/utils.py
+-rw-r--r--   0        0        0      584 2023-04-07 10:33:56.325380 metablock-0.5.2/pyproject.toml
+-rw-r--r--   0        0        0     1010 2023-04-07 10:33:56.325380 metablock-0.5.2/readme.md
+-rw-r--r--   0        0        0     1472 1970-01-01 00:00:00.000000 metablock-0.5.2/PKG-INFO
```

### Comparing `metablock-0.5.1/LICENSE` & `metablock-0.5.2/LICENSE`

 * *Files identical despite different names*

### Comparing `metablock-0.5.1/metablock/client.py` & `metablock-0.5.2/metablock/client.py`

 * *Files 6% similar despite different names*

```diff
@@ -96,21 +96,21 @@
             except Exception:
                 data = await response.text()
             raise MetablockResponseError(response, data)
         response.raise_for_status()
         data = await response.json()
         return wrap(data) if wrap else data
 
-    async def get_user(self, callback: Callback | None = None) -> dict:
+    async def get_user(self, callback: Callback | None = None) -> User:
         return await self.get(f"{self.url}/user", callback=callback, wrap=self._user)
 
-    async def get_space(self, callback: Callback | None = None) -> dict:
+    async def get_space(self, callback: Callback | None = None) -> Space:
         return await self.get(f"{self.url}/space", callback=callback, wrap=self._space)
 
-    async def update_user(self, callback: Callback | None = None, **data: Any) -> dict:
+    async def update_user(self, callback: Callback | None = None, **data: Any) -> User:
         return await self.patch(
             f"{self.url}/user", json=data, callback=callback, wrap=self._user
         )
 
     async def delete_user(self, callback: Callback | None = None) -> None:
         return await self.delete(f"{self.url}/user", callback=callback)
```

### Comparing `metablock-0.5.1/metablock/components.py` & `metablock-0.5.2/metablock/components.py`

 * *Files 0% similar despite different names*

```diff
@@ -87,14 +87,17 @@
 
     def __contains__(self, item: str) -> bool:
         return item in self.data
 
     def __eq__(self, other: Any) -> bool:
         return isinstance(other, self.__class__) and self.data == other.data
 
+    def _asdict(self) -> dict:
+        return self.data
+
     @property
     def cli(self) -> Metablock:
         return self.root.cli
 
     @property
     def id(self) -> str:
         return self.data.get("id", "")
@@ -181,19 +184,19 @@
             if not next_.startswith(url):
                 next_ = f'{url}?{next_.split("?")[1]}'
             data = await self.execute(next_, params=url_params)
             next_ = data.get("next")
             for d in data["data"]:
                 yield self.wrap(d)
 
-    def get_list(self, **params: Any) -> list[MetablockEntity]:
+    async def get_list(self, **params: Any) -> list[MetablockEntity]:
         url = self.list_create_url()
         return cast(
             list[MetablockEntity],
-            self.execute(url, params=as_params(**params), wrap=self.wrap_list),
+            await self.execute(url, params=as_params(**params), wrap=self.wrap_list),
         )
 
     async def get_full_list(self, **params: Any) -> list[MetablockEntity]:
         return [d async for d in self.paginate(**params)]
 
     async def get(self, id_: str, **kwargs: Any) -> MetablockEntity:  # type: ignore
         url = f"{self.url}/{id_}"
```

### Comparing `metablock-0.5.1/metablock/extensions.py` & `metablock-0.5.2/metablock/extensions.py`

 * *Files identical despite different names*

### Comparing `metablock-0.5.1/metablock/orgs.py` & `metablock-0.5.2/metablock/orgs.py`

 * *Files identical despite different names*

### Comparing `metablock-0.5.1/metablock/spaces.py` & `metablock-0.5.2/metablock/spaces.py`

 * *Files identical despite different names*

### Comparing `metablock-0.5.1/metablock/user.py` & `metablock-0.5.2/metablock/user.py`

 * *Files identical despite different names*

### Comparing `metablock-0.5.1/metablock/utils.py` & `metablock-0.5.2/metablock/utils.py`

 * *Files identical despite different names*

### Comparing `metablock-0.5.1/pyproject.toml` & `metablock-0.5.2/pyproject.toml`

 * *Files 26% similar despite different names*

```diff
@@ -1,27 +1,27 @@
 [tool.poetry]
 name = "metablock"
-version = "0.5.1"
+version = "0.5.2"
 description = "Metablock cloud python client"
 authors = ["Luca <luca@quantmind.com>"]
 license = "BSD"
 readme = "readme.md"
 
 [tool.poetry.dependencies]
 python = ">=3.10,<3.12"
 aiohttp = "^3.8.3"
 
 [tool.poetry.group.dev.dependencies]
-pytest-asyncio = "^0.20.3"
+pytest-asyncio = "^0.21.0"
 pytest = "^7.0.1"
 pytest-cov = "^4.0.0"
-mypy = "^0.991"
-black = "^22.12.0"
+mypy = "^1.2.0"
+black = "^23.3.0"
 isort = "^5.11.3"
 flake8 = "^6.0.0"
 flake8-builtins = "^2.0.1"
 codecov = "^2.1.12"
-python-dotenv = "^0.21.0"
+python-dotenv = "^1.0.0"
 
 [build-system]
 requires = ["poetry-core>=1.0.0"]
 build-backend = "poetry.core.masonry.api"
```

### Comparing `metablock-0.5.1/readme.md` & `metablock-0.5.2/readme.md`

 * *Files identical despite different names*

### Comparing `metablock-0.5.1/setup.py` & `metablock-0.5.2/PKG-INFO`

 * *Files 26% similar despite different names*

```diff
@@ -1,30 +1,47 @@
-# -*- coding: utf-8 -*-
-from setuptools import setup
+Metadata-Version: 2.1
+Name: metablock
+Version: 0.5.2
+Summary: Metablock cloud python client
+License: BSD
+Author: Luca
+Author-email: luca@quantmind.com
+Requires-Python: >=3.10,<3.12
+Classifier: License :: Other/Proprietary License
+Classifier: Programming Language :: Python :: 3
+Classifier: Programming Language :: Python :: 3.10
+Classifier: Programming Language :: Python :: 3.11
+Requires-Dist: aiohttp (>=3.8.3,<4.0.0)
+Description-Content-Type: text/markdown
 
-packages = \
-['metablock']
+# A Python Client for Metablock API
 
-package_data = \
-{'': ['*']}
+[![PyPI version](https://badge.fury.io/py/metablock.svg)](https://badge.fury.io/py/metablock)
+[![Python versions](https://img.shields.io/pypi/pyversions/metablock.svg)](https://pypi.org/project/metablock)
+[![Build](https://github.com/quantmind/metablock-py/workflows/build/badge.svg)](https://github.com/quantmind/metablock-py/actions?query=workflow%3Abuild)
+[![codecov](https://codecov.io/gh/quantmind/metablock-py/branch/master/graph/badge.svg?token=EAdSVpD0Af)](https://codecov.io/gh/quantmind/metablock-py)
 
-install_requires = \
-['aiohttp>=3.8.3,<4.0.0']
-
-setup_kwargs = {
-    'name': 'metablock',
-    'version': '0.5.1',
-    'description': 'Metablock cloud python client',
-    'long_description': '# A Python Client for Metablock API\n\n[![PyPI version](https://badge.fury.io/py/metablock.svg)](https://badge.fury.io/py/metablock)\n[![Python versions](https://img.shields.io/pypi/pyversions/metablock.svg)](https://pypi.org/project/metablock)\n[![Build](https://github.com/quantmind/metablock-py/workflows/build/badge.svg)](https://github.com/quantmind/metablock-py/actions?query=workflow%3Abuild)\n[![codecov](https://codecov.io/gh/quantmind/metablock-py/branch/master/graph/badge.svg?token=EAdSVpD0Af)](https://codecov.io/gh/quantmind/metablock-py)\n\nThis is an asynchronous python client for [metablock API](https://api.metablock.io/v1/docs).\n\n## Installation\n\nThis is a simple python package you can install via pip:\n\n```\npip install metablock\n```\n\n## Usage\n\nCreate the client\n\n```python\nfrom metablock import Metablock\n\ncli = Metablock()\n\n# get the user associated with the API token\nuser = await cli.get_user()\n```\n\nFor the authentication token you can create the `METABLOCK_API_TOKEN` environment variable.\n',
-    'author': 'Luca',
-    'author_email': 'luca@quantmind.com',
-    'maintainer': 'None',
-    'maintainer_email': 'None',
-    'url': 'None',
-    'packages': packages,
-    'package_data': package_data,
-    'install_requires': install_requires,
-    'python_requires': '>=3.10,<3.12',
-}
+This is an asynchronous python client for [metablock API](https://api.metablock.io/v1/docs).
 
+## Installation
+
+This is a simple python package you can install via pip:
+
+```
+pip install metablock
+```
+
+## Usage
+
+Create the client
+
+```python
+from metablock import Metablock
+
+cli = Metablock()
+
+# get the user associated with the API token
+user = await cli.get_user()
+```
+
+For the authentication token you can create the `METABLOCK_API_TOKEN` environment variable.
 
-setup(**setup_kwargs)
```

