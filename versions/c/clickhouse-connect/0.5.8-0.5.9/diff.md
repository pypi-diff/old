# Comparing `tmp/clickhouse-connect-0.5.8.tar.gz` & `tmp/clickhouse-connect-0.5.9.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "clickhouse-connect-0.5.8.tar", last modified: Fri Feb 10 18:49:03 2023, max compression
+gzip compressed data, was "clickhouse-connect-0.5.9.tar", last modified: Sat Feb 11 21:46:30 2023, max compression
```

## Comparing `clickhouse-connect-0.5.8.tar` & `clickhouse-connect-0.5.9.tar`

### file list

```diff
@@ -1,81 +1,81 @@
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-10 18:49:03.849518 clickhouse-connect-0.5.8/
--rw-r--r--   0 runner    (1001) docker     (123)    11389 2023-02-10 18:49:03.000000 clickhouse-connect-0.5.8/LICENSE
--rw-r--r--   0 runner    (1001) docker     (123)     1480 2023-02-10 18:49:03.849518 clickhouse-connect-0.5.8/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)      498 2023-02-10 18:49:03.000000 clickhouse-connect-0.5.8/README.md
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-10 18:49:03.845518 clickhouse-connect-0.5.8/clickhouse_connect/
--rw-r--r--   0 runner    (1001) docker     (123)        5 2023-02-10 18:49:03.000000 clickhouse-connect-0.5.8/clickhouse_connect/VERSION
--rw-r--r--   0 runner    (1001) docker     (123)      267 2023-02-10 18:49:03.000000 clickhouse-connect-0.5.8/clickhouse_connect/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-10 18:49:03.845518 clickhouse-connect-0.5.8/clickhouse_connect/cc_sqlalchemy/
--rw-r--r--   0 runner    (1001) docker     (123)      204 2023-02-10 18:49:03.000000 clickhouse-connect-0.5.8/clickhouse_connect/cc_sqlalchemy/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-10 18:49:03.845518 clickhouse-connect-0.5.8/clickhouse_connect/cc_sqlalchemy/datatypes/
--rw-r--r--   0 runner    (1001) docker     (123)       59 2023-02-10 18:49:03.000000 clickhouse-connect-0.5.8/clickhouse_connect/cc_sqlalchemy/datatypes/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     4798 2023-02-10 18:49:03.000000 clickhouse-connect-0.5.8/clickhouse_connect/cc_sqlalchemy/datatypes/base.py
--rw-r--r--   0 runner    (1001) docker     (123)    13539 2023-02-10 18:49:03.000000 clickhouse-connect-0.5.8/clickhouse_connect/cc_sqlalchemy/datatypes/sqltypes.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-10 18:49:03.849518 clickhouse-connect-0.5.8/clickhouse_connect/cc_sqlalchemy/ddl/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-10 18:49:03.000000 clickhouse-connect-0.5.8/clickhouse_connect/cc_sqlalchemy/ddl/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     1601 2023-02-10 18:49:03.000000 clickhouse-connect-0.5.8/clickhouse_connect/cc_sqlalchemy/ddl/custom.py
--rw-r--r--   0 runner    (1001) docker     (123)     7511 2023-02-10 18:49:03.000000 clickhouse-connect-0.5.8/clickhouse_connect/cc_sqlalchemy/ddl/tableengine.py
--rw-r--r--   0 runner    (1001) docker     (123)     3529 2023-02-10 18:49:03.000000 clickhouse-connect-0.5.8/clickhouse_connect/cc_sqlalchemy/dialect.py
--rw-r--r--   0 runner    (1001) docker     (123)     2521 2023-02-10 18:49:03.000000 clickhouse-connect-0.5.8/clickhouse_connect/cc_sqlalchemy/inspector.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-10 18:49:03.849518 clickhouse-connect-0.5.8/clickhouse_connect/cc_sqlalchemy/sql/
--rw-r--r--   0 runner    (1001) docker     (123)      460 2023-02-10 18:49:03.000000 clickhouse-connect-0.5.8/clickhouse_connect/cc_sqlalchemy/sql/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      888 2023-02-10 18:49:03.000000 clickhouse-connect-0.5.8/clickhouse_connect/cc_sqlalchemy/sql/ddlcompiler.py
--rw-r--r--   0 runner    (1001) docker     (123)      283 2023-02-10 18:49:03.000000 clickhouse-connect-0.5.8/clickhouse_connect/cc_sqlalchemy/sql/preparer.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-10 18:49:03.849518 clickhouse-connect-0.5.8/clickhouse_connect/cc_superset/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-10 18:49:03.000000 clickhouse-connect-0.5.8/clickhouse_connect/cc_superset/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     1232 2023-02-10 18:49:03.000000 clickhouse-connect-0.5.8/clickhouse_connect/cc_superset/datatypes.py
--rw-r--r--   0 runner    (1001) docker     (123)     8389 2023-02-10 18:49:03.000000 clickhouse-connect-0.5.8/clickhouse_connect/cc_superset/engine.py
--rw-r--r--   0 runner    (1001) docker     (123)     2012 2023-02-10 18:49:03.000000 clickhouse-connect-0.5.8/clickhouse_connect/common.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-10 18:49:03.849518 clickhouse-connect-0.5.8/clickhouse_connect/datatypes/
--rw-r--r--   0 runner    (1001) docker     (123)      311 2023-02-10 18:49:03.000000 clickhouse-connect-0.5.8/clickhouse_connect/datatypes/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    14080 2023-02-10 18:49:03.000000 clickhouse-connect-0.5.8/clickhouse_connect/datatypes/base.py
--rw-r--r--   0 runner    (1001) docker     (123)     9252 2023-02-10 18:49:03.000000 clickhouse-connect-0.5.8/clickhouse_connect/datatypes/container.py
--rw-r--r--   0 runner    (1001) docker     (123)     2562 2023-02-10 18:49:03.000000 clickhouse-connect-0.5.8/clickhouse_connect/datatypes/format.py
--rw-r--r--   0 runner    (1001) docker     (123)     4455 2023-02-10 18:49:03.000000 clickhouse-connect-0.5.8/clickhouse_connect/datatypes/network.py
--rw-r--r--   0 runner    (1001) docker     (123)     9609 2023-02-10 18:49:03.000000 clickhouse-connect-0.5.8/clickhouse_connect/datatypes/numeric.py
--rw-r--r--   0 runner    (1001) docker     (123)     2358 2023-02-10 18:49:03.000000 clickhouse-connect-0.5.8/clickhouse_connect/datatypes/registry.py
--rw-r--r--   0 runner    (1001) docker     (123)     3737 2023-02-10 18:49:03.000000 clickhouse-connect-0.5.8/clickhouse_connect/datatypes/special.py
--rw-r--r--   0 runner    (1001) docker     (123)     4058 2023-02-10 18:49:03.000000 clickhouse-connect-0.5.8/clickhouse_connect/datatypes/string.py
--rw-r--r--   0 runner    (1001) docker     (123)     7328 2023-02-10 18:49:03.000000 clickhouse-connect-0.5.8/clickhouse_connect/datatypes/temporal.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-10 18:49:03.849518 clickhouse-connect-0.5.8/clickhouse_connect/dbapi/
--rw-r--r--   0 runner    (1001) docker     (123)      882 2023-02-10 18:49:03.000000 clickhouse-connect-0.5.8/clickhouse_connect/dbapi/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     1531 2023-02-10 18:49:03.000000 clickhouse-connect-0.5.8/clickhouse_connect/dbapi/connection.py
--rw-r--r--   0 runner    (1001) docker     (123)     4368 2023-02-10 18:49:03.000000 clickhouse-connect-0.5.8/clickhouse_connect/dbapi/cursor.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-10 18:49:03.849518 clickhouse-connect-0.5.8/clickhouse_connect/driver/
--rw-r--r--   0 runner    (1001) docker     (123)     6324 2023-02-10 18:49:03.000000 clickhouse-connect-0.5.8/clickhouse_connect/driver/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     3704 2023-02-10 18:49:03.000000 clickhouse-connect-0.5.8/clickhouse_connect/driver/buffer.py
--rw-r--r--   0 runner    (1001) docker     (123)    32684 2023-02-10 18:49:03.000000 clickhouse-connect-0.5.8/clickhouse_connect/driver/client.py
--rw-r--r--   0 runner    (1001) docker     (123)     6068 2023-02-10 18:49:03.000000 clickhouse-connect-0.5.8/clickhouse_connect/driver/common.py
--rw-r--r--   0 runner    (1001) docker     (123)     1756 2023-02-10 18:49:03.000000 clickhouse-connect-0.5.8/clickhouse_connect/driver/compression.py
--rw-r--r--   0 runner    (1001) docker     (123)     2321 2023-02-10 18:49:03.000000 clickhouse-connect-0.5.8/clickhouse_connect/driver/context.py
--rw-r--r--   0 runner    (1001) docker     (123)     1295 2023-02-10 18:49:03.000000 clickhouse-connect-0.5.8/clickhouse_connect/driver/ctypes.py
--rw-r--r--   0 runner    (1001) docker     (123)     3024 2023-02-10 18:49:03.000000 clickhouse-connect-0.5.8/clickhouse_connect/driver/dataconv.py
--rw-r--r--   0 runner    (1001) docker     (123)      825 2023-02-10 18:49:03.000000 clickhouse-connect-0.5.8/clickhouse_connect/driver/ddl.py
--rw-r--r--   0 runner    (1001) docker     (123)     2628 2023-02-10 18:49:03.000000 clickhouse-connect-0.5.8/clickhouse_connect/driver/exceptions.py
--rw-r--r--   0 runner    (1001) docker     (123)     7212 2023-02-10 18:49:03.000000 clickhouse-connect-0.5.8/clickhouse_connect/driver/extras.py
--rw-r--r--   0 runner    (1001) docker     (123)    17318 2023-02-10 18:49:03.000000 clickhouse-connect-0.5.8/clickhouse_connect/driver/httpclient.py
--rw-r--r--   0 runner    (1001) docker     (123)     5396 2023-02-10 18:49:03.000000 clickhouse-connect-0.5.8/clickhouse_connect/driver/httputil.py
--rw-r--r--   0 runner    (1001) docker     (123)     6469 2023-02-10 18:49:03.000000 clickhouse-connect-0.5.8/clickhouse_connect/driver/insert.py
--rw-r--r--   0 runner    (1001) docker     (123)      634 2023-02-10 18:49:03.000000 clickhouse-connect-0.5.8/clickhouse_connect/driver/models.py
--rw-r--r--   0 runner    (1001) docker     (123)      316 2023-02-10 18:49:03.000000 clickhouse-connect-0.5.8/clickhouse_connect/driver/npconv.py
--rw-r--r--   0 runner    (1001) docker     (123)     4274 2023-02-10 18:49:03.000000 clickhouse-connect-0.5.8/clickhouse_connect/driver/npquery.py
--rw-r--r--   0 runner    (1001) docker     (123)      611 2023-02-10 18:49:03.000000 clickhouse-connect-0.5.8/clickhouse_connect/driver/options.py
--rw-r--r--   0 runner    (1001) docker     (123)     5720 2023-02-10 18:49:03.000000 clickhouse-connect-0.5.8/clickhouse_connect/driver/parser.py
--rw-r--r--   0 runner    (1001) docker     (123)    19216 2023-02-10 18:49:03.000000 clickhouse-connect-0.5.8/clickhouse_connect/driver/query.py
--rw-r--r--   0 runner    (1001) docker     (123)      803 2023-02-10 18:49:03.000000 clickhouse-connect-0.5.8/clickhouse_connect/driver/tools.py
--rw-r--r--   0 runner    (1001) docker     (123)     4269 2023-02-10 18:49:03.000000 clickhouse-connect-0.5.8/clickhouse_connect/driver/transform.py
--rw-r--r--   0 runner    (1001) docker     (123)      963 2023-02-10 18:49:03.000000 clickhouse-connect-0.5.8/clickhouse_connect/driver/types.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-10 18:49:03.849518 clickhouse-connect-0.5.8/clickhouse_connect/driverc/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-10 18:49:03.000000 clickhouse-connect-0.5.8/clickhouse_connect/driverc/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     1304 2023-02-10 18:49:03.000000 clickhouse-connect-0.5.8/clickhouse_connect/entry_points.py
--rw-r--r--   0 runner    (1001) docker     (123)     1305 2023-02-10 18:49:03.000000 clickhouse-connect-0.5.8/clickhouse_connect/json_impl.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-10 18:49:03.845518 clickhouse-connect-0.5.8/clickhouse_connect.egg-info/
--rw-r--r--   0 runner    (1001) docker     (123)     1480 2023-02-10 18:49:03.000000 clickhouse-connect-0.5.8/clickhouse_connect.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)     2568 2023-02-10 18:49:03.000000 clickhouse-connect-0.5.8/clickhouse_connect.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-02-10 18:49:03.000000 clickhouse-connect-0.5.8/clickhouse_connect.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (123)      281 2023-02-10 18:49:03.000000 clickhouse-connect-0.5.8/clickhouse_connect.egg-info/entry_points.txt
--rw-r--r--   0 runner    (1001) docker     (123)      179 2023-02-10 18:49:03.000000 clickhouse-connect-0.5.8/clickhouse_connect.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (123)       19 2023-02-10 18:49:03.000000 clickhouse-connect-0.5.8/clickhouse_connect.egg-info/top_level.txt
--rw-r--r--   0 runner    (1001) docker     (123)      192 2023-02-10 18:49:03.000000 clickhouse-connect-0.5.8/pyproject.toml
--rw-r--r--   0 runner    (1001) docker     (123)       38 2023-02-10 18:49:03.849518 clickhouse-connect-0.5.8/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (123)     3237 2023-02-10 18:49:03.000000 clickhouse-connect-0.5.8/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-11 21:46:30.639955 clickhouse-connect-0.5.9/
+-rw-r--r--   0 runner    (1001) docker     (123)    11389 2023-02-11 21:46:29.000000 clickhouse-connect-0.5.9/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (123)     1480 2023-02-11 21:46:30.639955 clickhouse-connect-0.5.9/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)      498 2023-02-11 21:46:29.000000 clickhouse-connect-0.5.9/README.md
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-11 21:46:30.631955 clickhouse-connect-0.5.9/clickhouse_connect/
+-rw-r--r--   0 runner    (1001) docker     (123)        5 2023-02-11 21:46:29.000000 clickhouse-connect-0.5.9/clickhouse_connect/VERSION
+-rw-r--r--   0 runner    (1001) docker     (123)      267 2023-02-11 21:46:29.000000 clickhouse-connect-0.5.9/clickhouse_connect/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-11 21:46:30.635955 clickhouse-connect-0.5.9/clickhouse_connect/cc_sqlalchemy/
+-rw-r--r--   0 runner    (1001) docker     (123)      204 2023-02-11 21:46:29.000000 clickhouse-connect-0.5.9/clickhouse_connect/cc_sqlalchemy/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-11 21:46:30.635955 clickhouse-connect-0.5.9/clickhouse_connect/cc_sqlalchemy/datatypes/
+-rw-r--r--   0 runner    (1001) docker     (123)       59 2023-02-11 21:46:29.000000 clickhouse-connect-0.5.9/clickhouse_connect/cc_sqlalchemy/datatypes/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4798 2023-02-11 21:46:29.000000 clickhouse-connect-0.5.9/clickhouse_connect/cc_sqlalchemy/datatypes/base.py
+-rw-r--r--   0 runner    (1001) docker     (123)    13539 2023-02-11 21:46:29.000000 clickhouse-connect-0.5.9/clickhouse_connect/cc_sqlalchemy/datatypes/sqltypes.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-11 21:46:30.635955 clickhouse-connect-0.5.9/clickhouse_connect/cc_sqlalchemy/ddl/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-11 21:46:29.000000 clickhouse-connect-0.5.9/clickhouse_connect/cc_sqlalchemy/ddl/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1601 2023-02-11 21:46:29.000000 clickhouse-connect-0.5.9/clickhouse_connect/cc_sqlalchemy/ddl/custom.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7511 2023-02-11 21:46:29.000000 clickhouse-connect-0.5.9/clickhouse_connect/cc_sqlalchemy/ddl/tableengine.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3529 2023-02-11 21:46:29.000000 clickhouse-connect-0.5.9/clickhouse_connect/cc_sqlalchemy/dialect.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2521 2023-02-11 21:46:29.000000 clickhouse-connect-0.5.9/clickhouse_connect/cc_sqlalchemy/inspector.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-11 21:46:30.635955 clickhouse-connect-0.5.9/clickhouse_connect/cc_sqlalchemy/sql/
+-rw-r--r--   0 runner    (1001) docker     (123)      460 2023-02-11 21:46:29.000000 clickhouse-connect-0.5.9/clickhouse_connect/cc_sqlalchemy/sql/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      888 2023-02-11 21:46:29.000000 clickhouse-connect-0.5.9/clickhouse_connect/cc_sqlalchemy/sql/ddlcompiler.py
+-rw-r--r--   0 runner    (1001) docker     (123)      283 2023-02-11 21:46:29.000000 clickhouse-connect-0.5.9/clickhouse_connect/cc_sqlalchemy/sql/preparer.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-11 21:46:30.635955 clickhouse-connect-0.5.9/clickhouse_connect/cc_superset/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-11 21:46:29.000000 clickhouse-connect-0.5.9/clickhouse_connect/cc_superset/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1232 2023-02-11 21:46:29.000000 clickhouse-connect-0.5.9/clickhouse_connect/cc_superset/datatypes.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8422 2023-02-11 21:46:29.000000 clickhouse-connect-0.5.9/clickhouse_connect/cc_superset/engine.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2012 2023-02-11 21:46:29.000000 clickhouse-connect-0.5.9/clickhouse_connect/common.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-11 21:46:30.635955 clickhouse-connect-0.5.9/clickhouse_connect/datatypes/
+-rw-r--r--   0 runner    (1001) docker     (123)      311 2023-02-11 21:46:29.000000 clickhouse-connect-0.5.9/clickhouse_connect/datatypes/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    14080 2023-02-11 21:46:29.000000 clickhouse-connect-0.5.9/clickhouse_connect/datatypes/base.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9252 2023-02-11 21:46:29.000000 clickhouse-connect-0.5.9/clickhouse_connect/datatypes/container.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2562 2023-02-11 21:46:29.000000 clickhouse-connect-0.5.9/clickhouse_connect/datatypes/format.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4455 2023-02-11 21:46:29.000000 clickhouse-connect-0.5.9/clickhouse_connect/datatypes/network.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9609 2023-02-11 21:46:29.000000 clickhouse-connect-0.5.9/clickhouse_connect/datatypes/numeric.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2358 2023-02-11 21:46:29.000000 clickhouse-connect-0.5.9/clickhouse_connect/datatypes/registry.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3737 2023-02-11 21:46:29.000000 clickhouse-connect-0.5.9/clickhouse_connect/datatypes/special.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4058 2023-02-11 21:46:29.000000 clickhouse-connect-0.5.9/clickhouse_connect/datatypes/string.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7328 2023-02-11 21:46:29.000000 clickhouse-connect-0.5.9/clickhouse_connect/datatypes/temporal.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-11 21:46:30.635955 clickhouse-connect-0.5.9/clickhouse_connect/dbapi/
+-rw-r--r--   0 runner    (1001) docker     (123)      882 2023-02-11 21:46:29.000000 clickhouse-connect-0.5.9/clickhouse_connect/dbapi/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1531 2023-02-11 21:46:29.000000 clickhouse-connect-0.5.9/clickhouse_connect/dbapi/connection.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4368 2023-02-11 21:46:29.000000 clickhouse-connect-0.5.9/clickhouse_connect/dbapi/cursor.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-11 21:46:30.639955 clickhouse-connect-0.5.9/clickhouse_connect/driver/
+-rw-r--r--   0 runner    (1001) docker     (123)     6333 2023-02-11 21:46:29.000000 clickhouse-connect-0.5.9/clickhouse_connect/driver/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4038 2023-02-11 21:46:29.000000 clickhouse-connect-0.5.9/clickhouse_connect/driver/buffer.py
+-rw-r--r--   0 runner    (1001) docker     (123)    32990 2023-02-11 21:46:29.000000 clickhouse-connect-0.5.9/clickhouse_connect/driver/client.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6061 2023-02-11 21:46:29.000000 clickhouse-connect-0.5.9/clickhouse_connect/driver/common.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1756 2023-02-11 21:46:29.000000 clickhouse-connect-0.5.9/clickhouse_connect/driver/compression.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2321 2023-02-11 21:46:29.000000 clickhouse-connect-0.5.9/clickhouse_connect/driver/context.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1295 2023-02-11 21:46:29.000000 clickhouse-connect-0.5.9/clickhouse_connect/driver/ctypes.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3024 2023-02-11 21:46:29.000000 clickhouse-connect-0.5.9/clickhouse_connect/driver/dataconv.py
+-rw-r--r--   0 runner    (1001) docker     (123)      825 2023-02-11 21:46:29.000000 clickhouse-connect-0.5.9/clickhouse_connect/driver/ddl.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2842 2023-02-11 21:46:29.000000 clickhouse-connect-0.5.9/clickhouse_connect/driver/exceptions.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7212 2023-02-11 21:46:29.000000 clickhouse-connect-0.5.9/clickhouse_connect/driver/extras.py
+-rw-r--r--   0 runner    (1001) docker     (123)    17491 2023-02-11 21:46:29.000000 clickhouse-connect-0.5.9/clickhouse_connect/driver/httpclient.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5190 2023-02-11 21:46:29.000000 clickhouse-connect-0.5.9/clickhouse_connect/driver/httputil.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6469 2023-02-11 21:46:29.000000 clickhouse-connect-0.5.9/clickhouse_connect/driver/insert.py
+-rw-r--r--   0 runner    (1001) docker     (123)      582 2023-02-11 21:46:29.000000 clickhouse-connect-0.5.9/clickhouse_connect/driver/models.py
+-rw-r--r--   0 runner    (1001) docker     (123)      316 2023-02-11 21:46:29.000000 clickhouse-connect-0.5.9/clickhouse_connect/driver/npconv.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4250 2023-02-11 21:46:29.000000 clickhouse-connect-0.5.9/clickhouse_connect/driver/npquery.py
+-rw-r--r--   0 runner    (1001) docker     (123)      611 2023-02-11 21:46:29.000000 clickhouse-connect-0.5.9/clickhouse_connect/driver/options.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5720 2023-02-11 21:46:29.000000 clickhouse-connect-0.5.9/clickhouse_connect/driver/parser.py
+-rw-r--r--   0 runner    (1001) docker     (123)    19354 2023-02-11 21:46:29.000000 clickhouse-connect-0.5.9/clickhouse_connect/driver/query.py
+-rw-r--r--   0 runner    (1001) docker     (123)      803 2023-02-11 21:46:29.000000 clickhouse-connect-0.5.9/clickhouse_connect/driver/tools.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4533 2023-02-11 21:46:29.000000 clickhouse-connect-0.5.9/clickhouse_connect/driver/transform.py
+-rw-r--r--   0 runner    (1001) docker     (123)      965 2023-02-11 21:46:29.000000 clickhouse-connect-0.5.9/clickhouse_connect/driver/types.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-11 21:46:30.639955 clickhouse-connect-0.5.9/clickhouse_connect/driverc/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-11 21:46:29.000000 clickhouse-connect-0.5.9/clickhouse_connect/driverc/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1304 2023-02-11 21:46:29.000000 clickhouse-connect-0.5.9/clickhouse_connect/entry_points.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1305 2023-02-11 21:46:29.000000 clickhouse-connect-0.5.9/clickhouse_connect/json_impl.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-11 21:46:30.635955 clickhouse-connect-0.5.9/clickhouse_connect.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)     1480 2023-02-11 21:46:30.000000 clickhouse-connect-0.5.9/clickhouse_connect.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     2568 2023-02-11 21:46:30.000000 clickhouse-connect-0.5.9/clickhouse_connect.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-02-11 21:46:30.000000 clickhouse-connect-0.5.9/clickhouse_connect.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)      281 2023-02-11 21:46:30.000000 clickhouse-connect-0.5.9/clickhouse_connect.egg-info/entry_points.txt
+-rw-r--r--   0 runner    (1001) docker     (123)      179 2023-02-11 21:46:30.000000 clickhouse-connect-0.5.9/clickhouse_connect.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       19 2023-02-11 21:46:30.000000 clickhouse-connect-0.5.9/clickhouse_connect.egg-info/top_level.txt
+-rw-r--r--   0 runner    (1001) docker     (123)      192 2023-02-11 21:46:29.000000 clickhouse-connect-0.5.9/pyproject.toml
+-rw-r--r--   0 runner    (1001) docker     (123)       38 2023-02-11 21:46:30.639955 clickhouse-connect-0.5.9/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (123)     3237 2023-02-11 21:46:29.000000 clickhouse-connect-0.5.9/setup.py
```

### Comparing `clickhouse-connect-0.5.8/LICENSE` & `clickhouse-connect-0.5.9/LICENSE`

 * *Files identical despite different names*

### Comparing `clickhouse-connect-0.5.8/PKG-INFO` & `clickhouse-connect-0.5.9/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: clickhouse-connect
-Version: 0.5.8
+Version: 0.5.9
 Summary: ClickHouse core driver, SqlAlchemy, and Superset libraries
 Home-page: https://github.com/ClickHouse/clickhouse-connect
 Author: ClickHouse Inc.
 Author-email: clients@clickhouse.com
 License: Apache License 2.0
 Keywords: clickhouse,superset,sqlalchemy,http,driver
 Platform: UNKNOWN
