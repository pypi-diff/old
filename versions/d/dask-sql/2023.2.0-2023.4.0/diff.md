# Comparing `tmp/dask_sql-2023.2.0.tar.gz` & `tmp/dask_sql-2023.4.0.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "dask_sql-2023.2.0.tar", last modified: Mon Feb  6 21:36:49 2023, max compression
+gzip compressed data, was "dask_sql-2023.4.0.tar", last modified: Thu Apr  6 14:40:06 2023, max compression
```

## Comparing `dask_sql-2023.2.0.tar` & `dask_sql-2023.4.0.tar`

### file list

```diff
@@ -1,179 +1,181 @@
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-06 21:36:49.550876 dask_sql-2023.2.0/
--rw-r--r--   0 runner    (1001) docker     (123)     1067 2023-02-06 19:23:05.000000 dask_sql-2023.2.0/LICENSE.txt
--rw-r--r--   0 runner    (1001) docker     (123)      119 2023-02-06 19:23:05.000000 dask_sql-2023.2.0/MANIFEST.in
--rw-r--r--   0 runner    (1001) docker     (123)     8519 2023-02-06 21:36:49.550876 dask_sql-2023.2.0/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)     8164 2023-02-06 19:23:05.000000 dask_sql-2023.2.0/README.md
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-06 21:36:49.530875 dask_sql-2023.2.0/dask_planner/
--rw-r--r--   0 runner    (1001) docker     (123)     2210 2023-02-06 19:23:05.000000 dask_sql-2023.2.0/dask_planner/.classpath
--rw-r--r--   0 runner    (1001) docker     (123)      686 2023-02-06 19:23:05.000000 dask_sql-2023.2.0/dask_planner/.gitignore
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-06 21:36:49.530875 dask_sql-2023.2.0/dask_planner/.settings/
--rw-r--r--   0 runner    (1001) docker     (123)      173 2023-02-06 19:23:05.000000 dask_sql-2023.2.0/dask_planner/.settings/org.eclipse.core.resources.prefs
--rw-r--r--   0 runner    (1001) docker     (123)       67 2023-02-06 19:23:05.000000 dask_sql-2023.2.0/dask_planner/.settings/org.eclipse.jdt.apt.core.prefs
--rw-r--r--   0 runner    (1001) docker     (123)      479 2023-02-06 19:23:05.000000 dask_sql-2023.2.0/dask_planner/.settings/org.eclipse.jdt.core.prefs
--rw-r--r--   0 runner    (1001) docker     (123)       86 2023-02-06 19:23:05.000000 dask_sql-2023.2.0/dask_planner/.settings/org.eclipse.m2e.core.prefs
--rw-r--r--   0 runner    (1001) docker     (123)    40851 2023-02-06 19:23:05.000000 dask_sql-2023.2.0/dask_planner/Cargo.lock
--rw-r--r--   0 runner    (1001) docker     (123)      847 2023-02-06 19:23:05.000000 dask_sql-2023.2.0/dask_planner/Cargo.toml
--rw-r--r--   0 runner    (1001) docker     (123)       43 2023-02-06 19:23:05.000000 dask_sql-2023.2.0/dask_planner/MANIFEST.in
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-06 19:23:05.000000 dask_sql-2023.2.0/dask_planner/README.md
--rw-r--r--   0 runner    (1001) docker     (123)      319 2023-02-06 19:23:05.000000 dask_sql-2023.2.0/dask_planner/pyproject.toml
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-06 21:36:49.530875 dask_sql-2023.2.0/dask_planner/src/
--rw-r--r--   0 runner    (1001) docker     (123)     8931 2023-02-06 19:23:05.000000 dask_sql-2023.2.0/dask_planner/src/dialect.rs
--rw-r--r--   0 runner    (1001) docker     (123)     1417 2023-02-06 19:23:05.000000 dask_sql-2023.2.0/dask_planner/src/error.rs
--rw-r--r--   0 runner    (1001) docker     (123)    31948 2023-02-06 19:23:05.000000 dask_sql-2023.2.0/dask_planner/src/expression.rs
--rw-r--r--   0 runner    (1001) docker     (123)     1277 2023-02-06 19:23:05.000000 dask_sql-2023.2.0/dask_planner/src/lib.rs
--rw-r--r--   0 runner    (1001) docker     (123)    53605 2023-02-06 19:23:05.000000 dask_sql-2023.2.0/dask_planner/src/parser.rs
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-06 21:36:49.534875 dask_sql-2023.2.0/dask_planner/src/sql/
--rw-r--r--   0 runner    (1001) docker     (123)      709 2023-02-06 19:23:05.000000 dask_sql-2023.2.0/dask_planner/src/sql/column.rs
--rw-r--r--   0 runner    (1001) docker     (123)      871 2023-02-06 19:23:05.000000 dask_sql-2023.2.0/dask_planner/src/sql/exceptions.rs
--rw-r--r--   0 runner    (1001) docker     (123)     1059 2023-02-06 19:23:05.000000 dask_sql-2023.2.0/dask_planner/src/sql/function.rs
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-06 21:36:49.538875 dask_sql-2023.2.0/dask_planner/src/sql/logical/
--rw-r--r--   0 runner    (1001) docker     (123)     3979 2023-02-06 19:23:05.000000 dask_sql-2023.2.0/dask_planner/src/sql/logical/aggregate.rs
--rw-r--r--   0 runner    (1001) docker     (123)     2946 2023-02-06 19:23:05.000000 dask_sql-2023.2.0/dask_planner/src/sql/logical/alter_schema.rs
--rw-r--r--   0 runner    (1001) docker     (123)     3317 2023-02-06 19:23:05.000000 dask_sql-2023.2.0/dask_planner/src/sql/logical/alter_table.rs
--rw-r--r--   0 runner    (1001) docker     (123)     3116 2023-02-06 19:23:05.000000 dask_sql-2023.2.0/dask_planner/src/sql/logical/analyze_table.rs
--rw-r--r--   0 runner    (1001) docker     (123)     3160 2023-02-06 19:23:05.000000 dask_sql-2023.2.0/dask_planner/src/sql/logical/create_catalog_schema.rs
--rw-r--r--   0 runner    (1001) docker     (123)     4099 2023-02-06 19:23:05.000000 dask_sql-2023.2.0/dask_planner/src/sql/logical/create_experiment.rs
--rw-r--r--   0 runner    (1001) docker     (123)     3420 2023-02-06 19:23:05.000000 dask_sql-2023.2.0/dask_planner/src/sql/logical/create_memory_table.rs
--rw-r--r--   0 runner    (1001) docker     (123)     3892 2023-02-06 19:23:05.000000 dask_sql-2023.2.0/dask_planner/src/sql/logical/create_model.rs
--rw-r--r--   0 runner    (1001) docker     (123)     3480 2023-02-06 19:23:05.000000 dask_sql-2023.2.0/dask_planner/src/sql/logical/create_table.rs
--rw-r--r--   0 runner    (1001) docker     (123)     2822 2023-02-06 19:23:05.000000 dask_sql-2023.2.0/dask_planner/src/sql/logical/describe_model.rs
--rw-r--r--   0 runner    (1001) docker     (123)     2870 2023-02-06 19:23:05.000000 dask_sql-2023.2.0/dask_planner/src/sql/logical/drop_model.rs
--rw-r--r--   0 runner    (1001) docker     (123)     2589 2023-02-06 19:23:05.000000 dask_sql-2023.2.0/dask_planner/src/sql/logical/drop_schema.rs
--rw-r--r--   0 runner    (1001) docker     (123)      891 2023-02-06 19:23:05.000000 dask_sql-2023.2.0/dask_planner/src/sql/logical/drop_table.rs
--rw-r--r--   0 runner    (1001) docker     (123)     1154 2023-02-06 19:23:05.000000 dask_sql-2023.2.0/dask_planner/src/sql/logical/empty_relation.rs
--rw-r--r--   0 runner    (1001) docker     (123)      963 2023-02-06 19:23:05.000000 dask_sql-2023.2.0/dask_planner/src/sql/logical/explain.rs
--rw-r--r--   0 runner    (1001) docker     (123)     3087 2023-02-06 19:23:05.000000 dask_sql-2023.2.0/dask_planner/src/sql/logical/export_model.rs
--rw-r--r--   0 runner    (1001) docker     (123)      936 2023-02-06 19:23:05.000000 dask_sql-2023.2.0/dask_planner/src/sql/logical/filter.rs
--rw-r--r--   0 runner    (1001) docker     (123)     3223 2023-02-06 19:23:05.000000 dask_sql-2023.2.0/dask_planner/src/sql/logical/join.rs
--rw-r--r--   0 runner    (1001) docker     (123)     1258 2023-02-06 19:23:05.000000 dask_sql-2023.2.0/dask_planner/src/sql/logical/limit.rs
--rw-r--r--   0 runner    (1001) docker     (123)     2961 2023-02-06 19:23:05.000000 dask_sql-2023.2.0/dask_planner/src/sql/logical/predict_model.rs
--rw-r--r--   0 runner    (1001) docker     (123)     1889 2023-02-06 19:23:05.000000 dask_sql-2023.2.0/dask_planner/src/sql/logical/projection.rs
--rw-r--r--   0 runner    (1001) docker     (123)     1978 2023-02-06 19:23:05.000000 dask_sql-2023.2.0/dask_planner/src/sql/logical/repartition_by.rs
--rw-r--r--   0 runner    (1001) docker     (123)     2814 2023-02-06 19:23:05.000000 dask_sql-2023.2.0/dask_planner/src/sql/logical/show_columns.rs
--rw-r--r--   0 runner    (1001) docker     (123)     2338 2023-02-06 19:23:05.000000 dask_sql-2023.2.0/dask_planner/src/sql/logical/show_models.rs
--rw-r--r--   0 runner    (1001) docker     (123)     2513 2023-02-06 19:23:05.000000 dask_sql-2023.2.0/dask_planner/src/sql/logical/show_schema.rs
--rw-r--r--   0 runner    (1001) docker     (123)     2516 2023-02-06 19:23:05.000000 dask_sql-2023.2.0/dask_planner/src/sql/logical/show_tables.rs
--rw-r--r--   0 runner    (1001) docker     (123)      950 2023-02-06 19:23:05.000000 dask_sql-2023.2.0/dask_planner/src/sql/logical/sort.rs
--rw-r--r--   0 runner    (1001) docker     (123)      844 2023-02-06 19:23:05.000000 dask_sql-2023.2.0/dask_planner/src/sql/logical/subquery_alias.rs
--rw-r--r--   0 runner    (1001) docker     (123)     2198 2023-02-06 19:23:05.000000 dask_sql-2023.2.0/dask_planner/src/sql/logical/table_scan.rs
--rw-r--r--   0 runner    (1001) docker     (123)     2381 2023-02-06 19:23:05.000000 dask_sql-2023.2.0/dask_planner/src/sql/logical/use_schema.rs
--rw-r--r--   0 runner    (1001) docker     (123)     6073 2023-02-06 19:23:05.000000 dask_sql-2023.2.0/dask_planner/src/sql/logical/window.rs
--rw-r--r--   0 runner    (1001) docker     (123)    16913 2023-02-06 19:23:05.000000 dask_sql-2023.2.0/dask_planner/src/sql/logical.rs
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-06 21:36:49.538875 dask_sql-2023.2.0/dask_planner/src/sql/optimizer/
--rw-r--r--   0 runner    (1001) docker     (123)    22202 2023-02-06 19:23:05.000000 dask_sql-2023.2.0/dask_planner/src/sql/optimizer/filter_columns_post_join.rs
--rw-r--r--   0 runner    (1001) docker     (123)     8017 2023-02-06 19:23:05.000000 dask_sql-2023.2.0/dask_planner/src/sql/optimizer.rs
--rw-r--r--   0 runner    (1001) docker     (123)      736 2023-02-06 19:23:05.000000 dask_sql-2023.2.0/dask_planner/src/sql/parser_utils.rs
--rw-r--r--   0 runner    (1001) docker     (123)     1505 2023-02-06 19:23:05.000000 dask_sql-2023.2.0/dask_planner/src/sql/schema.rs
--rw-r--r--   0 runner    (1001) docker     (123)      591 2023-02-06 19:23:05.000000 dask_sql-2023.2.0/dask_planner/src/sql/statement.rs
--rw-r--r--   0 runner    (1001) docker     (123)     8686 2023-02-06 19:23:05.000000 dask_sql-2023.2.0/dask_planner/src/sql/table.rs
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-06 21:36:49.538875 dask_sql-2023.2.0/dask_planner/src/sql/types/
--rw-r--r--   0 runner    (1001) docker     (123)     3673 2023-02-06 19:23:05.000000 dask_sql-2023.2.0/dask_planner/src/sql/types/rel_data_type.rs
--rw-r--r--   0 runner    (1001) docker     (123)     3671 2023-02-06 19:23:05.000000 dask_sql-2023.2.0/dask_planner/src/sql/types/rel_data_type_field.rs
--rw-r--r--   0 runner    (1001) docker     (123)    15080 2023-02-06 19:23:05.000000 dask_sql-2023.2.0/dask_planner/src/sql/types.rs
--rw-r--r--   0 runner    (1001) docker     (123)    29974 2023-02-06 19:23:05.000000 dask_sql-2023.2.0/dask_planner/src/sql.rs
--rw-r--r--   0 runner    (1001) docker     (123)      362 2023-02-06 19:23:05.000000 dask_sql-2023.2.0/dask_planner/update-dependencies.sh
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-06 21:36:49.550876 dask_sql-2023.2.0/dask_sql/
--rw-r--r--   0 runner    (1001) docker     (123)      277 2023-02-06 19:23:05.000000 dask_sql-2023.2.0/dask_sql/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      733 2023-02-06 19:23:05.000000 dask_sql-2023.2.0/dask_sql/_compat.py
--rw-r--r--   0 runner    (1001) docker     (123)      500 2023-02-06 21:36:49.550876 dask_sql-2023.2.0/dask_sql/_version.py
--rw-r--r--   0 runner    (1001) docker     (123)     9016 2023-02-06 19:23:05.000000 dask_sql-2023.2.0/dask_sql/cmd.py
--rw-r--r--   0 runner    (1001) docker     (123)      235 2023-02-06 19:23:05.000000 dask_sql-2023.2.0/dask_sql/config.py
--rw-r--r--   0 runner    (1001) docker     (123)    36317 2023-02-06 19:23:05.000000 dask_sql-2023.2.0/dask_sql/context.py
--rw-r--r--   0 runner    (1001) docker     (123)     9151 2023-02-06 19:23:05.000000 dask_sql-2023.2.0/dask_sql/datacontainer.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-06 21:36:49.542875 dask_sql-2023.2.0/dask_sql/input_utils/
--rw-r--r--   0 runner    (1001) docker     (123)      493 2023-02-06 19:23:05.000000 dask_sql-2023.2.0/dask_sql/input_utils/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      312 2023-02-06 19:23:05.000000 dask_sql-2023.2.0/dask_sql/input_utils/base.py
--rw-r--r--   0 runner    (1001) docker     (123)     2671 2023-02-06 19:23:05.000000 dask_sql-2023.2.0/dask_sql/input_utils/convert.py
--rw-r--r--   0 runner    (1001) docker     (123)      982 2023-02-06 19:23:05.000000 dask_sql-2023.2.0/dask_sql/input_utils/dask.py
--rw-r--r--   0 runner    (1001) docker     (123)    11719 2023-02-06 19:23:05.000000 dask_sql-2023.2.0/dask_sql/input_utils/hive.py
--rw-r--r--   0 runner    (1001) docker     (123)     1080 2023-02-06 19:23:05.000000 dask_sql-2023.2.0/dask_sql/input_utils/intake.py
--rw-r--r--   0 runner    (1001) docker     (123)     1773 2023-02-06 19:23:05.000000 dask_sql-2023.2.0/dask_sql/input_utils/location.py
--rw-r--r--   0 runner    (1001) docker     (123)     1146 2023-02-06 19:23:05.000000 dask_sql-2023.2.0/dask_sql/input_utils/pandaslike.py
--rw-r--r--   0 runner    (1001) docker     (123)     1222 2023-02-06 19:23:05.000000 dask_sql-2023.2.0/dask_sql/input_utils/sqlalchemy.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-06 21:36:49.542875 dask_sql-2023.2.0/dask_sql/integrations/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-06 19:23:05.000000 dask_sql-2023.2.0/dask_sql/integrations/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     5030 2023-02-06 19:23:05.000000 dask_sql-2023.2.0/dask_sql/integrations/fugue.py
--rw-r--r--   0 runner    (1001) docker     (123)     4589 2023-02-06 19:23:05.000000 dask_sql-2023.2.0/dask_sql/integrations/ipython.py
--rw-r--r--   0 runner    (1001) docker     (123)    10547 2023-02-06 19:23:05.000000 dask_sql-2023.2.0/dask_sql/mappings.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-06 21:36:49.542875 dask_sql-2023.2.0/dask_sql/physical/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-06 19:23:05.000000 dask_sql-2023.2.0/dask_sql/physical/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-06 21:36:49.542875 dask_sql-2023.2.0/dask_sql/physical/rel/
--rw-r--r--   0 runner    (1001) docker     (123)       34 2023-02-06 19:23:05.000000 dask_sql-2023.2.0/dask_sql/physical/rel/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     3858 2023-02-06 19:23:05.000000 dask_sql-2023.2.0/dask_sql/physical/rel/base.py
--rw-r--r--   0 runner    (1001) docker     (123)     2264 2023-02-06 19:23:05.000000 dask_sql-2023.2.0/dask_sql/physical/rel/convert.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-06 21:36:49.542875 dask_sql-2023.2.0/dask_sql/physical/rel/custom/
--rw-r--r--   0 runner    (1001) docker     (123)     1362 2023-02-06 19:23:05.000000 dask_sql-2023.2.0/dask_sql/physical/rel/custom/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     2638 2023-02-06 19:23:05.000000 dask_sql-2023.2.0/dask_sql/physical/rel/custom/alter.py
--rw-r--r--   0 runner    (1001) docker     (123)     2470 2023-02-06 19:23:05.000000 dask_sql-2023.2.0/dask_sql/physical/rel/custom/analyze_table.py
--rw-r--r--   0 runner    (1001) docker     (123)     1173 2023-02-06 19:23:05.000000 dask_sql-2023.2.0/dask_sql/physical/rel/custom/create_catalog_schema.py
--rw-r--r--   0 runner    (1001) docker     (123)     8951 2023-02-06 19:23:05.000000 dask_sql-2023.2.0/dask_sql/physical/rel/custom/create_experiment.py
--rw-r--r--   0 runner    (1001) docker     (123)     2601 2023-02-06 19:23:05.000000 dask_sql-2023.2.0/dask_sql/physical/rel/custom/create_memory_table.py
--rw-r--r--   0 runner    (1001) docker     (123)     8128 2023-02-06 19:23:05.000000 dask_sql-2023.2.0/dask_sql/physical/rel/custom/create_model.py
--rw-r--r--   0 runner    (1001) docker     (123)     2426 2023-02-06 19:23:05.000000 dask_sql-2023.2.0/dask_sql/physical/rel/custom/create_table.py
--rw-r--r--   0 runner    (1001) docker     (123)     1418 2023-02-06 19:23:05.000000 dask_sql-2023.2.0/dask_sql/physical/rel/custom/describe_model.py
--rw-r--r--   0 runner    (1001) docker     (123)     1329 2023-02-06 19:23:05.000000 dask_sql-2023.2.0/dask_sql/physical/rel/custom/distributeby.py
--rw-r--r--   0 runner    (1001) docker     (123)     1039 2023-02-06 19:23:05.000000 dask_sql-2023.2.0/dask_sql/physical/rel/custom/drop_model.py
--rw-r--r--   0 runner    (1001) docker     (123)      880 2023-02-06 19:23:05.000000 dask_sql-2023.2.0/dask_sql/physical/rel/custom/drop_schema.py
--rw-r--r--   0 runner    (1001) docker     (123)     1448 2023-02-06 19:23:05.000000 dask_sql-2023.2.0/dask_sql/physical/rel/custom/drop_table.py
--rw-r--r--   0 runner    (1001) docker     (123)     3943 2023-02-06 19:23:05.000000 dask_sql-2023.2.0/dask_sql/physical/rel/custom/export_model.py
--rw-r--r--   0 runner    (1001) docker     (123)     6504 2023-02-06 19:23:05.000000 dask_sql-2023.2.0/dask_sql/physical/rel/custom/metrics.py
--rw-r--r--   0 runner    (1001) docker     (123)     3528 2023-02-06 19:23:05.000000 dask_sql-2023.2.0/dask_sql/physical/rel/custom/predict_model.py
--rw-r--r--   0 runner    (1001) docker     (123)     1183 2023-02-06 19:23:05.000000 dask_sql-2023.2.0/dask_sql/physical/rel/custom/schemas.py
--rw-r--r--   0 runner    (1001) docker     (123)     1524 2023-02-06 19:23:05.000000 dask_sql-2023.2.0/dask_sql/physical/rel/custom/show_columns.py
--rw-r--r--   0 runner    (1001) docker     (123)      913 2023-02-06 19:23:05.000000 dask_sql-2023.2.0/dask_sql/physical/rel/custom/show_models.py
--rw-r--r--   0 runner    (1001) docker     (123)     1146 2023-02-06 19:23:05.000000 dask_sql-2023.2.0/dask_sql/physical/rel/custom/show_tables.py
--rw-r--r--   0 runner    (1001) docker     (123)      902 2023-02-06 19:23:05.000000 dask_sql-2023.2.0/dask_sql/physical/rel/custom/use_schema.py
--rw-r--r--   0 runner    (1001) docker     (123)    28191 2023-02-06 19:23:05.000000 dask_sql-2023.2.0/dask_sql/physical/rel/custom/wrappers.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-06 21:36:49.546875 dask_sql-2023.2.0/dask_sql/physical/rel/logical/
--rw-r--r--   0 runner    (1001) docker     (123)      916 2023-02-06 19:23:05.000000 dask_sql-2023.2.0/dask_sql/physical/rel/logical/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    21656 2023-02-06 19:23:05.000000 dask_sql-2023.2.0/dask_sql/physical/rel/logical/aggregate.py
--rw-r--r--   0 runner    (1001) docker     (123)     1361 2023-02-06 19:23:05.000000 dask_sql-2023.2.0/dask_sql/physical/rel/logical/cross_join.py
--rw-r--r--   0 runner    (1001) docker     (123)     1109 2023-02-06 19:23:05.000000 dask_sql-2023.2.0/dask_sql/physical/rel/logical/empty.py
--rw-r--r--   0 runner    (1001) docker     (123)      494 2023-02-06 19:23:05.000000 dask_sql-2023.2.0/dask_sql/physical/rel/logical/explain.py
--rw-r--r--   0 runner    (1001) docker     (123)     2155 2023-02-06 19:23:05.000000 dask_sql-2023.2.0/dask_sql/physical/rel/logical/filter.py
--rw-r--r--   0 runner    (1001) docker     (123)    13095 2023-02-06 19:23:05.000000 dask_sql-2023.2.0/dask_sql/physical/rel/logical/join.py
--rw-r--r--   0 runner    (1001) docker     (123)     4176 2023-02-06 19:23:05.000000 dask_sql-2023.2.0/dask_sql/physical/rel/logical/limit.py
--rw-r--r--   0 runner    (1001) docker     (123)     2581 2023-02-06 19:23:05.000000 dask_sql-2023.2.0/dask_sql/physical/rel/logical/project.py
--rw-r--r--   0 runner    (1001) docker     (123)     2114 2023-02-06 19:23:05.000000 dask_sql-2023.2.0/dask_sql/physical/rel/logical/sample.py
--rw-r--r--   0 runner    (1001) docker     (123)     1309 2023-02-06 19:23:05.000000 dask_sql-2023.2.0/dask_sql/physical/rel/logical/sort.py
--rw-r--r--   0 runner    (1001) docker     (123)      948 2023-02-06 19:23:05.000000 dask_sql-2023.2.0/dask_sql/physical/rel/logical/subquery_alias.py
--rw-r--r--   0 runner    (1001) docker     (123)     3170 2023-02-06 19:23:05.000000 dask_sql-2023.2.0/dask_sql/physical/rel/logical/table_scan.py
--rw-r--r--   0 runner    (1001) docker     (123)     1988 2023-02-06 19:23:05.000000 dask_sql-2023.2.0/dask_sql/physical/rel/logical/union.py
--rw-r--r--   0 runner    (1001) docker     (123)     2191 2023-02-06 19:23:05.000000 dask_sql-2023.2.0/dask_sql/physical/rel/logical/values.py
--rw-r--r--   0 runner    (1001) docker     (123)    16331 2023-02-06 19:23:05.000000 dask_sql-2023.2.0/dask_sql/physical/rel/logical/window.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-06 21:36:49.546875 dask_sql-2023.2.0/dask_sql/physical/rex/
--rw-r--r--   0 runner    (1001) docker     (123)       34 2023-02-06 19:23:05.000000 dask_sql-2023.2.0/dask_sql/physical/rex/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      805 2023-02-06 19:23:05.000000 dask_sql-2023.2.0/dask_sql/physical/rex/base.py
--rw-r--r--   0 runner    (1001) docker     (123)     2375 2023-02-06 19:23:05.000000 dask_sql-2023.2.0/dask_sql/physical/rex/convert.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-06 21:36:49.546875 dask_sql-2023.2.0/dask_sql/physical/rex/core/
--rw-r--r--   0 runner    (1001) docker     (123)      244 2023-02-06 19:23:05.000000 dask_sql-2023.2.0/dask_sql/physical/rex/core/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    35329 2023-02-06 19:23:05.000000 dask_sql-2023.2.0/dask_sql/physical/rex/core/call.py
--rw-r--r--   0 runner    (1001) docker     (123)      933 2023-02-06 19:23:05.000000 dask_sql-2023.2.0/dask_sql/physical/rex/core/input_ref.py
--rw-r--r--   0 runner    (1001) docker     (123)     7636 2023-02-06 19:23:05.000000 dask_sql-2023.2.0/dask_sql/physical/rex/core/literal.py
--rw-r--r--   0 runner    (1001) docker     (123)      983 2023-02-06 19:23:05.000000 dask_sql-2023.2.0/dask_sql/physical/rex/core/subquery.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-06 21:36:49.546875 dask_sql-2023.2.0/dask_sql/physical/utils/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-06 19:23:05.000000 dask_sql-2023.2.0/dask_sql/physical/utils/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    13012 2023-02-06 19:23:05.000000 dask_sql-2023.2.0/dask_sql/physical/utils/filter.py
--rw-r--r--   0 runner    (1001) docker     (123)     1221 2023-02-06 19:23:05.000000 dask_sql-2023.2.0/dask_sql/physical/utils/groupby.py
--rw-r--r--   0 runner    (1001) docker     (123)     6509 2023-02-06 19:23:05.000000 dask_sql-2023.2.0/dask_sql/physical/utils/ml_classes.py
--rw-r--r--   0 runner    (1001) docker     (123)     4312 2023-02-06 19:23:05.000000 dask_sql-2023.2.0/dask_sql/physical/utils/sort.py
--rw-r--r--   0 runner    (1001) docker     (123)     7386 2023-02-06 19:23:05.000000 dask_sql-2023.2.0/dask_sql/physical/utils/statistics.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-06 21:36:49.550876 dask_sql-2023.2.0/dask_sql/server/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-06 19:23:05.000000 dask_sql-2023.2.0/dask_sql/server/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     9050 2023-02-06 19:23:05.000000 dask_sql-2023.2.0/dask_sql/server/app.py
--rw-r--r--   0 runner    (1001) docker     (123)     5031 2023-02-06 19:23:05.000000 dask_sql-2023.2.0/dask_sql/server/presto_jdbc.py
--rw-r--r--   0 runner    (1001) docker     (123)     3833 2023-02-06 19:23:05.000000 dask_sql-2023.2.0/dask_sql/server/responses.py
--rw-r--r--   0 runner    (1001) docker     (123)     2752 2023-02-06 19:23:05.000000 dask_sql-2023.2.0/dask_sql/sql-schema.yaml
--rw-r--r--   0 runner    (1001) docker     (123)      253 2023-02-06 19:23:05.000000 dask_sql-2023.2.0/dask_sql/sql.yaml
--rw-r--r--   0 runner    (1001) docker     (123)     7739 2023-02-06 19:23:05.000000 dask_sql-2023.2.0/dask_sql/utils.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-06 21:36:49.538875 dask_sql-2023.2.0/dask_sql.egg-info/
--rw-r--r--   0 runner    (1001) docker     (123)     8519 2023-02-06 21:36:49.000000 dask_sql-2023.2.0/dask_sql.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)     5702 2023-02-06 21:36:49.000000 dask_sql-2023.2.0/dask_sql.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-02-06 21:36:49.000000 dask_sql-2023.2.0/dask_sql.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (123)      170 2023-02-06 21:36:49.000000 dask_sql-2023.2.0/dask_sql.egg-info/entry_points.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-02-06 21:36:49.000000 dask_sql-2023.2.0/dask_sql.egg-info/not-zip-safe
--rw-r--r--   0 runner    (1001) docker     (123)      353 2023-02-06 21:36:49.000000 dask_sql-2023.2.0/dask_sql.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (123)        9 2023-02-06 21:36:49.000000 dask_sql-2023.2.0/dask_sql.egg-info/top_level.txt
--rw-r--r--   0 runner    (1001) docker     (123)      524 2023-02-06 21:36:49.550876 dask_sql-2023.2.0/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (123)     2446 2023-02-06 19:23:05.000000 dask_sql-2023.2.0/setup.py
--rw-r--r--   0 runner    (1001) docker     (123)    83601 2023-02-06 19:23:05.000000 dask_sql-2023.2.0/versioneer.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 14:40:06.719195 dask_sql-2023.4.0/
+-rw-r--r--   0 runner    (1001) docker     (123)     1067 2023-04-06 14:39:11.000000 dask_sql-2023.4.0/LICENSE.txt
+-rw-r--r--   0 runner    (1001) docker     (123)      119 2023-04-06 14:39:11.000000 dask_sql-2023.4.0/MANIFEST.in
+-rw-r--r--   0 runner    (1001) docker     (123)     8519 2023-04-06 14:40:06.719195 dask_sql-2023.4.0/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     8164 2023-04-06 14:39:11.000000 dask_sql-2023.4.0/README.md
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 14:40:06.699195 dask_sql-2023.4.0/dask_planner/
+-rw-r--r--   0 runner    (1001) docker     (123)     2210 2023-04-06 14:39:11.000000 dask_sql-2023.4.0/dask_planner/.classpath
+-rw-r--r--   0 runner    (1001) docker     (123)      686 2023-04-06 14:39:11.000000 dask_sql-2023.4.0/dask_planner/.gitignore
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 14:40:06.699195 dask_sql-2023.4.0/dask_planner/.settings/
+-rw-r--r--   0 runner    (1001) docker     (123)      173 2023-04-06 14:39:11.000000 dask_sql-2023.4.0/dask_planner/.settings/org.eclipse.core.resources.prefs
+-rw-r--r--   0 runner    (1001) docker     (123)       67 2023-04-06 14:39:11.000000 dask_sql-2023.4.0/dask_planner/.settings/org.eclipse.jdt.apt.core.prefs
+-rw-r--r--   0 runner    (1001) docker     (123)      479 2023-04-06 14:39:11.000000 dask_sql-2023.4.0/dask_planner/.settings/org.eclipse.jdt.core.prefs
+-rw-r--r--   0 runner    (1001) docker     (123)       86 2023-04-06 14:39:11.000000 dask_sql-2023.4.0/dask_planner/.settings/org.eclipse.m2e.core.prefs
+-rw-r--r--   0 runner    (1001) docker     (123)    59398 2023-04-06 14:39:11.000000 dask_sql-2023.4.0/dask_planner/Cargo.lock
+-rw-r--r--   0 runner    (1001) docker     (123)      829 2023-04-06 14:39:11.000000 dask_sql-2023.4.0/dask_planner/Cargo.toml
+-rw-r--r--   0 runner    (1001) docker     (123)       43 2023-04-06 14:39:11.000000 dask_sql-2023.4.0/dask_planner/MANIFEST.in
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 14:39:11.000000 dask_sql-2023.4.0/dask_planner/README.md
+-rw-r--r--   0 runner    (1001) docker     (123)      319 2023-04-06 14:39:11.000000 dask_sql-2023.4.0/dask_planner/pyproject.toml
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 14:40:06.699195 dask_sql-2023.4.0/dask_planner/src/
+-rw-r--r--   0 runner    (1001) docker     (123)     8923 2023-04-06 14:39:11.000000 dask_sql-2023.4.0/dask_planner/src/dialect.rs
+-rw-r--r--   0 runner    (1001) docker     (123)     1417 2023-04-06 14:39:11.000000 dask_sql-2023.4.0/dask_planner/src/error.rs
+-rw-r--r--   0 runner    (1001) docker     (123)    32752 2023-04-06 14:39:11.000000 dask_sql-2023.4.0/dask_planner/src/expression.rs
+-rw-r--r--   0 runner    (1001) docker     (123)     1418 2023-04-06 14:39:11.000000 dask_sql-2023.4.0/dask_planner/src/lib.rs
+-rw-r--r--   0 runner    (1001) docker     (123)    54776 2023-04-06 14:39:11.000000 dask_sql-2023.4.0/dask_planner/src/parser.rs
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 14:40:06.703195 dask_sql-2023.4.0/dask_planner/src/sql/
+-rw-r--r--   0 runner    (1001) docker     (123)      709 2023-04-06 14:39:11.000000 dask_sql-2023.4.0/dask_planner/src/sql/column.rs
+-rw-r--r--   0 runner    (1001) docker     (123)      871 2023-04-06 14:39:11.000000 dask_sql-2023.4.0/dask_planner/src/sql/exceptions.rs
+-rw-r--r--   0 runner    (1001) docker     (123)     1071 2023-04-06 14:39:11.000000 dask_sql-2023.4.0/dask_planner/src/sql/function.rs
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 14:40:06.707195 dask_sql-2023.4.0/dask_planner/src/sql/logical/
+-rw-r--r--   0 runner    (1001) docker     (123)     4065 2023-04-06 14:39:11.000000 dask_sql-2023.4.0/dask_planner/src/sql/logical/aggregate.rs
+-rw-r--r--   0 runner    (1001) docker     (123)     2946 2023-04-06 14:39:11.000000 dask_sql-2023.4.0/dask_planner/src/sql/logical/alter_schema.rs
+-rw-r--r--   0 runner    (1001) docker     (123)     3317 2023-04-06 14:39:11.000000 dask_sql-2023.4.0/dask_planner/src/sql/logical/alter_table.rs
+-rw-r--r--   0 runner    (1001) docker     (123)     3116 2023-04-06 14:39:11.000000 dask_sql-2023.4.0/dask_planner/src/sql/logical/analyze_table.rs
+-rw-r--r--   0 runner    (1001) docker     (123)     3160 2023-04-06 14:39:11.000000 dask_sql-2023.4.0/dask_planner/src/sql/logical/create_catalog_schema.rs
+-rw-r--r--   0 runner    (1001) docker     (123)     4099 2023-04-06 14:39:11.000000 dask_sql-2023.4.0/dask_planner/src/sql/logical/create_experiment.rs
+-rw-r--r--   0 runner    (1001) docker     (123)     3428 2023-04-06 14:39:11.000000 dask_sql-2023.4.0/dask_planner/src/sql/logical/create_memory_table.rs
+-rw-r--r--   0 runner    (1001) docker     (123)     3892 2023-04-06 14:39:11.000000 dask_sql-2023.4.0/dask_planner/src/sql/logical/create_model.rs
+-rw-r--r--   0 runner    (1001) docker     (123)     3480 2023-04-06 14:39:11.000000 dask_sql-2023.4.0/dask_planner/src/sql/logical/create_table.rs
+-rw-r--r--   0 runner    (1001) docker     (123)     2822 2023-04-06 14:39:11.000000 dask_sql-2023.4.0/dask_planner/src/sql/logical/describe_model.rs
+-rw-r--r--   0 runner    (1001) docker     (123)     2870 2023-04-06 14:39:11.000000 dask_sql-2023.4.0/dask_planner/src/sql/logical/drop_model.rs
+-rw-r--r--   0 runner    (1001) docker     (123)     2589 2023-04-06 14:39:11.000000 dask_sql-2023.4.0/dask_planner/src/sql/logical/drop_schema.rs
+-rw-r--r--   0 runner    (1001) docker     (123)      895 2023-04-06 14:39:11.000000 dask_sql-2023.4.0/dask_planner/src/sql/logical/drop_table.rs
+-rw-r--r--   0 runner    (1001) docker     (123)     1154 2023-04-06 14:39:11.000000 dask_sql-2023.4.0/dask_planner/src/sql/logical/empty_relation.rs
+-rw-r--r--   0 runner    (1001) docker     (123)      963 2023-04-06 14:39:11.000000 dask_sql-2023.4.0/dask_planner/src/sql/logical/explain.rs
+-rw-r--r--   0 runner    (1001) docker     (123)     3087 2023-04-06 14:39:11.000000 dask_sql-2023.4.0/dask_planner/src/sql/logical/export_model.rs
+-rw-r--r--   0 runner    (1001) docker     (123)      932 2023-04-06 14:39:11.000000 dask_sql-2023.4.0/dask_planner/src/sql/logical/filter.rs
+-rw-r--r--   0 runner    (1001) docker     (123)     4458 2023-04-06 14:39:11.000000 dask_sql-2023.4.0/dask_planner/src/sql/logical/join.rs
+-rw-r--r--   0 runner    (1001) docker     (123)     1258 2023-04-06 14:39:11.000000 dask_sql-2023.4.0/dask_planner/src/sql/logical/limit.rs
+-rw-r--r--   0 runner    (1001) docker     (123)     2961 2023-04-06 14:39:11.000000 dask_sql-2023.4.0/dask_planner/src/sql/logical/predict_model.rs
+-rw-r--r--   0 runner    (1001) docker     (123)     1889 2023-04-06 14:39:11.000000 dask_sql-2023.4.0/dask_planner/src/sql/logical/projection.rs
+-rw-r--r--   0 runner    (1001) docker     (123)     1978 2023-04-06 14:39:11.000000 dask_sql-2023.4.0/dask_planner/src/sql/logical/repartition_by.rs
+-rw-r--r--   0 runner    (1001) docker     (123)     2814 2023-04-06 14:39:11.000000 dask_sql-2023.4.0/dask_planner/src/sql/logical/show_columns.rs
+-rw-r--r--   0 runner    (1001) docker     (123)     2338 2023-04-06 14:39:11.000000 dask_sql-2023.4.0/dask_planner/src/sql/logical/show_models.rs
+-rw-r--r--   0 runner    (1001) docker     (123)     2768 2023-04-06 14:39:11.000000 dask_sql-2023.4.0/dask_planner/src/sql/logical/show_schemas.rs
+-rw-r--r--   0 runner    (1001) docker     (123)     2847 2023-04-06 14:39:11.000000 dask_sql-2023.4.0/dask_planner/src/sql/logical/show_tables.rs
+-rw-r--r--   0 runner    (1001) docker     (123)      950 2023-04-06 14:39:11.000000 dask_sql-2023.4.0/dask_planner/src/sql/logical/sort.rs
+-rw-r--r--   0 runner    (1001) docker     (123)      844 2023-04-06 14:39:11.000000 dask_sql-2023.4.0/dask_planner/src/sql/logical/subquery_alias.rs
+-rw-r--r--   0 runner    (1001) docker     (123)     2198 2023-04-06 14:39:11.000000 dask_sql-2023.4.0/dask_planner/src/sql/logical/table_scan.rs
+-rw-r--r--   0 runner    (1001) docker     (123)     2381 2023-04-06 14:39:11.000000 dask_sql-2023.4.0/dask_planner/src/sql/logical/use_schema.rs
+-rw-r--r--   0 runner    (1001) docker     (123)     6120 2023-04-06 14:39:11.000000 dask_sql-2023.4.0/dask_planner/src/sql/logical/window.rs
+-rw-r--r--   0 runner    (1001) docker     (123)    17145 2023-04-06 14:39:11.000000 dask_sql-2023.4.0/dask_planner/src/sql/logical.rs
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 14:40:06.707195 dask_sql-2023.4.0/dask_planner/src/sql/optimizer/
+-rw-r--r--   0 runner    (1001) docker     (123)    22403 2023-04-06 14:39:11.000000 dask_sql-2023.4.0/dask_planner/src/sql/optimizer/filter_columns_post_join.rs
+-rw-r--r--   0 runner    (1001) docker     (123)    13564 2023-04-06 14:39:11.000000 dask_sql-2023.4.0/dask_planner/src/sql/optimizer/join_reorder.rs
+-rw-r--r--   0 runner    (1001) docker     (123)     7983 2023-04-06 14:39:11.000000 dask_sql-2023.4.0/dask_planner/src/sql/optimizer.rs
+-rw-r--r--   0 runner    (1001) docker     (123)      736 2023-04-06 14:39:11.000000 dask_sql-2023.4.0/dask_planner/src/sql/parser_utils.rs
+-rw-r--r--   0 runner    (1001) docker     (123)     1505 2023-04-06 14:39:11.000000 dask_sql-2023.4.0/dask_planner/src/sql/schema.rs
+-rw-r--r--   0 runner    (1001) docker     (123)      591 2023-04-06 14:39:11.000000 dask_sql-2023.4.0/dask_planner/src/sql/statement.rs
+-rw-r--r--   0 runner    (1001) docker     (123)     9684 2023-04-06 14:39:11.000000 dask_sql-2023.4.0/dask_planner/src/sql/table.rs
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 14:40:06.707195 dask_sql-2023.4.0/dask_planner/src/sql/types/
+-rw-r--r--   0 runner    (1001) docker     (123)     3673 2023-04-06 14:39:11.000000 dask_sql-2023.4.0/dask_planner/src/sql/types/rel_data_type.rs
+-rw-r--r--   0 runner    (1001) docker     (123)     3671 2023-04-06 14:39:11.000000 dask_sql-2023.4.0/dask_planner/src/sql/types/rel_data_type_field.rs
+-rw-r--r--   0 runner    (1001) docker     (123)    15196 2023-04-06 14:39:11.000000 dask_sql-2023.4.0/dask_planner/src/sql/types.rs
+-rw-r--r--   0 runner    (1001) docker     (123)    31438 2023-04-06 14:39:11.000000 dask_sql-2023.4.0/dask_planner/src/sql.rs
+-rw-r--r--   0 runner    (1001) docker     (123)      362 2023-04-06 14:39:11.000000 dask_sql-2023.4.0/dask_planner/update-dependencies.sh
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 14:40:06.719195 dask_sql-2023.4.0/dask_sql/
+-rw-r--r--   0 runner    (1001) docker     (123)      277 2023-04-06 14:39:11.000000 dask_sql-2023.4.0/dask_sql/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      733 2023-04-06 14:39:11.000000 dask_sql-2023.4.0/dask_sql/_compat.py
+-rw-r--r--   0 runner    (1001) docker     (123)      500 2023-04-06 14:40:06.719195 dask_sql-2023.4.0/dask_sql/_version.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9016 2023-04-06 14:39:11.000000 dask_sql-2023.4.0/dask_sql/cmd.py
+-rw-r--r--   0 runner    (1001) docker     (123)      235 2023-04-06 14:39:11.000000 dask_sql-2023.4.0/dask_sql/config.py
+-rw-r--r--   0 runner    (1001) docker     (123)    36295 2023-04-06 14:39:11.000000 dask_sql-2023.4.0/dask_sql/context.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9511 2023-04-06 14:39:11.000000 dask_sql-2023.4.0/dask_sql/datacontainer.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 14:40:06.711195 dask_sql-2023.4.0/dask_sql/input_utils/
+-rw-r--r--   0 runner    (1001) docker     (123)      493 2023-04-06 14:39:11.000000 dask_sql-2023.4.0/dask_sql/input_utils/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      312 2023-04-06 14:39:11.000000 dask_sql-2023.4.0/dask_sql/input_utils/base.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2671 2023-04-06 14:39:11.000000 dask_sql-2023.4.0/dask_sql/input_utils/convert.py
+-rw-r--r--   0 runner    (1001) docker     (123)      982 2023-04-06 14:39:11.000000 dask_sql-2023.4.0/dask_sql/input_utils/dask.py
+-rw-r--r--   0 runner    (1001) docker     (123)    11719 2023-04-06 14:39:11.000000 dask_sql-2023.4.0/dask_sql/input_utils/hive.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1080 2023-04-06 14:39:11.000000 dask_sql-2023.4.0/dask_sql/input_utils/intake.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1773 2023-04-06 14:39:11.000000 dask_sql-2023.4.0/dask_sql/input_utils/location.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1146 2023-04-06 14:39:11.000000 dask_sql-2023.4.0/dask_sql/input_utils/pandaslike.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1222 2023-04-06 14:39:11.000000 dask_sql-2023.4.0/dask_sql/input_utils/sqlalchemy.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 14:40:06.711195 dask_sql-2023.4.0/dask_sql/integrations/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 14:39:11.000000 dask_sql-2023.4.0/dask_sql/integrations/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5103 2023-04-06 14:39:11.000000 dask_sql-2023.4.0/dask_sql/integrations/fugue.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4589 2023-04-06 14:39:11.000000 dask_sql-2023.4.0/dask_sql/integrations/ipython.py
+-rw-r--r--   0 runner    (1001) docker     (123)    10547 2023-04-06 14:39:11.000000 dask_sql-2023.4.0/dask_sql/mappings.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 14:40:06.711195 dask_sql-2023.4.0/dask_sql/physical/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 14:39:11.000000 dask_sql-2023.4.0/dask_sql/physical/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 14:40:06.711195 dask_sql-2023.4.0/dask_sql/physical/rel/
+-rw-r--r--   0 runner    (1001) docker     (123)       34 2023-04-06 14:39:11.000000 dask_sql-2023.4.0/dask_sql/physical/rel/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3858 2023-04-06 14:39:11.000000 dask_sql-2023.4.0/dask_sql/physical/rel/base.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2264 2023-04-06 14:39:11.000000 dask_sql-2023.4.0/dask_sql/physical/rel/convert.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 14:40:06.715195 dask_sql-2023.4.0/dask_sql/physical/rel/custom/
+-rw-r--r--   0 runner    (1001) docker     (123)     1367 2023-04-06 14:39:11.000000 dask_sql-2023.4.0/dask_sql/physical/rel/custom/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2638 2023-04-06 14:39:11.000000 dask_sql-2023.4.0/dask_sql/physical/rel/custom/alter.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2396 2023-04-06 14:39:11.000000 dask_sql-2023.4.0/dask_sql/physical/rel/custom/analyze_table.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1173 2023-04-06 14:39:11.000000 dask_sql-2023.4.0/dask_sql/physical/rel/custom/create_catalog_schema.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9488 2023-04-06 14:39:11.000000 dask_sql-2023.4.0/dask_sql/physical/rel/custom/create_experiment.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2601 2023-04-06 14:39:11.000000 dask_sql-2023.4.0/dask_sql/physical/rel/custom/create_memory_table.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8644 2023-04-06 14:39:11.000000 dask_sql-2023.4.0/dask_sql/physical/rel/custom/create_model.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2426 2023-04-06 14:39:11.000000 dask_sql-2023.4.0/dask_sql/physical/rel/custom/create_table.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1418 2023-04-06 14:39:11.000000 dask_sql-2023.4.0/dask_sql/physical/rel/custom/describe_model.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1329 2023-04-06 14:39:11.000000 dask_sql-2023.4.0/dask_sql/physical/rel/custom/distributeby.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1039 2023-04-06 14:39:11.000000 dask_sql-2023.4.0/dask_sql/physical/rel/custom/drop_model.py
+-rw-r--r--   0 runner    (1001) docker     (123)      880 2023-04-06 14:39:11.000000 dask_sql-2023.4.0/dask_sql/physical/rel/custom/drop_schema.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1448 2023-04-06 14:39:11.000000 dask_sql-2023.4.0/dask_sql/physical/rel/custom/drop_table.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3943 2023-04-06 14:39:11.000000 dask_sql-2023.4.0/dask_sql/physical/rel/custom/export_model.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6504 2023-04-06 14:39:11.000000 dask_sql-2023.4.0/dask_sql/physical/rel/custom/metrics.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3528 2023-04-06 14:39:11.000000 dask_sql-2023.4.0/dask_sql/physical/rel/custom/predict_model.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1458 2023-04-06 14:39:11.000000 dask_sql-2023.4.0/dask_sql/physical/rel/custom/show_columns.py
+-rw-r--r--   0 runner    (1001) docker     (123)      913 2023-04-06 14:39:11.000000 dask_sql-2023.4.0/dask_sql/physical/rel/custom/show_models.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1501 2023-04-06 14:39:11.000000 dask_sql-2023.4.0/dask_sql/physical/rel/custom/show_schemas.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1520 2023-04-06 14:39:11.000000 dask_sql-2023.4.0/dask_sql/physical/rel/custom/show_tables.py
+-rw-r--r--   0 runner    (1001) docker     (123)      902 2023-04-06 14:39:11.000000 dask_sql-2023.4.0/dask_sql/physical/rel/custom/use_schema.py
+-rw-r--r--   0 runner    (1001) docker     (123)    28191 2023-04-06 14:39:11.000000 dask_sql-2023.4.0/dask_sql/physical/rel/custom/wrappers.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 14:40:06.715195 dask_sql-2023.4.0/dask_sql/physical/rel/logical/
+-rw-r--r--   0 runner    (1001) docker     (123)      916 2023-04-06 14:39:11.000000 dask_sql-2023.4.0/dask_sql/physical/rel/logical/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    21656 2023-04-06 14:39:11.000000 dask_sql-2023.4.0/dask_sql/physical/rel/logical/aggregate.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1328 2023-04-06 14:39:11.000000 dask_sql-2023.4.0/dask_sql/physical/rel/logical/cross_join.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1109 2023-04-06 14:39:11.000000 dask_sql-2023.4.0/dask_sql/physical/rel/logical/empty.py
+-rw-r--r--   0 runner    (1001) docker     (123)      494 2023-04-06 14:39:11.000000 dask_sql-2023.4.0/dask_sql/physical/rel/logical/explain.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2155 2023-04-06 14:39:11.000000 dask_sql-2023.4.0/dask_sql/physical/rel/logical/filter.py
+-rw-r--r--   0 runner    (1001) docker     (123)    13610 2023-04-06 14:39:11.000000 dask_sql-2023.4.0/dask_sql/physical/rel/logical/join.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4176 2023-04-06 14:39:11.000000 dask_sql-2023.4.0/dask_sql/physical/rel/logical/limit.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2581 2023-04-06 14:39:11.000000 dask_sql-2023.4.0/dask_sql/physical/rel/logical/project.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2114 2023-04-06 14:39:11.000000 dask_sql-2023.4.0/dask_sql/physical/rel/logical/sample.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1309 2023-04-06 14:39:11.000000 dask_sql-2023.4.0/dask_sql/physical/rel/logical/sort.py
+-rw-r--r--   0 runner    (1001) docker     (123)      948 2023-04-06 14:39:11.000000 dask_sql-2023.4.0/dask_sql/physical/rel/logical/subquery_alias.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3213 2023-04-06 14:39:11.000000 dask_sql-2023.4.0/dask_sql/physical/rel/logical/table_scan.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1988 2023-04-06 14:39:11.000000 dask_sql-2023.4.0/dask_sql/physical/rel/logical/union.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2191 2023-04-06 14:39:11.000000 dask_sql-2023.4.0/dask_sql/physical/rel/logical/values.py
+-rw-r--r--   0 runner    (1001) docker     (123)    15794 2023-04-06 14:39:11.000000 dask_sql-2023.4.0/dask_sql/physical/rel/logical/window.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 14:40:06.715195 dask_sql-2023.4.0/dask_sql/physical/rex/
+-rw-r--r--   0 runner    (1001) docker     (123)       34 2023-04-06 14:39:11.000000 dask_sql-2023.4.0/dask_sql/physical/rex/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      805 2023-04-06 14:39:11.000000 dask_sql-2023.4.0/dask_sql/physical/rex/base.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2410 2023-04-06 14:39:11.000000 dask_sql-2023.4.0/dask_sql/physical/rex/convert.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 14:40:06.715195 dask_sql-2023.4.0/dask_sql/physical/rex/core/
+-rw-r--r--   0 runner    (1001) docker     (123)      319 2023-04-06 14:39:11.000000 dask_sql-2023.4.0/dask_sql/physical/rex/core/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1151 2023-04-06 14:39:11.000000 dask_sql-2023.4.0/dask_sql/physical/rex/core/alias.py
+-rw-r--r--   0 runner    (1001) docker     (123)    35329 2023-04-06 14:39:11.000000 dask_sql-2023.4.0/dask_sql/physical/rex/core/call.py
+-rw-r--r--   0 runner    (1001) docker     (123)      933 2023-04-06 14:39:11.000000 dask_sql-2023.4.0/dask_sql/physical/rex/core/input_ref.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7636 2023-04-06 14:39:11.000000 dask_sql-2023.4.0/dask_sql/physical/rex/core/literal.py
+-rw-r--r--   0 runner    (1001) docker     (123)      986 2023-04-06 14:39:11.000000 dask_sql-2023.4.0/dask_sql/physical/rex/core/subquery.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 14:40:06.719195 dask_sql-2023.4.0/dask_sql/physical/utils/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 14:39:11.000000 dask_sql-2023.4.0/dask_sql/physical/utils/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    13012 2023-04-06 14:39:11.000000 dask_sql-2023.4.0/dask_sql/physical/utils/filter.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1221 2023-04-06 14:39:11.000000 dask_sql-2023.4.0/dask_sql/physical/utils/groupby.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6509 2023-04-06 14:39:11.000000 dask_sql-2023.4.0/dask_sql/physical/utils/ml_classes.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4312 2023-04-06 14:39:11.000000 dask_sql-2023.4.0/dask_sql/physical/utils/sort.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7449 2023-04-06 14:39:11.000000 dask_sql-2023.4.0/dask_sql/physical/utils/statistics.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 14:40:06.719195 dask_sql-2023.4.0/dask_sql/server/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 14:39:11.000000 dask_sql-2023.4.0/dask_sql/server/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8811 2023-04-06 14:39:11.000000 dask_sql-2023.4.0/dask_sql/server/app.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5031 2023-04-06 14:39:11.000000 dask_sql-2023.4.0/dask_sql/server/presto_jdbc.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4195 2023-04-06 14:39:11.000000 dask_sql-2023.4.0/dask_sql/server/responses.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2752 2023-04-06 14:39:11.000000 dask_sql-2023.4.0/dask_sql/sql-schema.yaml
+-rw-r--r--   0 runner    (1001) docker     (123)      253 2023-04-06 14:39:11.000000 dask_sql-2023.4.0/dask_sql/sql.yaml
+-rw-r--r--   0 runner    (1001) docker     (123)     7739 2023-04-06 14:39:11.000000 dask_sql-2023.4.0/dask_sql/utils.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 14:40:06.707195 dask_sql-2023.4.0/dask_sql.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)     8519 2023-04-06 14:40:06.000000 dask_sql-2023.4.0/dask_sql.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     5791 2023-04-06 14:40:06.000000 dask_sql-2023.4.0/dask_sql.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-06 14:40:06.000000 dask_sql-2023.4.0/dask_sql.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)      170 2023-04-06 14:40:06.000000 dask_sql-2023.4.0/dask_sql.egg-info/entry_points.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-06 14:40:06.000000 dask_sql-2023.4.0/dask_sql.egg-info/not-zip-safe
+-rw-r--r--   0 runner    (1001) docker     (123)      364 2023-04-06 14:40:06.000000 dask_sql-2023.4.0/dask_sql.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        9 2023-04-06 14:40:06.000000 dask_sql-2023.4.0/dask_sql.egg-info/top_level.txt
+-rw-r--r--   0 runner    (1001) docker     (123)      524 2023-04-06 14:40:06.719195 dask_sql-2023.4.0/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (123)     2457 2023-04-06 14:39:11.000000 dask_sql-2023.4.0/setup.py
+-rw-r--r--   0 runner    (1001) docker     (123)    83601 2023-04-06 14:39:11.000000 dask_sql-2023.4.0/versioneer.py
```

### Comparing `dask_sql-2023.2.0/LICENSE.txt` & `dask_sql-2023.4.0/LICENSE.txt`

 * *Files identical despite different names*

### Comparing `dask_sql-2023.2.0/PKG-INFO` & `dask_sql-2023.4.0/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: dask_sql
-Version: 2023.2.0
+Version: 2023.4.0
 Summary: SQL query layer for Dask
 Home-page: https://github.com/dask-contrib/dask-sql/
 Maintainer: Nils Braun
 Maintainer-email: nilslennartbraun@gmail.com
 License: MIT
 Requires-Python: >=3.8
 Description-Content-Type: text/markdown
