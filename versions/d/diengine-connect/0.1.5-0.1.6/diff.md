# Comparing `tmp/diengine-connect-0.1.5.tar.gz` & `tmp/diengine-connect-0.1.6.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "diengine-connect-0.1.5.tar", last modified: Mon Mar 27 09:16:45 2023, max compression
+gzip compressed data, was "diengine-connect-0.1.6.tar", last modified: Thu Apr  6 12:23:05 2023, max compression
```

## Comparing `diengine-connect-0.1.5.tar` & `diengine-connect-0.1.6.tar`

### file list

```diff
@@ -1,84 +1,86 @@
-drwxr-xr-x   0 xushihao   (501) staff       (20)        0 2023-03-27 09:16:45.652355 diengine-connect-0.1.5/
--rw-r--r--   0 xushihao   (501) staff       (20)    11389 2023-03-27 08:38:41.000000 diengine-connect-0.1.5/LICENSE
--rw-r--r--   0 xushihao   (501) staff       (20)     1336 2023-03-27 09:16:45.652223 diengine-connect-0.1.5/PKG-INFO
--rw-r--r--   0 xushihao   (501) staff       (20)      315 2023-03-27 08:38:41.000000 diengine-connect-0.1.5/README.md
-drwxr-xr-x   0 xushihao   (501) staff       (20)        0 2023-03-27 09:16:45.641605 diengine-connect-0.1.5/diengine_connect/
--rw-r--r--   0 xushihao   (501) staff       (20)        5 2023-03-27 09:16:38.000000 diengine-connect-0.1.5/diengine_connect/VERSION
--rw-r--r--   0 xushihao   (501) staff       (20)      261 2023-03-27 08:38:41.000000 diengine-connect-0.1.5/diengine_connect/__init__.py
-drwxr-xr-x   0 xushihao   (501) staff       (20)        0 2023-03-27 09:16:45.643183 diengine-connect-0.1.5/diengine_connect/cc_sqlalchemy/
--rw-r--r--   0 xushihao   (501) staff       (20)      200 2023-03-27 08:38:41.000000 diengine-connect-0.1.5/diengine_connect/cc_sqlalchemy/__init__.py
-drwxr-xr-x   0 xushihao   (501) staff       (20)        0 2023-03-27 09:16:45.643841 diengine-connect-0.1.5/diengine_connect/cc_sqlalchemy/datatypes/
--rw-r--r--   0 xushihao   (501) staff       (20)       57 2023-03-27 08:38:41.000000 diengine-connect-0.1.5/diengine_connect/cc_sqlalchemy/datatypes/__init__.py
--rw-r--r--   0 xushihao   (501) staff       (20)     4792 2023-03-27 08:38:41.000000 diengine-connect-0.1.5/diengine_connect/cc_sqlalchemy/datatypes/base.py
--rw-r--r--   0 xushihao   (501) staff       (20)    13531 2023-03-27 08:38:41.000000 diengine-connect-0.1.5/diengine_connect/cc_sqlalchemy/datatypes/sqltypes.py
-drwxr-xr-x   0 xushihao   (501) staff       (20)        0 2023-03-27 09:16:45.644409 diengine-connect-0.1.5/diengine_connect/cc_sqlalchemy/ddl/
--rw-r--r--   0 xushihao   (501) staff       (20)        0 2023-03-27 08:38:41.000000 diengine-connect-0.1.5/diengine_connect/cc_sqlalchemy/ddl/__init__.py
--rw-r--r--   0 xushihao   (501) staff       (20)     1599 2023-03-27 08:38:41.000000 diengine-connect-0.1.5/diengine_connect/cc_sqlalchemy/ddl/custom.py
--rw-r--r--   0 xushihao   (501) staff       (20)     7513 2023-03-27 08:38:41.000000 diengine-connect-0.1.5/diengine_connect/cc_sqlalchemy/ddl/tableengine.py
--rw-r--r--   0 xushihao   (501) staff       (20)     3515 2023-03-27 08:38:41.000000 diengine-connect-0.1.5/diengine_connect/cc_sqlalchemy/dialect.py
--rw-r--r--   0 xushihao   (501) staff       (20)     2513 2023-03-27 08:38:41.000000 diengine-connect-0.1.5/diengine_connect/cc_sqlalchemy/inspector.py
-drwxr-xr-x   0 xushihao   (501) staff       (20)        0 2023-03-27 09:16:45.644866 diengine-connect-0.1.5/diengine_connect/cc_sqlalchemy/sql/
--rw-r--r--   0 xushihao   (501) staff       (20)      458 2023-03-27 08:38:41.000000 diengine-connect-0.1.5/diengine_connect/cc_sqlalchemy/sql/__init__.py
--rw-r--r--   0 xushihao   (501) staff       (20)      884 2023-03-27 08:38:41.000000 diengine-connect-0.1.5/diengine_connect/cc_sqlalchemy/sql/ddlcompiler.py
--rw-r--r--   0 xushihao   (501) staff       (20)      281 2023-03-27 08:38:41.000000 diengine-connect-0.1.5/diengine_connect/cc_sqlalchemy/sql/preparer.py
-drwxr-xr-x   0 xushihao   (501) staff       (20)        0 2023-03-27 09:16:45.645233 diengine-connect-0.1.5/diengine_connect/cc_superset/
--rw-r--r--   0 xushihao   (501) staff       (20)        0 2023-03-27 08:38:41.000000 diengine-connect-0.1.5/diengine_connect/cc_superset/__init__.py
--rw-r--r--   0 xushihao   (501) staff       (20)     1228 2023-03-27 08:38:41.000000 diengine-connect-0.1.5/diengine_connect/cc_superset/datatypes.py
--rw-r--r--   0 xushihao   (501) staff       (20)     8404 2023-03-27 08:38:41.000000 diengine-connect-0.1.5/diengine_connect/cc_superset/engine.py
--rw-r--r--   0 xushihao   (501) staff       (20)     1989 2023-03-27 08:38:41.000000 diengine-connect-0.1.5/diengine_connect/common.py
-drwxr-xr-x   0 xushihao   (501) staff       (20)        0 2023-03-27 09:16:45.646897 diengine-connect-0.1.5/diengine_connect/datatypes/
--rw-r--r--   0 xushihao   (501) staff       (20)      297 2023-03-27 08:38:41.000000 diengine-connect-0.1.5/diengine_connect/datatypes/__init__.py
--rw-r--r--   0 xushihao   (501) staff       (20)    14636 2023-03-27 08:38:41.000000 diengine-connect-0.1.5/diengine_connect/datatypes/base.py
--rw-r--r--   0 xushihao   (501) staff       (20)     9238 2023-03-27 08:38:41.000000 diengine-connect-0.1.5/diengine_connect/datatypes/container.py
--rw-r--r--   0 xushihao   (501) staff       (20)     2558 2023-03-27 08:38:41.000000 diengine-connect-0.1.5/diengine_connect/datatypes/format.py
--rw-r--r--   0 xushihao   (501) staff       (20)     4649 2023-03-27 08:38:41.000000 diengine-connect-0.1.5/diengine_connect/datatypes/network.py
--rw-r--r--   0 xushihao   (501) staff       (20)    11078 2023-03-27 08:38:41.000000 diengine-connect-0.1.5/diengine_connect/datatypes/numeric.py
--rw-r--r--   0 xushihao   (501) staff       (20)     2352 2023-03-27 08:38:41.000000 diengine-connect-0.1.5/diengine_connect/datatypes/registry.py
--rw-r--r--   0 xushihao   (501) staff       (20)     3725 2023-03-27 08:38:41.000000 diengine-connect-0.1.5/diengine_connect/datatypes/special.py
--rw-r--r--   0 xushihao   (501) staff       (20)     5932 2023-03-27 08:38:41.000000 diengine-connect-0.1.5/diengine_connect/datatypes/string.py
--rw-r--r--   0 xushihao   (501) staff       (20)     8402 2023-03-27 08:38:41.000000 diengine-connect-0.1.5/diengine_connect/datatypes/temporal.py
-drwxr-xr-x   0 xushihao   (501) staff       (20)        0 2023-03-27 09:16:45.647471 diengine-connect-0.1.5/diengine_connect/dbapi/
--rw-r--r--   0 xushihao   (501) staff       (20)      880 2023-03-27 08:38:41.000000 diengine-connect-0.1.5/diengine_connect/dbapi/__init__.py
--rw-r--r--   0 xushihao   (501) staff       (20)     1525 2023-03-27 08:38:41.000000 diengine-connect-0.1.5/diengine_connect/dbapi/connection.py
--rw-r--r--   0 xushihao   (501) staff       (20)     4462 2023-03-27 08:38:41.000000 diengine-connect-0.1.5/diengine_connect/dbapi/cursor.py
-drwxr-xr-x   0 xushihao   (501) staff       (20)        0 2023-03-27 09:16:45.651922 diengine-connect-0.1.5/diengine_connect/driver/
--rw-r--r--   0 xushihao   (501) staff       (20)     6674 2023-03-27 08:38:41.000000 diengine-connect-0.1.5/diengine_connect/driver/__init__.py
--rw-r--r--   0 xushihao   (501) staff       (20)     4379 2023-03-27 08:38:41.000000 diengine-connect-0.1.5/diengine_connect/driver/buffer.py
--rw-r--r--   0 xushihao   (501) staff       (20)    34700 2023-03-27 08:50:35.000000 diengine-connect-0.1.5/diengine_connect/driver/client.py
--rw-r--r--   0 xushihao   (501) staff       (20)     6057 2023-03-27 08:38:41.000000 diengine-connect-0.1.5/diengine_connect/driver/common.py
--rw-r--r--   0 xushihao   (501) staff       (20)     1756 2023-03-27 08:38:41.000000 diengine-connect-0.1.5/diengine_connect/driver/compression.py
--rw-r--r--   0 xushihao   (501) staff       (20)       80 2023-03-27 08:38:41.000000 diengine-connect-0.1.5/diengine_connect/driver/constants.py
--rw-r--r--   0 xushihao   (501) staff       (20)     2410 2023-03-27 08:38:41.000000 diengine-connect-0.1.5/diengine_connect/driver/context.py
--rw-r--r--   0 xushihao   (501) staff       (20)     1316 2023-03-27 08:38:41.000000 diengine-connect-0.1.5/diengine_connect/driver/ctypes.py
--rw-r--r--   0 xushihao   (501) staff       (20)     3466 2023-03-27 08:38:41.000000 diengine-connect-0.1.5/diengine_connect/driver/dataconv.py
--rw-r--r--   0 xushihao   (501) staff       (20)      823 2023-03-27 08:38:41.000000 diengine-connect-0.1.5/diengine_connect/driver/ddl.py
--rw-r--r--   0 xushihao   (501) staff       (20)        0 2023-03-27 08:38:41.000000 diengine-connect-0.1.5/diengine_connect/driver/diengine.py
--rw-r--r--   0 xushihao   (501) staff       (20)     2842 2023-03-27 08:38:41.000000 diengine-connect-0.1.5/diengine_connect/driver/exceptions.py
--rw-r--r--   0 xushihao   (501) staff       (20)     7194 2023-03-27 08:38:41.000000 diengine-connect-0.1.5/diengine_connect/driver/extras.py
--rw-r--r--   0 xushihao   (501) staff       (20)    18878 2023-03-27 09:12:09.000000 diengine-connect-0.1.5/diengine_connect/driver/httpclient.py
--rw-r--r--   0 xushihao   (501) staff       (20)     6476 2023-03-27 08:38:41.000000 diengine-connect-0.1.5/diengine_connect/driver/httputil.py
--rw-r--r--   0 xushihao   (501) staff       (20)     6980 2023-03-27 08:38:41.000000 diengine-connect-0.1.5/diengine_connect/driver/insert.py
--rw-r--r--   0 xushihao   (501) staff       (20)      732 2023-03-27 08:38:41.000000 diengine-connect-0.1.5/diengine_connect/driver/models.py
--rw-r--r--   0 xushihao   (501) staff       (20)      312 2023-03-27 08:38:41.000000 diengine-connect-0.1.5/diengine_connect/driver/npconv.py
--rw-r--r--   0 xushihao   (501) staff       (20)     4232 2023-03-27 08:38:41.000000 diengine-connect-0.1.5/diengine_connect/driver/npquery.py
--rw-r--r--   0 xushihao   (501) staff       (20)      682 2023-03-27 08:38:41.000000 diengine-connect-0.1.5/diengine_connect/driver/options.py
--rw-r--r--   0 xushihao   (501) staff       (20)     5718 2023-03-27 08:38:41.000000 diengine-connect-0.1.5/diengine_connect/driver/parser.py
--rw-r--r--   0 xushihao   (501) staff       (20)    19957 2023-03-27 08:38:41.000000 diengine-connect-0.1.5/diengine_connect/driver/query.py
--rw-r--r--   0 xushihao   (501) staff       (20)      799 2023-03-27 08:38:41.000000 diengine-connect-0.1.5/diengine_connect/driver/tools.py
--rw-r--r--   0 xushihao   (501) staff       (20)     5371 2023-03-27 08:38:41.000000 diengine-connect-0.1.5/diengine_connect/driver/transform.py
--rw-r--r--   0 xushihao   (501) staff       (20)     1011 2023-03-27 08:38:41.000000 diengine-connect-0.1.5/diengine_connect/driver/types.py
-drwxr-xr-x   0 xushihao   (501) staff       (20)        0 2023-03-27 09:16:45.652046 diengine-connect-0.1.5/diengine_connect/driverc/
--rw-r--r--   0 xushihao   (501) staff       (20)        0 2023-03-27 08:38:41.000000 diengine-connect-0.1.5/diengine_connect/driverc/__init__.py
--rw-r--r--   0 xushihao   (501) staff       (20)     1294 2023-03-27 08:38:41.000000 diengine-connect-0.1.5/diengine_connect/entry_points.py
--rw-r--r--   0 xushihao   (501) staff       (20)     1306 2023-03-27 08:38:41.000000 diengine-connect-0.1.5/diengine_connect/json_impl.py
-drwxr-xr-x   0 xushihao   (501) staff       (20)        0 2023-03-27 09:16:45.642616 diengine-connect-0.1.5/diengine_connect.egg-info/
--rw-r--r--   0 xushihao   (501) staff       (20)     1336 2023-03-27 09:16:45.000000 diengine-connect-0.1.5/diengine_connect.egg-info/PKG-INFO
--rw-r--r--   0 xushihao   (501) staff       (20)     2554 2023-03-27 09:16:45.000000 diengine-connect-0.1.5/diengine_connect.egg-info/SOURCES.txt
--rw-r--r--   0 xushihao   (501) staff       (20)        1 2023-03-27 09:16:45.000000 diengine-connect-0.1.5/diengine_connect.egg-info/dependency_links.txt
--rw-r--r--   0 xushihao   (501) staff       (20)      263 2023-03-27 09:16:45.000000 diengine-connect-0.1.5/diengine_connect.egg-info/entry_points.txt
--rw-r--r--   0 xushihao   (501) staff       (20)        1 2023-03-27 09:16:45.000000 diengine-connect-0.1.5/diengine_connect.egg-info/not-zip-safe
--rw-r--r--   0 xushihao   (501) staff       (20)      179 2023-03-27 09:16:45.000000 diengine-connect-0.1.5/diengine_connect.egg-info/requires.txt
--rw-r--r--   0 xushihao   (501) staff       (20)       17 2023-03-27 09:16:45.000000 diengine-connect-0.1.5/diengine_connect.egg-info/top_level.txt
--rw-r--r--   0 xushihao   (501) staff       (20)      192 2023-03-27 08:38:41.000000 diengine-connect-0.1.5/pyproject.toml
--rw-r--r--   0 xushihao   (501) staff       (20)       38 2023-03-27 09:16:45.652396 diengine-connect-0.1.5/setup.cfg
--rw-r--r--   0 xushihao   (501) staff       (20)     3152 2023-03-27 08:38:41.000000 diengine-connect-0.1.5/setup.py
+drwxr-xr-x   0 xushihao   (501) staff       (20)        0 2023-04-06 12:23:05.241932 diengine-connect-0.1.6/
+-rw-r--r--   0 xushihao   (501) staff       (20)    11389 2023-04-06 12:01:46.000000 diengine-connect-0.1.6/LICENSE
+-rw-r--r--   0 xushihao   (501) staff       (20)     1336 2023-04-06 12:23:05.241757 diengine-connect-0.1.6/PKG-INFO
+-rw-r--r--   0 xushihao   (501) staff       (20)      315 2023-04-06 12:01:46.000000 diengine-connect-0.1.6/README.md
+drwxr-xr-x   0 xushihao   (501) staff       (20)        0 2023-04-06 12:23:05.231442 diengine-connect-0.1.6/diengine_connect/
+-rw-r--r--   0 xushihao   (501) staff       (20)        5 2023-04-06 12:21:42.000000 diengine-connect-0.1.6/diengine_connect/VERSION
+-rw-r--r--   0 xushihao   (501) staff       (20)      261 2023-04-06 12:15:24.000000 diengine-connect-0.1.6/diengine_connect/__init__.py
+drwxr-xr-x   0 xushihao   (501) staff       (20)        0 2023-04-06 12:23:05.233131 diengine-connect-0.1.6/diengine_connect/cc_sqlalchemy/
+-rw-r--r--   0 xushihao   (501) staff       (20)      200 2023-04-06 12:15:24.000000 diengine-connect-0.1.6/diengine_connect/cc_sqlalchemy/__init__.py
+drwxr-xr-x   0 xushihao   (501) staff       (20)        0 2023-04-06 12:23:05.233702 diengine-connect-0.1.6/diengine_connect/cc_sqlalchemy/datatypes/
+-rw-r--r--   0 xushihao   (501) staff       (20)       57 2023-04-06 12:15:24.000000 diengine-connect-0.1.6/diengine_connect/cc_sqlalchemy/datatypes/__init__.py
+-rw-r--r--   0 xushihao   (501) staff       (20)     4792 2023-04-06 12:15:24.000000 diengine-connect-0.1.6/diengine_connect/cc_sqlalchemy/datatypes/base.py
+-rw-r--r--   0 xushihao   (501) staff       (20)    13591 2023-04-06 12:15:24.000000 diengine-connect-0.1.6/diengine_connect/cc_sqlalchemy/datatypes/sqltypes.py
+drwxr-xr-x   0 xushihao   (501) staff       (20)        0 2023-04-06 12:23:05.234115 diengine-connect-0.1.6/diengine_connect/cc_sqlalchemy/ddl/
+-rw-r--r--   0 xushihao   (501) staff       (20)        0 2023-04-06 12:15:24.000000 diengine-connect-0.1.6/diengine_connect/cc_sqlalchemy/ddl/__init__.py
+-rw-r--r--   0 xushihao   (501) staff       (20)     1599 2023-04-06 12:15:24.000000 diengine-connect-0.1.6/diengine_connect/cc_sqlalchemy/ddl/custom.py
+-rw-r--r--   0 xushihao   (501) staff       (20)     7513 2023-04-06 12:15:24.000000 diengine-connect-0.1.6/diengine_connect/cc_sqlalchemy/ddl/tableengine.py
+-rw-r--r--   0 xushihao   (501) staff       (20)     3512 2023-04-06 12:15:24.000000 diengine-connect-0.1.6/diengine_connect/cc_sqlalchemy/dialect.py
+-rw-r--r--   0 xushihao   (501) staff       (20)     2435 2023-04-06 12:15:24.000000 diengine-connect-0.1.6/diengine_connect/cc_sqlalchemy/inspector.py
+drwxr-xr-x   0 xushihao   (501) staff       (20)        0 2023-04-06 12:23:05.234552 diengine-connect-0.1.6/diengine_connect/cc_sqlalchemy/sql/
+-rw-r--r--   0 xushihao   (501) staff       (20)      458 2023-04-06 12:15:24.000000 diengine-connect-0.1.6/diengine_connect/cc_sqlalchemy/sql/__init__.py
+-rw-r--r--   0 xushihao   (501) staff       (20)      884 2023-04-06 12:15:24.000000 diengine-connect-0.1.6/diengine_connect/cc_sqlalchemy/sql/ddlcompiler.py
+-rw-r--r--   0 xushihao   (501) staff       (20)      281 2023-04-06 12:15:24.000000 diengine-connect-0.1.6/diengine_connect/cc_sqlalchemy/sql/preparer.py
+drwxr-xr-x   0 xushihao   (501) staff       (20)        0 2023-04-06 12:23:05.234954 diengine-connect-0.1.6/diengine_connect/cc_superset/
+-rw-r--r--   0 xushihao   (501) staff       (20)        0 2023-04-06 12:15:24.000000 diengine-connect-0.1.6/diengine_connect/cc_superset/__init__.py
+-rw-r--r--   0 xushihao   (501) staff       (20)     1228 2023-04-06 12:15:24.000000 diengine-connect-0.1.6/diengine_connect/cc_superset/datatypes.py
+-rw-r--r--   0 xushihao   (501) staff       (20)     8404 2023-04-06 12:15:24.000000 diengine-connect-0.1.6/diengine_connect/cc_superset/engine.py
+-rw-r--r--   0 xushihao   (501) staff       (20)     1989 2023-04-06 12:15:24.000000 diengine-connect-0.1.6/diengine_connect/common.py
+drwxr-xr-x   0 xushihao   (501) staff       (20)        0 2023-04-06 12:23:05.236796 diengine-connect-0.1.6/diengine_connect/datatypes/
+-rw-r--r--   0 xushihao   (501) staff       (20)      297 2023-04-06 12:15:24.000000 diengine-connect-0.1.6/diengine_connect/datatypes/__init__.py
+-rw-r--r--   0 xushihao   (501) staff       (20)    14636 2023-04-06 12:15:24.000000 diengine-connect-0.1.6/diengine_connect/datatypes/base.py
+-rw-r--r--   0 xushihao   (501) staff       (20)     9238 2023-04-06 12:15:24.000000 diengine-connect-0.1.6/diengine_connect/datatypes/container.py
+-rw-r--r--   0 xushihao   (501) staff       (20)     2558 2023-04-06 12:15:24.000000 diengine-connect-0.1.6/diengine_connect/datatypes/format.py
+-rw-r--r--   0 xushihao   (501) staff       (20)     4649 2023-04-06 12:15:24.000000 diengine-connect-0.1.6/diengine_connect/datatypes/network.py
+-rw-r--r--   0 xushihao   (501) staff       (20)    11148 2023-04-06 12:15:24.000000 diengine-connect-0.1.6/diengine_connect/datatypes/numeric.py
+-rw-r--r--   0 xushihao   (501) staff       (20)     2352 2023-04-06 12:15:24.000000 diengine-connect-0.1.6/diengine_connect/datatypes/registry.py
+-rw-r--r--   0 xushihao   (501) staff       (20)     3725 2023-04-06 12:15:24.000000 diengine-connect-0.1.6/diengine_connect/datatypes/special.py
+-rw-r--r--   0 xushihao   (501) staff       (20)     5932 2023-04-06 12:15:24.000000 diengine-connect-0.1.6/diengine_connect/datatypes/string.py
+-rw-r--r--   0 xushihao   (501) staff       (20)     8402 2023-04-06 12:15:24.000000 diengine-connect-0.1.6/diengine_connect/datatypes/temporal.py
+drwxr-xr-x   0 xushihao   (501) staff       (20)        0 2023-04-06 12:23:05.237279 diengine-connect-0.1.6/diengine_connect/dbapi/
+-rw-r--r--   0 xushihao   (501) staff       (20)      880 2023-04-06 12:15:24.000000 diengine-connect-0.1.6/diengine_connect/dbapi/__init__.py
+-rw-r--r--   0 xushihao   (501) staff       (20)     1525 2023-04-06 12:15:24.000000 diengine-connect-0.1.6/diengine_connect/dbapi/connection.py
+-rw-r--r--   0 xushihao   (501) staff       (20)     4462 2023-04-06 12:15:24.000000 diengine-connect-0.1.6/diengine_connect/dbapi/cursor.py
+drwxr-xr-x   0 xushihao   (501) staff       (20)        0 2023-04-06 12:23:05.241233 diengine-connect-0.1.6/diengine_connect/driver/
+-rw-r--r--   0 xushihao   (501) staff       (20)     6674 2023-04-06 12:15:24.000000 diengine-connect-0.1.6/diengine_connect/driver/__init__.py
+-rw-r--r--   0 xushihao   (501) staff       (20)     4379 2023-04-06 12:15:24.000000 diengine-connect-0.1.6/diengine_connect/driver/buffer.py
+-rw-r--r--   0 xushihao   (501) staff       (20)    34700 2023-04-06 12:15:24.000000 diengine-connect-0.1.6/diengine_connect/driver/client.py
+-rw-r--r--   0 xushihao   (501) staff       (20)     6057 2023-04-06 12:15:24.000000 diengine-connect-0.1.6/diengine_connect/driver/common.py
+-rw-r--r--   0 xushihao   (501) staff       (20)     1756 2023-04-06 12:15:24.000000 diengine-connect-0.1.6/diengine_connect/driver/compression.py
+-rw-r--r--   0 xushihao   (501) staff       (20)       80 2023-04-06 12:15:24.000000 diengine-connect-0.1.6/diengine_connect/driver/constants.py
+-rw-r--r--   0 xushihao   (501) staff       (20)     2410 2023-04-06 12:15:24.000000 diengine-connect-0.1.6/diengine_connect/driver/context.py
+-rw-r--r--   0 xushihao   (501) staff       (20)     1316 2023-04-06 12:15:24.000000 diengine-connect-0.1.6/diengine_connect/driver/ctypes.py
+-rw-r--r--   0 xushihao   (501) staff       (20)     3466 2023-04-06 12:15:24.000000 diengine-connect-0.1.6/diengine_connect/driver/dataconv.py
+-rw-r--r--   0 xushihao   (501) staff       (20)      823 2023-04-06 12:15:24.000000 diengine-connect-0.1.6/diengine_connect/driver/ddl.py
+-rw-r--r--   0 xushihao   (501) staff       (20)        0 2023-04-06 12:15:24.000000 diengine-connect-0.1.6/diengine_connect/driver/diengine.py
+-rw-r--r--   0 xushihao   (501) staff       (20)     2842 2023-04-06 12:15:24.000000 diengine-connect-0.1.6/diengine_connect/driver/exceptions.py
+-rw-r--r--   0 xushihao   (501) staff       (20)     7194 2023-04-06 12:15:24.000000 diengine-connect-0.1.6/diengine_connect/driver/extras.py
+-rw-r--r--   0 xushihao   (501) staff       (20)    18878 2023-04-06 12:15:24.000000 diengine-connect-0.1.6/diengine_connect/driver/httpclient.py
+-rw-r--r--   0 xushihao   (501) staff       (20)     6476 2023-04-06 12:15:24.000000 diengine-connect-0.1.6/diengine_connect/driver/httputil.py
+-rw-r--r--   0 xushihao   (501) staff       (20)     6980 2023-04-06 12:15:24.000000 diengine-connect-0.1.6/diengine_connect/driver/insert.py
+-rw-r--r--   0 xushihao   (501) staff       (20)      732 2023-04-06 12:15:24.000000 diengine-connect-0.1.6/diengine_connect/driver/models.py
+-rw-r--r--   0 xushihao   (501) staff       (20)      312 2023-04-06 12:15:24.000000 diengine-connect-0.1.6/diengine_connect/driver/npconv.py
+-rw-r--r--   0 xushihao   (501) staff       (20)     4232 2023-04-06 12:15:24.000000 diengine-connect-0.1.6/diengine_connect/driver/npquery.py
+-rw-r--r--   0 xushihao   (501) staff       (20)      682 2023-04-06 12:15:24.000000 diengine-connect-0.1.6/diengine_connect/driver/options.py
+-rw-r--r--   0 xushihao   (501) staff       (20)     5718 2023-04-06 12:15:24.000000 diengine-connect-0.1.6/diengine_connect/driver/parser.py
+-rw-r--r--   0 xushihao   (501) staff       (20)    19957 2023-04-06 12:15:24.000000 diengine-connect-0.1.6/diengine_connect/driver/query.py
+-rw-r--r--   0 xushihao   (501) staff       (20)      799 2023-04-06 12:15:24.000000 diengine-connect-0.1.6/diengine_connect/driver/tools.py
+-rw-r--r--   0 xushihao   (501) staff       (20)     5424 2023-04-06 12:15:24.000000 diengine-connect-0.1.6/diengine_connect/driver/transform.py
+-rw-r--r--   0 xushihao   (501) staff       (20)     1011 2023-04-06 12:15:24.000000 diengine-connect-0.1.6/diengine_connect/driver/types.py
+drwxr-xr-x   0 xushihao   (501) staff       (20)        0 2023-04-06 12:23:05.241351 diengine-connect-0.1.6/diengine_connect/driverc/
+-rw-r--r--   0 xushihao   (501) staff       (20)        0 2023-04-06 12:15:24.000000 diengine-connect-0.1.6/diengine_connect/driverc/__init__.py
+-rw-r--r--   0 xushihao   (501) staff       (20)     1294 2023-04-06 12:15:24.000000 diengine-connect-0.1.6/diengine_connect/entry_points.py
+-rw-r--r--   0 xushihao   (501) staff       (20)     1306 2023-04-06 12:15:24.000000 diengine-connect-0.1.6/diengine_connect/json_impl.py
+drwxr-xr-x   0 xushihao   (501) staff       (20)        0 2023-04-06 12:23:05.232647 diengine-connect-0.1.6/diengine_connect.egg-info/
+-rw-r--r--   0 xushihao   (501) staff       (20)     1336 2023-04-06 12:23:05.000000 diengine-connect-0.1.6/diengine_connect.egg-info/PKG-INFO
+-rw-r--r--   0 xushihao   (501) staff       (20)     2570 2023-04-06 12:23:05.000000 diengine-connect-0.1.6/diengine_connect.egg-info/SOURCES.txt
+-rw-r--r--   0 xushihao   (501) staff       (20)        1 2023-04-06 12:23:05.000000 diengine-connect-0.1.6/diengine_connect.egg-info/dependency_links.txt
+-rw-r--r--   0 xushihao   (501) staff       (20)      263 2023-04-06 12:23:05.000000 diengine-connect-0.1.6/diengine_connect.egg-info/entry_points.txt
+-rw-r--r--   0 xushihao   (501) staff       (20)        1 2023-04-06 12:20:50.000000 diengine-connect-0.1.6/diengine_connect.egg-info/not-zip-safe
+-rw-r--r--   0 xushihao   (501) staff       (20)      179 2023-04-06 12:23:05.000000 diengine-connect-0.1.6/diengine_connect.egg-info/requires.txt
+-rw-r--r--   0 xushihao   (501) staff       (20)       17 2023-04-06 12:23:05.000000 diengine-connect-0.1.6/diengine_connect.egg-info/top_level.txt
+-rw-r--r--   0 xushihao   (501) staff       (20)      192 2023-04-06 12:01:46.000000 diengine-connect-0.1.6/pyproject.toml
+-rw-r--r--   0 xushihao   (501) staff       (20)       38 2023-04-06 12:23:05.241999 diengine-connect-0.1.6/setup.cfg
+-rw-r--r--   0 xushihao   (501) staff       (20)     3152 2023-04-06 12:01:46.000000 diengine-connect-0.1.6/setup.py
+drwxr-xr-x   0 xushihao   (501) staff       (20)        0 2023-04-06 12:23:05.241430 diengine-connect-0.1.6/tests/
+-rw-r--r--   0 xushihao   (501) staff       (20)      650 2023-04-06 12:01:46.000000 diengine-connect-0.1.6/tests/testCk.py
```

### Comparing `diengine-connect-0.1.5/LICENSE` & `diengine-connect-0.1.6/LICENSE`

 * *Files identical despite different names*

### Comparing `diengine-connect-0.1.5/PKG-INFO` & `diengine-connect-0.1.6/PKG-INFO`

 * *Files 6% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: diengine-connect
-Version: 0.1.5
+Version: 0.1.6
 Summary: Diengine core driver, SqlAlchemy, and Superset libraries
 Home-page: UNKNOWN
 Author: diengine Inc.
 License: Apache License 2.0
 Description: ## Diengine Connect
         
         A suite of Python packages for connecting Python to ClickHouse:
```