```

### Comparing `clickhouse-connect-0.5.8/clickhouse_connect/cc_sqlalchemy/datatypes/base.py` & `clickhouse-connect-0.5.9/clickhouse_connect/cc_sqlalchemy/datatypes/base.py`

 * *Files identical despite different names*

### Comparing `clickhouse-connect-0.5.8/clickhouse_connect/cc_sqlalchemy/datatypes/sqltypes.py` & `clickhouse-connect-0.5.9/clickhouse_connect/cc_sqlalchemy/datatypes/sqltypes.py`

 * *Files identical despite different names*

### Comparing `clickhouse-connect-0.5.8/clickhouse_connect/cc_sqlalchemy/ddl/custom.py` & `clickhouse-connect-0.5.9/clickhouse_connect/cc_sqlalchemy/ddl/custom.py`

 * *Files identical despite different names*

### Comparing `clickhouse-connect-0.5.8/clickhouse_connect/cc_sqlalchemy/ddl/tableengine.py` & `clickhouse-connect-0.5.9/clickhouse_connect/cc_sqlalchemy/ddl/tableengine.py`

 * *Files identical despite different names*

### Comparing `clickhouse-connect-0.5.8/clickhouse_connect/cc_sqlalchemy/dialect.py` & `clickhouse-connect-0.5.9/clickhouse_connect/cc_sqlalchemy/dialect.py`

 * *Files identical despite different names*

### Comparing `clickhouse-connect-0.5.8/clickhouse_connect/cc_sqlalchemy/inspector.py` & `clickhouse-connect-0.5.9/clickhouse_connect/cc_sqlalchemy/inspector.py`

 * *Files identical despite different names*

### Comparing `clickhouse-connect-0.5.8/clickhouse_connect/cc_sqlalchemy/sql/ddlcompiler.py` & `clickhouse-connect-0.5.9/clickhouse_connect/cc_sqlalchemy/sql/ddlcompiler.py`

 * *Files identical despite different names*

### Comparing `clickhouse-connect-0.5.8/clickhouse_connect/cc_superset/datatypes.py` & `clickhouse-connect-0.5.9/clickhouse_connect/cc_superset/datatypes.py`

 * *Files identical despite different names*

### Comparing `clickhouse-connect-0.5.8/clickhouse_connect/cc_superset/engine.py` & `clickhouse-connect-0.5.9/clickhouse_connect/cc_superset/engine.py`

 * *Files 1% similar despite different names*

```diff
@@ -98,15 +98,16 @@
 
     @classmethod
     def get_function_names(cls, database: Database) -> List[str]:
         if cls._function_names:
             return cls._function_names
         try:
             names = database.get_df(
-                'SELECT name FROM system.functions UNION ALL SELECT name FROM system.table_functions')['name'].tolist()
+                'SELECT name FROM system.functions UNION ALL ' +
+                'SELECT name FROM system.table_functions LIMIT 10000')['name'].tolist()
             cls._function_names = names
             return names
         except ClickHouseError:
             logger.exception('Error retrieving system.functions')
             return []
 
     @classmethod
