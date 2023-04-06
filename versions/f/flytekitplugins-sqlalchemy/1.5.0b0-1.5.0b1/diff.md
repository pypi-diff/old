# Comparing `tmp/flytekitplugins-sqlalchemy-1.5.0b0.tar.gz` & `tmp/flytekitplugins-sqlalchemy-1.5.0b1.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "flytekitplugins-sqlalchemy-1.5.0b0.tar", last modified: Tue Mar 21 00:09:56 2023, max compression
+gzip compressed data, was "flytekitplugins-sqlalchemy-1.5.0b1.tar", last modified: Wed Mar 29 18:58:44 2023, max compression
```

## Comparing `flytekitplugins-sqlalchemy-1.5.0b0.tar` & `flytekitplugins-sqlalchemy-1.5.0b1.tar`

### file list

```diff
@@ -1,16 +1,16 @@
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-21 00:09:56.672386 flytekitplugins-sqlalchemy-1.5.0b0/
--rw-r--r--   0 runner    (1001) docker     (123)      791 2023-03-21 00:09:56.668386 flytekitplugins-sqlalchemy-1.5.0b0/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)      528 2023-03-21 00:09:29.000000 flytekitplugins-sqlalchemy-1.5.0b0/README.md
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-21 00:09:56.668386 flytekitplugins-sqlalchemy-1.5.0b0/flytekitplugins/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-21 00:09:56.668386 flytekitplugins-sqlalchemy-1.5.0b0/flytekitplugins/sqlalchemy/
--rw-r--r--   0 runner    (1001) docker     (123)      335 2023-03-21 00:09:29.000000 flytekitplugins-sqlalchemy-1.5.0b0/flytekitplugins/sqlalchemy/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     5453 2023-03-21 00:09:29.000000 flytekitplugins-sqlalchemy-1.5.0b0/flytekitplugins/sqlalchemy/task.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-21 00:09:56.668386 flytekitplugins-sqlalchemy-1.5.0b0/flytekitplugins_sqlalchemy.egg-info/
--rw-r--r--   0 runner    (1001) docker     (123)      791 2023-03-21 00:09:56.000000 flytekitplugins-sqlalchemy-1.5.0b0/flytekitplugins_sqlalchemy.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)      400 2023-03-21 00:09:56.000000 flytekitplugins-sqlalchemy-1.5.0b0/flytekitplugins_sqlalchemy.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-03-21 00:09:56.000000 flytekitplugins-sqlalchemy-1.5.0b0/flytekitplugins_sqlalchemy.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (123)       16 2023-03-21 00:09:56.000000 flytekitplugins-sqlalchemy-1.5.0b0/flytekitplugins_sqlalchemy.egg-info/namespace_packages.txt
--rw-r--r--   0 runner    (1001) docker     (123)       43 2023-03-21 00:09:56.000000 flytekitplugins-sqlalchemy-1.5.0b0/flytekitplugins_sqlalchemy.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (123)       16 2023-03-21 00:09:56.000000 flytekitplugins-sqlalchemy-1.5.0b0/flytekitplugins_sqlalchemy.egg-info/top_level.txt
--rw-r--r--   0 runner    (1001) docker     (123)       38 2023-03-21 00:09:56.672386 flytekitplugins-sqlalchemy-1.5.0b0/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (123)     1158 2023-03-21 00:09:46.000000 flytekitplugins-sqlalchemy-1.5.0b0/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-29 18:58:44.556235 flytekitplugins-sqlalchemy-1.5.0b1/
+-rw-r--r--   0 runner    (1001) docker     (123)      791 2023-03-29 18:58:44.556235 flytekitplugins-sqlalchemy-1.5.0b1/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)      528 2023-03-29 18:58:20.000000 flytekitplugins-sqlalchemy-1.5.0b1/README.md
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-29 18:58:44.552235 flytekitplugins-sqlalchemy-1.5.0b1/flytekitplugins/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-29 18:58:44.552235 flytekitplugins-sqlalchemy-1.5.0b1/flytekitplugins/sqlalchemy/
+-rw-r--r--   0 runner    (1001) docker     (123)      335 2023-03-29 18:58:20.000000 flytekitplugins-sqlalchemy-1.5.0b1/flytekitplugins/sqlalchemy/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5559 2023-03-29 18:58:20.000000 flytekitplugins-sqlalchemy-1.5.0b1/flytekitplugins/sqlalchemy/task.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-29 18:58:44.552235 flytekitplugins-sqlalchemy-1.5.0b1/flytekitplugins_sqlalchemy.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)      791 2023-03-29 18:58:44.000000 flytekitplugins-sqlalchemy-1.5.0b1/flytekitplugins_sqlalchemy.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)      400 2023-03-29 18:58:44.000000 flytekitplugins-sqlalchemy-1.5.0b1/flytekitplugins_sqlalchemy.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-03-29 18:58:44.000000 flytekitplugins-sqlalchemy-1.5.0b1/flytekitplugins_sqlalchemy.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       16 2023-03-29 18:58:44.000000 flytekitplugins-sqlalchemy-1.5.0b1/flytekitplugins_sqlalchemy.egg-info/namespace_packages.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       43 2023-03-29 18:58:44.000000 flytekitplugins-sqlalchemy-1.5.0b1/flytekitplugins_sqlalchemy.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       16 2023-03-29 18:58:44.000000 flytekitplugins-sqlalchemy-1.5.0b1/flytekitplugins_sqlalchemy.egg-info/top_level.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       38 2023-03-29 18:58:44.556235 flytekitplugins-sqlalchemy-1.5.0b1/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (123)     1158 2023-03-29 18:58:35.000000 flytekitplugins-sqlalchemy-1.5.0b1/setup.py
```

### Comparing `flytekitplugins-sqlalchemy-1.5.0b0/PKG-INFO` & `flytekitplugins-sqlalchemy-1.5.0b1/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: flytekitplugins-sqlalchemy
-Version: 1.5.0b0
+Version: 1.5.0b1
 Summary: SQLAlchemy plugin for flytekit
 Author: dolthub
 Author-email: max@dolthub.com
 License: apache2
 Classifier: Intended Audience :: Science/Research
 Classifier: Intended Audience :: Developers
 Classifier: License :: OSI Approved :: Apache Software License