### Comparing `diengine-connect-0.1.5/diengine_connect/cc_sqlalchemy/datatypes/base.py` & `diengine-connect-0.1.6/diengine_connect/cc_sqlalchemy/datatypes/base.py`

 * *Files identical despite different names*

### Comparing `diengine-connect-0.1.5/diengine_connect/cc_sqlalchemy/datatypes/sqltypes.py` & `diengine-connect-0.1.6/diengine_connect/cc_sqlalchemy/datatypes/sqltypes.py`

 * *Files 1% similar despite different names*

```diff
@@ -93,15 +93,17 @@
         :param type_def: Parsed type def from ClickHouse arguments
         """
         if type_def:
             if self.dec_size:
                 precision = decimal_prec[self.dec_size]
                 scale = type_def.values[0]
             else:
-                precision, scale = type_def.values
+                precision = 0;
+                scale = 0;
+                # precision, scale = type_def.values
         elif not precision or scale < 0 or scale > precision:
             raise ArgumentError('Invalid precision or scale for ClickHouse Decimal type')
         else:
             type_def = TypeDef(values=(precision, scale))
         ChSqlaType.__init__(self, type_def)
         Numeric.__init__(self, precision, scale)
```

### Comparing `diengine-connect-0.1.5/diengine_connect/cc_sqlalchemy/ddl/custom.py` & `diengine-connect-0.1.6/diengine_connect/cc_sqlalchemy/ddl/custom.py`

 * *Files identical despite different names*