```

### Comparing `clickhouse-connect-0.5.8/clickhouse_connect/common.py` & `clickhouse-connect-0.5.9/clickhouse_connect/common.py`

 * *Files identical despite different names*

### Comparing `clickhouse-connect-0.5.8/clickhouse_connect/datatypes/base.py` & `clickhouse-connect-0.5.9/clickhouse_connect/datatypes/base.py`

 * *Files identical despite different names*

### Comparing `clickhouse-connect-0.5.8/clickhouse_connect/datatypes/container.py` & `clickhouse-connect-0.5.9/clickhouse_connect/datatypes/container.py`

 * *Files identical despite different names*

### Comparing `clickhouse-connect-0.5.8/clickhouse_connect/datatypes/format.py` & `clickhouse-connect-0.5.9/clickhouse_connect/datatypes/format.py`

 * *Files identical despite different names*

### Comparing `clickhouse-connect-0.5.8/clickhouse_connect/datatypes/network.py` & `clickhouse-connect-0.5.9/clickhouse_connect/datatypes/network.py`

 * *Files identical despite different names*

### Comparing `clickhouse-connect-0.5.8/clickhouse_connect/datatypes/numeric.py` & `clickhouse-connect-0.5.9/clickhouse_connect/datatypes/numeric.py`

 * *Files identical despite different names*

### Comparing `clickhouse-connect-0.5.8/clickhouse_connect/datatypes/registry.py` & `clickhouse-connect-0.5.9/clickhouse_connect/datatypes/registry.py`

 * *Files identical despite different names*

### Comparing `clickhouse-connect-0.5.8/clickhouse_connect/datatypes/special.py` & `clickhouse-connect-0.5.9/clickhouse_connect/datatypes/special.py`

 * *Files identical despite different names*

### Comparing `clickhouse-connect-0.5.8/clickhouse_connect/datatypes/string.py` & `clickhouse-connect-0.5.9/clickhouse_connect/datatypes/string.py`

 * *Files identical despite different names*

### Comparing `clickhouse-connect-0.5.8/clickhouse_connect/datatypes/temporal.py` & `clickhouse-connect-0.5.9/clickhouse_connect/datatypes/temporal.py`

 * *Files identical despite different names*

### Comparing `clickhouse-connect-0.5.8/clickhouse_connect/dbapi/__init__.py` & `clickhouse-connect-0.5.9/clickhouse_connect/dbapi/__init__.py`

 * *Files identical despite different names*

### Comparing `clickhouse-connect-0.5.8/clickhouse_connect/dbapi/connection.py` & `clickhouse-connect-0.5.9/clickhouse_connect/dbapi/connection.py`

 * *Files identical despite different names*

### Comparing `clickhouse-connect-0.5.8/clickhouse_connect/dbapi/cursor.py` & `clickhouse-connect-0.5.9/clickhouse_connect/dbapi/cursor.py`

 * *Files identical despite different names*

### Comparing `clickhouse-connect-0.5.8/clickhouse_connect/driver/__init__.py` & `clickhouse-connect-0.5.9/clickhouse_connect/driver/__init__.py`

 * *Files 5% similar despite different names*

```diff
@@ -44,15 +44,15 @@
     :param compress: Enable compression for ClickHouse HTTP inserts and query results.  True will select the preferred
       compression method (lz4).  A str of 'lz4', 'zstd', 'brotli', or 'gzip' can be used to use a specific compression type
     :param query_limit: Default LIMIT on returned rows.  0 means no limit
     :param connect_timeout:  Timeout in seconds for the http connection
     :param send_receive_timeout: Read timeout in seconds for http connection
     :param client_name: client_name prepended to the HTTP User Agent header. Set this to track client queries
       in the ClickHouse system.query_log.
