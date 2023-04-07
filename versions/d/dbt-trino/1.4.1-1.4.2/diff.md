# Comparing `tmp/dbt-trino-1.4.1.tar.gz` & `tmp/dbt-trino-1.4.2.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "dbt-trino-1.4.1.tar", last modified: Wed Mar  1 15:53:42 2023, max compression
+gzip compressed data, was "dbt-trino-1.4.2.tar", last modified: Fri Apr  7 10:35:53 2023, max compression
```

## Comparing `dbt-trino-1.4.1.tar` & `dbt-trino-1.4.2.tar`

### file list

```diff
@@ -1,54 +1,55 @@
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-01 15:53:42.725257 dbt-trino-1.4.1/
--rw-r--r--   0 runner    (1001) docker     (123)    11357 2023-03-01 15:52:55.000000 dbt-trino-1.4.1/LICENSE.txt
--rw-r--r--   0 runner    (1001) docker     (123)    26488 2023-03-01 15:53:42.725257 dbt-trino-1.4.1/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)    25609 2023-03-01 15:52:55.000000 dbt-trino-1.4.1/README.md
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-01 15:53:42.721257 dbt-trino-1.4.1/dbt/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-01 15:53:42.721257 dbt-trino-1.4.1/dbt/adapters/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-01 15:53:42.721257 dbt-trino-1.4.1/dbt/adapters/trino/
--rw-r--r--   0 runner    (1001) docker     (123)      565 2023-03-01 15:52:55.000000 dbt-trino-1.4.1/dbt/adapters/trino/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)       18 2023-03-01 15:52:55.000000 dbt-trino-1.4.1/dbt/adapters/trino/__version__.py
--rw-r--r--   0 runner    (1001) docker     (123)     3408 2023-03-01 15:52:55.000000 dbt-trino-1.4.1/dbt/adapters/trino/column.py
--rw-r--r--   0 runner    (1001) docker     (123)    15865 2023-03-01 15:52:55.000000 dbt-trino-1.4.1/dbt/adapters/trino/connections.py
--rw-r--r--   0 runner    (1001) docker     (123)     1728 2023-03-01 15:52:55.000000 dbt-trino-1.4.1/dbt/adapters/trino/impl.py
--rw-r--r--   0 runner    (1001) docker     (123)      659 2023-03-01 15:52:55.000000 dbt-trino-1.4.1/dbt/adapters/trino/relation.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-01 15:53:42.721257 dbt-trino-1.4.1/dbt/include/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-01 15:53:42.721257 dbt-trino-1.4.1/dbt/include/trino/
--rw-r--r--   0 runner    (1001) docker     (123)       52 2023-03-01 15:52:55.000000 dbt-trino-1.4.1/dbt/include/trino/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)       72 2023-03-01 15:52:55.000000 dbt-trino-1.4.1/dbt/include/trino/dbt_project.yml
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-01 15:53:42.721257 dbt-trino-1.4.1/dbt/include/trino/macros/
--rw-r--r--   0 runner    (1001) docker     (123)     7270 2023-03-01 15:52:55.000000 dbt-trino-1.4.1/dbt/include/trino/macros/adapters.sql
--rw-r--r--   0 runner    (1001) docker     (123)     1789 2023-03-01 15:52:55.000000 dbt-trino-1.4.1/dbt/include/trino/macros/apply_grants.sql
--rw-r--r--   0 runner    (1001) docker     (123)     2060 2023-03-01 15:52:55.000000 dbt-trino-1.4.1/dbt/include/trino/macros/catalog.sql
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-01 15:53:42.721257 dbt-trino-1.4.1/dbt/include/trino/macros/materializations/
--rw-r--r--   0 runner    (1001) docker     (123)     8740 2023-03-01 15:52:55.000000 dbt-trino-1.4.1/dbt/include/trino/macros/materializations/incremental.sql
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-01 15:53:42.721257 dbt-trino-1.4.1/dbt/include/trino/macros/materializations/seeds/
--rw-r--r--   0 runner    (1001) docker     (123)     3547 2023-03-01 15:52:55.000000 dbt-trino-1.4.1/dbt/include/trino/macros/materializations/seeds/helpers.sql
--rw-r--r--   0 runner    (1001) docker     (123)     1206 2023-03-01 15:52:55.000000 dbt-trino-1.4.1/dbt/include/trino/macros/materializations/snapshot.sql
--rw-r--r--   0 runner    (1001) docker     (123)     2948 2023-03-01 15:52:55.000000 dbt-trino-1.4.1/dbt/include/trino/macros/materializations/table.sql
--rw-r--r--   0 runner    (1001) docker     (123)      267 2023-03-01 15:52:55.000000 dbt-trino-1.4.1/dbt/include/trino/macros/materializations/view.sql
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-01 15:53:42.725257 dbt-trino-1.4.1/dbt/include/trino/macros/utils/
--rw-r--r--   0 runner    (1001) docker     (123)       84 2023-03-01 15:52:55.000000 dbt-trino-1.4.1/dbt/include/trino/macros/utils/any_value.sql
--rw-r--r--   0 runner    (1001) docker     (123)      131 2023-03-01 15:52:55.000000 dbt-trino-1.4.1/dbt/include/trino/macros/utils/array_append.sql
--rw-r--r--   0 runner    (1001) docker     (123)      108 2023-03-01 15:52:55.000000 dbt-trino-1.4.1/dbt/include/trino/macros/utils/array_concat.sql
--rw-r--r--   0 runner    (1001) docker     (123)      179 2023-03-01 15:52:55.000000 dbt-trino-1.4.1/dbt/include/trino/macros/utils/array_construct.sql
--rw-r--r--   0 runner    (1001) docker     (123)       86 2023-03-01 15:52:55.000000 dbt-trino-1.4.1/dbt/include/trino/macros/utils/bool_or.sql
--rw-r--r--   0 runner    (1001) docker     (123)      256 2023-03-01 15:52:55.000000 dbt-trino-1.4.1/dbt/include/trino/macros/utils/datatypes.sql
--rw-r--r--   0 runner    (1001) docker     (123)      104 2023-03-01 15:52:55.000000 dbt-trino-1.4.1/dbt/include/trino/macros/utils/date_trunc.sql
--rw-r--r--   0 runner    (1001) docker     (123)      165 2023-03-01 15:52:55.000000 dbt-trino-1.4.1/dbt/include/trino/macros/utils/dateadd.sql
--rw-r--r--   0 runner    (1001) docker     (123)     2080 2023-03-01 15:52:55.000000 dbt-trino-1.4.1/dbt/include/trino/macros/utils/datediff.sql
--rw-r--r--   0 runner    (1001) docker     (123)      108 2023-03-01 15:52:55.000000 dbt-trino-1.4.1/dbt/include/trino/macros/utils/hash.sql
--rw-r--r--   0 runner    (1001) docker     (123)      477 2023-03-01 15:52:55.000000 dbt-trino-1.4.1/dbt/include/trino/macros/utils/listagg.sql
--rw-r--r--   0 runner    (1001) docker     (123)      215 2023-03-01 15:52:55.000000 dbt-trino-1.4.1/dbt/include/trino/macros/utils/right.sql
--rw-r--r--   0 runner    (1001) docker     (123)       95 2023-03-01 15:52:55.000000 dbt-trino-1.4.1/dbt/include/trino/macros/utils/safe_cast.sql
--rw-r--r--   0 runner    (1001) docker     (123)      295 2023-03-01 15:52:55.000000 dbt-trino-1.4.1/dbt/include/trino/macros/utils/split_part.sql
--rw-r--r--   0 runner    (1001) docker     (123)      230 2023-03-01 15:52:55.000000 dbt-trino-1.4.1/dbt/include/trino/macros/utils/timestamps.sql
--rw-r--r--   0 runner    (1001) docker     (123)      681 2023-03-01 15:52:55.000000 dbt-trino-1.4.1/dbt/include/trino/sample_profiles.yml
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-01 15:53:42.725257 dbt-trino-1.4.1/dbt_trino.egg-info/
--rw-r--r--   0 runner    (1001) docker     (123)    26488 2023-03-01 15:53:42.000000 dbt-trino-1.4.1/dbt_trino.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)     1581 2023-03-01 15:53:42.000000 dbt-trino-1.4.1/dbt_trino.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-03-01 15:53:42.000000 dbt-trino-1.4.1/dbt_trino.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-03-01 15:53:42.000000 dbt-trino-1.4.1/dbt_trino.egg-info/not-zip-safe
--rw-r--r--   0 runner    (1001) docker     (123)       31 2023-03-01 15:53:42.000000 dbt-trino-1.4.1/dbt_trino.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (123)        4 2023-03-01 15:53:42.000000 dbt-trino-1.4.1/dbt_trino.egg-info/top_level.txt
--rw-r--r--   0 runner    (1001) docker     (123)       38 2023-03-01 15:53:42.725257 dbt-trino-1.4.1/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (123)     3560 2023-03-01 15:52:55.000000 dbt-trino-1.4.1/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 10:35:53.851560 dbt-trino-1.4.2/
+-rw-r--r--   0 runner    (1001) docker     (123)    11357 2023-04-07 10:35:20.000000 dbt-trino-1.4.2/LICENSE.txt
+-rw-r--r--   0 runner    (1001) docker     (123)     5888 2023-04-07 10:35:53.851560 dbt-trino-1.4.2/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     5009 2023-04-07 10:35:20.000000 dbt-trino-1.4.2/README.md
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 10:35:53.847560 dbt-trino-1.4.2/dbt/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 10:35:53.847560 dbt-trino-1.4.2/dbt/adapters/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 10:35:53.847560 dbt-trino-1.4.2/dbt/adapters/trino/
+-rw-r--r--   0 runner    (1001) docker     (123)      565 2023-04-07 10:35:20.000000 dbt-trino-1.4.2/dbt/adapters/trino/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)       18 2023-04-07 10:35:20.000000 dbt-trino-1.4.2/dbt/adapters/trino/__version__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3408 2023-04-07 10:35:20.000000 dbt-trino-1.4.2/dbt/adapters/trino/column.py
+-rw-r--r--   0 runner    (1001) docker     (123)    16151 2023-04-07 10:35:20.000000 dbt-trino-1.4.2/dbt/adapters/trino/connections.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1728 2023-04-07 10:35:20.000000 dbt-trino-1.4.2/dbt/adapters/trino/impl.py
+-rw-r--r--   0 runner    (1001) docker     (123)      659 2023-04-07 10:35:20.000000 dbt-trino-1.4.2/dbt/adapters/trino/relation.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 10:35:53.847560 dbt-trino-1.4.2/dbt/include/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 10:35:53.847560 dbt-trino-1.4.2/dbt/include/trino/
+-rw-r--r--   0 runner    (1001) docker     (123)       52 2023-04-07 10:35:20.000000 dbt-trino-1.4.2/dbt/include/trino/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)       72 2023-04-07 10:35:20.000000 dbt-trino-1.4.2/dbt/include/trino/dbt_project.yml
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 10:35:53.847560 dbt-trino-1.4.2/dbt/include/trino/macros/
+-rw-r--r--   0 runner    (1001) docker     (123)     8980 2023-04-07 10:35:20.000000 dbt-trino-1.4.2/dbt/include/trino/macros/adapters.sql
+-rw-r--r--   0 runner    (1001) docker     (123)     1789 2023-04-07 10:35:20.000000 dbt-trino-1.4.2/dbt/include/trino/macros/apply_grants.sql
+-rw-r--r--   0 runner    (1001) docker     (123)     2189 2023-04-07 10:35:20.000000 dbt-trino-1.4.2/dbt/include/trino/macros/catalog.sql
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 10:35:53.847560 dbt-trino-1.4.2/dbt/include/trino/macros/materializations/
+-rw-r--r--   0 runner    (1001) docker     (123)     8740 2023-04-07 10:35:20.000000 dbt-trino-1.4.2/dbt/include/trino/macros/materializations/incremental.sql
+-rw-r--r--   0 runner    (1001) docker     (123)     2453 2023-04-07 10:35:20.000000 dbt-trino-1.4.2/dbt/include/trino/macros/materializations/materialized_view.sql
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 10:35:53.847560 dbt-trino-1.4.2/dbt/include/trino/macros/materializations/seeds/
+-rw-r--r--   0 runner    (1001) docker     (123)     3547 2023-04-07 10:35:20.000000 dbt-trino-1.4.2/dbt/include/trino/macros/materializations/seeds/helpers.sql
+-rw-r--r--   0 runner    (1001) docker     (123)     1206 2023-04-07 10:35:20.000000 dbt-trino-1.4.2/dbt/include/trino/macros/materializations/snapshot.sql
+-rw-r--r--   0 runner    (1001) docker     (123)     2948 2023-04-07 10:35:20.000000 dbt-trino-1.4.2/dbt/include/trino/macros/materializations/table.sql
+-rw-r--r--   0 runner    (1001) docker     (123)      267 2023-04-07 10:35:20.000000 dbt-trino-1.4.2/dbt/include/trino/macros/materializations/view.sql
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 10:35:53.851560 dbt-trino-1.4.2/dbt/include/trino/macros/utils/
+-rw-r--r--   0 runner    (1001) docker     (123)       84 2023-04-07 10:35:20.000000 dbt-trino-1.4.2/dbt/include/trino/macros/utils/any_value.sql
+-rw-r--r--   0 runner    (1001) docker     (123)      131 2023-04-07 10:35:20.000000 dbt-trino-1.4.2/dbt/include/trino/macros/utils/array_append.sql
+-rw-r--r--   0 runner    (1001) docker     (123)      108 2023-04-07 10:35:20.000000 dbt-trino-1.4.2/dbt/include/trino/macros/utils/array_concat.sql
+-rw-r--r--   0 runner    (1001) docker     (123)      179 2023-04-07 10:35:20.000000 dbt-trino-1.4.2/dbt/include/trino/macros/utils/array_construct.sql
+-rw-r--r--   0 runner    (1001) docker     (123)       86 2023-04-07 10:35:20.000000 dbt-trino-1.4.2/dbt/include/trino/macros/utils/bool_or.sql
+-rw-r--r--   0 runner    (1001) docker     (123)      256 2023-04-07 10:35:20.000000 dbt-trino-1.4.2/dbt/include/trino/macros/utils/datatypes.sql
+-rw-r--r--   0 runner    (1001) docker     (123)      104 2023-04-07 10:35:20.000000 dbt-trino-1.4.2/dbt/include/trino/macros/utils/date_trunc.sql
+-rw-r--r--   0 runner    (1001) docker     (123)      165 2023-04-07 10:35:20.000000 dbt-trino-1.4.2/dbt/include/trino/macros/utils/dateadd.sql
+-rw-r--r--   0 runner    (1001) docker     (123)     2080 2023-04-07 10:35:20.000000 dbt-trino-1.4.2/dbt/include/trino/macros/utils/datediff.sql
+-rw-r--r--   0 runner    (1001) docker     (123)      108 2023-04-07 10:35:20.000000 dbt-trino-1.4.2/dbt/include/trino/macros/utils/hash.sql
+-rw-r--r--   0 runner    (1001) docker     (123)      477 2023-04-07 10:35:20.000000 dbt-trino-1.4.2/dbt/include/trino/macros/utils/listagg.sql
+-rw-r--r--   0 runner    (1001) docker     (123)      215 2023-04-07 10:35:20.000000 dbt-trino-1.4.2/dbt/include/trino/macros/utils/right.sql
+-rw-r--r--   0 runner    (1001) docker     (123)       95 2023-04-07 10:35:20.000000 dbt-trino-1.4.2/dbt/include/trino/macros/utils/safe_cast.sql
+-rw-r--r--   0 runner    (1001) docker     (123)      295 2023-04-07 10:35:20.000000 dbt-trino-1.4.2/dbt/include/trino/macros/utils/split_part.sql
+-rw-r--r--   0 runner    (1001) docker     (123)      230 2023-04-07 10:35:20.000000 dbt-trino-1.4.2/dbt/include/trino/macros/utils/timestamps.sql
+-rw-r--r--   0 runner    (1001) docker     (123)      681 2023-04-07 10:35:20.000000 dbt-trino-1.4.2/dbt/include/trino/sample_profiles.yml
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 10:35:53.851560 dbt-trino-1.4.2/dbt_trino.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)     5888 2023-04-07 10:35:53.000000 dbt-trino-1.4.2/dbt_trino.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     1645 2023-04-07 10:35:53.000000 dbt-trino-1.4.2/dbt_trino.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-07 10:35:53.000000 dbt-trino-1.4.2/dbt_trino.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-07 10:35:53.000000 dbt-trino-1.4.2/dbt_trino.egg-info/not-zip-safe
+-rw-r--r--   0 runner    (1001) docker     (123)       29 2023-04-07 10:35:53.000000 dbt-trino-1.4.2/dbt_trino.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        4 2023-04-07 10:35:53.000000 dbt-trino-1.4.2/dbt_trino.egg-info/top_level.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       38 2023-04-07 10:35:53.851560 dbt-trino-1.4.2/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (123)     3558 2023-04-07 10:35:20.000000 dbt-trino-1.4.2/setup.py
```

### Comparing `dbt-trino-1.4.1/LICENSE.txt` & `dbt-trino-1.4.2/LICENSE.txt`

 * *Files identical despite different names*

### Comparing `dbt-trino-1.4.1/dbt/adapters/trino/__init__.py` & `dbt-trino-1.4.2/dbt/adapters/trino/__init__.py`

 * *Files identical despite different names*

### Comparing `dbt-trino-1.4.1/dbt/adapters/trino/column.py` & `dbt-trino-1.4.2/dbt/adapters/trino/column.py`

 * *Files identical despite different names*

### Comparing `dbt-trino-1.4.1/dbt/adapters/trino/connections.py` & `dbt-trino-1.4.2/dbt/adapters/trino/connections.py`

 * *Files 2% similar despite different names*

```diff
@@ -369,14 +369,20 @@
         elif isinstance(value, date):
             date_formatted = value.strftime("%Y-%m-%d")
             return "DATE '{}'".format(date_formatted)
         else:
             raise ValueError("Cannot escape {}".format(type(value)))
 
 