### Comparing `diengine-connect-0.1.5/diengine_connect/cc_sqlalchemy/ddl/tableengine.py` & `diengine-connect-0.1.6/diengine_connect/cc_sqlalchemy/ddl/tableengine.py`

 * *Files identical despite different names*

### Comparing `diengine-connect-0.1.5/diengine_connect/cc_sqlalchemy/dialect.py` & `diengine-connect-0.1.6/diengine_connect/cc_sqlalchemy/dialect.py`

 * *Files 1% similar despite different names*

```diff
@@ -77,17 +77,17 @@
     def get_unique_constraints(self, connection, table_name, schema=None, **kw):
         return []
 
     def get_check_constraints(self, connection, table_name, schema=None, **kw):
         return []
 
     def has_table(self, connection, table_name, schema=None, **_kw):
-        result = connection.execute(f'EXISTS TABLE {full_table(table_name, schema)}')
-        row = result.fetchone()
-        return row[0] == 1
+        # result = connection.execute(f'EXISTS TABLE {full_table(table_name, schema)}')
+        # row = result.fetchone()
+        return True
 
     def has_sequence(self, connection, sequence_name, schema=None, **_kw):
         return False
 
     def do_begin_twophase(self, connection, xid):
         raise NotImplementedError
```

### Comparing `diengine-connect-0.1.5/diengine_connect/cc_sqlalchemy/inspector.py` & `diengine-connect-0.1.6/diengine_connect/cc_sqlalchemy/inspector.py`

 * *Files 23% similar despite different names*