-    :param send_progress: Ask ClickHouse to send progress headers.  Used for summary and keep alive
+    :param send_progress: Deprecated, has no effect.  Previous functionality is now automatically determined
     :param verify: Verify the server certificate in secure/https mode
     :param ca_cert: If verify is True, the file path to Certificate Authority root to validate ClickHouse server
      certificate, in .pem format.  Ignored if verify is False.  This is not necessary if the ClickHouse server
      certificate is trusted by the operating system.  To trust the maintained list of "global" public root
      certificates maintained by the Python 'certifi' package, set ca_cert to 'certifi'
     :param client_cert: File path to a TLS Client certificate in .pem format.  This file should contain any
       applicable intermediate certificates
```

### Comparing `clickhouse-connect-0.5.8/clickhouse_connect/driver/buffer.py` & `clickhouse-connect-0.5.9/clickhouse_connect/driver/buffer.py`

 * *Files 8% similar despite different names*

```diff
@@ -1,11 +1,12 @@
 import sys
 import array
 from typing import Any, Iterable
 
+from clickhouse_connect.driver.exceptions import StreamCompleteException
 from clickhouse_connect.driver.types import ByteSource
 
 must_swap = sys.byteorder == 'big'
 
 
 class ResponseBuffer(ByteSource):
     slots = 'slice_sz', 'buf_loc', 'end', 'gen', 'buffer', 'slice'