+@dataclass
+class TrinoAdapterResponse(AdapterResponse):
+    query: str = ""
+    query_id: str = ""
+
+
 class TrinoConnectionManager(SQLConnectionManager):
     TYPE = "trino"
 
     @contextmanager
     def exception_handler(self, sql):
         try:
             yield
@@ -440,23 +446,27 @@
             timezone=credentials.timezone,
         )
         connection.state = "open"
         connection.handle = ConnectionWrapper(trino_conn, credentials.prepared_statements_enabled)
         return connection
 
     @classmethod
-    def get_response(cls, cursor) -> AdapterResponse:
+    def get_response(cls, cursor) -> TrinoAdapterResponse:
         message = "SUCCESS"
-        return AdapterResponse(_message=message)
+        return TrinoAdapterResponse(
+            _message=message,
+            query=cursor._cursor.query,
+            query_id=cursor._cursor.query_id,
+            rows_affected=cursor._cursor.rowcount,
+        )  # type: ignore
 
     def cancel(self, connection):
         connection.handle.cancel()
 
     def add_query(self, sql, auto_begin=True, bindings=None, abridge_sql_log=False):
-
         connection = None
         cursor = None
 
         # TODO: is this sufficient? Largely copy+pasted from snowflake, so
         # there's some common behavior here we can maybe factor out into the
         # SQLAdapter?
         queries = [q.rstrip(";") for q in sqlparse.split(sql)]