```diff
@@ -10,18 +10,18 @@
 
 ch_col_args = ('default_type', 'codec_expression', 'ttl_expression')
 
 
 def get_engine(connection, table_name, schema=None):
     result_set = connection.execute(
         f"SELECT engine_full FROM system.tables WHERE database = '{schema}' and name = '{table_name}'")
-    row = next(result_set, None)
-    if not row:
-        raise NoResultFound(f'Table {schema}.{table_name} does not exist')
-    return build_engine(row.engine_full)
+    # row = next(result_set, None)
+    # if not row:
+    #     raise NoResultFound(f'Table {schema}.{table_name} does not exist')
+    return build_engine("MergeTree")
 
 
 class ChInspector(Inspector):
 
     def reflect_table(self, table, include_columns, exclude_columns, *_args, **_kwargs):
         schema = table.schema
         for col in self.get_columns(table.name, schema):
@@ -36,22 +36,22 @@
     def get_columns(self, table_name, schema=None, **_kwargs):
         table_id = full_table(table_name, schema)
         result_set = self.bind.execute(f'DESCRIBE TABLE {table_id}')
         if not result_set:
             raise NoResultFound(f'Table {full_table} does not exist')
         columns = []
         for row in result_set:
-            sqla_type = sqla_type_from_name(row.type)
-            col = {'name': row.name,
+            sqla_type = sqla_type_from_name(row[1])
+            col = {'name': row[0],
                    'type': sqla_type,
-                   'nullable': sqla_type.nullable,
+                   'nullable': False,
                    'autoincrement': False,
-                   'default': row.default_expression,
-                   'default_type': row.default_type,
-                   'comment': row.comment,
-                   'codec_expression': row.codec_expression,
-                   'ttl_expression': row.ttl_expression}
+                   'default': None,
+                   'default_type': 'String',
+                   'comment': None,
+                   'codec_expression': None,
+                   'ttl_expression': None}
             columns.append(col)
         return columns
 
 
 ChInspector.reflecttable = ChInspector.reflect_table  # Hack to provide backward compatibility for SQLAlchemy 1.3
```

