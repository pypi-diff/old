# Comparing `tmp/sqlglot-9.0.5.tar.gz` & `tmp/sqlglot-9.0.6.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "sqlglot-9.0.5.tar", last modified: Wed Oct 26 22:38:44 2022, max compression
+gzip compressed data, was "sqlglot-9.0.6.tar", last modified: Sat Oct 29 19:31:34 2022, max compression
```

## Comparing `sqlglot-9.0.5.tar` & `sqlglot-9.0.6.tar`

### file list

```diff
@@ -1,88 +1,88 @@
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-10-26 22:38:44.419385 sqlglot-9.0.5/
--rw-r--r--   0 runner    (1001) docker     (121)     1065 2022-10-26 22:38:34.000000 sqlglot-9.0.5/LICENSE
--rw-r--r--   0 runner    (1001) docker     (121)    10762 2022-10-26 22:38:44.419385 sqlglot-9.0.5/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (121)    10137 2022-10-26 22:38:34.000000 sqlglot-9.0.5/README.md
--rw-r--r--   0 runner    (1001) docker     (121)      279 2022-10-26 22:38:44.419385 sqlglot-9.0.5/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (121)      971 2022-10-26 22:38:34.000000 sqlglot-9.0.5/setup.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-10-26 22:38:44.415385 sqlglot-9.0.5/sqlglot/
--rw-r--r--   0 runner    (1001) docker     (121)     3299 2022-10-26 22:38:34.000000 sqlglot-9.0.5/sqlglot/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     1433 2022-10-26 22:38:34.000000 sqlglot-9.0.5/sqlglot/__main__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-10-26 22:38:44.415385 sqlglot-9.0.5/sqlglot/dataframe/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-10-26 22:38:34.000000 sqlglot-9.0.5/sqlglot/dataframe/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-10-26 22:38:44.415385 sqlglot-9.0.5/sqlglot/dataframe/sql/
--rw-r--r--   0 runner    (1001) docker     (121)      560 2022-10-26 22:38:34.000000 sqlglot-9.0.5/sqlglot/dataframe/sql/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    12000 2022-10-26 22:38:34.000000 sqlglot-9.0.5/sqlglot/dataframe/sql/column.py
--rw-r--r--   0 runner    (1001) docker     (121)    33120 2022-10-26 22:38:34.000000 sqlglot-9.0.5/sqlglot/dataframe/sql/dataframe.py
--rw-r--r--   0 runner    (1001) docker     (121)    40799 2022-10-26 22:38:34.000000 sqlglot-9.0.5/sqlglot/dataframe/sql/functions.py
--rw-r--r--   0 runner    (1001) docker     (121)     2148 2022-10-26 22:38:34.000000 sqlglot-9.0.5/sqlglot/dataframe/sql/group.py
--rw-r--r--   0 runner    (1001) docker     (121)     3207 2022-10-26 22:38:34.000000 sqlglot-9.0.5/sqlglot/dataframe/sql/normalize.py
--rw-r--r--   0 runner    (1001) docker     (121)     1776 2022-10-26 22:38:34.000000 sqlglot-9.0.5/sqlglot/dataframe/sql/operations.py
--rw-r--r--   0 runner    (1001) docker     (121)     2736 2022-10-26 22:38:34.000000 sqlglot-9.0.5/sqlglot/dataframe/sql/readwriter.py
--rw-r--r--   0 runner    (1001) docker     (121)     5346 2022-10-26 22:38:34.000000 sqlglot-9.0.5/sqlglot/dataframe/sql/session.py
--rw-r--r--   0 runner    (1001) docker     (121)      301 2022-10-26 22:38:34.000000 sqlglot-9.0.5/sqlglot/dataframe/sql/transforms.py
--rw-r--r--   0 runner    (1001) docker     (121)     5156 2022-10-26 22:38:34.000000 sqlglot-9.0.5/sqlglot/dataframe/sql/types.py
--rw-r--r--   0 runner    (1001) docker     (121)     1160 2022-10-26 22:38:34.000000 sqlglot-9.0.5/sqlglot/dataframe/sql/util.py
--rw-r--r--   0 runner    (1001) docker     (121)     4460 2022-10-26 22:38:34.000000 sqlglot-9.0.5/sqlglot/dataframe/sql/window.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-10-26 22:38:44.419385 sqlglot-9.0.5/sqlglot/dialects/
--rw-r--r--   0 runner    (1001) docker     (121)      814 2022-10-26 22:38:34.000000 sqlglot-9.0.5/sqlglot/dialects/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     7106 2022-10-26 22:38:34.000000 sqlglot-9.0.5/sqlglot/dialects/bigquery.py
--rw-r--r--   0 runner    (1001) docker     (121)     2435 2022-10-26 22:38:34.000000 sqlglot-9.0.5/sqlglot/dialects/clickhouse.py
--rw-r--r--   0 runner    (1001) docker     (121)      716 2022-10-26 22:38:34.000000 sqlglot-9.0.5/sqlglot/dialects/databricks.py
--rw-r--r--   0 runner    (1001) docker     (121)    11615 2022-10-26 22:38:34.000000 sqlglot-9.0.5/sqlglot/dialects/dialect.py
--rw-r--r--   0 runner    (1001) docker     (121)     6964 2022-10-26 22:38:34.000000 sqlglot-9.0.5/sqlglot/dialects/duckdb.py
--rw-r--r--   0 runner    (1001) docker     (121)    11555 2022-10-26 22:38:34.000000 sqlglot-9.0.5/sqlglot/dialects/hive.py
--rw-r--r--   0 runner    (1001) docker     (121)     7134 2022-10-26 22:38:34.000000 sqlglot-9.0.5/sqlglot/dialects/mysql.py
--rw-r--r--   0 runner    (1001) docker     (121)     3957 2022-10-26 22:38:34.000000 sqlglot-9.0.5/sqlglot/dialects/oracle.py
--rw-r--r--   0 runner    (1001) docker     (121)     8452 2022-10-26 22:38:34.000000 sqlglot-9.0.5/sqlglot/dialects/postgres.py
--rw-r--r--   0 runner    (1001) docker     (121)     9254 2022-10-26 22:38:34.000000 sqlglot-9.0.5/sqlglot/dialects/presto.py
--rw-r--r--   0 runner    (1001) docker     (121)      986 2022-10-26 22:38:34.000000 sqlglot-9.0.5/sqlglot/dialects/redshift.py
--rw-r--r--   0 runner    (1001) docker     (121)     7146 2022-10-26 22:38:34.000000 sqlglot-9.0.5/sqlglot/dialects/snowflake.py
--rw-r--r--   0 runner    (1001) docker     (121)     5008 2022-10-26 22:38:34.000000 sqlglot-9.0.5/sqlglot/dialects/spark.py
--rw-r--r--   0 runner    (1001) docker     (121)     2089 2022-10-26 22:38:34.000000 sqlglot-9.0.5/sqlglot/dialects/sqlite.py
--rw-r--r--   0 runner    (1001) docker     (121)     1002 2022-10-26 22:38:34.000000 sqlglot-9.0.5/sqlglot/dialects/starrocks.py
--rw-r--r--   0 runner    (1001) docker     (121)     1097 2022-10-26 22:38:34.000000 sqlglot-9.0.5/sqlglot/dialects/tableau.py
--rw-r--r--   0 runner    (1001) docker     (121)      393 2022-10-26 22:38:34.000000 sqlglot-9.0.5/sqlglot/dialects/trino.py
--rw-r--r--   0 runner    (1001) docker     (121)     8134 2022-10-26 22:38:34.000000 sqlglot-9.0.5/sqlglot/dialects/tsql.py
--rw-r--r--   0 runner    (1001) docker     (121)    10793 2022-10-26 22:38:34.000000 sqlglot-9.0.5/sqlglot/diff.py
--rw-r--r--   0 runner    (1001) docker     (121)      799 2022-10-26 22:38:34.000000 sqlglot-9.0.5/sqlglot/errors.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-10-26 22:38:44.419385 sqlglot-9.0.5/sqlglot/executor/
--rw-r--r--   0 runner    (1001) docker     (121)     1367 2022-10-26 22:38:34.000000 sqlglot-9.0.5/sqlglot/executor/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     2157 2022-10-26 22:38:34.000000 sqlglot-9.0.5/sqlglot/executor/context.py
--rw-r--r--   0 runner    (1001) docker     (121)      652 2022-10-26 22:38:34.000000 sqlglot-9.0.5/sqlglot/executor/env.py
--rw-r--r--   0 runner    (1001) docker     (121)    11871 2022-10-26 22:38:34.000000 sqlglot-9.0.5/sqlglot/executor/python.py
--rw-r--r--   0 runner    (1001) docker     (121)     1984 2022-10-26 22:38:34.000000 sqlglot-9.0.5/sqlglot/executor/table.py
--rw-r--r--   0 runner    (1001) docker     (121)    96511 2022-10-26 22:38:34.000000 sqlglot-9.0.5/sqlglot/expressions.py
--rw-r--r--   0 runner    (1001) docker     (121)    49033 2022-10-26 22:38:34.000000 sqlglot-9.0.5/sqlglot/generator.py
--rw-r--r--   0 runner    (1001) docker     (121)     5941 2022-10-26 22:38:34.000000 sqlglot-9.0.5/sqlglot/helper.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-10-26 22:38:44.419385 sqlglot-9.0.5/sqlglot/optimizer/
--rw-r--r--   0 runner    (1001) docker     (121)       56 2022-10-26 22:38:34.000000 sqlglot-9.0.5/sqlglot/optimizer/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    15489 2022-10-26 22:38:34.000000 sqlglot-9.0.5/sqlglot/optimizer/annotate_types.py
--rw-r--r--   0 runner    (1001) docker     (121)     1357 2022-10-26 22:38:34.000000 sqlglot-9.0.5/sqlglot/optimizer/eliminate_ctes.py
--rw-r--r--   0 runner    (1001) docker     (121)     5345 2022-10-26 22:38:34.000000 sqlglot-9.0.5/sqlglot/optimizer/eliminate_joins.py
--rw-r--r--   0 runner    (1001) docker     (121)     4879 2022-10-26 22:38:34.000000 sqlglot-9.0.5/sqlglot/optimizer/eliminate_subqueries.py
--rw-r--r--   0 runner    (1001) docker     (121)      385 2022-10-26 22:38:34.000000 sqlglot-9.0.5/sqlglot/optimizer/expand_multi_table_selects.py
--rw-r--r--   0 runner    (1001) docker     (121)      849 2022-10-26 22:38:34.000000 sqlglot-9.0.5/sqlglot/optimizer/isolate_table_selects.py
--rw-r--r--   0 runner    (1001) docker     (121)    12382 2022-10-26 22:38:34.000000 sqlglot-9.0.5/sqlglot/optimizer/merge_subqueries.py
--rw-r--r--   0 runner    (1001) docker     (121)     4110 2022-10-26 22:38:34.000000 sqlglot-9.0.5/sqlglot/optimizer/normalize.py
--rw-r--r--   0 runner    (1001) docker     (121)     2258 2022-10-26 22:38:34.000000 sqlglot-9.0.5/sqlglot/optimizer/optimize_joins.py
--rw-r--r--   0 runner    (1001) docker     (121)     2807 2022-10-26 22:38:34.000000 sqlglot-9.0.5/sqlglot/optimizer/optimizer.py
--rw-r--r--   0 runner    (1001) docker     (121)     6210 2022-10-26 22:38:34.000000 sqlglot-9.0.5/sqlglot/optimizer/pushdown_predicates.py
--rw-r--r--   0 runner    (1001) docker     (121)     4048 2022-10-26 22:38:34.000000 sqlglot-9.0.5/sqlglot/optimizer/pushdown_projections.py
--rw-r--r--   0 runner    (1001) docker     (121)    14716 2022-10-26 22:38:34.000000 sqlglot-9.0.5/sqlglot/optimizer/qualify_columns.py
--rw-r--r--   0 runner    (1001) docker     (121)     1793 2022-10-26 22:38:34.000000 sqlglot-9.0.5/sqlglot/optimizer/qualify_tables.py
--rw-r--r--   0 runner    (1001) docker     (121)      654 2022-10-26 22:38:34.000000 sqlglot-9.0.5/sqlglot/optimizer/quote_identities.py
--rw-r--r--   0 runner    (1001) docker     (121)    19111 2022-10-26 22:38:34.000000 sqlglot-9.0.5/sqlglot/optimizer/scope.py
--rw-r--r--   0 runner    (1001) docker     (121)    11831 2022-10-26 22:38:34.000000 sqlglot-9.0.5/sqlglot/optimizer/simplify.py
--rw-r--r--   0 runner    (1001) docker     (121)     7345 2022-10-26 22:38:34.000000 sqlglot-9.0.5/sqlglot/optimizer/unnest_subqueries.py
--rw-r--r--   0 runner    (1001) docker     (121)    85211 2022-10-26 22:38:34.000000 sqlglot-9.0.5/sqlglot/parser.py
--rw-r--r--   0 runner    (1001) docker     (121)     8507 2022-10-26 22:38:34.000000 sqlglot-9.0.5/sqlglot/planner.py
--rw-r--r--   0 runner    (1001) docker     (121)    10366 2022-10-26 22:38:34.000000 sqlglot-9.0.5/sqlglot/schema.py
--rw-r--r--   0 runner    (1001) docker     (121)     1172 2022-10-26 22:38:34.000000 sqlglot-9.0.5/sqlglot/time.py
--rw-r--r--   0 runner    (1001) docker     (121)    28635 2022-10-26 22:38:34.000000 sqlglot-9.0.5/sqlglot/tokens.py
--rw-r--r--   0 runner    (1001) docker     (121)     2395 2022-10-26 22:38:34.000000 sqlglot-9.0.5/sqlglot/transforms.py
--rw-r--r--   0 runner    (1001) docker     (121)      486 2022-10-26 22:38:34.000000 sqlglot-9.0.5/sqlglot/trie.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-10-26 22:38:44.415385 sqlglot-9.0.5/sqlglot.egg-info/
--rw-r--r--   0 runner    (1001) docker     (121)    10762 2022-10-26 22:38:44.000000 sqlglot-9.0.5/sqlglot.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (121)     2251 2022-10-26 22:38:44.000000 sqlglot-9.0.5/sqlglot.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (121)        1 2022-10-26 22:38:44.000000 sqlglot-9.0.5/sqlglot.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (121)        8 2022-10-26 22:38:44.000000 sqlglot-9.0.5/sqlglot.egg-info/top_level.txt
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-10-29 19:31:34.540509 sqlglot-9.0.6/
+-rw-r--r--   0 runner    (1001) docker     (121)     1065 2022-10-29 19:31:26.000000 sqlglot-9.0.6/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (121)    10762 2022-10-29 19:31:34.540509 sqlglot-9.0.6/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (121)    10137 2022-10-29 19:31:26.000000 sqlglot-9.0.6/README.md
+-rw-r--r--   0 runner    (1001) docker     (121)      279 2022-10-29 19:31:34.540509 sqlglot-9.0.6/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (121)      971 2022-10-29 19:31:26.000000 sqlglot-9.0.6/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-10-29 19:31:34.532509 sqlglot-9.0.6/sqlglot/
+-rw-r--r--   0 runner    (1001) docker     (121)     3299 2022-10-29 19:31:26.000000 sqlglot-9.0.6/sqlglot/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1433 2022-10-29 19:31:26.000000 sqlglot-9.0.6/sqlglot/__main__.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-10-29 19:31:34.532509 sqlglot-9.0.6/sqlglot/dataframe/
+-rw-r--r--   0 runner    (1001) docker     (121)        0 2022-10-29 19:31:26.000000 sqlglot-9.0.6/sqlglot/dataframe/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-10-29 19:31:34.536509 sqlglot-9.0.6/sqlglot/dataframe/sql/
+-rw-r--r--   0 runner    (1001) docker     (121)      560 2022-10-29 19:31:26.000000 sqlglot-9.0.6/sqlglot/dataframe/sql/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    12000 2022-10-29 19:31:26.000000 sqlglot-9.0.6/sqlglot/dataframe/sql/column.py
+-rw-r--r--   0 runner    (1001) docker     (121)    33120 2022-10-29 19:31:26.000000 sqlglot-9.0.6/sqlglot/dataframe/sql/dataframe.py
+-rw-r--r--   0 runner    (1001) docker     (121)    40799 2022-10-29 19:31:26.000000 sqlglot-9.0.6/sqlglot/dataframe/sql/functions.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2148 2022-10-29 19:31:26.000000 sqlglot-9.0.6/sqlglot/dataframe/sql/group.py
+-rw-r--r--   0 runner    (1001) docker     (121)     3207 2022-10-29 19:31:26.000000 sqlglot-9.0.6/sqlglot/dataframe/sql/normalize.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1776 2022-10-29 19:31:26.000000 sqlglot-9.0.6/sqlglot/dataframe/sql/operations.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2736 2022-10-29 19:31:26.000000 sqlglot-9.0.6/sqlglot/dataframe/sql/readwriter.py
+-rw-r--r--   0 runner    (1001) docker     (121)     5346 2022-10-29 19:31:26.000000 sqlglot-9.0.6/sqlglot/dataframe/sql/session.py
+-rw-r--r--   0 runner    (1001) docker     (121)      301 2022-10-29 19:31:26.000000 sqlglot-9.0.6/sqlglot/dataframe/sql/transforms.py
+-rw-r--r--   0 runner    (1001) docker     (121)     5156 2022-10-29 19:31:26.000000 sqlglot-9.0.6/sqlglot/dataframe/sql/types.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1160 2022-10-29 19:31:26.000000 sqlglot-9.0.6/sqlglot/dataframe/sql/util.py
+-rw-r--r--   0 runner    (1001) docker     (121)     4460 2022-10-29 19:31:26.000000 sqlglot-9.0.6/sqlglot/dataframe/sql/window.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-10-29 19:31:34.536509 sqlglot-9.0.6/sqlglot/dialects/
+-rw-r--r--   0 runner    (1001) docker     (121)      814 2022-10-29 19:31:26.000000 sqlglot-9.0.6/sqlglot/dialects/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7106 2022-10-29 19:31:26.000000 sqlglot-9.0.6/sqlglot/dialects/bigquery.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2435 2022-10-29 19:31:26.000000 sqlglot-9.0.6/sqlglot/dialects/clickhouse.py
+-rw-r--r--   0 runner    (1001) docker     (121)      716 2022-10-29 19:31:26.000000 sqlglot-9.0.6/sqlglot/dialects/databricks.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11615 2022-10-29 19:31:26.000000 sqlglot-9.0.6/sqlglot/dialects/dialect.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6964 2022-10-29 19:31:26.000000 sqlglot-9.0.6/sqlglot/dialects/duckdb.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11645 2022-10-29 19:31:26.000000 sqlglot-9.0.6/sqlglot/dialects/hive.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7134 2022-10-29 19:31:26.000000 sqlglot-9.0.6/sqlglot/dialects/mysql.py
+-rw-r--r--   0 runner    (1001) docker     (121)     3957 2022-10-29 19:31:26.000000 sqlglot-9.0.6/sqlglot/dialects/oracle.py
+-rw-r--r--   0 runner    (1001) docker     (121)     8452 2022-10-29 19:31:26.000000 sqlglot-9.0.6/sqlglot/dialects/postgres.py
+-rw-r--r--   0 runner    (1001) docker     (121)     9297 2022-10-29 19:31:26.000000 sqlglot-9.0.6/sqlglot/dialects/presto.py
+-rw-r--r--   0 runner    (1001) docker     (121)      986 2022-10-29 19:31:26.000000 sqlglot-9.0.6/sqlglot/dialects/redshift.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7179 2022-10-29 19:31:26.000000 sqlglot-9.0.6/sqlglot/dialects/snowflake.py
+-rw-r--r--   0 runner    (1001) docker     (121)     5008 2022-10-29 19:31:26.000000 sqlglot-9.0.6/sqlglot/dialects/spark.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2132 2022-10-29 19:31:26.000000 sqlglot-9.0.6/sqlglot/dialects/sqlite.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1002 2022-10-29 19:31:26.000000 sqlglot-9.0.6/sqlglot/dialects/starrocks.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1097 2022-10-29 19:31:26.000000 sqlglot-9.0.6/sqlglot/dialects/tableau.py
+-rw-r--r--   0 runner    (1001) docker     (121)      393 2022-10-29 19:31:26.000000 sqlglot-9.0.6/sqlglot/dialects/trino.py
+-rw-r--r--   0 runner    (1001) docker     (121)     9811 2022-10-29 19:31:26.000000 sqlglot-9.0.6/sqlglot/dialects/tsql.py
+-rw-r--r--   0 runner    (1001) docker     (121)    10793 2022-10-29 19:31:26.000000 sqlglot-9.0.6/sqlglot/diff.py
+-rw-r--r--   0 runner    (1001) docker     (121)      799 2022-10-29 19:31:26.000000 sqlglot-9.0.6/sqlglot/errors.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-10-29 19:31:34.536509 sqlglot-9.0.6/sqlglot/executor/
+-rw-r--r--   0 runner    (1001) docker     (121)     1367 2022-10-29 19:31:26.000000 sqlglot-9.0.6/sqlglot/executor/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2157 2022-10-29 19:31:26.000000 sqlglot-9.0.6/sqlglot/executor/context.py
+-rw-r--r--   0 runner    (1001) docker     (121)      652 2022-10-29 19:31:26.000000 sqlglot-9.0.6/sqlglot/executor/env.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11871 2022-10-29 19:31:26.000000 sqlglot-9.0.6/sqlglot/executor/python.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1984 2022-10-29 19:31:26.000000 sqlglot-9.0.6/sqlglot/executor/table.py
+-rw-r--r--   0 runner    (1001) docker     (121)    96633 2022-10-29 19:31:26.000000 sqlglot-9.0.6/sqlglot/expressions.py
+-rw-r--r--   0 runner    (1001) docker     (121)    49331 2022-10-29 19:31:26.000000 sqlglot-9.0.6/sqlglot/generator.py
+-rw-r--r--   0 runner    (1001) docker     (121)     5941 2022-10-29 19:31:26.000000 sqlglot-9.0.6/sqlglot/helper.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-10-29 19:31:34.540509 sqlglot-9.0.6/sqlglot/optimizer/
+-rw-r--r--   0 runner    (1001) docker     (121)       56 2022-10-29 19:31:26.000000 sqlglot-9.0.6/sqlglot/optimizer/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    15489 2022-10-29 19:31:26.000000 sqlglot-9.0.6/sqlglot/optimizer/annotate_types.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1357 2022-10-29 19:31:26.000000 sqlglot-9.0.6/sqlglot/optimizer/eliminate_ctes.py
+-rw-r--r--   0 runner    (1001) docker     (121)     5345 2022-10-29 19:31:26.000000 sqlglot-9.0.6/sqlglot/optimizer/eliminate_joins.py
+-rw-r--r--   0 runner    (1001) docker     (121)     4879 2022-10-29 19:31:26.000000 sqlglot-9.0.6/sqlglot/optimizer/eliminate_subqueries.py
+-rw-r--r--   0 runner    (1001) docker     (121)      385 2022-10-29 19:31:26.000000 sqlglot-9.0.6/sqlglot/optimizer/expand_multi_table_selects.py
+-rw-r--r--   0 runner    (1001) docker     (121)      849 2022-10-29 19:31:26.000000 sqlglot-9.0.6/sqlglot/optimizer/isolate_table_selects.py
+-rw-r--r--   0 runner    (1001) docker     (121)    12382 2022-10-29 19:31:26.000000 sqlglot-9.0.6/sqlglot/optimizer/merge_subqueries.py
+-rw-r--r--   0 runner    (1001) docker     (121)     4110 2022-10-29 19:31:26.000000 sqlglot-9.0.6/sqlglot/optimizer/normalize.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2258 2022-10-29 19:31:26.000000 sqlglot-9.0.6/sqlglot/optimizer/optimize_joins.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2807 2022-10-29 19:31:26.000000 sqlglot-9.0.6/sqlglot/optimizer/optimizer.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6210 2022-10-29 19:31:26.000000 sqlglot-9.0.6/sqlglot/optimizer/pushdown_predicates.py
+-rw-r--r--   0 runner    (1001) docker     (121)     4048 2022-10-29 19:31:26.000000 sqlglot-9.0.6/sqlglot/optimizer/pushdown_projections.py
+-rw-r--r--   0 runner    (1001) docker     (121)    14716 2022-10-29 19:31:26.000000 sqlglot-9.0.6/sqlglot/optimizer/qualify_columns.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1793 2022-10-29 19:31:26.000000 sqlglot-9.0.6/sqlglot/optimizer/qualify_tables.py
+-rw-r--r--   0 runner    (1001) docker     (121)      654 2022-10-29 19:31:26.000000 sqlglot-9.0.6/sqlglot/optimizer/quote_identities.py
+-rw-r--r--   0 runner    (1001) docker     (121)    19111 2022-10-29 19:31:26.000000 sqlglot-9.0.6/sqlglot/optimizer/scope.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11831 2022-10-29 19:31:26.000000 sqlglot-9.0.6/sqlglot/optimizer/simplify.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7345 2022-10-29 19:31:26.000000 sqlglot-9.0.6/sqlglot/optimizer/unnest_subqueries.py
+-rw-r--r--   0 runner    (1001) docker     (121)    86308 2022-10-29 19:31:26.000000 sqlglot-9.0.6/sqlglot/parser.py
+-rw-r--r--   0 runner    (1001) docker     (121)     8507 2022-10-29 19:31:26.000000 sqlglot-9.0.6/sqlglot/planner.py
+-rw-r--r--   0 runner    (1001) docker     (121)    10366 2022-10-29 19:31:26.000000 sqlglot-9.0.6/sqlglot/schema.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1171 2022-10-29 19:31:26.000000 sqlglot-9.0.6/sqlglot/time.py
+-rw-r--r--   0 runner    (1001) docker     (121)    28753 2022-10-29 19:31:26.000000 sqlglot-9.0.6/sqlglot/tokens.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2395 2022-10-29 19:31:26.000000 sqlglot-9.0.6/sqlglot/transforms.py
+-rw-r--r--   0 runner    (1001) docker     (121)      486 2022-10-29 19:31:26.000000 sqlglot-9.0.6/sqlglot/trie.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-10-29 19:31:34.532509 sqlglot-9.0.6/sqlglot.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (121)    10762 2022-10-29 19:31:34.000000 sqlglot-9.0.6/sqlglot.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (121)     2251 2022-10-29 19:31:34.000000 sqlglot-9.0.6/sqlglot.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (121)        1 2022-10-29 19:31:34.000000 sqlglot-9.0.6/sqlglot.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (121)        8 2022-10-29 19:31:34.000000 sqlglot-9.0.6/sqlglot.egg-info/top_level.txt
```

### Comparing `sqlglot-9.0.5/LICENSE` & `sqlglot-9.0.6/LICENSE`

 * *Files identical despite different names*

### Comparing `sqlglot-9.0.5/PKG-INFO` & `sqlglot-9.0.6/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: sqlglot
-Version: 9.0.5
+Version: 9.0.6
 Summary: An easily customizable SQL parser and transpiler
 Home-page: https://github.com/tobymao/sqlglot
 Author: Toby Mao
 Author-email: toby.mao@gmail.com
 License: MIT
 Classifier: Development Status :: 5 - Production/Stable
 Classifier: Intended Audience :: Developers
