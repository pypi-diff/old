# Comparing `tmp/dbt_firebolt-1.4.0.tar.gz` & `tmp/dbt_firebolt-1.4.1.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "/home/runner/work/dbt-firebolt/dbt-firebolt/dist/.tmp-jknhqutq/dbt_firebolt-1.4.0.tar", last modified: Wed Mar 15 11:40:16 2023, max compression
+gzip compressed data, was "/home/runner/work/dbt-firebolt/dbt-firebolt/dist/.tmp-8orlw96t/dbt_firebolt-1.4.1.tar", last modified: Thu Apr  6 12:58:32 2023, max compression
```

## Comparing `dbt_firebolt-1.4.0.tar` & `dbt_firebolt-1.4.1.tar`

### file list

```diff
@@ -1,63 +1,63 @@
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-15 11:40:16.000000 dbt_firebolt-1.4.0/
--rw-r--r--   0 runner    (1001) docker     (123)    11354 2023-03-15 11:39:47.000000 dbt_firebolt-1.4.0/LICENSE
--rw-r--r--   0 runner    (1001) docker     (123)       54 2023-03-15 11:39:47.000000 dbt_firebolt-1.4.0/MANIFEST.in
--rw-r--r--   0 runner    (1001) docker     (123)     4055 2023-03-15 11:40:16.000000 dbt_firebolt-1.4.0/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)     3263 2023-03-15 11:39:47.000000 dbt_firebolt-1.4.0/README.md
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-15 11:40:16.000000 dbt_firebolt-1.4.0/dbt/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-15 11:40:16.000000 dbt_firebolt-1.4.0/dbt/adapters/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-15 11:40:16.000000 dbt_firebolt-1.4.0/dbt/adapters/firebolt/
--rw-r--r--   0 runner    (1001) docker     (123)      411 2023-03-15 11:40:04.000000 dbt_firebolt-1.4.0/dbt/adapters/firebolt/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)       69 2023-03-15 11:39:47.000000 dbt_firebolt-1.4.0/dbt/adapters/firebolt/__version__.py
--rw-r--r--   0 runner    (1001) docker     (123)      538 2023-03-15 11:39:47.000000 dbt_firebolt-1.4.0/dbt/adapters/firebolt/column.py
--rw-r--r--   0 runner    (1001) docker     (123)     4896 2023-03-15 11:39:47.000000 dbt_firebolt-1.4.0/dbt/adapters/firebolt/connections.py
--rw-r--r--   0 runner    (1001) docker     (123)    13013 2023-03-15 11:39:47.000000 dbt_firebolt-1.4.0/dbt/adapters/firebolt/impl.py
--rw-r--r--   0 runner    (1001) docker     (123)     1152 2023-03-15 11:39:47.000000 dbt_firebolt-1.4.0/dbt/adapters/firebolt/relation.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-15 11:40:16.000000 dbt_firebolt-1.4.0/dbt/include/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-15 11:40:16.000000 dbt_firebolt-1.4.0/dbt/include/firebolt/
--rw-r--r--   0 runner    (1001) docker     (123)       52 2023-03-15 11:39:47.000000 dbt_firebolt-1.4.0/dbt/include/firebolt/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)       76 2023-03-15 11:39:47.000000 dbt_firebolt-1.4.0/dbt/include/firebolt/dbt_project.yml
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-15 11:40:16.000000 dbt_firebolt-1.4.0/dbt/include/firebolt/macros/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-15 11:40:16.000000 dbt_firebolt-1.4.0/dbt/include/firebolt/macros/adapters/
--rw-r--r--   0 runner    (1001) docker     (123)      621 2023-03-15 11:39:47.000000 dbt_firebolt-1.4.0/dbt/include/firebolt/macros/adapters/apply_grants.sql
--rw-r--r--   0 runner    (1001) docker     (123)     2017 2023-03-15 11:39:47.000000 dbt_firebolt-1.4.0/dbt/include/firebolt/macros/adapters/relation.sql
--rw-r--r--   0 runner    (1001) docker     (123)     9326 2023-03-15 11:39:47.000000 dbt_firebolt-1.4.0/dbt/include/firebolt/macros/adapters.sql
--rw-r--r--   0 runner    (1001) docker     (123)     1312 2023-03-15 11:39:47.000000 dbt_firebolt-1.4.0/dbt/include/firebolt/macros/catalog.sql
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-15 11:40:16.000000 dbt_firebolt-1.4.0/dbt/include/firebolt/macros/dbt_external_tables/
--rw-r--r--   0 runner    (1001) docker     (123)     1669 2023-03-15 11:39:47.000000 dbt_firebolt-1.4.0/dbt/include/firebolt/macros/dbt_external_tables/create_external_table.sql
--rw-r--r--   0 runner    (1001) docker     (123)      167 2023-03-15 11:39:47.000000 dbt_firebolt-1.4.0/dbt/include/firebolt/macros/dbt_external_tables/dropif.sql
--rw-r--r--   0 runner    (1001) docker     (123)      894 2023-03-15 11:39:47.000000 dbt_firebolt-1.4.0/dbt/include/firebolt/macros/dbt_external_tables/get_external_build_plan.sql
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-15 11:40:16.000000 dbt_firebolt-1.4.0/dbt/include/firebolt/macros/materializations/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-15 11:40:16.000000 dbt_firebolt-1.4.0/dbt/include/firebolt/macros/materializations/models/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-15 11:40:16.000000 dbt_firebolt-1.4.0/dbt/include/firebolt/macros/materializations/models/incremental/
--rw-r--r--   0 runner    (1001) docker     (123)      917 2023-03-15 11:39:47.000000 dbt_firebolt-1.4.0/dbt/include/firebolt/macros/materializations/models/incremental/column_helpers.sql
--rw-r--r--   0 runner    (1001) docker     (123)     5744 2023-03-15 11:39:47.000000 dbt_firebolt-1.4.0/dbt/include/firebolt/macros/materializations/models/incremental/incremental.sql
--rw-r--r--   0 runner    (1001) docker     (123)      581 2023-03-15 11:39:47.000000 dbt_firebolt-1.4.0/dbt/include/firebolt/macros/materializations/models/incremental/is_incremental.sql
--rw-r--r--   0 runner    (1001) docker     (123)     3564 2023-03-15 11:39:47.000000 dbt_firebolt-1.4.0/dbt/include/firebolt/macros/materializations/models/incremental/on_schema_change.sql
--rw-r--r--   0 runner    (1001) docker     (123)     5743 2023-03-15 11:39:47.000000 dbt_firebolt-1.4.0/dbt/include/firebolt/macros/materializations/models/incremental/strategies.sql
--rw-r--r--   0 runner    (1001) docker     (123)     1564 2023-03-15 11:39:47.000000 dbt_firebolt-1.4.0/dbt/include/firebolt/macros/materializations/seed.sql
--rw-r--r--   0 runner    (1001) docker     (123)     1752 2023-03-15 11:39:47.000000 dbt_firebolt-1.4.0/dbt/include/firebolt/macros/materializations/table.sql
--rw-r--r--   0 runner    (1001) docker     (123)      474 2023-03-15 11:39:47.000000 dbt_firebolt-1.4.0/dbt/include/firebolt/macros/materializations/test.sql
--rw-r--r--   0 runner    (1001) docker     (123)     1706 2023-03-15 11:39:47.000000 dbt_firebolt-1.4.0/dbt/include/firebolt/macros/materializations/view.sql
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-15 11:40:16.000000 dbt_firebolt-1.4.0/dbt/include/firebolt/macros/utils/
--rw-r--r--   0 runner    (1001) docker     (123)      117 2023-03-15 11:39:47.000000 dbt_firebolt-1.4.0/dbt/include/firebolt/macros/utils/array_append.sql
--rw-r--r--   0 runner    (1001) docker     (123)      117 2023-03-15 11:39:47.000000 dbt_firebolt-1.4.0/dbt/include/firebolt/macros/utils/array_concat.sql
--rw-r--r--   0 runner    (1001) docker     (123)      105 2023-03-15 11:39:47.000000 dbt_firebolt-1.4.0/dbt/include/firebolt/macros/utils/array_construct.sql
--rw-r--r--   0 runner    (1001) docker     (123)       87 2023-03-15 11:39:47.000000 dbt_firebolt-1.4.0/dbt/include/firebolt/macros/utils/bool_or.sql
--rw-r--r--   0 runner    (1001) docker     (123)      180 2023-03-15 11:39:47.000000 dbt_firebolt-1.4.0/dbt/include/firebolt/macros/utils/cast_bool_to_text.sql
--rw-r--r--   0 runner    (1001) docker     (123)      202 2023-03-15 11:39:47.000000 dbt_firebolt-1.4.0/dbt/include/firebolt/macros/utils/dateadd.sql
--rw-r--r--   0 runner    (1001) docker     (123)      213 2023-03-15 11:39:47.000000 dbt_firebolt-1.4.0/dbt/include/firebolt/macros/utils/datediff.sql
--rw-r--r--   0 runner    (1001) docker     (123)      186 2023-03-15 11:39:47.000000 dbt_firebolt-1.4.0/dbt/include/firebolt/macros/utils/except.sql
--rw-r--r--   0 runner    (1001) docker     (123)      192 2023-03-15 11:39:47.000000 dbt_firebolt-1.4.0/dbt/include/firebolt/macros/utils/intersect.sql
--rw-r--r--   0 runner    (1001) docker     (123)      588 2023-03-15 11:39:47.000000 dbt_firebolt-1.4.0/dbt/include/firebolt/macros/utils/listagg.sql
--rw-r--r--   0 runner    (1001) docker     (123)      129 2023-03-15 11:39:47.000000 dbt_firebolt-1.4.0/dbt/include/firebolt/macros/utils/position.sql
--rw-r--r--   0 runner    (1001) docker     (123)      254 2023-03-15 11:39:47.000000 dbt_firebolt-1.4.0/dbt/include/firebolt/macros/utils/right.sql
--rw-r--r--   0 runner    (1001) docker     (123)      464 2023-03-15 11:39:47.000000 dbt_firebolt-1.4.0/dbt/include/firebolt/macros/utils/split_part.sql
--rw-r--r--   0 runner    (1001) docker     (123)      397 2023-03-15 11:39:47.000000 dbt_firebolt-1.4.0/dbt/include/firebolt/macros/utils/timestamps.sql
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-15 11:40:16.000000 dbt_firebolt-1.4.0/dbt_firebolt.egg-info/
--rw-r--r--   0 runner    (1001) docker     (123)     4055 2023-03-15 11:40:16.000000 dbt_firebolt-1.4.0/dbt_firebolt.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)     2283 2023-03-15 11:40:16.000000 dbt_firebolt-1.4.0/dbt_firebolt.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-03-15 11:40:16.000000 dbt_firebolt-1.4.0/dbt_firebolt.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (123)      108 2023-03-15 11:40:16.000000 dbt_firebolt-1.4.0/dbt_firebolt.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (123)        4 2023-03-15 11:40:16.000000 dbt_firebolt-1.4.0/dbt_firebolt.egg-info/top_level.txt
--rwxr-xr-x   0 runner    (1001) docker     (123)      472 2023-03-15 11:39:47.000000 dbt_firebolt-1.4.0/pyproject.toml
--rw-r--r--   0 runner    (1001) docker     (123)     1928 2023-03-15 11:40:16.000000 dbt_firebolt-1.4.0/setup.cfg
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 12:58:32.000000 dbt_firebolt-1.4.1/
+-rw-r--r--   0 runner    (1001) docker     (123)    11354 2023-04-06 12:58:08.000000 dbt_firebolt-1.4.1/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (123)       54 2023-04-06 12:58:08.000000 dbt_firebolt-1.4.1/MANIFEST.in
+-rw-r--r--   0 runner    (1001) docker     (123)     4055 2023-04-06 12:58:32.000000 dbt_firebolt-1.4.1/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     3263 2023-04-06 12:58:08.000000 dbt_firebolt-1.4.1/README.md
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 12:58:32.000000 dbt_firebolt-1.4.1/dbt/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 12:58:32.000000 dbt_firebolt-1.4.1/dbt/adapters/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 12:58:32.000000 dbt_firebolt-1.4.1/dbt/adapters/firebolt/
+-rw-r--r--   0 runner    (1001) docker     (123)      411 2023-04-06 12:58:22.000000 dbt_firebolt-1.4.1/dbt/adapters/firebolt/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)       69 2023-04-06 12:58:08.000000 dbt_firebolt-1.4.1/dbt/adapters/firebolt/__version__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      538 2023-04-06 12:58:08.000000 dbt_firebolt-1.4.1/dbt/adapters/firebolt/column.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5026 2023-04-06 12:58:08.000000 dbt_firebolt-1.4.1/dbt/adapters/firebolt/connections.py
+-rw-r--r--   0 runner    (1001) docker     (123)    13013 2023-04-06 12:58:08.000000 dbt_firebolt-1.4.1/dbt/adapters/firebolt/impl.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1152 2023-04-06 12:58:08.000000 dbt_firebolt-1.4.1/dbt/adapters/firebolt/relation.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 12:58:32.000000 dbt_firebolt-1.4.1/dbt/include/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 12:58:32.000000 dbt_firebolt-1.4.1/dbt/include/firebolt/
+-rw-r--r--   0 runner    (1001) docker     (123)       52 2023-04-06 12:58:08.000000 dbt_firebolt-1.4.1/dbt/include/firebolt/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)       76 2023-04-06 12:58:08.000000 dbt_firebolt-1.4.1/dbt/include/firebolt/dbt_project.yml
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 12:58:32.000000 dbt_firebolt-1.4.1/dbt/include/firebolt/macros/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 12:58:32.000000 dbt_firebolt-1.4.1/dbt/include/firebolt/macros/adapters/
+-rw-r--r--   0 runner    (1001) docker     (123)     1095 2023-04-06 12:58:08.000000 dbt_firebolt-1.4.1/dbt/include/firebolt/macros/adapters/apply_grants.sql
+-rw-r--r--   0 runner    (1001) docker     (123)     2017 2023-04-06 12:58:08.000000 dbt_firebolt-1.4.1/dbt/include/firebolt/macros/adapters/relation.sql
+-rw-r--r--   0 runner    (1001) docker     (123)     9326 2023-04-06 12:58:08.000000 dbt_firebolt-1.4.1/dbt/include/firebolt/macros/adapters.sql
+-rw-r--r--   0 runner    (1001) docker     (123)     1312 2023-04-06 12:58:08.000000 dbt_firebolt-1.4.1/dbt/include/firebolt/macros/catalog.sql
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 12:58:32.000000 dbt_firebolt-1.4.1/dbt/include/firebolt/macros/dbt_external_tables/
+-rw-r--r--   0 runner    (1001) docker     (123)     1669 2023-04-06 12:58:08.000000 dbt_firebolt-1.4.1/dbt/include/firebolt/macros/dbt_external_tables/create_external_table.sql
+-rw-r--r--   0 runner    (1001) docker     (123)      167 2023-04-06 12:58:08.000000 dbt_firebolt-1.4.1/dbt/include/firebolt/macros/dbt_external_tables/dropif.sql
+-rw-r--r--   0 runner    (1001) docker     (123)      894 2023-04-06 12:58:08.000000 dbt_firebolt-1.4.1/dbt/include/firebolt/macros/dbt_external_tables/get_external_build_plan.sql
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 12:58:32.000000 dbt_firebolt-1.4.1/dbt/include/firebolt/macros/materializations/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 12:58:32.000000 dbt_firebolt-1.4.1/dbt/include/firebolt/macros/materializations/models/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 12:58:32.000000 dbt_firebolt-1.4.1/dbt/include/firebolt/macros/materializations/models/incremental/
+-rw-r--r--   0 runner    (1001) docker     (123)      917 2023-04-06 12:58:08.000000 dbt_firebolt-1.4.1/dbt/include/firebolt/macros/materializations/models/incremental/column_helpers.sql
+-rw-r--r--   0 runner    (1001) docker     (123)     5744 2023-04-06 12:58:08.000000 dbt_firebolt-1.4.1/dbt/include/firebolt/macros/materializations/models/incremental/incremental.sql
+-rw-r--r--   0 runner    (1001) docker     (123)      581 2023-04-06 12:58:08.000000 dbt_firebolt-1.4.1/dbt/include/firebolt/macros/materializations/models/incremental/is_incremental.sql
+-rw-r--r--   0 runner    (1001) docker     (123)     3564 2023-04-06 12:58:08.000000 dbt_firebolt-1.4.1/dbt/include/firebolt/macros/materializations/models/incremental/on_schema_change.sql
+-rw-r--r--   0 runner    (1001) docker     (123)     5743 2023-04-06 12:58:08.000000 dbt_firebolt-1.4.1/dbt/include/firebolt/macros/materializations/models/incremental/strategies.sql
+-rw-r--r--   0 runner    (1001) docker     (123)     1564 2023-04-06 12:58:08.000000 dbt_firebolt-1.4.1/dbt/include/firebolt/macros/materializations/seed.sql
+-rw-r--r--   0 runner    (1001) docker     (123)     1752 2023-04-06 12:58:08.000000 dbt_firebolt-1.4.1/dbt/include/firebolt/macros/materializations/table.sql
+-rw-r--r--   0 runner    (1001) docker     (123)      474 2023-04-06 12:58:08.000000 dbt_firebolt-1.4.1/dbt/include/firebolt/macros/materializations/test.sql
+-rw-r--r--   0 runner    (1001) docker     (123)     1706 2023-04-06 12:58:08.000000 dbt_firebolt-1.4.1/dbt/include/firebolt/macros/materializations/view.sql
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 12:58:32.000000 dbt_firebolt-1.4.1/dbt/include/firebolt/macros/utils/
+-rw-r--r--   0 runner    (1001) docker     (123)      117 2023-04-06 12:58:08.000000 dbt_firebolt-1.4.1/dbt/include/firebolt/macros/utils/array_append.sql
+-rw-r--r--   0 runner    (1001) docker     (123)      117 2023-04-06 12:58:08.000000 dbt_firebolt-1.4.1/dbt/include/firebolt/macros/utils/array_concat.sql
+-rw-r--r--   0 runner    (1001) docker     (123)      105 2023-04-06 12:58:08.000000 dbt_firebolt-1.4.1/dbt/include/firebolt/macros/utils/array_construct.sql
+-rw-r--r--   0 runner    (1001) docker     (123)       87 2023-04-06 12:58:08.000000 dbt_firebolt-1.4.1/dbt/include/firebolt/macros/utils/bool_or.sql
+-rw-r--r--   0 runner    (1001) docker     (123)      180 2023-04-06 12:58:08.000000 dbt_firebolt-1.4.1/dbt/include/firebolt/macros/utils/cast_bool_to_text.sql
+-rw-r--r--   0 runner    (1001) docker     (123)      202 2023-04-06 12:58:08.000000 dbt_firebolt-1.4.1/dbt/include/firebolt/macros/utils/dateadd.sql
+-rw-r--r--   0 runner    (1001) docker     (123)      213 2023-04-06 12:58:08.000000 dbt_firebolt-1.4.1/dbt/include/firebolt/macros/utils/datediff.sql
+-rw-r--r--   0 runner    (1001) docker     (123)      186 2023-04-06 12:58:08.000000 dbt_firebolt-1.4.1/dbt/include/firebolt/macros/utils/except.sql
+-rw-r--r--   0 runner    (1001) docker     (123)      192 2023-04-06 12:58:08.000000 dbt_firebolt-1.4.1/dbt/include/firebolt/macros/utils/intersect.sql
+-rw-r--r--   0 runner    (1001) docker     (123)      588 2023-04-06 12:58:08.000000 dbt_firebolt-1.4.1/dbt/include/firebolt/macros/utils/listagg.sql
+-rw-r--r--   0 runner    (1001) docker     (123)      129 2023-04-06 12:58:08.000000 dbt_firebolt-1.4.1/dbt/include/firebolt/macros/utils/position.sql
+-rw-r--r--   0 runner    (1001) docker     (123)      254 2023-04-06 12:58:08.000000 dbt_firebolt-1.4.1/dbt/include/firebolt/macros/utils/right.sql
+-rw-r--r--   0 runner    (1001) docker     (123)      464 2023-04-06 12:58:08.000000 dbt_firebolt-1.4.1/dbt/include/firebolt/macros/utils/split_part.sql
+-rw-r--r--   0 runner    (1001) docker     (123)      397 2023-04-06 12:58:08.000000 dbt_firebolt-1.4.1/dbt/include/firebolt/macros/utils/timestamps.sql
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 12:58:32.000000 dbt_firebolt-1.4.1/dbt_firebolt.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)     4055 2023-04-06 12:58:32.000000 dbt_firebolt-1.4.1/dbt_firebolt.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     2283 2023-04-06 12:58:32.000000 dbt_firebolt-1.4.1/dbt_firebolt.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-06 12:58:32.000000 dbt_firebolt-1.4.1/dbt_firebolt.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)      108 2023-04-06 12:58:32.000000 dbt_firebolt-1.4.1/dbt_firebolt.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        4 2023-04-06 12:58:32.000000 dbt_firebolt-1.4.1/dbt_firebolt.egg-info/top_level.txt
+-rwxr-xr-x   0 runner    (1001) docker     (123)      472 2023-04-06 12:58:08.000000 dbt_firebolt-1.4.1/pyproject.toml
+-rw-r--r--   0 runner    (1001) docker     (123)     1928 2023-04-06 12:58:32.000000 dbt_firebolt-1.4.1/setup.cfg
```

### Comparing `dbt_firebolt-1.4.0/LICENSE` & `dbt_firebolt-1.4.1/LICENSE`

 * *Files identical despite different names*

### Comparing `dbt_firebolt-1.4.0/PKG-INFO` & `dbt_firebolt-1.4.1/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: dbt_firebolt
-Version: 1.4.0
+Version: 1.4.1
 Summary: The Firebolt adapter plugin for dbt (data build tool)
 Home-page: https://github.com/firebolt-db/dbt-firebolt
 Author: Firebolt
 Author-email: support@firebolt.io
 License: Apache-2.0
 Project-URL: Bug Tracker, https://github.com/firebolt-db/dbt-firebolt/issues
 Classifier: License :: OSI Approved :: Apache Software License