@@ -23,15 +24,17 @@
             self.buf_loc += sz
             return self.buffer[self.buf_loc - sz: self.buf_loc]
         # Create a temporary buffer that bridges two or more source chunks
         bridge = bytearray(self.buffer[self.buf_loc: self.buf_sz])
         self.buf_loc = 0
         self.buf_sz = 0
         while len(bridge) < sz:
-            chunk = next(self.gen)
+            chunk = next(self.gen, None)
+            if not chunk:
+                raise StreamCompleteException
             x = len(chunk)
             if len(bridge) + x <= sz:
                 bridge.extend(chunk)
             else:
                 tail = sz - len(bridge)
                 bridge.extend(chunk[:tail])
                 self.buffer = chunk
@@ -41,15 +44,17 @@
 
     def read_byte(self) -> int:
         if self.buf_loc < self.buf_sz:
             self.buf_loc += 1
             return self.buffer[self.buf_loc - 1]
         self.buf_sz = 0
         self.buf_loc = 0
-        chunk = next(self.gen)
+        chunk = next(self.gen, None)
+        if not chunk:
+            raise StreamCompleteException
         x = len(chunk)
         if x > 1:
             self.buffer = chunk
             self.buf_loc = 1
             self.buf_sz = x
         return chunk[0]
 
@@ -109,11 +114,17 @@
         sz = column.itemsize * num_rows
         b = self.read_bytes(sz)
         column.frombytes(b)
         if must_swap:
             column.byteswap()
         return column
 
-    def close(self, ex: Exception = None):
+    @property
+    def last_message(self):
+        if len(self.buffer) == 0:
+            return None
+        return self.buffer.decode()
+
+    def close(self):
         if self.source:
-            self.source.close(ex)
+            self.source.close()
             self.source = None
```

### Comparing `clickhouse-connect-0.5.8/clickhouse_connect/driver/client.py` & `clickhouse-connect-0.5.9/clickhouse_connect/driver/client.py`

 * *Files 1% similar despite different names*

```diff
@@ -45,15 +45,15 @@
         self.server_tz = pytz.UTC
         self.server_version, server_tz, self.database = \
             tuple(self.command('SELECT version(), timezone(), database()', use_database=False))
         try:
             self.server_tz = pytz.timezone(server_tz)
         except UnknownTimeZoneError:
             logger.warning('Warning, server is using an unrecognized timezone %s, will use UTC default', server_tz)
-        server_settings = self.query('SELECT name, value, changed, description, type, readonly FROM system.settings')
+        server_settings = self.query('SELECT name, value, readonly FROM system.settings LIMIT 10000')
         self.server_settings = {row['name']: SettingDef(**row) for row in server_settings.named_results()}
         if database and not database == '__default__':
             self.database = database
         self.uri = uri
 
     def _validate_settings(self, settings: Optional[Dict[str, Any]]) -> Dict[str, str]:
         """
@@ -155,15 +155,15 @@
                                   query_tz: Optional[Union[str, tzinfo]] = None,
                                   column_tzs: Optional[Dict[str, Union[str, tzinfo]]] = None) -> StreamContext:
         """
         Variation of main query method that returns a stream of column oriented blocks. For
         parameters, see the create_query_context method.
         :return: StreamContext -- Iterable stream context that returns column oriented blocks
         """
-        return self._context_query(locals(), use_numpy=False).column_block_stream
+        return self._context_query(locals(), use_numpy=False, streaming=True).column_block_stream
 
     def query_row_block_stream(self,
                                query: str = None,
                                parameters: Optional[Union[Sequence, Dict[str, Any]]] = None,
                                settings: Optional[Dict[str, Any]] = None,
                                query_formats: Optional[Dict[str, str]] = None,
                                column_formats: Optional[Dict[str, Union[str, Dict[str, str]]]] = None,
@@ -173,15 +173,15 @@
                                query_tz: Optional[Union[str, tzinfo]] = None,
                                column_tzs: Optional[Dict[str, Union[str, tzinfo]]] = None) -> StreamContext:
         """
         Variation of main query method that returns a stream of row oriented blocks. For
         parameters, see the create_query_context method.
         :return: StreamContext -- Iterable stream context that returns blocks of rows
         """
-        return self._context_query(locals(), use_numpy=False).row_block_stream
+        return self._context_query(locals(), use_numpy=False, streaming=True).row_block_stream
 
     def query_rows_stream(self,
                           query: str = None,
                           parameters: Optional[Union[Sequence, Dict[str, Any]]] = None,
                           settings: Optional[Dict[str, Any]] = None,
                           query_formats: Optional[Dict[str, str]] = None,
                           column_formats: Optional[Dict[str, Union[str, Dict[str, str]]]] = None,
@@ -191,15 +191,15 @@
                           query_tz: Optional[Union[str, tzinfo]] = None,
                           column_tzs: Optional[Dict[str, Union[str, tzinfo]]] = None) -> StreamContext:
         """
         Variation of main query method that returns a stream of row oriented blocks. For
         parameters, see the create_query_context method.
         :return: StreamContext -- Iterable stream context that returns blocks of rows
         """
-        return self._context_query(locals(), use_numpy=False).rows_stream
+        return self._context_query(locals(), use_numpy=False, streaming=True).rows_stream
 
     @abstractmethod
     def raw_query(self, query: str,
                   parameters: Optional[Union[Sequence, Dict[str, Any]]] = None,
                   settings: Optional[Dict[str, Any]] = None,
                   fmt: str = None) -> bytes:
         """
@@ -241,15 +241,15 @@
                         max_str_len: Optional[int] = None,
                         context: QueryContext = None) -> StreamContext:
         """
         Query method that returns the results as a stream of numpy arrays.  For parameter values, see the
         create_query_context method
         :return: Generator that yield a numpy array per block representing the result set
         """
