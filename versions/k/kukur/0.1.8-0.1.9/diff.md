# Comparing `tmp/kukur-0.1.8.tar.gz` & `tmp/kukur-0.1.9.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "kukur-0.1.8.tar", last modified: Wed Jan 18 13:57:04 2023, max compression
+gzip compressed data, was "kukur-0.1.9.tar", last modified: Mon Jan 30 12:41:37 2023, max compression
```

## Comparing `kukur-0.1.8.tar` & `kukur-0.1.9.tar`

### file list

```diff
@@ -1,91 +1,91 @@
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-18 13:57:04.059628 kukur-0.1.8/
--rw-r--r--   0 runner    (1001) docker     (123)      552 2023-01-18 13:56:50.000000 kukur-0.1.8/LICENSE
--rw-r--r--   0 runner    (1001) docker     (123)     6101 2023-01-18 13:57:04.059628 kukur-0.1.8/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)     4125 2023-01-18 13:56:50.000000 kukur-0.1.8/README.md
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-18 13:57:04.055628 kukur-0.1.8/kukur/
--rw-r--r--   0 runner    (1001) docker     (123)     2740 2023-01-18 13:56:50.000000 kukur-0.1.8/kukur/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-18 13:57:04.055628 kukur-0.1.8/kukur/api_key/
--rw-r--r--   0 runner    (1001) docker     (123)      304 2023-01-18 13:56:50.000000 kukur-0.1.8/kukur/api_key/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     1824 2023-01-18 13:56:50.000000 kukur-0.1.8/kukur/api_key/app.py
--rw-r--r--   0 runner    (1001) docker     (123)     3205 2023-01-18 13:56:50.000000 kukur-0.1.8/kukur/app.py
--rw-r--r--   0 runner    (1001) docker     (123)     5040 2023-01-18 13:56:50.000000 kukur-0.1.8/kukur/base.py
--rw-r--r--   0 runner    (1001) docker     (123)     7374 2023-01-18 13:56:50.000000 kukur-0.1.8/kukur/cli.py
--rw-r--r--   0 runner    (1001) docker     (123)     7119 2023-01-18 13:56:50.000000 kukur-0.1.8/kukur/client.py
--rw-r--r--   0 runner    (1001) docker     (123)     1388 2023-01-18 13:56:50.000000 kukur-0.1.8/kukur/config.py
--rw-r--r--   0 runner    (1001) docker     (123)     1416 2023-01-18 13:56:50.000000 kukur-0.1.8/kukur/exceptions.py
--rw-r--r--   0 runner    (1001) docker     (123)     6553 2023-01-18 13:56:50.000000 kukur-0.1.8/kukur/flight.py
--rw-r--r--   0 runner    (1001) docker     (123)     6771 2023-01-18 13:56:50.000000 kukur-0.1.8/kukur/loader.py
--rw-r--r--   0 runner    (1001) docker     (123)      863 2023-01-18 13:56:50.000000 kukur-0.1.8/kukur/logging.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-18 13:57:04.055628 kukur-0.1.8/kukur/metadata/
--rw-r--r--   0 runner    (1001) docker     (123)     6766 2023-01-18 13:56:50.000000 kukur-0.1.8/kukur/metadata/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     7176 2023-01-18 13:56:50.000000 kukur-0.1.8/kukur/metadata/fields.py
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-18 13:56:50.000000 kukur-0.1.8/kukur/py.typed
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-18 13:57:04.055628 kukur-0.1.8/kukur/repository/
--rw-r--r--   0 runner    (1001) docker     (123)      900 2023-01-18 13:56:50.000000 kukur-0.1.8/kukur/repository/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     3348 2023-01-18 13:56:50.000000 kukur-0.1.8/kukur/repository/api_key.py
--rw-r--r--   0 runner    (1001) docker     (123)     2029 2023-01-18 13:56:50.000000 kukur-0.1.8/kukur/repository/base.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-18 13:57:04.055628 kukur-0.1.8/kukur/source/
--rw-r--r--   0 runner    (1001) docker     (123)    17084 2023-01-18 13:56:50.000000 kukur-0.1.8/kukur/source/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-18 13:57:04.055628 kukur-0.1.8/kukur/source/adodb/
--rw-r--r--   0 runner    (1001) docker     (123)      247 2023-01-18 13:56:50.000000 kukur-0.1.8/kukur/source/adodb/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     1482 2023-01-18 13:56:50.000000 kukur-0.1.8/kukur/source/adodb/adodb.py
--rw-r--r--   0 runner    (1001) docker     (123)     8341 2023-01-18 13:56:50.000000 kukur-0.1.8/kukur/source/arrow.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-18 13:57:04.055628 kukur-0.1.8/kukur/source/azure_data_explorer/
--rw-r--r--   0 runner    (1001) docker     (123)      224 2023-01-18 13:56:50.000000 kukur-0.1.8/kukur/source/azure_data_explorer/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     9880 2023-01-18 13:56:50.000000 kukur-0.1.8/kukur/source/azure_data_explorer/azure_data_explorer.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-18 13:57:04.055628 kukur-0.1.8/kukur/source/cratedb/
--rw-r--r--   0 runner    (1001) docker     (123)      200 2023-01-18 13:56:50.000000 kukur-0.1.8/kukur/source/cratedb/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     1395 2023-01-18 13:56:50.000000 kukur-0.1.8/kukur/source/cratedb/cratedb.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-18 13:57:04.055628 kukur-0.1.8/kukur/source/csv/
--rw-r--r--   0 runner    (1001) docker     (123)      394 2023-01-18 13:56:50.000000 kukur-0.1.8/kukur/source/csv/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    15226 2023-01-18 13:56:50.000000 kukur-0.1.8/kukur/source/csv/csv.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-18 13:57:04.055628 kukur-0.1.8/kukur/source/delta/
--rw-r--r--   0 runner    (1001) docker     (123)      227 2023-01-18 13:56:50.000000 kukur-0.1.8/kukur/source/delta/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     2395 2023-01-18 13:56:50.000000 kukur-0.1.8/kukur/source/delta/delta_lake.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-18 13:57:04.055628 kukur-0.1.8/kukur/source/feather/
--rw-r--r--   0 runner    (1001) docker     (123)      406 2023-01-18 13:56:50.000000 kukur-0.1.8/kukur/source/feather/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     1628 2023-01-18 13:56:50.000000 kukur-0.1.8/kukur/source/feather/feather.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-18 13:57:04.055628 kukur-0.1.8/kukur/source/influxdb/
--rw-r--r--   0 runner    (1001) docker     (123)      202 2023-01-18 13:56:50.000000 kukur-0.1.8/kukur/source/influxdb/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     6350 2023-01-18 13:56:50.000000 kukur-0.1.8/kukur/source/influxdb/influxdb.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-18 13:57:04.055628 kukur-0.1.8/kukur/source/integration_test/
--rw-r--r--   0 runner    (1001) docker     (123)      201 2023-01-18 13:56:50.000000 kukur-0.1.8/kukur/source/integration_test/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     2302 2023-01-18 13:56:50.000000 kukur-0.1.8/kukur/source/integration_test/integration_test_source.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-18 13:57:04.059628 kukur-0.1.8/kukur/source/json/
--rw-r--r--   0 runner    (1001) docker     (123)      198 2023-01-18 13:56:50.000000 kukur-0.1.8/kukur/source/json/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     2132 2023-01-18 13:56:50.000000 kukur-0.1.8/kukur/source/json/json.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-18 13:57:04.059628 kukur-0.1.8/kukur/source/kukur/
--rw-r--r--   0 runner    (1001) docker     (123)      201 2023-01-18 13:56:50.000000 kukur-0.1.8/kukur/source/kukur/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     3388 2023-01-18 13:56:50.000000 kukur-0.1.8/kukur/source/kukur/kukur.py
--rw-r--r--   0 runner    (1001) docker     (123)     3180 2023-01-18 13:56:50.000000 kukur-0.1.8/kukur/source/metadata.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-18 13:57:04.059628 kukur-0.1.8/kukur/source/odbc/
--rw-r--r--   0 runner    (1001) docker     (123)      194 2023-01-18 13:56:50.000000 kukur-0.1.8/kukur/source/odbc/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     1348 2023-01-18 13:56:50.000000 kukur-0.1.8/kukur/source/odbc/odbc.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-18 13:57:04.059628 kukur-0.1.8/kukur/source/parquet/
--rw-r--r--   0 runner    (1001) docker     (123)      446 2023-01-18 13:56:50.000000 kukur-0.1.8/kukur/source/parquet/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     1668 2023-01-18 13:56:50.000000 kukur-0.1.8/kukur/source/parquet/parquet.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-18 13:57:04.059628 kukur-0.1.8/kukur/source/piwebapi_da/
--rw-r--r--   0 runner    (1001) docker     (123)      205 2023-01-18 13:56:50.000000 kukur-0.1.8/kukur/source/piwebapi_da/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    10605 2023-01-18 13:56:50.000000 kukur-0.1.8/kukur/source/piwebapi_da/piwebapi_da.py
--rw-r--r--   0 runner    (1001) docker     (123)     2466 2023-01-18 13:56:50.000000 kukur-0.1.8/kukur/source/quality.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-18 13:57:04.059628 kukur-0.1.8/kukur/source/simulator/
--rw-r--r--   0 runner    (1001) docker     (123)      207 2023-01-18 13:56:50.000000 kukur-0.1.8/kukur/source/simulator/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    24102 2023-01-18 13:56:50.000000 kukur-0.1.8/kukur/source/simulator/simulator.py
--rw-r--r--   0 runner    (1001) docker     (123)    11396 2023-01-18 13:56:50.000000 kukur-0.1.8/kukur/source/sql.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-18 13:57:04.059628 kukur-0.1.8/kukur/source/sqlite/
--rw-r--r--   0 runner    (1001) docker     (123)      176 2023-01-18 13:56:50.000000 kukur-0.1.8/kukur/source/sqlite/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     1664 2023-01-18 13:56:50.000000 kukur-0.1.8/kukur/source/sqlite/sqlite.py
--rw-r--r--   0 runner    (1001) docker     (123)     3833 2023-01-18 13:56:50.000000 kukur-0.1.8/kukur/source/test.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-18 13:57:04.055628 kukur-0.1.8/kukur.egg-info/
--rw-r--r--   0 runner    (1001) docker     (123)     6101 2023-01-18 13:57:03.000000 kukur-0.1.8/kukur.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)     1770 2023-01-18 13:57:03.000000 kukur-0.1.8/kukur.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-01-18 13:57:03.000000 kukur-0.1.8/kukur.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (123)       42 2023-01-18 13:57:03.000000 kukur-0.1.8/kukur.egg-info/entry_points.txt
--rw-r--r--   0 runner    (1001) docker     (123)      203 2023-01-18 13:57:03.000000 kukur-0.1.8/kukur.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (123)       12 2023-01-18 13:57:03.000000 kukur-0.1.8/kukur.egg-info/top_level.txt
--rw-r--r--   0 runner    (1001) docker     (123)      104 2023-01-18 13:56:50.000000 kukur-0.1.8/pyproject.toml
--rw-r--r--   0 runner    (1001) docker     (123)       38 2023-01-18 13:57:04.059628 kukur-0.1.8/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (123)     1379 2023-01-18 13:56:50.000000 kukur-0.1.8/setup.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-18 13:57:04.059628 kukur-0.1.8/tests/
--rw-r--r--   0 runner    (1001) docker     (123)      113 2023-01-18 13:56:50.000000 kukur-0.1.8/tests/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    14914 2023-01-18 13:56:50.000000 kukur-0.1.8/tests/test_metadata.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-30 12:41:37.415004 kukur-0.1.9/
+-rw-r--r--   0 runner    (1001) docker     (123)      552 2023-01-30 12:41:24.000000 kukur-0.1.9/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (123)     6101 2023-01-30 12:41:37.415004 kukur-0.1.9/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     4125 2023-01-30 12:41:24.000000 kukur-0.1.9/README.md
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-30 12:41:37.407004 kukur-0.1.9/kukur/
+-rw-r--r--   0 runner    (1001) docker     (123)     2740 2023-01-30 12:41:24.000000 kukur-0.1.9/kukur/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-30 12:41:37.411004 kukur-0.1.9/kukur/api_key/
+-rw-r--r--   0 runner    (1001) docker     (123)      304 2023-01-30 12:41:24.000000 kukur-0.1.9/kukur/api_key/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1824 2023-01-30 12:41:24.000000 kukur-0.1.9/kukur/api_key/app.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3205 2023-01-30 12:41:24.000000 kukur-0.1.9/kukur/app.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5040 2023-01-30 12:41:24.000000 kukur-0.1.9/kukur/base.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7374 2023-01-30 12:41:24.000000 kukur-0.1.9/kukur/cli.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7119 2023-01-30 12:41:24.000000 kukur-0.1.9/kukur/client.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1388 2023-01-30 12:41:24.000000 kukur-0.1.9/kukur/config.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1416 2023-01-30 12:41:24.000000 kukur-0.1.9/kukur/exceptions.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6553 2023-01-30 12:41:24.000000 kukur-0.1.9/kukur/flight.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6771 2023-01-30 12:41:24.000000 kukur-0.1.9/kukur/loader.py
+-rw-r--r--   0 runner    (1001) docker     (123)      863 2023-01-30 12:41:24.000000 kukur-0.1.9/kukur/logging.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-30 12:41:37.411004 kukur-0.1.9/kukur/metadata/
+-rw-r--r--   0 runner    (1001) docker     (123)     6766 2023-01-30 12:41:24.000000 kukur-0.1.9/kukur/metadata/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7176 2023-01-30 12:41:24.000000 kukur-0.1.9/kukur/metadata/fields.py
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-30 12:41:24.000000 kukur-0.1.9/kukur/py.typed
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-30 12:41:37.411004 kukur-0.1.9/kukur/repository/
+-rw-r--r--   0 runner    (1001) docker     (123)      900 2023-01-30 12:41:24.000000 kukur-0.1.9/kukur/repository/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3348 2023-01-30 12:41:24.000000 kukur-0.1.9/kukur/repository/api_key.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2029 2023-01-30 12:41:24.000000 kukur-0.1.9/kukur/repository/base.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-30 12:41:37.411004 kukur-0.1.9/kukur/source/
+-rw-r--r--   0 runner    (1001) docker     (123)    17084 2023-01-30 12:41:24.000000 kukur-0.1.9/kukur/source/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-30 12:41:37.411004 kukur-0.1.9/kukur/source/adodb/
+-rw-r--r--   0 runner    (1001) docker     (123)      247 2023-01-30 12:41:24.000000 kukur-0.1.9/kukur/source/adodb/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1482 2023-01-30 12:41:24.000000 kukur-0.1.9/kukur/source/adodb/adodb.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8840 2023-01-30 12:41:24.000000 kukur-0.1.9/kukur/source/arrow.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-30 12:41:37.411004 kukur-0.1.9/kukur/source/azure_data_explorer/
+-rw-r--r--   0 runner    (1001) docker     (123)      224 2023-01-30 12:41:24.000000 kukur-0.1.9/kukur/source/azure_data_explorer/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9880 2023-01-30 12:41:24.000000 kukur-0.1.9/kukur/source/azure_data_explorer/azure_data_explorer.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-30 12:41:37.411004 kukur-0.1.9/kukur/source/cratedb/
+-rw-r--r--   0 runner    (1001) docker     (123)      200 2023-01-30 12:41:24.000000 kukur-0.1.9/kukur/source/cratedb/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1395 2023-01-30 12:41:24.000000 kukur-0.1.9/kukur/source/cratedb/cratedb.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-30 12:41:37.411004 kukur-0.1.9/kukur/source/csv/
+-rw-r--r--   0 runner    (1001) docker     (123)      394 2023-01-30 12:41:24.000000 kukur-0.1.9/kukur/source/csv/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    19451 2023-01-30 12:41:24.000000 kukur-0.1.9/kukur/source/csv/csv.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-30 12:41:37.411004 kukur-0.1.9/kukur/source/delta/
+-rw-r--r--   0 runner    (1001) docker     (123)      227 2023-01-30 12:41:24.000000 kukur-0.1.9/kukur/source/delta/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2395 2023-01-30 12:41:24.000000 kukur-0.1.9/kukur/source/delta/delta_lake.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-30 12:41:37.411004 kukur-0.1.9/kukur/source/feather/
+-rw-r--r--   0 runner    (1001) docker     (123)      406 2023-01-30 12:41:24.000000 kukur-0.1.9/kukur/source/feather/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1628 2023-01-30 12:41:24.000000 kukur-0.1.9/kukur/source/feather/feather.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-30 12:41:37.411004 kukur-0.1.9/kukur/source/influxdb/
+-rw-r--r--   0 runner    (1001) docker     (123)      202 2023-01-30 12:41:24.000000 kukur-0.1.9/kukur/source/influxdb/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6350 2023-01-30 12:41:24.000000 kukur-0.1.9/kukur/source/influxdb/influxdb.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-30 12:41:37.411004 kukur-0.1.9/kukur/source/integration_test/
+-rw-r--r--   0 runner    (1001) docker     (123)      201 2023-01-30 12:41:24.000000 kukur-0.1.9/kukur/source/integration_test/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2302 2023-01-30 12:41:24.000000 kukur-0.1.9/kukur/source/integration_test/integration_test_source.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-30 12:41:37.411004 kukur-0.1.9/kukur/source/json/
+-rw-r--r--   0 runner    (1001) docker     (123)      198 2023-01-30 12:41:24.000000 kukur-0.1.9/kukur/source/json/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2132 2023-01-30 12:41:24.000000 kukur-0.1.9/kukur/source/json/json.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-30 12:41:37.411004 kukur-0.1.9/kukur/source/kukur/
+-rw-r--r--   0 runner    (1001) docker     (123)      201 2023-01-30 12:41:24.000000 kukur-0.1.9/kukur/source/kukur/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3388 2023-01-30 12:41:24.000000 kukur-0.1.9/kukur/source/kukur/kukur.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3180 2023-01-30 12:41:24.000000 kukur-0.1.9/kukur/source/metadata.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-30 12:41:37.411004 kukur-0.1.9/kukur/source/odbc/
+-rw-r--r--   0 runner    (1001) docker     (123)      194 2023-01-30 12:41:24.000000 kukur-0.1.9/kukur/source/odbc/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1348 2023-01-30 12:41:24.000000 kukur-0.1.9/kukur/source/odbc/odbc.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-30 12:41:37.411004 kukur-0.1.9/kukur/source/parquet/
+-rw-r--r--   0 runner    (1001) docker     (123)      446 2023-01-30 12:41:24.000000 kukur-0.1.9/kukur/source/parquet/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1668 2023-01-30 12:41:24.000000 kukur-0.1.9/kukur/source/parquet/parquet.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-30 12:41:37.411004 kukur-0.1.9/kukur/source/piwebapi_da/
+-rw-r--r--   0 runner    (1001) docker     (123)      205 2023-01-30 12:41:24.000000 kukur-0.1.9/kukur/source/piwebapi_da/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    10605 2023-01-30 12:41:24.000000 kukur-0.1.9/kukur/source/piwebapi_da/piwebapi_da.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2466 2023-01-30 12:41:24.000000 kukur-0.1.9/kukur/source/quality.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-30 12:41:37.411004 kukur-0.1.9/kukur/source/simulator/
+-rw-r--r--   0 runner    (1001) docker     (123)      207 2023-01-30 12:41:24.000000 kukur-0.1.9/kukur/source/simulator/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    24102 2023-01-30 12:41:24.000000 kukur-0.1.9/kukur/source/simulator/simulator.py
+-rw-r--r--   0 runner    (1001) docker     (123)    11396 2023-01-30 12:41:24.000000 kukur-0.1.9/kukur/source/sql.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-30 12:41:37.411004 kukur-0.1.9/kukur/source/sqlite/
+-rw-r--r--   0 runner    (1001) docker     (123)      176 2023-01-30 12:41:24.000000 kukur-0.1.9/kukur/source/sqlite/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1664 2023-01-30 12:41:24.000000 kukur-0.1.9/kukur/source/sqlite/sqlite.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3833 2023-01-30 12:41:24.000000 kukur-0.1.9/kukur/source/test.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-30 12:41:37.407004 kukur-0.1.9/kukur.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)     6101 2023-01-30 12:41:37.000000 kukur-0.1.9/kukur.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     1770 2023-01-30 12:41:37.000000 kukur-0.1.9/kukur.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-01-30 12:41:37.000000 kukur-0.1.9/kukur.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       42 2023-01-30 12:41:37.000000 kukur-0.1.9/kukur.egg-info/entry_points.txt
+-rw-r--r--   0 runner    (1001) docker     (123)      203 2023-01-30 12:41:37.000000 kukur-0.1.9/kukur.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       12 2023-01-30 12:41:37.000000 kukur-0.1.9/kukur.egg-info/top_level.txt
+-rw-r--r--   0 runner    (1001) docker     (123)      104 2023-01-30 12:41:24.000000 kukur-0.1.9/pyproject.toml
+-rw-r--r--   0 runner    (1001) docker     (123)       38 2023-01-30 12:41:37.415004 kukur-0.1.9/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (123)     1379 2023-01-30 12:41:24.000000 kukur-0.1.9/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-30 12:41:37.411004 kukur-0.1.9/tests/
+-rw-r--r--   0 runner    (1001) docker     (123)      113 2023-01-30 12:41:24.000000 kukur-0.1.9/tests/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    14914 2023-01-30 12:41:24.000000 kukur-0.1.9/tests/test_metadata.py
```

### Comparing `kukur-0.1.8/LICENSE` & `kukur-0.1.9/LICENSE`

 * *Files identical despite different names*

### Comparing `kukur-0.1.8/PKG-INFO` & `kukur-0.1.9/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: kukur
-Version: 0.1.8
+Version: 0.1.9
 Summary: Kukur makes time series data and metadata available to the Apache Arrow ecosystem.
 Home-page: https://kukur.timeseer.ai/
 Author: Timeseer.AI
 Author-email: pypi@timeseer.ai
 License: Apache-2.0
 Description: # Kukur