```

### Comparing `sqlglot-9.0.5/README.md` & `sqlglot-9.0.6/README.md`

 * *Files identical despite different names*

### Comparing `sqlglot-9.0.5/setup.py` & `sqlglot-9.0.6/setup.py`

 * *Files identical despite different names*

### Comparing `sqlglot-9.0.5/sqlglot/__init__.py` & `sqlglot-9.0.6/sqlglot/__init__.py`

 * *Files 3% similar despite different names*

```diff
@@ -22,15 +22,15 @@
 from sqlglot.expressions import table_ as table
 from sqlglot.expressions import union
 from sqlglot.generator import Generator
 from sqlglot.parser import Parser
 from sqlglot.schema import MappingSchema
 from sqlglot.tokens import Tokenizer, TokenType
 
-__version__ = "9.0.5"
+__version__ = "9.0.6"
 
 pretty = False
 
 schema = MappingSchema()
 
 
 def parse(sql, read=None, **opts):
```

### Comparing `sqlglot-9.0.5/sqlglot/__main__.py` & `sqlglot-9.0.6/sqlglot/__main__.py`

 * *Files identical despite different names*

### Comparing `sqlglot-9.0.5/sqlglot/dataframe/sql/__init__.py` & `sqlglot-9.0.6/sqlglot/dataframe/sql/__init__.py`

 * *Files identical despite different names*

### Comparing `sqlglot-9.0.5/sqlglot/dataframe/sql/column.py` & `sqlglot-9.0.6/sqlglot/dataframe/sql/column.py`

 * *Files identical despite different names*

### Comparing `sqlglot-9.0.5/sqlglot/dataframe/sql/dataframe.py` & `sqlglot-9.0.6/sqlglot/dataframe/sql/dataframe.py`

 * *Files identical despite different names*

### Comparing `sqlglot-9.0.5/sqlglot/dataframe/sql/functions.py` & `sqlglot-9.0.6/sqlglot/dataframe/sql/functions.py`

 * *Files identical despite different names*

### Comparing `sqlglot-9.0.5/sqlglot/dataframe/sql/group.py` & `sqlglot-9.0.6/sqlglot/dataframe/sql/group.py`

 * *Files identical despite different names*

### Comparing `sqlglot-9.0.5/sqlglot/dataframe/sql/normalize.py` & `sqlglot-9.0.6/sqlglot/dataframe/sql/normalize.py`

 * *Files identical despite different names*

### Comparing `sqlglot-9.0.5/sqlglot/dataframe/sql/operations.py` & `sqlglot-9.0.6/sqlglot/dataframe/sql/operations.py`

 * *Files identical despite different names*

### Comparing `sqlglot-9.0.5/sqlglot/dataframe/sql/readwriter.py` & `sqlglot-9.0.6/sqlglot/dataframe/sql/readwriter.py`

 * *Files identical despite different names*

### Comparing `sqlglot-9.0.5/sqlglot/dataframe/sql/session.py` & `sqlglot-9.0.6/sqlglot/dataframe/sql/session.py`

 * *Files identical despite different names*

### Comparing `sqlglot-9.0.5/sqlglot/dataframe/sql/types.py` & `sqlglot-9.0.6/sqlglot/dataframe/sql/types.py`

 * *Files identical despite different names*

### Comparing `sqlglot-9.0.5/sqlglot/dataframe/sql/util.py` & `sqlglot-9.0.6/sqlglot/dataframe/sql/util.py`

 * *Files identical despite different names*

### Comparing `sqlglot-9.0.5/sqlglot/dataframe/sql/window.py` & `sqlglot-9.0.6/sqlglot/dataframe/sql/window.py`

 * *Files identical despite different names*

### Comparing `sqlglot-9.0.5/sqlglot/dialects/__init__.py` & `sqlglot-9.0.6/sqlglot/dialects/__init__.py`

 * *Files identical despite different names*

### Comparing `sqlglot-9.0.5/sqlglot/dialects/bigquery.py` & `sqlglot-9.0.6/sqlglot/dialects/bigquery.py`

 * *Files identical despite different names*

### Comparing `sqlglot-9.0.5/sqlglot/dialects/clickhouse.py` & `sqlglot-9.0.6/sqlglot/dialects/clickhouse.py`

 * *Files identical despite different names*

### Comparing `sqlglot-9.0.5/sqlglot/dialects/databricks.py` & `sqlglot-9.0.6/sqlglot/dialects/databricks.py`

 * *Files identical despite different names*

### Comparing `sqlglot-9.0.5/sqlglot/dialects/dialect.py` & `sqlglot-9.0.6/sqlglot/dialects/dialect.py`

 * *Files identical despite different names*

### Comparing `sqlglot-9.0.5/sqlglot/dialects/duckdb.py` & `sqlglot-9.0.6/sqlglot/dialects/duckdb.py`

 * *Files identical despite different names*

### Comparing `sqlglot-9.0.5/sqlglot/dialects/hive.py` & `sqlglot-9.0.6/sqlglot/dialects/hive.py`

 * *Files 1% similar despite different names*

```diff
@@ -107,14 +107,15 @@
     if isinstance(unnest, exp.Unnest):
         alias = unnest.args.get("alias")
         udtf = exp.Posexplode if unnest.args.get("ordinality") else exp.Explode
         return "".join(
             self.sql(
                 exp.Lateral(
                     this=udtf(this=expression),
+                    view=True,
                     alias=exp.TableAlias(this=alias.this, columns=[column]),
                 )
             )
             for expression, column in zip(unnest.expressions, alias.columns if alias else [])
         )
     return self.join_sql(expression)
 