```

### Comparing `dbt-trino-1.4.1/dbt/adapters/trino/impl.py` & `dbt-trino-1.4.2/dbt/adapters/trino/impl.py`

 * *Files identical despite different names*

### Comparing `dbt-trino-1.4.1/dbt/adapters/trino/relation.py` & `dbt-trino-1.4.2/dbt/adapters/trino/relation.py`

 * *Files identical despite different names*

### Comparing `dbt-trino-1.4.1/dbt/include/trino/macros/adapters.sql` & `dbt-trino-1.4.2/dbt/include/trino/macros/adapters.sql`

 * *Files 20% similar despite different names*

```diff
@@ -25,23 +25,28 @@
   {% do return(columns) %}
 {% endmacro %}
 
 
 {% macro trino__list_relations_without_caching(relation) %}
   {% call statement('list_relations_without_caching', fetch_result=True) -%}
     select
-      table_catalog as database,
-      table_name as name,
-      table_schema as schema,
-      case when table_type = 'BASE TABLE' then 'table'
-           when table_type = 'VIEW' then 'view'
-           else table_type
+      t.table_catalog as database,
+      t.table_name as name,
+      t.table_schema as schema,
+      case when mv.name is not null then 'materializedview'
+           when t.table_type = 'BASE TABLE' then 'table'
+           when t.table_type = 'VIEW' then 'view'
+           else t.table_type
       end as table_type