-        return self._context_query(locals(), use_numpy=True).np_stream
+        return self._context_query(locals(), use_numpy=True, streaming=True).np_stream
 
     # pylint: disable=duplicate-code,too-many-arguments,unused-argument
     def query_df(self,
                  query: str = None,
                  parameters: Optional[Union[Sequence, Dict[str, Any]]] = None,
                  settings: Optional[Dict[str, Any]] = None,
                  query_formats: Optional[Dict[str, str]] = None,
@@ -277,30 +277,31 @@
                         max_str_len: Optional[int] = None,
                         context: QueryContext = None) -> StreamContext:
         """
         Query method that returns the results as a StreamContext.  For parameter values, see the
         create_query_context method
         :return: Pandas dataframe representing the result set
         """
-        return self._context_query(locals(), use_numpy=True).df_stream
+        return self._context_query(locals(), use_numpy=True, streaming=True).df_stream
 
     def create_query_context(self,
                              query: str = None,
                              parameters: Optional[Union[Sequence, Dict[str, Any]]] = None,
                              settings: Optional[Dict[str, Any]] = None,
                              query_formats: Optional[Dict[str, str]] = None,
                              column_formats: Optional[Dict[str, Union[str, Dict[str, str]]]] = None,
                              encoding: Optional[str] = None,
                              use_none: Optional[bool] = None,
                              column_oriented: Optional[bool] = None,
                              use_numpy: Optional[bool] = False,
                              max_str_len: Optional[int] = 0,
                              context: Optional[QueryContext] = None,
                              query_tz: Optional[Union[str, tzinfo]] = None,
-                             column_tzs: Optional[Dict[str, Union[str, tzinfo]]] = None) -> QueryContext:
+                             column_tzs: Optional[Dict[str, Union[str, tzinfo]]] = None,
+                             streaming: bool = False) -> QueryContext:
         """
         Creates or updates a reusable QueryContext object
         :param query: Query statement/format string
         :param parameters: Optional dictionary used to format the query
         :param settings: Optional dictionary of ClickHouse settings (key/string values)
         :param query_formats: See QueryContext __init__ docstring
         :param column_formats: See QueryContext __init__ docstring
@@ -315,14 +316,15 @@
           String columns will always be object arrays
         :param context: An existing QueryContext to be updated with any provided parameter values
         :param query_tz  Either a string or a pytz tzinfo object.  (Strings will be converted to tzinfo objects).
           Values for any DateTime or DateTime64 column in the query will be converted to Python datetime.datetime
           objects with the selected timezone.
         :param column_tzs A dictionary of column names to tzinfo objects (or strings that will be converted to
           tzinfo objects).  The timezone will be applied to datetime objects returned in the query
+        :param streaming Marker used to correctly configure streaming queries
         :return: Reusable QueryContext
         """
         if context:
             return context.updated_copy(query=query,
                                         parameters=parameters,
                                         settings=settings,
                                         query_formats=query_formats,
@@ -330,15 +332,16 @@
                                         encoding=encoding,
                                         server_tz=self.server_tz,
                                         use_none=use_none,
                                         column_oriented=column_oriented,
                                         use_numpy=use_numpy,
                                         max_str_len=max_str_len,
                                         query_tz=query_tz,
-                                        column_tzs=column_tzs)
+                                        column_tzs=column_tzs,
+                                        streaming=streaming)
         # By default, a numpy context doesn't use None/NULL.  If NULL values are allowed, all numpy arrays must
         # be inefficient Object arrays
         if use_numpy and use_none is None:
             use_none = False
         if use_numpy and max_str_len is None:
             max_str_len = 0
         return QueryContext(query=query,
@@ -349,15 +352,16 @@
                             encoding=encoding,
                             server_tz=self.server_tz,
                             use_none=use_none,
                             column_oriented=column_oriented,
                             use_numpy=use_numpy,
                             max_str_len=max_str_len,
                             query_tz=query_tz,
-                            column_tzs=column_tzs)
+                            column_tzs=column_tzs,
+                            streaming=streaming)
 
     def query_arrow(self,
                     query: str,
                     parameters: Optional[Union[Sequence, Dict[str, Any]]] = None,
                     settings: Optional[Dict[str, Any]] = None,
                     use_strings: bool = True):
         """
```

### Comparing `clickhouse-connect-0.5.8/clickhouse_connect/driver/common.py` & `clickhouse-connect-0.5.9/clickhouse_connect/driver/common.py`

 * *Files 0% similar despite different names*

```diff
@@ -199,9 +199,9 @@
         if not self.gen:
             raise StreamClosedError
         self._in_context = True
         return self
 
     def __exit__(self, exc_type, exc_val, exc_tb):
         self._in_context = False
-        self.source.close(exc_val)
+        self.source.close()
         self.gen = None
```

### Comparing `clickhouse-connect-0.5.8/clickhouse_connect/driver/compression.py` & `clickhouse-connect-0.5.9/clickhouse_connect/driver/compression.py`

 * *Files identical despite different names*

### Comparing `clickhouse-connect-0.5.8/clickhouse_connect/driver/context.py` & `clickhouse-connect-0.5.9/clickhouse_connect/driver/context.py`

 * *Files identical despite different names*

### Comparing `clickhouse-connect-0.5.8/clickhouse_connect/driver/ctypes.py` & `clickhouse-connect-0.5.9/clickhouse_connect/driver/ctypes.py`

 * *Files identical despite different names*

### Comparing `clickhouse-connect-0.5.8/clickhouse_connect/driver/dataconv.py` & `clickhouse-connect-0.5.9/clickhouse_connect/driver/dataconv.py`

 * *Files identical despite different names*

### Comparing `clickhouse-connect-0.5.8/clickhouse_connect/driver/ddl.py` & `clickhouse-connect-0.5.9/clickhouse_connect/driver/ddl.py`

 * *Files identical despite different names*

### Comparing `clickhouse-connect-0.5.8/clickhouse_connect/driver/exceptions.py` & `clickhouse-connect-0.5.9/clickhouse_connect/driver/exceptions.py`

 * *Files 8% similar despite different names*

```diff
@@ -70,7 +70,15 @@
 
 
 class StreamClosedError(ProgrammingError):
     """Exception raised when a stream operation is executed on a closed stream."""
 
     def __init__(self):
         super().__init__('Executing a streaming operation on a closed stream')
+
+
+class StreamCompleteException(Exception):
+    """ Internal exception used to indicate the end of a ClickHouse query result stream."""
+
+
+class StreamFailureError(Exception):
+    """ Stream failed unexpectedly """
```

### Comparing `clickhouse-connect-0.5.8/clickhouse_connect/driver/extras.py` & `clickhouse-connect-0.5.9/clickhouse_connect/driver/extras.py`

 * *Files identical despite different names*

### Comparing `clickhouse-connect-0.5.8/clickhouse_connect/driver/httpclient.py` & `clickhouse-connect-0.5.9/clickhouse_connect/driver/httpclient.py`

 * *Files 3% similar despite different names*

```diff
@@ -35,15 +35,15 @@
     params = {}
     valid_transport_settings = {'database', 'buffer_size', 'session_id', 'compress', 'decompress',
                                 'session_timeout', 'session_check', 'query_id', 'quota_key', 'wait_end_of_query',
                                 'clickhouse_protocol_version'}
     optional_transport_settings = {'send_progress_in_http_headers', 'http_headers_progress_interval_ms',
                                    'enable_http_compression'}
 
-    # pylint: disable=too-many-arguments,too-many-locals,too-many-branches,too-many-statements
+    # pylint: disable=too-many-arguments,too-many-locals,too-many-branches,too-many-statements,unused-argument
     def __init__(self,
                  interface: str,
                  host: str,
                  port: int,
                  username: str,
                  password: str,
                  database: str,
@@ -94,30 +94,22 @@
             else:
                 self.http = default_pool_manager
 
         if not client_cert and username:
             self.headers['Authorization'] = 'Basic ' + b64encode(f'{username}:{password}'.encode()).decode()
         self.headers['User-Agent'] = common.build_client_name(client_name)
         self._read_format = self._write_format = 'Native'
+        self._progress_interval =  str(min(120000, (send_receive_timeout - 5) * 1000))
         self._transform = NativeTransform()
 
         connect_timeout, send_receive_timeout = coerce_int(connect_timeout), coerce_int(send_receive_timeout)
         self.timeout = Timeout(connect=connect_timeout, read=send_receive_timeout)
         self.query_retries = coerce_int(query_retries)
         self.http_retries = 1
 
-        if coerce_bool(send_progress):
-            ch_settings['wait_end_of_query'] = '1'
-            # We can't actually read the progress headers, but we enable them so ClickHouse sends data
-            # to keep the connection alive when waiting for long-running queries that don't return data
-            # Accordingly we make sure it's always less than the read timeout
-            ch_settings['send_progress_in_http_headers'] = '1'
-            progress_interval = min(120000, (send_receive_timeout - 5) * 1000)
-            ch_settings['http_headers_progress_interval_ms'] = str(progress_interval)
-
         if session_id:
             ch_settings['session_id'] = session_id
         elif 'session_id' not in ch_settings and common.get_setting('autogenerate_session_id'):
             ch_settings['session_id'] = str(uuid.uuid1())
 
         if coerce_bool(compress):
             compression = ','.join(available_compression)
@@ -176,16 +168,20 @@
                 names.append(col['name'])
                 types.append(registry.get_from_name(col['type']))
             return QueryResult([], None, tuple(names), tuple(types))
 
         if self.compression:
             headers['Accept-Encoding'] = self.compression
             params['enable_http_compression'] = '1'
-        response = self._raw_request(self._prep_query(context), params, headers, stream=True,
-                                     retries=self.query_retries)
+        response = self._raw_request(self._prep_query(context),
+                                     params,
+                                     headers,
+                                     stream=True,
+                                     retries=self.query_retries,
+                                     server_wait=not context.streaming)
         byte_source = RespBuffCls(ResponseSource(response))  # pylint: disable=not-callable
         query_result = self._transform.parse_response(byte_source, context)
         if 'X-ClickHouse-Summary' in response.headers:
             try:
                 summary = json.loads(response.headers['X-ClickHouse-Summary'])
                 query_result.summary = summary
             except json.JSONDecodeError:
@@ -235,15 +231,15 @@
         write_format = fmt if fmt else self._write_format
         headers = {'Content-Type': 'application/octet-stream'}
         if compression:
             headers['Content-Encoding'] = compression
         cols = f" ({', '.join([quote_identifier(x) for x in column_names])})" if column_names is not None else ''
         params = {'query': f'INSERT INTO {table}{cols} FORMAT {write_format}'}
         if self.database:
-            params['database'] =  self.database
+            params['database'] = self.database
         params.update(self._validate_settings(settings or {}))
         response = self._raw_request(insert_block, params, headers, error_handler=status_handler)
         logger.debug('Insert response code: %d, content: %s', response.status, response.data)
 
     def command(self,
                 cmd,
                 parameters: Optional[Union[Sequence, Dict[str, Any]]] = None,
@@ -293,20 +289,28 @@
     def _raw_request(self,
                      data,
                      params: Dict[str, str],
                      headers: Optional[Dict[str, Any]] = None,
                      method: str = 'POST',
                      retries: int = 0,
                      stream: bool = False,
+                     server_wait: bool = True,
                      error_handler: Callable = None) -> HTTPResponse:
         if isinstance(data, str):
             data = data.encode()
         headers = dict_copy(self.headers, headers)
         url = f'{self.url}?{urlencode(dict_copy(self.params, params))}'
         attempts = 0
+        if server_wait:
+            params['wait_end_of_query'] = '1'
+        # We can't actually read the progress headers, but we enable them so ClickHouse sends something
+        # to keep the connection alive when waiting for long-running queries and (2) to get summary information
+        # if not streaming
+        params['send_progress_in_http_headers'] = '1'
+        params['http_headers_progress_interval_ms'] = self._progress_interval
         while True:
             attempts += 1
             try:
                 response: HTTPResponse = self.http.request(method, url,
                                                            headers=headers,
                                                            timeout=self.timeout,
                                                            body=data,
```

### Comparing `clickhouse-connect-0.5.8/clickhouse_connect/driver/httputil.py` & `clickhouse-connect-0.5.9/clickhouse_connect/driver/httputil.py`

 * *Files 3% similar despite different names*

```diff
@@ -104,23 +104,22 @@
 
 
 class ResponseSource:
     def __init__(self, response: HTTPResponse, chunk_size: int = 1024 * 1024):
         self.response = response
         compression = response.headers.get('content-encoding')
         if compression == 'zstd':
-            zstd_decom = zstandard.ZstdDecompressor()
-            reader = zstd_decom.stream_reader(self, read_across_frames=False)
+            zstd_decom = zstandard.ZstdDecompressor().decompressobj()
 
             def decompress():
                 while True:
-                    chunk = reader.read()
+                    chunk = response.read(chunk_size)
                     if not chunk:
                         break
-                    yield chunk
+                    yield zstd_decom.decompress(chunk)
 
             self.gen = decompress()
         elif compression == 'lz4':
             lz4_decom = lz4.frame.LZ4FrameDecompressor()
 
             def decompress():
                 while lz4_decom.needs_input:
@@ -131,17 +130,12 @@
                         return
                     chunk = lz4_decom.decompress(data)
                     if chunk:
                         yield chunk
 
             self.gen = decompress()
         else:
-            self.gen = response.stream(decode_content=True)
+            self.gen = response.stream(amt=chunk_size, decode_content=True)
 
-    def read(self, amt: int) -> bytes:
-        return self.response.read(amt)
-
-    def close(self, ex: Exception = None):
-        if ex:
-            logger.warning('Closed HTTP response due to unexpected exception')
+    def close(self):
         self.response.drain_conn()
         self.response.close()
```

### Comparing `clickhouse-connect-0.5.8/clickhouse_connect/driver/insert.py` & `clickhouse-connect-0.5.9/clickhouse_connect/driver/insert.py`

 * *Files identical despite different names*

### Comparing `clickhouse-connect-0.5.8/clickhouse_connect/driver/models.py` & `clickhouse-connect-0.5.9/clickhouse_connect/driver/models.py`

 * *Files 8% similar despite different names*

```diff
@@ -22,11 +22,8 @@
 
 class SettingDef(NamedTuple):
     """
     ClickHouse setting definition from system.settings table
     """
     name: str
     value: str
-    changed: int
-    description: str
     readonly: int
-    type: str
```

### Comparing `clickhouse-connect-0.5.8/clickhouse_connect/driver/npquery.py` & `clickhouse-connect-0.5.9/clickhouse_connect/driver/npquery.py`

 * *Files 4% similar despite different names*

```diff
@@ -119,14 +119,14 @@
     def np_stream(self) -> StreamContext:
         return StreamContext(self, self._np_stream())
 
     @property
     def df_stream(self) -> StreamContext:
         return StreamContext(self, self._df_stream())
 
-    def close(self, ex: Exception = None):
+    def close(self):
         if self._block_gen is not None:
             self._block_gen.close()
             self._block_gen = None
         if self.source:
-            self.source.close(ex)
+            self.source.close()
             self.source = None
```

### Comparing `clickhouse-connect-0.5.8/clickhouse_connect/driver/options.py` & `clickhouse-connect-0.5.9/clickhouse_connect/driver/options.py`

 * *Files identical despite different names*

### Comparing `clickhouse-connect-0.5.8/clickhouse_connect/driver/parser.py` & `clickhouse-connect-0.5.9/clickhouse_connect/driver/parser.py`

 * *Files identical despite different names*

### Comparing `clickhouse-connect-0.5.8/clickhouse_connect/driver/query.py` & `clickhouse-connect-0.5.9/clickhouse_connect/driver/query.py`

 * *Files 2% similar despite different names*

```diff
@@ -45,15 +45,16 @@
                  encoding: Optional[str] = None,
                  server_tz: tzinfo = pytz.UTC,
                  use_none: Optional[bool] = None,
                  column_oriented: Optional[bool] = None,
                  use_numpy: Optional[bool] = None,
                  max_str_len: Optional[int] = 0,
                  query_tz: Optional[Union[str, tzinfo]] = None,
-                 column_tzs: Optional[Dict[str, Union[str, tzinfo]]] = None):
+                 column_tzs: Optional[Dict[str, Union[str, tzinfo]]] = None,
+                 streaming: bool = False):
         """
         Initializes various configuration settings for the query context
 
         :param query:  Query string with Python style format value replacements
         :param parameters: Optional dictionary of substitution values
         :param settings: Optional ClickHouse settings for the query
         :param query_formats: Optional dictionary of query formats with the key of a ClickHouse type name