### Comparing `diengine-connect-0.1.5/diengine_connect/cc_sqlalchemy/sql/ddlcompiler.py` & `diengine-connect-0.1.6/diengine_connect/cc_sqlalchemy/sql/ddlcompiler.py`

 * *Files identical despite different names*

### Comparing `diengine-connect-0.1.5/diengine_connect/cc_superset/datatypes.py` & `diengine-connect-0.1.6/diengine_connect/cc_superset/datatypes.py`

 * *Files identical despite different names*

### Comparing `diengine-connect-0.1.5/diengine_connect/cc_superset/engine.py` & `diengine-connect-0.1.6/diengine_connect/cc_superset/engine.py`

 * *Files identical despite different names*

### Comparing `diengine-connect-0.1.5/diengine_connect/common.py` & `diengine-connect-0.1.6/diengine_connect/common.py`

 * *Files identical despite different names*

### Comparing `diengine-connect-0.1.5/diengine_connect/datatypes/base.py` & `diengine-connect-0.1.6/diengine_connect/datatypes/base.py`

 * *Files identical despite different names*

### Comparing `diengine-connect-0.1.5/diengine_connect/datatypes/container.py` & `diengine-connect-0.1.6/diengine_connect/datatypes/container.py`

 * *Files identical despite different names*