```

### Comparing `flytekitplugins-sqlalchemy-1.5.0b0/README.md` & `flytekitplugins-sqlalchemy-1.5.0b1/README.md`

 * *Files identical despite different names*

### Comparing `flytekitplugins-sqlalchemy-1.5.0b0/flytekitplugins/sqlalchemy/task.py` & `flytekitplugins-sqlalchemy-1.5.0b1/flytekitplugins/sqlalchemy/task.py`

 * *Files 3% similar despite different names*

```diff
@@ -1,13 +1,13 @@
 import typing
 from dataclasses import dataclass
 
 import pandas as pd
 from pandas.io.sql import pandasSQL_builder
-from sqlalchemy import create_engine  # type: ignore
+from sqlalchemy import create_engine, text  # type: ignore
 
 from flytekit import current_context, kwtypes
 from flytekit.configuration import SerializationSettings
 from flytekit.configuration.default_images import DefaultImages, PythonVersion
 from flytekit.core.base_sql_task import SQLTask
 from flytekit.core.python_customized_container_task import PythonCustomizedContainerTask
 from flytekit.core.shim_task import ShimTaskExecutor
@@ -19,14 +19,15 @@
 class SQLAlchemyDefaultImages(DefaultImages):
     """Default images for the sqlalchemy flytekit plugin."""
 
     _DEFAULT_IMAGE_PREFIXES = {
         PythonVersion.PYTHON_3_8: "cr.flyte.org/flyteorg/flytekit:py3.8-sqlalchemy-",
         PythonVersion.PYTHON_3_9: "cr.flyte.org/flyteorg/flytekit:py3.9-sqlalchemy-",
         PythonVersion.PYTHON_3_10: "cr.flyte.org/flyteorg/flytekit:py3.10-sqlalchemy-",
+        PythonVersion.PYTHON_3_11: "cr.flyte.org/flyteorg/flytekit:py3.11-sqlalchemy-",
     }
 
 
 @dataclass
 class SQLAlchemyConfig(object):
     """
     Use this configuration to configure task. String should be standard
@@ -128,11 +129,11 @@
         print(f"Connecting to db {tt.custom['uri']}")
 
         interpolated_query = SQLAlchemyTask.interpolate_query(tt.custom["query_template"], **kwargs)
         print(f"Interpolated query {interpolated_query}")
         with engine.begin() as connection:
             df = None
             if tt.interface.outputs:
-                df = pd.read_sql_query(interpolated_query, connection)
+                df = pd.read_sql_query(text(interpolated_query), connection)
             else:
-                pandasSQL_builder(connection).execute(interpolated_query)
+                pandasSQL_builder(connection).execute(text(interpolated_query))
         return df
```

### Comparing `flytekitplugins-sqlalchemy-1.5.0b0/flytekitplugins_sqlalchemy.egg-info/PKG-INFO` & `flytekitplugins-sqlalchemy-1.5.0b1/flytekitplugins_sqlalchemy.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: flytekitplugins-sqlalchemy
-Version: 1.5.0b0
+Version: 1.5.0b1
 Summary: SQLAlchemy plugin for flytekit
 Author: dolthub
 Author-email: max@dolthub.com
 License: apache2
 Classifier: Intended Audience :: Science/Research
 Classifier: Intended Audience :: Developers
 Classifier: License :: OSI Approved :: Apache Software License
```

### Comparing `flytekitplugins-sqlalchemy-1.5.0b0/setup.py` & `flytekitplugins-sqlalchemy-1.5.0b1/setup.py`

 * *Files 8% similar despite different names*

```diff
@@ -2,15 +2,15 @@
 
 PLUGIN_NAME = "sqlalchemy"
 
 microlib_name = f"flytekitplugins-{PLUGIN_NAME}"
 
 plugin_requires = ["flytekit>=1.3.0b2,<2.0.0", "sqlalchemy>=1.4.7"]
 
-__version__ = "1.5.0b0"
+__version__ = "1.5.0b1"
 
 setup(
     name=microlib_name,
     version=__version__,
     author="dolthub",
     author_email="max@dolthub.com",
     description="SQLAlchemy plugin for flytekit",
```