```

### Comparing `dask_sql-2023.2.0/README.md` & `dask_sql-2023.4.0/README.md`

 * *Files identical despite different names*

### Comparing `dask_sql-2023.2.0/dask_planner/.classpath` & `dask_sql-2023.4.0/dask_planner/.classpath`

 * *Files identical despite different names*

### Comparing `dask_sql-2023.2.0/dask_planner/.gitignore` & `dask_sql-2023.4.0/dask_planner/.gitignore`

 * *Files identical despite different names*

### Comparing `dask_sql-2023.2.0/dask_planner/Cargo.lock` & `dask_sql-2023.4.0/dask_planner/Cargo.lock`

 * *Files 19% similar despite different names*

```diff
@@ -1,293 +1,445 @@
 # This file is automatically @generated by Cargo.
 # It is not intended for manual editing.
 version = 3
 
 [[package]]
+name = "adler"
+version = "1.0.2"
+source = "registry+https://github.com/rust-lang/crates.io-index"
+checksum = "f26201604c87b1e01bd3d98f8d5d9a8fcbb815e8cedb41ffccbeb4bf593a35fe"
+
+[[package]]
 name = "ahash"
-version = "0.8.1"
+version = "0.8.3"
 source = "registry+https://github.com/rust-lang/crates.io-index"
-checksum = "464b3811b747f8f7ebc8849c9c728c39f6ac98a055edad93baf9eb330e3f8f9d"
+checksum = "2c99f64d1e06488f620f932677e24bc6e2897582980441ae90a671415bd7ec2f"
 dependencies = [
  "cfg-if",
  "const-random",
  "getrandom",
  "once_cell",
  "version_check",
 ]
 
 [[package]]
 name = "aho-corasick"
-version = "0.7.19"
+version = "0.7.20"
 source = "registry+https://github.com/rust-lang/crates.io-index"
-checksum = "b4f55bd91a0978cbfd91c457a164bab8b4001c833b7f323132c0a4e1922dd44e"
+checksum = "cc936419f96fa211c1b9166887b38e5e40b19958e5b895be7c1f93adec7071ac"
 dependencies = [
  "memchr",
 ]
 
 [[package]]
+name = "alloc-no-stdlib"
+version = "2.0.4"
+source = "registry+https://github.com/rust-lang/crates.io-index"
+checksum = "cc7bb162ec39d46ab1ca8c77bf72e890535becd1751bb45f64c597edb4c8c6b3"
+
+[[package]]
+name = "alloc-stdlib"
+version = "0.2.2"
+source = "registry+https://github.com/rust-lang/crates.io-index"
+checksum = "94fb8275041c72129eb51b7d0322c29b8387a0386127718b096429201a5d6ece"
+dependencies = [
+ "alloc-no-stdlib",
+]
+
+[[package]]
 name = "android_system_properties"
 version = "0.1.5"
 source = "registry+https://github.com/rust-lang/crates.io-index"
 checksum = "819e7219dbd41043ac279b19830f2efc897156490d7fd6ea916720117ee66311"
 dependencies = [
  "libc",
 ]
 
 [[package]]
+name = "arc-swap"
+version = "1.6.0"
+source = "registry+https://github.com/rust-lang/crates.io-index"
+checksum = "bddcadddf5e9015d310179a59bb28c4d4b9920ad0f11e8e14dbadf654890c9a6"
+
+[[package]]
 name = "arrayref"
-version = "0.3.6"
+version = "0.3.7"
 source = "registry+https://github.com/rust-lang/crates.io-index"
-checksum = "a4c527152e37cf757a3f78aae5a06fbeefdb07ccc535c980a3208ee3060dd544"
+checksum = "6b4930d2cb77ce62f89ee5d5289b4ac049559b1c45539271f5ed4fdc7db34545"
 
 [[package]]
 name = "arrayvec"
 version = "0.7.2"
 source = "registry+https://github.com/rust-lang/crates.io-index"
 checksum = "8da52d66c7071e2e3fa2a1e5c6d088fec47b593032b254f5e980de8ea54454d6"
 
 [[package]]
 name = "arrow"
-version = "28.0.0"
+version = "32.0.0"
 source = "registry+https://github.com/rust-lang/crates.io-index"
-checksum = "aed9849f86164fad5cb66ce4732782b15f1bc97f8febab04e782c20cce9d4b6c"
+checksum = "87d948f553cf556656eb89265700258e1032d26fec9b7920cd20319336e06afd"
 dependencies = [
  "ahash",
+ "arrow-arith",
  "arrow-array",
  "arrow-buffer",
  "arrow-cast",
  "arrow-csv",
  "arrow-data",
  "arrow-ipc",
  "arrow-json",
+ "arrow-ord",
+ "arrow-row",
  "arrow-schema",
  "arrow-select",
- "chrono",
+ "arrow-string",
  "comfy-table",
+]
+
+[[package]]
+name = "arrow-arith"
+version = "32.0.0"
+source = "registry+https://github.com/rust-lang/crates.io-index"
+checksum = "cf30d4ebc3df9dfd8bd26883aa30687d4ddcfd7b2443e62bd7c8fedf153b8e45"
+dependencies = [
+ "arrow-array",
+ "arrow-buffer",
+ "arrow-data",
+ "arrow-schema",
+ "chrono",
  "half",
- "hashbrown 0.13.1",
- "multiversion",
  "num",
- "regex",
- "regex-syntax",
 ]
 
 [[package]]
 name = "arrow-array"
-version = "28.0.0"
+version = "32.0.0"
 source = "registry+https://github.com/rust-lang/crates.io-index"
-checksum = "6b8504cf0a6797e908eecf221a865e7d339892720587f87c8b90262863015b08"
+checksum = "9fe66ec388d882a61fff3eb613b5266af133aa08a3318e5e493daf0f5c1696cb"
 dependencies = [
  "ahash",
  "arrow-buffer",
  "arrow-data",
  "arrow-schema",
  "chrono",
  "half",
- "hashbrown 0.13.1",
+ "hashbrown 0.13.2",
  "num",
 ]
 
 [[package]]
 name = "arrow-buffer"
-version = "28.0.0"
+version = "32.0.0"
 source = "registry+https://github.com/rust-lang/crates.io-index"
-checksum = "d6de64a27cea684b24784647d9608314bc80f7c4d55acb44a425e05fab39d916"
+checksum = "4ef967dadbccd4586ec8d7aab27d7033ecb5dfae8a605c839613039eac227bda"
 dependencies = [
  "half",
  "num",
 ]
 
 [[package]]
 name = "arrow-cast"
-version = "28.0.0"
+version = "32.0.0"
 source = "registry+https://github.com/rust-lang/crates.io-index"
-checksum = "bec4a54502eefe05923c385c90a005d69474fa06ca7aa2a2b123c9f9532f6178"
+checksum = "491a7979ea9e76dc218f532896e2d245fde5235e2e6420ce80d27cf6395dda84"
 dependencies = [
  "arrow-array",
  "arrow-buffer",
  "arrow-data",
  "arrow-schema",
  "arrow-select",
  "chrono",
  "lexical-core",
  "num",
 ]
 
 [[package]]
 name = "arrow-csv"
-version = "28.0.0"
+version = "32.0.0"
 source = "registry+https://github.com/rust-lang/crates.io-index"
-checksum = "e7902bbf8127eac48554fe902775303377047ad49a9fd473c2b8cb399d092080"
+checksum = "4b1d4fc91078dbe843c2c50d90f8119c96e8dfac2f78d30f7a8cb9397399c61d"
 dependencies = [
  "arrow-array",
  "arrow-buffer",
  "arrow-cast",
  "arrow-data",
  "arrow-schema",
  "chrono",
  "csv",
+ "csv-core",
  "lazy_static",
  "lexical-core",
  "regex",
 ]
 
 [[package]]
 name = "arrow-data"
-version = "28.0.0"
+version = "32.0.0"
 source = "registry+https://github.com/rust-lang/crates.io-index"
-checksum = "7e4882efe617002449d5c6b5de9ddb632339074b36df8a96ea7147072f1faa8a"
+checksum = "ee0c0e3c5d3b80be8f267f4b2af714c08cad630569be01a8379cfe27b4866495"
 dependencies = [
  "arrow-buffer",
  "arrow-schema",
  "half",
  "num",
 ]
 
 [[package]]
 name = "arrow-ipc"
-version = "28.0.0"
+version = "32.0.0"
 source = "registry+https://github.com/rust-lang/crates.io-index"
-checksum = "fa0703a6de2785828561b03a4d7793ecd333233e1b166316b4bfc7cfce55a4a7"
+checksum = "0a3ca7eb8d23c83fe40805cbafec70a6a31df72de47355545ff34c850f715403"
 dependencies = [
  "arrow-array",
  "arrow-buffer",
  "arrow-cast",
  "arrow-data",
  "arrow-schema",
  "flatbuffers",
 ]
 
 [[package]]
 name = "arrow-json"
-version = "28.0.0"
+version = "32.0.0"
 source = "registry+https://github.com/rust-lang/crates.io-index"
-checksum = "3bd23fc8c6d251f96cd63b96fece56bbb9710ce5874a627cb786e2600673595a"
+checksum = "bf65aff76d2e340d827d5cab14759e7dd90891a288347e2202e4ee28453d9bed"
 dependencies = [
  "arrow-array",
  "arrow-buffer",
  "arrow-cast",
  "arrow-data",
  "arrow-schema",
  "chrono",
  "half",
  "indexmap",
+ "lexical-core",
  "num",
  "serde_json",
 ]
 
 [[package]]
+name = "arrow-ord"
+version = "32.0.0"
+source = "registry+https://github.com/rust-lang/crates.io-index"
+checksum = "074a5a55c37ae4750af4811c8861c0378d8ab2ff6c262622ad24efae6e0b73b3"
+dependencies = [
+ "arrow-array",
+ "arrow-buffer",
+ "arrow-data",
+ "arrow-schema",
+ "arrow-select",
+ "num",
+]
+
+[[package]]
+name = "arrow-row"
+version = "32.0.0"
+source = "registry+https://github.com/rust-lang/crates.io-index"
+checksum = "e064ac4e64960ebfbe35f218f5e7d9dc9803b59c2e56f611da28ce6d008f839e"
+dependencies = [
+ "ahash",
+ "arrow-array",
+ "arrow-buffer",
+ "arrow-data",
+ "arrow-schema",
+ "half",
+ "hashbrown 0.13.2",
+]
+
+[[package]]
 name = "arrow-schema"
-version = "28.0.0"
+version = "32.0.0"
 source = "registry+https://github.com/rust-lang/crates.io-index"
-checksum = "da9f143882a80be168538a60e298546314f50f11f2a288c8d73e11108da39d26"
+checksum = "ead3f373b9173af52f2fdefcb5a7dd89f453fbc40056f574a8aeb23382a4ef81"
 
 [[package]]
 name = "arrow-select"
-version = "28.0.0"
+version = "32.0.0"
 source = "registry+https://github.com/rust-lang/crates.io-index"
-checksum = "520406331d4ad60075359524947ebd804e479816439af82bcb17f8d280d9b38c"
+checksum = "646b4f15b5a77c970059e748aeb1539705c68cd397ecf0f0264c4ef3737d35f3"
 dependencies = [
  "arrow-array",
  "arrow-buffer",
  "arrow-data",
  "arrow-schema",
  "num",
 ]
 
 [[package]]
+name = "arrow-string"
+version = "32.0.0"
+source = "registry+https://github.com/rust-lang/crates.io-index"
+checksum = "c8b8bf150caaeca03f39f1a91069701387d93f7cfd256d27f423ac8496d99a51"
+dependencies = [
+ "arrow-array",
+ "arrow-buffer",
+ "arrow-data",
+ "arrow-schema",
+ "arrow-select",
+ "regex",
+ "regex-syntax",
+]
+
+[[package]]
+name = "async-compression"
+version = "0.3.15"
+source = "registry+https://github.com/rust-lang/crates.io-index"
+checksum = "942c7cd7ae39e91bde4820d74132e9862e62c2f386c3aa90ccf55949f5bad63a"
+dependencies = [
+ "bzip2",
+ "flate2",
+ "futures-core",
+ "futures-io",
+ "memchr",
+ "pin-project-lite",
+ "tokio",
+ "xz2",
+]
+
+[[package]]
 name = "async-trait"
-version = "0.1.64"
+version = "0.1.68"
 source = "registry+https://github.com/rust-lang/crates.io-index"
-checksum = "1cd7fce9ba8c3c042128ce72d8b2ddbf3a05747efb67ea0313c635e10bda47a2"
+checksum = "b9ccdd8f2a161be9bd5c023df56f1b2a0bd1d83872ae53b71a84a12c9bf6e842"
 dependencies = [
  "proc-macro2",
  "quote",
- "syn",
+ "syn 2.0.11",
 ]
 
 [[package]]
 name = "autocfg"
 version = "1.1.0"
 source = "registry+https://github.com/rust-lang/crates.io-index"
 checksum = "d468802bab17cbc0cc575e9b053f41e72aa36bfa6b7f55e3529ffa43161b97fa"
 
 [[package]]
+name = "base64"
+version = "0.21.0"
+source = "registry+https://github.com/rust-lang/crates.io-index"
+checksum = "a4a4ddaa51a5bc52a6948f74c06d20aaaddb71924eab79b8c97a8c556e942d6a"
+
+[[package]]
 name = "bitflags"
 version = "1.3.2"
 source = "registry+https://github.com/rust-lang/crates.io-index"
 checksum = "bef38d45163c2f1dde094a7dfd33ccf595c92905c8f8f4fdc18d06fb1037718a"
 
 [[package]]
 name = "blake2"
-version = "0.10.4"
+version = "0.10.6"
 source = "registry+https://github.com/rust-lang/crates.io-index"
-checksum = "b9cf849ee05b2ee5fba5e36f97ff8ec2533916700fc0758d40d92136a42f3388"
+checksum = "46502ad458c9a52b69d4d4d32775c788b7a1b85e8bc9d482d92250fc0e3f8efe"
 dependencies = [
  "digest",
 ]
 
 [[package]]
 name = "blake3"
-version = "1.3.1"
+version = "1.3.3"
 source = "registry+https://github.com/rust-lang/crates.io-index"
-checksum = "a08e53fc5a564bb15bfe6fae56bd71522205f1f91893f9c0116edad6496c183f"
+checksum = "42ae2468a89544a466886840aa467a25b766499f4f04bf7d9fcd10ecee9fccef"
 dependencies = [
  "arrayref",
  "arrayvec",
  "cc",
  "cfg-if",
  "constant_time_eq",
  "digest",
 ]
 
 [[package]]
 name = "block-buffer"
-version = "0.10.3"
+version = "0.10.4"
 source = "registry+https://github.com/rust-lang/crates.io-index"
-checksum = "69cce20737498f97b993470a6e536b8523f0af7892a4f928cceb1ac5e52ebe7e"
+checksum = "3078c7629b62d3f0439517fa394996acacc5cbc91c5a20d8c658e77abd503a71"
 dependencies = [
  "generic-array",
 ]
 
 [[package]]
-name = "bstr"
-version = "0.2.17"
+name = "brotli"
+version = "3.3.4"
 source = "registry+https://github.com/rust-lang/crates.io-index"
-checksum = "ba3569f383e8f1598449f1a423e72e99569137b47740b1da11ef19af3d5c3223"
+checksum = "a1a0b1dbcc8ae29329621f8d4f0d835787c1c38bb1401979b49d13b0b305ff68"
 dependencies = [
- "lazy_static",
- "memchr",
- "regex-automata",
- "serde",
+ "alloc-no-stdlib",
+ "alloc-stdlib",
+ "brotli-decompressor",
+]
+
+[[package]]
+name = "brotli-decompressor"
+version = "2.3.4"
+source = "registry+https://github.com/rust-lang/crates.io-index"
+checksum = "4b6561fd3f895a11e8f72af2cb7d22e08366bebc2b6b57f7744c4bda27034744"
+dependencies = [
+ "alloc-no-stdlib",
+ "alloc-stdlib",
 ]
 
 [[package]]
 name = "bumpalo"
-version = "3.11.1"
+version = "3.12.0"
+source = "registry+https://github.com/rust-lang/crates.io-index"
+checksum = "0d261e256854913907f67ed06efbc3338dfe6179796deefc1ff763fc1aee5535"
+
+[[package]]
+name = "byteorder"
+version = "1.4.3"
+source = "registry+https://github.com/rust-lang/crates.io-index"
+checksum = "14c189c53d098945499cdfa7ecc63567cf3886b3332b312a5b4585d8d3a6a610"
+
+[[package]]
+name = "bytes"
+version = "1.4.0"
 source = "registry+https://github.com/rust-lang/crates.io-index"
-checksum = "572f695136211188308f16ad2ca5c851a712c464060ae6974944458eb83880ba"
+checksum = "89b2fd2a0dcf38d7971e2194b6b6eebab45ae01067456a7fd93d5547a61b70be"
+
+[[package]]
+name = "bzip2"
+version = "0.4.4"
+source = "registry+https://github.com/rust-lang/crates.io-index"
+checksum = "bdb116a6ef3f6c3698828873ad02c3014b3c85cadb88496095628e3ef1e347f8"
+dependencies = [
+ "bzip2-sys",
+ "libc",
+]
+
+[[package]]
+name = "bzip2-sys"
+version = "0.1.11+1.0.8"
+source = "registry+https://github.com/rust-lang/crates.io-index"
+checksum = "736a955f3fa7875102d57c82b8cac37ec45224a07fd32d58f9f7a186b6cd4cdc"
+dependencies = [
+ "cc",
+ "libc",
+ "pkg-config",
+]
 
 [[package]]
 name = "cc"
-version = "1.0.74"
+version = "1.0.79"
 source = "registry+https://github.com/rust-lang/crates.io-index"
-checksum = "581f5dba903aac52ea3feb5ec4810848460ee833876f1f9b0fdeab1f19091574"
+checksum = "50d30906286121d95be3d479533b458f87493b30a4b5f79a607db8f5d11aa91f"
+dependencies = [
+ "jobserver",
+]
 
 [[package]]
 name = "cfg-if"
 version = "1.0.0"
 source = "registry+https://github.com/rust-lang/crates.io-index"
 checksum = "baf1de4339761588bc0619e3cbc0120ee582ebb74b53b4efbf79117bd2da40fd"
 
 [[package]]
 name = "chrono"
-version = "0.4.23"
+version = "0.4.24"
 source = "registry+https://github.com/rust-lang/crates.io-index"
-checksum = "16b0a3d9ed01224b22057780a37bb8c5dbfe1be8ba48678e7bf57ec4b385411f"
+checksum = "4e3c5919066adf22df73762e50cffcde3a758f2a848b113b586d1f86728b673b"
 dependencies = [
  "iana-time-zone",
  "num-integer",
  "num-traits",
  "winapi",
 ]
 
@@ -299,17 +451,17 @@
 dependencies = [
  "termcolor",
  "unicode-width",
 ]
 
 [[package]]
 name = "comfy-table"