```

### Comparing `kukur-0.1.8/README.md` & `kukur-0.1.9/README.md`

 * *Files identical despite different names*

### Comparing `kukur-0.1.8/kukur/__init__.py` & `kukur-0.1.9/kukur/__init__.py`

 * *Files identical despite different names*

### Comparing `kukur-0.1.8/kukur/api_key/app.py` & `kukur-0.1.9/kukur/api_key/app.py`

 * *Files identical despite different names*

### Comparing `kukur-0.1.8/kukur/app.py` & `kukur-0.1.9/kukur/app.py`

 * *Files identical despite different names*

### Comparing `kukur-0.1.8/kukur/base.py` & `kukur-0.1.9/kukur/base.py`

 * *Files identical despite different names*

### Comparing `kukur-0.1.8/kukur/cli.py` & `kukur-0.1.9/kukur/cli.py`

 * *Files identical despite different names*

### Comparing `kukur-0.1.8/kukur/client.py` & `kukur-0.1.9/kukur/client.py`

 * *Files identical despite different names*

### Comparing `kukur-0.1.8/kukur/config.py` & `kukur-0.1.9/kukur/config.py`

 * *Files identical despite different names*

### Comparing `kukur-0.1.8/kukur/exceptions.py` & `kukur-0.1.9/kukur/exceptions.py`

 * *Files identical despite different names*

### Comparing `kukur-0.1.8/kukur/flight.py` & `kukur-0.1.9/kukur/flight.py`

 * *Files identical despite different names*

### Comparing `kukur-0.1.8/kukur/loader.py` & `kukur-0.1.9/kukur/loader.py`

 * *Files identical despite different names*

### Comparing `kukur-0.1.8/kukur/logging.py` & `kukur-0.1.9/kukur/logging.py`

 * *Files identical despite different names*

### Comparing `kukur-0.1.8/kukur/metadata/__init__.py` & `kukur-0.1.9/kukur/metadata/__init__.py`

 * *Files identical despite different names*

### Comparing `kukur-0.1.8/kukur/metadata/fields.py` & `kukur-0.1.9/kukur/metadata/fields.py`

 * *Files identical despite different names*

### Comparing `kukur-0.1.8/kukur/repository/__init__.py` & `kukur-0.1.9/kukur/repository/__init__.py`

 * *Files identical despite different names*

### Comparing `kukur-0.1.8/kukur/repository/api_key.py` & `kukur-0.1.9/kukur/repository/api_key.py`

 * *Files identical despite different names*

### Comparing `kukur-0.1.8/kukur/repository/base.py` & `kukur-0.1.9/kukur/repository/base.py`

 * *Files identical despite different names*

### Comparing `kukur-0.1.8/kukur/source/__init__.py` & `kukur-0.1.9/kukur/source/__init__.py`

 * *Files identical despite different names*

### Comparing `kukur-0.1.8/kukur/source/adodb/adodb.py` & `kukur-0.1.9/kukur/source/adodb/adodb.py`

 * *Files identical despite different names*

### Comparing `kukur-0.1.8/kukur/source/arrow.py` & `kukur-0.1.9/kukur/source/arrow.py`

 * *Files 5% similar despite different names*

```diff
@@ -95,34 +95,39 @@
 
         if self.__options.data_format == "dir":
             return self._read_directory_data(selector)
 
         return self._read_row_data(selector)
 
     def _search_pivot(self, source_name: str) -> Generator[SeriesSelector, None, None]:
-        all_data = self.read_file(self.__loader.open())
+        all_data = self._load_pivot_data()
         for name in all_data.column_names[1:]:
             yield SeriesSelector(source_name, name)
 
     def _read_pivot_data(self, selector: SeriesSelector) -> pa.Table:
-        all_data = self.read_file(self.__loader.open())
+        all_data = self._load_pivot_data()
         if selector.name not in all_data.column_names:
             raise InvalidDataError(f'column "{selector.name}" not found')
         data = all_data.select([0, selector.name]).rename_columns(["ts", "value"])
-        data = _cast_ts_column(
-            data, self.__options.data_datetime_format, self.__options.data_timezone
-        )
         schema = pa.schema(
             [
                 ("ts", pa.timestamp("us", "utc")),
                 ("value", _get_value_schema_type(data)),
             ]
         )
         return data.cast(schema)
 
+    def _load_pivot_data(self) -> pa.Table:
+        all_data = self.read_file(self.__loader.open())
+        all_data = _map_pivot_columns(self.__options.column_mapping, all_data)
+        all_data = _cast_ts_column(
+            all_data, self.__options.data_datetime_format, self.__options.data_timezone
+        )
+        return all_data
+
     def _search_row(self, source_name: str) -> Generator[SeriesSelector, None, None]:
         all_data = self._load_row_data()
         # pylint: disable=no-member
         for name in pyarrow.compute.unique(all_data["series name"]):
             yield SeriesSelector(source_name, name.as_py())
 
     def _read_row_data(self, selector: SeriesSelector) -> pa.Table:
@@ -214,14 +219,23 @@
         }
     if "quality" in column_mapping:
         columns["quality"] = data[column_mapping["quality"]]
 
     return pa.Table.from_pydict(columns)
 
 
+def _map_pivot_columns(column_mapping: Dict[str, str], data: pa.Table) -> pa.Table:
+    ts_column_name = data.column_names[0]
+    if "ts" in column_mapping:
+        ts_column_name = column_mapping["ts"]
+
+    ts_column = data[ts_column_name]
+    return data.drop([ts_column_name]).add_column(0, "ts", ts_column)
+
+
 def _cast_ts_column(
     data: pa.Table, data_datetime_format: Optional[str], data_timezone: Optional[str]
 ) -> pa.Table:
     if data_datetime_format is not None:
         # pylint: disable=no-member
         data = data.set_column(
             data.column_names.index("ts"),
```

### Comparing `kukur-0.1.8/kukur/source/azure_data_explorer/azure_data_explorer.py` & `kukur-0.1.9/kukur/source/azure_data_explorer/azure_data_explorer.py`

 * *Files identical despite different names*

### Comparing `kukur-0.1.8/kukur/source/cratedb/cratedb.py` & `kukur-0.1.9/kukur/source/cratedb/cratedb.py`

 * *Files identical despite different names*

### Comparing `kukur-0.1.8/kukur/source/csv/csv.py` & `kukur-0.1.9/kukur/source/csv/csv.py`

 * *Files 18% similar despite different names*

```diff
@@ -239,24 +239,31 @@
     ) -> Generator[SeriesSelector, None, None]:
         if self.__loaders.data is None:
             return
 
         if self.__options.data_format == "row":
             yield from self._search_row(self.__loaders.data, search)
         elif self.__options.data_format == "pivot":