@@ -279,14 +280,15 @@
             exp.TsOrDsAdd: lambda self, e: f"DATE_ADD({self.sql(e, 'this')}, {self.sql(e, 'expression')})",
             exp.TsOrDsToDate: _to_date_sql,
             exp.TryCast: no_trycast_sql,
             exp.UnixToStr: lambda self, e: f"FROM_UNIXTIME({self.format_args(e.this, _time_format(self, e))})",
             exp.UnixToTime: rename_func("FROM_UNIXTIME"),
             exp.UnixToTimeStr: rename_func("FROM_UNIXTIME"),
             exp.PartitionedByProperty: lambda self, e: f"PARTITIONED BY {self.sql(e, 'value')}",
+            exp.NumberToStr: rename_func("FORMAT_NUMBER"),
         }
 
         WITH_PROPERTIES = {exp.AnonymousProperty}
 
         ROOT_PROPERTIES = {
             exp.PartitionedByProperty,
             exp.FileFormatProperty,
```

### Comparing `sqlglot-9.0.5/sqlglot/dialects/mysql.py` & `sqlglot-9.0.6/sqlglot/dialects/mysql.py`

 * *Files identical despite different names*

### Comparing `sqlglot-9.0.5/sqlglot/dialects/oracle.py` & `sqlglot-9.0.6/sqlglot/dialects/oracle.py`

 * *Files identical despite different names*

### Comparing `sqlglot-9.0.5/sqlglot/dialects/postgres.py` & `sqlglot-9.0.6/sqlglot/dialects/postgres.py`

 * *Files identical despite different names*

### Comparing `sqlglot-9.0.5/sqlglot/dialects/presto.py` & `sqlglot-9.0.6/sqlglot/dialects/presto.py`

 * *Files 1% similar despite different names*

```diff
@@ -111,14 +111,15 @@
     null_ordering = "nulls_are_last"
     time_format = "'%Y-%m-%d %H:%i:%S'"
     time_mapping = MySQL.time_mapping
 
     class Tokenizer(Tokenizer):
         KEYWORDS = {
             **Tokenizer.KEYWORDS,
+            "VARBINARY": TokenType.BINARY,
             "ROW": TokenType.STRUCT,
         }
 
     class Parser(Parser):
         FUNCTIONS = {
             **Parser.FUNCTIONS,
             "APPROX_DISTINCT": exp.ApproxDistinct.from_arg_list,
```

### Comparing `sqlglot-9.0.5/sqlglot/dialects/redshift.py` & `sqlglot-9.0.6/sqlglot/dialects/redshift.py`

 * *Files identical despite different names*

### Comparing `sqlglot-9.0.5/sqlglot/dialects/snowflake.py` & `sqlglot-9.0.6/sqlglot/dialects/snowflake.py`

 * *Files 2% similar despite different names*

```diff
@@ -184,14 +184,16 @@
             "TIMESTAMP_NTZ": TokenType.TIMESTAMP,
             "TIMESTAMP_TZ": TokenType.TIMESTAMPTZ,
             "TIMESTAMPNTZ": TokenType.TIMESTAMP,
             "SAMPLE": TokenType.TABLE_SAMPLE,
         }
 
     class Generator(Generator):
+        CREATE_TRANSIENT = True
+
         TRANSFORMS = {
             **Generator.TRANSFORMS,
             exp.ArrayConcat: rename_func("ARRAY_CAT"),
             exp.If: rename_func("IFF"),
             exp.StrToTime: lambda self, e: f"TO_TIMESTAMP({self.sql(e, 'this')}, {self.format_time(e)})",
             exp.UnixToTime: _unix_to_time,
             exp.TimeToUnix: lambda self, e: f"EXTRACT(epoch_second FROM {self.sql(e, 'this')})",
```

### Comparing `sqlglot-9.0.5/sqlglot/dialects/spark.py` & `sqlglot-9.0.6/sqlglot/dialects/spark.py`

 * *Files identical despite different names*

### Comparing `sqlglot-9.0.5/sqlglot/dialects/sqlite.py` & `sqlglot-9.0.6/sqlglot/dialects/sqlite.py`

 * *Files 5% similar despite different names*

```diff
@@ -16,14 +16,15 @@
 class SQLite(Dialect):
     class Tokenizer(Tokenizer):
         IDENTIFIERS = ['"', ("[", "]"), "`"]
         HEX_STRINGS = [("x'", "'"), ("X'", "'"), ("0x", ""), ("0X", "")]
 
         KEYWORDS = {
             **Tokenizer.KEYWORDS,
+            "VARBINARY": TokenType.BINARY,
             "AUTOINCREMENT": TokenType.AUTO_INCREMENT,
         }
 
     class Parser(Parser):
         FUNCTIONS = {
             **Parser.FUNCTIONS,
             "EDITDIST3": exp.Levenshtein.from_arg_list,
```

### Comparing `sqlglot-9.0.5/sqlglot/dialects/starrocks.py` & `sqlglot-9.0.6/sqlglot/dialects/starrocks.py`

 * *Files identical despite different names*

### Comparing `sqlglot-9.0.5/sqlglot/dialects/tableau.py` & `sqlglot-9.0.6/sqlglot/dialects/tableau.py`

 * *Files identical despite different names*

### Comparing `sqlglot-9.0.5/sqlglot/dialects/tsql.py` & `sqlglot-9.0.6/sqlglot/dialects/tsql.py`

 * *Files 13% similar despite different names*

```diff
@@ -1,7 +1,9 @@
+import re
+
 from sqlglot import exp
 from sqlglot.dialects.dialect import Dialect, parse_date_delta, rename_func
 from sqlglot.expressions import DataType
 from sqlglot.generator import Generator
 from sqlglot.helper import list_get
 from sqlglot.parser import Parser
 from sqlglot.time import format_time
@@ -23,14 +25,19 @@
     "wk": "week",
     "day": "day",
     "dd": "day",
     "d": "day",
 }
 
 
+DATE_FMT_RE = re.compile("([dD]{1,2})|([mM]{1,2})|([yY]{1,4})|([hH]{1,2})|([sS]{1,2})")
+# N = Numeric, C=Currency
+TRANSPILE_SAFE_NUMBER_FMT = {"N", "C"}
+
+
 def tsql_format_time_lambda(exp_class, full_format_mapping=None, default=None):
     def _format_time(args):
         return exp_class(
             this=list_get(args, 1),
             format=exp.Literal.string(
                 format_time(
                     list_get(args, 0).name or (TSQL.time_format if default is True else default),
@@ -38,26 +45,48 @@
                 )
             ),
         )
 
     return _format_time
 
 
+def parse_format(args):
+    fmt = list_get(args, 1)
+    number_fmt = fmt.name in TRANSPILE_SAFE_NUMBER_FMT or not DATE_FMT_RE.search(fmt.this)
+    if number_fmt:
+        return exp.NumberToStr(this=list_get(args, 0), format=fmt)
+    return exp.TimeToStr(
+        this=list_get(args, 0),
+        format=exp.Literal.string(
+            format_time(fmt.name, TSQL.format_time_mapping)
+            if len(fmt.name) == 1
+            else format_time(fmt.name, TSQL.time_mapping)
+        ),
+    )
+
+
 def generate_date_delta_with_unit_sql(self, e):
     func = "DATEADD" if isinstance(e, exp.DateAdd) else "DATEDIFF"
     return f"{func}({self.format_args(e.text('unit'), e.expression, e.this)})"
 
 
+def generate_format_sql(self, e):
+    fmt = (
+        e.args["format"]
+        if isinstance(e, exp.NumberToStr)
+        else exp.Literal.string(format_time(e.text("format"), TSQL.inverse_time_mapping))
+    )
+    return f"FORMAT({self.format_args(e.this, fmt)})"
+
+
 class TSQL(Dialect):
     null_ordering = "nulls_are_small"
     time_format = "'yyyy-mm-dd hh:mm:ss'"
 
     time_mapping = {
-        "yyyy": "%Y",
-        "yy": "%y",
         "year": "%Y",
         "qq": "%q",
         "q": "%q",
         "quarter": "%q",
         "dayofyear": "%j",
         "day": "%d",
         "dy": "%d",
@@ -89,14 +118,16 @@
         "M": "%-m",
         "dd": "%d",
         "d": "%-d",
         "HH": "%H",
         "H": "%-H",
         "h": "%-I",
         "S": "%f",
+        "yyyy": "%Y",
+        "yy": "%y",
     }
 
     convert_format_mapping = {
         "0": "%b %d %Y %-I:%M%p",
         "1": "%m/%d/%y",
         "2": "%y.%m.%d",
         "3": "%d/%m/%y",
@@ -131,14 +162,35 @@
         "111": "%Y/%m/%d",
         "112": "%Y%m%d",
         "113": "%d %b %Y %H:%M:%S:%f",
         "114": "%H:%M:%S:%f",
         "120": "%Y-%m-%d %H:%M:%S",
         "121": "%Y-%m-%d %H:%M:%S.%f",
     }
+    # not sure if complete
+    format_time_mapping = {
+        "y": "%B %Y",
+        "d": "%m/%d/%Y",
+        "H": "%-H",
+        "h": "%-I",
+        "s": "%Y-%m-%d %H:%M:%S",
+        "D": "%A,%B,%Y",
+        "f": "%A,%B,%Y %-I:%M %p",
+        "F": "%A,%B,%Y %-I:%M:%S %p",
+        "g": "%m/%d/%Y %-I:%M %p",
+        "G": "%m/%d/%Y %-I:%M:%S %p",
+        "M": "%B %-d",
+        "m": "%B %-d",
+        "O": "%Y-%m-%dT%H:%M:%S",
+        "u": "%Y-%M-%D %H:%M:%S%z",
+        "U": "%A, %B %D, %Y %H:%M:%S%z",
+        "T": "%-I:%M:%S %p",
+        "t": "%-I:%M",
+        "Y": "%a %Y",
+    }
 
     class Tokenizer(Tokenizer):
         IDENTIFIERS = ['"', ("[", "]")]
 
         KEYWORDS = {
             **Tokenizer.KEYWORDS,
             "BIT": TokenType.BOOLEAN,
@@ -154,14 +206,15 @@
             "SMALLMONEY": TokenType.SMALLMONEY,
             "ROWVERSION": TokenType.ROWVERSION,
             "UNIQUEIDENTIFIER": TokenType.UNIQUEIDENTIFIER,
             "XML": TokenType.XML,
             "SQL_VARIANT": TokenType.VARIANT,
             "NVARCHAR(MAX)": TokenType.TEXT,
             "VARCHAR(MAX)": TokenType.TEXT,
+            "TOP": TokenType.TOP,
         }
 
     class Parser(Parser):
         FUNCTIONS = {
             **Parser.FUNCTIONS,
             "CHARINDEX": exp.StrPosition.from_arg_list,
             "ISNULL": exp.Coalesce.from_arg_list,
@@ -170,27 +223,28 @@
             "DATENAME": tsql_format_time_lambda(exp.TimeToStr, full_format_mapping=True),
             "DATEPART": tsql_format_time_lambda(exp.TimeToStr),
             "GETDATE": exp.CurrentDate.from_arg_list,
             "IIF": exp.If.from_arg_list,
             "LEN": exp.Length.from_arg_list,
             "REPLICATE": exp.Repeat.from_arg_list,
             "JSON_VALUE": exp.JSONExtractScalar.from_arg_list,
+            "FORMAT": parse_format,
         }
 
         VAR_LENGTH_DATATYPES = {
             DataType.Type.NVARCHAR,
             DataType.Type.VARCHAR,
             DataType.Type.CHAR,
             DataType.Type.NCHAR,
         }
 
         def _parse_convert(self, strict):
             to = self._parse_types()
             self._match(TokenType.COMMA)
-            this = self._parse_field()
+            this = self._parse_column()
 
             # Retrieve length of datatype and override to default if not specified
             if list_get(to.expressions, 0) is None and to.this in self.VAR_LENGTH_DATATYPES:
                 to = exp.DataType.build(to.this, expressions=[exp.Literal.number(30)], nested=False)
 
             # Check whether a conversion with format is applicable
             if self._match(TokenType.COMMA):
@@ -230,8 +284,10 @@
 
         TRANSFORMS = {
             **Generator.TRANSFORMS,
             exp.DateAdd: generate_date_delta_with_unit_sql,
             exp.DateDiff: generate_date_delta_with_unit_sql,
             exp.CurrentDate: rename_func("GETDATE"),
             exp.If: rename_func("IIF"),
+            exp.NumberToStr: generate_format_sql,
+            exp.TimeToStr: generate_format_sql,
         }
```

### Comparing `sqlglot-9.0.5/sqlglot/diff.py` & `sqlglot-9.0.6/sqlglot/diff.py`

 * *Files identical despite different names*

### Comparing `sqlglot-9.0.5/sqlglot/errors.py` & `sqlglot-9.0.6/sqlglot/errors.py`

 * *Files identical despite different names*

### Comparing `sqlglot-9.0.5/sqlglot/executor/__init__.py` & `sqlglot-9.0.6/sqlglot/executor/__init__.py`

 * *Files identical despite different names*

### Comparing `sqlglot-9.0.5/sqlglot/executor/context.py` & `sqlglot-9.0.6/sqlglot/executor/context.py`

 * *Files identical despite different names*

### Comparing `sqlglot-9.0.5/sqlglot/executor/env.py` & `sqlglot-9.0.6/sqlglot/executor/env.py`

 * *Files identical despite different names*

### Comparing `sqlglot-9.0.5/sqlglot/executor/python.py` & `sqlglot-9.0.6/sqlglot/executor/python.py`

 * *Files identical despite different names*

### Comparing `sqlglot-9.0.5/sqlglot/executor/table.py` & `sqlglot-9.0.6/sqlglot/executor/table.py`

 * *Files identical despite different names*

### Comparing `sqlglot-9.0.5/sqlglot/expressions.py` & `sqlglot-9.0.6/sqlglot/expressions.py`

 * *Files 0% similar despite different names*

```diff
@@ -608,14 +608,15 @@
         "with": False,
         "this": True,
         "kind": True,
         "expression": False,
         "exists": False,
         "properties": False,
         "temporary": False,
+        "transient": False,
         "replace": False,
         "unique": False,
         "materialized": False,
     }
 
 
 class Describe(Expression):
@@ -971,15 +972,15 @@
         if join.kind == "CROSS":
             join.set("kind", None)
 
         return join
 
 
 class Lateral(UDTF):
-    arg_types = {"this": True, "outer": False, "alias": False}
+    arg_types = {"this": True, "view": False, "outer": False, "alias": False}
 
 
 # Clickhouse FROM FINAL modifier
 # https://clickhouse.com/docs/en/sql-reference/statements/select/from/#final-modifier
 class Final(Expression):
     pass
 
@@ -2668,14 +2669,18 @@
     arg_types = {"this": True, "format": True}
 
 
 class StrToUnix(Func):
     arg_types = {"this": True, "format": True}
 
 
+class NumberToStr(Func):
+    arg_types = {"this": True, "format": True}
+
+
 class Struct(Func):
     arg_types = {"expressions": True}
     is_var_len_args = True
 
 
 class StructExtract(Func):
     arg_types = {"this": True, "expression": True}
@@ -3471,15 +3476,15 @@
         return Array(expressions=[convert(v) for v in value])
     if isinstance(value, dict):
         return Map(
             keys=[convert(k) for k in value.keys()],
             values=[convert(v) for v in value.values()],
         )
     if isinstance(value, datetime.datetime):
-        datetime_literal = Literal.string(value.strftime("%Y-%m-%d %H:%M:%S"))
+        datetime_literal = Literal.string(value.strftime("%Y-%m-%d %H:%M:%S.%f%z"))
         return TimeStrToTime(this=datetime_literal)
     if isinstance(value, datetime.date):
         date_literal = Literal.string(value.strftime("%Y-%m-%d"))
         return DateStrToDate(this=date_literal)
     raise ValueError(f"Cannot convert {value}")
```

### Comparing `sqlglot-9.0.5/sqlglot/generator.py` & `sqlglot-9.0.6/sqlglot/generator.py`

 * *Files 0% similar despite different names*

```diff
@@ -61,14 +61,17 @@
         exp.LanguageProperty: lambda self, e: self.naked_property(e),
         exp.LocationProperty: lambda self, e: self.naked_property(e),
         exp.ReturnsProperty: lambda self, e: self.naked_property(e),
         exp.ExecuteAsProperty: lambda self, e: self.naked_property(e),
         exp.VolatilityProperty: lambda self, e: self.sql(e.name),
     }
 