-version = "6.1.2"
+version = "6.1.4"
 source = "registry+https://github.com/rust-lang/crates.io-index"
-checksum = "1090f39f45786ec6dc6286f8ea9c75d0a7ef0a0d3cda674cef0c3af7b307fbc2"
+checksum = "6e7b787b0dc42e8111badfdbe4c3059158ccb2db8780352fa1b01e8ccf45cc4d"
 dependencies = [
  "strum",
  "strum_macros",
  "unicode-width",
 ]
 
 [[package]]
@@ -332,34 +484,43 @@
  "once_cell",
  "proc-macro-hack",
  "tiny-keccak",
 ]
 
 [[package]]
 name = "constant_time_eq"
-version = "0.1.5"
+version = "0.2.5"
 source = "registry+https://github.com/rust-lang/crates.io-index"
-checksum = "245097e9a4535ee1e3e3931fcfcd55a796a44c643e8596ff6566d68f09b87bbc"
+checksum = "13418e745008f7349ec7e449155f419a61b92b58a99cc3616942b926825ec76b"
 
 [[package]]
 name = "core-foundation-sys"
 version = "0.8.3"
 source = "registry+https://github.com/rust-lang/crates.io-index"
 checksum = "5827cebf4670468b8772dd191856768aedcb1b0278a04f989f7766351917b9dc"
 
 [[package]]
 name = "cpufeatures"
-version = "0.2.5"
+version = "0.2.6"
 source = "registry+https://github.com/rust-lang/crates.io-index"
-checksum = "28d997bd5e24a5928dd43e46dc529867e207907fe0b239c3477d924f7f2ca320"
+checksum = "280a9f2d8b3a38871a3c8a46fb80db65e5e5ed97da80c4d08bf27fb63e35e181"
 dependencies = [
  "libc",
 ]
 
 [[package]]
+name = "crc32fast"
+version = "1.3.2"
+source = "registry+https://github.com/rust-lang/crates.io-index"
+checksum = "b540bd8bc810d3885c6ea91e2018302f68baba2129ab3e88f32389ee9370880d"
+dependencies = [
+ "cfg-if",
+]
+
+[[package]]
 name = "crunchy"
 version = "0.2.2"
 source = "registry+https://github.com/rust-lang/crates.io-index"
 checksum = "7a81dae078cea95a014a339291cec439d2f232ebe854a9d672b796c6afafa9b7"
 
 [[package]]
 name = "crypto-common"
@@ -369,21 +530,20 @@
 dependencies = [
  "generic-array",
  "typenum",
 ]
 
 [[package]]
 name = "csv"
-version = "1.1.6"
+version = "1.2.1"
 source = "registry+https://github.com/rust-lang/crates.io-index"
-checksum = "22813a6dc45b335f9bade10bf7271dc477e81113e89eb251a0bc2a8a81c536e1"
+checksum = "0b015497079b9a9d69c02ad25de6c0a6edef051ea6360a327d0bd05802ef64ad"
 dependencies = [
- "bstr",
  "csv-core",
- "itoa 0.4.8",
+ "itoa",
  "ryu",
  "serde",
 ]
 
 [[package]]
 name = "csv-core"
 version = "0.1.10"
@@ -391,186 +551,259 @@
 checksum = "2b2466559f260f48ad25fe6317b3c8dac77b5bdb5763ac7d9d6103530663bc90"
 dependencies = [
  "memchr",
 ]
 
 [[package]]
 name = "cxx"
-version = "1.0.80"
+version = "1.0.94"
 source = "registry+https://github.com/rust-lang/crates.io-index"
-checksum = "6b7d4e43b25d3c994662706a1d4fcfc32aaa6afd287502c111b237093bb23f3a"
+checksum = "f61f1b6389c3fe1c316bf8a4dccc90a38208354b330925bce1f74a6c4756eb93"
 dependencies = [
  "cc",
  "cxxbridge-flags",
  "cxxbridge-macro",
  "link-cplusplus",
 ]
 
 [[package]]
 name = "cxx-build"
-version = "1.0.80"
+version = "1.0.94"
 source = "registry+https://github.com/rust-lang/crates.io-index"
-checksum = "84f8829ddc213e2c1368e51a2564c552b65a8cb6a28f31e576270ac81d5e5827"
+checksum = "12cee708e8962df2aeb38f594aae5d827c022b6460ac71a7a3e2c3c2aae5a07b"
 dependencies = [
  "cc",
  "codespan-reporting",
  "once_cell",
  "proc-macro2",
  "quote",
  "scratch",
- "syn",
+ "syn 2.0.11",
 ]
 
 [[package]]
 name = "cxxbridge-flags"
-version = "1.0.80"
+version = "1.0.94"
 source = "registry+https://github.com/rust-lang/crates.io-index"
-checksum = "e72537424b474af1460806647c41d4b6d35d09ef7fe031c5c2fa5766047cc56a"
+checksum = "7944172ae7e4068c533afbb984114a56c46e9ccddda550499caa222902c7f7bb"
 
 [[package]]
 name = "cxxbridge-macro"
-version = "1.0.80"
+version = "1.0.94"
 source = "registry+https://github.com/rust-lang/crates.io-index"
-checksum = "309e4fb93eed90e1e14bea0da16b209f81813ba9fc7830c20ed151dd7bc0a4d7"
+checksum = "2345488264226bf682893e25de0769f3360aac9957980ec49361b083ddaa5bc5"
 dependencies = [
  "proc-macro2",
  "quote",
- "syn",
+ "syn 2.0.11",
+]
+
+[[package]]
+name = "dashmap"
+version = "5.4.0"
+source = "registry+https://github.com/rust-lang/crates.io-index"
+checksum = "907076dfda823b0b36d2a1bb5f90c96660a5bbcd7729e10727f07858f22c4edc"
+dependencies = [
+ "cfg-if",
+ "hashbrown 0.12.3",
+ "lock_api",
+ "once_cell",
+ "parking_lot_core",
 ]
 
 [[package]]
 name = "dask_planner"
 version = "0.1.0"
 dependencies = [
- "arrow",
  "async-trait",
+ "datafusion",
  "datafusion-common",
  "datafusion-expr",
  "datafusion-optimizer",
  "datafusion-sql",
  "env_logger",
  "log",
  "mimalloc",
  "parking_lot",
  "pyo3",
+ "pyo3-log",
+ "rand",
+ "tokio",
+ "uuid",
+]
+
+[[package]]
+name = "datafusion"
+version = "18.0.0"
+source = "registry+https://github.com/rust-lang/crates.io-index"
+checksum = "cd805bdf93d3137b37fd9966042df0c84ddfca0df5a8d32eaacb16cf6ab0d93d"
+dependencies = [
+ "ahash",
+ "arrow",
+ "async-compression",
+ "async-trait",
+ "bytes",
+ "bzip2",
+ "chrono",
+ "dashmap",
+ "datafusion-common",
+ "datafusion-expr",
+ "datafusion-optimizer",
+ "datafusion-physical-expr",
+ "datafusion-row",
+ "datafusion-sql",
+ "flate2",
+ "futures",
+ "glob",
+ "hashbrown 0.13.2",
+ "indexmap",
+ "itertools",
+ "lazy_static",
+ "log",
+ "num_cpus",
+ "object_store",
+ "parking_lot",
+ "parquet",
+ "paste",
+ "percent-encoding",
+ "pin-project-lite",
  "rand",
+ "smallvec",
+ "sqlparser",
+ "tempfile",
  "tokio",
+ "tokio-stream",
+ "tokio-util",
+ "url",
  "uuid",
+ "xz2",
 ]
 
 [[package]]
 name = "datafusion-common"
-version = "15.0.0"
+version = "18.0.0"
 source = "registry+https://github.com/rust-lang/crates.io-index"
-checksum = "7b17262b899f79afdf502846d1138a8b48441afe24dc6e07c922105289248137"
+checksum = "08c58d6714427f52f9815d19debab7adab5bac5b4d2a99d51c250e606acb6cf5"
 dependencies = [
  "arrow",
  "chrono",
+ "num_cpus",
+ "object_store",
+ "parquet",
  "sqlparser",
 ]
 
 [[package]]
 name = "datafusion-expr"
-version = "15.0.0"
+version = "18.0.0"
 source = "registry+https://github.com/rust-lang/crates.io-index"
-checksum = "533d2226b4636a1306d1f6f4ac02e436947c5d6e8bfc85f6d8f91a425c10a407"
+checksum = "2a32ee054230dd9a57d0bed587406869c4a7814d90154616aff2cb9991c1756f"
 dependencies = [
  "ahash",
  "arrow",
  "datafusion-common",
  "log",
  "sqlparser",
 ]
 
 [[package]]
 name = "datafusion-optimizer"
-version = "15.0.0"
+version = "18.0.0"
 source = "registry+https://github.com/rust-lang/crates.io-index"
-checksum = "ce7ba274267b6baf1714a67727249aa56d648c8814b0f4c43387fbe6d147e619"
+checksum = "6de4d144924de29a835feeff8313a81fdc2c7190111301508e09ea59a80edbbc"
 dependencies = [
  "arrow",
  "async-trait",
  "chrono",
  "datafusion-common",
  "datafusion-expr",
  "datafusion-physical-expr",
- "hashbrown 0.13.1",
+ "hashbrown 0.13.2",
  "log",
+ "regex-syntax",
 ]
 
 [[package]]
 name = "datafusion-physical-expr"
-version = "15.0.0"
+version = "18.0.0"
 source = "registry+https://github.com/rust-lang/crates.io-index"
-checksum = "f35cb53e6c2f9c40accdf45aef2be7fde030ea3051b1145a059d96109e65b0bf"
+checksum = "943e42356f0f6f5ac37ceacd412de9c4d7d8eba1e81b6f724f88699540c7f070"
 dependencies = [
  "ahash",
  "arrow",
  "arrow-buffer",
  "arrow-schema",
  "blake2",
  "blake3",
  "chrono",
  "datafusion-common",
  "datafusion-expr",
  "datafusion-row",
  "half",
- "hashbrown 0.13.1",
+ "hashbrown 0.13.2",
+ "indexmap",
  "itertools",
  "lazy_static",
  "md-5",
  "num-traits",
  "paste",
  "rand",
  "regex",
  "sha2",
  "unicode-segmentation",
  "uuid",
 ]
 
 [[package]]
 name = "datafusion-row"
-version = "15.0.0"
+version = "18.0.0"
 source = "registry+https://github.com/rust-lang/crates.io-index"
-checksum = "27c77b1229ae5cf6a6e0e2ba43ed4e98131dbf1cc4a97fad17c94230b32e0812"
+checksum = "6a506f5924f8af54e0806a995da0897f8c2b548d492793e045a3896d88d6714a"
 dependencies = [
  "arrow",
  "datafusion-common",
  "paste",
  "rand",
 ]
 
 [[package]]
 name = "datafusion-sql"
-version = "15.0.0"
+version = "18.0.0"
 source = "registry+https://github.com/rust-lang/crates.io-index"
-checksum = "569423fa8a50db39717080949e3b4f8763582b87baf393cc3fcf27cc21467ba7"
+checksum = "4a3d12047a5847f9667f4e2aa8fa2e7d5a6e1094b8e3546d58de492152a50dc7"
 dependencies = [
  "arrow-schema",
  "datafusion-common",
  "datafusion-expr",
+ "log",
  "sqlparser",
 ]
 
 [[package]]
 name = "digest"
-version = "0.10.5"
+version = "0.10.6"
 source = "registry+https://github.com/rust-lang/crates.io-index"
-checksum = "adfbc57365a37acbd2ebf2b64d7e69bb766e2fea813521ed536f5d0520dcf86c"
+checksum = "8168378f4e5023e7218c89c891c0fd8ecdb5e5e4f18cb78f38cf245dd021e76f"
 dependencies = [
  "block-buffer",
  "crypto-common",
  "subtle",
 ]
 
 [[package]]
+name = "doc-comment"
+version = "0.3.3"
+source = "registry+https://github.com/rust-lang/crates.io-index"
+checksum = "fea41bba32d969b513997752735605054bc0dfa92b4c56bf1189f2e174be7a10"
+
+[[package]]
 name = "either"
-version = "1.8.0"
+version = "1.8.1"
 source = "registry+https://github.com/rust-lang/crates.io-index"