-            yield from _search_pivot(self.__loaders.data, search)
+            yield from self._search_pivot(self.__loaders.data, search)
 
     def _search_row(
         self, loader: Loader, search: SeriesSearch
     ) -> Generator[SeriesSelector, None, None]:
         all_data = self._open_row_data(loader)
         # pylint: disable=no-member
         for name in pyarrow.compute.unique(all_data["series name"]):
             yield SeriesSelector(search.source, name.as_py())
 
+    def _search_pivot(
+        self, loader: Loader, search: SeriesSearch
+    ) -> Generator[SeriesSelector, None, None]:
+        all_data = self._open_pivot_data(loader)
+        for name in all_data.column_names[1:]:
+            yield SeriesSelector(search.source, name)
+
     def __read_all_data(self, selector: SeriesSelector) -> pa.Table:
         if self.__loaders.data is None:
             raise InvalidSourceException("No data path configured.")
         if self.__options.data_format == "pivot":
             return self._read_pivot_data(self.__loaders.data, selector)
 
         if self.__options.data_format == "dir":
@@ -288,62 +295,141 @@
 
         convert_options = _get_convert_options(
             timestamp_column,
             self.__options.data_datetime_format,
             self.__options.data_timezone,
         )
 
-        all_data = pyarrow.csv.read_csv(
-            loader.open(), read_options=read_options, convert_options=convert_options
-        )
-        all_data = _map_columns(self.__options.column_mapping, all_data)
-        all_data = _cast_ts_column(all_data, self.__options.data_timezone)
+        try:
+            all_data = pyarrow.csv.read_csv(
+                loader.open(),
+                read_options=read_options,
+                convert_options=convert_options,
+            )
+
+            all_data = _map_columns(self.__options.column_mapping, all_data)
+            all_data = _cast_ts_column(all_data, self.__options.data_timezone)
+        except pa.lib.ArrowInvalid as arrow_invalid_exception:
+            if self.__options.data_datetime_format is None:
+                raise arrow_invalid_exception
+
+            column_types = {timestamp_column: pa.string()}
+            convert_options = pyarrow.csv.ConvertOptions(
+                column_types=column_types,
+            )
+            all_data = pyarrow.csv.read_csv(
+                loader.open(),
+                read_options=read_options,
+                convert_options=convert_options,
+            )
+            all_data = _map_columns(self.__options.column_mapping, all_data)
+            all_data = _convert_timestamp(
+                all_data,
+                self.__options.data_datetime_format,
+                self.__options.data_timezone,
+            )
+
         if self.__mappers.quality.is_present():
             all_data = all_data.set_column(
                 3, "quality", self._map_quality(all_data["quality"])
             )
         return all_data
 
     def _read_directory_data(
         self, loader: Loader, selector: SeriesSelector
     ) -> pa.Table:
         columns = ["ts", "value"]