+    # whether 'CREATE ... TRANSIENT ... TABLE' is allowed
+    # can override in dialects
+    CREATE_TRANSIENT = False
     # whether or not null ordering is supported in order by
     NULL_ORDERING_SUPPORTED = True
     # always do union distinct or union all
     EXPLICIT_UNION = False
     # wrap derived values in parens, usually standard but spark doesn't support it
     WRAP_DERIVED_VALUES = True
 
@@ -364,23 +367,22 @@
 
     def create_sql(self, expression):
         this = self.sql(expression, "this")
         kind = self.sql(expression, "kind").upper()
         expression_sql = self.sql(expression, "expression")
         expression_sql = f"AS{self.sep()}{expression_sql}" if expression_sql else ""
         temporary = " TEMPORARY" if expression.args.get("temporary") else ""
+        transient = " TRANSIENT" if self.CREATE_TRANSIENT and expression.args.get("transient") else ""
         replace = " OR REPLACE" if expression.args.get("replace") else ""
         exists_sql = " IF NOT EXISTS" if expression.args.get("exists") else ""
         unique = " UNIQUE" if expression.args.get("unique") else ""
         materialized = " MATERIALIZED" if expression.args.get("materialized") else ""
         properties = self.sql(expression, "properties")
 
-        expression_sql = (
-            f"CREATE{replace}{temporary}{unique}{materialized} {kind}{exists_sql} {this}{properties} {expression_sql}"
-        )
+        expression_sql = f"CREATE{replace}{temporary}{transient}{unique}{materialized} {kind}{exists_sql} {this}{properties} {expression_sql}"
         return self.prepend_ctes(expression, expression_sql)
 
     def describe_sql(self, expression):
         return f"DESCRIBE {self.sql(expression, 'this')}"
 
     def prepend_ctes(self, expression, sql):
         with_ = self.sql(expression, "with")