-    from {{ relation.information_schema() }}.tables
-    where table_schema = '{{ relation.schema | lower }}'
+    from {{ relation.information_schema() }}.tables t
+    left join system.metadata.materialized_views mv
+          on mv.catalog_name = t.table_catalog and mv.schema_name = t.table_schema and mv.name = t.table_name
+    where t.table_schema = '{{ relation.schema | lower }}'
+          and (mv.catalog_name is null or mv.catalog_name =  '{{ relation.database | lower }}')
+          and (mv.schema_name is null or mv.schema_name =  '{{ relation.schema | lower }}')
   {% endcall %}
   {{ return(load_result('list_relations_without_caching').table) }}
 {% endmacro %}
 
 
 {% macro trino__reset_csv_table(model, full_refresh, old_relation, agate_table) %}
     {{ adapter.drop_relation(old_relation) }}
@@ -107,16 +112,17 @@
   as
     {{ sql }}
   ;
 {% endmacro %}
 
 
 {% macro trino__drop_relation(relation) -%}
+  {% set relation_type = 'materialized view' if relation.type == 'materializedview' else relation.type %}
   {% call statement('drop_relation', auto_begin=False) -%}
-    drop {{ relation.type }} if exists {{ relation }}
+    drop {{ relation_type }} if exists {{ relation }}
   {%- endcall %}
 {% endmacro %}
 
 
 {# see this issue: https://github.com/dbt-labs/dbt/issues/2267 #}
 {% macro trino__information_schema_name(database) -%}
   {%- if database -%}
@@ -140,16 +146,17 @@
   {%- call statement('drop_schema') -%}
     drop schema if exists {{ relation }}
   {% endcall %}
 {% endmacro %}
 
 
 {% macro trino__rename_relation(from_relation, to_relation) -%}
+  {% set from_relation_type = 'materialized view' if from_relation.type == 'materializedview' else from_relation.type %}
   {% call statement('rename_relation') -%}
-    alter {{ from_relation.type }} {{ from_relation }} rename to {{ to_relation }}
+    alter {{ from_relation_type }} {{ from_relation }} rename to {{ to_relation }}
   {%- endcall %}
 {% endmacro %}
 
 
 {% macro trino__alter_relation_comment(relation, relation_comment) -%}
   comment on {{ relation.type }} {{ relation }} is '{{ relation_comment | replace("'", "''") }}';
 {% endmacro %}
@@ -214,7 +221,39 @@
   {% for column in remove_columns %}
     {% set sql -%}
       alter {{ relation.type }} {{ relation }} drop column {{ column.name }}
     {%- endset -%}
     {% do run_query(sql) %}
   {% endfor %}
 {% endmacro %}
+
+
+{% macro create_or_replace_view() %}
+  {%- set identifier = model['alias'] -%}
+
+  {%- set old_relation = adapter.get_relation(database=database, schema=schema, identifier=identifier) -%}
+  {%- set exists_as_view = (old_relation is not none and old_relation.is_view) -%}
+
+  {%- set target_relation = api.Relation.create(
+      identifier=identifier, schema=schema, database=database,
+      type='view') -%}
+  {% set grant_config = config.get('grants') %}
+
+  {{ run_hooks(pre_hooks) }}
+
+  -- If there is another object delete it
+  {%- if old_relation is not none and not old_relation.is_view -%}
+    {{ handle_existing_table(should_full_refresh(), old_relation) }}
+  {%- endif -%}
+
+  -- build model
+  {% call statement('main') -%}
+    {{ get_create_view_as_sql(target_relation, sql) }}
+  {%- endcall %}
+
+  {% set should_revoke = should_revoke(exists_as_view, full_refresh_mode=True) %}
+  {% do apply_grants(target_relation, grant_config, should_revoke=True) %}
+
+  {{ run_hooks(post_hooks) }}
+
+  {{ return({'relations': [target_relation]}) }}
+{% endmacro %}
```

### Comparing `dbt-trino-1.4.1/dbt/include/trino/macros/apply_grants.sql` & `dbt-trino-1.4.2/dbt/include/trino/macros/apply_grants.sql`

 * *Files identical despite different names*

### Comparing `dbt-trino-1.4.1/dbt/include/trino/macros/catalog.sql` & `dbt-trino-1.4.2/dbt/include/trino/macros/catalog.sql`

 * *Files 20% similar despite different names*

```diff
@@ -34,28 +34,32 @@
                 table_schema != 'information_schema'
                 and
                 table_schema in ('{{ schemas | join("','") | lower }}')
 
         ),
 
         table_comment as (
-
+            {%- for schema in schemas %}
             select
                 catalog_name as "table_database",
                 schema_name as "table_schema",
                 table_name as "table_name",
                 comment as "table_comment"
 
             from system.metadata.table_comments
             where
                 catalog_name = '{{ information_schema.database }}'
                 and
                 schema_name != 'information_schema'
                 and
-                schema_name in ('{{ schemas | join("','") | lower }}')
+                schema_name = '{{ schema | lower }}'
+            {% if not loop.last %}
+            union all
+            {% endif %}
+            {%- endfor %}
         )
 
         select *
         from tables
         join columns using ("table_database", "table_schema", "table_name")
         join table_comment using ("table_database", "table_schema", "table_name")
         order by "column_index"