@@ -100,14 +101,15 @@
                     try:
                         timezone = pytz.timezone(timezone)
                         column_tzs[col_name] = timezone
                     except UnknownTimeZoneError as ex:
                         raise ProgrammingError('query_tz is not recognized') from ex
         self.column_tzs = column_tzs
         self.block_info = False
+        self.streaming = streaming
         self._update_query()
 
     @property
     def is_select(self) -> bool:
         return select_re.search(self.uncommented_query) is not None
 
     @property
@@ -148,15 +150,16 @@
                      encoding: Optional[str] = None,
                      server_tz: Optional[tzinfo] = None,
                      use_none: Optional[bool] = None,
                      column_oriented: Optional[bool] = None,
                      use_numpy: Optional[bool] = None,
                      max_str_len: Optional[int] = None,
                      query_tz: [Optional[Union[str, tzinfo]]] = None,
-                     column_tzs: [Optional[Dict[str, Union[str, tzinfo]]]] = None) -> 'QueryContext':
+                     column_tzs: [Optional[Dict[str, Union[str, tzinfo]]]] = None,
+                     streaming: bool = False) -> 'QueryContext':
         """
         Creates Query context copy with parameters overridden/updated as appropriate.
         """
         return QueryContext(query or self.query,
                             dict_copy(self.parameters, parameters),
                             dict_copy(self.settings, settings),
                             dict_copy(self.query_formats, query_formats),
@@ -164,15 +167,16 @@
                             encoding if encoding else self.encoding,
                             server_tz if server_tz else self.server_tz,
                             self.use_none if use_none is None else use_none,
                             self.column_oriented if column_oriented is None else column_oriented,
                             self.use_numpy if use_numpy is None else use_numpy,
                             self.max_str_len if max_str_len is None else max_str_len,
                             self.query_tz if query_tz is None else query_tz,
-                            self.column_tzs if column_tzs is None else column_tzs)
+                            self.column_tzs if column_tzs is None else column_tzs,
+                            streaming)
 
     def _update_query(self):
         self.final_query, self.bind_params = bind_query(self.query, self.parameters, self.server_tz)
         self.uncommented_query = remove_sql_comments(self.final_query)
 
 
 class QueryResult(Closable):