### Comparing `diengine-connect-0.1.5/diengine_connect/datatypes/format.py` & `diengine-connect-0.1.6/diengine_connect/datatypes/format.py`

 * *Files identical despite different names*

### Comparing `diengine-connect-0.1.5/diengine_connect/datatypes/network.py` & `diengine-connect-0.1.6/diengine_connect/datatypes/network.py`

 * *Files identical despite different names*

### Comparing `diengine-connect-0.1.5/diengine_connect/datatypes/numeric.py` & `diengine-connect-0.1.6/diengine_connect/datatypes/numeric.py`

 * *Files 0% similar despite different names*

```diff
@@ -241,17 +241,20 @@
     python_type = decimal.Decimal
     dec_size = 0
 
     @classmethod
     def build(cls: Type['Decimal'], type_def: TypeDef):
         size = cls.dec_size
         if size == 0:
-            prec = type_def.values[0]
-            scale = type_def.values[1]
-            size = decimal_size(prec)
+            # prec = type_def.values[0]
+            # scale = type_def.values[1]
+            # size = decimal_size(prec)
+            prec = 0
+            scale = 0
+            size = 1
         else:
             prec = decimal_prec[size]
             scale = type_def.values[0]
         type_cls = BigDecimal if size > 64 else Decimal
         return type_cls(type_def, prec, size, scale)
 
     def __init__(self, type_def: TypeDef, prec, size, scale):
```

