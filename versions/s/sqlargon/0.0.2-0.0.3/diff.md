# Comparing `tmp/sqlargon-0.0.2.tar.gz` & `tmp/sqlargon-0.0.3.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "sqlargon-0.0.2.tar", max compression
+gzip compressed data, was "sqlargon-0.0.3.tar", max compression
```

## Comparing `sqlargon-0.0.2.tar` & `sqlargon-0.0.3.tar`

### file list

```diff
@@ -1,20 +1,20 @@
--rw-r--r--   0        0        0    11357 2023-04-05 12:41:18.885995 sqlargon-0.0.2/LICENSE
--rw-r--r--   0        0        0     3136 2023-04-05 12:41:18.885995 sqlargon-0.0.2/README.md
--rw-r--r--   0        0        0     1471 2023-04-05 12:41:18.885995 sqlargon-0.0.2/pyproject.toml
--rw-r--r--   0        0        0      454 2023-04-05 12:41:18.885995 sqlargon-0.0.2/sqlargon/__init__.py
--rw-r--r--   0        0        0       22 2023-04-05 12:41:18.885995 sqlargon-0.0.2/sqlargon/_version.py
--rw-r--r--   0        0        0     3086 2023-04-05 12:41:18.889995 sqlargon-0.0.2/sqlargon/db.py
--rw-r--r--   0        0        0        0 2023-04-05 12:41:18.889995 sqlargon-0.0.2/sqlargon/dialects/__init__.py
--rw-r--r--   0        0        0      206 2023-04-05 12:41:18.889995 sqlargon-0.0.2/sqlargon/dialects/postgres.py
--rw-r--r--   0        0        0      243 2023-04-05 12:41:18.889995 sqlargon-0.0.2/sqlargon/dialects/sqlite.py
--rw-r--r--   0        0        0     6243 2023-04-05 12:41:18.889995 sqlargon-0.0.2/sqlargon/function_elements.py
--rw-r--r--   0        0        0        0 2023-04-05 12:41:18.889995 sqlargon-0.0.2/sqlargon/integrations/__init__.py
--rw-r--r--   0        0        0     1091 2023-04-05 12:41:18.889995 sqlargon-0.0.2/sqlargon/integrations/fastapi.py
--rw-r--r--   0        0        0     1315 2023-04-05 12:41:18.889995 sqlargon-0.0.2/sqlargon/mixins.py
--rw-r--r--   0        0        0      913 2023-04-05 12:41:18.889995 sqlargon-0.0.2/sqlargon/orm.py
--rw-r--r--   0        0        0        0 2023-04-05 12:41:18.889995 sqlargon-0.0.2/sqlargon/py.typed
--rw-r--r--   0        0        0     7358 2023-04-05 12:41:18.889995 sqlargon-0.0.2/sqlargon/repository.py
--rw-r--r--   0        0        0      793 2023-04-05 12:41:18.889995 sqlargon-0.0.2/sqlargon/settings.py
--rw-r--r--   0        0        0     3033 2023-04-05 12:41:18.889995 sqlargon-0.0.2/sqlargon/types.py
--rw-r--r--   0        0        0      255 2023-04-05 12:41:18.889995 sqlargon-0.0.2/sqlargon/util.py
--rw-r--r--   0        0        0     3834 1970-01-01 00:00:00.000000 sqlargon-0.0.2/PKG-INFO
+-rw-r--r--   0        0        0    11357 2023-04-06 09:54:04.659536 sqlargon-0.0.3/LICENSE
+-rw-r--r--   0        0        0     3280 2023-04-06 09:54:04.659536 sqlargon-0.0.3/README.md
+-rw-r--r--   0        0        0     1559 2023-04-06 09:54:04.659536 sqlargon-0.0.3/pyproject.toml
+-rw-r--r--   0        0        0      454 2023-04-06 09:54:04.659536 sqlargon-0.0.3/sqlargon/__init__.py
+-rw-r--r--   0        0        0       22 2023-04-06 09:54:04.659536 sqlargon-0.0.3/sqlargon/_version.py
+-rw-r--r--   0        0        0     3585 2023-04-06 09:54:04.659536 sqlargon-0.0.3/sqlargon/db.py
+-rw-r--r--   0        0        0        0 2023-04-06 09:54:04.659536 sqlargon-0.0.3/sqlargon/dialects/__init__.py
+-rw-r--r--   0        0        0      206 2023-04-06 09:54:04.659536 sqlargon-0.0.3/sqlargon/dialects/postgres.py
+-rw-r--r--   0        0        0      243 2023-04-06 09:54:04.659536 sqlargon-0.0.3/sqlargon/dialects/sqlite.py
+-rw-r--r--   0        0        0     6243 2023-04-06 09:54:04.659536 sqlargon-0.0.3/sqlargon/function_elements.py
+-rw-r--r--   0        0        0        0 2023-04-06 09:54:04.659536 sqlargon-0.0.3/sqlargon/integrations/__init__.py
+-rw-r--r--   0        0        0      824 2023-04-06 09:54:04.659536 sqlargon-0.0.3/sqlargon/integrations/fastapi.py
+-rw-r--r--   0        0        0     1315 2023-04-06 09:54:04.659536 sqlargon-0.0.3/sqlargon/mixins.py
+-rw-r--r--   0        0        0      913 2023-04-06 09:54:04.659536 sqlargon-0.0.3/sqlargon/orm.py
+-rw-r--r--   0        0        0        0 2023-04-06 09:54:04.659536 sqlargon-0.0.3/sqlargon/py.typed
+-rw-r--r--   0        0        0     7358 2023-04-06 09:54:04.659536 sqlargon-0.0.3/sqlargon/repository.py
+-rw-r--r--   0        0        0      803 2023-04-06 09:54:04.659536 sqlargon-0.0.3/sqlargon/settings.py
+-rw-r--r--   0        0        0     3033 2023-04-06 09:54:04.659536 sqlargon-0.0.3/sqlargon/types.py
+-rw-r--r--   0        0        0      255 2023-04-06 09:54:04.659536 sqlargon-0.0.3/sqlargon/util.py
+-rw-r--r--   0        0        0     3978 1970-01-01 00:00:00.000000 sqlargon-0.0.3/PKG-INFO
```

### Comparing `sqlargon-0.0.2/LICENSE` & `sqlargon-0.0.3/LICENSE`

 * *Files identical despite different names*

### Comparing `sqlargon-0.0.2/README.md` & `sqlargon-0.0.3/README.md`

 * *Files 3% similar despite different names*

```diff
@@ -9,14 +9,23 @@
 ![Mypy](https://img.shields.io/badge/mypy-checked-blue)
 ![Code Style](https://img.shields.io/badge/code%20style-black-000000.svg)
 [![security: bandit](https://img.shields.io/badge/security-bandit-yellow.svg)](https://github.com/PyCQA/bandit)
 
 
 *Wrapper around SQLAlchemy async session, core and Postgres native features*
 
+---
+Version: 0.0.3
+
+Documentation: https://performancemedia.github.io/sqlargon/
+
+Repository: https://github.com/performancemedia/sqlargon
+
+---
+
 ## About
 
 This library provides glue code to use sqlalchemy async sessions, core queries and orm models 
 from one object which provides somewhat of repository pattern. This solution has few advantages:
 
 - no need to pass `session` object to every function/method. It is stored (and optionally injected) in repository object
 - write data access queries in one place
```

### Comparing `sqlargon-0.0.2/pyproject.toml` & `sqlargon-0.0.3/pyproject.toml`

 * *Files 7% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 [tool.poetry]
 name = "sqlargon"
-version = "0.0.2"
+version = "0.0.3"
 description = "SQLAlchemy utils for Postgres and Sqlite"
 readme = "README.md"
 authors = [
     "Radzim Kowalow <radzim.kowalow@performance-media.pl>"
 ]
 
 [tool.poetry.dependencies]
@@ -46,14 +46,19 @@
 
 [tool.bandit]
 skips = ['B101']
 
 [tool.isort]
 profile = "black"
 
+[tool.mypy]
+python_version = 3.9
+ignore_missing_imports = true
+no_site_packages = true
+
 [tool.semantic_release]
 version_variable = [
     'sqlargon/_version.py:__version__',
 ]
 version_toml = 'pyproject.toml:tool.poetry.version'
 version_pattern = [
     'docs/index.md:Version: (\d+\.\d+\.\d+)',
```

### Comparing `sqlargon-0.0.2/sqlargon/db.py` & `sqlargon-0.0.3/sqlargon/db.py`

 * *Files 22% similar despite different names*

```diff
@@ -1,38 +1,36 @@
-from __future__ import annotations
-
 import functools
 from contextlib import asynccontextmanager
-from typing import Any, AsyncGenerator, Callable
+from typing import Any, AsyncGenerator, Callable, Type
 
 from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
 from sqlalchemy.pool import AsyncAdaptedQueuePool, Pool
 
 from .repository import SQLAlchemyModelRepository
 from .settings import DatabaseSettings
 from .util import json_dumps, json_loads
 
 
 def configure_repository_class(dialect):
-    if dialect == "postgres":
+    if dialect == "postgresql":
         from .dialects.postgres import configure_postgres_dialect
 
         configure_postgres_dialect(SQLAlchemyModelRepository)
 
     elif dialect == "sqlite":
         from .dialects.sqlite import configure_sqlite_dialect
 
         configure_sqlite_dialect(SQLAlchemyModelRepository)
 
 
 class Database:
     def __init__(
         self,
         url: str,
-        poolclass: type[Pool] = AsyncAdaptedQueuePool,
+        poolclass: Type[Pool] = AsyncAdaptedQueuePool,
         pool_size: int = 10,
         max_overflow: int = 0,
         pool_recycle: int = 1200,
         echo: bool = False,
         echo_pool: bool = True,
         json_serializer: Callable[[Any], str] = json_dumps,
         json_deserializer: Callable[[str], Any] = json_loads,
@@ -55,19 +53,17 @@
         self.session_maker = async_sessionmaker(
             bind=self.engine, expire_on_commit=False
         )
         self.session = asynccontextmanager(self.session_factory)
         configure_repository_class(self.engine.url.get_dialect().name)
 
         if use_depends:
-            from fastapi import Depends
-
-            from .integrations.fastapi import depends_on
+            from .integrations.fastapi import fastapi_integration
 
-            depends_on(Depends(self.session_factory))(SQLAlchemyModelRepository)
+            fastapi_integration(self.session_factory)
 
     async def session_factory(self) -> AsyncGenerator[AsyncSession, None]:
         async with self.session_maker() as session:
             try:
                 yield session
                 await session.commit()
             except:  # noqa
@@ -91,7 +87,23 @@
                     async with self.session() as session:
                         kwargs["session"] = session
                         return await func(*args, **kwargs)
 
             return wrapped
 
         return wrapper
+
+    def inject_repository(
+        self, repository_type: Type[SQLAlchemyModelRepository], name: str = "repository"
+    ):
+        def wrapper(func):
+            @functools.wraps(func)
+            async def wrapped(*args, **kwargs):
+                if name not in kwargs or kwargs[name] is None:
+                    async with self.session() as session:
+                        repository = repository_type(session=session)
+                        kwargs[name] = repository
+                        return await func(*args, **kwargs)
+
+            return wrapped
+
+        return wrapper
```

### Comparing `sqlargon-0.0.2/sqlargon/function_elements.py` & `sqlargon-0.0.3/sqlargon/function_elements.py`

 * *Files identical despite different names*

### Comparing `sqlargon-0.0.2/sqlargon/integrations/fastapi.py` & `sqlargon-0.0.3/sqlargon/integrations/fastapi.py`

 * *Files 13% similar despite different names*

```diff
@@ -1,35 +1,19 @@
 import inspect
 
-from ..repository import SQLAlchemyModelRepository
-
+from fastapi import Depends
 
-def depends_on(default):
-    """
-    Usage
-
-    @depends_on(Depends(get_db)
-    class SQLAlchemyModelRepository:
-        pass
-    or:
-    db = Database(..., use_depends=True)
-    :param default: Depends(db)
-    :return:
-    """
+from ..repository import SQLAlchemyModelRepository
 
-    def wrapper(cls: SQLAlchemyModelRepository):
-        old_signature = inspect.signature(cls.__init__)  # type: ignore
-        old_parameters: list[inspect.Parameter] = list(
-            old_signature.parameters.values()
-        )
-        old_first_parameter = old_parameters[0]
-        old_second_parameter = old_parameters[1]
-        new_first_parameter = old_second_parameter.replace(default=default)
-        new_parameters = [old_first_parameter, new_first_parameter] + [
-            parameter.replace(kind=inspect.Parameter.KEYWORD_ONLY)
-            for parameter in old_parameters[2:]
-        ]
-        new_signature = old_signature.replace(parameters=new_parameters)
-        setattr(cls.__init__, "__signature__", new_signature)  # type: ignore
-        return cls
 
-    return wrapper
+def fastapi_integration(factory):
+    old_signature = inspect.signature(SQLAlchemyModelRepository.__init__)  # type: ignore
+    old_parameters: list[inspect.Parameter] = list(old_signature.parameters.values())
+    old_first_parameter = old_parameters[0]
+    old_second_parameter = old_parameters[1]
+    new_first_parameter = old_second_parameter.replace(default=Depends(factory))
+    new_parameters = [old_first_parameter, new_first_parameter] + [
+        parameter.replace(kind=inspect.Parameter.KEYWORD_ONLY)
+        for parameter in old_parameters[2:]
+    ]
+    new_signature = old_signature.replace(parameters=new_parameters)
+    setattr(SQLAlchemyModelRepository.__init__, "__signature__", new_signature)  # type: ignore
```

### Comparing `sqlargon-0.0.2/sqlargon/mixins.py` & `sqlargon-0.0.3/sqlargon/mixins.py`

 * *Files identical despite different names*

### Comparing `sqlargon-0.0.2/sqlargon/orm.py` & `sqlargon-0.0.3/sqlargon/orm.py`

 * *Files identical despite different names*

### Comparing `sqlargon-0.0.2/sqlargon/repository.py` & `sqlargon-0.0.3/sqlargon/repository.py`

 * *Files identical despite different names*

### Comparing `sqlargon-0.0.2/sqlargon/settings.py` & `sqlargon-0.0.3/sqlargon/settings.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,12 +1,12 @@
 from pydantic import BaseSettings, Field, PyObject
 
 
 class DatabaseSettings(BaseSettings):
-    url: str = Field("postgres://localhost:5432", env="DATABASE_URL")
+    url: str = Field("postgresql+asyncpg://localhost:5432", env="DATABASE_URL")
     pool_size: int = Field(10, env="DATABASE_POOL_SIZE")
     echo: bool = Field(False, env="DATABASE_ECHO")
     echo_pool: bool = Field(True, env="DATABASE_ECHO_POOL")
     max_overflow: int = Field(0, env="DATABASE_MAX_OVERFLOW")
     pool_recycle: int = Field(3600, env="DATABASE_POOL_RECYCLE")
     poolclass: PyObject = Field(
         "sqlalchemy.AsyncAdaptedQueuePool", env="DATABASE_POOL_CLASS"
```

### Comparing `sqlargon-0.0.2/sqlargon/types.py` & `sqlargon-0.0.3/sqlargon/types.py`

 * *Files identical despite different names*

### Comparing `sqlargon-0.0.2/PKG-INFO` & `sqlargon-0.0.3/PKG-INFO`

 * *Files 7% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: sqlargon
-Version: 0.0.2
+Version: 0.0.3
 Summary: SQLAlchemy utils for Postgres and Sqlite
 Author: Radzim Kowalow
 Author-email: radzim.kowalow@performance-media.pl
 Requires-Python: >=3.8.1,<4.0
 Classifier: Programming Language :: Python :: 3
 Classifier: Programming Language :: Python :: 3.9
 Classifier: Programming Language :: Python :: 3.10
@@ -28,14 +28,23 @@
 ![Mypy](https://img.shields.io/badge/mypy-checked-blue)
 ![Code Style](https://img.shields.io/badge/code%20style-black-000000.svg)
 [![security: bandit](https://img.shields.io/badge/security-bandit-yellow.svg)](https://github.com/PyCQA/bandit)
 
 
 *Wrapper around SQLAlchemy async session, core and Postgres native features*
 
+---
+Version: 0.0.3
+
+Documentation: https://performancemedia.github.io/sqlargon/
+
+Repository: https://github.com/performancemedia/sqlargon
+
+---
+
 ## About
 
 This library provides glue code to use sqlalchemy async sessions, core queries and orm models 
 from one object which provides somewhat of repository pattern. This solution has few advantages:
 
 - no need to pass `session` object to every function/method. It is stored (and optionally injected) in repository object
 - write data access queries in one place
```