+        timestamp_column = "ts"
+        if "ts" in self.__options.column_mapping:
+            timestamp_column = self.__options.column_mapping["ts"]
+
         if self.__mappers.quality.is_present():
             columns.append("quality")
         if not self.__options.header_row:
             read_options = pyarrow.csv.ReadOptions(column_names=columns)
         else:
             read_options = pyarrow.csv.ReadOptions()
 
         convert_options = _get_convert_options(
             "ts", self.__options.data_datetime_format, self.__options.data_timezone
         )
 
-        data = pyarrow.csv.read_csv(
-            loader.open_child(f"{selector.tags['series name']}.csv"),
-            read_options=read_options,
-            convert_options=convert_options,
-        )
-        data = _map_columns(self.__options.column_mapping, data)
-        data = _cast_ts_column(data, self.__options.data_timezone)
+        try:
+            data = pyarrow.csv.read_csv(
+                loader.open_child(f"{selector.tags['series name']}.csv"),
+                read_options=read_options,
+                convert_options=convert_options,
+            )
+            data = _map_columns(self.__options.column_mapping, data)
+            data = _cast_ts_column(data, self.__options.data_timezone)
+        except pa.lib.ArrowInvalid as arrow_invalid_exception:
+            if self.__options.data_datetime_format is None:
+                raise arrow_invalid_exception
+
+            column_types = {timestamp_column: pa.string()}
+            convert_options = pyarrow.csv.ConvertOptions(
+                column_types=column_types,
+            )
+            data = pyarrow.csv.read_csv(
+                loader.open_child(f"{selector.tags['series name']}.csv"),
+                read_options=read_options,
+                convert_options=convert_options,
+            )
+            data = _map_columns(self.__options.column_mapping, data)
+            data = _convert_timestamp(
+                data,
+                self.__options.data_datetime_format,
+                self.__options.data_timezone,
+            )
         if self.__mappers.quality.is_present():
             return data.set_column(2, "quality", self._map_quality(data["quality"]))
         return data
 
     def _read_pivot_data(self, loader: Loader, selector: SeriesSelector) -> pa.Table:
-        convert_options = _get_convert_options(
-            "ts", self.__options.data_datetime_format, self.__options.data_timezone
-        )
-        all_data = pyarrow.csv.read_csv(loader.open(), convert_options=convert_options)
+        all_data = self._open_pivot_data(loader)
         if selector.name not in all_data.column_names:
             raise InvalidDataError(f'column "{selector.name}" not found')
-        data = all_data.select([0, selector.name]).rename_columns(["ts", "value"])
-        data = _cast_ts_column(data, self.__options.data_timezone)
-        schema = pa.schema([("ts", pa.timestamp("us", "utc")), ("value", pa.float64())])
-        return data.cast(schema)
+        data = all_data.select(["ts", selector.name]).rename_columns(["ts", "value"])
+        return data
+
+    def _open_pivot_data(self, loader: Loader) -> pa.Table:
+        timestamp_column = "ts"
+        if "ts" in self.__options.column_mapping:
+            timestamp_column = self.__options.column_mapping["ts"]
+
+        convert_options = _get_convert_options(
+            timestamp_column,
+            self.__options.data_datetime_format,
+            self.__options.data_timezone,
+        )
+        try:
+            all_data = pyarrow.csv.read_csv(
+                loader.open(), convert_options=convert_options
+            )
+            all_data = _map_pivot_columns(self.__options.column_mapping, all_data)
+            all_data = _cast_ts_column(all_data, self.__options.data_timezone)
+        except pa.lib.ArrowInvalid as arrow_invalid_exception:
+            if self.__options.data_datetime_format is None:
+                raise arrow_invalid_exception
+
+            column_types = {timestamp_column: pa.string()}
+            convert_options = pyarrow.csv.ConvertOptions(
+                column_types=column_types,
+            )
+            all_data = pyarrow.csv.read_csv(
+                loader.open(),
+                convert_options=convert_options,
+            )
+            all_data = _map_pivot_columns(self.__options.column_mapping, all_data)
+            all_data = _convert_timestamp(
+                all_data,
+                self.__options.data_datetime_format,
+                self.__options.data_timezone,
+            )
+        return all_data
 
     def _map_quality(self, quality_data: pa.Array) -> pa.Array:
         return self.__mappers.quality.map_array(quality_data)
 
 
 def _get_convert_options(
     timestamp_column: str,
@@ -351,14 +437,15 @@
     data_timezone: Optional[str],
 ) -> pyarrow.csv.ConvertOptions:
     column_types = {
         timestamp_column: pa.timestamp("us")
         if data_timezone is not None
         else pa.timestamp("us", "utc")
     }
+
     timestamp_parsers = (
         [data_datetime_format] if data_datetime_format is not None else None
     )
     return pyarrow.csv.ConvertOptions(
         column_types=column_types,
         timestamp_parsers=timestamp_parsers,
     )
@@ -372,14 +459,47 @@
     return data.set_column(
         data.column_names.index("ts"),
         "ts",
         pyarrow.compute.assume_timezone(data["ts"], data_timezone),
     )
 
 