-checksum = "90e5c1c8368803113bf0c9584fc495a58b86dc8a29edbf8fe877d21d9507e797"
+checksum = "7fcaabb2fef8c910e7f4c7ce9f67a1283a1715879a7c230ca9d6d1ae31f16d91"
 
 [[package]]
 name = "env_logger"
 version = "0.10.0"
 source = "registry+https://github.com/rust-lang/crates.io-index"
 checksum = "85cdab6a89accf66733ad5a1693a4dcced6aeff64602b634530dd73c1f3ee9f0"
 dependencies = [
@@ -599,189 +832,336 @@
 checksum = "aa68f1b12764fab894d2755d2518754e71b4fd80ecfb822714a1206c2aab39bf"
 dependencies = [
  "cc",
  "libc",
 ]
 
 [[package]]
+name = "fastrand"
+version = "1.9.0"
+source = "registry+https://github.com/rust-lang/crates.io-index"
+checksum = "e51093e27b0797c359783294ca4f0a911c270184cb10f85783b118614a1501be"
+dependencies = [
+ "instant",
+]
+
+[[package]]
 name = "flatbuffers"
-version = "22.9.29"
+version = "23.1.21"
 source = "registry+https://github.com/rust-lang/crates.io-index"
-checksum = "8ce016b9901aef3579617931fbb2df8fc9a9f7cb95a16eb8acc8148209bb9e70"
+checksum = "77f5399c2c9c50ae9418e522842ad362f61ee48b346ac106807bd355a8a7c619"
 dependencies = [
  "bitflags",
- "thiserror",
+ "rustc_version",
+]
+
+[[package]]
+name = "flate2"
+version = "1.0.25"
+source = "registry+https://github.com/rust-lang/crates.io-index"
+checksum = "a8a2db397cb1c8772f31494cb8917e48cd1e64f0fa7efac59fbd741a0a8ce841"
+dependencies = [
+ "crc32fast",
+ "miniz_oxide",
+]
+
+[[package]]
+name = "form_urlencoded"
+version = "1.1.0"
+source = "registry+https://github.com/rust-lang/crates.io-index"
+checksum = "a9c384f161156f5260c24a097c56119f9be8c798586aecc13afbcbe7b7e26bf8"
+dependencies = [
+ "percent-encoding",
+]
+
+[[package]]
+name = "futures"
+version = "0.3.27"
+source = "registry+https://github.com/rust-lang/crates.io-index"
+checksum = "531ac96c6ff5fd7c62263c5e3c67a603af4fcaee2e1a0ae5565ba3a11e69e549"
+dependencies = [
+ "futures-channel",
+ "futures-core",
+ "futures-executor",
+ "futures-io",
+ "futures-sink",
+ "futures-task",
+ "futures-util",
+]
+
+[[package]]
+name = "futures-channel"
+version = "0.3.27"
+source = "registry+https://github.com/rust-lang/crates.io-index"
+checksum = "164713a5a0dcc3e7b4b1ed7d3b433cabc18025386f9339346e8daf15963cf7ac"
+dependencies = [
+ "futures-core",
+ "futures-sink",
+]
+
+[[package]]
+name = "futures-core"
+version = "0.3.27"
+source = "registry+https://github.com/rust-lang/crates.io-index"
+checksum = "86d7a0c1aa76363dac491de0ee99faf6941128376f1cf96f07db7603b7de69dd"
+
+[[package]]
+name = "futures-executor"
+version = "0.3.27"
+source = "registry+https://github.com/rust-lang/crates.io-index"
+checksum = "1997dd9df74cdac935c76252744c1ed5794fac083242ea4fe77ef3ed60ba0f83"
+dependencies = [
+ "futures-core",
+ "futures-task",
+ "futures-util",
+]
+
+[[package]]
+name = "futures-io"
+version = "0.3.27"
+source = "registry+https://github.com/rust-lang/crates.io-index"
+checksum = "89d422fa3cbe3b40dca574ab087abb5bc98258ea57eea3fd6f1fa7162c778b91"
+
+[[package]]
+name = "futures-macro"
+version = "0.3.27"
+source = "registry+https://github.com/rust-lang/crates.io-index"
+checksum = "3eb14ed937631bd8b8b8977f2c198443447a8355b6e3ca599f38c975e5a963b6"
+dependencies = [
+ "proc-macro2",
+ "quote",
+ "syn 1.0.109",
+]
+
+[[package]]
+name = "futures-sink"
+version = "0.3.27"
+source = "registry+https://github.com/rust-lang/crates.io-index"
+checksum = "ec93083a4aecafb2a80a885c9de1f0ccae9dbd32c2bb54b0c3a65690e0b8d2f2"
+
+[[package]]
+name = "futures-task"
+version = "0.3.27"
+source = "registry+https://github.com/rust-lang/crates.io-index"
+checksum = "fd65540d33b37b16542a0438c12e6aeead10d4ac5d05bd3f805b8f35ab592879"
+
+[[package]]
+name = "futures-util"
+version = "0.3.27"
+source = "registry+https://github.com/rust-lang/crates.io-index"
+checksum = "3ef6b17e481503ec85211fed8f39d1970f128935ca1f814cd32ac4a6842e84ab"
+dependencies = [
+ "futures-channel",
+ "futures-core",
+ "futures-io",
+ "futures-macro",
+ "futures-sink",
+ "futures-task",
+ "memchr",
+ "pin-project-lite",
+ "pin-utils",
+ "slab",
 ]
 
 [[package]]
 name = "generic-array"
-version = "0.14.6"
+version = "0.14.7"
 source = "registry+https://github.com/rust-lang/crates.io-index"
-checksum = "bff49e947297f3312447abdca79f45f4738097cc82b06e72054d2223f601f1b9"
+checksum = "85649ca51fd72272d7821adaf274ad91c288277713d9c18820d8499a7ff69e9a"
 dependencies = [
  "typenum",
  "version_check",
 ]
 
 [[package]]
 name = "getrandom"
 version = "0.2.8"
 source = "registry+https://github.com/rust-lang/crates.io-index"
 checksum = "c05aeb6a22b8f62540c194aac980f2115af067bfe15a0734d7277a768d396b31"
 dependencies = [
  "cfg-if",
- "js-sys",
  "libc",
  "wasi",
- "wasm-bindgen",
 ]
 
 [[package]]
+name = "glob"
+version = "0.3.1"
+source = "registry+https://github.com/rust-lang/crates.io-index"
+checksum = "d2fabcfbdc87f4758337ca535fb41a6d701b65693ce38287d856d1674551ec9b"
+
+[[package]]
 name = "half"
-version = "2.1.0"
+version = "2.2.1"
 source = "registry+https://github.com/rust-lang/crates.io-index"
-checksum = "ad6a9459c9c30b177b925162351f97e7d967c7ea8bab3b8352805327daf45554"
+checksum = "02b4af3693f1b705df946e9fe5631932443781d0aabb423b62fcd4d73f6d2fd0"
 dependencies = [
  "crunchy",
  "num-traits",
 ]
 
 [[package]]
 name = "hashbrown"
 version = "0.12.3"
 source = "registry+https://github.com/rust-lang/crates.io-index"
 checksum = "8a9ee70c43aaf417c914396645a0fa852624801b24ebb7ae78fe8272889ac888"
 
 [[package]]
 name = "hashbrown"
-version = "0.13.1"
+version = "0.13.2"
 source = "registry+https://github.com/rust-lang/crates.io-index"
-checksum = "33ff8ae62cd3a9102e5637afc8452c55acf3844001bd5374e0b0bd7b6616c038"
+checksum = "43a3c133739dddd0d2990f9a4bdf8eb4b21ef50e4851ca85ab661199821d510e"
 dependencies = [
  "ahash",
 ]
 
 [[package]]
 name = "heck"
-version = "0.4.0"
+version = "0.4.1"
 source = "registry+https://github.com/rust-lang/crates.io-index"
-checksum = "2540771e65fc8cb83cd6e8a237f70c319bd5c29f78ed1084ba5d50eeac86f7f9"
+checksum = "95505c38b4572b2d910cecb0281560f54b440a19336cbbcb27bf6ce6adc6f5a8"
 
 [[package]]
 name = "hermit-abi"
-version = "0.1.19"
+version = "0.2.6"
 source = "registry+https://github.com/rust-lang/crates.io-index"
-checksum = "62b467343b94ba476dcb2500d242dadbb39557df889310ac77c5d99100aaac33"
+checksum = "ee512640fe35acbfb4bb779db6f0d80704c2cacfa2e39b601ef3e3f47d1ae4c7"
 dependencies = [
  "libc",
 ]
 
 [[package]]
 name = "hermit-abi"
-version = "0.2.6"
+version = "0.3.1"
 source = "registry+https://github.com/rust-lang/crates.io-index"
-checksum = "ee512640fe35acbfb4bb779db6f0d80704c2cacfa2e39b601ef3e3f47d1ae4c7"
-dependencies = [
- "libc",
-]
+checksum = "fed44880c466736ef9a5c5b5facefb5ed0785676d0c02d612db14e54f0d84286"
 
 [[package]]
 name = "humantime"
 version = "2.1.0"
 source = "registry+https://github.com/rust-lang/crates.io-index"
 checksum = "9a3a5bfb195931eeb336b2a7b4d761daec841b97f947d34394601737a7bba5e4"
 
 [[package]]
 name = "iana-time-zone"
-version = "0.1.53"
+version = "0.1.54"
 source = "registry+https://github.com/rust-lang/crates.io-index"
-checksum = "64c122667b287044802d6ce17ee2ddf13207ed924c712de9a66a5814d5b64765"
+checksum = "0c17cc76786e99f8d2f055c11159e7f0091c42474dcc3189fbab96072e873e6d"
 dependencies = [
  "android_system_properties",
  "core-foundation-sys",
  "iana-time-zone-haiku",
  "js-sys",
  "wasm-bindgen",
- "winapi",
+ "windows",
 ]
 
 [[package]]
 name = "iana-time-zone-haiku"
 version = "0.1.1"
 source = "registry+https://github.com/rust-lang/crates.io-index"
 checksum = "0703ae284fc167426161c2e3f1da3ea71d94b21bedbcc9494e92b28e334e3dca"
 dependencies = [
  "cxx",
  "cxx-build",
 ]
 
 [[package]]
+name = "idna"
+version = "0.3.0"
+source = "registry+https://github.com/rust-lang/crates.io-index"
+checksum = "e14ddfc70884202db2244c223200c204c2bda1bc6e0998d11b5e024d657209e6"
+dependencies = [
+ "unicode-bidi",
+ "unicode-normalization",
+]
+
+[[package]]
 name = "indexmap"
-version = "1.9.1"
+version = "1.9.3"
 source = "registry+https://github.com/rust-lang/crates.io-index"
-checksum = "10a35a97730320ffe8e2d410b5d3b69279b98d2c14bdb8b70ea89ecf7888d41e"
+checksum = "bd070e393353796e801d209ad339e89596eb4c8d430d18ede6a1cced8fafbd99"
 dependencies = [
  "autocfg",
  "hashbrown 0.12.3",
 ]
 
 [[package]]
 name = "indoc"
-version = "1.0.7"
+version = "1.0.9"
+source = "registry+https://github.com/rust-lang/crates.io-index"
+checksum = "bfa799dd5ed20a7e349f3b4639aa80d74549c81716d9ec4f994c9b5815598306"
+
+[[package]]
+name = "instant"
+version = "0.1.12"
+source = "registry+https://github.com/rust-lang/crates.io-index"
+checksum = "7a5bbe824c507c5da5956355e86a746d82e0e1464f65d862cc5e71da70e94b2c"
+dependencies = [
+ "cfg-if",
+]
+
+[[package]]
+name = "integer-encoding"
+version = "3.0.4"
 source = "registry+https://github.com/rust-lang/crates.io-index"
-checksum = "adab1eaa3408fb7f0c777a73e7465fd5656136fc93b670eb6df3c88c2c1344e3"
+checksum = "8bb03732005da905c88227371639bf1ad885cc712789c011c31c5fb3ab3ccf02"
 
 [[package]]
 name = "io-lifetimes"
-version = "1.0.1"
+version = "1.0.9"
 source = "registry+https://github.com/rust-lang/crates.io-index"
-checksum = "a7d367024b3f3414d8e01f437f704f41a9f64ab36f9067fa73e526ad4c763c87"
+checksum = "09270fd4fa1111bc614ed2246c7ef56239a3063d5be0d1ec3b589c505d400aeb"
 dependencies = [
+ "hermit-abi 0.3.1",
  "libc",
- "windows-sys",
+ "windows-sys 0.45.0",
 ]
 
 [[package]]
 name = "is-terminal"
-version = "0.4.0"
+version = "0.4.5"
 source = "registry+https://github.com/rust-lang/crates.io-index"
-checksum = "aae5bc6e2eb41c9def29a3e0f1306382807764b9b53112030eff57435667352d"
+checksum = "8687c819457e979cc940d09cb16e42a1bf70aa6b60a549de6d3a62a0ee90c69e"
 dependencies = [
- "hermit-abi 0.2.6",
+ "hermit-abi 0.3.1",
  "io-lifetimes",
  "rustix",
- "windows-sys",
+ "windows-sys 0.45.0",
 ]
 
 [[package]]
 name = "itertools"
 version = "0.10.5"
 source = "registry+https://github.com/rust-lang/crates.io-index"
 checksum = "b0fd2260e829bddf4cb6ea802289de2f86d6a7a690192fbe91b3f46e0f2c8473"
 dependencies = [
  "either",
 ]
 
 [[package]]
 name = "itoa"
-version = "0.4.8"
+version = "1.0.6"
 source = "registry+https://github.com/rust-lang/crates.io-index"
-checksum = "b71991ff56294aa922b450139ee08b3bfc70982c6b2c7562771375cf73542dd4"
+checksum = "453ad9f582a441959e5f0d088b02ce04cfe8d51a8eaf077f12ac6d3e94164ca6"
 
 [[package]]
-name = "itoa"
-version = "1.0.4"
+name = "jobserver"
+version = "0.1.26"
 source = "registry+https://github.com/rust-lang/crates.io-index"
-checksum = "4217ad341ebadf8d8e724e264f13e593e0648f5b3e94b3896a5df283be015ecc"
+checksum = "936cfd212a0155903bcbc060e316fb6cc7cbf2e1907329391ebadc1fe0ce77c2"
+dependencies = [
+ "libc",
+]
 
 [[package]]
 name = "js-sys"
-version = "0.3.60"
+version = "0.3.61"
 source = "registry+https://github.com/rust-lang/crates.io-index"
-checksum = "49409df3e3bf0856b916e2ceaca09ee28e6871cf7d9ce97a692cacfdb2a25a47"
+checksum = "445dde2150c55e483f3d8416706b97ec8e8237c307e5b7b4b8dd15e6af2a0730"
 dependencies = [
  "wasm-bindgen",
 ]
 
 [[package]]
 name = "lazy_static"
 version = "1.4.0"
@@ -850,48 +1230,48 @@
 dependencies = [
  "lexical-util",
  "static_assertions",
 ]
 
 [[package]]
 name = "libc"
-version = "0.2.137"
+version = "0.2.140"
 source = "registry+https://github.com/rust-lang/crates.io-index"
-checksum = "fc7fcc620a3bff7cdd7a365be3376c97191aeaccc2a603e600951e452615bf89"
+checksum = "99227334921fae1a979cf0bfdfcc6b3e5ce376ef57e16fb6fb3ea2ed6095f80c"
 
 [[package]]
 name = "libm"
-version = "0.2.5"
+version = "0.2.6"
 source = "registry+https://github.com/rust-lang/crates.io-index"
-checksum = "292a948cd991e376cf75541fe5b97a1081d713c618b4f1b9500f8844e49eb565"
+checksum = "348108ab3fba42ec82ff6e9564fc4ca0247bdccdc68dd8af9764bbc79c3c8ffb"
 
 [[package]]
 name = "libmimalloc-sys"
-version = "0.1.30"
+version = "0.1.32"
 source = "registry+https://github.com/rust-lang/crates.io-index"
-checksum = "dd8c7cbf8b89019683667e347572e6d55a7df7ea36b0c4ce69961b0cde67b174"
+checksum = "43a558e3d911bc3c7bfc8c78bc580b404d6e51c1cefbf656e176a94b49b0df40"
 dependencies = [
  "cc",
  "libc",
 ]
 
 [[package]]
 name = "link-cplusplus"
-version = "1.0.7"
+version = "1.0.8"
 source = "registry+https://github.com/rust-lang/crates.io-index"
-checksum = "9272ab7b96c9046fbc5bc56c06c117cb639fe2d509df0c421cad82d2915cf369"
+checksum = "ecd207c9c713c34f95a097a5b029ac2ce6010530c7b49d7fea24d977dede04f5"
 dependencies = [
  "cc",
 ]
 
 [[package]]
 name = "linux-raw-sys"
-version = "0.1.3"
+version = "0.1.4"
 source = "registry+https://github.com/rust-lang/crates.io-index"
-checksum = "8f9f08d8963a6c613f4b1a78f4f4a4dbfadf8e6545b2d72861731e4858b8b47f"
+checksum = "f051f77a7c8e6957c0696eac88f26b0117e54f52d3fc682ab19397a8812846a4"
 
 [[package]]
 name = "lock_api"
 version = "0.4.9"
 source = "registry+https://github.com/rust-lang/crates.io-index"
 checksum = "435011366fe56583b16cf956f9df0095b405b82d76425bc8981c0e22e60ec4df"
 dependencies = [
@@ -905,14 +1285,45 @@
 source = "registry+https://github.com/rust-lang/crates.io-index"
 checksum = "abb12e687cfb44aa40f41fc3978ef76448f9b6038cad6aef4259d3c095a2382e"
 dependencies = [
  "cfg-if",
 ]
 
 [[package]]
+name = "lz4"
+version = "1.24.0"
+source = "registry+https://github.com/rust-lang/crates.io-index"
+checksum = "7e9e2dd86df36ce760a60f6ff6ad526f7ba1f14ba0356f8254fb6905e6494df1"
+dependencies = [
+ "libc",
+ "lz4-sys",
+]
+
+[[package]]
+name = "lz4-sys"
+version = "1.9.4"
+source = "registry+https://github.com/rust-lang/crates.io-index"
+checksum = "57d27b317e207b10f69f5e75494119e391a96f48861ae870d1da6edac98ca900"
+dependencies = [
+ "cc",
+ "libc",
+]
+
+[[package]]
+name = "lzma-sys"
+version = "0.1.20"
+source = "registry+https://github.com/rust-lang/crates.io-index"
+checksum = "5fda04ab3764e6cde78b9974eec4f779acaba7c4e84b36eca3cf77c581b85d27"
+dependencies = [
+ "cc",
+ "libc",
+ "pkg-config",
+]
+
+[[package]]
 name = "md-5"
 version = "0.10.5"
 source = "registry+https://github.com/rust-lang/crates.io-index"
 checksum = "6365506850d44bff6e2fbcb5176cf63650e48bd45ef2fe2665ae1570e0f4b9ca"
 dependencies = [
  "digest",
 ]
@@ -930,39 +1341,28 @@
 checksum = "d61c719bcfbcf5d62b3a09efa6088de8c54bc0bfcd3ea7ae39fcc186108b8de1"
 dependencies = [
  "autocfg",
 ]
 
 [[package]]
 name = "mimalloc"
-version = "0.1.34"
+version = "0.1.36"
 source = "registry+https://github.com/rust-lang/crates.io-index"
-checksum = "9dcb174b18635f7561a0c6c9fc2ce57218ac7523cf72c50af80e2d79ab8f3ba1"
+checksum = "3d88dad3f985ec267a3fcb7a1726f5cb1a7e8cad8b646e70a84f967210df23da"
 dependencies = [
  "libmimalloc-sys",
 ]
 
 [[package]]
-name = "multiversion"
-version = "0.6.1"
+name = "miniz_oxide"
+version = "0.6.2"
 source = "registry+https://github.com/rust-lang/crates.io-index"
-checksum = "025c962a3dd3cc5e0e520aa9c612201d127dcdf28616974961a649dca64f5373"
+checksum = "b275950c28b37e794e8c55d88aeb5e139d0ce23fdbbeda68f8d7174abdf9e8fa"
 dependencies = [
- "multiversion-macros",
-]
-
-[[package]]
-name = "multiversion-macros"
-version = "0.6.1"
-source = "registry+https://github.com/rust-lang/crates.io-index"
-checksum = "a8a3e2bde382ebf960c1f3e79689fa5941625fe9bf694a1cb64af3e85faff3af"
-dependencies = [
- "proc-macro2",
- "quote",
- "syn",
+ "adler",
 ]
 
 [[package]]
 name = "num"
 version = "0.4.0"
 source = "registry+https://github.com/rust-lang/crates.io-index"
 checksum = "43db66d1170d347f9a065114077f7dccb00c1b9478c89384490a3425279a4606"
@@ -984,17 +1384,17 @@
  "autocfg",
  "num-integer",
  "num-traits",
 ]
 
 [[package]]
 name = "num-complex"
-version = "0.4.2"
+version = "0.4.3"
 source = "registry+https://github.com/rust-lang/crates.io-index"
-checksum = "7ae39348c8bc5fbd7f40c727a9925f03517afd2ab27d46702108b6a7e5414c19"
+checksum = "02e0d21255c828d6f128a1e41534206671e8c3ea0c62f32291e808dc82cff17d"
 dependencies = [
  "num-traits",
 ]
 
 [[package]]
 name = "num-integer"
 version = "0.1.45"
@@ -1036,149 +1436,240 @@
 dependencies = [
  "autocfg",
  "libm",
 ]
 
 [[package]]
 name = "num_cpus"
-version = "1.14.0"
+version = "1.15.0"
 source = "registry+https://github.com/rust-lang/crates.io-index"
-checksum = "f6058e64324c71e02bc2b150e4f3bc8286db6c83092132ffa3f6b1eab0f9def5"
+checksum = "0fac9e2da13b5eb447a6ce3d392f23a29d8694bff781bf03a16cd9ac8697593b"
 dependencies = [
- "hermit-abi 0.1.19",
+ "hermit-abi 0.2.6",
  "libc",
 ]
 
 [[package]]
+name = "object_store"
+version = "0.5.5"
+source = "registry+https://github.com/rust-lang/crates.io-index"
+checksum = "e1ea8f683b4f89a64181393742c041520a1a87e9775e6b4c0dd5a3281af05fc6"
+dependencies = [
+ "async-trait",
+ "bytes",
+ "chrono",
+ "futures",
+ "itertools",
+ "parking_lot",
+ "percent-encoding",
+ "snafu",
+ "tokio",
+ "tracing",
+ "url",
+ "walkdir",
+]
+
+[[package]]
 name = "once_cell"
-version = "1.16.0"
+version = "1.17.1"
 source = "registry+https://github.com/rust-lang/crates.io-index"
-checksum = "86f0b0d4bf799edbc74508c1e8bf170ff5f41238e5f8225603ca7caaae2b7860"
+checksum = "b7e5500299e16ebb147ae15a00a942af264cf3688f47923b8fc2cd5858f23ad3"
+
+[[package]]
+name = "ordered-float"
+version = "2.10.0"
+source = "registry+https://github.com/rust-lang/crates.io-index"
+checksum = "7940cf2ca942593318d07fcf2596cdca60a85c9e7fab408a5e21a4f9dcd40d87"
+dependencies = [
+ "num-traits",
+]
 
 [[package]]
 name = "parking_lot"
 version = "0.12.1"
 source = "registry+https://github.com/rust-lang/crates.io-index"
 checksum = "3742b2c103b9f06bc9fff0a37ff4912935851bee6d36f3c02bcc755bcfec228f"
 dependencies = [
  "lock_api",
  "parking_lot_core",
 ]
 
 [[package]]
 name = "parking_lot_core"
-version = "0.9.4"
+version = "0.9.7"
 source = "registry+https://github.com/rust-lang/crates.io-index"
-checksum = "4dc9e0dc2adc1c69d09143aff38d3d30c5c3f0df0dad82e6d25547af174ebec0"
+checksum = "9069cbb9f99e3a5083476ccb29ceb1de18b9118cafa53e90c9551235de2b9521"
 dependencies = [
  "cfg-if",
  "libc",
  "redox_syscall",
  "smallvec",
- "windows-sys",
+ "windows-sys 0.45.0",
+]
+
+[[package]]
+name = "parquet"
+version = "32.0.0"
+source = "registry+https://github.com/rust-lang/crates.io-index"
+checksum = "23b3d4917209e17e1da5fb07d276da237a42465f0def2b8d5fa5ce0e85855b4c"
+dependencies = [
+ "ahash",
+ "arrow-array",
+ "arrow-buffer",
+ "arrow-cast",
+ "arrow-data",
+ "arrow-ipc",
+ "arrow-schema",
+ "arrow-select",
+ "base64",
+ "brotli",
+ "bytes",
+ "chrono",
+ "flate2",
+ "futures",
+ "hashbrown 0.13.2",
+ "lz4",
+ "num",
+ "num-bigint",
+ "paste",
+ "seq-macro",
+ "snap",
+ "thrift",
+ "tokio",
+ "twox-hash",
+ "zstd",
 ]
 
 [[package]]
 name = "paste"
-version = "1.0.9"
+version = "1.0.12"
 source = "registry+https://github.com/rust-lang/crates.io-index"
-checksum = "b1de2e551fb905ac83f73f7aedf2f0cb4a0da7e35efa24a202a936269f1f18e1"
+checksum = "9f746c4065a8fa3fe23974dd82f15431cc8d40779821001404d10d2e79ca7d79"
+
+[[package]]
+name = "percent-encoding"
+version = "2.2.0"
+source = "registry+https://github.com/rust-lang/crates.io-index"
+checksum = "478c572c3d73181ff3c2539045f6eb99e5491218eae919370993b890cdbdd98e"
 
 [[package]]
 name = "pin-project-lite"
 version = "0.2.9"
 source = "registry+https://github.com/rust-lang/crates.io-index"
 checksum = "e0a7ae3ac2f1173085d398531c705756c94a4c56843785df85a60c1a0afac116"
 
 [[package]]
+name = "pin-utils"
+version = "0.1.0"
+source = "registry+https://github.com/rust-lang/crates.io-index"
+checksum = "8b870d8c151b6f2fb93e84a13146138f05d02ed11c7e7c54f8826aaaf7c9f184"
+
+[[package]]
+name = "pkg-config"
+version = "0.3.26"
+source = "registry+https://github.com/rust-lang/crates.io-index"
+checksum = "6ac9a59f73473f1b8d852421e59e64809f025994837ef743615c6d0c5b305160"
+
+[[package]]
 name = "ppv-lite86"
 version = "0.2.17"
 source = "registry+https://github.com/rust-lang/crates.io-index"
 checksum = "5b40af805b3121feab8a3c29f04d8ad262fa8e0561883e7653e024ae4479e6de"
 
 [[package]]
 name = "proc-macro-hack"
-version = "0.5.19"
+version = "0.5.20+deprecated"
 source = "registry+https://github.com/rust-lang/crates.io-index"
-checksum = "dbf0c48bc1d91375ae5c3cd81e3722dff1abcf81a30960240640d223f59fe0e5"
+checksum = "dc375e1527247fe1a97d8b7156678dfe7c1af2fc075c9a4db3690ecd2a148068"
 
 [[package]]
 name = "proc-macro2"
-version = "1.0.47"
+version = "1.0.54"
 source = "registry+https://github.com/rust-lang/crates.io-index"
-checksum = "5ea3d908b0e36316caf9e9e2c4625cdde190a7e6f440d794667ed17a1855e725"
+checksum = "e472a104799c74b514a57226160104aa483546de37e839ec50e3c2e41dd87534"
 dependencies = [
  "unicode-ident",
 ]
 
 [[package]]
 name = "pyo3"
-version = "0.18.0"
+version = "0.18.2"
 source = "registry+https://github.com/rust-lang/crates.io-index"
-checksum = "ccd4149c8c3975099622b4e1962dac27565cf5663b76452c3e2b66e0b6824277"
+checksum = "cfb848f80438f926a9ebddf0a539ed6065434fd7aae03a89312a9821f81b8501"
 dependencies = [
  "cfg-if",
  "indoc",
  "libc",
  "memoffset",
  "parking_lot",
  "pyo3-build-config",
  "pyo3-ffi",
  "pyo3-macros",
  "unindent",
 ]
 
 [[package]]
 name = "pyo3-build-config"
-version = "0.18.0"
+version = "0.18.2"
 source = "registry+https://github.com/rust-lang/crates.io-index"
-checksum = "9cd09fe469834db21ee60e0051030339e5d361293d8cb5ec02facf7fdcf52dbf"
+checksum = "98a42e7f42e917ce6664c832d5eee481ad514c98250c49e0b03b20593e2c7ed0"
 dependencies = [
  "once_cell",
  "target-lexicon",
 ]
 
 [[package]]
 name = "pyo3-ffi"
-version = "0.18.0"
+version = "0.18.2"
 source = "registry+https://github.com/rust-lang/crates.io-index"
-checksum = "0c427c9a96b9c5b12156dbc11f76b14f49e9aae8905ca783ea87c249044ef137"
+checksum = "a0707f0ab26826fe4ccd59b69106e9df5e12d097457c7b8f9c0fd1d2743eec4d"
 dependencies = [
  "libc",
  "pyo3-build-config",
 ]
 
 [[package]]
+name = "pyo3-log"
+version = "0.8.1"
+source = "registry+https://github.com/rust-lang/crates.io-index"
+checksum = "f9c8b57fe71fb5dcf38970ebedc2b1531cf1c14b1b9b4c560a182a57e115575c"
+dependencies = [
+ "arc-swap",
+ "log",
+ "pyo3",
+]
+
+[[package]]
 name = "pyo3-macros"
-version = "0.18.0"
+version = "0.18.2"
 source = "registry+https://github.com/rust-lang/crates.io-index"
-checksum = "16b822bbba9d60630a44d2109bc410489bb2f439b33e3a14ddeb8a40b378a7c4"
+checksum = "978d18e61465ecd389e1f235ff5a467146dc4e3c3968b90d274fe73a5dd4a438"
 dependencies = [
  "proc-macro2",
  "pyo3-macros-backend",
  "quote",
- "syn",
+ "syn 1.0.109",
 ]
 
 [[package]]
 name = "pyo3-macros-backend"
-version = "0.18.0"
+version = "0.18.2"
 source = "registry+https://github.com/rust-lang/crates.io-index"
-checksum = "84ae898104f7c99db06231160770f3e40dad6eb9021daddc0fedfa3e41dff10a"
+checksum = "8e0e1128f85ce3fca66e435e08aa2089a2689c1c48ce97803e13f63124058462"
 dependencies = [
  "proc-macro2",
  "quote",
- "syn",
+ "syn 1.0.109",
 ]
 
 [[package]]
 name = "quote"
-version = "1.0.21"
+version = "1.0.26"
 source = "registry+https://github.com/rust-lang/crates.io-index"
-checksum = "bbe448f377a7d6961e30f5955f9b8d106c3f5e449d493ee1b125c1d43c2b5179"
+checksum = "4424af4bf778aae2051a77b60283332f386554255d722233d09fbfc7e30da2fc"
 dependencies = [
  "proc-macro2",
 ]
 
 [[package]]
 name = "rand"
 version = "0.8.5"
@@ -1216,86 +1707,110 @@
 checksum = "fb5a58c1855b4b6819d59012155603f0b22ad30cad752600aadfcb695265519a"
 dependencies = [
  "bitflags",
 ]
 
 [[package]]
 name = "regex"
-version = "1.7.0"
+version = "1.7.3"
 source = "registry+https://github.com/rust-lang/crates.io-index"
-checksum = "e076559ef8e241f2ae3479e36f97bd5741c0330689e217ad51ce2c76808b868a"
+checksum = "8b1f693b24f6ac912f4893ef08244d70b6067480d2f1a46e950c9691e6749d1d"
 dependencies = [
  "aho-corasick",
  "memchr",
  "regex-syntax",
 ]
 
 [[package]]
-name = "regex-automata"
-version = "0.1.10"
+name = "regex-syntax"
+version = "0.6.29"
 source = "registry+https://github.com/rust-lang/crates.io-index"
-checksum = "6c230d73fb8d8c1b9c0b3135c5142a8acee3a0558fb8db5cf1cb65f8d7862132"
+checksum = "f162c6dd7b008981e4d40210aca20b4bd0f9b60ca9271061b07f78537722f2e1"
 
 [[package]]
-name = "regex-syntax"
-version = "0.6.28"
+name = "rustc_version"
+version = "0.4.0"
 source = "registry+https://github.com/rust-lang/crates.io-index"
-checksum = "456c603be3e8d448b072f410900c09faf164fbce2d480456f50eea6e25f9c848"
+checksum = "bfa0f585226d2e68097d4f95d113b15b83a82e819ab25717ec0590d9584ef366"
+dependencies = [
+ "semver",
+]
 
 [[package]]
 name = "rustix"
-version = "0.36.3"
+version = "0.36.11"
 source = "registry+https://github.com/rust-lang/crates.io-index"
-checksum = "0b1fbb4dfc4eb1d390c02df47760bb19a84bb80b301ecc947ab5406394d8223e"
+checksum = "db4165c9963ab29e422d6c26fbc1d37f15bace6b2810221f9d925023480fcf0e"
 dependencies = [
  "bitflags",
  "errno",
  "io-lifetimes",
  "libc",
  "linux-raw-sys",
- "windows-sys",
+ "windows-sys 0.45.0",
 ]
 
 [[package]]
 name = "rustversion"
-version = "1.0.9"
+version = "1.0.12"
 source = "registry+https://github.com/rust-lang/crates.io-index"
-checksum = "97477e48b4cf8603ad5f7aaf897467cf42ab4218a38ef76fb14c2d6773a6d6a8"
+checksum = "4f3208ce4d8448b3f3e7d168a73f5e0c43a61e32930de3bceeccedb388b6bf06"
 
 [[package]]
 name = "ryu"
-version = "1.0.11"
+version = "1.0.13"
 source = "registry+https://github.com/rust-lang/crates.io-index"
-checksum = "4501abdff3ae82a1c1b477a17252eb69cee9e66eb915c1abaa4f44d873df9f09"
+checksum = "f91339c0467de62360649f8d3e185ca8de4224ff281f66000de5eb2a77a79041"
+
+[[package]]
+name = "same-file"
+version = "1.0.6"
+source = "registry+https://github.com/rust-lang/crates.io-index"
+checksum = "93fc1dc3aaa9bfed95e02e6eadabb4baf7e3078b0bd1b4d7b6b0b68378900502"
+dependencies = [
+ "winapi-util",
+]
 
 [[package]]
 name = "scopeguard"
 version = "1.1.0"
 source = "registry+https://github.com/rust-lang/crates.io-index"
 checksum = "d29ab0c6d3fc0ee92fe66e2d99f700eab17a8d57d1c1d3b748380fb20baa78cd"
 
 [[package]]
 name = "scratch"
-version = "1.0.2"
+version = "1.0.5"
+source = "registry+https://github.com/rust-lang/crates.io-index"
+checksum = "1792db035ce95be60c3f8853017b3999209281c24e2ba5bc8e59bf97a0c590c1"
+
+[[package]]
+name = "semver"
+version = "1.0.17"
 source = "registry+https://github.com/rust-lang/crates.io-index"
-checksum = "9c8132065adcfd6e02db789d9285a0deb2f3fcb04002865ab67d5fb103533898"
+checksum = "bebd363326d05ec3e2f532ab7660680f3b02130d780c299bca73469d521bc0ed"
+
+[[package]]
+name = "seq-macro"
+version = "0.3.3"
+source = "registry+https://github.com/rust-lang/crates.io-index"
+checksum = "e6b44e8fc93a14e66336d230954dda83d18b4605ccace8fe09bc7514a71ad0bc"
 
 [[package]]
 name = "serde"
-version = "1.0.147"
+version = "1.0.159"
 source = "registry+https://github.com/rust-lang/crates.io-index"
-checksum = "d193d69bae983fc11a79df82342761dfbf28a99fc8d203dca4c3c1b590948965"
+checksum = "3c04e8343c3daeec41f58990b9d77068df31209f2af111e059e9fe9646693065"
 
 [[package]]
 name = "serde_json"
-version = "1.0.87"
+version = "1.0.95"
 source = "registry+https://github.com/rust-lang/crates.io-index"
-checksum = "6ce777b7b150d76b9cf60d28b55f5847135a003f7d7350c6be7a773508ce7d45"
+checksum = "d721eca97ac802aa7777b701877c8004d950fc142651367300d21c1cc0194744"
 dependencies = [
- "itoa 1.0.4",
+ "itoa",
  "ryu",
  "serde",
 ]
 
 [[package]]
 name = "sha2"
 version = "0.10.6"
@@ -1304,26 +1819,75 @@
 dependencies = [
  "cfg-if",
  "cpufeatures",
  "digest",
 ]
 
 [[package]]
+name = "slab"
+version = "0.4.8"
+source = "registry+https://github.com/rust-lang/crates.io-index"
+checksum = "6528351c9bc8ab22353f9d776db39a20288e8d6c37ef8cfe3317cf875eecfc2d"
+dependencies = [
+ "autocfg",
+]
+
+[[package]]
 name = "smallvec"
 version = "1.10.0"
 source = "registry+https://github.com/rust-lang/crates.io-index"
 checksum = "a507befe795404456341dfab10cef66ead4c041f62b8b11bbb92bffe5d0953e0"
 
 [[package]]
+name = "snafu"
+version = "0.7.4"
+source = "registry+https://github.com/rust-lang/crates.io-index"
+checksum = "cb0656e7e3ffb70f6c39b3c2a86332bb74aa3c679da781642590f3c1118c5045"
+dependencies = [
+ "doc-comment",
+ "snafu-derive",
+]
+
+[[package]]
+name = "snafu-derive"
+version = "0.7.4"
+source = "registry+https://github.com/rust-lang/crates.io-index"
+checksum = "475b3bbe5245c26f2d8a6f62d67c1f30eb9fffeccee721c45d162c3ebbdf81b2"
+dependencies = [
+ "heck",
+ "proc-macro2",
+ "quote",
+ "syn 1.0.109",
+]
+
+[[package]]
+name = "snap"
+version = "1.1.0"
+source = "registry+https://github.com/rust-lang/crates.io-index"
+checksum = "5e9f0ab6ef7eb7353d9119c170a436d1bf248eea575ac42d19d12f4e34130831"
+
+[[package]]
 name = "sqlparser"
-version = "0.27.0"
+version = "0.30.0"
 source = "registry+https://github.com/rust-lang/crates.io-index"
-checksum = "aba319938d4bfe250a769ac88278b629701024fe16f34257f9563bc628081970"
+checksum = "db67dc6ef36edb658196c3fef0464a80b53dbbc194a904e81f9bd4190f9ecc5b"
 dependencies = [
  "log",
+ "sqlparser_derive",
+]
+
+[[package]]
+name = "sqlparser_derive"
+version = "0.1.1"
+source = "registry+https://github.com/rust-lang/crates.io-index"
+checksum = "55fe75cb4a364c7f7ae06c7dbbc8d84bddd85d6cdf9975963c3935bc1991761e"
+dependencies = [
+ "proc-macro2",
+ "quote",
+ "syn 1.0.109",
 ]
 
 [[package]]
 name = "static_assertions"
 version = "1.1.0"
 source = "registry+https://github.com/rust-lang/crates.io-index"
 checksum = "a2eb9349b6444b326872e140eb1cf5e7c522154d69e7a0ffb0fb81c06b37543f"
@@ -1340,132 +1904,255 @@
 source = "registry+https://github.com/rust-lang/crates.io-index"
 checksum = "1e385be0d24f186b4ce2f9982191e7101bb737312ad61c1f2f984f34bcf85d59"
 dependencies = [
  "heck",
  "proc-macro2",
  "quote",
  "rustversion",
- "syn",
+ "syn 1.0.109",
 ]
 
 [[package]]
 name = "subtle"
 version = "2.4.1"
 source = "registry+https://github.com/rust-lang/crates.io-index"
 checksum = "6bdef32e8150c2a081110b42772ffe7d7c9032b606bc226c8260fd97e0976601"
 
 [[package]]
 name = "syn"
-version = "1.0.103"
+version = "1.0.109"
+source = "registry+https://github.com/rust-lang/crates.io-index"
+checksum = "72b64191b275b66ffe2469e8af2c1cfe3bafa67b529ead792a6d0160888b4237"
+dependencies = [
+ "proc-macro2",
+ "quote",
+ "unicode-ident",
+]
+
+[[package]]
+name = "syn"
+version = "2.0.11"
 source = "registry+https://github.com/rust-lang/crates.io-index"
-checksum = "a864042229133ada95abf3b54fdc62ef5ccabe9515b64717bcb9a1919e59445d"
+checksum = "21e3787bb71465627110e7d87ed4faaa36c1f61042ee67badb9e2ef173accc40"
 dependencies = [
  "proc-macro2",
  "quote",
  "unicode-ident",
 ]
 
 [[package]]
 name = "target-lexicon"
-version = "0.12.5"
+version = "0.12.6"
 source = "registry+https://github.com/rust-lang/crates.io-index"
-checksum = "9410d0f6853b1d94f0e519fb95df60f29d2c1eff2d921ffdf01a4c8a3b54f12d"
+checksum = "8ae9980cab1db3fceee2f6c6f643d5d8de2997c58ee8d25fb0cc8a9e9e7348e5"
 
 [[package]]
-name = "termcolor"
-version = "1.1.3"
+name = "tempfile"
+version = "3.4.0"
 source = "registry+https://github.com/rust-lang/crates.io-index"
-checksum = "bab24d30b911b2376f3a13cc2cd443142f0c81dda04c118693e35b3835757755"
+checksum = "af18f7ae1acd354b992402e9ec5864359d693cd8a79dcbef59f76891701c1e95"
 dependencies = [
- "winapi-util",
+ "cfg-if",
+ "fastrand",
+ "redox_syscall",
+ "rustix",
+ "windows-sys 0.42.0",
 ]
 
 [[package]]
-name = "thiserror"
-version = "1.0.37"
+name = "termcolor"
+version = "1.2.0"
 source = "registry+https://github.com/rust-lang/crates.io-index"
-checksum = "10deb33631e3c9018b9baf9dcbbc4f737320d2b576bac10f6aefa048fa407e3e"
+checksum = "be55cf8942feac5c765c2c993422806843c9a9a45d4d5c407ad6dd2ea95eb9b6"
 dependencies = [
- "thiserror-impl",
+ "winapi-util",
 ]
 
 [[package]]
-name = "thiserror-impl"
-version = "1.0.37"
+name = "thrift"
+version = "0.17.0"
 source = "registry+https://github.com/rust-lang/crates.io-index"
-checksum = "982d17546b47146b28f7c22e3d08465f6b8903d0ea13c1660d9d84a6e7adcdbb"
+checksum = "7e54bc85fc7faa8bc175c4bab5b92ba8d9a3ce893d0e9f42cc455c8ab16a9e09"
 dependencies = [
- "proc-macro2",
- "quote",
- "syn",
+ "byteorder",
+ "integer-encoding",
+ "ordered-float",
 ]
 
 [[package]]
 name = "tiny-keccak"
 version = "2.0.2"
 source = "registry+https://github.com/rust-lang/crates.io-index"
 checksum = "2c9d3793400a45f954c52e73d068316d76b6f4e36977e3fcebb13a2721e80237"
 dependencies = [
  "crunchy",
 ]
 
 [[package]]
+name = "tinyvec"
+version = "1.6.0"
+source = "registry+https://github.com/rust-lang/crates.io-index"
+checksum = "87cc5ceb3875bb20c2890005a4e226a4651264a5c75edb2421b52861a0a0cb50"
+dependencies = [
+ "tinyvec_macros",
+]
+
+[[package]]
+name = "tinyvec_macros"
+version = "0.1.1"
+source = "registry+https://github.com/rust-lang/crates.io-index"
+checksum = "1f3ccbac311fea05f86f61904b462b55fb3df8837a366dfc601a0161d0532f20"
+
+[[package]]
 name = "tokio"
-version = "1.25.0"
+version = "1.27.0"
 source = "registry+https://github.com/rust-lang/crates.io-index"
-checksum = "c8e00990ebabbe4c14c08aca901caed183ecd5c09562a12c824bb53d3c3fd3af"
+checksum = "d0de47a4eecbe11f498978a9b29d792f0d2692d1dd003650c24c76510e3bc001"
 dependencies = [
  "autocfg",
+ "bytes",
  "num_cpus",
  "parking_lot",
  "pin-project-lite",
  "tokio-macros",
- "windows-sys",
+ "windows-sys 0.45.0",
 ]
 
 [[package]]
 name = "tokio-macros"
-version = "1.8.0"
+version = "2.0.0"
+source = "registry+https://github.com/rust-lang/crates.io-index"
+checksum = "61a573bdc87985e9d6ddeed1b3d864e8a302c847e40d647746df2f1de209d1ce"
+dependencies = [
+ "proc-macro2",
+ "quote",
+ "syn 2.0.11",
+]
+
+[[package]]
+name = "tokio-stream"
+version = "0.1.12"
+source = "registry+https://github.com/rust-lang/crates.io-index"
+checksum = "8fb52b74f05dbf495a8fba459fdc331812b96aa086d9eb78101fa0d4569c3313"
+dependencies = [
+ "futures-core",
+ "pin-project-lite",
+ "tokio",
+]
+
+[[package]]
+name = "tokio-util"
+version = "0.7.7"
+source = "registry+https://github.com/rust-lang/crates.io-index"
+checksum = "5427d89453009325de0d8f342c9490009f76e999cb7672d77e46267448f7e6b2"
+dependencies = [
+ "bytes",
+ "futures-core",
+ "futures-sink",
+ "pin-project-lite",
+ "tokio",
+]
+
+[[package]]
+name = "tracing"
+version = "0.1.37"
+source = "registry+https://github.com/rust-lang/crates.io-index"
+checksum = "8ce8c33a8d48bd45d624a6e523445fd21ec13d3653cd51f681abf67418f54eb8"
+dependencies = [
+ "cfg-if",
+ "pin-project-lite",
+ "tracing-attributes",
+ "tracing-core",
+]
+
+[[package]]
+name = "tracing-attributes"
+version = "0.1.23"
 source = "registry+https://github.com/rust-lang/crates.io-index"
-checksum = "9724f9a975fb987ef7a3cd9be0350edcbe130698af5b8f7a631e23d42d052484"
+checksum = "4017f8f45139870ca7e672686113917c71c7a6e02d4924eda67186083c03081a"
 dependencies = [
  "proc-macro2",
  "quote",
- "syn",
+ "syn 1.0.109",
+]
+
+[[package]]
+name = "tracing-core"
+version = "0.1.30"
+source = "registry+https://github.com/rust-lang/crates.io-index"
+checksum = "24eb03ba0eab1fd845050058ce5e616558e8f8d8fca633e6b163fe25c797213a"
+dependencies = [
+ "once_cell",
+]
+
+[[package]]
+name = "twox-hash"
+version = "1.6.3"
+source = "registry+https://github.com/rust-lang/crates.io-index"
+checksum = "97fee6b57c6a41524a810daee9286c02d7752c4253064d0b05472833a438f675"
+dependencies = [
+ "cfg-if",
+ "static_assertions",
 ]
 
 [[package]]
 name = "typenum"
-version = "1.15.0"
+version = "1.16.0"
+source = "registry+https://github.com/rust-lang/crates.io-index"
+checksum = "497961ef93d974e23eb6f433eb5fe1b7930b659f06d12dec6fc44a8f554c0bba"
+
+[[package]]
+name = "unicode-bidi"
+version = "0.3.13"
 source = "registry+https://github.com/rust-lang/crates.io-index"
-checksum = "dcf81ac59edc17cc8697ff311e8f5ef2d99fcbd9817b34cec66f90b6c3dfd987"
+checksum = "92888ba5573ff080736b3648696b70cafad7d250551175acbaa4e0385b3e1460"
 
 [[package]]
 name = "unicode-ident"
-version = "1.0.5"
+version = "1.0.8"
 source = "registry+https://github.com/rust-lang/crates.io-index"
-checksum = "6ceab39d59e4c9499d4e5a8ee0e2735b891bb7308ac83dfb4e80cad195c9f6f3"
+checksum = "e5464a87b239f13a63a501f2701565754bae92d243d4bb7eb12f6d57d2269bf4"
+
+[[package]]
+name = "unicode-normalization"
+version = "0.1.22"
+source = "registry+https://github.com/rust-lang/crates.io-index"
+checksum = "5c5713f0fc4b5db668a2ac63cdb7bb4469d8c9fed047b1d0292cc7b0ce2ba921"
+dependencies = [
+ "tinyvec",
+]
 
 [[package]]
 name = "unicode-segmentation"
-version = "1.10.0"
+version = "1.10.1"
 source = "registry+https://github.com/rust-lang/crates.io-index"
-checksum = "0fdbf052a0783de01e944a6ce7a8cb939e295b1e7be835a1112c3b9a7f047a5a"
+checksum = "1dd624098567895118886609431a7c3b8f516e41d30e0643f03d94592a147e36"
 
 [[package]]
 name = "unicode-width"
 version = "0.1.10"
 source = "registry+https://github.com/rust-lang/crates.io-index"
 checksum = "c0edd1e5b14653f783770bce4a4dabb4a5108a5370a5f5d8cfe8710c361f6c8b"
 
 [[package]]
 name = "unindent"
-version = "0.1.10"
+version = "0.1.11"
 source = "registry+https://github.com/rust-lang/crates.io-index"
-checksum = "58ee9362deb4a96cef4d437d1ad49cffc9b9e92d202b6995674e928ce684f112"
+checksum = "e1766d682d402817b5ac4490b3c3002d91dfa0d22812f341609f97b08757359c"
+
+[[package]]
+name = "url"
+version = "2.3.1"
+source = "registry+https://github.com/rust-lang/crates.io-index"
+checksum = "0d68c799ae75762b8c3fe375feb6600ef5602c883c5d21eb51c09f22b83c4643"
+dependencies = [
+ "form_urlencoded",
+ "idna",
+ "percent-encoding",
+]
 
 [[package]]
 name = "uuid"
 version = "1.3.0"
 source = "registry+https://github.com/rust-lang/crates.io-index"
 checksum = "1674845326ee10d37ca60470760d4288a6f80f304007d92e5c53bab78c9cfd79"
 dependencies = [
@@ -1475,72 +2162,82 @@
 [[package]]
 name = "version_check"
 version = "0.9.4"
 source = "registry+https://github.com/rust-lang/crates.io-index"
 checksum = "49874b5167b65d7193b8aba1567f5c7d93d001cafc34600cee003eda787e483f"
 
 [[package]]
+name = "walkdir"
+version = "2.3.3"
+source = "registry+https://github.com/rust-lang/crates.io-index"
+checksum = "36df944cda56c7d8d8b7496af378e6b16de9284591917d307c9b4d313c44e698"
+dependencies = [
+ "same-file",
+ "winapi-util",
+]
+
+[[package]]
 name = "wasi"
 version = "0.11.0+wasi-snapshot-preview1"
 source = "registry+https://github.com/rust-lang/crates.io-index"
 checksum = "9c8d87e72b64a3b4db28d11ce29237c246188f4f51057d65a7eab63b7987e423"
 
 [[package]]
 name = "wasm-bindgen"
-version = "0.2.83"
+version = "0.2.84"
 source = "registry+https://github.com/rust-lang/crates.io-index"
-checksum = "eaf9f5aceeec8be17c128b2e93e031fb8a4d469bb9c4ae2d7dc1888b26887268"
+checksum = "31f8dcbc21f30d9b8f2ea926ecb58f6b91192c17e9d33594b3df58b2007ca53b"
 dependencies = [
  "cfg-if",
  "wasm-bindgen-macro",
 ]
 
 [[package]]
 name = "wasm-bindgen-backend"
-version = "0.2.83"
+version = "0.2.84"
 source = "registry+https://github.com/rust-lang/crates.io-index"
-checksum = "4c8ffb332579b0557b52d268b91feab8df3615f265d5270fec2a8c95b17c1142"
+checksum = "95ce90fd5bcc06af55a641a86428ee4229e44e07033963a2290a8e241607ccb9"
 dependencies = [
  "bumpalo",
  "log",
  "once_cell",
  "proc-macro2",
  "quote",
- "syn",
+ "syn 1.0.109",
  "wasm-bindgen-shared",
 ]
 
 [[package]]
 name = "wasm-bindgen-macro"
-version = "0.2.83"
+version = "0.2.84"
 source = "registry+https://github.com/rust-lang/crates.io-index"
-checksum = "052be0f94026e6cbc75cdefc9bae13fd6052cdcaf532fa6c45e7ae33a1e6c810"
+checksum = "4c21f77c0bedc37fd5dc21f897894a5ca01e7bb159884559461862ae90c0b4c5"
 dependencies = [
  "quote",
  "wasm-bindgen-macro-support",
 ]
 
 [[package]]
 name = "wasm-bindgen-macro-support"
-version = "0.2.83"
+version = "0.2.84"
 source = "registry+https://github.com/rust-lang/crates.io-index"
-checksum = "07bc0c051dc5f23e307b13285f9d75df86bfdf816c5721e573dec1f9b8aa193c"
+checksum = "2aff81306fcac3c7515ad4e177f521b5c9a15f2b08f4e32d823066102f35a5f6"
 dependencies = [
  "proc-macro2",
  "quote",
- "syn",
+ "syn 1.0.109",
  "wasm-bindgen-backend",
  "wasm-bindgen-shared",
 ]
 
 [[package]]
 name = "wasm-bindgen-shared"
-version = "0.2.83"
+version = "0.2.84"
 source = "registry+https://github.com/rust-lang/crates.io-index"
-checksum = "1c38c045535d93ec4f0b4defec448e4291638ee608530863b1e2ba115d4fff7f"
+checksum = "0046fef7e28c3804e5e38bfa31ea2a0f73905319b677e57ebe37e49358989b5d"
 
 [[package]]
 name = "winapi"
 version = "0.3.9"
 source = "registry+https://github.com/rust-lang/crates.io-index"
 checksum = "5c839a674fcd7a98952e593242ea400abe93992746761e38641405d28b00f419"
 dependencies = [
@@ -1566,14 +2263,23 @@
 [[package]]
 name = "winapi-x86_64-pc-windows-gnu"
 version = "0.4.0"
 source = "registry+https://github.com/rust-lang/crates.io-index"
 checksum = "712e227841d057c1ee1cd2fb22fa7e5a5461ae8e48fa2ca79ec42cfc1931183f"
 
 [[package]]
+name = "windows"
+version = "0.46.0"
+source = "registry+https://github.com/rust-lang/crates.io-index"
+checksum = "cdacb41e6a96a052c6cb63a144f24900236121c6f63f4f8219fef5977ecb0c25"
+dependencies = [
+ "windows-targets",
+]
+
+[[package]]
 name = "windows-sys"
 version = "0.42.0"
 source = "registry+https://github.com/rust-lang/crates.io-index"
 checksum = "5a3e1820f08b8513f676f7ab6c1f99ff312fb97b553d30ff4dd86f9f15728aa7"
 dependencies = [
  "windows_aarch64_gnullvm",
  "windows_aarch64_msvc",
@@ -1581,47 +2287,110 @@
  "windows_i686_msvc",
  "windows_x86_64_gnu",
  "windows_x86_64_gnullvm",
  "windows_x86_64_msvc",
 ]
 
 [[package]]
+name = "windows-sys"
+version = "0.45.0"
+source = "registry+https://github.com/rust-lang/crates.io-index"
+checksum = "75283be5efb2831d37ea142365f009c02ec203cd29a3ebecbc093d52315b66d0"
+dependencies = [
+ "windows-targets",
+]
+
+[[package]]
+name = "windows-targets"
+version = "0.42.2"
+source = "registry+https://github.com/rust-lang/crates.io-index"
+checksum = "8e5180c00cd44c9b1c88adb3693291f1cd93605ded80c250a75d472756b4d071"
+dependencies = [
+ "windows_aarch64_gnullvm",
+ "windows_aarch64_msvc",
+ "windows_i686_gnu",
+ "windows_i686_msvc",
+ "windows_x86_64_gnu",
+ "windows_x86_64_gnullvm",
+ "windows_x86_64_msvc",
+]
+
+[[package]]
 name = "windows_aarch64_gnullvm"
-version = "0.42.0"
+version = "0.42.2"
 source = "registry+https://github.com/rust-lang/crates.io-index"
-checksum = "41d2aa71f6f0cbe00ae5167d90ef3cfe66527d6f613ca78ac8024c3ccab9a19e"
+checksum = "597a5118570b68bc08d8d59125332c54f1ba9d9adeedeef5b99b02ba2b0698f8"
 
 [[package]]
 name = "windows_aarch64_msvc"
-version = "0.42.0"
+version = "0.42.2"
 source = "registry+https://github.com/rust-lang/crates.io-index"
-checksum = "dd0f252f5a35cac83d6311b2e795981f5ee6e67eb1f9a7f64eb4500fbc4dcdb4"
+checksum = "e08e8864a60f06ef0d0ff4ba04124db8b0fb3be5776a5cd47641e942e58c4d43"
 
 [[package]]
 name = "windows_i686_gnu"
-version = "0.42.0"
+version = "0.42.2"
 source = "registry+https://github.com/rust-lang/crates.io-index"
-checksum = "fbeae19f6716841636c28d695375df17562ca208b2b7d0dc47635a50ae6c5de7"
+checksum = "c61d927d8da41da96a81f029489353e68739737d3beca43145c8afec9a31a84f"
 
 [[package]]
 name = "windows_i686_msvc"
-version = "0.42.0"
+version = "0.42.2"
 source = "registry+https://github.com/rust-lang/crates.io-index"
-checksum = "84c12f65daa39dd2babe6e442988fc329d6243fdce47d7d2d155b8d874862246"
+checksum = "44d840b6ec649f480a41c8d80f9c65108b92d89345dd94027bfe06ac444d1060"
 
 [[package]]
 name = "windows_x86_64_gnu"
-version = "0.42.0"
+version = "0.42.2"
 source = "registry+https://github.com/rust-lang/crates.io-index"
-checksum = "bf7b1b21b5362cbc318f686150e5bcea75ecedc74dd157d874d754a2ca44b0ed"
+checksum = "8de912b8b8feb55c064867cf047dda097f92d51efad5b491dfb98f6bbb70cb36"
 
 [[package]]
 name = "windows_x86_64_gnullvm"
-version = "0.42.0"
+version = "0.42.2"
 source = "registry+https://github.com/rust-lang/crates.io-index"
-checksum = "09d525d2ba30eeb3297665bd434a54297e4170c7f1a44cad4ef58095b4cd2028"
+checksum = "26d41b46a36d453748aedef1486d5c7a85db22e56aff34643984ea85514e94a3"
 
 [[package]]
 name = "windows_x86_64_msvc"
-version = "0.42.0"
+version = "0.42.2"
+source = "registry+https://github.com/rust-lang/crates.io-index"
+checksum = "9aec5da331524158c6d1a4ac0ab1541149c0b9505fde06423b02f5ef0106b9f0"
+
+[[package]]
+name = "xz2"
+version = "0.1.7"
+source = "registry+https://github.com/rust-lang/crates.io-index"
+checksum = "388c44dc09d76f1536602ead6d325eb532f5c122f17782bd57fb47baeeb767e2"
+dependencies = [
+ "lzma-sys",
+]
+
+[[package]]
+name = "zstd"
+version = "0.12.3+zstd.1.5.2"
 source = "registry+https://github.com/rust-lang/crates.io-index"
-checksum = "f40009d85759725a34da6d89a94e63d7bdc50a862acf0dbc7c8e488f1edcb6f5"
+checksum = "76eea132fb024e0e13fd9c2f5d5d595d8a967aa72382ac2f9d39fcc95afd0806"
+dependencies = [
+ "zstd-safe",
+]
+
+[[package]]
+name = "zstd-safe"
+version = "6.0.4+zstd.1.5.4"
+source = "registry+https://github.com/rust-lang/crates.io-index"
+checksum = "7afb4b54b8910cf5447638cb54bf4e8a65cbedd783af98b98c62ffe91f185543"
+dependencies = [
+ "libc",
+ "zstd-sys",
+]
+
+[[package]]
+name = "zstd-sys"
+version = "2.0.7+zstd.1.5.4"
+source = "registry+https://github.com/rust-lang/crates.io-index"
+checksum = "94509c3ba2fe55294d752b79842c530ccfab760192521df74a081a78d2b3c7f5"
+dependencies = [
+ "cc",
+ "libc",
+ "pkg-config",
+]
```

### Comparing `dask_sql-2023.2.0/dask_planner/Cargo.toml` & `dask_sql-2023.4.0/dask_planner/Cargo.toml`

 * *Files 8% similar despite different names*

```diff
@@ -5,24 +5,25 @@
 description = "Bindings for DataFusion used by Dask-SQL"
 readme = "README.md"
 license = "Apache-2.0"
 edition = "2021"
 rust-version = "1.62"
 
 [dependencies]
-arrow = { version = "28.0.0", features = ["prettyprint"] }
-async-trait = "0.1.64"
-datafusion-common = "15.0.0"
-datafusion-expr = "15.0.0"
-datafusion-optimizer = "15.0.0"
-datafusion-sql = "15.0.0"
+async-trait = "0.1.68"
+datafusion = "18.0.0"
+datafusion-common = "18.0.0"
+datafusion-expr = "18.0.0"
+datafusion-optimizer = "18.0.0"
+datafusion-sql = "18.0.0"
 env_logger = "0.10"
 log = "^0.4"
 mimalloc = { version = "*", default-features = false }
 parking_lot = "0.12"
-pyo3 = { version = "0.18.0", features = ["extension-module", "abi3", "abi3-py38"] }
+pyo3 = { version = "0.18.2", features = ["extension-module", "abi3", "abi3-py38"] }
+pyo3-log = "0.8.1"
 rand = "0.8"
-tokio = { version = "1.25", features = ["macros", "rt", "rt-multi-thread", "sync", "fs", "parking_lot"] }
+tokio = { version = "1.27", features = ["macros", "rt", "rt-multi-thread", "sync", "fs", "parking_lot"] }
 uuid = { version = "1.3", features = ["v4"] }
 
 [lib]
 crate-type = ["cdylib"]
```

### Comparing `dask_sql-2023.2.0/dask_planner/src/dialect.rs` & `dask_sql-2023.4.0/dask_planner/src/dialect.rs`

 * *Files 9% similar despite different names*

```diff
@@ -12,21 +12,21 @@
 pub struct DaskDialect {}
 
 impl Dialect for DaskDialect {
     fn is_identifier_start(&self, ch: char) -> bool {
         // See https://www.postgresql.org/docs/11/sql-syntax-lexical.html#SQL-SYNTAX-IDENTIFIERS
         // We don't yet support identifiers beginning with "letters with
         // diacritical marks and non-Latin letters"
-        ('a'..='z').contains(&ch) || ('A'..='Z').contains(&ch) || ch == '_'
+        ch.is_ascii_lowercase() || ch.is_ascii_uppercase() || ch == '_'
     }
 
     fn is_identifier_part(&self, ch: char) -> bool {
-        ('a'..='z').contains(&ch)
-            || ('A'..='Z').contains(&ch)
-            || ('0'..='9').contains(&ch)
+        ch.is_ascii_lowercase()
+            || ch.is_ascii_uppercase()
+            || ch.is_ascii_digit()
             || ch == '$'
             || ch == '_'
     }
 
     /// Determine if a character starts a quoted identifier. The default
     /// implementation, accepting "double quoted" ids is both ANSI-compliant
     /// and appropriate for most dialects (with the notable exception of
@@ -43,15 +43,15 @@
     fn supports_filter_during_aggregation(&self) -> bool {
         true
     }
 
     /// override expression parsing
     fn parse_prefix(&self, parser: &mut Parser) -> Option<Result<Expr, ParserError>> {
         fn parse_expr(parser: &mut Parser) -> Result<Option<Expr>, ParserError> {
-            match parser.peek_token() {
+            match parser.peek_token().token {
                 Token::Word(w) if w.value.to_lowercase() == "ceil" => {
                     // CEIL(d TO DAY)
                     parser.next_token(); // skip ceil
                     parser.expect_token(&Token::LParen)?;
                     let expr = parser.parse_expr()?;
                     if !parser.parse_keyword(Keyword::TO) {
                         // Parse CEIL(expr) as normal
```

### Comparing `dask_sql-2023.2.0/dask_planner/src/error.rs` & `dask_sql-2023.4.0/dask_planner/src/error.rs`

 * *Files identical despite different names*

### Comparing `dask_sql-2023.2.0/dask_planner/src/expression.rs` & `dask_sql-2023.4.0/dask_planner/src/expression.rs`

 * *Files 3% similar despite different names*

```diff
@@ -1,13 +1,13 @@
 use std::{convert::From, sync::Arc};
 
-use arrow::datatypes::DataType;
+use datafusion::arrow::datatypes::DataType;
 use datafusion_common::{Column, DFField, DFSchema, ScalarValue};
 use datafusion_expr::{
-    expr::{BinaryExpr, Cast},
+    expr::{AggregateFunction, BinaryExpr, Cast, Sort, TryCast, WindowFunction},
     lit,
     utils::exprlist_to_fields,
     Between,
     BuiltinScalarFunction,
     Case,
     Expr,
     GetIndexedField,
@@ -83,18 +83,18 @@
     pub fn _column_name(&self, plan: &LogicalPlan) -> Result<String> {
         let field = expr_to_field(&self.expr, plan)?;
         Ok(field.qualified_column().flat_name())
     }
 
     fn _rex_type(&self, expr: &Expr) -> RexType {
         match expr {
-            Expr::Alias(..)
-            | Expr::Column(..)
-            | Expr::QualifiedWildcard { .. }
-            | Expr::GetIndexedField { .. } => RexType::Reference,
+            Expr::Alias(..) => RexType::Alias,
+            Expr::Column(..) | Expr::QualifiedWildcard { .. } | Expr::GetIndexedField { .. } => {
+                RexType::Reference
+            }
             Expr::ScalarVariable(..) | Expr::Literal(..) => RexType::Literal,
             Expr::BinaryExpr { .. }
             | Expr::Not(..)
             | Expr::IsNotNull(..)
             | Expr::Negative(..)
             | Expr::IsNull(..)
             | Expr::Like { .. }
@@ -116,16 +116,17 @@
             | Expr::InSubquery { .. }
             | Expr::GroupingSet(..)
             | Expr::IsTrue(..)
             | Expr::IsFalse(..)
             | Expr::IsUnknown(_)
             | Expr::IsNotTrue(..)
             | Expr::IsNotFalse(..)
+            | Expr::Placeholder { .. }
             | Expr::IsNotUnknown(_) => RexType::Call,
-            Expr::ScalarSubquery(..) => RexType::SubqueryAlias,
+            Expr::ScalarSubquery(..) => RexType::ScalarSubquery,
         }
     }
 }
 
 macro_rules! extract_scalar_value {
     ($self: expr, $variant: ident) => {
         match $self.get_scalar_value()? {
@@ -176,16 +177,27 @@
             Some(input_plans) if !input_plans.is_empty() => {
                 let mut schema: DFSchema = (**input_plans[0].schema()).clone();
                 for plan in input_plans.iter().skip(1) {
                     schema.merge(plan.schema().as_ref());
                 }
                 let name = get_expr_name(&self.expr).map_err(py_runtime_err)?;
                 schema
-                    .index_of_column(&Column::from_qualified_name(&name))
-                    .map_err(py_runtime_err)
+                    .index_of_column(&Column::from_qualified_name(name.clone()))
+                    .or_else(|_| {
+                        // Handles cases when from_qualified_name doesn't format the Column correctly.
+                        // Here, we split the name string and grab the relation/table names
+                        let split_name: Vec<&str> = name.split('.').collect();
+                        let relation = &split_name.first();
+                        let table = &split_name.get(1);
+                        let col = Column {
+                            relation: Some(relation.unwrap().to_string()),
+                            name: table.unwrap().to_string(),
+                        };
+                        schema.index_of_column(&col).map_err(py_runtime_err)
+                    })
             }
             _ => Err(py_runtime_err(
                 "We need a valid LogicalPlan instance to get the Expr's index in the schema",
             )),
         }
     }
 
@@ -227,14 +239,15 @@
             | Expr::Like { .. }
             | Expr::ILike { .. }
             | Expr::SimilarTo { .. }
             | Expr::IsNotUnknown(_)
             | Expr::Case { .. }
             | Expr::TryCast { .. }
             | Expr::WindowFunction { .. }
+            | Expr::Placeholder { .. }
             | Expr::Wildcard => {
                 return Err(py_type_err(format!(
                     "Encountered unsupported expression type: {}",
                     &self.expr.variant_name()
                 )))
             }
         }))
@@ -277,26 +290,26 @@
             | Expr::IsUnknown(expr)
             | Expr::IsNotTrue(expr)
             | Expr::IsNotFalse(expr)
             | Expr::IsNotUnknown(expr)
             | Expr::Negative(expr)
             | Expr::GetIndexedField(GetIndexedField { expr, .. })
             | Expr::Cast(Cast { expr, .. })
-            | Expr::TryCast { expr, .. }
-            | Expr::Sort { expr, .. }
+            | Expr::TryCast(TryCast { expr, .. })
+            | Expr::Sort(Sort { expr, .. })
             | Expr::InSubquery { expr, .. } => {
                 Ok(vec![PyExpr::from(*expr.clone(), self.input_plan.clone())])
             }
 
             // Expr variants containing a collection of Expr(s) for operands
-            Expr::AggregateFunction { args, .. }
+            Expr::AggregateFunction(AggregateFunction { args, .. })
             | Expr::AggregateUDF { args, .. }
             | Expr::ScalarFunction { args, .. }
             | Expr::ScalarUDF { args, .. }
-            | Expr::WindowFunction { args, .. } => Ok(args
+            | Expr::WindowFunction(WindowFunction { args, .. }) => Ok(args
                 .iter()
                 .map(|arg| PyExpr::from(arg.clone(), self.input_plan.clone()))
                 .collect()),
 
             // Expr(s) that require more specific processing
             Expr::Case(Case {
                 expr,
@@ -357,14 +370,15 @@
             ]),
 
             // Currently un-support/implemented Expr types for Rex Call operations
             Expr::GroupingSet(..)
             | Expr::Wildcard
             | Expr::QualifiedWildcard { .. }
             | Expr::ScalarSubquery(..)
+            | Expr::Placeholder { .. }
             | Expr::Exists { .. } => Err(py_runtime_err(format!(
                 "Unimplemented Expr type: {}",
                 self.expr
             ))),
         }
     }
 
@@ -435,16 +449,14 @@
                 | Operator::NotEq
                 | Operator::Lt
                 | Operator::LtEq
                 | Operator::Gt
                 | Operator::GtEq
                 | Operator::And
                 | Operator::Or
-                | Operator::Like
-                | Operator::NotLike
                 | Operator::IsDistinctFrom
                 | Operator::IsNotDistinctFrom
                 | Operator::RegexMatch
                 | Operator::RegexIMatch
                 | Operator::RegexNotMatch
                 | Operator::RegexNotIMatch => "BOOLEAN",
                 Operator::Plus | Operator::Minus | Operator::Multiply | Operator::Modulo => {
@@ -554,34 +566,30 @@
     }
 
     #[pyo3(name = "getFilterExpr")]
     pub fn get_filter_expr(&self) -> PyResult<Option<PyExpr>> {
         // TODO refactor to avoid duplication
         match &self.expr {
             Expr::Alias(expr, _) => match expr.as_ref() {
-                Expr::AggregateFunction { filter, .. } | Expr::AggregateUDF { filter, .. } => {
-                    match filter {
-                        Some(filter) => {
-                            Ok(Some(PyExpr::from(*filter.clone(), self.input_plan.clone())))
-                        }
-                        None => Ok(None),
+                Expr::AggregateFunction(AggregateFunction { filter, .. })
+                | Expr::AggregateUDF { filter, .. } => match filter {
+                    Some(filter) => {
+                        Ok(Some(PyExpr::from(*filter.clone(), self.input_plan.clone())))
                     }
-                }
+                    None => Ok(None),
+                },
                 _ => Err(py_type_err(
                     "getFilterExpr() - Non-aggregate expression encountered",
                 )),
             },
-            Expr::AggregateFunction { filter, .. } | Expr::AggregateUDF { filter, .. } => {
-                match filter {
-                    Some(filter) => {
-                        Ok(Some(PyExpr::from(*filter.clone(), self.input_plan.clone())))
-                    }
-                    None => Ok(None),
-                }
-            }
+            Expr::AggregateFunction(AggregateFunction { filter, .. })
+            | Expr::AggregateUDF { filter, .. } => match filter {
+                Some(filter) => Ok(Some(PyExpr::from(*filter.clone(), self.input_plan.clone()))),
+                None => Ok(None),
+            },
             _ => Err(py_type_err(
                 "getFilterExpr() - Non-aggregate expression encountered",
             )),
         }
     }
 
     #[pyo3(name = "getFloat32Value")]
@@ -709,18 +717,18 @@
         }
     }
 
     #[pyo3(name = "isDistinctAgg")]
     pub fn is_distinct_aggregation(&self) -> PyResult<bool> {
         // TODO refactor to avoid duplication
         match &self.expr {
-            Expr::AggregateFunction { distinct, .. } => Ok(*distinct),
+            Expr::AggregateFunction(funct) => Ok(funct.distinct),
             Expr::AggregateUDF { .. } => Ok(false),
             Expr::Alias(expr, _) => match expr.as_ref() {
-                Expr::AggregateFunction { distinct, .. } => Ok(*distinct),
+                Expr::AggregateFunction(funct) => Ok(funct.distinct),
                 Expr::AggregateUDF { .. } => Ok(false),
                 _ => Err(py_type_err(
                     "isDistinctAgg() - Non-aggregate expression encountered",
                 )),
             },
             _ => Err(py_type_err(
                 "getFilterExpr() - Non-aggregate expression encountered",
@@ -728,27 +736,27 @@
         }
     }
 
     /// Returns if a sort expressions is an ascending sort
     #[pyo3(name = "isSortAscending")]
     pub fn is_sort_ascending(&self) -> PyResult<bool> {
         match &self.expr {
-            Expr::Sort { asc, .. } => Ok(*asc),
+            Expr::Sort(Sort { asc, .. }) => Ok(*asc),
             _ => Err(py_type_err(format!(
                 "Provided Expr {:?} is not a sort type",
                 &self.expr
             ))),
         }
     }
 
     /// Returns if nulls should be placed first in a sort expression
     #[pyo3(name = "isSortNullsFirst")]
     pub fn is_sort_nulls_first(&self) -> PyResult<bool> {
         match &self.expr {
-            Expr::Sort { nulls_first, .. } => Ok(*nulls_first),
+            Expr::Sort(Sort { nulls_first, .. }) => Ok(*nulls_first),
             _ => Err(py_type_err(format!(
                 "Provided Expr {:?} is not a sort type",
                 &self.expr
             ))),
         }
     }
 
@@ -790,15 +798,15 @@
         _ => Ok(expr.canonical_name()),
     }
 }
 
 /// Create a [DFField] representing an [Expr], given an input [LogicalPlan] to resolve against
 pub fn expr_to_field(expr: &Expr, input_plan: &LogicalPlan) -> Result<DFField> {
     match expr {
-        Expr::Sort { expr, .. } => {
+        Expr::Sort(Sort { expr, .. }) => {
             // DataFusion does not support create_name for sort expressions (since they never
             // appear in projections) so we just delegate to the contained expression instead
             expr_to_field(expr, input_plan)
         }
         _ => {
             let fields =
                 exprlist_to_fields(&[expr.clone()], input_plan).map_err(DaskPlannerError::from)?;
```

### Comparing `dask_sql-2023.2.0/dask_planner/src/lib.rs` & `dask_sql-2023.4.0/dask_planner/src/lib.rs`

 * *Files 12% similar despite different names*

```diff
@@ -1,7 +1,8 @@
+use log::debug;
 use mimalloc::MiMalloc;
 use pyo3::prelude::*;
 
 mod dialect;
 mod error;
 mod expression;
 mod parser;
@@ -13,14 +14,17 @@
 /// Low-level DataFusion internal package.
 ///
 /// The higher-level public API is defined in pure python files under the
 /// dask_planner directory.
 #[pymodule]
 #[pyo3(name = "rust")]
 fn rust(py: Python, m: &PyModule) -> PyResult<()> {
+    // Initialize the global Python logger instance
+    pyo3_log::init();
+
     // Register the python classes
     m.add_class::<expression::PyExpr>()?;
     m.add_class::<sql::DaskSQLContext>()?;
     m.add_class::<sql::types::SqlTypeName>()?;
     m.add_class::<sql::types::RexType>()?;
     m.add_class::<sql::types::DaskTypeMap>()?;
     m.add_class::<sql::types::rel_data_type::RelDataType>()?;
@@ -37,9 +41,11 @@
         py.get_type::<sql::exceptions::ParsingException>(),
     )?;
     m.add(
         "DFOptimizationException",
         py.get_type::<sql::exceptions::OptimizationException>(),
     )?;
 
+    debug!("dask_planner Python module loaded");
+
     Ok(())
 }
```

### Comparing `dask_sql-2023.2.0/dask_planner/src/parser.rs` & `dask_sql-2023.4.0/dask_planner/src/parser.rs`

 * *Files 1% similar despite different names*

```diff
@@ -4,15 +4,15 @@
 
 use std::collections::VecDeque;
 
 use datafusion_sql::sqlparser::{
     ast::{Expr, Ident, SelectItem, Statement as SQLStatement, UnaryOperator, Value},
     dialect::{keywords::Keyword, Dialect},
     parser::{Parser, ParserError},
-    tokenizer::{Token, Tokenizer},
+    tokenizer::{Token, TokenWithLocation, Tokenizer},
 };
 use pyo3::prelude::*;
 
 use crate::{
     dialect::DaskDialect,
     sql::{exceptions::py_type_err, parser_utils::DaskParserUtils, types::SqlTypeName},
 };
@@ -255,22 +255,25 @@
     pub schema_name: Option<String>,
     pub model_name: String,
 }
 
 /// Dask-SQL extension DDL for `SHOW SCHEMAS`
 #[derive(Debug, Clone, PartialEq, Eq)]
 pub struct ShowSchemas {
-    /// like
+    /// optional catalog name
+    pub catalog_name: Option<String>,
+    /// optional LIKE identifier
     pub like: Option<String>,
 }
 
 /// Dask-SQL extension DDL for `SHOW TABLES FROM`
 #[derive(Debug, Clone, PartialEq, Eq)]
 pub struct ShowTables {
-    /// schema name
+    /// catalog and schema name, i.e. 'catalog_name.schema_name'
+    pub catalog_name: Option<String>,
     pub schema_name: Option<String>,
 }
 
 /// Dask-SQL extension DDL for `SHOW COLUMNS FROM`
 #[derive(Debug, Clone, PartialEq, Eq)]
 pub struct ShowColumns {
     /// schema and table name, i.e. 'schema_name.table_name'
@@ -384,15 +387,15 @@
 
     /// Parse the specified tokens with dialect
     pub fn new_with_dialect(sql: &str, dialect: &'a dyn Dialect) -> Result<Self, ParserError> {
         let mut tokenizer = Tokenizer::new(dialect, sql);
         let tokens = tokenizer.tokenize()?;
 
         Ok(DaskParser {
-            parser: Parser::new(tokens, dialect),
+            parser: Parser::new(dialect).with_tokens(tokens),
         })
     }
 
     #[allow(dead_code)]
     /// Parse a SQL statement and produce a set of statements with dialect
     pub fn parse_sql(sql: &str) -> Result<VecDeque<DaskStatement>, ParserError> {
         let dialect = &DaskDialect {};
@@ -424,21 +427,24 @@
             stmts.push_back(statement);
             expecting_statement_delimiter = true;
         }
         Ok(stmts)
     }
 
     /// Report unexpected token
-    fn expected<T>(&self, expected: &str, found: Token) -> Result<T, ParserError> {
-        parser_err!(format!("Expected {expected}, found: {found}"))
+    fn expected<T>(&self, expected: &str, found: TokenWithLocation) -> Result<T, ParserError> {
+        parser_err!(format!(
+            "Expected {}, found: {} at line {} column {}",
+            expected, found.token, found.location.line, found.location.column
+        ))
     }
 
     /// Parse a new expression
     pub fn parse_statement(&mut self) -> Result<DaskStatement, ParserError> {
-        match self.parser.peek_token() {
+        match self.parser.peek_token().token {
             Token::Word(w) => {
                 match w.keyword {
                     Keyword::CREATE => {
                         // move one token forward
                         self.parser.next_token();
                         // use custom parsing
                         self.parse_create()
@@ -449,15 +455,15 @@
                         // use custom parsing
                         self.parse_drop()
                     }
                     Keyword::SELECT => {
                         // Check for PREDICT token in statement
                         let mut cnt = 1;
                         loop {
-                            match self.parser.next_token() {
+                            match self.parser.next_token().token {
                                 Token::Word(w) => {
                                     match w.value.to_lowercase().as_str() {
                                         "predict" => {
                                             return self.parse_predict_model();
                                         }
                                         _ => {
                                             // Keep looking for PREDICT
@@ -541,15 +547,15 @@
             }
         }
     }
 
     /// Parse a SQL CREATE statement
     pub fn parse_create(&mut self) -> Result<DaskStatement, ParserError> {
         let or_replace = self.parser.parse_keywords(&[Keyword::OR, Keyword::REPLACE]);
-        match self.parser.peek_token() {
+        match self.parser.peek_token().token {
             Token::Word(w) => {
                 match w.value.to_lowercase().as_str() {
                     "model" => {
                         // move one token forward
                         self.parser.next_token();
 
                         let if_not_exists = self.parser.parse_keywords(&[
@@ -625,15 +631,15 @@
                 )))
             }
         }
     }
 
     /// Parse a SQL DROP statement
     pub fn parse_drop(&mut self) -> Result<DaskStatement, ParserError> {
-        match self.parser.peek_token() {
+        match self.parser.peek_token().token {
             Token::Word(w) => {
                 match w.value.to_lowercase().as_str() {
                     "model" => {
                         // move one token forward
                         self.parser.next_token();
                         // use custom parsing
                         self.parse_drop_model()
@@ -668,30 +674,30 @@
                 )))
             }
         }
     }
 
     /// Parse a SQL SHOW statement
     pub fn parse_show(&mut self) -> Result<DaskStatement, ParserError> {
-        match self.parser.peek_token() {
+        match self.parser.peek_token().token {
             Token::Word(w) => {
                 match w.value.to_lowercase().as_str() {
                     "schemas" => {
                         // move one token forward
                         self.parser.next_token();
                         // use custom parsing
                         self.parse_show_schemas()
                     }
                     "tables" => {
                         // move one token forward
                         self.parser.next_token();
 
                         // If non ansi ... `FROM {schema_name}` is present custom parse
                         // otherwise use sqlparser-rs
-                        match self.parser.peek_token() {
+                        match self.parser.peek_token().token {
                             Token::Word(w) => {
                                 match w.value.to_lowercase().as_str() {
                                     "from" => {
                                         // move one token forward
                                         self.parser.next_token();
                                         // use custom parsing
                                         self.parse_show_tables()
@@ -733,15 +739,15 @@
                 )))
             }
         }
     }
 
     /// Parse a SQL DESCRIBE statement
     pub fn parse_describe(&mut self) -> Result<DaskStatement, ParserError> {
-        match self.parser.peek_token() {
+        match self.parser.peek_token().token {
             Token::Word(w) => {
                 match w.value.to_lowercase().as_str() {
                     "model" => {
                         self.parser.next_token();
                         // use custom parsing
                         self.parse_describe_model()
                     }
@@ -760,15 +766,15 @@
                 )))
             }
         }
     }
 
     /// Parse a SQL USE SCHEMA statement
     pub fn parse_use(&mut self) -> Result<DaskStatement, ParserError> {
-        match self.parser.peek_token() {
+        match self.parser.peek_token().token {
             Token::Word(w) => {
                 match w.value.to_lowercase().as_str() {
                     "schema" => {
                         // move one token forward
                         self.parser.next_token();
                         // use custom parsing
                         let schema_name = self.parser.parse_identifier()?;
@@ -787,15 +793,15 @@
                 self.parser.parse_show()?,
             ))),
         }
     }
 
     /// Parse a SQL ANALYZE statement
     pub fn parse_analyze(&mut self) -> Result<DaskStatement, ParserError> {
-        match self.parser.peek_token() {
+        match self.parser.peek_token().token {
             Token::Word(w) => {
                 match w.value.to_lowercase().as_str() {
                     "table" => {
                         // move one token forward
                         self.parser.next_token();
                         // use custom parsing
                         self.parse_analyze_table()
@@ -815,15 +821,15 @@
                 )))
             }
         }
     }
 
     /// Parse a SQL ALTER statement
     pub fn parse_alter(&mut self) -> Result<DaskStatement, ParserError> {
-        match self.parser.peek_token() {
+        match self.parser.peek_token().token {
             Token::Word(w) => {
                 match w.keyword {
                     Keyword::TABLE => {
                         self.parser.next_token();
                         self.parse_alter_table()
                     }
                     Keyword::SCHEMA => {
@@ -851,15 +857,15 @@
     pub fn parse_predict_model(&mut self) -> Result<DaskStatement, ParserError> {
         // PREDICT(
         //     MODEL model_name,
         //     SQLStatement
         // )
         self.parser.expect_token(&Token::LParen)?;
 
-        let is_model = match self.parser.next_token() {
+        let is_model = match self.parser.next_token().token {
             Token::Word(w) => matches!(w.value.to_lowercase().as_str(), "model"),
             _ => false,
         };
         if !is_model {
             return Err(ParserError::ParserError(
                 "parse_predict_model: Expected `MODEL`".to_string(),
             ));
@@ -950,15 +956,15 @@
         }
         Ok(values)
     }
 
     fn parse_key_value_pair(&mut self) -> Result<(String, PySqlArg), ParserError> {
         let key = self.parser.parse_identifier()?;
         self.parser.expect_token(&Token::Eq)?;
-        match self.parser.next_token() {
+        match self.parser.next_token().token {
             Token::LParen => {
                 let key_value_pairs =
                     self.parse_comma_separated(DaskParser::parse_key_value_pair)?;
                 self.parser.expect_token(&Token::RParen)?;
                 Ok((
                     key.value,
                     PySqlArg::new(None, Some(CustomExpr::Nested(key_value_pairs))),
@@ -1068,15 +1074,15 @@
     ) -> Result<DaskStatement, ParserError> {
         // parse [IF NOT EXISTS] `table_name` AS|WITH
         let if_not_exists =
             self.parser
                 .parse_keywords(&[Keyword::IF, Keyword::NOT, Keyword::EXISTS]);
 
         let _table_name = self.parser.parse_identifier();
-        let after_name_token = self.parser.peek_token();
+        let after_name_token = self.parser.peek_token().token;
 
         match after_name_token {
             Token::Word(w) => {
                 match w.value.to_lowercase().as_str() {
                     "as" => {
                         self.parser.prev_token();
                         if if_not_exists {
@@ -1140,15 +1146,15 @@
                 )))
             }
         }
     }
 
     /// Parse Dask-SQL EXPORT MODEL statement
     fn parse_export_model(&mut self) -> Result<DaskStatement, ParserError> {
-        let is_model = match self.parser.next_token() {
+        let is_model = match self.parser.next_token().token {
             Token::Word(w) => matches!(w.value.to_lowercase().as_str(), "model"),
             _ => false,
         };
         if !is_model {
             return Err(ParserError::ParserError(
                 "parse_export_model: Expected `MODEL`".to_string(),
             ));
@@ -1198,16 +1204,31 @@
             model_name,
         };
         Ok(DaskStatement::DescribeModel(Box::new(describe)))
     }
 
     /// Parse Dask-SQL SHOW SCHEMAS statement
     fn parse_show_schemas(&mut self) -> Result<DaskStatement, ParserError> {
-        // Check for existence of `LIKE` clause
-        let like_val = match self.parser.peek_token() {
+        // parse optional `FROM` clause
+        let catalog_name = match self.parser.peek_token().token {
+            Token::Word(w) => {
+                match w.keyword {
+                    Keyword::FROM => {
+                        // move one token forward
+                        self.parser.next_token();
+                        // use custom parsing
+                        Some(self.parser.parse_identifier()?.value)
+                    }
+                    _ => None,
+                }
+            }
+            _ => None,
+        };
+        // parse optional `LIKE` clause
+        let like = match self.parser.peek_token().token {
             Token::Word(w) => {
                 match w.keyword {
                     Keyword::LIKE => {
                         // move one token forward
                         self.parser.next_token();
                         // use custom parsing
                         Some(self.parser.parse_identifier()?.value)
@@ -1215,26 +1236,31 @@
                     _ => None,
                 }
             }
             _ => None,
         };
 
         Ok(DaskStatement::ShowSchemas(Box::new(ShowSchemas {
-            like: like_val,
+            catalog_name,
+            like,
         })))
     }
 
     /// Parse Dask-SQL SHOW TABLES [FROM] statement
     fn parse_show_tables(&mut self) -> Result<DaskStatement, ParserError> {
-        let mut schema_name = None;
-        if !self.parser.consume_token(&Token::EOF) {
-            schema_name = Some(self.parser.parse_identifier()?.value);
+        if let Ok(obj_name) = &self.parser.parse_object_name() {
+            let (catalog_name, schema_name) = DaskParserUtils::elements_from_object_name(obj_name)?;
+            return Ok(DaskStatement::ShowTables(Box::new(ShowTables {
+                catalog_name,
+                schema_name: Some(schema_name),
+            })));
         }
         Ok(DaskStatement::ShowTables(Box::new(ShowTables {
-            schema_name,
+            catalog_name: None,
+            schema_name: None,
         })))
     }
 
     /// Parse Dask-SQL SHOW COLUMNS FROM <table>
     fn parse_show_columns(&mut self) -> Result<DaskStatement, ParserError> {
         self.parser.expect_keyword(Keyword::FROM)?;
         let (schema_name, table_name) =
```

### Comparing `dask_sql-2023.2.0/dask_planner/src/sql/column.rs` & `dask_sql-2023.4.0/dask_planner/src/sql/column.rs`

 * *Files identical despite different names*

### Comparing `dask_sql-2023.2.0/dask_planner/src/sql/exceptions.rs` & `dask_sql-2023.4.0/dask_planner/src/sql/exceptions.rs`

 * *Files identical despite different names*

### Comparing `dask_sql-2023.2.0/dask_planner/src/sql/function.rs` & `dask_sql-2023.4.0/dask_planner/src/sql/function.rs`

 * *Files 6% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 use std::collections::HashMap;
 
-use arrow::datatypes::DataType;
+use datafusion::arrow::datatypes::DataType;
 use pyo3::prelude::*;
 
 use super::types::PyDataType;
 
 #[pyclass(name = "DaskFunction", module = "dask_planner", subclass)]
 #[derive(Debug, Clone)]
 pub struct DaskFunction {
```

### Comparing `dask_sql-2023.2.0/dask_planner/src/sql/logical/aggregate.rs` & `dask_sql-2023.4.0/dask_planner/src/sql/logical/aggregate.rs`

 * *Files 9% similar despite different names*

```diff
@@ -1,8 +1,9 @@
 use datafusion_expr::{
+    expr::AggregateFunction,
     logical_plan::{Aggregate, Distinct},
     Expr,
     LogicalPlan,
 };
 use pyo3::prelude::*;
 
 use crate::{
@@ -69,41 +70,41 @@
     }
 }
 
 impl PyAggregate {
     fn _aggregation_arguments(&self, expr: &Expr) -> PyResult<Vec<PyExpr>> {
         match expr {
             Expr::Alias(expr, _) => self._aggregation_arguments(expr.as_ref()),
-            Expr::AggregateFunction { fun: _, args, .. }
+            Expr::AggregateFunction(AggregateFunction { fun: _, args, .. })
             | Expr::AggregateUDF { fun: _, args, .. } => match &self.aggregate {
                 Some(e) => py_expr_list(&e.input, args),
                 None => Ok(vec![]),
             },
             _ => Err(py_type_err(
                 "Encountered a non Aggregate type in aggregation_arguments",
             )),
         }
     }
 }
 
 fn _agg_func_name(expr: &Expr) -> PyResult<String> {
     match expr {
         Expr::Alias(expr, _) => _agg_func_name(expr.as_ref()),
-        Expr::AggregateFunction { fun, .. } => Ok(fun.to_string()),
+        Expr::AggregateFunction(AggregateFunction { fun, .. }) => Ok(fun.to_string()),
         Expr::AggregateUDF { fun, .. } => Ok(fun.name.clone()),
         _ => Err(py_type_err(
             "Encountered a non Aggregate type in agg_func_name",
         )),
     }
 }
 
 fn _distinct_agg_expr(expr: &Expr) -> PyResult<bool> {
     match expr {
         Expr::Alias(expr, _) => _distinct_agg_expr(expr.as_ref()),
-        Expr::AggregateFunction { distinct, .. } => Ok(*distinct),
+        Expr::AggregateFunction(AggregateFunction { distinct, .. }) => Ok(*distinct),
         Expr::AggregateUDF { .. } => {
             // DataFusion does not support DISTINCT in UDAFs
             Ok(false)
         }
         _ => Err(py_type_err(
             "Encountered a non Aggregate type in distinct_agg_expr",
         )),
```

### Comparing `dask_sql-2023.2.0/dask_planner/src/sql/logical/alter_schema.rs` & `dask_sql-2023.4.0/dask_planner/src/sql/logical/alter_schema.rs`

 * *Files identical despite different names*

### Comparing `dask_sql-2023.2.0/dask_planner/src/sql/logical/alter_table.rs` & `dask_sql-2023.4.0/dask_planner/src/sql/logical/alter_table.rs`

 * *Files identical despite different names*

### Comparing `dask_sql-2023.2.0/dask_planner/src/sql/logical/analyze_table.rs` & `dask_sql-2023.4.0/dask_planner/src/sql/logical/analyze_table.rs`

 * *Files identical despite different names*

### Comparing `dask_sql-2023.2.0/dask_planner/src/sql/logical/create_catalog_schema.rs` & `dask_sql-2023.4.0/dask_planner/src/sql/logical/create_catalog_schema.rs`

 * *Files identical despite different names*

### Comparing `dask_sql-2023.2.0/dask_planner/src/sql/logical/create_experiment.rs` & `dask_sql-2023.4.0/dask_planner/src/sql/logical/create_experiment.rs`

 * *Files identical despite different names*

### Comparing `dask_sql-2023.2.0/dask_planner/src/sql/logical/create_memory_table.rs` & `dask_sql-2023.4.0/dask_planner/src/sql/logical/create_memory_table.rs`

 * *Files 7% similar despite different names*

```diff
@@ -14,17 +14,17 @@
 }
 
 #[pymethods]
 impl PyCreateMemoryTable {
     #[pyo3(name = "getQualifiedName")]
     pub fn get_table_name(&self) -> PyResult<String> {
         Ok(match &self.create_memory_table {
-            Some(create_memory_table) => create_memory_table.name.clone(),
+            Some(create_memory_table) => create_memory_table.name.to_string(),
             None => match &self.create_view {
-                Some(create_view) => create_view.name.clone(),
+                Some(create_view) => create_view.name.to_string(),
                 None => {
                     return Err(py_type_err(
                         "Encountered a non CreateMemoryTable/CreateView type in get_input",
                     ))
                 }
             },
         })
```

### Comparing `dask_sql-2023.2.0/dask_planner/src/sql/logical/create_model.rs` & `dask_sql-2023.4.0/dask_planner/src/sql/logical/create_model.rs`

 * *Files identical despite different names*

### Comparing `dask_sql-2023.2.0/dask_planner/src/sql/logical/create_table.rs` & `dask_sql-2023.4.0/dask_planner/src/sql/logical/create_table.rs`

 * *Files identical despite different names*

### Comparing `dask_sql-2023.2.0/dask_planner/src/sql/logical/describe_model.rs` & `dask_sql-2023.4.0/dask_planner/src/sql/logical/describe_model.rs`

 * *Files identical despite different names*

### Comparing `dask_sql-2023.2.0/dask_planner/src/sql/logical/drop_model.rs` & `dask_sql-2023.4.0/dask_planner/src/sql/logical/drop_model.rs`

 * *Files identical despite different names*

### Comparing `dask_sql-2023.2.0/dask_planner/src/sql/logical/drop_schema.rs` & `dask_sql-2023.4.0/dask_planner/src/sql/logical/drop_schema.rs`

 * *Files identical despite different names*

### Comparing `dask_sql-2023.2.0/dask_planner/src/sql/logical/drop_table.rs` & `dask_sql-2023.4.0/dask_planner/src/sql/logical/drop_table.rs`

 * *Files 2% similar despite different names*

```diff
@@ -9,15 +9,15 @@
     drop_table: DropTable,
 }
 
 #[pymethods]
 impl PyDropTable {
     #[pyo3(name = "getQualifiedName")]
     pub fn get_name(&self) -> PyResult<String> {
-        Ok(self.drop_table.name.clone())
+        Ok(self.drop_table.name.to_string())
     }
 
     #[pyo3(name = "getIfExists")]
     pub fn get_if_exists(&self) -> PyResult<bool> {
         Ok(self.drop_table.if_exists)
     }
 }
```

### Comparing `dask_sql-2023.2.0/dask_planner/src/sql/logical/empty_relation.rs` & `dask_sql-2023.4.0/dask_planner/src/sql/logical/empty_relation.rs`

 * *Files identical despite different names*

### Comparing `dask_sql-2023.2.0/dask_planner/src/sql/logical/explain.rs` & `dask_sql-2023.4.0/dask_planner/src/sql/logical/explain.rs`

 * *Files identical despite different names*

### Comparing `dask_sql-2023.2.0/dask_planner/src/sql/logical/export_model.rs` & `dask_sql-2023.4.0/dask_planner/src/sql/logical/export_model.rs`

 * *Files identical despite different names*

### Comparing `dask_sql-2023.2.0/dask_planner/src/sql/logical/filter.rs` & `dask_sql-2023.4.0/dask_planner/src/sql/logical/filter.rs`

 * *Files 3% similar despite different names*

```diff
@@ -11,16 +11,16 @@
 
 #[pymethods]
 impl PyFilter {
     /// LogicalPlan::Filter: The PyExpr, predicate, that represents the filtering condition
     #[pyo3(name = "getCondition")]
     pub fn get_condition(&mut self) -> PyResult<PyExpr> {
         Ok(PyExpr::from(
-            self.filter.predicate().clone(),
-            Some(vec![self.filter.input().clone()]),
+            self.filter.predicate.clone(),
+            Some(vec![self.filter.input.clone()]),
         ))
     }
 }
 
 impl TryFrom<LogicalPlan> for PyFilter {
     type Error = PyErr;
```

### Comparing `dask_sql-2023.2.0/dask_planner/src/sql/logical/join.rs` & `dask_sql-2023.4.0/dask_planner/src/sql/logical/join.rs`

 * *Files 24% similar despite different names*

```diff
@@ -1,11 +1,14 @@
+use datafusion_common::Column;
 use datafusion_expr::{
     and,
     logical_plan::{Join, JoinType, LogicalPlan},
+    BinaryExpr,
     Expr,
+    Operator,
 };
 use pyo3::prelude::*;
 
 use crate::{
     expression::PyExpr,
     sql::{column, exceptions::py_type_err},
 };
@@ -15,38 +18,58 @@
 pub struct PyJoin {
     join: Join,
 }
 
 #[pymethods]
 impl PyJoin {
     #[pyo3(name = "getCondition")]
-    pub fn join_condition(&self) -> PyExpr {
+    pub fn join_condition(&self) -> PyResult<Option<PyExpr>> {
         // equi-join filters
         let mut filters: Vec<Expr> = self
             .join
             .on
             .iter()
-            .map(|(l, r)| Expr::Column(l.clone()).eq(Expr::Column(r.clone())))
-            .collect();
+            .map(|(l, r)| match (l, r) {
+                (Expr::Column(l), Expr::Column(r)) => {
+                    Ok(Expr::Column(l.clone()).eq(Expr::Column(r.clone())))
+                }
+                (Expr::Column(l), Expr::Cast(cast)) => {
+                    let right = Column::from_qualified_name(cast.expr.to_string());
+                    Ok(Expr::Column(l.clone()).eq(Expr::Column(right)))
+                }
+                (Expr::Column(l), Expr::BinaryExpr(bin_expr)) => {
+                    Ok(Expr::BinaryExpr(BinaryExpr::new(
+                        Box::new(Expr::Column(l.clone())),
+                        Operator::Eq,
+                        Box::new(Expr::BinaryExpr(bin_expr.clone())),
+                    )))
+                }
+                _ => Err(py_type_err(format!(
+                    "unsupported join condition. Left: {l} - Right: {r}"
+                ))),
+            })
+            .collect::<Result<Vec<_>, _>>()?;
 
         // other filter conditions
         if let Some(filter) = &self.join.filter {
             filters.push(filter.clone());
         }
 
-        assert!(!filters.is_empty());
-
-        let root_expr = filters[1..]
-            .iter()
-            .fold(filters[0].clone(), |acc, expr| and(acc, expr.clone()));
-
-        PyExpr::from(
-            root_expr,
-            Some(vec![self.join.left.clone(), self.join.right.clone()]),
-        )
+        if !filters.is_empty() {
+            let root_expr = filters[1..]
+                .iter()
+                .fold(filters[0].clone(), |acc, expr| and(acc, expr.clone()));
+
+            Ok(Some(PyExpr::from(
+                root_expr,
+                Some(vec![self.join.left.clone(), self.join.right.clone()]),
+            )))
+        } else {
+            Ok(None)
+        }
     }
 
     #[pyo3(name = "getJoinConditions")]
     pub fn join_conditions(&mut self) -> PyResult<Vec<(column::PyColumn, column::PyColumn)>> {
         let lhs_table_name: String = match &*self.join.left {
             LogicalPlan::TableScan(scan) => scan.table_name.clone(),
             _ => {
@@ -62,18 +85,23 @@
                 return Err(py_type_err(
                     "rhs Expected TableScan but something else was received!",
                 ))
             }
         };
 
         let mut join_conditions: Vec<(column::PyColumn, column::PyColumn)> = Vec::new();
-        for (mut lhs, mut rhs) in self.join.on.clone() {
-            lhs.relation = Some(lhs_table_name.clone());
-            rhs.relation = Some(rhs_table_name.clone());
-            join_conditions.push((lhs.into(), rhs.into()));
+        for (lhs, rhs) in self.join.on.clone() {
+            match (lhs, rhs) {
+                (Expr::Column(mut lhs), Expr::Column(mut rhs)) => {
+                    lhs.relation = Some(lhs_table_name.clone());
+                    rhs.relation = Some(rhs_table_name.clone());
+                    join_conditions.push((lhs.into(), rhs.into()));
+                }
+                _ => return Err(py_type_err("unsupported join condition")),
+            }
         }
         Ok(join_conditions)
     }
 
     /// Returns the type of join represented by this LogicalPlan::Join instance
     #[pyo3(name = "getJoinType")]
     pub fn join_type(&mut self) -> PyResult<String> {
```

### Comparing `dask_sql-2023.2.0/dask_planner/src/sql/logical/limit.rs` & `dask_sql-2023.4.0/dask_planner/src/sql/logical/limit.rs`

 * *Files identical despite different names*

### Comparing `dask_sql-2023.2.0/dask_planner/src/sql/logical/predict_model.rs` & `dask_sql-2023.4.0/dask_planner/src/sql/logical/predict_model.rs`

 * *Files identical despite different names*

### Comparing `dask_sql-2023.2.0/dask_planner/src/sql/logical/projection.rs` & `dask_sql-2023.4.0/dask_planner/src/sql/logical/projection.rs`

 * *Files identical despite different names*

### Comparing `dask_sql-2023.2.0/dask_planner/src/sql/logical/repartition_by.rs` & `dask_sql-2023.4.0/dask_planner/src/sql/logical/repartition_by.rs`

 * *Files identical despite different names*

### Comparing `dask_sql-2023.2.0/dask_planner/src/sql/logical/show_columns.rs` & `dask_sql-2023.4.0/dask_planner/src/sql/logical/show_columns.rs`

 * *Files identical despite different names*

### Comparing `dask_sql-2023.2.0/dask_planner/src/sql/logical/show_models.rs` & `dask_sql-2023.4.0/dask_planner/src/sql/logical/show_models.rs`

 * *Files identical despite different names*

### Comparing `dask_sql-2023.2.0/dask_planner/src/sql/logical/show_schema.rs` & `dask_sql-2023.4.0/dask_planner/src/sql/logical/show_schemas.rs`

 * *Files 9% similar despite different names*

```diff
@@ -10,14 +10,15 @@
 use pyo3::prelude::*;
 
 use crate::sql::{exceptions::py_type_err, logical};
 
 #[derive(Clone)]
 pub struct ShowSchemasPlanNode {
     pub schema: DFSchemaRef,
+    pub catalog_name: Option<String>,
     pub like: Option<String>,
 }
 
 impl Debug for ShowSchemasPlanNode {
     fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
         self.fmt_for_explain(f)
     }
@@ -40,39 +41,45 @@
         // there is no need to expose any expressions here since DataFusion would
         // not be able to do anything with expressions that are specific to
         // SHOW SCHEMAS
         vec![]
     }
 
     fn fmt_for_explain(&self, f: &mut fmt::Formatter) -> fmt::Result {
-        write!(f, "ShowSchema")
+        write!(f, "ShowSchema: catalog_name: {:?}", self.catalog_name)
     }
 
     fn from_template(
         &self,
         _exprs: &[Expr],
         _inputs: &[LogicalPlan],
     ) -> Arc<dyn UserDefinedLogicalNode> {
         Arc::new(ShowSchemasPlanNode {
             schema: Arc::new(DFSchema::empty()),
+            catalog_name: self.catalog_name.clone(),
             like: self.like.clone(),
         })
     }
 }
 
 #[pyclass(name = "ShowSchema", module = "dask_planner", subclass)]
 pub struct PyShowSchema {
     pub(crate) show_schema: ShowSchemasPlanNode,
 }
 
 #[pymethods]
 impl PyShowSchema {
+    #[pyo3(name = "getCatalogName")]
+    fn get_from(&self) -> PyResult<Option<String>> {
+        Ok(self.show_schema.catalog_name.clone())
+    }
+
     #[pyo3(name = "getLike")]
-    fn get_like(&self) -> PyResult<String> {
-        Ok(self.show_schema.like.as_ref().cloned().unwrap_or_default())
+    fn get_like(&self) -> PyResult<Option<String>> {
+        Ok(self.show_schema.like.clone())
     }
 }
 
 impl TryFrom<logical::LogicalPlan> for PyShowSchema {
     type Error = PyErr;
 
     fn try_from(logical_plan: logical::LogicalPlan) -> Result<Self, Self::Error> {
```

### Comparing `dask_sql-2023.2.0/dask_planner/src/sql/logical/show_tables.rs` & `dask_sql-2023.4.0/dask_planner/src/sql/logical/show_tables.rs`

 * *Files 16% similar despite different names*

```diff
@@ -10,14 +10,15 @@
 use pyo3::prelude::*;
 
 use crate::sql::{exceptions::py_type_err, logical};
 
 #[derive(Clone)]
 pub struct ShowTablesPlanNode {
     pub schema: DFSchemaRef,
+    pub catalog_name: Option<String>,
     pub schema_name: Option<String>,
 }
 
 impl Debug for ShowTablesPlanNode {
     fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
         self.fmt_for_explain(f)
     }
@@ -40,36 +41,46 @@
         // there is no need to expose any expressions here since DataFusion would
         // not be able to do anything with expressions that are specific to
         // SHOW TABLES FROM {schema_name}
         vec![]
     }
 
     fn fmt_for_explain(&self, f: &mut fmt::Formatter) -> fmt::Result {
-        write!(f, "ShowTables: schema_name: {:?}", self.schema_name)
+        write!(
+            f,
+            "ShowTables: catalog_name: {:?}, schema_name: {:?}",
+            self.catalog_name, self.schema_name
+        )
     }
 
     fn from_template(
         &self,
         _exprs: &[Expr],
         _inputs: &[LogicalPlan],
     ) -> Arc<dyn UserDefinedLogicalNode> {
         Arc::new(ShowTablesPlanNode {
             schema: Arc::new(DFSchema::empty()),
+            catalog_name: self.catalog_name.clone(),
             schema_name: self.schema_name.clone(),
         })
     }
 }
 
 #[pyclass(name = "ShowTables", module = "dask_planner", subclass)]
 pub struct PyShowTables {
     pub(crate) show_tables: ShowTablesPlanNode,
 }
 
 #[pymethods]
 impl PyShowTables {
+    #[pyo3(name = "getCatalogName")]
+    fn get_catalog_name(&self) -> PyResult<Option<String>> {
+        Ok(self.show_tables.catalog_name.clone())
+    }
+
     #[pyo3(name = "getSchemaName")]
     fn get_schema_name(&self) -> PyResult<Option<String>> {
         Ok(self.show_tables.schema_name.clone())
     }
 }
 
 impl TryFrom<logical::LogicalPlan> for PyShowTables {
```

### Comparing `dask_sql-2023.2.0/dask_planner/src/sql/logical/sort.rs` & `dask_sql-2023.4.0/dask_planner/src/sql/logical/sort.rs`

 * *Files identical despite different names*

### Comparing `dask_sql-2023.2.0/dask_planner/src/sql/logical/subquery_alias.rs` & `dask_sql-2023.4.0/dask_planner/src/sql/logical/subquery_alias.rs`

 * *Files identical despite different names*

### Comparing `dask_sql-2023.2.0/dask_planner/src/sql/logical/table_scan.rs` & `dask_sql-2023.4.0/dask_planner/src/sql/logical/table_scan.rs`

 * *Files identical despite different names*

### Comparing `dask_sql-2023.2.0/dask_planner/src/sql/logical/use_schema.rs` & `dask_sql-2023.4.0/dask_planner/src/sql/logical/use_schema.rs`

 * *Files identical despite different names*

### Comparing `dask_sql-2023.2.0/dask_planner/src/sql/logical/window.rs` & `dask_sql-2023.4.0/dask_planner/src/sql/logical/window.rs`

 * *Files 6% similar despite different names*

```diff
@@ -1,9 +1,16 @@
 use datafusion_common::ScalarValue;
-use datafusion_expr::{logical_plan::Window, Expr, LogicalPlan, WindowFrame, WindowFrameBound};
+use datafusion_expr::{
+    expr::WindowFunction,
+    logical_plan::Window,
+    Expr,
+    LogicalPlan,
+    WindowFrame,
+    WindowFrameBound,
+};
 use pyo3::prelude::*;
 
 use crate::{
     error::DaskPlannerError,
     expression::{py_expr_list, PyExpr},
     sql::exceptions::py_type_err,
 };
@@ -57,55 +64,57 @@
         py_expr_list(&self.window.input, &self.window.window_expr)
     }
 
     /// Returns order by columns in a window function expression
     #[pyo3(name = "getSortExprs")]
     pub fn get_sort_exprs(&self, expr: PyExpr) -> PyResult<Vec<PyExpr>> {
         match expr.expr.unalias() {
-            Expr::WindowFunction { order_by, .. } => py_expr_list(&self.window.input, &order_by),
+            Expr::WindowFunction(WindowFunction { order_by, .. }) => {
+                py_expr_list(&self.window.input, &order_by)
+            }
             other => Err(not_window_function_err(other)),
         }
     }
 
     /// Return partition by columns in a window function expression
     #[pyo3(name = "getPartitionExprs")]
     pub fn get_partition_exprs(&self, expr: PyExpr) -> PyResult<Vec<PyExpr>> {
         match expr.expr.unalias() {
-            Expr::WindowFunction { partition_by, .. } => {
+            Expr::WindowFunction(WindowFunction { partition_by, .. }) => {
                 py_expr_list(&self.window.input, &partition_by)
             }
             other => Err(not_window_function_err(other)),
         }
     }
 
     /// Return input args for window function
     #[pyo3(name = "getArgs")]
     pub fn get_args(&self, expr: PyExpr) -> PyResult<Vec<PyExpr>> {
         match expr.expr.unalias() {
-            Expr::WindowFunction { args, .. } => py_expr_list(&self.window.input, &args),
+            Expr::WindowFunction(WindowFunction { args, .. }) => {
+                py_expr_list(&self.window.input, &args)
+            }
             other => Err(not_window_function_err(other)),
         }
     }
 
     /// Return window function name
     #[pyo3(name = "getWindowFuncName")]
     pub fn window_func_name(&self, expr: PyExpr) -> PyResult<String> {
         match expr.expr.unalias() {
-            Expr::WindowFunction { fun, .. } => Ok(fun.to_string()),
+            Expr::WindowFunction(WindowFunction { fun, .. }) => Ok(fun.to_string()),
             other => Err(not_window_function_err(other)),
         }
     }
 
     /// Returns a Pywindow frame for a given window function expression
     #[pyo3(name = "getWindowFrame")]
     pub fn get_window_frame(&self, expr: PyExpr) -> Option<PyWindowFrame> {
         match expr.expr.unalias() {
-            Expr::WindowFunction { window_frame, .. } => {
-                window_frame.map(|window_frame| window_frame.into())
-            }
+            Expr::WindowFunction(WindowFunction { window_frame, .. }) => Some(window_frame.into()),
             _ => None,
         }
     }
 }
 
 fn not_window_function_err(expr: Expr) -> PyErr {
     py_type_err(format!(
@@ -152,29 +161,30 @@
     #[pyo3(name = "isFollowing")]
     pub fn is_following(&self) -> bool {
         matches!(self.frame_bound, WindowFrameBound::Following(_))
     }
     /// Returns the offset of the window frame
     #[pyo3(name = "getOffset")]
     pub fn get_offset(&self) -> PyResult<Option<u64>> {
-        match self.frame_bound {
-            WindowFrameBound::Preceding(ScalarValue::UInt64(val))
-            | WindowFrameBound::Following(ScalarValue::UInt64(val)) => Ok(val),
-            WindowFrameBound::Preceding(ref x) | WindowFrameBound::Following(ref x) => Err(
-                DaskPlannerError::Internal(format!("Unexpected window frame bound: {x:?}")).into(),
-            ),
+        match &self.frame_bound {
+            WindowFrameBound::Preceding(val) | WindowFrameBound::Following(val) => match val {
+                x if x.is_null() => Ok(None),
+                ScalarValue::UInt64(v) => Ok(*v),
+                // The cast below is only safe because window bounds cannot be negative
+                ScalarValue::Int64(v) => Ok(v.map(|n| n as u64)),
+                ref x => Err(DaskPlannerError::Internal(format!(
+                    "Unexpected window frame bound: {x}"
+                ))
+                .into()),
+            },
             WindowFrameBound::CurrentRow => Ok(None),
         }
     }
     /// Returns if the frame bound is unbounded
     #[pyo3(name = "isUnbounded")]
     pub fn is_unbounded(&self) -> PyResult<bool> {
         match &self.frame_bound {
-            WindowFrameBound::Preceding(ScalarValue::UInt64(v))
-            | WindowFrameBound::Following(ScalarValue::UInt64(v)) => Ok(v.is_none()),
-            WindowFrameBound::Preceding(ref x) | WindowFrameBound::Following(ref x) => Err(
-                DaskPlannerError::Internal(format!("Unexpected window frame bound: {x:?}")).into(),
-            ),
+            WindowFrameBound::Preceding(v) | WindowFrameBound::Following(v) => Ok(v.is_null()),
             WindowFrameBound::CurrentRow => Ok(false),
         }
     }
 }
```

### Comparing `dask_sql-2023.2.0/dask_planner/src/sql/logical.rs` & `dask_sql-2023.4.0/dask_planner/src/sql/logical.rs`

 * *Files 2% similar despite different names*

```diff
@@ -23,15 +23,15 @@
 pub mod join;
 pub mod limit;
 pub mod predict_model;
 pub mod projection;
 pub mod repartition_by;
 pub mod show_columns;
 pub mod show_models;
-pub mod show_schema;
+pub mod show_schemas;
 pub mod show_tables;
 pub mod sort;
 pub mod subquery_alias;
 pub mod table_scan;
 pub mod use_schema;
 pub mod window;
 
@@ -50,15 +50,15 @@
     describe_model::DescribeModelPlanNode,
     drop_model::DropModelPlanNode,
     drop_schema::DropSchemaPlanNode,
     export_model::ExportModelPlanNode,
     predict_model::PredictModelPlanNode,
     show_columns::ShowColumnsPlanNode,
     show_models::ShowModelsPlanNode,
-    show_schema::ShowSchemasPlanNode,
+    show_schemas::ShowSchemasPlanNode,
     show_tables::ShowTablesPlanNode,
     use_schema::UseSchemaPlanNode,
 };
 use crate::{error::Result, sql::exceptions::py_type_err};
 
 #[pyclass(name = "LogicalPlan", module = "dask_planner", subclass)]
 #[derive(Debug, Clone)]
@@ -173,15 +173,15 @@
 
     /// LogicalPlan::DropModel as DropModel
     pub fn drop_model(&self) -> PyResult<drop_model::PyDropModel> {
         to_py_plan(self.current_node.as_ref())
     }
 
     /// LogicalPlan::Extension::ShowSchemas as PyShowSchemas
-    pub fn show_schemas(&self) -> PyResult<show_schema::PyShowSchema> {
+    pub fn show_schemas(&self) -> PyResult<show_schemas::PyShowSchema> {
         to_py_plan(self.current_node.as_ref())
     }
 
     /// LogicalPlan::Repartition as PyRepartitionBy
     pub fn repartition_by(&self) -> PyResult<repartition_by::PyRepartitionBy> {
         to_py_plan(self.current_node.as_ref())
     }
@@ -293,14 +293,17 @@
             Err(_e) => Err(py_type_err("Unable to determine current node table name")),
         }
     }
 
     /// Gets the Relation "type" of the current node. Ex: Projection, TableScan, etc
     pub fn get_current_node_type(&mut self) -> PyResult<&str> {
         Ok(match self.current_node() {
+            LogicalPlan::Dml(_) => "DataManipulationLanguage",
+            LogicalPlan::DescribeTable(_) => "DescribeTable",
+            LogicalPlan::Prepare(_) => "Prepare",
             LogicalPlan::Distinct(_) => "Distinct",
             LogicalPlan::Projection(_projection) => "Projection",
             LogicalPlan::Filter(_filter) => "Filter",
             LogicalPlan::Window(_window) => "Window",
             LogicalPlan::Aggregate(_aggregate) => "Aggregate",
             LogicalPlan::Sort(_sort) => "Sort",
             LogicalPlan::Join(_join) => "Join",
@@ -361,14 +364,15 @@
                 } else if node.downcast_ref::<AlterSchemaPlanNode>().is_some() {
                     "AlterSchema"
                 } else {
                     // Default to generic `Extension`
                     "Extension"
                 }
             }
+            LogicalPlan::Unnest(_unnest) => "Unnest",
         })
     }
 
     /// Explain plan for the full and original LogicalPlan
     pub fn explain_original(&self) -> PyResult<String> {
         Ok(format!("{}", self.original_plan.display_indent()))
     }
```

### Comparing `dask_sql-2023.2.0/dask_planner/src/sql/optimizer/filter_columns_post_join.rs` & `dask_sql-2023.4.0/dask_planner/src/sql/optimizer/filter_columns_post_join.rs`

 * *Files 3% similar despite different names*

```diff
@@ -90,28 +90,29 @@
 
 /// Optimizer rule dropping join key columns post join
 #[derive(Default)]
 pub struct FilterColumnsPostJoin {}
 
 impl FilterColumnsPostJoin {
     #[allow(missing_docs)]
+    #[allow(dead_code)]
     pub fn new() -> Self {
         Self {}
     }
 }
 
 impl OptimizerRule for FilterColumnsPostJoin {
-    fn optimize(
+    fn try_optimize(
         &self,
         plan: &LogicalPlan,
-        _optimizer_config: &mut OptimizerConfig,
-    ) -> Result<LogicalPlan> {
+        _optimizer_config: &dyn OptimizerConfig,
+    ) -> Result<Option<LogicalPlan>> {
         // Store info about all columns in all schemas
         let all_schemas = &plan.all_schemas();
-        optimize_top_down(plan, all_schemas, HashSet::new())
+        Ok(Some(optimize_top_down(plan, all_schemas, HashSet::new())?))
     }
 
     fn name(&self) -> &str {
         "filter_columns_post_join"
     }
 }
 
@@ -184,40 +185,39 @@
                                 }
                             }
                         }
                         let projection_schema =
                             DFSchema::new_with_metadata(projection_schema_fields, HashMap::new());
 
                         // Create a Projection with the columns from the HashSet
-                        let projection_plan = LogicalPlan::Projection(Projection {
-                            expr: projection_columns,
-                            input: Arc::new(current_plan.clone()),
-                            schema: Arc::new(projection_schema.unwrap()),
-                        });
+                        let projection_plan =
+                            LogicalPlan::Projection(Projection::try_new_with_schema(
+                                projection_columns,
+                                Arc::new(current_plan.clone()),
+                                Arc::new(projection_schema?),
+                            )?);
 
                         // Add Projection to HashMap
                         new_plan.insert(counter, projection_plan);
                         counter += 1;
                     }
 
                     insert_post_join_columns(&mut post_join_columns, current_columns);
 
                     // Recurse on left and right inputs of Join
                     let left_join_plan = optimize_top_down(
                         &j.left,
                         &j.left.all_schemas(),
                         post_join_columns.clone(),
-                    )
-                    .unwrap();
+                    )?;
                     let right_join_plan = optimize_top_down(
                         &j.right,
                         &j.right.all_schemas(),
                         post_join_columns.clone(),
-                    )
-                    .unwrap();
+                    )?;
                     let join_plan = LogicalPlan::Join(Join {
                         left: Arc::new(left_join_plan),
                         right: Arc::new(right_join_plan),
                         on: j.on.clone(),
                         filter: j.filter.clone(),
                         join_type: j.join_type,
                         join_constraint: j.join_constraint,
@@ -230,22 +230,20 @@
                 }
                 LogicalPlan::CrossJoin(ref c) => {
                     // Recurse on left and right inputs of CrossJoin
                     let left_crossjoin_plan = optimize_top_down(
                         &c.left,
                         &c.left.all_schemas(),
                         post_join_columns.clone(),
-                    )
-                    .unwrap();
+                    )?;
                     let right_crossjoin_plan = optimize_top_down(
                         &c.right,
                         &c.right.all_schemas(),
                         post_join_columns.clone(),
-                    )
-                    .unwrap();
+                    )?;
                     let crossjoin_plan = LogicalPlan::CrossJoin(CrossJoin {
                         left: Arc::new(left_crossjoin_plan),
                         right: Arc::new(right_crossjoin_plan),
                         schema: c.schema.clone(),
                     });
 
                     // Add CrossJoin to HashMap
@@ -316,32 +314,31 @@
         let mut next_step;
         let mut return_plan = plan.clone();
 
         for key in (0..counter).rev() {
             next_step = new_plan.get(&key).unwrap();
             match next_step {
                 LogicalPlan::Projection(p) => {
-                    return_plan = LogicalPlan::Projection(Projection {
-                        expr: p.expr.clone(),
-                        input: Arc::new(previous_step.clone()),
-                        schema: p.schema.clone(),
-                    });
+                    return_plan = LogicalPlan::Projection(Projection::try_new_with_schema(
+                        p.expr.clone(),
+                        Arc::new(previous_step.clone()),
+                        p.schema.clone(),
+                    )?);
                 }
                 LogicalPlan::SubqueryAlias(s) => {
-                    return_plan = LogicalPlan::SubqueryAlias(SubqueryAlias {
-                        input: Arc::new(previous_step.clone()),
-                        alias: s.alias.clone(),
-                        schema: s.schema.clone(),
-                    });
+                    return_plan = LogicalPlan::SubqueryAlias(SubqueryAlias::try_new(
+                        previous_step.clone(),
+                        s.alias.clone(),
+                    )?);
                 }
                 LogicalPlan::Filter(f) => {
-                    return_plan = LogicalPlan::Filter(
-                        Filter::try_new(f.predicate().clone(), Arc::new(previous_step.clone()))
-                            .unwrap(),
-                    );
+                    return_plan = LogicalPlan::Filter(Filter::try_new(
+                        f.predicate.clone(),
+                        Arc::new(previous_step.clone()),
+                    )?);
                 }
                 LogicalPlan::Window(w) => {
                     return_plan = LogicalPlan::Window(Window {
                         input: Arc::new(previous_step.clone()),
                         window_expr: w.window_expr.clone(),
                         schema: w.schema.clone(),
                     });
@@ -370,14 +367,15 @@
                 }
                 LogicalPlan::Explain(e) => {
                     return_plan = LogicalPlan::Explain(Explain {
                         verbose: e.verbose,
                         plan: Arc::new(previous_step.clone()),
                         stringified_plans: e.stringified_plans.clone(),
                         schema: e.schema.clone(),
+                        logical_optimization_succeeded: false, // While Dask-SQL does not use the DataFusion Physical Planner we should set this value to False to guard any 3rd party dependency using Dask-SQL from assuming the plan is safe to use at this point.
                     });
                 }
                 LogicalPlan::Analyze(a) => {
                     return_plan = LogicalPlan::Analyze(Analyze {
                         verbose: a.verbose,
                         input: Arc::new(previous_step.clone()),
                         schema: a.schema.clone(),
@@ -392,20 +390,20 @@
                 }
                 LogicalPlan::Distinct(_) => {
                     return_plan = LogicalPlan::Distinct(Distinct {
                         input: Arc::new(previous_step.clone()),
                     });
                 }
                 LogicalPlan::Aggregate(a) => {
-                    return_plan = LogicalPlan::Aggregate(Aggregate {
-                        input: Arc::new(previous_step.clone()),
-                        group_expr: a.group_expr.clone(),
-                        aggr_expr: a.aggr_expr.clone(),
-                        schema: a.schema.clone(),
-                    });
+                    return_plan = LogicalPlan::Aggregate(Aggregate::try_new_with_schema(
+                        Arc::new(previous_step.clone()),
+                        a.group_expr.clone(),
+                        a.aggr_expr.clone(),
+                        a.schema.clone(),
+                    )?);
                 }
                 LogicalPlan::Sort(s) => {
                     return_plan = LogicalPlan::Sort(Sort {
                         expr: s.expr.clone(),
                         input: Arc::new(previous_step.clone()),
                         fetch: s.fetch,
                     });
@@ -496,30 +494,31 @@
     }
 }
 
 #[cfg(test)]
 mod tests {
     use std::sync::Arc;
 
-    use arrow::datatypes::{DataType, Field, Schema};
+    use datafusion::arrow::datatypes::{DataType, Field, Schema};
     use datafusion_expr::{
         col,
         logical_plan::{builder::LogicalTableSource, JoinType, LogicalPlanBuilder},
         sum,
     };
+    use datafusion_optimizer::OptimizerContext;
 
     use super::*;
 
     /// Optimize with just the filter_columns_post_join rule
     fn optimized_plan_eq(plan: &LogicalPlan, expected1: &str, expected2: &str) -> bool {
         let rule = FilterColumnsPostJoin::new();
         let optimized_plan = rule
-            .optimize(plan, &mut OptimizerConfig::new())
+            .try_optimize(plan, &OptimizerContext::new())
             .expect("failed to optimize plan");
-        let formatted_plan = format!("{}", optimized_plan.display_indent());
+        let formatted_plan = format!("{}", optimized_plan.unwrap().display_indent());
 
         if formatted_plan == expected1 || formatted_plan == expected2 {
             true
         } else {
             false
         }
     }
@@ -529,15 +528,15 @@
         // Projection: SUM(df.a), df2.b
         //   Aggregate: groupBy=[[df2.b]], aggr=[[SUM(df.a)]]
         //     Inner Join: df.c = df2.c
         //       TableScan: df
         //       TableScan: df2
         let plan = LogicalPlanBuilder::from(test_table_scan("df", "a"))
             .join(
-                &LogicalPlanBuilder::from(test_table_scan("df2", "b")).build()?,
+                LogicalPlanBuilder::from(test_table_scan("df2", "b")).build()?,
                 JoinType::Inner,
                 (vec!["c"], vec!["c"]),
                 None,
             )?
             .aggregate(vec![col("df2.b")], vec![sum(col("df.a"))])?
             .project(vec![sum(col("df.a")), col("df2.b")])?
             .build()?;
```

### Comparing `dask_sql-2023.2.0/dask_planner/src/sql/optimizer.rs` & `dask_sql-2023.4.0/dask_planner/src/sql/optimizer.rs`

 * *Files 8% similar despite different names*

```diff
@@ -3,93 +3,90 @@
 use datafusion_common::DataFusionError;
 use datafusion_expr::LogicalPlan;
 use datafusion_optimizer::{
     common_subexpr_eliminate::CommonSubexprEliminate,
     decorrelate_where_exists::DecorrelateWhereExists,
     decorrelate_where_in::DecorrelateWhereIn,
     eliminate_cross_join::EliminateCrossJoin,
-    // TODO: need to handle EmptyRelation for GPU cases
-    // eliminate_filter::EliminateFilter,
     eliminate_limit::EliminateLimit,
     eliminate_outer_join::EliminateOuterJoin,
     filter_null_join_keys::FilterNullJoinKeys,
     inline_table_scan::InlineTableScan,
-    limit_push_down::LimitPushDown,
     optimizer::{Optimizer, OptimizerRule},
-    projection_push_down::ProjectionPushDown,
     push_down_filter::PushDownFilter,
+    push_down_limit::PushDownLimit,
+    push_down_projection::PushDownProjection,
     rewrite_disjunctive_predicate::RewriteDisjunctivePredicate,
     scalar_subquery_to_join::ScalarSubqueryToJoin,
     simplify_expressions::SimplifyExpressions,
-    subquery_filter_to_join::SubqueryFilterToJoin,
     type_coercion::TypeCoercion,
     unwrap_cast_in_comparison::UnwrapCastInComparison,
-    OptimizerConfig,
+    OptimizerContext,
 };
-use log::trace;
+use log::{debug, trace};
 
 mod filter_columns_post_join;
-use filter_columns_post_join::FilterColumnsPostJoin;
+
+mod join_reorder;
+use join_reorder::JoinReorder;
 
 /// Houses the optimization logic for Dask-SQL. This optimization controls the optimizations
 /// and their ordering in regards to their impact on the underlying `LogicalPlan` instance
 pub struct DaskSqlOptimizer {
-    skip_failing_rules: bool,
     optimizer: Optimizer,
 }
 
 impl DaskSqlOptimizer {
     /// Creates a new instance of the DaskSqlOptimizer with all the DataFusion desired
     /// optimizers as well as any custom `OptimizerRule` trait impls that might be desired.
-    pub fn new(skip_failing_rules: bool) -> Self {
+    pub fn new() -> Self {
+        debug!("Creating new instance of DaskSqlOptimizer");
         let rules: Vec<Arc<dyn OptimizerRule + Sync + Send>> = vec![
             Arc::new(InlineTableScan::new()),
             Arc::new(TypeCoercion::new()),
             Arc::new(SimplifyExpressions::new()),
             Arc::new(UnwrapCastInComparison::new()),
             Arc::new(DecorrelateWhereExists::new()),
             Arc::new(DecorrelateWhereIn::new()),
             Arc::new(ScalarSubqueryToJoin::new()),
-            Arc::new(SubqueryFilterToJoin::new()),
             // simplify expressions does not simplify expressions in subqueries, so we
             // run it again after running the optimizations that potentially converted
             // subqueries to joins
             Arc::new(SimplifyExpressions::new()),
             // TODO: need to handle EmptyRelation for GPU cases
             // Arc::new(EliminateFilter::new()),
             Arc::new(EliminateCrossJoin::new()),
             Arc::new(CommonSubexprEliminate::new()),
             Arc::new(EliminateLimit::new()),
             Arc::new(RewriteDisjunctivePredicate::new()),
             Arc::new(FilterNullJoinKeys::default()),
             Arc::new(EliminateOuterJoin::new()),
             Arc::new(PushDownFilter::new()),
-            Arc::new(LimitPushDown::new()),
+            Arc::new(PushDownLimit::new()),
             // Dask-SQL specific optimizations
-            Arc::new(FilterColumnsPostJoin::new()),
+            // Arc::new(FilterColumnsPostJoin::new()),
+            Arc::new(JoinReorder::default()),
             // The previous optimizations added expressions and projections,
             // that might benefit from the following rules
             Arc::new(SimplifyExpressions::new()),
             Arc::new(UnwrapCastInComparison::new()),
             Arc::new(CommonSubexprEliminate::new()),
-            Arc::new(ProjectionPushDown::new()),
+            Arc::new(PushDownProjection::new()),
         ];
 
         Self {
-            skip_failing_rules,
             optimizer: Optimizer::with_rules(rules),
         }
     }
 
     /// Iterates through the configured `OptimizerRule`(s) to transform the input `LogicalPlan`
     /// to its final optimized form
     pub(crate) fn optimize(&self, plan: LogicalPlan) -> Result<LogicalPlan, DataFusionError> {
-        let mut config =
-            OptimizerConfig::default().with_skip_failing_rules(self.skip_failing_rules);
-        self.optimizer.optimize(&plan, &mut config, Self::observe)
+        let config = OptimizerContext::new();
+        self.optimizer.optimize(&plan, &config, Self::observe)
     }
 
     fn observe(optimized_plan: &LogicalPlan, optimization: &dyn OptimizerRule) {
         trace!(
             "== AFTER APPLYING RULE {} ==\n{}\n",
             optimization.name(),
             optimized_plan.display_indent()
@@ -97,16 +94,16 @@
     }
 }
 
 #[cfg(test)]
 mod tests {
     use std::{any::Any, collections::HashMap, sync::Arc};
 
-    use arrow::datatypes::{DataType, Field, Schema, SchemaRef};
-    use datafusion_common::{DataFusionError, Result, ScalarValue};
+    use datafusion::arrow::datatypes::{DataType, Field, Schema, SchemaRef};
+    use datafusion_common::{config::ConfigOptions, DataFusionError, Result};
     use datafusion_expr::{AggregateUDF, LogicalPlan, ScalarUDF, TableSource};
     use datafusion_sql::{
         planner::{ContextProvider, SqlToRel},
         sqlparser::{ast::Statement, parser::Parser},
         TableReference,
     };
 
@@ -119,18 +116,18 @@
     WHERE col_int32 > (\
       SELECT AVG(col_int32) FROM test \
       WHERE col_utf8 BETWEEN '2002-05-08' \
         AND (cast('2002-05-08' as date) + interval '5 days')\
     )";
         let plan = test_sql(sql)?;
         let expected = r#"Projection: test.col_int32
-  Filter: CAST(test.col_int32 AS Float64) > __sq_1.__value
+  Filter: CAST(test.col_int32 AS Float64) > __scalar_sq_1.__value
     CrossJoin:
       TableScan: test projection=[col_int32]
-      SubqueryAlias: __sq_1
+      SubqueryAlias: __scalar_sq_1
         Projection: AVG(test.col_int32) AS __value
           Aggregate: groupBy=[[]], aggr=[[AVG(test.col_int32)]]
             Filter: test.col_utf8 >= Utf8("2002-05-08") AND test.col_utf8 <= Utf8("2002-05-13")
               TableScan: test projection=[col_int32, col_utf8]"#;
         assert_eq!(expected, format!("{:?}", plan));
         Ok(())
     }
@@ -138,26 +135,40 @@
     fn test_sql(sql: &str) -> Result<LogicalPlan> {
         // parse the SQL
         let dialect = DaskDialect {};
         let ast: Vec<Statement> = Parser::parse_sql(&dialect, sql).unwrap();
         let statement = &ast[0];
 
         // create a logical query plan
-        let schema_provider = MySchemaProvider {};
+        let schema_provider = MySchemaProvider::new();
         let sql_to_rel = SqlToRel::new(&schema_provider);
         let plan = sql_to_rel.sql_statement_to_plan(statement.clone()).unwrap();
 
         // optimize the logical plan
-        let optimizer = DaskSqlOptimizer::new(false);
+        let optimizer = DaskSqlOptimizer::new();
         optimizer.optimize(plan)
     }
 
-    struct MySchemaProvider {}
+    struct MySchemaProvider {
+        options: ConfigOptions,
+    }
+
+    impl MySchemaProvider {
+        fn new() -> Self {
+            Self {
+                options: ConfigOptions::default(),
+            }
+        }
+    }
 
     impl ContextProvider for MySchemaProvider {
+        fn options(&self) -> &ConfigOptions {
+            &self.options
+        }
+
         fn get_table_provider(
             &self,
             name: TableReference,
         ) -> datafusion_common::Result<Arc<dyn TableSource>> {
             let table_name = name.table();
             if table_name.starts_with("test") {
                 let schema = Schema::new_with_metadata(
@@ -186,18 +197,14 @@
         fn get_aggregate_meta(&self, _name: &str) -> Option<Arc<AggregateUDF>> {
             None
         }
 
         fn get_variable_type(&self, _variable_names: &[String]) -> Option<DataType> {
             None
         }
-
-        fn get_config_option(&self, _option: &str) -> Option<ScalarValue> {
-            None
-        }
     }
 
     struct MyTableSource {
         schema: SchemaRef,
     }
 
     impl TableSource for MyTableSource {
```

### Comparing `dask_sql-2023.2.0/dask_planner/src/sql/parser_utils.rs` & `dask_sql-2023.4.0/dask_planner/src/sql/parser_utils.rs`

 * *Files identical despite different names*

### Comparing `dask_sql-2023.2.0/dask_planner/src/sql/schema.rs` & `dask_sql-2023.4.0/dask_planner/src/sql/schema.rs`

 * *Files identical despite different names*

### Comparing `dask_sql-2023.2.0/dask_planner/src/sql/statement.rs` & `dask_sql-2023.4.0/dask_planner/src/sql/statement.rs`

 * *Files identical despite different names*

### Comparing `dask_sql-2023.2.0/dask_planner/src/sql/table.rs` & `dask_sql-2023.4.0/dask_planner/src/sql/table.rs`

 * *Files 14% similar despite different names*

```diff
@@ -1,11 +1,11 @@
 use std::{any::Any, sync::Arc};
 
-use arrow::datatypes::{DataType, Field, SchemaRef};
 use async_trait::async_trait;
+use datafusion::arrow::datatypes::{DataType, Field, SchemaRef};
 use datafusion_common::DFField;
 use datafusion_expr::{Expr, LogicalPlan, TableProviderFilterPushDown, TableSource};
 use datafusion_optimizer::utils::split_conjunction;
 use datafusion_sql::TableReference;
 use pyo3::prelude::*;
 
 use super::logical::{create_table::CreateTablePlanNode, predict_model::PredictModelPlanNode};
@@ -21,20 +21,41 @@
         },
     },
 };
 
 /// DaskTable wrapper that is compatible with DataFusion logical query plans
 pub struct DaskTableSource {
     schema: SchemaRef,
+    statistics: Option<DaskStatistics>,
+    filepath: Option<String>,
 }
 
 impl DaskTableSource {
-    /// Initialize a new `EmptyTable` from a schema.
-    pub fn new(schema: SchemaRef) -> Self {
-        Self { schema }
+    /// Initialize a new `EmptyTable` from a schema
+    pub fn new(
+        schema: SchemaRef,
+        statistics: Option<DaskStatistics>,
+        filepath: Option<String>,
+    ) -> Self {
+        Self {
+            schema,
+            statistics,
+            filepath,
+        }
+    }
+
+    /// Access optional statistics associated with this table source
+    pub fn statistics(&self) -> Option<&DaskStatistics> {
+        self.statistics.as_ref()
+    }
+
+    /// Access optional filepath associated with this table source
+    #[allow(dead_code)]
+    pub fn filepath(&self) -> Option<&String> {
+        self.filepath.as_ref()
     }
 }
 
 /// Implement TableSource, used in the logical query plan and in logical query optimizations
 #[async_trait]
 impl TableSource for DaskTableSource {
     fn as_any(&self) -> &dyn Any {
@@ -67,45 +88,56 @@
     // For now we support all kinds of expr's at this level
     true
 }
 
 #[pyclass(name = "DaskStatistics", module = "dask_planner", subclass)]
 #[derive(Debug, Clone)]
 pub struct DaskStatistics {
-    #[allow(dead_code)]
     row_count: f64,
 }
 
 #[pymethods]
 impl DaskStatistics {
     #[new]
     pub fn new(row_count: f64) -> Self {
         Self { row_count }
     }
+
+    #[pyo3(name = "getRowCount")]
+    pub fn get_row_count(&self) -> f64 {
+        self.row_count
+    }
 }
 
 #[pyclass(name = "DaskTable", module = "dask_planner", subclass)]
 #[derive(Debug, Clone)]
 pub struct DaskTable {
     pub(crate) schema_name: Option<String>,
     pub(crate) table_name: String,
-    #[allow(dead_code)]
     pub(crate) statistics: DaskStatistics,
     pub(crate) columns: Vec<(String, DaskTypeMap)>,
+    pub(crate) filepath: Option<String>,
 }
 
 #[pymethods]
 impl DaskTable {
     #[new]
-    pub fn new(schema_name: &str, table_name: &str, row_count: f64) -> Self {
+    pub fn new(
+        schema_name: &str,
+        table_name: &str,
+        row_count: f64,
+        columns: Option<Vec<(String, DaskTypeMap)>>,
+        filepath: Option<String>,
+    ) -> Self {
         Self {
             schema_name: Some(schema_name.to_owned()),
             table_name: table_name.to_owned(),
             statistics: DaskStatistics::new(row_count),
-            columns: Vec::new(),
+            columns: columns.unwrap_or_default(),
+            filepath,
         }
     }
 
     // TODO: Really wish we could accept a SqlTypeName instance here instead of a String for `column_type` ....
     #[pyo3(name = "add_column")]
     pub fn add_column(&mut self, column_name: &str, type_map: DaskTypeMap) {
         self.columns.push((column_name.to_owned(), type_map));
@@ -152,15 +184,15 @@
 
 /// Traverses the logical plan to locate the Table associated with the query
 pub(crate) fn table_from_logical_plan(
     plan: &LogicalPlan,
 ) -> Result<Option<DaskTable>, DaskPlannerError> {
     match plan {
         LogicalPlan::Projection(projection) => table_from_logical_plan(&projection.input),
-        LogicalPlan::Filter(filter) => table_from_logical_plan(filter.input()),
+        LogicalPlan::Filter(filter) => table_from_logical_plan(&filter.input),
         LogicalPlan::TableScan(table_scan) => {
             // Get the TableProvider for this Table instance
             let tbl_provider: Arc<dyn TableSource> = table_scan.source.clone();
             let tbl_schema: SchemaRef = tbl_provider.schema();
             let fields: &Vec<Field> = tbl_schema.fields();
 
             let mut cols: Vec<(String, DaskTypeMap)> = Vec::new();
@@ -173,32 +205,33 @@
                         data_type.clone().into(),
                     ),
                 ));
             }
 
             let table_ref: TableReference = table_scan.table_name.as_str().into();
             let (schema, tbl) = match table_ref {
-                TableReference::Bare { table } => ("", table),
-                TableReference::Partial { schema, table } => (schema, table),
+                TableReference::Bare { table } => ("".to_string(), table),
+                TableReference::Partial { schema, table } => (schema.to_string(), table),
                 TableReference::Full {
                     catalog: _,
                     schema,
                     table,
-                } => (schema, table),
+                } => (schema.to_string(), table),
             };
 
             Ok(Some(DaskTable {
-                schema_name: Some(String::from(schema)),
+                schema_name: Some(schema),
                 table_name: String::from(tbl),
                 statistics: DaskStatistics { row_count: 0.0 },
                 columns: cols,
+                filepath: None,
             }))
         }
         LogicalPlan::Join(join) => {
-            //TODO: Don't always hardcode the left
+            // TODO: Don't always hardcode the left
             table_from_logical_plan(&join.left)
         }
         LogicalPlan::Aggregate(agg) => table_from_logical_plan(&agg.input),
         LogicalPlan::SubqueryAlias(alias) => table_from_logical_plan(&alias.input),
         LogicalPlan::EmptyRelation(empty_relation) => {
             let fields: &Vec<DFField> = empty_relation.schema.fields();
 
@@ -215,31 +248,34 @@
             }
 
             Ok(Some(DaskTable {
                 schema_name: Some(String::from("EmptySchema")),
                 table_name: String::from("EmptyRelation"),
                 statistics: DaskStatistics { row_count: 0.0 },
                 columns: cols,
+                filepath: None,
             }))
         }
         LogicalPlan::Extension(ex) => {
             let node = ex.node.as_any();
             if let Some(e) = node.downcast_ref::<CreateTablePlanNode>() {
                 Ok(Some(DaskTable {
                     schema_name: e.schema_name.clone(),
                     table_name: e.table_name.clone(),
                     statistics: DaskStatistics { row_count: 0.0 },
                     columns: vec![],
+                    filepath: None,
                 }))
             } else if let Some(e) = node.downcast_ref::<PredictModelPlanNode>() {
                 Ok(Some(DaskTable {
                     schema_name: e.schema_name.clone(),
                     table_name: e.model_name.clone(),
                     statistics: DaskStatistics { row_count: 0.0 },
                     columns: vec![],
+                    filepath: None,
                 }))
             } else {
                 Err(DaskPlannerError::Internal(format!(
                     "table_from_logical_plan: unimplemented LogicalPlan type {plan:?} encountered"
                 )))
             }
         }
```

### Comparing `dask_sql-2023.2.0/dask_planner/src/sql/types/rel_data_type.rs` & `dask_sql-2023.4.0/dask_planner/src/sql/types/rel_data_type.rs`

 * *Files identical despite different names*

### Comparing `dask_sql-2023.2.0/dask_planner/src/sql/types/rel_data_type_field.rs` & `dask_sql-2023.4.0/dask_planner/src/sql/types/rel_data_type_field.rs`

 * *Files identical despite different names*

### Comparing `dask_sql-2023.2.0/dask_planner/src/sql/types.rs` & `dask_sql-2023.4.0/dask_planner/src/sql/types.rs`

 * *Files 1% similar despite different names*

```diff
@@ -1,23 +1,24 @@
 pub mod rel_data_type;
 pub mod rel_data_type_field;
 
-use arrow::datatypes::{DataType, IntervalUnit, TimeUnit};
+use datafusion::arrow::datatypes::{DataType, IntervalUnit, TimeUnit};
 use datafusion_sql::sqlparser::{ast::DataType as SQLType, parser::Parser, tokenizer::Tokenizer};
 use pyo3::{prelude::*, types::PyDict};
 
 use crate::{dialect::DaskDialect, error::DaskPlannerError};
 
 #[derive(Debug, Clone, PartialEq, Eq, Hash, PartialOrd, Ord)]
 #[pyclass(name = "RexType", module = "datafusion")]
 pub enum RexType {
+    Alias,
     Literal,
     Call,
     Reference,
-    SubqueryAlias,
+    ScalarSubquery,
     Other,
 }
 
 #[derive(Debug, Clone, PartialEq, Eq, Hash, PartialOrd, Ord)]
 #[pyclass(name = "DaskTypeMap", module = "datafusion", subclass)]
 /// Represents a Python Data Type. This is needed instead of simple
 /// Enum instances because PyO3 can only support unit variants as
@@ -115,14 +116,18 @@
 
         Ok(DaskTypeMap {
             sql_type,
             data_type: d_type.into(),
         })
     }
 
+    fn __str__(&self) -> String {
+        format!("{:?}", self.sql_type)
+    }
+
     #[pyo3(name = "getSqlType")]
     pub fn sql_type(&self) -> SqlTypeName {
         self.sql_type.clone()
     }
 
     #[pyo3(name = "getDataType")]
     pub fn data_type(&self) -> PyDataType {
@@ -331,15 +336,15 @@
             "DYNAMIC_STAT" => Ok(SqlTypeName::DYNAMIC_STAR),
             "UNKNOWN" => Ok(SqlTypeName::UNKNOWN),
             _ => {
                 // complex data type name so use the sqlparser
                 let dialect = DaskDialect {};
                 let mut tokenizer = Tokenizer::new(&dialect, input_type);
                 let tokens = tokenizer.tokenize().map_err(DaskPlannerError::from)?;
-                let mut parser = Parser::new(tokens, &dialect);
+                let mut parser = Parser::new(&dialect).with_tokens(tokens);
                 match parser.parse_data_type().map_err(DaskPlannerError::from)? {
                     SQLType::Decimal(_) => Ok(SqlTypeName::DECIMAL),
                     SQLType::Binary(_) => Ok(SqlTypeName::BINARY),
                     SQLType::Varbinary(_) => Ok(SqlTypeName::VARBINARY),
                     SQLType::Varchar(_) | SQLType::Nvarchar(_) => Ok(SqlTypeName::VARCHAR),
                     SQLType::Char(_) => Ok(SqlTypeName::CHAR),
                     _ => Err(DaskPlannerError::Internal(format!(
```

### Comparing `dask_sql-2023.2.0/dask_planner/src/sql.rs` & `dask_sql-2023.4.0/dask_planner/src/sql.rs`

 * *Files 2% similar despite different names*

```diff
@@ -7,16 +7,16 @@
 pub mod schema;
 pub mod statement;
 pub mod table;
 pub mod types;
 
 use std::{collections::HashMap, sync::Arc};
 
-use arrow::datatypes::{DataType, Field, Schema, TimeUnit};
-use datafusion_common::{DFSchema, DataFusionError, ScalarValue};
+use datafusion::arrow::datatypes::{DataType, Field, Schema, TimeUnit};
+use datafusion_common::{config::ConfigOptions, DFSchema, DataFusionError};
 use datafusion_expr::{
     logical_plan::Extension,
     AccumulatorFunctionImplementation,
     AggregateUDF,
     LogicalPlan,
     PlanVisitor,
     ReturnTypeFunction,
@@ -30,14 +30,15 @@
 };
 use datafusion_sql::{
     parser::Statement as DFStatement,
     planner::{ContextProvider, SqlToRel},
     ResolvedTableReference,
     TableReference,
 };
+use log::{debug, warn};
 use pyo3::prelude::*;
 
 use self::logical::{
     create_catalog_schema::CreateCatalogSchemaPlanNode,
     drop_schema::DropSchemaPlanNode,
     use_schema::UseSchemaPlanNode,
 };
@@ -55,15 +56,15 @@
             create_table::CreateTablePlanNode,
             describe_model::DescribeModelPlanNode,
             drop_model::DropModelPlanNode,
             export_model::ExportModelPlanNode,
             predict_model::PredictModelPlanNode,
             show_columns::ShowColumnsPlanNode,
             show_models::ShowModelsPlanNode,
-            show_schema::ShowSchemasPlanNode,
+            show_schemas::ShowSchemasPlanNode,
             show_tables::ShowTablesPlanNode,
             PyLogicalPlan,
         },
     },
 };
 
 /// DaskSQLContext is main interface used for interacting with DataFusion to
@@ -87,31 +88,34 @@
 /// ```
 #[pyclass(name = "DaskSQLContext", module = "dask_planner", subclass)]
 #[derive(Debug, Clone)]
 pub struct DaskSQLContext {
     current_catalog: String,
     current_schema: String,
     schemas: HashMap<String, schema::DaskSchema>,
+    options: ConfigOptions,
 }
 
 impl ContextProvider for DaskSQLContext {
     fn get_table_provider(
         &self,
         name: TableReference,
     ) -> Result<Arc<dyn TableSource>, DataFusionError> {
-        let reference: ResolvedTableReference =
-            name.resolve(&self.current_catalog, &self.current_schema);
+        let reference: ResolvedTableReference = name
+            .clone()
+            .resolve(&self.current_catalog, &self.current_schema);
         if reference.catalog != self.current_catalog {
             // there is a single catalog in Dask SQL
             return Err(DataFusionError::Plan(format!(
                 "Cannot resolve catalog '{}'",
                 reference.catalog
             )));
         }
-        match self.schemas.get(reference.schema) {
+        let schema_name = reference.clone().schema.into_owned();
+        match self.schemas.get(&schema_name) {
             Some(schema) => {
                 let mut resp = None;
                 for table in schema.tables.values() {
                     if table.table_name.eq(&name.table()) {
                         // Build the Schema here
                         let mut fields: Vec<Field> = Vec::new();
                         // Iterate through the DaskTable instance and create a Schema instance
@@ -125,15 +129,38 @@
 
                         resp = Some(Schema::new(fields));
                     }
                 }
 
                 // If the Table is not found return None. DataFusion will handle the error propagation
                 match resp {
-                    Some(e) => Ok(Arc::new(table::DaskTableSource::new(Arc::new(e)))),
+                    Some(e) => {
+                        let table_ref = &self
+                            .schemas
+                            .get(reference.schema.as_ref())
+                            .unwrap()
+                            .tables
+                            .get(reference.table.as_ref())
+                            .unwrap();
+                        let statistics = &table_ref.statistics;
+                        let filepath = &table_ref.filepath;
+                        if statistics.get_row_count() == 0.0 {
+                            Ok(Arc::new(table::DaskTableSource::new(
+                                Arc::new(e),
+                                None,
+                                filepath.clone(),
+                            )))
+                        } else {
+                            Ok(Arc::new(table::DaskTableSource::new(
+                                Arc::new(e),
+                                Some(statistics.clone()),
+                                filepath.clone(),
+                            )))
+                        }
+                    }
                     None => Err(DataFusionError::Plan(format!(
                         "Table '{}.{}.{}' not found",
                         reference.catalog, reference.schema, reference.table
                     ))),
                 }
             }
             None => Err(DataFusionError::Plan(format!(
@@ -392,27 +419,28 @@
         None
     }
 
     fn get_variable_type(&self, _: &[String]) -> Option<DataType> {
         unimplemented!("RUST: get_variable_type is not yet implemented for DaskSQLContext")
     }
 
-    fn get_config_option(&self, _option: &str) -> Option<ScalarValue> {
-        None
+    fn options(&self) -> &ConfigOptions {
+        &self.options
     }
 }
 
 #[pymethods]
 impl DaskSQLContext {
     #[new]
     pub fn new(default_catalog_name: &str, default_schema_name: &str) -> Self {
         Self {
             current_catalog: default_catalog_name.to_owned(),
             current_schema: default_schema_name.to_owned(),
             schemas: HashMap::new(),
+            options: ConfigOptions::new(),
         }
     }
 
     /// Change the current schema
     pub fn use_schema(&mut self, schema_name: &str) -> PyResult<()> {
         if self.schemas.contains_key(schema_name) {
             self.current_schema = schema_name.to_owned();
@@ -449,14 +477,15 @@
                 "Schema: {schema_name} not found in DaskSQLContext"
             ))),
         }
     }
 
     /// Parses a SQL string into an AST presented as a Vec of Statements
     pub fn parse_sql(&self, sql: &str) -> PyResult<Vec<statement::PyStatement>> {
+        debug!("parse_sql - '{}'", sql);
         let dd: DaskDialect = DaskDialect {};
         match DaskParser::parse_sql_with_dialect(sql, &dd) {
             Ok(k) => {
                 let mut statements: Vec<statement::PyStatement> = Vec::new();
                 for statement in k {
                     statements.push(statement.into());
                 }
@@ -488,23 +517,24 @@
     ) -> PyResult<logical::PyLogicalPlan> {
         // Certain queries cannot be optimized. Ex: `EXPLAIN SELECT * FROM test` simply return those plans as is
         let mut visitor = OptimizablePlanVisitor {};
 
         match existing_plan.original_plan.accept(&mut visitor) {
             Ok(valid) => {
                 if valid {
-                    optimizer::DaskSqlOptimizer::new(true)
+                    optimizer::DaskSqlOptimizer::new()
                         .optimize(existing_plan.original_plan)
                         .map(|k| PyLogicalPlan {
                             original_plan: k,
                             current_node: None,
                         })
                         .map_err(py_optimization_exp)
                 } else {
                     // This LogicalPlan does not support Optimization. Return original
+                    warn!("This LogicalPlan does not support Optimization. Returning original");
                     Ok(existing_plan)
                 }
             }
             Err(e) => Err(py_optimization_exp(e)),
         }
     }
 }
@@ -592,20 +622,22 @@
                     if_exists: drop_model.if_exists,
                     schema: Arc::new(DFSchema::empty()),
                 }),
             })),
             DaskStatement::ShowSchemas(show_schemas) => Ok(LogicalPlan::Extension(Extension {
                 node: Arc::new(ShowSchemasPlanNode {
                     schema: Arc::new(DFSchema::empty()),
+                    catalog_name: show_schemas.catalog_name,
                     like: show_schemas.like,
                 }),
             })),
             DaskStatement::ShowTables(show_tables) => Ok(LogicalPlan::Extension(Extension {
                 node: Arc::new(ShowTablesPlanNode {
                     schema: Arc::new(DFSchema::empty()),
+                    catalog_name: show_tables.catalog_name,
                     schema_name: show_tables.schema_name,
                 }),
             })),
             DaskStatement::ShowColumns(show_columns) => Ok(LogicalPlan::Extension(Extension {
                 node: Arc::new(ShowColumnsPlanNode {
                     schema: Arc::new(DFSchema::empty()),
                     table_name: show_columns.table_name,
@@ -707,15 +739,15 @@
     }
 
     Signature::one_of(one_of_vector.clone(), Volatility::Immutable)
 }
 
 #[cfg(test)]
 mod test {
-    use arrow::datatypes::DataType;
+    use datafusion::arrow::datatypes::DataType;
     use datafusion_expr::{Signature, TypeSignature, Volatility};
 
     use crate::sql::generate_signatures;
 
     #[test]
     fn test_generate_signatures() {
         let sig = generate_signatures(vec![
```

### Comparing `dask_sql-2023.2.0/dask_sql/_compat.py` & `dask_sql-2023.4.0/dask_sql/_compat.py`

 * *Files identical despite different names*

### Comparing `dask_sql-2023.2.0/dask_sql/cmd.py` & `dask_sql-2023.4.0/dask_sql/cmd.py`

 * *Files identical despite different names*

### Comparing `dask_sql-2023.2.0/dask_sql/context.py` & `dask_sql-2023.4.0/dask_sql/context.py`

 * *Files 5% similar despite different names*

```diff
@@ -1,30 +1,33 @@
 import asyncio
 import inspect
 import logging
-import warnings
 from collections import Counter
 from typing import Any, Callable, Dict, List, Tuple, Union
 
 import dask.dataframe as dd
 import pandas as pd
 from dask import config as dask_config
 from dask.base import optimize
-from dask.distributed import Client
 
 from dask_planner.rust import (
     DaskSchema,
     DaskSQLContext,
     DaskTable,
     DFOptimizationException,
     DFParsingException,
     LogicalPlan,
 )
 
 try:
+    from dask_sql.physical.utils.statistics import parquet_statistics
+except ModuleNotFoundError:
+    parquet_statistics = None
+
+try:
     import dask_cuda  # noqa: F401
 except ImportError:  # pragma: no cover
     pass
 
 from dask_sql import input_utils
 from dask_sql.datacontainer import (
     UDF,
@@ -131,18 +134,19 @@
         RelConverter.add_plugin_class(custom.ShowSchemasPlugin, replace=False)
         RelConverter.add_plugin_class(custom.ShowTablesPlugin, replace=False)
         RelConverter.add_plugin_class(custom.UseSchemaPlugin, replace=False)
         RelConverter.add_plugin_class(custom.AlterSchemaPlugin, replace=False)
         RelConverter.add_plugin_class(custom.AlterTablePlugin, replace=False)
         RelConverter.add_plugin_class(custom.DistributeByPlugin, replace=False)
 
+        RexConverter.add_plugin_class(core.RexAliasPlugin, replace=False)
         RexConverter.add_plugin_class(core.RexCallPlugin, replace=False)
         RexConverter.add_plugin_class(core.RexInputRefPlugin, replace=False)
         RexConverter.add_plugin_class(core.RexLiteralPlugin, replace=False)
-        RexConverter.add_plugin_class(core.RexSubqueryAliasPlugin, replace=False)
+        RexConverter.add_plugin_class(core.RexScalarSubqueryPlugin, replace=False)
 
         InputUtil.add_plugin_class(input_utils.DaskInputPlugin, replace=False)
         InputUtil.add_plugin_class(input_utils.PandasLikeInputPlugin, replace=False)
         InputUtil.add_plugin_class(input_utils.HiveInputPlugin, replace=False)
         InputUtil.add_plugin_class(input_utils.IntakeCatalogInputPlugin, replace=False)
         InputUtil.add_plugin_class(input_utils.SqlalchemyHiveInputPlugin, replace=False)
         # needs to be the last entry, as it only checks for string
@@ -215,57 +219,52 @@
                 The data frame/location/hive connection to register.
             format (:obj:`str`): Only used when passing a string into the ``input`` parameter.
                 Specify the file format directly here if it can not be deduced from the extension.
                 If set to "memory", load the data from a published dataset in the dask cluster.
             persist (:obj:`bool`): Only used when passing a string into the ``input`` parameter.
                 Set to true to turn on loading the file data directly into memory.
             schema_name: (:obj:`str`): in which schema to create the table. By default, will use the currently selected schema.
-            statistics: (:obj:`Statistics`): if given, use these statistics during the cost-based optimization. If no
-                statistics are provided, we will just assume 100 rows.
+            statistics: (:obj:`Statistics`): if given, use these statistics during the cost-based optimization.
             gpu: (:obj:`bool`): if set to true, use dask-cudf to run the data frame calculations on your GPU.
                 Please note that the GPU support is currently not covering all of dask-sql's SQL language.
             **kwargs: Additional arguments for specific formats. See :ref:`data_input` for more information.
 
         """
         logger.debug(
             f"Creating table: '{table_name}' of format type '{format}' in schema '{schema_name}'"
         )
-        if "file_format" in kwargs:  # pragma: no cover
-            warnings.warn("file_format is renamed to format", DeprecationWarning)
-            format = kwargs.pop("file_format")
 
         schema_name = schema_name or self.schema_name
 
         dc = InputUtil.to_dc(
             input_table,
             table_name=table_name,
             format=format,
             persist=persist,
             gpu=gpu,
             **kwargs,
         )
 
-        self.schema[schema_name].tables[table_name.lower()] = dc
-        if statistics:
-            self.schema[schema_name].statistics[table_name.lower()] = statistics
-
-        # Register the table with the Rust DaskSQLContext
-        self.context.register_table(
-            schema_name, DaskTable(schema_name, table_name, 100)
-        )
+        if type(input_table) == str:
+            dc.filepath = input_table
+            self.schema[schema_name].filepaths[table_name.lower()] = input_table
+
+        if parquet_statistics and not statistics:
+            statistics = parquet_statistics(dc.df)
+            if statistics:
+                row_count = 0
+                for d in statistics:
+                    row_count += d["num-rows"]
+                statistics = Statistics(row_count)
+        if not statistics:
+            statistics = Statistics(float("nan"))
+        dc.statistics = statistics
 
-    def register_dask_table(self, df: dd.DataFrame, name: str, *args, **kwargs):
-        """
-        Outdated version of :func:`create_table()`.
-        """
-        warnings.warn(
-            "register_dask_table is deprecated, use the more general create_table instead.",
-            DeprecationWarning,
-        )
-        return self.create_table(name, df, *args, **kwargs)
+        self.schema[schema_name].tables[table_name.lower()] = dc
+        self.schema[schema_name].statistics[table_name.lower()] = statistics
 
     def drop_table(self, table_name: str, schema_name: str = None):
         """
         Remove a table with the given name from the registered tables.
         This will also delete the dataframe.
 
         Args:
@@ -460,19 +459,22 @@
     ) -> Union[dd.DataFrame, pd.DataFrame]:
         """
         Query the registered tables with the given SQL.
         The SQL follows approximately the postgreSQL standard - however, not all
         operations are already implemented.
         In general, only select statements (no data manipulation) works.
         For more information, see :ref:`sql`.
+
         Example:
             In this example, a query is called
             using the registered tables and then
             executed using dask.
+
             .. code-block:: python
+
                 result = c.sql("SELECT a, b FROM my_table")
                 print(result.compute())
         Args:
             sql (:obj:`str`): The query string to execute
             return_futures (:obj:`bool`): Return the unexecuted dask dataframe or the data itself.
                 Defaults to returning the dask dataframe.
             dataframes (:obj:`Dict[str, dask.dataframe.DataFrame]`): additional Dask or pandas dataframes
@@ -660,44 +662,30 @@
                 functionality. If you are working in a classic jupyter notebook,
                 you may set disable_highlighting=False if desired.
         """
         ipython_integration(
             self, auto_include=auto_include, disable_highlighting=disable_highlighting
         )
 
-    def run_server(
-        self,
-        client: Client = None,
-        host: str = "0.0.0.0",
-        port: int = 8080,
-        log_level=None,
-        blocking: bool = True,
-    ):  # pragma: no cover
+    def run_server(self, **kwargs):  # pragma: no cover
         """
         Run a HTTP server for answering SQL queries using ``dask-sql``.
 
         See :ref:`server` for more information.
 
         Args:
             client (:obj:`dask.distributed.Client`): If set, use this dask client instead of a new one.
             host (:obj:`str`): The host interface to listen on (defaults to all interfaces)
             port (:obj:`int`): The port to listen on (defaults to 8080)
             log_level: (:obj:`str`): The log level of the server and dask-sql
         """
         from dask_sql.server.app import run_server
 
         self.stop_server()
-        self.server = run_server(
-            context=self,
-            client=client,
-            host=host,
-            port=port,
-            log_level=log_level,
-            blocking=blocking,
-        )
+        self.server = run_server(**kwargs)
 
     def stop_server(self):  # pragma: no cover
         """
         Stop a SQL server started by ``run_server``.
         """
         if self.sql_server is not None:
             loop = asyncio.get_event_loop()
@@ -743,21 +731,28 @@
             for name, dc in schema.tables.items():
                 row_count = (
                     float(schema.statistics[name].row_count)
                     if name in schema.statistics
                     else float(0)
                 )
 
-                table = DaskTable(schema_name, name, row_count)
+                filepath = schema.filepaths[name] if name in schema.filepaths else None
                 df = dc.df
-
-                for column in df.columns:
-                    data_type = df[column].dtype
-                    sql_data_type = python_to_sql_type(data_type)
-                    table.add_column(column, sql_data_type)
+                columns = df.columns
+                cc = dc.column_container
+                if not dask_config.get("sql.identifier.case_sensitive"):
+                    columns = [col.lower() for col in columns]
+                    cc = cc.rename_handle_duplicates(df.columns, columns)
+                    dc.column_container = cc
+                column_type_mapping = list(
+                    zip(columns, map(python_to_sql_type, df.dtypes))
+                )
+                table = DaskTable(
+                    schema_name, name, row_count, column_type_mapping, filepath
+                )
 
                 rust_schema.add_table(table)
 
             if not schema.functions:
                 logger.debug("No custom functions defined.")
             for function_description in schema.function_lists:
                 name = function_description.name
```

### Comparing `dask_sql-2023.2.0/dask_sql/datacontainer.py` & `dask_sql-2023.4.0/dask_sql/datacontainer.py`

 * *Files 2% similar despite different names*

```diff
@@ -167,14 +167,30 @@
         where <number> is the column index.
         """
         return self.rename(
             columns={str(col): f"{prefix}_{i}" for i, col in enumerate(self.columns)}
         )
 
 
+class Statistics:
+    """
+    Statistics are used during the cost-based optimization.
+    Currently, only the row count is supported, more
+    properties might follow. It needs to be provided by the user.
+    """
+
+    def __init__(self, row_count: int) -> None:
+        self.row_count = row_count
+
+    def __eq__(self, other):
+        if isinstance(other, Statistics):
+            return self.row_count == other.row_count
+        return False
+
+
 class DataContainer:
     """
     In SQL, every column operation or reference is done via
     the column index. Some dask operations, such as grouping,
     joining or concatenating preserve the columns in a different
     order than SQL would expect.
     However, we do not want to change the column data itself
@@ -182,17 +198,25 @@
     but still would like to keep the columns accessible by name and index.
     For this, we add an additional `ColumnContainer` to each dataframe,
     which does all the column mapping between "frontend"
     (what SQL expects, also in the correct order)
     and "backend" (what dask has).
     """
 
-    def __init__(self, df: dd.DataFrame, column_container: ColumnContainer):
+    def __init__(
+        self,
+        df: dd.DataFrame,
+        column_container: ColumnContainer,
+        statistics: Statistics = None,
+        filepath: str = None,
+    ):
         self.df = df
         self.column_container = column_container
+        self.statistics = statistics
+        self.filepath = filepath
 
     def assign(self) -> dd.DataFrame:
         """
         Combine the column mapping with the actual data and return
         a dataframe which has the the columns specified in the
         stored ColumnContainer.
         """
@@ -250,27 +274,17 @@
             return self.func == other.func and self.row_udf == other.row_udf
         return NotImplemented
 
     def __hash__(self):
         return (self.func, self.row_udf).__hash__()
 
 
-class Statistics:
-    """
-    Statistics are used during the cost-based optimization.
-    Currently, only the row count is supported, more
-    properties might follow. It needs to be provided by the user.
-    """
-
-    def __init__(self, row_count: int) -> None:
-        self.row_count = row_count
-
-
 class SchemaContainer:
     def __init__(self, name: str):
         self.__name__ = name
         self.tables: Dict[str, DataContainer] = {}
         self.statistics: Dict[str, Statistics] = {}
         self.experiments: Dict[str, pd.DataFrame] = {}
         self.models: Dict[str, Tuple[Any, List[str]]] = {}
         self.functions: Dict[str, UDF] = {}
         self.function_lists: List[FunctionDescription] = []
+        self.filepaths: Dict[str, str] = {}
```

### Comparing `dask_sql-2023.2.0/dask_sql/input_utils/convert.py` & `dask_sql-2023.4.0/dask_sql/input_utils/convert.py`

 * *Files identical despite different names*

### Comparing `dask_sql-2023.2.0/dask_sql/input_utils/dask.py` & `dask_sql-2023.4.0/dask_sql/input_utils/dask.py`

 * *Files identical despite different names*

### Comparing `dask_sql-2023.2.0/dask_sql/input_utils/hive.py` & `dask_sql-2023.4.0/dask_sql/input_utils/hive.py`

 * *Files identical despite different names*

### Comparing `dask_sql-2023.2.0/dask_sql/input_utils/intake.py` & `dask_sql-2023.4.0/dask_sql/input_utils/intake.py`

 * *Files identical despite different names*

### Comparing `dask_sql-2023.2.0/dask_sql/input_utils/location.py` & `dask_sql-2023.4.0/dask_sql/input_utils/location.py`

 * *Files identical despite different names*

### Comparing `dask_sql-2023.2.0/dask_sql/input_utils/pandaslike.py` & `dask_sql-2023.4.0/dask_sql/input_utils/pandaslike.py`

 * *Files identical despite different names*

### Comparing `dask_sql-2023.2.0/dask_sql/input_utils/sqlalchemy.py` & `dask_sql-2023.4.0/dask_sql/input_utils/sqlalchemy.py`

 * *Files identical despite different names*

### Comparing `dask_sql-2023.2.0/dask_sql/integrations/fugue.py` & `dask_sql-2023.4.0/dask_sql/integrations/fugue.py`

 * *Files 2% similar despite different names*

```diff
@@ -48,14 +48,18 @@
     (on average) slower in computation and scaling.
     """
 
     def __init__(self, *args, **kwargs):
         """Create a new instance."""
         super().__init__(*args, **kwargs)
 
+    @property
+    def is_distributed(self) -> bool:
+        return True
+
     def select(
         self, dfs: fugue.dataframe.DataFrames, statement: str
     ) -> fugue.dataframe.DataFrame:
         """Send the SQL command to the dask-sql context and register all temporary dataframes"""
         c = Context()
 
         for k, v in dfs.items():
```

### Comparing `dask_sql-2023.2.0/dask_sql/integrations/ipython.py` & `dask_sql-2023.4.0/dask_sql/integrations/ipython.py`

 * *Files identical despite different names*

### Comparing `dask_sql-2023.2.0/dask_sql/mappings.py` & `dask_sql-2023.4.0/dask_sql/mappings.py`

 * *Files identical despite different names*

### Comparing `dask_sql-2023.2.0/dask_sql/physical/rel/base.py` & `dask_sql-2023.4.0/dask_sql/physical/rel/base.py`

 * *Files identical despite different names*

### Comparing `dask_sql-2023.2.0/dask_sql/physical/rel/convert.py` & `dask_sql-2023.4.0/dask_sql/physical/rel/convert.py`

 * *Files identical despite different names*

### Comparing `dask_sql-2023.2.0/dask_sql/physical/rel/custom/__init__.py` & `dask_sql-2023.4.0/dask_sql/physical/rel/custom/__init__.py`

 * *Files 0% similar despite different names*

```diff
@@ -8,17 +8,17 @@
 from .describe_model import DescribeModelPlugin
 from .distributeby import DistributeByPlugin
 from .drop_model import DropModelPlugin
 from .drop_schema import DropSchemaPlugin
 from .drop_table import DropTablePlugin
 from .export_model import ExportModelPlugin
 from .predict_model import PredictModelPlugin
-from .schemas import ShowSchemasPlugin
 from .show_columns import ShowColumnsPlugin
 from .show_models import ShowModelsPlugin
+from .show_schemas import ShowSchemasPlugin
 from .show_tables import ShowTablesPlugin
 from .use_schema import UseSchemaPlugin
 
 __all__ = [
     AnalyzeTablePlugin,
     CreateExperimentPlugin,
     CreateModelPlugin,
```

### Comparing `dask_sql-2023.2.0/dask_sql/physical/rel/custom/alter.py` & `dask_sql-2023.4.0/dask_sql/physical/rel/custom/alter.py`

 * *Files identical despite different names*

### Comparing `dask_sql-2023.2.0/dask_sql/physical/rel/custom/analyze_table.py` & `dask_sql-2023.4.0/dask_sql/physical/rel/custom/analyze_table.py`

 * *Files 6% similar despite different names*

```diff
@@ -52,17 +52,15 @@
         )
         statistics = statistics.append(df[[mapping(col) for col in columns]].describe())
 
         # Add additional information
         statistics = statistics.append(
             pd.Series(
                 {
-                    col: str(python_to_sql_type(df[mapping(col)].dtype).getSqlType())
-                    .rpartition(".")[2]
-                    .lower()
+                    col: str(python_to_sql_type(df[mapping(col)].dtype)).lower()
                     for col in columns
                 },
                 name="data_type",
             )
         )
         statistics = statistics.append(
             pd.Series(
```

### Comparing `dask_sql-2023.2.0/dask_sql/physical/rel/custom/create_catalog_schema.py` & `dask_sql-2023.4.0/dask_sql/physical/rel/custom/create_catalog_schema.py`

 * *Files identical despite different names*

### Comparing `dask_sql-2023.2.0/dask_sql/physical/rel/custom/create_experiment.py` & `dask_sql-2023.4.0/dask_sql/physical/rel/custom/create_experiment.py`

 * *Files 6% similar despite different names*

```diff
@@ -27,20 +27,27 @@
     which can be used for prediction
 
     sql syntax:
         CREATE EXPERIMENT <name> WITH ( key = value )
             AS <some select query>
 
     OPTIONS:
-    * model_class: Full path to the class of the model which has to be tuned.
+    * model_class: Class name or full path to the class of the model to train.
+      Any sklearn, cuML, XGBoost, or LightGBM classes can be inferred
+      without the full path. In this case, models trained on cuDF dataframes
+      are automatically mapped to cuML classes, and sklearn models otherwise.
+      We map to cuML-Dask based models when possible and single-GPU cuML models otherwise.
       Any model class with sklearn interface is valid, but might or
       might not work well with Dask dataframes.
       You might need to install necessary packages to use
       the models.
-    * experiment_class : Full path of the Hyperparameter tuner
+    * experiment_class : Class name or full path of the Hyperparameter tuner.
+      Any sklearn or cuML classes can be inferred
+      without the full path. In this case, models trained on cuDF dataframes
+      are automatically mapped to cuML classes, and sklearn models otherwise.
     * tune_parameters:
       Key-value of pairs of Hyperparameters to tune, i.e Search Space for
       particular model to tune
     * automl_class : Full path of the class which is sklearn compatible and
       able to distribute work to dask clusters, currently tested with
       tpot automl framework.
       Refer : [Tpot example](https://examples.dask.org/machine-learning/tpot.html)
```

### Comparing `dask_sql-2023.2.0/dask_sql/physical/rel/custom/create_memory_table.py` & `dask_sql-2023.4.0/dask_sql/physical/rel/custom/create_memory_table.py`

 * *Files identical despite different names*

### Comparing `dask_sql-2023.2.0/dask_sql/physical/rel/custom/create_model.py` & `dask_sql-2023.4.0/dask_sql/physical/rel/custom/create_model.py`

 * *Files 3% similar despite different names*

```diff
@@ -30,15 +30,19 @@
             AS <some select query>
 
     It sends the select query through the normal parsing
     and optimization and conversation and uses the result
     as the training input.
 
     The options control, how and which model is trained:
-    * model_class: Full path to the class of the model to train.
+    * model_class: Class name or full path to the class of the model to train.
+      Any sklearn, cuML, XGBoost, or LightGBM classes can be inferred
+      without the full path. In this case, models trained on cuDF dataframes
+      are automatically mapped to cuML classes, and sklearn models otherwise.
+      We map to cuML-Dask based models when possible and single-GPU cuML models otherwise.
       Any model class with sklearn interface is valid, but might or
       might not work well with Dask dataframes.
       You might need to install necessary packages to use
       the models.
     * target_column: Which column from the data to use as target.
       If not empty, it is removed automatically from
       the training data. Defaults to an empty string, in which
@@ -154,24 +158,27 @@
             raise ImportError(
                 f"Failed to import model {model_class}. Make sure it is spelled correctly and the relevant packages are installed."
             )
 
         model = ModelClass(**kwargs)
 
         if wrap_predict is None:
-            if "sklearn" in model_class or (
-                "cuml" in model_class and "cuml.dask" not in model_class
+            if (
+                "sklearn" in model_class
+                or ("cuml" in model_class and "cuml.dask" not in model_class)
+                or ("xgboost" in model_class and "xgboost.dask" not in model_class)
             ):
                 wrap_predict = True
             else:
                 wrap_predict = False
         if wrap_fit is None:
             if (
                 "sklearn" in model_class
                 or ("cuml" in model_class and "cuml.dask" not in model_class)
+                or ("xgboost" in model_class and "xgboost.dask" not in model_class)
             ) and hasattr(model, "partial_fit"):
                 wrap_fit = True
             else:
                 wrap_fit = False
 
         if target_column:
             non_target_columns = [
```

### Comparing `dask_sql-2023.2.0/dask_sql/physical/rel/custom/create_table.py` & `dask_sql-2023.4.0/dask_sql/physical/rel/custom/create_table.py`

 * *Files identical despite different names*

### Comparing `dask_sql-2023.2.0/dask_sql/physical/rel/custom/describe_model.py` & `dask_sql-2023.4.0/dask_sql/physical/rel/custom/describe_model.py`

 * *Files identical despite different names*

### Comparing `dask_sql-2023.2.0/dask_sql/physical/rel/custom/distributeby.py` & `dask_sql-2023.4.0/dask_sql/physical/rel/custom/distributeby.py`

 * *Files identical despite different names*

### Comparing `dask_sql-2023.2.0/dask_sql/physical/rel/custom/drop_model.py` & `dask_sql-2023.4.0/dask_sql/physical/rel/custom/drop_model.py`

 * *Files identical despite different names*

### Comparing `dask_sql-2023.2.0/dask_sql/physical/rel/custom/drop_schema.py` & `dask_sql-2023.4.0/dask_sql/physical/rel/custom/drop_schema.py`

 * *Files identical despite different names*

### Comparing `dask_sql-2023.2.0/dask_sql/physical/rel/custom/drop_table.py` & `dask_sql-2023.4.0/dask_sql/physical/rel/custom/drop_table.py`

 * *Files identical despite different names*

### Comparing `dask_sql-2023.2.0/dask_sql/physical/rel/custom/export_model.py` & `dask_sql-2023.4.0/dask_sql/physical/rel/custom/export_model.py`

 * *Files identical despite different names*

### Comparing `dask_sql-2023.2.0/dask_sql/physical/rel/custom/metrics.py` & `dask_sql-2023.4.0/dask_sql/physical/rel/custom/metrics.py`

 * *Files identical despite different names*

### Comparing `dask_sql-2023.2.0/dask_sql/physical/rel/custom/predict_model.py` & `dask_sql-2023.4.0/dask_sql/physical/rel/custom/predict_model.py`

 * *Files identical despite different names*

### Comparing `dask_sql-2023.2.0/dask_sql/physical/rel/custom/schemas.py` & `dask_sql-2023.4.0/dask_sql/physical/rel/custom/show_columns.py`

 * *Files 24% similar despite different names*

```diff
@@ -1,42 +1,53 @@
 from typing import TYPE_CHECKING
 
 import dask.dataframe as dd
 import pandas as pd
 
 from dask_sql.datacontainer import ColumnContainer, DataContainer
+from dask_sql.mappings import python_to_sql_type
 from dask_sql.physical.rel.base import BaseRelPlugin
 
 if TYPE_CHECKING:
     import dask_sql
     from dask_planner import LogicalPlan
 
 
-class ShowSchemasPlugin(BaseRelPlugin):
+class ShowColumnsPlugin(BaseRelPlugin):
     """
-    Show all schemas.
+    Show all columns (and their types) for a given table.
     The SQL is:
 
-        SHOW SCHEMAS
+        SHOW COLUMNS FROM <table>
 
     The result is also a table, although it is created on the fly.
     """
 
-    class_name = "ShowSchemas"
+    class_name = "ShowColumns"
 
     def convert(self, rel: "LogicalPlan", context: "dask_sql.Context") -> DataContainer:
+        show_columns = rel.show_columns()
 
-        show_schemas = rel.show_schemas()
+        schema_name = show_columns.getSchemaName() or context.schema_name
+        table_name = show_columns.getTableName()
 
-        # "information_schema" is a schema which is found in every presto database
-        schemas = list(context.schema.keys())
-        schemas.append("information_schema")
-        df = pd.DataFrame({"Schema": schemas})
-
-        # We currently do not use the passed additional parameter FROM.
-        like = str(show_schemas.getLike()).strip("'")
-        if like and like != "None":
-            df = df[df.Schema == like]
+        dc = context.schema[schema_name].tables[table_name]
+
+        cols = dc.column_container.columns
+        dtypes = list(
+            map(
+                lambda x: str(python_to_sql_type(x)).lower(),
+                dc.df.dtypes,
+            )
+        )
+        df = pd.DataFrame(
+            {
+                "Column": cols,
+                "Type": dtypes,
+                "Extra": [""] * len(cols),
+                "Comment": [""] * len(cols),
+            }
+        )
 
         cc = ColumnContainer(df.columns)
         dc = DataContainer(dd.from_pandas(df, npartitions=1), cc)
         return dc
```

### Comparing `dask_sql-2023.2.0/dask_sql/physical/rel/custom/show_models.py` & `dask_sql-2023.4.0/dask_sql/physical/rel/custom/show_models.py`

 * *Files identical despite different names*

### Comparing `dask_sql-2023.2.0/dask_sql/physical/rel/custom/show_tables.py` & `dask_sql-2023.4.0/dask_sql/physical/rel/custom/show_tables.py`

 * *Files 18% similar despite different names*

```diff
@@ -12,26 +12,35 @@
 
 
 class ShowTablesPlugin(BaseRelPlugin):
     """
     Show all tables currently defined for a given schema.
     The SQL is:
 
-        SHOW TABLES FROM <schema>
+        SHOW TABLES FROM [<catalog>.]<schema>
 
     Please note that dask-sql currently
     only allows for a single schema (called "schema").
 
     The result is also a table, although it is created on the fly.
     """
 
     class_name = "ShowTables"
 
     def convert(self, rel: "LogicalPlan", context: "dask_sql.Context") -> DataContainer:
-        schema_name = rel.show_tables().getSchemaName() or context.schema_name
+        show_tables = rel.show_tables()
+
+        # currently catalogs other than the default `dask_sql` are not supported
+        catalog_name = show_tables.getCatalogName() or context.catalog_name
+        if catalog_name != context.catalog_name:
+            raise RuntimeError(
+                f"A catalog with the name {catalog_name} is not present."
+            )
+
+        schema_name = show_tables.getSchemaName() or context.schema_name
 
         if schema_name not in context.schema:
             raise AttributeError(f"Schema {schema_name} is not defined.")
 
         df = pd.DataFrame({"Table": list(context.schema[schema_name].tables.keys())})
 
         cc = ColumnContainer(df.columns)
```

### Comparing `dask_sql-2023.2.0/dask_sql/physical/rel/custom/use_schema.py` & `dask_sql-2023.4.0/dask_sql/physical/rel/custom/use_schema.py`

 * *Files identical despite different names*

### Comparing `dask_sql-2023.2.0/dask_sql/physical/rel/custom/wrappers.py` & `dask_sql-2023.4.0/dask_sql/physical/rel/custom/wrappers.py`

 * *Files identical despite different names*

### Comparing `dask_sql-2023.2.0/dask_sql/physical/rel/logical/__init__.py` & `dask_sql-2023.4.0/dask_sql/physical/rel/logical/__init__.py`

 * *Files identical despite different names*

### Comparing `dask_sql-2023.2.0/dask_sql/physical/rel/logical/aggregate.py` & `dask_sql-2023.4.0/dask_sql/physical/rel/logical/aggregate.py`

 * *Files identical despite different names*

### Comparing `dask_sql-2023.2.0/dask_sql/physical/rel/logical/cross_join.py` & `dask_sql-2023.4.0/dask_sql/physical/rel/logical/cross_join.py`

 * *Files 6% similar despite different names*

```diff
@@ -1,12 +1,10 @@
 import logging
 from typing import TYPE_CHECKING
 
-import dask.dataframe as dd
-
 import dask_sql.utils as utils
 from dask_sql.datacontainer import ColumnContainer, DataContainer
 from dask_sql.physical.rel.base import BaseRelPlugin
 
 if TYPE_CHECKING:
     import dask_sql
     from dask_planner.rust import LogicalPlan
@@ -32,12 +30,12 @@
         df_rhs = dc_rhs.df
 
         # Create a 'key' column in both DataFrames to join on
         cross_join_key = utils.new_temporary_column(df_lhs)
         df_lhs[cross_join_key] = 1
         df_rhs[cross_join_key] = 1
 
-        result = dd.merge(df_lhs, df_rhs, on=cross_join_key, suffixes=("", "0")).drop(
+        result = df_lhs.merge(df_rhs, on=cross_join_key, suffixes=("", "0")).drop(
             cross_join_key, 1
         )
 
         return DataContainer(result, ColumnContainer(result.columns))
```

### Comparing `dask_sql-2023.2.0/dask_sql/physical/rel/logical/empty.py` & `dask_sql-2023.4.0/dask_sql/physical/rel/logical/empty.py`

 * *Files identical despite different names*

### Comparing `dask_sql-2023.2.0/dask_sql/physical/rel/logical/filter.py` & `dask_sql-2023.4.0/dask_sql/physical/rel/logical/filter.py`

 * *Files identical despite different names*

### Comparing `dask_sql-2023.2.0/dask_sql/physical/rel/logical/join.py` & `dask_sql-2023.4.0/dask_sql/physical/rel/logical/join.py`

 * *Files 4% similar despite different names*

```diff
@@ -82,25 +82,35 @@
         # In the second case we do a merge on all the a = b,
         # and then apply a filter using the other expressions.
         # In all other cases, we need to do a full table cross join and filter afterwards.
         # As this is probably non-sense for large tables, but there is no other
         # known solution so far.
 
         join_condition = join.getCondition()
-        lhs_on, rhs_on, filter_condition = self._split_join_condition(join_condition)
+        lhs_on, rhs_on, filter_condition = None, None, None
+        # A user can write certain queries that really should be `cross join` queries
+        # that will still enter this portion of the logic. IF the join_condition is
+        # None that means there are no conditions to join on. This means a cross join.
+        # By not entering this body during that condition we ensure that later on in
+        # processing we perform a cross join.
+        if join_condition is not None:
+            lhs_on, rhs_on, filter_condition = self._split_join_condition(
+                join_condition
+            )
+
+            # lhs_on and rhs_on are the indices of the columns to merge on.
+            # The given column indices are for the full, merged table which consists
+            # of lhs and rhs put side-by-side (in this order)
+            # We therefore need to normalize the rhs indices relative to the rhs table.
+            rhs_on = [index - len(df_lhs_renamed.columns) for index in rhs_on]
+
+            # 4. dask can only merge on the same column names.
+            # We therefore create new columns on purpose, which have a distinct name.
+            assert len(lhs_on) == len(rhs_on)
 
-        # lhs_on and rhs_on are the indices of the columns to merge on.
-        # The given column indices are for the full, merged table which consists
-        # of lhs and rhs put side-by-side (in this order)
-        # We therefore need to normalize the rhs indices relative to the rhs table.
-        rhs_on = [index - len(df_lhs_renamed.columns) for index in rhs_on]
-
-        # 4. dask can only merge on the same column names.
-        # We therefore create new columns on purpose, which have a distinct name.
-        assert len(lhs_on) == len(rhs_on)
         if lhs_on:
             # 5. Now we can finally merge on these columns
             # The resulting dataframe will contain all (renamed) columns from the lhs and rhs
             # plus the added columns
             df = self._join_on_columns(
                 df_lhs_renamed,
                 df_rhs_renamed,
@@ -234,26 +244,23 @@
             df_rhs_renamed = df_rhs_renamed[df_rhs_filter]
 
         df_lhs_with_tmp = df_lhs_renamed.assign(**lhs_columns_to_add)
         df_rhs_with_tmp = df_rhs_renamed.assign(**rhs_columns_to_add)
         added_columns = list(lhs_columns_to_add.keys())
 
         broadcast = dask_config.get("sql.join.broadcast")
-        if (
-            not BROADCAST_JOIN_SUPPORT_WORKING
-            and isinstance(broadcast, float)
-            or broadcast
+        if not BROADCAST_JOIN_SUPPORT_WORKING and (
+            isinstance(broadcast, float) or broadcast
         ):
             warnings.warn(
                 "Broadcast Joins may not work as expected with dask<2023.1.1"
                 "For more information refer to https://github.com/dask/dask/issues/9851"
-                "and https://github.com/dask/dask/issues/9870"
+                " and https://github.com/dask/dask/issues/9870"
             )
-        df = dd.merge(
-            df_lhs_with_tmp,
+        df = df_lhs_with_tmp.merge(
             df_rhs_with_tmp,
             on=added_columns,
             how=join_type,
             broadcast=broadcast,
         ).drop(columns=added_columns)
 
         return df
```

### Comparing `dask_sql-2023.2.0/dask_sql/physical/rel/logical/limit.py` & `dask_sql-2023.4.0/dask_sql/physical/rel/logical/limit.py`

 * *Files identical despite different names*

### Comparing `dask_sql-2023.2.0/dask_sql/physical/rel/logical/project.py` & `dask_sql-2023.4.0/dask_sql/physical/rel/logical/project.py`

 * *Files identical despite different names*

### Comparing `dask_sql-2023.2.0/dask_sql/physical/rel/logical/sample.py` & `dask_sql-2023.4.0/dask_sql/physical/rel/logical/sample.py`

 * *Files identical despite different names*

### Comparing `dask_sql-2023.2.0/dask_sql/physical/rel/logical/sort.py` & `dask_sql-2023.4.0/dask_sql/physical/rel/logical/sort.py`

 * *Files identical despite different names*

### Comparing `dask_sql-2023.2.0/dask_sql/physical/rel/logical/subquery_alias.py` & `dask_sql-2023.4.0/dask_sql/physical/rel/logical/subquery_alias.py`

 * *Files identical despite different names*

### Comparing `dask_sql-2023.2.0/dask_sql/physical/rel/logical/table_scan.py` & `dask_sql-2023.4.0/dask_sql/physical/rel/logical/table_scan.py`

 * *Files 2% similar despite different names*

```diff
@@ -58,17 +58,18 @@
     def _apply_projections(self, table_scan, dask_table, dc):
         # If the 'TableScan' instance contains projected columns only retrieve those columns
         # otherwise get all projected columns from the 'Projection' instance, which is contained
         # in the 'RelDataType' instance, aka 'row_type'
         df = dc.df
         cc = dc.column_container
         if table_scan.containsProjections():
-            field_specifications = (
-                table_scan.getTableScanProjects()
+            field_specifications = list(
+                map(cc.get_backend_by_frontend_name, table_scan.getTableScanProjects())
             )  # Assumes these are column projections only and field names match table column names
+
             df = df[field_specifications]
         else:
             field_specifications = [
                 str(f) for f in dask_table.getRowType().getFieldNames()
             ]
         cc = cc.limit_to(field_specifications)
         return DataContainer(df, cc)
```

### Comparing `dask_sql-2023.2.0/dask_sql/physical/rel/logical/union.py` & `dask_sql-2023.4.0/dask_sql/physical/rel/logical/union.py`

 * *Files identical despite different names*

### Comparing `dask_sql-2023.2.0/dask_sql/physical/rel/logical/values.py` & `dask_sql-2023.4.0/dask_sql/physical/rel/logical/values.py`

 * *Files identical despite different names*

### Comparing `dask_sql-2023.2.0/dask_sql/physical/rel/logical/window.py` & `dask_sql-2023.4.0/dask_sql/physical/rel/logical/window.py`

 * *Files 4% similar despite different names*

```diff
@@ -8,15 +8,14 @@
 import pandas as pd
 from pandas.api.indexers import BaseIndexer
 
 from dask_sql._compat import INDEXER_WINDOW_STEP_IMPLEMENTED
 from dask_sql.datacontainer import ColumnContainer, DataContainer
 from dask_sql.physical.rel.base import BaseRelPlugin
 from dask_sql.physical.rex.convert import RexConverter
-from dask_sql.physical.utils.groupby import get_groupby_with_nulls_cols
 from dask_sql.physical.utils.sort import sort_partition_func
 from dask_sql.utils import (
     LoggableDataFrame,
     make_pickable_without_dask_sql,
     new_temporary_column,
 )
 
@@ -244,37 +243,30 @@
     }
 
     def convert(self, rel: "LogicalPlan", context: "dask_sql.Context") -> DataContainer:
         (dc,) = self.assert_inputs(rel, 1, context)
 
         # Output to the right field names right away
         field_names = rel.getRowType().getFieldNames()
-        input_column_count = len(dc.column_container.columns)
         for window in rel.window().getGroups():
-            dc = self._apply_window(
-                rel, window, input_column_count, dc, field_names, context
-            )
+            dc = self._apply_window(rel, window, dc, field_names, context)
 
         # Finally, fix the output schema if needed
         df = dc.df
         cc = dc.column_container
-        cc = cc.limit_to(
-            cc.columns[input_column_count:] + cc.columns[0:input_column_count]
-        )
         cc = self.fix_column_to_row_type(cc, rel.getRowType())
         dc = DataContainer(df, cc)
         dc = self.fix_dtype_to_row_type(dc, rel.getRowType())
 
         return dc
 
     def _apply_window(
         self,
         rel,
         window,
-        input_column_count: int,
         dc: DataContainer,
         field_names: List[str],
         context: "dask_sql.Context",
     ):
         temporary_columns = []
 
         df = dc.df
@@ -284,20 +276,20 @@
         sort_columns, sort_ascending, sort_null_first = self._extract_ordering(
             rel, window, cc
         )
         logger.debug(
             f"Before applying the function, sorting according to {sort_columns}."
         )
 
-        df, group_columns = self._extract_groupby(df, rel, window, dc, context)
+        df, group_columns, temporary_columns = self._extract_groupby(
+            df, rel, window, dc, context
+        )
         logger.debug(
             f"Before applying the function, partitioning according to {group_columns}."
         )
-        # TODO: optimize by re-using already present columns
-        temporary_columns += group_columns
 
         operations, df = self._extract_operations(rel, window, df, dc, context)
         for _, _, cols in operations:
             temporary_columns += cols
 
         newly_created_columns = [new_column for _, new_column, _ in operations]
 
@@ -348,29 +340,28 @@
             upper_bound=upper_bound,
             operations=operations,
         )
 
         # TODO: That is a bit of a hack. We should really use the real column dtype
         meta = df._meta.assign(**{col: 0.0 for col in newly_created_columns})
 
-        df = df.groupby(group_columns).apply(
+        df = df.groupby(group_columns, dropna=False).apply(
             make_pickable_without_dask_sql(filled_map), meta=meta
         )
         logger.debug(
             f"Having created a dataframe {LoggableDataFrame(df)} after windowing. Will now drop {temporary_columns}."
         )
         df = df.drop(columns=temporary_columns).reset_index(drop=True)
 
         dc = DataContainer(df, cc)
         df = dc.df
         cc = dc.column_container
-
         for c in newly_created_columns:
             # the fields are in the correct order by definition
-            field_name = field_names[len(cc.columns) - input_column_count]
+            field_name = field_names[len(cc.columns)]
             cc = cc.add(field_name, c)
         dc = DataContainer(df, cc)
         logger.debug(
             f"Removed unneeded columns and registered new ones: {LoggableDataFrame(dc)}."
         )
         return dc
 
@@ -379,31 +370,28 @@
         df: dd.DataFrame,
         rel,
         window,
         dc: DataContainer,
         context: "dask_sql.Context",
     ) -> Tuple[dd.DataFrame, str]:
         """Prepare grouping columns we can later use while applying the main function"""
-        partition_keys = list(rel.window().getPartitionExprs(window))
+        partition_keys = rel.window().getPartitionExprs(window)
         if partition_keys:
             group_columns = [
-                df[dc.column_container.get_backend_by_frontend_name(o.column_name(rel))]
+                dc.column_container.get_backend_by_frontend_name(o.column_name(rel))
                 for o in partition_keys
             ]
-            group_columns = get_groupby_with_nulls_cols(df, group_columns)
-            group_columns = {
-                new_temporary_column(df): group_col for group_col in group_columns
-            }
+            temporary_columns = []
         else:
-            group_columns = {new_temporary_column(df): 1}
-
-        df = df.assign(**group_columns)
-        group_columns = list(group_columns.keys())
+            temp_col = new_temporary_column(df)
+            df = df.assign(**{temp_col: 1})
+            group_columns = [temp_col]
+            temporary_columns = [temp_col]
 
-        return df, group_columns
+        return df, group_columns, temporary_columns
 
     def _extract_ordering(
         self, rel, window, cc: ColumnContainer
     ) -> Tuple[str, str, str]:
         """Prepare sorting information we can later use while applying the main function"""
         logger.debug(
             "Error is about to be encountered, FIX me when bindings are available in subsequent PR"
```

### Comparing `dask_sql-2023.2.0/dask_sql/physical/rex/base.py` & `dask_sql-2023.4.0/dask_sql/physical/rex/base.py`

 * *Files identical despite different names*

### Comparing `dask_sql-2023.2.0/dask_sql/physical/rex/convert.py` & `dask_sql-2023.4.0/dask_sql/physical/rex/convert.py`

 * *Files 11% similar despite different names*

```diff
@@ -13,15 +13,16 @@
 
 logger = logging.getLogger(__name__)
 
 _REX_TYPE_TO_PLUGIN = {
     "RexType.Reference": "InputRef",
     "RexType.Call": "RexCall",
     "RexType.Literal": "RexLiteral",
-    "RexType.SubqueryAlias": "SubqueryAlias",
+    "RexType.Alias": "RexAlias",
+    "RexType.ScalarSubquery": "ScalarSubquery",
 }
 
 
 class RexConverter(Pluggable):
     """
     Helper to convert from rex to a python expression
```

### Comparing `dask_sql-2023.2.0/dask_sql/physical/rex/core/call.py` & `dask_sql-2023.4.0/dask_sql/physical/rex/core/call.py`

 * *Files identical despite different names*

### Comparing `dask_sql-2023.2.0/dask_sql/physical/rex/core/input_ref.py` & `dask_sql-2023.4.0/dask_sql/physical/rex/core/input_ref.py`

 * *Files identical despite different names*

### Comparing `dask_sql-2023.2.0/dask_sql/physical/rex/core/literal.py` & `dask_sql-2023.4.0/dask_sql/physical/rex/core/literal.py`

 * *Files identical despite different names*

### Comparing `dask_sql-2023.2.0/dask_sql/physical/rex/core/subquery.py` & `dask_sql-2023.4.0/dask_sql/physical/rex/core/subquery.py`

 * *Files 18% similar despite different names*

```diff
@@ -7,22 +7,22 @@
 from dask_sql.physical.rex.base import BaseRexPlugin
 
 if TYPE_CHECKING:
     import dask_sql
     from dask_planner.rust import Expression, LogicalPlan
 
 
-class RexSubqueryAliasPlugin(BaseRexPlugin):
+class RexScalarSubqueryPlugin(BaseRexPlugin):
     """
-    A RexSubqueryAliasPlugin is an expression, which references a Subquery.
+    A RexScalarSubqueryPlugin is an expression, which references a Subquery.
     This plugin is thin on logic, however keeping with previous patterns
     we use the plugin approach instead of placing the logic inline
     """
 
-    class_name = "SubqueryAlias"
+    class_name = "ScalarSubquery"
 
     def convert(
         self,
         rel: "LogicalPlan",
         rex: "Expression",
         dc: DataContainer,
         context: "dask_sql.Context",
```

### Comparing `dask_sql-2023.2.0/dask_sql/physical/utils/filter.py` & `dask_sql-2023.4.0/dask_sql/physical/utils/filter.py`

 * *Files identical despite different names*

### Comparing `dask_sql-2023.2.0/dask_sql/physical/utils/groupby.py` & `dask_sql-2023.4.0/dask_sql/physical/utils/groupby.py`

 * *Files identical despite different names*

### Comparing `dask_sql-2023.2.0/dask_sql/physical/utils/ml_classes.py` & `dask_sql-2023.4.0/dask_sql/physical/utils/ml_classes.py`

 * *Files identical despite different names*

### Comparing `dask_sql-2023.2.0/dask_sql/physical/utils/sort.py` & `dask_sql-2023.4.0/dask_sql/physical/utils/sort.py`

 * *Files identical despite different names*

### Comparing `dask_sql-2023.2.0/dask_sql/physical/utils/statistics.py` & `dask_sql-2023.4.0/dask_sql/physical/utils/statistics.py`

 * *Files 2% similar despite different names*

```diff
@@ -83,26 +83,26 @@
         layer = None
 
     # Make sure we are dealing with a
     # ParquetFunctionWrapper-based DataFrameIOLayer
     if not isinstance(layer, DataFrameIOLayer) or not isinstance(
         layer.io_func, ParquetFunctionWrapper
     ):
-        logger.warning(
+        logger.debug(
             f"Could not extract Parquet statistics from {ddf}."
             f"\nAttempted IO layer: {layer}"
         )
         return None
 
     # Collect statistics using layer information
     parts = layer.inputs
     fs = layer.io_func.fs
     engine = layer.io_func.engine
     if not issubclass(engine, ArrowDatasetEngine):
-        logger.warning(
+        logger.debug(
             f"Could not extract Parquet statistics from {ddf}."
             f"\nUnsupported parquet engine: {engine}"
         )
         return None
 
     # Set default
     if parallel is None:
@@ -112,16 +112,17 @@
     if parallel:
         # Group parts corresponding to the same file.
         # A single task should always parse statistics
         # for all these parts at once (since they will
         # all be in the same footer)
         groups = defaultdict(list)
         for part in parts:
-            path = part.get("piece")[0]
-            groups[path].append(part)
+            for p in [part] if isinstance(part, dict) else part:
+                path = p.get("piece")[0]
+                groups[path].append(p)
         group_keys = list(groups.keys())
 
         # Compute and return flattened result
         func = delayed(_read_partition_stats_group)
         result = dask.compute(
             [
                 func(
```

### Comparing `dask_sql-2023.2.0/dask_sql/server/app.py` & `dask_sql-2023.4.0/dask_sql/server/app.py`

 * *Files 4% similar despite different names*

```diff
@@ -2,15 +2,14 @@
 import logging
 from argparse import ArgumentParser
 from uuid import uuid4
 
 import dask.distributed
 import uvicorn
 from fastapi import FastAPI, HTTPException, Request
-from nest_asyncio import apply
 from uvicorn import Config, Server
 
 from dask_sql.context import Context
 from dask_sql.server.presto_jdbc import create_meta_data
 from dask_sql.server.responses import DataResults, ErrorResults, QueryResults
 
 app = FastAPI()
@@ -184,35 +183,30 @@
         Note:
             When running in a jupyter notebook without blocking,
             it is not possible to access the SQL server from within the
             notebook, e.g. using sqlalchemy.
             Doing so will deadlock infinitely.
 
     """
+    if context is None:
+        context = Context()
     _init_app(app, context=context, client=client)
     if jdbc_metadata:
         create_meta_data(context)
 
     if startup:
         app.c.sql("SELECT 1 + 1").compute()
 
     config = Config(app, host=host, port=port, log_level=log_level)
     server = Server(config=config)
 
-    loop = asyncio.get_event_loop()
     if blocking:
-        if loop and loop.is_running():
-            apply(loop=loop)
-
         server.run()
     else:
-        if not loop or not loop.is_running():
-            raise AttributeError(
-                "blocking=True needs a running event loop (e.g. in a jupyter notebook)"
-            )
+        loop = asyncio.get_event_loop()
         loop.create_task(server.serve())
         context.sql_server = server
 
 
 def main():  # pragma: no cover
     """
     CLI version of the :func:`run_server` function.
@@ -272,15 +266,15 @@
 
 
 def _init_app(
     app: FastAPI,
     context: Context = None,
     client: dask.distributed.Client = None,
 ):
-    app.c = context or Context()
+    app.c = context
     app.future_list = {}
 
     try:
         client = client or dask.distributed.Client.current()
     except ValueError:
         client = dask.distributed.Client()
     app.client = client
```

### Comparing `dask_sql-2023.2.0/dask_sql/server/presto_jdbc.py` & `dask_sql-2023.4.0/dask_sql/server/presto_jdbc.py`

 * *Files identical despite different names*

### Comparing `dask_sql-2023.2.0/dask_sql/server/responses.py` & `dask_sql-2023.4.0/dask_sql/server/responses.py`

 * *Files 4% similar despite different names*

```diff
@@ -1,11 +1,12 @@
 import uuid
 
 import dask.dataframe as dd
 import numpy as np
+import pandas as pd
 from fastapi import Request
 
 from dask_sql.mappings import python_to_sql_type
 
 
 class StageStats:
     def __init__(self):
@@ -60,21 +61,26 @@
         self.stats = StatementStats()
         self.warnings = []
 
 
 class DataResults(QueryResults):
     @staticmethod
     def get_column_description(df):
-        sql_types = [str(python_to_sql_type(t)) for t in df.dtypes]
+        sql_types = [str(python_to_sql_type(t)).lower() for t in df.dtypes]
         column_names = df.columns
         return [
             {
                 "name": column_name,
-                "type": sql_type.lower(),
-                "typeSignature": {"rawType": sql_type.lower(), "arguments": []},
+                "type": sql_type,
+                "typeSignature": {
+                    "rawType": sql_type,
+                    "arguments": []
+                    if sql_type not in ("char", "varchar")
+                    else [{"kind": "LONG", "value": 10}],
+                },
             }
             for column_name, sql_type in zip(column_names, sql_types)
         ]
 
     @staticmethod
     def get_data_description(df):
         if hasattr(df, "to_pandas"):
@@ -83,15 +89,17 @@
             DataResults.convert_row(row)
             for row in df.itertuples(index=False, name=None)
         ]
 
     @staticmethod
     def convert_cell(cell):
         try:
-            if np.isnan(cell):  # pragma: no cover
+            if pd.isna(cell):
+                return None
+            elif np.isnan(cell):  # pragma: no cover
                 return "NaN"
             elif np.isposinf(cell):
                 return "+Infinity"
             elif np.isneginf(cell):  # pragma: no cover
                 return "-Infinity"
         except TypeError:  # pragma: no cover
             pass
@@ -127,14 +135,15 @@
 class QueryError:
     def __init__(self, error: Exception):
         self.message = str(error)
         self.errorCode = 0
         self.errorName = str(type(error))
         self.errorType = "USER_ERROR"
 
-        try:
-            self.errorLocation = {
-                "lineNumber": error.from_line + 1,
-                "columnNumber": error.from_col + 1,
-            }
-        except AttributeError:  # pragma: no cover
-            pass
+        # FIXME: ParserErrors currently don't contain information on where the syntax error occurred
+        # try:
+        #     self.errorLocation = {
+        #         "lineNumber": error.from_line + 1,
+        #         "columnNumber": error.from_col + 1,
+        #     }
+        # except AttributeError:  # pragma: no cover
+        #     pass
```

### Comparing `dask_sql-2023.2.0/dask_sql/sql-schema.yaml` & `dask_sql-2023.4.0/dask_sql/sql-schema.yaml`

 * *Files identical despite different names*

### Comparing `dask_sql-2023.2.0/dask_sql/utils.py` & `dask_sql-2023.4.0/dask_sql/utils.py`

 * *Files identical despite different names*

### Comparing `dask_sql-2023.2.0/dask_sql.egg-info/PKG-INFO` & `dask_sql-2023.4.0/dask_sql.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: dask-sql
-Version: 2023.2.0
+Version: 2023.4.0
 Summary: SQL query layer for Dask
 Home-page: https://github.com/dask-contrib/dask-sql/
 Maintainer: Nils Braun
 Maintainer-email: nilslennartbraun@gmail.com
 License: MIT
 Requires-Python: >=3.8
 Description-Content-Type: text/markdown
```

### Comparing `dask_sql-2023.2.0/dask_sql.egg-info/SOURCES.txt` & `dask_sql-2023.4.0/dask_sql.egg-info/SOURCES.txt`

 * *Files 0% similar despite different names*

```diff
@@ -52,22 +52,23 @@
 dask_planner/src/sql/logical/join.rs
 dask_planner/src/sql/logical/limit.rs
 dask_planner/src/sql/logical/predict_model.rs
 dask_planner/src/sql/logical/projection.rs
 dask_planner/src/sql/logical/repartition_by.rs
 dask_planner/src/sql/logical/show_columns.rs
 dask_planner/src/sql/logical/show_models.rs
-dask_planner/src/sql/logical/show_schema.rs
+dask_planner/src/sql/logical/show_schemas.rs
 dask_planner/src/sql/logical/show_tables.rs
 dask_planner/src/sql/logical/sort.rs
 dask_planner/src/sql/logical/subquery_alias.rs
 dask_planner/src/sql/logical/table_scan.rs
 dask_planner/src/sql/logical/use_schema.rs
 dask_planner/src/sql/logical/window.rs
 dask_planner/src/sql/optimizer/filter_columns_post_join.rs
+dask_planner/src/sql/optimizer/join_reorder.rs
 dask_planner/src/sql/types/rel_data_type.rs
 dask_planner/src/sql/types/rel_data_type_field.rs
 dask_sql/__init__.py
 dask_sql/_compat.py
 dask_sql/_version.py
 dask_sql/cmd.py
 dask_sql/config.py
@@ -112,17 +113,17 @@
 dask_sql/physical/rel/custom/distributeby.py
 dask_sql/physical/rel/custom/drop_model.py
 dask_sql/physical/rel/custom/drop_schema.py
 dask_sql/physical/rel/custom/drop_table.py
 dask_sql/physical/rel/custom/export_model.py
 dask_sql/physical/rel/custom/metrics.py
 dask_sql/physical/rel/custom/predict_model.py
-dask_sql/physical/rel/custom/schemas.py
 dask_sql/physical/rel/custom/show_columns.py
 dask_sql/physical/rel/custom/show_models.py
+dask_sql/physical/rel/custom/show_schemas.py
 dask_sql/physical/rel/custom/show_tables.py
 dask_sql/physical/rel/custom/use_schema.py
 dask_sql/physical/rel/custom/wrappers.py
 dask_sql/physical/rel/logical/__init__.py
 dask_sql/physical/rel/logical/aggregate.py
 dask_sql/physical/rel/logical/cross_join.py
 dask_sql/physical/rel/logical/empty.py
@@ -138,14 +139,15 @@
 dask_sql/physical/rel/logical/union.py
 dask_sql/physical/rel/logical/values.py
 dask_sql/physical/rel/logical/window.py
 dask_sql/physical/rex/__init__.py
 dask_sql/physical/rex/base.py
 dask_sql/physical/rex/convert.py
 dask_sql/physical/rex/core/__init__.py
+dask_sql/physical/rex/core/alias.py
 dask_sql/physical/rex/core/call.py
 dask_sql/physical/rex/core/input_ref.py
 dask_sql/physical/rex/core/literal.py
 dask_sql/physical/rex/core/subquery.py
 dask_sql/physical/utils/__init__.py
 dask_sql/physical/utils/filter.py
 dask_sql/physical/utils/groupby.py
```

### Comparing `dask_sql-2023.2.0/setup.cfg` & `dask_sql-2023.4.0/setup.cfg`

 * *Files identical despite different names*

### Comparing `dask_sql-2023.2.0/setup.py` & `dask_sql-2023.4.0/setup.py`

 * *Files 13% similar despite different names*

```diff
@@ -38,24 +38,24 @@
             path="dask_planner/Cargo.toml",
             debug=debug_build,
         )
     ],
     python_requires=">=3.8",
     setup_requires=sphinx_requirements,
     install_requires=[
-        "dask[dataframe,distributed]>=2022.3.0,<=2023.1.1",
+        "dask[dataframe]>=2022.3.0,<=2023.3.2",
+        "distributed>=2022.3.0,<2023.3.3.0a0",
         "pandas>=1.4.0",
         # FIXME: handling is needed for httpx-based fastapi>=0.87.0
         "fastapi>=0.69.0,<0.87.0",
         "uvicorn>=0.13.4",
         "tzlocal>=2.1",
         "prompt_toolkit>=3.0.8",
         "pygments>=2.7.1",
         "tabulate",
-        "nest-asyncio",
     ],
     extras_require={
         "dev": [
             "pytest>=6.0.1",
             "pytest-cov>=2.10.1",
             "mock>=4.0.3",
             "sphinx>=3.2.1",
```

### Comparing `dask_sql-2023.2.0/versioneer.py` & `dask_sql-2023.4.0/versioneer.py`

 * *Files identical despite different names*