@@ -712,23 +714,29 @@
     def lambda_sql(self, expression):
         args = self.expressions(expression, flat=True)
         args = f"({args})" if len(args.split(",")) > 1 else args
         return self.no_identify(lambda: f"{args} -> {self.sql(expression, 'this')}")
 
     def lateral_sql(self, expression):
         this = self.sql(expression, "this")
+
         if isinstance(expression.this, exp.Subquery):
-            return f"LATERAL{self.sep()}{this}"
-        op_sql = self.seg(f"LATERAL VIEW{' OUTER' if expression.args.get('outer') else ''}")
+            return f"LATERAL {this}"
+
         alias = expression.args["alias"]
         table = alias.name
         table = f" {table}" if table else table
         columns = self.expressions(alias, key="columns", flat=True)
         columns = f" AS {columns}" if columns else ""
-        return f"{op_sql}{self.sep()}{this}{table}{columns}"
+
+        if expression.args.get("view"):
+            op_sql = self.seg(f"LATERAL VIEW{' OUTER' if expression.args.get('outer') else ''}")
+            return f"{op_sql}{self.sep()}{this}{table}{columns}"
+
+        return f"LATERAL {this}{table}{columns}"
 
     def limit_sql(self, expression):
         this = self.sql(expression, "this")
         return f"{this}{self.seg('LIMIT')} {self.sql(expression, 'expression')}"
 
     def offset_sql(self, expression):
         this = self.sql(expression, "this")