@@ -302,17 +306,17 @@
         .. deprecated:: 0.5.4
            Please use the row_block_stream property instead.  This method will be removed in a future release
         """
         for block in self._row_block_stream():
             for row in block:
                 yield row
 
-    def close(self, ex: Exception = None):
+    def close(self):
         if self.source:
-            self.source.close(ex)
+            self.source.close()
             self.source = None
         if self._block_gen is not None:
             self._block_gen.close()
             self._block_gen = None
 
     def __enter__(self):
         return self
```

### Comparing `clickhouse-connect-0.5.8/clickhouse_connect/driver/tools.py` & `clickhouse-connect-0.5.9/clickhouse_connect/driver/tools.py`

 * *Files identical despite different names*

### Comparing `clickhouse-connect-0.5.8/clickhouse_connect/driver/transform.py` & `clickhouse-connect-0.5.9/clickhouse_connect/driver/transform.py`

 * *Files 4% similar despite different names*

```diff
@@ -1,11 +1,12 @@
 from typing import Union
 
 from clickhouse_connect.datatypes import registry
 from clickhouse_connect.driver.common import write_leb128
+from clickhouse_connect.driver.exceptions import StreamCompleteException, StreamFailureError
 from clickhouse_connect.driver.insert import InsertContext
 from clickhouse_connect.driver.npquery import NumpyResult
 from clickhouse_connect.driver.query import QueryResult, QueryContext
 from clickhouse_connect.driver.types import ByteSource
 from clickhouse_connect.driver.compression import get_compressor
 
 _EMPTY_CTX = QueryContext()
@@ -23,32 +24,35 @@
             nonlocal block_num
             result_block = []
             try:
                 try:
                     if context.block_info:
                         source.read_bytes(8)
                     num_cols = source.read_leb128()
-                    num_rows = source.read_leb128()
-                except (StopIteration, IndexError):
-                    source.close()
+                except StreamCompleteException:
                     return None
+                num_rows = source.read_leb128()
                 for col_num in range(num_cols):
                     name = source.read_leb128_str()
                     type_name = source.read_leb128_str()
                     if block_num == 0:
                         names.append(name)
                         col_type = registry.get_from_name(type_name)
                         col_types.append(col_type)
                     else:
                         col_type = col_types[col_num]
                     context.start_column(name)
                     column = col_type.read_column(source, num_rows, context)
                     result_block.append(column)
             except Exception as ex:
-                source.close(ex)  # Ensure that the query is closed if something unexpected happens
+                source.close()
+                if isinstance(ex, StreamCompleteException):
+                    # We ran out of data before it was expected, this could be ClickHouse reporting an error
+                    # in the response
+                    raise StreamFailureError(source.last_message) from None
                 raise
             block_num += 1
             return result_block
 
         first_block = get_block()
         if first_block is None:
             return NumpyResult() if context.use_numpy else QueryResult([])
```

### Comparing `clickhouse-connect-0.5.8/clickhouse_connect/driver/types.py` & `clickhouse-connect-0.5.9/clickhouse_connect/driver/types.py`

 * *Files 7% similar despite different names*

```diff
@@ -2,19 +2,20 @@
 from typing import Sequence, Any
 
 Matrix = Sequence[Sequence[Any]]
 
 
 class Closable(ABC):
     @abstractmethod
-    def close(self, ex: Exception = None):
+    def close(self):
         pass
 
 
 class ByteSource(Closable):
+    last_message = None
 
     @abstractmethod
     def read_leb128(self) -> int:
         pass
 
     @abstractmethod
     def read_leb128_str(self) -> str:
```

### Comparing `clickhouse-connect-0.5.8/clickhouse_connect/entry_points.py` & `clickhouse-connect-0.5.9/clickhouse_connect/entry_points.py`

 * *Files identical despite different names*

### Comparing `clickhouse-connect-0.5.8/clickhouse_connect/json_impl.py` & `clickhouse-connect-0.5.9/clickhouse_connect/json_impl.py`

 * *Files identical despite different names*

### Comparing `clickhouse-connect-0.5.8/clickhouse_connect.egg-info/PKG-INFO` & `clickhouse-connect-0.5.9/clickhouse_connect.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: clickhouse-connect
-Version: 0.5.8
+Version: 0.5.9
 Summary: ClickHouse core driver, SqlAlchemy, and Superset libraries
 Home-page: https://github.com/ClickHouse/clickhouse-connect
 Author: ClickHouse Inc.
 Author-email: clients@clickhouse.com
 License: Apache License 2.0
 Keywords: clickhouse,superset,sqlalchemy,http,driver
 Platform: UNKNOWN
```

### Comparing `clickhouse-connect-0.5.8/clickhouse_connect.egg-info/SOURCES.txt` & `clickhouse-connect-0.5.9/clickhouse_connect.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `clickhouse-connect-0.5.8/setup.py` & `clickhouse-connect-0.5.9/setup.py`

 * *Files identical despite different names*