### Comparing `diengine-connect-0.1.5/diengine_connect/datatypes/registry.py` & `diengine-connect-0.1.6/diengine_connect/datatypes/registry.py`

 * *Files identical despite different names*

### Comparing `diengine-connect-0.1.5/diengine_connect/datatypes/special.py` & `diengine-connect-0.1.6/diengine_connect/datatypes/special.py`

 * *Files identical despite different names*

### Comparing `diengine-connect-0.1.5/diengine_connect/datatypes/string.py` & `diengine-connect-0.1.6/diengine_connect/datatypes/string.py`

 * *Files identical despite different names*

### Comparing `diengine-connect-0.1.5/diengine_connect/datatypes/temporal.py` & `diengine-connect-0.1.6/diengine_connect/datatypes/temporal.py`

 * *Files identical despite different names*

### Comparing `diengine-connect-0.1.5/diengine_connect/dbapi/__init__.py` & `diengine-connect-0.1.6/diengine_connect/dbapi/__init__.py`

 * *Files identical despite different names*

### Comparing `diengine-connect-0.1.5/diengine_connect/dbapi/connection.py` & `diengine-connect-0.1.6/diengine_connect/dbapi/connection.py`

 * *Files identical despite different names*

### Comparing `diengine-connect-0.1.5/diengine_connect/dbapi/cursor.py` & `diengine-connect-0.1.6/diengine_connect/dbapi/cursor.py`

 * *Files identical despite different names*

### Comparing `diengine-connect-0.1.5/diengine_connect/driver/__init__.py` & `diengine-connect-0.1.6/diengine_connect/driver/__init__.py`

 * *Files identical despite different names*

### Comparing `diengine-connect-0.1.5/diengine_connect/driver/buffer.py` & `diengine-connect-0.1.6/diengine_connect/driver/buffer.py`

 * *Files identical despite different names*

### Comparing `diengine-connect-0.1.5/diengine_connect/driver/client.py` & `diengine-connect-0.1.6/diengine_connect/driver/client.py`

 * *Files identical despite different names*

