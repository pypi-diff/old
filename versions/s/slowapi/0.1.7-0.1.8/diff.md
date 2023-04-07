# Comparing `tmp/slowapi-0.1.7.tar.gz` & `tmp/slowapi-0.1.8.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "slowapi-0.1.7.tar", max compression
+gzip compressed data, was "slowapi-0.1.8.tar", max compression
```

## Comparing `slowapi-0.1.7.tar` & `slowapi-0.1.8.tar`

### file list

```diff
@@ -1,12 +1,11 @@
--rw-r--r--   0        0        0     1072 2020-02-21 13:51:03.718094 slowapi-0.1.7/LICENSE
--rw-r--r--   0        0        0     1895 2022-11-28 10:17:47.053920 slowapi-0.1.7/README.md
--rw-r--r--   0        0        0     1131 2022-11-28 10:17:47.057920 slowapi-0.1.7/pyproject.toml
--rw-r--r--   0        0        0      116 2022-08-24 09:47:19.690232 slowapi-0.1.7/slowapi/__init__.py
--rw-r--r--   0        0        0      657 2020-02-21 13:50:26.017751 slowapi-0.1.7/slowapi/errors.py
--rw-r--r--   0        0        0    35086 2022-11-09 10:09:44.260872 slowapi-0.1.7/slowapi/extension.py
--rw-r--r--   0        0        0     7378 2022-11-09 10:09:44.260872 slowapi-0.1.7/slowapi/middleware.py
--rw-r--r--   0        0        0        0 2020-02-21 16:41:43.847052 slowapi-0.1.7/slowapi/py.typed
--rw-r--r--   0        0        0      700 2021-08-30 23:57:55.045524 slowapi-0.1.7/slowapi/util.py
--rw-r--r--   0        0        0     3870 2022-11-09 10:09:44.260872 slowapi-0.1.7/slowapi/wrappers.py
--rw-r--r--   0        0        0     2631 1970-01-01 00:00:00.000000 slowapi-0.1.7/setup.py
--rw-r--r--   0        0        0     2731 1970-01-01 00:00:00.000000 slowapi-0.1.7/PKG-INFO
+-rw-r--r--   0        0        0     1072 2020-02-21 13:51:03.718094 slowapi-0.1.8/LICENSE
+-rw-r--r--   0        0        0     2059 2023-03-30 09:40:52.975484 slowapi-0.1.8/README.md
+-rw-r--r--   0        0        0     1190 2023-04-07 14:11:37.251778 slowapi-0.1.8/pyproject.toml
+-rw-r--r--   0        0        0      116 2022-08-24 09:47:19.690232 slowapi-0.1.8/slowapi/__init__.py
+-rw-r--r--   0        0        0      657 2020-02-21 13:50:26.017751 slowapi-0.1.8/slowapi/errors.py
+-rw-r--r--   0        0        0    35047 2023-03-30 09:40:52.979484 slowapi-0.1.8/slowapi/extension.py
+-rw-r--r--   0        0        0     7378 2023-03-30 09:40:52.979484 slowapi-0.1.8/slowapi/middleware.py
+-rw-r--r--   0        0        0        0 2020-02-21 16:41:43.847052 slowapi-0.1.8/slowapi/py.typed
+-rw-r--r--   0        0        0      842 2023-03-30 09:40:52.979484 slowapi-0.1.8/slowapi/util.py
+-rw-r--r--   0        0        0     3870 2023-03-30 09:40:52.979484 slowapi-0.1.8/slowapi/wrappers.py
+-rw-r--r--   0        0        0     2947 1970-01-01 00:00:00.000000 slowapi-0.1.8/PKG-INFO
```

### Comparing `slowapi-0.1.7/LICENSE` & `slowapi-0.1.8/LICENSE`

 * *Files identical despite different names*

### Comparing `slowapi-0.1.7/README.md` & `slowapi-0.1.8/README.md`

 * *Files 13% similar despite different names*

```diff
@@ -1,12 +1,13 @@
 # SlowApi
 
 A rate limiting library for Starlette and FastAPI adapted from [flask-limiter](http://github.com/alisaifee/flask-limiter).
 
-Note: this is alpha quality code still, the API may change, and things may fall apart while you try it.
+This package is used in various production setups, handling millions of requests per month, and seems to behave as expected.
+There might be some API changes when changing the code to be fully `async`, but we will notify users via appropriate `semver` version changes.
 
 The documentation is on [read the docs](https://slowapi.readthedocs.io/en/latest/).
 
 # Quick start
 
 ## Installation
```

### Comparing `slowapi-0.1.7/pyproject.toml` & `slowapi-0.1.8/pyproject.toml`

 * *Files 6% similar despite different names*

```diff
@@ -1,43 +1,45 @@
 [tool.poetry]
 name = "slowapi"
-version = "0.1.7"
+version = "0.1.8"
 description = "A rate limiting extension for Starlette and Fastapi"
 authors = ["Laurent Savaete <laurent@where.tf>"]
 license = "MIT"
 
 readme = "README.md"
 
 repository = "https://github.com/laurents/slowapi"
 homepage = "https://github.com/laurents/slowapi"
 documentation = "https://slowapi.readthedocs.io/en/latest/"
 
 include = ["slowapi/py.typed"]
 
 [tool.poetry.dependencies]
 python = ">=3.7,<4.0"
-limits = "^2.3"
+limits = ">=2.3"
+redis = {version = "^3.4.1", optional = true}
 
 [tool.poetry.dev-dependencies]
 isort = "^4.3.21"
 mypy = "^0.910"
-black = "^22.3.0"
-fastapi = "^0.61.0"
+black = "^23.0.0"
+fastapi = "^0.89.0"
 lxml = "^4.9.1"
-starlette = "^0.13.6"
+starlette = "^0.22.0"
 mock = "^4.0.1"
 hiro = "^0.5.1"
 requests = "^2.22.0"
 pytest = "~=6.2.5"
 mkdocs = "^1.2.3"
 mkautodoc = "^0.1.0"
 types-redis = "^3.5.6"
 coverage = "^6.3"
 flake8 = "^4.0.1"
 setuptools = "^65.5.0"
+httpx = "^0.23.3"
 
 [tool.black]
 line-length = 88
 
 [tool.isort]
 multi_line_output = 3
 include_trailing_comma = true
@@ -47,8 +49,8 @@
 line_length = 88
 
 [build-system]
 requires = ["poetry-core>=1.0.0"]
 build-backend = "poetry.core.masonry.api"
 
 [tool.poetry.extras]
-redis = ["redis^3.4.1"]
+redis = ["redis"]
```

### Comparing `slowapi-0.1.7/slowapi/errors.py` & `slowapi-0.1.8/slowapi/errors.py`

 * *Files identical despite different names*

### Comparing `slowapi-0.1.7/slowapi/extension.py` & `slowapi-0.1.8/slowapi/extension.py`

 * *Files 2% similar despite different names*

```diff
@@ -19,18 +19,16 @@
     Set,
     Tuple,
     TypeVar,
     Union,
 )
 
 from limits import RateLimitItem  # type: ignore
-from limits.aio.storage import Storage as AsyncStorage  # type: ignore
 from limits.errors import ConfigurationError  # type: ignore
 from limits.storage import MemoryStorage, storage_from_string  # type: ignore
-from limits.storage import Storage  # type: ignore
 from limits.strategies import STRATEGIES, RateLimiter  # type: ignore
 from starlette.config import Config
 from starlette.datastructures import MutableHeaders
 from starlette.requests import Request
 from starlette.responses import JSONResponse, Response
 from typing_extensions import Literal
 
@@ -233,15 +231,15 @@
         self._swallow_errors = self.get_app_config(
             C.SWALLOW_ERRORS, self._swallow_errors
         )
         self._headers_enabled = self._headers_enabled or self.get_app_config(
             C.HEADERS_ENABLED, False
         )
         self._storage_options.update(self.get_app_config(C.STORAGE_OPTIONS, {}))
-        self._storage: Union[Storage, AsyncStorage] = storage_from_string(
+        self._storage = storage_from_string(
             self._storage_uri or self.get_app_config(C.STORAGE_URL, "memory://"),
             **self._storage_options,
         )
         strategy = self._strategy or self.get_app_config(C.STRATEGY, "fixed-window")
         if strategy not in STRATEGIES:
             raise ConfigurationError("Invalid rate limiting strategy %s" % strategy)
         self._limiter: RateLimiter = STRATEGIES[strategy](self._storage)
@@ -330,15 +328,19 @@
         app.state.limiter = self  # type: ignore
         app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)  # type: ignore
 
     def get_app_config(self, key: str, default_value: T = None) -> T:
         """
         Place holder until we find a better way to load config from app
         """
-        return self.app_config(key, default=default_value, cast=type(default_value))
+        return (
+            self.app_config(key, default=default_value, cast=type(default_value))
+            if default_value
+            else self.app_config(key, default=default_value)
+        )
 
     def __should_check_backend(self) -> bool:
         if self.__check_backend_count > MAX_BACKEND_CHECKS:
             self.__check_backend_count = 0
         if time.time() - self.__last_check_backend > pow(2, self.__check_backend_count):
             self.__last_check_backend = time.time()
             self.__check_backend_count += 1
@@ -647,15 +649,14 @@
         per_method: bool = False,
         methods: Optional[List[str]] = None,
         error_message: Optional[str] = None,
         exempt_when: Optional[Callable[..., bool]] = None,
         cost: Union[int, Callable[..., int]] = 1,
         override_defaults: bool = True,
     ) -> Callable[..., Any]:
-
         _scope = scope if shared else None
 
         def decorator(func: Callable[..., Response]):
             keyfunc = key_func or self._key_func
             name = f"{func.__module__}.{func.__name__}"
             dynamic_limit = None
             static_limits: List[Limit] = []
```

### Comparing `slowapi-0.1.7/slowapi/middleware.py` & `slowapi-0.1.8/slowapi/middleware.py`

 * *Files identical despite different names*

### Comparing `slowapi-0.1.7/slowapi/wrappers.py` & `slowapi-0.1.8/slowapi/wrappers.py`

 * *Files identical despite different names*

### Comparing `slowapi-0.1.7/setup.py` & `slowapi-0.1.8/PKG-INFO`

 * *Files 24% similar despite different names*

```diff
@@ -1,30 +1,94 @@
-# -*- coding: utf-8 -*-
-from setuptools import setup
+Metadata-Version: 2.1
+Name: slowapi
+Version: 0.1.8
+Summary: A rate limiting extension for Starlette and Fastapi
+Home-page: https://github.com/laurents/slowapi
+License: MIT
+Author: Laurent Savaete
+Author-email: laurent@where.tf
+Requires-Python: >=3.7,<4.0
+Classifier: License :: OSI Approved :: MIT License
+Classifier: Programming Language :: Python :: 3
+Classifier: Programming Language :: Python :: 3.7
+Classifier: Programming Language :: Python :: 3.8
+Classifier: Programming Language :: Python :: 3.9
+Classifier: Programming Language :: Python :: 3.10
+Classifier: Programming Language :: Python :: 3.11
+Provides-Extra: redis
+Requires-Dist: limits (>=2.3)
+Requires-Dist: redis (>=3.4.1,<4.0.0) ; extra == "redis"
+Project-URL: Documentation, https://slowapi.readthedocs.io/en/latest/
+Project-URL: Repository, https://github.com/laurents/slowapi
+Description-Content-Type: text/markdown
 