```

### Comparing `dbt_firebolt-1.4.0/README.md` & `dbt_firebolt-1.4.1/README.md`

 * *Files identical despite different names*

### Comparing `dbt_firebolt-1.4.0/dbt/adapters/firebolt/column.py` & `dbt_firebolt-1.4.1/dbt/adapters/firebolt/column.py`

 * *Files identical despite different names*

### Comparing `dbt_firebolt-1.4.0/dbt/adapters/firebolt/connections.py` & `dbt_firebolt-1.4.1/dbt/adapters/firebolt/connections.py`

 * *Files 2% similar despite different names*

```diff
@@ -5,14 +5,15 @@
 import dbt.exceptions
 from dbt.adapters.base import Credentials
 from dbt.adapters.sql import SQLConnectionManager
 from dbt.contracts.connection import (
     AdapterRequiredConfig,
     AdapterResponse,
     Connection,
+    QueryComment,
 )
 from dbt.events import AdapterLogger  # type: ignore
 from dbt.exceptions import DbtRuntimeError
 from firebolt.client import DEFAULT_API_URL
 from firebolt.client.auth import UsernamePassword
 from firebolt.db import connect as sdk_connect
 from firebolt.db.connection import Connection as SDKConnection
@@ -76,14 +77,16 @@
     """
 
     TYPE = 'firebolt'
 
     def __init__(self, profile: AdapterRequiredConfig):
         # Query comment in appent mode only
         # This allows clearer view of queries in query_history
+        if not hasattr(profile, 'query_comment'):
+            setattr(profile, 'query_comment', QueryComment())
         profile.query_comment.append = True
         super().__init__(profile)
 
     def __str__(self) -> str:
         return 'FireboltConnectionManager()'
 
     @classmethod
```

### Comparing `dbt_firebolt-1.4.0/dbt/adapters/firebolt/impl.py` & `dbt_firebolt-1.4.1/dbt/adapters/firebolt/impl.py`

 * *Files identical despite different names*

### Comparing `dbt_firebolt-1.4.0/dbt/adapters/firebolt/relation.py` & `dbt_firebolt-1.4.1/dbt/adapters/firebolt/relation.py`

 * *Files identical despite different names*

### Comparing `dbt_firebolt-1.4.0/dbt/include/firebolt/macros/adapters/relation.sql` & `dbt_firebolt-1.4.1/dbt/include/firebolt/macros/adapters/relation.sql`

 * *Files identical despite different names*

### Comparing `dbt_firebolt-1.4.0/dbt/include/firebolt/macros/adapters.sql` & `dbt_firebolt-1.4.1/dbt/include/firebolt/macros/adapters.sql`

 * *Files identical despite different names*

### Comparing `dbt_firebolt-1.4.0/dbt/include/firebolt/macros/catalog.sql` & `dbt_firebolt-1.4.1/dbt/include/firebolt/macros/catalog.sql`

 * *Files identical despite different names*

### Comparing `dbt_firebolt-1.4.0/dbt/include/firebolt/macros/dbt_external_tables/create_external_table.sql` & `dbt_firebolt-1.4.1/dbt/include/firebolt/macros/dbt_external_tables/create_external_table.sql`

 * *Files identical despite different names*

### Comparing `dbt_firebolt-1.4.0/dbt/include/firebolt/macros/dbt_external_tables/get_external_build_plan.sql` & `dbt_firebolt-1.4.1/dbt/include/firebolt/macros/dbt_external_tables/get_external_build_plan.sql`

 * *Files identical despite different names*

### Comparing `dbt_firebolt-1.4.0/dbt/include/firebolt/macros/materializations/models/incremental/column_helpers.sql` & `dbt_firebolt-1.4.1/dbt/include/firebolt/macros/materializations/models/incremental/column_helpers.sql`

 * *Files identical despite different names*

### Comparing `dbt_firebolt-1.4.0/dbt/include/firebolt/macros/materializations/models/incremental/incremental.sql` & `dbt_firebolt-1.4.1/dbt/include/firebolt/macros/materializations/models/incremental/incremental.sql`

 * *Files identical despite different names*

### Comparing `dbt_firebolt-1.4.0/dbt/include/firebolt/macros/materializations/models/incremental/is_incremental.sql` & `dbt_firebolt-1.4.1/dbt/include/firebolt/macros/materializations/models/incremental/is_incremental.sql`

 * *Files identical despite different names*

### Comparing `dbt_firebolt-1.4.0/dbt/include/firebolt/macros/materializations/models/incremental/on_schema_change.sql` & `dbt_firebolt-1.4.1/dbt/include/firebolt/macros/materializations/models/incremental/on_schema_change.sql`

 * *Files identical despite different names*

### Comparing `dbt_firebolt-1.4.0/dbt/include/firebolt/macros/materializations/models/incremental/strategies.sql` & `dbt_firebolt-1.4.1/dbt/include/firebolt/macros/materializations/models/incremental/strategies.sql`

 * *Files identical despite different names*

### Comparing `dbt_firebolt-1.4.0/dbt/include/firebolt/macros/materializations/seed.sql` & `dbt_firebolt-1.4.1/dbt/include/firebolt/macros/materializations/seed.sql`

 * *Files identical despite different names*

### Comparing `dbt_firebolt-1.4.0/dbt/include/firebolt/macros/materializations/table.sql` & `dbt_firebolt-1.4.1/dbt/include/firebolt/macros/materializations/table.sql`

 * *Files identical despite different names*

### Comparing `dbt_firebolt-1.4.0/dbt/include/firebolt/macros/materializations/view.sql` & `dbt_firebolt-1.4.1/dbt/include/firebolt/macros/materializations/view.sql`

 * *Files identical despite different names*

### Comparing `dbt_firebolt-1.4.0/dbt/include/firebolt/macros/utils/listagg.sql` & `dbt_firebolt-1.4.1/dbt/include/firebolt/macros/utils/listagg.sql`

 * *Files identical despite different names*

### Comparing `dbt_firebolt-1.4.0/dbt_firebolt.egg-info/PKG-INFO` & `dbt_firebolt-1.4.1/dbt_firebolt.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: dbt-firebolt
-Version: 1.4.0
+Version: 1.4.1
 Summary: The Firebolt adapter plugin for dbt (data build tool)
 Home-page: https://github.com/firebolt-db/dbt-firebolt
 Author: Firebolt
 Author-email: support@firebolt.io
 License: Apache-2.0
 Project-URL: Bug Tracker, https://github.com/firebolt-db/dbt-firebolt/issues
 Classifier: License :: OSI Approved :: Apache Software License
```

### Comparing `dbt_firebolt-1.4.0/dbt_firebolt.egg-info/SOURCES.txt` & `dbt_firebolt-1.4.1/dbt_firebolt.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `dbt_firebolt-1.4.0/setup.cfg` & `dbt_firebolt-1.4.1/setup.cfg`

 * *Files identical despite different names*

