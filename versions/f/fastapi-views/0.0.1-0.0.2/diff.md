# Comparing `tmp/fastapi_views-0.0.1.tar.gz` & `tmp/fastapi_views-0.0.2.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "fastapi_views-0.0.1.tar", max compression
+gzip compressed data, was "fastapi_views-0.0.2.tar", max compression
```

## Comparing `fastapi_views-0.0.1.tar` & `fastapi_views-0.0.2.tar`

### file list

```diff
@@ -1,27 +1,27 @@
--rw-r--r--   0        0        0    11357 2023-04-05 21:33:09.177601 fastapi_views-0.0.1/LICENSE
--rw-r--r--   0        0        0     1983 2023-04-05 21:33:09.177601 fastapi_views-0.0.1/README.md
--rw-r--r--   0        0        0      593 2023-04-05 21:33:09.177601 fastapi_views-0.0.1/fastapi_views/__init__.py
--rw-r--r--   0        0        0       22 2023-04-05 21:33:09.177601 fastapi_views-0.0.1/fastapi_views/_version.py
--rw-r--r--   0        0        0     1792 2023-04-05 21:33:09.177601 fastapi_views-0.0.1/fastapi_views/config.py
--rw-r--r--   0        0        0      479 2023-04-05 21:33:09.177601 fastapi_views-0.0.1/fastapi_views/errors/__init__.py
--rw-r--r--   0        0        0      449 2023-04-05 21:33:09.177601 fastapi_views-0.0.1/fastapi_views/errors/exceptions.py
--rw-r--r--   0        0        0     1253 2023-04-05 21:33:09.177601 fastapi_views-0.0.1/fastapi_views/errors/handlers.py
--rw-r--r--   0        0        0     1811 2023-04-05 21:33:09.177601 fastapi_views-0.0.1/fastapi_views/errors/models.py
--rw-r--r--   0        0        0      986 2023-04-05 21:33:09.177601 fastapi_views-0.0.1/fastapi_views/errors/utils.py
--rw-r--r--   0        0        0     1634 2023-04-05 21:33:09.177601 fastapi_views-0.0.1/fastapi_views/healthcheck.py
--rw-r--r--   0        0        0      331 2023-04-05 21:33:09.177601 fastapi_views-0.0.1/fastapi_views/openapi.py
--rw-r--r--   0        0        0      655 2023-04-05 21:33:09.177601 fastapi_views-0.0.1/fastapi_views/prometheus.py
--rw-r--r--   0        0        0        0 2023-04-05 21:33:09.177601 fastapi_views-0.0.1/fastapi_views/py.typed
--rw-r--r--   0        0        0      413 2023-04-05 21:33:09.177601 fastapi_views-0.0.1/fastapi_views/response.py
--rw-r--r--   0        0        0      293 2023-04-05 21:33:09.177601 fastapi_views-0.0.1/fastapi_views/routers.py
--rw-r--r--   0        0        0      741 2023-04-05 21:33:09.177601 fastapi_views-0.0.1/fastapi_views/serializer.py
--rw-r--r--   0        0        0     2063 2023-04-05 21:33:09.177601 fastapi_views-0.0.1/fastapi_views/settings.py
--rw-r--r--   0        0        0      745 2023-04-05 21:33:09.177601 fastapi_views-0.0.1/fastapi_views/types.py
--rw-r--r--   0        0        0        0 2023-04-05 21:33:09.177601 fastapi_views-0.0.1/fastapi_views/views/__init__.py
--rw-r--r--   0        0        0    11545 2023-04-05 21:33:09.177601 fastapi_views-0.0.1/fastapi_views/views/api.py
--rw-r--r--   0        0        0     1406 2023-04-05 21:33:09.177601 fastapi_views-0.0.1/fastapi_views/views/functools.py
--rw-r--r--   0        0        0     6888 2023-04-05 21:33:09.177601 fastapi_views-0.0.1/fastapi_views/views/generics.py
--rw-r--r--   0        0        0     1367 2023-04-05 21:33:09.177601 fastapi_views-0.0.1/fastapi_views/views/mixins.py
--rw-r--r--   0        0        0     1631 2023-04-05 21:33:09.177601 fastapi_views-0.0.1/fastapi_views/views/viewsets.py
--rw-r--r--   0        0        0     1289 2023-04-05 21:33:09.181602 fastapi_views-0.0.1/pyproject.toml
--rw-r--r--   0        0        0     2604 1970-01-01 00:00:00.000000 fastapi_views-0.0.1/PKG-INFO
+-rw-r--r--   0        0        0    11357 2023-04-06 09:52:57.767655 fastapi_views-0.0.2/LICENSE
+-rw-r--r--   0        0        0     1983 2023-04-06 09:52:57.767655 fastapi_views-0.0.2/README.md
+-rw-r--r--   0        0        0      593 2023-04-06 09:52:57.767655 fastapi_views-0.0.2/fastapi_views/__init__.py
+-rw-r--r--   0        0        0       22 2023-04-06 09:52:57.767655 fastapi_views-0.0.2/fastapi_views/_version.py
+-rw-r--r--   0        0        0     1792 2023-04-06 09:52:57.767655 fastapi_views-0.0.2/fastapi_views/config.py
+-rw-r--r--   0        0        0      479 2023-04-06 09:52:57.767655 fastapi_views-0.0.2/fastapi_views/errors/__init__.py
+-rw-r--r--   0        0        0      449 2023-04-06 09:52:57.767655 fastapi_views-0.0.2/fastapi_views/errors/exceptions.py
+-rw-r--r--   0        0        0     1253 2023-04-06 09:52:57.767655 fastapi_views-0.0.2/fastapi_views/errors/handlers.py
+-rw-r--r--   0        0        0     1811 2023-04-06 09:52:57.767655 fastapi_views-0.0.2/fastapi_views/errors/models.py
+-rw-r--r--   0        0        0      986 2023-04-06 09:52:57.767655 fastapi_views-0.0.2/fastapi_views/errors/utils.py
+-rw-r--r--   0        0        0     1634 2023-04-06 09:52:57.767655 fastapi_views-0.0.2/fastapi_views/healthcheck.py
+-rw-r--r--   0        0        0      331 2023-04-06 09:52:57.767655 fastapi_views-0.0.2/fastapi_views/openapi.py
+-rw-r--r--   0        0        0      655 2023-04-06 09:52:57.767655 fastapi_views-0.0.2/fastapi_views/prometheus.py
+-rw-r--r--   0        0        0        0 2023-04-06 09:52:57.767655 fastapi_views-0.0.2/fastapi_views/py.typed
+-rw-r--r--   0        0        0      413 2023-04-06 09:52:57.767655 fastapi_views-0.0.2/fastapi_views/response.py
+-rw-r--r--   0        0        0      293 2023-04-06 09:52:57.767655 fastapi_views-0.0.2/fastapi_views/routers.py
+-rw-r--r--   0        0        0      741 2023-04-06 09:52:57.767655 fastapi_views-0.0.2/fastapi_views/serializer.py
+-rw-r--r--   0        0        0     2063 2023-04-06 09:52:57.767655 fastapi_views-0.0.2/fastapi_views/settings.py
+-rw-r--r--   0        0        0      745 2023-04-06 09:52:57.767655 fastapi_views-0.0.2/fastapi_views/types.py
+-rw-r--r--   0        0        0        0 2023-04-06 09:52:57.767655 fastapi_views-0.0.2/fastapi_views/views/__init__.py
+-rw-r--r--   0        0        0    11545 2023-04-06 09:52:57.767655 fastapi_views-0.0.2/fastapi_views/views/api.py
+-rw-r--r--   0        0        0     1406 2023-04-06 09:52:57.767655 fastapi_views-0.0.2/fastapi_views/views/functools.py
+-rw-r--r--   0        0        0     6888 2023-04-06 09:52:57.767655 fastapi_views-0.0.2/fastapi_views/views/generics.py
+-rw-r--r--   0        0        0     1367 2023-04-06 09:52:57.767655 fastapi_views-0.0.2/fastapi_views/views/mixins.py
+-rw-r--r--   0        0        0     1631 2023-04-06 09:52:57.767655 fastapi_views-0.0.2/fastapi_views/views/viewsets.py
+-rw-r--r--   0        0        0     1561 2023-04-06 09:52:57.771655 fastapi_views-0.0.2/pyproject.toml
+-rw-r--r--   0        0        0     2604 1970-01-01 00:00:00.000000 fastapi_views-0.0.2/PKG-INFO
```

### Comparing `fastapi_views-0.0.1/LICENSE` & `fastapi_views-0.0.2/LICENSE`

 * *Files identical despite different names*

### Comparing `fastapi_views-0.0.1/README.md` & `fastapi_views-0.0.2/README.md`

 * *Files 0% similar despite different names*

```diff
@@ -9,15 +9,15 @@
 ![Mypy](https://img.shields.io/badge/mypy-checked-blue)
 ![Code Style](https://img.shields.io/badge/code%20style-black-000000.svg)
 [![security: bandit](https://img.shields.io/badge/security-bandit-yellow.svg)](https://github.com/PyCQA/bandit)
 
 *FastAPI Class Views and utilities*
 
 ---
-Version: 0.0.1
+Version: 0.0.2
 
 Documentation: https://performancemedia.github.io/fastapi-views/
 
 Repository: https://github.com/performancemedia/fastapi-views
 
 ---
```

### Comparing `fastapi_views-0.0.1/fastapi_views/__init__.py` & `fastapi_views-0.0.2/fastapi_views/__init__.py`

 * *Files identical despite different names*

### Comparing `fastapi_views-0.0.1/fastapi_views/config.py` & `fastapi_views-0.0.2/fastapi_views/config.py`

 * *Files identical despite different names*

### Comparing `fastapi_views-0.0.1/fastapi_views/errors/handlers.py` & `fastapi_views-0.0.2/fastapi_views/errors/handlers.py`

 * *Files identical despite different names*

### Comparing `fastapi_views-0.0.1/fastapi_views/errors/models.py` & `fastapi_views-0.0.2/fastapi_views/errors/models.py`

 * *Files identical despite different names*

### Comparing `fastapi_views-0.0.1/fastapi_views/errors/utils.py` & `fastapi_views-0.0.2/fastapi_views/errors/utils.py`

 * *Files identical despite different names*

### Comparing `fastapi_views-0.0.1/fastapi_views/healthcheck.py` & `fastapi_views-0.0.2/fastapi_views/healthcheck.py`

 * *Files identical despite different names*

### Comparing `fastapi_views-0.0.1/fastapi_views/prometheus.py` & `fastapi_views-0.0.2/fastapi_views/prometheus.py`

 * *Files identical despite different names*

### Comparing `fastapi_views-0.0.1/fastapi_views/serializer.py` & `fastapi_views-0.0.2/fastapi_views/serializer.py`

 * *Files identical despite different names*

### Comparing `fastapi_views-0.0.1/fastapi_views/settings.py` & `fastapi_views-0.0.2/fastapi_views/settings.py`

 * *Files identical despite different names*

### Comparing `fastapi_views-0.0.1/fastapi_views/types.py` & `fastapi_views-0.0.2/fastapi_views/types.py`

 * *Files identical despite different names*

### Comparing `fastapi_views-0.0.1/fastapi_views/views/api.py` & `fastapi_views-0.0.2/fastapi_views/views/api.py`

 * *Files identical despite different names*

### Comparing `fastapi_views-0.0.1/fastapi_views/views/functools.py` & `fastapi_views-0.0.2/fastapi_views/views/functools.py`

 * *Files identical despite different names*

### Comparing `fastapi_views-0.0.1/fastapi_views/views/generics.py` & `fastapi_views-0.0.2/fastapi_views/views/generics.py`

 * *Files 1% similar despite different names*

```diff
@@ -21,15 +21,15 @@
 P = TypeVar("P", bound=Type[BaseModel])
 
 
 class PK(BaseModel):
     id: UUID
 
 
-class GenericViewMixin(Generic[P], ErrorHandlerMixin):
+class GenericViewMixin(ErrorHandlerMixin, Generic[P]):
     repository: Repository
     params: P = BaseModel
 
     @classmethod
     def get_params(cls, action: str) -> P:
         return cls.params
```

### Comparing `fastapi_views-0.0.1/fastapi_views/views/mixins.py` & `fastapi_views-0.0.2/fastapi_views/views/mixins.py`

 * *Files identical despite different names*

### Comparing `fastapi_views-0.0.1/fastapi_views/views/viewsets.py` & `fastapi_views-0.0.2/fastapi_views/views/viewsets.py`

 * *Files identical despite different names*

### Comparing `fastapi_views-0.0.1/pyproject.toml` & `fastapi_views-0.0.2/pyproject.toml`

 * *Files 16% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 [tool.poetry]
 name = "fastapi-views"
-version = "0.0.1"
+version = "0.0.2"
 description = "FastAPI Class Views and utilities"
 authors = ["Radzim Kowalow <radzim.kowalow@performance-media.pl>"]
 readme = "README.md"
 packages = [{include = "fastapi_views"}]
 
 [tool.poetry.dependencies]
 python = ">=3.8.1,<4.0"
@@ -37,26 +37,36 @@
 [tool.pytest.ini_options]
 addopts = "--cov=./fastapi_views"
 testpaths = [
    "./tests"
 ]
 asyncio_mode = "auto"
 
-[tool.mypy]
-python_version = 3.11
-ignore_missing_imports = true
-no_site_packages = true
-exclude = "^tests"
+[tool.bandit]
+skips = ['B101']
 
 [tool.isort]
 profile = "black"
 
-[tool.coverage.report]
-exclude_lines = [
-   "pragma: no cover",
-   "if TYPE_CHECKING:",
-   "raise NotImplementedError"
+[tool.semantic_release]
+version_variable = [
+    'fastapi_views/_version.py:__version__',
+]
+version_toml = 'pyproject.toml:tool.poetry.version'
+version_pattern = [
+    'docs/index.md:Version: (\d+\.\d+\.\d+)',
+    'README.md:Version: (\d+\.\d+\.\d+)'
 ]
+upload_to_repository = false
+major_on_zero = true
+hvcs = "github"
+commit_message = "Bump version: {version}"
+tag_commit = false
+
+[tool.mypy]
+python_version = 3.9
+ignore_missing_imports = true
+no_site_packages = true
 
 [build-system]
 requires = ["poetry-core"]
 build-backend = "poetry.core.masonry.api"
```

### Comparing `fastapi_views-0.0.1/PKG-INFO` & `fastapi_views-0.0.2/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: fastapi-views
-Version: 0.0.1
+Version: 0.0.2
 Summary: FastAPI Class Views and utilities
 Author: Radzim Kowalow
 Author-email: radzim.kowalow@performance-media.pl
 Requires-Python: >=3.8.1,<4.0
 Classifier: Programming Language :: Python :: 3
 Classifier: Programming Language :: Python :: 3.9
 Classifier: Programming Language :: Python :: 3.10
@@ -26,15 +26,15 @@
 ![Mypy](https://img.shields.io/badge/mypy-checked-blue)
 ![Code Style](https://img.shields.io/badge/code%20style-black-000000.svg)
 [![security: bandit](https://img.shields.io/badge/security-bandit-yellow.svg)](https://github.com/PyCQA/bandit)
 
 *FastAPI Class Views and utilities*
 
 ---
-Version: 0.0.1
+Version: 0.0.2
 
 Documentation: https://performancemedia.github.io/fastapi-views/
 
 Repository: https://github.com/performancemedia/fastapi-views
 
 ---
```