-packages = \
-['slowapi']
+# SlowApi
 
-package_data = \
-{'': ['*']}
+A rate limiting library for Starlette and FastAPI adapted from [flask-limiter](http://github.com/alisaifee/flask-limiter).
 
-install_requires = \
-['limits>=2.3,<3.0']
-
-setup_kwargs = {
-    'name': 'slowapi',
-    'version': '0.1.7',
-    'description': 'A rate limiting extension for Starlette and Fastapi',
-    'long_description': '# SlowApi\n\nA rate limiting library for Starlette and FastAPI adapted from [flask-limiter](http://github.com/alisaifee/flask-limiter).\n\nNote: this is alpha quality code still, the API may change, and things may fall apart while you try it.\n\nThe documentation is on [read the docs](https://slowapi.readthedocs.io/en/latest/).\n\n# Quick start\n\n## Installation\n\n`slowapi` is available from [pypi](https://pypi.org/project/slowapi/) so you can install it as usual:\n\n```\n$ pip install slowapi\n```\n\n# Features\n\nMost feature are coming from FlaskLimiter and the underlying [limits](https://limits.readthedocs.io/).\n\nSupported now:\n\n- Single and multiple `limit` decorator on endpoint functions to apply limits\n- redis, memcached and memory backends to track your limits (memory as a fallback)\n- support for sync and async HTTP endpoints\n- Support for shared limits across a set of routes\n\n\n# Limitations and known issues\n\n  * The `request` argument must be explicitly passed to your endpoint, or `slowapi` won\'t be able to hook into it. In other words, write:\n\n```python\n    @limiter.limit("5/minute")\n    async def myendpoint(request: Request)\n        pass\n```\n\nand not:\n\n```python\n    @limiter.limit("5/minute")\n    async def myendpoint()\n        pass\n```\n\n  * `websocket` endpoints are not supported yet.\n\n# Developing and contributing\n\nPRs are more than welcome! Please include tests for your changes :)\n\nThe package uses [poetry](https://python-poetry.org) to manage dependencies. To setup your dev env:\n\n```bash\n$ poetry install\n```\n\nTo run the tests:\n```bash\n$ pytest\n```\n\n# Credits\n\nCredits go to [flask-limiter](https://github.com/alisaifee/flask-limiter) of which SlowApi is a (still partial) adaptation to Starlette and FastAPI.\nIt\'s also important to mention that the actual rate limiting work is done by [limits](https://github.com/alisaifee/limits/), `slowapi` is just a wrapper around it.\n',
-    'author': 'Laurent Savaete',
-    'author_email': 'laurent@where.tf',
-    'maintainer': 'None',
-    'maintainer_email': 'None',
-    'url': 'https://github.com/laurents/slowapi',
-    'packages': packages,
-    'package_data': package_data,
-    'install_requires': install_requires,
-    'python_requires': '>=3.7,<4.0',
-}
+This package is used in various production setups, handling millions of requests per month, and seems to behave as expected.
+There might be some API changes when changing the code to be fully `async`, but we will notify users via appropriate `semver` version changes.
 
+The documentation is on [read the docs](https://slowapi.readthedocs.io/en/latest/).
+
+# Quick start
+
+## Installation
+
+`slowapi` is available from [pypi](https://pypi.org/project/slowapi/) so you can install it as usual:
+
+```
+$ pip install slowapi
+```
+
+# Features
+
+Most feature are coming from FlaskLimiter and the underlying [limits](https://limits.readthedocs.io/).
+
+Supported now:
+
+- Single and multiple `limit` decorator on endpoint functions to apply limits
+- redis, memcached and memory backends to track your limits (memory as a fallback)
+- support for sync and async HTTP endpoints
+- Support for shared limits across a set of routes
+
+
+# Limitations and known issues
+
+  * The `request` argument must be explicitly passed to your endpoint, or `slowapi` won't be able to hook into it. In other words, write:
+
+```python
+    @limiter.limit("5/minute")
+    async def myendpoint(request: Request)
+        pass
+```
+
+and not:
+
+```python
+    @limiter.limit("5/minute")
+    async def myendpoint()
+        pass
+```
+
+  * `websocket` endpoints are not supported yet.
+
+# Developing and contributing
+
+PRs are more than welcome! Please include tests for your changes :)
+
+The package uses [poetry](https://python-poetry.org) to manage dependencies. To setup your dev env:
+
+```bash
+$ poetry install
+```
+
+To run the tests:
+```bash
+$ pytest
+```
+
+# Credits
+
+Credits go to [flask-limiter](https://github.com/alisaifee/flask-limiter) of which SlowApi is a (still partial) adaptation to Starlette and FastAPI.
+It's also important to mention that the actual rate limiting work is done by [limits](https://github.com/alisaifee/limits/), `slowapi` is just a wrapper around it.
 
-setup(**setup_kwargs)
```