+def _convert_timestamp(
+    data: pa.Table, data_datetime_format: str, data_timezone: Optional[str]
+) -> pa.Table:
+    # pylint: disable=no-member
+    data = data.set_column(
+        data.column_names.index("ts"),
+        "ts",
+        [
+            [
+                datetime.strptime(timestamp.as_py(), data_datetime_format)
+                for timestamp in data["ts"]
+            ]
+        ],
+    )
+
+    if data_timezone is None:
+        if data["ts"][0].as_py().tzinfo is None:
+            # pylint: disable=no-member
+            return data.set_column(
+                data.column_names.index("ts"),
+                "ts",
+                pyarrow.compute.assume_timezone(data["ts"], "UTC"),
+            )
+        return data
+
+    # pylint: disable=no-member
+    return data.set_column(
+        data.column_names.index("ts"),
+        "ts",
+        pyarrow.compute.assume_timezone(data["ts"], data_timezone),
+    )
+
+
 def _map_columns(column_mapping: Dict[str, str], data: pa.Table) -> pa.Table:
     if len(column_mapping) == 0:
         return data
 
     columns = {
         "ts": data[column_mapping["ts"]],
         "value": data[column_mapping["value"]],
@@ -390,13 +510,14 @@
 
     if "quality" in column_mapping:
         columns["quality"] = data[column_mapping["quality"]]
 
     return pa.Table.from_pydict(columns)
 
 
-def _search_pivot(
-    loader: Loader, search: SeriesSearch
-) -> Generator[SeriesSelector, None, None]:
-    all_data = pyarrow.csv.read_csv(loader.open())
-    for name in all_data.column_names[1:]:
-        yield SeriesSelector(search.source, name)
+def _map_pivot_columns(column_mapping: Dict[str, str], data: pa.Table) -> pa.Table:
+    ts_column_name = data.column_names[0]
+    if "ts" in column_mapping:
+        ts_column_name = column_mapping["ts"]
+
+    ts_column = data[ts_column_name]
+    return data.drop([ts_column_name]).add_column(0, "ts", ts_column)
```

### Comparing `kukur-0.1.8/kukur/source/delta/delta_lake.py` & `kukur-0.1.9/kukur/source/delta/delta_lake.py`

 * *Files identical despite different names*

### Comparing `kukur-0.1.8/kukur/source/feather/feather.py` & `kukur-0.1.9/kukur/source/feather/feather.py`

 * *Files identical despite different names*

### Comparing `kukur-0.1.8/kukur/source/influxdb/influxdb.py` & `kukur-0.1.9/kukur/source/influxdb/influxdb.py`

 * *Files identical despite different names*

### Comparing `kukur-0.1.8/kukur/source/integration_test/integration_test_source.py` & `kukur-0.1.9/kukur/source/integration_test/integration_test_source.py`

 * *Files identical despite different names*

### Comparing `kukur-0.1.8/kukur/source/json/json.py` & `kukur-0.1.9/kukur/source/json/json.py`

 * *Files identical despite different names*

### Comparing `kukur-0.1.8/kukur/source/kukur/kukur.py` & `kukur-0.1.9/kukur/source/kukur/kukur.py`

 * *Files identical despite different names*

### Comparing `kukur-0.1.8/kukur/source/metadata.py` & `kukur-0.1.9/kukur/source/metadata.py`

 * *Files identical despite different names*

### Comparing `kukur-0.1.8/kukur/source/odbc/odbc.py` & `kukur-0.1.9/kukur/source/odbc/odbc.py`

 * *Files identical despite different names*

### Comparing `kukur-0.1.8/kukur/source/parquet/parquet.py` & `kukur-0.1.9/kukur/source/parquet/parquet.py`

 * *Files identical despite different names*

### Comparing `kukur-0.1.8/kukur/source/piwebapi_da/piwebapi_da.py` & `kukur-0.1.9/kukur/source/piwebapi_da/piwebapi_da.py`

 * *Files identical despite different names*

### Comparing `kukur-0.1.8/kukur/source/quality.py` & `kukur-0.1.9/kukur/source/quality.py`

 * *Files identical despite different names*

### Comparing `kukur-0.1.8/kukur/source/simulator/simulator.py` & `kukur-0.1.9/kukur/source/simulator/simulator.py`

 * *Files identical despite different names*

### Comparing `kukur-0.1.8/kukur/source/sql.py` & `kukur-0.1.9/kukur/source/sql.py`

 * *Files identical despite different names*

### Comparing `kukur-0.1.8/kukur/source/sqlite/sqlite.py` & `kukur-0.1.9/kukur/source/sqlite/sqlite.py`

 * *Files identical despite different names*

### Comparing `kukur-0.1.8/kukur/source/test.py` & `kukur-0.1.9/kukur/source/test.py`

 * *Files identical despite different names*

### Comparing `kukur-0.1.8/kukur.egg-info/PKG-INFO` & `kukur-0.1.9/kukur.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: kukur
-Version: 0.1.8
+Version: 0.1.9
 Summary: Kukur makes time series data and metadata available to the Apache Arrow ecosystem.
 Home-page: https://kukur.timeseer.ai/
 Author: Timeseer.AI
 Author-email: pypi@timeseer.ai
 License: Apache-2.0
 Description: # Kukur
```

### Comparing `kukur-0.1.8/kukur.egg-info/SOURCES.txt` & `kukur-0.1.9/kukur.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `kukur-0.1.8/setup.py` & `kukur-0.1.9/setup.py`

 * *Files identical despite different names*

### Comparing `kukur-0.1.8/tests/test_metadata.py` & `kukur-0.1.9/tests/test_metadata.py`

 * *Files identical despite different names*