```

### Comparing `dbt-trino-1.4.1/dbt/include/trino/macros/materializations/incremental.sql` & `dbt-trino-1.4.2/dbt/include/trino/macros/materializations/incremental.sql`

 * *Files identical despite different names*

### Comparing `dbt-trino-1.4.1/dbt/include/trino/macros/materializations/seeds/helpers.sql` & `dbt-trino-1.4.2/dbt/include/trino/macros/materializations/seeds/helpers.sql`

 * *Files identical despite different names*

### Comparing `dbt-trino-1.4.1/dbt/include/trino/macros/materializations/snapshot.sql` & `dbt-trino-1.4.2/dbt/include/trino/macros/materializations/snapshot.sql`

 * *Files identical despite different names*

### Comparing `dbt-trino-1.4.1/dbt/include/trino/macros/materializations/table.sql` & `dbt-trino-1.4.2/dbt/include/trino/macros/materializations/table.sql`

 * *Files identical despite different names*

### Comparing `dbt-trino-1.4.1/dbt/include/trino/macros/utils/datediff.sql` & `dbt-trino-1.4.2/dbt/include/trino/macros/utils/datediff.sql`

 * *Files identical despite different names*

### Comparing `dbt-trino-1.4.1/dbt/include/trino/sample_profiles.yml` & `dbt-trino-1.4.2/dbt/include/trino/sample_profiles.yml`

 * *Files identical despite different names*

### Comparing `dbt-trino-1.4.1/dbt_trino.egg-info/SOURCES.txt` & `dbt-trino-1.4.2/dbt_trino.egg-info/SOURCES.txt`

 * *Files 4% similar despite different names*

```diff
@@ -10,14 +10,15 @@
 dbt/include/trino/__init__.py
 dbt/include/trino/dbt_project.yml
 dbt/include/trino/sample_profiles.yml
 dbt/include/trino/macros/adapters.sql
 dbt/include/trino/macros/apply_grants.sql
 dbt/include/trino/macros/catalog.sql
 dbt/include/trino/macros/materializations/incremental.sql
+dbt/include/trino/macros/materializations/materialized_view.sql
 dbt/include/trino/macros/materializations/snapshot.sql
 dbt/include/trino/macros/materializations/table.sql
 dbt/include/trino/macros/materializations/view.sql
 dbt/include/trino/macros/materializations/seeds/helpers.sql
 dbt/include/trino/macros/utils/any_value.sql
 dbt/include/trino/macros/utils/array_append.sql
 dbt/include/trino/macros/utils/array_concat.sql
```

### Comparing `dbt-trino-1.4.1/setup.py` & `dbt-trino-1.4.2/setup.py`

 * *Files 2% similar despite different names*

```diff
@@ -82,15 +82,15 @@
             "include/trino/macros/*.sql",
             "include/trino/macros/*/*.sql",
             "include/trino/macros/*/*/*.sql",
         ]
     },
     install_requires=[
         "dbt-core~={}".format(dbt_version),
-        "trino==0.321.0",
+        "trino~=0.322",
     ],
     zip_safe=False,
     classifiers=[
         "Development Status :: 5 - Production/Stable",
         "License :: OSI Approved :: Apache Software License",
         "Operating System :: Microsoft :: Windows",
         "Operating System :: MacOS :: MacOS X",
```