```

### Comparing `sqlglot-9.0.5/sqlglot/helper.py` & `sqlglot-9.0.6/sqlglot/helper.py`

 * *Files identical despite different names*

### Comparing `sqlglot-9.0.5/sqlglot/optimizer/annotate_types.py` & `sqlglot-9.0.6/sqlglot/optimizer/annotate_types.py`

 * *Files identical despite different names*

### Comparing `sqlglot-9.0.5/sqlglot/optimizer/eliminate_ctes.py` & `sqlglot-9.0.6/sqlglot/optimizer/eliminate_ctes.py`

 * *Files identical despite different names*

### Comparing `sqlglot-9.0.5/sqlglot/optimizer/eliminate_joins.py` & `sqlglot-9.0.6/sqlglot/optimizer/eliminate_joins.py`

 * *Files identical despite different names*

### Comparing `sqlglot-9.0.5/sqlglot/optimizer/eliminate_subqueries.py` & `sqlglot-9.0.6/sqlglot/optimizer/eliminate_subqueries.py`

 * *Files identical despite different names*

### Comparing `sqlglot-9.0.5/sqlglot/optimizer/isolate_table_selects.py` & `sqlglot-9.0.6/sqlglot/optimizer/isolate_table_selects.py`

 * *Files identical despite different names*

### Comparing `sqlglot-9.0.5/sqlglot/optimizer/merge_subqueries.py` & `sqlglot-9.0.6/sqlglot/optimizer/merge_subqueries.py`

 * *Files identical despite different names*

### Comparing `sqlglot-9.0.5/sqlglot/optimizer/normalize.py` & `sqlglot-9.0.6/sqlglot/optimizer/normalize.py`

 * *Files identical despite different names*

### Comparing `sqlglot-9.0.5/sqlglot/optimizer/optimize_joins.py` & `sqlglot-9.0.6/sqlglot/optimizer/optimize_joins.py`

 * *Files identical despite different names*

### Comparing `sqlglot-9.0.5/sqlglot/optimizer/optimizer.py` & `sqlglot-9.0.6/sqlglot/optimizer/optimizer.py`

 * *Files identical despite different names*

### Comparing `sqlglot-9.0.5/sqlglot/optimizer/pushdown_predicates.py` & `sqlglot-9.0.6/sqlglot/optimizer/pushdown_predicates.py`

 * *Files identical despite different names*

### Comparing `sqlglot-9.0.5/sqlglot/optimizer/pushdown_projections.py` & `sqlglot-9.0.6/sqlglot/optimizer/pushdown_projections.py`

 * *Files identical despite different names*

### Comparing `sqlglot-9.0.5/sqlglot/optimizer/qualify_columns.py` & `sqlglot-9.0.6/sqlglot/optimizer/qualify_columns.py`

 * *Files identical despite different names*

### Comparing `sqlglot-9.0.5/sqlglot/optimizer/qualify_tables.py` & `sqlglot-9.0.6/sqlglot/optimizer/qualify_tables.py`

 * *Files identical despite different names*

### Comparing `sqlglot-9.0.5/sqlglot/optimizer/quote_identities.py` & `sqlglot-9.0.6/sqlglot/optimizer/quote_identities.py`

 * *Files identical despite different names*

### Comparing `sqlglot-9.0.5/sqlglot/optimizer/scope.py` & `sqlglot-9.0.6/sqlglot/optimizer/scope.py`

 * *Files identical despite different names*

### Comparing `sqlglot-9.0.5/sqlglot/optimizer/simplify.py` & `sqlglot-9.0.6/sqlglot/optimizer/simplify.py`

 * *Files identical despite different names*

### Comparing `sqlglot-9.0.5/sqlglot/optimizer/unnest_subqueries.py` & `sqlglot-9.0.6/sqlglot/optimizer/unnest_subqueries.py`

 * *Files identical despite different names*

### Comparing `sqlglot-9.0.5/sqlglot/parser.py` & `sqlglot-9.0.6/sqlglot/parser.py`

 * *Files 1% similar despite different names*

```diff
@@ -127,14 +127,15 @@
     RESERVED_KEYWORDS = {*Tokenizer.SINGLE_TOKENS.values(), TokenType.SELECT}
 
     ID_VAR_TOKENS = {
         TokenType.VAR,
         TokenType.ALTER,
         TokenType.ALWAYS,
         TokenType.ANTI,
+        TokenType.APPLY,
         TokenType.BEGIN,
         TokenType.BOTH,
         TokenType.BUCKET,
         TokenType.CACHE,
         TokenType.CALL,
         TokenType.COLLATE,
         TokenType.COMMIT,
@@ -186,29 +187,30 @@
         TokenType.SET,
         TokenType.SHOW,
         TokenType.STABLE,
         TokenType.STORED,
         TokenType.TABLE,
         TokenType.TABLE_FORMAT,
         TokenType.TEMPORARY,
+        TokenType.TRANSIENT,
         TokenType.TOP,
         TokenType.TRAILING,
         TokenType.TRUNCATE,
         TokenType.TRUE,
         TokenType.UNBOUNDED,
         TokenType.UNIQUE,
         TokenType.UNPIVOT,
         TokenType.PROPERTIES,
         TokenType.PROCEDURE,
         TokenType.VOLATILE,
         *SUBQUERY_PREDICATES,
         *TYPE_TOKENS,
     }
 