### Comparing `diengine-connect-0.1.5/diengine_connect/driver/common.py` & `diengine-connect-0.1.6/diengine_connect/driver/common.py`

 * *Files identical despite different names*

### Comparing `diengine-connect-0.1.5/diengine_connect/driver/compression.py` & `diengine-connect-0.1.6/diengine_connect/driver/compression.py`

 * *Files identical despite different names*

### Comparing `diengine-connect-0.1.5/diengine_connect/driver/context.py` & `diengine-connect-0.1.6/diengine_connect/driver/context.py`

 * *Files identical despite different names*

### Comparing `diengine-connect-0.1.5/diengine_connect/driver/ctypes.py` & `diengine-connect-0.1.6/diengine_connect/driver/ctypes.py`

 * *Files identical despite different names*

### Comparing `diengine-connect-0.1.5/diengine_connect/driver/dataconv.py` & `diengine-connect-0.1.6/diengine_connect/driver/dataconv.py`

 * *Files identical despite different names*

### Comparing `diengine-connect-0.1.5/diengine_connect/driver/ddl.py` & `diengine-connect-0.1.6/diengine_connect/driver/ddl.py`

 * *Files identical despite different names*

### Comparing `diengine-connect-0.1.5/diengine_connect/driver/exceptions.py` & `diengine-connect-0.1.6/diengine_connect/driver/exceptions.py`

 * *Files identical despite different names*

### Comparing `diengine-connect-0.1.5/diengine_connect/driver/extras.py` & `diengine-connect-0.1.6/diengine_connect/driver/extras.py`

 * *Files identical despite different names*

### Comparing `diengine-connect-0.1.5/diengine_connect/driver/httpclient.py` & `diengine-connect-0.1.6/diengine_connect/driver/httpclient.py`

 * *Files identical despite different names*

### Comparing `diengine-connect-0.1.5/diengine_connect/driver/httputil.py` & `diengine-connect-0.1.6/diengine_connect/driver/httputil.py`

 * *Files identical despite different names*

### Comparing `diengine-connect-0.1.5/diengine_connect/driver/insert.py` & `diengine-connect-0.1.6/diengine_connect/driver/insert.py`

 * *Files identical despite different names*

### Comparing `diengine-connect-0.1.5/diengine_connect/driver/models.py` & `diengine-connect-0.1.6/diengine_connect/driver/models.py`

 * *Files identical despite different names*

### Comparing `diengine-connect-0.1.5/diengine_connect/driver/npquery.py` & `diengine-connect-0.1.6/diengine_connect/driver/npquery.py`

 * *Files identical despite different names*

### Comparing `diengine-connect-0.1.5/diengine_connect/driver/options.py` & `diengine-connect-0.1.6/diengine_connect/driver/options.py`

 * *Files identical despite different names*

### Comparing `diengine-connect-0.1.5/diengine_connect/driver/parser.py` & `diengine-connect-0.1.6/diengine_connect/driver/parser.py`

 * *Files identical despite different names*

### Comparing `diengine-connect-0.1.5/diengine_connect/driver/query.py` & `diengine-connect-0.1.6/diengine_connect/driver/query.py`

 * *Files identical despite different names*

### Comparing `diengine-connect-0.1.5/diengine_connect/driver/tools.py` & `diengine-connect-0.1.6/diengine_connect/driver/tools.py`

 * *Files identical despite different names*

### Comparing `diengine-connect-0.1.5/diengine_connect/driver/transform.py` & `diengine-connect-0.1.6/diengine_connect/driver/transform.py`

 * *Files 2% similar despite different names*

```diff
@@ -4,14 +4,15 @@
 from diengine_connect.driver.common import write_leb128
 from diengine_connect.driver.exceptions import StreamCompleteException, StreamFailureError
 from diengine_connect.driver.insert import InsertContext
 from diengine_connect.driver.npquery import NumpyResult
 from diengine_connect.driver.query import QueryResult, QueryContext
 from diengine_connect.driver.types import ByteSource
 from diengine_connect.driver.compression import get_compressor
+from diengine_connect.driver.models import ColumnDef
 
 _EMPTY_CTX = QueryContext()
 
 
 class NativeTransform:
 
     @staticmethod
```

### Comparing `diengine-connect-0.1.5/diengine_connect/driver/types.py` & `diengine-connect-0.1.6/diengine_connect/driver/types.py`

 * *Files identical despite different names*

### Comparing `diengine-connect-0.1.5/diengine_connect/entry_points.py` & `diengine-connect-0.1.6/diengine_connect/entry_points.py`

 * *Files identical despite different names*

### Comparing `diengine-connect-0.1.5/diengine_connect/json_impl.py` & `diengine-connect-0.1.6/diengine_connect/json_impl.py`

 * *Files identical despite different names*

### Comparing `diengine-connect-0.1.5/diengine_connect.egg-info/PKG-INFO` & `diengine-connect-0.1.6/diengine_connect.egg-info/PKG-INFO`

 * *Files 6% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: diengine-connect
-Version: 0.1.5
+Version: 0.1.6
 Summary: Diengine core driver, SqlAlchemy, and Superset libraries
 Home-page: UNKNOWN
 Author: diengine Inc.
 License: Apache License 2.0
 Description: ## Diengine Connect
         
         A suite of Python packages for connecting Python to ClickHouse:
```

### Comparing `diengine-connect-0.1.5/diengine_connect.egg-info/SOURCES.txt` & `diengine-connect-0.1.6/diengine_connect.egg-info/SOURCES.txt`

 * *Files 1% similar despite different names*

```diff
@@ -63,8 +63,9 @@
 diengine_connect/driver/npquery.py
 diengine_connect/driver/options.py
 diengine_connect/driver/parser.py
 diengine_connect/driver/query.py
 diengine_connect/driver/tools.py
 diengine_connect/driver/transform.py
 diengine_connect/driver/types.py
-diengine_connect/driverc/__init__.py
+diengine_connect/driverc/__init__.py
+tests/testCk.py
```

### Comparing `diengine-connect-0.1.5/setup.py` & `diengine-connect-0.1.6/setup.py`

 * *Files identical despite different names*