-    TABLE_ALIAS_TOKENS = ID_VAR_TOKENS - {TokenType.NATURAL}
+    TABLE_ALIAS_TOKENS = ID_VAR_TOKENS - {TokenType.NATURAL, TokenType.APPLY}
 
     TRIM_TYPES = {TokenType.LEADING, TokenType.TRAILING, TokenType.BOTH}
 
     FUNC_TOKENS = {
         TokenType.CURRENT_DATE,
         TokenType.CURRENT_DATETIME,
         TokenType.CURRENT_TIMESTAMP,
@@ -681,14 +683,15 @@
 
     def _parse_exists(self, not_=False):
         return self._match(TokenType.IF) and (not not_ or self._match(TokenType.NOT)) and self._match(TokenType.EXISTS)
 
     def _parse_create(self):
         replace = self._match(TokenType.OR) and self._match(TokenType.REPLACE)
         temporary = self._match(TokenType.TEMPORARY)
+        transient = self._match(TokenType.TRANSIENT)
         unique = self._match(TokenType.UNIQUE)
         materialized = self._match(TokenType.MATERIALIZED)
 
         if self._match_pair(TokenType.TABLE, TokenType.FUNCTION, advance=False):
             self._match(TokenType.TABLE)
 
         create_token = self._match_set(self.CREATABLES) and self._prev
@@ -719,14 +722,15 @@
             exp.Create,
             this=this,
             kind=create_token.text,
             expression=expression,
             exists=exists,
             properties=properties,
             temporary=temporary,
+            transient=transient,
             replace=replace,
             unique=unique,
             materialized=materialized,
         )
 
     def _parse_property(self):
         if self._match_set(self.PROPERTY_PARSERS):
@@ -1163,36 +1167,61 @@
     def _parse_from(self):
         if not self._match(TokenType.FROM):
             return None
 
         return self.expression(exp.From, expressions=self._parse_csv(self._parse_table))
 
     def _parse_lateral(self):
-        if not self._match(TokenType.LATERAL):
+        outer_apply = self._match_pair(TokenType.OUTER, TokenType.APPLY)
+        cross_apply = self._match_pair(TokenType.CROSS, TokenType.APPLY)
+
+        if outer_apply or cross_apply:
+            this = self._parse_select(table=True)
+            view = None
+            outer = not cross_apply
+        elif self._match(TokenType.LATERAL):
+            this = self._parse_select(table=True)
+            view = self._match(TokenType.VIEW)
+            outer = self._match(TokenType.OUTER)
+        else:
             return None
 
-        subquery = self._parse_select(table=True)
+        if not this:
+            this = self._parse_function()
 
-        if subquery:
-            return self.expression(exp.Lateral, this=subquery)
+        table_alias = self._parse_id_var(any_token=False)
 
-        self._match(TokenType.VIEW)
-        outer = self._match(TokenType.OUTER)
+        columns = None
+        if self._match(TokenType.ALIAS):
+            columns = self._parse_csv(self._parse_id_var)
+        elif self._match(TokenType.L_PAREN):
+            columns = self._parse_csv(self._parse_id_var)
+            self._match(TokenType.R_PAREN)
 
-        return self.expression(
+        expression = self.expression(
             exp.Lateral,
-            this=self._parse_function(),
+            this=this,
+            view=view,
             outer=outer,
             alias=self.expression(
                 exp.TableAlias,
-                this=self._parse_id_var(any_token=False),
-                columns=(self._parse_csv(self._parse_id_var) if self._match(TokenType.ALIAS) else None),
+                this=table_alias,
+                columns=columns,
             ),
         )
 
+        if outer_apply or cross_apply:
+            return self.expression(
+                exp.Join,
+                this=expression,
+                side=None if cross_apply else "LEFT",
+            )
+
+        return expression
+
     def _parse_join_side_and_kind(self):
         return (
             self._match(TokenType.NATURAL) and self._prev,
             self._match_set(self.JOIN_SIDES) and self._prev,
             self._match_set(self.JOIN_KINDS) and self._prev,
         )
 
@@ -1498,15 +1527,19 @@
         ):
             nulls_first = True
 
         return self.expression(exp.Ordered, this=this, desc=desc, nulls_first=nulls_first)
 
     def _parse_limit(self, this=None, top=False):
         if self._match(TokenType.TOP if top else TokenType.LIMIT):
-            return self.expression(exp.Limit, this=this, expression=self._parse_number())
+            limit_paren = self._match(TokenType.L_PAREN)
+            limit_exp = self.expression(exp.Limit, this=this, expression=self._parse_number())
+            if limit_paren:
+                self._match(TokenType.R_PAREN)
+            return limit_exp
         if self._match(TokenType.FETCH):
             direction = self._match_set((TokenType.FIRST, TokenType.NEXT))
             direction = self._prev.text if direction else "FIRST"
             count = self._parse_number()
             self._match_set((TokenType.ROW, TokenType.ROWS))
             self._match(TokenType.ONLY)
             return self.expression(exp.Fetch, direction=direction, count=count)
@@ -2132,15 +2165,15 @@
         elif to.this == exp.DataType.Type.CHAR:
             if self._match(TokenType.CHARACTER_SET):
                 to = self.expression(exp.CharacterSet, this=self._parse_var_or_string())
 
         return self.expression(exp.Cast if strict else exp.TryCast, this=this, to=to)
 
     def _parse_convert(self, strict):
-        this = self._parse_field()
+        this = self._parse_column()
         if self._match(TokenType.USING):
             to = self.expression(exp.CharacterSet, this=self._parse_var())
         elif self._match(TokenType.COMMA):
             to = self._parse_types()
         else:
             to = None
         return self.expression(exp.Cast if strict else exp.TryCast, this=this, to=to)
```

### Comparing `sqlglot-9.0.5/sqlglot/planner.py` & `sqlglot-9.0.6/sqlglot/planner.py`

 * *Files identical despite different names*

### Comparing `sqlglot-9.0.5/sqlglot/schema.py` & `sqlglot-9.0.6/sqlglot/schema.py`

 * *Files identical despite different names*

### Comparing `sqlglot-9.0.5/sqlglot/time.py` & `sqlglot-9.0.6/sqlglot/time.py`

 * *Files 0% similar despite different names*

```diff
@@ -39,9 +39,8 @@
         elif result == 2:
             sym = chars
 
         end += 1
 
         if result and end > size:
             chunks.append(chars)
-
     return "".join(mapping.get(chars, chars) for chars in chunks)
```

### Comparing `sqlglot-9.0.5/sqlglot/tokens.py` & `sqlglot-9.0.6/sqlglot/tokens.py`

 * *Files 0% similar despite different names*

```diff
@@ -103,14 +103,15 @@
     ALIAS = auto()
     ALWAYS = auto()
     ALL = auto()
     ALTER = auto()
     ANALYZE = auto()
     ANTI = auto()
     ANY = auto()
+    APPLY = auto()
     ARRAY = auto()
     ASC = auto()
     AT_TIME_ZONE = auto()
     AUTO_INCREMENT = auto()
     BEGIN = auto()
     BETWEEN = auto()
     BOTH = auto()
@@ -252,14 +253,15 @@
     SORT_BY = auto()
     STABLE = auto()
     STORED = auto()
     STRUCT = auto()
     TABLE_FORMAT = auto()
     TABLE_SAMPLE = auto()
     TEMPORARY = auto()
+    TRANSIENT = auto()
     TOP = auto()
     THEN = auto()
     TRUE = auto()
     TRAILING = auto()
     TRUNCATE = auto()
     UNBOUNDED = auto()
     UNCACHE = auto()
@@ -556,14 +558,15 @@
         "STORED": TokenType.STORED,
         "TABLE": TokenType.TABLE,
         "TABLE_FORMAT": TokenType.TABLE_FORMAT,
         "TBLPROPERTIES": TokenType.PROPERTIES,
         "TABLESAMPLE": TokenType.TABLE_SAMPLE,
         "TEMP": TokenType.TEMPORARY,
         "TEMPORARY": TokenType.TEMPORARY,
+        "TRANSIENT": TokenType.TRANSIENT,
         "THEN": TokenType.THEN,
         "TRUE": TokenType.TRUE,
         "TRAILING": TokenType.TRAILING,
         "TRUNCATE": TokenType.TRUNCATE,
         "UNBOUNDED": TokenType.UNBOUNDED,
         "UNION": TokenType.UNION,
         "UNPIVOT": TokenType.UNPIVOT,
@@ -578,14 +581,15 @@
         "WHEN": TokenType.WHEN,
         "WHERE": TokenType.WHERE,
         "WITH": TokenType.WITH,
         "WITH TIME ZONE": TokenType.WITH_TIME_ZONE,
         "WITH LOCAL TIME ZONE": TokenType.WITH_LOCAL_TIME_ZONE,
         "WITHIN GROUP": TokenType.WITHIN_GROUP,
         "WITHOUT TIME ZONE": TokenType.WITHOUT_TIME_ZONE,
+        "APPLY": TokenType.APPLY,
         "ARRAY": TokenType.ARRAY,
         "BOOL": TokenType.BOOLEAN,
         "BOOLEAN": TokenType.BOOLEAN,
         "BYTE": TokenType.TINYINT,
         "TINYINT": TokenType.TINYINT,
         "SHORT": TokenType.SMALLINT,
         "SMALLINT": TokenType.SMALLINT,
```

### Comparing `sqlglot-9.0.5/sqlglot/transforms.py` & `sqlglot-9.0.6/sqlglot/transforms.py`

 * *Files identical despite different names*

### Comparing `sqlglot-9.0.5/sqlglot.egg-info/PKG-INFO` & `sqlglot-9.0.6/sqlglot.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: sqlglot
-Version: 9.0.5
+Version: 9.0.6
 Summary: An easily customizable SQL parser and transpiler
 Home-page: https://github.com/tobymao/sqlglot
 Author: Toby Mao
 Author-email: toby.mao@gmail.com
 License: MIT
 Classifier: Development Status :: 5 - Production/Stable
 Classifier: Intended Audience :: Developers
```

### Comparing `sqlglot-9.0.5/sqlglot.egg-info/SOURCES.txt` & `sqlglot-9.0.6/sqlglot.egg-info/SOURCES.txt`

 * *Files identical despite different names*

